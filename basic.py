import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import string
import random

letters = string.ascii_lowercase
prefix = ''.join(random.choice(letters) for i in range(10))
toaster = ToastNotifier()
accounts = 1000
print('blasting ' + str(accounts) + ' accounts')


def sendRequest(i: int):
    print('registering ' + prefix + str(i))
    payload = {
        'first_name': prefix + str(i),
        'lms_phone_number': '085123456' + str(i),
        'email': prefix + str(i) + '@gmail.com',
        'password': '12345678'
    }
    url = r'{url/you-need/to-force}'
    with requests.session() as s:
        s.get(url)
        s.post(url, data=payload)
        with open("output.txt", "a") as file_object:
            file_object.write("registered: " + payload['email'] +
                              ", password: " + payload['password'] + "\n")


for i in range(accounts):
    sendRequest(i)
toaster.show_toast("Yo Bastard", "Successfully blasting " +
                   str(accounts) + ' account registrations')
