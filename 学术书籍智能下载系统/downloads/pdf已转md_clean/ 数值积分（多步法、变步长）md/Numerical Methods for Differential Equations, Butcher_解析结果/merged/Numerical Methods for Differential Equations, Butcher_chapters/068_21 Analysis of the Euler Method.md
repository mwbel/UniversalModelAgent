# 21 Analysis of the Euler Method

210 Formulation of the Euler method

Consider a differential equation system

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : [ a , b ] \times \mathbb { R } ^ { N }  \mathbb { R } ^ { N }$ is continuous and satisfies a Lipschitz condition $\| f ( x , y ) - f ( x , z ) \| \leq L \| y - z \|$ , for all $x$ in a neighbourhood of $x _ { 0 }$ and $y$ and $z$ in a neighbourhood of $y _ { 0 }$ . For simplicity, we assume that the Lipschitz condition holds everywhere; this is not a serious loss of generality because the existence and uniqueness of a solution to (210a) is known to hold in a suitable interval, containing $x _ { 0 }$ , and we can extend the region where a Lipschitz condition holds to the entire $N$ -dimensional vector space, secure in the knowledge that no practical difference will arise, because the solution will never extend beyond values in some compact set.

We assume that the solution to (210a) is required to be approximated at a point $\scriptstyle { \overline { { x } } }$ , and that a number of intermediate step points are selected. Denote these by $x _ { 1 }$ , $x _ { 2 }$ , . . . , $x _ { n } = { \overline { { x } } }$ . Define a function, $\widetilde { y }$ , on $[ x _ { 0 } , { \overline { { x } } } ]$ by the formula

$$
\begin{array} { r } { \widetilde { y } ( \boldsymbol { x } ) = \widetilde { y } ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , \widetilde { y } ( x _ { k - 1 } ) ) , \boldsymbol { x } \in ( x _ { k - 1 } , \boldsymbol { x } _ { k } ] , } \end{array}
$$

for $k = 1 , 2 , \ldots , n$ . If we assume that $\widetilde { y } ( x _ { 0 } ) = y ( x _ { 0 } ) = y _ { 0 }$ , then $\widetilde { y }$ exactly agrees with the function computed using the Euler method at the points $x = x _ { k }$ , $k = 1 , 2 , \ldots , n$ . The continuous function $\widetilde { y }$ , on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ , is a piecewise linear interpolant of this Euler approximation.

We are interested in the quality of $\widetilde { y }$ as an approximation to $y$ . This will clearly depend on the values of the step points $x _ { 1 }$ , $x _ { 2 }$ , $\cdot \cdot \cdot$ , and especially on the greatest of the distances between a point and the one preceding it. Denote the maximum of $x _ { 1 } - x _ { 0 }$ , $x _ { 2 } - x _ { 1 }$ , $\cdot \cdot \cdot$ , $x _ { n } - x _ { n - 1 }$ by $H$ .

We would like to know what happens to $\| \widetilde { y } ( \overline { { x } } ) - y ( \overline { { x } } ) \|$ as $H  0$ , given also that $\lVert \widetilde { \boldsymbol { y } } ( \boldsymbol { x } _ { 0 } ) - \boldsymbol { y } ( \boldsymbol { x } _ { 0 } ) \rVert  0 .$ . It is also interesting to know what happens to the uniform norm of $\| \widetilde { \boldsymbol { y } } ( \boldsymbol { x } ) - \boldsymbol { y } ( \boldsymbol { x } ) \|$ , for $x$ in $[ x _ { 0 } , { \overline { { x } } } ]$ . Under very general conditions, we show that $\widetilde { y }$ converges uniformly to $y$ , as the mesh is refined in this way.
