#Write by Vladimir Voinovskiy, e-mail - faraon842@gmail.com
import random, math, os
from PIL import Image, ImageDraw

TOP_OCEAN = 1
TOP_VULCAN = 2
TOP_TOXIC = 3
TOP_LIFELESS = 4
TOP_ICE = 5
TOP_GAS = 6
TOP_EARTH = 7
TOP_DESERT = 8
TOP_JUNGLE = 9

PI = 3.14159265

WIDTH = 1920
HEIGHT = 1080

ItN = 0

BasePlanetSize = 150

class CSatellite:
    def __init__(self, stype = None):
        self.type = stype
        self.res = 0

    def AddRes(self, e, ch, con, sim, strat, rare):
        random.seed(os.urandom(13))
        x = random.randint(1, 12)
        if x <= e:
            self.res = 1
        elif x <= e+ch:
            self.res = 2
        elif x <= e+ch+con:
            self.res = 3
        elif x <= e+ch+con+sim:
            self.res = 4
        elif x <= e+ch+con+sim+strat:
            self.res = 5
        elif x <= e+ch+con+sim+strat+rare:
            self.res = 6

class CPlanet:
    def __init__(self, ptype = None, psize = None):
        self.type = ptype
        self.size = psize
        self.satellite = []
        self.res = []

    def DetSize(self, chance1, chance2, chance3):
        random.seed(os.urandom(11))
        summ = chance1 + chance2 + chance3
        y = random.randint(1, summ)
        if y<=chance1:
            self.size = 0
        elif y <= chance1+chance2:
            self.size = 1
        elif y <= summ:
            self.size = 2

    def AddSatellite(self, chance):
        random.seed(os.urandom(17))
        z = random.randint(1, 10)
        if z <= chance:
            x = random.randint(1, 8)
            if x <= 4:
                self.satellite.append(CSatellite(TOP_LIFELESS))
                self.satellite[len(self.satellite)-1].AddRes(100, 100, 100, 300, 300, 300)
            elif x == 5:
                self.satellite.append(CSatellite(TOP_ICE))
                self.satellite[len(self.satellite)-1].AddRes(0, 300, 200, 300, 200, 200)
            elif x == 6:
                self.satellite.append(CSatellite(TOP_TOXIC))
                self.satellite[len(self.satellite)-1].AddRes(200, 300, 0, 200, 200, 300)
            elif x == 7:
                self.satellite.append(CSatellite(TOP_VULCAN))
                self.satellite[len(self.satellite)-1].AddRes(300, 200, 0, 300, 200, 200)
            elif x == 8:
                self.satellite.append(CSatellite(TOP_OCEAN))
                self.satellite[len(self.satellite)-1].AddRes(300, 300, 200, 200, 100, 100)

    def AddRes(self, e, ch, con, sim, strat, rare):
        random.seed(os.urandom(19))
        x = random.randint(1, 1200)
        if x <= e:
            self.res.append(1)
        elif x <= e+ch:
            self.res.append(2)
        elif x <= e+ch+con:
            self.res.append(3)
        elif x <= e+ch+con+sim:
            self.res.append(4)
        elif x <= e+ch+con+sim+strat:
            self.res.append(5)
        elif x <= e+ch+con+sim+strat+rare:
            self.res.append(6)

class CStar:
    def __init__(self, specclass = None, radius = None, color = None):
        self.specclass = specclass
        self.radius = radius
        self.color = color

