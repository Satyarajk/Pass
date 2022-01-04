import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#₹_&-+/*!?$()"
while 1:
     password_len = int(input("L"))
     password_count = int(input("N"))
     for x in range(0, password_count):
           password = ""
           for x in range(0, password_len):
           password_char = random.choice(Chars)
           password = password + password_char
       print(password)
