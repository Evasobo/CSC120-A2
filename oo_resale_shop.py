from computer import Computer
from typing import Dict, Optional, Union

  
class ResaleShop:
    
    inventory : list
     
       
    def __init__(self):
      self.inventory = []
    
    # to buy a new computer
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print(f"New computer addes: {computer.description}")
        
    #sell computer
    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print(f"Computer removed: {computer.description}")
        else:
            print("Error: Computer not found in inventory.")
        
        #updating the price or operating systen of a computer
    def update_computer(self, description, new_price=None, new_os=None):
        for computer in self.inventory:
            if computer.description == description:
                if new_price is not None:
                    computer.update_price(new_price)
                if new_os is not None:
                    computer.update_os(new_os)
                print(f"Computer updated: {description}")
                return
        print("Error: Computer not found in inventory.")
        
        def refurbish(self, computer: Computer, new_os: Optional [str] = None) -> None:
                
            if computer.year < 2000: 
                computer.price = 50
            elif 2000 <= computer.year <= 2005:
                computer.price = 100
            elif 2006 <= computer.year <= 2010:
                computer.price = 300
            elif 2011 <= computer.year <= 2015:
                computer.price = 500
            elif 2016 <= computer.year <= 2020:
                computer.price = 1000
            else:  # 2021 and newer
                computer.price = 1500
            
        def display_inventory(self):
            if not self.inventory:
                print("No inventory to display.")
            else:
                print(self.inventory)
                    
            
        
       