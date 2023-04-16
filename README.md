# Telegram Contacts to Excel

Telegram Contacts to Excel is a small app that can help you to import your 
Telegram contacts to an Excel file. It's a simple way to keep your 
contacts up to date, and to have a backup of your contacts in a familiar 
format.

## Usage

_Note: Before you get started, make sure you have Docker Compose installed 
on your desktop._

Usage
Note: You need to have Docker Compose installed on your desktop in order to use this app.

### Step 1: Clone the repository
Clone the application from GitHub by running the following command or another method you prefer: 

```bash
git clone https://github.com/kupri-ar/telegram-contacts-to-excel.git
```

### Step 2: Fill in the credentials
Fill in the .env file with your own Telegram credentials: 

```.env
API_ID=your_api_id
API_HASH=your_api_hash
PHONE=your_phone_number
```

You can get these credentials from the Telegram website.
* Go to https://my.telegram.org/auth
* Log in with your phone number and the confirmation code that Telegram sends to your phone
* Click on the "API development tools" link
* Fill out the form to create a new app (you can use any name and URL)
* Copy the "App api_id" and "App api_hash" values to your .env file
* Add your phone number to the .env file


### Step 3: Run the script
Start the app using one of the following methods, depending on your operating system:

#### Windows
To start the script on Windows, simply double-click on the start.bat file. 
This will open a command prompt and start the script.

#### MacOS and Unix/Linux
To start the script on MacOS or Unix/Linux, open a terminal and navigate to the directory where 
you cloned the application. Then, run the following command:
```bash
./start.sh
```
This will start the script in your terminal.

Made with :heart: by Kupri A.
