import time
def solution(l):
    ll=len(l)
    arr=[0]*ll
    cnt=0
    for i in range(ll):
        for j in range(i+1,ll):
            if l[j]%l[i]==0:
                arr[j]+=1
                cnt+=arr[i]

    return cnt

x=[y for y in range(1,2001)]
start_time=time.time()
print(solution(x),'Elapsed time:',time.time()-start_time)
