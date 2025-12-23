#Space Optimization

def BStr(n):
    dp0=[0]*2
    dp1=[0]*2
    
    dp0[1] = 1
    dp1[1] = 1

    for i in range(2, n+1):
        dp0[i%2] = dp0[(i%2)-1]+dp1[(i%2)-1]
        dp1[i%2] = dp0[(i%2)-1]
    return dp0[n%2] + dp1[n%2]
print(BStr(4))