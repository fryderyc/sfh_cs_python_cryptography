from Crypto.Hash import MD5
message = b"Hello World"  # note the added 'b' here, in contrast with Pluralsight code
h = MD5.new()
h.update(message)
print(h.hexdigest())