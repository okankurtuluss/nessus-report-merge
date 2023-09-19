# nessus-scan-merge
You can combine multiple Nessus reports into a single file.


#Use of:

1-) Download all scans to be merged from Nessus with the .nessus extension.

2-) Collect all .nessus extension files in a single directory.

3-) Then, when you run the tool as follows, a file named "combined_results.nessus" will be created in the same directory.

python3 nessus-merge.py

![merge2](https://github.com/okankurtuluss/nessus-report-merge/assets/33905344/c66881a6-250a-427d-a627-d97557d2d249)

4-) When you import the newly created "combined_results.nessus" file into Nessus, you will see that all scans have been combined.
