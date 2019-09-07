# -*- coding: utf8 -*-

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
  # TODO : get a random number
  item = my_list[0] # get a quote from the list
  return(item) #r return the item

user_answer = "" 

while user_answer != "q":
  print(get_random_item_in(quotes))
  user_answer = input('Tapez entrée pour connaitre une autre citation ou q pour quitter le programme.') 

for character in characters:
  m_character=character.capitalize()
  print(m_character)

