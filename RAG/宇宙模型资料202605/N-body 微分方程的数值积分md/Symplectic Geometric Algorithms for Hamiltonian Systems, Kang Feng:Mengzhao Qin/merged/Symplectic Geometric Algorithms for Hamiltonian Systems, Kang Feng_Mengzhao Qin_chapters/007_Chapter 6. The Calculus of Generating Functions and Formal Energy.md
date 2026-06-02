# Chapter 6. The Calculus of Generating Functions and Formal Energy

In the previous chapter, we constructed the symplectic schemes of arbitrary order via generating function. However the construction of generating functions is dependent on the chosen coordinates. One would like to know under what circumstance will the construction of generating functions be independent of the coordinates. The generating functions are deeply associated with the conservation laws, so it is important to study their properties and computations.

# 6.1 Darboux Transformation

Consider a cotangent bundle $T ^ { * } \mathbf { R } ^ { n } \simeq \mathbf { R } ^ { 2 n }$ with natural symplectic structure $[ \mathrm { F e n 9 8 a } ]$

$$
J _ { 2 n } = \left[ \begin{array} { c c } { { O } } & { { I _ { n } } } \\ { { } } & { { } } \\ { { - I _ { n } } } & { { O } } \end{array} \right] .
$$

Now we consider $\mathbf { R } ^ { 4 n }$ and the product of cotangent bundles $T ^ { * } \mathbf { R } \times T ^ { * } \mathbf { R } \simeq \mathbf { R } ^ { 4 n }$ with natural product symplectic structure:

$$
\widetilde J _ { 4 n } = \left[ \begin{array} { c c } { { - J _ { 2 n } } } & { { O } } \\ { { } } & { { } } \\ { { O } } & { { J _ { 2 n } } } \end{array} \right] .
$$

Correspondingly, we consider the product space $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n } \simeq \mathbf { R } ^ { 2 n }$ . Its cotangent bundle, $T ^ { * } ( \mathbf { R } ^ { n } \times \mathbf { R } ^ { n } ) = T ^ { * } \mathbf { R } ^ { 2 n } \simeq \mathbf { R } ^ { 4 n }$ has a natural symplectic structure:

$$
J _ { 4 n } = \left[ \begin{array} { c c } { { O } } & { { I _ { 2 n } } } \\ { { } } & { { } } \\ { { - I _ { 2 n } } } & { { O } } \end{array} \right] .
$$

Choose symplectic coordinates ${ z } = ( p , q )$ on the symplectic manifold, then for symplectic transformation, $g : T ^ { * } \mathbf { R } ^ { n }  T ^ { * } \mathbf { R } ^ { n }$ , we have

$$
\operatorname { g r } \left( g \right) = \left\{ { \left[ \begin{array} { l } { g _ { z } } \\ { z } \end{array} \right] } , z \in T ^ { * } \mathbf { R } ^ { n } \right\} ,
$$

it is a Lagrangian submanifold of $T ^ { * } \mathbf { R } ^ { n } \times T ^ { * } \mathbf { R } ^ { n }$ in $\widetilde { \mathbf R } ^ { 4 n } = ( \mathbf R ^ { 4 n } , \widetilde { J } _ { 4 n } )$ . Note that on $\mathbf { R } ^ { 4 n }$ here is a standard symplectic structure $\left( \mathbf { R } ^ { 4 n } , J _ { 4 n } \right)$ ": A generating map

$$
\alpha : T ^ { * } \mathbf { R } ^ { n } \times T ^ { * } \mathbf { R } ^ { n } \longrightarrow T ^ { * } ( \mathbf { R } ^ { n } \times \mathbf { R } ^ { n } )
$$

maps the symplectic structure (1.2) to the standard one (1.3). In particular, $\alpha$ maps Lagrangian submanifolds in $( \mathbf { R } ^ { 4 n } , \widetilde { J } _ { 4 n } )$ to Lagrangian submanifolds $\mathcal { L } _ { g }$ in $\left( \mathbf { R } ^ { 4 n } , J _ { 4 n } \right)$ . Suppose that $\alpha$ satisfies the transversality condition of $g$ Chapter 5, Equation (1.2), then

$$
\mathcal { L } _ { g } = \left\{ \left[ \begin{array} { c } { \mathbf { d } \phi _ { g } ( \omega ) } \\ { \omega } \end{array} \right] , \quad \omega \in T ^ { * } \mathbf { R } ^ { 2 n } \right\} ,
$$

$\phi _ { g }$ is called generating function of $g$ . We call this generating map $\alpha$ (linear case) or $\alpha _ { * }$ (nonlinear case) Darboux transformation, in other words, we have the following definition.

Definition 1.1. A linear map

$$
\alpha = \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { } & { } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] ,
$$

which acts as the followings:

$$
\mathbf { R } ^ { 4 n } \ni \left[ \begin{array} { l } { z _ { 0 } } \\ { z _ { 1 } } \end{array} \right] \longrightarrow \alpha \left[ \begin{array} { l } { z _ { 0 } } \\ { z _ { 1 } } \end{array} \right] = \left[ \begin{array} { l } { A _ { \alpha } z _ { 0 } + B _ { \alpha } z _ { 1 } } \\ { C _ { \alpha } z _ { 0 } + D _ { \alpha } z _ { 1 } } \end{array} \right] = \left[ \begin{array} { l } { w _ { 0 } } \\ { w _ { 1 } } \end{array} \right] \in \mathbf { R } ^ { 4 n } ,
$$

is called a Darboux transformation, if

$$
\alpha ^ { \prime } J _ { 4 n } \alpha = { \widetilde J } _ { 4 n } .
$$

Denote

$$
E _ { \alpha } = C _ { \alpha } + D _ { \alpha } , \quad F _ { \alpha } = A _ { \alpha } + B _ { \alpha } ,
$$

then, we have:

Definition 1.2. Let $\alpha$ be a Darboux tramsformation. Then we define

$$
\begin{array} { r l } & { S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) = \left\{ \alpha \in G L ( 4 n ) \mid \alpha ^ { \prime } J _ { 4 n } \alpha = \widetilde { J } _ { 4 n } \right\} = S p ( \widetilde { J } , J ) , } \\ & { S p ( J _ { 4 n } ) = \left\{ \beta \in G L ( 4 n ) \mid \beta ^ { \prime } J _ { 4 n } \beta = J _ { 4 n } \right\} = S p ( 4 n ) , } \\ & { S p ( \widetilde { J } _ { 4 n } ) = \left\{ \gamma \in G L ( 4 n ) \mid \gamma ^ { \prime } \widetilde { J } _ { 4 n } \gamma = \widetilde { J } _ { 4 n } \right\} = \widetilde { S } _ { p } ( 4 n ) . } \end{array}
$$

Definition 1.3. A special case of Darboux transformation

$$
\alpha _ { 0 } = { \left[ \begin{array} { l l } { J _ { 2 n } } & { - J _ { 2 n } } \\ { { \frac { 1 } { 2 } } I _ { 2 n } } & { { \frac { 1 } { 2 } } I _ { 2 n } } \end{array} \right] }
$$

is called Poincare transformation. ´

Remark 1.4. From the definition above, we know $\alpha _ { 0 } \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ .

Proposition 1.5. If $\alpha ~ \in ~ S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \beta ~ \in ~ S p ( 4 n ) , \gamma ~ \in ~ \widetilde { S } _ { p } ( 4 n )$ , then $\beta \alpha \gamma ~ \in$ $S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ .

Proposition 1.6. $\forall \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ , we have

$$
\begin{array} { r l } & { S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) = S p ( 4 n ) \alpha _ { 0 } = \alpha _ { 0 } \widetilde { S } _ { p } ( 4 n ) , } \\ & { S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) = S p ( 4 n ) \alpha = \alpha \widetilde { S } _ { p } ( 4 n ) . } \end{array}
$$

Proposition 1.7. Let $\alpha = \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) ,$

$$
\alpha ^ { - 1 } = \left[ \begin{array} { c c } { { - J _ { 2 n } C _ { \alpha } ^ { \prime } } } & { { J _ { 2 n } A _ { \alpha } ^ { \prime } } } \\ { { } } & { { } } \\ { { J _ { 2 n } D _ { \alpha } ^ { \prime } } } & { { - J _ { 2 n } B _ { \alpha } ^ { \prime } } } \end{array} \right] = \left[ \begin{array} { c c } { { A _ { \alpha ^ { - 1 } } } } & { { B _ { \alpha ^ { - 1 } } } } \\ { { } } & { { } } \\ { { C _ { \alpha ^ { - 1 } } } } & { { D _ { \alpha ^ { - 1 } } } } \end{array} \right] .
$$

Hint: Using the first equation of (1.2) in Definition 1.2.

Theorem 1.8. If $\alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ satisfies transversality condition $| C _ { \alpha } + D _ { \alpha } | \neq 0$ , then for all symplectic diffeomorphism $z ~  ~ g ( z )$ , $g \sim I _ { 2 n }$ (near identity), $g _ { z } \in$ $S p ( 2 n )$ , there exists a generating function:

$$
\phi _ { \alpha , g } : \mathbf { R } ^ { 2 n } \longrightarrow \mathbf { R } ,
$$

such that

$$
A _ { \alpha } g ( z ) + B _ { \alpha } z = \nabla \phi _ { \alpha , g } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) ,
$$

i.e.,

$$
( A _ { \alpha } g + B _ { \alpha } ) ( C _ { \alpha } g + D _ { \alpha } ) ^ { - 1 } z = \nabla \phi _ { \alpha , g } ( z ) .
$$

# 6.2 Normalization of Darboux Transformation

Denote ${ \cal M } \equiv { \cal S } p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ a submanifold in $G L ( 4 n )$ , $\mathrm { d i m } { \cal M } = \frac { 1 } { 2 } 4 n ( 4 n + 1 ) =$ $8 n ^ { 2 } + 2 n$ . Denote $M ^ { \ast } \equiv \left\{ \alpha \in M \ | \ E _ { \alpha } | \neq 0 \right\}$ an open submanifold of $M$ $\begin{array} { r l } { { \cal I } , \mathrm { d i m } { \cal M } ^ { * } = } \end{array}$ $\mathrm { d i m } M$ . Denote $M ^ { \prime } \equiv \{ \alpha \in M \mid E _ { \alpha } = I _ { n } , F _ { \alpha } = 0 \} \subset M ^ { * } \subset M$ .

Definition 2.1. A Darboux transformation is called a normalized Darboux transformation[Fen98a] , if

$$
E _ { \alpha } = I _ { 2 n } , \quad F _ { \alpha } = O _ { 2 n } .
$$

The following theorem answers the question on how to normalize a given Darboux transformation.

Theorem 2.2. $\forall \alpha \in M ^ { * }$ , there exists

$$
\begin{array} { r l } & { \beta _ { 1 } = \left[ \begin{array} { c c } { I _ { 2 n } } & { P } \\ { O } & { I _ { 2 n } } \end{array} \right] \in S p ( 4 n ) , } \\ & { \beta _ { 2 } = \left[ \begin{array} { c c } { \left( T ^ { - 1 } \right) ^ { \mathrm { T } } } & { O } \\ { O } & { T } \end{array} \right] \in S p ( 4 n ) , \quad | T | \neq 0 , } \end{array}
$$

such that $\beta _ { 2 } \beta _ { 1 } \alpha \in M ^ { \prime }$ .

Proof. We need only to take $P = - F _ { \alpha } E _ { \alpha } ^ { - 1 } = - ( A _ { \alpha } + B _ { \alpha } ) ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } , T = E _ { \alpha } ^ { - 1 } ,$ then

