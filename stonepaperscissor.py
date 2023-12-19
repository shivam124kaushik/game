while True:
    import random
    computer=random.randrange(1,3)
    user=int(input(
    '''enter your choice
    1 - stone
    2- paper
    3 - scissor'''))
    choices = {1: 'Stone', 2: 'Paper', 3: 'Scissors'}
    print(f"You choose {choices[user]}.")
    print(f"The computer choose {choices[computer]}.")
    if(user == 1 and computer == 1):
        print("tie")
    elif(user == 2 and computer == 3):
        print("computer win")
    elif(user == 3 and computer == 2):
        print("user win")
    elif(user == 2 and computer == 2):
        print("tie")
    elif(user == 1 and computer == 2):
        print("computer win")
    elif(user == 2 and computer == 1):
        print("user win")
    elif(user == 3 and computer == 2):
        print("user win")
    elif(user == 3 and computer == 3):
        print("tie")
    elif(user == 3 and computer == 1):
        print("user win")
    elif(user == 3 and computer == 1):
        print("computer win")
    else:
        print("invalid input")

