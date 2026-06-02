# 7 Representations

The group $\mathbf { E M p } ( 2 n )$ of all unitary operators of the form

$$
U = \mathcal { U } ( t _ { 1 } , t _ { 0 } , H )
$$

where $\pmb { H }$ runs over the time dependent quadratic Hamiltonians and $t _ { 1 } , t _ { 0 }$ range over the real numbers form a finite dimensional group called the extended metaplectic goup. The subgroup $\mathbf { M } _ { \mathbf { P } } ( 2 n )$ obtained by taking only

homogeneous quadratic Hamiltonians $\pmb { H }$ in (10) is called the metaplectic group. The subgroup $\operatorname { H G } ( 2 n )$ obtained by taking only affine Hamiltonians $H$ in (10) is called the Heisenberg group. By Theorem 5.2 the map

$$
\mathrm { E M p } ( 2 n ) \to \mathrm { E S p } ( W , \hbar ) : \mathcal { U } ( t _ { 1 } , t _ { 0 } , H ) \mapsto \mathfrak { g } _ { t _ { 0 } } ^ { t _ { 1 } } ( H )
$$

is a well-defined double cover (which depends on $\pmb { \hbar }$ ). This repesentation of the double cover of the symplectic group is called Siegel-Shale-Weil representation or the metaplectic representation. The restriction of the double cover to the Heisenberg group is injective and the resulting representation is called the Heisenberg representation.

Here is a more explicit description of the Heisenberg representation. If $H$ is an affine Hamiltonian with constant coefficients then

$$
\mathcal { U } ( t , t _ { 0 } , H ) = \mathcal { T } ( ( t - t _ { 0 } ) H )
$$

where

$$
\begin{array} { r } { \mathcal { T } ( H ) = e ^ { - i H _ { 0 } / \hbar - i \langle H _ { x } , x \rangle / \hbar + i \langle H _ { x } , H _ { y } \rangle / 2 \hbar } f ( x - H _ { y } ) . } \end{array}
$$

If $\pmb { \Psi }$ is a symplectic matrix then the map $H \mapsto T ( H \circ \Psi )$ is another such representation corresponding to the same value of Planck's constant $\pmb { \hbar }$ By the Stone-von Neumann theorem these representations are unitarily isomorphic. In other words there exists a unitary operator $U : L ^ { 2 } ( \mathbb { R } ^ { n } ) \to L ^ { 2 } ( \mathbb { R } ^ { n } )$ ,unique up to multiplication by a complex number of modulus 1,such that

$$
\mathcal { T } ( H \circ \Psi ) = U ^ { - 1 } \circ \mathcal { T } ( H ) \circ U .
$$

Such an intertwining operator $\boldsymbol { U }$ may be taken as a lift of $\Psi$ to the metaplectic group. This is apparently how the metaplectic representation was discovered (see [23]). The elements of the metaplectic representation are thus viewed as intertwining operators of various incarnations of the Heisenberg representation. See [20] for an exposition in terms of co-adjoint orbits and polarizations.

# 8Quantum field theory

By generalizing from affne symplectomorphisms to affine symplectic relations it should be possible to generalize the extended metaplectic representation to the extended metaplectic functor. An extended Lagrangian subspace is a Legendrian submanifold of $W$ which covers an affine Lagrangian subspace of $\pmb { \mathbb { R } } ^ { 2 n }$ . A quadratic function $S : \mathbb { R } ^ { n }  \mathbb { R }$ determines an extended Lagrangian subspace $L ( S )$ via

$$
L ( S ) = \{ ( x , y , u ) \in W : y = \partial _ { x } S ( x ) , \ u = e ^ { i S ( x ) / \hbar } \} .
$$

