# 5 Proof of the Main Result

In this section we prove Theorem 1.2. Let $\Omega \subset \mathbb { C } ^ { n }$ with ${ \overline { { \Omega } } } \subset U _ { \Sigma }$ and assume $e ( \Sigma ) < c ( \Omega )$ .If $\pmb { \Omega }$ is unbounded we have $\varphi _ { \Sigma } ( \Omega ) \cap \Omega \neq \emptyset$ since $\varphi _ { \Sigma } = \mathrm { I d }$ outside of a compact subset $\pmb { K }$ of $\mathbb { C } ^ { n }$ . So we may assume without loss of generality that $\pmb { \Omega }$ is bounded. Arguing indirectly let us assume $\varphi _ { \Sigma } ( \overline { { \Omega } } ) \cap \overline { { \Omega } } = \mathring { \varnothing } . \mathbb { C } ^ { n + 1 } \setminus \Sigma$ has two connected components $C ^ { + }$ and $C ^ { - }$ ， where $C ^ { + }$ is distinguished by the fact that it contains $( \mathbf { 0 } , \ldots , \mathbf { 0 } , - { \pmb { a } } + { \dot { \imath } } )$ for all large ${ \pmb a } \in { \pmb R }$ Fix ${ \pmb \delta } > { \pmb 0 }$ . We find ${ \pmb a } > { \pmb 0 }$ and $c ^ { - } < 0 , c ^ { + } > 0$ and $\Psi \in \mathcal { D }$ such that

