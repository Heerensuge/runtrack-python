def draw_carpet(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j or i == n-j:
                print("X", end="")
            else:
                print("-", end="")
        print()
        
draw_carpet(10)
