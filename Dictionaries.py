capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}

print(capital_city.values())
print(capital_city["Nepal"])
print(capital_city.items())

for i in capital_city.keys():
    print(i ,end = ":")
    print(capital_city[i])
 print(capital_city.items())

for a,b in capital_city.items():
     print(f"The value for the key {a} is {b}")

sgc=[('UUU','F'), ('UUC','F'), ('UUA','L'), ('UUG','L'), ('CUU','L'), ('CUC','L'), ('CUA','L'), ('CUG','L'),
('AUU','I'), ('AUC','I'), ('AUA','I'), ('AUG','M'), ('GUU','V'), ('GUC','V'), ('GUA','V'), ('GUG', 'V')]
Dict = dict(sgc)
print(Dict)



