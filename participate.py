import pandas as pd


class Participate:
    def __init__(self, file_path, df):
        self.file_path = file_path
        self.df = df
        self.i = False
        self.paric = False
        self.num = False
        self.cost = None
        self.discount = None
        self.total_cost = 0

    def show_event(self):
        df2 = pd.read_csv(self.file_path)
        print(df2.to_string())

    def total_capacity(self):
        list_total = list(self.df['total_capacity'])
        return list_total

    def remaining_capacity(self):
        list_remaining = list(self.df['remaining_capacity'])
        return list_remaining

    def cost_ticket(self):
        list_cost = list(self.df['cost_ticket'])
        return list_cost

    def discount_code(self):
        list_discount_code = list(self.df['discount_code'])
        return list_discount_code

    def discount_percent(self):
        list_discount_percent = list(self.df['discount_percent'])
        return list_discount_percent

    def choose_event_by_id(self):
        number_event = input('please enter the id of the event that you want: ')
        df1 = pd.read_csv(self.file_path, sep=",")
        check_id = list(df1["id"] == number_event)
        for i in range(len(check_id)):
            if check_id[i] == True:
                print('the event is exist,\n Enter the number of tickets to continue ')
                self.i = i
                self.paric = True
        else:
            print('this event is not exist.')

    def choose_event_by_name(self):
        name_event = input('please enter the name of the event that you want: ')
        df = pd.read_csv(self.file_path, sep=",")
        check_id = list(df["name"] == name_event)
        for i in range(len(check_id)):
            if check_id[i] == True:
                print('the event is exist,\n Enter the number of tickets to continue ')
                self.i = i
                self.paric = True
        else:
            print('this event is not exist.')

    def tickets_number(self,):
        if self.paric == True:
            num = input("enter the number of ticket that you want: ")
            list_total = Participate.total_capacity(self)
            if int(num) <= len(list_total):
                print('Number of tickets registered.\nPlease pay the price to continue.')
                self.num = num
            else:
                print('the number os the thicket is not allowed')
        else:
            print("you haven't chosen a event yet,"
                  " please choose first,than enter the number of ticket  ")

    def calculate_discount(self, code):

        list_discount_code = Participate.discount_code(self)
        list_discount_percent = Participate.discount_percent(self)
        if list_discount_code[self.i] == code:
            self.discount = list_discount_percent[self.i]
        else:
            print('Discount code not found.')

    def colculate_cost(self, discount):
        list_cost = Participate.cost_ticket(self)
        self.cost = list_cost[self.i] - (int(discount) + int(self.discount)) * list_cost[self.i]
        self.total_cost = int(self.num) * int(self.cost)
        print(f'You asked for {self.num} ticket and the price of each ticket is {self.cost} \n'
              f'So your total cost {self.total_cost} ')

    def payment_cost(self, cost):
        if int(cost) == self.total_cost:
            print('Your purchase was successful')
            list_total = Participate.total_capacity(self)
            list_remaining = Participate.remaining_capacity(self)
            list_total[self.i] -= 1
            list_remaining[self.i] -= 1
            self.df['total_capacity'] = list_total
            self.df['remaining_capacity'] = list_remaining
            self.df.to_csv(self.file_path, index=False, mode='w', header=False)

        else:
            print('Unsuccessful purchase,The entered cost is incorrect')