ItN = int(input("Введите кол-во нужных систем: "))
for NumSystem in range(1, ItN+1):
#==========================================================================================
#Звезда
#==========================================================================================
    random.seed(os.urandom(9))
    Star = CStar(0, 0, 0)
    Star.specclass = random.randint(1, 16)
    if Star.specclass == 1 or Star.specclass == 2:
        Star.radius = WIDTH/2*0.85
        Star.color = (66, 170, 255, 0)
        fon_color = (3, 12, 19)
        star = Image.open(os.path.abspath('texture\\star\\Class_O_'+str(random.randint(1, 2))+'.png'))
    elif Star.specclass == 3 or Star.specclass == 4 or Star.specclass == 5:
        Star.radius = WIDTH/3*0.85
        Star.color = (176, 224, 230, 0)
        fon_color = (8, 18, 19)
        star = Image.open(os.path.abspath('texture\\star\\Class_B_'+str(random.randint(1, 2))+'.png'))
    elif Star.specclass == 6 or Star.specclass == 7 or Star.specclass == 8 or Star.specclass == 9:
        Star.radius = WIDTH/4*0.85
        Star.color = (255, 255, 255, 0)
        fon_color = (18, 18, 18)
        star = Image.open(os.path.abspath('texture\\star\\Class_A_'+str(random.randint(1, 3))+'.png'))
    elif Star.specclass == 10 or Star.specclass == 11 or Star.specclass == 12:
        Star.radius = WIDTH/5*0.85
        Star.color = (255, 226, 183, 0)
        fon_color = (21, 22, 17)
        star = Image.open(os.path.abspath('texture\\star\\Class_F_'+str(random.randint(1, 3))+'.png'))
    elif Star.specclass == 13 or Star.specclass == 14:
        Star.radius = WIDTH/6*0.85
        Star.color = (252, 232, 131, 0)
        fon_color = (11, 11, 0)
        star = Image.open(os.path.abspath('texture\\star\\Class_G_'+str(random.randint(1, 3))+'.png'))
    elif Star.specclass == 15:
        Star.radius = WIDTH/7*0.85
        Star.color = (237, 118, 14, 0)
        fon_color = (21, 11, 1)
        star = Image.open(os.path.abspath('texture\\star\\Class_K_'+str(random.randint(1, 3))+'.png'))
    elif Star.specclass == 16:
        Star.radius = WIDTH/8*0.85
        Star.color = (255, 0, 51, 0)
        fon_color = (21, 1, 0)
        star = Image.open(os.path.abspath('texture\\star\\Class_M_'+str(random.randint(1, 2))+'.png'))
    x1, x2, x3, x4 = star.getpixel((star.size[0] - 5, star.size[1] - 5))
    fon_color = (x1, x2, x3)
    StarSystem = []
#==========================================================================================
#1 планета
#==========================================================================================
    random.seed(os.urandom(10))
    x = random.randint(1, 11)
    if x == 1:
        StarSystem.append(CPlanet(TOP_OCEAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 200, 200, 100, 100)
    elif x == 2 or x == 3 or x == 4:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 5 or x == 6 or x == 7:
        StarSystem.append(CPlanet(TOP_TOXIC, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 0, 200, 200, 300)
    elif x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 100, 300, 300, 300)
    elif x == 10:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 000, 000, 300)
    elif x == 11:
        StarSystem.append(CPlanet(TOP_DESERT, 0))
        StarSystem[len(StarSystem)-1].DetSize(4, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 300, 200, 100, 100)

#==========================================================================================
#2 планета
#==========================================================================================
    random.seed((os.urandom(20)))
    x = random.randint(1, 10)
    if x == 1:
        StarSystem.append(CPlanet(TOP_OCEAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 200, 200, 100, 100)
    elif x == 2:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 3:
        StarSystem.append(CPlanet(TOP_TOXIC, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 0, 200, 200, 300)
    elif x == 4 or x == 5:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 100, 300, 300, 300)
    elif x == 6:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 0, 0, 300)
    elif x == 7:
        StarSystem.append(CPlanet(TOP_EARTH, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 100, 400, 300, 100, 100)
    elif x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_DESERT, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 300, 200, 100, 100)
    elif x == 10:
        StarSystem.append(CPlanet(TOP_JUNGLE, 0))
        StarSystem[len(StarSystem)-1].DetSize(2, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 400, 200, 100, 0)

    StarSystem[len(StarSystem)-1].AddSatellite(1)
    StarSystem[len(StarSystem)-1].AddSatellite(1)
