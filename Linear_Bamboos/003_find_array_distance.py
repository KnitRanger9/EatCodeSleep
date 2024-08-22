#Leetcode 1385. Find distance between two arrays
if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    d = int(input())
    answer = 0
    for i in arr1:
        count = True
        for j in arr2:
            if i - j >= d:
                count = False
        if count == True: answer+=1
    print(answer)
