[//]:#(gvim: set fileencoding=utf8)

# Some Recursive Search Engines for Python

(c) [José Martinez](<jose.martinez@polytech.univ-nantes.fr>), [Polytech Nantes](https://polytech.univ-nantes.fr/), [Nantes University](https://www.univ-nantes.fr), All rights reserved

The use of this library is not authorised outside the Polytechnic School of Nantes University.

---

This is a fast translation of the code written previously in Prolog then in Haskell.
The full documentation is available for the Haskell version.
There is also a few more examples in the Haskell ancestor.
Finally, the Haskell code is unit-tested.
Therefore, the Python version might contain (more?!) bugs ...


## HISTORY

   * March 2019:  Starting the translation from the Haskell version
   * July 2023:  "Finishing" the translation from the Haskell version

## SOLVERS

There are a few solvers, in order of complexity:

   * naïve,
   * depth-limit,
   * directed cycle detection,
   * branch-and-bound,
   * IDS,
   * IDA, or IDA star when a non-null heuristic is used.

The last two are based respectively on depth-limit and branch-and-bound using a deepening strategy provided by a meta-solver.

### EXAMPLES

The few accompanying examples allow to somehow test most of the solvers, namely the first five.

---

