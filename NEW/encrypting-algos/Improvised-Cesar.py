#our set of available userinputs
from string import printable

#Grab in input from user in to this variable
#file_input = "Grab input frm here"

def caesarConvertEncrypt(file_input, user_key):
    
    #here is where the magic happens
    encrypted_txt=str()
    for each_char in file_input:
        encoding_algo = ( printable.find( each_char ) - user_key ) % 100
        encrypted_txt += printable[ encoding_algo ]
    
    return encrypted_txt

#user test
print(caesarConvertEncrypt("This is the random text to see if things work!!?",2445275443))