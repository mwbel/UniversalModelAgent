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
