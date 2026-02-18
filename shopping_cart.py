#This is a shopping cart program where users can add towards their "shopping cart"
#This program will allow users to add, delete, and update their shopping cart.
#The program will display the shopping list and to check if the person wants to buy the shopping cart or not.
#version 1.0

#TODO: Complete the storeItems and the userAttributes

#Imports
import time #Add delay to a console 
from datetime import datetime #Add datetime to print the time you bought things from the shop.
import os #This will allow to clear the text

#This constant will add tax towards the items that are sold in the shop
TAX = 0.15

#Items that the shop will sell
store_items = {
    "Katana": 300.00,
    "Longsword": 250.00,
    "Dagger" : 500.00,
}

#The user's attributes will be defined in a dictionary
userAttributes = {
    "cartIsEmpty": True,
    "shopping_cart": [], #Initially, the shopping cart will be empty since there is no database

}

#This function will clear the console
def clearText():
    os.system('cls' if os.name == 'nt' else 'clear')

#function to wait for the user to do something
def helpPause():
    input("\n Press Enter to return to the menu.")

#Add items towards the shopping cart
def addItem():
    pass

#Update items from the shopping cart
def updateItem():
    pass

#Delete items from the shopping cart
def deleteItem():
    pass

#This function will display the users shopping cart
def checkCart():
    pass


#This function will run the main function.
def main():
    print("Welcome to this program! We are selling these things!")
    answer = input("Would you like to proceed!").lower().strip()
    
