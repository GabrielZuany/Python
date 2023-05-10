#Build a program that have a function called by 'vote()', witch will recieve as parameter a person birth date and return if this person has mandatory vote, denied vote or optional vote.
def vote(year):
    """
    Description: =>This function will calculate the vote situation based on birth year.
    
    Args:
        year (int): birth year.
    """
    from datetime import date #Reduces memory cost. Will be used only when the function was called.
    today = date.today().year
    print(f'You have {today - year} years.')
    if today - year < 18:
        print('VOTE DENIED!')
    elif today - year > 65:
        print('OPTIONAL VOTE!')
    else:
        print('MANDATORY VOTE!')
    
#----------MAIN----------

birth = int(input('Insert your birth year: '))
vote(birth)