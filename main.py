import random
import string
def pass_gen():
    e_mail = input("for what you wnat to generate password ")
    spec_char = "@abcdefghijklimn&op$qrst#*ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s_letter = string.ascii_lowercase
    c_letter = string.ascii_uppercase
    n_no = string.digits
    size_count = int(input("input on elements in passwords"))
    print("press 1 for generate lowercase random alphabetical password")
    print("press 2 for generate uppercase random alphabetical password")
    print("press 3 for generate numeric random password")
    print("press 4 for generate special character random password")
    t_pass = int(input())
    if t_pass == 1:
        password = ''.join(random.choice(s_letter) for i in range(size_count))
        file1 = open(r"C:\Users\Pulkit\Desktop\passwords.txt","a")
        file1.write('\n')
        file1.write('email : ')
        file1.write(e_mail)
        file1.write('\n')
        file1.write("password : ")
        file1.write(password)

        print(password)
    elif t_pass == 2:
        password = ''.join(random.choice(c_letter) for i in range(size_count))
        file1 = open(r"C:\Users\Pulkit\Desktop\passwords.txt", "a")
        file1.write('\n')
        file1.write('email : ')
        file1.write(e_mail)
        file1.write('\n')
        file1.write("password : ")
        file1.write(password)
    elif t_pass == 3:
        password = ''.join(random.choice(n_no) for i in range(size_count))
        file1 = open(r"C:\Users\Pulkit\Desktop\passwords.txt", "a")
        file1.write('\n')
        file1.write('email : ')
        file1.write(e_mail)
        file1.write('\n')
        file1.write("password : ")
        file1.write(password)
    elif t_pass == 4:
        password = ''.join(random.choice(spec_char) for i in range(size_count))
        file1 = open(r"C:\Users\Pulkit\Desktop\passwords.txt", "a")
        file1.write('\n')
        file1.write('email : ')
        file1.write(e_mail)
        file1.write('\n')
        file1.write("password : ")
        file1.write(password)
    else:
        print("nope")

pass_gen()



