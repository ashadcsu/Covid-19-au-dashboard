import sys
import pandas as pd
sys.stdout=open('output.txt','w')
data=[['CSE-141', '3', 'Level 1 - Term 1', 'No', 'A', 'regular'], ['CSE-142', '1.5', 'Level 1 - Term 1', 'No', 'A', 'regular'], ['CSE-100', '0.75', 'Level 1 - Term 1', 'No', 'A', 'regular'], ['EE-181', '3', 'Level 1 - Term 1', 'No', 'B', 'regular'], ['EE-182', '1.5', 'Level 1 - Term 1', 'Yes', 'A+', 'regular'], ['Math-141', '3', 'Level 1 - Term 1', 'No', 'A+', 'regular'], ['Phy-141', '3', 'Level 1 - Term 1', 'No', 'A-', 'regular'], ['Phy-142', '1.5', 'Level 1 - Term 1', 'Yes', 'A', 'regular'], ['Hum-141', '2', 'Level 1 - Term 1', 'No', 'A-', 'regular'], ['CSE-111', '3.0', 'Level 1 - Term 2', 'No', 'A+', 'regular'], ['CSE-121', '3.0', 'Level 1 - Term 2', 'No', 'B-', 'regular'], ['CSE-143', '3.0', 'Level 1 - Term 2', 'No', 'A', 'regular'], ['Math-143', '4.0', 'Level 1 - Term 2', 'No', 'B+', 'regular'], ['Chem-141', '3.0', 'Level 1 - Term 2', 'No', 'A', 'regular'], ['CSE-122', '1.5', 'Level 1 - Term 2', 'Yes', 'A', 'regular'], ['CSE-144', '1.5', 'Level 1 - Term 2', 'Yes', 'A+', 'regular'], ['Chem-142', '0.75', 'Level 1 - Term 2', 'Yes', 'A-', 'regular'], ['Hum-144', '1.5', 'Level 1 - Term 2', 'Yes', 'B-', 'regular'], ['ME-246', '1.5', 'Level 2 - Term 1', 'Yes', 'A-', 'regular'], ['EE-281', '3', 'Level 2 - Term 1', 'No', 'A+', 'regular'], ['EE-282', '0.75', 'Level 2 - Term 1', 'Yes', 'A+', 'regular'], ['CSE-241', '3', 'Level 2 - Term 1', 'No', 'A+', 'regular'], ['CSE-242', '1.5', 'Level 2 - Term 1', 'Yes', 'A+', 'regular'], ['Math-241', '3', 'Level 2 - Term 1', 'No', 'A', 'regular'], ['CSE-245', '3', 'Level 2 - Term 1', 'No', 'A+', 'regular'], ['HUM-243', '3', 'Level 2 - Term 1', 'No', 'A+', 'regular'], ['CSE-243', '3', 'Level 2 - Term 2', 'No', 'A+', 'regular'], ['CSE-244', '1.5', 'Level 2 - Term 2', 'Yes', 'B+', 'regular'], ['EE-283', '3', 'Level 2 - Term 2', 'No', 'B-', 'regular'], ['EE-284', '0.75', 'Level 2 - Term 2', 'Yes', 'B+', 'regular'], ['CSE-251', '3', 'Level 2 - Term 2', 'No', 'A+', 'regular'], ['CSE-252', '1.5', 'Level 2 - Term 2', 'Yes', 'A+', 'regular'], ['CSE-223', '3', 'Level 2 - Term 2', 'No', 'A-', 'regular'], ['CSE-224', '0.75', 'Level 2 - Term 2', 'Yes', 'A+', 'regular'], ['Math-243', '3', 'Level 2 - Term 2', 'No', 'A+', 'regular'], ['CSE-200', '1.5', 'Level 2 - Term 2', 'Yes', 'A+', 'regular']]
def converter(d):
    if d=="A+":
    	return 4.00	
    elif d=="A":
        return 3.75
    elif d=="A-":
        return 3.50	
    elif d=="B+":
        return 3.25
    elif d=="B":
        return 3.00	
    elif d=="B-":
        return 2.75	
    elif d=="C+":
        return 2.50	
    elif d=="C":
        return 2.25
    elif d=="D":
        return 2.00	
    elif d=="F":
        return 0.00
term_wise_data={}
for i in data:
    if i[2] not in term_wise_data:
        term_wise_data[i[2]]=[]
        credit=float(i[1])
        grade=converter(i[4])
        prod=credit*grade
        fail_credit=0.0
        if i[4]=="F":
            fail_credit=converter(i[4])
        term_wise_data[i[2]].append(credit)
        term_wise_data[i[2]].append(prod)
        term_wise_data[i[2]].append(fail_credit)
    else:
        credit=float(i[1])
        grade=converter(i[4])
        prod=credit*grade
        fail_credit=0.0
        if i[4]=="F":
            fail_credit=converter(i[4])
        term_wise_data[i[2]][0]=term_wise_data[i[2]][0]+credit
        term_wise_data[i[2]][1]=term_wise_data[i[2]][1]+prod
        term_wise_data[i[2]][2]=term_wise_data[i[2]][2]+fail_credit

for i in term_wise_data:
    term_wise_data[i].append(term_wise_data[i][1]/(term_wise_data[i][0] - term_wise_data[i][2]))

print(term_wise_data)
sm=0
fail=0
totalcredit=0
sd=0
sgpa=[]
level=[]
for i in term_wise_data:
    sm= sm+ term_wise_data[i][1]
    fail= fail+ term_wise_data[i][2]
    totalcredit= totalcredit + term_wise_data[i][0]
    sd= sd+ term_wise_data[i][0]*term_wise_data[i][3]
    d=[]
    sgpa.append(term_wise_data[i][3])
    level.append(i)
    
print(sm/(totalcredit - fail))
print(totalcredit)
print(fail)
df=pd.DataFrame(sgpa,level,['sgpa'])
print(df)


         
