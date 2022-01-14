import kin_solver
from kin_solver import output
import math
from math import cos,sin,tan,pi

maty=output()
matz=maty
nos=maty[-1][-1].count('1')

p=pi/180
final=[]
the,alp,re,de=[],[],[],[]
for i in range(1,nos+1):
	theta=float(input("Enter theta"+str(i)+":"))
	alpha=float(input("Enter alpha"+str(i)+":"))
	r=float(input("Enter r"+str(i)+":"))
	d=float(input("Enter d"+str(i)+":"))
	the.append(theta)
	alp.append(alpha)
	re.append(r)
	de.append(d)


for j in range(0,4):
	matr=[]
	for k in range(0,4):
		maty=matz[j][k]
		for i in range(0,len(alp)):
			maty=maty.replace('c(theta'+str(i+1)+')',str(cos(the[i]*p)))
			maty=maty.replace('s(theta'+str(i+1)+')',str(sin(the[i]*p)))
			maty=maty.replace('c(alpha'+str(i+1)+')',str(cos(alp[i]*p)))
			maty=maty.replace('s(alpha'+str(i+1)+')',str(sin(alp[i]*p)))
			maty=maty.replace('r'+str(i+1),str(re[i]))
			maty=maty.replace('d'+str(i+1),str(de[i]))
		matr.append(maty)
	final.append(matr)

print(final)
