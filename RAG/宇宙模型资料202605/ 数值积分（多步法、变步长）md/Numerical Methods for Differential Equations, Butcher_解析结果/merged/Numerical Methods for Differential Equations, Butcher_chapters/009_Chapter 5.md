# Chapter 5

# General Linear Methods

50 Representing Methods in General Linear Form

# 500 Multivalue–multistage methods

The systematic computation of an approximation to the solution of an initial value problem usually involves just two operations: evaluation of the function $f$ defining the differential equation and the forming of linear combinations of previously computed vectors. In the case of implicit methods, further complications arise, but these can also be brought into the same general linear formulation.

We consider methods in which a collection of vectors forms the input at the beginning of a step, and a similar collection is passed on as output from the current step and as input into the following step. Thus the method is a multivalue method, and we write $r$ for the number of quantities processed in this way. In the computations that take place in forming the output quantities, there are assumed to be $s$ approximations to the solution at points near the current time step for which the function $f$ needs to be evaluated. As for Runge–Kutta methods, these are known as stages and we have an $s$ -stage or, in general, multistage method.

The intricate set of connections between these quantities make up what is known as a general linear method. Following Burrage and Butcher (1980), we represent the method by four matrices which we will generally denote by $A$ , $U$ , $B$ and $V$ . These can be written together as a partitioned $( s + r ) \times ( s + r )$ matrix

$$
\left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] .
$$

The input vectors available at step $n$ will be denoted by $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { \lfloor n - 1 \rfloor }$ , y[n−1] r . During the computations which constitute the step, stage values Y1, $Y _ { 2 }$ , . . . , $Y _ { s }$ , are computed and derivative values $F _ { i } = f ( Y _ { i } )$ , $i = 1 , 2 , \dots , s$ , are computed in terms of these. Finally, the output values are computed and, because these will constitute the input at step $n + 1$ , they will be denoted by $y _ { i } ^ { \lfloor n \rfloor }$ , $i = 1 , 2 , \dots , r$ . The relationships between these quantities are defined in terms of the elements of $A$ , $U$ , $B$ and $V$ by the equations

$$
\begin{array} { c } { { Y _ { i } = \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } h F _ { j } + \sum _ { j = 1 } ^ { r } u _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , s , } } \\ { { y _ { i } ^ { [ n ] } = \displaystyle \sum _ { j = 1 } ^ { s } b _ { i j } h F _ { j } + \sum _ { j = 1 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , r . } } \end{array}
$$

It will be convenient to use a more concise notation, and we start by defining vectors $\boldsymbol { Y } , \boldsymbol { F } \in \mathbb { R } ^ { s N }$ and $y ^ { \lfloor n - 1 \rfloor } , y ^ { \lfloor n \rfloor } \in \mathbb { R } ^ { r N }$ as follows:

$$
\begin{array} { r } { Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad F = \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { \vdots } \\ { F _ { s } } \end{array} \right] , \quad y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n - 1 ] } } \\ { y _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n - 1 ] } } \end{array} \right] , \quad y ^ { [ n ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n ] } } \\ { y _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n ] } } \end{array} \right] . } \end{array}
$$

Using these supervectors, it is possible to write (500a) and (500b) in the form

$$
\left[ \begin{array} { c } { Y } \\ { y ^ { [ n ] } } \end{array} \right] = \left[ \begin{array} { c c } { A \otimes I _ { N } } & { U \otimes I _ { N } } \\ { B \otimes I _ { N } } & { V \otimes I _ { N } } \end{array} \right] \left[ \begin{array} { c } { h F } \\ { y ^ { [ n - 1 ] } } \end{array} \right] .
$$

In this formulation, $I _ { N }$ denotes the $N \times N$ unit matrix and the Kronecker product is given by

$$
A \otimes I _ { N } = \left[ \begin{array} { c c c c } { a _ { 1 1 } I _ { N } } & { a _ { 1 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { 1 s } I _ { N } } \\ { a _ { 2 1 } I _ { N } } & { a _ { 2 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { 2 s } I _ { N } } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { a _ { s 1 } I _ { N } } & { a _ { s 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { s s } I _ { N } } \end{array} \right] .
$$

When there is no possibility of confusion, we simplify the notation by replacing

$$
\left[ \begin{array} { l l } { A \otimes I _ { N } } & { U \otimes I _ { N } } \\ { B \otimes I _ { N } } & { V \otimes I _ { N } } \end{array} \right] \quad \mathrm { b y } \quad \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] .
$$

In Subsections 502–505, we illustrate these ideas by showing how some known methods, as well as some new methods, can be formulated in this manner. First, however, we will discuss the possibility of transforming a given method into one using a different arrangement of the data passed from step to step.

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

# 502 Runge–Kutta methods as general linear methods

Since Runge–Kutta methods have a single input, it is usually convenient to represent them, as general linear methods, with $r = 1$ . Assuming the input vector is an approximation to $y ( x _ { n - 1 } )$ , it is only necessary to write $U = { \bf 1 }$ , $V = 1$ , write $B$ as the single row $b ^ { \prime }$ of the Runge–Kutta tableau and, finally, identify $A$ with the $s \times s$ matrix of the same name also in this tableau.

A very conventional and well-known example is the classical fourth order method

$$
\begin{array}{c} { \begin{array} { r l } & { { \begin{array} { l } { 0 } \\ { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } \\ { 1 } \end{array} } } \\ & { { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } } \end{array} }  \\ & { { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } } \end{array} 
$$

which, in general linear formulation, is represented by the partitioned matrix

$$
\left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} \right] .
$$

A more interesting example is the Lobatto IIIA method for which the straightforward representation, with $s \ = \ 3$ and $r ~ = ~ 1$ , is misleading. The reason is that the method has the ‘FSAL property’ in the sense that the final stage evaluated in a step is identical with the first stage of the following step. It therefore becomes possible, and even appropriate, to use a representation with $s = r = 2$ which expresses, quite explicitly, that the FSAL property holds. This representation would be

<table><tr><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>1</td><td>NA</td></tr></table>

$$
\left[ { \frac { \frac { 1 } { 3 } } { 3 } } \quad - { \frac { 1 } { 1 2 } } \quad \left| { 1 \frac { 5 } { 1 2 } } \right. \right] ,
$$

and the input quantities are supposed to be approximations to

$$
y _ { 1 } ^ { [ n - 1 ] } \approx y ( x _ { n - 1 } ) , \quad y _ { 2 } ^ { [ n - 1 ] } \approx h y ^ { \prime } ( x _ { n - 1 } ) .
$$

Finally, we consider a Runge–Kutta method introduced in Subsection 322, with tableau

As we pointed out when the method was introduced, it can be implemented as a two-value method by replacing the computation of the second stage derivative by a quantity already computed in the previous step. The method is now not equivalent to any Runge–Kutta method but, as a general linear method, it has coefficient matrix

<table><tr><td>0 3 -2</td><td>0 0 2</td><td>0 0 0</td><td>1 0 1 1 4</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1 1 1 0</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>1</td><td>0</td><td>0 0</td></tr></table>

# 503 Linear multistep methods as general linear methods

For a linear $k$ -step method $[ \alpha , \beta ]$ of the special form $\alpha ( z ) = 1 - z$ , the natural way of writing this as a general linear method is to choose $r = k + 1$ , $s = 1$ and the input approximations as

$$
y ^ { [ n - 1 ] } \approx \left[ \begin{array} { c } { y ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 2 } ) } \\ { \cdots } \\ { h y ^ { \prime } ( x _ { n - k } ) } \end{array} \right] .
$$

The matrix representing the method now becomes

$$
{ [ \begin{array} { l l l l l l l } { \beta _ { 0 } | } & { 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { \beta _ { k } } \\ { \beta _ { 0 } | } & { 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { \beta _ { k } } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] } .
$$

Because y[1 $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ and $y _ { k + 1 } ^ { [ n - 1 ] }$ occur in the combination $y _ { 1 } ^ { [ n - 1 ] } + \beta _ { k } y _ { k + 1 } ^ { [ n - 1 ] }$ in each of the two places where these quantities are used, we might try to simplify the method by transforming using the matrix

$$
T = { \left[ \begin{array} { l l l l l l } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { \beta _ { k } } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] } ~ .
$$

The transformed coefficient matrices become

$$
[ \begin{array} { l l l l l l l l } { A } & { U T ^ { - 1 } } \\ { T B } & { T V T ^ { - 1 } } \end{array} ] = [ \begin{array} { l l l l l l l l } { \beta _ { 0 } | 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { 0 } \\ { \beta _ { 0 } | 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } + \beta _ { k } } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] ,
$$

and we see that it is possible to reduce $r$ from $k + 1$ to $k$ , because the $( k + 1 ) \mathrm { t h }$ input vector is never used in the calculation.

The well-known technique of implementing an implicit linear multistep method by combining it with a related explicit method to form a predictor– corrector pair fits easily into a general linear formulation. Consider, for example, the PECE method based on the third order Adams Bashforth and Adams–Moulton predictor–corrector pair. Denote the predicted approximation by $y _ { n } ^ { * }$ and the corrected value by $y _ { n }$ . We then have

$$
\begin{array} { l } { { y _ { n } ^ { * } = y _ { n - 1 } + { \displaystyle \frac { 2 3 } { 1 2 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \displaystyle \frac { 4 } { 3 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) + { \displaystyle \frac { 5 } { 1 2 } } h f ( x _ { n - 3 } , y _ { n - 3 } ) , } } \\ { { y _ { n } = y _ { n - 1 } + { \displaystyle \frac { 5 } { 1 2 } } h f ( x _ { n } , y _ { n } ^ { * } ) + { \displaystyle \frac { 2 } { 3 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \displaystyle \frac { 1 } { 1 2 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) . } } \end{array}
$$

As a two-stage general linear method, we write $Y _ { 1 } ~ = ~ y _ { n } ^ { * }$ and $Y _ { 2 } ~ = ~ y _ { n }$ . The $r \ = \ 4$ input approximations are the values of $y _ { n - 1 }$ , $h f ( x _ { n - 1 } , y _ { n - 1 } )$ , $h f ( x _ { n - 2 } , y _ { n - 2 } )$ and $h f ( x _ { n - 3 } , y _ { n - 3 } )$ . The $( s + r ) \times ( s + r )$ coefficient matrix is now

$$
[ \begin{array} { c c } { 0 } & { 0 } \\ { \frac { 5 } { 1 2 } } & { 0 } \\ { \frac { 5 } { 1 2 } } & { 0 } \\ { 0 } & { 1 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} ] \begin{array} { c c c } { 1 } & { \frac { 2 3 } { 1 2 } } & { - \frac { 4 } { 3 } } \\ { 1 } & { \frac { 2 } { 3 } } & { - \frac { 1 } { 1 2 } } \\ { \frac { 2 } { 3 } } & { - \frac { 1 } { 1 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} ] .
$$

The one-leg methods, introduced by Dahlquist (1976) as counterparts of linear multistep methods, have their own natural representations as general linear methods. For the method characterized by the polynomial pair $[ \alpha ( z ) , \beta ( z ) ]$ , the corresponding one-leg method computes a single stage value $Y$ , with stage derivative $F ^ { \dagger }$ , using the formula

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } + { \biggl ( } \sum _ { i = 0 } ^ { k } \beta _ { i } { \biggr ) } h F ,
$$

where

$$
Y = \frac { \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } .
$$

This does not fit into the standard representation for general linear methods but it achieves this format when $Y$ and $y _ { n }$ are separated out from the two expressions (503b) and (503c). We find

$$
\begin{array} { l } { { \displaystyle Y = \beta _ { 0 } h F + \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) ^ { - 1 } \sum _ { i = 1 } ^ { k } ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } ) y _ { n - i } } , } \\ { { \displaystyle y _ { n } = \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) h F + \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } } . } \end{array}
$$

As a general linear method, it has the form

$$
[ \begin{array} { c }  \frac { \beta _ { 0 } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } | \begin{array} { c c c c c c } { \gamma _ { 1 } } & { \gamma _ { 2 } } & { \gamma _ { 3 } } & { \cdots } & { \gamma _ { k - 1 } } & { \gamma _ { k } } \\ { \alpha _ { 1 } } & { \alpha _ { 2 } } & { \alpha _ { 3 } } & { \cdots } & { \alpha _ { k - 1 } } & { \alpha _ { k } } \\ { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] , \end{array}
$$

where

$$
\gamma _ { i } = \bigg ( \sum _ { j = 0 } ^ { k } \beta _ { j } \bigg ) ^ { - 1 } \big ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } \big ) , \qquad i = 1 , 2 , \ldots , k .
$$

# 504 Some known unconventional methods

Amongst the methods that do not fit under the conventional Runge–Kutta or linear multistep headings, we consider the cyclic composite methods of Donelson and Hansen (1971), the pseudo Runge–Kutta methods of Byrne and Lambert (1966) and the hybrid methods of Gragg and Stetter (1964), Butcher (1965) and Gear (1965). We illustrate, by examples, how methods of these types can be cast in general linear form.

To overcome the limitations of linear multistep methods imposed by the conflicting demands of order and stability, Donelson and Hansen proposed a procedure in which two or more linear multistep methods are used in rotation over successive steps. Write the constituent methods as $( \alpha ^ { ( 1 ) } , \beta ^ { ( 1 ) } )$ , $( \alpha ^ { ( 2 ) } , \beta ^ { ( 2 ) } ) , . .$ . , $( \alpha ^ { ( m ) } , \beta ^ { ( m ) } )$ , so that the formula for computing $y _ { n }$ will be

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } ^ { ( j ) } y _ { n - i } + \sum _ { i = 0 } ^ { k } \beta _ { i } ^ { ( j ) } h f ( x _ { n - i } , y _ { n - i } ) ,
$$

where $j \in \{ 1 , 2 , \dots , m \}$ is chosen so that $n - j$ is a multiple of $m$ .

The step value $-$ that is the maximum of the degrees of $\alpha ^ { ( j ) }$ and $\beta ^ { ( j ) } \textrm { - }$ may vary amongst the $m$ constituent methods, but they can be assumed to have a common value $k$ equal to the maximum over all the basic methods. We illustrate these ideas in the case $k = 3$ , $m = 2$ . As a consequence of the Dahlquist barrier, order $p = 5$ with $k = 3$ is inconsistent with stability and therefore convergence. Consider the following two linear multistep methods:

$$
\begin{array} { r l } & { [ \alpha ^ { ( 1 ) } ( z ) , \beta ^ { ( 1 ) } ( z ) ] = [ 1 + \frac { 8 } { 1 1 } z - \frac { 1 9 } { 1 1 } z ^ { 2 } , \frac { 1 0 } { 3 3 } + \frac { 1 9 } { 1 1 } z + \frac { 8 } { 1 1 } z ^ { 2 } - \frac { 1 } { 3 3 } z ^ { 3 } ] , } \\ & { [ \alpha ^ { ( 2 ) } ( z ) , \beta ^ { ( 2 ) } ( z ) ] = [ 1 - \frac { 4 4 9 } { 2 4 0 } z - \frac { 1 9 } { 3 0 } z ^ { 2 } + \frac { 3 6 1 } { 2 4 0 } z ^ { 3 } , \frac { 2 5 1 } { 7 2 0 } + \frac { 1 9 } { 3 0 } z - \frac { 4 4 9 } { 2 4 0 } z ^ { 2 } - \frac { 3 5 } { 7 2 } z ^ { 3 } ] . } \end{array}
$$

Each of these has order 5 and is, of course, unstable. To combine them, used alternately, into a single step of a general linear method, it is convenient to regard $h$ as the stepsize for the complete cycle of two steps. We denote the incoming approximations as $y _ { n - 3 / 2 }$ , $y _ { n - 1 }$ , $h f _ { n - 2 }$ , $h f _ { n - 3 / 2 }$ and $h f _ { n - 1 } .$ The first half-step, relating $y _ { n - 1 / 2 }$ and $h f _ { n - 1 / 2 }$ to the input quantities, gives

$$
\begin{array} { r } { y _ { n - \frac { 1 } { 2 } } = \frac { 5 } { 3 3 } h f _ { n - \frac { 1 } { 2 } } + \frac { 1 9 } { 1 1 } y _ { n - \frac { 3 } { 2 } } - \frac { 8 } { 1 1 } y _ { n - 1 } - \frac { 1 } { 6 6 } h f _ { n - 2 } + \frac { 4 } { 1 1 } h f _ { n - \frac { 3 } { 2 } } + \frac { 1 9 } { 2 2 } h f _ { n - 1 } . } \end{array}
$$

Substitute this into the corresponding formula for $y _ { n }$ and we find

$$
\begin{array} { r } { y _ { n } = \frac { 4 7 5 3 } { 7 9 2 0 } h f _ { n - \frac { 1 } { 2 } } + \frac { 2 5 1 } { 1 4 4 0 } h f _ { n } + \frac { 1 9 } { 1 1 } y _ { n - \frac { 3 } { 2 } } - \frac { 8 } { 1 1 } y _ { n - 1 } \qquad } \\ { - \frac { 4 4 9 } { 1 5 8 4 0 } h f _ { n - 2 } + \frac { 3 4 6 3 } { 7 9 2 0 } h f _ { n - \frac { 3 } { 2 } } + \frac { 4 4 9 } { 6 6 0 } h f _ { n - 1 } . } \end{array}
$$

Translating these formulae into the $( A , U , B , V )$ formulation gives

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l l l l l l } { { \frac { 5 } { 3 3 } } } & { 0 } & { 0 } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 1 } { 6 6 } } } & { { \frac { 4 } { 1 1 } } } & { { \frac { 1 9 } { 2 2 } } } \\ { { \frac { 4 7 9 5 3 } { 7 9 2 0 } } } & { { \frac { 2 5 1 } { 1 4 4 0 } } } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 4 4 9 } { 1 5 8 4 0 } } } & { { \frac { 3 4 6 3 } { 7 9 2 0 } } } & { { \frac { 4 4 9 } { 6 6 0 } } } \\ { { \frac { 5 } { 3 3 } } } & { 0 } & { { \frac { 1 9 } { 1 9 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 1 } { 6 6 } } } & { { \frac { 1 } { 4 1 } } } & { { \frac { 1 9 } { 1 2 } } } \\ { { \frac { 4 7 5 3 } { 7 9 2 0 } } } & { { \frac { 2 5 1 } { 1 4 4 0 } } } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 1 } { 1 1 } } } & { - { \frac { 4 4 9 } { 1 5 8 4 0 } } } & { { \frac { 3 4 6 3 } { 7 9 2 0 } } } & { { \frac { 4 4 9 } { 6 6 0 } } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } .
$$

This formulation can be simplified, in the sense that $r$ can be reduced, and we have, for example, the following alternative coefficient matrices:

<table><tr><td rowspan="5">A U = B V</td><td>5 33 4753</td><td>0 251</td><td rowspan="5">1</td><td>1 66 449</td><td>4 1 3463</td><td>19 22 449</td></tr><tr><td>7920</td><td>1440</td><td>1 15840</td><td>7920</td><td>660</td></tr><tr><td>173 990</td><td>251 1980</td><td>1 1 180</td><td>307 990</td><td>329 330</td></tr><tr><td>0</td><td>0</td><td>0 0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Because of the natural way in which we have written this particular composite cyclic pair in general linear form, and then rewritten it, using equally simple operations, into a less recognizable form, an obvious question arises. The question is whether it might have been more appropriate to use the general linear formulation from the start, and then explore the existence of suitable methods that have no connection with linear multistep methods.

We now turn to pseudo Runge–Kutta methods. Consider the method given by (261a). Even though four input values are used in step $h F _ { 2 } ^ { [ n - 1 ] }$ and $h F _ { 3 } ^ { \lfloor n - 1 \rfloor }$ ), this can be effectively reduced to $n$ tw $( y _ { n - 1 } , h F _ { 1 } ^ { [ n - 1 ] }$ ecause, in , addition to $y _ { n - 1 }$ , only the combination $\begin{array} { r } { \frac { 1 } { 1 2 } h F _ { 1 } ^ { [ n - 1 ] } - \frac { 1 } { 3 } h F _ { 2 } ^ { [ n - 1 ] } - \frac { 1 } { 4 } h F _ { 3 } ^ { [ n - 1 ] } } \end{array}$ is actually used. This means that a quantity of this form, but with $n - 1$ replaced by $n$ , has to be computed in step $n$ for use in the following step. The $( 3 + 2 ) \times ( 3 + 2 )$ matrix representing this method is

$$
\left[ { \begin{array} { r r r r r r } { 0 } & { 0 } & { 0 } & { { \left| \begin{array} { l l } { 1 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 4 } { 3 } } } & { 0 } \end{array} \right|}  } & { 1 } & { 0 } \\ { { \frac { 1 1 } { 1 2 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 4 } } } & { 1 } & { 1 } \\ { { \frac { 1 } { 1 2 } } } & { - { \frac { 1 } { 3 } } } & { - { \frac { 1 } { 4 } } } & { 0 } & { 0 } \end{array} } \right] .
$$

For a seventh order method taken from Butcher (1965), the solution at the end of the step is approximated using ‘predictors’ at $x _ { n } - { \textstyle { \frac { 1 } { 2 } } } h$ and at $x _ { n }$ , in preparation for a final ‘corrector’ value, also at $x _ { n }$ . The input quantities correspond to solution approximations y[n−1]1 ≈ y(xn 1), y[n−1]2 ≈ y(xn 2) and y[n−1]3 ≈ y(xn−3), and the corresponding scaled derivative approximations y[n−1] ≈ hy- (xn 1), y[n −1]5 ≈ hy- (xn 2) and y[n6 −1] ≈ hy- (xn 3). The general linear representation is

<table><tr><td>0 384</td><td>0</td><td>0</td><td>225 128</td><td>200 128</td><td>153 128 212</td><td>225 128 1395</td><td>300 128</td><td>45 128</td></tr><tr><td>155 2304</td><td>0 465</td><td>0</td><td>540 128 783</td><td>297 31 135</td><td>31 31</td><td>155 135</td><td>2130 155 495</td><td>309 155</td></tr><tr><td>3085</td><td>3085</td><td>0</td><td>617</td><td>617</td><td>617</td><td>3085</td><td>3085</td><td>39 3085</td></tr><tr><td>2304 3085</td><td>465 3085</td><td>0</td><td>783 617</td><td>135 617</td><td>31 617</td><td>135 3085</td><td>495 3085</td><td>39</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3085 0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td></td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

# 505 Some recently discovered general linear methods

The methods already introduced in this section were inspired as modifications of Runge–Kutta or linear multistep methods. We now consider two example methods motivated not by either of the classical forms, but by the general linear structure in its own right.

The first of these is known as an ‘Almost Runge–Kutta’ method. That is, although it uses three input and output approximations, it behaves like a Runge–Kutta method from many points of view. The input vectors can be thought of as approximations to $y ( x _ { n - 1 } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } )$ and the output vectors are intended to be approximations to these same quantities, but evaluated at $x _ { n }$ rather than at $x _ { n - 1 }$ :

$$
\left[ { \begin{array} { c c c c c c c } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 1 6 } } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - { \frac { 1 } { 4 } } } & { 2 } & { 0 } & { 0 } & { 1 } & { - { \frac { 3 } { 4 } } } & { - { \frac { 1 } { 4 } } } \\ { 0 } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { 1 } & { { \frac { 1 } { 6 } } } & { 0 } \\ { 0 } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { 1 } & { { \frac { 1 } { 6 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { { - { \frac { 1 } { 3 } } } } & { 0 } & { - { \frac { 2 } { 3 } } } & { 2 } & { 0 } & { - 1 } & { 0 } \end{array} } \right] .
$$

The particular example given here has order 4, in contrast to the third order method introduced in Section 27 to illustrate implementation principles. Further details concerning Almost Runge–Kutta methodsare presented in Subsection 543.

The second example is given by the coefficient matrix

<table><tr><td>0 0 1 0 1</td><td>0</td><td>0 0</td><td>1 0 0 1</td><td>0 0 1</td></tr><tr><td>1 1</td><td>1</td><td>1</td><td>0</td><td>0 1</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td></td><td>R</td><td>N-</td></tr></table>

In the case of (505b), the input values are given respectively as approximations to

$$
\begin{array} { l c l } { y ( x _ { n - 1 } ) , } \\ { y ( x _ { n - 1 } + \frac { 1 } { 2 } h ) + h y ^ { \prime } ( x _ { n - 1 } ) } \end{array}
$$

and to

and the output consists of the same three quantities, to within $O ( h ^ { 4 } )$ , with $x _ { n - 1 }$ advanced one step to $x _ { n }$ . Thus the method has order 3. This is an example of a ‘type 1 DIMSIM method’, to be introduced in Subsection 541.

Both (505a) and (505b) possess the property of RK stability, which guarantees that the method behaves, at least in terms of linear stability, like a Runge–Kutta method. While their multivalue structure is a disadvantage compared with Runge–Kutta methods, they have some desirable properties. For (505a) the stage order is 2, and for (505b) the stage order is 3.

# Exercises 50

50.1 Write the general linear method given by (503a) in transformed form using the matrix

$$
T = \left[ { \begin{array} { r r r r r } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { - 1 } & { { \frac { 1 } { 4 } } } \\ { 0 } & { { \frac { 1 } { 6 } } } & { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } \right] .
$$

Note that this converts the method into Nordsieck form.

50.2 Write the general linear method given by (502a) in transformed form using the matrix

$$
T = \left[ \begin{array} { l l } { 1 } & { \frac { 1 } { 6 } } \\ { 0 } & { 1 } \end{array} \right] .
$$

50.3 Write the implicit Runge–Kutta method

$$
\frac { 1 \ { \left| \begin{array} { l l } { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \end{array} \right| } } { { \left| \begin{array} { l l } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \end{array} \right| } }
$$

as a general linear method with $r = 2$ , $s = 1$ , by taking advantage of the FSAL property.

50.4 Show that it is possible, by using a suitable transformation, to reduce the general linear method derived in Exercise 50.3 to an equivalent method with $r = s = 1$ . Show that this new method is equivalent to the implicit mid-point rule Runge–Kutta method.

50.5 Write the PEC predictor–corrector method based on the order 2 Adams– Bashforth method and the order 2 Adams–Moulton method in general linear form.

50.6 The following two methods were once popular, but are now regarded as flawed because they are ‘weakly stable’:

$$
\begin{array} { l } { y _ { n } = y _ { n - 2 } + 2 h f ( x _ { n - 1 } , y _ { n - 1 } ) , } \\ { y _ { n } = y _ { n - 3 } + \frac { 3 } { 2 } h ( f ( x _ { n - 1 } , y _ { n - 1 } ) + f ( x _ { n - 2 } , y _ { n - 2 } ) ) . } \end{array}
$$

This means that, although the methods are stable, the polynomial $\alpha$ for each of them has more than one zero on the unit circle. Show how to write them as a cyclic composite pair, using general linear formulation, and that they no longer have such a disadvantage.

50.7 Consider the Runge–Kutta method

Modify this method in the same way as was proposed for (502b), and write the resulting two-value method in general linear form.

# 51 Consistency, Stability and Convergence

# 510 Definitions of consistency and stability

Since a general linear method operates on a vector of approximations to some quantities computed in the preceding step, we need to decide something about the nature of this information. For most numerical methods, it is obvious what form this takes, but for a method as general as the ones we are considering here there are many possibilities. At least we assume that the $i$ th subvector in $y ^ { \lfloor n - 1 \rfloor }$ represents $u _ { i } y ( x _ { n - 1 } ) + v _ { i } h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { 2 } )$ . The vectors $u$ and $v$ are characteristic of any particular method, subject to the freedom we have to alter $v$ by a scalar multiple of $u$ ; because we can reinterpret the method by changing $x _ { n }$ by some fixed multiple of $h$ . The choice of $u$ must be such that the stage values are each equal to $y ( x _ { n } ) + O ( h )$ . This means that $U u = \mathbf { 1 }$ . We always require the output result to be $u _ { i } y ( x _ { n } ) + v _ { i } h y ^ { \prime } ( x _ { n } ) + O ( h ^ { 2 } )$ and this means that $V u = u$ and that $V v + B \mathbf { 1 } = u + v$ . If we are given nothing about a method except the four defining matrices, then $V$ must have an eigenvalue equal to 1 and $u$ must be a corresponding eigenvector. It then has to be checked that the space of such eigenvectors contains a member such that $U u = \mathbf { 1 }$ and such that $B { \bf 1 } - u$ is in the range of $V - I$ .

If a method has these properties then it is capable of solving $y ^ { \prime } = 1$ , with $y ( 0 ) = a$ exactly, in the sense that if $y _ { i } ^ { [ 0 ] } = u _ { i } a + v _ { i } h$ , then for all $n = 1$ , $2$ . . . , $y _ { i } ^ { \left[ n \right] } = u _ { i } { \left( a + n h \right) } + v _ { i } h$ . This suggests the following definitions:

Definition 510A A general linear method $( A , U , B , V )$ is ‘preconsistent’ if there exists a vector u such that

$$
\begin{array} { r } { V u = u , } \\ { U u = \mathbf { 1 } . } \end{array}
$$

The vector u is the ‘preconsistency vector’.

Definition 510B A general linear method $( A , U , B , V )$ is ‘consistent’ if it is preconsistent with preconsistency vector u and there exists a vector v such that

$$
B { \bf 1 } + V v = u + v .
$$

Just as for linear multistep methods, we need a concept of stability. In the general linear case this is defined in terms of the power-boundedness of $V$ and, as we shall see, is related to the solvability of the problem $y ^ { \prime } = 0$ .

Definition 510C A general linear method $( A , U , B , V )$ is ‘stable’ if there exists a constant $C$ such that, for all $n = 1 , 2 , \ldots$ , $\| V ^ { n } \| \leq C$ .

# 511 Covariance of methods

Assume the interpretation of a method is agreed to, at least in terms of the choice of the preconsistency vector. We want to ensure that numerical approximations are transformed appropriately by a shift of origin. Consider the two initial value problems

$$
\begin{array} { r l r l } & { \boldsymbol { y } ^ { \prime } ( \boldsymbol { x } ) = f ( \boldsymbol { y } ( \boldsymbol { x } ) ) , } & & { \boldsymbol { y } ( x _ { 0 } ) = y _ { 0 } , } \\ & { \boldsymbol { z } ^ { \prime } ( \boldsymbol { x } ) = f ( \boldsymbol { z } ( \boldsymbol { x } ) - \boldsymbol { \eta } ) , } & & { \boldsymbol { z } ( x _ { 0 } ) = y _ { 0 } + \boldsymbol { \eta } , } \end{array}
$$

where $\eta \in \mathbb { R } ^ { N }$ is arbitrary. If (511a) has a solution, then (511b) also has a solution, which is identical to the former solution except that each point on the trajectory is translated by $\eta$ . If the solution is required at some $\overline { { x } } > x _ { 0 }$ , then the solution to (511a) at this point can be found by subtracting $\eta$ from the solution of (511b).

When each of these problems is solved by a numerical method, it is natural to expect that the numerical approximations should undergo the same covariance rule as for the exact solution. This means that in a single step of a method $( A , U , B , V )$ , interpreted as having a preconsistency vector $u$ , we want to be able to shift component $i$ of $y ^ { [ 0 ] }$ by $u _ { i } \eta$ , for all $i = 1 , 2 , \dots , r$ , and be assured that component $i$ of $y ^ { [ 1 ] }$ is also shifted by the same amount. At the same time the internal approximations (the stage values) should be shifted by $\eta$ . Of course no shift will take place to the stage derivatives.

The idea of covariance is illustrated in Figure 511(i). For an initial value problem $( f , y _ { 0 } )$ as given by (511a), the operation $\nu$ represents the computation of a numerical approximation to the solution on an interval $[ x _ { 0 } , { \overline { { x } } } ]$ , or at a single value of $x$ . Furthermore, $\sigma$ represents a shift of coordinates by a specific vector $\eta$ , as in the transformation to the problem (511b). Covariance is just the statement that the diagram in Figure 511(i) commutes, that is, that $\sigma \circ \nu = \nu \circ \sigma$ . The diagonal arrow representing these equal composed functions corresponds to the operation of solving the problem and then shifting coordinates, or else shifting first and then solving.

The covariance of the output values is equivalent to (510a) and the covariance of the stage values is equivalent to (510b). We have no interest in methods that are not covariant even though it is possible to construct artificial methods which do not have this property but can still yield satisfactory numerical results.

![](images/b2580a2d7e659c1a9ddbfac42031cd27cecd59487aa604e169006e0b0c7535d3.jpg)  
A commutative diagram for covariance

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

# 513 The necessity of stability

Stability has the effect of guaranteeing that errors introduced in any step of a computation do not have disastrous effects on later steps. The necessity of this property is expressed in the following result:

Theorem 513A A general linear method $( A , U , B , V )$ is convergent only if it is stable.

Proof. Suppose, on the contrary, that $\left\{ \left\| V ^ { n } \right\| : n = 1 , 2 , 3 , \ldots \right\}$ is unbounded. This implies that there exists a sequence of vectors $w _ { 1 } , w _ { 2 } , w _ { 3 } , . . .$ such that $\| w _ { n } \| = 1$ , for all $n = 1 , 2 , 3 , \ldots$ , and such that the sequence $\{ \| V ^ { n } w _ { n } \| : n =$ $1 , 2 , 3 , \ldots \}$ is unbounded. Consider the solution of the initial value problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 0 ,
$$

using $( A , U , B , V )$ , where $n$ steps are taken with stepsize $h = 1 / n$ , so that the solution is approximated at $\overline { { x } } = 1$ . Irrespective of the choice of the vector $u$ in Definition 512A, the convergence of the method implies that the sequence of approximations converges to zero. For the approximation carried out with $n$ steps, use as the starting approximation

$$
\phi \Big ( \frac { 1 } { n } \Big ) = \frac { 1 } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } w _ { n } .
$$

This converges to zero, because $\left\| \phi ( { 1 } / { n } ) \right\| = \left( { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } \right) ^ { - 1 }$ . The result, computed after $_ { n }$ steps, will then be

$$
V ^ { n } \phi \Big ( \frac { 1 } { n } \Big ) = \frac { 1 } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } V ^ { n } w _ { n } ,
$$

