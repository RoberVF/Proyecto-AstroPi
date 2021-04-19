from sense_hat import SenseHat
import time 
import datetime
from pathlib import Path
import csv
from logzero import logger, logfile
import math

#Setting all variables
now_time = datetime.datetime.now()
start_time = datetime.datetime.now()
sense = SenseHat()
accel_only = sense.get_accelerometer()
dir_path = Path(__file__).parent.resolve()
accelerometer_data = sense.get_accelerometer_raw()
temperatura = sense.get_temperature()
presion = sense.get_pressure()
humedad = sense.get_humidity()
tiempo = 180

# Starting text
print ('Starting program...')
print (start_time)
# Creating text files and setting names of them
logfile(dir_path/"projectx.log")
data_file = dir_path/"datax.csv"

# Creating all funtions
def create_csv(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time","Temperature", "Pressure", "Humidity", "Altitude")
        writer.writerow(header)

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

#We use try to avoid any possible error
try:
    logger.info(f"Starting...")
    create_csv(data_file)
    # Creating a loop to compare the initials datas with the real time datas
    while (now_time < start_time + datetime.timedelta(minutes=tiempo)):
        logger.info(f"Reading values")
        altura = (1-math.pow(presion/1013.25,0.190284))*145366.45*0.3048
        altitud =((44330.7606715224)*(1-math.pow(presion/1013.25,1/5.2559)))
        altitud = round(altitud,2)  
        print('Temperatura:' + str (temperatura) + '  Presion:' + str (presion) + '  Humedad:' + str(humedad) + '   Altura:' + str(altitud) )
        #We prepare the header to the .csv file
        now_time = datetime.datetime.now()
        print (now_time)
        row = (datetime.datetime.now(), temperatura, presion, humedad, altitud)
        logger.info(f"Adding values to data.csv")
        add_csv_data(data_file, row)
    logger.info(f"Program ended")
# We use except if any error appears
except Exception as e:
    logger.error(f'{e.__class__.__name__}: {e})')
