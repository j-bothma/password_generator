import string
import random
from secrets import main_pass

txt = open("gen.txt", "a+")
def password_gen(x):
     passwords = ''.join(random.choice(string.ascii_letters+ string.digits + string.punctuation) for _ in range(int(x)))
     return passwords

if main_pass == "":
     print("Please create a master password")
     main_pass = input()
else:
     print("What is the master password?")
     ms_input = input()
     if ms_input == main_pass:
          print("Would you like to 1. Fetch all passwords or 2. Create new password?")
          choice = input()
          if choice == "1":
               with open("gen.txt", "r") as txt:
                    for line in txt:
                         print (line.strip())
          else:
               print("What is the password for?")
               website = input()
               print("What is the required length?")
               size = input()
               password = password_gen(size)
               txt.write(website + " - " + password)


     else:
          print("Password is incorrect")






