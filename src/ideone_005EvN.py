# your code goes here
""" base58 encoding / decoding functions """
import unittest
 
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
base_count = len(alphabet)
		
def encode(num):
	""" Returns num in a base58-encoded string """
	encode = ''
	
	if (num < 0):
		return ''
	
	while (num >= base_count):	
		mod = num % base_count
		encode = alphabet[mod] + encode
		num = num / base_count
 
	if (num):
		encode = alphabet[num] + encode
 
	return encode
 
def decode(s):
	""" Decodes the base58-encoded string s into an integer """
	decoded = 0
	multi = 1
	s = s[::-1]
	for char in s:
		decoded += multi * alphabet.index(char)
		multi = multi * base_count
		
	return decoded
 
class Base58Tests(unittest.TestCase):
 
  def test_alphabet_length(self):
    self.assertEqual(58, len(alphabet))
 
  def test_encode_10002343_returns_Tgmc(self):
    result = encode(10002343)
    self.assertEqual('Tgmc', result)
 
  def test_decode_Tgmc_returns_10002343(self):
    decoded = decode('Tgmc')
    self.assertEqual(10002343, decoded)
 
  def test_encode_1000_returns_if(self):
    result = encode(1000)
    self.assertEqual('if', result)
 
  def test_decode_if_returns_1000(self):
    decoded = decode('if')
    self.assertEqual(1000, decoded)
 
  def test_encode_zero_returns_empty_string(self):
    self.assertEqual('', encode(0))
 
  def test_encode_negative_number_returns_empty_string(self):
    self.assertEqual('', encode(-100))
 
if __name__ == '__main__':
  #print encode(int("00B94BA6C51B3D8372D82FDE5DC78773D960B5A82FCDAC8181",16))
  print hex(decode("Wh4bh"))