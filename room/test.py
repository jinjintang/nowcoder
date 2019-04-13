n=int(input())
p=list(map(int,input().split()))
M=10e9+7
v=[0]*(n+2)
for i in range(2,n+2):
    v[i]=((2*v[i-1])%M-v[p[i-2]]%M+2)%M
print(int(v[n+1]))
