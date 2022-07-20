data=[[1,2,3],[4,5,6],[7,8,9]]

for r, row in enumerate(data):#r에는 반복값 row에는 data의 r번째 값
    for c, col in enumerate(row):
        print(r,col)