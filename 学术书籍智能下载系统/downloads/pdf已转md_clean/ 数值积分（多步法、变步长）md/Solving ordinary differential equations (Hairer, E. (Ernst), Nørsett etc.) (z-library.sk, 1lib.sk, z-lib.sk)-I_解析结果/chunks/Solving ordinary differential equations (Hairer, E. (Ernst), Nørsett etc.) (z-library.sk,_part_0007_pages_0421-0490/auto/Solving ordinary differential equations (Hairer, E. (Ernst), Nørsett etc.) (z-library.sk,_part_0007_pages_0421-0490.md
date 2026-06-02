# II1.9. Asymptotic expansion of the global error

The asymptotic expansion of the global error of multistep methods was studied in the famous thesis of Gragg (1963). His proof is very technical and can also be found in a modified version in the book of Stetter (1973)， pp.234-245. The existence of asymptotic expansions for general linear methods was conjectured by Skeel (1976). The proof given below (Hairer and Lubich (1984)) is based on the ideas of Section II.8.

# An instructive exam ple

Let us start with an example in order to understand which kind of asymptotic expansion may be expected. We consider the simple differential equation

$$
y ^ { \prime } = - y , \qquad y ( 0 ) = 1 ,
$$

take a constant step size $h$ and apply the 3-step BDF-formula (1. with one of the following three starting procedures:

$$
\begin{array} { r l r l } & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } \mathrm { e x p } ( - h ) } \\ & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } 1 { - } h + \displaystyle \frac { h ^ { 2 } } { 2 } - \displaystyle \frac { h ^ { 3 } } { 6 } } & & { y _ { 2 } { = } 1 { - } 2 h + 2 h ^ { 2 } - \displaystyle \frac { 8 h ^ { 3 } } { 6 } } \\ & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } 1 { - } h + \displaystyle \frac { h ^ { 2 } } { 2 } } & & { y _ { 2 } { = } 1 - 2 h + 2 h ^ { 2 } . } \end{array}
$$

The three pictures on the left of Figure 9.1 (they correspond to the three starting procedures in the same order) show the global error divided by $h ^ { 3 }$ for the five step sizes $h = 1 / 5$ ,1/10, 1/20, 1/40, 1/80.

For the first two starting procedures we observe uniform conver-gence to the function $e _ { 3 } ( x ) { = } x e ^ { - x } / 4$ (cf. Formula (2.12)), so that

$$
y _ { n } - y ( x _ { n } ) = e _ { 3 } ( x _ { n } ) h ^ { 3 } + \mathbf { O } ( h ^ { 4 } ) \ ,
$$

valid uniformly for $0 \leq n h \leq C o n s t$ . In the third case we have convergence to $e _ { 3 } ( x ) = ( 9 + x ) e ^ { - x } / 4$ (Exercise 2), but this time the convergence is no longer uniform. Therefore (9.2) only holds for $x _ { n }$ bounded away from $x _ { 0 }$ , i.e. for $0 < \alpha \leq n h \leq C o n s t$ . In the three pictures on the right of Figure 9.1 the functions

$$
( y _ { n } - y ( x _ { n } ) - e _ { 3 } ( x _ { n } ) h ^ { 3 } ) / { h ^ { 4 } }
$$

![](images/f5f9264f23b35024421e522b37e06d839ab11b198efdad2094a03dcb57f87486.jpg)  
Figure 9.1. The values of $\frac { y _ { n } - y ( x _ { n } ) } { h ^ { 3 } }$ (left), $\frac { y _ { n } - y ( x _ { n } ) - e _ { 3 } ( x _ { n } ) h ^ { 3 } } { h ^ { 4 } }$ (right) for the 3-step BDF method and for three different starting procedures

are plotted. Convergence to functions $e _ { 4 } ( x )$ is observed in all cases. Clearly, since $e _ { 3 } ( x _ { 0 } ) \neq 0$ for the starting procedure (9.1c)， the sequence (9.3) diverges at $x _ { 0 }$ like $\mathbf { O } ( 1 / h )$ in this case.

We conclude from this example that for linear multistep methods there is in general no asymptotic expansion of the form

$$
y _ { n } - y ( x _ { n } ) = e _ { p } ( x _ { n } ) h ^ { p } + e _ { p + 1 } ( x _ { n } ) h ^ { p + 1 } + \cdot \cdot \cdot
$$

which holds uniformly for $0 \leq n h \leq C o n s t$ . It will be necessary to add perturbation terms

$$
y _ { n } - y ( x _ { n } ) = ( e _ { p } ( x _ { n } ) + \in _ { n } ^ { p } ) h ^ { p } + ( e _ { p + 1 } ( x _ { n } ) + \in _ { n } ^ { p + 1 } ) h ^ { p + 1 } + \cdot \cdot \cdot
$$

which compensate the irregularity near $x _ { 0 }$ . If the perturbations $\epsilon _ { n } ^ { j }$ decay exponentionally (for $n  \infty$ ), then they have no influence on the asymptotic expansion for $x _ { n }$ bounded away from $\boldsymbol { \mathscr { x } } _ { 0 }$

# Asymptotic expansion for strictly stable methods (8.4)

In order to extend the techniques of Section I1.8 to muitistep methods it is useful to write them as a "one-step" method in a higher dimensional space (cf. (4.8) and Example 8.2). This suggests we study at once the asymptotic expansion for the general method (8.4). Because of the presence of $\epsilon _ { n } ^ { j } h ^ { j }$ in (9.4), the iterative proof of Theorem 9.1 below will lead us to increment functions which also depend on $n$ , of the form

$$
\Phi _ { n } ( x , u , h ) = \Phi ( x , u + h \alpha _ { n } ( h ) , h ) + \beta _ { n } ( h ) \ .
$$

We therefore consider for an equidistant grid $( x _ { n } )$ the numerical procedure

$$
\begin{array} { c } { { u _ { 0 } = \phi ( h ) } } \\ { { { } } } \\ { { u _ { n + 1 } = S u _ { n } + h \Phi _ { n } ( x _ { n } , u _ { n } , h ) } } \end{array}
$$

where $\Phi _ { \pi }$ is given by (9.5) and the correct value function is again denoted by $z \left( x , h \right)$ . The following additional assumptions will simplify the discussion of an asymptotic expansion:

A1)Method (9.6) is stricty stable; i.e. it is stable (Definition 8.8) and 1 is the only eigenvalue of S with modulus one. In this case the spectral radius of $s - E$ (cf. Formula (8.11)) is smaller than 1 ;   
${ \bf A } 2 ) \alpha _ { n } ( h )$ and ${ \boldsymbol { \beta } } _ { n } \left( h \right)$ are polynomials， whose coeficients decay exponentially like $\mathbf { O } ( \rho _ { 0 } ^ { n } )$ for $n  \infty$ . Here ${ \boldsymbol \rho } _ { 0 }$ denotes some number lying between the spectral radius of $s - E$ and one; i.e. $\mathsf { p } ( \boldsymbol { S } - \boldsymbol { E } ) < \mathsf { p } _ { 0 } < 1$ ；

A3)the functions $\phi$ ， $z$ and $\Phi$ are sufficiently differentiable.

Assumption A3 allows us to expand the local error, defined by (8.9), into a Taylor series:

$$
\begin{array} { l } { { \displaystyle { \mathfrak { a } } + 1 = z ( x _ { n } + h , h ) - S z ( x _ { n } , h ) - h \Phi \big ( x _ { n } , z ( x _ { n } , h ) + h \mathfrak { a } _ { n } \big ( h ) , h \big ) - h \mathfrak { b } _ { n } } } \\ { { \displaystyle \qquad = d _ { 0 } ( x _ { n } ) + d _ { 1 } ( x _ { n } ) h + \cdot \cdot \cdot + d _ { N + 1 } ( x _ { n } ) h ^ { N + 1 } } } \\ { { \displaystyle \qquad - h ^ { 2 } \frac { \partial \Phi } { \partial u } ( x _ { n } , z ( x _ { n } , 0 ) , 0 ) \alpha _ { n } ( h ) - \cdot \cdot \cdot - h \mathfrak { b } _ { n } ( h ) + { \sf O } ( h ^ { N + 1 } ) \ , } } \end{array}
$$

The expressions involving $\alpha _ { n } \left( h \right)$ can be simplified further. Indeed, for a smooth function $G \left( x \right)$ we have

$$
\Im \left( x _ { n } \right) \alpha _ { n } ( h ) = G \left( x _ { 0 } \right) \alpha _ { n } ( h ) + h G ^ { \prime } ( x _ { 0 } ) n \alpha _ { n } ( h ) + \cdot \cdot \cdot + h ^ { N + 1 } R \left( n , \right)
$$

We observe that $n ^ { j } \alpha _ { _ n } ( h )$ is again a polynomial in $h$ and that its coefficients decay like" $\mathbf { 0 } ( \mathbf { \boldsymbol { \rho } } ^ { n } )$ where p satisfies $\boldsymbol { \rho } _ { 0 } < \boldsymbol { \rho } < 1$ . The same argument shows the boundedness of the remainder $R \ ( n \ , \ h )$ for $0 \leq n h \leq C o n s t$ .As a consequence we can write the local error in the form

$$
\begin{array} { r c l } { { } } & { { } } & { { d _ { 0 } = \gamma _ { 0 } + \gamma _ { 1 } h + \cdot \cdot \cdot + \gamma _ { N } h ^ { N } + 0 ( h ^ { N + 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { { } _ { n + 1 } = ( d _ { 0 } ( x _ { n } ) + \mathfrak { d } _ { n } ^ { 0 } ) + \cdot \cdot \cdot + ( d _ { N + 1 } ( x _ { n } ) + \mathfrak { d } _ { n } ^ { N + 1 } ) h ^ { N + 1 } + 0 ( h ^ { N + 2 } ) } } \end{array}
$$

The functions $d _ { j } ( \boldsymbol { x } )$ are smooth and the perturbations $8 { } _ { n } ^ { j }$ satisfy $\ S _ { n } ^ { j } { = } \mathbf { 0 } ( \boldsymbol { \rho } ^ { n } )$ . The expansion (9.7) is unique, because $\ S _ { \pi } ^ { j } \to$ 0 for $n  \infty$ ·

Method (9.6) is called consistent of order $\boldsymbol { p }$ , if the local error (9.7) satisfies (Lemma 8.11)

$$
d _ { n } = 0 ( h ^ { p } ) \qquad \mathrm { f o r } \quad 0 \leq n h \leq c o n s i , \quad \mathrm { a n d } \quad E d _ { p } ( x ) = 0 .
$$

Obs thisnth $8 { } _ { n } ^ { j }$ h ahe to vanish $j = 0 , \ldots , p - 1$ $\ S _ { n } ^ { p }$ tial decay of these terms implies that we still have

$$
d _ { n + 1 } + E ( d _ { n } + \cdot \cdot \cdot + d _ { 0 } ) = \mathrm { O } ( h ^ { P } ) \qquad \mathrm { f o r } 0 { \leq } n h { \leq } c o n s t ,
$$

in agreement with Definition 8.10. One can now easily verify that Lemma 8.12 ( $\Phi _ { \pi }$ satisfies a Lipschitz condition with the same constant as $\Phi$ ） and the Convergence Theorem 8.13 remain valid for Method (9.6). In the following theorem we use, as for one-step methods, the notation $\boldsymbol { u } _ { h _ { n } } ( \boldsymbol { x } ) = \boldsymbol { u } _ { n }$ when $x = x _ { n }$

Theorem 9.1. (Hairer-Lubich, 1984). Let the method (9.6) satisfy A $1 - A \ 3$ and be consistent of order $p \left( p \geq 1 \right)$ ).Then the global error has an asymptotic expansion of the form

$$
u _ { h } ( x ) - z ( x , h ) = e _ { p } ( x ) h ^ { p } + \cdot \cdot \cdot + e _ { N } ( x ) h ^ { N } + E ( x , h ) h ^ { N + 1 }
$$

where the $e _ { j } ( x )$ are given in the proof (cf. Formula $( 9 . I 8 )$ )and $E \left( x , h \right)$ is bounded uniformly in $h \in [ 0 , h _ { 0 } ]$ and for $x$ in compact intervals not containing $\boldsymbol { x } _ { \textup { 0 } }$ More precisely than (9.9), there is an expansion

$$
u _ { _ { R } } - z _ { _ { R } } = ( e _ { _ { p } } ( x _ { _ { R } } ) + \epsilon _ { _ { n } } ^ { p } ) h ^ { p } + \cdot \cdot \cdot + ( e _ { _ { N } } ( x _ { _ { R } } ) + \epsilon _ { _ { n } } ^ { N } ) h ^ { N } + \tilde { \cal E } ( n , h ) h _ { _ { \cal E } _ { \cal E } } ^ { I }
$$

where $\scriptstyle \epsilon _ { n } ^ { j } = 0 ( { \mathfrak { p } } ^ { n } )$ with $\mathsf { p } ( S - E ) < \mathsf { p } < 1$ and $\tilde { E } \left( n , h \right)$ is bounded for $0 \leq n h \leq c o n s t$

Remark: We obtain from (9.10) and (9.9)

$$
E ( x _ { n } , h ) = \tilde { E } ( n , h ) + h ^ { - 1 } \epsilon _ { n } ^ { N } + h ^ { - 2 } \epsilon _ { n } ^ { N - 1 } + \cdot \cdot \cdot + h ^ { p - N - 1 } \epsilon _ { n } ^ { p } ,
$$

so that the remainder term $E \left( x , h \right)$ is in general not uniformly bounded in $h$ for $x$ varying in an interval $[ x _ { 0 } , \bar { x } ]$ . However, if $x$ is bounded away from $\boldsymbol { \mathscr { x } } _ { \mathrm { ~ 0 ~ } }$ say ${ x \ge x _ { 0 } + 8 }$ ( $\delta > 0$ fixed), the sequence $\epsilon _ { n } ^ { j }$ goes to zero faster than any power of $8 / n \le h$ ·

Proof: a) As for one-step methods (cf. proof of Theorem 8.1, Chapter II) we construct a new method, which has as numerical solution

$$
\hat { a } _ { n } = u _ { n } - ( e ( x _ { n } ) + \epsilon _ { n } ) h ^ { p }
$$

for a given smooth function $e \left( x \right)$ and a given sequence $\epsilon _ { n }$ satisfying $\varepsilon _ { n } = \mathbf { O } ( \boldsymbol { \rho } ^ { n } ) .$ Such a method is given by

$$
\begin{array} { c } { { \hat { u } _ { 0 } = \hat { \phi } ( h ) } } \\ { { { } } } \\ { { \hat { u } _ { n + 1 } = S \hat { u } _ { n } + h \hat { \Phi } _ { n } ( x _ { n } , \hat { u } _ { n } , h ) } } \end{array}
$$

where $\hat { \boldsymbol { \Phi } } ( h ) { = } { \boldsymbol { \Phi } } ( h ) { - } ( \boldsymbol { e } ( \boldsymbol { x } _ { 0 } ) { + } \epsilon _ { 0 } ) h ^ { p }$ and

$$
\begin{array} { l } { { \hat { \Phi } _ { n } ( x , u , h ) = \Phi _ { n } ( x , u + ( e ( x ) + \epsilon _ { n } ) h ^ { p } , h ) } } \\ { { \mathrm { } - ( e ( x + h ) - S e ( x ) ) h ^ { p - 1 } - ( \epsilon _ { n + 1 } - S \epsilon _ { n } ) h ^ { p - 1 } . } } \end{array}
$$

Since $\Phi _ { n }$ is of the form (9.5), $\hat { \Phi } _ { n }$ is also of this form, so that its local error has an expansion (9.7). We shall now determine $e \left( x \right)$ and $\epsilon _ { n }$ in such a way that the method (9.12) is consistent of order $p + 1$ ·

b) The local error $\hat { d } _ { n }$ of (9.12) can be expanded as

$$
\begin{array} { r l } & { \quad \hat { d } _ { 0 } = z _ { 0 } - \hat { a } _ { 0 } = ( \gamma _ { p } + e ( x _ { 0 } ) + \epsilon _ { 0 } ) h ^ { p } + 0 ( h ^ { p + 1 } ) } \\ & { \quad \hat { d } _ { n + 1 } = z _ { n + 1 } - S z _ { n } - h \hat { \Phi } _ { n } ( x _ { n } , z _ { n } , h ) } \\ & { \quad \quad \quad = d _ { n + 1 } + \bigg ( ( I - S ) e ( x _ { n } ) + ( \epsilon _ { n + 1 } - S \epsilon _ { n } ) \bigg ) h ^ { p } } \\ & { \quad \quad \quad + \left( - G ( x _ { n } ) ( e ( x _ { n } ) + \epsilon _ { n } ) + e ^ { \prime } ( x _ { n } ) \right) h ^ { p + 1 } + 0 ( h ^ { p + 2 } ) \ . } \end{array}
$$

Here

$$
G ( x ) = \frac { \partial \Phi _ { n } } { \partial u } ( x , z ( x , 0 ) , 0 )
$$

which is independent of $n$ by (9.5). The method (9.12) is consistent of order $p + 1$ if (see (9.8))

$$
\begin{array} { r l } & { \epsilon _ { 0 } = - \gamma _ { 0 } - e ( x _ { 0 } ) } \\ & { d _ { p } ( x ) + ( I - S ) e ( x ) + \ S _ { n } ^ { p } + \epsilon _ { n + 1 } - S \epsilon _ { n } = 0 \quad \mathrm { f o r } x = x _ { n } } \\ & { E e ^ { \prime } ( x ) = E G \left( x \right) e ( x ) - E d _ { p + 1 } ( x ) \ . } \end{array}
$$

We assume for the moment that the system (i)-(ii) can be solved for $e \left( x \right)$ and $\epsilon _ { n }$ . This will actually be demonstrated in part d) of the proof. By the Convergence Theorem 8.13 the method (9.12) is convergent of order $p + 1 .$ Hence

$$
\begin{array} { r } { \widehat { a } _ { n } - z _ { n } = { \bf O } ( h ^ { p + 1 } ) \quad \mathrm { ~ u n i f o r m l y ~ f o r ~ } 0 \leq n h \leq c o n s t \enspace , } \end{array}
$$

which yields the statement (9.10) for $N = _ { P }$

c) The method (9.12) satisfies the assumptions of the theorem with $p$ replaced by $p + 1$ and ${ \mathfrak { p } } _ { 0 }$ by p. As in Theorem 8.1 (Section I.8) an induction argument yields the result.

d) It remains to find a solution of the system (i)-(ii). Condition (ii) is satisfied if

$$
\begin{array} { l } { { d _ { p } ( x ) = ( S - I ) ( e ( x ) + c ) \nonumber } } \\ { { \phantom { e } \epsilon _ { n + 1 } - c = S ( \epsilon _ { n } - c ) - 8 { } _ { n } ^ { p } } } \end{array}
$$

hold for some constant $c$ . Using $( I - S + E ) ^ { - 1 } ( I - S ) = ( I - E )$ , which is a consequence of $S E = E ^ { 2 } = E$ (see (8.11)), Formula (iia) is equivalent

to

$$
\bigl ( I - S + E \bigr ) ^ { - 1 } d _ { p } ^ { } \bigl ( x \bigr ) = - \bigl ( I - E \bigr ) \bigl ( e \bigl ( x \bigr ) + c \bigr ) .
$$

From (i) we obtain $\epsilon _ { 0 } - c = - \gamma _ { p } - ( e ( x _ { 0 } ) + c )$ , so that by (9.13)

$$
( I - E ) ( \epsilon _ { 0 } - c ) = - ( I - E ) \gamma _ { p } + \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) \ ,
$$

Since $E d _ { p } ( x _ { 0 } ) = 0$ , this relation is satisfied in particular if

$$
\epsilon _ { 0 } - c = - \left( I - E \right) \gamma _ { p } + \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) \ .
$$

The numbers $\epsilon _ { n } - c$ are now determined by the recurrencc relation (ib)

$$
\begin{array} { l } { { \displaystyle { \mathrm {  ~ \Sigma ~ } ^ { \prime } } \mathrm {  ~ \Sigma ~ } ^ { \epsilon } } _ { n } - c = S ^ { n } ( \epsilon _ { 0 } - c ) - \sum _ { j = 1 } ^ { n } S ^ { n - j } \mathfrak { d } _ { j - 1 } ^ { p } } \\ { \displaystyle { \mathrm {  ~ \Sigma ~ } } } \\ { { \displaystyle { \mathrm {  ~ \Sigma ~ } } ^ { \epsilon } \left( \epsilon _ { 0 } - c \right) + \left( S - E \right) ^ { n } \left( \epsilon _ { 0 } - c \right) - E \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p } + E \sum _ { j = n } ^ { \infty } \mathfrak { d } _ { j } ^ { p } - \sum _ { j = 1 } ^ { n } \left( S - E \right) ^ { n - j } \mathfrak { d } _ { j - 1 } ^ { p } } } \end{array}
$$

where we have used $S ^ { n } = E + ( S - E ) ^ { n }$ . If we put

$$
c = E \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p }
$$

the sequence $\{ \epsilon _ { n } \}$ defined above satisfies $\scriptstyle \epsilon _ { n } = 0 ( \rho ^ { n } )$ ,since $E \left( \epsilon _ { 0 } - c \right) = 0$ by (9.14) and since $\ S _ { n } ^ { p } { = } \mathbf { 0 } ( \boldsymbol { \rho } ^ { n } )$

In order to find $e \left( x \right)$ we define

$$
\nu ( x ) = E e ( x ) .
$$

With the help of Formulas (9.15) and (9.13) we can recover $e \left( x \right)$ from $\nu ( x )$ by

$$
e ( x ) = \nu ( x ) - ( I { - } S { + } E ) ^ { - 1 } d _ { p } ( x ) ~ .
$$

Equation (ii) can now be rewritten as the differential equation

$$
\nu ^ { \prime } ( x ) = E G \left( x \right) \left( \nu \left( x \right) - \left( I - S + E \right) ^ { - 1 } d _ { p } \left( x \right) \right) - E d _ { p + 1 } ( x ) \ ,
$$

and Condition (i) yields the starting value $\nu \left( x _ { 0 } \right) { = } { - } E \left( \gamma _ { p _ { . } } { + } \varepsilon _ { 0 } \right)$ . This initial value problem can be solved for $\nu \left( x \right)$ and we obtain $e \left( x \right)$ by (9.16). This function and the $\epsilon _ { n }$ defined above represent a solution of (i)-(ii). QED.

Remarks: a) It follows from (9.15)-(9.17) that the principal error term satisfies

$$
\begin{array} { l } { { e _ { p } ^ { \prime } ( x ) = E G ( x ) e _ { p } ( x ) - E d _ { p + 1 } ( x ) - \left( I - S + E \right) ^ { - 1 } d _ { p } ^ { \prime } ( x ) } } \\ { { e _ { p } ( x _ { 0 } ) = - E \gamma _ { p } - E \displaystyle \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p } - \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) . } } \end{array}
$$

b） Since $e _ { p + 1 } ( x )$ is just the principal error term of Method (9.12), it satisfies the differential equation (9.18) with $d _ { j }$ replaced by $\hat { d } _ { j + 1 }$ By an induction argument we therefore have for $j \equiv p$

$$
e _ { j } ^ { \prime } ( x ) = E G ( x ) e _ { j } ( x ) + \mathrm { i n h o m o g e n e i t y } \ ( x ) .
$$

# Weakly stable methods

We next study the asymptotic expansion for stable methods, which are not strictly stable. E.g. the explicit mid-point rule (1.13'), treated in connection with the GBS-algorithm (Section II.9), is of this type. As at the beginning of this section, we apply the mid-point rule to the problem $y \prime { = } { - y }$ ， $y \left( 0 \right) { = } 1$ and consider the following three starting procedures

$$
\begin{array} { l c r c l } { { y _ { 0 } = 1 ~ , ~ } } & { { ~ } } & { { ~ y _ { 1 } = \exp ( - h ) } } \\ { { } } & { { } } & { { } } & { { } } \\ { { y _ { 0 } = 1 ~ , ~ } } & { { ~ y _ { 1 } = 1 - h + \frac { { h ^ { 2 } } } { 2 } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { y _ { 0 } = 1 ~ , ~ } } & { { ~ y _ { 1 } = 1 - h ~ . } } \end{array}
$$

The three pictures on the left of Figure 9.2 show the global error divided by $\hat { h } ^ { 2 }$ For the first two starting procedures we have conver-

![](images/70f37d930b08f2f3615448f281c85bb0eab8fa75c44ace4d2fbaeb16c0514353.jpg)  
Figure 9.2. Asymptotic expansion of the mid-point rule (three different starting procedures)

gence to the function $x e ^ { - x } / 6$ ，while for (9.19c) the divided error $\bar { ( y } _ { n } - y ( x _ { n } ) ) / h ^ { 2 }$ converges to

$$
\begin{array} { l l } { { e ^ { - x } \left( \displaystyle \frac { 2 x - 3 } { 1 2 } - \frac { e ^ { x } } { 4 } \right) \qquad \mathrm { f o r } n \mathrm { e v e n } \ , } } \\ { { e ^ { - x } \left( \displaystyle \frac { 2 x - 3 } { 1 2 } + \frac { e ^ { x } } { 4 } \right) \qquad \mathrm { f o r } n \mathrm { o d d } \ . } } \end{array}
$$

We then subtract the $h ^ { 2 }$ -term from the global error and divide by $h ^ { 3 }$ in the case (9.19a) and by $h ^ { 4 }$ for b) and c). The result is plotted in the pictures on the right of Figure 9.2.

This example nicely illustrates the fact that we no longer have an asymptotic expansion of the form (9.9) or (9.10) but that there exists an expansion if we consider $x _ { n }$ with $n$ even; there exists a different expansion at $x _ { n }$ with $n$ odd (see also Exercise 2 of Section II.9). Similar results for more general methods wil be obtained here.

