# Assignment Solution
# Through this code we are trying to analyse and find out which method among FCFS, SPT, EDD, LPT, SSL, SCR, and a Usr specified method is
# best for sequencing of jobs considering different factors such as Utilisation, Average Lateness, Average Flow time and Average No. of 
# jobs in the system. The code generates Processing time and Due date values according to the constraint given in the question. It then 
# calculates the four factors for each condition of the processing time and due date. We observe which method gives the best value for 
# the considered factor and that method is shown as output.
# The code can be run for more than one simulation for accuracy.

from numpy import *
import random

# For User input
n = int(input("Number of jobs you want: "))
m = int(input("Number of Simulations you want: "))
user_specified = array([int(x) for x in input("Enter Sequence of jobs you want to check (Eg.:- for 5 jobs: 1 3 5 2 4): ").split()])
x = int(input("Which Case do you want to check for? : "))
# Test case if user commits a mistake while entering sequence rules
if size(user_specified)!=n:
    print("You have made a mistake while specifying sequencing rule")
else:
    user_specified_indices = user_specified-1
    # Creating an empty (All values set to 0) to store Utilization values for all given simulations
    UTI = zeros((m), dtype=int)
    Avg_FT = zeros((m), dtype=int)
    Avg_LT = zeros((m), dtype=int)
    Avg_noj = zeros((m), dtype=int)
    # A variable to navigate and store values into UTI array
    count=0

    # Function which take arrays as input and Outputs the 1st set of operation for a given method and gives a row as output 
    def operation(PT,DD):
        # Calculating Flowtime Array
        ft = zeros(n) #initializing array to be filled
        ft[0]=PT[0] 
        for i in range(n-1):
            ft[i+1] =ft[i] + PT[i+1]
        # Calculating Lateness Array
        lt=zeros(n) #initializing array to be filled
        for i in range(n):
            if (DD[i]-ft[i])<0:
                lt[i]=abs(DD[i]-ft[i])
            else:
                lt[i]=0
        # Calculating required parameters
        avg_ft=round((sum(ft) / n),2)
        avg_lt=round((sum(lt)/n),2)
        uti = round((sum(PT)/sum(ft)),4)
        av_no_jobs = round(((1/uti)),2)
        # Order of Row created for a method is : Average flow time | Average late time | Utilization | Average number of jobs
        ans = array([avg_ft,avg_lt,uti,av_no_jobs])
        return ans

    # Function to calculate slack (Created because it isn't needed in the table created by operation function but if defined here can be accessed through here)
    def slack(PT,DD):
        slack = zeros(n) #initializing array to be filled
        for i in range(n):
            slack[i]=abs(PT[i]-DD[i])
        return slack

    # Function to calculate Criticality Ratio
    def cra(PT,DD):
        cr= zeros(n) #initializing array to be filled
        for i in range(n):
            cr[i]=round((DD[i]/PT[i]),3)
        return cr

    # Creating a function so that we can control when to print an answer table and when not
    def printing_ans(ANS):
        print(ANS)
        print() #There for indentation purposes


    # Function that does Operations for all different methods mentioned. It generates final table comparing values from different methods for same PT and DD.
    def ans(PT,DD,user_specified_indices):
        # does operations for FCFS Method
        fcfs=operation(PT,DD)
        # does operations for EDD Method
        edd_indices = argsort(DD)  #For arranging as required by EDD Method
        edd_PT = PT[edd_indices]
        edd_DD = DD[edd_indices]
        edd=operation(edd_PT,edd_DD)
        # does operations for SPT Method
        spt_indices = argsort(PT)  #For arranging as required by SPT Method
        spt_PT = PT[spt_indices]
        spt_DD = DD[spt_indices]
        spt=operation(spt_PT,spt_DD)
        # does operations for User Specified Method
        us_sp_PT = PT[user_specified_indices] #For arranging as required by User Specified Method
        us_sp_DD = DD[user_specified_indices]
        user=operation(us_sp_PT,us_sp_DD)
        # does operations for LPT Method
        lpt_indices = argsort(PT)[::-1]  #For arranging as required by LPT Method
        lpt_PT = PT[lpt_indices]
        lpt_DD = DD[lpt_indices]
        lpt=operation(lpt_PT,lpt_DD)
        # does operations for SSL Method
        sl=slack(PT,DD)
        sl_indices = argsort(sl)  #For arranging as required by SSL Method
        sl_PT = PT[sl_indices]
        sl_DD = DD[sl_indices]
        ssl=operation(sl_PT,sl_DD)
        # does operations for SCR Method
        cr=cra(PT,DD)
        cr_indices = argsort(cr) #For arranging as required by SCR Method
        cr_PT = PT[cr_indices]
        cr_DD = DD[cr_indices]
        scr=operation(cr_PT,cr_DD)
        # creating raw table 
        AN = vstack([fcfs,edd,spt,lpt,ssl,scr,user])
        # Updating values into global variables
        global count
        global UTI
        global Avg_FT
        global Avg_LT
        global Avg_noj
        max_row_index = argmax(AN[:, 2])
        UTI[count] = int(max_row_index+1)
        max_row_index = argmin(AN[:, 0])
        Avg_FT[count] = int(max_row_index+1)
        max_row_index = argmin(AN[:, 1])
        Avg_LT[count] = int(max_row_index+1)
        max_row_index = argmin(AN[:, 3])
        Avg_noj[count] = int(max_row_index+1)
        count=count+1
        # To make table look readable
        firstcolumn=array([["FCFS"],["EDD"],["SPT"],["LPT"],["SSL"],["SCR"],["User Specified"]])
        firstrow=array(["Method","Avg FT","Avg LT","Uti","Avg No of Jobs"])
        AN2=hstack([firstcolumn,AN])
        ANS= vstack([firstrow,AN2]) #Created a readable final answer table which cam be printed using printing_ans() function
        # printing_ans(ANS) #To get whole final answer use printing_ans() function here

    # Function checking which through all utilization values we got,which methods has greatest utilization for maximum number of times
    def checking_method_with_best_utilization(UTI):
        # Using if-else to print out Method name
        most_frequent_value1 = bincount(UTI).argmax()
        print("Best Utilization Method: ", end="")
        if most_frequent_value1 == 1:
            print('FCFS')
        elif most_frequent_value1 == 2:
            print('EDD')
        elif most_frequent_value1 == 3:
            print('SPT')
        elif most_frequent_value1 == 4:
            print('LPT')
        elif most_frequent_value1 == 5:
            print('SSL')
        elif most_frequent_value1 == 6:
            print('SCR')
        elif most_frequent_value1 == 7:
            print('User Specified')
    
    # Function checking which through all Average lateness values we got,which methods has smallest average lateness for maximum number of times       
    def checking_method_with_best_AVG_Lateness(Avg_LT):
        # Using if-else to print out Method name
        most_frequent_value2 = bincount(Avg_LT).argmax()
        print("Least Avg Lateness method: ", end="")
        if most_frequent_value2 == 1:
            print('FCFS')
        elif most_frequent_value2 == 2:
            print('EDD')
        elif most_frequent_value2 == 3:
            print('SPT')
        elif most_frequent_value2 == 4:
            print('LPT')
        elif most_frequent_value2 == 5:
            print('SSL')
        elif most_frequent_value2 == 6:
            print('SCR')
        elif most_frequent_value2 == 7:
            print('User Specified')    
    
    # Function checking which through all Average flow time values we got,which methods has smallest average flow time for maximum number of times       
    def checking_method_with_best_AVG_Flow_Time(Avg_LT):
        # Using if-else to print out Method name
        most_frequent_value3 = bincount(Avg_FT).argmax()
        print("Least Avg Flow Time method: ", end="")
        if most_frequent_value3 == 1:
            print('FCFS')
        elif most_frequent_value3 == 2:
            print('EDD')
        elif most_frequent_value3 == 3:
            print('SPT')
        elif most_frequent_value3 == 4:
            print('LPT')
        elif most_frequent_value3 == 5:
            print('SSL')
        elif most_frequent_value3 == 6:
            print('SCR')
        elif most_frequent_value3 == 7:
            print('User Specified')
    
    # Function checking which through all Average No. of Jobs values we got,which methods has smallest average No. of jobs for maximum number of times       
    def checking_method_with_best_AVG_NO_of_Jobs(Avg_noj):
        # Using if-else to print out Method name
        most_frequent_value4 = bincount(Avg_noj).argmax()
        print("Least Avg No. of jobs method: ", end="")
        if most_frequent_value4 == 1:
            print('FCFS')
        elif most_frequent_value4 == 2:
            print('EDD')
        elif most_frequent_value4 == 3:
            print('SPT')
        elif most_frequent_value4 == 4:
            print('LPT')
        elif most_frequent_value4 == 5:
            print('SSL')
        elif most_frequent_value4 == 6:
            print('SCR')
        elif most_frequent_value4 == 7:
            print('User Specified')

    # Creating a function to Execute for different cases
    def applying_cases(m,n,a,b,c,d,user_specified_indices):  
        for i in range(m):      
            pt1=zeros(n) #initializing array to be filled
            for i in range(n):
                pt1[i]=random.randint(a, b)
            e=sum(pt1)
            dd = zeros(n) #initializing array to be filled
            for i in range(n):
                dd[i]=random.uniform(e*c, e*d)
            ans(pt1,dd,user_specified_indices)
        
        print()
        checking_method_with_best_utilization(UTI)
        checking_method_with_best_AVG_Lateness(Avg_LT)
        checking_method_with_best_AVG_Flow_Time(Avg_LT)
        checking_method_with_best_AVG_NO_of_Jobs(Avg_noj)
    # Using if-else ladder to select one among all available choices
    if x==1:
        a=2
        b=10
        c=0.3
        d=0.9
        applying_cases(m,n,a,b,c,d,user_specified_indices)
    elif x==2:
        a=2
        b=10
        c=0.5
        d=1.1
        applying_cases(m,n,a,b,c,d,user_specified_indices)
    elif x==3:
        a=2
        b=50
        c=0.3
        d=0.9
        applying_cases(m,n,a,b,c,d,user_specified_indices)
    elif x==4:
        a=2
        b=50
        c=0.5
        d=1.1
        applying_cases(m,n,a,b,c,d,user_specified_indices)
    elif x==5:
        a=2
        b=100
        c=0.3
        d=0.9
        applying_cases(m,n,a,b,c,d,user_specified_indices)
    elif x==6:
        a=2
        b=100
        c=0.5
        d=1.1
        applying_cases(m,n,a,b,c,d,user_specified_indices)
