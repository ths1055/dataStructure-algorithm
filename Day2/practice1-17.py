area=int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1,area+1):
    if i*i > area: break
    if area%i != 0: continue
    print(f'{i} X {area//i}')