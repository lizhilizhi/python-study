

import numpy as np
import  json
import jsonpath
import shuju


class cell_behavior(object):
    def __init__(self,date):
        self.date = date
    def sum_cell_behavior(date):
        total_amount_list = jsonpath.jsonpath(date,"$..total_amount")
        sum_total_amount = np.sum(total_amount_list)
        return sum_total_amount




sum_cell_behavior = cell_behavior.sum_cell_behavior(shuju.data)
print(sum_cell_behavior)