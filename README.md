# ITCS323 - Computer Data Communication
## Intro
Class assignment to simulate the error control in the data link layer.
- Parity Check
- Cyclic Redundancy Check
- Checksum
- Hamming Code

### How to run
Extract the `src` folder and run the program using commands to run the python script.
i.e.,
    `python3 run.py`

### How to input
Basically, when the program is called, the program would ask the user to input the information to perform the calculation. Input lines might be different depending upon the method the user chooses.

## Input and Output
### Parity Check
#### Input:
- dataword: the dataword that the user needs to input can be a 1 or 2-dimensional array.
    - i.e., 1-dimension `dataword: 100101`
    - i.e., 2-dimension `dataword: 100101 110101 100001`
- word size: the word size used to adjust the number of bits of the dataword.
    - i.e., `word size: 8`
- parity type: used to determine what type of parity would be applied.
    - i.e., `parity type: one-even`
    - i.e., `parity type: two-odd`
- array size: array size is needed when a 2-dimension dataword is input to determine the row of the dataword array
    - i.e., `array size: 3`
    
#### Output:
- result: determine whether the codeword that sends to the receiver is lost the data or not, 1 no error and 0 for there is an error occurs.
    - i.e., `result: 1`



### Cyclic Redundancy Check
#### Input:
- dataword: the dataword that the user needs to input must be a 1-dimensional array.
    - i.e., 1-dimension `dataword: 100101`
- word size: the word size used to adjust the number of bits of the dataword.
    - i.e., `word size: 8`
- CRC type: used to determine what type of parity would be applied.
    - i.e., `CRC type: crc-4`
    - i.e., `CRC type: crc-8`

#### Output:
- result: determine whether the codeword that sends to the receiver is lost the data or not, 1 no error and 0 for there is an error occurs.
    - i.e., `result: 1`



### Hamming Code
#### Input:
- dataword: the dataword that the user needs to input must be a 1-dimensional array.
    - i.e., 1-dimension `dataword: 100101`

#### Output:
- result: determine whether the codeword that sends to the receiver is lost the data or not, 1 no error and the position on the dataword for there is an error occurs.
    - i.e., `result: 1`
    - i.e., `result: 7`



### Checksum
#### Input:
- dataword: the dataword that the user needs to input must be a 1-dimensional array.
    - i.e., 1-dimension `dataword: 100101`
- word size: the word size used to adjust the number of bits of the dataword.
    - i.e., `word size: 8`
- number of blocks: the number of the block the user wants to split the dataword into the section.
    - i.e., `number of blocks: 3`

#### Output:
- result: determine whether the codeword that sends to the receiver is lost the data or not, 1 no error and 0 for there is an error occurs.
    - i.e., `result: 1`
    - i.e., `result: 0`


