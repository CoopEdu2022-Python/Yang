"""
1. 什么是单继承？[多行注释]
子类拥有父类的所有方法和属性

2. 为什么使用单继承？[多行注释]
子类继承自父类，可以直接享受父类中已经封装好的方法，不需要再次开发

3. 什么是继承的传递性？[多行注释]
C类从B类继承，B类又从A类继承
那么C类就具有B类和A类的所有属性和方法

子类拥有父类以及 类的父类中封装的所有属性和方法
"""
# 1. 什么是多继承？
# 子类可以拥有多个父类，并且具有所有父类的属性和方法

# 2. 如果子类继承自多个父类，且父类中具有相同名称的方法，子类会选择哪个父类的方法执行？
# __mro__ 可以查看方法 索顺序，从左到右
# 继承的顺序class C(A, D, B):顺序ADB