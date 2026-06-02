# B Useful Mathematrics

# B.1 Conic Sections

The ellipse, the parabola, and the hyperbola are collectively known as conic sections, since these three types of curve can be obtained by taking various different plane sections of a right cone.

An ellipse, centered on the origin, of major radius a and minor radius b, which are aligned along the $x \cdot$ - and $_ { 9 }$ -axes, respectively (see Figure B.1), satisfies the following wellknown equation:

$$
{ \frac { \mathrm { x } ^ { 2 } } { \mathrm { a } ^ { 2 } } } + { \frac { \mathrm { y } ^ { 2 } } { \mathrm { b } ^ { 2 } } } = 1 .
$$

Likewise, a parabola which is aligned along the $+ x$ -axis, and passes through the origin (see Figure B.2), satisfies:

$$
y ^ { 2 } - { \mathsf { b } } x = 0 ,
$$

where $\mathbf b > 0$ .

Finally, a hyperbola which is aligned along the $+ x$ -axis, and whose asymptotes intersect at the origin (see Figure B.3), satisfies:

$$
{ \frac { \mathrm { x } ^ { 2 } } { \mathrm { a } ^ { 2 } } } - { \frac { \mathrm { y } ^ { 2 } } { \mathrm { b } ^ { 2 } } } = 1 .
$$

Here, a is the distance of closest approach to the origin. The asymptotes subtend an angle $\Phi = \tan ^ { - 1 } ( { \bf b } / { \bf a } )$ with the $x$ -axis.

It is not obvious, from the above formulae, what the ellipse, the parabola, and the hyperbola have in common. It turns out, in fact, that these three curves can all be represented as the locus of a movable point whose distance from a fixed point is in a constant ratio to its perpendicular distance to some fixed straight-line. Let the fixed point—which is termed the focus of the ellipse/parabola/hyperbola—lie at the origin, and let the fixed line—which is termed the directrix—correspond to $x = - \mathrm { d }$ (with ${ \mathrm { ~ d ~ } } > 0 .$ ). Thus, the distance of a general point $( x , \ y )$ (which lies to the right of the directrix) from the focus is $\mathsf r { r } _ { 1 } = \sqrt { \mathsf r ^ { 2 } + \mathsf y ^ { 2 } }$ , whereas the perpendicular distance of the point from the directrix is $\boldsymbol { \mathrm { r } } _ { 2 } = \boldsymbol { \mathrm { x } } + \boldsymbol { \mathrm { d } } .$ —see Figure B.4. In polar coordinates, ${ \mathfrak { r } } _ { 1 } = { \mathfrak { r } }$ and $\mathsf { r } _ { 2 } = \mathsf { r } \cos \theta + \mathrm { d }$ . Hence, the locus of a point for which $\boldsymbol { \mathrm { r } } _ { 1 }$ and $\boldsymbol { \mathrm { r } } _ { 2 }$ are in a fixed ratio satisfies the following equation:

$$
\frac { \mathsf { r } _ { 1 } } { \mathsf { r } _ { 2 } } = \frac { \sqrt { x ^ { 2 } + \mathsf { y } ^ { 2 } } } { x + \mathsf { d } } = \frac { \mathsf { r } } { \mathsf { r } \cos \theta + \mathsf { d } } = e ,
$$

where $e \geq 0$ is a constant. When expressed in terms of polar coordinates, the above equation can be rearranged to give

$$
{ \mathrm {  ~ \cal ~ r = ~ } } \frac { { \mathrm {  ~ \cal ~ r _ { c } ~ } } } { 1 - e \ \cos \theta } ,
$$

![](images/6608dc1f6da191d551cc18f2234c5f94f83814c7c113fb255aae8b7130253d4e.jpg)  
Figure B.1: An ellipse.

![](images/8f445d45fecfc3eaf191caeddbc5aace886235ab5282e3d23008b1381ff06334.jpg)  
Figure B.2: A parabola.

![](images/ff0d820fdfa576de3f37ed0fd0f2c962549efe0cc811c43e24617c2062b94a61.jpg)  
Figure B.3: A hyperbola.

![](images/b31b2ac128b9156c401a243cafbed1a8608bfafc771f764d8bd9a51517c273ed.jpg)  
Figure B.4: Conic sections in polar coordinates.

