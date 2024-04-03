players = {
    'robert': {'position':'PG', 'jersey': 11} , 
    'james': {'position':'SG', 'jersey': 23}, 
    'mike': {'position':'shooting guard', 'jersey': 300}
             
             }

# Attempt to update it (this won't make sense in this structure as it might overwrite the whole dictionary)
players['robert'].update({'catch': 400, 'yard': 500})
players['james'].update({'catch': 300, 'yard': 400})
players['mike'].update({'catch': 200, 'yard': 300})




total = players['robert']['catch'] + players['robert']['yard']
total2 = players['james']['catch'] +  players['james']['yard']
total3 = players['mike']['catch'] + players['mike']['yard']


print(f" Robert total catch {total}")
print(f" James total catch {total2}")
print(f" Mike total catch {total3}")
print(players)
