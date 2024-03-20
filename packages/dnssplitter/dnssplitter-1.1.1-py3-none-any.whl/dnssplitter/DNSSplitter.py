#!/usr/bin/python3

"""A python class wrapper around the Public Suffix List (PSL) data,
   which can be found at https://github.com/publicsuffix/list.

Usage:

    import dnssplitter
    splitter = dnssplitter.DNSSplitter()

    splitter.init_tree() # uses internal data
    # or load your own:
    # splitter.load_psl_file("/path/to/public_suffix_list.dat")
    results = splitter.search_tree("www.foo.co.uk")

    # Returns an array of [prefix, registered_domain, public_point]:
    # results == ['www', 'foo.co.uk', 'co.uk']
"""

import os
import re

class DNSSplitter(object):
    """A python class wrapper around the Public Suffix List (PSL) data,
       which can be found at https://github.com/publicsuffix/list.

    Usage:

        import dnssplitter
        splitter = dnssplitter.DNSSplitter()

        splitter.init_tree() # uses internal data
        # or load your own:
        # splitter.load_psl_file("/path/to/public_suffix_list.dat")
        results = splitter.search_tree("www.foo.co.uk")

        # Returns an array of [prefix, registered_domain, public_point]:
        # results == ['www', 'foo.co.uk', 'co.uk']
    """
    _tree = None
    
    def __init__(self):
        pass

    @property
    def tree(self):
        """A python dict structure containing all the data from a 
           public suffix list extraction"""
        if not self._tree:
            self.init_tree()
        
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Set the internal tree structure"""
        self._tree = tree
    
    def search_tree(self, name):
        """Given a tree structure obtained from get_psl_tree(),
        searches it for the split point one label above the 
        public suffix list split point,
        and the prefix at the start of a domain name.

        Returns an array of [prefix, suffix, public_point]

        For example:

            www.foo.bar.co.uk

        would return

            ['www.foo','bar.co.uk', 'co.uk']

        as 'co.uk' is a registered public suffix.

        If the last label does not fall within the root servers at all,
        'None' is returned instead.
        """

        if not name or len(name) == 0:
            return None
        
        # strip starting and trailing dots
        if name[-1] == '.':
            name = name[:-1]
        if name[:1] == '.':
            name = name[1:]

        # convert to lower case and split to an array
        name = name.lower()
        parts = name.split(".")
        
        # does the last label even exist at all?
        if parts[len(parts) - 1] not in self.tree:
            return None

        target = ""
        node = self.tree

        # iterate over the rest of the nodes traversing the 'node' tree,
        # all the while building the 'target' string:

        for i in range(len(parts) - 1, -1, -1):
            if parts[i] in node:
                node = node[parts[i]]
                target = parts[i] + "." + target
            else:
                # if a wildcard exists in the tree, then
                # the node we're staring at is included in the break point
                if node and '*' in node: # everything below this point is a PSL
                    ps = ".".join(parts[i:])

                    if i <= 0: # exactly the psl point
                        # check to see if there is a ! exception entry for this node
                        if node and ("!" + parts[0]) in node:
                            # so now the entire domain is the current psl
                            registered_domain = ps
                            ps = ".".join(parts[i+1:])
                            prefix = ".".join(parts[0:i])
                            return [prefix, registered_domain, ps]
                        else:
                            return ['','',ps]
                    else:
                        if node and ("!" + parts[i]) in node:
                            registered_domain = ps
                            ps = ".".join(parts[i+1:])
                            prefix = ".".join(parts[0:i])
                            return [prefix, registered_domain, ps]
                        i -= 1
                    prefix = ".".join(parts[0:i]) # found split point
                    registered_domain = parts[i] + "." + ps
                    return [prefix, registered_domain, ps]

                # did we even get anywhere down the tree?
                if i == len(parts):
                    return None # not under a TLD at all

                # create the results:
                # from label1.label2.domain.in.psl:
                #    [ label1.label2 , domain.in.psl , in.psl ]
                prefix = ".".join(parts[0:i]) # found split point
                ps = ".".join(parts[i+1:])
                registered_domain = parts[i] + "." + ps
                return [prefix, registered_domain, ps]

        # if we're exactly at prefix split, return it
        if target == name + ".":
            return ['', '', name]

        return None

    def init_tree(self, domains = None):
        """Initializes the tree structure from an internal saved 
        copy of the PSL."""
        if not domains:
            domains = get_domains()
    
        tree = {}
        for domain in domains:
            parts = domain.split('.')
            node = tree
            for i in range(len(parts) - 1, -1, -1):
                if parts[i] not in node:
                    node[parts[i]] = {}
                node = node[parts[i]]

        self._tree = tree
        return tree

    def load_psl_file(self, filename):
        """Loads the PSL data from a public suffix list .dat filename,
           which can be found at https://github.com/publicsuffix/list"""
        filename = os.path.expanduser(filename)
        fileh = open(filename, "r")
        return(self.load_psl_fileh(fileh))

    def load_psl_fileh(self, fileh):
        """Loads the PSL data from a public suffix list .dat file handle,
           which can be found at https://github.com/publicsuffix/list"""
        commentmatch = re.compile(".*//.*")
        namematch = re.compile(".*[a-zA-Z0-9].*")
        psl = []
        nonascii = re.compile(".*([^-*!._a-z0-9A-Z ]).*") # XXX

        if not fileh:
            print("can't find the public suffix list")
            return(-1)

        for line in fileh:
            # if line[0] == '!':
            #     import pdb; pdb.set_trace()

            line = line.rstrip()
            if commentmatch.match(line):
                pass
            if nonascii.match(line):
                x = nonascii.match(line)
                #print "nope: " + x.group(1)
                pass
            elif namematch.match(line):
                psl.append(line)

        # sort the public suffix list so that items with more '.'s come first
        # XXX: with a tree I don't think we need to sort;
        # (the regexp likely needs it though)
        # need a python3 cmp equiv to sort by length first
        #psl.sort(key=_psl_sort_key)
        self.init_tree(psl)
        return psl


    def split_fsdb(self, inh, outh, keys):
        """Accepts input streams, converts them to pyfsdb objects, and adds
        new dns-split output keys based on input keys and sends the
        results as a new FSDB file to the output handle.
        """
        import pyfsdb

        inh = pyfsdb.Fsdb(file_handle=inh)
        outh = pyfsdb.Fsdb(out_file_handle=outh)

        outcols = list(inh.column_names)
        for key in keys:
            outcols.extend([key + '_prefix', key + '_domain', key + '_suffix'])
        outh.column_names = outcols

        key_cols = inh.get_column_numbers(keys)

        for row in inh:
            for key in key_cols:
                name = row[key]
                results = self.search_tree(name)

                if results:
                    row.extend(results)
                else:
                    row.extend(['','',''])

            outh.append(row)

        outh.close()
        
        
def psl_sorter(a, b):
    if a == b:
        return 0

    adots = a.split(".")
    bdots = b.split(".")
    if len(adots) > len(bdots):
        return -1
    elif len(adots) < len(bdots):
        return 1
    
    if a < b:
        return -1
    return 1

def _psl_sort_key(a):
    dots = a.split(".")
    # this hack won't work for len > 9
    a = str(len(dots)) + a

def get_domains():
    import dnssplitter.domains
    return dnssplitter.domains.DOMAINS

def psl_search_tree(tree, name):
    """Obsolete; use the class instead"""
    splitter = DNSSplitter()
    splitter.tree = tree
    return splitter.search_tree(name)

def get_psl_tree():
    """returns an ordered list of domains to dive into to check against
    the public suffix list.  Use psl_search_tree to check for matches."""

    """Obsolete; use the class instead"""
    splitter = DNSSplitter()
    return splitter.tree



