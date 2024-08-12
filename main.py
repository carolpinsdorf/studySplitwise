import os
from library import *
import time
os.system("clear")

# This system will work in a similar way as "SplitWise app" works.
# It will receive the the name and the amount spent in group/party
# and it will do the math so everyone in the group had spent the same amount
# It will return the amount and to whom the person needs to transfer the
#  money, so they are all even in the end.
# By: Carolina Pinsdorf 
# 12th Aug, 2024


# creating a table with people's names and amount spent
table = list()
person = {
    'name':'',
    'amount': 0,
}

# calling function to fill in the table
print(f"Let's create your party group!\n")
while True:
    fill_table(table,person)
    toContinue = input("Are you done?\nPress enter to continue OR Press any key to finish\n")
    if toContinue:
        break

# clean the terminal and show results
os.system("clear")
print(f"Now,let me do the math!\n")
time.sleep(2)

# calling function to do the math
result = calculate_debt(table)
for line in result:
    print(line)

    