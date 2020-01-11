import matplotlib.pyplot as plt
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

plt.ion()	# turn on interactive plotting

while True:
    pressure_list = []
    temp_list = []
    humidity_list = []
    x = []

    for a in range(20):

        pressure = sense.get_pressure()-1000
        pressure_list.append(pressure)

        temp = sense.get_temperature()
        temp_list.append(temp)

        humidity = sense.get_humidity()/2
        humidity_list.append(humidity)

        print(pressure, temp, humidity)

        x.append(a)

        sleep(1)

    plt.clf()
    plt.plot(x,humidity_list)
    plt.plot(x,temp_list,'r')
    plt.plot(x,pressure_list,'g')
    plt.draw()