# checks

Numerical checks behind statements in `paper/`. Python 3 with numpy and scipy.
Each script prints what it checks; none writes to the repository. Dates are the
day the check was run and the statement entered.

| script | checks | statement |
|---|---|---|
| `ost_2d_scan.py` | OST cones; twisted Bell states (8 distinct); snake identity; grid over doubled qubit theories with the unit forced to a pole; admissible Frobenius forms (LP); a first random search over semisimple algebras | `paper/results-ost-2dUTFT.md` §3, §5; toolbox O13 |
| `ost_2d_search.py` | degenerate-limit trend of the doubling scan; handle element; random search over R²⊕C and R⁴ algebras with the Frobenius form fixed to the Bell cap | `paper/results-ost-2dUTFT.md` §5 |

Runtime: about six and five minutes respectively (2026-09-08). Not exhaustive;
the searches are evidence, not proof (see §5 of the result file).
