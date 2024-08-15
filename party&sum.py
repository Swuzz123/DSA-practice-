# Way 1:
# def solve(n,l):
#     odd, even = [], []
#     for i in l:
#         if i % 2 == 0: even += [i]
#         else: odd += [i]
#     if odd == [] or even == []:return 0
#     else:
#         odd.sort()
#         even.sort()
#         max_odd = max(odd)
#         ans = 0
#         for i in even:
#             if i < max_odd:
#                 max_odd += i
#                 ans += 1
#             else:
#                 max_odd += 2 * max(even)
#                 ans += 2
#         return ans

# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     print(solve(n,l))
    
#Way 2:
def solve(n, l):
    odd, even = [], []
    
    for i in l:
        if i%2 != 0: 
            odd.append(i)
        else:
            even.append(i)
        
    if(len(odd) == 0 or len(even) == 0):
        return 0
    
    odd.sort()
    even.sort()
    max_odd = odd[-1]
    cnt = len(even)
    for i in even:
        if i > max_odd:
            cnt += 1
            break
        else:
            max_odd += i
            
    return cnt

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(n,l))

    
