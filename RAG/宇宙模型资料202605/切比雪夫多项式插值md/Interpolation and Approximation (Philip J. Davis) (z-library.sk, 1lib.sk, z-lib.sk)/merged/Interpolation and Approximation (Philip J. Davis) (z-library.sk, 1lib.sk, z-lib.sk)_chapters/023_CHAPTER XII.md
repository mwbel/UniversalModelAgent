# CHAPTER XII

# Expansion Theorems for Orthogonal Functions

We have seen that under fairly general circumstances,Fourier expansions converge in the mean to the elements that gave rise to them.But for many purposes of mathematics, convergence in the mean is not sufficiently strong: we may want pointwise convergence,or even uniform convergence.In the present chapter we take three orthogonal systems and develop expansion theorems for them.They are(l） The sines and cosines,(2) The Legendre polynomials,(3) Complex orthogonal polynomials. In many ways,the behavior of(l) and (2) are very similar.The complex analytic case (3) is quite different and serves as a striking contrast to the first two.

12.1 The Historical Fourier Series. The system ${ \frac { 1 } { \sqrt { 2 \pi } } } , { \frac { 1 } { \sqrt { \pi } } } \sin \ x ,$ $\frac { 1 } { \sqrt { \pi } } \cos x , \frac { 1 } { \sqrt { \pi } } \sin 2 x , \frac { 1 } { \sqrt { \pi } } \cos 2 x , . . . ,$ is ortonormal on $[ - \pi , \pi ]$ with re spect to the inner product $( f , g ) = \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) \ d x$ The Fourier series of $f ( x )$ is therefore

$$
f ( x ) \sim { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k x + b _ { k } \sin k x
$$

where

$$
\begin{array} { l } { { a _ { k } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x ) \cos { k x } d x , ~ k = 0 , 1 , . . . , } } \\ { { { } } } \\ { { b _ { k } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } f ( x ) \sin { k x } d x ~ k = 1 , 2 , . . . . } } \end{array}
$$

Ex. 1.

$$
f ( x ) = \left\{ \begin{array} { r l r l } { 1 } & { { } } & { } & { { } 0 \leq x \leq \pi } \\ { - 1 } & { { } } & { } & { { } - \pi \leq x < 0 } \end{array} \right.
$$

$$
f ( x ) \sim _ { \pi } ^ { 4 } \left( \sin x + { \frac { \sin 3 x } { 3 } } + { \frac { \sin 5 x } { 5 } } + \cdot \cdot \cdot \right) .
$$

Ex. 2.

$$
f ( x ) = \left\{ \begin{array} { c c } { { \displaystyle \frac { \pi - x } { 2 } } } & { { \qquad 0 \leq x \leq \pi } } \\ { { \displaystyle \frac { - \pi - x } { 2 } } } & { { \qquad - \pi \leq x < 0 } } \end{array} \right.
$$

$$
f ( x ) \sim \sin x + { \frac { \sin 2 x } { 2 } } + { \frac { \sin 3 x } { 3 } } + \cdots .
$$

Ex. 3.

$$
f ( x ) = | x | , \qquad - \pi \leq x \leq \pi ,
$$

$$
f ( x ) \sim { \frac { \pi } { 2 } } - { \frac { 4 } { \pi } } \left( \cos x + { \frac { \cos 3 x } { 3 ^ { 2 } } } + { \frac { \cos 5 x } { 5 ^ { 2 } } } + \cdot \cdot \cdot \right) .
$$

Ex. 4.

$$
f ( x ) = x ^ { 2 } , \qquad - \pi \leq x \leq \pi ,
$$

$$
f ( x ) \sim { \frac { \pi ^ { 2 } } { 3 } } - 4 \left( \cos x - { \frac { \cos 2 x } { 2 ^ { 2 } } } + { \frac { \cos 3 x } { 3 ^ { 2 } } } - \cdot \cdot \cdot \right) .
$$

THEOREM 12.1.1．Let $f ( x )$ be continuous and periodic in $[ - \pi , \pi ]$ ， $( f ( \pi ) =$ $f ( - \pi ) )$ ,and suppose that the Fourier series of $\pmb { f } ( \pmb { x } )$ converges uniformly there. Then it converges to $f ( x )$

Proof: If ${ \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k x + b _ { k } \sin b a$ converges unifomly,it willcon verge to a continuous function of period $2 \pi$ . Call the sum $g ( { \pmb x } )$ ：

$$
g ( x ) = { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k x + b _ { k } \sin k x .
$$

Since we may integrate a uniformly convergent series term by term,we have by orthogonality

$$
( g , \cos k x ) = a _ { k } , ( g , \sin k x ) = b _ { k } .
$$

But by defnition of the Fourier coeffcients,

$$
( f , \cos k x ) = a _ { k } ( f , \sin k x ) = b _ { k } .
$$

Hence $( f - g , \cos k x ) = 0 , k = 0 , 1 , 2 , \ldots , ( f - g , \sin k x ) = 0 ,$ $k = 1 , 2 , \ldots$ By the completeness of the sines and cosines (Theorem 11.2.3), $\begin{array} { r } { f - g \equiv 0 } \end{array}$ and hence $\scriptstyle f \equiv g$

COROLLARY 12.1.2．Let $f ( x )$ be continuous and periodic in $[ - \pi , \pi ]$ and have Fourier coefficients $\pmb { a } _ { \pmb { k } }$ bLet $\sum _ { \mathfrak { c } = 1 } ^ { \infty } | a _ { \mathfrak { k } } | + | b _ { \mathfrak { k } } | < \infty$ Then the Fourier series of $f$ converges absolutely and uniformly to $f ( { \pmb x } ) , - { \pmb \pi } \leq { \pmb x } \leq { \pmb \pi } .$

Proof: Since $| a _ { k } \cos k x + b _ { k } \sin k x | \leq | a _ { k } | + | b _ { k } |$ ，it follows from the Weierstrass “M test’that the Fourier series converges uniformly and absolutely. By Theorem 12.1.1,it converges to $f ( x )$

Ex.5．In Examples 3 and 4 just considered,the sum of the Fourier coeffcients converges absolutely.Hence we may replace the“\~”by $^ { 6 6 } = ^ { 9 5 }$

The smoothness of the function drastically affects the size of the Fourier coeffcients: the smoother the function the more rapid is the decrease of the coeffcients. The study of the convergence of Fourier series is largely the study of the interplay between assumptions of smoothness and conclusions about convergence.

THEOREM 12.1.3．Let $\pmb { f } ( \pmb { x } )$ be periodic in $[ - \pi , \pi ]$ $, ( f ( \pi ) = f ( - \pi ) , f ^ { \prime } ( \pi ) =$ $f ^ { \prime } ( - \pi ) )$ and be of class $C ^ { \mathbf { 2 } }$ there. Then,the Fourier series of $\pmb { f } ( \pmb { x } )$ converges uniformly and absolutely to $f ( x )$

Proof: $a _ { n } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos$ nxe dx, $\pmb { n } = 1$ ,2,. Integrate by parts。.

$$
a _ { n } = f ( x ) { \frac { \sin n x } { \pi n } } { \Biggl | } _ { - \pi } ^ { \pi } - { \frac { 1 } { \pi n } } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x ) \sin n x d x = - { \frac { 1 } { \pi n } } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x ) \sin n x d x
$$

$$
= \frac { f ^ { \prime } ( x ) \cos n x } { \pi n ^ { 2 } } \bigg | _ { - \pi } ^ { \pi } - \frac { 1 } { \pi n ^ { 2 } } \int _ { - \pi } ^ { \pi } f ^ { \prime \prime } ( x ) \cos n x d x = - \frac { 1 } { \pi n ^ { 2 } } \int _ { - \pi } ^ { \pi } f ^ { \prime \prime } ( x ) \cos n x d x
$$

We use the fact that $f ( \pi ) = f ( - \pi ) , f ^ { \prime } ( \pi ) = f ^ { \prime } ( - \pi )$ Since $f ^ { \prime \prime }$ is continuous on $[ - \pi , \pi ]$ ，we have $| f ^ { \prime \prime } ( x ) | \leq M , - \pi \leq x \leq \pi ,$ so that

$$
| a _ { n } | \leq { \frac { 2 M } { n ^ { 2 } } } .
$$

A similar inequality can be derived for $b _ { n }$ .The conclusion now follows by applying Corollary 12.1.2.

In the above proof, the convergence of $\sum \left| a _ { n } \right| + \left| b _ { n } \right|$ is guaranteed by the convergence of f $\sum _ { 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } }$ The strength of the power $\pmb { n ^ { 2 } }$ is unnecessary for convergence and can be reduced to $\pmb { n } ^ { 1 + \varepsilon }$ ， $\varepsilon > 0$ .The appropriate smoothness is that the derivative of the function satisfy a Lipschitz condition.

THEOREM 12.1.4． Let $f ( x ) \in C ^ { n } [ - \pi , \pi ]$ ,for some $n \geq 1$ ， and have period $\pmb { 2 \pi }$ $( f ( - \pi ) = f ( \pi ) , f ^ { \prime } ( - \pi ) = f ^ { \prime } ( \pi ) , \textrm { . . . } , f ^ { ( n ) } ( - \pi ) = f ^ { ( n ) } ( \pi )$ ) Suppose that ${ f ^ { ( n ) } ( x ) }$ satisfies a Lipschitz condition of order $\alpha \colon 0 < \alpha \leq 1$ Then the Fourier coeffcients of $f$ satisfy $| a _ { k } |$ ， cntx，k=1,2,..，and the Fourier series converges uniformly to $f ( x ) \ i n \ [ - \pi , \pi ]$

Proof: We prove the case $\pmb { n = 1 }$ . The cases ${ \pmb n } > 1$ follow from this case by integration by parts as in Theorem 12.1.3.

Consider $\cdot a _ { n } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) { \mathrm { c o s ~ } } n x d x = - { \frac { 1 } { \pi n } } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x ) { \mathrm { s i n ~ } } n x d x . { \mathrm { ~ I n ~ t h i s ~ l a s t ~ } }$ integral, set $x = x ^ { \prime } + { \frac { \pi } { n } }$ . Then, for $\pmb { n } \geq 1$

$$
\begin{array} { l } { { a _ { n } = \displaystyle - \frac { 1 } { \pi n } \int _ { - \pi - \pi / n } ^ { \pi - \pi / n } f ^ { \prime } ( x ^ { \prime } + \pi / n ) \sin \Big ( x ^ { \prime } + \frac { \pi } { n } \Big ) d x ^ { \prime } } } \\ { { ~ = \displaystyle \frac { 1 } { \pi n } \int _ { - \pi - \pi / n } ^ { \pi - \pi / n } f ^ { \prime } ( x ^ { \prime } + \pi / n ) \sin n x ^ { \prime } d x ^ { \prime } } } \\ { { ~ = \displaystyle \frac { 1 } { \pi n } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x + \pi / n ) \sin n x d x , } } \end{array}
$$

where we have extended the definition of $f ( x )$ by periodicity. Thus,

$$
a _ { n } = { \frac { 1 } { 2 \pi n } } \int _ { - \pi } ^ { \pi } [ f ^ { \prime } ( x + \pi / n ) - f ^ { \prime } ( x ) ] \sin { n x } d x .
$$

Now $| f ^ { \prime } ( x + \pi / n ) - f ^ { \prime } ( x ) | \leq C \left( { \frac { \pi } { n } } \right) ^ { \alpha }$ ,al $_ { \pmb { x } }$ Hence $| a _ { n } | \leq { \frac { 1 } { 2 \pi n } } C \left( { \frac { \pi } { n } } \right) ^ { \alpha } \cdot 2 \pi =$ Aiilite

$$
\sum _ { n = 1 } ^ { \infty } | a _ { n } | + | b _ { n } | < \infty ,
$$

the series converges uniformly.

THEOREM 12.1.5. Let $\pmb { f } ( \pmb { x } )$ be continuous and periodic in $[ - \pi , \pi ]$ ，and have a derivative $\pmb { f } ^ { \prime } ( \pmb { x } )$ that is piecewise continuous in $[ - \pi , \pi ]$ . Then the Fourier series of $f ( x )$ converges uniformly and absolutely in $[ - \pi , \pi ]$ to $f ( { \pmb x } )$

Proof: By the above work,for $\pmb { n } \geq 1$ ， $a _ { n } = - \frac { 1 } { \pi n } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x )$ sin nx dx. Write   
${ a _ { n } } ^ { \prime } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ^ { \prime } ( x )$ sin nx dx. Since $f ^ { \prime }$ is piecewise continuous, it is in ${ \cal L } ^ { 2 } [ - \pi , \pi ]$   
By Corollary 11.2.5, $\sum _ { n = 1 } ^ { \infty } ( a _ { n } ^ { \prime } ) ^ { 2 } < \infty$ .Now

$$
\sum _ { n = 1 } ^ { \infty } | a _ { n } | = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n } } | a _ { n } { ' } | \leq \biggl ( \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } \biggr ) ^ { \frac { 1 } { 2 } } \biggl ( \sum _ { n = 1 } ^ { \infty } ( { a _ { n } { ' } } ) ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } < \infty .
$$

Hence $\sum _ { n = 1 } ^ { \infty } \left| a _ { n } \right| < \infty$ A similar argumet shws that $\sum _ { n = 1 } ^ { \infty } | b _ { n } | < \infty$ The theorem now follows by Corollary 12.1.2.

We note in passing that it is sufficient to assume that $f ^ { \prime } ( x ) \in L ^ { 2 } [ - \pi , \pi ]$ One can show that the integration by parts is still valid,and the remainder of the proof holds as before.

Ex.6.If $f ( x )$ is a continuous,periodic,piecewise linear function,its Fourier series converges uniformly and absolutely to $f ( x )$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/68578ff092e87269be32542a025b9eaad745473faf57266f1a5fd2a9de282513.jpg)  
Figure 12.1.1.

More penetrating analyses of the convergence of Fourier series are based upon the study of its partial sums,rather than its coefficients.It is assumed that $f$ is defined on $- \pi \leq x < \pi$ and then extended over the whole axis periodically.

LEMMA l2.1.6. The following is a trigonometric identity:

$$
{ \frac { 1 } { 2 } } + \cos x + \cos 2 x + \cdot \cdot \cdot + \cos n x = { \frac { \sin ( n + { \frac { 1 } { 2 } } ) x } { 2 \sin { \frac { x } { 2 } } } } .
$$

Proof:

$$
\sin { ( k + \frac { 1 } { 2 } ) } x - \sin { ( k - \frac { 1 } { 2 } ) } x = 2 \sin { \frac { x } { 2 } } \cos { k x } .
$$

Hence

$$
\begin{array} { c } { { 2 \sin \displaystyle \frac { x } { 2 } \sum _ { k = 0 } ^ { n } \cos k x = \sum _ { k = 0 } ^ { n } \left\{ \sin ( k + \frac { 1 } { 2 } ) x - \sin ( k - \frac { 1 } { 2 } ) x \right\} } } \\ { { = \sin ( n + \frac { 1 } { 2 } ) x - \sin ( - \frac { 1 } { 2 } ) x } } \end{array}
$$

$$
{ \frac { 1 } { 2 } } + \sum _ { k = 1 } ^ { n } \cos k x = { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) x } } { 2 \sin { \frac { x } { 2 } } } } .
$$

COROLLARY 12.1.7.

$$
\begin{array} { c } { { \displaystyle K _ { n } ( x , t ) = \frac { 1 } { 2 \pi } + \frac { 1 } { \pi } \sum _ { k = 1 } ^ { n } \cos n x \cos n t + \sin n x \sin n t } } \\ { { \displaystyle = \frac { 1 } { \pi } \frac { \sin ( n + \frac { 1 } { 2 } ) ( x - t ) } { 2 \sin \frac { 1 } { 2 } ( x - t ) } } } \end{array}
$$

COROLLARY 12.1.8.

$$
{ \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) } t d t } { \sin { \frac { 1 } { 2 } } t } } = 1 .
$$

The function ${ \cal K } _ { n } ( x , t )$ is called the Dirichlet kernel and stands in the same relation to the orthogonal system of sines and cosines as does the Kernel Polynomial to systems of orthogonal polynomials.The Dirichlet kernel will reproduce,under integration,finite trigonometric sums of the form

$$
\sum _ { k = 0 } ^ { n } A _ { k } \cos k x + B _ { k } \sin k x .
$$

$\stackrel { , } { f } ( x ) \sim \frac { a _ { 0 } } { 2 } + \sum _ { k = 0 } ^ { \infty } a _ { k } \cos k x +$ si x hen

$$
\mathcal { S } _ { n } ( f ; x ) =  { S _ { n } } ( x ) = \frac { a _ { 0 } } { 2 } + \sum _ { k = 1 } ^ { n } a _ { k } \cos k x + b _ { k } \sin k x .
$$

LEMMA 12.1.9.

