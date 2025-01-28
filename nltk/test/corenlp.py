import unittest
from nltk.parse.corenlp import CoreNLPParser

class TestCoreNLPTagger(unittest.TestCase):
    def setUp(self):
        self.parser = CoreNLPParser(url='http://corenlp.run', tagtype='ner')

    def test_tag_numbers(self):
        sent = ['my', 'phone', 'number', 'is', '1111', '1111', '1111']
        expected_output = [('my', 'O'), ('phone', 'O'), ('number', 'O'),
                           ('is', 'O'), ('1111', 'NUMBER'), ('1111', 'NUMBER'), ('1111', 'NUMBER')]
        self.assertEqual(self.parser.tag(sent), expected_output)

if __name__ == '__main__':
    unittest.main()

