Proof.ThisisobtainedbycombiningLemma II.5.4andLemma3.1.We need theinvertibilityof $B ( y )$ to conclude that $\{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} ~ = ~ C o n s t$ followsfrom $B ( y ) \nabla \{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} = 0$ □

# VII.3.2 Simultaneous Linear Partial Differential Equations

If two functions $F ( y )$ and $G ( y )$ aregiven,formula(2.8）determines a function $h ( y ) = \{ F , G \} ( y )$ bydifferentiation.We now ask the inversequestion:Given functions $G ( y )$ and $h ( y )$ canwefinda function $F ( y )$ such that $\{ F , G \} ( y ) = h ( y ) ?$ Thisproblem representsa first order linearpartial differential equation for $F _ { \cdot }$ Sowe are led to the following problem,which we first discuss in two dimensions.

One Equation. Given functions $a ( y _ { 1 } , y _ { 2 } )$ $b ( y _ { 1 } , y _ { 2 } )$ , $h ( y _ { 1 } , y _ { 2 } )$ ,find all solutions $F ( y _ { 1 } , y _ { 2 } )$ satisfying

$$
a ( y _ { 1 } , y _ { 2 } ) \frac { \partial F } { \partial y _ { 1 } } + b ( y _ { 1 } , y _ { 2 } ) \frac { \partial F } { \partial y _ { 2 } } = h ( y _ { 1 } , y _ { 2 } ) .
$$

This equation is,for any point $( y _ { 1 } , y _ { 2 } )$ ,a linear relation between thepartial deriyatives of $F ^ { ' }$ ,butdoes not determine them individually.Thereis one direction, however,where thederivative isuniquely determined,namely that of thevector $\boldsymbol { n } = \left( a ( y _ { 1 } , y _ { 2 } ) , b ( y _ { 1 } , y _ { 2 } ) \right)$ ,since the left-hand side of equation(3.4)is thedirectionalderivative ${ \frac { \partial F } { \partial n } } .$ Tlis characteristic lines(see left picture of Fig.3.1).Ifwe parametrize them withaparameter $t$ ,we can compute $y _ { 1 } ( t )$ , $y _ { 2 } ( t )$ aswell as $F ( t ) = F \big ( y _ { 1 } ( t ) , y _ { 2 } ( t ) \big )$ as solutions of the following ordinary differential equations

$$
\dot { y } _ { 1 } = a ( y _ { 1 } , y _ { 2 } ) , \qquad \dot { y } _ { 2 } = b ( y _ { 1 } , y _ { 2 } ) , \qquad \dot { F } = h ( y _ { 1 } , y _ { 2 } ) .
$$

The initial values ${ ( y _ { 1 } ( 0 ) , y _ { 2 } ( 0 ) ) }$ can be chosen on an arbitrary curve $\gamma$ (which must betransversal to the characteristic lines)and the values $F | _ { \gamma }$ can be arbitrarily prescribed.The solution $F ( y _ { 1 } , y _ { 2 } )$ of(3.4)is then created by thecurves(3.5）wherever thecharacteristic lines go (right picture ofFig.3.1).

![](images/75e7ebaf5abe3cfac3cc79887e003b1ad7b3ca71110065bd5aee710fe10c630a.jpg)  
Fig.3.1.Characteristic lines and solution ofa first order linear partial differential equation

![](images/664d757df2dad7557e2c5017d6f3ce2b054e56b44af2a05b83ce78edfd4e55ce.jpg)  
Fig.3.2.Characteristic surfaces of two first order linear partial differential equations

For one equation in $n$ dimensions,the initial values $\left( y _ { 1 } ( 0 ) , \ldots , y _ { n } ( 0 ) \right)$ canbe freelychosen onamanifold of dimension $n - 1$ (e.g.,the subspace orthogonal to the characteristic line passing through a given point),and $F ^ { \prime }$ can bearbitrarilyprescribed onthis manifold.This guarantees the existence of $n - 1$ independent solutions in theneighbourhood of a given point.Here,independent means that the gradients of these functions are linearly independent.

Two Simultaneous Equations. Two simultaneous equations of dimension two are trivial.We therefore suppose $y = ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ and two equations of the form

$$
\begin{array} { r l } & { a _ { 1 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 1 } } + a _ { 2 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 2 } } + a _ { 3 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 3 } } = h _ { 1 } ( y ) , } \\ & { a _ { 1 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 1 } } + a _ { 2 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 2 } } + a _ { 3 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 3 } } = h _ { 2 } ( y ) } \end{array}
$$

foran unknown function $F ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ Thissystem can also be written as $D _ { 1 } F =$ $h _ { 1 } , D _ { 2 } F ^ { \prime } = h _ { 2 }$ ,where $D _ { i }$ denotes the Lie operator corresponding to the vector field $a ^ { [ i ] } ( y )$ Here,we havetwodirectional derivatives prescribed,namely $\frac { \partial F } { \partial n _ { 1 } }$ and $\frac { \partial F } { \partial n _ { 2 } }$ where $n _ { i } = a ^ { [ i ] } ( y )$ (seeFig.3.2).Therefore,we will have to follow both directions and,insteadof(3.5),wewill have two sets of ordinary differential equations

$$
\begin{array} { r l r l r l r l } & { \dot { y } _ { 1 } = a _ { 1 } ^ { [ 1 ] } ( y ) , } & & { \dot { y } _ { 2 } = a _ { 2 } ^ { [ 1 ] } ( y ) , } & & { \dot { y } _ { 3 } = a _ { 3 } ^ { [ 1 ] } ( y ) , } & & { \dot { F } = h _ { 1 } ( y ) } \\ & { \dot { y } _ { 1 } = a _ { 1 } ^ { [ 2 ] } ( y ) , } & & { \dot { y } _ { 2 } = a _ { 2 } ^ { [ 2 ] } ( y ) , } & & { \dot { y } _ { 3 } = a _ { 3 } ^ { [ 2 ] } ( y ) , } & & { \dot { F } = h _ { 2 } ( y ) . } \end{array}
$$

