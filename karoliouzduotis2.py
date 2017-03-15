from sys import argv

script, failas1, failas2, failas3 = argv

# atidarome failas1, kuris turi duomenu
in_failas1 = open(failas1)
# skaitome failas1 duomenis
duomenys_failas1 = in_failas1.read()
print "%r failas, turi savyje duomenu, kuriuos nukopijuosime i tuscius failus %r ir %r." % (failas1, failas2, failas3)

# pasivadiname rezultato_failas, kuriame atidarome failas2
rezultato_failas = open(failas2, 'w')
# i rezultato failas perrasinejame failas1 duomenis
rezultato_failas.write(duomenys_failas1)

# pasivadiname rezultato_failas, kuriame atidarome failas2
rezultato_failas2 = open(failas3, 'w')
# i rezultato failas perrasinejame failas1 duomenis
rezultato_failas2.write(duomenys_failas1)
print "Patikrinkite, ar %r ir %rlaiko savyje ta pacia informacija kaip %r." % (failas2, failas3, failas1)

rezultato_failas.close()
rezultato_failas2.close()
in_failas1.close()