$$
\begin{array} { r l } & { \Psi ( { \Sigma } ) \subset ( { \mathbb C } ^ { n } \oplus { \mathbb R } ) \cup ( { \mathbb C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) } \\ & { 2 a ( c ^ { + } - c ^ { - } ) < e ( { \Sigma } ) + \delta . } \end{array}
$$

We note that $\Psi ( { \boldsymbol { \Sigma } } )$ has the same holonomy. So we may assume without loss of generality that $\Psi ( { \boldsymbol { \Sigma } } )$ is $\pmb { \Sigma }$ . That is

$$
\begin{array} { r l } & { \Sigma \subset ( { \mathbb C } ^ { n } \oplus { \mathbb R } ) \cup ( { \mathbb C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) } \\ & { 2 a ( c ^ { + } - c ^ { - } ) < e ( \Sigma ) + \delta . } \end{array}
$$

We foliate an open neighbourhood in $C ^ { + } \cup \Sigma$ by hyperplanes $\Sigma _ { \epsilon } , 0 \le \epsilon \le \epsilon _ { 0 }$ with $\Sigma _ { 0 } = \Sigma$ and

$$
\Sigma _ { \epsilon } \subset ( { \bf C } ^ { n } \oplus { \bf R } \oplus i \epsilon ) \cup ( { \bf C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) ~ .
$$

Here ${ \bf \epsilon } \epsilon _ { 0 } > { \bf 0 }$ is supposed to be sufficiently small. With the obvious identification every $\Sigma _ { \epsilon }$ defines a holonomy

$$
\varphi _ { \epsilon } : U _ { \epsilon } \longrightarrow { \bf c } ^ { n } \ .
$$

If $\epsilon _ { 0 } > 0$ is small enough we have ${ \overline { { \Omega } } } \subset U _ { \epsilon }$ for every $\epsilon \in [ 0 , \epsilon _ { 0 } ]$ and $\varphi _ { \epsilon } ( \overline { { \Omega } } ) \cap \overline { { \Omega } } = \varnothing$ ， since the same is true for $\varphi _ { 0 } = \varphi _ { \Sigma }$ . Pick a $H \in \mathcal { H } _ { a d } ( \Omega )$ with

$$
m ( H ) \geq c ( \Omega ) - \delta \ .
$$

Pick a $\varphi _ { + } \in \theta _ { c ^ { + } }$ with

$$
d ( \varphi _ { + } ) \leq 2 a c _ { + } + \delta \ .
$$

Choose a smooth map $\gamma _ { 1 } : \mathbb { R } \longrightarrow [ 0 , + \infty )$ satisfying (assuming $\epsilon _ { 0 } < c _ { + }$ ）

$$
\begin{array} { r } { \begin{array} { l l l l } { \gamma _ { 1 } ( s ) } & { = } & { 0 } & { \mathrm { ~ f o r ~ } s \le 0 } \\ { \gamma _ { 1 } ^ { \prime } ( s ) } & { > } & { 0 } & { \mathrm { ~ f o r ~ } s \in ( 0 , \epsilon _ { 0 } ) } \\ { \gamma _ { 1 } ( s ) } & { = } & { c _ { 1 } } & { \mathrm { ~ f o r ~ } s \ge \epsilon _ { 0 } } \end{array} } \end{array}
$$

with $\pmb { c _ { 1 } }$ a constant bigger than $2 a ( c _ { + } - c _ { - } + 2 )$ . Next choose a smooth map $\gamma _ { 2 } : \mathbb { R } \longrightarrow [ c _ { 1 } , + \infty )$ satisfying

$$
\begin{array} { l } { { \gamma _ { 2 } \left( s \right) = c _ { 1 } \mathrm { f o r } s \le c _ { + } } } \\ { { \gamma _ { 2 } ^ { \prime } \left( s \right) > 0 \mathrm { f o r } s > c _ { + } } } \end{array}
$$

Now we define a smooth Hamitonian $K : \mathbb { C } ^ { n + 1 } \longrightarrow [ 0 , + \infty )$ by

$$
\begin{array} { l c l } { { K ( z ) } } & { { = } } & { { 0 \ \mathrm { f o r } \ z \in C ^ { - } } } \\ { { K ( z ) } } & { { = } } & { { \gamma _ { 1 } ( \epsilon ) \ \mathrm { f o r } \ z \in \Sigma _ { \epsilon } , 0 \leq \epsilon \leq \epsilon _ { 0 } } } \\ { { K ( z ) } } & { { = } } & { { c _ { 1 } \ \mathrm { f o r } \ z \in C ^ { + } \ \backslash \ \cup \Sigma _ { \epsilon } ) , \ \mathrm { I m } \ z _ { n + 1 } \leq c _ { + } } } \\ { { K ( z ) } } & { { = } } & { { \gamma _ { 2 } ( \mathrm { I m } z _ { n + 1 } ) \ \mathrm { f o r } \ \mathrm { I m } z _ { n + 1 } > c _ { + } \ . } } \end{array}
$$

By construction we have

$$
K ( z ) \geq \varphi _ { + } ( \operatorname { I m } z _ { n + 1 } ) , z \in \mathbb { C } ^ { n + 1 } \ . \nonumber
$$

Finally take a $\varphi _ { - } \in \theta _ { c _ { - } }$ with

$$
\varphi _ { - } ( \mathrm { I m } z _ { n + 1 } ) \geq K ( z ) , z \in \mathbb { C } ^ { n + 1 } \ .
$$

Defining $\varphi : \mathbb { R } \longrightarrow [ 0 , + \infty )$ by

$$
{ \begin{array} { l l l l } { \varphi ( s ) } & { = } & { 0 } & { { \mathrm { f o r ~ } } s \leq 0 } \\ { \varphi ( s ) } & { = } & { \gamma _ { 1 } ( s ) } & { { \mathrm { f o r ~ } } 0 \leq s \leq \epsilon _ { 0 } } \\ { \varphi ( s ) } & { = } & { c _ { 1 } } & { { \mathrm { f o r ~ } } \epsilon _ { 0 } \leq s \leq c _ { + } } \\ { \varphi ( s ) } & { = } & { \gamma _ { 2 } ( s ) } & { { \mathrm { f o r ~ } } s \geq c _ { + } } \end{array} }
$$

we see that $\pmb { K }$ satisfies (27) and (28)of section III with the $\varphi$ defined above for suitable constants $R _ { 1 }$ and $R _ { 2 } > 0$ . We define now a smooth functional $\tilde { \Phi } : E \longrightarrow \mathbb { R }$ by (with $\pmb { \alpha } ( t ) = ( 0 , \ldots , 0 , - \pmb { a } + t \pmb { a } ) )$

$$
\tilde { \Phi } ( z ) = \Phi ( z ) - \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t - \int _ { 1 } ^ { 2 } K ( z + \alpha ) d t \ ,
$$

and comparison functionals $\Phi _ { + }$ and $\Phi _ { - }$ by

$$
\begin{array} { l c l } { { \Phi _ { + } ( z ) } } & { { = } } & { { \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi _ { + } ( \mathrm { I m } z _ { n + 1 } ) d t } } \\ { { \Phi _ { - } ( z ) } } & { { = } } & { { \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi _ { - } ( \mathrm { I m } z _ { n + 1 } ) d t \ . } } \end{array}
$$

The max-min values of $\Phi _ { + }$ and $\Phi$ _ are $d ( \varphi _ { + } )$ and $d ( \varphi _ { - } )$ respectively. In view of Proposition 4.3 these values remain the same if we substract from $\Phi _ { + }$ and $\Phi _ { - }$ the functional $z \longrightarrow \int _ { 2 } ^ { 1 } H ( z _ { 1 } , . . . , z _ { n } ) d t$ for $H \in \mathcal { H } _ { a d } ( \Omega )$ . Next observe that for $z \in E$

$$
\begin{array} { r l } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { + } \big ( \mathrm { I m } z _ { n + 1 } \big ) d t } \\ { = } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { + } \big ( \mathrm { I m } \big ( z _ { n + 1 } + ( - a + t a ) \big ) \big ) d t } \\ { \geq } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } K \big ( z ( t ) + \alpha ( t ) \big ) d t } \\ { \geq } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { - } \big ( \mathrm { I m } \big ( z _ { n + 1 } \big ) \big ) d t \ . } \end{array}
$$

