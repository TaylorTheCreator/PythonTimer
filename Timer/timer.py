from threading import Thread
import time


def default_end(self):
    #temporary ending callback for the timer
    print("Timer " + self.name + " has completed!")

class Timer:
    def __init__(self, name,  callback=default_end, seconds=0):
        self.seconds = seconds
        self.name = name
        self.callback = callback
    
    def timer_complete(self):
        self.callback(self)

    def start(self):
        Thread(target=self.countdown).start()

    def countdown(self):
        while self.seconds > 0:
            time.sleep(1)
            self.seconds -= 1
            self.tick()
        self.timer_complete()

    def tick(self):
        #Perform logic on each tick, or dont... idc baka
        print(self.seconds)