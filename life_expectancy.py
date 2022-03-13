import sqlite3

import matplotlib.pyplot as plt
import numpy as np
Connection = sqlite3.connect('life.db')
curs = Connection.cursor()
#drop NULL value
sql_command = '''
DELETE FROM life 
where lifeexpectancy IS NULL 
OR GDPpercapita IS NULL 
'''
sql_command2 ='''SELECT Entity, Lifeexpectancy, GDPpercapita, Population FROM life1
WHERE Year = 2007
'''
curs.execute(sql_command)
curs.execute(sql_command2)

myresult = curs.fetchall()

#list1 = list(zip(*myresult))
np_list = np.array(myresult)

#plt.scatter(np_list[0:10,2], np_list[0:10,1])
#convert string to float
life_exp = np_list[0:150,1]
life_exp=np.asfarray(life_exp,float)
pop = np_list[0:150,3]
#convert to float
np_pop = np.asfarray(pop, float)
np_pop = np_pop/100000

gdp_cap = np_list[0:150,2]
gdp_cap = np.asfarray(gdp_cap,float)

country = np_list[0:150,0]
#print(gdp_cap)
#print(life_exp)
#display the size of the dot
#plt.scatter(gdp_cap,life_exp, s = np_pop)
fig, ax = plt.subplots()
ax.scatter(gdp_cap,life_exp, s = np_pop)

for i, txt in enumerate(country):
    ax.annotate(txt, (gdp_cap[i], life_exp[i]))

plt.xscale('log')

xlab = 'GDP per Capital in USD'
ylab = 'Life expectancy'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title('World Developement in 2007')
tick_val = [1000, 10000, 100000]
tick_tab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_tab)
plt.show()

#for x in myresult:
  #print(x)
#scatter
#plt.scatter(GDP, life_expetancy)
#plt.show()

Connection.close()