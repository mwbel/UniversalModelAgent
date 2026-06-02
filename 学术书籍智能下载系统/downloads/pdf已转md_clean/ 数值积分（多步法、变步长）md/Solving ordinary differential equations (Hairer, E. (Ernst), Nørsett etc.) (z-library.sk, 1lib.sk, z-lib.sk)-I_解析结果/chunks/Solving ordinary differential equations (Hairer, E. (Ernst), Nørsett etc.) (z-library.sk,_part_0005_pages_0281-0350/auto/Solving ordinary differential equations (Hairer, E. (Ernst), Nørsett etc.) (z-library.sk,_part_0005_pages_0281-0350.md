A repeated differentiation of this equation, using (13.11), leads to

$$
\begin{array} { r l } & { \quad ( \boldsymbol { g } ^ { \prime } ) ^ { ( 3 ) } = \sum _ { \boldsymbol { g } } \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) \boldsymbol { y } ^ { \mathcal { N } } + \sum _ { \boldsymbol { g } } \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { y } ^ { \prime } ) f ^ { \mathcal { N } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) \boldsymbol { \hat { y } } ^ { \mathcal { N } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) } \\ & { \quad \quad \times \delta _ { \boldsymbol { g } } ^ { 2 } f ^ { \prime } } \\ & { \quad \quad \quad \times \delta _ { \boldsymbol { g } } ^ { 2 } f ^ { \prime } } \\ & { \quad \quad \quad + \sum _ { \boldsymbol { g } } \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { y } ^ { \prime } ) \boldsymbol { y } ^ { \mathcal { N } } \boldsymbol { g } ^ { \mathcal { N } } \boldsymbol { g } ^ { \mathcal { L } } } \\ & { \quad \quad \quad \quad + \sum _ { \boldsymbol { g } } \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { y } ^ { \prime } ) \boldsymbol { y } ^ { \mathcal { N } } \boldsymbol { g } ^ { \mathcal { L } } f ^ { \mathcal { N } } ( \boldsymbol { g } , \boldsymbol { y } ) + \sum _ { \boldsymbol { g } } \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { y } ^ { \prime } ) f ^ { \mathcal { N } } ( \boldsymbol { g } , \boldsymbol { y } ) } \\ & { \quad \quad \quad \times \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) } \\ & { \quad \quad \quad \quad \times \frac { \partial f ^ { \prime } } { \partial \boldsymbol { g } ^ { \prime } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) \boldsymbol { y } ^ { \mathcal { N } } ( \boldsymbol { g } , \boldsymbol { g } ) \boldsymbol { y } ^ { \mathcal { L } } ( \boldsymbol { g } , \boldsymbol { g } ^ { \prime } ) \boldsymbol { y } ^ { \mathcal { L } } } \\ &  \quad \quad \quad \times \frac { \partial f ^ { \prime } }  \partial \boldsymbol { g }  \end{array}
$$

The continuation of this process becomes evcn more complex than for first order differential equations. A graphical representation of the above formulas will therefore be very helpful. In order to distinguish the derivatives with respect to $y$ and $y ^ { \prime }$ we need two kinds of vertices: "meagre" and "fat". Figure 13.1 shows the graphs that correspond to the above formulas.

For a precise definition of the above graphs we give

Definition 13.2. A labelled $N$ -tree of order $q$ is a labelled tree (see Definition 2.2)

$$
t : A _ { q } - \{ j \} \ \to \ A _ { q }
$$

![](images/00930c89a043001c2150dd4c65bc838b25d10a37ace392e5ac0e601c72acc268.jpg)  
Figure 13.1. The derivatives of the exact solution

together with a mapping

$$
t ^ { \prime } : A _ { q } \to \{ " \mathrm { m e a g r e } ^ { \prime \prime } , " \mathrm { f a t } " \}
$$

which satisfies:

a) the root of $t$ is always fat; i.e. $t ^ { \prime } ( j ) =$ "fat"; b) a meagre vertex has at most one son and this son has to be fat. We denote by $L N T _ { q }$ the set of all labelled $\mathbf { N }$ -trees of order $q$

The reason for Condition b) in Definition 13.2 is that all derivatives of $g \left( y , y ^ { \prime } \right) = y ^ { \prime }$ vanish identically with the exception of the first derivative with respect to y'.

In the scquel we use the notation end-vertex for a vertex which has no son. If no confusion is possible, we write $t$ instead of $\left( t , t ^ { \prime } \right)$ for a labelled $\mathbf { N }$ -tree.

Definition 13.3. For a labelled $\mathbf { N }$ -trce t we denote by

$$
\boldsymbol { F } ^ { J } ( \iota ) ( y , y )
$$

the expression which is a sum over the indices of all fat vertices of t (without $j _ { i }$ ， the index of the root) and ovcr the indiccs of all meagre end-vertices. The general term of this sum is a product of expressions

$$
\frac { \partial ^ { r } f ^ { K } } { \partial y ^ { L } \cdot \cdot \cdot \partial y ^ { \prime } { } ^ { M } \cdot \cdot \cdot \cdot } ( y , y ^ { \prime } ) \qquad \mathrm { a n d } \qquad y ^ { \prime } { } ^ { K } .
$$

A factor of the first type appears if the fat vertex $k$ is connected via a meagre son with $l , \ldots$ and directly with the fat sons $m \textrm { , } \ldots ;$ a factor $y ^ { \prime K }$ appears if $k$ is the index of a meagrc end-vertex. The vector $F \left( t \right) \left( y , y ^ { \prime } \right)$ is again called an elementary differential.

For some examples, see Table 13.3. Obscrve that the indices of the meagre vertices, which arc not end-verticcs, play no role in the above definition. In analogy to Definition 2.4 we have

Definition 13.4. Two labelled N-trees $\textbf { ( } t \textbf { , } t \textbf { ) }$ and $\scriptstyle ( u \ , u \ ^ { \prime } )$ arc equivalent, if they differ only by a permutation of their indices; i.e. if they have the same order, say $q$ ， and if there exists a bijection 0 $\tau { \dot { \mathbf { \nabla } } } { \cdot } { \mathbf { A } } _ { q } \to { \mathbf { \nabla } } A _ { q }$ with $\sigma \left( j \right) = j$ , such that $t \sigma = \sigma u$ on $A _ { q } - \{ j \}$ and $t ^ { \prime } \sigma = u ^ { \prime }$

For example, the second and fourth labelled $\mathbf { N }$ -trees of Formula (13.12;4) in Figure 13.1 are equivalent; and also the sccond and fifth of Formula (13.12;5).

Definition 13.5. An equivalence class of $q$ -th order labelled Ntrees is called an $N$ -tree of order $q$ . The set of all $\mathbf { N }$ -trees of order $q$ is denoted by $^ { N T } { } _ { q }$ . Wc further denote by $\alpha ( t )$ the number of elements in the equivalence class $t$ , i.c. the number of possible different monotonic labellings of t .

Representatives of $\mathbf { N }$ -trees up to order 5 are shown in Table 13.3. We are now able to give a closed formula for the derivatives of the exact solution of (13.11).

Theorem 13.6. The exact solution of (13.11) satisfies

$$
( y ^ { J } ) ^ { ( q ) } = \sum _ { t \ll L N T _ { q - 1 } } F ( t ) ( y , y ^ { \prime } ) = \sum _ { t \in N T _ { q - 1 } } \propto ( t ) F ( t ) ( y , y ^ { \prime } ) .
$$

Proof: The general formula is obtained by continuing the compu-tation for (13.12;2-4) as in Section II.2. QED.

# The derivatives of the numerical solution

We first rewrite (13.4) as

$$
\begin{array} { l } { { g _ { i } = y _ { 0 } + c _ { i } h y _ { 0 } ^ { \prime } + \sum \overline { { { a } } } _ { i j } h ^ { 2 } f \left( g _ { j } , g _ { j } ^ { \prime } \right) } } \\ { { \ } } \\ { { g _ { i } ^ { \prime } = y _ { 0 } ^ { \prime } \ + \ \sum a _ { i j } h f \left( g _ { j } , g _ { j } ^ { \prime } \right) } } \\ { { \ } } \\ { { y _ { 1 } = y _ { 0 } + h y _ { 0 } ^ { \prime } \ + \ \sum \overline { { { b } } } _ { i } h ^ { 2 } f \left( g _ { i } , g _ { i } ^ { \prime } \right) } } \\ { { \ } } \\ { { y _ { 1 } ^ { \prime } = y _ { 0 } ^ { \prime } \ + \ \sum b _ { i } h f \left( g _ { i } , g _ { i } ^ { \prime } \right) } } \end{array}
$$

so that the intermediate values $g _ { i } , g _ { i } ^ { \prime }$ are treated in the same way as $y _ { 1 } , y _ { 1 } ^ { \prime }$ In (13.13) there appear expressions of the form $h ^ { 2 } \Phi ( h )$ and $h \phi ( h ) .$ . Therefore we have to use in addition to (2.4) the formula

$$
{ ( h ^ { 2 } \Phi ( h ) ) } ^ { ( q ) } \vert _ { \tiny { h  0 } } = q \cdot ( q - 1 ) \cdot ( \Phi ( h ) ) ^ { ( q - 2 ) } \vert _ { \tiny { h  0 } } .
$$

We now compute successvely the derivatives of $g _ { i } ^ { J }$ and ${ g _ { i } } ^ { \prime J }$ at $h = 0$

$$
\begin{array} { c } { { ( g _ { i } ^ { J } ) ^ { ( 1 ) } \vert _ { \hphantom { 0 } h = 0 } = c _ { i } y _ { 0 } ^ { \prime \phantom { 0 } J } } } \\ { { ( g _ { i } ^ { \prime \phantom { 0 } J } ) ^ { ( 1 ) } \vert _ { \hphantom { 0 } h = 0 } = \sum a _ { i j } f ^ { J } \vert _ { \hphantom { 0 } y _ { 0 } , y _ { 0 } ^ { \prime } } } } \\ { { ( g _ { i } ^ { J } ) ^ { ( 2 ) } \vert _ { \hphantom { 0 } h = 0 } = 2 \sum a _ { i j } f ^ { J } \vert _ { \hphantom { 0 } y _ { 0 } , y _ { 0 } ^ { \prime } } . } } \end{array}
$$

For a further differentiation we need

$$
( f ^ { J } ( g _ { j } , g _ { j } ^ { \prime } ) ) ^ { ( 1 ) } = \sum _ { K } \frac { \partial f ^ { J } } { \partial y ^ { K } } ( g _ { j } , g _ { j } ^ { \prime } ) ( g _ { j } ^ { K } ) ^ { ( 1 ) } + \sum _ { K } \frac { \partial f ^ { J } } { \partial y ^ { \prime , K } } ( g _ { j } , g _ { j } ^ { \prime } ) ( { g _ { j } ^ { \prime } } ^ { K } ) ^ { ( 1 ) }
$$

With this formula we then obtain

$$
\begin{array} { c } { { ( g _ { i } ^ { \prime } ) ^ { ( 2 ) } \vert _ { \phantom { t } { h } _ { - 0 } } = 2 \sum _ { j } a _ { i j } c _ { j } \sum _ { K } \frac { \partial f ^ { j } } { \partial y ^ { K } } { y } ^ { \prime } { \ ' } _ { \left. \begin{array} { c } { { \mathcal { F } _ { 0 } , y _ { 0 } } } \\ { { \mathcal { F } _ { 0 } , y _ { 0 } } } \end{array} \right. } } } \\ { { + \left. 2 \sum _ { a _ { i j } a _ { j } \lambda _ { k } } \sum \frac { \partial f ^ { j } } { \partial y ^ { \prime } } { \ ' } _ { \mathcal { K } } \right. _ { \phantom { a } y _ { 0 } , y _ { 0 } } } } \\ { { \ j _ { k } \left( g _ { i } ^ { j } \right) ^ { ( 3 ) } \vert _ { \phantom { t } { h } _ { - 0 } } = 3 \cdot 2 \sum _ { i j } a _ { i j } c _ { j } \sum _ { K } \frac { \partial f ^ { j } } { \partial y ^ { K } } { \ ' } _ { \left. \begin{array} { c } { { \mathcal { F } _ { 0 } , y _ { 0 } } } \\ { { \mathcal { F } _ { 0 } , y _ { 0 } } } \end{array} \right. } } } \\ { { + \left. 3 \cdot 2 \sum _ { j , k } \overline { { { a } } } _ { i j } a _ { j k } \sum \frac { \partial f ^ { j } } { \partial y ^ { \prime } } { \ ' } _ { \mathcal { K } } { \ ' } _ { \mathcal { I } } { \ ' } ^ { K } \right. _ { y _ { 0 } , y _ { 0 } } } . } \end{array}
$$

To write down a general formula we need

Definition 13.7. For a labelled $\mathbf { N }$ -tree we denote by $\Phi _ { j } ( t )$ the expression which is a sum over the indices of all fat vertices of $t$ (without $j ,$ the index of the root). The general term of the sum is a product of

$a _ { k l }$ if the fat vertex k has a fat son l; $\bar { a } _ { k l }$ if the fat vertex $k$ is connected via a meagre son with l; and $c _ { k } ^ { m }$ if the fat vertex $k$ is connected with $m$ meagre end-vertices.

Theorem 13.8. The gi, ${ { g } _ { i } } ^ { \prime }$ of (13.13) satisfy

