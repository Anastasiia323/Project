# set.update()

words = {'music', 'conductor', 'songwriter'}
words2 = {'guitar', 'bass player'}
words3 = {'piano', 'violin'}
words.update(words2, words3)

print(words)

# set.intersection_update()

set1 = {'orange', 'apple', 'vine'}
set2 = {'vine', 'beer', 'cocktail'}

set1.intersection_update(set2)

print(set1)

# set.difference_update()
# set.add()
# set.discard()

colors = {'red', 'black', 'white', 'orange'}
colors2 = {'white', 'green', 'pink', 'orange'}

colors2.difference_update(colors)
colors.add('yellow')
colors.discard('red')

print(colors)
print(colors2)

# set.pop()

numbers = {'1', '2', '3', '4', '5'}

numbers.pop()


print(numbers)

# set.clear()

condition = {'drunk', 'happy', 'sad'}
condition.clear()

print(condition)

# frozenset_

furniture2 = frozenset('123456')

print(furniture2)



print(furniture2)
