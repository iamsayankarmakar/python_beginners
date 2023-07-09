# name = "alan"
# s = name.split(" ")
# print(s)
# if len(s) >= 2:
#     fname, lname = map(str,name.split(" "))
#     # print(fname)
#     # print(lname)
#     for i in range(len(fname)):
#         if fname[0].islower():
#             fname1 = fname.capitalize()
#         else:
#             fname1 = fname
#     for i in range(len(lname)):
#         if lname[0].islower():
#             lname1 = lname.capitalize()
#         else:
#             lname1 = lname
#     print(" ".join([fname1, lname1]))
# else:
#     for i in range(len(name)):
#         if name[0].islower() :
#             name1 = name.capitalize()
#         else:
#             name1 = name
#     print(name1)
#
def solve(s):
    l1 = s.split(" ")
    print(l1)
    name1 = " "
    for i in range(len(l1)):
        l1[i] = l1[i].capitalize()
        #name = l1[i].capitalize()
        #name1 = name1 + name

    print(" ".join(l1))

solve("chris alan")
solve("a123dds")
solve("12abc")

