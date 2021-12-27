import event
import SignLog as sl
import participate as par

# print('Please answer this question with a yes or no')
# reg = input('Have you registered? ')
# if reg.lower() == 'yes':
#     username = input('Please enter your username: ')
#     password = input('Please enter your password: ')
#     log_in = sl.LogIn(username, password)
#     log_in.check_username_pass()
#     log_in.account_locking()
#     log_in.check_client_or_manager()
#
# if reg.lower() == 'no':
#     register = sl.Register()
#     register.get_email()
#     register.sign_up()
#     register.unique_password()
user = None


def event_info():
    name = input("Please enter the name of event that you want to define: ")
    date = input("Please enter the date of event that you want to define: ")
    time = input("Please enter the time of event that you want to define: ")
    place = input("Please enter the place of event that you want to define: ")
    total_capacity = input("Please enter the total_capacity of event that you want to define: ")
    remaining_capacity = input("Please enter the remaining_capacity of event that you want to define: ")
    cost_ticket = input("Please enter the cost_ticket of event that you want to define: ")
    discount_code = input("Please enter the discount_code of event that you want to define: ")
    discount_percent = input("Please enter the discount_percent of event that you want to define: ")
    define_event = event.DefineEvent(name, date, time, place, total_capacity, remaining_capacity,
                                     cost_ticket, discount_code, discount_percent)
    return define_event


def menu():
    global user, user_participation, help
    print("Hello thanks for use this site,\nif you registered in this site please log in \nand if you haven't"
          "registered yet,please register first,\nfor registering you should have valid email.\n"
          "consider that if you are a manager,we have \nalready give you your username and password.")
    while True:
        print(
            "1.Register\t\t2.LogIn\t\t3.DefineEvent\t\t4.Participate\t\t\tQuit:else")
        process_number = input('Enter a process that you want: ')
        if process_number == '1':
            sing_in = sl.Register()
            sing_in.email_address_validation()
            sing_in.unique_email()
            sing_in.get_unique_username()
            sing_in.unique_username()
            sing_in.get_password()
            sing_in.register_to_list()
            sing_in.add_to_file()

        elif process_number == '2':
            log_in = sl.LogIn()
            log_in.get_check_username_pass()
            user = log_in.check_kind_of_user()
            log_in.return_output()
        elif process_number == '3':
            if user != None:
                if user == "Manager":
                    d_event = event_info()
                    d_event.convert_to_list()
                    d_event.append_to_csvfile()
                    d_event.event_registration()
                else:
                    print("you not allowed to define the event")
            else:
                print("you haven't entered yet.\n"
                      "for defining event please log in first. ")
        elif process_number == '4':
            print("Thank you for wanting to participate in the event \n"
                  "Choose any of the following processes that you want")
            # if len(event.list_df) != 0:
            df = event.list_df[0]
            user_participation = par.Participate("event.csv", df)
            user_participation.total_capacity()
            user_participation.remaining_capacity()
            user_participation.cost_ticket()
            user_participation.discount_code()
            user_participation.discount_percent()
            while True:
                print("1.show event\t\t2.choose a event\t\t"
                      "3.number of tickets\t\t4.discount\t\t5.pay a cost\t\t\tQuite:else")
                method_number = input("please the number of work you want to do: ")
                if method_number == '1':
                    user_participation.show_event()
                elif method_number == '2':
                    choose = input("you want to choose the event by name or id? ")
                    if choose.lower() == 'id':
                        user_participation.choose_event_by_id()
                    elif choose.lower() == 'name':
                        user_participation.choose_event_by_name()
                    else:
                        print("The word you entered could not be identified\n"
                              "if you want choose by id type 'id' and if you want choose by name"
                              "type 'name")
                elif method_number == '3':
                    user_participation.tickets_number()
                elif method_number == '4':
                    help = True
                    discount_code = input("if you have a discount code enter it,otherwise leave blank.")
                    if discount_code != None:
                        user_participation.calculate_discount(discount_code)
                    else:
                        discount_code = 0
                        user_participation.calculate_discount(discount_code)
                    print("we also consider a discount for a student and early ticket.\n"
                          "discount for student is 15% and for early ticket is 10% ")
                    discount_code2 = input('if you are a student enter number 1\n'
                                           'and if you want to buy a early ticket enter number 2')
                    if discount_code2 == '1':
                        user_participation.colculate_cost(0.15)
                    elif discount_code2 == '2':
                        user_participation.colculate_cost(0.1)
                    else:
                        print("The number entered is unacceptable. ")
                elif method_number == '5':
                    if help == False:
                        user_participation.colculate_cost(0)
                        cost = input("Please enter the cost you want to pay: ")
                        user_participation.payment_cost(cost)
                        user_lddd = []
                else:
                    break
        else:
            break


menu()
