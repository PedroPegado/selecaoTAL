n = int(input())

nums = [1, 2, 3]

for c in range(n):
    if c == 0:
        print(f'{nums[0]} {nums[1]} {nums[2]} PUM')
    else:
        nums[0] += 4
        nums[1] += 4
        nums[2] += 4
        print(f'{nums[0]} {nums[1]} {nums[2]} PUM')
    