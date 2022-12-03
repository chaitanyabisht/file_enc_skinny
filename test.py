from Crypto.Util.Padding import pad, unpad
plaintext = 'adf'
plaintext = pad(plaintext.encode(), 16, style='pkcs7')
# convert to hex
print(plaintext.hex())

#unpad
s = unpad(plaintext, 16, style='pkcs7')
print(s.hex())