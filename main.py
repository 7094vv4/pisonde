import smbus2
import bme280
import mh_z19
import board
from adafruit_ht16k33.matrix import Matrix8x8


def set_matrix():
    if co2 > 1500: # ✕
        matrix[0, 0] = 1
        matrix[1, 1] = 1
        matrix[2, 2] = 1
        matrix[3, 3] = 1
        matrix[4, 4] = 1
        matrix[5, 5] = 1
        matrix[6, 6] = 1
        matrix[7, 7] = 1
        matrix[0, 7] = 1
        matrix[1, 6] = 1
        matrix[2, 5] = 1
        matrix[3, 4] = 1
        matrix[4, 3] = 1
        matrix[5, 2] = 1
        matrix[6, 1] = 1
        matrix[7, 0] = 1
    elif co2 > 1000: # △
        matrix[0, 3] = 1
        matrix[0, 4] = 1
        matrix[1, 2] = 1
        matrix[1, 5] = 1
        matrix[2, 2] = 1
        matrix[2, 5] = 1
        matrix[3, 1] = 1
        matrix[3, 6] = 1
        matrix[4, 1] = 1
        matrix[4, 6] = 1
        matrix[5, 0] = 1
        matrix[5, 7] = 1
        matrix[6, 0] = 1
        matrix[6, 7] = 1
        matrix[7, 0] = 1
        matrix[7, 1] = 1
        matrix[7, 2] = 1
        matrix[7, 3] = 1
        matrix[7, 4] = 1
        matrix[7, 5] = 1
        matrix[7, 6] = 1
        matrix[7, 7] = 1
    else: # ○
        matrix[0, 2] = 1
        matrix[0, 3] = 1
        matrix[0, 4] = 1
        matrix[0, 5] = 1
        matrix[1, 1] = 1
        matrix[1, 6] = 1
        matrix[2, 0] = 1
        matrix[2, 7] = 1
        matrix[3, 0] = 1
        matrix[3, 7] = 1
        matrix[4, 0] = 1
        matrix[4, 7] = 1
        matrix[5, 0] = 1
        matrix[5, 7] = 1
        matrix[6, 1] = 1
        matrix[6, 6] = 1
        matrix[7, 2] = 1
        matrix[7, 3] = 1
        matrix[7, 4] = 1
        matrix[7, 5] = 1


matrix_i2c = board.I2C()
matrix = Matrix8x8(matrix_i2c)

matrix.brightness = 0
matrix.brink_rate = 0
matrix.fill(0)

bme280_port = 1
bme280_address = 0x76
bme280_bus = smbus2.SMBus(bme280_port)

bme280_calibration_params = bme280.load_calibration_params(
    bme280_bus, bme280_address)

bme280_data = bme280.sample(
    bme280_bus, bme280_address, bme280_calibration_params)

mh_z19_data = mh_z19.read()

temperature = bme280_data.temperature
humidity = bme280_data.humidity
pressure = bme280_data.pressure
co2 = mh_z19_data['co2']

print('Temperature: {:.1f} C'.format(temperature))
print('Humidity: {:.1f} %'.format(humidity))
print('Pressure: {:.1f} hPa'.format(pressure))
print('CO2 Concentration: {:.1f} ppm'.format(co2))
set_matrix()
