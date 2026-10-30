scores = [80, 70, 90, 60, 85, 75]

group1 = scores[::2]
group2 = scores[1::2]

print("Group 1:", group1)
print("Group 2:", group2)

print("Group 1 total:", sum(group1))
print("Group 2 total:", sum(group2))