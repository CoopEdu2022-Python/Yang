price = input("请输入苹果价格：")
weight = input("请输入苹果重量：")
#price1 = int(price) weight1 = int(weight)不知int为何不行1
price1 = float(price)
weight1 = float(weight)
Price = price1 * weight1
print("需要支付%.02f元" % Price)