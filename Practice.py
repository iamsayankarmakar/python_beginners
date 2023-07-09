# x = list(range(0,15))
# print(x)
# x.reverse()
# print(x)
# print(type(x))

# newlist = [0, "Kalyani Simanta", 8.5,
# "Kanchrapara", 15.6, "Naihati", 30.75, "Barrackpore", 46.8, "Dum Dum", 56.45, "Sealdah"]
# c = 0
# for i in newlist:
#         if type(i) == str:
#             print(i, type(i))
#             c += 1
# print(c)
#
dict = {"a": 100, "b": 200, "c": 300}
print(dict.items())
l1 = dict.values()
print(l1)
sum = 0
n = 0
for i in l1:
    sum += i
    n += 1

print(sum / n)

ClassV_Data = {"marks_out_of_50" : [24, 30, 32, 12, 44, 49], "name" : ['Sneha', 'Rahul',
'Trisha', 'Vijay', 'Neha', 'Robert']}
dict = {}
for i in range(6):
    dict[ClassV_Data["name"][i]] = ClassV_Data["marks_out_of_50"][i]
print(dict)
q = list(dict.keys())
print(q)
for i in range(len(q)):
    if dict[q[i]]< 20:
        dict.pop(q[i])
print(dict)