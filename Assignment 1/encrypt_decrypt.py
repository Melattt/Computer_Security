import os
import math
import string

# Read the file
def read_file(path):
    
    with open(path, "r") as file:
            full_text= " "
            for line in file:
                full_text += line
            return full_text


# Substitution cipher
# Encryption
def encrypt_text(text,key):
    # List of all characters which are which uppercase and lowercase s
    letters= string.ascii_letters  
     
    #An empty dictionary to store the substitution for the letters
    #Based on the key      
    sub = {}        
    for i in range(len(letters)): 
        sub[letters[i]] = letters[(i+key)%len(letters)] 
    
    encrypted_txt=[] 
    # Generating the cipher text    
    for letter in text: 
        if letter in letters: 
            l = sub[letter] 
            encrypted_txt.append(l) 
        else: 
            l = letter
            encrypted_txt.append(l) 
            
    return ("".join(encrypted_txt))

# Decryption
def decrypt_text(text,key):
    # List of all characters which uppercase and lowercase 
    letters= string.ascii_letters

    #An empty dictionary to store the substitution for the letters
    #Based on the key
    sub = {}      
    for i in range(len(letters)): 
        sub[letters[i]] = letters[(i-key)%(len(letters))] 
        
    # Iterate to get the original text
    decrypt_txt = [] 
    for letter in text: 
        if letter in letters: 
            l = sub[letter] 
            decrypt_txt.append(l) 
        else: 
            l = letter 
            decrypt_txt.append(l) 
            
    return ("".join(decrypt_txt)) 

# Transposition 
# Encryption
def encrypt_text2(text,key):
    # Generating the encrypted text
    encrypted_text = [""] * key
    # Iterating through each column in the encrypted text
    for coloum in range(key): 
        c_index = coloum
        # Loops until the current index passes the text's length
        while c_index < len(text): 
            # Puts the character in the current index
            encrypted_text[coloum] += text[c_index]
            # Moves the current index
            c_index += key
    # Converts the list(text) to a single string and it will return    
    return "".join(encrypted_text)

# Decryption
def decrypt_text2(text,key):
    # Obtaining the number of columns
    total_col = int(math.ceil(len(text) /float(key)))
    # The number of rows is equal to the key
    total_row = key

    # Generating the plain text
    decrypt_text = [""] * total_col 
    # col and row variables indicate where in the grid the character will enter
    col = 0
    row = 0
    for char in text:
        decrypt_text[col] += char
        col += 1
        # If no more columns or last shaded box go back to the first col 
        if (col == total_col) or (col == total_col -1 and row >= total_row - ((total_col*total_row) - len(text))):
            col = 0
            row += 1
    # Converts the list(text) to a single string and it will return 
    return "".join(decrypt_text)



# Program
Method = int(input("1 for Substitution or 2 for Transposition: ", ))
Perform = int(input("1 to Encrypt or 2 to Decrypt: ", ))

# if method = 1 substitution and method = 2 transposition
# if perform = 1 encrypt and perform = 2 decrypt

if Method == 1 and Perform == 1:                 
    path = input("Path: ",)                      
    key = int(input("Key: ",))
    Encrypted_Text = encrypt_text(read_file(path),key)
    # Create a file to store the encrypted text(substitution)
    with open('outfile.csv', 'w') as file_handler:        
        file_handler.write("{}\n".format(Encrypted_Text))

elif Method == 1 and Perform == 2:
    path = input("Path: ",)
    key = int(input("Key: ",))
    Decrypted_text = decrypt_text(read_file(path),key)
    # Create a file to store the decrypted text(substitution)
    with open('outfile.csv', 'w') as file_handler:
        file_handler.write("{}\n".format(Decrypted_text))


elif Method == 2 and Perform == 1:
    path = input("Path: ",)
    key = int(input("Key: ",))
    Encrypted_Tex = encrypt_text2(read_file(path),key)
    Encrypted_Text=Encrypted_Tex[1:]
    outFile = open("myOutFile.txt", "w")
    outFile.writelines("{}\n".format(Encrypted_Text))
    outFile.close()

elif Method ==  2 and Perform == 2:
    path = input("Path: ",)
    key = int(input("Key: ",))
    fd=open("myOutFile.txt","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("myOutFile.txt","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
    Decrypted_text = decrypt_text2(read_file(path),key)
    # Create a file to store the decrypted text(Transposition)
    outFile = open("myOutFile.txt", "w")
    outFile.writelines("{}\n".format(Decrypted_text))
    outFile.close()


#This is another code for substitution cipher
#It is almost same with the first one but I used string.printable here
"""
#Substitution cipher
def encrypt_text(text,key):
    # List of all characters which are considered to be printable 
    letters= string.printable   
     
    #An empty dictionary to store the substitution for the letters
    #Based on the key      
    sub = {}        
    for i in range(len(letters)): 
        sub[letters[i]] = letters[(i+key)%len(letters)] 
    
    encrypted_txt=[] 
    # Generating the cipher text    
    for letter in text: 
        if letter in letters: 
            l = sub[letter] 
            encrypted_txt.append(l) 
        else: 
            l = letter
            encrypted_txt.append(l) 
            
    return ("".join(encrypted_txt))

def decrypt_text(text,key):
    # List of all characters which are considered to be printable 
    letters= string.printable

    #An empty dictionary to store the substitution for the letters
    #Based on the key
    sub = {}      
    for i in range(len(letters)): 
        sub[letters[i]] = letters[(i-key)%(len(letters))] 
        
    # Iterate to get the original text
    decrypt_txt = [] 
    for letter in text: 
        if letter in letters: 
            l = sub[letter] 
            decrypt_txt.append(l) 
        else: 
            l = letter 
            decrypt_txt.append(l) 
            
    return ("".join(decrypt_txt))
"""