def game():
    return 65

score=game()
with open("Hi-score.txt", "r") as f:
    data=f.read()

if data == "":
    hs=0
else:
    hs=int(data)
if score>hs:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))

        print("Game Score: ", score)