with norm

$$
\left\| V ^ { n } \phi \Big ( \frac { 1 } { n } \Big ) \right\| = \frac { \| V ^ { n } w _ { n } \| } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } .
$$

Because the sequence $n \mapsto \| V ^ { n } w _ { n } \|$ is unbounded, an infinite set of $n$ values will have the property that the maximum value of $\| V ^ { i } w _ { i } \|$ , for $i \ \leq \ n$ , will occur with $i = n$ . This means that (513a) has value 1 arbitrarily often, and hence is not convergent to zero as $n \longrightarrow \infty$ . $\sqcup$

# 514 The necessity of consistency

By selecting a specific differential equation, as in Subsection 513, we can prove that for covariant methods, consistency is necessary.

Theorem 514A Let $( A , U , B , V )$ denote a convergent method which is, moreover, covariant with preconsistency vector $u$ . Then there exists a vector $v \in \mathbb { R } ^ { r }$ , such that (510c) holds.

Proof. Consider the initial value problem

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( 0 ) = 0 ,
$$

with constant starting values $\phi ( h ) ~ = ~ 0$ and $\begin{array} { r l } { \overline { { x } } } & { { } = ~ 1 } \end{array}$ . The sequence of approximations, when $n$ steps are to be taken with $h = 1 / n$ , is given by

$$
y ^ { [ i ] } = \frac { 1 } { n } B \mathbf { 1 } + V y ^ { [ i - 1 ] } , \qquad i = 1 , 2 , \ldots , n .
$$

This means that the error vector, after the $n$ steps have been completed, is given by

$$
\begin{array} { c } { { y ^ { [ n ] } - u = \displaystyle \frac { 1 } { n } \left( I + V + V ^ { 2 } + \cdots + V ^ { n - 1 } \right) B \mathbf { 1 } - u } } \\ { { \displaystyle = \displaystyle \frac { 1 } { n } \left( I + V + V ^ { 2 } + \cdots + V ^ { n - 1 } \right) ( B \mathbf { 1 } - u ) . } } \end{array}
$$

Because $V$ has bounded powers, it can be written in the form

$$
V = S ^ { - 1 } \left[ \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W } } \end{array} \right] S ,
$$

where $I$ is $\widetilde { r } \times \widetilde { r }$ for $\widetilde r \le r$ and $W$ is power-bounded and is such that $1 \not \in \sigma ( W )$ This means that

$$
y ^ { [ n ] } - u = S ^ { - 1 } \left[ \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { \frac { 1 } { n } ( I - W ) ^ { - 1 } ( I - W ^ { n } ) } } \end{array} \right] S ( B { \bf 1 } - u ) ,
$$

whose limit as $n \longrightarrow \infty$ is

$$
\begin{array} { r } { S ^ { - 1 } \left[ \begin{array} { l l } { I } & { 0 } \\ { 0 } & { 0 } \end{array} \right] S ( B \mathbf { 1 } - u ) . } \end{array}
$$

If $y ^ { \lfloor n \rfloor } - u$ is to converge to $0$ as $n \longrightarrow \infty$ , then $S ( B \mathbf { 1 } - u )$ has only zero in its first $\widetilde { r }$ components. Write this vector in the form

$$
\begin{array} { c } { S ( B \mathbf { 1 } - u ) = \left[ \begin{array} { c } { 0 } \\ { \left( I - W \right) \widetilde v } \end{array} \right] } \\ { = \left( I - \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { W } \end{array} \right] \right) S v } \\ { = S ( I - V ) v , } \end{array}
$$

where

$$
v = S ^ { - 1 } \left[ \begin{array} { l } { 0 } \\ { \widetilde { v } } \end{array} \right] .
$$

Thus $B { \bf 1 } + V v = u + v$ .

# 515 Stability and consistency imply convergence

We show that stable and consistent methods are convergent. This is done in three steps. The first is to analyse the internal and the external local truncation error; the second is to obtain a difference inequality relating the total error at the end of a step with the total error at the end of the previous step. Finally, we find a bound on the global error and show that it converges to zero.

In the truncation error estimation, we need to decide what the input and output approximations and the internal stages are intended to approximate. The choice we make here is determined by a wish for simplicity: we do not need good error bounds, only bounds sufficiently strong to enable us to establish convergence. Our assumption will be that $y _ { i } ^ { \left[ n \right] }$ approximates $u _ { i } y ( x _ { n } ) + h v _ { i } y ^ { \prime } ( x _ { n } )$ , and that the internal stage $Y _ { i }$ approximates $y ( x _ { n - 1 } + h c _ { i } )$ , where $c _ { i }$ is determined by what happens to the time variable.

We need to make some assumptions about the problem whose solution is being approximated. What we shall suppose is that there exists a closed set $S$ in $\mathbb { R } ^ { N }$ such that all values of $y ( x )$ that will ever arise in a trajectory lie in the interior of $S$ . Furthermore, we suppose that for any $y \in S$ , $\| y \| \leq M$ and $\| f ( y ) \| \leq L M$ . Also, we suppose that for $y , z \in S$ , $\| f ( y ) - f ( z ) \| \leq L \| y - z \|$ . Since we are concerned with the limit as $h  0$ , we restrict the value of $h$ to an interval $( 0 , h _ { 0 } ]$ , for some $h _ { 0 } > 0$ .

With this in mind, we find bounds as follows:

Lemma 515A Assume that $h \leq h _ { 0 }$ , chosen so that $h _ { 0 } L \| A \| _ { \infty } < 1$ . Define $\epsilon$ as the vector in $\mathbb { R } ^ { s }$ satisfying

$$
\sum _ { j = 1 } ^ { s } ( \delta _ { i j } - h _ { 0 } L | a _ { i j } | ) \epsilon _ { j } = \frac { 1 } { 2 } c _ { i } ^ { 2 } + \sum _ { j = 1 } ^ { s } | a _ { i j } c _ { j } | .
$$

Let y [n−1]i $\widehat { y } _ { i } ^ { \lfloor n - 1 \rfloor } = u _ { i } y ( x _ { n - 1 } ) + v _ { i } h y ^ { \prime } ( x _ { n - 1 } )$ , $\widehat { y } _ { i } ^ { [ n ] } = u _ { i } y ( x _ { n } ) + v _ { i } h y ^ { \prime } ( x _ { n } )$ , for $i \ =$ $1 , 2 , \ldots , r$ , and ${ \hat { Y _ { i } } } = y ( x _ { n - 1 } + h c _ { i } )$ , for $i = 1 , 2 , \dots , s$ , where $c = A { \bf 1 } + U v$ . Also let ${ \widetilde { Y _ { i } } }$ denote the value of $Y _ { i }$ that would be computed exactly using $\widehat { y } ^ { [ n - 1 ] }$ as input vector $y ^ { [ n - 1 ] }$ . Assume the function $f$ satisfies a Lipschitz condition with constant $L$ and that the exact solution to the initial value problem satisfies $\| y ( x ) \| \leq M$ , $\| y ^ { \prime } ( x ) \| \leq L M$ . Then

$$
\begin{array} { r l } & { \| \widehat { \gamma } _ { \xi } - h \displaystyle \sum _ { j = 1 } ^ { N } a _ { j , j } f ( \widehat { \gamma } _ { j } ) - \displaystyle \sum _ { j = 1 } ^ { N } { \cal E } _ { j } y _ { j } ^ { [ j - 1 ] } \| } \\ & { \qquad \leq { \small \widehat { h } ^ { 2 } } \displaystyle \sum _ { j = 1 } ^ { N } a _ { j } ( \displaystyle \frac { 1 } { 2 } a _ { j } ^ { 2 } + \displaystyle \sum _ { j = 1 } ^ { N } | a _ { j } z _ { j } | ) , } \\ & { \| \widehat { \gamma } _ { \xi } ^ { [ i ] } - h \displaystyle \sum _ { j = 1 } ^ { N } b _ { j } ( \widehat { \gamma } _ { j } ) - \displaystyle \sum _ { j = 1 } ^ { N } b _ { j } \widehat { \gamma } _ { j } ^ { [ j - 1 ] } \| } \\ & { \qquad \leq { \small \widehat { h } ^ { 2 } } L ^ { 2 } { \small \widehat { h } } ( \displaystyle \frac { 1 } { 2 } | a _ { i } | + | x _ { i } | + \displaystyle \sum _ { j = 1 } ^ { N } b _ { j } c _ { i j } | ) , } \\ & { \| \widehat { \gamma } _ { \xi } ^ { [ i ] } - h \displaystyle \sum _ { j = 1 } ^ { N } b _ { j } ( \widehat { \gamma } _ { j } ) - \displaystyle \sum _ { j = 1 } ^ { N } V _ { j } \widehat { \gamma } _ { j } ^ { [ j - 1 ] } \| } \\ & { \qquad \leq { \small \widehat { h } ^ { 2 } } L ^ { 2 } { \small \widehat { h } } ( \displaystyle \frac { 1 } { 2 } | a _ { i } | + | x _ { i } | + \displaystyle \sum _ { j = 1 } ^ { N } | b _ { j } c _ { i j } | + h _ { i } c _ { i j } \displaystyle \sum _ { j = 1 } ^ { N } | b _ { j } | ) . } \end{array}
$$

Proof. We first note that

$$
\begin{array} { r l r } {  { \| y ( x _ { n - 1 } + h c _ { i } ) - y ( x _ { n - 1 } ) \| = h \| \int _ { 0 } ^ { c _ { i } } y ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi \| } } \\ & { } & { \leq h \int _ { 0 } ^ { c _ { i } } \| y ^ { \prime } ( x _ { n - 1 } + h \xi ) \| d \xi } \\ & { } & { \leq | c _ { i } | h L M . } \end{array}
$$

We now have

$$
\widehat { Y } _ { i } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( \widehat { Y } _ { j } ) - \sum _ { j = 1 } ^ { r } U _ { i j } \widehat { y } _ { j } ^ { [ n - 1 ] } = T _ { 1 } + T _ { 2 } + T _ { 3 } + T _ { 4 } ,
$$

where

$$
\begin{array} { l } { \displaystyle T _ { 1 } = \widehat { Y } _ { i } - y ( x _ { n - 1 } ) - h \int _ { 0 } ^ { c _ { i } } f ( y ( x _ { n - 1 } + h \xi ) ) d \xi , } \\ { \displaystyle T _ { 2 } = y ( x _ { n - 1 } ) + c _ { i } h y ^ { \prime } ( x _ { n - 1 } ) - \sum _ { j = 1 } ^ { r } U _ { i j } \widehat { y } _ { j } ^ { [ n - 1 ] } - \sum _ { j = 1 } ^ { s } a _ { i j } h y ^ { \prime } ( x _ { n - 1 } ) , } \\ { \displaystyle T _ { 3 } = h \int _ { 0 } ^ { c _ { s } } \Big ( f ( y ( x _ { n - 1 } + h \xi ) ) - y ^ { \prime } ( x _ { n - 1 } ) \Big ) d \xi , } \\ { \displaystyle T _ { 4 } = - h \sum _ { j = 1 } ^ { s } a _ { i j } \Big ( f ( y ( x _ { n - 1 } + h c _ { j } ) ) - y ^ { \prime } ( x _ { n - 1 } ) \Big ) . } \end{array}
$$

Simplify and estimate these terms, and we find

$$
\begin{array} { r l } { \tau _ { \perp } = \boldsymbol { x } _ { \perp } ( x _ { \perp } + h _ { \perp } x _ { \perp } ) - \boldsymbol { x } _ { \perp } f _ { \perp } ^ { \mathrm { e x t } } ( x _ { \perp - 1 } ) - h _ { \perp } ^ { \mathrm { e x t } } \hat { \xi } _ { \perp } ^ { \mathrm { i n k } } x _ { \perp } + h _ { \perp } ^ { \mathrm { e x t } } \mathcal { U } = 0 , } & { } \\ { \tau _ { \perp } = \boldsymbol { x } _ { \perp } ( x _ { \perp } - 1 ) + \xi _ { \perp } \dot { \mu } ( x _ { \perp - 1 } ) } & { } \\ { \tau _ { \perp } = \boldsymbol { x } _ { \perp } \sum _ { \ell \in \mathcal { J } } \bigg [ \mathrm { a n d } _ { \ell } ( x _ { \perp - 1 } ) - \mathrm { i } \mathrm { B } _ { 2 \ell } \boldsymbol { x } _ { \perp } ^ { \mathrm { e x t } } ( x _ { \perp - 1 } ) \bigg ] - \sum _ { \ell = \mathcal { L } _ { \ell } } ^ { \infty } a _ { \ell } \dot { \mu } ( x _ { \perp - 1 } ) } \\ { - \frac { \xi _ { \perp } } { \sqrt { \pi } } \tau _ { \perp } \bigg [ \mathrm { a n d } _ { \ell } ( x _ { \perp - 1 } ) - \mathrm { i } \mathrm { A n d } _ { \ell } \boldsymbol { x } _ { \perp } + \mathrm { i } \mathrm { A n d } _ { \ell } \boldsymbol { x } _ { \perp } } \\ { - \Omega _ { \ell } \mathrm { e x t } \mathrm { e x t } \mathrm { e x t } _ { \perp } } & { } \\ { | \Omega _ { \ell } | = \boldsymbol { x } _ { \perp } \bigg [ \displaystyle \int _ { 0 } ^ { \mathcal { L } } \bigg ( g ( x _ { \perp - 1 } + x _ { \ell } ) - f _ { \ell } ( x _ { \ell - 1 } ) \bigg ) \bigg ] d \ell } & { } \\ { \leq \boldsymbol { h } \int _ { 0 } ^ { \mathcal { L } } \bigg [ \mathrm { i f f } ( x _ { \perp - 1 } + h _ { \ell } ) - f _ { \ell } ( x _ { \ell - 1 } ) \bigg ] \Big ] d \ell } & { } \\ { \leq \boldsymbol { h } \int _ { 0 } ^ { \mathcal { L } } \bigg [ \mathrm { i n d } _ { \ell - 1 } - \boldsymbol { x } _ { \ell } \mathrm { e x t } _ { \perp } \bigg ] - \boldsymbol { y } \bigg [ \mathrm { e x t } _ { \perp } \bigg ] } & { } \end{array}
$$$$
\begin{array} { r l } { | T | \leq 1 - \delta \left| \displaystyle \int _ { 0 } ^ { T } \left( \left. \beta ( S | S | S | S | S | + \delta ( \alpha ) - \beta ( \alpha ) \nu _ { 1 } ( S ) \right. \right) ^ { 2 } \right| } & { } \\ { \leq \beta \displaystyle \int _ { 0 } ^ { T } \left| \beta ( S | \alpha - \alpha + \beta ( \alpha ) - \beta ( \alpha ) \nu _ { 1 } ( S | \alpha - \alpha ) ) \right| \beta ( \alpha - \alpha ) } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \left| \beta ( S | \alpha - \alpha + \alpha + \beta ( \alpha ) - \alpha ( \alpha - \alpha ) ) \right| \alpha } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \Delta \sigma \int _ { 0 } ^ { T } \exp \xi ( \alpha - \alpha ) } \\ { - \frac { 2 } { 2 } \alpha ^ { 2 } \delta ^ { 2 } d \alpha \beta _ { 1 } ^ { 2 } } \\ { | T | = \alpha | \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( S | S | S | S | - \delta ( \alpha ) ) - \beta ( \alpha ) \nu _ { 1 } ( S | \alpha - \alpha ) \right| } \\ { \leq \alpha \displaystyle \sum _ { \beta = 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha ( S | S | \alpha - \alpha ) + \beta ( \alpha ) - \beta ( \alpha - \alpha ) ) \right| } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \sum _ { \alpha = 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha ( S | \alpha - \alpha ) - \beta ( \alpha ) \nu _ { 1 } ( S | \alpha - \alpha ) ) \right| } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \Delta \sigma \int _ { 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha - \alpha ) - \beta ( \alpha ) \right| } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \Delta \sigma \int _ { 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha - \alpha ) - \beta ( \alpha ) \right| } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \Delta \sigma \int _ { 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha - \alpha ) \right| } \\ { \leq \alpha \displaystyle \int _ { 0 } ^ { T } \alpha ^ { 2 } \Delta \sigma \int _ { 0 } ^ { T } \alpha ^ { 2 } \left| \beta ( \alpha - \alpha ) \right| } \end{array}
$$

so that, combining these estimates, we arrive at (515a).

To verify (515b), we write

$$
\widehat { y } _ { i } ^ { [ n ] } - h \sum _ { j = 1 } ^ { s } b _ { i j } f ( \widehat { Y } _ { j } ) - \sum _ { j = 1 } ^ { r } V _ { i j } \widehat { y } _ { j } ^ { [ n - 1 ] } = T _ { 1 } + T _ { 2 } + T _ { 3 } + T _ { 4 } ,
$$

where

$$
\begin{array} { l } { \displaystyle T _ { 1 } = u _ { i } \Big ( y ( x _ { n - 1 } + h ) - y ( x _ { n - 1 } ) - h \int _ { 0 } ^ { 1 } y ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi \Big ) , } \\ { \displaystyle T _ { 2 } = v _ { i } h y ^ { \prime } ( x _ { n - 1 } + h ) + \Big ( u _ { i } - \sum _ { j = 1 } ^ { s } b _ { i j } - \sum _ { j = 1 } ^ { r } V _ { i j } v _ { j } \Big ) h y ^ { \prime } ( x _ { n - 1 } ) , } \\ { \displaystyle T _ { 3 } = h u _ { i } \int _ { 0 } ^ { 1 } \big ( y ^ { \prime } ( x _ { n - 1 } + h \xi ) - y ^ { \prime } ( x _ { n - 1 } ) \big ) d \xi , } \\ { \displaystyle T _ { 4 } = - h \sum _ { j = 1 } ^ { s } b _ { i j } \big ( y ^ { \prime } ( x _ { n - 1 } + h c _ { j } ) - y ^ { \prime } ( x _ { n - 1 } ) \big ) . } \end{array}
$$

We check that $T _ { 1 } = 0$ and that, because $\begin{array} { r } { \sum _ { j = 1 } ^ { s } b _ { i j } + \sum _ { j = 1 } ^ { r } V _ { i j } v _ { j } = u _ { i } + v _ { i } } \end{array}$ , $T _ { 2 }$ simplifies to $h v _ { i } ( y ^ { \prime } ( x _ { n - 1 } + h ) - y ^ { \prime } ( x _ { n - 1 } ) )$ so that $\| T _ { 2 } \| \le h ^ { 2 } L ^ { 2 } M | v _ { i } |$ . Similarly, $\| T _ { 3 } \| \le \frac { 1 } { 2 } h ^ { 2 } L ^ { 2 } M | u _ { i } |$ − and $\begin{array} { r } { \left\| T _ { 4 } \right\| \leq h ^ { 2 } L ^ { 2 } M \sum _ { j = 1 } ^ { s } \left| b _ { i j } c _ { j } \right| } \end{array}$ . To prove (515c) we first need to estimate the elements of $\widetilde Y - \widehat Y$ by deducing from (515a) that

$$
\begin{array} { r } { \Big \| \left( \widetilde { Y } _ { i } - \widehat { Y } _ { i } \right) - h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \Big ( f ( \widetilde { Y } _ { j } ) - f ( \widehat { Y } _ { j } ) \Big ) \Big \| \le \Big ( \frac 1 2 c _ { i } ^ { 2 } + \displaystyle \sum _ { j = 1 } ^ { s } | a _ { i j } c _ { j } | \Big ) h ^ { 2 } L ^ { 2 } M , } \end{array}
$$

and hence that

$$
\| \widetilde { Y } _ { j } - \widehat { Y } _ { j } \| \le h ^ { 2 } L ^ { 2 } M \epsilon _ { j } .
$$

Thus,

$$
\left\| h \sum _ { j = 1 } ^ { s } b _ { i j } \big ( f ( \widetilde Y _ { j } ) - f ( \widehat Y _ { j } ) \big ) \right\| \leq h ^ { 2 } L ^ { 3 } M h _ { 0 } \sum _ { j = 1 } ^ { s } | b _ { i j } | \epsilon _ { j } .
$$

Add this estimate of $\begin{array} { r l } { \left\| h \sum _ { j = 1 } ^ { s } b _ { i j } \left( f ( \widetilde { Y } _ { j } ) - f ( \widehat { Y } _ { j } ) \right) \right\| } & { { } } \end{array}$ to (515b) to obtain (515c).

The next step in the investigation is to find a bound on the local truncation error.

Lemma 515B Under the conditions of Lemma 515A, the exact solution and the computed solution in a step are related by

$$
\widehat { y } _ { i } ^ { [ n ] } - y _ { i } ^ { [ n ] } = \sum _ { j = 1 } ^ { r } V _ { i j } \left( \widehat { y } _ { j } ^ { [ n - 1 ] } - y _ { j } ^ { [ n - 1 ] } \right) + K _ { i } ^ { [ n ] } , \qquad i = 1 , 2 , \ldots , r ,
$$

where

$$
\| K ^ { [ n ] } \| \leq h \alpha \operatorname* { m a x } _ { i = 1 } ^ { r } \left\| \widehat { y } _ { i } ^ { [ n - 1 ] } - y _ { i } ^ { [ n - 1 ] } \right\| + \beta h ^ { 2 } ,
$$

and $\alpha$ and $\beta$ are given by

$$
\alpha = L \operatorname* { m a x } _ { i = 1 } ^ { s } | \overline { { \epsilon } } _ { i } | ,
$$

where $\overline { { \epsilon } }$ is given by

$$
\sum _ { j = 1 } ^ { s } ( \delta _ { i j } - h _ { 0 } L | a _ { i j } | ) \overline { { { \epsilon } } } _ { j } = \sum _ { j = 1 } ^ { s } | U _ { i j } | , \qquad i = 1 , 2 , \ldots , s ,
$$

and

$$
\beta = L ^ { 2 } M \operatorname* { m a x } _ { i = 1 } ^ { s } \Big ( \frac { 1 } { 2 } | u _ { i } | + | v _ { i } | + \sum _ { j = 1 } ^ { s } | b _ { i j } c _ { j } | + h _ { 0 } L \sum _ { j = 1 } ^ { s } | b _ { i j } | \epsilon _ { j } \Big ) ,
$$

where $\epsilon$ is as in Lemma 515A.

Proof. From (515c), and the relation

$$
y _ { i } ^ { [ n ] } - h \sum _ { j = 1 } ^ { s } b _ { i j } f ( Y _ { j } ) - \sum _ { j = 1 } ^ { r } V _ { i j } y _ { j } ^ { [ n - 1 ] } = 0 ,
$$

we have

$$
\begin{array} { r l } { \displaystyle \left\| \widehat { \mathcal { I } } _ { i } ^ { ( n - 1 ) } - \mathcal { I } _ { i } ^ { [ n ] } - \sum _ { j = 1 } ^ { \ell } V _ { i j } \left( \widehat { \mathcal { I } } _ { j } ^ { ( n - 1 ) } - 9 _ { j } ^ { ( n - 1 ) } \right) \right\| } & { } \\ { \displaystyle \leq h \sum _ { j = 1 } ^ { \ell } \| b _ { i j } \| \left\| f ( \widehat { Y } _ { j } ^ { ( n ) } ) - f ( Y _ { j } ) \right\| } & { } \\ { \displaystyle \qquad + h ^ { 2 } L ^ { 2 } M \left( \frac { 1 } { 2 } \| u _ { i } \| + | v _ { i } | + \sum _ { j = 1 } ^ { s } | b _ { i j } c _ { j } | + h _ { 0 } L \sum _ { j = 1 } ^ { s } | b _ { i j } | \epsilon _ { j } \right) } & { } \\ { \displaystyle \leq h L \sum _ { j = 1 } ^ { \ell } | b _ { i j } | \left\| Y _ { j } - \widetilde { Y } _ { j } ^ { * } \right\| } & { } \\ { \displaystyle \qquad + h ^ { 2 } L ^ { 2 } M \left( \frac { 1 } { 2 } | u _ { i } | + | v _ { i } | + \sum _ { j = 1 } ^ { s } | b _ { i j } c _ { j } | + h _ { 0 } L \sum _ { j = 1 } ^ { s } | b _ { i j } | \epsilon _ { j } \right) . } \end{array}
$$

Bound $\eta _ { j } = \| \widetilde { Y } _ { j } - Y _ { j } \|$ using the estimate

$$
\left\| \widetilde { Y } _ { j } - Y _ { j } - \sum _ { k = 1 } ^ { r } U _ { j k } \left( \widehat { y } _ { k } ^ { [ n - 1 ] } - y _ { k } ^ { [ n - 1 ] } \right) \right\| \leq h L \sum _ { k = 1 } ^ { s } | a _ { j k } | \cdot \| \widetilde { Y } _ { k } - Y _ { k } \| ,
$$

which leads to

$$
\sum _ { k = 1 } ^ { s } ( \delta _ { j k } - h _ { 0 } L | a _ { j k } | ) \eta _ { k } \leq \sum _ { k = 1 } ^ { r } | U _ { j k } | \operatorname* { m a x } _ { k = 1 } ^ { r } \left\| \widehat { y } _ { k } ^ { [ n - 1 ] } - y _ { k } ^ { [ n - 1 ] } \right\|
$$

and to

$$
\| \widetilde { Y } _ { j } - Y _ { j } \| \le h \overline { { \epsilon } } _ { j } \operatorname* { m a x } _ { k = 1 } ^ { s } \| \widetilde { Y } _ { k } - Y _ { k } \| .
$$

Substitute this bound into (515d) and we obtain the required result.

To complete the argument that stability and consistency imply convergence, we estimate the global error in the computation of $y ( { \overline { { x } } } )$ by carrying out $n$ steps from an initial value $y ( x _ { 0 } )$ using a stepsize equal to $h = ( \overline { { x } } - x _ { 0 } ) / n$ .

Lemma 515C Using notations already introduced in this subsection, together with

