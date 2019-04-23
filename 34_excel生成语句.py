import  xlrd
import re

data = xlrd.open_workbook("风盾风控策略(4).xlsx")

table = data.sheet_by_name("消金")


sql = open('test3.txt',mode='w')


sum = 0
while sum < table.nrows:
    line = """INSERT INTO `risk_control_saas_beta`.`admission_default_rule` ( `id`, `engine_event`, `policy_var_name`,`policy_desc`, `logic`, `right_var_name`, `right_var_value`, `enable`, `result`, `created_at`, `updated_at`, `category`)VALUES( 'null', 'normal_tactic', '%s', '%s', '%s', '%s', '{\\"type\\": \\"%s\\", \\"value\\": %s}', 0, '不通过', NOW(),NOW(), '%s' );""" %(table.cell_value(sum,5),table.cell_value(sum,2),table.cell_value(sum,3),table.cell_value(sum,6),table.cell_value(sum,10),table.cell_value(sum,4),table.cell_value(sum,0))
    sql.writelines(line+"\n")
    sum = sum +1

sql.close()





#
#
# class  CustomerRule:
#     def set_param(self,i):
#         self.engine_event = ''
#         self.policy_var_name =table.cell_value(i,2)
#         self.policy_desc = table.cell_value(i,3)
#         self.logic = table.cell_value(i,4)
#         self.right_var_name = table.cell_value(i,5)
#         self.right_var_value = table.cell_value(i,6)
#         self.enable = table.cell_value(i,7)
#         self.result = table.cell_value(i,8)
#         self.enable = table.cell_value(i,9)
#         self.category = table.cell_value(i,10)



