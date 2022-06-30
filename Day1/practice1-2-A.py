def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙값을 출력합니다.')
a,b,c=map(int,input('정수 a,b,c의 값을 입력하세요.: ').split())

print(f'중앙값은 {med3(a,b,c)}입니다.')