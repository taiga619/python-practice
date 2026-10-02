# name1="太郎"
# height1=170
# weight1=65
# bmi1=weight1/((height1/100)*(height1/100))
# print(name1,bmi1)

# name2="花子"
# height2=160
# weight2=50
# bmi2=weight2/((height2/100)*(height2/100))
# print(name2,bmi2)

# name3="次郎"
# height3=180
# weight3=80
# bmi3=weight3/((height3/100)*(height3/100))
# print(name3,bmi3)

def calc_bmi(height_cm, weight_kg):
    return weight_kg/((height_cm/100)*(height_cm/100))

n = int(input("入力する人数を設定してください"))
for i in range(n):
    name = input("名前を入力してください")
    height = int(input("身長(cm)を入力してください"))
    weight = int(input("体重(kg)を入力してください"))
    print(name, "さんのBMIは", calc_bmi(height, weight), "です")