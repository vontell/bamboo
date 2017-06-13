# Bamboo
Bamboo is a library which works with pyQuil and Grove from Rigetti Computing to provide error correction. Methods are provided to convert original Quil programs into error-corrected Quil programs, through basic methodologies such as the Shor code to more complicated error correction methods such as CSS codes.

Welcome to the world of fault tolerant quantum computing!

## Usage and Examples

The Bamboo library is made to take previously defined pyQuil Program objects and output an error corrected version. You can use a specific error correction scheme if you have one in mind, or alternatively ask for a certain level of protection. For example:

```python

from grove import teleportation

bamboo = Bamboo()
bell_pair = teleportation.make_bell_pair(0, 1)

# Use a specific error correcting code
ft_bell_pair = bamboo.bit_flip_3_code(bell_pair)

# Alternatively, ask for certain protection
pr_bell_pair = bamboo.protect(bit_flips=1, sign_flips=0)

```