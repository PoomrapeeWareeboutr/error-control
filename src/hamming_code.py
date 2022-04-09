from helper import Helper
import numpy as np

helper = Helper()

class HammingCode:

    '''
        Find bits from corresponding specific positions and perform the parity operation.
    '''
    def find_parity(self, dataword: list, pos: int) -> int:
        bit = 0
        window = pos + 1                            # determine the size of the window.
        front, rear = window + pos - 1, pos         # assign the value of front and rear depending on the window size.
        for i in range(pos, len(dataword)):         
            if rear <= i <= front:                  # if the current bit is in the window that means this bit has correspond to the redundant bit.
                bit = (bit + dataword[i]) % 2       # then, perform the parity operation by counting bits.
            if i == front:                          # if the current index reaches the border of the window then, the window will move to the next corresponding position.
                rear = window + front + 1
                front = window + rear - 1
        
        return bit


    '''
        Codeword generator using Hamming Code (for the sender)
    '''
    def hamming_gen(self, dataword: list) -> list:
        r = 0                                       # the number of parity bit should be insert to the dataword.
        m = len(dataword)                           # length of the dataword.
        while 2**(r) < m + r + 1:                   # calculate the number of redundant bit.
            r += 1
        
        dataword = dataword[::-1]                   
        for pos in range(r):                        # insert parity bit at the specific position in the dataword.
            dataword.insert(2**(pos) - 1, 0)
        
        for pos in range(r):                        # at the parity bit position, find the value of that parity bit.
            index = 2**(pos) - 1
            dataword[index] = self.find_parity(dataword, index)
        
        dataword = dataword[::-1]
        return dataword                             # return the data along with inserted parity bits.

        
    '''
        Codeword checker using Hamming Code (for the receiver)
    '''
    def hamming_check(self, codeword: list) -> list:
        codeword = codeword[::-1]
        res, pos = list(), 0
        for i in range(len(codeword)):      # travel through the codeword and find the position of parity bits.
            if i == 2**(pos) - 1:           # if the current index matches the parity bit position then check the parity condition.
                res.insert(0, str(self.find_parity(codeword, i))) # find the value of the specific parity bit and keep it to the 'res' variable.
                pos += 1

        res = ''.join(res)                         
        res = int(res, 2)                   # convert the sequent bits gathered from the parity position to the decimal number.
        return -1 if res == 0 else res      # if the result is 0 that means has no error occurs then, return -1, otherwise, the error appears and returns the position of that error.


if __name__ == '__main__':
    pass
    


    


    