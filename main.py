import event
import SignLog as sl
import participate

print('Please answer this question with a yes or no')
reg = input('Have you registered? ')
if reg.lower() == 'yes':
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    log_in = sl.LogIn(username, password)
    log_in.check_username_pass()
    log_in.account_locking()
    log_in.check_client_or_manager()

if reg.lower() == 'no':
    register = sl.Register()
    register.get_email()
    register.sign_up()
    register.unique_password()

