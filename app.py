# slot machine game
import time as time
import random 

#Constants

NUM_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# rows and col symbols

Symbol_count = {
    "A":2,
    "B":4,
    "C":5,
    "D":8,
}

Symbol_value = {
    "A":8,
    "B":4,
    "C":3,
    "D":2,
}

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns    

def print_slots(columns): #transpose matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end= "")   
        print()

def is_winner(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for colum in columns:
            symbol_check = columns[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

print("Loading Slot Machine...")
time.sleep(1)

# put in money
def deposit():
    while True:
        userMoney = input("Add money to the machine: $")
        if userMoney.isdigit():
            money = int(userMoney)
            if money > 0 and money >= 10:
                print ("you have deposited $%s" % money)
                break
            else:
                print("please enter a propler amount over $10 ")
        else: print("Please enter a number")          

    return money    

def get_lines():
    while True:
        lines = input("How many lines do you want to play? 1 -" + (str(NUM_LINES)) + "?: " )
        if lines.isdigit():
            Num_lines = int(lines)
            if Num_lines > 0 and Num_lines <= NUM_LINES:
                print ("you have picked %s of lines" % Num_lines)
                break
            else:
                print("please enter a propler line amount ")
        else: print("Please enter a number")          

    return Num_lines    

def get_bet(lines, balance):
    while True:
        amount = input("How much to bet per line? $")
        if amount.isdigit():
            bet_amount = int(amount)
            if bet_amount >= MIN_BET and bet_amount <= MAX_BET:
                print (f"your total bet amount is ${bet_amount} over {lines} lines!")
                total_bet = bet_amount * lines
                if total_bet > balance:
                    print("you dont have enough to make that bet")
                    print(f"your total bet is ${total_bet} and you only have ${balance} left")
                else: break;    
            else: print(f"You must be ${MIN_BET} and ${MAX_BET} per line")
        else: print("please enter a number")                
    return total_bet 
        


## not finished yet need to work out balance bug
def Main():
    balance = deposit() #set starting amount
    while True:       
        lines_bet = get_lines() # set lines to play
        total_bet = get_bet(lines_bet, balance) #get total bet
        current_balance = balance - total_bet 
        print(f"Your total bet is ${total_bet}")
        columes_spun = get_slot_spin(ROWS,COLS,Symbol_count) # run algo to spin symbols
        print("Spinning...")
        time.sleep(1) # for effet
        print_slots(columes_spun) ## print out slots
        winning = is_winner(columes_spun, lines_bet, total_bet, Symbol_value)
        print(f"you won {winning}") 
        current_balance = total_bet + winning   
        print(f"your remaining funds are ${current_balance}")
        current_balance += winning
        if current_balance <= 0:
            print("Your out of money!!!")
            break
# start program
Main()