If we prescribe $F$ ona curve that is orthogonal to ${ \boldsymbol { n } } _ { 1 }$ and $_ { n 2 }$ ,and ifwe follow the solutions of(3.7）,we obtain the function $F$ ontwo 2-dimensional surfaces $S _ { 1 }$ and $S _ { 2 }$ containing the prescribed curve.Continuing from $S _ { 1 }$ along the second flow and from $S _ { 2 }$ along the firstflow,we may beledto the same point,but nothing guarantees that the obtained values for $F$ areidentical.To geta well-defined $F ^ { \prime }$ ,additional assumptions on the differential operators and on the inhomogeneities have to be made.

Thefollowing theorem,which is due to Jacobi (1862),hasbeen extended byClebsch (1866),who created the theory of completesystems("vollstandige

Systeme").These papers contained long analytic calculations with myriades of formulas.The wonderful geometric insight is mainly due to Sophus Lie.

Theorem 3.3.Let $\boldsymbol { D } _ { 1 } , \dots , \boldsymbol { D } _ { m }$ be $_ { m }$ $m < n$ lineardifferentialoperatorsin $\mathbb { R } ^ { n }$ correspondingto vectorfelds $a ^ { [ 1 ] } ( y ) , \ldots , a ^ { [ m ] } ( y )$ and suppose that these vectors arelinearly independent for $y = y _ { 0 } .$ 1f

$$
[ D _ { i } , D _ { j } ] = 0 \qquad f o r a l l i , j ,
$$

then the homogeneous system

$$
D _ { i } F = 0 \qquad f o r \ i = 1 , \ldots , m
$$

possesses(ina neighbourhood of $y _ { 0 }$ ） $n - m$ solutions for which the gradients $\nabla F ( y _ { 0 } )$ are linearly independent.

Furthermore,theinhomogeneoussystemofpartialdiffrentialequations

$$
D _ { i } F = h _ { i } \qquad f o r \ i = 1 , \dots , m
$$

possessesaparticular solution ina neighbourhood of $y _ { 0 }$ ，ifandonlyifinaddition to(3.8）the functions $h _ { 1 } ( y ) , \ldots , h _ { m } ( y )$ satisfytheintegrabilityconditions

$$
D _ { i } h _ { j } = D _ { j } h _ { i } \qquad f o r \mathop { a l l } i , j .
$$

Proof(a)Let $V$ denote the space of vectors in ${ \mathbb { R } } ^ { n }$ that are orthogonal to $a ^ { [ 1 ] } ( y _ { 0 } )$ ， $\cdots , a ^ { [ m ] } ( y _ { 0 } )$ ,and consider the $( n - m )$ -dimensional manifold $\mathcal { M } = y _ { 0 } + V .$ We then extend an arbitrary smooth function $F : \mathcal { M }  \mathbb { R }$ toaneighbourhood of $y _ { 0 }$ by

$$
F \Bigl ( \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Bigr ) = F \bigl ( y _ { 0 } + v \bigr ) .
$$

Noticethat(t1，.,tm,U）→y= $( t _ { 1 } , \dots , t _ { m } , v ) \mapsto y = \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v )$ defines alocaldiffeomorphism between neighbourhoods of $0$ and $y _ { 0 }$ Since the application of the operator $D _ { m }$ to(3.10)corresponds toadifferentiation with respect to and the expression $F \bigl ( \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \bigr )$ is independent of $t _ { m }$ by (3.10), we get $D _ { m } F ( y ) = 0$ ToproveDFyfo<irsteoageteoho in(3.1) $\varphi _ { t _ { i } } ^ { [ i ] }$ is in the left-most position.

(b)The necessity of (3.9) followsimmediately from $D _ { i } h _ { j } ~ = ~ D _ { i } D _ { j } F ~ = ~ $ $D _ { j } D _ { i } F ^ { \prime } = D _ { j } h _ { i } .$ Forgiven $h _ { i }$ satisfying(3.9)we define $F ( y )$ ina neighbourhood of $y _ { 0 }$ (i.e.,for small $t _ { 1 } , \ldots , t _ { m }$ and small $\boldsymbol { v }$ )by

$$
\begin{array} { l } { \displaystyle F \Big ( \varphi _ { t _ { m } } ^ { [ m ] } \circ _ { \nu , \dots , 0 } \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) = \int _ { 0 } ^ { t _ { 1 } } h _ { 1 } \Big ( \varphi _ { t } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t } \\ { \displaystyle \quad + \dots + \int _ { 0 } ^ { t _ { m } } h _ { m } \Big ( \varphi _ { t } ^ { [ m ] } \circ \varphi _ { t _ { m - 1 } } ^ { [ m - 1 ] } \circ _ { \nu , \dots } \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t , } \end{array}
$$

andweprove that it isa solution of the system $D _ { i } F = h _ { i }$ for $i = 1 , \ldots , m .$ Since only the last integral depends on $t _ { m }$ ,weimmediatelygetbydifferentiationwith respect to $t _ { m }$ that $D _ { m } F = h _ { m }$ For the computation of $D _ { i } F$ wedifferentiate with it integral gives respect to $t _ { i }$ Thefirst $h _ { i } ( \varphi _ { t _ { i } } ^ { [ i ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) )$ $i - 1$ integrals are independent of anthederivatiefthein $t _ { i }$ .The derivative of the integralsgives

$$
\begin{array} { r l r } {  { ^ { \rho t _ { j } } D _ { i } h _ { j } \Big ( \varphi _ { t } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t = \int _ { 0 } ^ { t _ { j } } D _ { j } h _ { i } \Big ( \varphi _ { t } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d \tau } } \\ & { } & { = h _ { i } \Big ( \varphi _ { t _ { j } } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) - h _ { i } \Big ( \varphi _ { t _ { j - 1 } } ^ { [ j - 1 ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) } \end{array}
$$

for $j = i + 1 , \dots , m .$ Summing up,this proves $D _ { i } F = h _ { i } .$

# VII.3.3 Coordinate Changes and the Darboux-Lie Theorem

Theemphasis here is to simplifya given Poisson structure as much as possible by a coordinate transformation.We change from coordinates $y _ { 1 } , \ldots , y _ { n }$ to $\widetilde { y } _ { 1 } ( y ) , \dots , \widetilde { y } _ { n } ( y )$ with continuously differentiable functions andan invertible Jacobian $A ( y ) = \partial \widetilde { y } / \partial y ,$ , and we denote $\widetilde F ( \widetilde y ) : = F ( y )$ and $\widetilde G ( \widetilde y ) : =$

![](images/fc653d630ace0da2aed89cf014b9c536fa8b4d828dd7c243f1fb277265cdfd4e.jpg)  
Fig.3.3.New coordinates ina Poisson system

![](images/2c4810bcf9efe411d690f095250efa9e46df05de5c66acdb54a42441e8b005cc.jpg)  
Jean Gaston Darboux

$G ( y )$ (seeFig.3.3).The Poisson structure aswell as the Poisson flow on one space willbecome another Poisson structure and flow on the other space by simply applying the chain rule:

$$
\sum _ { i , j } \frac { \partial F ( y ) } { \partial y _ { i } } b _ { i j } ( y ) \frac { \partial G ( y ) } { \partial y _ { j } } = \sum _ { i , j , k , l } \frac { \partial \widetilde { F } ( \widetilde { y } ) } { \partial \widetilde { y } _ { k } } \frac { \partial \widetilde { y } _ { k } } { \partial y _ { i } } b _ { i j } \big ( y ( \widetilde { y } ) \big ) \frac { \partial \widetilde { y } _ { l } } { \partial y _ { j } } \frac { \partial \widetilde { G } ( \widetilde { y } ) } { \partial \widetilde { y } _ { l } } .
$$

This is another Poisson structure with

$$
\widetilde { b } _ { k l } = \{ \widetilde { y } _ { k } , \widetilde { y } _ { l } \} \qquad \mathrm { o r } \qquad \widetilde { B } ( \widetilde { y } ) = A ( y ) B ( y ) A ( y ) ^ { T } .
$$

The same structure matrix is obtained if the Poisson system(2.12) is written in these newcoordinates (Exercise5).

Since $A$ isinvertible,the structure matrices $B$ and $\bar { B }$ have the same rank.We nowwant to obtain the simplest possible form for $\bar { B }$

Theorem3.4(Darboux 1882,Lie1888).Suppose that thematrix $B ( y )$ defines a Poisson bracket and is of constant rank $n - q \ = \ 2 m$ in $a$ neighbourhoodof $y _ { 0 } \in \mathbb { R } ^ { n } .$ Then,there exist functions $P _ { 1 } ( y ) , \dots , P _ { m } ( y )$ , $Q _ { 1 } ( y ) , \ldots , Q _ { m } ( y )$ ,and $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ satisfying

$$
\begin{array} { l l l } { { \{ P _ { i } , P _ { j } \} = 0 } } & { { \{ P _ { i } , Q _ { j } \} = - \delta _ { i j } } } & { { \{ P _ { i } , C _ { l } \} = 0 } } \\ { { \{ Q _ { i } , P _ { j } \} = \delta _ { i j } } } & { { \{ Q _ { i } , Q _ { j } \} = 0 } } & { { \{ Q _ { i } , C _ { l } \} = 0 } } \\ { { \{ C _ { k } , P _ { j } \} = 0 } } & { { \{ C _ { k } , Q _ { j } \} = 0 } } & { { \{ C _ { k } , C _ { l } \} = 0 } } \end{array}
$$

onaneighbourhood of $y _ { 0 }$ The gradientsof $P _ { i } , Q _ { i } , C _ { k }$ are linearly independent, sothat $y \mapsto \left( P _ { i } ( y ) , Q _ { i } ( y ) , C _ { k } ( y ) \right)$ constitutesa local change of coordinates to canonical form.

The functions $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ arecalleddistinguishedfunctions (ausgezeichneteFunktionen）by Lie.

Proof.We followLie'soriginal proof.Similarideas,andthe same notation,are alsopresent in Darboux'spaper.The proof proceeds in several steps,satisfying the conditions of(3.13),from one line tothe next,by solvingsystems of linear partial differential equations.

(a)If all $b _ { i j } ( y _ { 0 } ) = 0$ ,the constant rank assumption implies $b _ { i j } ( y ) = 0$ ina neighbourhood of $y _ { 0 }$ Wethus have $m = 0$ and all coordinates $C _ { i } ( y ) = y _ { i }$ are Casimirs.

（b)If there exist $i , j$ with $b _ { i j } ( y _ { 0 } ) \neq 0$ ,weset $Q _ { 1 } ( y ) = y _ { i }$ andwe determine $P _ { 1 } ( y )$ asthe solution of the linearpartial differential equation

$$
\{ Q _ { 1 } , P _ { 1 } \} = 1 .
$$

Because of $b _ { i j } ( y _ { 0 } ) \neq 0$ theassumption of Theorem 3.3is satisfied and thisyields the existence of $P _ { 1 }$ .We next consider the homogeneous system

$$
\{ Q _ { 1 } , F \} = 0 \qquad \mathrm { a n d } \qquad \{ P _ { 1 } , F \} = 0
$$

ofpartial differential equations.ByLemma 3.2and(3.14） theLie operatorscorrespondingto $Q _ { 1 }$ and $P _ { 1 }$ commute,sothatbyTheorem3.3 the system(3.15）has $n - 2$ independent solutions $F _ { 3 } , \ldots , F _ { n }$ Their gradients together with thoseof $Q _ { 1 }$ and $P _ { 1 }$ formabasis of $\mathbb { R } ^ { n }$ Wetherefore can change coordinates from $y _ { 1 } , \ldots , y _ { n }$ to $Q _ { 1 } , P _ { 1 } , F _ { 3 } , \ldots , F _ { n }$ （mapping $y _ { 0 }$ to $\scriptstyle { y _ { 0 } }$ ).In these coordinates the first two rows and the first two columns of the structure matrix $\hat { B } ( \widetilde { y } )$ have the required form.

(c）If $b _ { i j } ( \widetilde { y } _ { 0 } ) = 0$ for all $i , j \geq 3$ ,wehave $m = 1$ (similar to step(a)） and the coordinates $F _ { 3 } , \ldots , F _ { n }$ are Casimirs.

(d) If there exist $i \geq 3$ and $j \geq 3$ with $\hat { b } _ { i j } ( \widetilde { y } _ { 0 } ) \neq 0$ ,weset $Q _ { 2 } = F _ { i }$ andwe determine $P _ { 2 }$ fromthe inhomogeneous system

$$
\{ Q _ { 1 } , P _ { 2 } \} = 0 , \quad \{ P _ { 1 } , P _ { 2 } \} = 0 , \quad \{ Q _ { 2 } , P _ { 2 } \} = 1 .
$$

Theinhomogeneities satisfy (3.9),and the Lie operators corresponding to $Q _ { 1 }$ , $P _ { 1 }$ , $Q _ { 2 }$ commute (byLemma3.2).Theorem 3.3provesthe existence of such a $P _ { 2 }$ .We then consider the homogeneous system

$$
\{ Q _ { 1 } , F \} = 0 , \quad \{ P _ { 1 } , F \} = 0 , \quad \{ Q _ { 2 } , F \} = 0 , \quad \{ P _ { 2 } , F \} = 0
$$

andapply oncemore Theorem 3.3.We get $n - 4$ independent solutions,which we denote again $F _ { 5 } , \ldots , F _ { n }$ Asin part(b）of the proofwe get new coordinates $Q _ { 1 } , P _ { 1 } , Q _ { 2 } , P _ { 2 } , F _ { 5 } , \ldots , F _ { n }$ ,forwhich thefirst fourrowsand columns of the structurematrix are canonical.

(e)The proof now continues by repeating steps (c) and (d) until the structure matrix has thedesired form. □

Corollary3.5(CasimirFunctions).InthesituationofTheorem3.4thefunctions $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ satisfy

$$
\{ C _ { i } , H \} = 0 \qquad f o r a l l s m o o t h H .
$$

Proof.Theorem3.4 statesthat $\nabla C _ { i } ( y ) ^ { T } B ( y ) \nabla H ( y ) = 0$ ,when $H ( y )$ is one of the functions $P _ { j } ( y ) , Q _ { j } ( y )$ or $C _ { j } ( y )$ However,thegradients of these functions forma basis of ${ \mathbb { R } } ^ { n }$ Consequently, $\nabla C _ { i } ( y ) ^ { T } B ( y ) = 0$ and(3.16)is satisfied forall differentiable functions $H ( y )$ □

This property implies that all Casimir functions are first integrals of(2.12)whatever $H ( y )$ is.Consequently，(2.12）is (closeto $y _ { 0 }$ ）adifferential equation on the manifold

$$
{ \mathcal { M } } = \{ y \in U \mid C _ { i } ( y ) = C o n s t _ { i } , i = 1 , . . . , m \} .
$$

Corollary 3.6 (Transformation to Canonical Form).Denote the transformation ofTheorem3.4by $\boldsymbol { z } = \boldsymbol { \vartheta } ( y ) = \left( P _ { i } ( y ) , Q _ { i } ( y ) , C _ { k } ( y ) \right)$ With this changeof coordinates,the Poissonsystem $\dot { y } = B ( y ) \nabla H ( y )$ becomes

$$
\dot { z } = B _ { 0 } \nabla K ( z ) \qquad w i t h \qquad B _ { 0 } = \left( \begin{array} { r r } { { J ^ { - 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $K ( z ) = H ( y )$ Writing ${ z } = ( p , q , c )$ ,this systembecomes

$$
\dot { p } = - K _ { q } ( p , q , c ) , \qquad \dot { q } = K _ { p } ( p , q , c ) , \qquad \dot { c } = 0 .
$$

Proof. The transformed differential equation is

$$
\dot { z } = \vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } \nabla K ( z ) \qquad \mathrm { w i t h } \qquad y = \vartheta ^ { - 1 } ( z ) ,
$$

and Theorem3.4 states that $\vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } = B _ { 0 } ,$

# VII.4 Poisson Integrators

Before discussing geometric numerical integrators,we show that many important properties of Hamiltonian systems in canonical formremain valid for systems

$$
\begin{array} { r } { \dot { y } = B ( y ) \nabla H ( y ) , } \end{array}
$$

where $B ( y )$ represents a Poisson bracket.

# VII.4.1 Poisson Maps and Symplectic Maps

Wehave already seen that the Hamiltonian $H ( y )$ isafirst integral of(4.1).We shall showhere that the flow of(4.1) satisfiesaproperty closely related to symplecticity.

Definition 4.1.A transformation $\varphi : U \to \mathbb { R } ^ { n }$ (where $U$ is an open set in $\mathbb { R } ^ { n }$ )is calledaPoissonmapwith respect to the bracket (2.8),ifits Jacobian matrix satisfies

$$
\varphi ^ { \prime } ( y ) B ( y ) \varphi ^ { \prime } ( y ) ^ { T } = B \big ( \varphi ( y ) \big ) .
$$

Anequivalent condition is that forall smooth real-valued functions $F , G$ defined on $\varphi ( U )$ ,

$$
\{ F \circ \varphi , G \circ \varphi \} ( y ) = \{ F , G \} { \bigl ( } \varphi ( y ) { \bigr ) } ,
$$

asis seen by the chain rule and choosing $F , G$ asthe coordinate functions.It is clear from this condition that the composition of Poisson maps is again a Poisson map.Acomparison with (3.12) shows that Poisson maps leave the structurematrix invariant.

For the canonical symplectic structure,where $B ( y ) = J ^ { - 1 }$ ,condition (4.2） is equivalenttothe symplecticity ofthe transformation $\varphi ( y )$ Thiscan be seen by takingthe inverse of both sides of(4.2),and by multiplying the resulting equation with $\varphi ^ { \prime } ( y )$ from the right and with $\varphi ^ { \prime } ( y ) ^ { T }$ from the left.Alsoin the situation of a Hamiltonian system(2.17）ona symplectic submanifold $\mathcal { M }$ ,where $B ( y )$ is the structure matrix of the differential equationincoordinates $y$ asinTheorem2.8,condition (4.2)is equivalent to symplecticity in the sense of preserving the symplectic twoform(2.16) on the tangent space,as in(1.16):

Definition 4.2.A map $\psi : \mathcal { M }  \mathcal { M }$ ona symplectic manifold $\mathcal { M }$ is called symplecticif forevery $x \in \mathcal { M }$ ,

$$
\omega _ { \psi ( x ) } \left( \psi ^ { \prime } ( x ) \xi _ { 1 } , \psi ^ { \prime } ( x ) \xi _ { 2 } \right) = \omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) \qquad { \mathrm { f o r ~ a l l } } \quad \xi _ { 1 } , \xi _ { 2 } \in T _ { x } { \mathcal { M } } .
$$

A near-identity map $\psi : \mathcal { M }  \mathcal { M }$ is symplectic ifandonly if theconjugatemap $\varphi$ in local coordinates $x = \chi ( y )$ ,with $\varphi ( y )$ givenby $\psi ( x ) = \chi ( \varphi ( y ) )$ for $x = \chi ( y )$ , isa Poisson map for the structure matrix of(2.21), $B ( y ) = ( X ( y ) ^ { T } J X ( y ) ) ^ { - 1 }$ with $X ( y ) = X ^ { \prime } ( y )$ This holds because $\psi ^ { \prime } ( x ) \xi = X ( \varphi ( y ) ) \varphi ^ { \prime } ( y ) \eta$ for $x = \chi ( y )$ and $\xi = X ( y ) \eta$ ,and because (4.2) is equivalent to $\varphi ^ { \prime } ( y ) ^ { T } X ( \varphi ( y ) ) ^ { T } J X ( \varphi ( y ) ) \varphi ^ { \prime } ( y ) =$ $X ( y ) ^ { T } J X ( y )$

Theorem 4.3.1f $B ( y )$ isthe structurematrix ofaPoisson bracket,then theflow $\varphi _ { t } ( y )$ ofthedifferential equation(4.1)isa Poissonmap.

Proof.（a)For $B ( y ) = J ^ { - 1 }$ thisis exactly the statement of Theorem VI.2.4 on the symplecticity of the flow of Hamiltonian systems.This result can be extended ina straightforwardway tothematrix $B _ { 0 }$ of(3.18).

(b)For the general case consider the change of coordinates $z = \vartheta ( y )$ which transforms(4.1）tocanonical form(Theorem 3.4),i.e., $\vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } = B _ { 0 }$ and $\dot { z } = B _ { 0 } \nabla K ( z )$ with $K ( z ) = H ( y )$ (Corollary 3.6).Denoting theflows of(4.1)and $\dot { z } = B _ { 0 } \nabla K ( z )$ by $\varphi _ { t } ( y )$ and $\psi _ { t } ( z )$ ,respectively,we have $\psi _ { t } ( \vartheta ( y ) ) = \vartheta \big ( \varphi _ { t } ( y ) \big )$ and by the chain rule $\psi _ { t } ^ { \prime } \big ( \vartheta ( y ) \big ) \vartheta ^ { \prime } ( y ) = \vartheta ^ { \prime } \big ( \varphi _ { t } ( y ) \big ) \varphi _ { t } ^ { \prime } ( y ) .$ Inserting this relation into $\psi _ { t } ^ { \prime } ( z ) B _ { 0 } \psi _ { t } ^ { \prime } ( z ) ^ { T } = B _ { 0 }$ ,which follows from(a),proves the statement.

Adirect proof,avoidingtheuse of Theorem 3.4,is indicated in Exercise6.

FromTheorems2.8and4.3and theremarkafterDefinition4.2wenote the following.

Corollary4.4. Theflow ofa Hamiltoniansystem(2.17)ona symplectic submanifoldissymplectic.

Theinverse of Theorem 4.3isalso true.Itextends Theorem VI.2.6 fromcanonically symplectic transformationsto Poisson maps.

Theorem4.5.Let $f ( y )$ and $B ( y )$ becontinuously differentiable on an open set $U \subset \mathbb { R } ^ { m }$ and assume that $B ( y )$ representsa Poisson bracket (Definition 2.4). Then, $\dot { y } = f ( y )$ islocallyof theform(4.1),ifandonlyif

itsflow $\varphi _ { t } ( y )$ respects the Casimirsof $B ( y )$ ,i.e., $C _ { i } ( \varphi _ { t } ( y ) ) = C o n s t$ and its flow isaPoisson map for all $y \in U$ andforallsufficiently small t.

ProofThenecessity followsfromCorollary3.5and fromTheorem4.3.For the proof of suffciency we apply the change of coordinates $( u , c ) = \vartheta ( y )$ ofTheorem3.4,which transforms $B ( y )$ intocanonical form(3.18).Wewrite thedifferential equation ${ \dot { y } } = f ( y )$ in the new variables as

$$
\dot { u } = g ( u , c ) , \qquad \dot { c } = h ( u , c ) .
$$

Ourfirst assumption expresses the fact that the Casimirs,which are the components of $c$ ,arefirst integrals of this system.Consequently,we have $h ( u , c ) \equiv 0$ The secondassumption implies that theflow of（4.5）isaPoissonmap for $B _ { 0 }$ of(3.18). Writing downexplicitly the blocks of condition (4.2),we see that this is equivalent to the symplecticity of the mapping $u _ { 0 } \mapsto u ( t , u _ { 0 } , c _ { 0 } )$ ,with $c _ { 0 }$ asaparameter. FromTheorem VI.2.6we thus obtain the existence ofa function $K ( u , c )$ such that $g ( u , c ) = J ^ { - 1 } \nabla _ { u } K ( u , c ) .$ Notice that for flows depending smoothly ona parameter, theHamiltonian also depends smoothly on it.Consequently,the vector field(4.5) is of the form $B _ { 0 } \nabla K ( u , c )$ Transforming back to the original variableswe obtain $f ( y ) = B ( y ) \nabla H ( y )$ with $H ( y ) = K ( \vartheta ( y ) )$ (see Corollary 3.6). □

# VII.4.2 Poisson Integrators

The preceding theorem shows that“beingaPoisson map and respecting the Casimirs” is characteristic for the flow of a Poisson system.This motivates the following definition.

Definition 4.6.A numerical method $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ isaPoisson integrator for the structure matrix $B ( y )$ ,if the transformation $y _ { 0 } \mapsto y _ { 1 }$ respects the Casimirs and if it isaPoisson map whenever the method is applied to (4.1).

Observe that for a Poisson integrator one has to specify the class of structure matrices $B ( y )$ .Amethod will never beaPoisson integrator forall possible $B ( y )$ .

Example 4.7.The symplectic Euler method reads

$$
\ l _ { n + 1 } = u _ { n } + h u _ { n + 1 } v _ { n } H _ { v } ( u _ { n + 1 } , v _ { n } ) , \quad v _ { n + 1 } = v _ { n } - h u _ { n + 1 } v _ { n } H _ { u } ( u _ { n + 1 } , v _ { n } )
$$

fortheLotka-Volterra problem(2.13).It produces an excellent long-time behaviour (Fig.4.1,left picture).We shall show that this isaPoissonintegrator forall separable Hamiltonians $H ( u , v ) = K ( u ) + L ( v ) .$ For this we compute the Jacobian of the map $( u _ { n } , v _ { n } ) \mapsto ( u _ { n + 1 } , v _ { n + 1 } )$ ，

$$
{ \binom { 1 - h v _ { n } H _ { v } } { h v _ { n } ( H _ { u } + u _ { n + 1 } H _ { u u } ) } } \quad { \overset { 0 } { 1 } } { \bigg ( } { \frac { \partial ( u _ { n + 1 } , v _ { n + 1 } ) } { \partial ( u _ { n } , v _ { n } ) } } { \bigg ) } = { \binom { 1 } { 0 } } \quad \quad h u _ { n + 1 } ( H _ { v } + v _ { n } H _ { v v } )
$$

(theargument of thepartial derivatives of $H$ is $\left( u _ { n + 1 } , v _ { n } \right)$ everywhere),and we checkina straightforward fashion thevalidity of(4.2).Adifferent proof,using differential forms,is givenin Sanz-Serna(1994) fora special choiceof $H ( u , v )$ . Similarly,the adjoint of thesymplectic Euler method isa Poisson integrator,and sois their composition-the Stormer-Verlet scheme.Composition methods based onthis scheme yield high order Poisson integrators,because the composition of Poisson mapsis againa Poisson map.

The implicit midpoint rule,though symplectic whenapplied to canonical Hamiltonian systems,turns out not to bea Poisson map for the structure matrix $B ( u , v )$ of (2.13).Figure 4.1(right picture) shows that the numerical solution does not remain nearaclosed curve.

Itisadifcult task to construct Poisson integrators for general Poissonsystems; cf.the overview by Karasozen (2oo4).First of all,for non-constant $B ( y )$ condition(4.2）isno longera quadratic first integral of the problem augmented by its variational equation (see Sect.VI.4.1).Secondly,the Casimir functions can be arbitraryand weknow that only linear and quadratic first integralscan be conserved automatically(Chap.IV).Therefore,Poisson integratorswill have to exploit special structures of the particular problem.

SplittingMethods.Considera（general） Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ and suppose that the Hamiltonian permits a decomposition as $H ( y ) = H ^ { [ 1 ] } ( y ) + \ldots +$

![](images/281cb5f50771a756a88176691abd042384986d0219a20717d427cd84caadcfd8.jpg)  
Fig.4.1.Numerical solutions of theLotka-Volterr equations (2.13) (step size $h = 0 . 2 5$ , whichisverylargecomparedtotheperiodofthesolution;ooOsteps;initialvalues $( 4 , 2 )$ and $( 6 , 2 )$ for all methods)

$H ^ { [ m ] } ( y )$ ,such that the individual systems $\dot { y } = B ( y ) \nabla H ^ { [ i ] } ( y )$ can be solved exactly.The flow of these subsystemsisa Poisson map and automaticallyrespects theCasimirs,and so does their composition.McLachlan (1993),Reich (1993),and McLachlan&Quispel(2oo2) present several interesting examples.

Example 4.8.In the previous example of aLotka-Volterra equationwith separable Hamiltonian $H ( u , v ) = K ( u ) + L ( v )$ ,thesystemswith Hamiltonian $K ( u )$ and $L ( v )$ canbe solved explicitly.Since theflow of each of the subsystems is aPoisson map,so is their composition.Combininga half-step with $L$ afull stepwith $K$ ， and againa half-stepwith $L$ ,wethusobtain the followingVerlet-like second-order Poisson integrator:

$$
\begin{array} { r c l } { u _ { n + 1 / 2 } } & { = } & { \exp \bigl ( \frac { h } { 2 } v _ { n } \nabla L ( v _ { n } ) \bigr ) u _ { n } } \\ { v _ { n + 1 } } & { = } & { \exp \bigl ( - h u _ { n + 1 / 2 } \nabla K ( u _ { n + 1 / 2 } ) \bigr ) v _ { n } } \\ { u _ { n + 1 } } & { = } & { \exp \bigl ( \frac { h } { 2 } v _ { n + 1 } \nabla L ( v _ { n + 1 } ) \bigr ) u _ { n + 1 / 2 } . } \end{array}
$$

In the setting of Hamiltonian systems ona manifold,the splittingapproach can be formulated in the following way.

Variational Splitting.Considera Hamiltoniansystem(2.17) ona symplectic manifold $\mathcal { M }$ ,anduse a splitting $H = H ^ { [ 1 ] } + H ^ { [ 2 ] }$ of the Hamiltonian in the following algorithm:

1. Let $x _ { n } ^ { + } \in \mathcal { M }$ be the solution at time $h / 2$ of the equation for $_ { x }$

$$
( J { \dot { x } } - \nabla H ^ { [ 1 ] } ( x ) , \xi ) = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { x } { \mathcal { M } }
$$

with initial value $x ( 0 ) = x _ { n }$

2.Let $x _ { n + 1 } ^ { - }$ be the solution at time $h$ of

$$
( J { \dot { x } } - \nabla H ^ { [ 2 ] } ( x ) , \xi ) = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { x } { \mathcal { M } }
$$

with initial value $x ( 0 ) = x _ { n } ^ { + }$

3. Take $x _ { n + 1 }$ as the solution at time $h / 2$ of (4.7) with initialvalue $x ( 0 ) = x _ { n + 1 } ^ { - }$

Splitting algorithms for Hamiltonian systems on manifolds have been studied by Dullweber,Leimkuhler&McLachlan（1997）and Benettin,Cherubini& Fasso (2001)in the context of rigid body dynamics;see Sect.VII.5.Lubich (2004) and Faou&Lubich(2Oo4) have studied the above splitting method for applications in quantum moleculardynamics;see Sect.VII.6 for an example.

ByTheorem 2.8,the substeps 1.-3.written incoordinates $x = \chi ( y )$ are Poisson systems $\dot { y } = B ( y ) \nabla K ^ { [ i ] } ( y )$ with $K ^ { [ i ] } ( y ) = H ^ { [ i ] } ( \chi ( y ) )$ ,butthe algorithm itself isindependent of the choice of coordinates.Since the substeps are exact flows of Hamiltonian systems on the manifold $\mathcal { M }$ ,theircomposition yieldsa symplectic map.In the coordinates $y$ thesubsteps are the exact flows of Poisson systems,and hence their composition yieldsa Poisson map.

Poisson Integrators and Symplectic Integrators.Generally we note the followingcorrespondence,which rephrases the remark on symplectic mapsand Poisson mapsafterDefinition 4.2.Itapplies in particularto thesymplectic integratorsfor constrained mechanics of Sect.VII.1.

Lemma4.9.Anintegrator $x _ { 1 } = \varPsi _ { h } ( x _ { 0 } )$ fora Hamiltonian system (2.17)on a manifold $\mathcal { M }$ issymplecticifandonlyif the integratorwritten inlocalcoordinates, $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ corresponding to a coordinate map $x = \chi ( y )$ ,isaPoissonintegrator forthe structure matrix $B ( y )$ of(2.21).

# VII.4.3Integrators Based on the Darboux-Lie Theorem

If weexplicitly know a transformation $z ~ = ~ \vartheta ( y )$ that brings the system $\dot { y } =$ $B ( y ) \nabla H ( y )$ to canonical form (asin Corollary 3.6),wecanproceed as follows:compute $z _ { n } = \vartheta ( y _ { n } )$ ;applyasymplectic integrator to the transformed system $\dot { z } ~ = ~ B _ { 0 } \nabla K ( z )$ （ $B _ { 0 }$ is thematrix(3.18）and $K ( z ) \ = \ H ( y ) )$ whichyields $z _ { n + 1 } = \varPsi _ { h } ( z _ { n } )$ ;computefinally $y _ { n + 1 }$ from $z _ { n + 1 } = \vartheta ( y _ { n + 1 } ) .$ Thisyields a Poisson integratorby the followinglemma.

Lemma 4.10.Let $\boldsymbol { z } = ( u , c ) = \boldsymbol { \vartheta } ( y )$ bethetransformationof Theorem 3.4.Supposethat the integrator $\varPhi _ { h } ( y )$ takestheform

$$
\varPsi _ { h } ( z ) = \left( \begin{array} { c } { \varPsi _ { h } ^ { 1 } ( u , c ) } \\ { c } \end{array} \right)
$$

in the new variables $z = ( u , c )$ .Then, $\varPhi _ { h } ( y )$ isaPoisson integratorifandonlyif $u \mapsto \varPsi _ { h } ^ { 1 } ( u , c )$ isasymplectic integrator for everyc.

Proof. The integrator $\varPhi _ { h } ( y )$ is Poisson for the structure matrix $B ( y )$ ifand only if $\varPsi _ { h } ( z )$ is Poisson for the matrix $B _ { 0 }$ of(3.18);see Exercise 7.By assumption, $\varPsi _ { h } ( z )$ preserves the Casimirs of $B _ { 0 }$ .Theidentity

$$
\varPsi _ { h } ^ { \prime } ( z ) B _ { 0 } \varPsi _ { h } ^ { \prime } ( z ) ^ { T } = \left( \begin{array} { c c } { A J ^ { - 1 } A ^ { T } } & { 0 } \\ { 0 } & { 0 } \end{array} \right)
$$

with $A = \partial \varPsi _ { h } ^ { 1 } / \partial u$ proves the statement.

Notice that the transformation $\vartheta$ hasto be global in the sense that it has to be thesame for all integration steps.Otherwiseadegradationin performance,similar tothatof the experiment inExampleV.4.3,has to beexpected.

Example 4.11.Asa first illustration consider theLotka-Volterra system (2.13). Applyingthe transformation $\vartheta ( u , v ) = ( \ln u , \ln v ) = ( p , q )$ ,thissystem becomes canonicallyHamiltonian with

$$
K ( p , q ) = - H ( u , v ) = - H ( e ^ { p } , e ^ { q } ) .
$$

Ifweapply the symplectic Euler method to this Hamiltonian system,and if we transform back to the original variables,we obtain the method

$$
\begin{array} { r l } & { u _ { n + 1 } ~ = ~ u _ { n } \exp \bigl ( h v _ { n } H _ { v } ( u _ { n + 1 } , v _ { n } ) \bigr ) , } \\ & { v _ { n + 1 } ~ = ~ v _ { n } \exp \bigl ( - h u _ { n + 1 } H _ { u } ( u _ { n + 1 } , v _ { n } ) \bigr ) . } \end{array}
$$

Incontrast to themethod ofExample4.7,(4.9)isalsoaPoisson integrator for(2.13) if $H ( u , v )$ is not separable.If we compose a step with step size $h / 2$ of the symplecticEuler method with itsadjoint method,thenwe obtain again,in the case ofa separable Hamiltonian,the method (4.6).

Example 4.12 (Ablowitz-Ladik Discrete Nonlinear Schrodinger Equation). Aninteresting space discretization of the nonlinear Schrodinger equation is the Ablowitz-Ladikmodel

$$
i \dot { y } _ { k } + \frac { 1 } { \Delta x ^ { 2 } } \big ( y _ { k + 1 } - 2 y _ { k } + y _ { k - 1 } \big ) + \lvert y _ { k } \rvert ^ { 2 } \big ( y _ { k + 1 } + y _ { k - 1 } \big ) = 0 ,
$$

which we consider under periodic boundary conditions $y _ { k + N } = y _ { k }$ （ $\varDelta x = 1 / N$ ). Itiscompletely integrable(Ablowitz-Ladik1976)and,aswe shall see below,it isa Poisson system with noncanonical Poisson bracket.Splitting the variables into real and imaginaryparts, $y _ { k } = u _ { k } + i v _ { k }$ ,weobtain

$$
\begin{array} { r c l } { \dot { u } _ { k } } & { = } & { \displaystyle - \frac { 1 } { \Delta x ^ { 2 } } \big ( v _ { k + 1 } - 2 v _ { k } + v _ { k - 1 } \big ) - \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) \big ( v _ { k + 1 } + v _ { k - 1 } \big ) } \\ { \dot { v } _ { k } } & { = } & { \displaystyle \frac { 1 } { \Delta x ^ { 2 } } \big ( u _ { k + 1 } - 2 u _ { k } + u _ { k - 1 } \big ) + \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) \big ( u _ { k + 1 } + u _ { k - 1 } \big ) . } \end{array}
$$

With $u = ( u _ { 1 } , \dotsc , u _ { N } )$ , $v = ( v _ { 1 } , \ldots , v _ { N } )$ this system can be writen as

$$
\left( \begin{array} { c } { \dot { u } } \\ { \dot { v } } \end{array} \right) = \left( \begin{array} { c c } { 0 } & { - D ( u , v ) } \\ { D ( u , v ) } & { 0 } \end{array} \right) \left( \begin{array} { c } { \nabla _ { u } H ( u , v ) } \\ { \nabla _ { v } H ( u , v ) } \end{array} \right) ,
$$

where $D = \mathrm { d i a g } ( d _ { 1 } , \dots , d _ { N } )$ is thediagonal matrix with entries

$$
d _ { k } ( u , v ) = 1 + \Delta x ^ { 2 } \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) ,
$$

and the Hamiltonian is

$$
H ( u , v ) = \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } \Bigl ( u _ { l } u _ { l - 1 } + v _ { l } v _ { l - 1 } \Bigr ) - \frac { 1 } { \varDelta x ^ { 4 } } \sum _ { l = 1 } ^ { N } \ln \bigl ( 1 + \varDelta x ^ { 2 } ( u _ { l } ^ { 2 } + v _ { l } ^ { 2 } ) \bigr ) .
$$

Wethus getaPoisson system (the conditions ofLemma 2.3are directly verified). Thereare many possibilities to transform thissystem to canonical form.Tang, Pérez-Garcia&Vazquez（1997)propose the transformation

$$
p _ { k } = \frac { 1 } { \varDelta x \sqrt { 1 + \varDelta x ^ { 2 } v _ { k } ^ { 2 } } } \arctan \Bigl ( \frac { \varDelta x } { \sqrt { 1 + \varDelta x ^ { 2 } v _ { k } ^ { 2 } } } \cdot u _ { k } \Bigr ) , \qquad q _ { k } = v _ { k } ,
$$

forwhich the inversecanbecomputedinastraightforward way.Here,we suggest the transformation

$$
\begin{array} { l } { { p _ { k } = u _ { k } \sigma \big ( \varDelta x ^ { 2 } ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } ) \big ) } } \\ { { q _ { k } = v _ { k } \sigma \big ( \varDelta x ^ { 2 } ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } ) \big ) } } \end{array} \qquad \mathrm { w i t h } \qquad \sigma ( x ) = \sqrt { \frac { \ln ( 1 + x ) } { x } } ,
$$

which treats the variables more symmetrically.Itsinverseis

$$
\left. \begin{array} { l } { { u _ { k } = p _ { k } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { k } ^ { 2 } + q _ { k } ^ { 2 } ) \bigr ) } } \\ { { v _ { k } = q _ { k } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { k } ^ { 2 } + q _ { k } ^ { 2 } ) \bigr ) } } \end{array} \right. \qquad \mathrm { w i t h } \qquad \tau ( x ) = \frac { \exp { x } - 1 } { x } .
$$

Both transformations takethe system(4.1O) to canonical form.For the transformation(4.11）the Hamiltonianin thenewvariablesis

$$
\begin{array} { c } { { \displaystyle ( p , q ) = \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { l } ^ { 2 } + q _ { l } ^ { 2 } ) \bigr ) \tau \bigl ( \varDelta x ^ { 2 } ( p _ { l - 1 } ^ { 2 } + q _ { l - 1 } ^ { 2 } ) \bigr ) \Bigl ( p _ { l } p _ { l - 1 } + q _ { l } q _ { l - 1 } \Bigr ) } } \\ { { - \displaystyle \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } ( p _ { l } ^ { 2 } + q _ { l } ^ { 2 } ) . } } \end{array}
$$

Applying standard symplectic schemes to this Hamiltonian yields Poisson integrators for(4.10）.

# VII.5 Rigid Body Dynamicsand Lie-Poisson Systems

..these topics,which,after all,have occupied workers in geometric mechanicsformanyyears. （R.McLachlan 2003）

Animportant Poisson system is given by Euler's famous equations for the motionof arigidbody(see left picture ofFig.5.1）,forwhichwe recall the history and derivation and present various structure-preserving integrators.Euler's equationsare aparticular case ofLie-Poisson systems,which result from areduction process of Hamiltonian systems on a Lie group.

# VI1.5.1 Historyof theEuler Equations

“Lesujet que jeme propose detraiterici,est dela derniere importance dansla Mecanique;&j'ai deja faitplusieurs efforts pourlemetre dans tout son jour.Mais,quoiquele calcul ait assesbienreussi,&que j’ai decouvert desformules analytiques.,leur application étoit pourtant assujettieades difficultes qui $\mathbf { m } ^ { \prime }$ ontparu presque toutafait insurmontables. Or,depuis que j'ai developé les principes de la conoissance mecanique des corps,la belle propriete des trois axes principaux dont chaque corps est doué,m’a enfin mis en état de vaincre toutes ces difficultés,..

(Euler1758b,p.154)

Agreat challenge forEuler were his effortsto establish amathematical analysis for themotion ofarigid body.Due tothe factthat sucha bodycan haveanarbitrary shape and mass distribution (see left picture of Fig.5.2),and that therotation axis canarbitrarily movewith time,theproblemisdifficultand Euler struggled formany years(all these articlesare collected in OperaOmnia,Ser.II,Vols.7and 8).The breakthroughwas enabled bythediscovery thatany body,ascomplicatedasmaybe itsconfiguration,reduces toan inertia ellipsoid with three principal axesand three numbers,the principal moments of inertia(Euler 1758a;see themiddle pictureof Fig.5.2 and the citation).

![](images/8ee9f0d7c83432acf66bcb394669596405b4c2f2967219038991797e6c0400eb.jpg)  
Fig.5.1.Left picture:first publication of the Euler equations in Euler(1758b).Right picture: principal axesas eigenvectors inLagrange（1788)

TheInertia Ellipsoid.We choose a moving coordinate system connected to the body $B$ andwe consider motions of the bodywhere the origin is fixed.By another ofEuler's famous theorems,any such motion isinfinitesimallyarotation around an axis.Werepresent therotationaxisof the body bythedirectionofavector $\omega$ and the speed of rotation bythe length of $\omega$ .Thenthevelocity of amass point $x$ of $\boldsymbol { B }$ is given by the exterior product

$$
v = \omega \times x = { \left( \begin{array} { l } { \omega _ { 2 } x _ { 3 } = \omega _ { 3 } x _ { 2 } } \\ { \omega _ { 3 } x _ { 1 } - \omega _ { 1 } x _ { 3 } } \\ { \omega _ { 1 } x _ { 2 } - \omega _ { 2 } x _ { 1 } } \end{array} \right) } = { \left( \begin{array} { l l l } { 0 } & { - \omega _ { 3 } } & { \omega _ { 2 } } \\ { \omega _ { 3 } } & { 0 } & { - \omega _ { 1 } } \\ { - \omega _ { 2 } } & { \omega _ { 1 } } & { 0 } \end{array} \right) } { \left( \begin{array} { l } { { \bar { x } } _ { 1 } } \\ { { \bar { x } } _ { 2 } } \\ { { \bar { x } } _ { 3 } } \end{array} \right) }
$$

(orthogonal to $\omega$ orthogonal to $_ { x }$ ,and of length $\| { \boldsymbol { \omega } } \| \cdot \| { \boldsymbol { x } } \| \cdot \sin \gamma$ see the left picture ofFig.5.2).Thekinetic energyisobtained byintegratingtheenergy of themass

![](images/847ebebca93ad6ce67aed064593ada51e8299a5433c2e707f110c87ed6659309.jpg)  
Fig.5.2.Arigid bodyrotatingarounda variableaxis (left);thecorresponding inertiaellipsoid (middle); the corresponding angular momentum (right)

points $d m$ over the body

$$
\begin{array} { l } { T = \displaystyle \frac 1 2 \int _ { B } \| \omega \times x \| ^ { 2 } d m } \\ { = \displaystyle \frac 1 2 \int _ { B } \left( ( \omega _ { 2 } x _ { 3 } - \omega _ { 3 } x _ { 2 } ) ^ { 2 } \mp ( \omega _ { 3 } x _ { 1 } - \omega _ { 1 } x _ { 3 } ) ^ { 2 } \mp ( \omega _ { 1 } x _ { 2 } - \omega _ { 2 } x _ { 1 } ) ^ { 2 } \right) d m . } \end{array}
$$

If this is multiplied out,one obtains

$$
T = { \frac { 1 } { 2 } } \omega ^ { T } \theta \omega , \mathrm { w h e r e } \theta _ { i i } = \int _ { B } ( x _ { k } ^ { 2 } + x _ { \ell } ^ { 2 } ) d m , \theta _ { i k } = - \int _ { B } x _ { i } x _ { k } d m , ( i \neq k , \pm k ) \in \Omega ,
$$

Euler(1758a) showed,by endlesstrigonometric transformations,that there exist principal axes ofthe body in which this expression takes the form

$$
T = \frac { 1 } { 2 } \Big ( I _ { 1 } \omega _ { 1 } ^ { 2 } + I _ { 2 } \omega _ { 2 } ^ { 2 } + I _ { 3 } \omega _ { 3 } ^ { 2 } \Big ) .
$$

Thiswas historically the first transformation of such a3 $\times$ 3quadraticformtodiagonalform.Later,Lagrange(1788)discovered that theseaxeswere the eigenvectorsof thematrix $\Theta$ and themoments of inertia $I _ { k }$ thecorresponding eigenvalues(without calling them so,see the right picture of Fig.5.1).

TheAngular Momentum.The firstlaw ofNewton'sPrincipia states that themomentum $v \cdot m$ ofamasspoint remainsconstant in the absence of exterior forces. Thecorresponding quantity for rotational motion is the angular momentum,i.e., the exterior product $x \times v$ times the mass.Integrating over the body we obtain,with (5.1）,

$$
\boldsymbol { y } = \int _ { \boldsymbol { B } } ( \boldsymbol { x } \times \boldsymbol { v } ) d m = \int _ { \boldsymbol { B } } \bigl ( \boldsymbol { x } \times ( \boldsymbol { \omega } \times \boldsymbol { x } ) \bigr ) d m .
$$

If this ismultiplied out,the matrix $\Theta$ appears again and one obtains the surprising result(due to Poinsot 1834）

$$
y = \theta \omega , \qquad \mathrm { o r , i n t h e \ p r i n c i p a l ~ a x e s \ c o o r d i n a t e s , } \qquad y _ { k } = I _ { k } \omega _ { k } .
$$

Sucharelation is familiar from the theory of conjugate diameters (Apollonius,Book II,Prop.VI):the angular momentum isa vector orthogonal to theplane of vectors conjugateto $\omega$ (see theright picture of Fig.5.2）.

TheEuler Equations.Euler’s paper(1758a),on his discovery of the principal axes, isimmediately followed byEuler(1758b),where hederives hisequations for the motion ofa rigid body by long,doubtful and often criticized calculations,repeated ina litle less doubtful manner in Euler'smonumental treatise(1765).Beauty and elegance,not only of the result,butalso of the proof,isdue to Poinsot(1834）and Hayward（1856).ItismasterlydescribedbyKlein&Sommerfeld（1897),andin Chapter6of Arnold(1989).

From now on we choose the coordinate system,movingwith the body,such that theinertia tensor remainsdiagonal.Wealsowatch themotion of thebody from a coordinate system stationary in the space.The transformation ofavector $x \in \mathbb { R } ^ { 3 }$ in thebody frame4,to thecorresponding $\widetilde { x } \in \mathbb R ^ { 3 }$ in the stationary frame,isdenoted by

$$
\widetilde { x } = Q ( t ) x .
$$

Thematrix $Q ( t )$ is orthogonal and describes the motion of the body: for $x = e _ { i }$ we see that the columns of $Q ( t )$ are the coordinates of the body's principal axes in the stationaryframe.

Theanalogousstatement to Newton's first lawforrotational motion is:inthe absence ofexterior angular forces,the angular momentum $\bar { y }$ seenfromthefixed coordinate system,isaconstant vector5.Thissamevector $y$ seen from themoving frame,whichatany instancerotateswith the body around thevector $\boldsymbol { \omega }$ ,rotatesin the opposite direction.Therefore we have from (5.1),by changing the signs of $\boldsymbol { \omega }$ , thederivatives

$$
\begin{array} { r } { \left( \begin{array} { c } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { 0 } & { \omega _ { 3 } } & { - \omega _ { 2 } } \\ { - \omega _ { 3 } } & { 0 } & { \omega _ { 1 } } \\ { \omega _ { 2 } } & { - \omega _ { 1 } } & { 0 } \end{array} \right) \left( \begin{array} { c } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right) . } \end{array}
$$

If we insert $\omega _ { k } = y _ { k } / I _ { k }$ from (5.6),we obtain

$$
\left( { \begin{array} { c } { { \dot { y } _ { 1 } } } \\ { { \dot { y } _ { 2 } } } \\ { { \dot { y } _ { 3 } } } \end{array} } \right) = \left( { \begin{array} { c c c } { { 0 } } & { { y _ { 3 } / I _ { 3 } } } & { { - y _ { 2 } / I _ { 2 } } } \\ { { - y _ { 3 } / I _ { 3 } } } & { { 0 } } & { { y _ { 1 } / I _ { 1 } } } \\ { { y _ { 2 } / I _ { 2 } } } & { { - y _ { 1 } / I _ { 1 } } } & { { 0 } } \end{array} } \right) { \binom { y _ { 1 } } { y _ { 3 } } } = \left( { \begin{array} { c } { { ( I _ { 3 } ^ { - 1 } - I _ { 2 } ^ { - 1 } ) y _ { 3 } y _ { 2 } } } \\ { { ( I _ { 1 } ^ { - 1 } - I _ { 3 } ^ { - 1 } ) y _ { 1 } y _ { 3 } } } \\ { { ( I _ { 2 } ^ { - 1 } - I _ { 1 } ^ { - 1 } ) y _ { 2 } y _ { 1 } } } \end{array} } \right)
$$

or,byrearranging theproducts theotherwayround,

$$
\begin{array} { r } { \left( \begin{array} { l } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} \right) \left( \begin{array} { l } { y _ { 1 } / I _ { 1 } } \\ { y _ { 2 } / I _ { 2 } } \\ { y _ { 3 } / I _ { 3 } } \end{array} \right) , } \end{array}
$$

$C ( y ) = \textstyle { \frac { 1 } { 2 } } \sum _ { k = 1 } ^ { 3 } y _ { k } ^ { 2 }$ iand $\begin{array} { r } { H ( y ) = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { 3 } I _ { k } ^ { - 1 } y _ { k } ^ { 2 } } \end{array}$ Theseare the two quadratic invariants ofChap.IV.The first represents the length of the constant angular momentum $\bar { y }$ in the orthogonal body frame,and the second represents the energy(5.4).

Computation of the Position Matrix $Q ( t )$ Once we have solved the Euler equationsfor $y ( t )$ ,we obtain the rotation vector $\omega ( t )$ by(5.6).Itremains to find thematrix $Q ( t )$ which gives the position of our rotating body.We know that the columns of thematrix $Q$ ,seen in the stationary frame,correspond tothe unit vectors $e _ { i }$ in the bodyframe.Theserotate,by(5.1),with the velocity

$$
\Bigl ( \omega \times e _ { 1 } , \omega \times e _ { 2 } , \omega \times e _ { 3 } \Bigr ) = \left( \begin{array} { c c c } { { 0 } } & { { - \omega _ { 3 } } } & { { \omega _ { 2 } } } \\ { { \omega _ { 3 } } } & { { 0 } } & { { - \omega _ { 1 } } } \\ { { - \omega _ { 2 } } } & { { \omega _ { 1 } } } & { { 0 } } \end{array} \right) = W .
$$

We thus obtain $\dot { Q }$ ,therotational velocity expressed inthe stationary frame,by the back transformation (5.7):

$$
{ \dot { Q } } = Q W \qquad { \mathrm { o r } } \qquad Q ^ { T } { \dot { Q } } = W .
$$

Thisisadifferential system for $Q$ which,because $W$ is skew-symmetric,preserves the orthogonality of $Q .$ The problem is solved $-$ intheory.

# VII.5.2 Hamiltonian Formulation of Rigid Body Motion

Inorder to openthedoor for efficient numericalalgorithms,we treat therigid body asaconstrainedHamiltonian system.

Position Variables.Theposition of therigid bodyat time $t$ isdetermined,inview of(5.7),byathree-dimensional orthogonal matrix $Q ( t )$ The constraints to be respected are thus $Q ^ { I } Q - I = 0$ .

Kinetic Energy.Asin(5.12),we associate with $Q$ and $\dot { Q }$ the skew-symmetric matrix $W = Q ^ { T } \dot { Q }$ whose entries $\omega _ { k }$ ,arrangedasin(5.11),determine thekinetic energy by(5.4）:

$$
T = { \frac { 1 } { 2 } } \big ( I _ { 1 } \omega _ { 1 } ^ { 2 } + I _ { 2 } \omega _ { 2 } ^ { 2 } + I _ { 3 } \omega _ { 3 } ^ { 2 } \big ) .
$$

Forany diagonal matrix $D = \mathrm { d i a g } ( d _ { 1 } , d _ { 2 } , d _ { 3 } )$ we observe

$$
\mathrm { t r a c e } ( W D W ^ { T } ) = ( d _ { 2 } + d _ { 3 } ) { \omega } _ { 1 } ^ { 2 } + ( d _ { 3 } + d _ { 1 } ) { \omega } _ { 2 } ^ { 2 } + ( d _ { 1 } + d _ { 2 } ) { \omega } _ { 3 } ^ { 2 } .
$$

Therefore,with

$$
I _ { 1 } = d _ { 2 } + d _ { 3 } , I _ { 2 } = d _ { 3 } + d _ { 1 } , I _ { 3 } = d _ { 1 } + d _ { 2 } \mathrm { o r } d _ { k } = \int _ { \cal B } x _ { k } ^ { 2 } d m \ ,
$$

（note that $d _ { k } \ > \ 0$ forall bodiesthat have interior points),we obtain the kinetic energyas

$$
T = { \frac { 1 } { 2 } } \operatorname { t r a c e } \left( W D W ^ { T } \right) .
$$

Inserting $W = Q ^ { T } Q$ ,wehave

$$
T = { \frac { 1 } { 2 } } \operatorname { t r a c e } { ( Q ^ { T } \dot { Q } D \dot { Q } ^ { T } Q ) } = { \frac { 1 } { 2 } } \operatorname { t r a c e } { ( \dot { Q } D \dot { Q } ^ { T } ) } ,
$$

since $Q$ is an orthogonal matrix.

ConjugateVariables.We now have anexpression for thekinetic energy in termsof derivatives of position coordinates and are able to introduce the conjugate momenta

$$
P = \partial T / \partial { \dot { Q } } = { \dot { Q } } D .
$$

If we suppose to have,inaddition to $T$ ,apotential $U ( Q ) ,$ we get the Hamiltonian

$$
H ( P , Q ) = \textstyle { \frac { 1 } { 2 } } \operatorname { t r a c e } { \big ( } P D ^ { - 1 } P ^ { T } { \big ) } + U ( Q ) .
$$

LagrangeMultipliers.The constraints are given by the orthogonality of $\boldsymbol { \mathcal { Q } }$ ,i.e.,the equation $g ( Q ) = Q ^ { T } Q - I = 0 ,$ Since thismatrix is always symmetric,this consists of $\frac { 1 } { 2 } n ( n + 1 ) = 6$ independent algebraic conditions,calling for six Lagrangemultipliers.If the expression $G ( Q ) ^ { \tau } \lambda$ in(1.9)is actually computed, it turns out that this term becomes the product $Q \varLambda$ ,where the sixLagrange multipliersare arranged in a symmetric matrix $\varLambda$ ;seealso formula(IV.9.6).Thus,theconstrainedHamiltonian system(1.9）reads in our case,with $\nabla U = \left( \partial U / \partial Q _ { i j } \right)$ ，

$$
\begin{array} { r c l } { { \dot { Q } } } & { { = } } & { { P D ^ { - 1 } } } \\ { { \dot { P } } } & { { = } } & { { - \nabla U ( Q ) - Q \Lambda \qquad \mathrm { ( \nabla { A } \ s y m m e t r i c ) } } } \\ { { 0 } } & { { = } } & { { Q ^ { T } Q - I . } } \end{array}
$$

Reduction to theEuler Equations.The key idea is to introduce thematrix

$$
Y = Q ^ { T } P = Q ^ { T } \dot { Q } D = W D = \left( \begin{array} { c c c } { { 0 } } & { { - d _ { 2 } \omega _ { 3 } } } & { { d _ { 3 } \omega _ { 2 } } } \\ { { d _ { 1 } \omega _ { 3 } } } & { { 0 } } & { { - d _ { 3 } \omega _ { 1 } } } \\ { { - d _ { 1 } \omega _ { 2 } } } & { { d _ { 2 } \omega _ { 1 } } } & { { 0 } } \end{array} \right) ,
$$

where the $\omega _ { k }$ can be further expressed in terms of theangularmomenta $y _ { k } = I _ { k } \omega _ { k }$ Using the notation skew $( A ) = { \textstyle { \frac { 1 } { 2 } } } ( A - A ^ { \mathit { 1 } } )$ we see,with(5.13）,that

$$
Y - Y ^ { T } = 2 \operatorname { s k e w } \left( Y \right) = \left( { \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} } \right)
$$

contains just the angularmomenta.Moreover, $\mathcal Ḋ P Ḍ$ isskew-symmetric.By（5.18 thederivative of $Y$ is seen to be

$$
\dot { Y } = \dot { Q } ^ { T } P + Q ^ { T } \dot { P } = D ^ { - 1 } P ^ { T } P - Q ^ { T } \nabla U ( Q ) - A = D ^ { - 1 } Y ^ { T } Y - Q ^ { T } \nabla U ( Q )
$$

Taking the skew-symmetric part of this equation,the symmetric matrix $\varLambda$ drops out and we obtain

$$
\operatorname { s k e w } \left( { \dot { Y } } \right) = \operatorname { s k e w } \left( D ^ { - 1 } Y ^ { T } Y \right) = \operatorname { s k e w } \left( Q ^ { T } \nabla U ( Q ) \right) .
$$

These are,for $U = 0$ ,precisely the above Euler equations,obtained a second time.

# VII.5.3RigidBody Integrators

Foranumerical simulation of rigid bodymotions,one can either solve theconstrained Hamiltonian system(5.18）,or one can solve the differential equation (5.21） for theangular momentum $Y ( t )$ in tandem with the equation (5.12） for $Q ( t )$ We consider the following approaches:(I) an eficient application of the RATTLEalgorithm(1.26),and (II) various splitting methods.

# I)RATTLE

Weapply the symplectic RATTLE algorithm(1.26) to the system(5.18),and rewrite the formulas in terms of the variables $Y$ and $Q$ Thisapproach has been proposed anddeveloped independentlybyMcLachlan&Scovel(1995)andReich(1994).

Anapplication of theRATTLE algorithm(1.26)to the system(5.18)yields

$$
\begin{array} { r l r } { \quad } & { P _ { 1 / 2 } = \ b _ { 0 } - \cfrac { h } { 2 } \nabla U ( Q _ { 0 } ) - \cfrac { h } { 2 } Q _ { 0 } \varLambda _ { 0 } } & \\ { \quad } & { Q _ { 1 } = \ Q _ { 0 } + h P _ { 1 / 2 } D ^ { - 1 } , \quad \ Q _ { 1 } ^ { T } Q _ { 1 } = I } & { ( 5 . } \\ { \quad } & { P _ { 1 } = \ P _ { 1 / 2 } - \cfrac { h } { 2 } \nabla U ( Q _ { 1 } ) - \cfrac { h } { 2 } Q _ { 1 } \varLambda _ { 1 } , \quad } & { Q _ { 1 } ^ { T } P _ { 1 } D ^ { - 1 } + D ^ { - 1 } P _ { 1 } ^ { T } Q _ { 1 } = 0 , } \end{array}
$$

where both $\varLambda _ { 0 }$ and $\varLambda _ { 1 }$ are symmetric matrices.We let $Y _ { 0 } = Q _ { 0 } ^ { \prime } P _ { 0 }$ , $Y _ { 1 } = Q _ { 1 } ^ { \prime } P _ { 1 }$ , and ${ \cal Z } ~ = ~ Q _ { 0 } ^ { I } P _ { 1 / 2 } D ^ { - 1 }$ Wemultiplythe first relation of(5.22）by $Q _ { 0 } ^ { T }$ ,thelast relation by $Q _ { 1 } ^ { I }$ ,andwe eliminate the symmetric matrices $\varLambda _ { 0 }$ and $\varLambda _ { 1 }$ by taking the skew-symmetric parts of the resulting equations.The orthogonality of $Q _ { 0 } ^ { I } Q _ { 1 } =$ $I + h Z$ implies $h Z ^ { T } Z = - ( Z + Z ^ { T } )$ ,which can thenbeused to simplify the last relation.Altogether thisresults in the following algorithm.

Algorithm5.1. Let $Q _ { 0 }$ be orthogonal and $D Y _ { 0 }$ be skew-symmetric.One step $( Q _ { 0 } , Y _ { 0 } ) \mapsto ( Q _ { 1 } , Y _ { 1 } )$ ofthemethod then readsasfollows:

-find $Z$ suchthat $I + h Z$ is orthogonal and

$$
\mathrm { s k e w } \left( Z D \right) = \mathrm { ~ s k e w } \left( Y _ { 0 } \right) - \frac h 2 \mathrm { ~ s k e w } \left( Q _ { 0 } ^ { T } \nabla U ( Q _ { 0 } ) \right) ,
$$

-compute $Q _ { 1 } = Q _ { 0 } ( I + h Z )$

-compute $Y _ { 1 }$ suchthat $D Y _ { 1 }$ is skew-symmetric and

$$
\begin{array} { r } { \mathbf { k e w } \left( Y _ { 1 } \right) = \mathbf { s k e w } \left( Z D \right) - \mathbf { s k e w } \left( ( Z + Z ^ { T } ) D \right) - \frac { h } { 2 } \mathbf { s k e w } \left( Q _ { 1 } ^ { T } \nabla U ( Q _ { 1 } ) \right) . } \end{array}
$$

The second step is explicit,and the third steprepresentsa linear equation for the elementsof $Y _ { 1 }$

Computation of the First Step.We write for the knownpart of equation(5.23)

$$
\operatorname { s k e w } \left( Y _ { 0 } \right) - { \frac { h } { 2 } } \operatorname { s k e w } \left( Q _ { 0 } ^ { T } \nabla U ( Q _ { 0 } ) \right) = { \left( \begin{array} { l l l } { 0 } & { - \alpha _ { 3 } } & { \alpha _ { 2 } } \\ { \alpha _ { 3 } } & { 0 } & { - \alpha _ { 1 } } \\ { - \alpha _ { 2 } } & { \alpha _ { 1 } } & { 0 } \end{array} \right) } = A
$$

and have to solve

$$
\begin{array} { r } { \frac { 1 } { 2 } ( Z D - D Z ^ { T } ) = A , \quad ( I + h Z ^ { T } ) ( I + h Z ) = I , \quad \frac { 1 } { 2 } ( Z D + D Z ^ { T } ) = S } \end{array}
$$

(the trick was to add the last equation with $S$ anunknown symmetric matrix).Elimination gives $Z = ( A + S ) D ^ { - 1 }$ and $Z ^ { T } = D ^ { - 1 } ( S - A )$ Both inserted into the second equation lead to a Riccati equation for $S$ .There exist effcient algorithms forsuchproblems;see thereferencein Sect.IV.5.3andadetailed explanation in McLachlan& Zanna（2005).

Remark 5.2 (Moser-Veselov Algorithm).An independent accessto the above formulasisgiveninaremarkablepaperbyMoser&Veselov(1991),bytreating therigid bodythrougha discretizedvariational principle,similarto the ideasof Sect.VI.6.2.TheequivalenceisexplainedbyMcLachlan& Zanna（2oo5),followingasuggestion ofB.Leimkuhlerand S.Reich.

Quaternions(Euler Parameters).An efficient implementation of the above algorithmrequires suitablerepresentations of orthogonal matrices,and theuse of quaternionsisa standard approach.

Afterhaving revolutionized Lagrangian mechanics (see Chapt.VI),Hamilton struggled for years to generalize complex analysis to three dimensions.Hefinally achieved his dream,however not in three dimensions,but infour,and founded in 1843the theory of quaternions.

Foran introduction to quaternions(whose coefficients are sometimes called Eulerparameters)werefer to Sects.IV.2and IV.3 ofKlein(19o8),and fortheir usein numerical simulations to Sects.9.3and 11.3of Haug(1989).Quaternions can be written as $\begin{array} { r } { e = e _ { 0 } + i e _ { 1 } + j e _ { 2 } + k e _ { 3 } . } \end{array}$ wheremultiplication isdefined via the relations $i ^ { 2 } = j ^ { 2 } = k ^ { 2 } = - 1$ , $i j = k$ , $j k = i$ ， $k i = j$ and $j i = - k$ , $k j = - i$ , $i k = - j .$ The product of two quaternions $e \cdot f$ (written in matrix notation）is

$$
\begin{array} { r } { ( e _ { 0 } + i e _ { 1 } + j e _ { 2 } + k e _ { 3 } ) \quad = \quad \left( \begin{array} { l l l } { e _ { 0 } } & { < e _ { 1 } } & { - e _ { 2 } } & { - e _ { 3 } } \\ { e _ { 1 } ^ { > } } & { e _ { 0 } } & { < e _ { 3 } } & { e _ { 2 } } \\ { e _ { 2 } } & { e _ { 0 } } & { \ldots } & { e _ { 1 } } \\ { e _ { 3 } } & { e _ { 1 } ^ { > } } & { e _ { 2 } } \end{array} \right) \quad \left( \begin{array} { l } { f _ { 0 } } \\ { f _ { 1 } } \\ { f _ { 2 } } \\ { f _ { 3 } } \end{array} \right) } \end{array}
$$

Wesee(in grey）thatin dimensions $1 , 2 , 3$ appearsa skew-symmetric matrix $E$ whose structureis familiar to us.This part of thematrix changes sign if the two factorsare permuted.

Animportant discovery,for three dimensional applications of the quaternions, is the following:ifa quaternion $p$ isa3-vector (i.e.,has $p _ { 0 } = 0$ ),then $p ^ { \prime } = e \cdot p \cdot \overline { { e } }$ is a3-vector,too,and themap $p \mapsto p ^ { \prime }$ isdescribed by thematrix

$$
Q ( e ) = \| e \| ^ { 2 } I + 2 e _ { 0 } E + 2 E ^ { 2 } , \qquad E = \left( \begin{array} { c c c } { { 0 } } & { { - e _ { 3 } } } & { { e _ { 2 } } } \\ { { e _ { 3 } } } & { { 0 } } & { { - e _ { 1 } } } \\ { { - e _ { 2 } } } & { { e _ { 1 } } } & { { 0 } } \end{array} \right)
$$

where $\overline { { e } } = e _ { 0 } - i e _ { 1 } - j e _ { 2 } - k e _ { 3 }$ and $\| e \| ^ { 2 } = e \cdot \overline { { e } } = e _ { 0 } ^ { 2 } + e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } .$

Lemma5.3.1f $\| e \| = 1$ ，then thematrix $Q ( e )$ isorthogonal.Every orthogonal matrixwithdet $Q = 1$ canbewritten in this form.We have $Q ( e ) Q ( f ) = Q ( e f )$ so thatthemultiplication oforthogonalmatrices corresponds tothemultiplication of quaternions.

Geometrically,thematrix $Q$ effectsa rotation around theaxis $\varepsilon = ( e _ { 1 } , e _ { 2 } , e _ { 3 } ) ^ { T }$ with rotation angle $\varphi$ whichsatisfies $\tan ( \varphi / 2 ) = \lVert \varepsilon \rVert / e _ { 0 }$ .

Proof.Thecondition $Q ^ { \cal I } Q = I$ can be verified directly using $E ^ { I } = - E$ and $E ^ { 3 } = - ( e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } ) E .$ Thereciprocal statement isafamous theorem of Euler;it is based onthe fact that $\boldsymbol { \varepsilon }$ is an eigenvector of $Q$ ,which in dimension $3 \times 3$ always exists.The formula for $Q ( e ) Q ( f )$ follows from $e \cdot f \cdot p \cdot { \overline { { f } } } \cdot { \overline { { e } } } = ( e \cdot f ) \cdot p \cdot ( { \overline { { e \cdot f } } } )$

The geometric property follows from the virtues of the exterior product,because by （5.1） the matrix $Q$ mapsavector $x$ to

$$
x + 2 e _ { 0 } \varepsilon \times x + 2 \varepsilon \times ( \varepsilon \times x ) .
$$

This consists in arectangular mouvement in a plane orthogonal to $\succeq$ ；first vertical to $x$ by anamount $2 e _ { 0 } \left\| \boldsymbol { \varepsilon } \right\|$ (times the distance of $x$ ), then parallel to $x$ byan amount $2 \| \varepsilon \| ^ { 2 }$

![](images/971edbc10aafd00d3f0538e4cc11fcbbf4c17e17cec4572ab70e39ca9eafa59e.jpg)

Applying Pythagoras'Theoremas $( 2 e _ { 0 } \| \varepsilon \| ) ^ { 2 } + ( 2 \| \varepsilon \| ^ { 2 } - 1 ) ^ { 2 } = 1$ it turns out that the map is norm preserving if $e _ { 0 } ^ { 2 } + \| \varepsilon \| ^ { 2 } = 1 .$ Theangle $\varphi / 2$ ,whose tangens can be seen to be $\lVert \varepsilon \rVert / e _ { 0 }$ ,isanangle at the circumference of thecircle for the rotation angle $\varphi$ at the center. □

Foran efficient implementation of Algorithm 5.1werepresent the orthogonal matrices $Q _ { 0 }$ , $Q _ { 1 }$ ,and $I + h Z$ byquaternions.This reduces the dimension of the systems,and step2 becomesa simple multiplication of quaternions.For solving the nonlinear system of step 1,we let $I + h Z \ = \ Q ( e )$ With the values of $\alpha _ { i }$ from(5.24）and with skew $( h Z D ) = 2 e _ { 0 }$ skew $( E D ) + 2$ skew $( E ^ { 2 } D )$ ,theequation (5.23）becomes

$$
\binom { h \alpha _ { 1 } } { h \alpha _ { 2 } } \ = \ 2 e _ { 0 } \left( \begin{array} { l } { I _ { 1 } e _ { 1 } } \\ { I _ { 2 } e _ { 2 } } \\ { I _ { 3 } e _ { 3 } } \end{array} \right) \ + \ 2 \left( \begin{array} { l } { ( I _ { 3 } - I _ { 2 } ) e _ { 2 } e _ { 3 } } \\ { ( I _ { 1 } - I _ { 3 } ) e _ { 3 } e _ { 1 } } \\ { ( I _ { 2 } - I _ { 1 } ) e _ { 1 } e _ { 2 } } \end{array} \right) ,
$$

which,together with $e _ { 0 } ^ { 2 } + e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } = 1 ,$ represent four quadratic equations for fourunknowns.We solve them veryquickly byafew fixed-point iterations:update successively $e _ { i }$ fromtheith equationof(5.27）and then $e _ { 0 }$ from the normalizationcondition.AFortran subroutineRATORI for thisalgorithmisavailableon the homepage $<$ http://www.unige.ch/\~hairer>.

![](images/cd5423210dbd62fe69b18c59fd89effec7c867e520fdb76cde62999dc5f6ae87.jpg)  
Fig.5.3.Numerical solutions of the rigid body equations；without/with gravitation, with/without symmetry.Initial values $y _ { 1 0 } = 0 . 2 , y _ { 2 0 } = 1 . 0 , y _ { 3 0 } = 0 . 4 ;$ initial position of $Q _ { 0 }$ determined by the quatenion $e _ { 0 } = 0 . 4 , e _ { 1 } = 0 . 2 , e _ { 2 } = 0 . 4 , e _ { 3 } = 0 . 8$ ;moments ofinertia $I _ { 1 } ~ = ~ 0 . 5$ , $I _ { 2 } ~ = ~ 0 . 8 5$ (0.5in the symmetric case), $I _ { 3 } ~ = ~ 1 ;$ stepsize $h = 0 . 1$ , integration interval $0 \leq t \leq 3 0$

Conservation ofCasimir and Hamiltonian. Itis interesing to note that,in the absence ofapotential,the Algorithm5.1 preserves exactly theCasimir $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ and,more surprisingly,also the Hamiltonian $\begin{array} { r } { \frac { 1 } { 2 } ( y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 } ) } \end{array}$ Thiscan beseen as follows:without any potential we have skew $( Y _ { 0 } ) =$ skew（ $Z D )$ and skew $( Y _ { 1 } ) = - \operatorname { s k e w } \left( Z ^ { l ^ { \prime } } D \right)$ ,so that thevectors $( y _ { 1 0 } , y _ { 2 0 } , y _ { 3 0 } ) ^ { T }$ and $( y _ { 1 1 } , y _ { 2 1 } , y _ { 3 1 } ) ^ { T }$ are equal to $u + v$ and $u - v$ ,respectively,where $u$ and $\boldsymbol { v }$ are the vectors of the righthand side of(5.27).Since $u$ and $\boldsymbol { v }$ are orthogonal,we have $\| u + v \| = \| u - v \|$ , which proves the conservation of the Casimir.

To prove the conservation of the Hamiltonian,we first multiply therelation （5.27）with $G = \mathrm { d i a g } ( 1 / \sqrt { I _ { 1 } } , 1 / \sqrt { I _ { 2 } } , 1 / \sqrt { I _ { 3 } } )$ ,and then apply the same arguments. Thevectors $G u$ and $G v$ are still orthogonal.

Example5.4(Force-FreeandHeavy Top).WepresentinFig.5.3thenumerical solutions $y _ { i }$ obtained by the above algorithm.In the case of the heavy top,weassume the centre of gravity to be $( 0 , 0 , 1 )$ inthebody frame,and assumethat the third coordinate of the stationary frame isvertical.The potential energy due to gravity is then given by $U ( Q ) = q _ { 3 3 }$ and,expressedbyquaternions (5.26),itis $U = e _ { 0 } ^ { 2 } \mathrm { ~ - ~ }$ $e _ { 1 } ^ { 2 } - e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 }$

# (II) Spliting Methods

Asbefore we consider the differential equation(5.21） for theangular momenta in thebody $y _ { 1 } , y _ { 2 } , y _ { 3 }$ together with the differential equation(5.12） for the rotation matrix $Q$ .Anobvious splitting in the presence of a potential is

$$
\varphi _ { h / 2 } ^ { U } \circ \varPhi _ { h } ^ { T } \circ \varphi _ { h / 2 } ^ { U } ,
$$

where $\varphi _ { t } ^ { U }$ represents the exactffow of

$$
\dot { Q } = 0 , \qquad \mathrm { s k e w } ( \dot { Y } ) = - \mathrm { s k e w } ( Q ^ { T } \nabla U ( Q ) ) ,
$$

and $\varPhi _ { h } ^ { T }$ is asuitable numerical approximation of the system corresponding to kinetic energyonly,i.e.,without any potential $U ( Q )$ The use of splitting techniques forrigidbodydynamicswasproposedbyTouma&Wisdom（1994),McLachlan（1993),Reich（1994）,andDullweber,Leimkuhler&McLachlan（1997).Fasso (2003)presentsa careful study and comparison of variousways of splitting the kinetic energy.

Computation of $\varPhi _ { h } ^ { i } .$ Wedo this bysplitting once again,by letting several moments ofinertia tending to infinity (and the corresponding $\omega _ { i }$ tending to zero).In order to avoid formal difficultieswith infinite denominators,we write the system (5.10) togetherwith(5.12)in the form

$$
\begin{array} { r l } { \left( \begin{array} { c } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) } & { = \begin{array} { c c c } { \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} \right) } \end{array} \left( \begin{array} { c } { T _ { y _ { 1 } } ( y ) } \\ { T _ { y _ { 2 } } ( y ) } \\ { T _ { y _ { 3 } } ( y ) } \end{array} \right) } \\ { \dot { Q } } & { = Q \left( \begin{array} { c c c } { 0 } & { - T _ { y _ { 3 } } ( y ) } & { T _ { y _ { 2 } } ( y ) } \\ { T _ { y _ { 3 } } ( y ) } & { 0 } & { - T _ { y _ { 1 } } ( y ) } \\ { - T _ { y _ { 2 } } ( y ) } & { T _ { y _ { 1 } } ( y ) } & { 0 } \end{array} \right) , } \end{array}
$$

where $T ( y ) = { \textstyle \frac { 1 } { 2 } } ( y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 } )$ is the kinetic energy,and $T _ { y _ { i } } ( y )$ denote partialderivatives.

Three Rotations Splitting.An obvious splitting of the kinetic energy is

$$
T ( y ) = R _ { 1 } ( y ) + R _ { 2 } ( y ) + R _ { 3 } ( y ) , \qquad R _ { i } ( y ) = y _ { i } ^ { 2 } / ( 2 I _ { i } ) ,
$$

which results in the numerical method

$$
\begin{array} { r } { \varPhi _ { h } ^ { T } = \varphi _ { h / 2 } ^ { R _ { 3 } } \circ \varphi _ { h / 2 } ^ { R _ { 2 } } \circ \varphi _ { h } ^ { R _ { 1 } } \circ \varphi _ { h / 2 } ^ { R _ { 2 } } \circ \varphi _ { h / 2 } ^ { R _ { 3 } } , } \end{array}
$$

where $\varphi _ { t } ^ { R _ { i } }$ istheeactofi $T ( y )$ replaced by $R _ { i } ( y )$ Theflow $\varphi _ { t } ^ { R _ { 1 } }$ is easily obtained: $y _ { 1 }$ remains constant and the second and third equation in (5.29)boil down to the harmonic oscillator.We obtain

$$
y ( t ) = S ( \alpha t ) y ( 0 ) , \qquad Q ( t ) = Q ( 0 ) S ( \alpha t ) ^ { T }
$$

with $\alpha = y _ { 1 } ( 0 ) / I _ { 1 }$ and the rotation matrix

$$
\begin{array} { r } { S ( \theta ) = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right) . } \end{array}
$$

Similarsimple formulas are obtained for the exact flows corresponding to $R _ { 2 }$ and $R _ { 3 }$

Symmetric $^ +$ Rotation Spliting.Itis often advantageous,inparticular foranearly symmetric body（ $I _ { 1 } \approx I _ { 2 }$ ,toconsiderthespliting

$$
T ( y ) = R ( y ) + S ( y ) , \quad R ( y ) = \Big ( \frac { 1 } { I _ { 1 } } - \frac { 1 } { I _ { 2 } } \Big ) \frac { y _ { 1 } ^ { 2 } } { 2 } , \quad S ( y ) = \frac { 1 } { 2 } \Big ( \frac { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { y _ { 3 } ^ { 2 } } { I _ { 3 } } \Big ) \frac { y _ { 3 } ^ { 2 } } { 2 } .
$$

and the corresponding numerical integrator

$$
\varPhi _ { h } ^ { T } = \varphi _ { h / 2 } ^ { R } \circ \varphi _ { h } ^ { S } \circ \varphi _ { h / 2 } ^ { R } .
$$

The exact flow $\varphi _ { t } ^ { R }$ is the same as(5.32) with $I _ { 1 } ^ { - 1 }$ replaced by $I _ { 1 } ^ { - 1 } - I _ { 2 } ^ { - 1 } .$ Theflow ofthesymmetricforce-free top $\varphi _ { t } ^ { S }$ possessessimpleaalyticmulastoehe first picture of Fig.5.3):we observea precession of $y$ with constant speed around a coneandarotation of thebodyaround $\omega$ with constant speed.Therefore

$$
y ( t ) = B ( \beta t ) y ( 0 ) , \qquad Q ( t ) = Q ( 0 ) A ( t ) B ( \beta t ) ^ { T } ,
$$

where $\beta = ( I _ { 3 } ^ { - 1 } - I _ { 2 } ^ { - 1 } ) y _ { 3 } ( 0 )$ ,and

$$
\mathrm { l } ( t ) = \exp { \left( \frac { t } { I _ { 2 } } { \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } ( 0 ) } & { y _ { 2 } ( 0 ) } \\ { y _ { 3 } ( 0 ) } & { 0 } & { - y _ { 1 } ( 0 ) } \\ { - y _ { 2 } ( 0 ) } & { y _ { 1 } ( 0 ) } & { 0 } \end{array} \right) } \right) } , \quad B ( \theta ) = \left( - \sin \theta \quad \cos \theta \quad 0 \right)
$$

