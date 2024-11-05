
import time
from spin import spin_row
from print_r import print_row
from payout import get_payout


def main():
    balance = 100
    print("************************")
    print("Welcome to Python Slots.")
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")
    
    while balance > 0:
        print("-------------------------------------")
        print(f"Current Balance: Rs. {balance}")
        bet = input("Place your bet amount:")
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        time.sleep(2)
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
            print(f"congratulations!!!. You have won a amount of Rs.{payout}")
            
        else:
            print(":(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(")
            print("Sorry, you lost amount.")
            
        balance += payout
        
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        
        if play_again != "Y":
            break
    
    print("**************************************************")    
    print(f"Game Over!!! Your final balance is: Rs.{balance}")
    print("**************************************************")  
    
        
        
        
        
    


if __name__ == "__main__":
    main()