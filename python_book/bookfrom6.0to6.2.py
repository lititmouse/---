languages = {
    "xiaohua":"python",
    "xiangxing":"c",
    "xiaohong":"java",
}

#切片访问法
favarite_lauguage = languages["xiaohong"].upper()
print(favarite_lauguage)
value = languages.get("xiaohua")
print(value)
#get()访问值
point_value = languages.get("xianghuang","没有找到")
print(point_value)