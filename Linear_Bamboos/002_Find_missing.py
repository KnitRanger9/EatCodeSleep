# -*- coding: utf-8 -*-
if __name__=="__main__":
    arr=list(map(int, input().split()))
    x=0
    for i in arr:
        x+=i
    sum_n=((len(arr)+1)*(len(arr)+2))//2
    print(f"The missing number is: {sum_n - x}")