As a consequence

$$
d \bigl ( \varphi _ { - } \bigr ) \leq \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } \bigl ( h ( z ) \bigr ) \leq d \mathopen { } \mathclose \bgroup \left( \varphi _ { + } \aftergroup \egroup \right) ~ .
$$

Consequently in view of previous results

$$
2 a c _ { - } \le \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } \left( h ( z ) \right) \le 2 a c _ { + } + \delta \ .
$$

This result is true for any ${ \cal H } \in { \mathcal { H } } _ { a d } ( \Omega )$ . Now let (54) hold and let $\tilde { \Phi } _ { \tau }$ be the functional obtained from $\tilde { \Phi }$ by replacing $H$ by $\pmb { \tau H }$ for $\pmb { \tau } \in [ \mathbf { 0 } , \mathbf { 1 } ]$ . Since

$$
\left| \tilde { \Phi } _ { \tau _ { 1 } } ( z ) - \tilde { \Phi } _ { \tau _ { 2 } } ( z ) \right| \ \leq m ( H ) \left| \tau _ { 1 } - \tau _ { 2 } \right|
$$

we see that

$$
\tilde { d } _ { \tau } : = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } _ { \tau } ( h ( z ) )
$$

is a continuous,non increasing function of $\tau \in [ 0 , 1 ]$ ,with range in theinterval $[ 2 a c _ { - } , 2 a c _ { + } + \delta ]$ . Since $\tilde { \Phi } _ { \tau }$ satisfies $( W P S ) _ { d }$ for every $\pmb { d } \in \pmb { \mathbb { R } }$ in view of the results in section III we find for every $\tau \in [ 0 , 1 ]$ a critical point $z ^ { \tau }$ of $\tilde { \Phi } _ { \tau }$ Defining $u ( t ) = \alpha ( t ) + z ^ { \tau } ( t )$ we see that $\pmb { u }$ solves

$$
\begin{array} { r c l } { { i \frac { d } { d t } u } } & { { = } } & { { \bigl ( H ^ { \prime } ( u _ { 1 } , \ldots , u _ { n } ) , 0 \bigr ) \ \mathrm { o n } \ [ 0 , 1 ] } } \\ { { i \frac { d } { d t } u } } & { { = } } & { { K ^ { \prime } ( u ) \ \mathrm { o n } \ [ 1 , 2 ] } } \\ { { u _ { k } ( 0 ) } } & { { = } } & { { u _ { k } ( 2 ) \ \mathrm { f o r } \ k = 1 , \ldots , n } } \\ { { \mathrm { R e } u _ { n + 1 } ( 0 ) } } & { { = } } & { { - a \ , \ \mathrm { R e } u _ { n + 1 } ( 2 ) = a \ . } } \end{array}
$$

