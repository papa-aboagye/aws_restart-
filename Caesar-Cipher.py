def getDoubleAlphabet(alphabet):
    doubleAlphabet =alphabet + alphabet
    return doubleAlphabet
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
def getCipherKey():
    shiftAmount = int(input( "Please enter a key (whole number from 1-25): "))
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + (cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    findrealans = -1 * (cipherKey)
    return encryptMessage(message, findrealans, alphabet)
    
def runCaesarCipherProgram():
        myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(f'Alphabet: {myAlphabet}')
        myAlphabet2 = getDoubleAlphabet(myAlphabet)
        print(f'Alphabet2: {myAlphabet2}')
        myMessage = getMessage()
        print(myMessage)
        myCipherKey = getCipherKey()
        print(myCipherKey)
        myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
        print(f'Encrypted Message: {myEncryptedMessage}')
        myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
        print(f'Decypted Message: {myDecryptedMessage}')
        
        
    
           

        
runCaesarCipherProgram()
        
        
       
        
        