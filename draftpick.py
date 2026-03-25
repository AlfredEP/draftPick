role_available = ["jungler", "midlaner", "roamer", "goldlaner", "explaner"]

role_owner = {}

#player 1 
while True:
    s1_choice = input("Enter player 1 role : ").lower()
    if s1_choice in role_available and s1_choice not in role_owner:
        role_owner[s1_choice] = "Player 1"
        break
    else:
        if s1_choice in role_owner:
            print(f"{s1_choice} is already taken by {role_owner[s1_choice]}. Please choose another role.")
        else:
            print("Invalid role. Try again.")

#player 2
while True:
    s2_choice = input("Enter player 2 role : ").lower()
    if s2_choice in role_available and s2_choice not in role_owner:
        role_owner[s2_choice] = "Player 2"
        break
    else:
        if s2_choice in role_owner:
            print(f"{s2_choice} is already taken by {role_owner[s2_choice]}. Please choose another role.")
        else:
            print("Invalid role. Try again.")

#Player 3
while True:
    s3_choice = input("Enter player 3 role : ").lower()
    if s3_choice in role_available and s3_choice not in role_owner:
        role_owner[s3_choice] = "Player 3"
        break
    else:
        if s3_choice in role_owner:
            print(f"{s3_choice} is already taken by {role_owner[s3_choice]}. Please choose another role.")
        else:
            print("Invalid role. Try again.")

#Player 4
while True:
    s4_choice = input("Enter player 4 role : ").lower()
    if s4_choice in role_available and s4_choice not in role_owner:
        role_owner[s4_choice] = "Player 4"
        break
    else:
        if s4_choice in role_owner:
            print(f"{s4_choice} is already taken by {role_owner[s4_choice]}. Please choose another role.")
        else:
            print("Invalid role. Try again.")

#Player 5
while True:
    s5_choice = input("Enter player 5 role : ").lower()
    if s5_choice in role_available and s5_choice not in role_owner:
        role_owner[s5_choice] = "Player 1"
        break
    else:
        if s5_choice in role_owner:
            print(f"{s5_choice} is already taken by {role_owner[s5_choice]}. Please choose another role.")
        else:
            print("Invalid role. Try again.")

# Display the roles of each player
print("\nRole picked:")
for role, player in role_owner.items():
    #print(f"Role of {player} : {role}")
    print("Role of " + player + " : " + role)
print("Welcome to Mobile Legends")