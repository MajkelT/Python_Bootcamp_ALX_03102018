parametry = {"end" : "Koniec", "sep" : "_odstep_"}

print("To jest pierwszy tekst", "To jest drugi tekst", **parametry)
print("To jest trzeci kekst z osobnego printa")


def formatuj(*args, **kwargs):    #arguments, key word arguments
    tekst = "\n".join(args)
    for k in kwargs:
        tekst = tekst.replace("$"+k, str(kwargs[k]))
    return tekst

def test_formatuj():   #musi być, żeby obsłużył to PY test
    assert formatuj(
        'koszt $cena PLN',
        'kwota #cena brutto',
        cena=10,
    )