import sys
input=sys.stdin.readline

N,P,Q=map(int, input().split())
A={}
A[0]=1

def get_(N):
    first_=N//P
    second_=N//Q
    if A.get(N,0):
        return A[N]
    if not A.get(first_,0):
        A[first_]=get_(first_)
    if not A.get(second_,0):
        A[second_]=get_(second_)
    return A[first_]+A[second_]
    
print(get_(N))
