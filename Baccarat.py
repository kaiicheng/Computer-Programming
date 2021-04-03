import random

houseman_list = []
player_list = []

while True:
    # Set number of houseman's four dices.
    h_dice1 = random.randint(1, 6)
    h_dice2 = random.randint(1, 6)
    h_dice3 = random.randint(1, 6)
    h_dice4 = random.randint(1, 6)
    houseman_list = [h_dice1, h_dice2, h_dice3, h_dice4]
    houseman_list_final = [h_dice1, h_dice2, h_dice3, h_dice4]
    houseman_list_final.sort()
    # print(houseman_list)

    # Store number of four dices in houseman_list.
    h_dice1_count = houseman_list.count(houseman_list[0])
    h_dice2_count = houseman_list.count(houseman_list[1])
    h_dice3_count = houseman_list.count(houseman_list[2])
    h_dice4_count = houseman_list.count(houseman_list[3])
    # print(h_dice1_count)
    # print(h_dice2_count)
    # print(h_dice3_count)
    # print(h_dice4_count)
    h_total_count = h_dice1_count + h_dice2_count + h_dice3_count + h_dice4_count

    # Situation when the houseman has two pairs of same number or one pair of same number.
    # [2, 2, 4, 4] => count=2+2+2+2=8. [2, 2, 4, 6] => count=2+2+1+1=6
    if h_total_count >= 6:
        # Situation when the houseman has three dices with same number => shuffle again.
        # [2, 2, 2, 4] => count=3+3+3+1=10
        if h_total_count == 10:
            pass
        elif h_total_count == 16:
            houseman_point = 100
        else:
            # Situation when the houseman has two pairs of same number.
            if h_total_count == 8:
                houseman_point = max(houseman_list)
                break
            # Situation when the houseman has one pair of same number and other two different number.
            else:
                if h_dice1_count == 2:
                    # print(houseman_list)
                    # print(h_dice1)
                    houseman_list.remove(h_dice1)
                    houseman_list.remove(h_dice1)
                    houseman_point = houseman_list[0] + houseman_list[1]
                    break
                else:
                    if h_dice2_count == 2:
                        # print(houseman_list)
                        # print(h_dice2)
                        houseman_list.remove(h_dice2)
                        houseman_list.remove(h_dice2)
                        houseman_point = houseman_list[0] + houseman_list[1]
                        break
                    else:
                        if h_dice3_count == 2:
                            # print(houseman_list)
                            # print(h_dice3)
                            houseman_list.remove(h_dice3)
                            houseman_list.remove(h_dice3)
                            houseman_point = houseman_list[0] + houseman_list[1]
                            break
                        else:
                            if h_dice4_count == 2:
                                # print(houseman_list)
                                # print(h_dice4)
                                houseman_list.remove(h_dice4)
                                houseman_list.remove(h_dice4)
                                houseman_point = houseman_list[0] + houseman_list[1]
                                break

# print("houseman_point: ", end="")
# print(houseman_point)

while True:
    # Set number of player's four dices.
    p_dice1 = random.randint(1, 6)
    p_dice2 = random.randint(1, 6)
    p_dice3 = random.randint(1, 6)
    p_dice4 = random.randint(1, 6)
    player_list = [p_dice1, p_dice2, p_dice3, p_dice4]
    player_list_final = [p_dice1, p_dice2, p_dice3, p_dice4]
    player_list_final.sort()
    # print(player_list)

    # Store number of four dices in houseman_list.
    p_dice1_count = player_list.count(player_list[0])
    p_dice2_count = player_list.count(player_list[1])
    p_dice3_count = player_list.count(player_list[2])
    p_dice4_count = player_list.count(player_list[3])
    # print(p_dice1_count)
    # print(p_dice2_count)
    # print(p_dice3_count)
    # print(p_dice4_count)
    p_total_count = p_dice1_count + p_dice2_count + p_dice3_count + p_dice4_count

    # Situation when the player has two pairs of same number or one pair of same number.
    # [2, 2, 4, 4] => count=2+2+2+2=8. [2, 2, 4, 6] => count=2+2+1+1=6
    if p_total_count >= 6:
        # Situation when the player has three dices with same number => shuffle again.
        # [2, 2, 2, 4] => count=3+3+3+1=10
        if p_total_count == 10:
            pass
        elif p_total_count == 16:
            player_point = 100
        else:
            # Situation when the player has two pairs of same number.
            if p_total_count == 8:
                player_point = max(player_list)
                break
            # Situation when the player has one pair of same number and other two different number.
            else:
                if p_dice1_count == 2:
                    player_list.remove(p_dice1)
                    player_list.remove(p_dice1)
                    player_point = player_list[0] + player_list[1]
                    break
                else:
                    if p_dice2_count == 2:
                        player_list.remove(p_dice2)
                        player_list.remove(p_dice2)
                        player_point = player_list[0] + player_list[1]
                        break
                    else:
                        if p_dice3_count == 2:
                            player_list.remove(p_dice3)
                            player_list.remove(p_dice3)
                            player_point = player_list[0] + player_list[1]
                            break
                        else:
                            if p_dice4_count == 2:
                                player_list.remove(p_dice4)
                                player_list.remove(p_dice4)
                                player_point = player_list[0] + player_list[1]
                                break

# print("player_point: ", end="")
# print(player_point)

print("莊家點數 ", end="")
print(houseman_list_final)

print("玩家點數 ", end="")
print(player_list_final)

if player_point == 100:
    print("玩家", end="")
    print("\"BOW-GI\"")
elif houseman_point == 100:
    print("莊家", end="")
    print("\"BOW-GI\"")
else:
    if player_point > houseman_point:
        print("玩家winner")
    elif player_point == houseman_point:
        print("莊家winner")
    else:
        print("莊家winner")
