# CHAPTER XI

# The Theory of Closure and Completeness

11.1 The Fundamental Theorem of Closure and Completeness. Theorem 8.9.l related the concepts of closure and completeness for inner product spaces.In the present section，we shall do this for normed linear spaces.

DEFINITIoN ll.1.1． The sequence of elements $\left\{ x _ { k } \right\}$ is complete in a normed linear space $\pmb { X }$ if $L ( x _ { k } ) = 0$ ， $k = 1$ ,2,..., $\ b { L } \in \ b { X } ^ { * }$ ,implies $\mathbf { L } = \mathbf { 0 }$ $X ^ { * }$ is the normed conjugate space of $\pmb { X }$

(In an inner product space,there are now two definitions of complete sequences,Definition 8.9.4 and Defnition l1.1.1. If the space is complete, these definitions are equivalent.)

<table><tr><td rowspan="2">Space</td><td>Closed</td><td>Complete</td></tr><tr><td>A subspace is closed if it contains all its limit points.</td><td>A space is complete if every Cauchy sequence has a limit in the space.</td></tr><tr><td>Sequence</td><td>A sequence is closed if every element of the space can be approximated ar- bitrarilycloselyby finite linear combinations of the elements of the sequence.</td><td>A sequence {xn} is complete if L(xn)=0,n=0,1,..., L ∈X*,implies L=0.</td></tr></table>

The fundamental theorem is that closure and completeness are equivalent concepts.This emerges as a consequence of the Hahn-Banach Extension Theorem,and it is to this that we now turn.

DEFINITION 11.1.2．Let $\pmb { X }$ be a linear space and $\pmb { Y }$ a linear subspace. Let $L$ be a linear functional defined on $\pmb { Y }$ .A linear functional $L _ { 1 }$ is called an extension of $\pmb { L }$ to $\pmb { X }$ if $L _ { 1 } ( x )$ is defined for all ${ \pmb x } \in { \pmb X }$ and if $L _ { 1 } ( x ) = L ( x )$ for $\pmb { x } \in \pmb { Y }$

Ex.1. $\pmb { X }$ is the space of all functions defined on $[ a , b ]$ .Let $\pmb { Y }$ be the subspace $C [ \pmb { a } , \pmb { b } ]$ Let $a < x _ { 1 } < b$ and set $L ( f ) = \operatorname* { l i m } f ( x )$ .Let $L _ { 1 } ( f ) = f ( x _ { 1 } )$ Then $\mathbf { L _ { 1 } }$ is an extension of $\pmb { L }$ from $\pmb { Y }$ to $x$ $\pmb { x } \mathrm {  } \pmb { x } _ { 1 }$ -

THEOREM 11.1.1．Let $\pmb { X }$ be $^ { \pmb { a } }$ real normed linear space and $\pmb { Y }$ a linear subspace. ( $Y \neq X .$ .Let ${ \pmb p } ( { \pmb x } )$ be a real valued functional defined on the elements of $\pmb { X }$ and possessing the following normlike properties

$$
\begin{array} { r l } { p ( x ) \geq 0 ; } & { \quad x \in X } \\ { p ( x + y ) \leq p ( x ) + p ( y ) ; } & { \quad x , y \in X } \\ { p ( \lambda x ) = \lambda p ( x ) ; } & { \quad x \in X , \lambda \geq 0 . } \end{array}
$$

Let $L$ be $^ { \pmb { a } }$ real linear functional defined on $Y$ that satisfies

$$
L ( x ) \leq p ( x ) , \qquad x \in Y .
$$

Then $L$ can be extended to be $^ { \pmb { a } }$ linear functional $L _ { 1 }$ defined on $\pmb { X }$ and such that

$$
L _ { 1 } ( x ) \leq p ( x ) , \qquad x \in X .
$$

Proof: 1. Select an $\pmb { x _ { 0 } } \in X$ but $\notin Y$ Take $\textstyle { \pmb { x } } , y \in { \pmb { Y } }$ Then

$$
L ( y ) - L ( x ) = L ( y - x ) \leq p ( y - x ) .
$$

Now $p ( y - x ) \leq p ( y + x _ { 0 } ) + p ( - x - x _ { 0 } )$ so that

$$
- p ( - x - x _ { 0 } ) - L ( x ) \leq p ( y + x _ { 0 } ) - L ( y ) ; \qquad x , y \in Y .
$$

Think of $_ y$ as fixed in $\pmb { Y }$ and $_ { \pmb { x } }$ as varying in $\pmb { Y }$ .Then the last inequality shows that $- p ( - x - x _ { 0 } ) - L ( x )$ is bounded above. Similarly,for varying $y , p ( y + x _ { 0 } ) - L ( y )$ is bounded below.If we set

$$
\begin{array} { l } { r _ { 1 } = \underset { x \in Y } { \operatorname* { s u p } } \left[ - p ( - x - x _ { 0 } ) - L ( x ) \right] } \\ { r _ { 2 } = \underset { y \in Y } { \operatorname* { i n f } } \left[ p ( y + x _ { 0 } ) - L ( y ) \right] } \end{array}
$$

then we must have $- \infty < r _ { 1 } \le r _ { 2 } < \infty$ .Select a number $\pmb { r }$ such that $r _ { 1 } \leq r \leq r _ { 2 } .$ Then,

$$
- p ( - x - x _ { 0 } ) - L ( x ) \leq r \leq p ( y + x _ { 0 } ) - L ( y )
$$

for any $\textstyle { \boldsymbol { \mathfrak { x } } } , { \boldsymbol { \mathfrak { y } } } \in Y$

2.Consider the linear subspace $Y _ { 0 }$ consisting of all elements $_ y$ of the form $y = x + \lambda x _ { 0 }$ ， $\pmb { x } \in \pmb { Y }$ .Each element in $\mathbf { { \mathit { Y } } _ { 0 } }$ has a unique representation in this form. For suppose, $y \in Y _ { \mathbf { \pmb { \theta } } }$ and $y = x _ { 1 } + \lambda _ { 1 } x _ { 0 } = x _ { 2 } + \lambda _ { 2 } x _ { 0 }$ Then $x _ { 1 } - x _ { 2 } = ( \lambda _ { 1 } - \lambda _ { 2 } ) x _ { 0 }$ If $\lambda _ { 1 } \neq \lambda _ { 2 }$ then $\pmb { x _ { 0 } }$ would be a linear combination of ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } }$ and hence in $\pmb { Y }$ .This contradicts our selection of $\pmb { x _ { 0 } }$ . Therefore $\lambda _ { 1 } = \lambda _ { 2 }$ and hence also 𝑥1 = x2.

Define $L _ { 1 }$ on $\boldsymbol { Y } _ { \boldsymbol { \mathfrak { o } } }$ by means of

$$
L _ { 1 } ( y ) = L ( x ) + \lambda r .
$$

Now if $y \in Y , \lambda = 0$ and hence $L _ { 1 } ( y ) = L ( y )$ ， $y \in Y$ Since $\pmb { L }$ is linear,it follows easily that $L _ { 1 }$ is linear.

We wish to prove next that

$$
L _ { 1 } ( y ) \leq p ( y ) \qquad { \mathrm { f o r ~ a l l } } \quad y \in Y _ { 0 } .
$$

Decompose $_ y$ into the form $y = x _ { 1 } + \lambda x _ { 0 }$ .We need only deal with the case when $\lambda \neq 0$ .From (11.1.4) we have

$$
- p \Big ( - \frac { x _ { 1 } } { \lambda } - x _ { 0 } \Big ) - L \Big ( \frac { x _ { 1 } } { \lambda } \Big ) \leq r \leq p \Big ( \frac { x _ { 1 } } { \lambda } + x _ { 0 } \Big ) - L \Big ( \frac { x _ { 1 } } { \lambda } \Big ) .
$$

Now if $\lambda > 0 , p \Big ( \frac { x _ { 1 } } { \lambda } + x _ { 0 } \Big ) = \frac { 1 } { \lambda } p ( x _ { 1 } + \lambda x _ { 0 } )$ and the second inequality reduces to

$$
r \leq { \frac { 1 } { \lambda } } p ( x _ { 1 } + \lambda x _ { 0 } ) - { \frac { 1 } { \lambda } } L ( x _ { 1 } )
$$

or

$$
L _ { 1 } ( y ) = L ( x _ { 1 } ) + \lambda r \leq p ( x _ { 1 } + \lambda x _ { 0 } ) .
$$

If $\lambda < 0$ ,the first inequality may be employed:

$- p \left( - { \frac { x _ { 1 } } { \lambda } } - x _ { 0 } \right) = { \frac { 1 } { \lambda } } p ( x _ { 1 } + \lambda x _ { 0 } ) ; { \mathrm { h e n c e } } , p ( x _ { 1 } + \lambda x _ { 0 } ) - L ( x _ { 1 } ) \geq \lambda r$ and the conclusion is as before.

3.Consider,finally,all the linear functionals that extend $L$ to some linear subspace containing $\pmb { Y }$ and which satisfy the condition (ll.1.5).A partial ordering $L ^ { \prime } \leq L ^ { \prime }$ is defined amongst these functionals by agreeing that $L ^ { \prime } \leq L ^ { \prime \prime }$ means that $L ^ { \prime \prime }$ is an extension of $L ^ { \prime }$ .With this ordering, every totally ordered subset is seen to have an upper bound,i.e., the functional which is defined over the union of the domains of definition of the individual functionals and which takes on the values assgned by them. Zorn's Lemma (Theorem l.l3.l) tells us that there exists a maximal extension $L _ { 1 }$ .This linear functional is defined over the entire space $\pmb { X }$ ,for if not, it could have been further extended by the process described under 2.

If the space $\pmb { X }$ is separable,the use of Zorn's Lemma (and hence the axiom of choice) can be avoided.

A functional ${ \pmb p } ( { \pmb x } )$ satisfying ll.1.1 is known as $^ { \pmb { a } }$ convex functional.

THEOREM 11.l.2 (Hahn-Banach). Let $\pmb { X }$ be $^ { \pmb { a } }$ real normed linear space and $\pmb { Y }$ a subspace. Let $L$ be defined on $\pmb { Y }$ and have norm $\| L \| _ { \mathcal { F } }$ there. Then there is $^ { \pmb { a } }$ linear functional $L _ { 1 }$ which extends $\scriptstyle { \cal L }$ to $\pmb { X }$ and such that $\| L _ { 1 } \| _ { X } =$ $\| L \| _ { Y }$

Proof: Set $p ( { \pmb x } ) = \| { \pmb L } \| _ { V } \| { \pmb x } \|$ . The functional ${ \pmb p } ( { \pmb x } )$ is readily seen to fulfll the requirements (li.l.l). Therefore, by the previous theorem，we may extend $\pmb { L }$ to $L _ { 1 }$ so that

$$
L _ { 1 } ( x ) \leq \| L \| _ { Y } \| x \| , \qquad x \in X .
$$

Since also

$$
- L _ { 1 } ( x ) = L _ { 1 } ( - x ) \leq \| L \| _ { Y } \| - x \| = \| L \| _ { Y } \| x \| ,
$$

it follows that

$$
\left| L _ { 1 } ( x ) \right| \leq \left\| L _ { 1 } ^ { \prime } \right\| _ { Y } \left\| x \right\| .
$$

Hence,

$$
\operatorname* { s u p } _ { x \in X } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } \leq \| L \| _ { Y }
$$

so that

$$
\| L _ { 1 } \| \leq \| L \| _ { Y } .
$$

But $\| L \| _ { Y } = \operatorname* { s u p } _ { x \in Y } { \frac { | L ( x ) | } { \| x \| } } = \operatorname* { s u p } _ { x \in Y } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } \leq \operatorname* { s u p } _ { x \in X } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } = \| L _ { 1 } \| _ { X }$ and therefore $\| L \| _ { Y } \leq \| L _ { 1 } \| _ { X }$ Thus,finally $\| L _ { 1 } \| _ { X } = \| L \| _ { Y }$

This extension theorem also holds in complex normed linear spaces.To establish this,we make use of a simple device which associates a unique real normed linear space $X _ { R }$ to each complex normed linear space $\pmb { X }$ In this way,the burden of the proof is thrown back to the real situation.

DEFINITION 11.1.3． Let $\pmb { X }$ be a complex normed linear space.The space $X _ { R }$ will consist of the same elements as $\pmb { X }$ .Addition in $\scriptstyle { X _ { R } }$ will be identical with addition in $\pmb { X }$ If $\pmb { a }$ is real and ${ \boldsymbol { x } } \in { \boldsymbol { X } } _ { R }$ then $\pmb { a x }$ will be the element $( a + i 0 ) x = a x$ of $\pmb { X }$ $\| x \|$ in $X _ { R }$ will equal $\| x \|$ in $\pmb { X }$ .If $L$ is a bounded (and complex) linear functional defined on $\pmb { X }$ ,then by $L _ { R }$ we shall mean the real valued functional defined on $X _ { R }$ by means of

$$
L _ { R } ( x ) = { \mathrm { R e a l ~ p a r t ~ o f ~ } } L ( x ) .
$$

The $_ { \pmb { x } }$ in the left-hand member is considered to lie in $X _ { R }$ while in the right it is considered to lie in $\pmb { X }$

LEMMA 11.1.3．If $\scriptstyle { \cal L }$ is $^ { \pmb { a } }$ bounded linear functional on $\pmb { X }$ then $L _ { R }$ is $^ { \pmb { a } }$ bounded linear functional on $X _ { R }$

Proof: Let $_ { \pmb { x } }$ $\mathfrak { e } , \mathfrak { y } \in  {  { \cal X } } _ { R }$ and $a , b$ be real.

$$
{ \begin{array} { r l } & { L _ { R } ( a x + b y ) = \operatorname { R e } L ( a x + b y ) } \\ & { \qquad = \operatorname { R e } { \big \{ } a L ( x ) + b L ( y ) { \big \} } = a \operatorname { R e } L ( x ) + b \operatorname { R e } L ( y ) } \\ & { \qquad = a L _ { R } ( x ) + b L _ { R } ( y ) . } \end{array} }
$$

Therefore $L _ { R }$ is linear on $X _ { R }$ Also

$$
| L _ { R } ( x ) | = | { \mathrm { R e } } L ( x ) | \leq | L ( x ) | \leq \| L \| \ \| x \| _ { x } = \| L \| \ \| x \| _ { X _ { R } } .
$$

Therefore $L _ { R }$ is bounded on $X _ { R }$ ,and $\| L _ { R } \| \leq \| L \|$

LEMMA 11.1.4.If $L$ is a linear functional on $\pmb { X }$ then

$$
L ( x ) = L _ { R } ( x ) - i L _ { R } ( i x ) .
$$

Conversely if $\Lambda$ is $\pmb { a }$ linear functional on $X _ { R }$ , then the equation

$$
L ( x ) = \Lambda ( x ) - i \Lambda ( i x )
$$

defines a linear functional on $\pmb { X }$

Proof: If $L ( x ) = \operatorname { R e } L ( x ) + i \operatorname { I m } L ( x ) , x \in X$ ，then

$$
\begin{array} { r } { L ( i x ) =  { \mathrm { R e } } L ( i x ) + i  { \mathrm { I m } } L ( i x ) } \\ { = i  { \mathrm { R e } } L ( x ) -  { \mathrm { I m } } L ( x ) . } \end{array}
$$

Therefore Im $L ( x ) = - \mathrm { R e } L ( i x ) = - L _ { R } ( i x )$ ,so (11.1.8) follows.Conversely, given $\textstyle { \boldsymbol { \mathscr { x } } } , y \in X$ ,from (ll.l.9) we see that

$$
\begin{array} { r l } & { L ( { \pmb x } + { \pmb y } ) = \Lambda ( { \pmb x } + { \pmb y } ) - i \Lambda ( i { \pmb x } + i { \pmb y } ) } \\ & { \qquad = \Lambda ( { \pmb x } ) + \Lambda ( { \pmb y } ) - i \Lambda ( i { \pmb x } ) - i \Lambda ( i { \pmb y } ) } \\ & { \qquad = L ( { \pmb x } ) + L ( { \pmb y } ) . } \end{array}
$$

Moreover, if $\pmb { a }$ is real,

$$
\begin{array} { c } { { L ( a x ) = \Lambda ( a x ) - i \Lambda ( i a x ) } } \\ { { = a \Lambda ( x ) - i a \Lambda ( i x ) = a L ( x ) . } } \end{array}
$$

Finally,

$$
\begin{array} { c } { { L ( i x ) = \Lambda ( i x ) - i \Lambda ( - x ) } } \\ { { = i [ \Lambda ( x ) - i \Lambda ( i x ) ] = i L ( x ) . } } \end{array}
$$

Thus, $\pmb { L }$ is linear over $\pmb { X }$

