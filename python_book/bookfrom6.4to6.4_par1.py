#列表包字典
one_1 = {"密码":"2733333","账号":"74444454"}
one_2 = {"密码":"23333","账号":"4464444"}
one_3 = {"密码":"2373343","账号":"4444444"}
one_4 = {"密码":"2373433","账号":"44544344"}
one_5 = {"密码":"3237333","账号":"4442444"}
list_1 = [one_1,one_2,one_3,one_4,one_5]
for dicts in list_1:
    print(dicts)

#代码自动生成字典列表
#空列表
ghosts = []
#自动生成列表词典
for ghos_munber in range(10):
    now_ghost = {'颜色':'red','血量':20,"移动速度":3}
    ghosts.append(now_ghost)
#打印列表词典
for now_ghost in ghosts:
    print(now_ghost)
print(len(ghosts))
#切片更改词典ghosts[0:5]
for change_1 in ghosts[0:5]:
    change_1['颜色'] = "yellow"
    change_1['血量']  = 30
    change_1['移动速度'] =4
#条件改变词典
for change_2 in ghosts:
    if change_2["颜色"] == "red":
        change_2['颜色'] = "blank"
        change_2['血量']  = 10
        change_2['移动速度'] = 6

for now_ghost in ghosts:
    print(now_ghost)
print(len(ghosts))