$$
\begin{array} { r l } { \beta _ { 2 } \beta _ { 1 } \alpha ~ = ~ } & { \left[ \begin{array} { l l } { E _ { \alpha } ^ { \top } } & { O } \\ { O } & { E _ { \alpha } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c c } { I } & { - F _ { \alpha } E _ { \alpha } ^ { - 1 } } \\ { O } & { I } \end{array} \right] \left[ \begin{array} { c c } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } \\ { ~ } & { = ~ \left[ \begin{array} { l l } { A _ { \beta _ { 2 } \beta _ { 1 } \alpha } } & { B _ { \beta _ { 2 } \beta _ { 1 } \alpha } } \\ { C _ { \beta _ { 2 } \beta _ { 1 } \alpha } } & { D _ { \beta _ { 2 } \beta _ { 1 } \alpha } } \end{array} \right] } \\ { ~ } & { = ~ \alpha _ { 1 } = \left[ \begin{array} { c c } { E _ { \alpha } ^ { \prime } ( A _ { \alpha } - F _ { \alpha } E _ { \alpha } ^ { - 1 } C _ { \alpha } ) } & { E _ { \alpha } ^ { \prime } ( B _ { \alpha } - F _ { \alpha } E _ { \alpha } ^ { - 1 } D _ { \alpha } ) } \\ { E _ { \alpha } ^ { - 1 } C _ { \alpha } } & { E _ { \alpha } ^ { - 1 } D _ { \alpha } } \end{array} \right] . } \end{array}
$$

It’s easy to verify that

$$
A _ { \beta _ { 2 } \beta _ { 1 } \alpha } + B _ { \beta _ { 2 } \beta _ { 1 } \alpha } = O _ { 2 n } , \quad C _ { \beta _ { 2 } \beta _ { 1 } \alpha } + D _ { \beta _ { 2 } \beta _ { 1 } \alpha } = I _ { 2 n } .
$$

The theorem is proved.

From now on we will assume $\alpha$ is a normalized Darboux transformation unless it is specified otherwise.

Theorem 2.3. A Darboux transformation can be written in the standard form as

$$
\alpha = \left[ \begin{array} { c c } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } ( I + V ) } & { \frac { 1 } { 2 } ( I - V ) } \end{array} \right] , \quad V \in s p ( 2 n ) .
$$

Proof. It’s not difficult to show:

$$
\forall \alpha _ { 1 } \in M \Longrightarrow \exists \beta \in S p ( 4 n ) , \quad \beta = \left[ \begin{array} { l l } { A _ { \beta } } & { B _ { \beta } } \\ { C _ { \beta } } & { D _ { \beta } } \end{array} \right] ,
$$

such that $\alpha _ { 1 } = \beta$ , where $\alpha _ { 0 }$ is a Poincare transformation. After computation, we get ´

$$
\alpha _ { 1 } = \left[ \begin{array} { c c } { { A _ { \beta } J _ { 2 n } + \frac { 1 } { 2 } B _ { \beta } } } & { { - A _ { \beta } J _ { 2 n } + \frac { 1 } { 2 } B _ { \beta } } } \\ { { } } & { { } } \\ { { C _ { \beta } J _ { 2 n } + \frac { 1 } { 2 } D _ { \beta } } } & { { - C _ { \beta } J _ { 2 n } + \frac { 1 } { 2 } D _ { \beta } } } \end{array} \right] .
$$

Because $\alpha _ { 1 } \in M ^ { \prime }$ , we have $D _ { \beta } = I _ { 2 n }$ ! $B _ { \beta } = O$ , i.e., $\beta = \left[ \begin{array} { c c } { { A _ { \beta } } } & { { O } } \\ { { C _ { \beta } } } & { { I _ { 2 n } } } \end{array} \right]$ . Since $\beta \in S p ( 4 n )$ , we have $\beta = \left[ \begin{array} { c c } { { I _ { 2 n } } } & { { O } } \\ { { Q } } & { { I _ { 2 n } } } \end{array} \right]$ $Q \in S m ( 2 n )$ . Thus:

$$
\begin{array} { r l } { \alpha _ { 1 } } & { = \left[ \begin{array} { l l } { I _ { 2 n } } & { O } \\ { Q } & { I _ { 2 n } } \end{array} \right] \left[ \begin{array} { l l } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } I _ { 2 n } } & { \frac { 1 } { 2 } I _ { 2 n } } \end{array} \right] } \\ & { = \left[ \begin{array} { l l } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } I _ { 2 n } + Q J _ { 2 n } } & { \frac { 1 } { 2 } I _ { 2 n } - Q J _ { 2 n } } \end{array} \right] } \\ & { = \left[ \begin{array} { l l } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } ( I _ { 2 n } + V ) } & { \frac { 1 } { 2 } ( I _ { 2 n } - V ) } \end{array} \right] , } \end{array}
$$

where $Q ^ { \prime } = Q , V = 2 Q J .$ We shall write

$$
\alpha _ { V } = \left[ \begin{array} { c c } { { J _ { 2 n } } } & { { - J _ { 2 n } } } \\ { { } } & { { } } \\ { { \frac 1 2 ( I _ { 2 n } + V ) } } & { { \frac 1 2 ( I _ { 2 n } - V ) } } \end{array} \right] , \quad \alpha _ { V } ^ { - 1 } = \left[ \begin{array} { c c } { { - \frac 1 2 ( I _ { 2 n } - V ) } } & { { I _ { 2 n } } } \\ { { } } & { { } } \\ { { \frac 1 2 ( I _ { 2 n } + V ) } } & { { I _ { 2 n } } } \end{array} \right] .
$$

Therefore, the theorem is completed.

Corollary 2.4. Every $\alpha = \left[ \begin{array} { c c } { { A _ { \beta } } } & { { B _ { \beta } } } \\ { { C _ { \beta } } } & { { D _ { \beta } } } \end{array} \right] \in M ^ { * }$ has a normalized Darboux form

$$
\alpha _ { V } \in M ^ { \prime } , \quad V = ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } ( C _ { \alpha } - D _ { \alpha } ) \in s p ( 2 n ) .
$$

This result can be derived from (2.1).

From the following theorem, we can show that the normalization condition is natural.

Theorem 2.5. Let $G ^ { \tau }$ be a consistent difference scheme for equation $\dot { z } = J ^ { - 1 } H _ { z }$ , i.e.,

$1 ^ { \circ }$ $G ^ { \tau } ( z ) | _ { \tau = 0 } = z , \forall z , H .$

$$
\begin{array} { r l } { 2 ^ { \circ } } & { { } \frac { \partial G ^ { \tau } ( z ) } { \partial \tau } \Big | _ { \tau = 0 } = J ^ { - 1 } M _ { z } , \forall z , H . } \end{array}
$$

iff the generating Darboux transformation is normalized with $A = - J$ .

Proof. We take symplectic difference scheme of first order via generating function of type ${ \overset { \vartriangle } { \alpha } } = { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] }$ , we have

$$
A G ^ { \tau } ( z ) + B z = - \tau H _ { z } ( C G ^ { \tau } ( z ) + D z ) .
$$

We first prove the “ only if ” part of the theorem. When taking $\tau = 0$ , we have

$$
A G ^ { 0 } ( z ) + B z = ( A + B ) z = 0 , \quad \forall ~ z \Longrightarrow A + B = O .
$$

Differentiating (2.2) yields

$$
A \frac { \partial G ^ { \tau } ( z ) } { \partial \tau } \Big | _ { \tau = 0 } = - H _ { z } ( ( C + D ) z ) .
$$

Since

$$
\Big ( \frac { \partial G ^ { \tau } ( z ) } { \partial \tau } \Big ) \Big | _ { \tau = 0 } = J ^ { - 1 } H _ { z } ( z ) ,
$$

we have

$$
A J ^ { - 1 } H _ { z } ( z ) = - H _ { z } ( ( C + D ) z ) , \quad \forall \ H , z .
$$

Take special form $H ( z ) = z ^ { \mathrm { T } } b$ , and substitute it into above equation, we have

$$
\boldsymbol { A } \boldsymbol { J } ^ { - 1 } \boldsymbol { b } = - \boldsymbol { b } , \quad \forall \ \boldsymbol { b } ,
$$

which results in $A = - J$ .

On the other hand, since $H _ { z } ( z ) \ = \ H _ { z } ( ( C + D ) z ) , \forall \ H , z$ take special form $H = \frac { 1 } { 2 } z ^ { \mathrm { T } } z$ , and substitute it into the above equation, we get

$$
z = ( C + D ) z , \quad \forall z \Longrightarrow C + D = I .
$$

Now we prove the “ if ” part. Take

$$
A + B = O , \quad A = - J , \quad C + D = I ,
$$

then

$$
\begin{array} { c } { { A ( G ^ { \tau } ( z ) - z ) = - \tau H _ { z } ( C G ^ { \tau } ( z ) + D z ) , } } \\ { { \ } } \\ { { A = - J , \quad \tau = 0 \Longrightarrow G ^ { \tau } ( z ) \big \vert _ { \tau = 0 } = z . } } \end{array}
$$

On the other hand, we have

$$
A \left. \left( \frac { \partial G ^ { \tau } ( z ) } { \partial \tau } \right) \right| _ { \tau = 0 } = - H _ { z } ( ( C + D ) z ) \Longrightarrow \left. \left( \frac { \partial G ^ { \tau } ( z ) } { \partial \tau } \right) \right| _ { \tau = 0 } = J ^ { - 1 } H _ { z } ( z ) , \quad \forall \ z , H _ { \tau } ( z ) = 0 ,
$$

Therefore, the theorem is completed.

Theorem 2.6. A normalized Darboux transformation with $A = - J$ can be written in the standard form

$$
\alpha = \left[ \begin{array} { c c } { - J } & { J } \\ { \frac { 1 } { 2 } ( I - V ) } & { \frac { 1 } { 2 } ( I + V ) } \end{array} \right] , \quad \forall V \in s p ( 2 n ) .
$$

# 6.3 Transform Properties of Generator Maps and Generating Functions

Let

$$
\alpha = \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) ,
$$

denote $E _ { \alpha } = C _ { \alpha } + D _ { \alpha }$ , $F _ { \alpha } = A _ { \alpha } + B _ { \alpha }$ . Let $g \in S p$ -diff. From now on, we always assume that transversality condition is satisfied, i.e., $| E _ { \alpha } | \neq 0$ .

${ \bf e o r e m 3 . 1 . ~ \forall ~ } T ~ \in ~ G L ( 2 n ) , \ L e t \ \beta _ { T } \ = ~ \left[ \begin{array} { c c } { { ( T ^ { - 1 } ) ^ { \mathrm { T } } } } & { { O } } \\ { { O } } & { { T } } \end{array} \right] ~ \in ~ S p ( 4 n ) , \ \beta _ { T } \alpha ~ \in ~ { \mathrm { T } } ,$ $S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$

$$
\phi _ { \beta _ { T } \alpha , g } \cong \phi _ { \alpha , g } \circ T ^ { - 1 } .
$$

Proof. Since

$$
\beta _ { T } \boldsymbol \alpha = \left[ \begin{array} { c c } { \left( T ^ { - 1 } \right) ^ { \operatorname { T } } A _ { \boldsymbol \alpha } } & { \left( T ^ { - 1 } \right) ^ { \operatorname { T } } B _ { \boldsymbol \alpha } } \\ { T C _ { \boldsymbol \alpha } } & { T D _ { \boldsymbol \alpha } } \end{array} \right] = \left[ \begin{array} { c c } { A _ { \beta _ { T } \boldsymbol \alpha } } & { B _ { \beta _ { T } \boldsymbol \alpha } } \\ { C _ { \beta _ { T } \boldsymbol \alpha } } & { D _ { \beta _ { T } \boldsymbol \alpha } } \end{array} \right] ,
$$

we have

$$
A _ { \alpha } g ( z ) + B _ { \alpha } z = \nabla \phi _ { \alpha , g } \circ ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) ,
$$

and

$$
\begin{array} { r l r } { \left( T ^ { - 1 } \right) ^ { \mathrm { T } } A _ { \alpha } g ( z ) + \left( T ^ { - 1 } \right) ^ { \mathrm { T } } B _ { \alpha } z } & { = } & { \nabla \phi _ { \beta _ { T } \alpha , g } \circ ( T C _ { \alpha } g ( z ) + T D _ { \alpha } z ) \quad } \\ { \iff A _ { \alpha } g ( z ) + B _ { \alpha } z } & { = } & { T ^ { \prime } ( \nabla \phi _ { \beta _ { T } \alpha , g } ) \circ T ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) } \\ & { = } & { \nabla ( \phi _ { \beta _ { T } \alpha , g } \circ T ) ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) . \quad } \end{array}
$$

Comparing (3.2) with (3.3) for all $z$ , we find:

$$
\nabla \phi _ { \alpha , g } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) = \nabla ( \phi _ { \beta _ { T } \alpha , g } \circ T ) ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) .
$$

Thus we obtain

$$
\phi _ { \alpha , g } \cong \phi _ { \beta _ { T } \alpha , g } \circ T
$$

or

$$
\phi _ { \alpha , g } \circ T ^ { - 1 } \cong \phi _ { \beta _ { T } \alpha , g }
$$

The theorem is proved.

Theorem 3.2. $\forall S \in S p ( 2 n )$ , define $\gamma _ { S } = \left[ \begin{array} { c c } { { S } } & { { O } } \\ { { O } } & { { S } } \end{array} \right] \in \widetilde { S } p ( 4 n )$ . Then we have

