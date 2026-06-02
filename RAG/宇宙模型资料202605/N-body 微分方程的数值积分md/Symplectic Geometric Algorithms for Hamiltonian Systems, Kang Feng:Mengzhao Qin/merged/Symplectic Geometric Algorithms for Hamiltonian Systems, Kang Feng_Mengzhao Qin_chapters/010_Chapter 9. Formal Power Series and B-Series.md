# Chapter 9. Formal Power Series and B-Series

We study vector fields, their associated dynamical systems and phase flows together with their algorithmic approximations in $\mathbf { R } ^ { N }$ from the formal power series approach [Fen93a,Fen92] .

# 9.1 Notation

Our considerations will be local in both space and time, all related objects are $\mathbf { C } ^ { \infty }$ smooth. We use coordinate description and matrix notation, the coordinate vectors in $\mathbf { R } ^ { N }$ and vector functions $a : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ are denoted by column matrices. The identity vector function $1 _ { N }$ is given by $1 _ { N } ( x ) \ = \ x$ . For vector function $a = ( a _ { 1 } , \cdots , a _ { N } ) ^ { \mathrm { T } } : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ ,

$$
a \mathrm { * } : = \left( { \frac { \partial a _ { i } } { \partial x _ { j } } } \right) = \mathrm { J a c o b i a n \ m a t r i x } \ a ,
$$

the association $a \to a ^ { * }$ is linear, $a ^ { * }$ operates on scalar functions $\phi : \mathbf { R } ^ { N } \to \mathbf { R }$

$$
a ^ { * } \phi = \sum a _ { i } \frac { \partial \phi } { \partial x _ { i } } ,
$$

and on vector functions $b : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ as

$$
a ^ { * } b = a ^ { * } ( b _ { 1 } , \cdot \cdot \cdot , b _ { N } ) ^ { \mathrm { T } } = ( a ^ { * } b _ { 1 } , \cdot \cdot \cdot , a ^ { * } b _ { N } ) ^ { \mathrm { T } } = b _ { * } a , \quad a ^ { * } 1 _ { N } = a .
$$

Multiple applications of linear differential operators are naturally defined, such as $a ^ { * } b ^ { * }$ , $( a ^ { * } b ^ { * } ) c ^ { * }$ , $a ^ { * } ( b ^ { * } c ^ { * } )$ , etc. The operations are multilinear, associative but noncommutative; thus, powers can be defined as

$$
a ^ { * k } = a ^ { * } a ^ { * } \cdot \cdot \cdot a ^ { * } ( k { \mathrm { t i m e } } ) , \quad a ^ { k } : = a ^ { * k } 1 _ { N } ,
$$

the identity operator $I$ operates on scalar and vector functions $\phi$ and $b$ as $I \phi = \phi$ , $I b = b$ .

We identify all vector functions $a : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ as vector fields. All vector fields in $\mathbf { R } ^ { N }$ form a ( $\infty$ -dimensional) real Lie bracket under Lie bracket

$$
[ a , b ] : = a _ { * } b - b _ { * } a = b ^ { * } a - a ^ { * } b = ( b ^ { * } a ^ { * } - a ^ { * } b ^ { * } ) 1 _ { N } .
$$

The Lie algebra ${ \bf V } ^ { N }$ is associated with the ( $\infty$ -dimensional) local Lie group $\mathbf { D } ^ { N }$ of near-identity diffeomorphisms—or simply near-1 maps—of $\mathbf { R } ^ { N }$ .

Consider the dynamical system in $\mathbf { R } ^ { N }$

$$
\frac { \mathrm { d } \boldsymbol { x } } { \mathrm { d } t } = \boldsymbol { a } ( \boldsymbol { x } ) ,
$$

defined by a vector field $a$ . It possesses a phase flow $e _ { a } ^ { t } = e ^ { t }$ , which is a one-parameter (in $t$ ) group of near-1 maps of $\mathbf { R } ^ { N }$ ,

$$
e ^ { 0 } = 1 _ { N } , \quad e ^ { t + s } = e ^ { t } \circ e ^ { s } ,
$$

and generates the solution by $x ( 0 )  e _ { a } ^ { t } x ( 0 ) = x ( t )$ . The phase flow is expressible as a convergent power series in $t$ :

$$
\begin{array} { l } { { \displaystyle e _ { a } ^ { t } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } t ^ { k } e _ { k } , } } \\ { { \displaystyle e _ { 0 } = 1 _ { N } , \quad e _ { k } = \frac { 1 } { k } a ^ { * } e _ { k - 1 } = \frac { 1 } { k ! } ( a ^ { * } ) ^ { k } 1 _ { N } = \frac { 1 } { k ! } a ^ { k } . } } \end{array}
$$

We define

$$
\displaystyle \mathtt { E x p } t a ^ { * } : = I + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } ( t a ) ^ { * k } , \quad I \mathrm { \ i s \ t h e \ i d e n t i t y \ o p e r a t o r { . } }
$$

This is an operator power series operating on scalar and vector functions, and defined by

$$
\exp t a : = ( \mathrm { E x p } t a ^ { * } ) 1 _ { N } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } ( t a ^ { * } ) ^ { k } 1 _ { N } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } \frac { t ^ { k } } { k ! } a ^ { k } ,
$$

then

$$
e _ { a } ^ { t } = (  { \mathrm { E x p } } t a ^ { * } ) 1 _ { N } = \exp t a ,
$$

for scalar function

$$
\phi \circ e _ { a } ^ { t } = \phi \circ \exp { t a } = ( \exp { t a ^ { * } } ) \phi ,
$$

for vector function

$$
b \circ e _ { a } ^ { t } = b \circ \exp { t a } = ( \mathrm { E x p } t a ^ { * } ) b = ( \mathrm { E x p } t a ^ { * } ) b ^ { * } 1 _ { N } .
$$

Each numerical algorithm solving the system (1.1) possesses the step transition map $f _ { a } ^ { s }$ which is one-parameter (in step-size $s$ ) family (in general not a one-parameter group in $s$ ) of near-1 maps on $\mathbf { R } ^ { N }$ , expressible as a convergent power series in $s$

$$
f _ { a } ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } ,
$$

the coefficients can be determined recursively form the defining difference equation. The transition generates the numerical solution $x ( 0 ) ~ \longrightarrow ~ ( f _ { a } ^ { s } ) ^ { N } x ( 0 ) \approx x ( N s )$ by iterations with step-size $s$ chosen fixed in general.

The main problem is to construct and analyze the algorithmic approximations $\left. f _ { a } ^ { s } \approx e _ { a } ^ { t } \right| _ { t = s } = e _ { a } ^ { s }$ in a proper way. For this purpose, we propose a unified framework based on the apparatus of formal power series, Lie algebra of vector fields, and the corresponding Lie group of diffeomorphisms [Lie88,Olv93] .

# 9.2 Near-0 and Near-1 Formal Power Series

Among the formal power series $\sum _ { 0 } ^ { \infty } s ^ { k } a _ { k } , a _ { k } : \mathbf { R } ^ { N }  \mathbf { R } ^ { N }$ , we pick out two special classes. The first class consists of those with $a _ { 0 } ~ = ~ 0$ , called near-0 formal vector fields and the second class consists of those with $a _ { 0 } = 1 _ { N }$ , called near-1 formal maps (diffeomorphisms).

All near-0 formal vector fields $a ^ { s } = \sum _ { 1 } ^ { \infty } s ^ { k } a _ { k }$ form a ( $\infty$ -dim.) real Lie algebra $\mathbf { F V } ^ { N }$ under the Lie bracket

$$
[ a ^ { s } , b ^ { s } ] = \left[ \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } , \sum _ { k = 1 } ^ { \infty } s ^ { k } b _ { k } \right] : = \sum _ { k = 2 } ^ { \infty } s ^ { k } \sum _ { i + j = k } [ a _ { i } , b _ { j } ] .
$$

The associated near-0 formal differential operators and their products are

$$
\begin{array} { l } { ( a ^ { s } ) _ { * } : = \displaystyle \left( \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \right) _ { * } : = \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k * } , } \\ { \displaystyle a ^ { s * } : = \left( \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \right) ^ { * } : = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } ^ { * } , } \\ { \displaystyle a ^ { s * } b ^ { s * } : = \sum _ { k = 2 } ^ { \infty } s ^ { k } \sum _ { i + j = k } ^ { \infty } a _ { i } ^ { * } b _ { j } ^ { * } , \quad ( a ^ { s * } ) ^ { 2 } : = a ^ { s * } a ^ { s * } , \mathrm { e t c . } } \end{array}
$$

For any vector function $a = ( a _ { 1 } , \cdots , a _ { N } ) ^ { \mathrm { T } } : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ and any near-1 formal map $g ^ { s } = 1 + \sum _ { k = 1 } ^ { \infty } s ^ { k } g _ { k }$ , we define the composition,