$$
\begin{array} { l } { { ( g _ { i } ^ { J } ) ^ { ( q + 1 ) } \bigr | _ { \begin{array} { l } { { h = 0 } } \end{array} } = ( q + 1 ) \sum _ { \begin{array} { l } { { t \in L N T _ { q } } } \end{array} } \gamma ( t ) \sum _ { j } \overline { { { a } } } _ { i j } \Phi _ { j } ( t ) { F } ^ { J } ( t ) ( y _ { 0 } , y _ { 0 } ^ { } ) } } \\ { { ( g _ { i } ^ { \prime , J } ) ^ { ( q ) } \bigr | _ { \begin{array} { l } { { h = 0 } } \end{array} } = \sum _ { \begin{array} { l } { { t \in L N T _ { q } } } \end{array} } \gamma ( t ) \sum _ { j } \Phi _ { j } ( t ) { F } ^ { J } ( t ) ( y _ { 0 } , y _ { 0 } ^ { } ) \ . \qquad ( 1 3 . 1 5 ; \begin{array} { l } { { } } \end{array} } } \end{array}
$$

where $\gamma ( t )$ is given in Definition 2.10.

Proof: For small values of $q$ these formulas were obtained above; for general values of $q$ they are proved like Theorem 2.11. System (13.2) is a special case of what will later be treated as a partitioned system (see Section II.14). Theorem 13.8 will then appear again in a new light. QED.

Because of the similarity of the formulas for $g _ { i }$ and $y _ { 1 , \ } g _ { i } ^ { \prime }$ and $y _ { 1 } ^ { \prime }$ we have

Theorem 13.9. The numerical solution y1, yi of (13.13) satisfies

$$
\begin{array} { r l } & { ~ ( y _ { 1 } ^ { J } ) ^ { ( q ) } \vert _ { \begin{array} { l } { h = 0 } \end{array} } = q \displaystyle \sum _ { t \in L N T _ { q - 1 } } \gamma ( t ) \sum _ { i } ^ { - } \bar { b _ { i } } \Phi _ { i } ( t ) F ^ { J } ( t ) ( y _ { 0 } , y _ { 0 } ) } \\ & { ~ ( y _ { 1 } ^ { \prime , J } ) ^ { ( q - 1 ) } \vert _ { \begin{array} { l } { h = 0 } \end{array} } = \displaystyle \sum _ { t \in L N T _ { q - 1 } } \gamma ( t ) \sum _ { i } b _ { i } \Phi _ { i } ( t ) F ^ { J } ( t ) ( y _ { 0 } , y _ { 0 } ) \cdot ( y _ { 0 } , y _ { 1 } ^ { \prime } ) } \\ & { ~ \mathrm { ~ N E D } . } \end{array}
$$

# The order conditions

For the study of the order of a Nystrom method (Definition 13.1) one has to compare the Taylor series of $y _ { 1 } , y _ { 1 } ^ { \prime }$ with that of the true solution $y \left( x _ { 0 } { + } h \right) , y ^ { \prime } ( x _ { 0 } { + } h )$

Tbeorem 13.10. A Nystrom method (13.4) is of order $\boldsymbol { p }$ iff

$$
\begin{array} { r l r } & { \sum _ { \hat { b } _ { i } } \Phi _ { i } ( t ) = \displaystyle \frac { 1 } { \left( \boldsymbol { \rho } ( t ) + 1 \right) \cdot \boldsymbol { \gamma } ( t ) } f o r ~ N \cdot t r e e s ~ t ~ w i t h ~ \boldsymbol { \rho } ( t ) \le p - 1 ~ , }  & \\ & { \sum _ { \hat { b } _ { i } } \Phi _ { i } ( t ) = \displaystyle \frac { 1 } { \boldsymbol { \gamma } ( t ) } ~ \qquad } & { f o r ~ N \cdot t r e e s ~ t ~ w i t h ~ \boldsymbol { \rho } ( t ) \le p ~ . } \end{array}
$$

Here p(t) denotes the order of the $N$ -tree t, $\Phi _ { i } ( t )$ and $\gamma ( t )$ are given by Definition 13.7 and Formula (2.17).

Proof: The "if" part is an immediate consequence of Theorems 13.6 and 13.9. The "only if" part can be shown in the same way as for first order equations (cf. Excrcisc 4 of Section II.2). QED.

Let us briefly discuss whether the extra freedom in the choice of the parameters of (13.4) (by discarding the assumption (13.5)） can lead to a considerable improvement. Since the order conditions for RK-methods (Theorem 2.13) are a subset of (13.21) (see Exercise 3 below)， it is impossible to gain order with this extra freedom. Only somc (never all) error coefficients can be made smaller. Therefore we shall turn to Nystrom methods (13.9) for special second order differential equations (13.8).

For the study of the order conditions for (13.9) we write ( in autonomous form

$$
y \ ^ { \prime \prime } = f \left( y \right) .
$$

This special form implies that those elementary differentials which contain derivatives with respect to $y ^ { \prime }$ ， vanish identically. Consequently, only the following subset of $\mathbb { N }$ -trecs has to be considered:

Definition 13.11. An $\mathbf { N }$ -tree $\ell$ is called a special $N$ -tree or $S N$ -tree, if the fat vertices have only meagre sons.

Theorem 13.12. A Nystrom method (13.9) for the special differential equation (13.8) is of order p, if

$$
\begin{array} { r l r } & { \sum _ { \bar { b } _ { i } } \Phi _ { i } ( t ) = \frac { 1 } { \left( \rho ( t ) + 1 \right) \cdot \gamma ( t ) } } & { f o r ~ S N \cdot t r e e s ~ t ~ w i t h ~ \mathsf { p } ( t ) \le p - 1 ~ , } \\ & { \sum _ { \bar { b } _ { i } } \Phi _ { i } ( t ) = \displaystyle \frac { 1 } { \gamma ( t ) } } & { f o r ~ S N \cdot t r e e s ~ t ~ w i t h ~ \mathsf { p } ( t ) \le p ~ . } \\ & { \overset { i } { \ } } & { ( 1 3 . 2 4 ) } \end{array}
$$

NED.

Table 13.3. SN-trees, elementary differentials and order conditions   

<table><tr><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>p(1）</td><td rowspan=1 colspan=1>α（）</td><td rowspan=1 colspan=1>y(1)</td><td rowspan=1 colspan=1>F()(y，y）</td><td rowspan=1 colspan=1>Φ(）</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>oj</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>广</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>~2</td><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>EkyKK</td><td rowspan=1 colspan=1>G</td></tr><tr><td rowspan=1 colspan=1>3A</td><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>∑fkLyKyiKLEsislL</td><td rowspan=1 colspan=1>²Ea</td></tr><tr><td rowspan=1 colspan=1>15~61</td><td rowspan=1 colspan=1>kmmkm</td><td rowspan=1 colspan=1>444</td><td rowspan=1 colspan=1>131</td><td rowspan=1 colspan=1>4824</td><td rowspan=1 colspan=1>∑SKLMyKyLyKLMMSiMy&#x27;SML,MMshyMLM</td><td rowspan=1 colspan=1>GEcammMang</td></tr><tr><td rowspan=1 colspan=1>819101111213</td><td rowspan=1 colspan=1>KmpP.mPk   mmk   PmPkopm&lt;</td><td rowspan=1 colspan=1>555555</td><td rowspan=1 colspan=1>163411</td><td rowspan=1 colspan=1>510203060120</td><td rowspan=1 colspan=1>KL,M,P∑SLMpy&#x27;LyMPLMPEfepsLspL,P∑SLPSMy.LLPM∑SisMPy&#x27;My&#x27;pL,PMEispspLP</td><td rowspan=1 colspan=1>GM²a?∑ajlap1,p∑cajn1Man0²1Maja1</td></tr></table>

All SN-trees up to order 5， together with the elementary differentials and thc expressions $\Phi _ { j }$ ,p， $\alpha$ ，and $\gamma$ ， which are needed for the order conditions, are given in Table 13.3.

# On the construction of N ystrom methods

The following simplifying assumptions are useful for the construc-tion of Nystrom methods.

Lemma 13.13. Under the assumption

$$
\overline { { b } } _ { i } = b _ { i } ( 1 - c _ { i } ) \qquad i = 1 , \ldots , s
$$

the condition (13.24) implies (13.23).

Proof: Let $t$ be a SN-trce of order $\leq p - 1$ and denote by u the SN-tree of order $\rho ( t ) + 1$ obtained from t by attaching a new branch with a meagre vertex to the root of $t$ .By Definition 13.7 we have $\Phi _ { i } ( u ) = c _ { i } \Phi _ { i } ( t )$ and from Formula (2.15） it follows that $\gamma ( u ) = ( \rho ( t ) + 1 ) \gamma ( t ) / \rho ( t ) .$ The conclusion now follows sincc

$$
\sum _ { i } \bar { b _ { i } } \Phi _ { i } ( t ) = \sum _ { i } b _ { i } \Phi _ { i } ( t ) - \sum _ { i } b _ { i } \Phi _ { i } ( u ) = \frac { 1 } { \gamma ( t ) } - \frac { 1 } { \gamma ( u ) } = \frac { 1 } { ( \rho ( t ) + 1 ) \gamma ( t ) }
$$

QED.

Lemma 13.14. Let t and u be two SN-trees as skeiched in Figure 13.2, where ihe encircled parts are assumed to be identical. Then under the assumption

$$
{ \sum _ { j } } \bar { a } _ { i j } = \frac { c _ { i } ^ { ~ 2 } } { 2 } \qquad \quad i = 1 , . . . , s
$$

the order conditions for t and u are the same.

![](images/25e0053344924e79231715bbfdc2329e7ab5eb20a7f3be2721ab1447401271b0.jpg)  
Figure 13.2. Trees of Lemma 13.14

Proof: It follows from Dcfinition 13.7 and (13.26) that $\Phi _ { i } { \left( t \right) } = \Phi _ { i } { \left( u \right) } / 2$ and from Formula (2.15） that $\gamma ( t ) = 2 \gamma ( u )$ Both order conditions are thus identical. QED.

Condition (13.25) allows us to neglect the equations (13.23), while Condition (13.26) plays a similar role to that of (2.9) for Runge-Kutta methods. It expresses the fact that the $\boldsymbol { g } _ { i }$ of (13.13) approximate $y \left( x _ { \mathit { 0 } } { + } c _ { i } h \right)$ up to ${ \mathrm { O } } ( h ^ { 3 } )$ . As a consequence of Lemma 13.14, SN-trees which have at least one fat cnd-vertex can be left out (i.e. ${ t _ { 4 } } , { t _ { 6 } } , { t _ { 9 } } , { t _ { 1 0 } } , { t _ { 1 3 } }$ of Table 13.3).

With the help of (13.25) and (13.26) explicit Nystrom methods (13.9) of order $^ { 5 }$ with $s = 4$ can now easily be constructed: the order conditions for the trees $t _ { 1 } , \iota _ { 2 } , \iota _ { 3 } , t _ { 5 }$ and $t _ { 8 }$ just indicate that the quadrature formuia with nodes ${ \boldsymbol { c } } _ { 1 } = 0$ ， $c _ { 2 }$ ， $c _ { 3 }$ ， $c _ { 4 }$ and weights $b _ { \uparrow }$ ， $b _ { 2 }$ ， $b _ { 3 }$ $b _ { 4 }$ is of order 5. Thus the nodes $c _ { i }$ have to satisfy the orthogonality relation

$$
\begin{array} { l } { { \displaystyle \int _ { 0 } ^ { 1 } x ( x - c _ { 2 } ) ( x - c _ { 3 } ) ( x - c _ { 4 } ) d x = 0 } } \\ { { \mathrm { 0 } } } \end{array}
$$

and we sce that two degrecs of frcedom are still left in the choice of the quadrature formula. The $\bar { a } _ { \iota j }$ are now uniquely determined and can be computed as follows: $\bar { a } _ { 2 1 }$ is given by (13.26) for $i = 2$ .The order conditions for $\varepsilon _ { 7 }$ and $\varepsilon _ { 1 1 }$ constitute two linear equations for the unknowns

$$
\sum _ { j } \bar { a } _ { 3 j } c _ { j } \qquad \mathrm { a n d } \qquad \sum _ { j } \bar { a } _ { 4 j } c _ { j } .
$$

Torether ith 1 $i = 3$ Donen $\bar { a } _ { 3 1 }$ and $a _ { 3 2 }$ Finaly h $\ t _ { 1 7 }$ $\textstyle \sum _ { j } { \bar { a } } _ { 4 j } c _ { j } ^ { 2 }$ ficients $\sigma _ { 4 1 }$ $a _ { 4 2 }$ ， $\bar { a } _ { 4 3 }$ can be computed from a Vandermonde-type linear system. The method of Table 13.2 is obtained in this way.

For still higher order methods it is helpful to use further simpli fying assumptions; for exam ple

$$
\sum _ { j } \bar { a } _ { i j } c _ { j } ^ { q } = \frac { c _ { i } ^ { q + 2 } } { ( q + 2 ) ( q + 1 ) }
$$

which, for $q = 0$ , reduces to (13.26), and

$$
{ \sum } b _ { i } c _ { i } ^ { q } \overline { { { a } } } _ { i j } = b _ { j } \frac { c _ { i } ^ { q + 2 } } { ( q + 2 ) ( q + 1 ) } - \frac { c _ { i } } { q + 1 } + \frac { 1 } { q + 2 }
$$

which can be considered a generalization of Condition (1.12). For more details we refer to Hairer-Wanner (1976) and also to Albrecht (1955)，Batn (1976)， Beentjes-Gerritsen (1976)， Hairer (1977, 1982), where Nystrom methods of higher order are presented.

# Global convergence

Introducing the variable ${ \boldsymbol { z } } _ { n } = \left( y _ { n } , { \boldsymbol { y } } _ { n } ^ { \prime } \right) ^ { T }$ , a Nystrom method (1 can be written in the form

$$
z _ { 1 } = z _ { 0 } + h \Phi ( x _ { 0 } , z _ { 0 } , h )
$$

where

$$
\Phi ( x _ { 0 } , z _ { 0 } , h ) = \left( \begin{array} { c } { { y _ { 0 } ^ { \prime } + h \displaystyle { \sum _ { i } ^ { \prime } } b _ { i } k _ { i } ^ { \prime } } } \\ { { \displaystyle \sum _ { i } b _ { i } k _ { i } ^ { \prime } } } \end{array} \right) .
$$

(13.29) is just a special one-step method for the differcntial cquation (13.2)For a $\boldsymbol { p }$ -th order Nystrom method the_local error $( y ( x _ { 0 } { + } h ) { - } y _ { 1 } , y ^ { \prime } ( x _ { 0 } { + } h ) { - } y _ { 1 } ^ { \prime } ) ^ { T }$ can be bounded by $C h ^ { p + 1 }$ (Definition 13.1),which is in agreement with Formula (3.24). The convergence theorems of Section I.3 and the results on asymptotic expansions of the global error (Section I.8) are also valid here.

# Implementation of Nystrom methods

For an efficient implementation we nced a step size control mechanism. This can be performed in the same manner as for RKmethods (see Section II.4). One can either apply Richardson extrapolation in order to estimate the local error, or construct embedded Nystrom methods.

A series of embedded Nystrom methods has been constructed by Fehlberg (1972). These methods use a $( p + 1 )$ -st order approximation to $y \left( x _ { \mathrm { ~ 0 ~ } } \substack { + h } \right)$ for step size control. A $( p + 1 )$ -st order approximation to $y ^ { \prime } ( x _ { 0 } + h )$ is not needed, since the lower order approximations are used for step continuation.

As for first order differential equations, a different strategy - to use the higher order approximations for stcp continuation - turns out to be superior. A method of order 7(6) has been constructed by Dormand-Prince (1978) and its coefficients are given in Table 13.4. Morc recently, higher ordcr methods of this type were published by Filippi-Graf (1986).

# An extrapolation method for $y \ ^ { \prime \prime } { = } f \left( x \ , y \right)$

Les calculs originaux, comprenant environt 3.000 pages in-folio avec 358 grandes planches,et encore 3.800pagesdedeveloppementsmathematiques correspondants, appartiennent maintenant a la collection de manuscrits de la Bibliotheque de I'Universite, Christiania.   
(Stormer,1921)

If we rewrite the differential equation (13.8) as a first order system

$$
{ \binom { y } { y } } ^ { \prime } = { \binom { y } { f ( x , y ) } } \ , \qquad { \binom { y } { y } } ( x _ { 0 } ) = { \binom { y _ { 0 } } { y _ { 0 } ^ { \prime } } }
$$

we can apply the GBS-algorithm (9.13) directly to (13.30); this yields

$$
\begin{array} { r l } & { \quad y _ { 1 } = y _ { 0 } + h y _ { 0 } ^ { \prime } } \\ & { \quad y _ { 1 } ^ { \prime } = y _ { 0 } ^ { \prime } + h f ( x _ { 0 } , y _ { 0 } ) } \\ & { \quad y _ { i + 1 } = y _ { i - 1 } + 2 h y _ { i } ^ { \prime } } \\ & { \quad y _ { i + 1 } ^ { \prime } = y _ { i - 1 } ^ { \prime } + 2 h f ( x _ { i } , y _ { i } ) \qquad i = 1 , 2 , \ldots , 2 n } \\ & { \quad S _ { h } ( x ) = ( y _ { 2 n - 1 } + 2 y _ { 2 n } + y _ { 2 n + 1 } ) / 4 } \\ & { \quad S _ { h } ^ { \prime } ( x ) = ( y _ { 2 n - 1 } ^ { \prime } + 2 y _ { 2 n } ^ { \prime } + y _ { 2 n + 1 } ^ { \prime } ) / 4 \ . } \end{array}
$$

<table><tr><td>0</td><td>v+</td><td></td><td>098 001-）L</td><td colspan="2">090 1+L)L</td><td colspan="4">S</td><td colspan="4"></td><td>0</td><td colspan="2"></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8</td><td></td><td></td><td>0</td><td></td><td>0</td><td></td><td>0</td><td></td><td>！</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>9</td><td></td><td>(1MLLE+ 21824</td><td></td><td>12/97+</td><td></td><td>(1z/81+</td><td></td><td>(12/ss+</td><td></td><td></td><td></td><td>833</td><td></td></tr><tr><td>0</td><td>V-</td><td></td><td></td><td>1A-sL</td><td></td><td>L</td><td></td><td>12018922 {一</td><td>31612991</td><td>0820</td><td>968)6966 &#x27;s</td><td></td><td>2222 111111111111111</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(17/6L1£+</td><td>(1+</td><td></td><td>(1z/£11+</td><td></td><td></td><td></td><td></td></tr><tr><td>081 （1z&gt;-L) 6b</td><td>09 L</td><td>12-200</td><td>L</td><td></td><td>(111111</td><td>1122</td><td>15161+7751</td><td>96944</td><td>188041656</td><td>8711</td><td></td><td>4401181204 S</td><td></td><td>122256 si</td><td>15353 1/181+£61</td><td>正+</td><td>4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1/6-</td><td>(181-</td><td></td><td>1&gt;1</td><td></td><td></td><td></td><td></td></tr><tr><td>081 (z+L)</td><td>09</td><td>(1z+2)</td><td>090</td><td></td><td></td><td></td><td></td><td>9690</td><td></td><td>27266960</td><td></td><td>22918224</td><td></td><td>121525</td><td>82514</td><td></td><td>4</td></tr><tr><td>64</td><td>L</td><td></td><td>L</td><td></td><td></td><td></td><td></td><td>127244-11411</td><td></td><td>871</td><td></td><td>S</td><td></td><td>1112212001</td><td></td><td></td><td>1-L</td></tr><tr><td>S 可</td><td>S 1</td><td></td><td>S 8</td><td></td><td></td><td></td><td></td><td></td><td></td><td>£69</td><td></td><td>9</td><td></td><td>825</td><td></td><td>882</td><td>三</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>9</td><td></td><td>5 7618</td><td></td><td>5 9604</td><td></td><td>S</td><td>[</td></tr><tr><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>513</td><td></td><td>S4</td><td></td><td>7618 IL</td><td>8 E</td></tr><tr><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0S1</td><td>三</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>！ 000</td><td>[</td></tr><tr><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>01 1</td></tr><tr><td>1</td><td>0</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>1</td><td>q</td><td></td><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>p</td><td>?</td></tr></table>

Here, $S _ { h } \left( x \right)$ and $S _ { h } ^ { \prime } \left( x \right)$ are the numerical approximations to $y \left( x \right)$ and $y ^ { \prime } ( x )$ at ${ x = } { x _ { 0 } + } { H _ { \mathrm { ~ } } }$ ,where $H = 2 n h$ and ${ x _ { i } = } { x _ { 0 } + } i h$ . We now make the following important observation: for the computation of $y _ { 0 } , y _ { 2 } , y _ { 4 } , . . . , y _ { 2 n }$ (even indices) and of $y _ { 1 } ^ { \prime } , y _ { 3 } ^ { \prime } , . . . , y _ { 2 n + 1 } ^ { \prime }$ (odd indices) onlythe function values $f ( x _ { 0 } , y _ { 0 } ) , f ( x _ { 2 } , y _ { 2 } ) \quad , . . . ,$ $f \left( x _ { 2 n } , y _ { 2 n } \right)$ have to be calculated. Furthermore, we know from (9.17) that $y _ { 2 n }$ and $( y _ { 2 n - 1 } ^ { \prime } + y _ { 2 n + 1 } ^ { \prime } ) / 2$ cach posss an asymptotic expansion in even powers of $^ h$ . It is therefore obvious that (13.31c) should be replaced by (Gragg (1965))

$$
\begin{array} { l } { { S _ { h } ( x ) = y _ { 2 n } } } \\ { { S _ { h } ^ { \prime } ( x ) = ( y _ { 2 n - 1 } ^ { \prime } + y _ { 2 n + 1 } ^ { \prime } ) / 2 . } } \end{array}
$$

Using this final step, the number of function evaluations is reduced by a factor of two. These numerical approximations can now be used for extrapolation. Wc takc the harmonic sequence (9.8), put

$$
T _ { i 1 } = S _ { h } \left( x _ { 0 } { + } H \right) , T _ { i 1 } ^ { \prime } = S _ { h } ^ { \prime } \left( x _ { 0 } { + } H \right)
$$

and_compute theextrapolated expressions $T _ { i , j }$ and $T _ { i , j }$ by the Aitken-Neville formula (9.12).

Remark. Eliminating the $y _ { j } ^ { \prime }$ -values in (13.31b) we obtain the equivalent formula

$$
y _ { i + 2 } - 2 y _ { i } + y _ { i - 2 } = { ( 2 h ) } ^ { 2 } f \left( x _ { i } , y _ { i } \right) ,
$$

which is often called Stoermer's rule. For the implementation the formulation (13.31b) is to be preferred, since it is more stable with respect to round-off errors (see Section I.10).

# Numerical comparis ons

We conclude this Section with some numerical comparisons. For this we have written the following three codes:

ODEX2 is based on the extrapolation method described above. It is implemented in the same way as ODEX (the extrapolation code for first order differential equations). In particular, the order and step size strategy is that of Section I1.9.

DOPRIN is based on the fixed-order embedded Nyström method, whose coeficients are given in Table 13.4. Its step size selection is the same as for DOPRI8 and is described in Section I1.4.

FILGR9 is based on an embedded Nystrom method of order 9(8),due to Filippi-Graf (1986). It is implemented in the samc way as DOPRIN.

Listings of the two codes ODEX2 and DOPRIN are given in the appendix.

These three codes were applied to the three differential equations TWOB. LAGR, PLEl of Section I.10, which are all of the form $y ^ { \prime \prime } { = } f \left( x \ , y \right) $ . Each example was computed with the local error tolerances $1 0 ^ { - 3 }$ $1 0 ^ { - 6 }$ $1 0 ^ { - 9 }$ ， $1 0 ^ { - 1 2 }$ ， $1 0 ^ { - 1 5 }$ In Figurc 13.3 the precision $- \mathrm { l o g } _ { 1 0 } ( e r r o r )$ is compared to the number of function calis. In order to demonstrate the superiority of the special methods for $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ ， we also include the results of ODEX, the code for first order differential equations (Section I1.9).

![](images/11a2d4500f42379e86378bdd8ba75f37df574dd541558695b5c5b9d309e5baf9.jpg)  
Figure 13.3. Work-precision diagrams for the above examples

One can observe that ODEX2 is a real improvement over ODEX. The program is nearly twice as fast, which is in agreement with the theoretical considerations. For stringent tolerances ( $t o l \le 1 0 ^ { - 1 0 }$ ）the extrapolation code, which allows very high orders, gives the best results. For tolerances between $1 0 ^ { - 3 }$ and $1 0 ^ { - 8 }$ the fixed-order codes DOPRIN and FILGR9 are preferable. However, no superiority comparable to that of DOPRI8 for first-order systems (see Section II.10) can be observed.

Similar results as for ODEX2 are obtained by the code DIFEX2 of Deuflhard and Bauer (see Deuflhard (1985)).

# Higher order systems

The extension of the ideas of this Section to higher order systems

$$
y ^ { ( n ) } = f \left( x , y , y ^ { \prime } , \ldots , y ^ { ( n - 1 ) } \right)
$$

is now more or less straightforward. Again, a real improvement is only possible in the case when the right-hand side of (13.33) depends only on $x$ and y. A famous paper on this subject is the work of Zurmühl (1948). Tables of order conditions and methods are given in Hebsacker (1982).

# Exercises

1. Verify that the methods of Table 13.2 are of order 4 and 5, respectively.

2. The error coefficients of a $p$ -th order Nystrom method are defincd by

$$
\begin{array} { r l r } & { e ( t ) = \mathbb { 1 } - { ( \rho ( t ) + 1 ) } \gamma { ( t ) } \sum _ { \iota } ^ { } { \bar { b _ { i } } \Phi _ { i } ( t ) } } & { \mathrm { f o r ~ } \mathsf { \rho \rho \rho \rho ( t ) = } p } \\ & { e ^ { \prime } { ( t ) } = \mathbb { 1 } - \gamma { ( t ) } \sum _ { i } ^ { } { b _ { i } \Phi _ { i } ( t ) } } & { \mathrm { f o r ~ } \mathsf { \rho \rho \rho ( } t ) = p + 1 \ . } \end{array}
$$

a) The assumption (13.25) implies that

$$
e \left( t \right) = - \rho \left( t \right) e ^ { \prime } \left( u \right) \qquad \mathrm { ~ f o r ~ } \rho \left( t \right) = p ,
$$

where $\boldsymbol { \mu }$ is the $_ \mathrm { N }$ -tree obtained from $\ell$ by adding a branch with a meagre vertex to the root of t .

b) Compute the error cocfficients of Nystrom's method (Table 13.1) and compare them to those of the classical Runge-Kutta method.

3. Show that the order conditions for RK-methods (Theorem 2.13) arc a subset of the conditions (13.21). They correspond to the $\mathbf { N }$ - trees, all of whose vertices are fat.

4. Sometimes the definition of order of Nystrom methods (13.9) is relaxed to

$$
y \left( x _ { 0 } { + } h \right) - y _ { 1 } = \mathbf { O } ( h ^ { p + 1 } )
$$

$$
y \prime ( x _ { 0 } + h ) - y _ { 1 } ^ { \prime } = \mathbf { O } \big ( h ^ { p } \big )
$$

(see Nystrom (1925)). Show that the conditions (13.35) are not sufficient to obtain global convergence of order $p$

Hint. Investigate the asymptotic expansion of the global error with the help of Theorem 8.1 and Formula (8.8).

5. The numerical solutions $T _ { k k }$ and $T _ { k k }$ of the extrapolation method of this section are equivalent to a Nystrom method of order $p = 2 k$ with $s = \frac { p ^ { 2 } } { 8 } + \frac { p } { 4 } + 1$ stages.

# 11.14. P-series for partitioned ordinary differential equations

Divide ut regnes (Machiavelli)

We developed the theory of B-series (Sections II.2 and I.11) for the construction of the order conditions for RK-methods, where the underlying differential equation is autonomous, or where $x$ and y are integrated in the same way (i.e. (1.9) is satisfied). But we have already encountered several situations in which this theory was insufficient.

i) In Section I.1 (Exercise 6) we saw that additional order conditions arise if $x$ and y are integrated differently, i.e. if (1.9) is not satisfied. To understand their structure, we need an extension of the theory of B-series to the partitioned ordinary differential equation (2.1).

ii) The approach of Fehlberg (Section I.12) requires the study of RK-methods without (1.9) and in which the derivatives $f \mathrm { ~ , ~ } f _ { x } \mathrm { , ~ } f _ { x x } \mathrm { , . . . }$ vanish at $( x _ { 0 } , y _ { 0 } )$

iii) In Section II.13 we considered direct methods for the second order differential equation $y ^ { \prime \prime } { = } f \left( y \ : , y \ : \right)$ . We extended the theory of B-series to the partitioned ordinary differential equation

$$
\left( { y \atop y } , \right) ^ { \prime } = \left( { y \atop f \left( y , y \right) } ^ { \prime } \right)
$$

in order to obtain the general structure of the order conditions.

It is natural to ask for a common theory for such situations. Therefore, our aim is (Hairer (1981)) to extend the theory of Bseries to the general partitioned ordinary differential equation

$$
\left( \begin{array} { c } { { y _ { a } } } \\ { { } } \\ { { y _ { b } } } \end{array} \right) ^ { \prime } = \left( \begin{array} { c } { { f _ { a } ( y _ { a } , y _ { b } ) } } \\ { { } } \\ { { f _ { b } ( y _ { a } , y _ { b } ) } } \end{array} \right)
$$

and to obtain as special cases the order conditions for the above mentioned cases.

Other important applications of this theory will be to the study of order conditions for methods which treat different parts of an ordinary differential equation by different methods. These can be for example the linear and nonlinear parts (W-methods, see Volume II) or the "non-stiff" and "stiff" components (partitioned or compound methods) of the differential equation.

For notational convenience we consider the system (14.2) as being partitioned into two components. An extension to more components is straightforward. For a better understanding of how the elementary differentials and trees should be defined, we first look at the derivatives of the exact solution of (14.2).

# Derivatives of the exact solution, P-trees

In order to avoid sums and unnecessary indices we assume that $y _ { a }$ and $y _ { b }$ in (14.2) are scalar quantities. All subsequent formulas remain valid for vectors if the derivatives are interpreted as multilinear mappings. Differentiating (14.2) and inserting (14.2) again for the derivatives we obtain for thefirst component $y _ { a }$

$$
\begin{array} { r l } & { \boldsymbol { y } _ { a } ^ { ( 1 ) } = f _ { a } } \\ & { \boldsymbol { y } _ { a } ^ { ( 2 ) } = \frac { \partial f _ { a } } { \partial y _ { a } } f _ { a } + \frac { \partial f _ { a } } { \partial y _ { b } } f _ { b } } \\ & { \boldsymbol { y } _ { a } ^ { ( 3 ) } = \frac { \partial ^ { 2 } f _ { a } } { \partial y _ { a } ^ { 2 } } ( f _ { a } , f _ { a } ) + \frac { \partial ^ { 2 } f _ { a } } { \partial y _ { b } \partial y _ { a } } ( f _ { b } , f _ { a } ) } \\ & { + \left. \frac { \partial f _ { a } } { \partial y _ { a } } \frac { \partial f _ { a } } { \partial y _ { a } } f _ { a } + \frac { \partial f _ { a } } { \partial y _ { a } } \frac { \partial f _ { a } } { \partial y _ { b } } f _ { b } + \frac { \partial ^ { 2 } f _ { a } } { \partial y _ { a } \partial y _ { b } } ( f _ { a } , f _ { b } ) \right. } \\ & { \left. + \frac { \partial ^ { 2 } f _ { a } } { \partial y _ { b } ^ { 2 } } ( f _ { b } , f _ { b } ) + \frac { \partial f _ { a } } { \partial y _ { b } } \frac { \partial f _ { b } } { \partial y _ { a } } f _ { a } + \frac { \partial f _ { a } } { \partial y _ { b } } \frac { \partial f _ { b } } { \partial y _ { b } } f _ { b } \right. . } \end{array}
$$

Similar formulas hold for the derivatives of $y _ { b }$

For a graphical representation of these formulas we need two different kinds of vertices. As in Section II.13 we use "meagre" and "fat" vertices, which will correspond to $f _ { a }$ and $\boldsymbol { f } _ { b }$ , respectively. For-mulas (14.3) can then be represented as shown in Figure 14.1.

![](images/9d148a2b39354ccea5815d1e03109cea4990f1e8cbbe9ce36e08fec4004cf4fa.jpg)  
Figure 14.1. The derivatives of the exact solution $y _ { a }$

The formal definition of these graphs is given by

Definition 14.1. A labelled P-tree of order $q$ is a labelled tree (see Definition 2.2)

$$
i : A _ { q } - \{ j \} \to A _ { q }
$$

together with a mapping

$$
t ^ { \prime } : A _ { q }  \{ ^ { \prime \prime } { \mathrm { m e a g r e } } ^ { \prime \prime } , \ ^ { \prime \prime } { \mathrm { f a t } } ^ { \prime } \} .
$$

We denote by $L T P _ { q } ^ { u }$ the set of those labelled P-trees of order $q$ ， whose root is meagre (i.e. t'(j)="meagre"). Similarly, $L T P _ { q } ^ { b }$ is the set of $q$ -th order labelled P-trees with a "fat" root.

The second and fifth expressions in (14.3.3) are equal. We there-fore define

Definition 14.2. Two labelled P-trees $( t , t ^ { \prime } )$ and $( \boldsymbol { u } ~ , \boldsymbol { u } ~ ^ { \prime } )$ are equivalent, if they have the same order, say $q$ ， and if there exists a bijection $\sigma : A _ { q }  A _ { q }$ such that $\sigma \left( j \right) = j$ and the following diagram commutes:

$$
\begin{array}{c} \begin{array} { l } { { A _ { q } - \{ j \} \xrightarrow { \quad t \quad } = A _ { q } \bigcap _ { q } ^ { \quad t ^ { \prime } } } } \\ { { \ A _ { q } ^ { \quad } = \bigcup _ { q = \lfloor j \rfloor } ^ { \quad t } \underbrace { \left| _ { \sigma } ^ { \quad t ^ { \prime } } \right. } _ { \quad u _ { q } ^ { \quad } = A _ { q } ^ { \quad } } \bigcap _ { u ^ { \prime } } ^ { \quad t ^ { \prime } } } } \end{array} \{array \left\{ { \mathrm { " m e a g r e " , " f a t " } } \right\}   \end{array}
$$

Definition 14.3. An equivalence class of $q$ -th order labelled Ptrees is called a $P$ -tree of order $q$ The set of all P-trees of order g itha e rtiy $T P _ { . } ^ { a }$ that with fat rboy $T P _ { \_ q } ^ { b }$ $\ell$ $\propto ( t )$ number of elements in the equivalence class t.

Exam ples of P-trees together with the numbers $\boldsymbol \rho ( t )$ and $\mathbf { \boldsymbol { a } } \left( t \right)$ 3re given in Table 14.1 below. We first discuss a recursive representation of P-trees (extension of Definition 2.12), which is fundamental for the following theory.

Definition 14.4. Let $t _ { 1 } , \ldots , t _ { m }$ be P-trees. We then denote by

$$
t = _ { a } [ t _ { 1 } , \dots , t _ { m } ] \ .
$$

the unique P-tree1 such that the rootis "meagre"and the P-trees $\boldsymbol { \ t } _ { 1 } ,$ $\cdots , t _ { m }$ remain if the root and the adjacent branches are chopped off. Similarly, we denote by $\mathbf { \Omega } _ { b } \{ t _ { 1 } , \dots , t _ { m } \}$ the P-tree whose new root is "fat" (see Figure 14.2). We further denote by $\tau _ { a }$ and $\tau _ { b }$ the meagre and fat P-trees of order one.

![](images/c09927689fe5c0e412ac9d5034cf9f4607e967671404a645b7ab7c60d459c4de.jpg)  
Figure 14.2. Recursive definition of P-trees

Our next aim is to make precise the connection between P-trees and the expressions of the Formulas (14.3). For this we use the notation

$$
w \left( t \right) = \left\{ \begin{array} { l l } { a } & { \qquad \mathrm { i f ~ t h e ~ r o o t ~ o f ~ } t \mathrm { ~ i s ~ m e a g r e , } } \\ { b } & { \qquad \mathrm { i f ~ t h e ~ r o o t ~ o f ~ } t \mathrm { ~ i s ~ f a t . } } \end{array} \right.
$$

Definition 14.5. The elementary differentials, corresponding to (14.2), are defined recursively by $( \boldsymbol { y } = ( y _ { a } , y _ { b } )$ ）

and

$$
\begin{array} { r l } & { F ( \tau _ { a } ) ( y ) = f _ { a } ( y ) } \\ & { F ( \tau _ { b } ) ( y ) = f _ { b } ( y ) } \\ & { F ( t ) ( y ) = \cfrac { \partial ^ { m } f _ { w ( t ) } ( y ) } { \partial y _ { w ( t _ { 1 } ) } \cdot \cdot \cdot \partial y _ { w ( t _ { m } ) } } \cdot \big ( F ( t _ { 1 } ) ( y ) , . . . , F ( t _ { m } ) ( y ) \big ) } \end{array}
$$

for ${ \mathfrak { s } } = _ { a } [ t _ { 1 } , \dots , t _ { m } ]$ or t=blt1....,tm].

Elementary diferentials for P-trees up to order 3 are given explicitly in Table 14.1.

We now return to the starting-point of this section and continue the differentiation of Formulas (14.3). Using the notation of labelled P-trees, one sees that a differentiation of $F ( t ) ( y _ { a } , y _ { b } )$ can be interpreted as an addition of a new branch with a meagre or fat vertex and a new summation letter to each vertex of the labelled P-tree t. In the same way as we proved Theorem 2.6 for non-partitioned differential equations, we arrive at

Theorem 14.6. The derivatives of the exact solution of (14.2) satisfy

$$
\begin{array} { l } { { y _ { a } ^ { ( q ) } = \displaystyle \sum _ { t \in L T P _ { q } ^ { a } } F ( t ) ( y _ { a } , y _ { b } ) = \displaystyle \sum _ { t \in T P _ { q } ^ { a } } \alpha ( t ) F ( t ) ( y _ { a } , y _ { b } ) ~ ( y _ { a } , y _ { b } ) ~ , } } \\ { { y _ { b } ^ { ( q ) } = \displaystyle \sum _ { t \in L T P _ { q } ^ { b } } F ( t ) ( y _ { a } , y _ { b } ) = \displaystyle \sum _ { t \in T P _ { q } ^ { b } } \alpha ( t ) F ( t ) ( y _ { a } , y _ { b } ) ~ . } } \end{array}
$$

Table 14.1. P-trees and their elementary differentials   

<table><tr><td>P-tree</td><td>repr. (14.4)</td><td></td><td>p（）α(）</td><td> elementary differential</td></tr><tr><td></td><td>T 副</td><td>1</td><td>1</td><td>fa afafa</td></tr><tr><td></td><td>altql</td><td>2</td><td>1</td><td>aya</td></tr><tr><td></td><td>alt6]</td><td>2</td><td>1</td><td>afafb ayb a²5a</td></tr><tr><td>&lt;</td><td>alta,Ta]</td><td>3</td><td>1</td><td>(a,fa) 2</td></tr><tr><td>√</td><td>a[Ta,Tb]</td><td>3</td><td>2</td><td>-(fafb) ayaoyb 8f</td></tr><tr><td></td><td>a[T6,T6]</td><td>3</td><td>1</td><td>(fb,fb) y</td></tr><tr><td>&lt;</td><td>alalTall</td><td>3</td><td>1</td><td>afa afafa dya aya</td></tr><tr><td></td><td>ala[7b1]</td><td>3</td><td>1</td><td>afaofafb ayaayb</td></tr><tr><td></td><td>alb[7al]</td><td>3</td><td>1</td><td></td></tr><tr><td>！</td><td>al6[7611</td><td>3</td><td>1</td><td>ayb aya afaofbfb</td></tr><tr><td></td><td></td><td>：</td><td></td><td>ayayb</td></tr><tr><td>·</td><td>Tb</td><td>1</td><td>1</td><td>f</td></tr><tr><td></td><td>b[Ta]</td><td>2</td><td>1</td><td>afbfa aya</td></tr><tr><td>-</td><td>b[61</td><td>2</td><td>1</td><td>asbfb ayb</td></tr></table>

# P-series

In Section II.11 we saw the importance of the key-lemma Corollary 11.7 for the derivation of the order conditions for RK-methods. Therefore we extend this result also to partitioned ordinary differential equations.

It is convenient to introduce two new P-trees of order 0, namely $\scriptstyle { \mathcal { D } } _ { a }$ and $\mathcal { D } _ { b }$ The corresponding elementary differentialsare $F ( { \mathcal { O } } _ { a } ) ( y ) { = } y _ { a }$ and $F ( \mathcal { O } _ { b } ) ( y ) { = } y _ { b }$ . We further set

$$
\begin{array} { c } { { T P ^ { a } = \{ \mathcal { O } _ { a } \} \cup T P _ { 1 } ^ { a } \cup T P _ { 2 } ^ { a } \cup \cdots } } \\ { { { } } } \\ { { T P ^ { b } = \{ \mathcal { O } _ { b } \} \cup T P _ { 1 } ^ { b } \cup T P _ { 2 } ^ { b } \cup \cdots } } \\ { { { } } } \\ { { L T P ^ { a } = \{ \mathcal { O } _ { a } \} \cup L T P _ { 1 } ^ { a } \cup L T P _ { 2 } ^ { a } \cup \cdots } } \\ { { { } } } \\ { { L T P ^ { b } = \{ \mathcal { D } _ { b } \} \cup L T P _ { 1 } ^ { b } \cup L T P _ { 2 } ^ { b } \cup \cdots \ . } } \end{array}
$$

Definition 14.7. Let ${ \mathbf { c } } ( \mathcal { O } _ { a } )$ ）， $\mathbf { c } ( \mathcal { O } _ { b } )$ ， $\mathbb { c } ( \tau _ { a } )$ ， $\mathbf { c } ( \tau _ { b } ) , \ldots$ be real coef-ficients defined for al P-trees c : $T P ^ { a } \cup T P ^ { b } \scriptscriptstyle \to \mathbb { R }$ .The series

$$
P ( \mathbf { c } , y ) = \left( P _ { \alpha } ( \mathbf { c } , y ) , P _ { b } ( \mathbf { c } , y ) \right) ^ { T }
$$

where

$$
\begin{array} { l } { { P _ { a } ( \mathbf { c } , y ) = \displaystyle \sum _ { t \in L T P ^ { a } } \frac { h ^ { \mathsf { p } ( t ) } } { \mathsf { p } ( t ) ! } \mathbf { c } ( t ) F ( t ) ( y ) } } \\ { { P _ { b } ( \mathbf { c } , y ) = \displaystyle \sum _ { t \in L T P ^ { b } } \frac { h ^ { \mathsf { p } ( t ) } } { \mathsf { p } ( t ) ! } \mathbf { c } ( t ) F ( t ) ( y ) } } \end{array}
$$

is then called a $P$ -series.

Theorem 14.6 simply states that the exact solution of (14.2) is a P-series

$$
\left( y _ { a } ( x _ { 0 } \mathbf { + } h ) , y _ { b } ( x _ { 0 } \mathbf { + } h ) \right) ^ { T } = P \left( \mathbf { y } , \left( y _ { a } ( x _ { 0 } ) , y _ { b } ( x _ { 0 } ) \right) \right)
$$

with $\mathbf { y } ( t ) = \boldsymbol { 1 }$ for all P-trees t.

Theorem 14.8. Let c: $T P ^ { a } \cup T P ^ { b } \scriptscriptstyle { \to } \mathbb { R }$ be a sequence of coefficients such that $\begin{array} { r } { { \bf c } ( \mathcal { D } _ { a } ) { = } { \bf c } ( \mathcal { D } _ { b } ) { = } 1 . } \end{array}$ Then

$$
\begin{array} { r l } { h \left( \begin{array} { l } { f _ { a } ( P \left( \mathbf { c } , ( y _ { a } , y _ { b } ) ) \right) } \\ { f _ { b } ( P \left( \mathbf { c } , ( y _ { a } , y _ { b } ) ) \right) } \end{array} \right) } & { = P \left( \mathbf { c } ^ { \prime } , ( y _ { a } , y _ { b } ) \right) } \end{array}
$$

with

$$
\begin{array} { l l l } { { \mathfrak { c } ^ { \prime } ( \mathcal { Q } _ { a } ) = \mathfrak { c } ^ { \prime } ( \mathcal { Q } _ { b } ) = 0 } } & { { } } & { { } } \\ { { \mathfrak { c } ^ { \prime } ( \tau _ { a } ) = \mathfrak { c } ^ { \prime } ( \tau _ { b } ) = 1 } } & { { } } & { { ( 1 4 . 8 ) } } \\ { { \mathfrak { c } ^ { \prime } ( t ) = \mathsf { p } ( t ) \mathfrak { c } ( t _ { 1 } ) \cdot \cdot \cdot \mathfrak { c } ( t _ { m } ) } } & { { \mathrm { i f } } } & { { t = _ { a } [ t _ { 1 } , . . . , t _ { m } ] o r t = _ { b } [ t _ { 1 } , . . . , t _ { m } ] } } \end{array}
$$

The proof is related to that of Theorem 11.6. It is given with more details in Hairer (1981). QED.

We now apply the result of Theorem 14.8 to the situations mentioned at the beginning of this section.

# RK-methods violating (1.9)

For the non-autonomous differential equation $y ^ { \prime } { = } f \left( x \ , y \right)$ we consider the RK-method (1.8). We do not assume (1.9), so that the $x$ and y components are integrated differently. Thus we add $x \ ^ { \prime } { = } 1$ to the differential equation and obtain

$$
\begin{array} { l } { { y ^ { \prime } = f \left( x , y \right) } } \\ { { \ } } \\ { { x ^ { \prime } = 1 } } \end{array}
$$

This is of the form (14.2), if we put $y _ { _ a } = y , y _ { b } = x , f _ { _ a } ( y _ { _ a } , y _ { \bar { b } } ) = f ( x , y )$ and ${ f } _ { b } ( y _ { a } , y _ { b } ) = 1$ . Since $f _ { b }$ is a constant, all elementary differentials that involve derivatives of $f _ { b }$ vanish identically. Thus, P-trees where at least one fat vertex is not an end-vertex need not be considered. It remains to treat the set

For the derivation of the order conditions of the RK-method

$$
\begin{array} { l } { { k _ { i } ~ = ~ h f \left( x _ { 0 } { + } c _ { i } h , g _ { i } \right. } } \\ { { \left. g _ { i } ~ = ~ y _ { 0 } ~ { + } ~ { \sum _ { j } } a _ { i j } k _ { j } \right. } } \\ { { \left. y _ { 1 } ~ { = } ~ y _ { 0 } ~ { + } ~ { \sum _ { i } } b _ { i } k _ { i } \right. } } \end{array}
$$

we assume $k _ { i }$ and $\boldsymbol { \mathbf { \mathit { \varepsilon } } } _ { \boldsymbol { \mathbf { \mathit { \varepsilon } } } _ { i } }$ to be the first components of P-series

$$
k _ { i } = P _ { a } ( \mathbf { k } _ { i } , ( y _ { 0 } , x _ { 0 } ) ) ~ , ~ g _ { i } = P _ { a } ( \mathbf { g } _ { i } , ( y _ { 0 } , x _ { 0 } ) ) ~ .
$$

We also let

$$
x _ { 0 } + c _ { i } h \ = P _ { b } ( { \bf g } _ { i } , ( y _ { 0 } , x _ { 0 } ) ) \ ,
$$

so that $\mathbf { g } _ { i } ( \mathcal { D } _ { b } ) { = } 1$ ， $\mathbf { g } _ { i } ( \tau _ { b } ) { = } c _ { i }$ and ${ \bf g } _ { i } \left( t \right) = 0$ for the remaining P-tres with a fat root. The RK-formula (14.11) together with Theorem 14.8 now leads to

$$
\begin{array} { l } { \mathbf { k } _ { i } ( t ) = \mathbf { g } _ { i } ^ { \prime } ( t ) } \\ { \mathbf { g } _ { i } ( t ) = \displaystyle \sum _ { j } a _ { i j } \mathbf { k } _ { j } ( t ) } \end{array}
$$

for $t \in T _ { x }$ This defines the coefficients $\mathbf { k } _ { i } ( t )$ recursively and we obtain the order conditions (for order $\boldsymbol { p }$ )as

$$
\sum _ { i } b _ { i } \mathbf { k } _ { i } ( t ) = 1 { \mathrm { ~ f o r ~ } } t \in T _ { x } \ , \ \rho ( t ) \leq p \ ,
$$

We see that the usual order conditions drop out, with the exception that $\Sigma _ { j }$ $a _ { i j }$ is replaced by $c _ { i }$ at fat nodes.

![](images/ab863cac553d22ca4b3a5bce2ed633ac5f017ae00a803dccb57ab1207db68bc7.jpg)  
Figure 14.3. Elements of $T _ { x }$

In Figure 14.3 we present the first elements of $T _ { x }$

Example. The Condition (14.13) for the 5-th, 8-th and last Ptree of Figure 14.3 reads

$$
\begin{array} { c } { { 3 \displaystyle \sum _ { i , j } b _ { i } c _ { i } a _ { i j } = 1 } } \\ { { } } \\ { { 3 . 2 \displaystyle \sum _ { i , j } b _ { i } a _ { i j } c _ { j } = 1 } } \\ { { } } \\ { { 6 \cdot 3 \cdot 2 \displaystyle \sum _ { i , j , k , l } b _ { i } a _ { i j } c _ { j } a _ { j k } a _ { i l } c _ { l } = 1 ~ , } } \end{array}
$$

# Fehlberg methods

If for the exact solution of $y \ ^ { \prime } { = } f \left( x \ , y \right)$ we have that $y \left( x _ { 0 } \right)$ ， $y ^ { \prime } ( x _ { 0 } )$ ， $\scriptstyle \cdots , y ^ { ( m ) } ( x _ { 0 } ) = 0$ vanish at ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ ，then $f$ ， $\partial f / \partial x , . . . , \partial ^ { m - 1 } f / \partial x ^ { m - 1 }$ vanish at $( x _ { 0 } , y _ { 0 } )$ (see Section II.13, methods of Fehlberg). For this case we give the elements of $T _ { x }$ ， whose elementary diferentials do not in general vanish at $( x _ { 0 } , y _ { 0 } )$ , in Figure 14.4.

![](images/7de7f1eec7adb642d2a553bcbfd8c7a88efb982f0eec88df339456f82a1c1db5.jpg)  
Figure 14.4. P-trees, to be considered for the methods of Fehlberg (Section IL.12)

# Nystrom methods

As a last application of Theorem 14.8 we present a new derivation of the order conditions for Nystrom methods (Section I1.13). The second order differential equation $y ~ ^ { \prime \prime } { = } f \left( y \ , y \ ^ { \prime } \right)$ can be written in partitioned form as

$$
{ \left( \begin{array} { l } { y } \\ { y ^ { \prime } } \end{array} \right) } ^ { \prime } = { \left( \begin{array} { l } { y ^ { \prime } } \\ { f \left( y , y \right) } \end{array} \right) } ~ .
$$

In the notation of (14.2) we have $y _ { _ a } = y , y _ { b } = y ^ { \prime } , f _ { _ a } ( y _ { _ { a } } , y _ { _ b } ) = y _ { _ b }$ $f _ { b } ( y _ { a } , y _ { b } ) { = } f ( y _ { a } , y _ { b } )$ . The special structure of $f _ { a }$ implies that only Ptrees which satisfy the condition (see Definition 13.2)

"meagre vertices have at most one son and this son has to be fat"

have to be considered. The essential P-trees are thus

$$
\begin{array} { l r } { { T N _ { q } ^ { a } = \{ t \in T P _ { q } ^ { a } ; t \mathrm { ~ s a t i s f i e s ~ } ( 1 4 . 1 5 ) \} } } \\ { { T N _ { q } ^ { b } = \{ t \in T P _ { q } ^ { b } ; t \mathrm { ~ s a t i s f i e s ~ } ( 1 4 . 1 5 ) \} \ . } } \end{array}
$$

It follows that each element of TN& $T N _ { q + 1 } ^ { u }$ can be written as $t = \int _ { a } \ d u ]$ with $u \in T N _ { a } ^ { b }$ This implies a one-to-one correspondence between $T N _ { q + 1 } ^ { a }$ and $T { \tilde { N } } _ { q } ^ { b }$ , leaving the elementary differentials invariant:

$$
F \left( { } _ { a } [ u ] \right) ( y _ { a } , y _ { b } ) = \frac { \partial y _ { b } } { \partial y _ { b } } { \cdot } F ( u ) ( y _ { a } , y _ { b } ) = F ( u ) ( y _ { a } , y _ { b } ) .
$$

From this property it follows that

$$
\begin{array} { r } { h P _ { b } ( \mathfrak { c } , ( y _ { a } , y _ { b } ) ) = P _ { a } ( \mathfrak { c } ^ { \prime } , ( y _ { a } , y _ { b } ) ) \quad \mathrm { ~ w h e r e ~ } } \\ { \mathfrak { c } ^ { \prime } ( t ) = \mathfrak { p } ( t ) \mathfrak { c } ( u ) \quad \quad \mathrm { ~ i f ~ } \quad t = \mathfrak { _ { a } } [ u ] . } \end{array}
$$

This notation is in agreement with (14.8).

The order conditions of Method (13.13) can now be derived as follows: assume $g _ { i } \circ g _ { i } ^ { \prime }$ to be P-series

$$
g _ { i } = P _ { a } ( { \bf c } _ { i } , ( y _ { 0 } , y _ { 0 } ^ { } ) ) ~ , \qquad g _ { i } ^ { \prime } = P _ { b } ( { \bf c } _ { i } , ( y _ { 0 } , y _ { 0 } ^ { } ) ) ~ .
$$

Theorem 14.8 then implies

$$
h f \left( g _ { i } , g _ { i } ^ { \prime } \right) = P _ { b } ( \mathbf { c } _ { i } ^ { \prime } , ( y _ { 0 } , y _ { 0 } ^ { \prime } ) ) \ .
$$

Multiplying this relation by $h$ it follows from (14.17) that

$$
h ^ { 2 } f \left( g _ { i } , g _ { i } ^ { \prime } \right) = P _ { a } ( \mathbf { c } _ { i } ^ { \prime \prime } , ( y _ { 0 } , y _ { 0 } ^ { \prime } ) ) \ .
$$

Here ${ \mathfrak { c } } _ { i } ^ { \prime \prime } = ( \mathbf { c } _ { i } ^ { \prime } ) ^ { \prime } ,$ i.e.

$$
\begin{array} { l l l l l l l } { { \mathfrak { c } _ { i } ^ { \prime \prime } ( t ) = 0 } } & { { \mathrm { f o r } t = \varnothing _ { a } \mathrm { a n d } t = \mathfrak {tau } _ { a } } } & { { } } & { { } } & { { } } & { { } } \\ { { \mathfrak { c } _ { i } ^ { \prime \prime } ( { } _ { a } [ \tau _ { b } ] ) = 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \mathfrak { c } _ { i } ^ { \prime \prime } ( t ) = \mathsf { p } ( t ) \big ( \mathsf { p } ( t ) { - } 1 \big ) \mathfrak { c } _ { i } ( t _ { 1 } ) \cdot \cdot \cdot \mathfrak { c } _ { i } ( t _ { m } ) } } & { { \mathrm { i f } } } & { { } _ { t } = { } _ { a } [ { } _ { b } [ t _ { 1 } , \ldots , t _ { m } ] ] }  \end{array}
$$

The relations (14.18) and (14.19), when inserted into (13.13) yield, as usual, the recurrence relations

$$
\begin{array} { r l } & { \mathfrak { c } _ { i } ( { \tau _ { a } } ) = c _ { i } ~ , } \\ & { \mathfrak { c } _ { i } ( t ) = \sum _ { j } \overline { { a } } _ { i j } \mathfrak { c } _ { j } ^ { \prime \prime } ( t ) \mathrm { i f ~ t h e ~ r o o t ~ i s ~ m e a g r e } , } \\ & { \mathfrak { c } _ { i } ( t ) = \sum _ { j } a _ { i j } \mathfrak { c } _ { j } ^ { \prime } ( t ) \mathrm { i f ~ t h e ~ r o o t ~ i s ~ f a t } . } \end{array}
$$

In exactly the same way one gets the order conditions (for order $p$ ）

$$
\begin{array} { r l r } { \sum _ { i } \tilde { b _ { i } } \mathbf { c } _ { i } ^ { \prime \prime } ( t ) = 1 } & { } & { \mathrm { f o r } ~ t \in T N _ { q } ^ { a } ~ , ~ q = 2 , \dots , p ~ ; } \\ { \sum _ { i } b _ { i } \mathbf { c } _ { i } ^ { \prime } ( t ) = 1 } & { } & { \mathrm { f o r } ~ t \in T N _ { q } ^ { b } ~ , ~ q = 1 , \dots , p ~ . } \end{array}
$$

# Exercises

1. Denote the number of elements of ${ \underline { { T } } } { P _ { q } ^ { u } }$ (P-trees with meagre root of order $q$ ) by $\alpha _ { q }$ (see Table 14.2). Prove that

$$
\mathfrak a _ { 1 } + \mathfrak a _ { 2 } \boldsymbol x \ + \mathfrak a _ { 3 } \boldsymbol x ^ { 2 } + \cdot \cdot \cdot = { ( 1 - \boldsymbol x ) } ^ { - 2 \alpha _ { 1 } } { ( 1 - \boldsymbol x ^ { 2 } ) } ^ { - 2 \alpha _ { 2 } } { ( 1 - \boldsymbol x ^ { 3 } ) } ^ { - 2 \alpha _ { 3 } } \cdot \cdot \cdot
$$

Compute the first ${ \mathfrak { a } } _ { q }$ and compare them with the $a _ { q }$ of Table 2.2.

Table 14.2. Number of elements of TPg   

<table><tr><td>q</td><td>α 9</td><td>q</td><td>α 9</td></tr><tr><td>1</td><td>1</td><td>6</td><td>458</td></tr><tr><td>2</td><td>2</td><td>7</td><td>2058</td></tr><tr><td>3</td><td>7</td><td>8</td><td>9498</td></tr><tr><td>4</td><td>26</td><td>9</td><td>44947</td></tr><tr><td>5</td><td>107</td><td>10</td><td>216598</td></tr></table>

2. There is no explicit, 4-stage RK-method of order 4, which does not satisfy condition (1.9). Hint. Use the techniques of the proof of Lemma 1.4.   
3. Show that the order conditions (14.20) are the same as those given in Theorem 13.10.

# I1.15. Delay differential equations

"Detailed studies of the real world impel us, albeit reluctantly, to take account of the fact that the rate of change of physical systems depends not only on their present state, but also on their past history."

(Bellman - Cooke, 1963)

Delay differential equations are equations with "retarded arguments" or "time lags" such as

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , y \left( x - \tau \right) \right)
$$

or

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , y \left( x - \tau _ { 1 } \right) , y \left( x - \tau _ { 2 } \right) \right)
$$

or of even more general form. Here the derivative of the solutions depends also on its values at previous points.

Time lags are present in many models of applied mathematics. They can also be the source of interesting m athematical phenomena such as instabilities, limit cycles, periodic behaviour.

# Existence

For equations of the type (15.1) or (15.2), where the delay values $x - \tau$ are bounded away from $x$ by a positive constant, the question of existence is an easy matter: suppose that the solution is known, say

$$
y \left( x \right) = \Phi ( x ) \quad \mathrm { ~ f o r ~ } \quad x _ { 0 } - \tau \leq x \leq x _ { 0 } .
$$

Then $y \left( x - \tau \right)$ is a known function of $x$ for ${ x \mid } _ { 0 } \leq x \leq { x \mid } _ { 0 } + \tau$ and (15.1) becomes an ordinary differential equation， which can be treated by known existence theories. We then know $y \left( x \right)$ for ${ x \mid } _ { 0 } \leq x \leq { x \mid } _ { 0 } + { \tau }$ and can compute the solution for $x _ { 0 } { + } \tau \leq x \leq x _ { 0 } { + } 2 \tau$ and so on. This "method of steps" then yields existence and uniqueness results for all $x$ . For more details we recommend the books of Bellman-Cooke (1963) and Driver (1977, especially Chapter V).

Example 1. We consider the equation

$$
y ^ { \prime } ( x ) = - y ( x { - } 1 ) ~ , ~ y ( x ) = 1 ~ \mathrm { f o r } { - } 1 { \leq x \leq 0 } ~ .
$$

Proceeding as described above, we obtain

$$
\begin{array} { l c l } { y \left( x \right) = 1 - x } & { \mathrm { ~ f o r ~ } } & { 0 \leq x \leq 1 } \\ { y \left( x \right) = 1 - x + \displaystyle \frac { \left( x - 1 \right) ^ { 2 } } { 2 ! } } & { } & { \mathrm { ~ f o r ~ } 1 \leq x \leq 2 } \end{array}
$$

$$
y \left( x \right) = 1 - x + \frac { \left( x - 1 \right) ^ { 2 } } { 2 ! } - \frac { \left( x - 2 \right) ^ { 3 } } { 3 ! } \mathrm { f o r } 2 \leq x \leq 3 \mathrm { e t c } .
$$

The solution is displayed in Figure 15.1. We observe that despite the fact that the differential equation and the initial function are $C ^ { \infty }$ ,the solution has discontinuities in its derivatives. This results from the fact that the initial function does not satisfy the diferential equation. With every time step $\boldsymbol { \tau }$ , however, these discontinuities are smoothed out more and more.

![](images/2e03e27619eeaa83404eccfc297a2d76435e4d2d4a0d304316304d670cc1afc9.jpg)  
Figure 15.1. Solution of (15.3)

Example 2. Our next example clearly illustrates the fact that the solutions of a delay equation depend on the entire history between ${ { x } _ { 0 } } \mathrm { { - } } \tau$ and $x _ { 0 } ,$ and not only on the initial value:

$$
\begin{array} { r l } { y ^ { \prime } ( x ) = - 1 . 4 \cdot y ( x - 1 ) } & { } \\ { \mathrm { a ) } } & { \phi ( x ) = 0 . 8 \quad \mathrm { f o r } \ - 1 { \leq x } { \leq 0 } \ , } \\ { \mathrm { b ) } } & { \phi ( x ) = 0 . 8 \ + \ x \quad \mathrm { f o r } \ - 1 { \leq x } { \leq 0 } \ , } \\ { \mathrm { c ) } } & { \phi ( x ) = 0 . 8 \ + 2 x \quad \mathrm { f o r } \ - 1 { \leq x } { \leq 0 } \ . } \end{array}
$$

The solutions are displayed in Figure 15.2. An explanation for the oscillatory behaviour of the solutions will be given below.

![](images/82f7db237e527ae41d5a480f195bd8ba5badd13a227218c982515007836920a9.jpg)  
Figure 15.2. Solutions of (15.4)

Constant step size methods for constant delay

If we apply the Runge-Kutta method (1.8) to a delay equation (15.1) we obtain

$$
\begin{array} { r l r } & { } & { \mathrm {  ~ g } _ { i } ^ { ( n ) } = y _ { n } + h \sum _ { j } a _ { i j } f \left( x _ { n } + c _ { j } h , g _ { j } ^ { ( n ) } , y \left( x _ { n } + c _ { j } h - \tau \right) \right) } \\ & { } & { y _ { n + 1 } = y _ { n } + h \sum _ { j } b _ { j } f \left( x _ { n } + c _ { j } h , g _ { j } ^ { ( n ) } , y \left( x _ { n } + c _ { j } h - \tau \right) \right) . } \end{array}
$$

But which values should we give to $y \left( x _ { n } + c _ { i } h - \tau \right) \bar { \zeta }$ If the delay is constant and satisfies $\tau = k h$ for some integer $\nmid$ , the most natural idea is to use the back-values of the old solution

$$
\begin{array} { r l r } & { } & { g _ { i } ^ { \mathbf { \Gamma } } = y _ { n } + h \sum _ { j } a _ { i j } f ( x _ { n } + c _ { j } h , g _ { j } ^ { \mathbf { \Gamma } } , \gamma _ { j } ^ { \mathbf { \Gamma } ( n ) } ) } \\ & { } & { y _ { n + 1 } = y _ { n } + h \sum _ { j } b _ { j } f ( x _ { n } + c _ { j } h , g _ { j } ^ { \mathbf { \Gamma } ( n ) } , \gamma _ { j } ^ { \mathbf { \Gamma } ( n ) } ) } \end{array}
$$

where

$$
\gamma _ { j } ^ { ( n ) } = { \left\{ \begin{array} { l l } { \phi ( x _ { n } + c _ { j } h - \tau ) } & { { \mathrm { ~ i f ~ } } n < k } \\ { g _ { j } ^ { ( n - k ) } } & { { \mathrm { ~ i f ~ } } n \geq k } \end{array} \right. } ,
$$

This can be interpreted as solving successively

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , \Phi ( x - \tau ) \right)
$$

for the interval $[ x _ { 0 } , x _ { 0 } + \tau ]$ then

$$
\begin{array} { l } { { y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , z \left( x \right) \right) } } \\ { { z ^ { \prime } ( x ) = f \left( x - \tau , z \left( x \right) , \Phi ( x - 2 \tau ) \right) } } \end{array}
$$

for the interval $\left[ x _ { 0 } { + } \tau , x _ { 0 } { + } 2 \tau \right] ,$ then

$$
\begin{array} { r l } & { y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , z \left( x \right) \right) } \\ & { z ^ { \prime } ( x ) = f \left( x - \tau , z \left( x \right) , \nu \left( x \right) \right) } \\ & { \nu ^ { \prime } ( x ) = f \left( x - 2 \tau , \nu \left( x \right) , \phi ( x - 3 \tau ) \right) } \end{array}
$$

for the interval $[ x _ { 0 } + 2 \tau , x _ { 0 } { + } 3 \tau ]$ ，and so on. This is the perfect numerical analog of the "method of steps" mentioned above.

Theorem 15.1. If $c _ { i } , a _ { i j } , b _ { j }$ are the coefficients of a $p$ -th order Runge-Kutta method,then (15.5) is convergent of order p.

Proof: The sequence (15.1a), (15.1b),.. are ordinary differential equations normally solved by a $p$ -th order RK method. Therefore the result follows im mediately from Theorem 3.6. QED.

R emark. For the collocation method based on Gaussian quadrature formula, Theorem 15.1 gives the superconvergence result of Bellen (1984).

Numerical Example. We have integrated the Problem (15.12) below for $0 \leq x \leq 1 0$ with $a = 1 . 4$ , initial values $y \left( x \right) = 0$ ， $- 1 \leq x < 0$ ， $y \left( 0 \right) { = } 0 . 1$ ， and step sizes $h = 1$ , 1/2, 1/4, 1/8,.. using Butcher's method (Table 6.1) of order 6. The numerical results are presented in Table 15.1. The 6-th order convergence can clearly be observed.

Table 15.1. Numerical results for Method (15.5)   

<table><tr><td>h</td><td> nr. steps</td><td> nr. f-eval.</td><td> maximal error</td></tr><tr><td>1</td><td>10</td><td>70</td><td>1.69×10-2</td></tr><tr><td>1/2</td><td>20</td><td>140</td><td>4.76×10-4</td></tr><tr><td>1/4</td><td>40</td><td>280</td><td>4.76x10-6</td></tr><tr><td>1/8</td><td>80</td><td>560</td><td>7.80×10-8</td></tr><tr><td>1/16</td><td>160</td><td>1120</td><td>8.90×10-10</td></tr><tr><td>1/32</td><td>320</td><td>2240</td><td>2.14×10-11</td></tr><tr><td>1/64</td><td>640</td><td>4480</td><td>3.41×10-13</td></tr></table>

# Variable step size methods

Unfortunately, Method (15.5) does not allow us to change the step size arbitrarily, and an application to variable delay equations is not straightforward. If complete flexibility is desired, we need a global approximation to the solution. There is no use in having approximations only at a sequence of points. Therefore, choice methods for these problems are multistep methods of Adams or BDF type (see Chapter III.1) or continuous Runge-Kutta methods. For the sake of easy programming, we have chosen the Dormand and Prince method of order 5(4) together with the formulas (5.7) in Section I1.5. The superiority of this procedure over many other interpolation methods has been shown in extensive numerical tests by Gottwald (1985). For each interval of integration, the solution is represented globally by a polynomial of degree 4. Therefore， after each successful step of integration, the subroutine RETARD (slight modification of DOPRI5) makes a call to subroutine STORE, which writes these coefficients, together with the corresponding $x$ values, into a memory (common block COEF). A call to the real function YLAG(I,X) then searches the correct interval for $x$ and evaluates the corresponding polynomial for the I-th solution. Therefore, a call to RETARD solves delay equations, say Equation (15.4), if the subroutine FCN reads as

$$
{ \bf F } ( { \bf 1 } ) = - 1 . 4 \ast \mathrm { { Y L A G } } ( 1 , { \bf X } - 1 . , { \bf P H I } ) \ .
$$

Codes for RETARD, STORE, and YLAG together with a sample calling program are given in the appendix. Figures 15.1 and 15.2 have been computed with these routines.

As we have seen, the solutions possess discontinuities in the derivatives at several points, e.g. for (15.1) at ${ { x } _ { 0 } } ^ { + \tau }$ ， $x _ { 0 } + 2 \tau$ ， $x _ { 0 } + 3 \tau , \dots$ etc. Therefore it improves precision and computation time if these points are singled out and the calls to RETARD are renewed at these discontinuities.

Some of the difficulties for sophisticated software for delay equations (more general than (15.1)) consists in finding all points of discontinuity up to a certain order and also in an economical management of memory for all the coefficients of the past solution and overwriting what is no longer needed.

# Characteristic values of exponential solutions

It can be observed from Figures 15.1 and 15.2 that the solutions, after the initial phase, seem to tend to something like $e ^ { \alpha x } \cos { \beta } ( x - 8 )$ We now try to determine α and β. We study the equation

$$
y ^ { \prime } ( x ) = \lambda y ( x ) + \mu y ( x - 1 ) ~ .
$$

There is no loss of generality in supposing the delay $\tau = 1$ ， since any delay $\tau \neq 1$ can be reduced to $\tau = 1$ by a coordinate change.

We search for a solution of the form

$$
y \left( x \right) = e ^ { \gamma x } \qquad \mathrm { w h e r e } \qquad \gamma = \ l \alpha + i \beta .
$$

Introducing this into (15.6) we obtain the following "characteristic equation" for $\gamma$

$$
\gamma - \lambda - \mu e ^ { - \gamma } = 0 ~ ,
$$

which, for $\mu \neq 0$ ， possesses an infinity of solutions: in fact, if $\{ \gamma \}$ becomes large, we obtain from (15.8)， since λ is fixed, that $\mu e ^ { - \gamma }$ must be large too and

$$
\begin{array} { r } { \gamma \approx \mu e ^ { - \gamma } . } \end{array}
$$

This implies that $\gamma = \alpha + i \beta$ is close to the imaginary axis. Hence $\left| \gamma \right| \approx \left| \mathsf { \mathsf { \mathsf { \mathsf { \beta } } } } \right|$ and from (15.8’)

$$
| \beta | \approx | \mu | e ^ { - \alpha } ~ .
$$

Therefore the roots of (15.8) lie asymptotically on the curves

$- \alpha = \log \left| \beta \ \right| { - } \log \left| \mu \right|$ . Again from (15.8’), we have a root whenever the argument of $\mu e ^ { - i \beta }$ is close to $\pi / 2$ (for $\beta > 0$ ),i.e.if

$$
{ \mathsf { \beta } } \approx \ \arg \mu - { \frac { \pi } { 2 } } + 2 k \pi \qquad k = 1 , 2 , \cdot \cdot \cdot
$$

There are thus two sequences of characteristic values which tend to infinity on logasithmic curves left of the imaginary axis, with $2 \pi$ as asymptotic distance between two consecutive values.

The "general solution" of (15.6) is thus a Fourier-like superposition of solutions of type (15.7) (Wright (1946), see also Bellman - Cooke (1963), Chapter 4). The smaller Rey is, the faster these solutions "die out" as $x  \infty$ . The dominant solutions are thus (provided that the corresponding coefficients are not zero) those which correspond to the largest real part, i.e. those closest to the origin. For Equations (15.3) and (15.4) the characteristic equations are $\gamma + e ^ { - \gamma } = 0$ and $\gamma + 1 . 4 e ^ { - \gamma } = 0$ with‘solutions $\gamma = - 0 . 3 1 8 1 3 \pm 1$ .33724iand $\gamma = - 0 . 0 8 1 7 0 \pm 1 . 5 1 6 9 9 i$ respectively, which explainsnicely the behaviour of the asymptotic solutions of Figure 15.1 and Figure 15.2.

For the case of matrix equations

$$
y ^ { \prime } ( x ) = A y \left( x \right) + B y \left( x - 1 \right)
$$

where A and $B$ are not simultaneously diagonalizable, we set $y \left( x \right) = y e ^ { \gamma x }$ where $\nu \neq 0$ is a given vector. The equation now leads to

$$
\gamma \nu ~ = A \nu ~ + B e ^ { - \gamma } \nu ,
$$

which has a nontrivial solution if

$$
\mathrm { d e t } \left( \gamma I - A - B e ^ { - \gamma } \right) = 0 \ ,
$$

the characteristic equation for the more general case. The shape of the solutions of $( 1 5 . 8 ^ { \prime \prime } )$ is similar to those of (15.8), there are just $r = \operatorname { r a n k } ( B )$ points in each strip of width $2 \pi$ instead of one.

# Stability

All solutions of (15.6) remain stable for $x \to \infty$ if all characteristic roots of (15.8) remain in the negative half plane. This result follows either from the above expansion theorem or from the theory of Laplace transforms (e.g. Bellmann - Cooke (1963), Chapter 1), which, in fact, is closely related.

In order to study the boundary of the stability domain, we search for $( \lambda , \mu )$ values for which the first solution $\gamma$ crosses the imaginary axis, i.e. $\gamma = i \ \theta$ for 0 real. If we insert this into (15.8), we obtain

$$
\begin{array} { l } { { \lambda = - \mu \qquad \mathrm { f o r } \ \theta = 0 \qquad \mathrm { ( \gamma \ r e a l ) } } } \\ { { \lambda = i \theta - \mu e ^ { - i \theta } \qquad \mathrm { f o r } \ \theta \not = 0 } } \end{array}
$$

![](images/89d30007ac16e5bd0b2561cddb0e54974db9c1e6d8fdc5f0518a7d5469e9963f.jpg)  
Figure 15.3. Domain of stability for y $' ( x ) = \lambda y ( x ) + \mu y ( x - 1 )$

or, by separating real and imaginary parts,

$$
\lambda = \frac { \cos { \theta } \cdot \theta } { \sin { \theta } } , \mu = - \frac { \theta } { \sin { \theta } }
$$

valid for real λ and $\mu _ { * }$ . These paths are sketched in Figure 15.3 and separate in the $( \lambda , \mu )$ -plane the domains of stability and instability for the solutions of (15.6) (a result of Hayes (1950)).

If we put $\scriptstyle { \Theta = \pi / 2 }$ ， we find that the solutions of $y \ ^ { \prime } ( x ) = \mu y \left( x - 1 \right)$ remain stable for

$$
- \frac { \pi } { 2 } \leq \mu \leq 0
$$

and unstable for

$$
\mu < - \frac { \pi } { 2 } \ \mathrm { a s ~ w e l l ~ a s ~ \mu > ~ 0 ~ } .
$$

# An example from population dynamics

"Lord Cherwell drew my attention to an equation, equivalent to (8) (here: (15.12)) with $a = \log 2$ ，which he had encountered in his application of probability methods to the problem of distribution of primes. My thanks are due to him for thus introducing me to an interesting problem".   
(E.M. Wright, 1945)

We now demonstrate the phenomena discussed above and the power of our programs on a couple of examples drawn from applications. For supplementary applications of delay equations to all sorts of sciences, consult the impressive list in Driver (1977, p.239-240).

Let $y \left( x \right)$ represent the population of a certain species, whose development as a function of time is to be studied. The simple model of infinite exponential growth $y ^ { \prime } { = } \lambda y$ was soon replaced by the hypothesis that the growth rate λ will decrease with increasing population y due to illness and lack of food and space. One then arrives at the model (Verhulst (1845), Pearl (1922))

$$
y ^ { \prime } ( x ) = k ( a - y ( x ) ) { \cdot } y ( x ) .
$$

Nous donnerons le nom logistique a la courbe caracterisee par l'equation precedente" (Verhulst). It can be solved by elementary functions (Exercise 1). All solutions with initial value $y _ { 0 } > 0$ tend asym ptotically to $^ a$ as $x \to \infty$ . If we assume the growth rate to depend on the population of the preceding generation, (15.10) becomes a deiay equation (Cunningham (1954)， Wright (1955)， Kakutani and Markus (1958))

$$
y ^ { \prime } ( x ) = k \left( a - y \left( x - \tau \right) \right) \cdot y \left( x \right) .
$$

Introducing the new function ${ \boldsymbol { z } } \left( { \boldsymbol { x } } \right) = { \boldsymbol { k } } \tau y \left( \tau { \boldsymbol { x } } \right)$ into (15.11) and again replacing $z$ by y and $k a \tau$ by $^ a$ we obtain

$$
y ^ { \prime } ( x ) = ( a - y ( x - 1 ) ) \cdot y ( x ) ~ .
$$

This equation has an equilibrium point at $y \left( x \right) = a$ . The substitution $y \left( x \right) = a + z \left( x \right)$ and linearization leads to the equation $z \prime ( x ) { = } { - } a z ( x - 1 )$ ， and Condition (15.9) shows that this equilibrium point is locally stable if $0 < a \le \pi / 2$ . Hence the characteristic equation, here $\gamma + a e ^ { - \gamma } = 0$ ， possesses two real solutions iff $a < 1 / e = 0 . 3 6 8$ ,which makes monotonic solutions possible; otherwise they are oscillatory. For $a > \pi / 2$ the equilibrium solution is unstable and gives rise to a periodic limit cycle.

The solutions in Figure 15.4 have again been computed by the codes RETARD, STORE, YLAG of the appendix with subroutine FCN as

![](images/9bbf7666d56ada4b0566fb19179ce836cf5dd0e44a9e5fd405987fc84f36c193.jpg)  
Figure 15.4. Solutions of the population dynamics problem (15.12)

# Infectious disease modelling

"De tous ceux qui ont traite cette matlere, c'est sans contredit M. de la Condamine qui I'a fait avec plus de succes. Il est deja venu a bout de persuader la meilleure partie du monde raisonnable de la grande utilite de l'inoculation: quant aux autres, il serait inutile de vouloir employer la raison avec eux: puisqu'ils n'agissent pas par principes. I faut les conduire comme des enfants vers leur mieux.." (Daniel Bernoulli, 1760)

Daniel Bernoulli ("Docteur en medecine, Professeur de Physique en 'Universite de Bale, Associe etranger de 1'Academie des Sciences") was the first to use differential calculus to model infectious diseases, in his 1760 paper on smalpox vaccination. At the beginning of our century， mathematical modelling of epidemics gained new interest. This finally led to the classical model of Kermack - McKendrick (1927): Iet $y _ { 1 } ( x )$ measure the susceptible portion of the population, $y _ { 2 } ( x )$ the infected, and $y _ { 3 } ( x )$ the removed (e.g. immunized) one. It is then natural to assume that the number of newly infected people per time unit is proportional to the product $y _ { 1 } ( x ) y _ { 2 } ( x )$ ， just as in bim olecular chemical reactions (see Section I.16). If we finally assume the number of newly removed persons to be proportional to the infected ones, we arrive at the model

$$
y _ { 1 } ^ { \prime } = - y _ { 1 } y _ { 2 } y _ { 2 } ^ { \prime } = y _ { 1 } y _ { 2 } - y _ { 2 } y _ { 3 } ^ { \prime } = y _ { 2 }
$$

where we have taken for simplicity all rate constants equal to one. This system can be integrated by elementary methods (divide the first two equations and solve $d y _ { 2 } / d y _ { 1 } { = } - 1 + 1 / y _ { 1 } )$ . The numerical solution with initial values $y _ { 1 } ( 0 ) { = } 5$ ， $y _ { 2 } ( 0 ) { = } 0 . 1$ ， $y _ { 3 } ( 0 ) { = } 0$ is plotted in Figure 15.5: an epidemic breaks out, everybody finally becomes "removed" and nothing further happens.

![](images/5bcee8d4c73feaed1043cb41f929c64bcea4d16aa884822d861cc46cf8bfb11a.jpg)  
Figure 15.5. Solution of Kermack - McKendrick model (15.13)

We arrive at a periodic outbreak of the disease, if we assume that immunised people become susceptible again, say after a fixed time $\boldsymbol { \tau }$ $( \tau = 1 0 )$ . If we also introduce an incubation period of, say, $\tau _ { 2 } { } ^ { = 1 }$ ，we arrive at the model

$$
\begin{array} { l l } { { y _ { 1 } ^ { \prime } ( x ) = - y _ { 1 } ( x ) y _ { 2 } ( x - 1 ) + y _ { 2 } ( x - 1 0 ) } } \\ { { \qquad } } \\ { { y _ { 2 } ^ { \prime } ( x ) = y _ { 1 } ( x ) y _ { 2 } ( x - 1 ) - y _ { 2 } ( x ) } } \\ { { \qquad } } \\ { { y _ { 3 } ^ { \prime } ( x ) = y _ { 2 } ( x ) - y _ { 2 } ( x - 1 0 ) } } \end{array}
$$

instead of (15.13). The solutions of (15.14), for the initial phases $y _ { 1 } ( x ) { = } 5$ $y _ { 2 } ( x ) { = } 0 . 1$ ， $y _ { 3 } ( x ) { = } 1$ for $x \leq 0$ , are shown in Figure 15.6 and illustrate the periodic outbreak of the disease.

![](images/10df4483b3baea73bb17c220e957f929cf30bd29cfe0114c57e38900188180ff.jpg)  
Figure 15.6. Periodic outbreak of disease, model (15.14)

# An example from enzyme kinetics

Our next example, more complicated than the preceding ones, is from enzyme kinetics (Okamoto - Hayashi (1984)). Consider the fol-lowing consecutive reactions

$$
1 \overrightarrow { 1 \cdot \tau ^ { * } Y _ { 2 } \cdot \tau _ { k _ { 2 } } } \overrightarrow { Y _ { 3 } \cdot \tau _ { k _ { 3 } } } \overrightarrow { Y _ { 4 } } \overrightarrow { k _ { 4 } }
$$

where / is an exogenous substrate supply which is maintained con-stant and n molecules of the end product $Y _ { 4 }$ inhibit co-operatively the reaction step of $\boldsymbol { Y } _ { 1 } \boldsymbol { * } \boldsymbol { Y } _ { 2 }$ as

$$
z \ = \frac { k _ { 1 } } { 1 + \alpha ( y _ { 4 } ( x ) ) ^ { n } } \ .
$$

It is generally expected that the inhibitor molecule must be moved to the position of the regulatory enzyme by forces such as diffusion or active transport. Thus, we consider this time consuming process causing time-delay and we arrive at the model

$$
{ \begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = I - z y _ { 1 } ( x ) } \\ & { y _ { 2 } ^ { \prime } ( x ) = z y _ { 1 } ( x ) - y _ { 2 } ( x ) } \\ & { y _ { 3 } ^ { \prime } ( x ) = y _ { 2 } ( x ) - y _ { 3 } ( x ) } \\ & { y _ { 4 } ^ { \prime } ( x ) = y _ { 3 } ( x ) - 0 . 5 y _ { 4 } ( x ) } \\ & { z = { \cfrac { 1 } { 1 + 0 . 0 0 0 5 \left( y _ { 4 } ( x - 4 ) \right) ^ { 3 } } } ~ . } \end{array} }
$$

This system possesses an equilibrium at $z y _ { 1 } { = } y _ { 2 } { = } y _ { 3 } { = } I , y _ { 4 } { = } 2 I$ ， $y _ { 1 } { = } I \left( 1 { + } 0 . 0 0 4 I ^ { 3 } \right) { = } { : } c _ { 1 }$ . When it is linearized in the neighbourhood of this equilibrium point, it becomes

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = - c _ { 1 } y _ { 1 } ( x ) + c _ { 2 } y _ { 4 } ( x - 4 ) } \\ & { y _ { 2 } ^ { \prime } ( x ) = c _ { 1 } y _ { 1 } ( x ) - y _ { 2 } ( x ) - c _ { 2 } y _ { 4 } ( x - 4 ) } \\ & { y _ { 3 } ^ { \prime } ( x ) = y _ { 2 } ( x ) - y _ { 3 } ( x ) } \\ & { y _ { 4 } ^ { \prime } ( x ) = y _ { 3 } ( x ) - 0 . 5 y _ { 4 } ( x ) } \end{array}
$$

where $\scriptstyle { c _ { 2 } = c _ { 1 } \cdot I ^ { 3 } } .$ 0.006. By setting $y \left( x \right) = y \cdot e ^ { \gamma x }$ we arrive at the characteristic equation (see (15.8"))， which becomes after some simplifications

$$
( c _ { 1 } + \gamma ) { ( 1 + \gamma ) } ^ { 2 } ( 0 . 5 + \gamma ) + c _ { 2 } \gamma e ^ { - 4 \gamma } = 0 .
$$

As in the paper of Okamoto - Hayashi, we put $I = 1 0 . 5$ . Then (15.18) possesses one pair of complex solutions in $\mathbf { C } ^ { + }$ ,namely

$$
\gamma = 0 . 0 4 2 4 6 \pm \ : 0 . 4 7 6 6 6 i
$$

and the equilibrium solution is unstable (see Figure 15.7). The

![](images/3dba0704b58a78048a18774802870d43776ca1fadf71ba33caf0613667d62ac1.jpg)  
Figure 15.7. Solutions of the enzyme kinetics problem (15.16), $I = 1 0 . 5$ Initial values close to equilibrium position

period of the solution of the linearized equation is thus $T = 2 \pi / 0 . 4 7 6 6 6 = 1 3 . 1 8$ . The solutions then tend to a limit cycle of approximately the same period.

# A mathematical model in immunology

We conclude our series of examples with Marchuk's model (Marchuk 1975) for the struggle of viruses $V \left( t \right)$ ， antibodies $F ( t )$ and plasma cells $C \left( t \right)$ in the organism of a person infected by a viral disease. The equations are

$$
\begin{array} { l } { { \displaystyle { \frac { d V } { d t } } = ( h _ { 1 } - h _ { 2 } F ) V } } \\ { { \displaystyle { \frac { d C } { d t } } = \xi ( m ) h _ { 3 } F ( t - \tau ) V \left( t - \tau \right) - h _ { 5 } ( C - 1 ) } } \\ { { \displaystyle { \frac { d F } { d t } } = h _ { 4 } ( C - F ) - h _ { 8 } F V ~ . } } \end{array}
$$

The first is a Volterra - Lotkin like predator-prey equation. The second equation describes the creation of new plasma cells with time lag due to infection, in the absence of which the second term creates an equilibrium at $c = 1$ . The third equation models the creation of antibodies from plasma cells $( h _ { 4 } C$ ) and their decrease due to aging $( - h _ { 4 } F )$ and binding with antigens $( - h _ { 8 } F V )$ ). The term $\xi ( m )$ , finally, is defined by

$$
\xi ( m ) = \left\{ \begin{array} { l l } { { 1 } } & { { \mathrm { i f } m \leq 0 . 1 } } \\ { { ( 1 - m ) { \frac { 1 0 } { 9 } } } } & { { \mathrm { i f } 0 . 1 \leq m \leq 1 } } \end{array} \right.
$$

and expresses the fact that the creation of plasma cells slows down when the organism is damaged by the viral infection. The relative characteristic $m \left( t \right)$ of damaging is given by a fourth equation

$$
{ \frac { d m } { d t } } = h _ { 6 } V _ { \mathbf { \theta } } - h _ { 7 } m
$$

where the first term expresses the damaging and the second recuperation.

This modelallows us, by changing the coefficients h1, h2,, hg, to model all sorts of behaviour of stable health, unstable health, acute form of a disease, chronic form etc. See Chapter 2 of Marchuk (1983). In Figure 15.8 we plot the solutions of this model for $\tau = 0 . 5$ ， ${ h _ { \ 1 } } = 2$ ， ${ { h } _ { 2 } } \mathrm { { = } } 0 . 8$ ， $h _ { 3 } { = } 1 0 ^ { 4 }$ ， ${ h _ { \ 4 } } \mathrm { { = } } 0 . 1 7$ ， $h _ { \ 5 } { = } 0 . 5$ ， $h _ { 7 } { = } 0 . 1 2$ ， ${ h _ { \ 8 } } \mathrm { { = } } 8$ and initial values $\bar { V } \left( t \right) = \mathrm { m } \mathrm { a x } ( 0 , 1 0 ^ { - 6 } + t )$ if $t \le 0$ $C \ ( 0 ) { = } 1$ ， $F \left( t \right) = 1$ if $t \le 0$ ， $m \ ( 0 ) { = } 0$ . In dependence of the vaiue of $h _ { 6 }$ ${ h _ { 6 } } \mathrm { { = } } 1 0$ or $h _ { 6 } { = } 3 0 0$ ，we then observe either complete recovery (defined by $V \left( t \right) < 1 0 ^ { - 1 6 } )$ ,0r periodic outbreak of the disease due to damaging $\left( m \left( t \right) \right)$ becomes nearly 1).

![](images/3eee210694d6ef6331cb48ed0f62210e275e59e1125d9848bc8b2da1c9e107f4.jpg)  
Figure 15.8. Solutions of the Marchuk immunology model

# Integro-differen tial equations

Often the hypothesis that a system depends on the time lagged solution at a specified fixed value $x - \tau$ is not very realistic, and one should rather suppose this dependence to be stretched out over a longer period of time. Then, instead of (15.1), we would have for example

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) , \intop _ { x  \tau } ^ { x } K ( x , \xi , y ( \xi ) ) d \xi ) .
$$

The numerical treatment of these problems becomes much more expensive. If $K \left( x , \xi , y \right)$ is zero in the neighbourhood of the diagonal $x = \xi$ , one can eventually use RETARD and call a quadrature routine for each function evaluation.

Fortunately, many integro-differential equations can be reduced to ordinary or delay differential equations by introducing new variables for the integral function.

Example (Volterra (1934)). Consider the equation

$$
y ^ { \prime } ( x ) = { \biggl ( } \epsilon - \alpha y ( x ) - \intop _ { 0 } ^ { x } y ( \xi ) k ( x - \xi ) d \xi { \biggr ) } \cdot y ( x )
$$

for population dynamics, where the integral term represents a decrease of the reproduction rate due to pollution. If now for example $k \left( x \right) = c$ , we put

$$
\begin{array} { l } { \displaystyle { \int _ { 0 } ^ { x } y ( \xi ) d \xi = \nu ( x ) , \quad y ( x ) = \nu ^ { \prime } ( x ) } } \end{array}
$$

and obtain

$$
\nu ^ { \prime \prime } ( x ) = [ \epsilon - \alpha \nu ^ { \prime } ( x ) - c \nu ( x ) ] \nu ^ { \prime } ( x ) ~ ,
$$

an ordinary differential equation. The same method is possible for equations (15.20) with "degenerate kernel"; i.e. where

$$
K \left( x , \xi , y \right) = \sum _ { i = 1 } ^ { m } a _ { i } ( x ) b _ { i } ( \xi , y ) \ .
$$

If we insert this into (15.20) and put

$$
\nu _ { i } ( x ) = \int _ { x  \tau } ^ { x } b _ { i } ( \xi , y ( \xi ) ) d \xi ,
$$

we obtain

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , \sum _ { i = 1 } ^ { m } a _ { i } ( x ) \nu _ { i } ( x ) \right)
$$

$$
\nu _ { i } ^ { \prime } ( x ) = b _ { i } ( x , y ( x ) ) - b _ { i } ( x - \tau , y ( x - \tau ) ) \quad i = 1 , \dots , m ,
$$

a delay differential equation.

# Exercises

1. Compute the solution of the Verhulst - Pearl equation (15.10).

2. Compute the equilibrium points of Marchuk's equation ( and study their stability.

3. Assume that the kernel $\boldsymbol { k } _ { \mathbf { \lambda } } ( \boldsymbol { x } _ { \mathbf { \lambda } } )$ in Volterra's equation (15.21) is given by

$$
k \left( x \right) = p \left( x \right) e ^ { - \mathsf { B } x }
$$

where $p ( x )$ is some polynomial. Show that this problem can be transformed into an ordinary differential equation.

4. Consider the integro-differential equation

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) , \intop _ { 0 } ^ { x } K \left( x , \xi , y \left( \xi \right) \right) d \xi \right) .
$$

