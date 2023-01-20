#Salem Dejenu
#TechID=15443580
#STARID= tt0325hu
#Question 1
Num=int(input("Enter a number from 0 and 86,399:"))
Hours1=Num//3600
Minutes1=(Num%3600)//60
Seconds3=Num%60
print(Hours1)
print(Minutes1)
print(Seconds3)

#Question2

Days1= int((19*86400))
Hours2=int(12*3600)
Minutes3=int(15*60)
Seconds4=int((20))
totalseconds=int((Days1+Hours2+Minutes3+Seconds4))
a=int(totalseconds//7)
b=int(totalseconds//13)
c=int(totalseconds//35)

Population1=int(334205119)
TotalA=int(Population1+a)
TotalB=int(Population1-b)
TotalC=int(Population1+c)
Population2=int(TotalA+TotalB+TotalC)
print(Population2)

#Question 3
Seconds1=int(input("Enter amount of Seconds:"))
days= Seconds1//86400
Hours=(Seconds1%86400)//3600
Minutes=(Seconds1%3600)//60
Seconds=Seconds1%60

print(days,"days",Hours,"hours",Minutes,"minutes",Seconds,"seconds")

a=int(Seconds1//7)
b=int(Seconds1//13)
c=int(Seconds1//35)
Pop=int(334205119)

POP2=int(Pop+a-b+c)
print("total population",POP2)

#Question 4

population=int(334205119)
flapjacks=int(((((population+350)**2-12))/50))
flapjack2=(flapjacks**0.2)//1
print(flapjack2)
























