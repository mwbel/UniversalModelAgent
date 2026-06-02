# Box 10.3 COVARIANT DERIVATIVE VIEWED AS A MACHINE: CONNECTION COEFFICIENTS AS ITS COMPONENTS

# A.The Machine View

1. The covariant derivative operator $\blacktriangledown$ ,like most other geometric objects,can be regarded as a machine with slots. There is one such machine at each event ${ \boldsymbol { \mathscr { s p } } } _ { 0 }$ in spacetime. In brief, the machine interpretation of $\blacktriangledown$ at ${ \mathcal { P } } _ { 0 }$ says

(g.、v(）,u)=<σ.v>.   
First slot: insert Second slot; insert Third slot:insert A new vector:   
a l-form $\pmb { \sigma }$ that a vector field ${ \pmb v } ( \emptyset ^ { \mathnormal { \mathnormal } } )$ a vector $\pmb { u }$ that “the covariant de  
resides in the tan- defined on a neigh- resides in the rivative of the vec  
gent space at ${ \mathfrak { P } } _ { 0 }$ borhood of $\scriptstyle { \mathcal { P } } _ { 0 }$ tangent space at $\mathcal { P } _ { 9 }$ tor field $\pmb { \nu }$ with J ,respect to u." 1

[Note: this slot notation for $\blacktriangledown$ serves no useful purpose except to emphasize the "machine"-nature of $\blacktriangledown$ . This box is the only place it will be used.]

2.Geometrically, the output of the machine, $\langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle$ ,is obtained as follows: (a) Calculate the rate of change of ${ \pmb v } .$ $\yen 1$ ，along the vector $\pmb { u }$ ；when $\pmb { u }$ and $\pmb { \nu }$ are infinitesimally small, the calculation can be represented pictorially:

![](images/3190889cb58244799ef3f8d29de2e80c9dcc1ace240e150b24bef6b04bcb96f3.jpg)  
$\yen 1$ a vector that resides in the tangent space at $\scriptstyle { \mathcal { P } } _ { 0 }$

(b) Count how many surfaces of the l-form $\pmb { \sigma }$ are pierced by the vector $\yen 1$ (piercing occurs in tangent space at $\scriptstyle { \boldsymbol { \mathscr { s } } } _ { 0 } .$ ）

![](images/5a096cc3c6ddc96de52bdeebc5d542340be3ee2bad97f92fde1ea5e016d2a2cd.jpg)

$$
\langle \pmb { \sigma } , \pmb { \nabla _ { u } } \pmb { v } \rangle = - 2 . 8 .
$$

This number is the output of the machine $\blacktriangledown$ ,when $\pmb { \sigma }$ ${ \pmb v } ( \mathcal { P } )$ and $\pmb { u }$ are inserted into its slots.

3.Another, equivalent, statement of covariant derivative as a machine.Leave first slot empty (no mention of any 1-form $\pmb { \sigma }$ ); get a new vector field from original vector field $\pmb { \nu }$ ：

empty

=“covariant derivative of vector field $\pmb { \nu }$ along vector u."

4.A third machine operation. Leave first and third slots empty (no mention of any 1-form $\pmb { \sigma }$ ； no mention of any vector ${ \pmb u }$ along which to differentiate); get a (l) tensor field from original vector field $\pmb { \nu }$ ：

$$
\pmb { \bigtriangledown } ( \underbrace { \mathbf { \Pi } } _ { : : : } , \pmb { v } ( \pmb { \mathcal { P } } ) , \underbrace { \mathbf { \Pi } } _ { : : : } ) \equiv \pmb { \nabla } \pmb { v }
$$

This tensor field, $\forall v ,$ ,is the curved-space generalization of the flat-space $\forall v$ studied in $\ S 3 . 5$ . It has two slots (the two left empty in its definition). Its output for given input is

$$
\pmb { \nabla } \pmb { v } ( \underbrace { \vphantom { \ d u ( \pmb { v } } , \pmb { u } ) } _ { : : : : } , \pmb { u } ) = \pmb { \nabla } _ { \pmb { u } } \pmb { v }
$$

$$
\begin{array} { r } { \pmb { \nabla } \pmb { v } ( \pmb { \sigma } , \pmb { u } ) = \langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle . } \end{array}
$$

5. Summary of the quantities defined above:

(a) $\blacktriangledown$ is a covariant derivative operator; to get a number from it, insert ${ \pmb \sigma } , { \pmb v } ( \mathcal { P } )$ and $\pmb { u }$ ； the result is $\langle \pmb { \sigma } , \pmb { \ v } _ { \pmb { \ u } } \pmb { v } \rangle$   
(b) $\forall v$ is the gradient of $\pmb { \nu }$ ；to get a number from it,insert $\pmb { \sigma }$ and $\pmb { u }$ ；the result is $\langle \pmb { \sigma } , \pmb { \check { \bigtriangledown } } _ { \pmb { u } } \pmb { v } \rangle$ [same as in (a)}.   
(c） $\yen 1$ is the covariant derivative of $\pmb { \nu }$ along $\pmb { u }$ ; to get a number from it,insert $\pmb { \sigma }$ ； the result is $\langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle$ [same as in (a) and (b)).

# B. How $\blacktriangledown$ Differs from a Tensor

The machine $\blacktriangledown$ differs from a tensor in two ways. (l) The middle slot of $\blacktriangledown$ will not accept a vector; it demands a vector feld-the vector field that is to be differentiated. (2) V is not a linear machine (whereas a tensor must be linear!):

$$
\begin{array} { r l } & { \Psi ( a \sigma . f ( \mathcal { S } ^ { \rho } ) \pmb { v } ( \mathcal { S } ^ { \rho } ) , b \pmb { u } ) \equiv \langle a \sigma , \pmb { \nabla } _ { b \pmb { u } } f \pmb { v } \rangle } \\ & { \qquad = a b f \langle \sigma , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle + \underbrace { a b \langle \sigma , \pmb { v } \rangle \ \pmb { \nabla } _ { \pmb { u } } f } _ { \pmb { \downarrow } } } \\ & { \qquad \quad \mathrm { [ t h i s ~ w o u l d ~ b e ~ a b s e n t ~ i f ~ \pmb { v } ~ w e r e ~ a ] } \} } \\ & { \qquad \quad \mathrm { l i n e a r ~ m a c h i n e } . } \end{array}
$$

# C. The "Connection Coefficients" as Components of $\blacktriangledown$

Given a tensor $\pmb { s }$ of rank $\textstyle { \binom { 1 } { 2 } }$ ,a basis of tangent vectors $\{ \pmb { e } _ { \alpha } \}$ at the event $\mathcal { P } _ { 0 }$ where $\pmb { s }$ resides,and the dual basis of 1-forms $\{ \pmb { \omega } ^ { \alpha } \}$ ,one defines the components of $\pmb { s }$ by

$$
S ^ { \alpha } { } _ { \beta \gamma } \equiv \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } , \pmb { e } _ { \gamma } ) .
$$

One defines the components of $\blacktriangledown$ similarly, except that for $\blacktriangledown$ one needs not only a basis $\{ \pmb { e } _ { \alpha } \}$ at the event ${ \mathcal { P } } _ { 0 } ,$ but also a basis $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ at each event $\mathcal { P }$ in its neighborhood:

$$
\begin{array} { r l } & { \Gamma ^ { \alpha } { } _ { \beta \gamma } \equiv \mathrm { c o m p o n e n t s ~ o f ~ } \Psi = \Psi ( \boldsymbol { \omega } ^ { \alpha } , \boldsymbol { \mathbf { e } } _ { \beta } ( \mathcal { P } ) , \boldsymbol { \mathbf { e } } _ { \gamma } ) } \\ & { \qquad \equiv \langle \boldsymbol { \omega } ^ { \alpha } , \nabla _ { \pmb { e } _ { \gamma } } \mathbf { e } _ { \beta } \rangle } \\ &  \qquad \simeq \bigg ( \begin{array} { l } { \mathrm { \cdots } \mathrm { { \alpha } c o m p o n e n t ~ o f ~ c h a n g e ~ i n ~ b a s i s ~ v e c t o r ~ } \pmb { e } _ { \beta } , \mathrm { ~ w h e n } } \\ { \mathrm { i n ~ e v a l u a t i n g ~ } \pmb { e } _ { \beta } \mathrm { ~ o n e ~ m o v e s ~ f r o m ~ t a i l ~ t o ~ t i p ~ o f ~ } \pmb { e } _ { \gamma } \bigg ) . } \end{array} \end{array}
$$

These components of $\blacktriangledown$ are called the “connection coeffcients” of the basis $\big \{ \pmb { e } _ { \alpha } \big \}$ They are the “coordinate representation’of the covariant derivative operator $\blacktriangledown$

Thecovariant derivativeoperator $\blacktriangledown$ and the connection coeficients $\Gamma ^ { \alpha } { } _ { \mu \nu }$ provide different mathematical representations of the same geometric animal? Preposterous! The one animal runs from place to place and barks, or at least bites (takes difference, for example,between vector fields at one place and at a nearby place).The other animal, endowed with forty faces (see exercise 10.9) sits quietly at one spot. It would be difficult for two animals to look more different. Yet they do the same jobs in any world compatible with the equivalence principle: (1） they summarize the properties of all geodesics that go through the point in question; and,so doing, (2) they provide a physical means (parallel transport) to compare the values of vector fields and tensor fields at two neighboring events.

given input vectors $\pmb { \nu }$ and $\pmb { u }$ if ${ \pmb v } ( \mathcal { P } )$ is not constrained to be “constant” along $\pmb { \upsilon } = \pmb { d } / d \lambda$ ,then $( d / d \lambda ) \langle \pmb { \sigma } , \pmb { v } \rangle$ has contributions from both the change in $\pmb { \nu }$ and the change in $\pmb { \sigma }$ ：

$$
\frac { d } { d \lambda } \langle \sigma , v \rangle \equiv \pmb { \nabla } _ { u } \langle \sigma , v \rangle = \langle \pmb { \nabla } _ { u } \sigma , v \rangle + \langle \sigma , \pmb { \nabla } _ { u } v \rangle
$$

(see exercise 10.3).

Similarly, if $\pmb { s }$ is a $\mathbf { \Sigma } ( _ { 2 } ^ { 1 } )$ tensor field, then its gradient VS is a $\textstyle { \binom { 1 } { 3 } }$ tensor field defined as follows. Pick an event $\mathcal { P } _ { \mathbf { 0 } }$ pick three vectors ${ \pmb u } , { \pmb v } , { \pmb w } ,$ and a 1-form $\pmb { \sigma }$ in the tangent space at $\mathcal { P } _ { 0 } \mathrm { : \Omega }$ turn $\nu , w ,$ and $\pmb { \sigma }$ into “constant” vector fields and a “constant” 1-form field near $\mathcal { P } _ { \mathbf { 0 } }$ by means of parallel transport ( $\mathbf { \nabla } \cdot \mathbf { \vec { v } } _ { u } \mathbf { \vec { v } } = \mathbf { \nabla } \cdot \mathbf { \vec { w } } = \mathbf { \nabla } \cdot \mathbf { \vec { v } } _ { u } \mathbf { \vec { \sigma } } = 0$ at ${ \mathcal { P } } _ { 0 } ,$ ； then define

$$
\begin{array} { c } { { \nabla S ( \sigma , v , w , { \boldsymbol u } ) \equiv ( \nabla _ { \boldsymbol u } S ) ( \sigma , v , { \boldsymbol w } ) \equiv \nabla _ { \boldsymbol u } [ S ( \sigma , v , { \boldsymbol w } ) ] } } \\ { { { } } } \\ { { { } = \partial _ { \boldsymbol u } [ S ( \sigma , v , { \boldsymbol w } ) ] . } } \end{array}
$$

# Exercise 1O.1. ADDITIVITY OF COVARIANT DIFFERENTIATION

Show that the commutator ("closer of quadrilaterals") is additive:

$$
[ u , v + w ] = [ u , v ] + [ u , w ] ; \qquad [ u + n , v ] = [ u , v ] + [ n , v ] .
$$

Use this result,the additivity condition $\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } ( \pmb { v } + \pmb { w } ) = \pmb { \nabla } _ { \pmb { u } } \pmb { v } + \pmb { \nabla } _ { \pmb { u } } \pmb { w } , } \end{array}$ and symmetry of the covariant derivative, $\begin{array} { r } { \nabla _ { u } v - \nabla _ { v } u = [ u , v ] , } \end{array}$ to prove that

$$
\pmb { \nabla } _ { \pmb { u } + \pmb { m } } \pmb { v } = \pmb { \nabla } _ { \pmb { u } } \pmb { v } + \pmb { \nabla } _ { \pmb { n } } \pmb { v } .
$$

# Exercise 1O.2. CHAIN RULE FOR COVARIANT DIFFERENTIATION

Use pictures,and the “take-the-diference-and-take-the-limit” definition of $\yen 1$ (Box 10.2) to show that

$$
\pmb { \nabla _ { \pmb { u } } } ( f \pmb { v } ) = f \pmb { \nabla _ { \pmb { u } } } \pmb { v } + \pmb { v } \partial _ { \pmb { u } } [ f ] .
$$

# Exercise 1O.3. ANOTHER CHAIN RULE

Derive equation (l0.7)，using the “take-the-difference-and-take-the-limit” definitions of derivatives. Hint:Before taking the differences,parallel transport $\pmb { \sigma } [ \mathcal { P } ( \lambda ) ]$ and ${ \pmb v } \widetilde { \mathscr { P } } ( \lambda ) ]$ back from $\mathcal { P } ( \lambda )$ to ${ \mathcal { P } } ( 0 )$

# Exercise 1O.4. STILL ANOTHER CHAIN RULE

Show that, as in flat spacetime,so also in curved spacetime,

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } ( \pmb { v } \otimes \pmb { w } ) = ( \pmb { \nabla } _ { \pmb { u } } \pmb { v } ) \otimes \pmb { w } + \pmb { v } \otimes ( \pmb { \nabla } _ { \pmb { u } } \pmb { w } ) . } \end{array}
$$

Write down the more familiar component version of this equation in flat spacetime.

Solution to first part of exercise: Choose l-forms $\pmb { \sigma }$ and $\pmb { \rho }$ at the event $\scriptstyle { \mathcal { P } } _ { 0 }$ in question, and extend them along the vector $\pmb { u } = d / d \lambda$ by parallel transport, $\yen 123,456$ .Then

(def of $\pmb { \check { \check { \mathbf { \alpha } } } } _ { \pmb { \alpha } }$ on a tensor)

def of tensor product “ $\cdot \otimes ^ { \dag }$ ）

$$
{ \begin{array} { l } { \displaystyle [ \nabla _ { \boldsymbol { u } } ( { \boldsymbol { v } } \otimes { \boldsymbol { w } } ) ] ( \rho . \sigma ) = { \frac { d } { d \lambda } } [ ( { \boldsymbol { v } } \otimes { \boldsymbol { w } } ) ( \rho , \sigma ) ] } \\ { \displaystyle \qquad = { \frac { d } { d \lambda } } [ \langle \rho , { \boldsymbol { v } } \rangle \langle \sigma . { \boldsymbol { w } } \rangle ] } \\ { \displaystyle \qquad = { \frac { d \langle \rho , { \boldsymbol { v } } \rangle } { d \lambda } } \langle \sigma , { \boldsymbol { w } } \rangle + \langle \rho , { \boldsymbol { v } } \rangle { \frac { d \langle \sigma , { \boldsymbol { w } } \rangle } { d \lambda } } } \\ { \displaystyle \qquad = \langle \rho , \nabla _ { \boldsymbol { u } } { \boldsymbol { v } } \rangle \langle \sigma , { \boldsymbol { w } } \rangle + \langle \rho , { \boldsymbol { v } } \rangle \langle \sigma , \nabla _ { \boldsymbol { u } } { \boldsymbol { w } } \rangle } \\ { \displaystyle \qquad = [ ( \nabla _ { \boldsymbol { u } } { \boldsymbol { v } } ) \otimes { \boldsymbol { w } } ] ( \rho , \sigma ) + [ \mathbf { v } \otimes ( \nabla _ { \boldsymbol { u } } { \boldsymbol { w } } ) ] ( \rho , \sigma ) } \end{array} }
$$

(def of tensor product $\ " \otimes \ " )$

# Exercise 10.5. ONE MORE CHAIN RULE

Show,using techniques similar to those in exercise l0.4, that

$$
\begin{array} { r } { \Psi _ { u } ( \sigma \otimes \rho \otimes v ) = ( \pmb { \nabla } _ { u } \sigma ) \otimes \rho \otimes \pmb { v } + \sigma \otimes ( \pmb { \nabla } _ { u } \rho ) \otimes \pmb { v } + \sigma \otimes \rho \otimes ( \pmb { \nabla } _ { u } \pmb { v } ) . } \end{array}
$$

# Exercise 10.6. GEODESIC EQUATION

Use the “Schild's ladder" construction process for parallel transport (beginning of Box l10.2) to show that a geodesic paralel transports its own tangent vector along itself (end of Box 10.2).

# S10.4. PARALLEL TRANSPORT AND COVARIANTDERIVATIVE: COMPONENT APPROACH

The pictorial approach motivates the mathematics; the abstract approach makes the pictorial ideas precise; but usually one must use the component approach in order to actually do complex calculations.

To work with components, one needs a set of basis vectors $\{ \pmb { e } _ { \alpha } \}$ and the dual set of basis 1-forms $\{ \pmb { \omega } ^ { \alpha } \}$ . In flat spacetime a single such basis suffices; all events can use the same Lorentz basis. Not so in curved spacetime! There each event has its own tangent space, and each tangent space requires a basis of its own. As one travels from event to event, comparing their bases via parallel transport, one sees the bases twist and turn. They must do so. In no other way can they accommodate themselves to the curvature of spacetime. Bases at points $\mathcal { P } _ { 0 }$ and $\mathcal { P } _ { 1 } .$ ，which are the same when compared by parallel transport along one curve, must differ when compared along another curve (see “Curvature"; Chapter 11).

To quantify the twisting and turning of a “field” of basis vectors $\{ \pmb { e } _ { \alpha } ( { \mathcal { P } } ) \}$ and forms $\{ \pmb { \omega } ^ { \alpha } ( \mathcal { P } ) \}$ , use the covariant derivative. Examine the changes in vector fields along a basis vector ${ \pmb { e } } _ { \beta }$ ,abbreviating

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { \theta } _ { \beta } } } \equiv \pmb { \nabla _ { \beta } } \qquad ( \operatorname* { d e f } \ \mathrm { o f } \ \pmb { \nabla _ { \beta } } ) ; } \end{array}
$$

and especially examine the rate of change of some basis vector: $\pmb { \nabla } _ { \beta } \pmb { e } _ { \alpha } ,$ Thisrate of change is itself a vector, so it can be expanded in terms of the basis:

$$
\begin{array} { r } { \pmb { \nabla } _ { \beta } \pmb { e } _ { \alpha } = \pmb { e } _ { \mu } { \cal T } _ { \alpha \beta } ^ { \mu } \qquad ( \operatorname* { d e f } \operatorname { o f } { \varGamma ^ { \mu } } _ { \alpha \beta } ) ; } \end{array}
$$

note reversal of order of $\pmb { \alpha }$ and $\beta$ ！

and the resultant“connection coeffcients" $T ^ { \mu } { } _ { \alpha \beta }$ can be calculated by projection on the basis 1-forms:

$$
\langle { \pmb { \omega } } ^ { \mu } , { \pmb { \nabla } } _ { \beta } { \pmb e } _ { \alpha } \rangle = { \cal T } ^ { \mu } { } _ { \alpha \beta } .
$$

(See exercise l0.7;also Box l0.3.） Because the basis 1-forms are “locked into” the basis vectors $( \langle { \pmb { \omega } } ^ { \nu } , { \pmb e } _ { \alpha } \rangle = \delta _ { \alpha } ^ { \nu } )$ , these same connection coefficients $T ^ { \nu } { } _ { \alpha \dot { \beta } }$ tell how the 1-form basis changes from point to point:

$$
\begin{array} { c } { { \pmb { \nabla } _ { \beta } \pmb { \omega } ^ { \nu } = - \pmb { \Gamma } ^ { \nu } { } _ { \alpha \beta } \pmb { \omega } ^ { \alpha } , } } \\ { { \langle \pmb { \nabla } _ { \beta } \pmb { \omega } ^ { \nu } , \pmb { e } _ { \alpha } \rangle = - \pmb { \Gamma } ^ { \nu } { } _ { \alpha \beta } . } } \end{array}
$$

(See exercise 10.8.)

The connection coefficients do even more. They allow one to calculate the components of the gradient of an arbitrary tensor $\pmb { s }$ . In a Lorentz frame of flat spacetime, the components of $\yen 5$ are obtained by letting the basis vectors ${ \pmb e } _ { \alpha } = \partial \mathcal { P } / \partial x ^ { \alpha } =$ $\partial / \partial x ^ { \alpha }$ act on the components of $\pmb { s }$ Thus for a $\mathbf { \Sigma } ( _ { 2 } ^ { 1 } )$ tensor field $\pmb { s }$ one finds that

$$
{ \pmb \nabla } { \pmb S } ~ \mathrm { h a s ~ c o m p o n e n t s } ~ S _ { ~ \beta \gamma , \delta } ^ { \alpha } = \frac { \partial } { \partial \pmb x ^ { \delta } } [ S _ { ~ \beta \gamma } ^ { \alpha } ] .
$$

Not so in curved spacetime, or even in a non-Lorentz basis in flat spacetime. There the basis vectors turn, twist, expand, and contract, so even if $\pmb { s }$ were constant $( \pmb { \nabla } \pmb { s } = 0 )$ , its components on the twisting basis vectors would vary. The connection coefficients, properly applied, wil compensate for this twisting and turning. As one learns in exercise l0.10,the components of $\yen 5$ ,called $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ so that

Components of the gradient ofa tensor field

$$
\pmb { \nabla } \pmb { S } = S ^ { \alpha } { } _ { \beta \gamma ; \pmb { \delta } } \pmb { \sigma } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } \otimes \pmb { \omega } ^ { \delta } ,
$$

can be calculated from those of $\pmb { s }$ by the usual flat-space method, plus a correction applied to each index (i.e., to each basis vector):

$$
 \begin{array} { r l } { { \boldsymbol { \mathfrak { n } } } : \mathbf { w h e n ~ c o r r e c t i n g ~ } ^ { * } \mathbf { u p } ^ { * } { \mathrm { ~ i n d i c e s } } \mathbf { \Psi } } & { { \left[ \begin{array} { l } { \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \\ { \mathrm { o n ~ i n d e x ~ b e i n g ~ c o r r e c t e d } } \\ { \displaystyle } \end{array} \right] } } \\ &  \qquad { \left[ \begin{array} { l } { \qquad \qquad \displaystyle { \begin{array} { l } { \qquad \qquad \displaystyle { \Biggl \downarrow } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } \left[ { \mathrm { i n d e x ~ b e i n g ~ i n d e x } } \right] } \end{array}  } } \qquad { \mathrm { i n d e x } } \mathbf { \Psi } } \\ { \right]\qquad { \boldsymbol { S } } ^ { \alpha } _ { \beta \gamma ; \delta } = { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \gamma , \delta } + { \boldsymbol { S } } ^ { \mu } { \boldsymbol { \beta } } _ { \gamma } { \boldsymbol { T } } ^ { \alpha } { \mathrm { ~ \dagger } } \mathbf { \Psi } ^ { \beta } _ { \beta \delta } - { \boldsymbol { \frac { \uparrow } { \alpha } } } { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \gamma } { \boldsymbol { T } } ^ { \mu } { \boldsymbol { \beta } } _ { \beta \delta } - { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \mu } { \boldsymbol { T } } ^ { \mu } { \boldsymbol { \gamma } } _ { \gamma \delta } , } \\ { \qquad \displaystyle { \left[ \begin{array} { l } { { \qquad \mathrm { i n t e n ~ c o r r e c t i n g ~ i n d i c e s } } \\ { \qquad \quad \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \\ { \qquad \displaystyle { \Biggl [ \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \end{array}  } } \qquad { \mathrm { V o r ~ } } \mathbf { \Psi } } \end{\right]array} } \end{array} \end{array}
$$

Here

$$
S ^ { \alpha } { } _ { \beta \gamma , \delta } \equiv e _ { \delta } [ S ^ { \alpha } { } _ { \beta \gamma } ] \equiv \partial _ { \pmb { \rho } _ { \delta } } S ^ { \alpha } { } _ { \beta \gamma } .
$$

Components of the covariant derivative of a tensor field

Equation (l0.18) looks complicated;but it is really very simple,once the pattern has been grasped.

Just as one uses special notation, $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ ，for the components of $\yen 5$ so one introduces special notation, $D S ^ { \alpha } { } _ { \beta \gamma } / d \lambda$ ,for components of the covariant derivative $\pmb { \nabla _ { \pmb { u } } } \pmb { S }$ along ${ \pmb u } = d / d \lambda$ ：

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { S } = ( D S ^ { \alpha } { } _ { \beta \gamma } / d \lambda ) \pmb { e _ { \alpha } } \otimes \pmb { \omega ^ { \beta } } \otimes \pmb { \omega ^ { \gamma } } ; } \end{array}
$$

$$
{ \frac { D S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } = S ^ { \alpha } { } _ { \beta \gamma ; \delta } u ^ { \delta } = ( S ^ { \alpha } { } _ { \beta \gamma , \delta } + \mathrm { c o r r e c t i o n ~ t e r m s } ) u ^ { \delta } .
$$

Since for any $f$

$$
f _ { , \delta } u ^ { \delta } = \partial _ { \pmb { u } } f = d f / d \lambda
$$

this reduces to

$$
{ \frac { D S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } = { \frac { d S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } + S ^ { \mu } { } _ { \beta \gamma } { } T ^ { \alpha } { } _ { \mu \delta } u ^ { \delta } - S ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta \delta } u ^ { \delta } - S ^ { \alpha } { } _ { \beta \mu } { } T ^ { \mu } { } _ { \gamma \delta } u ^ { \delta } .
$$

Chain rule for gradient

The power of the component approach shows up clearly when one discusses chain rules for covariant derivatives. The multitude of abstract-approach chain rules (equations l0.2b, l0.7,10.10,10.11) all boil down into a single rule for components: The gradient operation “;” obeys the standard partial-differentiation chain rule of ordinary calculus.Example:

$$
\begin{array}{c} ( f v ^ { \alpha } ) _ { ; \mu } = f _ { ; \mu } v ^ { \alpha } + f v _ { ; \mu } ^ { \alpha }  \\ { \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \mathrm { ~ } } \end{array}
$$

(contract this with $u ^ { \mu }$ to get chain rule l0.2b). Another example:

$$
\begin{array} { l } { { ( \sigma _ { \alpha } v ^ { \alpha } ) _ { ; \mu } = \sigma _ { \alpha ; \mu } v ^ { \alpha } + \sigma _ { \alpha } v ^ { \alpha } { } _ { ; \mu } } } \\ { { \mathrm { ~ } \qquad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } } \\ { { \mathrm { ~ } \qquad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } } \end{array}
$$

(contract this with $u ^ { \mu }$ to get chain rule 10.7). Another example:

$$
( \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } ) _ { ; \mu } = \sigma _ { \alpha ; \mu } \rho _ { \beta } v ^ { \gamma } + \sigma _ { \alpha } \rho _ { \beta ; \mu } v ^ { \gamma } + \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } { } _ { ; \mu }
$$

EXERCISES

(contract this with $u ^ { \mu }$ to get chain rule 10.11). Another example: see Exercise (10.12) below.

# Exercise 10.7. COMPUTATION OF CONNECTION COEFFICIENTS Derive equation (l0.l4) for $T ^ { \mu } { } _ { \alpha \beta }$ from equation (10.13).

Exercise 10.8. CONNECTION FOR 1-FORM BASIS   
Derive equations (l0.15) and (10.16), which relate ${ \pmb v } _ { \beta } { \pmb \omega } ^ { \nu }$ 10 ${ { T ^ { \nu } } _ { \alpha \beta } }$ ，from equation (10.14). Hint: use equation (10.7).

# Exercise 10.9. SYMMETRY OF CONNECTION COEFFICIENTS

Show that the symmetry of spacetime's covariant derivative (equation l0.2a) is equivalent to the following symmetry condition on the connection coefficients:

$$
\begin{array} { l }  { \equiv { \cal { T } } ^ { \mu } { } _ { [ \alpha \beta ] } = - \frac { 1 } { 2 } \langle { \pmb { \omega } } ^ { \mu } , \underbrace { [ { \pmb { e } } _ { \alpha } , { \pmb { e } } _ { \beta } ] } _ { \displaystyle \mathrm { ~ \pmb { \ / { \ / { \ / } } } ~ } } \rangle \equiv - \frac { 1 } { 2 } c _ { \alpha \beta } \mathrm { \tiny { / } } \mathrm { ~ \pmb { \ / { \ / { \ / } } } ~ } } \\ { \mathrm { m u t a t o r ~ o f ~ b a s i s ~ v e c t o r s } { \ ! } } \end{array}
$$

As a special case, $T ^ { \mu } { } _ { \alpha \beta }$ is symmetric in α and $\beta$ when a coordinate basis $( \pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha } )$ is used. Show that in a coordinate basis this symmetry reduces the number of independent connection coeffcients at each event from $4 \times 4 \times 4 = 6 4$ to $4 \times 1 0 = 4 0$

# Exercise 10.10. COMPONENTS OF GRADIENT

Derive equation (10.18)for the components of the gradient, $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ . Hint: Expand $\pmb { s }$ in terms of the given basis,and then evaluate the righthand side of

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { S } = \pmb { \nabla } _ { \pmb { u } } ( S ^ { \alpha } { } _ { \beta \gamma } \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ) , } \end{array}
$$

for an arbitrary vector $\pmb { u }$ Use the chain rules (l0.2b) and (l0.l1). By comparing the result with

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { S } = S ^ { \alpha } { } _ { \beta \gamma ; \delta } u ^ { \delta } \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ,
$$

read of te components $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$

# Exercise 10.11. DIVERGENCE

Let $\pmb { \tau }$ be a $\textstyle { { \binom { 2 } { 0 } } }$ tensor field,and define the divergence on its second slot by the same process as in flat spacetime: $\pmb { \bigtriangledown } \cdot \pmb { \tau } =$ contraction of $\forall \pmb { \tau } _ { }$ i.e.,

