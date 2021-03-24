from random import *
#
# #zad1
#
# liczby = []
# for x in range(10):
#     liczby.append(randrange(1,30,1))
# print(liczby)
#
# plik = open("pomnozone","w")
# for x in liczby:
#     plik.write(str(x*2))
#     plik.write(" ")
# plik.close()
#
#
#
# #zad2
# plik = open("pomnozone", "r")
# print(plik.readlines())
# plik.close()
#


# #zad3
#
# with open("tekst.txt", "w+") as plik:
#     for x in range(5):
#         plik.write("Bla bla bla")
#     plik.close()
# plik = open("tekst.txt", "r")
# print(plik.readlines())
# plik.close()



# #zad4
#
# class NaZakupy():
#     def __init__(self, a, b, c, d):
#         self.nazwa_produktu = a
#         self.ilosc = b
#         self.jednostka_miary = c
#         self.cena_jed = d
#
#     def wyswietl_produkt(self):
#         print("Nazwa produktu = " + str(self.nazwa_produktu)  + "\n"
#               + "Ilosc = " + str(self.ilosc) + "\n"
#               + "Jednostka miary = " + str(self.jednostka_miary) + "\n"
#               + "Cena jednostkowa = " + str(self.cena_jed))
#
#     def ile_produktu(self):
#         print(str(self.ilosc) + str(self.jednostka_miary))
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
# produkt = NaZakupy("Mleko", 2, "l", 2)
# produkt.wyswietl_produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())



# #zad5
#
# 



# #zad6
# class Robaczek():
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += self.krok*ile_krokow
#
#     def idz_w_dol(self, ile_krokow):
#         self.y -= self.krok*ile_krokow
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= self.krok*ile_krokow
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x += self.krok*ile_krokow
#
#     def pokaz_gdzie_jestes(self):
#         return self.x,self.y
#
#
# podroz = Robaczek(0,0,2)
# podroz.idz_w_gore(5)
# podroz.idz_w_dol(2)
# podroz.idz_w_lewo(5)
# podroz.idz_w_prawo(2)
# print(podroz.pokaz_gdzie_jestes())