An element of the extended symplectic group can be interpreted as an extended Lagrangian subspace of the external tensor product $W ^ { * } \otimes W$ over $\bar { \mathsf { R } } ^ { 2 n } \times \mathsf { R } ^ { 2 n }$ .(The bar indicates that the sign of the symplectic form in the first factor is reversed.） More generally given circle bundles $W _ { 0 } \to \mathbb { R } ^ { 2 n _ { 0 } }$ and $W _ { 1 } \to \mathbb { R } ^ { 2 n _ { 1 } }$ as in Section 6 let $W _ { 0 1 } \to \bar { { \bar { \mathsf { R } } } } ^ { 2 n _ { 0 } } \times { \bar { { \mathsf { R } } } } ^ { 2 n _ { 1 } }$ be endowed with the connection form ${ \pmb { \alpha } } _ { 1 } - { \pmb { \alpha } } _ { 0 }$ . Then an extended symplectic relation is an extended Lagrangian subspace of $\bar { \mathsf { R } } ^ { 2 n _ { 0 } } \times \mathsf { R } ^ { 2 n _ { 1 } }$ . Extended Lagrangian subspaces appear as the special case $n _ { 0 } = 0$ . The extended metaplectic functor assigns to each extended symplectic relation a distribution on $\mathbb { R } ^ { n _ { 0 } } \times \mathbb { R } ^ { n _ { 1 } }$ ,determined by the relation only up to a sign,and respecting the operation of composition defined in section 2.In the case of an extended symplectomorphism $g _ { t _ { 0 } } ^ { t _ { 1 } } ( H )$ the distribution is the distribution kernel of $\mathcal { U } ( t _ { 0 } , t _ { 1 } , H )$ . For a quadratic generating function $S ( { \boldsymbol { x } } )$ the distribution is $e ^ { i S ( x ) / \hbar }$ multiplied by a normalizing factor. Composition of extended symplectic relations corresponds to composition of distribution kernels; there should be a formula like

$$
\mathcal { U } ( R _ { 0 1 } \# R _ { 1 2 } ) = \mathrm { t r } ( \mathcal { U } ( R _ { 0 1 } ) \otimes \mathcal { U } ( R _ { 1 2 } ) ) .
$$

The extended metaplectic functor should give a simple model of Segal's axioms for topological quantum field theory. Taking the homology of a Riemann surface as the underlying symplectic vector space should lead to a $( 2 + 1 )$ dimensional theory. This is what Atiyah calls the Abelian case (without the lattice).

# References

[1] S. Albevario and R. Hoegh-Krohn,Feynman path integrals and the corresponding method of stationary phase,in Feynman Path Integrals,ed. S. Albevario et al, Springer Lecture Notes in Physics 106 (1978) 3-57.   
[2] M.F.Atiyah,The Geometry and Physics of Knots, Cambridge University Press,1990.   
[3] C. Conley and E. Zehnder,The Birkhoff-Lewis fixed point theorem and a conjecture of V.I. Arnold, Invent.Math.73 (1983), 33-49.   
[4] C.C. Conley and E.Zehnder,Morse-type index theory for flows and periodic solutions of Hamiltonian equations, Commun. Pure Appl. Math. 37 (1984), 207-253.   
[5] I.Daubechies and J.R.Klauder,Quantum mechanical path integrals with Wiener measure for all polynomial Hamiltonians,Phys. Rev Letters 52 (1984) 1161; J. Math. Physics 26 (1985) 2239-2256.   
[6] I.Daubechies,J.R. Klauder,and T. Paul,Wiener measures for path integrals with affine kinematic variables,J.Math.Physics 28 (1987) 85- 102.   
[7] P.A.M. Dirac, The Lagrangian in quantum mechanics, Phys. Zeitschr.d. Sovyetunion 3 (1933) 64-72.   
[8] J.J. Duistermaat, On the Morse index in variational calculus,Advances in Mathematics 21 (1976),173-195.   
[9] R.P. Feynman, Space-time approach to non-relativistic quantum mechanics,Rev. Mod.Phisics 20 (1948),367-387.   
[10] R.P. Feynman and A.R. Hibbs, Quantum Mechanics and Path Integrals, MacGraw-Hill,1965.   
[11] V. Guillemin and S. Sternberg, Geometric Asymptotics, AMS Math Surveys 14,1977.   
[12] V. Guillemin and S. Sternberg, Symplectic Techniques in Physics, Cambridge University Press,1984.   
[13] L. Hormander,Fourier integral operators I, Acta Math.127 (1971),79- 183.   
[14] J.B. Keller, Corrected Bohr-Sommerfeld quantum conditions for nonseparable systems,Annals of Physics 4 (1958),180-188.   
[15] B. Kostant,Quantization and unitary representations,in Modern Analysis and its Applications Springer Lecture Notes in Math 170 (1970) 87-207.   
[16] J.Leray, Lagrangian Analysis and Quantum Mechanics,MIT press,1981.   
[17] J.W.Robbin and D.A. Salamon,Path integrals on phase space and the metaplectic representation,Preprint,1992.   
[18] J.W.Robbin,and D.A.Salamon, The spectral fow and the Maslov index, Preprint 1992.   
[19] J.W. Robbin,and D.A. Salamon, A Maslov index for paths, Preprint 1992.   
[20] P.L. Robinson and J.H. Rawnsley, The metaplectic representation, $M p ^ { c }$ structures and geometric quantization ,Memoirs of the American Mathematical Society 81,1989.

[21] D. Salamon and E. Zehnder，Morse theory for periodic solutions of Hamiltonian systems and the Maslov index, to appear in Comm.Pure Appl. Math.

[22] I.E.Segal, Foundations of the theory of dynamical systems of infinitely many degrees of freedom (I)，Mat. Fys.Medd. Danske Vid. Selsk. 31 (1959) 1-39.

[23] IE. Segal, Transforms for operators and symplectic automorphisms over a locally compact abelian group,Math. Scand.13 (1963) 31-43.

[24] D.Shale,Linear symmetries of free boson felds, Trans. AMS 103 (1962), 149-167.

[25] J.M. Souriau, Structures des Systemes Dynamiques, Dunod,Paris,1970.

[26] J.M. Souriau, Construction explicite de 'indice de Maslov. Group Theoretical Methods in Physics Springer Lecture Notes in Physics 50 (1975), 117-148.

[27] A. Weil, Sur certaine groupes d'operateurs unitaires,Acta math 111 (1964),143-211.

[28] A. Weinstein, Lectures on Symplectic Manifolds, AMS Reg. Conf. Ser. Math. 29,1977.

# Symplectic Mappings which are Stable at Infinity Eduard Zehnder Eidg. Technische Hochschule, Zürich
