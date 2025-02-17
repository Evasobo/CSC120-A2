class Computer:

   class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    # define methods
    def display_details(self):
        print(f"Description: {self.description}")
        print(f"Processor: {self.processor_type}")
        print(f"Hard Drive Capacity: {self.hard_drive_capacity} GB")
        print(f"Memory: {self.memory} GB")
        print(f"Operating System: {self.operating_system}")
        print(f"Year Made: {self.year_made}")
        print(f"Price: {self.price}")
        
        # Constructor 
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
        def display_inventory(self):
            if not self.inventory:
                print("No inventory to display.")
            else:
                print("Current Inventory:"+ self.inventory)
        
        def update_os(self, new_os: str):
            self.operating_system = new_os
            
        def update_os(self, new_price: str):
            self.price = new_price
    