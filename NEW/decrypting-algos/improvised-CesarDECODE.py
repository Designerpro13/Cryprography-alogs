#our set of available userinputs
from string import printable

#Insert file contents from user in to this variable
#encrypted_input = "Grab input frm here"

def caesarConvertDecrypt(encrypted_input, user_key):
    """
    The special {X: X c Z -> 5<X<100}
    here is a product specific code. Defined
    by the software developer, The idea is to
    let only the device used to encrypted file
    may only decrypt it in future.
    """
    #here is where the magic happens - AGAIN
    decrypted_txt=str()
    for each_char in encrypted_input:
        decoding_algo = ( printable.find( each_char ) + user_key ) % 100
        decrypted_txt += printable[ decoding_algo ]
    
    return decrypted_txt

#user test
print(caesarConvertDecrypt("c-.\P.\P]-*P[&=)><P]*{]P]>P\**P.+P]-.=,\P`>[:jjD",2445275443))
print(len(printable))