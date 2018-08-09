#! usr/bin/python3

class SetMenu:
    def __init__(self,menuitems):
        menu_items=menuitems
        self.menuitems=set()
        for i in menu_items:
            self.menuitems.add(i)
    def __len__(self):
        return len(self.menuitems)
    def __str__(self):
        st=''
        for i in self.menuitems:
            st=st+'Item: '+i.name+', Cost: '+str(i.cost)+', Rating: '+str(format(i.rating, '.6f'))+'\n'
        return st
    
    