$$
\phi _ { \alpha \gamma _ { S } , g } \cong \phi _ { \alpha , S \circ g \circ S ^ { - 1 } }
$$


<!-- chunk 0005: pages 281-350 -->
Proof. Since:

$$
\alpha \gamma _ { S } = \left[ \begin{array} { c c } { { A _ { \alpha } S } } & { { B _ { \alpha } S } } \\ { { } } & { { } } \\ { { C _ { \alpha } S } } & { { D _ { \alpha } S } } \end{array} \right] = \left[ \begin{array} { c c } { { A _ { \alpha } \gamma _ { S } } } & { { B _ { \alpha } \gamma _ { S } } } \\ { { } } & { { } } \\ { { C _ { \alpha } \gamma _ { S } } } & { { D _ { \alpha } \gamma _ { S } } } \end{array} \right] ,
$$

we have

$$
A _ { \alpha } S \circ g \circ S ^ { - 1 } z + B _ { \alpha } z = \nabla \phi _ { \alpha , S \circ g \circ S ^ { - 1 } } ( C _ { \alpha } S \circ g \circ S ^ { - 1 } z + D _ { \alpha } z ) .
$$

Since $S$ is nonsingular, replacing $z$ with $S ( z )$ results in

$$
A _ { \alpha } S \circ g ( z ) + B _ { \alpha } S z = \nabla \phi _ { \alpha , S \circ g \circ S ^ { - 1 } } ( C _ { \alpha } S \circ g ( z ) + D _ { \alpha } S z ) , \quad \forall z .
$$

On the other hand,

$$
( A _ { \alpha } S ) g ( z ) + ( B _ { \alpha } S ) z = \nabla \phi _ { \alpha \gamma _ { S } , g } [ ( C _ { \alpha } S ) g ( z ) + D _ { \alpha } S z ] , \quad \forall z .
$$

Compare (3.5) with (3.6) and note that

$$
| C _ { \alpha } + D _ { \alpha } | \neq 0 \Longleftrightarrow | C _ { \alpha } S + D _ { \alpha } S | \neq 0 \Longleftrightarrow | C _ { \alpha } S g _ { z } ( z ) + D _ { \alpha } S | \neq 0 .
$$

Finally, we obtain:

$$
\nabla \phi _ { \alpha \gamma S , g } = \nabla \phi _ { \alpha , S \circ g \circ S ^ { - 1 } } ,
$$

i.e.,

$$
\phi _ { \alpha \gamma S , g } \cong \phi _ { \alpha , S \circ g \circ S ^ { - 1 } } .
$$

The proof can be obtained.

Theorem 3. $3 . \ T a k e \ \beta = \left[ \begin{array} { c c } { { I _ { 2 n } } } & { { P } } \\ { { O } } & { { I _ { 2 n } } } \end{array} \right] \in S p ( 4 n ) , \ P \in S m ( 2 n ) , \ \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) ,$

$$
\phi _ { \beta \alpha , g } \cong \phi _ { \alpha , g } + \psi _ { p } ,
$$

where $\psi _ { p } = { \frac { 1 } { 2 } } w ^ { \prime } P w$ ( function independent of $g$ ).

Proof. Since:

$$
\beta \alpha = \left[ \begin{array} { c c } { { I _ { 2 n } } } & { { P } } \\ { { O } } & { { I _ { 2 n } } } \end{array} \right] \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { A _ { \alpha } + P C _ { \alpha } } } & { { B _ { \alpha } + P D _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] ,
$$

$$
E _ { \beta \alpha } = E _ { \alpha } , \quad F _ { \beta \alpha } = F _ { \alpha } + P E _ { \alpha } ,
$$

obviously,

$$
\begin{array} { r l } & { A _ { \beta \alpha } g ( z ) + B _ { \beta \alpha } z = \nabla \phi _ { \beta \alpha , g } ( C _ { \beta \alpha } g ( z ) + D _ { \beta \alpha } z ) , } \\ & { A _ { \alpha } g ( z ) + B _ { \alpha } z + ( P C _ { \alpha } g ( z ) + P D _ { \alpha } z ) = \nabla \phi _ { \beta \alpha , g } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) . } \end{array}
$$

On the other hand,

$$
\nabla \psi _ { P } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) = P ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) .
$$

Inserting (3.10) into (3.9), we obtain

$$
\begin{array} { l l l } { { A _ { \alpha } g ( z ) + B _ { \alpha } z \ = \ \nabla \phi _ { \beta \alpha , g } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) - \nabla \psi _ { P } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) } } \\ { { \ } } & { { \ } } \\ { { \ } } & { { \ = \ \nabla ( \phi _ { \beta \alpha , g } - \psi _ { P } ) ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) . } } \end{array}
$$

Compare (3.11) with

$$
A _ { \alpha } g ( z ) + B _ { \alpha } z = \nabla \phi _ { \alpha , g } ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) ,
$$

we obtain

$$
\phi _ { \beta \alpha , g } - \psi _ { P } \cong \phi _ { \alpha , g } .
$$

Analogically, we have:

Theorem 3.4. If we take $\beta = \left[ \begin{array} { c c } { { I _ { 2 n } } } & { { O } } \\ { { Q } } & { { I _ { 2 n } } } \end{array} \right] \in S p ( 4 n ) , Q \in S m ( 2 n )$

$$
\phi _ { \alpha , g } + \frac { 1 } { 2 } ( \nabla _ { w } \phi _ { \alpha , g } ( w ) ) ^ { \prime } Q ( \nabla _ { w } \phi _ { \alpha , g } ( w ) ) \cong \phi _ { \beta \alpha , g } ( w + Q \nabla \phi _ { \alpha , g } ( w ) ) .
$$

Theorem 3.5. We have the following relation:

$$
{ \phi } ^ { \phi } { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } , g ^ { - 1 } { \overbrace { g ^ { - 1 } } ^ { \cong - \phi } } { \left[ \begin{array} { l l } { - B } & { - A } \\ { D } & { C } \end{array} \right] } , g
$$

Proof. Since

$$
A _ { \alpha } g ^ { - 1 } ( z ) + B _ { \alpha } z = \nabla \phi _ { \alpha , g ^ { - 1 } } ( C _ { \alpha } g ^ { - 1 } ( z ) + D _ { \alpha } z ) ,
$$

replacing $z$ with $g ( z )$ yields

$$
A _ { \alpha } z + B _ { \alpha } g ( z ) = \nabla \phi _ { \alpha , g ^ { - 1 } } ( C _ { \alpha } z + D _ { \alpha } g ( z ) ) .
$$

Comparing (3.14) with

$$
- B _ { \alpha } g ( z ) - A _ { \alpha } z = \nabla \phi _ { \left[ \begin{array} { c c } { - B } & { - A } \\ { D } & { C } \end{array} \right] , g } ( D _ { \alpha } g ( z ) + C _ { \alpha } z ) ,
$$

the proof is complete.

# Theorem 3.6. If

$$
\begin{array} { r } { \phi ^ { } } \\ { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , g ^ { - 1 } \left[ \begin{array} { l l } { \underline { { \omega } } - \phi } \\ { C } & { D } \end{array} \right] , g ^ { - 1 } \ } \end{array} , \quad \forall \ ,
$$

then

$$
A + B = O , \quad C = D .
$$

Proof. By Theorem 3.5 and the uniqueness of Darboux transformation in Theorem 4.2, we have

$$
\left[ \begin{array} { c c } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right] = \pm \left[ \begin{array} { c c } { { - B } } & { { - A } } \\ { { D } } & { { C } } \end{array} \right] .
$$

We only consider the case “ $+ ^ { \dag }$ , where we have $A + B = O$ , $C = D$ .

Remark 3.7. For Poincare map ´ $\alpha _ { 0 } = { \left[ \begin{array} { l l } { J } & { - J } \\ { { \frac { 1 } { 2 } } I } & { { \frac { 1 } { 2 } } I } \end{array} \right] } ,$ , we have:

$$
\phi _ { \alpha _ { 0 } , g ^ { - 1 } } \cong - \phi _ { \alpha _ { 0 } , g } , \quad \forall g \in S p \ – d i f f .
$$

Theorem 3.8. Let $g _ { H } ^ { t }$ be the phase flow of Hamiltonian system $H ( z )$ . Then under Poincare map ´ $\alpha _ { 0 }$ the generating function for $g _ { H } ^ { t }$ is an odd function w.r.t $t$ , i.e.,

$$
\phi _ { \alpha _ { 0 } , g _ { H } ^ { t } } ( w , t ) = - \phi _ { \alpha _ { 0 } , g _ { H } ^ { t } } ( w , - t ) , \quad \forall ~ w \in { \bf R } ^ { 2 n } , \quad t \in { \bf R } .
$$

Proof. By the properties of generating function for $g _ { H } ^ { t }$ , we have

$$
\begin{array} { l } { { g _ { H } ^ { - t } = ( g _ { H } ^ { t } ) ^ { - 1 } , } } \\ { { \ } } \\ { { \phi _ { \alpha _ { 0 } , g _ { H } ^ { - t } } ( w , t ) = \phi _ { \alpha _ { 0 } , g _ { H } ^ { t } } ( w , - t ) = \phi _ { \alpha _ { 0 } , ( g _ { H } ^ { t } ) ^ { - 1 } } ( w , t ) = - \phi _ { \alpha _ { 0 } , g _ { H } ^ { t } } ( w , t ) . } } \end{array}
$$

The theorem is proved.

Theorem 3.9. If $S \in S p ( 2 n ) , \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \gamma _ { 1 } = \left[ \begin{array} { l l } { S } & { O } \\ { O } & { I } \end{array} \right] , t h e n$

$$
\begin{array} { r } { \alpha \gamma _ { 1 } = \left[ \begin{array} { l l } { A _ { \alpha } S } & { B _ { \alpha } } \\ { C _ { \alpha } S } & { D _ { \alpha } } \end{array} \right] . } \end{array}
$$

Assume $| E _ { \alpha \gamma _ { 1 } } | = | C _ { \alpha } S + D _ { \alpha } | \neq 0$ , we have

$$
\phi _ { \alpha , S \circ g } \cong \phi _ { \alpha \gamma _ { 1 } , g } ,
$$

i.e.,

$$
\phi _ { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , S \circ g } \cong \phi _ { \left[ \begin{array} { l l } { A S } & { B } \\ { C S } & { D } \end{array} \right] , g } .
$$

Theorem 3.10. If

$$
\gamma _ { 2 } = \left[ \begin{array} { c c } { { I } } & { { O } } \\ { { O } } & { { S } } \end{array} \right] , \quad \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \alpha \gamma _ { 2 } = \left[ \begin{array} { c c } { { A } _ { \alpha } } & { { B } _ { \alpha } { S } } \\ { { C } _ { \alpha } } & { { D } _ { \alpha } { S } } \end{array} \right] ,
$$

assume $| B _ { \alpha } + D _ { \alpha } S | \neq 0$ , we have

$$
\phi _ { \alpha , g \circ S ^ { - 1 } } \cong \phi _ { \alpha \gamma _ { 2 } , g } ,
$$

i.e.,

$$
{ } ^ { \phi } { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } , g \circ S ^ { - 1 } { \stackrel { \cong } { = } } \phi { \left[ \begin{array} { l l } { A } & { B S } \\ { C } & { D S } \end{array} \right] } , g \qquad 
$$

Proof. Since

$$
A g ( S ^ { - 1 } z ) + B z = \nabla \phi _ { \alpha , g \circ S ^ { - 1 } } \big ( C g ( S ^ { - 1 } z ) + D z \big ) , \quad \forall z ,
$$

replacing $z$ with $S z$ yields

$$
\begin{array} { r l } { A g ( z ) + B S z } & { = \nabla \phi _ { \alpha , g \circ S ^ { - 1 } } ( C g ( z ) + D S z ) } \\ & { = \nabla \phi _ { \left[ \begin{array} { l l } { A } & { B S } \\ { C } & { D S } \end{array} \right] , g } ( C g ( z ) + D S z ) , } \end{array}
$$

$$
\begin{array} { l } { \phi _ { } { \rho } _ { } { \left[ \begin{array} { l l } { A } & { B S } \\ { C } & { D S } \end{array} \right] , g } ^ { } \cong \phi _ { } { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } , g \circ S ^ { - 1 } } \end{array} .
$$

Therefore, the theorem is completed.

The proof of Theorem 3.9 is similar.

Theorem 3.11. If

$$
\beta = \left[ \begin{array} { c c } { \lambda I _ { 2 n } } & { O } \\ { O } & { I _ { 2 n } } \end{array} \right] \in C S p ( 4 n ) , \quad \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \lambda \neq 0 ,
$$

