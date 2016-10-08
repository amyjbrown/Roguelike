import init from colorama
import Fore, Back, Style from Colorama
init()
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
                areaMap[y][x]
