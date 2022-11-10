def currencyConverter():
    print ("Hi, this is the currency converter")
    cur = int(input("Please enter which type of currency you have. Choose from the list: 1. United States Dollar 2. European Euro 3. Chinese Yuan 4. Turkish Lira"))
    currency = {1 :  1,
                2 : 0.99,
                3 : 7.28,
                4 : 18.61}
    convert = float(currency.get(cur))
    amount = float(input("Please enter how much money you have."))
    total = amount / convert
    con = int(input("Please enter which type of currency you would like to convert to. Choose from the list: 1. United States Dollar 2. European Euro 3. Chinese Yuan 4. Turkish Lira"))
    conv = float(currency.get(con))
    final = conv * total
    print(final)

     
def groceryList():
 
    grocery = {"apple" : 1.50,
            "orange" : 1.00,
            "banana" : 1.00,
            "bagel" : 1.25,
            "cabbage" : 1.50,
            "spinach" : 4.25,
            "milk" : 2.75,
            "eggs" : 3.25,
            "cake" : 8.00,
            "pasta" : 3.50}
   
    bought = ["pasta", "cake"]
 
    total = 0
    for items in bought:
        itemPrice = grocery.get(items)
        total = itemPrice + total
 
    print("order costs " + str(total))
 
def main():
    groceryList()
    currencyConverter()
 
if __name__ == "__main__":
    main()
