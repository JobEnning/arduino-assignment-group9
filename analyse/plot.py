#%%
import numpy as np
import matplotlib.pyplot as plt

time, temp, pres, humi = np.genfromtxt("testdata_bme.dat", delimiter=',').T

plt.figure()
plt.plot(time, temp, '.-')
plt.xlim(0, time[-1]+time[1])
plt.xlabel("Time (s)")
plt.ylabel(r"Temperature (°C)")
plt.show()

plt.figure()
plt.plot(time, pres/100, '.-')
plt.xlim(0, time[-1]+time[1])
plt.xlabel("Time (s)")
plt.ylabel("Pressure (hPa)")
plt.show()

plt.figure()
plt.plot(time, humi, '.-')
plt.xlim(0, time[-1]+time[1])
plt.xlabel("Time (s)")
plt.ylabel("Relative humidity (%)")
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

time, co2 = np.genfromtxt("testdata_CO2.dat", delimiter=',').T

plt.figure()
plt.plot(time, co2, '.-')
plt.xlim(0, time[-1]+time[1])
plt.xlabel("Time (s)")
plt.ylabel(r"CO$_2$-concentration (ppm)")
plt.show()