$$
( \pmb { \nabla } \cdot \pmb { \tau } ) ^ { \alpha } = T ^ { \alpha \beta } { } _ { ; \beta } .
$$

Write the components $T ^ { \alpha \beta } { } _ { ; \beta }$ in terms of $T ^ { \alpha \beta } { } _ { , \beta }$ plus correction terms for each of the two indices of ${ \pmb \tau } .$

[Answer:

$$
T ^ { \alpha \beta } { } _ { ; \beta } = T ^ { \alpha \beta } { } _ { , \beta } + { } T ^ { \alpha } { } _ { \mu \beta } T ^ { \mu \beta } + T ^ { \beta } { } _ { \mu \beta } T ^ { \alpha \mu } { } . ]
$$

# Exercise 10.12. VERIFICATION OF CHAIN RULE

Let $S ^ { \alpha \beta } { } _ { \gamma }$ be components of a $\mathbf { \Sigma } ( _ { 1 } ^ { 2 } )$ tensor field, and $M _ { \beta } { } ^ { \gamma }$ be components of a $\textstyle { { \binom { 1 } { 1 } } }$ tensor field. By contracting these tensor fields,one obtains a vector field $S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma }$ 、The chain rule for the divergence of this vector field reads

$$
( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { ; \alpha } = S ^ { \alpha \beta } { } _ { \gamma ; \alpha } M _ { \beta } { } ^ { \gamma } + S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } { } _ { ; \alpha } ,
$$

Verify the validity of this chain rule by expressing both sides of the equation in terms of directional derivatives $\{ \cdot _ { e _ { \alpha } } )$ plus connection-coefficient corrections. Hint: the left side becomes

$$
( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { ; \alpha } = \underbrace { ( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { , \alpha } } _ { \Big \uparrow } + \Gamma ^ { \alpha } { } _ { \mu \alpha } ( S ^ { \mu \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) .
$$

The right side has many more correction terms (three on $S ^ { \alpha \beta } { } _ { \gamma : \alpha }$ ： two on $M _ { \beta } { } ^ { \gamma } { } _ { ; \alpha } )$ , but they must cancel against each other, leaving only one.

Exercise 1O.13. TRANSFORMATION LAW FOR CONNECTION COEFFICIENTS

Let $\{ \pmb { e } _ { \alpha } \}$ and $\{ \pmb { e } _ { \mu ^ { \prime } } \}$ be two different fields of basis vectors related by the transformation law

$$
\pmb { e } _ { \mu ^ { \prime } } ( \vartheta ^ { \bar { p } } ) = L ^ { \alpha } { } _ { \mu ^ { \prime } } ( \vartheta ^ { \bar { p } } ) \pmb { e } _ { \alpha } ( \vartheta ^ { \bar { p } } ) .
$$

Show that the corresponding connection coefficients are related by

$$
\begin{array} { r } { { \int ^ { \alpha ^ { \prime } } } { } _ { \beta ^ { \prime } \gamma ^ { \prime } } = \underbrace { L ^ { \alpha ^ { \prime } } { } _ { \rho } L ^ { \mu } { } _ { \beta ^ { \prime } } L ^ { \nu } { } _ { \gamma ^ { \prime } } } _ { \beta ^ { \prime } \gamma ^ { \prime } } \Gamma ^ { \rho } { } _ { \mu \nu } + L ^ { \alpha ^ { \prime } } { } _ { \mu } L ^ { \mu } { } _ { \beta ^ { \prime } , \gamma ^ { \prime } } } \end{array}
$$

standard transformation law for components of a tensor

# Exercise 10.14. POLAR COORDINATES IN FLAT 2-DIMENSIONAL SPACE

On a sheet of paper draw an $( r , \phi )$ polar coordinate system. At neighboring points, draw the basis vectors $\pmb { e } _ { \hat { \tau } } = \hat { \partial } / \hat { c } r$ and $\pmb { e } _ { \hat { \phi } } \equiv r ^ { - 1 } \partial / \partial \phi$ .(a)Use this picture,and Euclid's version of parallel transport, to justify the relations

$$
\forall _ { \hat { \tau } } \pmb { e } _ { \hat { \tau } } = 0 , \qquad \pmb { \nabla } _ { \hat { \tau } } \pmb { e } _ { \hat { \phi } } = 0 , \qquad \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \tau } } = r ^ { - 1 } \pmb { e } _ { \hat { \phi } } , \qquad \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \phi } } = - r ^ { - 1 } \pmb { e } _ { \hat { \tau } } ,
$$

(b) From these relations write down the connection coeffcients. (c) Let $\pmb { A } = A ^ { \hat { \tau } } \pmb { e } _ { \hat { \tau } } + A ^ { \hat { \phi } } \pmb { e } _ { \hat { \phi } }$ bea vectorfield. Show thatits divergence, $\pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { \alpha } } { } _ { ; \hat { \alpha } } = A ^ { \hat { \alpha } } { } _ { , \hat { \alpha } } + \Gamma ^ { \hat { \alpha } } { } _ { \hat { \mu } \hat { \alpha } } A ^ { \hat { \mu } }$ , can be calculated using the formula

$$
\pmb { \nabla } \cdot \pmb { A } = \frac { 1 } { r } \frac { \partial A \hat { \phi } } { \partial \phi } + \frac { 1 } { r } \frac { \partial ( r A ^ { \hat { \tau } } ) } { \partial r }
$$

(which should be familiar to most readers).

# \$10.5. GEODESIC EQUATION

Geodesic equation: abstract version

Geodesics--the parametrized paths of freely falling particles-were the starting point of this chapter. From them parallel transport was constructed (Schild's ladder; Box 10.2);and parallel transport in turn produced the covariant derivative and its connection coefficients. Given the covariant derivative, one recovered the geodesics: they were the curves whose tangent vectors, $\pmb { \upsilon } = d \mathcal { P } / d \lambda$ ，satisfy $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ $\mathbf { \widetilde { \mu } } _ { \pmb { { u } } }$ is parallel transported along itself).

Let a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ be given.Let it induce basis vectors $\pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha }$ into the tangent space at each event. Let the connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ for this “coordinate basis” be given. Then the component version of the “geodesic equation” $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ becomes a differential equation for the geodesic $x ^ { \alpha } ( \lambda )$ ：

$$
\begin{array} { r } { \pmb { \mathscr { u } } = \frac { d } { d \lambda } = \frac { d x ^ { \alpha } } { d \lambda } \frac { \partial } { \partial x ^ { \alpha } } \quad \Longrightarrow } \end{array}
$$

(2） then components of $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ are

$$
\begin{array} { r l } & { 0 = u ^ { \alpha } { } _ { ; \beta } u ^ { \beta } = ( u ^ { \alpha } { } _ { , \beta } + \Gamma ^ { \alpha } { } _ { \gamma \beta } u ^ { \gamma } ) u ^ { \beta } } \\ & { \quad = \frac { \partial } { \partial x ^ { \beta } } \bigg ( \frac { d x ^ { \alpha } } { d \lambda } \bigg ) \frac { d x ^ { \beta } } { d \lambda } + \Gamma ^ { \alpha } { } _ { \gamma \beta } \frac { d x ^ { \gamma } } { d \lambda } \frac { d x ^ { \beta } } { d \lambda } , } \end{array}
$$

which reduces to the differential equation

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \alpha } { } _ { \gamma \beta } \frac { d x ^ { \gamma } } { d \lambda } \frac { d x ^ { \beta } } { d \lambda } = 0 .
$$

Component version

This component version of the geodesic equation gives an analytic method ("translation”of Schild's ladder） for constructing the parallel transport law from a knowledge of the geodesics. Pick an event $\mathcal { P } _ { \mathbf { 0 } }$ and set up a coordinate system in its neighborhood. Watch many clock-carrying particles pass through (or arbitrarily close to) $\mathcal { P } _ { \mathbf { 0 } }$ .For each particle read off the values of $d ^ { 2 } x ^ { \alpha } / d \lambda ^ { 2 }$ and $d x ^ { \alpha } / d \lambda$ at $\mathcal { P } _ { \mathbf { 0 } } .$ Insert all the data for many particles into equation (lo.27),and solve for the connectioncoecientsostubdatlyet $T ^ { \alpha } { } _ { \gamma \beta }$ is obtained thereby; the antisymmetric part $T ^ { \alpha } { } _ { [ \gamma \beta ] }$ , vanishes identicallyin any coordinate frame! (See exercise 10.9.) Knowing $T ^ { \alpha } { } _ { \gamma \beta }$ ,use them to paralel transport any desired vector along any desired curve through $\mathcal { P } _ { \mathbf { 0 } }$ ：

How to construct parallel transport law from knowledge of geodesics

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { v } = 0 \quad \iff \quad \frac { d \pmb { v } ^ { \alpha } } { d \lambda } + \pmb { I } ^ { \alpha } \mathstrut _ { \gamma \beta } \pmb { v } ^ { \gamma } \frac { d \pmb { x } ^ { \beta } } { d \lambda } = 0 . } \end{array}
$$

# ExerCise 10.15. COMPONENTS OF PARALLEL-TRANSPORT LAW

EXERCISES

Show that equation (l0.28) is the component version of the law for parallel transporting a vector $\pmb { v }$ along the curve $\mathcal { P } ( \lambda )$ with tangent vector $\pmb { \upsilon } = d \mathcal { P } / d \lambda$

# Exercise 10.16. GEODESICS IN POLAR COORDINATES

In rectangular coordinates on a flat sheet of paper, Euclid's straight lines (geodesics) satisfy $d ^ { 2 } x / d \lambda ^ { 2 } = d ^ { 2 } y / d \lambda ^ { 2 } = 0$ 、Transform this geodesic equation into polar coordinates $( x =$ $r \ \cos \ \phi , \ y = r$ sin $\phi$ )；and read off the resulting connection coefficients by comparison with equation (lO.27). These are the connection coeficients for the coordinate basis $( \hat { \boldsymbol { o } } / \hat { \boldsymbol { o } } \boldsymbol { r } ,$ $\hat { \partial } / \hat { \partial } \phi )$ .From them calculate the connection coefficients for the basis

$$
\pmb { e } _ { \hat { \tau } } = \frac { \hat { \partial } } { \hat { o } r } , \qquad \pmb { e } _ { \hat { \phi } } = \frac { 1 } { r } \frac { \hat { c } } { \hat { \partial } \phi } .
$$

The answer should agree with the answer to part (b) of Exercise l0.l4. Hint: Use such relations as

$$
\Psi _ { e _ { \odot } } e _ { \hat { r } } = \Psi _ { ( 1 / \tau ) ( \hat { \partial } / \hat { \partial } \phi ) } ( \hat { c } / \partial r ) = \frac { 1 } { r } \Psi _ { ( \hat { \partial } / \hat { \partial } \phi ) } ( \hat { o } / \partial r ) .
$$

# Exercise 10.17. ROTATION GROUP:GEODESICS AND CONNECTION COEFFICIENTS

[Continuation of exercises 9.l3 and 9.l4.] In discussing the rotation group,one must make a clear distinction between the Euclidean space (coordinates $x , y , z$ ；basis vectors $\partial / \partial x , \partial / \partial y$ ， $\hat { \sigma } / \hat { \sigma } z )$ in which the rotation matrices act. and the group manifold $S O ( 3 )$ (coordinates $\downarrow , \theta .$ ， $\phi$ ; coordinate basis $\hat { \sigma } / \hat { c } \downarrow , \hat { \sigma } / \hat { \sigma } \theta , \hat { c } / \hat { \sigma } \phi$ ；basis of"generators” $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 } )$ ,whose points $\mathcal { P }$ are rotation matrices.

(a) Pick a vector

$$
\pmb { n } = \pmb { n } ^ { x } \hat { \sigma } / \hat { \sigma } x + \pmb { n } ^ { y } \hat { \sigma } / \hat { \sigma } y + \pmb { n } ^ { z } \hat { \sigma } / \hat { \sigma } z
$$

in Euclidean space. Show that

$$
\begin{array} { r } { \ddot { \mathcal { R } } _ { n } ( t ) \equiv \exp [ ( n ^ { x } ; \ddot { \lambda _ { 1 } } + n ^ { y } ; \ddot { \lambda _ { 2 } } + n ^ { z } ; \ddot { \lambda _ { 3 } } ) t ] } \end{array}
$$

is a rotation matrix that rotates the axes of Euclidean space by an angle

$$
t | n | = t [ ( n ^ { z } ) ^ { 2 } + ( n ^ { y } ) ^ { 2 } + ( n ^ { z } ) ^ { 2 } ] ^ { 1 / 2 }
$$

about the direction $\pmb { n }$ $( \bar { \mathcal { A } } _ { \ j } ^ { - }$ are matrices defined in exercise 9.13.)

(b) In the group manifold $S O ( 3 )$ ，pick a point (rotation matrix) $\mathcal { P }$ ,and pick a tangent vector $\pmb { u } = u ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ at $\mathcal { P }$ Let $\pmb { u }$ be a vector in Euclidean space with the same components as $\pmb { u }$ has in $S O ( 3 )$ ：

$$
{ \pmb u } = u ^ { 1 } { \pmb e } _ { 1 } + u ^ { 2 } { \pmb e } _ { 2 } + u ^ { 3 } { \pmb e } _ { 3 } ; \qquad { \pmb u } = u ^ { 1 } \hat { v } / \hat { v } x + u ^ { 2 } \hat { v } / \hat { v } y + u ^ { 3 } \hat { v } / \hat { v } z .
$$

Show that $\pmb { u }$ is the tangent vector (at $t = 0$ ）to the curve

$$
\mathcal { C } ( t ) = \mathcal { R } _ { \boldsymbol { u } } ( t ) \mathcal { P } .
$$

The curve $\mathcal { C } ( t )$ through the arbitrary point $\mathcal { P }$ with arbitrary tangent vector $\pmb { u } = ( d \mathcal { C } / d t ) _ { t = 0 }$ is a very special curve:every point on it differs from $\mathcal { P }$ by a rotation $\boldsymbol { \mathcal { R } } _ { \boldsymbol { \mu } } ( t )$ about one and the same direction $\pmb { u }$ No other curve in $S O ( 3 )$ with “starting conditions” $\{ \mathcal { P } , \pmb { u } \}$ has such beautiful simplicity.Hence it is natural to decree that each such $\mathcal { C } ( t )$ is a geodesic of the group manifold $S O ( 3 )$ 、This decree adds new geometric structure to $S O ( 3 )$ ; it converts $S O ( 3 )$ from a differentiable manifold into something more special: an affine manifold.

One has no guarantee that an arbitrarily chosen family of curves in an arbitrary manifold can be decreed to be geodesics.Most families of curves simply do not possess the right geometric properties to function as geodesics. Most will lead to covariant derivatives that violate one or more of the fundamental conditions (l0.2). To learn whether a given choice of geodesics is possible, one can try to derive connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ (for some given basis)corresponding to the chosen geodesics.If the derivation is successful, the choice of geodesics was a possble one. If the derivation produces inconsistencies,the chosen family of curves have the wrong geometric properties to function as geodesics.

(c) For the basis of generators $\{ \pmb { e } _ { \alpha } \}$ derive connection coefficients corresponding to the chosen geodesics, $\mathcal { C } ( t ) = \mathcal { R } _ { u } ( t ) \mathfrak { s } \bar { \mathcal { P } } ,$ of $S O ( 3 )$ . Hint: show that the components $u ^ { \alpha } = \langle { \pmb { \omega } } ^ { a } , { \pmb { \omega } } \rangle$ of the tangent $\pmb { \mu } = d \mathcal { E } / d t$ to a given geodesic are independent of position $\mathcal { C } ( t )$ along the geodesic. Then use the geodesic equation $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ ,expanded in the basis $\{ e _ { \alpha } \}$ , to calculate the symmetric part of the connection $T ^ { \alpha } { } _ { ( \beta \gamma ) }$ Finally use equation(10.23)tocalculate $\Gamma ^ { \alpha } { } _ { [ \beta \gamma ] }$ [Answer:

$$
T ^ { \alpha } { } _ { \beta \gamma } = \frac { 1 } { 2 } \epsilon _ { \alpha \beta \gamma } ,
$$

where $\epsilon _ { \alpha \beta \gamma }$ is the completely antisymmetric symbol with $\epsilon _ { 1 2 3 } = + 1$ This answer is independent of location $\mathcal { P }$ in $S O ( 3 ) ! ]$

# CHAPTER 11

# GEODESIC DEVIATION AND SPACETIME CURVATURE

Spacetime curvature manifests itself as gravitation, by means of the deviation of one geodesic from a nearby geodesic (relative acceleration of test particles).

Let the geodesics of spacetime be known. Then the covariant derivative $\blacktriangledown$ and its connection coeffcients ${ T ^ { \alpha } } _ { \beta \gamma }$ arealsoknonHowromtisoatiodoes one define, calculate, and understand geodesic deviation and spacetime curvature? The answer unfolds in this chapter, and is summarized in Box 11.1. To disclose the answer one must (l) define the “relative acceleration vector" $\yen 123,456$ which measures the deviation of one geodesic from another $( \ S 1 1 . 2 )$ ； (2) derive an expression in terms of $\blacktriangledown$ or $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ for the“Riemann curvature tensor,”which produces the geodesic deviation $( \ S 1 1 . 3 )$ ; (3) see Riemann curvature at work, producing changes in vectors that are parallel transported around closed circuits (S11.4);(4)see Riemann curvature test whether spacetime is flat (S11.5); and (5) construct a special coordinate system,“Riemann normal coordinates,"which is tied in a special way to the Riemann curvature tensor (S11.6).

This chapter is entirely   
Track 2.Chapters 9 and 10 are   
necessary preparation for it. It will be needed as   
preparation for (1) Chapters 12 and 13 (Newtonian gravity: Riemannian geometry), (2) the second half of Chapter 14 (calculation of curvature), and (3) the details,but not the message,of Chapter 15 (Bianchi identities).

# $\$ 12$ . THE RELATIVE ACCELERATION OF NEIGHBORING GEODESICS

Focus attention on a family of geodesics (Figure l1.1). Let one geodesic be distinguished from another by the value of a“selector parameter" $\pmb { n }$ .The family includes not only geodesics $n = 0 , 1 , 2 , \ldots$ but also geodesics for all intervening values of

Geometry of a family of geodesics:

Selector parameter

# BoX 11.1 GEODESIC DEVIATION AND RIEMANN CURVATURE IN BRIEF

"Geodesic separation" $\pmb { n }$ is displacement (tangent vector) from point on fiducial geodesic to point on nearby geodesic characterized by same value of affine parameter $\lambda$

Geodesic separation changes with respect to $\lambda$ (i.e., changes along the tangent vector $\pmb { \upsilon } = d / d \lambda$ ） at a rate given by the equation of geodesic deviation

$$
\nabla _ { u } \ \nabla _ { u } n + R i e m a m n \left( \ldots , { u } , n , { u } \right) = 0
$$

(second-order equation; see $\ S \ S 1 . 6$ and 1.7; Figures 1.10, 1.11, 1.12).

In terms of components of the Riemann tensor the driving force("tidal graviational force") is

$$
( . . . , { \pmb u } , { \pmb n } , { \pmb u } ) = { \pmb e } _ { \alpha } R ^ { \alpha } { } _ { \beta \gamma \delta } u ^ { \beta } n ^ { \gamma } u ^ { \delta } .
$$

The components of the Riemann curvature tensor in a coordinate frame are given in terms of the connection coefficients by the formula

$$
\begin{array} { l } { { R ^ { \alpha } { } _ { \beta \gamma \delta } = \displaystyle \frac { \partial T ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } - \frac { \partial T ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } } } \\ { { + T ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta \delta } - T ^ { \alpha } { } _ { \mu \delta } { \cal T ^ { \mu } } _ { \beta \gamma } . } } \end{array}
$$

This curvature tensor not only quantifies the concept of “tidal gravitational force,” but also enters into Einstein's law, by which “matter tells spacetime how to curve.” That law, to be studied in later chapters, takes the following operationalcomputational form in a given coordinate system:

(a)Write down trial formula for dynamic evolution of metric coefficients $g _ { \mu \nu }$ with time.

(b) Calculate the connection coefficients from

$$
\begin{array} { r } { { T ^ { \alpha } } _ { \mu \nu } = g ^ { \alpha \beta } { \cal T } _ { \beta \mu \nu } ; } \end{array}
$$

$$
{ \cal T } _ { \beta \mu \nu } = { \frac { 1 } { 2 } } \bigg ( { \frac { \partial g _ { \beta \nu } } { \partial x ^ { \mu } } } + { \frac { \partial g _ { \beta \mu } } { \partial x ^ { \nu } } } - { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \beta } } } \bigg )
$$

(derived in Chapter 13).

(c) Calculate Riemann curvature tensor from equation (3).

(d) Calculate Einstein curvature tensor from

$$
G _ { \mu \nu } = { R ^ { \alpha } } _ { \mu \alpha \nu } - { \frac { 1 } { 2 } } g _ { \mu \nu } g ^ { \sigma \tau } { R ^ { \alpha } } _ { \sigma \alpha \tau }
$$

(geometric significance in Chapter 15).

(e) Insert into Einstein's equations (Chapter 17):

