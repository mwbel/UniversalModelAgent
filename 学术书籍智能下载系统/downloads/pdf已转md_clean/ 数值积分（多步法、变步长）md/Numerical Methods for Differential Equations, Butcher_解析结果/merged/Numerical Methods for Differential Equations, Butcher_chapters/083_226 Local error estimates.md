# 226 Local error estimates

It is usually regarded as necessary to have, as an accompaniment to any numerical method, a means of assessing its accuracy, in completing each step it takes. The main reason for this is that the work devoted to each step, and the accuracy that is achieved in the step, should be balanced for overall efficiency. If the cost of each step is approximately constant, this means that the error committed in the steps should be approximately equal.

A second reason for assessing the accuracy of a method, along with the computation of the solution itself, is that it may be more efficient to change to a higher, or lower, member of the family of methods being used. The only way that this can really be decided is for the accuracy of a current method to be assessed and, at the same time, for some sort of assessment to be made of the alternative method under consideration. We discuss here only the local error of the current method.

It is not known how much a computed answer differs from what would correspond to the exact answer, defined locally. What is often available, instead, is a second approximation to the solution at the end of each step. The difference of these two approximations can sometimes be used to give quantitative information on the error in one of the two solution approximations.

We illustrate this idea in a single case. Suppose the method given by (222a) is used to give a starting value for the iterative solution of (225b). It is possible to estimate local errors by using the difference of these two approximations. We discuss this in more detail in the context of predictor–corrector Adams methods.

# Exercises 22

22.1 Assuming the function $f$ satisfies a Lipschitz condition and that $y$ , $y ^ { \prime }$ , $y ^ { \prime \prime }$ and $y ^ { \prime \prime \prime }$ are continuous, explain why the method given by (221a) and (221b) has order 2.

22.2 Explain why the method given by (222a) has order 2.

22.3 Find a method similar to (221a) and (221b), except that it is based on the mid-point rule, rather than the trapezoidal rule.

22.4 For a ‘quadrature problem’, $f ( x , y ) \quad = \quad \phi ( x )$ , compare the likely accuracies of the methods given in Subsections 221 and 222.

22.5 Verify your conclusion in Exercise 22.4 using the problem $y ^ { \prime } ( x ) = \cos ( x )$ on the interval $[ 0 , \pi / 2 ]$ .

22.6 Show that the backward difference method (225a) has order 2.

22.7 Calculate the solution to (203a) using the backward difference method (225a). Use $_ { n }$ steps with constant stepsize $\begin{array} { l l l } { h } & { = } & { \pi / n } \end{array}$ for $n =$ $2 ^ { \mathrm { { 0 } } } , 2 ^ { \mathrm { { 1 } } } , 2 ^ { \mathrm { { 2 } } } , \ldots , 2 ^ { \mathrm { { 1 0 } } }$ . Verify that second order behaviour is observed.
