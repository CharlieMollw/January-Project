import sys
import statistics as stat
import matplotlib as plt


readings = []
Temps = []
Carbs = []

while(len(sys.argv) > 1):
    Temp = sys.argv[1]
    sys.argv.remove(Temp)
    Carb = sys.argv[2]
    sys.argv.remove(Carb)
    readings.append([float(Temp), float(Carb)])
    Temps.append(float(Temp))
    Carbs.append(float(Carbs))

avgTemp = stat.mean(Temps)
medTemp = stat.median(Temps)
avgCarb = stat.mean(Carbs)
medCarb = stat.median(Carbs)

sortTemps = Temps
sortTemps.sort()
sortCarbs = Carbs
sortCarbs.sort()

ranTemps = sortTemps[len(sortTemps)-1] - sortTemps[0]
ranCarbs = sortCarbs[len(sortCarbs)-1] - sortCarbs[0]

relranTemps = sortTemps[len(sortTemps)-1] / sortTemps[0]
relranCarbs = sortCarbs[len(sortCarbs)-1] / sortCarbs[0]

cor = stat.correlation(Temps, Carbs)

if cor == -1:
    correlation = "The temperatures and C02 levels have an exact negative correlation"
elif cor <= -0.66:
    correlation = "The temperatures and C02 levels have a strong negative correlation"
elif cor <= -0.33:
    correlation = "The temperatures and C02 levels have a weak negative correlation"
elif cor <= 0.33:
    correlation = "The temperatures and C02 levels have very little correlation"
elif cor <= 0.66:
    correlation = "The temperatures and C02 levels have an weak positive correlation"
elif cor < 1:
    correlation = "The temperatures and C02 levels have an strong positive correlation"
else:
    correlation = "The temperatures and C02 levels have an exact positive correlation"