import numpy as np 
def ang_to_vec (ang):
	arg=np.deg2rad(ang)
	x=np.cos(arg)
	y=np.sin(arg)
	vector=np.column_stack((x,y))
	return vector

def ang_to_vec (vec):
	a=vec(...,0)
	b=vec(...,1)
	rad=np.arctan2(b,a) 		#arctan2(x,y) angle for computes x/y
	degree=np.degrees(rad)
	return degree