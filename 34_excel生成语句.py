import  xlrd
import re

data = xlrd.open_workbook("风盾风控策略(0424).xlsx")

table = data.sheet_by_name("小额")


sql = open('test7.txt',mode='w')


sum = 1
while sum < table.nrows:
    line = """INSERT INTO `risk_control_saas_beta`.`admission_default_rule` ( `id`, `engine_event`, `policy_var_name`,`policy_desc`, `logic`, `right_var_name`, `right_var_value`, `enable`, `result`, `created_at`, `updated_at`, `category`)VALUES( 'null', 'policy_credit', '%s', '%s', '%s', '%s', '{\\"type\\": \\"%s\\", \\"value\\": %s}', 0, '不通过', NOW(),NOW(), '%s' );""" %(table.cell_value(sum,5),table.cell_value(sum,2),table.cell_value(sum,3),table.cell_value(sum,6),table.cell_value(sum,10),table.cell_value(sum,4),table.cell_value(sum,0))
    sql.writelines(line+"\n")
    sum = sum +1

sql.close()