THEOREm 1l.1.5 (Bohnenblust-Sobczyk-Suchomlinoff). Let $\pmb { X }$ be a complex normed linear space and $\pmb { Y }$ a subspace. Let $\scriptstyle { \cal L }$ be a complex linear functional defined on $\boldsymbol { Y }$ and have norm $\| L \| _ { Y }$ there.Then there is $^ { \pmb { a } }$ linear functional $L _ { 1 }$ that extends $L$ to $\pmb { X }$ and such that $\| L _ { 1 } \| _ { X } = \| L \| _ { Y }$

Proof: Write $L ( x ) = L _ { R } ( x ) + i L _ { I } ( x )$ ， ${ \pmb x } \in { \pmb Y }$ where $L _ { R }$ and $L _ { I }$ are real valued. By Lemma l1.1.3, $L _ { R }$ is a bounded real valued linear functional defined on $Y _ { R }$ ，the real normed linear space associated with $\boldsymbol { Y }$ .Extend $L _ { R }$ to $X _ { R }$ by Theorem ll.l.2,and obtain a real,bounded, linear functional $L _ { 1 , R }$ for which ${ \cal L } _ { 1 , R } ( x ) = { \cal L } _ { R } ( x ) ;$ ${ \pmb x } \in { \pmb Y } _ { \pmb R }$ and for which $\| L _ { 1 , R } \| = \| L _ { R } \|$ Define

$$
L _ { 1 } ( x ) = L _ { 1 , R } ( x ) - i L _ { 1 , R } ( i x ) .
$$

By Lemma 11.1.4, $L _ { 1 }$ is a linear functional defined on the whole of $\pmb { X }$ It is an extension of $\scriptstyle { \cal L }$ For let ${ \pmb x } \in { \pmb Y }$ .Then,by (ll.1.8)(taking the $\pmb { X }$ as the present $\boldsymbol { Y }$ ，

$$
L ( x ) = L _ { R } ( x ) - i L _ { R } ( i x ) = L _ { 1 , R } ( x ) - i L _ { 1 , R } ( i x ) = L _ { 1 } ( x ) .
$$

We must finally prove that $\| L _ { 1 } \| = \| L \|$ . Since $L _ { 1 }$ is an extension of $\pmb { L }$ ,it is clear that $\| L \| \leq \| L _ { 1 } \|$ . On the other hand,suppose that $L _ { 1 } ( x ) = r e ^ { i \theta }$ $\pmb { x } \in \pmb { X }$ . Then,

$$
\begin{array} { r l } & { | L _ { 1 } ( x ) | = r = \mathrm { R e } L _ { 1 } ( e ^ { - i \theta } x ) = L _ { 1 , R } ( e ^ { - i \theta } x ) \leq \| L _ { 1 , R } \| \| e ^ { - i \theta } x \| } \\ & { \qquad = \| L _ { 1 , R } \| \| x \| = \| L _ { R } \| \| x \| \leq \| L \| \| x \| . } \end{array}
$$

The last inequality was observed after (ll.1.7).Therefore,for all ${ \pmb x } \in { \pmb X }$ ， $\frac { | L _ { 1 } ( x ) | } { \| x \| } \leq \| L \|$ ,so that $\| L _ { 1 } \| \leq \| L \|$ . Thus, $\| L _ { 1 } \| = \| L \|$

THEOREM 11.1.6．Let $\pmb { X }$ be $^ { \pmb { a } }$ normed linear space and $\pmb { Y }$ a linear subspace. Let $\pmb { x _ { 0 } } \in X$ ,but ${ \pmb x _ { 0 } } \notin Y$ and suppose that $d = \operatorname* { i n f } _ { y \in Y } \| y - x _ { 0 } \| > 0$ . Then we can find $^ { \pmb { a } }$ bounded linear functional, $\scriptstyle { \cal L }$ ,on $\pmb { X }$ such that

$$
\begin{array} { c c } { { L ( x ) = 0 } } & { { \quad x \in Y } } \\ { { } } & { { } } \\ { { L ( x _ { 0 } ) = 1 } } & { { } } \\ { { \| L \| = d ^ { - 1 } . } } & { { } } \end{array}
$$

Proof:As in Theorem l1.1.1, let $\mathbf { { \mathit { Y } } _ { 0 } }$ be the linear subspace of elements of the form $\pmb { \mathscr { x } } + \lambda \pmb { \mathscr { x } } _ { \mathbf { 0 } }$ ， $\pmb { x } \in \pmb { Y }$ .This decomposition is unique.Construct an $L$ over $\mathbf { { \mathit { Y } } _ { 0 } }$ as follows :

$$
L ( y ) = \lambda \quad { \mathrm { f o r } } \quad y = x + \lambda x _ { 0 } .
$$

In particular, $L ( { \pmb x } ) = \mathbf { 0 }$ whenever $\pmb { x } \in \pmb { Y }$ ，and $L ( x _ { 0 } ) = L ( 0 + 1 \cdot x _ { 0 } ) = 1$ Now

$$
{ \begin{array} { r l } & { \quad \displaystyle { \frac { | L ( y ) | } { \| y \| } } = \displaystyle { \frac { | \lambda | } { \| y \| } } = \displaystyle { \frac { | \lambda | } { \| x + \lambda x _ { 0 } \| } } = \displaystyle { \frac { 1 } { \left\| { \frac { x } { \lambda } } + x _ { 0 } \right\| } } = \displaystyle { \frac { 1 } { \left\| x _ { 0 } - \left( - { \frac { x } { \lambda } } \right) \right\| } } . } \\ & { \quad \mathrm { S i n c e } - \displaystyle { \frac { x } { \lambda } } \in Y , { \bigg \| } x _ { 0 } - \left( - { \frac { x } { \lambda } } \right) { \bigg \| } \geq d . } \end{array} }
$$

Hence

$$
\| L \| _ { Y _ { 0 } } = \operatorname* { s u p } _ { y \in Y _ { 0 } } \frac { | L ( y ) | } { \| y \| } \leq \frac { 1 } { d } .
$$

On the other hand,we can find a sequence of elements $\{ x _ { n } \} \in Y$ such that $\operatorname* { l i m } _ { n \to \infty } \| x _ { n } - x _ { 0 } \| = d$ Now ${ \pmb x _ { n } } - { \pmb x _ { 0 } } \in { \pmb Y _ { 0 } }$ so that

$$
| L ( x _ { n } - x _ { 0 } ) | \leq \| L \| _ { Y _ { 0 } } \| x _ { n } - x _ { 0 } \| .
$$

But $L ( x _ { n } ) = 0$ ， ${ \pmb n = 1 , 2 , \dots }$ ,and $L ( x _ { 0 } ) = 1$

Hence,

so that

$$
\begin{array} { l } { 1 \leq \| L \| _ { { Y _ { 0 } } } \| x _ { n } - x _ { 0 } \| , } \\ { 1 \leq \| L \| _ { { Y _ { 0 } } } d . } \end{array}
$$

Thefore $\Vert L \Vert _ { \textbf { \tiny { F _ { 0 } } } } \geq \frac { 1 } { d }$ and we must have

$$
\Vert L \Vert _ { Y _ { 0 } } = \frac { 1 } { d } .
$$

We now apply Theorem l1.1.5 to extend $L$ from $Y _ { \mathbf { 0 } }$ to $\pmb { X }$ with preservation of norm.

THEOREM 11.1.7 (Banach).Let $\pmb { X }$ be a normed linear space (real or complex). $\pmb { A }$ sequence of elements $\left\{ x _ { k } \right\}$ is closed if and only if it is complete.

Proof: Suppose $\left\{ x _ { k } \right\}$ is closed. Let $L \in X ^ { * }$ and suppose that $L ( x _ { k } ) = 0$ $k = 1$ ,2,.... Given any ${ \pmb x } \in { \pmb X }$ ，we may approximate $_ { x }$ arbitrarily closely by finite combinations of $x _ { k } \colon \| x - a _ { 1 } x _ { 1 } - a _ { 2 } x _ { 2 } - \cdot \cdot \cdot - a _ { n } x _ { n } \| \leq \varepsilon$ for some coefficients $\pmb { a } _ { \pmb { k } }$ Then,

$$
\begin{array} { r } { | L ( x ) | = | L ( x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { n } x _ { n } ) | \medskip \qquad } \\ { \leq \| L \| \| x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { n } x _ { n } \| \leq \| L \| \varepsilon . } \end{array}
$$

Allow $\varepsilon \to 0$ and obtain $L ( x ) = 0$ Since $\pmb { x }$ is arbitrary, $\mathbf { \nabla } L = \mathbf { 0 }$

Conversely, suppose that $L ( x _ { k } ) = 0 , k = 1 , 2 , . . . ,$ implies $\mathbf { \nabla } L = \mathbf { 0 }$ Let $\pmb { x _ { 0 } }$ be an element of $\pmb { X }$ and let $\boldsymbol { Y }$ be the linear subspace comprised of all finite linear combinations of $x _ { 1 } , x _ { 2 } , \ldots .$ We wish to prove $d = \operatorname* { i n f } _ { y \in Y } \| x _ { 0 } - y \| = 0$ Suppose the contrary.Then by the previous theorem，we can find an $\pmb { L }$ such that $\boldsymbol { L } ( y ) = \boldsymbol { 0 }$ ， $y \in Y$ and $L ( x _ { 0 } ) = 1$ . In particular, $L ( x _ { k } ) = 0$ ， $k =$ 1,2,....But by completeness,this implies $\mathbf { \nabla } L = 0$ and contradicts $L ( x _ { 0 } )$ $= 1$

Ex. 2. Let $\pmb { X }$ be a complete inner product space.Any $\pmb { L } \in \pmb { X } ^ { \ast }$ has the representation $\pmb { L } ( \pmb { x } ) = ( \pmb { x } , \pmb { x _ { 0 } } )$ for some ${ \pmb x } _ { \pmb 0 } \in { \pmb X }$ .Hence,the definition of completeness of $\{ x _ { k } \}$ is that $( x _ { k } , x ) = 0 , k = 1 , 2 , \ldots ,$ implies $\pmb { x } = \pmb { 0 }$ .In this case,the present theorem gives us the equivalence of $\pmb { A }$ and $\pmb { \cal E }$ of Theorem 8.9.1.

Ex. 3.Select $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right|$ .By Weierstrass’ Theorem, the powers $1 , x , x ^ { 2 } , \ldots$ ，are closed.For a given ${ \pmb g } ( { \pmb x } ) \in C$ the linear functional $L ( f ) ~ { \stackrel { \cdot } { = } } ~ \int _ { a } ^ { b } f ( x ) g ( x ) ~ d x \operatorname { i s } \operatorname { i n } X ^ { * } . \operatorname { H e n c e } \int _ { a } ^ { b } x ^ { n } g ( x ) ~ d x ~ = 0 , n ~ = 0 , 1 , 2 , \ldots , n - 1 .$ implies 、

Ex.4. Let $\{ \pmb { r _ { i } } \}$ be the set of all rational numbers lying in $a \leq x \leq b$ Let $\mathbf { \mathcal { S } } _ { i } ( x )$ be the step function defined by

$$
\begin{array} { r l r l } & { S _ { i } ( x ) = 1 } & & { a \le x \le r _ { i } } \\ & { S _ { i } ( x ) = 0 } & & { r _ { i } < x \le b . } \end{array}
$$

Then the system $\{  { \boldsymbol } S _ { i } (  { \boldsymbol } x ) \}$ is closed in $L ^ { 2 } [ a , b ]$ ·


<!-- chunk 0005: pages 281-350 -->
rb Pro0f: Let $f ( x ) \in L ^ { 2 } [ a , b ]$ . Suppose that|f(x)Si(x) dx = 0,i = 1,2.,.... Using the definition of $S _ { i } , \int _ { a } ^ { r _ { i } } f ( x ) d x = 0 , i \stackrel { \bullet u } { = } 1 , 2 , . . .$ , and hence the function $F ( t ) = \int _ { a } ^ { t } f ( x ) d x$ is zero at the rational points.But $F ( t ) \in C [ a , b ]$ and hence $\pmb { F } ( t ) \equiv \mathbf { 0 }$ It follows that $f ( x ) \equiv 0$ almost everywhere.The system $\{ \pmb { S } _ { i } ( \pmb { x } ) \}$ is accordingly complete and hence,closed.

Ex.5.Let $_ D$ be a bounded multiply connected region and let $A ( D )$ be the normed linear space of functions that are analytic in $\pmb { D }$ and continuous in $_ { D }$ plus its boundary. $\left\| f \right\| = \underset { z \in \bar { D } } { \operatorname* { m a x } } \ \left| f \left( z \right) \right|$ . The sequence of functions $1 , z , z ^ { 2 } , \ldots ,$ is not closed in $A ( D )$ .For if the sequence were closed,it would be complete.Now let ${ z _ { 0 } }$ be a point in one of the“holes”of $\pmb { D }$ .Consider the linear functional $L ( f ) =$ ${ \frac { 1 } { 2 \pi i } } \int _ { C } f \left( z \right) d z ,$ where $\boldsymbol { \mathfrak { c } }$ is a contour lying in $_ { D }$ and containing ${ \pmb z } _ { \pmb 0 }$ in its interior. $\pmb { L }$ is bounded over $A ( D )$ and $L ( z ^ { n } ) = 0 , n = 0 , 1 , \ldots .$ Therefore $\mathbf { L } = \mathbf { 0 }$ by completeness,but $\frac { 1 } { z - z _ { 0 } }$ is in $A ( D )$ and $L \left( { \frac { 1 } { z - z _ { 0 } } } \right) = 1$ Hence we have a contradiction.

Though completeness and closure are equivalent,it is convenient to employ both terms so that attention may be called to the appropriate defining property.

The property of closure is transitive.

THEOREM 11.1.8 (Lauricella). Let $\pmb { X }$ be $\pmb { a }$ normed linear space and let $\left\{ x _ { n } \right\}$ be a closed system. Then a second system $\left\{ y _ { n } \right\}$ is closed in $\pmb { X }$ if and only if $\romannumeral 4$ is closed in $\left\{ x _ { n } \right\}$ .By this we mean that each ${ \pmb x } _ { \pmb n }$ can be approximated arbitrarily closely by linear combinations of the $y _ { n }$

Proof:The necessity is trivial. To prove sufficiency, let ${ \pmb x } \in { \pmb X }$ and prescribe $\varepsilon > 0$ Since $\left\{ x _ { k } \right\}$ is closed we may find constants $a _ { 1 } , \ldots , a _ { N }$ such that $\| x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { N } x _ { N } \| \le \varepsilon / 2$ . We may obviously assume that each $\qquad \pmb { a } _ { i } \neq 0$ ,otherwise we simply ignore that coeffcient.Since $\left\{ y _ { k } \right\}$ is closed in $\left\{ x _ { k } \right\}$ ,we may find constants $b _ { i 1 } , b _ { i 2 } , . . . , b _ { i N _ { i } } , i = 1 , 2 , . . . , N$ such that

$$
\| x _ { i } - b _ { i 1 } y _ { 1 } - b _ { i 2 } y _ { 2 } - \cdot \cdot \cdot - b _ { i N _ { i } } y _ { N _ { i } } \| \leq \frac { \varepsilon } { 2 N | a _ { i } | } i = 1 , 2 , \ldots , N .
$$

If we set $w _ { i } = a _ { i } ( b _ { i 1 } y _ { 1 } + b _ { i 2 } y _ { 2 } + \cdot \cdot \cdot + b _ { i N _ { i } } y _ { N _ { i } } ) , i = 1 , 2 , \ldots , N ,$ then, $\| a _ { i } x _ { i } - w _ { i } \| \leq \frac { \varepsilon } { 2 N } , \qquad i = 1 , 2 , \ldots , N .$

Now, by the triangle inequality,

$$
\begin{array} { r l } & { \| x - w _ { 1 } - w _ { 2 } - \cdot \cdot \cdot - w _ { n } \| } \\ & { = \| x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { N } x _ { N } - w _ { 1 } - w _ { 2 } - \cdot \cdot \cdot - w _ { N } + a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { N } } \\ & { \leq \| x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { N } x _ { N } \| + \| a _ { 1 } x _ { 1 } - w _ { 1 } \| + \cdot \cdot \cdot + \| a _ { N } x _ { N } - w _ { N } \| } \\ & { \leq \frac { \varepsilon } { 2 } + N \frac { \varepsilon } { 2 N } = \varepsilon . } \end{array}
$$

In this way,we approximate $_ x$ to within $\pmb \varepsilon$ by $w _ { 1 } + \cdots + w _ { N }$ ，which is a combination of the y's.

# 11.2 Completeness of the Powers and Trigonometric Systems for $L ^ { 2 } [ a , b ]$

THEOREM 11.2.1. The powers $1 , x , x ^ { 2 } , \ldots$ , are complete over $L ^ { 2 } [ a , b ]$

Proof: Let $f ( x ) \in L ^ { 2 } [ a , b ]$ and assume that

$$
\int _ { a } ^ { b } x ^ { n } f ( x ) d x = 0 \qquad n = 0 , 1 , 2 , . . . .
$$

Set

$$
F ( x ) = \int _ { a } ^ { x } f ( t ) d t .
$$

Then $\pmb { F } ( \pmb { x } ) \in C [ \pmb { a } , \pmb { b } ]$ . In particular $F ( a ) = 0 , F ( b ) = 0$ . Integrating by parts,

$$
0 = \int _ { a } ^ { b } x ^ { n } f ( x ) d x = x ^ { n } F ( x ) { \biggl | } _ { a } ^ { b } - n { \int _ { a } ^ { b } x ^ { n - 1 } F ( x ) d x } .
$$

It follows that $\int _ { a } ^ { b } x ^ { n - 1 } F ( x ) d x = 0 n = 1 , 2 , . . . .$

Now by Ex.3, Section 11.1, the powers are complete for $C [ \pmb { a } , \pmb { b } ]$ with $\| f \| =$ $\operatorname* { m a x } _ { \pmb { a } \leq \pmb { x } \leq \pmb { b } } \ | f ( \pmb { x } ) |$ ，and this implies that $\pmb { F } ( \pmb { x } ) = \mathbf { 0 }$ . Therefore $\begin{array} { r } { f ( { \pmb x } ) = 0 } \end{array}$ almost everywhere.

COROLLARY 11.2.2. The sequence of orthonormal polynomials on $[ a , b ]$ ${ p _ { n } } ^ { * } ( x ) = k _ { n } x ^ { n } + \cdots , k _ { n } > 0$ ，has all the properties $\mathbf { A } { - } \mathbf { F }$ of Theorem 8.9.1 for $f \in L ^ { 2 } [ a , b ]$

A corresponding theorem for the trigononometric functions can be derived from the powers by a change of variable, but we prefer the following proof which makes use of an interesting analytic device.

LEMMA 11.2.3. Let $f ( x ) \in C [ - \pi , \pi ]$ and suppose that

$$
\int _ { - \pi } ^ { \pi } f ( x ) \cos { n x } d x = 0 \qquad n = 0 , 1 , . . . ,
$$

and

$$
\int _ { - \pi } ^ { \pi } f ( x ) \sin { n x } d x = 0 \qquad n = 1 , 2 , \ldots .
$$

Then $\pmb { f } ( \pmb { x } ) \equiv \mathbf { 0 }$

Proof: If $\pmb { T } _ { \pmb { n } } ( \pmb { x } )$ is an arbitrary trigonometric polynomial,it follows from (11.2.2)and (ll.2.3) that $\int _ { - \pi } ^ { \pi } f ( x ) \pmb { T } _ { n } ( x ) d x = 0 .$ Assume that $f ( { \pmb x } ) \not \equiv 0$ Then there is a point $\pmb { x _ { 0 } }$ interior to $[ - \pi , \pi ]$ at which $f ( x _ { 0 } ) \neq 0$ .For the sake of argument,assume that $f ( x _ { 0 } ) = m > 0$ .Then by continuity,we can find an interval $I \colon x _ { 0 } - \delta \leq x \leq x _ { 0 } + \delta$ contained in $( - \pi , \pi )$ throughout which $f ( x ) \geq m / 2$ .Construct the trigonometric function

$$
t ( x ) = 1 - \cos { \delta } + \cos { ( x - x _ { 0 } ) } .
$$

For $x _ { 0 } - \delta < x < x _ { 0 } + \delta$ cos $( x - x _ { 0 } ) > \cos \delta$ and therefore $t ( x ) > 1$ .For ${ \pmb x } = { \pmb x _ { 0 } } \pm \delta , t ( { \pmb x } ) = { \mathbb 1 }$ .Elsewhere in $[ - \pi , \pi ] , - 1 \leq \cos { ( x - x _ { 0 } ) } < \cos { \delta }$ so that

$$
- \cos \delta \leq t ( x ) < 1 \quad { \mathrm { a n d ~ t h e r e f o r e } } \quad | t ( x ) | < 1 .
$$

Now consider the trigonometric polynomial of order $\pmb { n }$ ， $T _ { n } ( x ) = [ t ( x ) ] ^ { n }$ It is clear that

$$
\begin{array} { r l } { T _ { n } ( x ) \ > 1 } & { { } \mathrm { f o r } \ I _ { 1 } ; \ x _ { 0 } - \delta < x < x _ { 0 } + \delta } \\ { T _ { n } ( x ) = 1 } & { { } \mathrm { f o r } \ x = x \ \pm \delta } \\ { | T _ { n } ( x ) | < 1 } & { { } \mathrm { f o r } \ I _ { 2 } \colon \mathrm { t h e ~ r e m a i n i n g ~ p o r t i o n s ~ o ~ } } \end{array}
$$

But

$$
0 = \int _ { - \pi } ^ { \pi } f ( x ) T _ { n } ( x ) d x = \int _ { I _ { 1 } } f ( x ) T _ { n } ( x ) d x + \int _ { I _ { 2 } } f ( x ) T _ { n } ( x ) d x ,
$$

so hat $\cdot \int _ { I _ { 1 } } = - \int _ { I _ { 2 } } . \mathrm { \normalfont ~ N o w } \left| \int _ { I _ { 2 } } f ( x ) T _ { n } ( x ) d x \right| \le \int _ { I _ { 2 } } | f ( x ) | d x$ and i hreore bounded as ${ \pmb n }  \infty$ Since $t ( x ) > 1$ on $I _ { 1 }$ $t ( \pmb { x } ) \geq 1 + \varepsilon$ on, say,

$$
I _ { 3 } \colon x _ { 0 } - \frac \delta 2 \leq x \leq x _ { 0 } + \frac \delta 2 .
$$

Therefore, $T _ { n } ( x ) = [ t ( x ) ] ^ { n } \geq ( 1 + \varepsilon ) ^ { n }$ on $I _ { 3 }$ and

$$
\int _ { I _ { 1 } } f ( x ) T _ { n } ( x ) d x \geq { \frac { m } { 2 } } \int _ { I _ { 3 } } T _ { n } ( x ) d x \geq { \frac { m } { 2 } } ( 1 + \varepsilon ) ^ { n } .
$$

This is a contradiction since $\int _ { I _ { 1 } } \to + \infty \ { \mathrm { w h i l e } } \rfloor$ $\int _ { I _ { 1 } }$ is bounded. The assumption that $f ( { \pmb x } ) \not \equiv 0$ cannot be maintained.

THEOREM 11.2.4. The system of functions cos $_ { n x }$ ， $\pmb { n = 0 , 1 , \dots }$ sin $\pmb { n x }$ ， n = 1,2,..., is complete in ${ \cal L } ^ { 2 } [ - \pi , \pi ]$

Proof: Let $f ( x ) \in L ^ { 2 } [ - \pi , \pi ]$ .We shall show that the conditions (11.2.2) and (11.2.3) imply $f ( x ) = 0$ almost everywhere. This will imply completeness for ${ \cal L } ^ { 2 } [ - \pi , \pi ]$ by Ex.2 of Section li.1. The function

$$
F ( x ) = \int _ { - \pi } ^ { x } f ( t ) d t
$$

is in $C [ - \pi , \pi ]$ and ${ \pmb F } ( - \pi ) = 0 , ~ { \pmb F } ( \pi ) = 0$ The last follows from (11.2.2) with $\pmb { n = 0 }$ If $\scriptstyle { \mathcal { T } } ( x )$ designates an arbitrary trigonometric polynomial, $\int _ { - \pi } ^ { \pi } f ( x ) T ( x ) d x = 0 .$ But

$$
\int _ { - \pi } ^ { \pi } f ( x ) T ( x ) d x = F ( x ) T ( x ) \left| _ { - \pi } ^ { \pi } - \int _ { - \pi } ^ { \pi } F ( x ) T ^ { \prime } ( x ) d x . \right.
$$

Hence $\int _ { - \pi } ^ { \pi } F ( x ) T ^ { \prime } ( x ) d x = 0$ for all derivatives $\mathbf { \nabla } ^ { T ^ { \prime } }$ of trigonometric polynomials.

In partieular $\int _ { - \pi } ^ { \pi } F ( x ) { \overset { \sin } { \cos } } n x d x = 0 \quad n = 1 , 2 , \dots . . . { \mathrm { C o n s i d e r ~ n o w } }$

$$
G ( x ) = F ( x ) - c , ~ c = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } F ( x ) ~ d x .
$$

