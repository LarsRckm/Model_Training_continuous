from create_data import generate_discontinous_timeseries2
import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(1000)
y_start = 5.0
random_number_range= ["norm",0,5]

for i in range(10):
    y_trend, y_noisy_spline,min_value_spline, max_value_spline, noise_std_value = generate_discontinous_timeseries2(x_values, y_start,random_number_range, [800000,1100000], 100000,["norm",0,0.05])



    fig, ax = plt.subplots(1,1)
    ax.plot(x_values, y_noisy_spline)
    ax.plot(x_values, y_trend)

    plt.show()