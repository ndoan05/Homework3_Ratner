# Nam Doan
# 1847037

count = 1
my_team = {}
new_team = {}

while count <= 5:
    jersey_num = int(input("Enter player %d's jersey number:\n" % count))
    rate_num = int(input("Enter player %d's rating:\n" % count))
    my_team[jersey_num] = rate_num
    list_jersey = list(my_team.keys())
    list_jersey = sorted(list_jersey)
    count += 1
    print()  

print("ROSTER")
for i in list_jersey:
    print("Jersey number: %d, Rating: %d" % (i, my_team[i]))

while True:
    list_jersey = list(my_team.keys())
    list_jersey = sorted(list_jersey)
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    option = input("\nChoose an option:\n")
    if option == "q":
        exit()
    elif option == "o":
        print()
        print("ROSTER")
        for i in list_jersey:
            print("Jersey number: %d, Rating: %d" % (i, my_team[i]))
    elif option == "a":
        jersey_num2 = int(input("Enter a new player's jersey number:\n"))
        rate_num2 = int(input("Enter the player's rating:"))
        new_team[jersey_num2] = rate_num2
        my_team.update(new_team)
    elif option == "d":
        jersey_remove = int(input("Enter a jersey number:\n"))
        my_team.pop(jersey_remove)
    elif option == "u":
        jersey_update = int(input("Enter a jersey number:\n"))
        rate_update = int(input("Enter a new rating for player:\n"))
        my_team[jersey_update] = rate_update
    elif option == "r":
        rate_above = int(input("Enter a rating:\n"))
        print()
        print("ABOVE %d" % rate_above)
        for jersey, rate in my_team.items():
            if rate > rate_above:
                print("Jersey number: %d, Rating: %d" % (jersey, rate))
            if rate <= rate_above:
                continue
