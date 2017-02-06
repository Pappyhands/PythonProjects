# Steps for Snork encryption:
# 1) Replace all instances of 'a' with the length of the sentence
# 2) Replace all instances of 'e' with the length of the sentence + 1
# 3) Replace all instances of 'i' with the length of the sentence + 2
# 4) Replace all instances of 'o' with the length of the sentence + 3
# 5) Replace all instances of 'u' with the length of the sentence + 4


print 'Please enter a sentence:' ,
message = raw_input()

length = len(message)

encryptedMessage = message.replace('a', str(length))
encryptedMessage = encryptedMessage.replace('e', str(length+1))
encryptedMessage = encryptedMessage.replace('i', str(length+2))
encryptedMessage = encryptedMessage.replace('o', str(length+3))
encryptedMessage = encryptedMessage.replace('u', str(length+4))

print 'The message encrypted is %s .' % encryptedMessage

encryptedMessage = encryptedMessage.replace(str(length), 'a')
encryptedMessage = encryptedMessage.replace(str(length+1), 'e')
encryptedMessage = encryptedMessage.replace(str(length+2), 'i')
encryptedMessage = encryptedMessage.replace(str(length+3), 'o')
encryptedMessage = encryptedMessage.replace(str(length+4), 'u')

print 'The message decrypted is %s .' % encryptedMessage