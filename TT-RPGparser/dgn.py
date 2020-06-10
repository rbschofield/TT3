locations = {1: {'desc': 'You are at the entrance to the dungeon, with stairs leading down.',
                 'monster': '',
                 'mr': '',
                 'treasure': ''},
             2: {'desc': 'You are in a small room, 20x20ft, with a low ceiling.',
                 'monster': 'A single Orc.',
                 'mr': '10',
                 'treasure': '1'}}

choices = {1: {1: ('Descend the steps.', '>2'),
               2: ('Wait here.', '>1')},
           2: {1: ('Fight the Orc.', '!2'),
               2: ('Run up the steps!', '>1'),
               3: ('Run for the North exit.', '$L.>3')}}

print('LOCATIONS:')
print(locations)
print()
print(locations[1])
print()
print(locations[1]['desc'])
print(locations[1]['monster'])
print()
print(locations[2]['desc'])
print(), print()
print('CHOICES: ')
print(choices)
print()
print(choices[2][3])
print()
print(choices[2][3][0])
