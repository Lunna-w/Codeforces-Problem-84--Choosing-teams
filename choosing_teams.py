n, k = list(map(int, input().split()))

ratings = list(map(int, input().split()))  

eligible_participants = 0  

for rating in ratings:
    
    if rating <= 5-k:
        eligible_participants += 1


teams = eligible_participants // 3

print(teams)