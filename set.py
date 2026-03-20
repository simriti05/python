# SET PROPERTIES: tab use krege jab hamko duplicacy hatani hatani
# 1)It is not a sequence(indexing and slicing is not allowed)
# 2)It is an un-ordered collection
# 3)It is mutable(operations like insertion and deletion are allowed)
# 4)It can not contain duplicate elements
# 5)It can't preserve the insertion order
# 6)It may contain only immutable type of object


#frozenset-makes set immutable
# s=set("MISSISSIPPI")
# print(s)
# s={10,10,10,20,30,40,50,40,40}
# print(s)



forest_A = {'Tiger', 'Elephant', 'Deer', 'Monkey', 'Peacock'}
forest_B = {'Deer', 'Monkey', 'Bear', 'Leopard', 'Fox'}

forest_A.add('Wolf')
print(forest_A)

forest_B.add('Wolf')
print(forest_B)

forest_A.remove('Elephant')
print(forest_A)

forest_B.discard('Tiger')
print(forest_B)

forest_A.discard('Panda') NOTHING HAPPENS IN FRONTEND 
print(forest_A)

forest_A.remove('Panda') THROWS ERROR
print(forest_A)


