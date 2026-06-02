$$
\frac { d x _ { i } } { d t } = \frac { \partial F } { \partial y _ { i } } , \frac { d y _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

$$
{ \cal F } = { \cal F } _ { 0 } + \mu { \cal F } _ { 1 } + \mu ^ { 2 } { \cal F } _ { 2 } + \cdots ,
$$

where $F _ { 0 }$ is a function of $x _ { 1 } , \ldots , x _ { n }$ only and $F _ { 1 } , F _ { 2 } , \dots$ are periodic with period $2 \pi$ with regard to $y _ { 1 } , \ldots , y _ { n }$ with functions of $x _ { 1 } , \ldots , x _ { n }$ as coefficients,and $\mu$ is a small parameter.We propose to satisfy these equations by formal series (Poincaré,1886a,1889a,1892,1893)

$$
\begin{array} { r } { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { n } x _ { i } ^ { ( n ) } + \cdot \cdot \cdot , } \\ { y _ { i } = y _ { i } ^ { ( 0 ) } + \mu y _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { n } y _ { i } ^ { ( n ) } + \cdot \cdot \cdot , } \end{array}
$$

with

$$
\begin{array} { l } { { \displaystyle x _ { i } ^ { ( k ) } = \sum _ { i } A \cos h t + \sum _ { } B \sin h t + E , } } \\ { { \displaystyle y _ { i } ^ { ( k ) } = \sum _ { i } A ^ { \prime } \cos h t + \sum _ { } B ^ { \prime } \sin h t + E ^ { \prime } t + D ^ { \prime } , } } \end{array}
$$

where $A , B , E , A ^ { \prime } , B ^ { \prime } , E ^ { \prime } , D ^ { \prime }$ ,being functions of the integration constants，are independent of $\mu$ and $t$ ，and $h$ depends on $\pmb { \mu }$ and is developable in powers of $\mu$ . If the equations (28） are satisfied up to the order $\mu ^ { p }$ when (29) are substituted, then

$$
\begin{array} { r l } & { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } x _ { i } ^ { ( p ) } , } \\ & { y _ { i } = y _ { i } ^ { ( 0 ) } + \mu y _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } y _ { i } ^ { ( p ) } } \end{array}
$$

are the formal solution of (28) up to the order $\mu ^ { p }$

Put

$$
S = S _ { 0 } + \mu S _ { 1 } + \cdot \cdot \cdot + \mu ^ { p } S _ { p } + \cdot \cdot \cdot ,
$$

where

$$
S _ { k } = \alpha _ { k 1 } y _ { 1 } + \alpha _ { k 2 } y _ { 2 } + \cdot \cdot \cdot + \alpha _ { k n } y _ { n } + \phi _ { k } ,
$$

with disposable constants $\alpha _ { i k }$ ， and with periodic functions $\phi _ { k }$ with period $2 \pi$ with regard to $y _ { 1 } , \ldots , y _ { n }$ . We try to satisfy formally the Hamilton-Jacobi equation

$$
F \Big ( \frac { \partial S } { \partial y _ { 1 } } , \frac { \partial S } { \partial y _ { 2 } } , \ldots , \frac { \partial S } { \partial y _ { n } } , y _ { 1 } , y _ { 2 } , \ldots , y _ { n } \Big ) = C ,
$$

with

$$
C = C _ { 0 } + \mu C _ { 1 } + \cdots + \mu ^ { p } C _ { p } + \cdots .
$$

By expanding both sides of (31) in powers of $\pmb { \mu }$ we obtain at first

$$
F _ { \boldsymbol 0 } \big ( \frac { \partial S _ { \boldsymbol 0 } } { \partial y _ { 1 } } , \dots , \frac { \partial S _ { \boldsymbol 0 } } { \partial y _ { n } } \big ) = C _ { \boldsymbol 0 } .
$$

This equation is satisfied by

$$
S _ { 0 } = x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } y _ { 1 } + x _ { 2 } ^ { \scriptscriptstyle ( 0 ) } y _ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { \scriptscriptstyle ( 0 ) } y _ { n } ,
$$

$$
\frac { \partial S _ { 0 } } { \partial y _ { 1 } } = x _ { 1 } ^ { ( 0 ) } , \ldots , \frac { \partial S _ { 0 } } { \partial y _ { n } } = x _ { n } ^ { ( 0 ) } ,
$$

where $x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$ are arbitrary constants depending on $C _ { \mathfrak { o } }$ . Put

$$
n _ { i } ^ { \left( 0 \right) } = - \frac { \partial F } { \partial x _ { i } ^ { \left( 0 \right) } } ;
$$

then the equation for $S _ { p }$ can be written

$$
n _ { 1 } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 1 } } + n _ { 2 } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 2 } } + \cdot \cdot \cdot + n _ { n } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { n } } = \Phi _ { p } + C _ { p } ,
$$

where $\Phi _ { p }$ contains the derivatives of $S _ { 0 } , S _ { 1 } , \ldots , S _ { p - 1 }$ with regard to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ ，and the coefficients of these derivatives are functions of $x _ { 1 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$ . The function $\Phi _ { p }$ is periodic with period $2 \pi$ with regard to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ . The function $S _ { p }$ can be determined successively，as can be proved by mathematical induction (Poincaré, 1893), such that its derivatives with regard to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ are periodic with period $2 \pi$ with regard to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ If $\Phi _ { p }$ ， being periodic with respect to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n } ,$ ,is written in the form

$$
\Phi _ { p } = A + \sum { B \cos { ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) } }
$$

$$
+ \sum \bar { B } \sin { ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) } ,
$$

then the solution is

$$
\begin{array} { l } { S _ { p } = \alpha _ { p 1 } y _ { 1 } + \cdot \cdot \cdot + \alpha _ { p n } y _ { n } } \\ { \displaystyle ~ + \sum \frac { B \sin { ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) } } { m _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + m _ { n } n _ { n } ^ { ( 0 ) } } } \\ { \displaystyle ~ - \sum \frac { \bar { B } \cos { ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) } } { m _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + m _ { n } n _ { n } ^ { ( 0 ) } } , } \end{array}
$$

with

$$
\alpha _ { p 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + \alpha _ { p n } n _ { n } ^ { ( 0 ) } = A + C _ { p } ,
$$

where we assume that there is no linear homogeneous relation with integer coefficients of the form

$$
\sum _ { i } m _ { i } n _ { i } ^ { \left( 0 \right) } = 0 .
$$

Among the arbitrary constants $x _ { i } ^ { ( 0 ) } , \alpha _ { 1 i } , \alpha _ { 2 i } , \ldots , \alpha _ { p i } ( i = 1 , 2 , \ldots , n )$ ， we choose $x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$ as the independent integration constants. We choose $\alpha _ { i k }$ all equal to zero. Then $C _ { 1 } , C _ { 2 } , \ldots , C _ { p }$ are functions of $C _ { 0 } , x _ { 1 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$

Let

$$
\Sigma _ { p } = S _ { 0 } + \mu S _ { 1 } + \cdot \cdot \cdot + \mu ^ { p } S _ { p } ,
$$

and

$$
\begin{array} { r } { \frac { \partial \Sigma _ { p } } { \partial y _ { i } } = x _ { i } , \qquad \frac { \partial \Sigma _ { p } } { \partial x _ { i } ^ { ( 0 ) } } = w _ { i } , } \end{array}
$$

and take $x _ { i } ^ { ( 0 ) }$ and $w _ { i }$ as the new canonical variables, then we obtain

$$
\frac { d x _ { i } ^ { \scriptscriptstyle ( 0 ) } } { d t } = \frac { \partial F } { \partial w _ { i } } , \qquad \frac { d w _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } .
$$

By our construction $S _ { p }$ satisfies (31) formally:

$$
F ( x _ { i } , y _ { i } ) = F \Big ( \frac { \partial \Sigma _ { p } } { \partial y _ { i } } , y _ { i } \Big ) = C _ { 0 } + \mu C _ { 1 } + \cdot \cdot \cdot + \mu ^ { p } C _ { p } + \mu ^ { p + 1 } \Phi _ { p } ,
$$

where $\Phi _ { p }$ is a function of $x _ { i } ^ { ( 0 ) } , w _ { i }$ and $\pmb { \mu }$ ,and is developable in powers of $\mu$ ,in which $C _ { \mathfrak { o } } , C _ { 1 } , \ldots , C _ { p }$ are functions of $x _ { i } ^ { ( 0 ) }$ . Put

$$
\begin{array} { r } { \nu _ { i } ^ { ( p ) } = - \frac { \partial C _ { 0 } } { \partial x _ { i } ^ { ( 0 ) } } - \mu \frac { \partial C _ { 1 } } { \partial x _ { i } ^ { ( 0 ) } } - \cdot \cdot \cdot - \mu ^ { p } \frac { \partial C _ { p } } { \partial x _ { i } ^ { ( 0 ) } } ; } \end{array}
$$

then we get

$$
\frac { d x _ { i } ^ { ( 0 ) } } { d t } = \mu ^ { p + 1 } \frac { \partial \Phi _ { p } } { \partial w _ { i } } , \qquad \frac { d w _ { i } } { d t } = \nu _ { i } ^ { ( p ) } - \mu ^ { p + 1 } \frac { \partial \Phi _ { p } } { \partial x _ { i } ^ { ( 0 ) } } .
$$

If we neglect quantities of order $\mu ^ { p + 1 }$ and higher,then we obtain integrals

$$
x _ { i } ^ { \scriptscriptstyle ( 0 ) } = \mathrm { c o n s t a n t } , \qquad w _ { i } = \upsilon _ { i } ^ { \scriptscriptstyle ( p ) } t + \varpi _ { i } .
$$

This result is substituted in

$$
\frac { \partial S } { \partial y _ { i } } = x _ { i } , \qquad \frac { \partial S } { \partial x _ { i } ^ { ( 0 ) } } = w _ { i } ,
$$

then the solution $x _ { i } , y _ { i }$ are obtained in the form developed in powers of $\mu$ with functions of $\boldsymbol { x } _ { i } ^ { ( 0 ) }$ and $w _ { i }$ as coefficients, up to the order $\mu ^ { p }$ ， in which $x _ { i } ^ { \scriptscriptstyle ( 0 ) }$ and $w _ { i }$ are integration constants. (35) are written

$$
x _ { i } = x _ { i } ^ { \scriptscriptstyle ( 0 ) } + \frac { \partial ( \Sigma _ { p } - S _ { 0 } ) } { \partial y _ { i } } , \qquad y _ { i } = w _ { i } + \frac { \partial ( \Sigma _ { p } - S _ { 0 } ) } { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } .
$$

Thus $x _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ in (29)are periodic with period $2 \pi$ with regard to $w _ { i }$ ·

The series (29) can be written

$$
\begin{array} { r l } & { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu \phi _ { i } ( w _ { k } , x _ { k } ^ { ( 0 ) } , \mu ) , } \\ & { y _ { i } = y _ { i } ^ { ( 0 ) } + \mu \psi _ { i } ( w _ { k } , x _ { k } ^ { ( 0 ) } , \mu ) . } \end{array}
$$

Poincaré (1893) proved that this solution can also be written

$$
\begin{array} { r l } & { x _ { i } = x _ { i } ^ { 0 } + \mu [ v _ { i } + \phi _ { i } ( w _ { k } + \mu \omega _ { k } , x _ { k } ^ { 0 } + \mu v _ { k } , \mu ) ] , } \\ & { y _ { i } = w _ { i } + \mu [ \omega _ { i } + \psi _ { i } ( w _ { k } + \mu \omega _ { k } , x _ { k } ^ { 0 } + \mu v _ { k } , \mu ) ] , } \end{array}
$$

where $\omega _ { i }$ and $v _ { i }$ are $_ { 2 n }$ functions of $x _ { i } ^ { ( 0 ) }$ and $\pmb { \mu }$ ，and developable in powers of $\mu$ . The functions $\phi _ { i } ( w _ { k } , x _ { k } ^ { ( 0 ) } , \mu )$ and $\psi _ { i } ( w _ { k } , x _ { k } ^ { ( 0 ) } , \mu )$ are periodic in $w _ { i }$ ，so that $v _ { i } + \phi _ { i } ( w _ { k } + \mu \omega _ { k } , x _ { k } ^ { \scriptscriptstyle ( 0 ) } + \mu v _ { k } , \mu )$ and $\omega _ { i } + \psi _ { i } ( w _ { k } \ +$ $\mu \omega _ { k } , x _ { k } ^ { ( 0 ) } + \mu v _ { k } , \mu )$ are periodic in $w _ { i }$ . These functions can be proved to be respectively equal to $\theta _ { i }$ and $\eta _ { i }$ ，where $\theta _ { i }$ and $\eta _ { i }$ are $_ { 2 n }$ arbitrarily chosen functions of $x _ { i } ^ { ( 0 ) }$ and $\mu$ developable in powers of $\pmb { \mu }$ . Thus the solution can be written

$$
\begin{array} { l } { { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \mu ^ { 2 } x _ { i } ^ { ( 2 ) } + \cdots , } } \\ { { y _ { i } = w _ { i } + \mu y _ { i } ^ { ( 1 ) } + \mu ^ { 2 } y _ { i } ^ { ( 2 ) } + \cdots , } } \end{array}
$$

in which $\boldsymbol { x } _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ are periodic functions of $w _ { i }$ . Hence we can arrange so that the mean values of the periodic functions $x _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ are arbitrary functions of $\boldsymbol { x } _ { i } ^ { ( 0 ) }$

We have seen that, when the variables $x _ { i }$ and $y _ { i }$ are substituted from (37), the derivatives $\partial F / \partial y _ { i }$ are functions of $x _ { i } ^ { ( 0 ) } , x _ { i } ^ { ( k ) } , w _ { i } , y _ { i } ^ { ( k ) }$ ， and are developable in powers of $\mu$ and periodic with regard to $w _ { i }$ We have

$$
\frac { \partial F } { \partial y _ { i } } = X _ { i } ^ { \scriptscriptstyle ( 0 ) } + \mu X _ { i } ^ { \scriptscriptstyle ( 1 ) } + \cdot \cdot \cdot + \mu ^ { k } X _ { i } ^ { \scriptscriptstyle ( k ) } + \cdot \cdot \cdot .
$$

Similarly we have

$$
- \frac { \partial F } { \partial x _ { i } } = Y _ { i } ^ { \scriptscriptstyle ( 0 ) } + \mu Y _ { i } ^ { \scriptscriptstyle ( 1 ) } + \dots + \mu ^ { k } Y _ { i } ^ { \scriptscriptstyle ( k ) } + \dots .
$$

Write

$$
n _ { i } = n _ { i } ^ { ( 0 ) } + \mu n _ { i } ^ { ( 1 ) } + \mu ^ { 2 } n _ { i } ^ { ( 2 ) } + \cdots ;
$$

then we have

$$
\sum _ { k } n _ { k } { \frac { \partial x _ { i } } { \partial w _ { k } } } = { \frac { \partial F } { \partial y _ { i } } } , \qquad \sum _ { k } n _ { k } { \frac { \partial y _ { i } } { \partial w _ { k } } } = - { \frac { \partial F } { \partial x _ { i } } } .
$$

By substituting the above expansions of $\partial F / \partial y _ { i } , - \partial F / \partial x _ { i }$ and $n _ { i }$ we derive the equations (Poincaré,1905)

$$
\begin{array} { r l } & { \displaystyle \sum _ { \ k } \ n _ { k } ^ { ( 0 ) } \ \frac { \partial x _ { i } ^ { ( p ) } } { \partial w _ { k } } = X _ { i } ^ { ( p ) } + Z _ { i } ^ { ( p ) } - \displaystyle \sum _ { k } \ n _ { k } ^ { ( p ) } \frac { \partial x _ { i } ^ { ( 0 ) } } { \partial w _ { k } } , } \\ & { \displaystyle \sum _ { k } \ n _ { k } ^ { ( 0 ) } \frac { \partial y _ { i } ^ { ( p ) } } { \partial w _ { k } } = Y _ { i } ^ { ( p ) } + T _ { i } ^ { ( p ) } - \displaystyle \sum _ { k } \ n _ { k } ^ { ( p ) } \frac { \partial y _ { i } ^ { ( 0 ) } } { \partial w _ { k } } , } \end{array}
$$

where

$$
\begin{array} { r l r } { \displaystyle \sum _ { k = 1 } ^ { n } \sum _ { q = 1 } ^ { p - 1 } n _ { k } ^ { ( q ) } \frac { \partial x _ { i } ^ { ( p - q ) } } { \partial w _ { k } } = - Z _ { i } ^ { ( p ) } } & { \ ( p > 1 ) , } & { \ Z _ { i } ^ { ( 1 ) } = 0 , } \\ { \displaystyle \sum _ { k = 1 } ^ { n } \sum _ { q = 1 } ^ { p - 1 } n _ { k } ^ { ( q ) } \frac { \partial y _ { i } ^ { ( p - q ) } } { \partial w _ { k } } = - T _ { i } ^ { ( p ) } } & { \ ( p > 1 ) , } & { \ T _ { i } ^ { ( 1 ) } = 0 . } \end{array}
$$

We obtain at first

$$
\sum _ { k } \ n _ { k } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } { \partial w _ { k } } = 0 , ~ \sum _ { k } \ n _ { k } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial y _ { i } ^ { \scriptscriptstyle ( 0 ) } } { \partial w _ { k } } = n _ { i } ^ { \scriptscriptstyle ( 0 ) } ,
$$

whence we get

$$
x _ { i } ^ { \scriptscriptstyle ( 0 ) } = \mathrm { c o n s t a n t } , \qquad y _ { i } ^ { \scriptscriptstyle ( 0 ) } = w _ { i } .
$$

Next we have

$$
\begin{array} { r l } & { \displaystyle \sum _ { k } { n _ { k } ^ { ( 0 ) } \frac { \partial { x _ { i } ^ { ( p ) } } } { \partial { w _ { k } } } = X _ { i } ^ { ( p ) } + Z _ { i } ^ { ( p ) } } , } \\ & { \displaystyle \sum _ { k } { n _ { k } ^ { ( 0 ) } \frac { \partial { y _ { i } ^ { ( p ) } } } { \partial { w _ { k } } } = Y _ { i } ^ { ( p ) } + T _ { i } ^ { ( p ) } - n _ { i } ^ { ( p ) } } . } \end{array}
$$

The functions $x _ { i } ^ { ( { p } ) }$ and $y _ { i } ^ { ( { p } ) }$ can be obtained so that they are periodic with respect to $w _ { i }$ and their mean values are arbitrary functions of $\boldsymbol { x } _ { k } ^ { ( 0 ) }$ . In fact, let

$$
X _ { i } ^ { \scriptscriptstyle ( p ) } + Z _ { i } ^ { \scriptscriptstyle ( p ) } = \sum A \cos ( m _ { 1 } w _ { 1 } + \cdot \cdot \cdot + m _ { n } w _ { n } + h ) ,
$$

then we obtain

$$
x _ { i } ^ { ( p ) } = \sum \frac { A \sin { ( m _ { 1 } w _ { 1 } + \cdot \cdot \cdot + m _ { n } w _ { n } + h ) } } { m _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + m _ { n } n _ { n } ^ { ( 0 ) } } + K _ { i } ^ { ( p ) } ,
$$

provided that there is no relation of the form (34),by choosing the mean values of $X _ { i } ^ { ( p ) } + Z _ { i } ^ { ( p ) }$ equal to zero,where the $K _ { i } ^ { ( { \mathcal { P } } ) }$ are arbitrary functions of $x _ { k } ^ { ( 0 ) }$ .The $y _ { i } ^ { ( { \mathfrak { p } } ) }$ can be obtained ina similar form by choosing the mean values of $Y _ { i } ^ { ( p ) } + T _ { i } ^ { ( p ) } - n _ { i } ^ { ( p ) }$ equal to zero. Thus the solution can be obtained by taking $n _ { i } ^ { ( p ) } \neq 0$ and by modifying the values of $\pmb { n } _ { i }$ at each approximation in the form (38). This is the essence of the theory of Newcomb (Section 14.4） and Lindstedt (Sections 12.5, 14.5).

However, we meet a difficulty when ${ \pmb F }$ depends only on $x _ { 1 }$ and $x _ { 2 }$ but is independent of $x _ { 3 } , \ldots , x _ { n }$ ,as in the three-body problem.In such a case we have the relation (34) in the form $n _ { 3 } ^ { ( 0 ) } = \cdots = n _ { n } ^ { ( 0 ) } = 0$ Take $n = 3$ ,as in the case of the restricted problem of three bodies. Then $F _ { 0 }$ is a function of $x _ { 1 }$ and $x _ { 2 }$ only,but does not depend on $x _ { 3 }$ We have $n _ { 3 } ^ { \scriptscriptstyle ( 0 ) } = - ( \partial { \cal F } / \partial x _ { 3 } ^ { \scriptscriptstyle ( 0 ) } ) = 0$ . Take the mean value of $\boldsymbol { F } _ { 1 }$ with respect to $y _ { 1 }$ and $y _ { 2 }$ and denote it by $\pmb R$ .Here $\pmb R$ may be a function of $x _ { 1 } , x _ { 2 } , x _ { 3 }$ and $y _ { 3 }$

At first suppose that $\pmb R$ does not depend on $y _ { 3 }$ . We require the solution of

$$
F \Big ( \frac { \partial S } { \partial y _ { 1 } } , \frac { \partial S } { \partial y _ { 2 } } , \frac { \partial S } { \partial y _ { 3 } } , y _ { 1 } , y _ { 2 } , y _ { 3 } \Big ) = C ,
$$

where

$$
\begin{array} { c } { { S = S _ { 0 } + \mu S _ { 1 } + \mu ^ { 2 } S _ { 2 } + \cdots , } } \\ { { C = C _ { 0 } + \mu C _ { 1 } + \mu ^ { 2 } C _ { 2 } + \cdots . } } \end{array}
$$

The zero-th order solution is

$$
F _ { 0 } ( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } ) = C _ { 0 } , \qquad { \frac { \partial S _ { 0 } } { \partial y _ { 1 } } } = x _ { 1 } ^ { ( 0 ) } , \qquad { \frac { \partial S _ { 0 } } { \partial y _ { 2 } } } = x _ { 2 } ^ { ( 0 ) } .
$$

Put

$$
\frac { \partial F _ { \boldsymbol { 0 } } } { \partial x _ { 1 } ^ { ( 0 ) } } = - n _ { 1 } ^ { ( 0 ) } , \qquad \frac { \partial F _ { \boldsymbol { 0 } } } { \partial x _ { 2 } ^ { ( 0 ) } } = - n _ { 2 } ^ { ( 0 ) } ,
$$

then we have

$$
S _ { 0 } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + [ S _ { 0 } ] ,
$$

where $[ S _ { 0 } ]$ is an unknown arbitrary function of $y _ { 3 }$ . The constants $x _ { 1 } ^ { ( 0 ) }$ and $x _ { 2 } ^ { ( 0 ) }$ are arbitrary， since $C _ { \mathfrak { d } }$ is arbitrary.

The next approximation is obtained from

$$
n _ { 1 } ^ { \left( 0 \right) } \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + n _ { 2 } ^ { \left( 0 \right) } \frac { \partial S _ { 2 } } { \partial y _ { 2 } } = F _ { 1 } \bigg ( x _ { 1 } ^ { \left( 0 \right) } , x _ { 2 } ^ { \left( 0 \right) } , \frac { \partial [ S _ { 0 } ] } { \partial y _ { 3 } } , y _ { 1 } , y _ { 2 } , y _ { 3 } \bigg ) - C _ { 1 } .
$$

The right-hand member should be periodic, irrespective of $[ S _ { 0 } ]$ ，and its mean value is

$$
R \left( x _ { 1 } ^ { \left( 0 \right) } , x _ { 2 } ^ { \left( 0 \right) } , \frac { \partial [ S _ { 0 } ] } { \partial y _ { 3 } } , y _ { 3 } \right) - C _ { 1 } .
$$

For obtaining $S _ { 1 }$ in the form

$\alpha _ { 1 1 } y _ { 1 } + \alpha _ { 1 2 } y _ { 2 } + \alpha _ { 1 3 } y _ { 3 } + \mathtt { a }$ periodic function of $y _ { 1 } , y _ { 2 } , y _ { 3 }$

it is necessary and sufficient that the mean value of the right-hand member of (39) should be equal to a constant $C _ { 1 } ^ { \prime } - C _ { 1 }$ . Then we have an equation

$$
R \left( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , \frac { \partial [ S _ { 0 } ] } { \partial y _ { 3 } } , y _ { 3 } \right) = C _ { 1 } ^ { \prime }
$$

for the determination of $[ S _ { 0 } ]$ . Since $\pmb R$ does not depend on $y _ { 3 }$ itis sufficient to take $\partial [ S _ { 0 } ] / \partial y _ { 3 } = x _ { 3 } ^ { ( 0 ) }$ . Since $C _ { 1 } ^ { \prime }$ is arbitrary, $\boldsymbol { x } _ { 3 } ^ { ( 0 ) }$ isalso arbitrary. Thus we obtain

$$
S _ { 0 } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + x _ { 3 } ^ { ( 0 ) } y _ { 3 } .
$$

By averaging both sides of (39) we find

$$
n _ { 1 } ^ { ( 0 ) } \alpha _ { 1 1 } + n _ { 2 } ^ { ( 0 ) } \alpha _ { 1 2 } = C _ { 1 } ^ { \prime } - C _ { 1 } .
$$

Since $C _ { 1 }$ is arbitrary, we take $C _ { 1 } = C _ { 1 } ^ { \prime }$ ,and hence $\alpha _ { 1 1 } = \alpha _ { 1 2 } = 0$ . Thus we can determine $S _ { 1 }$ except for an arbitrary function of $y _ { 3 }$

Suppose that $S _ { 0 } , S _ { 1 } , S _ { 2 } , \ldots , S _ { p - 1 }$ are determined in this manner. $S _ { p - 1 }$ is determined except for an arbitrary function of $y _ { 3 }$ . We propose to compute $S _ { p - 1 }$ completely，at the same time as $S _ { p }$ ，except for an arbitrary function of $y _ { 3 }$ .Equate the coefficients of $\mu ^ { \mathfrak { p } }$ on both sides of (31a).We obtain

$$
n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 1 } } + n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 2 } } = \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { \scriptscriptstyle ( 0 ) } } \frac { \partial S _ { p - 1 } } { \partial y _ { 3 } } + \Phi _ { p } - C _ { p } ,
$$

where $\Phi _ { p }$ depends only on $y _ { 1 } , y _ { 2 } , y _ { 3 }$ ，and on the derivatives of $S _ { 0 } , S _ { 1 } , \ldots , S _ { p - 1 }$ ，so that on $\partial S _ { p - 1 } / \partial y _ { 1 } , \partial S _ { p - 1 } / \partial y _ { 2 }$ The functions $S _ { 0 } , S _ { 1 } , \ldots , S _ { p - 2 }$ are known. The function $S _ { p - 1 }$ is known except for an arbitrary function of $y _ { 3 }$ .Hence ${ \partial S _ { p - 1 } } / { \partial y _ { 1 } }$ and ${ \partial S _ { p - 1 } } / { \partial y _ { 2 } }$ are known. Hence $\Phi _ { p }$ is known and is periodic with respect to $y _ { 1 }$ and $y _ { 2 }$

Let $\pmb { U }$ be a periodic function of $y _ { 1 } , y _ { 2 } , y _ { 3 }$ .Denote the mean value of $U$ with respect to $y _ { 1 }$ and $y _ { 2 }$ by $[ U ]$ ； then $[ U ]$ is a function of $y _ { 3 }$ The mean value of the right-hand member of (41) is a constant $C _ { p } ^ { \prime } -$ $C _ { p }$ .Hence

$$
\begin{array} { r } { \left[ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial S _ { p - 1 } } { \partial y _ { 3 } } \right] + \left[ \Phi _ { p } \right] = C _ { p } ^ { \prime } , } \end{array}
$$

$$
\begin{array} { r } { \left[ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial [ S _ { p - 1 } ] } { \partial y _ { 3 } } \right] + \left[ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial ( S _ { p - 1 } - [ S _ { p - 1 } ] ) } { \partial y _ { 3 } } \right] + [ \Phi _ { p } ] = C _ { p } ^ { \prime } . } \end{array}
$$

Since $[ S _ { p - 1 } ]$ does not depend on $y _ { 1 } , y _ { 2 }$ ，we have

$$
\begin{array} { r } { \left[ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial [ S _ { p - 1 } ] } { \partial y _ { 3 } } \right] = \frac { \partial [ S _ { p - 1 } ] } { \partial y _ { 3 } } \left[ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \right] = \frac { \partial R } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial [ S _ { p - 1 } ] } { \partial y _ { 3 } } . } \end{array}
$$

Hence

$$
\frac { \partial R } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial [ S _ { p - 1 } ] } { \partial y _ { 3 } } = C _ { p } ^ { \prime } - [ \Phi _ { p } ] - \biggl [ \frac { \partial F _ { 1 } } { \partial x _ { 3 } ^ { ( 0 ) } } \frac { \partial ( S _ { p - 1 } - [ S _ { p - 1 } ] ) } { \partial y _ { 3 } } \biggr ] .
$$

When $S _ { p - 1 }$ is known except for an arbitrary function of $y _ { 3 }$ ，then $S _ { p - 1 } - [ S _ { p - 1 } ]$ is known.Hence the right-hand member of (42）is known. Now $\pmb R$ is a known function of $x _ { 1 } , x _ { 2 } , x _ { 3 }$ ，where $x _ { 1 } , x _ { 2 } , x _ { 3 }$ are replaced by known constants $x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , x _ { 3 } ^ { ( 0 ) }$ ,respectively. Hence $\partial R / \partial x _ { 3 } ^ { ( 0 ) }$ is known,and the unknown function $\partial [ S _ { p - 1 } ] / \partial y _ { 3 }$ ，and hence $[ S _ { p - 1 } ]$ ， is obtained from (42).In order that $[ S _ { p - 1 } ]$ be a periodic function of $y _ { 3 }$ ，the mean value of the right-hand member of (42) should be zero. The mean value is $C _ { p } ^ { \prime } - C _ { p }$ . Since $C _ { p }$ is arbitrary, we can take $C _ { p } =$ $C _ { p } ^ { \prime }$ . Thus $S _ { p }$ is determined by such a recurrence process. It is remarked that $n _ { 3 }$ is now expanded in powers of $\mu$ beginning with the first power, not with the zero-th power of $\mu$

Next suppose that $\pmb R$ depends on $y _ { 3 }$ besides $x _ { 1 } , x _ { 2 } , x _ { 3 }$ . Replace $x _ { 1 } , x _ { 2 } ;$ $x _ { 3 }$ by $\xi _ { 1 } , \xi _ { 2 } , \partial T / \partial \eta _ { 3 }$ respectively，and equate $R$ to a constant $C _ { 1 } ^ { \prime }$ ； then we get

$$
R \left( \xi _ { 1 } , \xi _ { 2 } , \frac { \partial T } { \partial \eta _ { 3 } } , y _ { 3 } \right) = C _ { 1 } ^ { \prime } .
$$

Suppose that $_ T$ satisfying this equation is determined such that $T$ depends on the constants $\xi _ { 1 } , \xi _ { 2 }$ and a new integration constant $\xi _ { 3 }$ Then

$$
U = \xi _ { 1 } \eta _ { 1 } + \xi _ { 2 } \eta _ { 2 } + T
$$

satisfies

$$
R \left( { \frac { \partial U } { \partial y _ { 1 } } } , { \frac { \partial U } { \partial y _ { 2 } } } , { \frac { \partial U } { \partial y _ { 3 } } } , y _ { 3 } \right) = C _ { 1 } ^ { \prime } .
$$

The equations

$$
x _ { i } = \frac { \partial U } { \partial y _ { i } } , \qquad \eta _ { i } = \frac { \partial U } { \partial { \hat { \xi } } _ { i } } \qquad ( i = 1 , 2 , 3 )
$$

define the contact transformation from $x _ { i } , y _ { i }$ to $\xi _ { i } , \eta _ { i }$ Evidently $x _ { 1 } = \xi _ { 1 } , x _ { 2 } = \xi _ { 2 }$ The function $F _ { 0 }$ depends only on $\xi _ { 1 } , \xi _ { 2 }$ after the change of variables.

Let $U$ be a function such that $x _ { 3 } , y _ { 1 } - \eta _ { 1 } , y _ { 2 } - \eta _ { 2 } , y _ { 3 } - \eta _ { 3 }$ are functions of $\boldsymbol { \xi } _ { i }$ and $\eta _ { i }$ and periodic with respect to $\eta _ { i }$ .Then $\pmb { F }$ is periodic with respect to $\eta _ { i }$ after the change of variables. $\pmb R$ is the mean value of $\boldsymbol { F } _ { 1 }$ considered as a periodic function of $y _ { 1 } , y _ { 2 }$ .If $\pmb { F } _ { 1 }$ is regarded as a periodic function of $\eta _ { 1 }$ and $\eta _ { 2 }$ after the change of variables, then $\pmb R$ is again its mean value, i.e., from

$$
4 \pi ^ { 2 } R = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } F _ { 1 } d y _ { 1 } d y _ { 2 }
$$

we can derive

$$
4 \pi ^ { 2 } R = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } F _ { 1 } d \eta _ { 1 } d \eta _ { 2 } .
$$

In fact, we have

$$
\int \int F _ { 1 } d \eta _ { 1 } d \eta _ { 2 } = \int \int F _ { 1 } \Big ( \frac { \partial \eta _ { 1 } } { \partial y _ { 1 } } \frac { \partial \eta _ { 2 } } { \partial y _ { 2 } } - \frac { \partial \eta _ { 1 } } { \partial y _ { 2 } } \frac { \partial \eta _ { 2 } } { \partial y _ { 1 } } \Big ) d y _ { 1 } d y _ { 2 } .
$$

The variables $y _ { 1 } , y _ { 2 } , \eta _ { 1 } , \eta _ { 2 }$ do not enter in the relations

$$
x _ { 1 } = \xi _ { 1 } , \qquad x _ { 2 } = \xi _ { 2 } , \qquad x _ { 3 } = \frac { \partial U } { \partial y _ { 3 } } , \qquad \eta _ { 3 } = \frac { \partial U } { \partial \xi _ { 3 } } .
$$

When the new variables are expressed in functions of the old variables, then $\xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } , \eta _ { 3 }$ depend neither on $y _ { 1 }$ nor on $y _ { 2 }$ . Hence，when we replace $\hat { \xi } _ { 3 }$ by its value as a function of $x _ { 1 } , x _ { 2 } , x _ { 3 } , y _ { 3 }$ in $_ T$ ，we have

