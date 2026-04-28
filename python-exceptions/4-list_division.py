#!/usr/bin/python3
def list_division(listem1, listem2, liste_boyu):
    son_liste = []
    for i in range(liste_boyu):
        sonuc = 0
        try:
            eleman1 = listem1[i]
            eleman2 = listem2[i]
            sonuc = eleman1 / eleman2
        except IndexError:
            print("out of range")
            sonuc = 0
        except ZeroDivisionError:
            print("division by 0")
            sonuc = 0
        except (TypeError, ValueError):
            print("wrong type")
            sonuc = 0
        finally:
            son_liste.append(sonuc)
    return son_liste
