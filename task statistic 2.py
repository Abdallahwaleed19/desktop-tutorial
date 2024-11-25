from statistics import mode
import scipy.stats as stats
import matplotlib.pyplot as plt

def numbers(x):
    x.sort()
    n = len(x)
    sum1=0
    list1=[]
    list2=[]
    list3=[]
    thisdict={}
    #Median
    if len(x)%2 ==0:
        y = (n//2 + (n+2)//2)//2
    else :
        y = (n+1)//2
    print("Median= ",y)  
    #Mean
    for i in range (len(x)):
        sum1+=x[i]
    mean=sum1/n
    print("mean= ",mean)
    #Range
    max1=x[0]
    for j in range(len(x)):
        if x[j] > max1:
            max1=x[j]
    min1=x[0]
    for j in range(len(x)):
        if x[j] < min1:
            min1=x[j]
    Range=abs(max1-min1)
    print("Range= ",Range)
    # meandeviation
    sum2=0
    for k in x:
        if k in thisdict.keys():
            thisdict[k] +=1
        else:
            thisdict[k]=1
    for q in x:
        if q not in list2:
            list2.append(q)
    for w in thisdict.values():
        list1.append(w)
    for t in range (len(list1)):
        sum2+=list1[t]*abs(list2[t]-mean)
    meandeviation=sum2/n
    print("meandeviation= ",meandeviation)
    #mode
    modevalues=mode(x)
    print("mode=",modevalues)
    # Variance
    sum3=0
    for t in range (len(list1)):
        sum3+=list1[t]*((list2[t]-mean)**2)
    Variance=sum3/(n-1)
    print("Variance= ",Variance)
    #Standard deviation
    Standard=Variance**(1/2)
    print("Standard= ",Standard)
    #Coefficient of variation
    Cv=mean/Standard
    print("Coefficient of variation= ",Cv)
    for i in list1:
            list3.append((i/n)*100)
    print(list1,list2,list3)
    #pie chart
    plt.pie(list3,labels=list2)
    plt.title("pie chart")
    plt.show()
    #Bar Chart
    plt.figure(figsize=(6,4))
    plt.bar(list2,list1, color="skyblue",edgecolor="black")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Bar Chart")
    plt.tight_layout()
    plt.show()
    #Scatter plot
    plt.scatter(list2,list1,color="blue",marker="o",s=50)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Scatter plot")
    plt.tight_layout()
    plt.show()
    #Box plot
    Q1=0.25*(1+n)
    Q3=0.75*(1+n)
    if Q1 < (int(Q1)+0.5):
        Q1=int(Q1)
    elif Q1 > (int(Q1)+0.5):
        Q1=int(Q1+0.5)
    elif Q1 == (int(Q1)+0.5):
        Q1=int(Q1+0.5)
    print("Q1=",Q1,"=",x[Q1-1])
    if Q3 < (int(Q3)+0.5):
        Q3=int(Q3)
    elif Q3 > (int(Q3)+0.5):
        Q3=int(Q3+0.5)
    elif Q3 == (int(Q3)+0.5):
        Q3=int(Q3+0.5)
    print("Q3=",Q3,"=",x[Q3-1],)
    IQR=x[Q3-1]-x[Q1-1]
    print("IQR=",IQR)
    lower = x[Q1-1]-(1.5*IQR)
    upper = x[Q3-1]+(1.5*IQR)
    print("Lower fence = ", lower )
    print("upper fence = ", upper )
    outliers=[]
    for i in list2:
        if i > upper  or i < lower  :
            outliers.append(i)
    print("outliers = ", outliers)
    plt.boxplot(x, vert=False,patch_artist=True)
    plt.scatter(outliers,[0]*len(outliers),color="red")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Box plot")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    #Skewed
    if abs(y-x[Q1-1])>abs(y-x[Q3-1]):
        print("Skewed left")
    elif abs(y-x[Q1-1])<abs(y-x[Q3-1]):
        print("Skewed right")
    elif abs(y-x[Q1-1])==abs(y-x[Q3-1]):
        print("Skewed Bell shape")
    #Skewness and Kurtosis
    skewness=stats.skew(x)
    print("skewness=", skewness)
    kurtosis=stats.kurtosis(x)
    print("kurtosis=",kurtosis)


values = [10, 99, 87, 45, 67, 43, 45, 33, 21, 7, 65, 98]
print(numbers(values))
