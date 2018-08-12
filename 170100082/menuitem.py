#! /usr/bin/python3

class MenuItem:
    def __init__(self,name,cost,rating):
        self.name=name
        self.cost=cost
        self.rating=rating
    def __eq__(self,A):
        if self.name==A.name and self.cost==A.cost and self.rating==A.rating:
            return True
        else:
            return False
    def __str__(self):
        st='Item: '+self.name+', Cost: '+str(self.cost)+', Rating: '+str(format(self.rating, '.6f'))
        return st
    def __hash__(self):
        return hash(self.rating)
    def __lt__(self,A):
        return self.rating<A.rating
    