$$
\begin{array} { r } { { \cal { E } } ^ { [ i ] } = \left[ \begin{array} { c } { \widehat { y } _ { 1 } ^ { [ i ] } - y _ { 1 } ^ { [ i ] } } \\ { \widehat { y } _ { 2 } ^ { [ i ] } - y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { \widehat { y } _ { r } ^ { [ i ] } - y _ { r } ^ { [ i ] } } \end{array} \right] , \qquad i = 0 , 1 , 2 , \ldots , n , } \end{array}
$$

for the accumulated error in step $i$ , we have the estimate

$$
\| E ^ { [ n ] } \| \leq \left\{ \begin{array} { l l } { \exp ( \alpha C ( \overline { { x } } - x _ { 0 } ) ) \| E ^ { [ 0 ] } \| + \frac { \beta h } { \alpha } ( \exp ( \alpha C ( \overline { { x } } - x _ { 0 } ) ) - 1 ) , } & { \alpha > 0 , } \\ { \exp ( \alpha C ( \overline { { x } } - x _ { 0 } ) ) \| E ^ { [ 0 ] } \| + \beta C ( \overline { { x } } - x _ { 0 } ) h , } & { \alpha = 0 , } \end{array} \right.
$$

where $C = \mathrm { s u p } _ { i = 0 , 1 , \dots } \| V ^ { i } \| _ { \infty }$ and the norm of $E ^ { \left[ n \right] }$ is defined as the maximum of the norms of its $T$ subvectors.

Proof. The result of Lemma 515B can be written in the form

$$
E ^ { [ i ] } = ( V \otimes I ) E ^ { [ i - 1 ] } + K ^ { [ i ] } ,
$$

from which it follows that

$$
E ^ { [ i ] } = ( V ^ { i } \otimes I ) E ^ { [ 0 ] } + \sum _ { j = 1 } ^ { i } ( V ^ { j - 1 } \otimes I ) K ^ { [ i + 1 - j ] } ,
$$

and hence that

$$
\| E ^ { [ i ] } \| \leq C \| E ^ { [ 0 ] } \| + \sum _ { j = 0 } ^ { i - 1 } C \| K ^ { [ i - j ] } \| .
$$

Insert the known bounds on the terms on the right-hand side, and we find

$$
\| E ^ { [ i ] } \| \le \alpha h C \sum _ { j = 0 } ^ { i - 1 } \| E ^ { [ j ] } \| + C i \beta h ^ { 2 } + C \| E ^ { [ 0 ] } \| .
$$

This means that $\| E ^ { \lfloor i \rfloor } \|$ is bounded by $\eta _ { i }$ defined by

$$
\eta _ { i } = \alpha h C \sum _ { j = 0 } ^ { i - 1 } \eta _ { j } + C i \beta h ^ { 2 } + \eta _ { 0 } , \qquad \eta _ { 0 } = C \| E ^ { [ 0 ] } \| .
$$

To simplify this equation, find the difference of the formulae for $\eta _ { i }$ and $\eta _ { i - 1 }$ to give the difference equation

$$
\eta _ { i } - \eta _ { i - 1 } = \alpha h C \eta _ { i - 1 } + C \beta h ^ { 2 }
$$

with solution

$$
\eta _ { i } = ( 1 + h \alpha C ) ^ { i } \eta _ { 0 } + \frac { \beta h } { \alpha } ( ( 1 + h \alpha C ) ^ { i } - 1 ) ,
$$

or, if $\alpha = 0$ ,

$$
\eta _ { i } = \eta _ { 0 } + i C \beta h ^ { 2 } .
$$

Substitute $i = n$ and we complete the proof.

We summarize the implications of these results:

Theorem 515D A stable and consistent general linear method is convergent.

# Exercises 51

51.1 Show that the general linear method

$$
\left[ { \frac { 0 \left| 1 a \right. \quad a } { \left. b \right. \left| 1 0 \right. } } \right]
$$

is preconsistent with $u = [ 1 , 0 ] ^ { \scriptscriptstyle 1 }$ . For what values of $a$ , $b$ and $c$ is the method consistent?

51.2 Show that a linear multistep method, interpreted as a general linear method, is convergent if and only if the corresponding one-leg method is convergent.

51.3 For what values of $a$ , $b$ , $c$ , $d$ , $e$ , $f$ and $g$ is the method

$$
\left[ { \frac { 0 \ \left| \ a \ b \ \right. } { \ c \ \left| \ d \ c \ \right. } } \right]
$$

capable of producing convergent approximations?

# 52 The Stability of General Linear Methods

# 520 Introduction

The linear stability analysis of general linear methods, as for the special cases of Runge–Kutta and linear multistep methods, is based on the differential equation

$$
y ^ { \prime } ( x ) = q y ( x ) .
$$

The idea will be to consider the influence of a single step of the method on an incoming vector $y ^ { \lfloor n - 1 \rfloor }$ . We obtain a relation of the form

$$
y ^ { [ n ] } = M ( z ) y ^ { [ n - 1 ] } ,
$$

where $z = h q$ and $M ( z )$ is an $r \times r$ matrix-valued function of the complex variable $z$ .

Definition 520A For a general linear method $( A , U , B , V )$ , the ‘stability matrix’ $M ( z )$ is defined by

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U .
$$

As we have anticipated, we have the following result:

Theorem 520B Let $M ( z )$ denote the stability matrix for a general linear method. Then, for a linear differential equation (520a), (520b) holds with $z = h q$ .

Proof. For the special problem defined by $f ( y ) = q y$ , the vector of stage derivatives $F$ is related to the vector of stage values $Y$ by $F = q Y$ . Hence, (500c) reduces to the form

$$
\left[ \begin{array} { c } { { Y } } \\ { { y ^ { [ n ] } } } \end{array} \right] = \left[ \begin{array} { c c } { { A } } & { { U } } \\ { { B } } & { { V } } \end{array} \right] \left[ \begin{array} { c } { { z Y } } \\ { { y ^ { [ n - 1 ] } } } \end{array} \right] .
$$

It follows that $Y = ( I - z A ) ^ { - 1 } U y ^ { \lfloor n - 1 \rfloor }$ , and that

$$
y ^ { [ n ] } = z B Y + V y ^ { [ n - 1 ] } = M ( z ) y ^ { [ n - 1 ] } .
$$

If the method is stable, in the sense of Section 51, then $M ( 0 ) = V$ will be power-bounded. The idea now is to extend this to values of $z$ in the complex plane where $M ( z )$ has bounded powers.

Just as for Runge–Kutta and linear multistep methods, associated with each method is a stability region. This, in turn, is related to the characteristic polynomial of $M ( z )$ .

Definition 520C Let $( A , U , B , V )$ denote a general linear method and $M ( z )$ the corresponding stability matrix. The ‘stability function’ for the method is the polynomial $\Phi ( w , z )$ given by

$$
\Phi ( w , z ) = \operatorname* { d e t } ( w I - M ( z ) ) ,
$$

and the ‘stability region’ is the subset of the complex plane such that if $z$ is in this subset, then

$$
\operatorname* { s u p } _ { n = 1 } \| M ( z ) ^ { n } \| < \infty .
$$

We refer to the ‘instability region’ as the complement of the stability region.

Note that in applications of these definitions, $\Phi ( w , z )$ may be a rational function. Quite often, the essential properties will be contained in just the numerator of this expression. We equally refer to the numerator of this rational function as the stability function.

We state the following obvious result without proof.

Theorem 520D The instability region for $( A , U , B , V )$ is a subset of the set of points $z$ , such that $\Phi ( w , z ) = 0$ , where $| w | \geq 1$ . The instability region is a superset of the points defined by $\Phi ( w , z ) = 0$ , where $| w | > 1$ .

The unanswered question in this result is: ‘Which points on the boundary of the stability region are actually members of it?’ This is not always a crucial question, and we quite often interpret the stability region as the ‘strict stability region’, consisting of those $z$ for which

$$
\operatorname* { l i m } _ { n \to \infty } \| M ( z ) ^ { n } \| = 0 .
$$

This will correspond to the set of $z$ values such that $| w | < 1$ , for any $w$ satisfying $\Phi ( w , z ) = 0$ .

In particular, we can define A-stability.

Definition 520E A general linear method is ‘A-stable’ if $M ( z )$ is powerbounded for every $z$ in the left half complex plane.

Just as for Runge–Kutta and linear multistep methods, A-stability is the ideal property for a method to possess for it to be applicable to stiff problems. Corresponding to the further requirement for Runge–Kutta methods that $R ( \infty ) = 0$ , we have the generalization of L-stability to general linear methods.

Definition 520F A general linear method is L-stable if it is A-stable and $\rho ( M ( \infty ) ) = 0$ .

# 521 Methods with maximal stability order

Although a full discussion of the order of general linear methods will be postponed until Section 53, we look here at the relationship between stability and methods with a property closely related to order.

Definition 521A A method with stability function $\Phi ( w , z )$ has ‘stability order’ $\widetilde { p }$ if

$$
\Phi ( \exp ( z ) , z ) = O ( z ^ { \widetilde { p } + 1 } ) .
$$

Suppose the stability function is given by

$$
\Phi ( w , z ) = \sum _ { j = 0 } ^ { k } w ^ { k - j } \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { j } ,
$$

where $k$ is the $w$ -degree of $\Phi$ and $\nu _ { j }$ is the $z$ -degree of the coefficient of $w ^ { k - j }$ . We can regard the sequence of integers

$$
\nu = [ \nu _ { 0 } , \nu _ { 1 } , \ldots , \nu _ { k } ] ,
$$

as representing the complexity of the stability function $\Phi$ . To include all sensible cases without serious redundancies, we always assume that $\nu _ { j } \geq - 1$ for $j = 0 , 1 , 2 , \ldots , k$ with strict inequality in the cases $j = 0$ and $j = k$ .

It is interesting to ask the question: ‘For a given sequence $\nu$ , what is the highest possible stability order?’. The question can be looked at in two parts. First, there is the question of determining for what $\widetilde { p }$ it is possible to find a function $\Phi$ with a given complexity and with stability order $\hat { p }$ . Secondly, there is the question of finding a general linear method corresponding to a given $\Phi$ , with order $p$ as close as possible to $\widetilde { p }$ . The first half of the question can be firmly answered and is interesting since it gives rise to speculations about possible generalizations of the Ehle results on rational approximations to the exponential function. The definitive result that we have referred to is as follows:

Theorem 521B For given $\nu$ , the maximum possible stability order is given by

$$
\widetilde { p } = \sum _ { j = 0 } ^ { k } ( \nu _ { j } + 1 ) - 2 .
$$

Proof. If order higher than $\hat { p }$ given by (521a) is possible, then

$$
\sum _ { j = 0 } ^ { k } \exp ( ( k - j ) z ) \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { l } = C _ { \widetilde { p } + 2 } z ^ { \widetilde { p } + 2 } + C _ { \widetilde { p } + 3 } z ^ { \widetilde { p } + 3 } + \cdots ,
$$

where the right-hand side is convergent for any $z$ . Differentiate $\nu _ { k } + 1$ times and multiply the result by $\exp ( - z )$ . We now have a stability function with complexity $[ \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { k - 1 } ]$ , where the $w$ -degree can be reduced even further if $\nu _ { k - 1 } = - 1$ . Furthermore, the new approximation also has a stability order contrary to the bound we are trying to prove. Thus, by an induction argument


<!-- chunk 0007: pages 421-484 -->
we reduce to the case $k = 0$ , and it remains to prove that there does not exist a non-zero polynomial $P$ of degree $\nu _ { 0 }$ such that

$$
P ( z ) = O ( z ^ { \nu _ { 0 } + 1 } ) .
$$

To show that an approximation with stability order $\hat { p }$ given by (521a) exists, it is possible to reverse the non-existence argument and to construct the required stability function recursively, but we use a different approach.

Consider the rational function

$$
\phi ( t ) = \prod _ { j = 0 } ^ { k } ( t + j ) ^ { - \nu _ { j } - 1 } ,
$$

with partial fraction expansion which can be written in the form

$$
\phi ( t ) = \sum _ { j = 0 } ^ { k } \sum _ { l = 0 } ^ { \nu _ { j } } \frac { l ! \alpha _ { j l } } { ( j + t ) ^ { l + 1 } } .
$$

Calculate the integral

$$
\frac { 1 } { 2 \pi i } \oint _ { C } \phi ( t ) \exp _ { \widetilde { p } } ( t z ) d t ,
$$

where

$$
\exp _ { \widetilde { p } } ( z ) = \sum _ { j = 0 } ^ { \widetilde { p } } \frac { z ^ { j } } { j ! }
$$

is the polynomial of degree $\hat { p }$ approximating the exponential function to within $O ( z ^ { \overleftarrow { p } + 1 } )$ and $C$ is a circular counter-clockwise contour, centred at 0 and with radius $R > k$ . Using the partial fraction form of $\phi$ , (521c) is found to be

$$
\sum _ { j = 0 } ^ { k } \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { l } \exp _ { \widetilde { p } - l } ( - z j ) ,
$$

but using (521b), the integral can be bounded in terms of $R ^ { - 1 }$ for large $R$ , and is therefore zero. Use the fact that $z ^ { l } \exp _ { \widetilde { p } - l } ( - z j ) = z ^ { l } \exp ( - z j ) + { \cal O } ( z ^ { \widetilde { p } + 1 } )$ and the result follows. $\sqcup$

Because of the maximal order properties of these approximations, they will be known as ‘generalized Pad´e approximations’. Some examples are given in Table 521(I). In each case, $\Phi ( w , z )$ is scaled so that the coefficient of $w ^ { k } z ^ { 0 }$ is $^ { 1 }$ . Some of these functions correspond to A-stable methods, and this is indicated in the table. The entry for $\nu = [ 1 , 0 , 1 ]$ is reducible, in the sense that $\Phi ( w , z )$ factorizes into the approximation for [1, 1] multiplied by $w - 1$ ; the order 3 suggested for this method is, of course, an illusion.

Some generalized Pad´e approximations   

<table><tr><td></td><td>p</td><td>重(w,2)</td><td>Remarks</td></tr><tr><td>[1,0,0]2</td><td></td><td>(1-²z)w²-w+</td><td>A-stable</td></tr><tr><td>[1,0,1]3</td><td></td><td>(1-z)w²-2w+1+½z</td><td>A-stable</td></tr><tr><td>[1,1,0]3</td><td></td><td>(1-z)w²-（g+z)-½</td><td></td></tr><tr><td>[2,0,0]3</td><td></td><td>(1-/z+²z²）w²-w+↓</td><td>A-stable</td></tr><tr><td>[2,0,1]</td><td></td><td>(1-+）w²-++</td><td>A-stable</td></tr><tr><td>[2,1,0]</td><td>4</td><td>(1-1+z²）w²-（1+)-17</td><td>A-stable</td></tr><tr><td>[2,0,2]5</td><td></td><td>(1-+z²）w²-2ω+1++²</td><td>see text</td></tr><tr><td></td><td></td><td>7 2 1 15 15</td><td>比</td></tr><tr><td></td><td></td><td>[3,0,0]4（1-1+2²- 16 w+ 15 15</td><td>A-stable</td></tr><tr><td></td><td>[4,0,0] 5(1-x+</td><td>4 23 2 z4）w² 32 w+ 31 93 31</td><td></td></tr></table>

The approximation based on $\nu = \left\lfloor 2 , 0 , 2 \right\rfloor$ is especially interesting. According to the result formerly known as the Daniel–Moore conjecture (Daniel and Moore, 1970), it cannot correspond to an A-stable method and also have order $p = 5$ , because it does not satisfy the necessary condition $p \leq 2 s$ . However, the solutions to the equation $\Phi ( w , z ) = 0$ for $z = i y$ satisfy

$$
| w | ^ { 2 } = \left| { \frac { 8 \pm i y { \sqrt { 9 + y ^ { 2 } } } } { 8 - y ^ { 2 } - 5 i y } } \right| ^ { 2 } = 1 .
$$

By the maximum modulus principle, the bound $| w | \leq 1$ holds in the left halfplane and the only point in the closed left half-plane where the two $w$ roots have equal values on the unit circle is when $z = 0$ . For Obreshkov methods we have to regard this as representing instability in the sense of Dahlquist. On the other hand, general linear methods with this stability function exist with $V = I$ and therefore convergent methods are definitely possible. A possible method satisfying this requirement is

$$
\left[ \begin{array} { r } { { \frac { 5 } { 1 6 } } \qquad { \frac { 1 0 7 } { 4 8 } } } \\ { { - { \frac { 2 1 } { 1 7 1 2 } } \qquad { \frac { 5 } { 1 6 } } } \qquad 0 \quad 1 } \\ { { \frac { 7 7 5 } { 8 5 6 } } \qquad { - { \frac { 9 9 } { 8 } } } \qquad 1 \quad 0 } \\ { { - { \frac { 4 5 9 } { 9 1 5 9 2 } } \qquad { \frac { 2 9 5 } { 8 5 6 } } \qquad 0 \quad 1 } } \end{array} \right] .
$$

Although $\Phi ( \exp ( z ) , z ) = { \cal O } ( z ^ { 6 } )$ , the order is only 4 because the solution to $\Phi ( w , z ) = 0$ which is ‘principal’ in the sense that it is a good approximation to $\exp ( z )$ , is

$$
w = \frac { 1 + \frac 3 8 z \sqrt { 1 - \frac 1 9 z ^ { 2 } } } { 1 - \frac 5 8 z + \frac 1 8 z ^ { 2 } } = \exp ( z ) - \frac 1 { 2 7 0 } z ^ { 5 } + { \cal O } ( z ^ { 6 } ) .
$$

In Butcher and Chipman (1992), the search for possible $\nu$ corresponding to A-stable methods was focused on the cases $2 \nu _ { 0 } - \widetilde { p } \in \{ 0 , 1 , 2 \}$ . For $k = 1$ (the one-step case), this is necessary and sufficient for A-stability. It seems to be the case that, even for $k > 1$ , those methods for which $2 \nu _ { 0 } - \widetilde { p } > 2$ cannot be A-stable. This proposition has become known as the ‘Butcher–Chipman conjecture’. A partial proof was given in Butcher (2002), restricted to the cases $2 \nu _ { 0 } - \widetilde { p } = 3 , 4 , 7 , 8 , 1 1 , 1 2 , . . .$ , and a complete proof is given in Butcher (2008). An outline of the argument will be given in Subsection 522.

# 522 Outline proof of the Butcher–Chipman conjecture

The essential elements of the proof are just as in the proof of Theorem 355G. That is, the result hinges on the fact that if $2 \nu _ { 0 } - \widetilde { p } > 2$ , then an up arrow from zero must be tangential to the imaginary axis, or protrude into the left half-plane, and terminate at a pole. This will mean that this pole will be in the left half-plane or else the arrow will have to cross the imaginary axis to reach this pole.

The missing detail, which we will now focus on, is the fact that each pole is at the termination of an up arrow from zero. We cannot prove this in a simple way based on non-crossing of up and down arrows, because the relation $\Phi ( w \exp ( z ) , z ) = 0$ now defines a Riemann surface, rather that $w$ as a function of $z$ . The way we will proceed is (i) to modify the order arrow diagram slightly to avoid the need to deal in a special way with special points which arise in the diagram and (ii) to look at changes in the structure of the diagram as the approximation is changed smoothly from one approximation to another.

The modification to arrow diagrams is illustrated in the case of the [4, 2] Pad´e approximation. Consider Figure $5 2 2 ( \mathrm { i } )$ , where two versions of the arrow system are presented. On the left is the standard diagram and on the right is its modified form. The modifications are of two types. First, all arrows are moved an infinitesimal distance to the right to avoid an ambiguity caused by ‘stagnation points’, such as at $z = 0 .$ The ambiguity is that an up arrow arriving at a stagnation point is equally related to arrows leaving this point on the left and on the right. Under the modification, this arrow can be regarded as being continued as an up arrow to the right. For example, in the approximation shown in Figure $5 2 2 ( \mathrm { i } )$ , arrows arrive in directions $0 , 2 \pi / 7 , 4 \pi / 7 , \ldots , 1 2 \pi / 7 .$ In the diagram on the right these are continued unambiguously as outgoing up arrows in the directions $0 \pi / 7 , 3 \pi / 7 , 5 \pi / 7 , \dots , 1 3 \pi / 7$ , respectively. The second modification is to replace poles and zeros as termination points for up and down arrows respectively, by additional sheets in the Riemann surface. The way this done, in the case of poles, is to introduce the approximation defined by

![](images/555f0c6005b246c4acae5cc5aaa114db6092a5b008b706cab7f7449be19dae54.jpg)  
Unmodified (left) and modified (right) order arrows for the approximation [4, 2]

$$
( 1 - t ) \Phi ( w , z ) + t \widetilde { \Phi } ( w , z ) ,
$$

where $\widetilde { \Phi }$ is defined from $\left[ 0 \quad \nu _ { 0 } \quad \nu _ { 1 } \quad \cdot \cdot \cdot \quad \nu _ { k } \right]$ , normalized so that $\widetilde P _ { 1 } ( 0 ) = 1$ . If we take the limit as $t  0$ , the Riemann surface limit does not exist but the projection of the new sheet onto the $\mathcal { L }$ plane does exist. This new plane has the same projection as the order arrow system for

$$
\pm \exp ( z ) + P _ { 1 } ( z ) ,
$$

where the sign is chosen to agree with the coefficient of $w ^ { r + 1 }$ in $\widetilde { \Phi } ( w , z )$ . A similar construction is used for a new bottom sheet defined from the zeros of $P _ { k }$ . This means that the artificial bottom sheet is found as the limit as $t \longrightarrow 0$ of the arrow system for $w \Phi ( w , z ) \pm t$ . There is no reason why this should not be replaced by $w ^ { n } \Phi ( w , z ) \pm t$ where $n$ is any positive integer and we would obtain similar behaviour.

Given an order $p$ approximation $[ \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { k } ]$ , denoted by $\Phi$ , we can construct, for any $t \in [ 0 , 1 ]$ , the approximation $\Phi _ { t } = t \Phi + ( 1 - t ) \Phi _ { 0 }$ , where $\Phi _ { 0 }$ is the $\lfloor \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { r } - 1 \rfloor$ approximation of order $p - 1$ . Because of the uniqueness of generalized Pad´e approximations, $\Phi _ { t }$ will have order only $p - 1$ if $t < 1$ . The parameter $t$ now takes the role of homotopy variable and we will consider the structure of the arrow system as $t$ moves from 0 to 1. We illustrate in Figure 522(ii) what happens in a series of diagrams in the case $p = 4 , \nu _ { 0 } = 2$ , for $t = 0$ , $t = 0 +$ (a small positive value), $t = 1 -$ (a value less than but close to 1) and $t = 1$ . Note that these are stylized diagrams and apply to a generic situation. That is, they could apply to any of the approximations, [2, 2], $[ 2 , 1 , 0 ]$ , $\lfloor 2 , 0 , 1 \rfloor$ , $[ 2 , 0 , 0 ]$ etc. Furthermore, the diagrams are distorted to

![](images/cc9dd24fcdc27d1bf8180c4360f66618de51c41d77b1eaa1bb2d8a9adefbd43d.jpg)  
Homotopy from an order 3 to an order 4 approximation

![](images/5f11880b6c0744f803a6222f454856be888e597bf4b0b7071b21a2d25aff76bd.jpg)  
Illustrating the impossibility of A-stable methods with

$$
2 \nu _ { 0 } - p > 2
$$

avoid overlapping lines. For $t > 0$ , a new arrow is introduced; this is shown as a prominent line. As $t$ approaches 1, it moves into position as an additional up arrow to 0 and an additional up arrow away from 0.

In such a homotopic sequence as this, it is not possible that an up arrow associated with a pole is detached from 0 because either this would mean a loss of order or else the new arrow would have to pass through 0 to compensate for this. However, at the instant when this happens, the order would have been raised to $p$ , which is impossible because of the uniqueness of the $[ \nu _ { 0 } , \nu _ { 1 } , \ldots , \nu _ { k } ]$ approximation.

To complete this outline proof, we recall the identical final step in the proof of Theorem 355G which is illustrated in Figure 522(iii). If $2 \nu _ { 0 } > p + 2$ , then the up arrows which terminate at poles subtend an angle $( \nu _ { 0 } - 1 ) 2 \pi / ( p + 1 ) \geq \pi$ . If this angle is $\pi$ , as in (a) in this figure, then there will be an up arrow leaving $0$ in a direction tangential to the imaginary axis. Thus there will be points on the imaginary axis where $| w | > 1$ . In the case of (b), an up arrow terminates at a pole in the left half-plane, again making A-stability impossible. Finally, in (c), where an up arrow leaves 0 and passes into the left half-plane, but returns to the right half-plane to terminate at a pole, it must have crossed the imaginary axis. Hence, as in (a), there are points on the imaginary axis where $| w | > 1$ and A-stability is not possible.

# 523 Non-linear stability

We will consider an example of an A-stable linear multistep method based on the function

$$
( 1 - z ) w ^ { 2 } + ( - { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 4 } } z ) w + ( - { \textstyle \frac { 1 } { 2 } } - { \textstyle \frac { 3 } { 4 } } z ) .
$$

As a linear multistep method this is

$$
[ \begin{array} { c c c c }  { 1  { \begin{array} { c c c c } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 4 } } } & { { \frac { 3 } { 4 } } } \\ { { 1  { \begin{array} { c c c c } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 4 } } } & { { \frac { 3 } { 4 } } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} }  } } , } \end{array} ] } , \end{array}
$$

where the input to step $n$ consists of the vectors $y _ { n - 1 } , y _ { n - 2 } , h f ( y _ { n - 1 } ) , h f ( y _ { n - 2 } )$ , respectively.

To understand the behaviour of this type of method with a dissipative problem, Dahlquist (1976) analysed the corresponding one-leg method. However, with the general linear formulation, the analysis can be carried out directly. We first carry out a transformation of the input and output variables to the form

$$
\left[ \begin{array} { c c } { { A } } & { { U T ^ { - 1 } } } \\ { { T B } } & { { T V T ^ { - 1 } } } \end{array} \right] ,
$$

where

$$
T = \left[ { \begin{array} { r r r r r } { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 3 } } } & { { - \frac { 1 } { 3 } } } & { { \frac { 7 } { 6 } } } & { { - \frac { 1 } { 2 } } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] .
$$

The resulting method is found to be

$$
[ { \begin{array} { r r r r r } { 1 } & { { | \ 1 } & { { \ } - { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 3 } { 2 } } } & { 1 } & { - { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} } ] } \ .
$$

Because the first two output values in the transformed formulation do not depend in any way on the final two input values, these values, and the final two output values, can be deleted from the formulation. Thus, we have the reduced method

$$
[ { \frac { 1 } { 1 } } | { \begin{array} { r r } { 1 } & { - { \frac { 1 } { 2 } } } \\ { 1 } & { 0 } \\ { { \frac { 3 } { 2 } } } \end{array} } ] .
$$

From the coefficients in the first two rows of $T$ , we identify the inputs in (523a) with specific combinations of the input values in the original formulation:

$$
\begin{array} { r } { y _ { 1 } ^ { [ n - 1 ] } = \frac { 2 } { 3 } y _ { n - 1 } + \frac { 1 } { 3 } y _ { n - 2 } + \frac { 1 } { 3 } h f ( y _ { n - 1 } ) + \frac { 1 } { 2 } h f ( y _ { n - 2 } ) , } \\ { y _ { 2 } ^ { [ n - 1 ] } = \frac { 1 } { 3 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } + \frac { 7 } { 6 } h f ( y _ { n - 1 } ) - \frac { 1 } { 2 } h f ( y _ { n - 2 } ) . } \end{array}
$$

Stable behaviour of this method with a dissipative problem hinges on the verifiable identity

$$
\begin{array} { r l r } {  { \| y _ { 1 } ^ { n } \| ^ { 2 } + \frac { 1 } { 3 } \| y _ { 2 } ^ { [ n ] } \| ^ { 2 } = \| y _ { 1 } ^ { n - 1 ] } \| ^ { 2 } + \frac { 1 } { 3 } \| y _ { 2 } ^ { [ n - 1 ] } \| ^ { 2 } } } \\ & { } & { + 2 \langle h f ( Y ) , Y \rangle - \frac { 1 } { 4 } \| y _ { 2 } ^ { [ n - 1 ] } - h f ( Y ) \| ^ { 2 } . } \end{array}
$$

This means that if $2 \langle h f ( Y ) , Y \rangle ~ \leq ~ 0$ , then $\| y ^ { [ n ] } \| _ { G } ~ \leq ~ \| y ^ { [ n - 1 ] } \| _ { G }$ , where $G = \mathrm { d i a g } ( 1 , { \textstyle { \frac { 1 } { 3 } } } )$ .

Given an arbitrary general linear method, we ask when a similar analysis can be performed. It is natural to restrict ourselves to methods without unnecessary inputs, outputs or stages; such irreducible methods are discussed in Butcher (1987a).

As a first step we consider how to generalize the use of the $G$ norm. Let $G$ denote an $r \times r$ positive semi-definite matrix. For $u , v \in \mathbb { R } ^ { r N }$ made up from subvectors $u _ { 1 } , u _ { 2 } , \ldots , u _ { r } \in \mathbb { R } ^ { N }$ , $v _ { 1 } , v _ { 2 } , \ldots , v _ { r } \in \mathbb { R } ^ { N }$ , respectively, define $\langle \cdot , \cdot \rangle _ { G }$ and the corresponding semi-norm $\| \cdot \| _ { G }$ as

$$
\begin{array} { c } { { \displaystyle { \langle u , v \rangle _ { G } = \sum _ { i , j = 1 } ^ { r } g _ { i j } \langle u _ { i } , v _ { j } \rangle } , } } \\ { { \| u \| _ { G } ^ { 2 } = \langle u , u \rangle _ { G } . } } \end{array}
$$

We will also need to consider vectors $U \oplus u \in \mathbb { R } ^ { ( s + r ) N }$ , made up from subvectors $U _ { 1 } , U _ { 2 } , \dots , U _ { s } , u _ { 1 } , u _ { 2 } , \dots , u _ { r } \in \mathbb { R } ^ { N }$ . Given a positive semi-definite $( s + t ) \times ( s + r )$ matrix $M$ , we will define $\| U \oplus u \| _ { M }$ in a similar way. Given a diagonal $s \times s$ matrix $D$ , with diagonal elements $d _ { i } ~ \geq ~ 0$ , we will also write $\langle U , V \rangle _ { D }$ as $\textstyle \sum _ { i = 1 } ^ { s } d _ { i } \langle U _ { i } , V _ { i } \rangle$ . Using this terminology we have the following result:

Theorem 523A Let $Y$ denote the vector of stage values, $F$ the vector of stage derivatives and $y ^ { [ n - 1 ] }$ and $y ^ { \lfloor n \rfloor }$ the input and output respectively from a single step of a general linear method $( A , U , B , V )$ . Assume that $M$ is $a$ positive semi-definite $( s + r ) \times ( s + r )$ matrix, where

$$
M = \left[ \begin{array} { c c } { { D A + A ^ { \top } D - B ^ { \top } G B } } & { { D U - B ^ { \top } G V } } \\ { { U ^ { \top } D - V ^ { \top } G B } } & { { G - V ^ { \top } G V } } \end{array} \right] ,
$$

with $G$ a positive semi-definite $r \times r$ matrix and $D$ a positive semi-definite diagonal $s \times s$ matrix. Then

$$
\| y ^ { [ n ] } \| _ { G } ^ { 2 } = \| y ^ { [ n - 1 ] } \| _ { G } ^ { 2 } + 2 \langle h F , Y \rangle _ { D } - \| h F \oplus y ^ { [ n - 1 ] } \| _ { M } ^ { 2 } .
$$

Proof. The result is equivalent to the identity

$$
M = \left[ 0 \quad 0 \right] - \left[ B ^ { \intercal } \right] G \left[ B \quad V \right] + \left[ D \right] \left[ A \quad U \right] + \left[ A ^ { \intercal } \right] \left[ D \quad 0 \right] .
$$

We are now in a position to extend the algebraic stability concept to the general linear case.

Theorem 523B If $M$ given by (523b) is positive semi-definite, then

$$
\| y ^ { [ n ] } \| _ { G } ^ { 2 } \leq \| y ^ { [ n - 1 ] } \| _ { G } ^ { 2 } .
$$

524 Reducible linear multistep methods and $G$ -stability

We consider the possibility of analysing the possible non-linear stability of linear multistep methods without using one-leg methods. First note that a linear $k$ -step method, written as a general linear method with $r = 2 k$ inputs, is reducible to a method with only $k$ inputs. For the standard $k$ -step method written in the form (400b), we interpret $h f ( x _ { n - i } , y _ { n - i } )$ , $i = 1 , 2 , \ldots , k$ , as having already been evaluated from the corresponding $y _ { n - i }$ . Define the input vector $y ^ { [ n - 1 ] }$ by

$$
y _ { i } ^ { [ n - 1 ] } = \sum _ { j = i } ^ { k } { \bigl ( } \alpha _ { j } y _ { n - j + i - 1 } + \beta _ { j } h f ( x _ { n - j + i } , y _ { n - j + i - 1 } ) { \bigr ) } , \quad i = 1 , 2 , \ldots , k ,
$$

so that the single stage $Y = y _ { n }$ satisfies

$$
Y = h \beta _ { 0 } f ( x _ { n } , Y ) + y _ { 1 } ^ { [ n - 1 ] }
$$

and the output vector can be found from

$$
y _ { i } ^ { [ n ] } = \alpha _ { i } y _ { 1 } ^ { [ n - 1 ] } + y _ { i + 1 } ^ { [ n ] } + ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } ) h f ( x _ { n } , Y ) ,
$$

