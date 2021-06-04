# Feature Learning-based Distance Metrics for Privacy-preserving Process Mining

This is the program code for the Bachelor's thesis "Feature Learning-based Distance Metrics for Privacy-preserving Process Mining".


## Usage

```python
runPRETSA_FLDM
```
applies the PRETSA algorithm (see https://github.com/samadeusfp/PRETSA) using Feature Learning-based Distance Metrics.\
Input:
1) path to the event log to be sanitized (.csv) (used by PRETSA)*
2) path to the event log to be sanitized (.xes) (used to train the word embeddings)
3) k (int)
4) t (float)

Output:\
sanitized event log

*must contain 'duration' attribute which can be added using add_annotation_duration.py (see https://github.com/samadeusfp/PRETSA)

Event Logs are mostly available as .xes and can easily be converted to .csv i.e. using the ProcessMining4Python library (see https://pm4py.fit.fraunhofer.de/)

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
Bram Knols and Jan Martijn E. M. van der WerfDepartment of Information and Computing SciencesUtrecht University