We say that a method of the form (8.4) is weakly stable, if it is stable, but if the matrix S has, besides $\zeta _ { 1 } = 1$ ， further eigenvalues of modulus 1, say $\zeta _ { 2 } , \ldots , \zeta _ { i } .$ The matrix S therefore has the representation (cf. (8.11))

$$
S = \zeta _ { 1 } E _ { 1 } + \zeta _ { 2 } E _ { 2 } + \cdot \cdot \cdot + \zeta _ { l } E _ { l } + R
$$

where the $E _ { j }$ are the projectors (corresponding to $\zeta _ { j }$ ) and the spectral radius of $R$ satisfies $\rho ( R \ ) < 1$

In what follows we restrict ourselves to the case where all $\boldsymbol { \zeta } _ { j }$ $( j = 1 , \ldots , l )$ are roots of unity. This allows a simple proof for the existence of an asymptotic expansion and is at the same time by far the most important special case. For the general situation we refer to Hairer-Lubich (1984).

Theorem 9.2. Let the method (9.6) wih $\Phi _ { n }$ independent of n be stable, consistent of order $\boldsymbol { p }$ and satisfy A3. If all eigenvalues (of S ) of modulus 1 satisfy $\zeta _ { j } ^ { \ : q } = 1 \ : \ : ( j = 1 \ : , \ldots , l )$ for some positive integer $q$ , then we have an asymptotic expansion of the form ( $\scriptstyle ( 0 ) = e ^ { 2 \pi i / q }$ ）

$$
u _ { n } \ - z _ { n } \ = \ \sum _ { s = 0 } ^ { q - 1 } \mathfrak { u } ^ { n s } \left( e _ { p s } ( x _ { n } ) h ^ { p } \ + \ \cdot \ \cdot \ + e _ { N s } ( x _ { n } ) h ^ { N } \right) \ + E ( n , h ) h ^ { N + 1 }
$$

where the $e _ { j s } ( x )$ are smooth functions and $E \left( n \ , \ h \right)$ is uniformly bounded for $0 < 8 \leq n h \leq c o n s t$

Proof: The essential idea of the proof is to consider $q$ consecutive steps of Method (9.6) as one method over a large step. Puting $\tilde { u } _ { n } = u _ { n q + i } \quad ( 0 \leq i \leq q - 1$ fixed)， ${ \tilde { h } } = q h$ and $\boldsymbol { \tilde { x } } _ { n } = \boldsymbol { x } _ { i } + n \boldsymbol { \tilde { h } }$ ，thismethod becomes

$$
{ \tilde { u } } _ { n + 1 } = S ^ { q } { \tilde { u } } _ { n } + { \tilde { h } } { \tilde { \Phi } } ( { \tilde { x } } _ { n } , { \tilde { u } } _ { n } , { \tilde { h } } )
$$

with a suitably chosen $\tilde { \Phi }$ . E.g. for $q = 2$ we have

$$
\tilde { \Phi } ( \tilde { x } , \tilde { u } , \tilde { h } ) = \frac { 1 } { 2 } s \Phi ( \tilde { x } , \tilde { u } , \frac { \tilde { h } } { 2 } ) + \frac { 1 } { 2 } \Phi \left( \tilde { x } + \frac { \tilde { h } } { 2 } , { \cal S } \tilde { u } + \frac { \tilde { h } } { 2 } \Phi ( \tilde { x } , \tilde { u } , \frac { \tilde { h } } { 2 } ) , \frac { \tilde { h } } { 2 } \right)
$$

The assumption on the eigenvalues implies

$$
\boldsymbol { S } ^ { q } = \boldsymbol { E } _ { 1 } + \cdot \cdot \cdot + \boldsymbol { E } _ { l } + \boldsymbol { R } ^ { q }
$$

so that (9.21) is seen to be a strictly stable method. A straightforward calculation shows that the local error of (9.21) satisfies

$$
\begin{array} { r l } & { \qquad \tilde { d } _ { 0 } = { \bf O } ( h ^ { p } ) } \\ & { \qquad \tilde { d } _ { n + 1 } = ( I + S + \cdot \cdot \cdot + S ^ { q - 1 } ) d _ { p } ( \tilde { x } _ { n } ) h ^ { p } + { \bf O } ( h ^ { p + 1 } ) ~ . } \\ & { \qquad \mathrm { i n g ~ ( 9 . 1 9 ) ~ a n d ~ u s i n g ~ } \xi _ { j } ^ { q } = 1 \mathrm { ~ w e ~ o b t a i n , ~ w i t h ~ } \tilde { E } = E _ { 1 } + \cdot \cdot \cdot + E _ { l } , } \\ & { \qquad \tilde { E } \left( I + S + \cdot \cdot \cdot + S ^ { q - 1 } \right) d _ { p } ( x ) } \\ & { = \tilde { E } \left( I - \tilde { E } + q E _ { 1 } + \underset { j = 2 } { \overset { l } { \sum } } \frac { 1 - \xi _ { j } ^ { q } } { 1 - \xi _ { j } } E _ { j } + \underset { j = 1 } { \overset { q - 1 } { \sum } } R ^ { j } \right) d _ { p } ( x ) = q E _ { 1 } d _ { p } ( x ) ~ , } \end{array}
$$

which vanishes by (8.15). Hence, also Method (9.21) is consistent of order $p$ . All the assumptions of Theorem 9.1 are thus verified for Method (9.21). We therefore obtain

$$
\iota _ { n q + i } - z _ { n q + i } = \tilde { e } _ { p i } ( x _ { n q + i } ) h ^ { p } + \cdot \cdot \cdot + \tilde { e } _ { N i } ( x _ { n q + i } ) h ^ { N } + E _ { i } ( n , h ) h ^ { N + }
$$

where $E _ { i } ( n \ , \ h )$ has the desired boundedness properties. If we define $e _ { j s } ( x )$ as solution of the Vandermonde-type system

$$
\sum _ { s = 0 } ^ { q - 1 } \omega ^ { i s } e _ { j s } ( x ) = \widetilde { e } _ { j i } ( x )
$$

we obtain (9.20). QED.

# The adjoint method

For a method (8.4) the correct value function $z \left( x , h \right)$ , the starting procedure $\Phi ( h )$ and the increment function $\Phi ( x , u , h )$ are usu-ally also defined for negative h (see the examples of Section III.8). As for one-step methods (Section I.8) we shall give here a precise meaning to the numerical solution $\boldsymbol { u } _ { h } \left( \boldsymbol { x } \right)$ for negative h . This then leads in a natural way to the study of asymptotic expansions in even powers of h .

With the notation $\boldsymbol { u } _ { h } ( \boldsymbol { x } ) = \boldsymbol { u } _ { n }$ for $x = x _ { \mathrm { \ell _ { 0 } } } + n h \left( h > 0 \right)$ the method (8.4) becomes

$$
\begin{array} { r } { \begin{array} { r l r } { u _ { h } ( x _ { 0 } ) = \Phi ( h ) } & { { } \quad } & { ( \mathrm { i } \pi ^ { \prime } ) \leq \pi ^ { \prime } \frac { 1 } { h } , } \\ { u _ { h } ( x + h ) = S u _ { h } ( x ) + h \Phi ( x , u _ { h } ( x ) , h ) } & { { } \quad } & { \mathrm { f o r } x = x _ { 0 } + n h . } \end{array} } \end{array}
$$

We first replace $h$ by $- h$ in (9.22) to obtain

$$
\begin{array} { c } { { u _ { - h } ( x _ { 0 } ) = \phi ( - h ) } } \\ { { { } } } \\ { { u _ { - h } ( x - h ) = S u _ { - h } ( x ) - h \Phi ( x , u _ { - h } ( x ) , - h ) } } \end{array}
$$

and then $x$ by $x + h$ which gives

$$
\begin{array} { l } { { u _ { - h } ( x _ { 0 } ) = \phi ( - h ) \nonumber } } \\ { { u _ { - h } ( x ) = S u _ { - h } ( x + h ) - h \Phi ( x + h , u _ { - h } ( x + h ) , - h ) . } } \end{array}
$$

For sufficiently small $^ h$ this equation can be solved for $u _ { - h } ( x + h )$ (implicit function theorem) and we obtain

$$
\begin{array} { c } { { u _ { - h } ( x _ { 0 } ) = \Phi ( - h ) ~ , } } \\ { { u _ { - h } ( x + h ) = S ^ { - 1 } u _ { - h } ( x ) + h \Phi ^ { * } ( x , u _ { - h } ( x ) , h ) ~ . } } \end{array}
$$

The method (9.23),which is again of the form (8.4), is called the adjoint method of (9.22). Its correct value" function is $z ^ { * } ( x , h ) { = } z \left( x , - h \right)$ . Observe that for given S and $\Phi$ the new incre-ment function $\Phi ^ { * }$ is just defined by the pair of formulas

$$
\begin{array} { l } { { \nu = S u - h \Phi ( x + h , u , - h ) } } \\ { { } } \\ { { u = S ^ { - 1 } \nu + h \Phi ^ { * } ( x , \nu , h ) . } } \end{array}
$$

Example 9.3. Consider a linear multistep method with generating functions

$$
{ \displaystyle \rho ( \zeta ) = \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta ^ { j } } , ~ { \displaystyle \sigma \left( \zeta \right) = \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta ^ { j } } ~ .
$$

Then we have

$$
\left( \begin{array} { c c c c c } { { - \alpha _ { k - 1 } / \alpha _ { k } } } & { { - \alpha _ { k - 2 } / \alpha _ { k } } } & { { . . } } & { { . } } & { { - \alpha _ { 0 } / \alpha _ { k } } } \\ { { 1 } } & { { 0 } } & { { . . } } & { { . } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { . } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { . } } & { { 0 } } \\ { { } } & { { } } & { { \vdots } } & { { } } & { { : } } \\ { { } } & { { } } & { { 1 } } & { { 0 } } \end{array} \right) , \Phi ( x , u , h ) = \left( \begin{array} { c } { { 1 } } \\ { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right) \psi ( x , u , h ) .
$$

where $\psi = \psi ( x , u , h )$ is the solution of $( u = ( u _ { k - 1 } , \ldots , u _ { 0 } ) ^ { T } )$

$$
\alpha _ { k } \psi = \sum _ { j = 0 } ^ { k - 1 } 8 _ { j } f \left( x + j h , u _ { j } \right) + \beta _ { k } f \left( x + k h , h \psi - \sum _ { j = 0 } ^ { k - 1 } \frac { \alpha _ { j } } { \alpha _ { k } } u _ { j } \right) .
$$

A straightforward use of the formulas (9.24) shows that

$$
\begin{array} { r l r } { - 1 } & { { } } & { \left( \begin{array} { c c c c } { 0 } & { 1 } & { } & { } & { } \\ { 0 } & { 0 } & { } & { } & { } \\ { \vphantom { \int } 0 } & { \vphantom { \int } 0 } & { \dots } & { 1 } & { } \\ { \vphantom { \int } 0 } & { \dots } & { \dots } & { \dots } & { 1 } \\ { - \alpha _ { k } / \alpha _ { 0 } } & { - \alpha _ { k - 1 } / \alpha _ { 0 } } & { \dots } & { - \alpha _ { 1 } / \alpha _ { 0 } } \end{array} \right) , } & { \Phi ^ { * } ( x , \nu , h ) } & { { } = \left( \begin{array} { c } { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \end{array} \right) \Psi ^ { * } ( x , \nu , h ) } \end{array}
$$

where $\Psi ^ { * } { = } \Psi ^ { * } ( x \ , \nu \ , h )$ (with $\nu = ( \nu _ { 0 } , \ldots , \nu _ { k - 1 } ) ^ { T } )$ is given by

$$
- \alpha _ { 0 } \boldsymbol { \Psi } ^ { * } = \sum _ { j = 0 } ^ { k - 1 } \mathsf { B } _ { k - j } f \left( \boldsymbol { x } + \left( j - k + 1 \right) \boldsymbol { h } , \nu _ { j } \right) + \mathsf { B } _ { 0 } f \left( \boldsymbol { x } + \boldsymbol { h } , \boldsymbol { h } \boldsymbol { \Psi } ^ { * } - \sum _ { j = 0 } ^ { k - 1 } \frac { \alpha _ { k - j } } { \alpha _ { 0 } } \nu _ { j } \right)
$$

This shows that the adjoint method is again a linear multistep method. Its generating polynomials are

$$
\boldsymbol { \rho } ^ { * } ( \zeta ) = - \zeta ^ { k } \rho ( \frac { 1 } { \zeta } ) , \qquad \sigma ^ { * } ( \zeta ) = \zeta ^ { k } \sigma ( \frac { 1 } { \zeta } ) .
$$

Our next aim is to prove that the adjoint method has exactly the same asymptotic expansion as the original method, with h replaced by $- h$ .For this it is necessary that $S ^ { - 1 }$ also be a stable matrix. Therefore all eigenvalues of S must lie on the unit circle.

Theorem 9.4. Let the method (9.22) be stable, consistent of order p and assume that al eigenvalues of $s$ satisfy $\zeta _ { j } ^ { q } { = } 1$ for some positive integer $q$ Then the global error has an asymptotic expansion of the form $\scriptstyle { \hat { ( } } \omega = e ^ { 2 \pi i / q }$ ）

$$
\begin{array} { l } { { { \displaystyle { \stackrel { \prime } { } } } _ { \displaystyle { u _ { h } } } ( x _ { n } ) \stackrel { \prime } { } - z ( x _ { n } , h ) = \sum _ { s = 0 } ^ { q - 1 } \omega ^ { n s } \left( e _ { p s } ( x _ { n } ) h ^ { p } + \cdot \cdot \cdot \cdot + e _ { N s } ( x _ { n } ) h ^ { N } \right) } } \\ { { { } } } \\ { { { \qquad + \ E ( x _ { n } , h ) h ^ { N + 1 } , } } } \end{array}
$$

valid for positive and negative h. The remainder $E \left( x ~ , ~ h \right)$ is uniformly bounded for $\mid h \mid \leq h _ { 0 } a n d x _ { 0 } \leq x \leq { \hat { x } } .$

Proof: As in the proof of Theorem 9.2 we consider $q$ consecutive steps of Method (9.22) as one new method. The assumption on the eigenvalues implies that $S ^ { q } = I =$ identity. Therefore the new method is essentially a one-step method. The only difference is that here the starting procedure and the correct value function may depend on h . A straightforward extension of Theorem 8.5 of Chapter I1 (Exercise 3) implies the existence of an expansion

$$
\begin{array} { r } { u _ { h } ( x _ { n q + i } ) - z ( x _ { n q + i } , h ) = \tilde { e } _ { p i } ( x _ { n q + i } ) h ^ { p } + \cdot \cdot \cdot + \tilde { e } _ { N i } ( x _ { n q + i } ) h ^ { N } } \\ { + E _ { i } ( x _ { n q + i } , h ) h ^ { N + 1 } . \qquad } \end{array}
$$

This expansion is valid for positive and negative $h$ and the remainder $E _ { i } ( x \ , \ h \ )$ is bounded for $\left| h \right. \left| \leq h _ { 0 } \right.$ and $x _ { 0 } \leq x \leq \bar { x }$ . The same argument as in the proof of Theorem 9.2 now leads to the desired expansion. QED.

# Symmetric methods

The definition of symmetry for general linear methods is not as straightforward as for one-step methods. In Example 9.3 we saw that the components of the numerical solution of the adjoint method are in inverse order._Therefore, it is too restrictive to require $\Phi ( h ) { = } \Phi ( - h )$ ， $s = s ^ { - 1 }$ and $\bar { \Phi } { = } { \bar { \Phi } } ^ { * }$

However, for many methods of practical interest the correct value function satisfies a symmetry relation of the form

$$
z \left( x , h \right) = Q z \left( x + q h , - h \right)
$$

where $Q$ is a square matrix and $q$ an integer. This is for instance the case for linear multistep methods, where the correct value function is given by

$$
z \left( x , h \right) = \left( y \left( x + ( k - 1 ) h \right) , \ldots , y \left( x \right) \right) ^ { T } \ ;
$$

the relation (9.27) holds with

$$
{ \cal Q } \ = \ \left( \begin{array} { c c } { { } } & { { 1 } } \\ { { } } & { { . } } \\ { { 1 } } & { { } } \end{array} \right) \qquad \mathrm { a n d } \qquad q \ = k - 1 \ .
$$

Definition 9.5. Suppose that the correct value function satisfies (9.27). Method (9.22) is called symmetric (with respect to (9.27)), if the numerical solution satisfies its analogue

$$
u _ { h } ( x ) = Q u _ { - h } ( x + q h ) \ .
$$

Example 9.6. Consider a linear multistep method and suppose that the generating polynomials of the adjoint method (9.25) satisfy

$$
\begin{array} { r } { \rho ^ { \ast } ( \zeta ) = \rho ( \zeta ) , \qquad \sigma ^ { \ast } ( \zeta ) = \sigma ( \zeta ) . } \end{array}
$$

This is equivalent to the requirement (cf. (3.24))

$$
\alpha _ { k - j } = - \alpha _ { j } \ , \qquad \beta _ { k - j } = \beta _ { j } \ .
$$

A straightforward calculation (using the formulas of Example 9.3) then shows that the symmetry relation (9.29) holds for all ${ { x } \mathord {  } { } _ { \mathrm { { x } } } } _ { 0 } + { { n h } }$ whenever it holds for $x = x _ { 0 } .$ This imposes an additional condition on the starting procedure $\Phi ( h )$ ：

Let us finally demonstrate how Theorem 9.4 can be used to prove asymptotic expansions in even powers of $h$ . Denote by $u _ { h } ^ { j } ( x )$ the $j$ -th component of $u _ { h } ( x )$ . The symmetry relation (9.29) for multistep methods then implies

$$
\begin{array} { r } { \boldsymbol { \mu } _ { - h } ^ { k } ( \boldsymbol { x } ) = \boldsymbol { u } _ { h } ^ { 1 } ( \boldsymbol { x } - ( k - 1 ) h ) , } \end{array}
$$

Furthermore, for any multistep method we have

so that

$$
\begin{array} { c } { { u _ { h } ^ { k } ( x ) = u _ { h } ^ { 1 } ( x - ( k - 1 ) h ) } } \\ { { { } } } \\ { { u _ { h } ^ { k } ( x ) = u _ { - h } ^ { k } ( x ) } } \end{array}
$$

for symmetric methods. As a consequence of Theorem 9.4 the asymptotic expansion of the global error is in even powers of h, whenever the multistep method is symmetric in the sense of Definition 9.5.

# Exercises

1. Consider a strictly stable, $p$ -th order, linear multistep method written in the form (9.6) (see Example 9.3) and set

$$
G ( x ) = \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \ .
$$

a) Prove that

$$
E G \left( x \right) \mathbf { 1 } = \mathbf { 1 } \frac { \partial f } { \partial y } ( x \textrm { , } y ( x ) )
$$

where $\boldsymbol { E }$ is the matrix given by (8.11) and $\mathbf { 1 } = ( 1 , \ldots , 1 ) ^ { T }$

b) Show that the function $e _ { p } ( x )$ in the expansion (9.9) is given by $e _ { p } ( x ) = \mathbb { 1 } \hat { e } _ { p } ( x ) ,$ where

$$
\begin{array} { r } { \hat { e } _ { p } ^ { \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) \hat { e } _ { p } ( x ) - C y ^ { ( p + 1 ) } ( x ) } \end{array}
$$

and $c$ is the error constant (cf. (2.13)). Compute also ${ \partial _ { p } } ( x _ { 0 } )$

2. For the 3-step BDF-method, applied to $y ^ { \prime } { = } { - } y$ ， $y \left( 0 \right) { = } 1$ with start-ing procedure (9.1c), compute the function $e _ { 3 } ( x )$ and the perturbations $\bigl ( \epsilon _ { n } ^ { 3 } \bigr ) _ { n \geq 0 }$ in the expansion (9.4). Compare your result with Figure 9.1.

3. Consider the method

$$
\begin{array} { c } { { u _ { 0 } = \phi ( h ) } } \\ { { \ } } \\ { { u _ { n + 1 } = u _ { n } + h \Phi ( x _ { n } , z _ { n } , h ) } } \end{array}
$$

with correct,value function $z \left( x , h \right)$ ，

a) Prove that the global error has an asymptotic expansion of the form

$$
u _ { n } - z _ { n } = e _ { p } ( x _ { n } ) h ^ { p } + \cdot \cdot \cdot + e _ { N } ( x _ { n } ) h ^ { N } + E ( x _ { n } , h ) h ^ { N + 1 }
$$

where $E \left( x , h \right)$ is uniformly bounded for $0 \leq h \leq h _ { \mathrm { ~ 0 ~ } }$ and $x _ { 0 } \leq x \leq \hat { x }$ b) Show that Theorem 8.5 of Chapter II remains valid for Method (9.31).

4. Let $\rho ^ { * } ( \zeta )$ and $\sigma ^ { * } ( \zeta )$ be given by (9.25). Under the assumption

$$
\begin{array} { r } { \boldsymbol { \mathrm { p } } ^ { * } ( \boldsymbol { \xi } ) = \boldsymbol { C } \boldsymbol { \mathrm { p } } ( \boldsymbol { \xi } ) , \qquad \boldsymbol { \mathrm { \sigma } } ^ { * } ( \boldsymbol { \xi } ) = \boldsymbol { C } \boldsymbol { \mathrm { \sigma } } ( \boldsymbol { \xi } ) , } \end{array}
$$

the symmetry relation (9.29) is satisfied for all ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 } + n h$ whenever it is valid for ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ . What was the reason for setting $C = 1$ in (9.30)?

# I11.10. Multistep methods for second order differential equations

"En 19o4 jeus besoin d'une pareille methode pour calculer les trajectoires des corpuscules electrises dans un champ magnetique, et en essayant diverses methodes deja connues, mais sans les trouver assez commodes pour mon but, je fus conduit moi-méme a elaborer une methode assez simple, dont je me suis servi ensuite."   
(C. Stormer, 1921)

Because of their importance, second order differential equations deserve some additional attention. We already saw in Section I1.13 that for special second order differential equations certain direct onestep methods are more efficient than the classical Runge-Kutta methods. We now investigate whether a similar situation also holds for multistep methods.

Consider the second order differential equation

$$
y \prime \prime = f \left( x , y , y \right)
$$

where y is allowed to be a vector. We rewrite (10.1) in the usual way as a first order system and apply a multistep method

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } = h \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } ^ { \prime } } } \\ { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } ^ { \prime } = h \sum _ { i = 0 } ^ { k } \beta _ { i } f \left( x _ { n + i } , y _ { n + i } , y _ { n + i } ^ { \prime } \right) . } } \end{array}
$$

If the right hand side of the differential equation does not depend on

$$
y \ ^ { \prime \prime } = f \left( x \ , \ y \right) \ ,
$$

it is natural to look for numerical methods which do not involve the first derivative y'. An elimination of $\{ \boldsymbol { y } _ { n } ^ { \prime } \}$ in the equations (10.2)

$$
\sum _ { i = 0 } ^ { 2 k } \hat { \mathbf { \alpha } } _ { i } y _ { n + i } = h ^ { 2 } \sum _ { i = 0 } ^ { 2 k } \hat { \mathbf { \beta } } _ { i } f \left( x _ { n + i } , y _ { n + i } \right)
$$

where the new coefficients &., $\hat { \mathsf { \beta } } _ { i }$ are given by

$$
\sum _ { i = 0 } ^ { 2 k } \hat { \alpha } _ { i } \zeta ^ { i } \ = \ \biggl ( \sum _ { i = 0 } ^ { k } \alpha _ { i } \zeta ^ { i } \biggr ) ^ { 2 } \ , \qquad \sum _ { i = 0 } ^ { 2 k } \hat { \beta } _ { i } \zeta ^ { i } \ = \ \biggl ( \sum _ { i = 0 } ^ { k } \beta _ { i } \zeta ^ { i } \biggr ) ^ { 2 } \ .
$$

In what follows we investigate (10.4) with coefficients that do not necessarily satisfy (10.5). It is hoped to achieve the same order with a smaller step num ber.

# The first methods

"nous avons calcule plus de 120 trajectoires differentes, travail immense qui a exige plus de 45oo heures.."

"Sein Vortrag ist ubrigens ziemlich trocken und langweilig.. (B. Riemann's opinion about Encke, 1847)

Since most differential equations of celestial mechanics are of the form (10.3) it is not surprising that the first atempts at developing special methods for these equations were made by astronomers.

In his treatise on the aurora borealis, C.Stormer (1907) derived a second order differential equation describing the movement of electrical particles in the earth's magnetic field. For his extensive numerical calculations of these trajectories (see the quotation above!) he developed an accurate and simple method as follows: by adding the Taylor series for $y \left( x _ { n } + h \right)$ and $y \left( x _ { n } - h \right)$ we obtain

$$
\prime ( x _ { n } + h ) - 2 y ( x _ { n } ) + y ( x _ { n } - h ) = h ^ { 2 } y \prime \prime ( x _ { n } ) + { \frac { h ^ { 4 } } { 1 2 } } y ^ { ( 4 ) } ( x _ { n } ) + { \frac { h ^ { 6 } } { 3 6 0 } } y ^ { ( 6 ) } ( x _ { n } ) + \cdots
$$

If we insert $y ^ { \prime \prime } ( x _ { n } )$ from the differential equation (10.3) and neglect higher terms, we get

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n }
$$

as a first simple and accurate method, which is sometimes called Stormer's or Encke's method. For greater precision, we replace the higher derivatives of y by central differences of $f$

$$
\begin{array} { l } { { { h ^ { 2 } y ^ { ( 4 ) } ( x _ { n } ) = \Delta ^ { 2 } f _ { n - 1 } - \frac { 1 } { 1 2 } \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot } } } \\ { { { } } } \\ { { { h ^ { 4 } y ^ { ( 6 ) } ( x _ { n } ) = \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot } } } \end{array}
$$

and obtain

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ f _ { n } + \frac { 1 } { 1 2 } \Delta ^ { 2 } f _ { n - 1 } - \frac { 1 } { 2 4 0 } \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot \biggr ] .
$$

