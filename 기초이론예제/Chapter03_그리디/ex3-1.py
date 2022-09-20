N=1260
count=0

coin_type=[500, 100, 50, 10]
for coin in coin_type:
    count+=N//coin   #동전 개수     
    N%=coin          #나눈 후 잔액

print(count)

# N//coin = int(N//coin)
# //: 나누었을 때 몫의 정수형

'''
처음 풀이

N=1260  #거스름돈
count=0 #동전 개수

c1=0
c2=0
c3=0
c4=0

c1=int(N/500)
N-=500*c1

c2=int(N/100)
N-=100*c2

c3=int(N/50)
N-=50*c3

c4=int(N/10)
count=c1+c2+c3+c4

print(count)
'''