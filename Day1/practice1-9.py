print('a부터 b까지 정수의 합을 구합니다.')
a,b=map(int,input('정수 a b를 입력하세요.: ').split())

if a > b:
    a,b=b,a

sum=0
for i in range(a,b+1):
    sum+=i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')