a) For the degenerate kernel (15.22) Problem (15.24) becomes equivalent to the ordinary differential equation

$$
\begin{array} { l } { { \displaystyle y ^ { \prime } ( \boldsymbol { x } ) = f \left( x , y \left( x \right) , \sum _ { j = 1 } ^ { m } a _ { j } ( x ) \nu _ { j } ( x ) \right) } } \\ { { \displaystyle \nu _ { j } ^ { \prime } ( x ) = b _ { j } ( x , y \left( x \right) ) . } } \end{array}
$$

b) Show that an application of an explicit ( $\mathcal { P }$ -th order) Runge-Kutta method to (15.25) yields the formulas (Pouzet, 1963)

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } = y _ { n } ~ + ~ h \sum _ { i = 1 } ^ { s } { b _ { i } f \left( x _ { n } + c _ { i } h , g _ { i } ^ { \left( n \right) } , u _ { i } ^ { \left( n \right) } \right) } } } \\ { { \displaystyle g _ { i } ^ { \left( n \right) } = y _ { n } ~ + ~ h \sum _ { j = 1 } ^ { i - 1 } a _ { i j } f \left( x _ { n } + c _ { j } h , g _ { j } ^ { \left( n \right) } , u _ { j } ^ { \left( n \right) } \right) } } \\ { { \displaystyle u _ { i } ^ { \left( n \right) } = F _ { n } ( x _ { n } + c _ { i } h ) ~ + ~ h \sum _ { j = 1 } ^ { i - 1 } a _ { i j } K \left( x _ { n } + c _ { i } h , x _ { n } + c _ { j } h , g _ { j } ^ { \left( n \right) } \right) } } \end{array} \quad ( 1 5 )
$$