This formula is not yet very practical, since the diferences of the $f _ { n + 1 }$ $f _ { n + 2 }$ $\Delta ^ { 2 } f _ { n - 1 } { = } \Delta ^ { 2 } f _ { n - 2 } { + } \Delta ^ { 3 } f _ { n - 3 } { + } \Delta ^ { 4 } f _ { n - 4 } )$ onegets foruequstfon damentale dans notre methode...", C.Stormer, 1907)

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } } } \\ { { \displaystyle \quad = h ^ { 2 } f _ { n } + \frac { h ^ { 2 } } { 1 2 } \biggl [ \Delta ^ { 2 } f _ { n - 2 } + \Delta ^ { 3 } f _ { n - 3 } + \Delta ^ { 4 } f _ { n - 4 } - \frac { 1 } { 2 0 } \Delta ^ { 4 } f _ { n - 4 } \biggr ] . } } \end{array}
$$

"Had the Ast. Ges. Essay been entirely free from numerical blunder.s.,.." (P.H. Cowell and A.C.D. Crommelin, 1910)

Some years later Cowell and Crommelin (1910) used the same ideas to investigate the motion of Halley's comet. They considered one additional term in the series (10.6), namely

$$
\frac { 3 1 } { 6 0 4 8 0 } { \Delta } ^ { 6 } f _ { n - 3 } { \approx } \frac { 1 } { 1 9 5 1 } { { \Delta } ^ { 6 } } f _ { n - 3 } \ .
$$

The direct use of (10.6) in its fourth order version

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \Big [ f _ { n } + \frac { 1 } { 1 2 } \Delta ^ { 2 } f _ { n - 1 } \Big ]
$$

was advocated by B. Numerov (1924, 1927): instead of replacing $\Delta ^ { 2 } f _ { n - 1 }$ bysomething explicit,Numerovtries tosolve thisimplicit nonlinear equation directly for yn +1

# Stormer's problem

"Quand on est suffisamment exerce, on calcule environ   
trois points $\left( R \ , z \right)$ par heure."   
(C. Stormer, 1907)

Suppose that an elementary magnet is situated at the origin and that its axis corresponds to the $z$ -axis. The trajectory $( x \left( s \right) , \ y \left( s \right)$ $z \left( s \right) )$ of an electrical particle in this magnetic field is then given as the solution of (Stormer, 1907)

$$
\begin{array} { l } { { \displaystyle x ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( 3 y z z ^ { \prime } - \big ( 3 z ^ { 2 } - r ^ { 2 } \big ) y \big ) } } \\ { { \displaystyle y ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( \big ( 3 z ^ { 2 } - r ^ { 2 } \big ) x ^ { \prime } - 3 x z z ^ { \prime } \big ) } } \\ { { \displaystyle z ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( 3 x z y ^ { \prime } - 3 y z x ^ { \prime } \big ) } } \end{array}
$$

where $r ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } .$ Introducing the polar coordinates

$$
x \ = R \cos \phi \qquad y \ = R \sin \phi
$$

the system (10.9) becomes equivalent to

$$
{ \begin{array} { l } { { \boldsymbol { R } } ^ { \prime \prime } = \left( { \frac { 2 \gamma } { R } } + { \frac { R } { r ^ { 3 } } } \right) \left( { \frac { 2 \gamma } { R ^ { 2 } } } + { \frac { 3 R ^ { 2 } } { r ^ { 5 } } } - { \frac { 1 } { r ^ { 3 } } } \right) } \\ { z ^ { \prime \prime } = \left( { \frac { 2 \gamma } { R } } + { \frac { R } { r ^ { 3 } } } \right) { \frac { 3 R z } { r ^ { 5 } } } } \end{array} }
$$

![](images/cdaafdb2f0e9c44232b62ddaf6095e96a09f43676fe57f2745773f14f40cdf75.jpg)  
Figure 10.1. Solutions of (10.11a) in the $( R \ , \ z )$ -plane

$$
\phi ^ { \prime } = \left( \frac { 2 \gamma } { R } + \frac { R } { r ^ { 3 } } \right) \frac { 1 } { R }
$$

where $\gamma$ is some constant originating from the integration of $\phi ^ { \prime \prime } .$ The two equations (10.11a) constitute a second order differential equation of type (10.3) (observe that $r ^ { 2 } { = } R ^ { 2 } { + } z ^ { 2 }$ ),which can be solved numerically by the methods of this section. $\boldsymbol { \Phi }$ is then obtained by simple integration of (10.11b). Figure 10.1 shows two solutions of the subsystem (10.11a) with Stormer's original initial values R $\scriptstyle 0 ^ { = 0 . 2 5 7 4 5 3 }$ ， ${ z _ { 0 } } ^ { = 0 . 3 1 4 6 8 7 }$ ， $\gamma = - 0 . 5$ ${ r _ { 0 } } ^ { = \sqrt { R _ { \mathrm { ~ 0 ~ } } ^ { 2 } + z _ { 0 } ^ { 2 } } }$ ， $\scriptstyle Q _ { 0 } = 1 - ( 2 \gamma / R _ { \ 0 } + R _ { \ 0 } / r _ { 0 } ^ { \ 3 } ) ^ { 2 }$ $\stackrel { \scriptscriptstyle - } { R _ { \mathrm { \scriptsize ~ 0 } } ^ { \prime } } = \sqrt { \mathscr { Q } _ { \mathrm { \scriptsize ~ 0 } } } \cos u$ ， $z _ { 0 } ^ { \prime } { = } \sqrt { Q _ { 0 } } \sin \imath$ with $u \in \{ 0 , \pi / 4 , \pi , 5 \pi / 4 \}$ Figure 10.2 shows a three-dimensional view in $( x , y , z )$ of the solution with initial values $u = \pi / 4$ and $5 \pi / 4$

# Higher order methods

A generalization of St8rmer's formula can be derived as follows: integrating equation (10.3) twice we obtain

$$
y \left( x + h \right) = y \left( x \right) + h y ^ { \prime } ( x ) + h ^ { 2 } { \intop _ { 0 } ^ { 1 } { \left( 1 - s \right) } f \left( x + s h , y \left( x + s h \right) \right) } d s .
$$

![](images/fcf41424547f24f6378624e43744f0722921f3f2a41d9868297a89adcfc30664.jpg)  
Figure 10.2. Three dimensional view of the solution

In order to eliminate the first derivative of $y \left( x \right)$ we write the same formula with $h$ replaced by $- h$ and add the two expressions:

$$
\begin{array} { r l r } {  { y ( x + h ) - 2 y ( x ) + y ( x - h ) } } & { \mathrm { ( 1 0 . 1 3 ) } } \\ & { } & { = \displaystyle h ^ { 2 } \int ( 1 - s ) [ f ( x + s h , y ( x + s h ) ) + f ( x - s h , y ( x - s h ) ) ] d s . } \\ & { } & \end{array}
$$

As in the derivation of the Adams formulas (Section II.1) we replace the unknown function $f \left( t , y \left( t \right) \right)$ by the interpolation polynomial $p \left( t \right)$ of Formula (1.4). This yields the explicit method

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { k - 1 } \sigma _ { j } \nabla ^ { j } f _ { n }
$$

with coefficien ts $\mathrm { ~ \bf ~ \sigma ~ } _ { j }$ given by

$$
\sigma _ { j } \ = \ ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { } \big ( 1 { - } s \big ) \Bigg [ \left( { - } _ { j } ^ { s } \right) + \ \binom { s } { j } \Bigg ] d s .
$$

See Table 10.1 for their numerical values and Exercise 2 for their computation.

Table 10.1. Coefficients of the method (10.14)   

<table><tr><td>j</td><td>0 1 2</td><td>3 4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>oj</td><td>1 1 0</td><td>1 12 12</td><td>19 3 240 40</td><td>863 12096</td><td>275 4032</td></tr></table>

Special cases of (10.14) are

$$
\begin{array} { r l r } { \mathrm { ~ } } & { = 2 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n } \phantom { \frac { 1 } { 1 2 } } \qquad \mathrm { ~ } ( 1 0 . 1 \times n ) } \\ { \mathrm { ~ } } & { = 3 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 1 3 } { 1 2 } f _ { n } - \frac { 1 } { 6 } f _ { n - 1 } + \frac { 1 } { 1 2 } f _ { n - 2 } \biggr ] \phantom { \frac { 1 } { 1 2 } } } \\ { \mathrm { ~ } } & { = 4 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 7 } { 6 } f _ { n } - \frac { 5 } { 1 2 } f _ { n - 1 } + \frac { 1 } { 3 } f _ { n - 2 } - \frac { 1 } { 1 2 } f _ { n - 1 } \biggr ] \phantom { \frac { 1 } { 1 2 } } } \end{array}
$$

Method (10.14) with $k = 5$ is equivalent to Formula (10.7), the method used by Stormer (1907, 1921),and for $k = 6$ one obtains the method used by Cowell and Crom melin (1910). The simplest of these methods ( $k = 1 \AA$ ） has been successfully applied as the basis of an ex trapolation method (Section II.13, Formula (13.32)).

To obtain higher accuracy one can also use the interpolation polynomial $p ^ { * } ( t )$ of (1.7)， which passes through the additional point $( x _ { n + 1 } , f _ { n + 1 } )$ Replacing $f \left( t , y \left( t \right) \right)$ by $\boldsymbol { p } ^ { * } ( t )$ in (10.13） yields the implicit method

$$
\begin{array} { l } { { \mathrm { { } } ^ { \mathrm { { 0 0 } } } } } \\ { { \displaystyle { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \sigma _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 } } . } } \end{array}
$$

The coefficients $\sigma _ { j } ^ { * }$ are defined by

$$
\displaystyle \sigma _ { j } ^ { * } = ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } \left( 1 - s \right) \left[ \left( { - s + 1 \atop j } \right) + \left( { s + 1 \atop j } \right) \right] d s
$$

and are given in Tabie 10.2 for $j \le 6$ 。

For $k = 2$ (and also $k = 3$ ) one obtains the interesting method

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 1 } { 1 2 } f _ { n + 1 } + \frac { 1 0 } { 1 2 } f _ { n } + \frac { 1 } { 1 2 } f _ { n - 1 } \biggr ] \ ,
$$

which is generally attributed to Numerov.

Further methods can be derived by using the ideas of Nyström and Milne for first order equations. With the substitutions $h  2 h$ ， $2 s  s$ and $x \to x - h$ Formula (10.13) becomes

Table 10.2. Coefficients of the implicit method (10.16)   

<table><tr><td>j</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>水） 9</td><td>1 -1</td><td>1 0 12</td><td>-1 240</td><td>-1 240</td><td>-221 60480</td><td>-19 6048</td></tr></table>

$$
\begin{array} { l } { { y \left( x + h \right) - 2 y \left( x - h \right) + y \left( x - 3 h \right) = h ^ { 2 } \displaystyle \int _ { 0 } ^ { 2 } \left( 2 - s \right) } } \\ { { \left[ f \left( x + \left( s - 1 \right) h , y \left( x + \left( s - 1 \right) h \right) \right) + f \left( x - \left( s + 1 \right) h , y \left( x - \left( s + 1 \right) h \right) \right) \right] d , } } \end{array}
$$

If one replaces $\textstyle f \left( t , y \left( t \right) \right)$ by the polynomial $p \left( t \right)$ (or $p ^ { * } ( t )$ ）one obtains new classes of explicit and implicit methods.

# General form ulation

Our next aim is to study stability, consistency and convergence of general linear multistep methods for (10.3). We write them in the form

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } \ = h ^ { 2 } \sum _ { i = 0 } ^ { k } \beta _ { i } f \left( x _ { n + i } , y _ { n + i } \right) \ .
$$

The generating polynomials of the coefficients $\alpha _ { i }$ and $\mathsf { \beta } _ { i }$ are again denoted by

$$
{ \sf \rho } ( \xi ) = \sum _ { i = 0 } ^ { k } { { { \bf \alpha } _ { i } } \xi ^ { i } } , \qquad { \bf { \sigma } } ( \xi ) = \sum _ { i = 0 } ^ { k } { { \bf \beta } _ { i } } \xi ^ { i } \mathrm { ~ . ~ }
$$

If we apply Method (10.19) to the initial value problem

$$
y ^ { \prime \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y ^ { \prime } \left( x _ { 0 } \right) = y _ { 0 } ^ { \prime }
$$

it is natural to require that the starting values be consistent with both initial values, i.e. that

$$
\frac { y _ { i } - y _ { 0 } - i h y _ { 0 } ^ { \prime } } { h } \preccurlyeq 0 \quad \mathrm { f o r } \ h  \ 0 , \ i = 0 , 1 , \dots , k - 1 .
$$

# The stability condition

In order to get a feeling for the stability condition which is necessary for convergence, we consider the simple problem

$$
y ^ { \prime \prime } = 0 ~ , ~ y _ { 0 } ^ { } = 0 ~ , ~ y _ { 0 } ^ { \prime } = 0 ~ .
$$

Its numerical solution satisfies a linear difference equation with $\rho \left( \zeta \right)$ as characteristic polynomial. The same considerations as in the proof of Theorem 4.2 show that the following condition is necessary for convergence.

Definition 10.1. Method (10.19) is called stable, if the generating polynomial p(&) satisfies:

i) The roots of $\rho \left( \zeta \right)$ lie on or within the unit circle;   
ii) The multiplicity of the roots on the unit circle is at most two.

# A one-step formulation of Method (10.19)

It is possible to develop a theory analguous to that of Sections III.2 - II.4. This is due to Dahlquist (1959) and can also be found in the book of Henrici (1962). We prefer to rewrite (10.19) in the form (8.4) and to apply directly the results of Section I1.8 and I1.9 (cf. Example 8.7). In order to achieve this goal, we could put $\boldsymbol { u } _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ , which seems to be a natural choice. But then the corresponding matrix S does not satisfy the stability condition of Definition 8.8 because of the double roots of modulus 1. To overcome this difficulty we separate these roots. We split the characteristic polynomial $\rho ( \zeta )$ into

$$
\mathsf { p } ( \boldsymbol { \zeta } ) = \mathsf { p } _ { 1 } ( \boldsymbol { \zeta } ) \cdot \mathsf { p } _ { 2 } ( \boldsymbol { \zeta } )
$$

such that both polynomials

$$
{ \mathsf { \rho } } _ { 1 } ( \zeta ) = \sum _ { i = 0 } ^ { l } { \gamma _ { i } \zeta } ^ { i } ~ , \qquad { \mathsf { \rho } } _ { 2 } ( \zeta ) = \sum _ { i = 0 } ^ { m } { \kappa _ { i } \zeta } ^ { i } \qquad ( l + m = k ~ )
$$

possess only simple roots of modulus 1. Without loss of generality we opume the ned ie (2.10 $m \geq \iota$ tand $\alpha _ { \boldsymbol { k } } = \gamma _ { \boldsymbol { l } } = \kappa _ { m } = 1$ WUtig the shift $\boldsymbol { \mathit { E } }$

$$
\rho ( E ) y _ { n } = h ^ { 2 } \sigma ( E ) f _ { n } .
$$

The main idea is to introduce ${ \rho } _ { 2 } ( E ) y _ { n }$ as a new variable, say $h \nu _ { n }$ ,s0 that the multistep formula becomes equivalent to the system

$$
\mathsf { \rho } _ { 1 } ( E ) \nu _ { n } = h \sigma ( E ) f _ { n } \qquad \mathsf { \rho } _ { 2 } ( E ) y _ { n } = h \nu _ { n } \ .
$$

Introducing the vector

$$
\boldsymbol { u } _ { n } = ( \nu _ { n + l - 1 } , , . . . , \nu _ { n } , y _ { n + m - 1 } , . . . , y _ { n } ) ^ { T }
$$

Formula (10.25) can be written as

$$
u _ { n + 1 } = S u _ { n } + h \Phi ( x _ { n } , u _ { n } , h ) 
$$

whe

$$
\begin{array} { r } { \boldsymbol { \mathsf { \Sigma } } \boldsymbol { \mathsf { \Sigma } } = \left( \begin{array} { c c } { G } & { 0 } \\ { 0 } & { K } \end{array} \right) \ , \quad \boldsymbol { \Phi } ( \boldsymbol { x } _ { n } , \boldsymbol { u } _ { n } , \boldsymbol { h } ) = \left( \begin{array} { c } { \boldsymbol { \Psi } ( \boldsymbol { x } _ { n } , \boldsymbol { u } _ { n } , \boldsymbol { h } ) } \\ { 0 } \\ { \boldsymbol { \Psi } ( \boldsymbol { x } _ { n } ) } \\ { 0 } \\ { \boldsymbol { \Psi } _ { n } } \\ { 0 } \end{array} \right) \ , } \end{array}
$$

The matrices $G$ and $K$ are the companion matrices

$$
\begin{array} { r l r } { \mathrm { ~  ~ \gamma ~ } } & { = \left( \begin{array} { c c c c c } { - \gamma _ { l - 1 } - \gamma _ { l - 2 } } & { \cdots } & { \cdots } & { - \gamma _ { 0 } } \\ { 1 } & { 0 } & { \cdots } & { \cdot } & { 0 } \\ { 1 } & { 1 } & { \cdot } & { \cdot } & { 0 } \\ & & { \cdot } & { \cdot } & { 0 } \\ & & & { \vdots } & { \vdots } \\ & & & { 1 } & { 0 } \end{array} \right) ~ , ~ { \cal K } } & { = \left( \begin{array} { c c c c c } { - \kappa _ { m - 1 } - \kappa _ { m - 2 } } & { \cdots } & { \cdot } & { - \gamma _ { 0 } } & { \cdots } & { 0 } \\ { 1 } & { 0 } & { \cdots } & { \cdot } & { 0 } \\ { 1 } & { 1 } & { \cdots } & { \cdot } & { 0 } \\ & & { \vdots } & & { \vdots } \\ & & & { \vdots } & { \vdots } \\ & & & & { \uparrow } & { 0 } \end{array} \right) } \end{array}
$$

and $\psi = \psi ( x _ { n } , u _ { n } , h )$ is implicitly defined by

$$
\Psi = \sum _ { j = 0 } ^ { k - 1 } { \mathsf { \beta } } _ { j } f ( x _ { n } + j h , y _ { n + j } ) + { \mathsf { \beta } } _ { k } f ( x _ { n } + k h , h ^ { 2 } \Psi - \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j } y _ { n + j } ) .
$$

In this formula $\psi$ is written as a function of $x _ { n }$ ， $( y _ { n + k - 1 } , \dots , y _ { n } )$ and $h$ But the second relation of (10.25) shows that each value yn +k-1' \*\* , $y _ { n + m }$ can be expressd as alinear combination of the elements of $u _ { n }$ Therefore $\Psi$ is in fact a function of $( x _ { n } , u _ { n } , h )$ ·

Formula (10.26) defines our forward step procedure. The corresponding starting procedure is

$$
\boldsymbol { \Phi } ( h ) = \bigl ( \nu _ { l - 1 } , \ldots , \nu _ { 0 } , y _ { m - 1 } , \ldots , y _ { 0 } \bigr ) ^ { T }
$$

which,by (10.25)，is uniquely determined by $( y _ { k - 1 } , \dots , y _ { 0 } ) ^ { T }$ As correct value function we have

$$
\begin{array} { r } { z \left( x , h \right) = \left( \displaystyle \frac { 1 } { h } \mathsf { \rho } _ { 2 } ( E ) y \left( x + ( l - 1 ) h \right) , \ldots , \displaystyle \frac { 1 } { h } \mathsf { \rho } _ { 2 } ( E ) y \left( x \right) , \right) } \\ { y \left( x + ( m - 1 ) h , \ldots , y \left( x \right) \right) ^ { T } \ . } \end{array}
$$

By our choice of ${ \sf p } _ { 1 } ( \boldsymbol { \zeta } )$ and ${ \mathfrak { p } } _ { 2 } ( \zeta )$ (both have only simple roots of modulus 1） the matrices $G$ and $K$ are power bounded. Therefore S is also power bounded and Method (10.26) is stable in the sense of Definition 8.8.

# Consistency and con vergence

We search for conditions on the parameters $\alpha _ { i }$ and $\beta _ { i }$ , such that the method (10.26) is consistent of order $p$ (in the sense of Lemma 8.11). Let us start with the error in the initial values

$$
d _ { 0 } = z ( x _ { 0 } , h ) - \phi ( h ) .
$$

The first l components of this vector are

$$
\qquad \neg \circ _ { 2 } ( E ) y ( x _ { j } ) - \nu _ { j } = { \frac { 1 } { h } } \sum _ { i = 0 } ^ { m } \kappa _ { i } \left( y ( x _ { i + j } ) - y _ { i + j } \right) \qquad j = 0 , \dots , l - 1
$$

and the last m components are just

$$
y ( x _ { j } ) - y _ { j } \qquad j = 0 , . . . , m - 1 .
$$

We see that a sufficient condition for $d _ { 0 } { = } 0 ( h ^ { p } )$ to hold is

$$
y \left( x _ { j } \right) \sim y _ { j } = { \bf O } ( h ^ { p + 1 } ) \mathrm { f o r } j = 0 , 1 , \ldots , k - 1 .
$$

Consider next the local error at xn ,

$$
d _ { n + 1 } = z \big ( x _ { n } + h , h \big ) - S z \big ( x _ { n } , h \big ) - h \Phi \big ( x _ { n } , z \big ( x _ { n } , h \big ) , h \big ) .
$$

All com ponents of $d _ { n + 1 }$ vanish except the first, which equals

$$
d _ { n + 1 } ^ { ( 1 ) } = { \frac { 1 } { h } } \mathsf { p } ( E ) y ( x _ { n } ) - h \psi ( x _ { n } , z ( x _ { n } , h ) , h ) ~ .
$$

As in Section I1.2 we introduce the linear difference operator

$$
\begin{array} { l } { { L \left( y , x , h \right) = \rho ( E ) y \left( x \right) - h ^ { 2 } \sigma ( E ) y ^ { \prime \prime } ( x ) } } \\ { { \ } } \\ { { \displaystyle = \sum _ { i = 0 } ^ { k } \left( \alpha _ { i } y \left( x + i h \right) - h ^ { 2 } \beta _ { i } y ^ { \prime \prime } ( x + i h ) \right) . } } \end{array}
$$

Using Formula (10.28), an application of the mean value theorem yields

$$
d _ { n + 1 } ^ { ( 1 ) } = \frac { 1 } { h } L ( y , x _ { n } , h ) + h ^ { 2 } \mathsf { \& } f ^ { \prime } ( x _ { n + k } , \eta ) \cdot d _ { n + 1 } ^ { ( 1 ) }
$$

with $\mathbf { \boldsymbol { v } }$ as in Lemma 2.2. We therefore have

$$
d _ { n + 1 } = { \bf O } ( h ^ { p + 1 } ) \iff L \left( y , x _ { n } , h \right) = { \bf O } ( h ^ { p + 2 } ) \ .
$$

The Convergence Theorem 8.13 now yields

Theorem 10.2. Suppose that the method (10.19) is stable, that the starting values satisfy (10.29) and that

$$
L \left( y , x , h \right) = 0 ( h ^ { p + 2 } )
$$

for all sufficiently smooth functions $y \left( x \right)$ . Then the method (10.19) converges of order $p$ ,i.e.

$$
\| ~ y ( x _ { n } ) - y _ { n } ~ \| ~ \leq ~ C h ^ { p } ~ f o r ~ O \leq h n \leq C o n s t .
$$

NED.

A useful criterion for the verification of (10.31) is given by

Theorem 10.3. The multistep method (10.19) satisfies (10.31) if and only if the following equivalent conditions hold:

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } = 0 \ , \sum _ { i = 0 } ^ { k } i \alpha _ { i } = 0
$$

$$
\begin{array} { l c l } { { a n d } } & { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } = q ( q { - } 1 ) \sum _ { i = 0 } ^ { k } 8 _ { i } i ^ { q - 2 } } } & { { f o r } } & { { q = 2 , \ldots , p + 1 \ , } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { } } \\ { { \displaystyle \rho ( e ^ { h } ) - h ^ { 2 } \sigma ( e ^ { h } ) = 0 ( h ^ { p + 2 } ) } } & { { f o r } } & { { h  0 \ , } } \\ { { \displaystyle \frac { \rho ( \zeta ) } { ( \log \zeta ) ^ { 2 } } - \sigma ( \zeta ) = \mathbf { 0 } ( ( \zeta { - } 1 ) ^ { p } ) } } & { { f o r } } & { { \zeta {  } 1 \ . } } \end{array}
$$

The proof is the same as for Theorem 2.4 and hence omitted. NED.

Remarks. 1. $\zeta _ { 1 } = 1$ is necessarily a root of $\rho ( \zeta )$ of multiplicity two. Therefore the polynomials ${ \boldsymbol { \rho } } _ { 1 } , ~ { \boldsymbol { \rho } } _ { 2 }$ of (10.24) satisfy ${ \boldsymbol { \rho } } _ { 1 } ( 1 ) = 0$ and ${ \mathsf p } _ { 2 } ( 1 ) = 0$ . The correct value function $z \left( x , h \right)$ thus has a limit for $h  0$ ：

2. As for Adams methods one easily verifies that the method (10.14) is of order $k$ , and (10.16) of order $k + 1$

# Asym ptotic formula for the global error

Assume that the method (10.19) is stable and consistent of order $p \cdot$ The local truncation error of (10.26) is then given by

$$
d _ { n + 1 } = e _ { 1 } h ^ { p + 1 } C _ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } ) + \mathbf { O } ( h ^ { p + 2 } )
$$

with

$$
C _ { p + 2 } = { \frac { 1 } { ( p + 2 ) ! } } \sum _ { i = 0 } ^ { k } \left( { \alpha _ { i } } ^ { p + 2 } - ( p + 2 ) ( p + 1 ) { \beta _ { i } } ^ { p } \right) \ .
$$

Formula (10.32) can be verified by developing $L \left( y , x _ { n } , h \right)$ into a Taylor series in (10.30). An application of Theorem 9.1 (if 1 is the only root of modulus 1 of $\rho ( \zeta )$ ) or of Theorem 9.2 shows that the global error of Method (10.26) is of the form

