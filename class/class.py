class ClassA:
    @staticmethod
    def method_in_class_a():
        print("Method in ClassA")


class ClassB:
    def call_method_from_class_a(self):
        ClassA.method_in_class_a()
        print("Method in ClassB")


obj_b = ClassB()
obj_b.call_method_from_class_a()