Then it is easily verified that

$$
\int _ { - \pi } ^ { \pi } G ( x ) { \begin{array} { l } { \sin n x } \\ { \cos m x } \end{array} } d x = 0 \quad \begin{array} { l } { n = 1 , 2 , . . . , } \\ { m = 0 , 1 , 2 , . . . . } \end{array}  .
$$

By Lemma 11.2.3, $ { \boldsymbol { G } } (  { \boldsymbol { { x } } } ) \equiv \mathbf { 0 }$ .Therefore $\pmb { F } ( \pmb { x } ) = \pmb { c }$ But $\pmb { F } ( \pmb { \pi } ) = 0$ ，so that $\pmb { F } ( \pmb { x } ) \equiv \mathbf { 0 }$ .Accordingly $f ( x ) = 0$ almost everywhere.

CoROLLARY 11.2.5. The sequence of sines and cosines satisfles all the conditions A-F of Theorem 8.9.l for $f \in L ^ { 2 } [ - \pi , \pi ]$ . In particular, we have theParseval identity

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } [ f ( x ) ] ^ { 2 } d x = \ddagger a _ { 0 } ^ { 2 } + \sum _ { n = 1 } ^ { \infty } ( { a _ { n } } ^ { 2 } + { b _ { n } } ^ { 2 } )
$$

$$
a _ { n } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos n x d x , b _ { n } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \sin n x d x .
$$

11.3 The Müntz Closure Theorem. Suppose that one has been given a sequence of powers $\left\{ x ^ { p _ { k } } \right\}$ . Under what circumstances can continuous functions or functions in $L ^ { 2 }$ be approximated by linear combinations of these powers? Müntz gave an extensive discussion of this problem and used a method that is a beautiful application of Theorem 8.7.4.

LEMMA 11.3.1 (Cauchy). If

$$
\begin{array} { r } { D _ { n } = \left| \begin{array} { c c c c c } { \displaystyle \frac { 1 } { a _ { 1 } + b _ { 1 } } } & { \displaystyle \frac { 1 } { a _ { 1 } + b _ { 2 } } } & { \cdot \cdot \cdot } & { \displaystyle \frac { 1 } { a _ { 1 } + b _ { n } } } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \displaystyle \frac { 1 } { a _ { n } + b _ { 1 } } } & { \displaystyle \frac { 1 } { a _ { n } + b _ { 2 } } } & { \cdot \cdot \cdot } & { \displaystyle \frac { 1 } { a _ { n } + b _ { n } } } \end{array} \right| , } \end{array}
$$

then

$$
D _ { n } = \frac { \displaystyle \prod _ { i > j } ^ { n } ( a _ { i } - a _ { j } ) ( b _ { i } - b _ { j } ) } { \displaystyle \prod _ { i , j = 1 } ^ { n } ( a _ { i } + b _ { j } ) } .
$$

Proof:Regard the $\pmb { a } _ { i }$ sand the $b _ { j }$ sas $2 n$ independent variables and think of $D _ { n }$ as expanded and put over a common denominator.This common denominator is $\prod _ { i , j = 1 } ^ { n } ( a _ { i } + b _ { j } )$ .Each individual term is of degree $- 1$ so that $D _ { n }$ is of degree $- n$ .The common denominator has $\scriptstyle n ^ { 2 }$ factors and hence is of degree $\mathbf { \nabla } n ^ { 2 }$ .It follows that the numerator must be a polynomial of degree $n ^ { 2 } - n$ in the $^ { a }$ 'sand $^ { b }$ 's.

Note that if $a _ { i } = a _ { j }$ ,the ith row and the jth row of $D _ { n }$ will be identical, and $D _ { n } = 0$ .A similar observation holds if $b _ { i } = b _ { j }$ .It follows that the numerator must contain a factor of the form $\prod _ { i > j } ^ { n } ( a _ { i } - a _ { j } ) \prod _ { i > j } ^ { n } ( b _ { i } - b _ { j } ) \quad$ Each product here contains $1 + 2 + \cdots + ( n - 1 ) = { \frac { n ( n - 1 ) } { 2 } }$ factors so that the complete product contains $n ( n - 1 )$ factors.The degree is therefore correct and we must have

$$
D _ { n } = c _ { n } \frac { \underset { i > j } { \overset { n } { \prod } } ( a _ { i } - a _ { j } ) ( b _ { i } - b _ { j } ) } { \underset { i , j = 1 } { \overset { n } { \prod } } ( a _ { i } + b _ { j } ) }
$$

where $c _ { n }$ is a constant independent of the $^ { a }$ 's and b's.We shall show that $c _ { n } = 1$

Note that

$$
a _ { n } D _ { n } = { \left| \begin{array} { l l l } { { \displaystyle { \frac { 1 } { a _ { 1 } + b _ { 1 } } } } } & { { \cdots } } & { { \displaystyle { \frac { 1 } { a _ { 1 } + b _ { n } } } } } \\ { { \cdot } } & { { } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \displaystyle { \frac { a _ { n } } { a _ { n } + b _ { 1 } } } } } & { { \cdots } } & { { \displaystyle { \frac { a _ { n } } { a _ { n } + b _ { n } } } } } \end{array} \right| } .
$$

# Sec. 11.3

Therefore,

$$
\operatorname* { l i m } _ { a _ { n }  \infty } a _ { n } D _ { n } = | \begin{array} { c c c } { { 1 } } & { { \cdots } } & { { { \frac { 1 } { a _ { 1 } + b _ { n } } } } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { { \frac { 1 } { a _ { n - 1 } + b _ { 1 } } } } } & { { \cdots } } & { { { \frac { 1 } { a _ { n - 1 } + b _ { n } } } } } \\ { { } } & { { \cdot } } & { { \cdot } } \end{array} | .
$$

Also

$$
\operatorname* { l i m } _ { b _ { n }  \infty } \operatorname* { l i m } _ { a _ { n }  \infty } a _ { n } D _ { n } = | { \begin{array} { c c c c } { 1 } & { \cdots } & { { \frac { 1 } { a _ { 1 } + b _ { n - 1 } } } } & { 0 } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { 0 } \\ { { \frac { 1 } { a _ { n - 1 } + b _ { 1 } } } } & { \cdots } & { { \frac { 1 } { a _ { n - 1 } + b _ { n - 1 } } } } & { 0 } \\ { 1 } & { \cdot \cdot } & { \cdot } & { 1 } \end{array} } | = D _ { n - 1 } ,
$$

so that

$$
\operatorname* { l i m } _ { b _ { n } \to \infty } \operatorname* { l i m } _ { a _ { n } \to \infty } \frac { a _ { n } D _ { n } } { D _ { n - 1 } } = 1 .
$$

But from (11.3.3),

$$
{ \frac { a _ { n } D _ { n } } { D _ { n - 1 } } } = { \frac { c _ { n } } { c _ { n - 1 } } } { \frac { a _ { n } \prod _ { j = 1 } ^ { n - 1 } ( a _ { n } - a _ { j } ) \prod _ { j = 1 } ^ { n - 1 } ( b _ { n } - b _ { j } ) } { \displaystyle \prod _ { j = 1 } ^ { n } ( a _ { n } + b _ { j } ) \prod _ { j = 1 } ^ { n - 1 } ( b _ { n } + a _ { j } ) } }
$$

it follows that

$$
\operatorname* { l i m } _ { b _ { n } \to \infty } \operatorname* { l i m } _ { a _ { n } \to \infty } \frac { a _ { n } D _ { n } } { D _ { n - 1 } } = 1 = \frac { c _ { n } } { c _ { n - 1 } } .
$$

Therefore, $c _ { n } = c _ { n - 1 }$ . It is easily verified that $c _ { 1 } = 1$ . Hence $c _ { n } = 1$ ·

LEMMA 11.3.2. Let ${ \pmb p } _ { i } \neq { \pmb p } _ { j }$ . Then, assuming $p _ { i } , q > - \frac { 1 } { 2 }$

