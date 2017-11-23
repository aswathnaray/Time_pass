import pandas as pd
import matplotlib.pyplot as plt
import os.path as osp

file_source = "//vitoftp1\SFTP\spicy\Spicy_GEN_1 cells\Spicy_GEN1_Cylindrical hard casing\Ageing tests\Life-cycling\Raw data/1.ECU\Cycl_T25_Ch1C_TUM_Cyl_109_part1.xlsx"
head_row = 9
sheet_num = 0
print('Reading file of size ' + str(osp.getsize(file_source)/1048576) + ' MB')
file_data = pd.read_excel(file_source, sheetname=sheet_num, header=head_row)
c_no = 0
repeat_val = 1
mcolors = ["b", "g", "r", "c", "m", "k", "y", "w", "b", "g", "r", "c", "m", "y", "k", "w", "b", "g", "r", "c", "m",
               "y", "k", "w", "b", "g", "r", "c", "m", "y", "k", "w"]
lstyles = ['-', '-.', '--', ':', '-', '-.', '--', ':', '-', '-.', '--', ':', '-', '-.', '--', ':']

for col_name in list(file_data):
    print(str(c_no) + ': ' + str(col_name))
    c_no += 1

for repeat_dummy in range(100):
    color_no = 0
    if repeat_val == 1:
        x_ax = eval(input('Enter x-axis number: '))
        y_ax_string = input('Enter y-axis number(s) - seperate by commas: ')
        y_ax = y_ax_string.split(",")
        y_ax = [int(x) for x in y_ax]

        for y_ax_no in y_ax:
            plt.figure(num=1)
            plt.plot(file_data.iloc[:, x_ax], file_data.iloc[:, y_ax_no], color=mcolors[color_no], linestyle=lstyles[color_no])
            color_no += 1

        plt.grid()
        plt.show()
        repeat_val = eval(input('Do you want to plot more [0: No, 1: Yes]?: '))
    else:
        print('-- Program ended --')
        break

