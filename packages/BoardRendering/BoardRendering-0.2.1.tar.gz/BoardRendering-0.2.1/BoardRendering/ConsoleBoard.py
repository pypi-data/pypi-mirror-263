from .Exceptions import Exceptions
class Board:
    """Class of the board to use them"""
    def __init__(self, size : int, default : str):
        if size > 0: pass
        else: raise Exceptions.InvalidBoard("Board Size must be Greater then 0")
        self.size = size
        if default is not None: self.default = default
        else: self.default = "0"
        self.pixels = size * size
        xbase = ""
        for i in range(0, size):
            xbase = xbase + self.default
        sd = ""
        for i in range(0, size):
            sd = sd + xbase
        self.BD = sd
        display = ""
        for i in range(0, size):
            if i != self.size - 1: n = "\n"
            else: n = ""
            display = display + f"{xbase}{n}"
        self.display = display

    def get(self, position : tuple):
        """Returns the value of the position"""
        x = position[0]
        y = position[1]
        if x > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if y > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if x < 0: raise Exceptions.InvalidPosition("Position out of range")
        if y < 0: raise Exceptions.InvalidPosition("Position out of range")
        b = self.display.replace("\n", "")
        return(b[x + (y * self.size)])
    
    def set(self, position : tuple, new : str):
        """Sets the position of a value"""
        x = position[0]
        y = position[1]
        if x > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if y > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if x <  0: raise Exceptions.InvalidPosition("Position out of range")
        if y < 0: raise Exceptions.InvalidPosition("Position out of range")
        b = self.display
        b = b.replace("\n", "")
        bl = list(b)
        bl[x + (y * self.size)] = new
        newb = ""
        index = 0
        for l in bl:
            if index != self.size - 1: 
                newb = newb + l
                index += 1
            else: 
                newb = newb + f"{l}\n"
                index = 0
        self.display = newb
    
    def instances(self, search : str):
        """Returns a list of tuples of the positions of all instances of the provided Search"""
        found = []
        for y in range(0, self.size):
            for x in range(0, self.size):
                if self.get(position=(x, y)) == search: found.append((x, y))
        return(found)

    def randomposition(self):
        import random
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return((x,y))


    
    def pathfind(self, a, b):
        """Finds a path between two positions on the board"""
        if a[0] > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if a[1] > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if b[0] > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if b[1] > self.size - 1: raise Exceptions.InvalidPosition("Position out of range")
        if a[0] < 0: raise Exceptions.InvalidPosition("Position out of range")
        if a[1] < 0: raise Exceptions.InvalidPosition("Position out of range")
        if b[0] < 0: raise Exceptions.InvalidPosition("Position out of range")
        if b[1] < 0: raise Exceptions.InvalidPosition("Position out of range")
        cycle = False
        bx = b[0]
        by = b[1]
        currentpos = a
        positions = []
        while True:
            dontadd = False
            newpos = currentpos
            newposx = newpos[0]
            newposy = newpos[1]
            if cycle is False:
                if currentpos[0] > bx:
                    newposx -= 1
                elif currentpos[0] < bx:
                    newposx += 1
            elif cycle is True:
                if currentpos[1] > by:
                    newposy -= 1
                if currentpos[1] < by:
                    newposy += 1
            cycle = not cycle
            currentpos = (newposx, newposy)
            if currentpos == b:
                break
            if len(positions) > 0:
                if currentpos == positions[len(positions) - 1]:
                    dontadd = True
            if dontadd is False:
                positions.append(currentpos)
        return(positions)