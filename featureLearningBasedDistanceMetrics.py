delimter = "@"


def enumerateSequence(s):
    elemList = s.split(delimter)
    return elemList[1:]


def getDistance(t1, t2, eventDistanceMatrix):
    t1 = enumerateSequence(t1)
    t2 = enumerateSequence(t2)
    t1Len = len(t1)
    t2Len = len(t2)
    errSum = 0
    if t1Len == t2Len:
        for i in range(t1Len):
            errSum += eventDistanceMatrix[(t1[i], t2[i])]

    else:
        lenDiff = abs(t1Len - t2Len)
        if t1Len < t2Len:                       # Assumption: t1 always > t2
            t1, t2 = t2, t1
            t1Len, t2Len = t2Len, t1Len
            punishment = 2
        else:
            punishment = 3

        if t2Len == 0:
            return t1Len * punishment

        for i in range(t2Len):
            errSum += eventDistanceMatrix[(t1[i], t2[i])]

        for i in range(lenDiff):                # fixed value distance for all events beyond the shorter trace's length
            errSum += lenDiff * punishment

    return errSum
