#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

while True:

        hand= ["rock","paper","scisor"]
        roll= random.choice(hand)

        user = input("enter your choice-rock/paper/scisor?:")
        user_name= input("enter your name:")

        if (roll=="rock" and user=="paper") or (roll=="paper" and user== "scisor") or (roll== "scisor" and user== "rock"):      
            print(" congratulations!!!!!you won the game ")
            
        elif (roll== "paper" and user== "rock") or (roll=="scisor" and user== "paper") or (roll== "rock" and user== "scisor"):      
            print(" congratulations!!!!! computer won the game ")
            
        elif  (roll== "paper" and user== "paper") or (roll=="scisor" and user== "scisor") or (roll== "rock" and user== "rock"):      
            print(" game was tie")
            
        else:
            print("wrong entry .....please try again")
               
            


# In[ ]:





# In[ ]:




