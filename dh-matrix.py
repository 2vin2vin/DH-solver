import math
from math import cos,sin,tan,pi


m00='c(theta)'
m01='s(theta)'
m10='c(alpha)'
m11='s(alpha)'
r='r'
d='d'
n0='0'
n1='1'

def neg(m):
	if m[0]=='-':
		m=m[1:]
	else:
		m='-'+m
	return m

def join(a,b,value=None):
	if type(value)==int:
		if a=='r' or a=='d':
			a=a+str(value)
		else:
			a[-1]=str(value)
			a=a+')'
		if b=='r' or b=='d':
			b=b+str(value)
		else:
			b[-1]=str(value)
			b=b+')'
	return '('+ a+' x '+ b+')'

mat=[[m00,neg(join(m01,m10)),join(m01,m11),join(r,m00)],[m01,join(m00,m10),neg(join(m00,m11)),join(r,m01)],[n0,m11,m10,d],[n0,n0,n0,n1]]
value=int(input("enter nos of dh parameter rows:"))

def val(mat,value):
	matx=[]
	for i in range(0,4):
		matr=[]
		for j in range(0,4):
			a=mat[i][j]
			if a=='r' or a=='d':
				a=a+str(value)
			elif a=='1' or a=='0':
				a=a
			else:
				a=a.replace('a)','a'+str(value)+')')
			matr.append(a)
		matx.append(matr)
	return matx

def mul(a,b):
	x1=[]
	for i in range(0,4):
		x=[]
		for j in range(0,4):
			if a[i][j]=='0' or b[j][i]=='0':
				x.append('0')
			else:
				x.append(join(a[i][j],b[j][i]))
		x1.append(x)
	return x1


for k in range(1,value+1):
	if k==1:
		maty=val(mat,1)
		continue
	else:
		matz=val(mat,k)
		maty=mul(maty,matz)

print(maty)
		
def output():
	return maty
