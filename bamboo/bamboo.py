###############################################################################
#
# Bamboo - An error correction library for Rigetti Computing
#   Written and Designed by Aaron Vontell
#
#   Version 0.0.1
#
###############################################################################

import Pool

class Bamboo:
    
    def __init__(self, pool=None, gates=None, optimized=True):
        self.pool = Pool()
        self.gates = gate
        self.optimized = optimized
        
    ### Methods to be used in quantum error correction by the user ############
    
    def bit_flip_3_code(self, program):
        pass
    
    def sign_flip_3_code(self, program):
        pass
    
    def shor_code(self, program):
        signed = self.sign_flip_3_code(program)
        bitted = self.bit_flip_3_code(program)
        return bitted
    
    ### Private methods to be used by the Bamboo class ########################    