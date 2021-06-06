# Feature Learning-based Distance Metrics for Privacy-preserving Process Mining

This is the program code for the workshop paper "A Distance Metric for Privacy-preserving Process Mining based on Feature Learning".

This repository contains the Python-based source code and the evaluation files for the definition and evaluation of a feature learning-based trace distance metric, as presented in the paper "A distance metric for Privacy-preserving Process Mining based on Feature Learning". 
The metric builds upon the [Process Sanitization algorithm PRETSA](https://github.com/samadeusfp/PRETSA).

## Installation

Clone the repository and you're ready to go.

## Usage

```python
runPRETSA_FLDM
```
applies the [PRETSA algorithm](https://github.com/samadeusfp/PRETSA) using Feature Learning-based Distance Metrics.\
Input:
1) path to the event log to be sanitized (.csv) (used by PRETSA)*
2) path to the event log to be sanitized (.xes) (used to train the word embeddings)
3) k (int)
4) t (float)

Output:\
sanitized event log

*must contain 'duration' attribute which can be added using [add_annotation_duration.py](https://github.com/samadeusfp/PRETSA/blob/master/add_annotation_duration.py)

Event Logs are mostly available as .xes and can easily be converted to .csv i.e. using the [ProcessMining4Python library](https://pm4py.fit.fraunhofer.de/)


## Evaluation Results

The scripts used for the creation of the figures used throughout the paper can be found in the directory "Evaluation"

```python
advancedBehavioralAppropriateness.py
```
calculates the Advanced Behavioral Appropriateness Score for a given event log in relation to the other given event log.\
Input:
1) path to the first event log (original log) (.csv)
2) path to the second event log (sanitized log) (.csv)

Output: Score s; 0 <= s <= 1

```python
totalDurationError.py
```
calculates the Total Duration Error for a given event log in relation to the other given event log.\
Input:
1) path to the first event log (original log) (.csv)
2) path to the second event log (sanitized log) (.csv)

Output: Error e; 0 <= e <= 100

```python
check_sample_quality.py
```
among other scores, calculates the Truly Sampled Score for a given event log in relation to the other given event log.\
Input:
1) path to the first event log (original log) (.csv)
2) path to the second event log (sanitized log) (.csv)

Output: Truly Sampled Score s; 0 <= s <= 1\
For an explanation of the score, please refer to 

"Measuring the Behavioral Quality of Log Sampling",\
Bram Knols and Jan Martijn E. M. van der WerfDepartment of Information and Computing Sciences   Utrecht University

## Contact
fabian.roesel@hu-berlin.de

### License
We provide our code under the MIT license.
