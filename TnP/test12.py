# | union
# & intersection
# - subtraction
# ^ symmetric difference

all_stu={1,2,3,4,5,6,7,8,9,10,11}
sing={2,4,6,8}
dance={1,2,3,5,7}
back={2,9,10}
print("not in anything",all_stu-(sing|dance|back))
print("in all",sing&dance&back)
print("in sing and dance",sing&dance)