$$
{ \cal S } _ { n } ( x ) - f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { \pi } { \frac { f ( x + t ) + f ( x - t ) - 2 f ( x ) } { \sin { \frac { t } { 2 } } } } \sin { ( n + { \frac { 1 } { 2 } } ) t } d t
$$

Pro0f:

$$
{ \mathcal { S } } _ { n } ( x ) = \int _ { - \pi } ^ { \pi } K _ { n } ( x , t ) f ( t ) d t = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) } ( x - t ) } { \sin { \frac { 1 } { 2 } } ( x - t ) } } f ( t ) d t .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/78fced7f4ffa4b91a26ff8ca11113eba07834fba340e028f22e9cb85e914fa22.jpg)  
Figure 12.1.2 The Dirichlet Kernel ${ \pmb K } _ { \mathfrak { s } } ( { \pmb x } , 0 )$

Set $t = t ^ { \prime } + x$

$$
\begin{array} { l } { { \displaystyle { \mathcal { S } _ { n } ( x ) = \frac { 1 } { 2 \pi } \int _ { - \pi - x } ^ { \pi - x } f ( t ^ { \prime } + x ) \frac { \sin { ( n + \frac { 1 } { 2 } ) t ^ { \prime } } } { \sin { \frac { 1 } { 2 } t ^ { \prime } } } d t ^ { \prime } } } } \\ { { \displaystyle { \quad = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( x + t ) \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { \sin { \frac { 1 } { 2 } t } } d t } , } } \end{array}
$$

where the $f$ has now been extended by periodicity. Thus,

$$
{ \cal S } _ { n } ( x ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } f ( x + t ) \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { \sin { \frac { 1 } { 2 } t } } d t + \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { 0 } f ( x + t ) \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { \sin { \frac { 1 } { 2 } t } } d t .
$$

In the last integral, set $t ^ { \prime } = - t$ ,and obtain,

$$
{ \mathcal { S } } _ { n } ( x ) = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { \pi } [ f ( x + t ) + f ( x - t ) ] { \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { \sin { \frac { 1 } { 2 } } t } } d t .
$$

Now, from Corollary 12.1.8,

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { \pi } 2 f ( x ) { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) t } } { \sin { \frac { t } { 2 } } } } d t .
$$

The lemma follows by subtracting (l2.1.6) from (12.1.5).

THEOREM 12.1.10 (Riemann-Lebesgue). Let $f ( x ) \in L [ a , b ]$ Then

$$
\operatorname* { l i m } _ { t \to \infty } \int _ { a } ^ { b } f ( x ) { \cos t } x d x = \operatorname* { l i m } _ { t \to \infty } \int _ { a } ^ { b } f ( x ) { \sin t } x d x = 0
$$

Proof: For suffciently smooth functions, say those belonging to class $C ^ { 1 } [ \pmb { a } , \pmb { b } ]$ ,this is proved very simply by integration by parts:

$$
\int _ { a } ^ { b } f ( x ) \cos t x d x = { \frac { 1 } { t } } { \biggl [ } f ( b ) \sin t b - f ( a ) \sin t a - \int _ { a } ^ { b } f ^ { \prime } ( x ) \sin t x d x { \biggr ] } .
$$

Hence,

$$
\bigg | \int _ { a } ^ { b } f ( x ) \cos { t x } d x \bigg | \le \frac { 1 } { t } \bigg [ | f ( b ) | + | f ( a ) | + \int _ { a } ^ { b } | f ^ { \prime } ( x ) | d x \bigg ] .
$$

Allowing $t \to \infty$ , we obtain the stated limit. A similar argument holds for the sine.

Suppose now_ that $f \in L [ a , b ]$ Given $\varepsilon > 0$ ，we can find a polynomial $p ( x )$ such that $\int _ { a } ^ { b } | f ( x ) - g ( x ) | d x \leq \varepsilon$ (See Ex. 4, 8.9.) Now,

$$
\begin{array} { r l r } {  { \bigg | \int _ { a } ^ { b } f ( x ) \cos t x d x \bigg | = \bigg | \int _ { a } ^ { b } ( f ( x ) - p ( x ) ) \cos t x d x + \int _ { a } ^ { b } p ( x ) \cos t x d x \bigg | } } \\ & { } & { \leq \int _ { a } ^ { b } | f ( x ) - p ( x ) | d x + \bigg | \int _ { a } ^ { b } p ( x ) \cos t x d x \bigg | . } \end{array}
$$

As argued above, ，

$$
\begin{array} { r } { \underset { t  \infty } { \operatorname* { l i m } } \int _ { a } ^ { b } p ( x ) \cos t x d x = 0 , \mathrm { a n d ~ h e n c e } } \\ { \underset { t  \infty } { \operatorname* { l i m } } \underset { t  \infty } { \operatorname* { s u p } } \Bigg | \int _ { a } ^ { b } f ( x ) \cos t x d x \Bigg | \leq \varepsilon . } \end{array}
$$

Sincc ε is arbitrary, $\operatorname* { l i m } _ { t \to \infty } \int _ { a } ^ { b } f ( x ) \cos t x d x = 0 .$

LEMMA 12.1.11． Let $f \in L [ - \pi , \pi ]$ For any $\delta$ such that $0 < \delta < \pi$ ，

$$
\displaystyle { \mathcal { S } _ { n } ( x ) - f ( x ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \delta } \frac { f ( x + t ) + f ( x - t ) - 2 f ( x ) } { \sin { \frac { t } { 2 } } } \sin { ( n + \frac { 1 } { 2 } ) t d t } }
$$

Proof: Write the integral (12.1.4)in the for $\cdot \mathrm { m } \int _ { 0 } ^ { \delta } + \int _ { \delta } ^ { \pi }$ . Notice that over $[ \delta , \pi ]$ ，the integrand is an integrable function and hence by the Riemann-Lebesgue Theorem, $\int _ { \delta } ^ { \pi } \to 0$ as $\pmb { n }  \infty$

LemvA 2.1.12. Let $f ( x ) \in L [ - \pi , \pi ]$ We have $\operatorname* { l i m } _ { n \to \infty } S _ { n } ( x ) - f ( x ) = 0$

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { \delta } [ f ( x + t ) + f ( x - t ) - 2 f ( x ) ] \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { t } d t = 0 .
$$

Proof: Consider $_ { x }$ as fixed and write

$$
\varphi ( t ) = f ( x + t ) + f ( x - t ) - 2 f ( x ) .
$$

By Lemma 12.1.11, $S _ { n } ( x ) - f ( x ) \to 0$ if and only if

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { \delta } \varphi ( t ) \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { \sin { \frac { t } { 2 } } } d t = 0 .
$$

Now,

$$
\begin{array} { c } { { 2 { \displaystyle \int _ { 0 } ^ { 6 } } \varphi ( t ) { \displaystyle { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) t } } { t } } } d t } } \\ { { = 2 { \displaystyle \int _ { 0 } ^ { 6 } } \varphi ( t ) { \displaystyle { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) t } } { \sin { \displaystyle { \frac { t } { 2 } } } } } } d t + { \displaystyle \int _ { 0 } ^ { 6 } } \varphi ( t ) { \displaystyle { \left( { \frac { 2 } { t } } - { \frac { 1 } { \sin { \displaystyle { \frac { t } { 2 } } } } } \right) } \sin { ( n + { \frac { 1 } { 2 } } ) t } } d t . } } \end{array}
$$

Inasmuch as $\frac { 2 } { t } - \frac { 1 } { \sin \frac { t } { 2 } }$ has no singularityat the origin,itis integrable over

$[ 0 , \delta ]$ .Hence，by the Riemann-Lebesgue Theorem,this last integral $ 0$ as ${ \pmb n }  \infty$ ,and the lemma follows.

