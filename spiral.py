#спираль
a = int(input('Введите число '))
db, dc = 1, 0
b, c = 0, 0
arr = [[None] * a for i in range(a)]
for i in range(1, a * a + 1):
    arr[b][c] = i
    nb, nc = b + db, c + dc
    if 0 <= nb < a and 0 <= nc < a and not arr[nb][nc]:
        b, c = nb, nc
    else:
        db, dc = -dc, db
        b, c = b + db, c + dc
for b in list(zip(*arr)):
    print(*b)
