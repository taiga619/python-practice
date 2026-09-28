height_str = input("身長を入力してください")
height = float(height_str)
weight_str = input("体重を入力してください")
weight = float(weight_str)  
BMI = weight / (height/100 * height/100)
if BMI < 18.5:
    print("低体重")
elif 18.5 <= BMI < 25:
    print("普通体重")
else:
    print("肥満")

age_str = input("年齢を入力してください")
age = int(age_str)
if (age < 20) and (BMI < 18.5):
    print("あなたは低体重です。まだ成長期のため、十分な栄養と生活習慣を心がけましょう")