$$
\begin{array} { r l r l } & { G _ { \mu \nu } = 0 } & & { ( \mathrm { e m p t y ~ s p a c e } ) , } \\ & { G _ { \mu \nu } = 8 \pi T _ { \mu \nu } } & & { ( \mathrm { w h e n ~ m a s s  – e n e r g y ~ i s } } \end{array}
$$

(f） Test whether the trial formula for the dynamic evolution of the geometry was correct, and, if not, change it so it is.

Affine parameter

$\pmb { n } .$ The typical point $\mathcal { P }$ on the typical geodesic will be a continuous, doubly differentiable function of the selector parameter $\pmb { n }$ and the affine parameter $\lambda$ ； thus

$$
{ \mathcal { P } } = { \mathcal { P } } ( \lambda , n ) .
$$

Tangent vector

The tangent vector

$$
\pmb { u } = \frac { \partial \mathcal { P } } { \partial \lambda } \qquad ( \mathbf { C a r t a n \ n o t a t i o n } )
$$

or

$$
\pmb { u } = \frac { \partial } { \partial \lambda } \qquad \mathrm { ( n o t a t i o n ~ o f ~ t h i s ~ b o o k ) }
$$

is constant along any given geodesic in this sense: the vector $\pmb { u }$ at any point, trans-

![](images/fa9b741e11443dbcb279ceae37216f23809c4d79345b6934d4ed3c8eb1894407.jpg)  
Figure 11.1. One-parameter family of geodesics.The“selector parameter" $\pmb { n }$ tells which geodesic. The affine parameter $\lambda$ tells where on a given geodesic. The two tangent vectors indicated in the diagram are ${ \pmb u } =$ $\partial / \partial \lambda$ (Cartan: $\partial \mathscr { P } / \partial \lambda$ and ${ \pmb n } = \partial / \partial { \pmb n }$ (Cartan: $\hat { c } \hat { \mathscr { P } } / \hat { \mathscr { o } } n$ .

ported parallel to itself along the geodesic, arrives at a second point coincident in direction and length with the $\pmb { u }$ already existing at that point.

The“separation vector”

$$
\pmb { \eta } = \frac { \partial \pmb { \mathcal { P } } } { \partial \pmb { n } } \qquad ( \mathbf { C a r t a n \ n o t a t i o n } )
$$

or

$$
{ \pmb { \eta } } = { \frac { \partial } { \partial { \pmb { n } } } } \qquad { \mathrm { ( n o t a t i o n ~ o f ~ t h i s ~ b o o k ) } }
$$

measures the separation between the geodesic $\pmb { n }$ ,regarded as the fiducial geodesic, and the typical nearby geodesic, $n + 4 n$ (for small $\varDelta n$ ), in the sense that

$$
( \varDelta n ) \pmb { \mathstrut } = \left\{ \begin{array} { c } { { \Delta n \frac { \hat { c } ^ { \acute { \sigma } } } { \partial n } \nonumber } } \\ { { \mathrm { ~ { \ m e a s u r e s ~ t h e } ~ \left\{ \begin{array} { l } { { \mathrm { P 0 s i t i o n } } } \\ { { \mathrm { a n y } } } \\ { { \mathrm { f u n c t i o n } } } \end{array} \right\} } } } \end{array} \right.
$$

brought about by transfer of attention from the one geodesic to the other at a fixed value of the affine parameter $\lambda$ . This vector is represented by the arrow $\because \mathcal { D } \mathcal { L } \mathcal { L }$ in the first diagram in Box 11.2.

(continued on page 270)

“Fiducial geodesic”n. Separation vector n $\varDelta n =$ $\mathfrak { M } \mathcal { Q }$ leads from point $\because \pi$ on it, to point $\underset { ^ { \prime } } { \underbrace { \mathcal { O } } }$ with same value of affine parameter $\lambda$ (timelike quantity） on neighboring “test geodesic” $n + 4 n$

![](images/a28ed6ee49bb9cfc9d6a84fcb9345dd05bc652da0c53211cab81c74fb0c3fa90.jpg)

![](images/9af3beffe23496169fabf1bbbcc215f0d4e2491dae4cf8d8ff59ba6a7917b13d.jpg)

Parallel transport of $\mathcal { D } \mathcal { Q }$ by “Schild's ladder construction”(Box 10.2） to $\mathcal { D B }$ and $\mathcal { L } \mathcal { Q }$ If the test geodesic $n + 4 n$ had kept a constant separation from the fiducial geodesic $\pmb { n } ,$ its tracer point would have arrived at $\boldsymbol { \mathcal { I } }$ at the value $( \lambda - \varDelta \lambda )$ of the affine parameter, and at $\mathcal { B }$ at $( \lambda + \varDelta \lambda )$

Actual location of tracer point of test geodesic at values of the timelike affine parameter $( \lambda - 4 \lambda )$ ， $\lambda ,$ and $( \lambda + \varDelta \lambda )$

![](images/42a96cdbf832790bdf36a4230cefc65f30c08e70095e7fa3569ddc8ec0825006.jpg)

![](images/1b77acd4d3120c6a8a9f2d65f24650c0eb5b2da8914fc7433347c0f5aceba57c.jpg)

Confrontation between actual course of tracer point on test geodesic and “canonical course": course it would have had to take to keep constant separation from the tracer point moving along the fiducial geodesic.

Test geodesic same as before, except for uniform stretchout in scale of affine parameter. Any measure of departure of the actual course of geodesic from the canonical course $( \mathcal { Q Q B } )$ , to be useful, should be independent of this stretchout. Hence, take as measure of geodesic deviation,not the vector $\mathcal { B R }$ alone,nor the vector ${ \mathcal { Q } } { \mathcal { P } } _ { : }$ ，but the stretch-independent combination $\pmb { \delta } _ { 2 } = ( \mathcal { B } \mathcal { R } ) +$ $( \mathcal { Q P } )$ . Here the sign of addition implies that the two vectors have been transported parallel to themselves, before addition, to a common point $\mathfrak { L }$ in the diagram; $\mathfrak { R }$ in the differential calculus limit $\varDelta n \longrightarrow 0$ ， $\varDelta \lambda \longrightarrow 0$ .

![](images/2e8e9f25c65d29e622945e8778694ce8a1bbc778116fdf106bee7d4932dfde2d.jpg)

![](images/2754f609928705fc30861d7f4da689834b8420ac2dc53f8738e100cfcb4e86a1.jpg)

Alternative courses that the test geodesic of $\mathbf { o }$ could have taken through $\mathcal { L }$ (families of geodesics characterized by different degrees of divergence from the left or convergence towards the right). Tilt changes values of $\mathcal { Q } \mathcal { P }$ (to $\vec { q } \bar { \mathcal { P } } )$ and BR (to $\mathbf { \widehat { \mathbf { \mathcal { A } } } } _ { 1 } \mathbf { \overline { { \mathbf { \mathcal { R } } } } }$ ） individually,but not value of the sum $\pmb { \delta } _ { 2 . } = ( \mathcal { B } \mathcal { R } )$ $+ \left( \mathcal { Q } \mathcal { P } \right)$ ("lever principle").

Note that arrow $\mathcal { B R }$ is of first order in $\pmb { \varDelta \lambda }$ and of first order in $\varDelta n$ ；similarly for $\mathcal { Q } \mathcal { P }$ ; hence the combination $\pmb { \delta } _ { 2 }$ is of second order in $\pmb { \varDelta } \lambda$ and first order in $\pmb { \varDelta n }$ .Conclude that the arrow $\pmb { \delta } _ { 2 } / ( \pmb { \varDelta } \lambda ) ^ { 2 } ( \pmb { \varDelta } n )$ is the desired measure of geodesic deviation in the sense that:

size of mesh (ultimately to go to zero) cancels out; parameterization of test geodesic cancels out; slope of test geodesic cancels out.

Give this arrow the name “relative-acceleration vector”; and by examining it more closely (Box 11.3), discover the formula

$$
\pmb { \delta } _ { 2 } / ( \varDelta \lambda ) ^ { 2 } ( \varDelta n ) = \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n }
$$

for it.

Box ll.2 illustrates what it means to speak of geodesic deviation. One transports the separation n $\Delta n = \mathfrak { P } \mathfrak { Q } \mathfrak { Q }$ parallel to itself along the fiducial geodesic. The tip of this vector traces out the canonical course that the nearby tracer point would have to pursue if it were to maintain constant separation from the fiducial tracer point. The actual course of the test geodesic deviates from this “canonical’ course. The deviation,a vector ( $\mathcal { Q } \mathcal { P }$ of Box 1l.2), changes with the affine parameter ( ${ \mathcal { Q } } { \mathcal { P } }$ at $\boldsymbol { \mathcal { q } }$ ， 0at $\mathcal { L }$ Bat $\mathcal { B }$ ). The first derivative of this vector with respect to the affine parameter is sensitive to the scale of parameterization along the test geodesic, and to its slope (Box 11.2,F). Not so the second derivative. lt depends only on the tangent vector $\pmb { u }$ of the fiducial geodesic,and on the separation vector $\pmb { n } \pmb { \varDelta n }$ Divide this second derivative of the deviation by $\varDelta n$ and give it a name: the “relative-acceleration vector" Discover (Box 11.3) a simple formula for it

$$
( \mathrm { r e l a t i v e - a c c e l e r a t i o n ~ v e c t o r } ) = \nabla _ { \boldsymbol { u } } \ \nabla _ { \boldsymbol { u } } n .
$$

# $\$ 123$ TIDAL GRAVITATIONAL FORCES AND RIEMANN CURVATURE TENSOR

With“relative acceleration” now defined, turn to the“tidal gravitational force”(i.e., “spacetime curvature") that produces it. Use a Newtonian analysis of tidal forces

# Box 11.3 GEODESIC DEVIATION:ARROW CORRELATED WITH SECOND COVARIANT DERIVATIVE

The arrow $\pmb { \delta } _ { 2 }$ in Box 11.2 measures, not the rate of change of the separation of the test geodesic $n + \Delta n$ from the “canonical course"d2bB as baseline,but the second derivative:

$$
\begin{array} { r l } & { \bigg ( \mathrm { f i r s t ~ d e r i v a t i v e ~ a t ~ } \lambda + \frac { 1 } { 2 } { \varDelta \lambda } \bigg ) = \nabla _ { u } n = \frac { \mathcal { X } \mathcal { Q } - \mathcal { X } \mathcal { Q } } { \varDelta \lambda \varDelta n } = \frac { \mathcal { B } \mathcal { R } } { \varDelta \lambda \varDelta n } ; } \\ & { \bigg ( \mathrm { f i r s t ~ d e r i v a t i v e ~ a t ~ } \lambda - \frac { 1 } { 2 } { \varDelta \lambda } \bigg ) = \nabla _ { u } n = \frac { \mathcal { L } \mathcal { Q } - \mathcal { L } \mathcal { P } } { \varDelta \lambda \varDelta n } = \frac { - \mathcal { Q } \mathcal { P } } { \varDelta \lambda \varDelta n } . } \end{array}
$$

Transpose to common location $\lambda$ ,take difference,and divide it by $\Delta \lambda$ to obtain the second covariant derivative with respect to the vector $\pmb { u }$ ；thus

$$
\begin{array} { l } { \displaystyle \nabla _ { u }  \nabla _ { u } \boldsymbol { n } = \frac { ( \nabla _ { u } \boldsymbol { n } ) _ { \lambda + \frac { 1 } { 2 } } \boldsymbol { \varDelta \lambda } - ( \nabla _ { u } \boldsymbol { n } ) _ { \lambda - \frac { 1 } { 2 } } \boldsymbol { \varDelta \lambda } } { \boldsymbol { \varDelta \lambda } } } \\ { \displaystyle = \frac { ( \mathcal { B R } + \mathcal { A P } ) _ { \mathrm { v e c t o r s t r a n s p o r t e d t o } } } { ( \boldsymbol { \varDelta \lambda } ) ^ { 2 } \boldsymbol { \varDelta n } } = \frac { \delta _ { 2 } } { ( \boldsymbol { \varDelta \lambda } ) ^ { 2 } \boldsymbol { \varDelta n } } } \\ { \displaystyle = \overbrace { \boldsymbol { \cdots } \mathrm { r e l a t i v e \ a c c e l e r a t i o n \ v e c t o r ^ { \prime } } \mathrm { f o r \ n e i g h b o } } ^ { ( \mathcal { A } ) } } \end{array}
$$

(left half of Box 11.4) to motivate the geometric analysis (right half of same box). Thereby arrive at the remarkable equation

$$
\begin{array} { r l r } { \nabla _ { u } \nabla _ { u } \boldsymbol { n } } & { { } + } & { [ \nabla _ { \boldsymbol { n } } , \nabla _ { u } ] \boldsymbol { u } = 0 . } \\ { \mathrm { ~  ~ { \frac ~ { \phi ~ } { \varepsilon ~ } } ~ } } & { { } \Gamma ^ { \prime } \quad \mathrm { e l a t i v e } \quad } & { \Gamma ^ { \prime } \quad \mathrm { e " ~ t i d e \mathrm { - } p r o d u c i n g } } \\ { \mathrm { ~  ~ { \frac ~ { \phi ~ } { \varepsilon ~ } } ~ } } & { { } \mathrm { g r a v i t a t i o n a l ~ f o r c e s " ~ } , } \end{array}
$$

Tide-producing gravitational forces expressed in terms of a commutator

This equation is remarkable, because at first sight it seems crazy. The term $[ \pmb { \bigtriangledown _ { n } } , \pmb { \bigtriangledown _ { u } } ] \pmb { u }$ involves second derivatives of $\pmb { u }$ ,and a first derivative of $\forall _ { \pmb { n } }$ ：

$$
[ \pmb { \nabla } _ { n } , \pmb { \nabla } _ { u } ] \pmb { u } \equiv \pmb { \nabla } _ { n } \pmb { \nabla } _ { u } \pmb { u } - \pmb { \nabla } _ { u } \ \pmb { \nabla } _ { n } \pmb { u } .
$$

It thus must depend on how $\pmb { u }$ and $\pmb { n }$ vary from point to point. But the relative acceleration it produces, $\yen 1$ is known to depend only on the values of $\pmb { u }$ and $\pmb { n }$ at the fiducial point,not on how $\pmb { u }$ and $\pmb { n }$ vary (see Box 11.2, F). How is this possible?

Somehow all derivatives must drop out of the tidal-force quantity $[ \pmb { \nabla } _ { \pmb { n } } , \pmb { \nabla } _ { \pmb { u } } ] \pmb { u } .$ One must be able to regard $[ \pmb { \nabla } _ { \dots } , \pmb { \nabla } _ { \dots } ] \ldots \pmb { \mathrm { a s } }$ a purely local, algebraic machine with three slots,whose output is a vector. If it is purely local and not differential, then it is even linear (as one sees from the additivity properties of $\blacktriangledown$ ), so it must be a tensor. Give this tensor the name Riemann,and give it a fourth slot for inputing a 1-form:

$$
R i e m a n n \ ( . . . , c , A , B ) \equiv [ \Psi _ { A } , \Psi _ { B } ] C ;
$$

This is only a tentative definition of Riemann.Before accepting it, one should verify that it is, indeed,a tensor. Does it really depend on only the values of $\pmb { A }$ ， B, C at the point of evaluation,and not on how they are changing there? The answer (derived in Box l1.5) is “almost.”It fails the test, but with a slight modification it will pass.The modification is to replace the commutator $[ \pmb { \bigtriangledown _ { A } } , \pmb { \bigtriangledown _ { B } } ]$ by the"curvature operator"

Curvature operator defined

$$
\begin{array} { r } { \mathcal { R } ( A , B ) \equiv [ \nabla _ { A } , \nabla _ { B } ] - \nabla _ { [ A , B ] } , } \end{array}
$$

where $\yen 123$ is the derivative along the vector $[ A , B ]$ (commutator of $\pmb { A }$ and $\pmb { B }$ ) $( \mathcal { R } ( A , B ) \equiv [ \nabla _ { A } , \nabla _ { B } ]$ for the fields ${ \pmb A } = { \pmb n }$ and $\pmb { \cal B } = \pmb { \mu }$ of the geodesic-deviation problem, because $[ { \pmb n } , { \pmb u } ] = 0 .$ ） Then the modified and acceptable definition of the Riemann curvature tensor is

Riemann curvature tensor defined

$$
\begin{array} { r l } & { R i e m a n n \left( \ldots , \pmb { C } , \pmb { A } , \pmb { B } \right) \equiv \langle \pmb { \mathcal { A } } ( \pmb { A } , \pmb { B } ) \pmb { C } ; } \\ & { R i e m a n n \left( \sigma , \pmb { C } , \pmb { A } , \pmb { B } \right) \equiv \langle \pmb { \sigma } , \acute { \mathcal { A } } ( \pmb { A } , \pmb { B } ) \pmb { C } , } \end{array}
$$

To define Riemann thus,and to verify its tensorial character (exercise l1.2), does not by any means teach one what curvature is all about. To understand curvature, one must scrutinize Riemann from all viewpoints. That is the task of the rest of this chapter.

# Box 11.4 RELATIVE ACCELERATION OF_TEST PARTICLES一 GEOMETRIC ANALYSIS PATTERNED ON NEWTONIAN ANALYSIS

# Newtonian Analysis

# Geometric Analysis

1. Consider a family of test-particle trajectories $x ^ { j } ( t , n )$ in ordinary,three-dimensional space: $" t "$ is time measured by particle's clock, or any clock; $" n '$ is “selector parameter.”

1. Consider a family of test-particle trajectories (geodesics), ${ \mathcal { P } } ( \lambda , n )$ ,in spacetime: $^ { \mathfrak { s } } \lambda ^ { \mathfrak { s } }$ is affineparameter, i.e.， time measured by particle's clock; $" n "$ is “selector parameter.”

![](images/0f3187734a3f75b90bdf2e341aeb2b0a52d5f8cc59e0fed3c9ce7989da177eab.jpg)

![](images/4dd6460014c2577948e3a84f7b942be8b7d6e9601be5d16176b0de2c0255935f.jpg)

2. Equation of motion for each trajectory:

$$
\left( \frac { \partial ^ { 2 } x ^ { j } } { \partial t ^ { 2 } } \right) _ { n } + \frac { \partial \bar { \phi } } { \partial x ^ { j } } = 0 ,
$$

where $\pmb { \phi }$ is Newtonian potential.

2. Geodesic equation for each trajectory:

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 .
$$

[Looks like first-order equation； is actually second-order because the $\bullet \bullet \bullet$ being differentiated is itself a derivative, $\pmb { u } = ( \hat { \partial } \pmb { \mathcal { P } } _ { \mathrm { \prime } } / \hat { \partial } \lambda ) _ { n } . ]$

3. Take difference between equations of motion for neighboring trajectories, $\pmb { n }$ and $n + 4 n$ and take limit as $\varDelta n \longrightarrow 0$ -i.e.,take derivative

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } \left[ \left( \frac { \partial ^ { 2 } x ^ { j } } { \partial t ^ { 2 } } \right) _ { n } + \frac { \partial \phi } { \partial x ^ { j } } \right] = 0 . } \end{array}
$$

3.Take difference between geodesic equations for neighboring geodesics $\pmb { n }$ and $n + 4 n ,$ and take limit as $\varDelta n \longrightarrow 0$ -ie.,take covariant derivative

$$
\pmb { \nabla } _ { \pmb { n } } \left[ \pmb { \nabla } _ { \pmb { u } } \pmb { u } \right] = 0 .
$$

4. When $\hat { \partial } / \hat { \partial } n$ acts on second term, rewrite it as

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } = \left( \frac { \partial x ^ { k } } { \partial n } \right) _ { t } \frac { \partial } { \partial x ^ { k } } = n ^ { k } \frac { \partial } { \partial x ^ { k } } ; } \end{array}
$$

Thereby obtain

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial x ^ { j } } { \partial t } \right) _ { n } + \frac { \partial ^ { 2 } \varPhi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0 . } \end{array}
$$

4. There is no second term, so leave equation in form

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { n } } \left[ \pmb { \nabla } _ { \pmb { u } } \pmb { u } \right] = 0 . } \end{array}
$$

5. To obtain equation for relative acceleration, move $( \partial / \partial n ) _ { t }$ through both of the $\left( \partial / \partial t \right) _ { n }$ terms (permissible because partial derivatives commute!):

$$
\begin{array} { r } { \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial x ^ { j } } { \partial n } \right) _ { t } + \frac { \partial ^ { 2 } \varPhi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0 . } \end{array}
$$

This is equivalent to

（2n） 22 +xxn =0.   
[relative ttide-producing   
acceleration"] gravitational forces"]

5. To obtain equation for relative acceleration, $\yen 1$ move $\forall _ { \pmb { n } }$ through $\pmb { \tau } _ { \pmb { u } }$ and through the $\partial / \partial \lambda$ of $\pmb { \upsilon } = \partial \mathcal { P } / \partial \lambda$ ：

a. First step: In $\begin{array} { r } { \pmb { \nabla _ { n } } \pmb { \nabla _ { u } } \pmb { u } = 0 } \end{array}$ ,move $\forall _ { \pmb { n } }$ through $\pmb { \check { \nu } _ { \pmb { \ u } } }$ . The result:

$( \nabla _ { u } \ : \nabla _ { \boldsymbol { n } } + \underbrace { [ \ : \nabla _ { \boldsymbol { n } } , \ : \nabla _ { \boldsymbol { u } } ] } _ { \displaystyle \dot { \uparrow } } ) \boldsymbol { u } = 0 .$ commutator;must be included as protection against possibility that $\pmb { \nabla _ { u } } \pmb { \nabla _ { n } } \neq \pmb { \nabla _ { n } } \pmb { \nabla _ { u } }$

b. Second step: Move $\forall _ { \pmb { n } }$ through $\partial / \partial \lambda$ of $\pmb { \upsilon } = \partial \mathcal { P } / \partial \lambda$ ; i.e., write

$$
\begin{array} { r } { = \left[ \frac { \partial } { \partial n } , \frac { \partial } { \partial \lambda } \right] = \frac { \partial ^ { 2 } } { \partial n \partial \lambda } - \frac { \partial ^ { 2 } } { \partial \lambda \partial n } = 0 . } \end{array}
$$

c. Result:

uVun +[mu]u = 0   
"relative "tide-producing   
acceleration" gravitational forces"; i.e..“spacetime curvature”

Box 11.5 RIEMANN CURVATURE TENSOR

# A. Definition of Riemann Motivated by Tidal Gravitational Forces:

1. Tidal forces (spacetime curvature) produce relative acceleration of test particles (geodesics） given by

$$
\begin{array} { r } { \nabla _ { u } \nabla _ { u } \pmb { n } + [ \pmb { \nabla } _ { n } , \pmb { \nabla } _ { u } ] \pmb { u } = 0 . } \end{array}
$$

# Box 11.5 (continued)

2. This motivates the definition

$$
\begin{array} { r } { R i e m a n n \left( . \vphantom { \frac { b } { b } } \mathrm { ~ \frac ~ { \ p ~ { \frac { b } { b } } ~ { \frac { b } { b } } ~ { \frac { c } { d } } } ~ } , \pmb { c } , \pmb { A } , \pmb { B } \right) = [ \pmb { \nabla } _ { A } , \pmb { \nabla } _ { B } ] \pmb { C } . } \\ { \mathrm { \frac { 1 } { \ l e m p t y ~ s l o t ~ f o r ~ i n s e r t i n g } } } \end{array}
$$

# B. Failure of this Definition

1. Definition acceptable only if Riemann $( \ldots , \pmb { C } , \pmb { A } , \pmb { B } )$ is a linear machine, independent of how A, B, $\pmb { c }$ vary from point to point.

2. Check, in part: change variations of $\pmb { c }$ but not $\pmb { c }$ itself, at event $\mathcal { P } _ { \mathbf { 0 } }$

$$
\begin{array} { r } { \pmb { C } _ { \mathrm { N E W } } ( \mathcal { P } ) = f ( \mathcal { P } ) \pmb { C } _ { \mathrm { o L D } } ( \mathcal { P } ) . } \\ { \qquad \quad \vdots _ { [ \mathrm { a r b i t r a r y f u } } } \end{array}
$$

3. Does this change $[ \pmb { \nabla } _ { \pmb { A } } , \pmb { \nabla } _ { \pmb { B } } ] \pmb { C } ?$ Yes！ Exercise 11.1 shows

$$
\{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { N E W } } \} _ { \mathrm { a t } \mathcal { P } _ { 0 } } - \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { O L D } } \} _ { \mathcal { P } _ { 0 } } = C _ { \mathrm { O L D } } \nabla _ { [ A , B ] } f .
$$

# C. Modified Definition of Riemann:

1. The term causing trouble, $\pmb { c } _ { \mathrm { o L D } } \pmb { \bigtriangledown } _ { [ \pmb { A } , \pmb { B } ] } f ,$ can be disposed of by subtracting a “correction term” resembling it from Riemann-i.e.,by redefining

$$
\begin{array} { r } { R i e m a n n \left( \ldots , \ldots , { \pmb { C } } , { \pmb { A } } , { \pmb { B } } \right) \equiv \mathcal { R } ( { \pmb { A } } , { \pmb { B } } ) { \pmb { C } } , \qquad } \\ { \mathcal { R } ( { \pmb { A } } , { \pmb { B } } ) \equiv [ \pmb { \nabla } _ { \pmb { A } } , \pmb { \nabla } _ { \pmb { B } } ] - \pmb { \nabla } } \end{array}
$$

2. The above calculation then gives a result independent of the“modifying function” $f$

$$
\{ { \mathcal { R } } ( A , B ) C _ { \mathrm { N E W } } \} _ { \mathrm { a t } { \boldsymbol { \varphi } } _ { 0 } } = \{ { \mathcal { R } } ( A , B ) C _ { \mathrm { 0 L D } } \} _ { \mathrm { a t } { \boldsymbol { \varphi } } _ { 0 } } .
$$

# D. Is Modified Definition Compatible with Equation for Tidal Gravitational Forces?

2. This works just as well for modified definition of Riemann as for original definition, because

$$
\begin{array} { r } { \begin{array} { r } { \boldsymbol { \mathcal { R } } ( n , { \boldsymbol { u } } ) = [ \boldsymbol { \nabla } _ { n } , \boldsymbol { \nabla } _ { \boldsymbol { u } } ] - \boldsymbol { \nabla } _ { [ n , { \boldsymbol { u } } ] } = [ \boldsymbol { \nabla } _ { n } , \boldsymbol { \nabla } _ { \boldsymbol { u } } ] . } \\ { \qquad \quad \vdots \qquad \displaystyle { \mathrm { ~ L } } \int _ { \boldsymbol { u } } = 0 \mathrm { ~ b e c a u s e ~ } n = ( \partial / \partial n ) _ { \boldsymbol { \lambda } } \mathrm { ~ a n d } \Bigg ] } \end{array} } \\ { \boldsymbol { \nabla } _ { \boldsymbol { u } } = ( \partial / \partial \lambda ) _ { n } \mathrm { ~ c o m m u t e } \qquad } \end{array}
$$

Geodesic deviation and tidal forces cannot tell the difference between $\mathcal { R } ( \pmb { n } , \pmb { u } )$ and $[ \pmb { \nabla } _ { \pmb { n } } , \pmb { \nabla } _ { \pmb { u } } ] _ { : }$ ，nor consequently between old and new definitions of Riemann.

# E. Is Modified Definition Acceptable?

I.e., is Riemann $( \ldots , \pmb { c } , \pmb { A } , \pmb { B } ) \equiv \Re ( \pmb { A } , \pmb { B } ) \pmb { C }$ a linear machine with output independent of how $\pmb { A }$ ,B, $\pmb { c }$ vary near point of evaluation? YES! (See exercise l1.2.)

Take stock, first, of what one knows already about the Riemann curvature tensor. (l) Riemann is a tensor; despite the appearance of $\blacktriangledown$ in its definition (11.9), no derivatives actually act on the input vectors $\mathbf { A } , \mathbf { B } ,$ ,and C.(2) Riemann is a $\textstyle { { \binom { 1 } { 3 } } }$ tensor; its first slot accepts a l-form; the others, vectors. (3) Riemann is determined entirely by $\blacktriangledown$ ,or equivalently by the geodesics of spacetime,or equivalently by spacetime's parallel transport law; nothing but $\blacktriangledown$ and the input vectors and l-form are required to fix Riemann's output. (4) Riemann produces the tidal gravitational forces that pry geodesics (test-particle trajectories) apart or push them together; i.e., it characterizes the “curvature of spacetime":

Tide-producing gravitational forces expressed in terms of Riemann

$$
\nabla _ { u } \ : \nabla _ { u } n + R i e m a n n \ : ( . . . , u , n , u ) = 0 .
$$

(This “equation of geodesic deviation” follows from equations 11.6, 11.8, and l1.9, and the relation $[ { \pmb n } , { \pmb u } ] = 0$ ）

All tese facets of Riemann are pictorial (e.g., geodesic deviation; see Boxes 11.2 and ll.3) or abstract (e.g.,equations l1.8 and l1.9 for Riemann in terms of $\blacktriangledown$ ) Riemann's component facet,

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } \equiv R i e m a n n ~ ( \omega ^ { \alpha } , e _ { \beta } , e _ { \gamma } , e _ { \delta } ) \equiv \langle \omega ^ { \alpha } , \mathcal { R } ( e _ { \gamma } , e _ { \delta } ) e _ { \beta } \rangle , ~ .
$$

Components of Riemann expressed in terms of connection coefficients

is related to the component facet of $\blacktriangledown$ by the following equation, valid in any coordinate basis $\{ { \pmb e } _ { \alpha } \} = \left\{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \right\}$ ：

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } = { \frac { \partial { \cal { T } } ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } } - { \frac { \partial { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } } + { \cal { T } } ^ { \alpha } { } _ { \mu \gamma } { \cal { T } } ^ { \mu } { } _ { \beta \delta } - { \cal { T } } ^ { \alpha } { } _ { \mu \delta } { \cal { T } } ^ { \mu } { } _ { \beta \gamma } .
$$

(See exercise l1.3 for derivation,and exercise l1.4 for the extension to noncoordinate bases.） These components of Riemann,with no sign of any derivative operator anywhere, may leave one with a better feeling in one's stomach than the definition (l1.8)with its nondifferentiating derivatives!

Exercise 11.1. $[ \nabla _ { A } , \nabla _ { B } ] c$ DEPENDS ON DERIVATIVES OF $\pmb { c }$ (Based on Box 11.5.） Let $\pmb { c } _ { \mathrm { x E W } }$ and $\pmb { c } _ { \mathrm { o } \mathbf { L } \mathbf { D } }$ be vector fields related by

$$
\begin{array} { r } { \pmb { c } _ { \mathrm { N E W } } ( \mathcal { G } ) = f ( \mathcal { G } ) \pmb { c } _ { \mathrm { o L D } } ( \mathcal { G } ) . } \\ { \qquad \quad \mathrm { L } _ { \mathrm { l a r b i t r a r y } } } \end{array}
$$

Show that

$$
\begin{array} { r } { \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { N E W } } \} _ { \mathrm { a t } } \varphi _ { \mathrm { _ 0 } } - \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { O L D } } \} _ { \mathrm { a t } } \varphi _ { \mathrm { _ 0 } } = C _ { \mathrm { O L D } } \Psi _ { [ A , B ] } f . } \end{array}
$$

Exercise 11.2. PROOF THAT Riemann IS A TENSOR

Show from its definition (l1.8,11.9) that Riemann is a tensor. Hint: Use the following procedure.

(a)If $f ( \mathcal { P } )$ is an arbitrary function, show that

$$
{ \mathcal { R } } ( A , B ) f C = f { \mathcal { R } } ( A , B ) c .
$$

(b） Similarly show that

$$
{ \mathfrak { A } } \left( f { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } = f { \ o { \forall } { \hbar } } \left( { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } \qquad { \mathrm { a n d } } \qquad { \ o { \forall } { \hbar } } \left( { \pmb { A } } , f { \pmb { B } } \right) { \pmb { C } } = f { \ o { \forall } { \hbar } } \left( { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } ,
$$

(c) Show that ${ \mathcal { R } } ( \pmb { A } , \pmb { B } ) \pmb { c }$ is linear; i.e.,

$$
\begin{array} { r l } & { \Re ( \pmb { A } + \pmb { a } , \pmb { B } ) \pmb { C } = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { A } ( \pmb { a } , \pmb { B } ) \pmb { C } ; } \\ & { } \\ & { \mathcal { R } ( \pmb { A } , \pmb { B } + \pmb { b } ) \pmb { C } = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { A } ( \pmb { A } , \pmb { b } ) \pmb { C } ; } \\ & { \mathcal { R } ( \pmb { A } , \pmb { B } ) ( \pmb { C } + \pmb { c } ) = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { R } ( \pmb { A } , \pmb { B } ) \pmb { c } , } \end{array}
$$

(d) Now use the above properties to prove the most crucial feature of ${ \mathcal { R } } ( { \pmb A } , { \pmb B } ) { \pmb c }$ Modify the variations (gradients) of A. $\pmb { B }$ ,and $\pmb { c }$ in an arbitrary manner, but leave $\pmb { A } , \pmb { B } , \pmb { C }$ unchanged at ${ \mathcal { P } } _ { 0 }$

$$
\left. \begin{array} { l } { { { \pmb { A } } \longrightarrow { \pmb { A } } + a ^ { \alpha } { \pmb { e } } _ { \alpha } } } \\ { { { \pmb { B } } \longrightarrow { \pmb { B } } + b ^ { \alpha } { \pmb { e } } _ { \alpha } } } \\ { { { \pmb { C } } \longrightarrow { \pmb { C } } + c ^ { \alpha } { \pmb { e } } _ { \alpha } } } \end{array} \right. \qquad \} \begin{array} { l } { { a ^ { \alpha } ( { \mathcal { P } } ) , b ^ { \alpha } ( { \mathcal { P } } ) , c ^ { \alpha } ( { \mathcal { P } } ) \mathrm { a r b i t r a r y \ e x c e p t } } } \\ { { \mathrm { t h e y \ a l l \ v a n i s h \ a t \mathcal { S } } = { \mathcal { P } } _ { 0 } , } } \end{array}
$$

Show that this modification leaves ${ \mathcal { R } } ( \pmb { A } , \pmb { B } ) \pmb { c }$ unchanged at $\mathcal { P } _ { 0 } .$

(e)From these facts,conclude that Riemann is a tensor.

# Exercise 11.3. COMPONENTS OF Riemann IN COORDINATE BASIS

Derive equation (l1.12) for the components of the Riemann tensor in a coordinate basis. [Solution:

$$
\begin{array} { r l r l } & { R ^ { \alpha } { } _ { \beta \gamma \delta } = R i e m a n n ~ ( \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \beta } , \boldsymbol { e } _ { \gamma } , \boldsymbol { e } _ { \delta } ) } & & { \Big [ \mathrm { s t a n d a r d ~ w a y ~ t o } } \\ & { } & & { \Big [ \mathrm { c a l c u l a t e ~ c o m p o n e n t s } \Big ] } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { \mathcal { R } } ( \boldsymbol { e } _ { \gamma } , \boldsymbol { e } _ { \delta } ) \boldsymbol { e } _ { \beta } \rangle } & & { [ \mathrm { b y ~ d e f i n i t i o n ~ ( 1 1 . 9 ) } ] } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , ( \boldsymbol { \Psi } _ { \gamma } \boldsymbol { \Psi } _ { \delta } - \boldsymbol { \Psi } _ { \delta } \boldsymbol { \Psi } _ { \gamma } ) \boldsymbol { e } _ { \beta } \rangle } & & { \Big [ \mathrm { b y ~ d e f i n i t i o n ~ ( 1 1 . 8 ) ~ p l u s } } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \mu } \boldsymbol { T } ^ { \mu } { } _ { \beta \delta , \gamma } + ( \boldsymbol { e } _ { \nu } \boldsymbol { T } ^ { \nu } { } _ { \mu \gamma } ) \boldsymbol { T } ^ { \mu } { } _ { \beta \delta } - \boldsymbol { e } _ { \mu } \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma , \delta } - ( \boldsymbol { e } _ { \nu } \boldsymbol { T } ^ { \nu } { } _ { \mu \delta } ) \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma } \rangle } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , { } \boldsymbol { \theta } _ { \beta } \gamma - \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma , \delta } \rangle \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \mu } \rangle + ( \boldsymbol { T } ^ { \nu } { } _ { \mu \gamma } { \cal T } ^ { \mu } { } _ { \beta \delta } - \boldsymbol { T } ^ { \nu } { } _ { \mu \delta } \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma } ) \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \nu } \rangle , } \end{array}
$$

# Exercise 11.4. COMPONENTS OF RIEMANN IN NONCOORDINATE BASIS

In a noncoordinate basis with commutation coeffcients $c _ { \alpha \beta } { } ^ { \gamma }$ defined by equation (9.22),derive the following equation for the components of Riemann:

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } = { \Gamma ^ { \alpha } } _ { \beta \delta , \gamma } - { \Gamma ^ { \alpha } } _ { \beta \gamma , \delta } + { \Gamma ^ { \alpha } } _ { \mu \gamma } { { r ^ { \mu } } _ { \beta \delta } } - { \Gamma ^ { \alpha } } _ { \mu \delta } { { r ^ { \mu } } _ { \beta \gamma } } - { \Gamma ^ { \alpha } } _ { \beta \mu } { { c } _ { \gamma \delta } } ^ { \mu } .
$$

# $\$ 123$ ．PARALLEL TRANSPORT AROUND A CLOSED CURVE

What are the effects of spacetime curvature,and how can one quantify them? One effect is geodesic deviation (relative acceleration of test bodies), quantified by equation (ll.lO). Another effect, almost as important, is the change in a vector caused by parallel transport around a closed curve. This effect shows up most clearly in the same problem,geodesic deviation, that motivated curvature in the first place. The relative acceleration vector $\blacktriangledown _ { \pmb { u } } \ \pmb { \nabla } _ { \pmb { u } } \pmb { n }$ is also the change $\delta \pmb { u }$ in the vector u caused by parallel transport around the curve whose legs are the vectors $\pmb { n }$ and $\pmb { u }$ ：

Change in a vector due to parallel transport around a closed curve:

Related to geodesic deviation

$$
\begin{array} { r } { \pmb { \nabla _ { u } } \pmb { \nabla _ { u } } \pmb { n } = \delta \pmb { u } . } \end{array}
$$

(See Box l1.6 for proof.) Hence, in this special case one can write

$$
\delta \pmb { u } + R i e m a n n \left( . . . , \pmb { u } , \pmb { n } , \pmb { u } \right) = 0 .
$$

The expected generalization is obvious: pick a closed quadrilateral with legs u Aa and $\pmb { v } \pmb { \varDelta } b$ (Figure 11.2; $\pmb { \varDelta } a$ and $_ { \pmb { \varDelta b } }$ are small parameters,to go to zero at end of discussion). Parallel transport the vector $\pmb { A }$ around this quadrilateral. The resultant change in $\pmb { A }$ should satisfy the equation

$$
\delta { \pmb A } + R i e m a n { \pmb n } \left( . . . , { \pmb A } , { \pmb u } \Delta a , { \pmb v } \Delta b \right) = 0 ;
$$

Equation for change

or, equivalently,

