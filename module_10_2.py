import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies_counter = 100
        self.days_counter = 0

    def timer(self):
        while self.enemies_counter > 0:
            time.sleep(1)
            self.enemies_counter -= self.power
            self.days_counter += 1
            print(f"{self.name} сражается {self.days_counter} день(дня)..., осталось {self.enemies_counter} воинов.\n")

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer()
        print(f'{self.name} одержал победу спустя {self.days_counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')