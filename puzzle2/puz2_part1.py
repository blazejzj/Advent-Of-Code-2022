

def get_value_based_on_choice(choice: str) -> int:
    if(choice == "X" or choice == "A"):
        return 1
    elif(choice == "Y" or choice == "B"):
        return 2
    elif(choice == "Z" or choice == "C"):
        return 3

def my_choice_vs_opponent_choice(my_choice: str, opponent_choice: str):


    # C,Z Scissors
    # A,X Rock
    # B,Y Paper
    if opponent_choice == "A" and my_choice == "Y":
        return 6
    elif opponent_choice == "A" and my_choice == "X":
        return 3
    elif opponent_choice == "A" and my_choice == "Z":
        return 0

    elif opponent_choice == "B" and my_choice == "Y":
        return 3
    elif opponent_choice == "B" and my_choice == "X":
        return 0
    elif opponent_choice == "B" and my_choice == "Z":
        return 6

    elif opponent_choice == "C" and my_choice == "Y":
        return 0
    elif opponent_choice == "C" and my_choice == "X":
        return 6
    elif opponent_choice == "C" and my_choice == "Z":
        return 3


with open('puz2_input.txt', 'r') as file:

    sum = 0

    for line in file:
        opponent_char = line[0]
        my_char = line[2]
        #print(opponent_char, my_char)
        
        score_my_char = get_value_based_on_choice(my_char)
        sum = sum + score_my_char + my_choice_vs_opponent_choice(my_char, opponent_char)
        #print(f"{get_value_based_on_choice(opponent_char)} {get_value_based_on_choice(my_char)}")
        #print(score_my_char + my_choice_vs_opponent_choice(my_char, opponent_char))
        #print(f"Points because of win = {my_choice_vs_opponent_choice(my_char, opponent_char)}, Points because of choice = {get_value_based_on_choice(my_char)}")
    print(sum)
    



