import sys 

input=sys.stdin.readline


N = int(input())
sum = 0
start_, end_ = dict(), []
for i in range(N):
	car = input()
	start_[car] = i
for _ in range(N):
	car = input()
	end_.append(car)
 
for i in range(N-1):
	for j in range(i+1, N):
		if start_[end_[i]] > start_[end_[j]]:
			sum += 1
			break
print(sum)
