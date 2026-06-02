# 4 ${ \pmb { L } } ^ { p }$ -COHOMOLOGY

The proof of P. Julg's theorem involves several magic identities satisfied by special functions.We present now a direct argument that shows that ${ \pmb L } ^ { 2 }$ -harmonic forms on complex hyperbolic space are representable by partial boundary values. It turns out that the method applies to ${ \pmb L } ^ { p }$ -cohomology as well.

Recall that the ${ \pmb { L } } ^ { p }$ -cohomology $H _ { p } ^ { * } ( X )$ of a Riemannian manifold $\boldsymbol { x }$ is the cohomology of the complex $( \Omega _ { ( p ) } ^ { * } ( X ) , d )$ where $\Omega _ { ( p ) } ^ { * } ( X )$ is the space of differential forms $\pmb { \alpha }$ with $| \alpha | \in \mathbb { L } ^ { p }$ and $| d \alpha | \in L ^ { p }$ . In general, the image

$$
d ( \Omega _ { ( p ) } ^ { k - 1 } ( X ) ) \subset \Omega _ { ( p ) } ^ { k } ( X )
$$

is not closed, and one defines reduced ${ \pmb L } ^ { \pmb { p } }$ -cohomology as the quotient

$$
\overline { { H } } _ { p } ^ { k } ( X ) = \Omega _ { ( p ) } ^ { k } ( X ) / \overline { { d \Omega _ { ( p ) } ^ { k - 1 } ( X ) } }
$$

by the closure of the image of $^ d$

If $H _ { p } ^ { * } ( X ) = \overline { { H } } _ { p } ^ { * } ( X )$ i.e.,iftheimage $d ( \Omega _ { ( p ) } ^ { k - 1 } ( X ) )$ is coed in $\Omega _ { ( p ) } ^ { k } ( X )$ we say that $X$ has only reduced $L ^ { p }$ -coh omology in degree $k$ . This property is invariant under coarse quasiisometries,like those arising from isomorphisms of cocompact isometry groups.

For $\mathscr { p } = 2$ ， there is exactly one $L ^ { 2 }$ -harmonic form in each reduced $L ^ { 2 }$ -cohomology class,i.e., the space of $L ^ { 2 }$ -harmonic forms is isomorphic to $\overline { { H } } _ { 2 } ^ { * } ( X )$

We explain next that on a negatively curved manifold,a closed form in ${ \pmb { L } } ^ { p }$ often admits a boundary value. We start again with the easier case of real hyperbolic space,which has been computed independently by V. Goldshtein, V. Kuz'minov and I. Shvedov,[6].

4.1 ${ \pmb L } ^ { { \pmb p } }$ -cohomology of real hyperbolic space.- One uses the decomposition of real hyperbolic $\pmb { n }$ -space $X$ as a warped product

$$
X = \mathbf { R } _ { + } \times _ { \sinh r } S ^ { n - 1 } .
$$

Split a $\pmb { k }$ -form $\pmb { \alpha }$ as

$$
\alpha = a + b \wedge d r
$$

where $^ { a }$ and $\pmb { b }$ are viewed as functions on $\mathbf { R } _ { + }$ with values in ${ \pmb { L } } ^ { p }$ -differential forms on the sphere $S ^ { n - 1 }$ . The ${ \pmb { L } } ^ { { \pmb { p } } }$ norm of $\pmb { \alpha }$ is roughly the norm of ${ \pmb a }$ in $L ^ { p } ( e ^ { ( n - 1 - k p ) r } { \bar { d } } r )$ plus the norm of $\pmb { b }$ in $L ^ { p } ( e ^ { ( n - 1 - ( k - 1 ) p ) r } d r )$ . The form $\pmb { \alpha }$ is closed iff $\pmb { a }$ is closed and $\begin{array} { r } { \frac { \partial } { \partial r } a = \pm d b } \end{array}$ , which can be written

$$
\frac { \partial } { \partial r } d ^ { - 1 } a = \pm d ^ { - 1 } d b
$$

where $d ^ { - 1 }$ takes exact $k$ -forms to coexact $k - 1$ -forms. Thus $d ^ { - 1 }$ denotes the pseudo-inverse of $d$

If $p < n - 1 / k - 1 , L ^ { p } ( e ^ { ( n - 1 - ( k - 1 ) p ) r } d r ) \subset L ^ { 1 } ( d r )$ s0 $d ^ { - 1 } { \pmb { \alpha } }$ converges in ${ \pmb L } ^ { \pmb { p } }$ as $r \to + \infty$ ,and $^ { a }$ converges to a distribution $a ( \infty ) = B V ( \alpha )$

