# to run : pytest test.py

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

import skein_hash
import weakref
import binascii
from binascii import unhexlify, hexlify

import unittest

# block 211 for livenet.
best_hash_value = '00000011d6202b031df083700a5c11138bc05d8eec7e01757fc816974dc85c78'
header_hex_value = "03000000ea3f8b2d4f24d71b30a5941ad42bac191a147c41638fa39947d79ac4080000006daea14b9fdd2fe650a699f84b0c381e478b1897788bcd07ace0130c9d18614b74edd85dacb9191da5c99900"
 
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.my_best_hash = best_hash_value
        self.my_block_header = unhexlify(header_hex_value)

    def test_skein_hash(self):
        self.module_pow_hash = hexlify(skein_hash.getPoWHash(self.my_block_header)[::-1]).decode('utf-8')
        self.assertEqual(self.module_pow_hash, self.my_best_hash)

if __name__ == '__main__':
    unittest.main()

