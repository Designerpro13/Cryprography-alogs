#Install the library if needed
from string import printable
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from random import choice
from functools import reduce

'''
We will be using the popular AES encryption key
NOTE: This requries the INPUT TEXT to be of 
minimum size of 16.
'''

def aesKeygenerator():
    #genetrating size-16 AES key
    aes_key = reduce(lambda a, b: a + b, [choice(printable) for i in range(16)])
    print(f'AES secret key: {aes_key}') #Debug print
    return aes_key

def initializeVectorgenerator():
    initialization_vector = reduce(lambda a, b: a + b, [choice(printable) for i in range(16)])
    print(f"AES initialization vector: {initialization_vector}") #debug print
    return initialization_vector

def symmentricKeyEncrypt(input_text, aes_key, vector):
    # The encryptor is setup using the key & CBC. In both cases we need to convert the string (utf-8) into bytes
    sender_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(vector, 'utf-8')))
    
    #encryptor object
    aes_encryptor = sender_aes_cipher.encryptor()  

    # Encryption in chunks-completing the encryption process
    aes_ciphertext = aes_encryptor.update(bytes(input_text, 'utf-8')) + aes_encryptor.finalize()
    
    # Print debug
    print(f"Encrypted AES ciphertext: {aes_ciphertext}")
    return aes_ciphertext

#Print debug
generated_AESKey = aesKeygenerator()
generated_Vector = initializeVectorgenerator()
print(symmentricKeyEncrypt("This is a sample text to encrypt",
                            generated_AESKey,
                            generated_Vector)) 