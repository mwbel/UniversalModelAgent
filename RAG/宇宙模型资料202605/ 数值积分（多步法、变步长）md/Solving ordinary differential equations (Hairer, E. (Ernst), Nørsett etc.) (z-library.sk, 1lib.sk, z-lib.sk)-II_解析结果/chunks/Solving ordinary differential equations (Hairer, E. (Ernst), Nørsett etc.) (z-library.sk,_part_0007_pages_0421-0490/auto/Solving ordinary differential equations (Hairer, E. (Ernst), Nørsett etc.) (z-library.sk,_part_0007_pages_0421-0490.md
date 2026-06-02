![](images/786029a6dcb5d648daf5ca5bdd696139bb039e6fa2a0a36444966a1b12465ecb.jpg)  
Fig.3.1. Global error versus the step size

# Perturbed Initial Values

When integrating a singular perturbation problem, the numerical solution approximates the smooth solution only within the given tolerance $T o l$ . It is therefore interesting to investigate the influence of perturbations in the initial values on the global and local errors of the method. Let us begin with a numerical experiment. We perturb the $z ( 0 )$ value of (3.74) by an amount of $1 0 ^ { - 6 }$ and apply the Radau IIA methods to the problem (3.73). For the global error at ${ x _ { e n d } } \mathrm { = } 0 . 5$ we obtain ex-actly the same results as in Fig.3.1. This shows that the perturbation is completely damped out during integration. The results for the local error show a different behaviour and are displayed in Fig.3.2. We observe the presence of a“hump",exactly as in Fig.IV.7.4 and in Fig.IV.8.2.

![](images/f250347c703cb18d954b7b01d6efd6b0625694e7fa872f340d9a2e9d6893b533.jpg)  
Fig.3.2. Local error of Radau IA (perturbed initial value)

In order to explain this phenomenon we denote by $( y _ { 0 } , z _ { 0 } )$ the considered initial value, and by $( y _ { 1 } , z _ { 1 } )$ the numerical solution after one step with step size $h$ . The exact solution $y ( x ) , z ( x )$ passing through $( y _ { 0 } , z _ { 0 } )$ will have a boundary layer, and (under suitable assumptions, see Theorem 3.2) can be written as

$$
y ( x ) = \widetilde { y } ( x ) + \mathcal { O } ( \varepsilon e ^ { - x / \varepsilon } ) , \qquad z ( x ) = \widetilde { z } ( x ) + \mathcal { O } ( e ^ { - x / \varepsilon } ) .
$$

Here $\widetilde { y } ( \boldsymbol { x } ) , \widetilde { z } ( \boldsymbol { x } )$ represents a smooth solution of (3.1). We denote by $\widetilde { y } _ { 0 } = \widetilde { y } ( 0 )$ ， $\widetilde { z } _ { 0 } = \widetilde { z } ( 0 )$ the initial values on this smooth solution, and by $( \widetilde { y } _ { 1 } , \widetilde { z } _ { 1 } )$ the numerical approximation obtained by the same method with step size $h$ and initial values $( \widetilde { y } _ { 0 } , \widetilde { z } _ { 0 } )$ . The local error can now be written as

$$
z _ { 1 } - z ( h ) = ( z _ { 1 } - \widetilde { z } _ { 1 } ) + ( \widetilde { z } _ { 1 } - \widetilde { z } ( h ) ) + ( \widetilde { z } ( h ) - z ( h ) )
$$

and similarly for the $y$ -component. The last term in (3.76)，which is of size $\mathcal { O } ( T o l \cdot e ^ { - h / \varepsilon } )$ , can be neglected if the step size $h$ is significantly larger than $\varepsilon$ The term $\widetilde { z } _ { 1 } - \widetilde { z } ( h )$ represents the local error in the “smooth” situation and is bounded by at least $\mathcal { O } ( h ^ { q + 1 } )$ (apply Corollary 3.10 with $n = 1$ ). It can be observed in Fig.3.2 whenever $h$ or the error is large. The difference $z _ { 1 } - \widetilde { z } _ { 1 }$ is the term which causes the irregularity in Fig.3.2. Using Theorem 3.6 (with $\delta = 0$ ， $\theta = 0$ ， $\widehat { \eta } - \eta = \mathcal { O } ( \varepsilon \cdot T o l )$ ， $\begin{array} { r } { \widehat { \zeta } - \zeta = \mathcal { O } ( T o l ) , } \end{array}$ and the ideas of the proof of Theorem 3.8 (in particular Eq.(3.62)) we obtain

$$
\begin{array} { r l } & { z _ { 1 } - \widetilde { z } _ { 1 } = R \Big ( \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ( z _ { 0 } - \widetilde { z } _ { 0 } ) + \mathcal { O } ( \varepsilon \cdot T o l ) } \\ & { y _ { 1 } - \widetilde { y } _ { 1 } = \mathcal { O } ( \varepsilon \cdot T o l ) . } \end{array}
$$

For $\varepsilon < h$ we develop

$$
R \Bigl ( { \frac { h } { \varepsilon } } g _ { z } ( 0 ) \Bigr ) = R ( \infty ) + C { \frac { \varepsilon } { h } } g _ { z } ^ { - 1 } ( 0 ) + { \mathcal { O } } \Bigl ( \Bigl ( { \frac { \varepsilon } { h } } \Bigr ) ^ { 2 } \Bigr ) .
$$

This shows that an $h$ -independent expression $R ( \infty ) ( z _ { 0 } - \widetilde { z } _ { 0 } ) = \mathcal { O } ( T o l )$ will be observed in the local error, if $R ( \infty ) \neq 0$ . For methods with $R ( \infty ) = 0$ (such as Radau IA) the dominant part in $z _ { 1 } - \widetilde { z } _ { 1 }$ is $C ( \varepsilon / h ) g _ { z } ^ { - 1 } ( 0 ) ( z _ { 0 } - \widetilde { z _ { 0 } } ) = \mathcal { O } ( T o l \cdot \varepsilon / h )$ This term can be observed in Fig.3.2 as a straight line of slope $- 1$ . Thus in this region the local error increases like $h ^ { - 1 }$ when $h$ decreases. A similar perturbation, multiplied however by $\varepsilon$ , is observed for the $y$ -component.

This is not a serious drawback for a numerical implementation, because the phenomenon appears only for step sizes where the local error is smaller than $T o l$

# Exercises

1. Prove that the statement of Theorem 3.2 remains valid,if the assumption (3.11) is replaced by

for all $y , z$ in a neighbourhood of the solution $y _ { 0 } ( x ) , ~ z _ { 0 } ( x )$ of the reduced system.

Hint. Split the interval into a finite number of small subintervals and construct for each of them an inner product norm such that, after a rescaling of $\varepsilon$ ,(3.11) holds (see Nevanlinna 1976).

2. Let $y ( 0 ) = 2$ ; find the corresponding $z ( 0 )$ for the van der Pol equation (3.73), such that its solution is smooth.

Result.

$$
z ( 0 ) = - { \frac { 2 } { 3 } } + { \frac { 1 0 } { 8 1 } } \varepsilon - { \frac { 2 9 2 } { 2 1 8 7 } } \varepsilon ^ { 2 } - { \frac { 1 8 1 4 } { 1 9 6 8 3 } } \varepsilon ^ { 3 } + { \mathcal { O } } ( \varepsilon ^ { 4 } ) .
$$

3. If the assumption $q < p$ $p$ classical order, $q$ stage order) is dropped in Corollary 3.10, we still have

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) .
$$

Prove this statement. The implicit Euler method and the SIRK methods of Lemma IV.8.1 are typical examples with $p \approx q$

Hint. Apply Corollary 3.10 with $q$ reduced by 1.

This section is devoted to the extension of Rosenbrock methods (see Sect.IV.7) to differential-algebraic equations in semi-explicit form

$$
\begin{array} { r } { { \boldsymbol { y } } ^ { \prime } = f ( { \boldsymbol { y } } , z ) , \qquad { \boldsymbol { y } } ( { \boldsymbol { x } } _ { 0 } ) = { \boldsymbol { y } } _ { 0 } } \\ { 0 = g ( { \boldsymbol { y } } , z ) , \qquad z ( { \boldsymbol { x } } _ { 0 } ) = z _ { 0 } . } \end{array}
$$

We suppose that $g _ { z }$ is invertible (see (1.7))，so that the problem is of index 1. We shall obtain new methods for the numerical solution of such problems,and at the same time get more insight into the behaviour of Rosenbrock methods for stiff differential equations. In particular, the phenomenon of Fig.IV.7.4 will be explained.

# Definition of the Method

The main advantage of Rosenbrock methods over implicit Runge-Kutta methods is that nonlinear systems are completely avoided. The state space form method (transforming (4.1) to $y ^ { \prime } = f ( y , G ( y ) )$ ） would destroy this advantage. This is one more reason for considering the $\varepsilon$ -embedding method. For the problem (1.5）a Rosenbrock method reads

$$
\binom { k _ { z } } { \ell _ { \ast } } = h \left( { \begin{array} { c } { f ( v _ { \ast } , w _ { \iota } ) } \\ { \varepsilon ^ { - 1 } g ( v _ { \ast } , w _ { \iota } ) } \end{array} } \right) + h \left( { \begin{array} { c c } { f _ { y } } & { f _ { z } } \\ { \varepsilon ^ { - 1 } g _ { y } } & { \varepsilon ^ { - 1 } g _ { z } } \end{array} } \right) ( y _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \imath _ { \jmath } } \binom { k _ { \jmath } } { \ell _ { \jmath } }
$$

$$
\left( \begin{array} { l } { { v _ { \mathfrak { _ { \lambda } } } } } \\ { { w _ { \mathfrak { _ { \lambda } } } } } \end{array} \right) = \left( \begin{array} { l } { { y _ { 0 } } } \\ { { z _ { 0 } } } \end{array} \right) + \sum _ { \substack { \jmath = 1 } } ^ { \imath - 1 } \alpha _ { \mathfrak { _ { \imath } } \jmath } \left( \begin{array} { l } { { k _ { \jmath } } } \\ { { \ell _ { \jmath } } } \end{array} \right) , \qquad \left( \begin{array} { l } { { y _ { 1 } } } \\ { { z _ { 1 } } } \end{array} \right) = \left( \begin{array} { l } { { y _ { 0 } } } \\ { { z _ { 0 } } } \end{array} \right) + \sum _ { \substack { \imath = 1 } } ^ { s } b _ { \imath } \left( \begin{array} { l } { { k _ { \jmath } } } \\ { { \ell _ { \imath } } } \end{array} \right) .
$$

If we multiply the second line of (4.2) by $\varepsilon$ and then put $\varepsilon = 0$ we obtain

$$
\left( \begin{array} { l } { k _ { \ i } } \\ { 0 } \end{array} \right) = h \left( \begin{array} { l } { f ( v _ { \ i } , w _ { \iota } ) } \\ { g ( v _ { \iota } , w _ { \iota } ) } \end{array} \right) + h \left( \begin{array} { l l } { f _ { y } } & { f _ { z } } \\ { g _ { y } } & { g _ { z } } \end{array} \right) ( y _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \iota _ { \jmath } } \left( \begin{array} { l } { k _ { \jmath } } \\ { \ell _ { \jmath } } \end{array} \right) .
$$

Formulas (4.3a) and (4.3b) together constitute the extension of a Rosenbrock method to the problem (4.1). This type of method was first considered by Michelsen (1976) (quoted by Feng, Holland & Gallun (1984)). Further studies are due to Roche

(1988). We remark that the computation of $( k _ { \imath } , \ell _ { i } )$ from (4.3b) requires the solu-tion of a linear system with matrix

$$
\left( \begin{array} { c c } { I - \gamma h f _ { y } } & { - \gamma h f _ { z } } \\ { - \gamma h g _ { y } } & { - \gamma h g _ { z } } \end{array} \right)
$$

where all derivatives are evaluated at $( y _ { 0 } , z _ { 0 } )$ . For nonsingular $g _ { z }$ , nonzero $\gamma$ ,and small enough $h > 0$ ,this matrix is invertible. This can be seen by dividing the lower blocks by $\gamma h$ and then putting $h = 0$

Non-autonomous equations. If the functions $f$ and $g$ in (4.1) also depend on $\boldsymbol { \mathscr { x } }$ ， we replace (4.3b) by

$$
\left( { \begin{array} { c } { k _ { _ { 1 } } } \\ { 0 } \end{array} } \right) = h \left( { \begin{array} { c } { f ( x _ { _ { 0 } } + \alpha _ { _ { 1 } } h , v _ { _ { 1 } } , w _ { _ { 1 } } ) } \\ { g ( x _ { _ { 0 } } + \alpha _ { _ { 1 } } h , v _ { _ { 1 } } , w _ { _ { 1 } } ) } \end{array} } \right) + h \left( { \begin{array} { c c } { f _ { _ { y } } } & { f _ { z } } \\ { g _ { _ { y } } } & { g _ { z } } \end{array} } \right) \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { _ { 1 } \jmath } \left( { k _ { \jmath } \atop \ell _ { \jmath } } \right) + h ^ { 2 } \gamma _ { _ { 1 } } \left( { f _ { _ { x } } } \right)
$$

(compare with (IV.7.4a) and recall the definition of $\alpha _ { \iota }$ and $\gamma _ { \imath }$ in (IV.7.5)). All derivatives are evaluated at the initial value $\left( x _ { 0 } , y _ { 0 } , z _ { 0 } \right)$

Problems of the form $M u ^ { \prime } = \varphi ( u )$ . Rosenbrock formulas for these problems have been developed in Sect.IV.7 (Formula (IV.7.4b)) in the case of regular $M$ . This formula is also applicable for singular $M$ ，and can be justified as follows: It is theoretically possible to apply the transformation（1.2O) so that $M$ becomes the block-diagonal matrix with entries $I$ and O. The method (IV.7.4b) is then identical to method (4.3). Therefore, the theory to be developed in this section will also be valid for Rosenbrock method (IV.7.4b) applied to index 1 problems of the form $M u ^ { \prime } = \varphi ( u )$

Having introduced a new class of methods,we must study their order conditions. As usual, this is done by Taylor expansion of both the exact and the numerical solution (similar to Section I.2). A nice correspondence between the order condi-tions and certain rooted trees with two different kinds of vertices will be obtained (Roche 1988).

# Derivatives of the Exact Solution

In contrast to Sect.II.2, where we used “hordes of indices" (see Dieudonné's preface to his “Foundations of Modern Analysis"） to show us the way through the “woud met bomen” (Hundsdorfer), we here write higher derivatives as multilinear mappings. For example, the expression

$$
\sum _ { \ j , k } \frac { \partial ^ { 2 } g _ { i } } { \partial y _ { \ j } \partial z _ { k } } \cdot u _ { \ j } v _ { k } \quad \mathrm { \ i s { w r i t t e n } { a s } } \quad g _ { y z } ( u , \upsilon ) ,
$$

which simplifies the subsequent formulas.

We differentiate (4.1b) to obtain $0 = g _ { y } \cdot y ^ { \prime } + g _ { z } \cdot z ^ { \prime }$ and, equivalently,

$$
z ^ { \prime } = ( - g _ { z } ^ { - 1 } ) g _ { y } f .
$$

We now differentiate successively (4.1a) and (4.6) with respect to $\boldsymbol { \mathscr { x } }$ . We use the formula

$$
( - g _ { z } ^ { - 1 } ) ^ { \prime } u = \left( - g _ { z } ^ { - 1 } \right) \left( g _ { z y } { \left( \bigl ( - g _ { z } ^ { - 1 } \bigr ) u , f \right) } + g _ { z z } { \left( \bigl ( - g _ { z } ^ { - 1 } \bigr ) u , \bigl ( - g _ { z } ^ { - 1 } \bigr ) g _ { y } f \right) } \right)
$$

which is a consequence of $( A ^ { - 1 } ( x ) ) ^ { \prime } { = } { - } A ^ { - 1 } ( x ) A ^ { \prime } ( x ) A ^ { - 1 } ( x )$ and the chain rule. This gives

$$
y ^ { \prime \prime } = f _ { y } \cdot y ^ { \prime } + f _ { z } \cdot z ^ { \prime } = f _ { y } f + f _ { z } ( - g _ { z } ^ { - 1 } ) g _ { y } f
$$

$$
z ^ { \prime \prime } = ( - g _ { z } ^ { - 1 } ) { \Big ( } g _ { z y } ( ( - g _ { z } ^ { - 1 } ) g _ { y } f , f ) + g _ { z z } ( ( - g _ { z } ^ { - 1 } ) g _ { y } f , ( - g _ { z } ^ { - 1 } ) g _ { y } f ) { \Big ) }
$$

$$
+ ( - g _ { z } ^ { - 1 } ) \Big ( g _ { y y } ( f , f ) + g _ { y z } ( f , ( - g _ { z } ^ { - 1 } ) g _ { y } f \Big )
$$

$$
+ ( - g _ { z } ^ { - 1 } ) g _ { y } \Big ( f _ { y } f + f _ { z } ( - g _ { z } ^ { - 1 } ) g _ { y } f \Big ) .
$$

Clearly, these expressions soon become very complicated and a graphical representation of the terms in (4.8) and (4.9) is desirable.

# Trees and Elementary Differentials

We shall identify each occuring $f$ with a meagre vertex, and each of its deriva-tives with an upward leaving branch. The expression $( - g _ { z } ^ { - 1 } ) g$ is identified with a fat vertex. The derivatives of $g$ therein are again indicated by upwards leaving branches. For example,the second expression of (4.8) and the first one of (4.9) correspond to the trees in Fig. 4.1.

The above formulas for $y ^ { \prime } , z ^ { \prime } , y ^ { \prime \prime } , z ^ { \prime \prime }$ thus become

$$
\left. \begin{array} { l } { { y ^ { \prime } = \bullet } } \\ { { \ z ^ { \prime \prime } = \bigwedge \quad \ z ^ { \prime \prime } = \not { C } \Im \big \langle \displaystyle \hat { \big \langle } \ y \vee \Big \rangle \ \geq \ \not { C } \big \rangle } } \end{array} \right\}
$$

The first and fourth expressions in(4.9) are identical, because $g _ { z y } ( u , v ) { = } g _ { y z } ( v , u )$ This is in nice accordance with the fact that the corresponding"trees are topologically equivalent. The lowest vertex of a tree will be called its root.

We see that derivatives of $y$ are characterized by trees with a meagre root. These trees will be denoted by $t$ or $t _ { \imath }$ , the tree consisting only of the root (for $y ^ { \prime }$ ） being $\tau _ { y }$ . Derivatives of $z$ have trees with a fat root. These will be written as $u$ or $u _ { i }$ , the tree for $z ^ { \prime }$ being $\tau _ { z }$

$$
\int \limits _ { f _ { z } } ^ { f } \biggl \langle d z ^ { - 1 } \biggr \rangle g _ { y } \qquad ( - g _ { z } ^ { - 1 } ) g _ { y } \biggl \langle \overset { f } { \underbrace { et { } { ' } \mathstrut } } \biggr \rangle f _ { ( - g _ { z } ^ { - 1 } ) g _ { z y } } ^ { f }
$$

Fig. 4.1. Graphical representation of elementary differentials

Definition 4.1. Let $D A T = D A T _ { y } \cup D A T _ { z }$ denote the set of (differential algebraic rooted) trees defined recursively by

a) $\tau _ { y } \in D A T _ { y } , \tau _ { z } \in D A T _ { z } ;$   
b） $[ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots u _ { n } ] _ { y } \in D A T _ { y }$ if $t _ { 1 } , \ldots , t _ { m } \in D A T _ { y }$ and $u _ { 1 } , \ldots u _ { n } \in D A T _ { z }$   
c） $[ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { z } \in D A T _ { z }$ if $t _ { 1 } , \ldots , t _ { m } \in D A T _ { y }$ ， $u _ { 1 } , \ldots , u _ { n } \in D A T _ { z }$ , and $( m , n ) \neq ( 0 , 1 )$

Here $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ and $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z }$ represent unordered $( m + n )$ -tuples.

The graphical representation of these trees is as follows: if we connect the roots of $t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n }$ by $m + n$ branches to a new meagre vertex (the new root） we obtain $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ ; if we connect them to a new fat vertex we obtain $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z }$ . For example, the two trees of Fig.4.1 can be written as $\left\{ \tau _ { z } \right\} _ { y }$ and $[ \tau _ { z } , \tau _ { y } ] _ { z }$

Definition 4.2. The order of a tree $t \in D A T _ { y }$ or $u \in D A T _ { z }$ ， denoted by $\varrho ( t )$ or $\varrho ( u )$ , is the number of its meagre vertices.

We see in (4.1O) that this definition of order coincides with the derivative order of $y ^ { ( \imath ) }$ or $z ^ { ( \imath ) }$ as far as they are computed there.

We next give a recursive definition of the one-to-one correspondence between the trees in (4.10) and the expressions in (4.8) and (4.9).

Definition 4.3. The elementary differentials $F ( t )$ （or $F ( u )$ ) corresponding to trees in $D A T$ are defined as follows:

$$
\begin{array} { l } { { F ( \tau _ { y } ) = f , F ( \tau _ { z } ) = ( - g _ { z } ^ { - 1 } ) g _ { y } f , } } \\ { { F ( t ) = \displaystyle \frac { \partial ^ { m + n } f } { \partial y ^ { m } \partial z ^ { n } } \left( F ( t _ { 1 } ) , \ldots , F ( t _ { m } ) , F ( u _ { 1 } ) , \ldots , F ( u _ { n } ) \right) } } \\ { { \mathrm { ~ i f ~ } t = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y } \in D A T _ { y } , } } \\ { { F ( u ) = ( - g _ { z } ) ^ { - 1 } \displaystyle \frac { \partial ^ { m + n } g } { \partial y ^ { m } \partial z ^ { n } } \left( F ( t _ { 1 } ) , \ldots , F ( t _ { m } ) , F ( u _ { 1 } ) , \ldots , F ( u _ { n } ) \right) } } \\ { { \mathrm { ~ i f ~ } u = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z } \in D A T _ { z } . } } \end{array}
$$

Because of the symmetry of partial derivatives,this definition is unaffected by a permutation of $t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n }$ and therefore the functions $F ( t )$ and $F ( u )$ are well defined.

# Taylor Expansion of the Exact Solution

In order to get more insight into the process of (4.8) and (4.9) we study the differentiation of an elementary differential with respect to $x$ . By Leibniz' rule the differentiation of $F ( t )$ (or $F ( u ) )$ gives a sum of new elementary differentials which are obtained by the following four rules:

i) attach to each vertex a branch with $\tau _ { y }$ (derivative of $f$ or $g$ with respect to $y$ and addition of the factor $y ^ { \prime } = f$ ；   
ii） attach to each vertex a branch with $\tau _ { z }$ (derivative of $f$ or $g$ with respect to $z$ and addition of the factor $z ^ { \prime } = ( - g _ { z } ^ { - 1 } ) g _ { y } f )$ ；   
iii） split each fat vertex into two new fat vertices (linked by a new branch) and attach tothe lowerofthesefatverticesabranch with $\tau _ { y }$   
iv) as in (ii) split each fat vertex into two new fat vertices,but attach this time to the lower of the new fat vertices a branch with $\tau _ { z }$

The rules (iii) and (iv) correspond to the differentiation of $( - g _ { z } ^ { - 1 } )$ and follow at once from (4.7). We observe that the differentiation of a tree of order $q$ (or, more precisely,of its corresponding elementary differential） generates trees of order $q + 1$

As was the case in Sect.I.2, some of these trees appear several times in the derivative (as the first and fourth tree for $z ^ { \prime \prime }$ in (4.1O)). In order to distinguish all these trees, we indicate the order of generation of the meagre vertices by labels. This is demonstrated, for the first derivatives of $y$ , in Fig. 4.2. Since in the above differentiation process the new meagre vertex is always an end-vertex of the tree, the labelling thus obtained is necessarily increasing from the root upwards along each branch.

![](images/c0f9376f2b717e6f0682d9e48efc43629e736e590a5a463eb5ac21050ae9d486.jpg)  
Fig. 4.2. Monotonically labelled trees $( L D A T _ { y }$

Definition 4.4. A tree $t \in D A T _ { y }$ (or $u \in D A T _ { z }$ )together with a monotonic labelling of its meagre vertices is called a monotonically labelled tree. The sets of all such monotonically labelled trees are denoted by $L D A T _ { y } , L D A T _ { z }$ and LDAT.

Definition 4.2 (order of a tree) and Definition 4.3 (elementary differential) are extended in a natural way to monotonically labelled trees. We can therefore write the derivatives of the exact solution as follows:

Theorem 4.5 (Roche 1988). For the exact solution of(4.1) we have:

$$
\begin{array} { l } { { y ^ { ( q ) } ( x _ { 0 } ) = \displaystyle \sum _ { \substack { t \in L D A T _ { y } , \varrho ( t ) = q } } F ( t ) ( y _ { 0 } , z _ { 0 } ) = \displaystyle \sum _ { \substack { t \in D A T _ { y } , \varrho ( t ) = q } } \alpha ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) \hfill } } \\ { { z ^ { ( q ) } ( x _ { 0 } ) = \displaystyle \sum _ { \substack { u \in L D A T _ { z } , \varrho ( u ) = q } } F ( u ) ( y _ { 0 } , z _ { 0 } ) = \displaystyle \sum _ { \substack { u \in D A T _ { z } , \varrho ( u ) = q } } \alpha ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) \hfill } } \end{array}
$$

The integer coefficients $\alpha ( t )$ and $\alpha ( u )$ indicate the number of possible monotonic labellings of a tree.

Proof. For $q = 1$ and $q = 2$ this is just (4.1a), (4.6), (4.8) and (4.9). For general $q$ the above differentiation process of trees generates all elements of $L D A T$ ,each element exactly once. If the sum is taken over $D A T _ { y }$ and $D A T _ { z }$ ，the factors $\alpha ( t )$ and $\alpha ( u )$ must be added. □

# Taylor Expansion of the Numerical Solution

Our next aim is to prove an analogue of Theorem 4.5 for the numerical solution of a Rosenbrock method. We consider $y _ { 1 } , z _ { 1 }$ as functions of the step size $h$ and compute their derivatives.From (4.3a) it follows that

$$
y _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } ^ { ( q ) } ( 0 ) , \qquad z _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { \iota = 1 } ^ { s } b _ { i } \ell _ { \iota } ^ { ( q ) } ( 0 ) .
$$

Consequently we have to compute the derivatives of $k _ { \imath }$ and $\ell _ { \ i }$ . This is done as for Runge-Kutta methods (Sect.II.2) or for Rosenbrock methods applied to ordinary differential equations (Sect.IV.7).

We differentiate the first line of (4.3b) with respect to $h$ . Using Leibniz’ rule (II.2.4) this yields for $h \approx 0$

$$
k _ { i } ^ { ( q ) } = q \big ( f ( v _ { i } , w _ { i } ) \big ) ^ { ( q - 1 ) } + ( f _ { y } ) _ { 0 } q \sum _ { j = 1 } ^ { \iota } \gamma _ { i j } k _ { j } ^ { ( q - 1 ) } + ( f _ { z } ) _ { 0 } q \sum _ { j = 1 } ^ { \iota } \gamma _ { i j } \ell _ { j } ^ { ( q - 1 ) } .
$$

The index O in $( f _ { y } ) _ { 0 }$ and $( f _ { z } ) _ { 0 }$ indicates that the derivatives are evaluated at $( y _ { 0 } , z _ { 0 } )$ .The second line of (4.3b) is divided by $h$ before differentiation. This gives (again for $h = 0$ ）

$$
0 = \left( g ( v _ { \imath } , w _ { i } ) \right) ^ { ( q ) } + ( g _ { y } ) _ { 0 } \sum _ { j = 1 } ^ { i } \gamma _ { \imath j } k _ { j } ^ { ( q ) } + ( g _ { z } ) _ { 0 } \sum _ { j = 1 } ^ { \imath } \gamma _ { \imath j } \ell _ { j } ^ { ( q ) } .
$$

The derivatives of $f$ and $g$ can be computed by Faa di Bruno's formula (Lemma II.2.8). This yields

$$
\left( f ( v _ { i } , w _ { i } ) \right) ^ { ( q - 1 ) } = \sum \frac { \partial ^ { m + n } f ( v _ { \ i } , w _ { \ i } ) } { \partial y ^ { m } \partial z ^ { n } } \left( v _ { i } ^ { ( \mu _ { 1 } ) } , \ldots , v _ { \ i } ^ { ( \mu _ { m } ) } , w _ { \ i } ^ { ( \nu _ { 1 } ) } , \ldots , w _ { i } ^ { ( \nu _ { n } ) } \right)
$$

where the sum is over all“special $L D A T _ { y } ^ { \mathrm { ~ } \bullet \mathrm { ~ } }$ of order $q$ . These are monotonically labelled trees $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ where $t _ { j }$ and $u _ { \ j }$ do not have any ramifica-tion and alltheir vertices are meagre with the exception of the roots of $u _ { 1 } , \ldots , u _ { n } .$ The integers $\mu _ { j }$ and $\nu _ { j }$ are the orders of $t _ { j }$ and $u _ { j }$ ， respectively. They satisfy $\mu _ { 1 } + . . . + \mu _ { m } + \nu _ { 1 } + . . . + \nu _ { n } = q - 1$ . Similarly we apply Faa di Bruno's formula to $g$ and obtain

$$
\begin{array} { c } { \displaystyle \left( g ( v _ { i } , w _ { \imath } ) \right) ^ { ( q ) } = \sum \displaystyle \frac { \partial ^ { m + n } g ( v _ { \imath } , w _ { i } ) } { \partial y ^ { m } \partial z ^ { n } } \left( v _ { i } ^ { ( \mu _ { 1 } ) } , \ldots , v _ { \imath } ^ { ( \mu _ { m } ) } , w _ { i } ^ { ( \nu _ { 1 } ) } , \ldots , w _ { i } ^ { ( \nu _ { n } ) } \right) } \\ { \displaystyle + g _ { z } ( v _ { \imath } , w _ { i } ) w _ { i } ^ { ( q ) } . } \end{array}
$$

Here the sum is over all“special $L D A T _ { z } ^ { \mathrm { ~ } \bullet \prime }$ of order $q$ . They are defined as above but have a fat vertex. The integers $\mu _ { \ j } , \nu _ { j }$ satisfy $\mu _ { 1 } + \ldots + \mu _ { m } + \nu _ { 1 } + \ldots + \nu _ { n } = q$ The term with $g _ { z }$ is written separately,because (by the definition of $L D A T _ { z }$ ） $\left\{ u _ { 1 } \right\} _ { z }$ is not an admissible tree.

We are now in a position to compute the derivatives of $k _ { i }$ and $\ell _ { i }$ . For this it is convenient to introduce the notation

$$
\beta _ { i j } = \alpha _ { \iota j } + \gamma _ { i j }
$$

(with $\alpha _ { i i } = 0$ ) as in (IV.7.12). We also need the inverse of the matrix $( \beta _ { \imath j } )$ ,whose coefcients we denote by $\omega _ { i j }$ ：

$$
( \omega _ { i j } ) = ( \beta _ { \ i j } ) ^ { - 1 } .
$$

Theorem 4.6. The derivatives of $k _ { i }$ and $\ell _ { i }$ satisfy

$$
\begin{array} { l } { { k _ { i } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle { t \in L D A T _ { y } , \varrho ( t ) = q } } \gamma ( t ) \Phi _ { i } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \ell _ { i } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle u \in L D A T _ { z } , \varrho ( u ) = q } \gamma ( u ) \Phi _ { i } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) , } } \end{array}
$$

