# 105 The Van der Pol equation and limit cycles

The simple pendulum, which we considered in Subsection 103, is a non-linear variant of the ‘harmonic oscillator’ problem $y ^ { \prime \prime } = - y$ . We now consider another non-linear generalization of this problem, by adding a term $\mu ( 1 - y ^ { 2 } ) y ^ { \prime }$ , where $\mu$ is a positive constant, to obtain the ‘Van der Pol equation’

$$
y ^ { \prime \prime } ( x ) = \mu ( 1 - y ( x ) ^ { 2 } ) y ^ { \prime } ( x ) - y ( x ) .
$$

This problem was originally introduced by Van der Pol (1926) in the study of electronic circuits. If $\mu$ is small and the initial values correspond to what would be oscillations of amplitude less than 1, if $\mu$ had in fact been zero, it might be expected that the values of $y ( x )$ would remain small for all time.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/9a820c6fc1eaef1cbfd02b7f60788ec1fd057c1012e38c22156231684395b250.jpg)  
Van der Pol problem with $\mu = 1$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/b1ba043a959e999472da09e63135e7a0477bbce6fcd75fa3e3737348af023087.jpg)  
Van der Pol problem with $\mu = 3$

However, the non-linear term has the effect of injecting more ‘energy’ into the system, as we see by calculating the rate of change of $E = { \textstyle { \frac { 1 } { 2 } } } y ^ { \prime } ( x ) ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } y ( x ) ^ { 2 }$ . This is found to be

$$
{ \frac { d } { d x } } \left( { \frac { 1 } { 2 } } y ^ { \prime } ( x ) ^ { 2 } + { \frac { 1 } { 2 } } y ( x ) ^ { 2 } \right) = \mu ( 1 - y ( x ) ^ { 2 } ) y ^ { \prime } ( x ) ^ { 2 } > 0 ,
$$

as long as $| y | < 1$

Similarly, if $| y |$ starts with a high value, then $E$ will decrease until $| y | = 1$ . It is possible to show that the path, traced out in the $( y , y ^ { \prime } )$ plane, loops round the origin in a clockwise direction forever, and that it converges to a ‘limit cycle’ $-$ a periodic orbit. In Figure 105(i), this is illustrated for $\mu = 1$ . The path traced out in the $( y , y ^ { \prime } )$ plane moves rapidly towards the limit cycle and is soon imperceptibly close to it. In Figure 105(ii), the case $\mu = 3$ is presented.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/3f5f7d41743489e31437a4f24ad6d3fa6d191ba62a632e88f3f42996aa008430.jpg)  
Phase diagram for Lotka–Volterra solution with $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$ , together with seven alternative orbits

Of special interest in this problem, especially for large values of $\mu$ , is the fact that numerical methods attempting to solve this problem need to adjust their behaviour to take account of varying conditions, as the value of $1 - | y ( x ) | ^ { 2 }$ changes. The sharp change of direction of the path traced out near $( y , y ^ { \prime } ) ~ = ~ ( \pm 2 , 0 )$ for the $\mu ~ = ~ 3$ case, a phenomenon which becomes more pronounced as $\mu$ is further increased, is part of the numerical difficulty associated with this problem.
