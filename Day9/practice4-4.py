from typing import Any
from enum import Enum

class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity:int) -> None:
        self.no=0
        self.front=0
        self.rear=0
        self.capacity=capacity
        self.que=[None]*capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <=0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear]=x
        self.rear+=1
        self.no+=1
        if self.rear == self.capacity:
            self.rear=0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x=self.que[self.front]
        self.front+=1
        self.no-=1
        if self.front == self.capacity:
            self.front=0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value:Any) -> Any: # idx값 변화 관찰 필요
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value:Any) -> bool:
        c=0
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            if self.que[idx]==value:
                c+=1
        return c

    def __contains__(self, value:Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no=self.front=self.rear=0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i+self.front)%self.capacity],end=' ')
            print()

if __name__ == "__main__":
    Menu=Enum('Menu',['인큐','디큐','피크','검색','덤프','종료'])
    
    def select_menu() -> Menu:
        s=[f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s,sep='   ', end='')
            n=int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)
    
    q=FixedQueue(64)
    while True:
        print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
        menu=select_menu()

        if menu == Menu.인큐:
            x=int(input('데이터를 입력하세요.: '))
            try:
                q.enque(x)
            except FixedQueue.Full:
                print('큐가 가득 차 있습니다.')
        
        elif menu == Menu.디큐:
            try:
                x=q.deque()
                print(f'디큐한 데이터는 {x}입니다.')
            except FixedQueue.Empty:
                print('큐가 비어있습니다.')
        
        elif menu == Menu.피크:
            try:
                x=q.peek()
                print(f'피크한 데이터는 {x}입니다')
            except FixedQueue.Empty:
                print('스택이 비어있습니다.')

        elif menu == Menu.검색:
            x=int(input('검색할 값을 입력하세요.: '))
            if x in q:
                print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
            
            else:
                print('검색값을 찾을 수 없습니다.')

        elif menu == Menu.덤프:
            q.dump()

        else:
            break
        