Assume first for some $t \in [ 1 , 2 ]$ we have $\operatorname { I m } z _ { n + 1 } \geq c _ { + }$ . Then we must have

$$
u ( t ) = ( * , \ldots , * , - a , + 2 a ( t - 1 ) + \tau i )
$$

for $t \in [ 1 , 2 ]$ with $^ *$ being constants. Here $\pmb { \tau }$ satisfies (and is uniquely determined by) $\gamma _ { 2 } ^ { \prime } ( \tau ) = 2 a$ . We calculate using the properties of $\pmb { K }$

$$
\begin{array} { l l l } { { \tilde { \Phi } _ { \tau } ( z ^ { \tau } ) } } & { { \le } } & { { 2 a ( c _ { + } + 1 ) - c _ { 1 } } } \\ { { } } & { { \le } } & { { 2 a ( c _ { + } + 1 ) - 2 a ( c _ { + } - c _ { - } + 2 ) } } \\ { { } } & { { = } } & { { 2 a c _ { - } - 2 a } } \\ { { } } & { { < } } & { { 2 a c _ { - } ~ . } } \end{array}
$$

This contradicts (66) if $\begin{array} { r } { \tilde { \Phi } _ { \tau } \big ( z ^ { \tau } \big ) \equiv \operatorname* { s u p } _ { h \in { \cal B } } \operatorname* { i n f } _ { z \in { \cal E } ^ { - } } \tilde { \Phi } _ { \tau } \big ( h ( z ) \big ) } \end{array}$

Using (68) again we see that $\pmb { u }$ cannot be constant on [1,2]. The possibility left is that $\boldsymbol { u } ( t ) \in \Sigma _ { \epsilon }$ for some $\epsilon \in ( 0 , \epsilon _ { 0 } )$ . We note that

$$
\varphi _ { \epsilon } ( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) ) = ( u _ { 1 } ( 2 ) , \dots , u _ { n } ( 2 ) ) \ .
$$

By the properties of $H \in \mathcal { H } _ { a d } ( \Omega )$ we see that in case $( u _ { 1 } ( 1 ) , \ldots , u _ { n } ( 1 ) ) \ \in$ $\overline { { \Omega } }$ we must have $( u _ { 1 } ( 0 ) , \ldots , u _ { n } ( 0 ) ) \in { \overline { { \Omega } } }$ implying in view of the boundary condition on $\pmb { u }$ that $\varphi _ { \epsilon } ( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) ) \in { \overline { { \Omega } } }$ .This,however, contradicts our assumption. So we must have $( u _ { 1 } ( 1 ) , \ldots , u _ { n } ( 1 ) ) \notin \overline { { \Omega } }$ Consequently $\pmb { u }$ is constant on [0,1]. Hence $\pmb { u }$ solves

$$
\begin{array} { r l } & { i \frac { d } { d t } u = K ^ { \prime } ( u ) \mathrm { ~ o n ~ } [ 1 , 2 ] } \\ & { u _ { k } ( 1 ) = u _ { k } ( 2 ) \mathrm { ~ f o r ~ } k = 1 , \dots , n } \\ & { \mathrm { R e } u _ { n + 1 } ( 1 ) = - a , \mathrm { ~ R e } u _ { n + 1 } ( 2 ) = a } \\ & { \left( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) \right) \notin \overline { { \Omega } } \ . } \end{array}
$$

Hence $z ^ { \tau }$ is a critical point of the smooth fuctional $\hat { \pmb { \Phi } }$ defined by

$$
\hat { \Phi } ( z ) = \Phi ( z ) - \int _ { 1 } ^ { 2 } K ( z ) d t \mathrm { ~ . ~ }
$$

The gradient of $\hat { \Phi }$ at every point is a nonlinear Fredholm operator. Given any critical point $\pmb { z }$ we can construct a finite dimensional manifold $M _ { z } \subset E$ containing all critical points of $\hat { \Phi }$ close to $\pmb { z }$ and the critical points of $\hat { \Phi } \mid M _ { z }$ coincide. Using the Morse-Sard-theorem it follows that the critical levels of $\hat { \Phi }$ are a closed set of measure zero. Denote it by $\boldsymbol { \Gamma }$ . Clearly