$$
\begin{array} { l } { \displaystyle \delta ^ { 2 } = \operatorname* { m i n } _ { a _ { k } } \int _ { 0 } ^ { 1 } \lvert x ^ { q } - a _ { 1 } x ^ { p _ { 1 } } - a _ { 2 } x ^ { p _ { 2 } } - \cdot \cdot \cdot - a _ { n } x ^ { p _ { n } } \rvert ^ { 2 } d x } \\ { \displaystyle \qquad = \frac { 1 } { 2 q + 1 } \prod _ { i = 1 } ^ { n } \Big \{ \frac { p _ { i } - q } { p _ { i } + q + 1 } \Big \} ^ { 2 } . } \end{array}
$$

Proof:From Theorem 8.7.4, $\delta ^ { 2 } = \frac { g ( x ^ { q } , x ^ { p _ { 1 } } , x ^ { p _ { 2 } } , . . . , x ^ { p _ { n } } ) } { g ( x ^ { p _ { 1 } } , x ^ { p _ { 2 } } , . . . , x ^ { p _ { n } } ) }$ . Now $( x ^ { \alpha } , x ^ { \beta } ) =$   
$\int _ { 0 } ^ { 1 } x ^ { \alpha } x ^ { \beta } d x = { \frac { 1 } { \alpha + \beta + 1 } }$ . Therefore

$$
 g ( { \pmb x } ^ { p _ { 1 } } , \ldots , \ { \pmb x } ^ { p _ { n } } ) = | \begin{array} { c c } { { \frac { 1 } { p _ { 1 } + p _ { 1 } + 1 } } } & { { \cdots } } & { { \frac { 1 } { p _ { 1 } + p _ { n } + 1 } } } \\ { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } \\ { { \frac { 1 } { p _ { n } + p _ { 1 } + 1 } } } & { { \cdots } } & { { \frac { 1 } { p _ { n } + p _ { n } + 1 } } } \\ { { } } & { { } } & { { \frac { n } { i \pmb { \mathscr { S } } ^ { 2 } } } ( p _ { i } - p _ { j } ) ^ { 2 } \displaystyle \int _ { i , j = 1 } ^ { n } ( p _ { i } + p _ { j } + 1 ) . }  \end{array} 
$$

A similar expression is found for $g ( x ^ { q } , x ^ { p _ { 1 } } , \ldots , x ^ { p _ { n } } )$ .We then have

$$
\begin{array} { l l } { { \frac { \gamma ( x ^ { q } , x ^ { p _ { 1 } } , \ldots , x ^ { p _ { n } } ) } { g ( x ^ { p _ { 1 } } , \ldots , x ^ { p _ { n } } ) } } } & { { } } \\ { { \ } } & { { = \frac { ( q - p _ { 1 } ) ^ { 2 } ( q - p _ { 2 } ) ^ { 2 } \dots ( q - p _ { n } ) ^ { 2 } } { ( q + p _ { 1 } + 1 ) ( q + p _ { 2 } + 1 ) \dots ( q + p _ { n } + 1 ) ( q + q + 1 ) ( p _ { 1 } + 1 + q ) \dots ( p _ { n } + 1 + q ) } } } \\ { { \ } } & { { = \frac { 1 } { 2 q + 1 } \prod _ { i = 1 } ^ { n } \frac { ( q - p _ { i } ) ^ { 2 } } { ( q + p _ { i } + 1 ) ^ { 2 } } . } } \end{array}
$$

THEOREM 11.3.3 (Müntz). Let $\{ x ^ { p } \}$ be $\pmb { a }$ given infinite set of distinct powers with $\pmb { \mathscr { p } } > - \frac { 1 } { 2 }$ .In order that this system be closed in $L ^ { 2 } ( 0 , 1 )$ it is necessary and suffcient that the exponents $\{ p \}$ contains $^ { \pmb { a } }$ sequence $\left\{ p _ { i } \right\}$ such that either

$$
\operatorname * { l i m } _ { i  \infty } p _ { i } = - { \textstyle \frac { 1 } { 2 } } , \quad \sum _ { i = 1 } ^ { \infty } ( p _ { i } + { \textstyle \frac { 1 } { 2 } } ) = \infty ,
$$

or

$$
\operatorname * { l i m } _ { i \to \infty } p _ { i } = p , - \frac { 1 } { 2 } < p < \infty ,
$$

or

$$
\operatorname* { l i m } _ { i \to \infty } p _ { i } = \infty , p _ { i } \neq 0 , \sum _ { i = 1 } ^ { \infty } \frac { 1 } { p _ { i } } = \infty .
$$

Proof:Note that the condition $\textstyle p > - { \frac { 1 } { 2 } }$ insures that $x ^ { p } \in L ^ { 2 } ( 0 , 1 )$ . The powers $1 , x , x ^ { 2 } , \ldots$ ，are closed in $L ^ { 2 } ( 0 , 1 )$ by Theorem 11.2.1.Hence, $\{ x ^ { p } \}$ will be closed in $L ^ { 2 } ( 0 , 1 )$ if and only if each power ${ \pmb x } ^ { \pmb q }$ ， $q = 0 , 1 , \ldots _ { m }$ is approximable.This follows from Theorem l1.1.8. Thus,for each $\pmb q$ ,we must be able to find a sequence $\pmb { p _ { 1 } } , \pmb { p _ { 2 } } , \ldots$ ,such that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { m i n } _ { a _ { i } } \int _ { 0 } ^ { 1 } \lvert x ^ { a } - a _ { 1 } x ^ { p _ { 1 } } - a _ { 2 } x ^ { p _ { 2 } } - \cdot \cdot \cdot - a _ { n } x ^ { p _ { n } } \rvert ^ { 2 } d x = 0 .
$$

Referring to Lemma 11.3.2,for each $\pmb q$ we must be able to find a sequence $\left\{ p _ { \pmb { k } } \right\}$ such that

$$
\operatorname* { l i m } _ { n \to \infty } \prod _ { i = 1 } ^ { n } \Bigl ( \frac { p _ { i } - q } { p _ { i } + q + 1 } \Bigr ) ^ { 2 } = 0 .
$$

Sufficiency. Suppose that $\{ p \}$ has a finite limit point $\pmb { p }$ with $\textstyle p \neq - { \frac { 1 } { 2 } }$ .Now

$$
\operatorname* { l i m } _ { i \to \infty } { \frac { p _ { i } - q } { p _ { i } + q + 1 } } = { \frac { p - q } { p + q + 1 } } .
$$

Since $\textstyle p > - { \frac { 1 } { 2 } }$ and $q \geq 0$ ,it is easily verifed that $- 1 < \frac { p - q } { p + q + 1 } < 1$ $\left. \begin{array} { l } { \mathrm { \Lambda } _ { 1 } } \\ { \mathrm { \Lambda } _ { \mathrm { h o l d s . } } } \end{array} \right. \mathrm { w e } \mathrm { \Lambda } _ { \mathrm { h a v e } } \mathrm { f o r } i \geq n _ { \varepsilon } , \left| \begin{array} { l } { \mathrm { \Lambda } _ { p _ { i } } - q } \\ { p _ { i } + q + 1 } \end{array} \right| < 1 - \varepsilon .$ Hence, (11.3.12) holds.

Suppose we can select a sequence $\left\{ p _ { i } \right\}$ with (11.3.9) holding.Write

$$
\prod _ { i = 1 } ^ { n } \biggl ( \frac { p _ { i } - q } { p _ { i } + q + 1 } \biggr ) ^ { 2 } = \prod _ { i = 1 } ^ { n } \biggl ( 1 - \frac { p _ { i } + \frac { 1 } { 2 } } { q + \frac { 1 } { 2 } } \biggr ) ^ { 2 } \biggl / \prod _ { i = 1 } ^ { n } \biggl ( 1 + \frac { p _ { i } + \frac { 1 } { 2 } } { q + \frac { 1 } { 2 } } \biggr ) ^ { 2 } .
$$

Since im p=-,wehave,ultimately，+ Therefore,

$$
0 < 1 - \frac { p _ { i } + \frac { 1 } { 2 } } { q + \frac { 1 } { 2 } } < 1
$$

and the numerator of the right hand of (l1.3.l4) remains bounded.More  
over，since $\sum _ { i = 1 } ^ { \infty } { \frac { ( p _ { i } + \frac { 1 } { 2 } ) } { q + \frac { 1 } { 2 } } } = \infty$ ，the denominator diverges to $+ \infty \dag$ . Condition   
(11.3.12) is therefore fulfilled.

Finally,suppose we can select a sequence with (ll.3.1l) holding.Write

$$
\displaystyle \prod _ { i = 1 } ^ { n } \biggl ( \frac { p _ { i } - q } { p _ { i } + q + 1 } \biggr ) ^ { 2 } = \displaystyle \prod _ { i = 1 } ^ { n } \biggl ( 1 - \frac { q } { p _ { i } } \biggr ) ^ { 2 } \biggl / \prod _ { i = 1 } ^ { n } \biggl ( 1 + \frac { q + 1 } { p _ { i } } \biggr ) ^ { 2 } .
$$

In view of the hypothesis,the numerator converges to O while the denominator diverges to $+ \infty$ .Hence criterion(11.3.12) is fulfilled.

Necessity. Suppose that the set of exponents $\{ p \}$ contains no sequence $\left\{ p _ { i } \right\}$ fulfilling either (11.3.9,10,or 11).Then $\{ p \}$ must be either

(A) $\mathrm { ~ a ~ s e q u e n c e } \{ p _ { i } \} \mathrm { w i t h \ l i m \ } \operatorname { l i m } _ { i  \infty } p _ { i } = - \frac { 1 } { 2 } , \quad \sum _ { i = 1 } ^ { \infty } ( p _ { i } + \frac { 1 } { 2 } ) < \infty , \mathrm { o r \ }$ (B)a sec ${ \mathfrak { u e n c e } } \left\{ p _ { i } \right\} { \mathrm { w i t h ~ l i m ~ } } p _ { i } = \infty , \quad \sum _ { i = 1 } ^ { \infty } { \frac { 1 } { p _ { i } } } < \infty , { \mathrm { ~ o r ~ } }$ (C)a sequence $\left\{ p _ { i } \right\}$ which can be split into two sub-sequences one of type (A) and one of type (B).

In case (A),refer to (11.3.14). Select a $q \neq p _ { 1 } , p _ { 2 } , . . . .$ ，The numerator converges to zero if and only if one factor vanishes.This is impossible and hence the numerator has a positive limit.Similarly,the denominator converges to a positive limit. This means that (l1.3.l2) does not hold and $x ^ { q }$ cannot be approximated arbitrarily closely by $x ^ { p _ { 1 } } , x ^ { p _ { 2 } } , \ldots .$

In case (B),refer to (11.3.15). If $q \neq p _ { 1 } , p _ { 2 } , . . . .$ ,then the numerator and the denominator of its right hand side converge to a nonzero value.Again, arbitrarily close approximation of

In case (C)，select $\begin{array} { l } { \mathrm { { x m a t i o n ~ o f ~ } } x ^ { q } \mathrm { ~ 1 s ~ 1 m p o s s i b l e . ~ } } \\ { q \neq r _ { 1 } , r _ { 2 } , \dotsc ; \enspace s _ { 1 } , s _ { 2 } , \dotsc \enspace \mathrm { . ~ . ~ . ~ \operatorname { S e t } ~ } \displaystyle \prod _ { i = 1 } ^ { \infty } \biggl ( \frac { r _ { i } - q } { r _ { i } + q + 1 } \biggr ) ^ { 2 } = a , } \end{array}$ $\prod _ { i = 1 } ^ { \infty } \left( { \frac { s _ { i } - q } { s _ { i } + q + 1 } } \right) ^ { 2 } = b$ ,where,as we know from the discussion, $0 < a < \infty$ ； $0 < b < \infty$ Then, $\prod _ { i = 1 } ^ { \infty } \biggl ( \frac { p _ { i } - q } { p _ { i } + q + 1 } \biggr ) ^ { 2 } = a b$ 、Again, (11.3.12) does not hold.

THEOREM 11.3.4 (Müntz). Let $\{ p \}$ be $\pmb { a }$ sequence of distinct nonnegative numbers.In order that $\{ x ^ { p } \}$ be closed in $C [ 0 , 1 ]$ it is suffcient that

or that

$$
f o r w h i c h l i m \atop i \not \to \infty  p _ { i } = \infty \quad \mathrm { a n d } \quad \sum _ { i = 1 } ^ { \infty } \frac { 1 } { p _ { i } } = \infty ,
$$

One of the p's is O and $\{ p \}$ contains a sequence $\left\{ p _ { i } \right\}$ for which $\operatorname* { l i m } _ { i \to \infty } p _ { i } = p , 0 < p < \infty .$

Proof: Let $n > 0$ ， $\mathbf { \nabla } _ { \pmb { p } _ { i } } > 0$ ,then

$$
\begin{array} { r l }   { | \begin{array} { l } { x ^ { n } - \sum _ { i = 1 } ^ { N } a _ { i } x ^ { p _ { i } } | = n | \int _ { 0 } ^ { x } ( t ^ { n - 1 } - \sum _ { i = 1 } ^ { N } \frac { a _ { i } p _ { i } t ^ { p _ { i - 1 } } } { n } ) d t | } } \\ & { \qquad \leq n \displaystyle { \int _ { 0 } ^ { 1 } | t ^ { n - 1 } - \sum _ { i = 1 } ^ { N } \frac { a _ { i } p _ { i } t ^ { p _ { i - 1 } } } { n } | d t } } \end{array} \end{array}
$$

If (11.3.16) holds, $p _ { i } - 1 \to \infty$ ，and ${ \frac { 1 } { 2 } } \sum { \frac { 1 } { p _ { i } } } < \sum _ { p _ { i } - 1 } ^ { \infty } = \infty$ .The set of functions $x ^ { p _ { 1 } - 1 } , x ^ { p _ { 2 } - 1 } , \ldots .$ ,is therefore closed in $L ^ { 2 } [ 0 , 1 ]$ . By the inequality (11.3.18)， for $n - 1 = 0 , 1 , 2 , \ldots , \operatorname* { m a x } _ { 0 \leq x \leq 1 } \left| x ^ { n } - \sum _ { i = 1 } ^ { N } a _ { i } x ^ { p _ { i } } \right|$ can be made arbitrarily small by appropriate selection of $\pmb { a } _ { i }$ The set $x ^ { p _ { 1 } } , x ^ { p _ { 2 } } , \ldots$ ,is therefore closed in $\pmb { x } , \pmb { x } ^ { 2 } ;$ ，....By adjoining l,the augmented set will be closed in 1, $x , x ^ { 2 }$ 。...and hence in $C [ 0 , 1 ]$

Suppose next that (ll.3.17) holds and that $\pmb { \mathscr { p } } > \frac { 1 } { 2 }$ .According to Theorem 11.3.3, $\{ x ^ { p _ { i } - 1 } \}$ will be closed in $L ^ { 2 } [ 0 , 1 ]$ and the remainder of the proof is as above. If,however, $\pmb { \mathscr { p } } \leq \frac { 1 } { 2 }$ ，select a constant $c > 0$ such that $c p _ { i } > \frac { 1 } { 2 }$ ,ultimately.Then, $\{ x ^ { c p _ { i } } \}$ is closed in $C [ 0 , 1 ]$ . Take an $\pmb { f } ( \pmb { x } ) \in C [ 0 , 1 ]$ and let $g ( x ) = f ( x ^ { c } )$ . For appropriate constants $\pmb { a _ { i } }$

Setting ${ \pmb x } ^ { \prime } = { \pmb x } ^ { \pmb { c } }$

$$
\begin{array} { r l } & { \underset { 0 \leq x \leq 1 } { \operatorname* { m a x } } \left| f ( x ^ { c } ) - \underset { i = 1 } { \overset { n } { \sum } } a _ { i } x ^ { c p _ { i } } \right| \leq \varepsilon . } \\ & { \underset { 0 \leq x ^ { \prime } \leq 1 } { \operatorname* { m a x } } \left| f ( x ^ { c } ) - \underset { i = 1 } { \overset { n } { \sum } } a _ { i } x ^ { \prime p _ { i } } \right| \leq \varepsilon . } \end{array}
$$

# 11.4 Closure Theorems for Classes of Analytic Functions

LEMMA 11.4.1． Let $c$ be $\pmb { a }$ rectifable arc (with end points a and b included) of length $\scriptstyle { \cal L }$ .Let f(z) be defined on $c$ ,be continuous,and have $w ( \delta )$ as its modulus of continuity. Let $z _ { 0 } = a , z _ { 1 } , . . . , z _ { n } = b$ be points of $c$ taken in order along C. Suppose that $| z - z _ { i } | \leq \delta$ for $_ z$ in the arc ${ \bf \Phi } _ { i } z _ { i + 1 } , \ i = 0 , 1 , \dots , n - 1$ Then,

