import sqlite3
with sqlite3.connect('new.db') as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE regions(city TEXT, region TEXT )")
	cities=[('New York City', 'Northeast'),('San Francisco', 'West'),('Chicago', 'Midwest'),('Houston',	'South'),('Phoenix', 'West'),('Boston',	'Northeast'),('Los Angeles','West'),('Houston',	'South'),('Philadelphia', 'Northeast'),('San Antonio', 'South'),('San Diego','West'),('Dallas','South'),('San Jose','West'),('Jacksonville','South'),('Indianapolis','Midwest'),('Austin','South'),('Detroit','Midwest')]

	c.executemany("INSERT INTO regions(city, region) values(?,?)",cities)
	# c.execute("SELECT * FROM regions order by region ASC")
	f = c.fetchall()
	for r in f:
		print(r[0],'\t',r[1])
