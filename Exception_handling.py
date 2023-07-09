# a = input("Enter a number")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
#
# print("Important Lines of Codes ")
# print("End of Program")
#
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)