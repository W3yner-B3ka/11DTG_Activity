# This is a shopping cart program where users can add towards their "shopping cart"
# This program will allow users to add, delete, and update their shopping cart.
# The program will display the shopping list and to check if the person wants to buy the shopping cart or not.
# version 3.0 (added checkout, update items, and delete items. Also added user options to make flow easier)


# Imports
import time  # Add delay to a console
from datetime import (
    datetime,
)  # Add datetime to print the time you bought things from the shop.
import os  # This will allow to clear the text

# This constant will add tax towards the items that are sold in the shop
TAX = 0.15

# Items that the shop will sell
itemsForSale = {
    "Katana": 300.00,
    "Longsword": 250.00,
    "Dagger": 500.00,
}

# The user's attributes will be defined in a dictionary
userAttributes = {
    "cartIsEmpty": True,  # The cart will initially start as empty
    "shopping_cart": {},  # Initially, the shopping cart will be empty
}


# This function will clear the console
def clearText():
    os.system("cls" if os.name == "nt" else "clear")


# function to wait for the user to do something
def helpPause():
    input("\n Press Enter to return to the menu.")
    # if the enter key is pressed, go back to displaying the items
    time.sleep(1.5)
    clearText()
    displayItems()


# This function will display the items that are avalible in the shop
def displayItems():
    print(f"Here are the items we are selling today!")
    # Add a loop to display the items we are selling line by line
    # items will be represented as the key, price will be represented as the value
    for item, price in itemsForSale.items():
        # print the items displayed and the price in dollars with the tax
        print(f"{item}: ${price + TAX}")
    # end the loop then ask the user what would you like?
    user_input = input("What would you like?").lower()
    # check if what the user buys is in the items we are selling
    matched_item = checkIsFound(
        user_input, itemsForSale
    )  # user_input in the params  is user_input, store_items in the params is itemsForSale

    if matched_item:
        user_input = input(
            f"Would you like to add {matched_item} to your shopping cart? "
        ).lower()
        # if the user says yes, add the item
        if user_input == "yes":
            # ask the user how many do they want?
            quantity_input = input(f"How many {matched_item} would you like to buy?")
            # Make sure the quantity input is a digit.
            if quantity_input.isdigit() and int(quantity_input) > 0:
                quantity = int(quantity_input)
            elif quantity_input < 0:
                print("Invalid number, putting 1 as default")
                quantity = 1
            # add the item towards the dictionary
            time.sleep(1.5)
            clearText()
            addItem(matched_item, quantity)
            # else redirect them back to main menu.
        else:
            time.sleep(1.5)
            clearText()
            helpPause()
    # Redirect them back to the main menu if they type something not in stock
    else:
        print("The item you are looking for is not in our store.")
        time.sleep(1.5)
        clearText()
        displayItems()


# This function will display the users shopping cart
def displayCart():
    # if the cart is empty, print you have nothing
    if userAttributes["cartIsEmpty"] == True:
        print("You have nothing in your cart!")
    else:
        cart = userAttributes["shopping_cart"]
        # initially let the total price be zero
        total_price = 0
        # display the items in the shopping cart from the dictionary list
        print("Your shopping cart contains:  ")
        # loop through the items in the shopping cart
        for item, quantity in cart.items():
            # price will include the items initial cost plus the tax
            price = (itemsForSale[item] + TAX) * quantity
            # iterate the total price depending on how many items are in the cart
            total_price += price
            # display the item and round it to 2 d.p
            print(f"{item} x{quantity}: ${price:.2f}")
            # Display the total price and round it to 2 d.p
        print(f"\n Total price: ${total_price:.2f}")


# Add items towards the shopping car
# The parameter will be item so that we can pass down the matched_item
# quantity will initially be set to 1
def addItem(item, quantity=1):
    # add the matched item into the list
    cart = userAttributes["shopping_cart"]

    # if there is more than 1, add, else just equal to 1
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    # now the cart is not empty
    userAttributes["cartIsEmpty"] = False
    # Tell the user that it has been added into cart
    print(f"{quantity} {item} has been added into your cart.")
    # Wait for 1.5 seconds then display the cart
    time.sleep(1.5)
    print("Here is your shopping cart so far!")
    displayCart()

    # ask the user if they would like to continue shopping, update or delete the item.
    print("What would you like to do next?")
    # Ask the user what they would like to do
    userOptions()


