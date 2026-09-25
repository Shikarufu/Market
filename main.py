from InquirerPy import inquirer as i
from colorama import Fore,Back,Style
import pyfiglet
from rich.console import Console
import pandas as pd



console = Console()

# Generate the large ASCII block letters
ascii_title = pyfiglet.figlet_format("Market", font="slant")

# Print it using a vibrant gradient color
console.print(f"[bold green]{ascii_title}[/bold green]")



# Todo
# Make a option
run=True
cart=[]
Fruit=[
  {"name":"Banana","stock":5,"price":2},
  {"name":"Apple","stock":5,"price":2.3},
  {"name":"Kiwi","stock":5,"price":3},
  {"name":"Berry","stock":5,"price":2.5},
  {"name":"Orange","stock":5,"price":1.5}
]

Vegetable=[
  {"name": "Broccoli", "stock": 5, "price": 2.5},
  {"name": "Potato", "stock": 5, "price": 1.2},
  {"name": "Tomato", "stock": 5, "price": 1.8},
  {"name": "Spinach", "stock": 5, "price": 2.0},
  {"name": "Cabbage", "stock": 5, "price": 1.5}
]

Drink=[
  {"name": "Coca Cola", "stock": 5, "price": 1.3},
  {"name": "Pepsi", "stock": 5, "price": 1.3},
  {"name": "Lemonade", "stock": 5, "price": 2},
  {"name": "Orange Juice", "stock": 5, "price": 2.2},
  {"name": "Water", "stock": 5, "price": 0.5}
]
data=[]

while run:
  
  option=i.select(
    message="Please choose the option",
    choices=[
      {"name":"[a].Fruit🥝","value":"a"},
      {"name":"[b].Vegetable🥕","value":"b"},
      {"name":"[c].Drink🍹","value":"c"},
      {"name":"[d].View Cart","value":"d"},
      {"name":"[e].Exit➜]","value":"e"}
    ]

  ).execute()

  if option == "a":
    fruit_list=[{"name":f"{f['name']}, stock:{f['stock']}, price:${f['price']}",
             "value":f['name']
            }for f in Fruit]
    fruit_list.append({"name":"Go back","value":"back"})
    chosenFruit=i.select(
      message="Which fruit you want?",
      choices=fruit_list
    ).execute()

   
    if chosenFruit != "back":
      selected_item=None
      for fruit_item in Fruit:
        if fruit_item['name'] == chosenFruit:
          print(Fore.LIGHTGREEN_EX,f"You selected {fruit_item['name']}!")
          print(Style.RESET_ALL)
          selected_item=fruit_item
          break

      qty_str=i.text(message=f"How many {chosenFruit}s you want?\n-->").execute()
      qty=int(qty_str)

      if qty <= selected_item['stock']:
        # cart.append(chosenFruit)
        
        selected_item['stock'] -= qty

        price=selected_item['price']*qty
        # print(f"{price}")
        cart.append({
          "name":fruit_item['name'],
          "qty":qty,
          "price":price
      
        })
        print(f"Added {fruit_item['name']} to your cart!")

      else:
        print(Fore.LIGHTRED_EX,f"Not enough stock for you :(\n We only have {selected_item['stock']} left")
        print(Style.RESET_ALL)


  elif option == "b":
    vegetable_list=[
      {"name":f"{v['name']}, stock:{v['stock']}, price:${v['price']}",
      "value":v['name']}for v in Vegetable
    ]
    vegetable_list.append({"name":"Go back","value":"back"})
    chosen_vegetable=i.select(
      message="Which vegtable you want?",
      choices=vegetable_list
    ).execute()

    if chosen_vegetable != "back":
      selected_item=None
      for vegtable_item in Vegetable:
        if vegtable_item['name'] == chosen_vegetable:
          print(Fore.LIGHTGREEN_EX,f"You selected {vegtable_item['name']}",Style.RESET_ALL)
          selected_item=vegtable_item
          break

      qty_str=input(f"How many {vegtable_item['name']} you want?\n-->")
      qty=int(qty_str)

      if qty <=  selected_item['stock']:
        # stock process
        selected_item['stock']-=qty
        # calculate the price
        price=selected_item['price']*qty

        cart.append({
          "name":vegtable_item['name'],
          "qty":qty,
          "price":price 
        })
        print(f"Added {vegtable_item['name']} to your cart!")
      else:
        print(Fore.LIGHTRED_EX,f"Not enough stock for you :(\n We only have {selected_item['stock']} left")
        print(Style.RESET_ALL)
    
  # in dictionary we have name key,stock key, and price key
  elif option == "c":
    drink_list=[
      {"name":f"{d['name']}, stock:{d['stock']}, price:${d['price']}",
       "value":d['name']} for d in Drink
    ]
    drink_list.append({"name":"Go back","value":"back"})

    chosen_drink=i.select(
      message="Which drink you want?",
      choices=drink_list
    ).execute()

    if chosen_drink != "back":
      selected_item=None

      for drink_item in Drink:
        if drink_item['name'] == chosen_drink:
          print(Fore.LIGHTGREEN_EX,f"You selected {drink_item['name']}",Style.RESET_ALL)
          selected_item=drink_item
          break

      qty_str=input(f"How many {drink_item['name']} you want?\n-->")
      qty=int(qty_str)

      if qty <=  selected_item['stock']:
        selected_item['stock'] -= qty

        price=selected_item['price']*qty

        cart.append({
          "name":drink_item['name'],
          "qty":qty,
          "price":price
        })

        print(f"Added {drink_item['name']} to your cart!")
      else:
        print(Fore.LIGHTRED_EX,f"Not enough stock for you :(\n We only have {selected_item['stock']} left")
        print(Style.RESET_ALL)

  elif option == "d":
    for item in cart:
      data.append({
        "Name": item['name'],
        "Quantity": item['qty'],
        "Price": f"{item['price']:.2f}"
      })
    df=pd.DataFrame(data)
    if not cart:
      console.rule("  Cart is empty!  ")
      
    else:
      console.print("\n")
      console.rule()
      console.print("\n")
      print(df)    
      console.print("\n")
      console.rule()
      console.print("\n")
  # exit
  elif option == "e":
    # print(Fore.LIGHTGREEN_EX,"\t\t\t=====Receipt=====\n",Style.RESET_ALL)
    # print(Fore.LIGHTCYAN_EX,
    #   f"{cart}"
    # )
    if not cart:
      console.print("\n")
      console.rule()
      console.print("\n")
      print(Fore.RED,"You cart is empty!\nBuy something😘",Style.RESET_ALL)
      console.print("\n")
      console.rule()
      console.print("\n")
    else:
      totalPrice=0.0
      datas=[]
      print(Fore.LIGHTCYAN_EX)
      for item in cart:
        # print(f"{item['name']}\tx\t   {item['qty']}\t\t-$\t   {item['price']:.2f}")
        datas.append({
          "Name": item['name'],
          "Quantity": item['qty'],
          "Price": f"{item['price']:.2f}"
        })
        totalPrice+=item['price']

      console.print("\n")
      console.rule("[bold white on blue]  =====Receipt=====  [/bold white on blue]")
      console.print("\n")
      df=pd.DataFrame(datas)
      print(Fore.LIGHTMAGENTA_EX,df)
      print(f"\nYour bill:${totalPrice:.2f}")
      print(Style.RESET_ALL)
      console.print("\n")
      console.rule()
      console.print("\n")

      msg=pyfiglet.figlet_format("Thanks you for shopping!",font="slant")
      console.print(f"[bold green]{msg}[/bold green]")
    run=False