$$
\begin{array} { l } { { ( a \circ g ^ { s } ) ( x ) = a ( g ^ { s } ( x ) ) = a ( x ) + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } ( a \circ g ) _ { k } ( x ) , } } \\ { { ( a \circ g ) _ { k } = \displaystyle \sum _ { m = 1 } ^ { k } \displaystyle \sum _ { k _ { 1 } + \cdots + k _ { m } = k } \frac { 1 } { m ! } ( D ^ { m } a ) ( g _ { k _ { 1 } } , \cdot \cdot \cdot , g _ { k _ { m } } ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle D ^ { m } a = ( D ^ { m } a _ { 1 } , \cdots , D ^ { m } a _ { N } ) ^ { \mathrm { T } } , } } \\ { { \displaystyle D ^ { m } a _ { i } ( v _ { 1 } , \cdots , v _ { m } ) = \sum _ { j _ { 1 } , \cdots , j _ { m } = 1 } ^ { N } \frac { \partial ^ { m } a _ { i } } { \partial x _ { j _ { 1 } } \cdots \partial x _ { j _ { m } } } v _ { 1 j _ { 1 } } \cdots v _ { m j _ { m } } , } } \end{array}
$$

is the usual $m$ -th differential multi-linear form for $m$ tangent vectors $v _ { i } = ( v _ { i _ { 1 } } , \cdots ,$ $v _ { i _ { N } } ) ^ { \mathrm { T } } ( i \ = \ 1 , \cdot \cdot \cdot , m )$ at point $\boldsymbol { x } \in \mathbf { R } ^ { N }$ , which is invariant under permutation of Nvectors. Using the identities,

$$
\begin{array} { l } { { ( D ^ { 1 } a ) ( b ) = b ^ { * } a , } } \\ { { ( D ^ { 2 } a ) ( b , c ) = ( c ^ { * } b ^ { * } - ( c ^ { * } b ) ^ { * } ) a , } } \\ { { ( D ^ { 3 } a ) ( b , b , b ) = ( b ^ { * 3 } + 2 b ^ { 3 * } - 3 b ^ { * } b ^ { 2 * } ) a . } } \end{array}
$$

We get in particular

$$
\begin{array} { l } { ( a \circ g ) _ { 1 } = g _ { 1 } ^ { \ast } a , } \\ { ( a \circ g ) _ { 2 } = g _ { 2 } ^ { \ast } a + \cfrac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) a , } \\ { ( a \circ g ) _ { 3 } = g _ { 3 } ^ { \ast } a + ( ( g _ { 2 } ^ { \ast } g _ { 1 } ^ { \ast } - ( g _ { 2 } ^ { \ast } g _ { 1 } ) ^ { \ast } ) a + \cfrac 1 { 3 ! } ( g _ { 1 } ^ { \ast 3 } + 2 g _ { 1 } ^ { 3 \ast } - 3 g _ { 1 } ^ { \ast } g _ { 1 } ^ { 2 \ast } ) a . } \end{array}
$$

For any two near-1 formal maps

$$
f ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } , \quad g ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } g _ { k } ,
$$

the composition $f ^ { s } \circ g ^ { s }$ is defined in a term by term way:

$$
\begin{array} { l } { \displaystyle \big ( f ^ { s } \circ g ^ { s } \big ) ( x ) = f ^ { s } ( g ^ { s } ( x ) ) = 1 _ { N } ( g ^ { s } ( x ) ) + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } ( g ^ { s } ( x ) ) } \\ { \displaystyle = : 1 _ { N } ( x ) + \sum _ { k = 1 } ^ { \infty } s ^ { k } ( f \circ g ) _ { k } ( x ) , } \\ { \displaystyle ( f \circ g ) _ { 1 } = f _ { 1 } + g _ { 1 } , } \\ { \displaystyle ( f \circ g ) _ { k } = f _ { k } + g _ { k } + \delta ( f _ { 1 } , \cdots , f _ { k - 1 } ; g _ { 1 } , \cdots , g _ { k - 1 } ) , \quad k \geq 2 , } \\ { \displaystyle \delta ( f _ { 1 } , \cdots , f _ { k - 1 } ; g _ { 1 } , \cdots , g _ { k - 1 } ) = \displaystyle \sum _ { i = 1 } ^ { k - 1 } \sum _ { m = 1 } ^ { i } \sum _ { i _ { 1 } + \cdots + i _ { m = i } } \frac { 1 } { m ! } ( D ^ { m } f _ { k - i } ) ( g _ { i _ { 1 } } , \cdots , g _ { i _ { m } } ) . } \end{array}
$$

In particular we get,

$$
\begin{array} { l } { { ( f \circ g ) _ { 2 } = f _ { 2 } + g _ { 2 } + g _ { 1 } ^ { \ast } f _ { 1 } , } } \\ { { \ } } \\ { { ( f \circ g ) _ { 3 } = f _ { 3 } + g _ { 3 } + g _ { 1 } ^ { \ast } f _ { 2 } + g _ { 2 } ^ { \ast } f _ { 1 } + \displaystyle \frac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) f _ { 1 } , } } \\ { { \ } } \\ { { ( f \circ g ) _ { 4 } = f _ { 4 } + g _ { 4 } + g _ { 1 } ^ { \ast } f _ { 3 } + g _ { 2 } ^ { \ast } f _ { 2 } + g _ { 3 } ^ { \ast } f _ { 1 } + \displaystyle \frac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) f _ { 2 } \ ~ } } \\ { { \ } } \\ { { \ \qquad + ( g _ { 2 } ^ { \ast } g _ { 1 } ^ { \ast } - ( g _ { 2 } ^ { \ast } g _ { 1 } ) ^ { \ast } ) f _ { 1 } + \displaystyle \frac 1 { 3 ! } ( g _ { 1 } ^ { \ast 3 } + 2 g _ { 1 } ^ { 3 \ast } - 3 g _ { 1 } ^ { \ast } g _ { 1 } ^ { 2 \ast } ) f _ { 1 } . } } \end{array}
$$

Under this composition rule, all near-1 formal maps

$$
f ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k }
$$

form a $\scriptstyle ( \infty \mathrm { - d i m } )$ ) formal Lie group $\mathbf { F } \mathbf { D } ^ { N }$ . In group $\mathbf { F } \mathbf { D } ^ { N }$ , inverse elements, square roots, rational powers, etc., always exist, and their coefficients can always be determined recursively by the defining composition relations. For example, the inverse $( f ^ { s } ) ^ { - 1 } : = 1 + \sum _ { k = 1 } ^ { \infty } { s ^ { k } h _ { k } } = h ^ { s }$ is defined by $( f ^ { s } \circ h ^ { s } ) = 1 _ { N }$ , hence

$$
f _ { 1 } + h _ { 1 } = 0 , \quad f _ { k } + h _ { k } + \delta ( f _ { 1 } , \cdot \cdot , f _ { k - 1 } ; h _ { 1 } , \cdot \cdot , h _ { k - 1 } ) = 0 , \quad k \geq 2 .
$$

In particular,

$$
\begin{array} { l } { { h _ { 1 } = - f _ { 1 } , \quad h _ { 2 } = - f _ { 2 } + f _ { 1 } ^ { 2 } , } } \\ { { { } } } \\ { { h _ { 3 } = - f _ { 3 } + f _ { 1 } ^ { * } f _ { 2 } + \big ( f _ { 2 } ^ { * } - f _ { 1 } ^ { 2 * } \big ) f _ { 1 } - { \textstyle \frac 1 2 } f _ { 1 } ^ { 3 } + { \textstyle \frac 1 2 } f _ { 1 } ^ { 2 * } f _ { 1 } . } } \end{array}
$$

There is an obvious one-one correspondence between the Lie algebra $\mathbf { F V } ^ { N }$ and the Lie group $\mathbf { F } \mathbf { D } ^ { N }$ , established simply by $+ 1 _ { N }$ and $- 1 _ { N }$ . However, the more significant one-one correspondence between them is given by exp and its inverse log.

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \exp : { \bf { F } } { \bf { V } } ^ { N }  { \bf { F } } { \bf { D } } ^ { N } , } } \\ { { } } & { { } } & { { \displaystyle a ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \Longrightarrow ~ \exp a ^ { s } ~ = : 1 _ { N } + \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ! } ( a ^ { s * } ) ^ { m } 1 _ { N } } } \\ { { } } & { { } } & { { \displaystyle = : 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } = f ^ { s } . } } \end{array}
$$

Note that

$$
( a ^ { s * } ) ^ { m } = \left( \sum _ { k _ { 1 } = 1 } ^ { \infty } { s ^ { k _ { 1 } } a _ { k _ { 1 } } ^ { * } } \right) \cdot \cdot \cdot \left( \sum _ { k _ { m } = 1 } ^ { \infty } { s ^ { k _ { m } } a _ { k _ { m } } ^ { * } } \right) = \sum _ { k _ { 1 } , \cdots , k _ { m } = 1 } ^ { \infty } { s ^ { k _ { 1 } + \cdots + k _ { m } } a _ { k _ { 1 } } ^ { * } } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } ,
$$

so we get easily

$$
\begin{array} { l l } { f _ { k } = \displaystyle \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } , } & { k \geq 1 , f _ { 1 } = a _ { 1 } , } \\ { f _ { k } = a _ { k } + \displaystyle \sum _ { m = 2 } ^ { k } \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } , k \geq 2 , f _ { 2 } = a _ { 2 } + \displaystyle \frac { 1 } { 2 } a _ { 1 } ^ { 2 } . } \end{array}
$$

Note that (2.2) provides a 2-way recursion formula from $a _ { 1 } , \cdots , a _ { k }$ to $f _ { 1 } , \cdots , f _ { k }$ and vice versa. Therefore, exp maps $\mathbf { F V } ^ { N }$ one-one onto $\mathbf { F } \mathbf { D } ^ { N }$ and its inverse, i.e., log is defined by the same (2.2):

$$
\begin{array} { r l } & { \log = ( \exp ) ^ { - 1 } : { \mathbf { F } } { \mathbf { D } } ^ { N } \longrightarrow { \mathbf { F } } { \mathbf { V } } ^ { N } , } \\ & { \log \exp \ a ^ { s } = a ^ { s } , \quad \exp \log \ f ^ { s } = f ^ { s } . } \end{array}
$$

In particular,

$$
\begin{array} { l } { { a _ { 1 } = f _ { 1 } , \quad a _ { 2 } = f _ { 2 } - \displaystyle \frac { 1 } { 2 } a _ { 1 } ^ { 2 } , \quad a _ { 3 } = f _ { 3 } - \displaystyle \frac { 1 } { 2 } ( a _ { 1 } ^ { * } a _ { 2 } + a _ { 2 } ^ { * } a _ { 1 } ) - \displaystyle \frac { 1 } { 3 ! } a _ { 1 } ^ { 3 } , } } \\ { { \displaystyle a _ { 4 } = f _ { 4 } - \displaystyle \frac { 1 } { 2 } \big ( a _ { 1 } ^ { * } a _ { 3 } + a _ { 2 } ^ { 2 } + a _ { 3 } ^ { * } a _ { 1 } \big ) - \displaystyle \frac { 1 } { 3 ! } \big ( a _ { 1 } ^ { * } a _ { 1 } ^ { * } a _ { 2 } + a _ { 1 } ^ { * } a _ { 2 } ^ { * } a _ { 1 } + a _ { 2 } ^ { * } a _ { 1 } ^ { * } a _ { 1 } \big ) - \displaystyle \frac { 1 } { 4 ! } a _ { 1 } ^ { 4 } , } } \\ { { \displaystyle a _ { k } = f _ { k } - \displaystyle \sum _ { m = 2 } ^ { k - 1 } \displaystyle \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } - \displaystyle \frac { 1 } { k ! } a _ { 1 } ^ { k } , \quad k \ge 3 . } } \end{array}
$$

