import string
import random

hash_value = []
# This function returns the ascii value for each character
def get_ascii_value(character):
    return ord(character)

# Returns the hash value for a given text
def text_hash(text):
    hash_lst = []    # An empty array
    hash_value_for_text = 0

    for char in text:

        # Returns ascii value for each character
        ascii_value = get_ascii_value(char)      
        hash_value_for_text += ascii_value % 67  # 67 = A

    # if the hash vlue is greater than 255 it will divide it by 10
    while hash_value_for_text > 255:
        hash_value_for_text = int(hash_value_for_text / 10)

    # Prints the hash value for the given text
    print(" Hash for text: ", hash_value_for_text)
    # hash_lst = the hash value and the text itself
    hash_lst = [int(hash_value_for_text), text]

    return hash_lst

# Generating random strings
def random_string():

    # Contains every ascii letters and digits
    # k=50 is the length of the random strings is 50
    return ''.join(random.choices(string.ascii_letters + string.digits, k=50))

# Asking the user the number times to test(to test the random strings)
def generate_hashings(num_of_strings):

    for i in range(num_of_strings):
        # The random strings generated in (def random_string()) function
        string = random_string()

        # To get the hash values of the random strings
        hash_values = text_hash(string)

        # Appending the generated hash values to the hash_value=[]
        hash_value.append(hash_values)

    # A file to store the text and their hash values
    with open('outfile.csv', 'a+') as file_handler:
        file_handler.write("{}\n".format(hash_value))


# Main program
# For task 7a
text = input("\n Text to hash: ", )
hash_lst = text_hash(str(text))
print("Hash value and the hashed text:", hash_lst)
# For task 7b
num_hashes = int(input("How many hashes should be generated?", ))
print("Generating {0} hashes:".format(num_hashes))
generate_hashings(num_of_strings=num_hashes)