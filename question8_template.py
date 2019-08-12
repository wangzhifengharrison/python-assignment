"""COMP6730 question 8.

This should be completed individually.

Author: <u6068466>
Date: <Oct/21/2018>
"""
import random
import matplotlib.pyplot as plt
from assignment_template import fire_risk, load_bushfire, \
    load_vegetation_type, load_vegetation_density, load_wind_speed


def plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed):
    '''1. Function purpose: plot the number of cells on fire over time for each vegetation type. It is in graph format
      2. Restrictions: a. input (initial_bushfire, vegetation_type, vegetation_density, wind_speed) as lists of lists
      b. no return, show the plot
    '''
    steps = 200
    fire_factor_x = []
    initial_fire_point = set()
    vegetation = ["Open Forest", "Forest", "Open Woodland", "Woodland",
                  "Pine Forest", "Arboretum", "Grassland", "Shrubland",
                  "Golf Course", "Urban Vegetation", "Vineyard"]
    num_of_vegetation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vegetation_list = []

    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            if initial_bushfire[i][j] == '1':
                initial_fire_point.add((i, j))
    # all direction around point(x,y)
    near_fire_point = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for i in range(len(vegetation_type)):
        fire_factor_y = []
        for j in range(len(vegetation_type[i])):
            fire_factor_y.append(fire_risk(j, i, vegetation_type, vegetation_density, wind_speed))
        fire_factor_x.append(fire_factor_y)

    for step in range(steps):
        step_vegetation_list = []
        first_point = set(initial_fire_point)
        for point_value in set(initial_fire_point):
            for nearpoint in near_fire_point:
                pos_x = point_value[0] + nearpoint[0]
                pos_y = point_value[1] + nearpoint[1]
                if 0 <= pos_x < len(initial_bushfire) and 0 <= pos_y < len(initial_bushfire) and \
                        initial_bushfire[pos_x][pos_y] == '0':
                    random_num = 70 * random.random()
                    if random_num < fire_factor_x[pos_x][pos_y]:
                        initial_fire_point.add((pos_x, pos_y))

        final_point = set(initial_fire_point)
        new_point = final_point - first_point
        for i in range(len(vegetation)):
            for new_add_point in new_point:
                if vegetation_type[new_add_point[0]][new_add_point[1]] == vegetation[i]:
                    num_of_vegetation[i] = num_of_vegetation[i] + 1
        step_vegetation_list.extend(num_of_vegetation)
        vegetation_list.append(step_vegetation_list)
    # b - --blue
    # c - --cyan
    # g - --green
    # k - ---black
    # m - --magenta
    # r - --red
    # w - --white
    # y - ---yellow
    plt.plot(range(steps), [row[0] for row in vegetation_list], 'b--', label="Open Forest")
    plt.plot(range(steps), [row[1] for row in vegetation_list], 'c--', label="Forest")
    plt.plot(range(steps), [row[2] for row in vegetation_list], 'g--', label="Open Woodland")
    plt.plot(range(steps), [row[3] for row in vegetation_list], 'k--', label="Woodland")
    plt.plot(range(steps), [row[4] for row in vegetation_list], 'm--', label="Pine Forest")
    plt.plot(range(steps), [row[5] for row in vegetation_list], 'r--', label="Arboretum")
    plt.plot(range(steps), [row[6] for row in vegetation_list], 'm:', label="Grassland")
    plt.plot(range(steps), [row[7] for row in vegetation_list], 'y--', label="Shrubland")
    plt.plot(range(steps), [row[8] for row in vegetation_list], 'b-.', label="Golf Course")
    plt.plot(range(steps), [row[9] for row in vegetation_list], 'c-.', label="Urban Vegetation")
    plt.plot(range(steps), [row[10] for row in vegetation_list], 'k-.', label="Vineyard")

    plt.xlabel('Steps')
    plt.ylabel('Number of cells')
    plt.legend()  # show label text
    plt.title('Number of cells on fire over time for each vegetation type')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # south
    # initial_bushfire = load_bushfire("../data_and_code/data/south/initial_2003_bushfire.csv")
    # final_bushfire = load_bushfire("../data_and_code/data/south/2003_bushfire.csv")
    # vegetation_type = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
    # vegetation_density = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    # wind_speed = load_wind_speed("../data_and_code/data/south/wind.csv")
    # plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed)

    # ACT
    # initial_bushfire = load_bushfire("../data_and_code/data/act/initial_2003_bushfire.csv")
    # final_bushfire = load_bushfire("../data_and_code/data/act/2003_bushfire.csv")
    # vegetation_type = load_vegetation_type("../data_and_code/data/act/vegetation_type.csv")
    # vegetation_density = load_vegetation_density("../data_and_code/data/act/vegetation_density.csv")
    # wind_speed = load_wind_speed("../data_and_code/data/act/wind.csv")
    # plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed)

    # ANU
    initial_bushfire = load_bushfire("../untitled1/data/south/initial_2003_bushfire.csv")
    final_bushfire = load_bushfire("../untitled1/data/south/2003_bushfire.csv")
    vegetation_type = load_vegetation_type("../untitled1/data/south/vegetation_type.csv")
    vegetation_density = load_vegetation_density("../untitled1/data/south/vegetation_density.csv")
    wind_speed = load_wind_speed("../untitled1/data/south/wind.csv")
    plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed)

