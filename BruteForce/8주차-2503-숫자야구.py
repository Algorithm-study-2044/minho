import sys, itertools

n = int(input())
nums = [[1, ''.join(i)] for i in itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3)]

for _ in range(n):
    guess, strike, ball = sys.stdin.readline().rstrip().split()

    for i in range(len(nums)):
        valid, num = nums[i]
        if not valid:
            continue
        s_cnt = b_cnt = 0
        for j in range(3):
            if num[j] == guess[j]:
                s_cnt += 1
            elif guess[j] in num:  #strike가 아니면, ... ball -> else if
                b_cnt += 1
        if s_cnt != int(strike) or b_cnt != int(ball):
            nums[i][0] = 0

ans = 0
for i in range(len(nums)):
    if nums[i][0]:
        ans += 1
print(ans)
  #solution