An equivalent construction of $\log f ^ { s } = a ^ { s }$ is

$$
\log f ^ { s } = \sum _ { m = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { m - 1 } } { m } } h _ { m } ^ { s } ,
$$

where

$$
\begin{array} { r } { h _ { 1 } ^ { s } = f ^ { s } - 1 _ { N } , \quad h _ { m } ^ { s } = h _ { m - 1 } ^ { s } \circ f ^ { s } - h _ { m - 1 } ^ { s } . } \end{array}
$$

It is easy to compute

$$
\begin{array} { l } { { \displaystyle h _ { 1 } ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } = \sum _ { k _ { 1 } = 1 } ^ { \infty } s ^ { k _ { 1 } } ( 1 _ { N } \circ f ) _ { k _ { 1 } } } , } \\ { { } } \\ { { \displaystyle h _ { 2 } ^ { s } = \sum _ { k _ { 1 } , k _ { 2 } = 1 } ^ { \infty } s ^ { k _ { 1 } + k _ { 2 } } ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } , } } \\ { { } } \\ { { \displaystyle h _ { 3 } ^ { s } = \sum _ { k _ { 1 } , k _ { 2 } , k _ { 3 } = 1 } ^ { \infty } s ^ { k _ { 1 } + k _ { 2 } + k _ { 3 } } ( ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } \circ f ) _ { k _ { 3 } } , } } \\ { { } } \\ { { \displaystyle . . . . } } \end{array}
$$

Substituting in (2.3) and equating with $\sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k }$ , we get

$$
a _ { k } = \sum _ { m = 1 } ^ { k } { \frac { ( - 1 ) ^ { m - 1 } } { m } } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } ( \cdots ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } \cdots \circ f ) _ { k _ { m } } .
$$

It is easy to verify $\log \exp a ^ { s } = a ^ { s }$ for this log, so this is precisely the inverse of exp, thus agreeing with the previous one.

We use the above construction (2.4) to establish the formal Baker–Campbell– Hausdorff formula[Bak05,Hau06] . For arbitrary near-1 formal maps $f ^ { s } , g ^ { s }$ ,

$$
\log { \big ( } f ^ { s } \circ g ^ { s } { \big ) } = \log ~ f ^ { s } + \log ~ g ^ { s } + \sum _ { k = 1 } ^ { \infty } d _ { k } ( \log ~ f ^ { s } , \log ~ g ^ { s } ) ,
$$

where log $f ^ { s } = a ^ { s }$ , log $g ^ { s } = b ^ { s }$ , then[Dyn46]

$$
d _ { k } ( a ^ { s } , b ^ { s } ) = \frac { 1 } { k } \sum _ { m = 1 } ^ { k } \frac { ( - 1 ) ^ { m - 1 } } { m } \sum _ { { \bf \Phi } _ { p _ { 1 } + q _ { 1 } + \ldots + p _ { m } + q _ { m } = k } \atop { \bf \Phi } _ { p _ { i } + q _ { i } \geq 1 , p _ { i } \geq 0 , q _ { i } \geq 0 } } \frac { [ ( a ^ { s } ) ^ { p _ { 1 } } ( b ^ { s } ) ^ { q _ { 1 } } \cdot \cdot \cdot ( a ^ { s } ) ^ { p _ { m } } ( b ^ { s } ) ^ { q _ { m } } ] } { p _ { 1 } ! q _ { 1 } ! \cdot \cdot \cdot p _ { m } ! q _ { m } ! } ,
$$

where

$$
( x ) ^ { p } = x x \cdot \cdot \cdot x ( p { \mathrm { ~ t i m e s } } ) , \quad [ x _ { 1 } x _ { 2 } x _ { 3 } \cdot \cdot \cdot x _ { n } ] = [ [ \cdot \cdot [ [ x _ { 1 } , x _ { 2 } ] , x _ { 3 } ] , \cdot \cdot \cdot ] , x _ { n } ] .
$$

In particular,

$$
d _ { 1 } = { \frac { 1 } { 2 } } [ a ^ { s } , b ^ { s } ] , \quad d _ { 2 } = { \frac { 1 } { 1 2 } } { \big ( } [ a ^ { s } b ^ { s } b ^ { s } ] + [ b ^ { s } a ^ { s } a ^ { s } ] { \big ) } , \quad d _ { 3 } = - { \frac { 1 } { 2 4 } } [ a ^ { s } b ^ { s } b ^ { s } a ^ { s } ] .
$$

Let $\log { ( f ^ { s } \circ g ^ { s } ) } = c ^ { s } = \sum _ { k = 1 } ^ { \infty } { s ^ { k } c _ { k } }$ , then

$$
\begin{array} { l } { { c _ { 1 } = a _ { 1 } + b _ { 1 } , \quad c _ { 2 } = a _ { 2 } + b _ { 2 } + \displaystyle \frac { 1 } { 2 } [ a _ { 1 } b _ { 1 } ] , } } \\ { { \ } } \\ { { c _ { 3 } = a _ { 3 } + b _ { 3 } + \displaystyle \frac { 1 } { 2 } ( [ a _ { 1 } b _ { 2 } ] + [ a _ { 2 } b _ { 1 } ] ) + \displaystyle \frac { 1 } { 1 2 } ( [ a _ { 1 } b _ { 1 } b _ { 1 } ] + [ b _ { 1 } a _ { 1 } a _ { 1 } ] ) , } } \\ { { \ } } \\ { { c _ { 4 } = a _ { 4 } + b _ { 4 } + \displaystyle \frac { 1 } { 1 2 } ( [ a _ { 1 } b _ { 3 } ] + [ a _ { 2 } b _ { 2 } ] + [ a _ { 3 } b _ { 1 } ] ) } } \\ { { \ } } \\ { { \displaystyle \qquad + \displaystyle \frac { 1 } { 1 2 } \big ( [ a _ { 1 } b _ { 1 } b _ { 2 } ] + [ a _ { 1 } b _ { 2 } b _ { 1 } ] + [ a _ { 2 } b _ { 1 } b _ { 1 } ] + [ b _ { 1 } a _ { 1 } a _ { 2 } ] + [ b _ { 1 } a _ { 2 } a _ { 1 } ] + [ b _ { 2 } a _ { 1 } a _ { 1 } ] \big ) } } \\ { { \ } } \\ { { \displaystyle - \displaystyle \frac { 1 } { 2 4 } [ a _ { 1 } b _ { 1 } b _ { 1 } a _ { 1 } ] , \quad \mathrm { e t c . } } } \end{array}
$$

Note that the classical BCH formula is restricted to the composition of two oneparameter groups, where log $f ^ { s } = s a _ { 1 }$ and $\log { g ^ { s } } = s b _ { 1 }$ .

The log transform reduces matters at the Lie group level to those at the easier level of Lie algebra. All properties of near-1 formal maps have their logarithmic interpretations.

Proposition 2.1. [Fen93a,Fen92,Fen93b] We list some of them, let $\log f ^ { s } = a ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k }$ :

$1 ^ { \circ }$ $f ^ { s }$ is a phase flow, i.e., $f ^ { s + t } = f ^ { s } \circ f ^ { t } \Leftrightarrow \log f ^ { s } = s a _ { 1 }$ .   
$2 ^ { \circ }$ $f ^ { s }$ is revertible, i.e., $f ^ { s } \circ f ^ { - s } = 1 _ { N } \Leftrightarrow \log f ^ { s }$ is odd in $s$ .   
$3 ^ { \circ }$ $f ^ { s }$ raised to real $\mu$ -th power $( f ^ { s } ) ^ { \mu } \Leftrightarrow \log ( f ^ { s } ) ^ { \mu } = \mu \log f ^ { s } $ . In particular, $\log { ( f ^ { s } ) ^ { - 1 } } = - \log { f ^ { s } } , \log { \sqrt { f ^ { s } } } = { \frac { 1 } { 2 } } \log { f ^ { s } } .$ .   
$4 ^ { \circ }$ $f ^ { s }$ scaled to $f ^ { \alpha s } \Leftrightarrow \log { ( f ^ { \alpha s } ) } = ( \bar { \log { f } } ) ^ { \alpha s } .$ . In particular,   
$\log { ( f ^ { - s } ) } = ( \log { f } ) ^ { - s }$ .   
$5 ^ { \circ }$ $f ^ { s } - g ^ { s } = O ( s ^ { p + 1 } ) \Leftrightarrow \log f ^ { s } - \log g ^ { s } = O ( s ^ { p + 1 } ) .$ .   
$6 ^ { \circ }$ $\begin{array} { r l r } & { \stackrel { \scriptscriptstyle \mathcal { I } } { f ^ { s } } \circ g ^ { s } = g ^ { s } \circ f ^ { s } \Leftrightarrow \left[ \log f ^ { s } , \log g ^ { s } \right] = 0 \Leftrightarrow \log f ^ { s } \circ g ^ { s } ) = \log f ^ { s } + \log g ^ { s } + \log g ^ { s } . } & \\ & { ( f ^ { s } \circ g ^ { s } ) = h ^ { s } \Leftrightarrow \log h ^ { s } = \log ( f ^ { s } \circ g ^ { s } ) = \log f ^ { s } + \log g ^ { s } + \displaystyle \sum _ { k = 1 } ^ { \infty } d _ { k } ( \log f ^ { s } , \log g ^ { s } ) . } & \end{array}$ $7 ^ { \circ }$   
$8 ^ { \circ }$ $f ^ { s }$ symplectic $\Leftrightarrow$ all $a _ { k }$ are Hamiltonian fields (see Chapter 5).   
$9 ^ { \circ }$ $f ^ { s }$ contact $\Leftrightarrow$ all $a _ { k }$ are contact fields (see Chapter 11).   
$1 0 ^ { \circ }$ $f ^ { s }$ volume-preserving $\Leftrightarrow$ all $a _ { k }$ are source-free fields (see Chapter 10).

