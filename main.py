import re
email_condition = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
userinput_email = input('Enter email: ')
if (re.search(email_condition, userinput_email)):
    print('Yeah!!\nIt\'s a valid Email.')
else:
    print('Not an valid Email.')
