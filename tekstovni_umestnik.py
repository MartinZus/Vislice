import model

def izpis_igre(igra):
    return (
       "========================================================\n" +
       "Število preostalih dovoljenih napak {}\n".format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1) +
       "Pravilni del gesla: {}\n".format(igra.pravilni_del_gesla()) +
       "Neuspeli poiskusi: {}\n".format(igra.nepravilni_ugibi()) +
       "=========================================================="
    )

def izpis_zmage(igra):
    return f"Čestitam! Uganil si geslo {igra.geslo}"

def izpis_poraza(igra):
    return f"Porabil si vse poiskuse. Geslo je {igra.geslo}"

def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
