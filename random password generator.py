import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(113,128)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(33,48)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter4=chr(random.randint(52,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(123,128)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter6=chr(random.randint(97,122)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter7=chr(random.randint(58,64)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter8=chr(random.randint(91,96))
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter2 + uppercaseLetter3 + lowercaseLetter4 + uppercaseLetter5 + lowercaseLetter6 + uppercaseLetter7 + lowercaseLetter8 # + ....
password = shuffle(password)

#Ouput
print(password)