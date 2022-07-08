
class BentukBuah():
    bulat = 10
    jorong = 40
    panjang = 70

    def turun(self, x):
        if x <= self.bulat:
            return 0
        elif x >= self.jorong:
            return 1
        else:
            return bawah(x, self.jorong, self.bulat)

    def pas(self, x):
        if self.bulat < x < self.jorong:
            return atas(x, self.bulat, self.jorong)
        elif self.jorong < x < self.panjang:
            return bawah(x, self.jorong, self.panjang)
        elif x == self.jorong:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.jorong:
            return 1
        elif x <= self.panjang:
            return 0
        else:
            return up(x, self.panjang, self.jorong)

class BentukPucuk():
    runcing = 10
    bulat = 30
    datar = 50

    def sedikit(self, x):
        if x >= self.bulat:
            return 0
        elif x <= self.runcing:
            return 1
        else:
            return down(x, self.runcing, self.bulat)
    
    def cukup(self, x):
        if self.runcing < x < self.bulat:
            return up(x, self.runcing, self.bulat)
        elif self.bulat < x < self.datar:
            return down(x, self.bulat, self.datar)
        elif x == self.bulat:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.datar:
            return 1
        elif x <= self.bulat:
            return 0
        else:
            return up(x, self.bulat, self.datar)

class BentukLekukan():
    tiakada = 10
    sedikit = 30
    jelas = 50

    def sedikit(self, x):
        if x >= self.sedikit:
            return 0
        elif x <= self.tidakada:
            return 1
        else:
            return down(x, self.tidakada, self.sedikit)
    
    def cukup(self, x):
        if self.tidakada < x < self.sedikit:
            return up(x, self.tidakada, self.sedikit)
        elif self.sedikit < x < self.jelas:
            return down(x, self.sedikit, self.jelas)
        elif x == self.sedikit:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.jelas:
            return 1
        elif x <= self.sedikit:
            return 0
        else:
            return up(x, self.sedikit, self.jelas)

class Warna():
    merah = 25
    hijau = 40
    kuning = 65
   
    def sedikit(self, x):
        if x >= self.hijau:
            return 0
        elif x <= self.merah:
            return 1
        else:
            return down(x, self.merah, self.hijau)
    
    def cukup(self, x):
        if self.merah < x < self.hijau:
            return up(x, self.merah, self.hijau)
        elif self.hijau < x < self.kuning:
            return down(x, self.hijau, self.kuning)
        elif x == self.hijau:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.kuning:
            return 1
        elif x <= self.hijau:
            return 0
        else:
            return up(x, self.hijau, self.kuning)
