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
callAdvancedBA.py
```
calculates and displays the Advanced Behavioral Appropriateness Score for a given set of event logs.\
Input:
1) path to the directory where the event logs are located (.csv) *
2) path to the directory to save the output graphic in

Output: 
A graphic, similar to the ones displayed in the paper. Be advised that spacings and paddings are optimised for comparison of 2 modes for 3 event logs. Should you wish to change this setup you might have to adjust accordingly.

```python
callCheckSampleQuality.py
```
calculates and displays the Truly Sampled Score for a given set of event logs.\
Input:
1) path to the directory where the event logs are located (.csv) *
2) path to the directory to save the output graphic in

Output: 
A graphic, similar to the ones displayed in the paper. Be advised that spacings and paddings are optimised for comparison of 2 modes for 3 event logs. Should you wish to change this setup you might have to adjust accordingly.

For an explanation of the score, please refer to 

"Measuring the Behavioral Quality of Log Sampling",\
Bram Knols and Jan Martijn E. M. van der WerfDepartment of Information and Computing Sciences   Utrecht University


```python
traceDurationError.py
```
calculates and displays the Total Duration Error for a given set of event logs.\
Input:
1) path to the directory where the event logs are located (.csv) *
2) path to the directory to save the output graphic in

Output: 
A graphic, similar to the ones displayed in the paper. Be advised that spacings and paddings are optimised for comparison of 2 modes for 3 event logs. Should you wish to change this setup you might have to adjust accordingly.


* We recommed the following file structure, otherwise you will have to adjust the Evaluation code to fit your setup

~\EventLogs\\

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logName1\\

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName1.csv"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the unsanitized event log

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     "logName1_t[xx]\_k[xx]_[mode].csv"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the sanitized event logs


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName1_t[xx]\_k[xx]_[mode].csv"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName1_t[xx]\_k[xx]_[mode].csv"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logName2\\

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName2.csv"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the unsanitized event log

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     "logName2_t[xx]\_k[xx]_[mode].csv"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the sanitized event logs


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName2_t[xx]\_k[xx]_[mode].csv"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logName2_t[xx]\_k[xx]_[mode].csv"

<br/>
            
[mode] is the PRETSA instance used to sanitize the log, e.g. "Levenshtein", or "FDM"
## Contact
fabian.roesel@hu-berlin.de

### License
We provide our code under the MIT license.