THEOREM l2.1.13 (Riemann's Principle of Localization). Let $f ( x ) \in L [ - \pi , \pi ]$ and have $^ { \pmb { a } }$ Fourier Series

$$
f ( x ) \sim { \frac { a _ { 0 } } { 2 } } + \sum _ { n = 1 } ^ { \infty } a _ { n } \cos n x + b _ { n } \sin n x .
$$

The convergence of this series to $f ( x )$ at $^ { \pmb { a } }$ fxed point $_ { \pmb { x } }$ depends only upon the behavior of $f ( x )$ in an arbitrarily small neighborhood of $_ { \pmb { x } }$

Proof: By Lemma 12.1.12, convergence to $f ( x )$ depends upon

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { \delta } [ f ( x + t ) + f ( x - t ) - 2 f ( x ) ] \frac { \sin { ( n + \frac { 1 } { 2 } ) t } } { t } d t .
$$

Now this integral utilizes the values of $f ( x )$ only in the interval $( { \pmb x } - \delta ,$ ${ \pmb x } + \delta )$

THEOREM 12.1.14 (Dini's Criterion)．Let $_ { \pmb { x } }$ be fixed and suppose that

$$
\int _ { 0 } ^ { \delta } \left| \frac { \varphi ( t ) } { t } \right| d t < \infty .
$$

Then the Fourier series of $\pmb { f } ( \pmb { x } )$ converges at $_ x$ to $f ( x )$

Proof: Under the hypothesis, $\int _ { 0 } ^ { \delta } { \frac { \varphi ( t ) } { t } } \sin { ( n + \frac { 1 } { 2 } ) t } d t \to 0$ by the Riemann-Lebesgue Theorem. The theorem follows from Lemma 12.1.12.

COROLLARY 12.1.15. Let $f ( x )$ be differentiable at $_ { \ast }$ .Then the Fourier series of $f ( x )$ converges at $_ { \pmb { x } }$ to $f ( x )$

$$
\operatorname* { l i m } _ { t \to 0 } { \frac { f ( x + t ) - f ( x ) } { t } } = \operatorname* { l i m } _ { t \to 0 } { \frac { f ( x - t ) - f ( x ) } { t } } = f ^ { \prime } ( x ) .
$$

In a neighborhood of $\pmb { x }$ ,these two fractions,and consequently their sum, $\frac { \varphi ( t ) } { t }$ , are bounded functions of $\pmb { t }$ Thus, $\int _ { 0 } ^ { \delta } \left| \frac { \varphi ( t ) } { t } \right| d t < \infty .$

Actually, still less is required for convergence.

COROLLARY 12.1.16．Let $f$ satisfy $^ { \pmb { a } }$ Lipschitz condition of order $\alpha > 0$ at $\pmb { x }$ . Then the Fourier series of $f ( x )$ converges at $_ { x }$ to $f ( x )$

$$
\begin{array} { r l r } & { } & { P r o o f \colon | f ( x + t ) - f ( x ) | \le C t ^ { \alpha } ; \mathrm { ~ h e n c e ~ } \left| \frac { f ( x + t ) - f ( x ) } { t } \right| \le C t ^ { \alpha - 1 } \cdot \frac { \mu } { 2 } , \ } \\ & { } & { \displaystyle \left| \frac { \varphi ( t ) } { t } \right| < 2 C t ^ { \alpha - 1 } , \mathrm { a n d } \int _ { 0 } ^ { \delta } \left| \frac { \varphi ( t ) } { t } \right| d t < \infty . } \end{array}
$$

If $f$ has a simple jump discontinuity at a point, the Fourier Series converges to a value half way between the ends of the jump.To make this

precise,we shall suppose that at a point $_ { x }$ ,the two limits

$$
\operatorname* { l i m } _ { t \to 0 ^ { + } } f ( x + t ) = f ( x ^ { + } ) , \quad \operatorname* { l i m } _ { t \to 0 ^ { - } } f ( x + t ) = f ( x ^ { - } )
$$

exist.Suppose moreover, that at $x , f$ has both a right-hand derivative

$$
\operatorname* { l i m } _ { t \to 0 ^ { + } } { \frac { f ( x + t ) - f ( x ^ { + } ) } { t } } = f _ { + } { } ^ { \prime } ( x )
$$

anda left-hand derivative

$$
\operatorname* { l i m } _ { t \to 0 ^ { - } } { \frac { f ( x + t ) - f ( x ^ { - } ) } { t } } = f _ { - } { } ^ { \prime } ( x ) .
$$

THEOREM 12.1.17．Let $f \in L [ - \pi , \pi ]$ and at the point $_ { \pmb { x } }$ satisfy the above conditions. Then the Fourier Series for $f ( x )$ converges to the value

$$
{ \scriptstyle { \frac { 1 } { 2 } } } ( f ( x ^ { + } ) + f ( x ^ { - } ) ) .
$$

Proof:As in Lemma l2.1.9,we have

$$
{ \cal S } _ { n } ( x ) - \frac { \ i } { \ i } [ f ( x ^ { + } ) + f ( x ^ { - } ) ] = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } \frac { \varphi ( t ) \sin { ( n + \frac { \pi } { 2 } ) t } } { \sin \frac { t } { 2 } } d t
$$

where we now write

$$
\varphi ( t ) = f ( x + t ) + f ( x - t ) - 2 [ { \tt \frac { 1 } { 2 } } ( f ( x ^ { + } ) + f ( x ^ { - } ) ) ] .
$$

A parallel argument shows that Dini's criterion (l2.1.ll) is valid with this $\varphi ( t )$ . However, $\Bigg | \frac { \varphi ( t ) } { t } \Bigg | \leq \Bigg | \frac { f ( x + t ) - f ( x ^ { + } ) } { t } \Bigg | + \Bigg | \frac { f ( x - t ) - f ( x ^ { - } ) } { t } \Bigg |$ and in view of (12.1.13)and (12.1.14),we can find a $\delta$ suffciently small so that (12.1.11) holds.

COROLLARY 12.1.18．Let $f \in L [ - \pi , \pi ]$ and be piecewise smooth (each piece is in $C ^ { 1 }$ ）in $I = [ a , b ] , - \pi \leq a < b \leq \pi$ ，Then the Fourier series of $f$ converges at all points of $\boldsymbol { \mathit { I } }$ Its sum is $f ( x )$ at points of continuity and

$$
\frac { 1 } { 2 } ( f ( \pmb { x } ^ { + } ) + f ( \pmb { x } ^ { - } ) )
$$

at points of discontinuity.

12.2 Fejér's Theory of Fourier Series. The theory of divergent series makes much of a particular mode of summation introduced by $\mathbf { E }$ Cesaro. If an infinite series $\sum _ { \ i = 0 } ^ { \infty } a _ { \it \Pi _ { n } }$ diverges, its partial sums 1

$$
s _ { n } = { a } _ { 0 } + \cdots + { a } _ { n } ,
$$

of course, do not possess a limit. But it is quite possible that the averages

of the partial sums ${ \frac { 1 } { n + 1 } } \left( s _ { 0 } + s _ { 1 } + \cdots + s _ { n } \right)$ have a limit $s$ In such a case, the series $\sum _ { \ i = 0 } ^ { \infty } a _ { \it \ / n }$ is said to be $( C , 1 )$ summable to the value $\pmb { \vartheta }$ and we write

$$
s = \sum _ { n = 0 } ^ { \infty } a _ { n } , \quad ( C , 1 ) .
$$

Ex.1. $a _ { n } = ( - 1 ) ^ { n }$ . The series $1 - 1 + 1 - 1 + 1 - \cdot \cdot \cdot$ is divergent. The partial sums are $1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 \cdots .$ Their averages are $1 , \frac { 1 } { 2 } , \frac { 2 } { 3 } , \frac { 1 } { 2 } , \frac { 3 } { 5 } , \frac { 1 } { 2 } , \dots .$ The sequence of averages converges to $\scriptstyle { \frac { 1 } { 2 } }$ Thus $\begin{array} { l } { \frac { 1 } { 2 } = 1 - 1 + 1 - 1 + . . . , } \end{array}$ $( C , 1 )$

Ex. 2. $a _ { n } = ( - 1 ) ^ { n } n$ . The series $- 1 + 2 - 3 + 4 - 5 + \cdot \cdot \cdot$ is divergent. The partial sums are $- 1 , 1 , \ : - 2 , \ : 2 , \ : - 3 , 3 , \ : - 4 , 4 \cdot \cdot \cdot .$ Their averages are $^ { - 1 }$ ， $0 , \ - { \textstyle \frac { 2 } { 3 } } , \ 0 , \ - { \textstyle \frac { 3 } { 5 } } , \ 0 , \ - { \textstyle \frac { 4 } { 7 } } , \ 0 , \ \dots \ . \ . \ .$ This sequence does not converge and hencə the series is not summable $( C , 1 )$

As we have already proved (cf. 4.4), if $\sum _ { n = 0 } ^ { \infty } a _ { n }$ is convergent, then it is $( C , 1 )$ summable to the same value.

A family of summability methods of increasing strength is provided by Cesaro summability of rth order $( r > - 1 )$

DEFINITION l2.2.1. Given a series $\sum _ { n = 0 } ^ { \infty } a _ { n }$ Associate with it the formal   
power series $f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ and define constants $s _ { n } ^ { ( r ) }$ by means of the formal   
equation

$$
\frac { f ( x ) } { ( 1 - x ) ^ { r + 1 } } = \sum _ { n = 0 } ^ { \infty } s _ { n } ^ { ( r ) } x ^ { n } .
$$

If

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { s _ { n } ^ { ( r ) } } { \left( ^ n + { r } \right) } } = s ,
$$

then we shall write

$$
s = \sum _ { n = 0 } ^ { \infty } a _ { n } , ( C , r ) .
$$

In $1 9 0 4 { \mathrm { ~ L } }$ .Fejér made the remarkable discovery that the Fourier series of a continuous function $f ( x )$ is uniformly $( C , 1 )$ summable to $f ( x )$ . This stands in strong contrast to known fact (duBois-Reymond,l876,cf.Theorem 14.4.15) that there are continuous functions whose Fourier series are divergent at a point.Corresponding to the $( C , 1 )$ sums there is a kernel analogous to the Dirichlet kernel.The latter is oscillating,but Fejér's kernel is positive.

LEMMA 12.2.1. The following is a trigonometrical identity:

$$
\sin { \frac { x } { 2 } } + \sin { \frac { 3 } { 2 } } x + \cdots + \sin ( n - { \frac { 1 } { 2 } } ) x = { \cfrac { \sin ^ { 2 } { \frac { n x } { 2 } } } { \sin { \frac { x } { 2 } } } } .
$$

Prof: sin $( k - { \textstyle \frac { 1 } { 2 } } ) x \sin { \frac { x } { 2 } } = { \textstyle \frac { 1 } { 2 } } [ \cos { ( k - 1 ) x } - \cos { k x } ] .$ Hence,

$$
\begin{array} { l } { \displaystyle \sum _ { k = 1 } ^ { n } \sin { ( k - \frac { 1 } { 2 } ) } x \sin { \frac { x } { 2 } } = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { n } ( \cos { ( k - 1 ) x } - \cos { k x } ) } \\ { \displaystyle \qquad = \sin { \frac { x } { 2 } } \sum _ { k = 1 } ^ { n } \sin { ( k - \frac { 1 } { 2 } ) } x = \frac { 1 } { 2 } [ 1 - \cos { n x } ] = \sin ^ { 2 } { \frac { n x } { 2 } } . } \end{array}
$$

Therefore

$$
\sum _ { k = 1 } ^ { n } \sin { ( k - \frac { 1 } { 2 } ) x } = { \frac { \sin ^ { 2 } { \frac { n x } { 2 } } } { \sin { \frac { x } { 2 } } } } .
$$

LemMA 2.23 . $S _ { n } ( x ) = { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { n } a _ { k }$ cos $k x + b _ { k }$ sin $k x$ be the partal sum of the Fourier series of $( x ) . L e t \sigma _ { n } ( x ) = { \frac { 1 } { n } } ( S _ { 0 } ( x ) + S _ { 1 } ( x ) + \cdots + S _ { n - 1 } ( x ) ) .$ Then,

$$
\sigma _ { n } ( x ) = { \frac { 1 } { 2 \pi n } } \int _ { 0 } ^ { \pi } [ f ( x + t ) + f ( x - t ) ] { \frac { \sin ^ { 2 } { \frac { n } { 2 } } t } { \left( \sin { \frac { t } { 2 } } \right) ^ { 2 } } } d t .
$$

Pro0f:From (12.1.5)， Sx(x) = $\mathrm { ~ n ~ } \left( 1 2 . 1 . 5 \right) , \mathrm { ~ } S _ { k } ( x ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } [ f ( x + t ) + f ( x - t ) ] \frac { \sin { ( k + \frac { 1 } { 2 } ) t } } { \sin { \frac { t } { 2 } } } d t .$

Hence,

$$
\begin{array} { c } { { \displaystyle \sigma _ { n } ( x ) = \frac { 1 } { 2 \pi n } \int _ { 0 } ^ { \pi } \frac { [ f ( x + t ) + f ( x - t ) ] } { \sin { \frac { t } { 2 } } } \displaystyle \sum _ { k = 0 } ^ { n - 1 } \sin { ( k + \frac { 1 } { 2 } ) t } ~ d t } } \\ { { \displaystyle - \frac { 1 } { 2 \pi n } \int _ { 0 } ^ { \pi } [ f ( x + t ) + f ( x - t ) ] \frac { \sin ^ { 2 } { \frac { n t } { 2 } } } { \left( \sin { \frac { t } { 2 } } \right) ^ { 2 } } d t . } } \end{array}
$$

COROLLARY 12.2.3.

$$
\frac { 1 } { \pi n } \int _ { 0 } ^ { \pi } \frac { \sin ^ { 2 } \frac { n } { 2 } t } { \sin ^ { 2 } \frac { t } { 2 } } d t = 1 .
$$

Proof: Take $f ( x ) \equiv 1$ .Then the above integral is ${ \pmb \sigma _ { n } } ( x )$ for the Fourier series $\mathbf { l } + \mathbf { 0 } + \mathbf { 0 } + \cdots$ .It is readily verifed that ${ \pmb \sigma } _ { n } ( { \pmb x } ) \equiv { \bf 1 }$

COROLLARY 12.2.4. The Fejer sums ${ \pmb \sigma } _ { \pmb { n } } ( x )$ are bounded by the bounds of $f ( x )$ itself; that is to say,if $m \le f ( x ) \le M$ then $m \leq \sigma _ { n } ( x ) \leq M$

Proof: If $f ( x ) \leq M$ then $f ( x + t ) + f ( x - t ) \leq 2 M$ so that

$$
\sigma _ { n } ( x ) \leq { \frac { 2 M } { 2 \pi n } } \int _ { 0 } ^ { \pi } { \frac { \sin ^ { 2 } { \frac { n t } { 2 } } } { \sin ^ { 2 } { \frac { t } { 2 } } } } d t = M .
$$

Similarly for the lower bound.

LEMMA 12.2.5. For a fixed $_ { \pmb { x } }$ set $\varphi ( t ) = f ( x + t ) + f ( x - t ) - 2 f ( x )$ and

$$
K _ { n } ( t ) = \frac { 1 } { 2 \pi n } \frac { \sin ^ { 2 } \frac { n } { 2 } t } { \sin ^ { 2 } \frac { t } { 2 } } .
$$

Then we have

$$
\sigma _ { n } ( x ) - f ( x ) = \int _ { 0 } ^ { \pi } K _ { n } ( t ) \varphi ( t ) ~ d t
$$

Proof:By Corollary 12.2.3

$$
f ( x ) = { \frac { 1 } { 2 \pi n } } \int _ { 0 } ^ { \pi } { \frac { \sin ^ { 2 } { \frac { n } { 2 } } t } { \sin ^ { 2 } { \frac { t } { 2 } } } } f ( x ) d t .
$$

By subtracting (12.2.9) from (12.2.6) we obtain (12.2.8).

The function $K _ { n } ( t ) = { \frac { \sin ^ { 2 } { \frac { n } { 2 } } t } { 2 \pi n \sin ^ { 2 } { \frac { t } { 2 } } } }$ is known as the Fejer kernel.It satisfies

not only

$$
K _ { n } ( t ) \geq 0
$$

but also

$$
\int _ { 0 } ^ { \pi } K _ { n } ( t ) \ d t = { \mathrm { c o n s t a n t } } , \quad n = 1 , 2 , \ldots , \quad ( { \mathrm { C o r . ~ 1 1 . 2 . 3 } } ) ,
$$

and

$$
\operatorname* { l i m } _ { n \to \infty } M _ { n } ( \delta ) = 0
$$

where

$$
M _ { n } ( \delta ) = \operatorname* { m a x } _ { \delta \leq t \leq \pi } K _ { n } ( t ) .
$$

$$
\mathrm { \AA h i s ~ l a s t ~ f o l l o w s ~ f r o m } \frac { \sin ^ { 2 } \frac { n t } { 2 } } { 2 \pi n \sin ^ { 2 } \frac { t } { 2 } } \leq \frac { 1 } { 2 \pi n \left( \sin \frac { \delta } { 2 } \right) ^ { 2 } } \mathrm { i n } ~ \delta \leq t \leq \pi .
$$

Continuous functions that satisfy the three conditions (12.2.1o,ll,12) are known as general Fejér kernels.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/829b142628fdb3600e319ed652ff98bf97f96f5bf82c9ffff7f3ab5a4a320a4d.jpg)  
Figure 12.2.1 Fejer's Kernel ${ K _ { 6 } ( t ) }$

LEMMA 12.2.6. $\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | \sigma _ { n } ( x ) - f ( x ) | \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { 0 } \int _ { 0 } ^ { \delta } K _ { n } ( t ) | \varphi ( t ) | d t .$ Proof: From (12.2.8),

$$
| \sigma _ { n } ( x ) - f ( x ) | \leq \int _ { 0 } ^ { \pi } K _ { n } ( t ) \left| \varphi ( t ) \right| d t
$$

$$
\leq \int _ { 0 } ^ { \delta } K _ { n } ( t ) \left| \varphi ( t ) \right| d t + \int _ { \delta } ^ { \pi } K _ { n } ( t ) \left| \varphi ( t ) \right| d t
$$

Now, in view of (12.2.12),we have

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | \sigma _ { n } ( x ) - f ( x ) | \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { 0 } ^ { \delta } K _ { n } ( t ) | \varphi ( t ) | d t .
$$

THEOREM 12.2.7．Let $f ( x ) \in L [ - \pi , \pi ]$ and be continuous at the point $\pmb { x }$ Then

$$
\operatorname* { l i m } _ { n \to \infty } \sigma _ { n } ( x ) = f ( x ) .
$$

Proof: $\varphi ( t ) = f ( x + t ) + f ( x - t ) - 2 f ( x )$ If $f$ is continuous at $\pmb { x }$ given an $\varepsilon > 0$ ,we can find a $\delta > 0$ such that $| \varphi ( t ) | < \varepsilon$ for all $0 \leq t \leq \delta$ Now, with this $\delta , \int _ { 0 } ^ { \delta } K _ { n } ( t ) \left| \varphi ( t ) \right| d t \leq \varepsilon \int _ { 0 } ^ { \delta } K _ { n } ( t ) d t \leq \varepsilon \int _ { 0 } ^ { \pi } K _ { n } ( t ) d t = { \frac { \varepsilon } { 2 } }$ By Lemma

12.2.6, lim sup $| \sigma _ { n } ( x ) - f ( x ) | \leq \frac { \varepsilon } { 2 }$ .But $\pmb \varepsilon$ is arbitrary and hence

$$
\operatorname* { l i m } _ { n \to \infty } \sigma _ { n } ( x ) = f ( x ) .
$$

This conclusion can be strengthened under the assumption that $f ( x )$ is continuous in some closed interval $I : [ a , b ]$

THEOREM 12.2.8. $L e t f ( x ) \in L [ - \pi , \pi ] a n d \in C [ a , b ] w h e r e - \pi \leq a < b \leq \pi ;$ Then $\operatorname* { l i m } _ { n \to \infty } \sigma _ { n } ( x ) = f ( x )$ uniformly in $\scriptstyle I \colon [ a , b ]$

Proof: $f ( x )$ is uniformly continuous in $\boldsymbol { I }$ Hence, given an $\pmb \varepsilon$ ,we can find a $\delta$ such that

$$
\begin{array} { c } { { | \varphi ( t ) | = | f ( x + t ) + f ( x - t ) - 2 f ( x ) | } } \\ { { \mathrm { } } } \\ { { \leq | f ( x + t ) - f ( x ) | + | f ( x - t ) - f ( x ) | \leq \varepsilon } } \end{array}
$$

for $0 \leq t \leq \delta$ and for all $_ { x }$ in $\pmb { I }$ As before,

$$
| \sigma _ { n } ( x ) - f ( x ) | \leq \int _ { 0 } ^ { \delta } K _ { n } ( t ) \ | \varphi ( t ) | \ d t + M _ { n } ( \delta ) { \int _ { \delta } ^ { \pi } } | \varphi ( t ) | \ d t .
$$

Now,

$$
\begin{array} { r l } { \displaystyle \int _ { \delta } ^ { \pi } \lvert \varphi ( t ) \rvert d t } & { \le \displaystyle \int _ { 0 } ^ { \pi } \lvert \varphi ( t ) \rvert d t \le \displaystyle \int _ { 0 } ^ { \pi } \lvert f ( x + t ) \rvert d t + \displaystyle \int _ { 0 } ^ { \pi } \lvert f ( x - t ) \rvert d t + 2 \displaystyle \int _ { 0 } ^ { \pi } \lvert f ( x ) \rvert d t } \\ { \displaystyle } & { = \displaystyle \int _ { - \pi } ^ { \pi } \lvert f ( x + t ) \rvert d t + 2 \pi \lvert f ( x ) \rvert = \displaystyle \int _ { - \pi } ^ { \pi } \lvert f ( t ) \rvert d t + 2 \pi \lvert f ( x ) \rvert . } \end{array}
$$

For $x \in I , f$ is continuous and hence $| f | \leq M$ . Thus,

$$
\int _ { \delta } ^ { \pi } \left| \varphi ( t ) \right| d t \leq \int _ { - \pi } ^ { \pi } | f ( t ) | d t + 2 \pi M = { \mathrm { c o n s t . } } , \qquad x \in I .
$$

Finally, for all $x \in I$ ，

$$
| \sigma _ { n } ( x ) - f ( x ) | \leq \varepsilon \int _ { 0 } ^ { \delta } K _ { n } ( t ) d t + M _ { n } ( \delta ) \cdot { \mathrm { c o n s t . } } \leq { \frac { \varepsilon } { 2 } } + M _ { n } ( \delta ) \cdot { \mathrm { c o n s t . } }
$$

This bound is independent of $_ x$ ,and hence the convergence is uniform.

COROLLARY 12.2.9．Let $f ( x )$ be continuous and periodic in $[ - \pi , \pi ]$ . Then it may be approximated uniformly by trigonometric polynomials.

Proof: The trigonometric polynomials $\sigma _ { n } ( x )$ will serve as approximants.

THEOREM 12.2.10．Let $f \in L [ - \pi , \pi ]$ and suppose that at $^ { \pmb { a } }$ point $x , f ( x )$ has left-hand and right-hand limits, $f ( x ^ { + } )$ and $f ( x ^ { - } )$ ; then

$$
\operatorname * { l i m } _ { n  \infty } \sigma _ { n } ( x ) = \frac { 1 } { 2 } [ f ( x ^ { + } ) + f ( x ^ { - } ) ] .
$$

Proof:As before,we can write

$$
\sigma _ { n } ( x ) - { \mathfrak { z } } [ f ( x ^ { + } ) + f ( x ^ { - } ) ] = \int _ { 0 } ^ { \pi } K _ { n } ( t ) \varphi ( t ) d t
$$

where we now write $\varphi ( t ) = f ( x + t ) + f ( x - t ) - 2 [ { \textstyle \frac { 1 } { 2 } } ( f ( x ^ { + } ) + f ( x ^ { - } ) ) ]$ The proof now proceeds as in Theorem 12.2.7.

12.3 Fourier Series of Periodic Analytic Functions. We turn from periodic functions of great generality to periodic functions that are also analytic.Naturally,convergence must be uniform (Theorem l2.1.3),but the Fourier series emerges as a transformed version of the Laurent expansion,and convergence takes place over an entire strip of the complex plane.

It will be more convenient to deal with the complex form of the Fourier series and to assume that we are dealing with a complex function that has the complex period $\pmb { p }$ ：

$$
f ( z ) = f ( z + p ) .
$$

In the real Fourier series

$$
f ( x ) \sim { \frac { a _ { 0 } } { 2 } } + \sum _ { n = 1 } ^ { \infty } a _ { n } \cos n x + b _ { n } \sin n x
$$

place cos $n x = { \mathfrak { k } } ( e ^ { i n x } + e ^ { - i n x } )$ ,sin $n x = { \frac { i } { 2 } } \left( - e ^ { i n x } + e ^ { - i n x } \right)$ ,and obtain

$$
f ( x ) \sim \frac { a _ { 0 } } { 2 } + \sum _ { n = 1 } ^ { \infty } \left( \frac { a _ { n } - i b _ { n } } { 2 } \right) e ^ { i n x } + \left( \frac { a _ { n } + i b _ { n } } { 2 } \right) e ^ { - i n x } .
$$

This may be rewritten formally as

$$
f ( x ) \sim \sum _ { - \infty } ^ { + \infty } c _ { n } e ^ { i n x }
$$

where

$$
c _ { 0 } = \frac { a _ { 0 } } { 2 } , ~ c _ { n } = \frac { a _ { n } - i b _ { n } } { 2 } , ~ c _ { - n } = \frac { a _ { n } + i b _ { n } } { 2 } = \bar { c } _ { n } .
$$

In general,a complex Fourier series with a complex period $\pmb { p }$ is one that can be written in the form

$$
f ( z ) \sim \sum _ { - \infty } ^ { \infty } a _ { n } e ^ { 2 \pi i n z / p }
$$

where

$$
a _ { n } = { \frac { 1 } { p } } \int _ { z _ { 0 } } ^ { z _ { 0 } + p } f ( z ) e ^ { - 2 \pi i n z / p } d z .
$$

If ${ z _ { 0 } }$ and $\pmb { p }$ are real and if ${ \pmb a } _ { n } = \bar { \pmb a } _ { - n }$ ,then (l2.3.6) reduces to a real Fourier series.

Let us suppose that we have a function $f ( z )$ defined on a line $L \colon z _ { 0 } + \sigma p$ ， $- \infty < \sigma < \infty$ ,lying in the complex plane. $f ( z )$ will be assumed to have period $\pmb { p }$ and be analytic on $\pmb { L }$ .We can continue the function $f ( z )$ from the line into the complex plane,and in view of periodicity,it is clear that we can find an infnite strip of constant width parallel to $L$ and containing $\boldsymbol { L }$ in which $f ( z )$ may be assumed to be both periodic and analytic.There is a largest such strip.In certain instances it may degenerate to a half-plane or the entire plane.The maximum strip of analyticity of $f ( z )$ will be called $\pmb { S }$ and can be described in the following way

$$
S \colon \ - \infty \leq t _ { 1 } < \operatorname { I m } \left( \frac { z } { p } \right) < t _ { 2 } \leq \infty .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/90037cbfb8f43b6eeb95b9d44696d0ba5edcd816c12de9f5a0ce440052ca11ea.jpg)  
Figure 12.3.1.

