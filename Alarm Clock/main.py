# Python Alarm Clock

from pygame import mixer
import time
from datetime import datetime, timedelta
import os


def ring_Alarm(sound_file):
        mixer.init()
        mixer.music.load(sound_file)
        mixer.music.set_volume(0.7) 
        mixer.music.play()
        
        print("Press 'p' to snooze") 
        print("Press 'e' to exit the program") 
        query = input(" ") 
        
        if query == 'p':
            print("Alarm snoozed for 5 seconds.") 
            
            # Pausing the music 
            mixer.music.pause()
            
            # call the snooze function
            snooze()
                    
        elif query == 'e': 

            # Stop the mixer 
            mixer.music.stop() 
            


def snooze():
    snoozed_time = (datetime.now()  + timedelta(minutes=5)).time().replace(microsecond=0).isoformat()
    is_running = True
    while is_running:
        now = datetime.now().strftime("%H:%M:%S")
        if now == snoozed_time:
            ring_Alarm()
            is_running = False
            
        
def set_alarm_tone():
    try:
        sound_file = input("Enter the relative path of alarm tone you want to set: ")
        return sound_file
    except Exception:
        print("Something error occured. Please, Recheck with your file path too.")
        
    

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    print(alarm_time)
    
    sound_file = set_alarm_tone()
    
    is_running = True
    
    while is_running:
        os.system("cls")
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        time.sleep(1)
        
        if alarm_time == current_time:
            print("Wake Up!")
            
            ring_Alarm(sound_file)
            
            
            
           

            
            
            
    

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS) ")
    set_alarm(alarm_time)
