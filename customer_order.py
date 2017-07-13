# List of questions
questions = {
    "strong": "Do you like your drink strong?",
    "salty": "Do you like it with a salty tang?",
    "bitter": "Are you a lubber who likes it better?",
    "sweet": "Would you like a bit of sweetness with your poison?",
    "fruity": "Are you one for fruity finish?",
}

# List of ingredients
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of becon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def customer_order():
    """Creats a dictionary of the customer's order"""
    
    customer_resp = {}
    
    print ("Hey buddy!")
    qn1_ans = input (questions['strong'])
    if qn1_ans == "y" or qn1_ans == "yes":
        customer_resp['strong'] = True
    else:
        customer_resp["strong"] = False
    print ('bingo... \n')
    
    qn2_ans = input (questions['salty'])
    if qn2_ans == "y" or qn2_ans == "yes":
        customer_resp["salty"] = True
    else:
        customer_resp["salty"] = False
    print ('gotcha... \n')
    
    qn3_ans = input (questions['bitter'])
    if qn3_ans == "y" or qn3_ans == "yes":
        customer_resp["bitter"] = True
    else:
        customer_resp["bitter"] = False
    print ('right... \n')
    
    qn4_ans = input (questions['sweet'])
    if qn4_ans == "y" or qn4_ans == "yes":
        customer_resp["sweet"] = True
    else:
        customer_resp["sweet"] = False
    print ('Hmmm... \n')
    
    qn5_ans = input (questions['fruity'])
    if qn5_ans == "y" or qn5_ans == "yes":
        customer_resp["fruity"] = True
    else:
        customer_resp["fruity"] = False
    print ('Owkay! coming right up!')
    
    return customer_resp
    
if __name__ == '__name__':
    print (customer_order())