where

$$
\begin{array} { l } { { F _ { 0 } ( x ) = 0 } } \\ { { F _ { n + 1 } ( x ) = F _ { n } ( x ) + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } K \left( x , x _ { n } + c _ { i } h , g _ { i } ^ { ( n ) } \right) . } } \end{array}
$$

c) If we apply Method (15.26) to the Problem (15.24), where the

kernel does not necessarily satisfy (15.22)， we nevertheless have convergence of order $p$

Hint. Approximate the kernel by a degenerate one.

5. (Zennaro, 1986). For the delay equation (15.1) consider the method (15.5) where (15.5c) is replaced by

$$
\begin{array} { r } { \gamma _ { j } ^ { ( n ) } = \left\{ \begin{array} { l l } { \Phi ( x _ { n } + c _ { j } h - \tau ) \quad } & { \mathrm { i f } \ : n < k } \\ { \quad } \\ { q _ { n - k } ( c _ { j } ) \quad } & { \mathrm { i f } \ : n \geq k } \end{array} \right. . } \end{array}
$$

Here ${ { q } _ { n } } \left( \mathfrak { \theta } \right)$ is the polynomial given by a continuous Runge-Kutta method (Section I1.5)

$$
q _ { n } ^ { } \left( \boldsymbol { \theta } \right) = y _ { n } ^ { } + h \sum _ { j = 1 } ^ { s } b _ { j } ^ { } \left( \boldsymbol { \theta } \right) f \left( \boldsymbol { x } _ { n } ^ { } + \boldsymbol { c } _ { j } ^ { } h , \boldsymbol { g } _ { j } ^ { ( n ) } , \boldsymbol { \gamma } _ { j } ^ { ( n ) } \right) .
$$

a) Prove that the orthogonality conditions