This canalso be checked directly by differentiation.

Similar to the previous algorithmitis advantageous to usearepresentation of theappearing orthogonal matrices by quaternions.The correspondence between the orthogonal rotation matrices appearing in(5.32)and(5.33)and their quaternions is, inaccordancewithLemma5.3,the following:

$$
\begin{array} { r l } { S ( \theta ) ^ { T } } & { { }  \quad \cos ( \theta / 2 ) + i \sin ( \theta / 2 ) } \\ { B ( \theta ) ^ { T } } & { { } \Longleftrightarrow \quad \cos ( \theta / 2 ) + k \sin ( \theta / 2 ) } \\ { A ( t ) } & { { } \Longleftrightarrow \quad \cos ( \vartheta / 2 ) + a ^ { - 1 } \sin ( \vartheta / 2 ) \big ( i y _ { 1 } ( 0 ) + j y _ { 2 } ( 0 ) + k y _ { 3 } ( 0 ) \big ) , } \end{array}
$$

where $a = \sqrt { y _ { 1 } ( 0 ) ^ { 2 } + y _ { 2 } ( 0 ) ^ { 2 } + y _ { 3 } ( 0 ) ^ { 2 } }$ and $\vartheta = a t / I _ { 2 }$ Thematrix multiplicationsin thealgorithm can therefore bedone very efficiently.A Fortran subroutine QUATER forthe“symmetric $^ +$ rotationsplitting”algorithmisavailable on the homepage $<$ http://www.unige.ch/\~hairer>.

# VII.5.4Lie-Poisson Systems

In Sect.VII.5.1 we have seen that the reduction of the equations of motion of the rigidbody leads to the Poissonsystem(5.1O）witha structurematrix whose entries arelinear functions.Here we consider more general Poisson systems

$$
\dot { y } = B ( y ) \nabla H ( y ) ,
$$

where the structure matrix $B ( y )$ depends linearly on $y$ ,i.e.,

$$
b _ { i j } ( y ) = \sum _ { k = 1 } ^ { n } C _ { j i } ^ { k } y _ { k } \qquad { \mathrm { f o r ~ } } i , { \hat { y } } = 1 , { \mathrm { e } } { \mathrm { : } } s { \mathrm { : } } s = 1 ,
$$

Suchsystems,calledLie-Poisson systems,areclosely related to differential equations on thedual ofLiealgebras;seeMarsden&Ratiu(1999),Chaps.13and14, foran in-depth discussion of this theory.

RecallthataLiealgebra isavector spacewithabracketwhich isanti-symmetric and satisfies the Jacobiidentity (Sect.IV.6).Let $E _ { 1 } , \ldots , E _ { n }$ bea basis ofa vector space,and definea bracket by

$$
[ E _ { i } , E _ { j } ] = \sum _ { k = 1 } ^ { n } C _ { i j } ^ { k } E _ { k }
$$

with $C _ { i j } ^ { k }$ from(5.35).Ifre $B ( y )$ of (5.35) isskew-symmetricand satisfies(2.1O),then this bracket makes the vector spaceaLie algebra (the verificationisleftasexercise)Theient $C _ { i j } ^ { k }$ arecalledstructureonstantsofthe Liealgebra.Conversely,if westart fromaLiealgebrawith bracket given by(5.36), then the matrix $B ( y )$ defined by(5.35）is the structurematrix of aPoisson bracket.

LetgbeaLiealgebra witha basis $E _ { 1 } , \ldots , E _ { n }$ andlet ${ \mathfrak { g } } ^ { * }$ be the dual of the Lie algebra,i.e.,thevectorspace ofallinear forms $Y : { \mathfrak { g } }  \mathbb { R }$ Thedualityiswritten as $\langle Y , X \rangle$ for $Y \in { \mathfrak { g } } ^ { * }$ and $X \in { \mathfrak { g } }$ Wedenote by $F _ { 1 } , \ldots , F _ { n }$ the dual basis defined by $\langle F _ { i } , E _ { j } \rangle = \delta _ { i j }$ ,theKronecker $\delta$ ，

Theorem5.5.Let $y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T } \in \mathbb { R } ^ { n }$ $\mathfrak { g }$ bea Lie algebra with basis wessoeiate $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { n } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } } \end{array}$ $E _ { 1 } , \ldots , E _ { n }$ satisfying（5.36）.To andweconsidera Hamiltonian6 $H ( y ) = H ( Y )$

Then,thePoissonsystem $\dot { y } = B ( y ) \nabla H ( y )$ with $B ( y )$ givenby(5.35)isequivalentto thefollowingdifferentialequation on thedual ${ \mathfrak { g } } ^ { * }$ :

$$
\langle \dot { Y } , X \rangle = \langle Y , [ H ^ { \prime } ( Y ) , X ] \rangle \qquad f o r a l l \ X \in { \mathfrak { g } } ,
$$

whereH'(Y)=∑-1 H（E

Proof.Differentiating $H ( y ) = H ( Y )$ with respect to $y _ { i }$ gives

$$
\frac { \partial H ( y ) } { \partial y _ { i } } = \langle F _ { i } , H ^ { \prime } ( Y ) \rangle \qquad \mathrm { a n d } \qquad H ^ { \prime } ( Y ) = \sum _ { j = 1 } ^ { n } \frac { \partial H ( y ) } { \partial y _ { j } } E _ { j } .
$$

Herewe have used the identification $( { \mathfrak { g } } ^ { * } ) ^ { * } = { \mathfrak { g } }$ ,because $H ^ { \prime } ( Y )$ isactuallyan elementof $( { \mathfrak { g } } ^ { * } ) ^ { * } .$ With this formula for $H ^ { \prime } ( Y )$ we are able tocompute

$$
\left. Y , [ H ^ { \prime } ( Y ) , E _ { i } ] \right. = \left. Y , \sum _ { j = 1 } ^ { n } { \frac { \partial H ( y ) } { \partial y _ { j } } } \left[ E _ { j } , E _ { i } \right] \right. = \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } { \frac { \partial H ( y ) } { \partial y _ { j } } } C _ { j i } ^ { k } \left. Y , E _ { k } \right.
$$