$$
\delta { \pmb A } + 4 a \Delta b \mathcal { R } ( { \pmb u } , { \pmb v } ) { \pmb A } = 0 ;
$$

or, more precisely,

$$
\operatorname * { L i m } _ { 4 a  0 } ( { \frac { \delta A } { \varDelta a \ \varDelta b } } ) + R i e m a n n ( . . . , A , u , v ) = 0 .
$$

The proof is enlightening, for it reveals the geometric origin of the correction term $\yen 1$ in the curvature operator.

The circuit of transport (Figure l1.2) is to be made from two arbitrary vector fields u Aa and ${ \pmb v } \pmb { \varDelta b }$ .However,a circuit made only of these felds has a gap in it, for a simple reason. The magnitude of $\pmb { u }$ varies the wrong way from place to place. The displacement u $\pmb { \varDelta } \boldsymbol { a }$ that reaches.across at the bottom of the quadrilateral from

Derivation of equation for change

![](images/c8a24f87b098810e6c765271133a96ea4ae43879b31af243bd2c211e782a1f60.jpg)  
Figure 11.2. The change $\delta \pmb { A }$ in a vector $\pmb { A }$ as a result of parallel transport around a closed curve. The edges of the curve are the vector fields u $\pmb { \varDelta } a$ and $\pmb { v } \pmb { \mathcal { A } b }$ plus the“closer of the quadrilateral" $\{ v \ \varDelta b , \pmb { u } \ \varDelta a \} = \{ \pmb { v } ,$ u $\pmb { \varDelta a }$ $^ { \varDelta b }$ (see Box 9.2),

one line of v's to another cannot make the connection at the top of the quadrilateral. Similarly the v's vary the wrong way from place to place to connect the u's. To close the gap and complete the circuit, insert the “closer of quadrilaterals” $[ v \varDelta b$ ， $\pmb { \mathscr { u } } \Delta a ] = [ \pmb { v } , \pmb { u } ] \Delta a \Delta b$ (See Box 9.2 for why this vector closes the gap.)

With the route now specified, the vector $\pmb { A }$ is to be transported around it. One way to do this,“geometrical construction”by the method of Schild's ladder applied Over and over, is the foundation for planning a possible experiment. For planning an abstract and coordinate-free calculation (the present line of action), introduce a “fiducial field,” only to take it away at the end of the calculation. Plan: Conceive of $\pmb { A }$ , not as a localized vector defined solely at the start of the trip,but as a vector field (defined throughout the trip). Purpose: To provide a standard of reference (comparison of A transported from the origin with A at the place in question). Principle: The standard of reference will cancel out in the end. Procedure:

/Net change made in taking the vector A, originally localized at the start of the circuit,and transporting it parallel to itself ("mobile A") -8A= 1 around the closed circuit. This quantity cannot be evaluated until completion of circuit because there is no preexisting standard of (reference along the way. /A quantity subject to analysis for each leg of circuit individually. This new quantity is defined by introducing throughout the whole region a vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ ， smoothly varying, and in agreement at starting =+ point with the original localized A, but otherwise arbitrary. This new quantity is then given by $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ at starting point (same as Alocalized) at starting point) minus $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ at finish point (after transit). /Change in Afid relative to $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ in the course of transport along

