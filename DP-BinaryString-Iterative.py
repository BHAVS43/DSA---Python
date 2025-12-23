def BStr(n):
    dp0=[0]*(n+1)
    dp1=[0]*(n+1)
    
    dp0[1] = 1
    dp1[1] = 1
    for i in range(2, n+1):
        dp0[i] = dp0[i-1]+dp1[i-1]
        dp1[i] = dp0[i-1]
    return dp0[n] + dp1[n]
print(BStr(4))