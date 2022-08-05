def gcd(x:int, y:int) -> int:
    if y == 0:
        return x

    else:
        return gcd(y,x%y)

if __name__ == "__main__":
    print('두 정숫값의 최대 공약수를 구합니다.')
    x,y=map(int,input('첫 번째, 두 번째 정숫값을 입력하세요.: ').split())
    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}')