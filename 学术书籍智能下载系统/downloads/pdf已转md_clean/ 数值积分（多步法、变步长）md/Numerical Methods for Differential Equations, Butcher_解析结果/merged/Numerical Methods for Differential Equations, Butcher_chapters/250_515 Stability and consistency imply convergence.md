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
