# 1 Introduction and main results

1． An important question of symplectic topology is the following: given a manifold, does it admit a Lagrangian embedding into $\mathbb { C } ^ { n } ?$ A series of obstructions to existence of such embeddings arises due to pure topological reasons (see M.Audin's paper [1] for a detailed discussion). However in [3] M.Gromov discovered an obstruction of another nature. Using infinite-dimensional analysis he showed that on every embedded Lagrangian submanifold of $\mathbf { C } ^ { n }$ there exists a cycle with positive symplectic area.Thus the first Betti number of a manifold admitting a Lagrangian embedding into $\mathbf { C } ^ { n }$ does not vanish.

Besides the symplectic area there is another remarkable first cohomology class on Lagrangian submanifold of $\mathbf { C } ^ { n }$ - the Maslov class.Recently different restrictions on the Maslov class of Lagrangian embeddings were discovered (see [7],[5],[6]). It is natural to suppose that they also lead to an obstruction to existence of Lagrangian embeddings. In the present paper we construct such obstruction (see theorem 1 below). We use it in order to show that certain flat manifolds do not admit Lagrangian embeddings into $\mathbf { C } ^ { n }$ (see theorems 2,3 below)．Our approach is based on the Maslov class rigidity phenomenon for manifolds of non-positive curvature which was discovered by C. Viterbo (see [7] and section 2.2 below).

I am deeply grateful to I.H.E.S. for hospitality and to B. Bowditch, M. Gromov,M. Kapovich,J.-C. Sikorav and C. Vitero for numerous useful consultations and discussions.

2.We describe our obstruction in the following:

Theorem 1. Let $X$ and $Y$ be closed manifolds of dimension n admitting Riemannian metrics of non-positive sectional curvature. Suppose that there exists a Lagrangian embedding $f : Y \to T ^ { * } X$ such that the following conditions hold:

(c1) the Maslov class of $\pmb { f }$ vanishes; (c2) the composition of $\pmb { f }$ with the natural projection $T ^ { * } X  X$ induce monomorphism $A : H ^ { 1 } ( X ; { \mathbf { Z } } ) \to H ^ { 1 } ( Y ; { \mathbf { Z } } )$ which “expands” in the following sense:

$$
A ( H ^ { 1 } ( X ; \mathbf { Z } ) ) \subset m H ^ { 1 } ( Y ; \mathbf { Z } )
$$

where m is a positive integer such that $m > ( n + 1 ) / 2$ if $X$ is orientable and $m > n + 1$ $X$ is non-orientable.

Then $X$ does not admit a Lagrangian embedding into $\mathbf { C } ^ { n }$

Here the Maslov class $\mu _ { f } \in H ^ { 1 } ( Y , \pmb { \cal { Z } } )$ of a Lagrangian embedding $\pmb { f }$ ： $Y  T ^ { \ast } X$ is defined as follows. If $\gamma : \mathbb { R } / \pmb { \mathrm { \sf { Z } } }  V$ is a loop then the vector bundle $V = ( f \circ \gamma ) ^ { * } T ( T ^ { * } X )$ over $\mathbf { R } / \mathbf { Z }$ with fibers $V ( t ) = T _ { f ( \gamma ( t ) ) } T ^ { \ast } X$ has two Lagrangian subbundles $\Lambda _ { 0 } ( t ) = T _ { f ( \gamma ( t ) ) } ^ { * } X$ and $\Lambda _ { 1 } ( t ) = { \mathrm { r a n g e } } \mathrm { d f } ( \gamma ( t ) )$ . The integer $\smash { \big \langle \mu _ { f } , \gamma \big \rangle }$ is the relative Maslov index of $\Lambda _ { 0 }$ and $\Lambda _ { 1 }$

Theorem 1 is proved in $\ S \ O ^ { 2 }$

3. We will now give an application of Theorem 1. Let ${ \mathsf { T } } ^ { n }$ be a torus with coordinates ${ \mathfrak { x } } _ { 1 } , \ldots , { \mathfrak { x } } _ { n }$ (mod 1).

Consider a map $\alpha : \mathsf { T } ^ { n } \to \mathsf { T } ^ { n }$ , given by

$$
( x _ { 1 } , x _ { 2 } , \ldots , x _ { n - 1 } , x _ { n } ) \mapsto ( x _ { 1 } + 1 / ( 2 n - 2 ) , x _ { 3 } , \ldots , x _ { n } , - x _ { 2 } ) .
$$

Note that $\pmb { \alpha }$ generates a group, say $G$ , of transformations of the torus which is isomorphic to $\mathbf { Z } _ { 2 n - 2 }$ and acts freely. Denote by $K ^ { n }$ the quotient ${ \mathsf { T } } ^ { n } / G$

Theorem 2. If $\pmb { n } \geq \mathbf { 3 }$ then $K ^ { n }$ does not admit a Lagrangian embedding into $\mathbb { C } ^ { n }$ .

Remark 1. The manifold $K ^ { 2 }$ is the Klein bottle. Unfortunately our obstruction does not work in this case.

Remark 2. The manifold $K ^ { 3 }$ is described in the book [8],p.117 (there it is called $\mathcal { G } _ { 4 }$ ). One can check that $K ^ { 3 }$ is orientable. Thus there is no “soft” obstructions to Lagrangian embeddings of $K ^ { 3 }$ into ${ \mathbb C } ^ { 3 }$ (see [1], 4.3.2.). This means that $K ^ { 3 }$ admits a Lagrangian immersion into $\mathbb { C } ^ { 3 }$ as well as a totally real embedding.Moreover $H ^ { 1 } ( K ^ { 3 } , { \pmb { \mathrm { Z } } } ) = { \pmb { \mathrm { Z } } }$ . Thus the symplectic area control does not give an obstruction in this case.

The proof of Theorem 2 and its generalisation for certain fat manifolds one can find in $\ S 3$