where $\boldsymbol { \Upsilon } _ { \mathrm { c } } = e \mathrm { d }$

When written in terms of Cartesian coordinates, (B.4) can be rearranged to give

$$
\frac { ( x - x _ { c } ) ^ { 2 } } { { \bf a } ^ { 2 } } + \frac { y ^ { 2 } } { { \bf b } ^ { 2 } } = 1 ,
$$

for $e < 1$ . Here,

$$
{ \begin{array} { l } { \displaystyle \mathbf { a } ~ = ~ { \frac { \mathsf { r } _ { \mathsf { c } } } { 1 - e ^ { 2 } } } , } \\ { \displaystyle { \mathsf { b } } ~ = ~ { \frac { \mathsf { r } _ { \mathsf { c } } } { \sqrt { 1 - e ^ { 2 } } } } = { \sqrt { 1 - e ^ { 2 } } } \mathbf { a } , } \\ { \displaystyle \mathbf { x } _ { \mathsf { c } } ~ = ~ { \frac { e \mathsf { r } _ { \mathsf { c } } } { 1 - e ^ { 2 } } } = e \mathbf { a } . } \end{array} }
$$

Equation (B.6) can be recognized as the equation of an ellipse whose center lies at $( x _ { \mathrm { { c } } } , \ 0 )$ , and whose major and minor radii, a and $\boldsymbol { \mathrm { b } }$ , are aligned along the $x \cdot$ - and $_ { 9 }$ -axes, respectively [cf., Equation (B.1)]. Note, incidentally, that an ellipse actually possesses two focii located on the major axis $( \mathfrak { y } = 0 )$ ) a distance e a on either side of the geometric center (i.e., at $x = 0$ and $x = 2 e \mathrm { a } .$ ).

When again written in terms of Cartesian coordinates, Equation (B.4) can be rearranged to give

$$
y ^ { 2 } - 2 r _ { \mathrm { c } } \left( x - x _ { \mathrm { c } } \right) = 0 ,
$$

for $e = 1$ . Here, $\mathtt { x } _ { \mathrm { c } } = - \mathtt { r } _ { \mathrm { c } } / 2$ . This is the equation of a parabola which passes through the point $( x _ { \mathrm { c } } , \ 0 )$ , and which is aligned along the $+ x$ -direction $[ c f .$ , Equation (B.2)].

Finally, when written in terms of Cartesian coordinates, Equation (B.4) can be rearranged to give

$$
\frac { ( x - x _ { c } ) ^ { 2 } } { { \bf a } ^ { 2 } } - \frac { { \bf y } ^ { 2 } } { { \bf b } ^ { 2 } } = 1 ,
$$

for $e > 1$ . Here,

$$
\begin{array} { r c l } { \mathbf { a _ { \tau } } } & { = } & { \displaystyle \frac { \boldsymbol { \Upsilon } _ { \mathrm { c } } } { e ^ { 2 } - 1 } , } \\ { \mathbf { b _ { \tau } } } & { = } & { \displaystyle \frac { \boldsymbol { \Upsilon } _ { \mathrm { c } } } { \sqrt { e ^ { 2 } - 1 } } = \sqrt { e ^ { 2 } - 1 } \mathbf { a } , } \\ { \boldsymbol { x } _ { \mathrm { c } } } & { = } & { \displaystyle - \frac { e \boldsymbol { \Upsilon } _ { \mathrm { c } } } { e ^ { 2 } - 1 } = - e \mathbf { a } . } \end{array}
$$

Equation (B.11) can be recognized as the equation of a hyperbola whose asymptotes intersect at $( x _ { \mathrm { { c } } } , \ 0 )$ , and which is aligned along the $+ x$ -direction. The asymptotes subtend an angle

$$
\Phi = \tan ^ { - 1 } \left( { \frac { \mathrm { b } } { \mathrm { a } } } \right) = \tan ^ { - 1 } ( { \sqrt { e ^ { 2 } - 1 } } )
$$

with the $x$ -axis $[ c f .$ , Equation (B.3)].

In conclusion, Equation (B.5) is the polar equation of a general conic section which is confocal with the origin (i.e., the origin lies at the focus). For $e < 1$ , the conic section is an ellipse. For $e = 1$ , the conic section is a parabola. Finally, for $e > 1$ , the conic section is a hyperbola.

