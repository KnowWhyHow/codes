import pygame,math
pygame.init()

class Mass:
    def __init__(self,name,x,y,r,color,m,vx,vy):
        self.name = name
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.m = m
        self.vx =vx
        self.vy = vy
        self.pos = (self.x,self.y)
    def update(self):
        self.pos = (self.x,self.y)
    def display(self):
        pygame.draw.circle(win, self.color, self.pos, self.r)
        print(self.name,round(self.x),round(self.y),round(self.vx),round(self.vy))


class Universe:
    def __init__(self,G=1, T=1):
        self.G = G
        self.T = T
        self.objs = []
        self.n = 0
    def add(self, obj:Mass):
        self.objs.append(obj)
        self.n = len(self.objs)
    def action(self):
        for i in range(0,self.n-1):
            for j in range(i+1,self.n):
                move(self.objs[i],self.objs[j],self.G,self.T)
        for i in range(self.n):
            self.objs[i].display()

def dist(a:Mass,b:Mass):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def gravity(a:Mass,b:Mass,G):
    return G*(a.m*b.m)/(dist(a,b)**2)

def move(a:Mass,b:Mass,G,T):
    dist_x = a.x - b.x
    dist_y = a.y - b.y
    A = gravity(a,b,G)/b.m
    b.vx += dist_x / dist(a,b) * A * T
    b.vy += dist_y / dist(a,b) * A * T
    b.x +=b.vx
    b.y +=b.vy

    A = -gravity(a,b,G)/a.m
    a.vx += dist_x/dist(a,b) * A * T
    a.vy += dist_y/dist(a,b) * A * T
    a.x +=a.vx
    a.y +=a.vy
    b.update()
    a.update()

win_width = 1200
win_height = 800
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Bern Universe")

universe = Universe(G=1,T=1)

SUN = Mass('SUN',win_width/2,win_height/2,40,(255,0,0),100000,0,0)
universe.add(SUN)
p01 = Mass('p01',150,150,20,(0,0,255),10,5,-5)
universe.add(p01)
p02 = Mass('p02',200,200,15,(255,255,0),5,5,-5)
universe.add(p02)



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    universe.action()
    pygame.display.update()

pygame.quit()
