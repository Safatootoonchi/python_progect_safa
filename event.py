import logging


class DefineEvent:
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

    def append_to_csvfile(self):
        pass

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

