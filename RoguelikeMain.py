#Roguelike Main file
#
#
#JOOOOOOON
#TOOOOO DOOOOOO
#<1> FINISH AREA MAP INIATION
#<2> FINISH UP AREA MAP SCREEN RENDERING
#<3> CREATE THE MOB CLASS
#<4> FIGURE OUT HOW THE HELL SIMULATION WILL WORK
#
#

#import colorama color terminal text features
from colorama import init
init()
from colorama import Fore, Back, Style

#getMap
#Gets map from IO file or if left blank, the default object include here
#all points are chr() objects that will be refferenced in the texture object for rendering
basicMap = [[1,1,1,1,1,1,1,1,1,1],
            [1,0,0,3,3,0,0,0,3,1],
            [1,0,0,0,0,0,3,0,3,1],
            [1,0,1,1,1,0,0,0,0,1],
            [1,0,1,2,1,3,0,3,0,1],
            [1,0,1,1,1,0,0,0,0,1],
            [1,0,0,0,4,4,4,4,0,1],
            [1,0,4,0,3,4,4,4,0,1],
            [1,0,0,0,3,4,4,4,4,1],
            [1,1,1,1,1,1,1,1,1,1,]]
#Texture map
#{Key : Text Color, Background Color, Style, Text [" " for clean color tile], Can Move To, Can see through, Description
basicTexture = {0: (Fore.GREEN, Back.GREEN, Style.NORMAL, " ", True, True, "acidic ground riddled with softly callous shiefs of green"), #Grass
                1: (Fore.YELLOW, Back.YELLOW, Style.NORMAL, " ", False, False, "strong but scarred sandstone walls"), #wall
                2: (Fore.BLACK, Back.BLACK, Style.NORMAL, " ", True, True, ""), #Void
                3: (Fore.GREEN, Back.GREEN, Style.BRIGHT, "T", True,"Lush trees, standing solemn gaurd against heaven"), #Tree
                4: (Fore.CYAN, Back.BLUE, Style.NORMAL, "~", True, True,"Luscious living waters, blood of the biosphere"), #water
                }
class Tile:
    def __init__(self,textColor=Fore.WHITE, backColor = Back.BLACK, styleType=Style.NORMAL, text=".", canWalk = "True", canSee = "False", descript = "Test"):
        """Initializes all of the normal Tile object """
        self.textColor = textColor #Color of rendered text
        self.backColor = backColor #Color of background tile
        slef.styleType = styleType #type of text style (dim, normal, bright) Note on Windows only Bright and Normal display
        self.text= text #rendered text
        self.canWalk = canWalk #can walk through/into this space
        self.canSee = canSee #can see through this space, is used for Line of Sight Code whenever I finish that bullfuckery
        self.descript = descript #description of text on Look command, e.g. "grassy ground, walls of sandstone"
        return
    def renderTile(self, textColor, backColor, styleType, text):
        """most basic rendering tile type"""
        print(textColor + backColor + styleType + text, end ="")
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
    def __init__(dataMap = basicMap, textureMap = basicTexture):
        """initalies and creates a map out of a map of data points that are keys in a texture map, defaults to the town test function"""
        self.areaMap = dataMap
        self.textureMap = textureMap
        self.height = len(dataMap)
        self.width = len(dataMap[0])
        for y in range(len(dataMap)):
            for x in range(len(dataMap[0])):
                key = dataMap[y][x]
                ###create tile
        return

###ACTOR CLASS
###New thought process - simulation has each actor working by relative speed, player first then everyone else

class Actor:
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x
        return
    def move(self,ny, nx):
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

#renderTile
#Renders a single tile
def renderTile(fcolor, bcolor, s, text):
    print(fcolor + bcolor + s + text, end = Style.RESET_ALL)
    return

#Rendering Screen
#Renders action screen BUT NOT UI or Prompt, those will be handeled by renderUI and userPrompt
#takes dictionary of current items and mobs, and puts their render atributes in a dictionary by (Y,X) coords
#for every tile to be rendered, check if (X,Y) in the display dictionary, otherwise print normal text object
#Most difficult bullshit to do tbh
#Texture used for rendering the area
def renderScreen(py,px,area = basicMap, items = {}, mobs = {}, texture = basicTexture):
    """Text Area to render, items and mobile actors(mobs) to be added as needed"""
    for y in range(len(area)):
        for x in range(len(area[0])):
            if (y,x) != (py,px):
                renderTile(texture[area[y][x]][0], texture[area[y][x]][1], texture[area[y][x]][2],texture[area[y][x]][3])
            elif (y,x) == (py,px):
                renderTile(Fore.WHITE, texture[area[y][x]][1], Style.NORMAL,"@")
        print(Style.RESET_ALL)
    return


#Rendering UI
#renders the little info textbox after the action map
def renderUI():
    return
#understanding user input
#basic syntax and help functions
#will be most in-depth bullshit to do

#returns CanMove value based on area, texture
def moveIsLegal(y,x,area,texture):
    return texture[area[y][x]][4]


def userPrompt(y,x, area, texture):
    while True:
        move = input("Write where you want to go: <N>orth, <W>est, <E>ast, or <S>outh")
        if move.lower() in ("n", "north") and moveIsLegal(y-1,x,area,texture):
            return (y-1,x)
        elif move.lower() in ("s", "south") and moveIsLegal(y+1,x,area,texture):
            return (y+1,x)
        elif move.lower() in ("w", "west") and moveIsLegal(y,x-1,area,texture):
            return(y,x-1)
        elif move.lower() in ("e", "east") and moveIsLegal(y,x+1,area,texture):
            return(y,x+1)
        else:
            print(Fore.GREEN + "I'm sorry, that was an invalid command or position")
    return

#World Update
#Takes playerAction, mobs and runs through the ai/effects of each action 

#Main cycle
def main():
    #DO SETUP HERE
    #e.g. read in files, texture, mobs
    #roughshod system for player movement
    py = 1
    px = 1
    game = True
    while game:
        renderScreen(py,px)
        newSpace = userPrompt(py,px,basicMap,basicTexture)
        py = newSpace[0]
        px = newSpace[1]
    return

main()
