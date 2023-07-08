print('You can choose to go to a city called Py, Trainbus or Fashion.')
choice = input('Type the destination which you want to go to with your ticket --> ')
destinations = ['py', 'trainbus', 'fashion']
if choice.lower() in destinations:
    print('You shall stay in', choice.lower().capitalize() + '.')
else:
    print('That destination is not available.')