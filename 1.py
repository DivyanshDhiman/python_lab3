print("WELCOME TO THE AMANDO SHOPPING SITE")
print(" Type 1 to Add a product to the cart.")   
print(" Type 2 to Search for a product.")   
print(" Type 3 to Delete a product from the cart.")   
print(" Type 4 to Display the contents of the cart.")   
print(" Type 5 to Purchase items.")   
print(" Type 6 to Quit") 

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

if x == 6:
    print("ok")


print(" Type 2 to Search for a product.")   
print(" Type 3 to Delete a product from the cart.")   
print(" Type 4 to Display the contents of the cart.")   
print(" Type 5 to Purchase items.")   
print(" Type 6 to Quit") 

y=int(input("What do you want to do?"))
if y==2:
    print("You chose 2. That means you want to search a product from the cart.")
    d=int(input("How many products do you want to search?"))
    i=1
    while(i>5):
        print("This exceeds the limit of items in the cart.")
        break
    while(i<=d):
        e=input("Which product do you want to search?")
        i=i+1
        if e in shoppingCart:
            print (shoppingCart[e])
        else:
            print("this item is not available in the cart")
            
            
            
print(" Type 3 to Delete a product from the cart.")   
print(" Type 4 to Display the contents of the cart.")   
print(" Type 5 to Purchase items.")   
print(" Type 6 to Quit") 

z=int(input("what do you want to do?"))
if z==3:
    print("You chose 3. That means you want to delete a product from the cart.")
    f=int(input("How many products do you want to delete?"))
    i=1
    while(i>5):
        print("this is above the  maximum limit of the cart.")
        break
    while(i<=f):
        g=input("which product do you want to delete?")
        i=i+1
        if g in shoppingCart:
            shoppingCart.pop(g)
            print(shoppingCart)

print(shoppingCart)
if shoppingCart=={}:
    print("Shopping cart is empty.")



