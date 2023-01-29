n = int(input())
friends = input().split()

db = {f: i for i, f in enumerate(friends, start=1)}

friends2 = [db[str(i + 1)] for i in range(n)]

print(" ".join(map(str, friends2)))
