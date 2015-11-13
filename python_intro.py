temperature = int(input('What\'s the temperature?'))
if temperature < 0:
    print('Can\'t feel my hands')
elif 0 <= temperature < 10:
    print('It\'s kinda cold')
elif 10 <= temperature < 20:
    print('Cool but ok')
elif 20 <= temperature < 27:
    print('Perfect weather, isn\'t it?')
elif 27<= temperature < 37:
    print('I\'m not telling that it\'s hot but two hobbits just came into my room and throw out a ring')
else:
    print('unknown')
