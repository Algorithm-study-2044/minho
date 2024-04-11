## Solution1
n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

maximum, minimum = -float("INF"), float("INF")
def dfs(rslt, depth, operator):
    if depth == n:
        global maximum, minimum
        maximum = max(maximum, rslt)
        minimum = min(minimum, rslt)
        return
    
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                dfs(rslt+nums[depth], depth+1, operator)
            elif i == 1:
                dfs(rslt-nums[depth], depth+1, operator)
            elif i == 2:
                dfs(rslt*nums[depth], depth+1, operator)
            else:
                if rslt < 0:
                    dfs(-(-rslt//nums[depth]), depth+1, operator)
                else:
                    dfs(rslt//nums[depth], depth+1, operator)
            operator[i] += 1
    return

dfs(nums[0], 1, operator)
print(maximum)
print(minimum)


## Solution2 - using relationship between idx and operator
n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

maximum, minimum = -float("INF"), float("INF")
def dfs(rslt, operator):
    idx = n - sum(operator)
    if idx == n:
        global maximum, minimum
        maximum = max(maximum, rslt)
        minimum = min(minimum, rslt)
        return
    
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                dfs(rslt+nums[idx], operator)
            elif i == 1:
                dfs(rslt-nums[idx], operator)
            elif i == 2:
                dfs(rslt*nums[idx], operator)
            else:
                if rslt < 0:
                    dfs(-(-rslt//nums[idx]), operator)
                else:
                    dfs(rslt//nums[idx], operator)
            operator[i] += 1
    return

dfs(nums[0], operator)
print(maximum)
print(minimum)
