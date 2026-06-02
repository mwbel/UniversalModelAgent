The classical choice $n \ = \ 1$ [Sundman, 1912] replaces the $R ^ { - 2 }$ type singularity by an undetermined expression, $\mathbf { R } / R$ , as $R  0$ which is clearly better behaved for small separations. In section 3.3 we introduced the value $n = 3 / 2$ together with comoving coordinates for cosmological equations of motion. This is also a good compromise for eccentric twobody orbits since using the eccentric anomaly ( $n = 1$ ) is favourable at apocentre and the true anomaly ( $n = 2$ ) is better at pericentre.

Other alternative smoothing functions have been examined [Zare & Szebehely, 1975]. In particular, it was found that the inverse Lagrangian function offers practical advantages. However, for most purposes, integration of the perturbed two-body problem with the time transformation $t ^ { \prime } = R$ is preferable when it comes to two-body regularization. For completeness, we also mention a brave early attempt to introduce time smoothing based on the potential or kinetic energy of the most strongly bound cluster members [Heggie, 1972a]. Although the requirement of equal time-steps proved too expensive as far as star cluster simulations are concerned, this method was put to good use in a series of three-body scattering experiments [Hills, 1975].

The essential idea behind regularization is to transform both the time and the coordinates, and the latter proves much harder in the general case of three-dimensional (3D) motion. Since we are discussing the basic concept here, this can be done in 1D, which permits simplifications to be made in the absence of the term $\mathbf { R } / R$ with $n = 1$ . If we neglect external perturbations and set $t ^ { \prime } = x$ , equation (4.6) reduces to

$$
x ^ { \prime \prime } = x ^ { \prime 2 } / x - \left( m _ { k } + m _ { l } \right) .
$$

To proceed we make use of the binding energy per unit reduced mass,

$$
\begin{array} { r } { h = \frac { 1 } { 2 } \dot { \bf R } ^ { 2 } - ( m _ { k } + m _ { l } ) / R , } \end{array}
$$

which is a constant of the motion evaluated from the initial conditions. Substitution of $\dot { x } = x ^ { \prime } / x$ from (4.4) then gives

$$
x ^ { \prime \prime } = 2 h x + ( m _ { k } + m _ { l } ) .
$$

As can be readily seen, this equation is regular $^ *$ for $x \to 0$ . However, the displaced harmonic oscillator equation can be simplified by introducing new coordinates from the relation $u ^ { 2 } = x $ . Twice differentiation of $u ^ { 2 }$ , with one more use of the energy equation, finally yields the extremely simple result

$$
\begin{array} { r } { u ^ { \prime \prime } = \frac { 1 } { 2 } h u . } \end{array}
$$

We note that the coordinate transformation has reduced the frequency by a factor of 2, as well as eliminated the constant term.

In summary, the motion of two mass-points on a line can be integrated to high accuracy even though collisions take place. It is useful from a practical point of view to consider 1D as the limiting case for the eccentricity approaching unity. Finally, such an orbit may be calculated with constant time-step,

$$
\Delta \tau = \eta _ { U } / | 2 h | ^ { 1 / 2 } ,
$$

where $\eta _ { U } / 2 \pi$ is a specified fraction of the physical period.

# 4.3 Levi-Civita transformation

An increase of dimension from 1D to 2D first is quite instructive since it deals with the undetermined expression $\mathbf { R } / R$ . By analogy with the former development, we write $R = u _ { 1 } ^ { 2 } + u _ { 2 } ^ { 2 }$ which permits the coordinate transformation for the components $x$ and $y$ , denoted $R _ { 1 }$ and $R _ { 2 }$ ,

$$
\begin{array} { l } { { R _ { 1 } = u _ { 1 } ^ { 2 } - u _ { 2 } ^ { 2 } , } } \\ { { R _ { 2 } = 2 u _ { 1 } u _ { 2 } . } } \end{array}
$$

By summation of the squares, it is readily verified that the original relation is recovered. The transformation (4.12) may be written as

$$
\mathbf { R } = \mathcal { L } ( \mathbf { u } ) \mathbf { u } ,
$$

where the Levi-Civita [1920] matrix is given by

$$
\begin{array} { r } { \mathcal { L } ( { \bf u } ) = \left[ \begin{array} { c c } { u _ { 1 } } & { - u _ { 2 } } \\ { u _ { 2 } } & { u _ { 1 } } \end{array} \right] . } \end{array}
$$

The formal derivation of two-body regularization in 2D may be done in terms of manipulations with the Levi-Civita matrix. In the following we follow the presentation of Bettis & Szebehely [1972]. According to Stiefel $\&$ Scheifele [1971], the linear matrix (4.14) has the properties

$$
\begin{array} { r l } & { \mathcal { L } ^ { \mathrm { T } } ( \mathbf { u } ) \mathcal { L } ( \mathbf { u } ) = R \mathbf { I } , } \\ & { \qquad \mathcal { L } ^ { \prime } ( \mathbf { u } ) = \mathcal { L } ( \mathbf { u } ^ { \prime } ) , } \\ & { \qquad \mathcal { L } ( \mathbf { u } ) \mathbf { v } = \mathcal { L } ( \mathbf { v } ) \mathbf { u } , } \\ & { \mathbf { u } \cdot \mathbf { u } \mathcal { L } ( \mathbf { v } ) \mathbf { v } - 2 \mathbf { u } \cdot \mathbf { v } \mathcal { L } ( \mathbf { u } ) \mathbf { v } + \mathbf { v } \cdot \mathbf { v } \mathcal { L } ( \mathbf { u } ) \mathbf { u } = 0 . } \end{array}
$$

Here $\mathbf { I }$ is the unit matrix and $\mathbf { u } , \mathbf { v }$ are arbitrary vectors. The second of these equations holds for linear matrices, whereas the third obeys the commutative rule and the fourth defines the so-called ‘bilinear relation’.

We now aim to express (4.6) in terms of the new dependent variable $\mathbf { u }$ . The first regularized derivative of (4.13) is readily derived by employing the second and third properties (4.15), which yields

$$
\mathbf { R } ^ { \prime } = 2 \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime } .
$$

From $\mathcal { L } ^ { \prime } ( \mathbf { u } ) = \mathcal { L } ( \mathbf { u } ^ { \prime } )$ we then obtain

$$
\mathbf { R } ^ { \prime \prime } = 2 \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime \prime } + 2 \mathcal { L } ( \mathbf { u } ^ { \prime } ) \mathbf { u } ^ { \prime } .
$$

Using this form for $\mathbf { R } ^ { \prime \prime }$ , we substitute (4.13) and (4.16) in (4.6) with the choice $n = 1$ to give

$$
\begin{array} { r l r } & { } & { 2 \mathbf { u } \cdot \mathbf { u } \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime \prime } + 2 \mathbf { u } \cdot \mathbf { u } \mathcal { L } ( \mathbf { u } ^ { \prime } ) \mathbf { u } ^ { \prime } - 4 \mathbf { u } \cdot \mathbf { u } ^ { \prime } \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime } + ( m _ { k } + m _ { l } ) \mathcal { L } ( \mathbf { u } ) \mathbf { u } } \\ & { } & { \qquad = ( \mathbf { u } \cdot \mathbf { u } ) ^ { 3 } \mathbf { F } _ { k l } , \quad ( 4 \mathbf { u } \times \mathbf { u } ) ^ { 4 } } \end{array}
$$

where $R ^ { \prime } = 2 { \bf u } \cdot { \bf u } ^ { \prime }$ has been substituted for the scalar radial velocity. By virtue of the last equation (4.15), this expression reduces to

$$
2 \mathbf { u } \cdot \mathbf { u } \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime \prime } - 2 \mathbf { u } ^ { \prime } \cdot \mathbf { u } ^ { \prime } \mathcal { L } ( \mathbf { u } ) \mathbf { u } + ( m _ { k } + m _ { l } ) \mathcal { L } ( \mathbf { u } ) \mathbf { u } = ( \mathbf { u } \cdot \mathbf { u } ) ^ { 3 } \mathbf { F } _ { k l } .
$$

In the next step we multiply by ${ { \mathcal { L } } ^ { - 1 } } ( { \mathbf { u } } )$ and introduce the transpose defined by the first relation (4.15), which results in

$$
\begin{array} { r } { \mathbf { u } ^ { \prime \prime } + \frac 1 2 \{ [ ( m _ { k } + m _ { l } ) - 2 \mathbf { u } ^ { \prime } \cdot \mathbf { u } ^ { \prime } ] / \mathbf { u } \cdot \mathbf { u } \} \mathbf { u } = \frac 1 2 \mathbf { u } \cdot \mathbf { u } \mathcal { L } ^ { \mathrm { T } } ( \mathbf { u } ) \mathbf { F } _ { k l } . } \end{array}
$$

From (4.16) and the definition $\dot { R } = R ^ { \prime } / R$ this yields the velocity transformation

$$
\dot { \mathbf { R } } = 2 \mathcal { L } ( \mathbf { u } ) \mathbf { u } ^ { \prime } / R .
$$

Combining (4.21) with $\dot { \mathbf { R } } ^ { \mathrm { T } } = 2 \mathbf { u } ^ { \prime } \mathcal { L } ^ { \mathrm { T } } ( \mathbf { u } ) / R$ and the orthogonality condition, we obtain the simplified square velocity relation

$$
\dot { \bf R } ^ { 2 } = 4 { \bf u } ^ { \prime } \cdot { \bf u } ^ { \prime } / R .
$$

With $\mathbf { u } \cdot \mathbf { u } = R$ , this enables the final equation of motion to be written as

$$
\begin{array} { r } { \mathbf u ^ { \prime \prime } = \frac { 1 } { 2 } h \mathbf u + \frac { 1 } { 2 } R \mathcal { L } ^ { \mathrm { T } } ( \mathbf u ) \mathbf F _ { k l } . } \end{array}
$$

By (4.8) and (4.22), the binding energy per unit reduced mass takes the form

$$
h = [ ( 2 \mathbf { u } ^ { \prime } \cdot \mathbf { u } ^ { \prime } - ( m _ { k } + m _ { l } ) ] / R .
$$

The two-body energy $h$ changes with time due to the perturbing force. The scalar product of $\dot { \mathbf { R } }$ and (4.2) leads to the rate of energy change

$$
\frac { d } { d t } \left[ \frac { 1 } { 2 } \dot { \bf R } ^ { 2 } - \frac { ( m _ { k } + m _ { l } ) } { R } \right] = \dot { \bf R } \cdot { \bf F } _ { k l } ,
$$

which reproduces the well-known expression ${ \dot { h } } = { \dot { \mathbf { R } } } \cdot \mathbf { F } _ { k l }$ . Conversion to regularized derivative by $h ^ { \prime } = \mathbf { R } ^ { \prime } \cdot \mathbf { F } _ { k l }$ and use of the velocity expression (4.16) then results in the equation of motion

$$
\begin{array} { r } { \boldsymbol { h } ^ { \prime } = 2 \mathbf { u } ^ { \prime } \cdot \mathcal { L } ^ { \mathrm { T } } ( \mathbf { u } ) \mathbf { F } _ { k l } . } \end{array}
$$

We conclude this derivation by remarking that the beautiful Levi-Civita treatment is seldom used in practical work. It is particularly suitable for educational purposes when introducing students to the subject.

# 4.4 Kustaanheimo–Stiefel method

The relations (4.12) exploit properties of mapping in the complex plane; hence generalization to 3D is not possible. This stumbling block prevented progress until it was realized by Kustaanheimo & Stiefel [1965] that a 4D formulation could be achieved. Their generalization of the Levi-Civita formalism gave rise to the $4 \times 4$ matrix

$$
\mathcal { L } ( \mathbf { u } ) = \left[ \begin{array} { r r r r } { u _ { 1 } } & { - u _ { 2 } } & { - u _ { 3 } } & { u _ { 4 } } \\ { u _ { 2 } } & { u _ { 1 } } & { - u _ { 4 } } & { - u _ { 3 } } \\ { u _ { 3 } } & { u _ { 4 } } & { u _ { 1 } } & { u _ { 2 } } \\ { u _ { 4 } } & { - u _ { 3 } } & { u _ { 2 } } & { - u _ { 1 } } \end{array} \right] .
$$

It is convenient to use the same symbol as in (4.14) since it is clear from the context which formulation is intended. Now the basic relation (4.13) still applies but, because of some redundancy, a fourth fictitious coordinate and corresponding velocity is introduced. For completeness, the explicit components of $\mathbf { R }$ are given by

$$
\begin{array} { r l } & { R _ { 1 } = u _ { 1 } ^ { 2 } - u _ { 2 } ^ { 2 } - u _ { 3 } ^ { 2 } + u _ { 4 } ^ { 2 } , } \\ & { R _ { 2 } = 2 \big ( u _ { 1 } u _ { 2 } - u _ { 3 } u _ { 4 } \big ) , } \\ & { R _ { 3 } = 2 \big ( u _ { 1 } u _ { 3 } + u _ { 2 } u _ { 4 } \big ) , } \\ & { R _ { 4 } = 0 . } \end{array}
$$

Note that the fourth component of $\mathbf { R }$ is zero by application of (4.13). As can be readily verified, the square root of the sum of the distance squares (4.28) simplifies to

$$
R = u _ { 1 } ^ { 2 } + u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } + u _ { 4 } ^ { 2 } .
$$

When we go from a 2D to a 4D treatment, the fourth property (4.15) is not satisfied in general. Thus it can be shown [Stiefel $\&$ Scheifele, 1971] that for this to be the case, we require the relation

$$
u _ { 4 } u _ { 1 } ^ { \prime } - u _ { 3 } u _ { 2 } ^ { \prime } + u _ { 2 } u _ { 3 } ^ { \prime } - u _ { 1 } u _ { 4 } ^ { \prime } = 0 .
$$

This is called the bilinear relation and plays a fundamental role for understanding some theoretical aspects of the development† [cf. Stiefel $\&$ Scheifele, 1971]. In practical terms, it is a constraint and corresponds to the identity $\dot { R } _ { 4 } = 0$ . Here we merely remark that (4.30) may also be used as a check on the reliability of the numerical solutions, although this does not seem to have been tried.

Since one of the components of $\mathbf { u }$ is arbitrary, we have some freedom of choice when it comes to specifying the initial components. If $R _ { 1 } > 0$ , we combine the first equation (4.28) with (4.29), which results in

$$
\begin{array} { r } { u _ { 1 } ^ { 2 } + u _ { 4 } ^ { 2 } = \frac 1 2 ( R _ { 1 } + R ) . } \end{array}
$$

The redundancy choice $u _ { 4 } = 0$ then gives rise to the relations

