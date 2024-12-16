import random

list = ['water','snack','gun']


pc_choise = random.choice(list)


print("choose : 'water','snack','gun' :")
user_choise = str(input("choose the element according the list :"))
    
print("computer choos the : ",pc_choise)
print("you choose the : ",user_choise)


if(pc_choise == user_choise):
    print("you and pc choose same element its tie bro/sis")
    


if(pc_choise == 'water' and user_choise =='gun'):
    print("you are losser computer win ")
    
    
elif(pc_choise =='gun' and user_choise =='snack'):
    print("you are losser computer win ")
    
elif(pc_choise =='snack' and user_choise =='water'):
    print("you are losser computer win")
    
    
elif(user_choise not in list):
    print("what the fuck you doing get out from my code")
    
    
else:
    print("wow you win ")
    
    
            