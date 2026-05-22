# Flatten - 평탄화 작업
# 평탄화 작업을 위해 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
# 평탄화를 모두 수행한 이후 최고점과 최저점의 차이가 최대 1이 된다. 
# 가로 길이는 항상 100, 모든 위치에서 상자의 높이는 1이상 100이하
# 덤프 횟수는 1이상 1000이하

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

for test_case in range(1, 11):
    dump_count = int(input())

    # list로 받아야 함
    box_height = list(map(int, input().split()))

    # 덤프 횟수만큼 반복
    for flatten in range(dump_count):
        diff = max(box_height) - min(box_height)

        if diff <= 1: # 평탄화 완료
            break
        else: 
            # index(): 해당 값의 위치를 찾아주는 함수 
            box_height[box_height.index(max(box_height))] -= 1
            box_height[box_height.index(min(box_height))] += 1

    diff = max(box_height) - min(box_height)
    print(f'#{test_case} {diff}')