$$
\frac { \partial T } { \partial y _ { 1 } } = \frac { \partial T } { \partial y _ { 2 } } = 0 , \qquad \frac { \partial ^ { 2 } T } { \partial \hat { \xi } _ { 3 } \partial y _ { 1 } } = \frac { \partial ^ { 2 } T } { \partial \xi _ { 3 } \partial y _ { 2 } } = 0 .
$$

Thus we have

$$
\begin{array} { r } { \frac { \partial { \eta _ { 1 } } } { \partial y _ { 1 } } = 1 + \frac { \partial ^ { 2 } T } { \partial \xi _ { 1 } \partial y _ { 1 } } = 1 , \qquad \frac { \partial \eta _ { 1 } } { \partial y _ { 2 } } = \frac { \partial ^ { 2 } T } { \partial \xi _ { 2 } \partial y _ { 1 } } = 0 ; } \end{array}
$$

similarly

$$
\begin{array} { r } { \frac { \partial \eta _ { 2 } } { \partial y _ { 1 } } = 0 , \quad \quad \frac { \partial \eta _ { 2 } } { \partial y _ { 2 } } = 1 . } \end{array}
$$

Hence

$$
\iint F _ { 1 } d y _ { 1 } d y _ { 2 } = \iint F _ { 1 } d \eta _ { 1 } d \eta _ { 2 } .
$$

Moreover, since $C _ { 1 } ^ { \prime }$ depends only on the integration constants $\xi _ { 1 } ,$

$\xi _ { 2 } , \xi _ { 3 }$ ，the function $\pmb R$ depends only on $\xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 }$ . Thus we see that

$$
\frac { d \hat { \xi } _ { i } } { d t } = \frac { \partial F } { \partial \eta _ { i } } , \frac { d \eta _ { i } } { d t } = - \frac { \partial F } { \partial \xi _ { i } }
$$

are satisfied formally by the formal series

$$
\begin{array} { r l } & { \xi _ { i } = \xi _ { i } ^ { ( 0 ) } + \mu \xi _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } \xi _ { i } ^ { ( p ) } + \cdot \cdot \cdot , } \\ & { \eta _ { i } = w _ { i } + \mu \eta _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } \eta _ { i } ^ { ( p ) } + \cdot \cdot \cdot , } \\ & { w _ { i } = n _ { i } t + \varpi _ { i } , \qquad n _ { i } = n _ { i } ^ { ( 0 ) } + \mu n _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } n _ { i } ^ { ( p ) } + \cdot \cdot \cdot , } \end{array}
$$

where $\hat { \xi } _ { i } ^ { ( 0 ) }$ are constant, $\hat { \varsigma } _ { i } ^ { ( 1 ) } , \eta _ { i } ^ { ( 1 ) }$ are periodic functions of $\boldsymbol { w }$ depending on the $\pmb { n }$ integration constants $\xi _ { i } ^ { ( 0 ) }$ ，and $\varpi _ { i }$ are $_ n$ integration constants, and $\eta _ { i } ^ { \left( p \right) }$ depend further on the constants $\pmb { \xi } _ { i } ^ { ( 0 ) }$

Returning to the original variables we see that

$$
\frac { d x _ { i } } { d t } = \frac { \partial F } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } }
$$

are satisfied formally by the formal series

$$
\begin{array} { r } { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } x _ { i } ^ { ( p ) } + \cdot \cdot \cdot , } \\ { y _ { i } = \varepsilon _ { i } w _ { i } + y _ { i } ^ { ( 0 ) } + \mu y _ { i } ^ { ( 1 ) } + \cdot \cdot \cdot + \mu ^ { p } y _ { i } ^ { ( p ) } + \cdot \cdot \cdot , } \end{array}
$$

where $x _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ are periodic functions of $w$ ,and $\varepsilon _ { i }$ is equal to 1 for $i = 1$ or 2, and is equal to 1 or O for $i = 3$ according as $y _ { 3 } - \eta _ { 3 }$ 01 $y _ { 3 }$ is periodic with respect to $\eta _ { i }$ . Thus our problem is reduced to the integration of (43),or to the integration of

$$
\frac { d x _ { i } } { d t } = \frac { \partial R } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial R } { \partial x _ { i } } .
$$

In the three-body problem we have Delaunay's variables $L , L ^ { \prime } , G$ ， $G ^ { \prime } , H , H ^ { \prime } ; l , l ^ { \prime } , g , g ^ { \prime } , h , h ^ { \prime }$ ，or Poincaré's variables $\Lambda , \Lambda ^ { \prime } , \xi , \xi ^ { \prime } , p , p ^ { \prime } ;$ $\lambda , \lambda ^ { \prime } , \eta , \eta ^ { \prime } , q , q ^ { \prime }$ ，where ${ \boldsymbol { F } } = { \boldsymbol { F } } _ { 0 } + \mu { \boldsymbol { F } } _ { 1 { \mathrm { : } } }$ and $F _ { \mathfrak { g } }$ depends only on $\pmb { L }$ and $L ^ { \prime }$ or on $\Lambda$ and $\Lambda ^ { \prime }$ ，but $\boldsymbol { F } _ { 1 }$ is periodic with respect to $\iota$ and $ { \boldsymbol { l } } ^ { \prime }$ ，or to $\lambda$ and $\lambda ^ { \prime }$ . Let the mean value of $F _ { 1 }$ with respect to $\iota$ and $ { \boldsymbol { l } } ^ { \prime }$ or to $\lambda$ and $\lambda ^ { \prime }$ be $\pmb R$ , then the problem is reduced to the formal integration of

$$
\frac { d x _ { i } } { d t } = \frac { \partial R } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial R } { \partial x _ { i } } ,
$$

where $x _ { i }$ and $y _ { i }$ are the last four pairs of variables $G , G ^ { \prime } , H , H ^ { \prime } ; g , g ^ { \prime }$ ， $h , h ^ { \prime } ; \mathrm { o r } \ \xi , \xi ^ { \prime } , p , p ^ { \prime } ; \eta , \eta ^ { \prime } , q , q ^ { \prime }$ ; and $\pmb { L }$ and $L ^ { \prime }$ ，or $\Lambda$ and $\Lambda ^ { \prime }$ , are supposed to be constants.

$R$ is further expanded in a small parameter $\varepsilon$ , for example, and the method of solution described in the beginning of this Section 14.9 can be applied.

Poincaré's formulation of such dynamical problems was adopted to the classical quantum theory for atomic and molecular structure (Section 1.16) by Born and Brody (1921),Born and Pauli (1922), Pauli (1922),Bohr (1923) and Born and Heisenberg (1924).

Hagihara (1931） applied Lindstedt's theory to the motion of a particle around the bottom of a smooth elipsoid under gravity.

# 14.10 CHARLIER'S REMARK

Charlier (1904,1907) has shown that in (31) for $n = 2$ the constants ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ can be arbitrarily chosen within a certain domain,so that the series for $S _ { 1 } , S _ { 2 } , \ldots$ ， are convergent for all values of $x _ { 1 } ^ { ( 0 ) }$ and $x _ { 2 } ^ { ( 0 ) }$

Charlier put $R = F _ { \mathrm { 0 } } + \mu \Psi$ and

$$
F = R + \mu ( F _ { 1 } - \Psi ) + \mu ^ { 2 } F _ { 2 } + \cdot \cdot \cdot .
$$

Suppose that

$$
C = C _ { 0 } + \mu C _ { 1 } + \mu ^ { 2 } C _ { 2 } + \cdots ,
$$

then,corresponding to (32) and (33), we have

$$
R \left( { \frac { \partial S _ { 0 } } { \partial y _ { 1 } } } , { \frac { \partial S _ { 0 } } { \partial y _ { 2 } } } \right) = C _ { 0 } ,
$$

$$
n _ { 1 } ^ { ( 0 ) } \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + n _ { 2 } ^ { ( 0 ) } \frac { \partial S _ { 1 } } { \partial y _ { 2 } } = F _ { 1 } - \Psi - C _ { 1 } ,
$$

$$
n _ { 1 } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 1 } } + n _ { 2 } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { 2 } } = \Phi _ { p } - C _ { p } .
$$

If

$$
\Phi _ { p } = \sum A _ { i j } ^ { ( p ) } \cos { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

then we obtain

$$
S _ { p } = \sum _ { i n _ { 1 } ^ { ( 0 ) } \ + \ j n _ { 2 } ^ { ( 0 ) } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

and the solution of (45) is

$$
S _ { 0 } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } ,
$$

where $x _ { 1 } ^ { ( 0 ) }$ and $\pmb { x } _ { 2 } ^ { ( 0 ) }$ are arbitrary constants and $C _ { 0 } = R ( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } )$ Further

$$
n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } = - \frac { \partial R } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } = - \frac { \partial C _ { 0 } } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } , \qquad n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } = - \frac { \partial R } { \partial x _ { 2 } ^ { \scriptscriptstyle ( 0 ) } } = - \frac { \partial C _ { 0 } } { \partial x _ { 2 } ^ { \scriptscriptstyle ( 0 ) } } .
$$

Since $\Psi$ is an arbitrary function of $x _ { 1 }$ and $x _ { 2 }$ by our assumption, we can choose this function so that ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ are of arbitrary values with given values of $x _ { 1 } ^ { ( 0 ) }$ and $x _ { 2 } ^ { ( 0 ) }$ . Practically they are so chosen that ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ differ slightly from $- \partial F _ { 0 } / \partial x _ { 1 } ^ { ( 0 ) }$ and $- \partial F _ { 0 } / \partial x _ { 2 } ^ { ( 0 ) }$ respectively, in such a way that the series $S _ { p }$ is convergent. For example, we have

$$
{ \cal S } _ { 1 } = { \sum } ^ { \prime } \frac { A _ { i j } ^ { ( 1 ) } } { i n _ { 1 } ^ { ( 0 ) } + j n _ { 2 } ^ { ( 0 ) } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } .
$$

Suppose that

$$
F _ { 1 } - \Psi = \sum A _ { i j } ^ { ( 1 ) } \cos ( i y _ { 1 } + j y _ { 2 } )
$$

is convergent in the same way as a power series of $x _ { 2 }$ . By a suitable choice of the canonical elements the coefficients $\pmb { A } _ { i j } ^ { ( 1 ) }$ can be made to be of order $x _ { 2 } ^ { j }$ . Then the series for $S _ { \imath }$ is convergent, if ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ are so chosen that $n _ { 1 } ^ { ( 0 ) } / n _ { 2 } ^ { ( 0 ) }$ is one of the roots of an algebraic equation at least of the second degree with integer coefficients,according to the theorem of Bruns which will be proved in Section 15.3.Then the series for $S _ { 2 } , S _ { 3 } , \ldots$ are likewise convergent. However $\Psi$ should not be so chosen that $n _ { 1 } ^ { ( 0 ) } / n _ { 2 } ^ { ( 0 ) }$ satisfy a linear equation (34). In such a case $s$ cannot be expanded in powers of $\mu$ but of $\sqrt { \mu }$ ，as will be seen in Section 14.11.

Now among the choice of ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ it is most important to choose them as the true mean motions of $y _ { 1 }$ and $y _ { 2 }$ . We take

$$
R \left( \frac { \partial S _ { 0 } } { \partial y _ { 1 } } , \frac { \partial S _ { 0 } } { \partial y _ { 2 } } \right) = C .
$$

The solution is then

$$
S _ { 0 } = x _ { 1 } ^ { \prime } y _ { 1 } + x _ { 2 } ^ { \prime } y _ { 2 } ,
$$

$$
{ \cal S } _ { p } = { \sum } ^ { \prime } B _ { i j } ^ { ( p ) } \sin { ( i y _ { 1 } + j y _ { 2 } ) } , \qquad B _ { i j } ^ { ( p ) } = \frac { A _ { i j } ^ { ( p ) } } { i n _ { 1 } ^ { \prime } + j n _ { 2 } ^ { \prime } } ,
$$

$$
n _ { 1 } ^ { \prime } = - \frac { \partial R } { \partial x _ { 1 } ^ { \prime } } = - \frac { \partial C } { \partial x _ { 1 } ^ { \prime } } , \qquad n _ { 2 } ^ { \prime } = - \frac { \partial R } { \partial x _ { 2 } ^ { \prime } } = - \frac { \partial C } { \partial x _ { 2 } ^ { \prime } } .
$$

Thus we find

$$
S = x _ { 1 } ^ { \prime } y _ { 1 } + x _ { 2 } ^ { \prime } y _ { 2 } + { et { } { ' } \sum } ^ { \prime } B _ { i j } \sin { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

and finally

$$
\begin{array} { r l } & { n _ { 1 } ^ { \prime } t + c _ { 1 } = y _ { 1 } + et { } { ' } \sum _ { \lambda } \frac { \partial B _ { i j } } { \partial x _ { 1 } ^ { \prime } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } , } \\ & { n _ { 2 } ^ { \prime } t + c _ { 2 } = y _ { 2 } + et { } { ' } \sum _ { \lambda } \frac { \partial B _ { i j } } { \partial x _ { 2 } ^ { \prime } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } , } \end{array}
$$

which shows that $n _ { 1 } ^ { \prime }$ and $n _ { 2 } ^ { \prime }$ are the true mean motions of $y _ { 1 }$ and $y _ { 2 }$ ， provided that the right-hand members of these equations are convergent.

Another choice of ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ would be such that they are the osculating values of the mean motions of $y _ { 1 }$ and $y _ { 2 }$ at the epoch $t = 0$ From

$$
F _ { \boldsymbol 0 } \left( \frac { \partial S _ { \boldsymbol 0 } } { \partial y _ { \boldsymbol 1 } } , \frac { \partial S _ { \boldsymbol 0 } } { \partial y _ { \boldsymbol 2 } } \right) = C _ { \boldsymbol 0 }
$$

we obtain

$$
S _ { 0 } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } .
$$

The next equation is

$$
\begin{array} { r l } & { n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } \displaystyle \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } \displaystyle \frac { \partial S _ { 1 } } { \partial y _ { 2 } } = F _ { 1 } ( x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } , x _ { 2 } ^ { \scriptscriptstyle ( 0 ) } , y _ { 1 } , y _ { 2 } ) - C _ { 1 } , } \\ & { } \\ & { n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } \displaystyle \frac { \partial S _ { p } } { \partial y _ { 1 } } + n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } \displaystyle \frac { \partial S _ { p } } { \partial y _ { 2 } } = \Phi _ { p } - C _ { p } . } \end{array}
$$

In this case

$$
n _ { 1 } ^ { \left( 0 \right) } = - \frac { \partial F _ { 0 } } { \partial x _ { 1 } ^ { \left( 0 \right) } } , \qquad n _ { 2 } ^ { \left( 0 \right) } = - \frac { \partial F _ { 0 } } { \partial x _ { 2 } ^ { \left( 0 \right) } } .
$$

If we take

$$
F _ { 1 } = \sum A _ { i j } ^ { ( 1 ) } \cos { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

then

$$
S _ { 1 } = \alpha _ { 1 } + \beta _ { 1 } y _ { 1 } + \gamma _ { 1 } y _ { 2 } + { et { } { ' } \sum } B _ { i j } ^ { ( 1 ) } \sin { ( i y _ { 1 } + j y _ { 2 } ) } .
$$

The constants $\alpha _ { 1 } , \beta _ { 1 } , \gamma _ { 1 }$ are arbitrarily chosen with the single condition $n _ { 1 } ^ { ( 0 ) } \beta _ { 1 } + n _ { 2 } ^ { ( 0 ) } \gamma _ { 1 } = { \cal A } _ { 0 0 } ^ { ( 1 ) } - C _ { 1 } ,$ where $C _ { 1 }$ is arbitrary. Similarly

$$
S _ { p } = \alpha _ { p } + \beta _ { p } y _ { 1 } + \gamma _ { p } y _ { 2 } + et { } { ' } \sum _ { i } B _ { i j } ^ { ( p ) } \sin { ( i y _ { 1 } + j y _ { 2 } ) } .
$$

The constants $C _ { p }$ are determined by

$$
n _ { 1 } ^ { ( 0 ) } \beta _ { p } + n _ { 2 } ^ { ( 0 ) } \gamma _ { p } = { \cal A } _ { 0 0 } ^ { ( p ) } - C _ { p } .
$$

Thus $s$ is of the form

$$
S = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + \alpha + \beta y _ { 1 } + \gamma y _ { 2 } + et { } { ' } \sum _ { i } B _ { i j } \sin { ( i y _ { 1 } + j y _ { 2 } ) }
$$

where

$$
\begin{array} { c } { { \alpha = \mu \alpha _ { 1 } + \mu ^ { 2 } \alpha _ { 2 } + \cdot \cdot \cdot , \qquad \beta = \mu \beta _ { 1 } + \mu ^ { 2 } \beta _ { 2 } + \cdot \cdot \cdot , } } \\ { { \gamma = \mu \gamma _ { 1 } + \mu ^ { 2 } \gamma _ { 2 } + \cdot \cdot \cdot , \qquad B _ { i j } = \mu B _ { i j } ^ { ( 1 ) } + \mu ^ { 2 } B _ { i j } ^ { ( 2 ) } + \cdot \cdot \cdot . . } } \end{array}
$$

Hence the solution is

$$
x _ { 1 } = \frac { \partial S } { \partial y _ { 1 } } = x _ { 1 } ^ { ( 0 ) } + \beta + et { } { ' } \sum ^ { ' } i B _ { i j } \cos { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

$$
x _ { 2 } = \frac { \partial S } { \partial y _ { 2 } } = x _ { 2 } ^ { ( 0 ) } + \tau + et { } { ' } \sum ^ { } j B _ { i j } \cos { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

$$
n _ { 1 } t + c _ { 1 } = \frac { \partial S } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } = y _ { 1 } + \frac { \partial \alpha } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } + \frac { \partial \beta } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } y _ { 1 } + \frac { \partial \gamma } { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } y _ { 2 }
$$

$$
+ \sum ^ { \prime } \frac { \partial B _ { i j } } { \partial x _ { 1 } ^ { ( 0 ) } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

$$
n _ { 2 } t + c _ { 2 } = \frac { \partial S } { \partial x _ { 2 } ^ { ( 0 ) } } = y _ { 2 } + \frac { \partial \alpha } { \partial x _ { 2 } ^ { ( 0 ) } } + \frac { \partial \beta } { \partial x _ { 2 } ^ { ( 0 ) } } y _ { 1 } + \frac { \partial \gamma } { \partial x _ { 2 } ^ { ( 0 ) } } y _ { 2 }
$$

$$
+ \sum ^ { \prime } \frac { \partial B _ { i j } } { \partial x _ { 2 } ^ { ( 0 ) } } \sin { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

where

$$
n _ { 1 } = - \frac { \partial C } { \partial x _ { 1 } ^ { ( 0 ) } } , \qquad n _ { 2 } = - \frac { \partial C } { \partial x _ { 2 } ^ { ( 0 ) } } .
$$

Here $\alpha , \beta , \gamma$ should be so chosen that we should have $x _ { 1 } = x _ { 1 } ^ { ( 0 ) }$ ， $x _ { 2 } = x _ { 2 } ^ { ( 0 ) }$ for $\pmb { t = 0 }$ ，and that $c _ { 1 }$ and $c _ { 2 }$ should be the values of $y _ { 1 }$ and $y _ { 2 }$ for $t = 0$ . Then

$$
\begin{array} { l } { { 0 = \displaystyle \beta + \sum _ { i } ^ { \prime } i B _ { i j } \cos { ( i y _ { 1 } ^ { ( 0 ) } + j y _ { 2 } ^ { ( 0 ) } ) } , } } \\ { { 0 = \displaystyle \gamma + \sum _ { i } ^ { \prime } j B _ { i j } \cos { ( i y _ { 1 } ^ { ( 0 ) } + \cdot { j y _ { 2 } ^ { ( 0 ) } ) } } , } } \\ { { 0 = \alpha + \beta y _ { 1 } ^ { ( 0 ) } + \gamma y _ { 2 } ^ { ( 0 ) } + et { } { ' } \sum _ { i } ^ { \prime } B _ { i j } \sin { ( i y _ { 1 } ^ { ( 0 ) } + j y _ { 2 } ^ { ( 0 ) } ) } , } } \end{array}
$$

and

$$
C _ { p } = - \sum A _ { i j } ^ { ( p ) } \cos ( i y _ { 1 } ^ { ( 0 ) } + j y _ { 2 } ^ { ( 0 ) } ) = \Phi _ { p } ( y _ { 1 } ^ { ( 0 ) } , y _ { 2 } ^ { ( 0 ) } ) .
$$

Since we have

$$
C = F _ { \circ } + \sum \mu ^ { p } \Phi _ { p } ( y _ { \bot } ^ { \left( 0 \right) } , y _ { 2 } ^ { \left( 0 \right) } ) ,
$$

we obtain

$$
\begin{array} { l } { { n _ { 1 } = n _ { 1 } ^ { \left( 0 \right) } - \displaystyle \sum _ { j } \mu ^ { p } \frac { \partial \Phi _ { p } ( y _ { 1 } ^ { \left( 0 \right) } , y _ { 2 } ^ { \left( 0 \right) } ) } { \partial x _ { 1 } ^ { \left( 0 \right) } } , } } \\ { { \displaystyle n _ { 2 } = n _ { 2 } ^ { \left( 0 \right) } - \displaystyle \sum _ { j } \mu ^ { p } \frac { \partial \Phi _ { p } ( y _ { 1 } ^ { \left( 0 \right) } , y _ { 2 } ^ { \left( 0 \right) } ) } { \partial x _ { 2 } ^ { \left( 0 \right) } } . } } \end{array}
$$

We form $n _ { 1 } t + c _ { 1 }$ and $n _ { 2 } t + c _ { 2 }$ from these expressions for $n _ { 1 }$ and ${ \boldsymbol n } _ { 2 }$ ， and neglect the periodic terms on the right-hand sides of the resulting equations. Then we solve for $y _ { 1 }$ and $y _ { 2 }$ . Denote the coefficients of $t$ in these equations by ${ \bf N } _ { 1 }$ and $\mathbf { N } _ { 2 }$ respectively. Then

$$
\begin{array} { r l } & { \left( 1 + \frac { \partial \beta } { \partial x _ { 1 } ^ { ( 0 ) } } \right) \mathbf { N } _ { 1 } + \frac { \partial \gamma } { \partial x _ { 1 } ^ { ( 0 ) } } \mathbf { N } _ { 2 } = n _ { 1 } , } \\ & { } \\ & { \frac { \partial \beta } { \partial x _ { 2 } ^ { ( 0 ) } } \mathbf { N } _ { 1 } + \left( 1 + \frac { \partial \gamma } { \partial x _ { 2 } ^ { ( 0 ) } } \right) \mathbf { N } _ { 2 } = n _ { 2 } . } \end{array}
$$

The right-hand members $n _ { 1 }$ and $n _ { 2 }$ are expressed in terms of the osculating elements, so that these two equations give the relations between the true mean motions and the osculating elements.We have to the first order

$$
\begin{array} { r l } & { \mathrm { v _ { 1 } } = n _ { 1 } ^ { ( 0 ) } - \mu \frac { \partial A _ { 0 0 } ^ { ( 1 ) } } { \partial x _ { 1 } ^ { ( 0 ) } } - \mu et { } { ' } { \sum } _ { i } B _ { i j } ^ { ( 1 ) } \left( i \frac { \partial n _ { 1 } ^ { ( 0 ) } } { \partial x _ { 1 } ^ { ( 0 ) } } + \dot { I } \frac { \partial n _ { 2 } ^ { ( 0 ) } } { \partial x _ { 1 } ^ { ( 0 ) } } \right) \cos \left( i y _ { 1 } ^ { ( 0 ) } + \dot { J } y \right. } \\ & { \mathrm { v _ { 2 } } = n _ { 2 } ^ { ( 0 ) } - \mu \frac { \partial A _ { 0 0 } ^ { ( 1 ) } } { \partial x _ { 2 } ^ { ( 0 ) } } - \mu et { } { ' } { \sum } _ { i } B _ { i j } ^ { ( 1 ) } \left( i \frac { \partial n _ { 1 } ^ { ( 0 ) } } { \partial x _ { 2 } ^ { ( 0 ) } } + \dot { I } \frac { \partial n _ { 2 } ^ { ( 0 ) } } { \partial x _ { 2 } ^ { ( 0 ) } } \right) \cos \left( i y _ { 1 } ^ { ( 0 ) } + \dot { J } y \right. } \end{array}
$$

Such use of the osculating mean motions is advantageous,because it enables us not only to compute the various coefficients in the expansion of the disturbing function,but also to express the perturbation in convergent form.

We have from (48) to the first order in $\pmb { \mu }$

$$
x _ { 1 } = x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } + \mu { \sum } ^ { \prime } i B _ { i j } ^ { \scriptscriptstyle ( 1 ) } [ \cos ( i y _ { 1 } + j y _ { 2 } ) - \cos ( i y _ { 1 } ^ { \scriptscriptstyle ( 0 ) } + j y _ { 2 } ^ { \scriptscriptstyle ( 0 ) } ) ] .
$$

Let $\displaystyle \sum 3$ be the sum of the terms with small divisor $i n _ { 1 } ^ { ( 0 ) } + j n _ { 2 } ^ { ( 0 ) }$ in the series

$$
{ \sum } ^ { \prime } i B _ { i j } \ : [ \cos \ : ( i y _ { 1 } + j y _ { 2 } ) - \cos \ : ( i y _ { 1 } ^ { \ : ( 0 ) } + j y _ { 2 } ^ { \ : ( 0 ) } ) ] .
$$

Charlier showed that $\sum 3$ never exceeds a finite limit within a finite interval of time.In fact,

$$
\begin{array} { r } { \sum _ { \mathfrak { s } } = - \sum _ { \mathfrak { s } } \frac { 2 i A _ { i j } } { i n _ { 1 } ^ { ( 0 ) } + j n _ { 2 } ^ { ( 0 ) } } \sin \left( i \frac { y _ { 1 } + y _ { 1 } ^ { ( 0 ) } } { 2 } + j \frac { y _ { 2 } + y _ { 2 } ^ { ( 0 ) } } { 2 } \right) } \\ { \cdot \sin \left( i \frac { y _ { 1 } - y _ { 1 } ^ { ( 0 ) } } { 2 } + j \frac { y _ { 2 } - y _ { 2 } ^ { ( 0 ) } } { 2 } \right) . } \end{array}
$$

If $t$ is small, then $y _ { 1 } = y _ { 1 } ^ { ( 0 ) } + n _ { 1 } ^ { ( 0 ) } t , y _ { 2 } = y _ { 2 } ^ { ( 0 ) } + n _ { 2 } ^ { ( 0 ) } t$ ,hence

$$
\sum _ { 3 } = - \mu t \cdot \sum _ { \lambda } i A _ { i j } \sin \bigg ( i \frac { y _ { 1 } + y _ { 1 } ^ { ( 0 ) } } { 2 } + j \frac { y _ { 2 } + y _ { 2 } ^ { ( 0 ) } } { 2 } \bigg ) ,
$$

which is finite. The small divisor does not endanger the convergence of the series for $x _ { 1 { \mathrm { : } } }$ insofar as $t$ is not so large.

Substituting the values of the integration constants in $y _ { 1 }$ ,we see that the terms corresponding to the terms in $\textstyle \sum _ { 3 }$ are proportional to $t ^ { 2 }$ Thus the deviation of the theory from the observation increases with time as proportional to $t ^ { 2 }$ . If the sums $\sum B _ { i j }$ and $\sum \partial B _ { i j } / \partial x$ are convergent, then $\sum 3$ should be below a finite limit.

For higher-order perturbations,the power of $t$ involved is higher than 2.

Finally, Charlier put $\alpha = 0$ in the above treatment in order to apply to a group of asteroids as in Bohlin's group-perturbation method (Section 10.11):

Let $x _ { 1 } ^ { ( 0 ) }$ and $x _ { 2 } ^ { ( 0 ) }$ be given arbitrary numerical values and consider $\beta$ and $\gamma$ as the integration constants.We choose $C _ { 1 }$ so that

$$
n _ { 1 } ^ { ( 0 ) } \beta _ { 1 } + n _ { 2 } ^ { ( 0 ) } \gamma _ { 1 } = [ F _ { 1 } ] - C _ { 1 } .
$$

Charlier proceeded to the computation of the second-order terms.He chose $C _ { 2 }$ so that no constant term would be present in $\Phi _ { 2 } - C _ { 2 }$ and so on to higher-order terms.

I4.IIPOINCARE'S FORMULATION OF BOHLIN'S THEORY

The preceding method fails when there exist relations of the form (34)

$$
n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } m _ { 1 } + n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } m _ { 2 } + \cdots + n _ { \scriptscriptstyle n } ^ { \scriptscriptstyle ( 0 ) } m _ { \scriptscriptstyle n } = 0 ,
$$

where $m _ { i }$ are integers, because such a sum appears in the denominators.

Delaunay's method,as applied to the motion of a characteristic asteroid (Section 9.5), is one of those that dispose of this difficulty.

Consider

$$
\frac { d x _ { i } } { d t } = \frac { \partial F } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } } ,
$$

where $m _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdots + m _ { n } n _ { n } ^ { ( 0 ) }$ is very small. Then the problem reduces to the integration of

$$
F \Big ( \frac { \partial S } { \partial y _ { 1 } } , \frac { \partial S } { \partial y _ { 2 } } , \thinspace \thinspace \cdot \~ \cdot \~ , \frac { \partial S } { \partial y _ { n } } , y _ { 1 } , \thinspace \cdot ~ \cdot ~ , y _ { n } \Big ) = C .
$$

Put

$$
\begin{array} { r l } & { S = S _ { 0 } + \sqrt { \mu } S _ { 1 } + \mu S _ { 2 } + \mu \sqrt { \mu } S _ { 3 } + \cdots , } \\ & { C = C _ { 0 } + \mu C _ { 2 } + \mu ^ { 2 } C _ { 4 } + \cdots , } \end{array}
$$

and substitute in the equation (5O); then we obtain successively

$$
\begin{array} { r l } & { F _ { \psi } \Big \{ \frac { \partial \hat { \Delta } _ { \psi } } { \partial y _ { 1 } } , \frac { \partial \hat { \Delta } _ { \psi _ { 3 } } } { \partial y _ { 2 } } , \ldots , \frac { \partial \hat { \Delta } _ { \psi _ { 3 } } } { \partial y _ { 3 } } \Big \} = C _ { \psi } , } \\ & { \sum \frac { \partial F _ { \psi } } { \partial x _ { 1 } } \frac { \partial \hat { S } _ { 1 } } { \partial y _ { 4 } } \frac { \partial \hat { S } _ { 1 } } { \partial y _ { 4 } } = 0 , } \\ & { \sum \frac { \partial F _ { \psi } } { \partial x _ { 4 } } \frac { \partial \hat { S } _ { 2 } } { \partial y _ { 4 } } + \frac { 1 } { 2 } \sum \frac { \partial ^ { \mathcal { N } } \hat { \Delta } ^ { \mathcal { N } } _ { \psi } } { \partial x _ { 4 } \partial x _ { 5 } } \frac { \partial \hat { S } _ { 1 } } { \partial y _ { 4 } } \frac { \partial \hat { S } _ { 1 } } { \partial y _ { 5 } } = \Phi + C _ { \psi } , } \\ & { \sum \frac { \partial \hat { F } _ { \psi } } { \partial x _ { 5 } } \frac { \partial \hat { S } _ { 3 } } { \partial y _ { 4 } } + \frac { 1 } { 2 } \sum \frac { \partial ^ { \mathcal { N } } \hat { F } _ { \psi } } { \partial x _ { 4 } \partial x _ { 5 } } \frac { \partial \hat { S } _ { 1 } } { \partial y _ { 4 } \partial y _ { 5 } } = \Phi , } \\ & { \sum \frac { \partial \hat { F } _ { \psi } } { \partial x _ { 4 } } \frac { \partial \hat { S } _ { 4 } } { \partial y _ { 4 } } + \frac { 1 } { 2 } \sum \frac { \partial ^ { \mathcal { N } } \hat { F } _ { \psi } } { \partial x _ { 4 } \partial x _ { 5 } } \frac { \partial \hat { S } _ { 3 } } { \partial y _ { 4 } } \frac { \partial \hat { S } _ { 2 } } { \partial y _ { 5 } } = \Phi + C _ { \psi } , } \\ & { \ldots , } \end{array}
$$

where $\Phi$ denotes a known function, different for each of the equations. In the third equation $S _ { \mathfrak { d } }$ ，contained in $\Phi$ , is known from the foregoing equations.In the fourth equation $S _ { \mathfrak { o } }$ and $S _ { 1 }$ are known.In the fifth equation $S _ { \boldsymbol { 0 } } , S _ { \boldsymbol { \imath } }$ ,and $S _ { z }$ are known. The summation sign means the sum over $_ i$ and $k$ . In the third equation the combination $( i , k )$ appears twice for $i \neq k$ and once for $i = k$ . In the other equations it appears always twice.

Suppose that

$$
\frac { \partial S _ { 0 } } { \partial y _ { i } } = x _ { i } ^ { ( 0 ) }
$$

with constants $x _ { i } ^ { ( 0 ) }$ . The variables $x _ { i }$ are replaced by $x _ { i } ^ { \left( 0 \right) }$ in the derivatives of $\scriptstyle { F _ { 0 } }$ of (51） such that

$$
\frac { \partial F _ { 0 } } { \partial x _ { i } } = - n _ { i } ^ { ( 0 ) } , ~ \sum m _ { i } n _ { i } ^ { ( 0 ) } = 0 ,
$$

and no other linear relation exists among ${ n } _ { i } ^ { ( 0 ) }$ with integer coefficients. We propose to determine $s$ in such a way that ${ \partial S _ { p } } / { \partial y _ { i } }$ are periodic functions of $y _ { i }$ . The first equation of(51) determines $C _ { 0 }$ . The second equation is written

$$
\sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { 1 } } { \partial y _ { i } } = 0 .
$$

This equation is satisfied only if ${ \partial S _ { 1 } } / { \partial y _ { i } }$ are functions only of the combination $m _ { 1 } y _ { 1 } + \dotsb + m _ { n } y _ { n }$ .In fact，if $S _ { 1 }$ contains a term $\pmb { A }$ cos $( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot + p _ { n } y _ { n } )$ ，then the left-hand member of (53) should contain a term $- A ( p _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + p _ { n } n _ { n } ^ { ( 0 ) } )$ sin $( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot + p _ { n } y _ { n } )$ ， which should vanish only if $p _ { 1 } / m _ { 1 } = \cdot \cdot \cdot = p _ { n } / m _ { n }$ .Hence we should have

$$
S = \alpha _ { 1 } y _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } y _ { n } + f ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) .
$$

In the third equation of (51） we equate on both sides the terms depending on the sines and cosines of multiples of $m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n }$ The first term does not contain such a term, because otherwise such a term should be zero due to the equality (52). The second term depends only on $S _ { 1 }$ and is a function only of the combination $m _ { 1 } y _ { 1 } +$ $\cdots + m _ { n } y _ { n }$ . All these terms contain sines or cosines of multiples of $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$ only. Let $U$ be a function whose derivatives ${ \partial U } / { \partial y _ { i } }$ are periodic functions of $p _ { 1 } y _ { 1 } + \cdot \cdot \cdot + p _ { n } y _ { n }$ such that its term is either of the forms

$$
\alpha \cos { ( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot \cdot + p _ { n } y _ { n } ) } , \qquad \alpha \sin { ( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot \cdot + p _ { n } y _ { n } ) } .
$$

Denote by $[ U ]$ and call it the mean value of $\boldsymbol { U }$ ，when all trigonometric terms,except those for which $p _ { 1 } / m _ { 1 } = \cdot \cdot \cdot = p _ { n } / m _ { n }$ ，are taken off from $U$ .Then we have

$$
\left[ \frac { \partial U } { \partial y _ { i } } \right] = \frac { \partial [ U ] } { \partial y _ { i } } , ~ \sum ~ n _ { i } ^ { ( 0 ) } \frac { \partial [ U ] } { \partial y _ { i } } = \mathrm { c o n s t a n t } .
$$

If further $V$ is any periodic function,then we have

$$
{ \bigg [ } [ V ] { \frac { \partial U } { \partial y _ { i } } } { \bigg ] } = [ V ] { \bigg [ } { \frac { \partial U } { \partial y _ { i } } } { \bigg ] } .
$$

Hence we have from the third equation of (51)

$$
- \left[ \sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { 2 } } { \partial y _ { i } } \right] = \mathrm { c o n s t a n t } , \qquad \left[ \frac { \partial S _ { 1 } } { \partial y _ { i } } \frac { \partial S _ { 1 } } { \partial y _ { k } } \right] = \frac { \partial S _ { 1 } } { \partial y _ { i } } \frac { \partial S _ { 1 } } { \partial y _ { k } } ,
$$

$$
[ \Phi ] = - [ F _ { 1 } ] ,
$$

where $x _ { i }$ are replaced by $x _ { i } ^ { ( 0 ) }$ in $F _ { 1 }$ ，and this $\Phi$ is the same as the $\Phi$ in (51).Denote the constant on the right-hand side of the first equation by $C _ { 2 } ^ { \prime } - C _ { 2 }$ . Then we get,by taking the mean values of both sides,

$$
\frac { 1 } { 2 } \sum \hat { \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { i } \partial x _ { k } } } \frac { \partial S _ { 1 } } { \partial y _ { i } } \frac { \partial S _ { 1 } } { \partial y _ { k } } = C _ { 2 } ^ { \prime } - [ F _ { 1 } ] .
$$

Now from

$$
S _ { 1 } = \alpha _ { 1 } y _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } y _ { n } + f ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } )
$$