$$
\beta \alpha = \left[ \begin{array} { c c } { { \lambda A } } & { { \lambda B } } \\ { { C } } & { { D } } \end{array} \right] \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \mu ( \beta \alpha ) = \lambda ,
$$

then we have

$$
\begin{array} { c c } { { \phi _ { } } } & { { { } } } & { { { \bf \nabla } \lambda A { \bf \quad } \lambda B { \bf \sigma } } } \\ { { { } } } & { { { \bf \nabla } C { \bf \quad } D { \bf \sigma } } } \end{array} \biggr ] , g { \bf \sigma }  ^ { \cong \lambda \phi } { \left[ \begin{array} { l l } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right] } , g
$$

Proof. Since

$$
\begin{array}{c} \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) \Longrightarrow A g ( z ) + B z = \nabla \phi  \\ { \alpha \in S p ( \widetilde { J } _ { 4 n } , B _ { \mathbf { \Gamma } } ] , g } \end{array} ( C g ( z ) + D z ) ,
$$

$$
\beta \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) \Longrightarrow \lambda A g ( z ) + \lambda B z = \nabla \phi  \\  \left[ \begin{array} { c c } { { \lambda A } } & { { \lambda B } } \\ { { C } } & { { D } } \end{array} \right] , q ^ { ( C g ( z ) + D z ) }
$$

$$
\begin{array} { r } { \mathrm { L . H . S } = \lambda A g ( z ) + \lambda B z = \lambda \nabla \phi } \\ { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , g } \end{array} ( C g ( z ) + D z ) ,
$$

$$
\begin{array} { r } { \mathrm { R . H . S } = \nabla \phi { } } \\ { C \quad \boldsymbol { D } } \end{array} \bigg [ \begin{array} { c c } { ( C g ( z ) + D z ) , } \\ { \boldsymbol { C } } \end{array}
$$

then we have

$$
\begin{array} { r l } { \nabla \phi } \\ { \left[ \begin{array} { l l } { \lambda A } & { \lambda B } \\ { C } & { D } \end{array} \right] , \ L _ { g } ^ { ( C g ( z ) + D z ) = \lambda \nabla \phi } \Big [ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \Big ] , \ L _ { g } ^ { ( C g ( z ) + D z ) , } } \\ { \phi _ { \left[ \begin{array} { l l } { \lambda A } & { \lambda B } \\ { C } & { D } \end{array} \right] , \ L _ { g } ^ { \cong } } \ L _ { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , \ L _ { g } } ^ { \cong \lambda \phi } \ L _ { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , \ L _ { g } ^ { \ * } } . } \end{array}
$$

The theorem is proved.

Theorem 3.12. Let

$$
\beta = \left[ \begin{array} { c c } { I _ { 2 n } } & { O } \\ { O } & { \lambda I _ { 2 n } } \end{array} \right] \in C S p ( J _ { 4 n } ) , \quad \lambda \neq 0 , \quad \alpha \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) ,
$$

$$
\beta \alpha = \left[ \begin{array} { c c } { { A } } & { { B } } \\ { { \lambda C } } & { { \lambda D } } \end{array} \right] \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \mu ( \beta \alpha ) = \lambda ,
$$

then we have:

$$
\begin{array}{c} \begin{array} { l } { \phi } \\ { \left[ \begin{array} { l l } { A } & { B } \\ { \lambda C } & { \lambda D } \end{array} \right] , g } \end{array} \overset { \cong } \lambda \phi  \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , g \overset { \circ } { \mathrm { \partial } } \lambda ^ { - 1 } I _ { 2 n } .  \end{array}
$$

Proof. Since

$$
\begin{array} { r l } & { \left[ \begin{array} { c c } { A } & { B } \\ { A G } & { \lambda D } \end{array} \right] \in C S \wp ( \hat { \mathcal { A } } _ { 1 , \infty } , J _ { \infty } ) , } \\ &  \begin{array} { r } { A g ( z ) + B z = \operatorname { C S } \ng { \hat { \sigma } } _ { \left[ \begin{array} { c c } { A } & { B } \\ { A C } & { \lambda D } \end{array} \right] } \in \Lambda ^ { \mathrm { O C } } \wp ( z ) + \lambda D z \mapsto \downarrow , } \\ { \operatorname { L e t } S = \operatorname { P } \ng { \hat { \sigma } } _ { \left[ \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} \right] } \stackrel { ( C S \cup \mathcal { A } _ { 2 } ) - D ( z ) - \lambda \in \mathcal { O } } { \operatorname { P o r } { \hat { \sigma } } _ { \left[ \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} \right] } } \end{array} , } \\ &  \begin{array} { r }  \operatorname { R e t } S = \left( \oint _ { \left[ \begin{array} { c c } { A } & { B } \\ { A C } & { \lambda D } \end{array} \right] \ldots \right) \circ M \underline { { \hat { \sigma } } } _ { \alpha , \beta } ( C \wp ( z ) + D \hbar \hbar ) } \\ { \operatorname { R e t } S = \left( \oint _ { \left[ \begin{array} { c c } { A } & { B } \\ { A C } & { \lambda D } \end{array} \right] \ldots  \circ M \underline { { \hat { \sigma } } } _ { \alpha , \beta } ( C \wp ( z ) + D \hbar ) } \end{array} } \\ & \right) \begin{array} { r }  \operatorname { R e t } S = \left( \oint _ { \left[ \begin{array} { c c } { A } & { B } \\ { A C } & { \lambda D } \end{array} \right] \ldots \right) \circ S \hbar , } \\ { \operatorname { R e t } S = \left( \oint _ { \left[ \begin{array} { c c } { A } & { B } \\ { A C } & { \lambda D } \end{array} \right] \ldots  \circ S \hbar . } \end{array} } \end{\right)array} \end{array}
$$

hence

$$
{ \begin{array} { l } { \phi } \\ { { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } , g } \end{array} } \cong \lambda ^ { - 1 } \phi  { \left[ \begin{array} { l l } { \ A } & { B } \\ { \lambda C } & { \lambda D } \end{array} \right] } , g \ \mathrm { \ } { \mathrm { { \Omega } } } ^ { \circ } \lambda I _ { 2 n } .
$$

Therefore, the theorem is completed.

Before finishing this section, we will give two conclusive theorems which can include the contents of the seven theorems given before. They are easy to prove and the proofs are omitted here.

$$
\alpha \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \beta \in C S p ( J _ { 4 n } ) , \quad \beta = \left[ \begin{array} { c c } { a } & { b } \\ { c } & { d } \end{array} \right] ,
$$

obviously

$$
\beta \alpha \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \quad \mu ( \beta \alpha ) = \lambda ( \beta ) \mu ( \alpha ) ,
$$

and then the following theorem.

Theorem 3.13. For $\phi _ { \beta \alpha , g }$ , we have

$$
\begin{array} { r l } & { \phi _ { \beta \alpha , g } ( c \nabla _ { w } \phi _ { \alpha , g } ( w ) + d w ) } \\ & { \cong \lambda ( \beta ) \phi _ { \alpha , g } ( w ) + \left\{ \displaystyle \frac { 1 } { 2 } w ^ { \prime } ( d ^ { \prime } b ) w + ( \nabla _ { w } \phi _ { \alpha , g } ( w ) ) ^ { \prime } \right. } \\ & { \quad \left. \cdot ( c ^ { \prime } b ) w \displaystyle \frac { 1 } { 2 } ( \nabla _ { w } \phi _ { \alpha , g } ( w \lambda ) ) ^ { \prime } ( c ^ { \prime } a ) ( \nabla _ { w } \phi _ { \alpha , g } ( w ) ) \right\} . } \end{array}
$$

We now formulate the other one. Let $\alpha \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \gamma \in C S p ( \widetilde { J } _ { 4 n } ) \Leftrightarrow$ $\gamma ^ { \prime } \widetilde { J } _ { 4 n } \gamma = \nu ( \gamma ) \widetilde { J } _ { 4 n } \Rightarrow \alpha \gamma \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) , \mu ( \alpha \gamma ) = \mu ( \alpha ) \nu ( \gamma ) ,$ $\gamma = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } .$ We have the following theorem.

Theorem 3.14. For $\phi _ { \alpha \gamma , g }$ , we have

$$
\phi _ { \alpha \gamma , g } \cong \phi _ { \alpha , ( a g + b ) ( c g + d ) ^ { - 1 } } .
$$

# 6.4 Invariance of Generating Functions and Commutativity of Generator Maps

First we present the uniqueness theorem of the linear fractional transformation.

Theorem 4.1. Let

$$
\alpha = \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ & { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] , \quad \overline { { \alpha } } = \left[ \begin{array} { l l } { A _ { \overline { { \alpha } } } } & { B _ { \overline { { \alpha } } } } \\ { C _ { \overline { { \alpha } } } } & { D _ { \overline { { \alpha } } } } \end{array} \right] \in S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } ) ,
$$

If

$$
\begin{array} { c } { { ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } = ( A _ { \overline { { { \alpha } } } } M + B _ { \overline { { { \alpha } } } } ) ( C _ { \overline { { { \alpha } } } } M + D _ { \overline { { { \alpha } } } } ) ^ { - 1 } , } } \\ { { \forall \ M \sim I _ { 2 n } , \quad M \in S p ( 2 n ) , } } \end{array}
$$

then

$$
\overline { { \alpha } } = \pm \alpha .
$$

Proof. Let

$$
\begin{array} { l l } { { N _ { 0 } = ( A _ { \alpha } I + B _ { \alpha } ) ( C _ { \alpha } I + D _ { \alpha } ) ^ { - 1 } } } \\ { { { } } } \\ { { = ( A _ { \overline { { { \alpha } } } } I + B _ { \overline { { { \alpha } } } } ) ( C _ { \overline { { { \alpha } } } } I + D _ { \overline { { { \alpha } } } } ) ^ { - 1 } . } } \end{array}
$$

Suppose $\beta \in S p ( 4 n )$ , first we prove that if

$$
( A _ { \beta } N + B _ { \beta } ) ( C _ { \beta } N + D _ { \beta } ) ^ { - 1 } = N , \quad \forall \ N \sim N _ { 0 } , \quad N \in S m ( 2 n ) ,
$$

then $\beta = \pm I _ { 4 n }$ . Now we have two cases:

$2 ^ { \circ }$ $\begin{array} { r l } & { \beta ^ { N _ { 0 } } + B _ { \beta } ) ( C _ { \beta } N _ { 0 } + D _ { \beta } ) ^ { - 1 } = N _ { 0 } \Rightarrow A _ { \beta } N _ { 0 } + B _ { \beta } = N _ { 0 } C _ { \beta } N _ { 0 } + N _ { 0 } D _ { \beta } . } \\ & { \ker N = N _ { 0 } + \varepsilon I \Rightarrow A _ { \beta } ( N _ { 0 } + \varepsilon I ) + B _ { \beta } = ( N _ { 0 } + \varepsilon I ) C _ { \beta } ( N _ { 0 } + \varepsilon I ) + } \end{array}$ $( N _ { 0 } + \varepsilon I ) D _ { \beta }$ .

From $1 ^ { \circ }$ , $2 ^ { \circ } \ \Rightarrow \varepsilon A _ { \beta } = \varepsilon N _ { 0 } C _ { \beta } + \varepsilon C _ { \beta } N _ { 0 } + \varepsilon D _ { \beta } + \varepsilon ^ { 2 } C _ { \beta } , \forall \varepsilon .$ , which results in

$$
A _ { \beta } - D _ { \beta } - N _ { 0 } C _ { \beta } - C _ { \beta } N _ { 0 } = \varepsilon C _ { \beta } = 0 \Longrightarrow C _ { \beta } = 0 ,
$$

thus $A _ { \beta } = D _ { \beta }$

$1 ^ { \circ }$ e have $B = \left[ \begin{array} { c c } { { A _ { \beta } } } & { { B _ { \beta } } } \\ { { O } } & { { A _ { \beta } } } \end{array} \right]$ $B _ { \beta } = B _ { \beta } ^ { \prime }$

$$
A _ { \beta } N A _ { \beta } ^ { - 1 } = N - B _ { \beta } A _ { \beta } ^ { - 1 } .
$$

Subtracting this formula by $A _ { \beta } N _ { 0 } A _ { \beta } ^ { - 1 } = N _ { 0 } - B _ { \beta } A _ { \beta } ^ { - 1 }$ yields

$$
A _ { \beta } ( N - N _ { 0 } ) = ( N - N _ { 0 } ) A _ { \beta } .
$$

