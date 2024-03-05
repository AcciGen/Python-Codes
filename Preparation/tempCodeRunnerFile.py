at", "bat", "cock", "cow", "pig", "fox", "ant", "bird",
           "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]

s = list(input().lower())
ans_cnt = 0
ans = []

for animal in animals:

    rs = s.copy()
    
    check = True
    while check:

        count = 0
        for char in animal:
            if char in rs:
                count += 1
                rs.remove(char)
            else:
                check = False

        if count == len(animal):
            if animal not in ans:
                ans.append(animal)
            ans_cnt += 1

        if not rs:
            check = False            

print(ans_cnt, *ans)