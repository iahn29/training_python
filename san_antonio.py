# -*- coding: utf8 -*-

import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item_in(my_list):
  rand_index = random.randint(0, len(my_list) - 1) # random index
  item = my_list[rand_index] # get a quote from the list
  return(item) #r return the item

def message(character, quote):
  n_character=character.capitalize()
  n_quote=quote.capitalize()
  return "{} a dit : {}".format(n_character,n_quote)

user_answer = "" 

while user_answer != "q":
  print(message(get_random_item_in(characters),get_random_item_in(quotes)))
  user_answer = input('Tapez entrée pour connaitre une autre citation ou q pour quitter le programme.') 
