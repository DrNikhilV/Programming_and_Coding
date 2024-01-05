import hashlib
str = "Hello World"
result = hashlib.sha256(str.encode())
print(result.hexdigest())