THEOREM 12.3.1． Let $f ( z )$ be analytic in $\pmb { S }$ and have period $\pmb { p }$ . Then

$$
f ( z ) = \sum _ { k = - \infty } ^ { + \infty } a _ { k } e ^ { 2 \pi i n z / p }
$$

where

$$
a _ { k } = \frac { 1 } { p } \int _ { z _ { 0 } } ^ { z _ { 0 } + p } f ( z ) e ^ { - 2 \pi i n z / p } d z .
$$

The series (12.3.8) converges uniformly and absolutely in every substrip $S ^ { \prime } \colon t _ { 1 } < t _ { 1 } ^ { \prime } \leq \operatorname { I m } \left( z / p \right) \leq t _ { 2 } ^ { \prime } < t _ { 2 } .$

Proof: Make the change of variable

$$
w = e ^ { ( 2 \pi i z / p ) } , ~ z = \frac { p } { 2 \pi i } \log w .
$$

This function maps the strip $\pmb { S }$ into the annulus

$$
A \colon \ e ^ { - 2 \pi t _ { 2 } } < | w | < e ^ { - 2 \pi t _ { 1 } }
$$

in the w-plane.

Asa matter of fact,each period rectangle is mapped into the annulus so that the infinity of points of $S , z \pm m p , m$ integer,have the same image in $\pmb { A }$ . In view of the analyticity and periodicity of $f ( z )$ ，the function $g ( w ) =$

$f { \left( { \frac { p } { 2 \pi i } } \log w \right) }$ has a Laurent expansion

$$
g ( w ) = \sum _ { n = - \infty } ^ { + \infty } b _ { n } w ^ { n }
$$

with

$$
b _ { n } = \frac { 1 } { 2 \pi i } \int _ { C } \frac { g ( w ) } { w ^ { n + 1 } } d w \qquad n = 0 , \pm 1 , \pm 2 , . . . .
$$

$\pmb { c }$ is any circle $| w | = \rho$ contained in $\pmb { A }$ .In particular, select $\rho = e ^ { - 2 \pi \operatorname { I m } ( z _ { 0 } / p ) }$ . The series (l2.3.l2) converges uniformly and absolutely in any sub-annulus. Passing back to the $\pmb { w }$ variable,

$$
f ( z ) = g ( e ^ { 2 \pi i z / p } ) = \sum _ { n = - \infty } ^ { \infty } b _ { n } e ^ { 2 \pi i n z / p } .
$$

The integrals for $b _ { n }$ become

$$
b _ { n } = { \frac { 1 } { 2 \pi i } } \int _ { z _ { 0 } } ^ { z _ { 0 } + p } f ( z ) e ^ { - ( n + 1 ) ( 2 \pi i z / p ) } \cdot { \frac { 2 \pi i } { p } } e ^ { 2 \pi i z / p } d z
$$

This is identical to (12.3.9).

THEOREM 12.3.2．Let

$$
f ( z ) = \sum _ { n = - \infty } ^ { \infty } a _ { n } e ^ { 2 \pi i n z / p }
$$

where

$$
\operatorname* { l i m } _ { n  + \infty } \operatorname* { s u p } { \frac { 1 } { 2 \pi n } } \log | a _ { n } | = A
$$

$$
\operatorname* { l i m } _ { n  + \infty } \operatorname* { i n f } { \frac { 1 } { 2 \pi n } } \log | a _ { - n } | = B
$$

and

$$
- \infty \leq A < B \leq \infty .
$$

Then $f ( z )$ is analytic and periodic in the strip $A < \operatorname { I m } \left( { \frac { z } { p } } \right) < B$ but is analytic in no larger strip $A < \mathrm { I m } \left( \frac { z } { p } \right) < B _ { 1 }$ or $A _ { 1 } < \operatorname { I m } \left( { \frac { z } { p } } \right) < B$ $A _ { 1 } < A , B _ { 1 } > B$

Proof: Consider the series $\sum _ { n = 0 } ^ { \infty } a _ { n } w ^ { n } + \sum _ { n = 1 } ^ { \infty } a _ { - n } w ^ { - n } \equiv g _ { 1 } ( w ) + g _ { 2 } ( w )$ The radius of convergence $\pmb { r _ { 1 } }$ of ${ \pmb g } _ { \bf 1 }$ is given by (Theorem 1.9.4)

$$
{ \frac { 1 } { r _ { 1 } } } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } | a _ { n } | ^ { 1 / n } = e ^ { 2 \pi A } .
$$

The radius of convergence $\pmb { r _ { 2 } }$ of ${ \pmb g } _ { \pmb 2 }$ is

$$
r _ { 2 } = \operatorname* { l i m } _ { n  \infty } \operatorname* { s u p } | a _ { - n } | ^ { 1 / n } = e ^ { - 2 \pi B } .
$$

Since $A < B$ ， $g _ { 1 } + g _ { 2 }$ is regular in the annulus $e ^ { - 2 \pi B } < | w | < e ^ { - 2 \pi A }$ and cannot be continued analytically into a larger annulus over either the inner or outer circle. Applying (12.3.10), $f ( z )$ is analytic in the strip

$$
A < \mathrm { I m } ~ ( z / p ) < B ,
$$

but in no larger strip.

Ex.1．Let $0 ~ < r < 1$

$$
\frac { 1 } { 1 - r w } = \sum _ { k = 0 } ^ { \infty } r ^ { k } w ^ { k } \quad \mathrm { f o r } \quad | r w | < 1 .
$$

Hence

$$
{ \frac { 1 } { 1 \ - \ r e ^ { i z } } } = \sum _ { k = 0 } ^ { \infty } r ^ { k } e ^ { i k z } \quad { \mathrm { f o r } } \quad \left| r e ^ { i z } \right| < 1 , \quad { \mathrm { i . e . , ~ f o r } } \quad { \mathrm { I m } } \ z > \log r .
$$

Similarly

$$
\frac { 1 } { 1 - r e ^ { - i z } } = \sum _ { k = 0 } ^ { \infty } r ^ { k } e ^ { - i k z } \mathrm { \quad } \mathrm { f o r \quad } \mathrm { I m } z < - \mathrm { l o g } r .
$$

Adding,

$$
{ \frac { 1 - r ^ { 2 } } { 1 + r ^ { 2 } - 2 r \cos z } } = { \frac { 1 } { 1 - r e ^ { i z } } } + { \frac { 1 } { 1 - r e ^ { - i z } } } - 1 = 1 + 2 \sum _ { k = 1 } ^ { \infty } r ^ { k } \cos k z
$$

convergent uniformly and absolutely for $\log r < \mathbf { I m } z < - \log r$ This is the Poisson kernel of Potential Theory.

Ex.2. C $\cot z = { \frac { \cos z } { \sin z } } = i \cdot { \frac { e ^ { 2 i z } + 1 } { e ^ { 2 i z } - 1 } }$ The only singularities are on the real axis,and hence we anticipate two Fourier expansions,one valid in $\mathbf { I m } z > 0$ and the other in ${ \bf { I m } } z < 0$ .For instance,

${ \frac { 1 } { 2 } } ( i \cot z - 1 ) = { \frac { e ^ { 2 i z } } { 1 - e ^ { 2 i z } } } = \sum _ { k = 1 } ^ { \infty } e ^ { 2 i k z }$ valid for $| e ^ { 2 i z } | < 1$ ,ie.,for $\mathbf { I m } z > 0$

# 12.4 Convergence of the Legendre Series for Analytic Functions.

In this section, $P _ { n }$ designates the Legendre polynomials standardized by $P _ { n } ( 1 ) = 1$

LEMMA 12.4.1. Let $w = \frac { 1 } { 2 } ( z + z ^ { - 1 } )$ ; then,

$$
P _ { n } ( w ) = \sum _ { j = 0 } ^ { n } a _ { j } a _ { n - j } z ^ { n - 2 j } ; \quad a _ { j } = \frac { ( 2 j ) ! } { ( j ! ) ^ { 2 } 2 ^ { 2 j } } .
$$

Proof: From the generating identity (l0.3.22) we have

$$
{ \frac { 1 } { \sqrt { 1 - 2 w t + t ^ { 2 } } } } = \sum _ { n = 0 } ^ { \infty } P _ { n } ( w ) t ^ { n } .
$$

Now $( 1 - t z ) ^ { - \frac { 1 } { 2 } } ( 1 - t / z ) ^ { - \frac { 1 } { 2 } } = ( 1 - 2 w t + t ^ { 2 } ) ^ { - \frac { 1 } { 2 } }$ . Moreover,

$$
( 1 - t z ) ^ { - \frac { 1 } { 2 } } = \sum _ { n = 0 } ^ { \infty } a _ { n } t ^ { n } z ^ { n } , ~ ( 1 - t / z ) ^ { - \frac { 1 } { 2 } } = \sum _ { n = 0 } ^ { \infty } a _ { n } \frac { t ^ { n } } { z ^ { n } } .
$$

Hence,

$$
( 1 - 2 w t + t ^ { 2 } ) ^ { - \frac { 1 } { 2 } } = \sum _ { j , k = 0 } ^ { \infty } a _ { j } a _ { k } t ^ { j + k } z ^ { k - j } = \sum _ { n = 0 } ^ { \infty } t ^ { n } \sum _ { j = 0 } ^ { n } a _ { j } a _ { n - j } z ^ { n - 2 j } .
$$

Comparing coefficients, we obtain (12.4.1).

$$
| P _ { n } ( x ) | \leq 1 , \qquad - 1 \leq x \leq 1 .
$$

Proof: Set $z = e ^ { i \theta }$ ，then $w = \cos \theta$ .Hence, $P _ { n } ( \cos \theta ) = \sum _ { j = 0 } ^ { n } a _ { j } a _ { n - j } e ^ { i ( n - 2 j ) \theta } .$ Therefore, $| P _ { n } ( \cos \theta ) | \leq \sum _ { j = 0 } ^ { n } a _ { j } a _ { n - j } = P _ { n } ( \cos 0 ) = P _ { n } ( 1 ) = 1 \qquad $

LEMMA 12.4.3. The quantities ${ \pmb a } _ { j }$ defined by (12.4.1) are positive and decreasing. The quantities an--lare positive and increase with j. Moreover,

$$
\operatorname* { l i m } _ { n \to \infty } \sqrt { \overline { { \pi n } } } a _ { n } = 1 .
$$

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n - j } } { a _ { n } } } = 1 , \quad { \mathrm { f o r ~ } } j { \mathrm { ~ f i x e d } } ,
$$

$$
a _ { j } a _ { n - j } \leq a _ { n } , \qquad j = 0 , 1 , 2 , \ldots , n .
$$

Proof: (12.4.3) and (12.4.4) are proved by Stirling's formula. The remaining statements are clear from inspecting the formula

$$
a _ { 0 } = 1 , ~ a _ { n } = \frac { 1 \cdot 3 \cdot \cdot \cdot 2 n - 1 } { 2 \cdot 4 \cdot \cdot \cdot 2 n } .
$$

LEMMA 12.4.4. Let

$$
R _ { n } ( z ) = \sum _ { j = 0 } ^ { n } \bigg ( \frac { a _ { n - j } } { a _ { n } } - 1 \bigg ) a _ { j } z ^ { - 2 j } .
$$

Then

$$
\operatorname* { l i m } _ { n \to \infty } R _ { n } ( z ) = 0
$$

uniformly in the exterior of every circle $| z | \geq \rho > 1$

Prof: Given an $\varepsilon > 0$ Seleet $N = N ( \varepsilon )$ so large that $\sum _ { i = 1 } ^ { \infty } \rho ^ { - 2 i } < \varepsilon . \mathrm { ~ N ~ }$ ow, j=

$$
R _ { n } ( z ) = \sum _ { j = 0 } ^ { N } \bigg ( \frac { a _ { n - j } } { a _ { n } } - 1 \bigg ) a _ { j } z ^ { - 2 j } + \sum _ { N + 1 } ^ { n } \bigg ( \frac { a _ { n - j } } { a _ { n } } - 1 \bigg ) a _ { j } z ^ { - 2 j } .
$$

We have

$$
\begin{array} { r l } {  { \Big \vert \sum _ { j = 0 } ^ { N } \Big ( \frac { a _ { n - j } } { a _ { n } } - 1 \Big ) a _ { j } z ^ { - 2 j } \Big \vert \leq \sum _ { j = 0 } ^ { N } \Big ( \frac { a _ { n - j } } { a _ { n } } - 1 \Big ) a _ { j } \vert z ^ { - 2 j } \vert } } \\ & { \le \Big ( \frac { a _ { n - N } } { a _ { n } } - 1 \Big ) \sum _ { j = 0 } ^ { N } a _ { j } \vert z ^ { - 2 j } \vert \le \Big ( \frac { a _ { n - N } } { a _ { n } } - 1 \Big ) \sum _ { j = 0 } ^ { \infty } a _ { j } \vert z ^ { - 2 j } \vert } \\ & { = \Big ( \frac { a _ { n - N } } { a _ { n } } - 1 \Big ) \frac { \vert z \vert } { \sqrt { \vert z \vert ^ { 2 } - 1 } } \le \Big ( \frac { a _ { n - N } } { a _ { n } } - 1 \Big ) \frac \rho { \sqrt { \rho ^ { 2 } - 1 } } . } \end{array}
$$

The second inequality here is due to the fact that an-i_l increases with j. an The last follows since $r / \sqrt { r ^ { 2 } - 1 }$ is decreasing for $r > 1$ .Again, since

$$
0 \leq \bigg ( \frac { a _ { n - j } } { a _ { n } } - 1 \bigg ) a _ { j } \leq \frac { a _ { n - j } a _ { j } } { a _ { n } } \leq 1 ,
$$

$$
\biggl | \sum _ { N + 1 } ^ { n } \biggl ( \frac { a _ { n - j } } { a _ { n } } - 1 \biggr ) a _ { j } z ^ { - 2 j } \biggr | \leq \sum _ { N + 1 } ^ { n } | z | ^ { - 2 j } \leq \sum _ { N + 1 } ^ { \infty } | z | ^ { - 2 j } .
$$

Thus, for $| z | \geq \rho > 1$ ，

$$
| R _ { n } ( z ) | \leq \left( \frac { a _ { n - N } } { a _ { n } } - 1 \right) \frac { \rho } { \sqrt { \rho ^ { 2 } - 1 } } + \varepsilon .
$$

Now since αn-N=1, we can find an N1=N(N,ε) such that Qn-N-1≤εfor alln ≥ N1. Thus,for alln ≥N1,and for all| ≥ρ>1, $| R _ { n } ( z ) | \leq \varepsilon ( 1 + \rho ( \rho ^ { 2 } - 1 ) ^ { - \frac { 1 } { 2 } } )$ . (12.4.7) follows from this inequality.

THEOREM 12.4.5 (Laplace-Heine). Let $w = \frac { 1 } { 2 } ( z + z ^ { - 1 } )$ . (Cf. 1.13.) Then,

$$
\operatorname * { l i m } _ { n  \infty } \frac { \sqrt { \pi n } ( 1 - z ^ { - 2 } ) ^ { \frac { 1 } { 2 } } P _ { n } ( w ) } { z ^ { n } } = 1 ,
$$

uniformly in $| z | \geq \rho > 1$ ,and

$$
\operatorname * { l i m } _ { n  \infty } \frac { \sqrt { 2 \pi n } ( w ^ { 2 } - 1 ) ^ { \frac { 1 } { 4 } } P _ { n } ( w ) } { ( w + \sqrt { w ^ { 2 } - 1 } ) ^ { n + \frac { 1 } { 2 } } } = 1
$$

