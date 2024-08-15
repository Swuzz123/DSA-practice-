#tim so cau dung 
def find(a):
    n = len(a)
    limit = n/4
    cnt_A = 0
    cnt_B = 0
    cnt_C = 0
    cnt_D = 0
    for i in a:
        if i == 'A': cnt_A += 1
        if i == 'B': cnt_B += 1
        if i == 'C': cnt_C += 1
        if i == 'D': cnt_D += 1
    return min(cnt_A, limit) + min(cnt_B, limit) + min(cnt_C, limit) + min(cnt_D, limit)

test_case = int(input("Test case:"))
i = 1            
while(i <= test_case):
    print(i)
    i += 1
    a = str(input(""))
    print(find(a))
        