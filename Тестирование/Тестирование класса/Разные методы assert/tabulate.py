

#one_list = ["Метод","Использование"]
#listt = [
#    ["assertEqual(a, b)","Проверяет, что a == b"],
#    ["assertNotEqual(a, b)","Проверяет, что a != b"],
#    ["assertTrue(x)","Проверяет, что значение x истинно"],
#    ["assertFalse(x)","Проверяет, что значение x ложно"],
#    ["assertIn(элемент, список)","Проверяет, что элемент входит в список"],
#    ["assertNotIn(элемент, список)","Проверяет, что элемент не входит в список"]
#]
#print tabulate(one_list,listt)

from tabulate import tabulate
table=[['Alex',13,1,'Chess',10],['Zia',12,2,'Chess',25]]
headers=["Name","Age", "Number of Games","Favourite Game","Cost of Game"]
print tabulate(table, headers, tablefmt="grid")