where the term y [n]i+1 is omitted when $i ~ = ~ k$ . The reduced method has the defining matrices

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c } { \beta _ { 0 } } \\ { \beta _ { 0 } \alpha _ { 1 } + \beta _ { 1 } } \\ { \beta _ { 0 } \alpha _ { 2 } + \beta _ { 2 } } \\ { \beta _ { 0 } \alpha _ { 3 } + \beta _ { 3 } } \\ { \vdots } \\ { \beta _ { 0 } \alpha _ { k - 1 } + \beta _ { k - 1 } } \\ { \beta _ { 0 } \alpha _ { k } + \beta _ { k } } \end{array} \right] \left[ \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 1 } } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 2 } } & { 0 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 3 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { \alpha _ { k - 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \\ { \alpha _ { k } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} \right] ,
$$

and was shown in Butcher and Hill (2006) to be algebraically stable if it is A-stable.

# 525 $G$ -symplectic methods

In the special case of Runge–Kutta methods, the matrix $M$ , given by (357d), which arose in the study of non-linear stability, had an additional role. This was in Section 37 where $M$ was used in the characterization of symplectic behaviour. This leads to the question: ‘does $M$ , given by (523b), have any significance in terms of symplectic behaviour’?.

For methods for which $M \ = \ 0$ , although we cannot hope for quadratic invariants to be conserved, a ‘ $G$ extension’ of such an invariant may well be conserved. Although we will show this to be correct, it still has to be asked if there is any computational advantage in methods with this property. The author believes that these methods may have beneficial properties, but it is too early to be definite about this.

The definition, which we now present, will be expressed in terms of the submatrices making up $M$ .

Definition 525A A general linear method $( A , U , B , V )$ is $G$ -symplectic if there exists a positive semi-definite symmetric $r \times r$ matrix $G$ and an $s \times s$ diagonal matrix $D$ such that

$$
\begin{array} { r } { G = V ^ { \top } G V , } \\ { D U = B ^ { \top } G V , } \\ { D A + A ^ { \top } D = B ^ { \top } G B . } \end{array}
$$

The following example of a G-symplectic method was presented in Butcher (2006):

$$
\left[ { \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} } \right] = \left[ { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 6 } } } { \frac { 3 + { \sqrt { 3 } } } { 6 } } } \left| { \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } \end{array} } \right| { \mathrm { . ~ } } \right.
$$

It can be verified that (525d) satisfies (525a)–(525c) with $G = \mathrm { d i a g } ( 1 , 1 + \textstyle { \frac { 2 } { 3 } } { \sqrt { 3 } } )$ and $\begin{array} { r } { D = \mathrm { d i a g } ( \frac { 1 } { 2 } , \frac { 1 } { 2 } ) } \end{array}$ .

Although this method is just one of a large family of such methods which the author, in collaboration with Laura Hewitt and Adrian Hill of Bath University, is trying to learn more about, it is chosen for special attention here. An analysis in Theorem 534A shows that it has order 4 and stage order 2. Although it is based on the same stage abscissae as for the order 4 Gauss Runge–Kutta method, it has a convenient structure in that $A$ is diagonally implicit.

For the harmonic oscillator, the Hamiltonian is supposed to be conserved, and this happens almost exactly for solutions computed by this method for any number of steps. Write the problem in the form $y ^ { \prime } = i y$ so that for stepsize $h$ , $y ^ { \left[ n \right] } = M ( i h ) y ^ { \left[ n - 1 \right] }$ where $M$ is the stability matrix. Long term conservation requires that the characteristic polynomial of $M ( i h )$ has both zeros on the unit circle. This characteristic polynomial is:

![](images/67eaa37cf75bf7430eda4519b0e7a089692ba72a5463178ea47a45705b8540a7.jpg)  
Variation in $| y _ { 1 } ^ { \lfloor n \rfloor } |$ for $n = 0 , 1 , \ldots , 1 4 0$ , with $h = 0 . 1$ ; note that $\epsilon = 0 . 0 0 0 2 7 6$

$$
\begin{array} { r } { w ^ { 2 } \Big ( 1 - i h \frac { 3 + \sqrt { 3 } } { 6 } \Big ) ^ { 2 } + w \Big ( \frac { 2 } { 3 } i \sqrt { 3 } \Big ) h - \Big ( 1 + i h \frac { 3 + \sqrt { 3 } } { 6 } \Big ) ^ { 2 } . } \end{array}
$$

Substitute

$$
w = \frac { 1 + i h \frac { 3 + \sqrt { 3 } } { 6 } } { 1 - i h \frac { 3 + \sqrt { 3 } } { 6 } } i W ,
$$

and we see that

$$
W ^ { 2 } + h \frac { 2 \frac { \sqrt { 3 } } { 3 } } { 1 + h ^ { 2 } ( \frac { 3 + \sqrt { 3 } } { 6 } ) ^ { 2 } } W + 1 .
$$

The coefficient of $W$ lies in $( - \sqrt { 3 } + 1 , \sqrt { 3 } - 1 )$ and the zeros of this equation are therefore on the unit circle for all real $h$ . We can interpret this as saying that the two terms in

$$
\Big ( \big ( p _ { 1 } ^ { [ n ] } \big ) ^ { 2 } + \big ( q _ { 1 } ^ { [ n ] } \big ) ^ { 2 } \Big ) + \big ( 1 + { \textstyle \frac { 2 } { 3 } } \sqrt { 3 } \big ) \Big ( \big ( p _ { 2 } ^ { [ n ] } \big ) ^ { 2 } + \big ( q _ { 2 } ^ { [ n ] } \big ) ^ { 2 } \Big )
$$

are not only conserved in total but are also approximately conserved individually, as long as there is no round-off error. The justification for this assertion is based on an analysis of the first component of $y _ { 1 } ^ { \lfloor n \rfloor }$ as $n$ varies. Write the eigenvalues of $M ( i h )$ as $\lambda ( h ) = 1 + O ( h )$ and $\mu ( h ) = - 1 + O ( h )$ and suppose the corresponding eigenvectors, in each case scaled with first component equal to 1, are $u ( h )$ and $v ( h )$ respectively. If the input $y ^ { [ 0 ] }$ is $a u ( h ) + b v ( h )$ then $y _ { 1 } ^ { \lfloor n \rfloor } = a \lambda ( h ) ^ { n } + b \mu ( h ) ^ { n }$ with absolute value

$$
\vert y _ { 1 } ^ { [ n ] } \vert = \Big ( a ^ { 2 } + b ^ { 2 } + 2 a b \mathrm { R e } \big ( ( \overline { { \lambda ( h ) } } \mu ( h ) ) ^ { n } \big ) \Big ) ^ { 1 / 2 } .
$$

If $| b / a |$ is small, as it will be for small $h$ if a suitable starting method is used, $| y _ { 1 } ^ { n } |$ will never depart very far from its initial value. This is illustrated in Figure 525(i) in the case $h = 0 . 1$ .

# Exercises 52

52.1 Find the stability matrix and stability function for the general linear method

$$
\begin{array}{c} \left[ \frac { \frac { 1 } { 2 } } { \frac { 4 } { 3 } } \quad \frac { 1 } { 2 } \left| \begin{array} { r r } { 1 } & { - \frac { 1 } { 2 } } \\ { 1 } & { - \frac { 5 } { 6 } } \\ { \frac { 1 9 } { 1 6 } } & { \frac { 9 } { 1 6 } } \end{array} \right| \right. 1 \quad - \frac { 3 } { 4 }  \\ { \left. \frac { 1 } { 4 } \quad \frac { 3 } { 4 } \quad \right| \left. 0 \quad \quad 0 \right] } \end{array} .
$$

Show that this method A-stable.

52.2 Find a general linear method with stability function equal to the $[ 2 , 0 , 0 ]$ generalized Pad´e approximation to exp.

52.3 Find the $[ 3 , 0 , 1 ]$ generalized Pad´e approximation to exp.

52.4 Show that the $[ 2 , 0 , 1 ]$ generalized Pad´e approximation to exp is A-stable.

# 53 The Order of General Linear Methods

# 530 Possible definitions of order

Traditional methods for the approximation of differential equations are designed with a clear-cut interpretation in mind. For example, linear multistep methods are constructed on the assumption that, at the beginning of each step, approximations are available to the solution and to the derivative at a sequence of step points; the calculation performed by the method is intended to obtain approximations to these same quantities but advanced one step ahead. In the case of Runge–Kutta methods, only the approximate solution value at the beginning of a step is needed, and at the end of the step this is advanced one time step further.

We are not committed to these interpretations for either linear multistep or Runge–Kutta methods. For example, in the case of Adams methods, the formulation can be recast so that the data available at the start and finish of a step is expressed in terms of backward difference approximations to the derivative values or in terms of other linear combinations which approximate Nordsieck vectors. For Runge–Kutta methods the natural interpretation, in which $y _ { n }$ is regarded as an approximation to $y ( x _ { n } )$ , is not the only one possible. As we have seen in Subsection 389, the generalization to effective order is such an alternative interpretation.

For a general linear method, the $r$ approximations, $y _ { i } ^ { \lfloor n - 1 \rfloor }$ , $i = 1 , 2 , \dots , r$ , are imported into step $n$ and the $r$ corresponding approximations, $y _ { i } ^ { \left[ n \right] }$ , are exported at the end of the step. We do not specify anything about these quantities except to require that they are computable from an approximation to $y ( x _ { n } )$ and, conversely, the exact solution can be recovered, at least approximately, from y [i $y _ { i } ^ { [ n - 1 ] }$ , $i = 1 , 2 , \dots , r$ .

This can be achieved by associating with each input quantity, $y _ { i } ^ { \lfloor n - 1 \rfloor }$ , a generalized Runge–Kutta method,

$$
S _ { i } = \frac { c ^ { ( i ) } \enspace | \enspace { \cal A } ^ { ( i ) }  } { b _ { 0 } ^ { ( i ) } \enspace | \enspace b ^ { ( i ) T } \enspace } .
$$

Write $s _ { i }$ as the number of stages in $S _ { i }$ . The aim will be to choose these input approximations in such a way that if y[n−1]i is computed using Si applied to $y ( x _ { n - 1 } )$ , for $i = 1 , 2 , \dots , r$ , then the output quantities computed by the method, $y _ { i } ^ { [ n ] }$ , are close approximations to $S _ { i }$ applied to $y ( x _ { n } )$ , for $i = 1 , 2 , \dots , r$ .

We refer to the sequence of $r$ generalized Runge–Kutta methods $S _ { 1 } , S _ { 2 } , \ldots , S _ { r }$ as a ‘starting method’ for the general linear method under consideration and written as $S$ . It is possible to interpret each of the output quantities computed by the method, on the assumption that $S$ is used as a starting method, as itself a generalized Runge–Kutta method with a total of $s + s _ { 1 } + s _ { 2 } + \cdot \cdot \cdot + s _ { r }$ stages. It is, in principle, a simple matter to calculate the Taylor expansion for the output quantities of these methods and it is also a simple matter to calculate the Taylor expansion of the result found by shifting the exact solution forward one step. We write $S M$ for the vector of results formed by carrying out a step of $M$ based on the results of computing initial approximations using $S$ . Similarly, $_ { E S }$ will denote the vector of approximations formed by advancing the trajectory forward a time step $h$ and then applying each member of the vector of methods that constitutes $S$ to the result of this.

A restriction is necessary on the starting methods that can be used in practice. This is that at least one of $S _ { 1 }$ , $S _ { 2 } , \ldots ,$ $S _ { r }$ , has a non-zero value for the corresponding $b _ { 0 } ^ { ( i ) }$ . If $b _ { 0 } ^ { ( i ) } = 0$ , for all $i = 1$ , $2$ , $\cdot \cdot \cdot$ , $r$ , then it would not be possible to construct preconsistent methods or to find a suitable finishing procedure, $F ^ { \dagger }$ say, such that $S F$ becomes the identity method.

Accordingly, we focus on starting methods that are non-degenerate in the following sense.

Definition 530A A starting method $S$ defined by the generalized Runge– Kutta methods (530a), for $i \ = \ 1$ , 2, . . . , $r$ , is ‘degenerate’ if $b _ { 0 } ^ { ( i ) } = 0$ , for $i = 1$ , 2, . . . , $r$ , and ‘non-degenerate’ otherwise.

Definition 530B Consider a general linear method $M$ and a non-degenerate starting method $S$ . The method $M$ has order $p$ relative to $S$ if the results found from $S M$ and $E S$ agree to within $O ( ^ { p + 1 } )$ .

Definition 530C A general linear method $M$ has order $p$ if there exists a non-degenerate starting method $S$ such that $M$ has order $p$ relative to $S$ .

![](images/b516c4a268f24f380928fcb6e327a5875a866e56f0e2239c19ad64fdd4b4de8f.jpg)  
Representation of local truncation error

In using Definition 530C, it is usually necessary to construct, or at least to identify the main features of, the starting method $S$ which gives the definition a practical meaning. In some situations, where a particular interpretation of the method is decided in advance, Definition 530B is used directly. Even though the Taylor series expansions, needed to analyse order, are straightforward to derive, the details can become very complicated. Hence, in Subsection 532, we will build a framework for simplifying the analysis. In the meantime we consider the relationship between local and accumulated error.

# 531 Local and global truncation errors

Figure 531(i) shows the relationship between the action of a method $M$ with order $p$ , a non-degenerate starting method $S$ , and the action of the exact solution $E$ , related as in Definition 530C. We also include in the diagram the action of a finishing procedure $F$ which exactly undoes the work of $S$ , so that $S F = \mathrm { i d }$ . In this figure, $T$ represents the truncation error, as the correction that would have to be added to $S M$ to obtain $_ { E S }$ . Also shown is $\hat { T }$ , which is the error after carrying out the sequence of operations making up $S M F$ , regarded as an approximation to $E$ . However, in practice, the application of $F ^ { \dagger }$ to the computed result is deferred until a large number of steps have been carried out.

Figure 531(i) illustrates that the purpose of a general linear method is to approximate not the exact solution, but the result of applying $S$ to every point on the solution trajectory. To take this idea further, consider Figure 531(ii), where the result of carrying the approximation over many steps is shown. In step $k$ , the method $M$ is applied to an approximation to $E ^ { k - 1 } S$ to yield an approximation to $E ^ { k } S$ without resorting to the use of the finishing method $F ^ { \dagger }$ . In fact the use of $F$ is postponed until an output approximation is finally needed.

![](images/256d6c189cfa2a6a1c8a240c5eafaddd8ea41e4ba75287270e5ee89a2c1bcd4e.jpg)  
Representation of global truncation error

# 532 Algebraic analysis of order

Associated with each of the components of the vector of starting methods is a member of the algebra $G$ introduced in Subsection 385. Denote $\xi _ { i }$ , $i = 1 , 2 , \ldots , r$ , as the member corresponding to $S _ { i }$ . That is, $\xi _ { i }$ is defined by

$$
\begin{array} { l } { { \displaystyle \xi _ { i } ( \emptyset ) = b _ { 0 } ^ { ( i ) } , } } \\ { { \displaystyle \xi _ { i } ( t ) = \Phi ^ { ( i ) } ( t ) , \quad t \in T , } } \end{array}
$$

where the elementary weight $\Phi ^ { ( i ) } ( t )$ is defined from the tableau (530a). Associate $\eta _ { i } \in G _ { 1 }$ with stage $i = 1 , 2 , \dots , s$ , and define this recursively by

$$
\eta _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } U _ { i j } \xi _ { j } .
$$

Having computed $\eta _ { i }$ and $\eta _ { i } D$ , $i = 1 , 2 , \dots , s$ , we are now in a position to compute the members of $G$ representing the output approximations. These are given by

$$
\sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad i = 1 , 2 , \ldots , r .
$$

If the method is of order $p$ , this will correspond to $E \xi _ { i }$ , within $H _ { p }$ . Hence, we may write the algebraic counterpart to the fact that the method $M$ is of order $p$ , relative to the starting method $S$ , as

$$
E \xi _ { i } = \sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad \mathrm { i n ~ } G / H _ { p } , i = 1 , 2 , \ldots , r .
$$

Because (532b) represents a Taylor expansion, the expression

$$
E \xi _ { i } - \sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D - \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad i = 1 , 2 , \ldots , r ,
$$

represents the amount by which $y _ { i } ^ { \left[ n \right] }$ falls short of the value that would be found if there were no truncation error. Hence, (532d) is closely related to the local truncation error in approximation $i$ .

Before attempting to examine this in more detail, we introduce a vector notation which makes it possible to simplify the way formulae such as (532a) and (532c) are expressed. The vector counterparts are

$$
\begin{array} { r } { \eta = A \eta D + U \xi , } \\ { E \xi = B \eta D + V \xi , } \end{array}
$$

where these formulae are to be interpreted in the space $G / H _ { p }$ . That is, the two sides of (532e) and of (532f) are to be equal when evaluated for all $t \in T ^ { \# }$ such that $r ( t ) \leq p$ .

Theorem 532A Let $M = ( A , U , B , V )$ denote a general linear method and let $\xi$ denote the algebraic representation of a starting method $S$ . Assume that (532e) and (532f) hold in $G / H _ { p }$ . Denote

$$
\epsilon = E \xi - B \eta D - V \xi , \qquad i n \ : G .
$$

Then the Taylor expansion of $S ( y ( x _ { 0 } + h ) ) - M ( S ( y ( x _ { 0 } ) ) )$ is

$$
\sum _ { r ( t ) > p } \frac { \epsilon ( t ) } { \sigma ( t ) } h ^ { r ( t ) } F ( t ) ( y ( x _ { 0 } ) ) .
$$

Proof. We consider a single step from initial data given at $x _ { 0 }$ and consider the Taylor expansion of various expressions about $x _ { 0 }$ . The input approximation, computed by $S$ , has Taylor series represented by $\xi$ . Suppose the Taylor expansions for the stage values are represented by $\eta$ so that the stage derivatives will be represented by $\eta D$ and these will be related by (532e). The Taylor expansion for the output approximations is represented by $B \eta D + V \xi$ , and this will agree with the Taylor expansion of $S ( y ( x _ { 0 } + h ) )$ up to $h ^ { p }$ terms if (532f) holds. The difference from the target value of $S ( y ( x _ { 0 } + h ) )$ is given by (532g). $\boxed { \begin{array} { r l } \end{array} }$

# 533 An example of the algebraic approach to order

We will consider the modification of a Runge–Kutta method given by (502c). Denote the method by $M$ and a possible starting method by $S$ . Of the two quantities passed between steps, the first is clearly intended to approximate the exact solution and we shall suppose that the starting method for this approximation is the identity method, denoted by 1. The second approximation is intended to be close to the scaled derivative at a nearby point and we will assume that this is represented by $\theta : T ^ { \# } \to \mathbb { R }$ , where $\theta ( \varnothing ) = 0$ , $\theta ( \tau ) = 1$ . The values of $\theta ( t )$ for other trees we will keep as parameters to be chosen. Are there possible values of these parameters for which $M$ has order $p = 4$ , relative to $S$ ?

Calculations to verify order $p = 4$ for (502c)   

<table><tr><td>i</td><td>01</td><td>2</td><td>3</td><td></td><td></td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>ti</td><td>D.</td><td></td><td>：</td><td>?</td><td></td><td>Y</td><td>！</td><td>丫</td><td>：</td></tr><tr><td>S1</td><td>10</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S2</td><td>01</td><td>0</td><td></td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td></tr><tr><td>m1</td><td>1 0</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>n1D</td><td>0 1</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>m2</td><td>1</td><td>1 1</td><td>02</td><td>103</td><td>-104</td><td>-105</td><td>-106</td><td>-107</td><td>-108</td></tr><tr><td>n2D</td><td>0</td><td>1 1</td><td></td><td>4</td><td>-102</td><td></td><td>-02</td><td>-103</td><td>-104</td></tr><tr><td>n3</td><td>11</td><td>1+02</td><td></td><td>1+004-20</td><td></td><td>1+05</td><td>06-102</td><td>07-103</td><td>08-104</td></tr><tr><td>nD</td><td>01</td><td>1</td><td>1</td><td></td><td>1+02</td><td>1</td><td>1+02 +120</td><td>2+0</td><td>04-102</td></tr><tr><td>S</td><td>11 01</td><td>1 1</td><td>1 i</td><td></td><td>-102</td><td>1 </td><td>0</td><td>1 -103</td><td>120 -104</td></tr><tr><td>E1</td><td>11</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td>E2</td><td>01</td><td>1+02</td><td>1+202 +03</td><td></td><td>+02 +04</td><td>1+302</td><td>+0 +303+05+03+04+06+204+07+04+08</td><td>+0</td><td>+0</td></tr></table>

We will start with $\xi _ { 1 } = 1$ and $\xi _ { 2 } = \theta$ and compute in turn $\eta _ { 1 }$ , $\eta _ { 1 } D$ , $\eta _ { 2 }$ , $\eta _ { 2 } D$ , $\eta _ { 3 }$ , $\eta _ { 3 } D$ and finally the representatives of the output approximations, which we will write here as $\widehat { \xi _ { 1 } }$ and $\widehat { \xi _ { 2 } }$ . The order requirements are satisfied if and only if values of the free $\theta$ values can be chosen so that $\widehat { \xi _ { 1 } } = E \xi _ { 1 }$ and $\widehat { \xi _ { 2 } } = E \xi _ { 2 }$ . Reading from the matrix of coefficients for the method, we see that

$$
\begin{array} { r l r l } & { \eta _ { 1 } = \xi _ { 1 } , \qquad } & & { \eta _ { 2 } = \xi _ { 1 } - \frac { 1 } { 4 } \xi _ { 2 } + \frac { 3 } { 4 } \eta _ { 1 } D , } \\ & { \eta _ { 3 } = \xi _ { 1 } + \xi _ { 2 } - 2 \eta _ { 1 } D + 2 \eta _ { 2 } D , } \\ & { \widehat { \xi } _ { 1 } = \xi _ { 1 } + \frac { 1 } { 6 } \eta _ { 1 } D + \frac { 2 } { 3 } \eta _ { 2 } D + \frac { 1 } { 6 } \eta _ { 3 } D , \qquad } & & { \widehat { \xi } _ { 2 } = \eta _ { 2 } D . } \end{array}
$$

The details of these calculations are shown in Table 533(I). Comparing the entries in the $\widehat { \xi _ { 1 } }$ and $E \xi _ { 1 }$ rows in this table, we see that we get agreement if and only if $\theta _ { 2 } = - \frac { _ 1 } { 2 }$ . Moving now to the $\widehat { \xi _ { 2 } }$ and $E \xi _ { 2 }$ rows, we find that these agree only with specific choices of $\theta _ { 3 }$ , $\theta _ { 4 }$ , . . . , $\theta _ { 8 }$ . Thus the method has order 4 relative to $S$ for a unique choice of $\xi _ { 2 } = \theta$ , which is found to be

$$
\begin{array} { r } { [ \theta _ { 0 } ~ \theta _ { 1 } ~ \theta _ { 2 } ~ \theta _ { 3 } ~ \theta _ { 4 } ~ \theta _ { 5 } ~ \theta _ { 6 } ~ \theta _ { 7 } ~ \theta _ { 8 } ] = [ 0 ~ 1 ~ - \frac { 1 } { 2 } ~ \frac { 1 } { 4 } ~ \frac { 1 } { 8 } ~ - \frac { 1 } { 8 } ~ - \frac { 1 } { 1 6 } ~ - \frac { 7 } { 4 8 } ~ - \frac { 7 } { 9 6 } ] . } \end{array}
$$

It might seem from this analysis, that a rather complicated starting method is necessary to obtain fourth order behaviour for this method. However, the method can be started successfully in a rather simple manner. For $S _ { 1 }$ , no computation is required at all and we can consider defining $S _ { 2 }$ using the generalized Runge–Kutta method

$$
{ \frac { - { \frac { 1 } { 2 } } \ - { \frac { 1 } { 2 } } \ } { 0 \ { \left| \begin{array} { l l } { \ 0 } & { 1 } \end{array} \right. } } } .
$$

This starter, combined with a first step of the general linear method $M$ , causes this first step of the method to revert to the Runge–Kutta method (502b), which was used to motivate the construction of the new method.

# 534 The order of a $G$ -symplectic method

A second example, for the method (525d), introduced as an example of a G-symplectic method, is amenable to a similar analysis.

Theorem 534A The following method has order 4 and stage order 2:

$$
\left[ { \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} } \right] = \left[ { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 6 } } } { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 3 } } } { 6 } } } &  \left| { \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } \end{array} } \right|  \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} } \right] .
$$

Before verifying this result we need to specify the nature of the starting method $S$ and the values of the stage abscissae, $c _ { 1 }$ and $c _ { 2 }$ . From an initial point $( x _ { 0 } , y _ { 0 } )$ , the starting value is given by

$$
\begin{array} { l } { { y _ { 1 } ^ { [ 0 ] } = y _ { 0 } , } } \\ { { { } } } \\ { { y _ { 2 } ^ { [ 0 ] } = \frac { \sqrt { 3 } } { 1 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) - \frac { \sqrt { 3 } } { 1 0 8 } h ^ { 4 } y ^ { ( 4 ) } ( x _ { 0 } ) + \frac { 9 + 5 \sqrt { 3 } } { 2 1 6 } h ^ { 4 } \frac { \partial f } { \partial y } y ^ { ( 3 ) } ( x _ { 0 } ) , } } \end{array}
$$

and the abscissa vector is $\begin{array} { r } { c = \left[ \frac { 1 } { 2 } + \frac { 1 } { 6 } \sqrt { 3 } \quad \frac { 1 } { 2 } - \frac { 1 } { 6 } \sqrt { 3 } \right] ^ { 1 } . } \end{array}$

Proof. Write $\xi _ { 1 }$ , $\xi _ { 2 }$ as the representations of $y _ { 1 } ^ { \left[ 0 \right] }$ , $y _ { 2 } ^ { [ 0 ] }$ and $\eta _ { 1 }$ , $\eta _ { 2 }$ to represent the stages. The stages have to be found recursively and only the converged values are given in Table 534(I), which shows the sequence of quantities occurring in the calculation. The values given for $\widehat { \xi _ { i } }$ are identical to those for $E \xi _ { i }$ , $i = 1 , 2$ , verifying that the order is 4. Furthermore $\eta _ { i } ( t ) = E ^ { ( c _ { i } ) } ( t )$ , $i = 1 , 2$ , for $r ( t ) \leq 2$ , showing stage order 2. 

Calculations to verify order $p = 4$ for (534a)   

<table><tr><td>i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8 ：</td></tr><tr><td>ti S1</td><td>D 1</td><td>· 0</td><td>： 0</td><td>? 0</td><td>、 0</td><td>Y 0</td><td>· 0</td><td>丫 0</td><td>0</td></tr><tr><td>S</td><td>0</td><td></td><td>品</td><td>0</td><td>0</td><td></td><td></td><td>3+3</td><td>3+3</td></tr><tr><td></td><td></td><td>0 3+3</td><td>12 2+√3</td><td>9+5√3</td><td>9+5√3</td><td>18 11+6√3</td><td>36 11+6√3</td><td>36 2+√3</td><td>72 2+3</td></tr><tr><td>m1</td><td>1</td><td>6</td><td>12</td><td>36 2+√3</td><td>72</td><td>36 11+6√3</td><td>72</td><td>36</td><td>72</td></tr><tr><td>n1D</td><td>0</td><td>1</td><td>3+√3 6</td><td>6</td><td>2+√3 12</td><td>36</td><td>11+6√3 72</td><td>9+5√3 36</td><td>9+5√3 72</td></tr><tr><td>m2</td><td>1</td><td>3-3 6</td><td>2-3 12</td><td>3+5√3 36</td><td>3+5√3 72</td><td>7+6√3 36</td><td>7+6V3 72</td><td>4+3√3 36</td><td>4+3√3 72</td></tr><tr><td>n2D</td><td>0</td><td>1</td><td>3-3 6</td><td>2-3 6</td><td>2-√3 12</td><td>9-5√3 36</td><td>9-53 72</td><td>3+5√3 36</td><td>3+5√3 72</td></tr><tr><td>S</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>12</td><td>24</td></tr><tr><td>S</td><td>0</td><td>0</td><td></td><td></td><td>12</td><td>36</td><td>72</td><td>3+4v3 36</td><td>3+4√3 72</td></tr></table>

# 535 The underlying one-step method

In much the same way as a formal one-step method could be constructed as an underlying representation of a linear multistep method, as in Subsection 422, a one-step method can be constructed with the same underlying relationship to a general linear method. Consider a general linear method $( A , U , B , V )$ and suppose that the preconsistency vector is $u$ . We can ask if it is possible to find $\xi \in X ^ { r }$ and $\eta \in X _ { 1 } ^ { s }$ , such that (532e) and (532f) hold exactly but with $E$ replaced by $\theta \in X _ { 1 }$ ; that is, such that

$$
\begin{array} { r } { \eta ( t ) = A ( \eta D ) ( t ) + U \xi ( t ) , } \\ { ( \theta \xi ) ( t ) = B ( \eta D ) ( t ) + V \xi ( t ) , } \end{array}
$$

for all $t \in T ^ { \# }$ . In this case we can interpret $\theta$ as representing an underlying one-step method. The notional method represented by $\theta$ is not unique, because another solution can be found equal to ${ \widehat { \theta } } = \phi ^ { - 1 } \theta \phi$ , where $\phi \in X _ { 1 }$ is arbitrary. We see this by multiplying both sides of (535a) and (535b) by $\phi ^ { - 1 }$ to arrive at the relations

$$
\begin{array} { r } { \widehat { \eta } ( t ) = A ( \widehat { \eta } D ) ( t ) + U \widehat { \xi } ( t ) , } \\ { ( \widehat { \theta } \widehat { \xi } ) ( t ) = B ( \widehat { \eta } D ) ( t ) + V \widehat { \xi } ( t ) , } \end{array}
$$

with ${ \widehat { \xi } } = \phi ^ { - 1 } \xi$ . We want to explore the existence and uniqueness of the underlying one-step method subject to an additional assumption that some particular component of $\xi$ has a specific value. As a step towards this aim, we remark that (535a) and (535b) transform in a natural way if the method itself is transformed in the sense of Subsection 501. That is, if the method $( A , U , B , V )$ is transformed to $( A , U T ^ { - 1 } , T B , T V T ^ { - 1 } )$ , and (535a) and 535b) hold, then, in the transformed method, $\xi$ transforms to $T \xi$ and $\theta$ transforms to $T \theta T ^ { - 1 }$ . Thus

$$
\begin{array} { c } { { \eta ( t ) = A ( \eta D ) ( t ) + ( U T ^ { - 1 } ) ( T \xi ) ( t ) , } } \\ { { \ } } \\ { { ( ( T \theta T ^ { - 1 } ) ( T \xi ) ) ( t ) = T B ( \eta D ) ( t ) + V ( T \xi ) ( t ) . } } \end{array}
$$

This observation means that we can focus on methods for which $u = e _ { 1 }$ , the first member of the natural basis for $\mathbb { R } ^ { r }$ , in framing our promised uniqueness result.

Theorem 535A Let $( A , U , B , V )$ denote a consistent general linear method such that $u = e _ { 1 }$ and such that

$$
U = [ \mathbf { 1 } \quad \widetilde { U } ] , \qquad V = \left[ \begin{array} { l l } { 1 } & { \widetilde { v } ^ { \intercal } } \\ { 0 } & { \widetilde { V } } \end{array} \right] ,
$$

where $1 \not \in \sigma ( \overset { \sim } { V } )$ . Then there exists a unique solution to (535a) and (535b) for which $\xi _ { 1 } = 1$ .