$$
\begin{array} { r } { \underset { 0 } { \overset { 1 } { \sum } } \boldsymbol { \theta } ^ { q - 1 } \bigg [ \boldsymbol { \gamma } ( t ) \underset { j = 1 } { \overset { s } { \sum } } b _ { j } ( \boldsymbol { \theta } ) \Phi _ { j } ( t ) - \boldsymbol { \theta } ^ { \mathsf { p } ( t ) } \bigg ] d \boldsymbol { \theta } = 0 \quad \mathrm { f o r } \quad q + \mathsf { \rho } ( t ) \leq p } \\ { \quad \boldsymbol { \rho } ( t ) \underset { j = 1 } { \overset { s } { \sum } } \boldsymbol { \theta } , } \end{array}
$$

imply convergence of order $p$ ， if the underlying Runge-Kutta method is of order $p$ for ordinary differential equations.

Hint. Use the theory of B-series and the Grobner - Alekseev formula (14.18) of Section I.14.

b) If for a given Runge-Kutta method the polynomials $b _ { j } ( \boldsymbol { \theta } )$ of degree $\leq \vert ( p + 1 ) / 2 \vert$ are such that

$$
\int _ { 0 } ^ { 1 } \theta ^ { q - 1 } b _ { j } \bigl ( \theta \bigr ) d \theta = \frac { 1 } { q } b _ { j } \bigl ( 1 - c _ { j } ^ { q } \bigr ) q = 1 , \ldots , \left[ ( p - 1 ) / 2 \right] ,
$$

$$
b _ { j } ( 0 ) = 0 \ , \qquad b _ { j } ( 1 ) = b _ { j }
$$

then (15.27) is satisfied. In addition one has the order conditions

$$
\sum _ { j = 1 } ^ { s } b _ { j } \bigl ( { \boldsymbol { \Theta } } \bigr ) \Phi _ { j } \bigl ( t \bigr ) = \frac { { \boldsymbol { \Theta } } ^ { \boldsymbol { \rho } \bigl ( t \bigr ) } } { \gamma \bigl ( t \bigr ) } \quad \mathrm { ~ f o r ~ } \quad { \boldsymbol { \rho } } \bigl ( t \bigr ) \leq \bigl [ \bigl ( { \boldsymbol { p } } + 1 \bigr ) / 2 \bigr ] .
$$

c) Show that the conditions (15.28) admit unique polynomials $b _ { j } ( \boldsymbol { \theta } )$ of degree $\left[ ( p + 1 ) / 2 \right]$

6. Solve Volterra's equation (15.21) with $k \left( x \right) { = } c$ and compare the solution with the "pollution free" problem (15.10). Which population lives better, that with pollution, or that without?

# CHAPTER II MULTISTEP METHODS AND GENERAL LINEAR METHODS

This chapter is devoted to the study of multistep and general multivalue methods. After retracing their historical developement (Adams, Nystrom, Milne, BDF) we study in the subsequent sections the order, stability and convergence properties of these methods. Convergence is most elegantly set in the framework of one-step methods in higher dimensions. Sections III.5 and Il.6 are devoted to variable step size and Nordsieck methods. We then discuss the various available codes and compare them on the numerical examples of Section II.10 as well as on some equations of high dimension. Before closing the chapter with a section on special methods for second order equations, we discuss two highly theoretical subjects: one on general linear methods, including Runge-Kutta methods as well as multistep methods and many generalizations, and the other on the asymptotic expansion of the global error of such methods.

# II.1. Classical linear multistep formulas

and my undertaking must have ended here, if I had depended upon my own resources. But at this point Professor J.C. Adams furnished me with a perfectly satisfactory method of calculating by quadratures the exact theoretical forms of drops of fluids from the Differential Equation of Laplace."   
(F. Bashforth,1883)

Another improvement of Euler's method was considered even earlier than Runge-Kutta methods - the methods of Adams. Thesc were devised by John Couch Adams in order to solve a problem of F. Bashforth, which occured in an investigation of capillary action. Both the problem and the numerical integration schemes are published in Bashforth (1883). The actual origin of these methods must date back to at least 1855, since in that year F. Bashforth made an application to the Royal Society for assistance from the Government grant. There he wrote: "., but I am indebted to Mr Adams for a method of treating the differential equation

$$
\frac { \frac { d d z } { d u ^ { 2 } } } { \big ( 1 + \frac { { d z } ^ { 2 } } { { d u } ^ { 2 } } \big ) ^ { 3 / 2 } } + \frac { \frac { 1 } { u } \frac { d z } { d u } } { \big ( 1 + \frac { { d z } ^ { 2 } } { { d u } ^ { 2 } } \big ) ^ { 1 / 2 } } - 2 \alpha z = \frac { 2 } { b } ~ ,
$$

when put under the form

$$
{ \frac { b } { \ p } } \ + \ { \frac { b } { x } } \sin \Phi = 2 + 2 \alpha b ^ { 2 } { \frac { z } { b } } = 2 + \beta { \frac { z } { b } } \ ,
$$

which gives the theoretical form of the drop with an accuracy exceeding that of the most refined measurements."

In contrast to one-step methods, where the numerical solution is obtained solely from the differential equation and the initial value, the algorithm of Adams consists of two parts: firstly, a starting procedure which provides $y _ { 1 } , . . . , y _ { k - 1 }$ (approximations to the exact solution at the points $x _ { 0 } { + } h \ , \ldots , x _ { 0 } { + } ( k - 1 ) h \ )$ and, secondly， a multistep formula to obtain an approximation to the exact solution $y \left( x _ { \mathit { 0 } } + k h \right)$ This is then applied recursively, based on the numerical approximations of $k$ successive steps, to compute $y \left( x _ { 0 } + ( k + 1 ) h \right) , \ldots$ etc.

There are several possibilities for obtaining the starting values. J.C. Adams actually computed them using the Taylor series expansion of the exact solution (as described in Section I.8, see also Exercise 2). Another possbility is the use of any one-step method, e.g. a Runge-

Kutta method (see Chapter II). It is also usual to start with low-order Adams methods and very small step sizes.

# Explicit Adams methods

We now derive, following Adams, the first explicit multistep formulas. We introduce the notation ${ x _ { i } = } x _ { 0 } { + } i h$ for the grid points and suppose we know the numerical appoximations $y _ { n } , y _ { n - 1 } , \ldots , y _ { n - k + 1 }$ to the exact solution $y \left( x _ { n } \right) , \ldots , y \left( x _ { n - k + 1 } \right)$ of the differential equation

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } .
$$

Adams considers (1.1) in integrated form,

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n } \right) + \intop _ { x _ { n } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ , ~ }
$$

On the right hand side of (1.2) there appears the unknown solution $y \left( x \right)$ But since the approximations $y _ { n - k + 1 } , \ldots , y _ { n }$ are known, the values

$$
f _ { i } = f \left( x _ { i } , y _ { i } \right) \qquad \mathrm { f o r } i = n - k + 1 , \ldots , n
$$

are also available and it is natural to replace the function $f \left( t , y \left( t \right) \right)$ in (1.2) by the interpolation polynomial through the points $\{ ( \boldsymbol { x } _ { i } , f _ { i } ) | i = n - k + 1 , \ldots , n \}$ This polynomial can be expressed in terms of backward differences

$$
\nabla ^ { 0 } f _ { n } = f _ { n } , \qquad \nabla ^ { j + 1 } f _ { n } = \nabla ^ { j } f _ { n } - \nabla ^ { j } f _ { n - 1 }
$$

as follows:

$$
p \left( t \right) = p \left( x _ { n } + s h \right) = \sum _ { j = 0 } ^ { k - 1 } ( - 1 ) ^ { j } \binom { - s } { j } \nabla ^ { j } f _ { n }
$$