$$
\begin{array} { r c l } { { } } & { { } } & { { u _ { 1 } = [ \frac 1 2 ( R _ { 1 } + R ) ] ^ { 1 / 2 } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { u _ { 2 } = \frac 1 2 R _ { 2 } / u _ { 1 } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { u _ { 3 } = \frac 1 2 R _ { 3 } / u _ { 1 } . } } \end{array}
$$

Likewise, if $R _ { 1 } < 0$ , we subtract the first equation (4.28) from (4.29) and obtain

$$
\begin{array} { r } { u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } = \frac 1 2 ( R - R _ { 1 } ) . } \end{array}
$$

Thus by setting $u _ { 3 } = 0$ we have

$$
\begin{array} { r l } & { u _ { 2 } = [ \frac { 1 } { 2 } ( R - R _ { 1 } ) ] ^ { 1 / 2 } , } \\ & { u _ { 1 } = \frac { 1 } { 2 } R _ { 2 } / u _ { 2 } , } \\ & { u _ { 4 } = \frac { 1 } { 2 } R _ { 3 } / u _ { 2 } . } \end{array}
$$

The reason for these alternatives is that the initial values must be numerically well defined, and this is ensured by the above choice.

We also need an expression for the initial regularized velocity, $\mathbf { u } ^ { \prime }$ . This is achieved by inverting (4.16) and making use of the first relation (4.15), which leads to

$$
\begin{array} { r } { { \bf u } ^ { \prime } = \frac { 1 } { 2 } \mathcal { L } ( { \bf u } ) { \bf R } ^ { \prime } / R . } \end{array}
$$

Using the definition (4.4), we have $\dot { R } = R ^ { \prime } / R$ . This yields the more convenient expression

$$
\begin{array} { r } { { \bf u } ^ { \prime } = \frac { 1 } { 2 } \mathcal { L } ( { \bf u } ) \dot { \bf R } . } \end{array}
$$

From the above, it can be seen that the 2D formalism carries over to the KS treatment of 3D systems. However, as emphasized by Stiefel & Scheifele [1971], the same line of approach in going from the timesmoothed equations of motion (4.6) to (4.23) cannot be repeated in the general case. The reason is that the KS transformation is ambiguous and there is no unique set of vectors $\mathbf { u }$ for a given $\mathbf { R }$ . Accordingly, the only way around this difficulty is to postulate the form (4.23) and verify that the original equations of motion are satisfied. Following this formal exercise, we omit the argument from the Levi-Civita matrix and also represent the perturbing force as $\mathbf { F }$ for simplicity. Hence the equations of motion take the final form

$$
\begin{array} { r l } & { \mathbf { u } ^ { \prime \prime } = \frac { 1 } { 2 } h \mathbf { u } + \frac { 1 } { 2 } R \mathcal { L } ^ { \mathrm { T } } \mathbf { F } , } \\ & { \quad h ^ { \prime } = 2 \mathbf { u } ^ { \prime } \cdot \mathcal { L } ^ { \mathrm { T } } \mathbf { F } , } \\ & { \quad { t } ^ { \prime } = \mathbf { u } \cdot \mathbf { u } . } \end{array}
$$

It is evident that these equations are well behaved for $R \to 0$ . In particular, the relative contribution from the perturbing term is proportional to

$R ^ { 3 }$ for a circular orbit. Consequently, $h$ tends to a constant rapidly with decreasing perturbation. A total of ten regularized equations are required in order to obtain the solution for the relative motion, compared with just six in the case of direct integration. The method employed here is based on the standard polynomial or Hermite formulations and will be discussed in a subsequent chapter.

In practical applications, the question arises of how to determine the physical time. Notwithstanding the concept of the time element [cf. Stiefel $\&$ Scheifele, 1971], which has proved useful in satellite theory, a direct integration of (4.39) to high order has some merit. First, it can also be employed for near-parabolic and hyperbolic motion. A second advantage is that it is suitable during intervals of strong perturbations. Hence the simplicity of such a treatment for general $N$ -body problems outweighs some loss of accuracy for small perturbations on elliptic orbits when phase errors may be tolerated.

For future reference we note that when using the KS variables, the semi-major axis is obtained from $a = - \textstyle { \frac { 1 } { 2 } } ( m _ { k } + m _ { l } ) / h$ . Another useful expression is the eccentricity, evaluated at an arbitrary phase in the orbit by means of the eccentric anomaly. Hence combining $e \cos \theta = 1 - R / a$ and $e \sin \theta = { \bf R } \cdot \dot { \bf R } / [ ( m _ { k } + m _ { l } ) a ] ^ { 1 / 2 }$ we have

$$
e ^ { 2 } = ( 1 - R / a ) ^ { 2 } + 4 ( { \bf u } \cdot { \bf u ^ { \prime } } ) ^ { 2 } / ( m _ { k } + m _ { l } ) a .
$$

Here we have used the definition $R ^ { \prime } = \dot { R } R$ and substituted from $t ^ { \prime \prime } = R ^ { \prime }$ by (4.39).

To describe the motion completely, we introduce the centre of mass as a fictitious particle. The corresponding equation of motion is given by the mass-weighted sum of perturbations,

$$
{ \ddot { \mathbf { r } } } _ { \mathrm { c m } } = ( m _ { k } \mathbf { F } _ { k } + m _ { l } \mathbf { F } _ { l } ) / ( m _ { k } + m _ { l } ) .
$$

Note that the dominant two-body interaction cancels analytically here. Accordingly, the spatial coordinates of the components are recovered from

$$
\begin{array} { r } { { \bf r } _ { k } = { \bf r } _ { \mathrm { c m } } + \mu { \bf R } / m _ { k } , } \\ { { \bf r } _ { l } = { \bf r } _ { \mathrm { c m } } - \mu { \bf R } / m _ { l } , } \end{array}
$$

with $\mu = m _ { k } m _ { l } / ( m _ { k } + m _ { l } )$ , and similarly for the velocities $\dot { \mathbf { r } } _ { k } , \dot { \mathbf { r } } _ { l }$ . Further details of how to obtain the complete solutions are given in a later chapter.

The device of energy stabilization has also been tried with success. Following the discussion of section 3.5, we generalize (4.37) from (3.33) and include a correction term which yields

$$
\begin{array} { r } { \mathbf { u } ^ { \prime \prime } = \frac { 1 } { 2 } h \mathbf { u } + \frac { 1 } { 2 } R \mathcal { L } ^ { T } \mathbf { F } - \alpha ( \tilde { h } - h ) R \mathbf { u } ^ { \prime } / ( m _ { k } + m _ { l } ) . } \end{array}
$$

Accordingly, $\tilde { h } R$ is calculated explicitly at every step (cf. 4.24) and this quantity is well defined for $R \to 0$ . Likewise for the scaling factor $\alpha$ , which we take to be $0 . 4 / \Delta \tau$ on dimensional grounds, with the numerical constant being an optimum choice for the present integration scheme. Although the perturbation may be arbitrarily large in principle because the integration step is shortened, the stabilizing term should only be included for fairly modest values.

The standard KS formulation has also been implemented for a real application to geocentric satellite orbits [Palmer et al., 1998]. Comparisons with direct integration showed that the regularized equations are beneficial for obtaining accurate solutions of highly eccentric orbits.

On a historical note, the first application of KS regularization to the $N$ -body problem was given by Peters [1968a,b]. This development made use of the elegant Hamiltonian formalism which will be exploited in the next chapter. Numerical examples for $N = 3$ [Szebehely & Peters, 1967] and $N = 2 5$ [Peters, 1968b] were discussed at an early stage. In particular, the former study illustrating a sequence of close encounters did much to publicize the power of regularization in stellar dynamics.

It may also be remarked that the earliest $N$ -body implementations of KS employed the explicit recalculation of (4.24) instead of integrating the perturbation effect according to (4.26). However, very soon thereafter it was realized that the latter procedure is advantageous [Bettis & Szebehely, 1972; Aarseth, 1972b]. One of the reasons for the improved behaviour is that the explicit expression involves the predicted velocity which is known to lower order, but in addition the singular nature of (4.24) gives rise to growing oscillations at small separations.

Some advantages in adopting regularization of dominant two-body motion may be summarized as follows:

• The equations of motion are regular and well behaved for $R \to 0$ A smaller number of integration steps per orbit is required • The numerical stability of even circular motion is improved $\bullet$ Further error reduction may be achieved by rectification‡ • Distant contributions can be neglected since $F \propto 1 / r ^ { 3 }$ • Two-body elements can be used to study tidal interactions

The main point on the debit side is the need for coordinate transformations. However, the number of operations involved is not very large and no square root is required. In the next section we discuss an alternative regularization that employs the actual physical variables.

# 4.5 Burdet–Heggie alternative

Although elegant, the KS formulation involves frequent transformations from the coordinates $\mathbf { u }$ to $\mathbf { r } _ { k } , \mathbf { r } _ { l }$ , as well as setting up the initial relations (4.32). Such complications may act as a deterrent to the new practitioner who has to get used to working with fictitious quantities. It is therefore of interest to present an alternative method that is based on physical coordinates, thereby avoiding repetitive transformations. In the following we discuss the independent derivation of Heggie [1973], although an earlier formulation was presented by Burdet [1967, 1968].

We begin by choosing the standard time transformation, $t ^ { \prime } = R$ , which again gives rise to an equation of motion of the form

$$
\mathbf { R } ^ { \prime \prime } = R ^ { \prime } \mathbf { R } ^ { \prime } / R - M \mathbf { R } / R + R ^ { 2 } \mathbf { F } ,
$$

with the notation $M = m _ { k } + m _ { l }$

Following Heggie [1973], let us define the quantities $P$ and $\mathbf { B }$ by§

$$
\begin{array} { r l } & { P = - 2 M / R + { \bf R } ^ { \prime 2 } / R ^ { 2 } , } \\ & { { \bf B } = M { \bf R } / R - { \bf R } ^ { \prime 2 } { \bf R } / R ^ { 2 } + R ^ { \prime } { \bf R } ^ { \prime } / R . } \end{array}
$$

Straightforward application of (4.4) results in

$$
\begin{array} { r l } & { P = - 2 M / R + \dot { \bf R } ^ { 2 } , } \\ & { { \bf B } = M { \bf R } / R - \dot { \bf R } ^ { 2 } { \bf R } + ( { \bf R } \cdot \dot { \bf R } ) \dot { \bf R } . } \end{array}
$$

This enables us to write (4.44) as

$$
\mathbf { R } ^ { \prime \prime } = { \cal P } \mathbf { R } + \mathbf { B } + R ^ { 2 } \mathbf { F } .
$$

From (4.2), (4.46) and (4.47), we readily obtain the first-order companion equations for $\dot { P }$ and $\dot { \mathbf { B } }$ which, after conversion to primed derivatives by (4.4), take the final form

$$
\begin{array} { r l } & { P ^ { \prime } = 2 \mathbf { R } ^ { \prime } \cdot \mathbf { F } , } \\ & { \mathbf { B } ^ { \prime } = - 2 ( \mathbf { R } ^ { \prime } \cdot \mathbf { F } ) \mathbf { R } + ( \mathbf { R } \cdot \mathbf { F } ) \mathbf { R } ^ { \prime } + ( \mathbf { R } \cdot \mathbf { R } ^ { \prime } ) \mathbf { F } . } \end{array}
$$

The resulting equations of motion are well behaved for $R \to 0$ , and twobody regularization has therefore been achieved. We also note that, in the absence of perturbations, the quantities $P$ and $\mathbf { B }$ are constants of the motion, and hence in the general case are slowly varying elements.

It remains to determine an equation for the time. By differentiating twice the identity $R ^ { 2 } = \mathbf { R } \cdot \mathbf { R }$ we obtain, by (4.47) and (4.48), the relation

$$
R ^ { \prime \prime } = P R + M + { \bf R } \cdot { \bf F } R .
$$

Higher-order terms may be constructed by further differentiation. However, since this procedure would involve derivatives of the perturbing force, it is advantageous to develop a fitting polynomial for the function (4.50) itself. Hence by (4.3) we have that

$$
t ^ { ( 3 ) } = P t ^ { \prime } + M + ( { \bf R } \cdot { \bf F } ) R .
$$

This function is well behaved near the two-body singularity. Given the first three time derivatives by explicit expressions involving $R$ and $\mathbf { R } \cdot \mathbf { F }$ , higher orders may be constructed from divided differences of (4.50) if desired. An alternative solution method is discussed in the next section.

We now turn to the interpretation of the relevant quantities. Since $P = 2 h$ , the semi-major axis is obtained from

$$
a = - M / P .
$$

In the absence of perturbations, the equation of motion (4.48) represents a displaced harmonic oscillator. The frequency is therefore twice that given by KS regularization, which is the price to pay for avoiding the coordinate transformation. From $\mathbf { R } ^ { \prime \prime } = 0$ for the centre of the orbit at ${ \bf R } _ { 0 }$ , we have $\mathbf { B } = - P \mathbf { R } _ { 0 }$ . Since $| { \bf R } _ { 0 } | = e a$ measures the distance from the centre to the focal point, $\mathbf { B }$ is related to the eccentricity vector by

$$
\mathbf { B } = - M \mathbf { e } .
$$

Here $- \mathbf { B } / M$ is sometimes known as the Runge–Lenz–Laplace vector, or alternatively it is also named after Hamilton or even Newton.

The Burdet–Heggie scheme has been used successfully for a series of three-body scattering experiments with regularization of the dominant two-body motion [Valtonen, 1974, 1975]. It was also employed for studying linearized departures from a given orbit in theoretical investigations of binary evolution [Heggie, 1975]. Finally, it is pleasing to record that this method proved itself in $N$ -body simulations of core collapse [Giersz & Heggie, 1994a,b].

# 4.6 Hermite formulation

Hermite integration also lends itself to KS regularization. Although such a scheme has been used successfully in earlier versions of the code $\ S$ NBODY 4 [Aarseth, 1996a] and the more recent NBODY 6, it has now been replaced by a more sophisticated development, to be presented in the next section. However, this method does represent an attractive alternative for some problems and will therefore be discussed here. Its simplicity also serves as a useful introduction to this approach. Before proceeding, we note that the divided difference method of section 2.2 was used to integrate the KS equations of motion since 1969 [cf. Aarseth, 1972b]. The success of the Hermite $N$ -body method [Makino, 1991b; Makino & Aarseth, 1992] soon led to a change-over in order to have a uniform treatment.

Since higher derivatives feature more prominently, we change the notation and define the regularized force (per unit mass) as $\mathbf { F } _ { \mathrm { U } } = \mathbf { U } ^ { \prime \prime }$ , with U replacing $\mathbf { u }$ to conform with the following sections. For simplicity, we also set $\mathbf { Q } = \mathcal { L } ^ { T } \mathbf { P }$ , where $\mathbf { P }$ from now on is the perturbing force (to avoid confusion with $\mathbf { F } _ { \mathrm { U } }$ ). The equations of motion (4.37) and (4.39) then take the Hermite form

$$
\begin{array} { r l } & { \mathbf { F } _ { \mathrm { U } } = \frac { 1 } { 2 } h \mathbf { U } + \frac { 1 } { 2 } R \mathbf { Q } , } \\ & { \mathbf { F } _ { \mathrm { U } } ^ { \prime } = \frac { 1 } { 2 } ( h ^ { \prime } \mathbf { U } + h \mathbf { U } ^ { \prime } + R ^ { \prime } \mathbf { Q } + R \mathbf { Q } ^ { \prime } ) , } \\ & { \quad h ^ { \prime } = 2 \mathbf { U } ^ { \prime } \cdot \mathbf { Q } , } \\ & { \quad h ^ { \prime \prime } = 2 \mathbf { F } _ { \mathrm { U } } \cdot \mathbf { Q } + 2 \mathbf { U } ^ { \prime } \cdot \mathbf { Q } ^ { \prime } , } \\ & { \quad t ^ { \prime } = \mathbf { U } \cdot \mathbf { U } , } \end{array}
$$

where the standard equation for $t ^ { \prime }$ has been included for completeness.

Once again, the energy stabilization term in (4.43) may be included. Note that the stabilization term is only added to $\mathbf { F } _ { \mathrm { U } }$ for the purpose of predicting $\mathbf { U }$ and $\mathbf { U } ^ { \prime }$ and the contribution to $\mathbf { F } _ { \mathrm { U } } ^ { \prime }$ is not included. Hence only the basic expression (4.37) is saved for further use by the integration scheme. Following the tradition of $N B O D Y 5$ , the stabilized Hermite scheme was tried with low-order prediction (i.e. up to $\mathbf { F } _ { \mathrm { U } } ^ { \prime }$ ) of the KS variables which gives rise to a fairly simple formulation. However, subsequent experience [Kokubo, Yoshinaga & Makino, 1998; Mikkola & Aarseth, 1998] showed that significant accuracy may be gained by employing higherorder prediction at the expense of some additional operations. Procedures for initialization and integration will be presented in a later section. Finally, we remark that the Burdet–Heggie scheme discussed above could be converted to Hermite form; this might be particularly beneficial for the integration of physical time.

We end this brief section by pointing out an additional equation for $R$ that does not seem to have been employed in actual KS integrations. Twice differentiation of $R = { \bf U } \cdot { \bf U }$ gives $R ^ { \prime \prime } = 2 { \bf U } ^ { \prime \prime } \cdot { \bf U } + 2 { \bf U } ^ { \prime } \cdot { \bf U } ^ { \prime }$ . Combining the equation of motion with the definition of $h$ from (4.24), we obtain the expression [cf. Bettis & Szebehely, 1972]

$$
R ^ { \prime \prime } = 2 h R + ( m _ { k } + m _ { l } ) + { \bf U } \cdot { \bf Q } R .
$$

This differential equation may be solved and used as a check on the accuracy of $R$ or substituted in the higher derivatives of $t ^ { \prime }$ .

# 4.7 Stumpff functions

The emphasis of the present chapter is on the treatment of perturbed binaries. So far, it would appear that the KS method is the ultimate tool for $N$ -body simulations but no stone must be left unturned. Numerical integration of binaries presents formidable problems, mainly because of the time-scale since millions of Kepler periods may be involved. Hence we need to search for methods that combine long-term accuracy with efficiency. In this section, we describe an alternative two-body regularization that builds on the existing KS framework and appears to have significant advantages. The basic idea of the Stumpff KS method [Mikkola $\&$ Aarseth, 1998] is to expand the solution in Taylor series, where the higher orders are modified by coefficients representing the truncated terms.

The following discussion is based on the original adaptation. For simplicity, we introduce the notation $\Omega = - h / 2$ , $\mathbf { V } = \mathbf { U } ^ { \prime }$ and ${ \bf Q } = \mathcal { L } ^ { \mathrm { T } } ( { \bf U } ) { \bf P }$ with $\mathbf { P }$ the perturbation. This allows us to write the equations of motion in the shorter form

$$
\begin{array} { r } { \mathbf { U } ^ { \prime \prime } + \Omega \mathbf { U } = \frac { 1 } { 2 } R \mathbf { Q } , \quad \quad } \\ { \Omega ^ { \prime } = - \mathbf { V } \cdot \mathbf { Q } . } \end{array}
$$

The solution for the unperturbed Keplerian case ( $\mathbf Q = 0$ ) is given by

$$
\begin{array} { r l } & { \mathbf { U } _ { \mathrm { K } } = \mathbf { U } _ { 0 } G _ { 0 } ( \Omega _ { 0 } , \tau ) + \mathbf { V } _ { 0 } G _ { 1 } ( \Omega _ { 0 } , \tau ) , } \\ & { \mathbf { V } _ { \mathrm { K } } = \mathbf { V } _ { 0 } G _ { 0 } ( \Omega _ { 0 } , \tau ) - \Omega _ { 0 } \mathbf { U } _ { 0 } G _ { 1 } ( \Omega _ { 0 } , \tau ) , } \\ & { \mathbf { \Omega } _ { t _ { \mathrm { K } } } = t _ { 0 } + R _ { 0 } \tau + 2 \mathbf { U } _ { 0 } \cdot \mathbf { V } _ { 0 } G _ { 2 } ( 4 \Omega _ { 0 } , \tau ) + M G _ { 3 } ( 4 \Omega _ { 0 } , \tau ) . } \end{array}
$$

Here the functions $G _ { n }$ are defined in Stiefel & Scheifele [1971, pp 141–143]. We have the relations

$$
G _ { n } ( \Omega , \tau ) = \tau ^ { n } c _ { n } ( \Omega \tau ^ { 2 } ) ,
$$

where

$$
c _ { n } ( z ) = \sum _ { k = 0 } ^ { \infty } { \frac { ( - z ) ^ { k } } { ( n + 2 k ) ! } }
$$

are the Stumpff [1962] functions and $z = \Omega \tau ^ { 2 }$ . It can be seen from the series expansion that these functions satisfy the recursion relation

$$
c _ { n } = { \frac { 1 } { n ! } } - z c _ { n + 2 } .
$$

This expression may be used instead of the power series to evaluate the Stumpff functions for small arguments. The choice of order is a matter for the implementation, to be discussed in a subsequent chapter, but we note here that the expansion converges fast for small $z$ .

In order to discuss the solution of (4.57), we begin by considering the perturbed harmonic oscillator

$$
{ \cal Y } ^ { \prime \prime } + \Omega { \cal Y } = g ( \tau ) ,
$$

where primes denote differentiation with respect to $\tau$ and $\Omega = - h / 2$ is the square of the frequency if $h < 0$ . We obtain a Taylor series solution with derivatives given by

$$
\begin{array} { r } { Y ^ { ( k + 2 ) } + \Omega Y ^ { ( k ) } = g ^ { ( k ) } . } \end{array}
$$

Hence if $g$ is a polynomial of at most degree $n$ , the recursion relation above for $k > n$ reduces to the trigonometric one,

$$
{ \cal Y } ^ { ( k + 2 ) } + \Omega { \cal Y } ^ { ( k ) } = 0 .
$$

With the notation $Y ^ { ( k ) }$ for the derivatives at $\tau = 0$ , the expansion for $Y$ becomes

$$
\begin{array} { l } { { \displaystyle Y = \sum _ { k = 0 } ^ { n - 2 } Y ^ { ( k ) } \frac { \tau ^ { k } } { k ! } } } \\ { { \displaystyle ~ + Y ^ { ( n - 1 ) } \left( \frac { \tau ^ { n - 1 } } { ( n - 1 ) ! } - \frac { \Omega \tau ^ { n + 1 } } { ( n + 1 ) ! } + \frac { \Omega ^ { 2 } \tau ^ { n + 3 } } { ( n + 3 ) ! } - + \dots \right) } } \\ { { \displaystyle ~ + Y ^ { ( n ) } \left( \frac { \tau ^ { n } } { n ! } - \frac { \Omega \tau ^ { n + 2 } } { ( n + 2 ) ! } + \frac { \Omega ^ { 2 } \tau ^ { n + 4 } } { ( n + 4 ) ! } - + \dots \right) . } } \end{array}
$$

The terms associated with the two highest order derivatives are the $G$ -functions defined by (4.58). Hence the Taylor series expansion of a perturbed harmonic oscillator can be made exact for an equation of the type (4.61), provided we modify the coefficients of the last two derivatives of (4.64). Extracting the common terms, we are left with a power series close to unity in each case, with the respective multiplicative factors

$$
\begin{array} { c } { { \tilde { c } _ { n - 1 } = ( n - 1 ) ! c _ { n - 1 } ( z ) , } } \\ { { \tilde { c } _ { n } = n ! c _ { n } ( z ) . } } \end{array}
$$

This enables the solution to be obtained by

$$
Y ( \tau ) = \sum _ { k = 0 } ^ { n - 2 } Y ^ { k } \frac { \tau ^ { k } } { k ! } + Y ^ { ( n - 1 ) } \frac { \tau ^ { ( n - 1 ) } } { ( n - 1 ) ! } \tilde { c } _ { n - 1 } + Y ^ { ( n ) } \frac { \tau ^ { n } } { n ! } \tilde { c } _ { n } .
$$

We now proceed to discuss the solution of the equations of motion (4.56). If polynomial approximations are formed for the right-hand sides of the equations for $\mathbf { U }$ and $\Omega$ , we can integrate the former with the above

method, while for the latter it is sufficient to use the basic polynomial because $\Omega$ is slowly varying. Hence we express the three solutions in the form

$$
\begin{array} { l } { { { \displaystyle { \bf U } = \sum _ { k = 0 } ^ { n - 2 } \frac { { \bf U } ^ { k } } { k ! } \tau ^ { k } + \frac { { \bf U } ^ { ( n - 1 ) } } { ( n - 1 ) ! } \tau ^ { n - 1 } \tilde { c } _ { n - 1 } ( z ) + \frac { { \bf U } ^ { ( n ) } } { n ! } \tau ^ { n } \tilde { c } _ { n } ( z ) } , } } \\ { { \Omega = \Omega _ { 0 } + \Omega ^ { \prime } \tau + \frac { 1 } { 2 } \Omega ^ { \prime \prime } \tau ^ { 2 } + \dots , } } \\ { { \displaystyle { \bf \Omega } t = \sum _ { k = 0 } ^ { n - 2 } \frac { t ^ { ( k ) } } { k ! } \tau ^ { k } + \frac { t ^ { ( n - 1 ) } } { ( n - 1 ) ! } \tau ^ { n - 1 } \tilde { c } _ { n - 1 } ( 4 z ) + \frac { t ^ { ( n ) } } { n ! } \tau ^ { n } \tilde { c } _ { n } ( 4 z ) } , } \end{array}
$$

where the derivatives are evaluated at $\tau = 0$ . The $\tilde { c }$ -functions obey the relations

$$
\tilde { c } _ { k } ( z ) = k ! c _ { k } ( z ) ,
$$

with $z = \Omega _ { 0 } \tau ^ { 2 }$ , and similarly for $\tilde { c } _ { k } ( 4 z )$ .

In this formulation it is more meaningful to rewrite the original equation of motion in the form

$$
\begin{array} { r } { \mathbf { U } ^ { \prime \prime } + \Omega _ { 0 } \mathbf { U } = ( \Omega _ { 0 } - \Omega ) \mathbf { U } + \frac { 1 } { 2 } R \mathbf { Q } , } \end{array}
$$

which shows that the expansion has been carried out to sufficient order when the right-hand side has converged.

This concludes the formal development of the KS integration scheme. We remark that the differential term $\Omega _ { 0 } - \Omega$ in (4.69) is reminiscent of the classical Encke’s method that solves an equation of motion for small displacements from two-body motion [cf. Brouwer & Clemence, 1961]. Algorithms for the implementation of the Stumpff KS method in an $N$ -body code will be described in a later chapter. Some aspects of KS regularization are discussed elsewhere [cf. Aarseth, 1972b, 1985, 1994, 2001c].

For completeness, we mention an original formulation that was also based on Stumpff functions [Jernigan & Porter, 1989]. Although the application employed a recursive binary tree code, the integration method was concerned with weakly perturbed two-body motion of the form (4.56). However, instead of conventional step-wise advancement of the regularized equation of motion, the solutions are expressed as polynomials in terms of Stumpff functions. A key feature is that the perturbing force acting on a binary is given by an expression that takes account of the tidal field and also its time derivative. Provided the perturbing environment of a binary changes slowly, this method allows the solution to be advanced accurately over many Kepler periods in one time-step. Given that most hard binaries in cluster simulations are weakly perturbed, this novel method could be combined with one of the other KS treatments for dealing with more rapidly varying tidal forces.

# 5 Multiple regularization

# 5.1 Introduction

In the preceding chapter, we have considered several methods for dealing with the perturbed two-body problem. Formally all these methods work for quite large perturbations, provided the regularized time-step is chosen sufficiently small. However, the selection of the dominant pair in a triple resonance interaction frequently calls for new initializations where the intruder is combined with one of the components. Likewise, one may have situations in which two hard binaries approach each other with small impact parameter. Hence a description in terms of one dominant two-body motion tends to break down during strong interactions, precisely at times when interesting outcomes are likely to occur. Since the switching of dominant components reduces the efficiency and also degrades the quality of the results, it it highly desirable to seek alternative methods for improved treatment.

In this chapter, we discuss several multiple regularization methods that have turned out to be very beneficial in practical simulations. By multiple regularization it is understood that at least two separations in a compact subsystem are subject to special treatment where the two-body singularities are removed. We begin by describing a three-body formulation that may be considered the Rosetta Stone for later developments. The generalization to more members with just one reference body is also included for completeness. A subsequent section outlines the elegant global formulation and is followed by a detailed discussion of the powerful chain regularization. We then present a method for treating binaries of arbitrarily small periods in subsystems by scaling the external perturbation. Finally, we include a new time-smoothing scheme for studying a massive binary in the presence of perturbers. All these methods are invariably somewhat technical but the end result justifies the effort.

![](images/93e45e981eb8a96d07b744af9b5423585ab1dc20b978e9fee7f3443e380c058b.jpg)  
Fig. 5.1. Three-body configuration.

# 5.2 Aarseth–Zare method

According to Whittaker [1904], the general three-body problem is the most celebrated problem in dynamical astronomy. Hence an improved numerical treatment is likely to be of considerable interest. Whereas there is a vast literature on the restricted three-body problem [Szebehely, 1967], in which one of the masses is zero, relatively little attention has been devoted to the general case. No doubt the reason for the neglect is the intractable nature of this problem, and it is only in modern times that numerical investigations have become the theoretician’s tool, requiring more sophisticated treatments.

The basic idea in the following derivation is to introduce two coupled KS regularizations. Let a general three-body configuration be described by the non-zero particle masses $m _ { 1 } , m _ { 2 } , m _ { 3 }$ , with coordinates $\tilde { \mathbf { q } } _ { k }$ and corresponding momenta $\tilde { \bf p } _ { k }$ ( $k = 1 , 2 , 3$ ). This system has the Hamiltonian

$$
\widetilde { H } = \sum _ { k = 1 } ^ { 3 } \tilde { \bf p } _ { k } ^ { 2 } / 2 m _ { k } - m _ { 1 } m _ { 3 } / R _ { 1 } - m _ { 2 } m _ { 3 } / R _ { 2 } - m _ { 1 } m _ { 2 } / R ,
$$

where the distances $R _ { k } , R$ are defined in Fig. 5.1. The corresponding equations of motion form a system of 18 first-order differential equations.

We first reduce the order by six, employing the centre-of-mass (c.m.) integrals; in other words, placing the system at rest in an inertial frame. Using the c.m. condition ${ \bf p } _ { 3 } = - ( { \bf p } _ { 1 } + { \bf p } _ { 2 } )$ , we express the kinetic energy in terms of the two independent momenta, $\mathbf { p } _ { k }$ ( $k = 1 , 2$ ), associated with the mass-points $m _ { k }$ . Likewise, from the figure, $\mathbf { q } _ { k } = \mathbf { R } _ { k }$ represents the distance vectors with respect to $m _ { 3 }$ which is known as the reference body, whereas $R = | \mathbf { R } _ { 1 } - \mathbf { R } _ { 2 } |$ . ∗ Hence the Hamiltonian simplifies to

$$
H = \sum _ { k = 1 } ^ { 2 } \frac { 1 } { 2 \mu _ { k 3 } } { \bf p } _ { k } ^ { 2 } + \frac { 1 } { m _ { 3 } } { \bf p } _ { 1 } \cdot { \bf p } _ { 2 } - m _ { 1 } m _ { 3 } / R _ { 1 } - m _ { 2 } m _ { 3 } / R _ { 2 } - m _ { 1 } m _ { 2 } / R ,
$$

where $\mu _ { k 3 } = { m _ { k } m _ { 3 } } / { ( m _ { k } + m _ { 3 } ) }$ is the reduced mass of $m _ { k }$ . Since the corresponding equations of motion describe a system with six independent coordinates, it is natural to perform regularization in eight dimensions by increasing the set of physical variables in analogy with the KS formulation. This is achieved by defining the corresponding fourth components of $\mathbf { q } _ { k } , \mathbf { p } _ { k }$ to be zero.

We now introduce a new set of canonical variables in eight dimensions, denoted by $\mathbf { Q }$ and $\mathbf { P }$ . According to the theory of canonical contact transformations, we choose a generating function $W = W ( \mathbf { p } , \mathbf { Q } )$ . This enables us to obtain the new momenta in terms of the old ones by $\mathbf { P } _ { k } = \partial W / \partial \mathbf { Q } _ { k }$ , and likewise the new coordinates by $\mathbf { q } _ { k } = \partial W / \partial \mathbf { p } _ { k }$ . At this point we follow the notation of Szebehely [1967] and adopt a separable generating function of the form

$$
W = \sum _ { k = 1 } ^ { 2 } \mathbf { p } _ { k } \cdot \mathbf { f } _ { k } ,
$$

with each $\mathbf { f } _ { k }$ a function of $\mathbf Q _ { k }$ . This crucial step yields a simple result for the two relative coordinates ( $k = 1 , 2$ ),

$$
\mathbf { q } _ { k } = \mathbf { f } _ { k } .
$$

The corresponding transformation for the momenta becomes

$$
\mathbf { P } _ { k } = \mathbf { A } _ { k } \mathbf { p } _ { k } ,
$$

where the $4 \times 4$ matrix, $\mathbf { A } _ { k }$ , is composed of terms $\partial \mathbf { f } _ { k } / \partial \mathbf { Q } _ { k }$ . From a comparison of (5.5) with the regularized velocity transformation (4.36), we see that the matrix $\mathbf { A } _ { k }$ is identical to twice the corresponding transpose of the generalized Levi-Civita matrix (4.27). However, in view of the manner in which $\mathbf { A } _ { k }$ is introduced here, $^ \dagger$ it is more natural to present the derivation based on this quantity.

Since the matrix $\mathbf { A } _ { k }$ is orthogonal, it can be shown that

$$
\mathbf { A } _ { k } \mathbf { A } _ { k } ^ { \mathrm { T } } = 4 R _ { k } \mathbf { I } ,
$$

where $\mathbf { I }$ is the identity matrix. This allows the physical momenta and relative coordinates to be recovered from standard KS transformations,

with $\mathbf { p } _ { k } ^ { 2 } = \mathbf { P } _ { k } ^ { 2 } / 4 R _ { k }$ . Let us introduce the Hamiltonian function in the extended phase space, $\Gamma = H ( \mathbf { Q } , \mathbf { P } ) - E _ { 0 }$ , where $E _ { 0 }$ is the total energy. Regularization is now achieved by employing the time transformation

$$
d t = R _ { 1 } R _ { 2 } d \tau .
$$

With $\Gamma ^ { * } = R _ { 1 } R _ { 2 } \Gamma$ , the regularized Hamiltonian takes the form

$$
\begin{array} { r } { \Gamma ^ { * } = \frac { 1 } { 8 \mu _ { 1 3 } } R _ { 2 } { \bf P } _ { 1 } ^ { 2 } + \frac { 1 } { 8 \mu _ { 2 3 } } R _ { 1 } { \bf P } _ { 2 } ^ { 2 } + \frac { 1 } { 1 6 m _ { 3 } } { \bf P } _ { 1 } ^ { \mathrm { T } } { \bf A } _ { 1 } \cdot { \bf A } _ { 2 } ^ { \mathrm { T } } { \bf P } _ { 2 } } \\ { - m _ { 1 } m _ { 3 } R _ { 2 } - m _ { 2 } m _ { 3 } R _ { 1 } - \frac { m _ { 1 } m _ { 2 } R _ { 1 } R _ { 2 } } { | { \bf R } _ { 1 } - { \bf R } _ { 2 } | } - E _ { 0 } R _ { 1 } R _ { 2 } . } \end{array}
$$

From an inspection of (5.2) one can readily identify the terms, with $\mathbf { P } _ { k } ^ { 2 } / \mu _ { k 3 }$ representing the kinetic energy of the relative two-body motions.

The corresponding equations of motion for $k = 1 , 2$ are given by

$$
\frac { d \mathbf { Q } _ { k } } { d \tau } = \frac { \partial \Gamma ^ { * } } { \partial \mathbf { P } _ { k } } , ~ \frac { d \mathbf { P } _ { k } } { d \tau } = - \frac { \partial \Gamma ^ { * } } { \partial \mathbf { Q } _ { k } } .
$$

These equations are regular for $R _ { 1 }  0$ or $R _ { 2 }  0$ since ${ \bf P } _ { k } \ \to$ const as ${ \mathbf { R } } _ { k } \ \to \ 0$ , and hence a practical regularization of the three-body problem has been achieved [Aarseth & Zare, 1974].

It may be helpful for implementations to provide the full equations of motion in explicit form. Differentiation according to the first equation (5.9) yields the straightforward result

$$
{ \frac { d \mathbf { Q } _ { k } } { d \tau } } = { \frac { 1 } { 4 \mu _ { k 3 } } } R _ { l } \mathbf { P } _ { k } + { \frac { 1 } { 1 6 m _ { 3 } } } \mathbf { A } _ { k } \mathbf { A } _ { l } ^ { \mathrm { T } } \mathbf { P } _ { l } ,
$$

where $l = 3 - k$ . Likewise, we obtain the more complicated derivative of the momentum in compact notation as

$$
\begin{array} { l } { { \displaystyle \frac { d { \bf P } _ { k } } { d \tau } = 2 \left( R _ { l } E _ { 0 } - \frac { 1 } { 8 \mu _ { l 3 } } { \bf P } _ { l } ^ { 2 } + m _ { l } m _ { 3 } + \frac { m _ { 1 } m _ { 2 } } { | { \bf R } _ { 1 } - { \bf R } _ { 2 } | } R _ { l } \right) { \bf Q } _ { k } } } \\ { { \displaystyle ~ - \frac { 1 } { 8 m _ { 3 } } { \bf P } _ { k } { \bf A } _ { l } ^ { \mathrm { T } } { \bf P } _ { l } - \frac { m _ { 1 } m _ { 2 } R _ { 1 } R _ { 2 } } { | { \bf R } _ { 1 } - { \bf R } _ { 2 } | ^ { 3 } } { \bf A } _ { k } ( { \bf R } _ { k } - { \bf R } _ { l } ) } . } \end{array}
$$

With a total of eight components, evaluation of the second equation of motion requires a considerable numerical effort. However, to compensate, the regular structure permits quite large time-steps to be used.

The time transformation (5.7) regularizes all terms in the Hamiltonian associated with the distances $R _ { 1 }$ and $R _ { 2 }$ , leaving one singularity due to the potential energy term $m _ { 1 } m _ { 2 } / R$ . After differentiation, equation (5.11) contains two singular terms involving division by $R$ and $R ^ { 3 }$ . In view of the time transformation, these terms have a different origin, with the former having a kinematical interpretation and the latter representing the dynamical interaction. From the geometry of the problem, $R \simeq R _ { 1 }$ if $R > R _ { 2 }$ and $R _ { 1 } ~ > ~ R _ { 2 }$ ; hence in most cases the inequality $R > \operatorname* { m i n } \left\{ R _ { 1 } , R _ { 2 } \right\}$ ensures that the critical terms are numerically smaller than the regularized contributions. This desirable property compensates for the divisions and is mainly responsible for the improved treatment of even close triple encounters.

On the debit side, implementation of the switching procedure requires a transformation to physical variables with consequent small loss of accuracy before assigning new particle labels, whereupon the regularized quantities are introduced. However, when the masses are different, the heaviest particle tends to dominate the motion and is a natural reference body, thereby reducing the number of switching transformations.

A comment on the role of the mass ratios may also be in order. Since the present formulation does not include the case of one massless body, a significant loss of accuracy may be anticipated for very large mass ratios; i.e. the contributions from some terms would be downgraded. Moreover, the reason for the inability to deal with one zero mass particle is due to the c.m. condition becoming indeterminate. Equivalently, the Hamiltonian is based on reciprocals of the masses. For a regular treatment of the massless body in the restricted problem see the formulation by Heggie [1974].

In order to make a connection with the standard KS formulation, it is instructive to consider the analogous Hamiltonian equations for just two particles. For this purpose we select the two-body system $m _ { 1 }$ and $m _ { 3 }$ in the expression (5.8) for $\Gamma ^ { * }$ by omitting all terms connected with $m _ { 2 }$ , as well as the distance $R _ { 2 }$ . This simplification leads to a regularized two-body Hamiltonian which was first applied by Peters [1968a,b] to the dominant interaction in the general three-body problem. Introducing the binding energy per unit reduced mass, $h = E _ { 0 } / \mu _ { 1 3 }$ and omitting subscripts, we obtain the simple expression

$$
\Gamma _ { 2 } ^ { * } = { \bf P } ^ { 2 } / 8 \mu - m _ { 1 } m _ { 3 } - \mu h { \bf Q } ^ { 2 } .
$$

The equations of motion then follow by differentiation according to (5.9), which yields

$$
\begin{array} { l } { \displaystyle { \frac { d \mathbf { Q } } { d \tau } = \mathbf { P } / 4 \mu , } } \\ { \displaystyle { \frac { d \mathbf { P } } { d \tau } = 2 \mu h \mathbf { Q } . } } \end{array}
$$

Finally, the familiar form $\mathbf { Q } ^ { \prime \prime } = { \frac { 1 } { 2 } } h \mathbf { Q }$ is obtained after introducing the regularized velocity $\mathbf { V } = \mathbf { P } / \mu$ in the second equation since the first equation implies that $\mathbf { V } = 4 \mathbf { Q } ^ { \prime }$ .

In the case of 2D problems, (5.10) and (5.11) still apply but we may use the simpler Levi-Civita matrix (4.14). Problems in 1D are ideally suited to the present formulation since no switching is needed by placing the reference body in the middle. Following Mikkola $\&$ Hietarinta [1989], we introduce three equal-mass bodies, $m _ { i } = 1$ , with coordinates $x _ { 1 } < x _ { 0 } < x _ { 2 }$ and take $q _ { 1 } = x _ { 0 } - x _ { 1 }$ , $q _ { 2 } = x _ { 2 } - x _ { 0 }$ as new relative coordinates. From the generating function $S = p _ { 1 } ( x _ { 0 } - x _ { 1 } ) + p _ { 2 } ( x _ { 2 } - x _ { 0 } )$ , with momenta $p _ { i }$ , the new Hamiltonian becomes

$$
H = p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } - p _ { 1 } p _ { 2 } - \frac { 1 } { q _ { 1 } } - \frac { 1 } { q _ { 2 } } - \frac { 1 } { q _ { 1 } + q _ { 2 } } .
$$