we obtain

$$
\frac { \partial S _ { 1 } } { \partial y _ { i } } = \alpha _ { i } + m _ { i } f ^ { \prime } .
$$

If this expression is substituted in (55), then an equation of the second degree in $f ^ { \prime }$ is obtained,which can be written

$$
A f ^ { \prime 2 } + 2 B f ^ { \prime } + D = C _ { 2 } ^ { \prime } - [ F _ { 1 } ] ,
$$

where $A , B , D$ are constants depending on $\alpha _ { i }$ ，which can be chosen arbitrarily. We have three cases to distinguish.

(I) The revolution case.

In order that $f ^ { \prime }$ ， consequently ${ \partial S _ { 1 } } / { \partial y _ { i } }$ ， be periodic with respect to $m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n }$ ,it is necessary and sufficient that the equation (56) has real roots,that is, that

$$
B ^ { 2 } - A D + A C _ { 2 } ^ { \prime } - A [ F _ { 1 } ] > 0
$$

should be satisfied for all values of $m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n }$ . Since the $\alpha _ { i }$ are arbitrary, we take $\alpha _ { 1 } = \alpha _ { 2 } = \cdot \cdot \cdot = \alpha _ { n } = 0$ ，without loss of generality.Then (56) is reduced to

$$
A f ^ { \prime 2 } = C _ { 2 } ^ { \prime } - [ F _ { 1 } ] .
$$

Consider a diagram with $f ^ { \prime } +$ constant as the radius vector and with $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$ as the polar angle.

Suppose that $A > 0$ . For the periodicity of $f ^ { \prime }$ it is necessary at first that $f ^ { \prime }$ should remain always real, that is, $C _ { 2 } ^ { \prime }$ should be greater than the maximum of $[ F _ { 1 } ]$ . Then $f ^ { \prime }$ ， consequently ${ \partial S _ { 1 } } / { \partial y _ { i } }$ ,is periodic with respect to $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$ and does not vanish.

Next we determine $S _ { z }$ which should be of the form

$$
\alpha _ { 1 } ^ { ( 2 ) } y _ { 1 } + \ldots + \alpha _ { n } ^ { ( 2 ) } y _ { n } + \phi _ { 2 } ,
$$

where $\phi _ { 2 }$ is periodic, and in general $S _ { p }$ should be of the form

$$
\alpha _ { 1 } ^ { ( p ) } y _ { 1 } + \ldots + \alpha _ { n } ^ { ( p ) } y _ { n } + \phi _ { p } ,
$$

where $\phi _ { p }$ is periodic. We can put

$$
\frac { \alpha _ { 1 } ^ { ( p ) } } { m _ { 1 } } = \cdots = \frac { \alpha _ { n } ^ { ( p ) } } { m _ { n } }
$$

without loss of generality. Then we obtain

$$
- \Bigl [ \sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { i } } \Bigr ] = C _ { p } ^ { \prime } - C _ { p }
$$

for the determination of $S _ { p }$ . If (57) is satisfied,then we should have $C _ { p } ^ { \prime } = C _ { p }$ , in particular $C _ { 2 } ^ { \prime } = C _ { 2 }$ ·

The third equation of (51) is now of the form

$$
\sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { 2 } } { \partial y _ { i } } = \Phi ,
$$

where $\Phi$ contains the known function $S _ { 1 }$ and $\Phi$ isperiodic in $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ . Let

$$
\Phi = \sum { \cal A } \cos ( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot + p _ { n } y _ { n } ) ,
$$

then (58) gives

$$
\mathrm { ~  ~ \xi ~ } _ { \mathrm { { 2 } } } = \sum \frac { A \cos ( p _ { 1 } y _ { 1 } + \cdot \cdot \cdot + p _ { n } y _ { n } ) } { p _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdot \cdot \cdot + p _ { n } n _ { n } ^ { ( 0 ) } } + \psi ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) ,
$$

where $\psi$ is an arbitrary function of $m _ { 1 } y _ { 1 } + \dotsb + m _ { n } y _ { n }$ . This solution fails if there is a term such that $p _ { 1 } n _ { 1 } ^ { ( 0 ) } + \cdots + p _ { n } n _ { n } ^ { ( 0 ) } = 0$ ，that is, $p _ { 1 } / m _ { 1 } = p _ { 2 } / m _ { 2 } = \cdot \cdot \cdot = p _ { n } / m _ { n }$ . But this cannot occur because $[ \Phi ]$ $= 0$ .For the determination of $S _ { z }$ so that $\psi = [ S _ { 2 } ]$ , we equate the mean values of both sides of the third equation of (51). Then we obtain by [57]

$$
\Big [ \sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { 3 } } { \partial y _ { i } } \Big ] = 0 ,
$$

and

$$
\begin{array} { r } { \left[ \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { i } \partial x _ { k } } \frac { \partial S _ { 1 } } { \partial y _ { i } } \frac { \partial S _ { 2 } } { \partial y _ { k } } \right] = \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { i } \partial x _ { k } } \frac { \partial S _ { 1 } } { \partial y _ { i } } \frac { \partial [ S _ { 2 } ] } { \partial y _ { k } } , } \end{array}
$$

since $S _ { 1 }$ depends only on $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$ . Hence

$$
{ \frac { 1 } { 2 } } \sum { \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { i } \partial x _ { k } } } { \frac { \partial S _ { 1 } } { \partial y _ { i } } } { \frac { \partial [ S _ { 2 } ] } { \partial y _ { k } } } = [ \Phi ] .
$$

Denote the derivatives of $[ S _ { 2 } ]$ with respect to $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$ by $[ S _ { 2 } ^ { \prime } ]$ ，then

$$
\frac { \partial S _ { 1 } } { \partial y _ { i } } = m _ { i } f ^ { \prime } , \qquad \frac { \partial [ S _ { 2 } ] } { \partial y _ { k } } = m _ { k } [ S _ { 2 } ^ { \prime } ] ,
$$

and hence we have

$$
\frac { 1 } { 2 } \sum \hat { \partial } ^ { 2 } F _ { 0 } \qquad m _ { i } m _ { k } [ S _ { 2 } ^ { \prime } ] = \frac { [ \Phi ] } { f ^ { \prime } } .
$$

Since $f ^ { \prime } \not \equiv 0 , [ S _ { 2 } ^ { \prime } ]$ is periodic in $m _ { 1 } y _ { 1 } + \dots + m _ { n } y _ { n }$ and does not become infinite. $[ S _ { 2 } ]$ should be of the form $a ( m _ { 1 } y _ { 1 } + \cdot \cdot \cdot + m _ { n } y _ { n } ) + \psi$ ， where $a$ is a constant and $\psi$ is developable in sine and cosine series of multiples of $m _ { 1 } y _ { 1 } + \ldots + m _ { n } y _ { n }$

Thus having determined $S _ { z }$ completely we come to the fourth equation of (51)

$$
\sum n _ { i } ^ { \left( 0 \right) } \frac { \partial S _ { 3 } } { \partial y _ { i } } = \Phi .
$$

This is of the same form as (58) and can be solved in quite the same way.

# (II) The libration case.

Suppose that $C _ { 2 }$ is not greater than the maximum of $[ F _ { 1 } ]$ and hence $S _ { 1 }$ is not always real. Suppose for simplicity that $m _ { 1 } = 1$ ， $m _ { 2 } = \cdots =$ $m _ { n } = 0$ .Then we cannot so arrange that ${ \partial S _ { p } } / { \partial y _ { i } }$ be periodic in $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ ，but we can find a function $S _ { p }$ such that ${ \partial S _ { p } } / { \partial y _ { i } }$ are periodic in $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ . Denote by $[ U ]$ the mean value of $U$ considered as a periodic function of $y _ { 2 } , y _ { 3 } , \ldots , y _ { n } .$ We have then

$$
\Big [ \sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { p } } { \partial y _ { i } } \Big ] = \mathsf { c o n s t a n t } ,
$$

and

$$
\left[ \frac { \partial S _ { p } } { \partial y _ { 2 } } \right] , \left[ \frac { \partial S _ { p } } { \partial y _ { 3 } } \right] , \ldots , \left[ \frac { \partial S _ { p } } { \partial y _ { n } } \right]
$$

reduce to constants,and the relation (34) reduces to $n _ { 0 } ^ { ( 1 ) } = 0$ .Hence the left-hand member of (59) does not contain $[ \partial S _ { p } / \partial y _ { 1 } ]$ . Similarly to our suppositions (56) and (57) we consider $S _ { p }$ ， as well as ${ \partial S _ { p } } / { \partial y _ { i } }$ ，as periodic functions of $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ . Then the constant on the righthand side of (59) is zero.

We see from the second equation of (51) that $S _ { 1 }$ depends only on $y _ { 1 }$ and from the third equation that $S _ { 1 }$ is determined by taking its mean value

$$
\frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { 1 } ^ { 2 } } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } = C _ { 2 } - [ F _ { 1 } ] ,
$$

or

$$
- \sum n _ { i } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial S _ { 2 } } { \partial y _ { i } } = [ F _ { 1 } ] - F _ { 1 } .
$$

Since the right-hand member is a function of $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ ，whose mean value is zero, $S _ { z }$ can be determined except for an arbitrary function of $y _ { 1 }$ ,that is, $S _ { 2 } - [ S _ { 2 } ]$ can be determined by (61).By taking the mean value of the fourth equation of (51) we have

$$
{ \frac { { \hat { \partial } } ^ { 2 } F _ { 0 } } { \partial x _ { 1 } ^ { 2 } } } { \frac { \partial [ S _ { 2 } ] } { \partial y _ { 1 } } } { \frac { \partial S _ { 1 } } { \partial y _ { 1 } } } = [ \Phi ] .
$$

Hence we obtain $[ S _ { 2 } ]$ . The fourth equation of (51) is now written

$$
- \sum n _ { i } ^ {  } \frac { \partial S _ { 3 } } { \partial y _ { i } } = \Phi ,
$$

where $[ \Phi ] = 0$ . Hence $S _ { 3 } - [ S _ { 3 } ]$ can be determined from this equation similarly to the way in which $S _ { 2 } - [ S _ { 2 } ]$ has been calculated.It is remarked that ${ \partial S _ { p } } / { \partial y _ { i } }$ thus obtained are uniform functions of $y _ { 1 }$ and $\sqrt { \mathscr { C } _ { 2 } - [ F _ { 1 } ] }$

Now an auxiliary function $T$ is introduced

$$
\begin{array} { r } { \begin{array} { r l } & { T = T _ { 0 } + \sqrt { \mu } T _ { 1 } + \mu T _ { 2 } + \cdots , } \\ & { T _ { 0 } = x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } y _ { 1 } + \cdots + x _ { n } ^ { \scriptscriptstyle ( 0 ) } y _ { n } , } \end{array} } \end{array}
$$

where $x _ { i } ^ { ( 0 ) }$ are constants such that $F _ { 0 } = C _ { 0 } , n _ { 1 } ^ { ( 0 ) } = 0 . \ T _ { 0 }$ is nothing but the function $S _ { \mathfrak { o } }$ .We have for determining $T _ { \imath }$ an equation similar to (54), in which $S _ { 1 }$ and $C _ { 2 } ^ { \prime }$ are replaced by $T _ { 1 }$ and $C _ { 2 }$ ，respectively, that is,

$$
\frac { 1 } { 2 } \sum \ d \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { i } ^ { ( 0 ) } \partial x _ { k } ^ { ( 0 ) } } \frac { \partial T _ { 1 } } { \partial y _ { i } } \frac { \partial T _ { 1 } } { \partial y _ { k } } = C _ { 2 } - [ F _ { 1 } ] ,
$$

together with

$$
\begin{array} { r } { \frac { \partial T _ { 1 } } { \partial y _ { i } } = x _ { i } ^ { \prime } \qquad ( i = 2 , 3 , \ldots , n ) , } \end{array}
$$

where the $x _ { i } ^ { \prime }$ are not zero in this time.

Since $\partial ^ { 2 } F _ { 0 } / \partial x _ { i } ^ { ( 0 ) } \partial x _ { k } ^ { ( 0 ) }$ depend only on $\pmb { x } _ { i } ^ { ( 0 ) }$ ， they are constants.Hence, if ${ \partial T _ { 1 } } / { \partial y _ { i } }$ are replaced by $\pmb { x } _ { i } ^ { \prime }$ ，the equation (54a) becomes

$$
A \left( \frac { \partial T _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } + 2 B \frac { \partial T _ { 1 } } { \partial y _ { 1 } } + D = C _ { 2 } - \left[ F _ { 1 } \right] ,
$$

where $\pmb { A }$ is a constant and $B , D$ are homogeneous polynomials in $\boldsymbol { x } _ { i } ^ { \prime }$ ， whose first term is of the first degree and the second term is of the second degree.Thus we obtain

$$
\frac { \partial T _ { 1 } } { \partial y _ { 1 } } = - \frac { B } { A } \pm \sqrt { \frac { B ^ { 2 } } { A ^ { 2 } } - \frac { D } { A } + \frac { C ^ { 2 } } { A } - \frac { [ F _ { 1 } ] } { A } } .
$$

Put

$$
\frac { B ^ { 2 } } { A ^ { 2 } } - \frac { D } { A } + \frac { C _ { 2 } } { A } = x _ { 1 } ^ { \prime } , \qquad [ F _ { 1 } ] = A \psi ,
$$

then we have

$$
T _ { 1 } = x _ { 2 } ^ { \prime } y _ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { \prime } y _ { n } - \frac { B y _ { 1 } } { A } + \int d y _ { 1 } \sqrt { \overline { { x _ { 1 } ^ { \prime } - \psi } } } .
$$

The next coefficient $T _ { 2 }$ is determined by

$$
\sum n _ { i } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial T _ { \scriptscriptstyle 2 } } { \partial y _ { i } } = F _ { \scriptscriptstyle 1 } - [ F _ { \scriptscriptstyle 1 } ] ,
$$

which is analogous to (58） by which $S _ { 2 }$ has been determined. $T _ { 2 }$ is obtained from this equation, except for an arbitrary function of $y _ { 1 }$ Take $[ T _ { 2 } ] = 0$ and put

$$
\sum n _ { i } ^ { ( 0 ) } x _ { i } ^ { \prime } = - C _ { 1 } .
$$

We see from this equation that $T _ { \imath }$ is periodic in $y _ { i }$ but independent of $x _ { i } ^ { \prime }$ ，and that,since $T _ { \mathfrak { o } } , T _ { \mathfrak { r } } , T _ { \mathfrak { z } }$ satisfy the first three equations of (51), the left-hand side of (5O) reduces to $C _ { 2 } + \sqrt { \mu } C _ { 1 } + \mu C _ { 2 }$ ，with the exception of the term factored by $\mu \sqrt { \mu }$ ，where $s$ is replaced by $_ { T }$ in (50),provided that O on the right-hand side should be replaced by $C _ { 1 }$ in the second equation of (51).

Now put

$$
\begin{array} { r l } & { x _ { 1 } = \displaystyle \frac { \partial T } { \partial y _ { 1 } } = x _ { 1 } ^ { ( 0 ) } + \sqrt { \mu } \Big ( - \frac { B } { A } + \sqrt { x _ { 1 } ^ { \prime } - \psi } \Big ) + \mu \frac { \partial T _ { 2 } } { \partial y _ { 1 } } , } \\ & { y _ { 1 } ^ { \prime } = \displaystyle \frac { \partial T } { \partial x _ { 1 } ^ { \prime } } = \frac { \sqrt { \mu } } { 2 } \int \frac { d y _ { 1 } } { \sqrt { x _ { 1 } ^ { \prime } - \psi } } , } \\ & { x _ { i } = \displaystyle \frac { \partial T } { \partial y _ { i } } = x _ { i } ^ { ( 0 ) } + \sqrt { \mu } x _ { i } ^ { \prime } + \mu \frac { \partial T _ { 2 } } { \partial y _ { i } } , } \\ & { y _ { i } ^ { \prime } = \displaystyle \frac { \partial T } { \partial x _ { i } ^ { \prime } } = \sqrt { \mu } y _ { i } - \frac { \sqrt { \mu } y _ { 1 } } { A } \frac { \partial B } { \partial x _ { i } ^ { \prime } } ( i = 2 , 3 , \ldots , n ) . } \end{array}
$$

and take $\boldsymbol { x } _ { i } ^ { \prime }$ and $y _ { i } ^ { \prime }$ instead of $x _ { i }$ and $y _ { i }$ as the new variables.

Consider the third equation，which contains $y _ { 1 } ^ { \prime } , y _ { 1 }$ and $x _ { 1 } ^ { \prime }$ . If we suppose $x _ { 1 } ^ { \prime }$ as constant and let $y _ { 1 } ^ { \prime }$ only vary,then it can be proved that $y _ { 1 }$ is periodic in $y _ { 1 } ^ { \prime }$ Also $\sqrt { x _ { 1 } ^ { \prime } - \psi }$ ，consequently $\partial T _ { 1 } / \partial y _ { 1 ; }$ ,is a periodic function of $y _ { 1 } ^ { \prime }$ . These functions $y _ { 1 }$ and $\sqrt { x _ { 1 } ^ { \prime } - \psi }$ depend further on $x _ { 1 } ^ { \prime }$ ， which plays the role of the modulus of elliptic functions.Also we see that the period of these periodic functions is proportional to $\sqrt { \mu }$ Hence,in the case of libration, $x _ { 1 } , x _ { i } , y _ { 1 }$ and $y _ { i } ^ { \prime } - \sqrt { \mu } y _ { i }$ are periodic functions of $y _ { 1 } ^ { \prime }$ .The functions $x _ { 1 }$ and $x _ { 2 }$ depend on $y _ { i }$ but these are periodic with period $2 \pi$ in these $n - 1$ variables.If the old variables $x _ { i }$ and $y _ { i }$ are expressed as functions of the new variables $\boldsymbol { x } _ { i } ^ { \prime }$ and $y _ { i } ^ { \prime }$ ， then $x _ { i }$ ，cos $y _ { i }$ ，and sin $y _ { i }$ are periodic functions of $y _ { i } ^ { \prime }$ . The function ${ \pmb F }$ is also periodic with period $2 \pi$ in $y _ { i }$ . The period is equal to

$$
{ \sqrt { \mu } } \int _ { \alpha } ^ { \beta } { \frac { d y _ { 1 } } { { \sqrt { x _ { 1 } ^ { \prime } - \psi } } } } = { \sqrt { \mu } } P
$$

for $y _ { 1 } ^ { \prime }$ and equal to $\sqrt { \mu } \cdot 2 \pi$ for $y _ { i } ^ { \prime } , P$ being a function of $x _ { 1 } ^ { \prime }$ in the same way as the period of elliptic functions is a function of the modulus.

Write

$$
y _ { i } ^ { \prime } = { \sqrt { \mu } } z _ { i } ,
$$

then we have

$$
z _ { 1 } = \frac { 1 } { 2 } \int \frac { d y _ { 1 } } { \sqrt { x _ { 1 } ^ { \prime } - \psi } } , \qquad z _ { i } = y _ { i } - \frac { y _ { 1 } } { A } \frac { \partial B } { \partial x _ { i } ^ { \prime } } .
$$

$F$ becomes a periodic function of $z _ { i }$ . The period is equal to $P$ for $z _ { 1 }$ and equal to $2 \pi$ for $z _ { i }$ .Furthermore $F$ depends on $x _ { i } ^ { \prime }$ and is developable in powers of $\sqrt { \mu }$ in the form $C _ { 0 } + \sqrt { \mu } C _ { 1 } + \mu C _ { 2 } + \cdots ,$ ，where the first three terms are independent of $z _ { i }$ but are functions only of $x _ { i } ^ { \prime } . ~ C _ { 0 }$ is a constant,and $C _ { 1 }$ is a linear function of $x _ { i } ^ { \prime }$ independent of $x _ { 1 } ^ { \prime }$ .We have $C _ { 2 } = A x _ { 1 } ^ { \prime } + D - B ^ { 2 } / A$ ，whence $C _ { 2 }$ is a polynomial of the first degree with respect to the other variables $x _ { i } ^ { \prime }$

Now put

$$
F = C _ { 0 } + \sqrt { \mu } F ^ { * } ,
$$

then the equations (49) become

$$
\frac { d x _ { i } ^ { \prime } } { d t } = \frac { \partial F ^ { * } } { \partial z _ { i } } , \qquad \frac { d z _ { i } } { d t } = - \frac { \partial F ^ { * } } { \partial x _ { i } ^ { \prime } } ,
$$

where ${ \pmb { F } } ^ { * }$ is periodic with period $P$ with respect to $z _ { i }$ , but is periodic with period $2 \pi$ with respect to $z _ { 1 }$ . We further transform by

$$
u _ { 1 } = \int \frac { P d x _ { 1 } ^ { \prime } } { 2 \pi } , \qquad v _ { 1 } = \frac { 2 \pi z _ { 1 } } { P } .
$$

Then the equations become

$$
\begin{array} { r l r l } & { \frac { d u _ { 1 } } { d t } = \frac { \partial F ^ { * } } { \partial v _ { 1 } } , } & & { \frac { d x _ { i } ^ { \prime } } { d t } = \frac { \partial F ^ { * } } { \partial z _ { i } } , } \\ & { \frac { d v _ { 1 } } { d t } = - \frac { \partial F ^ { * } } { \partial u _ { 1 } } , } & & { \frac { d z _ { i } } { d t } = - \frac { \partial F ^ { * } } { \partial x _ { i } ^ { \prime } } ~ ( i = 2 , 3 , . . . , n ) , } \end{array}
$$

where $\pmb { F } ^ { * }$ is periodic with period $2 \pi$ with respect to $v _ { 1 } , z _ { 2 } , z _ { 3 } , \ldots , z _ { n }$ Also, ${ \pmb F } ^ { * }$ reduces to $C _ { 1 }$ for $\mu = 0$ $C _ { 1 }$ is independent of $C _ { 1 } ^ { \prime }$ ，and is a function only of $x _ { 2 } ^ { \prime } , \ldots , x _ { n } ^ { \prime } .$ because $n _ { 1 } ^ { ( 0 ) } = 0$ But $C _ { 2 }$ depends on $x _ { 1 } ^ { \prime }$ and consequently on $\pmb { u } _ { 1 }$ . Thus $C _ { 2 }$ depends only on $u _ { 1 } , x _ { 2 } ^ { \prime } , \ldots , x _ { n } ^ { \prime }$ . Hence there exist $_ n$ functions $u _ { 1 } , x _ { 2 } ^ { \prime } , \ldots , x _ { n } ^ { \prime }$ depending on $\pmb { n }$ variables $v _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ and $_ n$ arbitrary constants so that (i) when these functions are substituted in $\pmb { F } ^ { * }$ , it reduces to a constant, (ii) $u _ { 1 } d v _ { 1 } + x _ { 2 } ^ { \prime } d z _ { 2 } +$ $\cdots + x _ { n } ^ { \prime } d z _ { n } = d V$ is an exact differential,and (ii) these $\pmb { n }$ functions $u _ { 1 } , x _ { 2 } ^ { \prime } , \ldots , x _ { n } ^ { \prime }$ are periodic with period $2 \pi$ with respect to $v _ { 1 } , z _ { 2 } , \cdots , z _ { n }$ ·

If we define $\begin{array} { r } { d S = \sum x _ { i } d y _ { i } } \end{array}$ , then the system'

$$
\begin{array} { l l l } { { u _ { 1 } = \displaystyle \frac { \partial V } { \partial v _ { 1 } } , \qquad } } & { { x _ { i } ^ { \prime } = \displaystyle \frac { \partial V } { \partial z _ { i } } } } & { { ( i = 2 , 3 , \ldots , n ) , } } \\ { { \displaystyle u _ { 1 } = \displaystyle \int \frac { P d x _ { 1 } ^ { \prime } } { 2 \pi } , \qquad } } & { { v _ { 1 } = \displaystyle \frac { 2 \pi z _ { 1 } } { P } , } } & { { } } \\ { { \displaystyle x _ { k } = \displaystyle \frac { \partial T } { \partial y _ { k } } , \qquad } } & { { z _ { k } = \displaystyle \frac { \partial T } { \partial x _ { k } ^ { \prime } } \qquad ( k = 1 , 2 , \cdot \cdot , n ) , } } \end{array}
$$

and the system

$$
x _ { k } = { \frac { \partial S } { \partial y _ { k } } } \qquad ( k = 1 , 2 , \ldots , n ) ,
$$

are identical, provided that $V$ satisfies

$$
F ^ { * } \Big ( { \frac { \partial V } { \partial v _ { 1 } } } , { \frac { \partial V } { \partial z _ { i } } } , v _ { 1 } , z _ { i } \Big ) = \mathrm { c o n s t a n t } ,
$$

and that its derivatives are periodic with respect to $v _ { 1 } , z _ { i }$ and

$$
S = S _ { 0 } + \sqrt { \mu } S _ { 1 } + \mu S _ { 2 } + \cdot \cdot \cdot .
$$

The function $V$ is developable in powers of $\sqrt { \mu }$

$$
\begin{array} { r l } & { V = V _ { 0 } + \sqrt { \mu } V _ { 1 } + \mu V _ { 2 } + \cdots , } \\ & { V _ { i } = \beta _ { i } ^ { \scriptscriptstyle ( 1 ) } v _ { 1 } + \beta _ { i } ^ { \scriptscriptstyle ( 2 ) } z _ { 2 } + \cdots + \beta _ { i } ^ { \scriptscriptstyle ( n ) } z _ { n } + V _ { i } ^ { \prime } , } \end{array}
$$

where $V _ { i } ^ { \prime }$ are periodic and $_ n$ arbitrary constants $\beta _ { i } ^ { ( k ) }$ are suitably chosen. Then to each function $V$ there corresponds a unique function $s$ and vice versa.

If $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ are considered to be constant, then ${ x _ { 1 } } = \partial S / \partial y _ { 1 }$ is formally an equation for a closed curve, that is,we can find a function $\Phi _ { p }$ of $y _ { 1 }$ and $\mu$ ，developable in powers of $\sqrt { \mu }$ such that

$$
x _ { 1 } = \frac { \partial S _ { 0 } } { \partial y _ { 1 } } + \sqrt { \mu } \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + \mu \frac { \partial S _ { 2 } } { \partial y _ { 1 } } + \cdot \cdot \cdot + \mu ^ { p / 2 } \frac { \partial S _ { p } } { \partial y _ { 1 } } + \mu ^ { ( p + 1 ) / 2 } \Phi _ { p } ,
$$

is a closed curve.We say formally by meaning that, if $\mu$ tends to infinity,then the series may be divergent.

# (III) The limiting case.

Suppose that $C _ { 2 }$ is equal to the maximum of $[ F _ { 1 } ]$ , and put $m _ { 1 } = 1$ ， $m _ { i } = 0$ $0 \left( i = 2 , 3 , \ldots , n \right)$ ， and hence that $n _ { 1 } ^ { ( 0 ) } = 0$ . Then $\sqrt { \overline { { C _ { 2 } - [ F _ { 1 } ] } } } ,$ accordingly ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ ,isa periodic function of $y _ { 1 }$ with period not $2 \pi$ but $4 \pi$ ，and the radical changes its sign when $y _ { 1 }$ increases by $2 \pi$ ， vanishes for a single value of $y _ { 1 }$ in the interval O to $2 \pi$ ，where $[ F _ { 1 } ]$ has the maximum value.Without loss of generality we suppose that this value of $y _ { 1 }$ is equal to zero.Then we have $\partial S _ { \mathrm { 1 } } / \partial y _ { \mathrm { 1 } } = 0$ for $y _ { 1 } =$ $2 k \pi$ ，with any integer $k$ .By the equations (60) and (62)，which can be written

$$
\frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { 1 } ^ { 2 } } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } = C _ { 2 } - [ F _ { 1 } ] ,
$$

$$
\frac { \partial ^ { 2 } F _ { \scriptscriptstyle 0 } } { \partial x _ { \scriptscriptstyle 1 } ^ { \scriptscriptstyle 2 } } \frac { \partial [ S _ { \scriptscriptstyle p } ] } { \partial y _ { \scriptscriptstyle 1 } } \frac { \partial S _ { \scriptscriptstyle 1 } } { \partial y _ { \scriptscriptstyle 1 } } = \phi _ { p + 1 } ( y _ { \scriptscriptstyle 1 } ) + C _ { p + 1 } ,
$$

