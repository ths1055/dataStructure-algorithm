from __future__ import annotations
from select import select
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED=0
    EMPTY=1
    DELETED=2

class Bucket:
    def __init__(self, key:Any=None, value:Any=None, stat:Status=Status.EMPTY) -> None:
        self.key=key
        self.value=value
        self.stat=stat

    def set(self, key:Any, value:Any, stat:Status) -> None:
        self.key=key
        self.value=value
        self.stat=stat

    def set_status(self, stat:Status) -> None:
        self.stat=stat

class OpenHash:
    def __init__(self, capacity:int) -> None:
        self.capacity=capacity
        self.table=[Bucket()]*self.capacity

    def hash_value(self, key:Any) -> int:
        if isinstance(key,int):
            return key%self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capacity)

    def rehash_value(self, key:Any) -> int:
        return(self.hash_value(key)+1)%self.capacity
    
    def search_node(self, key:Any) -> Any:
        hash=self.hash_value(key)
        p=self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash=self.rehash_value(hash)
            p=self.table[hash]
        return None

    def search(self, key:Any) -> Any:
        p=self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
        
    def add(self, key:Any, value:Any) -> bool:
        if self.search(key) is not None:
            return False

        hash=self.hash_value(key)
        p=self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash]=Bucket(key,value,Status.OCCUPIED)
                return True
            hash=self.rehash_value(hash)
            p=self.table[hash]
        return False

    def remove(self, key:Any) -> int:
        p=self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ',end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제완료--')

if __name__ == "__main__":
    Menu=Enum('Menu',['추가','삭제','검색','덤프','종료'])

    def select_menu() -> Menu:
        s=[f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s, sep='', end='')
            n=int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)

    hash=OpenHash(13)
    while True:
        menu=select_menu()
        if menu == Menu.추가:
            key=int(input('추가할 키를 입력하세요.: '))
            val=input('추가할 값을 입력하세요.: ')
            if not hash.add(key,val):
                print('추가를 실패했습니다.')

        elif menu == Menu.삭제:
            key=int(input('삭제할 키를 입력하세요.: '))
            if not hash.remove(key):
                print('삭제를 실패했습니다.')
                
        elif menu == Menu.검색:
            key=int(input('검색할 키를 입력하세요.: '))
            t=hash.search(key)
            if t is not None:
                print(f'검색한 키를 갖는 값은 {t}입니다.')
            else:
                print('검색할 데이터가 없습니다.')

        elif menu == Menu.덤프:
            hash.dump()

        else:
            break