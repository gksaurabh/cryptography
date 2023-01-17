alpha = {
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k",
    11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u",
    21: "v",22: "w",23: "x",24: "y",25: "z", 26: " "
}

def getKey(letter):
    for key,val in alpha.items():
        if val == letter:
            return key

def getVal(num):
    for key,val in alpha.items():
        if key == num:
            return val

def message_to_keys(message):
    keys = []
    for i in range (0,len(message)):
        keys.append(getKey(message[i]))

    return keys

def keys_to_message(list_of_keys):
    message = ""
    for i in range (0, len(list_of_keys)):
        message += getVal(list_of_keys[i])

    return message

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



def main():
    print("hello world")
    print(ceaser_encrypt(9,"hello world"))
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()