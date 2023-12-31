# code from Pluralsight

from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64

class AESCrypto:

    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode())  # note the difference of this line comparing to the pluralsight code, we need to do encode() to turn this value into bytes
        return h.hexdigest()

    def __init__(self, key) :
        # Key Size is 128 bits
        self.key = self.md5_hash(key)

    def encrypt(self, cleartext) :
        # Block size should be equal to 128 bits
        Block_Size = AES.block_size
        pad = lambda s: s + (Block_Size - len(s) % Block_Size) * chr(Block_Size - len(s) % Block_Size)
        cleartext_blocks = pad(cleartext)
        
        # Create A Random IV
        iv = Random.new().read(Block_Size)
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks.encode()))

    def decrypt(self, enctext) :
        enctext = base64.b64decode(enctext)
        iv = enctext[:16]
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)
        # Inpad the blocks before decrypting
        unpad = lambda s : s[:-ord(s[-1:])]       # slight change in this line to cope with Python 3; original is lambda s : s[0:-ord(s[-1])] 
        return unpad(crypto.decrypt(enctext[16:]))   
    
aes = AESCrypto('password123')
encrypted = aes.encrypt('Hello World')
print(encrypted)
decrypted = aes.decrypt(encrypted)
print(decrypted)