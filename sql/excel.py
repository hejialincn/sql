from turtle import *
from random import *

def get(number):
    data=[]
    for i in range(number):
        data.append((i+1)*(80/cos)-40/cos)      
    return(data)   
name=[]
tiao=[]
color1=["green","blue","red","brown","orange","purple","pink","cyan","black","magenta","gold","tomato"]
namet=input("请输入表标题:")
number=eval(input("请输入柱形条数量："))
for i in range(number):
    name1=randint(0,100)
    #name1=input("请输入柱形条{}姓名：".format(i))
    one=randint(10,200)
    #one=eval(input("请输入柱形条{}高度：".format(i)))
    tiao.append(one)
    name.append(name1)
cos=1
long=number*80+20
height=(round(max(tiao))+1)+20
if (long-20)/80/50>=1 or  (height-20)/500>=1 :
    cos=cos*8
    long=number*80/cos+20
    height=(round(max(tiao))+1)/cos+20
    font1=5
elif (long-20)/80/40>=1 or  (height-20)/400>=1 :
    cos=cos*6
    long=number*80/cos+20
    height=(round(max(tiao))+1)/cos+20
    font1=8
elif (long-20)/80/30>=1 or  (height-20)/300>=1 :
    cos=cos*4
    long=number*80/cos+20
    height=(round(max(tiao))+1)/cos+20
    font1=10
elif (long-20)/80/24>=1 or  (height-20)/240>=1 :
    cos=cos*2
    long=number*80/cos+20
    height=(round(max(tiao))+1)/cos+20
    font1=12
else:
    font1=13
data=get(number)
x=-(long//2)
penup()
hideturtle()
speed(0)
goto(x+(long//2-10),height+20)
pendown()
write(namet,align="center",font=("宋体",20,"normal"))
penup()
goto(x,0)
pendown()
rt(-90)
fd(height)
rt(180)
fd(height)
left(90)
fd(long)
rt(180)
fd(long)
rt(180)
for i in range(number):
    penup()
    goto((data[i]+x+15),-20)
    pendown()
    write(name[i],align="center",font=("宋体",font1,"normal"))
    penup()
    goto((data[i]+x),0)
    pendown()
    fillcolor(color1[randint(0,len(color1)-1)])
    begin_fill()
    rt(-90)
    fd(tiao[i]/cos)
    rt(90)
    fd(15/cos)
    write(tiao[i],align="center",font=("宋体",font1,"normal"))
    fd(25/cos)
    rt(90)
    fd(tiao[i]/cos)
    rt(-90)
    end_fill()
    