the functions $S _ { p }$ can be determined by recurrence so that the ${ \partial S _ { p } } / { \partial y _ { i } }$ are periodic functions with period $2 \pi$ with respect to $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ and $4 \pi$ with respect to $y _ { 1 }$ . Since the constants $C _ { p }$ of the equation (51） are zero for $p$ odd, the equations (51） do not change when $y _ { 1 }$ increases by $2 \pi$ or when $\sqrt { \mu }$ changes its sign.Hence ${ \partial S _ { p } } / { \partial y _ { i } }$ changes to $( - 1 ) ^ { p } \partial S _ { p } / \partial y _ { i }$ when $y _ { 1 }$ increases by $2 \pi$ . Thus ${ \partial S _ { p } } / { \partial y _ { i } }$ is periodic with period $2 \pi$ with respect to $y _ { 1 }$ if $p$ is even. If $p$ is odd,the function changes its sign.

It can be proved that ${ \partial S _ { p } } / { \partial y _ { i } }$ are finite, provided that

$$
\phi _ { p + 1 } ( 0 ) + C _ { p + 1 } = \phi _ { p + 1 } ( 2 \pi ) + C _ { p + 1 } = 0 ,
$$

or $\phi _ { p + 1 } ( 0 ) = \phi _ { p + 1 } ( 2 \pi )$ if $p$ is odd, and $\phi _ { p + 1 } ( 0 ) = \phi _ { p + 1 } ( 2 \pi ) = 0$ if $p$ is even (Poincaré, 1893,pp.368-383).

As to concrete examples see Sections 2.4,2.19, 8.17, 9.7,and 9.22.

# 14.12BOHLIN'S SERIES

We have obtained the principal function $s$ in the preceding.The coordinates as functions of time are derived by applying Jacobi's theorem (Section 1.12).

For simplicity we suppose that $m _ { 1 } = 1$ ， $m _ { 2 } = \cdots = m _ { n } = 0$ . The function $s$ defined in Section 14.11 depends on $n$ variables $y _ { k }$ and $\pmb { n }$ arbitrary constants $\mathcal { X } _ { 2 } ^ { ( 0 ) } , \ldots , \mathcal { X } _ { n } ^ { ( 0 ) } , C _ { 2 }$ Put

$$
x _ { k } = \frac { \partial S } { \partial y _ { k } } , \qquad \theta _ { 1 } w _ { 1 } = \frac { \partial S } { \partial C _ { 2 } } , \qquad w _ { i } + \theta _ { i } w _ { 1 } = \frac { \partial S } { \partial x _ { i } ^ { ( 0 ) } }
$$

$$
( i = 2 , 3 , \ldots , n ; k = 1 , 2 , \ldots , n ) ,
$$

where $\theta _ { i }$ are functions of $C _ { 2 }$ and $x _ { i } ^ { ( 0 ) }$ . From these equations we can deduce $x _ { k }$ and $y _ { k }$ as functions of $w _ { k } , x _ { i } ^ { ( 0 ) }$ and $C _ { 2 }$ . Since $\theta _ { k }$ depend only on the constants $C _ { 2 }$ and $x _ { i } ^ { ( 0 ) }$ ，the $\theta _ { k }$ are constants and hence $w _ { k }$ are linear functions of time. The $\theta _ { k }$ are so chosen that $x _ { k }$ ，cos $y _ { k }$ ，sin $y _ { k }$ are periodic functions of $w _ { k }$ with period $2 \pi$

(I) The revolution case.

Suppose that ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ is always real and does not vanish.Then ${ \partial S _ { q } } / { \partial y _ { k } }$ $/ \partial y _ { k } \ ( q = 1 , 2 , . . . , p )$ are periodic functions of $y _ { k }$ with period $2 \pi$ We have

$$
\begin{array} { r } { S = S ^ { \prime } + \beta _ { 1 } y _ { 1 } + \cdot \cdot \cdot + \beta _ { n } y _ { n } , } \end{array}
$$

where $S ^ { \prime }$ is a periodic function of $y _ { k }$ ,and $\beta _ { \kappa }$ depend on $x _ { i } ^ { ( 0 ) }$ and $C _ { 2 }$ $S ^ { \prime }$ and $\beta _ { \kappa }$ are developable in powers of $\sqrt { \mu }$ Since $\alpha _ { i } ^ { ( 1 ) } = 0$ by (57), we have

$$
\beta _ { 2 } = x _ { 2 } ^ { \scriptscriptstyle ( 0 ) } , \qquad \beta _ { 3 } = x _ { 3 } ^ { \scriptscriptstyle ( 0 ) } , \ldots , \beta _ { n } = x _ { n } ^ { \scriptscriptstyle ( 0 ) } ,
$$

and the first term of the expansion of $\beta _ { 1 }$ in powers of $\sqrt { \mu }$ is $x _ { 1 } ^ { ( 0 ) }$

It can be proved that, when $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ are changed respectively to $w _ { 1 } + 2 k _ { 1 } \pi , w _ { 2 } + 2 k _ { 2 } \pi , \ldots , w _ { n } + 2 k _ { n } \pi ,$ ，with integers $k _ { \kappa }$ ，the variables $x _ { k }$ and $y _ { k }$ are changed to $x _ { k }$ and $y _ { \kappa } + 2 k _ { \kappa } \pi$ respectively. The $x _ { 1 } ^ { ( 0 ) }$ is related to $x _ { i } ^ { ( 0 ) }$ by (52)，which reduces to $n _ { 1 } ^ { ( 0 ) } = 0$ in the present case. Thus we obtain, for $\mu = 0$ ，

$$
\theta _ { 1 } = \frac { \partial x _ { 1 } ^ { ( 0 ) } } { \partial C _ { 2 } } = 0 , \qquad \theta _ { i } = \frac { \partial x _ { 1 } ^ { ( 0 ) } } { \partial x _ { i } ^ { ( 0 ) } } .
$$

From the first and third equations of (68) we have for $\mu = 0$

$$
x _ { k } = x _ { k } ^ { \scriptscriptstyle ( 0 ) } , \qquad w _ { 1 } + \frac { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } w _ { i } = y _ { 1 } + \frac { \partial x _ { 1 } ^ { \scriptscriptstyle ( 0 ) } } { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } y _ { i } .
$$

The second equation reduces to

$$
\theta _ { 1 } ^ { \prime } w _ { 1 } = \frac { \partial S _ { 1 } } { \partial C _ { 2 } } ,
$$

since $\sqrt { \mu } \theta _ { 1 }$ is the first term of the expansion of $\theta _ { 1 }$ in powers of $\sqrt { \mu }$ With the notation of Section 14.11 we have

$$
\theta _ { 1 } ^ { \prime } w _ { 1 } = \frac { \partial } { \partial C _ { 2 } } \int \sqrt { \frac { C _ { 2 } - [ F _ { 1 } ] } { A } } d y _ { 1 } = \frac { 1 } { 2 \sqrt { A } } \int \frac { d y _ { 1 } } { \sqrt { C _ { 2 } - [ F _ { 1 } ] } } .
$$

The right-hand member is expanded in the form $\gamma y _ { 1 } + \psi ( y _ { 1 } )$ ，where $\gamma$ is a constant depending on $C _ { 2 }$ and $x _ { i } ^ { ( 0 ) }$ ，and $\psi$ is a periodic function. We determine $\theta _ { 1 } ^ { \prime }$ by $\theta _ { 1 } ^ { \prime } = \gamma$ ，then we have $\gamma ( w _ { 1 } - y _ { 1 } ) = \psi$

On the other hand we have

$$
\frac { \partial w _ { 1 } } { \partial y _ { 1 } } = \frac { 1 } { 2 \gamma \sqrt { A } } \frac { 1 } { \sqrt { C _ { 2 } - [ F _ { 1 } ] } } = \frac { 1 } { 2 \gamma A ( \partial S _ { 1 } / \partial y _ { 1 } ) } .
$$

Since ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ is always of the same sign, $\partial w _ { 1 } / \partial y _ { 1 }$ is always positive, so that $w _ { 1 }$ is an increasing function of $y _ { 1 }$ ，and increases by $2 \pi$ when $y _ { 1 }$ increases by $2 \pi$ . Conversely $y _ { 1 }$ is an increasing function of $w _ { 1 }$ and increases by $2 \pi$ when $w _ { 1 }$ increases by $2 \pi$ .Hence we have $y _ { 1 } = w _ { 1 } + \eta .$ where $\eta$ is a function of $w _ { 1 }$ with period $2 \pi$ . Thus we see that the first term of the expansion of $x _ { k } , y _ { 1 } , y _ { i }$ are respectively $x _ { k } ^ { \left( 0 \right) } , w _ { 1 } + \eta , w _ { i } -$ $( { \partial x _ { 1 } ^ { ( 0 ) } } / { \partial x _ { i } ^ { ( 0 ) } } ) \eta .$ ，and that the following terms are periodic with respect to $w _ { k }$ ，and hence that $x _ { k }$ and $y _ { k } - w _ { k }$ are periodic functions of $w _ { k }$

We have seen that $w _ { k }$ are of the form

$$
w _ { k } = n _ { k } t + \varpi _ { k }
$$

with integration constants $\varpi _ { k }$ . In the expansion

$$
C = C _ { 0 } + \mu C _ { 2 } + \mu ^ { 2 } C _ { 4 } + \cdot \cdot \cdot ,
$$

$C _ { \mathfrak { o } }$ is a function of $x _ { i } ^ { \left( 0 \right) } ; C _ { 4 } , C _ { 6 } , \ldots$ are functions of $C _ { 2 }$ and $x _ { i } ^ { ( 0 ) }$ .By the method of Jacobi we have

$$
\theta _ { 1 } n _ { 1 } = - { \frac { \partial C } { \partial C _ { 2 } } } , \qquad n _ { i } + \theta _ { i } n _ { 1 } = - { \frac { \partial C } { \partial x _ { i } ^ { ( 0 ) } } } .
$$

Since $C$ and $\theta _ { \kappa }$ are given as functions of $C _ { 2 }$ and $x _ { i } ^ { ( 0 ) }$ ， these equations determine $n _ { k }$ as functions of $C _ { 2 }$ and $x _ { i } ^ { \left( 0 \right) }$ ， developed in powers of $\sqrt { \mu }$ The first term of the expansion of $n _ { 1 }$ is $\sqrt { \mu } / \gamma$ ,so that $n _ { 1 } = 0$ for $\mu = 0$ and $n _ { i } = - ( \partial C _ { 0 } / \partial x _ { i } ^ { ( 0 ) } ) = n _ { i } ^ { ( 0 ) }$ for $\mu = 0$

(II) The libration case.   
Suppose that ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ can vanish and is not always real. It can be shown that

$$
{ \frac { \partial S _ { p } } { \partial y _ { 1 } } } , { \frac { \partial S _ { p } } { \partial y _ { 2 } } } , \ldots , { \frac { \partial S _ { p } } { \partial y _ { n } } }
$$

are of the form

$$
\sum \frac { A } { ( \partial S _ { 1 } / \partial y _ { 1 } ) ^ { q } } \cos { ( p _ { 2 } y _ { 2 } + \cdot \cdot \cdot + p _ { n } y _ { n } ) } ,
$$

where $q , p _ { 2 } , \ldots , p _ { n }$ are integers and $\pmb { A }$ is a periodic function of $y _ { 1 }$ which is always finite.

In fact, suppose that $\partial S _ { 1 } / \partial y _ { k } , \ldots , \partial S _ { p - 1 } / \partial y _ { k }$ are of the form (70). The derivatives $\partial S _ { p } / \partial y _ { k }$ are defined by

$$
\sum _ { i = 2 } ^ { n } n _ { i } ^ { \left( 0 \right) } \frac { \partial S _ { p } } { \partial y _ { i } } = \Phi ,
$$

where $\Phi$ is a function of the form (7O), because the sum or the product or the derivatives of functions of the form (7O) are also of the form (70).From this equation $\partial S _ { p } / \partial y _ { 2 } , \ldots , \partial S _ { p } / \partial y _ { n } , S _ { p } - [ S _ { p } ]$ can be determined in the form (7O).Thus we obtain

$$
\begin{array} { r } { \frac { \partial [ S _ { p } ] } { \partial y _ { 1 } } \frac { \partial S _ { p } } { \partial y _ { 1 } } = [ \Phi ] , } \end{array}
$$

where $[ \Phi ]$ is of the form (70).Hence $\partial [ S _ { p } ] / \partial y _ { 1 }$ ， and consequently ${ \partial S _ { p } } / { \partial y _ { 1 } }$ ，are of the form (70).

Then the equations (68） give the unknown quantities $x$ and $\boldsymbol { y }$ as functions of $w$ .However we may proceed in the following manner.

Take the variables $u _ { 1 } , v _ { 1 } , x _ { i } , z _ { i }$ ,instead of $x _ { k }$ and $y _ { \kappa }$ ， as functions of $\pmb { n }$ integration constants and $_ n$ linear functions of time $w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ,$ such that $u _ { 1 } , v _ { 1 } - w _ { 1 } , x _ { i } ^ { \prime } , z _ { i } - w _ { i }$ are periodic functions of $\boldsymbol { w }$ and developable in powers of $\sqrt { \mu }$ .We have $w _ { k } = n _ { k } t + \varpi _ { k }$ ，where $\varpi _ { k }$ are the integration constants and $n _ { i }$ are developable in powers of $\sqrt { \mu } ,$ with $n _ { i } ( 0 )$ as the first term； but the expansion of $n _ { 1 }$ begins with a term of the order $\sqrt { \mu }$ since $n _ { 1 } ^ { ( 0 ) } = 0$

Consider a function $V$ which depends on $v _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ and $\pmb { n }$ integration constants $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ ，such that $V - \lambda _ { 1 } v _ { 1 } - \lambda _ { 2 } z _ { 2 } - \cdots$ $- ~ \lambda _ { n } z _ { n }$ is a periodic function of $v _ { 1 }$ and $z _ { i }$ ，and that

$$
u _ { 1 } = { \frac { \partial V } { \partial v _ { 1 } } } , \qquad x _ { i } ^ { \prime } = { \frac { \partial V } { \partial z _ { i } } } , \qquad w _ { k } = { \frac { \partial V } { \partial \lambda _ { k } } } .
$$

It can be shown (Poincaré,1892) that (73) are derived from (68). For the proof we put

$$
\begin{array} { l } { d V = u _ { 1 } d v _ { 1 } + \displaystyle \sum _ { i = 2 } \ d x _ { i } ^ { \prime } d z _ { i } + \displaystyle \sum _ { k = 1 } \ d w _ { k } d \lambda _ { k } , } \\ { d T = \displaystyle \sum _ { k = 1 } ^ { n } x _ { k } d y _ { k } + \sqrt { \mu } \sum _ { k = 1 } ^ { n } z _ { k } d x _ { k } ^ { \prime } , \qquad v _ { 1 } d u _ { 1 } = z _ { 1 } d x _ { 1 } ^ { \prime } , } \\ { S = \sqrt { \mu } V + T - \sqrt { \mu } \bigg ( \displaystyle \sum _ { i = 2 } ^ { n } z _ { i } x _ { i } ^ { \prime } + u _ { 1 } v _ { 1 } \bigg ) , } \end{array}
$$

then we obtain

$$
\begin{array} { l } { d T = \displaystyle \sum _ { k = 1 } ^ { n } x _ { k } d y _ { k } + \sqrt { \mu } \displaystyle \sum _ { i = 2 } ^ { n } z _ { i } d x _ { i } ^ { \prime } + \sqrt { \mu } v _ { 1 } d u _ { 1 } , } \\ { d S = \displaystyle \sum _ { k = 1 } ^ { n } x _ { k } d y _ { k } + \sqrt { \mu } \displaystyle \sum _ { k = 1 } ^ { n } w _ { k } d \lambda _ { k } , } \end{array}
$$

and hence

$$
x _ { k } = \frac { \partial S } { \partial y _ { k } } , \qquad \sqrt \mu w _ { k } = \frac { \partial S } { \partial \lambda _ { k } } \qquad ( k = 1 , 2 , \ldots , n ) .
$$

Here $V$ is expressed as a function of $v _ { 1 } , z _ { i } , \lambda _ { k } ; T$ as a function of $u _ { 1 } ,$ $x _ { i } ^ { \prime } , y _ { k } ^ { \prime } ; S$ as a function of $\lambda _ { k } , y _ { k }$ $( k = 1 , 2 , \dots , n ; i = 2 , 3 , \dots , n )$ We have $6 n$ variables $x _ { k } , y _ { k } , u _ { 1 } , v _ { 1 } , x _ { i } ^ { \prime } , z _ { i } , \lambda _ { k } , w _ { k }$ ,but there are relations among them:

$$
\begin{array} { r l r } { \displaystyle x _ { k } = \frac { \partial T } { \partial y _ { k } } \mathrm { , ~ } } & { { } \displaystyle \sqrt { \mu } z _ { i } = \frac { \partial T } { \partial x _ { i } ^ { \prime } } \mathrm { , ~ } } & { \displaystyle \sqrt { \mu } v _ { 1 } = \frac { \partial T } { \partial u _ { 1 } } , } \\ { \displaystyle u _ { 1 } = \frac { \partial V } { \partial v _ { 1 } } \mathrm { , ~ } } & { { } \displaystyle x _ { i } ^ { \prime } = \frac { \partial V } { \partial z _ { i } } \mathrm { , ~ } } & { \displaystyle w _ { k } = \frac { \partial V } { \partial \lambda _ { k } } , } \end{array}
$$

and there are only $_ { 2 n }$ independent variables.It can be seen that the function $s$ of (74) is obtained if we replace the constants $\boldsymbol { x } _ { i } ^ { ( 0 ) }$ and $C _ { 2 }$ in the function $s$ of the revolution case respectively by $x _ { i } ^ { ( 0 ) } + \sqrt { \mu } \lambda _ { i }$ and $\phi ( x _ { 2 } ^ { ( 0 ) } , x _ { 3 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } , \lambda _ { 2 } , \lambda _ { 3 } , \ldots , \lambda _ { n } )$ .Comparing (68） with (75）we see that

$$
\begin{array} { r } { \frac { \partial S } { \partial \lambda _ { 1 } } = \frac { \partial S } { \partial C _ { 2 } } \frac { \partial \phi } { \partial \lambda _ { 1 } } , \qquad \frac { \partial S } { \partial \lambda _ { i } } = \frac { \partial S } { \partial C _ { 2 } } \frac { \partial \phi } { \partial \lambda _ { i } } + \sqrt { \mu } \frac { \partial S } { \partial x _ { i } ^ { ( 0 ) } } , } \end{array}
$$

and hence that

$$
\sqrt { \mu } w _ { 1 } = \theta _ { 1 } w _ { 1 } \frac { \partial \phi } { \partial \lambda _ { 1 } } , \qquad \sqrt { \mu } w _ { i } = \theta _ { 1 } w _ { 1 } \frac { \partial \phi } { \partial \lambda _ { i } } + \sqrt { \mu } ( w _ { i } + \theta _ { i } w _ { 1 } ) .
$$

Hence $\theta _ { \kappa }$ of (68） should be replaced by

$$
\theta _ { 1 } = \frac { \sqrt { \mu } } { \partial \phi / \partial \lambda _ { 1 } } , \theta _ { i } = - \frac { \partial \phi / \partial \lambda _ { i } } { \partial \phi / \partial \lambda _ { 1 } } ,
$$

for obtaining (75) from (68).

(III) The limiting case.

Suppose that $C _ { 2 }$ is equal to the maximum of $[ F _ { 1 } ]$ Suppose that

$$
F = { \frac { \partial F } { \partial y _ { 1 } } } = { \frac { \partial F } { \partial y _ { i } } } = { \frac { \partial F } { \partial x _ { 1 } } } = 0 , \qquad { \mathrm { f o r } } \qquad x _ { 1 } = x _ { i } = y _ { 1 } = 0 ,
$$

and consequently that the expansions of $F _ { 1 } , F _ { 2 } , \ldots , F _ { n }$ in powers of $x _ { 1 } , x _ { i } , y _ { 1 }$ contain neither zero-degree terms nor first-degree terms other than those depending on $x _ { 2 } , x _ { 3 } , \ldots , x _ { n }$ Thus,if $x _ { 2 } ^ { ( 0 ) } = x _ { 3 } ^ { ( 0 ) } = \cdot \cdot \cdot =$ $x _ { n } ^ { ( 0 ) } = 0 , C _ { 2 } = C _ { 4 } = \cdot \cdot \cdot = 0$ ，whence we have $x _ { 1 } ^ { ( 0 ) } = C _ { 0 } = 0$ ，then this is the limiting case,and the function $s$ is such that ${ \partial S _ { p } } / { \partial y _ { 1 } }$ have each a simple zero-point and ${ \partial S _ { p } } / { \partial y _ { i } }$ have each a double zero-point for $y _ { 1 } = 0$ . If we give values near zero to the constants $x _ { 2 } ^ { ( 0 ) } , x _ { 3 } ^ { ( 0 ) } , \ldots ,$ $\pmb { x } _ { \pmb { \pi } } ^ { ( 0 ) }$ ， then we can choose $C _ { 2 } , C _ { 4 } , \ldots$ ，so that $C _ { 2 }$ is still equal to the maximum of $[ F _ { 1 } ]$ and that the conditions $\phi _ { p + 1 } ( 0 ) + C _ { p + 1 } = \phi _ { p + 1 } ( 2 \pi )$ $+ C _ { p + 1 } = 0$ ，(67) of Section 14.11,are satisfied,while the functions $S _ { 1 } , S _ { 2 } , \ldots , S _ { p }$ remain finite.

The values of $C _ { 2 } , C _ { 4 }$ ，... satisfying these conditions are holomorphic functions of $x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$ ，so that $C _ { p } = \phi _ { p } ( x _ { 2 } ^ { ( 0 ) } , \dots , x _ { n } ^ { ( 0 ) } )$ should vanish for $x _ { 2 } ^ { ( 0 ) } = \cdots = x _ { n } ^ { ( 0 ) } = 0$ . Thus $s$ is determined depending on $n - 1$ arbitrary constants $x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) }$ in the form

$$
S = \beta _ { 1 } y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { ( 0 ) } y _ { n } + S ^ { \prime } ,
$$

where $\beta _ { 1 }$ is a constant and $s \prime$ is expanded in sines and cosines of multiples of $y _ { 1 } / 2 , y _ { 2 } , \ldots , y _ { n }$ Also $S ^ { \prime }$ is holomorphic with respect to $x _ { i } ^ { ( 0 ) }$ ， such that ${ \partial S } / { \partial y _ { 1 } }$ admits a simple zero-point for $y _ { 1 } = 0$ and the other derivatives ${ \partial S } / { \partial y _ { i } }$ admit each a double zero-point. Put

$$
\begin{array} { l l l } { { C _ { 0 } = \phi _ { 0 } ( x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } ) , \ } } & { { } } & { { C _ { 2 } = \lambda + \phi _ { 2 } ( x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } ) , } } \\ { { \ } } & { { \nonumber } } & { { C _ { 4 } = \phi _ { 4 } ( x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } ) , \ } } & { { \ \ldots \ . } } \end{array}
$$

The derivatives of $s$ should be of the form (7O).Moreover，when we write a term of one of these derivatives in the form (7O),then the numerator $\pmb { A }$ does not depend on $\gimel$ ，according to the supposition just made. In such a case we say that it is of the form (7Oa). We can prove that, if $\partial S _ { 1 } / \partial y _ { k } , \partial S _ { 2 } / \partial y _ { k } , . . . , \partial S _ { p - 1 } / \partial y _ { k }$ are of the form (70a), then ${ \partial S _ { p } } / { \partial y _ { k } }$ are also of the form (70a).

In fact, the right-hand member of (71) is of the form (7Oa).Hence $\partial S _ { p } / \partial y _ { 2 } , \partial S _ { p } / \partial y _ { 3 } , \ldots , \partial S _ { p } / \partial y _ { n } , S _ { p } - [ S _ { p } ]$ are of the same form. Let $\partial S _ { p } / \partial y _ { 1 } - \partial [ S _ { p } ] / \partial y _ { 1 }$ be of the form

$$
\sum \ : A \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q } \sin ^ { \phantom { * } } ( \omega ) , \qquad \omega = p _ { 2 } y _ { 2 } + \cdots + p _ { n } y _ { n } ,
$$

then the derivative is

$$
\sum \frac { \partial A } { \partial y _ { 1 } } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q } \sin \left( \omega \right) - \sum _ { q = 2 } ^ { \infty } A \frac { \partial } { \partial y _ { 1 } } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } \cdot \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q - 2 } \sin \left( \omega \right) .
$$

If $\pmb { A }$ is independent of $\gimel$ ，then ${ \partial A } / { \partial y _ { 1 } }$ is independent of . On the other hand, $( \partial S _ { 1 } / \partial y _ { 1 } ) ^ { 2 }$ is, except for a constant factor, equal to $\lambda + \phi _ { 2 } - [ F _ { 2 } ]$ Hence $\partial ( \partial S _ { 1 } / \partial y _ { 1 } ) ^ { 2 } / \partial y _ { 1 }$ is independent of $\lambda$ ，so that (77) is independent of $\lambda$

Furthermore,the right-hand member of (72) is of the form (70a). Hence $\partial [ S _ { p } ] / \partial y _ { 1 }$ and ${ \partial S _ { p } } / { \partial y _ { 1 } }$ are also of the same form. Thus $s$ isof the form

$$
\begin{array} { r } { S = \displaystyle et { } { ' } \sum _ { A } A \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q } \sin ^ { * } ( \omega ) + \displaystyle et { } { ' } \sum _ { A } A _ { 1 } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q } d y _ { 1 } } \\ { + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { ( 0 ) } y _ { n } , } \end{array}
$$

where $\pmb { A }$ admits a zeropoint of order $q + 2$ for $\lambda = x _ { 2 } ^ { ( 0 ) } = \cdots = x _ { n } ^ { ( 0 ) }$ $= 0$ and $\pmb { A } _ { 1 }$ admits a zeropoint of order $q + 1$ for $y _ { 1 } = 0$

Thus we are to consider the equations analogous to (68)

$$
x _ { k } = \frac { \partial S } { \partial y _ { k } } , \qquad \theta _ { 1 } w _ { 1 } = \frac { \partial S } { \partial \lambda } , \qquad w _ { i } + \theta _ { i } w _ { 1 } = \frac { \partial S } { \partial x _ { i } ^ { ( 0 ) } } ,
$$

where we put $\lambda = x _ { i } ^ { ( 0 ) } = 0$ after the differentiation, but we can, even before the differentiation,put $\lambda = x _ { i } ^ { ( 0 ) } = 0$ in the first equation, $\boldsymbol { x } _ { i } ^ { ( 0 ) }$ $= 0$ in the second,and $\lambda = 0$ in the third equation. The first equation shows that $x _ { k }$ can be expanded in sines and cosines of multiples of $y _ { 1 } / 2 , y _ { 2 } , \ldots , y _ { n }$ . If we put $\lambda = 0$ in the third equation,then we see that $s$ is of the form (76) and hence by differentiating (76) that

$$
w _ { 1 } \theta _ { i } + w _ { i } = y _ { 1 } \frac { \partial \beta _ { 1 } } { \partial x _ { i } ^ { ( 0 ) } } + y _ { i } + \frac { \partial S ^ { \prime } } { \partial x _ { i } ^ { ( 0 ) } } .
$$

The last term is developable in sines and cosines of multiples of $y _ { 1 } / 2$ ， $y _ { 2 } , \ldots , y _ { n }$ . Next we differentiate (78) after putting $x _ { i } ^ { ( 0 ) } = 0$ ， then we obtain

$$
\frac { \partial S _ { 1 } } { \partial y _ { 1 } } = D \sqrt { \lambda - \left[ F _ { 1 } \right] } ,
$$

where $_ D$ is a constant.Hence we find

$$
\begin{array} { r } { \frac { \partial S } { \partial \lambda } = - \displaystyle \sum _ { q = 2 } \frac { A D ^ { 2 } } { 2 } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q - 2 } \sin \left( \omega \right) } \\ { + \displaystyle \int \sum _ { q = 2 } \frac { A _ { 1 } D ^ { 2 } } { 2 } \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { - q - 2 } d \mathfrak { x } _ { 1 } , } \end{array}
$$

where we put $\lambda = 0$ after the differentiation.For $y _ { 1 } = 0$ the derivative ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ admits a simple zero, $\pmb { A }$ a zero of order $q + 2$ ，and $\boldsymbol { A } _ { 1 }$ a zero of order $q + 1$ .While the first term of (81) remains finite, the integrand admits a simple infinity for $y _ { 1 } = 2 k \pi$ .Hence it is written

$$
{ \frac { \alpha } { 2 \sin { ( y _ { 1 } / 2 ) } } } + f ( y _ { 1 } ) ,
$$

where $f ( y _ { 1 } )$ is a finite and periodic function. The integral becomes logarithmically infinite for $y _ { 1 } = 0 , 2 \pi , \ldots$ ，so that it is of the form $\alpha$ log tan $( y _ { 1 } / 4 ) + \psi$ ，with a periodic function $\psi$ of $y _ { 1 }$ which remains finite for all values of $y _ { 1 }$ and $\alpha$ .Thus

$$
\frac { \partial S } { \partial \lambda } = \alpha \log \tan \frac { y _ { 1 } } { 4 } + \gamma y _ { 1 } + \Theta ,
$$

where $\boldsymbol { \gamma }$ is a new constant and $\Theta$ is a function developable in sines and cosines of multiples of $y _ { 1 } / 2 , y _ { 2 } , \ldots , y _ { n }$ Hence

$$
w _ { 1 } \theta _ { 1 } = \alpha \log \tan \frac { y _ { 1 } } { 4 } + \gamma y _ { 1 } + \Theta .
$$

We can determine $y _ { i }$ as functions of $w$ by (80) and (82),in which the right-hand members are expanded in powers of $\sqrt { \mu }$ . Due to the presence of the logarithmic term, $w _ { 1 }$ varies from -o to $+ \infty$ as $y _ { 1 }$ varies from O to $2 \pi$ ,for all possible values of $y _ { i }$ . Moreover the Jacobian $\Delta$ of the right-hand members of (80) and (82) with respect to $y _ { 1 } , y _ { 2 } ;$ $\ldots , y _ { n }$ does not vanish,and remains of the same sign.Hence $y _ { k }$ are uniform functions of $w$ for all real values of $w$ .Furthermore, $y _ { 1 } , y _ { i }$ $- \ w _ { i }$ are periodic functions of $w _ { 2 } , \ldots , w _ { n }$ Also $x _ { k }$ are uniform functions of $w$ and periodic with respect to $w _ { 2 } , \ldots , w _ { n }$ For $w _ { 1 } = \infty , y _ { 1 }$ $= 0$ ，we see from (82) that

$$
w _ { i } = y _ { i } + \frac { \partial S ^ { \prime } } { \partial x _ { i } ^ { ( 0 ) } } ,
$$

from which we obtain $y _ { 2 } , \ldots , y _ { n }$ as functions of $w _ { 2 } , \ldots , w _ { n }$ ，and $y _ { i } - w _ { i }$ are periodic with respect to $w _ { 2 } , \ldots , w _ { n }$ . The first equation of

(79) gives $x _ { k } = 0$ for $y _ { 1 } = 0$ . Thus we obtain a particular solution of (79) by putting

$$
x _ { 1 } = x _ { i } = y _ { 1 } = 0 , y _ { i } = w _ { i } + \eta _ { i } .
$$

These equations give a generalization of periodic solutions. $x _ { k } , y _ { 1 } ,$ $y _ { i } - w _ { i }$ are expressed as periodic functions of $n - 1$ arguments $w _ { i } = n _ { i } t + \varpi _ { i }$ .In the case of two degrees of freedom there is only one argument $w _ { 2 }$ ，and $x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } - w _ { 2 }$ are expressed as periodic functions of $w _ { 2 }$ ， consequently of time.

If $w _ { 1 }$ becomes negatively infinite, then $y _ { 1 }$ becomes very small and the right-hand member of (8O） is developed in increasing powers of $y _ { 1 }$ . The equation (82) is transformed to

$$
\exp \left\{ { \frac { w _ { 1 } } { \alpha } } \right\} = \tan { \frac { y _ { 1 } } { 2 } } \cdot \exp \left\{ { \frac { \gamma y _ { 1 } } { 2 } } \right\} \cdot \exp \left\{ { \frac { \Theta } { \alpha } } \right\} .
$$

If $\alpha > 0$ ，then exp $\{ w _ { \mathrm { 1 } } / \alpha \}$ is very small and the right-hand member of (84) is developed in powers of $y _ { 1 }$ .Thus we can write (80) and (82) in the form

$$
w _ { i } = y _ { i } + \psi _ { i } , \qquad \exp { \{ w _ { 1 } / \alpha \} } = \psi _ { 1 } ,
$$

where $\psi _ { i }$ are developed in powers of $y _ { 1 }$ and $\sqrt { \mu }$ ，and the coefficients of the expansion are periodic with respect to $y _ { 2 } , y _ { 3 } , \ldots , y _ { n } $ Hence both sides of the equations (85) are developed in powers of $y _ { 1 } , \cdot \sqrt { \mu }$ and exp $\{ w _ { 1 } / \alpha \}$ ，where $\alpha$ is also developable in powers of $\sqrt { \mu }$ ,its first term being $\sqrt { \mu } \alpha _ { 1 }$ . On the other hand, the first terms of the expansions of $\gamma$ and $\Theta$ are factored by $\sqrt { \mu }$ ， so that the expansions of $\gamma / \alpha$ and $\Theta / \alpha$ begin with terms independent of $\sqrt { \mu }$ Put $\mu = 0$ in (85)，then we obtain

$$
w _ { i } = y _ { i } + \frac { \partial x _ { 1 } ^ { ( 0 ) } } { \partial x _ { i } ^ { ( 0 ) } } y _ { 1 } , \qquad \exp \left\{ \frac { w _ { 1 } } { \alpha } \right\} = \exp \left\{ \frac { \partial S _ { 1 } } { \alpha _ { 1 } \partial \lambda } \right\} .
$$

The Jacobian of the right-hand members with respect to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ is equal to 1 for $y _ { 1 } = 0$ .Hence for all values of $w _ { 2 } , \ldots , w _ { n }$ the functions $y _ { \kappa }$ are developable in powers of $\sqrt { \mu }$ and exp $\{ w _ { 1 } / \alpha \}$ ，whose coeffcients are functions of $w _ { 2 } , w _ { 3 } , \ldots , w _ { n }$ .Moreover $w _ { i }$ increases by $2 \pi$ when $y _ { i }$ increases by $2 \pi$ .Hence $y _ { 1 }$ and $y _ { i } \mathrm { ~ - ~ } w _ { i }$ are developable in powers of $\sqrt { \mu }$ and exp $\{ w _ { \mathrm { 1 } } / \alpha \}$ ,whose coefficients are periodic functions of $w _ { 2 } , \ldots , w _ { n }$ .Then the first equation of (79） gives $x _ { k }$ developable in series of the same form.

If, instead of supposing $w _ { 1 } < 0$ and $\left| w _ { 1 } \right|$ very large and $y _ { 1 }$ nearly equal to zero, we suppose $w _ { 1 } > 0$ and very large and $y _ { 1 }$ nearly equal to $2 \pi$ , then we get the same result, provided that we replace exp $\{ w _ { 1 } / \alpha \}$ by exp $\{ - w _ { 1 } / \alpha \}$ in the expansions.

These are asymptotic solutions which will be discussed in Sections 19.7-19.10. The series in powers of $\sqrt { \mu }$ and the exponential do not converge, but, if they are expanded in powers of the exponential alone, they are convergent in the case of two degrees of freedom,but cannot be convergent in the case of more than two degrees of freedom (Poincaré,1892).

# 14.13EXTENSION OF BOHLIN'S THEORY

Divide the variables in two groups $x _ { 1 } , x _ { 2 } , \ldots , x _ { p } ; z _ { 1 } , z _ { 2 } , \ldots , z _ { q }$ and let the corresponding conjugate variables be $y _ { 1 } , y _ { 2 } , \ldots , y _ { p } ; u _ { 1 } , u _ { 2 } , \ldots ,$ $u _ { q }$ . Suppose that $F _ { 0 }$ depends on $x _ { i }$ ，but not on $z _ { j }$ ，as in the case of the three-body problem. Consider the Hamilton-Jacobi equation

$$
F \Big ( \frac { \partial S } { \partial y _ { i } } , \frac { \partial S } { \partial u _ { j } } , y _ { i } , u _ { j } \Big ) = C ,
$$

and expand $s$ in powers of $\sqrt { \mu }$ ， so that its derivatives are periodic with respect to $y _ { i }$ and $u _ { j }$

For $\mu = 0$ we have

$$
F _ { 0 } \Big ( \frac { \partial S _ { 0 } } { \partial y _ { 1 } } , \frac { \partial S _ { 0 } } { \partial y _ { 2 } } , \dots , \frac { \partial S _ { 0 } } { \partial y _ { p } } \Big ) = C _ { 0 } .
$$

Hence we obtain

$$
S _ { 0 } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + \cdot \cdot \cdot + x _ { p } ^ { ( 0 ) } y _ { p } + T _ { 0 } ,
$$

where $T _ { \mathfrak { o } }$ depends only on $u _ { j }$ . Put further

$$
n _ { i } ^ { \left( 0 \right) } = - \frac { \partial F _ { 0 } } { \partial x _ { i } ^ { \left( 0 \right) } } .
$$

If there is no linear homogeneous relation with integer coefficients among ${ n } _ { i } ^ { ( 0 ) }$ ，then the solution will be obtained，for example，by Lindstedt's theory, in the form of a series arranged in powers of $\mu$ instead of in powers of $\sqrt { \mu }$ .Suppose that there is such a linear relation and let $n _ { 1 } ^ { ( 0 ) } = 0$ be the one.

Let $\pmb { U }$ be a periodic function of $y _ { i }$ depending on $\boldsymbol { u } _ { j }$ . Denote by $[ U ]$ the mean value as a function of $y _ { 2 } , y _ { 3 } , \ldots , y _ { n }$ ，and by $\left[ \left[ U \right] \right]$ the mean value as a function of $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ $[ U ]$ is a function of $y _ { 1 }$ and $u _ { j }$ ， while $[ [ U ] ]$ is a function of $\boldsymbol { u } _ { j }$ only.Suppose that the derivatives of $U$ ，not $\pmb { U }$ itself,are periodic such that

$$
U = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + \cdot \cdot \cdot + x _ { p } ^ { ( 0 ) } y _ { p } + U ^ { \prime } ,
$$

where $U ^ { \prime }$ is periodic and $x _ { i } ^ { ( 0 ) }$ are constants, and put

$$
\begin{array} { r } { [ U ] = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + \cdot \cdot \cdot + x _ { p } ^ { ( 0 ) } y _ { p } + [ U ^ { \prime } ] , } \\ { { \scriptsize [ [ U ] ] } = x _ { 1 } ^ { ( 0 ) } y _ { 1 } + \cdot \cdot \cdot + x _ { p } ^ { ( 0 ) } y _ { p } + [ [ U ^ { \prime } ] ] } \end{array}
$$

The first equation of (51） in the beginning of Section 14.11 is nothing but (87). The second equation of (51) shows that $\partial S _ { 1 } / \partial y _ { 2 } , \ldots ,$ ${ \partial S _ { 1 } } / { \partial y _ { n } }$ are constants.We can suppose that the constants are zero without loss of generality. Then $S _ { 1 }$ is no more a function of $y _ { i }$ and $\boldsymbol { u } _ { j }$ ， so that we have $S _ { 1 } = [ S _ { 1 } ]$

The function $\Phi$ in the right-hand member of the third equation of (51) is $- { \pmb { F } } _ { 1 }$ . The second term on the left-hand side reduces to

$$
\frac { 1 } { 2 } \frac { { \partial ^ { 2 } } { F _ { 0 } } } { { \partial { x _ { 1 } ^ { ( 0 ) 2 } } } } \ : \left( { \frac { { \partial { S _ { 1 } } } } { { \partial { y _ { 1 } } } } } \right) ^ { 2 } .
$$

Put

$$
\frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 0 } } { \partial x _ { 1 } ^ { ( 0 ) 2 } } = A ,
$$

then the equation becomes

$$
- \sum n _ { i } ^ { ( 0 ) } \frac { \partial S _ { 2 } } { \partial y _ { i } } + A \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } = C _ { 2 } - F _ { 1 } .
$$