uniformly in the exterior of any region that contains $- 1 \leq w \leq 1$ . Furthermore,

$$
\operatorname* { l i m } _ { n \to \infty } | P _ { n } ( z ) | ^ { 1 / n } = \rho , \quad z \in \mathcal { E } _ { \rho } ,
$$

and uniformly on all $\mathcal { E } _ { \rho } , \rho \ge \rho ^ { \prime } > 1$

Proof: ${ \frac { P _ { n } ( w ) } { a _ { n } z ^ { n } } } = \sum _ { j = 0 } ^ { n } { \frac { a _ { j } a _ { n - j } } { a _ { n } } } z ^ { - 2 j } . \quad { \mathrm { H e n c e } } , \quad { \frac { P _ { n } ( w ) } { a _ { n } z ^ { n } } } - \sum _ { j = 0 } ^ { n } a _ { j } z ^ { - 2 j } = R _ { n } ( z ) .$ By   
(12.4.2) we have $\sum _ { = 0 } ^ { n } a _ { j } z ^ { - 2 j } \to ( 1 - z ^ { - 2 } ) ^ { - \frac { 1 } { 2 } }$ and $R _ { n } ( z ) \to 0$ ， both uniformly in j   
any $| z | \geq \rho > 1$ . Therefore

$$
\frac { P _ { n } ( w ) } { a _ { n } z ^ { n } }  ( 1 - z ^ { - 2 } ) ^ { - \frac { 1 } { 2 } }
$$

uniformly. Since $\sqrt { n \pi } a _ { n } \to 1$ ，(12.4.8）follows.Now with appropriate

interpretations of the square root,a simple calculation shows that $( { \bf l } - z ^ { - 2 } ) =$ $\frac { 2 \sqrt { w ^ { 2 } - 1 } } { w + \sqrt { w ^ { 2 } - 1 } } \mathfrak { a }$ nd (12.4.10) follows from (12.4.8).

Finally,

$$
\frac { \sqrt { \pi n } \left| ( 1 - z ^ { - 2 } ) ^ { \frac { 1 } { 2 } } \right| \left| P _ { n } ( w ) \right| } { | z | ^ { n } } = 1 + \varepsilon _ { n } ( z )
$$

where $\varepsilon _ { n } ( z ) \to 0$ uniformly in $| z | \geq \rho > 1$ . Thus，also $( 1 + \varepsilon _ { n } ( z ) ) ^ { 1 / n } \to 1$ uniformly there.Extracting the nth root of both sides of (12.4.1l) we obtain

$$
\operatorname* { l i m } _ { n  \infty } | P _ { n } ( w ) | ^ { 1 / n } = | z |
$$

uniformly in $| z | \geq \rho > 1$ ,and this is equivalent to (12.4.10).

LEMMA 12.4.6．If

$$
Q _ { n } ( z ) = \mathfrak { f } \int _ { - 1 } ^ { + 1 } \frac { P _ { n } ( t ) } { z - t } d t , n = 0 , 1 , 2 , . . . ,
$$

and $w = \frac { 1 } { 2 } ( z + z ^ { - 1 } )$ ,then

$$
Q _ { n } ( w ) = \sum _ { k = n + 1 } ^ { \infty } \frac { \sigma _ { n k } } { z ^ { k } }
$$

where

$$
| \sigma _ { n k } | \leq \pi \qquad n = 0 , 1 , 2 , \ldots ; k = n + 1 , n + 2 , \ldots .
$$

The function $Q _ { n } ( z )$ is known as the Legendre function of the second kind.It is also a solution of the differential equation (lo.3.l4) with $\alpha = \beta = 0$ ，but is linearly independent of $\smash { P _ { n } ( z ) }$ .The integral (12.4.l3) defines $Q _ { n } ( z )$ asa single valued function for all $\boldsymbol { z }$ in the plane with $- 1 \le z \le 1$ deleted. Actually $Q _ { n } ( z )$ may be continued analytically to the whole finite plane save at $- 1 , + 1$ as a multivalued function,but we shall not need this continuation.

Prof: From (12.4.13) we have $Q _ { n } ( w ) = z \int _ { - 1 } ^ { + 1 } \frac { P _ { n } ( t ) } { z ^ { 2 } - 2 z t + 1 } d t$ and seting

$$
t = \cos \theta , Q _ { n } ( w ) = \frac { 1 } { 2 } \int _ { 0 } ^ { \pi } \frac { P _ { n } ( \cos \theta ) \sin \theta d \theta } { 1 - \displaystyle \frac { 2 \cos \theta } { z } + \displaystyle \frac { 1 } { z ^ { 2 } } } .
$$

Now

$$
{ \begin{array} { r } { { \frac { \sin \theta } { z } } \left\{ { \cfrac { 1 } { 1 - { \cfrac { 2 \cos \theta } { z } } + { \cfrac { 1 } { z ^ { 2 } } } } } \right\} = { \frac { 1 } { 2 i } } \left\{ { \cfrac { { \frac { e ^ { i \theta } } { z } } } { 1 - { \cfrac { e ^ { i \theta } } { z } } } } - { \cfrac { { \frac { e ^ { - i \theta } } { z } } } { 1 - { \cfrac { e ^ { - i \theta } } { z } } } } \right\} } \\ { = { \frac { 1 } { 2 i } } \sum _ { m = 1 } ^ { \infty } \left( { \frac { e ^ { i \theta } } { z } } \right) ^ { m } - \left( { \frac { e ^ { - i \theta } } { z } } \right) ^ { m } = \sum _ { m = 1 } ^ { \infty } { \cfrac { \sin m \theta } { z ^ { m } } } . } \end{array} }
$$

The last series converges uniformly and absolutely for $0 \leq \theta \leq \pi$ and for all

$$
| z | \geq \rho > 1 . { \mathrm { ~ H e n c e , ~ } } Q _ { n } ( w ) = \int _ { 0 } ^ { \pi } P _ { n } ( \cos \theta ) \sum _ { m = 1 } ^ { \infty } { \frac { \sin m \theta } { z ^ { m } } } = \sum _ { m = 1 } ^ { \infty } { \frac { \sigma _ { n m } } { z ^ { m } } }
$$

where

$$
\sigma _ { n m } = \int _ { 0 } ^ { \pi } P _ { n } ( \cos \theta ) \sin { m \theta } d \theta .
$$

Since by Corollary 12.4.2, $| P _ { n } ( \cos \theta ) | \le 1$ ， (12.4.15) follows. Again setting cos $\theta = t$ ,we have

$$
\sigma _ { n m } = \int _ { - 1 } ^ { + 1 } P _ { n } ( t ) \frac { \sin { ( m \cos ^ { - 1 } t ) } } { \sqrt { 1 - t ^ { 2 } } } d t .
$$

But $\frac { \sin { ( m \cos ^ { - 1 } t ) } } { \sqrt { 1 - t ^ { 2 } } } = U _ { m - 1 } ( t )$ is a polynomial of degree $m - 1$ . Hence， by orthogonality， for $m - 1 < n$ ,i.e.， for $m < n + 1$ ， ${ \pmb { \sigma } } _ { n m } = 0$ This establishes (12.4.14).

THEOREM 12.4.7 (K. Neumann). Let $f ( z )$ be analytic in the interior of $\mathcal { E } _ { \rho } , \rho > 1$ , but not in the interior of any $\pmb { \mathcal { E } } _ { \pmb { \rho } ^ { \prime } }$ with $\rho ^ { \prime } > \rho$ Then,

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } P _ { n } ( z )
$$

with

$$
a _ { n } = { \frac { 2 n + 1 } { 2 } } \int _ { - 1 } ^ { + 1 } f ( x ) P _ { n } ( x ) d x
$$

or

$$
a _ { n } = { \frac { 2 n + 1 } { 2 ^ { n + 1 } n ! } } \int _ { - 1 } ^ { + 1 } f ^ { ( n ) } ( x ) ( 1 - x ^ { 2 } ) ^ { n } d x .
$$

The series converges absolutely and uniformly on any closed set in the interior of $\mathbf { \mathcal { E } _ { \rho } }$ .The series diverges exterior to $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho }$ Moreover,

$$
\operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { 1 / n } = { \frac { 1 } { \rho } } .
$$

Conversely, let $\left\{ a _ { n } \right\}$ be $\pmb { a }$ sequence of constants satisfying (12.4.21) with $\rho > 1$ . Then the series (12.4.18) converges uniformly and absolutely on any closed set in the interior of $\mathbf { \delta } _ { \pmb { \phi } } ^ { \mathcal { S } } ,$ to $^ { \pmb { a } }$ function $f ( z )$ for which (12.4.18-20) holds. The series diverges outside $\mathbf { \delta } _ { \pmb { \phi } _ { \rho } } ^ { \mathcal { O } }$

Proof: Let $\left\{ a _ { n } \right\}$ be a sequence of constants for which lim sup $| a _ { n } | ^ { 1 / n } = { \frac { 1 } { \rho } } ;$ n→8   
$1 < \rho \le \infty$ .Then by Lemma4.4.2and (12.4.10)，theseries $\sum _ { \ i = 0 } ^ { \infty } a _ { n } P _ { n } ( z )$ 1

converges in the interior of $\mathbf { \delta } _ { \pmb { \mathscr { E } } _ { \pmb { \rho } } } ^ { \pmb { \mathscr { E } } } ,$ to an analytic function $f ( z )$ . The convergence is uniform inside every $\pmb { \mathcal { E } } _ { \pmb { \rho } ^ { \prime } }$ ， $\pmb { \rho } ^ { \prime } < \pmb { \rho }$ .The series diverges outside $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho }$ . We have,

$$
{ \frac { 2 k + 1 } { 2 } } \int _ { - 1 } ^ { + 1 } f ( x ) P _ { k } ( x ) d x = { \frac { 2 k + 1 } { 2 } } \sum _ { n = 0 } ^ { \infty } a _ { n } \int _ { - 1 } ^ { + 1 } P _ { n } ( x ) P _ { k } ( x ) d x = a _ { k } .
$$

This follows from uniform convergence,the orthogonality of the $\bar { P } _ { n } \mathrm { ^ { \circ } } { \mathrm { s } }$ and (10.3.13). The alternate expression (l2.4.20) is formed from (12.4.19) by using Rodrigues' formula and integrating by parts.

Suppose,conversely，that $f ( z )$ is analytic in the interior of $\mathcal { E } _ { \rho } , \ \rho > 1$ We will estimate the size of the constants

$$
a _ { n } = { \frac { 2 n + 1 } { 2 } } \int _ { - 1 } ^ { + 1 } f ( t ) P _ { n } ( t ) d t .
$$

Select a $\pmb { \rho } ^ { \prime }$ with $1 < \rho ^ { \prime } < \rho$ Then $f ( z )$ is analytic in and on $\pmb { \mathcal { E } } _ { \pmb { \rho } ^ { \prime } }$ .Hence we may write for $- 1 \leq t \leq 1$ ，

$$
f ( t ) = { \frac { 1 } { 2 \pi i } } \int _ { \mathcal { E } _ { \rho ^ { \prime } } } { \frac { f ( z ) } { z - t } } d z .
$$

Combining the two equations,

$$
\begin{array} { l } { { a _ { n } { } = { } \displaystyle { \frac { 2 n + 1 } { 4 \pi i } } \int _ { - 1 } ^ { 1 } P _ { n } ( t ) { \int _ { \mathcal { E } _ { \rho ^ { \prime } } } } \frac { f ( z ) } { z - t } d z d t } } \\ { { { } = { } \displaystyle { \frac { 2 n + 1 } { 2 \pi i } } \int _ { \mathcal { E } _ { \rho ^ { \prime } } } f ( z ) { \int _ { - 1 } ^ { + 1 } } \frac { P _ { n } ( t ) } { z - t } d t d z { } = { } \displaystyle { \frac { 2 n + 1 } { 2 \pi i } } \int _ { \mathcal { E } _ { \rho ^ { \prime } } } f ( z ) Q _ { n } ( z ) d z . } } \end{array}
$$

# Therefore

$$
| a _ { n } | \leq \frac { 2 n + 1 } { 2 \pi } L ( \mathcal { \bar { O } } _ { \rho ^ { \prime } } ) \operatorname* { m a x } _ { z \in \mathcal { \bar { E } } _ { \rho ^ { \prime } } } | f ( z ) | \operatorname* { m a x } _ { z \in \mathcal { \bar { E } } _ { \rho ^ { \prime } } } | Q _ { n } ( z ) |
$$

where $L ( \mathcal { E } _ { \rho ^ { \prime } } )$ designates the length of $\pmb { \mathcal { E } } _ { \pmb { \rho } ^ { \prime } }$ .Now from Lemma 12.4.6, $Q _ { n } ( z ) = \sum _ { k = n + 1 } ^ { \infty } { \frac { \sigma _ { n k } } { \nu ^ { k } } }$ where $z = \frac { 1 } { 2 } ( \nu + \nu ^ { - 1 } )$ As $_ z$ describes the ellipse $\pmb { \mathcal { E } } _ { \pmb { \rho } ^ { \prime } }$ describes the circle $| \nu | = \rho ^ { \prime }$ .Hence,from inequality (12.4.15),

$$
\operatorname* { m a x } _ { z \in \mathcal { E } _ { \rho ^ { \prime } } } | Q _ { n } ( z ) | \le \sum _ { k = n + 1 } ^ { \infty } \frac { \pi } { ( \rho ^ { \prime } ) ^ { k } } = \frac { \pi ( \rho ^ { \prime } ) ^ { - n } } { \rho ^ { \prime } - 1 } .
$$

Combining this with (12.4.25), $| a _ { n } | \leq c ( 2 n + 1 ) ( \rho ^ { \prime } ) ^ { - n }$ where $c$ is a constant that depsenditrarn $\pmb { \rho } ^ { \prime }$ bult notan $\pmb { n }$ Therefore li P $| a _ { n } | ^ { 1 / n } \leq \frac { 1 } { \rho ^ { \prime } }$ · Since is arbitrary,it follows that $\pmb { n }  \infty$

$$
\operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { 1 / n } \leq { \frac { 1 } { \rho } } .
$$

Aslightmodifcatiooftefstpartofthotelstt $\sum _ { n = 0 } ^ { \infty } a _ { n } P _ { n } ( z )$ converges absolutely and uniformly in the interior of $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho }$ . If now,

$$
\operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { 1 / n } > { \frac { 1 } { \rho } } ,
$$

then $\sum _ { n = 0 } ^ { \infty } a _ { n } P _ { n } ( z )$ would converge uniformly in the interior of a larger ellipse   
$\mathcal { E } _ { \rho ^ { \ast } } ^ { \prime } , \rho ^ { \prime \prime } > \rho$ ， and hence provide an analytic continuation of $f ( z )$ there.By   
hypothesis this is impossible,since $\mathcal { E } _ { p }$ is the largest ellipse in which $f ( z )$ is   
analytic.Hence we must have

$$
\operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { 1 / n } = { \frac { 1 } { \rho } } .
$$

12.5 Complex Orthogonal Expansions. Let $\pmb { B }$ be a region of the complex plane for which $L ^ { 2 } ( B )$ is a Hilbert space. (Cf. Theorem 9.2.10.)

LEMMA 12.5.1. Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be $^ { \pmb { a } }$ sequence of functions of class $L ^ { 2 } ( B )$ that are Orthonormal with respect t $\begin{array} { c } { { \displaystyle \left. \begin{array} { c } { { . } } \\ { { { \it o t h e \ i n n e r \ p r o d u c t } \ ( f , g ) = \displaystyle \iint _ { B } f \tilde { g } \ ^ { } + } } \\ { { \displaystyle \sum _ { n = 1 } ^ { \infty } | h _ { n } ^ { * } ( z ) | ^ { 2 } \le \displaystyle \frac { 1 } { \pi r ^ { 2 } ( z ) } \ : , } } \end{array} \right. } } \end{array}$ dx dy. Then,

where $z \in B$ and $r ( z )$ is the distance from $_ z$ to the boundary of $\pmb { B }$

Proof:For fixed $_ z$ ， $L ( f ) = f ( z )$ is a bounded linear functional over $L ^ { 2 } ( B )$ (cf.Ex.4,9.3).Consider the problem of minimizing $\| f \| ^ { 2 }$ from among those combinations $f = a _ { 1 } h _ { 1 } { * } + \cdot \cdot \cdot + a _ { n } h _ { n } { * }$ for which $f ( z ) = 1$ . By Theorem 9.4.3,the minimum value is

$$
\biggl ( \sum _ { i = 1 } ^ { n } | h _ { i } ^ { * } ( z ) | ^ { 2 } \biggr ) ^ { - 1 } .
$$

