

class Song(object):

    # sita funkcija visada yra automatiskai
    # iskvieciama, kai pirma karta paminima klase
    def __init__(self, lyrics):
        # pirmas kintamasis (tekstas), kuri paduodi klases sukurimo metu yra priskiriamas
        # vidiniui klases kintamajam, kuris bus pasiekiamas kitoms klases funkcijoms(metodams).
        self.vidinis_lyrics = lyrics
        

    def sing_me_a_song(self):
        # naudojamas self.vidinis_lyrics, nes jis jau yra priskirtas init funkcijos metu.
        for line in self.vidinis_lyrics:
            print line

    def labas(self):
        print "labas"

    def eiluciu_kiekis(self):
        # self.vidinis_lyrics yra listas visu eiluciu.
        print len(self.vidinis_lyrics)        

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

daina = ["Saule sviecia",
"vanduo blizga",
"guli merga"]

dainos_zodziai = Song(daina)
dainos_zodziai.sing_me_a_song()
dainos_zodziai.labas()
dainos_zodziai.eiluciu_kiekis()

happy_bday.sing_me_a_song()
happy_bday.labas()


bulls_on_parade.sing_me_a_song()
bulls_on_parade.labas()


