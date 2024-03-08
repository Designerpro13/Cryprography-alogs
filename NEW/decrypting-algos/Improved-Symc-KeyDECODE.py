#Install the library if needed

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#from improvised-Symc-key import generated_Vector, generated_AESKey
'''
NOTE: the above function call happens to the previous encrypting file.
You can either output the one-time AES to user and assume them to
remmeber it all the time.
'''

def symmentricKeyDecrypt(encrypted_text, aes_key, vector):

    receiver_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(vector, 'utf-8')))
    aes_decryptor = receiver_aes_cipher.decryptor()

    # Do the decryption
    aes_plaintext_bytes = aes_decryptor.update(encrypted_text) + aes_decryptor.finalize()

    # convert back to a character string (we assume utf-8)
    orginal_text = aes_plaintext_bytes.decode('utf-8')

    return orginal_text

#User Test Run
#------Extracted from a custom AES algo------
a = "nkATKtfqRUsdjiZI"
v = "nsyfKquPDpJrbtHA"
b = bytes(b'\xeeX\xada$\xef\x1d\x94\xc0z\xd1\x1c\xa0\x86\xd9\x0b\xc3\xd3D;\xb3&\xd4\xe4U\x02pa\x08\xbd\x90\r')
print(symmentricKeyDecrypt(b,a,v))

