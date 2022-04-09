from helper import Helper
from parity_check import ParityCheck
from hamming_code import HammingCode
from checksum import Checksum
from crc import CRC

helper = Helper()

class ErrorControl:
    
    def __init__(self):
        self.method = (
            'parity',
            'crc',
            'checksum',
            'hamming-code'
        )
    

    ''' The function is to ask the user when they wants to change the codeword. '''
    def ask_codeword(self) -> chr:
        change = ''
        while change != 'y' and change != 'n':
            change = input('do you want to change codeword? (y/n): ')
            change = change.lower()
        return change


    ''' Call the Parity Check function. '''
    def run_parity(self) -> None:
        err = ParityCheck()
        dataword = input('dataword: ')
        word_size = int(input('word size: '))
        parity_type = input('parity type: ')
        array_size = int(input('array size: '))

        dim = parity_type.split('-')[0]
        if dim == 'one':
            dataword = helper.binary_list(dataword, dim)
        else:
            dataword = helper.binary_list(dataword.split(' '), dim)
        
        codeword = err.parity_gen(dataword, word_size, parity_type, array_size)
        print('codeword: ' + helper.binary_string(codeword[:], dim))

        change = self.ask_codeword()
        if change == 'y':
            codeword = input('codeword: ')
            if dim == 'one':
                codeword = helper.binary_list(codeword, dim)
            else:
                codeword = helper.binary_list(codeword.split(' '), dim)
        
        res = err.parity_check(codeword, parity_type, array_size + 1)
        print('result: ' + str(res))
    

    ''' Call the CRC function. '''
    def run_crc(self) -> None:
        err = CRC()
        dataword = input('dataword: ')
        word_size = int(input('word size: '))
        crc_type = input('crc-type: ')

        codeword = err.crc_gen(helper.binary_list(dataword, 'one'), word_size, crc_type)
        print('codeword: ' + helper.binary_string(codeword[:], 'one'))
        
        change = self.ask_codeword()
        if change == 'y':   
            codeword = input('codeword: ')
            codeword = helper.binary_list(codeword, 'one')

        res = err.crc_check(codeword, crc_type)
        print('result: ' + str(res))


    ''' Call the Checksum function. '''
    def run_checksum(self) -> None:
        err = Checksum()
        dataword = input('dataword: ')
        word_size = int(input('word size: '))
        num_blocks = int(input('number of block: '))

        codeword = err.checksum_gen(helper.binary_list(dataword, 'one'), word_size, num_blocks)
        print('codeword: ' + helper.binary_string(codeword[:], 'two'))
        
        change = self.ask_codeword()
        if change == 'y':   
            codeword = input('codeword: ')
            codeword = helper.binary_list(codeword.split(' '), 'two')
        
        res = err.checksum_check(codeword, word_size, num_blocks + 1)
        print('result: ' + str(res))


    ''' Call the Hamming Code function. '''
    def run_hamming(self) -> None:
        err = HammingCode()
        dataword = input('dataword: ')
        
        codeword = err.hamming_gen(helper.binary_list(dataword, 'one'))
        print('codeword: ' + helper.binary_string(codeword[:], 'one'))
        
        change = self.ask_codeword()
        if change == 'y':
            codeword = input('codeword: ')
            codeword = helper.binary_list(codeword, 'one')
        
        res = err.hamming_check(codeword)
        print('result: ' + str(res))


    ''' The main function is run the application. '''
    def run(self) -> None:
        
        while True:
            func = ''
            while func not in self.method:
                func = input('method: ').lower()
            
            if func == 'parity':
                self.run_parity()
            elif func == 'crc':
                self.run_crc()
            elif func == 'checksum':
                self.run_checksum()
            elif func == 'hamming-code':
                self.run_hamming()
            
            cont = ''
            while cont != 'y' and cont != 'n':
                cont = input('do you want to run the program again? (y/n): ').lower()
            
            if cont == 'n':
                break
            
            print()

    
if __name__ == '__main__':
    app = ErrorControl()
    app.run()
