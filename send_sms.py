from twilio.rest import Client
import sys
import requests
import json
with open('apiKeys.json') as f:
    data = json.load(f)
contacts = data.get('accounts')
sorted(contacts)
URL = data.get('data').get('URL')
usr = data.get('data').get('usr')
passkey = data.get('data').get('passkey')

def main():
    while(True):
        print("*******************************************")
        showBalance(URL, usr, passkey)
        print("Who would you like to send a message to?")
        displayMenu(contacts)
        print("")
        choice = raw_input("Select the choice: ")
        selectedContact = selection(choice, contacts)
        _message = message()
        send_sms(selectedContact, _message)

def displayMenu(contacts):
    num = 1
    for name in contacts:
        print("({}) {}   {}".format(num, name, contacts[name]))
        num = num+1
    print("(exit)")

def showBalance(url, usr, password):
    response = requests.get(url =url, auth=(usr,password))
    balance = response.json()['balance']
    print('Your leftover balance is: ' + balance+ '\n')
def send_sms(selected, message):
    if(selected != "NaN"):
        client = Client(usr, passkey)
        message = client.messages.create(body=message, from_='+19735543814', to=selected)
        print(message.sid)

def selection(choice, contacts):
    if choice == '1':
        return contacts["Justin Bakshi"]
    elif choice == '2':
        return contacts["Choman Saleem"]
    elif choice == '3':
        return contacts["Kim Lillard"]
    elif choice == '4':
        return contacts["Choman Saleem Google Voice"]
    elif choice == '5':
        return contacts['Nick Guinand']
    elif choice == 'exit':
        sys.exit()
    else:
        print("Selection Not Found")
        return "NaN"

def message():
    while(True):
        x = raw_input("What is the message: ") 
        if len(x.rstrip()) > 0:
            return x

if __name__ == "__main__":
    main()
