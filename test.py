""" x = [1,2,3,4,5]
for i in x[5:]:
    print(i) """
    
data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

for row in data[1:]:  # Skip the first row
    print(row)