(Newton's interpolation formula, see e.g. Henrici (1962), p.190). The numerical analogue to (1.2) is then given by

$$
y _ { n + 1 } = y _ { n } + \intop _ { x _ { n } } ^ { x _ { n + 1 } } p \left( t \right) d t
$$

or after insertion of (1.4) by

$$
y _ { n + 1 } = y _ { n } + h \sum _ { j = 0 } ^ { k - 1 } \gamma _ { j } \nabla ^ { j } f _ { n }
$$

where the coefficients Y ， satisfy

Table 1.1. Coefficients for the explicit Adams methods   

<table><tr><td>j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>γj</td><td>1</td><td>1</td><td>5</td><td>3</td><td>251</td><td>95</td><td>19087</td><td>5257</td><td>1070017</td></tr><tr><td></td><td></td><td>2</td><td>12</td><td>8</td><td>720</td><td>288</td><td>60480</td><td>17280</td><td>3628800</td></tr></table>

$$
\gamma _ { j } = { ( - 1 ) ^ { j } } \intop _ { 0 } ^ { 1 } { \binom { - s } { j } d s }
$$

(see Table 1.1 for their numerical values). A simple recurrence relation for these coefficients will be derived later (Formula (1.11)).

Special cases of (1.5). For $k = 1 , 2 , 3 , 4$ ， after expressing the backward differences in terms of $f _ { n - j }$ , one obtains the form ulas

$$
\begin{array} { l } { { k = 1 ; \quad y _ { n + 1 } = y _ { n } + h f _ { n } ~ , ~ ( 1 . 5 ^ { \prime } ) } } \\ { { k = 2 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 3 } { 2 } f _ { n } - \displaystyle \frac { 1 } { 2 } f _ { n - 1 } \right] ~ , } } \\ { { k = 3 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 2 3 } { 1 2 } f _ { n } - \displaystyle \frac { 1 6 } { 1 2 } f _ { n - 1 } + \displaystyle \frac { 5 } { 1 2 } f _ { n - 2 } \right] ~ , } } \\ { { k = 4 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 5 5 } { 2 4 } f _ { n } - \displaystyle \frac { 5 9 } { 2 4 } f _ { n - 1 } + \displaystyle \frac { 3 7 } { 2 4 } f _ { n - 2 } - \displaystyle \frac { 9 } { 2 4 } f _ { n - 3 } \right] ~ . } } \end{array}
$$

Remark. For $k = 1$ we have the explicit Euler method.

# Implicit Adams methods

The formulas (1.5) are obtained by integrating the interpolation polynomial (1.4) from $x _ { n }$ t0 $x _ { n + 1 }$ ,ieoutsidetheitpaite val $( x _ { n - k + 1 } , x _ { n } )$ . It is wel known that an interpolation polynomial is usually a rather poor approximation outside this interval. Thus the explicit Adams methods are not very accurate. Adams therefore also investigated methods where (1.4) is replaced by the interpolation polynomial which uses in addition the point $( x _ { n + 1 } , f _ { n + 1 } )$ ,i.e.

$$
p ^ { * } ( t ) = p ^ { * } ( x _ { n } + s h ) = \sum _ { j = 0 } ^ { k } ( - 1 ) ^ { j } \binom { - s + 1 } { j } \nabla ^ { j } f _ { n + 1 } .
$$

Inserting this into (1.2) we obtain the following im plicit method

$$
y _ { n + 1 } = y _ { n } + h \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 }
$$

where the coeficients $\gamma _ { j } ^ { \ast }$ satisfy

Table 1.2. Coefficients for the implicit Adams methods   

<table><tr><td>j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>Y</td><td>1</td><td>2</td><td>二1 12</td><td>-1 24</td><td>-19 720</td><td>-3 160</td><td>-863 60480</td><td>-275 24192</td><td>-33953 3628800</td></tr></table>

$$
{ \gamma _ { j } ^ { * } } = { ( - 1 ) ^ { j } } \intop _ { 0 } ^ { 1 } { \binom { - s + 1 } { j } } d s
$$

and are given in Table 1.2 for $j \le 8$ . Again, a simple recurrence relation can be derived for these coefficients (Exercise 3).

The formulas thus obtained are generally of the form

$$
y _ { n + 1 } = y _ { n } + h \left[ \beta _ { k } f _ { n + 1 } + \cdot \cdot \cdot + \beta _ { 0 } f _ { n - k + 1 } \right] .
$$

The first examples are as follows

$$
\begin{array} { l } { { k = 0 ; \quad y _ { n + 1 } = y _ { n } + h f _ { n + 1 } \ , \ } } \\ { { k = 1 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 1 } { 2 } f _ { n + 1 } + \displaystyle \frac { 1 } { 2 } f _ { n } \ \right] \ , } } \\ { { k = 2 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 5 } { 1 2 } f _ { n + 1 } + \displaystyle \frac { 8 } { 1 2 } f _ { n } - \displaystyle \frac { 1 } { 1 2 } f _ { n - 1 } \ \right] \ , } } \\ { { k = 3 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 9 } { 2 4 } f _ { n + 1 } + \displaystyle \frac { 1 9 } { 2 4 } f _ { n } - \displaystyle \frac { 5 } { 2 4 } f _ { n - 1 } + \displaystyle \frac { 1 } { 2 4 } f _ { n - 2 } \right] \ . } } \end{array}
$$

The special cases $\scriptstyle k = 0$ and $k = 1$ are the implicit Euler method and the trapezoidal rule, respectively. They are actually one-step methods and have already been considered in Chapter II.7.

The methods (1.8) give in general more accurate approximations to the exact solution than (1.5). This will be discussed in detail when the concepts of order and error constant are introduced (Section III.2). The price for this higher accuracy is that $y _ { n + 1 }$ is only defined implicitly by Formula (1.8). Therefore, in general a nonlinear equation has to be solved at each step. This can be done by fixed point iteration: let y ( be an approximation to $y _ { n + 1 }$ and define

$$
y _ { n + 1 } ^ { ( l ) } = y _ { n } + h \left[ \ B _ { k } f \left( x _ { n + 1 } , y _ { n + 1 } ^ { ( l - 1 ) } \right) + \ B _ { k - 1 } f _ { n } \ + \cdot \cdot \cdot + \mathsf { \beta } _ { 0 } f _ { n - k + 1 } \right] \ .
$$

Then,if thestepire $^ h$ is small enoug, $y _ { n + 1 } ^ { ( l ) }$ converges for $l  \infty$ t the numerical solution $y _ { n + 1 }$ of (1.8). In practice one uses for $y _ { n + 1 } ^ { ( 0 ) }$ the value obtained from the explicit formula (1.5) ("Predictor"), followed by one iteration of formula (1.10) ("Corrector"). This technique has been used by F.R. Moulton (1926) as well as by W.E. Milne (1926). J.C. Adams actually solved the implicit equation (1.8) by Newton's method, in the same way as is now usual for stiff equations (see Volume II).

Remark: Formula (1.5) is often attributed to Adams-Bashforth. Similarly, the multistep formula (1.8) is usually attributed to Adams-Moulton (F.R. Moulton (1926)). In fact, both formulas are due to Adams.

# Recurrence relations for the Y;

Using Euler's method of generating functions (see e.g. Henrici (1962)) we can deduce simple recurrence relations for $\boldsymbol { \gamma } _ { i }$ Denote by $G \left( t \right)$ the series

$$
G \left( t \right) = \sum _ { j = 0 } ^ { \infty } { \gamma _ { j } t ^ { j } } \mathrm { ~ . ~ }
$$

With the definition of $\gamma _ { j }$ and the binomial theorem one obtains

$$
\begin{array} { l } { G \left( t \right) = \displaystyle \sum _ { j = 0 } ^ { \infty } \left( - t \right) ^ { j } \int _ { 0 } ^ { 1 } \binom { - s } { j } d s = \displaystyle \int _ { 0 } ^ { 1 } \sum _ { j = 0 } ^ { \infty } \left( - t \right) ^ { j } \binom { - s } { j } d s } \\ { \displaystyle = \displaystyle \int _ { 0 } ^ { 1 } \left( 1 { - } t \right) ^ { - s } d s = - \frac { t } { \left( 1 - t \right) \log \left( 1 - t \right) } . } \end{array}
$$

This can be written as

$$
- \ { \frac { \log ( 1 - t ) } { t } } \ G \left( t \right) = { \frac { 1 } { 1 - t } }
$$

or as

$$
( 1 + \textstyle { \frac { 1 } { 2 } } t + \textstyle { \frac { 1 } { 3 } } t ^ { 2 } + \cdot \cdot \cdot ) ( \gamma _ { 0 } + \gamma _ { 1 } t + \gamma _ { 2 } t ^ { 2 } + \cdot \cdot \cdot ) = ( 1 + t + t ^ { 2 } + \cdot \cdot \cdot ) \ .
$$

Comparing the coefficients of $t ^ { m }$ we get the desired recurrence reiation

$$
\gamma _ { m } + \frac { 1 } { 2 } \gamma _ { m - 1 } + \frac { 1 } { 3 } \gamma _ { m - 2 } + \cdots + \frac { 1 } { m + 1 } \gamma _ { 0 } = 1 \ .
$$

The corresponding formula for implicit Adams methods is discussed in Exercise 3.

# Ex plicit Nystrδm methods

'Die angenaherte Integration hat, besonders in der letzten Zeit, ein ausgedehntes Anwendungsgebiet innerhalb der exakten Wissenschaften und der Technik gefunden."

(E.J. Nystrom, 1925)

In his review article on the numerical integration of differential equations (which we have already encountered in Section II.13), Nystrom (1925) also presents a new class of multistep methods. He considers instead of (1.2) the integral equation

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n - 1 } \right) + \intop _ { x _ { n - 1 } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ . ~ }
$$

Just as J.C. Adams did he replaces the unknown function $f \left( t , y \left( t \right) \right)$ by the polynomial $p \left( t \right)$ of (1.4) and so obtains the formula

$$
y _ { n + 1 } = y _ { n - 1 } + h \sum _ { j = 0 } ^ { k - 1 } \kappa _ { j } \nabla ^ { j } f _ { n }
$$

with the coefficients

$$
\kappa _ { j } = { ( - 1 ) ^ { j } } \intop _ { - 1 } ^ { 1 } { \binom { - s } { j } d s } .
$$

The first six of these coefficients are given in Table 1.3. E.J. Nystrom recommended the formulas (1.13)， since the coefficients $\kappa _ { j }$ were more convenient for his computations than the coefficients' $\gamma _ { j }$ of (1.5). This recommendation, surely reasonable for a computation by hand, is of little relevance for computations on a computer.

Table 1.3. Coefficients for the explicit Nystrom methods   

<table><tr><td>j</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Kj</td><td>2 0</td><td>1 1 3 3</td><td>29 90</td><td>14 45</td><td>1139 3780</td></tr></table>

Special cases: For $k = 1$ the formula

$$
y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n }
$$

is obtained. It is called the mid-point rule and is the simplest two-step method. Its symmetry was extremely useful in the extrapolation schemes of Section II.9. The case $k = 2$ yields nothing new, since $\kappa _ { 1 } { = } 0 .$ For $k = 3$ one gets

$$
y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 7 } { 3 } f _ { n } - \frac { 2 } { 3 } f _ { n - 1 } + \frac { 1 } { 3 } f _ { n - 2 } \right] .
$$

# Milne-Simpson methods

We consider again the integral equation (1.12). But this time we replace the integrand by the polynomial $\boldsymbol { p } ^ { * } ( t )$ of (1.7),which in addition to $f _ { n } ~ , ~ \dots , f _ { n - k + 1 }$ also interpolates the value $f _ { n + 1 }$ . Proceeding as usual, we now get the implicit formulas

$$
y _ { n + 1 } = y _ { n - 1 } + h \sum _ { j = 0 } ^ { k } \kappa _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 } ~ .
$$

The coefficients $\kappa _ { j } ^ { \ast }$ are defined by

$$
\kappa _ { j } ^ { \ast } = ( - 1 ) ^ { j } \int _ { - 1 } ^ { 1 } \binom { - s + 1 } { j } d s ,
$$

and the first of these are given in Table 1.4.

Table 1.4. Coefficients for the Milne-Simpson methods   

<table><tr><td>j</td><td>0 1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>x</td><td>2 -2</td><td>1 3</td><td>0</td><td>-1 90</td><td>-1 90</td><td>-37 3780</td></tr></table>

If the backward differences in (1.15) are expressed in terms of $f _ { n - j } ,$ . one obtains the following methods for special values of $k$ ：

$$
\begin{array} { r l r } { \mathrm { ~ } } & { : = 0 ; } & { y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n + 1 } \ , \ } \\ { \mathrm { ~ } } & { : = 1 ; } & { y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n } \ , \ } \\ { \mathrm { ~ } } & { : = 2 ; } & { y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 1 } { 3 } f _ { n + 1 } + \frac { 4 } { 3 } f _ { n } + \frac { 1 } { 3 } f _ { n - 1 } \right] \ , \ } \\ { \mathrm { ~ } } & { : = 4 ; } & { y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 2 9 } { 9 0 } f _ { n + 1 } + \frac { 4 4 } { 9 0 } f _ { n } + \frac { 4 } { 9 0 } f _ { n - 1 } + \frac { 4 } { 9 0 } f _ { n - 2 } - \frac { 1 } { 9 0 } f _ { n - 3 } \right] \ . } \end{array}
$$

The special case $k = 0$ is just Euler's implicit method applied with step size $2 h$ . For $k = 1$ one obtains the previously derived mid-point rule. The particular case $k = 2$ is an interesting method, known as the Milne method (see Milne (1926), (1970), p.66). It is a direct generalization of Simpson's rule.

Many other similar methods have been investigated. They are all based on an integral equation of the form

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n - l } \right) + \intop _ { x _ { n - l } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ , ~ }
$$

where $f \left( t , y \left( t \right) \right)$ is replaced either by the interpolating polynomial $p \left( t \right)$ (Formula (1.4)) or by $p ^ { * } ( t )$ (Formula (1.7). E.g. for $l = 3$ one obtains

$$
y _ { n + 1 } = y _ { n - 3 } + h \left[ { \frac { 8 } { 3 } } f _ { n } - { \frac { 4 } { 3 } } f _ { n - 1 } + { \frac { 8 } { 3 } } f _ { n - 2 } \right] .
$$

This particular method has been used by Milne (1926) as a "predictor" for his method: in order to solve the implicit equation (1.15'), Milne uses one or two fixed-point iterations with the numerical value of (1.18) as starting point.

Methods based on differentiation (BDF)

"My name is Gear." - - - "sorry? " "Gear, dshii, ii, ay, are." - . - “Jiea? (In a hotel in Paris)

The multistep formulas considered until now are all based on numerical integration, i.e. the integral in (1.17) is approximated numerically using some quadrature formula. The underlying idea of the following multistep formulas is totally different as they are based on the numerical differentiation of a given function.

Assume that the approximations $y _ { n - k + 1 } , \ldots , y _ { n }$ to the exact solution of (1.1) are known.In order to derive a formula for $y _ { n + 1 }$ we consider the polynomial $q \left( x \right)$ which interpolates the values $\{ ( x _ { i } , y _ { i } ) \mid i = n - k + 1 , . . . , n + 1 \}$ . As in (1.7) this polynomial can be expressed in terms of back ward differences, namely

$$
q \left( x \right) = q \left( x _ { n } + s h \right) = \sum _ { j = 0 } ^ { k } \left( - 1 \right) ^ { j } { \binom { - s + 1 } { j } } \nabla ^ { j } y _ { n + 1 } .
$$

The unknown value $y _ { n + 1 }$ will now be determined in such a way that the polynomial $q \left( x \right)$ satisfies the differential equation at at least one grid-point, i.e.

$$
q ^ { \prime } ( x _ { n + 1 - r } ) = f \left( x _ { n + 1 - r } , y _ { n + 1 - r } \right) ,
$$

For $r = 1$ we obtain explicit formulas. For $k = 1$ and $k = 2$ ,these are equivalent to the explicit Euler method and the mid-point rule, respectively. The case $k = 3$ yields

$$
\frac { 1 } { 3 } y _ { n + 1 } + \frac { 1 } { 2 } y _ { n } - y _ { n - 1 } + \frac { 1 } { 6 } y _ { n - 2 } = h f _ { n } .
$$

This formula, however, as well as those for $k > 3$ , is unstable (see Section I1.3) and therefore useless.

Much more interesting are the formulas one obtains when (1.20) is taken for $r = 0$ . In this case one gets the implicit formulas

$$
\sum _ { j = 0 } ^ { k } \ S _ { j } ^ { * } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 }
$$

with the coefficients

$$
\delta _ { j } ^ { * } = \left( - 1 \right) ^ { j } \frac { d } { d s } \left( { - s + 1 \atop j } \right) \mid _ { s = 1 } .
$$

Using the definition of the binomial coeficient

$$
( - 1 ) ^ { j } \binom { - s + 1 } { j } = \frac { 1 } { j ! } ( s - 1 ) s ( s + 1 ) \cdot \cdot \cdot ( s + j - 2 )
$$

the coefficients $\boldsymbol { \mathfrak { \delta } } _ { j } ^ { * }$ are obtained by direct differentiation:

$$
\mathfrak { d } _ { 0 } ^ { * } = 0 , \qquad \mathfrak { d } _ { j } ^ { * } = \frac { 1 } { j } \mathrm { f o r } j \ge 1 \ .
$$

Formula (1.22) therefore becomes

$$
\sum _ { j = 1 } ^ { k } \frac { 1 } { j } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 } .
$$

These multistep formulas, known as backward differentiation formulas (or BDF-methods) are widely used for the integration of stiff differentiai equations (see Volume II). They were introduced by Curtiss and Hirschfelder (1952)； Mitchell and Craggs (1953) call them "standard step-by-step methods".

For sake of completeness we give these formulas also in the form in which the backward differences are expressed in terms of the $y _ { n - j } .$

$$
\begin{array} { l l } { k = 1 ; } & { y _ { n + 1 } - y _ { n } = h f _ { n + 1 } \ , } \\ { k = 2 ; } & { \displaystyle \frac { 3 } { 2 } y _ { n + 1 } - 2 y _ { n } + \frac { 1 } { 2 } y _ { n - 1 } = h f _ { n + 1 } \ , } \\ { k = 3 ; } & { \displaystyle \frac { 1 1 } { 6 } y _ { n + 1 } - 3 y _ { n } + \frac { 3 } { 2 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } = h f _ { n + 1 } \ , } \\ { k = 4 ; } & { \displaystyle \frac { 2 5 } { 1 2 } y _ { n + 1 } - 4 y _ { n } + 3 y _ { n - 1 } - \frac { 4 } { 3 } y _ { n - 2 } + \frac { 1 } { 4 } y _ { n - 3 } = h f _ { n + 1 } \ , } \\ { k = 5 ; } & { \displaystyle \frac { 1 3 7 } { 6 0 } y _ { n + 1 } - 5 y _ { n } + 5 y _ { n - 1 } - \frac { 1 0 } { 3 } y _ { n - 2 } + \frac { 5 } { 4 } y _ { n - 3 } - \frac { 1 } { 5 } y _ { n - 4 } = h f _ { n + 1 } \ . } \\ { k = 6 ; } & { \displaystyle \frac { 1 4 7 } { 6 0 } y _ { n + 1 } - 6 y _ { n } + \frac { 1 5 } { 2 } y _ { n - 1 } - \frac { 2 0 } { 3 } y _ { n - 2 } + \frac { 1 5 } { 4 } y _ { n - 3 } - \frac { 6 } { 5 } y _ { n - 4 } + \frac { 1 } { 6 } y _ { n } \ . } \end{array}
$$

$$
= h f _ { n + 1 } ~ .
$$

For $k > 6$ the BDF-methods are unstable (see Section III.3).

# Exercises

1. Let the differential equation $y ^ { \prime } { = } y ^ { 2 }$ ， $y \left( 0 \right) = 1$ and the exact starting values ${ \boldsymbol y } _ { i } = 1 / \left( 1 - { \boldsymbol x } _ { i } \right)$ for $i = 0 , 1 , \ldots , k - 1$ be given. Apply the methods of Adams and study the expression $y \left( x _ { k } \right) - y _ { k }$ for small step sizes.

2. Consider the differential equation at the beginning of this section. It describes the form of a drop and can be written as (F. Bashforth 1883, page 26; the same problem as Exercise 2 of Section I1.1 in a different coordinate system)

$$
{ \frac { d x } { d \Phi } } = \rho \cos \Phi , \qquad { \frac { d z } { d \Phi } } = \rho \sin \Phi
$$

where

$$
\frac { 1 } { \rho } + \frac { \sin \Phi } { x } = 2 + \beta z \mathrm { ~ . ~ }
$$

p may be considered as a function of the coordinates $x$ and $z$ . It can be interpreted as the radius of curvature and $\Phi$ denotes the angle between the normal to the curve and the $z$ -axis (Figure 1.1). The initial values are given by $x \left( 0 \right) { = } 0$ $z \left( 0 \right) { = } 0$ ， $\rho ( 0 ) = 1$

![](images/40357fa79624103240deb990ee246be867a305a1411628b1b00dc4dffbcd50cd.jpg)  
Figure 1.1. Solution of the differential equation (1.24) and an illustration from the book of Bashforth

Solve the above differential equation along the lines of J.C. Adams:

a) Assuming

$$
{ \mathrm { \scriptsize ~ p ~ } } = 1 + b _ { 2 } { \dot { \Phi } } ^ { 2 } + b _ { 4 } \Phi ^ { 4 } + \cdots
$$

and inserting this expression into (1.24) we obtain after integration the truncated Taylor series of $x \left( \Phi \right)$ and $z \left( \Phi \right)$ in terms of $b _ { 2 } , b _ { 4 } , \ldots$ These parameters can then be calculated from (1.25) by comparing the coefficients of $\phi ^ { m } .$ In this way one obtains the solution for small values of $\Phi$ (starting values).