Proof. By carrying out a further transformation if necessary, we may assume without loss of generality that $\widetilde { V }$ is lower triangular. The conditions satisfied by $\xi _ { i } ( t )$ $i = 2 , 3 , \ldots , r$ ), $\eta _ { i } ( t )$ ( $i = 1 , 2 , \dots , s$ ) and $\theta ( t )$ can now be written in the form

$$
( 1 - \widetilde { V } _ { i , i } ) \xi _ { i } ( t ) = \sum _ { j = 1 } ^ { s } b _ { i j } ( \eta D ) ( t ) + \sum _ { j = 2 } ^ { i - 1 } \widetilde { V } _ { i - 1 , j - 1 } \xi _ { j } ( t ) ,
$$

$$
\eta _ { i } ( t ) = \sum _ { j = 1 } ^ { s } a _ { i j } ( \eta D ) ( t ) + 1 ( t ) + \sum _ { j = 2 } ^ { r } \widetilde { U } _ { i , j - 1 } \xi _ { j } ( t ) ,
$$

$$
\theta ( t ) = \sum _ { j = 1 } ^ { s } b _ { 1 j } ( \eta D ) ( t ) + 1 ( t ) + \sum _ { j = 2 } ^ { r } \widetilde v _ { j - 1 } \xi _ { j } ( t ) .
$$

In each of these equations, the right-hand sides involve only trees with order lower than $r ( t )$ or terms with order $r ( t )$ which have already been evaluated. Hence, the result follows by induction on $r ( t )$ . 

The extension of the concept of underlying one-step method to general linear methods was introduced in Stoffer (1993).

Although the underlying one-step method is an abstract structure, it has practical consequences. For a method in which $\rho ( \overset { \sim } { V } ) < 1$ , the performance of a large number of steps, using constant stepsize, forces the local errors to conform to Theorem 535A. When the stepsize needs to be altered, in accordance with the behaviour of the computed solution, it is desirable to commence the step following the change, with input approximations consistent with what the method would have expected if the new stepsize had been used for many preceding steps. Although this cannot be done precisely, it is possible for some of the most dominant terms in the error expansion to be adjusted in accordance with this requirement. With this adjustment in place, it becomes possible to make use of information from the input vectors, as well as information computed within the step, in the estimation of local truncation errors. It also becomes possible to obtain reliable information that can be used to assess the relative advantages of continuing the integration with an existing method or of moving onto a higher order method. These ideas have already been used to good effect in Butcher and Jackiewicz (2003) and further developments are the subject of ongoing investigations.

# Exercises 53

53.1 A numerical method of the form