$$
\displaystyle \left| \int _ { C } f ( z ) d z - \sum _ { i = 0 } ^ { n - 1 } f ( z _ { i } ) ( z _ { i + 1 } - z _ { i } ) \right| \le w ( \delta ) L .
$$

$$
\begin{array} { r } { \displaystyle \left| \displaystyle \int _ { c } f ( z ) d z - \sum _ { i = 0 } ^ { n - 1 } f ( z _ { i } ) ( z _ { i + 1 } - z _ { i } ) \right| = \displaystyle \left| \sum _ { i = 0 } ^ { n - 1 } \int _ { z _ { i } } ^ { z _ { i + 1 } } ( f ( z ) - f ( z _ { i } ) ) d z \right| } \\ { \displaystyle \qquad \leq \sum _ { i = 0 } ^ { n - 1 } \int _ { z _ { i } } ^ { z _ { i + 1 } } | f ( z ) - f ( z _ { i } ) | d s . } \end{array}
$$

Along $\boldsymbol { c }$ from $z _ { i }$ to $z _ { i + 1 }$ ，we have $| z - z _ { i } | \leq \delta$ so that $| f ( z ) - f ( z _ { i } ) | \leq w ( \delta )$

$$
\sum _ { i = 0 } ^ { n - 1 } \int _ { z _ { i } } ^ { z _ { i + 1 } } \lvert f ( z ) - f ( z _ { i } ) \rvert d s \leq \sum _ { i = 0 } ^ { n - 1 } w ( \delta ) \int _ { z _ { i } } ^ { z _ { i + 1 } } d s = w ( \delta ) { \cal L } .
$$

DEFINITIoN 11.4.1. A Jordan curve in the plane is a homeomorphic image of a circle.That is,it is a point set whose points $( { \pmb x } , y )$ can be represented parametrically ${ \pmb x } = { \pmb f } ( { \pmb \theta } )$ ， $y = g ( \theta )$ where (a) $f$ and $\pmb { g }$ are continuous and periodic functions of period $\mathbf { 2 } \pi$ and $( b ) \ f ( \theta _ { 1 } ) = f ( \theta _ { 2 } ) , \ g ( \theta _ { 1 } ) = g ( \theta _ { 2 } )$ implies that ${ \frac { 1 } { 2 \pi } } \left( \theta _ { 1 } - \theta _ { 2 } \right) = \mathrm { i n t e g e r } .$

In the work that follows,some facts about Jordan curves will be used without proof.

THEOREM 11.4.2 (Runge).Let $c$ be $\pmb { a }$ Jordan curve and let $f ( z )$ be analytic in the interior of and on $c$ Given $\pmb \varepsilon > \mathbf 0$ , we may find $^ { \pmb { a } }$ rational function $\pmb { R } ( z )$ whose poles lie exterior to $\boldsymbol { c }$ and such that

$$
| f ( z ) - R ( z ) | \leq \varepsilon
$$

for z inside and on $c$

Proof:We may find a contour $C ^ { \prime }$ consisting of a fnite number of analytic arcs which contains $c$ in its interior and inside and on which $f ( z )$ is still analytic. For $_ z$ inside and on $C , f ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { C ^ { \prime } } { \frac { f ( t ) } { t - z } } d t$ For arbitrary $t _ { 1 }$ and t2, $t _ { 2 } , \frac { f ( t _ { 1 } ) } { t _ { 1 } - z } - \frac { f ( t _ { 2 } ) } { t _ { 2 } - z } = \frac { f ( t _ { 1 } ) - f ( t _ { 2 } ) } { t _ { 1 } - z } - \frac { f ( t _ { 2 } ) ( t _ { 1 } - t _ { 2 } ) } { ( t _ { 1 } - z ) ( t _ { 2 } - z ) }$ ,so that

$$
\left| \frac { f ( t _ { 1 } ) } { t _ { 1 } - z } - \frac { f ( t _ { 2 } ) } { t _ { 2 } - z } \right| \leq \left[ \frac { | f ( t _ { 1 } ) - f ( t _ { 2 } ) | } { | t _ { 1 } - z | } + \frac { | f ( t _ { 2 } ) | | t _ { 1 } - t _ { 2 } | } { | t _ { 1 } - z | | t _ { 2 } - z | } \right] .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/59885823682e4922b4c9796a4dec774131afbc6c56619580cfd40f411bab7312.jpg)  
Figure 11.4.1.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/6c61d8e0343ce796daed59d7cb193c60209bcc112bf62577f25ab23195629f73.jpg)  
Figure 11.4.2.

Now let $t _ { 1 }$ and $t _ { 2 }$ lie on $C ^ { \prime }$ and $| t _ { 1 } - t _ { 2 } | \leq \delta$ ，Furthermore,set $w ( \delta ) = \mathrm { t h e }$ modulus of continuity of $f$ on $C ^ { \prime }$ ， $M = \operatorname* { m a x } _ { z \in C ^ { \prime } } | f ( z ) |$ ,and $\pmb { \rho } =$ minimum distance from $\boldsymbol { C }$ to $c \prime$ . Then, for $_ z$ in and on $c$ and $\pmb { t }$ on $C ^ { \prime }$ ，

$$
\left| \frac { f ( t _ { 1 } ) } { t _ { 1 } - z } - \frac { f ( t _ { 2 } ) } { t _ { 2 } - z } \right| \le \frac { w ( \delta ) } { \rho } + \frac { M \delta } { \rho ^ { 2 } } .
$$

Therefore for $\pmb { t }$ on $C ^ { \prime } , \frac { f ( t ) } { t - z }$ is uniformly continuous for $_ z$ in and on $c$ : It has a modulus of continuity $\Omega ( \delta )$ independent of $_ z$

Given an $\varepsilon > 0$ Let $\mathbf { \nabla } _ { L ^ { \prime } }$ be the length of $C ^ { \prime }$ . Determine $\pmb { \delta }$ so small that $\Omega ( \delta ) \leq 2 \pi \varepsilon / L ^ { \prime }$ .Determine sufficiently many points $t _ { 0 } , t _ { 1 } , \ldots , t _ { n } = t _ { 0 }$ on $c ^ { \prime }$ so that $| t - t _ { i } | \leq \delta , t \in t _ { i } t _ { i + 1 } , i = 0 , 1 , . . . , n - 1 .$ By Lemma 11.4.1,

$\left| { \frac { 1 } { 2 \pi i } } \int _ { C ^ { \prime } } { \frac { f ( t ) d t } { t - z } } - { \frac { 1 } { 2 \pi i } } \sum _ { i = 0 } ^ { n - 1 } { \frac { f ( t _ { i } ) } { t _ { i } - z } } \left( t _ { i + 1 } - t _ { i } \right) \right| \leq { \frac { \Omega ( \delta ) L ^ { \prime } } { 2 \pi } } \leq \varepsilon .$ The ratoa func $R ( z ) = { \frac { 1 } { 2 \pi i } } \sum _ { i = 0 } ^ { n - 1 } { \frac { f ( t _ { i } ) ( t _ { i + 1 } - t _ { i } ) } { t _ { i } - z } }$ fulfills the requirements ofthetheorem.

THEOREM 1l.4.3 (Runge)．Let $c$ be $\pmb { a }$ Jordan curve and let $\pmb { A } ( C )$ designate the linear space of functions that are analytic inside and on $\boldsymbol { c }$ Then the powers ${ \bf l } , z , z ^ { \bf 2 } ;$ 。...,are closed in $A ( C )$

Proof:We shall show first that if $\pmb { t }$ is a fixed point exterior to $c$ ，the particular function $\frac { 1 } { t - z }$ can be uniformly approximated inside and on $\boldsymbol { c }$ There are two cases to consider.(A） The point $\pmb { t }$ lies so far from $\boldsymbol { c }$ that a line $\ell$ can be drawn separating $\pmb { t }$ and $\boldsymbol { c }$ .(B)No such line can be drawn.In case A,it is clear that we can drawa circle $\pmb { G }$ that contains $\boldsymbol { c }$ in its interior and such that $\ell$ separates $\pmb { t }$ from $\pmb { G }$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/c31304b7ae0d8504886b1422b3846a728ce59e8dcfc0551350adef5a97ae8826.jpg)  
Figure 11.4.3.

Let $z _ { \mathbf { 0 } }$ be the center of $\pmb { G }$ Then we have,

$$
\frac { 1 } { t - z } = \frac { 1 } { t - z _ { 0 } } + \frac { z - z _ { 0 } } { ( t - z _ { 0 } ) ^ { 2 } } + \cdots .
$$

This series converges uniformly in $_ z$ for $\left| { \frac { z - z _ { 0 } } { t - z _ { 0 } } } \right| \leq \rho < 1$ All points $_ z$ in $\pmb { G }$ and hence inside and on $\boldsymbol { c }$ satisfy this inequality. The convergence is therefore uniform inside and on $c$ If $\varepsilon > 0$ is prescribed,we need only take suffciently many terms of (ll.4.3) and arrive at a polynomial $_ z$ which approximates $\frac { 1 } { t - z }$ uniformly inside and on $c$

A simple modification of the expansion (ll.4.3) allows us to conclude as much for the particular functions $\frac { c } { ( t - z ) ^ { n } } , n = 1 , 2 , . . . ,$ and hence for anypolynomial in $\frac { 1 } { t - z }$

In case B,we proceed as follows: Since $c$ is bounded,we can go out far enough and find a point $\smash { t ^ { * } }$ that can be separated from $\boldsymbol { c }$ by a line $\ell .$ Join $\pmb { t }$ and $\pmb { t } ^ { * }$ by a curve $\scriptstyle { \cal L }$ lying exterior to $c$ .Let $\pmb { d }$ be the minimum distance from $\pmb { L }$ to $c$ .Select a sequence of points on $L , t = t _ { 0 } , t _ { 1 } , . . . , t _ { N } = t ^ { * }$ ，such that $| t _ { i + 1 } - t _ { i } | < d , i = 0 , \dots , N - 1$ . Now

$$
{ \frac { 1 } { t - z } } = { \frac { 1 } { t _ { 1 } - z } } - { \frac { t - t _ { 1 } } { ( t _ { 1 } - z ) ^ { 2 } } } + { \frac { ( t - t _ { 1 } ) ^ { 2 } } { ( t _ { 1 } - z ) ^ { 3 } } } - \cdots .
$$

This series converges uniformly and absolutely for $\left| \frac { t - t _ { 1 } } { t _ { 1 } - z } \right| \le r < 1$ ; hence, in the exterior of every circle $\left| z - t _ { 1 } \right| > \frac { 1 } { r } \left| t - t _ { 1 } \right|$ . Since $| t - t _ { 1 } | < d$ the series converges uniformly inside and on $c$ If $\varepsilon > 0$ is prescribed,we can therefore find an integer $\pmb { N _ { 1 } }$ such that

$$
\left| \frac { 1 } { t - z } - P _ { N _ { 1 } } \Big ( \frac { 1 } { t _ { 1 } - z } \Big ) \right| \leq \frac { \varepsilon } { 2 N } , z \ \mathrm { i n s i d e \ a n d \ o n } \ C ,
$$

where $P _ { N _ { 1 } }$ designates an appropriate polynomial of degree ${ { N } _ { 1 } }$ ：

$$
P _ { N _ { 1 } } \Big ( \frac { 1 } { t _ { 1 } - z } \Big ) = \sum _ { k = 0 } ^ { N _ { 1 } } \frac { A _ { k } } { ( t _ { 1 } - z ) ^ { k } } .
$$

By a similar argument,we can approximate $\frac { A _ { k } } { ( t _ { 1 } - z ) ^ { k } }$ by a polynomial in $\frac { 1 } { t _ { 2 } - z }$ uniformly insie ad on $c$ up to an erry f $\frac { \varepsilon } { 2 N ( N _ { 1 } + 1 ) }$ Combining tesendiidaoais such that $P _ { N _ { 2 } } { \left( \frac { 1 } { t _ { 2 } - z } \right) }$

$$
\bigg | P _ { N _ { 1 } } \bigg ( \frac { 1 } { t _ { 1 } - z } \bigg ) - P _ { N _ { 2 } } \bigg ( \frac { 1 } { t _ { 2 } - z } \bigg ) \bigg | \le \frac { \varepsilon } { 2 N } , \qquad z \mathrm { i n s i d e a n d o n } C .
$$

We can therefore set up a chain of approximations,

$$
\bigg | P _ { N _ { k } } \bigg ( \frac { 1 } { t _ { k } - z } \bigg ) - P _ { N _ { k + 1 } } \bigg ( \frac { 1 } { t _ { k + 1 } - z } \bigg ) \bigg | \le \frac { \varepsilon } { 2 N } , \qquad z \mathrm { i n s i d e a n d o n } C ,
$$

Once we have arrived at $t _ { n } = t ^ { * }$ , we use case A to change to an approxima tion in powers of $\textit { \textbf { z } }$ ：

$$
{ \bigg | } P _ { N _ { n } } { \bigg ( } { \frac { 1 } { t _ { n } - z } } { \bigg ) } - P ( z ) { \bigg | } \leq { \frac { \varepsilon } { 2 } } , \qquad z { \mathrm { ~ i n s i d e ~ a n d ~ o n ~ } } C .
$$

The grand combination of these inequalities leads to

$$
\left| { \frac { 1 } { t - z } } - P ( z ) \right| \leq \varepsilon , \qquad z { \mathrm { ~ i n s i d e ~ a n d ~ o n ~ } } C
$$

for an appropriate polynomial $P ( z )$

The theorem is now completed by using Theorem l1.4.2.Let $f ( z )$ be analytic inside and on $c$ .Then we can find points $t _ { 1 } , \ldots , t _ { M }$ exterior to $\boldsymbol { c }$ and constants $a _ { 1 } , \dots , a _ { M }$ such that

$$
\left| f ( z ) - \sum _ { k = 1 } ^ { M } \frac { a _ { k } } { z - t _ { k } } \right| \le \frac { \varepsilon } { 2 } , \qquad z ~ \mathrm { i n s i d e ~ a n d ~ o n } ~ C .
$$

But for each $\pmb { k }$ ，we can find a polynomial $P _ { M _ { k } } ( z )$ ， of appropriate degree $M _ { k }$ ，such that

$$
\left| { \frac { a _ { k } } { z - t _ { k } } } - P _ { M _ { k } } ( z ) \right| \leq { \frac { \varepsilon } { 2 M } } , \qquad z { \mathrm { ~ i n s i d e ~ a n d ~ o n ~ } } C , k = 1 , 2 , \ldots , M .
$$

By combining these inequalities we obtain a polynomial $P ( z )$ for which

$$
| f ( z ) - P ( z ) | \leq \varepsilon , \qquad z { \mathrm { ~ i n s i d e ~ a n d ~ o n ~ } } C .
$$

Theorem l1.4.3 can be extended. It is sufficient to assume only that $f ( z )$ is analytic inside $c$ and continuous inside and on $c$ .The proof of this extension depends upon a continuity theorem for mapping functions.We cannot go into this matter in detail. It must suffice to present the leading ideas.

Let $\pmb { B }$ be a simply connected region whose boundary is a Jordan curve A sequence of bounded simply connected regions $B _ { n }$ will be said to con verge to $\pmb { B }$ from the outside if

(A）Each $B _ { n }$ contains $\bar { B }$ (the closure of $\pmb { B }$ ). （B) $B _ { n }$ contains $\overline { { B _ { n + 1 } } }$ (C)The set $B _ { 1 } \cap B _ { 2 } \cap \cdots$ contains no point exterior to $\pmb { B }$

For each $\pmb { B }$ ，we can find such a convergent sequence. Let $z = 0$ be interior to $\pmb { B }$ Map $B _ { n }$ conformally onto the unit circle $| w | < 1$ by means of $\phi _ { n } ( z )$ $\pmb { B }$ is mapped by $\phi ( z )$ . These mapping functions are fixed by requiring that $\phi _ { n } ( 0 ) = \phi ( 0 ) = 0$ ； ${ \phi _ { n } } ^ { \prime } ( 0 ) > 0$ ， $\phi ( 0 ) > 0$ Map $B _ { n }$ onto $\pmb { B }$ by means of $\boldsymbol { w } =$ $m _ { n } ( z ) ; m _ { n } ( 0 ) = 0$ ， ${ m _ { n } } ^ { \prime } ( 0 ) > 0$

THEOREM 11.4.4. With the above notation,

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { n  \infty } \phi _ { n } ( z ) = \phi ( z ) } \\ { \displaystyle \operatorname* { l i m } _ { n  \infty } m _ { n } ( z ) = z } \end{array}
$$

the limits holding uniformly in $\bar { B }$

For a proof of this theorem,the reader is referred to Walsh [1], p.32.

