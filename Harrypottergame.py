import random
import pyttsx3
from os import system 
def screen_clear():
    _=system('cls')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
wizard="""
 __          __  _                           __          ___                  _ 
 \ \        / / | |                          \ \        / (_)                | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   \ \  /\  / / _ ______ _ _ __ __| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   \ \/  \/ / | |_  / _` | '__/ _` |
    \  /\  /  __/ | (_| (_) | | | | | |  __/    \  /\  /  | |/ / (_| | | | (_| |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|     \/  \/   |_/___\__,_|_|  \__,_
"""
witch="""

 __          __  _                           __          ___ _       _     
 \ \        / / | |                          \ \        / (_) |     | |    
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   \ \  /\  / / _| |_ ___| |__  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   \ \/  \/ / | | __/ __| '_ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/    \  /\  /  | | || (__| | | |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|     \/  \/   |_|\__\___|_| |_|
                                                                           
                                                                           

"""

logo="""


 __    __  ____  _____   ____  ____   ___        _____  ____   ____  __ __  ______       ____   ____  ___ ___    ___ 
|  |__|  ||    ||     | /    ||    \ |   \      |     ||    | /    ||  |  ||      |     /    | /    ||   |   |  /  _]
|  |  |  | |  | |__/  ||  o  ||  D  )|    \     |   __| |  | |   __||  |  ||      |    |   __||  o  || _   _ | /  [_ 
|  |  |  | |  | |   __||     ||    / |  D  |    |  |_   |  | |  |  ||  _  ||_|  |_|    |  |  ||     ||  \_/  ||    _]
|  `  '  | |  | |  /  ||  _  ||    \ |     |    |   _]  |  | |  |_ ||  |  |  |  |      |  |_ ||  _  ||   |   ||   [_ 
 \      /  |  | |     ||  |  ||  .  \|     |    |  |    |  | |     ||  |  |  |  |      |     ||  |  ||   |   ||     |
  \_/\_/  |____||_____||__|__||__|\_||_____|    |__|   |____||___,_||__|__|  |__|      |___,_||__|__||___|___||_____|
                                                                                                                     




"""
user_win="""


____    ____  ______    __    __     ____    __    ____  ______   .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / /  __  \  |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   / |  |  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /  |  |  |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /   |  `--'  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     \______/  |__| \__| 
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            



"""

draw="""

 _______  .______          ___   ____    __    ____ 
|       \ |   _  \        /   \  \   \  /  \  /   / 
|  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  
|  |  |  ||      /      /  /_\  \  \            /   
|  '--'  ||  |\  \----./  _____  \  \    /\    /    
|_______/ | _| `._____/__/     \__\  \__/  \__/     
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    




"""
enemy_win="""


 _______ .__   __.  _______ .___  ___. ____    ____    ____    __    ____  ______   .__   __. 
|   ____||  \ |  | |   ____||   \/   | \   \  /   /    \   \  /  \  /   / /  __  \  |  \ |  | 
|  |__   |   \|  | |  |__   |  \  /  |  \   \/   /      \   \/    \/   / |  |  |  | |   \|  | 
|   __|  |  . `  | |   __|  |  |\/|  |   \_    _/        \            /  |  |  |  | |  . `  | 
|  |____ |  |\   | |  |____ |  |  |  |     |  |           \    /\    /   |  `--'  | |  |\   | 
|_______||__| \__| |_______||__|  |__|     |__|            \__/  \__/     \______/  |__| \__| 
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              




"""
comp_spells_easy=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy","Enneverate","Episkey","Liberacorpus","Rennervate",
        "Expelliarmus","Impedimenta","Langlock","Protego"]
comp_spells_hard=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy","Enneverate","Episkey","Liberacorpus","Rennervate",
        "Expelliarmus","Impedimenta","Langlock","Protego","Imperio","Crucio","Avada-Kedavara"]
attack_spells=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy"
        
        ]
healing_spells=["Enneverate","Episkey","Liberacorpus","Rennervate"]
defense_spells=["Expelliarmus","Impedimenta","Langlock","Protego"]
unforgivable_curses=["Imperio","Crucio","Avada-Kedavara"]
user_health=100
comp_health=100
comp_spell=""
should_continue=True
def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()


def exit_game():
    global should_continue
    should_continue=False
    

    
    
