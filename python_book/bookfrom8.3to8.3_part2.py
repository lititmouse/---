#实参课选择的
def get_complete_2(f_name,l_name,m_name=" "):
    full_name = f"{f_name}{m_name}{l_name}" 
    return full_name .title()

ludi = get_complete_2 ("鲁迪乌斯","格雷拉特")
print(ludi)