b) Use one of the proposed multistep formulas and calculate the solution for fixed β (say $\beta = 3$ ） over the interval $[ 0 , \pi ]$

3. Prove that the coefficients $\gamma _ { j } ^ { * }$ , defined by (1.9), satisfy

$$
\gamma _ { 0 } ^ { * } = 1
$$

$$
\gamma _ { m } ^ { * } + \frac { 1 } { 2 } \gamma _ { m - 1 } ^ { * } + \frac { 1 } { 3 } \gamma _ { m - 2 } ^ { * } + \cdot \cdot \cdot + \frac { 1 } { m + 1 } \gamma _ { 0 } ^ { * } = 0 \quad \mathrm { f o r ~ } m \geq 1 .
$$

4. Let κj, K, $\boldsymbol { \gamma } _ { j } , \boldsymbol { \gamma } _ { j } ^ { * }$ be the coefcients defined by (1.14)， (1.16), (1.6), (1.9), respectively. Show that

$$
\kappa _ { j } ^ { } = 2 \gamma _ { j } ^ { } - \gamma _ { j - 1 } ^ { } , \kappa _ { j } ^ { * } { = } 2 \gamma _ { j } ^ { * } { - } \gamma _ { j - 1 } ^ { * } \mathrm { ~ f o r ~ } j { \ge } 0
$$

(with $\gamma _ { - 1 } { = } \gamma _ { - 1 } ^ { * } { = } 0 )$

Hint: By spliting the integral in (1.14) one gets $\kappa _ { j } { = } \gamma _ { j } { + } \gamma _ { j } ^ { * }$ The relation ${ \boldsymbol \gamma } _ { j } ^ { * } { = } { \boldsymbol \gamma } _ { j } { - } { \boldsymbol \gamma } _ { j - 1 }$ is obtained by using a well-known identity for binomial coefficients .

# I11.2. Local error and order conditions

"You know, I am a multistep-man...and don't tell anybody,but the first program I wrote for the first Swedish computer was a Runge-Kutta code..." (G. Dahlquist, 1982, after some glasses of wine; printed with permission)

A general theory of multistep methods was started by the work of Dahlquist (1956, 1959)，and became famous through the classical book of Henrici (1962). All multistep formulas considered in the last section have this in common that the numerical approximations $y _ { i }$ as well as the values $\boldsymbol { f } _ { i }$ appear linearly. We thus consider the general difference equation

$$
\alpha _ { k } y _ { n + k } + \alpha _ { k - 1 } y _ { n + k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } y _ { n } = h \left( \beta _ { k } f _ { n + k } + \cdot \cdot \cdot + \beta _ { 0 } f _ { n } \right) ,
$$

which includes all previously considered methods as special cases. In this formula the $\mathbf { a } _ { i }$ and $\beta _ { i }$ are real parameters, h denotes the step size and

$$
f _ { i } ^ { \phantom { \dagger } } = f \left( x _ { i } ^ { \phantom { \dagger } } , y _ { i } ^ { \phantom { \dagger } } \right) , \qquad x _ { i } ^ { \phantom { \dagger } } = x _ { 0 } ^ { \phantom { \dagger } } + i h ,
$$

Throughout this chapter we shall assume that

$$
\alpha _ { k } \neq 0 \ , \quad | \ \alpha _ { 0 } | \ + | \ \beta _ { 0 } | > 0 \ .
$$

The first assumption expresses the fact that the implicit equation (2.1) can be solved with respect to $y _ { n + k }$ at least for suficiently small $\hbar$ . The second relation in (2.2) can always be achieved by reducing the index k , if necessary.

Formula (2.1) will be called a linear multistep method or more precisely a linear $k$ -step method. We also distinguish between explicit $( \beta _ { k } = 0 )$ and implicit $( \beta _ { k } \neq 0$ ） multistep methods.

# Local error of a multistep method

As the numerical solution of a multistep method does not depend only on the initial value problem (1.1) but also on the choice of the starting values, the definition of the local error is not as straightforward as for one-step methods (compare Sections I1.2 and I1.3).

Definition 2.1. The local error of the multistep method (2.1) is defined by

$$
y \left( x _ { k } \right) \mathrm { ~ - ~ } y _ { k }
$$

where $y \left( x \right)$ is the exact solution of $y ^ { \prime } { = } f \left( x , y \right) , y \left( x _ { 0 } \right) { = } y _ { 0 } ,$ and $y _ { k }$ is the numerical solution obtained from (2.1) by using the exact starting values $\boldsymbol y _ { i } = \boldsymbol y \left( \boldsymbol x _ { i } \right)$ for $i = 0 , 1 , \ldots , k - 1 .$

![](images/d27a939f44f97a8f45c062e394ce5eced82574e14b238b7c096a147bf5414727.jpg)  
Figure 2.1. Ilustration of the local error

In the case $k = 1$ this definition coincides with the definition of the local error for one-step methods. In order to show the connection with other possible definitions of the local error, we associate with (2.1) the linear difference operator $L$ defined by

$$
L \left( y , x , h \right) = \sum _ { i = 0 } ^ { k } \left[ \alpha _ { i } y \left( x + i h \right) - h \beta _ { i } y ^ { \prime } \left( x + i h \right) \right] .
$$

Here $y \left( x \right)$ is some differentiable function defined on an interval that contains the values $x + i h$ for $i = 0$ ,1,...,

Lemma 2.2. Consider the differential equation (1.1) with $f \left( x , y \right)$ continuousty differentiable and let $y \left( x \right)$ be its solution. For the local error one has

$$
y \left( x _ { k } \right) - y _ { k } \ = \ \left( \alpha _ { k } I - h \beta _ { k } { \frac { \partial f } { \partial y } } ( x _ { k } , \eta ) \right) ^ { - 1 } L \left( y , x _ { 0 } , h \right) \ .
$$

thec Here $\mathrm { \Delta \Psi ^ { \mathrm { T } } }$ is some value between e of a vetorvalued function $y \left( x _ { k } \right)$ $f$ and ， $\frac { \partial f } { \partial y } ( x _ { k } , \eta )$ $y _ { k }$ ，if $f$ is a scalar function. In is te Jacobin matrix,， whose rows are evaluated at possiby different values lying on the segment joining y(xk) and yk:

Proof: By Definition 2.1, $y _ { k }$ is determined implicitly by the equation

$$
\sum _ { i = 0 } ^ { k - 1 } \left[ \alpha _ { i } y \left( x _ { i } \right) - h \beta _ { i } f \left( x _ { i } , y \left( x _ { i } \right) \right) \right] + \alpha _ { k } y _ { k } - h \beta _ { k } f \left( x _ { k } , y _ { k } \right) = 0 \ .
$$

Inserting (2.3) we obtain

$$
L \left( y , x _ { 0 } , h \right) = \alpha _ { k } [ y \left( x _ { k } \right) - y _ { k } ] - h \beta _ { k } [ f \left( x _ { k } , y \left( x _ { k } \right) \right) - f \left( x _ { k } , y _ { k } \right) ]
$$

and the statement follows from the mean value theorem. QED.

This lemma shows that $\propto _ { k } ^ { - 1 } L \ ( y \ , x \ _ { 0 } , h )$ is essentially equal to the local error. Sometimes this term is also called the local crror (Dahlquist 1956, 1959).For explicit methods both expressions are equal.

# The order of a multistep method

Once the local error of a multistep method is defined, one can introduce the concept of order in the same way as for one-step methods.

Definition 2.3. The multistep method (2.1) is said to be of order $p$ , if one of the following two conditions is satisfied: i)forallsufficientlyregularfunctions $y \left( x \right)$ we have $L \left( y , x , h \right) = \mathbf { O } ( h ^ { p + 1 } )$ ； ii) the local error of (2.1) is $\mathbf { O } { ( h ^ { p + 1 } ) }$ for all sufficiently regular differential equations (1.1).

Observe that by Lemma 2.2 the above conditions i) and ii) are equivalent. Our next aim is to characterize the order of a multistep method in terms of the free parameters $\alpha _ { i }$ and $\beta _ { i }$ Dahlquist (1956) was the first to observe the fundamental role of the polynomials

$$
\begin{array} { l } { { \displaystyle { \mathsf { p } } \left( \zeta \right) = \alpha _ { k } \zeta ^ { k } + \alpha _ { k - 1 } \zeta ^ { k - 1 } + \cdots + \alpha _ { 0 } } } \\ { { \displaystyle { \sigma } \left( \zeta \right) = \beta _ { k } \zeta ^ { k } + \beta _ { k - 1 } \zeta ^ { k - 1 } + \cdots + \beta _ { 0 } } . } \end{array}
$$

They will be called the generating polynomials of the multistep method (2.1).

Theorem 2.4. The multistep method $( 2 . { \mathit { I } } )$ is of order $p$ , if and only if one of the following equivalent conditions is satisfied:

$$
\begin{array} { l } { { \mathrm { i } ) \quad \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } = 0 \quad a n d \quad \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } = q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \quad f o r \quad q = 1 , \dots , p \enspace ; } } \\ { { \mathrm { i i } ) \quad \displaystyle \mathsf { \rho } ( e ^ { h } ) - h \sigma ( e ^ { h } ) = 0 ( h ^ { p + 1 } ) \qquad f o r \quad h  0 \enspace ; } } \\ { { \mathrm { i i i } ) \quad \displaystyle \frac { \mathsf { \rho } ( \zeta ) } { \log \zeta } - \sigma ( \zeta ) = \mathsf { O } ( ( \zeta - 1 ) ^ { p } ) \qquad f o r \quad \zeta  1 \enspace . } } \end{array}
$$

Proof: Expanding $y \left( x + i h \right)$ and y $( x + i h )$ into a Taylor series and inserting these series (truncated if necessary) into (2.3) yields

$$
\begin{array} { c } { { \tiny { ? } \ ( y , x , h ) = \displaystyle \sum _ { i = 0 } ^ { k } \left[ \alpha _ { i } \sum _ { q \ge 0 } \frac { i ^ { q } } { q ! } h ^ { q } y ^ { ( q ) } ( x ) - h \beta _ { i } \sum _ { r \ge 0 } \frac { i ^ { r } } { r ! } h ^ { r } y ^ { ( r + 1 ) } ( x ) \right] } } \\ { { \tiny { \qquad k } } } \\ { { \tiny { = y \left( x \right) \sum _ { i = 0 } ^ { k } \alpha _ { i } + \displaystyle \sum _ { q \ge 1 } \frac { h ^ { q } } { q ! } y ^ { ( q ) } ( x ) \biggl [ \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \displaystyle \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \biggr ] \ . } } } \end{array}
$$

This implies the equivalence of Condition i) with $L \left( y , x , h \right)$ $= { \bf O } ( h ^ { p + 1 } )$ for all sufficiently regular functions $y \left( x \right)$

It remains to prove that the three conditions of Theorem 2.4 are equivalent. The identity

$$
L \left( \exp , 0 , h \right) = \rho \left( e ^ { h } \right) - h \sigma \left( e ^ { h } \right)
$$

where exp denotes the exponential function, together with

$$
L \left( \exp , 0 , h \right) = \sum _ { i = 0 } ^ { k } \alpha _ { i } + \sum _ { q \geq 1 } \frac { h ^ { q } } { q ! } \Bigg [ \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \Bigg ] \ ,
$$

which follows from (2.5)， shows the equivalence of the conditions i) and ii).

By use of the transformation $\zeta = e ^ { h }$ (or $h = \log \zeta )$ Condition ii） can be written in the form

$$
\begin{array} { r } { \mathsf { \rho } \mathsf { ( \xi ) } - \log \xi \sigma ( \boldsymbol \xi ) = \mathsf { O } ( ( \log \xi ) ^ { p + 1 } ) \qquad \mathrm { f o r ~ } \~ \xi \to \mathrm { ~ 1 ~ } . } \end{array}
$$

But this condition is equivalent to ii), since

$$
\begin{array} { r } { \log \  \zeta = ( \zeta - 1 ) + \mathbf { O } ( ( \zeta - 1 ) ^ { 2 } ) \ ~ \mathrm { f o r ~ } \ \zeta \to 1 \ . } \end{array}
$$

QED.

Remark : The conditions for a multistep method to be of order 1, which are usually called consistency conditions, can also be written in the form

$$
\mathsf { p } ( 1 ) = 0 \ , \qquad \mathsf { p ^ { \prime } ( 1 ) } = \sigma ( 1 ) \ .
$$

Once the proofs of the above order conditions have been understood, it is not difficult to treat the more general situation of non-equidistant grids (see Section I1.5 and the book of Stetter (1973), p.191).

Example 2.5. Order of the explicit Adams methods. Let us first investigate for which differential equations the explicit Adams methods give theoretically the exact solution. This is the case if the polynomial $p \left( t \right)$ of (1.4) is equal to $f \left( t , y \left( t \right) \right)$ . Suppose now that $f \left( t , y \right) { = } f \left( t \right)$ does not depend on y and is a polynomial of degree less than k . Then the explicit Adams methods integrate the differential equations

$$
y ^ { \prime } = q x ^ { q - 1 } , \qquad \mathrm { f o r } q = 0 , 1 , . . . , k
$$

exactly. This means that the local error is zero and hence, by Lemma 2.2,

$$
0 = L \left( { x ^ { q } } , 0 , h \right) = h ^ { q } \left[ \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \right] \quad \mathrm { f o r ~ } q = 0 , \dots , k \quad .
$$

This is just Condition i) of Theorem 2.4 with $p = k$ so that the order of the explicit Adams methods is at least $k$ . In fact it will be shown that the order of these methods is not greater than $k$ (Ex ample 2.7).

Example 2.6: For implicit Adams methods the polynomial $p ^ { * } ( t )$ of (1.7) is used instead of $p \left( t \right)$ . As the degree of $p ^ { * } ( t )$ is one higher than that of $p \left( t \right)$ ， the same considerations as in Example 2.5 show that the implicit Adams methods have order at least $k + 1$

All the methods of Section III.1 can be treated analogously (see Exercise 2 and Table 2.1).

# The error constant of a multistep method

The order of a multistep method indicates how fast the error tends to zero if $h  \mathrm { ~ 0 ~ }$ . Different methods of the same order, however, can have different errors; they are distinguished by the error constant. Formula (2.5) shows that the difference operator $L$ ， associated with a $p$ -th order multistep method, is such that for all sufficiently regular functions $y \left( x \right)$

$$
L \left( y , x , h \right) = C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x ) + \mathbf { O } ( h ^ { p + 2 } )
$$

where the constant $C _ { p + 1 }$ is given by

$$
C _ { p + 1 } = { \frac { 1 } { ( p + 1 ) ! } } \Bigg [ \sum _ { i = 0 } ^ { k } { \alpha _ { i } } ^ { p + 1 } - ( p + 1 ) \sum _ { i = 0 } ^ { k } { \beta _ { i } } i ^ { p } \Bigg ] ~ .
$$

This constant is not suitable as a measure of accuracy， since multipli-CationofForula(2.1bycostantcagiveauefo $C _ { p + 1 }$ whereas the numerical solution $\{ \boldsymbol { y } _ { n } \}$ remains unchanged. A better choice would be theconstant ${ \alpha } _ { k } ^ { - 1 } C _ { p + 1 } ^ { }$ ,since thelocalerrorofamul tistep method is given by (Lemma 2.2 and Formula (2.7))

$$
y ( x _ { k } ) - y _ { k } = \alpha _ { k } ^ { - 1 } C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { 0 } ) +  { \operatorname { O } ( h ^ { p + 2 } ) } \ .
$$

For several reasons, however, this is not yet a satisfactory definition, as we shall see from the following motivation: let

$$
e _ { n } \ = \ { \frac { y _ { n } - y \left( x _ { n } \right) } { h ^ { p } } }
$$

be the global error scaled by $h ^ { p }$ . Subtracting (2.1) from (2.3) and using (2.7) we have

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } e _ { \pi + i } ~ = ~ h \stackrel { 1 - p } { \sum _ { i = 0 } ^ { k } } \mathrm { \bf { \Sigma } } _ { i } ^ { k } \left( f \left( x _ { n + i } , y _ { n + i } \right) - f \left( x _ { n + i } , y \left( x _ { n + i } \right) \right) \right) } } \\ { { - C _ { p + 1 } h y ^ { ( p + 1 ) } ( x _ { n } ) ~ + { \bf O } ( h ^ { 2 } ) ~ . } } \end{array}
$$

The point is now to use

$$
y ^ { ( p + 1 ) } ( x _ { n } ) = { \frac { 1 } { \sigma ( 1 ) } } \sum _ { i  0 } ^ { k } \mathsf { \mathsf { \beta } } _ { i } y ^ { ( p + 1 ) } ( x _ { n + i } ) + \mathbf { O } ( h )
$$

which brings the error term in (2.10) inside the sum with the ${ \mathbf { } } | \beta _ { i }$ . We linearize

$$
^ { \ast } ( x _ { n + i } , y _ { n + i } ) - f ( x _ { n + i } , y ( x _ { n + i } ) ) = \frac { \partial f } { \partial y } ( x _ { n + i } , y ( x _ { n + i } ) ) h ^ { p } e _ { n + i } + 0 ( x _ { n + i } , y ( x _ { n + i } ) ) h ^ { p } e _ { n + i }
$$

and insert this together with (2.11) into (2.10). Neglecting the $\mathbf { O } ( h ^ { 2 } )$ and $\mathbb { O } \big ( h ^ { 2 p } \big )$ terms, we can interpret the obtained formula as the mul-tistep method applied to

$$
e ^ { \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) e ( x ) - C y ^ { ( p + 1 ) } ( x ) , e ( x _ { 0 } ) = 0 ,
$$

where

$$
C \ = \ { \frac { C _ { p + 1 } } { \sigma ( 1 ) } }
$$

is seen to be a natural measure for the global error and is therefore called the error constant.

Another derivation of Definition (2.13) will be given in the section on global convergence (see Exercise 2 of Section I1.4). Further, the solution of (2.12) gives just the first term of the asymptotic expansion of the global error (see Section II.9).

Example 2.7. Error constant of the explicit Adams methods. Consider the differential equation y'=f( ）with $f \left( x \right) = \left( k + 1 \right) x ^ { k }$ ，the exact solution of which is $y \left( x \right) = x ^ { k + 1 }$ As this differential equation is integrated exactly by the $\left( k + 1 \right)$ -step explicit Adams method (see Example 2.5), we have

$$
y \left( x _ { k } \right) - y \left( x _ { k - 1 } \right) = h \sum _ { j = 0 } ^ { k } { \gamma _ { j } \nabla ^ { j } f _ { k - 1 } } \mathrm { ~ . ~ }
$$

The local error of the $k$ -step explicit Adams method (1.5) is therefore given by

$$
y \left( x _ { k } \right) - y _ { k } \ = h \gamma _ { k } \nabla ^ { k } f _ { k - 1 } = h ^ { k + 1 } \gamma _ { k } f ^ { \left( k \right) } ( x _ { 0 } ) = h ^ { k + 1 } \gamma _ { k } y ^ { \left( k + 1 \right) } ( x _ { 0 } )
$$

As $\gamma _ { k } \neq 0$ , this formula shows that the order of the $k$ -step method is not greater than $k$ (compare Example 2.5). Furthermore, since $\alpha _ { k } = 1$ ， a comparison with Formula (2.9) yields $C _ { k + 1 } { = } { \boldsymbol { \gamma } } _ { k } .$ Finally, for Adams methods we have $p \left( \zeta \right) = \zeta ^ { k } - \zeta ^ { k - 1 }$ and $\rho ^ { \prime } ( 1 ) = 1$ , so that by the use of (2.6) the errocstatis given by $c = v _ { k }$

The error constants of all other previously considered multistep methods are summarized in Table 2.1 (observe that $\sigma ( 1 ) = 2$ for explicit Nystrom and Milne-Simpson methods).

Table 2.1. Order and error constant of multistep methods   

<table><tr><td>Method</td><td>Form ula</td><td>Order</td><td>Error Constant</td></tr><tr><td>Ex plicit Adam s</td><td>(1.5)</td><td>k</td><td>Yk</td></tr><tr><td>Im plicit Adam s</td><td>(1.8)</td><td>k+1</td><td>+1</td></tr><tr><td>Mid-point rule</td><td>(1.13&#x27;)</td><td>2</td><td>1 6</td></tr><tr><td>Nystrom,k &gt; 2</td><td>(1.13)</td><td>k</td><td>Kk 2</td></tr><tr><td>Milne, k =2</td><td>(1.15&#x27;)</td><td>4</td><td>1 180 *</td></tr><tr><td>Milne-Simpson, k &gt; 3</td><td>(1.15)</td><td>k+1</td><td>Kk+1 2</td></tr><tr><td>BDF</td><td>(1.22&#x27;)</td><td>k</td><td>1 k+1</td></tr></table>

# Irreducible methods

Let $\rho ( \zeta )$ and $\sigma ( \zeta )$ of Formula (2.4) be the generating polynomials of (2.1) and suppose that they have a common factor $\Phi ( \zeta )$ . Then define the polynomials

$$
{ \boldsymbol { \rho } } ^ { * } ( \zeta ) = \frac { \mathsf { \rho } ( \zeta ) } { \Phi ( \zeta ) } , \quad { \boldsymbol { \sigma } } ^ { * } ( \zeta ) = \frac { \sigma ( \zeta ) } { \Phi ( \zeta ) } ~ ,
$$

which are the generating polynomials of a new and simpler multistep method. Using the shift-operator $E$ , defined by

$$
E y _ { n } = y _ { n + 1 } \qquad \quad { \mathrm { o r } } \quad E y \left( x \right) = y \left( x + h \right)
$$

this multistep method can be written in compact form as

$$
\rho ^ { * } ( E ) y _ { n } \ = h \sigma ^ { * } ( E ) f _ { n } .
$$

Multiplication by $\phi ( E )$ shows that any solution $\{ y _ { n } \}$ of this method is

also a solution of $\operatorname { \rho } ( E { \bf \rho } ) y _ { n } = h \sigma ( E { \bf \rho } ) f _ { n }$ . The two methods are thus $L ^ { * }$ $\boldsymbol { C } _ { p + 1 } ^ { * }$

$$
\begin{array} { c } { { L \left( y , x , h \right) = \Phi ( E ) L ^ { * } ( y , x , h ) = C _ { p + 1 } ^ { * } h ^ { p + 1 } \Phi ( E ) y ^ { ( p + 1 ) } ( x ) + { \bf O } ( h ^ { p + 1 } ) , } } \\ { { { } } } \\ { { { } = C _ { p + 1 } ^ { * } \Phi ( 1 ) h ^ { p + 1 } y ^ { ( p + 1 ) } ( x ) + { \bf O } ( h ^ { p + 2 } ) } } \end{array}
$$

Cion one immeditely obtains $C _ { p + 1 } / \sigma ( 1 ) { = } C _ { p + 1 } ^ { * } / \sigma ^ { * } ( 1 )$ $C _ { p + 1 } { = } \Phi ( 1 ) C _ { p + 1 } ^ { * }$ and therefore also the rela hmethods thus hne thte same error constant.

The above analysis has shown that multistep methods whose generating polynomials have a common factor are not interesting. We therefore usually assume that

Multistep methods satisfying this property are called irreducible.

# The Peano kernel of a multistep method

The order and the error constant above do not yet give a com-$C _ { p + 1 }$ mula, to obtain a complete description of the error. The following discussion is an extension of the ideas of Peano (1913):

Theorem 2.8. Let the multistep method (2.1) be of order $\boldsymbol { p }$ and let $\eta \left( 1 \leq q \leq p \right)$ ） be an integer. For any $( q + 1 )$ times continuously differentiable function $y \left( x \right)$ we then have

where

$$
L \left( y , x , h \right) = h ^ { q + 1 } \int _ { 0 } ^ { k } K _ { q } ( s ) y ^ { \left( q + 1 \right) } ( x + s h ) d s ,
$$

$$
K _ { q } ( s ) = { \frac { 1 } { q ! } } \sum _ { i = 0 } ^ { k } \alpha _ { i } ( i - s ) _ { + } ^ { q } - { \frac { 1 } { ( q - 1 ) ! } } \sum _ { i = 0 } ^ { k } \mathfrak { p } _ { i } ( i - s ) _ { + } ^ { q - 1 }
$$

is called the $q$ -th Peano-kernel of the multistep method (3.1).

Remark. The notation

$$
( i - s ) _ { + } ^ { r } = \left\{ \begin{array} { c l l } { { \left( i - s \right) ^ { r } } } & { { \mathrm { f o r } } } & { { i - s > 0 } } \\ { { 0 } } & { { \mathrm { f o r } } } & { { i - s \leq 0 } } \end{array} \right.
$$

is used in the definition of the Peano-kernel. $\kappa _ { q } \left( s \right)$ is therefore

piece-wise a polynomial and satisfies

$$
K _ { q } ( s ) = { \frac { 1 } { q ! } } \sum _ { i = j } ^ { k } \alpha _ { i } ( i - s ) ^ { q } - { \frac { 1 } { ( q - 1 ) ! } } \sum _ { i = j } ^ { k } 8 _ { i } ( i - s ) ^ { q - 1 } \quad { \mathrm { f o r ~ } } s \in [ j - 1 , j ) ,
$$

Proof: Taylor's theorem with the integral representation of the rem ainder yields

$$
\begin{array} { l } { { \displaystyle ( x + i h ) = \sum _ { r = 0 } ^ { q } \frac { i ^ { r } } { r ! } h ^ { r } y ^ { ( r ) } ( x ) + h ^ { q + 1 } \int _ { 0 } ^ { \frac { i } { q } } \frac { ( i - s ) ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s , } } \\ { { \displaystyle + i h ) = \sum _ { r = 1 } ^ { q } \frac { i ^ { r - 1 } } { ( r - 1 ) ! } h ^ { r } y ^ { ( r ) } ( x ) + h ^ { q + 1 } \int _ { 0 } ^ { \frac { i } { ( q - 1 ) ! } } y ^ { ( q + 1 ) } ( x + s h ) d s } } \end{array}
$$

Inserting these two expressions into (2.3), the same considerations as in the proof of Theorem 2.4 show that for $q \leq p$ the polynomials before the integral are cancelled. The statement then follows from

$$
\int \limits _ { 0 } ^ { i } \frac { ( i - s ) ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s = \int \frac { k } { q ! } \frac { ( i - s ) _ { + } ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s .
$$

QED.

Besides the representation (2.15)， the Peano-kernel $K _ { q } ( s )$ has the following properties:

$$
s \in ( - \infty \mathrm { ~ , 0 } ) \cup [ k \mathrm { ~ , } \infty \mathrm { ~ ) ~ a n d ~ } q = 1 \mathrm { ~ , ~ . ~ . ~ , } p \mathrm { ~ ; ~ }
$$

$K _ { q } \left( s \right)$ is $( q - 2 )$ -times continuously differentiable and $\overset { \vartriangle { 1 } } { \boldsymbol { \mathcal { K } } _ { q } ^ { \prime } } ( s ) = - \boldsymbol { K } _ { q - 1 } ( s )$ for $q = 2 , \ldots , p$ (for $q = 2$ in the sense of distributions);

$\boldsymbol { K } _ { \mathrm { ~ \scriptsize ~ 1 ~ } } ( \boldsymbol { s } )$ is a piece-wise linear function with discontinuities at $0 , 1 \ , \ \dots , k \ .$ It has a jump of size ${ \mathsf { \beta } } _ { j }$ at the point $j$ and its slope over the interval $( j - \dot { 1 } , j ^ { \cdot }$ ）is given by $- ( \alpha _ { j } + \alpha _ { j + 1 } + \cdot \cdot \cdot + \alpha _ { k } )$

For the constant $C _ { p + 1 }$ of (2.8) we have

$$
C _ { p + 1 } { = } \intop _ { 0 } ^ { k } K _ { p } ( s ) d s .
$$

The proofs of Statements (2.16) to (2.19) are as follows: it is an immediate consequence of the definition of the Peano-kernel that $K _ { q } \left( s \right) = 0$ for $s \geq k$ and $q \leq p$ . In order to prove $K _ { q } \left( s \right) = 0$ also for $s \dot { < } 0$ we consider the polynomial $y \left( x \right) = ( x - s ) ^ { q }$ with $s$ as a parameter. Theorem 2.8 then shows that

$$
L \left( y , 0 , 1 \right) = \sum _ { i = 0 } ^ { k } \alpha _ { i } ( i - s ) ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } ( i - s ) ^ { q - 1 } \equiv 0 \qquad { \mathrm { f o r } } \quad q \leq p
$$

and hence $K _ { q . } \left( s \right) = 0$ for $s < 0$ . This gives (2.16). The relation (2.17) is seen by partial integration of (2.14). As an example, the Peanokernels for the 3-step Nystrom method $\left( 1 . 1 3 ^ { \circ } \right)$ ） are plotted in Figure 2.2.

![](images/54633242988b50c4c609225b2d7ae878089c97c2847fdb5cdf155a675a6333a8.jpg)  
Figure 2.2. Peano-kernels of the 3-step Nystrom method

# Exercises

1. Construction of multistep methods.

a) To any $k$ -th degree polynomial $\rho ( \zeta )$ satisfying $\rho \left( 1 \right) { = } 0$ there corresponds exactly one polynomial $\sigma \left( \zeta \right)$ of degree $\le k$ , such that the order of the corresponding multistep method is at least $k + 1$ b) In situation a) there exists exactly one polynomial $\sigma \left( \zeta \right)$ of degree $< k$ , such that the corresponding multistep method, which is then explicit, has order at least $k$ 、   
Hint. Condition ii) of Theorem 2.4.

