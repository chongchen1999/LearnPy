class StuSystem(object):
    def __init__(self):
        self.stus = []
        self.index = 0

    def add(self):
        name = input("请输入新学生的姓名:")
        tel = input("请输入新学生的手机号:")
        address = input("请输入新学生的住址:")

        new_stu = {"name": name, "tel": tel, "address": address}
        self.stus.append(new_stu)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.stus):
            self.index = 0
            raise StopIteration()
        else:
            self.index += 1
            return self.stus[self.index - 1]

stu_sys = StuSystem()

stu_sys.add()
stu_sys.add()
stu_sys.add()

for temp in stu_sys:
    print(temp)

print([x for x in stu_sys])