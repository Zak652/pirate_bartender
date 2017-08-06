# List of questions
questions = {
    "strong": "Do you like your drink strong?",
    "salty": "Do you like it with a salty tang?",
    "bitter": "Are you a lubber who likes it better?",
    "sweet": "Would you like a bit of sweetness with your poison?",
    "fruity": "Are you one for fruity finish?"
}

# We now need to ask the customer what type of drink they want
def drink_order():
    """collects customer drink preferences by asking them a question"""
    
    order_pref = {}
    
    allowed = ['y', 'yes', 'yeah', 'yep']
    
    for drink_type in questions:
        ans = input('{}: '.format(questions[drink_type]))
        ans = ans.lower()
        
        if ans in allowed:
            order_pref[drink_type] = True
        else:
            order_pref[drink_type] = False
        
    return order_pref
    
if __name__ == '__main__':
    drink_order()
