import random

player_score = 0
cpu_score = 0

while(True):
    player_choice = int(input("enter R for rock P for paper and S for scissors: "))
    cpu_choice = random.randint(1,3)

    if player_choice == cpu_choice:
        print('its a tie no points will be awarded')

        elif player_choice == "R":
            if cpu_choice == "P":
                print('cpu chose paper and won this round')
                cpu_score += 1
                print('cpu score: ' + str(cpu_score) + '\n' + 'your score: ' + str(player_score))

                if cpu_choice == "S":
                    print('cpu chose scissors. You won this round')
                    player_score += 1
                    print('cpu score: ' + str(cpu_score) + '\n' + 'your score: ' + str(player_score))


                    elif player_choice == "P":
                        if cpu_choice == "R":
                            print('cpu chose rock. You won this round')
                            player_score += 1
                            print('cpu score: ' + str(cpu_score) + '\n' + 'your score' + str(player_score))

                            if cpu_choice == "S":
                                print('cpu chose scissors and won this round')
                                cpu_score += 1
                                print('cpu score: ' + str(cpu_score) + '\n' + 'your score' + str(player_score))


                                else:
                                    if cpu_choice == "R":
                                      print('cpu chose rock and won this round')
                                      player_score += 1
                                      print('cpu score: ' + str(cpu_score) + '\n' + 'your score' + str(player_score))

                                    if cpu_choice == "P":
                                      print('cpu chose paper. You won this round')
                                      cpu_score += 1
                                      print('cpu score: ' + str(cpu_score) + '\n' + 'your score' + str(player_score))

            if player_score == 2:
                print('You won! Best two out of 3! ')
                break

            if cpu_score == 2:
                print('cpu won, sorry but you have lost! ')
                break