wherewe have used (5.36).Since $\langle \dot { Y } , E _ { i } \rangle = \dot { y } _ { i }$ and $\langle Y , E _ { k } \rangle = y _ { k }$ ,this shows that thedifferential equation （5.37）is equivalent to

$$
\dot { y } _ { \bar { \imath } } = \sum _ { j = 1 } ^ { n } \biggl ( \sum _ { k = 1 } ^ { n } C _ { j i } ^ { k } y _ { k } \biggr ) \frac { \partial H ( y ) } { \partial y _ { j } } ,
$$

which is nothing more than $\dot { y } = B ( y ) \nabla H ( y )$ with $B ( y )$ from (5.35）.

Weremark that (5.37) can bereformulated as

$$
{ \dot { Y } } = \operatorname { a d } _ { H ^ { \prime } ( Y ) } ^ { * } Y ,
$$

where $\operatorname { a d } _ { A } ^ { * }$ is theadjoint of the operator ad $_ A ( X ) = \lfloor A , X \rfloor$

Equation (5.37） is similar inappearance to the Lie bracket equation $\dot { L } \ =$ $[ A ( L ) , L ] = \operatorname { a d } _ { A ( L ) } L$ of Sect.IV.3.2.When $\mathfrak { g }$ is theLiealgebra of amatrix Lie group $G$ ,then solutions of that equationare of the form $L ( t ) = \operatorname { A d } _ { U ( t ) } L _ { 0 }$ where

$$
\mathbf { A d } _ { U } \mathbf { \boldsymbol { X } } = U \mathbf { \boldsymbol { X } } U ^ { - 1 } ;
$$

see the proof of LemmaIV.3.4.Similarly,for the solutionof(5.37)wehave the following.

Theorem 5.6.Consideramatrix Liegroup $G$ withLiealgebrag.Then,the solution $Y ( t ) \in { \mathfrak { g } } ^ { * }$ of(5.37)with initial value $Y _ { 0 } \in \mathfrak { g } ^ { * }$ isgiven by

$$
\langle Y ( t ) , X \rangle = \langle Y _ { 0 } , U ( t ) ^ { - 1 } X U ( t ) \rangle \qquad f o r a l l ~ X \in \mathfrak { g } ,
$$

where $U ( t ) \in G$ satisfies

$$
\dot { U } = - H ^ { \prime } ( Y ( t ) ) U , \quad U ( 0 ) = I .
$$

Equation (5.39) can be written as

$$
\begin{array} { r } { Y ( t ) = \operatorname { A d } _ { U ( t ) ^ { - 1 } } ^ { * } Y _ { 0 } , } \end{array}
$$

where $\mathrm { A d } _ { U - 1 } ^ { * }$ is the adjoint of $\mathrm { A d } _ { U - 1 }$ The solution $Y ( t )$ of（5.37)thus lies on the coadjoint orbit

$$
Y ( t ) \in \{ \mathbf { A d } _ { U - 1 } ^ { * } Y _ { 0 } ; U \in G \} .
$$

In coordinates $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { n } y _ { j } F _ { j } } \end{array}$ , we note $y _ { j } = \langle Y _ { 0 } , U ( t ) ^ { - 1 } E _ { j } U ( t ) \rangle .$

Proof.Differentiating the ansatz (5.39) for the solution we obtain

$$
\begin{array} { l l l } { \langle \dot { Y } , X \rangle } & { = } & { \langle Y _ { 0 } , - U ^ { - 1 } \dot { U } U ^ { - 1 } X U + U ^ { - 1 } X \dot { U } \rangle } \\ & { = } & { \langle Y _ { 0 } , U ^ { - 1 } [ X , \dot { U } U ^ { - 1 } ] U \rangle = \langle Y , [ X , \dot { U } U ^ { - 1 } ] \rangle , } \end{array}
$$

where we have used (5.39) in the first and the last equation.This shows that (5.37) is satisfied with the choice $U U ^ { - 1 } = - H ^ { \prime } ( Y )$

Example 5.7 (Rigid Body).The Lie group corresponding to the rigid bodyis SO(3)with the Lie algebra ${ \mathfrak { s o } } ( 3 )$ of skew-symmetric $3 \times 3$ matrices,with the basis

$$
E _ { 1 } = \left( { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right) , \quad E _ { 2 } = \left( { \begin{array} { c c c } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \end{array} } \right) , \quad E _ { 3 } = \left( { \begin{array} { c c c } { 0 } & { - 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) .
$$

If we let $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { T }$ be the coordinates of $X \in { \mathfrak { s o } } ( 3 )$ ,thenwe have $X v =$ $x \times v$ forall $\boldsymbol { v } \in \mathbb { R } ^ { 3 }$ Sincefor $U \in \mathrm { S O } ( 3 )$ ,

$$
U ^ { - 1 } X U v = U ^ { - 1 } ( x \times U v ) = U ^ { - 1 } x \times v ,
$$

the vector $U ^ { - 1 } x$ consists of the coordinates of $U ^ { - 1 } X U \in { \mathfrak { s o } } ( 3 )$

Let $y = ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) ^ { T }$ be the coordinates of $Y \in { \mathfrak { s o } } ( 3 ) ^ { * }$ with respect to the dual basis of $E _ { 1 } , E _ { 2 } , E _ { 3 }$ .Since

$$
\langle Y , U ^ { - 1 } X U \rangle = \Big \langle \sum _ { j = 1 } ^ { 3 } y _ { j } F _ { j } , \sum _ { i = 1 } ^ { 3 } ( U ^ { - 1 } x ) _ { i } E _ { i } \Big \rangle = y ^ { T } U ^ { - 1 } x = ( U y ) ^ { T } x ,
$$

the coordinates of $\operatorname { A d } _ { U ^ { - 1 } } Y$ are given by the vector $\ U y .$ Therefore,the coordinates of the coadjoint orbit of $Y$ lieona sphere of radius $\lVert y \rVert$ .The conservation of the coadjoint orbit thus reduces here to the preservation of the Casimir $C ( y ) = y _ { 1 } ^ { 2 } +$ $y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$

Lie-Poisson integrators seem to be have first beenconsidered by Ge&Marsden (1988),who extend the construction of symplectic methods by generating functions toLie-Poisson systems.Channel & Scovel（1991） propose an implementation of these methods based on a coordinatization of the group by the exponential map.

McLachlan （1993）proposes integrators based on spliting the Hamiltonian and illustrates this approach for various examples ofLie-Poisson systems.Whenapplicable,such splittingintegrators yield Poisson integrators that preserve the coadjoint orbits,since they are composed of exact flows ofLie-Poisson systems.

Engg& Faltinsen (2oo1） propose to solve numerically the Lie-Poisson system (5.34)by applying Lie groupintegrators suchas those of Sect.IV.8 to thedifferential equation (5.4O) with(5.39).Thisapproach keeps the solution on the coadjoint orbit byconstruction,but itdoes not,ingeneral,giveaPoisson integrator.

# VII.5.5 Lie-Poisson Reduction

Thereduction of the Hamiltonian equations of motion of the free rigid body to theEuler equations isan instance of a general reduction process from Hamiltonian systems with symmetry on aLie group toLie-Poisson systems,which we now describe;cf.Marsden&Ratiu(1999),Chap.13,forapresentation inamoreabstract framework and for an historical account.

Let us assume that the Lie group $G$ isasubgroup of ${ \mathrm { G L } } ( n )$ givenby

$$
G = \{ Q ; g _ { i } ( Q ) = 0 , i = 1 , \ldots , m \} ,
$$

and consider a Hamiltonian system on $G$ ,

$$
\begin{array} { l l } { \displaystyle \dot { P } ~ = ~ - \nabla _ { Q } H ( P , Q ) - \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla _ { Q } g _ { i } ( Q ) , \qquad \displaystyle \dot { Q } = \nabla _ { P } H ( P , Q ) } \\ { \displaystyle 0 ~ = ~ g _ { i } ( Q ) , \quad i = 1 , . . . , m , } \end{array}
$$

where $P , Q$ are square matrices,and $\nabla _ { Q } H = \left( \partial H / \partial Q _ { i j } \right) .$ This is of the form discussed in Sect.VII.1.2.In regionswhere thematrix

$$
\left( \frac { \partial ^ { 2 } H ( P , Q ) } { \partial P ^ { 2 } } \left( \nabla _ { Q } g _ { i } ( Q ) , \nabla _ { Q } g _ { j } ( Q ) \right) \right) _ { i , j = 1 } ^ { m } \qquad \mathrm { i s ~ i n v e r t i b l e } ,
$$

theLagrange parameters $\lambda _ { i }$ can be expressed in terms of $P$ and $Q$ (cf.formula (1.13)).Hence,aunique solution exists locally provided the initial values $( P _ { 0 } , Q _ { 0 } )$ are consistent,i.e., $g _ { i } ( Q _ { 0 } ) = 0$ and

$$
\begin{array} { r } { g _ { i } ^ { \prime } ( Q _ { 0 } ) \Big ( \nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \Big ) = \operatorname { t r a c e } \Big ( \nabla _ { Q } g _ { i } ( Q _ { 0 } ) ^ { T } \nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \Big ) = 0 , } \end{array}
$$

or equivalently, $Q _ { 0 } \in G$ and $\nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \in T _ { Q _ { 0 } } G$

Wenow assume that the Hamiltonian $H$ is quadratic in $P$ Aswe have seen in Sect.VII.1.2,the equations(5.43）can be viewed asa differential equationon the cotangent bundle $T ^ { \ast } G = \{ ( P , Q ) ; Q \in G , P \in T _ { Q } ^ { \ast } G \}$ where the cotangent space $T _ { Q } ^ { * G }$ isidentified with asubspace of matrices such that

$$
{ \cal P } \in T _ { Q } ^ { * } G \qquad \mathrm { i f ~ a n d ~ o n l y ~ i f } \qquad \nabla _ { P } H ( P , Q ) \in T _ { Q } G .
$$

Withthis identification,theduality beween $T _ { Q } ^ { * G }$ and $T _ { Q } G$ is given by thematrix inner product

$$
\langle P , V \rangle = \operatorname { t r a c e } \left( P ^ { T } V \right) \quad { \mathrm { ~ f o r ~ } } P \in T _ { Q } ^ { * } G , V \in T _ { Q } G .
$$

Wecall the Hamiltonianleft-invariant,if

$$
H ( U ^ { T } P , U ^ { - 1 } Q ) = H ( P , Q ) \qquad { \mathrm { ~ f o r ~ a l l ~ } } U \in G .
$$

In this case we have $H ( P , Q ) = H ( Q ^ { I } P , I ) $ and by differentiatingwe obtain $\nabla _ { P } H ( P , Q ) = Q \nabla _ { P } H ( Q ^ { I } P , I )$ By(5.45）and since $T _ { Q } G = \{ Q X ; X \in \mathfrak { g } \}$ with the Liealgebra $ { \mathfrak { g } } = T _ { I } G$ (cf.Sect.IV.6),this relation implies

$$
{ \cal P } \in T _ { Q } ^ { * } { \cal G } \qquad \mathrm { i f ~ a n d ~ o n l y ~ i f } \qquad { \cal Q } ^ { T } { \cal P } \in T _ { I } ^ { * } { \cal G } = \mathfrak { g } ^ { * } .
$$

Now $H ( P , Q )$ depends,for $( P , Q ) \in T ^ { * } G$ ,only on the product $Y = Q ^ { T } P \in { \mathfrak { g } } ^ { * }$ ， and wewrite7 $H ( P , Q ) = H ( Y )$ witha function $\boldsymbol { H } : \mathfrak { g } ^ { * }  \mathbb { R }$

Left-invariant Hamiltonian systems can be reduced toa Lie-Poisson system of half the dimension byaprocessthat generalizes the derivation of the Euler equations for the rigid body.

Theorem5.8.Considera Hamiltoniansystem(5.43）ona matrix Liegroup $G$ witha left-invariantquadratic Hamiltonian $H ( P , Q ) = H ( Y )$ for $Y = Q ^ { T } P .$ 1f $( P ( t ) , Q ( t ) ) \in T ^ { * } G$ isasolutionofthesystem(5.43),then $Y ( t ) = Q ( t ) ^ { T } P ( t ) \in \mathfrak { g } ^ { * }$ solvesthedifferentialequation(5.37).

Proof.Itisconvenient for the proof (though not necessary,see the lines following（2.17)）to extend the Hamiltonian $H : { \mathfrak { g } } ^ { * } \ \to \ \mathbb { R }$ toa function of arbitrarymatrices $Y$ bysetting $H ( Y ) ~ = ~ H ( I I Y )$ ,where $\boldsymbol { { \mathit { 1 } } } \boldsymbol { { \mathit { 1 } } }$ is the projection onto ${ \mathfrak { g } } ^ { * }$ given by $\langle I I Y , X \rangle = ( Y , X )$ forall $X ~ \in ~ { \mathfrak { g } }$ ,with the matrix inner product $( Y , X ) = \operatorname { t r a c e } \left( Y ^ { T } X \right)$ .

where Wefirst compute thederivatives of $Q ^ { T } P = Y$ nd $H ( P , Q ) = H ( Y ) = H ( I I Y ) = H ( y )$ $\begin{array} { r } { \pi Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } . } \end{array}$ Since $y _ { j } = \langle \varPi Q ^ { T } P , E _ { j } \rangle = ( Q ^ { T } P , E _ { j } )$ ,it follows from $\nabla _ { A }$ trace $( A ^ { T } B ) = B$ that

$$
7 p H ( P , Q ) = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } \nabla _ { P } y _ { j } = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } \nabla _ { P } \operatorname { t r a c e } \left( P ^ { T } Q E _ { j } \right) = Q H ^ { \prime } ( Y )
$$

where $\begin{array} { r } { H ^ { \prime } ( Y ) = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } E _ { j } \in \mathfrak { g } } \end{array}$ HEj∈gasinTheorem5.5.Using theidentityyj= trace $( P ^ { T } Q E _ { j } ) = \operatorname { t r a c e } { ( Q ^ { T } P E _ { j } ^ { T } ) }$ we get ina similar way

$$
\nabla _ { Q } H ( P , Q ) = P H ^ { \prime } ( Y ) ^ { T } .
$$

Consequently,the differential equations(5.43) become

$$
\dot { P } = - P H ^ { \prime } ( Q ^ { T } P ) ^ { T } - \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla _ { Q } g _ { i } ( Q ) , \qquad \dot { Q } = Q H ^ { \prime } ( Q ^ { T } P ) .
$$

The product rule $\dot { \boldsymbol { Y } } = \dot { \boldsymbol { Q } } ^ { T } \boldsymbol { P } + \boldsymbol { Q } ^ { T } \dot { \boldsymbol { P } }$ for $Y = Q ^ { T } P$ thus yields

$$
\dot { Y } = \bar { H ^ { \prime } } ( Y ) ^ { T } Y - Y \bar { H ^ { \prime } } ( Y ) ^ { T } - \sum _ { i = 1 } ^ { m } \lambda _ { i } Q ^ { T } \nabla _ { Q } g _ { i } ( Q ) .
$$

For $X \in { \mathfrak { g } }$ ,wenow exploit the properties

$$
\begin{array} { r l } & { \left. Q ^ { T } \nabla _ { Q } g _ { i } ( Q ) , X \right. = \left. \nabla _ { Q } g _ { i } ( Q ) , Q X \right. = 0 \qquad \mathrm { ( b e c a u s e ~ } Q X \in T _ { Q } G ) } \\ & { \left. [ H ^ { \prime } ( Y ) ^ { T } , Y ] , X \right. = \operatorname { t r a c e } \big ( \big ( Y ^ { T } H ^ { \prime } ( Y ) - H ^ { \prime } ( Y ) Y ^ { T } \big ) X \big ) } \\ & { \qquad = \operatorname { t r a c e } \big ( Y ^ { T } \big ( H ^ { \prime } ( Y ) X - X H ^ { \prime } ( Y ) \big ) \big ) = \left. Y , [ H ^ { \prime } ( Y ) , X ] \right. } \end{array}
$$

Since $Y ( t ) \in { \mathfrak { g } } ^ { * }$ for all $t$ ,this gives the equation (5.37).

Reduced Systemand Reconstruction.Combining Theorems5.8and5.5,we have reduced the Hamiltonian system(5.43)to the Lie-Poissonsystem for $\ b { y } ( t ) \in \mathbb { R } ^ { d }$ ,

$$
\begin{array} { r } { \dot { y } = B ( y ) \nabla H ( y ) , } \end{array}
$$

of half the dimension.To recover the full solution $( P ( t ) , Q ( t ) ) \in T ^ { * } G$ ,wemust solve this system alongwith

$$
\begin{array} { r } { { \dot { Q } } = Q H ^ { \prime } ( Y ) , \quad P = Q ^ { - T } Y } \end{array}
$$

where $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } . } \end{array}$

Poisson Structures.The Poisson bracket on $\mathbb { R } ^ { d }$ defined by $B ( y )$ is still closely relatedtothecanonical Poissonbracketon $\mathbb { R } ^ { 2 n ^ { 2 } } .$ Considerleft-invariantreal-valued functions $K , L$ on ${ \boldsymbol { \mathbf { \mathit { T } } } } ^ { * } { \boldsymbol { \mathbf { \mathit { G } } } }$ Thesecan be viewed as functions on $T ^ { * } G / G = { \mathfrak { g } } ^ { * } \subset$ Rnxn,

$$
K ( P , Q ) = K ( Y ) \mathrm { f o r } Y = Q ^ { T } P .
$$

(Aswe did previously in this section,we use the same symbol for these functions.） Via the projection $\pi : \mathbb { R } ^ { n \times n }  \mathfrak { g } ^ { * }$ used in the above proof,we can extend $K ( Y ) = K ( \varPi Y )$ toarbitrary $n \times n$ matrices $Y$ ,and via theaboverelationtoa left-invariant function $K ( P , Q )$ on $\mathbb { R } ^ { n \times n } \times \mathbb { R } ^ { n \times n }$ ,on which we have the canonical Poisson bracket

$$
\{ K , L \} _ { \mathrm { c a n } } = \sum _ { k , l = 1 } ^ { n } \Big ( \frac { \partial K } { \partial Q _ { k l } } \frac { \partial L } { \partial P _ { k l } } - \frac { \partial K } { \partial P _ { k l } } \frac { \partial L } { \partial Q _ { k l } } \Big ) .
$$

On the other hand,we can view $K$ asa function on $\mathbb { R } ^ { d }$ by choosing coordinates on ${ \mathfrak { g } } ^ { * }$ ,

$$
K ( y ) = K ( Y ) \quad { \mathrm { ~ f o r ~ } } Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in { \mathfrak { g } } ^ { * } .
$$

On $\mathbb { R } ^ { d }$ wehavethePoissonbracketdefined bythestructure matrix $B ( y )$ ,

$$
\{ K , L \} = \sum _ { i , j = 1 } ^ { d } \frac { \partial K } { \partial y _ { i } } b _ { i j } \frac { \partial L } { \partial y _ { j } } .
$$

Lemma5.9.Forleft-invariant functions $\begin{array} { r } { Q ^ { T } P = Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } } \end{array}$ $K , L$ asdescribed above,we have for

$$
\{ K , L \} ( y ) = \langle Y , [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \rangle = \{ K , L \} _ { \mathrm { c a n } } ( P , Q )
$$

where K()=∑(）Eg

Proof.Thefirstequality follows from theidentity

$$
b _ { i j } ( y ) = \left. Y , [ E _ { j } , E _ { i } ] \right. ,
$$

which isa direct consequence of the definition (5.35)with (5.36).For the second equality,therelations (5.48)and(5.49) for $K$ and $L$ yield

$$
\begin{array} { r c l } { \{ K , L \} _ { \mathrm { c a n } } ( P , Q ) } & { = } & { \mathrm { t r a c e } \left( K ^ { \prime } ( Y ) Y ^ { T } L ^ { \prime } ( Y ) - K ^ { \prime } ( Y ) ^ { T } Y L ^ { \prime } ( Y ) ^ { T } \right) } \\ & { = } & { \mathrm { t r a c e } \left( K ^ { \prime } ( Y ) Y ^ { T } L ^ { \prime } ( Y ) - L ^ { \prime } ( Y ) Y ^ { T } K ^ { \prime } ( Y ) \right) } \\ & { = } & { \mathrm { t r a c e } \left( Y ^ { T } [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \right) = \left. Y , [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \right. , } \end{array}
$$

which is the result.

Discrete Lie-Poisson Reduction.Considera symplectic integrator

$$
( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } ) \qquad \mathrm { o n } \ T ^ { * } G
$$

forthe left-invariant Hamiltonian system (5.43),and suppose that the method preserves the left-invariance:if $\phi _ { h } ( P _ { 0 } , Q _ { 0 } ) = ( P _ { 1 } , Q _ { 1 } )$ ,then

$$
\begin{array} { r } { \varPhi _ { h } ( U ^ { T } P _ { 0 } , U ^ { - 1 } Q _ { 0 } ) = ( U ^ { T } P _ { 1 } , U ^ { - 1 } Q _ { 1 } ) \mathrm { ~ f o r ~ a l l ~ } U \in G . } \end{array}
$$

Forexample,this is satisfied by theRATTLEalgorithm.Themethod then induces a one-stepmap

$$
Y _ { 1 } = \varPsi _ { h } ( Y _ { 0 } ) \qquad { \mathrm { o n ~ } } \mathfrak { g } ^ { * }
$$

bysetting $Y _ { 1 } = Q _ { 1 } ^ { \prime } P _ { 1 }$ for $( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } )$ with $Q _ { 0 } ^ { I } P _ { 0 } = Y _ { 0 }$ Thisisa numerical integrator for(5.37),and inthe coordinates $y = ( y _ { j } )$ with respect to the basis $( F _ { j } )$ of ${ \mathfrak { g } } ^ { * }$ this gives amap

$$
y _ { 1 } = \psi _ { h } ( y _ { 0 } ) \qquad \mathrm { o n } ~ \mathbb { R } ^ { d } ,
$$

which isanumerical integrator for the Poisson system (5.52).

Example5.10.For therigid body,applyingthe RATTLE algorithm to theconstrained Hamiltonian system (5.18）yields theintegrator for the Euler equations discussed in Sect.VII.5.3.By the followingresult thisisaPoisson integrator.

Theorem 5.11.1f $\varPhi _ { h } ( P , Q )$ isasymplecticand left-invariant integrator for(5.43), thenitsreduction $\psi _ { h } ( y )$ isa Poisson map.

ProofWewrite $\psi _ { h }$ as the composition

$$
\psi _ { h } : \mathbb { R } ^ { d } \xrightarrow { \xi } T ^ { * } G \xrightarrow { \phi _ { h } } T ^ { * } G \xrightarrow { \eta } \mathbb { R } ^ { d }
$$

were $\eta = ( \eta _ { j } )$ iste unetic $\eta _ { j } ( P , Q ) = y _ { j }$ for $\begin{array} { r } { Q ^ { T } P = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } } \end{array}$ and $\xi$ $\eta$ $\eta \circ \xi = \operatorname { i d }$   
$K , L$ on $\mathbb { R } ^ { d }$ we then have for $( P , Q ) = \xi ( y )$ ,usingLemma5.9intheouter equalities   
and the symplecticity of $\phi _ { h }$ in themiddle equality,

$$
\begin{array} { r c l } { [ K \circ \psi _ { h } , L \circ \psi _ { h } \} ( y ) } & { = } & { \{ K \circ \eta \circ \varPhi _ { h } , L \circ \eta \circ \varPhi _ { h } \} _ { \mathrm { c a n } } ( P , Q ) } \\ & { = } & { \{ K \circ \eta , L \circ \eta \} _ { \mathrm { c a n } } \big ( \varPhi _ { h } ( P , Q ) \big ) = \{ K , L \} \big ( \psi _ { h } ( y ) \big ) . } \end{array}
$$

This equation states that $\psi _ { h }$ is a Poisson map.

Asimilar reduction inadiscrete Lagrangian framework is studied byMarsden, Pekarsky&Shkoller（1999).

Thereduced numerical maps $\psi _ { h }$ and $\psi _ { h }$ have further structure-preserving properties:they preserve the Casimirs and the co-adjoint orbits.Thiswill be shown in Sect.IX.5.3with the help of backward error analysis.

# VII.6 Reduced Models of Quantum Dynamics

Toincorporate quantum effects in molecular dynamics simulations,computations aredonewith models that are intermediate between classical moleculardynamicsbased on Newton'sequations of motion and full quantum dynamics described bythe $N$ -particle Schrodinger equation.Thedirect computational treatment of the latteris not feasible because of its high dimensionality.These intermediate modelsareobtained by the Hamiltonian reduction(2.17） froman infinite-dimensional Hilbert space to an appropriately chosen manifold.In chemical physics,thisreductionisknownas the Dirac-Frenkel time-dependent variational principle.We illustrate this procedure for the case where the quantum-mechanical wave function isapproximated byacomplex Gaussian as proposed by Heller(1975).It turns out that the resulting ordinary differential equations have a Poisson structure,which wasrecently described by Faou&Lubich(2Oo4).Followingthat paper,we derive astructure-preserving explicit integrator for Gaussian wavepackets,which tends to theStormer-Verletmethod in theclassical limit.

# VII.6.1 Hamiltonian Structure of the Schrodinger Equation

The introduction of wave mechanics stands..as Schrodinger's monument and aworth one. (From Schrodinger's obituary inTheTimes1961:quoted from http://www-groups.dcs.st-and.ac.uk/history/Mathematicians/Schrodinger.html)

The time-dependent $\mathcal { N }$ -body Schrodinger equation reads (see,e.g.,Messiah (1999) and Thaller (2000))

$$
i \varepsilon { \frac { \partial { \psi } } { \partial t } } = H { \psi }
$$

for the wave function $\psi ~ = ~ \psi ( x , t )$ depending on the spatial variables $x =$ $( x _ { 1 } , \ldots , x _ { N } )$ with $x _ { k } \in \mathbb { R } ^ { d }$ (e.g.,with $d = 1$ or3in the partition）and the time $t \in \mathbb { R } .$ The squared absolute value $| \psi ( x , t ) | ^ { 2 }$ represents the joint probability density for $N$ particles to beat the positions $\mathcal { L } _ { 1 } , \ldots , \mathcal { L } _ { N }$ attime $t .$ In(6.1）, $\boldsymbol { \varepsilon }$ isa(small) positive number representing the scaled Planck constant and $i$ is thecomplex imaginary unit.The Hamiltonian operator $H$ iswritten

$$
H = T + V
$$

with the kinetic and potential energy operators

$$
T = - \sum _ { k = 1 } ^ { N } \frac { \varepsilon ^ { 2 } } { 2 m _ { k } } \varDelta _ { x _ { k } } \quad \mathrm { a n d } \quad V = V ( x ) ,
$$

where $m _ { k } > 0$ isa particle mass and $\varDelta _ { x _ { k } }$ the Laplacianin the variable $\boldsymbol { x } _ { k } \in \mathbb { R } ^ { d }$ , and where the real-valued potential $V$ acts asa multiplication operator $( V \phi ) ( x ) =$ $V ( x ) \phi ( x )$ .Underappropriate conditionson $V$ （boundedness of $V$ issufficient, butbynomeans necessary）,the operator $H$ is thena self-adjoint operator on thecomplex Hilbert space $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } )$ with domain ${ \cal D } ( H ) = { \cal D } ( T ) = \{ \phi \in$ $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } )$ $T \phi \in L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } ) \}$ ;see Sect.V.5.3ofKato(1980).

We separate thereal and imaginary parts of $\psi = v + i w \in L ^ { 2 } ( \mathbb R ^ { d N } , \mathbb C )$ ,the complexHilbert space ofLebesgue square-integrable functions.Thefunctions $v$ and $w$ arethus functions in thereal Hilbert space $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { R } )$ .We denote the complex inner product by $\langle \cdot , \cdot \rangle$ and the real inner product by $( \cdot , \cdot )$ .The $L ^ { 2 }$ normswill be simply denoted by $\| \cdot \|$

As $H$ isareal operator,formula(6.1） can bewritten

$$
\begin{array} { r c l } { { \varepsilon \dot { v } } } & { { = } } & { { H w , } } \\ { { \varepsilon \dot { w } } } & { { = } } & { { - H v , } } \end{array}
$$

orequivalently,with the canonical structure matrix

$$
J = \left( \begin{array} { c c } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right)
$$

and the Hamiltonian function (we use the same symbol $H$ as for the operator)

$$
H ( v , w ) = \frac { 1 } { 2 } \langle \psi , H \psi \rangle = \frac { 1 } { 2 } ( v , H v ) + \frac { 1 } { 2 } ( w , H w )
$$

for $\psi = v + i w$ in the domain of the operator $H$ .This becomes the canonica Hamiltonian system

$$
\left( \begin{array} { l } { \dot { v } } \\ { \dot { w } } \end{array} \right) = \varepsilon ^ { - 1 } J ^ { - 1 } \nabla H ( v , w ) .
$$

Note that the real multiplication with $J$ corresponds to the complex multiplication with the imaginary unit $i$ .The flow of this system preserves the canonical symplectic two-form

$$
\omega ( \xi _ { 1 } , \xi _ { 2 } ) = ( J \xi _ { 1 } , \xi _ { 2 } ) , \qquad \xi _ { 1 } , \xi _ { 2 } \in L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { R } ) ^ { 2 } .
$$

# VII.6.2 TheDirac-Frenkel Variational Principle

Fordealingwith atoms involvingmany electrons the accurate quantum theory,involvinga solution of thewave equation in many-dimensional space,is far too complicated to bepracticable.One must therefore resort toapproximate methods. (P.A.M.Dirac 1930)

Reduced models of the Schrodinger equation are obtained by restricting theequation toanapproximationmanifold $\mathcal { M }$ via (2.17),viz.,

$$
\begin{array} { r } { ( \varepsilon J \dot { \boldsymbol { u } } - \nabla H ( \boldsymbol { u } ) , \boldsymbol { \xi } ) = 0 \qquad \mathrm { f o r ~ a l l } \quad \boldsymbol { \xi } \in T _ { \boldsymbol { u } } \mathcal { M } , } \end{array}
$$

or equivalently in complex notation for $u = ( v , w ) ^ { T } = v + i w ,$

$$
\begin{array} { r } { \mathrm { { R e } } \left. \varepsilon i \dot { u } - H u , \xi \right. = 0 \qquad \mathrm { { f o r \ a l l } } \quad \xi \in T _ { u } \mathcal { M } . } \end{array}
$$

Taking thereal part can be omitted if the tangent space $\boldsymbol { T _ { u } } \boldsymbol { M }$ is complex linear. Equation(6.5）（usuallywithout thereal part） isknown astheDirac-Frenkel timedependentvariational principle,afterDirac（193O)andFrenkel （1934)；seealso McLachlan（1964),Heller（1976),Beck,Jackle,Worth&Meyer(2000),and references therein.

Wechoose a (local) coordinate map $u = \chi ( y )$ of $\mathcal { M }$ and denote its derivative $X _ { \mathbb { C } } ( y ) = V ( y ) + i W ( y ) = \chi ^ { \prime } ( y )$ or in the real setting as $X = { \binom { V } { W } } .$ Denoting by $X ^ { T }$ theadjoint of $X$ withrespect to the real inner product $( \cdot , \cdot )$ ,we thus obtain

