import  xlrd

data = xlrd.open_workbook("风盾风控策略(4).xlsx")

table = data.sheet_by_name("消金")



sql = open('test.txt',mode='w')


#
#     for i in table.row_values：



# line = """INSERT INTO `risk_control_saas_beta`.`admission_default_rule` ( `id`, `engine_event`, `policy_var_name`,"policy_var_name" `policy_desc`, `logic`, `right_var_name`, `right_var_value`, `enable`, `result`, `created_at`, `updated_at`, `category`)VALUES( , 'normal_tactic', '%s', '%s', '%s', '%s', '%s', %s, '%s', , , '业务策略' );""" %(table.cell_value(i,1),table.cell_value(i,2),table.cell_value(i,3),table.cell_value(i,4),table.cell_value(i,5),table.cell_value(i,6),table.cell_value(i,7))
#
#
#
# print(line)
#
# while i < table.nrows:
#     line = """INSERT INTO `risk_control_saas_beta`.`admission_default_rule` ( `id`, `engine_event`, `policy_var_name`,"policy_var_name" `policy_desc`, `logic`, `right_var_name`, `right_var_value`, `enable`, `result`, `created_at`, `updated_at`, `category`)VALUES( , 'normal_tactic', '%s', '%s', '%s', '%s', '%s', %s, '%s', , , '业务策略' );""" %(table.cell_value(i,1),table.cell_value(i,2),table.cell_value(i,3),table.cell_value(i,4),table.cell_value(i,5),table.cell_value(i,6),table.cell_value(i,7))
#     sql.writelines(line+"\n")
#     i = i+1
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n,sum))


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