DEFINITION 11.4.2．Let $c$ be a Jordan curve lying in the $z$ -plane. $W ( C )$ will designate the normed linear space of functions that are analytic in $c$ and continuous inside and on $c$ .The norm is defned by

$$
\| f \| = \operatorname* { m a x } _ { z \in C } | f ( z ) | .
$$

THEOREM 11.4.5 (Walsh). The powers 1, $z , z ^ { 2 }$ ...., are closed in $W ( C )$

Proof: Let $\boldsymbol { c }$ be the boundary of the finite region $\pmb { B }$ .Let $B _ { n }$ be a sequence of simply connected regions that converge to $\pmb { B }$ from the outside. Let $f ( z )$ be analytic in $\pmb { B }$ and continuous in $\bar { B }$ Then $f ( m _ { n } ( z ) )$ will be analytic in ${ \pmb B } .$ Given an $\pmb \varepsilon$ ,we can by Theorem ll.4.4 select an $_ n$ such that

$$
| f ( m _ { n } ( z ) ) - f ( z ) | \leq { \frac { \varepsilon } { 2 } } , \qquad z \in { \bar { B } } .
$$

By Theorem l1.4.3,we can find a polynomial $P ( z )$ such that

$$
| f ( m _ { n } ( z ) ) - P ( z ) | \leq { \frac { \varepsilon } { 2 } } , \qquad z \in { \bar { B } } .
$$

Combining these two inequalities yields the required approximation.

Uniform approximation in the complex plane by polynomials has one feature that distinguishes it sharply from the real case.If a sequence of analytic functions converges uniformly in a region,the limit of the sequence is analytic.Thus,in regions,at least,only analytic functions can be approximated uniformly by polynomials.However,this does not rule out the possibility of more general functions being approximated uniformly on sets that lack interior points.Nor does it rule out the possibility of several distinct analytic functions (noncontinuable one to the other) from being simultaneously approximated over mutually exterior regions.

A half century of work on the problem of uniform approximation in the complex plane by such mathematicians as Runge,Walsh,Lavrentieff, Keldysch,and Mergelyan has led to the following definitive theorems.

DEFINITION 11.4.2. A closed set $\pmb { S }$ in the plane will be said to separate the plane if the complement of $\pmb { S }$ is not connected.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/0d0ebbd5312ea2f8a0cabe3ed15df09ac9a5b287c8d25317f3af6001ccdb9c3e.jpg)  
Figure 11.4.4.

THEOREM 11.4.6．Let $\pmb { S }$ be $^ { \pmb { a } }$ closed bounded set that does not separate the plane. Let $f ( z )$ be continuous on $\pmb { S }$ and be analytic at interior points of $\pmb { S }$ Then $f ( z )$ may be uniformly approximated on $\pmb { S }$ by polynomials.

We formulate a converse as a separate theorem.

THEOREM 11.4.7． Let $\pmb { S }$ be a closed bounded set. If every function $f ( z )$ that is continuous on $\pmb { S }$ and analytic at its interior points can be approximated uniformly on $\boldsymbol { s }$ by polynomials,then $\pmb { S }$ does not separate the plane.

Ex.1.Let $B _ { 1 } , B _ { 2 } , \ldots , B _ { n }$ be $_ n$ mutually exterior bounded regions,with contours $C _ { 1 } , \ldots , C _ { n }$ as boundaries.If $f _ { k }$ is analytic in $B _ { k }$ and continuous in $\overline { { B } } _ { k } , k = 1 , 2 , \ldots , n$ ,then even though the functions $f _ { k }$ may have nothing to do with one another (i.e.,are not analytic continuations of one another) we can find a sequence of polynomials that converges uniformly to $f _ { k }$ in $\textstyle { \overline { { B } } } _ { k }$ simultaneously for $k = 1 , 2 , \ldots , n$ ·

Ex.2 (Walsh).Let $\boldsymbol { c }$ be a Jordan arc. If $f ( z )$ is continuous on $\boldsymbol { \mathfrak { c } }$ then it can be approximated uniformly by polynomials in $_ z$ When $\boldsymbol { \mathfrak { C } }$ is a segment of the real axis then this reduces to Weierstrass'theorem.

We terminate this section with a discussion of the closure of the powers $1 , z , z ^ { 2 } , \ldots$ ,in the Hilbert space $L ^ { 2 } ( B )$ .Here again,the nature of the region $\pmb { B }$ plays a crucial role.

A bounded region $\pmb { B }$ of the complex plane whose boundary $\boldsymbol { c }$ is a Jordan curve has the following property: the complement of $B \cup C$ is a single simply connected region whose boundary is exactly $c$ .The class of regions with this property is more extensive than the regions bounded by Jordan curves.For such regions $\pmb { B }$ ,the powers are closed in $L ^ { 2 } ( B )$

Ex.3. $\boldsymbol { B }$ is the disc $| z | < 1$ with $0 \leq x < 1$ excluded. $B$ does not have this property, for the complement of $B \cup C$ is $| z | > 1$ whose boundary $| z | = 1$ is only a part of $\boldsymbol { \mathfrak { c } }$

THEOREM 11.4.8 (Carleman-Farrell).Let $\pmb { B }$ be a bounded simply connected region with boundary $\boldsymbol { c }$ It is assumed that the complement of $B \cup C$ is $^ { \pmb { a } }$ single region whose boundary is exactly $c$ Then, the set of functions $\{ z ^ { n } \}$ $\pmb { n = 0 }$ ,1,...is closed in $L ^ { 2 } ( B )$

Proof:As in Theorem ll.4.5, the proof depends upon the continuity of mapping functions.

Let $B _ { n }$ be a sequence of regions bounded by Jordan curves which converge to $\pmb { B }$ from the outside.Let $w = m _ { n } ( z )$ map $B _ { n }$ conformally on $\pmb { B }$ ， $m _ { n } ( 0 ) = 0$ ， $m _ { n } ^ { \prime } ( 0 ) > 0$ .We assume that $z = 0$ is interior to $\pmb { B }$ (For the possibility of this type of convergence and for the uniform continuity of the mapping functions,(l1.4.ll),the reader is referred to Walsh [l],p.35.) Let $f ( z ) \in L ^ { 2 } ( B )$ .Consider the composite function

$$
f _ { n } ( z ) = f ( m _ { n } ( z ) ) { m _ { n } } ^ { \prime } ( z ) .
$$

$f _ { n } ( z )$ is analytic throughout the interior of $B _ { n }$ .We shall show first that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { B } \int _ { } | f ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y = 0 .
$$

Let $\pmb { B } ^ { \prime }$ designate any closed Jordan region contained in the interior of $\pmb { B }$ Then,

$$
\int _ { B } \int \int | f - f _ { n } | ^ { 2 } d x d y = \int _ { B ^ { \prime } } \int | f - f _ { n } | ^ { 2 } d x d y + \int \int _ { B - B ^ { \prime } } | f - f _ { n } | ^ { 2 } d x d y .
$$

Now $m _ { n } ( z ) \to z$ ， ${ m _ { n } } ^ { \prime } ( z ) \to 1$ uniformly on $\pmb { B ^ { \prime } }$ .Hence, $f _ { n } ( z ) \to f ( z )$ uniformly on $B ^ { \prime }$ and this implies that $\iint _ { B } | f - f _ { n } | ^ { 2 } d x d y  0$ Now, since $| f - f _ { n } | ^ { 2 } \leq$ $\mathbf { 2 } | f | ^ { 2 } + 2 | f _ { n } | ^ { 2 }$ ，

$$
\int \limits _ { B - B ^ { \prime } } \int \int \limits _ { 0 } ^ { \infty } | f - f _ { n } | ^ { 2 } d x d y \leq 2 \int \int _ { B - B ^ { \prime } } | f | ^ { 2 } d x d y + 2 \int \int _ { B - B ^ { \prime } } | f _ { n } | ^ { 2 } d x d y .
$$

Given an $\varepsilon > 0$ ，since $f \in L ^ { 2 } ( B )$ ，we may select a closed set $G \subset B$ such that $\begin{array} { r l } & { \displaystyle \iint | f | ^ { 2 } d x d y - \displaystyle \iint | f | ^ { 2 } d x d y \le \varepsilon / 6 . \mathrm { ~ I f ~ } B ^ { \prime } \mathrm { ~ i s ~ n o w ~ c h o s e n ~ s o ~ t h a t ~ } G \circ \varepsilon ^ { \prime } , } \\ & { \displaystyle \displaylimits _ { \mathrm { ~ h a v e ~ 2 ~ } } ^ { B } \iint | f | ^ { 2 } d x d y \le \varepsilon / 2 . \mathrm { ~ N o w } , } \\ & { \displaystyle \phantom { \frac { 1 } { 8 } } B - B ^ { \prime } } \end{array}$ $G \subset B ^ { \prime }$ we

$$
\iint _ { B - B ^ { \prime } } | f _ { n } | ^ { 2 } d x d y = \iint _ { B - B ^ { \prime } } | f ( m _ { n } ( z ) ) | ^ { 2 } | m _ { n } ^ { \prime } ( z ) | ^ { 2 } d x d y = \iint | f ( w ) | ^ { 2 } d A _ { w }
$$

where $S _ { n }$ is the image of $B - B ^ { \prime }$ under $w = m _ { n } ( z )$ and where $d A _ { w }$ is the area element in the w variable. Now, by the continuity of the mapping function,for sufficiently large $n , \mathrm { \ d } S _ { n }$ lies in $B - B ^ { \prime }$ and hence,as we have just seen,

$$
2 \iint _ { B ^ { \prime } - B ^ { \prime } } | f _ { n } | ^ { 2 } d x d y \leq \varepsilon / 2 .
$$

Combining these inequalities leads to (11.4.14).

Since $f _ { n } ( z )$ is analytic throughout $B _ { n }$ , it is analytic in $\overline { { B _ { n + 1 } } }$ Hence by Theorem 11.4.3,we can find a polynomial $\pmb { p } ( z )$ such that

$$
| f _ { n } ( z ) - p ( z ) | \leq \varepsilon , \qquad z \in { \overline { { B _ { n + 1 } } } } ,
$$

and therefore

$$
\int _ { B } \int _ { | f _ { n } ( z ) - p ( z ) | ^ { 2 } } d x d y \leq \int _ { B _ { n + 1 } } \int _ { | f _ { n } ( z ) - p ( z ) | ^ { 2 } } d x d y
$$

By combining (11.4.14) and (11.4.19)，we can find a polynomial $\pmb { p } ( z )$ such   
that $\iint _ { B } { \mid } f ( z ) - p ( z ) { \mid } ^ { 2 } d x d y$ is arbitrarily small.The powers are therefore   
closed in $L ^ { 2 } ( B )$

COROLLARY 11.4.9．If $\pmb { B }$ is a region as indicated, then orthonormal polynomials, $k _ { n } z ^ { n } + \cdots$ ， $k _ { n } > 0$ ,in $L ^ { 2 } ( B )$ possess the properties A-F of Theorem 8.9.1.

11.5 Closure Theorems for Normed Linear Spaces. One closed system may be used to generate other closed systems.

THEOREM 11.5.1．Let $\pmb { X }$ be a Banach space (i.e., $^ { a }$ complete normed linear space). Let $\left\{ x _ { k } \right\}$ be $^ { a }$ sequence that is closed in $\pmb { X }$ and such that

$$
\operatorname* { l i m } _ { n \to \infty } \| x _ { n } \| ^ { 1 / n } = \sigma , ~ 0 \leq \sigma < \infty .
$$

Let $\left\{ z _ { n } \right\}$ be a sequence of distinct complex numbers such that

$$
0 < | z _ { n } | \leq \rho < \sigma ^ { - 1 } .
$$

Then the sequence of elements

$$
y _ { n } = \sum _ { k = 1 } ^ { \infty } { z _ { n } } ^ { k } x _ { k } , \quad n = 1 , 2 , \ldots ,
$$

is closed in $\pmb { X }$

Proof: By equation (l1.5.3) we mean,of course, that

$$
\operatorname* { l i m } _ { m \to \infty } \left\| y _ { n } - \sum _ { k = 1 } ^ { m } z _ { n } { } ^ { k } x _ { k } \right\| = 0 , n = 1 , 2 , \ldots .
$$

To show that the series $\sum _ { i = 1 } ^ { \infty } z ^ { k } x _ { k }$ converges to an element $_ y$ (we omit the subscripts),consider the sequence of elements

$$
y ^ { ( p ) } = \sum _ { k = 1 } ^ { p } z ^ { k } x _ { k } .
$$

Now,

$$
\| y ^ { ( p + q ) } - y ^ { ( p ) } \| = \bigg \| \sum _ { k = p + 1 } ^ { q } z ^ { k } x _ { k } \bigg \| \leq \sum _ { k = p + 1 } ^ { q } \| x _ { k } \| | z ^ { k } | .
$$

In view of (11.5.1), the radius of convergence of the power series $\sum _ { \ i = 1 } ^ { \infty } \| { \boldsymbol x } _ { k } \| ~ z ^ { k }$ 1 is ${ \pmb { \sigma } } ^ { - 1 }$ ,so that for $_ z$ in the range $| z | < \rho$ ,this series is convergent.For a given $\varepsilon > 0$ ,we can find $\pmb { N }$ so large that for all $\pmb { \mathscr { p } } \geq N$ and all $q \geq 1$ ，

$$
\sum _ { k = p + 1 } ^ { q } \| x _ { k } \| \ | z ^ { k } | < \varepsilon .
$$

The same holds for $\| y ^ { ( p + q ) } - y ^ { ( p ) } \|$ . The sequence $\left\{ y ^ { \left( p \right) } \right\}$ is therefore a Cauchy sequence. Since $\pmb { X }$ is a complete space, there is a $_ y$ such that

$$
\operatorname* { l i m } _ { p \to \infty } \| y - y ^ { ( p ) } \| = 0 .
$$

Let $\ b { L } \in \ b { X } ^ { * }$ ，then $| L ( y ) - L ( y ^ { \mathsf { ^ { * } } } ) | \leq \| L \| \ \| y - y ^ { ( p ) } \|$ . Hence,

$$
L ( y _ { n } ) = \sum _ { k = 0 } ^ { \infty } L ( x _ { k } ) { z _ { n } } ^ { k } , n = 1 , 2 , . . . . .
$$

Consider now the power series $f ( z ) = \sum _ { k = 0 } ^ { \infty } L ( x _ { k } ) z ^ { k }$ We have

$$
\lvert L ( x _ { k } ) \rvert \leq \| L \| \ \| x _ { k } \| .
$$

Therefore,by (11.5.1), $f ( z )$ is analytic in $| z | < \sigma ^ { - 1 }$ .Suppose that $L ( y _ { n } ) = 0$ ， $\pmb { n } = 1$ ,2,...;then $f ( z _ { n } ) = 0$ .Therefore the zeros of $f ( z )$ have a limit point interior to $| z | < \sigma ^ { - 1 }$ .By the uniqueness theorem for analytic functions, $\textstyle f ( z ) \equiv 0$ .This implies that $L ( \boldsymbol { x } _ { k } ) = 0$ ， $\pmb { n = 1 }$ ,2,.... Since $\{ x _ { k } \}$ is assumed complete,it follows that $\mathbf { \nabla } L = 0$ ，Thus，the only solution of $L ( y _ { k } ) = 0$ ， $k = 1 , 2 , \ldots { }$ is $\mathbf { L } = \mathbf { 0 }$ .By Theorem 11.1.7, $\left\{ y _ { k } \right\}$ is closed in $\pmb { X }$

COROLLARY 11.5.2 (Szasz). Let $F ( z ) = \sum _ { k = 0 } ^ { \infty } c _ { k } z ^ { k }$ ， ${ c } _ { k }$ real, be a fixed power series and let $r > 0$ be itsradiusofcovergence.Assumethat $\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { k _ { n } } } = \infty$ where $k _ { 1 } < k _ { 2 } < \cdots$ is the sequence of all those integers $\geq 1$ for which $c _ { k } \neq 0$ If now $\left\{ t _ { n } \right\}$ is a sequence of distinct real numbers satisfying

$$
0 < | t _ { n } | \leq r _ { 1 } < r ,
$$

then the sequence of functions

$$
\begin{array} { r } { f _ { n } ( x ) = F ( t _ { n } x ) , n = 1 , 2 , . . . , } \end{array}
$$

is complete in $L ^ { 2 } ( 0 , 1 )$ .If $c _ { \mathbf { 0 } } \neq 0$ , it is also complete in $C ( 0 , 1 )$

