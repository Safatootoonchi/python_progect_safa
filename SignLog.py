import logging
import re
import pandas as pd
from csv import DictWriter


class Register:

    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.id = 0

    # To make sure users are unique and not duplicate, I get their email and check it.
    def email_address_validation(self):
        print('You need to enter a valid email to get started.')
        while True:
            try:
                email = input('Please Enter the email you want to securely register: ')
                if email.endswith(".com"):
                    if email.startswith('@') == False:
                        if re.findall("@", email):
                            df = pd.read_csv("register.csv", sep=",")
                            check_unique_email = list(df["Email"] == email)
                            if True in check_unique_email:
                                print('You have already registered with this email.')
                            else:
                                self.email = email
                                break
                        else:
                            raise ValueError()
                    else:
                        raise ValueError()
                else:
                    raise ValueError()

            except ValueError:
                print("email is wrong!please try again")
                print('Note: A standard email is an email with "@" in the middle and ".com" at the end.')

    def unique_email(self):
        return self.email

    def get_unique_username(self):
        while True:
            username = input('Please enter the username that you want: ')
            df = pd.read_csv("register.csv", sep=",")
            check_unique_username = list(df["Username"] == username)
            if True in check_unique_username:
                print('this is a duplicate username.\n'
                      'Please select another username for yourself. ')
            else:
                self.username = username
                break

    def unique_username(self):
        return self.username

    def get_password(self):  # I don't want password be unique.
        password = input('Please enter the password that you want: ')
        self.password = password

    def register_to_list(self):
        register_list = [[self.username, self.password, self.email, self.id]]
        return register_list

    def add_to_file(self):
        register_list = Register.register_to_list(self)
        dataframe = pd.DataFrame(register_list, columns=["Username", "Password", "Email", "Id"])
        dataframe.to_csv("register.csv", index=False, mode='a', header=False)
        print('Your registration was successful.\n'
              'You can enter the site now. ')


class LogIn:

    def __init__(self):
        self.username = None
        self.password = None
        self.output = False
        self.user = None
        self.id = None
        self.i = None

    def get_check_username_pass(self):
        for i in range(3):
            username = input('please enter your username: ')
            password = input('please enter your password: ')
            df = pd.read_csv("register.csv", sep=",")
            check_username = list(df["Username"] == username)
            check_password = list(df["Password"] == password)
            for i in range(len(check_password)):
                if check_username[i] == True and check_password[i] == True:
                    self.output = True
                    self.i = i
            if self.output == True:
                print("You have logged in successfully.now you can see events.")
                break
            else:
                print("The user not find")
        else:
            LogIn.account_locking(self)

    def check_kind_of_user(self):
        df = pd.read_csv("register.csv", sep=",")
        check_id = list(df["Id"] == 1)
        if check_id[self.i] == True:
            self.user = "Manager"
        else:
            self.user = "client"
        return self.user

    def return_output(self):
        return self.output

    def account_locking(self):
        logger = logging.getLogger(__name__)
        # Create handlers
        f_handler = logging.FileHandler('file.log')
        f_handler.setLevel(logging.ERROR)
        # Create formatters and add it to handlers
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        # Add handlers to the logger
        logger.addHandler(f_handler)
        logger.error(f'account of {self.username} is locked')
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.WARNING)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)
        logger.error(f'account of {self.username} is locked')

#
# a = Register()
# a.email_address_validation()
# a.unique_email()
# a.get_unique_username()
# a.unique_username()
# a.get_password()
# a.register_to_list()
# a.add_to_file()

# b = LogIn()
# b.get_check_username_pass()
# b.check_kind_of_user()
# b.return_output()

# username = a.get_user_pass()
# register_list = a.register_to_list()
# df = pd.read_csv("register.csv", sep=",")
# check_unique_email = list(df["Email"] == email)
# check_unique_username = list(df["Username"] == username)
# if True in check_unique_email:
#     print('You have already registered with this email.')
# elif True in check_unique_username:
#     print('This username has already exist. ')
# else:
#     dataframe = pd.DataFrame(register_list, columns=["Username", "Password", "Email"])
#     dataframe.to_csv("register.csv", index=True, mode='w', header=True)
#     print('Your registration was successful. ')
