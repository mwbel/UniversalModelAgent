# 7.6.3 Numerical methods based on local charts

A straightforward approach to discretization can be based on a symplectic atlas: simply parameterize the phase space $\mathcal { P }$ in local charts, and then solve the resulting (unconstrained) Hamiltonian systems in the parameters using a symplectic integrator.

Several problems with this approach surface rapidly when one attempts to use it to perform a simulation. These include the difficulty of identifying the boundaries of the local charts for the manifold in a general purpose numerical integration framework and the potential additional computational complexity that may be introduced in the parametric vector fields.

In the Hamiltonian setting, there is an additional difficulty introduced by parameterization. According to the results of the last section, the Hamiltonian that arises via a canonical parameterization is typically nonseparable. This generally occurs in the presence of a nonlinear constraint regardless of whether the original Hamiltonian was separable. Nonseparable Hamiltonian functions are, typically much more difficult to integrate than separable Hamiltonian functions because they require the use of an implicit scheme (whereas separable Hamiltonian functions can be treated with explicit integrators).

However, as explained by LEIMKUHLER AND REICH [111], there is still one more serious drawback to using parameterizations to integrate a Hamiltonian system, having to do with the “nearby Hamiltonian” introduced in Chapter 5. Recall that a key feature of a symplectic integrator is that it generates the exact flow, up to an exponentially small error term, of a nearby Hamiltonian system. Thus taking many steps with the same symplectic integrator is the same as taking many steps along the flow of the perturbed Hamiltonian system. This implies the existence of a conserved quantity, not much different from the exact energy, and confers a certain long-term stability on the numerical simulation and, consequently, a certain structural stability of the system under the process of discretization.

