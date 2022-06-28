def bubble_sort(S):
    n = len(S)
    for i in range(n):
        print(S)
        for j in range(n-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]

S = [50, 30, 40, 10, 20]
print("Sebelum buble sort", S)
bubble_sort(S)
print("setelah bubble sort", S)
