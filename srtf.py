arrivalT=[]
brustT=[]
waitT=[]
x=[]
count=0
avg=0
totalTime=0
process=[]
n = input( "enter the number of Processes: ")


for i in range(0 , n):
	process.append(raw_input("enter process name: "))
	arrivalT.append(raw_input("enter arrival time: "))
 	brustT.append(raw_input("enter burst time: ")) 
for i in range(0, n ):
	x.append(brustT[i])
brustT.append(9999)
  
for time in range(0 , count<>n):
	smallest=9
	for i in range(0 , n):
		if arrivalT[i]<=time and  brustT[i]<brustT[smallest] and  brustT[i]>0: 
			smallest=i    

waitT.append(0)          
i = 1
for i in xrange(n):
        waitT.append(0)
	j = 0
        for j in xrange(i):
            w=waitT[i]+brustT[j]
            waitT[i]=w
 
        totalTime+=waitT[i]
 
print'\nProcess\t    Burst Time    \tWaiting Time\n'
i = 0
for i in xrange(n):
        
        totalTime.append(brustT[i]+waitT[i])
        print'       ',process[i] ,  '       ' , brustT[i]  , '  	',waitT[i]    
 
 
print "\n\nAverage waiting time = \n",avg/n