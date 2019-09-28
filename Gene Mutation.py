###Q1.Longest common subsequece

def lcs(x,y): #use dynamic programming, construct a table c that records the optimal solution
    m = len(x) 
    n = len(y)
    c = [[0 for k in range(n+1)],[0 for k in range(n+1)]] #create c with two rows, storing the current maximum length and the previous one
    for i in range(1,m+1): #iterate through every element in x (and y)
        for j in range(1,n+1):
            #three situations discussed in textbook
            if x[i-1]==y[j-1]:
                c[1][j]=c[0][j-1]+1
            elif c[0][j] >= c[1][j-1]:
                c[1][j] = c[0][j]
            else:
                c[1][j]=c[1][j-1]
        #since we've already updated the current row with the previous row, we move the current row to c[0] so that it can be treated as the "previous row" for next iteration
        c[0]=c[1]
        #then we contruct the "current row" for the next iteration with 0s
        c[1]=[0 for k in range(n+1)]
    return c[0][-1]

#testcose
    
test1='acdgf'
test2='cgmnz'

print(lcs(test1,test2))


###Q2.Lengths of LCSs
import numpy as np

Set_Strings = {(0, 'CAGCGGGTGCGTAATTTGGAGAAGTTATTCTGCAACGAAATCAATCCTGTTTCGTTAGCTTACGGACTACGACGAGAGGGTACTTCCCTGATATAGTCAC'),
   (1, 'CAAGTCGGGCGTATTGGAGAATATTTAAATCGGAAGATCATGTTACTATGCGTTAGCTCACGGACTGAAGAGGATTCTCTCTTAATGCAA'),
   (2, 'CATGGGTGCGTCGATTTTGGCAGTAAAGTGGAATCGTCAGATATCAATCCTGTTTCGTAGAAAGGAGCTACCTAGAGAGGATTACTCTCACATAGTA'),
   (3, 'CAAGTCCGCGATAAATTGGAATATTTGTCAATCGGAATAGTCAACTTAGCTGGCGTTAGCTTTACGACTGACAGAGAGAAACCTGTCCATCACACA'),
   (4, 'CAGTCCGGCGTAATTGGAGAATATTTTGCAATCGGAAGATCAATCTTGTTAGCGTTAGCTTACGACTGACGAGAGGGATACTCTCTCTAATACAA'),
   (5, 'CACGGGCTCCGCATCTATTTTGGGTCAAGTTGCATATCAGTCATCGACAATCAAACACTGTTTTGCGGTAGATAAGATACGACTGAGAGAGGACGTTCGCTCGAATATAGTTAC'),
   (6, 'CACGGGTCCAATTTTGGAGTAAGTTGATATCGTCACGAAATCAATCCTGTTTCGGTAGTATAGGACTACGACGAGAGAGGACGTTCCTCTGATATAGTTAC'),
   (7, 'GGTCCGTCAATTTTGGAGTAAGTTGATATCGTCACGAAATCAATCCTGTTTCGGTAGTATAGGACTACGACGAGAGAGGACGTTCCTCTGATATAGTTAC'),
   (8, 'CACGGGAATCCGTCAATTTTGGAGTAAGTTGATATCGTCACGAAATCAATCCTGTTTCGGTAGTATAGGACTACGACGAGAGAGGACGTTCCTCTGATATAGTTAC'),
   (9, 'CACGGGTCCGTCAATTTTGGAGTAAGTTGATATCGTCACGAAATCAATCCTGTTTCGGTAGTATAGGACTACGACGAGAGAGGACGTTCCTCTGATATAGTTAC')}

Lst_Strings = list(Set_Strings) #making the set into a list for easy indexing

length_table=np.empty((10,10)) #create a length table where the element in the ith row and jth column (python index) is the length of LCS of the string i and j (according to Set_Strings)

for i in range(10): #Fill half of the table with the LCS of the strings, because there is repetition between Table[i][j] and Table[j][i], we only calculate once
    for j in range(i,10):
        length_table[Lst_Strings[i][0]][Lst_Strings[j][0]]=lcs(Lst_Strings[i][1],Lst_Strings[j][1])

#Since originally we have an unordered set of strings, when we transform it to a list, the strings are not sorted in order. Thus the table we have is not a triangular matrix.
#Transform the table to a lower-triangular matrix. We can just disregard the diagonal (which are the LCS of the strings themselves) and the upper triangle (which are the repetitions of the lower one)
for i in range(10):
    for j in range(10):
        if length_table[i][j]!=0: #
            if j>i:
                length_table[j][i]=length_table[i][j]
                length_table[i][j]= 0

print(length_table)
            
print([len(x[1]) for x in Set_Strings])          
            
            