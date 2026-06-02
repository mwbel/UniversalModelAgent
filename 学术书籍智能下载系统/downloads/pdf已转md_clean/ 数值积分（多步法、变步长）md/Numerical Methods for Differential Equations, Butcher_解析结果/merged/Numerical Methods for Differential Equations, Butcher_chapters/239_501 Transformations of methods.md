# 501 Transformations of methods

Let $T$ denote a non-singular $r \times r$ matrix. Given a general linear method characterized by the matrices $( A , U , B , V )$ , we consider the construction of a second method for which the input quantities, and the corresponding output quantities, are replaced by linear combinations of the subvectors in $y ^ { \lfloor n - 1 \rfloor }$ (or in $y ^ { \lfloor n \rfloor }$ , respectively). In each case the rows of $T$ supply the coefficients in the linear combinations. These ideas are well known in the case of Adams methods, where it is common practice to represent the data passed between steps in a variety of configurations. For example, the data imported into step $n$ may consist of approximations to $y ( x _ { n - 1 } )$ and further approximations to $h y ^ { \prime } ( x _ { n - i } )$ , for $i = 1 , 2 , \ldots , k$ . Alternatively it might, as in Bashforth and Adams (1883), be expressed in terms of $y ( x _ { n - 1 } )$ and of approximations to a sequence of backward differences of the derivative approximations. It is also possible, as proposed in Nordsieck (1962), to replace the approximations to the derivatives at equally spaced points in the past by linear combinations which will approximate scaled first and higher derivatives at $x _ { n - 1 }$ .

Let z [n−1]i , $i = 1 , 2 , \dots , r$ , denote a component of the transformed input data where

$$
z _ { i } ^ { [ n - 1 ] } = \sum _ { j = 1 } ^ { r } t _ { i j } y _ { j } ^ { [ n - 1 ] } , \qquad z _ { i } ^ { [ n ] } = \sum _ { j = 1 } ^ { r } t _ { i j } y _ { j } ^ { [ n ] } .
$$

This transformation can be written more compactly as

$$
z ^ { [ n - 1 ] } = T y ^ { [ n - 1 ] } , \qquad z ^ { [ n ] } = T y ^ { [ n ] } .
$$

Hence the method which uses the $y$ data and the coefficients $( A , U , B , V )$ , could be rewritten to produce formulae for the stages in the form

$$
Y = h A F + U y ^ { [ n - 1 ] } = h A F + U T ^ { - 1 } z ^ { [ n - 1 ] } .
$$

The formula for $y ^ { \lfloor n \rfloor } = h B F + V y ^ { \lfloor n - 1 \rfloor }$ , when transformed to give the value of $z ^ { \left[ n \right] }$ , becomes

$$
z ^ { [ n ] } = T { \bigl ( } h B F + V y ^ { [ n - 1 ] } { \bigr ) } = h ( T B ) F + ( T V T ^ { - 1 } ) z ^ { [ n - 1 ] } .
$$

Combine (501a) and (501b) into the single formula to give

$$
\left[ \begin{array} { c } { \boldsymbol { Y } } \\ { z ^ { [ n ] } } \end{array} \right] = \left[ \begin{array} { c c } { \boldsymbol { A } } & { \boldsymbol { U } T ^ { - 1 } } \\ { T \boldsymbol { B } } & { T V T ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \boldsymbol { h } \boldsymbol { F } } \\ { z ^ { [ n - 1 ] } } \end{array} \right] .
$$

Thus, the method with coefficient matrices $( A , U T ^ { - 1 } , T B , T V T ^ { - 1 } )$ is related to the original method $( A , U , B , V )$ by an equivalence relationship with a natural computational significance. The significance is that a sequence of approximations, using one of these formulations, can be transformed into the sequence that would have been generated using the alternative formulation.

It is important to ensure that any definitions concerning the properties of a generic general linear method transform in an appropriate manner, when the coefficient matrices are transformed.

Even though there may be many interpretations of the same general linear method, there may well be specific representations which have advantages of one sort or another. Some examples of this will be encountered later in this section.