$\boldsymbol { F } _ { 1 }$ depends on $x _ { i } , z _ { i } , y _ { j } , u _ { j }$ and is known. We replace in $F _ { 1 }$ the variables $x _ { i }$ by known constants $\boldsymbol { x } _ { i } ^ { ( 0 ) }$ and the variables $z _ { j }$ by unknown functions $\partial S _ { 0 } / \partial u _ { j } = \partial T _ { 0 } / \partial u _ { j }$ . Take the mean values with respect to $y _ { 2 } , \ldots , y _ { n }$ ，then $[ \partial S _ { 2 } / \partial y _ { i } ]$ reduce to constants which we suppose to be equal to zero, without loss of generality. Since $S _ { \imath }$ and $\partial T _ { 0 } / \partial u _ { j }$ do not depend on $y _ { 2 } , \ldots , y _ { n }$ ，we have

$$
A \left( { \frac { \partial S _ { 1 } } { \partial y _ { 1 } } } \right) ^ { 2 } = C _ { 2 } - [ F _ { 1 } ] ,
$$

from which we derive

$$
\frac { \partial S _ { 1 } } { \partial y _ { 1 } } = \sqrt { \frac { C _ { 2 } - [ F _ { 1 } ] } { A } } .
$$

Taking the mean value with respect to $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ we obtain

$$
\begin{array} { r } { \Big [ \Big [ \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \Big ] \Big ] = \Big [ \Big [ \frac { \sqrt { C _ { 1 } - [ F _ { 1 } ] } } { A } \Big ] \Big ] . } \end{array}
$$

If the derivatives of $S _ { 1 }$ are periodic,then the left-hand member is a constant which is denoted by $h$ . Thus

$$
\left[ \left[ \sqrt { \frac { C _ { 2 } - [ F _ { 1 } ] } { A } } \right] \right] = h ,
$$

or

$$
\int _ { 0 } ^ { 2 \pi } \sqrt { C _ { 2 } - [ F _ { 1 } ] } \cdot d y _ { 1 } = 2 \pi A h .
$$

The left-hand member depends on $\boldsymbol { u } _ { j }$ and the derivatives ${ \partial T _ { 0 } } / { \partial u _ { j } }$ which enter in $F _ { 1 }$ . Hence this can be looked upon as a partial differential equation defining $T _ { \mathfrak { d } }$ .Suppose that $\scriptstyle { { T _ { 0 } } }$ is such that its derivatives are periodic,then (9O) takes the form

$$
\Theta \Bigl ( \frac { \partial T _ { 0 } } { \partial u _ { j } } , u _ { j } \Bigr ) = 2 \pi A h .
$$

Suppose that the integration of this equation is possible and that the complete integral is

$$
T _ { 0 } = z _ { 1 } ^ { ( 0 ) } u _ { 1 } + \cdot \cdot \cdot + z _ { q } ^ { ( 0 ) } u _ { q } + T _ { 0 } ^ { \prime } ,
$$

where $z _ { j } ^ { ( 0 ) }$ are the integration constants,and $T _ { \mathfrak { o } } ^ { \prime }$ depends on $u _ { j }$ and $z _ { j } ^ { ( 0 ) }$ and is periodic with respect to $u _ { j }$ . Then $T _ { \mathfrak { d } }$ is known. ${ \partial S _ { 1 } } / { \partial y _ { 1 } }$ and hence $S _ { 1 } - [ [ S _ { 1 } ] ]$ can be determined.Hence $S _ { 1 } = S _ { 1 } ^ { \prime } + T _ { 1 } \mathrm { { : } }$ ，where $S _ { 1 } ^ { \prime }$ is a known function of $y _ { 1 }$ and $u _ { j }$ ，and $T _ { \imath }$ is as yet an unknown function of $\boldsymbol { u } _ { j } ^ { \prime }$ .Then (88） gives

$$
- \sum n _ { i } ^ { \scriptscriptstyle ( 0 ) } \frac { \partial S _ { 2 } } { \partial y _ { i } } = [ F _ { 1 } ] - F _ { 1 } ,
$$

whence

$$
\frac { \partial S _ { 2 } } { \partial y _ { 2 } } , \frac { \partial S _ { 2 } } { \partial y _ { 3 } } , . . . , \frac { \partial S _ { 2 } } { \partial y _ { n } } , S _ { 2 } - [ S _ { 2 } ]
$$

are obtained.

We can proceed by a similar manner to the calculation of higherorder terms.

Consider now the integration of the equation (90). In the three-body problem the function $F$ is expanded in positive powers of $\mu , \xi _ { 1 } , \xi _ { 1 } ^ { \prime } , \eta _ { 1 } ,$ $\eta _ { 1 } ^ { \prime } , p , q , p ^ { \prime } , q ^ { \prime }$ and in sines and cosines of multiples of $\lambda _ { 1 }$ and $\lambda _ { 1 } ^ { \prime }$ . A term sos $( m \lambda _ { 1 } + m ^ { \prime } \lambda _ { 1 } ^ { \prime } )$ is factoredbya monomialof degree atleast $| m + m ^ { \prime } | ,$ or differing from $| m + m ^ { \prime } |$ only by an even integer, in $\xi _ { 1 } , \eta _ { 1 } , p , q , \dots .$ Finally $F _ { 0 }$ depends only on $\Lambda _ { 1 }$ and $\Lambda _ { 1 } ^ { \prime }$

Suppose that we have a relation

$$
m { \frac { \partial { \cal F } _ { 0 } } { \partial \Lambda _ { 1 } ^ { ( 0 ) } } } + m ^ { \prime } { \frac { \partial { \cal F } _ { 0 } } { \partial \Lambda _ { 1 } ^ { \prime ( 0 ) } } } = 0 ,
$$

where $\Lambda _ { 1 } ^ { ( 0 ) }$ and $\Lambda _ { 1 } ^ { \prime ( 0 ) }$ are the constants which are put equal to ${ \partial S _ { 0 } } / { \partial \lambda _ { 1 } }$ and ${ \partial S _ { 0 } } / { \partial \lambda _ { 1 } ^ { \prime } }$ respectively，analogously to $x _ { i } ^ { ( 0 ) }$ in the above discussion. Put

$$
m \lambda _ { 1 } + m ^ { \prime } \lambda _ { 1 } ^ { \prime } = y _ { 1 } .
$$

$[ F _ { 1 } ]$ is formed if all terms depending on $\lambda _ { 1 }$ or $\lambda _ { 1 } ^ { \prime }$ ， except for the one depending only on $y _ { 1 }$ ，are taken off. Replace the variables $\xi _ { 1 } , \eta _ { 1 } , \xi _ { 1 } ^ { \prime } , \eta _ { 1 } ^ { \prime } ;$ $p , q , p ^ { \prime } , q ^ { \prime }$ respectively by $\varepsilon \hat { \xi } _ { 1 } , \varepsilon \eta _ { 1 } , \varepsilon \hat { \xi } _ { 1 } ^ { \prime } , \varepsilon \eta _ { 1 } ^ { \prime } , \varepsilon p , \varepsilon q , \varepsilon p ^ { \prime } , \varepsilon q ^ { \prime }$ ,then we obtain

$$
[ F _ { 1 } ] = R + R ^ { \prime } ,
$$

where $\pmb R$ is an aggregate of terms independent of both $\lambda _ { 1 }$ and $\lambda _ { 1 } ^ { \prime }$ so that

$$
R = [ [ F _ { 1 } ] ] ,
$$

and $R ^ { \prime }$ is an aggregate of terms depending only on $y _ { 1 }$ . Thus we have

$$
R = R _ { 0 } + \varepsilon ^ { 2 } R _ { 2 } + \varepsilon ^ { 4 } R _ { 4 } + \cdot \cdot \cdot .
$$

$\pmb { R } ^ { \prime }$ is divisible by $\varepsilon ^ { ( m + m ^ { \prime } ) }$ ， where $| m + m ^ { \prime } | > 2$ ， so that we can write $R ^ { \prime } = { \varepsilon } ^ { 3 } R ^ { \prime \prime }$ $R _ { 0 }$ depends only on $\Lambda _ { 1 } ^ { ( 0 ) }$ and $\Lambda _ { 1 } ^ { \prime ( 0 ) }$ ，which are constants. Hence we can put $C _ { 2 } = R _ { 0 } + k _ { 0 } ^ { 2 } + \varepsilon ^ { 2 } k _ { 1 } , A h = k _ { 0 } + \varepsilon ^ { 2 } k _ { 1 } ^ { \prime }$ ，so that (90) can be written

$$
\int _ { 0 } ^ { 2 \pi } { \sqrt { { \bar { k } } _ { 0 } ^ { 2 } + \varepsilon ^ { 2 } k _ { 1 } - \varepsilon ^ { 2 } R _ { 2 } - \varepsilon ^ { 3 } R ^ { \prime \prime } - \varepsilon ^ { 4 } R _ { 4 } - \dots \dots } } d y _ { 1 } = 2 \pi ( k _ { 0 } + \varepsilon ^ { 2 } k _ { 1 } ^ { \prime }
$$

Expanding the square root we obtain

$$
\frac { k _ { 1 } - R _ { 2 } } { 2 k _ { 0 } } + \varepsilon Z = k _ { 1 } ^ { \prime } ,
$$

or

$$
k _ { 1 } - 2 k _ { \scriptscriptstyle 0 } k _ { \scriptscriptstyle 1 } ^ { \prime } = K , ~ R _ { \scriptscriptstyle 2 } - 2 \varepsilon k _ { \scriptscriptstyle 0 } Z = K ,
$$

where $z$ represents a function developable in positive powers of $\varepsilon , \xi _ { : }$ $\eta , p , q$ ·

We transform the variables by

$$
\begin{array} { r l } { \dot { \varepsilon } = \sqrt { \Lambda _ { 1 } } { \cdot } e \cos \varpi , \qquad } & { \eta = - \sqrt { \Lambda _ { 1 } } { \cdot } e \sin \varpi , } \\ { \dot { \xi } ^ { \prime } = \sqrt { \Lambda _ { 1 } ^ { \prime } } { \cdot } e ^ { \prime } \cos \varpi ^ { \prime } , \qquad } & { \eta ^ { \prime } = - \sqrt { \Lambda _ { 1 } ^ { \prime } } { \cdot } e ^ { \prime } \sin \varpi ^ { \prime } , } \\ { p = \sqrt { \Lambda _ { 1 } } { \cdot } I \cos \theta , \qquad } & { q = - \sqrt { \Lambda _ { 1 } } { \cdot } I \sin \theta , } \\ { p ^ { \prime } = \sqrt { \Lambda _ { 1 } ^ { \prime } } { \cdot } I ^ { \prime } \cos \theta ^ { \prime } , \qquad } & { q ^ { \prime } = - \sqrt { \Lambda _ { 1 } ^ { \prime } } { \cdot } I ^ { \prime } \sin \theta ^ { \prime } , } \end{array}
$$

then, as in Section 14.7, $\pmb R$ becomes a function of $\Lambda _ { 1 } , \Lambda _ { 1 } ^ { \prime } , \lambda _ { 1 } , \lambda _ { 1 } ^ { \prime } , \rho _ { i } , \omega _ { i }$ $( i = 1 , 2 )$ ,and $\pmb { R } _ { 2 }$ reduces to

$$
\begin{array} { r } { 2 A _ { 1 } \rho _ { 1 } + 2 A _ { 2 } \rho _ { 2 } + 2 A _ { 3 } \rho _ { 3 } + 2 A _ { 4 } \rho _ { 4 } . } \end{array}
$$

Replacing $\rho _ { i }$ by $\partial T _ { 0 } / \partial \omega _ { i }$ the equation to be satisfied is

$$
\Theta \Big ( \frac { \partial T _ { 0 } } { \partial \omega _ { i } } , \omega _ { i } \Big ) = R _ { 2 } - 2 \varepsilon k _ { 0 } Z = K .
$$

The left-hand member is periodic in $\omega _ { i }$ ，and developable in powers of $\varepsilon$ .It reduces to $\pmb { R } _ { 2 }$ for $\varepsilon = 0$ ，and depends only on ${ \partial T _ { 0 } } / { \partial \omega _ { i } }$ but not on $\dot { \boldsymbol { \omega } } _ { i }$ .Hence we can solve this equation by the ordinary method of Lindstedt (Section 14.9). Thus the integration of the equation (90) in the present problem is made possible.

The case $m + m ^ { \prime } = \pm 1$ or $\pm 2$ can be treated in a similar manner. The case $m + m ^ { \prime } = 0$ ，where $\Lambda _ { 1 } ^ { ( 0 ) } = \Lambda _ { 1 } ^ { \prime ( 0 ) }$ ,is difficult to discuss.

Suppose that the function $s$ has been determined. Our next problem is to solve

$$
\frac { \partial S } { \partial x _ { k } ^ { ( 0 ) } } = w _ { k } + \theta _ { k } w _ { 1 } \qquad ( k > 1 )
$$

$$
\frac { \partial S } { \partial C _ { 2 } } = \theta _ { 1 } w _ { 1 } , \qquad \frac { \partial S } { \partial z _ { i } ^ { ( 0 ) } } = w _ { i } ^ { \prime } + \theta _ { i } ^ { \prime } w _ { 1 } ,
$$

$$
x _ { i } = \frac { \partial S } { \partial y _ { i } } , \qquad z _ { i } = \frac { \partial S } { \partial u _ { i } } ,
$$

where $\theta$ and $\theta ^ { \prime }$ are suitably chosen functions of $\bar { x _ { i } ^ { ( 0 ) } }$ and $\boldsymbol { z } _ { i } ^ { ( 0 ) }$ . The problem is to obtain $x _ { i } , y _ { i } , u _ { i }$ as functions of $x _ { i } ^ { ( 0 ) } , z _ { i } ^ { ( 0 ) } , w _ { i } , w _ { i } ^ { \prime }$ and replace $w _ { i }$ and $w _ { i } ^ { \prime }$ by linear functions of time with suitably chosen coefficients.

Since the derivatives of $s$ are periodic, $s$ can be written

$$
S = \beta y _ { 1 } + x _ { 2 } ^ { ( 0 ) } y _ { 2 } + \cdot \cdot \cdot + x _ { p } ^ { ( 0 ) } y _ { p } + z _ { 1 } ^ { ( 0 ) } u _ { 1 } + \cdot \cdot \cdot + z _ { q } ^ { ( 0 ) } u _ { q } + S ^ { \prime } ,
$$

where $\beta$ is independent of $y$ and $\pmb { u }$ ，and $s \prime$ is periodic with respect to $y$ and $\pmb { u }$ . The coefficients of $y _ { \ k } , k > 1$ ，and $u _ { i }$ can be considered to be equal to $\boldsymbol { x } _ { k } ^ { ( 0 ) }$ and $\boldsymbol { z } _ { i } ^ { ( 0 ) }$ respectively, that is, we adopt the hypothesis (57) without loss of generality. Furthermore we have

$$
\beta = \beta _ { 0 } + \sqrt { \mu } \beta _ { 1 } + \mu \beta _ { 2 } + \cdot \cdot \cdot ,
$$

where $\beta _ { 0 } = x _ { 1 } ^ { ( 0 ) }$ and $\beta _ { 1 } = h$ of (90),and

$$
{ \cal S } ^ { \prime } = { \cal S } _ { 0 } ^ { \prime } + \sqrt { \mu } { \cal S } _ { 1 } ^ { \prime } + \cdots ,
$$

$$
S _ { 0 } ^ { \prime } = T _ { 0 } ^ { \prime } , \qquad S _ { 1 } ^ { \prime } = \int { \left( \sqrt { \frac { { \overline { { C _ { 2 } - \left[ F _ { 1 } \right] } } } } { A } } - h \right) } d y _ { 1 } + T _ { 1 } ^ { \prime } .
$$

Thus (91) are written

$$
\begin{array} { c } { { w _ { i } + \theta _ { i } w _ { 1 } = y _ { i } + \displaystyle \frac { \partial \beta } { \partial x _ { i } ^ { ( 0 ) } } y _ { 1 } + \displaystyle \frac { \partial S ^ { \prime } } { \partial x _ { i } ^ { ( 0 ) } } , } } \\ { { { } } } \\ { { \theta _ { 1 } w _ { 1 } = \displaystyle \frac { \partial \beta } { \partial C _ { 2 } } y _ { 1 } + \displaystyle \frac { \partial S ^ { \prime } } { \partial C _ { 2 } } , } } \\ { { { } } } \\ { { w _ { k } ^ { \prime } + \theta _ { k } ^ { \prime } w _ { 1 } = u _ { k } + \displaystyle \frac { \partial \beta } { \partial z _ { k } ^ { ( 0 ) } } y _ { 1 } + \displaystyle \frac { \partial S ^ { \prime } } { \partial z _ { k } ^ { ( 0 ) } } . } } \end{array}
$$

Hence we take

$$
\theta _ { i } = \frac { \partial \beta } { \partial x _ { i } ^ { \left( 0 \right) } } , \qquad \theta _ { 1 } = \frac { \partial \beta } { \partial C _ { 2 } } , \qquad \theta _ { k } ^ { \prime } = \frac { \partial \beta } { \partial z _ { k } ^ { \left( 0 \right) } } .
$$

Since $\beta _ { 0 } = x _ { 1 } ^ { ( 0 ) }$ depends neither on $C _ { 2 }$ nor on $\boldsymbol { z } _ { k } ^ { ( 0 ) }$ ， the functions $\theta _ { 1 }$ and $\theta _ { \kappa } ^ { \prime }$ vanish for $\mu = 0$ and divisible by $\sqrt { \mu }$ But $\partial S ^ { \prime } / \partial C _ { 2 }$ reduces to $\partial T _ { 0 } ^ { \prime } / \partial C _ { 2 }$ and does not vanish for $\mu = 0$

Now

$$
w _ { k } = n _ { k } t + \varpi _ { k } , \qquad w _ { k } ^ { \prime } = n _ { k } ^ { \prime } t + \varpi _ { k } ^ { \prime } ,
$$

where $n _ { k }$ are determinate constants and $\varpi _ { k }$ arbitrary constants.The function $\pmb { F }$ ，when $x _ { k }$ and $z _ { k }$ are replaced by $\partial S / \partial y _ { k }$ and ${ \partial S } / { \partial u _ { k } }$ respectively, is equal to a constant depending on $x _ { i } ^ { ( 0 ) }$ ， $C _ { 2 }$ and $z _ { k } ^ { ( 0 ) }$ .Let it be $F = \phi ( x _ { i } ^ { ( 0 ) } , C _ { 2 } , z _ { k } ^ { ( 0 ) } )$ . Then we have

$$
n _ { i } + \theta _ { i } n _ { 1 } = - \frac { \partial \phi } { \partial x _ { i } ^ { \scriptscriptstyle ( 0 ) } } \qquad ( i > 1 ) ,
$$

$$
\theta _ { 1 } n _ { 1 } = - \frac { \partial \phi } { \partial C _ { 2 } } , \qquad n _ { k } ^ { \prime } + \theta _ { k } ^ { \prime } n _ { 1 } = - \frac { \partial \phi } { \partial z _ { k } ^ { ( 0 ) } } .
$$

$n _ { \kappa }$ are expanded in powers of $\sqrt { \mu }$ . Also we expand

$$
\begin{array} { c } { { \phi = C _ { 0 } + \mu C _ { 2 } + \mu ^ { 2 } C _ { 4 } + \cdots , } } \\ { { { } } } \\ { { C _ { 0 } = F _ { 0 } ( x _ { 1 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } ) , } } \end{array}
$$

then we obtain

$$
\frac { \partial C _ { 0 } } { \partial x _ { i } ^ { ( 0 ) } } = \frac { \partial F _ { 0 } } { \partial x _ { i } ^ { ( 0 ) } } + \frac { \partial F _ { 0 } } { \partial x _ { 1 } ^ { ( 0 ) } } \frac { \partial x _ { 1 } ^ { ( 0 ) } } { \partial x _ { i } ^ { ( 0 ) } } = - n _ { i } ^ { ( 0 ) } - n _ { 1 } ^ { ( 0 ) } \frac { \partial x _ { 1 } ^ { ( 0 ) } } { \partial x _ { i } ^ { ( 0 ) } } = - n _ { i } ^ { ( 0 ) } ,
$$

$$
\begin{array} { r } { n _ { 1 } ^ { ( 0 ) } = 0 . } \end{array}
$$

On the other hand,we see that

$$
\frac { \partial \phi } { \partial C _ { 2 } } = \mu
$$

and the expansion of $\partial \phi / \partial z _ { k } ^ { ( 0 ) }$ begins with a term of $\mu ^ { 2 }$ . Since $\theta _ { 1 }$ of the second equation of (93) is divisible by $\sqrt { \mu }$ and the right-hand member by $\pmb { \mu }$ ，we see that the expansion of $n _ { 1 }$ begins with a term in $\sqrt { \mu }$ . Since $\theta _ { k } ^ { \prime }$ are divisible by $\sqrt { \mu }$ in the third equation, $\theta _ { k } ^ { \prime } n _ { 1 }$ are divisible by $\mu$ and the right-hand member by $\mu ^ { 2 }$ ， the third equation shows that $n _ { k } ^ { \prime }$ are divisible by μ.

We discuss the equation (89) instead of (90). Take the variables $\Lambda _ { 1 } , \Lambda _ { 1 } ^ { \prime } , \lambda _ { 1 } , \lambda _ { 1 } ^ { \prime } , \rho _ { k } , \omega _ { k }$ .It is noted that both sides of (89) depend on $\lambda _ { 1 }$ and $\lambda _ { 1 } ^ { \prime }$ only through the combination $m \lambda _ { 1 } + m ^ { \prime } \lambda _ { 1 } ^ { \prime } = y _ { 1 }$ ； that they depend on $\Lambda _ { 1 }$ and $\Lambda _ { 1 } ^ { \prime }$ which are now replaced by $\Lambda _ { 1 } ^ { ( 0 ) }$ and $\Lambda _ { 1 } ^ { \prime ( 0 ) }$ ， respectively,and $\pmb { A }$ is a constant； that they are periodic with respect to $y _ { 1 }$ and $\omega _ { k }$ ； and finally that they are expanded in integral powers of $\varepsilon$ and in fractional powers of $\rho _ { k }$ which are now replaced by $\partial T _ { \mathfrak { o } } / \partial \omega _ { \varepsilon }$ Thus (89) takes the form

$$
H \Big ( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } , \frac { \partial T _ { 0 } } { \partial \omega _ { k } } , y _ { 1 } , \omega _ { k } \Big ) = C _ { 2 } .
$$

Expanding in powers of $\varepsilon$ we obtain successively the coefficients of the terms of $\varepsilon ^ { 0 } , \varepsilon ^ { 1 } , \varepsilon ^ { 2 }$ in the form

$$
A \left( \frac { \partial S _ { 1 } } { \partial y _ { 1 } } \right) ^ { 2 } + R _ { 0 } , \qquad 0 , \qquad R _ { 2 } + 2 A _ { 1 } \varrho _ { 1 } + 2 A _ { 2 } \varrho _ { 2 } + 2 A _ { 3 } \varrho _ { 3 } + 2 A _ { 4 } \varrho .
$$

where $R _ { 0 }$ is a constant depending on $\Lambda _ { 1 } ^ { ( 0 ) }$ and $\Lambda _ { 1 } ^ { \prime ( 0 ) }$ . Expand $S _ { 1 }$ of (94) in powers of $\varepsilon$

$$
\begin{array} { r l } & { S _ { 1 } = U _ { 0 } + \varepsilon U _ { 1 } + \varepsilon ^ { 2 } U _ { 2 } + \cdot \cdot \cdot , } \\ & { } \\ & { C _ { 2 } = \gamma _ { 0 } + \varepsilon \gamma _ { 1 } + \varepsilon ^ { 2 } \gamma _ { 2 } + \cdot \cdot \cdot , \quad T _ { 0 } = V _ { 0 } + \varepsilon V _ { 1 } + \cdot \cdot \cdot , } \end{array}
$$

where $\scriptstyle { \pmb { T } } _ { 0 }$ is replaced by its value in the averaged expression $\pmb R$ in the form:

$$
R = R _ { 0 } ^ { \prime } + \varepsilon ^ { 2 } R _ { 2 } ^ { \prime } + \varepsilon ^ { 3 } R _ { 3 } ^ { \prime } + \cdot \cdot \cdot .
$$

Equating the coefficients of $\varepsilon ^ { 0 } , \varepsilon ^ { 1 } , \varepsilon ^ { 2 } , \dots$ of the equation (94) we see that $\gamma _ { 1 } = U _ { 1 } = 0$ ， $\gamma _ { 2 } =$ constant, $\gamma _ { 3 } = U _ { 3 } = 0$ ，....We also obtain the equation

$$
2 \alpha A \frac { \partial U _ { q } } { \partial y _ { 1 } } + R _ { q } ^ { \prime } + M _ { q } \cos y _ { 1 } + N _ { q } \sin y _ { 1 } = \gamma _ { q } ,
$$

from the coefficients of $\varepsilon ^ { 1 \ : m + m ^ { \prime } \ : 1 }$ ， where $| m + m ^ { \prime } | = q$ and $M _ { q }$ and $N _ { q }$

depend on $\omega _ { k } , V _ { 0 } , V _ { 1 } , \ldots , V _ { q - 3 }$ ， which are known functions of $\omega _ { k }$ We have

$$
R _ { q } ^ { \prime } = 2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } + L _ { q } ,
$$

where $L _ { q }$ is a known function of $\omega _ { k }$ . We split this equation into

$$
2 \alpha { \cal A } \frac { \partial U _ { q } } { \partial y _ { 1 } } = - M _ { q } \cos y _ { 1 } + N _ { q } \sin y _ { 1 } ,
$$

$$
2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } = \gamma _ { q } - L _ { q } .
$$

The right-hand members being known, the values of $U _ { q }$ and $V _ { q - 2 }$ can be obtained from these equations. The derivatives of $V _ { q - 2 }$ are periodic with respect to $\omega _ { k }$ . Without loss of generality we suppose that the mean value of $\gamma _ { q } - L _ { q }$ vanishes.Then $V _ { q - 2 }$ itself is periodic and $U _ { q }$ is also periodic with respect to $y _ { 1 }$ and $\omega _ { k }$

By continuing this process we arrive, in equating the coefficients of $\varepsilon ^ { p } , p > q$ ，at

$$
2 \alpha A \frac { \partial U _ { p } } { \partial y _ { 1 } } + 2 \sum A _ { k } \frac { \partial V _ { p - 2 } } { \partial \omega _ { k } } = \gamma _ { p } + \Phi ,
$$

where $\Phi$ is a known function, periodic with respect to $y _ { 1 }$ and $\omega _ { k }$ , and developable in a trigonometric series. We choose $\gamma _ { p }$ so that the mean value of the right-hand member is zero.Then put

$$
\gamma _ { p } + \Phi = \Phi ^ { \prime } + \Phi ^ { \prime \prime } ,
$$

where $\Phi ^ { \prime }$ represents the terms depending on $y _ { 1 }$ ，and $\Phi ^ { \prime \prime }$ those independent of $y _ { 1 }$ such that

$$
\Phi ^ { \prime \prime } = [ [ \gamma _ { p } + \Phi ] ] .
$$

Then (95) is decomposed into

$$
2 \alpha { \cal A } \frac { \partial U _ { p } } { \partial y _ { 1 } } = \Phi ^ { \prime } , \qquad 2 \sum { \cal A } _ { k } \frac { \partial V _ { p - 2 } } { \partial \omega _ { k } } = \Phi ^ { \prime \prime } .
$$

These equations determine $V _ { p - 2 }$ and $U _ { p }$ ， which are periodic.

Thus the equations (89) have been integrated. We form

$$
- \sum n _ { k } ^ { ( 0 ) } \frac { \partial S _ { 3 } } { \partial y _ { k } } + 2 A \frac { \partial S _ { 2 } } { \partial y _ { 1 } } \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + \sum \frac { \partial F _ { 1 } } { \partial z _ { k } } \frac { \partial T _ { 1 } } { \partial u _ { k } } = \Phi ,
$$

and

$$
2 A \frac { \partial [ S _ { 2 } ] } { \partial y _ { 1 } } \frac { \partial S _ { 1 } } { \partial y _ { 1 } } + \sum \frac { \partial [ F _ { 1 } ] } { \partial z _ { k } } \frac { \partial T _ { 1 } } { \partial u _ { k } } = \Phi ,
$$

where

$$
\begin{array} { r } { [ S _ { 2 } ] = U _ { 0 } ^ { \prime } + \varepsilon U _ { 1 } ^ { \prime } + \varepsilon ^ { 2 } U _ { 2 } ^ { \prime } + \cdots , } \\ { T _ { 1 } = V _ { 0 } ^ { \prime } + \varepsilon V _ { 1 } ^ { \prime } + \varepsilon ^ { 2 } V _ { 2 } ^ { \prime } + \cdots . . . } \end{array}
$$

By equating the coefficients of $\varepsilon ^ { p }$ of (96) we obtain equations for determining $U _ { p } ^ { \prime }$ and $V _ { p - 2 } ^ { \prime }$ . There are of the same form as (95).

(I) The revolution case

Suppose that $a = U _ { \circ } = 0$ , then we can proceed in the same manner up to ${ \varepsilon } ^ { q }$ . But we have

$$
U _ { i } = 0 \qquad ( i = 1 , 2 , \ldots , q / 2 - 1 ) .
$$

If $q$ is even, then the equation for ${ \varepsilon } ^ { q }$ is

$$
A \left( { \frac { \partial U _ { q / 2 } } { \partial y _ { 1 } } } \right) ^ { 2 } + 2 \sum A _ { k } { \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } } + L _ { q }
$$

Put

$$
2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } = X ,
$$

then, by omiting the unnecessary suffixes we obtain

$$
\frac { \partial U _ { q / 2 } } { \partial y _ { 1 } } = \sqrt { \frac { \gamma - L - X - M \cos y _ { 1 } - N \sin y _ { 1 } } { A } } \equiv \sqrt { \overline { { Z } } } .
$$

The integral $\int { \sqrt { Z } } d y _ { 1 }$ is an elliptic functionof thesecond kind and one of the periods is $\int _ { 0 } ^ { 2 \pi } \sqrt { Z } d y _ { 1 }$ If $\boldsymbol { \gamma }$ and $X$ are chosen so that $Z$ is always positive,then this period is real. Let this period be equal to a given constant $h$ and put

$$
\int _ { 0 } ^ { 2 \pi } { \sqrt { Z } } d y _ { 1 } = h .
$$

Let the solution of this equation be

$$
X = \gamma + \psi ( \omega _ { k } ) ,
$$

where $\psi$ is a function of $\omega _ { k }$ which can be considered as given and periodic. Then we have

$$
2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } = \gamma + \psi ( \omega _ { k } ) .
$$

We can derive $V _ { q - 2 }$ from this equation and then $U _ { q / 2 }$ from (97).

# (II) The libration case

If $\gamma$ and $X$ are so chosen that $Z$ can vanish, then the second period of the elliptic function is real and equal to the constant $h$ . If we take an equation similar to (98),we obtain

$$
X = \gamma + \psi ^ { \prime } ( \omega _ { k } ) ,
$$

or

$$
2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } = \gamma + \psi ^ { \prime } ( \omega _ { k } ) .
$$

This equation determines $V _ { q - 2 }$ ，since $\psi ^ { \prime }$ is periodic and known.

(III) The limiting case

