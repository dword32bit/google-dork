import unittest
import urllib.parse
from google_dork.main import GoogleDork

class TestGoogleDork(unittest.TestCase):
    def setUp(self):
        self.dork = GoogleDork(
            domain="example.com",
            filetype="pdf",
            intext="confidential"
        )

    def test_build_query(self):
        query = urllib.parse.unquote(self.dork.build_query())
        self.assertIn("site:example.com", query)
        self.assertIn("filetype:pdf", query)
        self.assertIn('intext:"confidential"', query)

    def test_empty_query(self):
        dork = GoogleDork()
        self.assertEqual(dork.build_query(), "")

if __name__ == '__main__':
    unittest.main()
