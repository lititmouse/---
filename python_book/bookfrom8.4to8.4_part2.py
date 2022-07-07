"""
禁止函数修改列表move_productions(now_productions[:],old_productions)
now_productions[:]表示列表副本 
"""

def move_productions(orginal_productions,aim_productions):
    while len(orginal_productions) > 0:
        mover = orginal_productions.pop(0)
        print(f"\n正在搬移{mover}")
        aim_productions.append(mover)

#展示aim_productions的元素

def display_productions(aim_productions):
    print(f"\n目标列表包括:\n")
    for product in aim_productions:
        print(f"{product}")

now_productions = ["23333",'sdsdsd','dwdwd']
old_productions = []

move_productions(now_productions[:],old_productions)
display_productions(now_productions)
display_productions(old_productions)