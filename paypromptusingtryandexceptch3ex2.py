hrs=input('enter hours:')
rt=input('enter rate')
try:
    hours=float(hrs)
    rate=float(rt)
except:
    print('Error, please enter numeric input')
exit()
if hours<=40:
    print(hours*rate)
else:
    print((((hours-40)*rate)*1.5)+rate*40)    