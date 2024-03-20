import sys
input = sys.stdin.readline

word = input().rstrip() # 디버깅 과정에서 문자 끝에 빈칸 생기는 것 발견!!!
word = word.upper() # 결과가 대문자로 출력되서 처음에 대문자로 바꾸고 시작

# a부터 z까지 만들어 놓고 for문 돌리기엔 시간 초과가 발생할 듯;;
# 문자를 숫자로 바꿔서 리스트 인덱스에 연결하여 +1 하면 굳이 다 돌지 않아도 되지 않을가?
# 아스키 코드 활용 A:65, Z:90
# 아스키 코드에서 65 뺴면 리스트 0부터 인덱싱 가능

word_list = [0]*26
for i in word:
    word_index = ord(i)-65
    word_list[word_index] += 1
# print(word_list)

max_value = max(word_list)
# print(max_value)

max_cnt = word_list.count(max_value)
# print(max_cnt)

if max_cnt == 1:
    index = word_list.index(max_value)
    print(chr(index+65))
else:
    print('?')
    
    
### 1년 전의 내가 푼 풀이
### 1년 전의 내가 더 똑똑한 듯?
N = input().upper().strip() ##strip 중요 뒤에 엔터 지워줌
N_set = list(set(N))

cnt = []
for i in N_set:
    cnt.append(N.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(N_set[cnt.index(max(cnt))])