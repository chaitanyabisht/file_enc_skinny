import base64
from skinny import SkinnyCipher

def encryptFile(file_path, password, mode):
    # Open file
    file = open(file_path, 'rb')
    # Read file
    plaintext = file.read()
    # Convert to base64
    plaintext = base64.b64encode(plaintext)
    # Convert to string
    plaintext = plaintext.decode()
    # Get key
    key = SkinnyCipher().getKey(password)
    # Get IV from first 3 characters of password
    iv = SkinnyCipher().getKey(password[:3])
    # Get nonce from last 3 characters of password
    nonce = SkinnyCipher().getKey(password[-3:])
    
    # Encrypt
    if mode == 'ECB':
        ciphertext = SkinnyCipher().ECB_ENCRYPT(key, plaintext)
    elif mode == 'CBC':
        ciphertext = SkinnyCipher().CBC_ENCRYPT(key, plaintext, iv)
    elif mode == 'CTR':
        ciphertext = SkinnyCipher().CTR_ENCRYPT(key, plaintext, nonce)
    # Close file
    file.close()
    # Write to file
    file = open(file_path + ".enc", 'w')
    file.write(ciphertext)
    file.close()

def decryptFile(file_path, password, mode):
    # Open file
    file = open(file_path, 'r')
    # Read file
    ciphertext = file.read()
    # Get key
    key = SkinnyCipher().getKey(password)
    # Decrypt
    if mode == 'ECB':
        plaintext = SkinnyCipher().ECB_DECRYPT(key, ciphertext)
    elif mode == 'CBC':
        plaintext = SkinnyCipher().CBC_DECRYPT(key, ciphertext, iv)
    elif mode == 'CTR':
        plaintext = SkinnyCipher().CTR_DECRYPT(key, ciphertext, nonce)
    # Convert to bytes
    plaintext = plaintext.encode()
    # Convert to base64
    plaintext = base64.b64decode(plaintext)
    # Get IV from first 3 characters of password
    iv = SkinnyCipher().getKey(password[:3])
    # Get nonce from last 3 characters of password
    nonce = SkinnyCipher().getKey(password[-3:])
    # Close file
    file.close()
    # Write to file
    file = open(file_path[:-4] + ".dec", 'wb')
    file.write(plaintext)
    file.close()

if __name__ == '__main__':
    # Encrypt
    encryptFile('hello.txt', 'password', 'ECB')
    # Decrypt
    decryptFile('hello.txt.enc', 'password', 'ECB')