$$
\varepsilon X ( y ) ^ { T } J X ( y ) \dot { y } = X ( y ) ^ { T } \nabla _ { u } H ( \chi ( y ) ) .
$$

With $X _ { \mathbb { C } } ^ { * }$ denoting the adjoint of $X _ { \mathbb { C } }$ with respect to the complex inner product $\langle \cdot , \cdot \rangle$ , wenote $X _ { \mathbb { C } } ^ { * } X _ { \mathbb { C } } = ( V ^ { T } V + W ^ { T } W ) + i ( V ^ { T } W - W ^ { T } V ) = X ^ { T } X - i X ^ { T } J X$ and hence

$$
X ^ { T } J X = - \mathrm { I m } X _ { \mathbb { C } } ^ { * } X _ { \mathbb { C } } .
$$

Lemma 6.1.If $x _ { u } M$ isacomplex linear space forevery $u \in \mathcal { M }$ ,then $\mathcal { M }$ is $^ a$ symplectic submanifoldof $L ^ { 2 } ( \mathbb { R } ^ { N } , \mathbb { R } ) ^ { 2 }$ ,thatis,the symplectic two-form(6.3)is non-degenerate on $\boldsymbol { x } _ { u } \boldsymbol { \mathcal { M } }$ for all $u \in \mathcal { M }$ Expressedin coordinates,

$$
X ( y ) ^ { T } J X ( y ) \ i s \ i n \nu e r t i b l e f o r \ a l l \ y .
$$

Proof.Wefix $u = x ( y ) \in \mathcal { M }$ and omit the argument $y$ in the following. Since $T _ { u } { \mathcal { M } } = \mathop { \mathrm { R a n g e } } ( X _ { \mathbb { C } } )$ iscomplex linear byassumption,there existsa real linear mapping $L : \mathbb { R } ^ { m }  \mathbb { R } ^ { m }$ such that $i X _ { \mathbb { C } } \eta = X _ { \mathbb { C } } L \eta$ forall $\eta \in \mathbb { R } ^ { m } .$ This implies

$$
J X = X L \quad { \mathrm { a n d } } \quad L ^ { 2 } = - \operatorname { I d }
$$

and hence $X ^ { T } J X = X ^ { T } X L$ which is invertible.

Approximation properties of the Dirac-Frenkel variational principlecan beobtained fromthe interpretationas the orthogonal projection $\begin{array} { r } { \dot { u } = P _ { \perp } ( u ) \frac { 1 } { i \varepsilon } H u . } \end{array}$ which corresponds to taking the imaginary part in (6.5),as opposed to the symplectic projectionin(6.4）whichcorrespondsto thereal part.SeeLubich (2oo5) foranearoptimality result forapproximation on the manifold.

# VII.6.3 Gaussian Wavepacket Dynamics

Wedevelopa new approach to semiclassical dynamicswhich exploits the factthat extended wavefunctions for heavyparticles (orparticles inharmonicpotentials)may be decomposed into time-dependent wave packets,which spread minimally and which execute classical or nearly classicaltrajectories.AGaussian form for the wave packetsisassumed and equations of motion are derived for the parameters characterizing the Gaussian. (E.J.Heller1975)

Thevariational Gaussian wavepacket dynamics of Heller（1976) is obtained by choosing the manifold $\mathcal { M }$ in(6.5）as consisting of complex Gaussians.For ease ofpresentation we restrict our attention in the following to the one-particle case $N = 1$ （the extension to $N > 1$ isstraightforward;cf.Heller（1976）and Faou& Lubich(2004)).Herewe have

$$
\mathcal { M } = \{ u = \chi ( y ) \in L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } ) : y = ( p , q , \alpha , \beta , \gamma , \delta ) \in \mathbb { R } ^ { 2 d + 4 } \mathrm { ~ w i t h ~ } \beta > 0 \}
$$

with

$$
\Big ( \chi ( y ) \Big ) ( x ) = \exp \Big ( \frac { i } { \varepsilon } \big ( ( \alpha + i \beta ) | x - q | ^ { 2 } + p \cdot ( x - q ) + \gamma + i \delta \big ) \Big ) ,
$$

where $| \cdot |$ and·stand for the Euclidean norm and inner product on $\mathbb { R } ^ { d }$ Theparameters $q$ and $p$ represent the average position and momentum,respectively:for $u = \chi ( y )$ with $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta )$ and $\lVert u \rVert = 1$ ,adirect calculation shows that

$$
q = \langle u , x u \rangle = \int _ { \mathbb { R } ^ { d } } x | u ( x ) | ^ { 2 } d x , \qquad p = \langle u , - i \varepsilon \nabla u \rangle .
$$

Theparameter $\beta > 0$ determines thewidth of the wavepacket.The tangent space $T _ { u } \mathcal { M } \subset L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } )$ at a given point $u = \chi ( y ) \in \mathcal { M }$ is $( 2 d + 4 )$ -dimensional and is made of the elements of $L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } )$ written as

$$
{ \frac { i } { \varepsilon } } { \Bigl ( } ( A + i B ) | x - q | ^ { 2 } + ( P - 2 ( \alpha + i \beta ) Q ) \cdot ( x - q ) - p \cdot Q + C + i D { \Bigr ) } u
$$

with arbitrary $( P , Q , A , B , C , D ) ^ { T } \in \mathbb { R } ^ { 2 d + 4 } .$ Wenote that $x _ { u } M$ is complex linear, and $u \in T _ { u } { \mathcal { M } } .$ Bychoosing $\xi = i u$ in(6.5),this yields $( d / d t ) \| u \| ^ { 2 } = 2 \operatorname { R e } \left. \dot { u } , u \right. =$ O and hence the preservation of the squared $L ^ { 2 }$ normof $u = \chi ( y )$ ,which is given by

$$
\begin{array} { l l l } { { I ( y ) } } & { { = } } & { { \displaystyle \| u \| ^ { 2 } = \int _ { \mathbb R ^ { d } } \lvert u ( x ) \rvert ^ { 2 } d x } } \\ { { } } & { { = } } & { { \displaystyle \int _ { \mathbb R ^ { d } } \exp \left( - \frac 2 { \varepsilon } \bigl ( \beta \lvert x - q \rvert ^ { 2 } + \delta \bigr ) \right) d x = \exp \left( - \frac { 2 \delta } { \varepsilon } \right) \left( \frac { \pi \varepsilon } { 2 \beta } \right) ^ { d / 2 } . } } \end{array}
$$

The physically reasonable situation is $\| u \| ^ { 2 } = 1$ ,which corresponds to the interpretation of $\vert u ( x ) \vert ^ { 2 }$ asaprobability density.

With these preparations we have the following result of Faou&Lubich (2004).

Theorem6.2. TheHamiltonianreductionoftheSchrodingerequationtotheGaussian wavepacket manifold $\mathcal { M }$ of(6.7)-(6.8)yieldsthePoissonsystem

$$
\dot { y } = B ( y ) \nabla K ( y )
$$

where,for $y = ( p , q , \alpha , \beta , \gamma , \delta ) \in \mathbb { R } ^ { 2 d + 4 }$ with $\beta > 0$ ,andwith $1 _ { d }$ denoting the $d$ -dimensionalidentity,

$$
B ( y ) = \frac { 1 } { I ( y ) } \left( \begin{array} { c c c c c c } { 0 } & { - 1 _ { d } } & { 0 } & { 0 } & { - p } & { 0 } \\ { 1 _ { d } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \frac { 4 \beta ^ { 2 } } { \epsilon d } } & { 0 } & { - \beta } \\ { 0 } & { 0 } & { - \frac { 4 \beta ^ { 2 } } { \epsilon d } } & { 0 } & { \beta } & { 0 } \\ { p ^ { T } } & { 0 } & { 0 } & { - \beta } & { 0 } & { \frac { d + 2 } { 4 } \varepsilon } \\ { 0 } & { 0 } & { \beta } & { 0 } & { - \frac { d + 2 } { 4 } \varepsilon } & { 0 } \end{array} \right)
$$

definesaPoissonstructure,andfor $u = \chi ( y )$ ，

$$
K ( y ) = \langle u , H u \rangle = K _ { T } ( y ) + K _ { V } ( y )
$$

isthetotalenergywithineticndpotentialpts

$$
K _ { T } ( y ) = I ( y ) \left( \frac { | p | ^ { 2 } } { 2 m } + \frac { \varepsilon d } { 2 m } \frac { \alpha ^ { 2 } + \beta ^ { 2 } } { \beta } \right) = \langle u , T u \rangle
$$

and

$$
K _ { V } ( y ) = \int _ { \mathbb { R } ^ { d } } V ( x ) \exp \Big ( - \frac { 2 } { \varepsilon } \big ( \beta | x - q | ^ { 2 } + \delta \big ) \Big ) d x = \langle u , V u \rangle .
$$

Both $K ( y )$ and $I ( y )$ arefirstintegralsofthe system.

Proofsi $y$ is $\begin{array} { r } { \varepsilon X ( y ) ^ { T } J X ( y ) \dot { y } = \frac { 1 } { 2 } \nabla K ( y ) . } \end{array}$ Wenote (6.6)and

$$
X _ { \mathbb { C } } ( y ) = \frac { i } { \varepsilon } \left( x - q , - 2 a ( x - q ) - p , | x - q | ^ { 2 } , i | x - q | ^ { 2 } , 1 , i \right) u
$$

where $a = \alpha + \ i \beta$ and $u = \chi ( y )$ in the complex seting.Using the calculus of Gaussian integrals,we compute

$$
\small \begin{array} { r } { \zeta ^ { T } ( y ) J X ( y ) = \displaystyle { \frac { 1 } { 2 } } I ( y ) \left( \begin{array} { c c c c c c } { 0 } & { 1 _ { d } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 _ { d } } & { 0 } & { 0 } & { \frac { d p } { 2 \beta } } & { 0 } & { \frac { 2 p } { \varepsilon } } \\ { 0 } & { 0 } & { 0 } & { - \frac { \varepsilon d ( d + 2 ) } { 8 \beta ^ { 2 } } } & { 0 } & { - \frac { d } { 2 \beta } } \\ { 0 } & { - \frac { d p ^ { T } } { 2 \beta } } & { \frac { \varepsilon d ( d + 2 ) } { 8 \beta ^ { 2 } } } & { 0 } & { \frac { d } { 2 \beta } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \frac { d } { 2 \beta } } & { 0 } & { - \frac { 2 } { \varepsilon } } \\ { 0 } & { - \frac { 2 p ^ { T } } { \varepsilon } } & { \frac { d } { 2 \beta } } & { 0 } & { \frac { 2 } { \varepsilon } } & { 0 } \end{array} \right) , } \end{array}
$$

and inversion yields the differential equation with $B ( y ) = ( 2 \varepsilon X ^ { T } ( y ) J X ( y ) ) ^ { - 1 }$ as stated.The system isa Poisson system by Theorem 2.8.

Assuming $I ( y ) = \| u \| ^ { 2 } = 1$ ,weobserve thatthedifferential equationsfor the average position and momentum, $q$ and $p$ ,read

$$
\begin{array} { r } { \dot { q } = p / m , \qquad \dot { p } = - \langle u , \nabla V u \rangle } \end{array}
$$

for $u = \chi ( y )$ and $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta ) ,$ We then note $\langle u , \nabla V u \rangle \to \nabla V ( q )$ as $\varepsilon  0$ Thedifferential equations for $q$ and $p$ thus tend to Newtonian equations of motion in the classical limit $\varepsilon  0$ ：

$$
\dot { q } = p / m , \qquad \dot { p } = - \nabla V ( q ) .
$$

It will be useful to consider also scaled variables

$$
\widehat { \boldsymbol { y } } = \left( \boldsymbol { p } , \boldsymbol { q } , \alpha , \widehat { \beta } , \gamma , \widehat { \delta } \right) \in \mathbb { R } ^ { 2 d + 4 } \qquad \mathrm { w i t h } \quad \widehat { \beta } = \frac { \beta } { \varepsilon } , \widehat { \delta } = \frac { \delta } { \varepsilon } .
$$

Herewe have

$$
\dot { \widehat { \boldsymbol { y } } } = \widehat { \boldsymbol { B } } ( \widehat { \boldsymbol { y } } ) \nabla \widehat { \boldsymbol { K } } ( \widehat { \boldsymbol { y } } )
$$

where the structure matrix $\widehat { B } ( \widehat { y } )$ is independent of $\boldsymbol { \varepsilon }$ and where $\widehat { K } ( \widehat { \boldsymbol { y } } )$ depends regularlyon $\varepsilon \geq 0$

# VII.6.4 A Splitting Integrator for Gaussian Wavepackets

With the natural splitting $H = T + V$ into kineticand potential energy,we now consider the variational splittingintegrator(4.7)-(4.8),which here becomes the following.

1.We define $u _ { n } ^ { + }$ in $\mathcal { M }$ as the solution at time $h / 2$ of the equation for $u$ ,

$$
\langle i \varepsilon { \dot { u } } - V u , \xi \rangle = 0 \mathrm { ~ f o r ~ a l l ~ } \xi \in T _ { u } { \mathcal { M } }
$$

with initial value $u ( 0 ) = u _ { n } \in \mathcal { M }$

2.We define $u _ { n + 1 } ^ { - }$ as the solution at time $h$ of

$$
\langle i \varepsilon { \dot { u } } - T u , \xi \rangle = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { u } { \mathcal { M } }
$$

with initial value $u ( 0 ) = u _ { n } ^ { + }$

3. Then $u _ { n + 1 }$ is te solution at time $h / 2$ of (6.18) with initial value $u ( 0 ) = u _ { n + 1 } ^ { - }$

By Theorem 6.2,the substeps in thedefinition of this splitting method writen in the coordinates $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta )$ are the exact flows $\varphi _ { h / 2 } ^ { V }$ and $\varphi _ { h } ^ { T }$ of the Poisson systems

$$
\dot { \boldsymbol { y } } = B ( \boldsymbol { y } ) \nabla K _ { V } ( \boldsymbol { y } ) \quad \mathrm { ~ a n d ~ } \quad \dot { \boldsymbol { y } } = B ( \boldsymbol { y } ) \nabla K _ { T } ( \boldsymbol { y } ) .
$$

Note that both equations preserve the $L ^ { 2 }$ norm of $u = \chi ( y )$ ,which we assume to be 1 in the following.

Most remarkably,these equations can be solved explicitly.Let us consider first the equations (6.19).They are written,for $a = \alpha + i \beta$ and $c = \gamma + i \delta$ ,as

