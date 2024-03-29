"""COMP1730/6730 assignment S2 2018.

Coauthors: <u6261174>, <u6068466>, <u6323315>
Date: <05/10/2018>
"""
import random
from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk
import csv
import math


# The following functions must return the data in the form of a
# list of lists; the choice of data type to represent the value
# in each cell, for each file type, is up to you.

# Question 1 Loading the datasets
def load_vegetation_type(filename):
    '''1. Function purpose: load act vegetation_type, anu vegetation_type and south_vegetation_type from a file to a
      list of lists.
      2. Restrictions: a. input (filename) must be a string.
                       b. filename must point to a .csv format file.
                       c. output will be given as a lists of lists data structure.
    '''
    with open(filename) as vegetation_type_csvfile:
        reader = csv.reader(vegetation_type_csvfile)
        # get row from table
        vegetation_type_table = [row for row in reader]
    return vegetation_type_table


def load_vegetation_density(filename):
    '''1. Function purpose: load act vegetation_density, anu vegetation_density and south vegetation_density from a file
     to a list of lists.
      2. Restrictions: a. input (filename) must be a string.
                       b. filename must point to a .csv format file.
                       c. output will be given as a lists of lists data structure.
    '''
    with open(filename) as vegetation_density_csvfile:
        reader = csv.reader(vegetation_density_csvfile)
        # get row from table
        vegetation_density_table = [row for row in reader]
    return vegetation_density_table


def load_wind_speed(filename):
    '''1. Function purpose: load act wind, anu wind and south wind from a file to a list of lists.
      2. Restrictions: a. input (filename) must be a string.
                       b. filename must point to a .csv format file.
                       c. output will be given as a lists of lists data structure.
    '''
    with open(filename) as wind_speed_csvfile:
        reader = csv.reader(wind_speed_csvfile)
        # get row from table
        wind_speed_table = [row for row in reader]
    return wind_speed_table


def load_bushfire(filename):
    '''1. Function purpose: load act 2003_bushfire, initial_2003_bushfire, anu 2003_bushfire, initial_2003_bushfire and
    south 2003_bushfire, initial_2003_bushfire from a file to a list of lists.
      2. Restrictions: a. input (filename) must be a string.
                       b. filename must point to a .csv format file.
                       c. output will be given as a lists of lists data structure.
    '''
    with open(filename) as bushfire_csvfile:
        reader = csv.reader(bushfire_csvfile)
        # get row from table
        bushfire_table = [row for row in reader]
    return bushfire_table


# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed_map):
    '''1. Function purpose: get the highest wind speed from the dataset. Data are from act wind.csv, anu wind.csv, south
    wind.csv.
      2. Restrictions: a. input (wind_speed) must be a lists of lists.
                       b. output would return the highest wind speed and the highest wind speed is in float type.
    '''
    new_data = []
    for i in range(len(wind_speed_map)):
        # get every list maximum value
        new_data.append(max(wind_speed_map[i]))
    # get maximum value of the every list maximum value.
    return max(new_data)


# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.

def count_cells(vegetation_type):
    '''1. Function purpose: show the count the number of cells filled by each kind of vegetation.
      2. Restrictions: a. each cell is same which is 100 * 100 m.
                       b. no return value, print the number of cells occupied by each kind of vegetation.
                       c. input (vegetation_type) must be a lists of lists returned by previous "load_vegetation_type" function.

    '''
    # get all the vegetation_type with no duplicate.
    vegetation = []
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            if vegetation_type[i][j] != '' and vegetation_type[i][j] not in vegetation:
                vegetation.append(vegetation_type[i][j])
    # get how many cells a specific type of vegetation showed.
    vegetation_num = []
    for type in vegetation:
        num = 0
        for i in range(len(vegetation_type)):
            for j in range(len(vegetation_type[i])):
                if vegetation_type[i][j] == type:
                    num += 1
        vegetation_num.append(num)
    # print out vegetation_type as well as how many cells accordingly.
    for i in range(len(vegetation)):
        print(vegetation[i], ": ",vegetation_num[i])
# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.


def count_area(vegetation_type, vegetation_density):
    '''1. Function purpose: show the count the area covered by each kind of vegtation.
      2. Restrictions: a. each cell is same which is 100 * 100 m.
                       b. no return value, print the number of area occupied by each kind of vegetation.
                       c. input (vegetation_type) must be a lists of lists returned by previous "load_vegetation_type"
                       and "load_vegetation_density" function.
    '''
    # get all the vegetation_type with no duplicate.
    vegetation = []
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            if vegetation_type[i][j] != '' and vegetation_type[i][j] not in vegetation:
                vegetation.append(vegetation_type[i][j])
    # get how much area a specific type of vegetation showed.
    vegetation_density_sum =[]
    for type in vegetation:
        density_sum = 0.00
        for i in range(len(vegetation_type)):
            for j in range(len(vegetation_type[i])):
                if vegetation_type[i][j] == type:
                    density_sum += float(vegetation_density[i][j])*10000
        vegetation_density_sum.append(density_sum)
    # print out vegetation_type as well as how many area accordingly.
    for i in range(len(vegetation)):
        print(vegetation[i], ": %.2f" % vegetation_density_sum[i], " sq m")


# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    '''1. Function purpose: calculate the fire risk for a single cell and estimate the risk of fire in each cell
    according to the vegetation type, vegetation density and the wind speed.
    2. Restrictions: a. fire risk factor for a cell is math.sqrt(a + density), a is difference according to
    type of vegetation
    b. the nearby distance is calculated by manhattan distance formula which is:
    abs(dif_y) + abs(dif_x) <= fire_radius.
    c. input (x,y) are indices of the cell to calculate fire risk for, they have to be integers and within the board.
    other input are lists of lists and be generated from previous functions.
    d. output (sum_risk_factor) would be a float.
    '''
    # x is the column and y is the row
    dif_x_arr = []
    dif_y_arr = []
    fire_radius =0
    # fire_radius is the radius of fire impact
    if wind_speed[y][x] != '':
        fire_radius = math.floor(float(wind_speed[y][x]))
    for dif_y in range(-fire_radius, fire_radius + 1):
        for dif_x in range(-fire_radius, fire_radius + 1):
            if abs(dif_y) + abs(dif_x) <= fire_radius:
                dif_x_arr.append(dif_x)
                dif_y_arr.append(dif_y)
    # sum all of the risk factor
    sum_risk_factor = 0
    for dif_y in range(0, len(dif_y_arr)):
        pos_x = x + dif_x_arr[dif_y]
        pos_y = y + dif_y_arr[dif_y]
        if 0 <= pos_y < len(vegetation_type) and 0 <= pos_x < len(vegetation_type[pos_y]):
            if vegetation_type[pos_y][pos_x] == "Shrubland" or vegetation_type[pos_y][pos_x] == "Pine Forest":
                sum_risk_factor = sum_risk_factor + math.sqrt(0.2 + float(vegetation_density[pos_y][pos_x]))
            elif vegetation_type[pos_y][pos_x] == "Arboretum":
                sum_risk_factor = sum_risk_factor + math.sqrt(0.1 + float(vegetation_density[pos_y][pos_x]))
            elif vegetation_type[pos_y][pos_x] == "Urban Vegetation" or vegetation_type[pos_y][pos_x] == "Golf Course":
                sum_risk_factor = sum_risk_factor + math.sqrt(0.05 + float(vegetation_density[pos_y][pos_x]))
            else:
                if vegetation_density[pos_y][pos_x] != '':
                    sum_risk_factor = sum_risk_factor + math.sqrt(0 + float(vegetation_density[pos_y][pos_x]))
    return sum_risk_factor


# The arguments to this function are an initial bushfile map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.

def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    '''1. Function purpose: show the final bushfire map after the fire is spread through several steps.
      2. Restrictions: a. assume the fire is influenced by the initial circumstance and will spread to it's eight
      neighboughs.
      b. input (initial_bushfire, vegetation_type, vegetation_density) are lists of lists and steps is an integer.
      c. output lists of lists.
    '''
    point =set()
    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            if(initial_bushfire[i][j]=='1'):
                point.add((i,j))
    # all direction around point(x,y)
    near_fire_point = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    for step in range(1,steps):
        for point_value in set(point):
            for nearpoint in near_fire_point:
                # new point around point(x,y)
                pos_x =point_value[0]+nearpoint[0]
                pos_y = point_value[1]+nearpoint[1]
                if(pos_x>=0 and pos_x<len(initial_bushfire) and pos_y>=0 and pos_y<len(initial_bushfire)):
                    if(initial_bushfire[pos_x][pos_y]!=''):
                        point.add((point_value[0]+nearpoint[0],point_value[1]+nearpoint[1]))
    # judge if the new point is on board and should be fired (marked as '1') or not (marked as '').
    for point in point:
        if(point[0]<len(initial_bushfire)and point[1]<len(initial_bushfire)):
            if(initial_bushfire[point[0]][point[1]]):
                initial_bushfire[point[0]][point[1]]='1'
            else:
                initial_bushfire[point[0]][point[1]]=''

    return initial_bushfire

# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# the load_bushfire function).


def compare_bushfires(bushfire_a, bushfire_b):
    '''1. Function purpose: get the reality percentage to compare qualitatively and the reality through calculate how
    much result of the simulation overlaps with the real bushfire.
      2. Restrictions: a. input (bushfire_a, bushfire_b) are lists of lists.
      b. output is a float to see the percentage of cells that are the same.
      c. ignore black cells entirely.
    '''

    # total number of cells
    total_cells = len(bushfire_a)*len(bushfire_a[0])

    # count blank cells in the map
    count_blank_cell =0
    for i in range(len(bushfire_a)):
        for j in range(len(bushfire_a[i])):
            if(bushfire_a[i][j]==''):
                count_blank_cell = count_blank_cell +1

    # count same cell in the bushfire_a and bushfire_b
    count_same_cell =0
    for i in range(len(bushfire_a)):
        for j in range(len(bushfire_a[i])):
            if(bushfire_a[i][j]==bushfire_b[i][j] and bushfire_a[i][j]!=''):
                count_same_cell = count_same_cell +1
    return count_same_cell/(total_cells-count_blank_cell)


# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def simulate_bushfire_stochastic(initial_bushfire, steps,vegetation_type, vegetation_density,wind_speed):
    '''1. Function purpose: stochastically simulate fire spreading for a number of steps. It taskes fire_risk of the cell
    into consideration.
      2. Restrictions: a. input (initial_bushfire, vegetation_type, vegetation_density,wind_speed) which is lists of
      lists, (steps) which is an integer.
      b. output initial_bushfire is a list of lists.
    '''

    fire_factor_x=[]
    initial_fire_point = set()

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
        for point_value in set(initial_fire_point):
            for nearpoint in near_fire_point:
                pos_x = point_value[0] + nearpoint[0]
                pos_y = point_value[1] + nearpoint[1]
                if 0 <= pos_x < len(initial_bushfire) and 0 <= pos_y < len(initial_bushfire) and initial_bushfire[pos_x][pos_y] == '0':
                    random_num = 70 * random.random()
                    if random_num < fire_factor_x[pos_x][pos_y]:
                        initial_fire_point.add((pos_x, pos_y))

    for point in initial_fire_point:
        if point[0] < len(initial_bushfire) and point[1] < len(initial_bushfire):
            if initial_bushfire[point[0]][point[1]]:
                initial_bushfire[point[0]][point[1]] = '1'
            else:
                initial_bushfire[point[0]][point[1]] = ''

    return initial_bushfire


if __name__ == '__main__':

    # If you want something to happen when you run this file,
    # put the code in this `if` block.
    # veg_density_map = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
    # show_vegetation_density(veg_density_map)
    # wind_speed = load_wind_speed("../data_and_code/data/anu/wind.csv")
    # print(highest_wind_speed(wind_speed))

    # question 3 test
    # veg_density_type = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
    # veg_density_map = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    # count_cells(veg_density_type)
    # print()
    # count_area(veg_density_type, veg_density_map)

    # question 4 anu test
    # density_map = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
    # type_map = load_vegetation_density("../data_and_code/data/anu/vegetation_type.csv")
    # wind_speed_map = load_wind_speed("../data_and_code/data/anu/wind.csv")
    # show_fire_risk(fire_risk, type_map, density_map, wind_speed_map)

    # question 4 south test
    # density_map = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    # type_map = load_vegetation_density("../data_and_code/data/south/vegetation_type.csv")
    # wind_speed_map = load_wind_speed("../data_and_code/data/south/wind.csv")
    # show_fire_risk(fire_risk, type_map, density_map, wind_speed_map)

    # question 4 act
    # density_map = load_vegetation_density("../data_and_code/data/act/vegetation_density.csv")
    # type_map = load_vegetation_density("../data_and_code/data/act/vegetation_type.csv")
    # wind_speed_map = load_wind_speed("../data_and_code/data/act/wind.csv")
    # show_fire_risk(fire_risk, type_map, density_map, wind_speed_map)

    # question 5 anu test
    # initial_bushfire = load_bushfire("../data_and_code/data/anu/initial_2003_bushfire.csv")
    # vegetation_density = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
    # vegetation_type = load_vegetation_density("../data_and_code/data/anu/vegetation_type.csv")
    # final_bushfire =simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, 54)
    # show_bushfire(final_bushfire)

    # question 5 south test
    # initial_bushfire = load_bushfire("../data_and_code/data/act/initial_2003_bushfire.csv")
    # vegetation_density = load_vegetation_density("../data_and_code/data/act/vegetation_density.csv")
    # vegetation_type = load_vegetation_density("../data_and_code/data/act/vegetation_type.csv")
    # final_bushfire = simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, 100)
    # show_bushfire(final_bushfire)

    # question 6 anu test
    # bushfire_a = load_bushfire("../data_and_code/data/anu/initial_2003_bushfire.csv")
    bushfire_b = load_bushfire("../untitled1/data/act/2003_bushfire.csv")
    # bushfire_a = load_bushfire("../data_and_code/data/south/initial_2003_bushfire.csv")
    # bushfire_b = load_bushfire("../data_and_code/data/south/2003_bushfire.csv")
    # # bushfire_b =final_bushfire
    # print(compare_bushfires(bushfire_a, bushfire_b))

    # # question 7
    # act
    initial_bushfire = load_bushfire("../untitled1/data/act/initial_2003_bushfire.csv")
    # final_bushfire = load_bushfire("../data_and_code/data/act/2003_bushfire.csv")
    vegetation_type = load_vegetation_type("../untitled1/data/act/vegetation_type.csv")
    vegetation_density = load_vegetation_density("../untitled1/data/act/vegetation_density.csv")
    wind_speed = load_wind_speed("../untitled1/data/act/wind.csv")
    # # show_bushfire(initial_bushfire)
    stochastic_bush_fire = simulate_bushfire_stochastic(initial_bushfire, 180, vegetation_type, vegetation_density, wind_speed)
    show_bushfire(stochastic_bush_fire)
    # show_bushfire(final_bushfire)
    # south

    # print(compare_bushfires(stochastic_bush_fire, bushfire_b))