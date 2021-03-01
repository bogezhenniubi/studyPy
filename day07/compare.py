def max(myList):
    m1, m2 = (myList[0], myList[1]) if myList[0] > myList[1] else (myList[1], myList[0])
    for x in range(2, len(myList)):
        if myList[x] > m1:
            m2 = m1
            m1 = myList[x]
        elif myList[x] > m2:
            m2 = myList[x]
    return m1, m2