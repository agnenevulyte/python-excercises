from sys import argv
from os.path import exists

script, is_failo_pavadinimas, i_faila_pavadinimas = argv

print "Copying from %s to %s" % (is_failo_pavadinimas, i_faila_pavadinimas)

# we could do these two on one line too, how? with ,
ivesties_failas = open(is_failo_pavadinimas)

# skaitom ivesties faila su read komanda
ivesties_tekstas = ivesties_failas.read()

# apskaiciuojame ivesties teksto dydi
print "The input file is %d bytes long" % len(ivesties_tekstas)

# tikriname ar egzistuoja i_faila_pavadinimas vardu failas
print "Does the output file exist? %r" % exists(i_faila_pavadinimas)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# atsidaromme rezultato faila su rasymo teisemis (tai tik teises, rasyt negalima)
rezultato_failas = open(i_faila_pavadinimas, 'w')

# irasome pries tai skaityto failo turini i rezultato_failas
rezultato_failas.write(ivesties_tekstas)

print "Alright, all done."

rezultato_failas.close()
ivesties_failas.close()