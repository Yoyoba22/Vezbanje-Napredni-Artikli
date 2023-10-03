# Napraviti bazu podataka aritkli sa poljima
# Sifra artikla(serial pk), naziv(varchar), kolicina(integer) i cena(float).
# Popuniti sa makar 10 podataka.
# Podatke iz sql ucitati u pandas dataframe.
# Dizajn ima jedan entry i dva dugmeta. Dugmad imaju tekst “search and export” i export all.
# Kada se klikne bilo koje dugme otvara se novi prozor za odabir fajla za export. 
#Odabir je izmedju excel i csv fajla.
# Kada se odabere fajl ukoliko je kliknuto na dugme export all exportuje se ceo dataframe kao izabrani fajl.
# Ukoliko je kliknuto dugme export and search ispisuju se sve informacije vezane za pretrazeni 
#fajl u tip fajla koji je izabran u prozoru.


import psycopg2 as pg
import pandas as pd
from tkinter import *

class Artikli:
    def __init__(self):
        self.con=pg.connect(
            database='Artikli',
            host='localhost',
            port='5432',
            user='postgres',
            password='Yoyoba22'
            )
        self.artikli_df=None
    
    def get_artikli(self):
        self.artikli_df=pd.read_sql_query('SELECT * FROM Artikal',self.con)
    
    def export_all(self,odabir):
        if odabir=='csv':
            self.artikli_df.to_csv('svi_csv.csv',index=False)
            return 'CSV fajl uspesno kreiran'
        else:
            self.artikli_df.to_excel('svi_excel.xlsx',index=False)
            return 'Excel fajl uspesno kreiran'
    
    def search_dataframe(self,sifra):
        l=self.artikli_df.iloc[sifra-1]
        return l
    
    def search_sql(self,sifra):
        cursor=self.con.cursor()
        s='SELECT * FROM Artikal WHERE sifra_artikla={}'.format(sifra)
        cursor.execute(s)
        result=cursor.fetchall()
        cursor.close()

        return result
    
    def export_pretraga(self,sifra,odabir):
        if odabir=='csv':
            s=self.search_dataframe(sifra)
            s.to_csv('{}.csv'.format(s.loc['naziv']))
            return 'CSV Fajl uspesno eksportovan'
        else:
            s=self.search_dataframe(sifra)
            s.to_excel('{}.xlsx'.format(s.loc['naziv']))
            return 'Excel Fajl uspesno eksportovan'

A=Artikli()
A.get_artikli()

root=Tk()

def potvrda(odabir,searched):
    t=Toplevel(root)
    l=Label(t,text='Odaberite tip fajla').pack()
    t_b=Button(t,text='CSV')
    t_b.pack()
    b1=Button(t,text='Excel')
    b1.pack()
    l1=Label(t,text='')
    l1.pack()
    if odabir=='all':
        t_b.configure(command=lambda:l1.configure(text=A.export_all('csv')))
        b1.configure(command=lambda:l1.configure(text=A.export_all('excel')))
    else:
        t_b.configure(command=lambda:l1.configure(text=A.export_pretraga(int(searched),'csv')))
        b1.configure(command=lambda:l1.configure(text=A.export_pretraga(int(searched),'excel')))

e=Entry(root)
e.pack()
b=Button(root,text='Search and export',command=lambda:potvrda('s',e.get())).pack()
b1=Button(root,text='Export all',command=lambda:potvrda('all',None)).pack()


mainloop()