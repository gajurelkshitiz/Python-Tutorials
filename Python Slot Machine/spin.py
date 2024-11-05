import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    
    results = [random.choice(symbols) for _ in range(3)]
    return results