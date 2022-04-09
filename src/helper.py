import numpy as np
np.warnings.filterwarnings('ignore', category = np.VisibleDeprecationWarning)   # ignore the warning when the program uses np.insert() function.

class Helper:

    ''' 
        Function to insert bits if word size of dataword is less than the provided word size.
    '''
    def insert_zeros(self, dataword: list, word_size: int, array_size: int, dim: str) -> list:
        dataword = np.asarray(dataword)
        # for 1 dimension dataword, go to this condition.
        if dim == 'one':                                
            current_size = len(dataword)
            if current_size < word_size:        # if the current word size of the 1D dataword is less than provided word size then appends it at the front until it is equivalent.            
                dataword = np.insert(dataword, 0, np.zeros(word_size - current_size)).tolist() # insert bit '0' at the front.
            
            return dataword                     # return the new 1 dimension dataword along with the inserted bits.
        
        # for 2 dimension dataword, gonna fall into this branch.
        dataword = dataword.tolist()       
        for i in range(array_size):
            current_size = len(dataword[i])
            if current_size < word_size:        # if the current word size of the dataword[i] is less than provided word size then appends it at the front until it is equivalent.
                dataword[i] = np.insert(np.asarray(dataword[i]), 0, np.zeros(word_size - current_size)).tolist() # insert bit '0' at the front into the row to match the condition of word size.
        
        return dataword                         # return the new 2 dimension dataword.
    

    '''
        The function is to convert a binary list to a binary string.
        (list -> string)
    '''
    def binary_string(self, binary: list, dim: str) -> str:
        # for 1 dimension array goes here.
        if dim == 'one':
            return ''.join([str(bit) for bit in binary])

        # for 2 dimension array.
        for i in range(len(binary)):
            binary[i] = ''.join([str(bit) for bit in binary[i]])
        return ' '.join(seq for seq in binary)

    
    '''
        The method to convert a binary string to a binary list.
        (string -> list)
    '''
    def binary_list(self, binary: str or list, dim: str) -> list:
        # for 1 dimension array goes here.
        if dim == 'one':
            return [int(bit) for bit in binary]

        # for 2 dimension array.
        for i in range(len(binary)):
            binary[i] = [int(bit) for bit in binary[i]]
        return binary


if __name__ == '__main__':
    pass
    