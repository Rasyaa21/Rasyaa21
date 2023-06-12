import random
running = True
player_score = 0
computer_score = 0

pilih = ["batu", "gunting", "kertas"]
while running == True:
    player = pilih[int(input("Pilih Batu [1], Gunting [2], atau Kertas [3]  : "))-1]
    computer = random.choice(pilih)
    if player == computer:
        print("seri. Player dan komputer memilih "  + computer)
    else:
        print("Player memilih " + player + " vs Komputer memilih " + computer)
        if player == "batu" and computer == "kertas":
            
            computer_score = computer_score + 1
            print("computer menang :) - score :" + str(computer_score))
        elif player == "gunting" and computer == "batu":
            
            computer_score = computer_score + 1
            print("computer menang :) - score :" + str(computer_score))
        elif player == "kertas" and computer == "gunting":
            
            computer_score = computer_score + 1
            print("computer menang :) - score :" + str(computer_score))
        elif player == "kertas" and computer == "batu":
            
            player_score = player_score + 1
            print("player menang :) - score" + str(player_score))
        elif player == "batu" and computer == "gunting":
            
            player_score = player_score + 1
            print("player menang :) - score" + str(player_score))
        elif player == "gunting" and computer == "kertas":
            
            player_score = player_score + 1
            print("player menang :) - score" + str(player_score))
    if player_score == 10 or computer_score == 10:
        if player_score == 10:
            print("player menang")
        else:
            print("computer menang")
        print("Permainan selesai !")
        playagain = input("apakah ingin melanjutkan permainan y/n ? :")
        if playagain.lower() == "y":
            player_score = 0 
            computer_score = 0
        else: 
            running = False
print("terimakasih sudah bermain")



