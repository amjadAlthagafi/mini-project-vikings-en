from vikingsClasses import Viking, Saxon, War
import random
import time

CLASSMATES_NAMES = [
    "Ahmed", "Fatima", "Mohammed", "Zainab", "Omar",
    "Aisha", "Khalid", "Layla", "Ali", "Mariam"
]
def create_random_viking():
    name = random.choice(CLASSMATES_NAMES)
    health = random.randint(50, 100)
    strength = random.randint(30, 60)
    return Viking(name, health, strength)
def create_random_saxon():
    health = random.randint(40, 80)
    strength = random.randint(20, 50)
    return Saxon(health, strength)
def create_teams(viking_count=5, saxon_count=5):
    war = War()
    for _ in range(viking_count):
        war.addViking(create_random_viking())
    for _ in range(saxon_count):
        war.addSaxon(create_random_saxon())
    return war

def print_army_status(war):
    print(f"\n⚔️  Viking Army: {len(war.vikingArmy)} warriors")
    print(f"🛡️  Saxon Army: {len(war.saxonArmy)} warriors\n")

def run_game():
    print("""
    =============================
       VIKINGS VS SAXONS WAR
    =============================
    """)
   
    battle = create_teams(
        viking_count=random.randint(3, 7),
        saxon_count=random.randint(3, 7)
    )
    
    round_number = 1
    
    while True:
        print(f"\n🔥 Round {round_number} 🔥")
        print_army_status(battle)
        
    
        print("⚔️ Viking Attack!")
        time.sleep(1)
        result = battle.vikingAttack()
        print(f" → {result}")
        
    
        print("\n🛡️ Saxon Counterattack!")
        time.sleep(1)
        result = battle.saxonAttack()
        print(f" → {result}")
        
    
        time.sleep(1.5)
        status = battle.showStatus()
        print("\n" + "="*40)
        print(status)
        print("="*40)
        
   
        if "won" in status:
            break
            
        round_number += 1
        time.sleep(2)

if __name__ == "__main__":
    run_game()