$$
\begin{array} { r l } & { \cdot _ { 1 } ^ { [ n ] } = y _ { n - 1 } + h \widehat { a } _ { 1 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { a } _ { 1 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h a _ { 1 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h a _ { 1 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \\ & { \cdot _ { 2 } ^ { [ n ] } = y _ { n - 1 } + h \widehat { a } _ { 2 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { a } _ { 2 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h a _ { 2 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h a _ { 2 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \\ & { \qquad \quad + h a _ { 2 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h a _ { 2 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) } \\ & { \qquad \quad + h \widehat { b } _ { 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { b } _ { 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h b _ { 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h b _ { 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \end{array}
$$

is sometimes known as a ‘two-step Runge–Kutta method’. Find conditions for this method to have order 4.

53.2 Find an explicit fourth order method ( $a _ { 1 1 } = a _ { 1 2 } = a _ { 2 2 } = 0$ ) of the form given by Exercise 53.1.

53.3 Find an A-stable method of the form given by Exercise 53.1.

# 54 Methods with Runge–Kutta stability

# 540 Design criteria for general linear methods

We consider some of the structural elements in practical general linear methods, which are not available together in any single method of either linear multistep or Runge–Kutta type. High order is an important property, but high stage order is also desirable. For single-value methods this is only achievable when a high degree of implicitness is present, but this increases implementation costs. To avoid these excessive costs, a diagonally implicit structure is needed but this is incompatible with high stage order in the case of one-value methods. Hence, we will search for good methods within the large family of multistage, multivalue methods.

The additional complexity resulting from the use of diagonally implicit general linear methods makes good stability difficult to analyse or even achieve. Hence, some special assumptions need to be made. In Subsection 541 we present one attempt at obtaining a manageable structure using DIMSIM methods. We then investigate further methods which have the Runge–Kutta stability property so that the wealth of knowledge available for the stability of Runge–Kutta methods becomes available. Most importantly we consider methods with the Inherent Runge–Kutta stability property, introduced in Subsection 551.

# 541 The types of DIMSIM methods

‘Diagonally implicit multistage integration methods’ (DIMSIMs) were introduced in Butcher (1995a). A DIMSIM is loosely defined as a method in which the four integers $p$ (the order), $q$ (the stage order), $r$ (the number of data vectors passed between steps) and $s$ (the number of stages) are all approximately equal. To be a DIMSIM, a method must also have a diagonally implicit structure. This means that the $s \times s$ matrix $A$ has the form

$$
A = \left[ \begin{array} { c c c c c } { { \lambda } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { \lambda } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { a _ { s 1 } } } & { { a _ { s 2 } } } & { { a _ { s 3 } } } & { { \cdots } } & { { \lambda } } \end{array} \right] ,
$$

where $\lambda \geq 0$ . The rationale for this restriction on this coefficient matrix is that the stages can be computed sequentially, or in parallel if the lower triangular part of $A$ is zero. This will lead to a considerable saving over a method in which $A$ has a general implicit structure. For Runge–Kutta methods, where $r = 1$ , this sort of method is referred to as explicit if $\lambda = 0$ or as diagonally implicit (DIRK, or as singly diagonally implicit or SDIRK) if $\lambda > 0$ ; see Subsection 361.

Types of DIMSIM and related methods   

<table><tr><td>Type</td><td colspan="4"></td><td>Application</td><td></td><td>1Architecture</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td></td><td>a21</td><td>0</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>a31</td><td>a32</td><td>0</td><td>：</td><td>0</td><td>Non-stiff</td><td>Sequential</td></tr><tr><td></td><td>：</td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>as1</td><td>as2</td><td>as3</td><td>：</td><td>0 1</td><td></td><td></td></tr><tr><td></td><td>入</td><td>0</td><td>0</td><td>：：</td><td>0 1</td><td></td><td></td></tr><tr><td></td><td>a21</td><td>入</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td>2</td><td>a31</td><td>a32</td><td>入</td><td>：</td><td>0</td><td>Stiff</td><td>Sequential</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>：</td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>as1</td><td>as2</td><td>as3</td><td>：</td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：…</td><td>0</td><td></td><td></td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td>Non-stiff</td><td>Parallel</td></tr><tr><td></td><td>：</td><td>：</td><td></td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>：</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：.</td><td>0</td><td></td><td></td></tr><tr><td></td><td>入</td><td>0</td><td>0</td><td>：：</td><td>0</td><td></td><td></td></tr><tr><td></td><td>0</td><td>入</td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td>4</td><td>0</td><td>0</td><td>入</td><td></td><td>0</td><td>Stiff</td><td>Parallel</td></tr><tr><td></td><td></td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>：</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>入</td><td></td><td></td></tr></table>

While these Runge–Kutta methods suffer from the disadvantages associated with low stage order, there is no such difficulty associated with general linear methods.

For non-stiff problems, it is advantageous to choose $\lambda = 0$ , whereas for stiff problems, it is necessary that $\lambda > 0$ , if A-stability is to be achieved. Furthermore, as we have already remarked, parallel evaluation of the stages is only possible if $A$ is a diagonal matrix; specifically, this would be the zero matrix in the non-stiff case. From these considerations, we introduce the ‘types’ of a DIMSIM method, and we retain this terminology for methods with a similar structure.

The four types, together with their main characteristics, are shown in Table 541(I). The aim in DIMSIM methods has been to find methods in which $p$ , $q$ , $r$ and $s$ are equal, or approximately equal, and at the same time to choose $V$ as a simple matrix, for example a matrix with rank 1.

If $p = q$ , it is a simple matter to write down conditions for this order and stage order. We have the following result:

Theorem 541A A method

$$
\textstyle \left[ { \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} } \right] ,
$$

has order and stage order $p$ if and only if there exists a function

$$
\phi : \mathbb { C } \to \mathbb { C } ^ { r } ,
$$

analytic in a neighbourhood of $0$ , such that

$$
\begin{array} { r } { \exp ( c z ) = z A \exp ( c z ) + U \phi ( z ) + O ( z ^ { p + 1 } ) , } \\ { \exp ( z ) \phi ( z ) = z B \exp ( c z ) + V \phi ( z ) + O ( z ^ { p + 1 } ) , } \end{array}
$$

where $\exp ( c z )$ denotes the vector in $\mathbb { C } ^ { s }$ for which component $i$ is equal to $\exp ( c _ { i } z )$ .

Proof. Assume that (541a) and (541b) are satisfied and that the components of $\phi ( z )$ have Taylor series

$$
\phi _ { i } ( z ) = \sum _ { j = 0 } ^ { p } \alpha _ { i j } z ^ { j } + O ( z ^ { p + 1 } ) .
$$

Furthermore, suppose starting method $i$ is chosen to give the output

$$
\sum _ { j = 0 } ^ { p } \alpha _ { i j } h ^ { j } y ^ { ( j ) } ( x _ { 0 } ) + O ( h ^ { p + 1 } ) ,
$$

where $y$ denotes the exact solution agreeing with a given initial value at $x _ { 0 }$ Using this starting method, consider the value of

$$
y ( x _ { 0 } + h c _ { k } ) - h \sum _ { i = 1 } ^ { s } a _ { k i } y ^ { \prime } ( x _ { 0 } + h c _ { i } ) - \sum _ { i = 1 } ^ { r } U _ { k i } \sum _ { j = 0 } ^ { p } \alpha _ { i j } h ^ { j } y ^ { ( j ) } ( x _ { 0 } ) .
$$

If this is $O ( h ^ { p + 1 } )$ then it will follow that $Y _ { k } - y ( x _ { 0 } + h c _ { k } ) = O ( h ^ { p + 1 } )$ . Expand (541c) about $x _ { 0 }$ , and it is seen that the coefficient of $h ^ { j } y ^ { ( j ) } ( x _ { 0 } )$ is

$$
{ \frac { 1 } { j ! } } c _ { k } ^ { j } - \sum _ { i = 1 } ^ { s } a _ { k i } { \frac { 1 } { ( j - 1 ) ! } } c _ { i } ^ { j - 1 } - \sum _ { i = 1 } ^ { r } U _ { k i } \alpha _ { i j } .
$$

However, this is exactly the same as the coefficient of $z ^ { j }$ in the Taylor expansion of the difference of the two sides of (541a). Given that the order

of the stages is $p$ , and therefore that $h f ( Y _ { i } ) = h y ^ { \prime } ( x _ { 0 } + h c _ { i } ) + O ( h ^ { p + 1 } )$ , we can carry out a similar analysis of the condition for the $k$ th output vector to equal

$$
\sum _ { j = 0 } ^ { p } \alpha _ { k j } h ^ { j } y ^ { [ j ] } ( x _ { 0 } + h ) + O ( h ^ { p + 1 } ) .
$$

Carry out a Taylor expansion about $x _ { 0 }$ and we find that (541d) can be written as

$$
\sum _ { j = 0 } ^ { p } \sum _ { i = j } ^ { p } \alpha _ { k j } \frac { 1 } { ( i - j ) ! } h ^ { i } y ^ { ( i ) } ( x _ { 0 } ) + O ( h ^ { p + 1 } ) .
$$

The coefficient of $h ^ { i }$ in (541e) is identical to the coefficient of $z ^ { i }$ in $\exp ( z ) \phi _ { k } ( z )$ . Hence, combining this with the terms

$$
\sum _ { i = 1 } ^ { s } b _ { k i } \frac { 1 } { ( j - 1 ) ! } c _ { i } ^ { j - 1 } + \sum _ { i = 1 } ^ { r } V _ { k i } \alpha _ { i j } ,
$$

we find (541b).

To prove necessity, use the definition of order given by (532e) and (532f) and evaluate the two sides of each of these equations for the sequence of trees $t _ { 0 } = \emptyset$ , $t _ { 1 } = \tau$ , $t _ { 2 } = [ t _ { 1 } ]$ , $\cdot \cdot \cdot$ , $t _ { p } = [ t _ { p - 1 } ]$ . Use the values of $\alpha _ { i j }$ given by

$$
\alpha _ { i j } = \xi _ { i } ( t _ { j } ) ,
$$

so that

$$
( E \xi _ { i } ) ( t _ { j } ) = \sum _ { k = 0 } ^ { j } \frac { 1 } { k ! } \xi _ { i } ( t _ { j - k } ) ,
$$

which is the coefficient of $z ^ { j }$ in $\textstyle \exp ( z ) \sum _ { k = 0 } ^ { p } \alpha _ { i k } z ^ { k }$ . We also note that

$$
\eta _ { i } ( t _ { j } ) = \frac { 1 } { j ! } c _ { i } ^ { j } , \qquad ( \eta _ { i } D ) ( t _ { j } ) = \frac { 1 } { ( j - 1 ) ! } c _ { i } ^ { j - 1 } ,
$$

which are, respectively, the $z ^ { j }$ coefficients in $\exp ( c _ { i } z )$ and in $z \exp ( c _ { i } z )$ . Write $\phi ( z )$ as the vector-valued function with $i$ th component equal to $\scriptstyle \sum _ { k = 0 } ^ { p } \alpha _ { i k } z ^ { k }$ , and we verify that coefficients of all powers of $z$ up to $z ^ { p }$ agree in the two sides of (541a) and (541b). 

# 542 Runge–Kutta stability

For methods of types 1 and 2, a reasonable design criterion is that its stability region should be similar to that of a Runge–Kutta method. The reasons for this are that Runge–Kutta methods not only have convenient stability properties from the point of view of analysis but also that they have stability properties that are usually superior to those of alternative methods. For example, A-stability is inconsistent with high order for linear multistep methods but is available for Runge–Kutta methods of any order.

The stability matrix for a general linear method has the form

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U
$$

and the characteristic polynomial is

$$
\Phi ( w , z ) = \operatorname* { d e t } ( w I - M ( z ) ) .
$$

In general this is a complicated function, in which the coefficients of powers of $w$ are rational functions of $z$ . To obtain stability properties as close to those of a Runge–Kutta method as possible we will seek methods for which $\Phi ( w , z )$ factorizes as in the following definition.

Definition 542A A general linear method $( A , U , B , V )$ has ‘Runge–Kutta stability’ if the characteristic polynomial given by (542a) has the form

$$
\begin{array} { r } { \Phi ( w , z ) = w ^ { r - 1 } ( w - R ( z ) ) . } \end{array}
$$

For a method with Runge–Kutta stability, the rational function $R ( z )$ is known as the ‘stability function’ of the method.

We will usually abbreviate ‘Runge–Kutta stability’ by ‘RK stability’. We present two examples of methods satisfying this condition with $p = q = r =$ $s = 2$ and with $c = [ 0 \quad 1 ] ^ { \intercal } .$ . The first is of type 1 and is assumed to have the form

$$
[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { a _ { 2 1 } } { b _ { 1 1 } } \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} ] \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \\ { 1 - V _ { 1 2 } } & { V _ { 1 2 } } \\ { b _ { 1 1 } } & { b _ { 1 2 } } \end{array} ] .
$$

The assumption that $U = I$ is not a serious restriction because, if $U$ is nonsingular, an equivalent method can be constructed with $U = I$ and $B$ and $V$ replaced by $U B$ and $U V U ^ { - 1 }$ , respectively. The form chosen for $V$ makes it of rank $^ { 1 }$ and preconsistent for the vector $c = [ 1 \quad 1 ] ^ { \prime }$ .

By the stage order conditions, it is found that

$$
\phi ( z ) = ( I - z A ) \exp ( c z ) = \left[ \begin{array} { c } { { 1 } } \\ { { 1 + ( 1 - a _ { 2 1 } ) z + \frac { 1 } { 2 } z ^ { 2 } } } \end{array} \right] .
$$

To find $B$ , we have

$$
B z \exp ( c z ) = ( \exp ( z ) I - V ) \phi ( z ) + O ( z ^ { 3 } ) .
$$

Write the coefficients of $z$ and $z ^ { 2 }$ in separate columns and we deduce that

$$
\begin{array} { r } { B \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { 1 - V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { \frac { 1 } { 2 } ( 1 - V _ { 1 2 } ) } \\ { 2 - V _ { 1 2 } - a _ { 2 1 } + a _ { 2 1 } V _ { 1 2 } } & { 2 - a _ { 2 1 } - \frac { 1 } { 2 } V _ { 1 2 } } \end{array} \right] , } \end{array}
$$

so that

$$
B = \left[ \begin{array} { c c } { \frac { 1 } { 2 } - \frac { 1 } { 2 } V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { \frac { 1 } { 2 } ( 1 - V _ { 1 2 } ) } \\ { - \frac { 1 } { 2 } V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { 2 - a _ { 2 1 } - \frac { 1 } { 2 } V _ { 1 2 } } \end{array} \right] .
$$

To achieve RK stability, impose the requirement that the stability function $V + z B ( I - z A ) ^ { - 1 }$ has zero determinant and it is found that $a _ { 2 1 } = 2$ and $\begin{array} { r } { V _ { 1 2 } = \frac { 1 } { 2 } } \end{array}$ .

This gives the method

$$
[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { 2 } { \frac { 5 } { 4 } } \quad \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 1 } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } \\ { \frac { 3 } { 4 } } & { - \frac { 1 } { 4 } } \end{array} ] \frac { 1 } { 2 } \quad \frac { 1 } { 2 } ] .
$$

To derive a type 2 method with RK stability, carry out a similar calculation but with

$$
A = \left[ \begin{array} { c c } { { \lambda } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } \end{array} \right] .
$$

In this case, the method is

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \frac { \frac { \lambda } { 1 + 2 \lambda } } { \frac { 5 - 2 \lambda + 1 2 \lambda ^ { 2 } + 8 \lambda ^ { 3 } } { 4 + 8 \lambda } } \frac { \lambda } { \frac { 1 } { 4 } - \lambda ^ { 2 } } \frac { 0 } { \frac { 1 } { 2 } + \lambda } \frac { 1 } { \frac { 1 } { 2 } - \lambda } \right] ,
$$

or, with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ , for L-stability,

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c c c c c } { 1 - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 1 } & { 0 } \\ { \frac { 6 + 2 \sqrt { 2 } } { 7 } } & { 1 - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 1 } \\ { \frac { 7 3 - 3 4 \sqrt { 2 } } { 2 8 } } & { \frac { 4 \sqrt { 2 } - 5 } { 4 } } & { \frac { 3 - \sqrt { 2 } } { 2 } } & { \frac { \sqrt { 2 } - 1 } { 2 } } \\ { \frac { 8 7 - 4 8 \sqrt { 2 } } { 2 8 } } & { \frac { 3 4 \sqrt { 2 } - 4 5 } { 2 8 } } & { \frac { 3 - \sqrt { 2 } } { 2 } } & { \frac { \sqrt { 2 } - 1 } { 2 } } \end{array} \right] .
$$

Type 3 and type 4 methods do not exist with RK stability, and will not be explored in detail in this section. We do, however, give a single example of each. For the type 3 method we have

$$
[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { 0 } { - \frac { 3 } { 8 } } \begin{array} { c c c c } { 0 } & { 0 } & { | } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { - \frac { 3 } { 8 } } & { - \frac { 3 } { 8 } } & { - \frac { 3 } { 4 } } & { \frac { 7 } { 4 } } \\ { - \frac { 7 } { 8 } } & { \frac { 9 } { 8 } } & { - \frac { 3 } { 4 } } & { \frac { 7 } { 4 } } \end{array} ] .
$$

This method is designed for parallel computation in the sense that the two stages do not depend on each other, because $A = 0$ , and hence they can be evaluated in parallel. Is there any advantage in the use of methods like this? Of course, the answer will depend on the specific coefficients in the method but, in the case of (542d), we might wish to compare it with the type 1 method given by (542b) whose error constant has magnitude $\frac { 1 } { 6 }$ . In contrast, (542d) has error constant $\textstyle { \frac { 1 9 } { 2 4 } }$ which is equivalent to $\textstyle { \frac { 1 9 } { 9 6 } }$ 6 when adjusted for the sequential cost of one $f$ evaluation per step. Thus, in this case, the type 3 method is less efficient even under the assumption of perfect speed-up.

The type 4 method

$$
\begin{array}{c} { \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l l } { { \frac { 3 - { \sqrt { 3 } } } { 2 } } } & { 0 } & { 1 } & { 0 } \\ { { \frac { 0 } { 2 } } } & { { \frac { 3 - { \sqrt { 3 } } } { 2 } } } & { 0 } & { 1 } \\ { { \frac { 1 8 - 1 1 { \sqrt { 3 } } } { 4 } } } & { { \frac { 7 { \sqrt { 3 } } - 1 2 } { 4 } } } \\ { { \frac { 2 2 - 1 3 { \sqrt { 3 } } } { 4 } } } & { { \frac { 9 { \sqrt { 3 } } - 1 2 } { 4 } } } \end{array} \right] } { \frac { 3 - 2 { \sqrt { 3 } } } { 2 } }  & { { \frac { 2 { \sqrt { 3 } } - 1 } { 2 } } } \end{array} 
$$

is found to be A-stable with the additional property that its stability matrix has zero spectral radius at infinity. Just as for the type 3 method we have introduced, while the advantages of this type of method are not clear, results found by Singh (1999) are encouraging.

For type 1 and 2 methods, increasing order presents great challenges in the solution of the order conditions combined with RK stability requirements. For an account of the techniques used to find particular methods of orders up to 8, see Butcher and Jackiewicz (1996, 1998).

# 543 Almost Runge–Kutta methods

The characteristic feature of explicit Runge–Kutta methods, that only minimal information computed in a step is passed on as input to the next step, is a great advantage of this type of method but it is also a perceived disadvantage. The advantage lies in excellent stability properties, while the disadvantage lies in the low stage order to which the second and later stages are restricted. Almost Runge–Kutta methods (ARK) are an attempt to retain the advantage but overcome some of the disadvantages.

Recall the method (505a). Evaluate its stability matrix and we find

$$
{ \begin{array} { r l } & { M ( z ) = V + z B ( I - z A ) ^ { - 1 } U } \\ & { = { \left[ \begin{array} { l l } { 1 + { \frac { 5 } { 6 } } z + { \frac { 1 } { 3 } } z ^ { 2 } + { \frac { 1 } { 4 8 } } z ^ { 3 } } & { { \frac { 1 } { 6 } } + { \frac { 1 } { 6 } } z + { \frac { 7 } { 4 8 } } z ^ { 2 } + { \frac { 1 } { 4 8 } } z ^ { 3 } } & { { \frac { 1 } { 4 8 } } z ^ { 2 } + { \frac { 1 } { 9 6 } } z ^ { 3 } } \\ { z + { \frac { 5 } { 6 } } z ^ { 2 } + { \frac { 1 } { 3 } } z ^ { 3 } + { \frac { 1 } { 4 8 } } z ^ { 4 } } & { { \frac { 1 } { 6 } } z + { \frac { 1 } { 6 } } z ^ { 2 } + { \frac { 7 } { 4 8 } } z ^ { 3 } + { \frac { 1 } { 4 8 } } z ^ { 4 } } & { { \frac { 1 } { 4 8 } } z ^ { 3 } + { \frac { 1 } { 9 6 } } z ^ { 4 } } \\ { z + { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 7 } { 1 2 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } } & { - 1 + { \frac { 1 } { 2 } } z - { \frac { 1 } { 1 2 } } z ^ { 2 } + { \frac { 5 } { 2 4 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } } & { { \frac { 1 } { 4 8 } } z ^ { 4 } } \end{array} \right] } . } \end{array} }
$$

The eigenvalues of this matrix are

$$
\sigma ( M ( z ) ) = \left\{ 1 + z + { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 1 } { 6 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } , 0 , 0 \right\} ,
$$

Calculation of stages and stage derivatives for the method (505a)   

<table><tr><td rowspan="2">α</td><td colspan="9"></td></tr><tr><td>α(0）</td><td>α(.)</td><td>a(1</td><td>a(v）</td><td>a(E）</td><td>α()</td><td>a(）</td><td>α（Y）</td><td>(） α</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>D</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td></tr><tr><td>m1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>04 2</td><td>0 2</td><td>0 2</td><td>电</td><td>中</td></tr><tr><td>n1D</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1 2</td><td>美品 2</td><td></td></tr><tr><td>m2</td><td>1</td><td>1</td><td></td><td>1+0 16</td><td>1+204 32</td><td>1+05 16</td><td>1+206 32</td><td>03+207 32</td><td>04+208 32</td></tr><tr><td>m2D</td><td>0</td><td>1</td><td>#</td><td>1</td><td>1</td><td>1854</td><td>1</td><td>1+0 16</td><td>1+204 32</td></tr><tr><td>m3</td><td>1</td><td>1</td><td></td><td>1-0 4</td><td>1-204</td><td></td><td></td><td>1-207 8</td><td>1-408 16</td></tr><tr><td>m3D</td><td>0</td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td>1-0</td><td>1-204</td></tr><tr><td>m4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>G5</td><td>1 4</td><td></td><td>4</td><td>8</td></tr><tr><td>m4D</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>立</td><td>24 1</td></tr><tr><td>E</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>14</td><td>1</td><td>1</td><td>2</td></tr><tr><td>E</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>12</td><td></td></tr><tr><td>E</td><td>0</td><td>0</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>2 0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">cs&lt;c&lt;cB</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>0</td><td>0</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1 4</td></tr></table>

so that it is RK stable. Other features of the method are that the minimal information passed between steps is enough to push the stage order up to 2, and that the third input and output vector need not be evaluated to great accuracy because of what will be called ‘annihilation conditions’. These conditions ensure that errors like $O ( h ^ { 3 } )$ in the input vector $y _ { 3 } ^ { [ n - 1 ] }$ only affect the output results by $O ( h ^ { 5 } )$ .

Assume that the three input approximations are represented by $\xi _ { 1 } = 1$ , $\xi _ { 2 } = D$ and $\xi _ { 3 }$ , where we assume only that

$$
\xi _ { 3 } ( \emptyset ) = \xi _ { 3 } ( \bullet ) = 0 \qquad \mathrm { a n d } \qquad \xi _ { 3 } ( { \mathfrak { s } } ) = 1 .
$$

Thus, y[1 $y _ { 1 } ^ { [ n - 1 ] } = y ( x _ { n - 1 } ) , y _ { 2 } ^ { [ n - 1 ] } = h y ^ { \prime } ( x _ { n - 1 } ) , y _ { 3 } ^ { [ n - 1 ] } = h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { 3 } )$ . The output approximations are computed by first evaluating the representations of the stage values and stage derivatives. Since we are only working to order 5 accuracy in the output results, it will be sufficient to evaluate the stages only up to order 4. Denote the representations of the four stage values by $\eta _ { i }$ , $i = 1 , 2 , 3 , 4$ . Also, denote the values of $\xi _ { 3 } ( t )$ for trees of orders 3 and 4 by $\theta _ { i }$ , $i = \dag { 3 , 4 , . . . , 8 }$ . Details of the calculation of stage values are shown in Table 543(I).

Output and input values for (505a) evaluated at fifth order trees   

<table><tr><td>α</td><td colspan="8">a(）a(） a（）a（j） a（）a（Y）a（y）（）a（）</td></tr><tr><td></td><td colspan="8"></td></tr><tr><td>S3</td><td>0g 010 1</td><td>011</td><td>012</td><td>013</td><td>014</td><td>015</td><td>016</td><td>017</td></tr><tr><td>R</td><td>1 240</td><td>1+503</td><td>1+1004 480</td><td>1 480</td><td>1 120</td><td>1 240</td><td>1+503</td><td>1+1004</td></tr><tr><td></td><td>120</td><td>240 0</td><td>0</td><td></td><td>0</td><td>0</td><td>240</td><td>480</td></tr><tr><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td></tr><tr><td></td><td>-1</td><td></td><td></td><td></td><td>1</td><td>-1</td><td>4</td><td>1</td></tr><tr><td></td><td></td><td>-</td><td></td><td>-</td><td>1</td><td></td><td></td><td></td></tr></table>

The output results are intended to represent approximations to $E \xi _ { 1 }$ , $E \xi _ { 2 }$ and $E \xi _ { 3 }$ . Write the representation of $y _ { i } ^ { \left[ n \right] }$ by $E \hat { \xi } _ { i }$ , for $i = 1 , 2 , 3 .$ . We calculate $\widehat { \xi } _ { i }$ up to order 5 trees so that we not only verify fourth order behaviour, but also obtain information on the principal terms in the local truncation error. As a first step in this analysis, we note that, to order 4, $E \widehat { \xi } _ { 1 } = E$ and hence $\widehat { \xi _ { 1 } } = 1$ . Similarly $\widehat { \xi _ { 2 } } = D$ to fourth order. Up to fourth order, we have calculated the value of $\begin{array} { r } { E \xi _ { 3 } = - \frac 1 3 \eta _ { 1 } D - \frac 2 3 \eta _ { 3 } D + 2 \eta _ { 4 } D - \xi _ { 2 } } \end{array}$ and $\widehat { \xi _ { 3 } }$ is also given in Table 543(I).

If the calculations are repeated using the specific values $\lvert \theta _ { 3 } , \theta _ { 4 } , \theta _ { 5 } , \theta _ { 6 } , \theta _ { 7 } , \theta _ { 8 } \rvert$ $= [ - 1 , - \frac { 1 } { 2 } , 1 , \frac { 1 } { 2 } , \frac { 1 } { 2 } , \frac { 1 } { 4 } ]$ , then we have $\widehat { \xi _ { i } } = \xi _ { i } + H _ { 4 }$ so that, relative to a starting method defined by $\xi _ { i }$ , $i = 1 , 2 , 3$ , the method has order 4. However, a starting value defined for arbitrary values of $\theta _ { 3 }$ , $\theta _ { 4 }$ , . . . , $\theta _ { 8 }$ produces the specific choice given by the components of $\widehat { \xi _ { 3 } }$ after a single step. To investigate this method more precisely, the values of $\xi _ { 1 }$ , $\widehat { \xi _ { 2 } }$ and $\widehat { \xi _ { 3 } }$ have been calculated also for fifth order trees and these are shown in Table 543(II).

A reading of this table suggests that the method not only exhibits fourth order behaviour but also has reliable behaviour in its principal error terms. This is in spite of the fact that the starting method provides incorrect contributions of third and higher order elementary differentials, because these inaccuracies have no long term effect. The components of the error terms in the first output component depend on $\theta _ { 3 }$ and $\theta _ { 4 }$ after a single step, but this effect disappears in later steps.

In Subsection 544 we consider order 3 ARK methods, and we then return in Subsection 545 to a more detailed study of order 4 methods. However, we first discuss some questions which apply to both orders.

Because we will require methods in these families to have stage order 2, the matrix $U$ will need to be of the form

$$
U = [ \mathbf { 1 } \quad c - A \mathbf { 1 } \quad { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c ]
$$

and we will assume this throughout. We also note that the stability matrix $M ( z ) = V + z B ( I - z A ) ^ { - 1 } U$ is always singular because $z e _ { 1 } ^ { \intercal } - e _ { 2 } ^ { \intercal }$ is an eigenvalue of this matrix. We see this by observing that $z e _ { p } ^ { \intercal } ( I - z A ) = ( - z e _ { 1 } ^ { \intercal } + e _ { 2 } ^ { \intercal } ) B$ and $( z e _ { 1 } ^ { 1 } - e _ { 2 } ^ { 1 } ) V = z e _ { p } ^ { 1 } U$ .

544 Third order, three-stage ARK methods

Since $r = s = 3$ , we will write the coefficient matrices as follows:

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { 0 } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { u _ { 1 2 } } & { u _ { 1 3 } } \\ { 1 } & { u _ { 2 2 } } & { u _ { 2 3 } } \\ { 1 } & { b _ { 0 } } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } \end{array} \right] } .
$$

Denote the abscissa vector by $\boldsymbol { c } = [ c _ { 1 } , c _ { 2 } , 1 ] ^ { \scriptscriptstyle 1 }$ and also write $\boldsymbol { b } ^ { \intercal } = [ b _ { 1 } , b _ { 2 } , 0 ]$ and $\beta ^ { \uparrow } = [ \beta _ { 1 } , \beta _ { 2 } , \beta _ { 3 } ]$ .

Because we will require the method to have stage order 2, the matrix $U$ will need to be of the form given by (543a). For the method to have order 3, and at the same time be RK stable, it is necessary that the trace of $M$ is equal to the Taylor expansion of the non-zero eigenvalue. Thus,

$$
\mathrm { r } ( M ) = \mathrm { t r } ( V ) + z \mathrm { t r } ( B U ) + z ^ { 2 } \mathrm { t r } ( B A U ) + z ^ { 3 } \mathrm { t r } ( B A ^ { 2 } U ) = 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } ,
$$

and it follows that

$$
\begin{array} { c c c } { \operatorname { t r } ( B U ) = 1 , } & { \operatorname { t r } ( B A U ) = \frac { 1 } { 2 } , } & { \operatorname { t r } ( B A ^ { 2 } U ) = \frac { 1 } { 6 } , } \end{array}
$$

where we note that $\operatorname { t r } ( V ) = 1$ , because of the form of $V$ .

To obtain order 3 accuracy for the first output value, it is only necessary that

$$
\begin{array} { r } { b _ { 0 } + b _ { 1 } + b _ { 2 } = 1 , \quad b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } , \quad b _ { 1 } c _ { 1 } ^ { 2 } + b _ { 2 } c _ { 2 } ^ { 2 } = \frac { 1 } { 3 } , } \end{array}
$$

and to obtain an order 2 approximation to the scaled second derivative for the third output value, we require that

$$
\begin{array} { r } { \beta _ { 0 } + \boldsymbol { \beta } ^ { \top } \mathbf { 1 } = 0 , } \\ { \boldsymbol { \beta } ^ { \top } c = 1 . } \end{array}
$$

Note that $\begin{array} { r } { b ^ { \intercal } A c = \frac { 1 } { 6 } } \end{array}$ does not arise as an order condition, because the method has stage order 2. Expand the equations given in (544a), making use of (544b), and we find

$$
\begin{array} { r } { \beta ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { \beta ^ { \top } A ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { b ^ { \top } A c + \beta ^ { \top } A ^ { 2 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = \frac { 1 } { 6 } . } \end{array}
$$

Eliminating terms known to be zero, we see that (544g) simplifies to

$$
b _ { 2 } a _ { 2 1 } c _ { 1 } = \frac { 1 } { 6 ( 1 + \frac { 1 } { 2 } \beta _ { 3 } c _ { 1 } ) } .
$$

Consider the vector $v ^ { \mathsf { T } } = \beta _ { 3 } e _ { 3 } ^ { \mathsf { T } } - \beta ^ { \mathsf { T } } ( I + \beta _ { 3 } A )$ and note that $v ^ { \prime } x _ { 1 } = v ^ { \prime } x _ { 2 } =$ $c ^ { \mathsf { T } } x _ { 3 } = 0$ , where $x _ { 1 } = e _ { 3 }$ , $\begin{array} { r } { x _ { 2 } = \frac { 1 } { 2 } c ^ { 2 } - A c } \end{array}$ and $x _ { 3 } = A ( { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c ) .$ It is not possible that $x _ { 1 } , x _ { 2 } , x _ { 3 }$ are linearly dependent because this would imply $\beta _ { 1 } = \beta _ { 2 } = 0$ , which is inconsistent with $\beta ^ { 1 } { \bf 1 } = 0$ and $\beta ^ { \mathsf { I } } c = 1$ . Hence, $v ^ { \mapsto } = 0$ and we arrange this in the form

$$
\beta ^ { \intercal } = \beta _ { 3 } e _ { 3 } ^ { \intercal } ( I + \beta _ { 3 } A ) ^ { - 1 } = \beta _ { 3 } e _ { 3 } ^ { \intercal } - \beta _ { 3 } ^ { 2 } b ^ { \intercal } + \beta _ { 3 } ^ { 3 } b ^ { \intercal } A .
$$

Multiply (544i) by $c$ and use (544d), (544h) to obtain a relationship between $\beta _ { 3 }$ and $c _ { 1 }$ :

$$
c _ { 1 } = \frac { - 2 ( 1 - \beta _ { 3 } + \frac { 1 } { 2 } \beta _ { 3 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 3 } ^ { 3 } ) } { \beta _ { 3 } ( 1 - \beta _ { 3 } + \frac { 1 } { 2 } \beta _ { 3 } ^ { 2 } ) } .
$$

The ingredients for constructing an ARK method with $p = r = s = 3$ are now all available and they are put together as follows:

1. Choose the value of $\beta _ { 3 }$ .   
2. Evaluate $c _ { 1 }$ from (544j).   
3. Choose the value of $c _ { 2 }$ .   
4. Evaluate $b _ { 0 }$ , $b _ { 1 }$ , $b _ { 2 }$ to satisfy (544b).   
5. Evaluate $a _ { 2 1 }$ to satisfy (544h).   
6. Evaluate the remaining elements of $\beta ^ { \sf I }$ from (544i).   
7. Evaluate the elements of $U$ and $V$ .

together with the choice The following example method is found from $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ : $\beta _ { 3 } = 2$ , leading to $c _ { 1 } = \textstyle { \frac { 1 } { 3 } }$

$$
\begin{array} { r } { [ \begin{array} { c c c c c c } { 0 } & { 0 } & { 0 } & { | ~ 1 } & { \frac { 1 } { 3 } } & { \frac { 1 } { 1 8 } } \\ { \frac { 1 } { 2 } } & { 0 } & { 0 } & { | ~ 1 } & { \frac { 1 } { 6 } } & { \frac { 1 } { 1 8 } } \\ { 0 } & { \frac { 3 } { 4 } } & { 0 } & { 1 } & { \frac { 1 } { 4 } } & { 0 } \\ { 0 } & { \frac { 3 } { 4 } } & { 0 } & { 1 } & { \frac { 1 } { 4 } } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 3 } & { - 3 } & { 2 } \end{array} | ~ . } \end{array}
$$

Further examples of third order ARK methods, together with details on possible interpolation techniques, can be found in Rattenbury (2005).

# 545 Fourth order, four-stage ARK methods

We write specific coefficients of the method as shown in the tableau

$$
\left[ \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { u _ { 1 2 } } } & { { u _ { 1 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { u _ { 2 2 } } } & { { u _ { 2 3 } } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { b _ { 0 } } } & { { 0 } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { b _ { 0 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { \beta _ { 1 } } } & { { \beta _ { 2 } } } & { { \beta _ { 3 } } } & { { \beta _ { 4 } } } & { { \beta _ { 0 } } } & { { 0 } } & { { 0 } } \end{array} \right] .
$$

As usual, $c$ will denote the abscissa vector. We also write $b ^ { \intercal } = \left[ b _ { 1 } \quad b _ { 2 } \quad b _ { 3 } \quad 0 \right]$ and $\beta ^ { 1 } = [ \beta _ { 1 } , \quad \beta _ { 2 } \quad \beta _ { 3 } \quad \beta _ { 4 } ]$ .

As in the example method discussed in Subsection 543, the input approximations will be of the form $y ( x _ { n - 1 } ) + O ( h ^ { 5 } )$ , $h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { 5 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { 3 } )$ , The crucial assumptions we will make are that each of the stages is computed with order at least 2, and that the three output values are not affected by order 3 perturbations in the third input approximation. For stage order 2 it is necessary and sufficient that the matrix $U$ should have the form

$$
U = [ { \bf 1 } c - A { \bf 1 } \frac { 1 } { 2 } c ^ { 2 } - A c ] .
$$

Since $u _ { 4 2 } = b _ { 0 }$ , this will mean that $b ^ { \mathsf { I } } \mathbf { 1 } + b _ { 0 } = 1$ . The conditions for order 4 on the first output component yield the equations

$$
\begin{array} { r } { b ^ { \top } c = \frac { 1 } { 2 } , } \\ { b ^ { \top } c ^ { 2 } = \frac { 1 } { 3 } , } \\ { b ^ { \top } c ^ { 3 } = \frac { 1 } { 4 } , } \\ { b ^ { \top } A c ^ { 2 } = \frac { 1 } { 1 2 } , } \\ { b ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \end{array}
$$

where (545e) is included to ensure that an $O ( h ^ { 3 } )$ error in the third input vector does not detract from the order 4 behaviour. Combining (545b) and (545e), we find

$$
\begin{array} { r } { b ^ { \intercal } A c = \frac { 1 } { 6 } . } \end{array}
$$

Either (545e) or the equivalent condition (545f), together with the related condition on $\beta ^ { 1 }$ given in (545i) below, will be referred to as ‘annihilation conditions’. The vector $\beta ^ { \intercal }$ , together with $\beta _ { 0 }$ , defines the third output approximation, which is required to give the result $h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + O ( h ^ { 3 } )$ . Hence,

$$
\begin{array} { r } { \beta ^ { \mathsf { T } } \mathbf { 1 } + \beta _ { 0 } = 0 , } \\ { \beta ^ { \mathsf { T } } c = 1 . } \end{array}
$$

We now turn to the conditions for RK stability. If the stability matrix

$$
M ( z ) = V + z B U + z ^ { 2 } B A U + z ^ { 3 } B A ^ { 2 } U + z ^ { 4 } B A ^ { 3 } U
$$

is of $M ( z )$ e only a single non-zero eige and for order 4 must equal $\begin{array} { r } { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } } \end{array}$ st. tracerefore impose the conditions that the traces of $B U$ , $B A U$ , $B A ^ { 2 } U$ and $B A ^ { 3 } U$ values $^ { 1 }$ , $\textstyle { \frac { 1 } { 2 } }$ , $\textstyle { \frac { 1 } { 6 } }$ , $\textstyle { \frac { 1 } { 2 4 } }$ , respectively. These can be written in the form

$$
\begin{array} { r } { \beta ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 . } \\ { \beta ^ { \top } A ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { \beta ^ { \top } A ^ { 2 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { b ^ { \top } A ^ { 2 } c + \beta ^ { \top } A ^ { 3 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = \frac { 1 } { 2 4 } . } \end{array}
$$

Because $A ^ { 4 } = 0$ , (545l) simplifies to

$$
b ^ { \mathsf { T } } A ^ { 2 } c = { \frac { 1 } { 2 4 ( 1 + { \frac { 1 } { 2 } } \beta _ { 4 } c _ { 1 } ) } } .
$$

We now show that $\beta ^ { \sf I }$ satisfies the equation

$$
\beta _ { 4 } e _ { 4 } ^ { \mathsf { T } } = \beta ^ { \mathsf { T } } ( I + \beta _ { 4 } A ) .
$$

This follows by observing that $\beta _ { 4 } e _ { 4 } ^ { \mathsf { I } } - \beta ^ { \mathsf { I } } ( I + \beta _ { 4 } A )$ multiplied respectively by $e _ { 4 }$ , ${ \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c$ , $A ( \scriptstyle { \frac { 1 } { 2 } } c ^ { 2 } - A c )$ and $A ^ { 2 } ( { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c )$ are each zero if and only if each of (545j), (545k) and (545l) holds.

Multiply each side of (545n) by $( I + \beta _ { 4 } A ) ^ { - 1 } c$ and use (545h) to show that

$$
1 = \beta _ { 4 } - \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } + \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } - \frac { \beta _ { 4 } ^ { 4 } } { 2 4 ( 1 + \frac { 1 } { 2 } \beta _ { 4 } c _ { 1 } ) } ,
$$

from which it follows that

$$
c _ { 1 } = \frac { - 2 ( 1 - \beta _ { 4 } + \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } + \frac { 1 } { 2 4 } \beta _ { 4 } ^ { 4 } ) } { \beta _ { 4 } ( 1 - \beta _ { 4 } + \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } ) } .
$$

To construct a four-stage fourth order ARK method in detail, carry out the following steps:

1. Choose the value of $\beta _ { 4 }$ .   
2. Evaluate $c _ { 1 }$ from (545o).   
3. Choose values of $c _ { 2 }$ and $c _ { 3 }$ .   
4. Evaluate $b _ { 0 }$ , $b _ { 1 }$ , $b _ { 2 }$ , $b _ { 3 }$ to satisfy (545a), (545b), (545c), (545g).   
5. Evaluate $a _ { 2 1 }$ , $a _ { 3 1 }$ , $a _ { 3 2 }$ to satisfy (545f), (545d), (545m).   
6. Evaluate the remaining elements of $\beta ^ { \mathsf { T } }$ from (545n).   
7. Evaluate the elements of $U$ and $V$ .

In contrast to the method given in (505a), the following method has the same $c = [ 1 \quad { \scriptstyle { \frac { 1 } { 2 } } } \quad { \scriptstyle { \frac { 1 } { 2 } } } \quad 1 ] ^ { \intercal }$ but different $b ^ { \top }$ :

<table><tr><td>0 0 1 0 16 1 16</td><td>0 0 1 0</td><td>0 1 0 1 0 1</td><td>1 7 16 7 16</td><td>1-21-165 16</td></tr><tr><td>1</td><td>1</td><td>1 0 1 0</td><td>1 1 1 1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0 0</td><td>0</td></tr><tr><td></td><td>4</td><td>4 2</td><td>0 -1</td><td>0</td></tr></table>

A further example with $\begin{array} { r } { c = [ \frac { 1 1 } { 2 4 } \frac { 1 3 } { 2 4 } 1 1 1 ] ^ { ! } } \end{array}$ is given by the matrix

<table><tr><td rowspan=1 colspan=1>0      0      0     0</td><td rowspan=1 colspan=1>11         121124        1152</td></tr><tr><td rowspan=1 colspan=1>104     0      0     0297</td><td rowspan=1 colspan=1>1    455        1432376      10368</td></tr><tr><td rowspan=1 colspan=1>1820    44      0     04653    47</td><td rowspan=1 colspan=1>1523       47314653       2538</td></tr><tr><td rowspan=1 colspan=1>48     48     47    0143    143    286</td><td rowspan=1 colspan=1>1     47         0286</td></tr><tr><td rowspan=1 colspan=1>48     48     47    0143    143    286</td><td rowspan=1 colspan=1>1     47         0286</td></tr><tr><td rowspan=1 colspan=1>0      0      0     1</td><td rowspan=1 colspan=1>0     0          0</td></tr><tr><td rowspan=1 colspan=1>354    162    423    3143    143    286</td><td rowspan=1 colspan=1>51         00286</td></tr></table>

These methods were introduced in Butcher (1997, 1998). Although it does not seem possible to find similar methods with $s = p$ stages where $p > 4$ , we will see in the next subsection that something very similar can be achieved.

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

# 547 ARK methods for stiff problems

In Butcher and Rattenbury (2005), the ARK type of method was extended to the solution of stiff problems. Methods were presented with orders 3 and 4, subject to a number of criteria, and these were supported by preliminary numerical comparisons with standard methods. Because stiff ARK methods are still at an early stage of development, we will not attempt to give a full description, but will present a single third order method,

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = \left[ { \begin{array} { c c c c c c } { { \frac { 1 } { 3 } } } & { 0 } & { 0 } & { 0 } & { { \frac { 1 } { 3 } } } & { { \frac { 2 } { 6 } } } \\ { - { \frac { 1 } { 1 6 } } } & { { \frac { 1 } { 3 } } } & { 0 } & { { \frac { 1 } { 4 8 } } } & { { \frac { 1 } { 4 8 } } } \\ { - { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { 0 } } \\ { - { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { 0 } } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { { \frac { 1 } { 3 } } } & { - { \frac { 8 } { 3 } } } & { 2 } & { { \frac { 1 } { 3 } } } & { 0 } \end{array} } \right] ,
$$

together with a convenient starting method. This is not the most successful of the methods known so far, but it has simple coefficients and will serve for illustrative purposes.

To start the method, and simultaneously progress the method a single step forward, the starting method should be a three-output Runge–Kutta method. For input the value of $y ( x _ { 0 } )$ , the method given in the following tableau gives suitable approximations to $y ( x _ { 1 } )$ , $h y ^ { \prime } ( x _ { 1 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { 1 } )$ :

$$
\begin{array}{c} \left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac { 1 } { 3 } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { \frac { 1 } { 3 } } & { \frac { 1 } { 3 } } & { 0 } & { 0 } \\ { - \frac { 5 } { 3 } } & { \frac { 4 } { 3 } } & { \frac { 1 } { 3 } } & { 0 } \\ { \frac { 1 } { 1 } } & { - \frac { 1 } { 4 } } & { - \frac { 1 } { 1 2 } } & { \frac { 1 } { 3 } } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { - 2 } & { - 1 } & { \frac { 2 } { 3 } } & { \frac { 7 } { 3 } } \end{array} \right] 1  \end{array}
$$

For the method given by (547a), the stability function is

$$
R ( z ) = \frac { 1 - \frac { 1 } { 6 } z ^ { 2 } - \frac { 1 } { 2 7 } z ^ { 3 } } { ( 1 - \frac { 1 } { 3 } z ) ^ { 3 } } ,
$$

and it can be verified to satisfy the conditions of A-stability.

Further details concerning stiff ARK methods, and of ARK methods in general, can be found in Rattenbury (2005).

# Exercises 54

54.1 Find the stability matrix of the method given by (542b) and verify that it is RK-stable.

54.2 Does a transformation matrix exist such that the input to the transformed method approximates the two quantities $y ( x _ { n - 1 } + \theta h )$ and $h y ^ { \prime } ( x _ { n - 1 } + \theta h )$ , in each to within $O ( h ^ { 3 } )$ , for some $\theta$ ?

54.3 Show that the method given by (542c) is L-stable.

54.4 Is the same true for the method in which $\sqrt { 2 }$ is replaced by $- { \sqrt { 2 } }$ throughout?

54.5 Which of the two methods (542c) and the method where the sign of $\sqrt { 2 }$ is reversed, is likely to be more accurate?

54.6 Find a third order ARK method with $\beta _ { 3 } = 2$ and $c _ { 2 } = 1$

# 55 Methods with Inherent Runge–Kutta Stability

# 550 Doubly companion matrices

As a preliminary to a discussion of inherent RK stability, we recall the properties of the matrices introduced by Butcher and Chartier (1997). The original application was in the analysis of singly implicit methods with a specific effective order, but they also have a central role in the construction of the methods to be considered in Subsection 551. A review of doubly companion matrices is given in Butcher and Wright (2006).

Let $\alpha ( z ) = 1 + \alpha _ { 1 } z + \cdot \cdot \cdot + \alpha _ { n } z ^ { n }$ and $\beta ( z ) = 1 + \beta _ { 1 } z + \cdot \cdot \cdot + \beta _ { n } z ^ { n }$ denote given polynomials, and consider the $n \times n$ matrix

$$
X = \left[ { \begin{array} { c c c c c c c c } { - \alpha _ { 1 } } & { - \alpha _ { 2 } } & { - \alpha _ { 3 } } & { \cdots } & { - \alpha _ { n - 1 } } & { - \alpha _ { n } - \beta _ { n } } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - \beta _ { n - 1 } } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { - \beta _ { n - 2 } } \\ { \vdots } & { \vdots } & { \vdots } & & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - \beta _ { 1 } } \end{array} } \right] .
$$

Theorem 550A The coefficients in the characteristic polynomial of $X$ , $\operatorname* { d e t } ( w I - X ) = w ^ { n } + \gamma _ { 1 } w ^ { n - 1 } + \gamma _ { 2 } w ^ { n - 2 } + \cdot \cdot \cdot + \gamma _ { n }$ , are given by

$$
1 + \gamma _ { 1 } z + \gamma _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \gamma _ { n } z ^ { n } = \operatorname * { d e t } ( I - z X ) = \alpha ( z ) \beta ( z ) + O ( z ^ { n + 1 } ) .
$$

Proof. We assume that the eigenvalues of $X$ are distinct and non-zero. There is no loss of generality in this assumption because, for given values of the $\alpha$ coefficients, the coefficients in the characteristic polynomial are continuous functions of the $\beta$ coefficients; furthermore, choices of the $\beta$ coefficients which lead to distinct non-zero eigenvalues form a dense set.

Let $\lambda$ denote an eigenvalue of $X$ , and let

$$
\begin{array} { r } { v _ { k } = \lambda ^ { k } + \beta _ { 1 } \lambda ^ { k - 1 } + \beta _ { 2 } \lambda ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } , \qquad k = 0 , 1 , 2 , \dots , n . } \end{array}
$$

By comparing components numbered $n$ , $n - 1 , \ldots , 2$ of $X v$ and $\lambda v$ , where

$$
V = [ v _ { n - 1 } \quad v _ { n - 2 } \quad \cdot \cdot \cdot \quad 1 ] ^ { \top } ,
$$

we see that $v$ is the eigenvector corresponding to $\lambda$ . Now compare the first components of $\lambda v$ and $X v$ and it is found that

$$
\lambda v _ { n } + \alpha _ { 1 } v _ { n - 1 } + \cdot \cdot \cdot + \alpha _ { n } = 0
$$

and contains all the terms with non-negative exponents in the product

$$
v _ { n } ( 1 + \alpha _ { 1 } \lambda ^ { - 1 } + \cdots + \alpha _ { n } \lambda ^ { - n } ) .
$$

Replace $\lambda$ by $z ^ { - 1 }$ and the result follows.

Write $\phi ( z )$ for the vector (550b) with $\lambda$ replaced by $z$ . We now note that

$$
z \phi ( z ) - X \phi ( z ) = \prod _ { i = 1 } ^ { n } ( z - \lambda _ { i } ) e _ { 1 } ,
$$

because the expression vanishes identically except for the first component which is a monic polynomial of degree $n$ which vanishes when $z$ is an eigenvalue.

We are especially interested in choices of $\alpha$ and $\beta$ such that $X$ has a single $n$ -fold eigenvalue, so that

$$
\alpha ( z ) \beta ( z ) = ( 1 - \lambda z ) ^ { n } + O ( z ^ { n + 1 } )
$$

and so that the right-hand side of (550c) becomes $( z - \lambda ) ^ { n } e _ { 1 }$ . In this case it is possible to write down the similarity that transforms $X$ to Jordan canonical form.

Theorem 550B Let the doubly companion matrix $X$ be chosen so that (550d) holds. Also let $\phi ( z )$ denote the vector given by (550b) with $\lambda$ replaced by $z$ , and let $S$ the matrix given by

$$
\begin{array} { r } { \Psi = \big [ \frac { 1 } { ( n - 1 ) ! } \phi ^ { ( n - 1 ) } ( \lambda ) \quad \frac { 1 } { ( n - 2 ) ! } \phi ^ { ( n - 2 ) } ( \lambda ) \quad \cdots \quad \frac { 1 } { 1 ! } \phi ^ { \prime } ( \lambda ) \quad \phi ( \lambda ) \big ] . } \end{array}
$$

Then

$$
\Psi ^ { - 1 } X \Psi = \left[ \begin{array} { l l l l l l } { \lambda } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { \lambda } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { \lambda } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { \lambda } \end{array} \right] .
$$

Proof. From the special case of (550c), we have

$$
X \phi ( z ) = z \phi ( z ) - ( z - \lambda ) ^ { n } e _ { 1 } .
$$

Differentiate $k$ times, divide by $k$ ! and set $z = \lambda$ , for $k = 1 , 2 , \ldots , n - 1$ . The result is

$$
X \frac { 1 } { k ! } \phi ^ { ( k ) } ( \lambda ) = \lambda I \frac { 1 } { k ! } \phi ^ { ( k ) } ( \lambda ) + \frac { 1 } { ( k - 1 ) ! } \phi ^ { ( k - 1 ) } ( \lambda ) , \qquad k = 1 , 2 , \ldots , n - 1 .
$$

Hence the vectors $\phi ( \lambda )$ , $\phi ^ { \prime } ( \lambda ) , \textstyle { \frac { 1 } { 2 ! } } \phi ^ { \prime \prime } ( \lambda ) , \dots , \textstyle { \frac { 1 } { ( n - 1 ) ! } } \phi ^ { ( n - 1 ) } ( \lambda )$ form a sequence of eigenvector and generalized eigenvectors, and the result follows. 

The inverse of $\Psi$ is easy to evaluate by interchanging the roles of rows and columns of $X$ . We present the following result without further proof.

# Corollary 550C If

$$
\begin{array} { r } { \chi ( \lambda ) = [ 1 \quad \lambda + \alpha _ { 1 } \quad \lambda ^ { 2 } + \alpha _ { 1 } \lambda + \alpha _ { 2 } \quad \cdots \quad \lambda ^ { n - 1 } + \alpha _ { 1 } \lambda ^ { n - 2 } + \cdots + \alpha _ { n - 1 } ] , } \end{array}
$$

then

$$
\Psi ^ { - 1 } = [ \chi ( \lambda ) \quad { \textstyle { \frac { 1 } { 1 ! } } } \chi ^ { \prime } ( \lambda ) \quad \cdots \quad { \textstyle { \frac { 1 } { ( n - 2 ) ! } } } \chi ^ { ( n - 2 ) } ( \lambda ) \quad { \textstyle { \frac { 1 } { ( n - 1 ) ! } } } \chi ^ { ( n - 1 ) } ( \lambda ) ] ^ { \top } .
$$

# 551 Inherent Runge–Kutta stability

In this subsection we discuss a special type of general linear method based on several assumptions on the form of the method. The original formulation for stiff methods was given in Butcher (2001) and for non-stiff methods in Wright (2002). In Butcher and Wright (2003) it was shown how these ans¨atze are interrelated and this led to the current formulation in Butcher and Wright (2003a).

Besides making use of doubly companion matrices, we also use the special $r \times r$ matrix $J$ and its transpose $K$ , where

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right] .
$$

For the special type of inherently RK stable general linear method we consider, $A$ has the diagonally implicit form

$$
A = \left[ \begin{array} { c c c c c } { { \lambda } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { \lambda } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { a _ { s 1 } } } & { { a _ { s 2 } } } & { { a _ { s 3 } } } & { { \cdots } } & { { \lambda } } \end{array} \right] ,
$$

with $\lambda \geq 0$ , and $V$ has the form

$$
V = \left[ \begin{array} { l l } { 1 } & { v ^ { \textsf { T } } } \\ { 0 } & { \dot { V } } \end{array} \right] ,
$$

where $\rho ( \dot { V } ) = 0$ , with $\rho$ denoting spectral radius. We assume that $p = q$ and that $s = r = p + 1$ . In some special cases, the last columns of $U$ and $V$ will vanish, thus making it possible for $r$ to be reduced to $r = p$ .

Definition 551A A general linear method $( A , U , B , V )$ is ‘inherently Runge– Kutta stable’ if $V$ is of the form (551a) and the two matrices

$$
B A - X B \qquad a n d \qquad B U - X V + V X
$$

are zero except for their first rows, where $X$ is some matrix.

The significance of this definition is expressed in the following.

Theorem 551B Let $( A , U , B , V )$ denote an inherently RK stable general linear method. Then the stability matrix

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U
$$

has only a single non-zero eigenvalue.

Proof. Calculate the matrix

$$
( I - z X ) M ( z ) ( I - z X ) ^ { - 1 } ,
$$

which has the same eigenvalues as $M ( z )$ . We use the notation $=$ to denote equality of two matrices, except for the first rows. Because $B A \equiv X B$ and $B U \equiv X V - V X$ , it follows that

$$
\begin{array} { l } { { ( I - z X ) B \equiv B ( I - z A ) , } } \\ { { ( I - z X ) V \equiv V ( I - z X ) - z B U , } } \end{array}
$$

so that

$$
( I - z X ) M ( z ) \equiv V ( I - z X ) .
$$

Hence $( I - z X ) M ( z ) ( I - z X ) ^ { - 1 }$ is identical to $V$ , except for the first row. Thus the eigenvalues of this matrix are its $( 1 , 1 )$ element together with the $p$ zero eigenvalues of $\dot { V }$ . 

Since we are adopting, as standard $r = p + 1$ and a stage order $q = p$ , it is possible to insist that the vector-valued function of $z$ , representing the input approximations, comprises a full basis for polynomials of degree $p$ . Thus, we will introduce the function $Z$ given by

$$
Z = \left[ \begin{array} { c } { { 1 } } \\ { { z } } \\ { { z ^ { 2 } } } \\ { { \vdots } } \\ { { z ^ { p } } } \end{array} \right] ,
$$

which represents the input vector

$$
y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 1 } ) } \\ { h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) } \\ { \vdots } \\ { h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) } \end{array} \right] .
$$

This is identical, except for a simple rescaling by factorials, to the Nordsieck vector representation of input and output approximations, and it will be convenient to adopt this as standard.

Assuming that this standard choice is adopted, the order conditions are

$$
\begin{array} { r } { \exp ( c z ) = z A \exp ( c z ) + U Z + O ( z ^ { p + 1 } ) , } \\ { \exp ( z ) Z = z B \exp ( c z ) + V Z + O ( z ^ { p + 1 } ) . } \end{array}
$$

This result, and generalizations of it, make it possible to derive stiff methods of quite high orders. Furthermore, Wright (2003) has shown how it is possible to derive explicit methods suitable for non-stiff problems which satisfy the same requirements. Following some more details of the derivation of these methods, some example methods will be given.

# 552 Conditions for zero spectral radius

We will need to choose the parameters of IRKS methods so that the $p \times p$ matrix $\dot { V }$ has zero spectral radius. In Butcher (2001) it was convenient to force $\dot { V }$ to be strictly lower triangular, whereas in the formulation in Wright (2002) it was more appropriate to require $\dot { V }$ to be strictly upper triangular. To get away from these arbitrary choices, and at the same time to allow a wider range of possible methods, neither of these assumptions will be made and we explore more general options. To make the discussion non-specific to the application to IRKS methods, we assume we are dealing with $n \times n$ matrices related by a linear equation of the form

$$
y = a x b - c ,
$$

and the aim will be to find lower triangular $x$ such that $y$ is strictly upper triangular. The constant matrices $a$ , $b$ and $c$ will be assumed to be non-singular and LU factorizable. In this discussion only, define functions $\lambda$ , $\mu$ and $\delta$ so that for a given matrix $a$ ,

$\lambda ( a )$ is unit lower triangular such that $\lambda ( a ) ^ { - 1 } a$ is upper triangular, $\mu ( a )$ is the upper triangular matrix such that $a = \lambda ( { a } ) \mu ( { a } )$ , $\delta ( a )$ is the lower triangular part of $a$ .

Using these functions we can find the solution of (552a), when this solution exists. We have in turn

$$
\begin{array} { c } { { \delta ( a x b ) = \delta ( c ) , } } \\ { { \delta \bigl ( \mu ( a ^ { - 1 } ) ^ { - 1 } \lambda ( a ^ { - 1 } ) ^ { - 1 } x \lambda ( b ) \mu ( b ) \bigr ) = \delta ( c ) , } } \\ { { \delta \bigl ( \lambda ( a ^ { - 1 } ) ^ { - 1 } x \lambda ( b ) \bigr ) = \delta \bigl ( \mu ( a ^ { - 1 } ) \delta ( c ) \mu ( b ) ^ { - 1 } \bigr ) , } } \end{array}
$$

implying that

$$
x = \delta \big ( \lambda ( a ^ { - 1 } ) \delta \big ( \mu ( a ^ { - 1 } ) \delta ( c ) \mu ( b ) ^ { - 1 } \big ) \lambda ( b ) ^ { - 1 } \big ) .
$$

Thus, (552b) is the required solution of (552a).

This result can be generalized by including linear constraints in the formulation. Let $d$ and $e$ denote vectors in $\mathbb { R } ^ { n }$ and consider the problem

$$
\delta ( a x b - c ) = 0 , \qquad x d = e .
$$

Assume that $d$ is scaled so that its first component is 1. The matrices $a$ , $b$ and $c$ are now, respectively $n \times ( n - 1 )$ , $( n - 1 ) \times n$ and $( n - 1 ) \times ( n - 1 )$ . Partition these, and the vectors $d$ and $e$ , as

$$
\begin{array} { r } { a = \left[ \begin{array} { l l } { a _ { 1 } } & { a _ { 2 } } \end{array} \right] , \quad b = \left[ \begin{array} { l } { b _ { 1 } ^ { \top } } \\ { b _ { 2 } } \end{array} \right] , \quad d = \left[ \begin{array} { l } { 1 } \\ { d _ { 2 } } \end{array} \right] , \quad e = \left[ \begin{array} { l } { e _ { 1 } } \\ { e _ { 2 } } \end{array} \right] , } \end{array}
$$

where $a _ { 1 }$ is a single column and $b _ { 1 } ^ { \mathsf { I } }$ a single row.

The solution to this problem is

$$
\boldsymbol { x } = \left[ \begin{array} { c c } { \boldsymbol { e } _ { 1 } } & { \boldsymbol { 0 } } \\ { \boldsymbol { e } _ { 2 } - \widehat { \boldsymbol { x } } d _ { 2 } } & { \widehat { \boldsymbol { x } } } \end{array} \right] ,
$$

where $\widehat { x }$ satisfies $\delta ( \widehat { a x b } - c ) = 0$ , and

$$
\widehat { \boldsymbol { a } } = \boldsymbol { a } _ { 2 } , \quad \widehat { \boldsymbol { b } } = \boldsymbol { b } _ { 2 } - d _ { 2 } \boldsymbol { b } _ { 1 } ^ { \intercal } , \quad \widehat { \boldsymbol { c } } = \boldsymbol { c } - \boldsymbol { a e b } _ { 1 } ^ { \intercal } .
$$

Finally we consider the addition of a second constraint so that the problem becomes

$$
\delta ( a x b - c ) = 0 , \qquad x d = e , \qquad f ^ { \top } x = g ^ { \top } ,
$$

where $c$ is $( n - 2 ) \times ( n - 2 )$ and the dimensions of the various other matrix and vector partitions, including the specific values $d _ { 1 } = f _ { 3 } = 1$ , are indicated in parentheses

$$
\begin{array} { r l r } { \boldsymbol { a } = \left[ \begin{array} { l l l } { ^ { ( 1 ) } } & { ^ { ( n - 2 ) } } & { ^ { ( 1 ) } } \\ { ^ { ( 1 ) } } & { ^ { ( 2 ) } } & { ^ { ( 3 ) } } \end{array} \right] ( n - 2 ) } & { b = \left[ \begin{array} { l } { ^ { \left[ b \right] } _ { 1 } ^ { \top } } \\ { b _ { 2 } } \\ { b _ { 3 } } \end{array} \right] ( n - 2 ) } & { d = \left[ \begin{array} { l } { ^ { ( 1 ) } } \\ { 1 } \\ { d _ { 2 } } \\ { d _ { 3 } } \end{array} \right] ( n - 2 ) } \\ { \boldsymbol { e } = \left[ \begin{array} { l } { ^ { ( 1 ) } } \\ { e _ { 1 } } \\ { e _ { 2 } } \\ { e _ { 3 } } \end{array} \right] ( 1 ) } & { f ^ { \top } = \left[ \begin{array} { l l l } { ^ { ( 1 ) } } & { ^ { ( n - 2 ) } } & { ^ { ( 1 ) } } \\ { f _ { 1 } } & { f _ { 2 } ^ { \top } } & { 1 } \end{array} \right] ( 1 ) } & { g ^ { \top } = \left[ \begin{array} { l l l } { ^ { ( 1 ) } } & { ^ { ( n - 2 ) } } & { ^ { ( 1 ) } } \\ { g _ { 1 } } & { g _ { 2 } ^ { \top } } & { g _ { 3 } } \end{array} \right] ( 1 ) } \end{array}
$$

For both linear constraints to be satisfied it is necessary that $f ^ { \prime } e = f ^ { \prime } B d =$ $g ^ { \prime } d$ . Assuming this consistency condition is satisfied, denote the common value of $f ^ { \prime } e$ and $g ^ { \prime } d$ by $\theta$ . The solution can now be written in the form

$$
\begin{array} { r } { x = \left[ \begin{array} { c c c } { e _ { 1 } } & { 0 } & { 0 } \\ { e _ { 2 } - \widehat { x } d _ { 2 } } & { \widehat { x } } & { 0 } \\ { e _ { 3 } + g _ { 1 } - \theta + f _ { 2 } ^ { \top } \widehat { x } d _ { 2 } } & { g _ { 2 } - f _ { 2 } ^ { \top } \widehat { x } } & { g _ { 3 } } \end{array} \right] , } \end{array}
$$

where

$$
\delta ( \widehat { a } \widehat { x } \widehat { b } - \widehat { c } ) = 0 ,
$$

with

$$
\widehat { a } = a _ { 2 } - a _ { 3 } f _ { 2 } ^ { \intercal } , \qquad \widehat { b } = b _ { 2 } - d _ { 2 } b _ { 1 } ^ { \intercal } , \qquad \widehat { c } = c - a e b _ { 1 } ^ { \intercal } - a _ { 3 } g ^ { \intercal } b + \theta a _ { 3 } b _ { 1 } ^ { \intercal } .
$$

553 Derivation of methods with IRK stability

For the purpose of this discussion, we will always assume that the input approximations are represented by $Z$ given by (551b), so that these approximations as input to step $n$ are equal, to within $O ( h ^ { p + 1 } )$ , to the quantities given by (551c).

Theorem 553A If a general linear method with $p = q = r - 1 = s - 1$ has the property of IRK stability then the matrix $X$ in Definition 551A is a $( p + 1 ) \times ( p + 1 )$ doubly companion matrix.

Proof. Substitute (551d) into (551e) and compare (551d) with $z X$ multiplied on the left. We find

$$
\begin{array} { c } { { \exp ( z ) Z = z ^ { 2 } B A \exp ( c z ) + z B U Z + V Z + O ( z ^ { p + 1 } ) , } } \\ { { z \exp ( z ) X Z = z ^ { 2 } X B \exp ( c z ) + z X V Z + O ( z ^ { p + 1 } ) . } } \end{array}
$$

Because $B A \equiv X B$ and $B U \equiv X V - V X$ , the difference of (553a) and (553b) implies that

$$
z X Z \equiv Z + O ( z ^ { p + 1 } ) .
$$

Because $z J Z \equiv Z + O ( z ^ { p + 1 } )$ , it now follows that

$$
( X - J ) Z \equiv O ( z ^ { p } ) ,
$$

which implies that $X - J$ is zero except for the first row and last column. 

We will assume without loss of generality that $\beta _ { p + 1 } = 0$ .

By choosing the first row of $X$ so that $\sigma ( X ) = \sigma ( A )$ , we can assume that the relation $B A = X B$ applies also to the first row. We can now rewrite the defining equations in Definition 551A as

$$
\begin{array} { l } { { B A = X B , } } \\ { { B U = X V - V X + e _ { 1 } \xi ^ { \mathsf { T } } , } } \end{array}
$$

where $\xi ^ { \intercal } ~ = ~ [ \xi _ { 1 } ~ \xi _ { 2 } ~ \cdot ~ \cdot ~ \cdot ~ \xi _ { p + 1 } ]$ is a specific vector. We will also write $\xi ( z ) = \xi _ { 1 } z + \xi _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \xi _ { p + 1 } z ^ { p + 1 }$ . The transformed stability function in Theorem 551B can be recalculated as

$$
( I - z X ) { \cal M } ( z ) ( I - z X ) ^ { - 1 } = V + z e _ { 1 } \xi ^ { \top } ( I - z X ) ^ { - 1 } ,
$$

with $( 1 , 1 )$ element equal to

$$
\begin{array} { c } { { 1 + z \xi ( I - z X ) ^ { - 1 } e _ { 1 } = \displaystyle \frac { \operatorname* { d e t } ( I + z ( e _ { 1 } \xi - X ) ) } { \operatorname* { d e t } ( I - z X ) } } } \\ { { = \displaystyle \frac { ( \alpha ( z ) + \xi ( z ) ) \beta ( z ) } { \alpha ( z ) \beta ( z ) } + { \cal O } ( z ^ { p + 2 } ) , } } \end{array}
$$

where the formula for the numerator follows by observing that $X - e _ { 1 } \xi$ is a doubly companion matrix, in which the $\alpha$ elements in the first row are replaced by the coefficients of $\alpha ( z ) + \xi ( z )$ .

The $( 1 , 1 )$ element of the transformed stability matrix will be referred to as the ‘stability function’ and denoted by $R ( z )$ . It has the same role for IRKS methods as the stability function of a Runge–Kutta method. For implicit methods, the stability function will be $R ( z ) = N ( z ) / ( 1 - \lambda z ) ^ { p + 1 }$ , where $N ( z )$ is a polynomial of degree $p + 1$ given by

$$
N ( z ) = \exp ( z ) ( 1 - \lambda z ) ^ { p + 1 } - \epsilon _ { 0 } z ^ { p + 1 } + O ( z ^ { p + 2 } ) .
$$

The number $\epsilon _ { \mathrm { 0 } }$ is the ‘error constant’ and is a design parameter for a particular method. It would normally be chosen so that the coefficient of $z ^ { p + 1 }$ in $N ( z )$ is zero. This would mean that if $\lambda$ is chosen for A-stability, then this choice of $\epsilon _ { \mathrm { 0 } }$ would give L-stability.

For non-stiff methods, $\lambda = 0$ and $N ( z ) = \exp ( z ) - \epsilon _ { 0 } z ^ { p + 1 } + O ( z ^ { p + 2 } )$ . In this case, $\epsilon _ { \mathrm { 0 } }$ would be chosen to balance requirements of accuracy against an acceptable stability region.

In either case, we see from (553e) that $N ( z ) = \alpha ( z ) ( \beta ( z ) + \xi ( z ) ) + O ( z ^ { p + 1 } )$ , so that $\xi ( z )$ , and hence the coefficients $\xi _ { 1 }$ , $\xi _ { 2 }$ , . . . , $\xi _ { p + 1 }$ can be found.

Let $C$ denote the $( p + 1 ) \times ( p + 1 )$ matrix with $( i , j )$ element equal to $c _ { i } ^ { j - 1 } / ( j - 1 )$ ! and $E$ the $( p + 1 ) \times ( p + 1 )$ matrix with $( i , j )$ element equal to $1 / ( j - i ) !$ ! (with the usual convention that this element vanishes if $i > j$ ). We can now write (551d) and (551e) as

$$
\begin{array} { r } { U = C - A C K , } \\ { V = E - B C K . } \end{array}
$$

Substitute into (553d) and make use of (553c) and we find

$$
B C ( I - K X ) = X E - E X + e _ { 1 } \xi ^ { \mathsf { T } } .
$$

Both $I - K X$ and $X E - E X + e _ { 1 } \xi ^ { \intercal }$ vanish, except for their last columns, and (553f) simplifies to

$$
B C \left[ \begin{array} { c } { \beta _ { p } } \\ { \beta _ { p - 1 } } \\ { \vdots } \\ { \beta _ { 1 } } \\ { 1 } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac 1 { 1 ! } } & { \frac 1 { 2 ! } } & { \cdots } & { \frac 1 { p ! } } & { \frac 1 { ( p + 1 ) ! } - \epsilon _ { 0 } } \\ { 0 } & { \frac 1 { 1 ! } } & { \cdots } & { \frac 1 { ( p - 1 ) ! } } & { \frac 1 { ( p ) ! } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { \frac 1 { 1 ! } } & { \frac 1 { 2 ! } } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { \frac 1 { 1 ! } } \end{array} \right] \left[ \begin{array} { c } { \beta _ { p } } \\ { \beta _ { p - 1 } } \\ { \vdots } \\ { \beta _ { 1 } } \\ { 1 } \end{array} \right] .
$$

Imposing conditions on the spectrum of $V$ implies constraints on $B$ . This principle is used to derive methods with a specific choice of the vector $\beta$ and the abscissa vector $c$ .

Rather than work in terms of $B$ directly, we introduce the matrix $\widetilde { B } =$ $\Psi ^ { - 1 } B$ . Because

$$
{ \widetilde { B } } A = ( J + \lambda I ) { \widetilde { B } } ,
$$

and because both $A$ and $J + \lambda I$ are lower triangular, $\widetilde { B }$ is also lower triangular. In the derivation of a method, $\widetilde { B }$ will be found first and the method coefficient matrices found in terms of this as

$$
\begin{array} { l } { { A = \widetilde { B } ^ { - 1 } ( J + \lambda I ) \widetilde { B } , } } \\ { { U = C - A C K , } } \\ { { B = \Psi \widetilde { B } , } } \\ { { V = E - B C K . } } \end{array}
$$

To construct an IRKS method we need to carry out the following steps:

1. Choose the value of $\lambda$ and $\epsilon _ { \mathrm { 0 } }$ taking into account requirements of stability and accuracy.   
2. Choose $c _ { 1 }$ , $c _ { 2 }$ , $\cdot \cdot \cdot$ , $c _ { p + 1 }$ . These would usually be distributed more or less uniformly in $[ 0 , 1 ]$ .   
3. Choose $\beta _ { 1 }$ , $\beta _ { 2 }$ , $\cdot \cdot \cdot$ , $\beta _ { p }$ . This choice is to some extent arbitrary but can determine the magnitude of some of the elements in the coefficient matrices of the method.   
4. Choose a non-singular $p \times p$ matrix $P$ used to determine in what way $\dot { V }$ has zero spectral radius. If $\delta$ is defined as in Subsection 552, then we will impose the condition $\delta ( P ^ { - 1 } \dot { V } P ) = 0$ . It would be normal to choose $P$ as the product of a permutation matrix and a lower triangular matrix.

5. Solve the linear equations for the non-zero elements of $\widetilde { B }$ from a combination of the equations $\delta ( P ^ { - 1 } \dot { \Psi } \tilde { B } C \dot { K } P ) = \delta ( P ^ { - 1 } \dot { E } P ) \mathrm { a n d }$

$$
\widetilde { B } C \left[ \begin{array} { c } { \beta _ { p } } \\ { \beta _ { p - 1 } } \\ { \vdots } \\ { \beta _ { 1 } } \\ { 1 } \end{array} \right] = \Psi ^ { - 1 } \left[ \begin{array} { c c c c c } { \frac 1 { 1 ! } } & { \frac 1 { 2 ! } } & { \cdots } & { \frac 1 { p ! } } & { \frac 1 { ( p + 1 ) ! } - \epsilon _ { 0 } } \\ { 0 } & { \frac 1 { 1 ! } } & { \cdots } & { \frac 1 { ( p - 1 ) ! } } & { \frac 1 { ( p ) ! } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { \frac 1 { 1 ! } } & { \frac 1 { 2 ! } } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { \frac 1 { 1 ! } } \end{array} \right] \left[ \begin{array} { c } { \beta _ { p } } \\ { \beta _ { p - 1 } } \\ { \vdots } \\ { \beta _ { 1 } } \\ { 1 } \end{array} \right] .
$$

# 554 Methods with property $F ^ { \prime }$

There is a practical advantage for methods in which

$$
\begin{array} { r l } & { e _ { 1 } ^ { \top } B = e _ { p + 1 } ^ { \top } A , } \\ & { e _ { 2 } ^ { \top } B = e _ { p + 1 } ^ { \top } . } \end{array}
$$

A consequence of these assumptions is that $\beta _ { p } = 0$ .

For this subclass of IRKS methods, in addition to the existence of reliable approximations

$$
h F _ { i } = h y ^ { \prime } ( x _ { n - 1 } + h c _ { i } ) + O ( h ^ { p + 2 } ) , \qquad i = 1 , 2 , \ldots , p + 1 ,
$$

where $y ( x )$ is the trajectory such that $y ( x _ { n - 1 } ) = y _ { 1 } ^ { [ n - 1 ] }$ , the value of $y _ { 2 } ^ { \lfloor n - 1 \rfloor }$ provides an additional approximation

$$
h F _ { 0 } = h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) ,
$$

which can be used together with the $p + 1$ scaled derivative approximations given by (554a).

This information makes it possible to estimate the values of

$$
h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) \quad \mathrm { a n d } \quad h ^ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } ) ,
$$

which are used for local error estimation purposes both for the method currently in use as well as for a possible method of one higher order. Thus we can find methods which provide rational criteria for stepsize selection as well as for order selection.

Using terminology established in Butcher (2006), we will refer to methods with this special property as possessing property F. They are an extension of FSAL Runge–Kutta methods.

The derivation of methods based on the ideas in Subsections 553 and 554 is joint work with William Wright and is presented in Wright (2002) and Butcher and Wright (2003, 2003a).

# 555 Some non-stiff methods

The following method, for which $\begin{array} { r } { c = [ \frac { 1 } { 3 } , \frac { 2 } { 3 } , 1 ] ^ { \intercal } } \end{array}$ , has order 2:

$$
{ [ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] } =  [ \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } &   | \begin{array} { l l l } { 1 } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 1 8 } } } \\ { { \frac { 3 } { 1 0 } } } & { 0 } & { 0 } & { { | \begin{array} { l l l } { 1 } & { { \frac { 1 1 } { 3 0 } } } & { { \frac { 1 1 } { 9 0 } } } \\ { { \frac { 1 } { 5 } } } & { { \frac { 5 } { 1 2 } } } & { 0 } & { { | \begin{array} { l l l } { 1 } & { { \frac { 2 3 } { 6 0 } } } & { { \frac { 7 } { 4 5 } } } \\ { { \frac { 5 } { 3 } } } & { - { \frac { 2 9 } { 1 2 } } } & { { \frac { 4 } { 3 } } } & { { | \begin{array} { l l l } { 1 } & { { \frac { 5 } { 1 2 } } } & { { \frac { 2 } { 9 } } } \\ { - 2 } & { 4 } & { - 1 } & { 0 } & { 0 } \\ { 3 } & { - 9 } & { 6 } & { 0 } & { 0 } \end{array} | } } \end{array} ] } } } \end{array} ] } . \end{array} \end{array}
$$

This method was constructed by choosing $\beta _ { 1 } = - \textstyle { \frac { 1 } { 6 } }$ , $\beta _ { 2 } = \textstyle { \frac { 2 } { 9 } }$ , $\epsilon _ { 0 } = 0$ and requiring $\dot { V }$ to be strictly upper triangular. It could be interpreted as having an enhanced order of 3, but of course the stage order is only 2.

The next method, with $\begin{array} { r } { c = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } , \frac { 3 } { 4 } , 1 ] ^ { 1 } } \end{array}$ , has order 3:

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1 1 4</td><td></td><td>1 32</td><td>1 384 67</td></tr><tr><td>224 403 1851</td><td>0</td><td>0</td><td>0</td><td>1</td><td>45 806</td><td>45 3224</td><td>19344</td></tr><tr><td>2170</td><td>93 280</td><td>0</td><td>0</td><td>1</td><td>3777 8680 473</td><td>681 6944</td><td>297 138880</td></tr><tr><td>305 364</td><td>5 28</td><td>5 12</td><td>0</td><td>1</td><td>1092</td><td>81 728</td><td>17 17472</td></tr><tr><td>305 364</td><td>5 28</td><td>5 12</td><td>0</td><td>1</td><td>473 1092</td><td>81 728</td><td>17</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>17472 0</td></tr><tr><td>156</td><td>188</td><td>-20</td><td>8</td><td>0</td><td>52</td><td></td><td>1</td></tr><tr><td>7</td><td>7</td><td></td><td></td><td></td><td>7</td><td>1</td><td>28</td></tr><tr><td>512 7</td><td>584 7</td><td>160 3</td><td>16</td><td>0</td><td>568 21</td><td>4</td><td>1</td></tr></table>

For this method, possessing property F, $\beta _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ , $\beta _ { 2 } = \textstyle { \frac { 1 } { 1 6 } }$ , $\epsilon _ { 0 } = 0$ . The $3 \times 3$ matrix $\dot { V }$ is chosen so that $\delta ( P ^ { - 1 } \dot { V } P ) = 0$ , where

$$
P = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } \\ { 4 } & { 1 } & { 0 } \end{array} \right] } ~ .
$$

