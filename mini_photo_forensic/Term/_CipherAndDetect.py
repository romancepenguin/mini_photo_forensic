import random

def randomKey(LETTERS):
    key = random.randint(1, len(LETTERS))
    return key

def randomKeyAffine(length):
    key = random.randint(0,length)
    return key

def detectTime(timeMsg):
    cnt=0
    if timeMsg[0].isdigit():
        cnt += 1
    if timeMsg[1].isdigit():
        cnt += 1
    if timeMsg[2].isdigit():
        cnt += 1
    if timeMsg[3].isdigit():
        cnt += 1
    if timeMsg[4]==":":
        cnt += 1
    if timeMsg[7] == ":":
        cnt += 1
    if timeMsg[13] == ":":
        cnt += 1
    if timeMsg[16] == ":":
        cnt += 1

    if cnt==8:
        return True
    else:
        return False