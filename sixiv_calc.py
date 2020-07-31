import random
import numpy as np


class BreedCalculator:

    def __init__(self, parent_1=None, parent_2=None):
        '''
        Call BreedCalculator to calculate the probability of having a perfect 6 IV child Pokémon
        given the IVs of parent Pokémon holding Destiny Knot. Breeding technique for Pokemon Sword and Shield.
        Parent IVs must be given as lists that contain 6 ints that go from 1 to 6. Being the following:

        'No Good' = 1
        'Decent' = 2
        'Pretty good' = 3
        'Very Good' = 4
        'Fantastic' = 5
        'Best' = 6
        Example:

        parent_1 = [6, 6, 6, 6, 6, 6]
        parent_2 = [6, 6, 6, 6, 6, 6]
        '''
        self.parent_1 = parent_1
        self.parent_2 = parent_2

        if parent_2 is None:
            self.parent_2 = [6, 6, 6, 6, 6, 6]
        if parent_1 is None:
            self.parent_1 = [6, 6, 6, 6, 6, 6]

    def combination(self):
        child = []
        random_spec = random.randint(0, 5)
        for i in range(6):
            rand_par = random.randint(1, 2)
            if rand_par == 1:
                child.append(self.parent_1[i])
            else:
                child.append(self.parent_2[i])

        child[random_spec] = random.randint(1, 6)
        return child

    def sim(self, n=100000):
        com_str = []
        for i in range(n):
            result = ' '.join(str(i) for i in self.combination())
            com_str.append(result)
        return com_str

    def prob(self, n=100000):
        values, counts = np.unique(self.sim(), return_counts=True)
        p = counts[-1] / n
        if values[-1]  == '6 6 6 6 6 6':
            return 'Perfect IV hatch probability: {} %'.format(round(p * 100, 2))
        else:
            return 'Perfect IV hatch probability: {} %'.format(0)

p1 = [6,6,6,6,6,6]
p2 = [6,6,6,6,6,6]
calc = BreedCalculator(parent_1=p1, parent_2=p2)

print(calc.prob())
