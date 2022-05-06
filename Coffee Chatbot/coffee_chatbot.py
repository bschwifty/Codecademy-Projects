'''
Exercise Prompt: But first, coffee.

Whether it’s to get us ready to jump-start our day or to get us through a late-night cram session, 
many of us need our regular caffeine fix! Ordering coffee is just one example of a process that 
can be automated with the help of a chatbot.

You’re given the task of creating a Python chatbot that can help cut the wait time of a normal coffee
run by taking customers’ orders in advance. Write your code in the file called script.py and run it by 
entering python3 script.py in the terminal.
'''
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a {} {}!".format(size, drink_type))
  more = more_drinks()
  name = input("Can I get your name please? /n>")
  print("Thanks, {}! Your drink(s) will be out shortly.".format(name))

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
  if res == "a":
    return "Small"
  if res == "b":
    return "Medium"
  if res == "c":
    return "Large"
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_size()
    
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n>")
  if res == "a":
    return "Brewed Coffee"
  if res == "b":
    return "Mocha"
  if res == "c":
    return order_latte()
  else:
    print("Please select a drink type.")
    return get_drink_type()

def order_latte():
  res = input("What kind of milk would you like in your latte? \n[a] 2% Milk \n[b] Non-fat milk \n[c] Soy Milk\n>")
  if res == "a":
    return "2% Milk latte"
  if res == "b":
    return "Non-fat milk latte"
  if res == "c":
    return "Soy milk latte"
  else:
    print("Please select a type of milk.")
    return order_latte()

def more_drinks():
  res = input("Would you like any more drinks? Y/N \n>")
  if res.upper() == "Y":
    size = get_size()
    drink_type = get_drink_type()
    print("Alright, that's a {} {}!".format(size, drink_type))
    return more_drinks()
  if res.upper() == "N":
    print("Okay then!")  
  else:
    print("I'm sorry, did you say you wanted more drinks?")
    return more_drinks()

coffee_bot()
#size = get_size()
#drink_type = get_drink_type()