Take $N - N _ { 0 } = \varepsilon S , \forall S \in S m ( 2 n ) \Rightarrow A _ { \beta } S = S A _ { \beta }$ , $\forall S \in S m ( 2 n ) \Rightarrow A _ { \beta } = \lambda I _ { 2 n }$ (This can be proved by mathematical induction).

Then from $1 ^ { \circ }$ , $A _ { \beta } N _ { 0 } + B _ { \beta } = N _ { 0 } A _ { \beta } \Rightarrow B _ { \beta } = 0$ , and

$$
\beta = { \left[ \begin{array} { l l } { A _ { \beta } } & { O } \\ { O } & { A _ { \beta } } \end{array} \right] } = \lambda I _ { 4 n } \in S p ( 4 n ) \Longrightarrow \lambda = \pm 1 .
$$

Let $\beta = \overline { { \alpha } } \alpha ^ { - 1 }$ , then the fractional transformation of $\beta$ preserves all symmetric $N \sim$ $N _ { 0 }$ . Because $\alpha \in S p ( \widetilde { J } , J )$ , $\alpha ^ { - 1 } \in S p ( J , \widetilde J )$ , we have $\overline { { \alpha } } \alpha ^ { - 1 } \in S p ( J , J ) = S p ( 4 n )$ . The theorem is proved.

We now present the uniqueness theorem for Darboux transformations.

Theorem 4.2. Suppose $\alpha , \overline { { \alpha } } \in S p ( \widetilde { J } , J )$ , then

$$
\phi _ { \alpha , g } \cong \phi _ { \overline { { { \alpha } } } , g } , \quad \forall ~ g \in S p { \cdot } d i f f , \quad g \sim I _ { 2 n } \Longrightarrow \overline { { { \alpha } } } = \pm \alpha .
$$

Proof. From the hypothesis, we have

$$
\begin{array} { r c l } { { \phi _ { \alpha , g } } } & { { \cong } } & { { \phi _ { \overline { { { \alpha } } } , g } \Longrightarrow \mathrm { H e s s i a n } ( \phi _ { \alpha , g } ) = ( \phi _ { \alpha , g } ) _ { w w } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( A _ { \alpha } g ( z ) + B _ { \alpha } ) ( C _ { \alpha } g ( z ) + D _ { \alpha } ) ^ { - 1 } , } } \end{array}
$$

$$
( \phi _ { \overline { { \alpha } } , g } ) _ { w w } = ( A _ { \overline { { \alpha } } } g ( z ) + B _ { \overline { { \alpha } } } ) ( C _ { \overline { { \alpha } } } g ( z ) + D _ { \overline { { \alpha } } } ) ^ { - 1 } , \quad \forall g ( z ) \in S p ( 2 n ) \sim I .
$$

Then by uniqueness theorem of the linear fractional transformation $\alpha = \pm \overline { { \alpha } }$ . From the above proof, we get

$$
\mathrm { H e s s i a n } ( \phi _ { \alpha , g } ) = \mathrm { H e s s i a n } ( \phi _ { - \alpha , g } ) , \quad \forall \ g \in I , \alpha .
$$

The generating function $\phi _ { \alpha , g }$ depends on Darboux transformation $\alpha$ , symplectic diffeomorphism $g$ and coordinates. If we make a symplectic coordinate transformation $w  S ( z )$ , then $\phi ( S ) \Rightarrow \phi ( S ( z ) )$ , while the symplectic diffeomorphism $g$ is represented in $z$ coordinates as $S ^ { - 1 } \circ g \circ S$ , i.e.,

$$
\phi _ { \alpha , S ^ { - 1 } \circ g \circ S } = \phi _ { \alpha , g } \circ S
$$

For the invariance of generating function $\phi _ { g } ( S )$ under $S$ , one would like to expect

$$
\phi _ { \alpha , S ^ { - 1 } \circ g \circ S } = \phi _ { \alpha , g } \circ S , \quad \forall g \sim I .
$$

This is not true in general case. We shall study under what condition this is true for the normalized Darboux transformation $\alpha _ { V }$ . The following theorem answers this question.

# Theorem 4.3. Let

$$
\alpha = \alpha _ { V } = \left[ \begin{array} { c c } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } ( I + V ) } & { \frac { 1 } { 2 } ( I - V ) } \end{array} \right] , \quad \forall \ V \in s p ( 2 n ) , \quad \alpha _ { V } \in M ^ { \prime } ,
$$

$$
S \in S p ( 2 n ) , \quad \beta _ { S } = \left[ \begin{array} { c c } { ( S ^ { - 1 } ) ^ { \mathrm { T } } } & { O } \\ { O } & { S } \end{array} \right] \in S p ( J _ { 4 n } ) ,
$$

$$
\gamma _ { S } = \left[ \begin{array} { l l } { S } & { O } \\ { O } & { S } \end{array} \right] \in S p ( \widetilde { J } _ { 4 n } ) .
$$

Then the following conditions are equivalent:

$$
\begin{array} { r l } { 1 ^ { \circ } } & { \phi _ { \alpha _ { V } , S \circ g \circ S ^ { - 1 } } = \phi _ { \alpha , g } \circ S ^ { - 1 } , \forall g \subsetneq I . } \\ { 2 ^ { \circ } } & { \phi _ { \alpha _ { V } \gamma _ { S } , g } = \phi _ { \beta _ { S } \alpha _ { V } , g } , \forall g \subsetneq I . } \\ { 3 ^ { \circ } } & { \alpha _ { V } \gamma _ { S } = \beta _ { S } \alpha _ { V } . } \\ { 4 ^ { \circ } } & { S V = V S . } \end{array}
$$

Proof. $1 ^ { \circ } \Leftrightarrow 2 ^ { \circ }$ from Theorems 3.1 and Theorem 3.2. $2 ^ { \circ } \Rightarrow 3 ^ { \circ }$ using the uniqueness theorem on Darboux transformation 4.2. For

$$
\alpha _ { V } \gamma _ { S } = \pm \beta _ { S } \alpha _ { V } ,
$$

since $J S = { S ^ { \prime } } ^ { - 1 } J$ , sign “−” case is excluded. The rest of the proof is trivial.

There is a deep connection between the symmetry of a symplectic difference scheme and the conservation of first integrals.

Let $\mathcal { F }$ be the set of smooth functions defined on $\mathbf { R } ^ { n }$ .

Theorem 4.4. If Hamiltonian function $H$ is invariant under phase flow $g _ { F }$ with Hamiltonian function $F$ , then $F$ is first integral of the system with Hamiltonian function $H$ .

Let $H , F \in { \mathcal { F } }$ , then

$$
\begin{array} { l } { { F \circ g _ { H } ^ { t } \ = F \Longleftrightarrow \{ F , H \} = 0 \Longleftrightarrow H \circ g _ { F } ^ { t } = H \Longleftrightarrow g _ { H } ^ { t } } } \\ { { \qquad = g _ { F } ^ { - S } \circ g _ { H } ^ { t } \circ g _ { F } ^ { S } . } } \end{array}
$$

Theorem 4.5. Let $F$ be a conservation law of Hamiltonian system, then phase flow $g _ { H } ^ { t }$ (or symplectic schemes $\phi _ { H } ^ { \tau }$ ) keeps phase flow $g _ { F } ^ { t }$ with $F$ (or $\phi _ { F } ^ { \tau }$ ) invariant iff $F \circ g _ { H } = F + C$ . Let $F \in { \mathcal { F } } , g \in S p .$ -diff, then

$$
g = g _ { F } ^ { - t } \circ g \circ g _ { F } ^ { t } \left( o r g _ { F } ^ { t } = g ^ { - 1 } g _ { F } ^ { t } ( g ( z ) ) \Longleftrightarrow F \circ g = F + c . \right.
$$

Proof. The “ if ” part of the proof is obvious. Since

$$
\begin{array} { r l } { F \circ g } & { = F + c \Longrightarrow \nabla F = \nabla F \circ g \Longrightarrow g _ { F } ^ { t } = g _ { F \circ g } ^ { t } } \\ & { = g ^ { - 1 } \circ g _ { F } ^ { t } \circ g } \\ & { = g ^ { - 1 } g _ { F } ^ { t } ( g ( z ) ) \Longleftrightarrow g = g _ { F } ^ { - t } \circ g \circ g _ { F } ^ { t } . } \end{array}
$$

On the other hand, take the derivative of both sides of the following equation w.r.t. $t$ at $t = 0$ ,

$$
g _ { F } ^ { t } ( z ) = g ^ { - 1 } g _ { F } ^ { t } ( g ( z ) ) ,
$$

and notice that $g _ { * } ( z ) \in S p , g _ { * } ^ { - 1 } J ^ { - 1 } = J ^ { - 1 } g _ { * } ^ { \mathrm { T } }$ , we get

$$
J ^ { - 1 } \nabla F ( z ) = g _ { * } ^ { - 1 } ( z ) J ^ { - 1 } \nabla F ( g ( z ) ) = J ^ { - 1 } g _ { * } ^ { \mathrm { T } } ( z ) \nabla F ( g ( z ) ) ,
$$

then we have

$$
\nabla F = \nabla F \circ g \Longrightarrow F \circ g = F + c .
$$

Therefore, the theorem is completed.

# 6.5 Formal Energy for Hamiltonian Algorithm

Let $F ^ { s }$ be an analytic canonical transformation for $s$ , i.e.,

$1 ^ { \circ }$ $F ^ { s } \in S p$ -diff.   
$2 ^ { \circ }$ $F ^ { 0 } = \mathrm { i d }$ .   
$3 ^ { \circ }$ $F ^ { s }$ analytic if $| s |$ is small enough.

Then there exists a “formal” energy, i.e., a formal power series in $s$ ,

$$
h ^ { s } ( z ) = h ( s , z ) = \sum _ { i = 1 } ^ { \infty } { s ^ { i } h ^ { i } ( z ) }
$$

with the following property: if $h ^ { s } ( z )$ converges, the phase flow $g _ { h ^ { s } } ^ { t }$ is a canonical transformation with Hamiltonian function $h ^ { s } ( z )$ , which is considered as a timeindependent Hamiltonian with $s$ as a parameter and satisfies “equivalence condition”

$$
\left. g _ { h ^ { s } } ^ { t } \right| _ { t = s } = F ^ { s } .
$$

Therefore $h ^ { s } ( z ) = h ^ { s } ( F ^ { s } z ) $ , $\forall z \in \mathbf { R } ^ { 2 n }$ , thus $h ^ { s } ( z )$ is invariant under $F ^ { s }$ (for those $s , z$ in the domain of convergence of $h ^ { s } ( z ) _ { , } ^ { \cdot }$ ).

The generating function with $F ^ { s }$ , the new Hamiltonian function and $\alpha$ , the Darboux transformation is

$$
\phi _ { F ^ { s } , \alpha } ( w ) : \psi ( s , w ) = \sum _ { k = 1 } ^ { \infty } s ^ { k } \psi ^ { ( k ) } ( w ) .
$$

Introduce formal power series

$$
h ^ { s } ( z ) = h ( s , w ) = \sum _ { k = 1 } ^ { \infty } { s ^ { i } h ^ { i } ( w ) } .
$$

Assuming it converges, we associate the phase flow with the generating function

$$
\begin{array} { c l c r } { { } } & { { } } & { { \displaystyle h ^ { s } ( z ) \longrightarrow \psi _ { h ^ { s } , \alpha } ^ { t } ( w ) : \chi ( t , s , w ) = \sum _ { k = 1 } ^ { \infty } t ^ { k } \chi ^ { ( k ) } ( s , w ) , } } \\ { { } } & { { } } & { { \displaystyle \chi ^ { ( 1 ) } ( s , w ) = - h ( s , w ) . } } \end{array}
$$

For $k > 1$

$$
\begin{array} { r l } { \chi ^ { ( k + 1 ) } ( s , w ) } & { = \ - \displaystyle \sum _ { m = 1 } ^ { k } \frac { 1 } { ( k + 1 ) m ! } \sum _ { l _ { 1 } , \cdots , l _ { m } = 1 } ^ { 2 n } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } h _ { w _ { l _ { 1 } } , \cdots , w _ { l _ { m } } } ( s , w ) } \\ & { \quad \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { 1 } ) } ( s , w ) ) _ { l _ { 1 } } \cdot \cdot \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { m } ) } ( s , w ) ) _ { l _ { m } } } \\ & { = \ \displaystyle \sum _ { m = 1 } ^ { k } \frac { 1 } { ( k + 1 ) m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } \chi _ { w _ { l _ { 1 } } , \cdots , w _ { l _ { m } } } ^ { ( 1 ) } ( s , w ) } \\ & { \quad \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { 1 } ) } ( s , w ) ) _ { l _ { 1 } } \cdot \cdot \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { m } ) } ( s , w ) ) _ { l _ { m } } . } \end{array}
$$

