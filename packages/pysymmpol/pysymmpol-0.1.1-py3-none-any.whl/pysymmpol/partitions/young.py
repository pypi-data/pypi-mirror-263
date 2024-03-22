from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import sympy as sp

'''
In this module we define 2 concepts that
are completely connected.

    1. First we define the class of Young (or Ferrers) Diagrams
    using the usual partition notation.

    2. Then we define the class of Conjugacy Classes.
'''

@dataclass(frozen=True)
class YoungDiagram:
    '''
    Represents Young diagrams in the standard
    partition notation: It is a monotonic decreasing sequence
    L = (L1, L2, L3, ...,Ln) with L1 >= L2 >=L3 >= ... >= Ln.

    Example: (3,2,2,1)
    '''
    _partition: tuple


    def __post_init__(self) -> None:

        '''
        Validade Young diagram:
        1) The argument must be monotonic decreasing.
        2) The argument is a tuple.
        '''

        # Validate _partition as a tuple
        if not isinstance(self.partition, tuple):
            raise TypeError(f"Argument must be a tuple, and you passed a {type(self._partition)}")

        # Validade if the partition is a monotonic decreasing sequence. 
        par = self._partition
        A = all([x >= y for x,y in zip(par, par[1:])])
        #A = all([self._partition[i+1] <= self._partition[i] for i in range(len(self._partition) -1)])

        if not A:
            raise ValueError("Argument must be a monotonic decreasing sequence.")
        

    @property
    def partition(self) -> tuple:
        '''
        Gives the partition notation for the Young diagram.
        '''
        return self._partition


    @property
    def rows(self) -> int:
        '''
        This gives the number of rows in the diagram.
        '''
        return len(self.partition)


    @property
    def columns(self) -> int:
        '''
        This gives the number of columns in the diagram.
        '''
        return self.partition[0]


    @property
    def boxes(self) -> int: 
        '''
        This gives the number of boxes in the diagram.
        '''
        return sum(self.partition)


    def draw_diagram(self, n: int=0) -> None:
        '''
        Pictorial representation of the Young/Ferrers diagram in
        French notation. 
        '''
        emo = ['■', '•', '🎲', '🎯', '#']
        for i in range(self.rows):
            if self.partition[-i-1] > 0:
                print(f"{emo[n]} " * self.partition[-i-1])


    def count_diagonal(self) -> int: 
        '''
        Gives the number of boxes in the diagonal.

        In order to do this calculation,
        the method represents the Young diagram as a 
        partition[0] x len(partition) matrix filled
        with 1 and 0. After that, it sums over the diagonal.
        '''

        matrix = np.zeros((self.rows, self.columns))

        diagonal = 0

        for row in range(self.rows):
            for column in range(self.partition[row]):
                matrix[row][column] = 1
        return int(np.trace(matrix))


    def frobenius_coordinates(self) -> list:
        '''
        Frobenius coordinates for a given partition.

        The minus in the definition below is related
        to the fact that python lists start at 0 and not 1.
        Moreover, the method uses the definition where the coordinates
        are half integers. 
        '''

        transposed_diagram = self.transpose().partition
        FrobCoor = []
        for i in range(self.count_diagonal()):
            FrobCoor.append([self.partition[i] - i - sp.Rational(1,2),
                             -(transposed_diagram[i] - i - sp.Rational(1,2))])
        return FrobCoor


    def transpose(self) -> YoungDiagram:
        '''
        Gives the transposed (or conjugate) Young diagram. 
        For example, the conjugate of [3,2] is [2,2,1].

        The algorithm follows the logic: 

        The method builds a list of zeros and length equal
        to the highest column: that is the partition[0].
        In our example: partition[0]=3, then [0,0,0]

        We now fill in the list defined above, we loop over
        the length of the original partition, in our case i =1, 2

        transposed_diagram = [0,0,0]

        - loop 01: (i, row_length) = (0,3) => j =0,1,2. 
                j = 0 transporsed_diagram[0] = 1
                j = 1 transposed_diagram[1] = 1
                j = 2 transposed diagram[2] = 1
        and now we have transposed_diagram = [1,1,1]
        - loop 02 (i, row_length) = (1, 2) => j =0,1
                j = 0 transposed_diagram[0] = 2
                j = 1 transposed_diagram[0] = 2
        and now we have transposed_diagram = [2,2,1]
        '''
        transposed_diagram = [0] * (self.partition[0])

        for i, row_length in enumerate(self.partition):
            for j in range(row_length):
                transposed_diagram[j] += 1

        transposed_diagram_tuple = tuple(transposed_diagram)

        return YoungDiagram(transposed_diagram_tuple)


    def contains(self, other_young: YoungDiagram) -> bool:
        '''
        Checks if the original partition contains the new one.
        '''

        # Create some lists to concatenate these objects. 
        partition = self.partition
        other_partition = other_young.partition

        # Pad some zeros to write the two partitions in the same form (length).
        if len(other_partition) < len(partition):
            other_partition += (0,)*abs(len(partition) - len(other_partition))
        elif len(other_partition) > len(partition):
            partition += (0,)*abs(len(partition) - len(other_partition))

        sub_partition_condition = [x >= y for x, y in zip(partition, other_partition)]

        if all(sub_partition_condition):
            return True
        else:
            return False


    def interlaces(self, other_young: YoungDiagram) -> bool:
        '''
        Checks if the original partition interlaces the new one.
        '''

        # Create some lists because I need to concatenate these objects. 
        partition = self.partition
        other_partition = other_young.partition

        # Here I pad some zeros to write the two partitions in the same form (length).
        if len(other_partition) < len(partition):
            other_partition += (0,)*abs(len(partition) - len(other_partition))
        elif len(other_partition) > len(partition):
            partition += (0,)*abs(len(partition) - len(other_partition))

        interlacing_condition   = [x >= y for x, y in zip(other_partition, partition[1:])]

        if self.contains(other_young) and all(interlacing_condition):
            return True
        else:
            return False


    def conjugacy_partition(self) -> dict:
        '''
        Converts the partition notation to 
        the conjugacy class notation
        Example:
        [4,4,4,2,2,1] to {1: 1, 2: 2, 3: 0, 4: 3}.

        The algorithm works as follows:

        It creates a list of zeros with length equal
        to the largest row. In our case, 4
        conjugacy = [0, 0, 0, 0].

        It iterates over the partition, adding 1s to the
        corresponding slot in the conjugacy vector, for example
        partition (4,4,4,2,2,1) gives
        - loop 01: i = 4
            conjugacy[3] = 1
            conjugacy = [0,0,0,1]
        - loop 02: i = 4
            conjugacy[3] = 2
            conjugacy = [0,0,0,2]
        - loop 03: i = 4
            conjugacy[3] = 3
            conjugacy = [0,0,0,3]
        - loop 04: i = 2
            conjugacy[1] = 1
            conjugacy = [0,1,0,3]
        - loop 05: i = 2
            conjugacy[1] = 2
            conjugacy = [0,2,0,3]
        - loop 06: i = 1
            conjugacy[0] = 1
            conjugacy = [1,2,0,3]

        At the end we convert to a dictionary, and
        conjugacy = {1: 1, 2: 2, 3: 0, 4: 3}
        '''

        length = self.partition[0]
        conjugacy = [0]*length

        for i in self.partition:
            conjugacy[i-1] += 1

        # We finally create a dictionary for the conjugacy class
        conjugacy_class = dict(enumerate(conjugacy,1)) 

        return conjugacy_class
