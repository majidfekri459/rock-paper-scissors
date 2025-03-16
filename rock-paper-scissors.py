import random , os
os.system('cls')
dic_list={
    "s":"sang",
    "k":"kaghaz",
    "g":"gheichi"
}
user_scoer=0
ai_score=0 
while True:
    print
    vorodi= input("Open windows One or Tow. (1, 2, 3) , Exit Non_Alphanumeric and Integers ")
    if vorodi.isalnum():
        list_vorodi=["1", "2",'3']
        if vorodi in list_vorodi:
            if vorodi=="1":
                while True:
                    print("_"*10)
                    tedad_charkhsh=input( " Enter a Number for the game period or Exit the Alphabet game or ... ")
                    print("_"*10)
                    if tedad_charkhsh.isdigit():
                        if int(tedad_charkhsh) >0:
                            i=0
                            while i < int(tedad_charkhsh):
                                user=input(" sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                                print("_"*10)
                                list_entkhab=["s", "k", "g"]
                                ai1=random.choice(list_entkhab)
                                if user in list_entkhab:
                                    if user== ai1:
                                        print("Equal =")
                                    elif( user == "s" and ai1== "g") or (user == "k" and ai1 == "s") or ( user =="g" and ai1 == "k") :
                                        user_scoer+=1
                                        print("User+1  User > Ai ")
                                    else:
                                        ai_score+=1
                                        print("Ai+1  Ai > User ")
                                    print("_"*10)
                                    print(f'User Choice {dic_list[user]} , Ai Choice {dic_list[ai1]} ')
                                    print(f'User Scoer {user_scoer}, Ai Scoer {ai_score}')
                                    print("_"*10)
                                else:
                                    print("_"*10)
                                    print('N0 , Choose only "s", "k" , "g" ')
                                    i-=1
                                    print("_"*10)
                                i+=1
                            if user_scoer > ai_score:
                                print("User win! ")
                                print("_"*10)
                            elif user_scoer < ai_score:
                                print("Ai win! ")
                                print("_"*10)
                            else:
                                print("Equal = ")
                                print("_"*10)
                            user_scoer=0
                            ai_score=0    
                    elif tedad_charkhsh.isalpha():
                        break


            elif vorodi=='2':
                print("_"*10)
                chakhsh=(input("The Number of Rounds you have to win < User or Ai> Exit anything nut a Number  "))
                print("_"*10)
                if chakhsh.isdigit():
                    while True:
                        user=input(" sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                        print("_"*10)
                        list_entkhab=["s", "k", "g"]
                        ai1=random.choice(list_entkhab)
                        if user in list_entkhab:
                            print(f'User Choice {dic_list[user]} , Ai Choice {dic_list[ai1]} ')
                            if user== ai1:
                                print("Equal =")
                            elif( user == "s" and ai1== "g") or (user == "k" and ai1 == "s") or ( user =="g" and ai1 == "k") :
                                user_scoer+=1
                                print("User+1 User > Ai ")
                            else:
                                ai_score+=1
                                print("Ai+1 Ai > User ")
                            print("_"*10)
                        else:
                            print('N0 , Choose only "s", "k" , "g" ')
                            print("_"*10)
                        print(f'User Scoer {user_scoer}, Ai Scoer {ai_score}')
                        if user_scoer==int(chakhsh) or ai_score==int(chakhsh):
                            break
                    if user_scoer < ai_score:
                        print("Ai Won! ")
                        print("_"*10)
                    else:
                        print("User Won! ")
                        print("_"*10)
                elif chakhsh.isalpha():
                    pass
                user_scoer=0
                ai_score=0
            else:
                vorodi1= input("Open windows One or Tow. (1, 2) , Exit Non_Alphanumeric and Integers ")
                if vorodi1.isdigit():
                    if vorodi1 in ['2','1']:
                        if vorodi1=='1':
                            while True:
                                print("_"*10)
                                tedad_charkhsh=input( "Enter a Number for the game period or Exit the Alphabet game or ... ")
                                print("_"*10)
                                if tedad_charkhsh.isdigit():
                                    if int(tedad_charkhsh) >0:
                                        i=0
                                        while i < int(tedad_charkhsh):
                                            user=input("User1 sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                                            print("_"*10)
                                            list_entkhab=["s", "k", "g"]
                                            ai1=input("User2 sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                                            if user in list_entkhab and ai1 in list_entkhab :
                                                if user== ai1:
                                                    print("Equal =")
                                                elif( user == "s" and ai1== "g") or (user == "k" and ai1 == "s") or ( user =="g" and ai1 == "k") :
                                                    user_scoer+=1
                                                    print("User1 +1  User1 > User2 ")
                                                else:
                                                    ai_score+=1
                                                    print("User2 +1  User2 > User1 ")
                                                print("_"*10)
                                                print(f'User1 Choice {dic_list[user]} , User2 Choice {dic_list[ai1]} ')
                                                print(f'User1 Scoer {user_scoer}, User2 Scoer {ai_score}')
                                                print("_"*10)
                                            else:
                                                print("_"*10)
                                                print('N0 , Choose only "s", "k" , "g" ')
                                                i-=1
                                                print("_"*10)
                                            i+=1
                                        if user_scoer > ai_score:
                                            print("User1 win! ")
                                            print("_"*10)
                                        elif user_scoer < ai_score:
                                            print("User2 win! ")
                                            print("_"*10)
                                        else:
                                            print("Equal = ")
                                            print("_"*10)
                                        user_scoer=0
                                        ai_score=0    
                                elif tedad_charkhsh.isalpha():
                                    break
                        else:
                            while True:
                                print("_"*10)
                                chakhsh=(input("The Number of Rounds you have to win < User or Ai> Exit anything nut a Number "))
                                print("_"*10)
                                if chakhsh.isdigit():
                                    while True:
                                        list_entkhab=["s", "k", "g"]
                                        user=input("User1 sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                                        print("_"*10)
                                        ai1=input("User2 sang= Rock, kaghaz= Paper, gheichi= Scissors. (s, k, g) ")
                                        if user in list_entkhab and ai1 in list_entkhab :
                                            print(f'User1 Choice {dic_list[user]} , User2 Choice {dic_list[ai1]} ')
                                            if user== ai1:
                                                print("Equal =")
                                            elif( user == "s" and ai1== "g") or (user == "k" and ai1 == "s") or ( user =="g" and ai1 == "k") :
                                                user_scoer+=1
                                                print("User1 +1 User1 > User2 ")
                                            else:
                                                ai_score+=1
                                                print("User2 +1 User2 > User1 ")
                                            print("_"*10)
                                        else:
                                            print('N0 , Choose only "s", "k" , "g" ')
                                            print("_"*10)
                                        print(f'User1 Scoer {user_scoer}, User2 Scoer {ai_score}')
                                        if user_scoer==int(chakhsh) or ai_score==int(chakhsh):
                                            break
                                    if user_scoer < ai_score:
                                        print("User2 Won! ")
                                        print("_"*10)
                                    else:
                                        print("User1 Won! ")
                                        print("_"*10)
                                elif chakhsh.isalpha():
                                    break
                                user_scoer=0
                                ai_score=0
        else:
            print("_"*10)
            print("N0 , Just Choose 1 or 2 and 3")
        print("_"*10)
    else:
        print("Exit")
        break

