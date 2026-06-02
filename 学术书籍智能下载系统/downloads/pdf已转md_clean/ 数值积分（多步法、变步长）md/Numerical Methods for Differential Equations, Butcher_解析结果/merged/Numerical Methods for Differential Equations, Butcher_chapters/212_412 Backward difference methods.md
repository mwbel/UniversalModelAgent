# 412 Backward difference methods

These methods are also known as ‘backward difference formulae’ or BDF methods. Sometimes the notation BDF $k$ is used for the order $k$ member of this family. Instead of choosing a specific $\alpha$ polynomial, we consider the choice $\beta = \beta _ { 0 }$ , where $\beta _ { 0 }$ is to be chosen for consistency. From Theorem 410D we have

$$
\alpha ( 1 + z ) = - \beta _ { 0 } \log ( 1 + z ) + O ( z ^ { p + 1 } ) .
$$

Expand $\beta _ { 0 } \log ( 1 + z )$ to terms in $z ^ { k }$ , for order $p = k$ , and then substitute $z - 1$ in place of $z$ . It is found that

$$
\alpha ( z ) = \beta _ { 0 } \Big ( - ( z - 1 ) + { \textstyle \frac { 1 } { 2 } } ( z - 1 ) ^ { 2 } - { \textstyle \frac { 1 } { 3 } } ( z - 1 ) ^ { 3 } + \cdots \Big ) ,
$$

and $\beta _ { 0 }$ is chosen so that $\alpha ( 0 ) = 1$ . For $k = p = 1$ , we have $\alpha ( z ) = \beta _ { 0 } ( 1 - z )$ , so that $\beta _ { 0 } = 1$ and $\alpha _ { 1 } = 1$ . For $k = p = 2$ ,

$$
\begin{array} { r } { \alpha ( z ) = \beta _ { 0 } \Big ( ( 1 - z ) + \frac { 1 } { 2 } ( 1 - z ) ^ { 2 } \Big ) = \beta _ { 0 } \Big ( \frac { 3 } { 2 } - 2 z + \frac { 1 } { 2 } z ^ { 2 } \Big ) , } \end{array}
$$

Coefficients of the backward difference methods up to order 7   

<table><tr><td>k</td><td>α1</td><td>α2</td><td>α3</td><td>α4</td><td>α5</td><td>α6</td><td>α7</td><td>3</td><td>C</td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>B</td><td>中</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>300</td><td>300</td><td>200</td><td>药</td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>137</td><td>137</td><td>137</td><td>137</td><td>137</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>120</td><td>150</td><td>400</td><td>75</td><td>24</td><td>10</td><td></td><td></td><td>20</td></tr><tr><td></td><td>49</td><td>49</td><td>147</td><td>49</td><td>49</td><td>147</td><td></td><td></td><td>343</td></tr><tr><td></td><td>980</td><td>490</td><td>4900</td><td>1225</td><td>196</td><td>490</td><td>20</td><td></td><td>35</td></tr><tr><td>7</td><td>363</td><td>121</td><td>1089</td><td>363</td><td>121</td><td>1089</td><td>363</td><td>363</td><td>726</td></tr></table>

giving $\begin{array} { r } { \beta _ { 0 } = \frac { 2 } { 3 } } \end{array}$ and

$$
\alpha _ { 1 } = \frac { 4 } { 3 } , ~ \alpha _ { 2 } = - \frac { 1 } { 3 } .
$$

The coefficients for these methods are given up to $p = k = 7$ in Table 412(I), where the error constant $C$ is found to be $\beta _ { 0 } / ( p + 1 )$ .

Note that the method with $p = k = 7$ is of no practical value, in terms of the criteria for convergence, because it is not stable. This remark also applies to methods with $k > 7$ .

# Exercises 41

41.1 Given $\alpha _ { 2 }$ , find $\alpha _ { 1 }$ , $\beta _ { 1 }$ and $\beta _ { 2 }$ such that the linear multistep method $( 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } , \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } )$ has order 2. What are the bounds on $\alpha _ { 2 }$ for which the method is convergent?

41.2 Show that all backward difference methods with $k \leq 6$ are stable.

41.3 Show that the order 7 backward difference method is not stable.

41.4 Find a stable seventh order linear multistep method of the form $( 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { 8 } z ^ { 8 } , \beta _ { 0 } )$ .