where the coefficients $\Phi _ { i } ( t )$ and $\Phi _ { i } ( u )$ are given by $\Phi _ { \imath } ( \tau _ { y } ) = 1$ ， $\Phi _ { i } ( \tau _ { z } ) = 1$ and

$$
\Phi _ { i } ( t ) = \left\{ \begin{array} { l l } { { \displaystyle \sum _ { \mu _ { 1 } , \dots , \mu _ { m } , \nu _ { 1 } , \dots , \nu _ { n } } \alpha _ { \iota _ { \mu _ { 1 } } } \cdot \cdot \cdot \alpha _ { i \mu _ { m } } \alpha _ { \iota \nu _ { 1 } } \cdot \cdot \cdot \alpha _ { i \nu _ { n } } } } _ { \iota _ { \mu _ { 1 } } }  & { { \mathrm { ~ } } } \\ { { \quad \cdot \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } ) \Phi _ { \nu _ { 1 } } ( u _ { 1 } ) \cdot \cdot \cdot \Phi _ { \nu _ { n } } ( u _ { n } ) } } & { { \mathrm { ~ } } } \\ { { \quad \quad } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( t _ { 1 } ) } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( u _ { 1 } ) } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( u _ { 1 } ) } } & { { \mathrm { ~ } } } \end{array} \right.
$$

$$
\Phi _ { \imath } ( u ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { \jmath , \mu _ { 1 } , \ldots , \mu _ { m } , \nu _ { 1 } , \ldots , \nu _ { n } } \omega _ { i j } \alpha _ { j \mu _ { 1 } } \cdot \cdot \cdot \alpha _ { j \mu _ { m } } \alpha _ { \jmath \nu _ { 1 } } \cdot \cdot \cdot \alpha _ { j \nu _ { n } } } & \\ { \quad \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } ) \Phi _ { \nu _ { 1 } } ( u _ { 1 } ) \cdot \cdot \cdot \Phi _ { \nu _ { n } } ( u _ { n } ) } & \\ { \quad \quad \quad \quad i f u = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z } a n d m + n \geq 2 } \\ { \Phi _ { i } ( t _ { 1 } ) } & { \quad \quad \quad i f u = [ t _ { 1 } ] _ { z } } \end{array} \right.
$$

and the integer coefficients $\gamma ( t )$ and $\gamma ( u )$ are defined by $\gamma ( \tau _ { y } ) = 1 , \ \gamma ( \tau _ { z } ) = 1$ and

$$
\begin{array} { r l } & { \gamma ( t ) = \varrho ( t ) \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) \gamma ( u _ { 1 } ) \dots \gamma ( u _ { n } ) \quad i f t = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { y } } \\ & { \gamma ( u ) = \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) \gamma ( u _ { 1 } ) \dots \gamma ( u _ { n } ) \qquad i f u = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { z } . } \end{array}
$$

Proof. By (4.3a) we have

$$
v _ { \imath } ^ { ( \mu ) } = \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { \imath \jmath } k _ { \jmath } ^ { ( \mu ) } , \qquad w _ { \imath } ^ { ( \nu ) } = \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } \ell _ { \jmath } ^ { ( \nu ) } .
$$

We now insert (4.19) into (4.14) and the resulting formula for $( f ( v _ { \iota } , w _ { i } ) ) ^ { ( q - 1 ) }$ into (4.12). This yields (all expressions have to be evaluated at $h \approx 0$ ）

$$
\begin{array} { c } { { k _ { \imath } ^ { ( q ) } = q \displaystyle \sum _ { m + n \geq 2 } \displaystyle \frac { \partial ^ { m + n } f ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \displaystyle \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { \imath j } k _ { \jmath } ^ { ( \mu _ { 1 } ) } , \ldots , \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { i _ { j } } \ell _ { j } ^ { ( \nu _ { 1 } ) } , \ldots \right) } } \\ { { + q ( f _ { y } ) _ { 0 } \displaystyle \sum _ { \jmath = 1 } ^ { i } \beta _ { \imath j } k _ { \jmath } ^ { ( q - 1 ) } + q ( f _ { z } ) _ { 0 } \displaystyle \sum _ { j = 1 } ^ { \imath } \beta _ { \imath j } \ell _ { j } ^ { ( q - 1 ) } . } } \end{array}
$$

The same analysis for the second component leads to

$$
\begin{array} { l } { { \displaystyle 0 = \sum _ { m + n \geq 2 } \frac { \partial ^ { m + n } g ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } k _ { j } ^ { ( \mu _ { 1 } ) } , \dots , \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } \ell _ { j } ^ { ( \nu _ { 1 } ) } , \dots \right) } } \\ { { \displaystyle \qquad + ( g _ { y } ) _ { 0 } \sum _ { j = 1 } ^ { i } \beta _ { i j } k _ { j } ^ { ( q ) } + ( g _ { z } ) _ { 0 } \sum _ { j = 1 } ^ { i } \beta _ { i j } \ell _ { j } ^ { ( q ) } . } } \end{array}
$$

The sums in (4.20) and (4.21) are over elements of $L D A T$ exactly as in (4.14) and (4.15). Equation (4.21) allows us to extract $\ell _ { i } ^ { ( q ) }$ if we use the inverse of (βij). This gives

$$
\begin{array} { l } { { \displaystyle { \bf \zeta } _ { i } ^ { ( q ) } = \left( - g _ { z } \right) _ { 0 } ^ { - 1 } \sum _ { j = 1 } ^ { i } \omega _ { i j } \sum _ { m + n \geq 2 } \frac { \partial ^ { m + n } g ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { \kappa = 1 } ^ { j - 1 } \alpha _ { j \kappa } k _ { \kappa } ^ { ( \mu _ { 1 } ) } , \dots , \sum _ { \kappa = 1 } ^ { j - 1 } \alpha _ { j \kappa } \ell _ { \kappa } ^ { ( \nu _ { 1 } ) } , \dots , \sum _ { \kappa = 1 } ^ { i - 1 } \alpha _ { j \kappa } k _ { \kappa } ^ { ( \mu _ { 1 } ) } \right) } } \\ { { \displaystyle \qquad + \left( ( - g _ { z } ^ { - 1 } ) g _ { y } \right) _ { 0 } k _ { i } ^ { ( q ) } . \qquad \quad { \scriptstyle ( 4 . 2 2 \kappa ) } } } \end{array}
$$

The proof of Formula (4.18) is now by induction on $q$ . The case $q = 1$ follows immediately from (4.12) and (4.13). For general $q$ , we insert the induction hypothesis into (4.20) and (4.22),exploit the multilinearity of the derivatives,and arrange the summations as in the proof of Theorem II.2.11. □

Finally, Eq.(4.11) yields the derivatives of the numerical solution.

Theorem 4.7 (Roche 1988). The numerical solution of(4.3) satisfies:

$$
\begin{array} { l } { { \displaystyle y _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { t \in L D A T _ { y } , \varrho ( t ) = q } \gamma ( t ) \sum _ { \iota = 1 } ^ { s } b _ { \iota } \Phi _ { \iota } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \displaystyle z _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { \iota \in L D A T _ { z } , \varrho ( u ) = q } \gamma ( u ) \sum _ { i = 1 } ^ { s } b _ { \iota } \Phi _ { i } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) } } \end{array}
$$

where the coefficients $\gamma$ and $\Phi _ { \imath }$ are given in Theorem 4.6.

# Order Conditions

Comparing Theorem 4.5 and 4.7 we obtain

Theorem 4.8. For the Rosenbrock method (4.3) we have:

$$
\begin{array} { r l } { y ( x _ { 0 } + h ) - y _ { 1 } = \mathcal { O } ( h ^ { p + 1 } ) } & { i f f } \\ { \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } \Phi _ { i } ( t ) = \frac { 1 } { \gamma ( t ) } \quad } & { f o r t \in D A T _ { y } , \varrho ( t ) \le p ; } \end{array}
$$

$$
\begin{array} { r l } { z ( x _ { 0 } + h ) - z _ { 1 } = \displaystyle { \mathcal { O } ( h ^ { q + 1 } ) } i f f \quad } & { } \\ { \displaystyle { \sum _ { \imath = 1 } ^ { s } b _ { \imath } \Phi _ { \imath } ( u ) } = \frac { 1 } { \gamma ( u ) } \quad } & { \ f o r u \in D A T _ { z } , \varrho ( u ) \leq q , } \end{array}
$$

where the coeffcients $\Phi _ { i }$ and $\gamma$ are those of Theorem 4.6.

Repeated application of the recursive definition of $\Phi _ { \imath }$ in Theorem 4.6 yields the following algorithm:

Forming the Order Condition for a Given Tree: atach to each meagre vertex one summation index,and to each fat vertex two indices (one above the other). Then the left hand side of the order condition is a sum over all indices of a product with factors

$b _ { i }$ if $^ { \mathfrak { s } } { } _ { i } \mathbf { \vec { \mu } } ^ { \mathfrak { s } }$ is the index of the root (the lower index if the root is fat); $\alpha _ { \imath j }$ if $^ { 6 6 } j ^ { 3 }$ lies directly above $^ { \mathfrak { s } \mathfrak { e } ^ { \mathfrak { s } } \mathfrak { z } }$ and $^ { 6 6 } i ^ { , 9 }$ is multiply branched; βi if $^ { 6 6 } \vec { \mathcal { I } } ^ { \ ' }$ lies directly above $^ { 6 6 } i ^ { 7 3 }$ and $^ { \mathfrak { s } \mathfrak { e } ^ { \mathfrak { s } } \mathfrak { z } }$ is singly branched; $\omega _ { i j }$ if $^ { \mathbf { \omega } _ { ^ { 6 6 } i , j } ^ { \mathbf { \omega } } }$ are the two indices of a fat vertex $( ^ { 6 6 } i ^ { 3 3 } \mathrm { b e l o w } ^ { 6 6 } j ^ { 3 3 } )$

![](images/5d5ddc51cfdc4133ee2ec71e572850fcd0157e54685fa6bbc898cc4401986950.jpg)  
Fig. 4.3. Trees with labelling

As an example, we present the order conditions for the first two trees of Fig.4.3.

$$
\begin{array} { c } { { \displaystyle { \sum _ { i , j , k , \ell , m } b _ { i } \alpha _ { i j } \alpha _ { i k } \omega _ { k \ell } \beta _ { \ell m } = \frac { 1 } { 3 } } } } \\ { { { \displaystyle { \sum _ { i , j , k , \ell , m , n , p } b _ { \iota } \omega _ { i j } \alpha _ { j k } \alpha _ { j \ell } \omega _ { \ell m } \alpha _ { m n } \alpha _ { m p } = 1 } } . } } \end{array}
$$

The condition (4.23)can be further simplified if we use the fact that $\left( \omega _ { \imath j } \right)$ is the inverse of the matrix $( \beta _ { i j } )$ . Indeed, (4.23) is equivalent to

$$
\sum _ { i , j , k } b _ { i } \alpha _ { i j } \alpha _ { i k } = \frac { 1 } { 3 }
$$

which is the order condition for the third tree inFig.4.3. Exploiting this reduction systematically we arrive at the following result.

Lemma 4.9. For a Rosenbrock method (4.3) the order conditions corresponding to one of the following situations are redundant:

a) a fat vertex is singly branched.   
b) a singly branched vertex is followed by a fat vertex.

The subset of $D A T _ { y }$ which consists of trees with only meagre vertices, is simply $T$ (the set of trees of Sect.II.2). The corresponding order conditions are those given in Sect.IV.7. Consequently, a $p$ -th order Rosenbrock method has to satisfy all “classical” order conditions and, in addition, several “algebraic” conditions. The first of these new order conditions are given in Table 4.1. We have included the polynomial $p _ { t } ( \gamma )$ in its last column,which is the right-hand side of the order condition, when written in the form (IV.7.11').

# Convergence

Before we proceed to the actual construction of a new Rosenbrock method, we still have to study its convergence property. The following result will also involve

$$
R ( \infty ) = 1 - b ^ { T } B ^ { - 1 } \mathbb { 1 } = 1 - \sum _ { \iota , j } b _ { i } \omega _ { \iota j }
$$

where $R ( z )$ is the stability function (IV.7.14).

Table 4.1. Trees and elementary differentials   

<table><tr><td>g(t）</td><td>t</td><td>graph</td><td>r(t）</td><td>(t）</td><td>Pt(y)</td></tr><tr><td>4</td><td>t45</td><td></td><td>4</td><td>∑ajkaJewlmamnamp</td><td>1/4</td></tr><tr><td>2</td><td>u21</td><td></td><td>1</td><td>Mwkakeakm</td><td>1</td></tr><tr><td>3 3</td><td>u31</td><td></td><td>1 2</td><td>MwJkakeakmakn ∑wJkaklakmβmn</td><td>1 1/2-Y</td></tr><tr><td>3</td><td>u32</td><td></td><td>1</td><td>∑wjkakeαkmwmnanpanq</td><td>1</td></tr><tr><td></td><td>u33</td><td></td><td></td><td></td><td></td></tr></table>

We denote the local error of the Rosenbrock method (4.3) by

$$
\delta y _ { h } ( x ) = y _ { 1 } - y ( x + h ) , \qquad \delta z _ { h } ( x ) = z _ { 1 } - z ( x + h ) .
$$

Here $y _ { 1 } , z _ { 1 }$ is the numerical solution obtained with the exact initial values $y _ { 0 } =$ $y ( x )$ ， $z _ { 0 } = z ( x )$ ·

Theorem 4.10. Suppose that $g _ { z }$ is regular in $a$ neighbourhood of the solution $( y ( x ) , z ( x ) )$ of(4.1) and that the initial values $( y _ { 0 } , z _ { 0 } )$ are consistent. If the stability function is such that $| R ( \infty ) | < 1$ , and the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad \delta z _ { h } ( x ) = \mathcal { O } ( h ^ { p } ) ,
$$

then the Rosenbrock method (4.3) is convergent of order $p ; i . e . ,$

$$
y _ { n } - y ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \quad z _ { n } - z ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) \quad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t .
$$

Proof. Since $g _ { z }$ is regular we have

$$
\| g _ { z } ^ { - 1 } ( y , z ) g ( y , z ) \| \leq \delta
$$

for $( y , z )$ in acompact neighbourhood $\mathcal { U }$ of the solution. The $h$ -independent value of $\delta$ can be made arbitrarily small by shrinking $\mathcal { U }$ . We also suppose for the moment that the numerical solution and all its internal stages remain in this neighbourhood. The propagation of local errors will be studied in part (a),and their accumulation over the whole interval in part (b).

a) We consider two pairs of initial values, $( y _ { 0 } , z _ { 0 } )$ and $( \widehat { y } _ { 0 } , \widehat { z } _ { 0 } )$ , and apply the method to each (these values may be inconsistent, but they are assumed to lie in $\boldsymbol { \mathcal { U } } )$ . We shall prove that

$$
\begin{array} { r l } & { \| y _ { 1 } - \widehat { y } _ { 1 } \| \leq ( 1 + h L ) \| y _ { 0 } - \widehat { y } _ { 0 } \| + h M \| z _ { 0 } - \widehat { z } _ { 0 } \| } \\ & { \| z _ { 1 } - \widehat { z } _ { 1 } \| \leq N \| y _ { 0 } - \widehat { y } _ { 0 } \| + \kappa \| z _ { 0 } - \widehat { z } _ { 0 } \| } \end{array}
$$

where $\kappa < 1$ . For this we fix a sufficiently small step size $h$ , and consider $y _ { 1 } , z _ { 1 }$

$k _ { \imath } , \ell _ { \imath }$ as functions of $( y _ { 0 } , z _ { 0 } )$ . We shall show that

$$
\begin{array} { r l r l } & { \displaystyle \frac { \partial y _ { 1 } } { \partial y _ { 0 } } = I + \mathcal { O } ( h ) , } & & { \displaystyle \frac { \partial y _ { 1 } } { \partial z _ { 0 } } = \mathcal { O } ( h ) , } \\ & { \displaystyle \frac { \partial z _ { 1 } } { \partial y _ { 0 } } = \mathcal { O } ( 1 ) , } & & { \displaystyle \frac { \partial z _ { 1 } } { \partial z _ { 0 } } = R ( \infty ) I + \mathcal { O } ( h + \delta ) . } \end{array}
$$

The mean value theorem then implies (4.29).

We first estimate $k _ { \imath }$ and $\ell _ { \ i }$ , defined in (4.3b). Using (4.28) we compute $\ell _ { \ i }$ from the second line and insert it into the first one. This yields successively $k _ { \imath } =$ ${ \mathcal { O } } ( h )$ and $\ell _ { \ i } = \mathcal { O } ( h + \delta )$ for all internal stages. We then differentiate (4.3b) once with respect to $y _ { 0 }$ and once with respect to $z _ { 0 }$ . An analysis similar to that for $k _ { \imath }$ and $\ell _ { \ i }$ yields

$$
\begin{array} { r l r l } & { \displaystyle \frac { \partial k _ { \iota } } { \partial y _ { 0 } } = \mathcal { O } ( h ) , } & & { \displaystyle \frac { \partial k _ { i } } { \partial z _ { 0 } } = \mathcal { O } ( h ) } \\ & { \displaystyle \frac { \partial \ell _ { \iota } } { \partial y _ { 0 } } = \mathcal { O } ( 1 ) , } & & { \displaystyle \frac { \partial \ell _ { i } } { \partial z _ { 0 } } = - \sum _ { \jmath } \omega _ { \iota \jmath } I + \mathcal { O } ( h + \delta ) } \end{array}
$$

and the estimates (4.30) follow from (4.3a) and (4.25).

b) As a consequence of Lemma 3.9 (see Exercise 8), the propagation of the local errors $\delta y _ { h } ( x _ { \jmath - 1 } ) , \delta z _ { h } ( x _ { \jmath - 1 } )$ to the solution at $x _ { n }$ can be bounded by

$$
C \big ( \| \delta y _ { h } ( x _ { j - 1 } ) \| + ( h + \kappa ^ { n - \jmath } ) \| \delta z _ { h } ( x _ { \jmath - 1 } ) \| \big ) .
$$

Summing up these terms from $j = 1$ to $j = n$ and using (4.27) gives the stated bounds forthe global error, because $\textstyle \sum _ { j = 1 } ^ { n } \left( h + \kappa ^ { n - \jmath } \right) \leq C o n s t .$

Our assumption that the numerical solution and the internal stages lie in $\mathcal { U }$ can now easily be justified by induction on the step number. The numerical solution remains $\mathcal { O } ( h ^ { p } )$ -close to the exact solution and thus remains in $\mathcal { U }$ for sufficiently small $h$ ．This implies $g ( y _ { \jmath } , z _ { \jmath } ) = \mathcal { O } ( h ^ { p } )$ for all $j$ and hence also $\ell _ { \ i } = \mathcal { O } ( h )$ Consequently $( v _ { \imath } , w _ { \imath } )$ are also as close to the exact solution as we want. □

# Stiffly Accurate Rosenbrock Methods

We have already had several occasions to admire the beneficial effect of stiffly accurate Runge-Kutta methods (methods with $a _ { s i } = b _ { \imath }$ for all $i$ ; see Theorem 1.1 and Corollary 3.1O). What is the corresponding condition for Rosenbrock methods?

Definition 4.11. A Rosenbrock method is called stiffly accurate, if

$$
\alpha _ { s \ i } + \gamma _ { s \ i } = b _ { \ i } \quad ( i = 1 , \ldots , s ) \quad \mathrm { { a n d } } \quad \alpha _ { s } = 1 .
$$

Recall that $\textstyle \alpha _ { \iota } = \sum _ { \boldsymbol { \jmath } } \alpha _ { \iota \boldsymbol { \jmath } }$ . It has already been remarked at the end of Sect.IV.15 that methods satisfying (4.33) yield asymptotically exact results for the problem $y ^ { \prime } = \lambda ( y - \varphi ( x ) ) + \varphi ^ { \prime } ( x )$ . A further interesting interpretation of this condition has been given by C. Schneider (1991). He argues that DAE's are combinations of differential equations and algebraic equations; hence methods should be equally valuable for both extreme cases, either a purely differential equation, or a purely algebraic equation

$$
x ^ { \prime } = 1 , \qquad 0 = g ( x , z ) , \qquad g _ { z } { \mathrm { ~ i n v e r t i b l e ~ . } }
$$

Proposition 4.12. A stiffly accurate Rosenbrock method, applied to (4.34), yields

$$
z _ { 1 } = w _ { s } - g _ { z } ^ { - 1 } ( x _ { 0 } , z _ { 0 } ) \cdot g ( x _ { 0 } + h , w _ { s } ) .
$$

The numerical solution $z _ { 1 }$ is thus the result of one simplified Newton iteration for $0 = g ( x _ { 0 } + h , z )$ (with starting value $w _ { s }$ ）

Proof. Condition (4.33)together with $\sum _ { i } b _ { i } = 1$ implies that $\begin{array} { r } { \gamma _ { s } = \sum _ { j } \gamma _ { s j } = 0 } \end{array}$ Therefore, the second line of (4.5） gives (observe that $k _ { \ i } = h$ for the problem (4.34))

$$
0 = g ( x _ { 0 } + h . w _ { s } ) + g _ { z } ( x _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \imath } { \gamma } _ { \imath \jmath } \ell _ { \jmath } .
$$

Inserting the expression thus obtained for $\sum _ { \jmath } \gamma _ { \imath \jmath } \ell _ { \jmath }$ into

$$
z _ { 1 } = z _ { 0 } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \ell _ { \jmath } = w _ { s } + \sum _ { \jmath = 1 } ^ { s } \gamma _ { \mathfrak { s } \jmath } \ell _ { \jmath }
$$

proves the statement.

The values $( v _ { s } , w _ { s } )$ of the last stage are often used as an embedded solution for step size control. If this is the case for a stiffly accurate method, then many of the algebraic order condition are automatically satisfied. This is a consequence of the following result.

Proposition 4.13. Consider a stifly accurate Rosenbrock method. For suffciently regular problems (4.1) we have

$$
z _ { 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { q + 1 } )
$$

if and only if

$$
v _ { s } - y \big ( x _ { 0 } + h \big ) = \mathcal { O } \big ( h ^ { q } \big ) \qquad \quad a n d \qquad w _ { s } - z \big ( x _ { 0 } + h \big ) = \mathcal { O } ( h ^ { q } ) .
$$

Proof.Weusethe characterizationof Theorem 4.8and thefact that (with $\omega _ { i j }$ defined in (4.17))

$$
\sum _ { \ i } b _ { \ i } \omega _ { \ i \jmath } = \left\{ \begin{array} { l l } { 1 } & { \mathrm { ~ i f ~ } \ \jmath = s } \\ { 0 } & { \mathrm { ~ e l s e ~ . ~ } } \end{array} \right.
$$

Suppose first that (4.35) holds.For a tree $\boldsymbol { u } = \left[ \tau _ { y } , t _ { 2 } \right] _ { z }$ with arbitrary $t _ { 2 } \in D A T _ { y }$ we have, by definition of $\Phi _ { j } ( u )$ and $\gamma ( u )$ ，

$$
\sum _ { i } b _ { \imath } \Phi _ { \imath } ( u ) = \sum _ { \imath , j , k } b _ { \imath } \omega _ { i j } \alpha _ { j } \alpha _ { j k } \Phi _ { k } ( t _ { 2 } ) = \sum _ { k } \alpha _ { s k } \Phi _ { k } ( t _ { 2 } )
$$

and $\gamma ( u ) = \gamma ( t _ { 2 } )$ . Consequently, the order condition is satisfied for $u$ iff it is satisfied for $t _ { 2 }$ . Since $\varrho \big ( t _ { 2 } \big ) = \varrho \big ( u \big ) - 1$ , we see that $v _ { s } - y ( x _ { 0 } + h ) = \mathcal { O } \left( h ^ { q } \right)$ is a consequence of (4.35). By considering $\boldsymbol { u } = [ \tau _ { y } , u _ { 1 } ] _ { z }$ with $u _ { 1 } \in D A T _ { z }$ we deduce the second relation of (4.36). The “if" part is proved in a similar way. □

Finally we remark that because of (4.25) and (4.37) the stability function of a stiffly accurate Rosenbrock method always satisfies $R ( \infty ) = 0$ . This is a desirable property when solving stiff or differential algebraic equations.

# Construction of RODAS, a Stiffly Accurate Embedded Method

We want to construct an embedded Rosenbrock method (where $\widehat { y } _ { 1 } = v _ { s } , \widehat { z } _ { 1 } = w _ { s } )$ ， such that both methods are stiffly accurate. This gives the following conditions

$$
\begin{array} { l l } { { b _ { \imath } = \beta _ { s \imath } ~ ( i = 1 , \ldots , s ) , ~ \qquad \alpha _ { s } = 1 } } \\ { { \widehat { b } _ { i } = \alpha _ { s i } = \beta _ { s - 1 , i } ~ ( i = 1 , \ldots , s - 1 ) , ~ \qquad \alpha _ { s - 1 } = 1 } } \end{array}
$$

(as usual $\beta _ { i j } = \alpha _ { \iota j } + \gamma _ { i j } )$ . It follows from Proposition 4.12 that the last two stages represent simplified Newton iterations. Further,both methods have a stability function which vanishes at infinity. The construction of such a method of order 4(3) seems to be impossible with $s = 5$ . We therefore put $s = 6$

Here is the list of order conditions which have to be solved. We use the abbreviations $\alpha _ { \imath } , \beta _ { \imath } ^ { \prime }$ defined in (IV.7.16),and the coefficients $\omega _ { \imath \jmath }$ from (4.17).We shall require that

$$
y _ { 1 } - y ( x _ { 0 } + h ) = { \mathcal { O } } ( h ^ { 5 } ) , \qquad { \widehat { y } } _ { 1 } - y ( x _ { 0 } + h ) = { \mathcal { O } } ( h ^ { 4 } ) .
$$

Since we have sufficiently many parameters we also require

$$
v _ { s - 1 } - y ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { 3 } ) , \qquad w _ { s - 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { 3 } ) .
$$

By Proposition 4.13 this implies

$$
\widehat { z } _ { 1 } - z \big ( x _ { 0 } + h \big ) = { \mathcal O } \big ( h ^ { 4 } \big ) , \qquad z _ { 1 } - z \big ( x _ { 0 } + h \big ) = { \mathcal O } \big ( h ^ { 5 } \big ) ,
$$

which is more than sufficient to ensure convergence of order 4 (see Theorem 4 The conditions for (4.40) and (4.41) are (see Table IV.7.1 and Table 4.1)

$$
\begin{array} { r l } & { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } + ( b _ { 5 } + b _ { 6 } ) = 1 } \\ & { b _ { 2 } \beta _ { 2 } ^ { \prime } + b _ { 3 } \beta _ { 3 } ^ { \prime } + b _ { 4 } \beta _ { 4 } ^ { \prime } + ( b _ { 5 } + b _ { 6 } ) ( 1 - \gamma ) = \frac { 1 } { 2 } - \gamma } \\ & { b _ { 2 } \alpha _ { 2 } ^ { 2 } + b _ { 3 } \alpha _ { 3 } ^ { 2 } + b _ { 4 } \alpha _ { 4 } ^ { 2 } + ( b _ { 5 } + b _ { 6 } ) = \frac { 1 } { 3 } } \end{array}
$$

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { i } \partial _ { x } \beta _ { 1 2 } \partial _ { y } ^ { 2 } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 1 1 } ^ { 2 } \neq \frac { 1 } { 2 } \partial _ { y } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 1 1 } ^ { 2 } \neq \frac { 1 } { 2 } \partial _ { y } \beta _ { 1 2 } ^ { 1 } = \frac { 1 } { 2 } \partial _ { z } \gamma _ { 1 1 } ^ { 2 } \ \gamma ^ { 2 } \ } \\ & { \partial _ { x } \beta _ { 1 2 } ^ { 3 } \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 3 } ^ { 2 } \ \ + \frac { 1 } { 2 } \partial _ { x } \partial _ { z } \beta _ { 1 2 } ^ { 3 } \ \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \neq \frac { 1 } { 2 } \ } \\ & { \partial _ { y } \partial _ { 3 } \alpha _ { 3 } \partial _ { y } ^ { 2 } \partial _ { 1 } ^ { 2 } \ + \Delta _ { z } \partial _ { z } \gamma \sum _ { \alpha _ { 1 3 } } ^ { \alpha } \partial _ { y } ^ { 3 } \ \ + \frac { 1 } { 2 } \partial _ { x } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \ \ \ \ \mathrm { ( } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \ \ \ \mathrm { - } \ \gamma _ { 1 } ^ { 2 } \ \gamma } \\ & { \partial _ { x } \partial _ { x } \gamma _ { 2 1 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { z } \partial _ { x } \gamma ^ { 2 } \ \partial _ { 1 2 } ^ { 3 } \ \ \mathrm { ~ } } \\ & { \partial _ { y } \partial _ { 3 } \gamma _ { 3 2 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { z } \gamma \ \partial _ { 4 2 } ^ { 3 } \ \ \mathrm { ~ } } \\ & { \partial _ { z } \partial _ { 3 } \gamma _ { 3 2 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 4 2 } ^ { 3 } \ \gamma \ } \\ &  \partial _ { x } \partial _ { x } \partial _ { y } \partial _ { z } \gamma \end{array} \end{array}
$$

In order to solve the system (4.39), (4.43a-n) we can take $\gamma , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } , \beta _ { 2 } ^ { \prime } =$ $\beta _ { 2 1 } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ as free parameters. The remaining coeficients can then be computed as follows:

Step $l$ . We have $b _ { 6 } = \gamma$ by (4.39). The remaining $b _ { i }$ can be chosen such that (4.43a,b,c,e) are satisfied. We have one degree of freedom which can be exploited to fulfill the additional order condition $\textstyle \sum _ { i } b _ { i } \alpha _ { i } ^ { 4 } = 1 / 5$ . This step also yields $\beta _ { 6 i } \simeq$ $b _ { i }$ for $i = 1 , \ldots , 6$

Step 2. Compute the two expressions $b _ { 3 } \beta _ { 3 2 } + b _ { 4 } \beta _ { 4 2 }$ and $b _ { 4 } \beta _ { 4 3 }$ from (4.43d,g), and then $\beta _ { 3 2 }$ from(4.43b). Because f $\begin{array} { r } { \beta _ { i } ^ { \prime } = \sum _ { j = 1 } ^ { i - 1 } \beta _ { i j } } \end{array}$ tis etemines all $\beta _ { i j }$ with $i \leq 4$ . Observe that $\beta _ { i i } = \gamma$ for all

Step 3. Solve the linear system $( 4 . 4 3 \mathrm { j } , \mathrm { k } , \mathrm { l } )$ for $\alpha _ { 6 2 } , \alpha _ { 6 3 } , \alpha _ { 6 4 }$ . We have $\alpha _ { 6 5 } = \gamma$ by (4.39) and compute $\alpha _ { 6 1 }$ from $\begin{array} { r } { \alpha _ { 6 } = \sum _ { i } \alpha _ { 6 i } = 1 } \end{array}$ .This also yields $\beta _ { 5 i } \simeq \alpha _ { 6 i }$ by (4.39). Hence all $\beta _ { \imath j }$ and $\omega _ { i j }$ ,and also $\widehat { \boldsymbol { b } } _ { \iota } = \beta _ { 5 \iota }$ $( i = 1 , \ldots , 5 )$ are determined at this stage.

Step 4. The conditions $( 4 . 4 3 \mathrm { m } , \mathrm { n } )$ and $\alpha _ { 5 } = 1$ constitute 3 linear equations in the four unknown parameters $\alpha _ { 5 1 } , \alpha _ { 5 2 } , \alpha _ { 5 3 } , \alpha _ { 5 4 }$ . We have one degree of freedom in this step.

Step 5.The remaining two conditions (4.43f,i) are linear equations in $\alpha _ { 3 2 } ,$ $\alpha _ { 4 2 } , \alpha _ { 4 3 }$ . We have one more degree of freedom which can be exploited to fulfill the order condition for the tree $\left\{ \tau _ { y } , \tau _ { y } , \left[ \tau _ { y } \right] _ { y } \right\} _ { y }$ . The values of $\alpha _ { \imath 1 }$ are then determined by $\begin{array} { r } { \alpha _ { \iota } = \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { i \jmath } } \end{array}$ , and those of $\gamma _ { \imath j }$ are given by $\gamma _ { \imath j } = \beta _ { \imath j } - \alpha _ { \imath j }$

The coeficients for the code RODAS of the appendix were computed with the above procedure. In step 4 we have added the condition

$$
\sum _ { \imath , j } \alpha _ { 5 i } \omega _ { i j } = 1
$$

which will be explained in Exercise 3 below. The free parameters were chosen in

order to get an $A$ -stable method with small error constants. The result is

$$
\begin{array} { l l l } { { \gamma = 0 . 2 5 } } & { { } } & { { } } \\ { { \alpha _ { 2 } = 0 . 3 8 6 } } & { { } } & { { \alpha _ { 3 } = 0 . 2 1 } } & { { \alpha _ { 4 } = 0 . 6 3 } } \\ { { \beta _ { 2 } ^ { \prime } = 0 . 0 3 1 7 } } & { { } } & { { \beta _ { 3 } ^ { \prime } = 0 . 0 6 3 5 } } & { { \beta _ { 4 } ^ { \prime } = 0 . 3 4 3 8 } } \end{array}
$$

We do not claim that these values are optimal. Nevertheless, the numerical results of Sect.IV.10 (Fig.IV.10.8,IV.10.9 and IV.10.12) are encouraging. Although the new method needs 6 function evaluations per step, it is in general superior to the classical methods of Table IV.7.2 which need only 3 evaluations per step.

A different set of coeficients,based on the same construction, has been proposed by Steinebach (1995). The free parameters are chosen in order to satisfy the Scholz conditions $C _ { 2 } ( z ) \equiv 0$ and $C _ { 3 } ( z ) \equiv 0$ (see Eq.(15.41) of Sect.IV.15).

Dense Output. A natural way to define a continuous numerical solution for $y ( x _ { 0 } +$ $\theta h )$ ， $z { \big ( } x _ { 0 } + \theta h { \big ) }$ is

$$
y _ { 1 } ( \theta ) = y _ { 0 } + \sum _ { i = 1 } ^ { s } b _ { i } ( \theta ) k _ { i } , \qquad z _ { 1 } ( \theta ) = z _ { 0 } + \sum _ { \ i = 1 } ^ { s } b _ { i } ( \theta ) \ell _ { i } ,
$$

where the $b _ { \imath } ( \theta )$ are polynomials which satisfy $b _ { i } ( 0 ) = 0$ ， $b _ { \ i } ( 1 ) = b _ { \ i }$ . In complete analogy to Theorem 4.8 we have

$$
\begin{array} { l l } { { y ( x _ { 0 } + \theta h ) - y _ { 1 } ( \theta ) = \displaystyle { \mathcal O } ( h ^ { p + 1 } ) } } & { { \mathrm { i f f } \quad \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( \theta ) \Phi _ { \imath } ( t ) = \displaystyle { \frac { \theta ^ { e ( t ) } } { \gamma ( t ) } } } } \\ { { } } & { { \mathrm { f o r } t \in D A T _ { y } , \varrho ( t ) \leq p , } } \\ { { \displaystyle z ( x _ { 0 } + \theta h ) - z _ { 1 } ( \theta ) = \displaystyle { \mathcal O } ( h ^ { q + 1 } ) } } & { { \mathrm { i f f } \quad \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( \theta ) \Phi _ { \imath } ( u ) = \displaystyle { \frac { \theta ^ { e ( u ) } } { \gamma ( u ) } } } } \end{array}
$$

In our situation ( $( s = 6$ ) it is easy to fulfill these conditions with $p = 3$ and $q = 2$ · The additional condition $b _ { s } ( \theta ) = \gamma \theta$ makes the solution unique.

Methods of Order 5. C. Schneider (1991b) first constructed stiffly accurate Rosenbrock methods of order 5 with $s \simeq 8$ stages. Di Marzo （1992) then determined carefully the free parameters to obtain $A$ -stability and small error constants. The resulting method, implemented in the code RODAS5, gives excellent results (see Sect. IV.10).

# Inconsistent Initial Values

Even if we start the computation with consistent initial values, the numerical solution $( y _ { n } , z _ { n } )$ of a Rosenbrock method does not, in general, satisfy $g ( y _ { n } , z _ { n } ) = 0$ It is therefore of interest to investigate the local error also for inconsistent initial

values $\left( { y _ { 0 } , z _ { 0 } } \right)$ . But what is the local error? To which solution of (4.1) should we compare the numerical values? If

$$
\| ( g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) \| \leq \delta
$$

with sufficiently small $\delta$ , we can find (because of (1.7)) a locally unique $\widehat { z } _ { 0 }$ which satisfies $g ( y _ { 0 } , \widehat { z } _ { 0 } ) = 0$ . It is natural to compare the numerical solution $( y _ { 1 } , z _ { 1 } )$ t0 that solution of (4.1) which passes through $( y _ { 0 } , \widehat { z } _ { 0 } )$

Our first aim is to write this solution in terms of elementary differentials evaluated at $( y _ { 0 } , z _ { 0 } )$ . Using

$$
\begin{array} { r } { \widehat { z } _ { 0 } - z _ { 0 } = ( - g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( \delta ^ { 2 } ) , } \end{array}
$$

which is a consequence of $0 = g ( y _ { 0 } , z _ { 0 } ) + g _ { z } ( y _ { 0 } , z _ { 0 } ) ( \widehat { z } _ { 0 } - z _ { 0 } ) + . . . , \mathrm { w e ~ g e t }$

$$
\begin{array} { r l } & { y ( x _ { 0 } + h ) = y _ { 0 } + h f ( y _ { 0 } , \hat { z } _ { 0 } ) + \mathcal { O } ( h ^ { 2 } ) } \\ & { \qquad = y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) + h ( f _ { z } ( - g _ { z } ^ { - 1 } ) g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( h ^ { 2 } + h \delta ^ { 2 } ) } \\ & { z ( x _ { 0 } + h ) = \hat { z } _ { 0 } + h ( - g _ { z } ^ { - 1 } g _ { y } f ) ( y _ { 0 } , \hat { z } _ { 0 } ) + \mathcal { O } ( h ^ { 2 } ) } \\ & { \qquad = z _ { 0 } + ( - g _ { z } ^ { - 1 } g ) \big ( y _ { 0 } , z _ { 0 } ) + h ( - g _ { z } ^ { - 1 } g _ { y } f ) ( y _ { 0 } , z _ { 0 } ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { z z } \big ( - g _ { z } ^ { - 1 } g , - g _ { z } ^ { - 1 } g _ { y } f \big ) \big ) ( y _ { 0 } , z _ { 0 } ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { y z } \big ( f , - g _ { z } ^ { - 1 } g \big ) \big ) \big ( y _ { 0 } , z _ { 0 } \big ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { y } f _ { z } \big ( - g _ { z } ^ { - 1 } \big ) g \big ) \big ( y _ { 0 } , z _ { 0 } \big ) + \mathcal { O } ( h ^ { 2 } + \hat { \delta } ^ { 2 } ) } \end{array}
$$

The expressions so obtained allow a nice interpretation using trees. We only have to add in the recursive Definition 4.1 a tree of order O, which consists of a fat root. We denote this tree by $\varnothing _ { z }$ ，and extend Definition 4.3 by seting $F ( \varnothing _ { z } ) ( y , z ) =$ $( - g _ { z } ^ { - 1 } g ) ( y , z )$ . Then, the exprcssions of (4.49) and (4.50) correspond to the trees of Fig. 4.4.

![](images/68886b7ca0226b8f0357b7465c20aa372be2fede485e6940f61bffb82526eb12.jpg)  
Fig. 4.4. Trees,to be considered for inconsistent initial values

The numerical solution also possesses an expansion of the form (4.49), (4.50) with additional method-dependent coefficients. The first few terms are as follows:

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + \displaystyle \left( \sum _ { \iota } b _ { \iota } \right) h f ( y _ { 0 } , z _ { 0 } ) + \displaystyle \left( \sum _ { \iota , y , k } b _ { \iota } \beta _ { \iota j } \omega _ { \jmath k } \right) h ( f _ { z } ( - g _ { \iota } ^ { - 1 } ) g ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \qquad \quad + \mathcal { O } ( h ^ { 2 } + h \delta ^ { 2 } ) } } \\ { { z _ { 1 } = z _ { 0 } + \displaystyle \left( \sum _ { \iota , y } b _ { \iota } \omega _ { \iota j } \right) ( - g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( h + \delta ^ { 2 } ) . } } \end{array}
$$

In order to understand the form of these new coefficients we have to cxtend the proof of Theorem 4.6. It turns out that the elementary differentials are multiplicd by $\begin{array} { r } { \gamma ( t ) \sum _ { \iota } b _ { \iota } \Phi _ { \iota } ( t ) } \end{array}$ or $\gamma ( \mathfrak { u } ) \sum , b _ { \iota } \Phi _ { \iota } ( \mathfrak { u } )$ ,where $\gamma$ and $\Phi _ { \iota }$ are defined by $\gamma ( \emptyset _ { z } ) =$

1, $\begin{array} { r } { \Phi _ { i } ( \emptyset _ { z } ) = \sum _ { j } \omega _ { \iota j } } \end{array}$ and the recursion of Theorem 4.6. Equating the coeficients of the exact and numerical solutions yields new order conditions for the case of inconsistent initial values. The first of these (to be added to those of Table IV.7.1 and Table 4.1) are presented in Table 4.2.

Table 4.2. Order conditions for inconsistent initial values   

<table><tr><td>tree</td><td>order condition</td><td>size of error term</td></tr><tr><td>Y</td><td>∑baazywk=1/2</td><td>O(h²8）</td></tr><tr><td>。</td><td>∑bw=1</td><td>0(8）</td></tr><tr><td>10</td><td>∑bwaαjkwkl=1</td><td>O(hs)</td></tr></table>

Remarks. a) The first condition of Table 4.2 is exactly the same as that found by van Veldhuizen (1984) in a different context. It implies that the local error of the $y$ -component is of size $\mathcal { O } ( h ^ { p + 1 } + h ^ { 3 } \delta + h \delta ^ { 2 } )$

b) Condition $\sum _ { \iota _ { 1 } } b _ { \iota _ { 2 } } \omega _ { \iota _ { 2 } } = 1$ means that the stability function satisfies $R ( \infty ) =$ O.Unless this condition is satisfied, the local error of the $z$ -component contains an $h$ -independent term of size $\delta$ (which usually is near to $T o l$ ). This was observed numerically in Fig.IV.7.4 and explains the phenomenon of Fig.IV.7.3.

c) For Rosenbrock methods which satisfy (4.39), the second and third conditions of Table 4.2 are automatically fulfilled. For such methods the local error of the $z$ -component is of size $\mathcal { O } ( h ^ { q + \mathrm { i } } + h ^ { 2 } \delta + \delta ^ { 2 } )$

# Exercises

1. (Roche 1989). Consider the implicit Runge-Kutta method (1.11) applied to (1.6).

a) Prove that $z _ { 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { q + 1 } )$ iff

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } \Phi _ { \ i } ( u ) = \frac 1 { \gamma ( u ) } \qquad \mathrm { ~ f o r ~ } \quad u \in D A T _ { \ o z } , \ \varrho ( u ) \le q ,
$$

