# 392 Acceptance and rejection of steps

It is customary to test the error estimate in a step against $T$ and to accept the step only when the estimated error is smaller. To reduce the danger of rejecting too many steps, the safety factor in (391a) is inserted. Thus there would have to be a very large increase in the rate of error production for a step to be rejected. We now consider a different way of looking at the question of acceptance and rejection of steps. This is based on removing the safety factor but allowing for the possible acceptance of a step as long as the ratio of the error to the tolerance is not too great. We need to decide what ‘too great’ should mean.

The criterion will be based on attempting to minimize the rate of error production plus $T$ times the rate of doing work. Because we are considering the rejection of a completed step with size $h$ , we need to add the work already carried out to the computational costs in some way. Suppose that the error estimated for the step is $r ^ { - ( p + 1 ) } T$ , and that we are proposing to change the stepsize to $r h$ . This will mean that, until some other change is made, the rate of growth of error $+ \textit { T } \times$ work will be $T ( 1 + p ) / r h$ . By the time the original interval of size $h$ has been traversed, the total expenditure will be $T ( 1 + p ) / r h$ . Add the contribution from the work in the rejected step and the total expenditure will be $T ( ( p + 1 ) / r + p )$ .

If, instead, the step had been accepted, the expenditure (linear combination of error and work) would be $T ( r ^ { - ( p + 1 ) } + p )$ . Comparing the two results, we conclude that the step should be accepted if $r ^ { - ( p + 1 ) } \leq ( p + 1 ) / r$ , that is, when

Minimal value of stepsize ratio and maximal value of error/ $T$ for step acceptance   

<table><tr><td>p (p+1)-1/p</td><td>(p +1)(𝑝+1)/p</td></tr><tr><td>1</td><td>0.500 4.00</td></tr><tr><td>2 0.577</td><td>5.20</td></tr><tr><td>3</td><td>0.630 6.35</td></tr><tr><td>4 0.669</td><td>7.48</td></tr><tr><td>5 0.700</td><td>8.59</td></tr><tr><td>6 0.723</td><td>9.68</td></tr><tr><td>7 0.743</td><td>10.77</td></tr><tr><td>8 0.760</td><td>11.84</td></tr><tr><td>9 0.774</td><td>12.92</td></tr><tr><td>10 0.787</td><td>13.98</td></tr></table>

$$
r \geq ( p + 1 ) ^ { - 1 / p } ,
$$

and rejected otherwise. Looked at another way, the step should be accepted if the error estimated in a step, divided by the tolerance, does not exceed $( p + 1 ) ^ { ( p + 1 ) / p }$ . Values of $( p + 1 ) ^ { - 1 / p }$ and $( p + 1 ) ^ { ( p + 1 ) / p }$ are given in Table 392(I).