#==========================================================================================
#3 планета
#==========================================================================================
    random.seed((os.urandom(30)))
    x = random.randint(1, 13)
    if x == 1 or x == 2:
        StarSystem.append(CPlanet(TOP_OCEAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 200, 200, 100, 100)
    elif x == 3:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 4:
        StarSystem.append(CPlanet(TOP_TOXIC, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 0, 200, 200, 300)
    elif x == 5 or x == 6:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 10, 300, 300, 300)
    elif x == 7:
        StarSystem.append(CPlanet(TOP_ICE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(0, 300, 200, 300, 200, 200)
    elif x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_EARTH, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 100, 400, 300, 100, 100)
    elif x == 10 or x == 11:
        StarSystem.append(CPlanet(TOP_DESERT, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 300, 200, 100, 100)
    elif x == 12 or x == 13:
        StarSystem.append(CPlanet(TOP_JUNGLE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 400, 200, 100, 0)

    StarSystem[len(StarSystem)-1].AddSatellite(3)
    StarSystem[len(StarSystem)-1].AddSatellite(2)
    StarSystem[len(StarSystem)-1].AddSatellite(1)
#==========================================================================================
#4 планета
#==========================================================================================
    random.seed((os.urandom(40)))
    x = random.randint(1, 14)
    if x == 1:
        StarSystem.append(CPlanet(TOP_OCEAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 200, 200, 100, 100)
    elif x == 2 or x == 3:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 4:
        StarSystem.append(CPlanet(TOP_TOXIC, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 0, 200, 200, 300)
    elif x == 5 or x == 6 or x == 7:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 10, 300, 300, 300)
    elif x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_ICE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(0, 300, 200, 300, 200, 200)
    elif x == 10:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 0, 0, 300)
    elif x == 11:
        StarSystem.append(CPlanet(TOP_EARTH, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 100, 400, 300, 100, 100)
    elif x == 12:
        StarSystem.append(CPlanet(TOP_DESERT, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 300, 200, 100, 100)
    elif x == 13:
        StarSystem.append(CPlanet(TOP_JUNGLE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 1, 1)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 400, 200, 100, 0)

    StarSystem[len(StarSystem)-1].AddSatellite(3)
    StarSystem[len(StarSystem)-1].AddSatellite(3)
    StarSystem[len(StarSystem)-1].AddSatellite(1)
#==========================================================================================
#5 планета
#==========================================================================================
    random.seed((os.urandom(50)))
    x = random.randint(1, 11)
    if x == 1:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 2:
        StarSystem.append(CPlanet(TOP_TOXIC, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 300, 0, 200, 200, 300)
    elif x == 3 or x == 4:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 10, 300, 300, 300)
    elif x == 5 or x == 6:
        StarSystem.append(CPlanet(TOP_ICE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(0, 300, 200, 300, 200, 200)
    elif x == 7 or x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 0, 0, 300)
    elif x == 10:
        StarSystem.append(CPlanet(TOP_EARTH, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 2, 3)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(200, 100, 400, 300, 100, 100)

    StarSystem[len(StarSystem)-1].AddSatellite(4)
    StarSystem[len(StarSystem)-1].AddSatellite(2)
    StarSystem[len(StarSystem)-1].AddSatellite(2)
    StarSystem[len(StarSystem)-1].AddSatellite(1)
#==========================================================================================
#6 планета
#==========================================================================================
    random.seed((os.urandom(60)))
    x = random.randint(1, 11)
    if x == 1:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 3, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 2 or x == 3:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 3, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 10, 300, 300, 300)
    elif x == 4 or x == 5 or x == 6:
        StarSystem.append(CPlanet(TOP_ICE, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 3, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(0, 300, 200, 300, 200, 200)
    elif x == 7 or x == 8 or x == 9:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(1, 3, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 0, 0, 300)

    StarSystem[len(StarSystem)-1].AddSatellite(4)
    StarSystem[len(StarSystem)-1].AddSatellite(4)
    StarSystem[len(StarSystem)-1].AddSatellite(3)
    StarSystem[len(StarSystem)-1].AddSatellite(1)
#==========================================================================================
#7 планета
#==========================================================================================
    random.seed((os.urandom(70)))
    x = random.randint(1, 15)
    if x == 1:
        StarSystem.append(CPlanet(TOP_VULCAN, 0))
        StarSystem[len(StarSystem)-1].DetSize(3, 1, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 200, 0, 300, 200, 200)
    elif x == 2 or x == 3 or x == 4:
        StarSystem.append(CPlanet(TOP_LIFELESS, 0))
        StarSystem[len(StarSystem)-1].DetSize(3, 1, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(100, 100, 10, 300, 300, 300)
    elif x == 5 or x == 6 or x == 7 or x == 8:
        StarSystem.append(CPlanet(TOP_ICE, 0))
        StarSystem[len(StarSystem)-1].DetSize(3, 1, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(0, 300, 200, 300, 200, 200)
    elif x == 9 or x == 10 or x == 11 or x == 12:
        StarSystem.append(CPlanet(TOP_GAS, 0))
        StarSystem[len(StarSystem)-1].DetSize(3, 1, 4)
        for i in range(StarSystem[len(StarSystem)-1].size+1):
            StarSystem[len(StarSystem)-1].AddRes(300, 300, 300, 0, 0, 300)

    StarSystem[len(StarSystem)-1].AddSatellite(4)
    StarSystem[len(StarSystem)-1].AddSatellite(1)

    num = len(StarSystem) - 1
    for i in range(num):
        if StarSystem[i].type == TOP_GAS:
            StarSystem[i].size += 2
    
#==========================================================================================
#Расчёт орбит и растановка планет
#==========================================================================================
    PSys = Image.new("RGB", (WIDTH, HEIGHT), fon_color)
    draw = ImageDraw.Draw(PSys)
    Star.radius = Star.radius = WIDTH/2*0.85
    swidth, sheight = star.size
    star = star.crop((swidth/2, 0, swidth, sheight))
    star = star.resize((int(Star.radius), HEIGHT), Image.ANTIALIAS)
    PSys.paste(star, [0, 0, int(Star.radius), HEIGHT])
    Star.radius = Star.radius = WIDTH/3*0.85
    
    s = (WIDTH - Star.radius - 100)/(num + 1)
    for i in range(1, num + 1):
        draw.arc([0-(Star.radius+s*i), HEIGHT/2-(Star.radius+s*i), 0+(Star.radius+s*i), HEIGHT/2+(Star.radius+s*i)], -90, 90, fill = (255, 255, 255, 0))
        
        if StarSystem[i-1].type == TOP_OCEAN:
            planet = Image.open(os.path.abspath('texture\ocean\MapOcean'+str(random.randint(1, 30))+'.png'))
            color_planet = (66, 170, 255)
        elif StarSystem[i-1].type == TOP_VULCAN:
            planet = Image.open(os.path.abspath('texture\wulcan\MapVulcan'+str(random.randint(1, 30))+'.png'))
            color_planet = (255, 0, 0)
        elif StarSystem[i-1].type == TOP_TOXIC:
            planet = Image.open(os.path.abspath('texture\\toxic\\MapToxic'+str(random.randint(1, 30))+'.png'))
            color_planet = (255, 255, 0)
        elif StarSystem[i-1].type == TOP_LIFELESS:
            planet = Image.open(os.path.abspath('texture\\lifeless\\MapLifeless'+str(random.randint(1, 30))+'.png'))
            color_planet = (192, 192, 192)
        elif StarSystem[i-1].type == TOP_ICE:
            planet = Image.open(os.path.abspath('texture\\ice\\MapIce'+str(random.randint(1, 30))+'.png'))
            color_planet = (255, 255, 255)
        elif StarSystem[i-1].type == TOP_GAS:
            planet = Image.open(os.path.abspath('texture\\gas\\MapGas'+str(random.randint(1, 30))+'.png'))
            color_planet = (128, 0, 128)
        elif StarSystem[i-1].type == TOP_EARTH:
            planet = Image.open(os.path.abspath('texture\\earth\\MapEarth'+str(random.randint(1, 30))+'.png'))
            color_planet = (0, 0, 255)
        elif StarSystem[i-1].type == TOP_DESERT:
            planet = Image.open(os.path.abspath('texture\\desert\\MapDesert'+str(random.randint(1, 30))+'.png'))
            color_planet = (255, 165, 0)
        elif StarSystem[i-1].type == TOP_JUNGLE:
            planet = Image.open(os.path.abspath('texture\\jungle\\MapJungle'+str(random.randint(1, 30))+'.png'))
            color_planet = (0, 128, 0)
        planet = planet.resize((BasePlanetSize + StarSystem[i-1].size*50, BasePlanetSize + StarSystem[i-1].size*50), Image.ANTIALIAS)
        
        x0 = 0 + int((Star.radius + s*i) - (num-i)*s/30)
        y0 = int(HEIGHT/2)
        if i%2==0:
            y0 -= int(HEIGHT/5)
        else:
            y0 += int(HEIGHT/5)
        PSys.paste(planet, (int(x0 - (BasePlanetSize + StarSystem[i-1].size*50)/2), int(y0 - int((BasePlanetSize + StarSystem[i-1].size*50)/2))), planet)
        xR = x0 - 20/2 #вычитаем половину размера
        yR = y0 - (BasePlanetSize + StarSystem[i-1].size*50)/2 - 20/2 - 50
        NumRes = len(StarSystem[i-1].res)

        for j in range(NumRes):
            TypeRes = StarSystem[i-1].res[j]
            if TypeRes == 1:
                resource = Image.open(os.path.abspath('texture\\res\\Lightning.png'))
            elif TypeRes == 2:
                resource = Image.open(os.path.abspath('texture\\res\\Chemical.png'))
            elif TypeRes == 3:
                resource = Image.open(os.path.abspath('texture\\res\\FavConditions.png'))
            elif TypeRes == 4:
                resource = Image.open(os.path.abspath('texture\\res\\SimpleMet.png'))
            elif TypeRes == 5:
                resource = Image.open(os.path.abspath('texture\\res\\StrategicMet.png'))
            elif TypeRes == 6:
                resource = Image.open(os.path.abspath('texture\\res\\RareMet.png'))
            resource = resource.resize((30, 30), Image.ANTIALIAS)
            draw.arc([x0 - (BasePlanetSize + StarSystem[i-1].size*50)/2 - 30, y0 - (BasePlanetSize + StarSystem[i-1].size*50)/2 - 30,
                      x0 + (BasePlanetSize + StarSystem[i-1].size*50)/2 + 30, y0 + (BasePlanetSize + StarSystem[i-1].size*50)/2 + 30],
                     int(j*90/NumRes - 8) - 90 + 20, int(j*90/NumRes + 12) - 90 + 20, width = 10, fill = color_planet)
            x1 = (xR - x0)*math.cos(j*math.pi/2/NumRes + math.pi/9) - (yR - y0)*math.sin(j*math.pi/2/NumRes + math.pi/9) + x0
            y1 = (xR - x0)*math.sin(j*math.pi/2/NumRes + math.pi/9) + (yR - y0)*math.cos(j*math.pi/2/NumRes + math.pi/9) + y0
            PSys.paste(resource, (int(x1), int(y1)), resource)
        
        xS = x0 - 30/2
        yS = y0 - (BasePlanetSize + StarSystem[i-1].size*50)/2 - 30/2 - 70
        NumS = len(StarSystem[i-1].satellite)
        for k in range(NumS):
            S = StarSystem[i-1].satellite[k].type
            if S == TOP_LIFELESS:
                sputnik = Image.open(os.path.abspath('texture\\lifeless\\MapLifeless'+str(random.randint(1, 10))+'.png'))
            elif S == TOP_ICE:
                sputnik = Image.open(os.path.abspath('texture\\ice\\MapIce'+str(random.randint(1, 10))+'.png'))
            elif S == TOP_TOXIC:
                sputnik = Image.open(os.path.abspath('texture\\toxic\\MapToxic'+str(random.randint(1, 10))+'.png'))
            elif S == TOP_VULCAN:
                sputnik = Image.open(os.path.abspath('texture\\wulcan\\MapVulcan'+str(random.randint(1, 10))+'.png'))
            elif S == TOP_OCEAN:
                sputnik = Image.open(os.path.abspath('texture\\ocean\\MapOcean'+str(random.randint(1, 10))+'.png'))
            sputnik = sputnik.resize((60, 60), Image.ANTIALIAS)
            x2 = (xS - x0)*math.cos(-k*math.pi/2/NumS/1.2 - math.pi/9) - (yS - y0)*math.sin(-k*math.pi/2/NumS/1.2-math.pi/9) + x0
            y2 = (xS - x0)*math.sin(-k*math.pi/2/NumS/1.2 - math.pi/9) + (yS - y0)*math.cos(-k*math.pi/2/NumS/1.2-math.pi/9) + y0
            PSys.paste(sputnik, (int(x2), int(y2)), sputnik)
            
            yS -= (BasePlanetSize + StarSystem[i-1].size*50)/8 + 10
            x3 = (xS - x0)*math.cos(-k*math.pi/2/NumS/1.2 - math.pi/9) - (yS - y0)*math.sin(-k*math.pi/2/NumS/1.2-math.pi/9) + x0
            y3 = (xS - x0)*math.sin(-k*math.pi/2/NumS/1.2 - math.pi/9) + (yS - y0)*math.cos(-k*math.pi/2/NumS/1.2-math.pi/9) + y0
            yS += (BasePlanetSize + StarSystem[i-1].size*50)/8 + 10
            
            TypeRes = StarSystem[i-1].satellite[k].res
            if TypeRes == 1:
                resource = Image.open(os.path.abspath('texture\\res\\Lightning.png'))
            elif TypeRes == 2:
                resource = Image.open(os.path.abspath('texture\\res\\Chemical.png'))
            elif TypeRes == 3:
                resource = Image.open(os.path.abspath('texture\\res\\FavConditions.png'))
            elif TypeRes == 4:
                resource = Image.open(os.path.abspath('texture\\res\\SimpleMet.png'))
            elif TypeRes == 5:
                resource = Image.open(os.path.abspath('texture\\res\\StrategicMet.png'))
            elif TypeRes == 6:
                resource = Image.open(os.path.abspath('texture\\res\\RareMet.png'))
            resource = resource.resize((30, 30), Image.ANTIALIAS)
            PSys.paste(resource, (int(x3), int(y3)), resource)
    del draw

    PSys.save(os.path.abspath('result\\StarSystem'+str(NumSystem)+'.png'))
    if ItN == 1:
        PSys.show()