$$
\begin{array} { r l } & { \int \mathrm { ( R a n g e ~ i n ~ \mathbb { A } ^ { ( t e i d e ) } ~ r e l a t i v e ~ t o ~ t h e ~ p a r a l e l ) d i - t r a n s p o r t e d ~ \mathbb { A } ^ { ( m o b i n g ) } } , } \\ &  = \left( \begin{array} { l l } { \mathrm { o f ~ r e f i r e r n c e } , } & { \mathrm { ~ o f ~ e ~ o n ~ \mathbb { A } \in ~ \mathbb { B } ^ { \nu } ~ o f ~ t o ~ m a t i o n s ~ a l o n g ~ f o l l o w i n g ~ l e g } , } \\ { 1 \cdot 2 : } & { \mathrm { ~ i s ~ p o r s i n g ~ \mathbb { P } _ { \times } ^ { \nu } \mathbb { A } ^ { ( t i e n d ) } ~ \mathbb { A } ^ { \nu } ( \mathrm { o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / \mathrm { a v e l } } \mathrm { a d ~ \mathbb { A } ^ { \nu } ~ f r o r } } \\ { \quad \nu \ \mathbb { A } , } & { \mathrm { g i v i n i n g ~ \mathbb { P } _ { \times } \mathbb { A } ^ { ( t i e n d ) } } \ \Delta b \ \mathrm { ( ~ o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / a e d ~ \mathbb { A } ^ { \nu } ~ f r o r } } \\ { - \mu \ \lambda \mu _ { \nu } \mathrm { g i v i n g } - } & { \nabla _ { \times } A ^ { ( t i e n d ) } \ \mathcal { A } b \ \mathrm { ( o n ~ 1 i n e ~ t i r o u g h ~ s t a r t i n g ~ p o l ) } } \\ { - \mu \ \lambda \mu _ { \nu } \mathrm { i n i n g } - } & { \nabla _ { \times } A ^ { ( t i e n d ) } \ \mathcal { A } a \ \mathrm { ( o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / a c d } \nu \mathrm { ~ f o r ~ a } b } \end{array} \right. } \\ & { \quad \quad + u \ L _ { 0 } \mathrm { i d } \ \mathrm { B i n g ~ \mathbb { P } } _ { \times } } \\ & { \quad \quad + \left\{ \nu , u \right\} \Delta a \ L _ { 0 } \mathrm { i v i n g ~ \mathbb { P } } _ { \times } \ \mathrm { f i r e a l ~ \Delta a l ~ \delta a \ L e ~ ( o n ~ i n e ~ \mathbb { A } ^ { \nu } ~ s t a r t i n g ~ p o l ~ \pi ~ } ) } \\ & { = \left\{ \nabla _ { \nu } \nabla _ { \nu } - \nabla _ { \nu } \nabla _ { \nu } + \nabla _ { \nu \times 1 } \right\} \ \mathrm { A } ^ { ( t i e n d ) } \ \mathcal { A } a \mathcal { A } b } \\ &  = R i f \mathrm { n } \mu _ { \nu }  \end{array}
$$

Profit: The curvature operator

$$
\ R i e m a n n \left( \ldots , \ldots , \ldots , \pmb { u } , \pmb { v } \right) = \mathcal { R } ( \pmb { u } , \pmb { v } ) = [ \pmb { \nabla } _ { \pmb { u } } , \pmb { \nabla } _ { \pmb { v } } ] - \pmb { \nabla } _ { [ \pmb { u } , \pmb { v } ] } ,
$$

# Box 11.6 GEODESIC DEVIATION AND PARALLEL TRANSPORT AROUNDCLOSED CURVE: TWO ASPECTS OF SAME CONSTRUCTION

Geodesic Deviation

$$
\nabla _ { u } \nabla _ { u } n = \operatorname { L i m } _ { \stackrel { \scriptstyle \ A \lambda  0 } { \scriptstyle \ A n  0 } } \{ \frac { \displaystyle \mathcal { Q } \mathcal { P } + \mathit { \mathcal Q B } \mathcal { Q } } { \displaystyle ( \Delta \lambda ) ^ { 2 } \Delta n } \} .
$$

(See Boxes 11.2 and 11.3)

![](images/55554b111b50372aae71fb3b2eea2510fbfc48aae05ab533c41c490aaf440e02.jpg)

![](images/3ada0a3aac7462f95c3b58da9a508a9d46d9fdcfc4902c2f572be0da00a74739.jpg)

# Geodesic Deviation

Same result; different construction. To simplify the connection with closed-curve transport, change the tilt and dilate the parametrization of geodesic $\mathcal { S } \mathcal { Q } \mathcal { R }$ in A. The result: B,where $\overrightarrow { \mathcal { S } }$ and $\mathcal { Q }$ coincide. From F of Box l1.2 one knows $\tilde { a } \tilde { \cdot } \tilde { \mathcal { P } } +$ $\begin{array} { r } { { \mathfrak { A } } _ { \mathfrak { L } } ^ { \gamma } { \mathfrak { R } } = { \mathfrak { a } } ^ { \overline { { \mathcal { P } } } } + { \mathfrak { B } } { \overline { { \mathcal { R } } } } . } \end{array}$ -i.e. $\yen 123,456$ isthe same for this family of geodesics as for the original family

$$
\nabla _ { \boldsymbol { u } } \nabla _ { \boldsymbol { u } } \boldsymbol { n } = \operatorname * { L i m } _ { \stackrel { \mathrm { 4 \lambda  0 } } { \mathrm { 4 \lambda  0 } } } \{ \frac { \langle \boldsymbol { \mathcal { B } } \boldsymbol { \overbar { \mathcal { B } } } } { ( \Delta \lambda ) ^ { 2 } } \} .
$$

Also,to simplify discussion set $\varDelta n = \varDelta \lambda = 1$ ,and assume $\pmb { n }$ and $\pmb { u }$ are small enough that one can evaluate $\yen 1$ without taking the limit:

$$
\begin{array} { r } { \nabla _ { u } \ : \nabla _ { u } { n } = \langle \mathcal { B } \overline { { \mathcal { R } } } . } \end{array}
$$

# Parallel Transport Around Closed Curve, Performed by Same Construction

Plan: Parallel transport the vector u $\begin{array} { r } { \mathbf { \nabla } \cdot \mathbf { \delta } \varDelta \lambda = \mathcal { Q } \overline { { \mathcal { R } } } } \end{array}$ counterclockwise around the curve $2 \longrightarrow \bar { \varphi } \longrightarrow \mathcal { E } \stackrel { \cdot } { \longrightarrow } \mathcal { R } \longrightarrow \mathcal { Q } .$ Execution: (1) Call transported vector ${ \pmb u } ^ { ( \mathbf { m } ) } \ ( ^ { * } { \mathbf { m } ^ { \prime } }$ for “mobile"). (2) At $\mathcal { L }$ ， $\pmb { \upsilon } ^ { ( \mathbf { m } ) } = \mathcal { Q } \overline { { \mathcal { R } } }$ . (3)At $\bar { \mathcal P }$ ， $\pmb { \mu } ^ { ( \mathbf { m } ) } = \mathcal { \bar { P } } \mathcal { Q }$ because $\boldsymbol { \overline { { \mathcal { P } } } } \boldsymbol { \mathcal { Q } } \boldsymbol { \overline { { \mathcal { R } } } }$ is a geodesic and $\pmb { \mu } ^ { ( \mathbf { m } ) }$ is its tangent vector. (4) At $\mathcal { L }$ ， $\pmb { \mathscr { u } } ^ { ( \mathbf { m } ) } = \mathscr { L } \mathcal { D } \mathscr { R }$ according to Schild's ladder of the picture. (5) At $\mathfrak { R }$ ， $\pmb { u } ^ { ( \mathbf { m } ) } = \mathcal { R } \mathcal { R }$ because $\mathcal { L } \mathcal { D } \mathcal { R } \mathcal { R }$ is a geodesic and $\pmb { \mu } ^ { ( \mathbf { m } ) }$ is now its tangent vector. (6) At $\mathcal { L }$ ， $\pmb { \nu } ^ { ( \mathbf { m } ) } = \mathcal { Q } \mathcal { G } \beta$ according to Schild's ladder. Result: The change in ${ \pmb u } ^ { ( \mathbf { m } ) }$ is $- \mathcal { B } \overline { { \mathcal { R } } }$ .Had the curve been circuited in opposite direction $\mathcal { L } \longrightarrow \overline { { \mathcal { P } } } \stackrel { } { \longrightarrow }$ ${ \mathcal { Q } } \longrightarrow { \mathcal { R } } \longrightarrow { \mathcal { L } } )$ ， the change would have been $+ \sqrt [ 6 ] { 3 } \sqrt { 2 }$ ：

applied to the vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ ， gives the negative of the change in the localized vector A localized (called $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ during the phase of travel) on paralel transport around the closed circuit. It does not give the change in $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ on traversal of that circuit, for $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ has the same value at the end of the journey as at the beginning. Equation (l1.14'） expresses that change in terms of the conveniently calculated differential operator, $\boldsymbol { \mathcal { R } } ( \boldsymbol { u } , \boldsymbol { v } ) = [ \nabla _ { \boldsymbol { u } } , \nabla _ { \boldsymbol { v } } ] - \nabla _ { [ \boldsymbol { u } , \boldsymbol { v } ] }$ Paradox: Neither wanted nor evaluated is the change in the quantity $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ acted on by this operator. Payoff: Ostensibly differential in the character of its action on $\pmb { A }$ ,the operator Riemann $( \ldots , \ldots , \pmb { u } , \pmb { v } ) = \mathcal { R } ( \pmb { u } , \pmb { v } )$ is actually local. Thus,replace the proposed smoothly varying vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ by a quite different but also smoothly varying vector field Afild,new).Then the two fields need agree only at the one point in question for them to give the same output Riemann $( . . . , A , u , v ) = \mathcal { R } ( u , v ) A$ at that point. This one knows from the fact that δA, the quantity calculated, has an existence and value independent of the choice of $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ .This one can also verify by detailed calculation (exercise l1.2). Power: Although they cancel out in their response to any change of A with location, the several differentiations in the curvature operator respond directly to the “rate of change of geometry with location”("geodesic deviation"). Prolongation: The closed curve need not be a quadrilateral. The curvature operator tells how a vector changes on parallel transport about smallcurves of arbitrary shape (Box 11.7).

# Exercise 11.5. COPLANARITY OF CLOSED CURVES

EXERCISE

Let $\pmb { f } _ { 1 }$ and $\pmb { f _ { 2 } }$ be the bivectors (see Box 11.7) for two small closed curves at the same event.   
Show that the curves are coplanar if and only if ${ \pmb f } _ { 1 } = a { \pmb f } _ { 2 }$ for some number a.

# Box 11.7 THE LAW FOR PARALLEL TRANSPORT ABOUT A CLOSED CURVE

# A. Special Case

Curve is closed quadrilateral formed by vector fields $\pmb { u }$ and ${ \pmb v } .$

1. Law says (in component form)

$$
\delta A ^ { \alpha } + R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } u ^ { \gamma } v ^ { \delta } = 0 .
$$

2. On what characteristics of the closed curve does this depend?

a. Notice that $R ^ { \alpha } { } _ { \beta \gamma \delta } = - R ^ { \alpha } { } _ { \beta \delta \gamma }$ (antisymmetry in last two indices; obvious in equation 11.12 for components; also obvious because reversing the direction the curve is traversed-i.e., interchanging $\pmb { u }$ and $\pmb { \nu }$ -should reverse sign of $\delta \pmb { A }$ ). b.Equation （l） contracts $\pmb { \mu } \otimes \pmb { \nu }$ into these antisymmetric,last two indices. The symmetric part of $\pmb { u } \otimes \pmb { v }$ must give zero. Only the antisymmetric part, $\pmb { \upsilon } \wedge \pmb { v } = \pmb { \upsilon } \otimes \pmb { v } - \pmb { v } \otimes \pmb { u }$ can contribute:

$$
\delta A ^ { \alpha } + { \frac { 1 } { 2 } } R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } ( u \wedge v ) ^ { \gamma \delta } = 0 .
$$

3. This antisymmetric part is a “bivector."It is independent of the curve's shape; it depends only on (a) the plane the curve lies in, and (b) the area enclosed by the curve. [Although without metric “area” is meaningless,“relative areas at an event in a given plane” have just as much meaning as “relative lengths at an

# Box 11.7 (continued)

event along a given direction.” Two vectors at the same event lie on the same line if they are multiples of each other; their relative length in that case is their. ratio. Similarly, two small closed curves at the same event lie in the same plane if their bivectors are multiples of each other (exercise l1.5); their relative area in that case is the ratio of their bivectors.]

# B. General Case

Arbitrary but small closed curve.

1. Break the curve down into a number of quadrilaterals, all lying in the same plane as the curve.

![](images/63e0e55c3fcc65249aeb04f88de4ebf0cefc76c2ab4ba2fc5d102e2fb21dafe6.jpg)

2. Traverse each quadrilateral once in the same sense as the curve is to be traversed. Result: all interior edges get traversed twice in opposite directions (no net traversal); the outer edge (the curve itself） gets traversed once.

3. Thus,SA due to traversing curve is the sum of the $\delta \pmb { A }$ s from traversal of each quadrilateral:

$$
\delta A ^ { \alpha } = - \frac { 1 } { 2 } \sum _ { \mathrm { q u a d r i l a t e r a l s } } R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } ( u \wedge v _ { \mathrm { f o r ~ g i v e n ~ q u a d r i l a t e r a l } } ) ^ { \gamma \delta } .
$$

Define the bivector $\pmb { \mathscr { f } }$ for the curve as the sum of the bivectors for its component quadrilaterals:

$$
\pmb { \mathscr { t } } \equiv \mathrm { ~ \mathcal ~ { ~ \sum ~ } ~ } \left( \mathbf { u } \wedge \pmb { \mathscr { v } } \right) _ { \mathrm { q u a d r i l a t e r a l } }
$$

(add “areas"; keep plane the same).

4.Then

$$
\delta A ^ { \alpha } + \frac { 1 } { 2 } R _ { ~ \beta \gamma \delta } ^ { \alpha } A ^ { \beta } f ^ { \gamma \delta } \equiv \delta A ^ { \alpha } + R _ { ~ \beta \downarrow \gamma \delta \mid } ^ { \alpha } A ^ { \beta } f ^ { \gamma \delta } = 0 .
$$

# C. Warning

This is valid only for closed curves of small compass: δA doubles when the area doubles; but the error increases by a factor ${ \sim } 2 ^ { 3 / 2 }$ $\mathbf { \delta } \mathbf { \delta } \mathbf { A } \propto \Delta a \Delta b$ in calculation of $\ S 1 1 . 4$ ； but error $\propto ( A a ) ^ { 2 } \varDelta b$ or $\Delta a ( \Delta b ) ^ { 2 } ]$

# $\$ 123$ .FLATNESS IS EQUIVALENT TO ZERO RIEMANN CURVATURE

To say that space or spacetime or any other manifold is flat is to say that there exists a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ in which all geodesics appear straight:

Flatness ofamanifold defined

$$
x ^ { \alpha } ( \lambda ) = a ^ { \alpha } + b ^ { \alpha } \lambda .
$$

(Example: Lorentz spacetime of special relativity,where test bodies move on such straight lines.） They can appear so if and only if the connection coeffcients in the geodesic equation

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \beta } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ,
$$

expressed in the same coordinate system, all vanish:

$$
T ^ { \beta } { } _ { \mu \nu } = 0 .
$$

From the vanishing of these connection coeffcients,it follows immediately (equation 11.12) that all the components of the curvature tensor are zero:

Flatness implies Riemann $= 0$

$$
R ^ { \beta } { } _ { \gamma \mu \nu } = 0 .
$$

[Geometric restatement of $( 1 1 . 1 6 ) \longrightarrow ( 1 1 . 1 8 ) \longrightarrow ( 1 1 . 1 9 )$ : For all geodesics to be straight in a given coordinate system means that initially parallel geodesics preserve their separation; the geodesic deviation is zero; and therefore the curvature vanishes.]

Is the converse true? Does zero Riemann curvature imply the existence of a coordinate system in which all geodesics appear straight? Yes,as one sees by the following construction.

Transport a vector parallel to itself from $\mathcal { P } _ { 0 }$ to $\mathcal { L }$ ,and then back from $\mathcal { L }$ t0 ${ \mathcal { P } } _ { 0 }$ along a slightly different route. It returns to its starting point with no alteration in magnitude or direction, because Riemann everywhere vanishes. Therefore parallel transport of a base vector $\pmb { e } _ { \mu }$ from ${ \mathcal { P } } _ { 0 }$ to $\mathcal { L }$ yields at $\mathcal { L }$ a base vector $\pmb { \varrho } _ { \mu }$ that is independent,both in magnitude and in direction,of the route of transportation (for routes obtainable one from the other by any continuous sequence of deformations). As for $\mathcal { L }$ ，so for all points of the manifold; and as for the one base vector $\pmb { e } _ { \mu } ,$ so for a complete set of base vectors $( \mu = 0 , 1 , 2 , 3$ : Parallel transport of a basis $\{ \pmb { e } _ { \alpha } ( \mathcal { P } _ { 0 } ) \}$ yields everywhere a field of frames ("frame field"),each base vector of which suffers zero change (relative to the frame field) on parallel transport from any point to any nearby point: thus,

Proof that Riemann $= 0$ implies flatness

$$
\begin{array} { r } { \pmb { \nabla } \pmb { e } _ { \mu } = 0 ; } \end{array}
$$

or

$$
\pmb { \nabla } _ { \nu } \pmb { e } _ { \mu } \left( \equiv \pmb { \nabla } _ { \pmb { e } _ { \nu } } \pmb { e } _ { \mu } \right) = 0 .
$$

With the vanishing of these individual derivatives,there also vanishes the commutator of any two basis-vector fields:

$$
[ { \pmb e } _ { \mu } , { \pmb e } _ { \nu } ] = \pmb { \nabla } _ { \mu } { \pmb e } _ { \nu } - \pmb { \nabla } _ { \nu } { \pmb e } _ { \mu } = 0 - 0 = 0 .
$$

Lorentz coordinates exist if andonlyif Riemann $= 0$

Flatness does not imply Euclidean topology

The gap in the quadrilateral of Figure 11.2 (there read $" \tilde { \varrho } _ { \mu } ^ { \mathrm { ~ ~ } } , "$ for $" \pmb { u } _ { \pmb { \imath } } ^ { \ \ast } \cdots + \pmb { \imath } \pmb { \imath } _ { \pmb { \imath } } ^ { \ \ast } \pmb { \imath } _ { \pmb { \imath } } ^ { \ \ \ast } | \pmb { u } _ { \pmb { \imath } } ^ { \ \ \ast } | ^ { 2 }$ for $\cdots$ ） closes up completely. Thereupon one can introduce coordinates $x ^ { \mu }$ ,each of which increases with a motion in the direction of the corresponding vector field; and with appropriate scaling of these coordinates,one can write

$$
{ \pmb \mathscr { e } } _ { \mu } = \frac { \partial } { \partial x ^ { \mu } }
$$

(see exercise 9.9). With this coordinate basis in hand, one can employ the formula

$$
\pmb { \nabla } _ { \alpha } \pmb { e } _ { \beta } = \pmb { e } _ { \mu } { \varGamma } ^ { \mu } { } _ { \beta \alpha }
$$

to calculate the connection coefficients. From the vanishing of the quantities on the left,one concludes that all the connection coefficients on the right ("bending of geodesics") must be zero; so spacetime is indeed flat.

SurySpees $T ^ { \mu } { } _ { \alpha \beta } = 0$ everywhere and geodesics are straight lines, $x ^ { \alpha } ( \lambda ) = a ^ { \alpha } + b ^ { \alpha } \lambda$ -if and only $i f$ Riemann $= 0$

Note:In the spacetime of Einstein, which has a metric,one can choose $\{ \pmb { e } _ { \pmb { \mu } } ( \mathcal { P } _ { 0 } ) \}$ in the above argument to be orthonormal, $\underline { { \pmb { e } } } _ { \mu } \cdot \pmb { e } _ { \nu } = \eta _ { \mu \nu }$ at $\mathcal { P } _ { 0 }$ .The resulting field of frames willthen be orthonormal everywhere,and the resulting coordinate system will be Lorentz. Thus, in Einsteinian gravity the above summary can be rewritten: spacetime is flat (there exists a Lorentz coordinate system) if and only if Riemann $= 0$

Warning: Flatness does not necessarily imply Euclidean topology. Take a sheet of paper. It is flat.Roll it up into a cylinder.It is still flat,intrinsically. The tracks of geodesics over it have not changed. Distances between neighboring points have not changed. Only the topology has changed, so far as an observer confined forever to the sheet is concerned.(The“extrinsic geometry"-the way the sheet is embedded in the surrounding three-dimensional space-has also changed;but an observer on the sheet knows nothing of this, and it is not the subject of the present chapter. See, instead $\ S 2 1 . 5 . )$

Take this cylinder. Bend it around and glueits two ends together, without changing its flat intrinsic geometry. Doing so is impossible if the cylinder remains embedded in flat, three-dimensional Euclidean space； perfectly possible if it is embedded in a Euclidean space of4 dimensions. However,embedding is unimportant to observers confined to the cylinder, since all they ever measure is intrinsic geometry； so all that matters to them is the topological identification of the two ends of the cylinder with each other. The result is topologically a torus; but the tracks of geodesics are still unchanged; the intrinsic geometry is flat; Riemann vanishes.

By analogy, take flat Minkowskii spacetime.Pick some'Lorentz frame, and in it pick a cube $1 0 ^ { 1 0 }$ light years on each side $( 0 < x < 1 0 ^ { 1 0 }$ light years； similarly for $y$ and $z ^ { - }$ ). Identify opposite faces of the cube so that a geodesic exiting across one face enters across the other. The result is topologically a three-torus: a “closed universe”with finite volume,with flat, Minkowskii geometry,and with a form that changes not at all as Lorentz time $t$ passes (no expansion, no contraction).

# $\$ 123$ .RIEMANN NORMAL COORDINATES

In curved spacetime one can never find a coordinate system with ${ T ^ { \alpha } } _ { \beta \gamma } = 0$ everywhere. But one can always construct local inertial frames at a given event $\mathcal { P } _ { 0 }$ ; and as viewed in such frames,free particles must move along straight lines,at least locally-which means $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ must vanish,at least locally.

A very special and useful realization of such a local inertial frame is a Riemannnormal coordinate system. Pick an event $\mathcal { P } _ { 0 }$ and a set of basis vectors $\{ \pmb { e } _ { \alpha } ( \mathcal { P } _ { 0 } ) \}$ to be used there by an inertial observer. Fill spacetime, near ${ \mathcal { P } } _ { 0 }$ ,with geodesics radiating out from $\mathcal { P } _ { 0 }$ like the quills of a hedgehog or porcupine. Each geodesic is determined by its tangent vector $\pmb { v }$ at $\mathcal { P } _ { 0 }$ ; and the general point on it can be denoted

Riemann normal coordinates: arealization of local inertial frames

Geometric construction of Riemann normal coordinates

$$
\begin{array} { r }  \begin{array} { r l } & { \mathcal { P } = \mathcal { G } ( \lambda ; \pmb { v } ) . } \\ & { \Big [ \mathrm { a f f i n e ~ p a r a m e t e r } ; } \\ & { \Big [ \mathrm { t e l l s ~ ^ { \ast \ast } w h e r e ^ { \circ , ~ } o n ~ g e o d e s i c } \Big ] } \end{array} \begin{array} { r l } & { \Big [ \mathrm { ~ t a n g e n t ~ v e c t o r ~ a t ~ \mathcal { P } _ { 0 } ; ~ } } \\ & { \Big [ \mathrm { t e l l s ~ ^ { \ast \ast } w h i c h ~ g e o d e s i c } ^ { \prime } \end{array} \Big ) } \end{array}
$$

Actually, this gives more geodesics than are needed. One reaches the same point after parameter length $^ { \frac { 1 } { 2 } \lambda }$ if the initial tangent vector is $2 v$ ,as one reaches after $\lambda$ if the tangent vector is $\pmb { \nu }$

$$
\mathcal { G } ( \lambda ; \pmb { v } ) = \mathcal { G } \left( \frac { 1 } { 2 } \lambda ; 2 \pmb { v } \right) = \mathcal { G } ( 1 ; \lambda \pmb { v } ) .
$$

Thus,by fixing $\lambda = 1$ and varying $\pmb { \nu }$ in all possible ways,one can reach every point in some neighborhood of $\mathcal { P } _ { 0 }$ .This is the foundation for constructing Riemann normal coordinates. Choose an event $\mathcal { P }$ .Find that tangent vector $\pmb { \nu }$ at $\mathcal { P } _ { 0 }$ for which $\mathcal { P } =$ $\mathcal { G } ( 1 ; \pmb { v } )$ Expand that $\pmb { \nu }$ in terms of the chosen basis and give its components the names $x ^ { \alpha }$ ：

$$
{ \mathcal { P } } = { \mathcal { G } } ( 1 ; x ^ { \alpha } \pmb { e } _ { \alpha } ) .
$$

The point $\mathcal { P }$ determines $x ^ { \alpha }$ uniquely (if $\mathcal { P }$ is near enough to $\mathcal { P } _ { 0 }$ that spacetime curvature has not caused geodesics to cross each other). Similarly, $x ^ { \alpha }$ determines $\mathcal { P }$ uniquely.Hence, $x ^ { \alpha }$ can be chosen as the coordinates of $\mathcal { P }$ -its“Riemann-normal coordinates,based on the event $\mathcal { P } _ { 0 }$ and basis $\{ \pmb { e } _ { \alpha } ( \mathcal { S } _ { 0 } ) \}$ ”

Equation (l1.26） summarizes Riemann-normal coordinates concisely. Other equations,derived in exercise l1.9, summarize their powerful properties:

$$
\begin{array} { c } { { { \pmb e } _ { \alpha } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = ( \partial / \partial x ^ { \alpha } ) _ { \mathcal { S } { \bf \rho } _ { 0 } } ; } } \\ { { { \cal T } ^ { \alpha } { } _ { \beta \gamma } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = 0 ; } } \\ { { { \cal T } ^ { \alpha } { } _ { \beta \gamma , \mu } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = - \displaystyle \frac { 1 } { 3 } ( R ^ { \alpha } { } _ { \beta \gamma \mu } + R ^ { \alpha } { } _ { \gamma \beta \mu } ) . } } \end{array}
$$

Mathematical properties of Riemann normal coordinates

If spacetime has a metric (as it does in actuality),and if the observer's frame at $\mathcal { P } _ { 0 }$ has been chosen orthonormal $( \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } = \eta _ { \alpha \beta } )$ ，then

$$
\begin{array} { c } { { g _ { \alpha \beta } ( \mathcal { S } _ { 0 } ) = \eta _ { \alpha \beta } , } } \\ { { g _ { \alpha \beta , \mu } ( \mathcal { S } _ { 0 } ) = 0 , } } \\ { { g _ { \alpha \beta , \mu \nu } ( \mathcal { S } _ { 0 } ) = \displaystyle - \frac { 1 } { 3 } ( R _ { \alpha \mu \beta \nu } + R _ { \alpha \nu \beta \mu } ) } } \\ { { \displaystyle = - \frac { 2 } { 3 } J _ { \alpha \beta \mu \nu } , } } \end{array}
$$

$$
R _ { \alpha \beta \gamma \delta } ( \mathring { \mathcal { S } } _ { 0 } ) = g _ { \alpha \mathfrak { s } , \beta \gamma } ( \mathring { \mathcal { S } } _ { 0 } ) - g _ { \alpha \gamma , \beta \mathfrak { s } } ( \mathring { \mathcal { S } } _ { 0 } ) .
$$

Othermathematical realizations of a local inertial frame

Here $J _ { \alpha \beta \mu \nu }$ are components of the Jacobi curvature tensor (see exercise l1.7).

Is this the onlycoordinatesystem that is locallyinertial at ${ \mathcal { P } } _ { 0 }$ (i.e., has ${ T ^ { \alpha } } _ { \beta \gamma } = 0$ there)and is tied to the basis vectors ${ \pmb { e } } _ { \alpha }$ there (i.e., has $\partial / \partial x ^ { \alpha } = \pmb { e } _ { \alpha }$ there)? No. But all such coordinate systems (called “normal coordinates") will be the same to second order:

$$
\begin{array} { r } { x _ { \mathrm { N E W } } ^ { \alpha } ( \mathcal P ) = x _ { \mathrm { O L D } } ^ { \alpha } ( \mathcal P ) + \mathrm { c o r r e c t i o n s ~ o f ~ o r d e r } ~ ( x _ { 0 \mathrm { L D } } ^ { \alpha } ) ^ { 3 } . } \end{array}
$$

Moreover, only those the same to third order,

$$
\begin{array} { r } { x _ { \mathrm { N E W } } ^ { \alpha } ( \mathcal P ) = x _ { \mathrm { O L D } } ^ { \alpha } ( \mathcal P ) + \mathrm { c o r r e c t i o n s ~ o f ~ o r d e r ~ } ( x _ { 0 \mathrm { L D } } ^ { \alpha } ) ^ { 4 } , } \end{array}
$$

will preserve the beautiful ties (l1.29) and (l1.32) to the Riemann curvature tensor.

EXERCISES

# Exercise 11.6. SYMMETRIES OF Riemann

(To be discussd in Chapter l3). Show that Riemann has the following symmetries:

$$
\begin{array} { r l } { R ^ { \alpha } { } _ { \beta \gamma \delta } = R ^ { \alpha } { } _ { \beta [ \gamma \delta ] } \quad } & { ( \mathrm { a n t i s y m m e t r i c ~ o n ~ l a s t ~ 2 ~ i n d i c e s } ) } \\ { R ^ { \alpha } { } _ { \{ \beta \gamma \delta \} } = 0 \quad } & { ( \mathrm { v a n i s h i n g ~ o f ~ c o m p l e t e l y ~ a n t i s y m m e t r i c ~ p a r t } ) } \end{array}
$$

# Exercise 11.7. GEODESIC DEVIATION MEASURES ALL CURVATURE COMPONENTS

The equation of geodesic deviation, written up to now in the form

or

$$
\begin{array} { c } { { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \pmb { R i } e m a n n \left( . . . , \pmb { u } , \pmb { n } , \pmb { u } \right) = 0 } } \\ { { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \pmb { \mathcal { A } } ( \pmb { n } , \pmb { u } ) \pmb { u } = 0 , } } \end{array}
$$

also lets itself be written in the Jacobi form $\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \mathcal { J } ( \pmb { u } , \pmb { u } ) \pmb { n } = 0 . } \end{array}$ Here $\mathcal { J } ( \pmb { u } , \pmb { v } )$ ,the“Jacobi curvature operator,”is defined by

$$
\mathcal { J } ( \pmb { u } , \pmb { v } ) \pmb { n } \equiv \frac { 1 } { 2 } \left[ \mathcal { R } ( \pmb { n } , \pmb { u } ) \pmb { v } + \mathcal { R } ( \pmb { n } , \pmb { v } ) \pmb { u } \right] ,
$$

and is related to the“Jacobi curvature tensor” by

$$
\begin{array} { r } { J a c o b i \left( . . . , n , u , v \right) \equiv \mathcal { J } ( u , v ) n , } \end{array}
$$

which implies

$$
{ J ^ { \mu } } _ { \nu \alpha \beta } = { J ^ { \mu } } _ { \nu \beta \alpha } = { \frac { 1 } { 2 } } ( R ^ { \mu } { } _ { \alpha \nu \beta } + R ^ { \mu } { } _ { \beta \nu \alpha } ) .
$$

(a) Show that $J ^ { \mu } { } _ { ( \alpha \beta \gamma ) } = 0$ follows from $R ^ { \mu } { } _ { \alpha \beta \gamma } = R ^ { \mu } { } _ { \alpha [ \beta \gamma ] } .$

(b) Show that by studying geodesic deviation (allowing arbitrary $\pmb { u }$ and $\pmb { n }$ in $\yen 1$ $\mathcal { J } ( u , u ) n = 0 )$ one can measure all components of Jacobi.

(c) Show that Jacobi contains precisely the same information as Riemann.[Hint: show that

$$
{ R ^ { \mu } } _ { \alpha \nu \beta } = { \frac { 2 } { 3 } } ( J ^ { \mu } { } _ { \nu \alpha \beta } - J ^ { \mu } { } _ { \beta \alpha \nu } ) ;
$$

this plus equation(11.36) for $J ^ { \mu } { } _ { \nu \alpha \beta }$ proves "same information content".] Hene, by studying geodesic deviation one can also measure all the components of Riemann.

(d) Show that the symmetry of $R ^ { \mu } { } _ { [ \nu \alpha \beta ] } = 0$ is essentialin theequivalence between Jacobi and Riemann by exhibiting proposed values for $R ^ { \mu } { } _ { \nu \alpha \beta } = - R ^ { \bar { \mu } } { } _ { \nu \beta \alpha }$ for which $R ^ { \mu } { } _ { [ \nu \alpha \beta ] } \neq 0$ ， and from which one would find $J ^ { \mu } { } _ { \nu \alpha \beta } = 0$

# Exercise 11.8. GEODESIC DEVIATION IN GORY DETAIL

Write out the equation of geodesic deviation in component form in a coordinate system. Expand all covariant derivatives (semicolon notation) in terms of ordinary (comma) derivatives and in terms of I's to show all $\boldsymbol { r }$ and a terms explicitly.

# Exercise 11.9. RIEMANN NORMAL COORDINATES IN GENERAL

Derive properties (11.27),(11.28),(11.29),(11.31),(11.32),and (11.32') of Riemann normal coordinates. Hint: Proceed as follows.

(a)From definition (11.26),derive $( \partial \mathcal { P } / \partial x ^ { \alpha } ) _ { \varphi _ { 0 } } = \pmb { \varrho } _ { \alpha } .$ (b) Similarly,from definition (I1.26),show that each of the curves $x ^ { \alpha } = v ^ { \alpha } \lambda$ (where the $v ^ { \alpha }$ are constants) is a geodesic through ${ \mathcal P _ { 0 } } .$ with affine parameter $\lambda$ (c） Show that $T ^ { \alpha } { } _ { \beta \gamma } ( \mathcal { P } _ { 0 } ) = 0$ by substituting $x ^ { \alpha } = v ^ { \alpha } \lambda$ into the geodesic equation. (d） Since the curves $x ^ { \alpha } = v ^ { \alpha } \lambda$ are geodesics for every choice of the parameters $v ^ { \alpha }$ ,they provide not only a geodesic tangent $\pmb { \upsilon } \equiv ( \partial / \partial \lambda ) _ { v ^ { \alpha } }$ ，but also several deviation vectors ${ \pmb N } _ { ( \alpha ) } \equiv ( \partial / \partial v ^ { \alpha } ) _ { \lambda }$ . Compute the components of these vectors in the Riemann normal coordinate system,and substitute into the geodesic deviation equation as written in exercise 11.8. (e) Equate to zero the coefficients of the zeroth and first powers of $\lambda$ in the geodesic deviation equation of part (d),using

$$
\left. T ^ { \alpha } { } _ { \beta \gamma } \right| _ { x ^ { \mu } = v ^ { \mu } \lambda } = \lambda v ^ { \mu } \bar {Gamma ^ { \alpha } } { } _ { \beta \gamma , \mu } ( \mathcal { S } \vec { \rho } _ { 0 } ) + O ( \lambda ^ { 2 } ) ,
$$

which is a Taylor series for $\boldsymbol { r }$ Inthis wayarrveatequatin (1.29)for $T ^ { \alpha } { } _ { \beta \gamma , \mu }$ in terms of the Riemann tensor.

(f） From equations (11.28),(l1.29),and (8.24) for the connection coeffcients in terms of the metric, derive equations (11.31), (11.32),and (11.32').

# Exercise 11.10. BIANCHI IDENTITIES

Show that the Riemann curvature tensor satisfies the following“Bianchi identities”

$$
R ^ { \alpha } { } _ { \beta [ \gamma \delta ; \epsilon ] } = 0 .
$$

The geometric meaning of these identities will be discussed in Chapter 15.[Hint: Perform the calculation at the origin of a Riemann normal coordinate system.]

# Exercise 11.11. CURVATURE OPERATOR ACTS ON 1-FORMS

Let $\mathcal { R } ( \pmb { u } , \pmb { v } )$ be the operator $\begin{array} { r } { \langle \hat { \mathcal { R } } ( \pmb { \mu } , \pmb { v } ) = [ \pmb { \nabla } _ { \pmb { u } } , \pmb { \nabla } _ { \pmb { v } } ] - \pmb { \nabla } [ \pmb { u } , \pmb { v } ] } \end{array}$ when acting on l-forms $\pmb { \sigma }$ (or other tensors) as well as on tangent vectors. Show that

$$
\langle \Re ( { \pmb u } , { \pmb v } ) { \pmb \sigma } , { \pmb w } \rangle = - \langle { \pmb \sigma } , \Re ( { \pmb u } , { \pmb v } ) { \pmb w } \rangle .
$$

Exercise 11.12. ROTATION GROUP:RIEMANN CURVATURE

[Continuation of exercises 9.13,9.14,and I0.17.] Calculate the components of the Riemann curvature tensor for the rotation group's manifold $S O ( 3 )$ ； use the basis of generators $\{ e _ { \alpha } \}$ · [Answer:

$$
R ^ { \alpha } { } _ { \beta \gamma \delta } = \frac { 1 } { 2 } \delta _ { \gamma \delta } ^ { \alpha \beta } ,
$$

where $\delta _ { \gamma \delta } ^ { \alpha \beta }$ is the permutation symbol defined in equation (3.50l):

$$
\delta _ { \gamma \delta } ^ { \alpha \beta } \equiv ( \delta ^ { \alpha } { } _ { \gamma } \delta ^ { \beta } { } _ { \delta } - \delta ^ { \alpha } { } _ { \delta } \delta ^ { \beta } { } _ { \gamma } ) .
$$

Note that this answer is independent of location $\mathcal { P }$ in the group manifold.]

# CHAPTER 12

# NEWTONIAN GRAVITY IN THE LANGUAGE OF CURVED SPACETIME

The longest period of time for which a modern painting has hung upside down in a public gallery unnoticed is 47 days.This   
occurred to Le Bateau by Matisse in the Museum of Modern Art, New York City. In this time 116.000 people had passed through the gallery.

McWHIRTER AND MCWHIRTER (1971)

# $\$ 12.1$ .NEWTONIAN GRAVITY IN BRIEF

The equivalence principle is not unique to Einstein's description of the facts of gravity. What is unique to Einstein is the combination of the equivalence principle and local Lorentz geometry. To return to the world of Newton, forget everything discovered in the last century about special relativity,light cones,the limiting speed of light, and proper time. Return to the“universal time” $t$ of earlier centuries. In terms of that universal time,and of rectangular,“Galilean” space coordinates, Newtonian theory gives for the trajectories of neutral test particles

This chapter is entirely Track 2. Chapters 9-11 are necessary preparation for it.

It is not needed for any later chapter,but it will be helpful in (1）Chapter 17 (Einstein field equations) and (2) Chapters 38 and 39 (experimental tests and other theories of gravity).

$$
\begin{array} { r } { \frac { d ^ { 2 } x ^ { j } } { d t ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } = 0 ; } \end{array}
$$

Newtonian gravity:original formulation

Customarily one interprets these equations as describing the“curved paths" $x ^ { j } ( t )$ along which test particles fall in Euclidean space (not spacetime). These curved paths include circular orbits about the Earth and the parabolic trajectory of a baseball. Cartan (l923,1924) asks one to abandon this viewpoint. Instead, he says, regard these trajectories as geodesics $[ t ( \lambda ) , x ^ { j } ( \lambda ) ]$ in curved spacetime.(This change of viewpoint was embodied in Figures B and C of Box 1.6.) Since the “affinely ticking"

Newtonian gravity: translation into language of curved spacetime

Newtonian clocks carried by test particles read universal time (or some multiple, $\lambda = a t + b$ , thereof), the equation of motion (l2.1) can be rewritten

$$
\frac { d ^ { 2 } t } { d \lambda ^ { 2 } } = 0 , \qquad \frac { d ^ { 2 } x ^ { j } } { d \lambda ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } \left( \frac { d t } { d \lambda } \right) ^ { 2 } = 0 .
$$

By comparing with the geodesic equation

$$
d ^ { 2 } x ^ { \alpha } / d \lambda ^ { 2 } + { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } ( d x ^ { \beta } / d \lambda ) ( d x ^ { \gamma } / d \lambda ) = 0 ,
$$

one can read off the values of the connection coefficients:

$$
{ \cal T } _ { 0 0 } ^ { j } = \partial \phi / \partial x ^ { j } ; \qquad \mathrm { a l l ~ o t h e r } \ { \cal T } _ { \phantom { \alpha } \beta \gamma } ^ { \alpha } \ \mathrm { v a n i s h } .
$$

And by inserting these into the standard equation (l1.l2) for the components of the Riemann tensor, one learns (exercise l2.1)

$$
{ R ^ { j } } _ { 0 k 0 } = - { R ^ { j } } _ { 0 0 k } = { \frac { \hat { \sigma } ^ { 2 } \phi } { \hat { \sigma } x ^ { j } \hat { \sigma } x ^ { k } } } ; ~ \mathrm { a l l ~ o t h e r } ~ { R ^ { \alpha } } _ { \beta \gamma \delta } \mathrm { v a n i s h } .
$$

Finally, the source equation for the Newtonian potential

$$
\nabla ^ { 2 } \phi \equiv \sum _ { j } \phi _ { , j j } = 4 \pi \rho
$$

one can rewrite with the help of the “Ricci curvature tensor”

$$
R _ { \alpha \beta } \equiv R _ { \alpha \mu \beta } ^ { \mu } \ ( \mathrm { c o n t r a c t i o n \ o f } \ R i e m a n n )
$$

in the geometric form (exercise 12.2)

$$
R _ { 0 0 } = 4 \pi \rho ; \qquad \mathrm { a l l ~ o t h e r } ~ R _ { \alpha \beta } ~ \mathrm { v a n i s h } .
$$

Equation (12.4) for $\Gamma ^ { \alpha } { } _ { \beta \gamma } ,$ equation (12.5) for $R ^ { \alpha } { } _ { \beta \gamma \delta }$ , equation (12.8) for $R _ { \alpha \beta }$ ,plus the law of geodesic motion are the full content of Newtonian gravity,rewritten in geometric language.

It is one thing to pass quickly through these component manipulations. It is quite another to understand fully,in abstract and pictorial terms,the meanings of these equations and the structure of Newtonian spacetime. To produce such understanding, and to compare Newtonian spacetime with Einsteinian spacetime, are the goals of this chapter,which is based on the work of Cartan (l923,1924), Trautman (1965), and Misner (1969a).

# EXERCISES

# Exercise 12.1. RIEMANN CURVATURE OF NEWTONIAN SPACETIME

Derive equation (12.5） for $R ^ { \alpha } { } _ { \beta \gamma \delta }$ from equation (12.4) for $\varGamma ^ { \alpha } { } _ { \beta \gamma } .$

Exercise 12.2. NEWTONIAN FIELD EQUATION Derive the geometric form (12.8) of the Newtonian field equation from (12.5) through (12.7).

# $\$ 12.2$ . STRATIFICATION OF NEWTONIAN SPACETIME

Galileo and Newton spoke of a flat, Euclidean“absolute space”and of an “absolute time,”two concepts distinct and unlinked.In absolute space Newtonian physics took place; and as it took place,absolute time marched on. No hint was there that space and time might be two aspects ofa single entity,a curved “spacetime”-until Einstein made the unification in relativity physics,and Cartan (l923) followed suit in Newtonian physics in order to provide clearer insight into Einstein's ideas.

How do the absolute space of Galileo and Newton,and their absolute time, fit into Cartan's “Newtonian spacetime"? The key to the fit is stratification; stratification produced by the universal time coordinate t.

The geometry of Newtonian spacetime:

Regard t as a function (scalar field) defined once and for all in Newtonian spacetime

"Universal time" as a scalar field

$$
t = t ( { \mathcal { P } } ) .
$$

Without it, spacetime could not be Newtonian, for $" t "$ is every bit as intrinsic to Newtonian spacetime as the metric $" g \prime$ is to Lorentz spacetime. The layers of spacetime are the slices of constant t-the “space slices"-each of which has an identical geometric structure: the old “absolute space.”

Adopting Cartan's viewpoint, ask what kind of geometry is induced onto each space slice by the surrounding geometry of spacetime. A given space slice is endowed, by the Galilean coordinates of $\ S 1 2 . 1$ , with basis vectors $\pmb { e } _ { j } = \partial / \partial x ^ { j }$ ；and this basis has vanishing connection coefficients, $T ^ { j } { } _ { \kappa \ell } = 0$ [cf. equation (12.4)]. Consequently, the geometry of each space slice is completely flat.

“Absolute space” is Euclidean in its geometry, according to the old viewpoint, and the Galilean coordinates are Cartesian. Translated into Cartan's language, this says: not only is each space slice ( $( t =$ constant) flat,and not only do its Galilean coordinates have vanishing connection coefficients, but also each space slice is endowed with a three-dimensional metric,andits Galilean coordinate basis is orthonormal,

Space slices with Euclidean geometry

$$
\begin{array} { r } { \pmb { e } _ { i } \cdot \pmb { e } _ { j } = ( \hat { \partial } / \hat { \partial } \pmb { x } ^ { i } ) \cdot ( \hat { \partial } / \hat { \partial } \pmb { x } ^ { j } ) = \delta _ { i j } . } \end{array}
$$

If the space slices are really so flat, where do curvature and geodesic deviation enter in? They are properties of spacetime. Parallel transport a vector around a closed curve lying entirely in a space slice; it will return to its starting point unchanged.. But transport it forward in time by $\pmb { \varDelta t }$ , northerly in space by $\pmb { \varDelta x ^ { k } }$ , back in time by $- \Delta t$ ,and southerly by $- \varDelta x ^ { k }$ to its starting point; it will return changed by

Curvature acts in spacetime, not in space slices

$$
\begin{array} { r } { \delta \pmb { A } = - \mathcal { R } \bigg ( \Delta t \frac { \partial } { \partial t } , \pmb { A x } ^ { k } \frac { \partial } { \partial { \pmb x } ^ { k } } \bigg ) \pmb { A } ; } \end{array}
$$

i.e.,

$$
\begin{array} { r } { \delta A ^ { 0 } = 0 , \delta A ^ { j } = \leavevmode { - R ^ { j } \mathstrut _ { 0 0 k } A ^ { 0 } ( \varDelta t ) ( \varDelta x ^ { k } ) } = \frac { \vec { c } ^ { 2 } \phi } { \partial x ^ { j } \partial x ^ { k } } A ^ { 0 } ( \varDelta t ) ( \varDelta x ^ { k } ) . } \end{array}
$$

Geodesics of a space slice (Euclid's straight lines) that are initially parallel remain

always parallel. But geodesics of spacetime (trajectories of freely falling particles) initially parallel get pried apart or pushed together by spacetime curvature,

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \mathcal { R } ( \pmb { n } , \pmb { u } ) \pmb { u } = 0 ,
$$

or equivalently in Galilean coordinates:

$$
\frac { d ^ { 2 } n ^ { j } } { d t ^ { 2 } } + \frac { \partial ^ { 2 } \phi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0
$$

(see Box l2.1 and exercise 12.3).

# EXERCISE

# Exercise 12.3. GEODESIC DEVIATION DERIVED

Produce a third column for Box l1.4, one that carries out the “geometric analysis” in component notation using the Galilean connection coefficients (l2.4) of Newtonian spacetime. Thereby achieve a deeper understanding of how the geometric analysis parallels the old Newtonian analysis.

# $\$ 123$ . GALILEAN COORDINATE SYSTEMS

The Lorentz spacetime of special relativity has an existence and structure completely independent of any coordinate system. But a special property of its geometry (zero curvature) allows the introduction of a special class of coordinates (Lorentz coordinates), which cling to spacetime in a special way

By studying these special coordinate systems and the relationships between them (Lorentz transformations), one learns much about the structure of spacetime itself (breakdown in simultaneity; Lorentz contraction； time dilatation; ...).

Galilean coordinates defined

Similarly for Newtonian spacetime. Special properties of its geometry (explored in abstract later; Box 12.4) permit the introduction of special coordinates (Galilean coordiates), which cling to spacetime in a special way

$$
x ^ { 0 } ( { \mathcal { P } } ) = t ( { \mathcal { P } } ) ;
$$

$$
( \partial / \partial x ^ { j } ) \cdot ( \partial / \partial x ^ { k } ) = \delta _ { j k } ;
$$

$T ^ { j } { } _ { 0 0 } = \Phi _ { , j }$ for some scalar field $\pmb { \bar { p } }$ , and all other $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ vanish.

To understand Newtonian spacetime more deeply, study the relations between these Galilean coordinate systems.

Coordinate system for calculation: Galilean space coordinates $x ^ { j }$ and universal time coordinate $t ,$ General component form of equation:

$$
{ \frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } + R ^ { \alpha } { } _ { \beta \gamma \delta } { \frac { d x ^ { \beta } } { d \lambda } } n ^ { \gamma } { \frac { d x ^ { \delta } } { d \lambda } } = 0 .
$$

Special conditions for this calculation: let the particles'clocks (afine parameters) all be normalized to read universal time, $\lambda = t$ 、This means that the separation vector

$$
n ^ { \alpha } = (  { \partial } x ^ { \alpha } /  { \partial } n ) _ { \lambda }
$$

between geodesics has zero time component, $n ^ { 0 } = 0$ ; i.e., in abstract language,

$$
\langle d t , n \rangle = t _ { , \alpha } n ^ { \alpha } = n ^ { 0 } = 0 ;
$$

i.e., in geometric language, $\pmb { n }$ lies in a space slice (surface of constant $t$ ）.

Evaluation of covariant derivative:

![](images/5be2b9c2f4e5455c6fd9d26ae474abeedcd91ad47e50d31953c0eecd05f08281.jpg)

$\begin{array} { r } { \frac { D n ^ { \alpha } } { D \lambda } = \frac { d n ^ { \alpha } } { d \lambda } + \underbrace { { \Gamma ^ { \alpha } } _ { \beta \mu } } _ { \lambda } n ^ { \beta } \frac { d x ^ { \mu } } { d \lambda } = \frac { d n ^ { \alpha } } { d \lambda } , } \\  { [ 0 \mathrm { ~ u n l e s s ~ } \beta = 0 ] } ^ { \qquad } \enspace \enspace \middle [ \enspace . \vphantom { \int ^ { \alpha } } \end{array}$ a space index $( n ^ { 0 } = 0 )$ ] ${ \begin{array} { l } { { \frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } = { \frac { d ( D n ^ { \alpha } / d \lambda ) } { d \lambda } } + \underbrace { { \Gamma ^ { \alpha } } _ { \beta \mu } } _ { \mathrm { \normalfont ~ d } } { \frac { d n ^ { \beta } } { d \lambda } } { \frac { d x ^ { \mu } } { d \lambda } } = { \frac { d ( D n ^ { \alpha } / d \lambda ) } { d \lambda } } = { \frac { d ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } } = { \frac { d ^ { 2 } n ^ { \alpha } } { \mathrm { \normalfont ~ d } } } . } \\ { \left[ 0 { \mathrm { ~ u n l e s s ~ } } \beta = 0 \right] { \cfrac { d n ^ { \beta } } { \mathrm { \normalfont ~ / } 0 { \mathrm { ~ u n l e s s ~ } } \beta { \mathrm { ~ i s ~ s p a c e ~ i n d e x } } | } } } \end{array} }$

Evaluation of tidal accelerations:

RBy8 nydx8 =0 since $R _ { 0 k 0 } ^ { j }$ and $R _ { ~ 0 0 k } ^ { j }$ are only nonzero components. d

$$
\begin{array} { l } { { \underbrace { R ^ { j } { } _ { \beta \gamma \delta } } _ { \mathrm { \normalfont ~ \displaystyle \{ ~ \int ~ } } d \lambda \begin{array} { l } { { d x ^ { \beta } } } \\ { { d \lambda } } \end{array}  \{ \begin{array} { l l } { { d x ^ { \delta } } } \\ { { d \lambda } } \end{array} = R ^ { j } { } _ { 0 k 0 } \frac { d t } { d \lambda } n ^ { k } \frac { d t } { d \lambda } = R ^ { j } { } _ { 0 k 0 } n ^ { k } = \frac { { \hat { c } } ^ { 2 } \phi } { \hat { c } x ^ { j } \partial x ^ { k } } n ^ { k } . } } \\ { { \mathrm { \normalfont ~ \{ ~ \begin{array} { l l } { { ~ 0 \ u n l e s s ~ } \gamma ~ i s ~ s p a c e ~ i n d e x \} ~ } } \\ { { \mathrm { \normalfont ~ \{ ~ f o r ~ } \gamma ~ a ~ s p a c e ~ i n d e x ; ~ 0 ~ u n l e s s ~ } \beta = \delta = 0 \} } } \end{array} } \end{array}
$$

Resultant equation of geodesic deviation:

$$
\frac { d ^ { 2 } n ^ { 0 } } { d t ^ { 2 } } = 0
$$

Point of principle: how can one write down the laws of gravity and properties of spacetime in Galilean coordinates first $( \ S 1 2 . 1 )$ ,and only afterward (here) come to grip with the nature of the coordinate system and its nonuniqueness? Answer: (a quotation from $\ S 3 . 1$ ， slightly modified):“Here and elsewhere in science,as emphasized not least by Henri Poincaré,that view is out of date which used to say \*Define your terms before you proceed.' All the laws and theories of physics, including Newton's laws of gravity, have this deep and subtle character, that they both define the concepts they use (here Galilean coordinates) and make statements about these concepts."

The Newtonian laws of gravity, writen in a Galilean coordinate system

$$
x ^ { 0 } = t , \qquad ( \partial / \partial x ^ { j } ) \cdot ( \partial / \partial x ^ { k } ) = \delta _ { j k }
$$

make the statement ${ } ^ { \mathrm { * } } T ^ { j } { } _ { 0 0 } = \Phi _ { , j }$ and all other $T ^ { \alpha } { } _ { \beta \gamma } = 0 ^ { , \gamma }$ about the geometry of spacetime. This statement in turn gives information about the relationships between different Galilean systems. Let one Galilean system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ be given,and seek the most general coordinate transformation leading to another, $\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \}$ . The following constraints exist:(l) $x ^ { 0 ^ { \prime } } = x ^ { 0 } = t$ (both time coordinates must be universal.time); (2) at fixed $t$ (i.e.,in a fixed space slice) both sets of space coordinates must be Euclidean, so they must be related by a rotation and a translation:

$$
\begin{array} { l } { { x ^ { j ^ { \prime } } = A _ { j ^ { \prime } k } x ^ { k } + a ^ { j ^ { \prime } } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \scriptstyle \qquad \bigcup _ { \{ \mathrm { { r o t a t i o n ~ m a t r i x , ~ i . e . , ~ } } A _ { j ^ { \prime } L } A _ { k ^ { \prime } l } = \delta _ { j ^ { \prime } k ^ { \prime } } \} } } } \\ { { \scriptstyle x ^ { k } = A _ { j ^ { \prime } k } x ^ { j ^ { \prime } } - a ^ { k } , \mathrm { ~ w i t h ~ } a ^ { k } \equiv A _ { j ^ { \prime } k } a ^ { j ^ { \prime } } . } } \end{array}
$$

The rotation and translation might, a priori, be different on different slices, $A _ { j ^ { \prime } k } =$ $A _ { j ^ { \prime } k } ( t )$ and $a ^ { j } = a ^ { j } ( t )$ ； but (3) they must be constrained by the required special form of the connection coefficients. Calculate the connection coefficients in the new coordinate system, given their form in the old. The result (exercise l2.4) is:

$$
\begin{array} { l } { { { \cal T } ^ { j ^ { \prime } } { } _ { 0 ^ { \prime } k ^ { \prime } } = { \cal T } ^ { j ^ { \prime } } { } _ { k ^ { \prime } 0 ^ { \prime } } = A _ { j ^ { \prime } \mathrm { t } } \dot { A } _ { k ^ { \prime } \mathrm { t } } \qquad \mathrm { ( p r o d u c e s ~ ^ { * * } C o r i o l i s ~ f o r c e s ^ { * } ) } ; } } \\ { { \cal T } ^ { j ^ { \prime } } { } _ { 0 ^ { \prime } 0 ^ { \prime } } = \displaystyle \frac { \partial \phi } { \partial x ^ { j } } + A _ { j ^ { \prime } k } ( \ddot { A } _ { \mathit { t } ^ { \prime } k } x ^ { \mathit { t } ^ { \prime } } - \ddot { a } ^ { k } ) ; } \\ { { \cal T } ^ { * * } \mathrm { c e n t r i f u g a l ~ f o r c e s ^ { \prime } ) } . } \end{array}
$$

("Euclidean” index conventions; repeated space indices to be summed even if both are down; dot denotes time derivative). These have the standard Galilean form (l2.4) if and only if

$$
\begin{array} { c } { { \dot { A } _ { j ^ { \prime } k } = 0 , \phi ^ { \prime } = \phi - \ddot { a } ^ { k } x ^ { k } + \mathrm { c o n s t a n t . } } } \\ { { \left[ \begin{array} { l } { { \mathrm { N e w t o n i a n ~ p o t e n t i a l ~ i n } } } \\ { { \mathrm { n e w ~ c o o r d i n a t e ~ s y s t e m } } } \end{array} \right] ^ { \mathrm { ~ \dagger ~ } } \begin{array} { l } { { \dot { \mathrm { ~ L } } \mathord { \left[ \mathrm { N e w t o n i a n ~ p o t e n t i a l ~ i n } \right]}  } } \\ { { \mathrm { ~ \left[ \mathrm { o l d ~ c o o r d i n a t e ~ s y s t e m } ~ \right] ~ } } } \end{array} } } \end{array}
$$

These results can be restated in words: any two Galilean coordinate systems are related by(l) a time-independent rotation of the space grid (same rotation on each space slice), and (2) a time-dependent translation of the space grid (translation possibly different on different slices)

$$
\begin{array} { c } { { x ^ { j ^ { \prime } } = A _ { j ^ { \prime } k } x ^ { k } + a ^ { j ^ { \prime } } ( t ) . } } \\ { { \mathrm { [ c o n s t a n t ] } } } \end{array}
$$

Transformations linking Galilean coordinate systems

The Newtonian potential is not a function defined in spacetime with existence independent of allcoordinate systems. (There is no coordinate-free way to measure it.) Rather,it depends for its existence on a particular choice of Galilean coordinates; and if the choice is changed via equation (l2.16), then $\pmb { \phi }$ is changed:

$$
\phi ^ { \prime } = \phi - \ddot { a } ^ { k } x ^ { k } .
$$

(By contrast, an existence independent of all coordinates is granted to the universal time $t ( { \mathcal { P } } )$ and the covariant derivative ${ \pmb v } .$ ）

Newtonian potential depends on choice of Galilean coordinate system

Were all the matter in the universe concentrated'in a finite region of space and surrounded by emptiness (island universe")， then one could impose the global boundary condition

Absolute Galilean coordinates defined

$$
\phi \longrightarrow 0 \mathrm { \ a s \ } r \equiv ( x ^ { k } x ^ { k } ) ^ { 1 / 2 } \longrightarrow \infty .
$$

This would single out a subclass of Galilean coordinates ("absolute" Galilean coordinates), with a unique, common Newtonian potential. The transformation from one absolute Galilean coordinate system to any other would be

Transformations linking absolute Galilean coordinate systems

x=Ajκxk +a³+u"t   
[constant] [constant]   
rotation velocity] constant displacement

("Galilean transformation"). But. (l） by no local measurements could one ever distinguish these absolute Galilean coordinate systems from the broader class of Galilean systems (to distinguish, one must integrate the locally measurable quantity $\boldsymbol { \phi } _ { , j } = \boldsymbol { \Gamma ^ { j } } _ { 0 0 }$ out to infinity);and (2) astronomical data deny that the real universe is an island of matter surrounded by emptiness.

It is instructive to compare Galilean coordinates and Newtonian spacetime as described above with Lorentz coordinates and the Minkowskii spacetime of special relativity,and with the general coordinates and Einstein spacetime of general relativity;see Boxes l2.2 and 12.3.

(continued on page 298)

Box 12.2 NEWTONIAN SPACETIME，MINKOWSKIIAN SPACETIME，AND EINSTEINIAN SPACETIME: COMPARISON AND CONTRAST   

<table><tr><td>Query</td><td>Newtonian spacetime</td><td>Minkowskiian spacetime (special relativity)</td><td>Einsteinian spacetime (general relativity)</td></tr><tr><td>What a priori geometric structures does spacetime possess?</td><td>(l）Universal time function / (2) Covariant derivative (3) Spatial metric “&quot;; but spacetime metric can not be defined (exercise 12.10)</td><td>A spacetime metric that is fat (vanishing Riemann curvature)</td><td>A spacetime metric</td></tr><tr><td>What preferred coordinate systems are present?</td><td>(I）Galilean coordinates in general (2)Absolule Galilean coordinates in an island universe (this case nol considered here)</td><td>Lorentz coordinates</td><td>In general, every coordinate system is equally preferred (though in special cases with symmetry there are special preferred coordinates)</td></tr><tr><td>What is required to select out a particular preferred coordinate system?</td><td>(l）A single spatial orientation, the same throughout all spacetime (three Euler angles) (2)The arbitrary world line of the origin of space coordinates (three functions of time)</td><td>(I）A single spatial orientation, the same throughout all spacetime (three Euler angles) (2） The location of the origin of coordinates (four numbers) (3）The velocity of the origin of</td><td>All four functions of position x&quot;(s)</td></tr><tr><td>Under what conditions is“g and 2 are simultaneous”well-defined?</td><td>In general; it is a coordinate-free geometric concept</td><td>space coordinates (three numbers) Only after a choice of Lorentz frame has been made;“simultaneity”depends on the frame&#x27;s velocity</td><td>Only after arbitrary choice of time coordinate has been made</td></tr><tr><td>Under what conditions is“9 and 2 occur at same point in spaee”well- defined?</td><td>Only after choice of Galilean coordinates has been made</td><td>Only after choice of Lorentz coordinates has been made</td><td>Only after arbitrary choice of space Coordinates has been made</td></tr><tr><td>Under what conditions is“u and v, at different events,point in same direction&quot;well-defined?</td><td>Only if u and v are both spatial veciors((dt,u&gt;=(dt,v&gt;=0）；or if they lie in the same space slice and are arbitrary vectors; or if there exists a preferred route connecting their locations,along which to compare them by parallel.</td><td>Always</td><td>Only if u andv lie at events infinitesimally close together:or if there exists a preferred route (e.g.,a unique geodesic) connecting their locations,along which to compare them by parallel transport</td></tr><tr><td>Under what conditions is “the invariant distance between  and 2&quot; well-defined?</td><td>transport Only if gand  lie in the same space slice</td><td>Always</td><td>Only if and &amp;are sufliciently close together;or if there exists a unique preferred world line (e.g., a geodesic） linking them,along</td></tr></table>

Box 12.3 NEWTONIAN GRAVITY A_LA CARTAN,AND EINSTEINIAN GRAVITY: COMPARISON AND CONTRAST   

<table><tr><td>Property</td><td>Newton-Cartan</td><td>Einstein</td></tr><tr><td>Idea in brief (formulations of the equivalence principle of very different scope)</td><td>Laws of motion of free parti- cles in a local, freely falling,nonrotating frame are identical to Newton&#x27;s laws of motion as expressed in a gravity-free Galilean frame</td><td>Laws of physics in a local, freely falling,nonrotating frame are identical with the laws of physics as formulated in special relativity ina Lorentz frame</td></tr><tr><td>Idea even more briefly stated</td><td>Point mechanics simple in a local inertial frame</td><td>Everything simple ina local inertial frame</td></tr><tr><td>Consequence (tested to one part in 1011 by Roll-Krotkov- Dicke experiment)</td><td>Test particles of diverse composition started with same initial position and same initial velocity follow the sameworld line(&quot;definition of geodesic&quot;)</td><td>Test particles of diverse composition started with same initial position and same initial velocity follow the same world line(&quot;definition of geodesic&quot;)</td></tr><tr><td>Another consequence</td><td>In every local region,there existsa local frame(&quot;freely falling frame&quot;) in which all geodesics appear straight (all r =0）</td><td>In every local region there existsa local frame(freely falling frame&quot;) in which all geodesics appear straight (all ra =0）</td></tr><tr><td>Consequence of way light rays travel in real physical world?</td><td>Disregarded or evaded.All light rays have same velocity? Speed depend on motion of source? Speed depend on motion of observer? Possible to move fast enough to catch up with a light ray?No satisfactory position on any of these</td><td>Spacetime always and every- where has local Lorentz character</td></tr><tr><td>Summary of spacetime structure</td><td>Stratified into spacelike slices;geometry in each slice Euclidean;each slice charac- terized by value of universal time(geodesic parameter); displacement of one slice with respect to another not spec- ified;no such thing as a</td><td>No stratification.Well- defined interval between every event and every nearby event; spacetime has everywhere local Lorentz character,with one local frame (specific space and time axes) as good as another (other space and time axes);“homogeneous”rather</td></tr><tr><td>This structure expressed in mathematical language</td><td>rαu&#x27;s. yes: spacetime metric Surno: 冲 r&#x27;00= (i = 1,2.3); 2x</td><td>existence;all derived from （gB rauv = gaB 1 2 axu</td></tr></table>

![](images/fa987383bc8e4548c43742fcaa2166350e1ea9e828f2d8140066566b0532a3a0.jpg)  
Figure 12.1. The coordinate system carried by an orbital laboratory as it moves in a circular orbit about the Earth,

# Exercise 12.4. CONNECTION COEFFICIENTS FOR ROTATING, ACCELERATING COORDINATES

Beginning with equation (12.4) for the connection coeffcients of a Galilean coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ ，derive the connection coeffcients （12.14） of the coordinate system $\left\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \right\}$ of equations (l2.l3). From this, verify that (l2.15) are necessary and suffcient for $\left\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \right\}$ to be Galilean.

# Exercise 12.5. EINSTEIN'S ELEVATOR

Use the formalism of this chapter to discuss “Einstein's elevator"-i.e., the equivalence of “gravity” to an acceleration of one's reference frame.Which aspects of"gravity”are equivalent to an acceleration, and which are not?

# Exercise 12.6. GEODESIC DEVIATION ABOVE THE EARTH

A manned orbital laboratory is put into a circular orbit about the Earth [radius of orbit $\mathit { \Theta } = { \mathfrak { r } } _ { 0 } .$ angular velocity $\backsimeq \omega = ( M / { r _ { 0 } } ^ { 3 } ) ^ { 1 / 2 }$ -why?]. An astronaut jetisons a bag of garbage and watches it move along its geodesic path. He observes its motion relative to (non-Galilean) space coordinates $\{ x ^ { j ^ { \prime } } ( \mathcal { P } ) \}$ which-see Figure l2.1-(l) are Euclidean at each moment of universal time $[ ( \partial / \partial x ^ { j ^ { \prime } } ) \cdot ( \partial / \partial x ^ { k ^ { \prime } } ) = \delta _ { j k } ] ,$ (2) have origin at the laboratory's center,(3) have $\partial / \partial x ^ { \prime }$ pointing away from the Earth,(4） have $\hat { \boldsymbol { d } } / \hat { \boldsymbol { d } } \boldsymbol { x } ^ { \prime }$ and $\partial / \partial y ^ { \prime }$ in the plane of orbit. Use the equation of geodesic deviation to calculate the motion of the garbage bag in this coordinate system. Verify the answer by examining the Keplerian orbits of laboratory and garbage. Hints: (1) Calculate $R ^ { \alpha ^ { \prime } } { } _ { \beta ^ { \prime } \gamma ^ { \prime } \delta ^ { \prime } }$ in this coordinate system by atrivialtransformation of tensorial components. (2) Use equation (12.14) to calculate $\boldsymbol { T ^ { \alpha ^ { \prime } } } _ { \beta ^ { \prime } \gamma ^ { \prime } }$ at the center of the laboratory (i.e, on the fiducial geodesic).

# $\$ 123$ .GEOMETRIC, COORDINATE-FREE FORMULATION OF NEWTONIAN GRAVITY

To restate Newton's theory of gravity in coordinate-independent, geometric language is the principal goal of this chapter. It has been achieved,thus far,with extensive assistance from a special class of coordinate systems, the Galilean coordinates.To climb out of Galilean coordinates and into completely coordinate-free language is straightforward in principle. One merely passes from index notation to abstract notation.

ExmpleRe ${ \varGamma ^ { 0 } } _ { \alpha \beta } = 0$ of Galilean coordinates.

Solution: Write ${ \Gamma ^ { 0 } } _ { \alpha \beta } = - \langle \nabla _ { \beta } d t , \pmb { e } _ { \alpha } \rangle$ the vanishingof this forall $\pmb { \alpha }$ means $\pmb { \nabla } _ { \beta } \pmb { d t } = 0$ for all $\beta$ ,which in turn means $\pmb { \nabla _ { u } } \pmb { d t } = 0$ for all $\pmb { u }$ In words: the gradient of universal time is covariantly constant.

By this process one can construct a set of coordinate-free statements about Newtonian spacetime $\left( \mathbf { B 0 X } \ 1 2 . 4 \right)$ that are completely equivalent to the standard, non-geometric version of Newton's gravitation theory. From standard Newtonian theory, one can deduce these geometric statements (exercise l2.7); from these geometric statements, regarded as axioms, one can deduce standard Newtonian theory (exercise 12.8).

Coordinate-free，geometric axioms for Newton's theory of gravity

# Exercise 12.7. FROM NEWTON TO CARTAN

From the standard axioms of Newtonian theory (last part of Box l2.4) derive the geometric axioms (first part of Box l2.4). Suggested procedure:Verify each of the geometric axioms by a calculation in the Galilean coordinate system. Make free use of the calculations and results in $\ S 1 2 . 1$

# EXERCISES

# Exercise 12.8. FROM CARTAN TO NEWTON

From the geometric axioms of Newtonian theory (first part of Box l2.4) derive the standard axioms (last part of Box l2.4). Suggested procedure: (l) Pick three orthonormal, spatial basis vectors $( \pmb { \mathscr { e } } _ { j }$ with $\begin{array} { r } { \pmb { e } _ { j } \cdot \pmb { e } _ { k } = \delta _ { j k } } \end{array} .$ at some event ${ \mathcal { P } } _ { 0 }$ Parallel transport each of them by arbitrary routes to all other events in spacetime.

(2）Use the condition $\mathcal { R } ( \pmb { u } , \pmb { n } ) \pmb { e } _ { j } = 0$ for all $\pmb { u }$ and $\pmb { n }$ [axiom (3)] and an argument like that in $\ S 1 1 . 5$ to conclude: (a) the resultant vector fields $\pmb { e _ { j } }$ are independent of the arbitrary transport routes.(b) $\pmb { \nabla _ { \pmb { e } _ { j } } } = 0$ for the resultant fields,and (c) $[ { \pmb e } _ { j } , { \pmb e } _ { k } ] = 0$

(3)Pick an arbitrary“time line”,which passes through each space slice (slice of constant $t )$ once and only once.Parametrize it by $t$ and select its tangent vector as the basis vector ${ \pmb { e } } _ { 0 }$ at each event along it. Parallel transport each of these ${ \pmb { e } } _ { 0 }$ 's throughout its respective space slice by arbitrary routes.

(4) From axiom (4) conclude that the resultant field is independent of the transport routes; also show that the above construction process guarantees $\pmb { \nabla } _ { j } \pmb { e } _ { 0 } = \pmb { \nabla } _ { 0 } \pmb { e } _ { j } = 0$

(5)Show that $[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] = 0$ for all pairs of the four basis-vector fields,and conclude from this that there exists a coordinate system("Galilean coordinates") in which $\pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha }$ (see $\ S 1 1 . 5$ and exercise 9.9).

(6) Show that in this coordinate system $\pmb { e } _ { j } \cdot \pmb { e } _ { k } = \delta _ { j k }$ everywhere (space coordinates are Euclidean). and the only nonzero components of the connection coeficient are $T ^ { j } { _ { 0 0 } }$ ；here axioms (6) and (2） will be helpful.

(7)From the self-adjoint property of the Jacobi curvature operator (axiom 7) show that $R _ { 0 k 0 } ^ { j } = R _ { 0 j 0 } ^ { k }$ showatisos ${ T ^ { j } } _ { 0 0 , k } = { T ^ { k } } _ { 0 0 , j }$ and from this conclude that there exists a potential such that $T ^ { j } { } _ { 0 0 } = \Phi _ { . j } .$

(8) Show that the geometric field equation (axiom 5） reduces to Poisson's equation ²Φ = 4mp.

(9) Show that the geodesic equation for free fall (axiom 8) reduces to the Newtonian equation of motion $d ^ { 2 } x ^ { j } / d t ^ { 2 } + \dot { \phi } _ { { \scriptsize ; } } = 0$

(continued on page 302)

# Box 12.4 NEWTONIAN GRAVITY: GEOMETRIC FORMULATION CONTRASTED WITH STANDARD FORMULATION

# Geometric Formulation

Newton's theory of gravity and the properties of Newtonian spacetime can be derived from the following axioms. (For derivation see exercise 12.8.)

(l） There exists a function $t$ called“universal time",and a symmetric covariant derivative $\blacktriangledown$ (with associated geodesics, parallel transport law, curvature operator, etc.).

(2) The 1-form $\pmb { d t }$ is covariantly constant; ie.,

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { d t } = 0 \mathrm { ~ f o r ~ a l l ~ } \pmb { u } .
$$

[Consequence: if $\pmb { w }$ is a spatial vector field (i.e., $\pmb { w }$ lies everywhere in a surface of constant $t$ i.e. $\langle d t , { \pmb w } \rangle = 0$ everywhere), then $\yen 12$ is also spatial for every $\pmb { u }$

$$
\begin{array} { r } { \langle d t , \nabla _ { u } w \rangle = \nabla _ { u } \langle \underbrace { d t , w } _ { \begin{array} { l } { \begin{array} { l } { \begin{array} { r } { \cdot } \end{array} } \end{array} } } - \langle \underbrace { \nabla _ { u } \ : d t } _ { \begin{array} { l } { \vert } \\ { \begin{array} { l } { \cdot } \end{array} } } , w \rangle = 0 . ] } \\ { \left[ 0 \mathrm { ~ a l w a y s } \right] } \end{array} \end{array} \end{array}
$$

(3） Spatial vectors are unchanged by parallel transport around infinitesimal closed curves; i.e.,

(4) All vectors are unchanged by parallel transport around infinitesimal, spatial, closed curves; i.e.,

(5）The Ricci curvature tensor, $R _ { \alpha \beta } \equiv R _ { \alpha \mu \beta } ^ { \mu }$ , has the form

$$
R i c c i = 4 \pi \rho \ d t \otimes \ d t ,
$$

where $\pmb { \rho }$ is the density of mass.

(6) There exists a metric“.”defined on spatial vectors only，which is compatible with the covariant derivative in this sense: for any spatial $\boldsymbol { \mathsf { \Sigma } }$ and $\pmb { v } ,$ and for any $\pmb { u }$ whatsoever,

$$
\nabla _ { \boldsymbol { u } } ( \boldsymbol { w } \cdot \boldsymbol { v } ) = ( \nabla _ { \boldsymbol { u } } \boldsymbol { w } ) \cdot \boldsymbol { v } + \boldsymbol { w } \cdot ( \nabla _ { \boldsymbol { u } } \boldsymbol { v } ) .
$$

[Note: axioms (l), (2),and (3) guarantee that such a spatial metric can exist; see exercise 12.9.]

(7）The Jacobi curvature operator $\mathcal { f } \left( \pmb { u } , \pmb { n } \right)$ , defined for any vectors ${ \pmb u } , { \pmb n } , { \pmb p }$ by

$$
\mathscr { f } ( u , n )  { \boldsymbol { p } } = \frac { 1 } { 2 } [ \mathscr { R } (  { \boldsymbol { p } } , \pmb { n } )  { \boldsymbol { u } } + \mathscr { R } (  { \boldsymbol { p } } , \pmb { u } )  { \boldsymbol { n } } ] ,
$$

is “self-adjoint” when operating on spatial vectors; i.e., (8)“Ideal rods” measure the lengths that are calculated with the spatial metric; "ideal clocks” measure universal time $t$ (or some multiple thereof); and “freely falling particles” move along geodesics of $\pmb { \triangledown }$ [Note: this can be regarded as a definition of “ideal rods,”“ideal clocks,” and “freely falling particles.”A more complete theory (e.g.，general relativity； see $\ S 1 6 . 4 )$ would predict in advance whether a given physical rod or clock is ideal, and whether a given real particle is freely falling.]

Note: For an alternative but equivalent set of axioms,see pp. lO6-lO7 of Trautman (1965).

# Standard Formulation

The following standard axioms are equivalent to the above.

(l） There exist a universal time $t .$ ，a set of Cartesian space coordinates $x ^ { j }$ (called “Galilean coordinates"),and a Newtonian gravitational potential $\pmb { \phi }$

(2） The density of mass $\rho$ generates the Newtonian potential by Poisson's equation,

$$
\nabla ^ { 2 } \Phi \equiv \frac { \partial ^ { 2 } \phi } { \partial _ { \cdot } x ^ { j } \partial x ^ { j } } = 4 \pi \rho .
$$

(3） The equation of motion for a freely fallng particle is

$$
\begin{array} { r } { \frac { d ^ { 2 } . { \bf \vec { r } } ^ { j } } { d t ^ { 2 } } + \frac { \partial \phi } { \partial x ^ { j } } = 0 . } \end{array}
$$

(4）“Ideal rods” measure the Galilean coordinate lengths:“ideal clocks”measure universal time.

# ExerciSe 12.9. SPATIAL METRIC ALLOWED BY OTHER AXIOMS

Show that the geometric axioms (1),(2),and (3) of Box 12.4 permit one to introduce a spatial metric satisfying axiom (6). Hint:Pick an arbitrary spatial basis $\{ \pmb { e } _ { i } \}$ at some event. Define it to be orthonormal. $\pmb { e } _ { \dag } \cdot \pmb { e } _ { \ b { k } } \equiv \delta _ { j k }$ .Extend this basis through all spacetime by the method used in (1) of exercise 12.8. Define $\pmb { e } _ { j } \cdot \pmb { e } _ { k } \equiv \delta _ { j k }$ everywhere in spacetime for this basis. Then prove that the resulting metric satisfies the compatibility condition of axiom (6).

# Exercise 12.10. SPACETIME METRIC FORBIDDEN BY OTHER AXIOMS

Show that in Newtonian spacetime it is impossible to construct a nondegenerate spacetime metric ${ \pmb g }$ .defined on all vectors,that is compatible with the covariant derivative in the sense that

$$
\nabla _ { \boldsymbol { u } } g ( \boldsymbol { n } , \boldsymbol { p } ) = g ( \nabla _ { \boldsymbol { u } } \boldsymbol { n } , \boldsymbol { p } ) + g ( \boldsymbol { n } , \nabla _ { \boldsymbol { u } } \boldsymbol { p } ) .
$$

Note: to prove this requires mastery of the material in Chapter 8 or 13; so study either 8 or 13 before tackling it. Hint: Assume that such a $\pmb { \mathscr { g } }$ exists. Show,by the methods of exercise 12.8,that in a Galilean coordinate system the spatial components $g _ { j k }$ are independent of position in spacetime. Then use this and the form of $R ^ { \alpha } { } _ { \beta \gamma \delta }$ in Galilean coordinates to prove $R _ { \mathrm { i 0 } k 0 }$ and $- R _ { 0 i k 0 }$ are not identical, a result that conflicts with the symmetries of the Riemann tensor [eq.(8.45)] in a manifold with compatible metric and covariant derivative.

# $\$ 12.5$ . THE GEOMETRIC VIEW OF PHYSICS: A CRITIQUE

The principle of general covariance has no forcible content

An important digression is in order.

“Every physical quantity must be describable by a (coordinate-free） geometric object,and the laws of physics must all be expressble as geometric relationships between these geometric objects.” This view of physics, sometimes known as the "principle of general covariance," pervades twentieth-century thinking. But does it have any forcible content? No, not at all, according to one viewpoint that dates back to Kretschmann(1917). Any physical theory originally written in a special coordinate system can be recast in geometric,coordinate-free language. Newtonian theory is a good example, with its equivalent geometric and standard formulations (Box l2.4). Hence,as a sieve for separating viable theories from nonviable theories, the principle of general covariance is useless.

Twentieth-century viewpoint judges a theory by simplicity of its geometric formulation

Einstein's theory of gravity is simple: Newton's is complex

But another viewpoint is cogent. It constructs a powerful sieve in the form of a slightly altered and slightly more nebulous principle:“Nature likes theories that are simple when stated in coordinate-free, geometric language."\* According to this principle, Nature must love general relativity,and it must hate Newtonian theory. Of all theories ever conceived by physicists, general relativity has the simplest, most elegant geometric foundation [three axioms: (l) there is a metric;(2) the metric is governed by the Einstein field equation ${ \pmb { G } } = 8 \pi { \pmb { T } } .$ ：(3）all special relativistic laws of physics are valid in local Lorentz frames of metric]. By contrast, what diabolically clever physicist would ever foist on man a theory with such-a complicated geometric foundation as Newtonian theory?

Of course,from the nineteenth-century viewpoint, the roles are reversed. It judged simplicity of theories by examining their coordinate formulations. In Galilean coordinates,Newtonian theory is beautifully simple.Expressed as differential equations for the metric coefficients in a specific coordinate system,Einstein's field 'equations (ten of them now!) are horrendously complex.

The geometric, twentieth-century view prevails because it accords best with experimental data (see Chapters 38-40). In Chapter l7 it will be applied ruthlessly to make Einstein's field equation seem compelling.

# CHAPTER 13

# RIEMANNIAN GEOMETRY: METRIC AS FOUNDATION OF ALL

Philosophy is written in this great book (by which 丨 mean the universe) which stands always open to our view,but it cannot be understood unless one first learns how to comprehend the language and interpret the symbols in which it is written,and its symbols are triangles,circlas,and other geometric figures, without which it is not humanly possible to comprehend even one word of it;without these one wanders in a dark labyrinth.

GALILEO GALILEI (1623)

This chapter is entirely Track 2.   
Chapters $\bullet - 1 1$ are necessary   
preparation for it. It will be   
needed as preparation for (1） the second half of Chapter 14 (calculation of curvature), and (2) the details,but not the message,of Chapter 15 (Bianchi identities).

$\$ 123.6$ (proper reference frame) will be useful throughout the applications of gravitation theory (Chapters 18-40).

Constraints imposed on spacetime by special relativity

# $\$ 13.1$ . NEW FEATURES IMPOSED ON GEOMETRY BY LOCAL VALIDITY OF SPECIAL RELATIVITY

Freely falling particles (geodesics) define and probe the structure of spacetime. This spacetime is curved. Gravitation is a manifestation of its curvature.So far,so good, in terms of Newton's theory of gravity as translated into geometric language by Cartan.What is absolutely unacceptable, however,is the further consequence of the Cartan-Newton viewpoint (Chapter l2): stratification of spacetime into slidable slices,with no meaning for the spacetime separation between an event in one slice and an event in another.

Of all the foundations of physics, none is more firmly established than special relativity;and of all the lessons of special relativity none stand out with greater force than these.(l） Spacetime,far from being stratified,is homogeneous and isotropic throughout any region small enough ("local region"） that gravitational tide-producing effects ("spacetime curvatures") are negligible. (2) No local experiment whatsoever can distinguish one local inertial frame from another. (3) The speed of light is the same in every local inertial frame. (4) It is not possible to give frame-independent meaning to the separation in time ("no Newtonian stratification").(S） Between every event and every nearby event there exists a frame-independent, coordinate-independent spacetime interval("Riemannian geometry"). (6) Spacetime is always and everywhere locally Lorentz in character("local Lorentz character of this Riemannian geometry").

What mathematics gives all these physical properties? A metric: a metric that is locally Lorentz ( $\mathfrak { S 8 } 1 3 . 2$ and l3.6).All else then follows. In particular, the metric destroys the stratified structure of Newtonian spacetime, as well as its gravitational potential and universal time coordinate. But not destroyed are the deepest features of Newtonian gravity: (l） the equivalence principle (as embodied in geodesic description of free-fall motion, $\ S \ S 1 3 . 3$ and 13.4); and (2） spacetime curvature (as measured by tidal effects. $\ S 1 3 . 5 )$

The skyscraper of vectors, forms, tensors (Chapter 9), geodesics, parallel transport, covariant derivative (Chapter lO), and curvature (Chapter Il） has rested on crumbling foundations-Newtonian physics and a geodesic law based on Newtonian physics.But with metric now on the scene,the whole skyscraper can be transferred to new foundations without a crack appearing. Only one change is necessary: the geodesic law must be selected in a new,relativistic way; a way based on metric $( \ S \ S 1 3 . 3$ and l3.4). Resting on metric foundations, spacetime curvature acquires additional and stronger properties (the skyscraper is redecorated and extended), which are studied in $\ S 1 3 . 5$ and in Chapters l4 and I5,and which lead almost inexorably to Einstein's field equation.

Metric: the instrument which imposes the constraints

# $\$ 12$ .METRIC

A spacetime metric: a curved spacetime metric; a locally Lorentz, curved spacetime metric. This is the foundation of spacetime geometry in the real, physical world. Therefore take a moment to recall what “metric” is in three contrasting languages.

In the language of elementary geometry.“metric” is a table giving the interval between every event and every other event $\mathbf { ( B o x ~ l 3 . l }$ and Figure l3.1). In the language of coordinates,“metric” is a set of ten functions of position, $g _ { \mu \nu } ( x ^ { \alpha } )$ ,such that the expression

$$
\varDelta s ^ { 2 } = - \varDelta \tau ^ { 2 } = g _ { \mu \nu } ( x ^ { \alpha } ) \varDelta x ^ { \mu } \varDelta x ^ { \nu }
$$

# Metric described in three languages

gives the interval between any event $x ^ { \alpha }$ and any nearby event $x ^ { \alpha } + 4 x ^ { \alpha }$ In the language of abstract differential geometry， metric is a bilinear machine, $\pmb { \sigma } \equiv ( \dots \dots \dots )$ .te produce a number ["scalar product ${ \pmb g } ( { \pmb u } , { \pmb v } ) \equiv ( { \pmb u } \cdot { \pmb v } ) ^ { * } ]$ out of two tangent vectors. $\pmb { u }$ and ${ \pmb v } .$

The link between the abstract. machine viewpoint and the concrete coordinate viewpoint is readily exhibited. Let the tangent vector

$$
\pmb { \xi } \equiv \pmb { \varDelta } \mathrm { r } ^ { \alpha } \pmb { e } _ { \alpha } = \pmb { \varDelta } \mathrm { r } ^ { \alpha } ( \hat { \partial } / \hat { c } \pmb { x } ^ { \alpha } )
$$

represent the displacement between two neighboring events. The abstract viewpoint gives

$$
\mathbf { 1 } \mathfrak { s } ^ { : } \equiv \boldsymbol { \xi } \cdot \boldsymbol { \xi } \equiv g ( \mathbf { 1 } \mathfrak { x } ^ { \mu } \pmb { e } _ { \mu } . \mathbf { \mathcal { A } } \mathfrak { x } ^ { : \prime } \pmb { e } _ { \nu } ) = \mathbf { 4 } \mathfrak { x } ^ { \mu } \mathbf { 3 } \mathfrak { x } ^ { \nu } \pmb { g } ( \pmb { e } _ { \mu } . \pmb { e } _ { \nu } )
$$

(tontinued on page 310)

# Box 13.1 METRIC DISTILLED FROM DISTANCES

# Raw Data on Distances

Let the shape of the earth be described as in Figure l3.l,by giving distances between some of the principal identifiable points: buoys. ships, icebergs,lighthouses, peaks, and flags: points to a total of $n = 2 \times 1 0 ^ { 7 }$ . The total number of distances to be given is $n ( n - 1 ) / 2 = 2 \times 1 0 ^ { 1 4 }$ .With 2Oo distances per page of printout, this means

<table><tr><td>First point</td><td>Second point</td><td>Distance (Nautical miles)</td><td>First point</td><td>Seco pr</td></tr><tr><td>9,316,434</td><td>14,117,103</td><td>1410.316</td><td>9,316.434</td><td></td></tr><tr><td>9.316,434</td><td>14.117,104</td><td>1812.717</td><td>9,316,434</td><td></td></tr><tr><td>9,316,434</td><td>14,117,105</td><td>1629.291</td><td>9.3</td><td></td></tr><tr><td>921/4</td><td>14 </td><td></td><td></td><td></td></tr></table>

$1 0 ^ { 1 2 }$ pages weighing $6 \ { \tt g }$ each, or $6 \times 1 0 ^ { 6 }$ metric tons of data. With 6 tons per truck this means $1 0 ^ { 6 }$ truckloads of data; or with one truck passing by every 5 seconds, $5 \times 1 0 ^ { 6 }$ seconds or 2 months of night and day traffc to get in the data.

![](images/0bb12ea6a8b469300578dd8841d409944557902a55b9f23f1cc5c3d9a06ffd19.jpg)

# First Distillation: Distances to Nearby Points Only

Get distances between faraway points by adding distances covered on the elementary short legs of the trip.Boil down the table of distances to give only the distance between each point and the hundred nearest points. Now have $1 0 0 ~ n = 2 \times 1 0 ^ { 9 }$ distances, or $2 \times 1 0 ^ { 9 } / 2 0 0 = 1 0 ^ { 7 }$ pages of data, or 60 tons of records, or l0 truckloads..

# Second Distillation: Distances Between Nearby Points in Terms of Metric

Idealize the surface of the earth as smooth. Then in any sufficiently limited region the geometry is Euclidean. This circumstance has a happy consequence. It is.enough to know a few distances between the nearby points to be able to determine all the

distances between the nearby points.Locate point 2 so that (lO2) is a right triangle; thus, $( 1 2 ) ^ { 2 } = ( 1 0 ) ^ { 2 } + ( 2 0 ) ^ { 2 }$ Consider a point 3 close to 0. Define

$$
x ( 3 ) = ( 1 3 ) - ( 1 0 )
$$

and

$$
y ( 3 ) = ( 2 3 ) - ( 2 0 ) .
$$

Then the distance (O3) does not have to be supplied independently; it can be calculated from the formula\*

$$
( 0 3 ) ^ { 2 } = [ x ( 3 ) ] ^ { 2 } + [ y ( 3 ) ] ^ { 2 } .
$$

Similarly for a point 4 and its distance (O4) from the local origin O. Similarly for the distance $( m n )$ between any two points $m$ and $n$ that are close to 0:

$$
( m n ) ^ { 2 } = [ x ( m ) - x ( n ) ] ^ { 2 } + [ y ( m ) - y ( n ) ] ^ { 2 } .
$$

Thus it is only needful to have the distance $( 1 m )$ (from point l） and $( 2 m )$ (from point 2) for each point m close to 0 $( m = 3 , 4 , \dots , N + 2 )$ to be able to work out

$$
\left( \begin{array} { l } { \mathrm { v o f u m e ~ o f } } \\ { n \mathrm { - d i m e n s i o n a l } } \\ { \mathrm { s i m p l e x } } \\ { \mathrm { s p a n n e d ~ b y } } \\ { ( n + 1 ) \mathrm { p o i n t s } } \end{array} \right) = \left( \frac { ( - 1 ) ^ { n + 1 } } { 2 ^ { n } } \right) ^ { 1 / 2 } \frac { 1 } { n ! } \left| \begin{array} { l l l l l l } { 0 } & { 1 } & { 1 } & { 1 } & { \ldots } & { 1 } \\ { 1 } & { 0 } & { ( 0 1 ) ^ { 2 } } & { ( 0 2 ) ^ { 2 } } & { \ldots } & { ( 0 n ) ^ { 2 } } \\ { 1 } & { ( 1 0 ) ^ { 2 } } & { 0 } & { ( 1 2 ) ^ { 2 } } & { \ldots } & { ( 1 n ) ^ { 2 } } \\ { \ldots } & { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { 1 } & { ( n 0 ) ^ { 2 } } & { ( n 1 ) ^ { 2 } } & { ( n 2 ) ^ { 2 } } & { \ldots } & { 0 } \end{array} \right|
$$

$$
\begin{array} { c } { { \mathrm { a r e a } = \big \{ s \big [ s - ( 0 1 ) \big ] \big [ s - ( 0 2 ) \big ] \big [ s - ( 1 2 ) \big ] \big \} ^ { 1 / 2 } . } } \\ { { 2 s = ( 0 1 ) + ( 0 2 ) + ( 1 2 ) . } } \end{array}
$$

for the area of a triangle. Conversely. if the four points are to remain in two-dimensional Euchdean space.the tetrahedron must collapse to zero volume. This requirement supplies one condition on the one distance (O3).It simplifies the discussion of this condition to take (O3)smalland(IO2)to be a right triangle. as above. However. the general principle i、 independent of such approximations.and follows directly from the extended Hero-Tartaglia formula. It is enough in a locally Euclidean or Lorentz space of $n$ dimensions to have laid down $( n + 1 )$ fiducial points $0 , 1 . 2 . \dots n$ and to know the distance of every other point $j , k , \dots$ from these fiducial points. in order to be able to calculate the distance of these pointsj. k...from one another(distances between nearby points in terms of coordinates": metric as distilation of distance data).

its distance from every point $_ n$ close to 0. The prescription to determine the $N ( N - 1 ) / 2$ distances between these $N$ nearby points can be reexpressed to advantage in these words: (l) each point has two coordinates, $x$ and $y \cdot$ and (2) the distance is given in terms of these coordinates by the standard Euclidean metric; thus

$$
( \varDelta s ) ^ { 2 } = ( \varDelta x ) ^ { 2 } + ( \varDelta y ) ^ { 2 } .
$$

Having gone this far on the basis of“distance geometry” (for more on which,see Robb i9i4 and l936),one can generalize from a smallregion (Euclidean) to a large region (not Euclidean). Introduce any arbitrary smooth pair of everywhere-independent curvilinear coordinates $x ^ { k }$ ,and express distance, not only in the immediate neighborhood of the point O, but also in the immediate neighborhood of every point of the surface (except places where one has to go to another coordinate patch;at least two patches needed for 2-sphere) in terms of the formula

$$
d s ^ { 2 } = g _ { j k } d x ^ { j } d x ^ { k } .
$$

Thus out of the table of distances between nearby points one has distilled now five numbers per point (two coordinates, $x ^ { 1 } , x ^ { 2 }$ , and three metric coefficients, $g _ { 1 1 } , g _ { 1 2 } =$ $g _ { 2 1 }$ and $g _ { 2 2 } )$ ，down bya factor of $1 0 0 / 5 = 2 0 $ from what one had before (now 3 tons of data,or half a truckload).

# Third Distillation: Metric Coefficients Expressed as Analytical Functions of Coordinates

Instead of giving the three metric coefficients at each of the $2 \times 1 0 ^ { 7 }$ points of the surface,give them as functions of the two coordinates $x ^ { 1 } , x ^ { 2 }$ ,in terms of a power series or an expansion in spherical harmonics or otherwise with some modest number, say l00,of adjustable coefficients. Then the information about the geometry itself (as distinct from the coordinates of the $2 \times 1 0 ^ { 7 }$ points located on that geometry) is caught up in these three hundred coefficients, a single page of printout. Goodbye to any truck!In brief,metric provides a shorthand way of giving the distance between every point and every other point-but its role,its justification and its meaning lies in these distances and only in these many distances.

![](images/775ed2c40f3f70628979759e07c9c6ed380163a084588ec8794bf1a65227c8c6.jpg)  
Figure 13.1. 1 Distances determine geometry.Upper left: Sufciently great tidal forces,applied to theearth with tailored timing,have deformed it to the shape of a tear drop.Lower left: This tear drop is approximated by apolyhedron built out of triangles (skeleton geometry").The approximation can be madearbitrarily goodby making the number of triangles sufciently great and the size of each sufficiently small. Upper right:The geometry in each triangle is Euclidean: giving the three edge lengths fixes all the features of the figure,including the indicated angle.Lower right: The triangles that belong to a given vertex, laid out on a fat surface,fail to meet.The deficit angle measures the amount of curvature concentrated at that vertex on the tear-drop earth. The sum of these deficit angles for all vertices of the tear drop equals $4 \pi$ .This“Gauss-Bonnet theorem”is valid for any figure with the topology of the 2-sphere； for the simplest figure of all,a tetrahedron,four vertices with a deficit angle at each of $\mathfrak { l } 8 0 ^ { \circ }$ are needed-3 triangles $\times 6 0 ^ { \circ }$ per triangle available $= 1 8 0 ^ { \circ }$ deficit.In brief.the shape of the tear drop,in the given skeleton-geometry approximation,is determined by its 50 visible edge lengths plus.say,32 more edge lengths hidden behind the figure,oratotal of82 edge lengths,and by nothing more("distances determine geometry")."Metric" tells the distance between every point and every nearby point. If volcanic action raises Rejkjavik,the distances between that Icelandic capital and nearby points increase accordingly: distances again reveal shape.Conversely,that there is not a great bump on the earth in the vicinity of Iceland,and that the earth does not now have a tear-drop shape,can be unambiguously established byanalyzing the pattern of distances from point to point in a sufficiently well-distributed network of points,with no call for any observations other than measurements of distance.

for the interval between those events: comparison with the coordinate viewpoint [equation (13.1)] reveals

Covariant components of metric

$$
g _ { \mu \nu } = g ( e _ { \mu } , e _ { \nu } ) = e _ { \mu } \cdot e _ { \nu }
$$

"Line element"' compared with “metric as bilinear machine"

(standard equation for calculating components of a tensor).

Just as modern differential geometry replaces the old style“differential” df by the “differential form”df(Box 2.3,page 63), so it also replaces the old-style “line element"

$$
d s ^ { 2 } = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } = ( { \mathrm { " i n t e r v a l ~ b e t w e e n ~ } } x ^ { \alpha } { \mathrm { ~ a n d ~ } } x ^ { \alpha } + d x ^ { \alpha } { \mathrm { " ) } }
$$

by the bilinear machine ("metric tensor")

$$
g \equiv d s ^ { 2 } \equiv g _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu } .
$$

Metric produces a correspondence between 1-forms and tangent vectors

The output ${ \pmb g } ( { \pmb \xi } , { \pmb \xi } )$ of this machine,for given displacement-vector input, is identical to the old-style interval. Hence, $d s ^ { 2 } = g _ { \mu \nu } \ : d x ^ { \mu } \otimes d x ^ { \nu }$ represents the interval of an unspecified displacement; and the act of inserting $\pmb { \xi }$ into the slots of $\pmb { d } \pmb { s } ^ { 2 }$ is the act of making explicit the interval $g ( \xi , \xi ) = g _ { \mu \nu } \ : \varDelta x ^ { \mu } \ : \varDelta x ^ { \nu }$ of an explicit displacement.

In curved spacetime with metric, just as in flat spacetime with metric $( \ S 2 . 5 )$ ,a particular 1-form $\widetilde { \pmb { u } }$ corresponds to any given tangent vector $\pmb { u }$

("representation of the same physical quantity in the two alternative versions of vector and 1-form”;"corresponding representations”as $( _ { 0 } ^ { 1 } )$ -tensor and as $\ l ^ { ( 0 ) }$ -tensor). Example: the 1-form $\widetilde { \pmb { u } }$ corresponding to a basis vector $\pmb { \mu } = \pmb { e } _ { \alpha }$ has components

$$
\begin{array} { r l } & { \boldsymbol { u } _ { \beta } = \langle \widetilde { \pmb { u } } , \pmb { e } _ { \beta } \rangle \equiv g ( \pmb { u } , \pmb { e } _ { \beta } ) = \pmb { g } ( \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ) = \pmb { g } _ { \alpha \beta } ; } \\ & { \left[ \mathrm { s t a n d a r d ~ w a y ~ } \right] \overset { \mathrm { \scriptsize ~ \textstyle ~ \displaystyle ~ \displaystyle ~ } } { \longrightarrow } \left[ \begin{array} { l } { \qquad \qquad \mathrm { \textstyle ~ \displaystyle ~ \sum ~ } _ { [ \mathrm { \scriptsize ~ e q u a t i o n ~ ( 1 \cdot ~ c ) } ] } } \\ { \qquad \mathrm { \textstyle ~ \displaystyle ~ [ b y ~ } \pmb { u } = \pmb { e } _ { \alpha } ] } \end{array} \right. } \\ & { \qquad \mathrm { \quad ~ \displaystyle ~ } [ \mathrm { d e f i n i t i o n ~ } ( 1 3 . 5 ) ] . } \end{array}
$$

thus

Also as in flat spacetime $( \ S 3 . 2 )$ ,a tensor can accept either a vector or a 1-form into any given slot

$$
\pmb { S } ( \widetilde { \pmb { u } } , \pmb { \sigma } , \pmb { v } ) \equiv \pmb { S } ( \pmb { u } , \pmb { \sigma } , \pmb { v } ) .
$$

Lowering indices

Equivalently,in component language, the indices of a tensor can be lowered with the covariant components of the metric

$$
\begin{array} { r } { S _ { \alpha } { } ^ { \beta } { } _ { \gamma } = S ( \pmb { e } _ { \alpha } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = S ( \tilde { \pmb { e } } _ { \alpha } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = S ( g _ { \alpha \mu } \omega ^ { \mu } , \omega ^ { \beta } , \pmb { e } _ { \gamma } ) = g _ { \alpha \mu } S ^ { \mu \beta } { } _ { \gamma } , } \\ { \dot { \mathrm { ~ \ ` ~ } } [ \operatorname* { d e f i n i t i o n ~ o f ~ } S _ { \alpha } { } ^ { \beta } { } _ { \gamma } ] } \end{array}
$$

The basis vectors $\{ \pmb { \mathscr { e } } _ { \alpha } \}$ can be chosen arbitrarily at each event. Therefore the corresponding components $g _ { \alpha \beta }$ of the metric are quite arbitrary (though symmetric: $g _ { \alpha \beta } = g _ { \beta \alpha } )$ . But the mixed components $g ^ { \alpha } { } _ { \beta }$ are not arbitrary. In particular,equations (13.5) and (13.7) imply

$$
\pmb { g } ( \widetilde { \pmb { u } } , \pmb { v } ) \equiv \pmb { g } ( \pmb { u } , \pmb { v } ) \equiv \langle \widetilde { \pmb { u } } , \pmb { v } \rangle .
$$

Therefore one concludes that the metric tensor in mixed representation is identical with the unit matrix:

Mixed and contravariant components of metric

$$
g ^ { \alpha } { } _ { \beta } \equiv g ( \omega ^ { \alpha } , \pmb { e } _ { \beta } ) \equiv \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

This feature of the metric in turn fixes the contravariant components of the metric:

$$
\begin{array} { r } { g ^ { \alpha \mu } g _ { \mu \beta } = g ^ { \alpha } { } _ { \beta } = \delta ^ { \alpha } { } _ { \beta } ; } \\ { \mathrm { L } _ { [ \mathrm { ' l o w e r i n g } ] } } \end{array}
$$

i.e.,

$$
| | g ^ { \alpha \beta } | | \ \mathrm { i s \ t h e \ m a t r i x \ i n v e r s e \ o f \ } | | g _ { \alpha \beta } | | .
$$

This reciprocity enables one to undo the lowering of tensor indices (i.e.,raise indices) Raising indices with $g ^ { \alpha \beta }$ ：

$$
S ^ { \mu \beta } { } _ { \gamma } = \delta ^ { \mu } { } _ { \alpha } S ^ { \alpha \beta } { } _ { \gamma } = g ^ { \mu \nu } g _ { \nu \alpha } S ^ { \alpha \beta } { } _ { \gamma } = g ^ { \mu \nu } S _ { \nu } { } ^ { \beta } { } _ { \gamma } .
$$

The last two paragraphs may be summarized in brief:

（2） $\begin{array} { l } { { g _ { _ { \beta } } ^ { \alpha } = \delta ^ { \alpha } { } _ { \beta } ; } } \\ { { | | g ^ { \alpha \beta } | | = | | g _ { \alpha \beta } | | ^ { - 1 } ; } } \end{array}$ (3) tensor indices are lowered with $g _ { \alpha \beta }$ ； (4） tensor indices are raised with $g ^ { \alpha \beta }$

In this formalism of metric and index shufling,a big question demands attention: how can one tell whether the metric is locally Lorentz rather than locally Euclidean or locally something else? Of course, one criterion (necessary； not sufficient!） is dimensionality-a locally Lorentz spacetime must have four dimensions. (Recall the method of $\ S 1 . 2$ to determine dimensionality.） Confine attention, then, to fourdimensional manifolds. What else must one demand? One must demand that at every event $\mathcal { P }$ there exist an orthonormal frame (orthonormal set of basis vectors $\{ \pmb { \mathscr { e } } _ { \hat { \alpha } } \} )$ in which the components of the metric have their flat-spacetime form

$$
g _ { \hat { \alpha } \hat { \beta } } \equiv e _ { \hat { \alpha } } \cdot e _ { \hat { \beta } } = \eta _ { \alpha \beta } \equiv \mathrm { d i a g o n a l } ~ ( - 1 , 1 , 1 , 1 ) .
$$

To test for this is straightforward (exercise 13.1). (l） Search for a timelike vector $\pmb { u } \left( \pmb { u } \cdot \pmb { u } < 0 \right)$ . If none exist, spacetime is not locally Lorentz. If one is found, then (2） examine all non-zero vectors $\pmb { v }$ perpendicular to ${ \pmb u } .$ If they are all spacelike $( { \pmb v } \cdot { \pmb v } > 0 )$ , then spacetime is locally Lorentz. Otherwise it is not.

Metric must be locally Lorentz

# Exercise 13.1. TEST WHETHER SPACETIME IS LOCAL LORENTZ

Prove that the above two-step procedure for testing whether spacetime is locally Lorentz is valid: i.e.. prove that if the procedure says“yes." then there exists an orthonormal basis with $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \alpha \beta }$ at the event in question; if it says “no.” then no such basis exists.

# Exercise 13.2. PRACTICE WITH METRIC

A four-dimensional manifold with coordinates $v , r , \theta , \phi$ has line element (old-style notation)

$$
d s ^ { 2 } = { } - ( 1 - 2 M / r ) d { v ^ { 2 } } + 2 d { v } d r + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n ^ { 2 } } \theta d \phi ^ { 2 } ) ,
$$

corresponding to metric (new-style notation)

$$
d \pmb { \mathscr { s } } ^ { 2 } = - ( 1 - 2 M / r ) d \nu \otimes d v + d v \otimes d r + d r \otimes d v + r ^ { 2 } ( d \theta \otimes d \theta + \sin ^ { 2 } \theta d \phi \otimes d \phi ) ,
$$

where $M$ is a constant.

(a)Find the“covariant"components $g _ { \alpha \beta }$ and“contravariant"components $g ^ { \alpha \beta }$ of the metric in this coordinate system. [Answer: $g _ { v v } \dot { = } - ( 1 - 2 M / r )$ ， $g _ { v r } = g _ { r v } = 1$ ， $g _ { \theta \theta } = r ^ { 2 }$ ， $g _ { \phi \phi } = r ^ { 2 }$ $\sin ^ { 2 } \theta$ ； all other $g _ { \alpha \beta }$ vanish; $g ^ { v r } = g ^ { r v } = 1$ ， $g ^ { r r } = ( 1 - 2 M / r )$ ， $g ^ { \theta \theta } = r ^ { - 2 }$ ， $g ^ { \phi \phi } = r ^ { - 2 } \sin ^ { - 2 } \theta ,$ all other $g ^ { \alpha \beta }$ vanish.J

(b) Define a scalar field $t$ by

$$
t \equiv v - r - 2 M \ln [ ( r / 2 M ) - 1 ] .
$$

What are the covariant and contravariant components ( $\operatorname { \Pi } _ { \langle u _ { \alpha } \rangle }$ and $u ^ { \alpha }$ ）of the 1-form $\widetilde { \pmb { v } } \equiv { \pmb { d } } t ^ { \mathcal { T } } ;$ What is the squared length $\pmb { \upsilon } ^ { 2 } \equiv \pmb { \upsilon } \cdot \pmb { u }$ ,of the corresponding vector? Show that $\pmb { u }$ is timelike in the region $r > 2 M ,$ [Answer: $u _ { v } = 1$ ， $u _ { r } = - 1 / ( 1 \AA ^ { - 2 } M / r )$ ， $u _ { \theta } = u _ { \phi } = 0$ ； $u ^ { v } = - 1 / ( 1 -$ $2 M / r )$ ， $u ^ { r } = 0$ ， $u ^ { \theta } = u ^ { \phi } = 0$ ； $\begin{array} { r } { \pmb { \upsilon } ^ { 2 } = - 1 / ( 1 - 2 M / r ) . } \end{array}$ ]

(c) Find the most general non-zero vector orthogonal to $\bar { \pmb { \upsilon } }$ in the region $r > 2 M ,$ and show that it is spacelike. Thereby conclude that spacetime is locally Lorentz in the region $r > 2 M ,$ [Answer: Since $w \cdot u = w _ { \alpha } u ^ { \alpha } = - w _ { v } / ( 1 - 2 M / r )$ ， $w _ { v }$ must vanish, but $w _ { r } , ~ \boldsymbol { w } _ { \theta } , ~ \boldsymbol { w } _ { \phi }$ are arbitrary,and $w ^ { 2 } = ( 1 - 2 M / r ) w _ { r } ^ { ~ 2 } + r ^ { - 2 } w _ { \theta } ^ { ~ 2 } + r ^ { - 2 } \sin ^ { - 2 } \theta w _ { \phi } ^ { ~ 2 } > 0 . ]$

(d) Let $t , r , \theta , \phi$ be new coordinates for spacetime.Find the line element in this coordinate system.[Answer:This is the“Schwarzschild”line element

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } .
$$

(e）Find an orthonormal basis,for which $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \alpha \beta }$ in the region $r > 2 M$ [Answer:$\bullet _ { \widehat { 0 } } \equiv ( 1 - 2 M / r ) ^ { - 1 / 2 } \partial / \partial t$ ， $\begin{array} { r } { \pmb { e } _ { \hat { r } } \equiv ( 1 - 2 M / r ) ^ { 1 / 2 } \partial / \hat { \sigma } r } \end{array}$ ， $\pmb { e } _ { \hat { \theta } } \equiv r ^ { - 1 } \partial / \partial \theta$ ， $\pmb { e } _ { \hat { \phi } } = ( r \sin \theta ) ^ { - 1 } \hat { c } / \partial \phi . ]$

# $\$ 123.3$ .CONCORD BETWEEN GEODESICS OF CURVED SPACETIME GEOMETRY AND STRAIGHT LINES OF LOCAL LORENTZ GEOMETRY

More could be said about the mathematical machinery and physical implications of "metric,” but an issue of greater urgency presses for attention. What has metric (or spacetime interval) to do with geodesic (or world line of test particle)? Answer:

Two mathematical objects ("straight line in a local Lorentz frame” and“geodesic of the over-all global curved spacetime geometry") equal to the same physical object ("world line of test particle") must be equal to each other ("condition of consistency"). As a first method to spell out this consistency requirement, examine the two mathematical representations of the world line of a test particle in the neighborhood of a given event $\mathcal { P } _ { 0 }$ . The local-Lorentz representation says:

“Pick a local Lorentz frame at $\mathcal { P } _ { 0 }$ [As spelled out in exercise 13.3,such a local Lorentz frame is the closest thing there is to a global Lorentz frame at $\mathcal { P } _ { 0 }$ ；i.e., it is a coordinate system in which

$$
\begin{array} { r l } & { \mathrm {  { \mathcal E } } _ { \alpha \beta } (  { \mathcal P } _ { 0 } ) = \eta _ { \alpha \beta } \mathrm {  { \left( \mathrm { \mathrm { H a t } } \mathrm { - } s p a c e t i m e \mathrm { \ m e t r i c } \right) } } , } \\ & { \mathrm {  { \mathcal E } } _ { \alpha \beta , \gamma } (  { \mathcal P } _ { 0 } ) = 0 , } \end{array}
$$

$g _ { \alpha \beta , \gamma \delta } ( \mathcal { P } _ { 0 } ) \neq 0$ except in special cases, such as flat space.]

The world line in that frame has zero acceleration,

Local-Lorentz description of straight lines

$$
d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } = 0 \mathrm { ~ a t ~ } \hat { \mathcal { P } } _ { 0 } \mathrm { ~ ( ^ { * } s t r a i g h t \mathrm { - } l i n e ~ e q u a t i o n " ) , }
$$

where $\tau$ is proper time as measured by the particle's clock.”

The geodesic representation says

“In the local Lorentz frame, as in any coordinate frame, the world line satisfies the geodesic equation

Geodesic description of straight lines

$$
d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } + { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } ( d x ^ { \beta } / d \tau ) ( d x ^ { \gamma } / d \tau ) = 0
$$

$\tau$ is an affine parameter because it is time as measured by the test particle's clock)." Consistency of the two representations for any and every choice of test particle (any and every choice of $d x ^ { \alpha } / d \tau$ at ${ \mathcal { P } } _ { 0 }$ ）demands

Condition of consistency: y = 0 in local Lorentz frame

i.e., it demands that every,local Lorentz frame is a local inertial frame. (On local inertial frames see $\ S 1 1 . 6 . )$ In such a frame,allocal effects of "gravitation” disappear. That is the physical shorthand for (13.18).

One does not have to speak in the language of a specific coordinate system when one demands identity between the geodesic (derived from the $\Gamma ^ { \alpha } { } _ { \beta \gamma } )$ and the straight line of the local Lorentz geometry $( g _ { \mu \nu } )$ . The local Lorentz specialization of coordinates may be the most immediate way to see the physics ("no local effects of gravitation"), but it is not the right way to formulate the basic mathematical requirement in its full generality and power. The right way is to demand

$$
\begin{array} { r } { \pmb { \nabla } \pmb { g } = 0 ( ^ { \mathfrak { c } \mathfrak { c } } \mathrm { c o m p a t i b i l i t y ~ o f ~ } \pmb { g } \mathrm { ~ a n d ~ } \pmb { \nabla } ^ { \prime \prime } ) . } \end{array}
$$

Stated in the language of an arbitrary coordinate system, this requirement reads

Consistency reformulated: $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$

$$
g _ { \alpha \beta ; \gamma } \equiv \frac { \partial g _ { \alpha \beta } } { \partial x ^ { \gamma } } - { \Gamma ^ { \mu } } _ { \alpha \gamma } g _ { \mu \beta } - { \Gamma ^ { \mu } } _ { \beta \gamma } g _ { \alpha \mu } = 0 .
$$

That this covariant requirement is fulfilled in every coordinate system follows from its validity in one coordinate system: a local Lorentz frame. (The first term in this equation,and the last two terms,are separately required to vanish in the local Lorentz frame at point $\mathcal { P } _ { 0 }$ -and required to vanish by the physics.) From $\pmb { \nabla } _ { \pmb { g } } = 0$ ， One can derive both the abstract chain rule

$$
\nabla _ { u } \left( v \cdot w \right) = ( \nabla _ { u } v ) \cdot w + v \cdot ( \nabla _ { u } w )
$$

(Exercise 13.4） and the following equations for the connection coefficients in any frame in terms of (l) the metric coefficients, $g _ { \alpha \beta } = \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta }$ ,and (2） the covariant commutation coefficients

$$
c _ { \alpha \beta \gamma } \equiv c _ { \alpha \beta } ^ { \mu } g _ { \mu \gamma } \equiv \langle \pmb { \omega } ^ { \mu } , [ \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ] \rangle g _ { \mu \gamma }
$$

of that frame:

$$
\begin{array} { c } { { T ^ { \alpha } { } _ { \beta \gamma } = g ^ { \alpha \mu } { \cal T } _ { \mu \beta \gamma } \qquad \mathrm { ( d e f n i t i o n ~ o f } ~ { \cal T } _ { \mu \beta \gamma } \mathrm { ) , } } } \\ { { { } } } \\ { { { \cal T } _ { \mu \beta \gamma } = \displaystyle { \frac { 1 } { 2 } \left( g _ { \mu \beta , \gamma } + c _ { \mu \beta \gamma } + g _ { \mu \gamma , \beta } + c _ { \mu \gamma \beta } - g _ { \beta \gamma , \mu } - c _ { \beta \gamma \mu } \right) } } } \\ { { { } } } \\ { { { } = \displaystyle { \frac { 1 } { 2 } \left( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } \right) } ~ \mathrm { i n ~ a n y ~ c o o r d i n a t e ~ f r a n } } } \end{array}
$$

(See Exercise 13.4).

Equations (13.23) are the connection coefficients required to make the geodesics of curved spacetime coincide with the straight lines of the local Lorentz geometry. And they are fixed uniquely; no other choice of connection coefficients will do the job!

Summary: in curved spacetime with a local Lorentz metric,the following seemingly different statements are actually equivalent: (l） the geodesics of curved spacetime coincide with the straight lines of the local Lorentz geometry; (2) every local Lorentz frame [coordinates with $g _ { \alpha \beta } ( \mathcal { P } _ { 0 } ) = \eta _ { \alpha \beta } .$ $g _ { \alpha \beta , \gamma } ( \mathcal { P } _ { 0 } ) = 0 ]$ is a local inertial frame $\lbrack { T ^ { \alpha } { } _ { \beta \gamma } } ( \mathcal { P } _ { 0 } ) = 0 ] ,$ ：(3）the metric and covariant derivative satisfy the compatibility condition $\pmb { \nabla } _ { \pmb { g } } = 0$ ; (4) the covariant derivative obeys the chain rule (13.2O); (S) the connection coefficients are determined by the metric in the manner of equations (13.23).A sixth equivalent statement, derived in the next section, says (6) the geodesics of curved spacetime coincide with world lines of extremal proper time.

# EXERCISES

# Exercise 13.3. MATHEMATICAL REPRESENTATION OF LOCAL LORENTZ FRAME

By definition,a local Lorentz frame at a given event $\mathcal { P } _ { 0 }$ is the closest thing there to a global Lorentz frame. Thus, it should be a coordinate system with $g _ { \mu \nu } ( \mathcal { P } _ { 0 } ) = \eta _ { \mu \nu } ,$ and with as many derivatives of $g _ { \mu \nu }$ as possible vanishing at $\scriptstyle { \mathcal { P } } _ { 0 }$ Prove that there exist coordinates in which $g _ { \mu \nu } ( \mathcal { P } _ { 0 } ) = \eta _ { \mu \nu }$ and $g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } ) = 0$ ,but that $g _ { \mu \nu , \rho \sigma } ( \mathcal { P } _ { 0 } )$ cannot vanish in general. Hence, such coordinates are the mathematical representation of a local Lorentz frame.[Hint: Let $\{ x ^ { \alpha ^ { \prime } } ( { \mathcal { P } } ) \}$ be an arbitrary but specific coordinate system,and $\{ x ^ { \mu } ( { \mathcal { P } } ) \}$ be a local Lorentz frame,both with origins at $\mathscr { P } _ { 0 }$ . Expand the coordinate transformation between the two in powers of $x ^ { \mu }$

$$
x ^ { \alpha ^ { \prime } } = { M ^ { \alpha } } _ { \mu } x ^ { \mu } + \frac { 1 } { 2 } { N ^ { \alpha } } _ { \mu \nu } x ^ { \mu } x ^ { \nu } + \frac { 1 } { 6 } { P ^ { \alpha } } _ { \mu \nu \rho } x ^ { \mu } x ^ { \nu } x ^ { \rho } + \ldots ;
$$

and use the transformation matrix $L ^ { \alpha ^ { \prime } } { } _ { \mu } \equiv \hat { \sigma } x ^ { \alpha ^ { \prime } } / \hat { \sigma } x ^ { \mu }$ to get $g _ { \mu \nu } ( \mathcal { P } _ { 0 } )$ ， $g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } )$ ,and $g _ { \mu \nu , \rho \sigma } ( \mathcal { P } _ { 0 } )$ in terms of $g _ { \alpha ^ { \prime } \beta ^ { \prime } }$ anditid $M ^ { \alpha } { } _ { \mu } , N ^ { \alpha } { } _ { \mu \nu } , P ^ { \alpha } { } _ { \mu \nu \rho } .$ Show that whatever $g _ { \alpha ^ { \prime } \beta ^ { \prime } }$ may be (so long as it is nonsingular, so exists!),one can choose the 16 constants $M ^ { \alpha } { } _ { \mu }$ to make $g _ { \mu \nu } = \eta _ { \mu \nu }$ (ten conditions)； one can choose the $4 \times 1 0 = 4 0$ constants $N ^ { \gamma } { } _ { \mu \nu }$ to make the $1 0 \times 4 = 4 0 \ : g _ { \mu \nu , \rho } ( \mathcal { P } _ { 0 } )$ vanish; but one cannot in general choose the $4 \times 2 0 =$ $8 0 ~ P ^ { \alpha } { } _ { \mu \nu \rho }$ to make the $1 0 \times 1 0 = 1 0 0 g _ { \mu \nu , \rho \sigma }$ vanish.]

# Exercise 13.4. CONSEQUENCES OF COMPATIBILITY BETWEEN $\pmb { \mathscr { g } }$ AND $\blacktriangledown$

(a) From the condition of compatibility $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$ ,derive the chain rule (13.20). (b) From the condition of compatibility $\pmb { \bigtriangledown } \pmb { \mathfrak { g } } = 0$ and definitions (13.21) and (13.22), derive equation (13.23) for the connection coefficients. [Answer: See exercise 8.15,p. 216.]

# $\$ 123.4$ .GEODESICS AS WORLD LINES OF EXTREMAL PROPER TIME

In a local Lorentz frame, it is easy to distinguish a world line that is straight from one that is not. Position the Lorentz frame and so orient it that the starting point of the world line, $\boldsymbol { \mathcal { Q } }$ ,lies at the origin and the end point, $\it { \Omega } ^ { \it { \Delta } }$ ,lies at $x = 0 , y = 0$ ， $z = 0 , t = T .$ As an example of a nonstraight world line, consider passage at uniform velocity from $\boldsymbol { \mathcal { Q } }$ to point $\mathcal { P }$ .with coordinates $( \textstyle { \frac { 1 } { 2 } } T ; 0 , 0 , { \frac { 1 } { 2 } } R )$ and from there again with uniform velocity to point $\mathcal { B }$ The lapse of proper time from start to finish ("length of world line") is

![](images/449a44e24742d5cfad4a7304b1572d0fea19013b690a1d67d934399d9d58494c.jpg)

$$
\tau = ( T ^ { 2 } - R ^ { 2 } ) ^ { 1 / 2 } .
$$

Thus the lapse of proper time is diminished from its straight-line value,and diminished moreover for any choice of $R$ whatsoever, except for the zero or straight-line value $R = 0$ .As for this simple nonstraight curve, so also for any other nonstraight curve: the lapse of proper time between $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ is less than the straight-line lapse (Exercise 6.3). Thus, in flat spacetime,extremal length of world line is an indicator of straightness.

Any local region of the curved spacetime of the real, physical world is Lorentz in character. In this local Lorentz geometry, it is easy to set up Lorentz coordinates and carry out the extremal-length analysis just sketched to distinguish between a straight line and a nonstraight line:

$$
\begin{array} { l } { { \displaystyle \tau = \int _ { d } ^ { \varphi } d \tau = \int _ { d } ^ { \varphi \rangle } ( - \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } } \\ { { \displaystyle \quad = \left( \begin{array} { l } { { \mathrm { a ~ m a x i m u m ~ f o r ~ s t r a i g h t ~ l i n e } } } \\ { { \mathrm { a s ~ c o m p a r e d ~ t o ~ a n y ~ v a r i a n t ~ o f } } } \\ { { \mathrm { t h e ~ s t r a i g h t ~ l i n e } } } \end{array} \right) . } } \end{array}
$$

In flat spacetime,straight lines have extremal length

Extremal length in curved spacetime

Such a test for straightness can be carried out separately in each local Lorentz region along the world line, or, with greater efficiency, it can be carried out over many local Lorentz regions simultaneously, i.e.,over a region with endpoints $\boldsymbol { \mathcal { q } }$ and $\mathfrak { B }$ so widely separated that no single Lorentz frame can possibly contain them both. To carry out the analysis, one must abandon local Lorentz coordinates. Therefore introduce a general curvilinear coordinate system and find

$$
{ \begin{array} { r l } & { \tau = \int _ { \mathcal { a } } ^ { \varphi ^ { 3 } } d \tau = \int _ { \mathcal { a } } ^ { \varphi ^ { 3 } } ( - g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } \\ & { \qquad = { \Biggl ( } { \mathrm { i s ~ s t r a i g h t ~ i n ~ e a c h ~ l o c a l ~ L o r e n t l d ~ l i n e ~ t h a t } } } \\ & { \qquad = { \Biggl ( } { \mathrm { i s ~ s t r a i g h t ~ i n ~ e a c h ~ l o c a l ~ L o r e n t z ~ f r a m e } } } \\ & { \qquad { \mathrm { a l o n g ~ i t s ~ p a t h , ~ a s ~ c o m p a r e d ~ t o ~ a n y ~ } } ^ { * } { \mathrm { n e a r b y } } ^ { \prime } { \mathrm { , } } { \Biggr ) } . } \end{array} }
$$

In the real world,the path of extremal $\tau$ , being straight in every local Lorentz frame, must be a geodesic of spacetime.

Notice that the word “maximum” in equation (l3.24) has been replaced by "extremum” in the statement (13.25). When $\boldsymbol { \mathcal { Q } }$ and $\boldsymbol { \mathcal { B } }$ are widely separated, they may be connected by several different geodesics with differing lapses of proper time (Figure 13.2). Each timelike geodesic extremizes $\tau$ with respect to nearby deformations of itself, but the extremum need not be a maximum. When several distinct geodesics connect two events, the typical one is not a local maximum ("mountain peak") but a saddle point ("mountain pass") in such a diagram as Figure 13.2 0r 13.3.

Concord between locally straight lines (lines of extremal $\tau$ )and geodesics of curved spacetime demands that timelike geodesics have extremal proper length. If so, then any curve $x ^ { \mu } ( \lambda )$ between $\boldsymbol { \mathcal { Q } }$ (where $\lambda = 0$ and $\mathcal { B }$ (where $\lambda = 1$ ）that extremizes $\tau$ should satisfy the geodesic equation. To test for an extremal by comparing times, pick a curve suspected to be a geodesic,and deform it slightly but arbitrarily:

Along either curve the lapse of proper time is

$$
\tau = \int _ { d } ^ { \varepsilon \beta } d \tau = \int _ { 0 } ^ { 1 } \left( - g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } \right) ^ { 1 / 2 } d \lambda .
$$

At fixed $\lambda$ the metric coefficient $g _ { \mu \nu } [ x ^ { \alpha } ( \lambda ) ]$ differs from one curve to the other by

$$
\delta g _ { \mu \nu } \equiv g _ { \mu \nu } [ a ^ { \alpha } ( \lambda ) + \delta a ^ { \alpha } ( \lambda ) ] - g _ { \mu \nu } [ a ^ { \alpha } ( \lambda ) ] = { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } } \delta a ^ { \sigma } ( \lambda ) ;
$$

and the components $d x ^ { \prime } / d \lambda$ of the tangent vector differ by

$$
\delta \left( \frac { d x ^ { \nu } } { d \lambda } \right) \equiv \frac { d ( a ^ { \nu } + \delta a ^ { \nu } ) } { d \lambda } - \frac { d a ^ { \nu } } { d \lambda } = \frac { d } { d \lambda } ( \delta a ^ { \nu } ) .
$$

These changes in $g _ { \mu \nu }$ and $d x ^ { \nu } / d \lambda ,$ at fixed $\lambda$ , produce corresponding changes in the lapse of proper time in equation (13.27):

$$
\delta \tau = \int _ { 0 } ^ { 1 } \biggl \{ \frac { - g _ { \mu \nu } ( d a ^ { \mu } / d \lambda ) d ( \delta a ^ { \nu } ) / d \lambda - \frac { 1 } { 2 } ( g _ { \mu \nu , \sigma } \delta a ^ { \sigma } ) ( d a ^ { \mu } / d \lambda ) ( d a ^ { \nu } / d \lambda ) } { [ - g _ { \gamma \delta } ( d a ^ { \gamma } / d \lambda ) ( d a ^ { \delta } / d \lambda ) ] ^ { 1 / 2 } } \biggr \} d \lambda . \biggr .
$$

Integrate the first term by parts. Strike out the end-point terms, because both paths must pass through $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ $\delta a ^ { \mu } = 0$ at $\lambda = 0$ and $\lambda = 1$ ). Thus find

$$
\delta \tau = \int _ { \lambda = 0 } ^ { \lambda = 1 } f _ { \sigma } ( \lambda ) \ : \delta a ^ { \sigma } \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } d \lambda .
$$

Here the $f _ { \sigma }$ ("forceterms") in the integrand are abbreviations for the four expressions

$$
f _ { \sigma } ( \lambda ) = \frac { 1 } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } } \frac { d } { d \lambda } \frac { g _ { \sigma \nu } \frac { d a ^ { \nu } } { d \lambda } } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] ^ { 1 / 2 } } - \frac { \frac { 1 } { 2 } \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \frac { d a ^ { \mu } } { d \lambda } \frac { d a ^ { \nu } } { d \lambda } } { \left[ - g _ { \gamma \delta } \frac { d a ^ { \gamma } } { d \lambda } \frac { d a ^ { \delta } } { d \lambda } \right] } .
$$

An extremum is achieved,and the first-order change $\delta \tau$ vanishes for every first-order deformation $\delta a ^ { \sigma } ( \lambda )$ from an optimal path $x ^ { \sigma } = a ^ { \sigma } ( \lambda )$ , when the four quantities $f _ { \sigma }$ that multiply the $\delta a ^ { \sigma }$ all vanish. Thus one arrives at the four conditions

$$
f _ { \sigma } ( \lambda ) = 0
$$

for the determination of an extremal world line. (An alternative viewpoint on the extremization is spelled out in Figure 13.3.)

Suffcent these four equations are, but independent they are not, by reason of a “bead argument" (automatic vanishing of $\delta \tau$ for any set of changes that merely slide points, like beads, along an existing world line). The operation of mere “sliding of beads” implies the trivial change

$$
\delta a ^ { \sigma } ( \lambda ) = h ( \lambda ) \frac { d a ^ { \sigma } } { d \lambda } ,
$$

where $h ( \lambda )$ is an arbitrary function of position along the world line ("more sliding here than there"). Already knowing that this operation cannot change $\boldsymbol { \tau }$ oneis guaranteed that the integrand in (l3.30) must vanish when one inserts (13.33) for $\delta a ^ { \sigma }$ ； and must vanish, moreover, whatever choice is made for the arbitrary “magnitude of slide” factor $h ( \lambda )$ .This requirement implies and demands that the scalar product $f _ { \sigma } d a ^ { \sigma } / d \lambda$ must automatically vanish;or, otherwise stated,

$$
f _ { \sigma } \frac { d a ^ { \sigma } } { d \tau } = 0 .
$$

The argument applies,and this equation holds, whether one is or is not dealing with an optimal world line. An equation of this type, valid whether or not the world line is an allowable track for a free test particle (track of extremal lapse of proper

time),is known as an identity.Equation (13.34),an important identity in the realm of spacetime geodesics,is an appropriate forerunner for the Bianchi identities of Chapter 15: the most important identities in the realm of spacetime curvature.

The freedom that exists to “slide $\lambda$ -values along the world line”can be exploited to replace the arbitrary parameter $\lambda$ by the physically more interesting parameter of proper time itself,

$$
d \tau = \Big [ - g _ { \gamma \delta } { \frac { d a ^ { \gamma } } { d \lambda } } { \frac { d a ^ { \delta } } { d \lambda } } \Big ] ^ { 1 / 2 } d \lambda .
$$

.'yu.c   
Star oscillating back and forth through the plane of a disc galaxy,as an example of a situation where two events $\boldsymbol { \mathcal { Q } }$ and $\boldsymbol { \vartheta }$ can be connected by more than one geodesic. Upper left: The galaxy seen edge-on. showing (dashed line)the path of the star in question. referred to a local frame partaking of and comoving with the general revolution of the nearby“disc stars.” Upper right: The efective potential sensed by the star,according to Newtonian gravitation theory,is like that experienced bya ballwhich rolls down one inclined plane and up another("free fall toward galactic plane”with acceleration $g = \frac { 1 } { 2 }$ in the units used here).The three central frames: Possible and impossble world lines for the star connecting two given events $\boldsymbol { \mathcal { a } }$ (plane of galaxy at $t = 0$ and $\ddot { \ast } \beta$ (plane of galaxy at $t = 2$ ).Right:Throw starup from the galactic plane with enough velocity so that it just gets back to the plane at $t = 2$ Left: Throw it up with half the velocityand it will come back in half the time (very contrary to behavior of a simple harmonic oscillation,but in accord with galaxy's v-shaped potential)，thus being able to make two excursions in the allotted time between $\boldsymbol { \mathcal { a } }$ and :B.Center:A conceivable world line (conceivable with rocket propulsion!) but not a geodesic. Bottom: Comparison of these and any other paths that allow themselves to be approximated in the form

$$
z = a _ { 1 } \sin { ( \pi t / 2 ) } + a _ { 2 } \sin { ( 2 \pi t / 2 ) } .
$$

Here the two adjustable parameters, ${ \pmb a } _ { 1 }$ and $\pmb { a } _ { 2 }$ ，provide the coordinates in a two-dimensional “function space"(approximation to the infinite-dimensional function space required to depict allconceivable world lines connecting $\boldsymbol { \mathcal { a } }$ and $\boldsymbol { \mathfrak { B } }$ ; note comparison in right center frame between one-term Fourier approximation and exact,parabolic law of free fal; similarly in left center frame,where the two curves agree too closely to be shown separate on the diagram). Details: In the Context of general relativity,take an arbitrary world line that connects $\mathcal { Q }$ and $\mathcal { B }$ ,evaluate lapse of proper time,repeat for other world lines,and say that a given world line represents a posible motion ("geodesic") when for it the proper time is an extremum with respect to allnearby world lines.In the Newtonian approximation,the difference between the lapse of proper time and the lapse $( t _ { \mathcal { B } } - t _ { \ell } )$ of coordinate time is all that comes to attention, in the form of the “action integral"(on a “per-unit-mass basis")

$$
\begin{array} { l } { I = \int _ { d } ^ { \circ \beta } [ ( \mathrm { { k i n e t i c } } ) - ( \mathrm { { p o t e n t i a l } } ) ] d t } \\ { = \int [ \frac { 1 } { 2 } ( \frac { d z } { d t } ) ^ { 2 } -  | z | ] d t } \end{array}
$$

(maximum, or other extremum,in the proper time implies minimum,or corresponding other extremum, in the action $\pmb { I }$ ).The integration gives

$$
I = ( \pi ^ { 2 } a _ { 1 } ^ { 2 } / 8 ) - ( 4 | a _ { 1 } | / \pi ) + ( \pi ^ { 2 } a _ { 2 } ^ { 2 } / 2 )
$$

for $\vert a _ { 2 } \vert < \frac { 1 } { 2 } \vert a _ { 1 } \vert$ (one-excursion motions),and for $\vert a _ { 2 } \vert > \frac { 1 } { 2 } \left\{ a _ { 1 } \vert a _ { 2 } \vert \right.$ (two-excursion motions),

$$
I = ( \pi ^ { 2 } a _ { 1 } ^ { 2 } / 8 ) + ( \pi ^ { 2 } a _ { 2 } ^ { 2 } / 2 ) - ( 4 | a _ { 2 } | / \pi ) - ( a _ { 1 } ^ { 2 } / \pi | a _ { 2 } | ) .
$$

The one-excursion motion minimizes the action (maximizes the lapse of proper time). The two-excursion motion extremizes the action but does not minimize it ("saddle point”;“mountain pass”in the topography). Choquard (1955） gives other examples of problems of mechanics where there is more than one extremum.Morse (l934) and Morse and Cairns (i969) give a theorem connecting the number of saddles of various types with the numbers of maxima and minima ("critical-point theorem of the calculus of variations in the large").

![](images/50e40ff7d0429e80e0b2a6bb8ad266c7a47fbd6cb7e0a8761fcce4544221a4cc.jpg)

![](images/88ee75b80872a65b2e521e48121b9301daecf9cc91782e79910bdd5fae26c5d0.jpg)

![](images/d94fd8270489ff9aabc8853a64475d3c7913651d23e104bc2aaf92fbc90a6361.jpg)  
Figure 13.3. Extremizing lapse of proper time by suitable choice of world line.Left: Spacetime；and world line $F$ that extremizes the lapse of proper time $\boldsymbol { \tau }$ from $\boldsymbol { \mathcal { Q } }$ to $\boldsymbol { \mathcal { B } }$ compared to other world lines.The specific world lines depicted in the diagram happen to be distinguished from fiducial world line $G$ by two“Fourier amplitudes" $a _ { 1 }$ and ${ a } _ { 2 }$

$$
\delta a ^ { \mu } ( \lambda ) = a _ { 1 } \sin ( \pi \lambda ) + a _ { 2 } \sin ( 2 \pi \lambda ) , \ldots \ .
$$

where the arbitrary scaling of $\lambda$ ,and its zero,are so adjusted that $\lambda ( { \mathcal { Q } } ) = 0 , \lambda ( { \mathcal { B } } ) = 1 .$

Right:“Path space.”The coordinates in this space are the Fourier amplitudes $\pmb { a } _ { 1 }$ and $\alpha _ { 2 }$ .Only these two amplitudes (two dimensions") are shown out of what in principle are infinitely many amplitudes ("infinite-dimensional path space") required to represent the general timelike world line connecting $\boldsymbol { \mathscr { q } }$ and B.Any given contour curve runs through allthose points (in path space)for which the corresponding world lines (in spacetime) rack up the indicated lapse of proper time $\pmb { \tau }$ Foregoing description is classical: according to quantum mechanics,all the timelike world lines connecting $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ occur with the same probability amplitude(principle of democracy of histories") with theonly diference from one to another being the phase of this complex probability amplitude exp $( - i m \tau / \hbar )$ $m =$ mass of particle, $\hbar =$ quan tum of angular momentum). In ihe sum over these probability amplitudes, however,destructive interference wipes out the contributions from all those histories which differ too much from the optimal or classical history ("Fresnel wave zone";“Feynman's principle of sum over histories”;see Feynman and Hibbs, 1965).Capitalizing on this wave-mechanical background to show how the machinery of the physical world works,Box 25.3 spells out the Hamilton-Jacobi method ("short-wavelength limit of quantum mechanics"） for determining geodesics,a method considerably more convenient for most applications than the usuai “second-order differential equations for geodesics” (equation l0.27).

Focus on a specific world line, $x ^ { \mu } = a ^ { \mu } ( \lambda )$ ，with all deformations of it gone from view; one may replace $a ^ { \mu } ( \lambda )$ by $x ^ { \mu } ( \lambda )$ everywhere. Then the differential equations (13.32) for an extremal world line reduce to

$$
g _ { \sigma \nu } { \frac { d ^ { 2 } x ^ { \nu } } { d \tau ^ { 2 } } } + { \frac { 1 } { 2 } } \biggl ( { \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } } + { \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } } - { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } } \biggr ) { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } = 0 .
$$

As an aside, note that the identity (l3.34) now follows by one differentiation (with respect to $\pmb { \tau }$ ）of the equation

$$
g _ { \sigma \nu } { \frac { d x ^ { \sigma } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } + 1 = 0 .
$$

Thus the identity is to be interpreted as saying that 4-velocity and 4-acceleration are orthogonal for any world line, extremal or not. Now return to (l3.36), raise an index with $g ^ { \beta \sigma }$ ,and thereby bring the equation for a straight line of local Lorentz geometry into the form

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \tau ^ { 2 } } + g ^ { \beta \sigma } \frac { 1 } { 2 } \bigg ( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \bigg ) \frac { d x ^ { \mu } } { d \tau } \frac { d x ^ { \nu } } { d \tau } = 0 .
$$

Compare with the standard form of the equation for a geodesic in “premetric geometry,”

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \beta } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 .
$$

Conclude that the geodesics of the premetric geometry will agree with the straight lines of the local Lorentz geometry if and only if two conditions are satisfied: (l) the 40 connection coefficients $T ^ { \beta } { } _ { \mu \nu }$ that define geodesics, covariant derivatives, and parallel transport must be given in terms of the 10 metric coefficients $g _ { \mu \nu }$ ("Einstein gravitation potentials") by the equations (13.22) and (13.23) previously derived; and (2) the geodesic parameter $\lambda$ must agree with the proper time $\pmb { \tau }$ up to an arbitrary normalization of zero point and an arbitrary but constant scale factor； thus

$$
\lambda = a \tau + b .
$$

(Nothing in the formalism has any resemblance whatsoever to the universal time t of Newton“flowing everywhere uniformly";rather, there is a separate proper time $\pmb { \tau }$ for each geodesic). See Box 13.3 for another variational principle, which gives in one step both the extremal world line and the right parametrization on that line.

With this step,one has completed the transfer of the ideas of curved-space geometry from a foundation based on geodesics to a foundation based on metric. The resulting geometry always and everywhere anchors itself to the principle of"local Lorentz character,”as the geometry of Newton-Cartan never did and never could.

# Exercise 13.5. ONCE TIMELIKE，ALWAYS TIMELIKE

# EXERCISES

Show that a geodesic of spacetime which is timelike at one event is everywhere timelike. Similarly,show that a geodesic initially spacelike is everywhere spacelike,and a geodesic initially null is everywhere null.[Hint:This is the easiest exercise in the book!]

(coniinued on page 324)

# Box 13.2 "GEODESIC" VERSUS "EXTREMAL WORLD LINE"

Once the connection coefficients $T ^ { \alpha } { } _ { \mu \nu }$ have been expressed in terms of Einstein's gravitational potentials $g _ { \mu \nu }$ by the equations (l3.22) and (13.23), as they are now and hereafter will be in this book ("Riemannian or metric geometry"), it is permissible and appropriate to subsume under the one word“geodesic” two previously distinct ideas:(l) a parametrized world line that satisfies the geodesic equation

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \alpha } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ;
$$

and (2)a world line that extremizes the proper time (or, if spacelike,a curve that extremizes the proper distance) between two events $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ .The one possible source of confusion is this, that (l)

presupposes a properly parametrized curve (as was essential, for example, in the Schild's ladder con-struction employed for parallel transport in Chapter 10),whereas (2) cares only about the course of the world line through spacetime, being indifferent to what parametrization is used or whether any parametrization at all is introduced. This is not to deny the possibility of “marking in afterward’ along the extremal curve the most natural and easily evaluated of all parameters, the proper time itself, whereupon the extremal curve of (2) satisfies the geodesic equation of (l).Ambiguity is avoided by insisting on proper parametrization: henceforth the word “curve” means a parametrized curve, the word“geodesic” means a properly parametrized geodesic.

# Box 13.3 "DYNAMIC" VARIATIONAL PRINCIPLE FOR GEODESICS

If the principle of extremal length

$$
\tau = \int _ { d } ^ { \infty } { \biggl [ } - g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } { \biggr ] } ^ { 1 / 2 } d \lambda = \mathrm { e x t r e m u m }
$$

is indifferent to choice of parametrization $[ ^ { 6 6 } d \lambda ^ { 3 }$ canceling out in (l)] and if the geodesic equation finds the proper parametrization a matter of concern, it is appropriate to search for another extremal principle that yields in one package both the right curve and the right parameter. By analogy with elementary mechanics, one expects that an equation of motion [the geodesic equation

$$
d ^ { 2 } x ^ { \mu } / d \lambda ^ { 2 } + { \Gamma ^ { \mu } } _ { \alpha \beta } ( d x ^ { \alpha } / d \lambda ) ( d x ^ { \beta } / d \lambda ) = 0 ]
$$

whose leading term has the form $\mathbf { \cdots } \mathbf { \mathit { \hat { x } } } ^ { \mathbf { \prime } \mathbf { \prime } }$ can be derived from a Lagrangian with leading term $\mathbf { \phi } ^ { 6 6 1 } \dot { x } ^ { 2 } \mathbf { \bar { \phi } } ^ { , 9 }$ ("kinetic energy"；“dynamic” term). The simplest coordinate invariant generalization of ${ \scriptstyle { \frac { 1 } { 2 } } } { \dot { x } } ^ { 2 }$ is

$$
\frac { 1 } { 2 } g _ { \mu \nu } ( d x ^ { \mu } / d \lambda ) ( d x ^ { \nu } / d \lambda ) .
$$

Thus one is led to try, in place of the“geometric” principle of extremal length, a new“dynamic” extremal principle:

$$
{ \begin{array} { r l } & { I = { \cfrac { 1 } { 2 } } \int _ { a } ^ { \mathfrak { B } } g _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } d \lambda } \\ & { \quad = \int _ { a } ^ { \mathfrak { B } } L \left( x ^ { \sigma } , { \cfrac { d x ^ { \sigma } } { d \lambda } } \right) d \lambda = { \mathrm { e x t r e m u m } } } \end{array} }
$$

(replacement of square root in previous variational principle by first power). The condition for an extremum, here as before [equations (13.30)to (13.32)] is annulment of the so-called Euler-Lagrange “functional derivative”

$$
\begin{array} { r l } & { 0 = \frac { \delta I } { \delta x ^ { \sigma } } \equiv \left( \begin{array} { l } { \mathrm { c o e f f i c i e n t ~ o f ~ } \delta x ^ { \sigma } \mathrm { ~ i n } } \\ { \mathrm { t h e ~ i n t e g r a n d ~ o f ~ } \delta I } \end{array} \right) } \\ & { \quad = \frac { \partial L } { \partial x ^ { \sigma } } - \frac { d } { d \lambda } \frac { \partial L } { \partial \left( \frac { d x ^ { \sigma } } { d \lambda } \right) } ; } \end{array}
$$

or, written out in full detail,

$$
g _ { \sigma \nu } \frac { d ^ { 2 } x ^ { \nu } } { d \Lambda ^ { 2 } } + \frac { 1 } { 2 } \left( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \right) \frac { d x ^ { \mu } } { d \Lambda } \frac { d x ^ { \nu } } { d \Lambda } = 0 ;
$$

or, after multiplication by the reciprocal metric,

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + g ^ { \alpha \sigma } \frac { 1 } { 2 } \bigg ( \frac { \partial g _ { \sigma \nu } } { \partial x ^ { \mu } } + \frac { \partial g _ { \sigma \mu } } { \partial x ^ { \nu } } - \frac { \partial g _ { \mu \nu } } { \partial x ^ { \sigma } } \bigg ) \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ;
$$

which translates into the geodesic equation

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } } + { \Gamma ^ { \alpha } } _ { \mu \nu } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \nu } } { d \lambda } } = 0 .
$$

Thus,the new “dynamic” expression (2) is indeed extremal for geodesic curvesand, by contrast with proper length, (l), it is extremal when and only when the geodesic is affnely parametrized.[Its “Euler-Lagrange equations”(6)remain satisfied only under parameter changes $\lambda _ { \mathrm { n e w } } = a \lambda _ { \mathrm { o l d } } + b$ ，which keep the parameter affine; by contrast, the Euler-Lagrange equations (l3.31) and (13.32) for the “principle of extremal length”(l) remain satisfied for any change of parameter whatsoever.]