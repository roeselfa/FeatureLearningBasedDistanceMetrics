import AdvancedBA as ba
import matplotlib.pylab as plt
import seaborn as sns
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.util import constants

plt.rcParams.update({'font.size': 26})

caseIDKey = "Case ID"
activityKey = "Activity"

basePath = sys.argv[1]  # Path to the directory where all the event logs are located
savePath = sys.argv[2]  # Where to save the graphic

logNames = ['', '', '']  # the logs that should be compared in regards to Advanced BA (e.g. ["ApplicationProcess", "SepsisCases", "TravelClaims"])
modes = ['', '']  # the different PRETSA instances (e.g. {"Levenshtein", "FDM"])

kRange = [2, 4, 8, 16, 32, 64, 128, 256]  # range for privacy parameter k
tRange = [0.1, 0.25, 0.5, 0.75, 1]  # range for privacy parameter t

separator = ";"  # some .csv are separated by ";", some by ","


def main():
    matrices = list()
    for logName in logNames:

        originalLogPath = basePath + logName + '/' + logName + '.csv'
        originalFrame = csv_import_adapter.import_dataframe_from_path(originalLogPath, sep=separator)

        originalLog = conversion_factory.apply(originalFrame,
                                               parameters={constants.PARAMETER_CONSTANT_CASEID_KEY: caseIDKey,
                                                           constants.PARAMETER_CONSTANT_ACTIVITY_KEY: activityKey})

        originalTraces = getTracesFromLog(originalLog)
        uniqueEventList = getEventList(originalTraces)

        originalFollowsRelations = ba.getFollowsRelations(allEvents=uniqueEventList, traces=originalTraces)
        originalPrecedesRelations = ba.getPrecedesRelations(allEvents=uniqueEventList, traces=originalTraces)

        for m in modes:
            matrix = list()
            for t in tRange:
                column = list()
                for k in kRange:
                    sanitizedLogPath = basePath + logName + '/' + logName + '_t' + str(t) + '_k' + str(k) + '_' + m + '.csv'
                    sanitizedFrame = csv_import_adapter.import_dataframe_from_path(sanitizedLogPath, sep=";")  # PRETSA sanitized logs always use ';'

                    sanitizedLog = conversion_factory.apply(sanitizedFrame,
                                                            parameters={
                                                                constants.PARAMETER_CONSTANT_CASEID_KEY: caseIDKey,
                                                                constants.PARAMETER_CONSTANT_ACTIVITY_KEY: activityKey})

                    sanitizedTraces = getTracesFromLog(sanitizedLog)

                    sanitizedFollowsRelations = ba.getFollowsRelations(allEvents=uniqueEventList,
                                                                       traces=sanitizedTraces)
                    sanitizedPrecedesRelations = ba.getPrecedesRelations(allEvents=uniqueEventList,
                                                                         traces=sanitizedTraces)

                    baScore = ba.getBehavioralAppropriatenessScore(originalFollows=originalFollowsRelations,
                                                                   originalPrecedes=originalPrecedesRelations,
                                                                   sanitizedFollows=sanitizedFollowsRelations,
                                                                   sanitizedPrecedes=sanitizedPrecedesRelations,
                                                                   events=uniqueEventList)
                    print("Done with", logName, m, k, t, ':', baScore)
                    column.append(baScore)
                matrix.append(column)

            title = logName + ' (' + m + ')'
            matrices.append((title, matrix))

    fig, ax = plt.subplots(len(logNames), len(modes), figsize=(6 * len(modes), 4 * len(logNames)), sharey=True,
                           sharex=True)

    for i in range(len(matrices)):
        k = int(i / 2)
        j = i % 2
        name = matrices[i][0]
        matrix = matrices[i][1]

        xLabels = kRange
        yLabels = tRange

        im_normal = sns.heatmap(matrix, ax=ax[k][j], vmin=0, vmax=1, cmap="Greens", cbar=False)
        ax[k][j].set_yticklabels(yLabels, rotation=0)

        ax[k][j].set_title(name)
        ax[k][0].set_ylabel('t')

    ax[-1][-1].set_xlabel('k')
    ax[-1][-2].set_xlabel('k')
    ax[-1][-1].set_xticklabels(xLabels, rotation=30)
    ax[-1][-2].set_xticklabels(xLabels, rotation=30)
    mappable_normal = im_normal.get_children()[0]
    fig.subplots_adjust(bottom=-0.01)
    plt.colorbar(mappable_normal, ax=ax[:], orientation='horizontal', cmap="Greens", pad=0.102)
    plt.savefig(savePath + '.png', dpi=92, bbox_inches='tight')


def getTracesFromLog(log):
    resultLog = list()
    for trace in log:
        exportLog = list()
        for event in trace:
            exportLog.append(event[activityKey])
        resultLog.append(exportLog)

    return resultLog


def getEventList(traceSet):
    events = list()
    for t in traceSet:
        for e in t:
            if e not in events:
                events.append(e)

    return events


def getDiffMatrix(m1, m2):
    diffMatrix = list()

    for i in range(len(m1)):
        row1 = m1[i]
        row2 = m2[i]
        diffRow = list()
        if len(row1) != len(row2):
            raise ValueError("Rows should have same length!")
        for j in range(len(row1)):
            diffRow.append(row1[j] - row2[j])

        diffMatrix.append(diffRow)

    return diffMatrix


main()
print("Done")
