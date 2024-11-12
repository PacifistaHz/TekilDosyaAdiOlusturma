import datetime

dosyaAdi = datetime.datetime.now()
dosyaAdi = str(dosyaAdi)

print(dosyaAdi)

dosyaAdi = datetime.datetime.now()
dosyaAdi = dosyaAdi.strftime("%Y%m%d%H%M%S%f")

print(dosyaAdi)