import matplotlib.pyplot as plt

import nameyear

myname = u'Philip'
mygender = u'M'
getname = nameyear.nameyear[myname.upper()][mygender.upper()]

yearlist = []
countlist = []
for year in getname:
	yearlist.append(int(year))
	countlist.append(int(getname[year]))

plt.plot(yearlist,countlist,'ro')

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Name popularity of '+myname.title()+' ('+mygender.upper()+')')
plt.grid(True)
plt.show()