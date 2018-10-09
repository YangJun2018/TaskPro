#coding:utf-8
__author__ = 'Administrator'
import random,time

class Tiger():
    classname="Tiger"
    def __init__(self,weight=200):
        self.weight=weight

    def calling(self):
        print("Wow !!")
        self.weight-=5

    def feed(self,food):
        if food=="meat":
            self.weight+=10
            print('正确，体重 + 10')
        elif food=="grass":
            self.weight-=10
            print('太惨了，体重 - 10')


class SHEEP:
    classname="Sheep"
    def __init__(self,weight=100):
        self.weight=weight

    def calling(self):
        print("mie~~")
        self.weight-=5

    def feed(self,food):
        if food=="meat":
            self.weight+=10
            print('正确，体重 + 10')
        elif food=="grass":
            self.weight-=10
            print('太惨了，体重 - 10')

class ROOM:
    def __init__(self,num,animal):
        self.num=num
        self.animal=animal

rooms=[]
for id in  range(0,10):
    if random.randint(0,1):
        ani=Tiger(200)
    else:
        ani=SHEEP(100)
    room=ROOM(id,ani)
    rooms.append(room)

start_time=time.time()
while True:
    num=random.randint(1,10)
    now_time=time.time()
    if now_time-start_time>180:
        print("game is over")
        for idx,animal in enumerate(rooms):
            print('房间 :%s' % (idx + 1), room.animal.classname, room.animal.weight)
        break

    else:
        room=rooms[num-1]
        InData=input('我们来到了房间# %s, 要敲门吗?[y/n]' % num)
        if InData=='y':
            room.animal.calling()
        food=input("请给房间里面的动物喂食:")
        room.animal.feed(food.strip())


