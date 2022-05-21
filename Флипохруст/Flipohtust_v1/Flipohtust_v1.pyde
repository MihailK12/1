e=0
time=0
r=[]
for i in range(10):
    r.append(i*250)
k=[400, 200, 300, 240, 534, 240, 470, 329, 410, 170]
t=100
def setup():
    global fl, t, mieso, hleb
    size(600,600)
    frameRate(50)
    fl=loadImage('6.png') 
def draw():
    global e, time, r, fl, t
    
    if e == 0:                    # // "загрузка"
        fill(134,20,164)
        rect(200,200,200,200)
        textSize(55)
        fill(234,20,164)
        text('start',240,300)
                                  # // "сама игра"
    if e == 1:
        background(200)
        fill(14,20,244)
        rect(50,200,200,200)
        textSize(55)
        fill(0,0,0)
        text('Flip',110,320)
       
        fill(104,20,244)
        rect(350,200,200,200)
        textSize(45)
        fill(0,0,0)
        text('Flipik_X',360,320)
    if e == 4:
        background(50)
    if e == 3:
        background(50,255,0)
        ellipse(300,300,random(255),random(255))
    if e == 5:
        time=time+1
        background (100,156,254)
        
        if time>20:
            text("loading.",200,300)
        if time>160:
            text("loading..",200,300)
        if time>240:
            text("loading...",200,300)
        if time>250:
            background(200)
            fl=loadImage('6.png')
            image(fl,50,420,120,120)
            e=6
    if e == 6:
        background(200)
        for i in range(0,10):
            rect (r[i],k[i],50,600-k[i])
            r[i]=r[i]-2
            if r[i]<0 :
                r[i] = 2500
                k[i] = random(200, 500)
        image(fl,100,t,120,120)
        t=t+1
    text(e,20,90)
def mouseClicked():
    global e   
    if mouseX >200 and mouseX <400 and mouseY >200 and mouseY <400 and e==0: #start
        e = 1
    if e==1 and mouseX >50 and mouseX <250 and mouseY >200 and mouseY <400: #flip
        e = 3
    if e==1 and mouseX >400 and mouseX <500 and mouseY >200 and mouseY <400: #Flipik_X
        e = 4
    if e==3 and mouseX >250 and mouseX <350 and mouseY >250 and mouseY <350: #fill
        e = 5
    if e==6 and mouseX >250 and mouseX <350 and mouseY >250 and mouseY <350: #fill
        e = 6
        
def keyPressed():
    global t 
    if key == " " : 
        t=t-30
        
    if key == "z" : 
        t=t-100
