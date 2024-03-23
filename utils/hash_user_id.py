import base64

# Integer to be encoded
num = 1312113123

# Encoding the integer to Base64
encoded_text = base64.b64encode(str(num).encode()).decode()

print("Encoded:", encoded_text)

# Decoding the Base64 back to integer
decoded_num = int(base64.b64decode(encoded_text).decode())

print("Decoded:", decoded_num)