# 556 Some stiff methods

The first example, with $\textstyle \lambda = { \frac { 1 } { 4 } }$ and $\begin{array} { r } { c = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } , \frac { 3 } { 4 } , 1 ] ^ { \intercal } } \end{array}$ , has order 3:

This method was constructed with $\beta _ { 1 } = - \frac { 1 } { 4 }$ , $\beta _ { 2 } = \beta _ { 3 } = \textstyle { \frac { 1 } { 4 } }$ , $\begin{array} { r } { \epsilon _ { 0 } = \frac { 1 } { 2 5 6 } } \end{array}$ and $\delta ( \dot { V } ) = 0$ . The choice of $\epsilon _ { \mathrm { 0 } }$ was determined by requiring the stability function to be

$$
R ( z ) = \frac { 1 - \frac { 1 } { 8 } z ^ { 2 } - \frac { 1 } { 4 8 } z ^ { 3 } } { ( 1 - \frac { 1 } { 4 } z ) ^ { 4 } } ,
$$

which makes the method L-stable.

The second example has order 4 and an abscissa vector $\left[ \begin{array} { l l l l l } { 1 } & { \ \frac { 3 } { 4 } } & { \ \frac { 1 } { 4 } } & { \ \frac { 1 } { 2 } } & { \ 1 } \end{array} \right]$

$$
A = \left[ \begin{array} { r r r r r r } { \frac { 1 } { 4 } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - \frac { 5 1 3 } { 5 4 2 7 2 } } & { \frac { 1 } { 4 } } & { 0 } & { 0 } & { 0 } \\ { \frac { 3 7 0 6 1 1 9 } { 6 9 0 8 2 5 6 } } & { - \frac { 4 8 8 } { 3 8 1 9 } } & { \frac { 1 } { 4 } } & { 0 } & { 0 } \\ { \frac { 3 2 1 6 1 0 6 1 } { 1 9 7 5 4 9 2 3 2 } } & { - \frac { 1 1 1 8 1 4 } { 2 3 2 9 5 9 } } & { \frac { 1 3 4 } { 1 8 3 } } & { \frac { 1 } { 4 } } & { 0 } \\ { - \frac { 1 3 5 4 2 5 } { 2 9 4 8 4 9 6 } } & { - \frac { 6 4 1 } { 1 0 4 3 1 } } & { \frac { 7 3 } { 1 8 3 } } & { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } \end{array} \right] ,
$$

$$
V = \left[ \begin{array} { r r r r r r } { { 1 } } & { { - \frac { 3 6 7 3 1 3 } { 8 8 4 5 4 8 8 } } } & { { - \frac { 2 2 7 2 7 } { 2 9 4 8 4 9 6 } } } & { { \frac { 4 0 9 7 9 } { 5 8 9 6 9 9 2 } } } & { { \frac { 3 2 3 } { 6 2 0 7 3 6 } } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - \frac { 2 8 7 4 5 } { 1 0 4 3 1 } } } & { { - \frac { 1 9 3 7 } { 1 3 9 0 8 } } } & { { \frac { 1 1 7 } { 1 8 5 4 4 } } } & { { \frac { 6 5 } { 1 1 7 1 2 } } } \\ { { 0 } } & { { - \frac { 1 4 1 2 6 8 } { 1 0 4 3 1 } } } & { { - \frac { 2 0 5 0 } { 3 4 7 7 } } } & { { - \frac { 1 8 7 } { 2 3 1 8 } } } & { { \frac { 1 1 3 } { 1 4 6 4 } } } \\ { { 0 } } & { { - \frac { 2 1 6 4 1 6 } { 1 0 4 3 1 } } } & { { - \frac { 4 5 2 } { 3 4 7 7 } } } & { { - \frac { 4 9 1 } { 1 1 5 9 } } } & { { \frac { 1 6 1 } { 7 3 2 } } } \end{array} \right] .
$$

This property F method was constructed with $\beta _ { 1 } = \textstyle { \frac { 3 } { 4 } }$ , $\begin{array} { r } { \beta _ { 2 } = \frac { 3 } { 1 6 } } \end{array}$ , $\beta _ { 3 } = \textstyle { \frac { 1 } { 6 4 } }$ , $\begin{array} { r } { \epsilon _ { 0 } = \frac { 1 3 } { 1 5 3 6 0 } } \end{array}$ and $\delta ( P ^ { - 1 } \dot { V } P ) = 0$ , where

$$
P = \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 8 } & { 1 } & { 0 } & { 0 } \\ { 1 6 } & { 4 } & { 1 } & { 0 } \end{array} \right] .
$$

The method is L-stable with

$$
R ( z ) = { \frac { 1 - { \frac { 1 } { 4 } } z - { \frac { 1 } { 8 } } z ^ { 2 } + { \frac { 1 } { 9 6 } } z ^ { 3 } + { \frac { 7 } { 7 6 8 } } z ^ { 4 } } { ( 1 - { \frac { 1 } { 4 } } z ) ^ { 5 } } } .
$$

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

# 558 Scale and modify for error estimation

Consider first the constant stepsize case and assume that, after many steps, there is an accumulated error in each of the input components to step $n$ . If $y ( x )$ is the particular trajectory defined by $y ( x _ { n - 1 } ) = y _ { 1 } ^ { [ n - 1 ] }$ , then write the remaining input values as

$$
\begin{array}{c} y _ { i } ^ { [ n - 1 ] } = h ^ { i - 1 } y ^ { ( i - 1 ) } ( x _ { n - 1 } ) - \epsilon _ { i - 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) , ~  \\ { i = 2 , 3 , \ldots , p + 1 . ~ } \end{array}
$$

After a single step, the principal output will have acquired a truncation error so that its value becomes $y ( x _ { n } ) - \epsilon _ { 0 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } )$ , where

$$
\epsilon _ { 0 } = \frac { 1 } { ( p { + } 1 ) ! } - \frac { 1 } { p ! } \sum _ { j = 1 } ^ { s } b _ { 1 j } c _ { j } ^ { p } + \sum _ { j = 2 } ^ { r } v _ { 1 j } \epsilon _ { j - 1 } .
$$

Write $\epsilon$ as the vector with components $\epsilon _ { 1 }$ , $\epsilon _ { 2 }$ , $\cdot \cdot \cdot$ , $\epsilon _ { p }$ . The value of $\epsilon$ is determined by the fact that (558a) evolves after a single step to

$$
\begin{array}{c} y _ { i } ^ { [ n ] } = h ^ { i - 1 } y ^ { ( i - 1 ) } ( x _ { n } ) - \epsilon _ { i - 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) ,  \\ { i = 2 , 3 , \ldots , p + 1 . } \end{array}
$$

However,

$$
y _ { i } ^ { [ n ] } = h \sum _ { j = 1 } ^ { s } b _ { i j } y ^ { \prime } ( x _ { n - 1 } + h c _ { j } ) + \sum _ { j = 2 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } + O ( h ^ { p + 1 } ) , \quad i = 2 , 3 , \ldots , p + 1 ,
$$

so that substitution of (558a) and (558c) into (558d), followed by Taylor expansion about $x _ { n - 1 }$ , gives the result

$$
\begin{array} { r } { \boldsymbol { \epsilon } = \left[ \begin{array} { c } { \frac { 1 } { p ! } } \\ { \frac { 1 } { ( p - 1 ) ! } } \\ { \vdots } \\ { \frac { 1 } { 1 ! } } \end{array} \right] - \frac { 1 } { p ! } \dot { \boldsymbol { B } } + \dot { \boldsymbol { V } } \boldsymbol { \epsilon } , } \end{array}
$$

where $\dot { B }$ is the matrix $B$ with its first row deleted. It was shown in Wright (2003) that

$$
\epsilon _ { i } = \beta _ { p + 1 - i } , \quad i = 1 , 2 , \ldots , p .
$$

Without a modification to the simple scaling process, the constancy of $\epsilon$ from step to step will be destroyed, and we consider how to correct for this. There are several reasons for wanting this correction. First, the reliability of (558b), as providing an estimate of the local error in a step, depends on values of $\epsilon$ in the input to the current step. Secondly, asymptotically correct approximations to $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )$ are needed for stepsize control purposes and, if these approximations are based on values of both $h F$ and $y ^ { \lfloor n - 1 \rfloor }$ , then these will also depend on $\epsilon$ in the input to the step. Finally, reliable estimates of $h ^ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } )$ are needed as a basis for dynamically deciding when an order increase is appropriate. It was shown in Butcher and Podhaisky (2006) that, at least for methods possessing property F, estimation of both $h ^ { p + 1 } y ^ { ( p + 1 ) }$ and $h ^ { p + 2 } y ^ { ( p + 2 ) }$ is possible, as long as constant $\epsilon$ values are maintained.

In Subsection 557 we considered the method (555b) from the point of view of variable stepsize stability. To further adjust to maintain the integrity of $\epsilon$ in a variable $h$ regime, it is only necessary to add to the scaled and modified outputs $y _ { 3 } ^ { \lfloor n \rfloor }$ and $y _ { 4 } ^ { [ n ] }$ , appropriate multiples of $- h F _ { 1 } + 3 h F _ { 2 } - 3 h F _ { 3 } + h F _ { 4 }$ .

# Exercises 55

55.1 Show that the method given by (555a) has order 2, and that the stages are also accurate to this order.   
55.2 Find the stability matrix of the method (555a), and show that it has two zero eigenvalues.   
55.3 Show that the method given by (556a) has order 3, and that the stages are also accurate to this order.   
55.4 Find the stability matrix of the method (556a), and show that it has two zero eigenvalues.   
55.5 Show that (556a) is L-stable.   
55.6 Show that the $( i , j )$ element of $\Psi ^ { - 1 }$ is equal to the coefficient of $w ^ { i - 1 } z ^ { j - 1 }$ in the power series expansion about $z = 0$ of $\alpha ( z ) / ( 1 - ( \lambda + w ) z )$ .

# References