$$
u _ { h } ( x ) - z ( x , h ) = e ( x ) h ^ { p } + \mathbf { O } ( h ^ { p + 1 } )
$$

where $e \left( x \right)$ is the solution of

$$
e ^ { \prime } ( x ) = E \frac { \partial \Phi } { \partial u } \big ( x , z ( x , 0 ) , 0 \big ) e ( x ) - E e _ { 1 } \cdot C _ { p + 2 } y ^ { ( p + 2 ) } ( x ) \ .
$$

Here $E$ is the matrix defined in (8.12). Since no $h ^ { p }$ -term is present in the local error (10.32),it follows from (9.16) that $e \left( x \right) { = } E e \left( x \right)$ Therefore (see Exercise 4a) this function can be written as

$$
e \left( x \right) = { \binom { \gamma ( x ) \mathbb { 1 } } { \kappa ( x ) \mathbb { 1 } } } .
$$

A straightforward calculation of $\frac { \partial \Phi } { \partial \boldsymbol { u } } ( \boldsymbol { x } , z \left( \boldsymbol { x } , 0 \right) , 0 )$ and $E e _ { 1 }$ (fo1

details see Exercise 4) shows that (10.33) becomes equivalent to the system

$$
\begin{array} { l } { { \gamma ^ { \prime } ( x ) = \displaystyle \frac { \sigma ( 1 ) } { \rho _ { 1 } ^ { \prime } ( 1 ) } \frac { \partial f } { \partial y } ( x , y ( x ) ) \kappa ( x ) - \displaystyle \frac { C _ { p + 2 } } { \rho _ { 1 } ^ { \prime } ( 1 ) } y ^ { ( p + 2 ) } ( x ) } } \\ { { \kappa ^ { \prime } ( x ) = \displaystyle \frac { 1 } { \rho _ { 2 } ^ { \prime } ( 1 ) } \gamma ( x ) . } } \end{array}
$$

Differentiating (10.34b) and inserting $\gamma ^ { \prime } ( x )$ from (10.34a), we finally obtain

$$
\begin{array} { r } { \kappa ^ { \prime \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) \ltimes ( x ) - C y ^ { ( p + 2 ) } ( x ) } \end{array}
$$

with

$$
C \ = \ { \frac { C _ { p + 2 } } { \sigma ( 1 ) } } \ ,
$$

Here we have used the relation $\sigma ( 1 ) { = } \rho _ { 1 } ^ { \prime } ( 1 ) { \cdot } \rho _ { 2 } ^ { \prime } ( 1 )$ which is an immediate consequence of (10.23) and the assumption that the order of the method is at least 1. The constant $c$ in (10.35) is called the error constant of Method (10.19). It plays the same role as (2.13) for first order equations.

Since the last component of the vector $u _ { n }$ is $y _ { n }$ we have the desired result

$$
y _ { n } - y ( x _ { n } ) = \kappa ( x _ { n } ) h ^ { p } +  { \mathbf { O } } ( h ^ { p + 1 } )
$$

with $\kappa ( x )$ satisfying (10.35). Further terms in the asymptotic expansion of the global error can also be obtained by specializing the results of II.9.

# An order barrier for stable methods (10.19)

It is a natural task to look for stable multistep methods (10.19) of highest possible order.

Theorem 10.4. The order p of a stable linear multistep method (10.19) satisfies

$p ~ \leq ~ k + 2$ if k is even, $p \ \leq \ k + 1$ if k is odd.

Theorem 10.5. Stable multistep methods (10.19) of order k +2 are symmetric, i.e.

$$
\alpha _ { j } = \alpha _ { k - j } , \qquad \beta _ { j } = \beta _ { k - j } f o r \ { a l l } j .
$$

The proofs of these two theorems are similar to those of Theorems 3.5 and 3.9. We omit them and refer the reader to the original article of Dahlquist (1959) or to Henrici (1962).

# Rounding errors

Let us briefly discuss a further advantage of the formulation (10.26). Among the many possibilities of implementing a multistep method, consider the following two:

i) Store the values $( y _ { n + k - 1 } , \dots , y _ { n } )$ ） and compute $y _ { n + k }$ directly with Formula (10.19).   
ii) Store $u _ { n }$ and make use of Formula (10.26). We call this a stabilization of (10.19).

Both processes are mathematically equivalent. However, from a computational point of view the two methods are different. For small h the recurrence relation (10.19) is unstable (due to the roots of multiplicity two on the unit circle), whereas the recursion (10.26) is stable (S is power bounded). For an illustration of this difference we apply Stormer's formula (10.14') with $k = 4$ to the problem $y \ ^ { \prime \prime } { = } { - } y$ with $y \left( x \right) = \sin x$ as exact solution. We take the starting values on the exact solution and choose the step size $h = 0 . 0 1$ to keep the truncation error smaller than the rounding errors (single precision with EPSMACH $= 1 . 5 \cdot E - 8 )$ . Figure 10.3 shows the absolute value of the global error for both implementations. The error of the stabilized version is seen to be smaller by a factor of 100. The downward peaks are due to sign-changes in the global error.

![](images/f2418783d56bf70a1200b855c5d2ce821a52e88eeab7b99560e13b97f60eb9f0.jpg)  
Figure 10.3. Rounding errors for the two implementations of Stormer's formula (10.14') with $k = 4$

# Exercises

1. Compute the solution of St8rmer's problem (10.11a) with one ol the methods of this section.

2. a) Show that the generating functions of the coefficients $\boldsymbol { \sigma } _ { i }$ and $\sigma _ { j } ^ { * }$ (defined in (10.15) and (10.17))

$$
S \left( t \right) = \sum _ { j = 0 } ^ { \infty } { { \sigma _ { j } } t ^ { j } } \mathrm { ~ , ~ } \quad S ^ { * } ( t ) = \sum _ { j = 0 } ^ { \infty } { { \sigma _ { j } ^ { * } } t ^ { j } }
$$

satisfy

$$
S ( t ) = \sqrt { \frac { t } { \log ( 1 - t ) } } ) ^ { 2 } \frac { 1 } { 1 - t } S ^ { * } ( t ) = ( \frac { t } { \log ( 1 - t ) } ) ^ { 2 } ,
$$

b) Com pute the coefficients $d _ { j }$ of

$$
\sum _ { j = 0 } ^ { \infty } d _ { j } t ^ { j } = \left( { \frac { \log ( 1 - t ) } { t } } \right) ^ { 2 } = \left( 1 + { \frac { t } { 2 } } + { \frac { t ^ { 2 } } { 3 } } + { \frac { t ^ { 3 } } { 4 } } + \cdot \cdot \cdot \right) ^ { 2 }
$$

and derive a recurrence relation for the $\sigma _ { j }$ and $\sigma _ { j } ^ { * }$

c) Prove that

$$
{ \sigma } _ { j } ^ { * } = { \sigma } _ { j } - { \sigma } _ { j - 1 } .
$$

3. Let p(&) be a polynomial of degree k which has 1 as root of mul-tiplicity 2. Then there exists a unique $\sigma \left( \zeta \right)$ such that the corresponding method is of order $k + 1$

4. Consider the method (10.26) and, for simplicity， assume the differential equation to be a scalar one.

a) For any vector $w$ in $\mathbb { R } ^ { k }$ the im age vector $E w$ ,with $E$ given by (8.12), satisfies

$$
E w \ = \ { \binom { \gamma \mathbb { 1 } } { | \kappa \mathbb { 1 } } }
$$

where $\gamma , \kappa$ are real numbers and 1 is the vector with all elements equal to 1. The dimensions of $\gamma \mathbf { 1 }$ and κll are $l$ and $m$ ,respectively.

b) Verify that fo

$$
\begin{array} { r l } & { \textup { r } e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T } } \\ & { \boldsymbol { E } \left( { \boldsymbol { \alpha } \boldsymbol { e } _ { 1 } } \right) \ = \left( \begin{array} { l } { ( \boldsymbol { \alpha } / \rho _ { 1 } ^ { \prime } ( 1 ) ) \Im } \\ { ( \beta / \rho _ { 2 } ^ { \prime } ( 1 ) ) \Im } \end{array} \right) \ . } \end{array}
$$

c) Show that

$$
\begin{array} { r } { { \cal E } \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \left( { \gamma \bf 1 } \right) = \left( { \bf \Psi } \left( \frac { \sigma ( 1 ) } { \rho _ { 1 } ^ { \prime } ( 1 ) } \right) \bf { \Psi } \times { \bf \ I } \right) } \\ { { \cal E } \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \left( { \gamma \bf 1 } \right) = \left( { \bf \Psi } \left( \frac { 1 } { \rho _ { 2 } ^ { \prime } ( 1 ) } \right) \bf { \Psi } \times { \bf \Psi } \right) } \end{array} .
$$

Hint. With $Y _ { n } { = } ( y _ { n + k - 1 } , { \dots } , y _ { n } ) ^ { T }$ the formula (10.28) expresses $\psi$ as a function of $( x _ { n } , Y _ { n } , h )$ The vectors $Y _ { n }$ and $u _ { n }$ are related by

$$
{ K Y _ { n } } = L { \ * u _ { n } } + \mathbf { O } ( h )
$$

where

$$
\begin{array} { r l r } { K } & { = } & { \left( \begin{array} { l l l l l l } { \kappa _ { m } } & { \hdots } & { \hdots } & { \kappa _ { 0 } } & & & \\ & { \ddots } & & & { \ddots } & \\ & & & & { \ddots } & \\ & & { \kappa _ { m } } & { \hdots } & { \hdots } & { \kappa _ { 0 } } \\ & & & { 1 } & & \\ & & & { \ddots } & \\ & & & & { 1 } \end{array} \right) \qquad L = \left( \begin{array} { l l l l l l } { \hdots } & & { 0 } & & \\ & & { 0 } & \\ & & & & \\ & & & { 1 } & \\ & & & & { \ddots } \\ & & & & & { 1 } \end{array} \right) \qquad . } \end{array}
$$

Usethechain rulefor thecomputationof $\frac { \partial \Psi } { \partial u } ( x , z ( x , 0 ) , 0 ) ,$ See also Exercise 2 of Section III.4 and Exercise 1 of Section III.9.

5. Compute the error constant (10.36) for the methods (10.14) and (10.16).

$\sigma _ { k }$ and ${ \mathfrak {sigma } } _ { k + 1 } ^ { * } ,$

# APPENDIX. FORTRAN CODES

... but the software is in various states of development from experimental (a euphemism for badly written) to what we might cal...   
(W. Gear 1985)

The following Fortran codes have been developped for our numerical computations. They can be obtained from the Authors (Section de Mathematiques, Case Postale 240, CH-1211 Geneve 24, Switzerland) on an IBM diskette. Please send 15 Swiss Franks.

# 1. Dopri5

Explicit Runge-Kutta code based on the formulas of Dormand and Prince with step size control (see Table 4.6 of Section I.4). Best method for low tolerances $1 0 ^ { - 4 }$ to $1 0 ^ { - 7 }$ ）.

SUBROUTINE DOPRI5(N,FCN,X,Y,XEND,EPS,HMAX,H)   
C   
C NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDER   
C ORDINARY DIFFERENTIAL EQUATIONS $\mathbf { Y } ^ { \mathrm { ~ 5 ~ } } = \mathbb { F }$ (X,Y).   
C THIS IS AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER (4)5   
C DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.   
C C.F.SRCTION II.4   
C   
C INPUT PARAMETERS   
C   
C N DIMENSION OF THE SYSTEM （N.LE.51）   
C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THE   
C FIRST DERIVATIVE F(X,Y):   
C SUBROUTINE FCN(N,X,Y,F)   
C RBAL\*4 X,Y(N),F(N)   
C F(1)=.. BTC.   
C X INITIAL X-VALUE   
C XBND FINAL X-VALUE (XRND-X POSITIVE OR NEGATIVE)   
C Y(N) INITIAL VALUES FOR Y   
C BPS LOCAL TOLBRANCE   
C HMAX MAXIMAL STEPSIZE   
C H INITIAL STEPSIZE GUESS   
C   
C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
EXTERNAL SUBROUTINE (TO BR SUPPLIED BY THE USER) SOLOUS THIS SUBROUTINE IS CALLED AFTER EVERY SUCCESSFULLY COMPUTED STBP （AND THE INITIAL VALUE): SUBROUTINE SOLOUS (NR,X,Y,N) RBAL\*4 X,Y(N) FURNISHES THE SOLUTION Y AT THE NR-TH GRID-POINT X (THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTION IS NOT DESIRRD AT THE INTERMEDIATE POINTS. REAL\*4 K1(51),K2(51),K3(51),K4(51),K5(51),Y1(51),Y(N) LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CAN BE USED FOR STATISTICS   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STEPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NREJCT NUMBER OF REJECTED STEPS DATA NMAX/3000/,UROUND/5.E-8/   
C NMAX MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.+UROUND>1.   
C (TO BE ADAPTED BY THE USER) POSNEG=SIGN(1.,XEND-X)   
C INITIAL PRRPARATIONS HMAX=ABS(HMAX) H=AMIN1(AMAX1(1.E-4,ABS(H)),HMAX) H=SIGN(H,POSNEG) EPS=AMAX1(BPS,7.\*UROUND) REJECT=.FALSE. NACCPT=0 NRBJCT=0 NFCN=1 NSTEP=0 CALL SOLOUS(NACCPT+1,X,Y,N) CALl FCN(N,X,Y,K1）   
C BASIC INTEGRATION STEP 1 IF(NSTEP.GT.NMAX.OR.X+.1\*H.EQ.X)GOTO 79 IF（（X-XEND）\*POSNEG+UROUND.GT.O.） RETURN IF(（X+H-XEND)\*POSNEG.GT.O.)H=XEND-X NSTRP=NSTEP+1   
C THE FIRST 6 STAGES D0 22 I=1,N 22 Y1(I)=Y(I)+H\*.2\*K1(I) CALL FCN(N,X+.2\*H,Y1,K2) DO 23 I=1,N 23 Y1(I)=Y(I)+H\*((3./40.)\*K1(I)+(9./40.)\*K2(I)) CALL FCN(N,X+.3\*H,Y1,K3) DO 24 I=1,N 24 Y1(I)=Y(I)+H\*((44./45.)\*K1(I)-(56./15.)\*K2(I)+(32./9.)\*K3(I)) CALL FCN(N,X+.8\*H,Y1,K4) D0 25 I=1,N 25Y1(I)=Y(I)+H\*((19372./6561.)\*K1(I)-(25360./2187.)\*K2(I) &+(64448./6561.)\*K3(I)-(212./729.)\*K4（I)) CALL FCN(N,X+(8./9.)\*H,Y1,K5) D0 26 I=1,N 26Y1(I)=Y(I)+H\*((9017./3168.)\*K1(I)-(355./33.)\*K2(I) & +(46732./5247.)\*K3(I)+(49./176.)\*K4(I)-(5103./18656.)\*K5(I) XPH=X+H CALL FCN(N,XPH,Y1,K2) DO 27 I=1,N 27Y1(I)=Y(I)+H\*((35./384.)\*K1(I)+(500./1113.)\*K3(I) & +(125./192.)\*K4(I)-(2187./6784.)\*K5(I)+(11./84.)\*K2(I))   
C COMPUTE INTERMEDIATE SUM TO SAVE MEMORY D0 61 I=1,N 61K2(I)=(71./57600.)\*K1(I)-(71./16695.)\*K3(I) & +(71./1920.)\*K4(I)-(17253./339200.)\*K5(I)+(22./525.)\*K2(I)   
C THE LAST STAGE CALL FCN(N,XPH,Yl,K3) D0 28 I=1,N 28 $\mathrm { ~ K ~ 4 ~ ( ~ I ~ ) ~ } = ( \mathrm { ~ K ~ 2 ~ ( ~ I ~ ) ~ } - ( \mathrm { ~ 1 ~ } , / 4 0 ~ . ~ ) * \mathrm { ~ K ~ 3 ~ ( ~ I ~ ) ~ } ) * \mathrm { ~ H ~ }$ NFCN=NFCN+6   
C ERROR ESTIMATION ERR=0. D0 41 I=1,N DENOM=AMAX1(1.E-5,ABS(Y1(I)),ABS(Y(I)）,2.\*UROUND/EPS) 41 BRR=BRR+(K4(I)/DENOM)\*\*2 BRR=SQRT(ERR/FLOAT(N)) C COMPUTATION OF HNEW C WE REQUIRE .2<=HNEW/H<=10. FAC=AMAX1(.1,AMIN1(5.,(ERR/BPS)\*\*(1./5.)/.9)) HNBW=H/FAC IF(ERR.LE.RPS)THEN C 11i STEP IS ACCEPTED NACCPT=NACCPT+1 DO 44 I=1,N K1(I)=K3(I)   
44 Y(I)=Y1(I) X=XPH CALL SOLOUS(NACCPT+1,X,Y,N) IF（ABS(HNEW).GT.HMAX)HNEW=POSNEG\*HMAX IF(REJECT)HNEW=POSNEG\*AMINI(ABS(HNEW),ABS(H)) REJECT=.FALSE. ELSE C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1)NREJCT=NREJCT+1 END IF H=HNEW GOTO 1 C FAIL EXIT   
79 WRITE(6,979) X   
979 FORMAT(' EXIT OF DOPRI5 AT X=',E11.4) RETURN END C SUBROUTINE SOLOUS(NRPNTS,X,Y,N) REAL\*4 Y(N) RETURN END

# 2. Dopri8

Explicit Runge-Kutta code of high order based on the formulas of Prince and Dorm and with step size control (Table 6.4 of Section I1.6). It is written in double precision and preferable for tolerances between approximately $1 0 ^ { - 7 }$ and $1 0 ^ { - 1 3 }$ Do not use it below $1 0 ^ { - 1 6 }$

SUBROUTINE DOPRI8(N,FCN,X,Y,X&ND,EPS,HMAX,H)NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERORDINARY DIFFERENTIAL EQUATIONS Y'=F(X,Y).THIS IS AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER （7)8DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.C.F. SECTION II.6INPUT PARAMETERSN DIMENSION OF THE SYSTEM （N.LE.51)FCN NAME （EXTERNAL) OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*8 X,Y(N),F(N)F(1)=.. ETC.X INITIAL X-VALUEXEND FINAL X-VALUE (XEND-X POSITIVE OR NRGATIVE)Y(N) INITIAL VALUES FOR YBPS LOCAL TOLERANCEHMA X MAXIMAL STEPSIZEH INITIAL STEPSIZE GUESS

