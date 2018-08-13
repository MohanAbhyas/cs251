#! /usr/bin/python3

class MenuItem:
    def __init__(self,Name,Cost,Rating):
        self.Name=Name
        self.Cost=Cost
        self.Rating=Rating
    def __eq__(self,A):
        if self.Name==A.Name and self.Cost==A.Cost and self.Rating==A.Rating:
            return True
        else:
            return False
    def __str__(self):
        st='Item: '+self.Name+', Cost: '+str(self.Cost)+', Rating: '+str(format(self.Rating, '.6f'))
        return st
    def __hash__(self):
        return hash(str(self.Name)+str(self.Cost)+str(self.Rating)) 
    def __lt__(self,A):
        return self.Rating<A.Rating
