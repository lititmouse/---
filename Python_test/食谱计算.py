from typing import ChainMap, List

#分配三餐摄入能量
def divide_energy(__reccommand_energy_intake:str,__intake_ration:str):
    reccommand_energy_intake= int(__reccommand_energy_intake)
    tem__intake_ration_lsit= __intake_ration.split(sep=":")
    __intake_ration_lsit= list(map(int,tem__intake_ration_lsit))
  
    __x =[reccommand_energy_intake]*len(__intake_ration_lsit)
    __y= __intake_ration_lsit
    breakfast_lunch_support_intake_energy= list(map(lambda x,y:x*y/sum(__intake_ration_lsit),__x,__y))
    return breakfast_lunch_support_intake_energy

#分配每一餐的营养素的能量
def divide_nutrition_energy(__meal_energry:list,) -> List:
    __energy_ratio = input("输入糖类,脂肪,蛋白质比例\n推荐值0.55~0.65,0.2~0.3,0.1~0.15\n").split(",")
    mood =int(input("早晨输入0,午餐输入1,晚餐输入2\n")) 
    unll = []
    temp = __meal_energry.pop(mood)
    unll.append (temp)
    __meal_energry_listed = unll*len(__energy_ratio)
    cho_Oil_proteins_energy =list(map(lambda x,y:int(x*float(y)),__meal_energry_listed,__energy_ratio)) 
    return cho_Oil_proteins_energy

#根据能量计算每一种营养素的的重量

def count_all_mass (__cho_Oil_proteins_energy:list)-> List:
    cho_mass = __cho_Oil_proteins_energy[0]/4
    oll_mass = __cho_Oil_proteins_energy[1]/9
    proteins_mass = __cho_Oil_proteins_energy[2]/4
    return [cho_mass,oll_mass,proteins_mass]

#根据CHO的的重量计算主食的重量
def count_food_mass(__all__mass:list,__food_nutrition_dirt:dict)-> dict:
    staple_mass= (__all__mass[0]*100)/(__food_nutrition_dirt["CHO"]*__food_nutrition_dirt["eatable_part"])
    return {"name":__food_nutrition_dirt["name"],"food_mass":staple_mass}

#根据主食的重量计算主食的蛋白质
def count_food_proteins_mass(__all__mass:list,__food_nutrition_dirt:dict)-> dict:
    food_proteins_mass = __all__mass[0]*(__food_nutrition_dirt["proteins"]/__food_nutrition_dirt["CHO"])
    return {"name":__food_nutrition_dirt["name"],"food_proteins_mass":food_proteins_mass}


#根据主食的蛋白质和副食的总蛋白量计算副食重量
def count_complemntary(food_proteins_mass:dict,all__mass:list,complemntary_food_nutrition_ChainMap:ChainMap,complemntary_ratio_list:list)->list :
    complemntary_mass=[]
    complemntary_ratio_iter =iter(complemntary_ratio_list)
    all_complemntary_protein=all__mass[2]- food_proteins_mass["food_proteins_mass"]
    for mapping in complemntary_food_nutrition_ChainMap.maps:
        complemntary_ratio = next(complemntary_ratio_iter)
        
        complemntary_ooo= (all_complemntary_protein*100*complemntary_ratio)/(mapping["proteins"]*mapping["eatable_part"])
        complemntary_mass.append ({"name":mapping["name"],"protein_mass":complemntary_ooo})
    return complemntary_mass
#计算食用油量
def count_oil_mass(all_mass:list,food_mass:dict,__food_nutrition_dirt:list,complemntary_mass:list,complemntary_food_nutrition_ChainMap:ChainMap)-> float:
    oil_mass = all_mass[1]
    food_oil_mass = food_mass["food_mass"]*(__food_nutrition_dirt["oil"]/__food_nutrition_dirt["CHO"])
    complemntary_oll_mass = 0
    for _disce in complemntary_food_nutrition_ChainMap.maps:
        for _dict_ in complemntary_mass :
            if _disce["name"] == _dict_["name"]:
                complemntary_mass_one=_dict_["protein_mass"]*(__food_nutrition_dirt["oil"]/__food_nutrition_dirt["proteins"])
                complemntary_oll_mass += complemntary_mass_one
    counted_oil_mass =(float( oil_mass)-float(food_oil_mass) - float(complemntary_oll_mass))*0.8
    return {"oil":counted_oil_mass}

#根据菜品种类返回副食分配比例列表
def complemntary_ratio()->list:
    complemntary_ratio_unmber = int(input("副食的种类默认为2\n"))
    complemntary_ratio_list = [1/complemntary_ratio_unmber]*complemntary_ratio_unmber
    return complemntary_ratio_list

if __name__ == "__main__":
    #reccommand_energy_intake = "1800"
    reccommand_energy_intake = (input("输入推荐需求量\n"))
   # intake_ration= "3:4:3"
    intake_ration = input("输入早中晚餐摄入比例推荐值3:4:3\n")
    #energy_ratio = [0.55,0.3,0.15]
    #energy_ratio = input("输入糖类,脂肪,蛋白质比例\n推荐值0.55~0.65,0.2~0.3,0.1~0.15\n").split(",")
    
    


    food_nutrition_dirt={
    "name":"稻米（早籼，标一）",
    "eatable_part":1,
    "CHO":77.5,
    "oil":1,
    "proteins":8.8
    }

    complemntary_food_nutrition_dirt1={
    "name":"鸡蛋（红皮）",
    "eatable_part":0.88,
    "CHO":1.3,
    "oil":11.1,
    "proteins":12.8
    }

    complemntary_food_nutrition_dirt2={
    "name":"牛肉（瘦）",
    "eatable_part":1,
    "CHO":1.2,
    "oil":2.3,
    "proteins":20.2
    }

    complemntary_food_nutrition_ChainMap=ChainMap(complemntary_food_nutrition_dirt1,)
    
    divide_energys = divide_energy(reccommand_energy_intake,intake_ration)

    divided_nutrition_energy = divide_nutrition_energy(divide_energys,)

    all_food_mass =  count_all_mass(divided_nutrition_energy)

    food_mass=  count_food_mass(all_food_mass,food_nutrition_dirt)

    food_proteins_mass= count_food_proteins_mass(all_food_mass,food_nutrition_dirt)

    complemntary_ratio_list = complemntary_ratio()

    complemntary = count_complemntary(food_proteins_mass,all_food_mass,complemntary_food_nutrition_ChainMap,complemntary_ratio_list)
    
    print(complemntary)
    print(food_mass)

    print(count_oil_mass(all_food_mass,food_mass,food_nutrition_dirt,complemntary,complemntary_food_nutrition_ChainMap))