# B.2 Matrix Eigenvalue Theory

Suppose that A is a real symmetric matrix of dimension n. If follows that $\mathbf { A } ^ { * } = \mathbf { A }$ and $\mathbf { A } ^ { \mathsf { T } } = \mathbf { A } .$ , where ∗ denotes a complex conjugate, and T denotes a transpose. Consider the matrix equation

$$
\mathbf { A } \mathbf { x } = \lambda \mathbf { x } .
$$

Any column vector $\mathbf { x }$ which satisfies the above equation is called an eigenvector of A. Likewise, the associated number $\lambda$ is called an eigenvalue of A. Let us investigate the properties of the eigenvectors and eigenvalues of a real symmetric matrix.

Equation (B.16) can be rearranged to give

$$
\left( \mathbf { A } - \lambda \mathbf { 1 } \right) \mathbf { x } = \mathbf { 0 } ,
$$

where 1 is the unit matrix. The above matrix equation is essentially a set of n homogeneous simultaneous algebraic equations for the n components of $\mathbf { x }$ . A well-known property of such a set of equations is that it only has a non-trivial solution when the determinant of the associated matrix is set to zero. Hence, a necessary condition for the above set of equations to have a non-trivial solution is that

$$
\left| \mathbf { A } - \lambda \mathbf { 1 } \right| = 0 .
$$

The above formula is essentially an nth-order polynomial equation for $\lambda$ . We know that such an equation has n (possibly complex) roots. Hence, we conclude that there are n eigenvalues, and n associated eigenvectors, of the ${ \mathfrak { n } }$ -dimensional matrix A.

Let us now demonstrate that the n eigenvalues and eigenvectors of the real symmetric matrix A are all real. We have

$$
\mathbf { A x } _ { \mathrm { { i } } } = \lambda _ { \mathrm { { i } } } \mathbf { x } _ { \mathrm { { i } } } ,
$$

and, taking the transpose and complex conjugate,

$$
\mathbf { x } _ { \mathrm { i } } ^ { * \top } \mathbf { A } = \lambda _ { \mathrm { i } } ^ { * } \mathbf { x } _ { \mathrm { i } } ^ { * \top } ,
$$

where $\mathbf { x } _ { \mathrm { i } }$ and $\lambda _ { \mathrm { i } }$ are the ith eigenvector and eigenvalue of $\mathbf { A }$ , respectively. Left multiplying Equation (B.19) by $\mathbf { x } _ { \mathrm { i } } ^ { \ast \intercal }$ , we obtain

$$
\mathbf { x } _ { \mathrm { i } } ^ { \mathrm { * } \top } \mathbf { A } \mathbf { x } _ { \mathrm { i } } = \lambda _ { \mathrm { i } } \mathbf { x } _ { \mathrm { i } } ^ { \mathrm { * } \top } \mathbf { x } _ { \mathrm { i } } .
$$

Likewise, right multiplying (B.20) by $\mathbf { x } _ { \mathrm { i } }$ , we get

$$
\mathbf { x } _ { \mathrm { i } } ^ { \mathrm { * } \top } \mathbf { A } \mathbf { x } _ { \mathrm { i } } = \lambda _ { \mathrm { i } } ^ { \mathrm { * } } \mathbf { x } _ { \mathrm { i } } ^ { \mathrm { * } \top } \mathbf { x } _ { \mathrm { i } } .
$$

The difference of the previous two equations yields

$$
\begin{array} { r } { ( \lambda _ { \mathrm { i } } - \lambda _ { \mathrm { i } } ^ { * } ) \mathbf { x } _ { \mathrm { i } } ^ { * } { } ^ { \mathsf { T } } \mathbf { x } _ { \mathrm { i } } = 0 . } \end{array}
$$

It follows that $\lambda _ { \mathrm { i } } = \lambda _ { \mathrm { i } } ^ { \ast }$ , since $\mathbf { x } _ { \mathrm { i } } ^ { * \mathsf { T } } \mathbf { x } _ { \mathrm { i } }$ (which is $\mathbf { x } _ { \mathrm { i } } ^ { * } \cdot \mathbf { x } _ { \mathrm { i } }$ in vector notation) is positive definite.   
Hence, $\lambda _ { \mathrm { i } }$ is real. It immediately follows that $\mathbf { x } _ { \mathrm { i } }$ is real.