C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
C   
C EXTRRNAL SUBROUTINE (TO BR SUPPLIED BY THE USER)   
C   
C SOLOUT THIS SUBROUTINE IS CALLED AFTER EVERY   
C SUCCESSFULLY COMPUTED STEP (AND THB INITIAL VALUE): SUBROUTINE SOLOUT (NR,X,Y,N) REAL\*8 X,Y(N) FURNISHES THE SOLUTION Y AT THE NR-TH   
GRID-POINT X (THR INITIAL VALUB IS CON-SIDBRED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE，IF THR SOLUTION IS NOT DESIRED AT THE INTERMBDIATE POINTS.   
C IMPLICIT RRAL\*8 （A-H,O-Z) REAL\*8 Kl(51),K2(51),K3(51),K4(51),K5(51),K6(51),K7(51) \*,Y(N),Y1(51) LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CAN BE USED FOR STATISTICS   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STRPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NRBJCT NUMBER OF REJRCTED STEPS COMM0N/CoEF/C2,C3,C4,C5,c6,C7,c8,C9,C10,C11,C12,C13, &A21,A31,A32,A41,A43,A51,A53,A54,A61,A64,A65,A71,A74,A75,A76, &A81,A84,A85,A86,A87,A91,A94,A95,A96,A97,A98,A101,A104,A105,A106, &A107,A108,A109,A111,A114,A115,A116,A117,A118,A119,A1110,A121, &A124,A125,A126,A127,A128,A129,A1210,A1211,A131,A134,A135,A136, &A137,A138,A139,A1310,A1311,B1,B6,B7,B8,B9,B10,BI1,B12,B13, &BH1,BH6,BH7,BH8,BH9,BH1O,BH11,BH12 DATA NMAX/2000/,UROUND/1.73D-18/   
C NMAX MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.D0   
C (TO BE ADAPTED BY THE USER) CALL COEFST POSNEG=DSIGN(1.DO,XEND-X)   
C INITIAL PREPARATIONS HMAX=DABS(HMAX) H=DMIN1(DMAX1(1.D-1O,DABS(H)),HMAX) H=DSIGN(H,POSNEG) EPS=DMAX1(EPS,13.DO\*UROUND) REJECT=.FALSE. NACCPT=0 NREJCT=0 NFCN=0 NSTEP=0 CALL SOLOUT(NACCPT+1,X,Y,N)   
C BASIC INTEGRATION STEP 1 IF(NSTEP.GT.NMAX.OR.X+.03DO\*H.EQ.X)GOTO 79 IF((X-XEND)\*POSNEG+UROUND.GT.O.DO) RETURN IF((X+H-XEND)\*POSNBG.GT.O.DO)H=XEND-X CALL FCN(N,X,Y,K1) 2 CONTINUE NSTEP=NSTEP+1   
C THE FIRST 9 STAGES D0 22 I=1,N 22 Y1(I)=Y(I)+H\*A21\*K1(I) CALL FCN(N,X+C2\*H,Y1,K2) DO 23 I=1,N 23 Y1(I)=Y(I)+H\*(A31\*K1(I)+A32\*K2(I)) CALL FCN(N,X+C3\*H,Y1,K3) D0 24 I=1,N 24 Y1(I)=Y(I)+H\*(A41\*K1(I)+A43\*K3(I)) D0 25 I=1,N 25 Y1(I)=Y(I)+H\*(A51\*K1(I)+A53\*K3(I)+A54\*K4(I)) CALL FCN(N,X+C5\*H,Y1,K5) DO 26 I=1,N 26 Yl(I)=Y(I)+H\*(A61\*K1(I)+A64\*K4(I)+A65\*K5(I)) CALL FCN(N,X+C6\*H,Y1,K6) DO 27 I=1,N 27 Y1(I)=Y(I)+H\*(A71\*K1(I)+A74\*K4(I)+A75\*K5(I)+A76\*K6(I)) CALL FCN(N,X+C7\*H,Y1,K7) DO 28 I=1,N 28 Y1(I)=Y(I)+H\*(A81\*K1(I)+A84\*K4(I)+A85\*K5(I)+A86\*K6(I)+A87\*K7 CALL FCN(N,X+C8\*H,Y1,K2) DO 29 I=1,N 29 Y1(I)=Y(I)+H\*(A91\*K1(I)+A94\*K4(I)+A95\*K5(I)+A96\*K6(I)+A97\*K7. &+A98\*K2（I)) CALL FCN(N,X+C9\*H,Y1,K3) DO 30 I=1,N 30 Y1(I)=Y(I)+H\*(A101\*K1(I)+A104\*K4(I)+A105\*K5(I)+A106\*K6(I) &\~ +A107\*K7(I)+A108\*K2（I)+A109\*K3(I）)   
C COMPUTE INTERMEDIATE SUMS TO SAVE MEMORY DO 61 I=1,N Y11S=A111\*K1(I)+A114\*K4(I)+A115\*K5(I)+A116\*K6(I)+A117\*K7(I) & +A118\*K2（I)+A119\*K3（I） Y12S=A121\*K1(I)+A124\*K4(I)+A125\*K5(I)+A126\*K6(I)+A127\*K7(I) & +A128\*K2(I)+A129\*K3(I) K4(I)=A131\*K1(I)+A134\*K4(I)+A135\*K5(I)+A136\*K6(I)+A137\*K7(I） & +A138\*K2(I)+A139\*K3（I) K5(I)=B1\*K1(I)+B6\*K6(I)+B7\*K7(I)+B8\*K2(I)+B9\*K3(I) K6(I)=BH1\*K1(I)+BH6\*K6(I)+BH7\*K7(I)+BH8\*K2(I)+BH9\*K3（I) K2(I)=Y11S 61 K3(I)=Y12S   
C THE LAST 4 STAGES CALL FCN(N,X+C1O\*H,Yl,K7) D0 31 I=1,N 31 Y1(I)=Y(I)+H\*(K2(I)+A1110\*K7(I)) CALL FCN(N,X+C1I\*H,Yl,K2） XPH=X+H DO 32 I=1,N 32 Y1(I)=Y(I)+H\*(K3(I)+A1210\*K7(I)+A1211\*K2(I)) CALL FCN(N,XPH,Y1,K3) D0 33 I=1,N 33 Y1(I)=Y(I)+H\*(K4(I)+A1310\*K7(I)+A1311\*K2(I)) CALL FCN(N,XPH,Yl,K4) NFCN=NFCN+13 DO 35 I=1,N K5(I)=Y(I)+H\*(K5(I)+B10\*K7(I)+B11\*K2(I)+B12\*K3(I)+B13\*K4(I)) 35K6(I)=Y(I)+H\*(K6(I)+BH10\*K7(I)+BH11\*K2(I)+BH12\*K3(I))   
c BRROR ESTIMATION BRR=0.D0 D0 41 I=1,N DENOM=DMAX1(1.D-6,DABS(K5(I)),DABS(Y(I)),2.DO\*UROUND/BPS) 41 BRR=ERR+((K5(I)-K6(I))/DENOM)\*\*2 BRR=DSQRT(ERR/DFLOAT(N))   
C COMPUTATION OF HNEW   
C WE REQUIRE .333<=HNEW/W<=6. FAC=DMAX1((1.D0/6.DO),DMIN1(3.DO,(ERR/BPS)\*\*(1.D0/8.DO)/.9D0 HNEW=H/FAC IF(ERR.GT.EPS)GOTO 51   
C STEP IS ACCEPTED NACCPT=NACCPT+1 D0 44 I=1,N 44 Y(I)=K5(I) X=XPH CALL SOLOUT(NACCPT+1,X,Y,N) IF（DABS(HNEW) .GT.HMAX) HNEW=POSNEG\*HMAX IF(REJECT) HNEW=POSNEG\*DMINI(DABS(HNEW),DABS(H)) H=HNEW GOTO 1 STEP IS RRJECTED   
51 REJECT=.TRUE. H=HNEW IF(NACCPT.GE.1)NREJCT=NREJCT+1 NFCN=NFCN-1 GOTO 2 FAIL EXIT   
79 WRITE(6,979)X   
379 FORMAT(' EXIT OF DOPRI8 AT X=',D16. RETURN END SUBROUTINE COEFST THIS SUBROUTINE SETS THE COEFFICIEN' METHOD OF ORDER 8 WITH ERROR BSTIMA IMPLICIT REAL\*8 （A-H,O-Z) COMM0N/COBF/C2,C3,C4,C5,C6,C7,C8,c9 &A21,A31,A32,A41,A43,A51,A53,A54,A6 & A81,A84,A85,A86,A87,A91,A94,A95,A9 & A107,A108,A109,A111,A114,A115,A116 & A124,A125,A126,A127,A128,A129,A121( & A137,A138,A139,A1310,A1311,B1,B6,B‘ & BH1,BH6,BH7,BH8,BH9,BH1O,BH11,BH12 C2=1.D0/18.D0 C3=1.D0/12.D0 C4=1.D0/8.D0 C5=5.D0/16.D0 C6=3.D0/8.D0 C7=59.D0/400.D0 C8=93.D0/200.D0 C9=5490023248.D0/9719169821.D0 C10=13.D0/20.D0 C11=1201146811.D0/1299019798.D0 C12=1.D0 C13=1.D0 A21=C2 A31=1.D0/48.D0 A32=1.D0/16.D0 A41=1.D0/32.D0 A43=3.D0/32.D0 A51=5.D0/16.D0 A53=-75.D0/64.D0 A54=-A53 A61=3.D0/80.D0 A64=3.D0/16.D0 A65=3.D0/20.D0 A71=29443841.D0/614563906.D0 A74=77736538.D0/692538347.D0 A75=-28693883.D0/1125.D6 A76=23124283.D0/18.D8 A81=16016141.D0/946692911.D0 A84=61564180.D0/158732637.D0 A85=22789713.D0/633445777.D0 A86=545815736.D0/2771057229.D0 A87=-180193667.D0/1043307555.D0 A91=39632708.D0/573691083.D0 A94=-433636366.D0/683701615.D0 A95=-421739975.D0/2616292301.D0 A96=100302831.D0/723423059.D0 A97=790204164.D0/839813087.D0 A98=800635310.D0/3783071287.D0 A101=246121993.D0/1340847787.D0 A104=-37695042795.D0/15268766246.D0 A105=-309121744.D0/1061227803.D0

A106=-12992083.D0/490766935.D0  
A107=6005943493.D0/2108947869.D0  
A108=393006217.D0/1396673457.D0  
A109=123872331.D0/1001029789.D0  
A111=-1028468189.D0/846180014.D0  
A114=8478235783.D0/508512852.D0  
A115=1311729495.D0/1432422823.D0  
A116=-10304129995.D0/1701304382.D0  
A117=-48777925059.D0/3047939560.D0  
A118=15336726248.D0/1032824649.D0  
A119=-45442868181.D0/3398467696.D0  
A1110=3065993473.D0/597172653.D0  
A121=185892177.D0/718116043.D0  
A124=-3185094517.D0/667107341.D0  
A125=-477755414.D0/1098053517.D0  
A126=-703635378.D0/230739211.D0  
A127=5731566787.D0/1027545527.D0  
A128=5232866602.D0/850066563.D0  
A129=-4093664535.D0/808688257.D0  
A1210=3962137247.D0/1805957418.D0  
A1211=65686358.D0/487910083.D0  
A131=403863854.D0/491063109.D0  
A134=-5068492393.D0/434740067.D0  
A135=-411421997.D0/543043805.D0  
A136=652783627.D0/914296604.D0  
A137=11173962825.D0/925320556.D0  
A138=-13158990841.D0/6184727034.D0  
A139=3936647629.D0/1978049680.D0  
A1310=-160528059.D0/685178525.D0  
A1311=248638103.D0/1413531060.D0  
B1=14005451.D0/335480064.D0  
B6=-59238493.D0/1068277825.D0  
B7=181606767.D0/758867731.D0  
B8=561292985.D0/797845732.D0  
B9=-1041891430.D0/1371343529.D0  
B10=760417239.D0/1151165299.D0  
B11=118820643.00/751138087.D0  
B12=-528747749.D0/2220607170.D0  
B13=1.D0/4.D0  
BH1=13451932.D0/455176623.D0  
BH6=-808719846.D0/976000145.D0  
BH7=1757004468.D0/5645159321.D0  
BH8=656045339.D0/265891186.D0  
BH9=-3867574721.D0/1518517206.D0  
BH10=465885868.D0/322736535.D0  
BH11=53011238.D0/667516719.D0  
BH12=2.D0/45.D0  
RETURN  
BND

# 3. Odex

Extrapolation code (see Section I.9) with variable order and variable step size, Good for all tolerances, supreme for very high precision (e.g. $1 0 ^ { - 2 0 } \mathrm { o r } 1 0 ^ { - 3 0 } )$

SUBROUTINE ODEX (N,FCN,X,Y,XEND,EPS,HMAX,H)CNUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERORDINARY DIFFERENTIAL EQUATIONS Y'=F(X,Y).THIS IS AN EXTRAPOLATION-ALGORITHM，BASED ON THEEXPLICIT MIDPOINT RULE （WITH STEPSIZE CONTROLC AND ORDER SRLECTION).C C.F. SECTION II.9CC INPUT PARAMETERSCC N DIMENSION OF THE SYSTEM (N.LE.51)C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*8 X,Y(N),F(N)F(1)=... BTC.X INITIAL X-VALUEXEND FINAL X-VALUE （XRND.GT.X)C Y(N) INITIAL VALUES FOR YC EPS LOCAL TOLERANCEC HMAX MAXIMAL STEPSIZEC H INITIAL STEPSIZE GUESSCC OUTPUT PARAMETERSCC Y(N) SOLUTION AT XRNDCC EXTERNAL SUBROUTINE (TO BE SUPPLIED BY THE USER)CC SOLOUT THIS SUBROUTINE IS CALLED AFTER EVERYSUCCESSFULLY COMPUTED STEP (AND THEINITIAL VALUE）:SUBROUTINE SOLOUT (NR,X,Y,N)REAL\*8 X,Y(N)FURNISHES THE SOLUTION Y AT THE NR-THGRID-POINT X （THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT).SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTIONIS NOT DESIRED AT THE INTERMEDIATE POINTS.IMPLICIT REAL\*8 (A-H,O-Z)LOGICAL REJECT,LASTREAL\*8 Y(N)EXTERNAL FCNCOMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTC COMMON STAT CAN BE USED FOR STATISTICSNFCN NUMBER OF FUNCTION EVALUATIONSNSTEP NUMBER OF COMPUTED STEPSNACCPT NUMBER OF ACCEPTED STEPSC NREJCT NUMBER OF REJECTED STEPSCOMMON /EXTABL/ DZ(51),T(9,51),NJ(9),HH(9),W(9),ERR,FAI1 A(9),EPSD4,UROUND,FAC1,FAC2,SAFr2DATA NJ/2,4,6,8,10,12,14,16,18/DATA A/3.D0,7.D0,13.D0,21.D0,31.D0,43.D0,57.D0,73.D0,9DATA NMAX/800/,KM/9/,UROUND/1.73D-18/C NMAX MAXIMAL NUMBRR OF STEPSC UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.D0

(Iv DD AVAIIDU DI InD UUBn)DATA FAC1/2.D-2/,FAC2/4.D0/,FAC3/.9D0/,FAC4/.8D0/DATA SAFB1/.65D0/,SAFE2/.94D0/  
C INITIAL PRRPARATIONSRPSD4=EPS\*SAFE1NSTEP=0NREJCT=0NACCPT=0NFCN=0K=MAXO(3,MINO(8,INT(-DL0G10(BPS)\*.6D0+1.5D0)))H=DMINi(H,HMAX,(XEND-X)/2.D0)CALL SOLOUT (NACCPT+1,X,Y,N)BRR=0.D0W(1)=0.D0RrJECT=.FaLSE.LAST=.FALSE.  
C IS XEND REACHED IN THE NEXT STEP?10 H1=XEND-XIF （H1.LE.UROUND） GO TO 110H=DMINI(H,H1,HMAX)IF （H.GE.H1-UROUND) LAST=.TRUE.CALL FCN(N,X,Y,DZ)NFCN=NFCN+1  
C THE FIRST AND LAST STEPIF （NSTEP.EQ.O.OR.LAST) THENNSTEP=NSTEP+1D0 20 J=1,KKC=JCALL MIDEX(J,X,Y,H,HMAX,N,FCN)20 IF （J.GT.1.AND.ERR.LE.EPS) GO TO 60GO TO 55END IF  
C BASIC INTEGRATION STEP30 CONTINUENSTRP=NSTRP+1IF （NSTEP.GE.NMAX) GO TO 120KC=K-1DO 40 J=1,KC40 CALL MIDEX(J,X,Y,H,HMAX,N,FCN)  
C CONVERGENCE MONITORIF（K.EQ.2.OR.REJECT） GO TO 50IF (ERR.LE.EPS）GO TO 60IF (BRR/BPS.GT.(DFLOAT(NJ(K+1)\*NJ(K))/4.DO)\*\*2) GO TO 10050 CALL MIDRX(K,X,Y,H,HMAX,N,FCN)KC=KIF (ERR.LE.EPS) GO TO 60  
C HOPE FOR CONVERGENCE IN LINE K+155 IF (ERR/EPS.GT.(DFLOAT(NJ(K+1))/2.DO)\*\*2) GO TO 100KC=K+1CALL MIDEX(KC,X,Y,H,HMAX,N,FCN)IF （ERR.GT.EPS) GO TO 100  
C STEP IS ACCEPTED60 X=X+HDO 70 I=1,N70 Y(I)=T(1,I)NACCPT=NACCPT+1CALL SOLOUT (NACCPT+1,X,Y,N)  
C -. - COMPUTE OPTIMAL ORDERIF (KC.EQ.2） THENKOPT=3IF (REJECT) KOPT=2GO TO 80END IFIF (KC.LE.K) THENKOPT=KCIF (W(KC-1).LT.W(KC)\*FAC3) KOPT=KC-1IF (W(KC).LT.W(KC-1)\*FAC3) KOPT=MINO(KC+1,KM-1)BLDAKOPT=KC-1IF （KC.GT.3.AND.W(KC-2).LT.W(KC-1)\*FAC3) KOPT=KC-2IF (W(KC).LT.W(KOPT)\*FAC3) KOPT=MINO(KC,KM-1)END IF  
C AFTER A REJECTED STEP80 IF（REJECT）THENK=MINO(KOPT,KC）H=DMIN1(H,HH(K))REJECT=.FALSE.GO TO 10END IF  
C COMPUTE STEPSIZE FOR NEXT STEPIF （KOPT.LE.KC） THENH=HH(KOPT)ELSBIF （KC.LT.K.AND.W(KC).LT.W(KC-1)\*FAC4) THENH=HH(KC)\*A(KOPT+1)/A(KC)ELSEH=HH(KC)\*A(KOPT)/A(KC)ENDIFBND IFK=KOPTGO TO 10  
C STEP IS REJECTED100 K=MINO(K,KC）IF (K.GT.2.AND.W(K-1).LT.W(K)\*FAC3) K=K-1NREJCT=NREJCT+1H=HH(K)REJECT=.TRUE.GO TO 30  
C SOLUTION EXIT110 CONTINUERETURN  
C FAIL EXIT120 WRITE（6,\*)'MORE THAN ’,NmAx,' STEPS1RETURNEND  
CSUBROUTINE MIDEX(J,X,Y,H,HMAX,N,FCN)  
C THIS SUBROUTINE COMPUTES THE J-TH LINE OF THE  
C EXTRAPOLATION TABLE AND PROVIDES AN ESTIMATION  
C OF THE OPTIMAL STEPSIZEIMPLICIT REAL\*8 (A-H,O-Z）EXTERNAL FCNREAL\*8 Y(N),DY(51),YH1(51),YH2(51)COMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTCOMMON /EXTABL/ DZ(51),T(9,51),NJ(9),HH(9),W(9),ERR,FAC,1 A(9),EPSD4,UROUND,FAC1,FAC2,SAFE2HJ=H/DFLOAT(NJ(J))  
C EULER STARTING STEPDO 30 I=1,NYHI(I)=Y(I)30 YH2(I)=Y(I)+HJ\*DZ(I)  
C EXPLICIT MIDPOINT RULEM=NJ(J)-1D0 35 MM=1,MCALL FCN(N,X+HJ\*DFLOAT(MM),YH2,DY)D0 35 I=1,NYS=YH1(I)YH1(I) =YH2(I)35 YH2(I)=YS+2.DO\*HJ\*DY(I)  
C FINAL SMOOTHING STEPCALL FCN(N,X+H,YH2,DY)D0 40 $\mathbb { Z } = 1$ ,N40 T(J,I)=(YH1(I)+YH2(I)+HJ\*DY(I))/2.D0NFCN=NFCN+NJ(J）  
C --- POLYNOMIAL EXTRAPOLATIONIF （J.EQ.1) RETURNDO 60 L=J,2,-1FAC=(DFLOAT(NJ(J))/DFLOAT(NJ(L-1)))\*\*2-1.D0DO 60 I=1,NT(L-1,I)=T(L,I)+(T(L,I)-T(L-1,I))/FAC60 CONTINUEERR=0.D0D0 65 I=k,N  
C 一 SCALINGSCAL=DMAX1(DABS(Y(I)),DABS(T(1,I)),1.D-6,UROUND/EPSD4)65 BRR=BRR+((T(1,I)-T(2,I))/SCAL)\*\*2BRR=DSQRT(ERR/DFLOAT(N))  
C 一 COMPUTR OPTIMAL STEPSIZESBXPO=1.D0/DFLOAT(2\*J-1)FACMIN=FAC1\*\*EXPOFAC=DMINI(FAC2/FACMIN,DMAXI(FACMIN,(ERR/EPSD4)\*\*EXPO/SAFE2）)FAC=1.D0/FACHH(J)=DMINI（H\*FAC,HMAX)W(J)=A(J)/HH(J)RETURNBND  
CSUBROUTINE SOLOUT (NRPNTS,X,Y,N)IMPLICIT REAL\*8 (A-H,O-Z)REAL\*8 Y(N)RETURNEND

# 4. Odex2

Extrapolation code (see Section II.13) with variable order and variable step size for second order diferential systems of the form y $\prime \prime = f \left( x , y \right)$ Good for all tolerances.

SUBROUTINE ODEX2 (N,FCN,X,Y,YP,XEND,EPS,HMAX,H)CC NUMERICAL SOLUTION OF A SYSTEM OF SECOND ORDERC ORDINARY DIFFERENTIAL EQUATIONS Y"=F(X,Y).C THIS IS AN EXTRAPOLATION-ALGORITHM， BASED ON THEC EXPLICIT MIDPOINT RULE （WITH STEPSIZE CONTROLC AND ORDER SELECTION).C C.F. SECTION II.13CC INPUT PARAMETERSCC N DIMENSION OF THE SYSTEM （N.LE.51）C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEC SECOND DERIVATIVE F(X,Y):C SUBROUTINE FCN(N,X,Y,F)C REAL\*8 X,Y(N),F(N)C F(1)=... ETC.C X INITIAL X-VALUEC X BND FINAL X-VALUE (XEND.GT.X)C Y(N) INITIAL VALUES FOR YC YP(N) INITIAL VALUES FOR Y'C EPS LOCAL TOLERANCEC HMAX MAXIMAL STEPSIZEC H INITIAL STRPSIZE GUESSCC OUTPUT PARAMETERSCC Y(N) SOLUTION AT XENDC YP(N) DERIVATIVE OF SOLUTION AT XENDC

SUCCESSFULLY COMPUTED STEP (AND THEINITIAL VALUE):SUBROUTINE SOLUT2 (NR,X,Y,YP,N)REAL\*8 X,Y(N),YP(N)FURNISHES THE SOLUTION (Y,YP) AT THE NR-THGRID-POINT X (THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT).SUPPLY A DUMMY SUBROUTINE，IF THE SOLUTIONIS NOT DESIRED AT THE INTERMEDIATE POINTS.IMPLICIT REAL\*8 (A-H,O-Z)LOGICAL REJECT,LASTREAL\*8 Y(N),YP(N)EXTERNAL FCNCOMMON /STAT/NFCN,NSTEP,NACCPT,NREJCT  
C COMMON STAT CAN BE USED FOR STATISTICS  
C NFCN NUMBER OF FUNCTION EVALUATIONS  
C NSTBP NUMBER OF COMPUTED STEPS  
C NACCPT NUMBER OF ACCEPTED STEPS  
C NREJCT NUMBER OF REJECTED STEPSCOMMON /EXTABL/ DZ(51),T(9,51),TP(9,51),NJ(9),HH(9),W(9),BRR,F.A(9),rPSD4,UROUND,FACi,FAC2,SAFE2DATA NJ/2,4,6,8,10,12,14,16,18/DATA A/2.00,4.D0,7.00,11.00,16.D0,22.D0,29.D0,37.D0,46.D0/DATA NMAX/800/,KM/9/,UROUND/1.73D-18/  
C NMAX MAXIMAL NUMBER OF STEPS  
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.DO  
C (TO BE ADAPTED BY THE USER)DATA FAC1/2.D-2/,FAC2/4.D0/,FAC3/.9D0/,FAC4/.8D0/DATA SAFB1/.65D0/,SAFE2/.94D0/  
C INITIAL PRRPARATIONSBPSD4=EPS\*SAFE1NSTEP=0NREJCT=0NACCPT=0NFCN=0K=MAXO(3,MINO(8,INT(-DLOG10(EPS)\*.6D0+1.5D0)))H=DMINl(H,HMAX,(XBND-X)/2.D0)CALL SOLUT2 (NACCPT+1,X,Y,YP,N)ERR=0.D0W(1)=0.D0REJECT=.FALSE.LAST=.FALSE.  
C IS XEND REACHBD IN THE NEXT STEP?10 H1=XEND-XIF （HI.LE.UROUND） GO TO 110H=DMIN1(H,Hl,HMAX)IF（H.GR.HI-UROUND） LAST=.TRUE.CALL FCN(N,X,Y,DZ)NFCN=NFCN+1  
C THE FIRST AND LAST STEPIF （NSTEP.EQ.O.OR.LAST) THENNSTEP=NSTEP+1DO 20 J=1,KKC=JCALL STOERM(J,x,Y,YP,H,HMAX,N,FCN)20 IF（J.GT.1.AND.ERR.LR.EPS)GO TO 60GO T0 55BND IF  
C BASIC INTEGRATION STRP30 CONTINUENSTEP=NSTEP+1IF （NSTBP.GE.NMAX) GO TO 120KC=K-1D0 40 J=1,KC40 CALl STOERM(J,X,Y,YP,H,HMAX,N,FCN)  
C CONVERGENCE MONITORIF （K.EQ.2.OR.REJECT) GO TO 50IF (ERR.LE.EPS) GO TO 60IF (ERR/EPS.GT.(DFLOAT(NJ(K+1)\*NJ(K))/4.DO)\*\*2) GO TO50 CALL STOERM(K,X,Y,YP,H,HMAX,N,FCN)KC=KIF （ERR.LE.EPS) GO TO 60  
C HOPE FOR CONVERGBNCE IN LINE K+155 IF (BRR/BPS.GT.(DFLOAT(NJ(K+1))/2.DO)\*\*2) GO TO 100KC=K+1CALL STOERM(KC,X,Y,YP,H,HMAX,N,FCN)IF (ERR.GT.EPS) GO TO 100  
C STEP IS ACCEPTED60 X=X+HDO 70 I=1,NYP(I)=TP(1,I)70 Y(I)=T(1,I)NACCPT=NACCPT+1CALL SOLUT2 (NACCPT+1,X,Y,YP,N)  
C COMPUTE OPTIMAL ORDERIF (KC.EQ.2) THBNKOPT=3IF （REJECT） KOPT=2GO TO 80END IFIF (KC.LE.K) THENKOPT=KCIF(W(KC-1).LT.W(KC)\*FAC3) KOPT=KC-1IF (W(KC).LT.W(KC-1)\*FAC3) KOPT=MINO(KC+1,KM-1)ELSEKOPT=KC-1IF（KC.GT.3.AND.W(KC-2).LT.W(KC-1)\*FAC3) KOPT=KC-2IF(W(KC).LT.W(KOPT)\*FAC3)KOPT=MINO(KC,KM-1)END IF  
C AFTER A REJECTED STEP80 IF（REJECT） THENK=MINO(KOPT,KC)H=DMINi(H,HH(K))REJECT=.FALSR.GO TO 10BND IF  
C COMPUTR STEPSIZE FOR NEXT STEPIF（KOPT.LR.KC) THBNH=HH(KOPT)BLSEIF （KC.LT.K.AND.W(KC).LT.W(KC-1)\*FAC4) THENH=HH(KC)\*A(KOPT+1)/A(KC)ELSEH=HH(KC)\*A(KOPT)/A(KC)BNDIFBND IFK=KOPTGO TO 10  
C STRP IS REJECTrD  
100 K=MINO(K,KC)IF (K.GT.2.AND.W(K-1).LT.W(K)\*FAC3) K=K-1NRBJCT=NRBJCT+1H=HH(K)REJECT=.TRUE.GO TO 30  
C SOLUTION EXIT  
110 CONTINUERBTURN  
C FAIL EXIT  
120 WRITB(6,\*） MORE THAN',NMAX,’ STEPSRBTURNBNDSUBROUTINE STOERM(J,X,Y,YP,H,HMAX,N,FCN)  
C THIS SUBROUTINE COMPUTES THE J-TH LINE OF THE  
C EXTRAPOLATION TABLE AND PROVIDES AN ESTIMATION  
C OF THE OPTIMAL STEPSIZEIMPLICIT REAL\*8 (A-H,O-Z)EXTERNAL FCNREAL\*8 Y(N),YP(N),DY(5l),YHl(51),ZHl(51)COMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTCOMMON /EXTABL/ DZ(51),T(9,51),TP(9,51),NJ(9),HH(9),W(9),ERR,FA1 A(9),BPSD4,UROUND,FACl,FAC2,SAFE2HJ=H/DFLOAT(NJ(J))HJ2=HJ\*2.D0  
C EULER STARTING STEPDO 30 I=1.NYH1(I)=Y(I)30 ZH1(I)=YP(I)+HJ\*DZ(I)  
C EXPLICIT MIDPOINT (STOBRMER) RULEM=NJ(J)/2-1IF (J.EQ.1) GO TO 37D0 35 MM=1,MDO 33 I-1,N33 YH1(I)=YHi(I)+HJ2\*ZHl（I)CALL FCN(N,X+HJ2\*DFLOAT(MM),YH1,DY)DO 35 I=1,N35 ZHl(I)=ZH1(I)+HJ2\*DY(I)  
C FINAL STEP37 CONTINUEDO 40 I=1,N40 YHl(I)=YH1(I)+HJ2\*ZH1(I)CALL FCN(N,X+H,YHl,DY)D0 43 I=1,NT(J,I)=YH1(I)43 TP(J,I)=ZHi(I)+HJ\*DY(I)NFCN=NFCN+M+1  
C POLYNOMIAL EXTRAPOLATIONIF (J.BQ.1）RRTURND0 60 L=J,2,-1FAC=(DFLOAT(NJ(J))/DFLOAT(NJ(L-1)))\*\*2-1.D0DO 60 I=1,NT(L-1,I)=T(L,I)+(T(L,I)-T(L-1,I))/FACTP(L-1,I)=TP(L,I)+(TP(L,I)-TP(L-1,I))/FAC60 CONTINUEERR=0.D0D0 65 I=1,N  
C SCALINGSCAL=DMAX1(DABS(Y(I)),DABS(T(1,I)),1.D-6,UROUND/BPSD4)SCALP=DMAXi(DABS(YP(I)),DABS(TP(1,I)),1.D-6,UROUND/BPSD4)65 BRR=ERR+((T(1,I)-T(2,I))/SCAL)\*\*2+((TP(1,I)-TP(2,I))/SCALP)\*\*2ERR=DSQRT(ERR/DFLOAT(N\*2))  
C COMPUTE OPTIMAL STEPSIZESRXPO=1.D0/DFLOAT(2\*J-1)FACMIN=FAC1\*\*EXPOFAC=DMINI(FAC2/FACMIN,DMAXI(FACMIN,(RRR/BPSD4)\*\*EXPO/SAFE2))FAC=1.D0/FACHH(J)=DMIN1(H\*FAC,HMAX)W(J)=A(J)/HH(J)RETURNEND  
CSUBROUTINE SOLUT2 (NRPNTS,X,Y,YP,N)IMPLICIT RBAL\*8 (A-H,O-Z）REAL\*8 Y(N),YP(N)RETURNBND

# 5. Doprin

Explicit Runge-Kutta-Nystrom code based on the formulas of Dormand and Prince with step size control (see Table 13.4 of Section 2.13) for second order differential systems of the form y $\mathbf { \Phi } ^ { \prime \prime } = f \left( { \boldsymbol { x } } , { \boldsymbol { y } } \right)$

SUBROUTINE dOPRIN(N,FCN,X,Y,YP,XEND,rPS,HMAX,H)   
NUMERICAL SOLUTION OF A SYSTEM OF SECOND ORDER ORDINARY DIFFERENTIAL EQUATIONS Y"=F(X,Y). THIS IS AN EMBEDDED NYSTROEM METHOD OF ORDER (6)7 DUE TO DORMAND & PRINCE (WITH STEPSIZE CONTROL） C.F. SECTION II.13 INPUT PARAMETERS N DIMENSION OF THE SYSTEM (N.LE.51) FCN NAME （EXTERNAL) OF SUBROUTINE COMPUTING THE SECOND DERIVATIVE F(X,Y): SUBROUTINE FCN(N,X,Y,F) REAL\*8 X,Y(N),F(N) F(1)=... ETC. X INITIAL X-VALUE XEND FINAL X-VALUE (XEND.GT.X) Y(N) INITIAL VALUES FOR Y YP(N) INITIAL VALUES FOR Y' BPS LOCAL TOLERANCE HMA X MAXIMAL STEPSIZE H INITIAL STEPSIZE GURSS OUTPUT PARAMETERS Y(N) SOLUTION AT XEND YP(N) DERIVATIVE OF SOLUTION AT XEND EXTERNAL SUBROUTINE (TO BE SUPPLIED BY THE USER) SOLUT2 THIS SUBROUTINE IS CALLED AFTER EVERY SUCCESSFULLY COMPUTED STEP (AND THE INITIAL VALUE): SUBROUTINE SOLUT2 (NR,X,Y,YP,N) RrAL\*8 X,Y(N),YP(N) FURNISHES THE SOLUTION (Y,YP) AT THE NR-TH GRID-POINT X （THE INITIAL VALUE IS CON-SIDRRED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTION IS NOT DESIRED AT THE INTERMEDIATE POINTS. IMPLICIT REAL\*8 (A-H,O-Z) REAL\*8 K0(51),K1(51),K2(51),K3(51),K4(51),Yl(51),Y(N),YP(N LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT COMMON STaT CAUMBBRUSED FuNcTITATIStIUATIONS NSTRP NUMBER OF COMPUTED STEPS NACCPT NUMBER OF ACCEPTED STEPS NRBJCT NUMBER OF REJECTED STEPS DATA NMAX/2000/,UROUND/1.73D-18/   
C NMA X MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.DO   
C (TO BE ADAPTED BY THE USER) ALPH1=.1D0 ALPH2=.2D0 ALrnJ-3.vv/o.vv ALPH4=.5D0 SQ21=DSQRT(21.D0) ALPH5=(7.D0-SQ21)/14.D0 ALPH6=(7.D0+SQ21)/14.D0 C0=.05D0 C4=16.D0/45.D0 C5=49.D0/180.D0 G10=1.D0/200.D0 G20=1.D0/150.D0 G21=1.D0/75.D0 G30=171.D0/8192.D0 G31=45.D0/4096.D0 G32=315.D0/8192.D0 G40=5.D0/288.D0 G41=25.D0/528.D0 G42=25.D0/672.D0 G43=16.D0/693.D0 G50=(1003.D0-205.D0\*SQ21)/12348.D0 G51=(-18775.D0+4325.D0\*SQ21)/90552.D0 G52=(15600.D0-3425.D0\*SQ21)/43218.D0 G53=(-46208.D0+10112.D0\*SQ21)/237699.D0 G54=(3411.D0-745.D0\*SQ21)/24696.D0 G60=(793.D0+187.D0\*SQ21)/12348.D0 G61=(-8275.D0-2825.D0\*SQ21)/90552.D0 G62=(26100.D0+6175.D0\*SQ21)/43218.D0 G63=-(1905280.D0+483712.D0\*SQ21)/9745659.D0 G64=(3327.D0+797.D0\*SQ21)/24696.D0 G65=-(581.D0+127.D0\*SQ21)/1722.D0 G70=(-157.D0+3.D0\*SQ21)/378.D0 G71=(3575.D0-250.D0\*SQ21)/2772.D0 G72=-(21900.D0+1375.D0\*SQ21)/3969.D0 G73=(1168640.D0+23040.D0\*SQ21)/596673.D0 G74=-(1353.D0+26.D0\*SQ21)/2268.D0 G75=(12439.D0+2639.D0\*SQ21)/4428.D0 G76=(35.D0-7.D0\*SQ21)/36.D0 G80=.05D0 G84=8.D0/45.D0 G85=(49.D0+7.D0\*SQ21)/360.D0 G86=(49.D0-7.D0\*SQ21)/360.D0 POSNEG=DSIGN(1.DO,XEND-X)   
C INITIAL PREPARATIONS HMAX=DABS(HMAX) H=DMIN1(DMAX1(1.D-8,DABS(H)),HMAX) H=DSIGN(H,POSNEG) EPS=DMAX1(RPS,9.DO\*UROUND) REJECT=.FALSE. NACCPT=0 NREJCT=0 NFCN=1 NSTEP=0 CALL SOLUT2(NACCPT+1,X,Y,YP,N) CALL FCN(N,X,Y,KO)   
C BASIC INTEGRATION STEP 1 IF(NSTRP.GT.NMAX.OR.X+.05DO\*H.EQ.X)GOTO 79 IF((X-XEND)\*POSNEG+UROUND.GT.O.DO) RETURN IF((X+H-XEND)\*POSNEG.GT.O.DO)H=XEND-X HP2=H\*H NSTEP=NSTEP+1   
C THE FIRST 5 STAGES D0 21 $\mathbb { I } = 1$ ,N 21 Y1(I)=Y(I)+ALPH1\*H\*YP(I)+HP2\*G10\*KO（I) CALL FCN(N,X+ALPHl\*H,Y1,K1) DO 22 I=1,N 22 Y1(I)=Y(I)+ALPH2\*H\*YP(I)+HP2\*(G20\*K0(I)+G21\*K1(I) CALL FCN(N,X+ALPH2\*H,Yl,K2) DO 23 I=1,N 23 Yl(I)=Y(I)+ALPH3\*H\*YP(I)+HP2\*(G30\*K0(I)+G31\*K1(I)+G32\*K2(I)) CALL FCN(N,X+ALPH3\*H,Y1,K3) DO 24 I=1,N 24 Y1(I)=Y(I)+ALPH4\*H\*YP(I)+HP2\*(G40\*K0(I)+G41\*K1(I)+G42\*K2(I)+ &G43\*K3(I)) CALL FCN(N,X+ALPH4\*H,Yl,K4) D0 25 I=1,N 25Y1(I)=Y(I)+ALPH5\*H\*YP(I)+HP2\*(G50\*K0(I)+G51\*K1(I)+G52\*K2(I)+ & G53\*K3（I)+G54\*K4（I))   
C --COMPUTE INTERMEDIATE SUM TO SAVE MEMORY DO 61 I=1,N Y1S=G60\*K0(I)+G61\*K1(I)+G62\*K2(I)+G63\*K3(I)+G64\*K4（I） K3(I)=G70\*K0(I)+G71\*K1(I)+G72\*K2(I)+G73\*K3(I)+G74\*K4（I) 61 K2(I)=Yls   
C THE LAST 4 STAGES CALL FCN(N,X+ALPH5\*H,Y1,Kl) D0 26 I=1,N 26 Y1(I)=Y(I)+ALPH6\*H\*YP(I)+HP2\*(K2(I)+G65\*K1(I)) CALL FCN(N,X+ALPH6\*H,Y1,K2) DO 27 I=1,N 27 Y1(I)=Y(I)+H\*YP(I)+HP2\*(K3(I)+G75\*K1(I)+G76\*K2(I)) XPH=X+H CALL FCN(N,XPH,Y1,K3) DO 28 I=1,N 28 Y1(I)=Y(I)+H\*YP(I)+HP2\*(G80\*K0(I)+G84\*K4(I)+G85\*K1(I)+G86\*K2（I) DO 30 I=1,N 30 K4(I)=YP(I)+H\*(C0\*(K0(I)+K3(I))+C4\*K4(I)+C5\*(K1(I)+K2(I))) CALL FCN(N,XPH,Y1,K1) DO 33 I=1,N 33 K2(I)=HP2\*(K1(I)-K3(I))/20.D0 NFCN=NFCN+8   
C ERROR ESTIMATION BRR=0.D0 D0 41 I=1,N DENOM=DMAXI(1.D-6,DABS(YI(I)),DABS(Y(I)),2.DO\*UROUND/RPS) 41 ERR=ERR+(K2(I)/DBNOM)\*\*2 ERR=DSQRT(ERR/DFLOAT(N))   
C COMPUTATION OF HNEW   
C WE REQUIRE .2<=HNBW/H<=10. FAC=DMAX1(.1DO,DMIN1(5.DO,(ERR/EPS)\*\*(1.DO/7.DO)/.9D0)) HNEW=H/FAC IF(ERR.LE.RPS)THEN   
C STEP IS ACCEPTED NACCPT=NACCPT+1 DO 44 I=1,N YP(I)=K4(I) KO(I)=K1(I) 44 Y(I)=Y1（I) X=XPH CALL SOLUT2(NACCPT+1,X,Y,YP,N) IF(DABS(HNEW).GT.HMAX) HNEW=POSNBG\*HMAX IF(REJECT)HNEW=POSNEG\*DMINI(DABS(HNEW),DABS(H)) REJECT=.FALSE. ELSE   
C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1) NRRJCT=NREJCT+1 END IF H=HNBW GOTO 1   
C FAIL EXIT 79 WRITE(6,979)X   
979 FORMAT(' EXIT OF DOPRIN AT X=',D16.7) RBTURN END   
SUBROUTINE SOLUT2 (NRPNTS,X,Y,YP,N)   
IMPLICIT REAL\*8 (A-H,O-Z)   
REAL\*8 Y(N),YP(N)   
RETURN   
END

