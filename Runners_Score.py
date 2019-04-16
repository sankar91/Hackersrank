if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
maxv = max(arr)
l = list(filter(lambda x: x != maxv,arr))
print(max(l))

