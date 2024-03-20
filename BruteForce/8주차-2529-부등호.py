K =  int(input())
signs = list(input().split()) + ['1']  #for k+1 iteration, add one element

max_digit = ''
stack, num = [], 9
for i in range(K+1):
    if signs[i] == '<':
        stack.append(num)
    else:
        max_digit += str(num)
        while stack:
            max_digit += str(stack.pop())
    num -= 1

min_digit = ''
stack, num = [], 0
for i in range(K+1):
    if signs[i] == '>':
        stack.append(num)
    else:
        min_digit += str(num)
        while stack:
            min_digit += str(stack.pop())
    num += 1

print(max_digit)
print(min_digit)