# Update items from the shopping cart
def updateItem():
    # ask the user what would they like to change
    user_input = input("What would you like to change?")
    # check if what they want to change is found
    matched_item = checkIsFound(user_input, itemsForSale)

    # if not found, display to the user it is not there.
    if not matched_item:
        print("The item is not found in our store.")
        return

    # get the items inside the cart
    cart = userAttributes["shopping_cart"]
    # if the matched item is not in the cart
    if matched_item not in cart:
        print(f"{matched_item} is not in your cart.")
        return
    # try catch phrase, catch the error if the user puts anything less than zero or a decimal
    try:
        # ask the user how many items of the updated item do they want
        new_quantity = int(input(f"How many {matched_item} would you like now? "))
        # the matched item insde the cart is now the new quantity
        cart[matched_item] = new_quantity
        # display the user that the process has been done.
        print(f"{matched_item} quantity updated to {new_quantity}")
    except ValueError:
        print("Invalid number, keeping previous quantity")
    time.sleep(1.5)
    clearText()
    displayCart()
    # Ask the user what they would like to do
    userOptions()


# Delete items from the shopping cart
def deleteItem():
    # ask the user what they would like to delete
    user_input = input("What item would you like to delete?")
    # check if what they want to delete is found
    matched_item = checkIsFound(user_input, itemsForSale)
    # get the user_attributes items
    cart = userAttributes["shopping_cart"]
    # if the matched item is not in cart then return an error
    if matched_item not in cart:
        print(f"{matched_item} is not in your cart.")
    # delete the item from the cart
    del cart[matched_item]
    print(f"{matched_item} has been removed from your cart")
    time.sleep(1.5)
    clearText()
    displayCart()
    # Ask the user what they would like to do
    userOptions()


# Checkout items
def checkoutCart():
    # get the cart from the user attributes
    cart = userAttributes["shopping_cart"]
    # if there is nothing to checkout, then send them back to the main menu
    if not cart:
        print("You have nothing inside your cart.")
        time.sleep(1.5)
        clearText()
        displayItems()
        return
    # if there are items, ask the user if they want to checkout
    user_input = input("Would you like to checkout?").lower().strip()
    if user_input == "yes":
        print("\n=== Checkout ===")
        # display the cart
        displayCart()

        # Print the date and time of purchase
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n Purchased completed at {now}")

        # clear the cart after the checkout
        userAttributes["shopping_cart"] = {}
        userAttributes["cartIsEmpty"] = True

        # Send a goodbye message and thank them for shopping at the store
        print("\n Thank you for shopping at our sword store!")
        time.sleep(1.5)
        clearText()
        exit()
    else:
        print("Have a great time shopping at our store!")
        time.sleep(1.5)
        clearText()
        displayItems()


# This function will check whether if the items they say is within the cart
# the parameters will be the user input and the store item
def checkIsFound(user_input, store_item):
    # the words wil be the user input's sentences split into words
    words = user_input.split()
    # keys return a view object
    lowercase_storeItems = {item.lower(): item for item in store_item.keys()}
    # loop through the words split and check if the words match the item
    for keyword in words:
        # if the keyword is in the store items converted to lowercase
        if keyword in lowercase_storeItems:
            # display the lowercase store items
            return lowercase_storeItems[keyword]
    # else, return none
    return None


# User options
def userOptions():
    user_actions = int(
        input(
            "Press 1 to continue shopping,\n press 2 to update items,\n press 3 to delete items. \n press 4 to checkout your items \n press 5 to exit"
        )
    )
    time.sleep(1.5)
    clearText()
    # if the user press 1, display items that are for sale!
    if user_actions == 1:
        displayItems()
    # if the user press 2, ask the user what they would want to update
    elif user_actions == 2:
        updateItem()
    #  if the user press 3, ask the user what they would like to delete
    elif user_actions == 3:
        deleteItem()
    # else if the user user had enough shopping, greet a warm message then exit the program
    elif user_actions == 4:
        checkoutCart()
    else:
        print("Have a nice day!")
        exit()


# This function will run the main function.
def main():
    print("Welcome to this shop where we sell swords")
    # While the loop is true, run the program
    while True:
        # lower all of the characters and remove the spaces.
        answer = (
            input("Would you like to proceed and see what we offer?").lower().strip()
        )
        # if the answer is yes, proceed with selling the items
        if answer == "yes":
            time.sleep(1.5)
            clearText()
            displayItems()
        elif answer == "no":
            # Say a warm greeting then break the loop and exit
            print("Have a nice day, goodbye!")
            break
            exit()
        else:
            # if no input, tell the user please answer yes or no
            print("Please answer 'yes' or 'no'  ")


main()
