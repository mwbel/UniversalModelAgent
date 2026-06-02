# 237 Implicit Runge–Kutta methods

Implicit methods have the potential advantage, compared with explicit methods, that there will be fewer stages for the same order. The disadvantage is in the implicit nature of at least some of the stages. This makes it impossible to avoid iterative methods of evaluation. For the purpose of experimental comparison with explicit methods, we present here just three methods:

<table><tr><td>1 1</td><td>1 1 3</td><td>0 0 4</td></tr><tr><td>3-2√2 1</td><td>5- -3√2 4 1+√2 4</td><td>7- -5√2 4 3-√2 4 3-√2</td></tr><tr><td></td><td>1+√2 4</td><td>4 1 √ 6</td></tr><tr><td>G A +</td><td>14+ 1 1</td><td>1 1</td></tr></table>

It can be verified that (237a) has order 3, (237b) has order only 2 and (237c) has order 4. In the implicit case, the cost of using a specific method depends not so much on the number of stages, as on the difficulty in evaluating the stages. From this point of view, (237a) is the easiest to use because only one of the stages is implicit; (237b) and (237c) each have two interconnected implicit stages but, as we will see in Subsection 363, the order 2 method (237b) can be implemented more cheaply than (237c).