2. Find the multistep method of the form

$$
y _ { n + 2 } + \alpha _ { 1 } y _ { n + 1 } + \alpha _ { 0 } y _ { n } \ = h \left( \beta _ { 1 } f _ { n + 1 } + \beta _ { 0 } f _ { n } \right)
$$

of the highest possible order. Try this formula on the example $y ^ { \prime } { = } y , y ( 0 ) { = } 1 , h { = } 0 . 1 ,$

3. Verify that the order and the error constant of the BDF-formulas are those of Table 2.1.

4. Show that the Peano-kernel $K _ { p } ( s )$ does not change sign for the explicit and implicit Adams methods and for the BDF-formulas. Deduce from this property that

$$
L \left( y , x , h \right) = h ^ { p + 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( \zeta ) \quad \mathrm { w i t h } \quad \zeta \in \left( x , x + k h \right) .
$$

where the constant $C _ { p + 1 }$ is given by (2.8).

5. Let $y \left( x \right)$ be an exact solution of $y ^ { \prime } { = } f \left( x \ , y \right)$ and let $\boldsymbol { y } _ { i } = \boldsymbol { y } \left( \boldsymbol { x } _ { i } \right) ,$ $i = 0 , 1 , \ldots , k - 1$ . Assume that $f$ is continuous and satisfies a Lipschitz condition with respect to y $( f$ not necessarily differentiable). Prove that for consistent multistep methods (i.e. Formula (2.6) holds) the local error satisfies

$$
\| ~ y ( x _ { k } ) - y _ { k } \| ~ \leq ~ h \omega ( h )
$$

where ${ \mathfrak { o } } ( h ) \to 0$ for h- 0.

# I11.3. Stability and the first Dahlquist barrier

hat der Verfasser seither ofters Verfahren zur numerischen Integration von Differentialgleichungen beobachtet, die, obschon zwar mit bestechend kleinem Abbruchfehler behaftet, doch die grosse Gefahr der numerischen Instabilitat in sich bergen." (H. Rutishauser, 1952)

Rutishauser observed in his famous paper that high order and a small local error are not sufficient for a useful multistep method. The numerical solution can be "unstable", even though the step size h is taken very small. The same observation was made by Todd (1950), who applied certain difference methods to second order differential equations. Our presentation will mainly follow the lines of Dahlquist (1956),where this effect has been studied systematically. An interesting presentation of the historical development of numerical stability concepts can be found in Dahlquist (1985) "33 years of numerical instability, Part I".

Let us start with an example, taken from Dahlquist (1956)， see Exercise 2 of Section I1.2. Among all explicit 2-step methods we con-sider the formula with the highest order. A short calculation using Theorem 2.4 shows that this method of order 3 is given by

$$
y _ { n + 2 } + 4 y _ { n + 1 } - 5 y _ { n } = h \left( 4 f _ { n + 1 } + 2 f _ { n } \right) .
$$

Application to the differential equation

$$
y ^ { \prime } = y , \qquad y ( 0 ) = 1
$$

yields the linear difference relation

$$
y _ { n + 2 } + 4 ( 1 - h ) y _ { n + 1 } - ( 5 + 2 h ) y _ { n } ~ = 0 ~ ,
$$

As starting values we take $y _ { 0 } = 1$ and $\boldsymbol { y } _ { 1 } \mathrm { = e x p } ( h )$ , the values on the exact solution. The numerical solution together with the exact solution $\operatorname { e x p } ( x )$ is plotted in Figure 3.1 for the step sizes $h = 1 / 1 0$ ， $h = 1 / 2 0$ ， $h = 1 / 4 0$ , etc. In spite of the small local error, the results are very bad. One observes in Figure 3.1 that the results become worse as the step size decreased.

An explanation for this effect can easily be given. As usual for linear difference equations (Lagrange (1775))， we insert $y _ { j } = \zeta ^ { j }$ into (3.3). This leads to the characteristic equation

$$
\zeta ^ { 2 } + 4 ( 1 { - } h ) \zeta - ( 5 + 2 h ) = 0 .
$$

![](images/88f81fc81928f7b806ae17bd4ce86d40e89c6a24516343c3db836eb174eda10f.jpg)  
Figure 3.1. Numerical solution of the instable method (3.1)

The general solution of (3.3) is then given by

$$
y _ { n } = A \ \zeta _ { 1 } ^ { \ n } ( h ) + B \ \zeta _ { 2 } ^ { \ n } ( h )
$$

where

$$
\zeta _ { 1 } ( h ) = 1 + h + { \bf O } ( h ^ { 2 } ) , ~ \zeta _ { 2 } ( h ) = - 5 + { \bf O } ( h )
$$

are the roots of (3.4) and the coefficients A and $B$ are determined by the starting values $y _ { 0 }$ and $y _ { 1 }$ Since $\boldsymbol { \zeta } _ { 1 } ( h )$ approximates $\exp ( h )$ ,the first term in (3.5) approximates the exact solution $\operatorname { e x p } ( x )$ at the point $x = n h$ . The second term in (3.5)， often called a parasitic solution, is the one which causes trouble in our method: since for $h  \mathrm { ~ 0 ~ }$ the absolute value of $\zeta _ { 2 } ( h )$ is larger than one, this parasitic solution becomes very large and dominates the solution $y _ { n }$ for increasing $n$

We now turn to the stability discussion of the general method (2.1). The essential part is the behaviour of the solution as $n  \infty$ (or $h  ~ 0 ^ { \prime }$ ） with nh fixed. We see from (3.3) that for $h  ~ 0$ we obtain

$$
\alpha _ { k } y _ { n + k } + \alpha _ { k - 1 } y _ { n + k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } y _ { n } = 0 .
$$

This can be interpreted as the numerical solution of the method (2.1) for the differential equation

$$
y ^ { \prime } = 0 .
$$

We put $y _ { j } = \zeta ^ { j }$ in (3.6), divide by $\zeta ^ { n }$ , and find that $\zeta$ must be a root of

$$
\rho ( \zeta ) = \alpha _ { k } \zeta ^ { k } + \alpha _ { k - 1 } \zeta ^ { k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } = 0 \ .
$$

As in Section I.5, we again have some difficulty when (3.8) possesses cise 1 below) a root of multiplicity $y _ { n } = n ^ { J - 1 } \zeta ^ { n } ( j = 1 , . . . , m ) ,$ $m > 1$ . In this case (Lagrange (1792), see Exer- are solutions of (3.6)and we obtain by superposition:

Lemma 3.1. Let $\zeta _ { 1 } , \ldots , \zeta _ { l }$ be the roots of $\rho \left( \zeta \right)$ , of respective muliplicity $m _ { \textrm { 1 } } , \dots , m _ { l }$ Then the general solution of $\left( 3 . 6 \right)$ is given by

$$
y _ { n } = p _ { 1 } ( n ) \zeta _ { 1 } ^ { n } + \cdot \cdot \cdot + p _ { l } ( n ) \zeta _ { l } ^ { n }
$$

where the $p _ { j } ( n )$ are potynomials of degree $m _ { j } - 1$ . NED.

Formula (3.9) shows us that for boundedness of $y _ { n }$ ，as $n  \infty$ ,we need that the roots of (3.8) lie in the unit disc and that the roots on the unit circle be simple.

Definition 3.2. The multistep method (2.1) is called stable, if the generating polynomial $\rho \left( \zeta \right)$ (Formula (3.8)) satisfies the root condition; i.e.

i) The roots of $\rho \left( \zeta \right)$ lie on or within the unit circle;   
ii) The roots on the unit circle are simple.

Remark. In order to distinguish this stability concept from others, it is sometimes called zero-stability or, in honour of Dahlquist, also $D$ -stability.

Examples: For the explicit and implicit Adams methods, $\scriptstyle \mathsf { p } ( \zeta ) = \zeta ^ { k } - \zeta ^ { k - 1 }$ Besides the simple root 1, there is a $( k - 1 )$ -fold root at 0. The Adams methods are therefore stable.

The same is true for the explicit Nystrom and the Milne-Simpson methods, where $\scriptstyle \ p ( \zeta ) = \zeta ^ { k } - \zeta ^ { k - 2 }$ Note that here we have a simple root at $- 1$ . This root can be dangerous for certain differential equations (see Volume II).

# Stability of the BDF-formulas

The investigation of the stability of the BDF-formulas is more diffcuit.Asthecharacteristicpolyomialof $\nabla ^ { j } y _ { k + n } = 0$ is given by $\zeta ^ { k - j } ( \zeta - 1 ) ^ { j } = 0$ it follows from the representation (1.22') that the generating polynomial $\rho ( \zeta )$ of the BDF-formulas has the form

$$
{ \sf p } ( \xi ) = \sum _ { j = 1 } ^ { k } \frac { 1 } { j } \xi ^ { k - j } ( \xi - 1 ) ^ { j } \mathrm { ~ . ~ }
$$

In order to study the zeros of (3.10) it is more convenient to consider the polynom ial

$$
p ( z ) = ( 1 { - } z ) ^ { k } \rho ( { \frac { 1 } { 1 - z } } ) = \sum _ { j = 1 } ^ { k } { \frac { z ^ { j } } { j } }
$$

via the transform ation $\zeta = 1 / ( 1 - z )$ . This polynomial is just the $k$ -th partial sum of $- \mathrm { l o g } ( 1 - z )$ . As the roots of $p \left( z \right)$ and $\rho ( \zeta )$ are related by the above transformation, we have:

![](images/d0cd4fcf56f438bbe5dde3d5903e54b09f66037fc96fd8695521e93a31b079cf.jpg)  
Figure 3.2. Roots of the polynomial $p \left( z \right)$ of (3.11)

Lemma 3.3. The k -step $B D F$ -formula (1.22') is stable iff all roots of the potynomial (3.11) are outside the disc $\{ z \ ; | z - 1 | | \leq 1 \}$ , with simple roots allowed on the boundary.

NED.

The roots of (3.11) are displayed in Figure 3.2 for different values of k .

Theorem 3.4. The k -step BDF-formula (1.22') is stable for $k \leq 6$ ， and unstable for $k \geq 7$

Proof. The first assertion can be verified simply by a finite number of numerical calculations (see Figure 3.2. This was first observed by Mitchell and Craggs (1953)). The second statement, however, contains an infinity of cases and is more difficult. The first complete proof was given by Cryer (1971) in a technical report， a condensed version of which is published in Cryer (1972). A second proof is given in Creedon and Miller (1975) (see also Grigorieff (1977), p.135), based on the Schur-Cohn criterion. This proof is outlined in Exercise 4 below. The following proof, which is given in Hairer and Wanner (1983), is based on the representation

$$
p \left( z \right) = \int _ { 0 } ^ { z } \sum _ { j = 1 } ^ { k } \zeta ^ { j - 1 } d \zeta = \int _ { 0 } ^ { z } \frac { 1 - \zeta ^ { k } } { 1 - \zeta } d \zeta = \int _ { 0 } ^ { r } { { { \left( 1 - e ^ { i k \theta } s ^ { k } \right) } } } \Phi ( s ) d s
$$

with

$$
\zeta = s e ^ { i \theta } , \qquad z = r e ^ { i \theta } , \qquad \Phi ( s ) = \frac { e ^ { i \theta } } { 1 - s e ^ { i \theta } } .
$$

We cut the complex plane into $k$ sectors

$$
S _ { j } ~ = ~ \biggl \{ z ; ~ \frac { 2 \pi } { k } ( j - \frac { 1 } { 2 } ) < \arg ( z ) < \frac { 2 \pi } { k } ( j + \frac { 1 } { 2 } ) \biggr \} , ~ j = 0 , 1 ~ , \ldots , k - 1 ~ .
$$

On the rays bounding $S _ { j }$ we have $e ^ { i k \ \theta } = - 1$ , so that from (3.12)

$$
p ( z ) = \int _ { 0 } ^ { r } ( 1 + s ^ { k } ) \phi ( s ) d s
$$

always _lies in the angle spanned by with a positive weight function. Therefore the argument of $\phi ( s ) ,$ i.e. the angle between $\begin{array} { c } { { \left( z \atop e \right) } } \end{array}$ and $e ^ { i \pi } = - 1$ .So no revolution of $\arg ( p \left( z \right) )$ is possible on these rays, and due to the one revolution of $\arg ( z ^ { k } )$ at infinity between $\scriptstyle \theta = 2 \pi { \bigl ( } j - 1 / 2 { \bigr ) } / k$ and $\theta { = } 2 \pi ( j + 1 / 2 ) / k$ the principle of the argument (e.g. Henrici (1974), p.278) implies (see Figure 3.3) that in each sector $S _ { j }$ $, ( j = 1 , \ldots , k - 1$ ， with the exception of $j = 0$ ）there lies exactly one root of $p \left( z \right)$

![](images/93cbad297a6ee76a971d0ad05c13444f01fe18773518679853e5b5dfb2be0bb4.jpg)  
Figure 3.3. Argument of p(z ) of (3.11)

In order to complete the proof, we still have to bound the zeros of $p \left( z \right)$ from above: we observe that in (3.12) the term $s ^ { k }$ becomes large for $s > 1$ .We therefore partition (3.12) into two integrals $p \left( z \right) { = } I _ { 1 } { - } I _ { 2 } ,$ where

$$
I _ { 1 } = \int \displaylimits _ { 0 } ^ { r } \Phi ( s ) d s - \int \displaylimits _ { 0 } ^ { 1 } e ^ { i k \theta } s ^ { k } \Phi ( s ) d s , I _ { 2 } = e ^ { i k \theta } \int \displaylimits _ { 1 } ^ { r } s ^ { k } \Phi ( s ) d s .
$$

Since $| \phi ( s ) | \leq B$ (0）where

$$
B \left( \boldsymbol { \Theta } \right) = \left\{ \begin{array} { c c c } { \displaystyle \frac { 1 } { \sin \theta } \quad } & { 0 < \boldsymbol { \Theta } \leq \displaystyle \frac { \pi } { 2 } } \\ { \displaystyle 1 \quad } & { \displaystyle \frac { \pi } { 2 } \leq \boldsymbol { \Theta } \leq \pi \ , } \end{array} \right.
$$

we obtain

$$
I _ { 1 ^ { ! } } ~ \le ~ ( r + \frac { 1 } { k + 1 } ) B \left( \theta \right) < ~ r B \left( \theta \right) \frac { k + 2 } { k + 1 } ~ , ~ ( r > 1 ) ~ .
$$

Secondly, since $s ^ { k }$ is positive,

$$
I _ { \ 2 } = e ^ { i k { \ \theta } } \Phi { \int _ { 1 } ^ { r } } s ^ { k } d s \ \quad \ \mathrm { ~ w i t h ~ } \quad \Phi \in \mathrm { c o n v e x ~ h u l l ~ o f ~ } \{ \Phi ( s ) ; \ 1 \leq s \leq r \} \ .
$$

Any element of the above convex hull can be written in the form

$$
\Phi = \alpha \phi ( s _ { 1 } ) + ( 1 { - } \alpha ) \phi ( s _ { 2 } ) = \frac { \phi ( s _ { 1 } ) \phi ( s _ { 2 } ) } { \phi ( \hat { s } ) }
$$

with $\hat { s } = \alpha s _ { 2 } + ( 1 - \alpha ) s _ { 1 } , 0 \leq \alpha \leq 1 , 1 \leq s _ { 1 } , s _ { 2 } \leq r .$ Since $\phi ( s )$ decreases monotonically for $s \geq 1$ ，we _have $\Phi \ge _ { ; \Phi } ( r )$ . Some elementary geometry then leads to $\left| \Phi \right| \geq \frac { 1 } { 2 r }$ and we get

$$
I _ { 2 } | \ \cong \ \frac { r ^ { k + 1 } - 1 } { 2 r ( k + 1 ) } > \ \frac { r ( r ^ { k - 1 } - 1 ) } { 2 k + 2 } \ , ( r > 1 ) \ .
$$

From (3.13) and (3.14) we see that

$$
r \geq R \ ( \theta ) \ = \ \left( ( 2 k + 4 ) B \left( \theta \right) + 1 \right) ^ { 1 / \left( k - 1 \right) }
$$

im plies $I _ { 2 } > I _ { 1 }$ ,so that $p \left( z \right)$ cannot be zero. The curve $R$ (0）is aiso plotted in Figure 3.2 and cuts from the sectors $S _ { j }$ what we call Madam Imhof's cheese pie,each slice of which (with $j \neq 0$ ）must contain a zero of $p \left( z \right)$ A simple analysis shows that for $k = 1 2$ the cheese pie, cut from $S  { 1 }$ , is small enough to ensure the presence of zeros of $p \left( z \right)$ inside the disc $\{ z \ ; \ z - 1 \ \leq 1 \}$ As $R$ (0), for fixed 0, as well as $R$ $\pi / k$ ） are monotonically decreasing in $k$ ，the same is true for all $k \geq 1 2$ .For $6 < k < 1 2$ numerical calculations show that the method is unstable (see Figure 3.2 or Exercise 4). QED.

# Highest attainable order of stable multistep methods

It is a natural task to investigate the stability of the multistep methods with highest possible order. This has been performed by Dahlquist (1956), resulting in the famous "first Dahlquist-barrier".

Counting the order conditions (Theorem 2.4) shows that for order $p$ the parameters of a linear multistep method have to satisfy $p + 1$ linear equations. As $2 k + 1$ free parameters are involved (without loss of generality one can assume ${ \alpha } _ { k } = 1$ ), this suggests that $2 k$ is the highest attainable order. Indeed, this can be verified (see Exercise 5). However, these methods are of no practical significance, because we shall prove

Theorem 3.5. (The first Dahlquist-barrier). The order p of a stable linear k -step method satisfies

$p \leq k + 2$ if k is even,   
$p \leq k + 1$ if k is odd,   
p≤k if βk/αk≤O (in particular if the method is explicut).

We postpone the verification of this theorem and give some notations and lemmas, which will be useful for the proof. First of all we introduce the "Greek-Rom an transform ation"

$$
 \zeta = \frac { z + 1 } { z - 1 } \qquad \mathrm { o r } \qquad z = \frac { \zeta + 1 } { \zeta - 1 } \ .
$$

This transformation maps the disk $| \zeta | < 1$ onto the half-plane $\mathrm { R e } z < 0$ ， the upper half-plane $\mathrm { I m } z > 0$ onto the lower half-plane, the circle $| \zeta | = 1$ to the imaginary axis, the point $\zeta = 1$ to $z = \infty$ and the point $\zeta = - 1$ to $z = 0$ . We then consider the polynomials

$$
\begin{array} { l } { { R \left( z \right) = \left( \displaystyle \frac { z - 1 } { 2 } \right) ^ { k } \rho ( \zeta ) = \sum _ { j = 0 } ^ { k } a _ { j } z ^ { j } \mathrm { ~ , ~ } } } \\ { { \displaystyle S \left( z \right) = \left( \displaystyle \frac { z - 1 } { 2 } \right) ^ { k } \sigma ( \zeta ) = \sum _ { j = 0 } ^ { k } b _ { j } z ^ { j } \mathrm { ~ . ~ } } } \end{array}
$$

Since the zeros of R (z) and of $\rho \left( \zeta \right)$ are connected via the transformation (3.16)， the stability condition of a multistep method can be formulated in terms of $R \ ( z )$ as follows: all zeros of $R \ ( z )$ lie in the negative half-plane Re $z \le 0$ and no multiple zero of $R$ （ $z$ ）lies on the im aginary axis.

Lemma 3.6. Suppose the multistep method to be stable and of order at least O. We then have

i） $a _ { k } = 0$ and $a _ { k - 1 } { = } 2 ^ { 1 - k } \rho ^ { \prime } ( 1 ) \neq 0 ;$

ii) All non-vanishing coefficients of $R$ (z) have the same sign.

Proof: Dividing Formula (3.17) by $z ^ { k }$ and putting $z = \infty$ ,one sees that $a _ { k } = 2 ^ { - k } \rho ( 1 )$ . This expression must vanish, because the method is of order O. In the same way one gets ${ a _ { k } } _ { - 1 } { = } 2 ^ { 1 - k } \rho ^ { \prime } ( 1 )$ ， which is different from zero, since by stability 1 cannot be a multiple root of