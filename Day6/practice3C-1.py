from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int:
    for i,value in enumerate(a):
        if value == key:
            return i
    return -1

if __name__ == "__main__":
    print('실수를 검색합니다.')
    print('주의: "End"를 입력하면 종료합니다.')

    number=0
    x=[]

    while True:
        s=input(f'x[{number}]: ')
        if s == "End":
            break
        x.append(float(s))
        number+=1
    ky=float(input('검색할 값을 입력하세요.: '))

    idx=seq_search(x,ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')