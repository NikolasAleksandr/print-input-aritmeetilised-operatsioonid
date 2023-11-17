from math import * 
#1
nimi=input("Sisesta oma nimi: ")
print("Tere,maailm! Tervitan sind {0}".format(nimi))

#2
# 3 + 8  / (4 - 2) * 4 
vastus=3 + 8  / (4 - 2) * 4
print("Arvutame valjendust: 3 + 8  / (4 - 2) * 4")
print("1.Arvutame sulgudes oleva osa (4 - 2):", 4 - 2)
print("2.Jagame 8 selle tulemusega:", 8 / (4 - 2))
print("3.Korrutame selle tulemuse 4-ga:", (8 / (4 - 2)) * 4)
print("4.Liidame esialgse arvuga 3:", 3 + (8 / (4 - 2)) * 4)
print("Vastus on:", vastus)
vastus_ilma_suludeta = 3 + 8 / 4 - 2 * 4
print("Vastus ilma suludeta:", vastus_ilma_suludeta)

#2.1
ringi_r=3
ruudu_kylg=2*ringi_r
ruudu_S=ruudu_kylg**2
ruudu_P=ruudu_kylg*4
ringi_S=pi*ringi_r**2
ringi_C=2*pi*ringi_r
print("Ruudu pindala:", ruudu_S)
print("Ruudu ymbermõõt:", ruudu_P)
print("Ringi pindala:", ringi_S)
print("Ringi ymbermõõt:", ringi_C)

#2.2
import math
maa_r_km = 6378  # Maa raadius (kilomeetrites)
myndi_läbimõõt_cm = 2.52  # 2-eurose myndi läbimõõt (sentimeetrites)
euro_myndi_paksus_cm = 0.22  # 2-eurose myndi paksus (sentimeetrites)

myndi_läbimõõt_meetrites = myndi_läbimõõt_cm / 100
myndi_S_meetrites_ruudus = math.pi * (myndi_läbimõõt_meetrites / 2) ** 2
myndi_V_meetrites_kuubis = myndi_S_meetrites_ruudus * euro_myndi_paksus_cm / 100
maa_ymbermõõt_km = 2 * math.pi * maa_r_km
vajalikud_myndid = maa_ymbermõõt_km / myndi_läbimõõt_meetrites

print("Maa ymbermõõt:", maa_ymbermõõt_km, "km")
print("Myndi läbimõõt:", myndi_läbimõõt_cm, "cm")
print("Myndi arv vajalik Maa ymbermõõdu katmiseks:", int(vajalikud_myndid), "2-eurost mynti")

#Programm on kirjutatud nii, et selle muutmine teiste planeetide ja myntide jaoks on suhteliselt lihtne. Vaja lihtsalt muuta Maa raadius, myndi läbimõõt ja paksus

#3
#kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll kill-koll
kill_koll = "kill-koll"
killadi_koll = "killadi-koll"
sõna_jada = [kill_koll] * 2 + [killadi_koll] + [kill_koll] * 2 + [killadi_koll] + [kill_koll] * 4
print(" ".join(sõna_jada))
#две переменные kill_koll и killadi_koll  Использование переменных позволяет легко изменять значения строк в одном месте кода, что делает его более читаемым и поддерживаемым.


#4
#Просто чтобы показывались слова песен
print("Esimene laul :")
print("Rong see sõitis tsuhh tsuhh tsuhh,")
print("piilupart oli rongijuht.")
print("Rattad tegid rat tat taa,")
print("rat tat taa ja tat tat taa.")
print("Aga seal rongi peal,")
print("kas sa tead, kes olid seal?")
print()
print("Teine laul :")
print("Rong see sõitis tuut tuut tuut,")
print("piilupart oli rongijuht.")
print("Rattad tegid kill koll koll,")
print("kill koll koll ja kill koll kill.")

#Чтобы был выбор какую песню хотят
laulu_number = input("Sisesta laulu number (1 või 2): ")

if laulu_number == "1":
    print("Rong see sõitis tsuhh tsuhh tsuhh,")
    print("piilupart oli rongijuht.")
    print("Rattad tegid rat tat taa,")
    print("rat tat taa ja tat tat taa.")
    print("Aga seal rongi peal,")
    print("kas sa tead, kes olid seal?")
elif laulu_number == "2":
    print("Rong see sõitis tuut tuut tuut,")
    print("piilupart oli rongijuht.")
    print("Rattad tegid kill koll koll,")
    print("kill koll koll ja kill koll kill.")
else:
    print("Sellist laulu ei eksisteeri.")


