# 557 Scale and modify for stability

With the aim of designing algorithms based on IRKS methods in a variable order, variable stepsize setting, we consider what happens when $h$ changes from step to step. If we use a simple scaling system, as in classical Nordsieck implementations, we encounter two difficulties. The first of these is that methods which are stable when $h$ is fixed can become unstable when $h$ is allowed to vary. The second is that attempts to estimate local truncation errors, for both the current method and for a method under consideration for succeeding steps, can become unreliable.

Consider, for example, the method (555b). If $h$ is the stepsize in step $n$ , which changes to $r h$ in step $n + 1$ , the output would be scaled from $y ^ { \lfloor n \rfloor }$ to $( D ( r ) \otimes I _ { N } ) y ^ { [ n ] }$ , where $D ( r ) = \mathrm { d i a g } ( 1 , r , r ^ { 2 } , r ^ { 3 } )$ . This means that the $V$ matrix which determines stable behaviour for non-stiff problems, becomes effectively

$$
D ( r ) V = \left[ { \begin{array} { c c c c } { 1 } & { - \frac { 4 7 3 } { 1 0 9 2 } } & { - \frac { 8 1 } { 7 2 8 } } & { \frac { 1 7 } { 1 7 4 7 2 } } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { \frac { 5 2 } { 7 } r ^ { 2 } } & { \frac { 1 } { 7 } r ^ { 2 } } & { - \frac { 1 } { 2 8 } r ^ { 2 } } \\ { 0 } & { \frac { 5 6 8 } { 2 1 } r ^ { 3 } } & { \frac { 4 } { 7 } r ^ { 3 } } & { - \frac { 1 } { 7 } r ^ { 3 } } \end{array} } \right] .
$$

To guarantee stability we want all products of matrices of the form

$$
\begin{array} { r } { \widehat { V } ( r ) = \left[ \begin{array} { l l } { \frac { 1 } { 7 } r ^ { 2 } } & { - \frac { 1 } { 2 8 } r ^ { 2 } } \\ { \frac { 4 } { 7 } r ^ { 3 } } & { - \frac { 1 } { 7 } r ^ { 3 } } \end{array} \right] } \end{array}
$$

to be bounded. As a first requirement, we would need (557a) to be powerbounded. Because the determinant is zero, this means only that the trace $r ^ { 2 } ( 1 - r ) / 7$ must lie in $[ - 1 , 1 ]$ , so that $r \in [ 0 , r ^ { \star } ]$ , where $r ^ { \star } \approx 2 . 3 1 0 8 5 2 1 6 3$ is a zero of $r ^ { 3 } = r ^ { 2 } + 7$ . For a product $\widehat V ( r _ { n } ) \widehat V ( r _ { n - 1 } ) \cdot \cdot \cdot \widehat V ( r _ { 1 } )$ , the non-zero eigenvalue is $\textstyle \prod _ { i = 1 } ^ { n } \left( ( r ^ { 2 } - r ^ { 3 } ) / 7 \right)$ so that $r _ { 1 } , r _ { 2 } , \ldots , r _ { n } \in [ 0 , r ^ { \star } ]$ is sufficient for variable stepsize stability.

While this is a very mild restriction on $r$ values for this method, the corresponding restriction may be more severe for other methods. For example, for the scaled value of $V$ given by (556b) the maximum permitted value of $r$ is approximately 1.725419906.

Whatever restriction needs to be imposed on $r$ for stability, we may wish to avoid even this restriction. We can do this using a modification to simple Nordsieck scaling. By Taylor expansion we find

$$
\begin{array} { r l r } {  { - \frac { 4 0 } { 2 1 } h y ^ { \prime } ( x _ { n - 1 } + h c _ { 1 } ) - \frac { 6 } { 7 } h y ^ { \prime } ( x _ { n - 1 } + h c _ { 2 } ) + \frac { 4 0 } { 2 1 } h y ^ { \prime } ( x _ { n - 1 } + h c _ { 3 } ) } } \\ & { } & { \quad - \frac { 2 } { 3 } h y ^ { \prime } ( x _ { n - 1 } + h c _ { 4 } ) + \frac { 3 2 } { 2 1 } h y ^ { \prime } ( x _ { n - 1 } ) + \frac { 1 } { 7 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) - \frac { 1 } { 2 8 } h ^ { 3 } y ^ { ( 3 ) } ( x _ { n - 1 } ) } \\ & { } & { \quad \quad = O ( h ^ { 4 } ) , } \end{array}
$$

so that it is possible to add a multiple of the vector

$$
\begin{array} { r } { d = [ - { \frac { 4 0 } { 2 1 } } \quad - { \frac { 6 } { 7 } } \quad { \frac { 4 0 } { 2 1 } } \quad - { \frac { 2 } { 3 } } \ | 0 \quad { \frac { 3 2 } { 2 1 } } \quad { \frac { 1 } { 7 } } \quad - { \frac { 1 } { 2 8 } } ] } \end{array}
$$

to any row of the combined matrices $[ B | V ]$ without decreasing the order below 3. In the scale and modify procedure we can, after effectively scaling $[ B | V ]$ by $D ( r )$ , modify the result by adding $( 1 - r ^ { 2 } ) d$ to the third row and $4 ( 1 - r ^ { 3 } ) d$ to the fourth row. Expressed another way, write

$$
\delta = - \textstyle { \frac { 4 0 } { 2 1 } } h F _ { 1 } - \textstyle { \frac { 6 } { 7 } } h F _ { 2 } + \textstyle { \frac { 4 0 } { 2 1 } } h F _ { 3 } - \textstyle { \frac { 2 } { 3 } } h F _ { 4 } + \frac { 3 2 } { 2 1 } y _ { 2 } ^ { [ n - 1 ] } + \frac { 1 } { 7 } y _ { 3 } ^ { [ n - 1 ] } - \frac { 1 } { 2 8 } y _ { 4 } ^ { [ n - 1 ] } ,
$$

so that the scale and modify process consists of replacing $y ^ { \lfloor n \rfloor }$ by

$$
D ( r ) y ^ { [ n ] } + \mathrm { d i a g } \left( 0 , 0 , ( 1 - r ^ { 2 } ) , 4 ( 1 - r ^ { 3 } ) \right) \delta .
$$