$$
\chi ^ { ( k ) } ( s , w ) = \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( k , i ) } ( w ) , \mathrm { t h e n } \chi ( t , s , w ) = \sum _ { k > 1 } ^ { \infty } \sum _ { i = 0 } ^ { \infty } t ^ { k } s ^ { i } \chi ^ { ( k , i ) } ( w ) .
$$

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( k + 1 , i ) } ( w ) ~ = ~ \sum _ { i = 0 } ^ { \infty } s ^ { i } \sum _ { m = 1 } ^ { k } \frac { 1 } { ( k + 1 ) m ! } } \ ~ \sum _ { i _ { 0 } + i _ { 1 } + \cdots + i _ { m } = i \atop { k _ { 1 } + \cdots + k _ { m } = k } } }  \\ { { \ ~ \cdot ~ \sum _ { l _ { 1 } , \cdots , l _ { m } = 1 } ^ { 2 n } \chi _ { w _ { l _ { 1 } } , \cdots , w _ { l _ { m } } } ^ { ( 1 , i _ { 0 } ) } ( w ) ( A _ { 1 } \chi _ { w } ^ { ( k _ { 1 } , i _ { 1 } ) } ( w ) ) _ { l _ { 1 } } \cdot \cdot \cdot } }  \\ { { \ ~ \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { m } , i _ { m } ) } ( w ) ) _ { l _ { m } } . } } \end{array}
$$

Thus

$$
\begin{array} { r c l } { { \chi ^ { ( k + 1 , i ) } ( w ) } } & { { = } } & { { \displaystyle \sum _ { m = 1 } ^ { k } \frac { 1 } { ( k + 1 ) m ! } \sum _ { { \bf \Phi } _ { i _ { 0 } + i _ { 1 } + \cdots + i _ { m } = i } \atop { \bf \Phi } _ { k _ { 1 } + \cdots + k _ { m } = k } } \sum _ { l _ { 1 } , \cdots , l _ { m } = 1 } ^ { 2 n } \chi _ { w _ { l _ { 1 } } , \cdots , w _ { l _ { m } } } ^ { ( 1 , i _ { 0 } ) } ( w ) } } \\ { { } } & { { } } & { { \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { 1 } , i _ { 1 } ) } ( w ) ) _ { l _ { 1 } } \cdot \cdot \cdot ( A _ { 1 } \chi _ { w } ^ { ( k _ { m } , i _ { m } ) } ( w ) ) _ { l _ { m } } . } } \end{array}
$$

Let

$$
\chi ^ { ( 1 ) } ( s , w ) = \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( 1 , i ) } ( w ) = - h ( s , w ) = - \sum _ { i = 0 } ^ { \infty } s ^ { i } h ^ { i } ( w ) ,
$$

so the coefficient $\chi ^ { ( k + 1 , i ) }$ can be obtained by recursion,

$$
\chi ^ { ( 1 , i ) } = - h ^ { ( i ) } , \quad i = 0 , 1 , 2 , \cdots .
$$

Note that $\chi ^ { ( k + 1 , i ) }$ is determined only by the values of $\chi ^ { ( k ^ { \prime } , i ^ { \prime } ) } ( k ^ { \prime } \leq k , i ^ { \prime } \leq i )$

$$
\begin{array} { c c c c c c c } { \chi ^ { ( 1 , 0 ) } } & { \chi ^ { ( 1 , 1 ) } } & { \chi ^ { ( 1 , 2 ) } } & { \cdots } & { \chi ^ { ( 1 , i ) } } & { \chi ^ { ( 1 , i + 1 ) } } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { \chi ^ { ( k , 0 ) } } & { \chi ^ { ( k , 1 ) } } & { \chi ^ { ( k , 2 ) } } & { \cdots } & { \chi ^ { ( k , i ) } } & { \chi ^ { ( k , i + 1 ) } } \\ { \chi ^ { ( k + 1 , 0 ) } } & { \chi ^ { ( k + 1 , 1 ) } } & { \chi ^ { ( k + 1 , 2 ) } } & { \cdots } & { \chi ^ { ( k + 1 , i ) } } & { \chi ^ { ( k + 1 , i + 1 ) } } \end{array}
$$

The condition (5.1) can be now reexpressed as

$$
\chi ( t , s , w ) | _ { t = s } = \chi ( s , s , w ) = \psi ( s , w ) ,
$$

i.e.,

$$
\begin{array} { l } { \displaystyle \sum _ { k > 1 } ^ { \infty } s ^ { k } \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( k , i ) } ( w ) = \displaystyle \sum _ { k > 1 } ^ { \infty } s ^ { k } \psi ^ { ( k ) } ( w ) } \\ { \displaystyle \sum _ { i = 0 } ^ { \infty } s ^ { i } \sum _ { j = 0 } ^ { \infty } \chi ^ { ( k - j ) j } ( w ) = \displaystyle \sum _ { i = 1 } ^ { \infty } s ^ { i } \psi ^ { ( k ) } ( w ) , } \\ { \displaystyle \sum _ { j = 0 } ^ { k - 1 } \chi ^ { ( k - i , j ) } ( w ) = \psi ^ { ( k ) } , \quad k = 2 , 3 , \cdots , } \\ { \displaystyle \sum _ { j = 0 } ^ { k } \chi ^ { ( k - i , j ) } ( w ) = \psi ^ { ( k ) } , } \\ { \displaystyle \chi ^ { ( 1 , 0 ) } = \psi ^ { ( 1 ) } , } \\ { \displaystyle \sum _ { k = 0 } ^ { k } \chi ^ { ( k + 1 - i , j ) } = \psi ^ { ( k + 1 ) } , \quad k = 2 , 3 , \cdots } \end{array}
$$