Suppose that one of the periods of the corresponding elliptic integral of the first kind is infinite.The function $V _ { q - 1 }$ is derived from

$$
2 \sum A _ { k } \frac { \partial V _ { q - 2 } } { \partial \omega _ { k } } = L \gamma _ { q } - L _ { q } + \sqrt { M _ { q } ^ { 2 } + N _ { q } ^ { 2 } } .
$$

An absolutely similar process can be applied. After $V _ { q - 2 }$ is known, $U _ { q }$ is derived by solving (97).

This study by Poincaré (1892) of the extension of Bohlin's theory is rather incomplete.

The theory of Bohlin and Poincaré was worked out by Garfinkel (1966,1970,1970a,1972) for the canonical differential equations with the Hamiltonian

$$
- F = \sum _ { j = 0 } ^ { \infty } A _ { j } ( x ) \cos \Theta _ { j } ( y ) ,
$$

$$
\Theta _ { j } ( y ) = j _ { 1 } y _ { 1 } + j _ { 2 } y _ { 2 } , \qquad x = ( x _ { 1 } , x _ { 2 } ) , \qquad y = ( y _ { 1 } , y _ { 2 } ) ,
$$

in the case of resonance.Garfinkel classified a resonance term into shallow and deep. A shallow resonance occurs when the commensurability with the small divisor $h \ll 1$ is such that

$$
j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } = O ( A _ { j } h ^ { - s } ) , \qquad s \geq 0 , \qquad j \neq 0 ,
$$

where

$$
n _ { 1 } = { \frac { \partial A _ { 0 } } { \partial x _ { 1 } } } , \qquad n _ { 2 } = { \frac { \partial A _ { 0 } } { \partial x _ { 2 } } }
$$

are the secular rates of $y _ { 1 }$ and $y _ { 2 }$ respectively, and

$$
A _ { j } = O ( h ^ { m ( j ) } ) , \qquad j \neq 0 , \qquad m ( j ) \geq 1 .
$$

A deep resonance is such that

$$
j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } \ll A _ { j } h ^ { - 1 } .
$$

Garfinkel called ideal resonance the case when the Hamiltonian contains one deep resonance term and the other periodic terms are ordinary such that

$$
A _ { 0 } = O ( 1 ) , \qquad A _ { j } / \dot { \Theta } _ { j , \mathrm { s e c } } = O ( h ^ { s } ) , \qquad \dot { \jmath } \neq 0 , \qquad s \equiv 1 ,
$$

where $\dot { \Theta } _ { j , \mathrm { s e c } }$ denotes the secular part of $\dot { \Theta } _ { j }$

$$
\dot { \Theta } _ { j , \mathrm { s e c } } = j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } + O ( h ) .
$$

Elimination of short- and long-period terms by means of von Zeipel's method generates terms with small divisor $\dot { \Theta } _ { j , \mathrm { s e c } }$ . Garfinkel constructed the resonance solution for the ideal resonance problem and obtained the resonance width， libration width and the frequency of the fundamental libration.He applied it to the critical inclination problem of an artificial satellite (see Hori in Section 9.23).

Garfinkel, Jupp and Williams (1971) took the equations with the Hamiltonian

$$
- F = B ( x ) + 2 \mu A ( x ) \sin ^ { 2 } y , ~ \mu \ll 1 ,
$$

and constructed a recursive algorithm for generating the solution valid for the entire phase space, including asymptotically the classical limit, and expanded the solution in powers of $\mu ^ { 1 / 2 }$ according to Bohlin and von Zeipel． They transformed the variables $x , y$ to $x ^ { \prime } , y ^ { \prime }$ with the principal function $S ( x ^ { \prime } , y )$ by

$$
x ^ { \prime } = \mathrm { c o n s t a n t } , \qquad y ^ { \prime } = - { \frac { \partial F ^ { \prime } } { \partial x ^ { \prime } } } t + y ^ { \prime } ( 0 ) ,
$$

where $\pmb { F ^ { \prime } }$ is the transformed Hamiltonian, or inversely by

$$
x = x ^ { \prime } + \sum _ { j = 1 } ^ { \infty } \frac { \partial S _ { j } } { \partial y } , \qquad y ^ { \prime } = y + \sum _ { j = 1 } ^ { \infty } \frac { \partial S _ { j } } { \partial x ^ { \prime } } ,
$$

where

$$
{ \cal S } = \sum _ { j = 0 } ^ { \infty } S _ { j } , \qquad S _ { 0 } = x ^ { \prime } y .
$$

The second equation is a generalized Kepler equation of the form

$$
y ^ { \prime } = y + \mu ^ { 1 / 2 } \phi ,
$$

$$
\phi = \sum _ { j } \phi _ { j } , \qquad \phi _ { j } = \exp \left\{ - \left( \frac { k } { k ^ { \prime } } \right) ^ { j + 1 } \right\} ,
$$

where $k , k ^ { \prime }$ are the moduli of elliptic functions with $k ^ { 2 } + k ^ { \prime 2 } = 1$ . The choice of $\phi _ { j }$ is made so that (i) the solution is nonsingular,(i) $F _ { j } ^ { \prime } \le { O } ( \mu ^ { j / 2 } )$ ，and (ii) the solution is continuous.

Put

$$
y = y ^ { \prime } + \delta , \qquad \alpha = { \frac { \partial S _ { j } } { \partial y } } ,
$$

then the transformed Hamiltonian is expanded in powers of $\pmb { \delta }$ ：

F $= [ B + B ^ { \prime } \ : \delta \ : + \ : { \textstyle { \frac { 1 } { 2 } } } B ^ { \prime \prime } \ : \delta ^ { 2 } \ : + \ : \cdots \ : + \ : 2 \mu ( A + A ^ { \prime } \ : \delta \ : + \ : \cdots ) \ : \sin ^ { 2 } y ] _ { x = x } ,$ ， where $\pmb { \alpha }$ is the resonance parameter such that $\alpha = - B ^ { \prime } / \omega _ { 0 } ,$ $\omega _ { 0 } =$ $| 4 A B ^ { \prime } | ^ { 1 / 2 } \mu ^ { 1 / 2 }$ and $k = \operatorname* { m i n } \left( | \alpha | , | \alpha | ^ { - 1 } \right)$ . It is convenient to restrict the modulus $k$ to the range $0 \leq k \leq 1$ . We divide the domain of motion into three regimes according as $| \alpha | > 1 , | \alpha | < 1 , | \alpha | = 1$ ,i.e., $k =$ $| \alpha | ^ { - 1 } , | \alpha | , 1$ ,so that sin $x = \mathtt { s n } u$ ， $k$ sn $\pmb { u }$ ,tanh $\pmb { u }$ and cos $x = \mathtt { c n } u$ dn $\pmb { u }$ ， sech $\pmb { u }$ ，corresponding to revolution, libration and limiting case, respectively. The demarcation $\alpha = \mu ^ { - 1 / 2 }$ between deep and shallow resonances is the point where the resonance and the classical solutions have the same accuracy. The solution is derived without singularity and is valid for the entire phase space. The appearance of singularities at sin $x = \pm \alpha$ in the libration regime and $k ^ { \prime } = 0$ in the limiting case is avoided by the choice of the new Hamiltonian $F ^ { \prime }$ ，where

$$
\begin{array} { l l } { \phi _ { j } = \exp \left\{ - \left( \displaystyle \frac { k } { k ^ { \prime } } \right) ^ { j + 1 } \right\} \qquad } & { \mathrm { i f ~ } \alpha ^ { 2 } \geq 1 , } \\ { \phi _ { j } = 0 \qquad } & { \mathrm { i f ~ } \alpha ^ { 2 } \leq 1 . } \end{array}
$$

On the other hand, Jupp (1969,1970,1972,1973) used action and angle variables according to Poincaré (1893) either by the method of von Zeipel or that of Lie transforms (Sections 9.29 and 10.44).The variables in the Hamiltonian (99) in the libration case are transformed by

$$
x = x _ { 0 } + ( \mu p ) ^ { 1 / 2 } \mathtt { c n } ( w , k ) , \qquad \sin y = \left( { \frac { p } { p _ { 0 } } } \right) ^ { 1 / 2 } \mathtt { s n } ( w , k ) ,
$$

$$
t = \mu ^ { - 1 / 2 } \tau , \qquad w = 2 s p _ { 0 } ^ { 1 / 2 } , \qquad k ^ { 2 } = \frac { p } { p _ { 0 } } , \qquad p _ { 0 } = \frac { 4 A _ { 0 } } { B _ { 0 } ^ { ( 2 ) } } ,
$$

$$
[ B ^ { ( 1 ) } ] _ { x = x _ { 0 } } = 0 ,
$$

$$
A ^ { ( n ) } = { \frac { \partial ^ { n } A } { \partial x ^ { n } } } , \qquad B ^ { ( n ) } = { \frac { \partial ^ { n } B } { \partial x ^ { n } } } \qquad ( n = 1 , 2 , \ldots ) ,
$$

where asubscript zero indicates its value for the resonance $x = x _ { 0 }$

The resonance phenomena occur if $B ^ { ( 1 ) } = 0$ for some value $x _ { 0 }$ of $x$ Then we have

$$
\frac { \partial p } { \partial \tau } = - \frac { \partial \Psi } { \partial s } , \frac { \partial s } { \partial \tau } = \frac { \partial \Psi } { \partial p } ,
$$

$$
\begin{array} { c } { { \displaystyle \begin{array} { c } { { \sigma { \boldsymbol { \varepsilon } } } } \\ { { { \boldsymbol { F } } ( { \boldsymbol { x } } , { \boldsymbol { y } } ) + { \boldsymbol { B } } _ { 0 } = \mu \mathbb { F } ( { \boldsymbol { p } } , { \boldsymbol { s } } ) , } } \\ { { } } \\ { { \mathbb { Y } ( { \boldsymbol { p } } , { \boldsymbol { s } } ) = \displaystyle \sum _ { n = 2 } ^ { \infty } \mu ^ { ( n - 2 ) / 2 } \biggl [ \frac { { \boldsymbol { B } } _ { 0 } ^ { ( n ) } } { n ! } \mathrm { c n } ^ { 2 } ~ } } \\ { { } } \\ { { + \displaystyle \frac { A _ { 0 } ^ { ( n - 2 ) } B _ { 0 } ^ { ( 2 ) } } { 2 A _ { 0 } \cdot ( n - 2 ) ! } \mathrm { s n } ^ { 2 } w \biggr ] p ^ { n / 2 } \mathrm { c n } ^ { n - 2 } w . } } \end{array} } } \end{array}
$$

The libration region corresponds to $p < p _ { \mathfrak { o } }$ ，where $p$ takes the value of zero at the libration center.

We choose a new coordinate $v$ and the canonically conjugate momentum $\pmb { u }$ such that

$$
w = 2 s p _ { 0 } ^ { 1 / 2 } = 4 K ( p ) \frac { v } { \pi } , \qquad u = \frac { 4 p _ { 0 } ^ { 1 / 2 } } { \pi } ( E - k ^ { \prime 2 } K ) \equiv u _ { 0 } \phi ( p ) ,
$$

or $p = p _ { 0 } \psi ( u )$ ， where $K , E$ are the complete elliptic integrals of the first and second kinds,respectively.Then we obtain

$$
\frac { d u } { d \tau } = - \frac { \partial \Theta } { \partial v } , \qquad \frac { d v } { d \tau } = \frac { \partial \Theta } { \partial u } , \qquad w = \frac { 4 K ( u ) v } { \pi } ,
$$

where

$$
\begin{array} { r l r } {  { - \Psi ( p , s ) = - \Theta ( u , v ) } } \\ & { } & { = \sum _ { n = 2 } ^ { \infty } \mu ^ { ( n - 2 ) / 2 } \biggl [ \frac { B _ { 0 } ^ { ( n ) } } { n ! } \mathrm { c n } ^ { 2 } w + \frac { A _ { 0 } ^ { ( n - 2 ) } B _ { 0 } ^ { ( 2 ) } } { 2 A _ { 0 } \cdot ( n - 2 ) ! } \mathrm { s n } ^ { 2 } w \biggr ] } \\ & { } & { \cdot [ p _ { 0 } \psi ( u ) ] ^ { n / 2 } \mathrm { c n } ^ { n - 2 } w . } \end{array}
$$

Thus

$$
x - x _ { 0 } = [ \mu p _ { 0 } \psi ( u ) ] ^ { 1 / 2 } \mathrm { c n } \bigg [ \frac { 4 K v } { \pi } , \psi ^ { 1 / 2 } ( u ) \bigg ] ,
$$

$$
\sin y = \psi ^ { 1 / 2 } ( u ) \ \mathrm { s n } \ \biggl [ \frac { 4 K v } { \pi } , \psi ^ { 1 / 2 } ( u ) \biggr ] ,
$$

$$
K ( u ) = \int _ { 0 } ^ { \pi / 2 } [ 1 - \psi ( u ) \sin ^ { 2 } \alpha ] ^ { - 1 / 2 } d \alpha .
$$

Once $x _ { 0 } , \psi ( u )$ and $v$ are known we can determine $x$ and $y$

Using the principal function

$$
S ( u ^ { * } , v ) = S _ { 1 / 2 } + S _ { 1 } + S _ { 3 / 2 } + S _ { 2 } + \cdot \cdot \cdot
$$

of the von Zeipel method we obtain

$$
\begin{array} { c } { { \mathrm { * = \mathrm { c o n s t a n t } , } \qquad v ^ { \ast } = \frac { \partial F ^ { \ast } } { \partial u ^ { \ast } } \tau + v _ { \mathrm { 0 } } ^ { \ast } , \qquad v _ { \mathrm { 0 } } ^ { \ast } = \mathrm { c o n s t a n t } , } } \\ { { \qquad F ^ { \ast } ( u ^ { \ast } ) = \Theta ( u , v ) , } } \\ { { u = u ^ { \ast } + \mu ^ { \ast \prime 2 } \frac { \partial S _ { 1 / 2 } } { \partial v } + \mu \frac { \partial S _ { 1 } } { \partial v } + \cdots , } } \\ { { \qquad v ^ { \ast } = v + \mu ^ { \prime \prime } \frac { \partial S _ { 1 / 2 } } { \partial u ^ { \ast } } + \mu \frac { \partial S _ { 1 } } { \partial u ^ { \ast } } + \cdots . } } \end{array}
$$

Equating terms in equal powers of $\mu ^ { \tau / 2 }$ from these equations we find the expression for $F _ { r / 2 } ^ { * }$ .For $r$ odd we get $F _ { r / 2 } ^ { * } = 0$ For $r$ even the function $\boldsymbol { F } _ { { r } / 2 } ^ { * }$ can be determined. The expressions for ${ \partial S _ { r / 2 } } / { \partial v }$ and ${ \partial S _ { \tau / 2 } } / { \partial u ^ { * } }$ for any positive integer $r$ are written in purely periodic form in terms of the quantities sn $w$ ,cn $w$ ,dn $w$ ， $Z ( w )$ and two fundamental integrals $I _ { z c } ( w , 2 q , 1 )$ and $[ I _ { z } ( w , 2 q ) - \overline { { I _ { z } ( w , 2 q ) } } ]$ ，where

$$
I _ { z c } ( w , 2 q , 1 ) = \int _ { 0 } ^ { w } Z ^ { 2 q } ( \alpha ) \ c \mathrm { n } \ \alpha \ d \alpha , \qquad I _ { z } ( w , 2 q ) = \int _ { 0 } ^ { w } Z ^ { 2 q } ( \alpha ) \ d \alpha ,
$$

$$
\overline { { I _ { z } ( w , 2 q ) } } = \frac { 1 } { 4 K } \int _ { 0 } ^ { 4 K } I _ { z } ( w , 2 q ) \ : d w ,
$$

for some positive integer $q$ .The coefficients of these quantities in the expression for $\boldsymbol { F } _ { { r } / 2 } ^ { * }$ possess neither singularity nor small divisor. The constant $u ^ { * }$ appears in the form $\psi ( u ^ { * } )$ through $k , k ^ { \prime } , K$ and $E$

Once $F _ { { r } / 2 } ^ { * } ( u ^ { * } )$ and $S _ { r / 2 } ( u ^ { * } , v )$ are known for $r = 1 , 2 , 3 , \ldots$ we may derive $\psi ( u )$ and $v$ ，and thence $x$ and $y$ ，in powers of the constants $\psi ( u ^ { * } ) , v _ { 0 } ^ { * } , x _ { 0 }$ and the time $\pmb { \tau }$ . The quantities $u ^ { * }$ and $v _ { 0 } ^ { * }$ are two integration constants.

Jupp (1972) employed the Lie transform method for the discussion of the same problem.The nth order Lie series method furnishes the momentum to the $( n + 1 )$ -th order in the small parameter $\mu ^ { 1 / 2 }$ .For studying the revolution case Jupp defined $( u , v )$ by

$$
x = x _ { 0 } \pm \mu ^ { 1 / 2 } p _ { 0 } k \mathrm { d n } ( w , k ^ { - 1 } ) ,
$$

$$
\sin y = \sin ( w , k ^ { - 1 } ) \qquad ( k > 1 ) ,
$$

$$
w = 4 K ( k ^ { - 1 } ) \frac { v } { \pi } ,
$$

$$
u = \frac { 4 p _ { 0 } } { \pi } \int K ( k ^ { - 1 } ) d k = \frac { 4 p _ { 0 } } { \pi } k E ( k ^ { - 1 } ) .
$$

The modulus of the elliptic functions is $k ^ { - 1 }$ . By means of the reciprocal modulus formula $K ( k ) \to k ^ { - 1 } K ( k ^ { - 1 } )$ ,the revolution case can be derived from the libration case by making the direct substitution

$$
( w , k ) \to \pm k ^ { - 1 } \operatorname { s n } ( w , k ^ { - 1 } ) , \qquad K ( k ) \to k ^ { - 1 } K ( k ^ { - 1 } ) ,
$$

$$
\begin{array} { r l } & { ( w , k ) \to \pm K ^ { - \cdot } \sin { ( w , k ^ { \cdot } ) } , \qquad \operatorname { \& } ( \kappa ) \to k ^ { \cdot } \operatorname { \& } ( \kappa ^ { \cdot } ) , } \\ & { ( w , k ) \to \pm \dim { ( w , k ^ { - 1 } ) } , \qquad \operatorname { \& } ( k ) \to k E ( k ^ { - 1 } ) + k ^ { - 1 } k ^ { \prime 2 } K ( k ^ { - 1 } ) , } \\ & { \operatorname { \ i } ( w , k ) \to \operatorname { c n } { ( w , k ^ { - 1 } ) } , \qquad \operatorname { \& } ( w , k ) \to k Z ( w , k ^ { - 1 } ) . } \end{array}
$$

Jupp (1973) further considered the Hamiltonian

$$
- F = B ( x ) + 2 \mu A ( x ) \sin ^ { 2 } y + \mu f ( x , y ) ,
$$

where the perturbation $f$ is assumed to be $O ( A )$ and periodic in $y$ with period $2 \pi$ ，and

$$
f ( x , y ) = \mu ^ { m } \sum _ { r = 1 } ^ { N } [ A _ { \tau } ( x ) \cos r y + B _ { r } ( x ) \sin r y ] ,
$$

where $N$ is a positive integer. He employed the Lie series method.

Alfriend and Richardson (1973) studied the stability of the origin of an autonomous Hamiltonian system when the system possesses a third- or fourth-order resonance,where there exists among the mean motions $n _ { i }$ a set of relatively prime integers $k _ { i }$ ,not all zero,such that

$$
\sum _ { i = 0 } ^ { n } k _ { i } n _ { i } = 0 , \qquad \sum _ { i = 0 } ^ { n } | k _ { i } | = m \qquad ( m = 3 , 4 ) .
$$

The condition for instability was given in terms of the coefficients of the higher-order terms in the Hamiltonian.

# WHITTAKER'S THEORY

# 14.14WHITTAKER'S TRANSFORMATION

Consider with Whittaker (1902,1928) a dynamical system

$$
\frac { d x _ { i } } { d t } = \frac { \partial H } { \partial y _ { i } } , \frac { d y _ { i } } { d t } = - \frac { \partial H } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

where $\pmb { H }$ is supposed not to contain $t$ explicitly. The algebraic solution of $2 n$ simultaneous equations

$$
\frac { \partial H } { \partial y _ { i } } = 0 , \qquad \frac { \partial H } { \partial x _ { i } } = 0 \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

contains one or more sets of values $a _ { 1 } , \ldots , a _ { n } , b _ { 1 } , \ldots , b _ { n }$ Each of these sets of values corresponds to either an equilibrium point or a steady motion. Take a set of values $a _ { 1 } , \ldots , a _ { n } , b _ { 1 } , \ldots , b _ { n }$ . We pro-

pose to obtain the expresson for the solution of this dynamical prob-lem when the motion is of the type which terminates at this equilibrium point or this steady motion.

Take a new set of variables

$$
x _ { i } = a _ { i } + q _ { i } , \qquad y _ { i } = b _ { i } + p _ { i } \qquad ( i = 1 , 2 , \ldots , n ) ;
$$

then the differential equations are of the form

$$
\frac { d q _ { i } } { d t } = \frac { \partial H } { \partial p _ { i } } , \frac { d p _ { i } } { d t } = - \frac { \partial H } { \partial q _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

where $\pmb { H }$ is expressed in terms of $q _ { i }$ and $p _ { i }$ . For a set of very small values of $q _ { i }$ and $p _ { i }$ the Hamiltonian $\pmb { H }$ can be expanded:

$$
H = H _ { 0 } + H _ { 1 } + H _ { 2 } + \cdots ,
$$

where $H _ { k }$ is an aggregate of terms homogeneous of degree $k$ in $q _ { i }$ and $p _ { i }$ . Since $H _ { 0 }$ does not contain any of these variables, it can be omitted. The equations with $H _ { 1 }$ are satisfied identically when $q _ { i }$ and $p _ { i }$ are all equated to zero. Hence $H _ { 1 }$ can be taken to be zero. Thus the expansion of $\pmb { H }$ begins with the second-degree terms:

$$
\begin{array} { l } { { \displaystyle { \cal H } = { \cal H } _ { 2 } + { \cal H } _ { 3 } + \cdots \cdot \cdot , } } \\ { { \displaystyle { \cal H } _ { 2 } = \frac { 1 } { 2 } \cdot \sum \mathrm { ~ } ( a _ { r r } q _ { r } ^ { 2 } + 2 a _ { r s } q _ { r } q _ { s } ) + 2 \cdot \sum b _ { r s } q _ { r } p _ { s } } } \\ { { \displaystyle ~ + \frac { 1 } { 2 } \cdot \sum \mathrm { ~ } ( c _ { r r } p _ { r } ^ { 2 } + 2 c _ { r s } p _ { r } p _ { s } ) , } } \\ { { \displaystyle a _ { r s } = a _ { s r } , ~ c _ { r s } = c _ { s r } , ~ b _ { r s } \neq b _ { s r } . } } \end{array}
$$

Put

$$
\begin{array} { r l r } & { } & { - \lambda \eta _ { \tau } = a _ { \tau 1 } \hat { \xi } _ { 1 } + a _ { \tau 2 } \hat { \xi } _ { 2 } + \cdot \cdot \cdot + a _ { \tau n } \hat { \xi } _ { n } + b _ { \tau 1 } \eta _ { 1 } + \cdot \cdot \cdot + b _ { r n } \eta _ { n } , } \\ & { } & { \lambda \hat { \xi } _ { \tau } = b _ { 1 \tau } \hat { \xi } _ { 1 } + b _ { 2 \tau } \hat { \xi } _ { 2 } + \cdot \cdot \cdot + b _ { n \tau } \hat { \xi } _ { n } + c _ { \tau 1 } \eta _ { 1 } + \cdot \cdot \cdot + c _ { \tau n } \eta _ { n } } \\ & { } & { ( r = 1 , 2 , \ldots , n ) , } \end{array}
$$

and

$$
\begin{array}{c} \begin{array} { r l } { b _ { 1 1 } \quad } & { a _ { 1 n } \qquad b _ { 1 n } + \lambda } \\ { \quad \cdots \qquad } & { \quad \cdots \qquad } \\ { a _ { 1 n } \qquad } & { a _ { n n } \qquad b _ { n 1 } \qquad } & { b _ { n n } + \lambda } \\ { b _ { 1 1 } \qquad } & { \quad \cdots \qquad } & { b _ { n 1 } \qquad c _ { 1 1 } \qquad } & { c _ { n 1 } } \\ { \quad \cdots \qquad } & { \quad \cdots \qquad } & { \quad \cdots } \\ { b _ { 1 n } \qquad } & { b _ { n n } - \lambda } & { c _ { 1 n } \qquad } & { c _ { n n } } \end{array} \qquad 0 .  \end{array}
$$

Denote the roots of this determinantal equation by $\lambda _ { 1 } , \ldots , \lambda _ { n } , - \lambda _ { 1 } ,$ $\ldots , - \lambda _ { n }$ . Let the set of $\xi _ { i }$ and $\eta _ { i }$ which corresponds to a root $\lambda _ { r }$ be $\xi _ { i } ^ { ( \tau ) }$ and $\eta _ { i } ^ { ( r ) }$ . Then

$$
\begin{array} { r l r } & { } & { - \lambda _ { r } \eta _ { p } ^ { ( r ) } = a _ { p 1 } \xi _ { 1 } ^ { ( r ) } + \cdot \cdot \cdot + a _ { p n } \xi _ { n } ^ { ( r ) } + b _ { p 1 } \eta _ { 1 } ^ { ( r ) } + \cdot \cdot \cdot + b _ { p n } \eta _ { n } ^ { ( r ) } , } \\ & { } & { \lambda _ { r } \xi _ { p } ^ { ( r ) } = b _ { 1 p } \xi _ { 1 } ^ { ( r ) } + \cdot \cdot \cdot + b _ { n p } \xi _ { n } ^ { ( r ) } + c _ { p 1 } \eta _ { 1 } ^ { ( r ) } + \cdot \cdot \cdot + c _ { p n } \eta _ { n } ^ { ( r ) } . } \end{array}
$$

Multiply these equations by $\xi _ { p } ^ { ( s ) }$ and $\eta _ { \mathcal { P } } ^ { ( s ) }$ ， respectively, and add; then

$$
\lambda _ { r } \cdot \sum _ { i = 1 } ^ { n } \ ( \xi _ { i } ^ { ( r ) } \eta _ { i } ^ { ( s ) } - \xi _ { i } ^ { ( s ) } \eta _ { i } ^ { ( r ) } ) = H ( r , s ) ,
$$

$$
\begin{array} { r l } & { H ( r , s ) = a _ { 1 1 } \xi _ { 1 } ^ { ( r ) } \xi _ { 1 } ^ { ( s ) } + a _ { 1 2 } ( \xi _ { 1 } ^ { ( r ) } \xi _ { 2 } ^ { ( s ) } + \xi _ { 1 } ^ { ( s ) } \xi _ { 2 } ^ { ( r ) } ) + \cdots } \\ & { \qquad + b _ { 1 1 } ( \xi _ { 1 } ^ { ( r ) } \gamma _ { 1 } ^ { ( s ) } + \xi _ { 1 } ^ { ( s ) } \gamma _ { 1 } ^ { ( r ) } ) + \cdots + c _ { 1 1 } \eta _ { 1 } ^ { ( r ) } \eta _ { 1 } ^ { ( s ) } + \cdots . } \end{array}
$$

We have

$$
( \lambda _ { \tau } + \lambda _ { s } ) \cdot \sum _ { i } \ ( \xi _ { i } ^ { ( r ) } \eta _ { i } ^ { ( s ) } - \xi _ { i } ^ { ( s ) } \eta _ { i } ^ { ( r ) } ) = 0 .
$$

If $\lambda _ { r } + \lambda _ { s } \neq 0$ ，then

$$
\sum _ { i } \ ( \xi _ { i } ^ { ( r ) } \eta _ { i } ^ { ( s ) } - \xi _ { i } ^ { ( s ) } \eta _ { i } ^ { ( r ) } ) = 0 .
$$

Hence we should have

$$
\begin{array} { r } { H ( r , s ) = 0 . } \end{array}
$$

f $\lambda _ { \tau } + \lambda _ { s } = 0$ ，then $\xi _ { i } ^ { ( s ) } = \xi _ { i } ^ { ( - r ) }$ ， $\eta _ { i } ^ { ( s ) } = \eta _ { i } ^ { ( - r ) }$ ，and

$$
\lambda _ { \tau } \cdot \sum _ { i } \mathrm { ~ } ( \xi _ { i } ^ { ( r ) } \eta _ { i } ^ { ( - r ) } - \xi _ { i } ^ { ( - r ) } \eta _ { i } ^ { ( r ) } ) = H ( r , - r ) .
$$

Thus, by the substitution

$$
\begin{array} { r l } & { q _ { r } = \xi _ { r } ^ { ( 1 ) } q _ { 1 } ^ { \prime } + \xi _ { r } ^ { ( 2 ) } q _ { 2 } ^ { \prime } + \cdot \cdot \cdot + \xi _ { r } ^ { ( n ) } q _ { n } ^ { \prime } + \xi _ { r } ^ { ( - 1 ) } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + \xi _ { 1 } ^ { ( - n ) } p _ { n } ^ { \prime } , } \\ & { p _ { r } = \eta _ { r } ^ { ( 1 ) } q _ { 1 } ^ { \prime } + \eta _ { r } ^ { ( 2 ) } q _ { 2 } ^ { \prime } + \cdot \cdot \cdot + \eta _ { r } ^ { ( n ) } q _ { n } ^ { \prime } + \eta _ { r } ^ { ( - 1 ) } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + \eta _ { r } ^ { ( - n ) } p _ { n } ^ { \prime } , } \end{array}
$$

the coefficient of $\sum _ { i } { ( \delta q _ { i } \Delta p _ { i } - \Delta q _ { i } \delta p _ { i } } )$ in the expansion for $\delta q _ { r } ^ { \prime } \Delta p _ { s } ^ { \prime }$ becomes

$$
\sum _ { i } \big ( \xi ^ { ( r ) } \eta ^ { ( s ) } - \xi ^ { ( s ) } \eta ^ { ( r ) } \big ) .
$$

But this last expression vanishes for $\lambda _ { r } + \lambda _ { s } \neq 0$ .Hence we obtain

$$
\sum \left( \delta q _ { r } \Delta p _ { r } - \Delta q _ { r } \delta p _ { r } \right) = \sum \left( \delta q _ { r } ^ { \prime } \Delta p _ { r } ^ { \prime } - \Delta q _ { r } ^ { \prime } \delta p _ { r } ^ { \prime } \right)
$$

with

$$
\sum \left( \xi ^ { ( r ) } \eta ^ { ( - r ) } - \xi ^ { ( - r ) } \eta ^ { ( r ) } \right) = 1 .
$$

This shows that the transformation from $q _ { i } , ~ p _ { i }$ to $q _ { i } ^ { \prime } , \ p _ { i } ^ { \prime }$ is canonical (Section 4.2). Thus

$$
\frac { d q _ { r } ^ { \prime } } { d t } = \frac { \partial H } { \partial p _ { r } ^ { \prime } } , \frac { d p _ { r } ^ { \prime } } { d t } = - \frac { \partial H } { \partial q _ { r } ^ { \prime } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

where

$$
H _ { 2 } = \sum _ { r = 1 } ^ { n } H ( r , - r ) q _ { r } ^ { \prime } p _ { r } ^ { \prime } = \sum \lambda _ { r } q _ { r } ^ { \prime } p _ { r } ^ { \prime } ,
$$

and where $H _ { \kappa }$ is homogeneous of degree $k$ with respect to $q _ { i } ^ { \prime } , p _ { i } ^ { \prime }$

We make a further contact transformation

$$
q _ { r } = \frac { \partial W } { \partial p _ { \tau } } , \qquad p _ { r } ^ { \prime } = \frac { \partial W } { \partial q _ { r } ^ { \prime } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
W = \sum _ { r = 1 } ^ { n } p _ { r } q _ { r } ^ { \prime } - \frac { 1 } { 2 } \cdot \sum _ { r = 1 } ^ { n } \frac { p _ { r } ^ { 2 } } { \lambda _ { r } } - \frac { 1 } { 4 } \cdot \sum _ { r = 1 } ^ { n } \lambda _ { r } q _ { r } ^ { \prime 2 } .
$$

The transformed equations are also canonical and

$$
H _ { 2 } = \frac { 1 } { 2 } \cdot \sum _ { \tau = 1 } ^ { n } ~ ( p _ { \tau } ^ { 2 } + \lambda _ { \tau } ^ { 2 } q _ { \tau } ^ { 2 } ) ,
$$

where the $\lambda _ { \tau }$ are supposed to be real.

With a further transformation

$$
p _ { r } ^ { \prime } = \frac { \partial W } { \partial q _ { r } ^ { \prime } } , \qquad q _ { r } = \frac { \partial W } { \partial p _ { r } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
W = \sum _ { r = 1 } ^ { n } \Big [ q _ { r } ^ { \prime } \sin ^ { - 1 } \Big ( \frac { p _ { r } } { \sqrt { 2 \lambda _ { r } q _ { r } ^ { \prime } } } \Big ) + \frac { p _ { r } } { 2 \lambda _ { r } } \sqrt { 2 \lambda _ { r } q _ { r } ^ { \prime } - p _ { r } ^ { 2 } } \Big ] ,
$$

or

$$
p _ { r } = \sqrt { 2 \lambda _ { r } q _ { r } ^ { \prime } } \cdot \sin p _ { r } ^ { \prime } , \qquad q _ { r } = \sqrt { \frac { 2 q _ { r } ^ { \prime } } { \lambda _ { r } } } \cdot \cos p _ { r } ^ { \prime } ,
$$

the Hamiltonian equations change to

$$
\frac { d q _ { r } ^ { \prime } } { d t } = \frac { \partial H } { \partial p _ { r } ^ { \prime } } , \frac { d p _ { r } ^ { \prime } } { d t } = - \frac { \partial H } { \partial q _ { r } ^ { \prime } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
H = \lambda _ { 1 } q _ { 1 } ^ { \prime } + \lambda _ { 2 } q _ { 2 } ^ { \prime } + \cdot \cdot \cdot + \lambda _ { n } q _ { n } ^ { \prime } + H _ { 3 } + H _ { 4 } + \cdot \cdot \cdot ,
$$

where $H _ { \kappa }$ is homogeneous of degree $k / 2$ with respect to $q _ { r } ^ { \prime }$ and homogeneous of degree $k$ with respect to cos $p _ { r } ^ { \prime }$ and sin $p _ { r } ^ { \prime }$ . Such a power or product of cos $p _ { r } ^ { \prime }$ and sin $p _ { r } ^ { \prime }$ is expressed by sines or cosines of the angle $n _ { 1 } p _ { 1 } ^ { \prime } + n _ { 2 } p _ { 2 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime }$ ，and the Hamiltonian $H _ { r }$ can be written in the form

$$
q _ { 1 } ^ { \prime m _ { 1 } } q _ { 2 } ^ { \prime m _ { 2 } } \cdot \cdot \cdot q _ { n } ^ { \prime m _ { n } } \cos { ( n _ { 1 } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime } ) } ,
$$

$$
m _ { 1 } + m _ { 2 } + \cdots + m _ { n } = \frac { r } { 2 } , \qquad | n _ { 1 } | + | n _ { 2 } | + \cdots + | n _ { n } | \le r .
$$

Hence

$$
H = \sum _ { \mathrm { \scriptsize ~ { \it ~ 1 } } } A _ { n _ { 1 } n _ { 2 } \cdots n _ { n } } ^ { m _ { 1 } m _ { 2 } \cdots m _ { n } } q _ { 1 } ^ { \prime } { \overline { { { m } } } } _ { 1 } q _ { 2 } ^ { \prime } { \overline { { { m } } } } _ { 2 } . . . q _ { n } ^ { \prime } { \overline { { { \mathrm { \scriptsize ~ { c } } } } } } _ { n } \stackrel { \mathrm { \scriptsize { ~ s i n } } } { \cos { \mathrm { \scriptsize ~ { \it ~ 1 } } } } ( n _ { 1 } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime } ) ,
$$

$$
| m _ { 1 } | + \cdots + | m _ { n } | \leq 2 ( m _ { 1 } + m _ { 2 } + \cdots + m _ { n } ) .
$$

The series is absolutely convergent for all values of $p _ { 1 } ^ { \prime } , \ldots , p _ { n } ^ { \prime }$ ，provided that $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ are bounded by a superior limit. The series can be rewritten

$$
\begin{array} { c } { { H = a _ { 0 0 \cdots 0 } + \displaystyle \sum _ { \begin{array} { l } { { } } \\ { { } } \end{array} } a _ { n _ { 1 } n _ { 2 } \cdots n _ { n } } \cos { } ( n _ { 1 } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime } ) } } \\ { { + \displaystyle \sum _ { \begin{array} { l } { { } } \end{array} } b _ { n _ { 1 } n _ { 2 } \cdots n _ { n } } \sin { } ( n _ { 1 } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime } ) , } } \end{array}
$$

where the coefficients $^ { a }$ and $^ { b }$ are functions of $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ ，and the expansions of $a _ { n _ { 1 } n _ { 2 } \dots n _ { n } } , b _ { n _ { 1 } n _ { 2 } \dots n _ { n } }$ in powers of $a _ { 1 } ^ { \prime } , \ldots , a _ { n } ^ { \prime }$ do not contain terms of order lower than ${ \scriptstyle { \frac { 1 } { 2 } } } \{ | n _ { 1 } | + \cdots + | n _ { n } | \}$ ，and the summation is extended over all positive and negative integers $n _ { 1 } , \ldots , n _ { n _ { n } }$ ,including zero,except $n _ { 1 } = n _ { 2 } = \cdot \cdot \cdot = n _ { \pi } = 0$ ，and finally the expansion of $a _ { 0 0 } . . . _ { 0 }$ begins with terms with $\lambda _ { 1 } q _ { 1 } ^ { \prime } + \dots + \lambda _ { n } q _ { n } ^ { \prime }$ . These are the most important terms in the expansion of $\pmb { H }$ if $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ are small. For convenience we omit the terms

$$
\sum b _ { n _ { 1 } \cdots n _ { n } } \sin ( n _ { 1 } p _ { 1 } ^ { \prime } + \cdots + n _ { n } p _ { n } ^ { \prime } ) .
$$

Thus the equations of motion are transformed to

$$
\frac { d q _ { r } } { d t } = \frac { \partial H } { \partial p _ { r } } , \frac { d p _ { r } } { d t } = - \frac { \partial H } { \partial q _ { r } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
H = a _ { 0 0 } . . . { \mathrm { 0 + \sum } } \mathrm { ~ } a _ { n _ { 1 } n _ { 2 } \cdots n _ { n } } \cos { ( n _ { 1 } p _ { 1 } + \cdots + n _ { n } p _ { n } ) } ,
$$

where the coefficients $^ { a }$ are functions of $q _ { 1 } , \ldots , q _ { n }$ only. Moreover it is supposed that the periodic part of $\pmb { H }$ is small compared with the nonperiodic part $a _ { 0 0 } . . . _ { 0 }$ . The term with argument $n _ { 1 } p _ { 1 } + \cdots + n _ { n } p _ { n }$ has its coefficient $a _ { n _ { 1 } n _ { 2 } \dots n _ { n _ { n } } }$ at least of order ${ \scriptstyle { \frac { 1 } { 2 } } } \{ | n _ { 1 } | + \cdots + | n _ { n } | \}$ in the small quantities $q _ { 1 } , \ldots , q _ { n }$ . The expansion of $a _ { 0 0 \cdots 0 }$ begins with a term $\lambda _ { 1 } q _ { 1 } + \cdots + \lambda _ { n } q _ { n }$

Now we carry out the final transformation analogous to Delaunay's which gets rid of one periodic term,in order to make it evident that the nonperiodic part of $\pmb { H }$ is far more important.Choose a periodic term $a _ { n _ { 1 } \cdots n _ { \pi } }$ cos $( n _ { 1 } p _ { 1 } + \cdots + n _ { n } p _ { n } )$ and let

$$
H = a _ { 0 0 } . . . { } _ { 0 } ( q _ { 1 } , . . . , q _ { n } )
$$

$$
+ \ a _ { n _ { 1 } \cdots n _ { n } } ( q _ { 1 } , \ldots , q _ { n } ) \cos { ( n _ { 1 } p _ { 1 } + \cdots + n _ { n } p _ { n } ) } + R ,
$$

where $\pmb R$ represents all the remaining periodic terms of $\pmb { H }$ By the transformation

$$
p _ { r } ^ { \prime } = \frac { \partial W } { \partial q _ { r } ^ { \prime } } , \qquad q _ { r } = \frac { \partial W } { \partial p _ { r } } \quad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
W = q _ { 1 } ^ { \prime } p _ { 1 } + \cdot \cdot \cdot + q _ { n } ^ { \prime } p _ { n } + f ( q _ { 1 } ^ { \prime } , \cdot \cdot \cdot , q _ { n } ^ { \prime } , \theta ) ,
$$

$$
\theta = n _ { 1 } p _ { 1 } + \cdot \cdot \cdot + n _ { n } p _ { n } ,
$$

where $f$ is left indeterminate for the moment, the Hamiltonian equa-tions become

$$
\frac { d q _ { r } ^ { \prime } } { d t } = \frac { \partial H } { \partial p _ { r } ^ { \prime } } , \frac { d p _ { r } ^ { \prime } } { d t } = - \frac { \partial H } { \partial q _ { r } ^ { \prime } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
{ \begin{array} { r l } & { H = a _ { \scriptscriptstyle 0 0 \cdots \cdot 0 } \Bigl ( q _ { 1 } ^ { \prime } + n _ { \scriptscriptstyle 1 } { \frac { \partial f } { \partial \theta } } , \cdot \cdot \cdot , q _ { n } ^ { \prime } + n _ { \scriptscriptstyle n } { \frac { \partial f } { \partial \theta } } \Bigr ) } \\ & { \qquad + a _ { \scriptscriptstyle n \cdot \cdots n _ { n } } \Bigl ( q _ { 1 } ^ { \prime } + n _ { \scriptscriptstyle 1 } { \frac { \partial f } { \partial \theta } } , \cdot \cdot \cdot , q _ { n } ^ { \prime } + n _ { \scriptscriptstyle n } { \frac { \partial f } { \partial \theta } } \Bigr ) \cos \theta + R , } \end{array} }
$$

where $\theta$ and $\pmb R$ are expressed in terms of the new variables by

$$
p _ { r } ^ { \prime } = p _ { r } + \frac { \partial f } { \partial q _ { r } } , \qquad q _ { r } = q _ { r } ^ { \prime } + n _ { r } \frac { \partial f } { \partial \theta } .
$$

The quantity $\pmb \theta$ is determined so that it disappears identically from the expression:

$$
\begin{array} { r l } & { a _ { 0 0 \cdots 0 } \Big ( q _ { 1 } ^ { \prime } + n _ { 1 } \frac { \partial f } { \partial \theta } , \cdots \cdot \cdot , q _ { n } ^ { \prime } + n _ { n } \frac { \partial f } { \partial \theta } \Big ) } \\ & { \qquad + a _ { n _ { 1 } \cdots n _ { n } } \Big ( q _ { 1 } ^ { \prime } + n _ { 1 } \frac { \partial f } { \partial \theta } , \cdots , q _ { n } ^ { \prime } + n _ { n } \frac { \partial f } { \partial \theta } \Big ) \cos \theta , } \end{array}
$$

i.e., so that this expression is a function of $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ only.Denote this expression so defined by $a _ { 0 0 } ^ { \prime } . . . 0$ . The equation

$$
\begin{array} { r l } & { a _ { 0 0 \cdots 0 } \Big ( q _ { 1 } ^ { \prime } + n _ { 1 } \frac { \partial f } { \partial \theta } , \cdots , q _ { n } ^ { \prime } + n _ { n } \frac { \partial f } { \partial \theta } \Big ) } \\ & { \qquad + a _ { n 1 \cdots n _ { n } } \Big ( q _ { 1 } ^ { \prime } + n _ { 1 } \frac { \partial f } { \partial \theta } , \cdots , q _ { n } ^ { \prime } + n _ { n } \frac { \partial f } { \partial \theta } \Big ) \cos \theta = a _ { 0 0 \cdots 0 } ^ { \prime } } \end{array}
$$

expresses $\partial f / \partial \theta$ in terms of $q _ { 1 } ^ { \prime } , . . . , q _ { n } ^ { \prime } , a _ { 0 0 } ^ { \prime } . . . 0$ and cos $\theta$ Suppose that the solution of this equation for $\partial \mathbf { \hat { \boldsymbol { f } } } / \partial \mathbf { \boldsymbol { \theta } }$ is represented by a trigonometric series proceeding in multiples of $\theta$ in the form

$$
\frac { \partial f } { \partial \theta } = c _ { 0 } + \sum _ { k = 1 } ^ { \infty } c _ { k } \cos k \theta ,
$$

where $c _ { 0 } , c _ { 1 } , \ldots$ ， are known functions of $q _ { 1 } ^ { \prime } , . . . , q _ { n } ^ { \prime } , a _ { 0 0 } ^ { \prime } . . . 0$ .Only the last quantity $a _ { 0 0 } ^ { \prime } . . . 0$ is yet unknown.We determine it by the condition $c _ { 0 } = 0$ ,i.e.,by

$$
{ \frac { \partial f } { \partial \theta } } = \sum _ { k = 1 } ^ { \infty } c _ { k } \cos k \theta .
$$

Integrating this with the value of the integration constant zero, we obtain

$$
f = \sum _ { k = 1 } ^ { \infty } { \frac { c _ { k } } { k } } \sin k \theta .
$$

Thus the transformation in question is

$$
p _ { r } ^ { \prime } = p _ { r } + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k } \frac { \partial c _ { k } } { \partial q _ { r } ^ { \prime } } \sin k \theta ,
$$

$$
q _ { r } = q _ { r } ^ { \prime } + n _ { r } \cdot \sum _ { k = 1 } ^ { \infty } c _ { k } \cos k \theta \qquad ( r = 1 , 2 . . . , n ) .
$$

We have

$$
n _ { 1 } p _ { 1 } ^ { \prime } + \cdot \cdot \cdot + n _ { n } p _ { n } ^ { \prime } = \theta ^ { \prime } ,
$$

$$
\theta ^ { \prime } = \theta + \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k } } \left( n _ { 1 } { \frac { \partial c _ { k } } { \partial q _ { 1 } ^ { \prime } } } + \cdots + n _ { n } { \frac { \partial c _ { k } } { \partial q _ { n } ^ { \prime } } } \right) \sin k \theta .
$$