Pro0f: Set $\pmb { x _ { n } } = c _ { n } \pmb { x } ^ { n }$ .Theorems 11.3.3 and 11.3.4 imply that $\left\{ c _ { n } x ^ { n } \right\}$ is closed in $L ^ { 2 } [ 0 , 1 ]$ and in $C [ 0 , 1 ]$ . Now, $\| c _ { n } x ^ { n } \| _ { C [ 0 , 1 ] } = | c _ { n } |$ and $\| c _ { n } x ^ { n } \| _ { L ^ { 2 } [ 0 , 1 ] } =$ $\frac { | c _ { n } | } { \sqrt { 2 n + 1 } }$ . Hence, lim sup $\| c _ { n } x ^ { n } \| ^ { 1 / n } = \operatorname* { l i m }$ sup $| c _ { n } | ^ { 1 / n } = 1 / r$ The corollary $\pmb { n }  \infty$ $\pmb { n }  \infty$ now follows.

Ex.1． Let $F ( z ) = ( 1 + z ) ^ { s }$ where $\pmb { \mathscr { s } }$ is real and $\neq { \bf 0 }$ ,1,2,.... Under these conditions,none of the Maclaurin coefficients of $\pmb { F } ( z )$ vanishes,and $r = 1$ .Let $\{ t _ { n } \}$ be a sequence of points satisfying ${ \left| t _ { n } \right| } \le 1 - \varepsilon , n = 0 , 1 , \ldots \mathrm { . . . . T h e n } , ( 1$ $( 1 + t _ { n } x ) ^ { s }$ is complete in $L ^ { 2 } [ 0 , 1 ]$ and in $C [ 0 , 1 ]$

A sequence that is “suffciently close” to a complete sequence is itself complete.We present two theorems to this effect.

THEOREM 11.5.3 (Birkhoff).Let $\pmb { H }$ be a Hilbert space and $\{ x _ { n } * \}$ be $^ { \pmb { a } }$ complete orthonormal system. Let $\{ y _ { n } ^ { * } \}$ be $^ { a }$ second orthonormal system. If

$$
\sum _ { n = 1 } ^ { \infty } \| x _ { n } ^ { \ast } - y _ { n } ^ { \ast } \| ^ { 2 } < \infty ,
$$

then $\{ y _ { n } ^ { * } \}$ is also complete.

Proof: (1) If for some $N \geq 0$ ，

$$
\sum _ { N + 1 } ^ { \infty } \| x _ { k } ^ { \ast } - y _ { k } ^ { \ast } \| ^ { 2 } < 1 ,
$$

then the system ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } , \ldots , { x _ { N } } ^ { * } , { y _ { N + 1 } ^ { * } } , { y _ { N + 2 } ^ { * } } , \ldots$ , is complete in $\pmb { H }$ For, suppose there were an element $w \neq 0$ orthogonal to all these.Then

$$
\begin{array} { c } { { \| w \| ^ { 2 } = \displaystyle \sum _ { k = 1 } ^ { \infty } | ( w , x _ { k } ^ { * } ) | ^ { 2 } = \displaystyle \sum _ { k = N + 1 } ^ { \infty } | ( w , x _ { k } ^ { * } ) | ^ { 2 } = \displaystyle \sum _ { k = N + 1 } ^ { \infty } | ( w , x _ { k } ^ { * } - y _ { k } ^ { * } ) | ^ { 2 } } } \\ { { \le \displaystyle \sum _ { k = N + 1 } ^ { \infty } \| w \| ^ { 2 } \| x _ { k } ^ { * } - y _ { k } ^ { * } \| ^ { 2 } = \| w \| ^ { 2 } \displaystyle \sum _ { k = N + 1 } ^ { \infty } \| x _ { k } ^ { * } - y _ { k } ^ { * } \| ^ { 2 } < \| w \| ^ { 2 } } } \end{array}
$$

a contradiction.

(2) Suppose for some $N , \sum _ { N + 1 } ^ { \infty } \| x _ { k } ^ { \ast } - y _ { k } ^ { \ast } \| ^ { 2 } < 1$ Set

$$
z _ { k } = { x _ { k } } ^ { * } - \sum _ { j = N + 1 } ^ { \infty } ( { x _ { k } } ^ { * } , { y _ { j } } ^ { * } ) { y _ { j } } ^ { * } , \quad k = 1 , 2 , \ldots , N .
$$

Then the system, $z _ { 1 } , z _ { 2 } , . . . , z _ { N } , y _ { N + 1 } ^ { * } , y _ { N + 2 } ^ { * } , . . .$ , is complete in $\pmb { H }$ .For let $\pmb { w }$ be orthogonal to these elements. Then

$$
\begin{array} { l } { { 0 = ( w , z _ { k } ) = \displaystyle \left( w , { x _ { k } } ^ { * } - \sum _ { j = N + 1 } ^ { \infty } ( { x _ { k } } ^ { * } , { y _ { j } } ^ { * } ) { y _ { j } } ^ { * } \right) } } \\ { { = ( w , { x _ { k } } ^ { * } ) - \displaystyle \sum _ { j = N + 1 } ^ { \infty } ( { x _ { k } } ^ { * } , { y _ { j } } ^ { * } ) ( w , { y _ { j } } ^ { * } ) = ( w , { x _ { k } } ^ { * } ) . } } \end{array}
$$

Therefore $( w , { x _ { k } } ^ { * } ) = 0 , k = 1 , 2 , . ~ . ~ . ~ , N$ . By part (1), $w = 0$

To prove the theorem,select $\pmb { N }$ so large that $\sum _ { v + 1 } ^ { \infty } \| x _ { k } ^ { \ast } - y _ { k } ^ { \ast } \| ^ { 2 } < 1$ .Let $\pmb { S }$ 1 designate the orthogonal complement of $\{ y _ { N + 1 } ^ { * } , y _ { N + 2 } ^ { * } , . . . \}$ ,i.e., the set of all elements orthogonal to these elements.For $j \ge N + 1$ ,and for $1 \leq k \leq N$ ，

$$
z _ { k } , y _ { j } { } ^ { * } ) = ( x _ { k } { } ^ { * } , y _ { j } { } ^ { * } ) - \sum _ { p = N + 1 } ^ { \infty } ( x _ { k } { } ^ { * } , y _ { p } { } ^ { * } ) ( y _ { p } { } ^ { * } , y _ { j } { } ^ { * } ) = ( x _ { k } { } ^ { * } , y _ { j } { } ^ { * } ) - ( x _ { k } { } ^ { * } , y _ { j } { } ^ { * } ) = 0
$$

Hence $z _ { 1 } , z _ { 2 } , \dots , z _ { N } \in S$ Since $z _ { 1 } , ~ . ~ . ~ , z _ { N } , y _ { N + 1 } ^ { * } , ~ . ~ . ~ .$ ,is complete, $\pmb { S }$ cannot contain elements other than linear combinations of $z _ { 1 } , \dotsc , z _ { N }$ Thus, $\pmb { S }$ is a finite dimensional space of dimension $\le \pmb { N }$ .Note further that the elements ${ y _ { 1 } } ^ { * } , { y _ { 2 } } ^ { * } , \ldots , { y _ { N } } ^ { * }$ are in $\pmb { S }$ .Since they are orthonormal, they are independent and hence span $\pmb { S }$ .The elements $z _ { 1 } , z _ { 2 } , \dotsc , z _ { \scriptscriptstyle { X } }$ are therefore linear combinations of $y _ { 1 } * , \ y _ { 2 } *$ ，...， $y _ { N } { } ^ { * }$ .If, therefore, $( w , \ y _ { k } ^ { \ * } ) = 0$ ， $k = 1$ ,2,...，it follows that $w _ { \perp } z _ { 1 } , z _ { 2 } , . ~ . ~ . ~ , z _ { \mathrm { \scriptscriptstyle S V } } , y _ { N + 1 } ^ { * } , . ~ . ~ .$ ,and hence $w = 0$

THEOREM 11.5.4 (Paley-Wiener-Boas). Let $X$ be $^ { a }$ normed linear space and suppose that $\left\{ x _ { n } \right\}$ is closed in $X$ .1f $\left\{ y _ { n } \right\}$ is $^ { a }$ sequence such that for some number 2, $0 \leq \lambda < 1$ , and for allfnite sequences of constants $a _ { 1 } , a _ { 2 } , \ldots , a _ { n } .$ we have

$$
\left\| \sum _ { k = 1 } ^ { n } a _ { k } ( x _ { k } - y _ { k } ) \right\| \leq \lambda \left\| \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \right\| ,
$$

then $\left\{ y _ { n } \right\}$ is also closed in $X$

Proof: Let $X _ { \mathbf { i } }$ be the subspace of $X$ spanned by $\left\{ x _ { n } \right\}$ That is, $X _ { 1 }$ consists of allfinitelinear combinations $\sum _ { k = 1 } ^ { n } a _ { k } x _ { k }$ Let $L \in X ^ { * }$ with $L ( y _ { k } ) = 0 , k =$ 1,2,....We shall estimate the norm of $\boldsymbol { L }$ on $X _ { 1 }$

$$
\begin{array} { r l r } {  { \bigg | L \bigg ( \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \bigg ) \bigg | = \bigg | L \bigg ( \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } ( x _ { k } - y _ { k } ) \bigg | \leq \| L \| \bigg \| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } ( x _ { k } - y _ { k } ) \bigg \| } } \\ & { } & { \leq \lambda \| L \| \bigg \| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \bigg \| . } \end{array}
$$

Hence,over $X _ { 1 }$ ,the norm of $\pmb { L }$ does not exceed $\lambda \lVert L \rVert$

By Theorem l1.1.5,we may extend $\pmb { L }$ to the whole of $X$ without increasing the norm.Call the extension $\pmb { F }$ ：

$$
\begin{array} { l } { { { \pmb F } ( { \boldsymbol x } _ { k } ) = L ( { \boldsymbol x } _ { k } ) , ~ k = 1 , 2 , . ~ . ~ . ~ , } } \\ { { \| { \boldsymbol F } \| = \| L \| _ { { \boldsymbol X } _ { 1 } } . } } \end{array}
$$

Now, since $\left\{ x _ { k } \right\}$ is complete, ${ \pmb F } ( { \pmb x } _ { k } ) - { \pmb L } ( { \pmb x } _ { k } ) = { \pmb 0 } _ { : }$ $k = 1$ ,2,...,implies that ${ \pmb { F } } = { \pmb { L } }$ Therefore $\| L \| = \| F \| = \| L \| _ { X _ { 1 } } \leq \lambda \| L \|$ .Since $0 < \lambda < 1$ ，this implies that $L = 0$ .Therefore $\left\{ y _ { n } \right\}$ is complete and closed in $\pmb { X }$

COROLLARY 11.5.5. Let $H$ be a Hilbert space and let $\{ { x _ { k } } ^ { * } \}$ be a complete orthonormal sequence. Let $\left\{ y _ { k } \right\}$ be any sequence such that

$$
\left\| \sum _ { k = 1 } ^ { n } a _ { k } ( { x _ { k } } ^ { * } - y _ { k } ) \right\| ^ { 2 } \leq \lambda \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } . 0 \leq \lambda < 1
$$

for every sequence $\left\{ a _ { k } \right\}$ of complex members. Then $\left\{ y _ { k } \right\}$ is also complete. In particular,(11.5.12) holds if

$$
\sum _ { k = 1 } ^ { \infty } \| x _ { k } ^ { \ast } - y _ { k } \| ^ { 2 } = \lambda < 1 .
$$

$P r o o f \colon \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } = \left\| \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } ^ { * } \right\| ^ { 2 }$

under the assumption (11.5.13),

$$
\begin{array} { r } { \biggr \| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } ( { x _ { k } } ^ { * } - y _ { k } ) \biggr \| \le \displaystyle \sum _ { k = 1 } ^ { n } | a _ { k } | \| { x _ { k } } ^ { * } - y _ { k } \| \le \biggl ( \displaystyle \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } \biggl ( \displaystyle \sum _ { k = 1 } ^ { n } \| { x _ { k } } ^ { * } - y _ { k } \| ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } } \\ { \le \lambda ^ { \frac { 1 } { 2 } } \biggl ( \displaystyle \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } } \end{array}
$$

so that (11.5.12) holds with $\lambda ^ { \ddag }$ replacing $\lambda$

CoROLLARY 11.5.6 (Schafke). If (11.5.10) holds with $0 < \lambda < \frac { 1 } { 2 }$ then $\left\{ y _ { n } \right\}$ is closed if and only if $\left\{ x _ { n } \right\}$ is closed.

Proof: We need only show that $\left\{ y _ { n } \right\}$ closed implies $\left\{ x _ { n } \right\}$ closed. From (11.3 (11.5.10), we have $\begin{array} { r } { 1 0 ) \quad \mathrm { a n d ~ \ t h e ~ \ t r i a n g l e ~ \ i n e q u a l i t y , } \ \displaystyle \left\| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \right\| - \left\| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } y _ { k } \right\| \leq \lambda \left\| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \right\| . } \\ { \small \mathrm { e } , \ \left\| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } \right\| \leq \frac { 1 } { 1 - \lambda } \Big \| \displaystyle \sum _ { k = 1 } ^ { n } a _ { k } y _ { k } \Big \| . \operatorname { C o m b i n i n g ~ \ t h i s ~ \ o n c e ~ \alpha ~ a g a i n ~ \alpha ~ w i t h } } \end{array}$

$$
\left\| \sum _ { k = 1 } ^ { n } a _ { k } ( x _ { k } - y _ { k } ) \right\| \leq { \frac { \lambda } { 1 - \lambda } } \left\| \sum _ { k = 1 } ^ { n } a _ { k } y _ { k } \ \right\| .
$$

Now if0<λ<} then 0< $0 < \displaystyle \frac { \lambda } { 1 - \lambda } < 1$ ,and (l1.5.14) implies by Theorem 11.5.4 that $\left\{ x _ { n } \right\}$ is closed.

Ex.2 (Duffin-Eachus).Let $L ^ { 2 } [ - \pi , \pi ]$ designate the space of complex valued functions of a real variable which are measurable on $\left[ { - \pi , \pi } \right]$ and for which $( f , f ) = \int _ { - \pi } ^ { \pi } f ( x ) { \overline { { f ( x ) } } } \ d x < \infty$ .Let $\{ \lambda _ { n } \} , n = 0 , \pm 1 , \pm 2 , . . .$ ，be a sequence of complex numbers such that

$$
\left| \lambda _ { n } - n \right| \le \sigma < \frac { \log 2 } { \pi } = . 2 2 \cdot \cdot \cdot , n = 0 , \pm 1 , \pm 2 , . . . .
$$

Then the sequence of “nonharmonic”oscilltions $\{ e ^ { i \lambda _ { n } x } \} _ { \lambda }$ s complete in $L ^ { 2 } [ - \pi , \pi ]$

Proof:For simplicity of notation,think of the integers $n = 0 , \pm 1 , \pm 2 , . . . \nonumber$ as indexed $\pmb { I _ { 1 } } , \pmb { I _ { 2 } } , \dots .$ , and designate $\lambda _ { I _ { n } }$ by $\lambda _ { n } . ~ | \lambda _ { n } - I _ { n } | \leq \sigma , n = 1 , 2 , . ~ . ~ . ~ . ~ \mathbf { A }$ s one can verify using Theorem 1.2.4, $\left\{ \frac { e ^ { i I _ { n } x } } { \sqrt { 2 \pi } } \right\}$ isa complete orthonormal set for $L ^ { 2 } [ - \pmb { \pi } , \pmb { \pi } ]$ .Furthermore,if $f \in L ^ { 2 } [ - \pi , \pi ]$ ，then

$$
\left\| x ^ { j } f \left( x \right) \right\| = \left( \int _ { - \pi } ^ { \pi } | x ^ { j } f \left( x \right) | ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } } \leq \pi ^ { j } \left\| f \right\| .
$$

In Corollary 11.5.5,set

$$
{ x _ { k } } ^ { \ast } = \frac { 1 } { \sqrt { 2 \pi } } \ : e ^ { i { { I _ { k } } x } } , { y _ { k } } = \frac { { e ^ { i { \lambda _ { k } } x } } } { \sqrt { 2 } \pi } \ : .
$$

Then

$$
y _ { k } - { x _ { k } } ^ { * } = \frac { 1 } { \sqrt { \frac { 2 \pi } { 2 \pi } } } e ^ { i I _ { k } x } ( e ^ { i ( \lambda _ { k } - I _ { k } ) x } - 1 ) .
$$

For arbitrary constants $a _ { \mathbf { 1 } } , \ldots , a _ { n }$

$$
\left\| \sum _ { k = 1 } ^ { n } a _ { k } ( y _ { k } - x _ { k } { } ^ { * } ) \right\| = \left\| \sum _ { k = 1 } ^ { n } a _ { k } { \frac { e ^ { i I _ { k } x } } { \sqrt { 2 } \pi j = 1 } } { \frac { \omega ^ { j } ( \lambda _ { k } - I _ { k } x ^ { j } ) } { j ! } } \right\|
$$