$$
\begin{array} { c c c c c c c c c } { { } } & { { } } & { { - h ^ { ( 0 ) } } } & { { - h ^ { ( 1 ) } } } & { { - h ^ { ( 2 ) } } } & { { \cdots } } & { { - h ^ { ( k - 1 ) } } } & { { - h ^ { ( k ) } } } \\ { { \ } } & { { \psi ^ { ( 1 ) } } } & { { \chi ^ { ( 1 , 0 ) } } } & { { \chi ^ { ( 1 , 1 ) } } } & { { \chi ^ { ( 1 , 2 ) } } } & { { \cdots } } & { { \chi ^ { ( 1 , k - 1 ) } } } & { { \chi ^ { ( 1 , k ) } } } \\ { { \psi ^ { ( 2 ) } } } & { { \chi ^ { ( 2 , 0 ) } } } & { { \chi ^ { ( 2 , 1 ) } } } & { { \chi ^ { ( 2 , 2 ) } } } & { { \cdots } } & { { \chi ^ { ( 2 , k - 1 ) } } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { } } & { { } } & { { } } & { { } } \\ { { \psi ^ { ( k ) } } } & { { \chi ^ { ( k , 0 ) } } } & { { \chi ^ { ( k , 1 ) } } } & { { } } & { { } } & { { } } & { { } } \\ { { \psi ^ { ( k + 1 ) } } } & { { \chi ^ { ( k + 1 , 0 ) } } } & { { } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

and

$$
\begin{array} { r c l } { { } } & { { } } & { { \chi ^ { ( 1 , 0 ) } = \psi ^ { ( 1 ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \chi ^ { ( 2 , 0 ) } + \chi ^ { ( 1 , 1 ) } = \psi ^ { ( 2 ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \chi ^ { ( 3 , 0 ) } + \chi ^ { ( 2 , 1 ) } + \chi ^ { ( 1 , 2 ) } = \psi ^ { ( 3 ) } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \chi ^ { ( k + 1 , 0 ) } + \chi ^ { ( k , 1 ) } + \cdots + \chi ^ { ( 2 , k - 1 ) } + \chi ^ { ( 1 , k ) } = \psi ^ { ( k + 1 ) } . } } \end{array}
$$

Now if $\psi ^ { ( 1 ) } , \psi ^ { ( 2 ) } , \cdot \cdot \cdot , \psi ^ { ( k ) } , \psi ^ { ( k + 1 ) } , \cdot \cdot \cdot$ are known, then

$$
h ^ { ( 0 ) } = - \chi ^ { ( 1 , 0 ) } , \ h ^ { ( 1 ) } = - \chi ^ { ( 1 , 1 ) } , \ \cdot \cdot \cdot , \ h ^ { ( k - 1 ) } = - \chi ^ { ( 1 , k - 1 ) } , \ h ^ { ( k ) } = - \chi ^ { ( 1 , k ) } , \ \cdot \cdot \cdot
$$

can be determined. We get:

$$
\begin{array} { l } { { h ^ { ( 0 ) } = - \psi ^ { ( 1 ) } , } } \\ { { h ^ { ( 1 ) } = - \psi ^ { ( 2 ) } + \chi ^ { ( 2 , 0 ) } , } } \\ { { h ^ { ( 2 ) } = - \psi ^ { ( 3 ) } + ( \chi ^ { ( 3 , 0 ) } + \chi ^ { ( 2 , 1 ) } ) , } } \\ { { } } \\ { { \vdots } } \\ { { h ^ { ( k ) } = - \psi ^ { ( k + 1 ) } + ( \chi ^ { ( k + 1 , 0 ) } + \chi ^ { ( k , 1 ) } + \cdots + \chi ^ { ( 2 , k - 1 ) } ) , } } \\ { { \vdots } } \end{array}
$$

So $h ^ { ( 0 ) } , h ^ { ( 1 ) } , h ^ { ( 2 ) } , \cdot \cdot \cdot$ can be recursively determined by $\psi ^ { ( 1 ) } , \psi ^ { ( 2 ) } , \cdot \cdot \cdot ,$ . So we get the formal power series $h ^ { s } = \sum _ { i = 0 } ^ { \infty } s ^ { i } h ^ { ( i ) } ( z )$ , and in case of convergence, it satisfies

$$
g _ { h ^ { s } } ^ { t } | _ { t = s } = F ^ { s } .
$$

We now give a special example to show how to calculate the formal energy. Let us consider normal Darboux transformation with

$$
V = - E = \left[ \begin{array} { c c } { { O } } & { { - I } } \\ { { } } & { { } } \\ { { - I } } & { { O } } \end{array} \right] , \alpha _ { V } ^ { - 1 } = \left[ \begin{array} { c c } { { A _ { 1 } } } & { { B _ { 1 } } } \\ { { } } & { { } } \\ { { C _ { 1 } } } & { { D _ { 1 } } } \end{array} \right] ,
$$

where

$$
A _ { 1 } = \frac 1 2 ( J V J - J ) = \left[ \begin{array} { l l } { { O } } & { { O } } \\ { { } } & { { } } \\ { { - I } } & { { O } } \end{array} \right] .
$$

Suppose we just use the first term of the generating function of the generating map $\alpha _ { V }$ , i.e., we just consider the first order scheme

$$
F ^ { s } \sim \psi ( s , w ) = - s H ( w ) = \sum _ { i = 1 } ^ { \infty } \ : s ^ { k } \psi ^ { ( k ) } .
$$

Let us assume $\psi ^ { ( 1 ) } = - H ( w )$ . If $\psi ^ { ( 2 ) } = \psi ^ { ( 3 ) } = \cdot \cdot \cdot = 0$ , then $\chi ^ { ( 1 , 0 ) } = \psi ^ { ( 1 ) } = - H$ . We need to calculate $\chi ^ { ( 2 , 0 ) }$ . Since

$$
\begin{array} { r l } & { \chi _ { z } ^ { ( 1 , 0 ) } = - \left[ \begin{array} { c } { H _ { p } } \\ { H _ { q } } \end{array} \right] , } \\ & { A _ { 1 } \chi _ { z } ^ { ( 1 , 0 ) } = \left[ \begin{array} { c c } { O } & { O } \\ { - I } & { O } \end{array} \right] \left[ \begin{array} { c } { - H _ { p } } \\ { - H _ { q } } \end{array} \right] = \left[ \begin{array} { c } { O } \\ { H _ { p } } \end{array} \right] , } \\ & { \chi _ { z z } ^ { ( 1 , 0 ) } = - \left[ \begin{array} { c c } { H _ { p p } } & { H _ { p q } } \\ { H _ { q p } } & { H _ { q q } } \end{array} \right] . } \end{array}
$$

By formula (5.6), we get

$$
\begin{array} { r l } { \chi ^ { ( 2 , 0 ) } } & { = \displaystyle \frac { 1 } { 2 \times 1 ! } \sum _ { i _ { 0 } + i _ { 1 } = 0 } ^ { 2 n } \sum _ { k _ { 1 } = 1 } ^ { 2 n } \sum _ { l _ { 1 } = 1 } ^ { 2 n } \chi _ { z _ { l _ { 1 } } } ^ { ( 1 , i _ { 0 } ) } ( A _ { 1 } \chi _ { z } ^ { ( k _ { 1 } , i _ { 1 } ) } ) _ { l _ { 1 } } } \\ & { = \displaystyle \frac { 1 } { 2 } ( \chi _ { z } ^ { ( 1 , 0 ) } ) ^ { \prime } A _ { 1 } \chi _ { z } ^ { ( 1 , 0 ) } } \\ & { = \displaystyle - \frac { 1 } { 2 } \left[ \begin{array} { c } { H _ { p } } \\ { H _ { q } } \end{array} \right] ^ { \prime } \left[ \begin{array} { c } { 0 } \\ { H _ { p } } \end{array} \right] = \displaystyle - \frac { 1 } { 2 } H _ { q } ^ { \prime } H _ { p } . } \end{array}
$$

From formula (5.10), we get

$$
\chi ^ { ( 2 , 0 ) } + \chi ^ { ( 1 , 1 ) } = \psi ^ { ( 2 ) } = 0 \Longrightarrow \chi ^ { ( 1 , 1 ) } = - \chi ^ { ( 2 , 0 ) } = \frac { 1 } { 2 } H _ { q } ^ { \prime } H _ { p } .
$$

In order to obtain $\chi ^ { ( 1 , 2 ) }$ , we first determine $\chi ^ { ( 3 , 0 ) }$ and $\chi ^ { ( 2 , 1 ) }$ , and for the latter we need to caculate

$$
\begin{array} { r } { \boldsymbol { \lambda } ^ { ( 1 , 1 ) } = \displaystyle \frac { 1 } { 2 } \left[ \begin{array} { l } { \frac { \partial } { \partial { \phi } _ { j = 1 } ^ { N } } H _ { \phi _ { j } } H _ { p _ { j } } } \\ { \frac { \partial } { \partial q _ { j = 1 } ^ { N } } H _ { \phi _ { j } } H _ { p _ { j } } } \end{array} \right] } \\ { = \frac { 1 } { 2 } \left[ \begin{array} { l } { H _ { p q } H _ { p } + H _ { p p } H _ { q } } \\ { H _ { q p } H _ { p } + H _ { q p } H _ { q } } \end{array} \right] , } \\ { \boldsymbol { A } _ { 1 \lambda ^ { ( 1 , 1 ) } } = \left[ \begin{array} { l l } { O } & { O } \\ { - T } & { O } \end{array} \right] \boldsymbol { \lambda } ^ { ( 1 , 1 ) } } \\ { = \displaystyle - \frac { 1 } { 2 } \left[ \begin{array} { l } { O } \\ { H _ { p q } H _ { p } + H _ { p p } H _ { q } } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r } { A _ { 1 } \chi _ { z } ^ { ( 2 , 0 ) } = - A _ { 1 } \chi _ { z } ^ { ( 1 , 1 ) } \qquad } \\ { = \frac { 1 } { 2 } \left[ \begin{array} { c } { O } \\ { H _ { p q } H _ { p } + H _ { p p } H _ { q } } \end{array} \right] . } \end{array}
$$

For $k = 2 , i = 0$ , we have

$$
\begin{array} { r c l } { { \chi ^ { ( 3 , 0 ) } } } & { { = } } & { { \displaystyle { \frac { 1 } { 3 } \Big ( \frac { 1 } { 1 ! } \sum _ { i _ { 0 } + i _ { 1 } = 0 } ^ { 2 n } \sum _ { k _ { 1 } = 2 } ^ { 2 n } \sum _ { l _ { 1 } = 1 } ^ { 2 n } \chi _ { z _ { l _ { 1 } } } ^ { ( 1 , 0 ) } ( A _ { 1 } \chi _ { z } ^ { ( k _ { 1 } , 0 ) } ) _ { l _ { 1 } } } } } \\ { { } } & { { } } & { { \displaystyle { + \sum _ { l _ { 1 } , l _ { 2 } = 1 } ^ { 2 n } \sum _ { i _ { 0 } + i _ { 1 } + i _ { 2 } = 0 } ^ { 2 n } \sum _ { k _ { 1 } + k _ { 2 } = 2 } ^ { 2 n } \chi _ { z _ { l _ { 1 } } , z _ { l _ { 2 } } } ^ { ( 1 , 0 ) } ( A _ { 1 } \chi _ { z } ^ { ( k _ { 1 } , 0 ) } ) _ { l _ { 1 } } ( A _ { 1 } \chi _ { z } ^ { ( k _ { 2 } , 0 ) } ) _ { l _ { 2 } } \Big ) } } } \\ { { } } & { { = } } & { { \displaystyle { \frac { 1 } { 3 } \big ( \chi _ { z } ^ { ( 2 , 0 ) } \big ) ^ { \mathrm { T } } A _ { 1 } \chi _ { z } ^ { ( 2 , 0 ) } + \frac { 1 } { 6 } \big ( A _ { 1 } \chi _ { z } ^ { ( 1 , 0 ) } \big ) ^ { \mathrm { T } } \chi _ { z z } ^ { ( 1 , 0 ) } A _ { 1 } \chi _ { z } ^ { ( 1 , 0 ) } } } } \\ { { } } & { { = } } & { { \displaystyle { - \frac { 1 } { 6 } \big ( H _ { q } ^ { \mathrm { T } } H _ { p q } H _ { p } + H _ { q } ^ { \mathrm { T } } H _ { p p } H _ { q } + H _ { p } ^ { \mathrm { T } } H _ { q q } H _ { p } \big ) } . } } \end{array}
$$

For $k = 1 , i = 1$ , we have

$$
\begin{array} { r c l } { \chi ^ { ( 2 , 1 ) } = } & { \frac { 1 } { 2 } \displaystyle \sum _ { i _ { 0 } + i _ { 1 } = 1 } ^ { 2 n } \sum _ { k _ { 1 } = 1 } ^ { 2 n } \sum _ { l _ { 1 } = 1 } ^ { 2 n } \chi _ { z _ { l _ { 1 } } } ^ { ( 1 , i _ { 0 } ) } ( A _ { 1 } \chi _ { z } ^ { ( k _ { 1 } , i _ { 1 } ) } ) _ { l _ { 1 } } } \\ & { = } & { \frac { 1 } { 2 } \left( ( \chi _ { z } ^ { ( 1 , 0 ) } ) ^ { \operatorname { T } } A _ { 1 } \chi _ { z } ^ { ( 1 , 1 ) } + \left( \chi _ { z } ^ { ( 1 , 1 ) } \right) ^ { \operatorname { T } } A _ { 1 } \chi _ { z } ^ { ( 1 , 0 ) } \right) } \\ & { = } & { \frac { 1 } { 4 } ( H _ { q } ^ { \operatorname { T } } H _ { p p } H _ { q } + H _ { p } ^ { \operatorname { T } } H _ { q q } H _ { p } ) + \frac { 1 } { 2 } H _ { q } ^ { \operatorname { T } } H _ { p q } H _ { p } . } \end{array}
$$

From (5.11), we have

$$
\chi ^ { ( 3 , 0 ) } + \chi ^ { ( 2 , 1 ) } + \chi ^ { ( 1 , 2 ) } = \psi ^ { ( 3 ) } = 0 \Longrightarrow \chi ^ { ( 1 , 2 ) } = - ( \chi ^ { ( 3 , 0 ) } + \chi ^ { ( 2 , 1 ) } ) .
$$

For $k = 1 , i = 2$ ,

$$
\begin{array} { r l r } {  { \chi ^ { ( 1 , 2 ) } = \ - \Big \{ \ - \frac { 1 } { 6 } ( H _ { q } ^ { \mathrm { T } } H _ { p p } H _ { q } + H _ { p } ^ { \mathrm { T } } H _ { q q } H _ { p } ) - \frac { 1 } { 6 } H _ { q } ^ { \mathrm { T } } H _ { p q } H _ { p } } } \\ & { } & { + \frac { 1 } { 4 } ( H _ { q } ^ { \mathrm { T } } H _ { p p } H _ { q } + H _ { p } ^ { \mathrm { T } } H _ { q q } H _ { p } ) + \frac { 1 } { 2 } H _ { q } ^ { \mathrm { T } } H _ { p q } H _ { p } \Big \} } \\ & { } & { = \ - \frac { 1 } { 1 2 } ( H _ { q } ^ { \mathrm { T } } H _ { p p } H _ { q } + H _ { p } ^ { \mathrm { T } } H _ { q q } H _ { p } + 4 H _ { q } ^ { \mathrm { T } } H _ { p q } H _ { p } ) . } \end{array}
$$

Finally, we get the formal power series of energy

$$
\begin{array} { r l r } {  { h ( s , z ) = - ( \chi ^ { ( 1 , 0 ) } + s \chi ^ { ( 1 , 1 ) } + s ^ { 2 } \chi ^ { ( 1 , 2 ) } ) + O ( s ^ { 3 } ) } } \\ & { } & \\ & { } & { = H ( z ) - \frac { s } { 2 } H _ { q } ^ { \prime } H _ { p } + \frac { s ^ { 2 } } { 1 2 } ( H _ { q } ^ { \prime } H _ { p p } H _ { q } + H _ { p } ^ { \prime } H _ { q q } H _ { p } + 4 H _ { q } ^ { \prime } H _ { p q } H _ { q } ) + O ( s ^ { 3 } ) . } \end{array}
$$

Now, let $H ( z )$ be a time-independent Hamiltonian, let its phase flow be $g _ { H } ^ { t }$ , and let its generating function be

$$
\phi _ { g _ { H } ^ { t } } ( w ) = \phi ( t , w ) = \sum _ { k = 1 } ^ { \infty } t ^ { k } \phi ^ { ( k ) } ( w ) .
$$

Then we have

$$
\phi ^ { ( 1 ) } ( w ) = - H ( w ) ,
$$

for $k \geq 1$

$$
\phi ^ { ( k + 1 ) } ( w ) ~ = ~ \sum _ { m = 1 } ^ { k } { \frac { 1 } { ( k + 1 ) m ! } } \sum _ { l _ { 1 } , \cdots , l _ { m } = 1 } ^ { 2 n } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } \phi _ { w _ { l _ { 1 } } \cdots w _ { l _ { m } } } ^ { ( 1 ) } ( w )
$$

Theorem 5.1. [Fen98a] Let $F ^ { s }$ be a $S p$ -diff operator of order $m$ for Hamiltonian $H$ , i.e., $\phi ( s , w ) - \psi ( s , w ) = O ( | s | ^ { m + 1 } ) ,$ , and

$$
\left\{ \begin{array} { l l } { \psi ^ { ( 1 ) } ( w ) = \phi ^ { ( 1 ) } ( w ) = - H ( w ) , } \\ { \psi ^ { ( 2 ) } ( w ) = \phi ^ { ( 2 ) } ( w ) , } \\ { \vdots } \\ { \psi ^ { ( m ) } ( w ) = \phi ^ { ( m ) } ( w ) , } \end{array} \right.
$$

then

$$
h ^ { ( 0 ) } ( w ) = H ( w ) , \ h ^ { ( 1 ) } ( w ) = h ^ { ( 2 ) } ( w ) = \cdots = h ^ { ( m - 1 ) } ( w ) = 0 ,
$$

i.e.,

$$
h ( s , w ) - H ( w ) = o \left( | s | ^ { m } \right)
$$

and

$$
h ^ { ( m ) } ( w ) = \psi ^ { ( m + 1 ) } ( w ) - \phi ^ { ( m + 1 ) } ( w ) .
$$

Proof. First we show that $\chi ^ { ( k + 1 , i ) }$ depends only on derivatives of $\chi ^ { ( \boldsymbol { k } ^ { \prime } , i ^ { \prime } ) } \left( \boldsymbol { k } ^ { \prime } \right) \leq$ $k , i ^ { \prime } \leq i$ ). The recursion for $i = 0$ is the same as the recursion of phase flow generating function with Hamiltonian $\chi ^ { ( 1 , 0 ) } ( w )$ . For $i \geq 1$ , $\chi ^ { ( k + 1 , i ) } = \bar { 0 }$ , if $\chi ^ { ( k ^ { \prime } , i ^ { \prime } ) } = 0$ for all $i ^ { \prime } , k ^ { \prime }$ , such that $1 \leq i ^ { \prime } \leq i , 1 \leq k ^ { \prime } \leq k$ . We have

$$
\begin{array} { r l } & { \begin{array} { r l } { \lambda ^ { ( 1 ) } ( x ) = - 2 ^ { 2 } \lambda ^ { ( 2 ) } \tau ^ { 2 } \lambda ^ { ( 2 ) } } & { , } \\ { x ^ { ( 2 ) } = - \lambda ^ { ( 2 ) } \tau ^ { ( 2 ) } } & { , } \\ { \lambda ^ { ( 3 ) } ( x ) = \lambda ^ { ( 3 ) } } & { , } \end{array} } \\ & { \begin{array} { r l } { \frac { \lambda ^ { ( 3 ) } ( x ) } { 2 } } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 2 ) } x ^ { ( 3 ) } x ^ { ( 4 ) } , } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 3 ) } x ^ { ( 4 ) } , } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 4 ) } x ^ { ( 4 ) } , } & { , } \end{array} } \\ & { \begin{array} { r l } { \frac { \lambda ^ { ( 4 ) } ( x ) } { 2 } } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 2 ) } x ^ { ( 4 ) } x ^ { ( 4 ) } , } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 2 ) } x ^ { ( 4 ) } x ^ { ( 4 ) } , } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 3 ) } x ^ { ( 4 ) } x ^ { ( 4 ) } , } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 4 ) } x ^ { ( 4 ) } x ^ { ( 4 ) } + \lambda ^ { ( 4 ) ( 4 ) } x ^ { ( 4 ) } - x ^ { ( 4 ) ( 3 ) } } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 4 ) } x ^ { ( 2 ) } x ^ { ( 4 ) } , } & { , } \\ { \frac { \lambda ^ { ( 4 ) } ( x ) } { 2 } } & { , } \\ { x ^ { ( 4 ) } = x ^ { ( 4 ) } \lambda ^ { ( 4 ) } x ^ { ( 4 ) } , } & { , } \end{array} } \end{array}
$$

