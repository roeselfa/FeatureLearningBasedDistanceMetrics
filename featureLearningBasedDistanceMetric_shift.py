delimter = "@"

def length(s):
   return s.count(delimter)

def enumerateSequence(s):
    list = s.split(delimter)
    return enumerate(list[1:], 0)

# call with lenDiffPenalty = 2 per default
def traceDistance_shift(t1, t2, eventDistanceMatrix, lenDiffPenalty):
    if length(t1) < length(t2):
        return traceDistance_shift(t2, t1, eventDistanceMatrix, lenDiffPenalty=3)

    if length(t2) == 0:
        return length(t1) * lenDiffPenalty

    previous_row = [0] * (length(t2) + 1)
    for i, c1 in enumerateSequence(t1):
        current_row = [(i+1)*lenDiffPenalty]
        for j, c2 in enumerateSequence(t2):
            insertions = previous_row[j + 1] + lenDiffPenalty  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + lenDiffPenalty  # than t2
            substitutions = previous_row[j] + eventDistanceMatrix[(c1, c2)]
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
