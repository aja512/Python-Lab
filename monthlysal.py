bs=input("Enter basic salary:")
days=input("Enter no. of working days:")
ovrti=input("Enter no. of overtime working hrs:")
deduct=0
if days<6:
   deduct=3500
   salary=calci(bs,days,ovrti,deduct)
elif days>=6 and days<=12:
   deduct=1000
   salary= calci(bs,days,ovrti,deduct)
elif days>=13 and days<=18:
   deduct=800
   salary=calci(bs,days,ovrti,deduct)
else:
   deduct=0
   salary=calci(bs,days,ovrti,deduct)
			
def calci(bs,days,ovrti,deduct):
    sal=0
	emp=str(input('Enter type of Employee:'))
	if emp=='Permanent':
        bonus=22500
		sal=bs+ovrti*500+bonus-deduct
		print(sal)
	else:
		bonus=2500
		sal=bs+ovrti*500+bonus-deduct
		print(sal)
