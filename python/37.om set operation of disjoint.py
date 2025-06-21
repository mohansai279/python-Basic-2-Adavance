set1={"ram", "jenny","mohan","riya"}
set2={"jenny","mohan","riya"}
print(set1.isdisjoint(set2))
print(set1.isdisjoint("Keerthi" "harshita"))
print(set1.issubset(['jenny','karthik','ranchi']))
print(set1.issubset(["ram", "jenny","mohan"]))
print(set1.issuperset(["ram", "jenny","mohan"]))
print(set1.issuperset(set2))
set2.clear()
print(set2)
del set2  # we will get an error beacuase ! wait a minute guess it why ?
print(set2)