$$
\left\{ \begin{array} { r c l l c l } { \dot { q } } & { = } & { p / m , } & { } & { \begin{array} { r c l l c r } { \dot { a } } & { = } & { - 2 a ^ { 2 } / m , } & { } & { } \\ { \dot { \hat { c } } } & { = } & { \left( \frac { 1 } { 2 } | p | ^ { 2 } + i \varepsilon d a \right) / m , } \end{array} } \end{array} \right.
$$

with initial values $y _ { 0 } = ( p _ { 0 } , q _ { 0 } , a _ { 0 } , c _ { 0 } )$ corresponding to $u _ { 0 } = \chi ( y _ { 0 } ) .$ They have the solution

$$
q ( t ) = q _ { 0 } + \frac { t } { m } p _ { 0 } , \qquad p ( t ) = p _ { 0 } , \qquad a ( t ) = \frac { a _ { 0 } } { 1 + 2 a _ { 0 } t / m } ,
$$

and

$$
c ( t ) = c _ { 0 } + t \frac { | p _ { 0 } | ^ { 2 } } { 2 m } + \frac { i \varepsilon d } 2 \log \left( 1 + \frac { 2 a _ { 0 } t } m \right) ,
$$

Let usnow consider the equations (6.18).Taking into account the fact that the potential $V$ isreal,theseequations arewritten

$$
\begin{array} { r l r } & { \dot { p } = - \langle { u } , \nabla { V } { u } \rangle , \quad } & { \dot { q } = 0 , } \\ & { \dot { \alpha } = - \frac { 1 } { 2 d } \langle { u } , \Delta { V } { u } \rangle , \quad } & { \dot { \beta } = 0 , } \\ & { \dot { \gamma } = - \langle { u } , { V } { u } \rangle + \frac { \epsilon } { 8 \beta } \langle { u } , \Delta { V } { u } \rangle , \quad } & { \dot { \delta } = 0 , } \end{array}
$$

with the $L ^ { 2 }$ inner products

$$
\langle u , W u \rangle = \int _ { \mathbb { R } ^ { d } } W ( x ) \exp { \Big ( } - { \frac { 2 } { \varepsilon } } { \big ( } \beta | x - q | ^ { 2 } + \delta { \big ) } { \Big ) } d x
$$

for $W = V , \nabla V , \Delta V .$ Asthe $L ^ { 2 }$ inner products in the equations for $p$ , $\alpha$ , $\gamma$ depend onlyon $q , \beta , \delta$ which are constant along this trajectory,these equations can be solved til $\varPhi _ { h } = \varphi _ { h / 2 } ^ { V } \circ \varphi _ { h } ^ { T } \circ \varphi _ { h / 2 } ^ { V }$   
Thisgives thefollowingalgorithm(Faou&Lubich 2004).

Algorithm6.3(Gaussian Wavepacket Integrator).A stepfrom time $t _ { n }$ to $t _ { n + 1 }$ starting fromthe Gaussian wavepacket $u _ { n } = \chi ( p _ { n } , q _ { n } , \alpha _ { n } , \beta _ { n } , \gamma _ { n } , \delta _ { n } )$ proceedsas follows:

1.With $\langle W \rangle _ { n } = \langle u _ { n } , W u _ { n } \rangle$ given by(6.22)for $W = V , \nabla V , \Delta V$ compute

$$
\begin{array} { r c l } { { p _ { n + 1 / 2 } } } & { { = } } & { { p _ { n } - { \displaystyle \frac { h } { 2 } } \langle \nabla V \rangle _ { n } } } \\ { { } } & { { } } & { { } } \\ { { \alpha _ { n } ^ { + } } } & { { = } } & { { \alpha _ { n } - { \displaystyle \frac { h } { 4 d } } \langle \Delta V \rangle _ { n } } } \\ { { } } & { { } } & { { } } \\ { { \gamma _ { n } ^ { + } } } & { { = } } & { { \gamma _ { n } + { \displaystyle \frac { h \varepsilon } { 1 6 \beta _ { n } } } \langle \Delta V \rangle _ { n } . } } \end{array}
$$

2.From the values $p _ { n + 1 / 2 }$ ， $a _ { n } ^ { + } = \alpha _ { n } ^ { + } + i \beta _ { n }$ and $c _ { n } ^ { + } = \gamma _ { n } ^ { + } + i \delta _ { n }$ compute $q _ { n + 1 }$ ， $a _ { n + 1 } ^ { - } = \alpha _ { n + 1 } ^ { - } + i \beta _ { n + 1 } ,$ and $c _ { n + 1 } ^ { - } = \gamma _ { n + 1 } ^ { - } + i \delta _ { n + 1 } \nu i a$

$$
\begin{array} { r c l } { { q _ { n + 1 } } } & { { = } } & { { q _ { n } + { \displaystyle \frac { h } { m } } p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { \dot { a } _ { n + 1 } ^ { - } } } & { { = } } & { { { \displaystyle a _ { n } ^ { + } } \Big / \Big ( 1 + { \displaystyle \frac { 2 h } { m } } a _ { n } ^ { + } \Big ) } } \\ { { } } & { { } } & { { } } \\ { { c _ { n + 1 } ^ { - } } } & { { = } } & { { c _ { n } ^ { + } + { \displaystyle \frac { i \varepsilon d } { 2 } } \log \Big ( 1 + { \displaystyle \frac { 2 h } { m } } a _ { n } ^ { + } \Big ) . } } \end{array}
$$

3.Compute $p _ { n + 1 } , \alpha _ { n + 1 } , \gamma _ { n + 1 } f r o m$

$$
\begin{array} { r c l } { \displaystyle p _ { n + 1 } } & { = } & { \displaystyle p _ { n + 1 / 2 } - \frac { h } { 2 } \langle \nabla V \rangle _ { n + 1 } } \\ { \displaystyle \alpha _ { n + 1 } } & { = } & { \displaystyle \alpha _ { n + 1 } ^ { - } - \frac { h } { 4 d } \langle \varDelta V \rangle _ { n + 1 } } \\ { \gamma _ { n + 1 } } & { = } & { \displaystyle \gamma _ { n + 1 } ^ { - } + \frac { h \varepsilon } { 1 6 \beta _ { n + 1 } } \langle \varDelta V \rangle _ { n + 1 } . } \end{array}
$$

Let us collect properties of this algorithm.

Theorem6.4.The splittingschemeofAlgorithm6.3isanexplicit,symmetric, second-order numerical methodforGaussianwavepacketdynamics(6.11)-(6.13). ItisaPoissonintegratorforthe structurematrix(6.12),andit preservestheunit $L ^ { 2 }$ normof the wavepackets: $\| u _ { n } \| = 1$ forall $_ { n }$ .

Inthe limit $\varepsilon  0$ ,theposition andmomentum approximations $q _ { n }$ , $p _ { n }$ ofthis methodtendtothoseobtainedbyapplyingthe Stormer-Verletmethodtotheassociatedclassical mechanical system(6.15).

Thestatement for $\varepsilon  0$ follows directly from theequations for $_ { p _ { n + 1 / 2 } }$ ， $q _ { n + 1 }$ $p _ { n + 1 }$ and from noting $\langle \nabla V \rangle _ { n } \to \nabla V ( q _ { n } )$

Inview of the small parameter $\boldsymbol { \varepsilon }$ ,thediscussion of the order of the method requires morecare.Here it isuseful toconsider the integrator in the scaled variables $\boldsymbol { \widehat { y } } = ( p , q , \alpha , \beta / \varepsilon , \gamma , \delta / \varepsilon )$ of(6.16).Since the differential equation(6.17) contains $\in$ onlyasaregularperturbation parameter,after $_ { n }$ steps of the splitting integrator we havethe $\varepsilon$ -uniformerrorbound

$$
{ \widehat { y } } _ { n } - { \widehat { y } } ( t _ { n } ) = O ( h ^ { 2 } ) ,
$$

where the constants symbolized by the $O$ -notationare independentof $\boldsymbol { \varepsilon }$ andof $n$ and $h$ with $n h \leq$ Const.For the approximation of the absolute values of the Gaussian wavepackets thisyields

$$
\left| \left| u _ { n } \right| ^ { 2 } - | u ( t _ { n } ) | ^ { 2 } \right| = O ( h ^ { 2 } ) ,
$$

but the approximation of the phases is only such that

$$
\| u _ { n } - u ( t _ { n } ) \| = O ( h ^ { 2 } / \varepsilon ) .
$$

Wereferto Faou $\&$ Lubich(2oo4）for the formulation of the correspondingalgorithmfor $N > 1$ particles,for further properties such as the exact conservation oflinear and angular momentum and the long-time near-conservation of the total energy $\{ u _ { n } , H u _ { n } \}$ ,and for numerical experiments.

# VII.7 Exercises

1.Prove that the Poisson bracket (2.8) satisfies the Jacobi identity(2.4) for all functions $F , G , H$ ,ifand onlyif it satisfies(2.4) for thecoordinate functions $y _ { i } , y _ { j } , y _ { k }$

Hint(F.Engel,inLie'sGesammelteAbh.vol.5,p.753).IftheJacobi identityis writtenasin(3.3）,we see that there are no second partial derivatives of $F ^ { \prime }$ (the lefthand sideisaLie bracket,theright-hand sidehasno second derivativesof $F$ anyway).Other permutations show the same result for $G$ and $H$ .

2.For $x$ in an open subset of $\mathbb { R } ^ { m }$ ,let $A ( x ) = { \bigl ( } a _ { i j } ( x ) { \bigr ) }$ bean invertible skewsymmetric $m \times m$ -matrix,with

$$
{ \frac { \partial a _ { i j } } { \partial x _ { k } } } + { \frac { \partial a _ { k i } } { \partial x _ { j } } } + { \frac { \partial a _ { j k } } { \partial x _ { i } } } = 0 \qquad { \mathrm { f o r ~ a l l ~ } } i , j , k .
$$

（a）Show that $B ( x ) = A ( x ) ^ { - 1 }$ satisfies(2.1O)and hence definesa Poisson bracket.   
(b) Generalize Theorem 2.8 to Hamiltonian equations(2.18)with the two-form $\omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) = \xi _ { 1 } ^ { I } A ( x ) \xi _ { 2 }$ ,   
Remark.Condition(7.1） says that $\omega$ isa closed differential form.

3.Solve the following first order partial differential equation:

$$
3 { \frac { \partial F } { \partial y _ { 1 } } } + 2 { \frac { \partial F } { \partial y _ { 2 } } } - 5 { \frac { \partial F } { \partial y _ { 3 } } } = 0 .
$$

Result. $f ( 2 y _ { 1 } - 3 y _ { 2 } , 5 y _ { 2 } + 2 y _ { 3 } )$

4.Find two solutions of the homogeneous system

$$
3 \frac { \partial F } { \partial y _ { 1 } } + \frac { \partial F } { \partial y _ { 2 } } - 2 \frac { \partial F } { \partial y _ { 3 } } - 5 \frac { \partial F } { \partial y _ { 4 } } = 0 , \qquad 2 \frac { \partial F } { \partial y _ { 1 } } - \frac { \partial F } { \partial y _ { 2 } } - 3 \frac { \partial F } { \partial y _ { 4 } } = 0 ,
$$

such that their gradients are linearly independent.

5.Consider a Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ andachange of coordinates $z ~ = ~ \vartheta ( y )$ Prove that inthe new coordinates the system isof the form $\dot { z } = \bar { B } ( z ) \nabla K ( z )$ ,where $\bar { B } ( z ) = \vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T }$ (cf.formula (3.12))and $K ( z ) = H ( y )$ .

6.Givean elementary proof of Theorem4.3.

Hint.Define $\delta ( t ) : = \varphi _ { t } ^ { \prime } ( y ) B ( y ) \varphi _ { t } ^ { \prime } ( y ) ^ { T } \ - \ B \big ( \varphi _ { t } ( y ) \big )$ Using the variational equation for(4.1） prove that $\delta ( t )$ is the solution of a homogeneous linear differential equation.Therefore, $\delta ( 0 ) = 0$ implies $\delta ( t ) = 0$ forall $t$ .

7. Let $z = \vartheta ( y )$ bea transformation taking the Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ to $\dot { z } = \tilde { B } ( z ) \nabla K ( z )$ Prove that $\varPhi _ { h } ( y )$ isa Poisson integrator for $B ( y )$ if and onlyif $\varPsi _ { h } ( z ) = \vartheta \circ \varPhi _ { h } \circ \vartheta ^ { - 1 } ( z )$ isaPoisson integrator for $\bar { B } ( z )$ ,

8.Let $B$ beaskew-symmetric but otherwise arbitrary constant matrix,and consider the Poisson system $\dot { y } = B \nabla H ( y )$ Prove that every symplectic Runge-Kutta method isa Poisson integrator for such asystem. Hint.Transform $B$ toblock-diagonal form.

9.(M.J.Gander 1994).Consider theLotka-Volterra equation (2.13) with separable Hamiltonian $H ( u , v ) = K ( u ) + L ( v ) ,$ Prove that

$$
u _ { n + 1 } = u _ { n } + h u _ { n } v _ { n } H _ { v } ( u _ { n } , v _ { n } ) , \quad v _ { n + 1 } = v _ { n } - h u _ { n + 1 } v _ { n } H _ { u } ( u _ { n + 1 } , v _ { n } )
$$

is a Poisson integrator for this system.

10.Find a change of coordinates that transforms the Lotka-Volterra system (2.14) intoaHamiltonian system (in canonical form).Following the approach of Example 4.11constructPoisson integrators forthis system.

11.Prove that the matrix $B ( y )$ ofExample2.7definesaPoisson bracket,by showingthat the bracketis givenasDirac's bracket(Dirac 1950)

$$
\{ F , G \} = \{ { \widehat F } , { \widehat G } \} - \textstyle \sum _ { i , j } \{ { \widehat F } , c _ { i } \} \gamma _ { i j } \{ c _ { j } , { \widehat G } \} .
$$

Here $F$ and $G$ are functions of $_ y$ , $\hat { F }$ and $\widehat { G }$ are smooth functions of $x$ satisfying $\widehat { F } ( x ( y ) ) \ : = \ : F ( y )$ and $G ( \chi ( y ) ) = G ( y )$ ， $c _ { i } ( x )$ aretheconstraintfunctions defining the manifold $\mathcal { M }$ ,and $\gamma _ { i j }$ are theentries of the inverse of thematrix $\left( \left\{ c _ { i } , c _ { j } \right\} \right)$ ThePoisson bracket to the left in（7.2） correspondsto $B ( y )$ and those totheright are thecanonical brackets evaluatedat $x = \chi ( y )$ Replacing $\hat { F } ( x )$ by $\begin{array} { r } { \widehat { F } ( x ) + \sum _ { k } \mu _ { k } ( x ) c _ { k } ( x ) } \end{array}$ with $\mu _ { k } ( x )$ such that $\{ \widehat { F } , c _ { k } \} = 0$ on $\mathcal { M }$ eliminates the sumin(7.2)and proves the Jacobi identity for $B ( y )$ .

# Chapter VIII. Structure-Preserving Implementation

Thischapter is devoted to practical aspects of an implementation of geometric integrators.We explain strategies for changing the step size whichdo not deteriorate the correct qualitative behaviour of the solution.We study multiple time stepping strategies,the effect of round-off in long-time integrations,and the efficient solution of nonlinear systems arising in implicit integration schemes.

# VIII.1 Dangers of Using Standard Step Size Control

Another possible shortcoming of the method concerns its behavior when usedwitha variable stepsize...The integratorcompletely loses its desirable qualities...This can be understood at least qualitatively by realizing thatby changing the time step one is in essence continually changingthe nearby Hamiltonian... (B.Gladman,M.Duncan&J.Candy1991)

In the previouschapterswe have studied symmetricand symplectic integrators,and wehave seen an enormous progress in long-time integrations of various problems. Decadesago,a similar enormous progresswas the introduction of algorithms with automatic step size control.Naively,one would expect that the blind combination ofboth techniques leads to even betterperformances.We shall see bya numerical experiment that thisis not the case,a phenomenon observed by Gladman,Duncan &Candy(1991)and Calvo& Sanz-Serna(1992).

We study the long-time behaviour of symplectic methods combined with the following standard step size selection strategy(see e.g.,Hairer,Nprsett&Wanner (1993),Sect.II.4).We assume that an expression $e r r _ { n }$ related to the local error is available for the current step computed with step size $h _ { n }$ (usually obtained with an embedded method).Based on an asymptotic formula $e r r _ { n } \approx C h _ { n } ^ { r }$ (for $h _ { n } \to 0$ and ontherequirement to get an errorclose toa user supplied tolerance Tol,we predict a new step size by

$$
h _ { n e w } = 0 . 8 5 \cdot h _ { n } \Big ( \frac { T o l } { e r r _ { n } } \Big ) ^ { 1 / r } ,
$$

wherea safety factor O.85 is included.We thenapplythe methodwithstep size $h _ { n + 1 } \ = \ h _ { n e w } .$ If for the new step $e r r _ { n + 1 } \ \leq \ T o l$ ,thestep isaccepted and the integration is continued.If $e r r _ { n + 1 } > T o l$ ,it isrejected and recomputed with the step size $h _ { n e w }$ obtained from（1.1）with $n + 1$ instead of $\boldsymbol { n }$ Similar step size strategies areimplemented inmost codes for solving ordinary differential equations.

![](images/89c4b9a7b805c613f09b5494523bcb8db9b5a2028cb879af0a3423484ffb932b.jpg)  
Fig.1.1.Stormer-Verlet scheme applied with fixed step size(middle)orwith the standard step size strategy(below) compared to the exact solution(above);solutions are for the interval $0 \leq t \leq 1 2 0$ (left),for $2 0 0 0 \leq t \leq 2 1 2 0$ (middle),and for $4 0 0 0 \leq t \leq 4 1 2 0$ (right)

Numerical Experiment. We consider the perturbed Kepler problem

$$
\begin{array} { c c c } { { \dot { q } _ { 1 } = p _ { 1 } , } } & { { ~ \dot { p } _ { 1 } = - \displaystyle \frac { q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - \displaystyle \frac { \delta q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 5 / 2 } } } } \\ { { \dot { q } _ { 2 } = p _ { 2 } , } } & { { ~ \dot { p } _ { 2 } = - \displaystyle \frac { q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - \displaystyle \frac { \delta q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 5 / 2 } } } } \end{array}
$$

$\delta = 0 . 0 1 5 )$ with initialvalues

$$
q _ { 1 } ( 0 ) = 1 - e , \quad q _ { 2 } ( 0 ) = 0 , \quad p _ { 1 } ( 0 ) = 0 , \quad p _ { 2 } ( 0 ) = \sqrt { ( 1 + e ) / ( 1 - e ) }
$$

(eccentricity $e = 0 . 6$ ).AsanumericalmethodwetaketheStormer-Verlet scheme (I.1.17)which is symmetric,symplectic,and of order2.The fixed step size implementation isstraightforward.For thevariable step size strategywe take for $e r r _ { n }$ the Euclidean normof thedifference between the Stormer-Verlet solutionand the symplectic Euler solution(which is availablewithout any further functionevaluation). Since $e r r _ { n } = { \cal O } ( h _ { n } ^ { 2 } )$ wetake $r = 2$ in (1.1).

![](images/96dd645b19f619b34a145b7524602d28b49626376587fd7631de76adc029c9f1.jpg)  
Fig.1.2.Study of the error intheHamiltonianand of the global error for theStormer-Verlet scheme.Fixed step size implementation with $h = 1 0 ^ { - 3 }$ variablestep size with $T o l = 1 0 ^ { - 4 }$

The numerical solution in the $\left( q _ { 1 } , q _ { 2 } \right)$ -planeispresented inFig.1.1.Tomake thelong-time behaviour of the two implementationsvisible,we show the numerical solution on threedifferentparts of the integration interval.We have included thenumbers of steps needed for the integration toreach $t = 1 2 0$ ,2120,and4120, respectively.We see that the qualitative behaviour of thevariable step size implementation is not correct,although itis more precise on short intervals.Moreover, thenear-preservation of theHamiltonianis lost (see Fig.1.2） asisthelinear error growth.Apparently,the error in the Hamiltonian behaves like $\left| a - b t \right|$ forthevariable step size implementation,and that for the solution like $\vert c t - d t ^ { 2 } \vert$ (with constants $a , b , c , d$ depending on $T o l$ ).Dueto therelatively large eccentricity of theproblem, thevariable step size implementation needs fewer function evaluations foragiven accuracy ona short timeinterval,but the opposite is true forlong-time integrations.

The aim of the next two sections is to present approaches which permit the use ofvariable step sizes for symmetric or symplectic methods without losing the qualitatively correctlong-time behaviour.

# VIII.2 Time Transformations

A variable step size implementation produces approximations $y _ { n }$ ona (non-equidistant）grid $\left\{ t _ { n } \right\}$ Thesame effectcan beachieved by performingin advance a time transformation $t  \tau$ and by applyingaconstant step size implementation tothetransformed system.If the time transformation is given as the solution ofa diferentialequation,itfollowsfromthecinrule $\begin{array} { r } { \frac { d y } { d \tau } = \frac { d y } { d t } \frac { d t } { d \tau } } \end{array}$ thatthe transformed systemis

$$
y ^ { \prime } = \sigma ( y ) f ( y ) , \qquad t ^ { \prime } = \sigma ( y ) .
$$

Here,prime indicates a derivative with respect to $\tau$ ,and we use the same letter $y$ for the solutions $y ( t )$ of $\dot { y } = f ( y )$ and $y ( \tau )$ of (2.1). If $\sigma ( y ) > 0$ ,the correspondence $t  \tau$ isbijective.

Applyinga numerical method with constant step size $\succeq$ to（2.1）yieldsapproximations $y _ { n } \approx y ( \tau _ { n } ) = y ( t _ { n } )$ ,where $\begin{array} { r } { { \mathrm { \Delta } n } = n \varepsilon } \end{array}$ and

$$
t _ { n + 1 } - t _ { n } = \int _ { n \varepsilon } ^ { ( n + 1 ) \varepsilon } \sigma { \big ( } y ( \tau ) { \big ) } d \tau \approx \varepsilon \sigma ( y _ { n } ) .
$$

Approximations to $t _ { n }$ areobtained by integrating numerically the differential equation $t ^ { \prime } = \sigma ( y )$ togetherwith $y ^ { \prime } = \sigma ( y ) f ( y )$

Inthe context of geometric numerical integration,we are interested in time transformations such that the vector field $\sigma ( y ) f ( y )$ retains geometric features of $f ( y )$

# VIII.2.1 Symplectic Integration

Fora Hamiltonian system $\dot { y } = f ( y ) = J ^ { - 1 } \nabla H ( y )$ it is natural to search for step size functions $\sigma ( y )$ such that(2.1） isagain Hamiltonian.For thiswe have tocheck whether the Jacobian of $\sigma ( y ) \nabla H ( y )$ is symmetric (cf.Integrability Lemma VI.2.7). But this is the case onlyif $\nabla H ( y ) \nabla \sigma ( y ) ^ { T }$ is symmetric,i.e., $\nabla H ( y )$ and $\nabla \sigma ( y )$ are collinear,so that $\begin{array} { r } { \frac { d } { d t } \sigma \big ( y ( t ) \big ) \ = \nabla \sigma \big ( y ( t ) \big ) ^ { T } J \nabla H \big ( y ( t ) \big ) \ = \ 0 , } \end{array}$ Consequently, $\sigma ( y ) = C o n s t$ along solutions of the Hamiltonian systemwhich is what makes this approach unattractive foravariable step size integration.This disappointing fact has beenobserved by Stoffer(1988,1995)and Skeel&Gear(1992).

Themain idea for circumventing this diffculty is the following:suppose we want to integrate the Hamiltonian system with steps of size $h \approx \varepsilon \sigma ( y )$ where $\sigma ( y ) > 0$ isastate-dependent given function and $\varepsilon > 0$ isa small parameter. Instead of multiplying the vector field $f ( y ) = J ^ { - 1 } \nabla H ( y )$ by $\sigma ( y )$ ,we consider the new Hamiltonian

$$
K ( y ) = \sigma ( y ) \Big ( H ( y ) - H _ { 0 } \Big ) ,
$$

where $H _ { 0 } ~ = ~ H ( y _ { 0 } )$ fora fixed initial value $y _ { 0 }$ .Thecorresponding Hamiltonian systemis

$$
y ^ { \prime } = \sigma ( y ) J ^ { - 1 } \nabla H ( y ) + \left( H ( y ) - H _ { 0 } \right) J ^ { - 1 } \nabla \sigma ( y ) .
$$

Compared to (2.1） we have introduced a perturbation,which vanishes along the solution of the Hamiltonian system passing through $y _ { 0 }$ ,butwhich makesthe system Hamiltonian.

Time transformations such as in (2.3)are used in classical mechanics for an analytictreatment of Hamiltonian systems (Levi-Civita(1906,192O),where(2.3）is called the“Darboux-Sundman transformation",see Sundman(1912)).Zare& Szebehely(1975) consider such time transformations for numerical purposes (without takingcareofsymplecticity).Waldvogel&Spirig（1995)applythe transformations proposed byLevi-Civita to Hill'slunar problemand solve the transformed equations bycomposition methods in order to preserve the symplectic structure.The following general procedurewas proposed independently by Hairer(1997)and Reich(1999).

Algorithm2.1.Applyanarbitrarysymplectic one-stepmethod with constant step size $\varepsilon$ totheHamiltoniansystem(2.4),augmented by $t ^ { \prime } = \sigma ( y )$ Thisyields numericalapproximations $( y _ { n } , t _ { n } )$ with $y _ { n } \approx y ( t _ { n } )$ .

Although this algorithmyields numerical approximations on anon-equidistant grid,it canbe considered asa fixed stepsize,symplectic method applied toa differentHamiltonian system.This interpretation allowsone to apply the standard techniques for the study of its long-time behaviour.

A disadvantage of thisalgorithmis that for separable Hamiltonians $H ( p , q ) =$ $T ( p ) + U ( q )$ the transformed Hamiltonian (2.3)is no longer separable.Hence,methodsthat are explicit for separable Hamiltoniansare not explicitin the implementationofAlgorithm2.1.The following examples illustrate that this disadvantage can bepartially overcome for the important caseof Hamiltonian functions

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ^ { - 1 } p + U ( q ) ,
$$

where $M$ is aconstant symmetric matrix.

Example2.2 (Symplectic Eulerwith $\mathbf { \xi } _ { p }$ -Independent Step Size Function).For step size functions $\sigma ( q )$ thesymplectic Euler method,applied with constant step size $\boldsymbol { \mathsf { E } }$ to(2.4）,reads

$$
\begin{array} { r l } & { p _ { n + 1 } = p _ { n } - \varepsilon \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \varepsilon \Big ( \frac { 1 } { 2 } p _ { n + 1 } ^ { T } M ^ { - 1 } p _ { n + 1 } + U ( q _ { n } ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) } \\ & { q _ { n + 1 } = q _ { n } + \varepsilon \sigma ( q _ { n } ) M ^ { - 1 } p _ { n + 1 } } \end{array}
$$

and yieldsan approximation at $t _ { n + 1 } = t _ { n } + \varepsilon \sigma ( q _ { n } ) .$ The first equation is non-$p _ { n + 1 }$ $\beta : = \| p _ { n + 1 } \| _ { M } ^ { 2 } : =$ $p _ { n + 1 } ^ { T } M ^ { - 1 } p _ { n + 1 }$

$$
\beta = \Big \| p _ { n } - \varepsilon \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \varepsilon \Big ( \frac { \beta } { 2 } + U ( q _ { n } ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) \Big \| _ { M } ^ { 2 }
$$

which canbe solved directly.Thenumerical solution $( p _ { n + 1 } , q _ { n + 1 } )$ is then given explicitly.

Choices of Step Size Functions. Sometimes suitable functions $\sigma ( p , q )$ areknown a priori.For example,for the two-body problem one can take $\sigma ( p , q ) = \| q \| ^ { \alpha } ,$ e.g., $\alpha = 2$ ,or $\alpha = 3 / 2$ topreserve the scaling invariance（Budd &Piggott 2Oo3）,so that smaller step sizes are taken when the two bodies are close.

Aninteresting choice,which does not require any a priori knowledge of the solution,is $\sigma ( y ) = \| f ( y ) \| ^ { - 1 } .$ The solution of (2.1) then satisfies $\| y ^ { \prime } ( \tau ) \| = 1$ (arclength parameterization）andwe get approximations $y _ { n }$ thatare nearly equidistant inthephase space.Such time transformations have been proposed by McLeod& Sanz-Serna（1982) for graphical reasonsandby Huang&Leimkuhler（1997).Fora Hamiltonian system with $H ( p , q )$ givenby(2.5),itis thusnatural to consider

$$
\sigma ( p , q ) = { \left( { \frac { 1 } { 2 } } p ^ { T } M ^ { - 1 } p + \nabla U ( q ) ^ { T } M ^ { - 1 } \nabla U ( q ) \right) } ^ { - 1 / 2 } .
$$

Wehave chosen this particular norm,because it leaves the expression (2.6) invariant with respect to linear coordinate changes $q \mapsto A q$ （implying $p \mapsto A ^ { - T } p$ .Exploiting the fact that the Hamiltonian(2.5)is constant along solutions,the step size function(2.6) can be replaced by the $\boldsymbol { p }$ -independent function

$$
\sigma ( { q } ) = \Big ( \big ( H _ { 0 } - U ( { q } ) \big ) + \nabla U ( { q } ) ^ { T } M ^ { - 1 } \nabla U ( { q } ) \Big ) ^ { - 1 / 2 } .
$$

Theuse of(2.6) and (2.7） gives nearly identical results,but (2.7)is easier to implement.Ifweare interestedin an output that isapproximatively equidistant in the $q$ -space,we cantake

$$
\sigma ( q ) = { \left( H _ { 0 } - U ( q ) \right) } ^ { - 1 / 2 } .
$$

Example2.3 (Stormer-Verlet Schemewith $\boldsymbol { p }$ -Independent Step Size Function). Fora step size function $\sigma ( q )$ theStormer-Verlet scheme gives

$$
\begin{array} { r l } & { p _ { n + 1 / 2 } = p _ { n } - \frac { \varepsilon } { 2 } \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \frac { \varepsilon } { 2 } \Big ( H \big ( p _ { n + 1 / 2 } , q _ { n } \big ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) } \\ & { \quad q _ { n + 1 } = q _ { n } + \frac { \varepsilon } { 2 } \big ( \sigma ( q _ { n } ) + \sigma ( q _ { n + 1 } ) \big ) M ^ { - 1 } p _ { n + 1 / 2 } } \\ & { p _ { n + 1 } = p _ { n + 1 / 2 } - \frac { \varepsilon } { 2 } \sigma ( q _ { n + 1 } ) \nabla U ( q _ { n + 1 } ) } \\ & { \qquad \quad - \frac { \varepsilon } { 2 } \Big ( H \big ( p _ { n + 1 / 2 } , q _ { n + 1 } \big ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n + 1 } ) , } \end{array}
$$

Thefirst equation isessentially the same as that for the symplectic Eulermethod, andit can be solved for $_ { p _ { n + 1 / 2 } }$ as explained in Example 2.2.The second equation isimplicit in $q _ { n + 1 }$ ,but itis suficient to solve thescalar equation

$$
\gamma = \sigma \Big ( q _ { n } + \frac { \varepsilon } { 2 } \big ( \sigma ( q _ { n } ) + \gamma \big ) M ^ { - 1 } p _ { n + 1 / 2 } \Big )
$$

for $\gamma = \sigma ( q _ { n + 1 } ) .$ Newton iterations can be effciently applied,because $\nabla \sigma ( q )$ is available already.Thelastequation (for $p _ { n + 1 }$ )is explicit.This variable step size Stormer-Verlet scheme gives approximations at $t _ { n }$ ,where

$$
t _ { n + 1 } = t _ { n } + \frac { \varepsilon } { 2 } \bigl ( \sigma ( q _ { n } ) + \sigma ( q _ { n + 1 } ) \bigr ) .
$$

![](images/cafd874ef84dfac8555f905ad8f1f11a86f25a90b5bb7de9f84e8bdccf66994b.jpg)  
Fig.2.1.Various step size strategies forthe Stormer-Verlet scheme(Example2.3)applied to theperturbedKeplerproblem(1.2）on the interval [0,10](approximately two periods)

In Fig.2.1 we illustrate how the different step size functions influence the position of the output points.Weapply the Stormer-Verlet method of Example2.3 to the perturbed Keplerproblem(1.2)with initial values,perturbation parameter,and eccentricity asin Sect.VIII.1.As step size functions we use(2.7),(2.8),and constant step size $\sigma ( q ) \equiv 1$ Forall three choices of $\sigma ( q )$ wehave adjusted theparameter $\varepsilon$ in such away that themaximal error in the Hamiltonianis close to O.O1.The step size strategy(2.7)isapparently themost efficient one.Forthisstrategy,we observe that the output points in the $q$ -plane concentrate in regionswhere thevelocity is large, while the constant step size implementation shows the opposite behaviour.

# VIII.2.2Reversible Integration

For $\rho$ -reversibledifferential equations $\dot { y } = f ( y )$ ,i.e., $f ( \rho y ) = - \rho f ( y )$ for all $_ y$ ,the time transformed problem (2.1) remains $\rho$ -reversibleif

$$
\sigma ( \rho y ) = \sigma ( y ) .
$$

Thiscondition is not very restrictiveand is satisfiedby many important time transformations.Inparticular,(2.11） holds for thearc lengthparameterization $\sigma ( y ) =$ $\| f ( y ) \| ^ { - 1 }$ if $\rho$ is orthogonal.Consequently,it makes sense to apply symmetric,reversible numerical methods with constant step size $\varepsilon$ directly to the system (2.1).

However,similar to the symplectic integration of Sect.VII.2.1,there isa serious disadvantage.For separable differential equations (i.e.,problems that can be splitas ${ \dot { p } } = f _ { 1 } ( q )$ , $\dot { q } = f _ { 2 } ( p )$ ）and for non-constant $\sigma ( p , q )$ the transformed system(2.1) isnolonger separable.Hence,methods that are explicit for separable problemsare notnecessarily explicit for(2.1）.

Example2.4(Adaptive Stormer-VerletMethod).We considera Hamiltonian systemwithseparable Hamiltonian(2.5),andweapply the Stormer-Verlet scheme to(2.1).Thisyields(Huang&Leimkuhler1997)

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 / 2 } = p _ { n } - \displaystyle \frac { \varepsilon } { 2 } s _ { n } \nabla U ( q _ { n } ) } } \\ { { } } & { { } } & { { q _ { n + 1 } = q _ { n } + \displaystyle \frac { \varepsilon } { 2 } \bigl ( s _ { n } + s _ { n + 1 } \bigr ) M ^ { - 1 } p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } = p _ { n + 1 / 2 } - \displaystyle \frac { \varepsilon } { 2 } s _ { n + 1 } \nabla U ( q _ { n + 1 } ) , } } \end{array}
$$

where $s _ { n } = \sigma ( p _ { n + 1 / 2 } , q _ { n } )$ and $s _ { n + 1 } = \sigma ( p _ { n + 1 / 2 } , q _ { n + 1 } )$ (notice that the $s _ { n + 1 }$ of thecurrent step is not the same as the $s _ { n }$ of the subsequent step,if $\sigma ( p , q )$ depends on $p$ .Thevalues $( p _ { n + 1 } , q _ { n + 1 } )$ are approximations to the solutionat $t _ { n }$ ,where

$$
t _ { n + 1 } = t _ { n } + \frac { \varepsilon } { 2 } \big ( s _ { n } + s _ { n + 1 } \big ) .
$$

Fora $p$ -independent step size function $s$ ,method (2.12) corresponds to that of Example2.3,where the terms involving $\nabla \sigma ( q )$ areremoved.The implicitness of(2.12) iscomparable to that of the method of Example2.3.Completely explicit variantsof this method will be discussed in the next section.

We conclude this section with a brief comparison of the variable step size Stormer-Verletmethods of Examples2.3 and 2.4.Method(2.12) is easier to implement and more efficient when the step size function $\sigma ( p , q )$ is expensive to evaluate.Ina few numerical comparisons we observed,however,that the errorin the Hamiltonian and in the solution isin general larger for method(2.12),and that themethod（2.9） becomes competitive when $\sigma ( p , q )$ is $p$ -independentand easyto evaluate.A similar observationin favour of method(2.9) has beenmadeby Calvo, L6pez-Marcos& Sanz-Serna(1998).

# VIII.3 Structure-Preserving Step Size Control

Thedisappointing long-time behaviour in Fig.1.1 of thevariable step sizeimplementationof theStormer-Verlet scheme isdue to lack of reversibility.Indeed,fora $\rho$ -reversible differential equationthe step size $h _ { n + 1 / 2 }$ taken for stepping from $y _ { n }$ to $y _ { n + 1 }$ should be the same as thatwhen stepping from $\rho y _ { n + 1 }$ to $\rho y _ { n }$ (cf.Fig.V.1.1). The strategy of Sect.VII.1,for which the step sizedepends on information of the preceding step,cannot guarantee such a property.

# VIII.3.1Proportional,Reversible Controllrs

Following a suggestion of Stoffer (1988）we consider step sizes depending only oninformation of the present step,i.e.,beingproportional to some function of the actual state.This leads tothealgorithm

$$
y _ { n + 1 } = \varPhi _ { h _ { n + 1 / 2 } } ( y _ { n } ) , \qquad h _ { n + 1 / 2 } = \varepsilon s ( y _ { n } , \varepsilon ) ,
$$

where $\varPhi _ { h } ( y )$ isa one-step method for $\dot { y } = f ( y )$ ,and $\boldsymbol { \varepsilon }$ isasmall parameter.For theoretical investigations itis useful to consider themapping

$$
\varPsi _ { \varepsilon } ( y ) : = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) .
$$

This isa one-stepdiscretization,consistent with $y ^ { \prime } = s ( y , 0 ) f ( y )$ ,andapplied with constant step size $\boldsymbol { \varepsilon }$ .Consequently,all results concerning the long-time integration

with constant steps (e.g.,backward error analysis of Chap.IX),and the definitions ofsymmetryandreversibilitycanbeextendedinastraightforwardway.

Symmetry.Wecall the algorithm(3.1） symmetric,if $\varPsi _ { \varepsilon } ( y )$ issymmetric,i.e., $\bar { \psi } _ { \varepsilon } = \bar { \psi } _ { - \varepsilon } ^ { - 1 } .$ In the case of a symmetric $\phi _ { h }$ this is equivalent to

$$
\begin{array} { r } { s ( \widehat { y } , - \varepsilon ) = s ( y , \varepsilon ) \qquad \mathrm { w i t h } \qquad \widehat { y } = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) . } \end{array}
$$

Reversibility.Thealgorithm(3.1）is called $\rho$ -reversibleif,whenapplied toa $\rho$ reversibledifferential equation, $\varPsi _ { \varepsilon } ( y )$ is $\rho$ -reversible,i.e., $\rho \circ \varPsi _ { \varepsilon } = \varPsi _ { \varepsilon } ^ { - 1 } \circ \rho$ (cf. Definition V.1.2).If the method $\phi _ { h }$ is $\rho$ -reversible then this is equivalent to

$$
\begin{array} { r } { s ( \rho ^ { - 1 } \widehat { y } , \varepsilon ) = s ( y , \varepsilon ) \qquad \mathrm { w i t h } \qquad \widehat { y } = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) . } \end{array}
$$

Example 3.1.Aiming at step sizes $h \approx \varepsilon \sigma ( y )$ (cf.(2.2)）,Hut,Makino&McMillan (1995)propose the use of $\begin{array} { r } { s ( y , \varepsilon ) = \frac { 1 } { 2 } \big ( \sigma ( y ) + \sigma ( \widehat { y } ) \big ) } \end{array}$ where,as in Sect.VIII.2, $\sigma ( y )$ issome function that usesana priori knowledge of the solution of thedifferential equation.Notice that,becauseof $\widehat { y } = \phi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ ,thevalue of $s ( y , \varepsilon )$ isdefined byanimplicit relation.Condition(3.3）is satisfied whenever $\varPhi _ { h } ( y )$ issymmetric, and(3.4）is satisfiedwhenever $\varPhi _ { h } ( y )$ is $\rho$ -reversibleand $\sigma ( \rho y ) = \sigma ( y )$ holds.Fora proof of these statements one shows that $s ( \widehat { y } , - \varepsilon )$ and $s ( y , \varepsilon )$ (resp. $s ( \rho ^ { - 1 } \widehat { y } , \varepsilon )$ and $s ( y , \varepsilon ) )$ are solution of the same nonlinear equation.

How can we find suitable step size functions $s ( y , \varepsilon )$ which satisfy all these properties,and whichdo not requireanyapriori knowledge of thesolution？Inaremarkablepublication,Stoffer（1995)gives thekeyto theanswerof thisquestion. Hesimply proposes to choose the step size $h$ in such a way that the local error estimatesatisfies $e r r = T o l$ （in contrast to $e r r \le T o l$ for the standard strategy).Let us explain this idea in some more detail forRunge-Kutta methods.

Example3.2 (Symmetric,Variable Step SizeRunge-Kutta Methods).For the numerical solution of $\dot { y } = f ( y )$ we consider Runge-Kutta methods

$$
Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ) , \qquad y _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } ) ,
$$

with coefficients satisfying $a _ { s + 1 - i , s + 1 - j } + a _ { i j } = b _ { j }$ for all $i , j$ Such methods are symmetric and reversible (cf.TheoremV.2.3).A common approach for step size controlistosideranembededeod $\begin{array} { r } { \widehat { y } _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } f ( Y _ { i } ) } \end{array}$ (which has the same internal stages $Y _ { i }$ ）andtotake thedifference $y _ { n + 1 } - { \hat { y } } _ { n + 1 } ,$ i.e.,

$$
D ( y _ { n } , h ) = h \sum _ { i = 1 } ^ { s } e _ { i } f ( Y _ { i } )
$$

with $e _ { i } = b _ { i } - { \widehat { b } } _ { i }$ as indicatorofthelocal error.Formethods where $Y _ { i } \approx y ( t _ { n } + c _ { i } h )$ (e.g.,collocation or discontinuous collocation） one usually computes the coefficients $e _ { i }$ fromanontrivial solution of the homogeneous linear system

$$
\sum _ { i = 1 } ^ { s } e _ { i } c _ { i } ^ { k - 1 } = \bar { 0 } \qquad \mathrm { f o r } \quad k = 1 , \ldots , s - \bar { 1 } .
$$

Thisyields $D ( y _ { n } , h ) = { \mathcal { O } } ( h ^ { r } )$ with $r$ close to $s$ .According to the suggestion of Stoffer(1995)we determine the step size $h _ { n + 1 / 2 }$ such that

$$
\| D ( y _ { n } , h _ { n + 1 / 2 } ) \| = T o l .
$$

A Taylor expansion around $h = 0$ shows that $D ( y , h ) = d _ { r } ( y ) h ^ { r } + { \mathcal O } ( h ^ { r + 1 } )$ with some $r \geq 1$ We assume $\lVert d _ { r } ( y ) \rVert \neq 0$ and we put $\varepsilon = T o l ^ { 1 / r }$ ,sothat $h _ { n + 1 / 2 }$ from (3.8)can be expressed by asmooth function $s ( y , \varepsilon )$ as (3.1).

Tosatisfythe symmetryrelation (3.3)we determine the $e _ { i }$ such that

$$
e _ { s + 1 - i } = e _ { i } \quad \mathrm { f o r ~ a l l ~ } i \qquad \mathrm { o r } \qquad e _ { s + 1 - i } = - e _ { i } \quad \mathrm { f o r ~ a l l ~ } i
$$

(Hairer& Stoffer 1997).If the Runge-Kutta method is symmetric,this then implies

$$
| | D ( y _ { n } , h ) | | = | | D ( y _ { n + 1 } , - h ) | | \qquad \mathrm { w i t h } \qquad y _ { n + 1 } = \varPhi _ { h } ( y _ { n } ) .
$$

This follows from the fact that the internal stage vectors $Y _ { i }$ of the step from $y _ { n }$ to $y _ { n + 1 }$ and the stage vectors $Y _ { i }$ of the step from $y _ { n + 1 }$ to $y _ { n }$ (negative step size $- h$ ） arerelated by $Y _ { i } = Y _ { s + 1 - i } .$ The step sizedetermined by(3.8) is thus the same for both steps and,consequently,condition(3.3)holds.

Thereversibilityrequirement(3.4)isaconsequence of

$$
| | D ( y _ { n } , h ) | | = | | D ( \rho ^ { - 1 } y _ { n + 1 } , h ) | | \qquad \mathrm { w i t h } \qquad y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )
$$

which is satisfied for orthogonal mappings $\rho$ (i.e., $\rho ^ { T } \rho = I$ ).This is seenas follows: applying $\phi _ { h }$ to $\rho ^ { - 1 } y _ { n + 1 }$ gives $\rho ^ { - 1 } y _ { n }$ and theinternal stagesare $Y _ { i } = \rho ^ { - 1 } Y _ { s + 1 - i }$ Hence,we have from (3.9) that $D ( \rho ^ { - 1 } y _ { n + 1 } , h ) = \pm \rho ^ { - 1 } D ( y _ { n } , h )$ ,and (3.11） follows from the orthogonality of $\rho$

A simple special case is the trapezoidal rule

$$
y _ { n + 1 } = y _ { n } + { \frac { h _ { n \mp 1 / 2 } } { 2 } } { \Big ( } f ( y _ { n } ) + f ( y _ { n + 1 } ) { \Big ) }
$$

combined with

$$
D ( y _ { n } , h ) = { \frac { h } { 2 } } { \Big ( } f ( y _ { n + 1 } ) - f ( y _ { n } ) { \Big ) } .
$$

Thescalar nonlinear equation （3.8）for $h _ { n + 1 / 2 }$ can be solved in tandem with the nonlinear system (3.12).

Example 3.3 (Symmetric, Variable Step Size Stormer-Verlet Scheme).The strategy of Example 3.2can beextended ina straightforward waytopartitioned Runge-Kutta methods.For example,for the second order symmetric Stormer-Verlet scheme (I.1.17),applied to the problem ${ \dot { q } } = p$ , $\dot { p } = - \nabla U ( q ) .$ wecan take

$$
D ( p _ { n } , q _ { n , v } h ) = \frac { h } { 2 } \left( { { \nabla U ( q _ { n + 1 } ) - \nabla U ( q _ { n } ) } } \right)
$$

![](images/adaad9b01a2871634b8381e9d0616a9ebdac66ae71c15d998aaaa4a6a396dd4b.jpg)  
Fig.3.1.Stormer-Verlet scheme appliedwith the symmetricadaptive step size strategy of Example3.3 $T o l = 0 . 0 1 $ the three pictures have the same meaningasin Fig.1.1

aserror indicator.The first component is just thedifference of the Stormer-Verlet solution and the numerical approximation obtained by the symplectic Eulermethod. The second component is a symmetrized version of it.

We apply this method with $h _ { n + 1 / 2 }$ determined by(3.8）and $T o l = 0 . 0 1$ tothe perturbed Keplerproblem（1.2) with initialvaluesas inFig.1.1.Theresult is given inFig.3.1.We identifyacorrect qualitative behaviour(compared to thewrongbehaviour for the standard step size strategyin Fig.1.1).It should bementioned that thework for solving the scalar equation (3.8) for $h _ { n + 1 / 2 }$ is not negligible,because theStormer-Verletschemeis explicit.Solving this equation iteratively,every iterationrequires one force evaluation $\nabla U ( q )$ .An efficient solver for this scalar nonlinearequation should be used.

ATwo-Step Proportional Controller.With theaim of obtaining acompletely explicitintegrator,Huang&Leimkuhler（1997）propose theuse of two-term recurrencerelations for the step size sequence,see also Holder,Leimkuhler&Reich (2001).Instead of usingarelation between $h _ { n + 1 / 2 }$ , $y _ { n }$ and $y _ { n + 1 }$ (cf.Example3.1) whichisnecessarilyimplicit,itissuggestedto usea symmetric relation.between $h _ { n - 1 / 2 }$ , $h _ { n + 1 / 2 }$ ,and $y _ { n }$ ,which then isexplicit.In particular,with thenotation $h _ { n + 1 / 2 } = \varepsilon s _ { n + 1 / 2 }$ ,it is proposed touse the two-term recurrence relation

$$
\frac { 1 } { s _ { n + 1 / 2 } } + \frac { 1 } { s _ { n - 1 / 2 } } = \frac { 2 } { \sigma ( y _ { n } ) } ,
$$

starting with $s _ { 1 / 2 } ~ = ~ \sigma ( y _ { 0 } )$ .Incombination with the Stormer-Verlet method for separableHamiltonians,thisalgorithm iscompletely explicit,and the authors report anexcellent performance for realistic problems.

Arigorous analysis ofthe long-timebehaviourof thisvariablestep size Stormer-Verletmethod ismuch moredifficult.Theresultsof Chapters IX and XI cannot be applied,because it is nota one-step mapping $y _ { n } \mapsto y _ { n + 1 }$ Theanalysis ofCirilli, Hairer&Leimkuhler（1999)shows that,similartoweaklystablemultistepmethods (Chap.XV),the numerical solution and the step size sequence contain oscillatory terms.Although these oscillations are usually very small (and hardlyvisible),it seems difcult to get rigorous estimates for them.

# VIII.3.2 Integrating,Reversible Controllers

Allvariable step size approaches of this chapter are based on some time transformation $t  \tau$ given by $\begin{array} { r } { \frac { d t } { d \tau } = \sigma ( y ) } \end{array}$ sothatthedrentialuation,xpresinte newtimevariable $\tau$ ,becomes

$$
y ^ { \prime } = { \frac { 1 } { z } } f ( y ) , \qquad z \sigma ( y ) = 1 .
$$

In Sect.VIII.2 we insert $z ^ { - 1 } = \sigma ( y )$ into the differential equation and apply anumerical method to $y ^ { \prime } = \sigma ( y ) f ( y ) .$ InSect.VIII.3.1we first discretizethe algebraic relation $z \sigma ( y ) = 1$ expressing $z _ { n + 1 / 2 }$ in terms of $y _ { n }$ and $y _ { n + 1 }$ ,and then apply a one-stepmethod to the differential equation in (3.14) assuming $z = z _ { n + 1 / 2 }$ being constant.

Inthepresent section we first differentiate the algebraic relation of (3.14)with respect to $\tau$ Thisyieldsby Leibniz'rule ${ z } ^ { \prime } { \sigma } ( y ) + { z } \nabla { \sigma } ( y ) ^ { T } y ^ { \prime } = 0$ sothat

$$
\begin{array} { r } { \boldsymbol { z } ^ { t } = G ( \boldsymbol { y } ) \qquad \mathrm { w i t h } \qquad G ( \boldsymbol { y } ) = - \displaystyle \frac { 1 } { \sigma ( \boldsymbol { y } ) } \nabla \sigma ( \boldsymbol { y } ) ^ { T } \boldsymbol { f } ( \boldsymbol { y } ) . } \end{array}
$$

Theidea of differentiating the constraint in(3.14） has been raised in Huang& Leimkuhler(1997),but soon abandoned in favourof thecontroller(3.13).The subsequent algorithm togetherwith itstheoretical justification iselaborated in Hairer &Soderlind(2oo4).The idea is to discretize first the differential equation in (3.15) andthen toapplya one-stepmethod totheproblem(3.14）with constant $z$ .The proposed algorithm is thus

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n - 1 / 2 } + \varepsilon G ( y _ { n } ) } } \\ { { y _ { n + 1 } } } & { { = } } & { { \Phi _ { \varepsilon / z _ { n + 1 / 2 } } ( y _ { n } ) } } \end{array}
$$

with $z _ { 1 / 2 } = z _ { 0 } + \varepsilon G ( y _ { 0 } ) / 2$ and $z _ { 0 } = 1 / \sigma ( y _ { 0 } ) .$ Thisalgorithm is explicit whenever the underlying one-step method $\varPhi _ { h } ( y )$ isexplicit.Itis called integrating controller, because the step size density is obtained by summingupsmall quantities.

Foratheoreticalanalysisitisconvenienttointroduce $z _ { n } = ( z _ { n + 1 / 2 } + z _ { n - 1 / 2 } ) / 2$ and towrite(3.16)asa one-step method for the augmented system

$$
y ^ { \prime } = { \frac { 1 } { z } } f ( y ) , \qquad z ^ { \prime } = G ( y ) .
$$

Notice that $I ( y , z ) = z \sigma ( y )$ isafirst integral ofthis system.

Algorithm3.4.Let $\varPhi _ { h } ( y )$ beaone-step method for $\dot { y } = f ( y )$ ， $y ( 0 ) = y _ { 0 }$ With $G ( y )$ given by(3.15）, $z _ { 0 } = 1 / \sigma ( y _ { 0 } )$ andconstant $\varepsilon$ welet

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n } + \varepsilon G ( y _ { n } ) / 2 } } \\ { { y _ { n + 1 } } } & { { = } } & { { \varPhi _ { \varepsilon / z _ { n + 1 / 2 } } ( y _ { n } ) } } \\ { { z _ { n + 1 } } } & { { = } } & { { z _ { n + 1 / 2 } + \varepsilon G ( y _ { n + 1 } ) / 2 . } } \end{array}
$$

Thevalues $y _ { n }$ approximate $y ( t _ { n } )$ where $t _ { n + 1 } = t _ { n } + \varepsilon / z _ { n + 1 / 2 }$

Thisalgorithm has an interestinginterpretation as Strang splitting for the solutionof(3.17):itapproximates the flow of $z ^ { \prime } = G ( y )$ with fixed $_ y$ overahalf-step $\varepsilon / 2$ ;thenappliesthemethod $\boldsymbol { \varPhi _ { \varepsilon } }$ to $y ^ { \prime } = f ( y ) / z$ with fixed $z$ ;finally,itcomputesa second half-step of $z ^ { \prime } = G ( y )$ with fixed $_ y$ .

With the notation

$$
{ \widehat { \boldsymbol { \phi } } } _ { \varepsilon } : { \left( \begin{array} { l } { y _ { n } } \\ { z _ { n } } \end{array} \right) } \mapsto { \left( \begin{array} { l } { y _ { n + 1 } } \\ { z _ { n + 1 } } \end{array} \right) } \qquad { \mathrm { a n d } } \qquad { \widehat { \boldsymbol { \rho } } } = { \left( \begin{array} { l l } { \rho } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } .
$$

theAlgorithm 3.4 has thefollowingproperties：

$\hat { \varPhi } _ { \varepsilon }$ is symmetric whenever $\phi _ { h }$ is symmetric;   
$\hat { \varPhi } _ { \varepsilon }$ is reversible with respect to $\hat { \rho }$ whenever $\phi _ { h }$ is reversible with respect to $\rho$ and $G ( \rho y ) = - G ( y )$ (this is a consequence of $\sigma ( \rho y ) = \sigma ( y ) )$

Theseproperties imply that standard techniques for constant step size implementations can be applied to $\widehat { \varPhi } _ { \varepsilon }$ ,and thus yield insight into the variable step size algorithmof this section.Itwill be shown in Chap.XI that when applied to integrable reversible systems there isno drift in the action variablesand the global error grows onlylinearlywith time.Moreover,the firstintegral $I ( y , z ) = z \sigma ( y )$ ofthe system (3.17)isalso well preserved(without drift) for such problems.

Example3.5(Variable Step Size Stormer-Verlet method).Considera Hamiltoniansystem with separable Hamiltonian $H ( p , q ) \ = \ T ( p ) + U ( q )$ Using the Stormer-Verletmethodas basicmethod the abovealgorithm becomes(starting with $z _ { 0 } = 1 / \sigma ( y _ { 0 } )$ and $z _ { 1 / 2 } = z _ { 0 } + \varepsilon G ( p _ { 0 } , q _ { 0 } ) / 2 )$

$$
\begin{array} { r c l } { z _ { n + 1 / 2 } } & { = } & { z _ { n - 1 / 2 } + \varepsilon G ( p _ { n } , q _ { n } ) } \\ { p _ { n + 1 / 2 } } & { = } & { p _ { n } - \varepsilon \nabla U ( q _ { n } ) / ( 2 z _ { n + 1 / 2 } ) } \\ { q _ { n + 1 } } & { = } & { q _ { n } + \varepsilon \nabla T ( p _ { n + 1 / 2 } ) / z _ { n + 1 / 2 } } \\ { p _ { n + 1 } } & { = } & { p _ { n + 1 / 2 } - \varepsilon \nabla U ( q _ { n + 1 } ) / ( 2 z _ { n + 1 / 2 } ) . } \end{array}
$$

Thismethod isexplicit,symmetric and reversible as longas $G \rho ~ = ~ - G$ ,and computes approximations on a non-equidistant grid $\left\{ { { t } _ { n } } \right\}$ givenby $t _ { n + 1 } ~ = ~ t _ { n } ~ +$ $\varepsilon / z _ { n + 1 / 2 }$

Letusapply thismethod to the perturbed Kepler problem withdata and initial values as in the beginning of this chapter.Further,we select $\sigma ( q ) = ( q ^ { T } q ) ^ { \alpha / 2 }$ with $\alpha = 3 / 2$ ,sothat the control function(3.15) becomes

$$
G ( p , q ) = - \alpha p ^ { T } q / q ^ { T } q .
$$

Figure 3.2 shows the error in the Hamiltonian along the numerical solution as well asthe global error in the solution (fictive step size $\varepsilon = 0 . 0 2$ Theerror in the Hamiltonian is proportional to $\varepsilon ^ { 2 }$ without drift,and the global error grows linearly with time (in double logarithmic scale a linear growth corresponds toa line with slope one;such lines aredrawn in grey).This isqualitatively the same behaviouras observed in constant step size implementations of symplectic methods.

![](images/b0eb4b7f2be58835ecb01a644b5c79fb06633a4c3cabd5433f899e3a322c086f.jpg)  
Fig.3.2.Numerical Hamiltonian and global errorasa function of time

![](images/645b19732c706e21563cf158f98e29f3dde4ce420909b2dc3b4fd74e7af7e334.jpg)  
Fig.3.3.Step sizes of the variable step size Stormer-Verlet method asa function of time,andthe control error $z _ { n } \sigma ( q _ { n } ) - z _ { 0 } \sigma ( q _ { 0 } )$ （grey curve）

Figure 3.3 shows the selected step sizes $h _ { n + 1 / 2 } = \varepsilon / z _ { n + 1 / 2 }$ asa function of time,and the control error $z _ { n } \sigma ( q _ { n } ) - z _ { 0 } \sigma ( q _ { 0 } )$ in grey.Since its deviation from the constant value $z _ { 0 } \sigma ( q _ { 0 } ) = 1$ issmall without any drift,the step density remains close to $1 / \sigma ( q )$ .Foran explanation of this excellent long-time behaviourwe refer to Sect.XI.3.

# VIII.4 Multiple Time Stepping

Acompletely different approachto variable step sizeswillbe described in this section.We are interested in situationswhere:

·many solution components of thedifferential equation vary slowly and only a few components have fast dynamics; or   
computationally expensive parts of the right-hand side do not contribute much to thedynamics of the solution.

Inthe first case itis tempting to use large step sizes for the slow components and small step sizes for the fast ones.Such integrators,called multirate methods,were first formulatedbyRice(196O)and Gear&Wells（1984).Theywere furtherdevelopedby Gunther&Rentrop(1993)inview ofapplications inelectriccircuit simulation,and by Engstler&Lubich（1997)with applicationsinastrophysics.Symmetric multirate methodsare obtained from theapproachesdescribed belowand are speciallyconstructed byLeimkuhler&Reich(2001).

The second case suggests the use of methods that evaluate the expensive part of thevector field less often than therest.Thisapproach iscalled multiple time stepping.Itwasoriginallyproposed forastronomyby Hayli（1967）and hasbecome verypopularinmoleculardynamics simulations(Streett,Tildesley& Saville 1978, Grubmuller,Heller,Windemuth&Schulten1991,Tuckerman,Berne&Martyna 1992).As noticed by Biesiadecki& Skeel (1993),one approach to such methods is within the framework of splitting and composition methods,which yields symmetricand symplectic methods.A second family of symmetric multiple time stepping methods results from the concept of using averaged force evaluations.

# VIII.4.1 Fast-Slow Splitting: the Impulse Method

Consideradifferential equation

$$
\dot { y } = f ( y ) , \qquad f ( y ) = f ^ { [ \mathrm { s l o w } ] } ( y ) + f ^ { [ \mathrm { f a s t } ] } ( y ) ,
$$

where the vector field is split into summands contributing to slow and fast dynamics,respectivelyndwhere $f ^ { \mathrm { [ s l o w ] } } ( y )$ ismoreexpensive toevaluate than $f ^ { \mathrm { { ( f a s t ) } } } ( y )$ . Multiratemethodscanoftenbecastintothisframework bycollectingin $f ^ { \mathrm { [ s l o w ] } } ( y )$ those components of $f ( y )$ which produce slow dynamics and in $f ^ { \mathrm { [ f a s t ] } } ( y )$ theremaining components.

Algorithm4.1.Foragiven $N \geq 1$ andfor thedifferentialequation(4.1) amultiple timesteppingmethodisobtainedfrom

$$
\big ( \boldsymbol { \varPhi } _ { h / 2 } ^ { [ \mathrm { s l o w } ] } \big ) ^ { * } \circ \big ( \boldsymbol { \varPhi } _ { h / N } ^ { [ \mathrm { f a s t } ] } \big ) ^ { N } \circ \boldsymbol { \varPhi } _ { h / 2 } ^ { [ \mathrm { s l o w } ] } ,
$$

whereslow] wher andfast aree $\dot { y } = f ^ { \left[ \mathrm { s l o w } \right] } ( y )$ ${ \dot { y } } = f ^ { \left[ \mathrm { f a s t } \right] } \left( y \right)$

ThemethodofAlgorithm4.1isalready stated insymmetrizedform（ $\boldsymbol { \varPhi } _ { h } ^ { * }$ denotes theadjoint of $\phi _ { h }$ ).Itisoftencalledtheimpulsemethod,because theslowpart $f ^ { \mathrm { [ s l o w ] } }$ ofthevector fieldisused-impulse-like-only at the beginningand at the end of the step,whereas the many small substepsin between are concerned solely through integrating the fastsystem $\dot { y } = f ^ { \mathrm { [ f a s t ] } } ( y )$ .

Lemma 4.2. Let $\bar { \Phi } _ { h } ^ { \lfloor s \log \rfloor }$ beanarbitrarymethodoforderl,and $\varPhi _ { h } ^ { [ \mathrm { f a s t } ] }$ asymmetric method oforder2.Then,themultipletime steppingalgorithm(4.2）issymmetric and of order2.

f $f ^ { \mathrm { [ s l o w ] } } ( y )$ and $f ^ { \mathrm { [ f a s t ] } } ( y )$ are Hamiltonian and if $\varPhi _ { h } ^ { [ \mathrm { s l o w } ] }$ and lfast] areboth symplectic,then themultiple time steppingmethodisalsosymplectic.

Proof.Due to the interpretation of multiple time stepping as composition methods the proof of these statements is obvious. □

Theorder statement ofLemma4.2isvalid for $h  0$ ,but should be taken with caution if the product of the step size $h$ witha Lipschitz constant of the problem isnotsmall (see Chap.XII fora detailedanalysis):itis not stated,and is not true in general for large $N$ ,thatif $h$ and $h / N$ are the step sizes needed to integrate the slowand fast system,respectively,withanerror bounded by $\succeq$ ,then the error of the combined scheme is $\mathcal { O } ( \varepsilon )$

Themost important application of multiple time stepping is in Hamiltonian systemswithaseparableHamiltonian

$$
H ( p , q ) = T ( p ) + U ( q ) , \qquad U ( q ) = U ^ { [ \mathrm { s l o w } ] } ( q ) + U ^ { [ \mathrm { f a s t } ] } ( q ) .
$$

Ifwe let the fast vector field correspond to $T ( p ) + U ^ { [ \mathrm { f a s t } ] } ( q )$ and the slow vector field to $U ^ { \left[ \mathrm { s l o w } \right] } \left( q \right)$ ,andifweapplytheStormer-Verletmethodandexactintegration, respectively,Algorithm4.1reads

$$
\varphi _ { h / 2 } ^ { [ \mathrm { s l o w } ] } \circ \left( \varphi _ { h / 2 N } ^ { [ \mathrm { f a s t } ] } \circ \varphi _ { h / N } ^ { T } \circ \varphi _ { h / 2 N } ^ { [ \mathrm { f a s t } ] } \right) ^ { N } \circ \varphi _ { h / 2 } ^ { [ \mathrm { s l o w } ] } ,
$$

where $\varphi _ { t } ^ { T } , \varphi _ { t } ^ { [ \mathrm { s l o w } ] } , \varphi _ { t } ^ { [ \mathrm { f a s t } ] }$   
$T ( p ) , U ^ { [ \mathrm { s l o w } ] } ( q ) , U ^ { [ \mathrm { f a s t } ] } ( q )$ $N = 1$   
(4.4)reduces to the Stormer-Verlet scheme applied to the Hamiltonian system with $H ( p , q )$ This isaconsequenceof thefactthat $\varphi _ { t } ^ { [ \mathrm { f a s t } ] } \circ \varphi _ { t } ^ { [ \mathrm { s l o w } ] } = \varphi _ { t } ^ { U }$ is the exact flow of the Hamiltonian system corresponding to $U ( q )$ of(4.3）.In the molecular dynamicsliterature,themethod(4.4)isknownastheVerlet-Imethod(Grubmuller etal.1991,who consider the method with little enthusiasm）orr-RESPA method (Tuckerman et al.1992,with much more enthusiasm).

Example 4.3.In order to illustrate the effect of multiple time steppingwe choose a ‘solarsystem'with twoplanets,i.e.,withaHamiltonian

$$
H ( p , q ) = \frac { 1 } { 2 } \Big ( \frac { p _ { 0 } ^ { T } p _ { 0 } } { m _ { 0 } } + \frac { p _ { 1 } ^ { T } p _ { 1 } } { m _ { 1 } } + \frac { p _ { 2 } ^ { T } p _ { 2 } } { m _ { 2 } } \Big ) - \frac { m _ { 0 } m _ { 1 } } { \lVert q _ { 0 } - q _ { 1 } \rVert } - \frac { m _ { 0 } m _ { 2 } } { \lVert q _ { 0 } - q _ { 2 } \rVert } - \frac { m _ { 1 } m _ { 2 } } { \lVert q _ { 1 } - q _ { 2 } \rVert }
$$

where $m _ { 0 } = 1 , m _ { 1 } = m _ { 2 } = 1 0 ^ { - 2 }$ and initial values $q _ { 0 } = ( 0 , 0 )$ ， $\dot { q } _ { 0 } = ( 0 , 0 )$ , $q _ { 1 } = ( 1 , 0 )$ ， $\dot { q } _ { 1 } = ( 0 , 1 )$ , $q _ { 2 } = ( 4 , 0 )$ , $\dot { q } _ { 2 } = ( 0 , 0 . 5 )$ With thesedata,the motion of the two planets is nearly circular with periods close to $2 \pi$ and $1 4 \pi$ ,respectively.

We split the potential as

$$
U ^ { [ \mathrm { { f a s t } } ] } ( q ) = - \frac { m _ { 0 } m _ { 1 } } { \| q _ { 0 } - q _ { 1 } \| } , \qquad U ^ { [ \mathrm { s l o w } ] } ( q ) = - \frac { m _ { 0 } m _ { 2 } } { \| q _ { 0 } - q _ { 2 } \| } - \frac { m _ { 1 } m _ { 2 } } { \| q _ { 1 } - q _ { 2 } \| } ,
$$

andweapply thealgorithm of（4.4）with $N = 1$ (Stormer-Verlet）, $N = 4$ ,and $N = 8$ Since the evaluation of $\varphi _ { t } ^ { [ \mathrm { s l o w } ] }$ isabout twice as expensive ast $\varphi _ { t } ^ { [ \mathrm { f a s t } ] }$ and thatof $\varphi _ { t } ^ { x }$ isofnegligible cost,thecomputational work of applying（4.4） onafixed interval isproportional to

![](images/e534411f806bdfbe8418bc5bdcfe5627350d39d3bc6cae317304494bccf4ee33.jpg)  
Fig.4.1.Maximal error in the Hamiltonianasa function of computational work

$$
{ \frac { 2 \pi } { h } } \cdot { \frac { ( 2 + N ) } { 3 } } .
$$

Ourcomputations have shown that this measure of work corresponds very well to the actual cpu time.

Wehave solved this problemwith many different step sizes $h$ Figure4.1shows themaximal error in theHamiltonian (over the interval $[ 0 , 2 0 0 \pi ]$ asafunction of thecomputational work(4.5).We notice that the value $N \ = \ 4$ yields excellent resultsforrelatively large aswell assmall step sizes.It noticeably improves the performance of the Stormer-Verlet method.If $N$ becomes too large,anirregular behaviourforlarge step sizes isobserved.Such“artificial resonances”are notorious forthismethodand havebeendiscussedbyBiesiadecki&Skeel(1993)forasimilar experiment;also see Chap.XIII.For large $N$ we also note a loss of accuracy for small step sizes.The optimal choice of $N$ (which here isclose to 4) depends on the problem and on the splitting into fastand slow parts,and has to be determined by experiment.

Themultiple time stepping technique can be iteratively extended to problems withmore than two different time scales.The idea is to split the‘fastvector field of(4.1） into $f ^ { \vert \mathrm { f a s t } \vert } ( y ) = f ^ { \vert f f \vert } ( y ) + f ^ { \vert f s \vert } ( y )$ ,and toreplace themethod $\bar { \Phi } _ { h } ^ { [ \mathrm { f a s t } ] }$ in Algorithm 4.1withamultiple time steppingmethod.Depending on theproblem,a significant gain incomputer time may be achieved in thisway.

Manymore multiple time stepping methods that extend the above Verlet-I/r-RESPA/impulse method,have been proposed in the literature,most notably the mollified impulse method of Garcia-Archilla,Sanz-Serna & Skeel (1999)；see Sect. XIII.1.

# VIII.4.2 Averaged Forces

Adifferent approach to multiple time stepping arises from the idea of advancing the stepwith averaged forceevaluations.We describesuchamethod forthe secondorder equation

$$
\ddot { y } = f ( y ) , \qquad f ( y ) = f ^ { [ \mathrm { s l o w } ] } ( y ) + f ^ { [ \mathrm { f a s t } ] } ( y ) .
$$

The exact solution satisfies

$$
y ( t + h ) - 2 y ( t ) + y ( t - h ) = h ^ { 2 } \int _ { - 1 } ^ { 1 } ( 1 - | \theta | ) f { \big ( } y ( t + \theta h ) { \big ) } d \theta ,
$$

where the integral on theright-hand side represents a weighted average of the force along the solution,which is now going to be approximated.At $t = t _ { n }$ ,wereplace

$$
f \big ( y ( t _ { n } + \theta h ) \big ) \approx f ^ { \mathrm { [ s l o w ] } } ( y _ { n } ) + f ^ { \mathrm { [ f a s t ] } } \big ( u ( \theta h ) \big )
$$

where $u ( \tau )$ isasolution of thediferential equation

$$
\ddot { u } = f ^ { \mathrm { [ s l o w ] } } ( y _ { n } ) + f ^ { \mathrm { [ f a s t ] } } ( u ) .
$$

Wethen have

$$
\begin{array} { r } { h ^ { 2 } \displaystyle \int _ { - 1 } ^ { 1 } ( 1 - | \theta | ) \Big ( f ^ { [ \mathrm { s l o w } ] } ( y _ { n } ) + f ^ { [ \mathrm { f a s t } ] } \big ( u ( \theta h ) \big ) \Big ) d \theta = u ( h ) - 2 u ( 0 ) + u ( - h ) . } \end{array}
$$

The velocitiesare treated similarly,starting from the identity

$$
{ \dot { y } } ( t + h ) - { \dot { y } } ( t - h ) = h \int _ { - 1 } ^ { 1 } f { \big ( } y ( t + \theta h ) { \big ) } d \theta ~ .
$$

ASymmetric Two-StepMethod.For the differential equation（4.7）we assume the initial values

$$
u ( 0 ) = y _ { n } , \quad \dot { u } ( 0 ) = \dot { y } _ { n } .
$$

This initial value problemissolved numerically,e.g.,bythe Stormer-Verletmethod with a smaller step size $\pm h / N$ onthe interval $[ - h , h ]$ ,yieldingnumerical approximations $u _ { N } ( \pm h )$ and $\upsilon _ { N . } ( \pm h )$ to $u ( \pm h )$ and $\dot { u } ( \pm h )$ ,respectively.Note that no further evaluations of $f ^ { \mathrm { [ s l o w ] } }$ areneeded for the computation of $u _ { N } ( \pm h )$ and $v _ { N } ( \pm h )$ . This finally givesthe symmetric two-stepmethod(Hochbruck&Lubich 1999a)

$$
\begin{array} { r c l } { { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } } } & { { = } } & { { u _ { N } ( h ) - 2 u _ { N } ( 0 ) + u _ { N } ( - h ) } } \\ { { } } & { { } } & { { } } \\ { { \dot { y } _ { n + 1 } - \dot { y } _ { n - 1 } } } & { { = } } & { { v _ { N } ( h ) - v _ { N } ( - h ) . } } \end{array}
$$

The starting values $y _ { 1 }$ and $\dot { y } _ { 1 }$ are chosen as $u _ { N } ( h )$ and $v _ { N } ( h )$ which correspond to (4.7）and(4.8）for $n = 0$ ,.

ASymmetric One-step Method.An explicit one-step method with similar averaged forcesisobtainedwhen theinitial values for(4.7)are chosenas

$$
u ( 0 ) = y _ { n } , \quad \dot { u } ( 0 ) = 0 .
$$

Itmayappear crude to take zeroinitial values for the velocity,butweremark that for linear $f ^ { \mathrm { [ f a s t ] } }$ theaveraged force $( u ( h ) - 2 u ( 0 ) + u ( - h ) ) / h ^ { 2 }$ does not depend on the choice of ${ \dot { u } } ( 0 )$ Moreover the solution then satisfies $u ( - t ) = u ( t )$ sothat the computational cost is halved.We again denote by $u _ { N } ( h ) = u _ { N } ( - h )$ thenumerical approximation to $u ( h )$ obtained with step size $\pm h / N$ from a one-step method (e.g., fromthe Stormer-Verlet scheme).Because of(4.1O) the averaged forces

$$
F _ { n } = { \frac { 1 } { h ^ { 2 } } } \left( u _ { N } ( h ) - 2 u _ { N } ( 0 ) + u _ { N } ( - h ) \right) = { \frac { 2 } { h ^ { 2 } } } \left( u _ { N } ( h ) - u _ { N } ( 0 ) \right)
$$

now depend only on $y _ { n }$ and not on thevelocity $\dot { y } _ { n }$ .Intrustworthy Verlet manner, the scheme $y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } F _ { n }$ can bewritten as the one-step method

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle v _ { n + 1 / 2 } = ~ v _ { n } + \frac { h } { 2 } F _ { n } } } \\ { { } } & { { } } & { { \displaystyle y _ { n + 1 } = ~ y _ { n } + h v _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { \displaystyle v _ { n + 1 } = ~ v _ { n + 1 / 2 } + \frac { h } { 2 } F _ { n + 1 } ~ , } } \end{array}
$$

Theauxiliaryvariables $\upsilon _ { n }$ canbeinterpreted as averaged velocities:we have

$$
v _ { n } = { \frac { y _ { n + 1 } - y _ { n - 1 } } { 2 h } } \approx { \frac { y ( t _ { n + 1 } ) - y ( t _ { n - 1 } ) } { 2 h } } = { \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } { \dot { y } } ( t _ { n } + \theta h ) d \theta ~ .
$$

Thisaverage may differ substantially from $\dot { y } ( t _ { n } )$ if the solution is highly oscillatory in $[ - h , h ]$ In the experiments of this section it turned out that the choice $v _ { 0 } = \dot { y } _ { 0 }$ and ${ \dot { y } } _ { n } = v _ { n }$ asvelocity approximations gives excellent results.

Ina multirate context,symmetric one-step schemesusing averaged forces werestudiedbyHochbruck&Lubich（1999b),Nettesheim&Reich(1999),and Leimkuhler&Reich(2oo1).Aclosely related approach forproblemswithmultiple timescalesis the heterogeneousmultiscalemethod byE(2oo3)and Engquist& Tsai (2005).

Example 4.4.We addasatellite of mass $m _ { 3 } = 1 0 ^ { - 4 }$ to the three body-problem of Example4.3.It movesrapidlyaround theplanet number one.The initial positions and velocities are $q _ { 3 } = ( 1 . 0 1 , 0 )$ and $p _ { 3 } = ( 0 , 0 )$ We split the potential as

$$
U ^ { [ \mathrm { f a s t } ] } ( q ) = - \frac { m _ { 1 } m _ { 3 } } { \lVert q _ { 1 } - q _ { 3 } \rVert } , \qquad U ^ { [ \mathrm { s l o w } ] } ( q ) = - \sum _ { \stackrel { i < j } { ( i , j ) \neq ( 1 , 3 ) } } \frac { m _ { i } m _ { j } } { \lVert q _ { i } - q _ { j } \rVert } ,
$$

andwe apply themethods (4.9),(4.11),and the impulse method (4.4).Since the sumin $U ^ { \left[ \mathrm { { s l o w } } \right] }$ contains 5 terms,the computational work is proportional to

$$
\begin{array} { l l } { { \displaystyle { \frac { 5 + N } { 6 h } } } } & { { \mathrm { f o r } \mathrm { m e t h o d s } ( 4 . 1 1 ) \mathrm { a n d } ( 4 . 4 ) } } \\ { { \displaystyle { \frac { 6 + 2 N } { 6 h } } } } & { { \mathrm { f o r } \mathrm { m e t h o d } ( 4 . 9 ) . } } \end{array}
$$

Foreach of the methodswe have optimizedthe number $N$ ofsmall steps.We obtaineda flatminimum near $N = 4 0$ for(4.9） and(4.4),and a morepronounced minimumat $N = 1 2$ for(4.11).Figure4.2shows the errorsat $t = 1 0$ in the positionsand in the Hamiltonianasa function of the computational work.

![](images/e0328cc4aea977061c2ef2956146f18a2c27b0432e41960886e8fe0aaf7bc951.jpg)  
Fig.4.2.Errors in position and in the Hamiltonianasa function of the computational work; theclassical Stormer-Verletmethod,the impulsemethod(4.4),andtheaveraged forcemethods(4.11) and(4.9).The errors in the Hamiltonianare indicatedby grey lines(same linestyle)

Theerrorin the position islargest for the Stormer-Verlet method and significantlysmallest for theone-stepaveraged-forcemethod(4.11).The errorsinthe velocitiesareabouta factor 1oo largerforallmethods.Theyarenot included in thefigure.The error in the Hamiltonianis very similar for all methodswith the exception of the two-stepaveraged-force method (4.9),for which it is much larger.

# VIII.5 Reducing Rounding Errors

..the idea is to capture the rounding errors and feed them back into the summation. （N.J.Higham1993）

All numerical methods for solving ordinary differential equations require thecomputation of arecursion of the form

$$
y _ { n + 1 } = y _ { n } + \delta _ { n } ,
$$

where $\delta _ { n }$ ,theincrement,isusuallysmallerinmagnitude thantheapproximation $y _ { n }$ to the solution.In this situation the rounding errors caused by the computation of $\delta _ { n }$ are in general smaller than those due to theaddition in (5.1).

Afirst attempt at reducing the accumulation of rounding errors (in fixed-point arithmetic forhisRunge-Kutta code）wasdue to Gill（1951）.Kahan（1965）and Moller（1965) both extended this idea to floating point arithmetic.The resulting algorithmisnowadayscalled‘compensated summation’,and aparticularly nicepresentationandanalysisis givenbyN.Higham(1993).In the followingalgorithmwe assume that $y _ { n }$ isa scalar;vector valued recursions are treated componentwise.

Algorithm5.1 (Compensated Summation). Let $y _ { 0 }$ and $\{ \delta _ { n } \} _ { n \geq 0 }$ be given and put $e = 0$ Compute $y _ { 1 } , y _ { 2 } , \ldots$ from(5.1)asfollows:

$$
{ \begin{array} { r l } & { f o r \ n = 0 , 1 , 2 , \dots \ d o } \\ & { \ a = y _ { n } } \\ & { \ e = e + \delta _ { n } } \\ & { y _ { n + 1 } = a + e } \\ & { \ e = e + ( a - y _ { n + 1 } ) } \\ & { e n d \ d o } \end{array} }
$$

Thisalgorithm can best be understood with the help of Fig.5.1 (following the presentation of N.Higham(1993)).We present the mantissas of floating point numbers by boxes,for which the horizontal position indicates the exponent (fora large exponent the box ismore to the left).The mantissas of $y _ { n }$ and $e$ togetherrepresent theaccurate value of $y _ { n }$ （notice that in the beginning $e = 0$ .Theoperationsof Algorithm5.1yield $y _ { n + 1 }$ andanew $e$ which together represent $y _ { n + 1 } = y _ { n } + \delta _ { n }$ No digit of $\delta _ { n }$ islost in thisway.Witha standard summation the last digits of $\delta _ { n }$ (those indicated by $\delta ^ { \prime \prime }$ inFig.5.1）would have beenmissed.

![](images/468a261368e639014b8e78498ef8492f397ecc64ecd2169672bea9f0cc2d4cf8.jpg)  
Fig.5.1.Illustration of the technique of"compensated summation"

Numerical Experiment.We study the effect of compensated summation on the Keplerproblem(I.2.2) (writtenasafirst order system)with eccentricity $e = 0 . 6$ andinitial valuesasin(I.2.11）,so that theperiod of the elliptic orbitisexactly $2 \pi$ Asthenumerical integrator we take the composition method(V.3.13） of order 8with the Stormer-Verlet scheme as basic integrator.We compute the numerical solution with step size $h = 2 \pi / 5 0 0$ oncewith standard update of the increment, oncewith compensated summation (both in double precision）and,in order to geta reference solution,we also perform the whole computation in quadruple precision. The difference between the double and quadruple precision computations gives us therounding errors.Their Euclidean normsasa function of timeare displayed in Fig.5.2.

Wesee that throughout the whole integration interval the rounding errors of the standard implementationarenearlya factor of1oo larger than those of theimplementation with compensated summation.This corresponds to the inverse of the step size or,more precisely,to the mean quotient between $y _ { n }$ and $\delta _ { n }$ in(5.1）.InFig.5.2 wehave also included the pure global error of the method(without rounding errors） atintegral multiples of the period $2 \pi$ (henceno oscillationsare visible).This is obtained as the difference of the numerical solution computed with quadruple precisionand the exact solution.We observea linear growth of thepure global error (thiswill be explained in Sect.X.3)anda growth like $\mathcal { O } ( t ^ { 3 / 2 } )$ due to the rounding errors.Thus,eventually the rounding errorswill surpass the truncation errors,but this happens for the compensated summation only after some 1ooo periods.

![](images/947181b58bd9028ecd71dd2a1648f7fa0e27c7d3ce7958e6c9dcce83a1d6a012.jpg)  
Fig.5.2.Rounding errors and pure global error asa function of time;the parallel grey lines indicatea growth of $\mathcal { O } ( t ^ { 3 / 2 } )$

Probabilistic Explanation of the Error Growth.Our aim is to explain the growth rateof rounding errors observed in Fig.5.2.Denote by $\varepsilon _ { k }$ thevector of rounding errorsproduced during the computations in the kth step.Since the derivative of the flow $\varphi _ { t } ( y )$ describes the propagation of these errors,the accumulated rounding error attime $t = t _ { N }$ （ $t _ { k } = k h$ )is

$$
\eta _ { t } = \sum _ { k = 1 } ^ { N } \varphi _ { t - t _ { k } } ^ { \prime } ( y _ { k } ) \varepsilon _ { k } .
$$

FortheKeplerproblemand,infact,forallcompletelyintegrabledifferential equations(cf.Sect.X.1) the flow and itsderivative grow at most linearlywith time,i.e.,

$$
\left\| \varphi _ { t - t _ { k } } ^ { \prime } ( y ) \right\| \leq a + b ( t - t _ { k } ) \qquad { \mathrm { f o r } } \quad t \geq t _ { k } .
$$

Using $\varepsilon _ { k } = \mathcal { O } ( e p s )$ ,where eps denotes the roundoff unit of the computer,an applicationof the triangleinequalityto(5.2)yields $\eta _ { t } = \mathcal { O } ( t ^ { 2 } e p s ) .$ From our experiment ofFig.5.2we see that such an estimate is too pessimistic.

Fora better understanding of accumulated rounding errors over long time intervalswe makeuse of probability theory.Such an approach has been developed in theclassical book of Henrici (1962).We assume that the components $\mathbf { \xi } \in k \mathbf { \overset { . } { 2 } }$ of $\varepsilon _ { k }$ are randomvariableswithmeanand variance

$$
E ( \varepsilon _ { k i } ) = 0 , \qquad V a r ( \varepsilon _ { k i } ) = C _ { k i } \cdot e p s ^ { 2 } ,
$$

and uniformly bounded $C _ { k i } \leq C .$ For simplicity we assume that all $\varepsilon _ { k i }$ areindependentrandom variables.Replacing the matrix $\varphi _ { t - t _ { k } } ( y _ { k } )$ in (5.2)with $\varphi _ { t - t _ { k } } \bigl ( y ( t _ { k } ) \bigr )$

and denoting its entries by $w _ { i j k }$ ,the $i$ th component of the accumulated rounding error(5.2）becomes

$$
\eta _ { t i } = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { n } w _ { i j k } \varepsilon _ { k j } ,
$$

a linear combination of therandomvariables $\varepsilon _ { k j }$ .Elementaryprobability theory thus implies that

$$
E ( \eta _ { t i } ) = 0 \qquad \mathrm { a n d } \qquad V a r ( \eta _ { t i } ) = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { n } w _ { i j k } ^ { 2 } V a r ( \varepsilon _ { k j } ) .
$$

Inserting theestimate (5.3) for $w _ { i j k }$ we get

$$
V a r \left( \eta _ { t i } \right) \le \sum _ { k = 1 } ^ { N } \left( a + b ( t - t _ { k } ) \right) ^ { 2 } \operatorname* { m a x } _ { j = 1 , \ldots , n } V a r \left( \bar { \varepsilon } _ { k j } \right) = \mathcal { O } \Bigl ( \frac { C } { h } t ^ { 3 } e p s ^ { 2 } \Bigr ) .
$$

Consequently,the Euclidean norm of the expected rounding error $\eta _ { t }$ is

$$
\left( \sum _ { i = 1 } ^ { n } V a r \left( \eta _ { t i } \right) \right) ^ { 1 / 2 } = \mathcal { O } \left( \sqrt { \frac { C } { h } } t ^ { 3 / 2 } e p s \right) .
$$

This is in excellent agreement with the results displayed in Fig.5.2.

# VIII.6 Implementation of ImplicitMethods

Symplecticmethods for general Hamiltonian equationsare implicit,and so are symmetric methods for general reversible systems.Also,whenwe consider variable step sizeextensions asdescribed in SectionsVII.3and VIII.2,we are led to nonlinear equations.The efficient numerical solution of such nonlinear equations is the main difficultyinan implementation of implicit methods.Notice that in the context of geometric integration thereis no need of ad-hoc strategies for step size and order selection,so that the remaining parts of a computer code are more or less straightforward.

In the following we discuss the numerical solution of the nonlinear system defined by an implicit Runge-Kutta method.Wehave the Gauss methods ofSect.II.1.3 inmind which are symplectic and symmetric.An extension of the ideas to partitionedRunge-Kuttamethodsand to Nystrommethodsis obvious.For simplicity of notation we consider autonomous differential equations ${ \dot { y } } = f ( y ) ,$ andwewrite thenonlinear system of Definition II.1.1 inthe form

$$
Z _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } f { \big ( } y _ { n } + Z _ { j n } { \big ) } = 0 , \qquad i = 1 , . . . , s .
$$

The unknown variables are $\mathcal { L } _ { 1 n } , \ldots , \mathcal { L } _ { s n }$ ,and theequivalence ofthetwo formulations isvia therelation $k _ { i } = f \left( y _ { n } + Z _ { i n } \right) .$ Thenumerical solution after one step can be expressed as

$$
y _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f \bigl ( y _ { n } + Z _ { i n } \bigr ) .
$$

Forimplicit Runge-Kutta methods the equations (6.1） represent a nonlinear system that has to be solved iteratively.We discuss thechoice of good starting approximations for $\boldsymbol { Z } _ { i n }$ aswell as different nonlinear equation solvers (fixed-point iteration, modifiedNewton methods).

# VIII.6.1 Starting Approximations

Themost simple approximations to the solution $Z _ { i n }$ of (6.1）are $Z _ { i n } ^ { 0 } ~ = ~ 0$ or $Z _ { i n } ^ { 0 } ~ = ~ h c _ { i } f ( y _ { n } )$ where $c _ { i } = \textstyle \sum _ { j = 1 } ^ { s } a _ { i j }$ Teyeow and we will try to exploit the information of previous steps for improving them. Thereare essentially two possibilities:either use only the information of the last step $y _ { n - 1 } \mapsto y _ { n }$ （methods（A）and(B）below）,orconsidera fixed $i$ anduse the interpolation polynomial that passes through $\angle i , n - l$ for $l = 1 , 2 , \ldots$ (method(C)）. Letusseparatelydiscuss these twoapproaches.

(A)Use of Continuous Output.Consider the polynomial $w _ { n - 1 } ( t )$ ofdegree $s$ that interpolates the values $( t _ { n - 1 } , y _ { n - 1 } )$ and $( t _ { n - 1 } + c _ { i } h , Y _ { i , n - 1 } )$ for $i = 1 , \dots , s$ ,where $Y _ { i , n - 1 } = y _ { n - 1 } + Z _ { i , n - 1 }$ istheargument in (6.1) of theprevious step.For collocation methods (such as Gauss methods) $w _ { n - 1 } ( t )$ is the collocation polynomial,and we knowfrom Lemma II.1.6 that oncompact intervals

$$
w _ { n - 1 } ( t ) - y ( t ) = \mathcal { O } ( h ^ { q + 1 } )
$$

with $q = s$ ,where $y ( t )$ denotes the solution of $\dot { y } = f ( y )$ satisfying $y ( t _ { n - 1 } ) = y _ { n - 1 }$ . ForRunge-Kutta methods that are not collocation methods,(6.3)holdswith $q$ defined by the condition $C ( q )$ of(II.1.11).Since the solution of $\dot { y } = f ( y )$ passing through $y ( t _ { n } ) ~ = ~ y _ { n }$ is $\mathcal { O } ( h ^ { p + 1 } )$ closeto $y ( t )$ with $p \ \geq \ q$ ,wehave $w _ { n } ( t ) \ =$ $w _ { n - 1 } ( t ) + \mathcal { O } ( h ^ { q + 1 } )$ and the computablevalue

$$
Z _ { i n } ^ { 0 } = Y _ { i n } ^ { 0 } - y _ { n } , \qquad Y _ { i n } ^ { 0 } = w _ { n - 1 } ( t _ { n } + c _ { i } h )
$$

servesas starting approximation for(6.1）with an error of size $\mathcal { O } ( h ^ { q + 1 } )$ Thisapproachis standard in variable step size implementations of implicit Runge-Kutta methods(cf.Sect.IV.8ofHairer&Wanner(1996)).Since $w _ { n - 1 } ( t ) - y _ { n - 1 }$ isalinear combination of the $Z _ { i , n - 1 } = Y _ { i , n - 1 } - y _ { n - 1 } ,$ itfollows from(6.1）that itisalso a linear combination of $h f ( Y _ { i , n - 1 } )$ ,sothat

$$
Y _ { i n } ^ { 0 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } f ( Y _ { j , n - 1 } ) .
$$

For a constant step size implementation,the $\beta _ { i j }$ depend only onthe method coefficientsand can be computedinadvanceasthe solution of the linear Vandermonde typesystem

$$
\sum _ { j = 1 } ^ { s } \beta _ { i j } c _ { j } ^ { k - 1 } = \frac { ( 1 + c _ { i } ) ^ { k } } { k } , \qquad k = 1 , \ldots , s
$$

(see Exercise 2).For collocation methods and for methods with $q ~ \geq ~ s - 1$ the coefficients $\beta _ { i j }$ from(6.6)are optimal in the sense that they are the only ones making (6.5)an sth order approximation to the solution of(6.1).For $q \ < \ s - 1$ ,more complicated order conditions have to be considered(Sand 1992).

(B)Starting Algorithms Using Additional Function Evaluations.In particular for high order methodswhere $s$ isrelatively large,a much more accurate starting approximationcan be constructed with the aid ofa few additional function evaluations.Such startingalgorithms have been investigated by Laburta(1997),who presents coefficients for the Gauss methodsup to order8inLaburta(1998).

The idea is to use starting approximations of the form

$$
Y _ { i n } ^ { 0 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } f ( Y _ { j , n - 1 } ) + h \sum _ { j = 1 } ^ { m } \nu _ { i j } f ( Y _ { s + j , n - 1 } ) ,
$$

where $Y _ { 1 , n - 1 } , \dots , Y _ { s , n - 1 }$ arethe internal stages of the basic implicit Runge-Kutta method(with coefficients $c _ { i } , a _ { i j } , b _ { j } )$ ,and theadditionalinternal stagesare computed from

$$
Y _ { s + i , n - 1 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s + i - 1 } \mu _ { i j } f ( Y _ { j , n - 1 } ) .
$$

Forafixed $i$ ,weinterpret $Y _ { i n } ^ { 0 }$ as the result of the explicit Runge-Kutta method with coefficients of therighttableau of

$$
\begin{array} { r } { \frac {  { c } } { \vert \vert + c \vert } \left. \begin{array} { l } { A } \\ { B } \\ { b ^ { T } } \end{array} \right.  { a } \quad \quad \quad \quad \quad \quad \frac {  { a } \vert \vert M _ { 1 } } { \beta _ { i } ^ { T } } \ k _ { i } ^ { T } } \end{array}
$$

Here, $( M _ { 1 } , M _ { 2 } ) = M = ( \mu _ { j k } )$ $\begin{array} { r } { \mu _ { j } = \sum _ { k = 1 } ^ { s + j - 1 } \mu _ { j k } } \end{array}$ and $c , \mu , \beta _ { i } , \nu _ { i }$ are the vectors composed of $c _ { j } , \mu _ { j } , \beta _ { i j } , \nu _ { i j }$ respectively.The exact stage values $Y _ { i n }$ are interpreted astheresult of the Runge-Kutta method with coefficients given in the left tableau of(6.8).The entries of the vectors $\mathbb { 1 } , b$ and $a _ { i }$ are $1 , b _ { j }$ and $a _ { i j }$ ,respectively,and $B$ is thematrix whose rows areall equal to $b ^ { T }$ .

Ifthe orderconditions(see Sect.III.1) for the two Runge-Kutta methods of(6.8) give the same result for all trees with $\leq r$ vertices,we get an approximation of order $r$ ,i.e., $Y _ { \ i n } ^ { 0 } - Y _ { i n } = \mathcal { O } ( h ^ { r + 1 } ) ,$ For the bushy tree $\tau _ { k } = [ \circ , \ldots , \bullet ]$ with $k$ vertices wehave

$$
\sum _ { j = 1 } ^ { s } \beta _ { i j } c _ { j } ^ { k - 1 } + \sum _ { j = 1 } ^ { m } \nu _ { i j } \mu _ { j } ^ { k - 1 } = \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { k - 1 } + \sum _ { j = 1 } ^ { s } a _ { i j } ( 1 + c _ { j } ) ^ { k - 1 } .
$$

Notice that for collocation methods (such as the Gauss methods) the condition $C ( s )$ reduces the right-hand expression of this equation to $( 1 + c _ { i } ) ^ { k } / k$ for $k \leq s$ For $m = 0$ ,these conditions are thus equivalent to (6.6).

For the tree $[ \tau _ { k } ] = [ [ \circ , \ldots , \circ ] ]$ with $k + 1$ vertices we get thecondition

$$
\begin{array} { r l r } {  { \sum _ { j , l = 1 } ^ { s } \beta _ { i j } a _ { j l } c _ { l } ^ { k - 1 } + \sum _ { j = 1 } ^ { m } \nu _ { i j } \Big ( \sum _ { l = 1 } ^ { s } \mu _ { j l } c _ { l } ^ { k - 1 } + \sum _ { l = 1 } ^ { m } \mu _ { j , s + l } \mu _ { l } ^ { k - 1 } \Big ) } } \\ & { } & { \equiv \sum _ { j , l = 1 } ^ { s } b _ { j } a _ { j l } c _ { l } ^ { k - 1 } + \sum _ { j , l = 1 } ^ { s } a _ { i j } \Big ( b _ { l } c _ { l } ^ { k - 1 } + a _ { j l } ( 1 + c _ { l } ) ^ { k - 1 } \Big ) . } \end{array}
$$

Wenow assume that the Runge-Kutta method corresponding to the right tableau of (6.8）satisfies condition $C ( s ) .$ Thismeans that themethod $( c , A , b )$ isa collocation method,and that the coefficients $\mu _ { i j }$ have to be computed from the linear system

$$
\sum _ { j = 1 } ^ { s + i - 1 } \mu _ { i j } c _ { j } ^ { k - 1 } = \frac { \mu _ { i } ^ { k } } { k } , \qquad k = 1 , \ldots , s .
$$

Themethod corresponding to the left tableau of(6.8）then also satisfies $C ( s )$ .Consequently，the order conditions are simplified considerably,and it follows from Sect.IIL.1 that $Y _ { i n } ^ { 0 }$ is anapproximationtotheexactstagevalue $Y _ { i n }$ of order $s + 1$ or $s + 2$ if the following conditions hold:

$$
\begin{array} { r l } { \mathrm { o r d e r ~ } s + 1 } & { \mathrm { ~ i f ~ } ( 6 . 9 ) \mathrm { f o r ~ } k = 1 , . . . , s + 1 ; } \\ { \mathrm { o r d e r ~ } s + 2 } & { \mathrm { ~ i f ~ } ( 6 . 9 ) \mathrm { f o r ~ } k = 1 , . . . , s + 2 , \mathrm { a n d ~ } ( 6 . 1 0 ) \mathrm { f o r ~ } k = s + 1 } \end{array}
$$

Foran approximation of order $s + 1$ weput $m = 1$ ,wearbitrarily choose $\mu _ { 1 }$ ,wecomputeμ1jfrom(6.11）,and thecoefficients $\beta _ { i j }$ and $\nu _ { i 1 }$ from（6.9）with $k = 1 , \ldots , s + 1$ Areasonablechoice for the freeparameteris $\mu _ { 1 } \in [ 1 , 2 ]$ (inour computations we take $\mu _ { 1 } = 1 . 7 5$ for $s = 2 , 4$ ,and $\mu _ { 1 } = 1 . 8$ for $s = 6$ .1

Foranapproximation of order $s + 2$ weput $m = 3 .$ One of the three additional function evaluations can be saved if we put $\mu _ { 1 } = 0$ and $\mu _ { 2 } ~ = ~ 1$ .Thisimplies $Y _ { s + 1 , n - 1 } = y _ { n - 1 }$ and $Y _ { s + 2 , n - 1 } = y _ { n }$ so that theevaluation of $f ( Y _ { s + 1 , n - 1 } )$ is already availablefrom computations for thepreceding step(FSAL technique,“first sameas last").In our experiments we take $\mu _ { 3 } ~ = ~ 1 . 6$ for $s \ = \ 2$ , $\mu _ { 3 } = 1 . 6 5$ for $s = 4$ ,and $\mu _ { 3 } = 1 . 7 5$ for $s = 6$ Thecoefficients $\mu _ { i j } , \beta _ { i j } , \nu _ { i j }$ are then obtained as the solution of Vandermonde like linear systems.

Forpleeatiooetkiti $Z _ { i n } ^ { 0 } =$ $Y _ { i n } ^ { 0 } - y _ { n }$ andtowrite(6.7) in the form

$$
Z _ { i n } ^ { 0 } = h \sum _ { j = 1 } ^ { s } \alpha _ { i j } f ( Y _ { j , n - 1 } ) + h \sum _ { j = 1 } ^ { m } \nu _ { i j } f ( Y _ { s + j , n - 1 } )
$$

with $\alpha _ { i j } = \beta _ { i j } - b _ { j } .$

(C)Equistage Approximation.From the implicit function theorem,applied to the nonlinear system（6.1）,weknow that $Z _ { i n } = z ( y _ { n } , h )$ ,where the function $z ( y , h )$ isas smoothas $f ( y )$ Furthermore,since on compact intervals the global errorofa one-step method permits an asymptotic expansion in powers of $h$ ,wehave $y _ { n - l } =$ $y _ { N } ( t _ { n - l } , h ) + O ( h ^ { N + 1 } )$ with $y _ { N } ( t , h ) = y ( t ) + h ^ { p } e _ { p } ( t ) + \ldots , + h ^ { N } e _ { N } ( t )$ (thevalue of $N$ can bechosen arbitrarily largeif $f ( y )$ issufficiently smooth).Consequently, $Z _ { i , n - l }$ is $\mathcal { O } ( h ^ { N + 1 } )$ closeto the smooth function $z \left( y _ { N } ( t , h ) , h \right)$ at $t = t _ { n } - l h$ . Let $\zeta _ { i } ( t )$ be the polynomial of degree $k - 1$ defined by $\zeta _ { i } ( t _ { n - l } ) ~ = ~ Z _ { i , n - l }$ for $l = 1 , \ldots , k .$ Then,thevalue

$$
Z _ { i n } ^ { 0 } = \zeta _ { i } ( t _ { n } )
$$

yieldsa $\mathcal { O } ( h ^ { k + 1 } )$ approximation to the solution of (6.1).This interpolation procedure was first proposed by In't Hout(1992） for the numerical solution of delay differential equations.For the iterative solution of the nonlinearRunge-Kutta equations(6.1）,the startingapproximation (6.14) is proposed and analyzed by Calvo (2002).

The implementation of this approach is very simple.Using Newton's interpolation formulawe have

$$
Z _ { i n } ^ { 0 } = Z _ { i , n - \bar { 1 } } + \nabla Z _ { i , n - 1 } + \ldots + \nabla ^ { k - 1 } Z _ { i , n - \bar { 1 } }
$$

with backward differences given by $\nabla Z _ { i , n } = Z _ { i , n } - Z _ { i , n - 1 }$ ， $\nabla ^ { 2 } Z _ { i , n } = \nabla Z _ { i , n } -$ $\nabla Z _ { i , n - 1 }$ ,etc.

Numerical Study of Starting Approximations.We consider the Keplerproblem with eccentricity $e = 0 . 6$ and initial values such that the period is $2 \pi$ Withmany different step sizes $h = 2 \pi / N$ wecompute $N + 1$ stepswith the Gauss method oforder $p = 2 s$ $p = 4 , 8 , 1 2 )$ In the last stepwe compute thedifferent starting approximations and their error $\begin{array} { r l } {  { ( \sum _ { i = 1 } ^ { s } \| Z _ { i n } - Z _ { i n } ^ { 0 } \| ^ { 2 } ) ^ { 1 / 2 } } } \end{array}$ asa function of the step size $h$ .Theresult isplotted inFig.6.1.There,thepictures also contain the global errors after one period.Theyallow us to localize the values of $h$ ,which are of practical interest.

Weobserve that theequistage approximation(6.15)also behaves like $O ( h ^ { k + 1 } )$ when $k + 1$ islarger than the order of the integrator.However,dueto the increasingerror constants,the accuracy isimproved only for small step sizes.An optimal $k$ couldbe estimated by checking the decrease of the backward differences ${ \| \nabla ^ { \ j } Z _ { i , n - 1 } \| }$ The error of the starting approximation obtained from the continuous output behaves like $\mathcal { O } ( h ^ { s + 1 } )$ (for the Gauss methods)and,incontrast to the equistageapproximation,improveswith increasing order.The approximations (6.7）of order $s + 1$ and $s + 2$ areaclearimprovement.Asaconclusionwe find that for this example the equistage approximation (whichis free from additional function evaluations)ispreferable only for $s = 2$ (order4).For higher order,theapproximation obtained from(6.7)is significantlymore accurate and so itisworthwhile to spend these two additional function evaluations per step.

![](images/69beb852057ef22351766065abe6f17c16cc98bcd42403a02d5a1960f2ca7dd1.jpg)  
Fig.6.1.Errors of starting approximations for Gauss methodsas functions of the step size $h$ :thickdashed lines for the extrapolatedcontinuous output (6.4)and for theapproximations (6.7)of order $s + 1$ and $s + 2$ thinsolid linesfor theequistage approximation (6.15)with $k = 0 , 1 , \ldots , 7 ;$ thethick solid line representsthe global error of the method after one period

# VIII.6.2 Fixed-Point VersusNewton Iteration

Finallywe investigate the iterative solution of the nonlinearRunge-Kutta system (6.1).We discuss fixed-point and Newton-like iterations,and we compare their efficiency to the use of composition methods.

Fixed-Point Iteration.This isthe most simple and most natural iteration for the solutionof (6.1).Withanystartingapproximation $Z _ { i n } ^ { 0 }$ fromSect.VII.6.1 it reads

$$
Z _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } f \bigl ( y _ { n } + Z _ { j n } ^ { k } \bigr ) , \qquad i = 1 , \ldots , s .
$$

In the case where the entries of the Jacobian matrix $f ^ { \prime } ( y )$ arenot excessively large (nonstiff problems)and that the step sizeis sufficiently small,this iteration convergesfor tothe solution of(6.1).Usually,the iteration is stopped ifa cetinomofteitcees $Z _ { i n } ^ { k + 1 } - Z _ { i n } ^ { k }$ isucymal.euse $Z _ { i n } ^ { k }$ intheupdate formula(6.2） so thatno additional function evaluationisrequired.

Foranumerical study of the convergence of this iteration,we consider the Kepler problem with eccentricity $e = 0 . 6$ and initial values as in the preceding experiments(period of the solution is $2 \pi$ ).Weapply theGaussmethodsoforder 4,8,and 12 with various step sizes.For the integration over one period we show in Table 6.1 the total number of function evaluations,the mean number of required iterations per step,and the global errorat the endpoint of integration.Asa stopping criterion for thefixed-point iteration wecheck whether the norm of the difference of two successiveapproximations is smaller than $1 0 ^ { - 1 6 }$ (roundoff unit in double precision).As astarting approximation $Z _ { i n } ^ { 0 }$ we use (6.15)with $k = 8$ for the method of order 4, and the approximation(6.7)of order $s + 2$ forthe methods of orders 8and 12.The coefficients are those presented after equation (6.12).

Table6.1.Statistics of Gauss methods (total number of function evaluations,number of fixed-point iterations per step,and the global error at the endpoint)for computations of the Kepler problem over one period with $e = 0 . 6$   
Fixed-point iteration (general problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order4</td><td rowspan=1 colspan=1>80316.19.2.10-2</td><td rowspan=1 colspan=1>104310.41.7.10-2</td><td rowspan=1 colspan=1>13937.01.3.10-3</td><td rowspan=1 colspan=1>18254.68.4.10-5</td><td rowspan=1 colspan=1>23192.95.3.10-6</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>10219.71.1.10-3</td><td rowspan=1 colspan=1>14556.86.9.10-7</td><td rowspan=1 colspan=1>20914.73.6.10-9</td><td rowspan=1 colspan=1>30073.31.8.10-11</td><td rowspan=1 colspan=1>41832.16.9.10-14</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>12978.32.7.10-6</td><td rowspan=1 colspan=1>17315.48.0.10-11</td><td rowspan=1 colspan=1>23113.52.7.10-14</td><td rowspan=1 colspan=1>34412.5≤roundoff</td><td rowspan=1 colspan=1>59172.1≤roundoff</td></tr></table>

Since the starting approximations are more accurate for small $h$ thenumber ofnecessary iterationsdecreasesdrastically.Inparticular,for the4th ordermethod weneed about 16 iterations per step for $h = 2 \pi / 2 5$ ,butat most2iterationswhen $h \leq 2 \pi / 8 0 0$ Ifoneisinterestedin high accuracycomputations (e.g.,long-time simulationsin astronomy),forwhich theerror over one period is not larger than $1 0 ^ { - 1 0 }$ ,Table6.1illustratesthat highordermethods( $p \geq 1 2$ )aremost efficient.

Newton-Type Iterations.Astandard technique for solving nonlinear equations is Newton's method or some modification of it.Writing the nonlinear system (6.1）of animplicit Runge-Kutta method as $F ( Z ) = 0$ with $Z = ( Z _ { 1 n } , \ldots , Z _ { s n } ) ^ { \cal I }$ ,the Newton iteration is

$$
Z ^ { k + 1 } = Z ^ { k } - M ^ { - 1 } F ( Z ^ { k } ) ,
$$

where $M$ is some approximation to the Jacobian matrix $F ^ { \prime } ( Z ^ { k } )$ .Since the solution $\boldsymbol { \mathcal { L } }$ of the nonlinear system is $\mathcal { O } ( h )$ close to zero,it is common to use $M = F ^ { \prime } ( 0 )$ so that the matrix $M$ isindependent of the iteration index $k$ Inour special situation weget

$$
M = I \otimes I - h A \otimes J
$$

with $J = f ^ { \prime } ( y _ { n } ) .$ Here, $I$ denotes the identity matrix of suitable dimension,and $A$ is theRunge-Kutta matrix.

Werepeat the experiment of Table 6.1with modified Newton iterations instead offixed-point iterations.Theresultis shownin Table 6.2.We have suppressed the errorat the end of theperiod,because itis the sameasin Table6.1.As expected,the convergence is faster(i.e.,thenumber of iterationsper stepissmaller)so that the total numberof function evaluations isreduced.However,wedo not see in this table thatwe computed at every step the Jacobian $f ^ { \prime } ( y _ { n } )$ andan $L R$ -decompositionof thematrix $M .$ Even if we exploit the tensor product structure in(6.18)as explained