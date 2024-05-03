#問題 https://atcoder.jp/contests/abc350/tasks/abc350_c

N = int(input())
A = [int(x) for x in input().split()]
number_of_times = 0
result = []
while True:  #ソートが完了するまでループ

    for i in range(len(A)-1):  #バブルソート
        x = i+1
        if A[i] > A[i+1]:
            result.append([A[x], A[i]])
            A[i], A[x] = A[x], A[i]
            number_of_times += 1
    
    j = 1
    x = 0
    for x in range(len(A)-1):  #ソートされているか確認
        if A[x] < A[x+1]:
            j += 1
    if j == len(A):  #ソートされていたらループから抜ける
        break


print(number_of_times)
for a, b in result:
    print(a, b)