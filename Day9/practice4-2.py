from decimal import MIN_ETINY
from typing import Any
from enum import Enum

class FixedStack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity:int=256) -> None:
        self.stk=[None]*capacity
        self.capacity=capacity
        self.ptr=0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr<=0

    def is_full(self) -> bool:
        return self.ptr>=self.capacity

    def push(self, value:Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr]=value
        self.ptr+=1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr-=1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self) -> None:
        self.ptr=0

    def find(self, value:Any) -> Any:
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value:Any) -> int:
        c=0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c+=1
        return c
    
    def __contains__(self, value:Any) -> bool:
        return self.count(value)>0

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
            

if __name__ == "__main__":
    Menu=Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])
    
    def select_menu() -> Menu:
        s=[f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s,sep='   ', end='')
            n=int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)
    
    s=FixedStack(64)
    while True:
        print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
        menu=select_menu()

        if menu == Menu.푸시:
            x=int(input('데이터를 입력하세요.: '))
            try:
                s.push(x)
            except FixedStack.Full:
                print('스택이 가득 차 있습니다.')
        
        elif menu == Menu.팝:
            try:
                x=s.pop()
                print(f'팝한 데이터는 {x}입니다.')
            except FixedStack.Empty:
                print('스택이 비어있습니다.')
        
        elif menu == Menu.피크:
            try:
                x=s.peek()
                print(f'피크한 데이터는 {x}입니다')
            except FixedStack.Empty:
                print('스택이 비어있습니다.')

        elif menu == Menu.검색:
            x=int(input('검색할 값을 입력하세요.: '))
            if x in s:
                print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
            
            else:
                print('검색값을 찾을 수 없습니다.')

        elif menu == Menu.덤프:
            s.dump()

        else:
            break
        