By (9.2.28), $\pi r ^ { 2 } ( z ) \cdot 1 \leq \| f \| ^ { 2 } = \left( \sum _ { i = 1 } ^ { n } | { h _ { i } } ^ { * } ( z ) | ^ { 2 } \right) ^ { - 1 }$ ，where $f$ is the minimizing function. Then, $\sum _ { i = 1 } ^ { n } | h _ { i } ^ { \ast } ( z ) | ^ { 2 } \leq \frac { 1 } { \pi r ^ { 2 } ( z ) }$ . This inequality is independent of $\pmb { n }$ and hence (12.5.1) follows.

THEOREM 12.5.2． Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be a complete orthonormal system for $L ^ { 2 } ( B )$ If the sequence of constants $\left\{ a _ { n } \right\}$ satisfies

the series

$$
\sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty ,
$$

$$
f ( z ) = \sum _ { n = 1 } ^ { \infty } a _ { n } h _ { n } { } ^ { * } ( z )
$$

converges absolutely and uniformly in every closed bounded set contained in $\pmb { B }$

to a function $f ( z )$ of class $L ^ { 2 } ( B )$ and for which

$$
a _ { n } = ( f , h _ { n } { * } ) , \qquad n = 1 , 2 , \ldots .
$$

Conversely, if $f ( z ) \in L ^ { 2 } ( B )$ and coe ffcients ${ \pmb a } _ { n }$ are defined by (12.5.4),then the series (12.5.3) converges to $f ( z )$ absolutely and uniformly in every closed bounded set contained in $\pmb { B }$

Proof: Assume (12.5.2). By the Schwarz inequality and (12.5.1),

$$
\sum _ { k = m } ^ { n } | a _ { k } h _ { k } { } ^ { * } ( z ) | \leq \left[ \sum _ { k = m } ^ { n } | a _ { k } | ^ { 2 } \right] ^ { \frac { 1 } { 2 } } \left[ \sum _ { k = m } ^ { n } | h _ { k } { } ^ { * } ( z ) | ^ { 2 } \right] ^ { \frac { 1 } { 2 } } \leq \left[ \sum _ { k = m } ^ { \infty } | a _ { k } | ^ { 2 } \right] ^ { \frac { 1 } { 2 } } \cdot { \frac { 1 } { \sqrt { \pi } r ( z ) } } \cdot
$$

Let $\pmb { B } ^ { \prime }$ designate a closed bounded set contained in $\pmb { B }$ ，Then there is a minimum distance $\pmb { r }$ from $\pmb { B ^ { \prime } }$ to the boundary of $\pmb { B }$ .Therefore,

$$
\sum _ { k = m } ^ { n } | a _ { k } h _ { k } { } ^ { * } ( z ) | \leq \frac { 1 } { \sqrt { \pi } r } \biggl [ \sum _ { k = m } ^ { \infty } | a _ { k } | ^ { 2 } \biggr ] ^ { \frac { 1 } { 2 } }
$$

throughout $\pmb { B ^ { \prime } }$ .In view of (12.5.1),for $\pmb { m }$ suffciently large the left-hand side can be made arbitrarily small uniformly for all $\pmb { n } > m$ and for all $z$ in $\pmb { B } ^ { \prime }$ .Therefore (l2.5.3) converges uniformly and absolutely to a function $f ( z )$ which must be analytic in $\pmb { B ^ { \prime } }$ Since $\pmb { B ^ { \prime } }$ is an arbitrary subregion of $B , f ( z )$ must be analytic in $\pmb { B }$

We must show that

$$
\begin{array} { r l r } {  { f ( z ) \in L ^ { 2 } ( B ) . \operatorname { S e t } f _ { n } ( z ) = \sum _ { k = 1 } ^ { n } a _ { k } { h _ { k } } ^ { * } ( z ) . \operatorname { T h e n } } } \\ & { } & { \| f _ { m } ( z ) - f _ { n } ( z ) \| ^ { 2 } = \sum _ { m } ^ { n } | a _ { k } | ^ { 2 } . \quad } \end{array}
$$

In view of (12.5.1), $\{ f _ { m } ( z ) \}$ is a Cauchy sequence and hence by the completeness of $L ^ { 2 } ( B )$ (Lemma 9.2.9) it converges in norm to a function $g ( z ) \in L ^ { 2 } ( B )$ But precisely as in the proof of Lemma 9.2.9,convergence in norm implies uniform convergence on closed bounded subregions of $\pmb { B }$ Hence $f _ { n } ( z ) \to g ( z )$ on $\pmb { B ^ { \prime } }$ .Therefore $f ( z ) \equiv g ( z )$ and is in $L ^ { 2 } ( B )$

Consider $( f , \ : h _ { k } { } ^ { * } ) - ( f _ { n } , \ : h _ { k } { } ^ { * } ) = ( f - f _ { n } , \ : h _ { k } { } ^ { * } )$ for $\pmb { n } \geq k$ . We have,

$$
| ( f , { h _ { k } } ^ { * } ) - ( f _ { n } , { h _ { k } } ^ { * } ) | ^ { 2 } \leq \| f - f _ { n } \| \| { h _ { k } } ^ { * } \| = \| f - f _ { n } \| .
$$

Since lim $\| f - f _ { n } \| = 0 , \ ( f _ { n } , { h _ { k } } ^ { * } ) \to ( f , { h _ { k } } ^ { * } )$ But for ${ \pmb n } \geq k$ we have by n-8   
orthogonality, $( f _ { n } , h _ { k } { } ^ { * } ) = a _ { k }$ Therefore, $a _ { k } = ( f , h _ { k } { ^ \ast } )$

Conversely, let $f ( z ) \in L ^ { 2 } ( B )$ . Define constants $a _ { k } = ( f , h _ { k } { ^ \ast } )$ .Since $\{ h _ { k } ^ { * } \}$ is closed,it follows from Theorem 8.9.1C that $\| f \| ^ { 2 } = \sum _ { k = 1 } ^ { \infty } | a _ { k } | ^ { 2 } < \infty$ Now, apply thefrst part of thepresenttheorem.The series $\sum _ { k = 1 } ^ { \infty } a _ { k } h _ { k } { ^ { * } } ( z )$ converges uniformly and absolutely to a function,call it $g ( z )$ ,which is in $L ^ { 2 } ( B )$ and for which $( g , h _ { k } { } ^ { * } ) = a _ { k } = ( f , h _ { k } { } ^ { * } )$ .Thus $( g - f , h _ { k } ^ { \ast } ) = 0$ k = 1,2,.... By Theorem 8.9.1, this implies that $g - f \equiv 0$

COROLLARY 12.5.3． Let $\pmb { B }$ be a bounded simply connected region whose boundary is C. Suppose that the complement of $B + C$ is a single region whose boundary is exactly $c$ Then, any $f \in L ^ { 2 } ( B )$ may be expanded in a series of orthogonal polynomials that is uniformly and absolutely convergent in closed subsets of $\pmb { B }$

Proof:Under these assumptions, the powers $1 , z , z ^ { 2 }$ 。...,are complete in $L ^ { 2 } ( B )$ ,and hence there is a coinplete orthonormal system of polynomials. (Cf. Theorem 11.4.8.)

Note the implication of Theorem 12.5.2.If $f ( z )$ is single valued and analytic in the closed region $\pmb { B }$ ,it may not necessarily possess a power series expansion that converges to $f$ in $\pmb { B }$ .But it can be expanded in a series of orthogonal functions that converge uniformly in arbitrary bounded subregions.

THEOREM 12.5.4.Let $\pmb { L }$ be a linear functional defined on $L ^ { 2 } ( B )$ and which is applicable term by term to series of analytic functions that converge uniformly in closed bounded subsets of $\pmb { B }$ Then $\scriptstyle { \cal L }$ is bounded over $L ^ { 2 } ( B )$

Pro0f: Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be a complete orthonormal sequence for $L ^ { 2 } ( B )$ .For any $f \in L ^ { 2 } ( B ) , f ( z ) = \sum _ { n = 1 } ^ { \infty } ( f , { h _ { n } } ^ { * } ) { h _ { n } } ^ { * } ( z )$ ,converging uniformly in every closed bounded subset of $\pmb { B }$ Hence for all $f \in L ^ { 2 } ( B )$ ， $\textit { L } ( f ) { = } \sum _ { n = 1 } ^ { \infty } ( f , h _ { n } { ^ { * } } ) L ( h _ { n } { ^ { * } } )$ The proof is completed by application of Theorem 9.3.8.

COROLLARY 12.5.5. The following linear functionals are bounded over $L ^ { 2 } ( B )$

(1) $L ( f ) = f ^ { ( n ) } ( z _ { 0 } )$ ， $\pmb { n = 0 }$ ,l,..., where ${ z _ { 0 } }$ is a point of $\pmb { B }$ (2) $L ( f ) = \int _ { C } w ( z ) f ( z ) d z$ where $\boldsymbol { c }$ is $^ { \pmb { a } }$ rectifable arc lying in $\pmb { B }$ and $w ( z )$ is continuous.

