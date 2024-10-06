import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class BST:
    
    def __init__(self):
        # test array
        # test = ["Harmony", "Dream", "Peace", "Butterfly", "Energy"," Journey", "Rainbow", "Apple", "Courage", None, "Garden", None, "Nature", "Quest", "Treasure"] 
         # set test array
        # self.__tree = test
        
        self.__tree = []
        self.__current = 0
        self.__left = 1
        self.__right = 2
        
    def __goLeft(self):
        self.__current = self.__left
        self.__left = self.__current * 2 + 1
        self.__right = self.__left + 1
        
    def __goRight(self):
        self.__current = self.__right
        self.__left = self.__current * 2 + 1
        self.__right = self.__left + 1
    
    def setTree(self, tree):
        self.__tree = tree
        
    def getTree(self):
        return self.__tree

    def findValue(self, target):
        if not any(target.lower() in item.lower() for item in self.__tree if item is not None):
            return False
        
        self.__current = 0
        self.__left = 1
        self.__right = 2
        
        while self.__current < len(self.__tree)-1 and self.__tree[self.__current] is not None:
            
            print("current:", self.__tree[self.__current])
            
            if self.__left < len(self.__tree):
                print("left:", self.__tree[self.__left])
            else:
                print("left: None")
        
            if self.__right < len(self.__tree):
                print("right:", self.__tree[self.__right])
            else:
                print("right: None")
            print("\n")
                
            if (target.lower() == self.__tree[self.__current].lower()):
                return True
                
            if(target.lower() < self.__tree[self.__current].lower()):
                self.__goLeft()
            else:
                self.__goRight()
        
        return False
    
    def findMin(self):
        self.__current = 0
        self.__left = 1
        self.__right = 2
        
        print("** Tree **\n")
        print(self.__tree)
        print("\n")
        
        if not self.__tree :
            print("\n** Tree is empty **")
            return False
        
        try:
            while self.__tree[self.__current]:
                
                print("current:", self.__tree[self.__current])
                if self.__left < len(self.__tree):
                    print("left:", self.__tree[self.__left])
                else:
                    print("left: None")            
                print("\n")
                
                if self.__left >= len(self.__tree) or self.__tree[self.__left] is None:
                    return self.__tree[self.__current]
                else:
                    self.__goLeft()
                
        except IndexError :
            return self.__tree[self.__current]
            
        return False
        
    def findMax(self):
        self.__current = 0
        self.__left = 1
        self.__right = 2
        
        print("** Tree **\n")
        print(self.__tree)
        print("\n")
        
        if not self.__tree :
            print("\n** Tree is empty **")
            return False
        
        try:
            while self.__tree[self.__current]:
                
                print("current:", self.__tree[self.__current])
                if self.__right < len(self.__tree):
                    print("right:", self.__tree[self.__right])
                else:
                    print("right: None")
                print("\n")
                
                if self.__right >= len(self.__tree) or self.__tree[self.__right] is None:
                    return self.__tree[self.__current]
                else:
                    self.__goRight()
                    
        except IndexError :
            return self.__tree[self.__current]
        
        return False

def menu(Tree):
    err = ""
    while True:
        try:
            print("** Tree **\n")
            print(Tree.getTree(), "\n")
            
            print("** Menu **\n")
            print("1.Set tree (It will remove old tree)")
            # print("2.See tree")
            print("2.Find value")
            print("3.Find min")
            print("4.Find max")
            
            # print("\n99.set Test Tree")
            
            if len(err)>0:
                print(err)
                err = ""
                
            select = int(input("\n-"))
            return select
        
        except ValueError:
            err = "\n** The input must be a number !! **\n"
            clear_screen()
            continue

def main():
    Tree = BST()
    
    while True:
        clear_screen() 
        select = menu(Tree)
        if (select == 1): # set tree
            clear_screen()
            tree = []
            Tree.setTree(tree)
            err = ""
            while True:
                clear_screen()
                print("** Tree **\n")
                print(tree, "\n")
                print("Type 1 to add None")
                print("Type 0 to exit\n")
                
                if len(err) > 0: 
                    print(err)
                    err = ""
                
                data = input(f"Input data: ")
                print("\n")
                
                checkSpaces = "".join(data.split())
                
                if (data == "0"):
                    break
                
                elif data == "1":
                    tree.append(None)
                    continue
                
                elif checkSpaces == "":
                    err = "** Input must be a character only **\n"          
                    continue
                
                elif data.isalpha():
                    tree.append(data)
                    
                else:
                    err = "** Input must be a character only **\n"
                    continue
                
            Tree.setTree(tree)
            continue

        # if (select == 2): # see tree
        #     clear_screen()
        #     print("** Tree **\n")
        #     print(Tree.getTree(), "\n")
        #     print("Enter to exit\n")
        #     input()
        #     continue
        
        if(select == 2): # find value
            err = ""
            while  True:
                clear_screen()
                print("** Tree **\n")
                print(Tree.getTree(), "\n")
                print("** Find Value **\n")
                print("Type 0 to exit\n")
                
                if len(err)>0:
                    print(err)
                    err = ""
                    
                target = input("Input value: ")
                print("\n")
                
                if target == "0":
                    break
                    
                if target.isalpha():
                    break
                else:
                    err = "** Input must be a character only **\n"
                    continue
               
            if target == '0': continue
            if (Tree.findValue(target)):
                print("Found: ", target)
            else:
                print("Not found: ", target)
                
            input("\nEnter to exit\n")
            continue
                
        if(select == 3): # find min
            clear_screen()
            print("** Find Minimum value **\n")
            print(f"\nMinimum value: {Tree.findMin()}")
            input("\nEnter to exit\n")
            continue
        
        if(select == 4): # find max
            clear_screen()
            print("** Find Maximum value **\n")
            print(f"\nMaximum value: {Tree.findMax()}")
            input("\nEnter to exit\n")
            continue
        
        if(select == 99): # set test array
            # test array
            test = ["Harmony", "Dream", "Peace", "Butterfly", "Energy"," Journey", "Rainbow", "Apple", "Courage", None, "Garden", None, "Nature", "Quest", "Treasure"] 
            Tree.setTree(test)
            continue
            
if __name__ == "__main__":
    main()
    