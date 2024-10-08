#O(n^2) time|  O(1) space
# def validStartingCity(distances,fuel,mpg):
#     numberOfCities=len(distances)
#     for startCityIdx in range(numberOfCities):
#         milesRemaining=0
#         for currentCityIdx in range(startCityIdx,startCityIdx+numberOfCities):
#             if milesRemaining<0:
#                 continue
#             currentCityIdx=currentCityIdx%numberOfCities

#             fuelFromCurrentCity=fuel[currentCityIdx]
#             distanceToNextCity=distances[currentCityIdx]
#             milesRemaining+=fuelFromCurrentCity*mpg-distanceToNextCity

#         if milesRemaining>=0:
#             return startCityIdx
#     return -1

#O(n) time|  O(1) space
def validStartingCity(distances,fuel,mpg):
    numberOfCities=len(distances)
    milesRemaing=0
    indexOfStartingCityCandidate=0
    milesRemaingAtStartingCityCandidate=0

    for cityIdx in range(1,numberOfCities):
        distanceFromPreviousCity=distances[cityIdx-1]
        fuelFromPreviousCity=fuel[cityIdx-1]

        milesRemaing+=fuelFromPreviousCity*mpg-distanceFromPreviousCity

        if milesRemaing<milesRemaingAtStartingCityCandidate:
            milesRemaingAtStartingCityCandidate=milesRemaing
            indexOfStartingCityCandidate=cityIdx
    return indexOfStartingCityCandidate