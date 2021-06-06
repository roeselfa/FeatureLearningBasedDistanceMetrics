from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.util import constants


def getPredecessorsOfEventInTrace(event, trace):
    predecessors = list()
    if event not in trace:
        return predecessors

    eventIndex = max(loc for loc, val in enumerate(trace) if val == event)
    restTrace = trace[:eventIndex]

    for e in restTrace:
        if e not in predecessors:
            predecessors.append(e)

    return predecessors


def getFollowersOfEventInTrace(event, trace):
    followers = list()
    if event not in trace:
        return followers
    eventIndex = trace.index(event)
    restTrace = trace[eventIndex + 1:]

    for e in restTrace:
        if e not in followers:
            followers.append(e)

    return followers


def getFollowsRelations(allEvents, traces):
    followsMatrix = {}

    for event in allEvents:
        alwaysFollows = allEvents.copy()
        neverFollows = allEvents.copy()

        for eClmn in allEvents:
            followsMatrix[(event, eClmn)] = 'S'

        for trace in traces:
            if event in trace:
                followers = getFollowersOfEventInTrace(event, trace)
                for f in followers:
                    if f in neverFollows:
                        neverFollows.remove(f)

                for e in allEvents:
                    if e not in followers:
                        if e in alwaysFollows:
                            alwaysFollows.remove(e)

        for a in alwaysFollows:
            followsMatrix[(event, a)] = 'A'

        for n in neverFollows:
            followsMatrix[(event, n)] = 'N'

    return followsMatrix


def getPrecedesRelations(allEvents, traces):
    precedesMatrix = {}

    for event in allEvents:
        alwaysPrecedes = allEvents.copy()
        neverPrecedes = allEvents.copy()

        for eClmn in allEvents:
            precedesMatrix[(event, eClmn)] = 'S'

        for trace in traces:
            if event in trace:
                predecessors = getPredecessorsOfEventInTrace(event, trace)
                for p in predecessors:
                    if p in neverPrecedes:
                        neverPrecedes.remove(p)

                for e in allEvents:
                    if e not in predecessors:
                        if e in alwaysPrecedes:
                            alwaysPrecedes.remove(e)

        for a in alwaysPrecedes:
            precedesMatrix[(event, a)] = 'A'

        for n in neverPrecedes:
            precedesMatrix[(event, n)] = 'N'

    return precedesMatrix


def getIntersectionSize(set1, set2, events):
    counter = 0
    for e1 in events:
        for e2 in events:
            if set1[(e1, e2)] == set2[(e1, e2)]:
                counter += 1
    return counter


def getBehavioralAppropriatenessScore(originalFollows, originalPrecedes, sanitizedFollows, sanitizedPrecedes,
                                      events):
    followsIntersectSize = getIntersectionSize(originalFollows, sanitizedFollows, events)
    precedesIntersectSize = getIntersectionSize(originalPrecedes, sanitizedPrecedes, events)
    followsSize = len(sanitizedFollows)
    precedesSize = len(sanitizedPrecedes)
    score = (followsIntersectSize / (2 * followsSize)) + (precedesIntersectSize / (2 * precedesSize))
    return score


caseIDKey = "Case ID"
activityKey = "Activity"
durationKey = "Complete Timestamp"

