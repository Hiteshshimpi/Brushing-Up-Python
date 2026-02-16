# cannot contain duplicates
# can have different data types
# set is immutable
myset = {1,2,3,4,'Hitesh'}
myset2={6,7,8}
print(myset)

# loop a set

for vale in myset:
    print(vale)


#inbuilt methods

# add items
myset.add('True')
print(myset)

# update to merge two sets
myset.update(myset2)
print(myset)


# to remove  and discard
myset.remove('True')
print(myset)

myset.discard('2')

# also pop
myset.pop()
print(myset)

# clears the enter set
myset.clear()
print(myset)