###############################################################################
#
# Pool - Data structure for qubit management in error corrected codes
#   Written and Designed by Aaron Vontell
#
#   Version 0.0.1
#
###############################################################################

class Pool:
    '''
    Represents a pool of qubits to be used as resources in quantum error
    correction. Manages the use and release of these qubit resources.
    '''
    
    def __init__(self, program):
        self.program = program;
    
    def replace_program(program):
        self.program = program
    
    def append_program(program):
        self.program += program
    
class LogicalQubit:
    '''
    Represents a logic qubit, which consists of one or more physical qubits
    '''
    
    def __init__(self, original_index):
        self.physicals = []
        self.original_index = original_index
    
class PhysicalQubit:
    
    def __init__(self):
        pass