$$
= \left\| \sum _ { j = 1 } ^ { \infty } { \frac { 1 } { j ! } } x ^ { j } \sum _ { k = 1 } ^ { n } a _ { k } i ^ { j } ( \lambda _ { k } - I _ { k } ) ^ { j } { \frac { e ^ { i I _ { k } x } } { \sqrt { 2 \pi } } } \right\| \leq \sum _ { j = 1 } ^ { \infty } { \frac { 1 } { j ! } } \left\| x ^ { j } \sum _ { k = 1 } ^ { n } a _ { k } i ^ { j } ( \lambda _ { k } - I _ { k } ) ^ { j } { \frac { e ^ { i I _ { k } x } } { \sqrt { 2 \pi } } } \right\|
$$

$$
\leq \sum _ { j = 1 } ^ { \infty } \frac { \pi ^ { j } } { j ! } \Bigg \| \sum _ { k = 1 } ^ { n } a _ { k } i ^ { j } ( \lambda _ { k } - I _ { k } ) ^ { j } \frac { e ^ { i I _ { k } x } } { \sqrt { 2 \pi } } \Bigg \| = \sum _ { j = 1 } ^ { \infty } \frac { \pi ^ { j } } { j ! } \bigg ( \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } | \lambda _ { k } - I _ { k } | ^ { 2 j } \bigg ) ^ { \frac { 1 } { 2 } }
$$

$$
\leq \sum _ { j = 1 } ^ { \infty } \frac { \sigma ^ { j } \pi ^ { j } } { j ! } \biggl ( \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } = ( e ^ { \sigma \pi } - 1 ) \biggl ( \sum _ { k = 1 } ^ { n } | a _ { k } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } .
$$

Since $\sigma < \frac { \log 2 } { \pi } , e ^ { \sigma \pi } - 1 < 1$ ,and condition (11.5.12) is fulfilled.

Ex. 3.Let $\{ { h _ { n } } ^ { * } ( z ) \}$ be complete and orthonormal for $L ^ { 2 } ( B )$ .If $f _ { n } ( z ) \in L ^ { 2 } ( B )$ and if $\begin{array} { l } { { \displaystyle \sum _ { n = 1 } ^ { \infty } \iint \vert h _ { n } { ^ * } ( z ) - f _ { n } ( z ) \vert ^ { 2 } d x d y < 1 , \mathrm { t h e n } \ \{ f _ { n } \} \ \mathrm { i s \ c o m p l e t e \ i n } \ L ^ { 2 } ( B ) . } } \\ { { \displaystyle , \mathrm { ~ i f ~ } \ { ^ B _ { \mathrm { ~ i s \ t h e \ u n i t \ c i r c l e } , } \sum _ { n = 1 } ^ { \infty } \iint \Bigg \vert } \left. \frac { V \overline { { n + 1 } } } { \pi } z ^ { n } - f _ { n } ( z ) \right. ^ { 2 } d x d y < 1 } } \\ { { \displaystyle \sum _ { n } \mathrm { i s \ c o m p l e t e } } . } \end{array}$ In par-ticular implies that $\{ f _ { n } \}$

# NOTES ON CHAPTER XI

1l.1 Davis and Fan [l] has a generalization of Theorem l1.1.7.

11.2-11.3 Kaczmarz and Steinhaus [1], Natanson [1]

11.4 Walsh [2],Chapter I.Behnke and Sommer [1],pp.244-249.For a proof of Theorems 11.4.6,11.4.7 see Walsh [2],pp.367-371.

11.5 For Theorem 1l.5.l Kaczmarz and Steinhaus [l],p. l45,Davis and Fan [1]. Theorem 11.5.3 is due to G.D.Birkhoff. The present formulation and proof is due to G.Birkhoff and G.-C.Rota [l].For Theorem 11.5.4, R.P.Boas [1],Davis and Fan [1]. For additional references to this type of result see Buck [3], pp.349-350.

# PROBLEMS

1. If $\{ x _ { n } \}$ is complete in $x$ and if $x _ { 1 } = a _ { 1 1 } y _ { 1 }$

$$
x _ { 2 } = a _ { 2 1 } y _ { 1 } + a _ { 2 2 } y _ { 2 }
$$

then $\{ y _ { n } \}$ is complete in $x$

2. In $\ell ^ { 2 }$ ， $x _ { 1 } = ( a _ { 1 1 } , 0 , 0 , 0 , \ldots )$

$$
\begin{array} { r l } & { x _ { 2 } = ( a _ { 2 1 } , a _ { 2 2 } , 0 , 0 , 0 , \dots ) } \\ & { x _ { 3 } = ( a _ { 3 1 } , a _ { 3 2 } , a _ { 3 3 } , 0 , 0 , 0 , \dots ) } \\ & { ~ \cdot } \\ & { ~ . } \end{array}
$$

If $a _ { i i } > 0$ ， prove that $\{ x _ { i } \}$ is closed.

3. If a sequence $\{ x _ { n } \}$ is complete for a space $x$ ， it is complete for every subspace.

4. Let ${ \pmb w } ( { \pmb x } ) \in C [ { \bf 0 } , { \bf 1 } ]$ and $\frac { 1 } { w ( x ) } \geq \varepsilon > 0$ there.The set $\{ w ( x ) f _ { n } ( x ) \}$ is closed in $L ^ { 2 } [ 0 , 1 ]$ if and only if $\{ f _ { n } ( x ) \}$ is.

5.Discuss the second Riemann derivative (Prob.15,Ch.1) as an extension (in the sense of linear functionals) of the ordinary second derivative.

6. If $p ( x )$ is a convex functional defined on a linear space $x$ ,the set of elements $_ { \pmb { x } }$ defined by $p ( { \boldsymbol { x } } ) \leq c$ is convex.

7. If $\boldsymbol { \mathfrak { c } }$ is a convex set in a linear space $x$ ，a boundary point of $c$ may be defined as a point $_ x$ for which we can find two line segments $x _ { 1 } x$ and ${ \boldsymbol { x } } { \boldsymbol { x } } _ { \mathbf { 2 } }$ such that all the interior points of $x _ { 1 } x$ are in $\ b { c }$ while none of the interior points of ${ \pmb x } { \pmb x } _ { \mathbf { 2 } }$ are in $c$ .Prove that the boundary of $p ( x ) \leq c$ is given by $p ( { \boldsymbol { x } } ) = c$

8. Let $x$ be a normed linear space and $\mathbf { \Delta } _ { \mathbf { Y } }$ a linear subspace.Let $x _ { \mathbf { 0 } } \in X$ but $\notin Y$ . A necessary and sufficient condition that inf vEY $\| y - x _ { 0 } \| \leq d$ is that if Le X\*and L(x)=1,L(y)=0,y∈ Y,then |l ≥a.

9. Give a second proof of this theorem in a Hilbert space.

10.The interval $[ a , b ]$ is divided into $\pmb { n }$ equal parts at $a = x _ { 0 } < x _ { 1 } < \cdots$ $< x _ { n } = b$ . A function $f ( x )$ is in $C [ \boldsymbol { a } , \boldsymbol { b } ]$ ,is linear between the $x _ { i }$ and $x _ { i + 1 }$ ，and $f ( x _ { i } ) = y _ { i } =$ rational. The set of all such $f ^ { \prime } { \bf s } , n = 1 , 2 , \ldots$ ,is denumerable and closed in $C [ \boldsymbol { a } , \boldsymbol { b } ]$

11. Let $T _ { r } ( x ) = \frac { x } { r } , 0 \leq x \leq r ; T _ { r } ( x ) = 1 , r \leq x \leq 1 .$ If $\boldsymbol { r } _ { \pmb { n } }$ is the sequence of rationals lying in $0 < x \le 1$ ,is $\{ T _ { r _ { n } } ( x ) \}$ closed in $L ^ { 2 } [ 0 , 1 ] !$

12. Two solutions in $L ^ { 2 } [ 0 , 1 ]$ to the moment problem

$$
\int _ { 0 } ^ { 1 } f ( x ) x ^ { n } = m _ { n } \quad n = 0 , 1 , \ldots ,
$$

must be equal almost everywhere.

13. $\pmb { S }$ consists of a finite or infinite set of disjoint closed intervals in [0,1]. Prove that $\pmb { S }$ is uniquely determined by its moments

$$
m _ { n } = \int _ { S } x ^ { n } d x , \quad n = 0 , 1 , 2 , . . . .
$$

14.Remove one term from the trigonometric set of Theorem 11.2.4. The resulting set is not complete in $L ^ { 2 } [ - \pi , \pi ]$

15.Let $0 < a < \pi$ Set $f ( x ) = - 1$ for $- \pi - a < x < - \pi + a , f ( x ) = 0$ for $- \pi + a < x < \pi - a , f ( x ) = 1$ for $\pi \mathrm { ~ - ~ } a \mathrm { ~ } < x < \pi \mathrm { ~ + ~ } a$ 、Showthat

$$
\int _ { - \pi - a } ^ { \pi + a } f ( x ) \sum _ { \mathbf { c o s } n x } ^ { \sin n x } d x = 0 .
$$

Hence,show that 1,sin $_ x$ cos $_ { x }$ ,...,is not complete in $L ^ { 2 } [ c , d ]$ with $c < - \pi ,$ $d > \pi$

16.Consider the space of complex valued functions of a real variable $_ { x }$ that are measurable on $\left[ { - \pi , \pi } \right]$ and for which $\int _ { - \pi } ^ { \pi } \vert f ( x ) \vert ^ { 2 } d x < \infty$ .Prove that the set of functions $\{ e ^ { i n x } \} n = 0 , \pm 1 , \pm 2 , . . . ,$ ,is complete in this space.

17. Let $H _ { n }$ be the $\textbf { \textit { n } } \times \textbf { \textit { n } }$ matrix whose $\textit { i }$ ,jth element is +j-1.(The Hilbert matrix.)Show that det Hn = 1123!..(2n-1)! Obtain an asymptotic expression for det $H _ { n }$ as $n \to \infty$ and compare with the exact value when $\textbf { \em n } = \textbf { 4 }$

18.Let $a _ { i } , b _ { i }$ be distinct and set

$$
\begin{array} { l } { \displaystyle { A ( x ) = ( x - a _ { 1 } ) ( x - a _ { 2 } ) \cdot \cdot \cdot ( x - a _ { n } ) , } } \\ { \displaystyle { B ( x ) = ( x - b _ { 1 } ) ( x - b _ { 2 } ) \cdot \cdot \cdot ( x - b _ { n } ) , } } \\ { \displaystyle { A _ { i } ( x ) = \frac { A ( x ) } { A ^ { \prime } ( a _ { i } ) ( x - a _ { i } ) } , } } \\ { \displaystyle { B _ { i } ( x ) = \frac { B ( x ) } { B ^ { \prime } ( b _ { i } ) ( x - b _ { i } ) } . } } \end{array}
$$

If $c$ designates the matrix $\left( { \frac { 1 } { a _ { i } - b _ { j } } } \right)$ ，then ${ \cal { C } } ^ { - 1 } = ( c _ { i j } )$ where

$$
c _ { i j } = ( a _ { j } - b _ { i } ) A _ { j } ( b _ { i } ) B _ { i } ( a _ { j } ) .
$$

19.If Hn-1 = Sij, then δ = $s _ { i j } = \frac { ( - 1 ) ^ { i + j } } { i + j - 1 } \frac { ( n + i - 1 ) ! ( n + j - 1 ) ! } { [ ( i - 1 ) ! ( j - 1 ) ! ] ^ { 2 } ( n - i ) ! ( n - j ) ! } \ : .$ $x , x ^ { \frac { 1 } { 2 } } , x ^ { \frac { 1 } { 3 } } ,$ j−16-n $C [ 0 , 1 ] \colon$ $x ^ { 1 0 ^ { 1 0 } }$ $x ^ { 1 0 ^ { 1 0 } + 1 }$ $x ^ { 1 0 ^ { 1 0 } + 2 }$ $L ^ { 2 } [ 0 , 1 ]$

22.Let ${ \pmb p _ { \pmb n } }$ be the nth prime number. Then $x ^ { p _ { 1 } } , x ^ { p _ { 2 } } , \ldots ,$ is closed in $L ^ { 2 } [ 0 , 1 ]$

23.Does the Müntz theorem hold as stated for an arbitrary interval $[ a , b ] !$

24. Formulate a theorem as to when $\int _ { 0 } ^ { 1 } f ( x ) x ^ { \lambda _ { n } } d x = 0 , n = 0 , 1 , . . .$ , implies

25. If $f \in L ^ { 2 } [ 0 , 1 ]$ and $\begin{array} { c c c } { { \displaystyle { m _ { n } = \int _ { 0 } ^ { 1 } f ( x ) x ^ { n } d x } } } \\ { { \mathrm { h o l d . } } } \end{array}$ ,then $\{ m _ { n } \} \in \ell ^ { 2 }$ . However, the converse doesn't necessarily hold.·

26.The sequence ${ \frac { 1 } { x + 1 } } , { \frac { 1 } { x + 2 } } , { \frac { 1 } { x + 3 } } , \dots .$ ,is complete in $L ^ { 2 } [ 0 , 1 ]$

27. If $0 \leq a < b$ ,the sequence $1 , \log { ( x + 1 ) } , \log { ( x + 2 ) } , . . . ,$ is complete in $L ^ { 2 } [ a , b ]$

28.The sequence $f _ { n } ( z ) = n z ^ { n } \quad n = 1 , 2 , . . .$ ，converges to O uniformly on every closed subset of $| z | < 1$ ,but $\operatorname* { l i m } _ { n \to \infty } \int _ { | z | < 1 } | f _ { n } ( z ) | ^ { 2 } \neq 0 .$

29.Let $A ( C )$ be the space of functions that are analytic in ${ \cal { C } } \colon \left| z \right| < 1$ and continuous in $| z | \leq 1$ with $\| f \| = \operatorname* { m a x } _ { | z | < 1 } \ \left| f ( z ) \right|$ .If one of the powers is omitted from the sequence $\{ z ^ { n } \} , n = 0 , 1 , \ldots$ ，the resulting sequence is not closed in the space.

30.Let $\boldsymbol { \mathfrak { c } }$ designate a circle.The origin is assumed to be exterior to $\ b { C }$ .If $\boldsymbol { w } ( z )$ is in $A ( C )$ and does not vanish in the closed circle,then the sequence ${ \pmb w } ( z )$ ， $z w ( z ) , z ^ { 2 } w ( z ) , \ldots ,$ is closed in $\pmb { A } ( \pmb { C } )$ .In particular,the sequence $z ^ { n }$ ， $z ^ { n + 1 }$ ...is closed in $A ( C )$ for any $\pmb { n }$ .Generalize.

31. If $B$ is bounded and multiply connected, then $1 , z , z ^ { 2 } , \ldots$ ,are not closed in $L ^ { 2 } ( B )$

32.If $f ( z )$ is continuous on $| z | = 1$ ， it can be approximated uniformly by linear combinations of $1 , z , z ^ { 2 } , \ldots , \bar { z } , \bar { z } ^ { 2 } , \ldots .$

33. Let $\boldsymbol { \sigma }$ be a smooth arc and let $f ( z )$ be continuous on $\boldsymbol { \sigma }$ Show that

$$
\int _ { C } f ( z ) { \bar { z } } ^ { n } d s = 0 , n = 0 , 1 , . . . ,
$$

implies $\boldsymbol { f } \left( \boldsymbol { z } \right) \equiv \boldsymbol { 0 }$ .Generalize.What if $\ b { C }$ is a closed curve?

34. Let $\{ x _ { k } * \}$ be a complete orthonormal system for a Hilbert space $\pmb { H }$ Show that ${ x _ { 1 } } ^ { * } - { x _ { 2 } } ^ { * } , { x _ { 2 } } ^ { * } - { x _ { 3 } } ^ { * } , { x _ { 3 } } ^ { * } - { x _ { 4 } } ^ { * } , \mathrm { ~ . ~ . ~ , }$ is also complete.The conclusion may be false if $\{ x _ { k } \ast \}$ is merely complete.

35.In a Hilbert space,let $\{ x _ { n } * \}$ be complete and orthonormal. Let $\{ y _ { n } \}$ be an arbitrary sequence for which $( x _ { n } * , y _ { n } ) \neq 0 \quad n = 1 , 2 , \cdot \cdot \cdot \cdot \mathbf { I f }$

$$
\sum _ { n = 1 } ^ { \infty } \left( 1 \ - \left| { \frac { ( x _ { n } * , y _ { n } ) } { ( y _ { n } , y _ { n } ) } } \right| ^ { 2 } \right) \ < 1 ,
$$

then $\{ y _ { n } \}$ is complete.
