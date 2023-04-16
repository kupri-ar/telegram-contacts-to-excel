import os

from dotenv import load_dotenv

import tel_svc
import xlsx_svc

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
MODE = os.getenv('MODE')


if __name__ == '__main__':
    input()

    print('\n\nHello! You can import contacts from your Telegram account into an Excel file. \n\n'
          'Check your credentials:\n'
          'API_ID: {}\nAPI_HASH: {}\nPHONE_NUMBER: {}\n'.format(API_ID, API_HASH, PHONE_NUMBER))

    _continue = input("Continue? (Y/N) \n")

    if _continue.lower() == "y":
        print("Starting...\n")

        contacts = tel_svc.get_contacts(API_ID, API_HASH, PHONE_NUMBER, MODE)
        xlsx_svc.create_contacts_excel_file(contacts)

        print('Finished!')
    elif _continue.lower() == "n":
        print("Stopping...\n\n")
    else:
        print("Invalid answer. Please enter Y or N.\n\n")

