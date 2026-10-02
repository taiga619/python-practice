# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("こんにちは、",self.name, "です。", self.age, "歳です。")

# person1 = Person("太郎", 25)
# person2 = Person("花子", 30)
# person1.greet()
# person2.greet()

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.done_list = []
    def add_task(self, actions, contents):
        if actions == "add":
            print(contents, "added")
            self.task_list.append(contents)
    def complete_task(self, actions, contents):
        if actions == "done":
            self.task_list.remove(contents)
            print(contents, "done")
            self.done_list.append(contents)
    def dont_task(self, actions, contents):
        if actions == "dont":
            print(contents, "dont")
            self.task_list.remove(contents)

tm = TaskManager()
tm.add_task("add", "買い物")
tm.add_task("add", "掃除")
tm.add_task("add", "洗い物")
tm.complete_task("done","買い物")
tm.dont_task("dont","掃除")
print("タスクリストは", tm.task_list, "です。")
print("完了リストは", tm.done_list, "です。")