f $\alpha \in d ( \Omega _ { ( p ) } ^ { k - 1 } )$ ,or if $p \leq n - 1 / k$ ,then $B V ( \alpha ) = 0$

Conversely, if $B V ( \alpha ) = 0$ ,then $\pmb { \alpha }$ admits a primitive $\beta$ in ${ \pmb { L } } ^ { { \pmb { p } } }$ . Indeed, the Poincaré homotopy formula

$$
\beta ( r ) = - \int _ { 0 } ^ { + \infty } b ( r + s ) d s
$$

(no dr component） solves $d { \boldsymbol { \beta } } = \alpha$ and is in ${ \pmb { L } } ^ { p }$ (Hardy inequality） for $p <$ $n - 1 / k - 1$

In conclusion,for real hyperbolic $\pmb { n }$ -space, ${ \pmb L } ^ { \pmb { p } }$ -cohomology in degree $\pmb { k }$ vanishes for $p \leq n - 1 / k$ ,and, for $n - 1 / k < p < n - 1 / k - 1$ ,it is isomorphic to a certain function space of closed $\pmb { k }$ -forms on $S ^ { n - 1 }$ . In particular, it is a Hausdorff Banach space, thus,for such values of $\pmb { p }$ and $k$ ,real hyperbolic space has only reduced cohomology. The $\pmb { L ^ { p } }$ norm can be recovered in terms of boundary values - up to a constant,see [12] for the case when $k = 1$

For $p = n - 1 / k - 1$ ,reduced cohomology vanishes but $L ^ { p }$ -cohomology is huge.

The same argument applies to manifolds with variable curvature. Indeed,what matters is the Lie derivative of the metric on forms under the radial vector ffeld $\frac { \partial } { \partial r }$ . This is controlled by sectional curvature. This leads to the following comparison result (Jens Heber's help was instrumental in obtaining the sharp curvature assumption).

4.2THEOREM [13].- Let $X$ be a complete simply connected Riemannian manifold of dimension $\pmb { n }$ with negatively $\delta$ -pinched sectional curvature, i.e., $- 1 \le K \le \delta < 0$ . For all

$$
p < 1 + \frac { n - k } { k - 1 } \sqrt { - \delta } ,
$$

an ${ \pmb L } ^ { \pmb { p } }$ closed $\pmb { k }$ -form admits a boundary value,which determines its cohomology class. In particular, $\boldsymbol { x }$ has only reduced $L ^ { p }$ -cohomology in degree $k$

4.3 ${ \pmb { L } } ^ { 2 }$ -cohomology of complex hyperbolic plane.- We now check that the $L ^ { 2 }$ -cohomology of complex hyperbolic plane in degree 2 is a limiting case of the above comparison theorem. Indeed, the theorem applies to ${ \pmb { L } } ^ { p }$ closed 2-forms on complex hyperbolic plane, for all $\mathbf { \hat { \boldsymbol { p } } } < \mathbf { \hat { \boldsymbol { 2 } } }$ : there exists a boundary value,which determines the $L ^ { p }$ -cohomology class.

For $\mathbf { \hat { \varepsilon } } ^ { p } \geq \mathbf { 2 }$ ,the boundary value does not exist any more,but a partial boundary operator will replace it,at least when $p < 4$

The complex hyperbolic plane in polar coordinates is not a warped product : the metric on spheres increases at different speeds along the factors of the splitting

$$
T S ^ { 3 } = \xi \oplus \xi ^ { \perp } .
$$

Accordingly,a 2-form has to be split into four components

$$
\alpha = a + a ^ { \prime } d \tau + b \wedge d r + b ^ { \prime } \tau \wedge d r .
$$

The $L ^ { p }$ norm of $\pmb { \alpha }$ in roughly the sum of the norms of $a \in L ^ { p } ( e ^ { ( 4 - 3 p ) r } d r )$ $a ^ { \prime } + b ^ { \prime } \in L ^ { p } \big ( e ^ { ( 4 - 2 p ) r } d r \big )$ ， $b \in L ^ { p } ( e ^ { ( 4 - p ) r } d r )$ For $\pmb { p = 2 }$ , the limiting exponent 0 for $\pmb { b ^ { \prime } }$ prevents one from having an ordinary boundary value as in the preceding paragraph.

If we view the forms $a + d a ^ { \prime } \wedge \tau \in \mathcal { T } ^ { 2 }$ and $b \in \Omega ^ { 1 } / \mathcal { T } ^ { 1 }$ as elements of Rumin's complex,the equation $d \alpha = 0$ implies

$$
d _ { \xi } \big ( a + d a ^ { \prime } \wedge \tau \big ) = 0
$$

and

$$
\frac { \partial } { \partial r } ( a + d a ^ { \prime } \wedge \tau ) = d _ { R } b
$$

which implies that $a + d a ^ { \prime } \wedge \tau$ converges (when $\mathfrak { p } < 4$ ),this is our partial boundary value $B V ( \pmb { \alpha } )$ . It factors through reduced ${ \pmb L } ^ { \pmb { p } }$ -cohomology，and is injective on the reduced cohomology.

It turns out that the complex hyperbolic plane has only reduced cohomology in degree 2. This is a special case of a theorem of A.Borel, [2]. It also follows from estimates on the spectrum of the Laplacian. Indeed, for ${ { \pmb L } ^ { 2 } }$ -functions and 1-forms,the spectrum of the Laplacian is bounded below, [3]. This implies an estimate of the form

$$
\parallel \beta \parallel _ { 2 } ^ { 2 } \leq C \left( \parallel d \beta \parallel _ { 2 } ^ { 2 } + \parallel \delta \beta \parallel _ { 2 } ^ { 2 } \right)
$$

for compactly supported 1-forms $\beta$ ，which therefore implies that the image $d ( \Omega _ { ( 2 ) } ^ { 1 } ( \mathbf { C } H ^ { 2 } ) )$ is closed in $\Omega _ { ( 2 ) } ^ { 2 } ( \mathbf { C } H ^ { 2 } )$ . We conclude that our partial boundary value $B V$ is injective on $L ^ { 2 }$ -cohomology .

This elementary approach cannot give the finer information on complex types contained in theorem 3.5.

# References

[1]M．ATIYAH，V. PATODI, I. SINGER,Spectral assymetry and Riemannian geometry，Math. Proc. Cambridge Philos. Soc. 78, 405-432 (1975).   
[2]A.BOREL,The $L ^ { 2 }$ -cohomology of negatively curved Rieman-nian symmetric spaces，Ann. Acad. Sci. Fennicae 1O,95-105 (1985).   
[3] H.DONNELLY, CH. FEFFERMAN, $L ^ { 2 }$ -cohomology and index theorem for the Bergman metric, Annals of Math. 118,(1983),593- 618.   
[4] P.Y.GAILLARD, Transformation de Poisson de formes différentielles， Comment.Math.Helvetici 61, 581- (1986).   
[5] V. GINzBURG,On closed characteristics of 2-forms, PhD Thesis,Berkeley (1990).   
[6] V. GOL'DSHTEIN, V. KUZ'MINOV,I. SHVEDOV, ${ \pmb L } ^ { { \pmb p } }$ -cohomology of noncompact riemannian manifolds, to appear in Sib. Mat. Zh.   
[7] M. GRoMov, Asymptotic properties of discrete groups, Preprint I.H.E.S. (1992).   
[8] A.JuHL,On the Poisson transformation for differential forms on hyperbolic spaces， Seminar Analysis der K.Weierstrass Institut 1987/88,p. 224-236,Teubner,Leipzig (1988).   
[9] P. JULG, $\kappa$ -theorie des $C ^ { \ast }$ -algebres associees a certains groupes hyperboliques， These d'Etat, Université de Strasbourg (1991).   
[10] P．JULG,G． KASPAROV, $\pmb { L }$ 'anneau ${ \cal K K } _ { G } ( { \bf C } , { \bf C } )$ pour $\boldsymbol { G } =$ $S U ( n , 1 )$ ，to appear in C.R. Acad. Sci. Paris.   
[11] B.HELFFER,J.NoURRIGAT,Hypoelipticité maximale pour des opérateurs polynomes de champs de vecteurs， Progress in Math.58, Bikhauser (1985).   
[12]P.PANsU,Cohomologie $L ^ { p }$ des varietes a courbure négative, cas du degré un， in “P.D.E.and Geometry $1 9 8 8 ^ { \mathfrak { n } }$ ,Rend. Sem. Mat.Torino,Fasc.spez., 95-120 (1989).   
[13] P.PANsU,Cohomologie $L ^ { p }$ et pincement,in preparation.   
[14] M.RuMIn, Un complexe de formes différentielles sur les variétés de contact，C.R. Acad. Sci. Paris 310, 401-404 (1990).   
[15] ZHONG GE, Generalized characteristics for Carnot-Caratheodory metrics, Preprint Univ. Arizona, Tuczon (1991).

# The Maslov class rigidity and non-existence of Lagrangian embeddings

Leonid Polterovich   
Institut des Hautes Etudes Scientifiques 35,route de Chartres   
91440-BURES sur YVETTE (France)\*

October 1990
