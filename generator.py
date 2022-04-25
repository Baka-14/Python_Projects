import sys
import random

def main():
    print("Welcome to Random Food generator")
    flavours=("Vanilla",'Chocolate','Strawberry','Bubblegum',
               'Pista','Mirchi','Masala','Oreo','Mango','Caramel' )

    food=('Dosa','Idli','Paratha','Upma','Wada','Bonda'
            'Poha','Set_Dosa','Bajji')
    while True:
        a=random.choice(flavours)
        b=random.choice(food)
        print("\n\n")
        print("{}{}".format(a,b),file=sys.stder)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else Q to quit)\n ")
        if try_again.lower() == "q": 
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__": 
    main()
    