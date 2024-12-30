import random

class StuSystem(object):
    def __init__(self):
        self.stus = []

    def add(self):
        name = input("请输入新学生的姓名:")
        tel = input("请输入新学生的手机号:")
        address = input("请输入新学生的住址:")

        new_stu = {"name": name, "tel": tel, "address": address}
        self.stus.append(new_stu)

    def add_random(self):
        name = random.randint(10000000000, 19999999999)

    def __iter__(self):
        return iter(self.stus)

stu_sys = StuSystem()

stu_sys.add()
stu_sys.add()
stu_sys.add()

for temp in stu_sys:
    print(temp)