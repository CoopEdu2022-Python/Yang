#12.2.2
#访问父类的私有属性、方法
#在 f2() 方法中，通过 _ClassName__attribute_name 直接访问 A 类的私有属性；在 f3() 方法中，通过 _ClassName__method_name 直接调用 A 类的私有方法
class A:
    def __init__(self):
        self.__u = 10

    def __f1(self):
        self.__u += 1
        print(self.__u)

    def _ClassName__attribute_name(self):
        print(self.__u)

    def _ClassName__method_name(self):
        self.__f1()


class B(A):
    def f2(self):
        super()._ClassName__attribute_name()

    def f3(self):
        super()._ClassName__method_name()

b=B()
b.f2()
b.f3()