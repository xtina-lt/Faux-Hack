# 1) acquire access to fender's systems
# 2) update passwords file
# 3) add signiture

'''1) READING THE PASSWORDS'''
# 1) import
import json
import csv

# 2)initiate storage variables
compromised_users = []
passwords = []

# 3) Context manager
with open('passwords.csv') as csv_file:
    # 4) .DictReader
    # saves as dictionary
    # incase different delimeter:
    # np_reader = csv.DictReader(np_users, delimiter=';')
    csv_file_reader = csv.DictReader(csv_file)
    for row in csv_file_reader:
        # 5) iterate through dictionary, append to variable
        # # except first line
        passwords.append(row['Password'])
        compromised_users.append(row['Username'])

'''2) Save compromised users'''
with open('compromised_users.txt', 'w') as compromised_user_file:
    for i in compromised_users:
        compromised_user_file.write(i)

'''Notify Boss'''
#import json
with open('boss_message.json', 'w') as boss_message:
    dict = {
        'recipient': 'The Boss',
        'message': 'Mission Success'
    }
    json.dump(dict, boss_message)

'''Scrambling Password'''
# frame someone else by using their signiture
# this is the file that will replace passwords
with open('new_passwords.csv', 'w') as new_passwords_obj:
    frame_signiture = '''
    _  _     ___   __  ____             
    / )( \   / __) /  \(_  _)            
    ) \/ (  ( (_ \(  O ) )(              
    \____/   \___/ \__/ (__)             
    _  _   __    ___  __ _  ____  ____  
    / )( \ / _\  / __)(  / )(  __)(    \ 
    ) __ (/    \( (__  )  (  ) _)  ) D ( 
    \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
            ____  __     __   ____  _  _ 
    ___   / ___)(  )   / _\ / ___)/ )( 
    (___)  \___ \/ (_/\/    \___ \) __ (
        (____/\____/\_/\_/(____/\_)(_/
    __ _  _  _  __    __                
    (  ( \/ )( \(  )  (  )               
    /    /) \/ (/ (_/\/ (_/\             
    \_)__)\____/\____/\____/
    '''
    new_passwords_obj.write(frame_signiture)
