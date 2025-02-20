# job-scheduling-algorithms

This project was developed as part of the **Principles of Industrial Engineering (ME207)** course at **IIT Indore**.

This Python program evaluates various job sequencing methods for a single machine to determine the best method based on multiple performance metrics. The methods analyzed include:
- **FCFS (First-Come-First-Serve)**
- **SPT (Shortest Processing Time)**
- **EDD (Earliest Due Date)**
- **LPT (Longest Processing Time)**
- **SSL (Smallest Slack)**
- **SCR (Smallest Criticality Ratio)**
- **User-Specified Sequence**

The program generates random processing times and due dates based on six predefined cases. It then calculates the following metrics for each method:
- **Utilization**: Measures machine efficiency.
- **Average Lateness**: Measures how late jobs are completed.
- **Average Flow Time**: Measures the average time jobs spend in the system.
- **Average Number of Jobs in the System**: Calculates the average number of jobs being processed or waiting.

The method that performs best for each metric is displayed as output.
## Cases for Processing Times and Due Dates

The program evaluates six different cases for generating random processing times and due dates:

1. **Case 1**:
   - Processing Time: Random numbers between **2 and 10**.
   - Due Dates: Random numbers between **30%** and **90%** of the total processing time.

2. **Case 2**:
   - Processing Time: Random numbers between **2 and 10**.
   - Due Dates: Random numbers between **50%** and **110%** of the total processing time.

3. **Case 3**:
   - Processing Time: Random numbers between **2 and 50**.
   - Due Dates: Random numbers between **30%** and **90%** of the total processing time.

4. **Case 4**:
   - Processing Time: Random numbers between **2 and 50**.
   - Due Dates: Random numbers between **50%** and **110%** of the total processing time.

5. **Case 5**:
   - Processing Time: Random numbers between **2 and 100**.
   - Due Dates: Random numbers between **30%** and **90%** of the total processing time.

6. **Case 6**:
   - Processing Time: Random numbers between **2 and 100**.
   - Due Dates: Random numbers between **50%** and **110%** of the total processing time.

Each case allows for varied scenarios to test the effectiveness of different sequencing methods under diverse conditions.

## How to Use
1. Run the program and input:
   - Number of jobs (`n`).
   - Number of simulations (`m`).
   - A user-specified sequence of jobs (optional).
   - The case number (1–6) for processing times and due dates.
2. The program will output the best-performing method for each metric.