Next, let us show that two eigenvectors corresponding to two different eigenvalues are mutually orthogonal. Let

$$
\begin{array} { r l r } { { \bf A } { \bf x } _ { \mathrm { i } } } & { = } & { \lambda _ { \mathrm { i } } { \bf x } _ { \mathrm { i } } , } \\ { { \bf A } { \bf x } _ { \mathrm { j } } } & { = } & { \lambda _ { \mathrm { j } } { \bf x } _ { \mathrm { j } } , } \end{array}
$$

where $\lambda _ { \mathrm { i } } \neq \lambda _ { \mathrm { j } }$ . Taking the transpose of the first equation and right multiplying by $\mathbf { x } _ { \mathrm { j } }$ , and left multiplying the second equation by $\mathbf { x } _ { \mathrm { i } } ^ { \mathsf { T } }$ , we obtain

$$
\begin{array} { r l r } { { \bf x } _ { \mathrm { i } } ^ { \top } { \bf A } { \bf x } _ { \mathrm { j } } } & { = } & { \lambda _ { \mathrm { i } } { \bf x } _ { \mathrm { i } } ^ { \top } { \bf x } _ { \mathrm { j } } , } \\ { { \bf x } _ { \mathrm { i } } ^ { \top } { \bf A } { \bf x } _ { \mathrm { j } } } & { = } & { \lambda _ { \mathrm { j } } { \bf x } _ { \mathrm { i } } ^ { \top } { \bf x } _ { \mathrm { j } } . } \end{array}
$$

Taking the difference of the above two equations, we get

$$
\begin{array} { r } { ( \lambda _ { \mathrm { i } } - \lambda _ { \mathrm { j } } ) \mathbf { x } _ { \mathrm { i } } ^ { \top } \mathbf { x } _ { \mathrm { j } } = 0 . } \end{array}
$$

Since, by hypothesis, $\lambda _ { \mathrm { i } } \neq \lambda _ { \mathrm { j } }$ , it follows that $\mathbf { x } _ { \mathrm { i } } ^ { \mathsf { T } } \mathbf { x } _ { \mathrm { j } } = 0$ . In vector notation, this is the same as $\mathbf { x } _ { \mathrm { { i } } } \cdot \mathbf { x } _ { \mathrm { { j } } } = 0$ . Hence, the eigenvectors $\mathbf { x } _ { \mathrm { i } }$ and $\mathbf { x } _ { \mathrm { j } }$ are mutually orthogonal.

Suppose that $\lambda _ { \mathrm { i } } = \lambda _ { \mathrm { j } } = \lambda$ . In this case, we cannot conclude that $\mathbf { x } _ { \mathrm { i } } ^ { \mathsf { T } } \mathbf { x } _ { \mathrm { j } } = 0$ by the above argument. However, it is easily seen that any linear combination of $\mathbf { x } _ { \mathrm { i } }$ and $\mathbf { x } _ { \mathrm { j } }$ is an eigenvector of A with eigenvalue $\lambda$ . Hence, it is possible to define two new eigenvectors of A, with the eigenvalue $\lambda$ , which are mutually orthogonal. For instance,

$$
\begin{array} { r c l } { \mathbf { x } _ { \mathrm { i } } ^ { \prime } } & { = } & { \mathbf { x } _ { \mathrm { i } } , } \\ { \mathbf { x } _ { \mathrm { j } } ^ { \prime } } & { = } & { \mathbf { x } _ { \mathrm { j } } - \left( \frac { \mathbf { x } _ { \mathrm { i } } ^ { \intercal } \mathbf { x } _ { \mathrm { j } } } { \mathbf { x } _ { \mathrm { i } } ^ { \intercal } \mathbf { x } _ { \mathrm { i } } } \right) \mathbf { x } _ { \mathrm { i } } . } \end{array}
$$

It should be clear that this argument can be generalized to deal with any number of eigenvalues which take the same value.

In conclusion, a real symmetric n-dimensional matrix possesses n real eigenvalues, with n associated real eigenvectors, which are, or can be chosen to be, mutually orthogonal.