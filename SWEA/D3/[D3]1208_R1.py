# Flatten

for test_case in range(1, 11):
    dump_count = int(input())
    box_height = list(map(int, input().split()))

    for flatten in range(dump_count):
        diff = max(box_height) - min(box_height)

        if diff <= 1:
            break
        else:
            max_val = max(box_height)
            min_val = min(box_height)
            box_height[box_height.insight(max_val)] -= 1
            box_height[box_height.insight(min_val)] += 1
        
    diff = max(box_height) - min(box_height)
    print(f'#{test_case} {diff}')

