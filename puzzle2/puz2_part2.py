

def get_value_based_on_choice(choice: str) -> int:
    if(choice == "X" or choice == "A"):
        return 1
    elif(choice == "Y" or choice == "B"):
        return 2
    elif(choice == "Z" or choice == "C"):
        return 3

def get_new_choice(match: str, opponent_choice: str) -> str:

    if(opponent_choice == "A" and match == "X"):
        return "Z"
    elif(opponent_choice == "A" and match == "Y"):
        return "X"
    elif(opponent_choice == "A" and match == "Z"):
        return "Y"

    elif(opponent_choice == "B" and match == "X"):
        return "X"
    elif(opponent_choice == "B" and match == "Y"):
        return "Y"
    elif(opponent_choice == "B" and match == "Z"):
         return "Z"

    elif(opponent_choice == "C" and match == "X"):
        return "Y"
    elif(opponent_choice == "C" and match == "Y"):
        return "Z"
    elif(opponent_choice == "C" and match == "Z"):
        return "X"
    
    # X = need to Lose
    # Y = need to Draw
    # Z = need to Win

    # C,Z Scissors
    # A,X Rock
    # B,Y Paper

with open('puz2_input.txt', 'r') as file:

    sum = 0

    for line in file:

        opponent = char = line[0]
        my_char = line[2]
        
        round_score = 0
        if my_char == "X":
            round_score = 0
        elif my_char == "Y":
            round_score = 3
        elif my_char == "Z":
            round_score = 6

        new_choice = get_new_choice(my_char, opponent)
        new_choice_score = get_value_based_on_choice(new_choice)

        sum = sum + new_choice_score + round_score
    print(sum)
    



