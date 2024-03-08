#our set of available userinputs
from string import printable

#Grab in input from user in to this variable
file_input = "Grab input frm here"

def Caesar_convert(file_input, user_key,X=14):
    """
    The special {X: X c Z -> 5<X<100}
    here is a product specific code. Defined
    by the software developer, The idea is to
    let only the device used to encrypted file
    may only decrypt it in future.
    """
    #here is where the magic happens
    encrypted_txt=str()
    for each_char in file_input:
        encoding_algo = ( printable.find( each_char ) - user_key ) % X
        encrypted_txt += printable[ encoding_algo ]
    
    return encrypted_txt

#user test
print(Caesar_convert("This is the random text to see if things work!!?",2005))