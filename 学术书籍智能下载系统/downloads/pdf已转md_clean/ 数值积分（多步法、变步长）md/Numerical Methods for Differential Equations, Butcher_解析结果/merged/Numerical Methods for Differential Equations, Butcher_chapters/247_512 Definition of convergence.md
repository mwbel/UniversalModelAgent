# 512 Definition of convergence

Just as for linear multistep methods, the necessity of using a starting procedure complicates the idea of convergence. We deal with this complication by assuming nothing more from the starting procedure than the fact that, for sufficiently small $h$ , it produces an approximation arbitrarily close to

$$
\left[ \begin{array} { c } { u _ { 1 } y ( x _ { 0 } ) } \\ { u _ { 2 } y ( x _ { 0 } ) } \\ { \vdots } \\ { u _ { r } y ( x _ { 0 } ) } \end{array} \right] ,
$$

where $u$ is some non-zero vector in $\mathbb { R } ^ { r }$ . Here $y ( x _ { 0 } )$ is the given initial data and it will be our aim to obtain a good approximation at some $\overline { { x } } > x _ { 0 }$ . This approximation should converge to

$$
\left[ \begin{array} { c } { u _ { 1 } y ( \overline { { x } } ) } \\ { u _ { 2 } y ( \overline { { x } } ) } \\ { \vdots } \\ { u _ { r } y ( \overline { { x } } ) } \end{array} \right] ,
$$

for any problem satisfying a Lipschitz condition. For notational convenience, (512a) will usually be abbreviated as $u y ( { \overline { { x } } } )$ .

Formally, we write $\phi ( h )$ for the starting approximation associated with the method and with a given initial value problem.

Definition 512A A general linear method $( A , U , B , V )$ , is ‘convergent’ if for any initial value problem

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

subject to the Lipschitz condition $\| f ( y ) - f ( z ) \| \leq L \| y - z \|$ , there exist a nonzero vector $u \in \mathbb { R } ^ { r }$ , and a starting procedure $\phi : ( 0 , \infty ) \to \mathbb { R } ^ { r }$ , such that for all $i = 1 , 2 , \dots , r$ , $\begin{array} { r } { \operatorname* { l i m } _ { h \to 0 } \phi _ { i } ( h ) = u _ { i } y ( x _ { 0 } ) } \end{array}$ , and such that for any $\overline { { x } } > x _ { 0 }$ , the sequence of vectors $y ^ { [ n ] }$ , computed using $n$ steps with stepsize $h = ( \overline { { x } } - x _ { 0 } ) / n$ and using $y ^ { [ 0 ] } = \phi ( h )$ in each case, converges to $u y ( { \overline { { x } } } )$ .

The necessity of stability and consistency, as essential properties of convergent methods, are proved in the next two subsections, and this is followed by the converse result that all stable and consistent methods are convergent.