where $\gamma ( u )$ and $\Phi _ { \imath } ( u )$ arede $\alpha _ { \imath \jmath }$ and $\beta _ { \imath \jmath }$ are replaced bytheRunge-Kutcoefficients $a _ { \imath \jmath }$

b) Show that those trees in $D A T _ { z }$ which have more than one fat vertex,are redundant.

2. The simplifying assumptions (4.39) imply that many of the (algebraic) order conditions are automatically satisfied. Characterize the corresponding trees.

3.State the order condition for the tree $\left[ \tau _ { y } , \left[ \tau _ { y } , \emptyset _ { z } \right] _ { z } \right] _ { z }$

a) Show that the corresponding error term is of size $\mathcal { O } ( h ^ { 2 } \delta )$ with $\delta$ given in (4.48). b)For methods satisfying (4.39),this condition is equivalent to (4.44).

4.(Ostermann 1990). Suppose that the Rosenbrock method (4.3) satisfies (4.27). Define polynomials $b _ { \imath } ( \theta )$ of degree $q = [ ( p + 1 ) / 2 ]$ by $b _ { \imath } ( 0 ) = 0$ ， $b _ { \ i } ( 1 ) = b _ { \ i }$ ， and

$$
\int _ { 0 } ^ { 1 } b _ { \iota } ( \theta ) \theta ^ { \ell - 1 } \ d \theta = \left\{ \begin{array} { l l } { \sum _ { \ j } b _ { \ j } \big ( \alpha _ { \ j \iota } + \gamma _ { \ j \iota } \big ) } & { \quad \mathrm { i f ~ } \ \ell = 1 } \\ { \sum _ { \ j } b _ { \ j } \alpha _ { \ j } ^ { \ell - 1 } \alpha _ { \ j \iota } } & { \quad \mathrm { i f ~ } \ \ell = 2 , \dots , q - 1 . } \end{array} \right.
$$

Prove that the error of the dense output formulas (4.46) is $\mathcal { O } ( h ^ { q + 1 } )$

Hint. Extend the ideas of Exercise II.17.5 to Rosenbrock methods.

5. Suppose that a Rosenbrock method is implemented in the form (IV.7.25). If it satisfies (4.39), then its last two stages allow a very simple implementation

Hint. Prove that

$$
m _ { \ i } = \left\{ \begin{array} { l l } { { a _ { s \ i } ~ } } & { { \ i = 1 , \ldots , s - 1 } } \\ { { 1 ~ } } & { { \ i = s ~ , } } \end{array} \right. \qquad a _ { s \ i } = \left\{ \begin{array} { l l } { { a _ { s - 1 , s } ~ } } & { { \ i = 1 , \ldots , s - 2 } } \\ { { 1 ~ } } & { { \ i = s - 1 ~ . } } \end{array} \right.
$$

6.Partitioned Rosenbrock methods (Rentrop,Roche & Steinebach 1989). Consider the method (4.3） with $f _ { y }$ and $f _ { z }$ replaced by 0. Derive necessary and sufficient conditions that it be of order $p$

Remark. Case (a) of Lemma 4.9 remains valid in this new situation. However, the trees of Lemma 4.9b give rise to new conditions.

7. What is the“algebraic order”of the classical 4th order Rosenbrock methods of Section IV.7?

8. Let $\left\{ u _ { n } \right\} , \left\{ v _ { n } \right\}$ be two sequences of non-negative numbers satisfying (componentwise)

$$
\binom { u _ { n + 1 } } { v _ { n + 1 } } \leq \binom { 1 + h L } { N } \quad k M \bigg ) \binom { u _ { n } } { v _ { n } }
$$

with $0 \leq \kappa < 1$ and positive constants $L , M , N$ . Prove that for $h \leq h _ { 0 }$ and $n h \le C o n s t$

$$
u _ { n } \leq C ( u _ { 0 } + h v _ { 0 } ) , \qquad \quad v _ { n } \leq C ( u _ { 0 } + ( h + \kappa ^ { n } ) v _ { 0 } ) .
$$

Hint. Apply Lemma 3.9 with $\varepsilon = h$ and $M = 0$ .

The numerical computations of Sect.IV.1O have revealed the extrapolation code SEULEX as one of the best method for very stringent tolerances. The aim of the present section is to justify theoretically the underlying numerical method, the extrapolated linearly implicit Euler method, for singular perturbation problems as a representative of stiff equations.

# Linearly Implicit Euler Discretization

The linearly implicit Euler method (IV.9.25) applied to the singular perturbation problem (1.5) reads

$$
\left( \begin{array} { r r } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { \varepsilon I - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { l } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { l } { f ( y _ { \iota } , z _ { \iota } ) } \\ { g ( y _ { \iota } , z _ { \iota } ) } \end{array} \right) .
$$

Here we have used abbreviations such as $f _ { y } ( 0 ) = f _ { y } ( y _ { 0 } , z _ { 0 } )$ for the partial derivatives. We recall that the numerical approximations at $x _ { 0 } + H$ $\left( H = n h \right)$ are extrapolated according to (IV.9.26).

For the differential algebraic problem (1.6) we just put $\varepsilon = 0$ in (5.1). This yields

$$
\left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { c } { f ( y _ { \iota } , z _ { \iota } ) } \\ { g ( y _ { \iota } , z _ { \iota } ) } \end{array} \right) .
$$

Possible extensions to non-autonomous problems have been presented in Sect.IV.9. For problems $M u ^ { \prime } = \varphi ( u )$ we use the formulation (IV.9.34) also for singular $M$ Due to the invariance of the method with respect to the transformation (1.23),all results of this section are equally valid for $M u ^ { \prime } = \varphi ( u )$ of index 1.

The performance of extrapolation methods relies heavily on the existence of an asymptotic expansion of the global error. Such expansions are well understood, if the differential equation is nonstiff (see Sections II.8 and IV.9). But what happens if the problem is stiff or differential-algebraic?

Continued study of special problems is still a commendable way towards greater insight ... (E.Hopf 1950)

Example 5.1. Consider the test problem

$$
y ^ { \prime } = 1 , \qquad \varepsilon z ^ { \prime } = - z + g ( y ) .
$$

Method (5.1) yields the exact result $y _ { \imath } = x _ { \imath } = x _ { 0 } + i h$ for the $y$ -component, and the recursion

$$
( \varepsilon + h ) z _ { \iota + 1 } = \varepsilon z _ { \iota } + h g ( x _ { \iota } ) + h ^ { 2 } g ^ { \prime } ( x _ { 0 } )
$$

for the $z$ -component. In order to compute the coeficients of the asymptotic expansion (Theorem II.8.1), we insert

$$
z _ { \iota } = z ( x _ { \iota } ) + h b _ { 1 } ( x _ { \iota } ) + h ^ { 2 } b _ { 2 } ( x _ { \iota } ) + h ^ { 3 } b _ { 3 } ( x _ { \iota } ) + \ldots
$$

into (5.4),expand into a Taylor series and compare the coefficients of $h ^ { \jmath }$ .This yields the differential equation

$$
\varepsilon b _ { \bf 1 } ^ { \prime } ( x ) + b _ { \bf 1 } ( x ) = - \frac { \varepsilon } { 2 } z ^ { \prime \prime } ( x ) - z ^ { \prime } ( x ) + g ^ { \prime } ( x _ { 0 } )
$$

for $b _ { 1 } ( x )$ ， and similar ones for $b _ { 2 } ( x ) , b _ { 3 } ( x )$ , etc. Putting $\iota \ : = 0$ in (5.5） we get the initial values $b _ { \imath } ( x _ { 0 } ) = 0$ (all $\wr$ ). In general, the computation of the functions $b _ { 1 } ( x ) , \ b _ { 2 } ( x ) , \ldots$ is rather tedious. We therefore continue this example for the special case $x _ { 0 } = 0$ ， $g ( x ) = x ^ { 2 } + 2 \varepsilon x$ .and $z _ { 0 } = 0$ ,so that the exact solution of (5.3) is $z ( x ) = x ^ { 2 }$ . In this situation we get

$$
\begin{array} { l } { { b _ { 1 } ( x ) = - 3 \varepsilon e ^ { - r / \varepsilon } + 3 \varepsilon - 2 x } } \\ { { b _ { 2 } ( x ) = - \displaystyle \left( 1 + \frac { 3 x } { 2 \varepsilon } \right) e ^ { - x / \varepsilon } + 1 } } \\ { { b _ { 3 } ( x ) = \displaystyle \left( \frac { x } { 2 \varepsilon ^ { 2 } } - \frac { 3 x ^ { 2 } } { 8 \varepsilon ^ { 3 } } \right) e ^ { - x / \varepsilon } } } \end{array}
$$

etc. We observe that for $\varepsilon  0$ ,the function $b _ { 2 } ( x )$ becomes discontinuous at $x = 0$ ， and $b _ { 3 } \mathopen { } \mathclose \bgroup \left( x ^ { \ast } \aftergroup \egroup \right)$ is even not uniformly bounded. Hence, the expansion (5.5) is not useful for the study of extrapolation, if $\varepsilon$ is small compared to the step size $H$

The idea is now to omit in (5.6) the terms containing the factor $e ^ { - x / \varepsilon }$ by requiring that the functions $\boldsymbol { b } _ { \imath } ( \boldsymbol { x } )$ be smooth uniformly in $\boldsymbol { \mathcal { E } }$ and, instead, to add a discrete perturbation $\beta _ { \imath }$ to (5.5). For our example, this then becomes

$$
z _ { i } = x _ { \imath } ^ { 2 } + h ( 3 \varepsilon - 2 x _ { \imath } ) + h ^ { 2 } + \beta _ { \imath } .
$$

Inserting (5.7a) into (5.4) gives the relation $( \varepsilon + h ) { \beta _ { \iota + 1 } } = \varepsilon { \beta _ { \iota } }$ . The value of $\beta _ { 0 }$ is obtained from (5.7a) with $i \approx 0$ . We thus get

$$
\beta _ { \imath } = - \Big ( 1 + \frac { h } { \varepsilon } \Big ) ^ { - \imath } \big ( 3 \varepsilon h + h ^ { 2 } \big ) .
$$

If the numerical solution is extrapolated, the smooth terms in (5.7) are eliminated one after the other. It remains to study the effect of extrapolation on the perturbation terms $\beta _ { \ i }$ .If the differential equation is very stiff $\left( \varepsilon \ll h \right)$ ，these terms are very small and may be neglected over a wide range of $j _ { l }$ (observe that $i \geq n _ { 1 } )$ ，

Example 5.2.For the differential-algebraic problem

$$
y ^ { \prime } = 1 , \qquad 0 = - z + g ( y )
$$

with initial values $y _ { 0 } = x _ { 0 } , z _ { 0 } = g ( x _ { 0 } )$ the numerical solution, given by (5.2), is

$$
z _ { \ i } = \left\{ \begin{array} { l l } { { g ( x _ { 0 } ) } } & { { \mathrm { ~ f o r ~ } i = 0 \nonumber } } \\ { { g ( x _ { \ i - 1 } ) + h g ^ { \prime } ( x _ { 0 } ) } } & { { \mathrm { ~ f o r ~ } i \geq 1 \nonumber . } } \end{array} \right.
$$

Developing its second formula (for $i \geq 1$ yields

$$
z _ { \imath } = g ( x _ { \imath } ) + h \big ( g ^ { \prime } ( x _ { 0 } ) - g ^ { \prime } ( x _ { \imath } ) \big ) + \frac { h ^ { 2 } } { 2 } g ^ { \prime \prime } ( x _ { \imath } ) - \frac { h ^ { 3 } } { 6 } g ^ { \prime \prime \prime } ( x _ { \imath } ) + \mathcal { O } ( h ^ { 4 } ) .
$$

If we add the perturbation

$$
\beta _ { \imath } = h \beta _ { i } ^ { 1 } + h ^ { 2 } \beta _ { \imath } ^ { 2 } + h ^ { 3 } \beta _ { i } ^ { 3 } + \ldots
$$

(which is different from zero only for $i \approx 0$ ) we get for all $i$

$$
z _ { \imath } - g ( x _ { \imath } ) = \sum _ { \jmath = 1 } ^ { 3 } h ^ { j } ( b _ { j } ( x _ { i } ) + \beta _ { i } ^ { j } ) + \mathcal { O } ( h ^ { 4 } )
$$

where

$$
b _ { 1 } ( x ) = g ^ { \prime } ( x _ { 0 } ) - g ^ { \prime } ( x ) , \quad b _ { 2 } ( x ) = \frac { 1 } { 2 } g ^ { \prime \prime } ( x ) , \quad b _ { 3 } ( x ) = - \frac { 1 } { 6 } g ^ { \prime \prime \prime } ( x )
$$

are smooth functions and the perturbations are given by

$$
\beta _ { 0 } ^ { 1 } = 0 , \quad \beta _ { 0 } ^ { 2 } = - { \frac { 1 } { 2 } } g ^ { \prime \prime } ( x _ { 0 } ) , \quad \beta _ { 0 } ^ { 3 } = { \frac { 1 } { 6 } } g ^ { \prime \prime \prime } ( x _ { 0 } ) .
$$

If we add a further algebraic equation to (5.8), e.g., $0 = u - k ( z )$ ， and again apply Method (5.2)，we get three different formulas for $u _ { \iota }$ ，one for $\iota \approx 0$ ，one for $i = 1$ ，and a different one for $i \geq 2$ . In an expansion of the type (5.10) for $u _ { \iota } - k \big ( g \big ( x _ { \iota } \big ) \big )$ , perturbation terms will be present for $i \approx 0$ and for $i \approx 1$

# Perturbed Asymptotic Expansion

For general differential algebraic problems we have the following result.

Theorem 5.3 (Deuflhard, Hairer & Zugck 1987). Consider the problem (1.6) with consistent initial values $( y _ { 0 } , z _ { 0 } )$ , and suppose that (1.7) is satisfied. The global error of the linearly implicit Euler method (5.2) then has an asymptotic $h$ -expansion of the form

$$
\begin{array} { l } { { \displaystyle y _ { \imath } - y \big ( x _ { \imath } \big ) = \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( a _ { \jmath } \big ( x _ { i } \big ) + \alpha _ { \imath } ^ { \jmath } \big ) + \mathcal { O } \big ( h ^ { M + 1 } \big ) } } \\ { { \displaystyle z _ { \imath } - z \big ( x _ { \imath } \big ) = \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } \big ( x _ { i } \big ) + \beta _ { \imath } ^ { \jmath } \big ) + \mathcal { O } \big ( h ^ { M + 1 } \big ) } } \end{array}
$$

where $a _ { \ j } ( \ j ) , \ j _ { \ j } ( \ j )$ are smooth functions and the perturbations satisfy (see Table 5.1 and 5.2)

$$
\begin{array} { r l } { \alpha _ { \iota } ^ { 1 } = 0 , \quad \alpha _ { \iota } ^ { 2 } = 0 , } & { \alpha _ { \iota } ^ { 3 } = 0 , \quad \beta _ { \iota } ^ { 1 } = 0 \quad \quad f o r \ \iota \geq 0 } \\ { \beta _ { \iota } ^ { 2 } = 0 \quad } & { f o r \ \iota \geq 1 } \\ { \alpha _ { \iota } ^ { \jmath } = 0 \quad } & { f o r \ \iota \geq j - 4 \ a n d \ \jmath \geq 4 } \\ { \beta _ { \iota } ^ { \jmath } = 0 \quad } & { f o r \ \iota \geq j - 2 \ a n d \ j \geq 3 . } \end{array}
$$

The error terms in (5.11) are uniformly bounded for $x _ { \ i } = i h \le H$ ， $i f ~ H$ is sufficiently small.

Table 5.1.Non-zero $\alpha$ 's

Table 5.2.Non-zero $\beta$ 's

$$
\begin{array} { c c } { \small { ( \begin{array} { c c c c c c c c c c c c c c c c } { \small { b } } & { \small { h } } & { h ^ { 2 } } & { h ^ { 3 } } & { h ^ { 4 } } & { h ^ { 5 } } & { h ^ { 6 } } & { h ^ { 7 } } & { \small { ( \begin{array} { c c c c c c c c c c c c } { \boxed { h } } & { h ^ { 2 } } & { h ^ { 3 } } & { h ^ { 3 } } & { h ^ { 4 } } & { h ^ { 5 } } & { h ^ { 6 } } & { h ^ { 7 } } & { h ^ { 7 } } & { h ^ { 7 } } & { h ^ { 8 } } & { h ^ { 7 } } & { h ^ { 7 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 2 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 3 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 4 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \ast } & { \ast } & { \ast } \\ { y _ { 5 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } \end{array} ) } } \end{array} ) } } \end{array} \quad \begin{array} { c c c c c c c c c c c c }  \small  ( \begin{array} { c c c c c c c c c } { \box { h } } & { h ^ { 2 } } &  h  \end{array} \end{array}
$$

Proof. In part (a) we shall recursively construct truncated expansions

$$
\begin{array} { l } { \widehat { y } _ { \iota } = y ( x _ { \iota } ) + \displaystyle \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( a _ { \jmath } ( x _ { \iota } ) + \alpha _ { \iota } ^ { \jmath } \big ) + h ^ { M + 1 } \alpha _ { \iota } ^ { M + 1 } } \\ { \widehat { z } _ { \iota } = z ( x _ { \iota } ) + \displaystyle \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } ( x _ { \iota } ) + \beta _ { \iota } ^ { \jmath } \big ) } \end{array}
$$

such that the defect of $\widehat { \boldsymbol { y } } _ { \iota } , \widehat { \boldsymbol { z } } _ { \iota }$ inserted into the method is small; more precisely, we require that

$$
\begin{array} { r } { \left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c c } { \widehat { y } _ { \iota + 1 } - \widehat { y } _ { \iota } } \\ { \widehat { z } _ { i + 1 } - \widehat { z } _ { \iota } } \end{array} \right) = h \left( \begin{array} { c c } { f ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \\ { g ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \end{array} \right) + { \mathcal O } ( h ^ { M + 2 } ) . } \end{array}
$$

For the initial values we rquire $\widehat { y } _ { 0 } = y _ { 0 } , \widehat { z } _ { 0 } = z _ { 0 }$ , or equivalently

$$
a _ { \ i } ( 0 ) + \alpha _ { 0 } ^ { \ i } = 0 , \qquad b _ { \ i } ( 0 ) + \beta _ { 0 } ^ { \ j } = 0 ,
$$

and the perturbation terms are assumed to satisfy

$$
\alpha _ { \ i } ^ { \ j }  0 , \qquad \beta _ { \ i } ^ { \ j }  0 \qquad \mathrm { f o r } \quad \ i  \infty ,
$$

otherwise, these limits could be added to the smooth parts. The result will then follow from a stability estimate derived in part (b).

a) For the construction of $a _ { \ j } ( \boldsymbol { x } ) , b _ { \ j } ( \boldsymbol { x } ) , \alpha _ { \iota } ^ { \ j } , \beta _ { \iota } ^ { \ j }$ we insert (5.13) into (5.14), and develop

$$
\begin{array} { c } { { f ( \widehat { y } _ { \imath } , \widehat { z } _ { \imath } ) = f \bigl ( y ( x _ { \imath } ) , z ( x _ { \imath } ) \bigr ) + f _ { y } ( x _ { \imath } ) \bigl ( h a _ { 1 } ( x _ { \imath } ) + h \alpha _ { \imath } ^ { 1 } + \ldots \bigr ) } } \\ { { + f _ { z } ( x _ { \imath } ) \bigl ( h b _ { 1 } ( x _ { \imath } ) + h \beta _ { \imath } ^ { 1 } + \ldots \bigr ) } } \\ { { + f _ { y y } ( x _ { \imath } ) \bigl ( h a _ { 1 } ( x _ { \imath } ) + h \alpha _ { \imath } ^ { 1 } + \ldots \bigr ) ^ { 2 } + \ldots , } } \\ { { { \widehat { y } } _ { \imath + 1 } - \widehat { y } _ { \imath } = y ( x _ { \imath + 1 } ) - y ( x _ { \imath } ) + h \bigl ( a _ { 1 } ( x _ { \imath + 1 } ) - a _ { 1 } ( x _ { \imath } ) + \alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 } \bigr ) + \ldots } } \\ { { = h y ^ { \prime } ( x _ { \imath } ) + \displaystyle \frac { h ^ { 2 } } { 2 } y ^ { \prime \prime } ( x _ { \imath } ) + \ldots + h ^ { 2 } a _ { 1 } ^ { \prime } ( x _ { \imath } ) + h ( \alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 } ) + \ldots , } } \end{array}
$$

where $f _ { y } ( x ) = f _ { y } ( y ( x ) , z ( x ) )$ , etc. Similarly, we develop $g ( \widehat { y } _ { \imath } , \widehat { z } _ { \imath } )$ and $\widehat { z } _ { \iota + 1 } - \widehat { z } _ { \iota }$ ， and compare coefficients of $h ^ { j + 1 }$ (for $j = 0 , \ldots , M )$ . Each power of $h$ will lead to two conditions - one containing the smooth functions and the other containing the perturbation terms.

First step. Equating the coefficients of $h ^ { 1 }$ yields the equations (1.6) for the smooth part (due to consistency of the method), and $\alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { i } ^ { 1 } = 0$ for $i \geq 0$ Because of (5.16) we get $\alpha _ { \ i } ^ { \ i } = 0$ for all $i \geq 0$ (compare (5.12a)).

Second step. The coeficents of $h ^ { 2 }$ give

$$
\begin{array} { c l l } { { a _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { 1 } { 2 } y ^ { \prime \prime } ( x ) - f _ { y } ( 0 ) y ^ { \prime } ( x ) - f _ { z } ( 0 ) z ^ { \prime } ( x ) = f _ { y } ( x ) a _ { 1 } ( x ) + f _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { - g _ { y } ( 0 ) y ^ { \prime } ( x ) - g _ { z } ( 0 ) z ^ { \prime } ( x ) = g _ { y } ( x ) a _ { 1 } ( x ) + g _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { \alpha _ { \imath + 1 } ^ { 2 } - \alpha _ { \imath } ^ { 2 } - f _ { z } ( 0 ) ( \beta _ { \imath + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 } ) = f _ { z } ( 0 ) \beta _ { \imath } ^ { 1 } } } \\ { { - g _ { z } ( 0 ) ( \beta _ { \imath + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 } ) = g _ { z } ( 0 ) \beta _ { \imath } ^ { 1 } . } } \end{array}
$$

Observe that the coefficients $\alpha _ { \ i } ^ { \ell } , \beta _ { \ i } ^ { \ell }$ have to be independent of $h , s 0$ that $f _ { z } ( 0 )$ ， $g _ { z } ( 0 )$ cannot be replaced by $f _ { z } ( x _ { \imath } ) , g _ { z } ( x _ { \imath } )$ in the right-hand sides of (5.17c, d). The system (5.17) can be solved as follows. Compute $b _ { 1 } ( x )$ from (5.17b） and insert it into (5.17a). This gives a linear differential equation for $a _ { 1 } ( x )$ .Because of (5.15) and $\alpha _ { 0 } ^ { 1 } = 0$ the initial value is $a _ { 1 } ( 0 ) = 0$ . Therefore $a _ { 1 } ( x )$ and $b _ { 1 } ( x )$ are uniquely determined by (5.17a, b).Differentiating $g ( y ( x ) , z ( x ) ) = 0$ and putting $x \approx 0$ implies that the left-hand side of (5.17b) vanishes at $x \approx 0$ . Consequently, we have $b _ { 1 } ( 0 ) = 0$ and by (5.15),also $\beta _ { 0 } ^ { 1 } = 0$ . Condition (5.17d) then implies $\beta _ { \imath } ^ { 1 } = 0$ (all $i$ ), and (5.17c) together with (5.16) give $\alpha _ { \ i } ^ { 2 } = 0 \ ( \mathrm { a l l } \ i )$

Third step. As in the second step we get (for $j = 2$ ）

$$
\begin{array} { r } { a _ { \jmath } ^ { \prime } ( x ) = f _ { y } ( x ) a _ { \jmath } ( x ) + f _ { z } ( x ) b _ { \jmath } ( x ) + r ( x ) } \\ { 0 = g _ { y } ( x ) a _ { \jmath } ( x ) + g _ { z } ( x ) b _ { \jmath } ( x ) + s ( x ) , } \end{array}
$$

where $r ( x ) , s ( x )$ are known functions depending on derivatives of $y ( x ) , z ( x )$ ， and on $a _ { \ell } ( x ) , b _ { \ell } ( x )$ with $\ell \leq j - 1$ . We further get

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 3 } - \alpha _ { \iota } ^ { 3 } = f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } } \\ { 0 = g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } . } \end{array}
$$

We compute $a _ { 2 } ( x ) , b _ { 2 } ( x )$ as in step 2. However, $b _ { 2 } ( 0 ) \neq 0$ in general,and for the first time, we are forced to introduce a perturbation term $\beta _ { 0 } ^ { 2 } \neq 0$ . From (5.18c,d) we then get $\beta _ { \imath } ^ { 2 } = 0$ (for $i \geq 1 $ and $\alpha _ { \ i } ^ { 3 } = 0$ (for all $\textit { \textbf { l } }$ ）

Fourth step. Comparing the coefficients of $h ^ { 4 }$ we just get (5.18a,b) with $j = 3$ and (5.18c,d) with the upper index raised by 1. As above we conclude ${ \beta } _ { \ i } ^ { 3 } = 0$ (for $i \geq 1$ and $\alpha _ { \ i } ^ { 4 } = 0$ (for all $i$ ).

General step. The conditions for the smooth functions are (5.18a,b). For the perturbation terms we get

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { \jmath + 1 } - \alpha _ { \iota } ^ { \jmath + 1 } = f _ { \boldsymbol { z } } ( 0 ) \beta _ { \iota + 1 } ^ { \jmath } + \varrho _ { \iota } ^ { \jmath } } \\ { 0 = g _ { \boldsymbol { z } } ( 0 ) \beta _ { \iota + 1 } ^ { \jmath } + \sigma _ { \iota } ^ { \jmath } , } \end{array}
$$

where $\boldsymbol { \underline { { \varrho } } } _ { \iota } ^ { \jmath } , \boldsymbol { \sigma } _ { \iota } ^ { \jmath }$ are linear combinations of expressions which contain as factors $\alpha _ { \imath + 1 } ^ { \ell } , \ \alpha _ { \imath } ^ { \ell - 1 }$ β-1 with $\ell \leq j$ . For example, we have $\varrho _ { \imath } ^ { 4 } = f _ { z z } ( 0 ) ( \beta _ { \imath } ^ { 2 } ) ^ { 2 }$ and $\sigma _ { \imath } ^ { 4 } = g _ { z z } ( 0 ) ( \beta _ { \imath } ^ { 2 } ) ^ { 2 }$ ．The proof of (5.12) is now by induction on $j$ By the induction hypothesis we have ${ \varrho _ { \mathrm { \ell } _ { \mathrm { : } } } ^ { \mathrm { \mathcal { I } } } } = 0$ ， $\sigma _ { \ i } ^ { \ j } = 0$ for $\iota \geq j - 3$ . Formula (5.19d) hence implies $\beta _ { \iota + 1 } ^ { J } = 0$ (for $i \geq j - 3 )$ and (5.19c) together with (5.16) gives $\alpha _ { \iota } ^ { \jmath + 1 } = 0$ (for $i \geq \jmath - 3 )$ . But this is simply the statement $( 5 . 1 2 \mathrm { c } , \mathrm { d } )$

b) We still have to estimate the remainder term,i.e., differences $\Delta y _ { \imath } = y _ { \imath } - \widehat { y } _ { \imath }$ ， $\Delta z _ { \imath } = z _ { \imath } - \widehat { z } _ { \imath }$ . Subtracting (5.14) from (5.2) and eliminating $\Delta y _ { i + 1 } , \Delta z _ { i + 1 }$ yields

$$
\begin{array} { r l } & { \left( \begin{array} { l } { \Delta y _ { \iota + 1 } } \\ { \Delta z _ { \iota + 1 } } \end{array} \right) = \left( \begin{array} { l } { \Delta y _ { \iota } } \\ { \Delta z _ { \iota } } \end{array} \right) } \\ & { \qquad + \left( \begin{array} { l l } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { - g _ { z } ^ { - 1 } ( 0 ) } \end{array} \right) \left( \begin{array} { l } { h \big ( f ( y _ { \iota } , z _ { \iota } ) - f ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) \big ) } \\ { g ( y _ { \iota } , z _ { \iota } ) - g ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \end{array} \right) + \left( \begin{array} { l } { \mathcal { O } ( h ^ { M + 2 } ) } \\ { \mathcal { O } ( h ^ { M + 1 } ) } \end{array} \right) . } \end{array}
$$

The application of a Lipschitz condition for $f ( y , z )$ and $g \{ y , z \}$ then gives

$$
\begin{array} { r } { \left( \begin{array} { l } { \left\| \Delta y _ { \imath + 1 } \right\| } \\ { \left\| \Delta z _ { \imath + 1 } \right\| } \end{array} \right) \leq \left( \begin{array} { l l } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { \varrho } \end{array} \right) \left( \left\| \Delta y _ { \imath } \right\| \right) + \left( \mathcal { O } ( h ^ { M + 2 } ) \right) , } \end{array}
$$

where $| \varrho \} < 1$ if $H$ is sufficiently small. Applying Lemma 3.9 we deduce ${ \| \Delta y _ { \imath } \| + }$ $\| \Delta z _ { \imath } \| = \mathcal { O } \big ( h ^ { M + 1 } \big )$ □

# Order Tableau

We consider (5.2) as our basic method for extrapolation, i.e., we takc some step number sequence $n _ { 1 } < n _ { 2 } < \ldots .$ ，put ${ \hslash } _ { \mathit { 1 } } = H / n _ { \mathit { 1 } }$ , and define

$$
Y _ { \ j 1 } = y _ { h _ { \ j } } ( x _ { 0 } + H ) , \qquad Z _ { \ j 1 } = z _ { h _ { \ j } } ( x _ { 0 } + H ) ,
$$

the numerical solution of (1.6) after $n _ { \jmath }$ steps with step size ${ \boldsymbol { \jmath } } _ { \boldsymbol { \imath } , \boldsymbol { \imath } }$ . We then extrapolate these values according to (IV.9.26) and obtain $Y _ { \jmath k } , Z _ { \jmath k }$ . What is the order of the approximations thus obtained?

Theorem 5.4 (Deuflhard, Hairer & Zugck 1987). If we consider the harmonic sequence $\{ 1 , 2 , 3 , 4 , \ldots \}$ , then the extrapolated values $Y _ { j k } , ~ Z _ { j k }$ satisfy

$$
Y _ { \jmath k } - y ( x _ { 0 } + h ) = { \mathcal O } ( H ^ { r _ { \jmath k } + 1 } ) , \qquad Z _ { \jmath k } - z ( x _ { 0 } + H ) = { \mathcal O } ( H ^ { s _ { \jmath k } } )
$$

where the differential-algebraic orders $\boldsymbol { r } _ { \jmath k } , s _ { \jmath k }$ are given in Tables 5.3 and 5.5.

# Table 5.3.orders $r _ { j k }$

Table 5.4. orders S jk · $\begin{array} { l } { { \begin{array} { l l l l l l l l l } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 5 } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 5 } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } \end{array} } } \end{array}$ 5 5

