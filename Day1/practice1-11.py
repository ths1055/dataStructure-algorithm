print('a부터 b까지 정수의 합을 구합니다.')
a,b=map(int,input('정수 a b를 입력하세요.: ').split())

if a > b:
    a,b=b,a

sum=0
for i in range(a,b):
    print(f'{i}+',end='')
    sum+=i

print(f'{b}=',end='')
sum+=b

print(sum)