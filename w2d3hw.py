#!/usr/bin/env python
# coding: utf-8

# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

# In[8]:


from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?


def shopping_cart():
    cart = {}
    count = 1
    item_found = False
    while True:
        action = input('Do you want to : Show/Add/Delete or Quit? ')
        if action.lower()=='show' or action.lower()=='s':
            print("Here is your shopping cart: ")
            for k,v in cart.items():
                print(f"{k}: {v}")
        elif action.lower()=='add' or action.lower()=='a':
            to_add = input('What would you like to add? ')
            cart[count] = to_add
            count += 1
        elif action.lower()=='delete' or action.lower()=='d':
            to_delete = input('What do you want to delete? ')
            for key, value in cart.items():
                if str(key)==to_delete or value==to_delete:
                    del cart[key]
                    item_found = True
                    break
            if not item_found:
                print("It looks like that number/item isn't in your cart. ")
        elif action.lower()=='quit' or action.lower()=='q':
            print('Quitting...')
            for k,v in cart.items():
                print(f"{k}: {v}")
            break
        else:
            print("Sorry, I don't recognize that command.")


# In[9]:


shopping_cart()


# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# In[2]:


import calcmod

#for area, input two values one for length and one for width
#for circumference input radius

print(calcmod.area())
print(calcmod.circ())


# In[ ]:




