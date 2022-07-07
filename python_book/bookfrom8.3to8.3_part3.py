#返回词典

def person_infor (nane,phone,email):
    person_information = {"名字":nane, "电话号码":phone, "电子邮箱":email}
    return person_information

one=person_infor("小名",233333,"233333")
print (one)