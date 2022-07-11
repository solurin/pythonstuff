#   Name:      Nick Soluri
#   Class:      CSC 112  Spring 2019
#   Project:    #3 -- create our own hashmap

from Array import *
from obj import *
import sys

class HashMap:
    '''   explain the structure here '''

    def __init__(self, size,  percent_collision=25):
        ''' This method is DONE!  Do not change'''

        self.array = Array(size)
        self.percent_collision = percent_collision
        self.boundary = int(size * (1-percent_collision/100))
        self.next_ovflow = self.boundary   # where the next overflow value will be store
        self.debug = False
    
    def put(self, key, newvalue):
        '''see the handout, too complicated '''
        index = hash(key)
        if array[index] == None:
            self.array[index] = Object(key, value)
        elif array[index].key == key:
            array[index].value = newvalue
        else:
            ####

        
        pass

    def get_location(self, key):
        '''see the handout, too complicated '''
        pass

    def get(self, key):
        ''' use get_location and if it returns > -1, get the value at self.array[index].value '''
        pass

    def hash(self, key):
        ''' add up the ord of each character of the string of key and return modulo the size of
          self.array sans the upper percent_collision number of slots that are reserved for the
          collision area.
        '''
        pass

    #------------------------------everything from here on down is done, don't change!---------------------

    def exists(self, key):
        ''' Returns True if an object with this key is in the array  [DONE] 
        return self.get_location(key) == -1
        '''
        

    def delete(self, key):
        '''use get_location and if it returns > -1, then ask if index < self.boundary.
           If so, put Object("TOMBSTONE", None) into self.array[index] to indicate it was deleted.
           If index >= self.boundary, then it is in the overflow area, so delete it and close up the
           empty space by calling  HashMap.moveUp(self.array, index)   [DONE] '''
        
        index = self.get_location(key)
        if index == -1:
            return   # not found
        if self.debug:
            print("Here we delete..." + str(key)+"    index="+str(index))
        if index < self.boundary:
            self.array[index] = Object("TOMBSTONE!", None)
        else:
            HashMap.moveUp(self.array, index)
            self.next_ovflow -= 1

    def moveUp(somelist, startingpos):
        '''   Deletes the item in the somelist at startingpos.  Moves all later values down by 1 slot
             to close up the 'hole.'  Puts None at the end. [DONE] '''
        i = startingpos
        print("moveUP, startingpos=",startingpos)
        print("len somelist=",len(somelist))
        sys.stdout.flush()
        while i < len(somelist)-1:
            print("i=",i)
            sys.stdout.flush()
            somelist[i] = somelist[i + 1]
            i += 1
        somelist[len(somelist)-1] = None

    def getKeys(self):
        ''' returns a sorted list of keys [DONE] '''
        allkeys = set()
        for i in range(0,len(self.array)):
            if self.array[i] is not None:
                allkeys.add(self.array[i].key)
        return sorted(list(allkeys))

    def getValues(self):
        ''' returns a sorted list of values, with duplicates removed. Go through the array sequentailly and
           put all the keys into a set and then return a sorted list of that set.  [DONE] '''
        allvalues = set()
        for i in range(0,len(self.array)):
            if self.array[i] is not None:
                allvalues.add(self.array[i].value)
        return sorted(list(allvalues))

    def findValue(self, somevalue):
        ''' returns a list of keys that have been mapped to this value.  Empty list if there are none. [DONE] '''
        keys = []
        for i in range(0,len(self.array)):
            if self.array[i] is not None and self.array[i].value == somevalue:
                keys.append(self.array[i].key)
        return sorted(keys)

    def clear(self):
        '''  Clear out all objects (by making a completely new array)  [DONE] '''
        self.array = Array(len(self.array))

    def info(self):
        ''' returns a string that contains all the vital stats about the hashmap  [DONE] '''

        rets = "Size: " + str(len(self.array)) + "\n"
        
        numcollision = 0
        for i in range(self.boundary,len(self.array)):
            if self.array[i] != None:
                numcollision += 1
        rets += "In collision : " + str(numcollision) + "\n"
        rets += "The last " + str(self.percent_collision) + "% of the slots are used for collisions."
        return rets

    def display(self):
        '''   Creates a string that is suitable for printing that shows the contents of the hashmap
             right now.  [DONE] '''
        s = ""
        for i in range(len(self.array)):
            flag = ("*" if i >= self.boundary else " ")
            s += "%s%3d. " % (flag, i)
            if self.array[i] != None:
                if self.array[i].value == None:
                    s += self.array[i].key + "=None"
                else:
                    s += self.array[i].key + "=" + self.array[i].value
            s += "\n"
        return s
