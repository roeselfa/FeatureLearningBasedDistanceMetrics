import gensim
from scipy import spatial
import logging

eventName = 'concept:name'

def calculateEventDistanceMatrix(eventVector, trainingModel):
    distanceMatrix = {}
    for i in range(len(eventVector)):
        e1 = eventVector[i]
        for j in range(len(eventVector)):
            e2 = eventVector[j]
            if i == j:
                similarity = 1
            else:
                similarity = 1 - spatial.distance.cosine(trainingModel[e1], trainingModel[e2])

            distanceMatrix[(e1, e2)] = 1 - similarity

    return distanceMatrix


def extractActivitiesFromLog(log):
    resultLog = list()

    for trace in log:
        eventLog = list()
        for event in trace:
            eventLog.append(event[eventName])
        resultLog.append(eventLog)

    return resultLog


def trainModel(rawLog):
    sentences = extractActivitiesFromLog(rawLog)
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # train the model 1000 times on the data from the log
    print("Training the model on 10000 iterations...")
    model = gensim.models.Word2Vec(sentences, min_count=1, iter=1000)
    events = model.wv.index2entity
    eventDistanceMatrix = calculateEventDistanceMatrix(events, model)
    return model, eventDistanceMatrix
