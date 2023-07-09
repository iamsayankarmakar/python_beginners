string = "BANANA"
player1 = "Kevin"
player2 = "Stuart"
pl1_score = 0
pl2_score = 0
l1 = list(string)
res = [string[i: j] for i in range(len(string))for j in range(i + 1, len(string) + 1)]
#vowel = ("A",'a',  "E","e", "I","i" "O","o", "U",'u')
print(res)
for i in range(len(res)):
    if res[i].startswith(("A", 'a',  "E", "e", "I", "i" "O", "o", "U", 'u')):
        pl1_score += 1
    else:
        pl2_score += 1
if pl1_score > pl2_score:
    print(player1 + " "+str(pl1_score))
elif pl1_score == pl2_score:
    print("Draw")
else:
    print(player2 + " "+str(pl2_score))

//