If we adopt the coordinate transformation $q _ { 1 } = Q _ { 1 } ^ { 2 }$ , $q _ { 2 } = Q _ { 2 } ^ { 2 }$ , the new generating function gives rise to the momenta $P _ { i } = 2 Q _ { i } p _ { i }$ . Combined with the time transformation $t ^ { \prime } = q _ { 1 } q _ { 2 }$ , this yields the regularized Hamiltonian $\Gamma ^ { * } = q _ { 1 } q _ { 2 } ( H - E )$ . Thus in explicit form

$$
\Gamma ^ { * } = { \textstyle \frac { 1 } { 4 } } ( { \cal P } _ { 1 } ^ { 2 } Q _ { 2 } ^ { 2 } + { \cal P } _ { 2 } ^ { 2 } Q _ { 1 } ^ { 2 } - { \cal P } _ { 1 } { \cal P } _ { 2 } Q _ { 1 } Q _ { 2 } ) - Q _ { 1 } ^ { 2 } - Q _ { 2 } ^ { 2 } - \frac { Q _ { 1 } ^ { 2 } Q _ { 2 } ^ { 2 } } { Q _ { 1 } ^ { 2 } + Q _ { 2 } ^ { 2 } } - Q _ { 1 } ^ { 2 } Q _ { 2 } ^ { 2 } { \cal E } ,
$$

which results in simple equations of motion. Note that the divisor represents the sum of the two distances and is therefore optimal. For data analysis or movie making, the coordinates $x _ { 1 }$ , $x _ { 2 }$ are obtained from substituting the c.m. relation $\begin{array} { r } { x _ { 0 } = \frac { 1 } { 3 } ( q _ { 1 } - q _ { 2 } ) } \end{array}$ . The relative velocities are determined by $\dot { q } _ { i } = { \partial H } / { \partial p _ { i } }$ , combined with the c.m. condition $\begin{array} { r } { \dot { x } _ { 0 } = \frac { 1 } { 3 } ( \dot { q } _ { 1 } - \dot { q } _ { 2 } ) } \end{array}$ , whereas (5.14) can be used for the energy check. A formulation for unequal masses is given by Mikkola $\&$ Hietarinta [1991]. The corresponding Hamiltonian looks similar to the form (5.8), if we note the factor 2 in the definition of $\mathbf { A } _ { k }$ and take account of the reverse sign in the third term due to the different generating function.

To conform with the present style, a discussion of practical details such as decision-making will be postponed to a later section. Next we provide a complete summary of the relevant transformations. Given the initial relative coordinates, $\mathbf q _ { k }$ , and momenta, $\mathbf { p } _ { k }$ , if $q _ { 1 } \geq 0$ the regularized coordinates for the first two-body motion are specified by

$$
\begin{array} { l } { { Q _ { 1 } = [ \frac { 1 } { 2 } ( | { \bf q } _ { 1 } | + q _ { 1 } ) ] ^ { 1 / 2 } , } } \\ { { Q _ { 2 } = \frac { 1 } { 2 } q _ { 2 } / Q _ { 1 } , } } \\ { { Q _ { 3 } = \frac { 1 } { 2 } q _ { 3 } / Q _ { 1 } , } } \\ { { Q _ { 4 } = 0 , } } \end{array}
$$

otherwise the appropriate choice is taken to be

$$
\begin{array} { r } { Q _ { 2 } = [ \frac { 1 } { 2 } ( | { \bf q } _ { 1 } | - q _ { 1 } ) ] ^ { 1 / 2 } , } \end{array}
$$

$$
\begin{array} { r c l } { { } } & { { } } & { { Q _ { 1 } = \frac { 1 } { 2 } q _ { 2 } / Q _ { 2 } , } } \\ { { } } & { { } } & { { Q _ { 3 } = 0 , } } \\ { { } } & { { } } & { { Q _ { 4 } = \frac { 1 } { 2 } q _ { 3 } / Q _ { 2 } . } } \end{array}
$$

Likewise, the regularized momenta are given by (5.5). Because of the redundant fourth components of physical coordinates and momenta, numerical work only requires the $4 \times 3$ submatrix of $\mathbf { A } _ { k }$ , which for $k = 1$ takes the complete form

$$
{ \bf A } _ { 1 } = 2 \left[ \begin{array} { r r r r } { { Q _ { 1 } } } & { { Q _ { 2 } } } & { { Q _ { 3 } } } & { { Q _ { 4 } } } \\ { { - Q _ { 2 } } } & { { Q _ { 1 } } } & { { Q _ { 4 } } } & { { - Q _ { 3 } } } \\ { { - Q _ { 3 } } } & { { - Q _ { 4 } } } & { { Q _ { 1 } } } & { { Q _ { 2 } } } \\ { { Q _ { 4 } } } & { { - Q _ { 3 } } } & { { Q _ { 2 } } } & { { - Q 1 } } \end{array} \right] .
$$

Inverse transformations yield the physical variables. Thus the relative coordinates, denoted by ${ \bf R } _ { k }$ ( $k = 1 , 2$ ) in Fig. 5.1, are obtained from

$$
\begin{array} { r } { { \bf q } _ { k } = \frac 1 2 { \bf A } _ { k } ^ { \mathrm { T } } { \bf Q } _ { k } , } \end{array}
$$

which reproduces the well-known KS transformations, whereas the momenta are inverted by (5.5) and (5.6) according to

$$
\begin{array} { r } { \mathbf p _ { k } = \frac { 1 } { 4 } \mathbf A _ { k } ^ { \mathrm { T } } \mathbf P _ { k } / R _ { k } . } \end{array}
$$

Corresponding relations for the second KS pair are derived in a similar way. Finally, the coordinates and momenta expressed in the local c.m. frame are recovered from

$$
\begin{array} { l } { { \displaystyle { \tilde { \bf q } } _ { 3 } = - \sum _ { k = 1 } ^ { 2 } m _ { k } { \bf q } _ { k } / M } , } \\ { { } } \\ { { \displaystyle { \tilde { \bf q } } _ { k } = { \tilde { \bf q } } _ { 3 } + { \bf q } _ { k } } , } \\ { { \displaystyle { \tilde { \bf p } } _ { k } = { \bf p } _ { k } , } } \\ { { \displaystyle { \tilde { \bf p } } _ { 3 } = - ( { \bf p } _ { 1 } + { \bf p } _ { 2 } ) } , \qquad ( k = 1 , 2 ) } \end{array}
$$

where $M = m _ { 1 } + m _ { 2 } + m _ { 3 }$

The time transformation (5.7) employed above is not unique and several alternatives have been examined [Aarseth, 1976]. One such case is the choice of the inverse potential energy using $t ^ { \prime } = - 1 / \Phi$ , which gives rise to the explicit relation for the time [Baumgarte $\&$ Stiefel, 1974] by

$$
t = - ( \tau + C ) / 2 E _ { 0 } + \sum _ { i = 1 } ^ { 3 } \mathbf { r } _ { i } \cdot \mathbf { p } _ { i } / 2 E _ { 0 } .
$$

Here the coordinates and momenta are expressed in the c.m. frame and the constant $C$ is determined initially, when $\tau = 0$ . Utilization of the

regularized variables developed above, together with the condition (5.6), results in the final regular expression (excepting $E _ { 0 } = 0$ )

$$
t = - ( \tau + C ) / 2 E _ { 0 } + \sum _ { k = 1 } ^ { 2 } \mathbf { Q } _ { k } ^ { \mathrm { T } } \mathbf { P } _ { k } / 4 E _ { 0 } .
$$

A change of time transformation requires the equations of motion to be modified. Taking the cue from (5.7), we write

$$
d t = g _ { 1 } g _ { 2 } d \tau ,
$$

with $g _ { 1 } = R _ { 1 } R _ { 2 }$ . Consequently, the potential energy formulation gives

$$
g _ { 2 } = ( m _ { 1 } m _ { 3 } R _ { 2 } + m _ { 2 } m _ { 3 } R _ { 1 } + m _ { 1 } m _ { 2 } R _ { 1 } R _ { 2 } / R ) ^ { - 1 } .
$$

We absorb $g _ { 1 }$ in the definition of $\Gamma ^ { * }$ which gives rise to the new equations of motion

$$
\begin{array} { l } { \displaystyle \frac { d \mathbf { Q } _ { k } } { d \tau } = g _ { 2 } \frac { \partial \Gamma ^ { * } } { \partial \mathbf { P } _ { k } } , } \\ { \displaystyle \frac { d \mathbf { P } _ { k } } { d \tau } = - g _ { 2 } \frac { \partial \Gamma ^ { * } } { \partial \mathbf { Q } _ { k } } - \Gamma ^ { * } \frac { \partial g _ { 2 } } { \partial \mathbf { Q } _ { k } } . } \end{array}
$$

The existence of an improper integral for the time if both the distances $R _ { 1 }$ and $R _ { 2 }$ approach zero together has prompted yet another time transformation, given by $g _ { 2 } = ( R _ { 1 } + R _ { 2 } ) ^ { - 1 / 2 }$ . Thus the property that $t ^ { \prime } \propto R ^ { 3 / 2 }$ near triple collisions represents the limiting case for convergence. Actual experiments show that this choice of time transformation may give better results in practice, together with the condition $\Gamma ^ { * } = 0$ [Aarseth, 1976], but $g _ { 2 } = ( R _ { 1 } + R _ { 2 } ) ^ { - 1 }$ also merits attention. Note that in the original formulation, with $g _ { 1 } = R _ { 1 } R _ { 2 }$ , this procedure is not justified since regularity of the equations is lost. Finally, equations of motion for the more recently suggested time transformation $t ^ { \prime } = 1 / L$ can be readily constructed [cf. Alexander, 1986; Appendix B] and deserves consideration.

# 5.3 External perturbations

The above method may also be used to study close encounters between binaries and single particles that occur in $N$ -body simulations. In this case we need to include the effect of the external particles in the equations of motion, unless the unperturbed approximation is assumed. Consider a system of $N$ particles and three mass-points $m _ { i }$ with corresponding coordinates $\mathbf { r } _ { i }$ which form a subsystem to be regularized. Consequently, we write the regularized Hamiltonian as

$$
\Gamma ^ { * } = R _ { 1 } R _ { 2 } ( H _ { 3 } + \mathscr { R } - E ) ,
$$

where $H _ { 3 }$ is given by (5.1), $\mathcal { R }$ is the perturbing function expressed in terms of the physical variables $\mathbf { r }$ and $\mathbf { p }$ , and $E$ is the total energy. Since $\mathcal { R }$ does not depend on the momenta $\mathbf { P } _ { k }$ , the new equations of motion for $k = 1 , 2$ take the form

$$
\begin{array} { r l } & { \displaystyle \frac { d \mathbf { Q } _ { k } } { d \tau } = \frac { \partial ( R _ { 1 } R _ { 2 } H _ { 3 } ) } { \partial \mathbf { P } _ { k } } , } \\ & { \displaystyle \frac { d \mathbf { P } _ { k } } { d \tau } = - ( H _ { 3 } - E _ { 3 } ) \frac { \partial ( R _ { 1 } R _ { 2 } ) } { \partial \mathbf { Q } _ { k } } - R _ { 1 } R _ { 2 } \frac { \partial } { \partial \mathbf { Q } _ { k } } ( H _ { 3 } + \mathcal { R } ) , } \end{array}
$$

where $E _ { 3 } = E - \mathcal { R }$ is the subsystem energy.

For the present purpose we need only consider the external potential energy part of $_ { \mathcal { R } }$ , since the kinetic energy of the subsystem is treated independently. Hence we obtain the desired perturbation term from

$$
{ \frac { \partial { \mathcal { R } } } { \partial \mathbf { Q } _ { k } } } = \sum _ { i = 1 } ^ { 3 } { \frac { \partial { \mathcal { R } } } { \partial \mathbf { r } _ { i } } } { \frac { \partial \mathbf { r } _ { i } } { \partial \mathbf { q } _ { k } } } { \frac { \partial \mathbf { q } _ { k } } { \partial \mathbf { Q } _ { k } } } .
$$

Explicit differentiation yields the perturbing force

$$
\partial { \mathcal R } / \partial { \bf r } _ { i } = - m _ { i } { \bf F } _ { i } ,
$$

where $\mathbf { F } _ { i }$ is defined by

$$
\mathbf { F } _ { i } = - \sum _ { j = 4 } ^ { N } \frac { m _ { j } ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) } { \vert \mathbf { r } _ { i } - \mathbf { r } _ { j } \vert ^ { 3 } } . \qquad ( i = 1 , 2 , 3 )
$$

The actual coordinates are required for several purposes when studying a perturbed subsystem. Thus from (5.21) and the subsystem c.m. condition $\mathbf { r } _ { 0 } = \sum m _ { i } \mathbf { r } _ { i } / M$ we obtain the explicit conversion formulae

$$
\begin{array} { r l } & { { \bf r } _ { 1 } = { \bf r } _ { 0 } + ( m _ { 2 } + m _ { 3 } ) { \bf q } _ { 1 } / M - m _ { 2 } { \bf q } _ { 2 } / M , } \\ & { { \bf r } _ { 2 } = { \bf r } _ { 0 } - m _ { 1 } { \bf q } _ { 1 } / M + ( m _ { 1 } + m _ { 3 } ) { \bf q } _ { 2 } / M , } \\ & { { \bf r } _ { 3 } = { \bf r } _ { 0 } - m _ { 1 } { \bf q } _ { 1 } / M - m _ { 2 } { \bf q } _ { 2 } / M . } \end{array}
$$

Hence the expressions for $\partial \mathbf { r } _ { i } / \partial \mathbf { q } _ { k }$ simplify to mass ratios. From the basic transformation (5.19) it follows that

$$
\partial { \bf q } _ { k } / \partial { \bf Q } _ { k } = { \bf A } _ { k } .
$$

Finally, combining all the terms results in

$$
\partial \mathcal { R } / \partial \mathbf { Q } _ { k } = - \mathbf { A } _ { k } [ m _ { 1 } m _ { 2 } ( \mathbf { F } _ { 2 } - \mathbf { F } _ { 1 } ) ( - 1 ) ^ { k } + m _ { k } m _ { 3 } ( \mathbf { F } _ { k } - \mathbf { F } _ { 3 } ) ] / M .
$$

We remark that differential (or tidal) accelerations appear. Hence only contributions from relatively nearby perturbers need to be taken into account in the summation (5.32), in analogy with standard KS.

It remains to derive an expression for the energy that is affected by the perturbations. From $E _ { 3 } = E - \mathcal { R }$ , the internal energy change is

$$
d E _ { 3 } / d \tau = - d \mathcal { R } / d \tau .
$$

Consequently, we can also use (5.35) to evaluate $E _ { 3 } ^ { \prime }$ because

$$
\frac { d \mathcal { R } } { d \tau } = \sum _ { k = 1 } ^ { 2 } \frac { \partial \mathcal { R } } { \partial \mathbf { Q } _ { k } } \frac { d \mathbf { Q } _ { k } } { d \tau } .
$$

Substituting for the equation of motion (5.10) combined with the expression (5.35) and employing the orthogonality condition $\mathbf { A } _ { k } \mathbf { A } _ { k } ^ { \mathrm { T } } = 4 R _ { k }$ , we finally arrive at the desired equation

$$
\frac { d \mathcal { R } } { d \tau } = - \frac { 1 } { 4 } \sum _ { k = 1 } ^ { 2 } R _ { l } \mathbf { P } _ { k } ^ { \mathrm { T } } \mathbf { A } _ { k } ( \mathbf { F } _ { k } - \mathbf { F } _ { 3 } ) .
$$

Hence when external perturbations are included, the energy, $E _ { 3 }$ , needs to be updated in a consistent manner for use in (5.29). On the other hand, (5.28) does not contain the external potential. Since the perturbers are advanced separately, the total energy is a sum of two independent terms and can therefore still be used as a check.

This concludes the formal development of the basic three-body regularization. Practical matters relating to code implementation and applications will be discussed in a subsequent chapter.

# 5.4 Wheel-spoke generalization

The concept of a parallel regularization with respect to one reference body was extended to an arbitrary membership by Zare [1974] at the same time as the method discussed above was developed. This method only appears to have been tried in a binary–binary scattering experiment [Alexander, 1986]. However, since the verdict was favourable and applications to stellar systems with a central black hole seem relevant, the essential points will be presented here. As shown by Fig. 5.2, the generalization to larger systems conjures up the image of a wheel-spoke and we shall employ this name here in the absence of a recognized alternative.

The basic formulation starts with the Hamiltonian for a system of $N { + 1 }$ particles containing a subsystem of $n + 1$ members. Let the generalized coordinates and momenta be denoted by $\tilde { \mathbf { q } } _ { i }$ and $\tilde { \bf p } _ { i }$ , with $R _ { i j } = | \tilde { \bf q } _ { i } - \tilde { \bf q } _ { j } |$ representing the inter-particle distances. As before, we reduce the order by employing the six c.m. integrals. Accordingly, the coordinates and momenta are redefined with respect to the reference body, $m _ { 0 }$ , such that ${ \bf q } _ { 0 }$ and $\mathbf { p } _ { 0 }$ are the corresponding position and momentum. The transformation is achieved by the generating function

![](images/02ef2db2645a657c704d502f033e36c7ea55c2d9a30ca0936193e184876f7c2e.jpg)  
Fig. 5.2. Wheel-spoke geometry.

$$
W ( \mathbf { q } _ { i } , \tilde { \mathbf { p } } _ { i } ) = \sum _ { i = 1 } ^ { N } \tilde { \mathbf { p } } _ { i } \cdot \mathbf { q } _ { i } + \left( \sum _ { i = 0 } ^ { N } \tilde { \mathbf { p } } _ { i } \right) \cdot \mathbf { q } _ { 0 } .
$$

Since the reduced Hamiltonian has ${ \bf q } _ { 0 }$ as an ignorable coordinate, we can set $\mathbf p _ { 0 } = 0$ for the c.m. The Hamiltonian then takes the form

