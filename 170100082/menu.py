#! usr/bin/python3

class Menu:
    def __init__(self,items):
        self.items=items
    def __len__(self):
        return len(self.items)
    def __str__(self):
        st=''
        for i in self.items:
            st=st+'Item: '+i.Name+', Cost: '+str(i.Cost)+', Rating: '+str(format(i.Rating, '.6f'))+'\n' 
        return st
