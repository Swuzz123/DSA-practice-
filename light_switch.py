def solve(n, k):
    i = 1
    b_keep = 0
    for i in range(len(n)):
        tmp = (n[i]-n[0])/(2*k)
        b = n[i]-n[0]-tmp*2*k
        print(tmp)
        print(b)
        if b > k: 
            return -1
        else:
            b_keep = b
            
    return n[-1] + b_keep

n = int(input("Nhap n: "))
k = int(input("Nhap k: "))
arr = []
for i in range(n):
    val = int(input(""))
    arr.append(val)
    
arr.sort()
print(arr)
print(solve(arr,k))
        