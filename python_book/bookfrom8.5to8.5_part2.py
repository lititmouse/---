"""使用任意数量的关键字参数"""
def build_telephone_book(f_name,l_name,**information):
    information['first_name'] = f_name
    information['last_name'] = l_name
    return information

user_1 =  build_telephone_book("zheng","yuansong",mnber="123423434",locating="shanghai")
print(user_1)