4 7 48 4 4

Proof. We use the expansion (5.11). It follows from $\alpha _ { \ i } ^ { 1 } = \beta _ { \ i } ^ { 1 } = 0$ (for all $i \geq 0$ ） and from (5.15) that $a _ { 1 } ( x _ { 0 } ) = b _ { 1 } ( x _ { 0 } ) = 0$ . Since $a _ { \ j } ( \ j x )$ and $\boldsymbol { b } _ { \ u { \jmath } } ( \boldsymbol { x } )$ are smooth functions we obtain $a _ { 1 } ( x _ { 0 } + H ) = \mathcal { O } ( H )$ ， $b _ { 1 } ( x _ { 0 } + H ) = \mathcal { O } ( H )$ and the errors of $Y _ { j 1 } , Z _ { j 1 }$ $\mathcal { O } ( H ^ { 2 } )$   
$a _ { 2 } ( x _ { 0 } + H ) = { \mathcal { O } } ( H )$ However, since $\beta _ { 0 } ^ { 2 } \neq 0$ in general, we have $b _ { 2 } ( x _ { 0 } ) \neq 0$ by (5.15) and the term $b _ { 2 } ( x _ { 0 } + H )$ is only of size $\mathcal { O } ( 1 )$ . One extrapolation of the numerical solution eliminates the terms with $j = 1$ in (5.11). The error is thus of size $\mathcal { O } ( H ^ { 3 } )$ for $Y _ { _ { \jmath 2 } }$ but only $\mathcal { O } ( H ^ { 2 } )$ for $Z _ { j 2 }$ , verifying the second columns of Tables 5.3 and 5.4. If we continue the extrapolation process, the smooth parts of the error expansion (5.11) are eliminated one after the other. The perturbation terms, however, are not eliminated.

For the $y$ -component the first non-vanishing perturbation for $i \geq n _ { 1 } = 1$ is $\alpha _ { 1 } ^ { 6 }$ Therefore, the diagonal elements of the extrapolation tableau for the $y$ -component (Table 5.3) contain an error term of size $\mathcal { O } ( H ^ { 6 } )$ (observe that $\alpha _ { 1 } ^ { 6 }$ is multiplied by $h ^ { 6 }$ in (5.11). The elements $Y _ { j , \ j - 1 }$ of tefirstsubdiagonaldependonlyon $Y _ { \ell 1 } = y _ { n _ { \ell } }$ for $\ell \geq 2$ . Since $n _ { 2 } \geq 2$ , only the perturbations $\alpha _ { i } ^ { j }$ with $i \geq 2$ can have an influence. We see from (5.12) that the first non-vanishing perturbation for $i \geq 2$ is $\alpha _ { 2 } ^ { \overline { { \ell } } }$ . This explains the $\mathcal { O } ( H ^ { 7 } )$ error term in the first subdiagonal of Table 5.3.

For the $z$ -component, $\beta _ { 1 } ^ { 4 }$ is the first perturbation term for $i \geq 1$ . Hence the diagonal entries of the extrapolation tableau for the $z$ -component contain an error of size $\mathcal { O } ( H ^ { 4 } )$ . All other entries of Tables 5.3 and 5.4 can be verified analogously.

If we consider a step number sequence $\{ n _ { j } \}$ which is different from the harmonic sequence,we obtain the corresponding order tableaux as follows: the $j$ th diagonal of the new tableau is the $n _ { j }$ th diagonal of Table 5.3 and 5.4, respectively.

Theorem 5.4 then remains valid with $r _ { j k } , s _ { j k }$ given by these new tableaux. This implies that a larger $n _ { 1 }$ ，say ${ { \ n } _ { 1 } } = 2$ increases, the order of the extrapolated values. Numerical computations have shown that the sequence

$$
\{ 2 , 3 , 4 , 5 , 6 , \ldots \}
$$

is superior to the harmonic sequence. It is therefore recommended for SEULEX.

It is interesting to study the influence of the perturbation terms on the extra-polated values. Suppose that $\alpha _ { n _ { 1 } } ^ { j }$ (or $\beta _ { n _ { 1 } } ^ { j } )$ is the leading perturbation term in $Y _ { 1 1 }$ (or $Z _ { 1 1 }$ ). Because of the recursion (IV.9.26) all $Y _ { k k }$ then contain an error term of the form $C _ { k } H ^ { \jmath } \alpha _ { n _ { 1 } } ^ { \jmath }$ , whereas the $Y _ { \jmath k }$ (for $j > k$ ) do not depend on $\alpha _ { n _ { 1 } } ^ { \prime }$ . The error constants $C _ { k }$ are given recursively by

$$
C _ { 1 } = \frac { 1 } { n _ { 1 } ^ { J } } , \qquad C _ { k } = - \frac { n _ { 1 } } { n _ { k } - n _ { 1 } } C _ { k - 1 }
$$

and tend to zero exponentially, if $k$ increases.

# Error Expansion for Singular Perturbation Problems

Our aim is to extend the analysis of Example 5.1 to general singular perturbation problems

$$
\begin{array} { r l } { y ^ { \prime } = f ( y , z ) , \quad } & { { } y ( 0 ) = y _ { 0 } } \\ { \varepsilon z ^ { \prime } = g ( y , z ) , \quad } & { { } z ( 0 ) = z _ { 0 } , \quad 0 < \varepsilon \ll 1 , } \end{array}
$$

where the solution $y ( x ) , z ( x )$ is assumed to be sufficiently smooth (i.e., its deriva-tives up to a certain order are bounded independently of $\varepsilon$ ). An important observa-tion in Example 5.1 was the existence of smooth solutions of the (linear) differential equations for the coefficients $\boldsymbol { b } _ { \boldsymbol { \imath } } ( \boldsymbol { x } )$ . In the general situation we shall be concerned with equations of the form

$$
\begin{array} { r } { a ^ { \prime } = f _ { y } ( x ) a + f _ { z } ( x ) b + c ( x , \varepsilon ) } \\ { \varepsilon b ^ { \prime } = g _ { y } ( x ) a + g _ { z } ( x ) b + d ( x , \varepsilon ) } \end{array}
$$

(the coefficients $f _ { y } ( x ) = f _ { y } ( y ( x ) , z ( x ) )$ , etc. depend smoothly on $\varepsilon$ because the solution of (5.25) itself depends on $\varepsilon$ , even if $f$ and $g$ are $\varepsilon$ -independent).

Lemma 5.5. Suppose that the logarithmic norm of $g _ { z } ( x )$ satisfies

$$
\mu ( g _ { z } ( x ) ) \leq - 1 \qquad f o r \quad 0 \leq x \leq \overleftrightarrow { x } .
$$

For $a$ given value

$$
a ( 0 ) = a _ { 0 } ^ { 0 } + \varepsilon a _ { 0 } ^ { \perp } + \dots + \varepsilon ^ { N } a _ { 0 } ^ { N } + \mathcal { O } ( \varepsilon ^ { N + 1 } )
$$

there exists a unique $( u p t o \mathcal { O } ( \varepsilon ^ { N + 1 } ) )$

$$
b ( 0 ) = b _ { 0 } ^ { 0 } + \varepsilon b _ { 0 } ^ { 1 } + \dots + \varepsilon ^ { N } b _ { 0 } ^ { N } + \mathcal { O } ( \varepsilon ^ { N + 1 } )
$$

such that the solutions $a ( x )$ ， $b ( x )$ of (5.26) and their first $N$ derivatives are bounded independently of $\varepsilon$ ，

Proof. We insert the finite expansions

$$
\widehat { a } ( x ) = \sum _ { i = 0 } ^ { N } \varepsilon ^ { \prime } a _ { \ i } ( x ) , \quad \widehat { b } ( x ) = \sum _ { i = 0 } ^ { N } \varepsilon ^ { \prime } b _ { \ i } ( x )
$$

with $\varepsilon$ -independent coeficients $a _ { _ 2 } ( x ) b _ { i } ( x )$ into (5.26) and compare powers of $\varepsilon$ (see Section VI.2). This leads to the differential-algebraic system (2.4). Consequently, $a _ { 0 } ^ { 0 }$ determines $b _ { 0 } ^ { 0 }$ ; these two together with $a _ { 0 } ^ { 1 }$ determine $b _ { 0 } ^ { 1 }$ ,etc. The remainders $a ( x ) - { \widehat { a } } ( x ) , \ b ( x ) - { \widehat { b } } ( x )$ are then estimated as in the proof of Theorem 2.1. □

The next result exhibits the dominant perturbation terms in an asymptotic ex-pansion of the error of the linearly implicit Euler method, when it is applied to a singular perturbation problem.

Theorem 5.6 (Hairer&Lubich 1988). Assume that the solution of(5.25) is smooth. Under the condition

$$
\lVert ( I - \gamma g _ { z } ( 0 ) ) ^ { - 1 } \rVert \leq \frac { 1 } { 1 + \gamma } \qquad f o r a l l \quad \gamma \geq 1
$$

(which is a consequence of(5.27) and Theorem IV.11.2), the numerical solution of (5.1) possesses for $\varepsilon \leq h$ a perturbed asymptotic expansion of the form

$$
\begin{array} { l } { { y _ { i } = y ( x _ { i } ) + h a _ { 1 } ( x _ { i } ) + h ^ { 2 } a _ { 2 } ( x _ { i } ) + { \mathcal O } ( h ^ { 3 } ) } } \\ { { \displaystyle - \varepsilon f _ { z } ( 0 ) { g _ { z } ^ { - 1 } } ( 0 ) \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - \prime } \big ( h b _ { 1 } ( 0 ) + h ^ { 2 } b _ { 2 } ( 0 ) \big ) } } \\ { { z _ { \imath } = z ( x _ { \imath } ) + h b _ { 1 } ( x _ { \imath } ) + h ^ { 2 } b _ { 2 } ( x _ { \imath } ) + { \mathcal O } ( h ^ { 3 } ) } } \\ { { \displaystyle ~ - \left( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \right) ^ { - \displaystyle i } \big ( h b _ { 1 } ( 0 ) + h ^ { 2 } b _ { 2 } ( 0 ) \big ) } } \end{array}
$$

where $x _ { i } = i h \le H$ with $H$ sufficiently small (but independent of $\varepsilon$ ). The smooth functions $a _ { \ j } ( x ) , b _ { j } ( x )$ satisfy

$$
a _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ^ { 2 } ) , \quad a _ { 2 } ( 0 ) = \mathcal { O } ( \varepsilon ) , \quad b _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ) , \quad b _ { 2 } ( 0 ) = \mathcal { O } ( 1 ) .
$$

Proof. This proof is organized like that of Theorem 5.3. In part (a) we recursively construct truncated expansions (for $M \leq 2$ ）

$$
\begin{array} { l } { { \displaystyle { \widehat { y } } _ { i } = y \big ( x _ { i } \big ) + \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( a _ { j } \big ( x _ { i } \big ) + \alpha _ { i } ^ { \jmath } \big ) } } \\ { { \displaystyle { \widehat { z } } _ { \imath } = z \big ( x _ { i } \big ) + \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } \big ( x _ { i } \big ) + \beta _ { i } ^ { j } \big ) } } \end{array}
$$

such that

$$
\left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { \varepsilon I - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c c } { \widehat { y } _ { i + 1 } - \widehat { y } _ { i } } \\ { \widehat { z } _ { i + 1 } - \widehat { z } _ { i } } \end{array} \right) = h \left( \begin{array} { c c } { f ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \\ { g ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \end{array} \right) + \mathcal { O } ( h ^ { M + 2 } ) .
$$

The smooth functions $a _ { _ { 3 } } ( x ) , b _ { j } ( x )$ clearly depend on $\boldsymbol { \varepsilon }$ , but are independent of $h$ . The perturbation terms $\alpha _ { \ i } ^ { j } , \beta _ { \ i } ^ { j }$ (for $i \geq 1$ ),however,willdepend smoothly on $\varepsilon$ and on $\varepsilon / h$ . As in the case $\varepsilon = 0$ , we shall require that (5.15) and (5.16) hold. The differences $y _ { \imath } - \widehat { y } _ { \imath }$ and $z _ { \imath } - \widehat { z } _ { \imath }$ will then be estimated in part b).

a) The case $M = 0$ is obvious. Indeed, the values $\widehat { \boldsymbol { y } } _ { \boldsymbol { \imath } } = \boldsymbol { y } ( \boldsymbol { x } _ { \boldsymbol { \imath } } )$ ， $\widehat { z } _ { \iota } = z ( x _ { \iota } )$ satisfy (5.32) with $M = 0$ . The construction of the coefficients in (5.31) is done in two steps.

