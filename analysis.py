import sys
import statistics as stat
import matplotlib.pyplot as plt


readings = []
Temps = []
Carbs = []

while(len(sys.argv) > 1):
    Temp = sys.argv[1]
    sys.argv.remove(Temp)
    Carb = sys.argv[1]
    sys.argv.remove(Carb)
    readings.append([float(Temp), float(Carb)])
    Temps.append(float(Temp))
    Carbs.append(float(Carb))

avgTemp = stat.mean(Temps)
medTemp = stat.median(Temps)
avgCarb = stat.mean(Carbs)
medCarb = stat.median(Carbs)

sortTemps = Temps.copy()
sortTemps.sort()
sortCarbs = Carbs.copy()
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

plt.scatter(Temps, Carbs)
plt.xlabel('Temperature (C)')
plt.ylabel('C02 Levels (ppm)')
plt.title('Temperature Compared to C02 Levels')
count = 1
for i in readings:
    plt.annotate(f"Microbit {count}", (i[0], i[1]))
    count += 1
plt.savefig('temp_carb_correlation.png')

with open('analysis_report.txt', 'w') as f:
    f.write("Analysis Report\n")
    f.write("----------------\n")
    f.write(f"Number of Readings: {len(readings)}\n")
    f.write("\n")
    count = 1
    for i in readings:
        f.write(f"Microbit {count} --- Temperature: {i[0]} C, C02 Level: {i[1]} ppm\n")
        count += 1
    f.write("\n")
    f.write("Statistical Analysis:\n")
    f.write("----------------\n")
    f.write(f"Average Temperature: {avgTemp:.2f}\n")
    f.write(f"Median Temperature: {medTemp:.2f}\n")
    f.write(f"Average C02 Level: {avgCarb:.2f}\n")
    f.write(f"Median C02 Level: {medCarb:.2f}\n")
    f.write(f"Range of Temperatures: {ranTemps:.2f}\n")
    f.write(f"Range of C02 Levels: {ranCarbs:.2f}\n")
    f.write(f"Relative Range of Temperatures: {relranTemps:.2f}\n")
    f.write(f"Relative Range of C02 Levels: {relranCarbs:.2f}\n")
    f.write(f"Correlation Coefficient: {cor:.4f}\n")
    f.write(f"{correlation}\n")

