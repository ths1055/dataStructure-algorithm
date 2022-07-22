from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int:
    for i,value in enumerate(a):
        if value == key:
            return i
    return -1

if __name__ == "__main__":
    t=(4,7,5.6,2,3.14,1)
    s="string"
    a=['DTS','AAC','FLAC']

    print(f'{t}에서 5.6의 인덱스는 {seq_search(t,5.6)}입니다.')
    print(f'{s}에서 n의 인덱스는 {seq_search(s,"n")}입니다.')
    print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a,"DTS")}입니다.')