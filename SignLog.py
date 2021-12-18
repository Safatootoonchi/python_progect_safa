import logging


class Register:
    def __init__(self):
        pass

    def get_email(self):
        pass

    def sign_up(self):
        pass

    def unique_password(self):
        pass


class LogIn:
    id = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_username_pass(self):
        pass

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
    def check_client_or_manager(self):
        pass


