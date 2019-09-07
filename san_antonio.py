# -*- coding: utf8 -*-

import random
import json

'''quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]'''

'''characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]'''

def read_value_from_json(file_name,key):
  values = []
  # Open the json file
  with open(file_name) as f:
    # Load file data in data
    data = json.load(f)
    for entry in data:
      values.append(entry[key])
    return values
   
def get_random_item_in(my_list):
  rand_index = random.randint(0, len(my_list) - 1) # random index
  item = my_list[rand_index] # get a quote from the list
  return(item) #r return the item

def get_random_character():
  characters = read_value_from_json("characters.json","character")
  return get_random_item_in(characters)

def get_random_quote():
  quote = read_value_from_json("quotes.json","quote")
  return get_random_item_in(quote)

def message(character, quote):
  n_character=character.capitalize()
  n_quote=quote.capitalize()
  return "{} a dit : {}".format(n_character,n_quote)

user_answer = "" 

while user_answer != "q":
  print(message(get_random_character(),get_random_quote()))
  user_answer = input('Tapez entrée pour connaitre une autre citation ou q pour quitter le programme.') 