First step $( M = 1 )$ .We insert (5.31) into (5.32) and compare the smooth coefficients of $h ^ { 2 }$ . This gives

$$
\begin{array} { c } { { a _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { 1 } { 2 } y ^ { \prime \prime } ( x ) - f _ { y } ( 0 ) y ^ { \prime } ( x ) - f _ { z } ( 0 ) z ^ { \prime } ( x ) = f _ { y } ( x ) a _ { 1 } ( x ) + f _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { \varepsilon b _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { \varepsilon } { 2 } z ^ { \prime \prime } ( x ) - g _ { y } ( 0 ) y ^ { \prime } ( x ) - g _ { z } ( 0 ) z ^ { \prime } ( x ) = g _ { y } ( x ) a _ { 1 } ( x ) + g _ { z } ( x ) b _ { 1 } ( x ) } } \end{array}
$$

ByLemma 5.5 the initial value $b _ { \mathrm { 1 } } ( 0 )$ is uniquely determined by $a _ { \mathrm { \scriptsize ~ j } } ( 0 )$ . Differentiation of $\varepsilon z ^ { \prime } = g ( y , z )$ with respect to $\mathscr { x }$ gives $\varepsilon z ^ { \prime \prime } ( x ) = g _ { y } ( x ) y ^ { \prime } ( x ) + g _ { z } ( x ) z ^ { \prime } ( x )$ Inserted into (5.33b) this yields the relation

$$
g _ { y } ( 0 ) a _ { 1 } ( 0 ) + g _ { z } ( 0 ) b _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon )
$$

with known right-hand side.

As to the perturbation terms, we obtain by collecting everything up to $\mathcal { O } ( h ^ { 2 } )$

$$
\begin{array} { r l } { \alpha _ { i + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } - h f _ { y } ( 0 ) ( \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } ) - h f _ { z } ( 0 ) ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) } & { { } } \\ { = h f _ { y } ( x _ { \iota } ) \alpha _ { \iota } ^ { 1 } + h f _ { z } ( x _ { \iota } ) \beta _ { \iota } ^ { 1 } } & { { } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) - h g _ { y } ( 0 ) ( \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } ) - h g _ { z } ( 0 ) ( \beta _ { i + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) } & { { } } \\ { = h g _ { y } ( x _ { \iota } ) \alpha _ { \iota } ^ { 1 } + h g _ { z } ( x _ { \iota } ) \beta _ { \iota } ^ { 1 } } & { { } } \end{array}
$$

and try to determine the most important parts of this. We firstly replace $h f _ { y } ( x _ { \imath } ) \alpha _ { \imath } ^ { 1 }$ by $h f _ { y } ( 0 ) \alpha _ { \iota } ^ { 1 }$ and similarly for three other terms. This is motivated by the fact that we search for exponentially decaying $\alpha _ { \pmb { \imath } }$ . Therefore with $x _ { \imath } = i h$ ，

$$
\begin{array} { r } { \left( f _ { y } ( x _ { \imath } ) - f _ { y } ( 0 ) \right) \alpha _ { \imath } ^ { \rfloor } = \mathcal { O } ( h ) . } \end{array}
$$

Then many terms cancel in (5.35). We next observe that $\beta _ { i + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 }$ is multiplied by $\varepsilon$ ,but not $\alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 }$ . This suggests that the $\beta _ { \imath + \jmath } ^ { 1 }$ are an order of magnitude larger than $\boldsymbol \alpha _ { \imath + 1 } ^ { \mathrm { 1 } }$ . Neglecting therefore $\boldsymbol \alpha _ { \imath + 1 } ^ { 1 }$ where it competes with $\boldsymbol { \beta } _ { \iota + 1 } ^ { 1 }$ ,we are led to define

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } = h f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 1 } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) = h g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 1 } . } \end{array}
$$

It remains to verify a posteriori, that there exist solutions of $( 5 . 3 3 \mathrm { a } , \mathrm { b } , \mathrm { c } , \mathrm { d } )$ which produce an error term $\mathcal O ( h ^ { 3 } )$ in (5.32): from (5.33d) we obtain

$$
\beta _ { \iota } ^ { 1 } = \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - \iota } \beta _ { 0 } ^ { 1 } .
$$

Since we require $\alpha _ { \imath } ^ { 1 }  0$ for $i \to \infty$ ,the solution of (5.33c) is given by

$$
\alpha _ { \iota } ^ { 1 } = \varepsilon f _ { z } ( 0 ) { g } _ { z } ^ { - 1 } ( 0 ) \Big ( I - \frac { h } { \varepsilon } { g } _ { z } ( 0 ) \Big ) ^ { - \iota } \beta _ { 0 } ^ { 1 } .
$$

For $i \approx 0$ this implies the relation

$$
\alpha _ { 0 } ^ { 1 } = \varepsilon f _ { z } ( 0 ) g _ { z } ^ { - 1 } ( 0 ) \beta _ { 0 } ^ { 1 } .
$$

The assumption (5.15) together with (5.34) and (5.37) uniquely determine the coefficients $a _ { 1 } ( 0 ) , b _ { 1 } ( 0 ) , \alpha _ { 0 } ^ { 1 } , \beta _ { 0 } ^ { 1 }$ . We remark that $b _ { \mathbf { 1 } } ( 0 ) = { \mathcal { O } } ( \varepsilon )$ and $a _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ^ { 2 } )$ Using the fact that $\alpha _ { \ i } ^ { 1 } = \mathcal { O } ( \varepsilon ^ { 2 } )$ and $\varepsilon \leq h$ , one easily verifies that the quantities (5.31) with $M = 1$ satisfy (5.32).

Second step $M = 2 )$ . Comparing the smooth coefficients of $h ^ { 3 }$ in (5.32) gives two differential equations for $a _ { 2 } ( x ) , b _ { 2 } ( x )$ which are of the form (5.26). It follows from Lemma 5.5 that the initial values have to satisfy a relation

$$
g _ { y } ( 0 ) a _ { 2 } ( 0 ) + g _ { z } ( 0 ) b _ { 2 } ( 0 ) = \mathcal { O } ( 1 )
$$

with known right-hand side. As in the first step we require for the perturbations

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 2 } - \alpha _ { \iota } ^ { 2 } = h f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 2 } - \beta _ { \iota } ^ { 2 } ) = h g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } . } \end{array}
$$

and obtain the formulas (5.36) and (5.37) with $\alpha _ { \imath } ^ { 1 } , \beta _ { \imath } ^ { 1 }$ replaced by $\alpha _ { \ i } ^ { 2 } , \beta _ { \ i } ^ { 2 }$ . Again the values $a _ { 2 } ( 0 ) , b _ { 2 } ( 0 ) , \alpha _ { 0 } ^ { 2 } , \beta _ { 0 } ^ { 2 }$ are uniquely determined by (5.15), (5.38), and (5.37). Due to the $\mathcal { O } ( 1 )$ term in (5.38) we only have $b _ { 2 } ( 0 ) = \mathcal { O } ( 1 )$ and $a _ { 2 } ( 0 ) =$ ${ \mathcal { O } } ( \varepsilon )$

We still have to verify (5.32) with $M = 2$ . In the left-hand side we have ne-glected terms of the form $h f _ { y } ( 0 ) ( h \alpha _ { \iota } ^ { 1 } + h ^ { 2 } \alpha _ { i } ^ { 2 } )$ .This is justified,because $\alpha _ { \ i } ^ { 1 } =$ $\mathcal { O } ( \varepsilon ^ { 2 } )$ ， $\alpha _ { \ i } ^ { 2 } = \mathcal { O } ( \varepsilon )$ and $\varepsilon \leq h$ . The most dangerous term, neglected in the righthand side of (5.32) is

$$
h \big ( f _ { z } ( x _ { \imath } ) - f _ { z } ( 0 ) \big ) ( h \beta _ { \imath } ^ { 1 } + h ^ { 2 } \beta _ { \imath } ^ { 2 } ) .
$$

However, $f _ { z } ( x _ { \imath } ) - f _ { z } ( 0 ) = \mathcal { O } ( \imath h )$ ,and $\beta _ { \imath } ^ { 1 } = \mathcal { O } ( \varepsilon 2 ^ { - \imath } )$ ， $\beta _ { \imath } ^ { 2 } = \mathcal { O } ( 2 ^ { - \imath } )$ by (5.28) and $\varepsilon \leq h$ . This shows that the term (5.40) is also of size $\mathcal { O } ( h ^ { 4 } )$ ， so that (5.32) holds with $M = 2$

b) In order to estimate the remainder term,i.e., the differences $\Delta y _ { \imath } = y _ { \imath } - \widehat { y } _ { \imath }$ ， $\Delta z _ { \imath } = z _ { \imath } - \widehat { z } _ { \imath }$ we subtract (5.32) from (5.1) and eliminate $\Delta y _ { i + 1 }$ and $\Delta z _ { \imath + 1 }$ . This

gives

$$
\begin{array} { r l } & { \biggl ( \Delta y _ { i + 1 } \atop \Delta z _ { i + 1 } \biggr ) = \biggl ( \frac { \Delta y _ { i } } { \Delta z _ { i } } \biggr ) } \\ & { + \biggl ( \begin{array} { l l } { I + O ( h ) } & { \mathcal { O } ( h ) } \\ { O ( 1 ) } & { \left( \frac { \varepsilon } { h } I - g _ { z } ( 0 ) \right) ^ { - 1 } } \end{array} \biggr ) \biggl ( \begin{array} { l } { h \bigl ( f ( y _ { i } , z _ { i } ) - f ( \widehat { y } _ { i } , \widehat { z } _ { i } ) \bigr ) } \\ { g ( y _ { i } , z _ { i } ) - g ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \end{array} \biggr ) + \biggl ( \mathcal { O } ( h ^ { M + 2 } ) \biggr ) . } \end{array}
$$

Due to (5.28) and $\varepsilon \leq h$ we have

$$
\Big \| I + \Big ( \frac { \varepsilon } { h } I - g _ { z } ( 0 ) \Big ) ^ { - 1 } g _ { z } ( 0 ) \Big \| = \Big \| \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - 1 } \Big \| \leq \frac { \varepsilon } { \varepsilon + h } \leq \frac { 1 } { 2 } .
$$

We therefore again obtain (5.20) with some $| \varrho | < 1$ ,if $H$ is sufficiently small. We then deduce the result as in the proof of Theorem 5.3. □

![](images/0246742a20f1c7b322a3908bbdacc4b0f10356066f183ef642ddf26ec1fd2dfc.jpg)  
Fig. 5.1. Step size/error diagram

![](images/bdd6da939c45401d2d7d2ca58e0054a00b6edd52591b5d3c8f166c6f1f603777.jpg)  
Fig. 5.2. $T _ { j j }$ as functions of $H / \varepsilon$

Of course,it is possible to add a third step to the above proof. However, the recursions for $\alpha _ { i } ^ { 3 } , \beta _ { i } ^ { 3 }$ are no longer as simple as in (5.33) or (5.39). Moreover, the perturbations of (5.29) and (5.30) already describe very well the situation encountered in practice. We shallillustrate this with the following numerical example (see also Hairer &Lubich 1988).

Consider van der Pol's equation (2.73) with $\varepsilon = 1 0 ^ { - 5 }$ and with initial values (2.74) on the smooth solution. We take the step number sequence (5.23) and apply Method (5.1) $n _ { j }$ times with step size $h = H / n _ { j }$ The numerical result $Y _ { j 1 } , Z _ { j 1 }$ is then extrapolated according to (IV.9.26). In Fig.5.1 we show in logarithmic scale the errors $| Z _ { \ j j } - z ( H ) |$ for $j = 1 , 2 , \dots , 6$ as functions of $H$ . We observe that whenever the error is larger than $\varepsilon ^ { 2 } = 1 0 ^ { - 1 0 }$ ， the curves appear as straight lines with slopes $2 , 2 , 3 , 4 , 5$ , and 6,respectively. If its slope is $q$ , we have $\mathrm { l o g } ( e r r o r ) \approx$ $q \log { H } + C o n s t$ ,or equivalently $e r r o r \approx C H ^ { q }$ . This corresponds (with exception of the last one) to the orders predicted by the subdiagonal entries of Table 5.4 for the case $\varepsilon = 0$

In order to understand the irregular behaviour of the curves when the error becomes smaller than $\varepsilon ^ { 2 } = 1 0 ^ { - 1 0 }$ ， we study the influence of extrapolation on the perturbation terms in (5.30). Since $b _ { 1 } ( 0 )$ contains a factor $\varepsilon$ , the dominant part of the perturbation in $Z _ { j 1 }$ is $( I - ( h / \varepsilon ) g _ { z } ( 0 ) ) ^ { - n _ { j } } h ^ { 2 } b _ { 2 } ( 0 )$ ，where $b _ { 2 } ( 0 )$ is some constant and $\begin{array} { r } { h = H / n _ { g } } \\ { . } \end{array}$ : We assume the matrix $g _ { z } ( 0 )$ to be diagonalized and put $g _ { z } ( 0 ) = - 1$ . The dominant perturbation in $Z _ { \ j 1 }$ is therefore $\varepsilon ^ { 2 } T _ { j 1 } b _ { 2 } ( 0 )$ ，where

$$
T _ { j 1 } = \Big ( \frac { H } { \varepsilon n _ { j } } \Big ) ^ { 2 } \Big ( 1 + \frac { H } { \varepsilon n _ { j } } \Big ) ^ { - n _ { j } } .
$$

Due to the linearity of extrapolation, the dominant perturbation in $Z _ { \ j }$ will be $\varepsilon ^ { 2 } T _ { j j } b _ { 2 } ( 0 )$ ，where $T _ { j \jmath }$ is obtained from (5.42) and (IV.9.26). For the step number sequence (5.23) the values of $T _ { j j }$ are plotted as functions of $H / \varepsilon$ in Fig.5.2.For large values of $H / \varepsilon$ the curves appear as horizontal lines. This is a consequence of our choice $n _ { 1 } = 2$ and of the fact that

$$
T _ { j j } = C _ { j } \cdot \Big ( \frac { H } { \varepsilon } \Big ) ^ { 2 - n _ { 1 } } + \mathcal { O } \Big ( \Big ( \frac { H } { \varepsilon } \Big ) \Big ) ^ { 1 - n _ { 1 } } \qquad \mathrm { f o r } \quad \frac { H } { \varepsilon } \to \infty ,
$$

where $C _ { 1 } = 1$ and the other $C _ { \jmath }$ are given by the recursion (5.24).

The errors of Fig. 5.1 are now seen to be a superposition of the errors, predicted from the case $\varepsilon = 0$ (Theorem 5.4),and of the perturbations of Fig.5.2 scaled by a factor $\mathcal { O } ( \varepsilon ^ { 2 } )$ ·

Remark. As mentioned in Sect.VI.1, the implicit Euler discretization possesses a classical asymptotic expansion for differential-algebraic problems (1.6) of index 1 (case $\varepsilon = 0$ ). However, for singular perturbation problems,perturbations of the same type as in (5.29) and (5.3O) are present. The only difference is that all $b _ { i } ( 0 )$ contain a factor $\varepsilon$ for the implicit Euler method. For details and numerical experiments we refer to Hairer & Lubich (1988). A related analysis for a slightly different class of singular perturbation problems is presented in Auzinger, Frank & Macsek (1990).

# Dense Output

Extrapolation methods typically take very large (basic） step sizes during integra-tion. This makes it important that the method possess a continuous numerical solution. The first attempt to get a dense output for extrapolation methods is due to Lindberg (1972). His approach, however, imposes severe restrictions on the step number sequence. We present here the dense output of Hairer & Ostermann (1990), which exists for any step number sequence.

The main idea (due to Ch.Lubich) is the following: when computing the $j$ - th entry of the extrapolation tableau, we consider not only $Y _ { j 1 } = y _ { n _ { j } }$ ， but also compute the difference $( y _ { n _ { j } } - y _ { n _ { j } - 1 } ) / h _ { j }$ . Since these expressions possess an $h$ - expansion, their extrapolation gives an accurate approximation to $y ^ { \prime } ( x _ { 0 } + H )$ . By considering higher differences,we get also approximations to higher derivatives of $y ( x )$ at $x _ { 0 } + H$ . They are then used for Hermite interpolation. The reason for computing the derivatives only at the right end of the basic interval, is the presence of perturbation terms as described in Theorems 5.3 and 5.6. These perturbations are large at the beginning (near the initial value),but decrease exponentially for increasing $i$ . For the same reason, one must not use differences of a too high an order. We thus choose an integer $\lambda$ (usually O or 1) and avoid the values $y _ { 0 } , \ldots , y _ { n _ { 1 } + \lambda - 2 }$ for the computation of the finite differences. We remark that a similar idea was used by Deuflhard & Nowak (1987) to construct consistent initial values for differentialalgebraic problems.

An algorithmic description of the dense output for the linearly implicit Euler method is as follows (we suppose that the value $Y _ { \kappa \kappa }$ has been accepted as a numerical approximation to $y ( x _ { 0 } + H ) )$ .

Step $I$ For each $j \in \{ 1 , \ldots , \kappa \}$ we compute

$$
r _ { \jmath } ^ { ( k ) } = \frac { \nabla ^ { k } y _ { n _ { j } } ^ { ( \jmath ) } } { h _ { \jmath } ^ { k } } \qquad \mathrm { f o r } \quad k = 1 , \dots , j - \lambda .
$$

Here $y _ { \imath } ^ { ( { \jmath } ) }$ isthe approximation of $y ( x _ { i } )$ , Obaineding theuationf $Y _ { j 1 }$ and $\nabla y _ { \imath } = y _ { \imath } - y _ { \imath - 1 }$ is the backward difference operator.

Step 2. We exrapoate $r _ { \jmath } ^ { ( k ) }$ ， $\left( \kappa - k - \lambda \right)$ tiesis s t mation $\gamma ^ { ( k ) }$ t0 $y ^ { ( k ) } ( x _ { 0 } + H )$

Step 3. We define the polynomial $P ( \theta )$ of degree $\kappa$ by

$$
\begin{array} { l l } { { P ( 0 ) = y _ { 0 } , } } & { { P ( 1 ) = Y _ { \kappa \kappa } } } \\ { { P ^ { ( k ) } ( 1 ) = H ^ { k } r ^ { ( k ) } \quad } } & { { \mathrm { f o r } k = 1 , \ldots , \kappa - 1 . } } \end{array}
$$

The following theorem shows to which order these polynomials approximate the exact solution.

Theorem 5.7 (Hairer & Ostermann 1990). Consider a nonstiff differential equation and let $\lambda \in \{ 0 , 1 \}$ . Then, the error of the interpolation polynomial $P ( \theta )$ satisfies

$$
P ( \theta ) - y ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) \qquad f o r \quad H \to 0 .
$$

Proof. Since $P ( \theta )$ is a polynomial of degree $\kappa$ , the error due to interpolation is of size ${ \mathcal { O } } ( H ^ { \kappa + 1 } )$ . We know that $Y _ { \kappa \kappa } - y ( x _ { 0 } + H ) = \mathcal { O } ( H ^ { \kappa + 1 } )$ . Therefore it suffices to prove that

$$
r ^ { ( k ) } = y ^ { ( k ) } ( x _ { 0 } + H ) + \mathcal { O } ( H ^ { \kappa - k - \lambda + 1 } ) \qquad \mathrm { ~ f o r ~ } \quad k = 1 , \dots , \kappa - 1 .
$$

Due to the asymptotic expansion of the global error $y _ { \imath } - y ( x _ { \imath } )$ , the approximations $r _ { j } ^ { ( k ) }$ also have an expansion of the form

$$
r _ { j } ^ { ( k ) } = y ^ { ( k ) } ( x _ { 0 } + H ) + h _ { j } a _ { 1 } ^ { ( k ) } + h _ { j } ^ { 2 } a _ { 2 } ^ { ( k ) } + \dots .
$$

The statement (5.45) now follows from the fact that each extrapolation eliminates one power of $h$ in (5.46). □

It is now natural to investigate the error of the dense output $P ( \theta )$ also for stiff differential equations, such as singular perturbation problems. We shall treat here the limit case $\varepsilon = 0$ which is easier to analyse and, nevertheless, gives much insight into the structure of the error for very stiff problems.

For the differential-algebraic system (1.6) one defines the dense output in ex-actly the same way as for ordinary differential equations. As the system (1.6) is partitioned into $y -$ and $z$ -components, it is convenient to denote the corresponding interpolation polynomials by $P ( \theta )$ and $Q ( \theta )$ , respectively.

Theorem 5.8 (Hairer & Ostermann 1990). Let $y ( x ) , z ( x )$ be the solution of (1.6). Suppose that the step number sequence satisfies $n _ { 1 } + \lambda \ge 2$ with $\lambda \in \{ 0 , 1 \}$ . We then have

$$
\begin{array} { r l } & { P ( \theta ) - y ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) + \mathcal { O } ( H ^ { r + 1 } ) , } \\ & { Q ( \theta ) - z ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) + \mathcal { O } ( H ^ { s } ) , } \end{array}
$$

where $\mathscr { r }$ and $s$ are the $( \kappa + n _ { 1 } + \lambda - 2 , \kappa )$ -entries of Table 5.3 and Table 5.4, respectively.

Proof. We use the perturbed asymptotic error expansions of Theorem 5.3. Their smooth terms are treated exactly as in the proof of Theorem 5.7 and yield the ${ \mathcal { O } } ( H ^ { \kappa + 1 - \lambda } )$ error term in (5.47). The second error terms in (5.47) are due to $y _ { i }$ cpe $z _ { \imath }$ $i \ge n _ { \jmath } - j + \lambda$ $n _ { \jmath } - j \geq n _ { 1 } - 1$ $r _ { \jmath } ^ { ( k ) }$ $y _ { 0 } , \ldots , y _ { n _ { 1 } + \lambda - 2 }$ do not enter into the formulas for $r _ { j } ^ { ( k ) }$ ， so that the dominant perturbation comes from $y _ { n _ { 1 } + \lambda - 1 }$ (01 $z _ { n _ { 1 } + \lambda - 1 } )$ □

It is interesting to note that for $\lambda = 1$ , the second error term in (5.47) is of the same size as that in the numerical solution $Y _ { \kappa \kappa } , Z _ { \kappa \kappa }$ (see Theorem 5.4). However, one power of $H$ is lost in the first term of (5.47). On the other hand, one $H$ may be lost in the second error term,if $\lambda \approx 0$ . Both choices lead to a cheap (no additional function evaluations) and accurate dense output. Its order for $\theta \in ( 0 , 1 )$ is at most one lower than the order obtained for $\theta \simeq 1$ .

# Exercises

1. The linearly implicit mid-point rule, applied to the differential-algebraic system (1.6),reads

$$
\begin{array} { r l r } {  { ( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} ) ( \begin{array} { c } { y _ { { z + 1 } } - y _ { i } } \\ { z _ { i + 1 } - z _ { i } } \end{array} ) } } \\ & { } & { = - ( \begin{array} { c c } { I + h f _ { y } ( 0 ) } & { h f _ { z } ( 0 ) } \\ { h g _ { z } ( 0 ) } & { h g _ { z } ( 0 ) } \end{array} ) ( \begin{array} { c } { y _ { { z } } - y _ { { z - 1 } } } \\ { z _ { i } - z _ { i - 1 } } \end{array} ) + 2 h ( \begin{array} { c } { f ( y _ { { z } } , z _ { i } ) } \\ { g ( y _ { { z } } , z _ { i } ) } \end{array} ) . } \end{array}
$$

If we compute $y _ { 1 } , z _ { 1 }$ from (5.2),and if we define the numerical solution at $x _ { 0 } + H \enspace ( H = 2 m h )$ by

$$
\begin{array} { r l r } { y _ { h } ( x _ { 0 } + H ) = \frac { 1 } { 2 } ( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) , } & { { } } & { z _ { h } ( x _ { 0 } + H ) = \frac { 1 } { 2 } ( z _ { 2 m + 1 } + z _ { 2 m - 1 } ) , } \end{array}
$$

this algorithm constitutes an extension of (IV.9.16) to differential-algebraic problems.

a) Show that this method integrates the problem (5.8) exactly.

b) Apply the algorithm to

$$
y ^ { \prime } = 1 , \quad 0 = u - y ^ { 2 } , \quad 0 = v - y u , \quad 0 = w - y v , \quad 0 = z - y w
$$

with zero initial values and verify the formula

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \left( z _ { 2 m + 1 } + z _ { 2 m - 1 } \right) - z ( x _ { 2 m } ) = - 1 0 x _ { 2 m } ^ { 3 } h ^ { 2 } + 9 x _ { 2 m } h ^ { 4 } } \\ & { \phantom { \frac { 1 } { 2 } } - ( - 1 ) ^ { m } \bigl ( \frac { 1 } { 8 } x _ { 2 m } ^ { 5 } + x _ { 2 m } ^ { 3 } h ^ { 2 } + 9 x _ { 2 m } h ^ { 4 } \bigr ) . } \end{array}
$$

Remark. The error of the $z$ -component thus contains an $h$ -independent term of size $\mathcal { O } ( H ^ { 5 } )$ , which is not affected by extrapolation.

2. Consider the method of Exercise 1 as the basis of an $h ^ { 2 }$ -extrapolation me-thod. Prove that for the step number sequence (IV.9.22) the extrapolated values satisfy

$$
Y _ { j k } - y ( x _ { 0 } + H ) = { \mathcal { O } } ( H ^ { r _ { j k } + 1 } ) , \qquad Z _ { \ j k } - z ( x _ { 0 } + H ) = { \mathcal { O } } ( H ^ { s _ { \ j k } } )
$$

with $\boldsymbol { r } _ { j k } , \boldsymbol { s } _ { j k }$ given in Tables 5.5 and 5.6.

Hint. Interpret $Y _ { \ j 1 } , Z _ { \ j 1 }$ as numerical solution of a Rosenbrock method (Exercise 3 of Sect.IV.9) and verify the order condition derived in Sect. VI.3 (see also Hairer & Lubich (1988b) and C. Schneider (1993)).

Table 5.5. orders rjk ·

Table 5.6. orders S jk ·

$\begin{array} { l } { { 1 } } \\ { { 1 \quad 3 } } \\ { { 1 \quad 3 \quad 5 } } \\ { { 1 \quad 3 \quad 5 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 \quad 7 } } \end{array}$

5 5 5

Quasilinear differential equations are usually understood to be equations in which the highest derivative appears linearly. In the case of first order ODE systems, they are of the form

$$
C ( y ) \cdot y ^ { \prime } = f ( y ) ,
$$

where $C ( y )$ is a $n \times n$ -matrix. In the regions where $C ( y )$ is invertible,Eq. (6.1) can be written as

$$
y ^ { \prime } = C ( y ) ^ { - 1 } \cdot f ( y )
$$

and every ODE-code can be applied by solving at every function call a linear system. But this would destroy, for example, a banded structure of the Jacobian and it is therefore often preferable to treat Eq.(6.1) directly. If the matrix $C$ is everywhere of rank m $( m < n )$ ,Eq. (6.1) represents a quasilinear differential-algebraic system.

# Example: Moving Finite Elements

As an example, we present the classical idea of "moving finite elements", described in K. Miller & R.N. Miller (1981): the solution $u ( x , t )$ of a nonlinear partial differential equation

$$
\frac { \partial u } { \partial t } = L \big ( u ( x , t ) \big ) , \quad u ( 0 , t ) = u ( 1 , t ) = 0 ,
$$

where $L ( u )$ is an unbounded nonlinear differential operator, is approximated by finite element polygons $v ( x , a _ { 1 } , s _ { 1 } , \ldots , a _ { n } , s _ { n } )$ which satisfy $v ( s _ { j } , \ldots ) = a _ { j }$ (see Fig. 6.1). These polygons form a $2 n$ -dimensional manifold in the Hilbert space $L ^ { 2 } ( 0 , 1 )$ parametrized by $a _ { 1 } , s _ { 1 } , \ldots , a _ { n } , s _ { n }$ . The idea is now to move simultaneously $a ( t )$ and $s ( t )$ in oder to adapt at any time the finite element solution as best as possible to Eq.(6.2).

![](images/9d533172dfb7c7e8f72c7345eedb907d7dff46ce744b32570798b1234156f4e2.jpg)  
Fig. 6.1. Moving finite elements

We thus require that the defect $\dot { v } - L ( v )$ remains always orthogonal to the tangent space. The conditions

$$
\int _ { 0 } ^ { 1 } { \bigl ( } { \dot { v } } - L ( v ) { \bigr ) } \cdot { \frac { \partial v } { \partial a _ { j } } } d x = 0 \qquad \int _ { 0 } ^ { 1 } { \bigl ( } { \dot { v } } - L ( v ) { \bigr ) } \cdot { \frac { \partial v } { \partial s _ { j } } } d x = 0
$$

lead to a system of type (6.1) with

$$
\begin{array} { r l r l } & { c _ { 2 j - 1 , 2 k - 1 } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial a _ { j } } \cdot \frac { \partial v } { \partial a _ { k } } d x , } & & { c _ { 2 j - 1 , 2 k } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial a _ { j } } \cdot \frac { \partial v } { \partial s _ { k } } d x , } \\ & { c _ { 2 j , 2 k - 1 } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial s _ { j } } \cdot \frac { \partial v } { \partial a _ { k } } d x , } & & { c _ { 2 j , 2 k } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial s _ { j } } \cdot \frac { \partial v } { \partial s _ { k } } d x , } \\ & { f _ { 2 j - 1 } = \int _ { 0 } ^ { 1 } L ( v ) \cdot \frac { \partial v } { \partial a _ { j } } d x , } & & { f _ { 2 j } = \int _ { 0 } ^ { 1 } L ( v ) \cdot \frac { \partial v } { \partial s _ { j } } d x . } \end{array}
$$