(3) L)f()f(xyer $\pmb { G }$ is a cosed rgion ontiredin $\pmb { B }$ and G $w ( z )$ is continuous there.

Proof:Each of these linear functionals can be applied term by term to uniformly convergent series of analytic functions in $\pmb { B }$

Ex.1．Any finite linear combination of linear functionals mentioned above is bounded over $L ^ { 2 } ( B )$

12.6 Reproducing Kernel Functions. Let $\boldsymbol { s }$ designate a point set lying in the space of one or more real or complex variables.We shall designate points of $\pmb { S }$ by $P , Q , \dots$ ，etc. $\pmb { X }$ will denote a complete inner product space of functions defined on $\pmb { S }$

DEFINITIoN l2.6.1． A function of two variables $\pmb { P }$ and $Q$ in $ { \boldsymbol { S } } ,  { \boldsymbol { K } } (  { \boldsymbol { P } } ,  { \boldsymbol { Q } } )$ ， is called $\pmb { a }$ reproducing kernel function for the space $\pmb { X }$ if

(a) For each fixed $Q \in { \mathcal { S } } , K ( P , Q )$ ,considered as a function of $\pmb { P }$ is in $\pmb { X }$ (b) For every function $f ( P ) \in X$ and for every point $Q \in { \mathcal { S } }$ ,the reproducing property

$$
f ( Q ) = ( f ( P ) , K ( P , Q ) ) _ { P }
$$

holds.The subscript outside the last parenthesis (which will be frequently omitted) indicates that $Q$ is held constant and the inner product is formed on the variable $\pmb { P }$

THEOREM l2.6.l (Aronszajn). A necessary and sufficient condition that $\pmb { X }$ have $\pmb { a }$ reproducing kernel function is that for each fixed $Q \in { \mathcal { S } }$ ，the linear functional

$$
L ( f ) = f ( Q )
$$

be bounded:

$$
| L ( f ) | \leq c _ { Q } \parallel f \parallel
$$

for some constant $c _ { Q }$ and for all $f \in X$

Proof: Suppose first that $\pmb { K } ( P , Q )$ is a reproducing kernel. Then,

$$
f ( Q ) = ( f ( P ) , K ( P , Q ) ) _ { P } .
$$

By the Schwarz inequality,

$$
\begin{array} { r l } & { | f ( Q ) | ^ { 2 } \leq ( f ( P ) , f ( P ) ) ( K ( P , Q ) , K ( P , Q ) ) _ { P } } \\ & { \qquad = \| f \| ^ { 2 } K ( Q , Q ) . } \end{array}
$$

The last identity follows by the reproducing property of $\pmb { \kappa }$ .Hence (12.6.3) holds with $c _ { Q } = \sqrt { { \bf K } ( Q , Q ) }$

Suppose,conversely,that (l2.6.3) holds for each fixed $Q$ .By Theorem 9.3.3,we can find a function $g ( P ) = g _ { Q } ( P ) \in X$ such that

$$
f ( Q ) = L ( f ) = ( f ( P ) , g _ { Q } ( P ) ) .
$$

Now set $K ( P , Q ) = g _ { Q } ( P )$ and it is clear that $\pmb { \kappa }$ is a reproducing kernel.

THEOREM 12.6.2．If $\pmb { X }$ possesses $\pmb { a }$ reproducing kernel,the kernel is unique.

Proof: Suppose we have two reproducing kernels ${ \cal K } ( P , Q ) , { \cal J } ( P , Q )$ Let $Q$ be fixed; then

$$
\begin{array} { r l } & { \| K ( P , Q ) - J ( P , Q ) \| ^ { 2 } = ( K ( P , Q ) - J ( P , Q ) , K ( P , Q ) - J ( P , Q ) ) _ { P } } \\ & { \qquad = ( K ( P , Q ) - J ( P , Q ) , K ( P , Q ) ) _ { P } - ( K ( P , Q ) } \\ & { \qquad - J ( P , Q ) , J ( P , Q ) ) _ { P } . } \end{array}
$$

Since $\pmb { K }$ and $\pmb { J }$ are both reproducing kernels,each of the two inner products is equal to $K ( Q , Q ) \_ J ( Q , Q )$ .Hence $\| K ( P , Q ) - J ( P , Q ) \| ^ { 2 } = 0$ and hence $K ( P , Q ) = J ( P , Q )$ for all $\pmb { P }$ Since $Q$ is arbitrary,it holds for all $P$ and $Q$

THEOREM 12.6.3．If $\pmb { X }$ possesses a reproducing kernel $K ( P , Q )$ then

$$
K ( R , Q ) = { \overline { { K ( Q , R ) } } } .
$$

Proof: Let $P , Q$ and $\pmb { R }$ be three points in $\pmb { S }$ ，Then, by the reproducing property,

$$
( K ( P , Q ) , K ( P , R ) ) _ { P } = K ( R , Q ) .
$$

Similarly,

$$
( K ( P , R ) , K ( P , Q ) ) _ { P } = K ( Q , R ) .
$$

But by the Hermitian symmetry of the inner product,the left-hand sides must be complex conjugate quantities.

If $\pmb { X }$ has a reproducing kernel, then convergence in norm implies pointwise convergence.More precisely,

THEOREM 12.6.4. Let $\pmb { X }$ have a reproducing kernel and let lim $\| f - f _ { n } \| = 0$ Then,for each $\pmb { P } \in \pmb { S }$ ， n→8

$$
\operatorname* { l i m } _ { n \to \infty } f _ { n } ( P ) = f ( P ) .
$$

The convergence holds uniformly in every subset $s ^ { \prime }$ of $\pmb { S }$ over which $K ( Q , Q )$ is bounded.

$$
\begin{array} { r l } & { | f ( Q ) - f _ { n } ( Q ) | ^ { 2 } = | ( f ( P ) - f _ { n } ( P ) , K ( P , Q ) ) _ { P } | ^ { 2 } } \\ & { \qquad \le \| f - f _ { n } \| ^ { 2 } ( K ( P , Q ) , K ( P , Q ) ) _ { P } } \\ & { \qquad = \| f - f _ { n } \| ^ { 2 } K ( Q , Q ) \le \| f - f _ { n } \| ^ { 2 } M } \end{array}
$$

where $M$ is a bound for $\kappa ( Q , Q )$ in $s ^ { \prime }$ . The theorem follows by allowing $n \to \infty$

COROLLARY 12.6.5．If $\pmb { X }$ has $\pmb { a }$ reproducing kernel, then the Fourier expansion of $^ { \pmb { a } }$ function in a complete orthonormal system converges pointwise to the function and uniformly over subsets of $\boldsymbol { s }$ for which $K ( Q , Q )$ is bounded.

Proof: Theorem 8.9.1(b).

If $\pmb { X }$ has a reproducing kernel, the representer of a bounded linear functional has a very simple expression.

THEOREM 12.6.6．Let $\pmb { X }$ have a reproducing kernel $\pmb { K } ( P , Q )$ ，and let $\pmb { L }$ be a bounded linear functional defined on $\pmb { X }$ .Then the function

$$
h ( Q ) = \overline { { L _ { P } K ( P , Q ) } }
$$

is in $\pmb { X }$ and for all $f \in X$ ，

$$
L ( f ) = ( f ( Q ) , h ( Q ) ) .
$$

(The subscript in $L _ { P }$ indicates that $Q$ is held fixed and $L$ is applied to $K ( P , Q )$ as a function of $\pmb { P }$ ）

Proof:By Theorem 9.3.3,there is an $\pmb { h } ( P ) \in \pmb { X }$ such that $L ( f ) = ( f , h )$ for all $f \in X$ .Hence,

$$
\overline { { { { \cal L } _ { P } K ( P , Q ) } } } = \overline { { { ( K ( P , Q ) , h ( P ) ) _ { P } } } } = ( h ( P ) , K ( P , Q ) ) _ { P } = h ( Q ) .
$$

COROLLARY 12.6.7.

$$
\| L \| ^ { 2 } = L _ { Q } { \overline { { L _ { P } K ( P , Q ) } } } .
$$

Proof: From Corollary 9.3.4 we have,

$$
\| L \| ^ { 2 } = ( h ( Q ) , h ( Q ) ) = L _ { Q } ( h ( Q ) ) = L _ { Q } { \widehat { L _ { P } K ( P , Q ) } } .
$$

Ex.1.Let ${ \mathcal { P } } _ { n }$ be an inner product space of real or complex polynomials of degree $\leq n$ as in lo.l or 1o.2.The linear functional $L ( f ) = f ( z _ { 0 } )$ is bounded. (Ex.l0,l0.2.）The kernel polynomial is a reproducing kernel for $\mathcal { P } _ { n }$ .(Theorem 10.1.5.)

Ex.2.Let $\pmb { B }$ be a region of the complex plane.If $z \in B$ ，then $L ( f ) = f ( z )$ is a bounded linear functional over $L ^ { 2 } ( B )$ $\mathbf { \vec { E } x }$ .4,9.3).Hence by Lemma 9.2.9 and Theorem 12.6.1, $L ^ { 2 } ( B )$ has a reproducing kernel. If $L ^ { 2 } ( B )$ is a Hilbert space and if $\{ h _ { n } { } ^ { * } ( z ) \}$ is a complete orthonormal sequence,the reproducing kernel has the representation

$$
K ( z , w ) = \sum _ { n = 1 } ^ { \infty } h _ { n } { ^ { * } } ( z ) \overline { { h _ { n } { ^ { * } } ( w ) } } .
$$

$K ( z , w )$ is known as the Bergman kernel for the region $\textbf {  { B } }$ . This representation rests upon the following theorems.

THEOREM 12.6.8． Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be $\pmb { a }$ complete orthonormal system in $L ^ { 2 } ( B )$ For fixed $w \in \mathcal Ḋ B Ḍ$ ，the series (12.6.l3) converges uniformly and absolutely in every closed bounded subregion $B ^ { \prime }$ contained in $\pmb { B }$ The sum is analytic in $z \in B$ and of class $L ^ { 2 } ( B )$ . Furthermore, $( K ( z , w ) , \ : h _ { k } { ^ \ast ( z ) } ) _ { z } = \overline { { h _ { k } { ^ \ast ( w ) } } }$

Proof:By Lemma 12.5.1, $\sum _ { n = 1 } ^ { \infty } | h _ { n } \ast ( w ) | ^ { 2 } < \infty$ 、The theorem now follows   
by applying Theorem 12.5.2.

THEOREM 12.6.9．Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be $\pmb { a }$ complete orthonormal system for $L ^ { 2 } ( B )$ Then (12.6.13) is $\pmb { a }$ (and hence the) reproducing kernel for $L ^ { 2 } ( B )$ ; that is, for all $f ( z ) \in L ^ { 2 } ( B )$ we have

$$
f ( w ) = ( f ( z ) , K ( z , w ) ) _ { z } = \int _ { \cal B } \int f ( z ) \ { \overline { { K ( z , w ) } } } \ d x \ d y .
$$

Proof: Since $f \in L ^ { 2 } ( B )$ ， $f ( z ) = \sum _ { k = 1 } ^ { \infty } ( f , { h _ { k } } ^ { * } ) { h _ { k } } ^ { * } ( z )$ Now from Theorem 12.6.8, $( K ( z , w ) , \ : h _ { k } { ^ \ast ( z ) ) } _ { z } = \overline { { h _ { k } { ^ \ast ( w ) } } }$ From Theorem $8 . 9 . 1 ( \mathrm { C ^ { \prime } } )$ ，

$$
\left( f ( z ) , K ( z , w ) \right) _ { z } = \sum _ { k = 1 } ^ { \infty } \left( f , h _ { k } { } ^ { * } \right) \left( h _ { k } { } ^ { * } ( z ) , K ( z , w ) \right) _ { z } = \sum _ { k = 1 } ^ { \infty } \left( f , h _ { k } { } ^ { * } \right) h _ { k } { } ^ { * } ( w ) = f ( w ) .
$$

COROLLARY 12.6.10． Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be $^ { \pmb { a } }$ complete orthonormal sequence for $L ^ { 2 } ( B )$ . Suppose that $L$ is $^ { \pmb { a } }$ bounded linear functional defined on $L ^ { 2 } ( B )$ . Then

$$
h ( w ) = \sum _ { n = 1 } ^ { \infty } h _ { n } { } ^ { * } ( w ) \overline { { L ( h _ { n } { } ^ { * } ( z ) ) } }
$$

is the representer of $\pmb { L }$ and

$$
\| L \| ^ { 2 } = \sum _ { n = 1 } ^ { \infty } | L ( { h _ { n } } ^ { * } ( z ) ) | ^ { 2 } = L _ { w } \overline { { L _ { z } K ( z , w ) } } .
$$

Proof:Use Theorems 9.3.5 and 12.6.9.

Ex.3. Let $B$ designate the circle $| z | < 1$ . The functious

$$
\sqrt { \frac { n + 1 } { \pi } } z ^ { n } \quad ( n = 0 , 1 , 2 , . . . )
$$

are complete and orthonormal in $L ^ { 2 } ( B )$ .Hence the reproducing kernel for $L ^ { 2 } ( B )$ is

$$
K ( z , w ) = \sum _ { n = 0 } ^ { \infty } \frac { n + 1 } { \pi } z ^ { n } \bar { w } ^ { n } = \frac { 1 } { \pi ( 1 - z \bar { w } ) ^ { 2 } } .
$$

Ex. 4. Consider an ellipse ${ \pmb { \mathscr { E } } } _ { \pmb { \rho } }$ (Definition 1.13.1). Designate its inside by $\hat { \pmb { \mathscr { E } } } _ { \pmb { \rho } }$ As we have seen in Ex.4,1o.2,the polynomials

$$
{ p _ { n } } ^ { * } ( z ) = 2 \sqrt { \frac { n + 1 } { \pi } } ( \rho ^ { 2 n + 2 } - \rho ^ { - 2 n - 2 } ) ^ { - \frac { 1 } { 2 } } U _ { n } ( z ) ,
$$

$$
U _ { n } ( z ) = ( 1 - z ^ { 2 } ) ^ { - \frac { 1 } { 2 } } \sin { [ ( n + 1 ) \operatorname { a r c } \cos z ] }
$$

are orthonormal for $L ^ { 2 } ( \hat { \pmb \sigma } _ { \pmb \rho } )$ . They are also complete (Theorem 11.4.8). Hence the reproducing kernel for $L ^ { 2 } ( \hat { \pmb \sigma } _ { \rho } )$ is

$$
K ( z , w ) = \frac { 4 } { \pi } \sum _ { n = 0 } ^ { \infty } ( n + 1 ) \frac { U _ { n } ( z ) \overline { { { U _ { n } ( w ) } } } } { \rho ^ { 2 n + 2 } - \rho ^ { - 2 n - 2 } } .
$$

Ex.5.Let ${ \pmb z } _ { \pmb 0 }$ be interior to $B \colon \left| z \right| < 1$ .If $z _ { \mathbf { 0 } } \in B$ ,the linear functional

$$
L ( f ) = f ^ { ( j ) } ( z _ { 0 } ) \qquad j , \mathrm { i n t e g e r } \geq 0 ,
$$

is bounded over $L ^ { 2 } ( B )$ .(Ex.4,9.3.) Its representer $g ( w )$ is given by

$$
\overline { { { g ( w ) } } } = \frac { d ^ { ( j ) } } { d z ^ { ( j ) } } \frac { 1 } { \pi ( 1 - z \bar { w } ) ^ { 2 } } \bigg | _ { z = z _ { 0 } } = \frac { ( - 1 ) ^ { j } ( j + 1 ) ! \bar { w } ^ { j } } { \pi ( 1 - z _ { 0 } \bar { w } ) ^ { j + 2 } } .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/32179b9f1c3ce90fefadf44295a69eb1031b920b49db3415461960219c61ed96.jpg)  
igre $K ( x , x ) = { \frac { 1 } { \pi ( 1 - x ^ { 2 } ) ^ { 2 } } }$

In particular, the conjugate representer for $L ( f ) = f ( z _ { 0 } )$ is n(1-200）2. It8 norm is $\| L \| ^ { 2 } = { \frac { 1 } { \pi ( 1 - | z _ { 0 } | ^ { 2 } ) ^ { 2 } } }$

It should be observed that the bilinear expression (l2.6.l3) is not necessarily convergent for an arbitrary Hilbert space of functions.Thus,over ${ \cal L } ^ { 2 } [ - \pi , \pi ]$ we are led to the formal series

$$
{ \frac { 1 } { 2 \pi } } + { \frac { 1 } { \pi } } \sum _ { k = 1 } ^ { \infty } \cos k x \cos k t + \sin k x \sin k t .
$$

According to Corollary l2.l.7，convergence would be equivalent to the existence ead fites $\operatorname * { l i m } _ { n  \infty } K _ { n } ( x , t ) = \operatorname * { l i m } _ { n  \infty } \frac { 1 } { \pi } \frac { \sin { ( n + \frac { 1 } { 2 } ) } ( x - t ) } { 2 \sin { \frac { 1 } { 2 } ( x - t ) } }$ . But for any selection of $_ { \pmb { x } }$ and $\pmb { t }$ ,this limit does not exist.

In a space with a reproducing kernel, complete sets of functions can be generated conveniently from complete sets of functionals.

THEOREM 12.6.11．Let $\pmb { X }$ be $^ { \pmb { a } }$ complete inner product space of functions that has $^ { \pmb { a } }$ reproducing kernel $\pmb { K } ( P , \pmb { Q } )$ .I1f $\{ L _ { k } \}$ is $^ { \pmb { a } }$ sequence of bounded linear functionals on $\pmb { X }$ such that $f \in X$ ， $L _ { k } ( f ) = 0$ ， $k = 1 , 2 , \ldots$ ，implies $\scriptstyle f \equiv 0$ ， then the functions

$$
h _ { n } ( Q ) = \overline { { { L _ { n , P } K ( P , Q ) } } } \qquad n = 1 , 2 , . . . ,
$$

form a complete set for $\pmb { X }$

Proof:By Theorem 12.6.6, $L _ { n } ( f ) = ( f ( Q ) , h _ { n } ( Q ) )$ Hence $\left\{ h _ { n } ( Q ) \right\}$ isa complete sequence of functions,by Definition 8.9.4.

Ex.6.Let $\pmb { B }$ be a region that has a Bergman kernel function $\kappa ( z , w )$ .Let $z ^ { \prime }$ be a point of $\pmb { B }$ and suppose that ${ \boldsymbol { z } } _ { i }$ lie in $\pmb { B }$ and lim $z _ { i } = z ^ { \prime }$ .Then the functions $\overline { { K ( z _ { i } , w ) } } \quad i = 1 , 2 , \ldots ,$ ，and the functions $ \frac { d ^ { n } } { d z ^ { n } } ^ { i  \infty } | _ { z = z ^ { \prime } } n = 0 , 1 , . . . ,$ are complete for $L ^ { 2 } ( B )$

A further example of a reproducing kernel comes from the topic of differential equations.

Ex.7. Let $\pmb { X }$ consist of all functions ${ \pmb F } ( { \pmb x } )$ of the form

$$
F ( x ) = \int _ { 0 } ^ { x } f ( t ) d t , \qquad 0 \leq x \leq 1
$$

where $f ( t ) \in L ^ { 2 } [ 0 , 1 ]$ .If $G ( x ) = \int _ { 0 } ^ { x } g ( t ) d t ,$ ，then an inner product $( F , G )$ will be defined by

$$
( F , G ) \ = \int _ { 0 } ^ { 1 } f ( x ) g ( x ) \ d x \ = \int _ { 0 } ^ { 1 } F ^ { \prime } ( x ) G ^ { \prime } ( x ) \ d x .
$$

Now

$$
F ( x ) = \int _ { 0 } ^ { x } F ^ { \prime } ( t ) d t = \int _ { 0 } ^ { 1 } F ^ { \prime } ( t ) K ^ { \prime } ( t , x ) d t ,
$$

where

Hence,if we write

$$
\begin{array} { r l r l } & { K ^ { \prime } ( t , x ) = 1 } & & { 0 \leq t \leq x } \\ & { K ^ { \prime } ( t , x ) = 0 } & & { x < t \leq 1 . } \\ & { } & \\ & { K ( t , x ) = t } & & { 0 \leq t \leq x } \\ & { K ( t , x ) = x } & & { x \leq t \leq 1 , } \end{array}
$$

we have

$$
F ( x ) = ( F ( t ) , K ( t , x ) ) _ { t } .
$$

$\kappa ( t , x )$ is the reproducing kernel for $x$

The reader may recognize $K ^ { \prime } ( t , x )$ as the Green's function for the differential system $y ^ { \prime } = 0 , y ( 0 ) = 0$ .This is an instance of the following more inclusive situation. Let $x$ denote the space of functions defined on $[ a , b ]$ that can be written as an $\pmb { n }$ -folditerated integral

$$
F ( x ) = \int _ { a } ^ { x } d x \cdot \cdot \cdot \int _ { a } ^ { x } f ( x ) d x
$$

with $f ( x ) \in L ^ { 2 } [ a , b ]$ .Introduce the bilinear diferential expression

$$
( F , G ) \ = \int _ { a \ j = 0 } ^ { b } { \sum _ { a \ j } ^ { n } { a _ { j } ( x ) F ^ { ( j ) } ( x ) G ^ { ( j ) } ( x ) d x } }
$$

$$
a _ { 0 } ( x ) > 0 , a _ { n } ( x ) > 0 ; \quad a _ { i } ( x ) \geq 0 , \qquad i = 1 , 2 , \ldots , n - 1 .
$$

For ${ \pmb { F } } = { \pmb { G } }$ ,this leads to the norm (or energy integral)

$$
\| F \| ^ { 2 } = ( F , F ) = \int _ { a } ^ { b } \sum _ { j = 0 } ^ { n } a _ { j } ( x ) [ F ^ { ( j ) } ( x ) ] ^ { 2 } d x .
$$

The energy integral has associated with it the Euler-Lagrange diferential equation

$$
\sum _ { j = 0 } ^ { n } ( - 1 ) ^ { j } ( a _ { j } ( x ) F ^ { ( j ) } ( x ) ) ^ { ( j ) } = 0 .
$$

Consider also the $\scriptstyle 2 n$ boundary conditions

$$
\sum _ { j = m } ^ { n } ( - 1 ) ^ { j } ( a _ { j } ( x ) F ^ { ( j ) } ( x ) ) ^ { ( j - m ) } = 0
$$

at $x = a$ and $x = b , m = 1 , 2 , \ldots , n$

Then,if $\pmb { K } ( \pmb { x } , \pmb { t } )$ is the Green's function for the differential system (12.6.30,31), it is also the reproducing kernel for the function space $x$ .(Compare also the Peano kernel of 3.7.)

Ex.8.In Ex.7, $\pmb { K } ( \pmb { x } , \pmb { x } ) = \pmb { x }$ ,and from (12.6.4),

$$
\lvert F ( x ) \rvert ^ { 2 } \leq x \parallel F \parallel ^ { 2 } = x \int _ { 0 } ^ { 1 } \lvert F ^ { \prime } ( t ) \rvert ^ { 2 } d t .
$$

This exhibits the boundedness of the linear functional $L ( F ) = F ( x )$ in this space.

Ex.9.Let $X = L ^ { 2 } [ - \pi , \pi ]$ .This is not, properly speaking a function space, but a space of equivalence classes in which two functions are equivalent if and 'only if they differ on a set of at most zero measure.The functional $L ( f ) = f ( x ) ,$ 、 relevant to the definition of a reproducing kernel, is not defined.

However,let us not ignore the most famous reproducing kernel of them all: the Dirac delta function $K ( x , y ) = \delta ( x - y )$ .The reproducing integral expression

$$
f ( x ) = \int _ { - \pi } ^ { \pi } f ( y ) \delta ( x - y ) d y
$$

and the (divergent) orthogonal expansion

$$
\delta ( x - y ) = { \frac { 1 } { 2 \pi } } + { \frac { 1 } { \pi } } \sum _ { k = 1 } ^ { \infty } \cos k x \cos k y + \sin k x \sin k y = { \frac { 1 } { 2 \pi } } + { \frac { 1 } { \pi } } \sum _ { k = 1 } ^ { \infty } \cos k ( x - y )
$$

are basic to the theory of the $\pmb { \delta }$ function. Though many suggestive things can be done formally,a proper relation between the $\pmb { \delta }$ function and reproducing kernels must be sought within a different framework of ideas.

The intimate relationship between reproducing kernels and completeness may be strengthened.

THEOREM 12.6.12．Let $L ^ { 2 } ( B )$ be a Hilbert space and let ${ \pmb K } ( z , w )$ beits reproducing kernel. Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be an orthonormal system. This system is complete if and only if

$$
K ( z , z ) = \sum _ { k = 1 } ^ { \infty } | h _ { k } { } ^ { * } ( z ) | ^ { 2 } , \qquad z \in { \cal B } .
$$

Proof: If $\{ { h _ { n } } ^ { * } ( z ) \}$ is complete,(l2.6.34) follows directly from Theorem 12.6.8 and (12.6.13). Suppose the system is incomplete. Then by Theorem 9.3.12 we may find nonzero functions ${ g _ { n } } ^ { * } ( z )$ such that the combined system $\{ h _ { n } * \} , \{ g _ { n } * \}$ is complete and orthonormal. By (l2.6.13),

$$
K ( z , z ) = \sum _ { k = 1 } ^ { \infty } | h _ { k } ^ { \ast } ( z ) | ^ { 2 } + \sum _ { k = 1 } ^ { \infty } | g _ { k } ^ { \ast } ( z ) | ^ { 2 } .
$$

Hence $K ( z , z ) > \sum _ { k = 1 } ^ { \infty } | h _ { k } ^ { } \ast ( z ) | ^ { 2 }$ at some point of $\pmb { B }$

A similar criterion holds for $L ^ { 2 } [ a , b ]$

THEOREM 12.6.13 (Vitali). The orthonormal sequence $\{ f _ { n } { } ^ { * } ( x ) \}$ is complete for $L ^ { 2 } [ a , b ]$ if and only if

$$
\sum _ { n = 1 } ^ { \infty } \left( \int _ { a } ^ { t } f _ { n } { } ^ { * } ( x ) d x \right) ^ { 2 } = t - a , \qquad a \leq t \leq b .
$$

Proof: For $S ( x ) \in L ^ { 2 } [ a , b ]$ , and assuming the sequence complete, we have by Theorem 89.(16) $\int _ { a } ^ { b } S ^ { 2 } ( x ) d x = \sum _ { n = 1 } ^ { \infty } \left( \int _ { a } ^ { b } S ( x ) f _ { n } ^ { * } ( x ) d x \right) ^ { 2 }$ Pix $\pmb { t }$ im $[ \pmb { a } , \pmb { b } ]$ and select $\boldsymbol { S } ( \boldsymbol { x } ) = \boldsymbol { 1 }$ ， $a \leq x \leq t , S ( x ) = 0 , t < x \leq b$ This yields (12.6.35) immediately.

Conversely,suppose that (l2.6.35) holds.As we have seen,this tells us that Parseval's Identity holds for step functions $\pmb { S } ( \pmb { x } )$ of the above type. As in the proof of Theorem 8.9.1 $( \mathbf { C }  \mathbf { B } )$ , the sequence $\{ f _ { n } { } ^ { * } ( x ) \}$ is therefore closed in the set of these $\mathbf { \nabla } _ { \mathbf { \vec { s } } }$ .By Ex.4,1l.1,the step functions $\mathbb { S } _ { i }$ are closed in $L ^ { 2 } [ a , b ]$ .By the transitivity of closure,(Theorem l1.1.8), $\{ f _ { n } * \}$ is closed in $L ^ { 2 } [ a , b ]$

The relationship between (l2.6.34) and (l2.6.35) is this:whereas the former is the kernel identity,the latter is an integrated form of this identity. Starting with the symbolic equation,

$$
\delta ( x - y ) = \sum _ { n = 1 } ^ { \infty } { f _ { n } } ^ { * } ( x ) { f _ { n } } ^ { * } ( y )
$$

as suggested by (l2.6.33),a single integration yields

$$
1 = \int _ { a } ^ { u } \delta ( x - y ) d y = \sum _ { n = 1 } ^ { \infty } { f _ { n } } ^ { * } ( x ) \int _ { a } ^ { u } { f _ { n } } ^ { * } ( y ) d y .
$$

A second integration yields

$$
u - a = \int _ { a } ^ { u } d x = \sum _ { n = 1 } ^ { \infty } \int _ { a } ^ { u } f _ { n } { } ^ { * } ( x ) d x \int _ { a } ^ { u } f _ { n } { } ^ { * } ( y ) d y = \sum _ { n = 1 } ^ { \infty } \left( \int _ { a } ^ { u } f _ { n } { } ^ { * } ( x ) d x \right) ^ { 2 } .
$$

We conclude this chapter by giving a useful alternative expression for the kernel function for $L ^ { 2 } ( B )$ in a case where $\pmb { B }$ is fairly simple.

THEOREM 12.6.14．Let $w = m ( z )$ map a region $B \ : 1 - 1$ conformally onto the unit circle $c$ Then,the reproducing kernel for $L ^ { 2 } ( B )$ is

$$
K ( z , t ) = \frac { m ^ { \prime } ( z ) \overline { { m ^ { \prime } ( t ) } } } { \pi ( 1 - m ( z ) \overline { { m ( t ) } } ) ^ { 2 } } , ~ z , t \in B .
$$

Proof:Let the map inverse to $\pmb { m }$ be $z = M ( w )$ . Then, $\boldsymbol { m } ( \boldsymbol { M } ( \boldsymbol { w } ) ) \equiv \boldsymbol { w }$ and $m ^ { \prime } ( M ( w ) ) M ^ { \prime } ( w ) \equiv 1$ For any $f , g \in L ^ { 2 } ( B )$ ，we have

$$
( f , g ) = \int \int _ { B } f ( z ) { \overline { { g ( z ) } } } \ d x \ d y = \int _ { C } \int f ( M ( w ) ) { \overline { { g ( M ( w ) ) } } } \ | M ^ { \prime } ( w ) | ^ { 2 } \ d u \ d v , \eqno ( w \implies u + i v ) .
$$

This follows from (9.2.35) and the method of Lemma 9.2.4. The system of functions un(z) =√ $u _ { n } ( z ) = \sqrt { \frac { n + 1 } { \pi } } \ ( m ( z ) ) ^ { n } m ^ { \prime } ( z )$ ， $\pmb { n = 0 } , \ \pmb { 1 } , \ \dots .$ ，is complete and orthonormal for $L ^ { 2 } ( B )$ .For

$$
\begin{array} { l } { \displaystyle \sqrt { \frac { \pi } { n + 1 } } \ ( f , u _ { n } ) = \displaystyle \iint _ { B } f ( z ) \overline { { { ( m ( z ) ) ^ { n } } { m ^ { \prime } ( z ) } } } \ d x \ d y } \\ { \displaystyle = \iint f ( M ( w ) ) \overline { { { w ^ { n } } { m ^ { \prime } ( M ( w ) ) } } } \ | M ^ { \prime } ( w ) | ^ { 2 } \ d u \ d v } \\ { \displaystyle \qquad = \ \iint f ( M ( w ) ) M ^ { \prime } ( w ) \overline { { { w ^ { n } } } } \ d u \ d v . } \end{array}
$$

Hence $( f , u _ { n } ) = 0 \ n = 0 , 1 , . . . .$ ,implies,by the completeness of $1 , w , w ^ { 2 }$ ， ...,over $L ^ { 2 } ( C )$ ，that $f ( M ( w ) ) M ^ { \prime } ( w ) \equiv 0$ Since $M ^ { \prime } \ne 0 , f \equiv 0$ .Therefore $\left\{ u _ { n } \right\}$ is complete for $L ^ { 2 } ( B )$ .Similarly for orthonormality.

By Theorem 12.6.9,

$$
K ( z , t ) = \frac { 1 } { \pi } \sum _ { n = 0 } ^ { \infty } ( n + 1 ) ( m ( z ) ) ^ { n } m ^ { \prime } ( z ) \overline { { ( m ( t ) ) ^ { n } m ^ { \prime } ( t } } ) .
$$

In view of the identity $( 1 - x ) ^ { - 2 } = \sum _ { n = 0 } ^ { \infty } ( n + 1 ) x ^ { n }$ , we obtain (12.6.36).

COROLLARY 12.6.15.Let $w = m ( z )$ map $\pmb { B }$ onto the unit circle. The mapping is normalized by requiring that ${ \mathbf { } m } ( t ) = 0$ ， $m ^ { \prime } ( t ) > 0$ where $\pmb { t }$ is $^ { \pmb { a } }$ fixed point in B. Then,

$$
m ( z ) = { \mathrm { c o n s t } } \cdot \int _ { t } ^ { z } K ( z , t ) d z .
$$

Proof: Since $m ( t ) = 0 , K ( z , t ) = \frac { 1 } { \pi } m ^ { \prime } ( z ) m ^ { \prime } ( t )$ . Hence

$$
m ( z ) = \frac { \pi } { m ^ { \prime } ( t ) } \int _ { t } ^ { z } K ( z , t ) \ : d z .
$$

If $\pmb { B }$ has a sufficiently smooth boundary, (see Theorem ll.4.8), there is a complete orthonormal set of polynomials in $L ^ { 2 } ( B )$ ,and ${ \pmb K } ( { \pmb z } , { \pmb t } )$ can, in principle,be computed directly by (l2.6.13). Equation (l2.6.37) then gives an elementary representation for the mapping function.

Ex.10.Let $c$ designate the unit circle $| z | < 1$ and $\boldsymbol { G } _ { \pmb { s } }$ be $\boldsymbol { \mathfrak { C } }$ with the radius ${ \bf 0 } \le { \pmb x } < { \bf 1 }$ deleted.Note that $\boldsymbol { C } _ { \pmb { S } }$ does not fulfill the condition of Theorem 11.4.8. The powers $1 , z , z ^ { 2 } , \ldots ,$ ，cannot be complete in $L ^ { 2 } ( C _ { S } )$ .For assume they were. The removal of $\mathbf { 0 } \leq x \leq \mathbf { 1 }$ does not affect the double integrals.Hence, $\sqrt { \frac { n + 1 } { \pi } } z ^ { n } \quad n = 0 , 1 , . . . ,$ ， is a complete orthonormal system for both $L ^ { 2 } ( C )$ and $L ^ { 2 } ( C _ { S } )$ . This implies that $\kappa _ { C } ( z , t ) = K _ { C _ { s } } ( z , t )$ By (12.6.37),this is absurd.

# NOTES ON CHAPTER XII

12.1-12.2 Zygmund [l] is an exhaustive treatise on this topic. 12.3 See,e.g.,Behnke and Sommer [l] pp.249-256. 12.4Jackson [2] pp.63-68. Szeg [1],Chapter 9; Hobson [1],Chapter 2; Rainville [l], Chapter 10. 12.5Bergman [2].Nehari [1]. 12.6Bergman [2]. Aronszajn [2].Bergman and Schiffer [1],Part B, Chapter II.Example 5:Golomb and Weinberger [l].For further criteria as in Theorem 12.6.12,see Tricomi [l] pp.26-30.

# PROBLEMS

1.How do the symmetries (1) $f ( - x ) = f ( x ) ,$ (2) $\begin{array} { r } { f ( - x ) = - f ( x ) , } \end{array}$ (3) $f ( x + \pi ) = f ( x )$ (4) $f ( x + \pi ) = - f ( x )$ influence the structure of the Fourier coefficients of $f \left( x \right) \ !$

2.What is the Fourier series of a trigonometric polynomial?

3.What is the Fourier series for $\cos ^ { n } x \ell$

4.Sgn si $1 ~ k t = { \frac { 4 } { \pi } } \sum _ { j = 0 } ^ { \infty } { \frac { \sin { ( 2 j + 1 ) } ~ k t } { 2 j + 1 } } \quad k = 1 , 2 , \ldots { \mathrm { . ~ } } { \mathrm { . ~ D i s c u s s ~ t h e ~ c o r } }$ onvergence.

5. $\left| \sin x \right| = { \frac { 8 } { \pi } } \sum _ { n = 1 } ^ { \infty } { \frac { \sin ^ { 2 } n x } { 4 n ^ { 2 } - 1 } }$

6.Let $0 < h < \pi$ and $f ( x ) = 1$ for $| x | \leq h , f ( x ) = 0$ for $h < | x | \leq \pi$

$$
f \left( x \right) \sim \frac { 2 h } { \pi } \bigg [ \frac { 1 } { 2 } + \sum _ { k = 1 } ^ { \infty } \frac { \sin k h } { k h } \cos k x \bigg ] .
$$

# Convergence?

7. Diseus the onvergence f $\sum _ { n = 1 } ^ { \infty } r ^ { n }$ sin $n x = { \frac { r \sin x } { 1 - 2 r \cos x + r ^ { 2 } } } .$

8. Prove that for $| r | < 1 , { \frac { 1 - r \cos z } { 1 - 2 r \cos z + r ^ { 2 } } } = 1 + r \cos z + r ^ { 2 } \cos 2 z + \cdot \cdot \cdot .$

The expansion is convergent in an infinite strip parallel to the $_ { x }$ axis.

9. Prove that arc tan $\frac { r \sin z } { 1 - r \cos z } = r \sin z + { \frac { 1 } { 2 } } r$ sin $2 z + \cdots$ ，and discuss the convergence.

10.Set $f ( x ) = e ^ { z x }$ in Parseval's Theorem on $[ 0 , 2 \pi ]$ and derive the identity e2n2 T

$$
\begin{array} { r l } & { \frac { { \mathrm { , } } ^ { 2 \pi z } \ + \ 1 } { 2 \pi z \ - \ 1 } = \displaystyle \frac { 1 } { z } \ + \ 2 z \sum _ { n = 1 } ^ { \infty } \frac { 1 } { z ^ { 2 } \ + \ n ^ { 2 } } . } \\ & { \ \mathrm { 1 1 . \ } \operatorname* { P r o v e \ t h a t } \displaystyle \frac { 1 } { p } \int _ { z _ { 0 } } ^ { z _ { 0 } + p } \left| f ( z ) \right| ^ { 2 } d z \ = \sum _ { n = - \infty } ^ { \infty } \left| a _ { n } \right| ^ { 2 } e ^ { - 4 \pi n \operatorname { I m } ( z _ { 0 } / p ) } . } \end{array}
$$

12.Use Theorem 12.2.7 to prove that if $f ( x )$ is continuous at $_ x$ and if the Fourier series of $f ( x )$ converges at $_ { x }$ ,it converges to $f ( x )$ ·

13.Is there a $( C , 1 )$ sum of the formal kernel

14.

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { 2 \pi } + \frac { 1 } { \pi } \sum _ { k = 1 } ^ { \infty } \cos { n x } \cos { n t } + \sin { n x } \sin { n t } \uparrow } } \\ { { \displaystyle \left| x \right| \sim \sum _ { k = 0 } ^ { \infty } a _ { n } P _ { n } ( x ) } } \end{array}
$$