# 6. Retard

Modification of the code DOPRI5 for delay differential equations (see Section I.15). A sample calling program is included. The subroutines STORE and YLAG are also useful for dense output and graphics.

C SAMPLE CALLING PROGRAM FOR RETARDC SOLVING PROBLEM （15.12） WITH SAME INITIAL CONDITIONSC AS FOR TABLE 15.1.DIMENSION Y（1)COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISCCOMMON/STAT/NFCN,NSTEP,NACCPT,NRBJCTEXTERNAL FCN$\mathtt { X 0 } = 0$ ，LAST=0H=0.5Y(1)=0.1Do i I=1,10X=FLOAT(I-1)XEND=FLOAT(I)EPS=1.E-6HMAX=1.CALL RETARD(1,FCN,X,Y,XEND,EPS,HMAX,H)WRITE(6,\*)X,Y(1)WRITE(6,\*) COMMON STAT:',NFCN,NSTEP,NACCPT,NREJC1 CONTINUESTOPENDSUBROUTINE FCN(N,X,Y,F)DIMBNSION Y(N),F(N)EXTERNAL PHIA=1.4F(1)=(A-YLAG(1,X-1.,PHI))\*Y(1)RETURNENDREAL FUNCTION PHI(I,X)IF(I.EQ.1)PHI=O.RETURNENDSUBROUTINE RETARD(N,FCN,X,Y,XEND,EPS,HMAX,H)NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERRETARDED DIFFERENTIAL EQUATIONS Y'=F(X,Y(X),Y(X-TAU),..)。THIS IS BASED ON AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER （4)5DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.C.F. SECTIONS II.5 AND II.15INPUT PARAMRTERSN DIMENSION OF THE SYSTEM （N.LB.51)FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*4 X,Y(N),F(N)EXTERNAL PHI

