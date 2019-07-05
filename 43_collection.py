


name_tuple = (1,1,1)
#拆包
age,name,*other = name_tuple

#作为dict的key
user_info_dict = {}
user_info_dict[name_tuple]="bodu"


print(user_info_dict)