def game(name):
    global comp_health
    global user_health
    global difficulty
    damage=random.randint(1, 20)
    health=random.randint(1,20)
    if difficulty=="easy":
        comp_spell=random.choice(comp_spells_easy)
    else:
        comp_spell=random.choice(comp_spells_hard)
    
    user_spell=input("\n\nChoose a spell to fight your enemy: ").lower()
    if user_spell>="0" and user_spell<="9":
        print(f"\n\n{name} attacked with {attack_spells[int(user_spell)-1]}")
        speak("Damage Dealt to Enemy")
        comp_health-=damage
        #print(comp_health)
    elif user_spell>="a" and user_spell<="d":
        print(f"\n\n{name} healed themselves with {user_spell}")
        speak("Health Healed")
        user_health+=health
        #print(user_health)
    if user_spell>="e"and user_spell<="h" and comp_spell in attack_spells:
        print(f"\n\nEnemy attacked with {comp_spell} which {name} defended with {user_spell}")
        print(f"0 Damage done to you")
        speak("0 Damage Done to you")
    if comp_spell in attack_spells:
        print(f"\n\nEnemy attacked with {comp_spell}")
        speak("Damage dealt to You")
        user_health-=damage
        #print(user_health)
    elif comp_spell in healing_spells:
        print(f"\n\nEnemy healed themselves with {comp_spell}")
        speak("Damage healed by enemy")
        comp_health+=health
        #print(comp_health)
    if comp_spell in defense_spells and user_spell>="0" and user_spell<="9":
        print(f"\n\n{name} attacked with {attack_spells[int(user_spell)-1]} which the enemy defended with {comp_spell}")
        print(f"\n\n0 Damage done to enemy")
        speak("0 damage done to enemy")
    if comp_spell=="Imperio":
        user_health-=30
        print(f"\n\nEnemy attacked you with the {comp_spell} Unforgivable Curse.")
        speak("High Damage dealt to you")
    elif comp_spell=="Crucio":
        user_health-=50
        print(f"\n\nEnemy attacked you with the {comp_spell} Unforgivable Curse.")
        speak("High Damage dealt to you")
    elif comp_spell=="Avada-Kedavara":
        user_health-=80
        print(f"\n\nEnemy attacked you with the {comp_spell} Unforgivable Curse.")
        speak("High Damage dealt to you")

    #print(comp_spell)
    win(name)
def win(name):
    global comp_health
    global user_health
    if comp_health<=0 and user_health<=0:
        print(draw)
        speak("Battle Draw")
        comp_health=0
        user_health=0
        exit_game()
    elif comp_health<=0 and user_health!=0:
        print(user_win)
        speak("You Win!!")
        comp_health=0
        exit_game()
    elif comp_health!=0 and user_health<=0:
        print(enemy_win)
        speak("Enemy won!!!")
        user_health=0
        exit_game()
    
    
    

print(logo)
name=input("Enter Your Name: ")
choice=input("\n\nAre you a witch or a wizard? ").lower()
difficulty=input("Please choose a difficulty. Type 'easy' for easy difficulty and 'hard' for hard difficulty: ").lower()
if difficulty=="easy":
        print("You have chosen easy difficulty, Enemy won't be able to use Unforgivable Curses.")
else:
        print("You have chosen hard difficulty, Enemy will be able to use Unforgivable Curses.")

if choice=="wizard":
        print(wizard)
    
        speak("Welcome Wizard. Let's Fight....") 
    
elif choice=="witch":
        print(witch)
        print(man)
        speak("Welcome Witch. Let's Fight.....")
    
else:
        print("Wrong Choice!!!")    
print("Below are the instructions to play the game:")
print("\n\nEnter any key from 1 to 10 for Attack spells ")
print(attack_spells)
print("\n\nPress any key from A,B,C,D to heal yourself.")
print(healing_spells)
print("\n\nPress any key from E,F,G,H to protect/shield yourself. ")
print(defense_spells)
print("\n\nEach key contains a different spell. So don't be afraid to press different keys. ")
ch=input("\n\nReady to Play? Press 'y' to Play the game.")
screen_clear()
   

    
print(logo)
while should_continue:
    
    game(name)
    
print(f"Final Health of {name}: {user_health}")
print(f"Final Health of Enemy: {comp_health}")