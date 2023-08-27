from Crypto.Hash import HMAC
message = b"Hello World"  # note the added 'b' here, in contrast with Pluralsight code
password = b"mypassword"
h = HMAC.new(password)
h.update(message)
print(h.hexdigest())