For the partial derivatives of $v$ , sketched in Fig.6.1, the non-zero of these scalar products become

$$
\begin{array} { l l } { { c _ { 2 j - 1 , 2 j - 1 } = \frac { 1 } { 3 } ( \triangle _ { j } + \triangle _ { j + 1 } ) } } & { { c _ { 2 j - 1 , 2 j } = - \frac { 1 } { 3 } ( m _ { j } \triangle _ { j } + m _ { j + 1 } \triangle _ { j + 1 } ) } } \\ { { c _ { 2 j , 2 j - 1 } = - \frac { 1 } { 3 } ( m _ { j } \triangle _ { j } + m _ { j + 1 } \triangle _ { j + 1 } ) } } & { { c _ { 2 j , 2 j } = \frac { 1 } { 3 } ( m _ { j } ^ { 2 } \triangle _ { j } + m _ { j + 1 } ^ { 2 } \triangle _ { j + 1 } ) + \displaystyle \frac { 2 \varepsilon ^ { 2 } } { \angle \varepsilon } . } } \end{array}
$$

$$
\begin{array} { r l } { c _ { 2 j - 1 , 2 j + 1 } = c _ { 2 j + 1 , 2 j - 1 } = \frac { 1 } { 6 } \Delta _ { j + 1 } } & { { } c _ { 2 j - 1 , 2 j + 2 } = c _ { 2 j + 2 , 2 j - 1 } = - \frac { 1 } { 6 } m _ { j + 1 } \Delta _ { j + 1 } } \\ { c _ { 2 j , 2 j + 1 } = c _ { 2 j + 1 , 2 j } = - \frac { 1 } { 6 } m _ { j + 1 } \Delta _ { j + 1 } } & { { } c _ { 2 j , 2 j + 2 } = c _ { 2 j + 2 , 2 j } = \frac { 1 } { 6 } m _ { j + 1 } ^ { 2 } \Delta _ { j + 1 } - \varepsilon ^ { 2 } } \end{array}
$$

where

$$
\Delta _ { \ j } = s _ { j } - s _ { j - 1 } , \quad m _ { j } = ( a _ { j } - a _ { j - 1 } ) / \Delta _ { \ j } , \qquad j = 1 , \ldots , n + 1 .
$$

The matrix $C ( y )$ is banded with bandwidth $3 + 1 + 3$ . The $\varepsilon ^ { 2 }$ -terms in (6.5) come from an “internodal viscosity” penalty term, explained in Miller & Miller (1981), which aims to regularize the relative movement of the nodes $s _ { j }$ whenever their position is ill-conditioned,which happens to appear in the vicinity of inflection points (see Fig.6.2).

It is then hoped that the nodes move automatically into the critical regions of the solutions, move with shocks which may appear, and that $a ( t )$ and $s ( t )$ become smooth functions.

Application to Burgers’Equation. Burgers’Equation is given by

$$
u _ { t } = - u u _ { x } + \mu u _ { x x } \qquad \mathrm { o r } \qquad u _ { t } = - \Big ( \frac { u ^ { 2 } } { 2 } \Big ) _ { x } + \mu u _ { x x }
$$

where $\mu = 1 / R$ and $R$ is called te Reynolds number. This is one of the equations originally designed by Burgers (1948） as $^ { 6 6 } \mathbf { 2 }$ mathematical model illustrating the theory of turbulence". However, soon afterwards,E. Hopf (195O) presented an analytical solution (see Exercise 1 below) and concluded that “we doubt that Burgers’equation fully illustrates the statistics of free turbulence.(...） Equation (1） is too simple a model to display chance fluctuations ...". Nowadays it remains interesting as a nonlinear equation resembling the Navier-Stokes' equations in fluid dynamics which possesses, for $R$ large,shock waves and, for $R \to \infty$ ， discontinuous solutions. Here,the integrals in (6.4) become

$$
f _ { 2 j - 1 } = A _ { j } + \mu B _ { j } , \quad f _ { 2 j } = C _ { j } + \mu D _ { \jmath } , \qquad j = 1 , \ldots n .
$$

where

$$
\begin{array} { r l } & { A _ { j } = \big ( a _ { j - 1 } - a _ { j } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j - 1 } \big ) + \big ( a _ { j } - a _ { j + 1 } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j + 1 } \big ) , } \\ & { B _ { j } = \big ( m _ { j + 1 } - m _ { j } \big ) , } \\ & { C _ { j } = - m _ { j } \big ( a _ { j - 1 } - a _ { j } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j - 1 } \big ) - m _ { j + 1 } \big ( a _ { j } - a _ { j + 1 } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j + 1 } \big ) , } \\ & { D _ { j } = \big ( m _ { j + 1 } - m _ { j } \big ) \big ( \frac { 1 } { 2 } m _ { j + 1 } + \frac { 1 } { 2 } m _ { j } \big ) , } \end{array}
$$

(in the case of $D _ { \ j }$ appears the product of a Dirac $\delta$ function with a discontinuous function; these must be suitably “mollified"). We choose as initial function

$$
u ( x , 0 ) = ( \sin ( 3 \pi x ) ) ^ { 2 } \cdot ( 1 - x ) ^ { 3 / 2 } \ , \qquad \mu = 0 . 0 0 0 3
$$

and as initial positions

$$
s _ { j } = j / ( n + 1 ) , \quad a _ { j } = u ( s _ { j } , 0 ) , \qquad j = 1 , \ldots , n , \quad n = 1 0 0 ,
$$

and solve the problem with smoothing parameter $\varepsilon = 1 0 ^ { - 2 }$ for $0 \leq t \leq 1 . 9$ . Two shock waves arise which later fuse into one (see Fig. 6.2).

![](images/f229978c2f7bfcd0247816cb24e24a34384387e1d403dc1c5072fd063046ff93.jpg)  
Fig. 6.2.Moving finite element solution of Burgers’ equation

# Problems of Index One

For invertible $C ( y )$ ，Eq.(6.1） is an ordinary differential equation and standard theory (for existence and uniqueness results) can be applied. If the matrix is illconditioned or even singular, new investigations are necessary. In order to exclude equations with singularities, such as $x y ^ { \prime } = ( q + b x ) y$ (see Sect.I.5), we assume that

$$
C ( y ) { \mathrm { ~ h a s ~ c o n s t a n t ~ r a n k ~ } } m ( m < n )
$$

in a neighbourhood of the solution. Then the columns of $C ( y )$ span an $m$ -dimensional subspace $\mathcal { I } m \ : C ( y )$ which moves with $y$ . Clearly, in order that (6.1） can make sense, we need consistent initial values,i.e., we need

$$
f ( y _ { 0 } ) \in { \underline { { \tau } } } m C ( y _ { 0 } ) .
$$

We shall now show, how, under a certain condition, this property can be satisfied for all $_ x$ and determines uniquely the solution: choose a nonsingular matrix

$$
T ( y ) = { \binom { T _ { 1 } ( y ) } { T _ { 2 } ( y ) } } \qquad { \mathrm { s u c h ~ t h a t } } \qquad T ( y ) C ( y ) = { \binom { B _ { 1 } ( y ) } { 0 } } ;
$$

this means that the rows of $T _ { 2 } ( y )$ must span the $( n - m )$ -dimensional orthogonal complement of $\mathcal { T } m C ( y )$ . Then we multiply Eq. (6.1) by $T ( y )$ and obtain

$$
\left( { \begin{array} { c } { B _ { 1 } ( y ) } \\ { 0 } \end{array} } \right) y ^ { \prime } = \left( { \begin{array} { c } { T _ { 1 } ( y ) f ( y ) } \\ { T _ { 2 } ( y ) f ( y ) } \end{array} } \right) ,
$$

so that the condition corresponding to (6.9) becomes visible in the form $\begin{array} { r } { T _ { 2 } ( y ) f ( y ) = } \end{array}$ O. Differentiating this relation and inserting the derivative into the second part of (6.11), we obtain

$$
\left( { \cal B } _ { 1 } ( y ) \atop ( T _ { 2 } f ) ^ { \prime } ( y ) \right) y ^ { \prime } = \left( { \displaystyle ( T _ { 1 } f ) ( y ) \atop 0 } \right) ,
$$

which is a regular quasilinear equation if the matrix

$$
\begin{array} { r } { \left( \begin{array} { c } { B _ { 1 } ( y ) } \\ { ( T _ { 2 } f ) ^ { \prime } ( y ) } \end{array} \right) \qquad \mathrm { i s ~ i n v e r t i b l e . } } \end{array}
$$

Lemma 6.1. Let the matrix $C ( y )$ satisfy (6.8) and (6.13),and let the initial values $y _ { 0 }$ fulfill (6.9). Then, the quasilinear problem $C ( y ) y ^ { \prime } = f ( y )$ $y ( x _ { 0 } ) = y _ { 0 }$ possesses a locally unique solution.

Proof. Condition (6.9) means that $T _ { 2 } ( y _ { 0 } ) f ( y _ { 0 } ) = 0$ and the second part of (6.12) assures that $( T _ { 2 } ( y ( x ) ) f ( y ( x ) ) ) ^ { \prime } = 0$ . Therefore we have $( T _ { 2 } f ) ( y ( x ) ) = 0$ for all $_ x$ , and the solution of (6.12) solves also (6.11) and (6.1). □

The following result gives a consequence of condition (6.13) which shall be essential in the later discussions of feasibility of numerical procedures.

Lemma 6.2. Assume that $C ( y )$ satisfies (6.8) and (6.13). If $f ( y _ { 0 } ) = C ( y _ { 0 } ) y _ { 0 } ^ { \prime }$ ， then the matrix

$$
C ( y ) + \lambda \bigl ( f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) \bigr )
$$

is invertible for sufficiently small $\lambda \neq 0$ and for $y$ sufficiently close to $y _ { 0 }$ .Here,

$$
\Gamma ( y , y ^ { \prime } ) = { \frac { \partial } { \partial y } } { \big ( } C ( y ) y ^ { \prime } { \big ) } .
$$

Proof. Condition (6.13) implies that

$$
T ( y ) C ( y ) + \lambda ( T f ) ^ { \prime } ( y _ { 0 } ) \qquad \mathrm { i s ~ i n v e r t i b l e }
$$

for small $\lambda \neq 0$ and $y$ close to $y _ { 0 }$ . Using $T ^ { \prime } C + T C ^ { \prime } = B ^ { \prime }$ we have

$$
( T ^ { \prime } f ) ( y _ { 0 } ) = T ^ { \prime } ( y _ { 0 } ) C ( y _ { 0 } ) y _ { 0 } ^ { \prime } = - T ( y _ { 0 } ) \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) + B ^ { \prime } ( y _ { 0 } ) y _ { 0 } ^ { \prime } .
$$

Since $B ^ { \prime } ( y _ { 0 } ) y _ { 0 } ^ { \prime }$ does not contribute to the lower block of the matrix (6.14), it can be neglected after insertion of $( T f ) ^ { \prime } = T f ^ { \prime } + T ^ { \prime } f$ and (6.15) into (6.14). This implies that

$$
T ( y ) C ( y ) + \lambda T ( y _ { 0 } ) { \big ( } f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) { \big ) } \qquad { \mathrm { i s ~ i n v e r t i b l e . } }
$$

The statement of the Lemma now follows from a continuity argument.

# Numerical Treatment of $C ( \boldsymbol { y } ) \boldsymbol { y } ^ { \prime } = f ( \boldsymbol { y } )$

As has been said above, in the case of invertible matrices $C ( y )$ , one can eventually apply an explicit numerical method to (6.1').However,if Eq.(6.1') is stiff,implicit methods have to be applied. In this case it may be advantageous to have methods that avoid the computation of the Jacobian of $C ( y ) ^ { - 1 } f ( y )$

Transformation to Semi-Explicit Form. In the case where (6.1') is stiff or where $C ( y )$ is singular and satisfies (6.8) and (6.13) we introduce $z = y ^ { \prime }$ as new variable, such that system (6.1) becomes of the semi-explicit form

$$
\begin{array} { c } { { y ^ { \prime } = z } } \\ { { 0 = C ( y ) z - f ( y ) } } \end{array}
$$

Here,all methods of the preceding sections can be applied (at least formally). The study of convergence, however, needs further investigation, because Condition (1.7) is no longer satisfied here.

Implicit Runge-Kutta and Multistep Methods. With the $\varepsilon$ -embedding approach (see (1.11) for Runge-Kutta methods and (2.2) for multistep methods) we are led to

nonlinear equations, which, when solved by Newton iterations, require the solution of linear systems of the form

$$
\left( \begin{array} { c c } { - \alpha I } & { I } \\ { \Gamma ( y _ { 0 } , z _ { 0 } ) - f ^ { \prime } ( y _ { 0 } ) } & { C ( y _ { 0 } ) } \end{array} \right) .
$$

Here $\alpha = ( \gamma h ) ^ { - 1 }$ ，and $\gamma$ is an eigenvalue of the Runge-Kutta matrix. By Lemma 6.2 this matrix is invertible for small enough $h > 0$ . Convergence follows from the results of Sections VI.3 and VII.4 (see Exercise 2).

Rosenbrock Methods. Method (4.3) applied to system (6.16) leads to

$$
\left( { v _ { \mathfrak { r } } } _ { \mathfrak { a } } \right) = \left( { y _ { 0 } } \atop { z _ { 0 } } \right) + \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } \left( { k _ { \jmath } } \atop { \ell _ { \jmath } } \right) , \qquad \left( { y _ { 1 } } \atop { z _ { 1 } } \right) = \left( { y _ { 0 } } \atop { z _ { 0 } } \right) + \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } \left( { k _ { \imath } } \atop { \ell _ { i } } \right) .
$$

$$
\binom { k _ { i } } { 0 } = h \left( { C ( v _ { i } ) w _ { i } } + h \left( { \begin{array} { c c } { 0 } & { I } \\ { \Gamma _ { 0 } - f _ { 0 } ^ { \prime } } & { C ( y _ { 0 } ) } \end{array} } \right) \sum _ { j = 1 } ^ { i } \gamma _ { \upsilon _ { j } } \binom { k _ { j } } { \ell _ { j } } . \right)
$$

Again, it can be seen that (6.18b) represents a linear system whose regularity is assured by Lemma 6.2. However, since Condition (1.7) is not satisfied, a new theory for the order conditions of the local error as well as for convergence of the global error is necessary. This theory reveals, for example, that new order conditions for the coefficients are necessary and explains why, say, the code RODAS, directly applied to (6.16), does not give precise results. For full details we refer the reader to the original publication Lubich & Roche (1990).

# Extrapolation Methods

The first problem is to find suitable linearly implicit Euler discretizations for (6.1), to serve as basic method for the extrapolation algorithm (see Sect.IV.9).

Method of Deuflhard & Nowak. Applying the linearly implicit Euler method (IV.9.15) to the differential equation (6.1') we obtain

$$
( I - h A ) ( y _ { i + 1 } - y _ { \imath } ) = h C ( y _ { i } ) ^ { - 1 } f ( y _ { \imath } )
$$

where

$$
A \approx ( C ^ { - 1 } f ) ^ { \prime } ( y _ { 0 } ) = C ( y _ { 0 } ) ^ { - 1 } \left( f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) \right)
$$

with $\Gamma ( y , y ^ { \prime } )$ as in Lemma 6.2. Multiplication of (6.19) with $C ( y _ { \imath } )$ yield:

$$
\left( C ( y _ { \iota } ) - h C ( y _ { \iota } ) C ( y _ { 0 } ) ^ { - 1 } J \right) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( y _ { \iota } )
$$

with $J = f \prime ( y _ { 0 } ) - \Gamma \big ( y _ { 0 } , y _ { 0 } ^ { \prime } \big )$ ．Deuflhard & Nowak（1987） suggest to replace $C ( y _ { \imath } ) C ( y _ { 0 } ) ^ { - 1 }$ by the identity matrix,which “may be interpreted as just introduc-ing an approximation error into the Jacobian matrix". This leads to the discretization

$$
\left( C ( y _ { \imath } ) - h J \right) ( y _ { \imath + 1 } - y _ { \imath } ) = h f ( y _ { \imath } )
$$

which represents the basic step for the code LIMEX described in Deuflhard & Nowak (1987). The regularity of the matrix of this linear system is again assured by Lemma 6.2.

The computation of $J$ requires an approximation to $z _ { 0 } = y _ { 0 } ^ { \prime }$ . Such consistent initial values must be computed explicitely for the first basic steps,and are obtained by extrapolation of

$$
z _ { n } = ( y _ { n } - y _ { n - 1 } ) / h
$$

in the subsequent steps.

Linearly-Implicit Euler to Semi-Explicit Model. Another possibility is to apply the linearly-implicit Euler discretization (5.2) to the differential-algebraic system (6.16). This gives

$$
\left( \begin{array} { c c } { I } & { - h I } \\ { - h J } & { h C ( y _ { 0 } ) } \end{array} \right) \left( \begin{array} { c } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { c } { z _ { \iota } } \\ { f ( y _ { \iota } ) - C ( y _ { \iota } ) z _ { \iota } } \end{array} \right)
$$

with $z _ { 0 } = y _ { 0 } ^ { \prime } = y ^ { \prime } ( x _ { 0 } )$ . The first line yields $z _ { \imath + 1 } = ( y _ { \imath + 1 } - y _ { \imath } ) / h$ and the second line becomes

$$
\left( C ( y _ { 0 } ) - h J \right) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( y _ { \iota } ) - \left( C ( y _ { \iota } ) - C ( y _ { 0 } ) \right) ( y _ { \iota } - y _ { \iota - 1 } ) .
$$

The right-most term vanishes for $i = 0$ ,so that $y _ { - 1 }$ does not enter the algorithm.

Asymptotic Expansions. The theoretical justification of the use of either (6.20) or (6.23)as basic step for an extrapolation process requires the investigation of the asymptotic expansion of their global errors.

In the situation where $C ( y )$ is invertible, the discretization (6.2O) is a consistent one-step discretization of (6.1'） and possesses therefore,by standard theory (Theorem II.8.1),an asymptotic expansion, the terms of which, however, depend on the stiffness. Since the system (6.16) is of the form (1.6) with assumption (1.7) satisfied, we can conclude from Theorem 5.3 the existence of a perturbed asymptotic expansion for the second discretization (6.23).

In the situation where $C ( y )$ is singular,Lubich (1989) reveiled the existence of a perturbed asymptotic expansion for both discretizations (6.20) and (6.23). We refer to this original publication for further details, in particular to the study of the influence of these perturbations to the extrapolated numerical approximation.

# Exercises

1. Reconstruct E. Hopf's analytic solution of Burgers' equation (6.6). Hint. Introduce the new dependent variable

$$
\varphi ( x , t ) = \exp \left\{ - \frac { 1 } { 2 \mu } \int _ { 0 } ^ { x } u ( \xi , t ) d \xi - \int _ { 0 } ^ { t } c ( \tau ) d \tau \right\} .
$$

Show that for a suitably chosen $c ( t )$ the function $\varphi ( x , t )$ satisfies the one dimensional heat equation. The solution $u ( x , t )$ of (6.6) can then be recovered from $\varphi ( x , t )$ by

$$
u = - 2 \mu ( \log \varphi ) _ { x } = - 2 \mu ( \varphi _ { x } / \varphi ) .
$$

2.Assume that (6.8) and (6.13) hold. By eliminating from $0 = C ( y ) z - f ( y )$ as many components of $z$ as possible, transform the system (6.16) into an equivalent one of the form

$$
y ^ { \prime } = F ( y , u ) , \qquad 0 = G ( y ) ,
$$

where $u$ collects the remaining components of $z$ ·

a) Prove that Runge-Kutta methods and multistep methods are invariant with respect to this transformation.

b) Show that $G _ { y } ( y ) F _ { u } ( y , u )$ is invertible, so that the convergence results of Sections VII.3 and VII.4 can be applied.

3. (Quasilinear problems with gradient-type mass-matrix, see HLR89, page 111). Consider the electrical circuit (1.14), but suppose this time that the capacities depend on the voltages, e.g. as

$$
C _ { k } = { C _ { k 0 } } / { \left( 1 - ( U _ { i } - U _ { j } ) / U _ { b } \right) ^ { 1 / 2 } }
$$

so that the expressions $C _ { k } ( U _ { i } ^ { \prime } - U _ { j } ^ { \prime } )$ in (1.14) must be replaced by $( C _ { k } ( U _ { \imath } -$ $U _ { \jmath } ) /$ . Show that then the corresponding equations are of the form (6.1) with

$$
C ( y ) = A q ^ { \prime } ( y )
$$

where $A$ is a constant matrix and $q ( y )$ a known function of $y$ . Show that such problems can be efficiently solved by introducing $q ( y ) = z$ as a new variable such that the problem becomes semi-explicit as

$$
A z ^ { \prime } = f ( y ) , \qquad 0 = z - q ( y ) .
$$

# Chapter VII. Differential-Algebraic Equations of Higher Index

![](images/62063237685b84940fee033d61d0f261f48b19af3c0b3af89fdfccdffd92aea2.jpg)  
(Drawing by K.Wanner)

In the preceding chapter we considered the simplest special case of differentialalgebraic equations - the so-called index 1 problem. Many problems of practical interest are, however, of higher index, which makes them more and more difficult for their numerical treatment.

We start by classfying differential-algebraic equations (DAE) by the index (index of nilpotency for linear problems with constant coefficients; differentiation and perturbation index for general nonlinear problems) and present some examples arising in applications (Sect. VII.1). Several different approaches for solving numerically higher index problems are discussed in Sect. VI1.2: index reduction by differentiation combined with suitable projections,state space form methods, and treatment as overdetermined or unstructured systems. Sections VI1.3 and VII.4 study the convergence properties of multistep methods and Runge-Kutta methods when they are applied directly to index 2 systems. It may happen that the order of convergence is lower than for ordinary differential equations ("order reduction"). The study of conditions which guarantee a certain order is the subject of Sect. VII.5. Half-explicit methods for index 2 problems are especially suited for constrained mechanical systems (Sect. VI.6). A multibody mechanism and its numerical treatment are detailed in Sect. VI1.7. Finally, we discuss symplectic methods for constrained Hamiltonian systems (Sect. VII.8), and explain their long-term behaviour by a backward error analysis for differential equations on manifolds.

# VII.1 The Index and Various Examples

The most general form of a differential-algebraic system is that of an implicit differential equation

$$
F ( u ^ { \prime } , u ) = 0
$$

where $F$ and $u$ have the same dimension. We always assume $\boldsymbol { F }$ to be sufficiently differentiable. A non-autonomous system is brought to the form(1.1) by appending $\mathscr { x }$ to the vector $u$ , and by adding the equation $x ^ { \prime } = 1$

If $\partial F / \partial u ^ { \prime }$ is invertible we can formally solve (1.1) for $u ^ { \prime }$ to obtain an ordinary differential equation. In this chapter we are interested in problems (1.1） where $\partial F / \partial u ^ { \prime }$ is singular.

# Linear Equations with Constant Coefficients

Uebrigens kann ich die Meinung des Hrn. Jordan nicht theilen, dass es ziemlich schwer sei, der Weierstrass-schen Analyse zu folgen； sie scheint mir im Gegentheil vollkommen durchsichtig zu sein, ... (L. Kronecker 1874)

The simplest and best understood problems of the form(1.1) are linear differential equations with constant coefficients

$$
B u ^ { \prime } + A u = d ( x ) .
$$

In looking for solutions of the form $e ^ { \lambda x } u _ { 0 }$ (if $d ( x ) \equiv 0 { \mathrm { . } }$ ） we are led to consider the “matrix pencil” $A + \lambda B$ . When $A + \lambda B$ is singular for all values of $\lambda$ , then (1.2)has either no solution or infinitely many solutions for a given initial value (Exercise 1). We shall therefore deal only with regular matrix pencils, i.e., with problems where the polynomial $\operatorname* { d e t } ( A + \lambda B )$ does not vanish identically. The key to the solution of (1.2) is the following simultaneous transformation of $A$ and $B$ to canonical form.

Theorem 1.1(Weierstrass 1868, Kronecker 1890). Let $A + \lambda B$ be a regular matrix pencil. Then there exist nonsingular matrices $P$ and $Q$ such that

$$
P A Q = \left( { \begin{array} { c c } { C } & { 0 } \\ { 0 } & { I } \end{array} } \right) , \qquad P B Q = \left( { \begin{array} { c c } { I } & { 0 } \\ { 0 } & { N } \end{array} } \right)
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $I I _ { \perp }$ Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_31, $©$ Springer-Verlag Berlin Heidelberg 2010

where N = blockdiag $( N _ { 1 } , \ldots , N _ { k } )$ ,each $N _ { \imath }$ is of the form

$$
N _ { \imath } = \left( \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { } } & { { 0 } } \\ { { } } & { { \cdot \cdot } } & { { \cdot \cdot } } & { { } } \\ { { } } & { { } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { } } & { { } } & { { 0 } } \end{array} \right) ,
$$

and $C$ can be assumed to be in Jordan canonical form.

Proof (Gantmacher 1954 (Chapter XII),see also Exercises 2 and 3). We fix some $c$ such that $A + c B$ is invertible. If we multiply

$$
A + \lambda B = A + c B + ( \lambda - c ) B
$$

by the inverse of $A + c B$ and then transform $( A + c B ) ^ { - 1 } B$ to Jordan canonical form (Theorem I.12.2) we obtain

$$
\left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { I } } \end{array} \right) + \left( \lambda - c \right) \left( \begin{array} { c c } { { J _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { J _ { 2 } } } \end{array} \right) .
$$

Here, $J _ { 1 }$ contains the Jordan blocks with non-zero eigenvalues, $J _ { 2 }$ those with zero eigenvalues (the dimension of $J _ { 1 }$ is just the degree of the polynomial $\operatorname* { d e t } ( A +$ $\lambda B )$ ). Consequently, ${ { J } _ { 1 } }$ and $I - c J _ { 2 }$ are both invertible and multiplying (1.5) from the left by blockdiag $\left( J _ { 1 } ^ { - 1 } , ( I - \bar { c } J _ { 2 } ) ^ { - 1 } \right)$ gives

$$
\left( { \begin{array} { c c } { J _ { 1 } ^ { - 1 } ( I - c J _ { 1 } ) } & { 0 } \\ { 0 } & { I } \end{array} } \right) + \lambda \left( { \begin{array} { c c } { I } & { 0 } \\ { 0 } & { ( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 } } \end{array} } \right) .
$$

The matrices $J _ { 1 } ^ { - 1 } ( I - c J _ { 1 } )$ and $( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 }$ can then be brought to Jordan canonical form. Since all eigenvalues of $( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 }$ are zero,we obtain the desired decomposition (1.3). □

Theorem 1.1 allows us to solve (1.2) as follows: we premultiply(1.2) by $P$ and use the transformation

$$
u = Q \left( \begin{array} { c } { { y } } \\ { { z } } \end{array} \right) , \qquad P d ( x ) = \left( \begin{array} { c } { { \eta ( x ) } } \\ { { \delta ( x ) } } \end{array} \right) .
$$

This decouples the differential-algebraic system (1.2) into

$$
y ^ { \prime } + C y = \eta ( x ) , \qquad N z ^ { \prime } + z = \delta ( x ) .
$$

The equation for $y$ is just an ordinary differential equation. The relation for $z$ decouples again into $k$ subsystems, each of the form (with $m = m _ { \imath }$ ）

$$
z _ { 2 } ^ { \prime } + z _ { 1 } = \delta _ { 1 } ( x )
$$

$$
\begin{array} { c } { { z _ { m } ^ { \prime } + z _ { m - 1 } = \delta _ { m - 1 } ( x ) } } \\ { { z _ { m } = \delta _ { m } ( x ) . } } \end{array}
$$

Here $z _ { m }$ is determined by the last equation,and the other components are obtained recursively by repeated differentiation. Thus $z _ { 1 }$ depends on the $( m - 1 )$ -th derivative of $\delta _ { m } ( x )$ . Since numerical differentiation is an unstable procedure, the largest $m _ { \imath }$ appearing in (1.4） is a measure of numerical difficulty for solving problem (1.2). This integer $\left( \operatorname* { m a x } { m _ { \ i } } \right)$ ） is called the index of nilpotency of the matrix pencil $A + \lambda B$ . It does not depend on the particular transformation used to get (1.3) (see Exercise 4).

Linear Equations with Variable Coefficients. In the case, where the matrices $A$ and $B$ in (1.2) depend on $\boldsymbol { x }$ , the study of the solutions is much more complicated. Multiplying the equation by $P ( x )$ and substituting $u = Q ( x ) v$ , yields the system

$$
P B Q v ^ { \prime } + ( P A Q + P B Q ^ { \prime } ) v = 0 ,
$$

which shows that the transformation (1.3) is no longer relevant. With the use of transformations of the form (1.8), Kunkel & Mehrmann (1995) derive a canonical form for linear systems with variable coefficients.

# Differentiation Index

A lot of English cars have steering wheels. (Fawlty Towers,Cleese and Booth 1979)

Let us start with the following example:

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = 0 . 7 \cdot y _ { 2 } + \sin ( 2 . 5 \cdot z ) = f _ { 1 } ( y , z ) } \\ & { y _ { 2 } ^ { \prime } = 1 . 4 \cdot y _ { 1 } + \cos ( 2 . 5 \cdot z ) = f _ { 2 } ( y , z ) } \\ & { 0 = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } - 1 = g ( y ) . } \end{array}
$$

The“control variable” $z$ in (1.9a) can be interpreted as the position of a “steering wheel” keeping the vector field $( y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } )$ tangent to the circle $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } = 1$ ,so that condition (1.9b) remains continually satisfied (see Fig.1.1a). By differentiating (1.9b) and substituting(1.9a) we therefore must have

