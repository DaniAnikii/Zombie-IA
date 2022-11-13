N = int(input())
for moves in range(9999):
    zx = list(map(int, input().split()))
    zy = list(map(int, input().split()))
    x, y = map(int, input().split())
    
    peligro = False
    next_x = x + 1
    next_y = y + 1
    amenaza = 0
    
    if N > 800:
        parametro = 4
    else :
        parametro = 2

    for i in range(N):
        if zx[i] == x + 1 and zy[i] == y:
            amenaza += 1
        if zx[i] == x + 2 and zy[i] == y:
            amenaza += 1
        if zx[i] == x and zy[i] == y + 1:
            amenaza += 1
        if zx[i] == x + 2 and zy[i] == y + 1:
            amenaza += 1
        if zx[i] == x and zy[i] == y + 2:
            amenaza += 1
        if zx[i] == x + 1 and zy[i] == y + 2:
            amenaza += 1
        if zx[i] == x + 2 and zy[i] == y + 2:
            amenaza += 1
        if zx[i] == next_x and zy[i] == next_y:
            peligro = True
            break
    
    if peligro == False and amenaza < parametro:
        print("RD")
    else:
        print("S")

        