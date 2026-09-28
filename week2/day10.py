def judge_grade(score):
    if score >= 80:
        return("優")
    elif 60 <= score <= 79:
        return("良")
    else:
        return("不可")
    
scores = []
n=int(input("人数を入力してください"))
for i in range(n):
    score = int(input("点数を入力してください")) 
    scores.append(score)
    judge = judge_grade(score) 
    print(score, "点は", judge, "です")

    average = sum(scores) / (i + 1)
    print("平均値は", average, "です")

counts = {}
for scores_search in scores:
    if scores_search in counts:
        counts[scores_search] = counts[scores_search] + 1
    else:
        counts[scores_search] = 1
for keys, values in counts.items():
    print(keys, ":", values)   