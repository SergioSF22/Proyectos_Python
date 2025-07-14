"""Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}"""
set1 = {1, 2, "tres", "cuatro"}
set2 = {"tres", 4, 5}
set3 = set1.union(set2)
print(set3)