$$
g _ { y } ( y ) f ( y , z ) = 0 .
$$

This defines a “hidden” submanifold of the cylinder,on which all solutions of $( 1 . 9 \mathrm { a } , \mathbf { b } )$ must lie (see Fig.1.1b). We stilldo not know how, with increasing $x$ ， the variable $z$ changes. This is obtained by differentiating(1.9c) with respect to $_ x$ ： $g _ { y y } ( f , f ) + g _ { y } f _ { y } f + g _ { y } f _ { z } z ^ { \prime } = 0$ . From this relation we can extract

$$
z ^ { \prime } = - ( g _ { y } f _ { z } ) ^ { - 1 } \left( g _ { y y } ( f , f ) + g _ { y } f _ { y } f \right)
$$

if

$$
g _ { y } ( y ) f _ { z } ( y , z ) \qquad { \mathrm { i s ~ i n v e r t i b l e . } }
$$

![](images/d8b1c8fd022bf17e511c5a0378a7f3ed9530fd69deaf0cd4bae25b921352fb2b.jpg)  
Fig.1.la. The vector field (1.9a,d)

![](images/4971b822e2c9e2e5cdd0bd6afb0fd938d17b898a7b2dd4d99c60e73cde5c6d8e.jpg)  
Fig.1.1b. The hidden submanifold

We have been able to transform the above differential-algebraic equation (1.9a,b) into an ordinary differential system (1.9a,d) by two analytic differentiations of the constraint (1.9c). This fact is used for the following definition, which has been developed in several papers (Gear & Petzold 1983,1984; Gear, Gupta & Leimkuhler 1985,Gear 1990, Campbell & Gear 1995).

Definition 1.2. Equation (1.1) has differentiation index $d i = m$ if $m$ is the minimal number of analytical differentiations

$$
F ( u ^ { \prime } , u ) = 0 , \ \frac { d F ( u ^ { \prime } , u ) } { d x } = 0 \ , \ \ldots \ , \ \frac { d ^ { m } F ( u ^ { \prime } , u ) } { d x ^ { m } } = 0
$$

such that equations (1.11) allow us to extract by algebraic manipulations an explicit ordinary differential system $u ^ { \prime } = \varphi ( u )$ (which is called the “underlying $O D E ^ { , } )$ .

Examples. Linear Equations with Constant Coefficients. The following problem

$$
\begin{array} { r l r l } { z _ { 2 } ^ { \prime } + z _ { 1 } = \delta _ { 1 } } & { { } \quad } & { z _ { 2 } ^ { \prime \prime } + z _ { 1 } ^ { \prime } = \delta _ { 1 } ^ { \prime } } \\ { z _ { 3 } ^ { \prime } + z _ { 2 } = \delta _ { 2 } } & { { } \Rightarrow } & { z _ { 3 } ^ { \prime \prime \prime } + z _ { 2 } ^ { \prime \prime } = \delta _ { 2 } ^ { \prime \prime } \quad } & { \Rightarrow } & { z _ { 1 } ^ { \prime } = \delta _ { 1 } ^ { \prime } - \delta _ { 2 } ^ { \prime \prime } + \delta _ { 3 } ^ { \prime \prime \prime } } \\ { z _ { 3 } = \delta _ { 3 } } & { { } \quad } & { z _ { 3 } ^ { \prime \prime \prime } = \delta _ { 3 } ^ { \prime \prime \prime } } \end{array}
$$

can be seen to have differentiation index 3. For linear equations with constant coefficients the differentiation index and the index of nilpotency are therefore the same.

Systems of Index $l$ . The differential-algebraic systems already seen in Chapter VI

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) } \end{array}
$$

have no $z ^ { \prime }$ . We therefore differentiate (1.13b) to obtain

$$
z ^ { \prime } = - g _ { z } ^ { - 1 } ( y , z ) g _ { y } ( y , z ) f ( y , z )
$$

which is possible if $g _ { z }$ is invertible in a neighbourhood of the solution. The problem (1.13a,b), for invertible $g _ { z }$ , is thus of differentiation index 1.

Systems of Index 2. In the system (see example (1.9))

$$
\begin{array} { c } { { y ^ { \prime } = f \bigl ( y , z \bigr ) } } \\ { { 0 = g \bigl ( y \bigr ) , } } \end{array}
$$

where the variable $z$ is absent in the algebraic constraint, we obtain by differentiation of(1.14b) the “hidden constraint"

$$
0 = g _ { y } ( y ) f ( y , z ) .
$$

If (1.10) is satisfied in a neighbourhood of the solution, then (1.14a) and (1.14c) constitute an index 1 problem. Differentiation of (1.14c) yields the missing differential equation for $z$ ,so that the problem(1.14a,b) is of differentiation index 2. If the initial values satisfy $0 = g ( y _ { 0 } )$ and $0 = g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } )$ , we call them consistent. In this case,and only in this case,the system (1.14a,b) possesses a (locally) unique solution.

System (1.14a,b) is a representative of the larger class of problems of type (1.13a,b) with singular $g _ { z }$ . If we assume that $g _ { z }$ has constant rank in a neighbourhood of the solution, we can eliminate certain algebraic variables from $0 = g ( y , z )$ until the system is of the form (1.14). This can be done as follows: from the con-stant rank assumption it follows that either there exists a component of $g$ such that $\partial g _ { i } / \partial z _ { 1 } \neq 0$ locally, or $\partial g / \partial z _ { 1 }$ vanishes identically so that $g$ is already independent of $z _ { 1 }$ . In the first case we can express $z _ { 1 }$ as a function of $y$ and the remaining components of $z$ ，and then we can eliminate $z _ { 1 }$ from the system. Repeating this procedure with $z _ { 2 } , z _ { 3 }$ , etc.,will lead to a system of the form (1.14). This transformation does not change the index. Moreover, most numerical methods are invariant under this transformation. Therefore, theoretical work done for systems of the form (1.14) will also be valid for more general problems.

Systems of Index 3.Problems of the form

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { z ^ { \prime } = k ( y , z , u ) } } \\ { { 0 = g ( y ) } } \end{array}
$$

are of differentiation index 3, if

$$
g _ { y } f _ { z } k _ { u } \mathrm { i s \ i n v e r t i b l e }
$$

in a neighbourhood of the solution. Differentiating (1.15c) twice gives

$$
\begin{array} { l } { 0 = g _ { y } f } \\ { 0 = g _ { y y } ( f , f ) + g _ { y } f _ { y } f + g _ { y } f _ { z } k . } \end{array}
$$

Equations (1.15a,b),(1.15e) together with Condition (1.16) are of the index 1 form (1.13a,b). Consistent inital values must satisfy the three conditions (1.15c,d,e).

An extensive study of the solution space of general differential-algebraic systems is done by Griepentrog & März (1986),März (1989,1990). These authors try to avoid assumptions on the smoothness on the problem as far as possible and re-place the above differentiations by a careful study of suitable projections depending only on the first derivatives of $F$ .

# Differential Equations on Manifolds

In the language of differentiable manifolds,whose use in DAE theory was urged by Rheinboldt (1984),a constraint (such as $g ( y ) = 0$ )represents a manifold, which we denote by

$$
\mathcal { M } = \{ y \in \mathbb { R } ^ { n } \mid g ( y ) = 0 \} .
$$

We assume that $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ (with $m < n \mathrm { ~ . ~ }$ )is a sufficiently differentiable function whose Jacobian $g _ { y } ( y )$ has full rank for $y \in M$ . For a fixed $y \in \mathcal { M }$ we denote by

$$
T _ { y } { \mathcal { M } } = \{ v \in \mathbb { R } ^ { n } \mid g _ { y } ( y ) v = 0 \} ,
$$

the tangent space of $\mathcal { M }$ at $y$ . This is a linear space and has the same dimension $n - m$ as the manifold $\mathcal { M }$

![](images/a05449e58134f1bab72e7577852de2caf7a02d4360e8f679e754fa5c26b2628c.jpg)  
Fig.1.2. A manifold with a tangent vector field, a chart, and a solution curve

A vector field on $\mathcal { M }$ is a mapping $v : \mathcal { M } \to \mathbb { R } ^ { n }$ , which satisfies $v ( y ) \in T _ { y } \mathcal { M }$ for all $y \in M$ . For such a vector field we call

$$
y ^ { \prime } = v ( y ) , \qquad y \in { \mathcal { M } }
$$

a differential equation on the manifold $\mathcal { M }$ . Differentiation on an $\left( n { - } m \right)$ -dimensional manifold is described by so-called charts $\varphi _ { i } : U _ { i } \to E _ { i }$ ,where the $U _ { i }$ cover the manifold $\mathcal { M }$ and the $E _ { \imath }$ are open subsets of $\mathbb { R } ^ { n - m }$ (Fig.1.2; see also Lang (1962), Chap.II and Abraham, Marsden & Ratiu (1983), Chap.III). The local theory of ordinary differential equations can be extended to vector fields on manifolds in a straightforward manner:

Project the vectors $v ( y )$ onto $E _ { i }$ via a chart $\varphi _ { i }$ by multiplying $v ( y )$ with the Jacobian of $\varphi _ { \imath }$ at $y$ . Then apply standard results to the pro-jected vector field in $\mathbb { R } ^ { n - m }$ ,and pull the solution back to $\mathcal { M }$

(see Fig.1.2). The local existence of solutions of (1.19) can be shown in this way. The obtained solution is independent of the chosen chart. Where the solution leaves the domain of a chart, the integration must be continued via another one.

Index 2 Problems. Consider the system $_ { ( 1 . 1 4 a , b ) }$ and suppose that (1.10) is satisfied. This condition implies that $g _ { y } ( y )$ is of full rank,so that (1.17) is a smooth manifold. Moreover, the Implicit Function Theorem implies that the differentiated constraint (1.14c） can be solved for $z$ (in a neighbourhood of the solution), i.e., there exists a smooth function $h ( y )$ such that

$$
g _ { y } ( y ) f ( y , z ) = 0 \qquad \Longleftrightarrow \qquad z = h ( y ) .
$$

Inserting this relation into (1.10a) yields

$$
y ^ { \prime } = f { \big ( } y , h ( y ) { \big ) } , \qquad y \in { \mathcal { M } }
$$

which is a differential equation on the manifold(1.17), because $f ( y , h ( y ) ) \in T _ { y } \mathcal { M }$ by (1.20). The differential equation (1.21) is equivalent to (1.14a,b).

Example. The manifold $M$ for problem (1.9） is onedimensional (circle). In points,where $y _ { 1 } \neq \pm 1$ ，we can solve (1.9b) to obtain locally $y _ { 2 } = \pm { \sqrt { 1 - y _ { 1 } ^ { 2 } } }$ . The map $( y _ { 1 } , y _ { 2 } ) \mapsto y _ { 1 }$ consitutes a chart $\varphi$ , which is bijective in a neighbourhood of the considered point. Inserting $z$ from $( 1 . 9 \mathrm { c } )$ and the above $y _ { 2 }$ into (1.9a), yields an equation $y _ { 1 } ^ { \prime } = G ( y _ { 1 } )$ ， which is the projected vector field in $\mathbb { R } ^ { 1 }$ .

![](images/921403f36c4fc4059542cbc9c2c69b3aea22d84744aaf445db8d4d07c067765c.jpg)

Index 3 Problems.For the system $( 1 . 1 5 \mathrm { a } , \mathsf { b } , \mathsf { c } )$ the solutions lie on the manifold

$$
\mathcal { M } = \{ ( y , z ) ~ \vert ~ g ( y ) = 0 , ~ g _ { y } ( y ) f ( y , z ) = 0 \} .
$$

The assumption (1.16) implies that $g _ { y } ( y )$ and $g _ { y } ( y ) f _ { z } ( y , z )$ have full rank, so that $\mathcal { M }$ is a manifold. Its tangent space at $( y , z )$ is

$$
\begin{array} { r } { T _ { ( y , z ) } \mathcal { M } = \{ ( v , w ) | g _ { y } ( y ) v = 0 , g _ { y y } ( y ) \big ( f ( y , z ) , v \big ) \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } } \\ { + g _ { y } ( y ) \big ( f _ { y } ( y , z ) v + f _ { z } ( y , z ) w \big ) = 0 \} . } \end{array}
$$

Solving Eq.(1.15e) for $u$ and inserting the result into (1.15b) yields a differential equation on the manifold $\mathcal { M }$ . Because of (1.15d,e), the obtained vector field lies in the tangent space $T _ { ( y , z ) } { \mathcal { M } }$ for all $( y , z ) \in M$

# The Perturbation Index

Now fills thy sleep with perturbations. (The Ghost of Anne in Shakespeare's Richard III,act $\mathbb { V } _ { \mathfrak { s } }$ sc.I)

A second concept of index,due to HLR89 1, interprets the index as a measure of sensitivity of the solutions with respect to perturbations of the given problem.

Definition 1.3. Equation (1.1） has perturbation index $p i = n$ along a solution $u ( x )$ on $[ 0 , { \overline { { x } } } ]$ ,if $m$ is the smallest integer such that, for all functions $\widehat { \mathcal { U } } \big ( \mathcal { X } \big )$ having a defect

$$
F ( \widehat { u } ^ { \prime } , \widehat { u } ) = \delta ( x ) ,
$$

there exists on $\left[ 0 , { \overline { { x } } } \right]$ an estimate

$$
\| \widehat { u } ( x ) - u ( x ) \| \leq C \Big ( \| \widehat { u } ( 0 ) - u ( 0 ) \| + \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ( \xi ) \| + . . . + \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ^ { ( m - 1 ) } ( \xi ) \| \Big )
$$

whenever the expression on the right-hand side is sufficiently small.

Remark. We deliberately do not write “Let ${ \widehat { u } } ( x )$ be the solution of $F ( \widehat { \mathcal { U } } ^ { \prime } , \widehat { \mathcal { U } } ) =$ $\delta ( x ) \ldots ^ { \mathfrak { n } }$ in this definition, because the existence of such a solulion ${ \widehat { u } } ( x )$ for an arbitrarily given $\displaystyle \delta ( x )$ is not assured. We start with $\widehat { u }$ and then compute $\delta$ as defect of (1.1).

Systems of Index 1. For the computation of the perturbation index of (1.13a,b) we consider the perturbed system

$$
\begin{array} { r } { \widehat { \mathcal { Y } } ^ { \prime } = f ( \widehat { \mathcal { Y } } , \widehat { z } ) + \delta _ { 1 } ( x ) } \\ { 0 = g ( \widehat { \mathcal { Y } } , \widehat { z } ) + \delta _ { 2 } ( x ) . } \end{array}
$$

The essential observation is that the difference $\widehat { z } \sim z$ can be estimated with the help of the Implicit Function Theorem, without any differentiation of the equation. Since $g _ { z }$ is invertible by hypothesis, this theorem gives from (1.26b) compared to (1.13b)

$$
\| \widehat { \widetilde { \widetilde { \mathbf { \Gamma } } } } ( x ) - z ( x ) \| \leq C _ { 1 } \big ( \| \widehat { \widetilde { \boldsymbol { y } } } ( x ) - \boldsymbol { y } ( x ) \| + \| \delta _ { 2 } ( x ) \| \big )
$$

as long as the right-hand side of (1.27) is sufficiently small. We now subtract (1.26a) from (1.13a), integrate from 0 to $\boldsymbol { x }$ ,use a Lipschitz condition for $f$ and the above estimate for ${ \widehat { z } } ( x ) - z ( x )$ . This gives for $e ( x ) = \| { \widehat { y } } ( x ) - y ( x ) \|$

$$
e ( x ) \leq e ( 0 ) + C _ { 2 } \int _ { 0 } ^ { r } e ( t ) d t + C _ { 3 } \int _ { 0 } ^ { x } \| \delta _ { 2 } ( t ) \| d t + \Big \| \int _ { 0 } ^ { \varepsilon } \delta _ { 1 } ( t ) d t \Big \| .
$$

In this estimate the norm is inside the integral for $\delta _ { 2 }$ , but outside the integral for $\delta _ { 1 }$ This is due to the fact that perturbations of the algebraic equation(1.13b) are more

serious than perturbations of the differential equation (1.13a). We finally apply Gronwall's Lemma (Exercise I.10.2) to obtain on a bounded interval $[ 0 , { \overline { { x } } } ]$

$$
\begin{array} { l l l } { \displaystyle \| \widehat { y } ( x ) - y ( x ) \| \leq C _ { 4 } \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \int _ { 0 } ^ { x } \| \delta _ { 2 } ( t ) \| d t + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \Big \| \int _ { 0 } ^ { \xi } \delta _ { 1 } ( t ) d t \Big \| \Big ) } \\ { \displaystyle \leq C _ { 5 } \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta _ { 2 } ( \xi ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta _ { 1 } ( \xi ) \| \Big ) . } \end{array}
$$

This inequality,together with (1.27),shows that the perturbation index of the problem is 1.

Systems of Index 2. We consider the following perturbation of system (1.14a,b)

$$
\begin{array} { c } { { \widetilde { y } ^ { \prime } = f ( \widehat { y } , \widehat { z } ) + \delta ( x ) } } \\ { { 0 = g ( \widehat { y } ) + \theta ( x ) . } } \end{array}
$$

Differentiation of (1.28b) gives

$$
0 = g _ { y } ( \widehat { y } ) f ( \widehat { y } , \widehat { z } ) + g _ { y } ( \widehat { y } ) \delta ( x ) + \theta ^ { \prime } ( x ) .
$$

Under the assumption (1.1O) we can use the estimates of the index 1 case (with $\delta _ { 2 } ( x )$ replaced by $g _ { y } \big ( \widehat { y } ( x ) \big ) \delta ( x ) + \theta ^ { \prime } ( x ) )$ to obtain

$$
\begin{array} { r l } & { \| \widehat { y } ( x ) - y ( x ) \| \leq C \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \int _ { 0 } ^ { x } \big ( \| \delta ( \xi ) \| + \| \theta ^ { \prime } ( \xi ) \| \big ) d \xi \Big ) } \\ & { \| \widehat { z } ( x ) - z ( x ) \| \leq C \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ( \xi ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \theta ^ { \prime } ( \xi ) \| \Big ) . } \end{array}
$$

Since these estimates depend on the first derivative of $\theta$ , the perturbation index of this problem is 2. A sharper estimate for the $y$ -component is given in Exercise 6.

Example. Fig.1.3 presents an illustration for the index 2 problem (1.9a,b). Small perturbations of $g ( y )$ ，once discontinuous in the first derivative (left),the other of oscillatory type (right),results in discontinuities or violent oscillations of $z$ ， respectively.

The above examples might give the impression that the differentiation index and the perturbation index are always equal. The following counter-examples show that this is not true.

Counterexamples. The first counterexample of type $M ( y ) y ^ { \prime } = f ( y )$ is given by Lubich (1989):

$$
\begin{array} { r l r } { y _ { 1 } ^ { \prime } - y _ { 3 } y _ { 2 } ^ { \prime } + y _ { 2 } y _ { 3 } ^ { \prime } = 0 } & { } & { \widehat { y } _ { 1 } ^ { \prime } - \widehat { y } _ { 3 } \widehat { y } _ { 2 } ^ { \prime } + \widehat { y } _ { 2 } \widehat { y } _ { 3 } ^ { \prime } = 0 \quad \quad } \\ { y _ { 2 } = 0 } & { } & { \widehat { y } _ { 2 } = \varepsilon \sin \omega x } \\ { y _ { 3 } = 0 } & { } & { \widehat { y } _ { 3 } = \varepsilon \cos \omega x } \end{array}
$$

with $y _ { \ i } ( 0 ) = 0 \ ( i = 1 , 2 , 3 )$ . Inserting $\widehat { y } _ { 2 } = \varepsilon \sin \omega x$ and $\widehat { y } _ { 3 } = \varepsilon \cos \omega x$ into the first equation gives $\widehat { y } _ { 1 } ^ { \prime } = \varepsilon ^ { 2 } \omega$ which makes, for $\varepsilon$ fixed and $\omega  \infty$ ,an estimate

![](images/2c58003ff96d5ed7c11d372fb556371c627ee360c7628512f5d6257c0bcc1cdc.jpg)  
Fig.1.3.Perturbations of an index 2 problem

(1.25)with $m \simeq 1$ impossible. However, for $m \simeq 2$ the estimate (1.25) is clearly satisfied. This problem,which is obviously of differentiation index 1,is thus of perturbation index 2.

It was believed for some time (see the first edition, p.479),that the differenti-ation and perturbation indices can difer at most by 1. The following example, due to Campbell & Gear (1995), was therefore a big surprise:

$$
y _ { m } N y ^ { \prime } + y = 0 ,
$$

where $N$ is a $m \times m$ upper triangular nilpotent Jordan block. Since the last row of $N$ is zero, we have $y _ { m } = 0$ ,and the differentiation index is 1. On the other hand, adding a perturbation makes $y _ { m }$ different from zero. This is the reason why the perturbation index of(1.32) is $m$

# Control Problems

Many problems of control theory lead to ordinary differential equations of the form $y \prime = f ( y , u )$ ，where $u$ represents a set of controls. Similar as in example (1.9) above, these controls must be applied so that the solution satisfies some constraints $0 = g ( y , u )$ . For numerical examples of such control problems we refer to Brenan (1983)(space shutle simulation) and Brenan, Campbell & Petzold (1989).

Optimal Control Problems are differential equations $y \prime = f ( y , u )$ formulated in such a way that the control $u ( x )$ has to minimize some cost functional. The Euler-- Lagrange equation then often becomes a differential-algebraic system (Pontryagin, Boltyanskij,Gamkrelidze & Mishchenko 1961,Athans & Falb 1966,Campbell 1982).We demonstrate this on the problem

$$
y ^ { \prime } = f ( y , u ) , \qquad y ( 0 ) = y _ { 0 }
$$

with cost functional

$$
J ( u ) = \int _ { 0 } ^ { 1 } \varphi \big ( y ( x ) , u ( x ) \big ) d x .
$$

For a given function $u ( x )$ the solution $y ( x )$ is determined by (1.33a). In order to find conditions for $u ( x )$ which minimize $\boldsymbol { J } ( u )$ of (1.33b), we consider the perturbed control $u ( x ) + \varepsilon \delta u ( x )$ where $\delta u ( x )$ is an arbitrary function and $\varepsilon$ a small number. To this control there corresponds a solution $y ( x ) + \varepsilon \delta y ( x ) + { \mathcal { O } } ( \varepsilon ^ { 2 } )$ of (1.33a); hence (by comparing powers of $\varepsilon$ ）

$$
\delta y ^ { \prime } ( x ) = f _ { y } ( x ) \delta y ( x ) + f _ { u } ( x ) \delta u ( x ) , \qquad \delta y ( 0 ) = 0 ,
$$

where, as usual, $f _ { y } ( x ) = f _ { y } ( y ( x ) , u ( x ) )$ , etc. Linearization of (1.33b) shows that

$$
J ( u + \varepsilon \delta u ) - J ( u ) = \varepsilon \int _ { 0 } ^ { 1 } \left( \varphi _ { y } ( x ) \delta y ( x ) + \varphi _ { u } ( x ) \delta u ( x ) \right) d x + \mathcal O ( \varepsilon ^ { 2 } )
$$

so that

$$
\int _ { 0 } ^ { 1 } \left( \varphi _ { y } ( x ) \delta y ( x ) + \varphi _ { u } ( x ) \delta u ( x ) \right) d x = 0
$$

is a necessary condition for $u ( x )$ to be an optimal solution of our problem. In order to express $\delta y$ in terms of $\delta u$ in (1.35),we introduce the adjoint differential equation

$$
\boldsymbol { v } ^ { \prime } = - f _ { y } ( \boldsymbol { x } ) ^ { \mathcal { T } } \boldsymbol { v } - \varphi _ { y } ( \boldsymbol { x } ) ^ { \mathcal { T } } , \qquad \boldsymbol { v } ( 1 ) = 0
$$

with inhomogeneity $\varphi _ { y } ( x ) ^ { T }$ . Hence we have (see Exercise 7)

$$
\int _ { 0 } ^ { 1 } \varphi _ { y } ( x ) \delta y ( x ) d x = \int _ { 0 } ^ { 1 } v ^ { T } ( x ) f _ { u } ( x ) \delta u ( x ) d x .
$$

Inserted into (1.35) this gives the necessary condition

$$
\int _ { 0 } ^ { 1 } \Big ( \boldsymbol { v } ^ { T } ( \boldsymbol { x } ) f _ { u } ( \boldsymbol { x } ) + \varphi _ { u } ( \boldsymbol { x } ) \Big ) \delta \boldsymbol { u } ( \boldsymbol { x } ) d \boldsymbol { x } = 0 .
$$

Since this relation has to be satisfied for all $\delta u$ we obtain the necessary relation $v ^ { T } ( x ) f _ { u } ( x ) + \varphi _ { u } ( x ) = 0$ by the so-called “fundamental lemma of variational calculus".

In summary, we have proved that a solution of the above optimal control problem has to satisfy the system

$$
\begin{array} { r l r l } & { \boldsymbol { y } ^ { \prime } = f ( \boldsymbol { y } , \boldsymbol { u } ) , } & & { \boldsymbol { y } ( 0 ) = \boldsymbol { y } _ { 0 } } \\ & { \boldsymbol { v } ^ { \prime } = - f _ { y } ( \boldsymbol { y } , \boldsymbol { u } ) ^ { T } \boldsymbol { v } - \varphi _ { y } ( \boldsymbol { y } , \boldsymbol { u } ) ^ { T } , } & & { \boldsymbol { v } ( 1 ) = 0 } \\ & { 0 = \boldsymbol { v } ^ { T } f _ { u } ( \boldsymbol { y } , \boldsymbol { u } ) + \varphi _ { u } ( \boldsymbol { y } , \boldsymbol { u } ) . } \end{array}
$$

This is a boundary value differential-algebraic problem. It can also be obtained directly from the Pontryagin minimum principle (see Pontryagin et al. 1961, Athans & Falb 1966).

Differentiation of the algebraic relation in (1.39) shows that the system (1.39) has index 1 if the matrix

$$
\sum _ { i = 1 } ^ { n } v _ { i } \frac { \partial ^ { 2 } f _ { \imath } } { \partial u ^ { 2 } } \left( y , u \right) + \frac { \partial ^ { 2 } \varphi } { \partial u ^ { 2 } } \left( y , u \right)
$$

is invertible along the solution.A situation where the system (1.39) has index 3 is presented in Exercise 8. An index 5 problem of this type is given in “Example $3 . 1 ^ { \mathfrak { s } }$ of Clark (1988). Other control problems with a large index are discussed in Campbell (1995).

# Mechanical Systems

... berechnen wir $T , V , L$ . Mehr brauchen wir von der Geometrie und Mechanik unseres Systems nicht zu wissen. Alles üibrige besorgt ohne unser Zutun der Formalismus von LAGRANGE.

(Sommerfeld 1942, $\ S 3 5 \mathrm { \Omega }$

An interesting class of differential-algebraic systems appears in mechanical modeling of constrained systems. A choice method for deriving the equations of mo-tion of mechanical systems is the Lagrange-Hamilton principle, whose long history goes back to merely theological ideas of Leibniz and Maupertuis. Let $q _ { 1 } , \ldots , q _ { n }$ be position coordinates of a system and $u _ { i } = \dot { q } _ { i }$ the velocities. Suppose a function $L ( q , \dot { q } )$ is given; then the Euler equations of the variational problem

$$
\int _ { t _ { 1 } } ^ { t _ { 2 } } L ( q , \dot { q } ) d t = \operatorname* { m i n } !
$$

are given by

$$
{ \frac { d } { d t } } \left( { \frac { \partial L } { \partial { \dot { q } } _ { k } } } \right) - { \frac { \partial L } { \partial q _ { k } } } = 0 , \qquad k = 1 , \ldots , n
$$

or

$$
\sum _ { \ell = 1 } ^ { n } L _ { \dot { q } _ { k } \dot { q } _ { \ell } } \ddot { q } _ { \ell } = L _ { q _ { k } } - \sum _ { \ell = 1 } ^ { n } L _ { \dot { q } _ { k } q _ { \ell } } \dot { q } _ { \ell } .
$$

The great discovery of Lagrange (1788) is that for $L = T - U$ ，where $T$ is the kinetic energy and $U$ the potential energy, the differential equations (1.43) describe the movement of the corresponding “conservative system". For a proof and various generalizations, consult any book on mechanics e.g., Sommerfeld (1942)，vol.I, $\ S \ S 3 3 - 3 7$ , or Arnol'd (1979), part II.

Example 1. For the mathematical pendulum of length $\ell$ we choose as position coordinate the angle $\theta = q _ { 1 }$ such that $T = m \ell ^ { 2 } { \dot { \theta } } ^ { 2 } / 2$ and $U = - \ell m g \cos { \theta }$ . Then (1.43) becomes $\ell { \ddot { \theta } } = - g \sin \theta$ , the well-known pendulum equation.

Movement with Constraints. Suppose now that we have some constraints $g _ { 1 } ( q ) =$ $0 ; \ldots , g _ { m } ( q ) = 0$ on our movement. Another great idea of Lagrange is to vary the “Lagrange function” as follows in this case

$$
L = T - U - \lambda _ { 1 } g _ { 1 } ( q ) - . . . - \lambda _ { m } g _ { m } ( q )
$$

where the “Lagrange multipliers” $\lambda _ { i }$ are appended to the coordinates. The important fact is that, since $L$ is independent of $\bar { \dot { \lambda } } _ { i }$ , the equation (1.43), for the derivatives with respect to $\lambda _ { k }$ , just becomes $0 = g _ { k } ( q )$ , the desired side conditions.

Example 2. We now describe the pendulum in Cartesian coordinates $x , y$ with constraint $x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } = 0$ . This gives for (1.44)

$$
L = { \frac { m } { 2 } } { \bigl ( } { \dot { x } } ^ { 2 } + { \dot { y } } ^ { 2 } { \bigr ) } - m g y - \lambda ( x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } )
$$

and (1.43) becomes

$$
\begin{array} { c } { { m \ddot { x } = - 2 x \lambda } } \\ { { m \ddot { y } = - m g - 2 y \lambda } } \\ { { 0 = x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } . } } \end{array}
$$