So, $\chi ^ { ( k , i ) }$ can be generated successively through (5.9), (5.6). Then

$$
h ( s , w ) = \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( 1 , i ) } ( w ) .
$$

Using equation $H = \psi ^ { ( 1 ) } = \phi ^ { ( 1 ) } = \chi ^ { ( 1 , 0 ) }$ and (5.9), (5.14) ,we get

$$
\chi ^ { ( 2 , 0 ) } = \phi ^ { ( 2 ) } , \chi ^ { ( 3 , 0 ) } = \phi ^ { ( 3 ) } , \cdots , \chi ^ { ( k , 0 ) } = \phi ^ { ( k ) } , \cdots
$$

Using Equation (5.14), we get

$$
\psi ^ { ( 2 ) } = \phi ^ { ( 2 ) } = \chi ^ { ( 1 , 1 ) } + \phi ^ { ( 2 ) } \Longrightarrow \chi ^ { ( 1 , 1 ) } = 0 .
$$

Applying Equations (5.9) and (5.14), we get

$$
\chi ^ { ( 2 , 1 ) } = 0 \Longrightarrow \chi ^ { ( 3 , 1 ) } = \chi ^ { ( 4 , 1 ) } = \cdots = \chi ^ { ( k , 1 ) } = \cdots = 0 .
$$

Applying equation

$$
\psi ^ { ( 3 ) } = \phi ^ { ( 3 ) } = \chi ^ { ( 1 , 2 ) } + \chi ^ { ( 2 , 1 ) } + \chi ^ { ( 3 , 0 ) } = \chi ^ { ( 1 , 2 ) } + 0 + \phi ^ { ( 3 ) } \Longrightarrow \chi ^ { ( 1 , 2 ) } = 0 ,
$$

then

$$
\chi ^ { ( 2 , 2 ) } = \chi ^ { ( 3 , 2 ) } = \chi ^ { ( 4 , 2 ) } = \cdots = \chi ^ { ( k , 2 ) } = \cdots = 0 .
$$

Finally

$$
\psi ^ { ( m ) } = \phi ^ { ( m ) } = \chi ^ { ( 1 , m - 1 ) } + \chi ^ { ( 2 , m - 2 ) } + \cdot \cdot \cdot + \chi ^ { ( m - 1 , 1 ) } + \phi ^ { ( m ) } \Longrightarrow \chi ^ { ( 1 , m - 1 ) } = 0 ,
$$

then

$$
\chi ^ { ( 2 , m - 1 ) } = \chi ^ { ( 3 , m - 1 ) } = \chi ^ { ( 4 , m - 1 ) } = \cdots = \chi ^ { ( k , m - 1 ) } = \cdots = 0 .
$$

Since $\chi ^ { ( k , i ) } = 0 , \forall i = 1 , 2 , \cdot \cdot \cdot , m - 1$ and $k = 1 , 2 , 3 \cdots$ , then the equation

$$
\begin{array} { r l } { \psi ^ { ( m + 1 ) } = \chi ^ { ( 1 , m ) } + \chi ^ { ( 2 , m - 1 ) } + \cdot \cdot \cdot + \chi ^ { ( m , 1 ) } + \chi ^ { ( m + 1 , 0 ) } } & { } \\ { \implies \chi ^ { ( 1 , m ) } = \psi ^ { ( m + 1 ) } - \phi ^ { ( m + 1 ) } , } & { } \end{array}
$$

so we finally get

$$
h ( s , z ) = \sum _ { i = 0 } ^ { \infty } s ^ { i } \chi ^ { ( 1 , i ) } = H ( z ) + s ^ { m } ( \psi ^ { ( m + 1 ) } - \phi ^ { ( m + 1 ) } ) + O \left( | s | ^ { m + 1 } \right) ,
$$

i.e.,

$$
h ( s , z ) - H ( z ) = s ^ { m } ( \psi ^ { ( m + 1 ) } ( z ) - \phi ^ { ( m + 1 ) } ( z ) ) + { \cal O } ( | s | ^ { m + 1 } ) .
$$

So in particular, if $F ^ { s } \sim \psi ( s , w )$ is given by the truncation of phase flow generating function, i.e.,

$$
\begin{array} { l } { { \psi ^ { ( 1 ) } = \phi ^ { ( 1 ) } = H , } } \\ { { \psi ^ { ( 2 ) } = \phi ^ { ( 2 ) } , \cdot \cdot \cdot , \psi ^ { ( m ) } = \phi ^ { ( m ) } , } } \\ { { \psi ^ { ( m + 1 ) } = \phi ^ { ( m + 1 ) } = 0 , } } \end{array}
$$

then

$$
h ( s , z ) = H ( z ) - O ( | s | ^ { m + 1 } ) .
$$

Therefore, the theorem is completed.

# 6.6 Ge–Marsden Theorem

In this section, we describe the result of Ge–Marsden, which talks about nonexistence of symplectic schemes that preserving energy. Due to the importance of preserving energy for a numerical method, extensive effort has been made by many people in searching for energy-preserving symplectic scheme, yet none of them is successful. Ge Zhong, a former Ph.D. student of Prof. Feng, first proved in his thesis [Ge88] the non-existence of the energy-preserving symplectic schemes. The result was published later in [GM88] by himself and Marsden, and now is called Ge–Marsden theorem.

Let $H$ be such a Hamiltonian function, where in its neighborhood of some level surface (energy surface), there exists no other conservation law exception energy. In other words, given a function $f$ defined in a neighborhood of energy surface $H = c _ { 0 }$ , if $\{ f , H \} = 0$ , then $f = g ( H )$ , where $g$ is a function on $\mathbf { R } ^ { 1 }$ .

A symplectic scheme can be regarded as a one-parameter family of symplectic transformation $\phi ^ { \tau } ( \tau \geq 0 )$ . A well-posed difference scheme should satisfy the consistency condition which ensures $\phi ^ { \tau }$ depends smoothly on parameter $\tau$ .

Now suppose that we have a symplectic scheme which preserves the energy, i.e.,

$$
H \circ \phi ^ { \tau } = H ,
$$

where $\phi ^ { \tau }$ maps energy surface $H \ = \ c$ to itself. We denote the mapping $\phi ^ { \tau } , ~ g _ { H } ^ { \tau }$ restricted on to the level surface $H = c$ respectively as

$$
f _ { H } ^ { \tau } \vert _ { H = c } , ~ \phi ^ { \tau } \vert _ { H = c } .
$$

Theorem 6.1 (G–M theorem). [Ge88] There exists a function $\tau = \tau ( c , t )$ defined on a neighborhoold of $0 \in \mathbf { R }$ , such that

$$
\phi ^ { \tau ( c , t ) } \big | _ { H = c } = g ^ { t } \big | _ { H = c } .
$$

This means that if we can find a symplectic scheme preserving energy, we can solve the original Hamiltonian system equivalently by a reparametrization of time parameter in phase flow $g _ { H } ^ { t }$ . In general this is impossible.

The proof of above Theorem 6.1 bases on the following Lemma 6.2.

Lemma 6.2. Let $g _ { A _ { 1 } } ^ { t } , g _ { A _ { 2 } } ^ { t }$ be solutions of following systems of ODE respectively.

$$
\frac { \mathrm { d } x } { \mathrm { d } t } = A _ { 1 } ( x , t ) , \quad \frac { \mathrm { d } x } { \mathrm { d } t } = c ( t ) A _ { 1 } ( x , t ) ,
$$

where $c ( t )$ is function of $t$ , then

$$
g _ { A _ { 1 } } ^ { t } = g _ { A _ { 2 } } ^ { \tau ( t ) } ,
$$

where $\tau ( t )$ is the solution of following system:

$$
\frac { \mathrm { d } \tau } { \mathrm { d } t } = c ( t ) , \quad \tau ( o ) = 0 .
$$

Proof. omit.

Now we give a proof of Theorem 6.1.

Proof. Let $F ( z , \tau )$ be a Hamiltonian function, whose phase flow is $\phi ^ { \tau }$ . Then from $H \circ \phi ^ { \tau } = H$ and Theorem2.20 of Chapter 3 we get $\{ F ( \cdot , \tau ) , H \} = 0$ . According to the assumption, there exists a $F _ { 1 }$ such that:

$$
F ( z , \tau ) = F _ { 1 } \big ( H ( z ) , \tau \big ) ,
$$

and the vector field generated by Hamiltonian function $F ( z , \tau )$ is

$$
J ^ { - 1 } F _ { 1 } ^ { \prime } ( H ( z ) , \tau ) H _ { z } ,
$$

which is tangent to the energy surface $H = c$ . Its restriction to the level surface $H = c$ is

$$
J ^ { - 1 } F _ { 1 } ^ { \prime } ( c , \tau ) H _ { z } \Big | _ { H = c } .
$$

It differs from the restriction of vector field $J ^ { - 1 } H _ { z }$ to the level surface $H = c$ only by a constant $F _ { 1 } ^ { \prime } ( c , \tau )$ . By Lemma 6.2 the proof is completed.

All symplectic transformations that keep $H$ invariant compose a group $S ( H )$ . $S ( H )$ is a rigidity under which $S _ { 0 } ( H )$ is a contained connected support set of unit transformation of group $S ( H )$ . $S _ { 0 } ( H )$ induces the level surface $H = c$ by the set of all transformation, denoted by $S _ { 0 } ( H ) | _ { H = 0 }$ . Then $S _ { 0 } ( H )$ is a curve

$$
S _ { 0 } ( H ) = \{ g _ { H } ^ { t } \big | _ { H = c } , t \in \mathbf { R } \} .
$$

Note that the rigidity of $S _ { 0 } ( H )$ exactly counteracts the existence of energy-preserving symplectc scheme.

# Bibliography

[Fen98] K. Feng: The calculus of generating functions and the formal energy for Hamiltonian systems. J. Comput. Math., 16:481–498, (1998).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91a] K. Feng and M.Z. Qin: Hamiltonian Algorithms for Hamiltonian Dynamical Systems. Progr. Natur. Sci., 1(2):105–116, (1991).   
[FQ91b] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FQ03] K. Feng and M. Z. Qin: Symplectic Algorithms for Hamiltonian Systems. Zhejiang Press for Science and Technology, Hangzhou, in Chinese, First edition, (2003).   
[Ge88] Z. Ge: Symplectic geometry and its application in numerical analysis. PhD thesis, Computer Center, CAS, (1988).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[GM88] Z. Ge and J. E. Marsden: Lie–Poisson Hamilton–Jacobi theory and Lie–Poisson integrators. Physics Letters A, pages 134–139, (1988).   
[GW95] Z. Ge and D.L. Wang: On the invariance of generating functions for symplectic transformations. Diff. Geom. Appl., 5:59–69, (1995).