Alexander R. (1977) Diagonally implicit Runge–Kutta methods for stiff ODEs. SIAM J. Numer. Anal., 14, 1006–1021.   
Axelsson O. (1969) A class of A-stable methods. BIT, 9, 185–199.   
Axelsson O. (1972) A note on class of strongly A-stable methods. BIT, 12, 1–4.   
Barton D., Willers I. M. and Zahar R. V. M. (1971) The automatic solution of systems of ordinary differential equations by the method of Taylor series. Comput. J., 14, 243–248.   
Bashforth F. and Adams J. C. (1883) An Attempt to Test the Theories of Capillary Action by Comparing the Theoretical and Measured Forms of Drops of Fluid, with an Explanation of the Method of Integration Employed in Constructing the Tables which Give the Theoretical Forms of Such Drops. Cambridge University Press, Cambridge.   
Brenan K. E., Campbell S. L. and Petzold L. R. (1989) Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations. North-Holland, New York.   
Brouder C. (2000) Runge–Kutta methods and renormalization. Eur. Phys. J. C., 12, 521–534.   
Burrage K. (1978) A special family of Runge–Kutta methods for solving stiff differential equations. BIT, 18, 22–41.   
Burrage K. and Butcher J. C. (1980) Non-linear stability of a general class of differential equation methods. BIT, 20, 185–203.   
Burrage K., Butcher J. C. and Chipman F. H. (1980) An implementation of singlyimplicit Runge–Kutta methods. BIT, 20, 326–340.   
Butcher J. C. (1963) Coefficients for the study of Runge–Kutta integration processes. J. Austral. Math. Soc., 3, 185–201.   
Butcher J. C. (1963a) On the integration processes of A. Huˇta. J. Austral. Math. Soc., 3, 202–206.   
Butcher J. C. (1965) A modified multistep method for the numerical integration of ordinary differential equations. J. Assoc. Comput. Mach., 12, 124–135.   
Butcher J. C. (1965a) On the attainable order of Runge–Kutta methods. Math. Comp., 19, 408–417.   
Butcher J. C. (1966) On the convergence of numerical solutions to ordinary differential equations. Math. Comp., 20, 1–10.   
Butcher J. C. (1972) An algebraic theory of integration methods. Math. Comp., 26, 79–106.   
Butcher J. C. (1975) A stability property of implicit Runge–Kutta methods. BIT, 15, 358–361.   
Butcher J. C. (1977) On A-stable implicit Runge–Kutta methods. BIT, 17, 375–378. Comput. Mach., 26, 731–738.   
Butcher J. C. (1985) The nonexistence of ten-stage eighth order explicit Runge– Kutta methods. BIT, 25, 521–540.   
Butcher J. C. (1987) The Numerical Analysis of Ordinary Differential Equations, Runge–Kutta and General Linear Methods. John Wiley & Sons Ltd, Chichester.   
Butcher J. C. (1987a) The equivalence of algebraic stability and AN-stability. BIT, 27, 510–533.   
Butcher J. C. (1995) On fifth order Runge–Kutta methods. BIT, 35, 202–209.   
Butcher J. C. (1995a) An introduction to DIMSIMs. Comput. Appl. Math., 14, 59– 72.   
Butcher J. C. (1997) An introduction to ‘Almost Runge–Kutta’ methods. Appl. Numer. Math., 24, 331–342.   
Butcher J. C. (1998) ARK methods up to order five. Numer. Algorithms, 17, 193– 221.   
Butcher J. C. (2001) General linear methods for stiff differential equations. BIT, 41, 240–264.   
Butcher J. C. (2002) The A-stability of methods with Pad´e and generalized Pad´e stability functions. Numer. Algorithms, 31, 47–58.   
Butcher J. C. (2006) General linear methods. Acta Numerica, 15, 157–256.   
Butcher J. C. (2008) Order and stability of generalized Pad´e approximations. Appl. Numer. Math. (to appear).   
Butcher J. C. and Cash J. R. (1990) Towards efficient Runge–Kutta methods for stiff systems. SIAM J. Numer. Anal., 27, 753–761.   
Butcher J. C. and Chartier P. (1997) A generalization of singly-implicit Runge– Kutta methods. Appl. Numer. Math., 24, 343–350.   
Butcher J. C. and Chipman F. H. (1992) Generalized Pad´e approximations to the exponential function. BIT, 32, 118–130.   
Butcher J. C. and Hill A. T. (2006) Linear multistep methods as irreducible general linear methods. BIT, 46, 5–19.   
Butcher J. C. and Jackiewicz Z. (1996) Construction of diagonally implicit general linear methods of type 1 and 2 for ordinary differential equations. Appl. Numer. Math., 21, 385–415.   
Butcher J. C. and Jackiewicz Z. (1998) Construction of high order diagonally implicit multistage integration methods for ordinary differential equations. Appl. Numer. Math., 27, 1–12.   
Butcher J. C. and Jackiewicz Z. (2003) A new approach to error estimation for general linear methods. Numer. Math., 95, 487–502.   
Butcher J. C. and Moir N. (2003) Experiments with a new fifth order method. Numer. Algorithms, 33, 137–151 .   
Butcher J. C. and Podhaisky H. (2006) On error estimation in general linear methods for stiff ODEs. Appl. Numer. Math., 56, 345–357.   
Butcher J. C. and Rattenbury N. (2005) ARK methods for stiff problems. Appl. Numer. Math., 53, 165–181 .   
Butcher J. C. and Wright W. M. (2003) A transformation relating explicit and diagonally-implicit general linear methods. Appl. Numer. Math., 44, 313–327.   
Butcher J. C. and Wright W. M. (2003a) The construction of practical general linear methods. BIT, 43, 695–721.   
Butcher J. C. and Wright W. M. (2006) Applications of doubly companion matrices. Appl. Numer. Math., 56, 358–373. points. J. Assoc. Comput. Mach., 13, 114–123.   
Cooper G. J. (1987) Stability of Runge-Kutta methods for trajectory problems. IMA J. Numer. Anal., 7, 1–13.   
Cooper G. J. and Verner J. H. (1972) Some explicit Runge–Kutta methods of high order. SIAM J. Numer. Anal., 9, 389–405.   
Curtis A. R. (1970) An eighth order Runge–Kutta process with eleven function evaluations per step. Numer. Math., 16, 268–277.   
Curtis A. R. (1975) High-order explicit Runge–Kutta formulae, their uses and limitations. J. Inst. Math. Appl., 16, 35–55.   
Curtiss C. F. and Hirschfelder J. O. (1952) Integration of stiff equations. Proc. Nat. Acad. Sci. U.S.A., 38, 235–243.   
Dahlquist G. (1956) Convergence and stability in the numerical integration of ordinary differential equations. Math. Scand., 4, 33–53.   
Dahlquist G. (1963) A special stability problem for linear multistep methods. BIT, 3, 27–43.   
Dahlquist G. (1976) Error analysis for a class of methods for stiff non–linear initial value problems. In G. A. Watson (ed.) Numerical Analysis, Lecture Notes in Math. 506, Springer, Berlin, 60–72.   
Dahlquist G. (1978) G-stability is equivalent to A-stability. BIT, 18, 384–401.   
Dahlquist G. (1983) On one-leg multistep methods. SIAM J. Numer. Anal., 20, 1130–1138.   
Dahlquist G. and Jeltsch R. (1979) Generalized disks of contractivity for explicit and implicit Runge–Kutta methods, Technical Report TRITA NA–7906, Dept. of Numer. Anal. and Computing Sci., Roy. Inst. Tech.   
Daniel J. W. and Moore R. E. (1970) Computation and Theory in Ordinary Differential Equations. W. H. Freeman, San Francisco.   
Davis P. J. and Rabinowitz P. (1984) Methods of Numerical Integration. Academic Press, New York.   
Donelson J. and Hansen E. (1971) Cyclic composite multistep predictor–corrector methods. SIAM J. Numer. Anal., 8, 137–157.   
Dormand J. R. and Prince P. J. (1980) A family of embedded Runge–Kutta formulae. J. Comput Appl, Math., 6, 19–26.   
Ehle B. L. (1969) On Pad´e approximations to the exponential function and $A$ -stable methods for the numerical solution of initial value problems, Research Rep. CSRR 2010, Dept. of AACS, University of Waterloo, Ontario, Canada.   
Ehle B. L. (1973) A-stable methods and Pad´e approximations to the exponential. SIAM J. Math. Anal., 4, 671–680.   
Ehle B. L. and Picel Z. (1975) Two parameter, arbitrary order, exponential approximations for stiff equations. Math. Comp., 29, 501–511.   
Euler L. (1913) De integratione aequationum differentialium per approximationem. In Opera Omnia, 1st series, Vol. 11, Institutiones Calculi Integralis, Teubner, Leipzig and Berlin, 424–434.   
Fehlberg E. (1968) Classical fifth, sixth, seventh and eighth order Runge–Kutta formulas with stepsize control, NASA TR R-287.   
Fehlberg E. (1969) Klassische Runge–Kutta-Formeln f¨unfter und siebenter Ordnung mit Schrittweiten-Kontrolle. Computing, 4, 93–106.   
Gear C. W. (1965) Hybrid methods for initial value problems in ordinary differential equations. SIAM J. Numer. Anal., 2, 69–86. Math. Comp., 21, 146–156.   
Gear C. W. (1971) Numerical Initial Value Problems in Ordinary Differential Equations. Prentice Hall, Englewood Cliffs, NJ.   
Gear C. W. (1971a) Algorithm 407, DIFSUB for solution of ordinary differential equations. Comm. ACM, 14, 185–190.   
Gear C. W. (1980) Runge–Kutta starters for multistep methods. ACM Trans. Math. Software, 6, 263–279.   
Gibbons A. (1960) A program for the automatic integration of differential equations using the method of Taylor series. Comput. J., 3, 108–111.   
Gill S. (1951) A process for the step-by-step integration of differential equations in an automatic computing machine. Proc. Cambridge Philos. Soc., 47, 96–108.   
Gragg W. B. and Stetter H. J. (1964) Generalized multistep predictor–corrector methods. J. Assoc. Comput. Mach., 11, 188–209.   
Gustafsson K. (1991) Control theoretic techniques for stepsize selection in explicit Runge–Kutta methods. ACM Trans. Math. Software, 17, 533–544.   
Gustafsson K., Lundh M. and S¨oderlind G. (1988) A PI stepsize control for the numerical solution of ordinary differential equations. BIT, 28, 270–287.   
Hairer E. (1978) A Runge–Kutta method of order 10. J. Inst. Math. Appl., 21, 47–59.   
Hairer E. and Leone P. (2000) Some properties of symplectic Runge–Kutta methods. NZ J. Math., 29, 169–175.   
Hairer E., Lubich C. and Roche M. (1989) The Numerical Solution of Differential-Algebraic Systems by Runge–Kutta Methods, Lecture Notes in Math. 1409. Springer, Berlin.   
Hairer E., Lubich C. and Wanner G. (2006) Geometric Numerical Integration: Structure-preserving Algorithms for Ordinary Differential Equations. Springer, Berlin.   
Hairer E., Nørsett S. P. and Wanner G. (1993) Solving Ordinary Differential Equations I: Nonstiff Problems. Springer, Berlin.   
Hairer E. and Wanner G. (1974) On the Butcher group and general multi-value methods. Computing, 13, 1–15.   
Hairer E. and Wanner G. (1981) Algebraically stable and implementable Runge– Kutta methods of high order. SIAM J. Numer. Anal., 18, 1098–1108.   
Hairer E. and Wanner G. (1982) Characterization of non-linearly stable implicit Runge–Kutta methods. In J. Hinze (ed.) Numerical Integration of Differential Equations and Large Linear Systems, Lecture Notes in Math. 968, Springer, Berlin, 207–219.   
Hairer E. and Wanner G. (1996) Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems. Springer, Berlin.   
Henrici P. (1962) Discrete Variable Methods in Ordinary Differential Equations. John Wiley & Sons Inc, New York.   
Henrici P. (1963) Error Propagation for Difference Methods. John Wiley & Sons Inc, New York.   
Heun K. (1900) Neue Methoden zur approximativen Integration der Differentialgleichungen einer unabh¨angigen Ver¨anderlichen. Z. Math. Phys., 45, 23–38.   
Higham N. J. (1993) The accuracy of floating point summation. SIAM J. Sci. Comput., 14, 783–799.   
Hundsdorfer W. H. and Steininger B. I. (1991) Convergence of linear multistep and one-leg methods for stiff nonlinear initial value problems. BIT, 31, 124–143. la r´esolut on num´erique des ´equations diff ielles du premier cta Fac. Nat. Univ. Comenian. Math., 1, 201–224.   
Huˇta A. (1957) Contribution \`a la formule de sixi\`eme ordre dans la m´ethode de Runge–Kutta–Nystr¨om. Acta Fac. Nat. Univ. Comenian. Math., 2, 21–24.   
Iserles A., Munthe-Kaas H. Z., Nørsett S. P. and Zanna A. (2000) Lie-group methods. Acta Numer., 9, 215–365.   
Iserles A. and Nørsett S. P. (1991) Order Stars. Chapman & Hall, London.   
Kahan W. (1965) Further remarks on reducing truncation errors. Comm. ACM, 8, 40.   
Kirchgraber U. (1986) Multistep methods are essentially one-step methods. Numer. Math., 48, 85–90.   
Kutta W. (1901) Beitrag zur n¨aherungsweisen Integration totaler Differentialgleichungen. Z. Math. Phys., 46, 435–453.   
Lambert J. D. (1991) Numerical Methods for Ordinary Differential Systems: the Initial Value Problem. John Wiley & Sons Ltd, Chichester.   
Lasagni F. M. (1988) Canonical Runge–Kutta methods. Z. Angew. Math. Phys., 39, 952–953.   
L´opez-Marcos M. A., Sanz-Serna J. M. and Skeel R. D. (1996) Cheap enhancement of symplectic integrators. In D. F. Griffiths and G. A. Watson (eds.) Numerical Analysis, Pitman Res. Notes Math. Ser., 344, Longman, Harlow, 107–122.   
Lotka A. J. (1925) Elements of Physical Biology. Williams and Wilkins, Baltimore, Md.   
Merson R. H. (1957) An operational method for the study of integration processes. In Proc. Symp. Data Processing, Weapons Research Establishment, Salisbury, S. Australia.   
Milne W. E. (1926) Numerical integration of ordinary differential equations. Amer. Math. Monthly, 33, 455–460.   
Milne W. E. (1953) Numerical Solution of Differential Equations. John Wiley & Sons Inc, New York.   
Møller O. (1965) Quasi double-precision in floating point addition. BIT, 5, 37–50.   
Møller O. (1965a) Note on quasi double-precision. BIT, 5, 251–255.   
Moore R. E. (1964) The automatic analysis and control of error in digital computation based on the use of interval numbers. In L. B. Rall (ed.) Error in Digital Computation, vol. 1. John Wiley & Sons Inc, New York, 61–130.   
Moulton F. R. (1926) New Methods in Exterior Ballistics. University of Chicago Press.   
Nordsieck A. (1962) On numerical integration of ordinary differential equations. Math. Comp., 16, 22–49.   
Nørsett S. P. (1974) Semi-explicit Runge–Kutta methods, Report No. 6/74, Dept. of Math., Univ. of Trondheim.   
Nystr¨om E. J. (1925) Uber die numerische Integration von Differentialgleichungen. ¨ Acta Soc. Sci. Fennicae, 50 (13), 55pp.   
Obreshkov N. (1940) Neue Quadraturformeln. Abh. der Preuß. Akad. der Wiss., Math.-naturwiss. Klasse, 4, .   
Prothero A. and Robinson A. (1974) On the stability and accuracy of one-step methods for solving stiff systems of ordinary differential equations. Math. Comp., 28, 145–162.   
Rattenbury N. (2005) Almost Runge–Kutta methods for stiff and non-stiff problems, PhD thesis, The University of Auckland.   
Richardson L. F. (1927) The deferred approach to the limit. Philos. Trans. Roy. Soc. London Ser. A., 226, 299–361.   
Robertson H. H. (1966) The solution of a set of reaction rate equations. In J. Walsh (ed.) Numerical Analysis: An Introduction, Academic Press, London, 178–182.   
Romberg W. (1955) Vereinfachte numerische Integration. Norske Vid. Selsk. Forh., Trondheim, 28, 30–36.   
Rosenbrock H. H. (1963) Some general implicit processes for the numerical solution of differential equations. Comput. J., 5, 329–330.   
Runge C. (1895) Uber die numerische Aufl¨ ¨ osung von Differentialgleichungen. Math. Ann., 46, 167–178.   
Sanz-Serna J. M. (1988) Runge–Kutta schemes for Hamiltonian systems. BIT, 39, 877–883.   
Sanz-Serna J. M. and Calvo M. P. (1994) Numerical Hamiltonian Problems. Chapman & Hall, London.   
Scherer R. (1977) A note on Radau and Lobatto formulae for ODEs. BIT, 17, 235– 238.   
Scherer R. (1978) Spiegelung von Stabilit¨atsbereichen. In R. Bulirsch, R. D. Grigorieff and J. Schr¨oder (eds.) Numerical Treatment of Differential Equations, Lecture Notes in Math. 631, Springer, Berlin, 147–152.   
Singh A. D. (1999) Parallel diagonally implicit multistage integration methods for stiff ordinary differential equations, PhD thesis, The University of Auckland.   
S¨oderlind G. (2002) Automatic control and adaptive time-stepping. Numer. Algorithms, 31, 281–310.   
Stoffer D. (1993) General linear methods: connection to one step methods and invariant curves. Numer. Math., 64, 395–408.   
Suris Yu. B. (1988) Preservation of symplectic structure in the numerical solution of Hamiltonian systems (in Russian). Akad. Nauk SSSR, Inst. Prikl. Mat., Moscow,, 232, 148–160, 238–239.   
Van der Pol B. (1926) On relaxation-oscillations. Philos. Mag. Ser. 7, 2, 978–992.   
Verner J. H. (1978) Explicit Runge–Kutta methods with estimates of the local truncation error. SIAM J. Numer. Anal., 15, 772–790.   
Vitasek E. (1969) The numerical stability in solution of differential equations. In J.L. Morris (ed.) Conf. on Numerical Solution of Differential Equations, Lecture Notes in Math. 109, Springer, Berlin, 87–111.   
Volterra V. (1926) Variazioni e fluttuazioni del numero d’individui in specie animali conviventi. Memorie della R. Accad. Naz. dei Lincei, (Ser. VI), 2, 31–131.   
Wanner G., Hairer E. and Nørsett S. P. (1978) Order stars and stability theorems. BIT, 18, 475–489.   
Wantanabe D. S. and Sheikh Q. M. (1984) One-leg formulas for stiff ordinary differential equations. SIAM J. Sci. Statist. Comput., 2, 489–496.   
Watts H. A. and Shampine L. F. (1972) A-stable block implicit one-step methods. BIT, 12, 252–266.   
Wright K. (1970) Some relationships between implicit Runge–Kutta, collocation and Lanczos $\tau$ methods, and their stability properties. BIT, 10, 217–227.   
Wright W. M. (2002) Explicit general linear methods with inherent Runge–Kutta stability. Numer. Algorithms, 31, 381–399.   
Wright W. M. (2003) General linear methods with inherent Runge–Kutta stability, PhD thesis, The University of Auckland.

# Index

A-stability, 76, 230, 238, 261, 270, 272,   
343, 353, 356, 365, 398, 421   
$\mathrm { A } ( \alpha )$ -stability, 230   
Adams, xiv, 105, 375   
adjoint methods, 220   
Alexander, 261   
algebraic analysis of order, 413   
algebraic stability, 250, 252   
AN-stability, 245, 252   
angular momentum, 5   
annihilation conditions, 129, 427, 431   
arithmetic-geometric mean, 43   
asymptotic error formula, 72   
Axelsson, 240

B-series, 280   
B-stability, 250   
Barton, 115   
Bashforth, xiv, 105, 375   
BN-stability, 250, 252   
boundary locus, 344, 346   
Brenan, xv   
Brouder, 280   
Burrage, 124, 258, 266, 373   
Butcher, 93, 122, 124, 163, 188, 192, 198, 240, 241, 258, 261, 266, 271, 280, 301, 358, 373, 380, 382, 402, 419, 420, 426, 433, 434, 436, 438, 445   
Butcher–Chipman conjecture, 402   
Byrne, 122, 380   
Calvo, xv   
Campbell, xv   
Cash, 271   
Cauchy–Schwarz inequality, 58   
Chartier, 436   
Chipman, 266, 402   
Christoffel–Darboux formula, 269   
coefficient tableau, 94

companion matrix, 25   
compensated addition, 82   
compensated summation, 83   
conjugacy, 302   
consistency, 107, 109, 317, 320–322, 324,   
326, 385, 389, 390, 396   
contraction mapping principle, 22   
convergence, 69, 107, 109, 317, 319, 322,   
324, 326, 385, 387, 388, 390, 396   
Cooper, 196   
covariance, 108, 386   
Curtis, 196   
Curtiss, 105

Dahlquist, 105, 247, 248, 320, 353, 358, 360, 361, 364, 365, 379   
Dahlquist barrier, 353, 355, 380   
Dahlquist second barrier, 358   
Daniel, 401   
Daniel–Moore barrier, 401   
DASSL, xv   
Davis, 20   
delay differential equation, 31 neutral, 32   
density of tree, 140   
derivative weight, 156   
difference equation, 38 Fibonacci, 40 linear, 38, 44   
differential equation autonomous, 2, 150 chemical kinetics, 14 dissipative, 8 Euler (rigid body), 20 Hamiltonian, xv, 34 harmonic oscillator, 16 initial value problem, 2 Kepler, 4, 87, 127 linear, 24 Lotka–Volterra, 18

G-stability, 343, 360, 361, 365   
Gaussian quadrature, 189, 215   
Gear, xiv, 122, 318, 368, 370, 380   
generalized order conditions, 186   
generalized Pad´e approximation, 400   
Gibbons, 115   
Gill, 82, 93, 180   
Gill–Møller algorithm, 82, 83   
global truncation error, 395, 412   
Gragg, 122, 380   
graph, 137   
Gustafsson, 130, 312, 313

many-body, 28 method of lines, 7 mildly stiff, 60 Prothero and Robinson, 262 restricted three–body, 28 Robertson, 15 simple pendulum, 10 stiff, 26, 64, 74, 214, 245, 308, 313, 343, 353 Van der Pol, 16 differential index, 13 differential-algebraic equation, xiv, 10, 36 differentiation, 146 DIFSUB, xiv Dirichlet conditions, 7 DJ-reducibility, 247 Donelson, 380 Dormand, 198, 211 doubly companion matrix, 436, 442

Hairer, xiv, xv, 77, 161, 188, 196, 220,   
240, 241, 258, 267, 280, 281, 356,   
358   
Hamiltonian, 5   
Hansen, 380   
Henrici, 81, 105   
Heun, 93   
hidden constraint, 37   
Higham, 82   
Hirschfelder, 105   
homomorphism, 290   
Hundsdorfer, 361   
Huˇta, 93, 163, 192, 194   
E-polynomial, 231, 270   
eccentricity, 6   
effective order, 273, 302, 365, 436   
efficient extrapolation, 299   
Ehle, 240, 245   
Ehle barrier, 243, 244   
Ehle conjecture, 240   
elementary differential, 150, 151, 156   
elementary differentials   
independence of, 160   
elementary weight, 155, 156   
independence, 163   
elliptic integral, 43   
equivalence, 281   
error constant, 335   
error estimation, 79   
error estimator, 198   
error growth, 335   
error per step, 311   
error per unit step, 311   
Euler, 51   
existence and uniqueness, 22   
ideal, 300   
implementation, 128, 259   
index reduction, 13   
inherent Runge–Kutta stability, 438   
internal order, 182   
internal weights, 157   
interpolation, 131   
invariant, 35   
Iserles, 241

Jackiewicz, 419, 426   
Jacobian, xiv   
Jacobian matrix, 27, 260, 271, 313   
Jeltsch, 247, 248

Kahan, 82   
Kirchgraber, 338   
Kronecker product, 374   
Kutta, 93, 178, 192   
Fehlberg, 198, 208   
Feng, xv   
finger, 78, 241   
forest, 287   
product, 288   
FSAL property, 211, 376   
L-stability, 238, 261, 262, 270, 398   
labelled trees, 144   
Laguerre polynomial, 267   
Laguerre polynomials, 269   
Lambert, J. D., 320   
Lambert, R. J., 122, 380   
Lasagni, 276   
Legendre polynomials, 215   
Leone, 258   
limit cycles, 16   
linear stability, 397   
linear stability function, 246   
Lipschitz condition, 22, 65   
Lobatto IIIA, 376   
Lobatto quadrature, 196, 222   
local extrapolation, 198   
local truncation error, 324, 393, 412   
L´opez-Marcos, 280   
Lotka, 18   
Lubich, xv, 220   
Lundh, 130, 312

matrix convergent, 46 Jordan, 47 power-bounded, 46 stable, 46   
Merson, 93, 198, 201   
method Adams, 105 Adams–Bashforth, xiv, 105, 109, 111, 318, 331, 346, 378 Adams–Moulton, xiv, 91, 105, 109, 111, 330, 378 Almost Runge–Kutta (ARK), 128, 383, 426 stiff, 434 backward difference, 105, 330, 332 collocation, 252 cyclic composite, 380 DESIRE, 273, 275 diagonally implicit, 261 DIMSIM, xiv, 383, 420, 421 types, 421 DIRK, 261, 421 Dormand and Prince, 198, 211 Euler, xiii, 51, 65, 78 convergence, 68 order, 69 Fehlberg, 198, 208 Gauss, 257, 265 general linear, 90, 124 order, 280   
generalized linear multistep, 124   
Gill, 180   
higher derivative, 88, 119   
Huˇta, 163, 192   
hybrid, 122, 380   
implicit, 91   
implicit Euler, 63, 64   
implicit Runge–Kutta, 102   
IRK stable, 442   
Kutta, 192   
leapfrog, 339   
linear multistep, xiv, 87, 105, 107, 377 implementation, 366 order of, 329   
Lobatto, 257   
Lobatto IIIA, 91   
Lobatto IIIC, 265   
Merson, 198, 201   
mid-point rule, 94   
modified multistep, 122   
multiderivative, 90   
multistage, 88, 373   
multistep, 88   
multivalue, 88, 373   
Nordsieck, 368, 371   
Nystr¨om, 105   
Obreshkov, 90, 401   
one-leg, 360, 361, 364, 379   
PEC, 111   
PECE, 111, 378   
PECEC, 111   
PECECE, 111   
predictor–corrector, 105   
predictor-corrector, xiv, 92, 109, 349, 378   
pseudo Runge–Kutta, 122, 123, 380, 382   
Radau IA, 257, 265   
Radau IIA, 257, 265   
reflected, 219   
Rosenbrock, 90, 120   
Runge–Kutta, xiii, xiv, 87, 93, 112, 319, 376 algebraic property, 280 effective order, 303 embedded, 202 equivalence class, 281, 285 Gauss, 238, 252 generalized, 292, 416 group, 284

identity, 286 implementation, 308 implicit, 99, 213, 259 inverse, 286 irreducible, 282 Lobatto IIIC, 238 order, 162 Radau IA, 238 Radau IIA, 238, 252 symplectic, 275 Runge–Kutta (explicit), 170 high order, 195 order 4, 175 order 5, 190 order 6, 192 SDIRK, 261, 421 singly implicit, 266, 268, 270 starting, 112, 318 Taylor series, 89, 114 underlying one-step, 337, 338, 417 Verner, 198, 210 weakly stable, 339 Milne, 105, 112, 339 Milne device, 111 Moir, 433 Moore, 115, 401 Moulton, xiv, 105 Munthe-Kaas, xv Møller, 82

order of tree, 139   
order star, 77, 240, 241   
order stars, 356   
order web, 243   
P-equivalence, 281   
Pad´e approximation, 232, 244   
Pad´e approximation, 120   
periodic orbit, 17   
perturbing method, 302   
Petzold, xv   
$\Phi$ -equivalence, 281   
PI control, 312   
Picard iteration, 154   
Picel, 240   
powers of matrix, 46   
preconsistency, 108, 320, 385   
Prince, 198, 211   
principal moments of inertia, 21   
problem   
discontinuous, 133   
Prothero, 262

quotient group, 301

Neumann conditions, 7   
Newton, 214   
Newton iteration, 214, 308, 313   
Newton method, 42, 91   
non-linear stability, 248   
Nordsieck, 368, 375   
Nordsieck vector, 440   
normal subgroup, 301   
Nørsett, xv, 77, 161, 240, 241, 261, 267,   
356, 358   
Nystr¨om, 93, 105, 192   
Rabinowitz, 20   
Radau code, xiv   
Radau quadrature, 222   
Rattenbury, 433, 434   
reduced method, 247   
relaxation factor, 314   
Richardson, 198   
Riemann surfaces, 356   
RK stability, 420, 423, 424, 432   
Robertson, 15   
Robinson, 262   
Roche, xv   
Romberg, 199   
rooted tree, 96, 137   
Rosenbrock, 90, 120   
round-off error, 80   
rounding error, 80   
Runge, 93   
Runge–Kutta, xiv   
Runge–Kutta group, 287   
Obreshkov, 90   
one-sided Lipschitz condition, 24, 26   
optimal stepsize sequences, 198, 308   
order, 329, 410   
order arrows, 79, 242, 243, 358   
order barrier, 187, 352   
order conditions, 95, 162   
scalar problems, 162   
S-stability, 230   
safety factor, 310   
Sanz-Serna, xv, 276, 280   
Scherer, 220   
Schur criterion, 345, 349   
Shampine, 240   
Sheikh, 361   
similarity transformation, 316   
simplifying assumption, 171   
Singh, 426   
Skeel, 280   
S¨oderlind, 130, 312, 313   
stability, 107, 109, 317, 320, 322, 324,   
326, 342, 385, 386, 388, 390, 396   
stability function, 76, 100, 398, 424   
stability matrix, 397, 424, 432   
stability order, 398, 399   
stability region, 74, 75, 100, 344, 398   
explicit Runge–Kutta, 101   
implicit Runge–Kutta, 102   
stage order, 262   
starting method   
degenerate, 411   
non-degenerate, 411   
Steiniger, 361   
stepsize control, 58, 112   
stepsize controller, 310   
Stetter, 122, 380   
Stoffer, 338, 418   
subgroup, 300   
super-convergence, 19   
superposition principle, 24   
Suris, 276   
symmetry, 148   
symmetry of tree, 140   
symplectic behaviour, 7

Taylor expansion, 153, 159   
Taylor’s theorem, 148   
tolerance, 308   
transformation of methods, 375   
tree, 137   
truncation error, 333 estimation, 390, 419 global, 66, 166, 168, 265, 390 local, 60, 66, 72, 73, 79, 112, 165, 168, 198, 309, 336, 428 built-in estimate, 201 estimate, 91

$V$ transformation, 254, 258   
Van der Pol, 16   
variable order, 308, 318   
variable stepsize, 130, 340, 368, 371, 419   
Verner, 196, 198, 210   
Vitasek, 82   
Volterra, 18   
W transformation, 254   
Wanner, xiv, xv, 77, 161, 220, 240, 241,   
258, 267, 280, 281, 356, 358   
Watanabe, 361   
Watts, 240   
weak stability, 339   
Willers, 115   
Wright, K., 240   
Wright, W. M., 436, 438, 440, 445, 450   
Wronskian, 35

Zahar, 115   
Zanna, xv   
zero spectral radius, 440   
zero-stability, 320
