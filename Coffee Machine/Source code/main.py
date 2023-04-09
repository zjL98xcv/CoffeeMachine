from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

git clone <https://github.com/zjL98xcv/CoffeeMachine/new/main?readme=1>

#create instance of class
CoffeeMaker1 = CoffeeMaker()
Menu1 = Menu()
money_machine1 = MoneyMachine()

#print resources of coffee machine



is_on = True
while is_on:
    option = Menu1.get_items()
    choice = input(f"What would you like? {option}")
    if choice == "report":
        CoffeeMaker1.report()
        money_machine1.report()
    elif choice == "off":
        is_on = False
    else:
        drink = Menu1.find_drink(choice)
        if CoffeeMaker1.is_resource_sufficient(drink) and money_machine1.make_payment(drink.cost):
                CoffeeMaker1.make_coffee(drink)
                
















#Access attribute

#Call back function
