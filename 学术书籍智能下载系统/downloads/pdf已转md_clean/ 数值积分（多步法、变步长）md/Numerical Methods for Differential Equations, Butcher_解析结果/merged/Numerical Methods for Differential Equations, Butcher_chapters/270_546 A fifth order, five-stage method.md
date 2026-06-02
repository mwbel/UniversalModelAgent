# 546 A fifth order, five-stage method

We will consider a special method constructed using a more general formulation of fourth order methods in which there is an additional fifth stage. There is enough freedom to ensure that the error constants are zero. This does not mean that, regarded as an ARK method, a method constructed this way has fifth order, because the trivial rescaling normally used to achieve variable stepsize does not preserve the correct behaviour up to $h ^ { 5 }$ terms. However, a slight modification to the way the method is implemented restores fifth order performance.

The derivation and the results of preliminary experiments are presented in Butcher and Moir (2003). A fuller description is given by Rattenbury (2005).

For constant stepsize, the tableau for the method is

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0 0</td><td>1 1</td><td></td></tr><tr><td>2</td><td>0 75</td><td>0</td><td>0</td><td></td><td>1 10</td><td>药 69</td></tr><tr><td>27 160</td><td>128</td><td>0</td><td>0</td><td>0</td><td>1 3 640</td><td>1280</td></tr><tr><td>8</td><td>51 28</td><td>8</td><td>0</td><td>0</td><td>1 41 140</td><td>17 280</td></tr><tr><td>1</td><td>1</td><td>1</td><td>7</td><td>0</td><td>1 7</td><td>0</td></tr><tr><td></td><td></td><td></td><td>90</td><td></td><td>90</td><td></td></tr><tr><td>16 45</td><td>1</td><td>16 45</td><td>7 90</td><td>0</td><td>1 7 90</td><td>0</td></tr><tr><td>0</td><td></td><td>0</td><td>0</td><td>1</td><td>0 0</td><td></td></tr><tr><td></td><td>0</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>1352 225</td><td>34 15</td><td>256 75</td><td>196 225</td><td>24 5</td><td>0 242 75</td><td>0</td></tr></table>

When the stepsize is changed at the end of step $n$ from $h$ to $r h$ , an additional term has to be added to the scaled result. In this context $D ( r )$ will denote the scaling matrix $D ( r ) = \mathrm { d i a g } ( 1 , r , r ^ { 2 } )$ so that, for any of the lower order ARK methods, change of stepsize would be accompanied by the rescaling $y ^ { [ n ] } \to ( D ( r ) \otimes I _ { N } ) y ^ { [ n ] }$ . For (546a), this is corrected to

$$
y ^ { [ n ] }  ( D ( r ) \otimes I _ { N } ) y ^ { [ n ] } + r ^ { 2 } ( 1 - r ) \delta ,
$$

where

$$
\begin{array} { r } { \delta = \frac { 4 9 6 } { 4 5 } h F 1 + \frac { 2 2 4 } { 2 5 } h F 2 - \frac { 4 9 2 8 } { 2 2 5 } h F 3 - \frac { 6 4 8 2 } { 2 2 5 } h F 4 + 3 8 h F 5 - \frac { 1 6 3 6 } { 2 2 5 } y _ { 2 } ^ { [ n - 1 ] } . } \end{array}
$$
