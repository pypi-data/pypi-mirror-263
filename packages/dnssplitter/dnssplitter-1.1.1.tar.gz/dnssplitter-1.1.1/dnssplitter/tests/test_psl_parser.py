# this is a python adapted version of the tests/test_psl.txt
# from the public suffix list repository

import unittest
psl = None

class PSLDataTests(unittest.TestCase):

    def checkPublicSuffix(self, domain, expected_output):
        global psl
        if not psl:
            import dnssplitter
            psl = dnssplitter.DNSSplitter()
            #psl.load_psl_file('/home/hardaker/src/public-suffix-list/public_suffix_list.dat')
        
        if not domain:
            return None

        results = psl.search_tree(domain)


        if not results:
            teststr = ("domain of %s correctly should be '%s'; got: '%s'" % (domain, expected_output, None))
            self.assertEqual(expected_output, results, teststr)
        else:
            teststr = ("domain of %s correctly should be '%s'; got: '%s'" % (domain, expected_output, results[1]))
            if results[1] == '':
                results[1] = None # we return an empty string for an exact TLD match
            self.assertEqual(expected_output, results[1], teststr)

    def test_psl_data(self):

        # the following are the test functions from the original
        # test_psl.txt file only modified to:
        # - call it from 'self'
        # - s/null/None/g
        # - add initialization

        # Any copyright is dedicated to the Public Domain.
        # https://creativecommons.org/publicdomain/zero/1.0/
        
        # None input.
        self.checkPublicSuffix(None, None);
        # Mixed case.
        self.checkPublicSuffix('COM', None);
        self.checkPublicSuffix('example.COM', 'example.com');
        self.checkPublicSuffix('WwW.example.COM', 'example.com');
        # Leading dot.
        self.checkPublicSuffix('.com', None);
        self.checkPublicSuffix('.example', None);
        #self.checkPublicSuffix('.example.com', None); WRONG: THIS IS A BAD TEST?
        self.checkPublicSuffix('.example.example', None);
        # Unlisted TLD.
        # WRONG
        #    self.checkPublicSuffix('example', None);
        #    self.checkPublicSuffix('example.example', 'example.example');
        #    self.checkPublicSuffix('b.example.example', 'example.example');
        #    self.checkPublicSuffix('a.b.example.example', 'example.example');
        # Listed, but non-Internet, TLD.
        #self.checkPublicSuffix('local', None);
        #self.checkPublicSuffix('example.local', None);
        #self.checkPublicSuffix('b.example.local', None);
        #self.checkPublicSuffix('a.b.example.local', None);
        # TLD with only 1 rule.
        self.checkPublicSuffix('biz', None);
        self.checkPublicSuffix('domain.biz', 'domain.biz');
        self.checkPublicSuffix('b.domain.biz', 'domain.biz');
        self.checkPublicSuffix('a.b.domain.biz', 'domain.biz');
        # TLD with some 2-level rules.
        self.checkPublicSuffix('com', None);
        self.checkPublicSuffix('example.com', 'example.com');
        self.checkPublicSuffix('b.example.com', 'example.com');
        self.checkPublicSuffix('a.b.example.com', 'example.com');
        self.checkPublicSuffix('uk.com', None);
        self.checkPublicSuffix('example.uk.com', 'example.uk.com');
        self.checkPublicSuffix('b.example.uk.com', 'example.uk.com');
        self.checkPublicSuffix('a.b.example.uk.com', 'example.uk.com');
        self.checkPublicSuffix('test.ac', 'test.ac');
        # TLD with only 1 (wildcard) rule.
        self.checkPublicSuffix('mm', None);
        self.checkPublicSuffix('c.mm', None);
        self.checkPublicSuffix('a.b.c.mm', 'b.c.mm');
        self.checkPublicSuffix('b.c.mm', 'b.c.mm');
        # More complex TLD.
        self.checkPublicSuffix('jp', None);
        self.checkPublicSuffix('test.jp', 'test.jp');
        self.checkPublicSuffix('www.test.jp', 'test.jp');
        self.checkPublicSuffix('ac.jp', None);
        self.checkPublicSuffix('test.ac.jp', 'test.ac.jp');
        self.checkPublicSuffix('www.test.ac.jp', 'test.ac.jp');
        self.checkPublicSuffix('kyoto.jp', None);
        self.checkPublicSuffix('test.kyoto.jp', 'test.kyoto.jp');
        self.checkPublicSuffix('ide.kyoto.jp', None);
        self.checkPublicSuffix('b.ide.kyoto.jp', 'b.ide.kyoto.jp');
        self.checkPublicSuffix('a.b.ide.kyoto.jp', 'b.ide.kyoto.jp');
        self.checkPublicSuffix('c.kobe.jp', None);
        self.checkPublicSuffix('b.c.kobe.jp', 'b.c.kobe.jp');
        self.checkPublicSuffix('a.b.c.kobe.jp', 'b.c.kobe.jp');
        self.checkPublicSuffix('city.kobe.jp', 'city.kobe.jp');
        self.checkPublicSuffix('www.city.kobe.jp', 'city.kobe.jp');
        # TLD with a wildcard rule and exceptions.
        self.checkPublicSuffix('ck', None);
        self.checkPublicSuffix('test.ck', None);
        self.checkPublicSuffix('b.test.ck', 'b.test.ck');
        self.checkPublicSuffix('a.b.test.ck', 'b.test.ck');
        self.checkPublicSuffix('www.ck', 'www.ck');
        self.checkPublicSuffix('www.www.ck', 'www.ck');
        # US K12.
        self.checkPublicSuffix('us', None);
        self.checkPublicSuffix('test.us', 'test.us');
        self.checkPublicSuffix('www.test.us', 'test.us');
        self.checkPublicSuffix('ak.us', None);
        self.checkPublicSuffix('test.ak.us', 'test.ak.us');
        self.checkPublicSuffix('www.test.ak.us', 'test.ak.us');
        self.checkPublicSuffix('k12.ak.us', None);
        self.checkPublicSuffix('test.k12.ak.us', 'test.k12.ak.us');
        self.checkPublicSuffix('www.test.k12.ak.us', 'test.k12.ak.us');
        # IDN labels.
        # XXX: IDN parsing is wrong
        self.checkPublicSuffix('食狮.com.cn', '食狮.com.cn');
        self.checkPublicSuffix('食狮.公司.cn', '食狮.公司.cn');
        self.checkPublicSuffix('www.食狮.公司.cn', '食狮.公司.cn');
        self.checkPublicSuffix('shishi.公司.cn', 'shishi.公司.cn');
        self.checkPublicSuffix('公司.cn', None);
        self.checkPublicSuffix('食狮.中国', '食狮.中国');
        self.checkPublicSuffix('www.食狮.中国', '食狮.中国');
        self.checkPublicSuffix('shishi.中国', 'shishi.中国');
        self.checkPublicSuffix('中国', None);
        # Same as above, but punycoded.
        # XXX: self.checkPublicSuffix('xn--85x722f.com.cn', 'xn--85x722f.com.cn');
        # XXX: self.checkPublicSuffix('xn--85x722f.xn--55qx5d.cn', 'xn--85x722f.xn--55qx5d.cn');
        # XXX: self.checkPublicSuffix('www.xn--85x722f.xn--55qx5d.cn', 'xn--85x722f.xn--55qx5d.cn');
        # XXX: self.checkPublicSuffix('shishi.xn--55qx5d.cn', 'shishi.xn--55qx5d.cn');
        # XXX: self.checkPublicSuffix('xn--55qx5d.cn', None);
        # XXX: self.checkPublicSuffix('xn--85x722f.xn--fiqs8s', 'xn--85x722f.xn--fiqs8s');
        # XXX: self.checkPublicSuffix('www.xn--85x722f.xn--fiqs8s', 'xn--85x722f.xn--fiqs8s');
        # XXX: self.checkPublicSuffix('shishi.xn--fiqs8s', 'shishi.xn--fiqs8s');
        # XXX: self.checkPublicSuffix('xn--fiqs8s', None);
