#Roguelike Main file
#
#
#JOOOOOOON
#TOOOOO DOOOOOO
#1 ADD OTHER ENTITIES
#2 SANITIZE RENDERDICT, MAKE INTERACTIONS WITH OTHER ENTITIES
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

#getMap
#Gets map from IO file or if left blank, the default object include here
#all points are chr() objects that will be refferenced in the texture object for rendering
basicMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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
    def renderArea(self,mobList = {}):
        for y in range(self.height):
            for x in range(self.width):
                if (y,x) in mobList:
                    mobList[(y,x)].renderSelf(self.areaMap[y][x].getBackground())
                else:
    
                    self.areaMap[y][x].renderTile()
            print()
        return

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
    def act(self, area=None, actorList=None):
        ###act() is where the ai lurks
        ###should look into bringing in some sort of scripting or generic system
        return


class Player(Actor):
    def __init__(self, name = "Player", y=1, x=1, text="@", color = Fore.WHITE, style=Style.BRIGHT):
        self.name = name
        self.y = y
        self.x = x
        self.text = text
        self.color = color
        self.style = style
        return
    def act(self, area = None, actorList = None):
        while True:
            move = input("Write where you want to go: <N>orth, <W>est, <E>ast, or <S>outh: ")
            if move.lower() in ("n", "north") and area.areaMap[self.y-1][self.x].legalMove():
                self.y += -1
                return
            elif move.lower() in ("s", "south") and area.areaMap[self.y+1][self.x].legalMove():
                self.y += 1
                return
            elif move.lower() in ("w", "west") and area.areaMap[self.y][self.x-1].legalMove():
                self.x += -1
                return
            elif move.lower() in ("e", "east") and area.areaMap[self.y][self.x+1].legalMove():
                self.x += 1
                return
            else:
                print(Fore.RED + Style.DIM + "I'm sorry, that was an invalid command or position")
        return

#Creates actorList for rendering
def makeActorRenderDict(actorList = []):
    renderDict = {}
    for actor in actorList:
        renderDict[(actor.y,actor.x)] = actor
    return renderDict


#Rendering UI
#renders the little info textbox after the action map
def renderUI():
    return



def userPrompt(text = ""):
    return


#World Update
#Takes playerAction, mobs and runs through the ai/effects of each action 

#Main cycle
def main():
    #DO SETUP HERE
    #e.g. read in files, texture, mobs
    #roughshod system for player movement
    game = True
    currentArea = Area()
    actorList = [Player()]
    while game:
        renderDict = makeActorRenderDict(actorList)
        currentArea.renderArea(renderDict)
        for dude in actorList:
            dude.act(currentArea,actorList)
    return

main()
