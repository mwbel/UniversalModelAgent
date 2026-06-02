# 247 Numerical examples

Using the starting process described in Subsection 246, and a range of orders, the same test problem as was used in Subsection 239, that is, (201d) with $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ , was solved for PEC and PECE Adams methods. The errors generated for these methods are shown in Figures 247(i) (PEC methods) and 247(ii) (PECE methods). The orders are attached to the curves. Note that, at least for this problem, the two modes have almost identical errors. This means, perhaps, that the extra cost of PECE methods is not justified. However, for large stepsizes, there is an advantage in PECE methods because many types of unstable behaviour exhibit themselves more severely for PEC methods. For example, the iterative starting procedure that we have used, failed to converge for large stepsizes (not shown in the diagrams). This effect persisted for a larger range of stepsizes for PEC methods than was the case for PECE methods.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/5494bcf92a7d4a8c5fbd9582959ba818cc37b03bd70df79100959d8ada89343b.jpg)  
Orbital calculations for various PECE methods

# Exercises 24

24.1 Find a linear multistep method of order 3 of the form

$$
y _ { n } = y _ { n - 2 } + \beta _ { 1 } h f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } h f ( x _ { n - 2 } , y _ { n - 2 } ) + \beta _ { 3 } h f ( x _ { n - 3 } , y _ { n - 2 } ) .
$$

24.2 Find a linear multistep method of order 3 of the form

$$
y _ { n } = y _ { n - 2 } + \beta _ { 0 } h f ( x _ { n } , y _ { n } ) + \beta _ { 1 } h f ( x _ { n - 1 , y _ { n - 1 } } ) + \beta _ { 2 } h f ( x _ { n - 2 } , y _ { n - 2 } ) .
$$

24.3 If the differential equation $y ^ { \prime } = y$ is solved using the implicit method $y _ { n } = y _ { n - 2 } + 2 h f ( x _ { n - 1 } , y _ { n - 1 } )$ , show that the resulting difference equation has a solution which grows in powers of $1 + h + \textstyle { \frac { 1 } { 2 } } h ^ { 2 } + O ( h ^ { 3 } )$ and a second solution that grows in powers of a quantity with smaller magnitude.

24.4 If the differential equation $y ^ { \prime } = - y$ is solved using the same method, show that the resulting difference equation has a solution which grows in powers of $\textstyle 1 - h + { \frac { 1 } { 2 } } h ^ { 2 } + O ( h ^ { 3 } )$ but has a second solution that grows in powers of a quantity with greater magnitude.
