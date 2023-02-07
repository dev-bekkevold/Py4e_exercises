date = int(input('What day of your cycle is it today? '))
if date <= 13:
    print('You are in your first phase')
elif date <= 20:
    print('You are in your second phase')
else:
    print('You are in your last phase')
    
    