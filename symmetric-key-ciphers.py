# The following dictionary will be used as our text base with key value pairs in order decrypt and encrypt
# our messages 

alpha = {
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k",
    11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u",
    21: "v",22: "w",23: "x",24: "y",25: "z", 26: " "
}

# getKey allows us to search through our alphabet/character space and obtain the key for a matching value.
def getKey(letter):
    for key,val in alpha.items():
        if val == letter:
            return key

# getVal allows us to search through our alphabet/character space and obtain the value for a matching key.
def getVal(num):
    for key,val in alpha.items():
        if key == num:
            return val

# message_to_keys converts a string into a list of integers with respective keys for each character in the string. 
def message_to_keys(message):
    keys = []
    for i in range (0,len(message)):
        keys.append(getKey(message[i]))

    return keys

# keys_to_message converts a list of integers into a message of type string.
def keys_to_message(list_of_keys):
    message = ""
    for i in range (0, len(list_of_keys)):
        message += getVal(list_of_keys[i])

    return message

# The following is the implementation of a shift encryption

    # convert the message into a list of keys.
    # loop through the keys and for each key add the shift value. if it is greater than 25 then subtract 26 
    # this allows us to stil stay within our character space/dictionary defined above. 
    # then append the encrypted keys to a new list and convert the encrypted list into a message using the
    # the function above. 

def ceaser_encrypt(shift, message):
    keys = message_to_keys(message)
    encrypted_keys = []

    for key in keys:
        if key <= 25:
            eKey = key + shift
            if (eKey > 25):
                eKey = eKey - 26

            encrypted_keys.append(eKey)
        else:
            encrypted_keys.append(key)

    return keys_to_message(encrypted_keys)

# The following is the implentation of the affine cipher encrytion

    # convert the message into a list of keys.
    # loop through the keys and use the formula (k = ax + b) where: # k is our encrypted value in the form of an integer           
                                                                    # a,b is our key entered by the user
                                                                    # x is our current value in the form of an integer before encryption.
        # if our encrypted key is larger than the character space then keep subtracting 26 from it until it is within our character space.
    # then append the encrypted keys to a new list and convert the encrypted list into a message using the
    # the function above. 

def affine_encrypt(a,b,message):
    keys = message_to_keys(message)
    encrypted_keys = []
    for key in keys:
        if key <= 25:
            eKey = (a*key) + b
            while (eKey > 25):
                eKey = eKey - 26
            encrypted_keys.append(eKey)
        else:
            encrypted_keys.append(key)

    return keys_to_message(encrypted_keys)


def main():
    print("hello world")
    print(ceaser_encrypt(9,"hello world"))
    print(affine_encrypt(12,9,"hello world"))
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()