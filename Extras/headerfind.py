# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from openpyxl import load_workbook


def head_csv(file_ip_csv):
    row_ref = 100
    df = pd.read_csv(file_ip_csv, nrows=row_ref, chunksize=1)
    n_weight = 0
    rind = 0
    ind_val = 0
    for row in df:
        row_val = 0
        row = row.dtypes
        for e_idx in range(row.shape[0]):
            if row[e_idx] == np.dtype(np.object) or row[e_idx] == np.dtype(np.str):
                row_val += 1
            else:
                pass
        if row_val > n_weight:
            ind_val = rind
        n_weight = row_val
        rind += 1
    return ind_val


def head_xl(file_ip_xl):
    wb = load_workbook(file_ip_xl, read_only=True)
    n_weight = 0
    rind = 0
    ind_val = 0
    rown = 0
    sheet_no = eval(input('Enter sheet number: ')) - 1
    ws = wb.worksheets[sheet_no]
    for row in ws:
        if rown <= 100:
            row_val = 0
            for element in row:
                if type(element.value) == np.dtype(np.object) or type(element.value) == np.dtype(np.str):
                    # print('element')
                    row_val += 1
                else:
                    pass
            if row_val >= n_weight:
                ind_val = rind
                n_weight = row_val
            rind += 1
        else:
            break
        rown += 1
    return ind_val, sheet_no
    # ws = wb[eval(input('Enter sheet number: '))]
    #             print(type(element.value))
    # iter_df = df.iterrows()
    # n_weight = 0
    # rind = 0
    # ind_val = 0
    # for row in iter_df:
    #     row_val = 0
    #     print(row)
    #     row = row[1].dtypes
    #     for e_idx in range(row.shape[0]):
    #         if row[e_idx] == np.dtype(np.object):
    #             row_val += 1
    #         else:
    #             pass
    #     if row_val > n_weight:
    #         ind_val = rind
    #     n_weight = row_val
    #     rind += 1
    # return ind_val


def head(file_find_type):
    if '.csv' in str(file_find_type):
        output = head_csv(file_find_type)
        if output == 0:
            return output
        else:
            return output+1
    elif '.xls' in str(file_find_type):
        return head_xl(file_find_type)


#
# file1 = "C:\\Users\BADRINAR\Desktop\Test_data.csv"
# file_temp = "//eteintern01/ETE data/Batterijtestlabo/Kokam/16Ah/Cycle_life/2C/20-100/1/2 Ruwe data/Mat4Bat extraction raw data of ecu data from cel 7 version 2.csv"
# file_xlsx = "C:/Users/BADRINAR/Documents/170525_Data_eVAN17/Highway.xlsx"
# print(head(str(input('Enter file path: '))))
