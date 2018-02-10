i=0
n=10

aif=[15,47,71,111,123,152,166,226,310,320]
sif=[43,36,34,30,38,40,31,29,36,30]
di=[]
ci=[]

while (i<n):

     ai = aif[i]
     if (len(ci)!=0):
        if ai < ci[i-1]:
           di.insert(i,ci[i-1]-ai)
        else:
          di.insert(i, 0)
     else:
        di.insert(i,0)

     si = sif[i]
     ci.insert(i , ai+di[i]+si)
     i = i+1


ganancias_viejo=49*n;

for x in di:
  if x>2:
    ganancias_viejo-=5;
sum=0

for x in ci:
  if x >12: 
   sum = x-12
   extras=sum*10
   ganancias_viejo-=extras
  
    
print ("Ganancia del dia ",ganancias_viejo)
     
     
     
sum = 0
sum2=0
for x in range(0,len(sif)):
    sum+=sif[x]
    sum2+=di[x]
    
    
Cn = aif[len(aif)-1] + di[len(di)-1] + sif[len(sif)-1] 

average_delay=sum2/n

Average_interarrival_time=aif[len(aif)-1]/n
average_Service_time=float(sum/n)
arrival_rate=1/Average_interarrival_time
W=average_delay+average_Service_time

I=(n/Cn)*W
Q=(n/Cn)*average_delay
X=(n/Cn)*average_Service_time



print ("\ndi = " + str(di))
print ("ci = " + str(ci))


print("\nAverage_interarrival_time = ",Average_interarrival_time)
print("Arrival rate = ",arrival_rate)
print("Average service time = ",average_Service_time)
print("Service rate = ",(1/average_Service_time))

print("-----------------------------------------------")
print("Average delay = ",average_delay)
print("Average wait = ",W)
print("I,  = ",I)
print("Q = ",Q)
print("X = ",X)