The log transform has important bearing on dynamical systems with Lie algebra structure. The structure-preserving property of maps $f ^ { s }$ at the Lie group $( \mathbf { G } \subset \mathbf { D } _ { m } )$ ) level can be characterized through their logarithms at the associated Lie algebra $\mathbf { L } \subset$ $\mathbf { V } _ { m }$ ) level.

# 9.3 Algorithmic Approximations to Phase Flows

# 9.3.1 Approximations of Phase Flows and Numerical Method

We return to the main problem of approximation to the phase flow for dynamical system ${ \frac { \operatorname { d } { \boldsymbol { x } } } { \operatorname { d } t } } = a ( { \boldsymbol { x } } )$ .

$$
\begin{array} { l } { { f _ { a } ^ { s } = f ^ { s } = 1 _ { N } + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } \approx e _ { a } ^ { s } = 1 _ { N } + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } e _ { k } , } } \\ { { e _ { k } = \displaystyle \frac { a ^ { k } } { k ! } . } } \end{array}
$$

If $f _ { k } = e _ { k }$ $( 1 \leq k \leq p )$ ), we say $f _ { a } ^ { s }$ is accurate to order $\geq p$ , if moreover, $f _ { p + 1 } \neq e _ { p + 1 }$ we say it is accurate to order $p$ .

Let $\log f ^ { s } = a ^ { s } = \sum s ^ { k } a _ { k } .$ . Note that the first $p { + 1 }$ equations in (2.2) completely determine $a _ { 1 } , a _ { 2 } , \cdots , a _ { p + 1 }$ and $f _ { 1 } , f _ { 2 } , \cdots , f _ { p + 1 }$ each other. It is then easy to establish

$$
\begin{array} { r l } & { f _ { k } = e _ { k } , \quad 1 \leq k \leq p ; \quad f _ { p + 1 } \neq e _ { p + 1 } \Longleftrightarrow } \\ & { a = a _ { 1 } = e _ { 1 } ; \quad a _ { k } = 0 , \quad 1 < k \leq p ; \quad a _ { p + 1 } = f _ { p + 1 } - e _ { p + 1 } \neq 0 . } \end{array}
$$

So, the orders of approximation for $f _ { a } ^ { s } \approx e _ { a } ^ { s }$ and for $\log f _ { a } ^ { s } - s a$ are the same.

Moreover, note that we have a formal field

$$
s ^ { - 1 } \log f ^ { s } = s ^ { - 1 } a ^ { s } = a + \sum _ { k = 1 } ^ { \infty } s ^ { k + 1 } a _ { k + 1 } = a + O ( s ^ { p } ) ,
$$

which is the original field $a$ up to a near-0 perturbation and defines a formal dynamical system

$$
{ \frac { \mathrm { d } x } { \mathrm { d } t } } = ( s ^ { - 1 } \log f ^ { s } ) ( x ) = a ( x ) + \sum _ { k = 1 } ^ { \infty } { s ^ { k + 1 } a _ { k + 1 } ( x ) }
$$

whose diagoible algorithm formal of order $t$ $s$ is exactly ed solution $t$ $e _ { s ^ { - 1 } a ^ { s } } ^ { t } ~ = ~ \exp { t s ^ { - 1 } } a ^ { s }$ $e _ { s ^ { - 1 } a ^ { s } } ^ { t } | _ { t = s }$ $f ^ { s }$ $f _ { a } ^ { s }$ $p$   
equation with field $a$ ; however, it gives the right solution of a perturbed equation with field $s ^ { - 1 } \log f _ { a } ^ { s } = a + O ( s ^ { p } )$ . There could be many methods with the same formal order of accuracy but with quite different qualitative behavior. The problem is to choose among them those leading to allowable perturbations in the equation. For systems with geometric structure, the $8 ^ { \circ } , 9 ^ { \circ } , 1 0$ $1 0 ^ { \circ }$ of Proposition 2.1 provide guidelines for a proper choice. The structure-preservation requirement for the algorithms precludes all unallowable perturbations alien to the pertinent type of dynamics. Take, for example, Hamiltonian systems. A transition map $f _ { a } ^ { s }$ for Hamiltonian field $a$ is symplectic if and only if all fields $a _ { k }$ are Hamiltonian, i.e., the induced perturbations in the equation are Hamiltonian. So symplectic algorithms are clean, inherently free from all kinds of perturbations alien to Hamiltonian dynamics (such as artificial dissipation inherent in the vast majority of conventional methods), this accounts for their superior performance. The situations are the same for contact and volume-preserving algorithms . The Proposition 2.1 profound impact on later developed called “Backward error series” work, “Modified equation” and “Modified integrator”[Hai94,CHV05,CHV07] .

# 9.3.2 Typical Algorithm and Step Transition Map

Finally we give, as an illustration, four simplest methods together with step transition maps and their logarithms.

$$
e _ { a } ^ { s } = 1 _ { N } + s a + \frac { 1 } { 2 } s ^ { 2 } a ^ { 2 } + \frac { 1 } { 3 ! } s ^ { 3 } a ^ { 3 } + O ( s ^ { 4 } ) .
$$

