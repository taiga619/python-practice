# l1=[]
# l2=[]
# def f(a,b):
#     if a=="add":
#         l1.append(b)
#     elif a=="done":
#         x=l1.pop(0)
#         l2.append(x)
#         print(x,"done")
#     elif a=="undo":
#         y=l2.pop()
#         l1.insert(0,y)
#         print(y,"back")


# from collections import deque

# task_list = deque()
# done_list = deque()

# def add_task(actions, contents):
#     if actions == "add":
#         return task_list.append(contents)
    
# def complete_task(actions):
#     if actions == "done":
#         x = task_list.popleft()
#         print(x, "done")
#         return done_list.append(x)

# def undo_task(actions):
#     if actions == "undo":
#         y = done_list.pop()
#         print(y, "back")
#         return task_list.insert(0, y)
    
# add_task("add","買い物")
# add_task("add","掃除")
# complete_task("done")
# complete_task("done")
# undo_task("undo")


def task_change(actions, contents):
    if actions == "add":
        return task_list.append(contents)
    elif actions == "done":
        task_list.remove(contents)
        print(contents, "done")
        return done_list.append(contents)
    elif actions == "dont":
        print(contents, "dont")
        return task_list.remove(contents)
   

task_list = []
done_list = []

n = int(input("変更する項目数を入力してください"))

for i in range(n):
    action = input("add or done or dont を入力してください")
    content = input("具体的なタスク名を記入してください")
    task_change(action, content)

print("タスクリストは", task_list, "です")
print("完了リストは", done_list, "です")