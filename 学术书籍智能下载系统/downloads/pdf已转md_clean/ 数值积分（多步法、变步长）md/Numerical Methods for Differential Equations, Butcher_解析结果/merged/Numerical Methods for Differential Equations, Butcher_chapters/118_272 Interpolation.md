# 272 Interpolation

To obtain an approximation solution for a specific value of $x$ , it is possible to shorten the final step, if necessary, to complete the step exactly at the right place. However, it is usually more convenient to rely on a stepsize control mechanism that is independent of output requirements, and to produce required output results by interpolation, as the opportunity arises. The use of interpolation makes it also possible to produce output at multiple and arbitrary points. For the third order method introduced in Subsection 270, a suitable interpolation scheme is based on the third order Hermite interpolation formula using both solution and derivative data at the beginning and end of each step. It is usually considered to be an advantage for the interpolated solution to have a reasonably high order of continuity at the step points and the use of third order Hermite will give first order continuity. We will write the interpolation formula in the form

$$
\begin{array} { r l } & { y ( x _ { n - 1 } + h t ) \approx ( 1 + 2 t ) ( 1 - t ) ^ { 2 } y ( x _ { n - 1 } ) + ( 3 - 2 t ) t ^ { 2 } y ( x _ { n } ) } \\ & { \qquad + t ( 1 - t ) ^ { 2 } h y ^ { \prime } ( x _ { n - 1 } ) - t ^ { 2 } ( 1 - t ) h y ^ { \prime } ( x _ { n } ) . } \end{array}
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/35d8434cd222a65ca98f3c3abbb7739a1d14f2e0a351854bec22534ee0b981fd.jpg)  
Third order ARK method computations for the Kepler problem

To see how well the numerical method discussed in this section works in practice, it has been applied to the Kepler problem introduced in Subsection 101. For each of the eccentricity values chosen, denoted by $e$ , the problem has been scaled to an initial value

$$
\begin{array} { r } { y ( 0 ) = \Big [ 1 - e \quad 0 \quad 0 \quad \sqrt { ( 1 + e ) / ( 1 - e ) } \Big ] ^ { \top } , } \end{array}
$$

so that the period will be $2 \pi$ . The aim is to approximate the solution at $x = \pi$ for which the exact result is

$$
y ( \pi ) = { \Bigl [ } - 1 - e \quad 0 \quad 0 \quad - { \sqrt { ( 1 - e ) / ( 1 + e ) } } { \Bigr ] } ^ { \intercal } .
$$

In the first experiment, the problem was solved for a range of eccentricities $e = 0 , { \frac { 1 } { 2 } } , { \frac { 3 } { 4 } } , { \frac { 7 } { 8 } }$ with a tolerance of $T = 1 0 ^ { - 4 }$ . The results are shown in Figure 273(i) with all step points marked. The computed result for $x = \pi$ cannot be found from the variable stepsize schemes unless interpolation is carried out or the final step is forced to arrive exactly at the right value of $x$ . There was no discernible difference between these two half-period approximations, and their common values are indicated on the results.

The second experiment performed with this problem is to investigate the dependence on the accuracy actually achieved, as the tolerance is varied. The results achieved are almost identical for each of the eccentricities considered and the results will be reported only for $\textstyle e = { \frac { 7 } { 8 } }$ . Before reporting the outcome of this experiment, we might ask what might be expected. If we really were controlling locally committed errors, the stepsize would, approximately, be proportional to $T ^ { 1 / ( p + 1 ) }$ ; however, the contribution to global error, of errors committed within each small time interval, is proportional to $h ^ { p }$ . Hence we should expect that, for very small tolerances, the total error will be proportional to $T ^ { p / ( p + 1 ) }$ . But the controller we are using for the ARK method is not based on an asymptotically correct error estimate, and this will alter the outcome.

Global error and numbers of steps for varying tolerance with the Kepler problem   

<table><tr><td>T</td><td>|Error|l</td><td>Ratio</td><td>Steps</td></tr><tr><td>80</td><td>4.84285</td><td>3.94773</td><td>7</td></tr><tr><td>8-1</td><td>1.22674</td><td>3.71289</td><td>8</td></tr><tr><td>8-2</td><td>3.30401 1×10-1</td><td>3.98876</td><td>8</td></tr><tr><td>8-3</td><td>8.28328× 10-2</td><td>3.54007</td><td>10</td></tr><tr><td>8</td><td>2.33986 × 10-2</td><td>4.72504</td><td>13</td></tr><tr><td>8 -5</td><td>4.95205 × 10-3</td><td>4.73180</td><td>19</td></tr><tr><td>8-6</td><td>1.04655 × 10-3</td><td>4.65786</td><td>30</td></tr><tr><td>8-7</td><td>2.24684 × 10-4</td><td>4.58854</td><td>50</td></tr><tr><td>8-8</td><td>4.89663 × 10-5</td><td>4.78350</td><td>82</td></tr><tr><td>8-9</td><td>1.02365 × 10-5</td><td>4.75845</td><td>137</td></tr><tr><td>8-10</td><td>2.15123 × 10-6</td><td>4.74429</td><td>228</td></tr><tr><td>8-11</td><td>4.53436 × 10-7</td><td>4.73529</td><td>382</td></tr><tr><td>8-12</td><td>9.57567 × 10-8</td><td>4.76011</td><td>642</td></tr><tr><td>8-13</td><td>2.01165 × 10-8</td><td>4.75737</td><td>1078</td></tr><tr><td>8-14</td><td>4.22848 × 10-9</td><td></td><td>1810</td></tr></table>

In fact the results given in Table 273(I), for this third order method, do show an approximately two-thirds power behaviour. We see this by looking at the ratios of successive norm errors as $T$ is reduced by a factor of 8. Also included in the table is the number of steps. As $T$ becomes small, the number of steps should approximately double each time $T$ is decreased by a factor $\frac { 1 } { 8 }$ .
