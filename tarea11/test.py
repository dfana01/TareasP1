import unittest
from main import DirectAddressTable


class DirectAccessTableTest(unittest.TestCase):
    def test_insert(self):
        dat = DirectAddressTable()
        dat.insert("asdgw")
        self.assertEqual(dat.search("asdgw"), "asdgw")

    def test_delete(self):
        dat = DirectAddressTable()
        dat.insert("asdgw")
        dat.delete("asdgw")
        self.assertEqual(dat.search("asdgw"), None)

    def test_search(self):
        dat = DirectAddressTable()
        dat.insert("ardgw")
        dat.insert("asdgf")
        dat.insert("asdgw")
        dat.insert("asdgw")
        self.assertEqual(dat.search("asdgw"), "asdgw")

    def test_key_no_more_than_5(self):
        dat = DirectAddressTable()
        try:
            dat.insert("ardgwa")
        except Exception as err:
            self.assertTrue('Key need to be 5 letter' in str(err))

    def test_only_letter_key(self):
        dat = DirectAddressTable()
        try:
            dat.insert("ardgwa134")
        except Exception as err:
            self.assertTrue('The key needs to compose all by letters' in str(err))


if __name__ == '__main__':
    unittest.main()