$$
H = \sum _ { i = 1 } ^ { N } \frac { { \bf p } _ { i } ^ { 2 } } { 2 \mu _ { i } } + \frac { 1 } { m _ { 0 } } \sum _ { i < j } ^ { N } { \bf p } _ { i } ^ { \mathrm { T } } \cdot { \bf p } _ { j } - m _ { 0 } \sum _ { i = 1 } ^ { N } \frac { m _ { i } } { R _ { i } } - \sum _ { i < j } ^ { N } \frac { m _ { i } m _ { j } } { R _ { i j } } ,
$$

where $\mu _ { i } = m _ { i } m _ { 0 } / ( m _ { i } + m _ { 0 } )$ and $R _ { i } = | \mathbf { q } _ { i } |$ .

The system is divided into two subsystems, with masses $I I l _ { 1 } , I I l _ { 2 } , \ldots , I I l _ { n }$ in the first one which will be considered for special treatment. The regularization procedure itself is quite similar to the three-body case, and in practice the local Hamiltonian is used instead of (5.40). We introduce $n$ canonical variables $\mathbf { Q } _ { i }$ and $\mathbf { P } _ { i }$ and write the generating function

$$
W ( \mathbf { p } _ { i } , \mathbf { Q } _ { i } ) = \sum _ { i = 1 } ^ { N } \mathbf { p } _ { i } ^ { \mathrm { T } } \cdot \mathbf { f } _ { i } ( \mathbf { Q } _ { i } ) ,
$$

where $\mathbf { f } _ { i } ( \mathbf { Q } _ { i } )$ represents KS coordinates for $\textit { i } \leq n$ . The corresponding regularized momenta are obtained by

$$
\mathbf { P } _ { i } = \mathbf { A } _ { i } \mathbf { p } _ { i } , \qquad ( i = 1 , \ldots , n )
$$

where the matrix $\mathbf { A } _ { i }$ is defined by (5.18) in the usual way. Moreover, the coordinates and momenta for the remaining system are simply taken as ${ \bf Q } _ { i } = { \bf q } _ { i }$ and $\mathbf { P } _ { i } ~ = ~ \mathbf { p } _ { i }$ . Thus the new Hamiltonian consists of two parts, where the equations of motion for $i ~ > ~ n$ are of standard form. By analogy with the preceding section, an additional equation can be derived for the change in the energy of the regularized subsystem due to the perturbations, instead of using the original explicit formulation based on a time-consuming summation if $N$ is large.

A variety of time transformations are available here, as discussed in the original paper. However, from systematic comparisons of binary–binary scattering experiments [Alexander, 1986] it appears that the inverse Lagrangian (i.e. $d t = d \tau / L$ ) is the best choice in practice. The latter form is also simple to implement and, as discussed below, has been found advantageous in other multiple regularizations. With a suitable time transformation, the equations of motion are regular and permit $R _ { i } \to 0$ for all the $n$ spokes.

For completeness, the relevant transformations are summarized here. Given the initial conditions $m _ { i } , { \tilde { \mathbf { q } } } _ { i } , { \tilde { \mathbf { p } } } _ { i }$ , the relative coordinates and absolute momenta are defined by

