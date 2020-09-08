from random import *

def recur(li1, li2, result) :
    # 결과값 추가
    result.append(li1)
    
    # enumerate를 통해 현재 횟수 + li2값 하나를 꺼냄 ->  재귀함수를 호출하고, 호출될 때마다 li1 + [x]를 결과값에 추가하고 + 반복문을 진행
    for i, x in enumerate(li2) :
        # 1번째 인자로 기존의 li1에 꺼낸 값을 추가, 2번재 인자로 꺼낸 값을 제외한 나머지 li2를 전달, 3번째 인자로 기존의 결과값 저장을 위한 리스트 전달
        recur(li1 + [x], li2[i+1:], result)

def comb(li) :
    
    # 중복제거
    li = list(set(li))
    
    # 결과값 저장을 위한 빈 리스트 생성
    result = []

    # 재귀함수 호출. call by assignment를 통해 result에 결과값이 담겨서 옴
    recur([], li, result)
    
    # 0번째 인덱스 값은 빈 리스트이기 때문에 버리고 return
    return result[1:]

# test
if __name__ == "__main__" :

    li1 =[x for x in range(randint(1, 10))]

    # 중복 제거 잘 되는지 확인
    li2 =[x for x in range(randint(1, 10))] + [x for x in range(randint(1, 10))]    

    test1 = comb(li1)
    test2 = comb(li2)
    
    print(li1)
    print(test1)
    print(li2)
    print(test2)
