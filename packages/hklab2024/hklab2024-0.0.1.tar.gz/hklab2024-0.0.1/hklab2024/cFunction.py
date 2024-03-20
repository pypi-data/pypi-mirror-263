def trimmedMean(inList):
    """
    function: calculate mean ...
    
    """

    # inList = [1,1,1,1,10,10,10,10,100,100,100,100]
    
    minValue = min(inList)
    
    maxValue = max(inList)
    
    minValueCount = inList.count(minValue)
    maxValueCount = inList.count(maxValue)
    
    totalSum = sum(inList) - (minValue*minValueCount) - (maxValue*maxValueCount)
    
    totalCount = len(inList) - minValueCount - maxValueCount
    
    result = totalSum / totalCount

    return result