$$
\tilde { \Phi } _ { \tau } ( z _ { \tau } ) \in - \tau m ( H ) + \Gamma \ .
$$

Since $\tau \longrightarrow \tilde { d } _ { \tau } = \tilde { \Phi } _ { \tau } ( z ^ { \tau } )$ is continuous and non increasing we find

$$
\tilde { d } _ { \tau } = - \tau m ( H ) + \tilde { d } _ { 0 } \ .
$$

In view of (66)

$$
2 a c _ { - } \leq - \tau m ( H ) + \tilde { d } _ { 0 } \leq 2 a c _ { + } + \delta
$$

for every $\tau \in [ 0 , 1 ]$ . Hence $\tilde { d } _ { 0 } \leq 2 a c _ { + } + \delta$ and $2 a c _ { - } \leq - m ( H ) + \tilde { d } _ { 0 }$ .This implies

$$
m ( H ) \leq 2 a ( c _ { + } - c _ { - } ) + \delta \ .
$$

Since by (54) $m ( H ) \geq { \mathfrak { c } } ( \Omega ) - \delta$ we deduce

$$
\begin{array} { l l l } { { \mathrm { c } ( \Omega ) } } & { { \leq } } & { { 2 a ( \mathrm { c } _ { + } - \mathrm { c } _ { - } ) + \delta + \delta } } \\ { { } } & { { \leq } } & { { e ( \Sigma ) + 3 \delta ~ . } } \end{array}
$$

Since $\delta$ was arbitrarily chosen

$$
{ \sf c } ( \Omega ) \leq e ( \Sigma ) \ .
$$

This， however, contradicts our assumption $e ( \Sigma ) ~ < ~ c ( \Omega )$ .This proves Theorem 1.2. □

# References

[1] Benci, V.and Rabinowitz,P.,Critical point theory for indefinite functionals,Invent.Math.,52,(197)9,241-273.   
[2] Ekeland,I. and Hofer,H., Symplectic topology and Hamiltonian dynamics,Math. Zeit.,200, (1990), 355-378.   
[3] Ekeland,I.and Hofer,H., Symplectic topology and Hamiltonian dynamics II, Math. Zeit.,203,(1990), 553-567.   
[4] Eliashberg，Y.and Hofer，H.，Towards the definition of symplectic boundary, to appear GAFA.   
[5] Hofer,H.,On strongly indefinite functionals with applications,TAMS, 275,(1983) 185-214.   
[6] Hofer,H., Symplectic capacities, in Geometry of low-dimensional manifolds，Vol. 2, edited by S. K. Donaldson and C.B. Thomas, pp.15-34, Cambridge University Press,1990.   
[7] Hofer, H., On the topological properties of symplectic maps, Proceedings of the Royal Society of Edinburgh,115 A, (1990), 25-38.   
[8] Hofer,H.and Zehnder,E.,Periodic solutions on hypersurfaces and a result by C. Viterbo, Inv. Math., 90,(1987),1-7

[9] Hofer,H.and Zehnder,E.,A new capacity for symplectic manifolds,in Analysis et cetera, edited by P.H. Rabinowitz and E. Zehnder,405-428, Academic press,1990.

[10] Sikorav， J.-C.,， Systemes Hamiltoniens et Topologie Symplectique, preprint,Dipartimento di Matematica dell' Universita di Pisa, 1990.

[11] Viterbo, C.， Capacites symplectiques et applications, Astéristique, Séminaire Bourbaki, 695,1989.

[12] Viterbo, C., Symplectic topology as the geometry of generating functions,preprint, January,1991.

# Caustics $D _ { k }$ at points of interface between two media

M. Kazarian

The object of our investigation is singularities of caustics at points of inter-face between two media. When a beam of light passes through the interface, it is refracted according to a well-known law: the ratio of sines of inclination angles of incoming and outgoing beams is equal to the ratio of speeds of propagation of waves in the media (fig.1). The bigger the inclination angle of the incoming beam the bigger the one of the outgoing beam, and for some angle we have an effect of complete reflection: if the inclination angle is larger then the beam is reflected. If the caustic approaches the interface at a point where there is no complete reflection it is only refracted preserving all its singularities.Quite a different situation occurs at points of complete reflection. At this points a caustic arises even if there was no caustic in the first medium (fg. 2). Let us call the caustic new if there was no caustic in the first medium.

