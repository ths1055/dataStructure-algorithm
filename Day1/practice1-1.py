print('세 정수의 최댓값을 구합니다.')

a,b,c=map(int,input('정수 a b c의 값을 입력하세요.: ').split())

maximum=a
if b > maximum: maximum=b
if c > maximum: maximum=c

print(f'최댓값은 {maximum}입니다.')