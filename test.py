d1 = {'Антон':{'city':'Moskow','temp':20,'wind':'o'},
		'Настя':{'city':'Tbilisy','temp':25,'wind':'s'},
		'Марина':{'city':'Piter','temp':15,'wind':'w'}
	}

v_n = input ('Имя: ')
print (d1.get(v_n, 'Данных нет'));
print (d1.get(v_n));
print (d1[v_n]);
####

