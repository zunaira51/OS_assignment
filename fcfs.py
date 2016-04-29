Pqueue = []
totaltime = 0
st = []
wt = []
a = 0
st.append(a) 
n = int(raw_input('enter the total number of processes:')) 
for i in xrange(n): 
	Pqueue.append([]) 
	Pqueue[i].append(raw_input('enter p_name:')) 
	Pqueue[i].append(int(raw_input('enter p_arrival:'))) 
	Pqueue[i].append(int(raw_input('enter p_burst:'))) 
	a = a + Pqueue[i][2] 
        st.append(a)
        Pqueue[i].append(st) 
        w = st[i] - Pqueue[i][1]
        Pqueue[i].append(w)
	wt.append(w) 
	totaltime += wt[i] 
	print ' '

Pqueue.sort(key = lambda Pqueue:Pqueue[1]) 
print 'ProcessName\tArrivalTime\tBurstTime\tWaitingTime' 
for i in xrange(n): 
    print Pqueue[i][0] , '\t\t', Pqueue[i][1] , '\t\t' , Pqueue[i][2] , '\t\t' , Pqueue[i][4],'\n' 
print 'Total waiting time:' , totaltime
print 'Average waiting time:' , (totaltime/n) 