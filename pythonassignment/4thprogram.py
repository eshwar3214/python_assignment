# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to calculate the product of two n*n matrices

a,b,c=[],[],[]
n=int(input('enter order'))
print("enter elements of first matrix")
for i in range(1,n+1):
      p=[]
      for j in range(1,n+1):
          s=int(input((i,j) ))
          p.append(s)
      a.append(p)
print("enter elements of 2nd matrix")
for i in range(1,n+1):
      d=[]
      for j in range(1,n+1):
            t=int(input((i,j) ))
            d.append(t)
      b.append(d)
for i in range(1,n+1):
      r=[]
      for j in range(1,n+1):
            r.append(0)
      c.append(r)
for i in range(n):
      for j in range(n):
            for k in range(n):
                  c[i][j]+=a[i][k]*b[k][j]
print("product of marices is ")
for i in c:
      print(i)