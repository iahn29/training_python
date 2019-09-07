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

user_answer = 'B'

# Show random quote

if user_answer == "B":
  # leave the program
  pass
elif user_answer == "C":
  print("Désolé mauvaise réponse")
else:
  # Show another quote
  pass

def show_random_quote(my_list):
  # get a random number
  quote = my_list[0]
  print(quote)

show_random_quote(quotes)
