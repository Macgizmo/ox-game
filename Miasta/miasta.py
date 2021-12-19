city1={'yes':250, 'no': 138, 'none': 17}
city2={'yes':193, 'no': 232, 'none': 16}
import collections
counter1 = collections.Counter(city1)
counter2 = collections.Counter(city2)
counter3 = counter1 + counter2
print(counter3)
#%%

city1={'yes':250, 'no': 138, 'none': 17}
city2={'yes':193, 'no': 232, 'none': 16}
import collections
counter1 = collections.Counter(city1)
counter2 = collections.Counter(city2)
counter3 = counter1 + counter2
print(counter3['yes'])
