import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class BST:
    def __init__(self):
        test = ["Harmony", "Dream", "Peace", "Butterfly", "Energy"," Journey", "Rainbow", "Apple", "Courage", None, "Garden", None, "Nature", "Quest", "Treasure"] # test array
        self.__tree = test # set testing array
        
        # self.__tree = []
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
        if not target:
            return False
        
        self.__current = 0
        self.__left = 1
        self.__right = 2
        try:
            while self.__tree[self.__current]:
                print("current:", self.__tree[self.__current])
                print("left: ", self.__tree[self.__left])
                print("right: ", self.__tree[self.__right])
                print("\n")
                
                if (target.lower() == self.__tree[self.__current].lower()):
                    return True
                
                if(target.lower() < self.__tree[self.__current].lower()):
                    self.__goLeft()
                else:
                    self.__goRight()
        except IndexError:
            return True
        
        except:
            return False
    
    def findMin(self):
        self.__current = 0
        self.__left = 1
        self.__right = 2
        
        try:
            while self.__tree[self.__current]:
                print("current:", self.__tree[self.__current])
                print("left: ", self.__tree[self.__left])
                print("right: ", self.__tree[self.__right])
                print("\n")
                
                if self.__left >= len(self.__tree) or not self.__tree[self.__left]:
                    return self.__tree[self.__current]
                else:
                    self.__goLeft()
                    
        except IndexError :
            return self.__tree[self.__current]
        
        except:
            return False
        
    def findMax(self):
        self.__current = 0
        self.__left = 1
        self.__right = 2
        try:
            while self.__tree[self.__current]:
                print("current:", self.__tree[self.__current])
                print("left: ", self.__tree[self.__left])
                print("right: ", self.__tree[self.__right])
                print("\n")
                
                if self.__right >= len(self.__tree) or not self.__tree[self.__right]:
                    return self.__tree[self.__current]
                else:
                    self.__goRight()
                    
        except IndexError :
            return self.__tree[self.__current]
        
        except:
            return False
        
def menu():
    while True:
        try:
            print("** Menu **\n")
            print("1.Set tree (It will remove old tree)")
            print("2.See tree")
            print("3.Find value")
            print("4.Find min")
            print("5.Find max")
            select = int(input("\n-"))
            return select
        except ValueError:
            clear_screen()
            continue
    
def main():
    Tree = BST()
    while True:
        clear_screen() 
        select = menu()
        if (select == 1): # set tree
            clear_screen()
            Tree.setTree([])
            tree = []
            
            while True:
                clear_screen()
                print("** Tree **\n")
                print(tree, "\n")
                print("Type 1 to add None")
                print("Type 0 to exit\n")
                
                data = input(f"Input data: ")
                print("\n")
                if (data == "0"):
                    break
                
                if data == "1":
                    tree.append(None)
               
                checkSpaces = "".join(data.split())
                if not data or checkSpaces == "":
                   continue
                    
                try:
                    data = int(data)
                    continue
                
                except ValueError:
                    tree.append(data)
                
            Tree.setTree(tree)
            continue
        
        if (select == 2): # see tree
            clear_screen()
            print("** Tree **\n")
            print(Tree.getTree(), "\n")
            print("Enter to exit\n")
            input()
            continue
        
        if(select == 3): # find value
            while  True:
                clear_screen()
                print("** Tree **\n")
                print(Tree.getTree(), "\n")
                print("** Find Value **\n")
                target = input("Input value: ")
                    
                if target.isalpha():
                    break
                else:
                    continue
               
            if (Tree.findValue(target)):
                print("\nFound: ", target)
            else:
                print("\nNot found: ", target)
                
            input("\nEnter to exit")
            continue
                
        if(select == 4): # find min
            clear_screen()
            print(f"\nMinimum value: {Tree.findMin()}")
            print("\nEnter to exit\n")
            input()
            continue
        
        if(select == 5): # find max
            clear_screen()
            print(f"\nMaximum value: {Tree.findMax()}")
            print("\nEnter to exit\n")
            input()
            continue
            
if __name__ == "__main__":
    main()
    