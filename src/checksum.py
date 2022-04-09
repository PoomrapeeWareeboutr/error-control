from helper import Helper
import numpy as np

helper = Helper()

class Checksum:
    
    '''
        The method to do a 1's complement operation of a bits sequence.
    '''
    def ones_complement(self, checksum: list) -> list:
        for i in range(len(checksum)):
            checksum[i] = (checksum[i] + 1) % 2     # make a bit to an opposite value, 0 -> 1 and 1 -> 0 
        return checksum                             
    

    '''
        Summation operation of the checksum method.
    '''
    def addition(self, dataword: list, word_size: int, num_blocks: int) -> list:
        checksum = '0'                                                  # initialize the checksum value.
        for i in range(num_blocks):
            checksum = bin(int(''.join([str(bit) for bit in dataword[i]]), 2) + int(checksum, 2)) # perform addition for each dataword.
            
            current_size = len(checksum[2:])
            if current_size > word_size:                                # check whether the dataword size exceeds the limit number or not. if true, go to this branch. 
                exceed = current_size - word_size                          
                checksum = checksum[2 + exceed:]                        # split the bit that exceeds out of the checksum.
                remainder = checksum[2:2 + exceed]                      # save the exceeded bit into the 'remainder' variable.
                
                checksum = bin(int(checksum, 2) + int(remainder, 2))    # perform the add operation again between the checksum and the remainder.
        
        checksum = [int(bit) for bit in checksum[2:]]                   # convert checksum string to a bits array.
        return checksum


    '''
        Checksum generator (for the sender).
    '''
    def checksum_gen(self, dataword: list, word_size: int, num_blocks: int) -> list:
        dataword = helper.insert_zeros(dataword, word_size, -1, 'one')

        word_size = len(dataword) // num_blocks
        dataword = np.array_split(dataword, num_blocks)                 # split dataword into m blocks of the data.
        dataword = [bit.tolist() for bit in dataword]       
        
        checksum = self.addition(dataword, word_size, num_blocks)       # perform addition between each dataword in the array.
        checksum = helper.insert_zeros(checksum, word_size, len(dataword[0]), 'one') # if the number of bits is not equal to word size then, insert 0 at the front to reach that number. 
        
        dataword.append(self.ones_complement(checksum))                 # add the checksum value to the end of the dataword and send it out.
        return dataword

    
    '''
        Checksum checker (for the receiver).
    '''
    def checksum_check(self, codeword: list, word_size: int, num_blocks: int) -> int:
        checksum = self.addition(codeword, word_size, num_blocks)       # bring a codeword that contains the checksum value to perform the addition to find checksum again.
        checksum = helper.insert_zeros(checksum, word_size, len(codeword[0]), 'one') # if the number of bits is not equal to word size then, insert 0 at the front to reach that number.
        
        checksum = self.ones_complement(checksum)                       # do 1's complement of the checksum.
        for bit in checksum:
            if bit == 1:                                                
                return 0                                                # if the checksum didn't be all 0 bits then, the error occurs. then, return 0.
        return 1                                                        # if it's all 0, no error occurs.


if __name__ == '__main__':
    pass

    