When the numerical solution is obtained by integrating the differential equations in local minimal coordinates (local charts), we find that the symplectic map associated to the numerical simulation changes whenever we switch to a new chart: the realization as the flow of a single Hamiltonian system therefore does not apply. Thus the perturbed conserved quantity is lost, and the result observed in practice is typically a loss of long-term stability. The only exception to this rule is provided if one can find local coordinates in which one can integrate the equations of motion exactly. Then the modified Hamiltonian is the same as the original energy function and a change of charts does not affect conservation of energy. This obvious statement has some importance for the implementation of splitting methods in local coordinates (see BENETTIN, CHERUBINI, AND FASSO\` [17]).

In summary, as a general proposition, use of local coordinate charts as a basis for numerical integration is unwise for the following reasons:

Identifying the boundaries of local charts and switching between separate coordinate charts in the course of a simulation can introduce a costly computational overhead. Missed chart changes may lead to singularities in the solutions of the differential equations. The use of a parametrization often adds significant computational complexity, e.g. by introducing transcendental functions into a vector field where only simple polynomials may otherwise be needed.   
. Finally, the use of parameterized equations may greatly limit the possibilities for obtaining efficient geometric numerical integrators respecting other invariants of the flow.

Despite these pessimistic comments, parameterizations may sometimes be used effectively in special applications for which the constraint geometry is well understood, or for which the choice of appropriate parameters greatly simplifies the description of the vector field.

# 7.6.4 Methods based on projection

Because the flow of the underlying ordinary differential equations (7.9)–(7.10) has the tangent bundle $\tau { \mathcal { M } }$ as an invariant submanifold, this formulation is sometimes proposed as the basis for numerical simulation. However, it is important to note that $T \mathcal { M }$ will typically not be an invariant submanifold for the discretization method applied to those equations. This means that the numerical solution, started from initial conditions in $T \mathcal { M }$ may drift gradually off the manifold and into the larger Euclidean space in which the flow is embedded. One way around this problem is to project the numerical solution back on to $\tau { \mathcal { M } }$ at the end of each timestep [84] or to stabilize the manifold [10].

# 7.7 Exercises

1. Local charts. It is also possible to describe the pendulum in terms of just two Euclidean charts as follows (refer to Fig. 7.7). In the first chart, we identify a point $Q ( x , y )$ of the unit circle with a point on the real line $\xi$ by passing a line through $Q$ and the point at the top of the unit circle $N$ and letting $R$ denote the point of intersection with the $x$ -axis. This works for all points $Q$ on the unit circle except $N$ itself. In the other chart, we identify points of the unit circle to points of the $x - \mathsf { a x i s }$ in the same way, except that we use the “south pole” $S$ instead of $N$ as a point of the straight line.

![](images/c2ee208b98a31710704cd709ca32810294d32175a46a37271a671f5acf273ba9.jpg)  
Figure 7.7 Parametrization of the circle in two charts on the real line.

a. Write out formulas for these two parameterizations and determine the canonical equations for the pendulum problem in each chart.   
b. Discretize the equations using the implicit midpoint rule and device a proper criterion to switch from one chart to the other. Perform a numerical experiment with $g = 0$ and $( q _ { 1 } ( 0 ) , q _ { 2 } ( 0 ) , p _ { 1 } ( 0 ) , p _ { 2 } ( 0 ) ) = ( 1 , 0 , 0 , - 2 )$ . Monitor the total energy.   
c. Repeat the experiment under (b) with a SHAKE/RATTLE discretization of the constrained formulation for the pendulum.

2. Regularity of constraints. Let $M$ be a symmetric positive definite matrix. Show that the matrix $G M ^ { - 1 } G ^ { T }$ is nonsingular provided the matrix $\pmb { G }$ has full rank (i.e. has linearly independent rows).

3. Time-reversibility. Show that SHAKE and RATTLE are time-reversible.

4. Linear stability analysis. Consider the linearly constrained system with equations of motion

$$
\begin{array} { r } { \dot { x } = u , } \\ { \dot { y } = v , } \\ { \dot { u } = - \omega _ { 1 } ^ { 2 } x - \alpha \lambda , } \\ { \dot { v } = - \omega _ { 2 } ^ { 2 } y - \beta \lambda , } \\ { \alpha x + \beta y = 0 , } \end{array}
$$

where $\alpha , \beta , \omega _ { 1 }$ and $\omega _ { 2 }$ are real numbers, and we will assume the normalization $\alpha ^ { 2 } + \beta ^ { 2 } = 1$ .

a. Eliminate the multiplier (by twice differentiating the constraint relationship with respect to time) to obtain

$$
\lambda = \alpha \omega _ { 1 } ^ { 2 } x + \beta \omega _ { 2 } ^ { 2 } y .
$$

b. Next, assume $\beta \neq 0$ , and solve the constraint for $y$ in terms of $x$ (this is a global parameterization). Show that the equations of motion reduce to

$$
\begin{array} { l } { \dot { x } = u , } \\ { \dot { u } = - \left( ( 1 - \alpha ^ { 2 } ) \omega _ { 1 } ^ { 2 } + \alpha ^ { 2 } \omega _ { 2 } ^ { 2 } \right) ) x , } \end{array}
$$

which describes a new harmonic oscillator with frequency

$$
\bar { \omega } = \sqrt { ( 1 - \alpha ^ { 2 } ) \omega _ { 1 } ^ { 2 } + \alpha ^ { 2 } \omega _ { 2 } ^ { 2 } } .
$$

c. Apply the RATTLE discretization to the constrained system, resulting in

$$
\begin{array} { c } { { x ^ { n + 1 } = x ^ { n } + \Delta t u ^ { n + 1 / 2 } , } } \\ { { y ^ { n + 1 } = y ^ { n } + \Delta t v ^ { n + 1 / 2 } , } } \\ { { u ^ { n + 1 / 2 } = u ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \omega _ { 1 } ^ { 2 } x ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \alpha \lambda _ { ( r ) } ^ { n } , } } \\ { { v ^ { n + 1 / 2 } = v ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \omega _ { 2 } ^ { 2 } y ^ { n } - \displaystyle \frac { 1 } { 2 } \Delta t \beta \lambda _ { ( r ) } ^ { n } , } } \\ { { \alpha x ^ { n + 1 } + \beta y ^ { n + 1 } = 0 , } } \end{array}
$$

and

$$
\begin{array} { c } { { u ^ { n + 1 } = u ^ { n + 1 / 2 } - \displaystyle \frac { 1 } { 2 } \Delta t \omega _ { 1 } ^ { 2 } x ^ { n + 1 } - \displaystyle \frac { 1 } { 2 } \Delta t \alpha \lambda _ { ( \mathrm { v } ) } ^ { n + 1 } , } } \\ { { v ^ { n + 1 } = v ^ { n + 1 / 2 } - \displaystyle \frac { 1 } { 2 } \Delta t \omega _ { 2 } ^ { 2 } y ^ { n + 1 } - \displaystyle \frac { 1 } { 2 } \Delta t \beta \lambda _ { ( \mathrm { v } ) } ^ { n + 1 } , } } \\ { { \alpha u ^ { n + 1 } + \beta v ^ { n + 1 } = 0 . } } \end{array}
$$

Assume $\alpha x ^ { n } + \beta y ^ { n } = 0$ and also $\alpha u ^ { n } + \beta v ^ { n } = 0$ , so that

$$
\lambda _ { ( \mathfrak { r } ) } ^ { n } = \alpha \omega _ { 1 } ^ { 2 } x ^ { n } + \beta \omega _ { 2 } ^ { 2 } y ^ { n } .
$$

Find a similar expression for $\lambda _ { ( \vee ) } ^ { n + 1 }$

Show that RATTLE reduces in the coordinates $x ^ { n } , \ u ^ { n }$ , to a St¨ormer– Verlet discretization of the harmonic oscillator with frequency $\bar { \omega }$ . What can you conclude about possible stepsize restrictions?

e. Repeat the discussion for RATTLE replaced by the implicit midpoint method as the basic integration method in (7.39)–(7.43).

5. Constraint chains. The iteration matrix

$$
\pmb { R } = \pmb { G } ( \pmb { q } ^ { n } ) \pmb { M } ^ { - 1 } \pmb { G } ( \pmb { q } ^ { n } ) ^ { T }
$$

appearing in a quasi-Newton method for SHAKE takes a particularly simple form for problems only involving length constraints. We can write these constraints in the following compact form

$$
g _ { i } = \frac { 1 } { 2 } ( \pmb { q } ^ { T } S _ { i } \pmb { q } - L _ { i } ^ { 2 } ) ,
$$

where $L _ { j }$ is the length of the constraint, and $S _ { j }$ is a $d \times d$ stamp matrix with $3 \times 3$ blocks. This matrix is zero in all but the following components: if the i th constraint links particles $k$ and $I$ , then the $k k$ and $I I$ blocks of $S _ { j }$ are $\boldsymbol { I } _ { 3 }$ ( $3 \times 3$ identity matrix) and the $k I$ and $I k$ blocks are $- I _ { 3 }$ . With this notation it is easy to show that the $i j$ element $R _ { i j }$ of $R$ has the form

$$
\begin{array} { r } { R _ { i j } = \pmb q ^ { T } S _ { i } \pmb { M } ^ { - 1 } S _ { j } \pmb q . } \end{array}
$$

This implies in turn that

$$
R _ { i i } = ( \frac { 1 } { m _ { \mathsf { \tiny { l e f t } } ( i ) } } + \frac { 1 } { m _ { \mathsf { \tiny { r i g h t } } ( i ) } } ) L _ { i } ^ { 2 } ,
$$

where left $( i )$ and right $( i )$ represent the two particle indices associated to constraint $j$ . Now $R _ { i j }$ is zero unless constraints $j$ and $j$ share a common particle. If right $\displaystyle ( i ) = \mathsf { l e f t } ( j )$ , then we can write

$$
\begin{array} { l } { { R _ { i j } = \displaystyle \frac { 1 } { m _ { \mathrm { l e f t } ( j ) } } ( \pmb { q } _ { \mathrm { l e f t } ( i ) } - \pmb { q } _ { \mathrm { r i g h t } ( i ) } ) ^ { T } ( \pmb { q } _ { \mathrm { l e f t } ( j ) } - \pmb { q } _ { \mathrm { r i g h t } ( j ) } ) } } \\ { { \displaystyle \ = \frac { 1 } { m _ { \mathrm { l e f t } ( j ) } } r _ { i } r _ { j } \cos \theta _ { i j } } } \end{array}
$$

with $r _ { i } = \lVert \pmb { q } _ { \mathrm { l e f t } ( i ) } - \pmb { q } _ { \mathrm { r i g h t } ( i ) } \rVert$ , $r _ { j } = \lVert \pmb { q } _ { \mathrm { l e f t } ( j ) } - \pmb { q } _ { \mathrm { r i g h t } ( j ) } \rVert$ and $\theta _ { j j }$ is the angle between the two constraints $j$ and $j$ . Now along solutions of the constrained equations, we know that $r _ { i } \equiv L _ { j }$ , etc.

a. Consider a system of three particles of equal mass connected by two rigid length constraints of equal length. Find an explicit expression for the associated $2 \times 2$ matrix $R$ .   
b. Implement the SHAKE time discretization and apply (i) a quasi-Newton method and (ii) SHAKE iteration to solve the nonlinear constraint equations. Compare the two approaches in terms of efficiency.   
c. Consider a system of three particles of equal mass connected by three rigid length constraints of equal length. Repeat exercises (a) and (b).

# 8

Rigid body dynamics

In this chapter, we discuss formulation issues and symplectic integration methods for simulating the motion of a rigid body. Rigid bodies arise frequently in engineering, chemistry, and physics. For example, they occur in molecular simulation when the flexibility of small polyatomic units such as the water molecule, or $\mathsf { C H } _ { 4 }$ is ignored. Cogwheels, space vehicles, and the planets are some other objects that are commonly modeled by rigid bodies.

Even in the absence of external applied forces, any rigid body more complicated than a uniform sphere will exhibit complicated motion, as defined by the moments of inertia of the body. A hint of the potential complexity of the motion is provided by the classic illustration using a hardbound book, which typically has three unequal moments of inertia $I _ { 1 } < I _ { 2 } < I _ { 3 }$ with $I _ { 1 }$ corresponding to an axis drawn along the binding, $I _ { 2 }$ to an axis across the cover, and $I _ { 3 }$ to an axis through the pages of the book (see Fig. 8.1). As the book is tossed up and spinning around each of the axes, the following dynamics are observed: around the first and third axes, the motion combines a stable periodic rotation with the rising and falling motion due to gravity, whereas the rotation with respect to the middle axis is much more complicated. (See, for example, [124] for more explanation.) (It helps to place a rubber band around the book’s cover to keep it closed while conducting experiments.)

Developing a method to simulate general rigid body motions, especially for long-term integration, proves an interesting and challenging task. The first issue we must confront is the selection of a set of coordinates that describe body orientation and spatial position. Since a rigid body has six degrees of freedom, the positional description must include at least this many configuration variables. For example, a rigid body can be formulated in terms of three Euler angles describing the orientation in space relative to a reference configuration defined in terms of a certain sequence of axial rotations together with the three coordinates of the center of mass. However, if these variables, together with the corresponding momenta, are selected as the basis for a canonical description of the motion of the body, the resulting equations of motion are found to have singularities which impede their numerical solution.

![](images/0104234118f2a0543a8146406cec7cba6e3a901a30b9c1d1729995379f93d04a.jpg)  
Figure 8.1 A hardbound book tossed up and spinning about one of its axes of inertia provides a simple illustration of rigid body motion.

To overcome this defect of the Euler angles, it is possible – and often desirable – to introduce additional redundant variables together with constraints. We will develop various approaches by relating them to a natural canonical formulation of the rigid body dynamics in terms of rotation matrices: the Lie group $S O ( 3 )$ consisting of $3 \times 3$ orthogonal matrices with unit determinant.1 This is a global coordinatization in the language of the last chapter. The rotational kinetic energy term of the Lagrangian can be written in these variables simply as

$$
\mathcal { L } _ { \mathrm { { r o t } } } = \frac { 1 } { 2 } \mathrm { t r a c e } ( \dot { Q } R \dot { Q } ^ { T } ) ,
$$

where $Q$ is subject to an orthogonality constraint $Q ^ { T } Q = I _ { 3 }$ , $\boldsymbol { I } _ { 3 }$ the $3 \times 3$ identity matrix, and $R$ is a constant $3 \times 3$ matrix closely related to the “inertia tensor” of the body.

In addition to the rotation matrix formulation, other popular choices of parameterization of rigid body motion include Hamilton’s quaternions (Cayley– Klein parameters) and cartesian (particle) models. Another formulation is based on the Euler equations, which can be obtained by a formal reduction procedure. In principle, any of these formulations can be used with a variety of timestepping methods. However, the choice of parameterization and the design of a discretization method are not independent. We will see that some sets of parameters facilitate efficient symplectic/reversible discretization while others may make this task difficult or render the resulting schemes useless because of the computational expense involved.

# 8.1 Rigid bodies as constrained systems

We now consider the formulation of the equations of motion for a single rigid body acted on by a (possibly nonlinear) potential field. The basic ideas naturally extend to systems of interacting rigid bodies.

The definition of a rigid body (see [104, 7, 2]) is simply a set of particles of prescribed mass whose positions are relatively fixed in space. Assume for the moment that the number of particles is finite, and that their instantaneous positions are $\pmb { q } _ { i }$ , $i = 1 , \dots , k$ . The kinetic energy of this collection is given by $\textstyle T = \sum _ { i = 1 } ^ { k } m _ { i } \| { \dot { \pmb q } } _ { i } \| ^ { 2 }$ , and the potential by $V = V ( \pmb q _ { 1 } , \pmb q _ { 2 } , \dots , \pmb q _ { k } )$ .

Define by $\pmb q _ { \mathrm { c m } }$ the center of mass of the set of particles:

$$
\pmb { q } _ { \mathrm { c m } } = \frac { \sum _ { i = 1 } ^ { k } m _ { i } \pmb { q } _ { i } } { \sum _ { i = 1 } ^ { k } m _ { i } } .
$$

In a fixed reference configuration $( r _ { 1 } ^ { 0 } , r _ { 2 } ^ { 0 } , \ldots , r _ { k } ^ { 0 } )$ the center of mass is located at the origin. Any possible configuration of the particles of the rigid body can be expressed in terms of two types of elementary motions applied to some reference configuration: a common rotation of each of the particles of the body about the center of mass followed by a common translation in space of each particle. Let $Q$ denote an orthogonal $3 \times 3$ matrix with unit determinant, i.e. a rotation matrix with respect to vectors in $\mathbb { R } ^ { 3 }$ , and let $\pmb { d } \in \mathbb { R } ^ { 3 }$ be a displacement, then we may write

$$
\pmb { q } _ { i } = \pmb { Q } r _ { i } ^ { 0 } + \pmb { d } .
$$

If we view the points of the body as moving in space along some smooth trajectory, we can imagine a corresponding trajectory in the orientation $Q$ and spatial position $\pmb { d }$ , i.e.

$$
\pmb { q } _ { i } ( t ) = \pmb { Q } ( t ) \pmb { r } _ { i } ^ { 0 } + \pmb { d } ( t ) .
$$

Since $\pmb { q } _ { i } ( t ) = \pmb { q } _ { \mathsf { c m } } ( t )$ for $r _ { i } ^ { 0 } = \mathbf { 0 }$ , we have $\pmb { d } ( t ) = \pmb { q } _ { \mathsf { c m } } ( t )$ and the velocities therefore satisfy

$$
\frac { d } { d t } { \pmb q } _ { i } ( t ) = \dot { { \pmb q } } _ { \mathtt { c m } } ( t ) + \dot { { \pmb Q } } ( t ) { \pmb r } _ { i } ^ { 0 } ,
$$

so the kinetic energy can be written as

$$
T = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { k } m _ { i } \| \dot { \pmb q } _ { \mathrm { c m } } ( t ) + \dot { \pmb Q } ( t ) { \pmb r } _ { i } ^ { 0 } \| ^ { 2 } .
$$

Expanding the squared two-norm using the properties of the inner product, we find

$$
T = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { k } m _ { i } ( \| \dot { \pmb q } _ { \mathrm { c m } } ( t ) \| ^ { 2 } + 2 \dot { \pmb q } _ { \mathrm { c m } } ( t ) \cdot [ \dot { \pmb Q } ( t ) \pmb r _ { i } ^ { 0 } ] + \| \dot { \pmb Q } ( t ) \pmb r _ { i } ^ { 0 } \| ^ { 2 } ) .
$$

Now the middle term in this expression vanishes, since

$$
\sum _ { i = 1 } ^ { k } m _ { i } \dot { \pmb q } _ { \mathrm { c m } } ( t ) \cdot [ \dot { \pmb Q } ( t ) \pmb r _ { i } ^ { 0 } ] = \dot { \pmb q } _ { \mathrm { c m } } ( t ) \cdot [ \dot { \pmb Q } ( t ) \sum _ { i = 1 } ^ { k } m _ { i } \pmb r _ { i } ^ { 0 } ] = 0 ,
$$

as $( r _ { 1 } ^ { 0 } , \ldots , r _ { k } ^ { 0 } )$ is a reference configuration, i.e. $\textstyle \sum _ { i } m _ { i } r _ { i } ^ { 0 } = \mathbf { 0 }$ .

We can now define translation and rotational parts of the kinetic energy b

$$
T _ { \mathrm { t r a n s } } = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { k } m _ { i } \lVert \dot { \pmb q } _ { \mathrm { c m } } \rVert ^ { 2 } ,
$$

and

$$
T _ { \mathrm { r o t } } = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { k } m _ { i } \lVert \dot { \pmb { Q } } r _ { i } ^ { 0 } \rVert ^ { 2 } .
$$

To express the rotational kinetic energy more compactly, observe the following identity of linear algebra: for any pair of vectors $\pmb { u }$ , $\pmb { v } \in \mathbb { R } ^ { k }$

$$
\pmb { u } ^ { T } \pmb { v } = \mathrm { t r } \left( \pmb { u } \pmb { v } ^ { T } \right) ,
$$

where $\operatorname { t r } ( A )$ represents the trace (sum of diagonal elements) of a matrix A. Using this fact, we have

$$
\begin{array} { l } { { \displaystyle { T _ { \mathrm { r o t } } = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { K } m _ { i } \| Q { \bf r } _ { i } ^ { 0 } \| ^ { 2 } } } \ ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { K } m _ { i } \left[ Q { \bf r } _ { i } ^ { 0 } \right] ^ { T } \left[ \hat { Q } { \bf r } _ { i } ^ { 0 } \right] } \ ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { K } m _ { i } \mathrm { t r } \left( \left[ \hat { Q } { \bf r } _ { j } ^ { 0 } \right] \left[ \hat { Q } { \bf r } _ { i } ^ { 0 } \right] ^ { T } \right) } \ ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { K } m _ { i } \mathrm { t r } \left( Q { \bf r } _ { j } ^ { 0 } [ { \bf r } _ { i } ^ { 0 } ] ^ { T } { \hat { Q } } ^ { T } \right) } \ ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { K } \left( R { \cal Q } { \bf R } { \cal Q } ^ { T } \right) } \ ~ , } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \mathrm { t r } \left( Q R { \cal Q } ^ { T } \right) } \ ~ . } \  \end{array}
$$

where we have defined the symmetric matrix $R$ by

$$
R = \sum _ { i = 1 } ^ { k } m _ { i } r _ { i } ^ { 0 } [ r _ { i } ^ { 0 } ] ^ { T } .
$$

The matrix $R$ can be viewed as a mass-weighted sum of projections along the displacements of points in the reference configuration. We will refer to $R$ as the mass tensor of the body.2

Since $R$ is symmetric one can always find a reference coordinate system $\bar { e } _ { i }$ , $i = 1 , 2 , 3$ , so that $R$ is diagonal with diagonal entries $r _ { i j }$ , $j = 1 , 2 , 3$ . Note that the coordinate system is held fixed on the rigid body contrary to a laboratory coordinate system which is fixed in space. The mass tensor $R$ can now be written as

$$
R = \sum _ { i = 1 } ^ { 3 } r _ { i i } \bar { e } _ { i } \bar { e } _ { i } ^ { T } = \left[ \begin{array} { c c c } { { r _ { 1 1 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { r _ { 2 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { r _ { 3 3 } } } \end{array} \right] .
$$

We will see later in this chapter that this particular choice of the reference system is equivalent to the statement that the inertia tensor of the rigid body is also diagonal with the principal moments of inertia equal to $I _ { 1 } ~ = ~ r _ { 2 2 } +$ $r _ { 3 3 }$ , $\begin{array} { r } { I _ { 2 } ~ = ~ r _ { 1 1 } + r _ { 3 3 } } \end{array}$ , and $\begin{array} { r } { I _ { 3 } ~ = ~ r _ { 1 1 } + r _ { 2 2 } } \end{array}$ . From now on we will assume that all matrices are expressed with respect to the reference coordinate system $\bar { e } _ { i }$ , $i = 1 , 2 , 3$ .

In the given variables, the Lagrangian becomes

$$
L = T _ { \mathrm { r o t } } ( \dot { \bf Q } ) + T _ { \mathrm { t r a n s } } ( \dot { \bf q } _ { \mathrm { c m } } ) - V _ { \mathrm { e x t } } ( \pmb { Q } , \pmb { q } _ { \mathrm { c m } } ) ,
$$

where $V _ { \mathrm { e x t } }$ is the potential energy function expressed in terms of the center of mass of the collection of particles and the rotation matrix. We must bear in mind, however, that this Lagrangian is subject to a holonomic constraint: the condition that $Q$ must be an orthogonal matrix!

In order to formulate the constraint and augmented Lagrangian, we note that the orthogonality condition on $Q$

$$
Q ^ { T } Q = I _ { 3 } ,
$$

gives rise to six independent constraints on the matrix $Q$ , so six multipliers are needed. These can be introduced in the form of the six independent elements of a symmetric matrix $\pmb { \Lambda }$ , with the augmented Lagrangian having the simple

expression

$$
\tilde { L } = T _ { \mathrm { r o t } } ( \dot { Q } ) + T _ { \mathrm { t r a n s } } ( \dot { q } _ { \mathrm { c m } } ) - V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) - \mathrm { t r } ( ( Q ^ { T } Q - I _ { 3 } ) \varLambda ) .
$$

# 8.1.1 Hamiltonian formulation

Recall that the gradient $\nabla _ { q } V ( q )$ of a scalar-valued function $V ( q )$ is defined by

$$
\langle \nabla _ { \pmb { q } } V ( \pmb { q } ) , \delta \pmb { q } \rangle = \operatorname* { l i m } _ { \varepsilon  0 } \frac { V ( \pmb { q } + \varepsilon \delta \pmb { q } ) - V ( \pmb { q } ) } { \varepsilon } .
$$

Since we will now work with matrices, we have to introduce an appropriate inner product. Throughout this chapter we will use

$$
\langle \pmb { A } , \pmb { B } \rangle = \mathrm { t r } ( \pmb { A } \pmb { B } ^ { T } )
$$

for any two $3 \times 3$ matrices $\pmb { A }$ and $B$

Once the (unconstrained) Lagrangian (8.4) has been found, we may introduce the canonical momentum in the usual way by a matrix

$$
P = \nabla _ { \dot { Q } } L ( Q , \dot { Q } ) .
$$

One finds that this matrix can be expressed compactly as $P = { \dot { Q } } R$ . It is important to keep in mind that the two matrices $Q$ and $R$ do not commute. Hence the ordering of the two variables in the definition of $P$ is crucial.

It must be pointed out that there are certain rigid bodies for which the matrix $R$ is singular; specifically linear and planar bodies have this feature. For the moment we will simply assume that $R$ is nonsingular; we will correct the equations for the case of planar bodies in Section 8.1.2.

The momentum corresponding to the center of mass has the expression

$$
\begin{array} { r } { \pmb { p } _ { \mathtt { c m } } = M \dot { \pmb q } _ { \mathtt { c m } } , } \end{array}
$$

with $\textstyle M = \sum _ { i = 1 } ^ { k } m _ { i }$ the total mass of the rigid body.

The constrained Hamiltonian formulation is now found exactly in the same manner as outlined in the previous chapter and we obtain:

$$
\tilde { H } = \frac { 1 } { 2 } \mathrm { t r } ( P R ^ { - 1 } P ^ { T } ) + \frac { 1 } { 2 M } \| p _ { \mathrm { c m } } \| ^ { 2 } + V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) + \mathrm { t r } ( ( Q ^ { T } Q - I _ { 3 } ) \varLambda ) ,
$$

$$
\begin{array} { r l } & { \frac { d } { d t } q _ { \mathrm { c m } } = M ^ { - 1 } p _ { \mathrm { c m } } , } \\ & { \frac { d } { d t } p _ { \mathrm { c m } } = - \nabla q _ { \mathrm { c m } } V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) , } \\ & { \phantom { \frac { d } { d t } } \frac { d } { d t } Q = P R ^ { - 1 } , } \\ & { \frac { d } { d t } P = - \nabla _ { Q } V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) - 2 Q \Lambda , } \\ & { \phantom { \frac { d } { d t } } I _ { 3 } = Q ^ { T } Q . } \end{array}
$$

The holonomic constraint (8.12) implies that $Q$ is a rotation matrix provided the initial $Q ( 0 ) = Q _ { 0 }$ is a rotation matrix; i.e. $Q _ { 0 } ^ { T } Q _ { 0 } = I _ { 3 }$ and det $Q _ { 0 } = 1$ . The set of all rotation matrices $Q \in \mathbb { R } ^ { 3 }$ forms the group $S O ( 3 )$ .

Differentiate the constraint $Q ^ { T } Q = I _ { 3 }$

$$
Q ^ { T } \dot { \pmb { Q } } + \dot { \pmb { Q } } ^ { T } \pmb { Q } = { \pmb { 0 } } ,
$$

hence, from (8.10) and using the symmetry of $R$

$$
\begin{array} { r } { Q ^ { T } P R ^ { - 1 } + R ^ { - 1 } P ^ { T } Q = \mathbf { 0 } . } \end{array}
$$

Thus, when viewed as a constrained system, the equations (8.10)–(8.12) constitute a Hamiltonian system on the manifold

$$
{ \mathcal { P } } = \{ ( Q , P ) \in \mathbb { R } ^ { 3 \times 3 } \times \mathbb { R } ^ { 3 \times 3 } : Q ^ { T } Q = I _ { 3 } , Q ^ { T } P R ^ { - 1 } + R ^ { - 1 } P ^ { T } Q = \bf { 0 } \} .
$$

The symplectic structure on $\mathcal { P }$ is given by the restriction of the canonical symplectic structure on $\mathbb { R } ^ { 3 \times 3 } \times \mathbb { R } ^ { 3 \times 3 }$ to $\mathcal { P }$ . The canonical structure on $\mathbb { R } ^ { 3 \times 3 } \times \mathbb { R } ^ { 3 \times 3 }$ , in turn is obtained by viewing $3 \times 3$ matrices as vectors in $\mathbb { R } ^ { 9 }$ .

Note that the manifold $\mathcal { P }$ is not the cotangent bundle $T ^ { * } S O ( 3 )$ , which can be identified with the manifold

$$
T ^ { \ast } S O ( 3 ) = \{ ( Q , \bar { P } ) \in \mathbb { R } ^ { 3 \times 3 } \times \mathbb { R } ^ { 3 \times 3 } : Q ^ { T } Q = I _ { 3 } , Q ^ { T } \bar { P } + \bar { P } ^ { T } Q = \bf { 0 } \} .
$$

However, we can relate any element $( Q , P ) \in { \mathcal { P } }$ to an element $( Q , \bar { P } ) \in T ^ { * } S O ( 3 )$ via the transformation

$$
\bar { \pmb { P } } = \pmb { P } - \pmb { Q } \pmb { \Gamma } ,
$$

where the symmetric matrix $\boldsymbol { \mathsf { \Pi } } ^ { r } \in \mathbb { R } ^ { 3 \times 3 }$ is defined by

$$
\pmb { \cal { r } } = \frac { 1 } { 2 } \left( \pmb { Q } ^ { T } \pmb { P } + \pmb { P } ^ { T } \pmb { Q } \right) .
$$

This is equivalent to

$$
\bar { P } = \frac 1 2 \left( P - Q P ^ { T } Q \right) .
$$

It can be shown that this map is symplectic (this is equivalent to showing that a map from $( \pmb q , \pmb p )$ to $( q , \bar { p } )$ defined by

$$
\bar { \pmb { p } } = \pmb { p } - \pmb { G } ( \pmb { q } ) ^ { T } \pmb { \lambda }
$$

is symplectic provided $g ( \pmb q ) = \pmb 0$ , as pointed out in Lemma 1 of Chapter 7). We conclude that the equations (8.10)–(8.12) combined with (8.14) define a Hamiltonian system on $T ^ { * } S O ( 3 )$ .

Let us also briefly discuss the evaluation of $\nabla _ { Q } V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } )$ . In many applications, for example a force action on a fixed reference location $r ^ { 0 }$ on the rigid body, we are led to a potential energy term of the form

$$
V ( \pmb q ) = V ( \pmb q _ { \mathrm { c m } } + \pmb Q r ^ { 0 } ) = V _ { \mathrm { e x t } } ( \pmb Q , \pmb q _ { \mathrm { c m } } ) .
$$

Then the definition

$$
\mathrm { t r } ( \nabla _ { Q } V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) \delta Q ^ { T } ) = \operatorname* { l i m } _ { \varepsilon \to 0 } \frac { V _ { \mathrm { e x t } } ( Q + \varepsilon \delta Q , q _ { \mathrm { c m } } ) - V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) } { \varepsilon }
$$

leads to the expression

$$
\nabla _ { Q } V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) = \nabla _ { q } V ( q ) [ r ^ { 0 } ] ^ { T } .
$$

See the Exercises.

# 8.1.2 Linear and planar bodies

In the case of linear and planar bodies, the above discussion must be amended. For a linear body (a pendulum), in which all the points of the body lie along a straight line, the orientation in space is defined by a single unit vector $\pmb { u }$ , so there is just one multiplier. The mass tensor $R$ will have only its (1, 1) element nonzero.

For a planar body, the orientation is defined by two vectors, say $\pmb { u } _ { 1 }$ and $\pmb { u } _ { 2 }$ . There are three constraints (unit length for each of the two vectors and orthogonality of $\pmb { u } _ { 1 }$ and $\pmb { u } _ { 2 }$ ) and therefore three multipliers which can be cast in the form of a $2 \times 2$ symmetric matrix.

A unified treatment of the equations for linear, planar, and three-dimensional bodies is possible in the formulation (8.7) and (8.8)–(8.12) if we view $Q$ and $P$ as lying in $\mathbb { R } ^ { 3 \times k }$ , with $k$ the dimension of the body, and suppose $R$ and $\pmb { \Lambda }$ to be $k \times k$ (rather than $3 \times 3$ ) symmetric matrices. (See the Exercises.)

# 8.1.3 Symplectic discretization using SHAKE

Let us now consider the symplectic integration of the rigid body. For simplicity, we will initially restrict our treatment to the case where the center of mass of the body is fixed in space, so that only rotational motions, governed by equations (8.10)–(8.12), need be considered.

As first pointed out by MCLACHLAN AND SCOVEL [133] and REICH [154, 156], the obvious approach is to apply the SHAKE/RATTLE method to the constrained equations. This yields a symplectic method that propagates the variable $( Q , P )$ on $\mathcal { P }$ . The discrete equations for the RATTLE discretization can be written as follows:

$$
\begin{array} { c } { { \displaystyle Q ^ { n + 1 } = Q ^ { n } + \Delta t P ^ { n + 1 / 2 } R ^ { - 1 } , } } \\ { { { \cal P } ^ { n + 1 / 2 } = P ^ { n } - \displaystyle \frac { \Delta t } { 2 } \nabla _ { Q } V _ { \mathrm { e x t } } ( Q ^ { n } ) - \Delta t Q ^ { n } \Lambda _ { ( r ) } ^ { n } , } } \\ { { { \cal I } _ { 3 } = [ Q ^ { n + 1 } ] ^ { T } Q ^ { n + 1 } , } } \\ { { { \cal P } ^ { n + 1 } = P ^ { n + 1 / 2 } - \displaystyle \frac { \Delta t } { 2 } \nabla _ { Q } V _ { \mathrm { e x t } } ( Q ^ { n + 1 } ) - \Delta t Q ^ { n + 1 } \Lambda _ { ( v ) } ^ { n + 1 } , } } \\ { { 0 = [ Q ^ { n + 1 } ] ^ { T } P ^ { n + 1 } R ^ { - 1 } + R ^ { - 1 } [ P ^ { n + 1 } ] ^ { T } Q ^ { n + 1 } . } } \end{array}
$$

The implementation of the RATTLE method requires that we solve a nonlinear system at each timestep. Setting

$$
\bar { Q } ^ { n + 1 } : = Q ^ { n } + \Delta t P ^ { n } R ^ { - 1 } - \frac { \Delta t ^ { 2 } } { 2 } \nabla _ { Q } V _ { \mathrm { e x t } } ( Q ^ { n } ) R ^ { - 1 } ,
$$

and writing $Q$ for $Q ^ { n + 1 }$ as well as $\wedge$ for $\pmb { \Lambda } _ { ( r ) } ^ { n }$ , the equations become

$$
\begin{array} { l } { Q = \bar { Q } ^ { n + 1 } - \Delta t ^ { 2 } Q ^ { n } \Lambda R ^ { - 1 } , } \\ { I _ { 3 } = Q ^ { T } Q . } \end{array}
$$

Substituting the first equation into the second, we obtain

$$
\begin{array} { r l } & { I _ { 3 } = [ \bar { Q } ^ { n + 1 } ] ^ { T } \bar { Q } ^ { n + 1 } - \Delta t ^ { 2 } \left\{ R ^ { - 1 } \Lambda [ Q ^ { n } ] ^ { T } \bar { Q } ^ { n + 1 } + [ \bar { Q } ^ { n + 1 } ] ^ { T } Q ^ { n } \Lambda R ^ { - 1 } \right\} + } \\ & { \qquad + \Delta t ^ { 4 } R ^ { - 1 } \Lambda \Lambda R ^ { - 1 } , } \end{array}
$$

where we have made use of the symmetry of $R$ and $\wedge$ . To work out a simple iterative solution scheme, we first neglect terms of order $\Delta t ^ { 3 }$ and higher. Taking note of $[ \bar { Q } ^ { n + 1 } ] ^ { T } Q ^ { n } = I _ { 3 } + { \mathcal { O } } ( \Delta t )$ , we obtain the linear relation

$$
{ \bf 0 } \approx ( [ \bar { Q } ^ { n + 1 } ] ^ { T } \bar { Q } ^ { n + 1 } - I _ { 3 } ) - \Delta t ^ { 2 } ( \Lambda R ^ { - 1 } + R ^ { - 1 } \Lambda ) ,
$$

which we have to solve for $\bar { \Lambda } = \Delta t ^ { 2 } \Lambda$ .

We now recall the special form (8.3) of the mass tensor $R$ which allows us to easily solve any system of type

$$
{ \bf 0 } = { \cal M } - ( \bar { \Lambda } R ^ { - 1 } + R ^ { - 1 } \bar { \Lambda } )
$$

for $\bar { \Lambda }$ . Specifically, multiplication of (8.22) by $\bar { e } _ { i } ^ { T }$ from the right and by $\bar { e } _ { j }$ from the left yields $0 = m _ { i j } - \bar { \lambda } _ { i j } / r _ { j j } - \bar { \lambda } _ { i j } / r _ { i i }$ . This relation is easily inverted to express the solution $\bar { \pmb { \Lambda } } = \{ \bar { \lambda } _ { i j } \}$ explicitly as

$$
\bar { \lambda } _ { i j } = { \frac { r _ { i i } r _ { j j } } { r _ { i i } + r _ { j j } } } m _ { i j } \qquad ( i , j = 1 , 2 , 3 ) .
$$

In our case, we set

$$
\pmb { M } = [ \bar { \pmb { Q } } ^ { n + 1 } ] ^ { T } \bar { \pmb { Q } } ^ { n + 1 } - \pmb { I } _ { 3 }
$$

and obtain, in first approximation

$$
Q _ { ( 1 ) } = \bar { Q } ^ { n + 1 } - Q ^ { n } \bar { \Lambda } _ { ( 1 ) } R ^ { - 1 } ,
$$

with $\bar { \cal A } _ { ( 1 ) } = \{ \bar { \lambda } _ { i j } \}$ determined by (8.23). This guides us to the simple quasi-Newton iteration

$$
\begin{array} { r l r } {  { \pmb { Q } _ { ( k ) } = \pmb { Q } _ { ( k - 1 ) } - \pmb { Q } ^ { n } \bar { \pmb { \Lambda } } _ { ( k ) } \pmb { R } ^ { - 1 } , } } \\ & { } & { \pmb { 0 } = ( \pmb { Q } _ { ( k - 1 ) } ^ { T } \pmb { Q } _ { ( k - 1 ) } - \pmb { I } _ { 3 } ) - ( \bar { \pmb { \Lambda } } _ { ( k ) } \pmb { R } ^ { - 1 } + \pmb { R } ^ { - 1 } \bar { \pmb { \Lambda } } _ { ( k ) } ) , } \end{array}
$$

for $k > 1$ till convergence at which point we set $Q ^ { n + 1 } = Q _ { ( k + 1 ) }$ . During the iteration we also use the computed $\bar { \Lambda } _ { ( k ) }$ to update the momentum matrix $P ^ { n + 1 / 2 }$ . Compare the discussion in Section 7.2.2. A description of other Newton-type iteration schemes can be found in [98].

The momentum constraint (8.21) leads to a linear equation in $\pmb { \Lambda } _ { ( v ) } ^ { n + 1 }$ of type (8.22) and, hence, is easy to enforce.

# 8.1.4 Numerical experiment: a symmetric top

We perform a numerical experiment involving an axially symmetric rigid body with its center of mass held fixed ( $\begin{array} { r } { \pmb { q } _ { \mathtt { C m } } = \mathbf { 0 } , } \end{array}$ ). We further suppose that a conservative force is applied to a fixed reference point $r ^ { 0 }$ on the axis of symmetry.

The rigid body is given moments of inertia $I _ { 1 } = 4$ , $I _ { 2 } = 4$ and $I _ { 3 } = 1$ , making it a long, thin object, symmetric around the third axis of inertia with mass tensor

$$
\begin{array} { r } { R = \left[ \begin{array} { c c c } { 0 . 5 } & { 0 } & { 0 } \\ { 0 } & { 0 . 5 } & { 0 } \\ { 0 } & { 0 } & { 3 . 5 } \end{array} \right] . } \end{array}
$$

The body is attached by a spring (coefficient $K = 5$ ) from the fixed reference point $\boldsymbol { r } ^ { 0 } = ( 0 , 0 , 1 ) ^ { T }$ on the rigid body to a point $\pmb q ^ { 0 } = ( 0 , 0 , - 1 ) ^ { T }$ fixed in the laboratory frame. The associated potential energy expression is given by

$$
V _ { \mathrm { e x t } } ( Q ) = \frac { K } { 2 } \| Q r ^ { 0 } - \pmb { q } ^ { 0 } \| ^ { 2 } .
$$

The object is initially oriented so that the third axis of inertia coincides with the $Z \cdot$ -axis in the laboratory frame implying $Q ( 0 ) = I _ { 3 }$ . 3 Initial body angular momenta applied are $\pi _ { 1 } = 0$ , $\pi _ { 2 } = 0 . 1$ and $\pi _ { 3 } = 2$ . This means that the body is initially set spinning around its axis of symmetry and is provided a small downward impetus. The associated initial momentum matrix $P$ is given as the solution of

$$
\begin{array} { r l } & { \hat { \boldsymbol { \pi } } = \left[ \begin{array} { c c c } { 0 } & { - 2 } & { 0 . 1 } \\ { 2 } & { 0 } & { 0 } \\ { - 0 . 1 } & { 0 } & { 0 } \end{array} \right] = \boldsymbol { P } - \boldsymbol { P } ^ { T } , } \\ & { \mathbf { 0 } = \boldsymbol { P } \boldsymbol { R } ^ { - 1 } + \boldsymbol { R } ^ { - 1 } \boldsymbol { P } ^ { T } , } \end{array}
$$

which is equivalent to

$$
\begin{array} { r } { P R ^ { - 1 } + R ^ { - 1 } P = R ^ { - 1 } \widehat { \pmb { \pi } } . } \end{array}
$$

The origin of these equations is explained in the following section. The explicit solution is

$$
\begin{array} { r } { \pmb { P } ( 0 ) = \left[ \begin{array} { c c c } { 0 } & { - 1 } & { 0 . 0 8 7 5 } \\ { 1 } & { 0 } & { 0 } \\ { - 0 . 0 1 2 5 } & { 0 } & { 0 } \end{array} \right] . } \end{array}
$$

Under these circumstances, the body spirals gradually away from the upright position, eventually swinging down (this phase is quite rapid) before returning again to the upright position. Although it is a slight misuse of terminology, let us refer to such a motion as a “quasi-period.”

The variation in speed of oscillation over one quasi-period makes this a somewhat challenging integration problem. The results of a numerical experiment using a RATTLE integrator and $\Delta t = 0 . 1$ are shown in Fig. 8.2. The motion $\pmb { q } ( t ) = \pmb { Q } ( t ) r ^ { 0 }$ of the symmetry axis of the body, as seen in the laboratory frame, is plotted on the left. On the right are shown the fluctuations in the $Z \cdot$ -component of $\pmb q ( t )$ v. time, above the plot of energy error v. time. The rapid changes in the energy error are associated with the times of rapid motion as the top briefly swings down.

![](images/6de97e63e213751e1bce7f6243136eb2c0d94946f6c6d9316af8cfd135516df6.jpg)  
Figure 8.2 Motion of the symmetric top, as computed using RATTLE.

# 8.2 Angular momentum and the inertia tensor

A common alternative description for the rotational kinetic energy is based on the body angular momentum vector $\pmb { \pi } \in \mathbb { R } ^ { 3 }$ . Introduction of this concept will pave the way for another very useful approach to symplectic integration based on the rigid body Euler equations. We start the derivation by introducing the spatial angular velocity vector $\pmb { \omega }$ via the classical definition

$$
\dot { \pmb { r } } _ { i } = \pmb { \omega } \times \pmb { r } _ { i } ,
$$

where $r _ { i } = q _ { i } - q _ { \mathrm { c m } }$ is a displacement vector. Using the setting from Section 8.1, the standard (spatial) angular momentum vector $\pmb { m }$ can then be expressed as

$$
\begin{array} { l } { \displaystyle { m = \sum _ { i = 1 } ^ { k } m _ { i } \boldsymbol { r } _ { i } \times \dot { \boldsymbol { r } } _ { i } } } \\ { \displaystyle { \quad = \sum _ { i = 1 } ^ { k } m _ { i } \boldsymbol { r } _ { i } \times ( \boldsymbol { \omega } \times \boldsymbol { r } _ { i } ) } } \\ { \displaystyle { \quad = \sum _ { i = 1 } ^ { k } m _ { i } \left[ \lVert \boldsymbol { r } _ { i } \rVert ^ { 2 } - { r } _ { i } { r } _ { i } ^ { T } \right] \boldsymbol { \omega } } . } \end{array}
$$

Since

$$
r _ { i } = Q r _ { i } ^ { 0 } ,
$$

we obtain

$$
{ \pmb m } = { \pmb Q } \left( \sum _ { i = 1 } ^ { k } m _ { i } \left[ \| r _ { i } ^ { 0 } \| ^ { 2 } - r _ { i } ^ { 0 } \left[ r _ { i } ^ { 0 } \right] ^ { T } \right] \right) { \pmb Q } ^ { T } { \pmb \omega } ,
$$

in terms of a fixed reference configuration. The body angular momentum vector $\pmb { \pi }$ is now defined by ${ \pmb { \pi } } = { \pmb Q } ^ { T } { \pmb m }$ . Similarly the body angular velocity vector is $\pmb { \omega } ^ { \mathrm { b o d y } } = \pmb { Q } ^ { T } \pmb { \omega }$ and we obtain the relation

with the inertial tensor given by

$$
{ \pmb T } = \sum _ { i = 1 } ^ { k } m _ { i } \left[ \| r _ { i } ^ { 0 } \| ^ { 2 } - r _ { i } ^ { 0 } \left[ r _ { i } ^ { 0 } \right] ^ { T } \right] = \sum _ { i = 1 } ^ { k } m _ { i } \| r _ { i } ^ { 0 } \| ^ { 2 } { \pmb I } _ { 3 } - R .
$$

If the mass tensor $R$ is diagonalized and represented in the form (8.3), then

$$
\sum _ { i = 1 } ^ { k } m _ { i } \| r _ { i } ^ { 0 } \| ^ { 2 } = \sum _ { i = 1 } ^ { 3 } r _ { i i } \| \bar { \pmb { e } } _ { i } \| ^ { 2 } = r _ { 1 1 } + r _ { 2 2 } + r _ { 3 3 } ,
$$

and

$$
{ \pmb T } = \left[ \begin{array} { c c c } { r _ { 2 2 } + r _ { 3 3 } } & { 0 } & { 0 } \\ { 0 } & { r _ { 1 1 } + r _ { 3 3 } } & { 0 } \\ { 0 } & { 0 } & { r _ { 1 1 } + r _ { 2 2 } } \end{array} \right] ,
$$

with the principal moments of inertia $\begin{array} { r } { I _ { i } = \sum _ { j \neq i } r _ { j j } } \end{array}$

Let us link the angular momentum and angular velocity vectors to the canonical variables in the constrained formulation (8.8)–(8.12). Since $r _ { i } = Q r _ { i } ^ { 0 }$ , we obtain

$$
\dot { \bf Q } r _ { i } ^ { 0 } = { \bf \nabla } \omega \times { \bf Q } r _ { i } ^ { 0 } .
$$

Next we make use of the fact that for any vector $\pmb { u } \in \mathbb { R } ^ { 3 }$ , we can write

$$
{ \widehat { \pmb { \omega } } } { \pmb { u } } = { \pmb { \omega } } \times { \pmb { u } } ,
$$

where $\widehat { \pmb { \omega } }$ is the $3 \times 3$ skew-symmetric matrix

$$
\pmb { \hat { \omega } } = \left[ \begin{array} { c c c } { 0 } & { - \omega _ { 3 } } & { \omega _ { 2 } } \\ { \omega _ { 3 } } & { 0 } & { - \omega _ { 1 } } \\ { - \omega _ { 2 } } & { \omega _ { 1 } } & { 0 } \end{array} \right] ,
$$

${ \pmb { \omega } } = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) ^ { T }$ . 4 Hence (8.24) implies the relation

$$
\begin{array} { r } { \pmb { \hat { \omega } } = \pmb { \dot { Q } } \pmb { Q } ^ { T } = \pmb { P } \pmb { R } ^ { - 1 } \pmb { Q } ^ { T } . } \end{array}
$$

4Similar expression will be frequently used in the rest of this chapter. We remind the reader of the following convention. If $^ { b }$ is a 3-vector, then the associated skew-symmetric $3 \times 3$ matrix is denoted by $\widehat { b }$ . We use capital letters for the skew matrix forms of body angular momentum and angular velocity since these are standard notation often found in the literature.

It is also easy to verify from (8.24) and

$$
Q ^ { T } \dot { Q } r _ { i } ^ { 0 } = Q ^ { T } \left[ \pmb { \omega } \times \pmb { Q } r _ { i } ^ { 0 } \right] = ( Q ^ { T } \pmb { \omega } ) \times r _ { i } ^ { 0 }
$$

that

$$
\begin{array} { r } { \widehat { \pmb { \omega } } ^ { \mathrm { b o d y } } = \pmb { Q } ^ { T } \dot { \pmb { Q } } = \pmb { Q } ^ { T } \pmb { P } \pmb { R } ^ { - 1 } . } \end{array}
$$

Furthermore, we have the important identity:

$$
\widehat { \pmb { \pi } } = \widehat { \pmb { \omega } } ^ { \mathrm { b o d y } } \pmb { R } - \pmb { R } \left[ \widehat { \pmb { \omega } } ^ { \mathrm { b o d y } } \right] ^ { T } = \pmb { Q } ^ { T } \pmb { P } - \pmb { P } ^ { T } \pmb { Q } ,
$$

for the skew matrix form of the body angular momentum vector $\pmb { \pi }$ , which can be verified by explicit computation using (8.3). Specifically, multiplication from the left by $\bar { \pmb { e } } _ { i } ^ { T }$ and by $\bar { e } _ { j }$ from the right yields

$$
\widehat { \pi } _ { i j } = ( r _ { i i } + r _ { j j } ) \widehat { \omega } _ { i j } ^ { \mathrm { b o d y } } ,
$$

which is equivalent to $\pi _ { k } = I _ { k } \omega _ { k } ^ { \mathsf { b o d y } }$ , $k = 1 , 2 , 3$ . (See also the exercises.)

From $\widehat { \pmb { \omega } } = \dot { Q } Q ^ { T }$ and $\widehat { \pmb { \omega } } ^ { \mathrm { b o d } \ddot { \bf y } } = Q ^ { T } \dot { \pmb { Q } }$ , we see that $\widehat { \pmb { \omega } } = Q \widehat { \pmb { \omega } } ^ { \mathrm { b o d y } } Q ^ { T }$ . The same transformation applies to the angular momentum vectors and we obtain the expression

$$
\begin{array} { r } { \widehat { \pmb { m } } = \pmb { Q } \widehat { \pmb { \pi } } \pmb { Q } ^ { T } = { \pmb { P } } \pmb { Q } ^ { T } - \pmb { Q } { \pmb { P } } ^ { T } . } \end{array}
$$

This expression is useful when setting up the initial conditions for a constrained rigid body formulation. In particular, given an initial angular momentum vector $\pmb { m }$ (or an initial $\pmb { \pi }$ ) and an initial orientation matrix $Q$ the unique initial momentum matrix $P$ is determined by (8.25) subject to $( Q , P ) \in { \mathcal { P } }$ .

With this we have completed our brief discussion on how the classical definitions of angular velocity and angular momentum relate to the canonical variables used in the constrained rigid body formulation (8.8)–(8.12).

# 8.3 The Euler equations of rigid body motion

We next show that the equations of a rigid body with its center of mass held fixed at $\pmb q _ { \mathrm { c m } } = { \bf 0 }$ can be reduced to a system of three differential equations for the angular momenta and associated equations for the orientation of the rigid body. These differential equations have a special generalized (noncanonical) Hamiltonian structure which can be treated using an explicit Hamiltonian splitting method.

We start our discussion from the angular momentum identity $m = Q \pi =$ $\textstyle \sum _ { i } m _ { i } r _ { i } \times { \dot { r } } _ { i }$ . Differentiation with respect to time yields

$$
\dot { m } = \dot { Q } \pi + Q \dot { \pi } = \sum _ { i } m _ { i } r _ { i } \times \ddot { r } _ { i } ,
$$

which, multiplied by $Q ^ { T }$ , is equivalent to

$$
\dot { \pmb { \pi } } = - \pmb { Q } ^ { T } \dot { \pmb { Q } } \pmb { \pi } + \sum _ { i } m _ { i } \pmb { q } _ { i } ^ { 0 } \times \pmb { Q } ^ { T } \ddot { \pmb { r } } _ { i } .
$$

We now take note of

$$
Q ^ { T } { \dot { Q } } \pi = { \widehat { \omega } } ^ { \mathrm { b o d y } } \pi = \left( { \widehat { T ^ { - 1 } } } \pi \right) \pi = T ^ { - 1 } \pi \times \pi = - \pi \times T ^ { - 1 } \pi = - { \widehat { \pi } } T ^ { - 1 } \pi ,
$$

and assume an external force $m _ { i } { \ddot { r } } _ { i } = F _ { i }$ acting on the rigid body at a point $r _ { i } = Q r _ { i } ^ { 0 }$ , then we obtain the Euler equation

$$
\pmb { \dot { \pi } } = \widehat { \pmb { \pi } } \pmb { T } ^ { - 1 } \pmb { \pi } + \sum _ { i } \pmb { r } _ { i } ^ { 0 } \times \pmb { Q } ^ { T } \pmb { F } _ { i }
$$

for forced rigid body motion. We call

$$
{ \pmb { N } } = \sum _ { i } r _ { i } ^ { 0 } \times { \pmb { Q } } ^ { T } { \pmb { F } } _ { i } = { \pmb { Q } } ^ { T } \left( \sum _ { i } r _ { i } \times { \pmb { F } } _ { i } \right)
$$

the applied torque in body coordinates.

The differential equation for the rotation matrix $Q$ had already been derived previously as

$$
\dot { \pmb { Q } } = \pmb { Q } \widehat { \pmb { \omega } } ^ { \mathrm { b o d y } } = \pmb { Q } ( \widehat { \pmb { T } ^ { - 1 } \pmb { \pi } } ) .
$$

Let us concentrate for a moment on the free rigid body, i.e. $\pmb { F } _ { j } = \pmb { 0 }$ . Then the equation (8.26) can be solved independently of (8.27). The free rigid body Euler equation

$$
\dot { \pmb { \pi } } = \widehat { \pmb { \pi } } \pmb { T } ^ { - 1 } \pmb { \pi }
$$

is an example of a noncanonical Hamiltonian system (actually a Lie–Poisson system) with Hamiltonian function (kinetic energy)

$$
\mathcal { T } ( \pmb { \pi } ) = \frac { 1 } { 2 } \pmb { \pi } ^ { T } T ^ { - 1 } \pmb { \pi } = \frac { 1 } { 2 } \left( \frac { \pi _ { 1 } ^ { 2 } } { I _ { 1 } } + \frac { \pi _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { \pi _ { 3 } ^ { 2 } } { I _ { 3 } } \right)
$$

and Lie–Poisson structure matrix

$$
\begin{array} { r } { J ( { \pmb \pi } ) = \widehat { \pmb \pi } = \left( \begin{array} { c c c } { 0 } & { - \pi _ { 3 } } & { \pi _ { 2 } } \\ { \pi _ { 3 } } & { 0 } & { - \pi _ { 1 } } \\ { - \pi _ { 2 } } & { \pi _ { 1 } } & { 0 } \end{array} \right) . } \end{array}
$$

In other words, the Euler equation (8.26) is equivalent to the more abstract formulation

$$
\frac { d } { d t } \pmb { \pi } = \pmb { J } ( \pmb { \pi } ) \nabla _ { \pmb { \pi } } \mathcal { T } ( \pmb { \pi } ) .
$$

The Lie–Poisson bracket $\{ F , G \}$ of two functions $F ( \pmb { \pi } )$ and $G ( { \pmb \pi } )$ is defined by

$$
\left\{ F , G \right\} ( \pmb { \pi } ) = \left[ \nabla _ { \pmb { \pi } } F ( \pmb { \pi } ) \right] ^ { T } J ( \pmb { \pi } ) \nabla _ { \pmb { \pi } } G ( \pmb { \pi } ) .
$$

The Lie–Poisson bracket is anti-symmetric and satisfies the Jacobi identity [149, 124, 7]. In this sense the Euler equation (8.29) is a generalization of the Hamiltonian formulations we have encountered so far. Note, however, that the matrix $J$ is not invertible hence we cannot define a symplectic form $J ^ { - 1 } d { \pmb { \pi } } \wedge d { \pmb { \pi } }$ . On the other hand, it is easily verified that the Euclidean norm of the momentum vector $\pmb { \pi }$ is a first integral of (8.29) for any choice of the Hamiltonian $\tau$ . This is due to the fact that the structure matrix $\jmath$ is singular and of rank two. Functions that are first integrals of a system for any choice of the Hamiltonian are also called Casimir functions. They are always linked to the fact that the structure matrix $J$ is singular. We also point out that the rigid body structure matrix $J = \widehat { \pmb { \pi } }$ is invertible on the level sets of $| | { \pmb { \pi } } | | =$ constant. This allows us to define a (canonical) symplectic structure on each of these two-dimensional level sets. See OLVER [149], MARSDEN AND RATIU [124], or ARNOLD [7] for more details.

Let us next have a closer look at the equation (8.27). We can view the rotation matrix $Q \in S O ( 3 )$ as the collection of three column vectors $\pmb { S } _ { j } \in \mathbb { R } ^ { 3 }$ that are orthogonal to each other and that have unit length; i.e.

$$
Q ^ { T } = \left[ s _ { 1 } , s _ { 2 } , s _ { 3 } \right] .
$$

Then equation (8.27) is rewritten as

$$
\frac { d } { d t } { \pmb Q } ^ { T } = - ( \widehat { { \pmb T } ^ { - 1 } } { \pmb \pi } ) { \pmb Q } ^ { T } ,
$$

which is equivalent to

$$
\frac { d } { d t } s _ { j } = - ( \pmb { T } ^ { - 1 } \pmb { \pi } ) \times \pmb { s } _ { j } = s _ { j } \times ( \pmb { T } ^ { - 1 } \pmb { \pi } ) = \widehat { s } _ { j } \nabla _ { \pmb { \pi } } \mathcal { T } ( \pmb { \pi } ) , \qquad ( j = 1 , 2 , 3 ) .
$$

The system (8.29)–(8.30) constitutes a Hamiltonian system in the variable

$$
z = ( s _ { 1 } , s _ { 2 } , s _ { 3 } , \pmb { \pi } ) ^ { T } \in \mathbb { R } ^ { 1 2 }
$$

and with the skew-symmetric Lie–Poisson structure matrix5

$$
J ( z ) = \left( \begin{array} { c c c c } { 0 } & { 0 } & { 0 } & { \widehat { s } _ { 1 } } \\ { 0 } & { 0 } & { 0 } & { \widehat { s } _ { 2 } } \\ { 0 } & { 0 } & { 0 } & { \widehat { s } _ { 3 } } \\ { \widehat { s } _ { 1 } } & { \widehat { s } _ { 2 } } & { \widehat { s } _ { 3 } } & { \widehat { \pi } } \end{array} \right) \in \mathbb { R } ^ { 1 2 \times 1 2 } .
$$

The equations of motion of a free rigid body take now the abstract form

$$
\frac { d } { d t } z = J ( z ) \nabla _ { z } \mathcal { H } ( z ) ,
$$

where

$$
\mathcal { H } = \mathcal { T } = \frac { 1 } { 2 } \pmb { \pi } ^ { T } \pmb { T } ^ { - 1 } \pmb { \pi } .
$$

Using this general Hamiltonian framework, one can consider systems where the Hamiltonian $\mathcal { H }$ depends on the state variable $z$ in an arbitrary way. Typically, the Hamiltonian $\mathcal { H }$ is however of the form

$$
\mathscr { H } = \frac { 1 } { 2 } \pmb { \pi } ^ { T } T ^ { - 1 } \pmb { \pi } + \mathscr { V } ( s _ { 1 } , s _ { 2 } , s _ { 3 } ) .
$$

Example 1 Consider a rigid body with fixed center of mass $\pmb { q } _ { \mathrm { c m } } = \mathbf { 0 }$ andan external force $F$ acting on a (fixed) point $r ^ { 0 }$ in the body reference configuration. In other words, the force is assumed to be given by

$$
\boldsymbol { F } ( \boldsymbol { r } ) = - \boldsymbol { \nabla } _ { \boldsymbol { r } } \boldsymbol { V } ( \boldsymbol { r } ) , \quad \boldsymbol { r } = \boldsymbol { Q } \boldsymbol { r } ^ { 0 } .
$$

We call this force the spatial force. The rigid body potential energy is

$$
\mathcal { V } ( s _ { 1 } , s _ { 2 } , s _ { 3 } ) = V ( Q r ^ { 0 } ) ,
$$

and the corresponding equations of motion are given by

$$
\frac { d } { d t } \pi = \pmb { \pi } \times ( \pmb { T } ^ { - 1 } \pmb { \pi } ) + \sum _ { j = 1 } ^ { 3 } \pmb { s } _ { j } \times \nabla _ { s _ { j } } \mathcal { V } ( \pmb { s } _ { 1 } , \pmb { s } _ { 2 } , \pmb { s } _ { 3 } )
$$

and

$$
\frac { d } { d t } \pmb { s } _ { j } = \pmb { s } _ { j } \times ( \pmb { T } ^ { - 1 } \pmb { \pi } ) ,
$$

$j = 1 , 2 , 3$ . Let us write $r$ in terms of the unit coordinate vectors $e _ { j }$ (fixed laboratory frame with $e _ { j } ^ { T } Q = s _ { j } ^ { T }$ ), i.e.

$$
r = \sum _ { j = 1 } ^ { 3 } ( s _ { j } ^ { T } r ^ { 0 } ) \pmb { e } _ { j } ,
$$

since $\pmb { e } _ { j } ^ { T } \pmb { r } = \pmb { e } _ { j } ^ { T } \pmb { Q } \pmb { r } ^ { 0 } = \pmb { s } _ { j } ^ { T } \pmb { r } ^ { 0 }$ . Then

$$
\begin{array} { r l } & { \displaystyle \sum _ { j = 1 } ^ { 3 } s _ { j } \times \nabla _ { s _ { j } } \mathcal { V } ( s _ { 1 } , s _ { 2 } , s _ { 3 } ) = - \sum _ { j = 1 } ^ { 3 } s _ { j } \times \big ( ( \boldsymbol { F } ( \boldsymbol { r } ) ^ { T } \boldsymbol { e } _ { j } ) \boldsymbol { r } ^ { 0 } \big ) } \\ & { \quad \quad \quad \quad = - \sum _ { j = 1 } ^ { 3 } \big ( ( \boldsymbol { F } ( \boldsymbol { r } ) ^ { T } \boldsymbol { e } _ { j } ) s _ { j } \big ) \times \boldsymbol { r } ^ { 0 } } \\ & { \quad \quad \quad = \boldsymbol { r } ^ { 0 } \times ( \boldsymbol { Q } ^ { T } \boldsymbol { F } ( \boldsymbol { r } ) ) } \end{array}
$$

is the standard formula for the applied torque in body coordinates (compare (8.26)). This procedure generalizes to any number of particle locations

$$
r _ { i } = \sum _ { j = 1 } ^ { 3 } ( s _ { j } ^ { T } r _ { i } ^ { 0 } ) \pmb { e } _ { j } , \qquad i = 1 , \dots , k ,
$$

and potential energies $V = V ( \boldsymbol { r } _ { 1 } , \dots , \boldsymbol { r } _ { k } )$

# 8.3.1 Symplectic discretization of the Euler equations

We have already seen that SHAKE/RATTLE discretization can be used to treat the constrained formulation (8.17)–(8.21). This leads to a system of nonlinear equations that needs to be solved at each timestep.

An attractive alternative for simulating free rigid body motion is based on Euler equations (8.29)–(8.30) and the idea of splitting the Hamiltonian into explicitly solvable components. This was proposed by MCLACHLAN [128], REICH [153, 154], and TOUMA AND WISDOM [193]. The Hamiltonian of a free rigid body is given by (8.28), which we write as

$$
T ( \pmb { \pi } ) = T _ { 1 } ( \pi _ { 1 } ) + T _ { 2 } ( \pi _ { 2 } ) + T _ { 3 } ( \pi _ { 3 } ) ,
$$

where $\mathcal { T } _ { j } ( \pi _ { j } ) = \pi _ { j } ^ { 2 } / ( 2 I _ { j } ) , j = 1 , 2 , 3 .$ . The crucial observation is that each entry $\mathcal { T } _ { j }$ gives rise to equations of motion which can be solved exactly. Let us demonstrate this for $\mathcal { T } _ { 1 }$ . The corresponding equations of motion can be written as a system of linear differential equations

$$
\frac { d } { d t } \pi = { \cal A } _ { 1 } \pi , \qquad \frac { d } { d t } s _ { j } = { \cal A } _ { 1 } s _ { j } , \quad ( j = 1 , 2 , 3 ) ,
$$

where

$$
A _ { 1 } = \frac { 1 } { { \cal I } _ { 1 } } \left( \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \pi _ { 1 } } } \\ { { 0 } } & { { - \pi _ { 1 } } } & { { 0 } } \end{array} \right) .
$$

Note that

$$
\frac { d } { d t } \pi _ { 1 } = 0 ,
$$

which implies that the solutions are simply given by

$$
{ \pmb \pi } ( t ) = e ^ { t A _ { 1 } } { \pmb \pi } ( 0 ) , \qquad { \pmb s } _ { j } ( t ) = e ^ { t A _ { 1 } } { \pmb s } _ { j } ( t ) , \quad ( j = 1 , 2 , 3 ) ,
$$

with

$$
e ^ { t A _ { 1 } } = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \omega _ { 1 } t } & { \sin \omega _ { 1 } t } \\ { 0 } & { - \sin \omega _ { 1 } t } & { \cos \omega _ { 1 } t } \end{array} \right) , \quad \omega _ { 1 } = \frac { \pi _ { 1 } } { I _ { 1 } } .
$$

The equations (8.33) provide an explicit expression for the exact flow map $\pmb { \phi } _ { t , \mathcal { T } _ { 1 } }$ corresponding to the system

$$
\frac { d } { d t } z = J ( z ) \nabla _ { z } \mathcal { T } _ { 1 } ( \pi _ { 1 } ) ,
$$

$z = ( s _ { 1 } , s _ { 2 } , s _ { 3 } , \pmb { \pi } ) ^ { T }$ . Similar expressions can be found for the flow maps corresponding to the entries $\mathcal { T } _ { 2 }$ and $\mathcal { T } _ { 3 }$ in (8.32).

A second-order symplectic method is now obtained by subsequent concatenation of the exact solutions corresponding to the five terms in

$$
\mathcal { T } = \frac { 1 } { 2 } \mathcal { T } _ { 1 } + \frac { 1 } { 2 } \mathcal { T } _ { 2 } + \mathcal { T } _ { 3 } + \frac { 1 } { 2 } \mathcal { T } _ { 2 } + \frac { 1 } { 2 } \mathcal { T } _ { 1 } ,
$$

over a time interval $t = \Delta t$ . To be more precise. We define a numerical method

$$
z ^ { n + 1 } = \pmb { \psi } _ { \Delta t , T } ( z ^ { n } )
$$

by the composition of flow maps

$$
\pmb { \psi } _ { \Delta t , \mathscr { T } } = \pmb { \phi } _ { \Delta t / 2 , \mathscr { T } _ { 1 } } \circ \pmb { \phi } _ { \Delta t / 2 , \mathscr { T } _ { 2 } } \circ \pmb { \phi } _ { \Delta t , \mathscr { T } _ { 3 } } \circ \pmb { \phi } _ { \Delta t / 2 , \mathscr { T } _ { 2 } } \circ \pmb { \phi } _ { \Delta t / 2 , \mathscr { T } _ { 1 } } .
$$

This method is obviously symplectic since each flow map preserves $\| { \pmb { \pi } } \|$ and is symplectic on the level sets of constant $\| \pmb { \pi } \|$ . The method also conserves the spatial angular momentum vector $I$ exactly. This follows again from the exact conservation under each flow map. This splitting and its implementation can be improved. For example, one could replace exact matrix exponentials by the Cayley transform, i.e., for any of three skew-symmetric matrices $\pmb { A } _ { i }$ we can use

$$
e ^ { t A _ { i } } \approx ( I - t A _ { i } ) ^ { - 1 } ( I + t A _ { i } ) \in S O ( 3 ) .
$$

There are also other splitting of $\tau$ possible. See the discussion in the following subsection and TOUMA AND WISDOM [193], DULLWEBER, LEIMKUHLER, AND MCLACHLAN. [54] as well as BUSS [38] and FASSO [56].

This method can now also be used to integrate more general rigid body systems with Hamiltonian

$$
\mathscr { H } = \frac { 1 } { 2 } \pmb { \pi } ^ { T } T ^ { - 1 } \pmb { \pi } + \mathscr { V } ( s _ { 1 } , s _ { 2 } , s _ { 3 } ) .
$$

Similar to the St¨ormer–Verlet method, we split the total Hamiltonian into the kinetic energy $\mathcal { T } = 1 / 2 \pmb { \pi } ^ { T } \pmb { T } ^ { - 1 } \pmb { \pi }$ and the potential energy $\nu$ . A second-order method can then be derived based on

$$
\mathcal { H } = \frac { 1 } { 2 } \mathcal { V } + \mathcal { T } + \frac { 1 } { 2 } \mathcal { V } ,
$$

The equations of motion corresponding to the potential energy $\nu$ are given by

$$
\frac { d } { d t } \pmb { \pi } = \sum _ { j = 1 } ^ { 3 } \pmb { s } _ { j } \times \nabla _ { \pmb { s } _ { j } } \mathcal { V } ( \pmb { s } _ { 1 } , \pmb { s } _ { 2 } , \pmb { s } _ { 3 } ) , \qquad \frac { d } { d t } \pmb { s } _ { j } = 0 , \quad ( j = 1 , 2 , 3 ) ,
$$

and can be solved exactly. In particular, since

$$
N = \sum _ { j = 1 } ^ { 3 } \pmb { s } _ { j } \times \nabla _ { \pmb { s } _ { j } } \mathcal { V } ( \pmb { s } _ { 1 } , \pmb { s } _ { 2 } , \pmb { s } _ { 3 } ) = \mathrm { c o n s t . } ,
$$

we obtain ${ \pmb \pi } ( t ^ { \prime } ) = { \pmb \pi } ( t ) + ( t ^ { \prime } - t ) { \pmb N }$ and ${ \pmb s } _ { j } ( t ^ { \prime } ) = { \pmb s } _ { j } ( t )$ . Denote the corresponding flow map by $\phi _ { t , \mathcal { V } }$ . Then, based on the splitting (8.36) and upon using (8.34) to propagate the kinetic energy part, we obtain the second-order symplectic method

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t / 2 , \mathscr { V } } \circ \pmb { \psi } _ { \Delta t , \mathscr { T } } \circ \pmb { \phi } _ { \Delta t / 2 , \mathscr { V } } ,
$$

for the generalized Euler system

$$
\frac { d } { d t } z = J ( z ) \nabla _ { z } \mathcal { H } ( z ) ,
$$

with Hamiltonian (8.35).

# 8.3.2 Numerical experiment: the Lagrangian top

Below we show that the Hamiltonian for a Lagrangian top is of the form (8.35) and conduct a numerical experiment to test the symplectic splitting method. See [7, 73] for a detailed analysis of the Lagrangian top.

The matrix $\tau$ is defined by the three principal moments of inertia of the (axially symmetric) top. Symmetry of the top implies that $I _ { 1 } = I _ { 2 }$ . The potential energy function $\nu$ is obtained by introducing the fixed reference vector $r ^ { 0 }$ to point from the stationary point of contact to the center of mass, i.e. $\boldsymbol { r } ^ { 0 } = ( 0 , 0 , L ) ^ { T }$ . We set the distance from the fixed point to the center of mass equal to one, i.e., $L = 1$ . Then the potential energy becomes

$$
\mathcal { V } ( Q ) = - c k ^ { T } Q r ^ { 0 } ,
$$

where $\pmb { k } = ( 0 , 0 , - 1 ) ^ { T }$ gives the direction of gravity and $c = m g$ is the product of the mass $m$ of the top and the gravitational constant $g$ . The orthogonal matrix $Q ( t )$ describes the rotation of the rigid body about its stationary point of contact and $Q ^ { T } = [ s _ { 1 } , s _ { 2 } , s _ { 3 } ]$ as before. Note that the potential energy can be written as a function of $s _ { 3 }$ alon

$$
{ \mathcal { V } } ( s _ { 3 } ) = - c \left[ r ^ { 0 } \right] ^ { T } Q ^ { T } k = c \left[ r ^ { 0 } \right] ^ { T } s _ { 3 } .
$$

Employing the above outlined abstract Hamiltonian framework, we obtain the equations of motion

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { \pi } = \pmb { \pi } \times \pmb { T } ^ { - 1 } \pmb { \pi } + c \pmb { s } _ { 3 } \times \pmb { r } ^ { 0 } , } \\ { \displaystyle \frac { d } { d t } \pmb { s } _ { i } = \pmb { s } _ { i } \times \pmb { T } ^ { - 1 } \pmb { \pi } , \qquad ( i = 1 , 2 , 3 ) . } \end{array}
$$

These equations can be integrated using the composition method (8.37) with the kinetic energy part integrated by the standard splitting (8.34). However, one can solve the free Euler equation for a symmetric rigid body exactly. To do so, we split the kinetic energy into two contributions [193, 54]

$$
\mathcal { T } = \frac { 1 } { 2 I } \pmb { \pi } ^ { T } \pmb { \pi } + \frac { 1 } { 2 } \left( \frac { 1 } { I _ { 3 } } - \frac { 1 } { I } \right) \pi _ { 3 } ^ { 2 } ,
$$

$I = I _ { 1 } = I _ { 2 }$ , instead of three which yields the modified composition method

$$
\pmb { \psi } _ { \Delta t , \mathcal { T } } = \pmb { \phi } _ { \Delta t , \tilde { \mathcal { T } } _ { 2 } } \circ \pmb { \phi } _ { \Delta t , \tilde { \mathcal { T } } _ { 1 } } ,
$$

where

$$
\tilde { \mathcal { T } } _ { 1 } = \frac { 1 } { 2 I } \pmb { \pi } ^ { T } \pmb { \pi } ,
$$

and

$$
\tilde { \mathcal { T } } _ { 2 } = \frac { 1 } { 2 } \left( \frac { 1 } { I _ { 3 } } - \frac { 1 } { I } \right) \pi _ { 3 } ^ { 2 } .
$$

Note that ${ \pmb { \pi } } ( t ) = c o n s t$ . for the Hamiltonian $\tilde { \tau } _ { 1 }$ which allows for the exact integration of the equation of motion for $\pmb { S } _ { j }$ , $j = 1 , 2 , 3$ ; i.e.,

$$
\frac { d } { d t } \pmb { \pi } = \pmb { 0 } , \qquad \frac { d } { d t } \pmb { s } _ { i } = - \frac { 1 } { I } \pmb { \hat { \pi } } \pmb { s } _ { i } .
$$

Even more importantly, the two Hamiltonian functions $\mathcal { T } _ { 1 } , ~ \mathcal { T } _ { 2 }$ commute and, hence, the composition method $\pmb { \psi } _ { \Delta t , \mathcal { T } }$ is equal to the exact flow map:

$$
\pmb { \phi } _ { \Delta t , \mathscr { T } } = \pmb { \phi } _ { \Delta t , \tilde { \mathscr { T } } _ { 1 } } \circ \pmb { \phi } _ { \Delta t , \tilde { \mathscr { T } } _ { 2 } } .
$$

The exact propagator $\pmb { \phi } _ { \Delta t , \mathcal { T } }$ for the kinetic energy part of the Lagrangian top’s Hamiltonian is now used in (8.37) to obtain a second-order symplectic method for the spinning top.

We conduct a numerical experiments with $c = 1$ and

$$
\pmb { Q } ( 0 ) = \left[ \begin{array} { c c c } { \cos { 0 . 6 } } & { 0 } & { - \sin { 0 . 6 } } \\ { 0 } & { 1 } & { 0 } \\ { \sin { 0 . 6 } } & { 0 } & { \cos { 0 . 6 } } \end{array} \right] .
$$

This corresponds to an initial $\pmb { \mathscr { s } } _ { 3 } = ( \sin 0 . 6 , 0 , \cos 0 . 6 ) ^ { T }$ . The equations of motion are integrated with the above splitting methods using a stepsize of $\Delta t = 0 . 1$ . The motion of the center of mass $\pmb q _ { \mathsf { c m } } ( t ) = \pmb Q r ^ { 0 }$ is given in Fig. 8.3 for $I _ { 1 } = I _ { 2 } = 5$ , $I _ { 3 } = 1$ , and the initial body angular momentum ${ \pmb { \pi } } = ( 0 , 0 , 5 ) ^ { T }$ . The error in energy and the motion of the $Z$ -component of $\pmb { q } _ { \mathsf { c m } } ( t )$ are shown on the right of Fig. 8.3. Note that this experiment corresponds to a Lagrangian top initially spinning only about its axis of symmetry and which is released from that position without applying any additional torque. See also [7, 73] and problem 4 in the Exercises.

![](images/3119009912860178d9b99273e09d3167ec270794c509fb6bb8407aad4b63372c.jpg)  
Figure 8.3 Motion of the Lagrangian top, as computed with an explicit splitting method.

As a second test we implemented the splitting algorithm (8.37) for the symmetric top example of Section 8.1.4 with the purpose of comparing with our previously computed RATTLE solution. For a stepsize of $\Delta t = 0 . 1$ and with the exact propagator (8.40) used in (8.37), the numerical trajectories are essentially indistinguishable from those obtained using RATTLE. However, the splitting scheme preserves the energy better by a factor of about 40. Furthermore, the splitting method is much easier to implement and more efficient than the RAT-TLE approach and emerges here as the clear winner.

The situation changes when the exact propagator (8.40) is replaced by the standard kinetic energy splitting (8.34). The results, using an identical timestep of $\Delta t = 0 . 1$ are shown in Fig. 8.4. There are some significant differences with the results using RATTLE (compare with Fig. 8.2). First, the new trajectory appears to be somewhat less regular, related to the appearance for the first time of sharp peaks in the evolution of the energy error. In Fig. 8.5 a projection of a very long time numerical solution in the neighborhood of the upright body position is shown for each method, dramatizing the improved regularity of the RATTLE orbit. Even more striking, perhaps, is the fact that the new computation finds too many quasi-periods (22 instead of 19) in the integration on [0, 200]. In fact 19 is very nearly the correct figure for this time interval, and this is only achieved by an eight-fold reduction in the integration timestep. On the other hand, the standard reduction/splitting method exhibits better energy conservation, even at the large timestep, than the RATTLE approach. (A careful comparison of methods must include attention to the efficient implementation of the RATTLE nonlinear solver, which can add to the work.)

![](images/e1ac24df038df6bc00d2ed54fd35c6517eabbc920d074a382e18dc7cf94a9632.jpg)  
Figure 8.4 Motion of the symmetric sprung top, as computed using the standard reduction/splitting scheme.

The experiment highlights the necessity for a careful choice of the splitting. It is often advisable to use a splitting of the rigid body kinetic energy into an entirely symmetric contribution $\begin{array} { r } { \mathcal { T } _ { \mathsf { s } } = \frac { 1 } { 2 I } \pmb { \pi } ^ { T } \pmb { \pi } } \end{array}$ and a “perturbation,” i.e.

$$
\mathcal { T } = \frac { 1 } { 2 I } \pmb { \pi } ^ { T } \pmb { \pi } + \frac { 1 } { 2 } \left( \frac { 1 } { I _ { 1 } } - \frac { 1 } { I } \right) \pi _ { 1 } ^ { 2 } + \frac { 1 } { 2 } \left( \frac { 1 } { I _ { 2 } } - \frac { 1 } { I } \right) \pi _ { 2 } ^ { 2 } + \frac { 1 } { 2 } \left( \frac { 1 } { I _ { 3 } } - \frac { 1 } { I } \right) \pi _ { 3 } ^ { 2 } .
$$

A natural choice is to set $I = I _ { j }$ for some appropriate index $i \in \{ 1 , 2 , 3 \}$ (see [56] for a detailed comparison).

# 8.3.3 Integrable discretization: RATTLE and the scheme of MOSER AND VESELOV

The free rigid body is completely integrable. It was first pointed out that a completely integrable discretization for the free rigid body is possible in an article of

$\Delta t ( Y ^ { n + 1 } - [ { Y ^ { n + 1 } } ] ^ { T } )$ coincides with the second step of the Moser–Veselov algorithm.

# 8.4 Order 4 and order 6 variants of RATTLE for the free rigid body

The observation mentioned above due to MCLACHLAN AND ZANNA [127] of the exact integrability of the RATTLE method has ramifications for the design of higher-order schemes. When applied with constant step size, it follows from the integrability result that the RATTLE scheme solves exactly the modified equation

$$
\frac { d } { d t } \pmb { \pi } = ( 1 + \Delta t ^ { 2 } \tau _ { 3 } + \Delta t ^ { 4 } \tau _ { 5 } + \cdot \cdot \cdot ) \pmb { \pi } \times \pmb { T } ^ { - 1 } \pmb { \pi } ,
$$

where the $\tau _ { 2 i + 1 }$ are constants depending on the Hamiltonian, the inertial tensor $\tau$ , the mass tensor $R$ and the Casimir $\| \pmb { \pi } \|$ . This modified equation is a time reparametization of the original free rigid body equation. Hence, by rescaling the initial condition $\pmb { \pi } _ { 0 }$ it is possible to improve the order of RATTLE.

Introduce the family of constants

$$
C _ { R , i , j } = r _ { 1 1 } ^ { i } r _ { 2 2 } ^ { j } + r _ { 1 1 } ^ { i } r _ { 3 3 } ^ { j } + r _ { 2 2 } ^ { i } r _ { 3 3 } ^ { j } , \qquad i , j = 1 , 2 , \ldots ,
$$

associated to the mass tensor $R$ and set

$$
C _ { R , i } = C _ { R , i , i } , \qquad C _ { R } = C _ { R , 1 } .
$$

Denote as

$$
{ \mathcal H } _ { 2 } = r _ { 1 1 } ^ { 2 } \pi _ { 1 } ^ { 2 } + r _ { 2 2 } ^ { 2 } \pi _ { 2 } ^ { 2 } + r _ { 3 3 } ^ { 2 } \pi _ { 3 } ^ { 2 } ,
$$

the constant which is a linear combination of the Hamiltonian $\mathcal { H }$ and the Casimir $\| { \pmb { \pi } } \|$ of the free rigid body. Consider the constants

$$
\tau _ { 3 } = \frac { 1 } { 6 \operatorname * { d e t } ( { \cal T } ) ^ { 2 } } \left( ( 3 \operatorname * { d e t } ( { \cal R } ) \mathrm { t r } ( { \cal R } ) + C _ { { \cal R } , 2 } ) \| \pi \| ^ { 2 } + ( 3 C _ { { \cal R } } + \mathrm { t r } ( { \cal R } ^ { 2 } ) ) \mathcal { H } _ { 2 } \right) ,
$$

and

$$
\begin{array} { l } { \displaystyle \tau _ { 5 } = \frac { 1 } { 4 0 \mathrm { d e t } ( T ) ^ { 4 } } \Big ( \big ( 3 \mathrm { t r } ( R ^ { 4 } ) + 2 7 C _ { R , 2 } + 1 5 \mathrm { t r } ( R ^ { 2 } ) C _ { R } + 4 5 \mathrm { d e t } ( R ) \mathrm { t r } ( R ) \big ) \mathcal { H } _ { 2 } ^ { 2 } } \\ { \displaystyle \quad + \big ( 1 0 C _ { R , 3 } + 5 0 \mathrm { d e t } ( R ) \mathrm { t r } ( R ) C _ { R } } \\ { \displaystyle \quad + 1 0 \mathrm { d e t } ( R ) \mathrm { t r } ( R ^ { 2 } ) + 2 C _ { R , 2 } \mathrm { t r } ( R ^ { 2 } ) } \\ { \displaystyle \quad - 2 8 \mathrm { d e t } ( R ^ { 2 } ) ) \| \pi \| ^ { 2 } \mathcal { H } _ { 2 } } \\ { \displaystyle \quad + \big ( 6 0 \mathrm { d e t } ( R ^ { 2 } ) C _ { R } + 3 C _ { R , 4 } + 2 7 \mathrm { d e t } ( R ^ { 2 } ) \mathrm { t r } ( R ^ { 2 } ) } \\ { \displaystyle \quad + 1 5 \mathrm { d e t } ( R ) \big ( C _ { R , 2 , 3 } + C _ { R , 3 , 2 } ) \big ) \| \pi \| _ { 2 } ^ { 4 } \Big ) . } \end{array}
$$

![](images/bfbd92a941f3ad9ce5bbc1624718d9d472017a0fbef032650f9219dc835e3075.jpg)  
Figure 8.5 Motion of the symmetric sprung top, as computed using the standard reduction/splitting scheme (left) and using the RATTLE approach (right).

MOSER AND VESELOV [141] (see also LEWIS AND SIMO [114]). Perhaps as remarkable in our context is the fact, noted by MCLACHLAN AND ZANNA [127], that the RATTLE method when applied to the free rigid body is actually equivalent to the Moser–Veselov algorithm.

To see this, introduce into the RATTLE method (8.17)–(8.21) the auxiliary variables ${ \pmb Y } ^ { n } = { \pmb P } ^ { n } [ { \pmb Q } ^ { n } ] ^ { T } , { \pmb Y } ^ { n + 1 / 2 } = { \pmb P } ^ { n + 1 / 2 } [ { \pmb Q } ^ { n } ] ^ { T }$ and $\pmb { Y } ^ { n + 1 } = \pmb { P } ^ { n + 1 } [ \pmb { Q } ^ { n + 1 } ] ^ { T }$ . By construction, one has $Y ^ { n } = R \hat { \pmb { \omega } } ^ { n }$ and hence ${ \widehat { \pmb { \pi } } } ^ { n } = { \pmb { Y } } ^ { n } - [ { \pmb { Y } } ^ { n } ] ^ { T }$ . Moreover, $\begin{array} { r } { { \pmb Y } ^ { n + 1 / 2 } = { \pmb Y } ^ { n } - \frac { 1 } { 2 } \Delta t { \pmb Q } ^ { n } [ { \pmb P } ^ { n + 1 / 2 } ] ^ { T } { \pmb R } ^ { - 1 } { \pmb P } ^ { n + 1 / 2 } [ { \pmb Q } ^ { n } ] ^ { T } = { \pmb Y } ^ { n } + \Delta t { \pmb S } , } \end{array}$ , where $s$ is a symmetric matrix. Introducing $Q = Q ^ { n + 1 } [ Q ^ { n } ] ^ { T } = I _ { 3 } + \Delta t R ^ { - 1 } P ^ { n + 1 / 2 } [ Q ^ { n } ] ^ { T } =$ $I _ { 3 } + \Delta t { \cal R } ^ { - 1 } \mathsf { Y } ^ { n + 1 / 2 }$ , it is immediately verified that $Q ^ { n + 1 }$ is orthogonal if and only if $Q$ is orthogonal.

Now, we rewrite $\Delta t \widehat { \pmb { \pi } } ^ { n } = \Delta t ( \pmb { Y } ^ { n } - [ \pmb { Y } ^ { n } ] ^ { T } )$ in terms of $Q$ . We have $\Delta t \widehat { \pmb { \pi } } ^ { n } =$ $R ( Q - I _ { 3 } ) - \Delta t ^ { 2 } S - ( Q ^ { T } - I _ { 3 } ) R + \Delta t ^ { 2 } S ^ { T } = R Q - Q ^ { T } R$ , since $s$ is symmetric. The equation $\Delta t \widehat { \pmb { \pi } } ^ { n } = { \pmb R } \pmb { Q } - { \pmb Q } ^ { T } { \pmb R }$ is precisely the Moser–Veselov equation that one has to solve for an orthogonal matrix $Q$ . Similarly, $\Delta t \widehat { \pmb { \pi } } ^ { n + 1 } = { Q } { R } - { R } { Q } ^ { T } =$

Scaling the initial condition $\pmb { \pi } _ { 0 }$ to ${ \pmb { \pi } } _ { 0 } / ( 1 { + } \Delta t ^ { 2 } \tau _ { 3 } )$ , applying the RATTLE scheme, and then multiplying back by $\left( 1 + \Delta t ^ { 2 } \tau _ { 3 } \right)$ , raises the order of the RATTLE scheme from 2 to 4, and preserves integrability and symplecticity.

Similarly, scaling the initial condition $\pmb { \pi } _ { 0 }$ to ${ \pmb { \pi } } _ { 0 } / ( 1 + \Delta t ^ { 2 } \tau _ { 3 } + \Delta t ^ { 4 } ( \tau _ { 5 } - 2 \tau _ { 3 } ^ { 2 } ) )$ , applying RATTLE and multiplying back by the same scaling factor, improves the order of RATTLE to 6. For more details on these methods and accompanying numerical experiments, see [127].

# 8.5 Freely moving rigid bodies

So far, we have considered a single rigid body with its center of mass held fixed. We now relax this condition and consider a freely moving rigid body. Let us assume that a spatial coordinate system is given and that the represention of a vector in spatial coordinates is denoted by $q \in \mathbb { R } ^ { 3 }$ . The particular spatial vector that points from the origin of the laboratory frame to the center of mass of the rigid body is denoted by $\pmb q _ { c m }$ . We consider also a fixed reference vector $r ^ { 0 }$ that points from the center of mass to a given (fixed) point on the rigid body. Then the position of this point is given by the spatial vector

$$
\pmb { q } ( t ) = \pmb { q } _ { c m } ( t ) + \pmb { Q } ( t ) \pmb { r } ^ { 0 } = \pmb { q } _ { c m } ( t ) + \sum _ { j = 1 } ^ { 3 } \left( \pmb { s } _ { j } ( t ) ^ { T } \pmb { r } ^ { 0 } \right) \pmb { e } _ { j } ,
$$

where $e _ { j }$ $_ { \cdot j } , j = 1 , 2 , 3$ , are (fixed) coordinate vectors in the laboratory frame.6 Thus the motion of any fixed point on the rigid body is completely characterized by the evolution of the center of mass $\pmb q _ { c m }$ and the three vectors $s _ { j }$ . Let us assume for a moment that no external forces act on the rigid body. Then the equations of motion for the center of mass and the rotation matrix decouple and are simply given by

$$
\frac { d } { d t } \pmb { \pi } = \pmb { \pi } \times \pmb { T } ^ { - 1 } \pmb { \pi } , \qquad \frac { d } { d t } s _ { j } = s _ { j } \times \pmb { T } ^ { - 1 } \pmb { \pi } , \quad ( j = 1 , 2 , 3 ) ,
$$

and

$$
\frac { d } { d t } \pmb { q } _ { c m } = \frac { 1 } { M } \pmb { p } _ { c m } , \qquad \frac { d } { d t } \pmb { p } _ { c m } = \mathbf { 0 } .
$$

$M$ is the total mass of the rigid body and $\pmb { p _ { c m } } \in \mathbb { R } ^ { 3 }$ the momentum of the center of mass. The combined system can be propagated in time by solving the center of mass equations of motion exactly and by applying the second-order symplectic

integration method for the Euler equations as suggested in the previous section. Let us denote the resulting time- $\Delta t .$ -propagator by $\pmb { \psi } _ { \Delta t , \mathcal { T } }$ , where $\tau$ stands for the kinetic energy

$$
\mathcal { T } = \frac { 1 } { 2 M } \| \pmb { p } _ { c m } \| ^ { 2 } + \frac { 1 } { 2 } \pmb { \pi } ^ { T } \pmb { T } ^ { - 1 } \pmb { \pi } ,
$$

of the unforced rigid body.

Consider now a rigid body with an $\mathsf { e x }$ ternal force $F$ acting at a (fixed) reference point $r ^ { 0 }$ on the rigid body. In other words, the force is assumed to be given in spatial coordinates by

$$
\pmb { F } ( \pmb { q } ) = - \nabla _ { \pmb { q } } V ( \pmb { q } ) , \quad \pmb { q } = \pmb { Q } r ^ { 0 } + \pmb { q } _ { c m } .
$$

Then, upon applying (8.41), we formally obtain

$$
\mathcal { V } ( \pmb { q } _ { c m } , s _ { 1 } , s _ { 2 } , s _ { 3 } ) = V ( \pmb { q } ) = V \left( \pmb { q } _ { c m } + \sum _ { j = 1 } ^ { 3 } \left( s _ { j } ^ { T } r ^ { 0 } \right) \pmb { e } _ { j } \right) .
$$

It is easily verified (see Example 1) that the equations of motion corresponding to the potential energy $\nu$ are given by

$$
\frac { d } { d t } \pmb { \pi } = \pmb { r } ^ { 0 } \times \sum _ { j = 1 } ^ { 3 } \left( \pmb { e } _ { j } ^ { T } \pmb { F } ( \pmb { q } ) \right) \pmb { \mathfrak { s } } _ { j } , \qquad \frac { d } { d t } \pmb { s } _ { j } = \pmb { 0 } , \quad ( j = 1 , 2 , 3 ) ,
$$

and

$$
\frac { d } { d t } \pmb { q } _ { c m } = \mathbf { 0 } , \qquad \frac { d } { d t } \pmb { p } _ { c m } = \pmb { F } ( \pmb { q } ) .
$$

A symplectic splitting method can be based on

$$
\mathcal { H } = \frac { 1 } { 2 } \mathcal { V } + \mathcal { T } + \frac { 1 } { 2 } \mathcal { V } .
$$

We have already derived several second-order symplectic methods $\pmb { \psi } _ { \Delta t , \mathcal { T } }$ for the integration of the Hamiltonian $\mathcal { H } = \mathcal { T }$ (free rigid body). The equations of motion corresponding to $\varkappa = \nu$ can be integrated exactly since $d \pmb { q } _ { C m } / d t = d \pmb { s } _ { i } / d t =$ $d \pmb q / d t = \pmb 0$ . Let us denote the corresponding flow map by $\phi _ { t , \gamma }$ . Then a secondorder symplectic method for the integration of (8.42) is provided by the composition method

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t / 2 , \mathscr { V } } \circ \pmb { \psi } _ { \Delta t , \mathscr { T } } \circ \pmb { \phi } _ { \Delta t / 2 , \mathscr { V } } .
$$

This splitting approach to the integration of rigid bodies was proposed by TOUMA AND WISDOM in [193] and by REICH in [156].

Example 2Consider a completely symmetric rigid body; i.e. $I = I _ { 1 } = I _ { 2 } = I _ { 3 }$ ，with a spring attached to it at a point $r ^ { 0 }$ on the rigid body. The spring is assumed to have a rest length $L$ , a spring constant $\boldsymbol { K }$ , and its second end being attached to the origin of the coordinate system. The potential energy of the spring is

$$
V ( \pmb q ) = \frac { K } { 2 } ( r - L ) ^ { 2 } ,
$$

where $r = \| \pmb { q } \|$ , $\pmb q = \pmb q _ { c m } + \pmb Q r ^ { 0 }$ , and the spatial force is

$$
\boldsymbol { F } ( \boldsymbol { q } ) = - K \frac { r - L } { r } \boldsymbol { q } .
$$

The force $F _ { c m }$ acting on the center of mass is

$$
\pmb { F } _ { c m } = \pmb { F } ( \pmb { q } ) = - K \frac { r - L } { r } \left( \pmb { q } _ { c m } + \sum _ { j = 1 } ^ { 3 } ( \pmb { s } _ { j } ^ { T } \pmb { r } ^ { 0 } ) \pmb { e } _ { j } \right) ,
$$

and the applied torque $N$ in body coordinates is

$$
\pmb { N } = K \frac { r - I } { r } \sum _ { j = 1 } ^ { 3 } ( \pmb { q } ^ { T } \pmb { e } _ { j } ) \pmb { s } _ { j } \times \pmb { r } ^ { 0 } .
$$

The kinetic energy of the rigid body is

$$
\mathcal { T } = \frac { 1 } { 2 \cal { I } } \pmb { \pi } ^ { T } \pmb { \pi } + \frac { 1 } { 2 \cal { M } } \pmb { p } _ { c m } ^ { T } \pmb { p } _ { c m } ,
$$

with associated free rigid body equations of motion

$$
\frac { d } { d t } \pmb { \pi } = \mathbf { 0 } , \qquad \frac { d } { d t } \pmb { s } _ { j } = - I ^ { - 1 } \pmb { \widehat { \pi } } \pmb { s } _ { j } , \quad ( j = 1 , 2 , 3 ) ,
$$

and

$$
\frac { d } { d t } { \pmb { p } } _ { c m } = { \bf 0 } , \qquad \frac { d } { d t } { \pmb { q } } _ { c m } = M ^ { - 1 } { \pmb { p } } _ { c m } ,
$$

which can be solved exactly. Thus a symplectic integrator can be based on the splitting

$$
\mathcal { H } = \frac { 1 } { 2 } \mathcal { V } + \mathcal { T } + \frac { 1 } { 2 } \mathcal { V } ,
$$

with each of the three entries being explicitly integrable.

We conduct a numerical experiment for the set of parameters $I = K = M = L = 1$ and $r ^ { 0 } = ( 0 , 0 , 1 )$ . The initial conditions are $\pmb q _ { c } = \pmb q$ , $Q = \pmb { I }$ , ${ \pmb { \pi } } = ( 1 , 1 , 2 ) ^ { T }$ , and $\pmb { p } _ { c } = ( 1 , 0 , 0 ) ^ { T }$ . See Fig. 8.6 for the numerical results obtained for $\Delta t = 0 . 0 1$ . ✷

![](images/1c03a7986e8d2b9a30817e94ced329575ed128ec295bc9de4fc08d4316151236.jpg)  
Figure 8.6 Rigid body motion under an external force field.

The approach described so far easily generalizes to systems of interacting rigid bodies. The associated algorithm has been successfully applied to rigid body molecular dynamics by DULLWEBER, LEIMKUHLER, AND MCLACHLAN [54].

We mention that one can also treat rigid bodies that are linked by constraints. Take, for example, two rigid bodies that are connected by a rigid rod linking a material point $r _ { 1 } ^ { 0 }$ on the first rigid body and a material point $r _ { 2 } ^ { 0 }$ on the second body. The associated (holonomic) constraint can be formulated as

$$
0 = r _ { 1 2 } - L ,
$$

where $L$ is the length of the rod and $r _ { 1 2 } = \| r _ { 1 2 } \|$

$$
\pmb { r } _ { 1 2 } = \pmb { q } _ { c m , 1 } + \pmb { Q } _ { 1 } \pmb { r } _ { 1 } ^ { 0 } - \pmb { q } _ { c m , 2 } - \pmb { Q } _ { 2 } \pmb { r } _ { 2 } ^ { 0 } .
$$

The Hamiltonian of the systems is

$$
\mathcal { H } = \mathcal { T } _ { 1 } + \mathcal { T } _ { 2 } + \lambda ( r _ { 1 2 } - L ) .
$$

Although such systems can be treated numerically by a natural extension of the splitting methods considered in this chapter, it is probably conceptually easier to apply an approach based on a RATTLE discretization in terms of rotation matrices.

# 8.6 Other formulations for rigid body motion

We next briefly outline other popular choices for formulating rigid body dynamics. The following two approaches can be viewed as defining a set of generalized coordinates $\pmb { \xi }$ in some appropriate configuration space, together with a map from the parameter space to the $3 \times 3$ orthogonal matrices.

While each of these choices of parameters can be used as the basis for numerical simulation, they have certain disadvantages compared with the methods outlined in the previous sections.

# 8.6.1 Euler angles

It was observed by EULER (ca. 1776) that the orientation of a body in space can be specified in terms of three successive rotations with respect to some set of coordinate axes fixed in the body. The specific sequence of rotations used by Euler is as follows:

1. A counterclockwise rotation about the z-axis through an angle $\alpha$

2. A counterclockwise rotation about the $x - \mathsf { a x i s }$ through an angle $\beta$ .

3. A counterclockwise rotation about the z-axis through an angle $\gamma$

The rotation matrix $Q$ can be expressed as a product of these three planar rotations according to

$$
\pmb { Q } = \left[ \begin{array} { c c c } { \cos \gamma } & { \sin \gamma } & { 0 } \\ { - \sin \gamma } & { \cos \gamma } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \beta } & { \sin \beta } \\ { 0 } & { - \sin \beta } & { \cos \beta } \end{array} \right] \left[ \begin{array} { c c c } { \cos \alpha } & { \sin \alpha } & { 0 } \\ { - \sin \alpha } & { \cos \alpha } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] .
$$

There is nothing particularly special about the choice of axes for rotations ( $Z$ , then $x$ , then $Z$ ) used by Euler: the only restriction is that no two successive $\mathtt { a x e s }$ of the sequence may be the same. The Euler angles provide a parameterized description of the space of rotation matrices, and associated equations of motion can be derived. However these equations do not cover all possible orientations of a rigid body, and singularities in the equations defining the parameters complicate numerical integration of the resulting equations of motion, not just at the point of singularity, but also in the vicinity of it. One way of resolving the problem is to switch to a new set of angle variables (defined by a different sequence of axes) whenever integration proceeds into the vicinity of a singular point, but this approach is algorithmically cumbersome and suffers from the several other problems mentioned for local charts in Chapter 7. In particular, it is very difficult to obtain a satisfactory geometric method based on this approach.

# 8.6.2 Quaternions

Because of problems with the Euler angles, an alternative set of parameters is more frequently used in simulations, based on Hamilton’s quaternions. This approach is essentially equivalent to the use of “Euler parameters” or “Cayley– Klein variables,” although implementations may vary slightly.

Hamilton’s quaternions are a quadruple of parameters ${ \pmb \sigma } = ( \sigma _ { 0 } , \sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } )$ subject to the constraint $\sigma _ { 0 } ^ { 2 } + \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } + \sigma _ { 3 } ^ { 2 } = 1$ . The rotation matrix is defined in terms of the parameters by

$$
\pmb { Q } = \pmb { I _ { 3 } } + 2 \sigma _ { 0 } \hat { \pmb { e } } + 2 \hat { \pmb { e } } ^ { 2 } , \qquad \hat { \pmb { e } } = \left[ \begin{array} { c c c } { 0 } & { - \sigma _ { 3 } } & { \sigma _ { 2 } } \\ { \sigma _ { 3 } } & { 0 } & { - \sigma _ { 1 } } \\ { - \sigma _ { 2 } } & { \sigma _ { 1 } } & { 0 } \end{array} \right] .
$$

The quaternions obey coupled differential equations involving the body angular momenta $\pmb { \pi }$ . These differential equations take the form

$$
\frac { d } { d t } \pmb { \sigma } = \pmb { B } ( \pmb { \sigma } ) \pmb { T } ^ { - 1 } \pmb { \pi } ; \qquad \frac { d } { d t } \pmb { \pi } = \hat { \pmb { \pi } } \pmb { T } ^ { - 1 } \pmb { \pi } + \pmb { N } ,
$$

where $\pmb { T } = \mathrm { d i a g } ( I _ { 1 } , I _ { 2 } , I _ { 3 } )$ is the (diagonalized) inertial tensor,

$$
B ( \pmb { \sigma } ) = \left[ \begin{array} { c c c } { - \sigma _ { 1 } } & { - \sigma _ { 2 } } & { - \sigma _ { 3 } } \\ { \sigma _ { 0 } } & { - \sigma _ { 3 } } & { \sigma _ { 2 } } \\ { \sigma _ { 3 } } & { \sigma _ { 0 } } & { - \sigma _ { 1 } } \\ { - \sigma _ { 2 } } & { \sigma _ { 1 } } & { \sigma _ { 0 } } \end{array} \right] ,
$$

and $N$ is the applied torque in body coordinates.

The equations of motion can be shown to be Hamiltonian with a noncanonical Lie–Poisson structure similar to that of the Euler equation. In fact, the same splitting ideas as developed in Section 8.3.1 can be applied and lead essentially to identical propagation schemes. The only difference is that one either works directly with the rotation matrix $Q \in \mathbb { R } ^ { 3 \times 3 }$ or with $\pmb { \sigma } \in \mathbb { R } ^ { 4 }$ and employs the relation (8.44).

A constrained Hamiltonian version of the quaternionic description is also possible by viewing the quaternions as a set of generalized coordinates subject to the holonomic constraint $\| \pmb { \sigma } \| ^ { 2 } = 1$ . Using (8.44), we introduce $\pmb { \sigma }$ and $\dot { \pmb { \sigma } }$ into the rigid body Lagrangian (8.5) and determine the canonical momenta through the formula

$$
p _ { \sigma } = \frac { \partial L } { \partial \dot { \sigma } } .
$$

Although symplectic integration methods based on such an approach can be formulated, the RATTLE approach based on the rotation matrix $Q$ is found to be more efficient and conceptional easier to implement.

# 8.7 Exercises

1. Lagrange and Hamiltonian equations for rigid bodies. Verify the gradient expression (8.16) using the definition (8.15). Also show that

$$
P R ^ { - 1 } = \frac { 1 } { 2 } \nabla _ { P } \mathrm { t r } ( P R ^ { - 1 } P ^ { T } ) .
$$

Essentially the same result can be used to derive the constrained Lagrange equation from the Lagrangian function (8.5). (Hint: You may find the identities

$$
\mathrm { t r } ( \pmb { A } ) = \mathrm { t r } ( \pmb { A } ^ { T } ) , \quad \mathrm { t r } ( \pmb { A } \pmb { B } ) = \mathrm { t r } ( \pmb { B } \pmb { A } ) , \quad \pmb { u } ^ { T } \pmb { v } = \mathrm { t r } ( \pmb { u } \pmb { v } ^ { T } )
$$

useful.)

2. Planar rigid bodies. Let us introduce a set of orthogonal unit vectors $t _ { i } \in \mathbb { R } ^ { 3 }$ $j = 1 , 2 , 3$ , such that

$$
Q = [ t _ { 1 } , t _ { 2 } , t _ { 3 } ] \in \mathbb { R } ^ { 3 \times 3 } .
$$

We also write

$$
\dot { Q } = [ \dot { t } _ { 1 } , \dot { t } _ { 2 } , \dot { t } _ { 3 } ]
$$

for the time derivative. The rotational kinetic energy of a rigid body can then be expressed as

$$
T _ { \mathrm { r o t } } = \frac 1 2 \mathrm { t r } ( \dot { Q } R \dot { Q } ^ { T } ) = \frac 1 2 \sum _ { i = 1 } ^ { 3 } r _ { i i } \lVert \dot { \pmb { t } } _ { i } \rVert ^ { 2 } .
$$

We have $r _ { 3 3 } = 0$ for a planar rigid body and the rotational kinetic energy reduces to

$$
T _ { \mathrm { r o t } } = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { 2 } { r _ { i i } \| \dot { \bf t } _ { i } \| ^ { 2 } } .
$$

Since the third unit vector $t _ { 3 }$ is no longer part of the equations, we also redefine the matrix $Q$ by

$$
Q = [ t _ { 1 } , t _ { 2 } ] \in \mathbb { R } ^ { 3 \times 2 } .
$$

This matrix still satisfies $Q ^ { T } Q = I _ { 2 }$ but $I _ { 2 }$ is now the $2 \times 2$ identity matrix.

a. Verify that

$$
T _ { \mathrm { r o t } } = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { 2 } r _ { i i } \lVert \dot { \pmb { t } } _ { i } \rVert ^ { 2 } = \frac { 1 } { 2 } \mathrm { t r } ( \dot { \pmb { Q } } \pmb { R } \dot { \pmb { Q } } ^ { T } ) ,
$$

with $\dot { \pmb Q } = [ \dot { \pmb t } _ { 1 } , \dot { \pmb t } _ { 2 } ] \in \mathbb { R } ^ { 3 \times 2 }$ and

$$
\begin{array} { r } { R = \left[ { \begin{array} { c c } { r _ { 1 1 } } & { 0 } \\ { 0 } & { r _ { 2 2 } } \end{array} } \right] . } \end{array}
$$

b. The augmented Lagrangian takes the expression

$$
\tilde { L } = T _ { \mathrm { r o t } } ( \dot { Q } ) + T _ { \mathrm { t r a n s } } ( \dot { q } _ { \mathrm { c m } } ) - V _ { \mathrm { e x t } } ( Q , q _ { \mathrm { c m } } ) - \mathrm { t r } ( ( Q ^ { T } Q - I _ { 2 } ) \varLambda ) .
$$

Derive the associated Hamiltonian equations of motion and suggest a numerical implementation.

3. Mass tensor and inertia tensor. Let $R$ be the diagonal mass tensor of a free rigid body and $\tau$ the corresponding diagonal inertia tensor. We have the following relation between the diagonal elements of these two matrices

$$
t _ { i i } = \sum _ { j \neq i } r _ { j j } .
$$

Show that this relation implies that

$$
\widehat { b } R + R \widehat { b } = \widehat { T b }
$$

holds for any vector $b$ and associated skew-symmetric matrix $\widehat { b }$ .

4. Lagrangian top. Show that the third component $m _ { 3 } = s _ { 3 } ^ { T } \pmb { \pi }$ of the spatial angular momentum vector $m = Q \pi$ is preserved under the equations (8.38)– (8.39) for the symmetric top. Show that the third component $\pi _ { 3 }$ of the body angular momentum is also preserved. Denote the energy of the Lagrangian top by $E$ and introduce the four constants (compare [7, 73])

$$
\begin{array} { l } { \alpha = \displaystyle \frac { 2 E - \pi _ { 3 } ^ { 2 } / m _ { 3 } } { I _ { 1 } } , } \\ { \beta = \displaystyle \frac { c } { I _ { 1 } } , } \\ { a = \displaystyle \frac { \pi _ { 3 } } { I _ { 1 } } , } \\ { b = \displaystyle \frac { m _ { 3 } } { I _ { 1 } } . } \end{array}
$$

Provided that the distance between the stationary point of contact and the center of mass is equal to one, it can be shown that the third component $u ( t ) = q _ { 3 } ( t )$ of the center of mass motion $\pmb q _ { \mathrm { c m } } ( t ) = \pmb Q ( t ) \pmb r ^ { 0 }$ satisfies the differential equation

$$
\dot { u } ^ { 2 } = ( 1 - u ^ { 2 } ) ( \alpha - \beta u ) - ( b - a u ) ^ { 2 } .
$$

Of particular importance are the two roots of

$$
0 = ( 1 - u _ { i } ^ { 2 } ) ( \alpha - \beta u _ { i } ) - ( b - a u _ { i } ) ^ { 2 } ,
$$

$j = 1 , 2$ , in the interval $u \in [ - 1 , 1 ]$ . With $u _ { 1 } < u _ { 2 }$ the motion in $u ( t )$ satisfies $u _ { 1 } \leq u ( t ) \leq u _ { 2 }$ . Compute the two roots for the data given in Section 8.3.2 and compare with the computed motion in $u ( t ) ~ = ~ q _ { 3 } ( t )$ as displayed in Fig. 8.3. Note also that the initial body angular momentum vector implies that $u _ { 2 } = b / a$ .

5. Structure matrix and Casimir functions. Find the structure matrix $J$ corresponding to the Hamiltonian equations of motion for a single rigid body with kinetic energy

$$
\mathcal { T } ( \pmb { p } _ { c m } , \pmb { \pi } ) = \frac { 1 } { 2 m } \pmb { p } _ { c m } ^ { T } \pmb { p } _ { c m } + \frac { 1 } { 2 } \pmb { \pi } ^ { T } \pmb { T } ^ { - 1 } \pmb { \pi } ,
$$

moving in $\mathbb { R } ^ { 3 }$ under a potential energy $\mathcal { V } ( q _ { c m } , s _ { 1 } , s _ { 2 } , s _ { 3 } )$ . What is the rank of $J ?$ Find the associated Casimir functions.

6. Angular momentum conservation. Show that total angular momentum

$$
\pmb { m } _ { \mathrm { t o t } } = \pmb { q } _ { c m } \times \pmb { p } _ { c m } + \pmb { Q } \pmb { \pi } ,
$$

is conserved for any single rigid body with a potential energy of the form

$$
\mathcal { V } = \psi ( \| \pmb q \| ) , \qquad \pmb q = \pmb q _ { c m } + \pmb { Q } r ^ { 0 } .
$$

7. Numerical conservation of angular momentum. Consider the RATTLE algorithm (8.17)–(8.21) for a free rigid body; i.e. $V _ { \mathrm { e x t } } = 0$ . Show that the spatial angular momentum matrix ${ \widehat { \pmb { m } } } ^ { n } = P ^ { n } [ { \pmb { Q } } ^ { n } ] ^ { T } - { \pmb { Q } } ^ { n } [ { \pmb { P } } ^ { n } ] ^ { T }$ is exactly conserved along numerical solutions. Hint: use the fact that $\widehat { \pmb { m } } ^ { n }$ is skew symmetric.

8. Coupled rigid bodies. Write the equations of motion for two identical rigid bodies with total mass $m$ and tensor of inertia $\tau$ interacting through a harmonic spring with rest length $L$ and force constant $\boldsymbol { K }$ . The spring is attached to the rigid bodies at the material points $r _ { i } ^ { 0 }$ , $i = 1 , 2$ . Give a second-order composition method for the case $I = I _ { 1 } = I _ { 2 } \ne I _ { 3 }$ (symmetric rigid body).

9. Quaternions. Given a unit vector $\textbf { \textit { n } } \in \ \mathbb { R } ^ { 3 }$ and a real number $\omega$ , verify RODRIGUES’ formula

$$
Q = \mathrm { e } ^ { \omega \hat { n } } ,
$$

where the rotation matrix $Q$ is given by (8.44) with $\sigma _ { 0 } = \cos ( \omega / 2 )$ and

$$
\left[ \sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } \right] = \sin ( \omega / 2 ) \left[ n _ { 1 } , n _ { 2 } , n _ { 2 } \right] .
$$

RODRIGUES’ formula is useful for implementing a splitting method for symmetric or nearly symmetric rigid bodies. Note that $\sigma _ { 0 }$ can be replaced by $\sigma _ { 0 } = ( 1 - \omega ^ { 2 } / 4 ) / ( 1 + \omega ^ { 2 } / 4 )$ and

$$
\left[ \sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } \right] = \frac { \omega } { 1 + \omega ^ { 2 } / 4 } \left[ n _ { 1 } , n _ { 2 } , n _ { 2 } \right] ,
$$

which provides an inexpensive approximation to the exact matrix exponential for $\omega \ll 1$ .

# 9

# Adaptive geometric integrators

It is well known that during the integration of nonlinear systems of ordinary differential equations changes in the character of the solutions may demand corresponding changes in the integration timestep. In the context of Hamiltonian systems this need develops from fluctuations in the forces along a solution curve. For motivation we need look no further than the historic Kepler problem which was introduced in Chapter 3. Kepler’s first two laws tell us (i) that a body in bound gravitational motion moves along an ellipse with the fixed point at one focus and that (ii) the orbit sweeps out equal sections of the ellipse in equal times. This is diagrammed in the illustration below (Fig. 9.1), which shows a Keplerian orbit and several points equally spaced in time along the orbit.

![](images/366f47650fb9c197553ec557c95fcb80859c32fd0c57b1ed2d623cdfea233204.jpg)  
Figure 9.1 An orbit of the Kepler problem. The moving body sweeps out equal areas in equal times, moving most rapidly in the vicinity of the fixed body. The points shown along the Kepler ellipse are encountered at uniform intervals in time.

Recall that the force acting on the moving body in the Kepler system is inversely proportional to the square of the separation from the fixed body. When the orbits in the Kepler problem (or, more generally, in a gravitational $N .$ -body problem) are highly eccentric (as they are for example for Comets in our Solar System) the magnitude of the force along orbits can vary considerably. It is clear that the dynamics in the vicinity of close approach will be challenging to resolve accurately. For this reason, some sort of adaptivity in time is essential.1

The traditional approach to varying stepsize in ordinary differential equation solvers is based on selecting a stepsize so that an error estimate is kept below a prescribed tolerance. Because computing the global error is essentially impossible in general purpose integration, the standard approaches use a local error estimate. For example, it is common when integrating with a Runge–Kutta method to add an additional stage to the method so that a higher-order approximation is provided; the difference between the two approximations is then used as an error estimate. Schemes like this can be designed to work with symplectic methods, but the results obtained in numerical experiments are wholly unsatisfying. The observation has been made that, for long term stability, fixed stepsize symplectic methods actually outperform their variable stepsize counterparts when compared on an efficiency basis. This raised a quandary when it first was discovered by GLADMAN, DUNCAN, AND CANDY [72], CALVO AND SANZ-SERNA [42], SKEEL AND GEAR [176] and others in the early 1990s. After all, the symplectic maps form a group, hence the composition of symplectic integrators with various stepsizes

$$
\pmb { \psi } = \pmb { \psi } _ { \Delta t _ { 1 } } \pmb { \psi } _ { \Delta t _ { 2 } } \ldots \pmb { \psi } _ { \Delta t _ { N } } ,
$$

remains a symplectic map. Why should the performance be so poor? The same poor behaviour was observed whether or not the stepsize sequence was obtained from a series of computations based on the solution or was provided a priori.

The best explanation emerged with the development of the backward error analysis. In order to construct the so-called perturbed Hamiltonian expansion for a symplectic method, it is necessary to assume that the symplectic maps used in each timestep are identical. If the stepsize varies, we have the problem that we generate approximations to one, then another perturbed Hamiltonian as the stepsize changes; there is no reason to expect that this sort of process would produce a stable long-term propagation. It seems from this that the prospects for getting good results from symplectic methods with traditional variable stepsize techniques are dim.

# 9.1 Sundman and Poincar´e transformations

The key to effective geometric integration with variable stepsize lies in the use of a time transformation

$$
\frac { d t } { d \tau } = g ( \pmb q , \pmb p ) ,
$$

nearly Keplerian character of many of the trajectories. However, in this instance we are merely using the unmodified Kepler problem as a device to illustrate a general approach to variable stepsize.

where $g$ is a smooth, positive scalar-valued function of positions and momenta. We refer to this as a Sundman transformation. If this transformation is applied to an autonomous system of differential equations, there results a new system of differential equations whose solutions evolve in the rescaled, or “fictive,” time. In fact, the actual orbits of the system do not change; they are just traversed at a different speed. If the original Hamiltonian is $H ( \pmb { q } , \pmb { p } )$ , the system that results from application of (9.1) is

$$
\begin{array} { r l } & { \displaystyle \frac { d } { d \tau } \pmb { q } = \frac { d \pmb { q } } { d t } \frac { d t } { d \tau } = g ( \pmb { q } , \pmb { p } ) \nabla _ { \pmb { p } } H ( \pmb { q } , \pmb { p } ) , } \\ & { \displaystyle \frac { d } { d \tau } \pmb { p } = \frac { d \pmb { p } } { d t } \frac { d t } { d \tau } = - g ( \pmb { q } , \pmb { p } ) \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) . } \end{array}
$$

This system is, in general, no longer Hamiltonian. (It is Hamiltonian in very special cases, such as when the function $g$ is a function of a first integral of the problem – for example the energy – but this choice appears to be of little practical interest.) On the other hand, if $g ( q , - p ) = g ( q , p )$ and $g ( \pmb { q } , \pmb { p } ) > 0$ , then time-reversibility can be maintained by the Sundman transformation. Sundman transformations had actually been in frequent use in computational astronomy from the mid 1960s for varying the timestep (albeit without maintaining the preservation of time-reversal symmetry under subsequent discretization).

Now consider the fixed-stepsize integration of (9.2)–(9.3) with a stepsize $\Delta \tau$ in fictive time, generating a discrete trajectory $\left\{ \left( { \pmb q } ^ { n } , { \pmb p } ^ { n } \right) \right\}$ . Because of the timetransformation, each fixed step in $\tau$ corresponds to a time-step in $t$ of length $\Delta t _ { n } \approx g ( { \pmb q } ^ { n } , { \pmb p } ^ { n } ) \Delta \tau$ . This relation is not exact; in fact, to resolve the time variable we need to numerically solve the differential equation (9.1) in tandem with the system in order to determine the evolution of time. STOFFER [178, 179] pointed out that the system (9.2)–(9.3),(9.1) could be solved by a reversible integrator, yielding a reversible variable stepsize method. A related scheme, also based on reversible Sundman transformation, was suggested in 1995 by the astronomers HUT, MAKINO AND MCMILLAN as a modification of the St¨ormer–Verlet method [90]. The methods mentioned so far are all implicit, a consequence of the coupling the various components of the vector field via the Sundman transformation. This implicitness is undesirable in many of the applications where variable stepsize methods are most likely to be needed, such as gravitational dynamics. A semiexplicit approach (“Adaptive Verlet”) was eventually developed by HUANG AND LEIMKUHLER [89].

Before turning our attention to this scheme, let us consider the symplectic alternative. Along with Sundman transformations, there is another class of time transformations which can be used as the foundation for geometric integration. From a given Hamiltonian $H ( { \pmb q } , { \pmb p } )$ construct a new Hamiltonian by first subtracting the energy $E$ of a trajectory, then multiplying this difference by a positive, smooth scaling function $g ( \pmb { q } , \pmb { p } )$

$$
\tilde { H } ( \pmb { q } , \pmb { p } ) = g ( \pmb { q } , \pmb { p } ) ( H ( \pmb { q } , \pmb { p } ) - E ) .
$$

Noting that the energy is constant along trajectories, we can infer that if at some initial point on the trajectory $H ( q ^ { 0 } , p ^ { 0 } ) = E$ , then this same relation is satisfied at all points of the trajectory, thus, as well, $\tilde { \cal H } \equiv 0$ along this trajectory. The equations of motion for the modified Hamiltonian (9.4) take the form

$$
\begin{array} { l } { \displaystyle \frac { d } { d \tau } q = g ( { q } , { p } ) \nabla _ { p } H ( { q } , { p } ) + ( H ( { q } , { p } ) - E ) \nabla _ { p } g ( { q } , { p } ) , } \\ { \displaystyle \frac { d } { d \tau } p = - g ( { q } , { p } ) \nabla _ { q } H ( { q } , { p } ) - ( H ( { q } , { p } ) - E ) \nabla _ { q } g ( { q } , { p } ) . } \end{array}
$$

These equations can be seen to reduce to (9.2)–(9.3) along the energy surface, thus the Poincar´e and Sundman transformations are formally equivalent, in the absence of perturbation. The transformation (9.4) has the same effect as (9.1) with respect to the exact solutions. This suggests that we could implement a variable stepsize integration strategy by first applying the Poincar´e transformation and then discretizing the resulting system using a fixed stepsize symplectic integrator, an idea independently suggested by HAIRER [78] and REICH [158]. In this case, our numerical method would consist of the iteration of a single symplectic map, so standard backward error analysis (see Chapter 5) could be used to justify the resulting method.

In the context of numerical integrations, however, it should be emphasized that this approach raises some new issues. First, the energy is unlikely to be exactly conserved, and this destroys the direct correspondence between time and fictive time when the Poincar´e transformation is used. From (9.4) we can see that if an error $\Delta \tilde { H }$ is introduced in the Hamiltonian $\tilde { H }$ at some stage of numerical integration, then the true energy will satisfy

$$
\Delta H = \frac { \Delta \tilde { H } } { g } ,
$$

thus in situations where $g$ becomes very small (where the timesteps needed for integration are small), the true energy error can be large, and the equations (9.5)–(9.6) will differ significantly from the Sundman-transformed equations (9.2)–(9.3); hence the correspondence between time and fictive time will be destroyed at points where the computation is most difficult.

A second problem raised by the Poincar´e transformation has to do with the numerical implementation of the method. We know from earlier chapters that the available methods for integrating Hamiltonian systems with a nonseparable Hamiltonian are all implicit. Since (9.4) couples the positions and momenta, even when the original Hamiltonian $H$ is separable, the methods may not be practical for many applications. On the other hand, there are settings where such a symplectic approach may be reasonable: for example, if the original Hamiltonian is of low dimension or is given in a nonseparable form, or if certain combinations of numerical method and time transformation are employed. We will briefly return to discuss the symplectic approach later in this chapter.

# 9.2 Reversible variable stepsize integration

We now consider the application of reversible adaptive methods. Eventually, we will see that this approach allows for construction of efficient higher-order variable stepsize methods, and we will see how this reversible adaptive framework can be combined with more sophisticated methods such as those used to regularize fewbody close approaches in N-body gravitation.

Recall that a differential equation system

$$
\frac { d } { d t } z = { \pmb f } ( z ) , \qquad z \in \mathbb { R } ^ { d }
$$

is reversible with respect to a linear involution $s$ (a mapping of $\mathbb { R } ^ { d }$ with $S ^ { 2 } = I ^ { \cdot }$ ) if

$$
- S f ( S z ) = f ( z ) .
$$

In particular, a canonical Hamiltonian system is reversible with respect to $p  - p$ if $H ( \pmb { q } , - \pmb { p } ) = H ( \pmb { q } , \pmb { p } )$ . A system of differential equations

$$
\begin{array} { c } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \pmb F } ( { \pmb q } , { \pmb p } ) , } } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = { \pmb G } ( { \pmb q } , { \pmb p } ) } } \end{array}
$$

is reversible under the same involution if $F ( q , - p ) = - F ( q , p )$ , and $G ( q , - p ) =$ $G ( \pmb { q } , \pmb { p } )$ .

From the definition, it is easy to see that applying a Sundman transformation (9.1) with positive scaling $g$ and $g ( S z ) = g ( z )$ to a reversible system $\begin{array} { r } { \frac { d } { d t } z = \pmb { f } ( z ) } \end{array}$ will yield another reversible system. If we discretize the rescaled system

$$
\frac { d z } { d \tau } = g ( z ) f ( z )
$$

by some numerical method we obtain a discrete trajectory $\{ z ^ { n } \}$ , and each point on this trajectory will correspond to a point $\tau _ { n }$ in the rescaled time. Evidently, we must solve (9.1) along with the differential equations for the phase variables in order to resolve the temporal variable.

It remains to find a suitable discretization of the system (9.2)–(9.3). One approach, which is usually acceptable for low-dimensional problems, is just to apply the implicit midpoint method (or some other reversible integrator) to the rescaled equations. This has the advantage of simplicity and generality. We will illustrate this general approach to adaptive integration with a simple example: the soft impact oscillator with one degree-of-freedom Hamiltonian

$$
H ( q , p ) = \frac { p ^ { 2 } } { 2 } + \frac { 1 } { q ^ { 2 } } + \frac { k } { 2 } q ^ { 2 } .
$$

The orbits of this problem are periodic. A phase plane orbit (for $k = 0 . 1$ ) is shown below (Fig. 9.2), along with graphs of each coordinate against time. Note that the momenta must change very rapidly on a short time interval as the material point approaches the origin, and then gradually on the remainder of the period; this problem can benefit from some sort of adaptivity in the timestep.

![](images/d53d633fcdf4b392929cf674040e1775892c98d097306121ec8f547c274e4469.jpg)  
Figure 9.2 An orbit of the “impact-oscillator” for $k = 0 . 1$ . The figure to the left shows the motion in the phase plane; in the right, the positions and momenta are graphed against time. Note the sharp change in the momenta as $q$ approaches the origin.

We solve this system numerically for the following initial condition $q ( 0 ) = 2$ , $p ( 0 ) = - 4$ for $t \in [ 0 , 1 0 0 ]$ using the following three related second-order methods: (1) the trapezoidal rule (abbreviated “TR”), (2) an implementation of the trapezoidal rule with a third-order error estimate (TR23),2 and (3) Trapezoidal Rule applied to the rescaled equations

$$
\begin{array} { l } { { { \displaystyle \frac { d } { d t } q = g ( q ) p } , } } \\ { { { \displaystyle \frac { d } { d t } p = g ( q ) ( 2 q ^ { - 3 } - k q ) , } } } \end{array}
$$

2This solver is implemented in MATLAB 6 as ode23t and is specifically recommended for problems with little or no damping.

with the rescaling function

$$
g ( q ) = \frac { 1 } { 1 + q ^ { - 2 } }
$$

(abbreviated TRS).

![](images/eaeec3d92b4d793ce83ce95fe6839c533beb847e473f4e9e770e8f8763954c7c.jpg)  
Figure 9.3 Energy errors in simulations of the impact oscillator using the three variants of trapezoidal rule. In the upper figure the simulation timestep, tolerance, and fictive timestep were all tuned so that a total of 1000 timesteps were taken to cover the time interval [0, 100]. In the lower figure, 4000 timesteps were used.

The energy errors for representative simulations are shown in Fig. 9.3. In order to perform comparable experiments, we tuned the integration parameters (timestep, tolerance, or fictive timestep) so that all methods required the same number of trapezoidal rule steps to integrate to time 100. Observe that the energy of both the trapezoidal rule and the traditional variable stepsize methods fluctuate substantially, in the vicinity of the “collision.” On the other hand, the reversible variable stepsize method shows a stable, relatively mild energy variation with no secular drift. Comparing the upper and lower panels of Fig. 9.3, we see that the results are qualitatively similar regardless of the number of timesteps used in the simulation.

The mechanism which leads to the energy drift in TR23 becomes clearer when we look at the close-up of the energy in the vicinity of collision (Fig. 9.4).

![](images/b390cbe28986db15d9a55340b9b6aed5f9e6ece11d10c2ecd4f97cf35ba493b0.jpg)  
Figure 9.4 Close-up of the energy evolution in the vicinity of a collision. The TR and TRS schemes return to the pre-collisional value. By contrast, the TR23 method loses a substantial amount of energy during the collision.

For the TR and TRS methods, which are time reversible, the energy error graph can be seen to be geometrically symmetric around a vertical line through the time of collision. Because the energy is nearly exactly maintained far from the collision, the symmetry in energy implies that it must go back to the correct value as we leave the point of collision. By contrast, the TR23 method, which actually controls the local error in energy at the point of collision somewhat better than TRS, does not possess the symmetric energy behavior of the other methods. As a consequence, even on the relatively modest interval considered, the reversible variable stepsize method easily wins this competition, when compared on an efficiency basis (with efficiency measured by energy error per timestep); on longer time intervals or in larger problems, one can expect the results to be even more dramatic. The important symmetry property for the evolution of the energy error is not guaranteed to be present in all simulations. It can be shown to hold for two-body problems with central forces [109]. The benefits of the reversible adaptive framework are less apparent in the presence of interactions between three or more bodies. We will return to this issue in the section on Coulombic problems, below.

The choice of the time-rescaling function is critical to the success of the symmetric adaptive methods. We discuss this problem in the following and subsequent sections of this chapter.

# 9.2.1 Local error control as a time transformation

Given a symmetric one-step method $\psi _ { \Delta t }$ , an adaptive method can be generated by solving the equations

$$
\begin{array} { r l } & { z ^ { n + 1 } = \pmb { \psi } _ { \Delta t _ { n } } ( z ^ { n } ) , } \\ & { \quad \quad 0 = P ( \Delta t _ { n } , z ^ { n } , z ^ { n + 1 } ) . } \end{array}
$$

If the scalar function $P$ is symmetric with respect to transposition of its last two arguments, then the resulting method will be symmetric.

As suggested by STOFFER [179] (see also [83]) we can base $P$ on an estimate for the local error using various schemes, such as finite differences. In the case where the underlying method $\psi _ { \Delta t }$ is a symmetric Runge–Kutta or Partitioned Runge–Kutta method, a traditional embedded error estimate can be developed using the stages of the method; the only restriction is that the formula for the error estimate we use should be symmetric.

To illustrate, suppose we start with the trapezoidal rule,

$$
z ^ { n + 1 } = z ^ { n } + \frac { \Delta t } { 2 } \left[ \pmb { f } ( z ^ { n } ) + \pmb { f } ( z ^ { n + 1 } ) \right] .
$$

The local error in one step of Trapezoidal Rule is

$$
\mathbf { l e } = { \frac { \Delta t ^ { 3 } } { 1 2 } } { \frac { d ^ { 3 } } { d t ^ { 3 } } } z ( \xi ) .
$$

This error can be estimated in a variety of ways. We can also use the differential equation itself to define $\frac { d ^ { 3 } } { d t ^ { 3 } } z$ along the solution. In a one-dimensional case we would have

$$
{ \frac { d } { d t } } z = f \Rightarrow { \frac { d ^ { 2 } } { d t ^ { 2 } } } z = f ^ { \prime } f \Rightarrow { \frac { d ^ { 3 } } { d t ^ { 3 } } } z = f ^ { \prime \prime } f ^ { 2 } + f ^ { \prime 2 } f
$$

(or in higher dimensions, a more complicated version of this formula). The local error in the nth step of trapezoidal rule can then be approximated by

$$
I e \approx \frac { \Delta t ^ { 3 } } { 1 2 } ( f ^ { \prime \prime } f ^ { 2 } + f ^ { \prime 2 } f ) .
$$

Setting the magnitude of this estimate to a prescribed tolerance tol yields

$$
\Delta t = \left[ \frac { 1 2 \mathrm { t o l } } { | f ^ { \prime \prime } f ^ { 2 } + f ^ { \prime 2 } f | } \right] ^ { 1 / 3 } .
$$

Note that the stepsize has been written as a function of tol and the solution itself. We could, for example, evaluate the estimate at $z ^ { n + 1 / 2 } = ( z ^ { n } + z ^ { n + 1 } ) / 2$ , then introduce the expression for $\Delta t$ directly into (9.7), the result being a secondorder implicit adaptive integrator. The parameter tol acts in the usual way to allow a refinement of the approximate solution. In practice we would need to modify the stepsize formula to avoid singularities and to ensure the smoothness of the timestep map.

Alternatively, if we define $\Delta \tau = \ t \circ 1 ^ { 1 / 3 }$ , we see that we are simply solving a certain Sundman rescaling of the original problem, so that any of the schemes mentioned in this chapter could be used. This example is a special case of a more general observation that symmetric methods based on error estimates can be viewed as reversible discretizations of a Sundman-transformed problem (see [179]).

Controlling local error makes sense if the goal of computation is a numerical solution with a small trajectory error, but this is not necessarily the situation we confront when using a geometric integrator. On the other hand, there are likely to be situations where some combination of various types of stepsize controls, including one based on local error, should be used in simulation.

In the following subsections, we consider the construction of efficient methods for implementing reversible variable stepsize based on time reparameterization. The schemes described above are implicit. In the sequel we show how semi-explicit and even fully explicit methods can be developed.

# 9.2.2 Semi-explicit methods based on generalized leapfrog

We consider a reparameterization of a separable Hamiltonian system

$$
\begin{array} { l } { { \displaystyle { \frac { d { \pmb q } } { d \tau } } = g ( { \pmb q } , { \pmb p } ) { \pmb M } ^ { - 1 } { \pmb p } } , } \\ { { \displaystyle { \frac { d { \pmb p } } { d \tau } } = - g ( { \pmb q } , { \pmb p } ) \nabla _ { { \pmb q } } V ( { \pmb q } ) . } } \end{array}
$$

The system is not solvable by the standard Verlet method.

On the other hand, if we apply the generalized leapfrog method, we obtain the following system

$$
\begin{array} { l } { { \displaystyle { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \frac { \Delta \tau } { 2 } ( g ( { \pmb q } ^ { n } , { \pmb p } ^ { n + \frac { 1 } { 2 } } ) + g ( { \pmb q } ^ { n + 1 } , { \pmb p } ^ { n + \frac { 1 } { 2 } } ) ) { \pmb M } ^ { - 1 } { \pmb p } ^ { n + \frac { 1 } { 2 } } , } } \\ { { \displaystyle { \pmb p } ^ { n + \frac { 1 } { 2 } } = { \pmb p } ^ { n } - \frac { \Delta \tau } { 2 } g ( { \pmb q } ^ { n } , { \pmb p } ^ { n + \frac { 1 } { 2 } } ) \nabla _ { \pmb q } V ( { \pmb q } ^ { n } ) } , } \\ { { \displaystyle { \pmb p } ^ { n + 1 } = { \pmb p } ^ { n + \frac { 1 } { 2 } } - \frac { \Delta \tau } { 2 } g ( { \pmb q } ^ { n + 1 } , { \pmb p } ^ { n + \frac { 1 } { 2 } } ) \nabla _ { \pmb q } V ( { \pmb q } ^ { n + 1 } ) } . } \end{array}
$$

The equations (9.10)–(9.12) are implicit, requiring the solution of a nonlinear system at each step, but the fact that $g$ is scalar means that a relatively efficient Newton solver based on rank-one updates is possible, as pointed out in [89]. Moreover, in case $g$ is a function only of $\pmb q$ (or $p$ ) the scheme actually becomes semi-explicit, in the sense that the timestepping can be performed with only one force evaluation per timestep. Specifically, if $g = g ( \pmb q )$ , then (9.11) gives $p ^ { n + \frac { 1 } { 2 } }$ explicitly. If we evaluate $g$ on both sides of (9.10) and set $\gamma ^ { n + 1 } = g ( { \pmb q } ^ { n + 1 } )$ , then we arrive at

$$
\gamma ^ { n + 1 } = g ( \pmb { q } ^ { n } + \frac { \Delta \tau } { 2 } ( \gamma ^ { n } + \gamma ^ { n + 1 } ) M ^ { - 1 } \pmb { p } _ { n + \frac { 1 } { 2 } } ) ,
$$

but since $p ^ { n + 1 / 2 }$ is now known, this is just a scalar nonlinear equation for $\gamma ^ { n + 1 }$ , readily solvable by Newton iteration. This scheme will be efficient provided the evaluation of $g$ and its gradient are inexpensive. For example if the system involves long-ranged forces, but the time reparameterization is short-ranged – a typical case – then the per timestep cost of incorporating adaptivity in this way will be neglible.

# 9.2.3 Differentiating the control

We next describe an approach based on introducing the stepsize control as a new variable along with its own differential equation. After discretization, this results in an algorithm requiring evaluation of the Hessian of the potential energy function, or rather its products with certain vectors. Differentiating $\gamma = g ( \pmb { q } , \pmb { p } )$ with respect to the reparameterized time $\tau$ yields

$$
\begin{array} { l } { \displaystyle \frac { d } { d \tau } \gamma = ( \nabla _ { q } g ( q , p ) ) ^ { T } \frac { d } { d \tau } q + ( \nabla _ { p } g ( q , p ) ) ^ { T } \frac { d } { d \tau } p } \\ { \displaystyle \quad = g ( q , p ) \left[ ( \nabla _ { q } g ( q , p ) ) ^ { T } M ^ { - 1 } p - ( \nabla _ { p } g ( q , p ) ) ^ { T } \nabla _ { q } V ( q ) \right] . } \end{array}
$$

We then look for a discretization for the coupled system in $\left( \pmb q , \pmb { p } , \gamma \right)$ . We will illustrate for the choice

$$
\begin{array} { r } { g ( \pmb { q } , \pmb { p } ) = ( \pmb { p } ^ { T } \pmb { M } ^ { - 2 } \pmb { p } + \| \nabla _ { \pmb { q } } V ( \pmb { q } ) \| ^ { 2 } ) ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

Since $\nabla _ { p } g ( q , p ) = - g ( q , p ) ^ { - 3 } M ^ { - 2 } p$ and $\nabla _ { q } g ( q , p ) = - g ( q , p ) ^ { - 3 } V _ { q q } ( q )$ $\nabla _ { q } V ( q )$ ,

$$
\frac { d } { d \tau } \gamma = \frac { p ^ { T } M ^ { - 1 } V _ { q q } ( q ) \nabla _ { q } V ( q ) - p ^ { T } M ^ { - 2 } \nabla _ { q } V ( q ) } { g ( q , p ) ^ { 2 } } = : G ( q , p ) .
$$

Next, we partition the variables as $\pmb q$ and $( p , \gamma )$ and discretize using the generalized leapfrog

$$
\begin{array} { l } { { \pmb q ^ { n + 1 } = { \pmb q } ^ { n } + \Delta \tau g ^ { n + \frac { 1 } { 2 } } { \pmb M } ^ { - 1 } { \pmb p } ^ { n + \frac { 1 } { 2 } } , } } \\ { { \gamma ^ { n + \frac { 1 } { 2 } } = \gamma ^ { n } + \displaystyle \frac { \Delta \tau } { 2 } G ( { \pmb q } ^ { n } , { \pmb p } ^ { n + \frac { 1 } { 2 } } ) , } } \\ { { \pmb p ^ { n + \frac { 1 } { 2 } } = { \pmb p } ^ { n } - \displaystyle \frac { \Delta \tau } { 2 } g ^ { n + \frac { 1 } { 2 } } \nabla _ { \pmb q } V ( { \pmb q } ^ { n } ) , } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \gamma ^ { n + 1 } = \gamma ^ { n + 1 / 2 } + \frac { \Delta \tau } { 2 } G ( q ^ { n + 1 } , p ^ { n + \frac { 1 } { 2 } } ) , } } \\ { { \displaystyle p ^ { n + 1 } = p ^ { n + 1 / 2 } - \frac { \Delta \tau } { 2 } g ^ { n + \frac { 1 } { 2 } } \nabla _ { q } V ( q ^ { n + 1 } ) , } } \\ { { \displaystyle t _ { n + 1 } = t _ { n } + \Delta \tau \gamma ^ { n + \frac { 1 } { 2 } } . } } \end{array}
$$

It can be shown that these equations reduce to solving a cubic polynomial for $\gamma ^ { n + 1 / 2 }$ , after which all steps are explicit. For details see [89], which also includes numerical experiments with the method. This scheme works well in practice. For the application of this idea in the context of gravitational dynamics, see [134].

Note that, for $N -$ -body systems, efficient schemes are typically available which allow the rapid computation of matrix–vector products involving the Hessian matrix in tandem with the force evaluation [118].

# 9.2.4 The Adaptive Verlet method

We now describe a reversible adaptive timestepping scheme which admits both semi-explicit and fully explicit variants. The idea is to write the Sundmantransformed equations of motion for a Newtonian mechanical system as a constrained differential equation system, in the form

$$
\begin{array} { c } { { \displaystyle \frac { d } { d \tau } \pmb { q } = \gamma \pmb { M } ^ { - 1 } \pmb { p } , } } \\ { { \displaystyle \frac { d } { d \tau } \pmb { p } = \gamma \nabla _ { q } V ( \pmb { q } ) , } } \\ { { \gamma = g ( \pmb { q } , \pmb { p } ) . } } \end{array}
$$

This approach broadens the possibilities for methods, since we may now evaluate $g$ at different points than the vector field. A broad class of second-order symmetric methods can be written in the form

$$
\begin{array} { l } { { q ^ { n + 1 / 2 } = q ^ { n } + \displaystyle \frac { 1 } { 2 } \Delta t \gamma ^ { n } M ^ { - 1 } p ^ { n + 1 / 2 } , } } \\ { { \displaystyle p ^ { n + 1 / 2 } = p ^ { n } + \displaystyle \frac { 1 } { 2 } \Delta t \gamma ^ { n } \nabla q V ( q ^ { n } ) , } } \\ { { \displaystyle \quad 0 = R ( q ^ { n } , q ^ { n + 1 } , q ^ { n + 1 / 2 } , p ^ { n } , p ^ { n + 1 } , p ^ { n + 1 / 2 } , \gamma ^ { n } , \gamma ^ { n + 1 } ) , } } \\ { { \displaystyle q ^ { n + 1 } = q ^ { n + 1 / 2 } + \displaystyle \frac { 1 } { 2 } \Delta t \gamma ^ { n + 1 } M ^ { - 1 } p ^ { n + 1 / 2 } , } } \\ { { \displaystyle p ^ { n + 1 } = p ^ { n + 1 / 2 } + \displaystyle \frac { 1 } { 2 } \Delta t \gamma ^ { n + 1 } \nabla q V ( q ^ { n + 1 } ) . } } \end{array}
$$

Here $R$ is a smooth function depending on $g ( \pmb { q } , \pmb { p } )$ , invariant under $q ^ { n } \to { \pmb q } ^ { n + 1 }$ , $p ^ { n } \to p ^ { n + 1 }$ , $\gamma ^ { n } \to \gamma ^ { n + 1 }$ , and approximating to second-order accuracy the equation $\gamma = g ( \pmb { q } , \pmb { p } )$ . Note that the method has the form of two separate Verlet half steps with a stepsize adjustment in between, but in some cases the stepsize adjustment could make the whole calculation fully implicit. These schemes are referred to collectively as the Adaptive Verlet method. The simplest explicit scheme of this type is defined by

$$
\gamma ^ { n } + \gamma ^ { n + 1 } = 2 g ( { \pmb q } ^ { n + 1 / 2 } , { \pmb p } ^ { n + 1 / 2 } ) .
$$

An alternative method, originally suggested by HUANG $\&$ LEIMKUHLER in [89], is defined by

$$
\frac { 1 } { \gamma ^ { n + 1 } } + \frac { 1 } { \gamma ^ { n } } = \frac { 1 } { g ( \pmb { q } ^ { n + 1 / 2 } , \pmb { p } ^ { n } ) } + \frac { 1 } { g ( \pmb { q } ^ { n + 1 / 2 } , \pmb { p } ^ { n + 1 } ) } .
$$

When cost is measured in terms of function evaluations, the Adaptive Verlet method is usually much more efficient than the implicit schemes mentioned earlier. For example, when compared against the symmetric adaptive trapezoidal rule discretization (TRS in the previous section), applied to the same impact oscillator problem and with the same rescaling function, the Adaptive Verlet method requires about a quarter of the work required for the implicit scheme to compute solutions with the same accuracy. These considerations are likely to be ampified for larger systems.

# 9.3 Sundman transformations

Reversible variable stepsize methods require the specification of an auxiliary timereparameterization function $g ( \pmb { q } , \pmb { p } )$ . It is possible to choose this rescaling function based on a functional of the vector field; in this case the method becomes more or less problem independent, since the computations performed for varying stepsizes can be fully automated.

# 9.3.1 Arclength parameterization

In some sense the most natural rescaling is one which is provided by the vector field itself. Recall that the arclength $s$ of a parameterized solution curve in the interval $\left[ { { t _ { 0 } } , { t _ { 0 } } + \Delta { t } } \right]$ is

$$
s ( \Delta t ) = \int _ { t _ { 0 } } ^ { t _ { 0 } + \Delta t } \lVert \frac { d } { d t } z ( t ) \rVert d t .
$$

If we introduce a Sundman transformation of the form

$$
\frac { d t } { d \tau } = \frac { 1 } { \lVert \frac { d } { d t } z \rVert } ,
$$

the arclength along solution curves is normalized to the fictive timestep. We term this method “arclength reparameterization.” Note that the Sundman transformation can be expressed as a function of the phase variables only by using the differential equations

$$
{ \frac { d t } { d \tau } } = { \frac { 1 } { \| f ( z ) \| } } .
$$

It is entirely possible that the vector field will vanish at a point on a solution curve, in which case the arclength reparameterization becomes singular. This can be corrected by introducing a regularizing parameter as discussed below in Section 9.3.3. Arclength reparameterization has the virtue of simplicity, but it is not usually the optimal choice on an efficiency basis.

# 9.3.2 Rescaling for the N-body problem

A particularly important application for variable stepsize methods arises in the simulation of Coulombic systems, including both gravitational dynamics and classical atomic models [19, 108]. In N-body systems, it is natural to choose the rescaling function as a homogeneous function of the distances. Here we show how a time transformation for two-body gravitational interactions can be naturally constructed as a consequence of a scaling symmetry, based on the treatment in [36]. This transformation is useful in Coulombic N-body applications.

Recall that the Kepler Hamiltonian is

$$
H ( \pmb { q } , \pmb { p } ) = \frac { 1 } { 2 } \| \pmb { p } \| ^ { 2 } - \frac { 1 } { \| \pmb { q } \| } ,
$$

with equations of motion

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } q = p , } } \\ { { \displaystyle { \frac { d } { d t } } p = - { \frac { q } { \| q \| ^ { 3 } } } . } } \end{array}
$$

The system possesses angular momentum and energy as first integrals. (The existence of an additional first integral, the so-called Runge–Lenz vector, places the Kepler problem in the class of “super-integrable systems,” a consequence of which is the existence of closed periodic orbits for a wide range of initial data.) Indeed, the Kepler problem admits three types of orbits expressed in terms of the projection of the phase variables on to the position plane, based on the value of the energy: (i) a closed ellipse for $H < 0$ , (ii) a parabola for $H = 0$ , (iii) a hyperbola for $H > 0$ .

The Kepler problem possesses an important scaling symmetry. If we rescale the variables $t , \pmb { q }$ , and $\pmb { p }$ as follows

$$
t = \alpha \tilde { t } , \qquad q = \alpha ^ { 2 / 3 } \tilde { q } , \qquad p = \alpha ^ { - 1 / 3 } \tilde { p } ,
$$

then we find that the form of the system of equations (9.23)–(9.24) expressed in these new variables is the same as the original. This scaling symmetry reflects a natural invariance of physical systems with respect to changes of units.

Now consider a Sundman transformation of the form

$$
\frac { d t } { d \tau } = \| \pmb { q } \| ^ { 3 / 2 } ,
$$

which changes the Kepler equations to

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d \tau } } \pmb { q } = \| \pmb { q } \| ^ { 3 / 2 } \pmb { p } } , } \\ { { \displaystyle { \frac { d } { d \tau } } \pmb { p } = - \| \pmb { q } \| ^ { - 3 / 2 } \pmb { q } } . } \end{array}
$$

Observe that the scaling symmetry for this new system becomes

$$
\tau = \tilde { \tau } , \qquad E = \tilde { E } , \qquad q = \alpha ^ { 2 / 3 } \tilde { q } , \qquad p = \alpha ^ { - 1 / 3 } \tilde { p } .
$$

The time variable has been made invariant under the action of the scaling symmetry. This choice of Sundman transformation has additional consequences. For example, it can be shown that with this choice, the collision event occurs in approximately the same fictive time regardless of the energy of the colliding particle [24, 109]. This choice is also found to be approximately optimal in numerical experiments.

# 9.3.3 Stepsize bounds

Regardless of which stepsize controls are used, it is usually necessary to modify the control to limit the stepsize to some range of values. Let us define $\Delta t _ { \mathrm { m i n } }$ and $\Delta t _ { \mathrm { m a x } }$ as minimum and maximum stepsizes, respectively. Let $g$ be a given a stepsize control, such as one of those discussed above. Since the effective stepsize is $g \Delta \tau$ , and $\Delta \tau$ is known and fixed at the start of simulation, the problem is just to define a monotonic function $g  \hat { g } = \phi ( g )$ , so that the interval $\lbrack 0 , \infty )$ is remapped to $[ a , b ]$ , where $a = \Delta t _ { \operatorname* { m i n } } / \Delta \tau$ , and $b = \Delta t _ { \mathrm { m a x } } / \Delta \tau$ . This is easily accomplished. For example, let

$$
\hat { g } = b \frac { g + a } { g + b } .
$$

Alternative remappings are possible, but this simple heuristic works in most cases. Note that in Adaptive Verlet, stepsizes are allowed to oscillate slightly around the target value, so these are only approximate bounds on the actual stepsize that would be observed in simulation.

# 9.4 Backward error analysis

A criticism that may be made of time-reversible adaptive methods such as Adaptive Verlet is this: since the method does not define a symplectic map, we lose the powerful Hamiltonian backward error analysis (as considered in Chapter 5). However, it turns out that a meaningful backward error analysis is possible for time-reversible systems. Indeed, a theory of backward error analysis and preservation of approximate first integrals for reversible integrable systems has been developed without any recourse to the Hamiltonian structure (see the text [80] for a summary of the main results).

The idea first followed by HAIRER AND STOFFER [83] is to start with a perturbation series for the numerical flow, defining a sequence of interpolating vector fields $\tilde { { f } } _ { k } ( z ; \Delta t ) , k = 0 , 1 , . . . ,$ which constitute approximate modified equations of a given order, and then to show that if the numerical method is reversible under involution $s$ , then the perturbed vector fields $\tilde { f } _ { k } \big ( \boldsymbol { z } ; \Delta t \big )$ satisfy the reversibility condition

$$
- S \tilde { f } _ { k } ( S z ) = \tilde { f } _ { k } ( z ) .
$$

In this way we can view the numerical solution obtained from time-reversible discretization as approximately determined from the evolution of a reversible continuous dynamical system as already mentioned in Chapter 5.

As for symplectic methods, there are some limitations to this type of backward error analysis. First, one finds that the theory only guarantees in general that the best truncation of the modified equations accurately determines the numerical solution on an interval of length $\mathcal { O } ( \Delta t ^ { - 1 } )$ . Work is in progress to try to determine estimates that would hold on much longer intervals (for example, $\mathcal { O } ( e ^ { c / \Delta t } ) )$ ), but the current efforts require that the system be close to integrable. At the time of this writing, it is not clear how this theory will develop. In many applications, particularly in large scale systems with chaotic solutions, the idea is often to use very large timesteps (just small enough to guarantee stability of the method) so that the accessible timescale is as large as possible, but in these cases there are serious questions concerning the practical relevance of backward error analysis. Nonetheless, backward error analysis is certainly valid for some types of simulations and its usefulness is likely only to increase as theoretical work continues on this topic.

We will restrict this discussion to the case of the Adaptive Verlet method, which is the most commonly used scheme. A backward error analysis of the Adaptive Verlet method is given in [45]. The method can be formally written as

$$
\begin{array} { r } { \pmb q ^ { n } = \tilde { \pmb q } ( \tau _ { n } ) + ( - 1 ) ^ { n } \hat { \pmb q } ( \tau _ { n } ) , } \\ { \pmb p ^ { n } = \tilde { \pmb p } ( \tau _ { n } ) + ( - 1 ) ^ { n } \hat { \pmb p } ( \tau _ { n } ) , } \end{array}
$$

$$
\gamma ^ { n } = \tilde { \gamma } ( \tau _ { n } ) + ( - 1 ) ^ { n } \hat { \gamma } ( \tau _ { n } ) ,
$$

where $\tau _ { n } = n \Delta \tau$ and the modified equations are

$$
\begin{array} { r l } & { \tilde { \pmb q } ^ { \prime } = \tilde { g } \pmb { M } ^ { - 1 } \tilde { \pmb p } + \Delta \tau ^ { 2 } \tilde { \pmb Q } _ { 2 } ( . ) + \cdot \cdot \cdot , \qquad \hat { \pmb q } = \Delta \tau ^ { 2 } \hat { \pmb Q } _ { 2 } ( . ) + \cdot \cdot \cdot , } \\ & { \tilde { \pmb p } ^ { \prime } = \tilde { g } \pmb { F } ( \tilde { \pmb q } ) + \Delta \tau ^ { 2 } \tilde { \pmb P } _ { 2 } ( . ) + \cdot \cdot \cdot , \qquad \hat { \pmb p } = \Delta \tau ^ { 2 } \hat { \pmb P } _ { 2 } ( . ) + \cdot \cdot \cdot , } \\ & { \tilde { \gamma } = \pmb { G } ( \tilde { \pmb q } , \tilde { \pmb p } ) + \Delta \tau ^ { 2 } \tilde { G } _ { 2 } ( . ) + \cdot \cdot \cdot , \qquad \hat { \gamma } ^ { \prime } = \hat { G } ( . ) + \Delta \tau ^ { 2 } \hat { G } _ { 2 } ( . ) + \cdot \cdot \cdot , } \end{array}
$$

with uniquely determined initial values satisfying

$$
\begin{array} { r } { q _ { 0 } = \tilde { q } ( 0 ) + \hat { q } ( 0 ) , \quad p _ { 0 } = \tilde { p } ( 0 ) + \hat { p } ( 0 ) , \quad \gamma _ { 0 } = \tilde { \gamma } ( 0 ) + \hat { \gamma } ( 0 ) . } \end{array}
$$

All of the expansions are formal and in even powers of $\Delta \tau$ . The functions in the above equations depend only on $\tilde { \pmb q } , \tilde { \pmb p }$ and $\hat { \boldsymbol { \gamma } }$ ; importantly the formulas for $\hat { G } , \hat { G } _ { 2 }$ , $Q _ { 2 } , P _ { 2 }$ all contain $\hat { \boldsymbol { \gamma } }$ as a factor. In addition it can be shown that $\hat { \gamma } = O ( \Delta \tau ^ { 2 } )$ and this, with the above equations, gives $\hat { \pmb q } = O ( \Delta \tau ^ { 4 } ) , \hat { \pmb p } = O ( \Delta \tau ^ { 4 } )$ .

An instability can arise when the oscillating terms in the expansion for $\gamma _ { n }$ grow with time. The leading oscillatory term is of the form

$$
\hat { \gamma } _ { 2 } = \hat { g } _ { 2 } ( \tau _ { n } ) \Delta \tau ^ { 2 } .
$$

The presence of this artificial dynamic is the price we pay for a fully explicit scheme. In many applications, these wobbles are essentially invisible, but in certain applications, for example Coulombic problems, the oscillation may grow quite large at the most difficult points along the trajectory (points of close approach of two bodies). (In extreme cases, the oscillations can make the stepsize become negative, leading to a complete breakdown of the integrator.)

In general, the behaviour of $\hat { g } _ { 2 }$ depends on the stepsize update formula and the differential equations, in a complicated way. For the important special case where $\hat { g } _ { 2 }$ is a function of $\pmb q$ only, it can be shown that for the stepsize update (9.19), we have, as we approach the collision,

$$
\hat { g } _ { 2 } ( \tau ) \sim K _ { 1 } / \gamma ,
$$

while for the choice (9.20), the operative formula is

$$
\hat { g } _ { 2 } ( \tau ) \sim K _ { 2 } \gamma .
$$

Neither of these will present a significant problem in the case where the stepsize variation is moderate, but in applications such as gravitation, for which $\gamma \to 0$ i n the vicinity of close approach, the stepsize formula (9.20) gives far better results than the other choice.

In practice, (9.20) is generally the safer choice, for the magnitude of $\gamma$ would typically be inhibited in the design of the scaling function (see below), whereas its reciprocal would generally be allowed to grow substantially at difficult points on the trajectory. A scheme for eliminating wobble in Adaptive Verlet to leading order was also given in [45].

# 9.5 Generalized reversible adaptive methods

As discussed in [86] it is possible to generalize the variable stepsize apparatus to allow reversible adaptive integration of systems admitting a general linear reversing symmetry. Such methods can be constructed starting from the assumption of a certain base discretization method (not necessarily symmetric) $\psi _ { \Delta t }$ , together with its adjoint method $\psi _ { \Delta { t } } ^ { * }$ . Recall from Chapter 4 that we can construct a symmetric method by concatenation

$$
\tilde { \pmb { { \psi } } } _ { \Delta t } = \pmb { { \psi } } _ { \frac { 1 } { 2 } \Delta t } ^ { * } \pmb { { \psi } } _ { \frac { 1 } { 2 } \Delta t } .
$$

A reversible variable stepsize method can also be constructed based on $\psi _ { \Delta t }$

$$
\begin{array} { r l } & { \qquad z ^ { n + 1 / 2 } = \pmb { \psi } _ { \frac { 1 } { 2 } \gamma ^ { n } \Delta \tau } ( z ^ { n } ) , } \\ & { \qquad \gamma ^ { n } + \gamma ^ { n + 1 } = 2 g ( z ^ { n + 1 / 2 } ) , } \\ & { \qquad z ^ { n + 1 } = \pmb { \psi } _ { \frac { 1 } { 2 } \gamma ^ { n + 1 } \Delta \tau } ^ { * } ( z ^ { n + 1 / 2 } ) . } \end{array}
$$

Clearly this method maps $\left( z ^ { n } , \gamma ^ { n } \right) )$ to $( z ^ { n + 1 } , \gamma ^ { n + 1 } )$ . It is easy to compute the inverse of the associated map and to check the reversibility condition (with respect to the involution $\tau \to - \tau , z \to S z , \gamma \to \gamma$ . Because of symmetry, the method is of even order. The scheme is evidently convergent (since it is based on two applications of a convergent method), so it must be second order.

If we identify $\Delta t ^ { n }$ with $\gamma ^ { n } \Delta \tau$ , we could eliminate the variable $\gamma ^ { n }$ and write the method in a more compact form. As we will shortly see, it turns out that it is also necessary in many cases to consider a different choice of the symmetric update for the time-rescaling parameter. In general we term this class of methods symmetric adaptive composition schemes:

# SYMMETRIC ADAPTIVE COMPOSITION

Given $\psi _ { \Delta t }$ , a convergent integrator for $\begin{array} { r l r } { \frac { d } { d t } z } & { { } = } & { { \bf f } ( z ) } \end{array}$ , and $R ( t _ { 0 } , t _ { 1 } , z _ { 0 } , \bar { z } , z _ { 1 } , \tau )$ a function satisfying $R ( t _ { 0 } , t _ { 1 } , z _ { 0 } , \bar { z } , z _ { 1 } , \tau ) \equiv$ $R \big ( t _ { 1 } , t _ { 0 } , z _ { 1 } , \bar { z } , z _ { 0 } , \tau \big )$ , $\begin{array} { l l l } { \frac { \partial R } { \partial t _ { 1 } } } & { \neq } & { 0 } \end{array}$ , The following equations define a reversible method

$$
\begin{array} { r l } & { z ^ { n + 1 / 2 } = \pmb { \psi } _ { \frac { 1 } { 2 } \Delta t _ { n } } \big ( z ^ { n } \big ) , } \\ & { \qquad 0 = R ( \Delta t _ { n } , \Delta t _ { n + 1 } , z ^ { n } , z ^ { n + 1 / 2 } , z ^ { n + 1 } , \Delta \tau ) , } \\ & { z ^ { n + 1 } = \pmb { \psi } _ { \frac { 1 } { 2 } \Delta t _ { n + 1 } } ^ { * } \big ( z ^ { n + 1 / 2 } \big ) . } \end{array}
$$

This method reduces to Adaptive Verlet in case the base method is a symplectic Euler.

# 9.5.1 Switching

The idea of the variable stepsize method can be generalized to provide a tool for developing reversible methods with more complicated algorithmic features, such as variable order of accuracy or even adaptive replacement of one integrator by another. The idea of the Adaptive Verlet scheme is roughly this: we apply a given standard integrator with a particular stepsize, modify the stepsize in a symmetric way, then apply the adjoint of the integrator using the new stepsize. A similar idea can be used to modify the features of the method that is used or to allow additional forms of adaptivity in the numerical solution.

Consider the following problem. We have a vector field $\pmb { f }$ , and two integrators $\hat { \pmb { { \psi } } } _ { \Delta t } ^ { ( 1 ) }$ and $\hat { \pmb { { \psi } } } _ { \Delta t } ^ { ( 2 ) }$ preserving some given geometric structure associated to $\boldsymbol { f }$ . Suppose further that we have an indicator (monitor) function $M ( z )$ which quantifies some aspect of the solution, say the difficulty of computing it, or simply the usefulness of one of the two techniques compared with the other. We wish to develop a new integrator with the following properties:

1. It should automatically switch between $\hat { \pmb { \psi } } _ { \Delta t } ^ { ( 1 ) }$ an d Ψˆ(2) so that when $M ( z ) <$ $\beta$ , say, we integrate with the first method, while when $M ( z ) > \beta$ we use the second method, and   
2. It should be smooth and preserve the same geometric structures as each of the two maps.

The idea is to introduce a smooth switching function, $\sigma ( m )$ (sometimes called a sigmoidal function) on an interval containing $\beta$ , smoothly passing from 1 to 0. Shifted scaled arctangent functions can be used for this purpose, but it is generally better for efficiency purposes to use a piecewise polynomial switch defined on a compact interval $[ m _ { - } , m _ { + } ]$ containing $\beta$ . It is easy to construct a polynomial $\sigma$ , with zero derivatives at $m _ { - }$ and $m _ { + }$ of any desired degree, with the properties: $\sigma ( m _ { - } ) = 1$ , $\sigma ( m _ { + } ) = 0$ , $\sigma$ monotone decreasing on $[ m _ { - } , m _ { + } ]$ .

Now we construct a splitting of $\boldsymbol { f }$

$$
\begin{array} { r } { f = f _ { 1 } + f _ { 2 } , \qquad f _ { 1 } ( z ) = \sigma ( M ( z ) ) f ( z ) , \qquad f _ { 2 } ( z ) = ( 1 - \sigma ( M ( z ) ) ) f ( z ) , } \end{array}
$$

and recover the solution by iterating for example the following concatenation of maps: Ψˆ∆t = Ψˆ(1) $\hat { \pmb { { \psi } } } _ { \Delta t } = \hat { \pmb { { \psi } } } _ { \sigma ( M ( z ) ) \Delta t } ^ { ( 1 ) } \circ \hat { \pmb { { \psi } } } _ { ( 1 - \sigma ( M ( z ) ) ) \Delta t } ^ { ( 2 ) }$ Ψˆ(2)(1 σ(M(z)))∆t . When M(z) < m−, the switch σ will be fully “on” (value 1), so that the effect will be to apply method $\hat { \pmb { \psi } } _ { \Delta t } ^ { ( 1 ) }$ to $\pmb { f }$ . When $M ( z ) > m _ { + }$ , the switch $\sigma$ will be fully “off” (value 0), so that the the numerical solution will be propagated by applying method Ψˆ(2)∆t to $\boldsymbol { f }$ . Between $m _ { - }$ and $m _ { + }$ , both methods contribute to the numerical solution, by solving in each case some polynomially rescaled version of the original vector field. In other words, what we have done is to construct a homotopy of the two numerical integration maps Ψˆ(1) and Ψˆ(2) .

The challenge is to implement, in an efficient manner, schemes based on this idea. In general, we cannot expect the structure $\sigma ( M ( z ) ) f$ to match the structure of $\pmb { f }$ , for example.

One symmetric method that could be used in the general case is as follows

$$
\begin{array} { r l } & { z ^ { n + 1 / 2 } = \hat { \pmb { \psi } } _ { ( 1 - \sigma ( M ( z ^ { n + 1 / 2 } ) ) ) \Delta t / 2 } ^ { ( 2 ) } \circ \hat { \pmb { \psi } } _ { \sigma ( M ( z ^ { n } ) ) \Delta t / 2 } ^ { ( 1 ) } ( z ^ { n } ) , } \\ & { \quad z ^ { n + 1 } = \hat { \pmb { \psi } } _ { \sigma ( M ( z ^ { n + 1 } ) ) \Delta t / 2 } ^ { ( 1 ) * } \circ \hat { \pmb { \psi } } _ { ( 1 - \sigma ( M ( z ^ { n + 1 / 2 } ) ) ) \Delta t / 2 } ^ { ( 2 ) * } ( z ^ { n + 1 / 2 } ) . } \end{array}
$$

The notation $\hat { \pmb { { \psi } } } _ { \Delta t } ^ { * }$ indicates the adjoint map of $\hat { \pmb { { \psi } } } _ { \Delta t }$ , defined by $\hat { \pmb { { \psi } } } _ { \Delta t } ^ { * } = \hat { \pmb { { \psi } } } _ { - \Delta t } ^ { - 1 }$ . The reversible switching integrator is symmetric. It is also second order. It switches the integrators completely. Its major drawback is that it is implicit, even if the two methods on which it is based are explicit.

Based on our experience with adaptive timestepping, the most natural approach to explicit schemes is to introduce a discrete variable $\sigma _ { n }$ which can be udpated according to a symmetric formula. However, such methods tend to introduce a small oscillatory component in the error in $\sigma$ ; since $\sigma$ is zero in a substantial part of the domain, the numerical errors will tend to introduce an instability in the method. An explicit alternative is likely to be more successful if we change our perspective so that we switch based on the value of $M ( z )$ rather than based on $\sigma$ . Specifically, we could introduce a discrete monitor variable $\mu _ { n }$ and employ an explicit scheme of the following sort

$$
\begin{array} { r l } & { \qquad z ^ { n + 1 / 2 } = \hat { \pmb { \psi } } _ { ( 1 - \sigma ( \mu _ { n } ) ) \Delta t / 2 } ^ { ( 2 ) } \circ \hat { \pmb { \psi } } _ { \sigma ( \mu _ { n } ) ) \Delta t / 2 } ^ { ( 1 ) } ( z ^ { n } ) , } \\ & { \qquad \mu _ { n + 1 } + \mu _ { n } = M ( z ^ { n + 1 / 2 } ) , } \\ & { \qquad z ^ { n + 1 } = \hat { \pmb { \psi } } _ { \sigma ( \mu _ { n + 1 } ) ) \Delta t / 2 } ^ { ( 1 ) * } \circ \hat { \pmb { \psi } } _ { ( 1 - \sigma ( \mu _ { n + 1 } ) ) \Delta t / 2 } ^ { ( 2 ) * } ( z ^ { n + 1 / 2 } ) . } \end{array}
$$

If each of the two schemes involved is explicit with explicit adjoint, then the overall method is also explicit. The indicator function $M$ should be designed so that $M ( z )$ is bounded well away from zero, to avoid the possibility of $\mu$ becoming negative during the integration.

In practice, we expect that adaptivity must be introduced in a problem-specific way. For a detailed discussion of switching in the context of few body Coulombic systems, see [101].

# 9.6 Poincar´e transformations

In this section, we briefly discuss the implementation of Poincar´e transformations for symplectic variable stepsize integration. Recall that there are many explicit symplectic integrators for Hamiltonian systems in separated form, $H ( { \pmb q } , { \pmb p } ) =$ $T ( p ) + V ( q )$ , but all known symplectic integrators which work for general $H$ are implicit. In general, the Poincar´e-transformed equations will require treatment with an implicit method, since the transformation couples the position and momenta variables.

Experience with reversible and symplectic methods in a variety of applications suggest that symplectic schemes often exhibit improved stability compared with their reversible counterparts. Comparisons of symplectic and reversible methods for small model problems also suggest that a symplectic scheme may be more reliable. On the other hand, efficiency considerations typically demand, even for moderate-sized applications, an explicit integrator.

It turns out that it is often the case that the time-reparameterization function $g$ can be chosen to be a function of positions only, $g = g ( \pmb q )$ . In this case, a semiexplicit first-order method is possible.

The equations of motion after Poincar´e transformation become

$$
\begin{array} { l } { \displaystyle \frac { d } { d \tau } \boldsymbol { q } = \boldsymbol { g } ( \boldsymbol { q } ) \nabla _ { p } T ( p ) , } \\ { \displaystyle \frac { d } { d \tau } p = - \boldsymbol { g } ( \boldsymbol { q } ) \nabla _ { \boldsymbol { q } } V ( \boldsymbol { q } ) - ( H ( \boldsymbol { q } , p ) - E ) \nabla _ { \boldsymbol { q } } \boldsymbol { g } ( \boldsymbol { q } ) . } \end{array}
$$

If we discretize this system with the symplectic Euler method, there results

$$
\begin{array} { r l } & { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta \tau g ( \pmb { q } ^ { n } ) \nabla _ { p } T ( \pmb { p } ^ { n + 1 } ) , } \\ & { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta \tau g ( \pmb { q } ^ { n } ) \nabla _ { \pmb { q } } V ( \pmb { q } ^ { n } ) } \\ & { \qquad - \Delta \tau ( T ( \pmb { p } ^ { n + 1 } ) + V ( \pmb { q } ^ { n } ) - E ) \nabla _ { \pmb { q } } g ( \pmb { q } ^ { n } ) . } \end{array}
$$

Define vectors

$$
\begin{array} { r } { \pmb { a } = \pmb { p } ^ { n } - \Delta \tau g ( \pmb { q } ^ { n } ) \nabla _ { \pmb { q } } V ( \pmb { q } ^ { n } ) - \Delta \tau ( V ( \pmb { q } ^ { n } ) - E ) \nabla _ { \pmb { q } } g ( \pmb { q } ^ { n } ) , } \end{array}
$$

and

$$
\pmb { b } = \nabla _ { \pmb { q } } g ( \pmb { q } ^ { n } ) .
$$

Then we can write an implicit formula for the kinetic energy

$$
\hat { T } : = T ( \pmb { p } ^ { n + 1 } ) = T ( \pmb { a } - \hat { T } \pmb { b } ) .
$$

Under normal circumstances, this is an inexpensive problem to solve for $\hat { T }$ . For example, if ${ \cal T } ( p ) = { \textstyle \frac { 1 } { 2 } } p ^ { T } { \cal M } ^ { - 1 } p$ , it becomes a scalar quadratic equation in $\hat { T }$ . Once $\hat { T }$ is known, this can be inserted in (9.34) to yield $p ^ { n + 1 }$ , and then $\pmb q ^ { n + 1 }$ can be computed from (9.33).

It would be desirable to find higher-order semi-explicit symplectic methods under these assumptions. A natural candidate for a second-order method would be based on the concatenation of (9.33)–(9.34) with its adjoint. The problem is therefore to find an efficient way to solve

$$
\begin{array} { r l } & { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta \tau g ( \pmb { q } ^ { n + 1 } ) \nabla _ { p } T ( \pmb { p } ^ { n } ) , } \\ & { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta \tau g ( \pmb { q } ^ { n + 1 } ) \nabla _ { q } V ( \pmb { q } ^ { n + 1 } ) } \\ & { \qquad - \Delta \tau ( T ( \pmb { p } ^ { n } ) + V ( \pmb { q } ^ { n + 1 } ) - E ) \nabla _ { q } g ( \pmb { q } ^ { n + 1 } ) . } \end{array}
$$

The calculation is all explicit after $\pmb q ^ { n + 1 }$ is obtained from (9.35), hence the challenge is to solve equations of the form

$$
\hat { g } : = g ( \pmb q ^ { n + 1 } ) = g ( \pmb a ^ { \prime } + \hat { g } \pmb b ^ { \prime } ) ,
$$

where $\pmb { a } ^ { \prime }$ and ${ \pmb b } ^ { \prime }$ are fixed vectors. If this calculation can be performed efficiently, the entire method may be viable. In some cases, as when arclength reparameterization is used, the work required is similar to that of an implicit scheme for the full problem. However, in other cases, the work may be much less to solve (9.37) than it would be to apply an implicit method to the whole system. An example is where we know that the timestep is strongly dependent on only one or a few of the variables of a large system.

Another difficulty for the symplectic approach arises when the underlying fixed stepsize method which is most suited to the structure of the problem is a complicated construction, perhaps resulting from composition of a number of building blocks and coordinate transformations. In this case, the time-reversible approach is to be preferred, since its implementation is essentially independent of the details of how the fixed stepsize method is constructed; it is much easier to retain the explicit (or partially explicit) structure of the underlying fixed-stepsize scheme.

# 9.7 Exercises

1. Sundman transformation. Show that if a Sundman transformation is a function of the energy of a Hamiltonian system, the rescaled system is also Hamiltonian. Is this likely to give good results? Why or why not?

2. Scaling invariance. Show that (9.25) expresses a scaling invariance for the Kepler problem. How is the energy changed under this scaling of the variables?

3. Poincar´e transformation. Show that the symplectic Euler method can be made explicit for the Poincar´e transformation $g ( \pmb q )$ .

4. Constrained dynamics and adaptivity. Develop an adaptive method for simulating a constrained Hamiltonian system such as the spherical pendulum (unit

length, unit mass, and unit gravitational constant) subject to soft collisions (inverse power repulsion) with a fixed body at position $\pmb q _ { 0 }$ . The equations of motion can be written as

$$
\begin{array} { c } { { \dot { \pmb q } = \pmb M ^ { - 1 } \pmb p , } } \\ { { \dot { \pmb p } = - \nabla _ { \pmb q } V ( \pmb q ) - \pmb q \lambda , } } \\ { { \| \pmb q \| ^ { 2 } = 1 , } } \end{array}
$$

where the potential

$$
V ( { \pmb q } ) = z + \phi ( | { \pmb q } - { \pmb q } _ { 0 } | ) , \qquad \phi ( r ) = r ^ { - \alpha } ,
$$

is the sum of gravitational potential and the distance-dependent interaction potential between the pendulum bob and fixed body. The Sundman transformation should be chosen to reduce the stepsize in the vicinity of collisions between the bob and the fixed body. Test your method and report on its relative efficiency as a function of the power $\alpha$ in the repulsive wall and the choice of Sundman transformation function.

5. Switching. Discuss the construction of a time-reversible integrator to switch order of accuracy. As an example, consider the pair of methods consisting of the St¨ormer–Verlet method and the fourth order Yoshida method given in Chapter 6. Design a method which automatically changes the effective order of from 2 to 4 in a certain given region $R$ of phase space.

# 10

# Highly oscillatory problems

Hamiltonian systems often exhibit dynamical phenomena covering a vast range of different time scales. In this chapter, we will discuss systems with two well separated time scales. More specifically, we consider systems for which the fast motion is essentially oscillatory. Such systems can arise from very different applications such as celestial or molecular dynamics and they might manifest themselves in very different types of Hamiltonian equations. Hence, the discussion in this chapter is necessarily limited to special cases. However, the basic principles and ideas have a much wider range of applicability.

A standard integrator, whether symplectic or not, will, in general, have to use a stepsize that resolves the oscillations in the fast system and, hence, one might be forced to use very small timesteps in comparison to the slow dynamics which is of primary interest. However, in special cases, one might be able to individually exactly solve the fast oscillatory and the slow system. Following the idea of splitting methods, this suggests to compose these two exact propagators and to apply a stepsize that is large with respect to the period of the fast oscillations. Such a method is then called a large timestep (LTS) method. Often the fast oscillations cannot be integrated analytically. A natural idea for the construction of an LTS method is then to assign different timesteps to different parts of the system. This approach is called multiple timestepping (MTS) and can often even be implemented such that the overall timestepping procedure still generates a symplectic map.1 We will explain the basic idea of symplectic LTS/MTS methods in Section 10.1.

While the idea of LTS/MTS methods is very appealing, they have severe limitations which are linked to numerically induced resonances [20, 67] and a break-down of backward error analysis. The instability problem can be partially overcome by combining LTS/MTS methods with the idea of averaging. Averaging over a highly oscillatory degree of freedom is a very powerful tool in classical mechanics and a short introduction to the idea of averaging and the concept of an adiabatic invariant will be provided in Section 10.2. In Sections 10.3 and 10.4, we will describe two numerical methods that utilize averaging to eliminate or weaken resonance-induced instabilities in MTS methods. More specifically, the mollified impulse (MOLLY) method of GARC´ıA-ARCHILLA, SANZ-SERNA, AND SKEEL [67] was the first method to improve the stability properties of a symplectic MTS method by replacing the slow potential energy terms by an averaged (mollified) contribution. We will explain the basic idea of mollified MTS (MOLLY) in Section 10.4. MOLLY was subsequently extended to a wider class of averaging procedures by HAIRER, HOCHBRUCK, AND LUBICH (see the monograph [80]). A somewhat different approach, called reversible averaging (RA), was suggested by LEIMKUHLER AND REICH [112]. Reversible averaging will be discussed in Section 10.3.

# 10.1 Large timestep methods

In this section we will investigate large timestep (LTS) methods for Hamiltonian systems with slow and highly oscillatory degrees of freedom. We will in particular develop the idea of multiple timestepping (MTS) methods and investigate their numerical behavior for simple model problems. We will observe that MTS methods work well except for instabilities near certain choices of the stepsize $\Delta t$ . These instabilities are caused by numerical resonances which can already be observed for LTS methods applied to a single oscillatory degree of freedom and which are caused by a break-down of backward error analysis as discussed in Section 10.5.

# 10.1.1 A single oscillatory degree of freedom

Let us start with a numerical example.

Example 1 Consider a fast harmonic oscillator subject to a perturbation,for example

$$
\dot { q } = \omega p , \qquad \dot { p } = - \omega q - q .
$$

For $\omega \gg 1$ , the solutions are highly oscillatory and the eigenvalues of the solution operator

$$
{ \cal W } ( t ) = { \bf e } ^ { t A } , \qquad A = \left[ \begin{array} { c c } { { 0 } } & { { \omega } } \\ { { - \omega - 1 } } & { { 0 } } \end{array} \right] ,
$$

are on the unit circle for all $\omega \ge 0$ , i.e. the eigenvalues have modulus equal to one.

From a numerical point of view, one could be tempted to split the equations of motion into its highly oscillatory contribution

$$
\dot { q } = \omega p , \qquad \dot { p } = - \omega q ,
$$

and the perturbation

$$
\dot { q } = 0 , \qquad \dot { p } = - q .
$$

If we denote the associated matrix-valued solution operators by $W _ { 1 } ( t )$ and $W _ { 2 } ( t )$ , respectively, a second-order numerical propagator is obtained, for example via the matrix product

$$
\begin{array} { r } { \pmb { M } _ { \Delta t } = \pmb { W } _ { 2 } ( \Delta t / 2 ) \pmb { W } _ { 1 } ( \Delta t ) \pmb { W } _ { 2 } ( \Delta t / 2 ) . } \end{array}
$$

![](images/8eecc2540bac6d7d4907c4f77896314476b2769f7095b32603a6a37c6c17558e.jpg)  
Figure 10.1 Modulus of eigenvalues of numerical propagator ${ M } _ { \Delta t }$ as a function of $\omega \Delta t$ .

We compute the modulus of the eigenvalues of ${ M } _ { \Delta t }$ for $\omega = 1 0$ as a function of the stepsize $\Delta t \leq 0 . 2$ . Regions of instabilities can be clearly seen in Fig. 10.1 for $\omega \Delta t \approx k \pi$ , $k = 1 , 2 , 3$ .

A similar behavior would be observed for the LTS splitting method (10.3) applied to a nonlinearly perturbed harmonic oscillator

$$
\dot { q } = \omega p , \qquad \dot { p } = - \omega q - g ^ { \prime } ( q ) .
$$

We now give a heuristic reasoning for these numerically observed instabilities. We first introduce action-angle variables $( J , \phi )$ via $q ~ = ~ \sqrt { 2 J } \cos \phi$ and $p =$

$- \sqrt { 2 J } \sin \phi$ . Next we rewrite the given Hamiltonian $H = \omega ( p ^ { 2 } + q ^ { 2 } ) / 2 + g ( q )$ i n the form

$$
H ( \phi , J ) = \omega J + H _ { \mathsf { s } } ( \phi , J ) ,
$$

where $H _ { s } = g ( \sqrt { 2 J } \cos \phi )$ and, hence, $H ( \phi , J )$ is $2 \pi$ -periodic in the angle $\phi$ . Both $H _ { \mathrm { f } } = \omega J$ and $H _ { s }$ can be solved exactly and we define the LTS method $\psi _ { \Delta t }$ as a simple second-order composition of the associated flow maps, for example

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t / 2 , H _ { \mathrm { s } } } \circ \pmb { \phi } _ { \Delta t , H _ { \mathrm { f } } } \circ \pmb { \phi } _ { \Delta t / 2 , H _ { \mathrm { s } } } .
$$

According to a result by KUKSIN AND POSCHEL ¨ [100] (see also MOAN [135]), the symplectic method $\psi _ { \Delta t }$ can be written as the exact time-one-flow map of an extended Hamiltonian system $\tilde { H } _ { \Delta t } ( \phi , J , s , E )$ , where $\tilde { H } _ { \Delta t }$ is $2 \pi$ -periodic in the parameter $S$ . We may assume (see the Exercises) that the variable $S$ evolves according to the differential equation $\dot { s } = - \pi$ . The variable $E$ is the “action” variable conjugate to $s$ . The embedding of $\psi _ { \Delta t }$ into such an exact time-one-flow map can be chosen such that $\tilde { H }$ is a real-analytic function of the general form

$$
\tilde { H } _ { \Delta t } ( \phi , J , s , E ) = \Omega _ { \Delta t } J - \pi E + \Delta t f _ { \Delta t } ( \phi , J , s ) ,
$$

where $f _ { \Delta t }$ is an appropriate function and $\Omega _ { \Delta t } \in [ - \pi , \pi )$ is defined by

$$
\Omega _ { \Delta t } = [ \omega \Delta t + \pi ] _ { \sf m o d } 2 \pi - \pi .
$$

The definition of $\Omega _ { \Delta t }$ is motivated by the fact that

$$
\pmb { \phi } _ { \Delta t , H _ { \mathrm { f } } } = \pmb { \phi } _ { \Delta t , \hat { H } _ { \mathrm { f } } } ,
$$

with $\hat { H } _ { \mathrm { f } } = \Omega _ { \Delta t } J / \Delta t = \hat { \omega } J$ . Hence the numerical method (10.5) cannot distinguish between $\omega$ and $\hat { \omega } = \Omega _ { \Delta t } / \Delta t$ .

For $\Delta t \omega  0$ , we obtain $\Omega _ { \Delta t } = \Delta t \omega$ and one can average over the (fast) variable $S$ in $\tilde { H } _ { \Delta t }$ and that leads to the modified Hamiltonian of standard backward error analysis [143, 16]. However, for the LTS methods considered in this chapter, $\omega \Delta t$ and hence $\Omega _ { \Delta t }$ are not necessarily small. In fact, $| \Omega _ { \Delta t } |$ is only bounded by $\pi$ . To understand the possible implications let us investigate the canonical equations of motion

$$
\begin{array} { l l } { \dot { \phi } = \Omega _ { \Delta t } + \Delta t \nabla _ { J } f _ { \Delta t } ( J , \phi , s ) , \qquad } & { \boldsymbol { j } = - \Delta t \nabla _ { \phi } f _ { \Delta t } ( J , \phi , s ) , } \\ { \dot { s } = - \pi , \qquad } & { \dot { E } = - \Delta t \nabla _ { s } f _ { \Delta t } ( \phi , J , s ) . } \end{array}
$$

The associated flow map $\boldsymbol { \Phi } _ { \tau , \tilde { H } }$ completely characterizes the behavior of the numerical method $\psi _ { \Delta t }$ . In particular, the numerical method is called effectively stable2 if $J ( \tau )$ and $E ( \tau )$ remain bounded over long time-intervals $| { \boldsymbol { \tau } } | \leq n \cdot \Delta t$ ,

$n \gg 1$ . We only state at this point that the averaging principle (see, for example, [8]) implies that $J ( \tau )$ and $E ( \tau )$ are approximately constant provided

(i) the two natural frequencies $\Omega _ { 1 } = - \pi$ and $\Omega _ { 2 } = \Omega _ { \Delta t }$ of the system are non-resonant3 and

(ii) there is separation of time scales, i.e. the two frequencies $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are much larger than $| \dot { J } |$ and $| \dot { E } |$ .

Condition (ii) is clearly not satisfied for

$$
\omega \Delta t = 2 k \pi , \qquad k = 1 , 2 , 3 , \ldots ,
$$

since this implies

$$
\Omega _ { 2 } = \Omega _ { \Delta t } = 0 .
$$

On the other hand, for

$$
\omega \Delta t = k \pi , \qquad k = 1 , 3 , 5 , \ldots ,
$$

we obtain

$$
\Omega _ { 2 } = \Omega _ { \Delta t } = - \pi = \Omega _ { 1 } ,
$$

and Condition (i) is violated. These heuristic arguments provide some indication why numerical instabilities are observed for $\omega \Delta t$ equal to integer multiples of $\pi$ . See the Exercises for more background material.

# 10.1.2 Slow-fast systems

We now extend the idea of LTS methods to a more general class of slow–fast Hamiltonian systems. This will lead us to the concept of multiple timestepping (MTS). Let us assume that we are given a Hamiltonian function $H$ that can be split into two parts $H _ { \mathsf { f } }$ and $H _ { s }$ ; i.e. $H = H _ { \uparrow } + H _ { \uparrow }$ . The assumption is that the equations of motion associated with $H _ { s }$ can be solved with a stepsize $\Delta t _ { s }$ , while the dynamics of $H _ { \mathsf { f } }$ requires a stepsize $\Delta t _ { \mathsf { f } } \ll \Delta t _ { \mathsf { s } }$ . A standard symplectic integrator will then require that a stepsize of $\Delta t \approx \Delta t _ { \mathsf { f } }$ is used for the overall system with Hamiltonian $H$ . Of course, one would like to make use of the fact that part of the system evolves on a slower time scale and to develop an LTS method.

To illustrate the basic idea we consider a standard Newtonian system with Hamiltonian

$$
H _ { 5 } = \frac 1 2 p ^ { T } M ^ { - 1 } p + V ( \pmb q )
$$

and assume that it is coupled to a rapidly oscillating degree of freedom with position $x$ , momentum $p _ { x }$ and Hamiltonian

$$
H _ { \mathsf { f } } = \frac { 1 } { 2 \varepsilon } \left[ p _ { x } ^ { 2 } + V _ { \mathsf { f } } ( x , \pmb { q } ) \right] ,
$$

where $\varepsilon > 0$ is a small parameter and $V _ { \mathsf { f } }$ is an appropriate potential energy function. An example of such a fast system is provided by a stiff harmonic oscillator whose position $x$ vibrates about an equilibrium position $L > 0$ that depends on the slow coordinates $\pmb q$ ; i.e. $L = L ( q )$ . The associated Hamiltonian is

$$
H _ { \mathrm { f } } = \frac { 1 } { 2 \varepsilon } \left[ p _ { x } ^ { 2 } + ( x - L ( \pmb { q } ) ) ^ { 2 } \right] .
$$

Another $\mathsf { e x }$ ample is provided by a stiff harmonic oscillator whose “spring” constant $K > 0$ depends on $\pmb q$ ; i.e.

$$
H _ { \mathsf { f } } = \frac { 1 } { 2 \varepsilon } \left[ p _ { x } ^ { 2 } + K ( \pmb { q } ) x ^ { 2 } \right] .
$$

In either case, we can write the total Hamiltonian $H$ as

$$
H = H _ { \mathrm { f } } + H _ { \mathrm { s } }
$$

and obtain the equations of motion

$$
\begin{array} { r l r l } & { \dot { \pmb { p } } = - \nabla _ { \pmb { q } } V ( \pmb { q } ) - \varepsilon ^ { - 1 } \nabla _ { \pmb { q } } V _ { \dagger } ( x , \pmb { q } ) , } & & { \dot { \pmb { q } } = \pmb { M } ^ { - 1 } \pmb { p } , } \\ & { \dot { p } _ { x } = - \varepsilon ^ { - 1 } \nabla _ { x } V _ { \dagger } ( x , \pmb { q } ) , } & & { \dot { x } = \varepsilon ^ { - 1 } p _ { x } , } \end{array}
$$

which can be integrated by the St¨ormer–Verlet method. However, for stability reasons, the stepsize $\Delta t$ has to be proportional to $\varepsilon$ .

A simple idea to improve this situation is to integrate the equations of motion associated to the Hamiltonian $H _ { \mathsf { f } }$ ; i.e.

$$
\begin{array} { r l } { \dot { p } = - \varepsilon ^ { - 1 } \nabla _ { q } V _ { \mathsf { f } } ( x , q ) , \quad } & { \dot { q } = \mathbf { 0 } , } \\ { \dot { p } _ { x } = - \varepsilon ^ { - 1 } \nabla _ { x } V _ { \mathsf { f } } ( x , q ) , \quad } & { \dot { x } = \varepsilon ^ { - 1 } p _ { x } , } \end{array}
$$

either exactly or to apply the St¨ormer–Verlet method with a small stepsize $\delta t \sim \varepsilon$ . We denote the associated propagator by $\pmb { \psi } _ { \delta t , H _ { \mathrm { f } } }$ . Then we apply $\pmb { \psi } _ { \delta t , H _ { f } }$ over $N$ steps, where the integer $N$ is chosen such that the slow system

$$
\begin{array} { c c } { { \dot { p } = - \nabla _ { q } V ( q ) , ~ } } & { { \dot { q } = M ^ { - 1 } p , } } \\ { { \dot { p } _ { x } = 0 , ~ } } & { { \dot { x } = 0 , } } \end{array}
$$

can be integrated by the St¨ormer–Verlet method with stepsize $\Delta t = \delta t \cdot N$ . Let us denote this propagator by $\psi _ { \Delta t , H _ { \mathrm { s } } }$ . A symmetric one step method is now given by the composition

$$
\psi _ { \Delta t } = \psi _ { \Delta t / 2 , H _ { \mathrm { s } } \mathrm { ~ o ~ } \big [ } \psi _ { \delta t , H _ { \mathrm { f } } } { \big ] } ^ { N } \circ \psi _ { \Delta t / 2 , H _ { \mathrm { s } } } .
$$

This is an example of a multiple timestepping (MTS) method. To summarize, the general idea of MTS is to split the given Hamiltonian into a slow and fast part, to integrate the fast and slow systems using a symplectic method with different timesteps, and to obtain an overall timestepping method by proper composition as in (10.9). The resulting one-step method is symplectic. However, the map $\psi _ { \Delta t }$ is not necessarily close to the identity and standard backward error analysis does not apply. Hence it is not clear whether such a method will be stable and conserve energy.

# 10.1.3 Adiabatic invariants

To gain insight into the solution behavior of the slow–fast systems introduced in the previous subsection, let us discuss the limiting case $\varepsilon  0$ for bounded Hamiltonian $H$ . We view $H _ { \mathsf { f } }$ as a time-dependent Hamiltonian

$$
H _ { \mathrm { f } } ( x , p _ { x } , t ) = \frac { 1 } { 2 \varepsilon } p _ { x } ^ { 2 } + \frac { 1 } { \varepsilon } V _ { \mathrm { f } } ( x , \pmb { q } ( t ) )
$$

in the fast degree of motion $( x , p _ { x } )$ , where $\pmb q ( t )$ is a given slowly varying function. Because of the bounded energy assumption, we necessarily have $p _ { x } ( t ) = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ and $x ( t ) = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ . Note also that, because of the $\mathsf { e x }$ plicit time dependence, the equations

$$
\dot { p } _ { x } = - \varepsilon ^ { - 1 } \nabla _ { x } V _ { \mathsf { f } } ( x , t ) , \qquad \dot { x } = \varepsilon ^ { - 1 } p _ { x }
$$

do not preserve the Hamiltonian $H _ { \mathrm { f } }$ . However, for $\varepsilon$ small enough, the solutions of (10.10) form nearly closed curves, with approximate period $\tau = \mathcal { O } ( \varepsilon )$ , due to the time dependence of $V _ { \sf f } ( x , t )$ . Hence, over one period, we can formally “shadow” the $\mathsf { e x a c t }$ trajectory by the curve obtained for the same initial data and the same equations but with $t$ temporarily frozen to its initial value $t = \bar { t }$ . Let us denote the region enclosed by this periodic curve by $\mathcal { A } ( \bar { t } ) \subset \mathbb { R } ^ { 2 }$ . We can compute the area $A$ of the region $\mathcal { A }$ for any value of $\bar { t } = t$ ; i.e.

$$
A ( t ) = \int _ { A ( t ) } d p \wedge d q .
$$

Note that the area necessarily satisfies $A ( t ) = { \mathcal { O } } ( \varepsilon )$ for bounded energy $H _ { f } =$ $\mathcal { O } ( \varepsilon ^ { 0 } )$ .