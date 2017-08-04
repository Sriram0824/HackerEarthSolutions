
# coding: utf-8

# In[6]:

#print the letters in the input removing duplicates and print it in the same order
from collections import OrderedDict
s=input()
k=OrderedDict()
for i in s:
    if i not in k:
        k[i]=1
for j in k:
    print(j,end='')
   


# In[ ]:

#INPUT The first line will contain an integer T denoting the number of test cases. The following T lines will contain a string S in lower case letters only.

#OUTPUT Print the number the vowels in the string S.

def calculate_vowels(ist):
    a=('a','e','i','o','u')
    count=0
    for i in ist:
        if i in a:
            count=count+1
    print(count)
    
nt=int(input())
for x in range(nt):
    ist=input()
    calculate_vowels(ist)
    

        


# In[1]:

def palindrome_check(ins):
    rins=ins[::-1]
    if rins==ins:
        ls=len(ins)
        if ls%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    
nt=int(input())
for x in range(nt):
    ins=input()
    palindrome_check(ins)
  


# In[15]:

#Each name belongs to exactly one group.
#Names that belong to the same group are pairwise anagrams.
#The first character of all the names in the same group are equal.
#The last character of all the names in the same group are equal.
#The number of groups is minimum possible.
#Input- The first line contains a single integer N indicating the size of the list. This is followed by N lines where each line contains a name listed by Sumit.
#Output- In a single line print minimum number of groups in a partition that satisfy above conditions
#all passed except 2 test cases
from collections import Counter
def check_an(inp):
    count=0
    temp=[]
    for i in inp:
        for j in inp:
            if(i != j and i[0]==j[0] and i[len(i)-1]== j[len(j)-1] and Counter(i)==Counter(j)):
                temp.append(j)
        if(len(temp)>0):
            for k in temp:
                inp.remove(k)
            del temp[:]
            count=count+1
    print(count)       
            
                
    
nt=int(input())
inp=[]
for x in range(nt):
    ins=input()
    inp.append(ins)
check_an(inp)    
    


# In[ ]:

def find_mm(inp):
    maxcount=0
    mincount=0
    for i in inp:
        if int(i)!=min(inp):
            maxcount=maxcount+int(i)
    for i in inp:
        if int(i)!=max(inp):
            mincount=mincount+int(i)
    print(mincount," ",maxcount)
    
        

nt=int(input())
inp=[]
ins=input()
inp=ins.split(' ')
find_mm(inp)
    


# nt=int(input())
# inp=[]
# ins=input()
# inp=int(ins.split(' '))
# print(inp)

# In[28]:

def find_mm(inp):
    inp.sort()
    maxcount=0
    mincount=0
    for index,value in enumerate(inp):
        if index != 0:
            maxcount=maxcount+value
        if index !=len(inp)-1:
            mincount=mincount+value
    print(mincount,maxcount)
    
nt=int(input())
inp=[]
inp1=[]
ins=input()
inp1=ins.split(' ')
for i in inp1:
    if(i!=' '):
        inp.append(int(i))
find_mm(inp)
    


# In[10]:

#searching index of a number
a=int(input())
b=input()
b1=[]
b1=map(lambda t: int(t),b.split())
c=int(input())
for index,i in enumerate(b1):
    if i==c:
        print(index)


# In[28]:

s="suvojit"
i=0
print(s[i:i+7])


# In[ ]:

nt=int(input())
for i in range(nt):
    scount=0
    sjcount=0
    inp=input()
    for i in range(len(inp)):
        if(inp[i:i+7]=="SUVOJIT"):
            sjcount=sjcount+1
        else:
            if(inp[i:i+4]=="SUVO"):
                scount=scount+1
    print('SUVO = {0}, SUVOJIT = {1}'.format(scount,sjcount))
            


# In[8]:

"""
Input: 
First line contains T, number of transactions done by Square in a day.
The following line contains T integers, the worth of each transactions. 
Next line contains Q, the no of queries.
Next Q lines contain an integer each representing the daily target.

Output: 
For each query, print the transaction number where the daily limit is achieved or -1 if the target can't be achieved.

"""
nt=int(input())
inp=input()
b=list(map(lambda t:int(t),inp.split()))
q=int(input())
tsum=sum(b)
for i in range(q):
    tar=int(input())
    count=0
    day=0
    if tar<=tsum:
        for j in b:
                if count < tar:
                    count=count+j
                    day=day+1
                else:
                    break
        print(day)
    else:
        print("-1")
    
    


# In[34]:

"""
Input Format

First Line of Input Contain Single Value N, Size of List
Second Line of Input Contain N Space Separated Integers
Third Line of Input Contain Single Value K

Output Format

Smallest Integer Value That is Repeated Exactly K Number of Time

Constraints
"""
from collections import Counter
nt=int(input())
b=[int(x) for x in input().split()]
b.sort()
c=Counter(b)
e=int(input())
for i in c:
    if(c[i]==e):
        print(i)
        break


# In[8]:

nt=int(input())
li=[]
for i in range(nt):
    msg=input()
    l=[int(x) for x in msg.split() if x.isdigit()==True]
    for i in l:
        li.append(i)
print(li)
    
    
    


# In[ ]:

""""
Input:
First line of input is N and Q.
Second line of input contains N space separated integer.
Next Q line contains Q integer each representing K described in problem statement.

Output:
Print Q lines each representing the Kth number when all remaining numbers are arranged in ascending order.

10 5
79 72 46 40 6 79 17 28 84 27 
2
9
2
5
1
"""
nt=[int(x) for x in input().split()] 
l=[int(x) for x in input().split()] 
l.sort() 
for x in range(nt[1]): 
    x=l[int(input())-1]
    print(x) 
    l.remove(x) 
    l.sort()


# In[ ]:

inp=set(input())
nt=int(input())
count=0
for i in range(nt):
    l=input()
    flag=True
    for k in l:
        if k not in inp:
                flag=False
    if flag==True:
        count=count+1
print(count)
    
        
            
        
        


# In[ ]:

from collections import Counter
nt=int(input())
l=[]
for i in range(nt):
    inp=[x for x in input().split() if '#' in x]
    for j in inp:
        l.append(j)
n=Counter(l).most_common()
n.sort(key=lambda x:x[0])
n.sort(key=lambda x:x[1],reverse=True)
for index,y in enumerate(n):
    if index<5:
        print(y[0])
    else:
        break
    


# In[14]:

from collections import Counter
l=["apple","apple","apple","Appstore","Appstore","Appstore","bat","bat","bat","bat"]
n=Counter(l).most_common()
print(n)
n.sort(key=lambda x:x[0])
n.sort(key=lambda x:x[1],reverse=True)
for i in n:
    print(i[0])


# In[ ]:



