# 102 A problem arising from the method of lines

The second initial value problem we consider is based on an approximation to a partial differential equation. Consider the parabolic system

$$
\frac { \partial u } { \partial t } = \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } , \qquad ( x , t ) \in [ 0 , 1 ] \times [ 0 , \infty ) ,
$$

where we have used $t$ to represent time, $x$ to represent distance and $\boldsymbol { u } ( \boldsymbol { x } , t )$ t o represent some quantity, such as temperature, which diffuses with time. For this problem it is necessary to impose conditions on the boundaries $x = 0$ and $x = 1$ as well as at the initial time $t = 0$ . We may interpret the solution as the distribution of the temperature at points in a conducting rod, given that the temperature is specified at the ends of the rod. In this case the boundary conditions would be of the form $u ( 0 , t ) = \alpha ( t )$ and $u ( 1 , t ) = \beta ( t )$ . Equation (102a) is known as the heat or diffusion equation, and the conditions given at $x = 0$ and $x = 1$ are known as Dirichlet boundary values. This is in contrast to Neumann conditions, in which the values of $\partial u / \partial x$ are given at the ends of the $x$ interval.

To convert this problem into an ordinary differential equation system, which denote the values of mimics the behaviour of the parabolic equation, let $\begin{array} { r } { u ( \frac { 1 } { N + 1 } , t ) , u ( \frac { 2 } { N + 1 } , t ) , \dots , u ( \frac { N } { N + 1 } , t ) } \end{array}$ $y _ { 1 } ( t ) , y _ { 2 } ( t ) , \dotsc , y _ { N } ( t )$ , respectively. That is, ,

$$
y _ { j } ( t ) = u \left( { \frac { j } { N + 1 } } , t \right) , \qquad j = 0 , 1 , 2 , \ldots , N + 1 ,
$$

where we have included $y _ { 0 } ( t ) = u ( 0 , t )$ , $y _ { N + 1 } ( t ) = u ( 1 , t )$ for convenience.

For $j = 1 , 2 , \dots , N$ , $\partial ^ { 2 } u / \partial x ^ { 2 }$ , evaluated at $x = j / ( N + 1 )$ , is approximately equal to $( N + 1 ) ^ { 2 } ( y _ { j - 1 } - 2 y _ { j } + y _ { j + 1 } )$ . Hence, the vector of derivatives of $y _ { 1 } , y _ { 2 } , \dotsc , y _ { N }$ is given by

$$
\begin{array} { l } { \frac { d y _ { 1 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( \alpha ( t ) - 2 y _ { 1 } ( t ) + y _ { 2 } ( t ) \big ) , } \\ { \frac { d y _ { 2 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { 1 } ( t ) - 2 y _ { 2 } ( t ) + y _ { 3 } ( t ) \big ) , } \\ { \frac { d y _ { 3 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { 2 } ( t ) - 2 y _ { 3 } ( t ) + y _ { 4 } ( t ) \big ) , } \\ { \vdots } \\ { \frac { d y _ { N - 1 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { N - 2 } ( t ) - 2 y _ { N - 1 } ( t ) + y _ { N } ( t ) \big ) , } \\ { \frac { d y _ { N } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { N - 1 } ( t ) - 2 y _ { N } ( t ) + \beta ( t ) \big ) . } \end{array}
$$

This system can be written in vector–matrix form as

$$
y ^ { \prime } ( t ) = A y ( t ) + v ( t ) ,
$$

where

$$
= ( N + 1 ) ^ { 2 } { \left[ \begin{array} { l l l l l l l l } { - 2 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 1 } & { - 2 } & { 1 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - 2 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } & { - 2 } \end{array} \right] } , \quad v = ( N + 1 ) ^ { 2 } { \left[ \begin{array} { l } { \alpha ( t ) } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 0 } \\ { \beta ( t ) } \end{array} \right] } .
$$

The original problem is ‘dissipative’ in the sense that, if $u$ and $\boldsymbol { v }$ are each solutions to the diffusion equation, which have identical boundary values but different initial values, then

$$
W ( t ) = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \big ( u ( x , t ) - v ( x , t ) \big ) ^ { 2 } d x
$$

is non-increasing as $t$ increases. We can verify this by differentiating with respect to $t$ and by showing, using integration by parts, that the result found

cannot be positive. We have

$$
\begin{array} { r l } & { \frac { d W } { d t } = \displaystyle \int _ { 0 } ^ { 1 } \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial u ( x , t ) } { \partial t } - \frac { \partial v ( x , t ) } { \partial t } \right) d x } \\ & { \quad \quad = \displaystyle \int _ { 0 } ^ { 1 } \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial ^ { 2 } u ( x , t ) } { \partial x ^ { 2 } } - \frac { \partial ^ { 2 } v ( x , t ) } { \partial x ^ { 2 } } \right) d x } \\ & { \quad \quad = \displaystyle \left[ \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) \right] _ { 0 } ^ { 1 } } \\ & { \qquad \quad \quad \quad - \displaystyle \int _ { 0 } ^ { 1 } \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) ^ { 2 } d x } \\ & { \quad \quad \quad = - \displaystyle \int _ { 0 } ^ { 1 } \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) ^ { 2 } d x } \\ & { \quad \quad \quad \le 0 . } \end{array}
$$

Even though the approximation of (102a) by (102b) is not exact, it is an advantage of the discretization we have used, that the qualitative property is still present. Let $y$ and $z$ be two solutions to the ordinary differential equation system. Consider the nature of

$$
\widehat W ( t ) = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ^ { 2 } .
$$

We have

$$
\begin{array} { l } { \displaystyle \frac { d \widehat { W } } { d t } = \sum _ { i = 1 } ^ { N } ( y _ { j } - z _ { j } ) \left( \frac { d y _ { j } } { d t } - \frac { d z _ { j } } { d t } \right) } \\ { \displaystyle \quad = ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ( y _ { j - 1 } - 2 y _ { j } + y _ { j + 1 } - z _ { j - 1 } + 2 z _ { j } - z _ { j + 1 } ) } \\ { \displaystyle \quad = 2 ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N - 1 } ( y _ { j } - z _ { j } ) ( y _ { j + 1 } - z _ { j + 1 } ) - 2 ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ^ { 2 } } \\ { \displaystyle \quad = - ( N + 1 ) ^ { 2 } \sum _ { j = 0 } ^ { N } ( y _ { j + 1 } - y _ { j } - z _ { j + 1 } + z _ { j } ) ^ { 2 } } \\ { \displaystyle \quad \leq 0 . } \end{array}
$$

Another aspect of the discretization that might be explored is the spectrum of the matrix $A$ , in comparison with the spectrum of the linear operator $u \mapsto { \frac { d ^ { 2 } u } { d x ^ { 2 } } }$ on the space of $C ^ { 2 }$ functions on $[ 0 , 1 ]$ for which $u ( 0 ) = u ( 1 ) = 0$ . The eigenfunctions for the continuous problem are of the form $\sin ( k \pi x )$ , for $k = 1 , 2 , 3 , \ldots$ and the corresponding eigenvalues are $- k ^ { 2 } \pi ^ { 2 }$ . For the discrete problem, we need to find the solutions to the problem

$$
( A - \lambda I ) \left[ \begin{array} { c } { v _ { 1 } } \\ { v _ { 2 } } \\ { \vdots } \\ { v _ { N } } \end{array} \right] = 0 ,
$$

where $v _ { 1 }$ , $v _ { 2 }$ , $\cdot \cdot \cdot$ , $v _ { N }$ are not all zero. Introducing also $v _ { 0 } = v _ { N + 1 } = 0$ , we find that it is possible to write (102c) in the form

$$
v _ { j - 1 } - q v _ { j } + v _ { j + 1 } = 0 , \qquad j = 1 , 2 , \ldots , N ,
$$

where $q = 2 + \lambda / ( N + 1 ) ^ { 2 }$ . The difference equation (102d) has solution of the form $v _ { i } = C ( \mu ^ { i } - \mu ^ { - i } )$ , where $\mu + \mu ^ { - 1 } = q$ , unless $q = \pm 2$ (which is easily seen to be impossible). Because $v _ { N + 1 } = 0$ , it follows that $\lambda ^ { 2 N + 2 } = 2$ . Because $\mu \neq \pm 1$ , it follows that

$$
\mu = \exp \left( \frac { k \pi i } { N + 1 } \right) , \qquad k = 1 , 2 , \ldots , N ,
$$

with $i = \sqrt { - 1 }$ . Hence,

$$
\lambda = - 2 ( N + 1 ) ^ { 2 } \left( 1 - \cos \left( \frac { k \pi } { N + 1 } \right) \right) = - 4 ( N + 1 ) ^ { 2 } \sin ^ { 2 } \left( \frac { k \pi } { 2 N + 2 } \right) .
$$

For $N$ much larger than $k$ , we can use the approximation $\sin ( \xi ) \approx \xi$ , for small $\xi$ , to give eigenvalue number $k$ as $\lambda _ { k } \approx - k ^ { 2 } \pi ^ { 2 }$ . On the other hand, for $k$ small, the eigenvalue number $N + 1 - k$ is $\lambda _ { N + 1 - k } \approx - 4 ( N + 1 ) ^ { 2 } + k ^ { 2 } \pi ^ { 2 }$ .
