

# name: fill_table
# description: fills the table with a dictionary where the name of the person
# is the key and the amount spent is the value
# preenchendo registro


def fill_table(t:list, person:dict) -> None:
    person['name'] = input('Name: ')
    person['amount'] = float(input("Amount spent: $ "))
    t.append(person.copy())

# name: calculte_debts
# description: it will do the math so everyone in the group had spent the same amount
# It will return the amount and to whom the person needs to transfer
def calculate_debt(t:list) -> list:
    # calculate the total amount spent (total) and split in equal parts(med)
    total = 0
    for person in t:
        total += person['amount']
    med = total / len(t)

    # intialize dictionaries to keep people who will receive and who will pay
    creditors = {}
    debtors = {}

    # calculates who's in debt who's with credit
    for person in t:
        name = person['name']
        amount = person['amount']
        balance = amount - med
        if balance < 0:
            debtors[name] = -balance
        elif balance > 0:
            creditors[name] =  balance

    result = []
    
    #calculates who's gonna pay whom and format the string
    for creditor, credit in creditors.items():
        for debtor, debt in debtors.items():
            if credit == 0:
                break
            if debt == 0:
                continue
            payment = min(credit,debt)
            result.append(f"{debtor} owes ${payment:.2f} to {creditor}\n")
            credit -= payment
            debt -= payment

    return result

    
            