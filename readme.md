# Logic and Language

## Dependencies

- Use python 3.10+
- Install the `requirements.txt` using `pip install -r requirements.txt`

## Code

1. Run file `FOL_solver.py` and wait until the file is done. \
  1.1. This file runs the CCG parses on all the sick-nl sentences and then solves only for the Trial cases.\
  1.2. This is currently in windows mode, to change to linux mode open the file and change the line: `mode="windows"` to `mode="linux"`.\
  1.3. To change from the trial dataset to the test dataset, change the line `if dataset != "TRIAL":` to `if dataset != "TEST":`, same applied for TRAIN.
2. check the folder `output\` for all the results. \
2.1. `test_all_read.png` contains all the trial code cases where errors are labeled as neutral. \
2.2. `test_parse_read.png` contains all the trial code where errors are omitted. \
2.3 `solve.py` see below.

## solve.py

The first line always includes the problem number and the true label from the sick-dataset. The next three lines contain information about the FOL strings. \
H is the hypothesis. \
P is the premise. \
S is the solution.

If either the Hypothesis or Premise is an error, the solution is also automatically an `error`. \
If the H or P contains a Lambda, the prover9 `sread_term` error is provided. \
If a FOL string is incorrectly parsed, the prover9 `sread_term` error is provided. 

If the parsing is succesful S will be in the form of one of three cases; \
s:True | False -> Entailment \
s:False | True -> Contradiction \
s:False | False -> Neutral
