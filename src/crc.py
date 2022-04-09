from helper import Helper
import numpy as np

helper = Helper()

class CRC:

    '''
        Initialize the value of the divisor depending on the CRC type.
    '''
    def __init__(self):
        self.crc_type = {
            'crc-4': '11111',
            'crc-8': '111010101',
            'rev-crc-16': '10100000000000011',
            'crc-16': '11000000000000101',
            'crc-24': '1100000000101000100000001',
            'crc-32': '100000100110000010001110110110111'
        }
    

    '''
        Perform XOR operation between the sub-dividend and divisor.
    '''
    def xor(self, sub_dividend: str, divisor: str) -> str:
        n = len(divisor)
        remainder = ''
        for i in range(n):                          # do XOR operation one-by-one bits.
            if sub_dividend[i] != divisor[i]:       # if the bit at the specific position between dividend and divisor is different, the result bit is 1.
                remainder += '1'                    # then, add bit '1' to the 'remainder' variable.
            else:                                   # if bits are the same then, the result bit is 0.
                remainder += '0'                    # then, add bit '0' to the 'remainder' variable.

        return remainder                            # return the remainder.


    '''
        This method is used to run the division operation using the xor() method.
    '''
    def mod2div(self, dividend: str, divisor: str) -> (str, str):
        quotient = ''
        remainder = ''
        f, i, j = 0, len(divisor), len(dividend)
        while i <= j:
            if dividend[f] != '0':                                          # if the first bit of the current dividend is not 0. 
                remainder = self.xor(dividend[f:i], divisor)                # then, do a division with the CRC divisor.
                quotient += '1'                                             # and update the quotient with bit 1.    
            else:                                                           # otherwise, if the first bit of the current dividend is 0. 
                remainder = self.xor(dividend[f:i], '0' * len(divisor))     # then, do a division with a serial bit of 0.
                quotient += '0'                                             # and update the quotient with bit 0. 
            dividend = dividend.replace(dividend[f:i], remainder)           # after getting the remainder, replace the dividend with the remainder for the sub-range.
            f, i = f + 1, i + 1                                             # update the range of the sub-dividend to calculate it in the next round. 

        return quotient, remainder[1:]
    

    '''
        The codeword generator for the sender.
    '''
    def crc_gen(self, dataword: list, word_size: int, crc_type: str) -> list:
        dataword = helper.insert_zeros(dataword, word_size, -1, 'one')
        
        divisor = self.crc_type[crc_type]                                                   # find the divisor which depends on the CRC type.
        dataword = ''.join([str(bit) for bit in dataword])                          
        remainder = self.mod2div(dataword + ('0' * (len(divisor) - 1)), divisor)[1]         # find the remainder value of the specific dataword.
        
        dataword += remainder                                                               # append the remainder to the dataword.
        return [int(bit) for bit in dataword]                                               # send the codeword out.


    '''
        The error checker for the receiver.
    '''
    def crc_check(self, codeword: list, crc_type: str) -> int:
        divisor = self.crc_type[crc_type]                                           # find the divisor which depends on the CRC type.
        codeword = ''.join([str(bit) for bit in codeword])                          
        remainder = self.mod2div(codeword, divisor)[1]                              # find the remainder value of the codeword.
        
        remainder = int(remainder, 2)                                               # convert the remainder to decimal numbers.
        return 1 if remainder == 0 else 0                                           # if the remainder is 0, no error occurs and return 1, otherwise, return 0 for the failure.


if __name__ == '__main__':
    pass