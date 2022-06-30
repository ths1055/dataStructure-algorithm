print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1,score2,score3,score4,score5=map(int,input('1 2 3 4 5번 학생의 점수를 입력하세요.: ').split())

total=0
total+=score1;total+=score2;total+=score3;total+=score4;total+=score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total/5}점입니다.')