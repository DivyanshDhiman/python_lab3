print("WELCOME TO THE AMANDO SHOPPING SITE")
print(" 1.Type 1 to Add a product to the cart.")   
print(" 2.Type 2 Search for a product.")   
print(" 3.Type 3 Delete a product from the cart.")   
print(" 4.Type 4 Display the contents of the cart.")   
print(" 5.Type 5 Purchase items.")   
print(" 6.Type 6 to Quit") 

shoppingCart = {}

x = int(input("What do you want to do?"))

if x == 1:
    print("You chose 1. That means you want to add a product to the cart.")
    a=int(input("How many products do you want to buy?"))
    i=1
    while(i>5):
        print("Cart is full")
        break
    
    while(i<=a):
        b=input("Which product do you want to buy?")
        c=int(input("Write the price of this product in dollars."))
        i=i+1
        shoppingCart.update({b:c})
print(shoppingCart)
    
   

    


     














