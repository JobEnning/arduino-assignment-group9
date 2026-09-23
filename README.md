# arduino-assignment-group9
The description of the Arduino project of group 9 for the Open Science course.

## Components
There are two sensors involved in this setup. The CO2 sensor is shown below (front and back):
<img src="pictures/CO2.png" width="300">
<img src="pictures/CO2_2.png" width="300">

The other sensor is the Pressure/Temperature/Relative Humidity sensor, shown below:
<img src="pictures/TPRH.png" width="300">
<img src="pictures/TPRH2.png" width="300">

TODO add other components (Lester?)

## Wiring diagram
TODO insert wiring diagram (Loek)

## Installing the Arduino IDE
TODO Loek will add text here
also how to blink

## Clone the repository
TODO (Marijke)

## Running the codes
### General
Connect the Arduino using the USB-C (computer) to USB-B cable (Arduino). At the top, select the Arduino UNO. 
At the left, click the Library Manager button (books icon). Search for the following libraries and install them and their dependencies (install all):
- Adafruit BME280 Library, version 2.3.0
- 

### Temperature, pressure and relative humidity
Open the file `code/PTRHsensor/PTRHsensor.ino` in the Arduino IDE. Upload the code to the Arduino by clicking the `Upload` button in the top left (arrow to the right). Open the `Serial Monitor` with the button at the top right. The code will initialise the SD card and then starts measuring. The data is shown in the Serial Monitor window, but is also written to a `data.csv` file on the SD card; see below. The sensor measures the temperature (in degrees Celsius), the pressure (in Pascal) and the relative humidity (in percentages) with an interval of 10 seconds. 

### CO2 sensor
For the CO2 sensor, the same steps should be followed as for the temperature/pressure/relative humidity sensor, but with the file `code/CO2sensor/CO2sensor.ino`. The sensor measures the CO2 concentration of the air in parts per million (ppm) every 10 seconds. 

## Extract the data
The file `code/csv-extract/csv-extract.ino` can be used to show all the data stored in the `data.csv` file on the Arduino. Open the file and upload it to the Arduino as before. By running the code, the data is printed to the Serial Monitor window. Copy and paste the data to a file on your computer (`code/analyse/testdata_bme.dat` for the temperature/pressure/relative humidity data, `code/analyse/testdata_CO2.dat` for the CO2 concentration data) for analysis; see below. The file possibly contains data from both sensors, make sure to put the data corresponding to the correct sensor in the correct file. 

## Clear the SD card
The file `code/sdcard-erase/sdcard-erase.ino` can be used to erase the data on the SD card. Open the file and upload to the Arduino as before. 

# Analysis
The code `analyse/plot.py` generates plots showing the data. Run this Python code using VSCode, Spyder or any other software capable of running Python code. 