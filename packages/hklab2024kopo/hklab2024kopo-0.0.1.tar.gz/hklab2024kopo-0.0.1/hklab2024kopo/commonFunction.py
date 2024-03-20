def trimmedMeanHk(inList):
    """
        description: calculate average value (except min, max Value)
        parameters:
        inList -> list : value shall be number
    """
    #inList = [1,1,1,1,10,10,10,100,100,100]

    maxValue = max(inList)
    minValue = min(inList)

    maxValueCnt = inList.count(maxValue);
    minValueCnt = inList.count(minValue);

    maxMom = sum(inList) - (minValue * minValueCnt) -(maxValue * maxValueCnt)
    maxSon = len(inList) - minValueCnt - maxValueCnt

    answer = (int)(maxMom/maxSon)
    return answer


def trimmedMeanHk5555(inList):
    """
        description: calculate average value (except min, max Value)
        parameters:
        inList -> list : value shall be number
    """
    #inList = [1,1,1,1,10,10,10,100,100,100]

    maxValue = max(inList)
    minValue = min(inList)

    maxValueCnt = inList.count(maxValue);
    minValueCnt = inList.count(minValue);

    maxMom = sum(inList) - (minValue * minValueCnt) -(maxValue * maxValueCnt)
    maxSon = len(inList) - minValueCnt - maxValueCnt

    answer = (int)(maxMom/maxSon)
    return answer