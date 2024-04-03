from prettytable import PrettyTable
table = PrettyTable()

table.add_column("City", ["Pune", "Mumbai", "Hyderabad"])
table.add_column("State", ["Maharashtra", "Maharashtra", "Telangana"])
table.align='c'
print(table)

