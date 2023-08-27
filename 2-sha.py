from Crypto.Hash import SHA256
message = b"Hello World"  # note the added 'b' here, in contrast with Pluralsight code
h = SHA256.new()
h.update(message)
print(h.hexdigest())