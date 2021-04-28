def liczba_do_elementu_listy(liczba, lista):
    nowa_lista=[]
    for i in lista:
        nowy_element = i + liczba
        nowa_lista.append(nowy_element)
    return nowa_lista

lista1=[1,2,3,4]
liczba1=10
wynik1=liczba_do_elementu_listy(liczba1, lista1)
print(wynik1)
lista2=[66,77,88,99]
liczba2=2
wynik2=liczba_do_elementu_listy(liczba2, lista2)
print(wynik2)
lista3=[100,101,102,103,104,105]
liczba3=5
wynik3=liczba_do_elementu_listy(liczba3, lista3)
print(wynik3)
lista4=[1000,2000,3000]
liczba4=100
wynik4=liczba_do_elementu_listy(liczba4, lista4)
print(wynik4)
