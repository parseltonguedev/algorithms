# question 5.1 - true
# question 5.2 - false
# question 5.3 - true
# question 5.4 - false


voted = {}


def check_voter(name):
    if voted.get(name):
        print('kick')
    else:
        voted[name] = True
        print("let them vote")


check_voter('sam')
check_voter('mike')
check_voter('sam')

# question 5.5 - 3, 4
# question 5.6 - 2, 5
# question 5.7 - 2, 3, 4
