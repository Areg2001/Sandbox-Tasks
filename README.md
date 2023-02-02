#Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numpy.

```bash
pip install numpy
```
##BitVector

A data structure consisting of a collection of bits.

##Usage

```python
# create bitvector
bitvector = BitVector(size)

# convert 0 -> 1
bitvector.set(index)

# convert 1 -> 0
bitvector.reset(index)
```