where $a _ { n } = 0 , n$ odd, $\begin{array} { r } { a _ { \mathbf { 0 } } = \frac { 1 } { 2 } , a _ { \mathbf { 2 } } = \frac { 5 } { 8 } } \end{array}$

$$
a _ { n } = \frac { 2 n + 1 } { ( n - 1 ) ( n + 2 ) } P _ { n } ( 0 ) n = 3 , 4 , . . . .
$$

15.If $( x ) \ : = \ : 1 , 0 \leq x \leq 1 , f ( x ) = - 1 , - 1 \leq x < 0$ ,then

$$
f ( x ) \sim - \sum _ { k = 0 } ^ { \infty } \frac { 4 k + 3 } { 2 k + 1 } { \binom { - \frac { 1 } { 2 } } { k + 1 } } P _ { 2 k + 1 } ( x ) .
$$

16. Let $0 < a < 1$ . Show by Rodrigues’ Formula and integration by parts that

$$
\frac { 1 } { ( 1 - x ) ^ { a } } \sim \sum _ { n = 0 } ^ { \infty } a _ { n } P _ { n } ( x )
$$

where

$$
{ \bf \tau } _ { 0 } = \frac { 1 } { 2 ^ { a } ( 1 - a ) } , a _ { 1 } = \frac { 3 a } { 2 ^ { a } ( 1 - a ) ( 2 - a ) } , a _ { n } = \frac { ( 2 n + 1 ) a ( a + 1 ) \cdot \cdot \cdot ( a + n - 1 ) } { 2 ^ { a } ( 1 - a ) ( 2 - a ) \cdot \cdot \cdot ( n + 1 - a ) } , \nonumber 
$$

Discuss convergence.

17. ${ \frac { 1 - h ^ { 2 } } { ( 1 \ - \ 2 h z \ + \ h ^ { 2 } ) ^ { \frac { 3 } { 2 } } } } = \sum _ { n = 0 } ^ { \infty } ( 2 n \ + \ 1 ) h ^ { n } P _ { n } ( z ) ,$ Discuss convergence.

18.Use Theorem 12.4.7 to conclude that if $f \in C ^ { \infty } [ - 1 , 1 ]$ and if the derivatives are“not too large,”then $f$ can be continued analytically into the complex plane.

19. The Bergman kernel for $| z | < r$ is $\frac { r ^ { 2 } } { \pi ( r ^ { 2 } - z \bar { w } ) ^ { 2 } } .$

20.Verify by Vitali's Theorem that cos $n x , n = 0 , 1 , 2 , \ldots$ ，is complete for $L ^ { 2 } [ 0 , \pi ]$

21.Apply Vitali's Theorem to $P _ { n } ( x )$ and obtain an identity for the Legendre polynomials.
