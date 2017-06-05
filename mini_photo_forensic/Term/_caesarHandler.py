
import _CipherAndDetect

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def hackCaesar(message):

    # loop through every possible key
    for key in range(len(LETTERS)):

        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is the same as the original Caesar program:

        # run the encryption/decryption code on each symbol in the message
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)  # get the number of the symbol
                num = num - key

                # handle the wrap-around if num is 26 or larger or less than 0
                if num < 0:
                    num = num + len(LETTERS)

                # add number's symbol at the end of translated
                translated = translated + LETTERS[num]

            else:
                # just add the symbol without encrypting/decrypting
                translated = translated + symbol

        # display the current key being tested, along with its decryption
        #print('Key #%s: %s' % (key, translated))
        match=_CipherAndDetect.detectTime(translated)
        if(match):
           # print translated
           # print key#%len(LETTERS)
            return key#%len(LETTERS)

    return -1
def encryptOrdecrypt(message,mode,key):

    # tells the program to encrypt or decrypt
     # set to 'encrypt' or 'decrypt'

    # every possible symbol that can be encrypted

    # stores the encrypted/decrypted form of the message
    translated = ''
    # capitalize the string in message
    #message = message.upper()

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = (num - key)%len(LETTERS)

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # print the encrypted/decrypted string to the screen
    #print(translated)
    return translated

#encryptOrdecrypt("hello world","encrypt")
#encryptOrdecrypt("uryy|-%| yq","decrypt")

#hackCaesar("uryy|-%| yq")

