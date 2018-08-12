#! usr/bin/python3

class Menu:
    def __init__(self,menuitems):
        self.menuitems=menuitems
    def __len__(self):
        return len(self.menuitems)
    def __str__(self):
        st=''
        for i in self.menuitems:
            st=st+'Item: '+i.name+', Cost: '+str(i.cost)+', Rating: '+str(format(i.rating, '.6f'))+'\n' 
        return st
    
    