(1) Explicit Euler method $( E )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = s a ( x _ { 0 } ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = s a , } } \\ { { \displaystyle f _ { E } ^ { s } = 1 _ { N } + s a , } } \\ { { \displaystyle \log f _ { E } ^ { s } = s a - \frac { s ^ { 2 } } { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \end{array}
$$

non-revertible, order $= 1$ .

(2) Implicit Euler method $( I )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = s a ( x _ { 1 } ) , } } \\ { { f ^ { s } - 1 _ { N } = s a \circ f ^ { s } , } } \\ { { f _ { I } ^ { s } = ( 1 _ { N } - s a ) ^ { - 1 } = ( f _ { E } ^ { - s } ) ^ { - 1 } = 1 + s a + s ^ { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \\ { { \log f _ { I } ^ { s } = s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \end{array}
$$

non-revertible, order $= 1$

(3) Trapezoidal method $( T )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = \displaystyle \frac { s } { 2 } ( a ( x _ { 1 } ) + a ( x _ { 0 } ) ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = \displaystyle \frac { s } { 2 } ( a \circ f ^ { s } + a ) , } } \\ { { \displaystyle f _ { T } ^ { s } = \left( 1 _ { N } - \frac { s } { 2 } a \right) ^ { - 1 } \circ \left( 1 _ { N } + \frac { s } { 2 } a \right) = f _ { I } ^ { \frac { s } { 2 } } \circ f _ { E } ^ { \frac { s } { 2 } } } } \\ { { \displaystyle ~ = ( f _ { E } ^ { \frac { s } { 2 } } ) ^ { - 1 } \circ f _ { C } ^ { s } \circ f _ { E } ^ { \frac { s } { 2 } } = 1 _ { N } + s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + \frac { s ^ { 3 } } { 4 } a ^ { 3 } + O ( s ^ { 4 } ) , } } \\ { { \log f _ { T } ^ { s } = s a + \frac { s ^ { 3 } } { 1 2 } a ^ { 3 } + O ( s ^ { 5 } ) , } } \end{array}
$$

revertible, order ${ \it \Delta \phi } = 2 { \it \Delta \Psi }$ , symplectic for linear Hamiltonian but non-symplectic for nonlinear Hamiltonian systems, where $f _ { C } ^ { s }$ denoting following centered Euler scheme.

(4) Centered Euler method $( C )$ :

$$
\begin{array} { l } { { \displaystyle x _ { 1 } - x _ { 0 } = s a \Big ( \frac 1 2 \big ( x _ { 1 } + x _ { 0 } \big ) \Big ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = s a \circ \Big ( \frac 1 2 \big ( f ^ { s } + 1 _ { N } \big ) \Big ) , } } \end{array}
$$

2-stage version recommended for implementation:

$$
\begin{array} { r l } & { \bar { x } = x + \frac { s } { 2 } a ( \bar { x } ) , \quad x _ { 1 } = 2 \bar { x } - x _ { 0 } , } \\ & { \bar { x } = f _ { \bar { I } } ^ { \ \frac { s } { 2 } } ( x _ { 0 } ) , \qquad x _ { 1 } = 2 f _ { \bar { I } } ^ { \ \frac { s } { 2 } } ( x _ { 0 } ) - 1 _ { N } ( x _ { 0 } ) , } \\ & { f _ { C } ^ { \  s } = 2 f _ { \bar { I } } ^ { \ \frac { s } { 2 } } - 1 _ { N } = \left( 1 _ { N } + \frac { s } { 2 } a \right) \circ \left( 1 _ { N } - \frac { s } { 2 } a \right) ^ { - 1 } = f _ { E } ^ { \ \frac { s } { 2 } } \circ f _ { \bar { I } } ^ { \frac { s } { 2 } } } \\ & { \qquad = 1 _ { N } + s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + \frac { s ^ { 3 } } { 8 } ( a _ { \ast } a ^ { 2 } + a ^ { 3 } ) + { \cal O } ( s ^ { 4 } ) , } \\ & { \log f _ { C } ^ { \ } = s a + s ^ { 3 } \left( \frac { 1 } { 8 } a _ { \ast } a ^ { 2 } - \frac { 1 } { 2 4 } a ^ { 3 } \right) + { \cal O } ( s ^ { 5 } ) , } \end{array}
$$

revertible, order $= 2$ , unconditionally symplectic with preservation of all quadratic invariants for Hamiltonian systems.

Note the similarities and delicate differences between $C$ and $T$ : Both can be composed by a $\frac { s } { 2 }$ implicit and a $\frac { s } { 2 }$ explicit stages but in opposite orderings. Moreover, they

are conjugate to each other. $C$ is far less known than $T$ , it becomes prominent only after the recent development of symplectic algorithms [Fen85] . In crucial aspects, $C$ is superior.

Remark 3.1. The above $\log f _ { C } ^ { s }$ is not others but just formal vector fields for centered Euler scheme or present called backward error analysis

$$
\bar { f } = f + \frac { s ^ { 2 } } { 1 2 } ( f ^ { \prime } f ^ { \prime } f - \frac { 1 } { 2 } f ^ { \prime \prime } ( f , f ) ) .
$$

# 9.4 Related B-Series Works

Consider the numerical solution of ODEs

$$
\dot { z } = f ( z ) , \quad z \in \mathbf { R } ^ { n } .
$$

B-series methods: B-series were introduced by Harier and Wanner $\mathrm { [ H W 7 4 ] }$ . The Taylor series of exact solution of (4.1) with initial value $z ( 0 ) = z$ can be written as

$$
z ( h ) = z + h f ( z ) + { \frac { h ^ { 2 } } { 2 ! } } f ^ { \prime } ( z ) f ( z ) + { \frac { h ^ { 3 } } { 3 ! } } { \big ( } f ^ { \prime \prime } ( f ( z ) , f ( z ) ) + f ^ { \prime } ( z ) f ^ { \prime } ( z ) f ( z ) { \big ) } + \cdots .
$$

B-series methods are numerical integrators $z _ { n + 1 } = \Phi _ { h } ( z _ { n } )$ whose Taylor series have the same structure with real coefficients $a ( \tau )$ :

$$
\begin{array} { r c l } { { \Phi _ { h } ( z ) } } & { { = } } & { { z + h a ( \bullet ) f ( z ) + h ^ { 2 } a ( \underline { { { \ O } } } ) f ^ { \prime } ( z ) f ( z ) + h ^ { 3 } \bigl ( \frac { a ( \underline { { { \ O } } } ) } { 2 ! } f ^ { \prime \prime } ( f ( z ) , f ( z ) ) } } \\ { { } } & { { } } & { { + a ( \bigl \{ \begin{array} { l } { { \ O } } \\ { { \ O } } \end{array}  + \ O } ( z ) f ^ { \prime } ( z ) f ^ { \prime } ( z ) \bigr ) + \cdot \cdot \cdot , }  \end{array}
$$

where coefficients $a ( \tau )$ are defined for all rooted trees and characterize the integrator.

Every numerical integrator (including $\mathbf { R - K }$ method) can be expanded into a Bseries as introduced and studied in[HW74] .

Definition 4.1 (rooted tree and forest). The set of rooted tree $T$ and forest $\mathcal { F }$ are defined recursively by

$1 ^ { \circ }$ The tree , only one vertex belong to $T$ ;   
$2 ^ { \circ }$ If $\tau _ { 1 } , \cdots , \tau _ { n }$ are $n$ tree of $\tau$ , the forest $u = \tau _ { 1 } , \cdots , \tau _ { n }$ is the commutative product of $\tau _ { 1 } , \cdots , \tau _ { n }$ ;   
$3 ^ { \circ }$ If $u$ is a forest of $\mathcal { F }$ , then $u = | \tau |$ is a tree of $T$ .

Let $T = \{ \cdot , \cdot , \cdot \} , \nabla , \cdot \cdot \cdot \}$ be the set of rooted trees and let $\varnothing$ be the empty tree. For $\tau _ { 1 } , \cdot \cdot \cdot , \tau _ { n } \in T$ , we denote by $\tau = [ \tau _ { 1 } , \cdots , \tau _ { n } ]$ the tree obtained by grafting the roots of $\tau _ { 1 } , \cdots , \tau _ { n }$ to a new vertex which becomes the root of $\tau$ . Elementary differentials $F _ { f } ( \tau )$ are defined by induction as

$$
F _ { f } ( \bullet ) ( z ) = f ( z ) , \quad F _ { f } ( \tau ) ( z ) = f ^ { ( m ) } ( z ) \big ( F _ { f } ( \tau _ { 1 } ) , \cdot \cdot \cdot , F _ { f } ( \tau _ { m } ) ( z ) \big ) .
$$

For real coefficients $a ( \emptyset )$ and $a ( \tau ) , \tau \in T$ a B-series is a series of the form

$$
B ( f , a , z ) ~ = ~ a ( \emptyset ) I d + \sum _ { \tau \in T } { \frac { h ^ { | \tau | } } { \sigma ( \tau ) } } ~ a ( \tau ) ~ F _ { f } ( \tau ) ( z ) ~
$$

where $I d$ stands for the identity; $I d ( z ) = z$ and the scalars $a ( \tau )$ are the known normalization coefficients[BSS96] . Now, we give following examples:

Example 4.2. The Taylor series of the exact solution of (4.1) can be written as a Bseries $z ( h ) = B ( f , e ) ( z _ { 0 } )$ with coefficients $a ( \tau ) = e ( \tau ) = \frac { 1 } { \gamma ( \tau ) } , \forall \tau \in T .$ .

Example 4.3. The coefficient B-series for explicit Euler scheme $a ( \tau ) = 0 , \forall \tau \in T$ except $a ( \cdot ) = 1$ .

Example 4.4. The coefficient B-series for implicit Euler scheme $a ( \tau ) = 1 , \forall \tau \in T$ .

Example 4.5. The coefficient B-series for centered Euler scheme $\boldsymbol { a } ( \tau ) = \left( \frac { 1 } { 2 } \right) ^ { | \tau | - 1 }$ , $\forall \tau \in T$ .

Example 4.6. The coefficient B-series for trapezoidal scheme $a ( \bullet ) = 1 , a ( \pmb { \zeta } ) =$

$$
{ \frac { 1 } { 2 } } , a ( \pmb { \gamma } ) = { \frac { 1 } { 2 } } , a ( \pmb { \gamma } ) = { \frac { 1 } { 4 } } , \cdots .
$$

Example 4.7. The coefficient B-series for R–K method $( A , b , c ) , a ( \tau ) = b ^ { \mathrm { T } } \phi ( \tau ) , \forall \tau$ $\forall \tau \in$ $T$ .

Partitions and skeletons: A partition $p ^ { \tau }$ of a tree $\tau$ is obtained by cutting some of the edges $\mathrm { [ C H V 0 7 ] }$ . The resulting list of trees is denoted by $P ( p ^ { \tau } )$ . Eventually, the set of all partitions $p ^ { \tau }$ of $\tau$ is denoted by $P ( p ^ { \tau } )$ . Now, given a partition $p ^ { \tau }$ , the corresponding skeleton $\chi ( p ^ { \tau } )$ , as introduced in $[ \mathrm { C H V 0 7 } ]$ , is the tree obtained by contracting each tree of $P ( p ^ { \tau } )$ to a single vertex and by re-establishing the cut edges (see Tables 4.1 – 4.25). We observe that a tree $\tau \in T$ has exactly $2 ^ { | \tau | - \bar { 1 } }$ partitions $p ^ { \tau }$ and that different partitions may lead to the same $P ( p ^ { \tau } )$ . An admissible partition is a partition with at most one cut along any part from the root to any terminal vertex. We denote ${ \mathcal { A } } { \mathcal { P } } ^ { \tau }$ as the set of admissible partition of $\tau$ and by convention, we suppose that $\varnothing \in { \mathcal { A } } { \mathcal { P } } ^ { \tau }$ . We denote $\# ( p ^ { \tau } )$ as number of subtrees. We denote this distinguished tree by $R ( p ^ { \tau } ) ( \operatorname { o r } r _ { p } )$ . We denote $P ^ { * } ( p ^ { \tau } ) = P ( p ^ { \tau } ) \setminus R ( p ^ { \tau } )$ as the list of forest that do not contain the root of $\tau$ . We distinguish $r _ { p }$ as the tree $v _ { p }$ (or $P ( p ^ { \tau } ) )$ whose root coincides with the root of $\tau$ . This tree is usually referred to as a subtree of $\tau$ and we denoted by $v _ { p } ^ { * } \left( \operatorname { o r } P ^ { * } ( p ^ { \tau } ) \right)$ the forest obtained by removing $r _ { p }$ from $v _ { p }$ . The above definition can be seen in Tables 4.1 – 4.25.

# 9.4.1 The Composition Laws

The following theorem result on the composition of B-series was obtained by[HW74] . Now we formulate this theorem in the form [CHV07] :

Theorem 4.8. Let $a , b : T \cup \{ \varnothing \} \to \mathbf { R }$ be two mappings, with $a ( \emptyset ) = 1$ . Then $B$ -series $B ( f , a ) ( z )$ inserted into $B ( f , b ) ( \cdot )$ is still a $B$ -series

$$
B ( f , b ) \big ( B ( f , a ) ( z ) \big ) = B ( f , a \cdot b ) ( z ) ,
$$

and $a \cdot b : T \cup \{ \varnothing \} \to \mathbf { R }$ is defined by

$$
( a \cdot b ) = b ( \emptyset ) = b ( \emptyset ) , \quad \forall \tau \in T , \quad ( a \cdot b ) = \sum _ { p \in A \mathcal { P } ( \tau ) } b ( r _ { p } ) a ( v _ { p } ^ { * } ) ,
$$

where a is extended to $\mathcal { F }$ , as follows:

$$
\forall u = \tau _ { 1 } \cdot \cdot \cdot \tau _ { n } \in \mathcal { F } , \quad a ( u ) = \prod _ { i = 1 } ^ { n } a ( \tau _ { i } ) .
$$

Table 4.1. The partitions of a tree of order 2 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>：</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1>{5</td><td rowspan=1 colspan=1>{5</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0}{}</td><td rowspan=1 colspan=1>{0}{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.2. The partitions of a tree of order 3 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{...)</td></tr><tr><td rowspan=1 colspan=1>R(pT）</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.3. The partitions of a tree of order 3 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>()</td></tr><tr><td rowspan=1 colspan=1>R(（p）</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.4. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1>{0}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.5. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>&gt;</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>丫</td></tr><tr><td rowspan=1 colspan=1>P(p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{M}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>p EAP</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.6. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>.</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.7. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>()</td><td rowspan=1 colspan=1>()</td></tr><tr><td rowspan=1 colspan=1>R(p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{…})</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.8. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(pT）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(pT)</td><td rowspan=1 colspan=1>{0}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.9. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1>\</td><td rowspan=1 colspan=1>\</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pEAPT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.10. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R（p）</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>p ∈AP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.11. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>&gt;</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>）.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{·)}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.12. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(pT）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.13. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>中</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{0)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{..)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.14. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>入</td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.15. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.16. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.17. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（pT)</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{…}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.}</td></tr><tr><td rowspan=1 colspan=1>#（pT）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.18. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>R（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.19. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>心</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>心</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{..)</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.20. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>v</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{0</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.21. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>力</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{..)</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{..}</td></tr><tr><td rowspan=1 colspan=1>#(pT)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.22. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>{v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.23. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.24. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>vv</td><td rowspan=1 colspan=1>vv</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.25. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.:)</td><td rowspan=1 colspan=1>{.:)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1>{W}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td></tr><tr><td rowspan=1 colspan=1>#（p</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

# 9.4.2 Substitution Law

$\mathrm { I n } ^ { \mathrm { [ C H V 0 7 , C H V 0 5 ] } }$ ,they introduce a new composition law on B-series, denoted by $^ *$ and called law of substitution, obtained as a result of the substitution of vector field $g ( z ) =$ $\frac { 1 } { h } B ( f , b ) ( z )$ with $b ( \emptyset ) = 0$ , into another B-series $B ( g , a ) ( z )$ . Chartier, Hairer, and Vilmart give the following theorem:

Theorem 4.9. For $b ( \emptyset ) = 0$ , the vector field $h ^ { - 1 } B ( f , b )$ gives a $B$ -series

$$
B ( h ^ { - 1 } B ( f , b ) , a ) = B ( f , b \ast a ) .
$$

We have $( b * a ) ( \emptyset ) = a ( \emptyset )$ and for all $\tau \in T$ ,

$$
( b \ast a ) ( \tau ) = \sum _ { p \in \mathcal { P } ( \tau ) } a ( \chi _ { p } ) b ( v _ { p } ) ,
$$

where $b$ is extended to $\mathcal { F }$ as follows:

$$
\forall u = \tau _ { 1 } \cdot \cdot \cdot \tau _ { n } \in \mathcal { F } , \quad a ( u ) = \prod _ { i = 1 } ^ { n } a \left( \tau _ { i } \right) .
$$

Remark 4.10. The composition law for the trees of order $\leq 5$ is listed in Example 4.22.

Remark 4.11. The Substitution law for the (backward error) trees of order $\leq 5$ is listed in Example 4.24.

Remark 4.12. The Substitution law for the trees of order $\leq 5$ is listed in Example 4.23.

Modified integrators (called generating function method or preprocessed vector field integrators): Let $\Psi _ { f , h }$ is the exact h-flow for Equation (4.1) which is a B-series with coefficient $e ( \tau ) = \frac { 1 } { \gamma ( \tau ) }$ Consequently, the coefficient $\breve { b } ( \tau )$ of the modified differential equation for $\Phi _ { f , h } = B ( f , a )$ is obtained from

$$
( \breve { b } * a ) ( \tau ) = e ( \tau ) , \quad \forall \tau \in T .
$$

Backward error analysis (called formal vector field, modified equation or postprocessed vector field): The modified differential equation of a method $\Psi _ { f , h } = B ( f , e )$ is obtained by putting $\Phi _ { f , h }$ equal to the exact flow. Its coefficient $\widehat { b } ( \tau )$ is therefore obtained from

$$
( \widehat { b } * e ) ( \tau ) = a ( \tau ) , \quad \forall \tau \in T .
$$

Remark 4.13. Substituting the expression $\frac { 1 } { \gamma }$ given in (4.13) into (4.14) gives $\stackrel { \smile } { b } { * } \widehat { b } { * } a =$ $a$ . Therefore, $\breve { b }$ and $\widehat { b } ( \tau )$ are inverse elements for substitution law $^ *$

$$
\Breve { \boldsymbol { b } } ( \tau ) * \widehat { \boldsymbol { b } } ( \tau ) = \widehat { \boldsymbol { b } } ( \tau ) * \Breve { \boldsymbol { b } } ( \tau ) = \delta _ { \bullet } ( \tau ) .
$$

Proposition 4.14. Using formulae (4.13) and (4.11) in Example 4.23, we easily obtain modified centered Euler scheme of sixth order first find $\ d _ { i n } \mathrm { [ C H V 0 7 ] }$ :

$$
\begin{array} { r c l } { { \dot { z } } } & { { = } } & { { f ( z ) + \displaystyle \frac { h ^ { 2 } } { 2 4 } \big [ f ^ { ( 2 ) } ( f , f ) - 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + \displaystyle \frac { h ^ { 4 } } { 1 2 0 } \big [ \frac { 3 } { 4 8 } f ^ { ( 4 ) } ( f , f , f , f ) } } \\ { { } } & { { } } & { { - \displaystyle \frac { 1 } { 4 } f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ) + \frac { 1 } { 4 } f ^ { ( 2 ) } ( f , f ^ { ( 2 ) } ( f , f ) ) - f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { + \displaystyle \frac { 2 } { 4 } f ^ { ( 2 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) - \frac { 3 } { 1 2 } f ^ { ( 1 ) } f ^ { ( 3 ) } ( f , f , f ) + \displaystyle \frac { 1 } { 2 } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { - \displaystyle \frac { 1 } { 4 } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) + f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + O ( h ^ { 6 } ) . } } \end{array}
$$

Proof. First, we must point out $\breve { b } ( \tau ) = 0 , \forall | \tau | = e v e n$ . We calculate coefficient $\breve { b } (  { \uparrow } )$ as follows

$$
\begin{array} { r l r } & { } & { \check { b } ( \begin{array} { c } { \check { \pmb { \zeta } } } \\ { \check { \pmb { \updownarrow } } } \end{array} ) + 2 a ( \dot { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \pmb { \zeta } ) + a ( \pmb { \gamma } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \dot { \pmb { \zeta } } ) } \\ & { } & { \qquad \vdots } \\ & { } & { + a ( \dot { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \pmb { \zeta } ) + a ( \check { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 5 } = e ( \check { \pmb { \zeta } } ) . } \end{array}
$$

Note the formula in Example 4.23, coefficient $a ( \tau )$ in Example 4.5, and $\gamma ( \tau )$ in Table

4.26, we have $\begin{array} { r } { \check { b } ( \displaystyle \sum _ { i = 0 } ^ { j } + \frac { 1 } { 2 4 } - \frac { 1 } { 1 6 } = \frac { 1 } { 2 4 0 } . } \end{array}$

The proof of others is left to the reader.

Proposition 4.15. In 2001, the author first obtained modified equation for centered Euler scheme given in Example 4.6 of Chapter 7. Using formulas (4.14) and (4.23) in Example 4.24, we can obtain this formula again.

Proof. First, we must point out ${ \widehat b } ( \tau ) = 0 , \forall | \tau | = e v e n$ . We calculate coefficient $\widehat { b } ( \curlyeq \Psi )$ as follows

$$
\widehat { b } ( { \mathbb { V } } ) + 6 e ( { \mathbb { V } } ) \widehat { b } ( \bullet ) ^ { 2 } \widehat { b } ( { \mathbb { V } } ) + \frac { 1 } { \gamma } ( { \mathbb { V } } ) = a ( { \mathbb { V } } ) .
$$

Note the formula in Example 4.22, coefficient $a ( \tau )$ in Example 4.5, and $\gamma ( \tau )$ in Table 4.26, we have $\widehat { b } ( \Psi ) = \frac { 1 } { 1 6 } + \frac { 1 } { 6 } - \frac { 1 } { 5 } = \frac { 7 } { 2 4 0 }$ The proof of others is left to the reader.

Remark 4.16. After calculating the coefficients $\breve { b } ( \tau )$ and $\widehat { b } ( \tau )$ , we list following in Table 4.26.

Remark 4.17. Can directly test following equation

$$
\Breve { b } ( \tau ) * \widehat { b } ( \tau ) = \delta _ { \bullet } ( \tau ) ,
$$

via $^ *$ operation formula (4.11).

Remark 4.18. Relating the previous laws to two Hopf algebra introduced, respectively, by Connes and Kremer[CK98] and by Calaque, Ebrahimi-Fard, and Manchon[CEFM08] , we can see these papers[Bro00],[CHV08]].

Table 4.26. Coefficients $\sigma ( \tau ) , \gamma ( \tau ) , \breve { b } ( \tau )$ , and $\widehat { b } ( \tau )$ for trees of order $\leqslant 5$   

<table><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>！</td></tr><tr><td rowspan=1 colspan=1>g(T)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Y(T)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>6(1)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1/12</td><td rowspan=1 colspan=1>−1/12</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>6()</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>−1/12</td><td rowspan=1 colspan=1>1/12</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>&lt;</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VY</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>?</td></tr><tr><td rowspan=1 colspan=1>g(T)</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>7(T)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>(T)</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>1/120</td><td rowspan=1 colspan=1>-1/80</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>-1/120</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>1/120</td><td rowspan=1 colspan=1>1/240</td></tr><tr><td rowspan=1 colspan=1>6(T)</td><td rowspan=1 colspan=1>7/240</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>-7/240</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>-1/80</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>−1/240</td></tr></table>

# 9.4.3 The Logarithmic Map

The coefficient $\omega ( \tau )$ can be interpreted as the coefficient of the modified field obtained by backward error analysis, for the explicit Euler method $z _ { 1 } = z _ { 0 } + h f ( z _ { 0 } )$ , corresponding to $a = \delta _ { \emptyset } + \delta _ { \bullet }$ . They can be computed by formula (4.11) or (4.22). Murua $\mathrm { i n } ^ { [ \mathrm { M u r 0 6 } ] }$ ∅ •gives the following formula

$$
\begin{array} { r } { \log { ( a ) } = ( a - b _ { \emptyset } ) * \omega . } \end{array}
$$

Properties of logarithmic map has been discussed in Proposition 2.1. Using formula of Example 4.24, determined $\omega ( \tau ) ( = \widehat { b } ( \tau ) )$ recursively , because $a ( \tau ) = 0 \forall \tau \in T$ except $a ( \cdot ) = 1$ .

For example: from 14 formula of Example 4.24, we have

$$
\begin{array} { r l } & { b ( \sqrt [ ] { \textstyle \mathstrut } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 1 2 } ) + ( \frac { 1 } { 2 } ) ( - \frac { 1 } { 2 } ) ( \frac { 1 } { 6 } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 2 } ) ( \frac { 1 } { 3 } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 4 } ) + \frac { 1 } { 6 } ( \frac { 1 } { 6 } ) + 2 ( \frac { 1 } { 6 } ) ( \frac { 1 } { 4 } ) } \\ & { + ( \frac { 1 } { 3 } ) ( \frac { 1 } { 4 } ) + 2 ( \frac { 1 } { 3 } ) ( \frac { 1 } { 3 } ) + ( \frac { 1 } { 2 4 } ) ( - \frac { 1 } { 2 } ) + 3 ( \frac { 1 } { 8 } ) ( - \frac { 1 } { 2 } ) + \frac { 1 } { 3 0 } = 0 , } \end{array}
$$

then we get

$$
\omega ( { \dot { \bigtriangledown } } ) = b ( { \dot { \bigtriangledown } } ) = { \frac { 1 } { 2 0 } } .
$$

The test of others $\omega ( \tau )$ is left the reader.

We give following Table 4.27(compare with [Mur06],[CHV05][CHV08],[CEFM08] ).

Table 4.27. Coefficient $\omega ( \tau )$ for trees of order $\leqslant 5$   

<table><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>w(t)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1/2</td><td rowspan=1 colspan=1>1/6</td><td rowspan=1 colspan=1>1/3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1/12</td><td rowspan=1 colspan=1>-1/6</td><td rowspan=1 colspan=1>-1/4</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>ω(t）-1/30</td><td rowspan=1 colspan=1>ω(t）-1/30</td><td rowspan=1 colspan=1>-1/60</td><td rowspan=1 colspan=1>1/30</td><td rowspan=1 colspan=1>1/30</td><td rowspan=1 colspan=1>1/10</td><td rowspan=1 colspan=1>1/20</td><td rowspan=1 colspan=1>3/20</td><td rowspan=1 colspan=1>1/5</td><td rowspan=1 colspan=1>1/60</td></tr></table>

Definition 4.19. (Lie derivative of B-series) Let $b ( \tau )$ with $b ( \emptyset ) = 0$ and $a ( \tau )$ be the coefficient of two B-series and let $z ( t )$ be a formal solution of the differential equation $h \dot { z } ( t ) = B ( b , z ( t ) )$ . The Lie derivatives of the function $B ( a , z ( t ) )$ with respect to the vector field $B ( b , z ( t ) )$ is again B-series

$$
h \frac { \mathrm { d } } { \mathrm { d } t } B ( a , z ( t ) ) = B ( \partial _ { b } a , z ( t ) ) .
$$

Its coefficients are given by $\partial _ { b } a ( \emptyset ) = 0$ and for $| \tau | \geq 1$ by

$$
\partial _ { b } a ( \tau ) = \sum _ { \theta \in S P ( \tau ) } a ( \theta ) b ( \tau \setminus \theta ) , \quad \partial _ { b } a ( \tau ) = \sum _ { p ^ { \tau } \in \mathcal { P } ( \tau ) } a ( \chi _ { p } ) b ( v _ { p } ) .
$$

Exercise 4.20. [HLW02] Prove that the coefficient of modified differential equation are recursively defined by $b ( \emptyset ) = 0 , b ( \cdot ) = 1$ and

$$
b ( \tau ) = a ( \tau ) - \sum _ { j = 2 } ^ { | \tau | } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) ,
$$

where $\partial _ { b } ^ { j - 1 } b ( \tau )$ is the $( j - 1 )$ -th iterative of the Lie-derivative $\partial _ { b }$ .

Proposition 4.21. The above-mentioned formula (4.20) is just formula $b * \frac { 1 } { \gamma ( \tau ) } =$ $a ( \tau )$ namely

$$
\sum _ { j = 1 } ^ { | \tau | } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) = b ( \tau ) * \frac { 1 } { \gamma ( \tau ) } .
$$

Proof. Note that formula (4.23) in Example 4.24 and Tables 4.1 – 4.25, can obtain this results directly. -

For Example: from 4th formula of Example 4.24, we have

$$
\begin{array}{c} \begin{array} { c }  { e ( \bullet ) b ( \displaystyle \sum _ { \begin{array} { l } { b } \\ { { } \end{array} } + 2 e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \underline { { { \uparrow } } } ) + e ( \displaystyle \sum _ { } ^ { \bullet } ) b ( \bullet ) ^ { 3 } = a ( \displaystyle \sum _ { } ^ { } ) , } } \\ { { b ( \displaystyle \sum _ { \begin{array} { l } { b } \\ { { } \end{array} } + b ( \bullet ) b ( \underline { { { \uparrow } } } ) + \frac { 1 } { 6 } b ( \bullet ) ^ { 3 } = a ( \displaystyle \sum _ { } ^ { } ) , } } \\ { { b ( \displaystyle \sum _ { } ^ { } ) = a ( \displaystyle \sum _ { } ^ { \bullet } ) - b ( \bullet ) b ( \underline { { { \uparrow } } } ) - \frac { 1 } { 6 } b ( \bullet ) ^ { 3 } . } } \end{array} } \end{array}
$$

Example 4.22. The composition laws for the trees of order $\leq 5$ are

$$
\begin{array} { r l } { \alpha _ { 1 } \zeta _ { 2 } } & { = \beta _ { 2 } \zeta _ { 1 } + \frac { 1 } { 2 } - \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 1 } + \frac { 1 } { 8 } \beta _ { 4 } \zeta _ { 2 } } \\ { \gamma _ { 3 } \zeta _ { 2 } } & { = \left. \zeta _ { 2 } \zeta _ { 3 } \right. - \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \alpha _ { 3 } \zeta _ { 2 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \alpha _ { 3 } \zeta _ { 3 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. - 6 \left. \zeta _ { 2 } \zeta _ { 3 } \right. + \frac { 1 } { 8 } \zeta _ { 3 } } \\ { \zeta _ { 4 } } & { = \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. - \frac { 1 } { 8 } \zeta _ { 3 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \beta _ { 4 } \zeta _ { 2 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. + 8 \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. - \beta _ { 4 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + \beta _ { 4 } \zeta _ { 3 } } \\ { \zeta _ { 3 } \zeta _ { 4 } } &  = \beta _ { 3 } \zeta _ { 2 } + \frac   \end{array}
$$$$
\begin{array} { r l } & { \quad \alpha : \forall \mathcal { F } _ { j } = \alpha \mathcal { F } _ { j } \left( \mathcal { F } _ { j } + \mathcal { E } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } \right) } \\ & { \quad = \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } + \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array} { r l } { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \{ \vec { y } \} + b ( \langle \cdot \rangle \cdot a ( \mathbb { Y } ) + b ( \bullet ) \cdot a ( \bigstar ) ) + b ( \bigstar ) \cdot a ( \bullet ) ^ { 2 } } \\ & { \qquad \int } \\ & { \quad + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) } \\ { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \{ \vec { y } \} ) + b ( \bigstar ) \cdot a ( \langle \cdot \rangle + b ( \bullet ) \cdot a ( \bigstar ) + b ( \underline { { Y } } ) \cdot a ( \bigstar ) } \\ & { \qquad \int } \\ & { \qquad + b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) } \\ { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \bigstar ) + b ( \bigstar ) \cdot a ( \bullet ) + b ( \bullet ) \cdot a ( \bullet ) \cdot a ( \mathbb { Y } ) + b ( \bigstar ) \cdot a ( \bullet ) ^ { 2 } } \\ & { \quad + b ( \bigstar ) \cdot a ( \bullet ) + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \cdot ) \cdot a ( \bullet ) \cdot a ( \mathbb { Y } ) + b ( \bigstar ) ^ { 2 } } \\ & { \quad + b ( \bigstar ) \cdot a ( \bullet ) + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) \cdot a ( \mathbb { Y } ) \cdot a ( \mathbb { Y } ) } \end{array}
$$

Example 4.23. The substitution law $^ *$ defined in for the trees of order $\leq 5$ .

$$
 \begin{array} { r l } &   \begin{array} { r l } & { { \lambda } \operatorname { i n } ( t ^ { 2 } ) } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 3 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 5 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 6 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 6 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 5 } ] } \\ & { - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 6 } ] ) } \\ & { - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ) } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ) } \\ &  - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 1 } ] + \operatorname* { m a x } [ t ^ { 1 0 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 1 } ] + \operatorname* { m a x } [ \end{array} \end{array}
$$

$$
\begin{array} { r l } { \Delta x ^ { 2 } \Delta y ( x , y , z ) } & { = \delta ^ { 2 } \Delta y ( x , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z ) ( 2 ) } \\ { \Delta z ( x , y , z ) } & { = \delta ^ { 2 } \Delta z ( x , y , z ) } \\ { \Delta x ^ { 2 } \Delta y ( x , y , z ) } & { = \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z ) - \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z ) - \Delta z ( x , y , z ) \Delta z ( x , y , z ) - \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , y ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ { \Delta z ( x , y , z , z ) } & { = \delta ^ { 2 } \Delta y ( x , y , z , y ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ & { \quad \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \Delta y ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array} { r l } { \varepsilon _ { \perp } } & { = } \\ { \varepsilon _ { \perp } - \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\ { + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ( \varepsilon _ { \perp } ^ { \perp } \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } \\ & { + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } } \\ & { + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ( \varepsilon _ { \perp } ^ { \perp } \Phi _ { 3 } ^ { \perp } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) \varepsilon _ { \perp } ^ { \perp } } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\  \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) + \varepsilon _ { \perp } ( \Phi _  2 \end{array}
$$$$
\begin{array} { r l } { ( \lambda \circ u ) _ { i } ^ { \lambda } } & { = \alpha ( \lambda ^ { 1 } , \theta , \partial \lambda ^ { 2 } ) = \alpha ( \beta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + 2 \alpha ( \beta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } & { = \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } & { = \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) \qquad \quad \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ &  + 2 \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \ \end{array}
$$

Example 4.24. The substitution law $^ *$ defined in for the trees of order $\leq 5$

$$
\begin{array} { r l } & { \delta \neq ( e ^ { - \frac { 1 } { 2 } } - e ^ { - \frac { 1 } { 2 } } ) \delta \neq ( 2 , 1 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } + \frac { 1 } { 2 } ( 2 ) \delta + 1 \right) ^ { 2 } \delta \neq ( 2 ) \delta \neq ( 1 + e ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 1 + e ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ &  \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( 2 ) \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( e ^  \ \end{array}
$$

$$
\begin{array} { r l } { \psi _ { * } \gets ( \boldsymbol { * } ) b ( \dot { \mathcal { V } } ) = } & { e ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { H } } ( \cdot ) b ( \dot { \mathcal { V } } ) ) + ( e ( \cdot ) b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) + ) ^ { 2 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + 4 e ( \cdot \mathbb { V } ) b ( \dot { \mathcal { V } } ) ( b ( \cdot ) ^ { 3 } b ( \dot { \mathcal { V } } ) + e ( \cdot \mathbb { V } ) b ( \dot { \mathcal { V } } ) b ( \cdot ) ^ { 5 } ) } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) = } & { e ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + c ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + 2 c ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) } \\ & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathbb { V } } ) + 2 e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathcal { V } } ) + e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + 2 e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) ^ { 2 } + 2 e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + 2 e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 3 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) } & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 5 } } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) } &  = e ( \cdot ) b ( \dot { \mathcal { V } } ) + 2 e ( \cdot ) b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) + 2 c ( \dot { \mathcal { V } } ) b ( \ \end{array}
$$

$$
\begin{array} { r c l } { { b \ast e \big ( \textstyle { \mathsf { Y } } \big ) } } & { { = } } & { { e ( \bullet ) b ( \textstyle { \mathsf { Y } } ) + e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \textstyle { \mathsf { Y } } ) + 3 e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \textstyle { \mathsf { Y } } ) } } \\ { { } } & { { } } & { { + 3 e ( \textstyle { \mathsf { Y } } ) b ( \bullet ) ^ { 2 } b ( \pmb { \mathsf { Y } } ) + 3 e ( \pmb { \mathsf { Y } } ) b ( \bullet ) ^ { 2 } b ( \textstyle { \mathsf { Y } } ) + e ( \pmb { \mathsf { Y } } ) b ( \bullet ) ^ { 3 } b ( \pmb { \updownarrow } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 3 e ( \textstyle { \mathsf { Y } } ) b ( \bullet ) ^ { 3 } b ( \pmb { \updownarrow } ) + e ( \pmb { \mathsf { Y } } ) _ { b ( \bullet ) ^ { 5 } } } } \end{array}
$$

$$
\begin{array} { r l } { \alpha  \sqrt { \frac { \beta } { \hbar } } } & { = \epsilon + \beta \frac { \hbar } { 8 } ( \frac { 1 } { \hbar } + \epsilon / \hbar ) \epsilon \frac { \hbar } { 2 } \hbar ( 3 + \epsilon / \hbar ) \epsilon ^ { \frac { \beta } { \hbar } } \gamma _ { 1 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\ & { + \epsilon ( \hbar / 8 / 2 3 \epsilon / \hbar ) \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\ & { + \epsilon \frac { \hbar } { 8 } ( \frac { 1 6 } { 1 6 } + \epsilon / \hbar \epsilon ^ { \frac { \beta } { \hbar } } { 1 6 } \epsilon \frac { 1 6 } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\  \alpha  \frac { \hbar } \end{array}
$$

$$
\begin{array} { r l } & { \quad + 4 2 7 5 \times 1 9 7 2 + 4 7 8 7 3 + 1 4 7 9 7 1 + 2 1 7 5 8 7 3 + 1 0 7 1 2 5 } \\ & { \quad + 1 4 7 8 1 4 8 5 8 7 1 + 2 1 2 1 5 1 9 8 1 8 7 8 2 8 1 } \\ & { \quad + 1 4 8 9 1 4 8 5 1 4 7 1 + 2 1 2 1 5 1 9 1 8 7 8 2 8 1 } \\ & { \quad - 1 3 4 0 6 9 9 7 1 1 + 1 4 7 1 9 1 2 + 1 4 1 9 1 1 4 5 1 1 2 1 + 2 1 1 1 4 1 6 1 7 8 4 1 } \\ & { \quad + 1 4 0 6 9 7 1 1 1 4 1 + 2 1 1 4 1 4 1 1 9 1 1 + 3 1 1 1 1 1 4 1 1 1 9 1 1 + 2 1 1 1 1 4 1 0 1 8 1 9 1 } \\ & { \quad + 1 6 8 8 4 1 1 4 1 9 1 1 4 1 + 2 1 1 1 4 1 0 1 4 1 1 + 3 1 1 1 1 4 1 1 4 1 1 1 9 1 1 + 3 1 1 1 1 1 8 1 1 1 } \\ & { \quad + 1 9 7 1 1 1 1 4 1 1 4 1 1 9 1 1 + 3 1 1 1 1 4 1 1 1 1 1 + 3 1 1 1 1 1 4 1 1 1 1 1 + 3 1 1 1 1 1 1 1 1 1 1 1 + 3 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 9 7 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 1 4 1 1 1 1 1 1 1 1 1 1 1 3 1 3 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 } \\ & { \quad - 1 3 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 4 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 } \\ &  \quad + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 +  \end{array}
$$

# Bibliography

[Bak05] H. F. Baker: Alternants and continuous groups. Proc. London Math. Soc., 3:24–47, (1905).   
[Bro00] Ch. Brouder: Runge–Kutta methods and renormalization. Euro. Phys. J. C, 12:521– 534, (2000).   
[BSS96] J. C. Butcher and J. M. Sanz-Serna: The number of conditions for a Runge–Kutta method to have effective order p. Appl. Numer. Math., 22:103–111, (1996).   
[CEFM08] D. Calaque, K. Ebrahimi-Fard, and D. Manchon: Two Hopf algebra of trees interacting. arXiv: 0806.2238 v 2, (2008).   
[CHV05] P. Chartier, E. Hairer, and G. Vilmart: A substitution law for B-series vector fields. Technical Report 5498, INRIA, (2005).   
[CHV07] P. Chartier, E. Hairer, and G. Vilmart: Numerical integration based on modified differential equations. Math. Comp., 76(260):1941–1953, (2007).   
[CHV08] P. Chartier, E. Hairer, and G Vilmart: Composing and substituting S-series and Bseries of integrators and vector fields. Preprint, www.irisa.fr/ipso/fichiers/algebraic.pdf, (2008).   
[CK98] A. Connes and D. Kreimer: Hopf algebra, renormazation and noncommutative geometry. Communications in Mathematical Physics, 199:203–242, (1998).   
[Dyn46] E. B. Dynkin: Normed Lie algebra and analytic groups, volume 1. Amer. Math. Soc. (translation), (1946).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen92] K. Feng: Formal power series and numerical methods for differential equations. In T. Chan and Z. C. Shi, editors, International conf. on scientific computation, pages 28–35. World Scientific, Singapore, (1992).   
[Fen93a] K. Feng: Formal dynamical systems and numerical algorithms. In K. Feng and Z. C. Shi, editors, International conf. on computation of differential equations and dynamical systems, pages 1–10. World Scientific, Singapore, (1993).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C. Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equations and dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[Hai94] E. Hairer: Backward analysis of numerical integrators and symplectic methods. Annals of Numer. Math., 1:107–132, (1994).   
[Hau06] F. Hausdorff: Die symbolische exponentialformel in der gruppentheorie. Berichte der Sachsischen Akad. der Wissensch., 58:19–48, (1906).   
[HLW02] E. Hairer, Ch. Lubich, and G. Wanner: Geometric Numerical Integration. Number 31 in Springer Series in Computational Mathematics. Springer-Verlag, Berlin, (2002).   
[HW74] E. Hairer and G. Wanner: On the Butcher group and general multivalue methods. Computing, 13:1–15, (1974).   
[Lie88] S. Lie; Zur theorie der transformationsgruppen. Christiania, Gesammelte Abh., Christ. Forh. Aar., 13, (1988).   
[Mur06] A. Murua: The Hopf algebra of rooted trees, free Lie algebra, and Lie series. Foundations of Computational Mathematics, 6(4):387–426, (2006).   
[Olv93] P. J. Olver: Applications of Lie Groups to Differential Equations. GTM 107. Springer-Verlag, Berlin, Second edition, (1993).   
[Ote91] J. A. Oteo: The Baker–Campbell–Hausdorff formula and nested commutator identities. J. of Math. Phys., 32(2):419–424, (1991).   
[OW00] B. Owren and B. Welfert: The Newton iteration on Lie groups. BIT, 40(1):121–145, (2000).   
[Owr06] B. Owren: Order conditions for commutator-free Lie group methods. J. Phys. A: Math. Gen., 39:5585–5599, (2006).   
[Rei99] S. Reich: Backward error analysis for numerical integrators. SIAM J. Numer. Anal., 36:475–491, (1999).   
[SS96] J. M. Sanz-Serna: Backward Error Analysis for Symplectic Integrators. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 193–206. American Mathematical Society, New York, (1996).   
[SS97] J. M. Sanz-Serna: Geometric integration. In The State of the Art in Numerical Analysis (York, 1996), volume 63 of Inst. Math. Appl. Conf. Ser. New Ser., pages 121–143, Oxford Univ. Press, New York, (1997).
