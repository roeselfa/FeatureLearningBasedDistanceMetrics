from pm4py.objects.log.importer.xes import factory as xes_importer
import sys
from pretsa_FLDM import PretsaFLDM
from trainModelAndEventDistanceMatrix import trainModel
import pandas as pd

csvPath = sys.argv[1]
xesPath = sys.argv[2]
k = int(sys.argv[3])
t = float(sys.argv[4])

print("Training model. This may take a few moments.\n")
logXES = xes_importer.import_log(xesPath)
model, eventDistanceMatrix = trainModel(logXES)
print("Done.\n")

# import file with duration attribute added to it
sys.setrecursionlimit(3000)
print("Load Event Log")
eventLog = pd.read_csv(csvPath, delimiter=";")
print("Starting experiments")

targetFilePath = csvPath.replace(".csv", "_t%s_k%s_FLDM.csv" % (t, k))
pretsa = PretsaFLDM(eventLog, model, eventDistanceMatrix)                       # create PRETSA object

cutOutCases = pretsa.runPretsa(int(k), float(t))
print("Modified " + str(len(cutOutCases)) + " cases for k=" + str(k))
privateEventLog = pretsa.getPrivatisedEventLog()
privateEventLog.to_csv(targetFilePath, sep=";", index=False)

print("Done.")