In this example the physical meaning of $\lambda$ is the tension in the rod which maintains the mass point on the desired orbit.

The general form of a constrained mechanical system (1.43) is in vector notation (after replacing dots by primes)

$$
\begin{array} { c } { q ^ { \prime } = u } \\ { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } \\ { 0 = g ( q ) } \end{array}
$$

where $M ( q ) = T _ { \dot { q } \dot { q } } = T _ { u u }$ is a positive definite matrix, $G ( q ) = \partial g / \partial q$ and $q =$ $( q _ { 1 } , \ldots , q _ { n } ) ^ { T }$ ， $\boldsymbol { u } \equiv ( \dot { q } _ { 1 } , \dots , \dot { q } _ { n } ) ^ { T }$ ， $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { T }$ . Various formulations are possible for such a problem, each of which leads to a different numerical approach.

Index 3 Formulation (position level, descriptor form). If we formally multiply (1.46b) by $M ^ { - 1 }$ ,the system (1.46) becomes of the form (1.15) with $( q , u , \lambda )$ in the roles of $( y , z , u )$ . The condition (1.16), written out for (1.46), is

$$
G M ^ { - 1 } G ^ { T } \qquad \mathrm { i s ~ i n v e r t i b l e } .
$$

This is satisfied, if the constraints (1.46c) are independent, i.e., if the rows of the matrix $G$ are linearly independent. Under this assumption, the system (1.46a,b,c) is thus an index 3 problem.

Index 2 Formulation (velocity level). Differentiation of (1.46c) gives

$$
0 = G ( q ) u .
$$

If we replace (1.46c) by (1.46d) we obtain a system of the form (1.14a,b) with $( q , u )$ in the role of $y$ and $\lambda$ that of $z$ ．One verifies that Condition (1.10） is equivalent to (1.47), so that $( 1 . 4 6 \mathsf { a } , \mathsf { b } , \mathsf { d } )$ represents a problem of index 2.

Index 1 Formulation (acceleration level). If we differentiate twice the constraint (1.46c), the resulting equation together with (1.46b) yield

$$
\left( \begin{array} { c c } { { M ( q ) } } & { { G ^ { T } ( q ) } } \\ { { G ( q ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { u ^ { \prime } } } \\ { { \lambda } } \end{array} \right) = \left( \begin{array} { c } { { f ( q , u ) } } \\ { { - g _ { q q } ( q ) ( u , u ) } } \end{array} \right) .
$$

This allows us to express $u ^ { \prime }$ and $\lambda$ as functions of $q , u$ , provided that the matrix in (1.46e) is invertible. Hence,(1.46a,e) consitute an index 1 problem. The assumption on the matrix in Eq.(1.46e) is weaker than (1.47),because $M ( q )$ need not be regular.

All these formulations are mathematically equivalent,if the initial values are consistent, i.e., if (1.46c,d,e) are satisfied. However, if for example the index 2 system (1.46a,b,d) is integrated numerically, the constraints of the original problem will no longer be exactly satisfied. For this reason Gear, Gupta & Leimkuhler (1985)introduced another index 2 formulation("... an interesting way of reducing the problem to index two and adding variables so that the constraint continues to be satisfied".).

GGL Formulation. The idea is to add the constraint (1.46d) to the original system and to introduce an additional Lagrange multiplier $\mu$ in (1.46a). For the sake of symmetry we also multiply (1.46a) by $M ( q )$ , so that the whole system becomes

$$
\begin{array} { c } { { M ( q ) q ^ { \prime } = M ( q ) u - G ^ { T } ( q ) \mu } } \\ { { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) } } \\ { { 0 = G ( q ) u . } } \end{array}
$$

Here the differential variables are $( q , u )$ and the algebraic variables are $( \mu , \lambda )$ . System (1.48) is of the form (1.14a,b) and the index 2 assumption is satisfied if (1.47) holds.

A concrete mechanical system is described in detail, together with numerical results for all the above formulations, in Sect. VI.7.

# Exercises

1. Prove that the initial value problem

$$
B u ^ { \prime } + A u = 0 , \qquad u ( 0 ) = u _ { 0 }
$$

has a unique solution if and only if the matrix pencil $A + \lambda B$ is regular.

Hint for the "only if" part. If $\mathscr { n }$ is the dimension of $u$ , choose arbitrarily $n + 1$ distinct $\lambda _ { i }$ and vectors $\textstyle v _ { \imath } \neq 0$ satisfying $( A + \lambda _ { \iota } B ) v _ { \iota } = 0$ . Then take a linear combination, such that $\sum { \alpha _ { \ i } v _ { \ i } } = 0$ ,but $\sum \alpha _ { \ i } e ^ { \lambda _ { \ i } x } v _ { i } \not \equiv 0$

2. (Stewart 1972). Let $A + \lambda B$ be a regular matrix pencil. Show that there exist unitary matrices $Q$ and $Z$ such that

$$
\begin{array} { r } { Q A Z = \left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) , \qquad Q B Z = \left( \begin{array} { c c } { B _ { 1 1 } } & { B _ { 1 2 } } \\ { 0 } & { B _ { 2 2 } } \end{array} \right) } \end{array}
$$

are both triangular. Further, the diagonal elements of $A _ { 2 2 }$ and $B _ { 1 1 }$ are all 1, those of $B _ { 2 2 }$ are all 0.

Hint (Compare with the Schur decomposition of Theorem I.12.1). Let $\lambda _ { 1 }$ be a zero of $\operatorname* { d e t } ( A + \lambda B )$ and $v _ { 1 } \neq 0$ be such that $( A + \lambda _ { 1 } B ) v _ { 1 } = 0$ . Verify that $B v _ { 1 } \neq 0$ and that

$$
A Z _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { - \lambda _ { 1 } } } & { { \ast } } \\ { { 0 } } & { { \widetilde { A } } } \end{array} \right) , \qquad B Z _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { 1 } } & { { \ast } } \\ { { 0 } } & { { \widetilde { B } } } \end{array} \right)
$$

where $Q _ { 1 } , Z _ { 1 }$ are unitary matrices whose first columns are $B v _ { 1 }$ and $v _ { 1 }$ ,respectively. The matrix pencil $\widetilde { A } + \lambda \widetilde { B }$ is again regular and this procedure can be continued until $\operatorname* { d e t } ( \tilde { A } + \lambda \tilde { B } ) = C o n s t$ which implies that det $\widetilde { B } = 0$ In this case we take a vector $v _ { 2 } \not = 0$ such that $\widetilde { B } v _ { 2 } = 0$ and transform $\widetilde { A } + \lambda \widetilde { B }$ with unitary matrices $Q _ { 2 } , Z _ { 2 }$ ， whose first columns are $\stackrel { \sim } { A } v _ { 2 }$ and $v _ { 2 }$ ， respectively. For a practical computation of the decomposition (1.50) see Golub & Van Loan (1989), Sect. 7.7.

3. Under the assumptions of Exercise 2 show that there exist matrices $S$ and $T$ such that

$$
\begin{array} { r l } { ( I  } & { { } S } \\ { ( 0  } & { { } I ) ( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} ) ( I  } & { { } T ) = ( \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} ) , } \\ { ( \begin{array} { c c } { I } & { { } S } \\ { 0 } & { I } \end{array} ) ( \begin{array} { c c } { B _ { 1 1 } } & { B _ { 1 2 } } \\ { 0 } & { B _ { 2 2 } } \end{array} ) ( \begin{array} { c c } { I } & { { } T } \\ { 0 } & { I } \end{array} ) = ( \begin{array} { c c } { B _ { 1 1 } } & { 0 } \\ { 0 } & { B _ { 2 2 } } \end{array} ) . } \end{array}
$$

Hint. These matrices have to satisfy

$$
\begin{array} { r } { A _ { 1 1 } T + A _ { 1 2 } + S A _ { 2 2 } = 0 } \\ { B _ { 1 1 } T + B _ { 1 2 } + S B _ { 2 2 } = 0 } \end{array}
$$

and can be computed as follows: the first column of $T$ is obtained from(1.51b) because $\boldsymbol { B } _ { 1 1 }$ is invertible and the first column of $S B _ { 2 2 }$ vanishes; then the first column of $S$ is given by (1.51a) because $A _ { 2 2 }$ is invertible; the second column of $S B _ { 2 2 }$ is then known and we can compute the second column of $T$ from (1.51b), etc.

4.Prove that the index of nilpotency of a regular matrix pencil $A + \lambda B$ does not depend on the choice of $P$ and $Q$ in (1.3).

Hint. Consider two different decompositions of the form (1.3) and denote the matrices which appear by $C _ { 1 } , N _ { 1 }$ and $C _ { 2 } , N _ { 2 }$ , respectively. Show the existence of a regular matrix $T$ such that $N _ { 2 } = T ^ { - 1 } N _ { 1 } T$

5.Prove that the system $( \mathrm { V I } . 3 . 4 \mathrm { a } , \mathrm { b } )$ has index 2 (it is of the form (1.14a,b) and satisfies (1.10)). The full system (VI.3.4) has perturbation index $k$

6.(Arnold 1993). Consider the index 2 problem(1.14) and its perturbation(1.28). Prove that the difference $\Delta y ( x ) = \widehat { y } ( x ) - y ( x )$ satisfies

$$
\begin{array} { r l } & { \displaystyle \| \Delta y ( x ) \| \leq C \Big ( \| \Delta y ( 0 ) \| + \underset { 0 \leq \xi \leq x } { \operatorname* { m a x } } \Big ( \Big \| \int _ { 0 } ^ { \xi } P ( t ) \delta ( t ) d t \Big \| } \\ & { \qquad + \| \theta ( \xi ) \| + \big ( \| \delta ( \xi ) \| + \| \theta ^ { \prime } ( x ) \| \big ) ^ { 2 } \Big ) \Big ) } \end{array}
$$

with the projector $P ( t ) = I - \left( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \right) \left( y ( t ) , z ( t ) \right)$ ， provided that the right hand side is sufficiently small.

Hint. Linearize Eq.(1.29) around $( y , z )$ ，extract $\widehat { z } - z$ ， and insert it into the difference of (1.28a) and (1.14a). The term $\left( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \right) \left( y ( x ) , z ( x ) \right) \theta ^ { \prime } ( x )$ can be replaced by $\begin{array} { r } { \frac { d } { d x } \Big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \big ( y ( x ) , z ( x ) \big ) \theta ( x ) \Big ) + \mathcal { O } ( | | \theta ( x ) | | ) } \end{array}$ before integration.

7. For the linear initial value problem

$$
y ^ { \prime } = A ( x ) y + f ( x ) , \qquad y ( 0 ) = 0
$$

consider the adjoint problem

Prove that

$$
\begin{array} { c } { { \displaystyle v ^ { \prime } = - A ( x ) ^ { T } v - g ( x ) , \qquad v ( 1 ) = 0 . } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } g ( x ) ^ { T } y ( x ) d x = \int _ { 0 } ^ { 1 } v ( x ) ^ { T } f ( x ) d x . } } \end{array}
$$

8. Consider a linear optimal control problem with quadratic cost functional

$$
\begin{array} { c } { { y ^ { \prime } = A y + B u + f ( x ) , \qquad y ( 0 ) = y _ { 0 } } } \\ { { J ( u ) = \displaystyle { \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \left( y ( x ) ^ { T } C y ( x ) + u ( x ) ^ { T } D u ( x ) \right) d x } , } } \end{array}
$$

where $C$ and $D$ are assumed to be positive semi-definite.

a) Prove that $\boldsymbol { J } ( \boldsymbol { u } )$ is minimal if and only if

$$
\begin{array} { r l } & { y ^ { \prime } = A y + B u + f ( x ) , \qquad y ( 0 ) = y _ { 0 } } \\ & { v ^ { \prime } = - A ^ { T } v - C y , \qquad v ( 1 ) = 0 } \\ & { 0 = B ^ { T } v + D u . } \end{array}
$$

b) If $D$ is positive definite, then (1.52) has index 1.

c)If $D \approx 0$ and $B ^ { T } C B$ is positive definite, then (1.52) has index 3.

# VII.2 Index Reduction Methods

We have seen in Sect. VI.1 that the numerical treatment of problems of index 1, which are either in the half-explicit form(1.13) or in the form $M u ^ { \prime } = \varphi ( u )$ ,is not much more difficult than that of ordinary differential equations. For higher index problems the situation changes completely. This section is devoted to the study of several approaches that are all based on the idea of modifying the problem in such a way that the index is reduced.

# Index Reduction by Differentiation

The most apparent way of reducing the index is to differentiate repeatedly the algebraic constraints (see Definition 1.2). In general, it is recommended to differentiate until having obtained an index 1 problem. For example, the index 2 problem (1.14a,b) is replaced by (1.14a,c), or the constrained mechanical system (1.46a,b,c) by (1.46a,b,e). The resulting problem is then solved by the methods of Chapter VI.

We illustrate this approach at the “pendulum example"

$$
\begin{array} { c } { { x ^ { \prime } = u , \qquad u ^ { \prime } = - x \lambda } } \\ { { y ^ { \prime } = v , \qquad v ^ { \prime } = - 1 - y \lambda } } \\ { { 0 = x ^ { 2 } + y ^ { 2 } - 1 . } } \end{array}
$$

In this form it has index 3. Differentiating the algebraic constraint twice yields

$$
\begin{array} { l } { { 0 = x u + y v , } } \\ { { 0 = - \lambda ( x ^ { 2 } + y ^ { 2 } ) - y + u ^ { 2 } + v ^ { 2 } . } } \end{array}
$$

Equations (2.1a,b) together with(2.3) represent an index 1 problem. We can extract $\lambda$ from(2.3) and insert it into (2.1a,b)to get a differential equation for $x , y , u , v ,$ which can be solved by standard methods.

Drift-off Phenomenon. As an example we apply the code DOPRI5 to the index 1 problem(2.1a,b),(2.3) with initial values $x _ { 0 } = 1$ ， $y _ { 0 } = 0$ ， $u _ { 0 } = 0$ ， $v _ { 0 } = 0$ . We are interested, how well the constraints (2.1c) and (2.2) are preserved by the numerical solution. The result presented in Fig.2.1 shows that the error in the constraint (2.2) grows linearly, that in (2.1c) grows even quadratically. This phenomenon is explained as follows:

![](images/f052aa438cba3d426b8d7179d70c42a73a18079d1d1106160ed948deffa2f25f.jpg)  
Fig.2.1. Error in the constraints for DOPRI5 $\mathit { \Omega } ( A t o l = R t o l = 1 0 ^ { - 6 }$ ）

Consider a constrained mechanical system (see (1.46))

$$
\begin{array} { c } { q ^ { \prime } = u } \\ { { { \cal M } ( q ) u ^ { \prime } = f ( q , u ) - { \cal G } ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) . } } \end{array}
$$

Differentiating (2.4c) twice we get

$$
\left( \begin{array} { c c } { { M ( q ) } } & { { G ^ { T } ( q ) } } \\ { { G ( q ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { u ^ { \prime } } } \\ { { \lambda } } \end{array} \right) = \left( \begin{array} { c } { { f ( q , u ) } } \\ { { - q _ { q q } ( q ) ( u , u ) } } \end{array} \right)
$$

which, together with (2.4a),is the corresponding index 1 problem. The important observation is now that the index 1 problem possesses a solution for arbitrary initial values $q _ { 0 }$ and $u _ { 0 }$ . Due to the fact that the second derivative of $g ( q ( t ) )$ vanishes (this is a consequence of the lower relation of (2.5)), the solution of the index 1 problem satisfies

$$
\begin{array} { r l } & { g \big ( \boldsymbol { q } ( t ) \big ) = g \big ( \boldsymbol { q } _ { 0 } \big ) + ( t - t _ { 0 } ) G ( \boldsymbol { q } _ { 0 } ) \boldsymbol { u } _ { 0 } , } \\ & { G \big ( \boldsymbol { q } ( t ) \big ) \boldsymbol { u } ( t ) = G \big ( \boldsymbol { q } _ { 0 } \big ) \boldsymbol { u } _ { 0 } . } \end{array}
$$

Theorem 2.1. If we apply a pth order numerical method to the index $l$ problem $( 2 . 4 a )$ ，(2.5) with consistent initial values at $t _ { 0 } = 0$ ， then the numerical solution $\left( q _ { n } , u _ { n } \right)$ at time $t _ { n }$ satisfies $( f o r \ t _ { n } - t _ { 0 } \leq C o n s t )$

$$
\begin{array} { r } { \| g ( q _ { n } ) \| \leq h ^ { p } ( A t _ { n } + B t _ { n } ^ { 2 } ) , \qquad \| G ( q _ { n } ) u _ { n } \| \leq h ^ { p } C t _ { n } . } \end{array}
$$

The value $h$ represents the maximal step size used.

Proof. Denote by $q ( t , t _ { 0 } , q _ { 0 } , u _ { 0 } )$ the solution of the index 1 problem with initial value $( \boldsymbol { q } _ { 0 } , \boldsymbol { u } _ { 0 } )$ at $t = t _ { 0 }$ . Since the local error $q _ { \jmath + 1 } - q ( t _ { j + 1 } , t _ { \jmath } , q _ { \jmath } , u _ { \jmath } )$ is of size $\mathcal { O } ( h _ { \jmath } ^ { p + 1 } )$ (and similarly for the $u$ -component),itfollows from (2.6a) that

$$
\left. \left. g \big ( q ( t _ { n } , t _ { j + 1 } , q _ { j + 1 } , u _ { j + 1 } ) \big ) - g \big ( q ( t _ { n } , t _ { j } , q _ { j } , u _ { j } ) \big ) \right. \right. \leq h _ { j } ^ { p + 1 } \big ( A + 2 B ( t _ { n } - t _ { j + 1 } ) \big ) .
$$

Adding up these inequalities from $j = 0$ to $j = n - 1$ gives the desired bound for $g ( q _ { n } )$ ,because the initial values are consistent, i.e., $g ( q ( t _ { n } , t _ { 0 } , q _ { 0 } , u _ { 0 } ) ) = 0$ . The second estimate of Theorem 2.1 is proved in the same way. □

Baumgarte Stabilization. The historically first remedy for this drift-off is due to Baumgarte (1972). Instead of replacing the constraint (2.4c) by its second time derivative,he proposes to replace (2.4c) by the linear combination

$$
0 = \ddot { g } + 2 \alpha \dot { g } + \beta ^ { 2 } g ,
$$

where ${ \dot { g } } , { \ddot { g } }$ are time derivatives of (2.4c),i.e.,

$$
g \simeq g ( q ) , \qquad \dot { g } = G ( q ) u , \qquad \ddot { g } = g _ { q q } ( q ) ( u , u ) + G ( q ) \big ( f ( q , u ) - G ^ { T } ( q ) \lambda \big ) .
$$

Eq.(2.7) together with (2.4b) determines $u ^ { \prime }$ and $\lambda$ as functions of $( q , u )$ ,and the resulting differential equation can be solved numerically. The idea is now to choose the free parameters $\alpha$ and $\beta$ in such a way that (2.7) is an asymptotically stable differential equation, e.g., $\beta = \alpha$ and $\alpha > 0$ . Consequently, the functions $g ( q ( t ) )$ and $G ( \boldsymbol { q } ( t ) ) \boldsymbol { u } ( t )$ are exponentially decreasing, in contrast to (2.6). The difficulty of this approach lies in a good choice of $\alpha$ . For small values of $\alpha$ the damping will not be sufficiently strong,whereas for large $\alpha$ the resulting differential equation becomes stiff and explicit methods are no longer efficient. A careful investigation on the choice of $\alpha$ can be found in Ascher, Chin & Reich (1994).

# Stabilization by Projection

We shall now analyze another possibility for avoiding the instability of the preceding example, namely the repeated projection of the numerical solution onto the solution manifold.

Index 2 Problems. Consider the system (1.14a,b). Suppose that $( y _ { n - 1 } , z _ { n - 1 } )$ is an approximation to the solution at time $t _ { n - 1 }$ which satisfies $g ( y _ { n - 1 } ) = 0$ and $g _ { y } ( y _ { n - 1 } ) f ( y _ { n - 1 } , z _ { n - 1 } ) = 0$ . Applying a numerical one-step method (state space form method of Sect. VI.1) with these values to the index 1 system(1.14a,c) yields an approximation $\widetilde { y } _ { n } , \widetilde { z } _ { n }$ that, in general, does not satisfy the constraint (1.14b). A natural way of projecting the approximation $\widetilde { y } _ { n }$ to the solution manifold $\mathcal { M }$ of Eq.(1.17) is along the image of $f _ { z }$ (see also the projected Runge-Kutta methods of Sect. VII.4). We therefore define $y _ { n }$ as the solution of

$$
y - \widetilde { y } _ { n } = f _ { z } ( \widetilde { y } _ { n } , \widetilde { z } _ { n } ) \mu , \qquad g ( y ) = 0 ,
$$

and then we adjust $z _ { n }$ by solving the equation $g _ { y } ( y _ { n } ) f ( y _ { n } , z _ { n } ) = 0$ Applying simplified Newton iterations to the nonlinear system (2.8) requires the decomposition of the matrix

$$
\left( \begin{array} { c c } { { I } } & { { f _ { z } ( \widetilde { y } _ { n } , \widetilde { z } _ { n } ) } } \\ { { g _ { y } ( \widetilde { y } _ { n } ) } } & { { 0 } } \end{array} \right) .
$$

Block elimination shows that the invertibility of (2.9) is a consequence of (1.10), and that only the matrix $g _ { y } f _ { z }$ has to be decomposed. Such a decomposition is usually already available from the application of the numerical method, so that the projection (2.8) is very cheap.

It is now natural to ask, whether this projection procedure can distroy the convergence properties of the underlying method. For a $p$ th order one-step method the local error is of size $\mathcal { O } ( h ^ { p + 1 } )$ . Since the solution of (1.14a,c) passing through $\left( y _ { n - 1 } , z _ { n - 1 } \right)$ satisfies $g ( y ( t ) ) = 0$ , it holds $g ( \widetilde { y } _ { n } ) = \mathcal { O } ( h ^ { p + 1 } )$ . Hence, the solution of (2.8) satisfies $\mu = \mathcal { O } ( h ^ { p + 1 } )$ ， $y _ { n } - \widetilde { y } _ { n } = \mathcal { O } ( h ^ { p + 1 } )$ ,and $z _ { n } - \widetilde { z } _ { n } = \mathcal { O } ( h ^ { p + 1 } )$ By the Implicit Function Theorem this solution depends smoothly on $( \widetilde { y } _ { n } , \widetilde { z } _ { n } )$ ,s0 that the mapping $( y _ { n - 1 } , z _ { n - 1 } ) \mapsto ( y _ { n } , z _ { n } )$ represents a $p$ th order one-step method for (1.14a,c). Convergence of order $p$ thus follows from the standard theory (see Sects.VI.1 and II.3). This proof also applies to multistep methods.

Constrained Mechanical Systems. For the index 3 system $_ { ( 2 . 4 a , b , c ) }$ the situation is slightly more complex. We assume consistent values $\left( q _ { n - 1 } , u _ { n - 1 } , \lambda _ { n - 1 } \right)$ at time $t _ { n - 1 }$ and apply a one-step method to the index 1 system (2.4a), (2.5) to obtain $\left( \widetilde { q } _ { n } , \widetilde { u } _ { n } \right)$ . Since the position constraint (2.4c) only depends on $q$ ， the projections for $q$ and $u$ can be done sequentially.

Projection on Position Constraint. We define $q _ { n }$ as solution of the nonlinear system

$$
\begin{array} { r } { M ( \widetilde { q } _ { n } ) ( q _ { n } - \widetilde { q } _ { n } ) + G ^ { T } ( \widetilde { q } _ { n } ) \mu = 0 } \\ { g ( q _ { n } ) = 0 . } \end{array}
$$

Projection on Velocity Constraint. With the value $q _ { n }$ obtained from the above projection we let $u _ { n }$ be the solution of

$$
\begin{array} { r } { M ( q _ { n } ) ( u _ { n } - \widetilde { u } _ { n } ) + G ^ { T } ( q _ { n } ) \mu = 0 } \\ { G ( q _ { n } ) u _ { n } \qquad = 0 . } \end{array}
$$

Lubich (1991） introduced this kind of projection, because “it is invariant under affine transformations of coordinates". We remark that the system (2.11) is linear, whereas (2.1O) is nonlinear and has to be solved by (simplified) Newton iterations. The index 3 assumption that the matrix in Eq.(2.5) is invertible,implies the existence of the projected values $q _ { n }$ and $u _ { n }$ (at least for sufficiently small step size). It is possible to alter slightly the arguments of $M$ and $G ^ { T }$ in the upper lines of (2.10) and (2.11) or to solve the system (2.11) iteratively,if this is computationally advantageous. Convergence of this method is proved in the same way as in the index 2 case.

Velocity Stabilization. It can be seen from (2.6) that errors in the velocity constraint $G ( q ) u = 0$ are more critical for the numerical solution than errors in the position constraint $g ( q ) = 0$ . It is therefore interesting to study the method, where the numerical solution is projected only to the velocity constraint. Alishenas & Olafsson (1994) come to the conclusion that “velocity projection is the most efficient projection with regard to improvement of the numerical integration".

We have applied the code DOPRI5 in four different variants to the index 1 formulation of the pendulum equation (2.1): (i) standard application without any pro-jection,(ii) only projection on the position constraint, (iii) only projection on the velocity constraint,(iv) sequential position and velocity projections. The the global error (in position and velocity) during integration is shown in Fig.2.2. We conclude that a projection on the position constraint without projection on the velocity constraint does not improve the global error (it makes it even worse in our example). On the other hand, velocity stabilization is as efficient as the complete projection (position and velocity). Nearly no difference can be observed in Fig.2.2.

![](images/1a7a22670a2fe9dac27741d160191fe4d44bacf3d5c38b1367162ef0d4c28b26.jpg)  
Fig.2.2. Global error of DOPRI5 with various projections $\mathit { \Omega } ( A t o l = R t o l = 1 0 ^ { - 6 }$ ）

# Differential Equations with Invariants

Closely related to the above techniques is the numerical treatment of differential equations with invariants. Consider the initial value problem

$$
y ^ { \prime } = f ( y ) , \qquad y ( 0 ) = y _ { 0 } ,
$$

and suppose that the solution is known to have the invariant

$$
\varphi ( y ) = 0 .
$$

For example, the differential equation (1.46a,e) for $( q , u )$ has the invariants (1.46c) and (1.46d). Conservation laws (total energy,...） may also be written in the form (2.13). The invariant (2.13) is called a frst integral, if $\varphi _ { y } ( y ) f ( y ) \equiv 0$ in a neighbourhood of the solution.

Linear first integrals of the form $\varphi ( y ) = c + d ^ { T } y$ are preserved exactly by most integration methods (e.g., Runge-Kutta and multistep methods). Quadratic first integrals are preserved exactly by symplectic Runge-Kutta methods (see Theorem II.16.7). More complicated invariants are in general not preserved.

The above projection techniques can be adapted to the treatment of the problem (2.12-13) (see Shampine (1986),Eich (1993),Ascher, Chin & Reich (1994)).We apply a numerical method to (2.12) and project (orthogonally or somehow else) the numerical solution onto the manifold defined by (2.13). As discussed above, this precedure retains the order of convergence of the basic method.

Hamiltonian Systems. Differential equations of the form

$$
p _ { \ i } ^ { \prime } = - \frac { \partial H } { \partial q _ { \ i } } ( p , q ) , \qquad q _ { \ i } ^ { \prime } = \frac { \partial H } { \partial p _ { \ i } } ( p , q ) , \qquad i = 1 , \ldots , n ,
$$

where $\displaystyle H : \mathbb { R } ^ { 2 n }  \mathbb { R }$ is a smooth function, always have ${ \cal H } ( p , q ) = C o n s t$ as first integral. It is tempting to exploit this information and project the numerical solution

![](images/6ae6d227259038adb5c9f0f5153bcd6ae4a551bdc1c28b3cb349e1ddced4f7a3.jpg)  
Fig. 2.3. Study of the projection onto the manifold ${ \cal H } ( p , q ) = { \cal H } ( p _ { 0 } , q _ { 0 } )$

onto the manifold $H ( p , q ) = H ( p _ { 0 } , q _ { 0 } )$ . Consider for example the perturbed Kepler problem with Hamiltonian

$$
H ( p , q ) = { \frac { p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } } { 2 } } - { \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } } - { \frac { 0 . 0 0 5 } { \sqrt { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 } } } }
$$

and initial values $q _ { 1 } ( 0 ) = 1 - e$ ， $q _ { 2 } ( 0 ) = 0$ ， $p _ { 1 } ( 0 ) = 0$ ， $p _ { 2 } ( 0 ) = \sqrt { ( 1 + e ) / ( 1 - e ) }$ (eccentricity $e = 0 . 6 { \dot { } } ,$ ). The upper pictures of Fig. 2.3 show the numerical solution obtained by the explicit Euler method with step size $h = 0 . 0 1$ ; to the left without any projection, and to the right with projection onto ${ \cal H } = C o n s t$ . An improvement can be observed, but the numerical solution still does not reflect the geometric structure of the exact solution (invariant torus). We also have applied the symplectic Euler method (see Eq.(16.54) of Sect.II.16). Here we see that the numerical