#Roguelike Main file
#
#
#JOOOOOOON
#TOOOOO DOOOOOO
#0 MAKE GENERAL INTERACTION INTERFACE
#1 Done <<ADD OTHER ENTITIES
#2 DONE <<SANITIZE RENDERDICT, MAKE INTERACTIONS WITH OTHER ENTITIES
#3 ADD MORE OPTIONS FOR MOVEMENT
#4 ADD OTHER INTERACTION OPTIONS
#5 ADD WAYS TO GENERATE NEW MAP
#6 ADD LINE OF SIGHT CODE FOR WALKING AROUND DUNGEON MAPS OR HOSTILE AREAS
#7 ADD WAYS TO STORE, LOAD MAPS
#8 ADD WAYS TO STORE, SAVE, LOAD GAME
#9 ADD TEXT INTERACTIONS

#import colorama color terminal text features
from colorama import init
init(autoreset = True)
from colorama import Fore, Back, Style
basicMap = [[1,1,1,1,1,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1]]

extracMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,3,3,0,0,4,3,0,3,0,0,0,0,1],
            [1,0,0,0,0,0,3,4,3,0,0,0,0,3,0,1],
            [1,0,1,1,1,0,4,4,0,0,0,0,0,0,0,1],
            [1,0,1,2,1,3,4,3,0,1,1,1,0,0,0,1],
            [1,0,1,1,1,0,4,0,1,1,5,1,1,3,0,1],
            [1,0,0,0,4,4,4,0,1,5,5,5,1,0,0,1],
            [1,0,4,0,3,4,4,0,1,5,5,5,1,0,0,1],
            [1,0,0,0,3,4,4,0,1,1,0,1,1,0,0,1],
            [1,0,3,0,3,4,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,3,4,3,0,0,0,0,0,3,0,0,1],
            [1,0,3,3,0,4,4,0,0,0,0,3,3,3,0,1],
            [1,0,0,3,0,3,3,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#Texture map
#{Key : Text Color, Background Color, Style, Text [" " for clean color tile], Can Move To, Can see through, Description
basicTexture = {0: (Fore.GREEN, Back.GREEN, Style.NORMAL, " ", True, True, "acidic ground riddled with softly callous shiefs of green"), #Grass
                1: (Fore.YELLOW, Back.YELLOW, Style.NORMAL, " ", False, False, "strong but scarred sandstone walls"), #wall
                2: (Fore.BLACK, Back.BLACK, Style.NORMAL, " ", True, True, ""), #Void
                3: (Fore.GREEN, Back.GREEN, Style.BRIGHT, "T", True,"Lush trees, standing solemn gaurd against heaven"), #Tree
                4: (Fore.CYAN, Back.BLUE, Style.NORMAL, "~", True, True,"Luscious living waters, blood of the biosphere"), #water
                5: (Fore.YELLOW, Back.RED, Style.BRIGHT, "-",True, True, "Church floor")
                }
class Tile:
    def __init__(self,textColor=Fore.WHITE, backColor = Back.BLACK, styleType=Style.NORMAL, text=".", canWalk = "True", canSee = "False", descript = "Test"):
        """Initializes all of the normal Tile object """
        self.textColor = textColor #Color of rendered text
        self.backColor = backColor #Color of background tile
        self.styleType = styleType #type of text style (dim, normal, bright) Note on Windows only Bright and Normal display
        self.text= text #rendered text
        self.canMove = canWalk #can walk through/into this space
        self.canSee = canSee #can see through this space, is used for Line of Sight Code whenever I finish that bullfuckery
        self.descript = descript #description of text on Look command, e.g. "grassy ground, walls of sandstone"
        return
    def getBackground(self):
        """Returns the background color for item rendering"""
        return self.backColor
    def renderTile(self):
        """most basic rendering tile type"""
        print(self.textColor + self.backColor + self.styleType + self.text, end ="")
        return
    def legalMove(self):
        """Returns whether tile can be moved into(True) or not (False)"""
        return self.canMove
    def seeThrough(self):
        """Returns whether tile is transparent/can be seen through (True) or not (False)"""
        return self.canSee
    def convertTile(self, textColor, backColor, styleType, text, canWalk, canSee, descript):
        """converTitle(...) all the normal text documents, used if you wish to shift it to another tile type or create a unique tile type (e.g, graffiti walls"""
        self.textColor = textColor #Color of rendered text
        self.backColor = backColor #Color of background tile
        slef.styleType = styleType #type of text style (dim, normal, bright) Note on Windows only Bright and Normal display
        self.text= text #rendered text
        self.canWalk = canWalk #can walk through/into this space
        self.canSee = canSee #can see through this space, is used for Line of Sight Code whenever I finish that bullfuckery
        self.descript = descript #description of text on Look command, e.g. "grassy ground, ruined walls of sandstone"
        return
    def describe(self):
        """describe() returns description so that userInput and Look can use it as needed"""
        return descript
    def paintTile(self,textColor, backColor, styleType, text):
        """paintTile(..) Converts all of the aesthetics of a tile while leaving gameplay mechanics (description, passability, transparency) unchanged"""
        self.textColor = textColor
        self.backColor = backColor
        self.styleType = styleType
        self.text = text
        return

    
class Area:
    def __init__(self,dataMap = basicMap, textureMap = basicTexture):
        """initalies and creates a map out of a map of data points that are keys in a texture map, defaults to the town test function"""
        self.areaMap = dataMap
        self.textureMap = textureMap
        self.height = len(dataMap)
        self.width = len(dataMap[0])
        for y in range(len(dataMap)):
            for x in range(len(dataMap[0])):
                key = dataMap[y][x]
                self.areaMap[y][x] = Tile(textureMap[key][0], textureMap[key][1],
                                    textureMap[key][2], textureMap[key][3], textureMap[key][4],
                                    textureMap[key][5])
        return

    def render(self,mobList = {}):
        for y in range(self.height):
            for x in range(self.width):
                if (y,x) in mobList:
                    mobList[(y,x)].renderSelf(self.areaMap[y][x].getBackground())
                else:
    
                    self.areaMap[y][x].renderTile()
            print()
        return
    def legalMove(self,y,x):
        if (y >=0 and y < self.height) and (x >= 0 and x < self.width):
            return self.areaMap[y][x].legalMove()
        else:
            return False

###ACTOR CLASS
###New thought process - simulation has each actor working by relative speed, player first then everyone else

class Actor:
    def __init__(self, name, y, x, text, color, style):
        self.name = name
        self.y = y
        self.x = x
        self.text = text
        self.color = color
        self.style = style
        return
    def renderSelf(self, background = Back.BLACK):
        back = background
        print(self.color + back + self.style + self.text, end = "")
    def move(self,ny,nx):
        ##called inside the the act system
        self.y = ny
        self.x = nx
        return
    def attack(self):
        return
    def getPos(self):
        return (self.y, self.x)
    def switch(self, otherActor):
        """"switch(otherActor to be switch places)"""
        new = otherActor.getPos()
        old = self.getPos()
        self.move(new[0],new[1])
        otherActor.move(old[0],old[1])
        return otherActor
    def act(self, area, actorList):
        ###act() is where the ai lurks
        #walking code man what the fuck yall?
        ny = self.y
        nx = self.x+1
        if area.legalMove(ny, nx):
            for actor in actorList:
                if (actor.getPos == (ny,nx) and self != actor):
                    print(actor.getPos())
                    print(self.getPos())
                    actor = self.switch(actor)
                    print(self.getPos())
                    print(actor.getPos())
                    return actorList
            self.move(self.y,self.x+1)
            return actorList
        
###Class speciiically for player
###Of primary note is this uses playerInput for it's act()
class Player(Actor):
    def __init__(self, name = "Player", y=1, x=1, text="@", color = Fore.WHITE, style=Style.BRIGHT, ID = 0):
        self.name = name
        self.y = y
        self.x = x
        self.text = text
        self.color = color
        self.style = style
        self.idnum = ID
        return
    def getID(self):
        return self.idnum
    def act(self, area = None, actorList = None):
        while True:
            move = userPrompt()
            if move[0] == "m":
                ny = self.y+move[1][0]
                nx = self.x+move[1][1]
                if area.legalMove(ny,nx):
                    for actor in actorList:
                        if ((ny, nx) == actor.getPos() and self != actor):
                            #SWAPS CHARACTERS
                            print(actor.getPos())
                            print(self.getPos())
                            actor = self.switch(actor)
                            print(Fore.CYAN + Style.DIM + "You switch places with " + actor.name)
                            print(actor.getPos())
                            print(self.getPos())
                            return actorList
                    self.move(ny,nx)
                    return actorList
                else:
                    print(Fore.RED + Style.DIM + "Ow! You can't walk there")
            elif move[0] == "l":
                print(Fore.GREEN + "You stand in the oasis village of Radjemukh")#placer holder
            elif move[0] == "a":
                print(Fore.YELLOW + "I'm sorry I haven't implimented this yet")#Placer holder
            elif move[0] == "h":
                parseHelp()
            elif move[0] == "w":
                return actorList
            else:
                print(Fore.RED + Style.DIM + "I do not recognize that command. please enter a valid action")
        return


def parseHelp():
    commandList = """Commands:
    <A>ttack: Attacks nearby opponents. If multiple nearby, will prompt for target.
    <L>ook: Describes your location and nearby features you can
    <?>Help: opens this help menu.
    Movement:
    <N>orth, <S>outh, <W>est, <E>ast, <NW> North West, <NE> North East, <SW> South West, <SE> South East
    Moving in the direction of an item will cause normal interaction, i.e. a trade of blows or talking."""
    print("Enter a topic, <Q>uit, or Commands")
    while True:
        parse = input("Help>> ").lower()
        if parse in ("command", "commands", "c"):
            print(Fore.CYAN + Style.DIM + commandList)
        elif parse in ("exit","q"):
            return
        else:
            print("I don't fucking know")
    return

#Creates actorList for rendering
def makeActorRenderDict(actorList = []):
    renderDict = {}
    for actor in actorList:
        renderDict[(actor.y,actor.x)] = actor
    return renderDict

#runSimulation will bite me in the ass
#YES I CAN FUCKING MODIFY THE LIST MY FOR-LOOP IS BASED ON
#HAHAHAAHAHA
####REWRITE ACT() SO THAT IT RETURNS ACTOR LIST
def runSimulation(actorList = []):
    renderDict = makeActionRenderDict(actorList)
    for actor in actorList:
        actor.act()

#Rendering UI
#renders the little info textbox after the action map
def renderUI():
    return

#User prompt
#Should make action queue?
#Format:
#main_loop
##if queue empty then prompt user for input
##parse input
##run actions for all entities
##remove item from queue
##Else: don't ask for input, but simply pass next item from queue to player.act()
#QUESTION: How do deal with potential other problems? e.g. walk north into wall
##Ambient interupt value? e.g. if Interupt == True, then empty queue and ask for new input in cases where avatar knowledge changes, attacked, illegal actions
##Is it worth while to skip lots of boring movement
##OTOH, if you add a wait til healed option this would be necessary
#Perhaps create an strategy class? e.g. action - arguement(s) - duration; e.g. walk north 5 times => [m, (-1,0), 5] and let the act() function work with input
def userPrompt():
    """Takes input, breaks it down and parses it, and then returns what actions the user would like to do"""
    prompt = input(">>")
    prompt = prompt.lower()
    #
    #       N
    #       ^
    #E   <  X >   W
    #      \/ 
    #       S
    #
    if prompt in ("n", "north"):
        return ("m", (-1,0)) #(y,x)
    elif prompt in ("s", "south"):
        return ("m", (1,0))
    elif prompt in ("e", "east"):
        return ("m", (0,1))
    elif prompt in ("w", "west"):
        return ("m", (0,-1))
    elif prompt in ("nw", "north west", "northwest"):
        return ("m", (-1,-1))
    elif prompt in ("ne", "north east", "northeast"):
        return ("m", (-1,1))
    elif prompt in ("sw", "south west", "southwest"):
        return ("m", (1,-1))
    elif prompt in ("se", "south east", "southeast"):
        return ("m", (1,1))
    elif prompt in ("?", "help"):
        return ("h")
    elif prompt in ("a", "attack"):
        return ("a")
    elif prompt in ("l", "look"):
        return ("l")
    elif prompt in ("p", "wait"):
        return ("w")
    else:
        return ("x")
    return

class World:
    def __init__(self,area = None, actorList = []):
        self.currentArea = area
        self.areaMatrix = [area]
        self.actorList = actorList
        self.level = 0 #Town
        return
    def update(self):
        for actor in self.actorList:
            self.actorList = actor.act(self.currentArea,self.actorList)
        return
    def goLevel():
        return
    def renderArea(self):
        self.currentArea.render(makeActorRenderDict(self.actorList))
        return
            

#Main cycle
def main():
    #DO SETUP HERE
    #e.g. read in files, texture, mobs
    #roughshod system for player movement
    game = True
    #currentArea = Area()
    #actorList = [Player(), Actor(name = "Mister Test Man", y=2, x=2, text = "@", color = Fore.RED, style = Style.BRIGHT, idnum =1)]
    #walker = Actor(name = "Walker", y=2,x=2,text = "@",color = Fore.CYAN, style = Style.BRIGHT, idnum = 1)
    world = World(Area(),[Player(y=2,x=3),Actor(name = "Mister Test Man", y=2, x=2, text = "@", color = Fore.RED, style = Style.BRIGHT)])
    while game:
        world.renderArea()
        world.update()
    return

main()
