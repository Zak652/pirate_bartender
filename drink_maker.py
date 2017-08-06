# Import customer_order and random functions
import customer_order
import random

# List of ingredients
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of becon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def make_drink ():
    """Makes a drink based on customer order preferences"""
    
    customer_pref = customer_order.drink_order()
    drink = []
    
    for pref in customer_pref:
        if customer_pref[pref] == True:
            drink.append(random.choice(ingredients[pref]))
    
    return drink
    
if __name__ == '__main__':
    print (make_drink)
