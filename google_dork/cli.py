import argparse
import sys
from .main import GoogleDork

def main():
    parser = argparse.ArgumentParser(
        description="Google Dorking Tool - Search Google with advanced operators",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -d example.com -f pdf
  %(prog)s -d example.com -t "confidential"
  %(prog)s -u "admin" -d .gov
  %(prog)s --intext "password" --domain example.com
        """
    )

    parser.add_argument('-d', '--domain', help='Target domain to search')
    parser.add_argument('-f', '--filetype', help='Specific file type to search for (pdf, doc, etc.)')
    parser.add_argument('-x', '--intext', help='Search for specific text within pages')
    parser.add_argument('-t', '--intitle', help='Search for specific text in page titles')
    parser.add_argument('-u', '--inurl', help='Search for specific text in URLs')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    if not any([args.domain, args.filetype, args.intext, args.intitle, args.inurl]):
        parser.print_help()
        sys.exit(1)

    try:
        dork = GoogleDork(
            domain=args.domain,
            filetype=args.filetype,
            intext=args.intext,
            intitle=args.intitle,
            inurl=args.inurl
        )

        if args.debug:
            print("Debug Mode: ON")
            print("Query Parameters:")
            print(f"Domain: {args.domain}")
            print(f"Filetype: {args.filetype}")
            print(f"Intext: {args.intext}")
            print(f"Intitle: {args.intitle}")
            print(f"Inurl: {args.inurl}")

        results = dork.search()
        dork.display_results(results)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        if args.debug:
            raise
        sys.exit(1)

if __name__ == "__main__":
    main()
