#Codsoft Internship
#Task-4 Rock,paper,scissor game
import random
def winner(user_choice,com_choice):
    
    if user_choice==com_choice:
        return 'Its Tie'
    elif user_choice =='rock'and com_choice=='scissor' or user_choice=='scissor'and com_choice =='paper' or user_choice=='paper'and com_choice=='rock':
        return("You win")
    else:
        return f'You lose!'
def Game():
     user_choice=input("choose Rock,paper or scissors:").lower()
     com_choice=random.choice(['rock','paper','scissor'])
     if user_choice not in['rock','paper','scissor']:
        print("Enter valid choices")
        Game()
        print(f'user_score:{user_choice}\n computer_Score:{com_choice}')
     result=winner(user_choice,com_choice)
     return result


def main():
    user_score=0
    com_score=0
    while True:
        result=Game()
        if 'win' in result:
            user_score+=1
        elif'lose'in result:
            com_score+=1
        print(f'user score:{user_score}\nComputer score:{com_score}')
        playagain=input('Do you want to play again yes or no: ').lower()
        if playagain != 'yes':
            print("Thank you..")
            break   
    if user_score>com_score:
        print("You Win")
    elif user_score==com_score:
        print("Its Tie")
    else:
        print("You Lose")
if __name__=="__main__":
    main()
   
    
    

        