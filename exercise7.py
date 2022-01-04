from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if(a==stopper):
            mixer.music.stop()
            break

def log(msg):
    with open("health.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_time=5
    eyes_time = 30
    ex_time = 45

    while True :
        if time()-init_water > water_time:
            print("Drinking time . Enter stop to stop ")
            musicloop("water.mp3","stop")
            init_water=time()
            log("Drank water at")
        elif time()-init_eyes > eyes_time:
            print("Eyes resting time . enter ey_stop to stop the alarm")
            musicloop("eyes.mp3","ey_stop")
            init_eyes=time()
            log("Relaxed eyes at")
        elif time()-init_exercise>ex_time:
            print("Exercise time . enter ex_stop to stop the alarm")
            musicloop("exercise.mp3","ex_stop")
            init_exercise=time()
            log("workout done at")


