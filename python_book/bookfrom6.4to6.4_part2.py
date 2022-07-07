#在字典中储存列表
#创建包子的配方,并且访问
#bun = {
    #"馅":["酱肉","鲜肉","芝麻",'灌汤'],
   # "皮":["厚","薄"]}
#print("你可以选折",

   # "\n",bun["馅"],
   # "\n",bun["皮"])

liked_lunguages = {
    'xiaohiong':['Java','PHP','Python'],
    'xiangming':['Go','JavaScript','NET'],
    'xianghuang':['C++','Java','NET'],
}
################################################################
#直接访问like_lunguger
#print(liked_lunguages.items())
################################################################
#for遍历所有的键值对
for nane , lunguages in liked_lunguages.items():
    print(f"\n程序员{nane}最喜欢的的语言有:")
    #for遍历的值
    for lunguage in lunguages:
        print(f"\t{lunguage}")
