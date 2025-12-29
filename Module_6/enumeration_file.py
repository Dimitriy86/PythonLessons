from enum import Enum, auto

# -----------------------------------------------------------------------------------------

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
if today == Day.MONDAY:
    print("Today is monday.")
else:
    print("Today isn't monday.")

# -----------------------------------------------------------------------------------------

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status
    
    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Order '{self.name}' is updated to status {self.status.name}.")

    def display_status(self):
        print(f"Status of order is {self.name}: {self.status.name}.")


order1 = Order("Notebook", OrderStatus.NEW)
order2 = Order("Book", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()
