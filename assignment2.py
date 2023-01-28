print("<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3. VEHICLE ROTATES RIGHT\n4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEW THE MATRIX\n0. EXIT")
print("Please enter the commands with a plus sign (+) between them.")
counter=None
while counter==None:
 seq=input()
 seqlist=seq.split("+")
 for i in seqlist:
    if i.startswith("5_")==True:
        seqlist[seqlist.index(i)]=int(i[2:])
 sidelength=int(seqlist[0])
 Matrix=[["+" for x in range(sidelength+2)]for y in range(sidelength+2)]
 for i in range(1,sidelength+1):
    for j in range(1,sidelength+1):
        Matrix[i][j] =" "
 location_x , location_y = 1,1
 brush=False
 direction="right"
 def turn(leftright):
    global direction
    if leftright=="left":
        if direction=="right":
            direction="up"
        elif direction=="down":
            direction="right"
        elif direction=="left":
            direction="down"
        elif direction=="up":
            direction="left"
    elif leftright=="right":
        if direction=="right":
            direction="down"
        elif direction=="down":
            direction="left"
        elif direction=="left":
            direction="up"
        elif direction=="up":
            direction="right"
 def paint():
    global brush,location_x,location_y
    if brush==True:
        Matrix[location_y][location_x] = "*"
 def brushdown():
    global brush
    brush=True
    paint()
 def brushup():
    global brush
    brush=False
 def move(i):
    global location_y,location_x,direction
    if direction=="right":
        templocation=location_x
        counterlocation=location_x+i
        if location_x + i > sidelength:
            for k in range(sidelength - location_x):
                location_x += 1
                paint()
            location_x = 1
            paint()
            if counterlocation > 2*sidelength:
                while counterlocation > 2*sidelength:
                    for j in range(sidelength - 1):
                        location_x += 1
                        paint()
                    location_x = 1
                    paint()
                    counterlocation -= sidelength
            else:
                for j in range(i - (sidelength-templocation) -1):
                    location_x += 1
                    paint()
        else:
            for k in range(i):
                location_x += 1
                paint()
    if direction=="down":
        templocation = location_y
        counterlocation = location_y + i
        if location_y + i > sidelength:
            for k in range(sidelength - location_y):
                location_y += 1
                paint()
            location_y = 1
            paint()
            if counterlocation > 2 * sidelength:
                while counterlocation > 2 * sidelength:
                    for j in range(sidelength - 1):
                        location_y += 1
                        paint()
                    location_y = 1
                    paint()
                    counterlocation -= sidelength
            else:
                for j in range(i - (sidelength - templocation) - 1):
                    location_y += 1
                    paint()
        else:
            for k in range(int(i)):
                location_y += 1
                paint()
    if direction=="left":
        templocation = location_x
        counterlocation = sidelength - location_x + i
        if sidelength - location_x + i > sidelength:
            for k in range(location_x-1):
                location_x -= 1
                paint()
            location_x = sidelength
            paint()
            if counterlocation > 2 * sidelength:
                while counterlocation > 2 * sidelength:
                    for j in range(sidelength - 1):
                        location_x -= 1
                        paint()
                    location_x = sidelength
                    paint()
                    counterlocation -= sidelength
            else:
                for j in range(i - (templocation)):
                    location_x -= 1
                    paint()
        else:
            for k in range(int(i)):
                location_x -= 1
                paint()
    if direction=="up":
        templocation = location_y
        counterlocation = sidelength - location_y + i
        if sidelength - location_y + i >= sidelength:
            for k in range(location_y-1):
                location_y -= 1
                paint()
            location_y = sidelength
            paint()
            if counterlocation > 2 * sidelength:
                while counterlocation > 2 * sidelength:
                    for j in range(sidelength - 1):
                        location_y -= 1
                        paint()
                    location_y = sidelength
                    paint()
                    counterlocation -= sidelength
            else:
                for j in range(i - (templocation)):
                    location_y -= 1
                    paint()
        else:
            for k in range(int(i)):
                location_y -= 1
                paint()
 def reverse():
     global direction
     if direction=="right":
         direction="left"
     elif direction=="down":
         direction="up"
     elif direction=="left":
         direction="right"
     elif direction=="up":
         direction="down"
 for i in seqlist[1:]:
    if i=="1":
        brushdown()
    elif i=="2":
        brushup()
    elif i=="3":
        turn("right")
    elif i=="4":
        turn("left")
    elif i=="6":
        brushup()
        move(3)
    elif i=="7":
        reverse()
    elif i=="8":
        for k in range(sidelength+2):
            for j in range(sidelength+2):
                if j!=sidelength+1:
                    print(Matrix[k][j],end="")
                else:
                    print(Matrix[k][j])
    elif type(i)==int:
        move(i)
    elif i=="0":
        counter = "stop"
        break
    else:
        print("You entered an incorrect command. Please try again!")
        break