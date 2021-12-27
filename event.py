import logging
import pandas as pd

list_df = []
class DefineEvent:
    id = 0

    def __init__(self, name, date, time, place, total_capacity, remaining_capacity, cost_ticket, discount_code,
                 discount_percent):
        self.name = name
        self.date = date
        self.time = time
        self.place = place
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.cost_ticket = cost_ticket
        self.discount_code = discount_code
        self.discount_percent = discount_percent
        DefineEvent.id += 1

    def convert_to_list(self):
        event_list = [[DefineEvent.id, self.name, self.date, self.time, self.place,
                      self.total_capacity, self.remaining_capacity,
                      self.cost_ticket, self.discount_code, self.discount_percent]]
        return event_list

    def append_to_csvfile(self):

        event_list = DefineEvent.convert_to_list(self)
        event_list_header = ["id", "name", "date", "time", "place",
                             "total_capacity", "remaining_capacity",
                             "cost_ticket", "discount_code", "discount_percent"]
        dataframe = pd.DataFrame(event_list, columns=event_list_header)
        dataframe.to_csv("event.csv", index=False, mode='a', header=True)
        list_df.append(dataframe)
        return dataframe

    def tickets_sold(self):
        pass

    def event_registration(self):
        logger = logging.getLogger(__name__)
        # Create handlers
        f_handler2 = logging.FileHandler('file2.log')
        f_handler2.setLevel(logging.INFO)
        # Create formatters and add it to handlers
        f_format2 = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        f_handler2.setFormatter(f_format2)
        # Add handlers to the logger
        logger.addHandler(f_handler2)
        logger.warning(f'The event is {self.name} in date : {self.date} and in time : {self.time}')
