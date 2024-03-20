from argparse import ArgumentParser, FileType, ArgumentDefaultsHelpFormatter
import sys
import dnssplitter

"""Splits DNS names in an incoming FSDB file into public suffix list
components (prefix, domain-name and suffix)."""

def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            description=__doc__,
	                        epilog="Exmaple Usage: ")

    parser.add_argument("-k", "--name-keys", default=["name"],
                        type=str, nargs="*",
                        help="The dns key columns to split on.  The key will be a prefix in the output columns with _prefix, _domain_name and _suffix as output columns.")

    parser.add_argument("input_file", type=FileType('r'),
                        nargs='?', default=sys.stdin,
                        help="")

    parser.add_argument("output_file", type=FileType('w'),
                        nargs='?', default=sys.stdout,
                        help="")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    splitter = dnssplitter.DNSSplitter()
    splitter.init_tree(0)

    splitter.split_fsdb(args.input_file, args.output_file, args.name_keys)

if __name__ == "__main__":
    main()
