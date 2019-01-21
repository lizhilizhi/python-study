
# 数组


# http://www.cnblogs.com/alex3714/articles/5717620.html
name = ["zhejiang","hangzhou","quzhou"]
name.append("newone") #追加
name.insert(2,"从第二个前面插入")#插入
name[2]="444" #修改
del name[4] #删除
newname = ["zhangjiang1","zhejiang2"]
name.extend(newname) #扩展
# print(name[0:4])#打印
name_copy = name.copy() #拷贝
name.count() #统计
print (name[0:5])

names.sort()#排序

names.reverse() #反转
name.index() #获取下标

# 元组
# 元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能再修改，所以又叫只读列表
names = ("alex","jack","eric")
# 它只有2个方法，一个是count,一个是index，完毕。　