Inverting this series we find (Section 2.3)

$$
\theta = \theta ^ { \prime } + \sum _ { k = 1 } ^ { \infty } d _ { k } \sin k \theta ^ { \prime } ,
$$

where $d _ { 1 } , d _ { 2 } , \ldots$ . are known functions of $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ . We obtain finally

$$
\begin{array} { l } { { p _ { \tau } = p _ { r } ^ { \prime } + \displaystyle \sum _ { k = 1 } ^ { \infty } r e _ { k } \sin k \theta ^ { \prime } , } } \\ { { q _ { r } = q _ { r } ^ { \prime } + n _ { r } \cdot \displaystyle \sum _ { k = 1 } ^ { \infty } g _ { k } \cos k \theta ^ { \prime } , \qquad ( r = 1 , 2 , . . . , n ) , } } \end{array}
$$

where $\boldsymbol { e } _ { k }$ and $g _ { \kappa }$ are known functions of $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ . After this transformation is made,the original equation

$$
R = \sum a _ { m _ { 1 } \cdots m _ { n } } \cos { ( m _ { 1 } p _ { 1 } + \cdots + m _ { n } p _ { n } ) }
$$

is changed to

$$
R = \sum a _ { m _ { 1 } \cdots m _ { n } } ^ { \prime } \cos { ( m _ { 1 } p _ { 1 } ^ { \prime } + \cdots + m _ { n } p _ { n } ^ { \prime } ) } ,
$$

where $a _ { m _ { 1 } \ldots m _ { n _ { n } } } ^ { \prime }$ are known functions of $q _ { 1 } ^ { \prime } , \ldots , q _ { n } ^ { \prime }$ 、Hence, after the transformation has been effected,the dynamical system is still expressed by a system of equations

$$
\frac { d q _ { r } } { d t } = \frac { \partial H } { \partial p _ { r } } , \frac { d p _ { r } } { d t } = - \frac { \partial H } { \partial q _ { r } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

$$
H = a _ { 0 0 \cdots 0 } + \sum a _ { m _ { 1 } \cdots m _ { n } } \cos { ( m _ { 1 } p _ { 1 } + \cdots + m _ { n } p _ { n } ) } ,
$$

where the coefficients $a _ { m _ { 1 } \ldots m _ { n } }$ are known functions of $q _ { 1 } , \ldots , q _ { n }$ .Thus the equations are of a similar form to the previous equations,but the term

$$
a _ { m _ { 1 } \cdots m _ { n } } \cos { ( m _ { 1 } p _ { 1 } + \cdots + m _ { n } p _ { n } ) }
$$

is transferred from the periodic part of $\pmb { H }$ to its nonperiodic part, and the nonperiodic part becomes more important than in the equations before the transformation is made (compare with Section 9.1).

By successive applications of this transformation the periodic part of $\pmb { H }$ becomes less and less important,as compared with the nonperiodic part，and finally it becomes insignificant and negligible. Denote the final variables at this stage by $\alpha _ { 1 } , \ldots , \alpha _ { n }$ ， $\beta _ { 1 } , \ldots , \beta _ { n }$ . Then the final equations are

$$
\frac { d \alpha _ { r } } { d t } = \frac { \partial H } { \partial \beta _ { r } } , \frac { d \beta _ { r } } { d t } = - \frac { \partial H } { \partial \alpha _ { r } } \qquad ( r = 1 , 2 , \ldots , n ) ,
$$

and we have

$$
\frac { d \alpha _ { \tau } } { d t } = 0 , \qquad \beta _ { r } = - \int \frac { \partial H } { \partial \alpha _ { \tau } } d t .
$$

Thus $\alpha _ { r } =$ constant,

$$
\beta _ { r } = \mu _ { r } t + \varepsilon _ { r } , \mu _ { r } = - \frac { \partial H } { \partial \alpha _ { r } } ( r = 1 , 2 , \cdot \cdot \cdot , n ) ,
$$

where the $\varepsilon _ { r }$ are arbitrary constants,and the parts of $\mu _ { r }$ independent of $\alpha _ { 1 } , \ldots , \alpha _ { n }$ are denoted by $- \lambda _ { r }$

By the inverse transformation we obtain

$$
q _ { r } = f _ { r } ( \alpha _ { 1 } , \ldots , \alpha _ { n } ) + \sum { a _ { m _ { 1 } \cdots m _ { n } } } \cos { ( m _ { 1 } \beta _ { 1 } + \cdots + m _ { n } \beta _ { n } ) } ,
$$

$$
\begin{array} { c }  { p _ { \tau } = \beta _ { r } + \displaystyle \sum _ { \begin{array} { c } { { b _ { m _ { 1 } } \ldots m _ { n } } } \end{array} } { \overline { { { \sin { ( m _ { 1 } \beta _ { 1 } + \cdot \cdot \cdot + m _ { n } \beta _ { n } ) } } } } } } \\ { { ( r = 1 , 2 , \ldots , n ) . } } \end{array}
$$

Thus the original variables are expressed by trigonometric series proceeding with the sums of multiples of $_ n$ angular variables,where the angular variables are all linear functions of $t$ ，and

$$
\mu _ { \tau } = \lambda _ { \tau } + \sum _ { k _ { 1 } , k _ { 2 } , \cdots , k _ { n } } \alpha _ { 1 } ^ { k _ { 1 } } \alpha _ { 2 } ^ { k _ { 2 } } \cdot \cdot \cdot \alpha _ { n } ^ { k _ { n } } ,
$$

and the coefficients of the trigonometric terms are functions of arbitrary constants $\alpha _ { 1 } , \ldots , \alpha _ { n }$ . This gives one of the families of solutions of the dynamical system,whose limiting member is the equilibrium position or the steady motion from which we have started.

# 14.15ADELPHIC INTEGRAL

Consider the periodic solutions of a dynamical system with two degrees of freedom, in particular the force-free motion on the surface of an ellipsoid.A closed curve on the surface corresponds to a periodic solution of the problem.A geodesic,which is a closed curve,is a periodic solution.For such a closed geodesic the so-called Joachimstal relation $p d =$ constant holds,where $p$ is the perpendicular distance from the center of the ellipsoid to the tangent plane at that point and $d$ is the diameter of the ellipsoid parallel to the tangent to the geodesic passing through that point (Salmon, 1912).The same relation holds for a line of curvature of the ellipsoid. Thus a geodesic belongs to or is associated with the line of curvature with the same value of pd. There is only one line of curvature with a fixed value of $p d$ ,but there are an infinite number of geodesics belonging to one line of curvature.A line of curvature consists of two closed curves on an ellipsoid, that is, the two intersection lines of the ellipsoid with the two types of confocal quadrics. In order that a geodesic be closed, the value of the parameter, in this case the value of pd, should be rational. Otherwise it is non-closed.If it is closed, then there exist an infinite number of closed geodesics belonging to the same line of curvature.If it is not closed, then the geodesics belonging to the line of curvature are not closed. This is evident upon consideration of an ellipsoid of revolution． The two portions of the line of curvature are parallel circles on the surface. The infinite number of geodesics belonging to this line of curvature are obtained by rotating around the axis of symmetry (Salmon,1912).

If

$$
\phi ( q _ { 1 } , q _ { 2 } , p _ { 1 } , p _ { 2 } ) = \mathrm { c o n s t a n t }
$$

is an integral of a dynamical system, then the infinitesimal contact transformation (Section 1.8) defined by

$$
\begin{array} { r } { \dot { \ i } q _ { 1 } = \varepsilon \frac { \partial \phi } { \partial p _ { 1 } } , \qquad \delta q _ { 2 } = \varepsilon \frac { \partial \phi } { \partial p _ { 2 } } , \qquad \delta p _ { 1 } = - \varepsilon \frac { \partial \phi } { \partial q _ { 1 } } , \qquad \delta p _ { 2 } = - \varepsilon \frac { \partial \phi } { \partial q _ { 2 } } , } \end{array}
$$

transforms a trajectory to an adjacent curve which is again a trajectory.An infinitesimal transformation corresponding to $p d =$ constant transforms a geodesic to another geodesic belonging to the same line of curvature.Thus $\infty ^ { 2 }$ geodesics on the surface of an ellipsoid are classified into families consisting of $\infty ^ { 1 }$ geodesics.Members of one family of $\infty ^ { 1 }$ geodesics are either all closed or all non-closed.

Besides these there are three closed geodesics,that is, the three principal sections of the ellipsoid. They are of particular character, being isolated,and do not belong to any family. The above transformation transforms each principal section into itself, that is, these particular geodesics are invariant under the transformation. These are the singular solutions of an ordinary differential equation of the first order. If a differential equation of the first order admits a particular infinitesimal transformation, then this infinitesimal transformation changes the ordinary integral curves one into another but leaves invariant the singular integral curves.

These periodic curves are periodic solutions.If a periodic solution belongs to a continuous family of $\infty ^ { 1 }$ periodic solutions with the same value of the energy constant,and is transformed to another one of the family under the infinitesimal transformation belonging to an integral, then the periodic solution is called ordinary.If there is no ad-jacent periodic solution corresponding to the same value of the energy constant, then the periodic solution is called singular. An ordinary periodic solution is a member of a continuous family of $\infty ^ { 2 }$ periodic solutions,and a singular periodic solution is a member of a family of $\infty ^ { 1 }$ periodic solutions.The problem of geodesics is different from that of periodic solutions,because the energy constant is immaterial for geodesics.

An asymptotic solution is associated with a singular periodic solution，but not with an ordinary periodic solution. An asymptotic geodesic of a quadric surface winds round and round on the surface of a hyperboloid of one sheet and finally becomes asymptotic to the principal elliptic section of the hyperboloid．This principal elliptic section is a singular periodic solution.

Suppose that the solution of a general dynamical system with two degrees of freedom is expressed as the sum of terms of the form

$$
a _ { m n } \cos { ( m \beta _ { 1 } + n \beta _ { 2 } ) } ,
$$

where m and $_ n$ are positive or negative integers including zero, and $a _ { m n }$ depends on two integration constants $\alpha _ { 1 }$ and $\alpha _ { 2 }$ ， and where $\beta _ { 1 } =$ $\mu _ { 1 } t + \varepsilon _ { 1 } , \beta _ { 2 } = \mu _ { 2 } t + \varepsilon _ { 2 } .$ with $\mu _ { 1 }$ and $\mu _ { 2 }$ depending only on $\alpha _ { 1 }$ and $\alpha _ { 2 }$ ， and with integration constants $\varepsilon _ { 1 }$ and $\varepsilon _ { 2 }$ .If $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are such that $\mu _ { 1 }$ and $\pmb { \mu } _ { 2 }$ are commensurable,then there exist periodic solutions with period $2 \pi / \nu$ ，where $\nu$ is the least integral multiple of $\pmb { \mu } _ { 1 }$ and $\pmb { \mu _ { 2 } }$ By varying $\varepsilon _ { 1 }$ continuously we get a family of periodic solutions with the same period. These are ordinary periodic solutions. Since a transformation of $\varepsilon _ { 2 }$ is composed of a transformation of $\varepsilon _ { 1 }$ and an addition of a constant to $t$ ，the transforms of $\varepsilon _ { 1 }$ and of $\varepsilon _ { 2 }$ are not distinct.A singular periodic solution exists in general in the domain where a solution in the form of purely trigonometric series is impossible.

An infinitesimal transformation， which transforms every ordinary periodic solution to an adjacent periodic solution of the same family with the same period and energy constant, corresponding to a small change of $\varepsilon$ ,is called an adelphic transformation by Whittaker (1917, 1928).An integral corresponds to an adelphic transformation.This is called an adelphic integral. A dynamical system with two degrees of freedom admits only one adelphic transformation,and hence only one adelphic integral. Another adelphic integral can be obtained by combining with the energy integral. The adelphic integral for the geodesic problem on an ellipsoid is $p d =$ constant.For the problems of one center of gravitation the adelphic integral is Euler's integral. If there is an ignorable coordinate, then the corresponding momentum put equal to a constant is an adelphic integral.

The difficulty may be avoided in the formulation of the famous theorem of Poincaré that a series in celestial mechanics,as will be discussed in the next chapter, is not uniformly convergent for all values of $t$ on one hand and for all values of the constants contained in two limits on the other hand. The unsatisfactory feature of usual series is caused by this deep-seated peculiarity in the nature of the problem. It is diffcult to discuss by the ordinary method of solution in celestial mechanics.By fixing our attention on a single integral of a dynamical system without aiming at the complete solution，we propose to find out what the peculiarity.of the problem is. We will see that it is closely related to an adelphic integral.

At first we try to find an adelphic integral of a dynamical system of two degrees of freedom

$$
\frac { d x _ { i } } { d t } = \frac { \partial H } { \partial y _ { i } } , \frac { d y _ { i } } { d t } = - \frac { \partial H } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

$$
H ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) = { \tt c o n s t a n t } ,
$$

where $\pmb { H }$ is written in the form of an infinite series proceeding in ascending powers of $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$ ，and in trigonometric form with multiples of $y _ { 1 }$ and $y _ { 2 }$ as the arguments:

$$
x _ { 1 } ^ { m / 2 } x _ { 2 } ^ { n / 2 } \cos { ( i y _ { 1 } + j y _ { 2 } ) } ,
$$

where $_ m$ and $_ n$ are positive integers including zero,and $_ i$ and $j$ are integers,positive or negative or zero，such that $m - | i |$ and $\dot { n } - | \dot { \boldsymbol { \jmath } } |$ are zero or an even integer. The sum $m + n$ is called the order of the term. The lowest-order terms are linear in $x _ { 1 }$ and $x _ { 2 }$ and independent of $y _ { 1 }$ and $y _ { 2 }$ . Write $H$ in the form

$$
H = s _ { 1 } x _ { 1 } + s _ { 2 } x _ { 2 } + H _ { 3 } + H _ { 4 } + \cdots ,
$$

where $H _ { r }$ is of order $r$ and

$$
H _ { 3 } = x _ { 1 } ^ { 3 / 2 } [ U _ { 1 } \cos y _ { 1 } + U _ { 2 } \cos 3 y _ { 1 } ]
$$

$$
\begin{array} { r l } { \textnormal { \texttt { * } } } & { \textnormal { \texttt { * } } _ { \mathrm { 1 } } x _ { \mathrm { 2 } } ^ { 1 / 2 } [ U _ { \mathfrak { s } } \cos y _ { \mathrm { 2 } } + U _ { \mathfrak { s } } \cos { ( 2 y _ { \mathrm { 1 } } + y _ { \mathrm { 2 } } ) } + U _ { \mathfrak { s } } \cos { ( 2 y _ { \mathrm { 1 } } - y _ { \mathrm { 2 } } ) } } \\ & { + \mathrm { \texttt { * } } _ { \mathrm { 1 } } x _ { \mathrm { 2 } } ^ { 1 / 2 } x _ { \mathrm { 2 } } [ U _ { \mathfrak { s } } \cos y _ { \mathrm { 1 } } + U _ { \tau } \cos { ( 2 y _ { \mathrm { 2 } } + y _ { \mathrm { 1 } } ) } + U _ { \mathfrak { s } } \cos { ( 2 y _ { \mathrm { 2 } } - y _ { \mathrm { 1 } } } } \\ & { + \mathrm { \texttt { * } } _ { \mathrm { 2 } } ^ { 3 / 2 } [ U _ { \mathfrak { s } } \cos y _ { \mathrm { 2 } } + U _ { \mathrm { 1 0 } } \cos { 3 y _ { \mathrm { 2 } } } ] . } \end{array}
$$

We now discuss three cases.

Case I. The ratio $s _ { 1 } / s _ { 2 }$ is irrational.

f $\phi ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) =$ constant is an integral, then we should have

$$
\begin{array} { r } { \frac { \partial \phi } { \partial x _ { 1 } } \frac { \partial H } { \partial y _ { 1 } } + \frac { \partial \phi } { \partial x _ { 2 } } \frac { \partial H } { \partial y _ { 2 } } - \frac { \partial \phi } { \partial y _ { 1 } } \frac { \partial H } { \partial x _ { 1 } } - \frac { \partial \phi } { \partial y _ { 2 } } \frac { \partial H } { \partial x _ { 2 } } = 0 , } \end{array}
$$

or (Section 4.3)

$$
( \phi , H ) = 0 .
$$

Put

$$
\phi = s _ { 1 } x _ { 1 } - s _ { 2 } x _ { 2 } + \phi _ { 3 } + \phi _ { 4 } + \cdot \cdot \cdot ,
$$

where $\phi _ { r }$ is an aggregate of terms of degree $r$ in $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$

Inserting this expansion of $\phi$ in (102) and equating the lowest-order terms to zero we obtain

$$
{ s _ { 1 } } \frac { { \partial \phi _ { 3 } } } { { \partial y _ { 1 } } } + { s _ { 2 } } \frac { { \partial \phi _ { 3 } } } { { \partial y _ { 2 } } } = { s _ { 1 } } \frac { { \partial H _ { 3 } } } { { \partial y _ { 1 } } } - { s _ { 2 } } \frac { { \partial H _ { 3 } } } { { \partial y _ { 2 } } } .
$$

This shows that to a term $\pmb { A }$ cos $( m y _ { 1 } + n y _ { 2 } )$ in $\pmb { H _ { 3 } }$ there corresponds in $\phi _ { 3 }$ a term

$$
\frac { s _ { 1 } m - s _ { 2 } n } { s _ { 1 } m + s _ { 2 } n } A \cos { ( m y _ { 1 } + n y _ { 2 } ) } .
$$

Thus $\phi _ { 3 }$ is easily calculated. Then equating the fourth-order terms from (102) to zero, we get

$$
{ s _ { 1 } } \frac { { \partial { \phi _ { 4 } } } } { { \partial { y _ { 1 } } } } + { s _ { 2 } } \frac { { \partial { \phi _ { 4 } } } } { { \partial { y _ { 2 } } } } = { s _ { 1 } } \frac { { \partial { H _ { 4 } } } } { { \partial { y _ { 1 } } } } - { s _ { 2 } } \frac { { \partial { H _ { 4 } } } } { { \partial { y _ { 2 } } } } + ( { \phi _ { 3 } , H _ { 3 } } ) .
$$

The function $\phi _ { 4 }$ can be derived, since the right-hand member is also known.Thus we find

$$
\begin{array} { r l } {  { \mathrm { t } = \phi \equiv s _ { 1 } x _ { 1 } - s _ { 2 } x _ { 2 } } } \\ & { \phantom { = } + x _ { 1 } ^ { 3 / 2 } [ U _ { 1 } \cos y _ { 1 } + U _ { 2 } \cos 3 y _ { 1 } ] } \\ & { \phantom { = } - x _ { 1 } x _ { 2 } ^ { 1 / 2 } \Big [ - U _ { 3 } \cos y _ { 2 } + \frac { 2 s _ { 1 } - s _ { 2 } } { 2 s _ { 1 } + s _ { 2 } } U _ { 4 } \cos ( 2 y _ { 1 } + y _ { 2 } ) } \end{array}
$$

$$
+ \frac { 2 s _ { 1 } + s _ { 2 } } { 2 s _ { 1 } - s _ { 2 } } U _ { 5 } \cos { ( 2 y _ { 1 } - y _ { 2 } ) } \Biggr ]
$$

$$
+ \frac { s _ { 1 } + 2 s _ { 2 } } { s _ { 1 } - 2 s _ { 2 } } U _ { 8 } \cos { ( 2 y _ { 2 } - y _ { 1 } ) } \ ]
$$

$$
\begin{array} { l } { { + x _ { 1 } ^ { 3 / 2 } [ - U _ { 9 } \cos y _ { 2 } - U _ { 1 0 } \cos 3 y _ { 2 } ] } } \\ { { + \ \cdots . } } \end{array}
$$

Consider a dynamical system with the Hamiltonian

$$
\begin{array} { r l } & { H = 2 ^ { 1 / 2 } x _ { 1 } \sin ^ { 2 } y _ { 1 } + x _ { 2 } \sin ^ { 2 } y _ { 2 } } \\ & { \qquad - \frac { 1 + 3 \cdot 2 ^ { 1 / 4 } x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } } { 3 ( 1 + 2 ^ { 5 / 4 } x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } + 2 ^ { 1 / 2 } x _ { 1 } \cos ^ { 2 } y _ { 1 } + 2 x _ { 2 } \cos ^ { 2 } y _ { 2 } ) ^ { 3 / 2 } } , } \end{array}
$$

or, if we expand this,

$$
\begin{array} { r l } & { H = 2 ^ { 1 / 2 } x _ { 1 } + x _ { 2 } + 2 ^ { 7 / 4 } x _ { 1 } ^ { 3 / 2 } [ - \cos y _ { 1 } - \frac { 1 } { 3 } \cos 3 y _ { 1 } ] } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x } + 2 ^ { - 3 / 4 } x _ { 1 } ^ { 1 / 2 } x _ { 2 } [ - 2 \cos y _ { 1 } - \cos ( y _ { 1 } + 2 y _ { 2 } ) - \cos ( y _ { 1 } - 2 y _ { 2 } ) ] } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x x } + \cdots . } \end{array}
$$

The integral (103) just obtained is

$$
\begin{array} { c c } { { \dag } } & { { = \phi \equiv 2 ^ { 1 / 2 } x _ { 1 } - x _ { 2 } + 2 ^ { 7 / 4 } x _ { 1 } ^ { 3 / 2 } ( - \cos y _ { 1 } - \frac { 1 } { 3 } \cos 3 y _ { 1 } ) } } \\ { { \dag } } & { { \dag + 2 ^ { - 3 / 4 } x _ { 1 } ^ { 1 / 2 } x _ { 2 } [ - 2 \cos y _ { 1 } + ( 1 - 2 ^ { 1 / 2 } ) ^ { 2 } \cos ( y _ { 1 } + 2 y _ { 2 } ) } } \\ { { \dag } } & { { \dag \ } } & { { \dag \ } } \\ { { \dag \ } } & { { \dag \ } } & { { \qquad ( 1 \mathrm { ~ + ~ } 2 ^ { 1 / 2 } ) ^ { 2 } \cos ( y _ { 1 } - 2 y _ { 2 } ) ] } } \\ { { \dag \ } } & { { \dag \ } } & { { \qquad ( 1 0 \mathrm { ~ } } } \end{array}
$$

The new dynamical system has an integral

$$
\mathrm { t } = [ x _ { 2 } ^ { 1 / 2 } \sin y _ { 2 } + 2 ^ { 1 / 4 } x _ { 1 } ^ { 1 / 2 } x _ { 2 } ^ { 1 / 2 } \sin y _ { 1 } \sin y _ { 2 } - 2 ^ { 3 / 4 } x _ { 1 } ^ { 1 / 2 } x _ { 2 } ^ { 1 / 2 } \sin y _ { 1 } \cos y _ { 2 } ] ^ { 2 }
$$

$$
- \frac { 1 + 2 ^ { 1 / 4 } x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } } { ( 1 + 2 ^ { 5 / 4 } x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } + 2 ^ { 1 / 2 } x _ { 1 } \cos ^ { 2 } y _ { 1 } + 2 x _ { 2 } \cos ^ { 2 } y _ { 2 } ) ^ { 1 / 2 } } ,
$$

