from itertools import combinations_with_replacement
#1부터 100장의 중복개수 개의  n장 카드
#이중 3장을 아무거나 뽑아 중복가능한 합한 값을 기록한다.
#기록 값 중 k번째 큰 수를 출력하는 프로그램

list(combinations_with_replacement(n,3))