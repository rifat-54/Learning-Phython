# collection={1,2,2,2,"hello","world","world"}

# print(collection)

# print(len(collection))

collection=set()

collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hellow")

collection.add((4,5,6))

collection.add([6,7])

collection.remove(1)


print(collection)