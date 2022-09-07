hrs=input('Enter work hours:')
rt=input('Enter pay rate:')
hours=float(hrs)
rate=float(rt)
if hours<=40:
    print(hours*rate)
else:
    print(40*rate+(hours-40)*rate*1.5)    