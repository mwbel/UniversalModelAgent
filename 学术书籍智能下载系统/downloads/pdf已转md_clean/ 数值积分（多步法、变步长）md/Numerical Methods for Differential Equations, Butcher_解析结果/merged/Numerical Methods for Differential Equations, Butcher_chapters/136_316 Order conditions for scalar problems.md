# 316 Order conditions for scalar problems

Early studies of Runge–Kutta methods were built around the single scalar equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) .
$$

Even though it was always intended that methods derived for (316a) should be interpreted, where appropriate, in a vector setting, a subtle difficulty arises for orders greater than 4.

We adopt the notation $f _ { x }$ , $f _ { y }$ for partial derivatives of $f$ with respect to the first and second arguments, with similar notations for higher derivatives. Also, for simplicity, we omit the arguments in expressions like $f _ { x } ( x , y )$ . By straightforward differentiation of (316a), we have

$$
y ^ { \prime \prime } = f _ { x } + f _ { y } y ^ { \prime } = f _ { x } + f _ { y } f ,
$$

where the two terms together correspond to the elementary differential associated with $t = \mathbb { I }$ Similarly, for the third derivative we have

$$
y ^ { \prime \prime \prime } = { \left( { { f _ { x x } } + 2 { f _ { x y } } f + { f _ { y y } } { f ^ { 2 } } } \right) + \left( { { f _ { y } } ( { f _ { x } } + { f _ { y } } { f } ) } \right) } ,
$$

where the grouped terms correspond to $t = \mathsf { Y }$ and $t = { \mathfrak { f } }$ respectively.

The expressions that arise here, and for the fourth derivative, are more complicated, because of the presence of derivatives with respect to $x$ . However, the terms can be grouped together according to the elementary differentials to which they correspond. Furthermore, the order conditions are identical to those found in the general vector case. When similar expressions are worked out for the 17 elementary differentials of order 5, we find a confusion between the results for two particular trees. In fact for each of $t _ { 1 } = { \sqrt [ { \object Object] { \operatorname { \rho } } } } \mathrm { a n d } t _ { 2 } = { \sqrt [ { \math { \rho } } } , F$ $F ( t )$ reduces to

$$
F ( t ) = f _ { y } ( f _ { y y } f + f _ { x y } ) ( f _ { y } f + f _ { x } ) ,
$$

and instead of two order conditions

$$
\Phi ( t _ { 1 } ) = \sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } = { \frac { 1 } { \gamma ( t _ { 1 } ) } } = { \frac { 1 } { 3 0 } }
$$

and

$$
\Phi ( t _ { 2 } ) = \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac 1 { \gamma ( t _ { 2 } ) } = \frac 1 { 4 0 } ,
$$

we have the single condition

$$
\sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } + \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac { 7 } { 1 2 0 } .
$$

We discuss in Subsection 325 the construction of fifth order methods. These usually satisfy the so-called $D ( 1 )$ condition, which we introduce in Subsection 321. This simplifying assumption has, as one of its consequences, the dependence of (316b) on other conditions, for which there is no confusion. Hence, for methods satisfying $D ( 1 )$ , scalar and vector order 5 conditions are equivalent.

For orders 6 and higher, the confusion between the order conditions for the scalar case becomes more pronounced. The first published methods of this order(Huˇta, 1956, 1957) were derived for scalar problems but, nevertheless, have order 6 for the general vector case (Butcher, 1963a).
