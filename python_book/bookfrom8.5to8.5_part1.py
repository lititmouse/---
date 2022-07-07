"""
传递任意数量的的实参
结合使用位置实参和任意数量的实参
"""
#制作拼盘饭

def make_conbination (principal_food,*Side_dishes):
    print(f"宁要的主食是:\n\t{principal_food}")
    print("你的配菜包括:")
    for side_dish in Side_dishes:
        print(f"\t{side_dish}")

make_conbination("米饭","红烧肉","番茄炒鸡蛋")