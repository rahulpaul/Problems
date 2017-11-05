"""
Spyder Editor

This is a temporary script file.
"""

import random


class Food:
    
    def __init__(self, name, value, calorie):
        self.name = name
        self.value = value
        self.calorie = calorie
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calorie
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return ''.join((self.name, ':', '<', str(self.value), ', ' , 
                        str(self.calorie), '>'))


def buildMenu(names, values, calories):
    return [Food(*entry) for entry in zip(names, values, calories)]

#names = ['Green Apple', 'Orange']
#values = [100, 50]
#calories = [10, 4]

#for food in buildMenu(names, values, calories):
#    print(food)


def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    totalCost, totalValue = 0., 0.
    selectedItems = []
    for item in itemsCopy:
        if totalCost + item.getCost() <= maxCost:
            totalCost += item.getCost()
            totalValue += item.getValue()
            selectedItems.append(item)
    
    return totalValue, totalCost, selectedItems


def testGreedy(items, constraint, keyFunction):
    value, cost, taken = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', value)
    for item in taken:
        print('   ', item)


def testGreedys(foods, maxUnits):
    print('Use Greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('Use Greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda food: 1 / food.getCost())
    print('Use Greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, calories)


def maxVal(toConsider, avail):    
    if len(toConsider) == 0 or avail == 0:
        return 0, ()
    elif toConsider[0].getCost() > avail:
        return maxVal(toConsider[1:], avail)
    nextItem = toConsider[0]
    remainingItems = toConsider[1:]
    withVal, withToTake = maxVal(remainingItems, avail - nextItem.getCost())
    withVal += nextItem.getValue()
    withoutVal, withoutToTake = maxVal(remainingItems, avail)
    if withVal > withoutVal:
        withToTake += (nextItem, )        
        return withVal, withToTake
    else :
        return withoutVal, withoutToTake


def fastMaxVal(toConsider, avail, memo={}):
    key = len(toConsider), avail
    if key in memo:
        return memo[key]    
    elif len(toConsider) == 0 or avail == 0:
        result =  0, ()
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        remainingItems = toConsider[1:]
        withVal, withToTake = fastMaxVal(remainingItems, avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(remainingItems, avail, memo)
        if withVal > withoutVal:
            withToTake += (nextItem, )
            result = withVal, withToTake
        else :
            result = withoutVal, withoutToTake
    memo[key] = result
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Use Search Tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken = ', val)
    print('Total cost of items taken = ', sum(item.getCost() for item in taken))
    if not printItems:
        return
    for item in taken:
        print('   ', item)


"""
Generates all combinations of N items into two bags, whereby each item is in 
one or zero bags.

Yields a tuple, (bag1, bag2), where each bag is represented as a list of which 
item(s) are in each bag.
"""

def yieldAllCombos(toConsider, bag1=(), bag2=()):
        if len(toConsider) == 0:
            yield bag1, bag2
        else:
            nextItem = toConsider[0]
            remainingItems = toConsider[1:]
            # nextIem is not selected in either bag
            yield from yieldAllCombos(remainingItems, bag1, bag2)            
            # nextItem selected in bag1
            yield from yieldAllCombos(remainingItems, bag1 + (nextItem, ), bag2)
            # nextItem selected in bag2
            yield from yieldAllCombos(remainingItems, bag1, bag2 + (nextItem, ))


def yieldAllCombosNonRecursive(items):    
    emptyEntry = (), ()  # no items selected in either bag
    yield emptyEntry
    powerSet = [emptyEntry]
    for item in items:
        newEntries = []
        for bag1, bag2 in powerSet:
            bag1WithItem = bag1 + (item, )
            bag2WithItem = bag2 + (item, )
            entry1 = bag1WithItem, bag2
            entry2 = bag1, bag2WithItem
            newEntries.extend((entry1, entry2))
        
        for entry in newEntries:
            yield entry
        
        powerSet.extend(newEntries)
            
            
def testYieldAllCombosRecursive(items):
    n = 0
    for bag1, bag2 in yieldAllCombos(items):
        print(bag1, bag2)
        n += 1
    print('Total combination for ', len(items), 'items = ', n)


def testYieldAllCombosNonRecursive(items):
    n = 0
    for bag1, bag2 in yieldAllCombosNonRecursive(items):
        print(bag1, bag2)
        n += 1
    print('Total combination for ', len(items), 'items = ', n)        


def testYieldAllCombos(items):
    set1 = set([(bag1, bag2) for bag1, bag2 in yieldAllCombos(items)])
    set2 = set([(bag1, bag2) for bag1, bag2 in yieldAllCombosNonRecursive(items)])
    print('Total combination for ', len(items), 'items, using recursive algo = ', len(set1))
    print('Total combination for ', len(items), 'items, using non-recursive algo = ', len(set2))
    print('set1 == set2 is', set1 == set2)
    

def buildLargeMenu(numItems, maxValue, maxCost):
    indices = list(range(numItems))
    names = ['Food-' + str(i) for i in indices]
    values = [random.randint(1, maxValue) for _ in indices]
    calories = [random.randint(1, maxCost) for _ in indices]
    return buildMenu(names, values, calories)


def testMaxValLarge(algorithm):
    for numItems in range(5, 500, 5):
        print('Try a menu with numItems', numItems, 'items')
        items = buildLargeMenu(numItems, 90, 250)
        testMaxVal(items, 750, algorithm, printItems=False)
        print('\n################################\n')
        
        

def main():
    # testGreedys(foods, 750)
    # testMaxVal(foods, 750, maxVal)
    
    # print('\n################################\n')

    # testGreedys(foods, 1000)
    # testMaxVal(foods, 1000, maxVal)
    
    # print('\n################################\n')
    # items = list(range(5))
    # testYieldAllCombosRecursive(items)
    # testYieldAllCombosNonRecursive(items)
    # testYieldAllCombos(items)
    
    testMaxValLarge(fastMaxVal)


if __name__ == '__main__':
    main()



