F(1)=-YLAG(1,X-1.,PHI)+... F(2)=... BTC.   
WHBRE "PHI" IS THE(BXTERNAL) NAME OF   
A REAL FUNCTION COMPUTING THE   
I-TH COMPONBNT OF THE INITIAL FUNCTION PHI（X)   
REAL FUNCTION PHI(I,X)   
IF（I.EQ.1) PHI=... BTC.   
X INITIAL X-VALUE   
C XBND FINAL X-VALUE (XEND>X)   
Y(N) INITIAL VALUES FOR Y   
BPS LOCAL TOLERANCE   
HMAX MAXIMAL STEP SIZE   
C H INITIAL STEP SIZE GUESS   
C   
C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
C   
REAL\*4 K1(51),K2(51),K3(51),K4(51),K5(51),K6(51),K7(51)   
RBAL\*4 Y1(51),Y(N)   
LOGICAL REJECT,DISC   
COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC   
C MEANING OF THESE VARIABLES:   
C IFIRST LOWEST STEP NUMBER STILL IN MEMORY COEF;   
LAST ADDRESS OF LAST DATA WRITTEN BY STORE ON COMMON BLOCK COEF, MUST BE SET TO O IN THE CALLING PROGRAM   
BEFORE THE FIRST CALL.   
x0 INITIAL POINT， MUST BE SET IN THE CALLING PROGRAM   
C BEFORE THE FIRST CALL.   
C X LAST =X+H OF LAST WRITTEN STEP;   
C IPOS POSITION OF LAST SUCCESSFUL SEARCH IN FUNCTION YLAG; C DISC LOGICAL VARIABLE，NECESSARY FOR THE DISTINCTION   
C OF K7 AND KI OF THE FOLLOWING STEP IN THE CASE   
C WHBN Y(XO) IS DIFFERENT FROM PHI(XO).   
COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CONTAINS STATISTICAL INFORMATION:   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STEPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NREJCT NUMBER OF REJECTED STEPS   
COMMON/UROUND/UROUND   
C UROUND SMALLEST NUMBER SATISFYING 1.+UROUND>1.   
C (TO BE ADAPTED BY THE USER)   
DATA UROUND/5.8-8/   
DATA NMAX/3000/   
C NMA X MAXIMAL NUMBER OF STEPS   
C INITIAL PREPARATIONS   
HMAX=ABS(HMAX)   
H=AMIN1(AMAXI(1.E-4,ABS(H)),HMAX)   
H=SIGN(H,1.)   
EPS=AMAX1(BPS,7.\*UROUND）   
RrJrCT=.faLse.   
NACCPT=0   
NRRJCT=0   
NFCN=1   
NSTEP=0   
DISC=.TRUE.   
CALL FCN(N,X,Y,K1)   
IF(.NOT.DISC) CALL FCN(N,X,Y,K1)   
BASIC INTEGRATION STEP   
1 DISC=.TRUE.   
IF(NSTBP.GT.NMAX.OR.X+.1\*H.EQ.X)GOTO 79   
IF((X-XEND)+UROUND.GT.O.）RETURN   
IF((X+H-XBND).GT.O.)H=XEND-X   
NSTEP=NSTRP+1   
C THB 7 RUNGE-KUTTA STAGES   
DO 22 I=1,N   
22 Yl(I)=Y(I)+H\*.2\*Kl(I)   
CALL FCN(N,X+.2\*H,Y1,K2）   
D0 23 I=1,N   
23 Y1(I)=Y(I)+H\*((3./40.)\*K1(I)+(9./40.)\*K2(I))   
CALL FCN(N,X+.3\*H,Y1,K3） 24 Y1(I)=Y(I)+H\*((44./45.)\*K1(I)-(56./15.)\*K2(I)+(32./9.)\*H CALL FCN(N,X+.8\*H,Y1,K4) DO 25 I=1,N 25 Y1(I)=Y(I)+H\*((19372./6561.)\*K1(I)-(25360./2187.)\*K2(I) &+(64448./6561.)\*K3(I)-(212./729.)\*K4(I)) CALL FCN(N,X+(8./9.)\*H,Y1,K5) DO 26 I=1,N" 26 Y1(I)=Y(I)+H\*((9017./3168.)\*K1(I)-(355./33.)\*K2(I) &+(46732./5247.)\*K3(I)+(49./176.)\*K4(I)-(5103./18656. XPH=X+H CALL FCN(N,XPH,Y1,K6) DO 27 I=1,N 27Y1(I)=Y(I)+H\*((35./384.)\*K1(I)+(500./1113.)\*K3(I) & +(125./192.)\*K4(I)-(2187./6784.)\*K5(I)+(11./84.)\*K6( DISC=.TRUE. CALL FCN(N,XPH,Y1,K7） D0 28 I=1,N 28 K2(I)=((71./57600.)\*K1(I)-(71./16695.)\*K3(I)+(71./1920. & -(17253./339200.)\*K5(I)+(22./525.)\*K6(I)-(1./40.)\*K7 NFCN=NFCN+6   
C ERROR ESTIMATION BRR=0. D0 41 I=1,N DENOM=AMAX1(1.R-5,ABS(YI(I)),ABS(Y(I)),2.\*UROUND/BPS） 41 ERR=ERR+(K2(I)/DBNOM)\*\*2 ERR=SQRT(ERR/FLOAT(N))   
C COMPUTATION OF HNEW   
C WE RBQUIRE .2<=HNEW/H<=10. FAC=AMAX1(.1,AMIN1(5.,(ERR/EPS)\*\*(1./6.)/.9)) HNEW=H/FAC IF(ERR.LE.EPS)THEN   
C STEP IS ACCEPTED NACCPT=NACCPT+1 CALL STORE(X,XPH,Y,N,K1,K3,K4,K5,K6） D0 44 I=1,N K1(I)=K7(I) 44 Y(I)=YI(I)   
C --- RECOMPUTE KI IN THE CASE OF DISCONTINUOUS INITIAL PHASE IF(.NOT.DISC) CALL FCN(N,XPH,Y,Kl) X=XPH IF(ABS(HNEW).GT.HMAX)HNEW=HMAX IF(REJECT) HNEW=AMINI(ABS(HNEW),ABS(H)) REJBCT=.FALSE. BLSE   
C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1) NREJCT=NRRJCT+1 BND IF H=HNBW G0T0 1   
C FAIL BXIT 79 WRITE(6,979)x   
979 FORMAT(' BXIT OF RETARD AT X=',E11.4) RETURN BND   
C SUBROUTINE STORE(X,XPH,Y,N,FG1,FG3,FG4,FG5,FG6) PARAMETER (NN=4,MXST=800） DIMENSION Y(N),FG1(N),FG3(N),FG4(N),FG5(N),FG6(N) COMMON/COEF/XSTOR(MXST),YSTOR(NN,MXST). &C1(NN,MXST).C2(NN,MXST),C3(NN.MXST),C4(NN,MXST)   
C --- COEFFICIENTS FOR GLOBAL SOLUTION ARE STORED IN COEF COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC LAST=LAST+1 IFIRST=MAXO(1,LAST-MXST+1) IADR=MOD(LAST-1,MXST)+1 XLAST= XPH XSTOR(IADR)=X DO 2 I=1,NN YSTOR(I,IADR)=Y(I) C1(I,IADR)=FG1(I) C2(I,IADR)=-(1337./480.)\*FG1(I)+(105400./27825.)\*FG & (135./80.)\*FG4(I)-(54675./212000.)\*FG5(I)+(66./7 C3(I,IADR)=(1039./360.)\*FG1(I)-(468200./83475.)\*FG3 & (9./2.)\*FG4(I)+(400950./318000.)\*FG5(I)-(638./21 C4(I,IADR)=-(1163./1152.)\*FG1(I)+(37900./16695.)\*FG & (415./192.)\*FG4(I)-(674325./508800.)\*FG5(I)+(374 2 CONTINUE RETURN BND p' REAL FUNCTION YLAG(I,X,PHI) PARAMETER (NN=4,MXST=800) LOGICAL DISC COMMON/COEF/XSTOR(MXST),YSTOR(NN,MXST), & C1(NN,MXST),C2(NN,MXST),C3(NN,MXST),C4(NN,X) COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC COMMON/UROUND/UROUND   
C INITIAL PHASE IF（DISC） THEN IF(ABS(X-XO).LE.(3.\*UROUND\*ABS(X)))DISC=.FALSE. IF(X.LE.XO)THEN YLAG=PHI(I,X) RETURN END IF END IF   
C COMPUTE THK POSITION OF X IF(X.LT.XSTOR(IFIRST))THEN WRITE （6,\*) MEMORY FULL，MXST $=$ ',MXST STOP BND IF IPOS=MAXO(IFIRST,MINO(LAST,IPOS)) 1 IADR=MOD(IPOS-1,MXST)+1 IF（X.LT.XSTOR(IADR).AND.IPOS.GT.IFIRST) THEN IPOS=IPOS-1 GOTO 1 END IF 2 IADR=MOD(IPOS,MXST)+1 IF（IPOS.LT.LAST) THEN IF（X.GT.XSTOR(IADR)） THEN IPOS=IPOS+1 GOTO 2 END IF END IF   
C COMPUTE THE DESIRED APPROXIMATION IADR=MOD(IPOS-1,MXST)+1 IF（IPOS.BQ.LAST) THEN H=XLAST-XSTOR(IADR) ELSE H=XSTOR(MOD(IPOS,MXST)+1)-XSTOR(IADR) END IF S=(X-XSTOR(IADR))/H YLAG=YSTOR(I,IPOS)+H\*S\*(C1(I,IPOS)+S\*(C2(I,IPOS) & +S\*(C3(I,IPOS)+S\*C4(I,IPOS)))) RETURN END   
N.H. Abel (1826): Untersuchungen uber die R eihe: $1 + { \frac { m } { 1 } } x + { \frac { m ( m - 1 ) } { 1 \cdot 2 } } x ^ { 2 } + { \frac { m ( m - 1 ) ( m - 2 ) } { 1 \cdot 2 \cdot 3 } } x ^ { 3 } + \ldots \ldots \ldots u . s . w .$ Crelle J. f.d. r.u.angew. Math. (in zwanglosen Heften), vol.1, p.311- 339.   
N.H. Abel (1827): Ueber einige bestimmte Integrale, Crelle J. f. d. r. u. angew. Math., vol.2, p.22-30.   
M. Abramowitz and I.A.Stegun (1964): Handbook of mathematical functions, Dover, 1000 pages.   
J.C. Adams (1883): see FBashforth (1883).   
A.C. Aitken (1932): On interpolation by iteration of proportional parts， wihout the use of differences; Proc. Edinburgh Math. Soc. Second ser. Vol.3,p.56- 76.   
J. Albrecht (1955): Beitrage zum Runge-Kutt-Verfahren, ZAMM, vol.35, p.100- 110.   
V.M. Alekseev (1961): An estimate for the perturbations of the solution of ordinary differential equations (Russian). Vestn. Mosk. Univ.,Ser.I, Math. Meh, 2, p.28-36.   
JIe Rond d'Alembert (1748): Suite des recherches sur le calcul integral, quatrieme partie: Methodes pour integrer quelques equations différentielles， Hist. Acad. Berlin, Tom.IV, p.275-291.   
R.F. Arenstorf (1963): Periodic solutions of the restricted three body problem representing analytic continuations of Keplerian eliptic motions， Amer. J. Math., vol.LXxxV, p.27-35.   
C. Arzela (1895): Sulle funzioni di linee, Memorie dell. R. Accad. delle Sc. di Bo-logna, 5e serie, vol.V, p.225-244, see also: vol.V, p.257-270, vol.VI, (1896), p.131-140.   
N. Bakhvalov (1976): Methodes numeriques, Editions Mir, Moscou $6 0 0 \{ \mathbf { p } \mathbf { p } .$ , russian edition 1973.   
F. Bashforth (1883): An attempt to test the theories of capillary action by comparing the theoretical and measured forms of drops of fluid. Wuth an explanation of the method of integration employed in constructing the tables which give the theoretical form of such drops, by J.CAdams, Cambridge Univ. Press.   
R.H. Batin (1976): Resolution of Runge-Kutta-Nystrom condution equations through eighth order, AIAA J., vol.14, p.1012-1021.   
F.L. Bauer, H. Rutishauser and E. Stiefel (1963): New aspects in numerical quadrature. Proc. of Symposia in Appl. Math. vol.15, p.199-218, Am. Math. soc.   
PA. Beentjes and W.J. Gerritsen (1976): Higher order R unge-Kutta methods for the numerical solution of second order differential equations without first deriva-tives，Report NW 34/76,Math. Centrum, Amsterdam plexen Veranderlichen.'Zweite Auflage. Springer Verlag, Berlin-Gottingen-Heidelberg.   
A. Bellen (1984): One-step collcation for delay differential equatins， J. Comput. Appl. Math. Vol.10, p.275-283.   
R. Bellman and K.L. Cooke (1963): Diferential-Difference equations, Academic Press, 462pp.   
I. Bendixson (1893): Sur le calcul des integrales d'un systeme d'equations differenieles par des approximations successives, Stock. Akad. Forh., Vol.51, p.599-612.   
I. Bendixson (1901): Sur les courbes definies par des équations differentielles， Acta Mathematica, vol.24, p.1-88.   
Jac. Bernoulli (1695): Explicationes, Annotationes & Additiones ad ea, quae in Actis sup.anni de Curva Elastica, Isochrona Paracentrica, & Velaria, hinc inde memorata， & partim controversa legundur; ubi de Linea mediarum directio-num, alisque novis, Acta Erudit. Lipsiae, Anno MDCxCV, p. 537-553.   
Jac. Bernoulli (1697): Solutio Problematum Fratermorum, Peculiari Programmate Cal. Jan.I697 Groningae, nec non Actorum Lips. mense Jun. & Dec.1696， & Febr.1697 propositorum: una cum Propositione reciproca aliorum. Acta Erud. Lips. MDCXCVII, p.211-217.   
Joh. Bernoull (1696): Problema novum Mathematicis propositorum. Acta Erud. Lips. MDCXCVI, p.269, Opera Omnia vol.I, p.161 and 165, Lausannae & Genevae 1742.   
Joh. Bernouli (1697): De Conoidibus et Sphaeroidibus quaedam. Solutio anatytica Aequationis in Actis A. 1695， pag. 553 propositae, Acta Erud. Lips., MDCXCVII, p.113-118.   
Joh. Bernoulli (1697b): Solutioque Problematis a se in Actis 1696, p.269, proposit， de invenienda Linea Brachystochrona， Acta Erud.Lips. MDCXCVII, p.206, Opera Omnia vol.I, p.187-193.   
D. Bernoulli (176O): Essai d une nouvelle anatyse de la moralite causee par la petite verole,et des avantages de l'inoculation pour la prevenirHist.et Mem. de I'Acad. Roy. Sciences Paris, 1760, p.1-45; Werke Band 2,p.235-267.   
L. Bieberbach (1923): Theorie der Diferentialgleichungen， Grundlehren Bd.VI, Springer Verlag.   
L. Bieberbach (1951): On the remainder of the Runge-Kutta formula in the theory of ordinary differential equations， Zeitschr. angew. Math.Phys. (ZAMP), vol.2, p.233-248.   
G. Birkhoff and R.S. Varga (1965): Discretization errors for wel-set Cauchy problems I, Journal of Math. and Physics, volXLIV, p.1-23.   
C. de Boor and B. Swartz (1973): Collocation ai Gaussian points, SIAM J. Numer. Anal., vol.10, p.582-606.   
R. Bulirsch and J. Stoer (1964): Fehlerabschatzungen und Extrapolation mit rationalen Funktionen bei Verfahren vom Richardson-Typus, Num. Math. Vol.6, p.413-427.   
R. BulirschandJ.Stoer (1966): Numerical treatment ofordinary diferential equa tions by extrapolation methods, Num.Math.vol.8, p.1-13.   
K. Burrage (1985): Order and stability properties of explicit multivalue methods. Appl. Numer. Anal., vol.1, pp.363-379. (lyuvj. Aun-uicur suviuty Uj u gentrui usg Uj differential equation methods.B,vol.20,pp.5-20.   
K.Burrage and PMoss (1980):Simplifying assumptions for the order of paritioned multivalue eos..   
J.C.Butcher (1963): Coeficients for the study of Runge-Kuta integration processes, J. Austral. Math. Soc., vol.3, p.185-201.   
J.C. Butcher (1963a): On the integration processof A. Huta,J.Austral. MathSoc., vol.3, p.202-206.   
J.C.Butcher (1964a): Implicu Runge-Kuta Processes， Math. Comput. vol.18, p.50-64.   
J.C. Butcher (1964b): On Runge-Kuta processs of high order, J.Austral. Math. Soc. vol.IV, Part2, p.179-194.   
J.C. Butcher (1964c): Integration proceses based on Radau quadrature formulas, Math. Comput., Vol.18, p2-44.   
J.C. Butcher (1965a): A modified multistep method for the numerical integrution of ordinaryiffretaleios.J.C,vo2,5.   
J.C. Butcher (1965b): On the atainable order of Runge-Kutta methods， Math. of Comp. vol.19, p.408-417.   
J.C.Butcher (1966): On the convergence of numerical solutions to ordinary diferentil equations,th.omt.,ol,p.10   
J.C. Butcher (1967): A multistep generalization of Runge-Kutta methods with four or five stages. J. ACM, vol.14, p.84-99.   
J.C.Butcher (1969):The efective order of Runge-Kutta methods, in: Conference on the numerical solution of differential equations, Lecture notes in Math. Vol.109, p.133-139.   
J.C. Butcher (1972): An algebraic theory of integration methods, Math. Comput. Vol.26, p.79-106.   
J.C. Butcher (1975): An order bound for Runge-Kuta methods, SIAM JNum. Anal. vol.12, p.304-315.   
J.C. Butcher (1981): A eneralzationof singlymplicit methods，B,vol.21,p.15- 189.   
J.C. Butcher (1984): An application of the Runge-K utta space, BIT, vol.24, p.425- 440.   
J.C. Butcher (1985a): General linear method: a survey， Appl. Num. Math., vol.1, p.273-284.   
J.C. Butcher (1985b): The non-existence of ten stage eighth order explicit Runge-K utta methods, BIT, vol.25, p.521-540.   
G.D. Byrne and A.C. Hindmarsh (1975): A polyalgorithm for the numerical solution of ordinary differential equations, ACM Trans. on Math. Software, vol.1, No.1, p.71-96.   
G.D. Byrne and RJ. Lambert (1966): Pseudo-Runge-Kut methods involving two points, J. Assoc. Comput. Mach., vol.13, p.114-123.   
A.L. Cauchy (1824): Résume des Lecons donnees a l'Ecole Royale Polytechnique. Suite du Calcul Infinitesimal: published: Equations differentielles ordi-naires, ed. Chr. Gilain, Johnson 1981.   
A.L. Cauchy (1831): Sur la mecanique celeste et sur un nouveau calcul appelé calcul des timites, lu a l'acad. de Turin le 11 oct 1831; also: exerc. d'anal. et de pysique math, 2, Paris 1841; oeuvres (2), 12. de Parls. (Aug. 5, Nov. 21,183y, June 2y, Oct. 26,184U, etc).   
A. Cayley (1858): Amemoir on thetheory of matrices,Phil. Trans.of Royal Soc.of London,vol.CXLVIl, p.17-37, Mathematical Papers vol.2， Nr.152, p.475.   
F. Ceschino and J. Kuntzmann (1963): Problemes diférentiels de conditions initiales (methodes meriqes),d s   
F. Ceschino and J. Kuntzmann (1963): Problemes diferentiels de conditions initiales, Dunod Paris; english translation: Numerical solutions of initial value problems, Prentice Hall 1966   
F.Ceschino (1961): Modification de la longueur du pas dans Pintegration numerique par les méthodes a pas lies, Chiffres 2, p.101-106.   
F.Ceschino(962):Evaluationde lereurparpasdans lesproblemesdiferentels Chiffres vol.5, p.223-229.   
A.C. Clairaut (1734): Solution de plusieurs problemes ou il s'agit de trouver des courbes dont la propriete consiste dans une certaine relation entre leurs branches, exprimee par une Equation donnee, Memoires de Math.et de Phys. de l'Acad. Royale des Sciences, Paris, Annee MDCCXXXIV, p.196-215.   
L. Collatz (1951): Numerische Behandlung von Diferentialgleichungen, Grundlehren Band LX,Springer Verlag，458pp;second edition1955;third edition and english translation 1960.   
P. Collet and J.P. Eckmann (1980): Iterated maps on the interval as dynamical systems, Birkhuser,248pp.   
G.J. Cooper and J.H. Verner (1972): Some explicit Runge-Kuta methods of high order, SIAM J.Numer. Anal. vol.9, p.389-405.   
G.J. Cooper (1978): The order of convergence of general linear methods for ordinary differential equations. SAM, J. Numer. Anal., vol.15, pp.643-661.   
SA.Corey (1906):Amethod of approximationAmer.Math.MonthlyVl13, p.137-140.   
P.H. Cowell and A.C.D. Crommelin (1910): Investigation of the motion of Halley's comet from 1759 to 1910. Appendix to Greenwich Observations for 1909, Edinburgh, p.1-84.   
D.M. Creedon and JJ.H. Miller (1975): The stability properties of q-step backward difference schemes, BIT, vol.15, p.244-249.   
M. Crouzeix (1975): Sur Papproximation des equations différentielles operationnelles lineaires par des methodes de Runge-Kutt， These d'etat, Univ. Paris 6, 192pp.   
M. Crouzeix and F J. Lisbona (1984): The convergence of variable-stepsize, variable formula, multistep methods, SIAM J.Num.Anal. 21, p.512-534.   
C.W. Cryer (1971): A proof of the instability of backward-difference multistep methods for the numerical integration of ordinary differential equations, Tech. Rep. No.117, Comp. Sci. Dept., Univ. of Wisconsin, p.1-52.   
C.W. Cryer (1972): On the instability of high order backward-difference multistep methods, BIT, vol.12, p.17-25.   
W.J. Cunningham (1954): A nonlinear differential-difference equation of growth, Proc. Mat. Acad. Sci., USA, vol.40, p.708-713.   
A.R. Curtis (197O): An eighth order R unge-Kutta process with eleven function evalua-tions per step, Numer. Math. Vol.16, p.268-277.   
A.R. Cuius (1yiS): Hign-oraer expucu Kunge-K uua jormuiae, tneir uses, ana tmua-tions, J.Inst. Maths Applics, vol.16, p.35-55.   
C.F. Curtiss and J.O. Hirschfelder (1952): Integration of stiff equations. Proc. of the National Academy of Sciences of U.S., vol.38,p.235-243.   
G. Dahlquist and R. Jeltsch (1979): Generalized disks of contractivity for explici and implicit Ruge-uta eos.eort--796,, Inst. Techn. Stockholm.   
G.Dahlquist (1956): Convergenceand stability in the numerical integration of ordi-nary differential equations, Math. Scand., vol.4, p.33-53.   
G.Dahlquist (1959): Stability and errorbounds in the numerical integration of ordi nary differential equations， Trans. of the Royal Inst. of Techn., Stockholm,Sweden,Nr.30,p.   
G. Dahlquist (1985): 33 years of numerical instability，part.I, BIT, vol25,p.188- 204.   
J. Descloux (1963): A note on a paper by A. Nordsieck, Report No.131, Dept. of Comp. Sci., Univ. of Ilinois at Urbana-Champaign.   
P. Deuflhard and E. Hairer ed. (1983): Numerical treatment of inverse problems in differeniald inegral eioir,otoel $3 5 7 \mathrm { p p }$   
P. Deuflhard and G. Bader (1982): Multiple shooting techniques revisited, Preprint Nr.163, Univ.Heidelberg,Inst.Angew.Math.D-690 Heidelberg1. Summary published in: P. Deuflhard, E. Hairer, (1983) p.74-94.   
P. Deuflhard (1980): Recent advances in multiple shooting techniques; In: Computational techniques for ordinary differential equations (Gladwell-Sayers, ed.),Section 10,p.217272, Academics.   
P.Deufihard (1983): Order and stepsize control in extrapolation methods， Num. Math. vol.41, p.399-422.   
P. Deuflhard (1985): Recent progress in extrapolation methods for ordinary differential equations,Aev.,l275   
J. Donelson and E. Hansen (1971): Cyclic composite multistep predictor-corrector methods. SIAM, J. Numer. Anal., vol.8, pp.137-157.   
J.R. Dormand and PJ. Prince (1978): New Runge-Kutta algorithms for numerical simulation in dynamical astronomy， Celestial Mechanics， vol.18,p223- 232.   
J.R. Dormand and P.J. Prince (198O): A family of embedded Runge-Kutta formulae, J.Comp. Appl. Math. vol.6, p.19-26.   
R.D. Driver (1977): Ordinary and delay differential equations, Applied Math. Sciences 20, Springer Verlag,501pp.   
B.L. Ehle (1968): High order A-stable methods for the numerical solution of systems of D E's, BIT vol.8, p.276-278.   
N.F. Eispack (1974): B.T.Smuh， JM. Boyle, B.S.Garbow, Y Jkebe，V.C.Klema, CB Moler: Matrix Eigensytem Routines，(Fortran-translationsof algo rithms_ published in Reinsch and Wilkinson), Lecture Notes in Com-puter Science, vol.6, Springer Verlag.   
H. Eltermann (1955): Fehlerabschatzung bei naherungsweiser Losung von Systemen von Differentialgleichungen erster Ordnung, Math. Zeitschr. vol.62, p.469-501.   
R. England (1969): Error estimates for Runge-Kuta type solutions to systems of ordi-nary differential equations; The Computer J. vol.12, p.166-170.   
W.H. Enright, T.E. Hull and B. Lindberg (1975): Comparing numerical methods for stiff systems of $O \mathcal { D } \mathcal { E } _ { \mathcal { S } } ,$ BIT vol.15, p.10-48.   
W.H. Enright, K.R. Jackson, S.P. Nbrsett and P.G. Thomson (1985): Interpolants for Runge-Kutt formulas, Technical Report 180/85, Dept. Comput. Science, Toronto, Canada M5 1A5, $3 6 ~ \mathrm { p \bar { p } }$   
L. Euler (1728): Nova methodus innumerabiles aequationes diffrentiales secundi gradus reducendi ad aequationes differentiales primi gradus, Comm. acad. scient. Petrop.vol.3, p.124-137; Opera Omnia vol.XXII, p.1-14.   
L. Euler (1743): $D e$ integratione aequationum differentialium altiorum graduum,Miscellanea Berolinensia vol.7, p.193-242；Opera Omnia vol.XXII, p.108- 149. See also: Letter from Euler to Joh. Bernoulli, 15.Sept.1739.   
L. Euler (1744): Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes ., Lausannae & Genevae, Opera Omnia (intr. by Caratheodory) vol.XXIV, p.1-308.   
L. Euler (175O): Methodus aequationes differentiales altiorum graduum integrandi uterius promota， Novi Comment. acad. scient. Petrop. vol.3, p.3-35; Opera Omnia vol.XXII, p.181-213.   
L. Euler (1756): Elementa calculi variationum, presented September 16, 1756 at theAcad.of Science,Berlin;printed 1766,OperaOmnia vol.XXV,p.141-176.   
L. Euler (1768): Institutionum Calculi Integralis, Volumen Primum, Opera Omnia vol.XI.   
L. Euler (1769): Institutionum Calculi Integralis， Volumen Secundum， Opera Omnia vol.Xi.   
L. Euler (1778): Specimen transformationis singularis serienum， Nova acta. acad. Petrop., vol.12 (1794),p.58-70,Opera OmniavolVI, p.41-55.   
E. Fehlberg (1958): Eine Methode zur Fehlerverkleinerung beim Runge-Kuta-VerfahrenZAMvol.38, p.4226   
E. Fehlberg (1964): New high-order Runge-Kuta formulas with step size control for systems of first and second order differential equations, ZAMM, vol.44, Sonderheft T17-T19.   
E. Fehlberg (1968): Classical fifth-, sixth-， seventh-， and eighth order Runge-Kutta formuias with step size control; NASA Technical Report 287 (1968); extract published in Computing vol.4, p.93-106 (1969).   
E.Fehlberg (1969): Low-order classcal Runge-Kutta formulas with step size control and their application to some heat transfer problems，NASA Technical Report 315 (1969)，extract published in Computing vol.6，p.61-71 (1970).   
E. Fehlberg (1972): Classical eighth- and lower-order Runge-Kutt-Nystrom formulas with stepsize control for special second-order differential equations， NASA Technical Report R-381.   
M. Feigenbaum (1978): Quantitative universality for a class of nonlinear transformations,JStat.Phys.vol.19,p.25-52,vol.21 (1979),.669706.   
J.R. Field and R.M. Noyes (1974): Oscilations in chemical systems. IV. Limi cycle behavior in a model of a real chemical reaction, J. Chem. Physics, vol.60, p.1877-1884.   
S. Filippi and J. Graf (1986): New Runge-Kut-Nystrom formula-pairs of order 8(7),9(8). I0(9) and 11(10) for differential equations of the form $y \ ^ { \prime \prime } { = } f \left( x \ , y \right)$ , J.Comput. and Applied Math., vol.14, p.361-370.

R. Fletcher and D.C. Sorensen (1983): An algorithmic derivation of the Jordan canonical form, Amer. Math. Monthly, vol.90, No.1, p.12-16.

C.V.D. Forrington (1961-62): Extensions of the predictor-corrector method for the solution of systems of ordinary differential equations, Comput. J. 4, p.80 84.

J.BJ. Fourier (1807): Sur la propagation de la chaleur, unpublished manuscript; published: La theorie analytique de la chaleur, Paris 1822.

V. Franceschini (1980): Feigenbaum sequence of bifurcations in the Lorenz model, J.Stat, Phys. vol.22, p.397-406.

R.A. Frazer, W.P. Jones and S.W. Skan (1937): Approximations to functions and to the solutions of differential equations，Reports and Memoranda Nr.1799 (2913),Aeronautical Research Commiee. 3pp.

A.Fricke (1949): Ueber die Fehlerabschatzung des Adamsschen Verfahrens zur Inte gration gewohnlicher Diferentialgleichungen erster Ordnung， ZAMM, vol.29, p.165-178.

M.Frommer (1934): Ueber das Auftreten von Wirbeln und Strudeln (geschlossener und spiraliger Integralkurven) inder Umgebung rationaler Unbestimmtheits-stellen, Math. Ann., vol.109, p.395-424.

L.Fuchs (1866): Zur Theorie der linearen Differentialgleichungen mit verdnderlichen Coefficienten, Crelle J. f. d. r. u. angew. Math., vol.66, p.121-160 (prepublished in 'Programm der stadtischen Gewerbeschule zu Berlin, Ostern 1865").

P. Funk (1962): Variationsrechnung und ihre Anwendung in Physik und Technik, Springer Verlag, Grundlehren Bd. 94, 676 p.

C.F. Gauss (1812): Disquisitiones generales circa seriem infinitam

$$
\begin{array} { r l } & { 1 + \frac { \alpha \beta } { 1 \cdot \gamma } x + \frac { \alpha \left( \alpha + 1 \right) \beta \left( \beta + 1 \right) } { 1 \cdot 2 \cdot \gamma \left( \gamma + 1 \right) } x x } \\ & { \qquad + \frac { \alpha \left( \alpha + 1 \right) \left( \alpha + 2 \right) \beta \left( \beta + 1 \right) \left( \beta + 2 \right) } { 1 \cdot 2 \cdot 3 \cdot \gamma \left( \gamma + 1 \right) \left( \gamma + 2 \right) } x ^ { 3 } + e t c , } \end{array}
$$

Werke vol.3, p.123-162.

W. Gautschi (1962): On inverses of Vandermonde and confluent Vandermonde matri-ces, Numer. Math. vol.4, p.117-123.

C.W. Gear and D.S. Watanabe (1974): Stability and convergence of variable order multistep methods, SIAM J. Num. Anal. 11, p.1044-1058.

C.W. Gear and K.W. Tu (1974): The effect of variable mesh size on the stability of multistep methods, SIAM J. Num. Anal. 11, p.1025-1043.

C.W. Gear (1965): Hybrid methods for initial value problems in ordinary differentiai equations. SIAM J. Numer. Anal., ser.B, vol.2, p.69-86.

C.W. Gear (1971): Numerical initial value problems in ordinary differential equations, Prentice-Hall, 253pp.

A. Gibbons (1960): A program for the automatic integration of differential equations using the method of Taylor series, Computer J. vol.3, p.108-111.

S. Gill (1951): A process for the step-by-step integration of differential equations in an automatic digital computing machine， Proc. Cambridge Philos. Soc., vol.47, p.95-108.

B. Giovannini, L. Weiss-Parmeggiani and B.T. Ulrich (1978): Phase locking in coupled Josephson weak links, Helvet. Physica Acta, vol.51, p.69-74.

H.H. Goldstine (1980): A History of the Calculus of Variations, Springer Verlag, 410p.   
G.H. Golub and J.H. Wilkinson (1976): Iu-conditioned eigensystems and the computation of theJordan canonical form,AReview,vol.18,p.578-619.   
B.A. Gottwald (1985): Zur Modelierung zeiverzogerterbioogischer Prozesse,Infomatik Fachberichte,vol.109,p.350-354, Springer Verlag.   
W.B. Gragg and H.J. Stetter (1964):Generalized multistep predictor-corrector methods. J. ACM, vol.11, pp.188-209.   
W.B. Gragg (1964): Repeated extrapolation to the limit in the numerical solution of ordinary differential equations,Thesis， Univ. of California; see also SIAM J. Numer. Anal., vol.2, p.384-403 (1965).   
W.B.Gragg (1965):On extrapolationalgorithms for ordinary initial value problems， SIAMJ.Num. Anal.,ser.B,vol.2,p.384-43.   
R.D. Grigorieff (1977): Numerik gewohnlicher Differentialgleichungen 2. Teubner Studienbucher,Stt   
R.D. Grigorief (1983): Stability of multistep-methods on variable grids，Numer. Math. 42, p.359-377.   
W. Grobner (1960): Die Liereihen und ihre Anwendungen, D. Verl. d. Wis. Berlin, 2nd ed. 1967.   
T.H. Gronwal (1919): Note on the derivatives with respect to a parameter of the solu-tions of a system of differential equations, Ann. Math. vol.20, p.292-296.   
H. Hahn (1921): Theorie der reelen FunktionenSpringer Verlag Berlin, $6 0 0 \mathrm { p p }$   
W. Hahn (1967): Stability of motion, Springer Verlag, 446pp.   
E. Hairer and G. Wanner (1973): Mulistep-multistage-multiderivative methods for ordinary differential equations, Computing Vol.11, p.287-303.   
E. Hairer and G. Wanner (1974): On the Butcher group and general multi-value methods, Computing Vol.13, p.1-15.   
E. Hairer and G. Wanner (1976): A theory for Nystrom methods, Numer. Math., vol.25, p.383-400.   
E. Hairer and G. Wanner (1983): On the instability of the BDF formulas, SIAM J. Numer. Anal., vol.20, No.6, p.1206-1209.   
E. Hairer and Ch. Lubich (1984): Asymptotic expansions of the global error of fixed-stepsize methods, Numer. Math. vol.45, p.345-360.   
E.Hairer (197): Methodes de Nystrom pour l'equation diferentielle $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ Numer. Math., vol.27, p.283-300.   
E. Hairer (1978): A Runge-Kutta method of order 10, J.Inst. Maths Applics, vol.21, p.47-59.   
E. Hairer (1981): Order conditions for numerical methods for partitioned ordinary differential equations, Numer. Math., vol.36, p.431-445.   
E. Hairer (1982): A one-step method of order 10 for $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ , IMA J. Num. Anal. vol.2, p.83-94.   
P.C. Hammer and J.W. Hollngsworth (1955): Trapezoidal methods of approximating solutions of differential equations, MTAC vol.9, p.92-96.   
N.D. Hayes (1950): Roots of the transzendental equation associated with a certain difference-differential equation, J. of London Math. Soc., vol.25, p.226- 232. ytnwUjnungt-nwu mtnu Jui systems of n -th order diferential equations, J. Comput. Appl. Math., vol.8, p.3-14.   
P. Henrici (1962): Discrete variable methods in ordinary diferential equations. John Wiley & Sons,Inc.,New-York-London-Sydney.   
P.Henrici (1974):Applied andcomputational complexanalysis, Volume1,John Wiley &Sons,New York,68pp.   
Ch. Hermnite (1878): Extrait dune lettre de M. Ch. Hermite a M. Borchardt sur la formule dinterpolation de Lgrange,J.de Crelle,v84,p.；Os tome III, p.432-443.   
K. Heun (1900): Neue Methode zur approximativen Integration der Diferentialgleichungen einer unabhangigen Veranderlichen, Zeitschr. fur Math.u. Phys., vol.45, p238.   
A.C. Hindmarsh (1972): GEAR : ordinary differential equation system sotver, UCID-30001,Rev2,,imore,f.   
A.C. Hindmarsh (1980): LSoDE and LSODI, two new initial value ordinary diferential equation solvers, ACM Signum Newsletter 15,4.   
M.W. Hirsch and S. Smale (1974): Differential equations, dynamical systems and linear algebraAcad.es   
E.W. Hobson (1921): The theory offunctions of a real variable,vol.ICamridge, 670pp.   
G.'t Hooft (1974): Magnetic monopoles in unified gauge theories， Nucl. Phys. vol.B79, p.276-284.   
E. Hopf (1942): Abzweigung einer periodischen Losung von einer stationaren Losung eines Differenalsystems，Ber.math.physik.Kl. Akad.d.Wiss.Leipig, Bd.XCIV, p.-22.   
M.K. Horn (1983): Fourth and fifth-order scaled Runge-Kutt algorithms for treating dense output, SIAM JNumer. Anal. vol.20, p.558-568.   
PJ.van der Houwen (1977):Construction of integration formulas for initial vatue problems, North-Holland Amsterdam, $2 6 9 \mathrm { p p }$   
T.E. Hull W.H. Enright,B.M. Felln and A.E. Sedgwick (1972): Comparing numerical methods for ordinary differential equations, SIAM J. Numer. Anal., vol.9, p.603-637.   
T.E. Hull and R.L. Johnston (1964): Optimum Runge-Kutta methods, Math. Com-put., vol.18, p.306-310.   
T.E. Hull (1967): A search for optimum methods for the numerical integration of ordinary dierential equations,SAM Rev., vol.9, p.647-654.   
B.L. Hulme (1972): One-step piecewise potynomial Galerkin methods for initial value problems,ath. of Comput. vol.26, p.415-426.   
W.H. Hundsdorfer and M.N. Spijker (1981): A note on $B$ -stability of Runge-Kutta methods, Num. Math. Vol.36, p.319-331.   
A. Hurwitz (1895): Ueber die Bedingungen, unter welchen eine Gleichung nur Wurzebn mit negativen reellen Theilen besitzt, Math. Ann., vol.46, p273-284; Werke vol.2, p.533ff.   
E.L. Ince (1944): Ordinary differential equations， Dover Publications, New York, $5 5 8 \mathrm { p p }$   
G. Iooss and D.D. Joseph (1980): Elementary stability and bifurcation theory, Springer Verlag, 286 pp. (see chapter VII).   
C. Jordan (187o): Traite des Substitutions et des equations algebriques, Paris 667pp.   
C. Jordan (1928): Sur une formule d interpolation, Atti Congresso Bologna, vol 6, p.157-177   
B. Kaogstrom and A. Ruhe (1980): An algorithm for numerical computation of the Jordan normal form of a complex matrix; ACM Trans. Math. Software, vol.6, p.398-419. (Received May 1975, revised Aug.1977, accepted May 1979).   
S. Kakutani and L. Marcus (1958): On the non-linear difference-differential equation $\mathbf { \beta } _ { \prime } ^ { \prime } ( t ) = [ A - B y \left( t - \tau \right) ] y \left( t \right)$ ,in: Contributions to the theory of non-linear oscillations, Ed. by S.Lefschetz, Princeton, vol.IV, p.1-18.   
E. Kamke (193O): Ueber die eindeutige Bestimmtheut der Integrale von Diferential gleichugnen I1， Sitz. Ber. Heidelberg Akad. Wiss. Math. Naturw. Kl., 17. Abhandl., see also Math.Zeitschr., vol. 32, p.101-107.   
E. Kamke (1942): Diferentialgleichungen,Losungsmethoden und Losungen，Becker & Erler,Leipzig, 642pp.   
K.H. Kastlunger and G. Wanner (1972): Runge Kuuta processes with mutiple nodes, Computing vol.9, p.9-24.   
K.H. Kastlunger and G. Wanner (1972b): On Turan type implicit Runge-Kutta methods, Computing vol.9, p.317-325.   
H.B. Keller (1968): Numerical methods for two-point boundary-value problems, Blaisdell Publ. Comp., $1 8 4 \ \scriptstyle { \mathbb { p p } } .$ (see section 2.4).   
W.O. Kermack and A.G.Mc. Kendrick (1927): Contributions to the mathematical theory of epidemics (Par I), Proc. Roy. Soc., A, vol.115, p.700-721.   
R.King (1966):Runge-Kuta methods with constrained minimum eror bounds， Math. Comput., vol.20, p.386-391.   
H. Knapp and G. Wanner (1969): LIESE II A program for ordinary diferential equations using Lie-series, MRC Report No.10o8, Math. Research Center, Univ. Wisconsin,Madison,Wisc.53706.   
G. Kowalewski (1908): see Leibniz (1693).   
F.T. Krogh (1969): A variable step variable order mulistep method for the numerical solution of ordinary differential equations， Information Processing 68, North-Holland, Amsterdam, p.194-199.   
F.T. Krogh (1973): Algorithms for changing the step size, SIAM J. Num. Anal. 10, p.949-965.   
F.T. Krogh (1974): Changing step size in the integration of diferential equations using modified devided differences， Proceedings of the Conference on the Num. Sol. of ODE, Lecture Notes in Math. No.362, Springer Verlag New York, p.22-71.   
N. Kryloff and N. Bogoliuboff (1947): Introduction to non-linear Mechanics， free translation by S. Lefschetz, Princeton Univ. Press, $1 0 5 \mathrm { p p }$   
E.E.Kummer (839):Note sur integrationde lequation $d ^ { n } y / d x ^ { n } = x ^ { m } y$ par des integrales definies, Crelle J. f. d. r. u. angew. Math., vol.19, p286-288.   
J. Kuntzmann (1961): Neuere Entwickelungen der Methode von Runge-Kutta, ZAMM, vol.41,p28-31.   
J. Kuntzmann (1959): Deux formules optimales du type de Runge-Kutta, Chifres, vol.2, p.21-26. gleichungen, Zeitschr. fur Math. u. Phys., vol.46, p.435-453.   
J.L.de Lagrange (1759):Recherches sur la nature et la propagation duson, Miscell. Taurinensia t.I,Oeuvrest.1,914.   
J.LdeLagrange (762):olutiondediferensproblemsde CculItegalscel. Taurinensa,t.I,evres t.1,47668.   
J.L.de Lagrange (174): Sur les Integrales particulieres des Equations diférentielles, Oeuvres, tom.4, p.5-108.   
J.L.de Lagrange (1775): Recherche sur les Suites Recurrentes, Nouveaux Mem. de l'Acad. royale des Sciences et Belles-Lettres, Berlin. Oeuvres vol.4, p.159.   
J.L.de Lagrange (1788): Mecanique anatytique, Paris, Oeuvres t.11 et 12.   
J.L.de Lagrange (1792): Memoire sur texpression du terme general des series recurrentes, lorsque lequation generatrice a des racines egales， Nouv. Mem. de l'Acad. royale des Sciences de Berlin, Oeuvres t.5,p.627-641.   
J.L.de Lagrange (1797): Theorie des fonctions anatytiques, contenant les principes du calcul differentiel, degages de toute consideration d’infiniment petits, devanouissants，de limites et de fluxions，et reduis a Panalyse algebrique des quantites finies,Paris,1797,nouv.ed.1813,Oeuvres Tome9.   
P.S. Laplace (An $\mathbf { \Delta } \mathbf { X } \mathbf { I I I } \ = \ \mathbf { \Delta } 1 8 0 5$ ): Supplement au dixieme livre du Traite de mecanique celeste surl'ction capillaire,Paris chez Courcier, $6 5 + 7 8 \mathrm { p p }$   
P.D. Lax and R.D. Richtmyer (1956): Survey of the stabity of linear limite difference equations, Comm. Pure Appl. Math., vol.9, p.267-293.   
R. Lefever and G. Nicolis (1971): Chemical Instabilities and sustained oscillations, J. theor. Biol., vol.30, p.267-284.   
G.W. Leibniz (1691): Methodus， qua innummerarum linearum construction ex data proprietate tangentium seu aequatio inter abscissam et ordinatam ex dato valore subtangentialis, exhibetur. Letter to Huygens, in: C.I. Gerhardt, Leibnizens math. Schriften,1850, Band II, p.116-121.   
G.W. Leibniz (1693) (Gothofredi Guilielmi Leibnitzii): Supplementum Geometriae Dimensoriae seugeneralissima omnium tetra gonismorum effectio per motum: Similiterque multiplex constructio linea ex data tangentium conditione,Acta Eruditorum， Lipsiae,p.385-392；german translation:G. Kowalewski, Leibniz uber die Analysis des Unendlichen, Ostwalds Klassiker Nr.162 (1908), p.24-34.   
A.M. Liapunov (1892): Probleme general de la stabilite du mouvement, russ., trad. en francais 1907 (Annales de la Faculte des Sciences de Toulouse), reprinted 1947 Princeton Univ. Press, $4 7 4 \mathrm { p p }$   
A.M. Lienard (1928): Etude des oscillations entretenues, Revue generale de l'Elec-tricite, tome XXII, p. 901-912 et 946-954.   
E. Lindelof (1894): Sur tapplication des methodes d'approximation successives a letude des integrales reelles des equations diferentielles ordinaires, J. de Math., 4e serie, vol.10, p.117-128.   
J. Liouville (1836): Sur le developpement des fonctions ou parties de fonctions en series dont les divers termes sont assujetis a satisfaire a une meme equation différentielle du second ordre, contenant un parametre variable, Journ. de Math. pures et appl., vol.1, p.253-265.   
J. Liouville (1838): Sur la Theorie de la variation des constantes arbitraires, Liou-ville J. de Math. vol.3, p.342-349.   
J. Liouville (1841): Remarques nouveles sur l'equation de Riccati, J. des Math. pures et appl., vol.6, p.1-13.   
R. Lipschitz (1876): Sur la possibiliute d'integrer completement un systeme donne dequations differentielles, Bulletin des Sciences Math. et Astr.， Paris, vol.10, p.149-159.   
R. Lobatto (1852): Lessen over Differentiaal- en Integraal-Rekening， 2 vol., La Haye 1851-52.   
E.N. Lorenz (1979): On the prevalence of aperiodicity in simple systems, Global Analysis,Calgary 1978，ed.by M.Grmela and J.E.Marsden，Lecture Notes in Mathematics, vol.755, p.53-75.   
M. Lotkin (1951): On the accuracy of Runge-K utta methods, MTAC vol.5, p.128- 132.   
G.I. Marchuk (1975): Prostejshaya matematicheskaya model virusnogo zabolevaniya, Novosibirsk, VTS SO AN SSSR. Preprint.   
G.I. Marchuk (1983): Mathematical models in immunology. Translation series, Optimization oftwae,NewYork,Springer Verlag,5pp.   
M. Marden (1966): Geometry of polynomials， American Mathematical Society, Pro vidence, Rhode Island, 2nd edition.   
J.E. Marsden and M. McCracken (1976): The Hopf bifurcation and its applications, Springer,New York, 408pp.   
R.M. May (1976): Simple mathematical models with very complicated dynamics， Nature, vol.261, p.459-467   
R.H. Merson (1957): An operational method for the study of integration processes, Proc. Symp.Data Processing, Weapons Research Establishment, Salisbury,Australia, p.110-1 to11025.   
W.E. Milne (1926): Numerical integration of ordinary differential equations，Amer. Math. Monthly, vol.33,p.455-460.   
W.E. Milne (197o): Numerical solution of differential equations. Dover Publications, Inc.,New York, second edition.   
R.von Mises (1930):Zurnumerischen Integration von Dferentialgleichungen ZAMM, vol.10, p.81-92.   
A.R. Mitchell and J.W. Craggs (1953): Stability of difference relations in the solution of ordinary diferential equations， Math.Tables Aids Comput., vol.7, p.127-129.   
C. Moler and C. Van Loan (1978): Nineten dubious ways to compute the exponential of a matrix; AM Review,Vol20, p.801-836.   
R.E. Moore (1966): Interval Anatysis, Prentice-Hall Inc,145p.   
R.E. Moore (1979): Methods and applications of interval anatysis， SIAM studies in Appl. Math., 190pp.   
F.R. Moulton (1926): New methods in exterior balistics. Univ. Chicago Press.   
M. Muller (1926): Ueber das Fundamentalheorem in der Theorie der gewohnlichen Diferentialgleichungen，Math.Zeitschr.,vol.26,p619-645. (Kap).   
E.H. Neville (1934): Iterative interpolation, Ind. Math. Soc. J. Vol.20, p.87-120.   
I. Newton (1671): Methodus Fluxionum et Serierum Infinitarum， edita Londini 1736,Opuscula mathematica vol.I, Traduit en francais par M.de Buffon, Paris MDCCXL. (rou.). T uwsupnuc iuuruuw pruupu muuenuuu, Iipiunatui S. Pepys, Reg. Soc. Praeses, julii 5, 1686, Londini anno MDCLXXXVII.   
S.P. Nbrset and G. Wanner (1979): The real-pole sandwich for rational approximations and oscilation equations,BI vol.19, p.79-94.   
S.P. Nbrsett(1974a): One-step methods of Hermite type for numerical integration of stiff systems,,vl.14,p.6-77.   
S.P. Nbrsett (1974b): Semi explicit Runge-K uta methods， Report No.6/74, ISBN 82-7151-009-6,ept. ath.Univ.ondeim,oray, $6 8 + 7 \mathrm { p p }$   
A. Nordsieck (1962): On numerical integration of ordinary diferential equations, Math. Comp., vol.16, p.22-49.   
B. Numerov (B.VNoumerov) (1924): A method of extrapolation of perturbations. Monthly notices of the Royal Astronomical Society,vol84,p.59-601.   
B. Numerov (1927): Note on the numerical integration of $d ^ { 2 } x / d t ^ { 2 } { = } f \left( x \ , t \right)$ Astron. Nachrichten,vol230, p.359-364.   
E.J. Nystrom (1925): Ueber die numerische Integration von Diferentialgleichungen, Acta Soc. Sci. Fenn., vol.50, No.13, p.1-54.   
M. Okamoto and K. Hayashi (1984): Frequency conversion mechanism in enzymatic feedback systems,J.Theor.Biol., vol.108, p.529-537.   
J. Oliver (1975): Acuriosityof low-order expliit Runge-Kutta methods, Math. Comp., vol.29, p.1032-1036.   
M.R. Osborne (1966): On Nordsieck's method for the numerical solution of ordinary diffeential eil.,.   
B.N. Parlett (1976): A recurrence among the elements of functions of triangular matrices, Linear Algebra Appl., vol.14, p.117-121.   
G. Peano (1888): Integration par series des equations differentielles lineaires, Math. Annalen,2,.   
G. Peano (1890): Demonstration de l'integrabilite des equations differentieles ordi-naires, Math. Annalen vol.37, p.182-228; see also the german translation and commentation: G. Mie, Math. Annalen vol.43 (1893), p.553- 568.   
G.Peano (1913): Resto nelle formule di quadratura, espresso con un integrale definito，Atti Della Reale Accad. Dei Lincei, Rendiconti, vol.22,N.9, p.562-569, Roma.   
R. Pearl and LJ. Reed (1922): A further note on the mathematical theory of populationgrowth, Proceedings of the National Acad. of Sciences, vol.8, No.12, pp.365-368.   
L.M. Perko (1984): Limit cycles of quadratic systems in the plane, Rocky Mountain J. of Math., vol.14, p.619-645.   
O. Perron (1915): Ein neuer Existenzbeweis fur die Integrale der Diffrentialgleichung $y ^ { \prime } { = } f \left( x \operatorname { \lrcorner } y \right)$ , Math Annalen, vol.76, p.471-484.   
O. Perron (1918, zur Zeit im Felde): Ein neuer Existenzbeweis fur die Integrale eines_ Systems gewohnlicher Differentialgleichungen， Math. Annalen, vol.78, p.378-384.   
O. Perron (1929): Ueber Stabilitat und asymptotisches Verhalten der Integrale von Differentialgleichungssystemen, Math. Z., vol.29, p.129-160 (see par.3).   
E. Picard (189O): Memoire sur la theorie des equations aux derivees partieles et la methode des approximations successives, J. de Math. pures et appl., 4e serie, vol.6, p.145-210.   
P. Piotrowsky (1969): Stability， consistency and convergence of variable k -step methods for numerical integration of large systems of ordinary differential equations,Lecture Notes in Math., 109, Dundee 1969, p.221-227.   
H. Poincare (1881,82,85): Sur les courbes definies par les equations differentiells， J. de Math.,3e serie,t.7,p375-422,e serie,t.8,p25-296,4e srie,t., p.167-244.   
H. Poincare (1893): Les methodes nouveles de la mecanique celeste， Tome I, 480pp, Gauthier-Villars Paris.   
S.D. Poisson (1835): Theorie mathematique de la chaleur,Paris, Bachelier, 532pp., Supplement 1837, 72pp.   
B. Van der Pol (1926): On "R elaxation Oscillations", Phil. Mag., vol.2, p.978-992; reproduced in:B.vn derPol,elected Sientific Papers,vol.I,oth Holland Publ. Comp. Amsterdam (1960).   
P. Pouzet (1963): Etude en vue de leur traitement numerique des equations intégrales detype Volerra， Rev. Francais Traitement Information (Chiffes), vol.6, p.79-112.   
PJ. Prince and J.R. Dormand (1981): High order embedded Runge-Kutta formulae, J.Comp. Appl. Math. vol.7, p.67-75.   
H. Prufer (1926): Neue Herleitung der Sturm-Liouvillschen Reihenentwicklung stetiger Funktionen, Math. Annalen vol. 95, p.499-518.   
R. Radau (1880): Etude sur les formes d'appoximation qui servent a calculer la valeur numerique d'une integrale definie, Liouville J. de Mathem. pures et appl., 3eser., tome VI, p.283-336. (Voir p.307).   
A. Ralston (1962): Runge-Kutta methods with minimum error bounds， Math. Com-put., vol.16, p.431-437, corr. vol.17, p.488.   
Lord Rayleigh (1883): On maintained vibrations， Phil. Mag. Ser.5, vol.15, p.229- 235.   
W.T. Reid (1980): Sturmian theory for ordinary differential equations, Springer Verlag, Appl. Math., Serie31, 559pp.   
J. Riccati (1712): Soluzione generale del Problema inverso intomo a raggi osculatori,., determinar la curva, a cui convenga una tal'espressione, Gioale de'Letterati d'Italia, vol.11, p.204-220.   
J. Riccati (1723): Animadversiones in aequationes diferentiales secundi gradus, Acta Erud. Lips.,anno MDcCXxiII, p.502-510.   
L.F. Richardson (1910): The approximate arithmetical solution by finite differences of physical problems including differential equations, with an application to the stresses in a masonry dam, Phil. Trans., A, vol.210, p.307-357.   
L.F. Richardson (1927): The deferred approach to the limit, Phil. Trans. A, vol. 226, p.299-349.   
B. Riemann (1854): Ueber die Darstelbarkeit einer Function durch eine trigonometrische Reihe, von dem Verfasser behufs seiner Habilitation an der Universitat zu Gottingen der philosophischen Facultat eingereicht; collected works pp. 227-265.   
W. Romberg (1955): Vereinfachte numerische Integration， Norske Vid. Selsk. Forhdl, vol.28, p.30-36.   
E. Rothe (1930): Z weidimensionale parabolische Randwertaufgaben als Grenzfall eindimensionaler Randwertaufgaben,Math. Annalen,vol.102,p.650670 method, Appl. Math. Sci. 22, Springer Verlag,396pp.   
E.J. Routh (1877): A Treatise on the stabity of a given state of motions, being the essay to which the Adams prize was adjudged in 1877, in the University of Cambridge. London 108pp.   
F.J. Routh (1884): A Treatise on the dynamics of a system of rigid bodies，pan l and I1, 4th edition (st ed.860,6th ed.1897,german translation with remarks of F.Klein 1898).   
D. Ruelle and F. Takens (1971): On the nature of turbulence, Commun. Math. Physics, vol.20, p.167-192.   
C. Runge and H. Konig (1924): Vorlesungen liber numerisches Rechnen，Grund-lehren XI,Spriger Verlag,p.   
C. Runge (1895): Ueber die numerischeAuflosungvon Dferentialgleichungen,Math. Ann., vol.46, p.167-178.   
C.Runge (1905): Ueber dienumerische Auflosung totalerDiferentialgleichungen Gottinger Nachr., p.252-257.   
H. Rutishauser (1952): Ueber die Instabilitat von Methoden zur Integration gewohnlicher Differentialgleichungen, ZAMP, vol.3, p.65-74.   
D. Sarafyan (1966): Error estimation for Runge-Kutta methods through pseudoiterative formulas; Techn. Rep. Nol4, Lousiana State Univ., New Orle-ans, May 1966.   
L. Scheeffer (1884): Zur Theorie der stetigen Funktionen einer reellen Veranderlichen, Acta Mathematica, vol.5, p.183-194.   
I. Schur (19o9): Ueber die charakteristischen W urzeln einer linearen Substitution mit einer Anwendung auf die Theorie der Integralgleichungen, Math.Ann., vol.66, p.488-510.   
L.F. Shampine (1979): Storage reduction for Runge-K utta codes， ACM Trans. Math. Sofware, Vol.5,p.245-250.   
L.F. Shampine and L.S. Baca (1984): Fixed vs. variable order R unge-Kutta, Rept. SAND84-141ia Nat's.，queque, ic, $5 7 \mathrm { p p }$   
L.F. Shampine and M.K. Gordon (1975): Computer Solution of Ordinary Differential Equations, The Initial Value Problem， Freeman and Com-pany, San Francisco, 318pp.   
L.F. Shampine and H.A. Watts (1979): The art of writing a Runge-Kutta code. I1, Appl. Math. Comput., vol.5, p.93-121.   
L.F. Shampine, H.A. Wats and S.M. Davenport (1976): Sotving nonstiff ordinary differential equations - The state of the ar, SIAM Rev.vol.18,p.376-410.   
E.B. Shanks (1966): Solutions of differential equations by evaluations of functions, Math. of Comp. vol.20, p.21-38.   
D. Sommer (1965): Numerische Anwendung impliziter Runge_kutta-Formeln, ZAMM, vol. 45, Sonderheft, p. T77-79.   
Shi Songling (1980): A concrete example of the existence of four limit cycles for plane quadratic systems, Sci. Sinica, vol.23, p.153-158.   
G.F. Simmons (1972): Differential equations with applications and historical notes, MC Graw-Hill,465pp.   
R. Skeel (1976): Anatysis of fixed-stepsize methods， SIAM J. Numer. Anal., vol.13, p.664-685.   
N.D.Jkwi (1)ro). Lyuivuwn jorms Uj muusitp jurmuud, Repon N7o"yto, Depl. of Comp. Sci., Univ. of Ilinois at Urbana-Champaign.   
M.N. Spijker (1971): On the structure of error estimates forfinte diference methods. Numer. Math., vol.18, pp.73-100.   
JF. Steffensen (1956): On the restricted problem of three bodies， K.danske Vidensk.Selsk., Mat-fys. Medd. 30 Nr.18.   
H.J. Stettr (197O): Symmetric two-step algorihms for ordinary differential equations, Computing vol.5, p.267-280.   
H.J. Stetter (1973): Anatysis of discretization methods for ordinary differential equa-tions, Springer Verlag, Berlin-Heidelberg-New York .   
C. Stormer (1907): Sur les trajectoires des corpuscules electrises. Arch. sci. phys. nat., Geneve, vol.24, p.5-18, 113-158, 221-247.   
C. Stormer (1921): Methodes d'integration numerique des equations diferentielles ordinaires. C.R. congr. interm. math., Strasbourg, p.243-257.   
J.Stoer andR.Bulirsch(1973):Einfuhrung indie numerische Mathemaik，Springer Verlag,1st ed. 1973、English translation 1980 (see section 7.3.5).   
J. Stoer and R. Bulirsch (1980): Introduction to Numerical Analysis, Springer Verlag, $6 0 9 \mathrm { p p . , }$ german edition 1973.   
C. Stoermer (1907): Sur les trajectoires des corpuscules electrises， Arch. sci. phys. nat., Geneve, vol.24, p.5-18, 113-158, 221-247.   
C. Stoermer (1921): Methodes d'integration numerique des equations diferentieles ordinaires, C.R. congr. interm. math., Strasbourg, p.243-257.   
A.H. Stroud and D.D. Stancu (1965): Quadrature formulas with multiple Gaussian nodes, SIAM J. Numer. Anal., ser.B., vol.2, p.129-143.   
Ch. Sturm (1829): Buletin des Sciences de Ferussac, tome XI, p.419,see also: Algebre de Choquet et Mayer (1832).   
Ch. Sturm (1836): Sur les equations diferentieles lineaires du second ordre, Journal de Math. pures et appl. (Liouville)，vol.1, p.106-186 (see also p.253, p.269, p.373 of this volume).   
J. Todd (1950): Notes on modern numerical analysis， I， Math. Tables Aids Com-put., vol.4, p.39-44.   
W. Tollmien (1938): Ueber die Fehlerabschatzung beim Adamsschen Verfahren zur Integration gewohnlicher Differentialgleichungen, ZAMM, vol.18, p.83-90.   
W. Tomson (Lord Kelvin) and P.G.Tait (1879): Treatise on natural philosophy (Vol.I., Part I),Cambridge; New edition1890,508pp.   
W. Uhlmann (1957): Fehlerabschatzungen bei Anfangswenaufgaben gewohnlicher Differentialgleichungssysteme 1. Ordnung， ZAMM (Zeitschr. Angew. Math. Mech.) vol.37, p.88-99.   
P.F. Verhuist (1845): Recherches mathematiques sur la loi d'accroissment de la po-pulation, Nuov. Mem. Acad. Roy. Bruxelles, vol.18, p.3-38.   
J.H. Verner (1978): Explicit Runge-Kuta methods with estimates of the local trunca-tion error, SIAM J.Numer. Anal. vol.15, p.772-790.   
L. Vietoris (1953): Der Richtungsfehler einer durch das Adamssche Interpolationsverfahren gewonnenen Naherungslosung einer Gleichung $y ^ { \prime } =$ J $\textit { f } ( x , y )$ Oesterr.Akad. Wiss., Math.-naturw. Kl.， Abt. IIa, vol.162, p.157-167 and p.293-299.   
V. Volterra (1934): Remarques sur la Note de M. Regnier et Mue Lambin. C.R.Acad. Sc. t. CXClX, p.1682. See also: V.Volterra - U.d'Ancona , Les associations biologiques au point de vue mathematique, Paris 1935.   
W. Walter (97):Diffrenaland intgral inequaliesSpringer Verag 3p man edition 1964.   
W. Walter (1971): There is an elementary proofof Peano's existence theorem,Amer. Math.Monthly,vol.78,p.170-173.   
G.Wanner (1969): Integration gewohnlicher Diferentialgleichungen，Lie Reihen, Runge-Ku-etoeneiba.   
G. Wanner (1973): Runge-Kutta methods with expansions in even powers of h， Computing vol.11, p.81-85.   
G. Wanner (1983): On Shis counter example for the 16th Hilber problemInternal Rep.Sect. de Math.，Univ.Geneve 1982; in german in:Jahrbuch Ueberblicke Mathematik 1983, ed. Chattrji, Fenyo, Kulisch, Laugwitz,Liedl, BI Mannheim, p.9-24.   
H.A. Watts (1983): Starting stepsize for an ODE solver, J. Comp. Appl. Math. vol.9, p.177-191.   
K. Weierstrass (1858): Ueber ein die homogenen Functionen zweiten Grades betref. fendes Theorem, nebst Anwendung desselben auf die Theorie der kleinen Schwingungen， Monatsber. der Konigl. Akad. der Wiss, 4. Marz 1858, Werke Bd.I, p.233-246.   
J. Weissinger (1950): Eine verscharfte Fehlerabschatzung zum Extrapolationsverfahren von Adams, ZAMM, vol.30, p.356-363.   
O. Wilde (1892): Lady Windermere's Fan, Comedy in four acts.   
J.H. Wilkinson (1965): The algebraic eigenvalue problem， Monographs on numerical analysis, Oord,6pp.   
J.H. Wilkinson and C. Reinsch (1970): Linear Algebra, Grundlehren Band 186, Springer Verlag,439 pp.   
A. Wintner and F.D. Murnaghan (1931) : A canonical form for real matrices under orthogonal transformations,Proc. Nat. Acad. Sci. U.S.A., vol.17,p.417 420.   
E.M. Wright (1945): On a sequence defined by a non-linear recurrence formula, J. of London Math. Soc., vol.20, p.68-73.   
E.M. Wright (1946):The non-linear difference-differential equation, Quart. J. of Math., vol.17, p.245-252.   
E.M. Wright (1955): A non-linear difference-differential equation, Jf.d.r.u. angew. Math., vol.194, p.66-87.   
K. Wright (1970): Some relationships between implicut Runge-Kutta collocation and Lanczos T methods，and their sability properties，BI vol.10,p.217-227.   
H. Wronski (1810): Premier principe des methodes algorithmiques comme base de la technique algorithmique, publication refused by the Acad. de Paris (for more details see: S.Dickstein, Int. Math. Congress 1904, p.517).   
M. Zennaro (1986): Natural continuous extensions of Runge-K uta methods, Math. Comput. Vol.46, p.119-133.   
JA. Zonneveld (1963): Automatic integration of ordinary differential equations， Report R743,Mathematisch Centrum, Postbus 4079, 1009AB Amsterdam. Appeared in book form 1964.   
R. Zurmuhl (1948): Runge-Kutt-Verfahren zur numerischen Integration von Differ-entialgleichungen n-ter Ordnung, ZAMM, vol.28, p.173-182.   
R. Zurmuhl (1952): Runge-Kutta Verfahren unter Verwendung hoherer Ableitungen, Z angew. Math. Mech. vol.32, p.153-154.