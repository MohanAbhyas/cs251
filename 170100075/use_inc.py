from inc import *
import sys 
k=sys.argv
input_file=k[1]
output_file=k[2]
flag=int(k[3])
try:
	data=np.loadtxt(input_file,delimiter=",")
	
	if (data.ndim==2 and flag==1):
		out=np.array(vec_to_ang(data))
		np.savetxt(output_file,out,delimiter=",")
	elif (data.ndim==1 and flag==0):
		out=ang_to_vec(data)
		np.savetxt(output_file,out,delimiter=",")
	else:
		raise ValueError
except Exception as e:
	exit(1)
