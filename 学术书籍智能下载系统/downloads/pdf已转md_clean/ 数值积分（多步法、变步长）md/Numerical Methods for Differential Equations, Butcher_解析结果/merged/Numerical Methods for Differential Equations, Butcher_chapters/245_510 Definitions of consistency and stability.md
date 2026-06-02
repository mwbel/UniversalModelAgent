# 510 Definitions of consistency and stability

Since a general linear method operates on a vector of approximations to some quantities computed in the preceding step, we need to decide something about the nature of this information. For most numerical methods, it is obvious what form this takes, but for a method as general as the ones we are considering here there are many possibilities. At least we assume that the $i$ th subvector in $y ^ { \lfloor n - 1 \rfloor }$ represents $u _ { i } y ( x _ { n - 1 } ) + v _ { i } h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { 2 } )$ . The vectors $u$ and $v$ are characteristic of any particular method, subject to the freedom we have to alter $v$ by a scalar multiple of $u$ ; because we can reinterpret the method by changing $x _ { n }$ by some fixed multiple of $h$ . The choice of $u$ must be such that the stage values are each equal to $y ( x _ { n } ) + O ( h )$ . This means that $U u = \mathbf { 1 }$ . We always require the output result to be $u _ { i } y ( x _ { n } ) + v _ { i } h y ^ { \prime } ( x _ { n } ) + O ( h ^ { 2 } )$ and this means that $V u = u$ and that $V v + B \mathbf { 1 } = u + v$ . If we are given nothing about a method except the four defining matrices, then $V$ must have an eigenvalue equal to 1 and $u$ must be a corresponding eigenvector. It then has to be checked that the space of such eigenvectors contains a member such that $U u = \mathbf { 1 }$ and such that $B { \bf 1 } - u$ is in the range of $V - I$ .

If a method has these properties then it is capable of solving $y ^ { \prime } = 1$ , with $y ( 0 ) = a$ exactly, in the sense that if $y _ { i } ^ { [ 0 ] } = u _ { i } a + v _ { i } h$ , then for all $n = 1$ , $2$ . . . , $y _ { i } ^ { \left[ n \right] } = u _ { i } { \left( a + n h \right) } + v _ { i } h$ . This suggests the following definitions:

Definition 510A A general linear method $( A , U , B , V )$ is ‘preconsistent’ if there exists a vector u such that

$$
\begin{array} { r } { V u = u , } \\ { U u = \mathbf { 1 } . } \end{array}
$$

The vector u is the ‘preconsistency vector’.

Definition 510B A general linear method $( A , U , B , V )$ is ‘consistent’ if it is preconsistent with preconsistency vector u and there exists a vector v such that

$$
B { \bf 1 } + V v = u + v .
$$

Just as for linear multistep methods, we need a concept of stability. In the general linear case this is defined in terms of the power-boundedness of $V$ and, as we shall see, is related to the solvability of the problem $y ^ { \prime } = 0$ .

Definition 510C A general linear method $( A , U , B , V )$ is ‘stable’ if there exists a constant $C$ such that, for all $n = 1 , 2 , \ldots$ , $\| V ^ { n } \| \leq C$ .
