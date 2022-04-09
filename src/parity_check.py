from helper import Helper
import numpy as np

helper = Helper()

class ParityCheck:
    
    '''
        This method finds the parity bit that should add at the end of the dataword.
    It's depend on the type of the parity check which passes to the parameter 
    of the function.
    '''
    def find_parity_bit(self, dataword: list, context: str) -> int:
        bit = dataword.count(1) % 2         # if the number of bit 1 modulo by 2 is equal to 0 that means, the number of bit is even.
        if context == 'odd':                # if the type of parity check is odd then, make the bit be opposite by plus 1 and modulo by 2 again.
            bit = (bit + 1) % 2             
        return bit                          # return the parity bit that should add in the dataword.
    

    '''
        The function is to check whether the error occurs or not by bringing the parity 
    bit of the codeword compared with a type of parity.
    '''
    def is_error(self, bit: int, context: str) -> bool:
        if not bit:                         # if the bit is 0.
            if context == 'odd':            # then, check the type is odd parity or not if yes, error is occured.
                return True                 
        else:                               # else if the bit is 1
            if context != 'odd':            # then, check the type is even parity or not if yes, error is occured.
                return True                 
        return False                        # if the program has not entered any condition branch that means there is no error.

    
    '''
        The function to wrap a dataword to a codeword before send to the physical layer.
    This function also known as the generator (for the sender).
    '''
    def parity_gen(self, dataword: list, word_size: int, parity_type: str, array_size: int) -> list:
        dim, context = parity_type.split('-')       # split the parity_type variable to dim (dimension) and context (type of the parity) variable.

        # for 1 dimension
        if dim == 'one':                                                # if the dimension of the dataword is 1D, the program will go into this condition.
            dataword = helper.insert_zeros(dataword, word_size, -1, 'one')
            dataword.append(self.find_parity_bit(dataword, context))    # find and add the parity bit at the end of the dataword.
            return dataword                                             # return the dataword along with extra bit AKA codeword.
        
        # for 2 dimension
        dataword = helper.insert_zeros(dataword, word_size, array_size, 'two')
        for i in range(array_size):
            dataword[i].append(self.find_parity_bit(dataword[i], context)) # find parity bits of each row and add it at the end of the row.
        
        extra_codeword = list()
        dataword = np.asarray(dataword)
        for i in range(word_size + 1):
            extra_codeword.append(self.find_parity_bit(dataword[:,i].tolist(), context)) # find parity bits of each column and add it to the new extra codeword.
        
        dataword = dataword.tolist()
        dataword.append(extra_codeword)     # add the new codeword at the end of dataword.
        return dataword                     # return a new dataword as codeword.

    
    '''
        The function to receive the codeword and detect whether the dataword lost the correctness or not.
    Also known as the checker (for the receiver).
    '''
    def parity_check(self, codeword: list, parity_type: str, array_size: int) -> int:
        dim, context = parity_type.split('-')       # split the parity_type variable to dim (dimension) and context (type of the parity) variable.
        
        # for 1 dimension
        if dim == 'one':                            # if the dimension of the dataword is 1D, the program will go into this condition.
            bit = codeword.count(1) % 2             # count bits and see a number of bit 1 is even or odd if even bit = 0, otherwise bit = 1.
            if self.is_error(bit, context):         # send 'bit' along with 'context' to the function 'is_error' to check the error is occur or not.
                return 0                            # if function return true it means error so, the program return 0.
            return 1                                # otherwise, no error return 1.
        
        # for 2 dimension
        codeword = np.asarray(codeword)
        for i in range(array_size):
            bit = codeword[i,:].tolist().count(1) % 2   # count bits in **row aspect** and see a number of bit 1 is even or odd if even bit = 0, otherwise bit = 1.
            if self.is_error(bit, context):             # send 'bit' along with 'context' to the function 'is_error' to check the error is occur or not.
                return 0                                # if function return true it means error so, the program return 0.
        
        for i in range(len(codeword[0])):
            bit = codeword[:,i].tolist().count(1) % 2   # count bits in **column aspect** and see a number of bit 1 is even or odd if even bit = 0, otherwise bit = 1.
            if self.is_error(bit, context):             # send 'bit' along with 'context' to the function 'is_error' to check the error is occur or not.
                return 0                                # if function return true it means error so, the program return 0.
        
        return 1                                        # in the case of the program reach at this line so, the data that receive from the sender has no error


if __name__ == '__main__':
    pass