$$
\begin{array} { r c l } { { } } & { { } } & { { { \bf q } _ { i } = \tilde { { \bf q } } _ { i } - \tilde { { \bf q } } _ { N } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { { \bf p } _ { i } = \tilde { { \bf p } } _ { i } , } } \end{array}
$$

with $i = 1 , 2 , \dots , N$ . The standard KS coordinate transformations apply for $i \leq n$ , whereas for $i > n$ we use the physical coordinates with respect to $m _ { 0 }$ . Likewise, the regularized momenta are obtained from (5.42). Inverse transformations yield the physical coordinates

$$
\begin{array} { l l } { { { \bf q } _ { i } = \frac { 1 } { 2 } { \bf A } _ { i } ^ { \mathrm { T } } { \bf Q } _ { i } , \qquad } } & { { ( i = 1 , 2 , \dots , n ) } } \\ { { { \bf q } _ { i } = { \bf Q } _ { i } , \qquad } } & { { ( i = n + 1 , \dots , N ) } } \end{array}
$$

and corresponding momenta

$$
\begin{array} { l l } { { { \bf p } _ { i } = \frac { 1 } { 4 } { \bf A } _ { i } ^ { \mathrm { T } } { \bf P } _ { i } / R _ { i } , } } & { { ( i = 1 , 2 , \dots , n ) } } \\ { { { \bf p } _ { i } = { \bf P } _ { i } . } } & { { ( i = n + 1 , \dots , N ) } } \end{array}
$$

The final coordinates and momenta are then obtained from

$$
\begin{array} { l } { { \displaystyle { \tilde { \bf q } } _ { 0 } = \sum _ { i = 1 } ^ { N } m _ { i } { \bf q } _ { i } / \sum _ { i = 0 } ^ { N } m _ { i } } , } \\ { { \displaystyle { \tilde { \bf q } } _ { i } = { \tilde { \bf q } } _ { 0 } + { \bf q } _ { i } } , } \\ { { \displaystyle { \tilde { \bf p } } _ { i } = { \bf p } _ { i } , \quad ( i = 1 , 2 , \ldots , N ) } } \\ { { \displaystyle { \tilde { \bf p } } _ { 0 } = - \sum _ { i = 1 } ^ { N } { \bf p } _ { i } . } } \end{array}
$$

One can envisage several ways of using the wheel-spoke regularization. However, in order to be efficient, the reference body should contain most of the mass of the regularized subsystem. An attractive feature of this formulation is that no switching of the reference body may be required if this condition is fulfilled. One possible new application would be to a central dominant black hole system, where the closest stars would constitute the regularized part with the external members advanced by (say) the selfconsistent field method [Hernquist & Ostriker, 1992]. Such a treatment would permit changes of membership due to collisions and boundary crossings. The method also lends itself to studying collisions in small systems (i.e. $n = N$ ). In either case, the solutions might be advanced by an individual time-step scheme to speed up the calculation, or the Bulirsch–Stoer [1966] integrator for increased accuracy. Although dominant motions can be integrated more accurately when regularized, any applications to planetary simulations are probably best carried out with the time-symmetric method [Kokubo, Yoshinaga & Makino, 1998] discussed in section 2.7.

# 5.5 Heggie’s global formulation

Although highly efficient, the three-body development discussed above lacks the property of symmetry between the particles. This treatment was extended to a global formulation by Heggie [1974] whose derivation will be followed closely for the case $N \ : = \ : 3$ . A somewhat complicated generalization to $N > 3$ is also available but for practical purposes the reformulation of Mikkola [1984a, 1985a] is preferable.

We begin with a Hamiltonian of the form (5.1) but adopt slightly different notation. Let $\tilde { \mathbf { q } } _ { i } ( i = 1 , 2 , 3$ ) be the Cartesian coordinates in an inertial frame and $\tilde { \bf p } _ { i }$ the conjugate momenta. The Hamiltonian then takes the symmetrical form

$$
\tilde { H } = \sum _ { i = 1 } ^ { 3 } { \tilde { \bf p } } _ { k } ^ { 2 } / 2 m _ { i } - m _ { 2 } m _ { 3 } / | \tilde { \bf q } _ { 2 } - \tilde { \bf q } _ { 3 } | - m _ { 3 } m _ { 1 } / | \tilde { \bf q } _ { 3 } - \tilde { \bf q } _ { 1 } | - m _ { 1 } m _ { 2 } / | \tilde { \bf q } _ { 1 } - \tilde { \bf q } _ { 2 } |
$$

We consider the solution of the corresponding Hamiltonian equations

$$
\begin{array} { r l r l } & { \dot { \tilde { \bf { q } } } _ { 1 } = \tilde { \bf { p } } _ { i } / m _ { i } , } & & { ( i = 1 , 2 , 3 ) } \\ & { \dot { \tilde { \bf { p } } } _ { 1 } = - \frac { m _ { 1 } m _ { 2 } \left( \tilde { \bf { q } } _ { 1 } - \tilde { \bf { q } } _ { 2 } \right) } { \vert \tilde { \bf { q } } _ { 1 } - \tilde { \bf { q } } _ { 2 } \vert ^ { 3 } } - \frac { m _ { 1 } m _ { 3 } \left( \tilde { \bf { q } } _ { 1 } - \tilde { \bf { q } } _ { 3 } \right) } { \vert \tilde { \bf { q } } _ { 1 } - \tilde { \bf { q } } _ { 3 } \vert ^ { 3 } } , } & & { ( * ) } \end{array}
$$

where the asterisk indicates two similar equations by cyclic interchange of indices.

In the following we assume for simplicity that the c.m. is at rest. Let us define the relative distance vectors

$$
{ \bf q } _ { 1 } = \tilde { \bf q } _ { 2 } - \tilde { \bf q } _ { 3 } . \mathrm { ~  ~ \Gamma ~ } ( * )
$$

From this symmetrical definition we see that the meaning of the associated distances, $R _ { i }$ , is reversed from that of Fig. 5.1. We now introduce new momenta satisfying the relation

$$
\tilde { \mathbf { p } } _ { i } = \sum _ { j = 1 } ^ { 3 } \mathbf { p } _ { j } ^ { \mathrm { T } } \partial \mathbf { q } _ { j } / \partial \tilde { \mathbf { q } } _ { i } .
$$

By (5.49) this simplifies to

$$
\tilde { \bf p } _ { 1 } = - { \bf p } _ { 2 } + { \bf p } _ { 3 } . \mathrm { ~  ~ \Gamma ~ } ( * )
$$

Substitution of (5.49) and (5.51) into (5.47) yields the new Hamiltonian

$$
\begin{array} { r l } & { H = \frac { { \bf p } _ { 1 } ^ { 2 } } { 2 \mu _ { 2 3 } } + \frac { { \bf p } _ { 2 } ^ { 2 } } { 2 \mu _ { 3 1 } } + \frac { { \bf p } _ { 3 } ^ { 2 } } { 2 \mu _ { 1 2 } } - \left( \frac { { \bf p } _ { 2 } ^ { \mathrm { T } } { \bf p } _ { 3 } } { m _ { 1 } } + \frac { { \bf p } _ { 3 } ^ { \mathrm { T } } { \bf p } _ { 1 } } { m _ { 2 } } + \frac { { \bf p } _ { 1 } ^ { \mathrm { T } } { \bf p } _ { 2 } } { m _ { 3 } } \right) } \\ & { \quad \quad - \frac { m _ { 2 } m _ { 3 } } { q _ { 1 } } - \frac { m _ { 3 } m _ { 1 } } { q _ { 2 } } - \frac { m _ { 1 } m _ { 2 } } { q _ { 3 } } , } \end{array}
$$

where $q _ { i } = | \mathbf { q } _ { i } |$ and $\mu _ { i j } = { m _ { i } m _ { j } } / { ( m _ { i } + m _ { j } ) }$ . This gives rise to the equations of motion

$$
\begin{array} { r l } & { { \dot { \bf q } } _ { 1 } = { \bf p } _ { 1 } / \mu _ { 2 3 } - { \bf p } _ { 3 } / m _ { 2 } - { \bf p } _ { 2 } / m _ { 3 } , } \\ & { { \dot { \bf p } } _ { 1 } = - m _ { 2 } m _ { 3 } { \bf q } _ { 1 } / q _ { 1 } ^ { 3 } . } \end{array}
$$

Explicit relations for ${ \bf q } _ { i }$ and $\mathbf { p } _ { i }$ are recovered by similar expressions to those in the previous section and other quantities have the usual meaning.

As above, there is considerable freedom in the choice of time transformations. In the first instance, we adopt the basic relation

$$
d t = R _ { 1 } R _ { 2 } R _ { 3 } d \tau .
$$

Denoting the new Hamiltonian by $\widetilde { H } ( \mathbf { Q } _ { i } , \mathbf { P } _ { i } )$ , we write as before

$$
\Gamma ^ { * } = { \cal R } _ { 1 } { \cal R } _ { 2 } { \cal R } _ { 3 } ( \tilde { \cal H } - E _ { 0 } ) ,
$$

where $E _ { 0 }$ is the numerical value of $\tilde { H }$ along the solution path. From the definition of $\tilde { H }$ , the final regularized Hamiltonian becomes

$$
\begin{array} { l }  { { \Gamma ^ { * } = { \frac { 1 } { 8 } } \left( { \frac { R _ { 2 } R _ { 3 } } { \mu _ { 2 3 } } } { \bf P } _ { 1 } ^ { \mathrm { T } } { \bf P } _ { 1 } + { \frac { R _ { 3 } R _ { 1 } } { \mu _ { 3 1 } } } { \bf P } _ { 2 } ^ { \mathrm { T } } { \bf P } _ { 2 } + { \frac { R _ { 1 } R _ { 2 } } { \mu _ { 1 2 } } } { \bf P } _ { 3 } ^ { \mathrm { T } } { \bf P } _ { 3 } \right) } } \end{array}
$$

Again the corresponding equations of motion are obtained from the usual expressions (5.9). Differentiation leads to considerable simplification and

it can be seen that the resulting equations are regular for collisions between any particle pair.

Alternative time transformations may also be tried here. By analogy with the preceding section, the choice

$$
g _ { 2 } = ( R _ { 1 } + R _ { 2 } + R _ { 3 } ) ^ { - 3 / 2 }
$$

leads to regularized equations with the desirable asymptotic behaviour. The modified equations of motion for $i = 1 , 2 , 3$ then take the form

$$
\begin{array} { l }  { \displaystyle { \frac { d \mathbf { Q } _ { i } } { d \tau } = g _ { 2 } \frac { \partial \Gamma ^ { * } } { \partial \mathbf { P } _ { i } } , } } \\  { \displaystyle { \frac { d \mathbf { P } _ { i } } { d \tau } = - g _ { 2 } \left[ \frac { \partial \Gamma ^ { * } } { \partial \mathbf { Q } _ { i } } - \frac { 3 } { 2 } \Gamma ^ { * } \frac { \partial } { \partial \mathbf { Q } _ { i } } \ln ( R _ { 1 } + R _ { 2 } + R _ { 3 } ) \right] . } } \end{array}
$$

It has been found [Heggie, 1974] that setting $\Gamma ^ { * } = 0$ introduces unstable modes as triple collision is approached. This behaviour is connected with the modified time transformation where growing modes are present without the last term in the momentum equation, which has a stabilizing effect. However, the additional complications introduced by (5.57) may be avoided for less extreme configurations if a lower limit on the system size for non-zero angular momentum can be estimated.

By analogy with the treatment of section 5.3, the global formulation has been extended to the perturbed three-body problem [Heggie, 1974]. This formulation does not appear to have been implemented in any existing $N$ -body code and is given at the end of Appendix A.

# 5.6 Mikkola’s derivation

The previous development was also generalized to arbitrary memberships [Heggie, 1974]. Since this treatment involves a total of $4 N ( N - 1 ) + 1$ equations, the complexity increases rapidly with $N$ , especially as the right-hand side of the second member (5.9) also grows faster than $N$ . The complications of the original formulation are such that $N = 4$ already represents a formidable challenge to the practitioner. Given the importance of binary–binary interactions in star cluster simulations, we therefore present a simpler derivation due to Mikkola [1984a, 1985a] which is easier to implement. This task is accomplished by employing a modified notation while retaining the essential features.

We begin by writing the Hamiltonian in terms of the physical coordinates and momenta,

$$
H = \sum _ { i = 1 } ^ { N } \frac { { \bf w } _ { i } ^ { 2 } } { 2 m _ { i } } - \sum _ { i = 1 } ^ { N - 1 } \sum _ { j = i + 1 } ^ { N } \frac { m _ { i } m _ { j } } { | { \bf r } _ { i } - { \bf r } _ { j } | } .
$$

Let $\mathbf { q } _ { i j } = \mathbf { r } _ { i } - \mathbf { r } _ { j }$ be the new coordinates and define new momenta by

$$
\mathbf { w } _ { i } = \sum _ { j = i + 1 } ^ { N } \mathbf { p } _ { i j } - \sum _ { j = 1 } ^ { i - 1 } \mathbf { p } _ { j i } .
$$

This transformation introduces $N ( N - 1 ) / 2$ fictitious particles. A direct substitution shows that a solution of (5.60) is given by

$$
\mathbf { p } _ { i j } = ( \mathbf { w } _ { i } - \mathbf { w } _ { j } ) / N .
$$

In order to achieve a simpler notation, we now replace the double indices by a single running index, $k$ . Thus henceforth we work with ${ \bf q } _ { k } , { \bf p } _ { k }$ , where $k = ( i - 1 ) N - i ( i + 1 ) / 2 + j$ for $\textit { i } < \textit { j }$ is a 1D array that contains $K = N ( N - 1 ) / 2$ members. This enables (5.60) to be expressed as

$$
{ \bf w } _ { i } = \sum _ { k = 1 } ^ { K } a _ { i k } { \bf p } _ { k } ,
$$

where by definition $a _ { i k } = 1$ and $a _ { j k } = - 1$ when $k = k ( i , j )$ and zero otherwise. We define the mass products $M _ { k } = m _ { i } m _ { j }$ . The new Hamiltonian then takes the form

$$
H = \sum _ { u , v = 1 } ^ { K } T _ { u v } \mathbf { p } _ { u } \cdot \mathbf { p } _ { v } - \sum _ { k = 1 } ^ { K } M _ { k } / q _ { k } ,
$$

where the matrix elements are given by

$$
T _ { u v } = { \textstyle \frac { 1 } { 2 } } \sum _ { e = 1 } ^ { N } a _ { e u } a _ { e v } / m _ { e } . \quad ( u = 1 , \ldots , K ) \quad ( v = 1 , \ldots , K )
$$

The standard KS transformations now provide the necessary relations between physical and regularized quantities, where the generalized Levi-Civita matrix $\mathcal { L }$ defined by (4.27) plays the usual role. After introducing the time transformation $d t = g ( \mathbf { P } , \mathbf { Q } )$ , we obtain the desired regularized form $\Gamma ^ { * }$ , with the Hamiltonian function itself in terms of $\mathbf { P } , \mathbf { Q }$ as

$$
H = \textstyle { \frac { 1 } { 4 } } \sum _ { u , v } ^ { K } T _ { u v } { \mathbf { P } } _ { u } ^ { \mathrm { T } } \mathcal { L } _ { u } ^ { \mathrm { T } } \mathcal { L } _ { v } { \mathbf { P } } _ { v } / Q _ { u } ^ { 2 } Q _ { v } ^ { 2 } - \sum _ { e = 1 } ^ { N } M _ { e } / Q _ { e } ^ { 2 } .
$$

Given the final Hamiltonian above, the standard way of carrying out the differentiations after multiplying by the function $g$ of (5.54) leads to complicated expressions for $N > 3$ . Instead we revert to the basic form of $\Gamma ^ { * }$ and write the equations of motion as

$$
\begin{array} { r l } & { \displaystyle \frac { d { \bf Q } } { d \tau } = g \frac { \partial { \cal H } } { \partial { \bf P } } + ( { \cal H } - E _ { 0 } ) \frac { \partial g } { \partial { \bf P } } , } \\ & { \displaystyle \frac { d { \bf P } } { d \tau } = - g \frac { \partial { \cal H } } { \partial { \bf Q } } - ( { \cal H } - E _ { 0 } ) \frac { \partial g } { \partial { \bf Q } } . } \end{array}
$$

Note that $H - E _ { 0 } = 0$ on the solution path but the regularity of the equations is actually lost if this term is omitted.

Several time transformations have been considered. However, use of the Lagrangian by $g = 1 / L$ appears to have practical advantages [Zare & Szebehely, 1975; Alexander, 1986]. The paper by Alexander provides a useful systematic comparison of the multiple regularization methods discussed above. Among the few applications of the global regularization method we mention the pioneering work on binary–binary interactions [Mikkola, 1983, 1984b], as well as use of an unperturbed four-body treatment in star cluster simulations with primordial binaries [Aarseth, 1985a; Heggie & Aarseth, 1992]. We also note that the global formulation is simple in one respect, namely there is no decision-making connected with switching of dominant components. Further discussions concerning the properties of the method can be found in the original exposition [Mikkola, 1985a]. Suffice it to state that an examination of the equations shows that two-body collision configurations can be studied without any problems. Appendix A contains the equations of motion and a collection of the relevant formulae, including external perturbations.

# 5.7 Chain treatment

The basic Aarseth–Zare regularization method has proved itself in scattering experiments and star cluster simulations [Aarseth & Heggie, 1976; Heggie & Aarseth, 1992], as well as in more traditional three-body investigations [Aarseth et al., 1994a,b]. Subsequently, the Heggie–Mikkola global formulation was employed to study binary–binary interactions, likewise for compact subsystems where the external perturbation can be ignored. In view of this activity, it is perhaps remarkable that it took another 17 years for the three-body method to be extended to $N = 4$ [Mikkola & Aarseth, 1990]. This new treatment was reformulated for arbitrary memberships [Mikkola & Aarseth, 1993] with an improved notation, which will be used in the following.

The concept of a chain is very simple and is illustrated in Fig.5.3 for a system of four mass-points. We introduce the dominant two-body forces along a chain of inter-particle vectors, where the pair-wise attractions are treated by the KS formalism. Contributions from the other less dominant interactions are added to the regular terms in a similar way to the original three-body formulation. Hence the number of equations to be integrated is $8 ( N - 1 ) + 1$ , compared with $4 N ( N { - } 1 ) { + } 1$ in the global implementation.

Consider a system of $N$ particles with inertial coordinates $\mathbf { r } _ { i }$ , velocities $\mathbf { v } _ { i }$ and masses $m _ { i }$ , $i = 1 , 2 , \ldots , N$ . Further, take the c.m. to be at rest with the local coordinates ${ \bf q } _ { i }$ and momenta $\mathbf { p } _ { i } = m _ { i } \mathbf { v } _ { i }$ . After selecting the chain vectors connecting the $N$ mass-points, we relabel them $1 , 2 , \ldots , N$ as shown in the figure. The generating function

![](images/72eba5bf3d860517f64f7e7e41b89ae85644470d1e162c4820322bbcb28a50d0.jpg)  
Fig. 5.3. Four-body chain.

$$
S = \sum _ { k = 1 } ^ { N - 1 } \mathbf { W } _ { k } \cdot ( \mathbf { q } _ { k + 1 } - \mathbf { q } _ { k } )
$$

then gives the old momenta ${ \bf p } _ { k } = \partial S / \partial { \bf q } _ { k }$ in terms of the new ones. The relative momentum vectors $\mathbf { W } _ { k }$ are obtained recursively by

$$
\mathbf { W } _ { k } = \mathbf { W } _ { k - 1 } - \mathbf { p } _ { k } , \qquad \quad ( k = 2 , \ldots , N - 2 )
$$

with $\mathbf { W } _ { 1 } = - \mathbf { p } _ { 1 }$ and ${ \bf W } _ { N - 1 } = { \bf p } _ { N }$ . These momenta and corresponding relative coordinates, $\mathbf { R } _ { k } = \mathbf { q } _ { k + 1 } - \mathbf { q } _ { k }$ , are substituted into the unperturbed Hamiltonian which becomes

$$
\begin{array} { l } { { \displaystyle { \cal H } = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { N - 1 } \left( \frac { 1 } { m _ { k } } + \frac { 1 } { m _ { k + 1 } } \right) { \bf W } _ { k } ^ { 2 } - \sum _ { k = 2 } ^ { N } \frac { 1 } { m _ { k } } { \bf W } _ { k - 1 } \cdot { \bf W } _ { k } } } \\ { { \displaystyle ~ - \sum _ { k = 1 } ^ { N - 1 } \frac { m _ { k } m _ { k + 1 } } { R _ { k } } - \sum _ { 1 \le i \le j - 2 } ^ { N } \frac { m _ { i } m _ { j } } { R _ { i j } } . } } \end{array}
$$

We now employ the time transformation $d t = g d \tau$ , where $g = 1 / L$ is the inverse Lagrangian [cf. Alexander, 1986]. The regularized Hamiltonian $\Gamma ^ { * } = g \left( H - E \right)$ again gives rise to equations of motion of the form (5.9). Inspection of these equations reveals that the two-body solutions are regular for any $R _ { k } \to 0$ . Since the time transformation does not introduce terms that cancel analytically, the differentiation of each term is carried out separately. Some care is needed to obtain the partials with respect to $\mathbf { Q }$ of the non-chained part, $U _ { \mathrm { n c } }$ , represented by the last term of (5.69). Let us adopt the traditional notation $\mathcal { L }$ for the generalized Levi-Civita matrix instead of $\bar { \bf Q }$ used in the original paper. Thus if $\mathbf { Q }$ is the KS transform of $\mathbf { R }$ and $U _ { \mathrm { n c } } = U ( \mathbf { R } )$ , then $\partial U _ { \mathrm { n c } } / \partial \mathbf { Q } = 2 \mathcal { L } ^ { \mathrm { T } } \mathbf { F }$ , where ${ \bf F } = \partial U _ { \mathrm { n c } } / \partial { \bf R }$ . Thus a conservative external potential may be treated as an additional part of the non-chained potential. This is discussed below for the perturbed formulation.

When required, the relative coordinates and momenta are recovered from the standard KS relations by

$$
\begin{array} { r c l } { { } } & { { } } & { { { \bf R } _ { k } = \mathcal { L } _ { k } { \bf Q } _ { k } , } } \\ { { } } & { { } } & { { { \bf W } _ { k } = \frac { 1 } { 2 } \mathcal { L } _ { k } { \bf P } _ { k } / { \bf Q } _ { k } ^ { 2 } . } } \end{array}
$$

Procedures for chain selection require special care in order to ensure that the dominant two-body motions are included. Still, the scheme admits of a certain elasticity at the expense of efficiency, as long as the nonchained distances do not become too small compared with the chained distances. Since this feature forms an important part of the chain algorithms, it may be useful to discuss some relevant aspects.

The chain needs to be constructed ab initio before the calculation can begin. First the shortest inter-particle vector is determined. We proceed by searching for the particle which is closest to either end of the known chain. This operation is repeated until all the particles have been included. To facilitate the procedure, it is beneficial to sort all the distances and perform a sequential search for the missing terms.

We readily see that the new chain vectors can be expressed as sums or differences of the old ones. This is achieved by writing physical vectors as sums of chain vectors in a coordinate system where the first particle is located at the origin. Special attention is also required to retain accuracy by carrying out the transformations directly from the old chain vectors, $\mathbf { R } _ { k }$ , to the new ones, instead of using the physical coordinates, $\mathbf { r } _ { i }$ .

Let the identity of the chain particles defined above be $I _ { 1 } , I _ { 2 } , \ldots , I _ { N }$ and denote the identities in the old and new chains by $I _ { k } ^ { \mathrm { o l d } }$ and $I _ { k } ^ { \mathrm { n e w } }$ . We then express the old partial sums along the chain by

$$
{ \bf q } _ { I _ { k } ^ { \mathrm { o l d } } } = \sum _ { \nu = 1 } ^ { k - 1 } { \bf R } _ { \nu } ^ { \mathrm { o l d } } ,
$$

with the new chain vectors given by

$$
{ \bf R } _ { \mu } ^ { \mathrm { n e w } } = { \bf q } _ { I _ { \mu + 1 } ^ { \mathrm { n e w } } } - { \bf q } _ { I _ { \mu } ^ { \mathrm { n e w } } } .
$$

Hence we need to use the correspondence between the old and new indices to obtain the new chain vectors, ${ \bf R } _ { k }$ . It can be seen that if $k _ { 0 }$ and $k _ { 1 }$ are such that $I _ { k _ { 0 } } ^ { \mathrm { o l d } } = I _ { \mu } ^ { \mathrm { n e w } }$ and $I _ { k _ { 1 } } ^ { \mathrm { o l d } } = I _ { \mu + 1 } ^ { \mathrm { n e w } }$ , then we have

$$
{ \displaystyle { \bf R } _ { \mu } ^ { \mathrm { n e w } } = \sum _ { \nu = 1 } ^ { N - 1 } B _ { \mu \nu } { \bf R } _ { \nu } ^ { \mathrm { o l d } } } ,
$$

where $B _ { \mu \nu } = 1$ if ( $k _ { 1 } > \nu$ and $k _ { 0 } \le \nu$ ) and $B _ { \mu \nu } = - 1$ if ( $k _ { 1 } \leq \nu$ and $k _ { 0 }$ $> \nu$ ), otherwise $B _ { \mu \nu } = 0$ . In practical applications the chain configuration is rechecked every integration step but the overheads are still modest because the high-order Bulirsch–Stoer [1966] integrator requires many function calls. Moreover, the total number of such switchings by relabelling is relatively small in typical calculations.

The chain method may be used for two purposes. First we have the simple case of a small- $N$ system, in which all the members may be included [Sterzik & Durisen, 1998; Kiseleva et al., 1998]. Distant escapers may be removed from the chain in order to speed up the calculation, but otherwise the procedures outlined above suffice. The alternative usage of studying energetic interactions in a general $N$ -body code requires special considerations. Below we provide the necessary details for including the external perturbations, whereas corresponding algorithms for the interface with an $N$ -body system will be discussed in a later chapter.

Let $\mathbf { F } _ { j }$ be the perturbing acceleration acting on a body of mass $m _ { j }$ in the inertial coordinate system. For consistency with the previous notation, let the chain membership still be denoted by $N$ , with each component subject to an external acceleration, $\mathbf { F } _ { j }$ , considered as a known function of time. Hence we assume that all the other bodies are advanced by some direct integration scheme. We now augment the original Hamiltonian (5.69) by adding the perturbing potential

$$
\delta U = \sum _ { j = 1 } ^ { N } m _ { j } \mathbf { q } _ { j } \cdot \left[ \mathbf { F } _ { j } ( t ) - \mathbf { F } _ { 0 } ( t ) \right] + M \mathbf { r } _ { 0 } \cdot \mathbf { F } _ { 0 } ( t ) ,
$$

where $\begin{array} { r } { \mathbf { F } _ { 0 } = \sum _ { j = 1 } ^ { N } m _ { j } \mathbf { F } _ { j } / M } \end{array}$ is the c.m. acceleration in the inertial system defined by $\mathbf { r } _ { 0 } = \sum m _ { j } \mathbf { r } _ { j } / M$ and $M$ is the associated mass.

Next we should express the coordinates, $\mathbf { q } _ { j }$ , in terms of the chain coordinates, ${ \bf R } _ { k }$ , and substitute these into the expression for $\delta U$ , which yields the corresponding contributions, $\delta \Dot { \mathbf { W } } _ { k }$ , to the derivatives of the chain momenta, $\mathbf { W } _ { k }$ . However, from the transformation formulae one easily derives the recursive relations

$$
\begin{array} { c c } { { \delta \dot { \mathbf { p } } _ { j } = m _ { j } ( \mathbf { F } _ { j } - \mathbf { F } _ { 0 } ) , } } & { { ~ ( j = 1 , \hdots , N ) } } \\ { { \delta \dot { \mathbf { W } } _ { 1 } = - \delta \dot { \mathbf { p } } _ { 1 } , } } & { { ~ } } \\ { { \delta \dot { \mathbf { W } } _ { k } = \delta \dot { \mathbf { W } } _ { k - 1 } - \delta \dot { \mathbf { p } } _ { k } , } } & { { ~ ( k = 2 , \hdots , N - 2 ) } } \\ { { \delta \dot { \mathbf { W } } _ { N - 1 } = \delta \dot { \mathbf { p } } _ { N } , } } & { { ~ } } \end{array}
$$

where $\delta$ denotes the perturbative part of the derivative. The corresponding corrections to the derivatives of the KS momenta are then given by

$$
\delta \mathbf { P } _ { k } ^ { \prime } = 2 g \mathcal { L } _ { k } ^ { \mathrm { T } } \delta \dot { \mathbf { W } } _ { k } ,
$$

and the rate of change of the internal energy may be written

$$
d E / d \tau = 2 \sum _ { k = 1 } ^ { N - 1 } { \bf Q } _ { k } ^ { \mathrm { / T } } \mathcal { L } _ { k } ^ { \mathrm { T } } \delta \dot { \bf W } _ { k } .
$$

The total energy previously denoted by $E _ { 0 }$ may now be integrated as an additional equation. Since only the perturbation with respect to the c.m. enters in the expressions for $\delta \Dot { \mathbf { W } } _ { k }$ , it is usually sufficient to include tidal contributions from nearby particles. We also note that (5.77) makes use of the term $d \mathbf { Q } _ { k } / d \tau$ , which is already known.

A complete collection of formulae for chain regularization is given in Appendix B. The original paper [Mikkola $\&$ Aarseth, 1990] makes a comparison with the global method for $N = 3$ and discusses practical aspects.

# 5.8 Slow-down procedure

Extremely close binaries occur frequently in modern star cluster simulations which usually include a distribution of primordial binaries [McMillan, Hut & Makino, 1990; Heggie & Aarseth, 1992]. Normally such binaries are unperturbed and easily treated but configurations in hierarchical subsystems may give rise to considerable time-scale problems, whether treated by KS or chain regularization. In the case of small perturbations, we may apply the principle of adiabatic invariance and still represent the motions to a good approximation although the orbital phase is lost. Such a scheme has turned out to be very useful [Mikkola & Aarseth, 1996] and will be presented in the following. The question of whether it could also be introduced into the other multiple regularizations described above does not appear to have been addressed. $^ \ddag$

Consider a weakly perturbed binary with the standard equation of relative motion

$$
\ddot { \mathbf { r } } = - M _ { \mathrm { b } } \mathbf { r } / r ^ { 3 } + \mathbf { F } ,
$$

where $M _ { \mathrm { b } }$ is the combined mass of the binary components and $\mathbf { F }$ is the external perturbation. One way to solve this equation numerically is to employ the variation of constants method. In that case the equation of motion for a two-body element $q = q ( \mathbf { r } , \mathbf { v } , t )$ takes the simple form

$$
\dot { q } = \partial q / \partial { \bf v } \cdot { \bf F } ,
$$

where the right-hand side is a small quantity. However, the rapid fluctuations persist and the time-step can only be increased for relatively small perturbations.

The new idea is to slow down the internal dominant two-body motion such that one orbit may represent several Kepler periods. This is achieved by scaling the small perturbation and the physical time-step by a slowly varying factor exceeding unity. In this approximation, we therefore ensure a correct treatment of the secular effects. To demonstrate more carefully what is involved, we write the coupled equations containing the slow-down factor $\kappa$ as

$$
\begin{array} { l } { { \dot { \mathbf { v } } = - \kappa ^ { - 1 } \mathbf { r } / r ^ { 3 } + \mathbf { F } , } } \\ { { \dot { \mathbf { r } } = \kappa ^ { - 1 } \mathbf { v } . } } \end{array}
$$

Hence the new period is $\kappa$ times the original one and the integration is speeded up by the same amount. Let us write the equation for the variation of an element $q = q ( t / \kappa , \mathbf { r } , \mathbf { v } )$ , with $t / \kappa$ representing the scaling of time. This leads to

$$
{ \begin{array} { l } { { \dot { q } } = { \frac { \partial q } { \partial t } } + { \frac { \partial q } { \partial \mathbf { r } } } \cdot { \dot { \mathbf { r } } } + { \frac { \partial q } { \partial \mathbf { v } } } { \dot { \mathbf { v } } } } \\ { = \kappa ^ { - 1 } \left[ { \frac { \partial q } { \partial ( t / \kappa ) } } + { \frac { \partial q } { \partial \mathbf { r } } } \cdot \mathbf { v } - { \frac { \mathbf { r } } { r ^ { 3 } } } \cdot { \frac { \partial q } { \partial \mathbf { v } } } \right] + { \frac { \partial q } { \partial \mathbf { v } } } \cdot \mathbf { F } } \\ { = { \frac { \partial q } { \partial \mathbf { v } } } \cdot \mathbf { F } , } \end{array} }
$$

where the final result simplifies to the earlier form (5.79), because the two-body terms cancel due to $q$ being an element. It should be noted that now the short-period terms are multiplied by the factor $\kappa$ which therefore tends to counteract the advantage.

In the original Hamiltonian formulation we have

$$
\begin{array} { r } { H = \frac { 1 } { 2 } p ^ { 2 } / \mu - M _ { \mathrm { b } } / r - U , } \end{array}
$$

where $\mu$ is the reduced mass and $U$ is the perturbing force function which yields the external force by $\mathbf { F } = \partial U / \partial \mathbf { r }$ . The modified formulation may be described by the new Hamiltonian

$$
\tilde { H } = \kappa ^ { - 1 } ( { \textstyle \frac { 1 } { 2 } } p ^ { 2 } / \mu - M _ { \mathrm { b } } / r ) - U ,
$$

which leads to the above slowed-down equations of motion. This principle can also be applied more generally in an $N$ -body system, and even in complicated situations that may occur in chain regularization [Mikkola $\&$ Aarseth, 1993].

The idea may be formulated in the following way. First, separate from the Hamiltonian, $H$ , those terms which give the internal interaction of the pair of particles forming the weakly perturbed binary, denoted $H _ { b }$ . Second, multiply the part $H _ { b }$ by the slow-down factor $\kappa ^ { - 1 }$ to get

$$
H _ { \mathrm { n e w } } = \kappa ^ { - 1 } H _ { b } + \left( H - H _ { b } \right) ,
$$

and form the usual Hamiltonian equations of motion

$$
\dot { \mathbf { P } } = - \partial H _ { \mathrm { n e w } } / \partial \mathbf { Q } , \qquad \dot { \mathbf { Q } } = \mathbf { \nabla } \partial H _ { \mathrm { n e w } } / \partial \mathbf { P } .
$$

Alternatively, for a regularized formulation, we first write

$$
\Gamma _ { \mathrm { n e w } } = H _ { \mathrm { n e w } } - E ,
$$

and multiply by the time transformation, $g$ , before forming the equations of motion. Since $\kappa$ changes with time, $H _ { \mathrm { n e w } }$ is not constant and for the associated numerical value we may write

$$
\dot { E } = \partial \kappa ^ { - 1 } / \partial t H _ { b } .
$$

In practice, $\kappa$ is adjusted by a small discrete amount after each step. Hence the corresponding change in $E$ is a delta function, obtained as a fraction $1 / \kappa _ { \mathrm { n e w } } - 1 / \kappa _ { \mathrm { o l d } }$ of the instantaneous binding energy, $H _ { b }$ .

The formulation (5.84) may be applied to many dynamical problems featuring weakly perturbed systems and long time-scales. However, in the following we focus on implementation in the chain regularization discussed above.

Given the chain coordinates, ${ \bf R } _ { k }$ , and momenta, $\mathbf { W } _ { k }$ , we write the Hamiltonian as

$$
H = \sum T _ { i j } \mathbf { W } _ { i } \cdot \mathbf { W } _ { j } - \sum M _ { k } / R _ { k } - \sum M _ { i j } / R _ { i j } ,
$$

where the auxiliary quantities affected by the present formulation are given by the original expressions,

$$
\begin{array} { c c } { { T _ { k k } = \frac 1 2 ( 1 / m _ { k } + 1 / m _ { k + 1 } ) , } } & { { } } \\ { { T _ { k k + 1 } = - 1 / m _ { k } , } } & { { } } \\ { { M _ { k } = m _ { k } m _ { k + 1 } . } } & { { ( k = 1 , . . . , N - 1 ) } } \end{array}
$$

To construct an expression for the internal interaction of a binary within the chain, we first note that the relevant term in the potential energy is ${ M } _ { b } / { R } _ { b }$ if $b$ is the index of the distance between the binary components§ $m _ { b }$ , $m _ { b + 1 }$ . Hence we must select from the kinetic energy those terms which have $1 / m _ { b }$ or $1 / m _ { b + 1 }$ as a factor. The resulting combination of terms, however, also contains the c.m. kinetic energy which must be subtracted and added to the rest of the Hamiltonian.

We write the c.m. kinetic energy for the pair $m _ { b }$ , $m _ { b + 1 }$ as

$$
T _ { \mathrm { c m } } = \frac { 1 } { 2 } ( { \mathbf { W } } _ { b + 1 } - { \mathbf { W } } _ { b - 1 } ) ^ { 2 } / ( m _ { b } + m _ { b + 1 } ) .
$$

This is valid in all cases, provided that the quantities $\mathbf { W } _ { k }$ are defined to be zero whenever the index $k$ is outside the range $\lfloor 1 , N - 1 \rfloor$ . Selection of the relevant terms from the Hamiltonian and expansion of the expression for $T _ { \mathrm { { c m } } }$ gives the following new expressions for evaluating the matrix $\mathit { T } _ { i j }$ and vector $M _ { k }$ in the presence of a slowed-down binary. First we calculate

$$
\begin{array} { c } { { T _ { k k + 1 } = - 1 / m _ { k } / \kappa _ { k } , } } \\ { { { \cal T } _ { k + 1 k + 2 } = - 1 / m _ { k + 1 } / \kappa _ { k } , ~ ( k = 1 , 3 , 5 , . . . , \leq N ) } } \end{array}
$$

where a slow-down coefficient $\kappa _ { k } = 1$ has been defined for every chain vector, except for $k = b$ . Next we evaluate the expressions

$$
\begin{array} { c } { { T _ { b - 1 } \ { b + 1 } = - ( 1 - \kappa _ { b } ^ { - 1 } ) / ( m _ { b } + m _ { b + 1 } ) , } } \\ { { \delta T _ { b - 1 } \ { b - 1 } = \delta T _ { b + 1 } \ { b + 1 } = - \frac { 1 } { 2 } T _ { b - 1 } \ { b + 1 } , } } \end{array}
$$

and finally

$$
\begin{array} { r c l } { { } } & { { } } & { { T _ { k k } = - \frac { 1 } { 2 } ( T _ { k } \mathbf { \epsilon } _ { k + 1 } + T _ { k + 1 } \mathbf { \epsilon } _ { k + 2 } ) + \delta T _ { k k } , } } \\ { { } } & { { } } & { { M _ { k } = m _ { k } m _ { k + 1 } / \kappa _ { k } . } } \end{array}
$$

Only two modifications remain which affect the evaluation of the equations of motion. First we must change the equation for $\mathbf { A } _ { k }$ that appear in the algorithm for the chain derivatives (cf. B.11) to read

$$
\mathbf { A } _ { k } = \frac { 1 } { 2 } \sum ( T _ { k i } + T _ { i k } ) \mathbf { W } _ { i } , \qquad ( | i - k | \leq 2 )
$$

because there are more non-zero off-diagonal elements in the $T$ -matrix. Hence only the summation limit has changed here. Finally, the total energy that appears explicitly in the usual equations of motion must be modified by the amount

$$
\delta E = - \frac { m _ { b } m _ { b + 1 } } { 2 a } \left( \frac { 1 } { \kappa _ { b } ^ { \mathrm { n e w } } } - \frac { 1 } { \kappa _ { b } ^ { \mathrm { o l d } } } \right) ,
$$

where $a$ is the actual semi-major axis. This contribution should be added to the total energy when the slow-down factor changes from the old value, $\kappa _ { b } ^ { \mathrm { o l d } }$ , to the new one, $\kappa _ { b } ^ { \mathrm { n e w } }$ .

So far we have discussed the slow-down procedure for only one binary. However, we may have several such binaries in a chain subsystem and the operations above may then be repeated for any relevant index $b$ if desired. It may also be remarked that the addition of external perturbations does not affect the slow-down scheme since the internal tidal forces dominate.

Another type of $N$ -body system of current interest consists of one or more planets orbiting a central star which interacts with other cluster members [de la Fuente Marcos & de la Fuente Marcos, 1999] or is perturbed in scattering experiments [Laughlin & Adams, 1998]. In this case the above strategy needs to be modified slightly. Thus the binary energy appearing in (5.95) is replaced by the total subsystem energy which must be calculated explicitly. Moreover, the size of the perturbation is now estimated by considering the outermost planet. The chain regularization is quite effective for studying different types of configurations, provided the condition of approximate isolation is satisfied. Thus the slow-down procedure is applied to a compact subsystem for long time intervals of small perturbations and yet we retain the advantage of treating strong interactions leading to exchange or escape.

# 5.9 Time-transformed leapfrog scheme

The regularization schemes discussed so far are quite satisfactory for most stellar systems. However, application to the case of very large mass ratios leads to loss of efficiency as well as accuracy. In particular, the problem of black hole binaries in galactic nuclei is currently topical. So far the standard KS treatment discussed above has only been partially successful [Quinlan & Hernquist, 1997; Milosavljevi´c & Merritt, 2001]. On general grounds, extension to chain regularization is also unlikely to be satisfactory because the total subsystem energy that appears explicitly in the equations of motion is dominated by the binary components. In view of the small period and large binding energy of such a binary, some other kind of regularization or smoothing method is therefore desirable.

Below we describe a new time-transformed leapfrog scheme that offers practical advantages for studying systems with large mass ratios [Mikkola & Aarseth, 2002]. Consider first the standard leapfrog equations

$$
\begin{array} { l } { { \displaystyle { \bf r } _ { 1 / 2 } = { \bf r } _ { 0 } + \frac { h } { 2 } { \bf v } _ { 0 } } , \ ~ } \\ { { \displaystyle { \bf v } _ { 1 } = { \bf v } _ { 0 } + h { \bf F } ( { \bf r } _ { 1 / 2 } ) } , \ ~ } \\ { { \displaystyle { \bf r } _ { 1 } = { \bf r } _ { 1 / 2 } + \frac { h } { 2 } { \bf v } _ { 1 } } , \ ~ } \end{array}
$$

where $h$ is the time-step and $\mathbf { F }$ denotes the acceleration at $t = { \textstyle { \frac { 1 } { 2 } } } h$ . We adopt a time transformation $d s = \Omega ( \mathbf { r } ) d t$ , with $\Omega$ an arbitrary function and introduce a new auxiliary quantity $W = \Omega$ . The new idea here is to evaluate $W$ by the auxiliary equation

$$
{ \dot { W } } = \mathbf { v } \cdot { \frac { \partial { \boldsymbol { \Omega } } } { \partial \mathbf { r } } } ,
$$

rather than explicitly. This allows us to solve the two sets of equations in separate stages; namely (i) $\mathbf { r } ^ { \prime } = \mathbf { v } / W$ , $t ^ { \prime } = 1 / W$ , $\mathbf { v } ^ { \prime } = 0$ , $W ^ { \prime } = 0$ , and (ii)

$\mathbf { v } ^ { \prime } = \mathbf { F } / \Omega$ , $W ^ { \prime } = \dot { W } / \Omega$ , $\mathbf { r } ^ { \prime } = 0$ , $t ^ { \prime } = 0$ . Consequently, we write

$$
\begin{array} { l } { \displaystyle \mathbf { r } = \mathbf { r } _ { 0 } + s \frac { \mathbf { v } } { W } , } \\ { \displaystyle t = t _ { 0 } + s \frac { 1 } { W } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \mathbf { v } _ { 1 } = \mathbf { v } _ { 0 } + s \frac { \mathbf { F } \left( \mathbf { r } _ { 1 / 2 } \right) } { \Omega \left( \mathbf { r } _ { 1 / 2 } \right) } , } \\ & { W _ { 1 } = W _ { 0 } + s \frac { \mathbf { v } + \mathbf { v } _ { 0 } } { 2 \Omega \left( \mathbf { r } _ { 1 / 2 } \right) } \cdot \frac { \partial \Omega \left( \mathbf { r } _ { 1 / 2 } \right) } { \partial \mathbf { r } _ { 1 / 2 } } . } \end{array}
$$

Hence the solutions have been combined into a form of leapfrog, taking $s = { \frac { 1 } { 2 } } h$ in (5.98); then $s = h$ in (5.99) and finally again $s = { \textstyle { \frac { 1 } { 2 } } } h$ in (5.98), using the midpoint rule. The numerical solutions are obtained by employing the high-order Bulirsch–Stoer method. Thus, with the above leapfrog algorithm, several integrations are performed with gradually decreasing substeps, $h$ , and the results are extrapolated to zero step-length.

Up to now, the choice of the time transformation has not been specified. When considering an application to small subsystems, it is convenient to choose the function

$$
\Omega = \sum _ { i < j } \frac { \Omega _ { i j } } { r _ { i j } } ,
$$

where $\Omega _ { i j }$ may be taken as the mass products or simply as unity. Here we make the latter choice which assigns equal weights to all the members. Hence the gradient is simply the force function

$$
\frac { \partial \Omega } { \partial \mathbf { r } _ { k } } \equiv \mathbf { G } _ { k } = \sum _ { j \neq k } \frac { \mathbf { r } _ { j } - \mathbf { r } _ { k } } { r _ { k j } ^ { 3 } } .
$$

The corresponding equations of motion for each particle, $k$ , are given by

$$
\begin{array} { l l } { { { \displaystyle { \bf r } _ { k } ^ { \prime } = \frac { { \bf v } _ { k } } { W } } , } } & { { ~ t ^ { \prime } = \frac { 1 } { W } , } } \\ { { { \displaystyle { \bf v } _ { k } ^ { \prime } = \frac { { \bf F } _ { k } } { \Omega } } , } } & { { ~ W ^ { \prime } = \frac { 1 } { \Omega } \sum _ { k } { \bf v } _ { k } \cdot { \bf G } _ { k } , } } \end{array}
$$

whereupon the leapfrog algorithm (5.96) is attained.

This formulation has also been generalized to include separately external perturbations of conservative type as well as relativistic effects. In this case we replace the last pair of equations (5.103) by

$$
\mathbf { v } ^ { \prime } = ( \mathbf { F } + \mathbf { f } ( \mathbf { v } ) ) / \Omega , \qquad W ^ { \prime } = \mathbf { v } \cdot \mathbf { G } / \Omega ,
$$

where $\mathbf f ( \mathbf v )$ denotes the velocity-dependent part of the acceleration and subscripts have been omitted for simplicity. For small relativistic corrections, the leapfrog velocity integration may be replaced by the implicit midpoint method

$$
\mathbf { v } _ { 1 } = \mathbf { v } _ { 0 } + h ( \mathbf { F } + \mathbf { f } ( \mathbf { v } _ { \mathrm { a } } ) ) / \Omega ,
$$

with $\begin{array} { r } { \mathbf { v } _ { \mathrm { a } } = \frac { 1 } { 2 } ( \mathbf { v } _ { 0 } + \mathbf { v } _ { 1 } ) } \end{array}$ the average velocity. Convergent solutions are usually obtained after a few iterations. In either case, the energy of the subsystem is no longer constant but its change can be determined by integration of the additional equation

$$
E ^ { \prime } ( { \mathbf { v } _ { \mathrm { a } } } ) = \sum _ { k } m _ { k } { \mathbf { v } _ { k } } \cdot { \mathbf { f } _ { k } } ( { \mathbf { v } _ { \mathrm { a } } } ) / \Omega ,
$$

where $\mathbf { v } _ { \mathrm { a } }$ represents all the average velocities. Finally, this equation can be treated in the same way as (5.104) to yield the energy jump $\Delta E = h E ^ { \prime }$ .

Tests of small systems ( $N \ = \ 1 0$ with two heavy bodies) show that the time-transformed leapfrog (TTL) method is performing well. Thus significantly higher accuracy with about half the number of function evaluations was achieved when including the time transformation. Reliable solutions for coalescence by gravitational radiation have also been obtained involving one or both of the massive binary components. Since the Bulirsch–Stoer integrator is rather expensive when including many interactions, the new method is intended for treating a compact subsystem containing a massive binary and significant perturbers, but intervals of unperturbed motion may also be studied. Finally, it may be noted that integration of the time transforming function $W$ ensures a more wellbehaved solution than direct evaluation. A particular advantage is that if any other distances become very large, the time transformation function approaches more closely to the inverse binary separation, which would give exact binary motion by the leapfrog integration.

# 5.10 Algorithmic regularization

The power of special time transformations was demonstrated in the previous section. Thus when combined with leapfrog integration we essentially achieve a practical regularization scheme where arbitrarily close but non-singular encounters may be studied. This property was first discovered when considering a simplified form of the Hamiltonian [Mikkola $\&$ Tanikawa, 1999a,b]. In view of the connection with the TTL method, a brief discussion of the main idea is of interest.¶

We begin by writing the two-body Hamiltonian as

$$
H = T - U ,
$$

where $T$ and $U > 0$ define the kinetic and potential energy, respectively. Application of the time transformation

$$
d s = U d t
$$

gives rise to the time-transformed Hamiltonian

$$
\Gamma = ( T - U + P _ { t } ) / U .
$$

Here $P _ { t } = - E _ { 0 }$ with $E _ { 0 }$ the initial total energy. Although this Hamiltonian is not separable, $\Gamma = 0$ on the solution path. This enables us to define the logarithmic function

$$
\Lambda = \ln ( 1 + \Gamma ) ,
$$

which after simplification leads to the separable form

$$
\Lambda = \ln ( T + P _ { t } ) - \ln U .
$$

A modified leapfrog algorithm can now be introduced that produces correct positions and momenta for an elliptic orbit, albeit with a thirdorder phase error. Provided the coordinates are not evaluated at the singularity, this treatment also applies to collision orbits. Hence a practical regularization is achieved in the absence of a coordinate transformation. The formulation has been generalized to arbitrary memberships and used successfully to study collisions in a 1D system of six particles.

The numerical solutions are improved by introducing chain coordinates in order to reduce round-off errors. However, comparison with the basic chain method shows that the latter is still more efficient for critical triple encounters. One paper [Mikkola & Tanikawa, 1999b] also contains some useful explanations of the first- and second-order Bulirsch–Stoer method. Finally, for completeness, we mention an analogous derivation of the logarithmic Hamiltonian for symplectic integration [Preto & Tremaine, 1999].

We end this chapter by reviewing two global regularization methods of the general three-body problem in 2D [Lemaˆıtre, 1955; Waldvogel, 1972]. The first derivation is based on a complicated Hamiltonian which is not suitable for numerical work. It is also not clear whether a generalization to 3D introduces singular terms [cf. Heggie, 1974]. However, the Hamiltonian of the second formulation does satisfy the requirement of simplicity. A comparison with the three-body methods of sections 5.2 and 5.5 would therefore be of considerable interest.

6

Tree codes

# 6.1 Introduction

Direct $N$ -body simulations are of necessity expensive because of the need to evaluate all the $N ( N - 1 ) / 2$ force interaction terms. We have seen that the Ahmad–Cohen [1973] neighbour scheme only alleviates the problem to some extent. However, once the particle number becomes sufficiently large, the dynamical behaviour begins to change because close encounters are less important. This behaviour has inspired methods for collisionless systems to be developed, such as tree codes or multipole expansions. In this chapter, we are concerned with tree codes since some relevant aspects of the latter have already been discussed. First we review the basic features of the pioneering Barnes & Hut [1986] scheme which is widely used in a variety of applications. Since the emphasis in this book is on collisional stellar dynamics, we devote a section to describing a tree code for point-mass interactions [McMillan & Aarseth, 1993] in the hope that it might be revived. The final section deals with an independent development for flattened systems [Richardson, 1993a,b] that has been used to study different stages of planetary formation as well as ring dynamics, where collisions play an important role.

# 6.2 Basic formulation

In view of the rapid growth in the computational requirements for increasing particle numbers when using direct summation, it is not surprising that several tree-based approaches have been made to speed up the expensive force calculation. The basic idea of employing a tree structure is that the interactions due to a group of distant members can be described by a small number of parameters involving low-order moments of the mass distribution. Depending on the opening angle subtended by each group, the total force is then obtained as a sum over these contributions, as well as any individual nearby particles. In the following we outline the basic ideas of the Barnes–Hut [1986] tree-based force algorithm which has been adopted in the methods described in the subsequent sections.

![](images/5e986b5b181b318323ace0c3dad00801692ac151cb6701807f203185b2fc8910.jpg)  
Fig. 6.1. Tree structure.

We begin by constructing one empty cubical cell containing the whole system, called the root node. If more than one particle is assigned to any cell, it is split into eight daughter cells, and this procedure is continued recursively until all the members have been allocated single cells. The data structure of each cell provides information about global quantities such as mass and c.m. position accumulated at that level, as well as pointers to the relevant daughter cells that contain further information. Because of the hierarchical subdivision needed to separate two particles, many of the cells will in fact be empty. A typical cell arrangement is shown in Fig. 6.1 for ten particles distributed in 2D.

Given the tree structure, the force on any particle may be obtained by a recursive procedure that starts at the root cell containing the whole system. Let $l$ be the size of the cell under consideration and $D$ the distance from its c.m. to a particle. If $l / D < \theta$ , where $\theta$ is the opening angle or tolerance, the respective interactions are summed; otherwise the current cell is subdivided into eight cells and each one examined in a similar manner. This procedure continues until all the particles have been included, either in groups or as individual summations. For large $N$ , the total number of such interactions for one particle is of order $\log N$ . In some types of simulations involving softened potentials, an opening angle $\theta \simeq 1$ is often used. However, this results in relatively large force errors, albeit of a random nature.

Two strategies may be used to increase the accuracy of the force calculation. By reducing $\theta$ below unity more neighbouring particles will be considered individually but the limit $\theta  0$ reverts to the direct summation method with additional overheads. The alternative way of providing more information for each cell employs a multipole expansion to be described in the next section. For simplicity, the original formulation did not include the quadrupole terms and the leapfrog integrator used the same time-step for all particles. However, the computational cost of going to higher orders will eventually become prohibitive; hence a compromise of moderate opening angles combined with a relatively low-order expansion offers the best practical solution. Since the cost of rebuilding the whole tree is somewhat less than the cost of one tree force evaluation on all particles, the total cost of this part is still $O ( N \log N )$ for large values of $N$ . As will be seen in the next section, the scaling coefficient is surprisingly large if high accuracy is desired; hence special features are needed to achieve an efficient formulation.

Before going on to discuss a code suitable for point-mass calculations, we mention an astrophysical application of the Hernquist [1987] tree code since it pertains to collisions [Arabadjis $\&$ Richstone, 1996]. This work included the effects of stellar evolution and collisions, as well as a central black hole and rotation. Star formation was also modelled by reprocessing material ejected through stellar mass loss. The rotationally flattened systems showed a steeper density profile than spherical systems, with preferential radial velocities in the halo.

# 6.3 Collisional treatment

Several improvements are required in order to achieve satisfactory performance for star cluster simulations. In the first place, it is desirable to increase the accuracy of each force evaluation which can then be used in a high-order polynomial instead of the basic leapfrog integration. The second objective is to introduce an individual time-step scheme both for the particles and the cells. Third, close encounters and persistent binaries may be treated by regularization techniques. The following developments [McMillan & Aarseth, 1993] are based on the Barnes–Hut scheme because of its ease of construction and conceptual simplicity.

Consider a test particle at the position $\mathbf { r } = \left( r _ { 1 } , r _ { 2 } , r _ { 3 } \right)$ in the centreof-mass (c.m.) system of $K$ particles with masses $m _ { k }$ and coordinates $\mathbf { x } _ { k }$ . The potential at an external position $\mathbf { r }$ is then given in terms of the multipole expansion [Aarseth, 1967]

$$
\Phi ( r ) = - { \frac { M } { r } } - { \frac { Q _ { i j } r _ { i } r _ { j } } { 2 r ^ { 5 } } } - { \frac { S _ { i j } r _ { i } ^ { 2 } r _ { j } + S _ { 1 2 3 } r _ { 1 } r _ { 2 } r _ { 3 } } { 2 r ^ { 7 } } } + O \left( { \frac { \Delta x } { r } } \right) ^ { 5 } .
$$

Here $\Delta x$ represents the size of the system and repeated indices $i$ and $j$ are summed from 1 to 3. The explicit expressions for the monopole, $M$ ,

quadrupole, $Q$ , and octupole, $S$ , Legendre coefficients take the form

$$
\begin{array} { c } { { { \cal M } = \displaystyle \sum m _ { k } , } } \\ { { Q _ { i j } = \displaystyle \sum m _ { k } \big ( 3 x _ { i , k } x _ { j , k } - | { \bf x } _ { k } | ^ { 2 } \delta _ { i j } \big ) , } } \\ { { S _ { i j } = \displaystyle \sum m _ { k } [ 5 \big ( 3 - 2 \delta _ { i j } \big ) x _ { i , k } ^ { 2 } - 3 \big | { \bf x } _ { k } \big | ^ { 2 } \big ] x _ { j , k } , } } \\ { { S _ { 1 2 3 } = 1 5 \displaystyle \sum m _ { k } x _ { 1 , k } x _ { 2 , k } x _ { 3 , k } , } } \end{array}
$$

where the summation is over $K$ internal mass-points. Although the dipole term $\mathbf { D } \ = \ \sum m _ { k } \mathbf { x } _ { k }$ does not appear in the expansion (6.1) since $\mathbf { r }$ is expressed with respect to the c.m. of the $K$ particles, the value of $\mathbf { D } / M$ for each node must still be known. Analogous expressions are readily constructed for internal points (cf. section 3.4).

The question of expansion order must be decided after appropriate tests. Thus going to one more order than given explicitly here (i.e. hexadecapole) would be quite expensive in view of the rapidly growing number of terms, and it would probably be more efficient to reduce the opening angle slightly. Figure 1 of the original paper illustrates typical relative force errors for different orders and opening angles. For a target median force accuracy of about $1 0 ^ { - 4 }$ considered adequate for the present purpose, we need an opening angle $\theta \leq 0 . 4$ for quadrupole moments, whereas $\theta \leq 0 . 5$ is sufficient when octupole terms are included. This general result is in good agreement with other findings [cf. Makino, 1990].

When constructing the cell moments in a tree, we employ a recursive calculation, from the leaves up, such that the moments of each cell are determined by a sum over its eight daughter cells. We begin with the monopole and dipole terms and denote by $m _ { d }$ and $x _ { d }$ the known masses and c.m. of the daughters. The mass $M$ and c.m. coordinates $\mathbf { X }$ of the parents are then simply

$$
\begin{array} { l } { { \displaystyle M = \sum m _ { d } , } } \\ { { \displaystyle { \bf X } = \frac { 1 } { M } \sum m _ { d } { \bf x } _ { d } , } } \end{array}
$$

where the summation over $d$ is from 1 to 8 and subscripts have been omitted. For the quadrupole moments $\mathbf { Q }$ and $\mathbf { q } _ { d }$ , similar expressions to (6.2) again apply, except that the moments of each daughter, $\mathbf { q } _ { d }$ , must be included explicitly, which gives

$$
Q _ { i j } = \sum m _ { d } ( 3 x _ { i , d } x _ { j , d } - | \mathbf { x } _ { d } | ^ { 2 } \delta _ { i j } ) + q _ { i j , d } .
$$

Lastly, for the octupole terms $\mathbf { s }$ and $s _ { d }$ , we obtain in a similar way

$$
S _ { i j } = \sum m _ { d } [ 5 ( 3 - 2 \delta _ { i j } ) x _ { i , d } ^ { 2 } - 3 | { \bf x } _ { d } | ^ { 2 } ] x _ { j , d } +
$$

$$
\begin{array} { c } { { 5 ( 1 - \delta _ { i j } ) x _ { i , d } q _ { i j , d } + \frac 5 2 x _ { j , d } q _ { i i , d } - x _ { l , d } q _ { j l , d } + s _ { i j , d } , } } \\ { { S _ { 1 2 3 } = 1 5 \sum m _ { d } [ x _ { 1 , d } x _ { 2 , d } x _ { 3 , d } } } \\ { { + \frac 5 3 ( x _ { 1 , d } q _ { 2 3 , d } + x _ { 2 , d } q _ { 3 1 , d } + x _ { 3 , d } q _ { 1 2 , d } ) ] + s _ { 1 2 3 , d } , } } \end{array}
$$

where the repeated index, $l$ , in the penultimate term of the first equation is summed. If we define single particles to have zero quadrupole and octupole moments, the above expressions apply whether the daughters of a node are nodes or particles.

Traditionally tree codes have used a low-order integrator and older versions also employed the same time-step for all particles. Since the computational effort of a complete tree construction is $O ( N \log N )$ , with the same scaling but a smaller coefficient than for determining all the forces, it has been customary to continue this practice. However, star cluster simulations span a much wider range in length- and time-scale which requires the use of high-order integration together with individual timesteps. Hence a different strategy must be devised in order to replace the full reconstruction of the tree at every step.

A solution to the tree construction problem is to consider the deformation of the cells with time and update the current values by prediction. The growing deformation modifies the size of each cell, but this can be controlled by using the effective size in the algorithm, or by reducing $\theta$ slightly. Although the particles do not need to fit exactly into the original cubical grid, it is important that the c.m. values for the higher moments of each cell are known to sufficient accuracy. We therefore introduce the idea of individual time-steps for the tree structure, and update the relevant moments by prediction, without explicit reference to the corresponding particle motions. The cells then take on the characteristics of particles, with their own internal derivatives, ${ \dot { \mathbf { Q } } } , { \dot { \mathbf { S } } }$ , as well as time-steps. Now different regions evolve on their own time-scale, and various parts of the tree must be reconstructed at the appropriate time. We delay details of determining the cell time-steps until later and go on to discuss how to extrapolate partial moments.

Suppose that a part of the tree is reconstructed at some time $t _ { 0 }$ . Moreover, assume that all the relevant particles are synchronized, as in the Hermite scheme, so that any relevant quantity can be evaluated without extrapolation. In addition to $\mathbf { X } _ { 0 } , \mathbf { Q } _ { 0 } , \mathbf { S } _ { 0 }$ , we also require the corresponding derivatives ${ \bf V } _ { 0 } = \dot { \bf X } _ { 0 } , { \bf A } _ { 0 } = \ddot { \bf X } _ { 0 }$ , etc. at time $t _ { 0 }$ which are formed by explicit differentiation of (6.2). Cell centroids are predicted to the same order as the particles, i.e.

$$
\begin{array} { r } { \mathbf { X } ( t _ { 0 } + \delta t ) = \mathbf { X } _ { 0 } + \mathbf { V } _ { 0 } \delta t + \frac { 1 } { 2 } \mathbf { A } _ { 0 } \delta t ^ { 2 } + \frac { 1 } { 6 } \dot { \mathbf { A } } _ { 0 } \delta t ^ { 3 } , } \end{array}
$$

where $\delta t < \Delta t$ is the cell time-step. The cell monopole derivatives are

obtained from the relevant particle quantities in an analogous manner to the recursive construction of $\mathbf { X }$ from the array $\left\{ { \bf x } _ { d } \right\}$ .

Prediction of quadrupole moments also needs to be performed to third order. The corresponding derivatives are evaluated by successive differentiation of (6.4), with $\mathbf { a } _ { k } = \dot { \mathbf { v } } _ { k }$ , which gives

$$
\begin{array} { r l } & { \dot { Q } _ { i j } = \sum m _ { k } ( 3 v _ { i , k } x _ { j , k } + 3 x _ { i , k } v _ { j , k } - 2 \mathbf { x } _ { k } \cdot \mathbf { v } _ { k } \delta _ { i j } ) + \dot { q } _ { i j , k } , } \\ & { \ddot { Q } _ { i j } = \sum m _ { k } [ 3 a _ { i , k } x _ { j , k } + 6 v _ { i , k } v _ { j , k } + 3 x _ { i , k } a _ { j , k } } \\ & { ~ - 2 ( \mathbf { x } _ { k } \cdot \mathbf { a } _ { k } + | \mathbf { v } _ { k } | ^ { 2 } ) \delta _ { i j } ] + \ddot { q } _ { i j , k } , } \\ & { Q _ { i j } ^ { ( 3 ) } = \sum m _ { k } [ 3 \dot { a } _ { i , k } x _ { j , k } + 9 a _ { i , k } v _ { j , k } + 9 v _ { i , k } a _ { j , k } + 3 x _ { i , k } \dot { a } _ { j , k } } \\ & { ~ - 2 ( \mathbf { x } _ { k } \cdot \dot { \mathbf { a } } _ { k } + 3 \mathbf { v } _ { k } \cdot \mathbf { a } _ { k } ) \delta _ { i j } ] + q _ { i j , k } ^ { ( 3 ) } . } \end{array}
$$

With multipole prediction, the descent of the tree proceeds almost as previously, except that before the opening criterion is applied to a cell, its c.m. position is updated. If the cell remains unopened, its quadrupole moments are also predicted before use by

$$
\begin{array} { r } { { \bf Q } ( t _ { 0 } + \delta t ) = { \bf Q } _ { 0 } + \dot { \bf Q } _ { 0 } \delta t + \frac { 1 } { 2 } \ddot { \bf Q } _ { 0 } \delta t ^ { 2 } + \frac { 1 } { 6 } { \bf Q } _ { 0 } ^ { ( 3 ) } \delta t ^ { 3 } . } \end{array}
$$

The earlier remark about the cost of the hexadecapole moments also applies to the octupole derivatives which would contain a large number of terms. We neglect the prediction of these derivatives by choosing to limit the time-step instead. However, it seems likely that there would be some benefit by introducing the $\dot { \bf S }$ terms obtained by differentiating (6.5).

A number of criteria have been used to determine time-steps for the cells. We define three characteristic time-scales for each cell as follows. The first is the crossing time

$$
\Delta t _ { \mathrm { c r o s s } } = \operatorname* { m i n } _ { k } \left[ { \frac { ( \Delta X ) ^ { 2 } } { ( \mathbf { x } _ { k } - \mathbf { X } ) \cdot ( \mathbf { v } _ { k } - \mathbf { V } ) } } \right] ,
$$

where the index $k$ refers to all particles in the cell and $\Delta X$ is the cell size. Next we introduce a monopole prediction time by

$$
\Delta t _ { \mathrm { m o n o } } = \left( \frac { \Delta X | \mathbf { A } | + | \mathbf { V } ^ { 2 } | } { | \mathbf { V } | | \dot { \mathbf { A } } | + | \mathbf { A } | ^ { 2 } } \right) ^ { 1 / 2 } .
$$

Finally, we take the quadrupole prediction time as

$$
\Delta t _ { \mathrm { q u a d } } = \left( \frac { | \mathbf { Q } | | \ddot { \mathbf { Q } } | + | \dot { \mathbf { Q } } ^ { 2 } | } { | \dot { \mathbf { Q } } | | \mathbf { Q } ^ { ( 3 ) } | + | \ddot { \mathbf { Q } } | ^ { 2 } } \right) ^ { 1 / 2 } .
$$

We now choose the actual cell time-step from

$$
\Delta t _ { \mathcal { C } } = \eta _ { \mathrm { c } } \operatorname* { m i n } \left\{ \Delta t _ { \mathrm { c r o s s } } , \Delta t _ { \mathrm { m o n o } } , \Delta t _ { \mathrm { q u a d } } \right\} ,
$$

where the choice $\eta _ { \mathrm { c } } \simeq 0 . 1$ for the accuracy parameter gives satisfactory results. In practice, the quadrupole time-scale is the most sensitive. The expressions for the monopole and quadrupole time-steps are based on the original time-step criterion for direct $N$ -body integration.

A cell $\mathcal { C }$ is due to be reconstructed when $t _ { 0 , \mathcal { C } } + \Delta t _ { \mathcal { C } } \leq t$ , in which case the whole part of the tree below $\mathcal { C }$ is rebuilt. This has the effect of updating all the cells descended from $c$ . Hence a daughter cell whose updating time exceeds that of its parent can simply be excluded from consideration by the time-step scheduling algorithm.

There are several reasons why the standard individual time-step scheme is not well suited to the present tree-based code. First, the cost of frequent particle prediction can become substantial and comparable to a force calculation. Another consideration is that it is difficult to ensure synchronization when both particles and, cells are involved. Moreover, the corrector as well as time-step determinations are scalar operations when particles are advanced one at a time, whereas it is desirable to implement procedures for parallel or vector supercomputers. For these and other reasons we introduce a block time-step algorithm [McMillan, 1986]. This procedure anticipated the later quantization of time-steps in the Hermite integration scheme [Makino, 1991b]. Since the relevant aspects have already been discussed in chapter 2, it suffices to state that the time-steps take values $2 ^ { n } \Delta t _ { 0 }$ , where $\Delta t _ { 0 }$ is the smallest at a given time.

The scheduling itself is concerned with determining all the members of block $n$ , which are advanced together. A novel algorithm is adopted which does not appear to have been used by others. Thus at the $j$ th step, all particles in or below the $n _ { j } \mathrm { t h }$ block are updated, where $n _ { j }$ takes the successive values $1 , 2 , 1 , 3 , 1 , 2 , 1 , 3 , 1 , 4 , \dots$ This scheme is quite fast and is implemented by maintaining a sorted list $\{ i _ { \ell } \}$ of all the particles such that $\Delta t _ { i \ell } \leq \Delta t _ { i \ell + 1 }$ for $1 \le \ell < N$ . The block structure then consists of a second list of pointers $\left\{ p _ { k } \right\}$ to the ordered time-step list, so that particles $i _ { 1 } , i _ { 2 } , \ldots , i _ { p 1 }$ are in block 1, with time-step $\Delta t _ { 0 }$ , and particles $i _ { p 1 + 1 } , i _ { p 1 + 2 } , \ldots , i _ { p 2 }$ are in block 2, with time-step $2 \Delta t _ { 0 }$ , etc. Thus at step $j$ , the particles to be advanced are $i _ { 1 } , i _ { 2 } , \dotsc , i _ { n _ { j } }$ , where $n _ { j }$ is defined above. The advantage of this algorithm is that the choice of particles to be integrated does not require any further search.

For the scheduling to work, it is important that the time-step list $\{ i _ { \ell } \}$ be ordered such that the block boundaries are correct. Thus particles moving to a lower block are exchanged with the last element in the current block, and the block pointers are adjusted. If necessary, the process is repeated until the correct level has been reached. Likewise, particles moving to a higher block are treated similarly, except that to maintain synchronization at the next block-step, only one adjustment is allowed each time-step. Unlike the present procedure in standard Hermite integration, the natural steps of all particles are retained and are used for limiting the new step in order to ensure convergence. Finally, when a new block is added below block 1, $\Delta t _ { 0 }$ and the step counter $j$ must be replaced by $\scriptstyle { \frac { 1 } { 2 } } \Delta t _ { 0 }$ and $2 j$ , respectively. Hence at a given time $\Delta t _ { 0 }$ represents the smallest time-step.

Cells also have associated time-steps which must be scheduled in some way. It is convenient to employ the same scheme as above so that when a cell is rebuilt, its time-step and those of any descendants are determined and added to the block list. The block structure itself is defined by the particles and, because two-body regularization is used, the condition $\Delta t <$ $\Delta t _ { 0 }$ for cells never arises. Hence after a given block of particles has been advanced, we rebuild any cells that are due for updating.

Unlike the particles, cells can contain other cells, and some care is needed to avoid redundancies and inconsistencies, as for example attempting to reconstruct both a cell and its parent at the same time. One can easily avoid this by including a cell in the block list only if its time-step is smaller than that of any ancestor. All the affected cells can then be rebuilt at once, with the entire operation being completely vectorizable, which is desirable for some hardware.

It is quite inexpensive and highly advantageous to ensure that the tree is rebuilt at least as often as the whole system is synchronized; i.e. at the largest time-step. This is achieved by placing the root node in or below the top particle block. Since the tree is predicted to the same accuracy as the particles, we do not impose that the time-step of a particle be smaller than that of its parent cell. The situation can easily be remedied if it were desirable to construct the tree from synchronized particles, namely by requiring that no particle has a time-step exceeding that of its parent node. As can be seen, the present scheme is very flexible and can be modified to suit particular requirements.

Even if there were no numerical problems connected with hard binaries, their presence would cause complications in the construction and maintenance of the tree and block structure. It is therefore natural to implement two-body regularization in analogy with standard $N$ -body codes, and there is no reason why multiple regularization cannot be included. Since practical details of the KS method will be discussed elsewhere, it suffices to deal with some aspects relating to the tree code formulation.

As far as the tree structure is concerned, the c.m. of a regularized pair is treated as one particle since its internal motion is advanced separately. Regularization therefore places a lower limit of $a _ { \mathrm { h a r d } } \simeq r _ { \mathrm { h } } / N$ on the particle separation, where $r _ { \mathrm { h } }$ is the half-mass radius, and consequently this also prevents the time-step $\Delta t _ { 0 }$ from reaching rather small values. Although the tree sees a binary as a mass-point which is resolved into individual components when necessary, its quadrupole and octupole moments are included correctly in its parent cell.

A bonus of the tree formulation is that it dispenses with the perturber lists used in direct $N$ -body codes. This feature may not lead to much gain in efficiency since the AC method provides lists of relevant particles for perturber selection. However, there is the question of soft binaries for which the neighbour list allocation may not be sufficiently large. This problem may be partially circumvented by restricting regularization to hard binaries and, since the number of perturbers actually decreases with increasing $N$ , it is convenient to retain the standard perturber lists which are calculated from the tree.

Since regularization employs a non-linear internal time, the corresponding physical time-steps cannot be incorporated into the block scheme. However, regularized solutions are distinct from the other treatment and we simply perform all the necessary operations before beginning each block-step. Hence each KS solution is advanced until its next treatment time exceeds the current block time. This part may be vectorized if a large number of perturbed KS pairs require attention simultaneously.

Two particles are selected for KS treatment if their two-body motion is dominant, with time-steps $\Delta t _ { i } < \Delta t _ { \mathrm { c l } }$ , where the close encounter timestep is derived from the corresponding distance $R _ { \mathrm { c l } } \simeq 4 r _ { \mathrm { h } } / N$ , slightly modified by the density contrast. Use of this time-step criterion normally implies that the two particles are approaching each other with $R < { \cal R } _ { \mathrm { c l } }$ , unless other particles are involved. Because a relative time-step criterion is used, two such particles are normally in the same block, otherwise synchronization can be enforced at the previous step.

The presence of a KS pair requires minor modification of the cellopening algorithm in order to maintain continuity of the force. Since the KS pair will normally be resolved into its components, we require that the same be true of the separate components in the tree. This is achieved by opening any cell whose diameter $\mathcal { D }$ and distance $R$ from the particle in question satisfies $D + \alpha a \ : > \ : \theta R$ , where $\alpha \simeq 1$ and $a$ is the relevant semi-major axis.

The collisional tree code described above has reached a state of development where it may be used in large-scale simulations. Based on comparison tests with a fairly modest particle number (i.e. $N = 1 0 2 4$ ), the cross-over point with respect to standard summation is estimated to be in the region of $N \simeq 1 0 ^ { 4 }$ . One reason is the rather large scaling coefficient required for a high-order scheme. Even at this particle number, the tree code will barely reach its asymptotic $N \log N$ regime; hence a fairly powerful computer will be needed in order to exploit the performance. It is also very encouraging that the results of a core collapse calculation shows excellent agreement with direct integration. Further details of accuracy and timing can be found in the original paper [cf. McMillan & Aarseth, 1993]. Finally, the present formulation is suitable for both workstations and conventional supercomputers, and the time is now ripe for a more serious application to be attempted on faster hardware.

An earlier tree code development which was not pursued [Jernigan & Porter, 1989] also employed two-body regularization. This novel formulation is based on a recursive binary tree data structure and an accurate KS integration method for every level of the binary tree. Given that the computing time scaled as $T _ { \mathrm { c o m p } } \propto N ^ { 1 . 6 2 }$ for $N \leq 3 2 \mathrm { K }$ compared with $N ^ { 1 . 6 3 }$ for $\theta = 0 . 5$ above, this method deserves to be resurrected.

# 6.4 Flattened systems

Planetesimal systems exhibit two characteristic features that facilitate a tree-code approach. First, the dominance of the central body, be it a star or a planet, reduces the effects of the mutual interactions which can therefore be considered as perturbations during most of the motion. Such systems also tend to be disc-like and hence may require less computational effort for dealing with the vertical dimension than fully 3D systems. In the following we describe a unique tree code method [Richardson, 1993a,b] which has also been applied to the problem of planetary rings [Richardson, 1994]. More recently, the cosmological tree code PKDGRAV (discussed in a later chapter) was adapted to studying planetary formation as well as ring simulations [Richardson et al., 2000].

The planetesimal method combines two techniques in order to study large particle numbers efficiently. In the first place, the particle in box scheme [Wisdom & Tremaine, 1988] discussed in section 3.6 has been adopted to represent a small self-similar patch, thereby increasing the dynamical range significantly. Again the interactions are evaluated by the Barnes–Hut [1986] tree code, with periodic boundary conditions which include the effect of eight surrounding ghost boxes [Aarseth et al., 1993]. By referring the individual coordinates to the centre of a comoving Cartesian coordinate frame, the equations of motion take the linearized form (3.37). The sliding box procedure is carried out according to section 3.6, and particles leaving the central box are replaced by corresponding ghost images such that, apart from collisions, the particle number is preserved.

The multipole expansion includes terms up to quadrupole order as a compromise between complexity and efficiency. Once again, three derivatives of the quadrupole tensor are calculated explicitly and used for updating during the quadrupole prediction [cf. McMillan & Aarseth, 1993]. The integration scheme is based on the divided difference formulation of section 2.2. To speed up the treatment, a 2D tree is used to describe the flattened 3D system. This calls for special procedures, such as ‘effective size’ for each node that is recalculated during updates. The effective size is defined as the maximum of the actual size of the node and the predicted $y$ - or $z$ -extensions of each child from the c.m., whereas excursions in the radial $x$ -direction are usually small. This device prevents excessive subdivision for two particles that are arbitrarily close in 2D projection.

A variety of special features have been implemented in the planetesimal code. Most original is the concept of tree repair which is very useful in collision-dominated systems with small time-steps, since otherwise tree construction after every time-step would be extremely expensive. Thus if a particle crosses the boundary of its cell, the relevant nodes are updated consistently without affecting other parts of the tree. This entails destroying old nodes which become de-populated, or creating new ones.

The treatment of collisions also requires considerable care. Both dissipation and spin (discussed in section 17.4) are included for greater realism. In order to reduce the amount of collision overshooting, a more sensitive time-step criterion is employed inside small separations $r < 1 0 r _ { 0 }$ , with

$$
\Delta t = 2 ^ { - 1 0 r _ { 0 } / r } \eta r / \dot { r } ,
$$

where $r _ { 0 }$ is a typical particle size and $\eta$ is the tolerance factor ( $\simeq 0 . 0 2$ ). This results in significant improvement of angular momentum conservation at little extra effort since collisions are relatively rare. The choice of opening angle, $\theta = 0 . 6$ , shows factors of 2–3 speed-up with respect to the direct method for $N = 2 5 0$ . However, the asymptotic approach to the theoretical $N \log N$ algorithm may require even larger particle numbers [cf. McMillan $\&$ Aarseth, 1993].

The planetesimal tree code called $B O X \ – T R E E$ has also been applied to a simulation of Saturn’s B ring [Richardson, 1993a, 1994], which demonstrated its versatility. Here collisions are a main feature and the time-step criterion (6.13) proved inadequate at high densities. Instead the general expression (2.13) was found to be satisfactory, although it is relatively expensive in the tree code formulation. Another feature of general interest concerns the determination of post-collision velocities and spin rates when normal and transverse restitution coefficients appropriate to small bodies are prescribed. More details of this treatment are presented in section 17.4. Finally, we note that test results for low particle densities are in good agreement with the original box formulation, as well as an analytical model [Goldreich & Tremaine, 1978] when self-gravity is not included.

7

# Program organization

# 7.1 Introduction

We now make an abrupt transition to a presentation of various algorithms utilized by the direct summation codes. Before proceeding further, it will be useful to include some practical aspects in order to have a proper setting for the subsequent more technical procedures. First we introduce the main codes that have been developed for studying different gravitational $N$ -body problems. Where possible, the same data structure has been employed, except that the most recent versions are formulated in terms of the Hermite integration scheme. Since the largest codes are quite complicated, we attempt to describe the overall organization by tables and a flowchart to provide some enlightenment. Later sections give further details concerning input parameters, variables and data structure; each of these elements play an important role for understanding the general construction. We also discuss a variety of optional features which provide enhanced flexibility for examining different processes.

# 7.2 $N$ -body codes

Before describing the characteristics of the codes, we introduce some short-hand notation to illustrate the different solution methods employed [cf. Makino & Aarseth, 1992]. Thus by ITS we denote the basic individual time-step scheme, whereas ACS defines the Ahmad–Cohen [1973] neighbour scheme. Likewise, HITS and HACS are used for the corresponding Hermite integration methods. Finally, MREG refers to the implementations of unperturbed three-body [Aarseth & Zare, 1974] and four-body chain regularization [Mikkola & Aarseth, 1990], as well as perturbed chain regularization [Mikkola & Aarseth, 1993]. Also note that the latter contains (optionally) the slow-down procedures discussed earlier. Because of the programming complexities involved, only one multiple regularization of each type is currently permitted, but it is extremely rare for more than one such critical interaction to occur at the same time in standard cluster simulations. However, an extension to several compact subsystems or the introduction of wheel-spoke regularization (cf. section 5.4) would be beneficial for some problems. On the other hand, an arbitrary number of simultaneous KS solutions can be used to study large populations of primordial binaries [Aarseth, 1985a, 2001a; Wilkinson et al., 2003].

Table 7.1 summarizes the combination of integration schemes in the main codes, together with typical particle numbers for applications. The choice of names is historical but indicates an increasing degree of complexity in the solution methods, starting with one force polynomial. The codes NBODY 1 and NBODY 2 are of less interest here since they are based on a softened potential and are only suitable for collisionless systems. Moreover, a detailed description of these codes can be found elsewhere [Aarseth, 2001b]. Equivalent Hermite versions of NBODY 1 and NBODY 2 also exist [cf. Makino & Aarseth, 1992]. Likewise, the cosmological simulation code COMOV E discussed in section 3.3 is based on NBODY 2. Still, it is very useful to gain experience with simple codes before attempting more complicated tasks.

Star cluster simulations are facilitated by the introduction of two-body regularization [Aarseth, 1972b; Bettis & Szebehely, 1972]. The KS method adopted is of the same type as the corresponding direct $N$ -body integrator for compatibility; i.e. the older codes NBODY 3 and NBODY 5 are still entirely based on divided differences. Of the four point-mass codes, one (NBODY 3) is intended for small- $N$ systems, whereas another one (NBODY 4) has been adapted for the special-purpose HARP and GRAPE computers,∗ and is likewise based on brute-force solutions of the gravitational many-body problem. This leaves us with the three last codes for general use on laptops, workstations or conventional supercomputers.

It does not follow that a code for small particle numbers is much more compact since many of the key building blocks are essentially similar and the data structure is preserved. Thus the main technical difference between $N B O D Y 3$ and NBODY 5 is the lack of neighbour lists in the former, although the latter also contains additional astrophysics. Since $N$ is usually relatively modest when using NBODY 3 (i.e. $N ~ \leq ~ 1 0 0$ for efficiency reasons), the extra cost of obtaining perturber lists for two-body regularization by full summation is not a concern, otherwise one could devise an analogous strategy connected with the centre-of-mass (c.m.) motion.

Table 7.1. Direct N-body codes.   

<table><tr><td>Code</td><td>Characteristic description</td><td>Membership</td></tr><tr><td>NBODY1</td><td>ITS with softening</td><td>3-100</td></tr><tr><td>NBODY2</td><td>ACS with softening</td><td>50-104</td></tr><tr><td>NBODY3</td><td>ITS with KS and MREG</td><td>3-100</td></tr><tr><td>NBODY4</td><td>HITS with KS and MREG</td><td>10-105</td></tr><tr><td>NBODY5</td><td>ACS with KS and MREG</td><td>50－104</td></tr><tr><td>NBODY6</td><td>HACS with 1KS and MREG</td><td>50－104</td></tr><tr><td>NBODY7</td><td>As NBODY6 with BHbinary</td><td>50－104</td></tr></table>

In other words, the corresponding neighbour list could be renewed on a somewhat longer time-scale to mimic the regular time-step used by NBODY 2.

The codes NBODY 5 and NBODY 6 are mainly intended for star cluster simulations. The former has been a work-horse for more than 20 years now and the main features have been described elsewhere [cf. Aarseth, 1985a, 1994]. With the subsequent arrival of Hermite integration [Makino, 1991a; Makino & Aarseth, 1992], the code NBODY 6 appears to be more robust and at least as accurate for the same CPU time. Some general aspects have been discussed elsewhere [Aarseth, 1994, 1996b, 1999a,b] but a complete description is still lacking. After a period of testing and developments, it is now beginning to produce useful results [Kroupa, Aarseth & Hurley, 2001]. Although the actual integration methods differ somewhat, many other aspects of interest are in fact very similar and can be discussed together. The very recent code NBODY 7 [Aarseth, 2003a] contains the additional implementation of BH binary dynamics discussed in section 5.9 and there is also an equivalent GRAPE-6 version which has proved itself [cf. Aarseth, 2003b]. Finally, the HARP or GRAPE code NBODY 4 deals with several additional astrophysical processes that are of general interest and can be readily included in NBODY 6.

# 7.3 Flowcharts

A general description of complicated code structure is facilitated by recourse to flowcharts, supported by tables defining variables, as well as algorithms. The following schematic illustration shown in Fig. 7.1 provides an overview. The simplicity is deceptive and even the first segment contains a number of special features in the star cluster codes.

For convenience, we concentrate on describing the generally available code NBODY 6 but remark that NBODY 4 is broadly similar apart from lacking the AC neighbour scheme. Turning first to initialization, the main steps are outlined in Algorithm 7.1 for clarity, whereas the actual scaling from any initial units to $N$ -body units as well as the final astrophysical data conversion is detailed in section 7.4. In view of the variety of initial conditions, there is some provision for explicit generation (i.e. Plummer model); otherwise specially prepared data may be supplied (cf. Table 7.4). Independent optional features such as external tidal fields, primordial binaries (and hierarchical triples), stellar evolution and interstellar clouds are also catered for, as discussed further in the next chapter. Finally, force polynomials and time-steps are assigned and any hard primordial binaries initialized for KS treatment.

![](images/1efe5d370a4e95707ddaf440390d261569adb1be78c5c0178689f0f23ecb216a.jpg)  
Fig. 7.1. Schematic code structure.

Algorithm 7.1. Initialization procedures.   

<table><tr><td>1</td><td>Initialize useful counters and variables</td></tr><tr><td>2</td><td>Read input parameters and options</td></tr><tr><td>3</td><td>Obtain initial conditions (in situ or prepared file)</td></tr><tr><td></td><td>Scale all mi, ri, ri to N-body units</td></tr><tr><td>5</td><td>Define scaling factors for data conversion</td></tr><tr><td>6</td><td>Introduce external tidal field (optional)</td></tr><tr><td>7</td><td>Generate a primordial binary distribution (optional)</td></tr><tr><td>8</td><td>Assign stellar evolution parameters (optional)</td></tr><tr><td>9</td><td>Add a population of interstellar clouds (optional)</td></tr><tr><td>10</td><td>Evaluate force polynomials and specify time-steps</td></tr><tr><td>11</td><td>Regularize any close primordial binaries (optional)</td></tr></table>

Next we consider the more complicated part which deals with the different ways of obtaining numerical solutions. Since a full discussion of the data structure is deferred until later in this chapter, only some general aspects are included in the flowchart of Fig. 7.2.

Each integration cycle consists of advancing all equations of motion consistently up to the end of the block-step. The new cycle begins by selecting all single and c.m. particles due for treatment by the Hermite scheme (cf. section 9.2). Before dealing with the standard case, any KS or compact subsystem solutions are advanced. If the particle sequence is maintained (e.g. no physical collision), the coordinates and velocities of the relevant neighbours are predicted. Assuming a conventional computer, the irregular and regular integration of each particle is carried out sequentially. However, in order to preserve an invariant outcome, the current coordinates and velocities, $\mathbf { r } _ { i }$ , $\mathbf { v } _ { i }$ , for particles in the same block are only copied from the corresponding corrected values at the end of the block-step. In the case of KS termination or multiple subsystem initialization, the program flow is interrupted by special procedures discussed later. For completeness, we also mention new KS initialization here, although this task is in fact considered at the beginning of the block-step. This entails setting the time equal to the previous block time, whereupon the cycle starts again with a new sorted sequence. The cycle ends by checking the optional procedures for implementing stellar evolution.

![](images/418ec1245fd455136fc1866fd55c7fb95b56161f9b018719d105a1af10d58707.jpg)  
Fig. 7.2. Integration cycle.

The decision of whether to produce results is also taken just after the new block time has been determined. Thus if the next output time is exceeded, the integration cycle is suspended temporarily and the current time is redefined as the previous block time when all the relevant solutions are updated. Likewise, any additional data saved for later analysis may be initiated at this stage by introducing an appropriate time interval. This requires the prediction of all quantities to highest order, which is also needed for the energy check. At such times, most solutions will usually be known to order $\dot { \mathbf { F } }$ at least. A discussion of any other procedures is less relevant here and is therefore left to a later chapter.

A special indicator is used to facilitate program control. Historically this was introduced to overlay different modules in order to save valuable memory, hence the notation $I P H A S E$ for this indicator. It may be helpful to consult the list of possible values, given in Table 7.2.

Table 7.2. Indicator for flow control.   

<table><tr><td rowspan=1 colspan=1>0  Standard value1  New KS regularization2  KS termination3  Output and energy check</td></tr><tr><td rowspan=1 colspan=1>4  Three-body regularization</td></tr><tr><td rowspan=1 colspan=1>5  Four-body regularization</td></tr><tr><td rowspan=1 colspan=1>6  New hierarchical system</td></tr><tr><td rowspan=1 colspan=1>7  Termination of hierarchy</td></tr><tr><td rowspan=1 colspan=1>8  Chain regularization9  Physical collision-1  Exceptional cases</td></tr></table>

All these indicators are used and have the same meaning in the codes NBODY 3 and higher versions, and a few are also found in NBODY 2. It is convenient to employ a negative value for denoting exceptional cases, such as using only part of a routine, signalling additional procedures or denoting a change of the particle sequence (cf. section 7.7).

# 7.4 Scaling and units

The use of units in $N$ -body simulations has been rather non-uniform. Ideally, results should be presented in a way that at least facilitates comparison with other models, if not observations. The comparison problems were due to the theoretician’s preference for considering a wide variety of scales and reporting the results in terms of natural variables, unlike observers who are constrained by reality. Eventually, it was agreed by the small community of practitioners to employ so-called ‘standard $N$ -body units’ for the actual calculations [Heggie & Mathieu, 1986]. Briefly stated, the scaled total mass, $M$ , and equilibrium virial radius, $r _ { \mathrm { V } }$ , are taken to be unity, with the total energy $E _ { 0 } = - 0 . 2 5$ for bound systems.

Algorithm 7.2. Scaling to standard units.   

<table><tr><td>1</td><td>Initialize ri,ri in the inertial c.m.frame</td></tr><tr><td>2</td><td>Scale the masses by ∑i mi = 1, giving m =1/N</td></tr><tr><td>3</td><td>Calculate kinetic, potential and tidal energy T, U, W</td></tr><tr><td>4</td><td>Define the virial energy expression V = U + 2 W</td></tr><tr><td>4</td><td>Multiply the velocities by Qv = (Qvir|V|/T)1/2</td></tr><tr><td>5</td><td>Scale ri, ri to Eo = -0.25 using β= (1- Qvir)U/Eo</td></tr></table>

The steps for achieving the desired scaling are given by Algorithm 7.2. Here $Q _ { \mathrm { v i r } }$ is the specified virial ratio which is a half for overall equilibrium and $V = U + 2 W$ is the virial energy. Note that $W$ is not yet determined during the scaling procedure and is therefore only included with zero value to be formally correct. For open star clusters, the $z$ -component of the angular momentum is absorbed in the kinetic energy [cf. Chandrasekhar, 1942, eq. 5.535]. The last operation involves multiplying all coordinates by $\beta$ and dividing the velocities by $\beta ^ { 1 / 2 }$ . As a check, the total energy should now be† $E = - 0 . 2 5$ . In these units we have $\begin{array} { r } { \sigma ^ { 2 } = \frac { 1 } { 2 } } \end{array}$ for the mean square equilibrium velocity, which gives a constant crossing time

$$
t _ { \mathrm { c r } } = 2 r _ { \mathrm { V } } / \sigma = 2 \sqrt { 2 } .
$$

Since the central velocity dispersion in a bound cluster exceeds $\sigma$ by some factor (about 2 for a typical King [1966] model), we define the energy of a hard binary by (4.1). The corresponding scaled binding energy per unit mass is then obtained by the general expression

$$
h _ { \mathrm { h a r d } } = - 4 \operatorname* { m a x } { \{ T , | T + U | \} } / M ,
$$

which takes the dimensionless value $h _ { \mathrm { h a r d } } = - 1$ at equilibrium. Note that although $M = 1$ initially, the removal of escapers affects all the global quantities, including the total energy itself. For this reason, a consistent updating of the relevant parameters is desirable as the cluster evolves.

In the case of a cluster with regularized binaries, $T$ represents the sum of contributions from single particles and c.m. motions, whereas the potential energy, $U$ , excludes all internal two-body interactions. Hence the quantity $T + U + W$ is the total energy that binds the cluster and $2 Q _ { \mathrm { v i r } } - 1$ denotes the fractional departure from overall equilibrium in per cent. With regularized binaries present, the actual total energy is obtained by adding all the predicted two-body binding energies. Note that if the alternative definition of including all the potential energy in $U$ is used, the virial ratio $Q _ { \mathrm { v i r } } = T / | U + 2 W |$ may be dominated by a single eccentric binary.

The scaling of astrophysical quantities to internal units is often a source of confusion. The main reason for this is due to taking $G = 1$ for the gravitational constant. Such problems are readily resolved by performing dimensional analysis. Let us now introduce some basic relations in terms of physical units. A cluster is essentially defined by the two global parameters $R _ { \mathrm { V } }$ and $M _ { \mathrm { S } }$ together with $N$ , which are usually specified as input (see next section). For most work in stellar dynamics, it is convenient to express the length scale, $R _ { \mathrm { V } }$ , in pc and mean stellar mass, $M _ { \mathrm { S } }$ , in $M _ { \odot }$ , from which all quantities of interest can be derived. Distances and masses are then simply obtained from the $N$ -body units by $\tilde { r } = R _ { \mathrm { V } } r$ and $\tilde { m } = M _ { \mathrm { S } } \bar { m }$ .

For the velocity we determine the conversion factor in $\mathrm { k m s ^ { - 1 } }$ from

$$
\tilde { V } ^ { * } = 1 \times 1 0 ^ { - 5 } ( G M _ { \odot } / L ^ { * } ) ^ { 1 / 2 } ,
$$

where $L ^ { * }$ is a length scale. With $G , M _ { \odot } , L ^ { * }$ expressed in cgs units and choosing $L ^ { * } = 1 \mathrm { p c }$ , this gives $\tilde { V } ^ { * } = 6 . 5 5 7 \times 1 0 ^ { - 2 }$ . Taking account of the total mass and cluster length scale then yields the scaling relation

$$
V ^ { * } = 6 . 5 5 7 \times 1 0 ^ { - 2 } ( N M _ { \mathrm { S } } / R _ { \mathrm { V } } ) ^ { 1 / 2 } .
$$

The scaling of time is also done in two stages as follows. First the fiducial time factor is taken to be $\tilde { T } ^ { * } = ( L ^ { * 3 } / G M _ { \odot } ) ^ { 1 / 2 }$ , or 14.94 in units of Myr. Converting to the cluster parameters, we obtain

$$
T ^ { * } = 1 4 . 9 4 ( R _ { \mathrm { V } } ^ { 3 } / N M _ { \mathrm { S } } ) ^ { 1 / 2 } .
$$

Hence the velocity in units of $\mathrm { k m s ^ { - 1 } }$ and the time in Myr are obtained by $\tilde { v } = \tilde { V } ^ { * } v$ and $\tilde { t } = \tilde { T } ^ { * } t$ , where $\boldsymbol { v }$ and $t$ are in $N$ -body units. Finally, the relation for the crossing time in Myr becomes

$$
T _ { \mathrm { c r } } = 2 \sqrt { 2 } T ^ { * } .
$$

Applying the basic conversion factors $M _ { \mathrm { S } } , R _ { \mathrm { V } } , V ^ { * } , T ^ { * }$ and dimensional analysis, we can now evaluate all the relevant quantities in convenient physical units. Note that individual masses, $m _ { i }$ , may be expressed in scaled $N$ -body or astrophysical units, depending on the context.

# 7.5 Input parameters and options

Each code has its own choice of input parameters that can take a range of values according to the desired objective. In practice it is useful to be aware of any limitations and a well-designed code should include consistency checks to prevent inappropriate usage. However, one should also allow a certain flexibility for experimentation; hence any restrictions are often curtailed by compromise. It is useful to distinguish between parameters specifying the model to be investigated and those that control the solutions. Alternatively, an optional facility for including a prepared set of initial conditions can be used to over-ride the choice of model parameters, since only a few explicit models are generated in situ.

Table 7.3 gives suggested numerical values for the main variables controlling the integration in the codes $N B O D Y 5$ and NBODY 6 in the case $N = 1 0 0 0$ and, as can be seen, the simplicity is evident. Given the standard scaling to $N$ -body units discussed above, only a few of these quantities depend on the particle number. First, the central value of the initial neighbour sphere may be taken as $S _ { 0 } \simeq 0 . 3 ( N / 1 0 0 0 ) ^ { 1 / 3 }$ for the standard scaling $r _ { \mathrm { V } } = 1$ . At larger distances, the initial neighbour radius is modified according to the expression $S ^ { 2 } = S _ { 0 } ^ { 2 } \left( 1 + r ^ { 2 } \right)$ if the system is centrally concentrated.

A good choice for the maximum neighbour number is $n _ { \mathrm { m a x } } \simeq 2 N ^ { 1 / 2 }$ , but this has not been investigated above $N \simeq 1 0 0 0$ . $^ \ddagger$ However, in the case of primordial binaries with a general IMF it is desirable to employ more generous values of $n _ { \mathrm { m a x } }$ since even a hard binary may have a relatively large semi-major axis that requires many perturbers inside the distance $\lambda a ( 1 + e )$ , where $\lambda$ is a dimensionless quantity. From the basic close encounter distance $R _ { \mathrm { c l } } = 4 r _ { \mathrm { h } } / N$ defined by (1.9) and dimensional analysis, the corresponding time-step for typical parabolic motion is determined empirically as $\Delta t _ { \mathrm { c l } } \simeq 0 . 0 4 ( R _ { \mathrm { c l } } ^ { 3 } / \bar { m } ) ^ { 1 / 2 }$ , where $m$ is the mean mass. A slightly smaller value of $R _ { \mathrm { c l } }$ is used in practice (cf. (9.3)). Note that a binary with mass components $m _ { i } = 1 0 \bar { m }$ would already be hard at a semi-major axis $a \simeq 1 0 0 / N$ .

The codes contain an option for automatic adjustments of all regularization parameters, carried out at intervals $\Delta t _ { \mathrm { a d j } }$ . The regularized time-step, to be defined in a later section, is chosen such that there are $2 \pi / \eta _ { U }$ steps per unperturbed orbit. The suggested value refers to the Hermite Stumpff integration, whereas $\eta _ { U } = 0 . 1$ is appropriate for the other KS methods. The value of $h _ { \mathrm { h a r d } }$ follows directly from $\epsilon _ { \mathrm { h a r d } } / \bar { \mu }$ , with $\mu$ the mean reduced mass (cf. (4.1)). Most of the remaining quantities are a matter of personal taste but have been included for completeness.

As can be seen, the most important parameters are either dimensionless or have dynamical significance. Hence a change to different particle numbers requires minor modifications of the basic input template. Needless to say, a number of additional features are included in order to permit different effects to be studied, whereas others ensure a smooth running of the code. These are optional and offer facilities for a wide variety of paths to be decided on initially and, if desired, can also be changed during the calculation after a temporary halt which saves the current state. Since many of the relevant procedures will be discussed in later sections, Table 7.4 includes a representative subset (out of 40 options) for inspection. We remark that options offer greater flexibility than logical variables, since the former can be assigned multiple values and defined in order of increasing complexity. Naturally, care must be exercised to ensure that the different options are mutually consistent. This is usually achieved by constructing a template when investigating a specific problem.

Table 7.3. Integration parameters.   

<table><tr><td>n1 NR S</td><td>Time-step parameter for irregular force Time-step parameter for regular force Initial radius of the neighbour sphere</td><td>0.02 0.03 0.3</td></tr><tr><td>nmax</td><td>Maximum neighbour number</td><td>70.0</td></tr><tr><td>△tadj</td><td>Time interval for energy check</td><td>2.0</td></tr><tr><td>△tout</td><td>Time interval for main output</td><td>10.0</td></tr><tr><td>QE</td><td>Tolerance for energy check</td><td>1.0 ×10-5</td></tr><tr><td>Rv</td><td>Virial cluster radius in pc</td><td>2.0</td></tr><tr><td>Ms</td><td>Mean stellar mass in solar units</td><td>0.8</td></tr><tr><td>Qvir</td><td>Virial theorem ratio (T/|U + 2Wl)</td><td>0.5</td></tr><tr><td>△tcl</td><td>Time-step criterion for close encounters</td><td>4.0 ×10-5</td></tr><tr><td>Rcl</td><td>Distance criterion for KS regularization</td><td>0.001</td></tr><tr><td>nu</td><td>Regularized time-step parameter</td><td>0.2</td></tr><tr><td>hhard</td><td>Energy per unit mass for hard binary</td><td>-1.0</td></tr><tr><td>7min</td><td>Limit for unperturbed KS motion</td><td>1.0 ×10-6</td></tr><tr><td>7max</td><td>Termination criterion for soft binaries</td><td>0.01</td></tr></table>

# 7.6 Basic variables

All $N$ -body codes require a number of variables for each particle, the minimum being just six if equal masses are chosen. In the following we concentrate on describing NBODY 6, although NBODY 5 contains exactly the same direct integration variables. For ease of reference, these are listed in Table 7.5 together with a brief definition. The actual variables employed by the codes are also included for convenience according to the programming style of upper case for all FORTRAN statements.

Given the theoretical exposition of the preceding chapters, the comments to all the entries are self-explanatory. Because of the static memory allocation in older FORTRAN versions, maximum array sizes are specified before compilation. A number of FORTRAN parameters are included in a header file params. $h$ and these are defined in Table 7.6. For illustration, Column 3 contains representative values for a cluster simulation that allows up to $N _ { \mathrm { s } } = 1 0 0 0$ single particles and $N _ { \mathrm { b } } = 1 0 0 0$ hard primordial binaries to be studied. Since every new KS solution also requires a corresponding c.m. particle to be introduced, the storage requirement is for $N _ { \mathrm { s } } + 3 N _ { \mathrm { b } }$ particle arrays. Moreover, some allocation should also be made for additional regularizations during the early stages since all the original binaries may still be present.

All the important variables are kept together in a global common block common6.h to facilitate data communication and restart of a calculation from the saved state. Since the integration variables represent $4 8 N$ doubleprecision words (cf. section 3.2), this part is of size $9 6 N$ words. In addition, the recommended neighbour list allocation is of size $2 ( N _ { \mathrm { s } } + N _ { \mathrm { b } } ) ^ { 1 / 2 }$ , with some extra locations for algorithmic complications.

Table 7.4. Optional features.   

<table><tr><td>1 Manual common save on unit 1 at any time 2 Common save on unit 2 at output time or restart 3 Data bank on unit 3 with specified frequency 5 Different types of initial conditions Output of Lagrangian radii 8 Primordial binaries (extra input required) 10 Regularization diagnostics 11 Primordial triples (extra input required) 13 Interstellar clouds (extra input required) 14 External tidal force; open or globular clusters 15 Multiple regularization or hierarchical systems 16 Updating of regularization parameters Rcl, △tcl 17 Modification of η1 and nr by tolerance QE 19 Synthetic stellar evolution with mass loss 20 Different types of initial mass functions 22 Initial conditions mi,ri,r; from prepared data 23 Removal of distant escapers (isolated or tidal) 26 Slow-down of KS and/or chain regularization 27 Tidal circularization (sequential or continuous) 28 Magnetic braking and gravitational radiation</td></tr></table>

The corresponding common variables for the KS scheme are given in Table 7.7. In addition to the 18 basic entries there are another ten arrays pertaining to the Stumpff method. This makes a total of 110 words for each KS solution, compared with 94 words for the difference formulation. As in direct integration, we use the convention ‘force’ to denote acceleration. Note that standard variables such as $t _ { 0 } , \Delta t$ and $L$ are also used for KS solutions, with the convention that the first component, $m _ { k }$ , is referred to; i.e. $k = 2 I _ { \mathrm { p } } - 1$ for pair index $I _ { \mathrm { p } }$ . This scheme was introduced before primordial binaries became relevant, but in any case disc space is not usually an issue for direct $N$ -body simulations.

A modern code employs a large number of unique variable names to define useful quantities, most of which are scalars. Accordingly, the choice is between local and global allocation. The strategy of the present design is to keep all essential variables for direct and KS integration in one common block, whereas the more complicated chain regularization is described by temporary common variables. Since most chain interactions are of short duration, this usage enables a calculation to be restarted from the latest common save by continuing the high-order integration cycle as if no interruption had occurred, so that the end result should be identical to a continuous calculation. This is usually achieved even in the large codes and it is highly desirable that a given outcome be reproducible, at least over short intervals in order to deal with any technical problems. Provisions are also included for changing a variety of input variables and options at restart time. Such a procedure makes it possible to study the effect of varying some condition at a given stage in the evolution, or simply extend the simulation beyond the prescribed termination time.

Table 7.5. Basic variables.   

<table><tr><td>X0 X0 V0 X X V F F F(1) m △t to T0 F1 FI D1 D2 D3 D3 △T T FR FR D D3R RS</td><td>Primary coordinates XODOT Primary velocity Coordinates for predictions XDOT Velocity for predictions One half the total force (per unit mass) FDOT One sixth the total force derivative BODY Particle mass (also initial mass mo) STEP Irregular time-step Time of last irregular force calculation Irregular force FIDOT First derivative of irregular force Second derivative of irregular force Third derivative of irregular force STEPR Regular time-step TOR Time of last regular force calculation Regular force FRDOT First derivative of regular force D2R Second derivative of regular force Third derivative of regular force</td></tr></table>

Table 7.6. FORTRAN parameters.   

<table><tr><td>Nmax Kmax Lmax Mmax Hierarchicalbinaries Mdis Recently disrupted KS components</td><td>Total particle number and c.m.bodies 4010 KS solutions 1010 Neighbour lists 100</td></tr></table>

Table 7.7. KS regularization variables.   

<table><tr><td>Uo U</td><td>UO U</td><td>Primary regularized coordinates Regularized coordinates for predictions</td></tr><tr><td>U&#x27;</td><td>UDOT</td><td>Regularized velocity</td></tr><tr><td>Fu</td><td>FU</td><td>One half the regularized force</td></tr><tr><td>Fu (2)</td><td>FUDOT</td><td>One sixth the regularized force derivative</td></tr><tr><td>E UJ</td><td>FUDOT2</td><td>Second derivative of regularized force</td></tr><tr><td>F (3) U</td><td>FUDOT3</td><td>Third derivative of regularized force</td></tr><tr><td>h</td><td>H</td><td>Binding energy per unit reduced mass</td></tr><tr><td>h&#x27;</td><td>HDOT</td><td>First derivative of the specific binding energy</td></tr><tr><td>h(2)</td><td>HDOT2</td><td>Second derivative of the binding energy</td></tr><tr><td>h(3)</td><td>HDOT3</td><td>Third derivative of the binding energy</td></tr><tr><td>h(4)</td><td>HDOT4</td><td>Fourth derivative of the binding energy</td></tr><tr><td>△T</td><td>DTAU</td><td>Regularized time-step</td></tr><tr><td>t(2)</td><td>TDOT2</td><td>Second regularized derivative of physical time</td></tr><tr><td>t(3)</td><td>TDOT3</td><td>Third regularized derivative of physical time</td></tr><tr><td>R</td><td>R</td><td>Two-body separation</td></tr><tr><td>Ro</td><td>RO</td><td>Initial value of the two-body separation</td></tr><tr><td>Y</td><td>GAMMA</td><td>Relative perturbation</td></tr></table>

# 7.7 Data structure

Elegant code design assists greatly in delineating the complex paths that are an inevitable feature of any such large undertaking. To this end, the data structure itself plays a vital role. Thus we need to allow for a changing situation in which new KS solutions appear or are terminated and escaping particles are removed during the calculation. These requirements make it desirable to abandon a rigid data structure in favour of a flexible scheme. There are essentially two ways to overcome this problem. We can either adopt the style of $C$ -programming and introduce pointers, or modify the relevant particle arrays according to the changing situation. $\ S$ Apart from questions of hardware and efficiency, a FORTRAN program is easier to follow if the arrays can be maintained in an ordered fashion. However, the latter strategy does involve extra cost as well as programming complexities. Fortunately the cost of the relabelling scheme is relatively modest in practice since the number of new KS and other regularized solutions is usually small even with primordial binaries.

![](images/539186cf6ab53d72be80839fb3094604edb83454145f8fd040e765739951a882.jpg)  
Fig. 7.3. Ordering of KS pairs. The figure shows the data structure for (a) creation of new pair, and (b) KS termination.

The present data organization is based on updating the particle arrays to give a sequential representation [cf. Aarseth, 1985a]. This is achieved by re-ordering all the relevant variables at each new change of configuration. For each KS pair, $I _ { \mathrm { p } }$ , the corresponding c.m. location is situated at $N + I _ { \mathrm { p } }$ . Hence given the particle number, $N$ , and number of pairs, $N _ { \mathrm { p } }$ , the first single particle is located at $I _ { \mathrm { s } } = 2 N _ { \mathrm { p } } + 1$ and the last c.m. at $N + N _ { \mathrm { p } }$ .

Figure 7.3 illustrates the general case of increasing or reducing the number of regularized solutions with other pairs present. At a given time, all the KS components occupy the $2 N _ { \mathrm { p } }$ first sequential locations, followed by the single particles. In Fig. 7.3(a), the particle pair $k , l$ has been selected for regularization. Consequently, all particle arrays at locations $2 N _ { \mathrm { p } } + 1$ and $2 N _ { \mathrm { p } } + 2$ are exchanged with those of the regularization candidates and the corresponding c.m. is introduced at $N + N _ { \mathrm { p } } + 1$ . At an appropriate stage during the initialization, the current pair index, $N _ { \mathrm { p } }$ , is increased by one. In the reverse case of terminating an existing KS solution, as in Fig 7.3(b), all more recent pairs are moved up to liberate the locations $2 N _ { \mathrm { p } } - 1$ and $2 N _ { \mathrm { p } }$ for the terminated components at $2 I _ { \mathrm { p } } - 1$ and $2 I _ { \mathrm { p } }$ , which now become the first single particles, whereupon the corresponding c.m. is removed by compression.

The data structure enables a sequential force summation to be carried out from $I _ { \mathrm { s } }$ to $N _ { \mathrm { t o t } } = N + N _ { \mathrm { p } }$ , provided due care is exercised for $i > N$ . In this case, if $r _ { i j } ^ { 2 } > \lambda ^ { 2 } R ^ { 2 }$ , the force is obtained by including the mass-point contribution, otherwise the two components are first resolved. The c.m. approximation parameter is related to the unperturbed two-body limit for consistency and given by λ = γ−1/3min

The advantage of having a well-ordered scheme is evident. Given that the cost of a new initialization is $O ( N )$ , the required switching of arrays does not add significantly since the effort of obtaining the force polynomials themselves dominates on a conventional computer. However, there are additional costs of updating all the internal neighbour and perturber lists due to the changed locations of a few particles. Fortunately this effort can be speeded up in many ways by taking advantage of the sequential ordering, and in any case these operations are fast because only integer arithmetic is involved. Hence the cost of all KS-related initializations in a large simulation is essentially negligible since the total number of such episodes is relatively small even when the number of binaries is large.

In the case of escaper removal, the common arrays of bound cluster members are compressed. Now there is no polynomial initialization but again all relevant lists must be made consistent with the new sequence. Since both the particle number and relevant locations change with time, it is convenient to define a unique label or so-called ‘name’, ${ \mathcal { N } } _ { i }$ , at the beginning. Thus we adopt ${ \mathcal { N } } _ { i } = i$ for all initial binary components and single particles and $\mathcal { N } _ { j } = \mathcal { N } _ { 2 k - 1 } + N _ { 0 }$ for the c.m. of each KS pair, $k$ , where $N _ { 0 }$ is the initial particle number. This is particularly useful for identification of binary components that may be involved in exchange or collisions. Further details of reconfiguration and escape procedures will be given in later sections, together with a discussion of the data structure for hierarchies.

# 8 Initial setup

# 8.1 Introduction

A variety of procedures need to be carried out before the calculation proper can begin. The prescriptions for input parameters and options are discussed in chapter 7. Here we concentrate on different types of initial conditions for star cluster simulations, whereas planetary systems are described elsewhere. The cluster models are first generated for single stars with a specified initial mass function (hereafter IMF) and scaled to internal units. Since a variety of distributions may be considered, we provide several detailed algorithms. Next we present some procedures for including a realistic distribution of primordial binaries. Modelling of star clusters also requires external effects to be added. We distinguish between the motion of open clusters in circular orbits and globular clusters in 3D, with the galactic tidal force truncating the outer parts. Interstellar clouds form another perturbing agent which may be taken into account. Finally, with these procedures completed, the force polynomials for direct solutions as well as for any dominant two-body motions can be initialized.

# 8.2 Initial conditions for clusters

Although the choice of starting configurations for star cluster simulations is extremely wide, we may be guided by certain principles and observational constraints. Such models are usually represented by a smooth IMF and centrally concentrated density distribution. Depending on the objectives, the velocities may represent approximate equilibrium or initial collapse, whereas cosmological models are characterized by expansion.

The subject of the IMF has a long and chequered history. On the computational side, it has been known for a long time [Wielen, 1967; Aarseth, 1973] that a general mass spectrum increases the evolution rate significantly. The question of the upper and lower mass limits is still a matter for debate. However, the consensus is emerging that the low-mass stars do not form a significant proportion of the total mass [Kroupa, 2001a]. As far as small clusters are concerned, a few massive stars may play an important role due to mass loss on short time-scales. Going to larger clusters ( $N \simeq 1 0 ^ { 4 }$ ), this effect is probably less and we may consider a power-law distribution where the maximum stellar mass is a stochastic variable.

Guided by analysis of observational data, the simplest choice for open clusters is a classical Salpeter-type IMF, given by the power law

$$
f ( m ) \propto m ^ { - \alpha }
$$

for a specified mass range $[ m _ { 1 } , m _ { N } ] .$ . The exponent is traditionally taken as $\alpha = 2 . 3$ [Salpeter, 1955]. The corresponding distribution for each member $i$ is readily obtained by the expression

$$
m _ { i } ^ { - ( \alpha - 1 ) } = m _ { 1 } ^ { - ( \alpha - 1 ) } - ( i - 1 ) g _ { \cal N } ,
$$

with

$$
g _ { N } = ( m _ { 1 } ^ { - ( \alpha - 1 ) } - m _ { N } ^ { - ( \alpha - 1 ) } ) / ( N - 1 ) .
$$

A more realistic alternative is provided by the mass generating function [Kroupa, Tout $\&$ Gilmore, 1993]

$$
m ( X ) = 0 . 0 8 + \frac { \gamma _ { 1 } X ^ { \gamma _ { 2 } } + \gamma _ { 3 } X ^ { \gamma _ { 4 } } } { ( 1 - X ) ^ { 0 . 5 8 } } ,
$$

with the random number $X$ uniform in $[ 0 , 1 ]$ . The best-fit coefficients for the solar neighbourhood are given by $\gamma _ { 1 } = 0 . 1 9 , \gamma _ { 2 } = 1 . 5 5 , \gamma _ { 3 } = 0 . 0 5 , \gamma _ { 4 } =$ 0.6. If desired, values outside a specified range may be rejected, with $m _ { N } \ >$ 0.08 as the lower limit. A more flexible form of the fitting function (8.4) has also been developed to allow for any five-part power-law in specified mass intervals [Kroupa, 2001a,b]. As an example, a smaller effective power-law index is indicated below $0 . 5 M _ { \odot }$ ; i.e. $\alpha = 0 . 3$ for the mass range $0 . 0 1 -$ $0 . 0 8 M _ { \odot }$ and $\alpha = 1 . 3$ for $0 . 0 8 \substack { - 0 . 5 M _ { \odot } }$ . Consequently, the mass fraction in brown dwarfs below $0 . 0 8 M _ { \odot }$ would be less than $6 \%$ with a corresponding membership fraction of $3 7 \%$ . Instead of using $\alpha = 2 . 3$ for all masses above $0 . 5 M _ { \odot }$ , there is some evidence for $\alpha \simeq 2 . 5 - 2 . 7$ above $1 M _ { \odot }$ . Note that in the case of the standard IMF given by (8.2) it is convenient to specify the mean mass (in solar units) as an input parameter, whereas this quantity is redetermined from the actual distribution when using the relation (8.4).

The initial density distribution is usually taken to be fairly spherical with some degree of central concentration. Traditionally, the Plummer model [Plummer, 1911] has served this purpose well. We therefore begin this exercise by giving the complete algorithm before turning to more versatile models [Aarseth, H´enon $\&$ Wielen, 1974].

The space density of the Plummer model is given by

$$
\rho ( r ) = \frac { 3 M } { 4 \pi r _ { 0 } ^ { 3 } } \frac { 1 } { [ 1 + ( r / r _ { 0 } ) ^ { 2 } ] ^ { 5 / 2 } } ,
$$

where $r _ { 0 }$ is a scale factor related to the half-mass radius by $r _ { \mathrm { h } } \simeq 1 . 3 r _ { 0 }$ [Aarseth & Fall, 1980]. In the following we adopt the scaling $M \ = \ 1$ , $r _ { 0 } = 1$ , which gives the mass inside a sphere of radius $r$ as

$$
M ( r ) = r ^ { 3 } ( 1 + r ^ { 2 } ) ^ { - 3 / 2 } .
$$

First a radius, $r$ , is chosen by setting $M ( r ) = X _ { 1 }$ , where $X _ { 1 }$ is a random number in [0, 1]. Substituting into (8.6) and simplifying we obtain

$$
r = ( X _ { 1 } ^ { - 2 / 3 } - 1 ) ^ { - 1 / 2 } .
$$

A rejection may be applied in rare cases of large distances (e.g. $r > 1 0 r _ { \mathrm { h } }$ ). The three spatial coordinates $x , y , z$ are now selected by choosing two normalized random numbers, $X _ { 2 } , X _ { 3 }$ , and writing

$$
\begin{array} { l } { { z = ( 1 - 2 X _ { 2 } ) r , } } \\ { { x = ( r ^ { 2 } - z ^ { 2 } ) ^ { 1 / 2 } \cos 2 \pi X _ { 3 } , } } \\ { { y = ( r ^ { 2 } - z ^ { 2 } ) ^ { 1 / 2 } \sin 2 \pi X _ { 3 } . } } \end{array}
$$

Let us assume isotropic velocities. From the corresponding potential $\Phi = - ( 1 + r ^ { 2 } ) ^ { - 1 / 2 }$ in scaled units, the escape velocity is given by $v _ { \mathrm { e } } =$ $2 ^ { 1 / 2 } ( 1 + r ^ { 2 } ) ^ { - 1 / 4 }$ . Since the system is assumed to be in a steady state, we have $f ( \mathbf { r } , \mathbf { v } ) \propto ( - E ) ^ { 7 / 2 }$ for the distribution function [Binney & Tremaine, 1987], where $E$ is the specific energy. Hence the probability distribution of the dimensionless velocity ratio $q = v / v _ { \mathrm { e } }$ is proportional to

$$
g ( q ) = q ^ { 2 } ( 1 - q ^ { 2 } ) ^ { 7 / 2 } .
$$

To obtain the velocities we use von Neumann’s rejection technique and note that $g ( q ) \ < \ 0 . 1$ with $q$ in [0, 1]. Let $X _ { 4 } , X _ { 5 }$ be two normalized random numbers. If $0 . 1 X _ { 5 } \ < \ g ( X _ { 4 } )$ we take $q = X _ { 4 }$ ; otherwise a new pair of random numbers is chosen. The isotropic velocity components $v _ { x } , v _ { y } , v _ { z }$ are obtained by employing the principle of (8.8) above, using two further random numbers, $X _ { 6 } , X _ { 7 }$ . If a general mass function is chosen, the individual masses can also be assigned sequentially since the system has some discreteness. This introduces further statistical fluctuations in the density distribution but, as can be verified, departures from overall equilibrium during the first crossing time are small if $Q _ { \mathrm { v i r } } = 0 . 5$ .