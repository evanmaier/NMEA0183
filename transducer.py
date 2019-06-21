import time
from NMEA0183 import NMEA0183

serial_location = '/dev/ttyUSB0'
serial_baudrate = 4800
serial_timeout = 5

#Provides the required serial device info
nmea = NMEA0183(serial_location,serial_baudrate,serial_timeout)

#Starts the serial connection
nmea.start()

#Checks if there is a valid connection
if nmea.exit == False:
   print('Connection!')
   #wait for buffer
   time.sleep(3)

   while True:

      #Depth data
      depth = nmea.data_depth['meters']

      #Weather data
      temperature = nmea.data_weather['water_temp']

      time.sleep(0.1)

   #Quit the NMEA connection
   nmea.quit()

else:
   print('No connection!')
