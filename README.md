# Python-Challenge

This repository contains two Python scripts, PyBank and PyPoll, that analyze financial and poll data, respectively. Each script reads a CSV file, performs the analysis, and prints the results to the terminal and to a text file.

## Pybank

Workfile: ./PyBank/main.py

csvfile: ./PyBank/Resources/budget_data.csv

txtfile: ./PyBank/analysis/results.txt

Pybank is distinct in that we split both columns and to do a lot of computations with the second column. The challenge was found in the finding of the average of the changes but I derived an easy formula to compute for that. If you see in my code this specific line is what computed my average:

```{python}
average = (int(budgetlist[(period-1)][1]) - int(budgetlist[0][1]))/(period-1)
```

Really proud of this line.


## PyPoll

Workfile: ./PyPoll/main.py
csvfile: ./PyPoll/Resources/election_data.csv
txtfile: ./PyPoll/analysis/results.txt

PyPoll is a very interesting assignment. It had a lot of rows, and it is not sorted per candidate. Had to use unique(), count() and learned how print with '\n'. Taking percentage to show using round() also became useful and printing to text file just became simpler. 


## Author
Juliano Miguel Lacson

---
