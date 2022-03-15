import random
# Creating a 8 letter password string includes numbers and alphabets 
# and also includes special characters

s1 =''
a = ['@','#','$','&','*','.','!']
s1 += chr(random.randrange(65, 90))
s1 += chr(random.randrange(97, 122))
s1 += chr(random.randrange(65, 90))
s1 += chr(random.randrange(97, 122))
s1 += str(random.randrange(0, 9))
s1 += str(random.randrange(0, 9))
s1 += a[random.randrange(0, 7)]

s1 = list(s1)
random.shuffle(s1)
s1 = ''.join(s1)    

print(s1)
