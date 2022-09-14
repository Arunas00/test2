a = 10
a = a + 2
print(a)

a += 2
print("Dabar reiksme yra:", a)

a = a ** 3 #laipsnio pakelimas
print("pakelus 3 laipsniu:", a)

a /= 100
print("padalinus 100:", a)

b = 13
sveika_dalis = b // 2
print(b, "sveika dalis /2 yra:", sveika_dalis)

dalybos_liekana = b % 2
print(b, "liekana dalijant is 2:", dalybos_liekana)

user_input = input("Ivesk --> ")
print(int(user_input) * 3)