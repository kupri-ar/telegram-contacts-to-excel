from telethon import functions
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import GetUserPhotosRequest

import pil_svc


def get_contacts(api_id, api_hash, phone_number, mode=''):
    with TelegramClient('session_name', api_id, api_hash) as client:
        # connect to Telegram
        client.connect()

        print('Connected to Telegram\n')

        # if the user is not already authorized, send an authorization request
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone=phone_number)

        print('Trying to get Telegram contacts...\n')

        try:
            # get your own contacts
            get_contact_result = client(functions.contacts.GetContactsRequest(hash=0))
            contacts = get_contact_result.contacts
        except Exception as e:
            print(e)
            return

        print('Received {} contacts\n'.format(len(contacts)))

        contact_list = []

        print('Your Telegram Contacts:')

        # print the names of your contacts
        for contact in contacts:

            # for test
            if mode == 'test':
                if len(contact_list) > 5:
                    break

            img = None
            try:
                user = client.get_entity(contact.user_id)
                photo = client(GetUserPhotosRequest(user_id=user.id, offset=0, max_id=0, limit=1))

                if photo.photos:
                    ph = photo.photos[0]
                    img = pil_svc.resize_and_get_image(client, ph)

                user_data_to_save = dict(
                    user_id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    username=user.username,
                    phone_number=user.phone,
                )
                print('{} | {} | {} | {} | {} | {}'.format(user.id, user.first_name, user.last_name, user.username,
                                                           user.phone, 'have an img' if img else 'no img'))

                user_data_to_save['img'] = img
                contact_list.append(user_data_to_save)
            except Exception as e:
                print(e)

        return contact_list