Theorem 1. Suppose that the initial wave front and interface are in general position. Then the analytic continuation of the new caustic at a point of complete reflection together with the interface form a singularity which is diffeomorphic to the caustic $D _ { k }$ of the Lagrangian mapping given by the generating family

$$
F ( x , y , z ) = x ^ { 2 } y + y ^ { k - 1 } + q _ { k - 1 } y ^ { k - 2 } + . . . + q _ { 2 } y + q _ { 1 } x
$$

together with the plane $q _ { 1 } = 0$ for some $\pmb { k } \geq \mathbf { 3 }$ (for $\pmb { k } = 3$ it is better to write $A _ { 3 }$ instead of $D _ { 3 }$ ）□

Corollary. In three-dimensional space points of interface where refracted beams touch the interface form a line of complete reflection.

At a generic point of the line of complete reflection analytic continuation of the new caustic together with the interface form a singularity diffeomorphic to the cuspidal edge together with the tangent plane passing through the edge. Physically either one of the branches of the caustic is visible (fig.2a) or the caustic is invisible at all(fig. 2b).

At those points of the line of complete reflection,at which the reflected beam touches the line itself the analytic continuation of the new caustic together with the interface form a singularity diffeomorphic to the caustic

![](../chunks/N-body-Symplectic geometry (Dietmar Salamon) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/32c89c8001d25abc946fc1fb22769b209aa7d4b21e4a020b7cc921017582e2b9.jpg)  
Figure 1:

![](../chunks/N-body-Symplectic geometry (Dietmar Salamon) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/ac2fbe21573bd05e9a6a049aa3f73d51d819f1724dbbec559075f49d0c0f915c.jpg)  
Figure 2:

![](../chunks/N-body-Symplectic geometry (Dietmar Salamon) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/2c7368413bbc945f74a6c6bef4e091037ddb2926cb7a41a1330f141df7fabad4.jpg)  
Figure 3:

![](../chunks/N-body-Symplectic geometry (Dietmar Salamon) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/8a048c69bf16ec6260dd5fdf23b2c726a8b1b0d57a33b32d258f6cf7d78ab6f8.jpg)  
Figure 4:

$D _ { 4 }$ together with the tangent plane passing through one of the cuspidal edges (fig. 3a,4a). Physically visible parts of caustics are represented on fig.3b,4b.□

In three-dimensional space one more singularity may occur. Namely, suppose that there is a caustic in the first medium. Its smooth part intersects the interface transversally along some line. Along this line the inclination angle may change and at some points the caustic itself may have complete reflection. In such points the refracted caustic resembles a “symmetric butterfly”, that is a caustic with the generating family

$$
x ^ { 6 } + q _ { 3 } x ^ { 4 } + q _ { 2 } x ^ { 2 } + q _ { 1 } x
$$

(fig. 5, physically visible parts are represented on fig. 5b,c. They resemble correspondent parts of the caustic $D _ { 4 }$ but are not diffeomorphic to them). In [4] such a caustic arises as a stable caustic under the condition of symmetry. In our case a symmetry is not supposed and the differential type of this caustic seems to have an infinite number of moduli. It was noticed by V.M. Zakalyukin that if the interface is flat and the media are uniform then the caustic is really symmetric. Thus we can regard the problem of investigation of caustics at points of an interface as a problem of broken symmetry.

![](../chunks/N-body-Symplectic geometry (Dietmar Salamon) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/dde07d4a480d876e8e9bf566d121f10500491ec636f125d3904e30dd94abb871.jpg)  
Figure 5:

In Section 1 we formulate the problem mathematically as a problem for Lagrangian mappings.

In Section 2 we discuss the genericity condition and calculate the normal form for initial data of the propagation of waves in the second medium.

In Section 3 we solve an auxiliary problem of clasification of Lagrangian mappings with given boundary conditions. The results of this classification are used in the proof of Theorem 1.

The author is grateful to V.M. Zakalyukin for stating the problem and constant attention to the work. The author also expresses his thanks to V.I. Arnold for valuable observations.
