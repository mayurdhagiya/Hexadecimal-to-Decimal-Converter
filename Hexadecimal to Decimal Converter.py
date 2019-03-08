import sys
mac = None
if len(sys.argv)  < 2:
	print "Usage: python convert.py <mac address> https://www.miniwebtool.com/mac-address-generator/ "
	_m = raw_input("Enter Mac Address:")
	mac = _m
else:
	mac = sys.argv[1]
maclist = []
decimal_maclist = []
'''
add whatever the sprater you want.
'''
symbols = [':','-']

print mac

for i in symbols:
	if i in mac:
		maclist = mac.split(i)
		break

print maclist
for i in maclist:
	decimal_maclist.append(int(i,16))
print "["
for num, val in enumerate(decimal_maclist):
    if num >= (len(decimal_maclist)-1):
	print val
    else:
	print val,','
print "]"