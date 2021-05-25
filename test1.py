from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0

for x in c:
    ans += c[x] // 2
if map in range int(input):
    print(ans)
else:
    print("The number in {} does not match the number of {}" .format(c, n))