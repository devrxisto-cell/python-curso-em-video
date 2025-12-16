from calendar import day_name

m = float(input("Digite uma distância em metros: "))
c = m * 100
ml = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
dm = m / 1
print("{} metros é igual á : {} Quilômetro.".format(m, km))
print("{} metro é igual á : {} Hectômetro .".format(m, hm))
print("{} metro é igual á : {} Decâmetro.".format(m, dam))
print("{} metro é igual á : {} Decímetro.".format(m, dm))
print("{} metro é igual á : {} Centímetro.".format(m, c))
print("{} metro é igual á : {} Milímetro.".format(m, ml))