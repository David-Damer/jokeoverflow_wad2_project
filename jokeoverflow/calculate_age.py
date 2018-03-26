from datetime import date
'''
function to calculate registered users age
to restrict unsuitable content
'''

def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
