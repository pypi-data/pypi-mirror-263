This package is intended to operate as a simple intuitive interface for handling laborious elementary set theory calculations.
The goal is to make all operations on sets feel intuitive and number like (similar to MATLAB's handling of matrices)!

*********************Installation*********************
Ensure that Python is installed on your machine then run `pip install SetCalcPy`
Invoke `import SetCalcPy` in your file or console!
Enjoy!

*********************Simple Operations*********************
+ Declare sets like so `A = Set(1,2,3)` and `B = Set(1,2,Set(3,4))
+ Take the union of two sets (find all elements in `A` or `B`): `A + B`
+ Take the intersection of two sets (find all elements in `A` and `B`): `A & B`
+ Take the disjoint of two sets (find all elements in `A` but not `B`): `A - B`
+ Find the powerset of a set (all subsets of `A`): `A.powerSet()`
+ Calculate the cartesian product of two or more sets: `A * B` or `A.cartesianProduct(*sets to multiply by*)`
+ Find the complement of a set (all elements in the universe specified but not in `A`): `A.complement()`

*********************Other Features*********************
- Iterate through sets just like lists
- Access elements just like lists (the first element of `A` is `A[0]`)
- Test set equality: `A == B`
- Convert to a list: `A.__list__()`
- Check for membership: `1 in A` evaluates to True because 1 is an element of `A`
- Check length: `len(A)`

*********************Change Log*********************
- Fixed issue when printing Sets containing tuples with Sets where Sets would not display properly
- Fixed miscalculation bug with the cartesian product
- Fixed issues with Sets containing strings