or, if we expand this,

$$
\begin{array} { c } { { \mathrm { o n s t a n t } = x _ { 2 } + 2 ^ { - 1 / 4 } ( 1 - 2 ^ { 1 / 2 } ) x _ { 1 } ^ { 1 / 2 } x _ { 2 } \cos { ( y _ { 1 } ^ { . } + 2 y _ { 2 } ) } } } \\ { { - 2 ^ { 1 / 4 } ( 1 + 2 ^ { 1 / 2 } ) x _ { 1 } ^ { 1 / 2 } x _ { 2 } \cos { ( y _ { 1 } - 2 y _ { 2 } ) } } } \\ { { + \ \cdots . } } \end{array}
$$

This series (105) can be obtained by multiplying(106) by 2 and then subtracting the product from (104). The equation (104) is the energy integral of the new system.Thus the integral (1O3) is identical with the integral formed by algebraic and trigonometric processes under the condition assuring its convergency.Hence the series (1O3） may be inferred to be convergent insofar as $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$ are suffciently small, although the rigorous proof of the convergence seems to be difficult (see Bruns's proof in Section 15.4).

Thus,if the energy integral and the integral (103） are known， the dynamical problem of two degrees of freedom can be solved.By adding the energy integral to (103) we find

$$
\begin{array} { l } { { \displaystyle { + \left. x _ { 1 } x _ { 2 } ^ { 1 / 2 } \right[ \frac { 2 } { 2 s _ { 1 } + s _ { 2 } } U _ { 4 } \cos \left( 2 y _ { 1 } + y _ { 2 } \right) + \frac { 2 } { 2 s _ { 1 } + s _ { 2 } } U _ { 5 } \cos \left( 2 y _ { 1 } - y _ { 2 } \right) } } } \\ { { \displaystyle { + \left. x _ { 1 } ^ { 1 / 2 } x _ { 2 } \right[ \frac { 1 } { s _ { 1 } } U _ { 6 } \cos y _ { 1 } + \frac { 1 } { s _ { 1 } + 2 s _ { 2 } } U _ { \tau } \cos \left( 2 y _ { 2 } + y _ { 1 } \right) } } } \\  { \displaystyle { + \frac { 1 } { - \left. 1 \right. \left. U _ { \tau } \cos \left( 2 y _ { \tau } - y _ { 1 } \right) \right] } } } \end{array}
$$$$
+ \frac { 1 } { s _ { 1 } - 2 s _ { 2 } } U _ { 8 } \cos { ( 2 y _ { 2 , } - y _ { 1 } ) } \ ]
$$

We get by subtracting (103) from the energy integral

$$
l _ { 2 } = x _ { 2 } + x _ { 1 } x _ { 2 } ^ { 1 / 2 } \Bigl [ \frac { 1 } { S _ { 2 } } U _ { 3 } \cos y _ { 2 } + \frac { 1 } { 2 s _ { 1 } + s _ { 2 } } U _ { 4 } \cos \left( 2 y _ { 1 } + y _ { 2 } \right)
$$

$$
\displaystyle - \frac { 1 } { 2 s _ { 1 } - s _ { 2 } } U _ { 5 } \cos { ( 2 y _ { 1 } - y _ { 2 } ) } \Biggr ]
$$

$$
\begin{array} { l } { { \displaystyle + x _ { 1 } ^ { 1 / 2 } x _ { 2 } \biggl [ \frac { 2 } { s _ { 1 } + 2 s _ { 2 } } U _ { \tau } \cos { ( 2 y _ { 2 } + y _ { 1 } ) } - \frac { 2 } { s _ { 1 } - 2 s _ { 2 } } U _ { \circ } \cos { ( 2 y _ { 2 } - y _ { 1 } ) } } } \\ { { \displaystyle + x _ { 2 } ^ { 3 / 2 } \biggl [ \frac { 1 } { s _ { 2 } } U _ { \circ } \cos { y _ { 2 } } + \frac { 1 } { s _ { 2 } } U _ { \circ } \cos { 3 y _ { 2 } } \biggr ] } } \\ { { \displaystyle + \ \cdot \cdot \cdot , } } \end{array}
$$

where $l _ { 1 }$ and $l _ { 2 }$ are arbitrary constants. The first approximation gives $x _ { 1 } = l _ { 1 } , x _ { 2 } = l _ { 2 }$ .The second approximation is

$$
x _ { 1 } = l _ { 1 } - l _ { 1 } ^ { 3 / 2 } \Big [ \frac { 1 } { s _ { 1 } } U _ { 2 } \cos y _ { 1 } + \frac { 1 } { s _ { 2 } } U _ { 2 } \cos 3 y _ { 2 } \Big ]
$$

$$
\begin{array} { r l } {  { \mathrm { ~ \sum ~ } _ { i = 1 } ^ { 2 } \lfloor _ { S _ { 1 } } \cos { z } - \frac { 1 } { S _ { 1 } } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } + \frac { 2 } { 2 S _ { 1 } } U _ { 5 } \cos { ( 2 y _ { 1 } - y _ { 2 } ) } \rfloor } \quad } & { } \\ & { -  l _ { 1 } l _ { 2 } ^ { 1 2 } \Big [ \frac { 2 } { 2 S _ { 1 } + s _ { 2 } } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } + \frac { 2 } { 2 s _ { 1 } - s _ { 2 } } U _ { 5 } \cos { ( 2 y _ { 1 } - y _ { 2 } ) } \Big ]  } \\ & { -  l _ { 1 } ^ { 1 2 } l _ { 2 } \Big [ \frac { 1 } { S _ { 1 } } U _ { 6 } \cos { y _ { 1 } } + \frac { 1 } { s _ { 1 } + 2 s _ { 2 } } U _ { \tau } \cos { ( 2 y _ { 2 } + y _ { 1 } ) }  } \\ & { \qquad \quad +  \frac { 1 } { \mathrm { ~ \sum ~ } U _ { 5 } } \cos { ( 2 y _ { 2 } - y _ { 1 } ) } ] } \end{array}
$$

$$
x _ { 2 } = l _ { 2 } - l _ { 1 } l _ { 2 } ^ { 1 / 2 } \Big [ \frac { 1 } { S _ { 2 } } U _ { 3 } \cos y _ { 2 } + \frac { 1 } { 2 s _ { 1 } + s _ { 2 } } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) }
$$

$$
\displaystyle - \frac { 1 } { 2 s _ { 1 } - s _ { 2 } } U _ { 5 } \cos { ( 2 y _ { 1 } - y _ { 2 } ) } \Biggr ]
$$

$$
\begin{array} { l } { { \displaystyle - \frac { l _ { 1 } ^ { \prime 2 } l _ { 2 } } { l _ { 1 } ^ { \prime } + 2 s _ { 2 } } U _ { \tau } \cos { ( 2 y _ { 2 } + y _ { 1 } ) } - \frac { 2 } { s _ { 1 } - 2 s _ { 2 } } U _ { \tt s } \cos { ( 2 y _ { 2 } - y _ { 1 } ) } } } \\ { { \displaystyle - \frac { l _ { 2 } ^ { 3 / 2 } } { l _ { 2 } ^ { 3 } } \Big [ \frac { 1 } { S _ { 2 } } U _ { \tt s } \cos y _ { 2 } + \frac { 1 } { s _ { 2 } } U _ { \tt 1 0 } \cos 3 y _ { 2 } \Big ] } } \\ { { \displaystyle + \ \cdot \cdot \cdot . } } \end{array}
$$

Or we have

$$
x _ { 1 } = \frac { \partial W } { \partial y _ { 1 } } , \qquad x _ { 2 } = \frac { \partial W } { \partial y _ { 2 } } ,
$$

$$
W = l _ { 1 } y _ { 1 } + l _ { 2 } y _ { 2 } - l _ { 1 } ^ { 3 / 2 } \Big [ \frac { 1 } { S _ { 1 } } U _ { 1 } \sin y _ { 1 } + \frac { 1 } { 3 S _ { 1 } } U _ { 2 } \sin 3 y _ { 1 } \Big ]
$$

$$
- l _ { 1 } l _ { 2 } ^ { 1 / 2 } \Bigl [ \frac { 1 } { s _ { 2 } } U _ { 3 } \sin y _ { 2 } + \frac { 1 } { 2 s _ { 1 } + s _ { 2 } } U _ { 4 } \sin ( 2 y _ { 1 } + y _ { 2 } )
$$

$$
\begin{array} { c } { { + \displaystyle \frac { 1 } { 2 s _ { 1 } - s _ { 2 } } U _ { s } \sin { ( 2 y _ { 1 } - y _ { 2 } ) } \Bigg ] } } \\ { { - \displaystyle h _ { 1 } ^ { \prime } \mathcal { U } _ { \delta } \sin y _ { 1 } + \displaystyle \frac { 1 } { 2 s _ { 2 } + s _ { 1 } } U _ { \tau } \sin { ( 2 y _ { 2 } + y _ { 1 } ) } } } \\ { { + \displaystyle \frac { 1 } { 2 s _ { 2 } - s _ { 1 } } U _ { \star } \sin { ( 2 y _ { 2 } - y _ { 1 } ) } \Bigg ] } } \\ { { - \displaystyle \frac { b _ { 2 } ^ { \prime } \left[ \frac { 1 } { s _ { 2 } } U _ { s } \sin y _ { 2 } + \frac { 1 } { 3 s _ { 2 } } U _ { \parallel s } \sin { 3 y _ { 2 } } \right] } } } \\ { { + \displaystyle \ldots . . } } \end{array}
$$

Terms which contain $y _ { 1 }$ and $y _ { 2 }$ not as arguments of trigonometric functions are of the form $\alpha _ { 1 } y _ { 1 } + \alpha _ { 2 } y _ { 2 }$ ，where

$\alpha _ { 1 } = l _ { 1 } +$ terms of the fourth and higher orders in $l _ { 1 } ^ { 1 / 2 }$ and $l _ { 2 } ^ { 1 / 2 }$ ， $\alpha _ { 2 } = l _ { 2 } +$ terms of the fourth and higher orders in $l _ { 1 } ^ { 1 / 2 }$ and $l _ { 2 } ^ { 1 / 2 }$ ·

Inverting these series we obtain $l _ { 1 }$ and $l _ { 2 }$ in terms of $\alpha _ { 1 }$ and $\alpha _ { 2 }$ . Thus

$$
W = \alpha _ { 1 } y _ { 1 } + \alpha _ { 2 } y _ { 2 } - \alpha _ { 1 } ^ { 3 / 2 } \Bigl [ \frac { 1 } { s _ { 1 } } U _ { 1 } \sin y _ { 1 } + \frac { 1 } { 3 s _ { 1 } } U _ { 2 } \sin 3 y _ { 1 } \Bigr ]
$$

$$
\begin{array} { c } { { + \displaystyle \frac { 1 } { 2 s _ { 1 } - s _ { 2 } } U _ { \bar { s } } \sin { ( 2 y _ { 1 } - y _ { 2 } ) } \Big ] } } \\ { { { } } } \\ { { - \alpha _ { 1 } ^ { 1 / 2 } \alpha _ { 2 } \Big [ \displaystyle \frac { 1 } { s _ { 1 } } U _ { \bar { s } } \sin y _ { 1 } + \displaystyle \frac { 1 } { 2 s _ { 2 } + s _ { 1 } } U _ { \tau } \sin { ( 2 y _ { 2 } + y _ { 1 } ) } } } \\ { { { } } } \\ { { + \displaystyle \frac { 1 } { 2 s _ { 2 } - s _ { 1 } } U _ { \bar { s } } \sin { ( 2 y _ { 2 } - y _ { 1 } ) } \Big ] } } \\ { { { } } } \\ { { - \alpha _ { 2 } ^ { 3 / 2 } \Big [ \displaystyle \frac { 1 } { s _ { 2 } } U _ { \bar { s } } \sin y _ { 2 } + \displaystyle \frac { 1 } { 3 s _ { 2 } } U _ { \bar { s } ^ { 3 } } \sin { 3 y _ { 2 } } \Big ] } } \\ { { { } } } \\ { { + \ . . . } } \end{array}
$$

The variables $y _ { 1 }$ and $y _ { 2 }$ do not appear except in the combination $\alpha _ { 1 } y _ { 1 } + \alpha _ { 2 } y _ { 2 }$ and in the arguments of trigonometric functions. The system

$$
x _ { 1 } = \frac { \partial W } { \partial y _ { 1 } } , \qquad x _ { 2 } = \frac { \partial W } { \partial y _ { 2 } } , \qquad \beta _ { 1 } = \frac { \partial W } { \partial \alpha _ { 1 } } , \qquad \beta _ { 2 } = \frac { \partial W } { \partial \alpha _ { 2 } }
$$

defines a contact transformation from $( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } )$ to $( \alpha _ { 1 } , \alpha _ { 2 } , \beta _ { 1 } , \beta _ { 2 } )$ and the system

$$
\frac { d \alpha _ { 1 } } { d t } = \frac { \partial H } { \partial \beta _ { 1 } } , \frac { d \alpha _ { 2 } } { d t } = \frac { \partial H } { \partial \beta _ { 2 } } , \frac { d \beta _ { 1 } } { d t } = - \frac { \partial H } { \partial \alpha _ { 1 } } , \frac { d \beta _ { 2 } } { d t } = - \frac { \partial H } { \partial \alpha _ { 2 } }
$$

admits integrals $\alpha _ { 1 } =$ constant, $\alpha _ { 2 } =$ constant. The second pair of these equations give

$$
{ \beta _ { 1 } } = - \frac { { \partial { \cal H } ( \alpha _ { 1 } , \alpha _ { 2 } ) } } { { \partial \alpha _ { 1 } } } t + \varepsilon _ { 1 } , \qquad \beta _ { 2 } = - \frac { { \partial { \cal H } ( \alpha _ { 1 } , \alpha _ { 2 } ) } } { { \partial \alpha _ { 2 } } } t + \varepsilon _ { 2 } ,
$$

where $\varepsilon _ { 1 }$ and $\varepsilon _ { 2 }$ are arbitrary constants. Thus the solution is

$$
\frac { \partial W } { \partial y _ { 1 } } = x _ { 1 } , \qquad \frac { \partial W } { \partial y _ { 2 } } = x _ { 2 } ,
$$

$$
\frac { \partial W } { \partial \alpha _ { 1 } } = - \frac { \partial H ( \alpha _ { 1 } , \alpha _ { 2 } ) } { \partial \alpha _ { 1 } } t + \varepsilon _ { 1 } , \qquad \frac { \partial W } { \partial \alpha _ { 2 } } = - \frac { \partial H ( \alpha _ { 1 } , \alpha _ { 2 } ) } { \partial \alpha _ { 2 } } t + \varepsilon _ { 2 } .
$$

Hence the solution for the coordinates and momenta is expressed in trigonometric series with linear functions of $t$ as arguments. The arguments are of the form $m \beta _ { 1 } + n \beta _ { 2 }$ . The change of $\varepsilon _ { 1 }$ without any change of $\bar { \varepsilon } _ { 2 } , \alpha _ { 1 } ,$ and $\alpha _ { 2 }$ makes $l _ { 1 }$ and $l _ { 2 }$ invariant,and hence affects neither the integral (1O3) nor the energy integral,and makes the constant in the integral (1O3) and the energy constant invariant.Thus the infinitesimal transformation corresponding to the integral (1O3) transforms such orbits among such orbits themselves.Hence (1O5） is an adelphic integral of the dynamical system.

Case II.The ratio $s _ { 1 } / s _ { 2 }$ is rational and equal to $m / n$ , and further there is no term cos $( n y _ { 1 } - m y _ { 2 } )$ in $H _ { 3 }$

The integral (1O3) of Case I has a factor $( n s _ { 1 } - m s _ { 2 } )$ in the denominator, which vanishes for $s _ { 1 } / s _ { 2 } = m / n$ . This is the real root of the principal difficulty in celestial mechanics,as has been often quoted in the preceding chapters.We remove such terms from the series. Suppose that $s _ { 1 } = 2$ ， $s _ { 2 } = 1$ . The factor $s _ { 1 } - 2 s _ { 2 }$ appearing often in (103) is zero.The equation for $\phi _ { 3 }$ in this case is

$$
2 \frac { \partial \phi _ { 3 } } { \partial y _ { 1 } } + \frac { \partial \phi _ { 3 } } { \partial y _ { 2 } } = 2 \frac { \partial H _ { 3 } } { \partial y _ { 1 } } - \frac { \partial H _ { 3 } } { \partial y _ { 2 } } ,
$$

and those for $\phi _ { 4 } , \phi _ { 5 } , . . .$ are

$2 \frac { \partial \phi _ { r } } { \partial y _ { 1 } } + \frac { \partial \phi _ { r } } { \partial y _ { 2 } } = \mathsf { a }$ know su of ters th type

$$
x _ { 1 } ^ { m / 2 } x _ { 2 } ^ { n / 2 } \sin { ( k _ { 1 } y _ { 1 } + k _ { 2 } y _ { 2 } ) } .
$$

In integrating the equations for $\phi _ { \tau }$ in Case I we have used a particular integral corresponding to each known term of the right-hand member of each equation. If $s _ { 1 } = 2$ ， $s _ { 2 } = 1$ , then the arbitrary part of the solution contains terms of the type proper to $\phi _ { 3 }$ . Hence we write the integral of the equations

$$
2 \frac { \partial \phi _ { 3 } } { \partial y _ { 1 } } + \frac { \partial \phi _ { 3 } } { \partial y _ { 2 } } = x _ { 1 } ^ { 3 / 2 } \sin y _ { 1 }
$$

in the form

$$
\begin{array} { r } { \phi _ { 3 } = - \frac { 1 } { 2 } x _ { 1 } ^ { 3 / 2 } \cos y _ { 1 } + \alpha x _ { 1 } ^ { 1 / 2 } x _ { 2 } \cos { ( y _ { 1 } - 2 y _ { 2 } ) } , } \end{array}
$$

where $\alpha$ is an arbitrary constant.Thus terms with arbitrary coefficients in $\phi _ { 3 } , \phi _ { 4 } , \ldots$ are obtained. These arbitrary coefficients should then be computed so that terms with vanishing denominators are removed from the subsequently determined parts of $\phi$ . Thus an adelphic integral without vanishing denominator is obtained in Case II.

Consider a dynamical system with the Hamiltonian

$$
{ \begin{array} { r l } & { 2 x _ { 1 } \sin ^ { 2 } y _ { 1 } + x _ { 2 } \sin ^ { 2 } y _ { 2 } } \\ & { ~ + { \cfrac { 1 } { 2 ( 1 + 2 x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } + x _ { 1 } \cos ^ { 2 } y _ { 1 } + 2 x _ { 2 } \cos ^ { 2 } y _ { 2 } ) ^ { 2 } } } } \\ & { ~ - { \cfrac { 1 + x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } } { ( 1 + 2 x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } + x _ { 1 } \cos ^ { 2 } y _ { 1 } + 2 x _ { 2 } \cos ^ { 2 } y _ { 2 } ) ^ { 3 / 2 } } } , } \end{array} }
$$

or, by expanding this in powers of $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$

$$
\begin{array} { r l } & { H = 2 x _ { 1 } + x _ { 2 } + x _ { 1 } ^ { 3 / 2 } [ - \frac { 9 } { 2 } \cos y _ { 1 } - \frac { 3 } { 2 } \cos 3 y _ { 1 } ] } \\ & { \qquad + \ x _ { 1 } ^ { 2 } [ \frac { 7 5 } { 1 6 } + \frac { 2 5 } { 4 } \cos 2 y _ { 1 } + \frac { 2 5 } { 1 6 } \cos 4 y _ { 1 } ] } \\ & { \qquad + \ x _ { 1 } x _ { 2 } [ - 3 - 3 \cos 2 y _ { 1 } - 3 \cos 2 y _ { 2 } } \\ & { \qquad - \frac { 3 } { 2 } \cos { ( 2 y _ { 1 } + 2 y _ { 2 } ) } - \frac { 3 } { 2 } \cos { ( 2 y _ { 1 } - 2 y _ { 2 } ) } ] } \\ & { \qquad + \ x _ { 2 } ^ { 2 } [ - \frac { 9 } { 1 6 } - \frac { 5 } { 4 } \cos 2 y _ { 2 } - \frac { 3 } { 1 6 } \cos 4 y _ { 2 } ] } \\ & { \qquad + \ \cdot \cdot . } \end{array}
$$

Since the lowest degree term of the adelphic integral is $x _ { 2 }$ ， we have

$$
\phi = x _ { 2 } + \phi _ { 3 } + \phi _ { 4 } + \cdot \cdot \cdot .
$$

The $\phi _ { 3 }$ is determined by

$$
2 \frac { \partial \phi _ { 3 } } { \partial y _ { 1 } } + \frac { \partial \phi _ { 3 } } { \partial y _ { 2 } } = 0 ,
$$

or by

$$
\phi _ { 3 } = \alpha x _ { 1 } ^ { 1 / 2 } x _ { 2 } \cos { ( y _ { 1 } - 2 y _ { 2 } ) } ,
$$

with an arbitrary constant $\alpha$ . Similarly $\phi _ { 4 }$ is obtained from

$$
2 \frac { \partial \phi _ { 4 } } { \partial y _ { 1 } } + \frac { \partial \phi _ { 4 } } { \partial y _ { 2 } } = x _ { 1 } x _ { 2 } [ ( 6 + { \textstyle \frac { 9 } { 2 } } \alpha ) \sin 2 y _ { 2 } + ( 3 + { \textstyle \frac { 9 } { 4 } } \alpha ) \sin ( 2 y _ { 1 } + 2 y _ { 2 } )
$$

$$
\begin{array} { c } { { - \left( 3 + \frac { 9 } { 4 } \alpha \right) \sin \left( 2 y _ { 1 } - 2 y _ { 2 } \right) ] } } \\ { { + \ x _ { 2 } ^ { 2 } [ \frac { 3 } { 2 } \sin 2 y _ { 2 } + \frac { 3 } { 2 } \sin 4 y _ { 2 } ] } } \end{array}
$$

in the form

$$
\begin{array} { r } { \phi _ { 4 } = x _ { 1 } x _ { 2 } [ - ( 3 + \frac { 9 } { 4 } \alpha ) \cos 2 y _ { 2 } - ( \frac { 1 } { 2 } + \frac { 3 } { 8 } \alpha ) \cos ( 2 y _ { 1 } + 2 y _ { 2 } } \end{array}
$$

$$
\begin{array} { r } { + ( \frac { 9 } { 2 } + \frac { 9 } { 8 } \alpha ) \cos { ( 2 y _ { 1 } - 2 y _ { 2 } ) } ] + x _ { 2 } ^ { 2 } [ - \frac { 3 } { 4 } \cos { 2 y _ { 2 } } - \frac { 3 } { 1 6 } \cos { 4 y _ { 2 } } ] . } \end{array}
$$

The equation for $\phi _ { 5 }$ is

$$
2 \frac { \partial \phi _ { 5 } } { \partial y _ { 1 } } + \frac { \partial y _ { 5 } } { \partial y _ { 2 } } = \frac { \partial H _ { 5 } } { \partial y _ { 2 } } + ( \phi _ { 3 } , H _ { 4 } ) + ( \phi _ { 4 } , H _ { 3 } ) .
$$

We determine $_ { \alpha }$ so that the terms sin $( y _ { 1 } - 2 y _ { 2 } )$ should disappear from the right-hand members of this equation,that is,

$$
\begin{array} { r } { \frac { 3 9 } { 2 } - \frac { 4 5 } { 2 } ( 1 + \frac { 3 } { 4 } \alpha ) + \frac { 1 2 3 } { 8 } \alpha = 0 , } \end{array}
$$

$$
\alpha = - 2 .
$$

Substituting this value of $_ { \alpha }$ in $\phi _ { 3 }$ and $\phi _ { 4 }$ the integral is

$$
= x _ { 2 } - 2 x _ { 1 } ^ { 1 / 2 } x _ { 2 } \cos { ( y _ { 1 } - 2 y _ { 2 } ) }
$$

$$
\begin{array} { r l r } & { + \ x _ { 1 } x _ { 2 } [ \frac { 3 } { 2 } \cos \ 2 y _ { 2 } + \frac { 1 } { 4 } \cos \ ( 2 y _ { 1 } + 2 y _ { 2 } ) - \frac { 3 } { 4 } \cos \ ( 2 y _ { 1 } - 2 y _ { 2 } ) ] } \\ & { + \ x _ { 2 } ^ { 2 } [ - \frac { 3 } { 4 } \cos \ 2 y _ { 2 } - \frac { 3 } { 1 6 } \cos \ 4 y _ { 2 } ] } \\ & { + \ \cdot \cdot \cdot . } & { { \mathrm { ( 1 1 0 ) } } } \end{array}
$$

Thus we see that the dynamical system specified by (1O9) has an integral of the form

$$
\mathrm { \Delta t } = \frac { 1 } { 2 } [ \sqrt { 2 x _ { 2 } } \sin y _ { 2 } + x _ { 1 } ^ { 1 / 2 } \sqrt { 2 x _ { 2 } } \sin y _ { 1 } \sin y _ { 2 } - 2 \sqrt { 2 x _ { 1 } x _ { 2 } } \sin y _ { 1 } \sin y _ { 2 } ] ^ { 2 }
$$

$$
- \frac { 1 + x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } } { ( 1 + 2 x _ { 1 } ^ { 1 / 2 } \cos y _ { 1 } + x _ { 1 } \cos ^ { 2 } y _ { 1 } + 2 x _ { 2 } \cos ^ { 2 } y _ { 2 } ) ^ { 1 / 2 } } ,
$$

This is an adelphic integral, as can be seen easily. By expanding (111) in ascending powers of $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$ by the multinomial theorem,we see that the series is identical with (11O).Hence the series obtained in this Case II is convergent in all real values of $y _ { 1 }$ and $y _ { 2 }$ as far as $\left| x _ { 1 } \right|$ and $\left| x _ { 2 } \right|$ are smaller than a fixed number.

Case III. The ratio $s _ { 1 } / s _ { 2 }$ is rational and equal to $m / n$ ，but there is a term cos $( n y _ { 1 } - m y _ { 2 } )$ in $H _ { 3 }$ ·

Let one of the integrals of the diferential equations in terms of $( x _ { 1 } ,$ $x _ { 2 } , y _ { 1 } , y _ { 2 } )$ be

$$
\begin{array} { r } { f ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) + \frac { g ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) } { \mu } = \gamma , } \end{array}
$$

where $\gamma$ is an arbitrary constant and $\mu$ is a definite constant expressed in terms of the quantities appearing in the differential equations.This kind of integral loses its meaning when $\mu$ tends to zero.However, we can deduce an integral which has its meaning even for $\mu \to 0$ Suppose that $\mu \neq 0$ and write

$$
\mu f ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) + g ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) = \mu \gamma .
$$

Let $\mu \to 0$ ，then

$$
g ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) = c , \qquad c = \operatorname * { l i m } _ { \mu  0 } { ( \mu \gamma ) } .
$$

We apply this principle to the dynamical system defined by the Hamiltonian

$$
\begin{array} { r } { H = x _ { 1 } - 2 x _ { 2 } + x _ { 1 } ^ { 3 / 2 } U _ { 1 } \cos y _ { 1 } + x _ { 1 } x _ { 2 } ^ { 1 / 2 } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } . } \end{array}
$$

The adelphic integral obtained by the method which has been used for Case I from the Hamiltonian

$$
H = s _ { 1 } x _ { 1 } + s _ { 2 } x _ { 2 } + x _ { 1 } ^ { 3 / 2 } U _ { 1 } \cos y _ { 1 } + x _ { 1 } x _ { 2 } ^ { 1 / 2 } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) }
$$

with $s _ { 1 }$ and $s _ { 2 }$ arbitrary is in the form

constant

$$
\begin{array} { r l } {  { = s _ { 1 } x _ { 1 } - s _ { 2 } x _ { 2 } + x _ { 1 } ^ { 3 / 2 } U _ { 1 } \cos y _ { 1 } } } \\ & { + \frac { 2 s _ { 1 } - s _ { 2 } } { 2 s _ { 1 } + s _ { 2 } } x _ { 1 } x _ { 2 } ^ { 1 / 2 } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } } \\ & { + \frac { s _ { 2 } } { 2 s _ { 1 } + s _ { 2 } } U _ { 1 } U _ { 4 } x _ { 1 } ^ { 3 / 2 } x _ { 2 } ^ { 1 / 2 } \Big [ \frac { 4 \cos { ( y _ { 1 } + y _ { 2 } ) } } { s _ { 1 } + s _ { 2 } } } \\ & { \phantom { + } + \frac { 2 \cos { ( 3 y _ { 1 } + y _ { 2 } ) } } { 3 s _ { 1 } + s _ { 2 } } \Big ] } \end{array}
$$

$$
+ \ U _ { 1 } ^ { 2 } U _ { 4 } x _ { 1 } ^ { 2 } x _ { 2 } ^ { 1 / 2 } \frac { S _ { 2 } } { 2 s _ { 1 } + s _ { 2 } } \biggl [ - \frac { 3 } { 3 s _ { 1 } + s _ { 2 } } \frac { \cos { ( 4 y _ { 1 } + y _ { 2 } ) } } { 4 s _ { 1 } + s _ { 2 } }
$$

$2 s _ { 1 } + s _ { 2 }$ is the vanishing denominator in this series for $s _ { 1 } = 1$ ， $s _ { 2 } = - 2$ We modify this series so that the vanishing denominator disappears.

By the principle just described we proceed as follows.

The lowest term affected by the vanishing denominator is

$$
\frac { 2 s _ { 1 } - s _ { 2 } } { 2 s _ { 1 } + s _ { 2 } } x _ { 1 } x _ { 2 } ^ { 1 / 2 } U _ { 4 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } .
$$

Hence the corresponding lowest term in the integral is

$$
x _ { 1 } x _ { 2 } ^ { 1 / 2 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } .
$$

Write this integral in the form

$$
= \phi = x _ { 1 } x _ { 2 } ^ { 1 / 2 } \cos { ( 2 y _ { 1 } + y _ { 2 } ) } + \phi _ { 4 } + \phi _ { 5 } + \cdot \cdot \cdot ,
$$

where $\phi _ { \tau }$ is an aggregate of terms of order $r$ in $x _ { 1 } ^ { 1 / 2 }$ and $x _ { 2 } ^ { 1 / 2 }$ . Substituting this in the equation $( \phi , H ) = 0$ we get from the fourth-order terms the equation for $\phi _ { 4 }$

$$
\begin{array} { r } { \frac { \partial \phi _ { 4 } } { \partial y _ { 1 } } - 2 \frac { \partial \phi _ { 4 } } { \partial y _ { 2 } } = x _ { 1 } ^ { 3 / 2 } x _ { 2 } ^ { 1 / 2 } U _ { 1 } [ 2 \sin { ( y _ { 1 } + y _ { 2 } ) } + \sin { ( 3 y _ { 1 } + y _ { 2 } ) } ] . } \end{array}
$$

The integral is

$$
\phi _ { 4 } = x _ { 1 } ^ { 3 / 2 } x _ { 2 } ^ { 1 / 2 } U _ { 1 } [ 2 \cos { ( y _ { 1 } + y _ { 2 } ) } - \cos { ( 3 y _ { 1 } + y _ { 2 } ) } ] .
$$

We may add terms of the form

$$
\alpha x _ { 1 } ^ { 2 } + \beta x _ { 1 } x _ { 2 } + \gamma x _ { 2 } ^ { 2 }
$$

with arbitrary constants $\alpha , \beta , \gamma$ to this integral. This is equivalent to an addition of an arbitrary quadratic function of the energy integral and the adelphic integral. However the adelphic integral in the present case does not begin with linear terms in $x _ { 1 }$ and $x _ { 2 }$ . Hence we can determine the arbitrary constants of (114) so that terms with the vanishing denominator disappear from higher-order terms of $\phi$ . Thus we write

$$
\phi _ { 4 } = x _ { 1 } ^ { 3 / 2 } x _ { 2 } ^ { 1 / 2 } U _ { 1 } [ 2 \cos { ( y _ { 1 } + y _ { 2 } ) } - \cos { ( 3 y _ { 1 } + y _ { 2 } ) } ] + \alpha x _ { 1 } ^ { 2 }
$$

and substitute in the equation for $\phi _ { 5 }$

$$
\begin{array} { r } { \frac { \partial \phi _ { 5 } } { \partial y _ { 1 } } - 2 \frac { \partial \phi _ { 5 } } { \partial y _ { 2 } } = ( \phi _ { 4 } , H _ { 3 } ) . } \end{array}
$$

The terms containing sin $( 2 y _ { 1 } + y _ { 2 } )$ on the right-hand side are

$$
- 3 x _ { 1 } ^ { 2 } x _ { 2 } ^ { 1 / 2 } U _ { 1 } ^ { 2 } \sin { ( 2 y _ { 1 } + y _ { 2 } ) } - 4 \alpha x _ { 1 } ^ { 2 } x _ { 2 } ^ { 1 / 2 } U _ { 4 } \sin { ( }
$$

If

$$
\begin{array} { r } { \alpha = - \frac { 3 } { 4 } \frac { U _ { 1 } ^ { 2 } } { U _ { 4 } } , } \end{array}
$$

then all these terms vanish.In this way we can obtain the adelphic integral without the vanishing denominator by repeated application of this procedure.

Thus the adelphic integral is obtained for Case II and Case III.It can be employed for solving the system of differential equations in each of the three cases.The coordinates are expanded, however,in different forms according as the three cases. This circumstance supplies an underlying explanation of Poincaré's theorem that the series employed in celestial mechanics do not converge uniformly for any continuous range of values,because the series referred to are of the type discussed in Case I,and the series in Case I should be replaced by the series in Case II or in Case III when the constants $s _ { 1 }$ and $s _ { 2 }$ vary continuously from an irrational value to a rational value of the ratio