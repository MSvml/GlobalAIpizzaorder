## Pizza Order System ##

import csv
import datetime

## First, let's create a menu.

menu = """*Please Select a Pizza :
1: Classic Pizza - ingredients : Tomato, mozzarella and basil.
2: Margarita Pizza - ingredients : tomato, mozzarella, basil, olive oil and salt.
3: Mix Pizza - ingredients : mushroom, cheddar cheese, tomato, sausage, salami and sausage.
4: White Pizza - ingredients : ricotta sauce, mozzarella cheese, romano cheese and parsley.
5: Supreme Pizza - Ingredients : pizza sauce, mozzarella cheese, sausage, freshly sliced ​​red and green peppers, onions, mushrooms and pepperoni.
6: Pepperoni Pizza - ingredients : pizza sauce, mozzarella, pepperoni, thyme.
7: Gennaro Pizza - ingredients : pizza sauce, mozzarella cheese, sliced ​​sausage, marinated mushrooms, corn and thyme.
* Extra Ingredients of your choice:
11: Olive
12: mushroom
13: Goat cheese
14: Cheddar cheese
15: Mozzarella
16: Tomato
17: corn
18: Sausage
* Thank You!"""


## and write this menu in a notepad. Let's create a notebook named menu.txt

with open('Menu.txt', 'w',encoding="utf-8") as f:
    f.write(menu)
    

##let's create a Pizza superclass. Let's define the general features of our pizzas here    
 
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
    

## and let's create the pizzas we want as subclass
    
class ClassicPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
    
    
class MargaritaPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)


class MixPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class WhitePizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        
class SupremePizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
    
    
class PepperoniPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
        

class GennaroPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)

## Let's create a superclass called extra for extra ingredients to add to pizzas
        
class Extra:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

###and let's create subclasses that define all our materials    
    
class Olive(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Mushrooms(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
        
class GoatCheese(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
        
class Cheese(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
        
class Mozzarella(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Tomato(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
        
class Corn(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
        
class Sausage(Extra):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost 

## Let's create a superclass that will combine pizza and selected ingredients

class Decoator:
    def __init__(self, pizzaC , extraClasses):
        self.pizza = pizzaC
        self.extraDesc = ''
        self.extraTotal = 0
        for extraC in extraClasses :
            self.extraTotal += extraC.get_cost()
            self.extraDesc += ', extra ' + extraC.get_description()
            
        
    def get_cost(self):
        return self.pizza.get_cost() + self.extraTotal
    
    def get_description(self):
        return self.pizza.get_description() + self.extraDesc

    
 
## Let's create a superclass where we define user information

class Kullanici:
    def init(self, name, id_no, cc_num, cc_cvv):
        self.name = name
        self.id_no = id_no
        self.cc_num = cc_num
        self.cc_cvv = cc_cvv

## and let's create an ordering function. There should be a function that allows him to choose a pizza and as many extra toppings as he wants. 
## After choosing the customer's pizza, he can add all the extra ingredients he wants.
def create_order():
    with open("Menu.txt","r",encoding="utf-8") as f:
        menu=f.read()
        print(menu)

    pizza_choice = int(input("Please select a pizza  : "))
    if pizza_choice == 1:
        pizza = ClassicPizza("Clasic Pizza", 15)
    elif pizza_choice == 2:
        pizza = MargaritaPizza("Margarita Pizza", 20)
    elif pizza_choice == 3:
        pizza = MixPizza("Mix Pizza", 18)
    elif pizza_choice == 4:
        pizza = WhitePizza("White Pizza", 15)
    elif pizza_choice == 5:
        pizza = SupremePizza("Supreme Pizza", 20)
    elif pizza_choice == 6:
        pizza = PepperoniPizza("Pepperoni Pizza", 18)
    elif pizza_choice == 7:
        pizza = GennaroPizza("Gennaro Pizza", 20)
    else:
        print("You made an invalid choice.")
        return None
    
    extra_list = []
    while True :
        extra_choice = input("Please choose your extra : (q for quit )")
        if extra_choice == 'q':
            break
        elif extra_choice == '11':
            extra = Olive("Olive",3)
            extra_list.append(extra)
        elif extra_choice == '12':
            extra = Mushrooms("Mushroom", 5)
            extra_list.append(extra)
        elif extra_choice == '13':
            extra = GoatCheese("Goat Cheese", 7)
            extra_list.append(extra)
        elif extra_choice == '14':
            extra = Cheese("Cheddar cheese", 7)
            extra_list.append(extra)
        elif extra_choice == '15':
            extra = Mozzarella("Mozzarella", 7)
            extra_list.append(extra)
        elif extra_choice == '16':
            extra = Tomato("tomato ", 4)
            extra_list.append(extra)
        elif extra_choice == '17':
            extra = Corn("corn ", 5)
            extra_list.append(extra)
        elif extra_choice=='18':
            extra=Sausage("sausage",6)
            extra_list.append(extra)
        else:
            print("You made an invalid choice.")
            return None

    
    ## Use Decorator to combine pizza and sauce objects
    
    pizza_with_extra = Decoator(pizza, extra_list)
        
    ## Let's request user information and order details from the user
    
    name=input("Please text your name.")
    print(f"Hello {name}, we will save your order details.")
    id_no=input("Please enter your  ID number: ")
    cc_num = input("Please enter your credit card number: ")
    cc_cvc = input("Please enter your credit card CVC number: ")
    addres = input("Please enter your delivery address: ")
    Phone = input("Please enter your phone number: ")
    
    
    
    ## let's print the order details
    
    print("Your order details are as follows:")
    print(f"Delivery address: {addres}")
    print(f"Phone Numebr: {Phone}")
    print("Your order is ready. You have ordered a pizza as below: ")
    print("your choice: ", pizza_with_extra.get_description())
    print("Total cost: ", pizza_with_extra.get_cost() , "TL")
    
    # Save the order
    now = datetime.datetime.now()
    with open("orders.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Order date:  ',now.strftime("%Y-%m-%d %H:%M:%S"), "\n  Customer Order Detail: ",   pizza_with_extra.get_description(), '\n   Order amount: ' , pizza_with_extra.get_cost()  ,'\n   Customer Name Surname: ' ,name, '\n   Customer  ID Number: ' , id_no,'\n   Customer Card Number: ',cc_num,'\n   Customer Card CVC Number: ',cc_cvc,'\n   Customer address: ', addres, '\n   Customer phone number: ',Phone])

        
 ### let's call the order function and run our code       
create_order()
