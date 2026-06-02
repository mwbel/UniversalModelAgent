# Chapter 1

# Differential and Difference Equations

10 Differential Equation Problems

100 Introduction to differential equations

As essential tools in scientific modelling, differential equations are familiar to every educated person. In this introductory discussion we do not attempt to restate what is already known, but rather to express commonly understood ideas in the style that will be used for the rest of this book.

The aim will always be to understand, as much as possible, what we expect to happen to a quantity which satisfies a differential equation. At the most obvious level, this means predicting the value this quantity will have at some future time. However, we are also interested in more general questions such as the adherence to possible conservation laws or perhaps stability of the long-term solution. Since we emphasize numerical methods, we often discuss problems with known solutions mainly to illustrate qualitative and numerical behaviour.

Even though we sometimes refer to ‘time’ as the independent variable, that is, as the variable on which the value of the ‘solution’ depends, there is no reason for insisting on this interpretation. However, we generally use $x$ to denote the ‘independent’ or ‘time’ variable and $y$ to denote the ‘dependent variable’. Hence, differential equations will typically be written in the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

where

$$
y ^ { \prime } = { \frac { d y } { d x } } .
$$

Sometimes, for convenience, we omit the $x$ in $y ( x )$ .

The terminology used in (100a) is misleadingly simple, because y could be a vector-valued function. Thus, if we are working in RN, and x is permitted to take on any real value, then the domain and range of the function f which

defines a differential equation and the solution to this equation are given by

# f : R  R N  R N , y : R → RN .

Since we might be interested in time values that lie only in some interval $[ a , b ] ,$ we sometimes consider problems in which y : $[ a , b ] \to \mathbb { R } ^ { N } ,$ and f : $[ \overline { { a , b } } ]$ ×RN → RN . When dealing with specific problems, it is often convenient to focus, not on the vector-valued functions f and $y ,$ but on individual components. Thus, instead of writing a differential equation system in the form of (100a), we can write coupled equations for the individual components:

A differential equation for which f is a function not of $x ,$ but of y only, is said to be ‘autonomous’. Some equations arising in physical modelling are more naturally expressed in one form or the other, but we emphasize that it is always possible to write a non-autonomous equation in an equivalent autonomous form. All we need to do to change the formulation is to introduce an additional component $y _ { N + 1 }$ into the y vector, and ensure that this can always maintain the same value as $x ,$ by associating it with the differential equation $y _ { N + 1 } ^ { \prime } =$ 1. Thus, the modified system is

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = f _ { 1 } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { y _ { 2 } ^ { \prime } ( x ) = f _ { 2 } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { \qquad \vdots } \\ & { { y _ { N } ^ { \prime } ( x ) = f _ { N } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } } \\ & { y _ { N + 1 } ^ { \prime } ( x ) = 1 . } \end{array}
$$

A system of differential equations alone does not generally define a unique solution, and it is necessary to add to the formulation of the problem a number of additional conditions. These are either ‘boundary conditions’, if further information is given at two or more values of $x$ , or ‘initial conditions’, if all components of $y$ are specified at a single value of $x$ .

If the value of $y ( x _ { 0 } ) = y _ { 0 }$ is given, then the pair of equations

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

is known as an ‘initial value problem’. Our main interest in this book is with exactly this problem, where the aim is to obtain approximate values of $y ( x )$

for specific values of $x$ , usually with $x > x _ { 0 }$ , corresponding to the prediction of the future states of a differential equation system.

Note that for an $N$ -dimensional system, the individual components of an initial value vector need to be given specific values. Thus, we might write

![](images/f7d2e32b346925824aaec87f4e7aaad8c07f787c07282d1bee9db690d134502e.jpg)

When the problem is formally converted to autonomous form (100c), the value of $\eta _ { N + 1 }$ must be identical to $x _ { 0 }$ , otherwise the requirement that $y _ { N + 1 } ( x )$ should always equal $x$ would not be satisfied.

For many naturally occurring phenomena, the most appropriate form in which to express a differential equation is as a high order system. For example, an equation might be of the form

$$
y ^ { ( n ) } = \phi \left( x , y , y ^ { \prime } , y ^ { \prime \prime } , \ldots , y ^ { ( n - 1 ) } \right) ,
$$

with initial values given for $y ( x _ { 0 } ) , y ^ { \prime } ( x _ { 0 } ) , y ^ { \prime \prime } ( x _ { 0 } ) , \ldots , y ^ { ( n - 1 ) } ( x _ { 0 } )$ . Especially important in the modelling of the motion of physical systems subject to forces are equation systems of the form

$$
\begin{array} { c } { y _ { 1 } ^ { \prime \prime } ( x ) = f _ { 1 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ { y _ { 2 } ^ { \prime \prime } ( x ) = f _ { 2 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ { \vdots \qquad \vdots } \\ { y _ { N } ^ { \prime \prime } ( x ) = f _ { N } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \end{array}
$$

where the equations, though second order, do have the advantages of being autonomous and without $y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } , \ldots , y _ { N } ^ { \prime }$ occurring amongst the arguments of $f _ { 1 } , f _ { 2 } , \ldots , f _ { N }$ .

To write (100f) in what will become our standard first order system form, we can introduce additional components $y _ { N + 1 } , y _ { N + 2 } , \ldots , y _ { 2 N } .$ . The differential equation system (100f) can now be written as the first order system

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = y _ { N + 1 } , } \\ & { y _ { 2 } ^ { \prime } ( x ) = y _ { N + 2 } , } \\ & { \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { y _ { N } ^ { \prime } ( x ) = y _ { 2 N } , } \\ & { y _ { N + 1 } ^ { \prime } ( x ) = f _ { 1 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { y _ { N + 2 } ^ { \prime } ( x ) = f _ { 2 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { \quad \quad \quad \quad \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

# 101 The Kepler problem

The problems discussed in this section are selected from the enormous range of possible scientific applications. The first example problem describes the motion of a single planet about a heavy sun. By this we mean that, although the sun exerts a gravitational attraction on the planet, we regard the corresponding attraction of the planet on the sun as negligible, and that the sun will be treated as being stationary. This approximation to the physical system can be interpreted in another way: even though both bodies are in motion about their centre of mass, the motion of the planet relative to the sun can be modelled using the simplification we have described. We also make a further assumption, that the motion of the planet is confined to a plane.

Let $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ denote rectangular coordinates centred at the sun, specifying at time $x$ the position of the planet. Also let $y _ { 3 } ( x )$ and $y _ { 4 } ( x )$ denote the components of velocity in the $y _ { 1 }$ and $y _ { 2 }$ directions, respectively. If $M$ denotes the mass of the sun, $\gamma$ the gravitational constant and $m$ the mass of the planet, then the attractive force on the planet will have magnitude

$$
\frac { \gamma M m } { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } .
$$

Resolving this force in the coordinate directions, we find that the components of acceleration of the planet, due to this attraction, are $- \gamma M y _ { 1 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 }$ and $- \gamma M y _ { 2 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 }$ , where the negative sign denotes the inward direction of the acceleration.

We can now write the equations of motion:

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = y _ { 4 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = - \frac { \gamma M y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } , } \\ { \displaystyle \frac { d y _ { 4 } } { d x } = - \frac { \gamma M y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } . } \end{array}
$$

By adjusting the scales of the variables, the factor $\gamma M$ can be removed from the formulation, and we arrive at the equations

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = y _ { 4 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = - \frac { y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } , } \\ { \displaystyle \frac { d y _ { 4 } } { d x } = - \frac { y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } . } \end{array}
$$

The solutions of this system are known to be conic sections, that is, ellipses, parabolas or hyperbolas, if we ignore the possibility that the trajectory is a straight line directed either towards or away from the sun. We investigate this further after we have shown that two ‘first integrals’, or invariants, of the solution exist.

Theorem 101A The quantities

$$
\begin{array} { l } { { H = \displaystyle \frac { 1 } { 2 } \left( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } \right) - ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 1 / 2 } , } } \\ { { A = y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 } } } \end{array}
$$

are constant.

Proof. We verify that the values of $d H / d x$ and $d A / d x$ are zero if $y$ satisfies (101a)–(101d). We have

$$
{ \begin{array} { r l } & { { \cfrac { d H } { d x } } = y _ { 3 } { \cfrac { d y _ { 3 } } { d x } } + y _ { 4 } { \cfrac { d y _ { 4 } } { d x } } + y _ { 1 } { \cfrac { d y _ { 1 } } { d x } } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 } + y _ { 2 } { \cfrac { d y _ { 2 } } { d x } } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 } } \\ & { \qquad = - { \cfrac { y _ { 1 } y _ { 3 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } - { \cfrac { y _ { 2 } y _ { 4 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + { \cfrac { y _ { 1 } y _ { 3 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + { \cfrac { y _ { 2 } y _ { 4 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } } \\ & { \qquad = 0 } \end{array} }
$$

and

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle { \frac { d A } { d x } } = y _ { 1 } \displaystyle { \frac { d y _ { 4 } } { d x } } + \frac { d y _ { 1 } } { d x } y _ { 4 } - y _ { 2 } \displaystyle { \frac { d y _ { 3 } } { d x } } - \frac { d y _ { 2 } } { d x } y _ { 3 } } } \\ { { } } & { { } } & { { = - \displaystyle { \frac { y _ { 1 } y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + y _ { 3 } y _ { 4 } + \frac { y _ { 2 } y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - y _ { 4 } y _ { 3 } } } \\ { { } } & { { } } & { { = 0 . } } \end{array}
$$

The quantities $H$ and $A$ are the ‘Hamiltonian’ and ‘angular momentum’, respectively. Note that $H = T + V$ , where $T = \textstyle { \frac { 1 } { 2 } } \left( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } \right)$ is the kinetic energy and $V = - ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 1 / 2 }$ is the potential energy.

A further property of this problem is its invariance under changes of scale of the variables:

$$
\begin{array} { r l } & { y _ { 1 } = \alpha ^ { - 2 } \overline { { y } } _ { 1 } , } \\ & { y _ { 2 } = \alpha ^ { - 2 } \overline { { y } } _ { 2 } , } \\ & { y _ { 3 } = \alpha \overline { { y } } _ { 3 } , } \\ & { y _ { 4 } = \alpha \overline { { y } } _ { 4 } , } \\ & { x = \alpha ^ { - 3 } \overline { { x } } . } \end{array}
$$

The Hamiltonian and angular momentum get scaled to

$$
\begin{array} { l l l } { { \overline { { { H } } } = \displaystyle \frac { 1 } { 2 } \left( \overline { { { y } } } _ { 3 } ^ { 2 } + \overline { { { y } } } _ { 4 } ^ { 2 } \right) - ( \overline { { { y } } } _ { 1 } ^ { 2 } + \overline { { { y } } } _ { 2 } ^ { 2 } ) ^ { - 1 / 2 } = \alpha ^ { - 2 } H , } } \\ { { \overline { { { A } } } = \overline { { { y } } } _ { 1 } \overline { { { y } } } _ { 4 } - \overline { { { y } } } _ { 2 } \overline { { { y } } } _ { 3 } } } & { { = \alpha A . } } \end{array}
$$

A second type of transformation is based on a two-dimensional orthogonal transformation (that is, a rotation or a reflection or a composition of these) $Q$ , where $Q ^ { - 1 } = Q ^ { \ i } .$ The time variable $x$ is invariant, and the position and velocity variables get transformed to

$$
\left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \end{array} \right] = \left[ \begin{array} { l l } { Q } & { 0 } \\ { 0 } & { Q } \end{array} \right] \left[ \begin{array} { l } { \overline { { y } } _ { 1 } } \\ { \overline { { y } } _ { 2 } } \\ { \overline { { y } } _ { 3 } } \\ { \overline { { y } } _ { 4 } } \end{array} \right] .
$$

It is easy to see that $A = 0$ implies that the trajectory lies entirely in a subspace defined by $\cos ( \theta ) y _ { 1 } = \sin ( \theta ) y _ { 2 }$ , $\cos ( \theta ) y _ { 3 } = \sin ( \theta ) y _ { 4 }$ for some fixed angle $\theta$ . We move on from this simple case and assume that $A \neq 0$ . The sign of $H$ is of crucial importance: if $H \geq 0$ then it is possible to obtain arbitrarily high values of $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 }$ without $y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 }$ vanishing. We exclude this case for the present discussion and assume that $H \ < \ 0$ . Scale $H$ so that it has a value $- \frac { 1 } { 2 }$ and at the same time $A$ takes on a positive value. This value cannot exceed $1$ because we can easily verify an identity involving the derivative of $r = \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } }$ . This identity is

$$
\left( r \frac { d r } { d x } \right) ^ { 2 } = 2 H r ^ { 2 } + 2 r - A ^ { 2 } = - r ^ { 2 } + 2 r - A ^ { 2 } .
$$

Since the left-hand side cannot be negative, the quadratic function in $r$ on the right-hand side must have real roots. This implies that $A \ \leq \ 1$ . Write $A = { \sqrt { 1 - e ^ { 2 } } }$ , for $e \geq 0$ , where we see that $e$ is the eccentricity of an ellipse on which the orbit lies. The minimum and maximum values of $r$ are found to be $1 - e$ and $1 + e$ , respectively. Rotate axes so that when $r = 1 - e$ , which we take as the starting point of time, $y _ { 1 } = 1 - e$ and $y _ { 2 } = 0$ . At this point we find that $y _ { 3 } = 0$ and $y _ { 4 } = \sqrt { ( 1 + e ) / ( 1 - e ) }$ .

Change to polar coordinates by writing $y _ { 1 } = r \cos ( \theta )$ , $y _ { 2 } = r \sin ( \theta )$ . It is found that

$$
\begin{array} { l } { { y _ { 3 } = \displaystyle \frac { d y _ { 1 } } { d x } = \displaystyle \frac { d r } { d x } \cos ( \theta ) - r \displaystyle \frac { d \theta } { d x } \sin ( \theta ) , } } \\ { { y _ { 4 } = \displaystyle \frac { d y _ { 2 } } { d x } = \displaystyle \frac { d r } { d x } \sin ( \theta ) + r \displaystyle \frac { d \theta } { d x } \cos ( \theta ) , } } \end{array}
$$

so that, because $y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 } = { \sqrt { 1 - e ^ { 2 } } }$ , we find that

$$
r ^ { 2 } { \frac { d \theta } { d x } } = { \sqrt { 1 - e ^ { 2 } } } .
$$

From (101e) and (101f) we find a differential equation for the path traced out by the orbit

$$
\left( \frac { d r } { d \theta } \right) ^ { 2 } = \frac { 1 } { 1 - e ^ { 2 } } r ^ { 2 } \left( e ^ { 2 } - ( 1 - r ) ^ { 2 } \right) ,
$$

and we can verify that this is satisfied by

$$
\frac { 1 - e ^ { 2 } } { r } = 1 + e \cos ( \theta ) .
$$

If we change back to Cartesian coordinates, we find that all points on the trajectory lie on the ellipse

$$
( y _ { 1 } + e ) ^ { 2 } + \frac { y _ { 2 } ^ { 2 } } { 1 - e ^ { 2 } } = 1 ,
$$

with centre $( - e , 0 )$ , eccentricity $e$ , and major and minor axis lengths 1 and $\sqrt { 1 - e ^ { 2 } }$ respectively.

As we have seen, a great deal is known about this problem. However, much less is known about the motion of a many-body gravitational system.

One of the aims of modern numerical analysis is to understand the behaviour of various geometrical properties. In some cases it is possible to preserve the value of quantities that are invariant in the exact solution. In other situations, such as problems where the Hamiltonian is theoretically conserved, it may be preferable to conserve other properties, such as what is known as ‘symplectic behaviour’.

We consider further gravitational problems in Subsection 120.

# 102 A problem arising from the method of lines

The second initial value problem we consider is based on an approximation to a partial differential equation. Consider the parabolic system

$$
\frac { \partial u } { \partial t } = \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } , \qquad ( x , t ) \in [ 0 , 1 ] \times [ 0 , \infty ) ,
$$

where we have used $t$ to represent time, $x$ to represent distance and $\boldsymbol { u } ( \boldsymbol { x } , t )$ t o represent some quantity, such as temperature, which diffuses with time. For this problem it is necessary to impose conditions on the boundaries $x = 0$ and $x = 1$ as well as at the initial time $t = 0$ . We may interpret the solution as the distribution of the temperature at points in a conducting rod, given that the temperature is specified at the ends of the rod. In this case the boundary conditions would be of the form $u ( 0 , t ) = \alpha ( t )$ and $u ( 1 , t ) = \beta ( t )$ . Equation (102a) is known as the heat or diffusion equation, and the conditions given at $x = 0$ and $x = 1$ are known as Dirichlet boundary values. This is in contrast to Neumann conditions, in which the values of $\partial u / \partial x$ are given at the ends of the $x$ interval.

To convert this problem into an ordinary differential equation system, which denote the values of mimics the behaviour of the parabolic equation, let $\begin{array} { r } { u ( \frac { 1 } { N + 1 } , t ) , u ( \frac { 2 } { N + 1 } , t ) , \dots , u ( \frac { N } { N + 1 } , t ) } \end{array}$ $y _ { 1 } ( t ) , y _ { 2 } ( t ) , \dotsc , y _ { N } ( t )$ , respectively. That is, ,

$$
y _ { j } ( t ) = u \left( { \frac { j } { N + 1 } } , t \right) , \qquad j = 0 , 1 , 2 , \ldots , N + 1 ,
$$

where we have included $y _ { 0 } ( t ) = u ( 0 , t )$ , $y _ { N + 1 } ( t ) = u ( 1 , t )$ for convenience.

For $j = 1 , 2 , \dots , N$ , $\partial ^ { 2 } u / \partial x ^ { 2 }$ , evaluated at $x = j / ( N + 1 )$ , is approximately equal to $( N + 1 ) ^ { 2 } ( y _ { j - 1 } - 2 y _ { j } + y _ { j + 1 } )$ . Hence, the vector of derivatives of $y _ { 1 } , y _ { 2 } , \dotsc , y _ { N }$ is given by

$$
\begin{array} { l } { \frac { d y _ { 1 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( \alpha ( t ) - 2 y _ { 1 } ( t ) + y _ { 2 } ( t ) \big ) , } \\ { \frac { d y _ { 2 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { 1 } ( t ) - 2 y _ { 2 } ( t ) + y _ { 3 } ( t ) \big ) , } \\ { \frac { d y _ { 3 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { 2 } ( t ) - 2 y _ { 3 } ( t ) + y _ { 4 } ( t ) \big ) , } \\ { \vdots } \\ { \frac { d y _ { N - 1 } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { N - 2 } ( t ) - 2 y _ { N - 1 } ( t ) + y _ { N } ( t ) \big ) , } \\ { \frac { d y _ { N } ( t ) } { d t } = ( N + 1 ) ^ { 2 } \big ( y _ { N - 1 } ( t ) - 2 y _ { N } ( t ) + \beta ( t ) \big ) . } \end{array}
$$

This system can be written in vector–matrix form as

$$
y ^ { \prime } ( t ) = A y ( t ) + v ( t ) ,
$$

where

$$
= ( N + 1 ) ^ { 2 } { \left[ \begin{array} { l l l l l l l l } { - 2 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 1 } & { - 2 } & { 1 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - 2 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } & { - 2 } \end{array} \right] } , \quad v = ( N + 1 ) ^ { 2 } { \left[ \begin{array} { l } { \alpha ( t ) } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 0 } \\ { \beta ( t ) } \end{array} \right] } .
$$

The original problem is ‘dissipative’ in the sense that, if $u$ and $\boldsymbol { v }$ are each solutions to the diffusion equation, which have identical boundary values but different initial values, then

$$
W ( t ) = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \big ( u ( x , t ) - v ( x , t ) \big ) ^ { 2 } d x
$$

is non-increasing as $t$ increases. We can verify this by differentiating with respect to $t$ and by showing, using integration by parts, that the result found

cannot be positive. We have

$$
\begin{array} { r l } & { \frac { d W } { d t } = \displaystyle \int _ { 0 } ^ { 1 } \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial u ( x , t ) } { \partial t } - \frac { \partial v ( x , t ) } { \partial t } \right) d x } \\ & { \quad \quad = \displaystyle \int _ { 0 } ^ { 1 } \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial ^ { 2 } u ( x , t ) } { \partial x ^ { 2 } } - \frac { \partial ^ { 2 } v ( x , t ) } { \partial x ^ { 2 } } \right) d x } \\ & { \quad \quad = \displaystyle \left[ \left( u ( x , t ) - v ( x , t ) \right) \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) \right] _ { 0 } ^ { 1 } } \\ & { \qquad \quad \quad \quad - \displaystyle \int _ { 0 } ^ { 1 } \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) ^ { 2 } d x } \\ & { \quad \quad \quad = - \displaystyle \int _ { 0 } ^ { 1 } \left( \frac { \partial u ( x , t ) } { \partial x } - \frac { \partial v ( x , t ) } { \partial x } \right) ^ { 2 } d x } \\ & { \quad \quad \quad \le 0 . } \end{array}
$$

Even though the approximation of (102a) by (102b) is not exact, it is an advantage of the discretization we have used, that the qualitative property is still present. Let $y$ and $z$ be two solutions to the ordinary differential equation system. Consider the nature of

$$
\widehat W ( t ) = \frac { 1 } { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ^ { 2 } .
$$

We have

$$
\begin{array} { l } { \displaystyle \frac { d \widehat { W } } { d t } = \sum _ { i = 1 } ^ { N } ( y _ { j } - z _ { j } ) \left( \frac { d y _ { j } } { d t } - \frac { d z _ { j } } { d t } \right) } \\ { \displaystyle \quad = ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ( y _ { j - 1 } - 2 y _ { j } + y _ { j + 1 } - z _ { j - 1 } + 2 z _ { j } - z _ { j + 1 } ) } \\ { \displaystyle \quad = 2 ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N - 1 } ( y _ { j } - z _ { j } ) ( y _ { j + 1 } - z _ { j + 1 } ) - 2 ( N + 1 ) ^ { 2 } \sum _ { j = 1 } ^ { N } ( y _ { j } - z _ { j } ) ^ { 2 } } \\ { \displaystyle \quad = - ( N + 1 ) ^ { 2 } \sum _ { j = 0 } ^ { N } ( y _ { j + 1 } - y _ { j } - z _ { j + 1 } + z _ { j } ) ^ { 2 } } \\ { \displaystyle \quad \leq 0 . } \end{array}
$$

Another aspect of the discretization that might be explored is the spectrum of the matrix $A$ , in comparison with the spectrum of the linear operator $u \mapsto { \frac { d ^ { 2 } u } { d x ^ { 2 } } }$ on the space of $C ^ { 2 }$ functions on $[ 0 , 1 ]$ for which $u ( 0 ) = u ( 1 ) = 0$ . The eigenfunctions for the continuous problem are of the form $\sin ( k \pi x )$ , for $k = 1 , 2 , 3 , \ldots$ and the corresponding eigenvalues are $- k ^ { 2 } \pi ^ { 2 }$ . For the discrete problem, we need to find the solutions to the problem

$$
( A - \lambda I ) \left[ \begin{array} { c } { v _ { 1 } } \\ { v _ { 2 } } \\ { \vdots } \\ { v _ { N } } \end{array} \right] = 0 ,
$$

where $v _ { 1 }$ , $v _ { 2 }$ , $\cdot \cdot \cdot$ , $v _ { N }$ are not all zero. Introducing also $v _ { 0 } = v _ { N + 1 } = 0$ , we find that it is possible to write (102c) in the form

$$
v _ { j - 1 } - q v _ { j } + v _ { j + 1 } = 0 , \qquad j = 1 , 2 , \ldots , N ,
$$

where $q = 2 + \lambda / ( N + 1 ) ^ { 2 }$ . The difference equation (102d) has solution of the form $v _ { i } = C ( \mu ^ { i } - \mu ^ { - i } )$ , where $\mu + \mu ^ { - 1 } = q$ , unless $q = \pm 2$ (which is easily seen to be impossible). Because $v _ { N + 1 } = 0$ , it follows that $\lambda ^ { 2 N + 2 } = 2$ . Because $\mu \neq \pm 1$ , it follows that

$$
\mu = \exp \left( \frac { k \pi i } { N + 1 } \right) , \qquad k = 1 , 2 , \ldots , N ,
$$

with $i = \sqrt { - 1 }$ . Hence,

$$
\lambda = - 2 ( N + 1 ) ^ { 2 } \left( 1 - \cos \left( \frac { k \pi } { N + 1 } \right) \right) = - 4 ( N + 1 ) ^ { 2 } \sin ^ { 2 } \left( \frac { k \pi } { 2 N + 2 } \right) .
$$

For $N$ much larger than $k$ , we can use the approximation $\sin ( \xi ) \approx \xi$ , for small $\xi$ , to give eigenvalue number $k$ as $\lambda _ { k } \approx - k ^ { 2 } \pi ^ { 2 }$ . On the other hand, for $k$ small, the eigenvalue number $N + 1 - k$ is $\lambda _ { N + 1 - k } \approx - 4 ( N + 1 ) ^ { 2 } + k ^ { 2 } \pi ^ { 2 }$ .

# 103 The simple pendulum

# Formulation as a differential-algebraic equation

Consider a small mass $m$ attached to a light inelastic string of length $\it l$ , with the other end attached to the origin of coordinates, which can swing back and forth in a vertical plane. Let $X$ , measured in a rightwards direction, and $Y$ , measured in a downward direction, be the coordinates. Because the string is inelastic, the tension $T$ in the string always matches other forces resolved in the direction of the string so as to guarantee that the length does not change.

The way these forces act on the mass is shown in Figure 103(i). Also shown is the angle $\theta$ defined by $X = l \sin ( \theta )$ , $Y = l \cos ( \theta )$ .

We denote by $U$ and $V$ , respectively, the velocity components in the $X$ and

![](images/752c49403addb0e147f4c05423a006586ad916b4a0a2e9ab309e953a59e1b11a.jpg)  
Simple pendulum

$Y$ directions. The motion of the pendulum is governed by the equations

$$
\begin{array} { r l r } & { \frac { d X } { d x } = U , } & \\ & { \frac { d Y } { d x } = V , } & \\ & { \displaystyle { m \frac { d U } { d x } = - \frac { T X } { l } , } } & \\ & { \displaystyle { m \frac { d V } { d x } = - \frac { T Y } { l } + m g , } } & \\ & { \displaystyle { X ^ { 2 } + Y ^ { 2 } = l ^ { 2 } , } } & \end{array}
$$

where, in addition to four differential equations (103a)–(103d), the constraint (103e) expresses the constancy of the length of the string. The tension $T$ acts as a control variable, forcing this constraint to remain satisfied. By rescaling variables in a suitable way, the ‘differential-algebraic’ equation system (103a)– (103e) can be rewritten with the constants $m$ , $g$ and $\it l$ replaced by $^ { 1 }$ in each case. In the rescaled formulation write $y _ { 1 } = X$ , $y _ { 2 } = Y$ , $y _ { 3 } = U$ , $y _ { 4 } = V$ and $y _ { 5 } = T$ , and we arrive at the system

$$
\begin{array} { l } { \displaystyle { \frac { d y _ { 1 } } { d x } = y _ { 3 } , } } \\ { \displaystyle { \frac { d y _ { 2 } } { d x } = y _ { 4 } , } } \\ { \displaystyle { \frac { d y _ { 3 } } { d x } = - y _ { 1 } y _ { 5 } , } } \\ { \displaystyle { \frac { d y _ { 4 } } { d x } = - y _ { 2 } y _ { 5 } + 1 } . } \\ { \displaystyle { \frac { 2 } { d } + y _ { 2 } ^ { 2 } = 1 } . } \end{array}
$$

It will be convenient to choose initial values defined in terms of $\theta = \Theta$ , with

the velocity equal to zero. That is,

$$
y _ { 1 } ( 0 ) = \sin ( \Theta ) , \quad y _ { 2 } ( 0 ) = \cos ( \Theta ) , \quad y _ { 3 } ( 0 ) = y _ { 4 } ( 0 ) = 0 , \quad y _ { 5 } ( 0 ) = \cos ( \Theta ) .
$$

The five variables are governed by four differential equations (103f)–(103i), together with the single algebraic constraint (103j). We will say more about this below, but first we consider the classical way of simplifying the problem.

# Formulation as a single second order equation

Make the substitutions $\begin{array} { r l r } { y _ { 1 } } & { { } = } & { \sin ( \theta ) } \end{array}$ , $\begin{array} { r l r } { y _ { 2 } } & { { } = } & { \cos ( \theta ) } \end{array}$ . Because (103j) is automatically satisfied, the value of $y _ { 5 }$ loses its interest and we eliminate this by taking a linear combination of (103h) and (103i). This gives the equation system

$$
\begin{array} { c } { { \displaystyle \cos ( \theta ) \frac { d \theta } { d x } = y _ { 3 } , } } \\ { { \displaystyle - \sin ( \theta ) \frac { d \theta } { d x } = y _ { 4 } , } } \\ { { \displaystyle - \cos ( \theta ) \frac { d y _ { 3 } } { d x } + \sin ( \theta ) \frac { d y _ { 4 } } { d x } = \sin ( \theta ) . } } \end{array}
$$

Differentiate (103k) and (103l) and substitute into (103m) and we obtain the well-known single-equation formulation of the simple pendulum:

$$
{ \frac { d ^ { 2 } \theta } { d x ^ { 2 } } } + \sin ( \theta ) = 0 ,
$$

with initial values

$$
\theta ( 0 ) = \Theta , \qquad \theta ^ { \prime } ( 0 ) = 0 .
$$

It can be shown that the period of the pendulum is given by

$$
T = 4 \int _ { 0 } ^ { \pi / 2 } \frac { d \phi } { \sqrt { 1 - \sin ^ { 2 } \phi \sin ^ { 2 } \frac { \Theta } { 2 } } }
$$

and some values are given in Table 103(I).

The value for $0 ^ { \circ }$ can be interpreted as the period for small amplitudes. The fact that $T$ increases slowly as $\Theta$ increases is the characteristic property of a simple pendulum which makes it of practical value in measuring time.

Formulation as a Hamiltonian problem

In the formulation (103n), write the $H$ as the ‘Hamiltonian’

$$
\begin{array} { r } { H ( p , q ) = \frac { 1 } { 2 } p ^ { 2 } - \cos ( q ) , } \end{array}
$$

Period of simple pendulum for various amplitudes   

<table><tr><td rowspan=1 colspan=2>Θ          T</td></tr><tr><td rowspan=1 colspan=2>0°  6.2831853072</td></tr><tr><td rowspan=1 colspan=2>3°  6.2842620831</td></tr><tr><td rowspan=1 colspan=2>6° 6.2874944421</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>6.2928884880</td></tr><tr><td rowspan=1 colspan=1>12°</td><td rowspan=1 colspan=1>6.3004544311</td></tr><tr><td rowspan=1 colspan=1>15°</td><td rowspan=1 colspan=1>6.3102066431</td></tr><tr><td rowspan=1 colspan=1>18°</td><td rowspan=1 colspan=1>6.3221637356</td></tr><tr><td rowspan=1 colspan=1>21°</td><td rowspan=1 colspan=1>6.3363486630</td></tr><tr><td rowspan=1 colspan=1>24°</td><td rowspan=1 colspan=1>6.3527888501</td></tr><tr><td rowspan=1 colspan=1>27°</td><td rowspan=1 colspan=1>6.3715163462</td></tr><tr><td rowspan=1 colspan=1>30°</td><td rowspan=1 colspan=1>6.3925680085</td></tr></table>

where $q \ = \ \theta$ and $p \ = \ d \theta / d x$ . The second order equation (103n) is now equivalent to the first order system

$$
\left[ \begin{array} { c } { { p ^ { \prime } } } \\ { { q ^ { \prime } } } \end{array} \right] = \left[ \begin{array} { c c } { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c } { { \frac { \partial H } { \partial p } } } \\ { { \frac { \partial H } { \partial q } } } \end{array} \right] .
$$

Differential index and index reduction

Carry out three steps, of which the first is to differentiate (103j) and substitute from (103f) and (103g) to give the result

$$
y _ { 1 } y _ { 3 } + y _ { 2 } y _ { 4 } = 0 .
$$

The second step is to differentiate (103o) and to make various substitutions from (103f)–(103i) to arrive at the equation

$$
y _ { 2 } + y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } - y _ { 5 } = 0 .
$$

The third and final step is to differentiate (103p) and make various substitutions to arrive at the result

$$
\frac { d y _ { 5 } } { d x } = \frac { y _ { 2 } } { d x } + 2 y _ { 3 } \frac { d y 3 } { d x } + 2 y _ { 4 } \frac { d y _ { 4 } } { d x } = y _ { 4 } + 2 y _ { 3 } ( - y _ { 1 } y _ { 5 } ) + 2 y _ { 4 } ( - y _ { 2 } y _ { 5 } + 1 ) ,
$$

which simplifies to

$$
{ \frac { d y _ { 5 } } { d x } } = 3 y _ { 4 } .
$$

Given that consistent initial values are used, it seems that the equations (103f)–(103i) together with any of (103j), (103o), (103p) or (103q) give identical solutions.

Which of the possible formulations should be used? From the point of view of physical modelling, it seems to be essential to require that the length constraint (103j) should hold exactly. On the other hand, when it comes to numerical approximations to solutions, it is found that the use of this constraint in the problem description creates serious computational difficulties. It also seems desirable from a modelling point of view to insist that (103o) should hold exactly, since this simply states that the direction of motion is tangential to the arc on which it is constrained to lie.

# 104 A chemical kinetics problem

We next consider a model of a chemical process consisting of three species, which we denote by $A$ , $B$ and $C$ . The three reactions are

$$
\begin{array} { c } { A  B , } \\ { B + C  A + C , } \\ { B + B  C . } \end{array}
$$

Let $y _ { 1 }$ , $y _ { 2 }$ and $y _ { 3 }$ denote the concentrations of $A$ , $B$ and $C$ , respectively. We assume these are scaled so that the total of the three concentrations is $^ { 1 }$ , and that each of three constituent reactions will add to the concentration of any of the species exactly at the expense of corresponding amounts of the reactants. The reaction rate of (104a) will be denoted by $k _ { 1 }$ . This means that the rate at which $y _ { 1 }$ decreases, and at which $y _ { 2 }$ increases, because of this reaction, will be equal to $k _ { 1 } y _ { 1 }$ . In the second reaction (104b), $C$ acts as a catalyst in the production of $A$ from $B$ and the reaction rate will be written as $k _ { 2 }$ , meaning that the increase of $y _ { 1 }$ , and the decrease of $y _ { 3 }$ , in this reaction will have a rate equal to $k _ { 2 } y _ { 2 } y _ { 3 }$ . Finally, the production of $C$ from $B$ will have a rate constant equal to $k _ { 3 }$ , meaning that the rate at which this reaction takes place will be $k _ { 3 } y _ { 2 } ^ { 2 }$ . Putting all these elements of the process together, we find the system of differential equations for the variation with time of the three concentrations to be

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = - k _ { 1 } y _ { 1 } + k _ { 2 } y _ { 2 } y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = k _ { 1 } y _ { 1 } - k _ { 2 } y _ { 2 } y _ { 3 } - k _ { 3 } y _ { 2 } ^ { 2 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } . } \end{array}
$$

If the three reaction rates are moderately small numbers, and not greatly different in magnitude, then this is a straightforward problem. However, vastly different magnitudes amongst $k _ { 1 }$ , $k _ { 2 }$ and $k _ { 3 }$ can make this problem complicated to understand as a chemical model. Also, as we shall see, the problem then becomes difficult to solve numerically. This problem was popularized by Robertson (1966), who used the reaction rates

$$
k _ { 1 } = 0 . 0 4 , \qquad k _ { 2 } = 1 0 ^ { 4 } , \qquad k _ { 3 } = 3 \times 1 0 ^ { 7 } .
$$

Before looking at the problem further we note that, even though it is written as a three-dimensional system, it would be a simple matter to rewrite it in two dimensions, because $y _ { 1 } + y _ { 2 } + y _ { 3 }$ is an invariant and is usually set to a value of 1, by an appropriate choice of the initial values. We always assume this value for $y _ { 1 } + y _ { 2 } + y _ { 3 }$ . Furthermore, if the initial value has non-negative values for each of the three components, then this situation is maintained for all positive times. To see why this is the case, write (104d), (104e) and (104f) in the forms

$$
\begin{array} { c } { \frac { d \left( \exp \left( k _ { 1 } x \right) y _ { 1 } \right) } { d x } = \exp ( k _ { 1 } x ) k _ { 2 } y _ { 2 } y _ { 3 } , } \\ { \frac { d \left( \exp \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x \right) y _ { 2 } \right) } { d x } = \exp \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x \right) F , } \\ { \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } , } \end{array}
$$

where

$$
F = k _ { 1 } y _ { 1 } + \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) y _ { 1 } y _ { 2 } + \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) - k _ { 2 } \right) y _ { 2 } y _ { 3 } + \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) - k _ { 3 } \right) y
$$

so that each of $\exp ( k _ { 1 } x ) y _ { 1 }$ , $\exp ( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x ) y _ { 2 }$ and $y _ { 3 }$ is non-decreasing.

An interesting feature of this problem is that a small perturbation that does not disturb the invariance of $y _ { 1 } + y _ { 2 } + y _ { 3 }$ is damped out rapidly. To see why this is the case, eliminate $y _ { 1 }$ so that the differential equation system in the remaining two components becomes

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 2 } } { d x } = k _ { 1 } ( 1 - y _ { 2 } - y _ { 3 } ) - k _ { 2 } y _ { 2 } y _ { 3 } - k _ { 3 } y _ { 2 } ^ { 2 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } . } \end{array}
$$

The Jacobian matrix, the matrix of partial derivatives, is given by

$$
J ( x ) = \left[ \begin{array} { c c } { - k _ { 1 } - k _ { 2 } y _ { 3 } - 2 k _ { 3 } y _ { 2 } } & { - k _ { 1 } - k _ { 2 } y _ { 2 } } \\ { 2 k _ { 3 } y _ { 2 } } & { 0 } \end{array} \right] ,
$$

and the characteristic polynomial is

$$
\lambda ^ { 2 } + ( k _ { 1 } + k _ { 2 } y _ { 3 } + 2 k _ { 3 } y _ { 2 } ) \lambda + 2 k _ { 3 } y _ { 2 } ( k _ { 1 } + k _ { 2 } y _ { 2 } ) .
$$

![](images/c2d5ba9e5d7f8de9498dae2edaaa7e3d1771347e634ad8169d8ae066d4bb5de6.jpg)  
Solution and most negative eigenvalue for the Robertson problem

An analysis of the discriminant of (104i) indicates that for $y _ { 2 } , y _ { 3 } \in ( 0 , 1 ]$ , both zeros are real and negative. Along the actual trajectory, one of the eigenvalues of $J ( x )$ , denoted by $\lambda$ , rapidly jumps to a very negative value, with the second eigenvalue retaining a small negative value. Consider a small perturbation $z$ to the solution, so that the solution becomes $y + z$ . Because the two components of $z$ are small we can approximate $f ( y + z )$ by $f ( y ) + ( \partial f / \partial y ) z$ . Hence, the perturbation itself satisfies the equation

$$
{ \left[ \begin{array} { l } { { \cfrac { d z _ { 2 } } { d x } } } \\ { { \cfrac { d z _ { 3 } } { d x } } } \end{array} \right] } = J ( x ) { \left[ \begin{array} { l } { z _ { 2 } } \\ { z _ { 3 } } \end{array} \right] }
$$

and the negative eigenvalues of $J ( x )$ guarantee the decay of the components of $z$ .

The solution to this problem, together with the value of $\lambda$ , is shown in Figure 104(i).

# 105 The Van der Pol equation and limit cycles

The simple pendulum, which we considered in Subsection 103, is a non-linear variant of the ‘harmonic oscillator’ problem $y ^ { \prime \prime } = - y$ . We now consider another non-linear generalization of this problem, by adding a term $\mu ( 1 - y ^ { 2 } ) y ^ { \prime }$ , where $\mu$ is a positive constant, to obtain the ‘Van der Pol equation’

$$
y ^ { \prime \prime } ( x ) = \mu ( 1 - y ( x ) ^ { 2 } ) y ^ { \prime } ( x ) - y ( x ) .
$$

This problem was originally introduced by Van der Pol (1926) in the study of electronic circuits. If $\mu$ is small and the initial values correspond to what would be oscillations of amplitude less than 1, if $\mu$ had in fact been zero, it might be expected that the values of $y ( x )$ would remain small for all time.

![](images/9a820c6fc1eaef1cbfd02b7f60788ec1fd057c1012e38c22156231684395b250.jpg)  
Van der Pol problem with $\mu = 1$

![](images/b1ba043a959e999472da09e63135e7a0477bbce6fcd75fa3e3737348af023087.jpg)  
Van der Pol problem with $\mu = 3$

However, the non-linear term has the effect of injecting more ‘energy’ into the system, as we see by calculating the rate of change of $E = { \textstyle { \frac { 1 } { 2 } } } y ^ { \prime } ( x ) ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } y ( x ) ^ { 2 }$ . This is found to be

$$
{ \frac { d } { d x } } \left( { \frac { 1 } { 2 } } y ^ { \prime } ( x ) ^ { 2 } + { \frac { 1 } { 2 } } y ( x ) ^ { 2 } \right) = \mu ( 1 - y ( x ) ^ { 2 } ) y ^ { \prime } ( x ) ^ { 2 } > 0 ,
$$

as long as $| y | < 1$

Similarly, if $| y |$ starts with a high value, then $E$ will decrease until $| y | = 1$ . It is possible to show that the path, traced out in the $( y , y ^ { \prime } )$ plane, loops round the origin in a clockwise direction forever, and that it converges to a ‘limit cycle’ $-$ a periodic orbit. In Figure 105(i), this is illustrated for $\mu = 1$ . The path traced out in the $( y , y ^ { \prime } )$ plane moves rapidly towards the limit cycle and is soon imperceptibly close to it. In Figure 105(ii), the case $\mu = 3$ is presented.

![](images/3f5f7d41743489e31437a4f24ad6d3fa6d191ba62a632e88f3f42996aa008430.jpg)  
Phase diagram for Lotka–Volterra solution with $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$ , together with seven alternative orbits

Of special interest in this problem, especially for large values of $\mu$ , is the fact that numerical methods attempting to solve this problem need to adjust their behaviour to take account of varying conditions, as the value of $1 - | y ( x ) | ^ { 2 }$ changes. The sharp change of direction of the path traced out near $( y , y ^ { \prime } ) ~ = ~ ( \pm 2 , 0 )$ for the $\mu ~ = ~ 3$ case, a phenomenon which becomes more pronounced as $\mu$ is further increased, is part of the numerical difficulty associated with this problem.

# 106 The Lotka–Volterra problem and periodic orbits

In the modelling of the two-species ‘predator–prey’ problem, differential equation systems of the following type arise:

$$
\begin{array} { r } { u ^ { \prime } = u ( 2 - v ) , } \\ { v ^ { \prime } = v ( u - 1 ) , } \end{array}
$$

where the factors $2 - v$ and $u - 1$ can be generalized in various ways. This model was proposed independently by Lotka (1925) and Volterra (1926). The two variables represent the time-dependent populations, of which $\boldsymbol { v }$ is the population of predators which feed on prey whose population is denoted by $u$ . It is assumed that $u$ would have been able to grow exponentially without limit, if the predator had not been present, and that the factor $2 - v$ represents the modification to its growth rate because of harvesting by the predator. The predator in turn, in the absence of prey, would die out exponentially, and requires at least a prey population of $u = 1$ to feed upon to be able to grow. Of the two stationary solutions, $( u , v ) = ( 0 , 0 )$ and $( u , v ) = ( 1 , 2 )$ , the second is more interesting because small perturbations from this point will lead to periodic orbits around the stationary point. By dividing (106a) by (106b), we obtain a differential equation for the path traced out by $( u , v )$ . The solution is that $I ( u , v )$ is constant, where

Approximations to the period $T$ , given by (106d) for $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$   

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>Approximate integral</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>4.62974838287860</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>4.61430252126987</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>4.61487057379480</td></tr><tr><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>4.61487051945097</td></tr><tr><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>4.61487051945103</td></tr><tr><td rowspan=1 colspan=1>320</td><td rowspan=1 colspan=1>4.61487051945103</td></tr></table>

$$
I ( u , v ) = \log ( u ) + 2 \log ( v ) - u - v .
$$

It is interesting to try to calculate values of the period $T$ , for a given starting point $( u _ { 0 } , v _ { 0 } )$ . To calculate $T$ , change to polar coordinates centred at the stationary point

$$
u = 1 + r \cos ( \theta ) , \qquad v = 2 + r \sin ( \theta )
$$

and calculate the integral $\int _ { 0 } ^ { 2 \pi } \phi ( \theta ) d \theta$ , where

$$
\phi ( \theta ) = \frac { 1 } { v \cos ^ { 2 } ( \theta ) + u \sin ^ { 2 } ( \theta ) } .
$$

Starting values $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$ lead to the orbit featured in Figure $1 0 6 ( \mathrm { i } )$ . Orbits with various other starting values are also shown. The period, based on the integral of (106c), has been calculated with a varying number $n$ of equally spaced values of $\theta \in [ 0 , 2 \pi ]$ , using the trapezoidal rule. It is known that for certain smooth functions, the error of this type of calculation will behave, not like a power of $n ^ { - 1 }$ , but like $\exp ( - \alpha n )$ , for some problem-specific parameter $\alpha$ . This super-convergence is evidently realized for the present problem, where the observed approximations

$$
T = \int _ { 0 } ^ { 2 \pi } \phi ( \theta ) d \theta \approx { \frac { 2 \pi } { n } } \sum _ { k = 0 } ^ { n - 1 } \phi \left( { \frac { 2 \pi k } { n } } \right)
$$

are shown in Table 106(I) for $n = 1 0 , 2 0 , 4 0 , \ldots , 3 2 0$ . Evidently, to full machine accuracy, the approximations have converged to T = 4.61487051945103. An

α Computation of orbit and period for the Lotka–Volterra problem   

<table><tr><td>theta = linspace(O,2*pi,n+1);</td></tr><tr><td>co = cos(theta);</td></tr><tr><td>si = sin(theta);</td></tr><tr><td>C = u0*v0 2*exp(-u0-v0);</td></tr><tr><td>r = ones(size(theta));</td></tr><tr><td>u = 1+r.*co;</td></tr><tr><td>v = 2+r.*si;</td></tr><tr><td>carryon=1;</td></tr><tr><td>while carryon</td></tr><tr><td>f = u.*v. 2-C*exp(u+v);</td></tr><tr><td>df = -v.*r.*(v.*co. 2+u.*si. 2);</td></tr><tr><td>dr = f./df;</td></tr><tr><td>r = r-dr;</td></tr><tr><td>u = 1+r.*co;</td></tr><tr><td>V = 2+r.*si; carryon = norm(dr,inf）&gt; O.0ooooo001;</td></tr><tr><td>end</td></tr><tr><td>phi = 1./(v.*co.2+u.*si.2);</td></tr><tr><td></td></tr><tr><td>period = (2*pi/n)*sum(phi(1:n));</td></tr></table>

explanation of the phenomenon of rapid convergence of the trapezoidal rule for periodic functions can be found in Davis and Rabinowitz (1984), and in papers referenced in that book.

In Algorithm $1 0 6 \alpha$ , MATLAB statements are presented to carry out the computations that were used to generate Figure 106(i) and Table 106(I). To compute the value of $r$ for each $\theta$ , the equation $f ( r ) = 0$ is solved, where

$$
f ( r ) = ( \exp ( I ( u , v ) ) - C ) \exp ( u + v ) = u v ^ { 2 } - C \exp ( u + v ) ,
$$

with $C = u _ { 0 } v _ { 0 } ^ { 2 } \exp ( - u _ { 0 } - v _ { 0 } )$ . Note that the statement $\boldsymbol { \mathrm { ~ u ~ . ~ v ~ } }$ . $2 \mathrm { - C * e x p \left( u + v \right) }$ evaluates a vector with element number $i$ equal to $u _ { i } v _ { i } ^ { 2 } - C \exp ( u _ { i } + v _ { i } )$ , and that linspace(0,2\*pi,n+1) generates a vector with $n + 1$ components, equally spaced in $[ 0 , 2 \pi ]$ .

# 107 The Euler equations of rigid body rotation

For a rigid body on which no moments are acting, the three components of angular velocity, in terms of the principal directions of inertia fixed in the

body, satisfy the Euler equations:

$$
\begin{array} { r } { I _ { 1 } \cfrac { d w _ { 1 } } { d t } = ( I _ { 2 } - I _ { 3 } ) w _ { 2 } w _ { 3 } , } \\ { I _ { 2 } \cfrac { d w _ { 2 } } { d t } = ( I _ { 3 } - I _ { 1 } ) w _ { 3 } w _ { 1 } , } \\ { I _ { 3 } \cfrac { d w _ { 3 } } { d t } = ( I _ { 1 } - I _ { 2 } ) w _ { 1 } w _ { 2 } , } \end{array}
$$

where the ‘principal moments of inertia’ $I _ { 1 }$ , $I _ { 2 }$ and $I _ { 3 }$ are positive. Denote the kinetic energy by $\scriptstyle { \frac { 1 } { 2 } } E$ and the squared norm of the angular momentum by $F$ . That is,

$$
\begin{array} { r } { E = I _ { 1 } w _ { 1 } ^ { 2 } + I _ { 2 } w _ { 2 } ^ { 2 } + I _ { 3 } w _ { 3 } ^ { 2 } , } \\ { F = I _ { 1 } ^ { 2 } w _ { 1 } ^ { 2 } + I _ { 2 } ^ { 2 } w _ { 2 } ^ { 2 } + I _ { 3 } ^ { 2 } w _ { 3 } ^ { 2 } . } \end{array}
$$

Differentiate these expressions and substitute in $d w _ { i } / d t$ , $i = 1 , 2 , 3$ , to obtain a zero result in each case. Hence, $E$ and $F ^ { \dagger }$ are invariants of the solution to (107a). This observation provides useful tests on numerical methods for this problem because there is in general no reason why these invariants should be maintained in a numerical approximation.

# Exercises 10

10.1 You are given the initial value problem

$$
u ^ { \prime \prime \prime } ( x ) - 3 u ^ { \prime \prime } ( x ) + 2 u ( x ) u ^ { \prime } ( x ) = 0 , \quad u ( 1 ) = 2 , u ^ { \prime } ( 1 ) = - 1 , u ^ { \prime \prime } ( 1 ) = 4 .
$$

Show how to reformulate this problem in the form

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ .

10.2 You are given the non-autonomous initial value problem

$$
\begin{array} { l l } { { u ^ { \prime } = x u + x ^ { 2 } v , } } & { { u ( 0 ) = 3 , } } \\ { { v ^ { \prime } = u - v + 2 x w , } } & { { v ( 0 ) = 2 , } } \\ { { w ^ { \prime } = u + \displaystyle \frac { v } { 1 + x } , } } & { { w ( 0 ) = 5 . } } \end{array}
$$

Show how to write this as an autonomous problem.

10.3 The matrix

$$
A = ( N - 1 ) ^ { 2 } \left[ \begin{array} { c c c c c c c } { - 1 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 1 } & { - 2 } & { 1 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - 2 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } & { - 1 } \end{array} \right]
$$

arises in the numerical solution of the heat equation, but with Neumann boundary conditions. Find the eigenvalues of $A$ .

10.4 Calculate the period of an orbit of the Lotka–Volterra problem which passes through the point $( 3 , 2 )$ .

# 11 Differential Equation Theory

110 Existence and uniqueness of solutions

A fundamental question that arises in scientific modelling is whether a given differential equation, together with initial conditions, can be reliably used to predict the behaviour of the trajectory at later times. We loosely use the expression ‘well-posed’ to describe a problem that is acceptable from this point of view. The three attributes of an initial value problem that have to be taken into account are whether there actually exists a solution, whether the solution, if it exists, is unique, and how sensitive the solution is to small perturbations to the initial information. Even though there are many alternative criteria for answering these questions in a satisfactory manner, we focus here on the existence of a Lipschitz condition. This is especially convenient because the same type of condition can be used to study the behaviour of numerical approximations.

Definition 110A The function $f ~ : ~ [ a , b ] \times \mathbb { R } ^ { N } ~ \longrightarrow ~ \mathbb { R } ^ { N }$ is said to satisfy a ‘Lipschitz condition in its second variable’ if there exists a constant $L$ , known as a ‘Lipschitz constant’, such that for any $x \in [ a , b ]$ and $Y , Z \in \mathbb { R } ^ { N }$ , $\| f ( x , Y ) - f ( x , Z ) \| \leq L \| Y - Z \|$ .

We need a basic lemma on metric spaces known as the ‘contraction mapping principle’. We present this without proof.

Lemma 110B Let $M$ denote a complete metric space with metric $\rho$ and let $\phi : { \cal M }  { \cal M }$ denote a mapping which is a contraction, in the sense that there exists a number $k$ , satisfying $0 \leq k < 1$ , such that, for any $\eta , \zeta \in M$ , $\rho ( \phi ( \eta ) , \phi ( \zeta ) ) \leq k \rho ( \eta , \zeta )$ . Then there exists a unique $\xi \in M$ such that $\phi ( \xi ) = \xi$ .

We can now state our main result.

Theorem 110C Consider an initial value problem

$$
\begin{array} { c } { { y ^ { \prime } ( x ) = f ( x , y ( x ) ) , } } \\ { { y ( a ) = y _ { 0 } , } } \end{array}
$$

where $f : [ a , b ] \times \mathbb { R } ^ { N }  \mathbb { R } ^ { N }$ is continuous in its first variable and satisfies a Lipschitz condition in its second variable. Then there exists a unique solution to this problem.

Proof. Let $M$ denote the complete metric space of continuous functions $y : [ a , b ] \to \mathbb { R } ^ { N }$ , such that $y ( a ) = y _ { 0 }$ . The metric is defined by

$$
\rho ( y , z ) = \operatorname* { s u p } _ { x \in [ a , b ] } \exp ( - K ( x - a ) ) \| y ( x ) - z ( x ) \| ,
$$

where $K > L$ . For given $y \in M$ , define $\phi ( y )$ as the solution $Y$ on $[ a , b ]$ to the initial value problem

$$
\begin{array} { l c r } { { Y ^ { \prime } ( x ) = f ( x , Y ( x ) ) , } } \\ { { Y ( a ) = y _ { 0 } . } } \end{array}
$$

This problem is solvable by integration as

$$
\phi ( y ) ( x ) = y _ { 0 } + \int _ { a } ^ { x } f ( s , y ( s ) ) d s .
$$

This is a contraction because for any two $y , z \in M$ , we have

$$
\begin{array} { r l } { \rho ( \phi ( y ) , \phi ( z ) ) \leq } & { \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \left\| \int _ { a } ^ { x } \big ( f ( s , y ( s ) ) - f ( s , z ( s ) ) \big ) d s \right\| } \\ & { \leq \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \| f ( s , y ( s ) ) - f ( s , z ( s ) ) \| d s } \\ & { \leq L \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \| y ( s ) - z ( s ) \| d s } \\ & { \leq L \rho ( y , z ) \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \exp ( K ( s - a ) ) d s } \\ & { \leq L \rho ( y , z ) \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \exp ( K ( s - a ) ) d s } \\ & { \leq \frac { L } { K } \rho ( y , z ) . } \end{array}
$$

The unique function $y$ that therefore exists satisfying $\phi ( y ) = y$ , is evidently the unique solution to the initial value problem given by (110a), (110b). 

The third requirement for being well-posed, that the solution is not overly sensitive to the initial condition, can be readily assessed for problems satisfying

a Lipschitz condition. If $y$ and $z$ each satisfy (110a) with $y ( a ) \ = \ y _ { 0 }$ and $z ( a ) = z _ { 0 }$ , then

$$
\frac { d } { d x } \| y ( x ) - z ( x ) \| \leq L \| y ( x ) - z ( x ) \| .
$$

Multiply both sides by $\exp ( - L x )$ and deduce that

$$
{ \frac { d } { d x } } { \big ( } \exp ( - L x ) \| y ( x ) - z ( x ) \| { \big ) } \leq 0 ,
$$

implying that

$$
\begin{array} { r } { \| y ( x ) - z ( x ) \| \leq \| y _ { 0 } - z _ { 0 } \| \exp \big ( L ( x - a ) \big ) . } \end{array}
$$

This bound on the growth of initial perturbations may be too pessimistic in particular circumstances. Sometimes it can be improved upon by the use of ‘one-sided Lipschitz conditions’. This will be discussed in Subsection 112.

# 111 Linear systems of differential equations

Linear differential equations are important because of the availability of a superposition principle. That is, it is possible for a linear differential equation system to combine known solutions to construct new solutions. The standard form of a linear system is

$$
\frac { d y } { d x } = A ( x ) y + \phi ( x ) ,
$$

where $A ( x )$ is a possibly time-dependent linear operator. The corresponding ‘homogeneous’ system is

$$
{ \frac { d y } { d x } } = A ( x ) y .
$$

The superposition principle, which is trivial to verify, states that:

Theorem 111A If $\widehat { y }$ is a solution to (111a) and $y _ { 1 } , y _ { 2 } , \ldots , y _ { k }$ are solutions to (111b), then for any constants $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$ , the function $y$ given by

$$
\boldsymbol { y } ( \boldsymbol { x } ) = \boldsymbol { \widehat { y } } ( \boldsymbol { x } ) + \sum _ { i = 1 } ^ { k } \alpha _ { i } \boldsymbol { y } _ { i } ( \boldsymbol { x } ) ,
$$

is a solution to (111a).

The way this result is used is to attempt to find the solution which matches a given initial value, by combining known solutions.

Many linear problems are naturally formulated in the form of a single high order differential equation

$$
Y ^ { ( m ) } ( x ) - C _ { 1 } ( x ) Y ^ { ( m - 1 ) } ( x ) - C _ { 2 } ( x ) Y ^ { ( m - 2 ) } ( x ) - \cdot \cdot \cdot - C _ { m } ( x ) Y ( x ) = g ( x ) .
$$

By identifying $Y ( x ) = y _ { 1 } ( x ) , Y ^ { \prime } ( x ) = y _ { 2 } ( x ) , . . . , Y ^ { ( m - 1 ) } = y _ { m } ( x )$ , we can rewrite the system in the form

$$
\frac d { d x } \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { m } ( x ) } \end{array} \right] = A ( x ) \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { m } ( x ) } \end{array} \right] + \phi ( x ) ,
$$

where the ‘companion matrix’ $A ( x )$ and the ‘inhomogeneous term’ $\phi ( x )$ are given by

$$
\mathbf { \Psi } ( x ) = \left[ \begin{array} { c c c c c c } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } \\ { C _ { m } ( x ) } & { C _ { m - 1 } ( x ) } & { C _ { m - 2 } ( x ) } & { \cdots } & { C _ { 1 } ( x ) } \end{array} \right] , \quad \phi ( x ) = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { g ( x ) } \end{array} \right] .
$$

When $A ( x ) = A$ in (111b) is constant, then to each eigenvalue $\lambda$ of $A$ , with corresponding eigenvector $\boldsymbol { v }$ , there exists a solution given by

$$
y ( x ) = \exp ( \lambda x ) v .
$$

When a complete set of eigenvectors does not exist, but corresponding to $\lambda$ there is a chain of generalized eigenvectors

$$
A v _ { 1 } = \lambda v _ { 1 } + v , \quad A v _ { 2 } = \lambda v _ { 2 } + v _ { 1 } , \quad \ldots , \quad A v _ { k - 1 } = \lambda v _ { k - 1 } + v _ { k - 2 } ,
$$

then there is a chain of additional independent solutions to append to (111d):

$$
y _ { 1 } = x \exp ( \lambda x ) v _ { 1 } , \quad y _ { 2 } = x ^ { 2 } \exp ( \lambda x ) v _ { 2 } , \quad \ldots , \quad y _ { k - 1 } = x ^ { k - 1 } \exp ( \lambda x ) v _ { k - 1 } .
$$

In the special case in which $A$ is a companion matrix, so that the system is equivalent to a high order equation in a single variable, as in (111c), with $C _ { 1 } ( x ) = C _ { 1 } , C _ { 2 } ( x ) = C _ { 2 } , . . . , C _ { m } ( x ) = C _ { m }$ , each a constant, the characteristic polynomial of $A$ is

$$
P ( \lambda ) = \lambda ^ { m } - C _ { 1 } \lambda ^ { m - 1 } - C _ { 2 } \lambda ^ { m - 2 } - \cdot \cdot \cdot - C _ { m } = 0 .
$$

For this special case, $P ( \lambda )$ is also the minimal polynomial, and repeated zeros always correspond to incomplete eigenvector spaces and the need to use generalized eigenvectors. Also, in this special case, the eigenvector corresponding to $\lambda$ , together with the generalized eigenvectors if they exist, are

$$
\boldsymbol { \upsilon } = \left[ \begin{array} { c } { 1 } \\ { \lambda } \\ { \lambda ^ { 2 } } \\ { \vdots } \\ { \lambda ^ { m - 1 } } \end{array} \right] , \boldsymbol { v } _ { 1 } = \left[ \begin{array} { c } { 0 } \\ { 1 } \\ { 2 \lambda } \\ { \vdots } \\ { ( m - 1 ) \lambda ^ { m - 2 } } \end{array} \right] , \boldsymbol { v } _ { 2 } = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 1 } \\ { \vdots } \\ { \frac { ( m - 1 ) ( m - 2 ) } { 2 } \lambda ^ { m - 3 } } \end{array} \right] , \boldsymbol { \ldots } . \boldsymbol { \ldots } .
$$

# 112 Stiff differential equations

Many differential equation systems of practical importance in scientific modelling exhibit a distressing behaviour when solved by classical numerical methods. This behaviour is distressing because these systems are characterized by very high stability, which can turn into very high instability when approximated by standard numerical methods. We have already seen examples of stiff problems, in Subsections 102 and 104, and of course there are many more such examples. The concept of the ‘one-sided Lipschitz condition’ was mentioned in Subsection 110 without any explanation. Stiff problems typically have large Lipschitz constants, but many have more manageable one-sided Lipschitz constants, and this can be an aid in obtaining realistic growth estimates for the effect of perturbations.

We confine ourselves to problems posed on an inner product space. Thus we assume that there exists an inner product on $\mathbb { R } ^ { N }$ denoted by $\langle u , v \rangle$ , and that the norm is defined by $\| u \| ^ { 2 } = \langle u , u \rangle$ .

Definition 112A The function f satisfies a ‘one-sided Lipschitz condition’, with ‘one-sided Lipschitz constant’ l if for $a l l x \in [ a , b ]$ and $a l l u , v \in \mathbb { R } ^ { N } ,$

$$
\langle f ( x , u ) - f ( x , v ) , u - v \rangle \leq l \| u - v \| ^ { 2 } .
$$

It is possible that the function $f$ could have a very large Lipschitz constant but a moderately sized, or even negative, one-sided Lipschitz constant. The advantage of this is seen in the following result.

![](images/e7f68e229af62882ede24da454c5abfb9966990dc6e200fc5e51b776db818b68.jpg)

![](images/70566a35b72b86ad7795b1debf17114d7e5eb9210cc26f255e4c60b9f65e3e2a.jpg)

Proof. We have

$$
\begin{array} { l } { \displaystyle \frac { d } { d x } \| y ( x ) - z ( x ) \| ^ { 2 } = \frac { d } { d x } \langle y ( x ) - z ( x ) , y ( x ) - z ( x ) \rangle } \\ { = 2 \langle f ( x , y ( x ) ) - f ( x , z ( x ) ) , y ( x ) - z ( x ) \rangle } \\ { \leq 2 l \| y ( x ) - z ( x ) \| ^ { 2 } . } \end{array}
$$

Multiply by $\exp \big ( - 2 l ( x - x _ { 0 } ) \big )$ and it follows that

$$
\frac { d } { d x } \big ( \exp \big ( - 2 l ( x - x _ { 0 } ) \big ) \| y ( x ) - z ( x ) \| ^ { 2 } \big ) \leq 0 ,
$$

so that $\exp \big ( - 2 l ( x - x _ { 0 } ) \big ) \| y ( x ) - z ( x ) \| ^ { 2 }$ is non-increasing.

Note that the problem described in Subsection 102 possesses the one-sided Lipschitz condition with ${ \mathit { l } } = 0$ .

Even though stiff differential equation systems are typically non-linear, there is a natural way in which a linear system arises from a given non-linear system. Since stiffness is associated with the behaviour of perturbations to a given solution, we suppose that there is a small perturbation $\epsilon Y ( x )$ t o a solution $y ( x )$ . The parameter $\epsilon$ is small, in the sense that we are interested only in asymptotic behaviour of the perturbed solution as this quantity approaches zero. If $y ( x )$ is replaced by $y ( x ) + \epsilon Y ( x )$ in the differential equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

and the solution expanded in a series in powers of $\epsilon$ , with $\epsilon ^ { 2 }$ and higher powers replaced by zero, we obtain the system

$$
y ^ { \prime } ( x ) + \epsilon Y ^ { \prime } ( x ) = f ( x , y ( x ) ) + \epsilon { \frac { \partial f } { \partial y } } Y ( x ) .
$$

Subtract (112a) from (112b) and cancel out $\epsilon$ , and we arrive at the equation governing the behaviour of the perturbation,

$$
Y ^ { \prime } ( x ) = \frac { \partial f } { \partial y } Y ( x ) = J ( x ) Y ( x ) ,
$$

say. The ‘Jacobian matrix’ $J ( x )$ has a crucial role in the understanding of problems of this type; in fact its spectrum is sometimes used to characterize stiffness. In a time interval $\Delta x ,$ chosen so that there is a moderate change in the value of the solution to (112a), and very little change in $J ( x ) ,$ the eigenvalues of $J ( x )$ determine the growth rate of components of the perturbation. The existence of one or more large and negative values of $\lambda \Delta x ,$ $\mathrm { f o r } \ \lambda \in \sigma ( J ( x ) )$ , the spectrum of $J ( x )$ , is a sign that stiffness is almost certainly present. If $J ( x )$ possesses complex eigenvalues, then we interpret this test for stiffness as the existence of $\mathrm { ~ a ~ } \lambda = \mathrm { { R e } } \lambda + i \mathrm { { I m } } \lambda \in \sigma ( J ( x ) )$ such that Reλ∆x is negative with large magnitude.

# Exercises 11

11.1 Show how to modify Theorem 110C so that the Lipschitz condition holds only in a neighbourhood of $y _ { 0 }$ and where the solution is only required to exist on $[ a , b ]$ , where $\widetilde { b }$ satisfies $a < \widetilde { b } \le b$ .

11.2 By finding two vectors $\alpha$ and $\beta$ so that the system

$$
\begin{array} { r } { y ^ { \prime } ( x ) = \left[ \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] y ( x ) + \left[ \begin{array} { c } { \sin ( x ) } \\ { 0 } \\ { \cos ( x ) } \end{array} \right] , } \end{array}
$$

has a solution of the form ${ \widehat { y } } ( x ) = \sin ( x ) \alpha + \cos ( x ) \beta$ , find the general solution to this problem.

# 12 Further Evolutionary Problems

# 120 Many-body gravitational problems

We consider a more general gravitational problem involving $_ { n }$ mutually attracting masses $M _ { 1 } , M _ { 2 } , \ldots , M _ { n }$ at position vectors $y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dots , y _ { n } ( x )$ , satisfying the $_ { 3 n }$ -dimensional second order differential equation system

$$
y _ { i } ^ { \prime \prime } ( x ) = - \sum _ { j \neq i } { \frac { \gamma M _ { j } ( y _ { i } - y _ { j } ) } { \| y _ { i } - y _ { j } \| ^ { 3 } } } , \qquad i = 1 , 2 , \ldots , n .
$$

Reformulated as a first order system, the problem is $6 n$ -dimensional because each of the $y _ { i }$ has three components and the velocity vectors $y _ { i } ^ { \prime }$ also have three components.

To reduce this problem to a manageable level in situations of practical interest, some simplifications can be made. For example, in models of the solar system, the most massive planets, Jupiter, Uranus, Neptune and Saturn, are typically regarded as the only bodies capable of influencing the motion of the sun and of each other. The four small planets closest to the sun, Mercury, Venus, Earth and Mars, are, in this model, regarded as part of the sun in the sense that they add to its mass in attracting the heavy outer planets towards the centre of the solar system. To study the motion of the small planets or of asteroids, they can be regarded as massless particles, moving in the gravitation fields of the sun and the four large planets, but not at the same time influencing their motion.

Another model, involving only three bodies, is useful for studying the motion of an Earth–Moon satellite or of an asteroid close enough to the Earth to be strongly influenced by it as well as by the Sun. This system, known as the restricted three–body problem, regards the two heavy bodies as revolving in fixed orbits about their common centre of mass and the small body as attracted by the two larger bodies but not affecting their motion in any way. If it is possible to approximate the large-body orbits as circles, then a further simplification can be made by working in a frame of reference that moves with them. Thus, we would regard the two large bodies as being fixed in space with their rotation in the original frame of reference translated into a modification of the equations of gravitational motion.

To simplify this discussion, we use units scaled to reduce a number of constants to unit value. We scale the masses of the two larger bodies to $1 - \mu$ and $\mu$ and their positions relative to the moving reference frame by the vectors $( \mu - 1 ) e _ { 1 }$ and $\mu e _ { 1 }$ , so that their centre of mass is at the origin of coordinates. Write $y _ { 1 }$ , $y _ { 2 }$ and $y _ { 3 }$ as the scalar variables representing the position coordinates of the small body and $y _ { 4 }$ , $y _ { 5 }$ and $y _ { 6 }$ as the corresponding velocity coordinates. Under these assumptions, the equations of motion become

![](images/930f4d2a1612a67d13ed6e9bdb6b9e75b0bb8c729f031ebc133da1960b39358a.jpg)  
A solution to the restricted three-body problem

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = y _ { 4 } , } \\ & { y _ { 2 } ^ { \prime } = y _ { 5 } , } \\ & { y _ { 3 } ^ { \prime } = y _ { 6 } , } \\ & { y _ { 4 } ^ { \prime } = 2 y _ { 5 } + y _ { 1 } - \frac { \mu \left( y _ { 1 } + \mu - 1 \right) } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) \left( y _ { 1 } + \mu \right) } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } , } \\ & { y _ { 5 } ^ { \prime } = - 2 y _ { 4 } + y _ { 2 } - \frac { \mu y _ { 2 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) y _ { 2 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } } \\ & { y _ { 6 } ^ { \prime } = - \frac { \mu y _ { 3 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) y _ { 3 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } . } \end{array}
$$

Planar motion is possible; that is, solutions in which $y _ { 3 } = y _ { 6 } = 0$ at all times. One of these is shown in Figure $1 2 0 ( \mathrm { i } )$ , with the values of $( y _ { 1 } , y _ { 2 } )$ plotted as the orbit evolves. The heavier mass is at the point $( \mu , 0 )$ and the lighter mass is at $( 1 - \mu , 0 )$ , where $( 0 , 0 )$ is marked 0 and $( 1 , 0 )$ is marked $^ { 1 }$ . For this calculation the value of $\mu = 1 / 8 1 . 4 5$ was selected, corresponding to the Earth-Moon system. The initial values for this computation were $\begin{array} { c c l } { { ( y _ { 1 } , y _ { 2 } , y _ { 3 } , y _ { 4 } , y _ { 5 } , y _ { 6 } ) } } & { { = } } & { { ( 0 . 9 9 4 , 0 , 0 , 0 , - 2 . 0 0 1 5 8 5 1 0 6 3 7 9 0 8 2 5 2 2 4 , 0 ) } } \end{array}$ and the period was 17.06521656015796.

![](images/ac27af0624e5d41c865c35f221fb73ac279a0bb1b9dfc6891cd3ce66c0fbed63.jpg)  
A second solution to the restricted three-body problem

![](images/5d87e128594947b12440fc27b1b2e878d9230caf38c4456f39efa69733c0c93b.jpg)  
A figure-of-eight orbit for three equal masses

A second solution, identical except for the initial value $\left( y _ { 1 } , y _ { 2 } , y _ { 3 } , y _ { 4 } , y _ { 5 } , y _ { 6 } \right)$ $= ( 0 . 8 7 9 7 8 , 0 , 0 , 0 , - 0 . 3 7 9 7 , 0 )$ ) and a period 19.14045706162071, is shown in Figure 120(ii).

If the three masses are comparable in value, then the restriction to a simpler system that we have considered is not available. However, in the case of a number of equal masses, other symmetries are possible. We consider just a single example, in which three equal, mutually attracting masses move in a figure-of-eight orbit. This is shown in Figure 120(iii).

![](images/66accfeec67fab96b5f831d1d86131268b2cdc28faf615ce7657237c200587ee.jpg)  
Solution to delay differential equation (121b)

121 Delay problems and discontinuous solutions

A functional differential equation is one in which the rate of change of $y ( x )$ depends not just on the values of $y$ for the same time value, but also on time values less than $x$ . In the simplest case, this has the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) , y ( x - \tau ) ) ,
$$

where $^ { - }$ is a constant delay. Note that this cannot be cast as an initial value problem with the hope of actually defining a unique solution, because at an initial point $x _ { 0 }$ , the derivative depends on the value of $y ( x _ { 0 } - \tau )$ . What we will need to do in the case of (121a) is to specify the value of $y$ on an initial interval $[ x _ { 0 } - \tau , x _ { 0 } ]$ .

A linear delay differential equation

We consider the problem given by

$$
\begin{array} { r } { y ^ { \prime } ( x ) = - y ( x - \frac { \pi } { 2 } ) , \quad x > 0 , \qquad y ( x ) = x , \quad x \in [ - \frac { \pi } { 2 } , 0 ] . } \end{array}
$$

For $x$ in the interval $[ 0 , \frac { \pi } { 2 } ]$ we find

$$
y ( x ) = - \int _ { 0 } ^ { x } ( x - { \textstyle \frac { \pi } { 2 } } ) d x = { \textstyle \frac { 1 } { 2 } } x ( \pi - x ) ,
$$

with $\begin{array} { r } { y ( \frac { \pi } { 2 } ) = \frac { 1 } { 8 } \pi ^ { 2 } } \end{array}$ . This process can be repeated over the sequence of intervals $[ \frac { \pi } { 2 } , \pi ]$ , $[ \pi , { \textstyle \frac { 3 \pi } { 2 } } ]$ , $\cdot \cdot \cdot$ to obtain values of $y ( x )$ shown in Figure 121(i) for $x \leq 4 \pi$ .

It appears that the solution is attempting to approximate sinusoidal behaviour as time increases. We can verify this by estimating a local amplitude defined by

$$
A ( x ) = ( y ( x ) ^ { 2 } + y ^ { \prime } ( x ) ^ { 2 } ) ^ { \frac { 1 } { 2 } } .
$$

This function is also shown in Figure $\mathrm { 1 2 1 ( i ) }$ and we note the discontinuity at $x \ = \ 0$ , corresponding to the discontinuity in the value of $y ^ { \prime } ( x )$ . Such discontinuities are to be expected because the right-derivative is given by the formula for $y ^ { \prime } ( x )$ for $x$ positive and the left-derivative is found from the derivative of the initial function. For each positive integral multiple of $\scriptstyle { \frac { 1 } { 2 } } \pi$ , there will always be an inherited non-smooth behaviour but this will be represented by a discontinuity in increasingly higher derivatives.

![](images/db14b96a7e562ed9350742357a0ab32dc9586a0a1247cd5b36edc95694748014.jpg)  
Solution to neutral delay differential equation (121c)

We will now consider a problem with two delays.

# An example with persistent discontinuities

A delay differential equation of ‘neutral type’ is one in which delayed values of $y ^ { \prime }$ also occur in the formulation. An example of this type of problem is

$$
\begin{array} { r l r l } & { y ^ { \prime } ( x ) = \frac { 1 } { 2 } y ^ { \prime } ( x - 1 ) + a y ( x - \sqrt { 2 } ) , } & & { x > 0 , } \\ & { y ( x ) = 1 , } & & { x \in [ - \sqrt { 2 } , 0 ] , } \end{array}
$$

where the constant is given by $\begin{array} { r } { a = \exp ( \sqrt { 2 } ) - \frac { 1 } { 2 } \exp ( \sqrt { 2 } - 1 ) } \end{array}$ and was contrived to ensure that $\exp ( x )$ would have been a solution, if the initial information had been defined in terms of that function.

The solution is shown in Figure 121(ii) and we see that it seems to be approximating exponential behaviour more and more closely as $x$ increases. However, there is a discontinuity in $y ^ { \prime } ( x )$ at every positive integer value of $x$ . Specifically, for each $n$ there is a jump given by

$$
\operatorname* { l i m } _ { x \to n + } y ^ { \prime } ( x ) - \operatorname* { l i m } _ { x \to n - } y ^ { \prime } ( x ) = 2 ^ { - n } a .
$$

# 122 Problems evolving on a sphere

Given a function $H ( y )$ , we will explore situations in which solutions to $y ^ { \prime } ( x ) \ = \ f ( y )$ preserve the value of $H ( y ( x ) )$ . In the special case in which $H ( y ) ~ = ~ \textstyle { \frac { 1 } { 2 } } \| y \| ^ { 2 }$ , this will correspond to motion on a sphere. We recall the standard notation

$$
\begin{array} { r } { \nabla ( H ) = \left[ \begin{array} { c } { \frac { \partial H } { \partial y _ { 1 } } } \\ { \frac { \partial H } { \partial y _ { 2 } } } \\ { \vdots } \\ { \frac { \partial H } { \partial y _ { N } } } \end{array} \right] } \end{array}
$$

and consider problems of the ‘Poisson’ form

$$
y ^ { \prime } = L ( x , y ) \nabla ( y ) ,
$$

where $L ( x , y )$ is always a skew-symmetric matrix. For such problems $H ( y ( x ) )$ is invariant. To verify this, calculate

$$
{ \frac { d } { d x } } H ( y ( x ) ) = \sum _ { i = 1 } ^ { N } { \frac { \partial H } { \partial y _ { i } } } y _ { i } ^ { \prime } ( x ) = \nabla ( H ) ^ { \top } L ( x , y ) \nabla ( y ) = 0 ,
$$

because of the skew-symmetry of $L$ .

The Euler equations, discussed in Subsection 107, provide two examples of this. To show that $E ( w )$ is invariant write $\begin{array} { r } { H ( w ) = \frac { 1 } { 2 } E ( w ) } \end{array}$ , and to show that $F ( w )$ is invariant write $\begin{array} { r } { H ( w ) = \frac { 1 } { 2 } F ( w ) } \end{array}$ . The problem reverts to the form of (122a), with $y$ replaced by $w$ , where $L ( x , w )$ is given by

$$
\left[ \begin{array} { c c c } { { 0 } } & { { \frac { I _ { 3 } w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { - \frac { I _ { 2 } w _ { 2 } } { I _ { 1 } I _ { 3 } } } } \\ { { - \frac { I _ { 3 } w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { 0 } } & { { \frac { I _ { 1 } w _ { 1 } } { I _ { 2 } I _ { 3 } } } } \\ { { \frac { I _ { 2 } w _ { 2 } } { I _ { 1 } I _ { 3 } } } } & { { - \frac { I _ { 1 } w _ { 1 } } { I _ { 2 } I _ { 3 } } } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { c c c } { { 0 } } & { { - \frac { w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { \frac { w _ { 2 } } { I _ { 1 } I _ { 3 } } } } \\ { { \frac { w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { 0 } } & { { - \frac { w _ { 1 } } { I _ { 2 } I _ { 3 } } } } \\ { { - \frac { w _ { 2 } } { I _ { 1 } I _ { 3 } } } } & { { \frac { w _ { 1 } } { I _ { 2 } I _ { 3 } } } } & { { 0 } } \end{array} \right] ,
$$

respectively.

We now revert to the special case $\begin{array} { r } { H ( x ) = \frac { 1 } { 2 } y ^ { \intercal } y } \end{array}$ , for which (122a) becomes

$$
y ^ { \prime } = L ( x , y ) y .
$$

An example is the contrived problem

$$
{ \left[ \begin{array} { l } { y _ { 1 } ^ { \prime } } \\ { y _ { 2 } ^ { \prime } } \\ { y _ { 3 } ^ { \prime } } \end{array} \right] } = { \left[ \begin{array} { l l l } { ~ 0 } & { - y _ { 1 } } & { - \sin ( x ) } \\ { ~ y _ { 1 } } & { ~ 0 } & { ~ - 1 } \\ { \sin ( x ) } & { 1 } & { ~ 0 } \end{array} \right] } ~ { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right] } , ~ { \left[ \begin{array} { l } { y _ { 1 } ( 0 ) } \\ { y _ { 2 } ( 0 ) } \\ { y _ { 3 } ( 0 ) } \end{array} \right] } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } ,
$$

with solution $y _ { 1 } ( x ) = \cos ( x )$ , $y _ { 2 } ( x ) = \cos ( x ) \sin ( x )$ , $y _ { 3 } ( x ) = \sin ^ { 2 } ( x )$ . The solution values for $x \in [ 0 , 1 . 4 \pi ]$ are shown in Figure $1 2 2 ( \mathrm { i } )$ .

Problems of the form (122b) are a special case of

$$
Y ^ { \prime } = L ( x , Y ) Y ,
$$

where $Y$ has a number of columns. In this case the inner product of two specific columns will be invariant. In particular, if $Y ( x )$ is a square matrix,

![](images/58c07b19b162bdabedb36b15be96c20ca928769870cb6435e0e5d7c7784ef5a8.jpg)  
Solution to problem (122c) with $_ { y 3 }$ pointing out of the page

initially orthogonal, and $L ( x , Y )$ is always skew-symmetric, then $Y ( x )$ will remain orthogonal. Denote the elements of $Y$ by $y _ { i j }$ . An example problem of this type is

$$
Y ^ { \prime } ( x ) = \left[ \begin{array} { c c c c } { { 0 } } & { { - 1 } } & { { \mu y _ { 2 1 } } } \\ { { 1 } } & { { 0 } } & { { - \mu y _ { 1 1 } } } \\ { { - \mu y _ { 2 1 } } } & { { \mu y _ { 1 1 } } } & { { 0 } } \end{array} \right] Y , \qquad Y ( 0 ) = I ,
$$

with $\mu$ a real parameter. The solution to (122e) is

$$
Y ( x ) = \left[ \begin{array} { c c c c } { \cos ( x ) } & { - \sin ( x ) \cos ( \mu x ) } & { } & { \sin ( x ) \sin ( \mu x ) } \\ { \sin ( x ) } & { \cos ( x ) \cos ( \mu x ) } & { - \cos ( x ) \sin ( \mu x ) } \\ { 0 } & { \sin ( \mu x ) } & { } & { \cos ( \mu x ) } \end{array} \right] .
$$

# 123 Further Hamiltonian problems

In the Hamiltonian formulation of classical mechanics, generalized coordinates $q _ { 1 }$ , $q _ { 2 }$ , . . . , $q _ { N }$ and generalized momenta $p _ { 1 }$ , $p _ { 2 }$ , $\cdot \cdot \cdot$ , $p _ { N }$ are used to represent the state of a mechanical system. The equations of motion are defined in terms

of a ‘Hamiltonian’ function $H ( p _ { 1 } , p _ { 2 } , \ldots , p _ { N } , q _ { 1 } , q _ { 2 } , \ldots , q _ { N } )$ by the equations

$$
\begin{array} { l } { { \displaystyle p _ { i } ^ { \prime } = - \frac { \partial H } { \partial q _ { i } } , } } \\ { { \displaystyle q _ { i } ^ { \prime } = \frac { \partial H } { \partial p _ { i } } . } } \end{array}
$$

Write $y ( x )$ as a vector variable, made up from $N$ momenta followed by the $N$ coordinates. That is,

$$
\begin{array} { r } { y _ { i } = \left\{ \begin{array} { l l } { p _ { i } , \quad \quad \quad 1 \leq i \leq N , } \\ { q _ { i - N } , \quad N + 1 \leq i \leq 2 N . } \end{array} \right. } \end{array}
$$

With the understanding that $H$ is regarded as a function of $y$ , the differential equations can be written in the form $y ^ { \prime } = f ( y )$ , where

$$
\boldsymbol { f } ( \boldsymbol { y } ) = \boldsymbol { J } \boldsymbol { \nabla } ( \boldsymbol { H } ) , \qquad \boldsymbol { J } = \left[ \begin{array} { l l } { 0 } & { - \boldsymbol { I } } \\ { \boldsymbol { I } } & { \ 0 } \end{array} \right] ,
$$

in which $I$ is the $N \times N$ unit matrix.

Theorem 123A $H ( y ( x ) )$ is invariant.

Proof. Calculate $\partial H / \partial y$ to obtain the result

The Jacobian of this problem is equal to

$$
\frac { \partial } { \partial y } f ( y ) = \frac { \partial } { \partial y } \left( J \nabla ( H ) \right) = J W ( y ) ,
$$

where $W$ is the ‘Wronskian’ matrix defined as the $2 N \times 2 N$ matrix with $( i , j )$ element equal to $\partial ^ { 2 } H / \partial y _ { i } \partial y _ { j }$ .

If the initial value $y _ { 0 } = y ( x _ { 0 } )$ is perturbed by a small number $\epsilon$ multiplied by a fixed vector $v _ { 0 }$ , then, to within $O ( \epsilon ^ { 2 } )$ , the solution is modified by $\epsilon v + O ( \epsilon ^ { 2 } )$ where

$$
v ^ { \prime } ( x ) = \frac { \partial f } { \partial y } v ( x ) = J W ( y ) v ( x ) .
$$

For two such perturbations $u$ and $\boldsymbol { v }$ , it is interesting to consider the value of the scalar $u ^ { \intercal } J v$ .

This satisfies the differential equation

$$
\frac { d } { d x } u ^ { \top } J v = u ^ { \top } J J W v + ( J W u ) ^ { \top } J v = - u ^ { \top } W v + u ^ { \top } W v = 0 .
$$

Hence we have:

![](images/dadda48945c747f8d40cffb4f8c1d188edcdbf33b3e86a65ad2e5edd43f4de68.jpg)  
Illustration of symplectic behaviour for $H ( p , q ) = p ^ { 2 } / 2 + q ^ { 2 } / 2$ (left) and $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ (right). The underlying image depicts the North Island brown kiwi, Apteryx mantelli.

# Theorem 123B $u ^ { \intercal } J v$ is invariant with time.

In the special case of a two-dimensional Hamiltonian problem, the value of $\left( \epsilon u \right) ^ { \prime } J ( \epsilon v )$ can be interpreted as the area of the infinitesimal parallelogram with sides in the directions $u$ and $v$ . As the solution evolves, $u$ and $v$ might change, but the area $u ^ { \prime } J v$ remains invariant. This is illustrated in Figure 123(i) for the two problems $H ( p , q ) = p ^ { 2 } / 2 + q ^ { 2 } / 2$ and $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ respectively.

# 124 Further differential-algebraic problems

Consider the initial value problem

$$
\begin{array} { c } { { y ^ { \prime } = y + z , } } \\ { { \begin{array} { r l } \end{array} } } \\ { { 0 = z + z ^ { 3 } - y , } } \\ { { \begin{array} { r l } \end{array} } } \\ { { y ( 0 ) = 2 , \quad z ( 0 ) = 1 . } } \end{array}
$$

This is an index 1 problem, because a single differentiation of (124b) and a substitution from (124a) converts this to a differential equation system consisting of (124b) together with $z ^ { \prime } = ( y + z ) / ( 1 + 3 z ^ { 2 } )$ . However, this reduction does not do justice to the original formulation in the sense that a solution with slightly perturbed initial values has little to do with the original index 1 problem. This emphasizes the fact that initial conditions for the differential-algebraic equation formulation must be consistent with the algebraic constraint for it to be well-posed. A more appropriate reduction is to replace (124a) by $y ^ { \prime } = y + \phi ( y )$ , where $\phi ( y )$ is the real value of $z$ which satisfies (124b).

We next introduce an initial value problem comprising two differential equations and a single algebraic constraint:

$$
\begin{array} { c } { { y _ { 1 } ^ { \prime } = - \sin ( z ) , } } \\ { { y _ { 2 } ^ { \prime } = 2 \cos ( z ) - y _ { 1 } , } } \\ { { 0 = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } - 1 , } } \\ { { y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = 0 , \qquad z ( 0 ) = 0 . } } \end{array}
$$

An attempt to reduce this to an ordinary differential equation system by differentiating (124f) and substituting from (124d) and (124e), leads to a new algebraic constraint

$$
- y _ { 1 } \sin ( z ) + y _ { 2 } ( 2 \cos ( z ) - y _ { 1 } ) = 0 ,
$$

and it is clear that this will be satisfied by the solution to the original problem. However, this so-called ‘hidden constraint’ introduces a new complexity into this type of problem. That is, for initial values to be consistent, (124h) must be satisfied at the initial time. If, for example, the initial values $y _ { 1 } ( 0 ) = 1$ and $y _ { 2 } ( 0 ) = 0$ are retained, but the initial value $z ( 0 )$ is perturbed slightly, (124h) will not be satisfied and no genuine solution exists. But the hidden constraint, as the problem has actually been posed, is satisfied, and we can take the reduction towards an ordinary differential equation system to completion. Differentiate (124h) and substitute from (124d) and (124e) and we finally arrive at

$$
z ^ { \prime } ( \cos ^ { 2 } ( z ) + 2 \sin ^ { 2 } ( z ) ) = \sin ^ { 2 } ( z ) + y _ { 2 } \sin ( z ) + ( 2 \cos ( z ) - y _ { 1 } ) ^ { 2 } .
$$

Because two differentiation steps were required to reach this equation, the original system is referred to as an index 2 problem. In summary, the original index 2 problem, comprising (124d), (124e), (124f) has been reduced, first to an index 1 formulation (124d), (124e), (124h), and then to an ordinary differential equation system (124d), (124e), (124i).

# Exercises 12

12.1 Show that a problem of the form

$$
\begin{array} { l } { { u ^ { \prime } = - \alpha ^ { \prime } ( v ) \gamma ( u , v ) , } } \\ { { v ^ { \prime } = \beta ^ { \prime } ( u ) \gamma ( u , v ) , } } \end{array}
$$

satisfies the assumptions of (122a) with a suitable choice of $H ( u , v )$ .

12.2 Write the Lotka–Volterra equations (106a), (106b) in the form given in Exercise 12.1.

# 13 Difference Equation Problems

# 130 Introduction to difference equations

While differential equations deal with functions of a continuous variable, difference equations deal with functions of a discrete variable. Instead of a formula for the derivative of a function written in terms of the function itself, we have to consider sequences for which each member is related in some specific way to its immediate predecessor or several of its most recent predecessors. Thus we may write

$$
x _ { n } = \phi _ { n } ( x _ { n - 1 } , x _ { n - 2 } , \ldots , x _ { n - k } ) ,
$$

where $k$ is the ‘order’ of this difference equation. This equation, in which $x _ { n }$ depends on $k$ previous values, can be recast in a vector setting in which members of the sequence lie not in $\mathbb { R }$ but in $\mathbb { R } ^ { k }$ , and depend only on one previous value. Thus if

$$
X _ { n } = \left[ \begin{array} { c } { { x _ { n } } } \\ { { x _ { n - 1 } } } \\ { { \vdots } } \\ { { x _ { n - k + 1 } } } \end{array} \right] ,
$$

then

$$
X _ { n } = \Phi _ { n } ( X _ { n - 1 } ) = \left[ \begin{array} { c } { \phi _ { n } ( x _ { n - 1 } , x _ { n - 2 } , \ldots , x _ { n - k } ) } \\ { x _ { n - 1 } } \\ { x _ { n - 2 } } \\ { \vdots } \\ { x _ { n - k + 1 } } \end{array} \right] .
$$

Just as for differential equations, we can use either formulation as we please.

# 131 A linear problem

Consider the difference equation

$$
y _ { n } = 3 y _ { n - 1 } - 2 y _ { n - 2 } + C \theta ^ { n } ,
$$

where $C$ and $\theta$ are constants. We do not specify an initial value, but aim instead to find the family of all solutions. As a first step, we look at the special case in which $C = 0$ . In this case, the equation becomes linear in the sense that known solutions can be combined by linear combinations. The simplified equation in matrix–vector form is

$$
\left[ \begin{array} { c } { y _ { n } } \\ { y _ { n - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { 3 } & { - 2 } \\ { 1 } & { 0 } \end{array} \right] \left[ \begin{array} { c } { y _ { n - 1 } } \\ { y _ { n - 2 } } \end{array} \right] ,
$$

which can be rewritten as

$$
\left[ \begin{array} { c } { y _ { n } - y _ { n - 1 } } \\ { - y _ { n } + 2 y _ { n - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { 2 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { y _ { n - 1 } - y _ { n - 2 } } \\ { - y _ { n - 1 } + 2 y _ { n - 2 } } \end{array} \right] ,
$$

with solution defined by

$$
\begin{array} { c } { { y _ { n } - y _ { n - 1 } = A 2 ^ { n - 1 } , } } \\ { { - y _ { n } + 2 y _ { n - 1 } = B , } } \end{array}
$$

for constants $A$ and $B$ . By eliminating $y _ { n - 1 }$ , we find

$$
y _ { n } = A 2 ^ { n } + B
$$

for the general solution. The fact that this combines powers of $2$ and $^ { 1 }$ , the eigenvalues of the matrix

$$
\left[ { \begin{array} { r r } { 3 } & { - 2 } \\ { 1 } & { 0 } \end{array} } \right] ,
$$

suggests that we can look for solutions for the original formulation in the form $\lambda ^ { n }$ without transforming to the matrix–vector formulation. Substitute this trial solution into (131a), with $C = 0$ , and we find, apart from a factor $\lambda ^ { n - 2 }$ , that the condition on $\lambda$ is

$$
\lambda ^ { 2 } - 3 \lambda + 2 = 0 .
$$

This is the characteristic polynomial of the matrix (131b), but it can be read off immediately from the coefficients in (131a).

To find the general solution to (131a), if $C \neq 0$ , it is easy to see that we only need to find one special solution to which we can add the terms $A 2 ^ { n } + B$ to obtain all possible solutions. A special solution is easily found, if $\theta \neq 1$ and $\theta \neq 2$ , in the form

$$
y _ { n } = \frac { C \theta ^ { n + 2 } } { ( \theta - 1 ) ( \theta - 2 ) } .
$$

This type of special solution is not available if $\theta$ equals either $^ { 1 }$ or 2. In these cases a special solution can be found as a multiple of $_ { n }$ or $n 2 ^ { { n } }$ , respectively. Combining these cases, we write the general solution as

$$
y _ { n } = { \left\{ \begin{array} { l l } { A 2 ^ { n } + B - C n , } & { \theta = 1 , } \\ { A 2 ^ { n } + B + 2 C n 2 ^ { n } , } & { \theta = 2 , } \\ { A 2 ^ { n } + B + { \frac { C \theta ^ { 2 } } { ( \theta - 1 ) ( \theta - 2 ) } } \theta ^ { n } , } & { \theta \neq 1 , \theta \neq 2 . } \end{array} \right. }
$$

132 The Fibonacci difference equation

The initial value difference equation

$$
y _ { n } = y _ { n - 1 } + y _ { n - 2 } , \qquad y _ { 0 } = 0 , \quad y _ { 1 } = 1 ,
$$

is famous because of the mathematical, biological and even numerological significance attached to the solution values

$$
1 , 2 , 3 , 5 , 8 , 1 3 , 2 1 , 3 4 , 5 5 , 8 9 , 1 4 4 , \ldots .
$$

To find the general solution, solve the polynomial equation

$$
\lambda ^ { 2 } - \lambda - 1 = 0 ,
$$

to find the terms $\lambda _ { 1 } ^ { n }$ and $\lambda _ { 2 } ^ { n }$ , where

$$
\begin{array} { r } { \lambda _ { 1 } = \frac { 1 + \sqrt { 5 } } { 2 } , \quad \lambda _ { 2 } = \frac { 1 - \sqrt { 5 } } { 2 } = - \lambda _ { 1 } ^ { - 1 } . } \end{array}
$$

To find the coefficients $A$ and $B$ in the general solution

$$
\begin{array} { r } { y _ { n } = A \left( \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { n } + B \left( - \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { - n } , } \end{array}
$$

substitute $n = 0$ and $n = 1$ , to find $A = - B = 5 ^ { - 1 / 2 }$ , and therefore the specific solution to the initial value problem (132a),

$$
\begin{array} { r } { y _ { n } = \frac { 1 } { \sqrt { 5 } } \bigg ( \Big ( \frac { 1 + \sqrt { 5 } } { 2 } \Big ) ^ { n } - \Big ( - \frac { 1 + \sqrt { 5 } } { 2 } \Big ) ^ { - n } \bigg ) . } \end{array}
$$

# 133 Three quadratic problems

We consider the solutions to the problems

$$
\begin{array} { l } { y _ { n } = y _ { n - 1 } ^ { 2 } , } \\ { y _ { n } = y _ { n - 1 } ^ { 2 } - 2 , } \\ { y _ { n } = y _ { n - 1 } y _ { n - 2 } . } \end{array}
$$

If $z _ { n } = \ln ( y _ { n } )$ in (133a), then $z _ { n } = 2 z _ { n - 1 }$ with solution $z _ { n } = 2 ^ { n } z _ { 0 }$ . Hence, the general solution to (133a) is

$$
y _ { n } = y _ { 0 } ^ { 2 ^ { n } } .
$$

To solve (133b), substitute $y _ { n } = z _ { n } + z _ { n } ^ { - 1 }$ , so that

$$
z _ { n } + \frac { 1 } { z _ { n } } = z _ { n - 1 } ^ { 2 } + \frac { 1 } { z _ { n - 1 } ^ { 2 } } ,
$$

and this is satisfied by any solution to $z _ { n } = z _ { n - 1 } ^ { 2 }$ . Hence, using the known solution of (133a), we find

$$
y _ { n } = z _ { 0 } ^ { 2 ^ { n } } + z _ { 0 } ^ { - 2 ^ { n } } ,
$$

where $z _ { 0 }$ is one of the solutions to the equation

$$
z _ { 0 } + { \frac { 1 } { z _ { 0 } } } = y _ { 0 } .
$$

Finally, to solve (133c), substitute $z _ { n } = \ln ( y _ { n } )$ , and we find that

$$
z _ { n } = z _ { n - 1 } + z _ { n - 2 } .
$$

The general solution to this is found from the Fibonacci equation, so that substituting back in terms of $y _ { n }$ , we find

$$
y _ { n } = A ^ { \left( { \frac { 1 } { 2 } } ( 1 + { \sqrt { 5 } } ) \right) ^ { n } } \cdot B ^ { \left( { \frac { 1 } { 2 } } ( 1 - { \sqrt { 5 } } ) \right) ^ { n } } ,
$$

with $A$ and $B$ determined from the initial values.

# 134 Iterative solutions of a polynomial equation

We discuss the possible solution of the polynomial equation

$$
x ^ { 2 } - 2 = 0 .
$$

Of course this is only an example, and a similar discussion would be possible with other polynomial equations. Consider the difference equations

$$
\begin{array} { l l l } { { y _ { n } = y _ { n - 1 } - \displaystyle \frac { 1 } { 2 } y _ { n - 1 } ^ { 2 } + 1 , } } & { { y _ { 0 } = 0 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = y _ { n - 1 } - \displaystyle \frac { 1 } { 2 } y _ { n - 1 } ^ { 2 } + 1 , } } & { { y _ { 0 } = 4 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = y _ { n - 1 } - y _ { n - 1 } ^ { 2 } + 2 , } } & { { y _ { 0 } = \displaystyle \frac { 3 } { 2 } , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = \displaystyle \frac { y _ { n - 1 } } { 2 } + \displaystyle \frac { 1 } { y _ { n - 1 } } , } } & { { y _ { 0 } = 1 0 0 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = \displaystyle \frac { y _ { n - 1 } y _ { n - 2 } + 2 } { y _ { n - 1 } + y _ { n - 2 } } , } } & { { y _ { 0 } = 0 , } } \end{array}
$$

Note that each of these difference equations has $\sqrt { 2 }$ as a stationary point. That is, each of them is satisfied by $y _ { n } = { \sqrt { 2 } }$ , for every $n$ . Before commenting further, it is interesting to see what happens if a few values are evaluated numerically for each sequence. These are shown in Table 134(I).

Note that (134a) seems to be converging to $\sqrt { 2 }$ , whereas (134b) seems to have no hope of ever doing so. Of course the starting value, $y _ { 0 }$ , is the distinguishing feature, and we can perhaps investigate which values converge and which ones do not. It can be shown that the fate of the iterates for various starting values can be summarized as follows:

The first few terms in the solutions of some difference equations   

<table><tr><td></td><td></td><td>Equation (134a）Equation (134b） Equation (134c) Equation (134d) Equation (134e)</td><td></td><td></td></tr><tr><td>yo</td><td>0.0000000000</td><td>4.0000000000</td><td>1.50000000001.000000×10²0.0000000000</td><td></td></tr><tr><td>y1</td><td>1.0000000000 -3.0000000000</td><td></td><td>1.25000000005.001000×101.0000000000</td><td></td></tr><tr><td>y2</td><td>1.5000000000 -6.5000000000</td><td></td><td>1.68750000002.502500×102.0000000000</td><td></td></tr><tr><td>Y3</td><td>1.3750000000 -2.662500×10</td><td></td><td>0.8398437500 1.255246×101.3333333333</td><td></td></tr><tr><td>y4</td><td></td><td></td><td>1.4296875000 -3.800703×1022.1345062256 6.3558946949 1.4000000000</td><td></td></tr><tr><td>Y5</td><td></td><td></td><td>1.4076843262 -7.260579×104 -0.4216106015 3.3352816093 1.4146341463</td><td></td></tr><tr><td>y6</td><td></td><td></td><td></td><td>1.4168967451 -2.635873×1091.4006338992 1.9674655622 1.4142114385</td></tr></table>

$$
\begin{array} { l l } { y _ { 0 } \in \{ - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } \} } & { { \mathrm { C o n v e r g e n c e ~ t o ~ } } x = - { \sqrt { 2 } } } \\ { y _ { 0 } \in ( - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } ) { : } } & { { \mathrm { C o n v e r g e n c e ~ t o ~ } } x = { \sqrt { 2 } } } \\ { y _ { 0 } \notin [ - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } ] { : } } & { { \mathrm { D i v e r g e n c e } } } \end{array}
$$

Note that the starting value $y _ { 0 } = - { \sqrt { 2 } }$ , while it is a fixed point of the mapping given by (134a), is unstable; that is, any small perturbation from this initial value will send the sequence either into instability or convergence to $+ \sqrt { 2 }$ . A similar remark applies to $y _ { 0 } = 2 + { \sqrt { 2 } }$ , which maps immediately to $y _ { 1 } = - { \sqrt { 2 } }$ .

The difference equation (134c) converges to $\pm \sqrt { 2 }$ in a finite number of steps for $y _ { 0 }$ in a certain countable set; otherwise the sequence formed from this equation diverges.

Equation (134d) is the Newton method and converges quadratically to $\sqrt { 2 }$ for any positive $y _ { 0 }$ . By quadratic convergence, we mean that $| y _ { n } - { \sqrt { 2 } } |$ divided by $| y _ { n - 1 } - { \sqrt { 2 } } | ^ { 2 }$ is bounded. In fact, in the limit as $n \longrightarrow \infty$ ,

$$
{ \frac { y _ { n } - { \sqrt { 2 } } } { ( y _ { n - 1 } - { \sqrt { 2 } } ) ^ { 2 } } } \to { \frac { \sqrt { 2 } } { 4 } } .
$$

The iteration scheme given by (134e) is based on the secant method for solving non-linear equations. To solve $\phi ( y ) ~ = ~ 0$ , $y _ { n }$ is found by fitting a straight line through the two points $( y _ { n - 2 } , \phi ( y _ { n - 2 } ) )$ and $( y _ { n - 1 } , \phi ( y _ { n - 1 } ) )$ and defining $y _ { n }$ as the point where this line crosses the horizontal axis. In the case $\phi ( y ) = y ^ { 2 } - 2$ , this results in (134e).

It is interesting to ask if there exists an ‘order’ $k$ for this sequence. In other words, assuming that convergence is actually achieved, does $k \geq 1$ exist such that

$$
\frac { | y _ { n } - { \sqrt { 2 } } | } { | y _ { n - 1 } - { \sqrt { 2 } } | k }
$$

has a limiting value as $n \to \infty$ ? For the secant method $k$ does exist, and has the value $\textstyle k = { \frac { 1 } { 2 } } ( { \sqrt { 5 } } + 1 )$ .

# 135 The arithmetic-geometric mean

Let $a _ { 0 }$ and $b _ { 0 }$ be real numbers chosen so that $0 < b _ { 0 } < a _ { 0 }$ , and define the sequence of $( a _ { n } , b _ { n } )$ pairs by the formulae

$$
\begin{array} { l c r } { { a _ { n } = \frac { 1 } { 2 } ( a _ { n - 1 } + b _ { n - 1 } ) , } } & { { } } & { { n = 1 , 2 , \ldots . . . } } \\ { { b _ { n } = \sqrt { a _ { n - 1 } b _ { n - 1 } } , } } & { { } } & { { } } \end{array}
$$

We can verify (i) that $b _ { n - 1 } < b _ { n } < a _ { n } < a _ { n - 1 }$ for all $n \geq 1$ and (ii) that the sequence $a _ { 0 } - b _ { 0 }$ , $a _ { 1 } - b _ { 1 }$ , $a _ { 2 } - b _ { 2 } , \dots$ converges to zero. The truth of (i) follows from elementary properties of arithmetic and geometric means. Furthermore, (ii) can be proved from the identity

$$
a _ { n } - b _ { n } = { \frac { ( a _ { n - 1 } - b _ { n - 1 } ) ^ { 2 } } { 2 { \bigl ( } { \sqrt { a _ { n - 1 } } } + { \sqrt { b _ { n - 1 } } } { \bigr ) } ^ { 2 } } } .
$$

The common limit of the $a _ { n }$ and $b _ { n }$ sequences is known as the ‘arithmeticgeometric mean’ of $a _ { 0 }$ and $b _ { 0 }$ . We present a single application.

The quantities

$$
\begin{array} { l } { { F ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \left( a ^ { 2 } \cos ^ { 2 } ( \theta ) + b ^ { 2 } \sin ^ { 2 } ( \theta ) \right) ^ { - 1 / 2 } d \theta , } } \\ { { E ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \left( a ^ { 2 } \cos ^ { 2 } ( \theta ) + b ^ { 2 } \sin ^ { 2 } ( \theta ) \right) ^ { 1 / 2 } d \theta , } } \end{array}
$$

are known as ‘complete elliptic integrals’ of the first and second kind, respectively. The value of $4 E ( a , b )$ is the length of the circumference of the ellipse

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } = 1 .
$$

Use $a _ { 0 } = a$ and $b _ { 0 } = b$ as starting values for the computation of the sequences defined by (135a), and denote by $a _ { \infty }$ the arithmetic-geometric mean of $a _ { 0 }$ and $b _ { 0 }$ . Then it can be shown that

$$
F ( a _ { 0 } , b _ { 0 } ) = F ( a _ { 1 } , b _ { 1 } ) ,
$$

and therefore that

$$
F ( a _ { 0 } , b _ { 0 } ) = F ( a _ { \infty } , a _ { \infty } ) = \frac { \pi } { 2 a _ { \infty } } .
$$

The value of $E ( a _ { 0 } , b _ { 0 } )$ can also be found from the sequences that lead to the arithmetic-geometric mean. In fact

$$
E ( a _ { 0 } , b _ { 0 } ) = \frac { \pi } { 2 a _ { \infty } } \left( a _ { 0 } ^ { 2 } - 2 a _ { 1 } ( a _ { 0 } - a _ { 1 } ) - 4 a _ { 2 } ( a _ { 1 } - a _ { 2 } ) - 8 a _ { 3 } ( a _ { 2 } - a _ { 3 } ) - \cdot \cdot \cdot \right) .
$$

# Exercises 13

13.1 Write the difference equation given by (134e) in the form

$$
z _ { n } = \phi ( z _ { n - 1 } ) ,
$$

with $z _ { 0 }$ a given initial value.

13.2 Write the difference equation system

$$
\begin{array} { r l r } { \boldsymbol { u } _ { n } = \boldsymbol { u } _ { n - 1 } + \boldsymbol { v } _ { n - 1 } , } & { { } } & { \boldsymbol { u } _ { 0 } = 2 , } \\ { \boldsymbol { v } _ { n } = 2 \boldsymbol { u } _ { n - 1 } + \boldsymbol { v } _ { n - 1 } ^ { 2 } , } & { { } } & { \boldsymbol { v } _ { 0 } = 1 , } \end{array}
$$

in the form $y _ { n } = \phi ( y _ { n - 1 } , y _ { n - 2 } )$ , with $y _ { 0 }$ and $y _ { 1 }$ given initial values.

13.3 Use the formula for the error in linear interpolation together with the solution to (133c) to verify the order of convergence of (134e).

13.4 Calculate $\sqrt { 2 }$ by applying the Newton method to the equation

$$
2 x ^ { - 2 } - 1 = 0 .
$$

13.5 Calculate the value of $\sqrt { 3 }$ by applying the secant method to

$$
x ^ { 2 } - 3 = 0 .
$$

13.6 Calculate the circumference of the ellipse

$$
{ \frac { x ^ { 2 } } { 9 } } + { \frac { y ^ { 2 } } { 4 } } = 1 ,
$$

using the arithmetic-geometric mean.

# 14 Difference Equation Theory

140 Linear difference equations

The standard form for linear difference equation systems is

$$
X _ { n } = A _ { n } X _ { n - 1 } + \phi _ { n } ,
$$

which becomes an initial value problem if the value of the initial vector $X _ { 0 }$ is specified. The corresponding system in which $\phi _ { n }$ is omitted is the ‘homogeneous part’.

Many linear difference equations are more naturally formulated as

$$
y _ { n } = \alpha _ { n 1 } y _ { n - 1 } + \alpha _ { n 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { n k } y _ { n - k } + \psi _ { n } ,
$$

but these are easily recast in the form (140a) by writing

$$
X _ { n } = \left[ \begin{array} { c } { { y _ { n } } } \\ { { y _ { n - 1 } } } \\ { { \vdots } } \\ { { y _ { n - k + 1 } } } \end{array} \right] , \quad A _ { n } = \left[ \begin{array} { c c c c } { { \alpha _ { n 1 } } } & { { \alpha _ { n 2 } } } & { { \cdots } } & { { \alpha _ { n k } } } \\ { { 1 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right] , \quad \phi _ { n } = \left[ \begin{array} { c } { { \psi _ { n } } } \\ { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right] .
$$

To solve (140a) as an initial value problem, we need to use products of the form

$$
\prod _ { i = m } ^ { n } A _ { i } = A _ { n } A _ { n - 1 } \cdot \cdot \cdot A _ { m + 1 } A _ { m } .
$$

We have:

Theorem 140A The problem (140a), with initial value $X _ { 0 }$ given, has the unique solution

$$
y _ { n } = { \biggl ( } \prod _ { i = 1 } ^ { n } A _ { i } { \biggr ) } X _ { 0 } + \left( \prod _ { i = 2 } ^ { n } A _ { i } \right) \phi _ { 1 } + \left( \prod _ { i = 3 } ^ { n } A _ { i } \right) \phi _ { 2 } + \cdot \cdot \cdot + A _ { n } \phi _ { n - 1 } + \phi _ { n } .
$$

Proof. The result holds for $n = 0$ , and the general case follows by induction.

# 141 Constant coefficients

We consider the solution of a linear difference equation with constant coefficients:

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } + \psi _ { n } .
$$

The solution is found in terms of the solution to the canonical problem in which the initial information is given in the form

$$
\begin{array} { r } { \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { - 1 } } \\ { \vdots } \\ { y _ { - k + 2 } } \\ { y _ { - k + 1 } } \end{array} \right] = \left[ \begin{array} { c } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 0 } \end{array} \right] . } \end{array}
$$

Denote the solution to this problem at step $m$ by

$$
y _ { m } = \theta _ { m } , \qquad m = 0 , 1 , 2 , \ldots , n ,
$$

with $\theta _ { m } = 0$ for $m \ < \ 0$ . Given the difference equation (141a) with initial values $y _ { 0 } , y _ { 1 } , \ldots , y _ { k - 1 }$ , define linear combinations of this data by

$$
{ \left[ \begin{array} { l } { { \widetilde { y } } _ { k - 1 } } \\ { { \widetilde { y } } _ { k - 2 } } \\ { { \widetilde { y } } _ { k - 3 } } \\ { \vdots } \\ { { \widetilde { y } } _ { 1 } } \\ { { \widetilde { y } } _ { 0 } } \end{array} \right] } = { \left[ \begin{array} { l l l l l l } { 1 } & { \theta _ { 1 } } & { \theta _ { 2 } } & { \cdots } & { \theta _ { k - 2 } } & { \theta _ { k - 1 } } \\ { 0 } & { 1 } & { \theta _ { 1 } } & { \cdots } & { \theta _ { k - 3 } } & { \theta _ { k - 2 } } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \theta _ { k - 4 } } & { \theta _ { k - 3 } } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { \theta _ { 1 } } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] } ^ { - 1 } { \left[ \begin{array} { l } { y _ { k - 1 } } \\ { y _ { k - 2 } } \\ { y _ { k - 3 } } \\ { \vdots } \\ { y _ { 1 } } \\ { y _ { 0 } } \end{array} \right] } .
$$

We are now in a position to write down the solution to (141a).

Theorem 141A Using the notation introduced in this subsection, the solution to (141a) with given initial values $y _ { 0 } , y _ { 1 } , \ldots , y _ { k - 1 }$ is given by

$$
y _ { n } = \sum _ { i = 0 } ^ { k - 1 } \theta _ { n - i } { \widetilde { y } } _ { i } + \sum _ { i = k } ^ { n } \theta _ { n - i } \psi _ { i } .
$$

Proof. Substitute $n = m$ , for $m = 0 , 1 , 2 , \ldots , k - 1$ , into (141c), and we obtain the value

$$
y _ { m } = \widetilde { y } _ { m } + \theta _ { 1 } \widetilde { y } _ { m - 1 } + \cdot \cdot \cdot + \theta _ { m } \widetilde { y } _ { 0 } , \quad m = 0 , 1 , 2 , \ldots , k - 1 .
$$

This is equal to $y _ { m }$ if (141b) holds. Add the contribution to the solution from each of $m = k , k + 1 , \ldots , n$ and the result follows. 

# 142 Powers of matrices

We are interested in powers of a matrix $A$ in terms of two questions: when is the sequence of powers bounded, and when does the sequence converge to the zero matrix? There are various equivalent formulations of the criteria for these properties of $A$ , and we state the most widely accessible of these.

Definition 142A A square matrix $A$ is ‘stable’ if there exists a constant $C$ such that for all $n = 0 , 1 , 2 , \ldots$ , $\| A ^ { n } \| \leq C$ .

This property is often referred to as ‘power-boundedness’.

Definition 142B A square matrix A is ‘convergent’ if $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \| A ^ { n } \| = 0 } \end{array}$ .

Theorem 142C Let A denote an $m \times m$ matrix. The following statements are equivalent:

(i) A is stable.   
(ii) The minimal polynomial of A has all its zeros in the closed unit disc and all its multiple zeros in the open unit disc.   
(iii) The Jordan canonical form of $A$ has all its eigenvalues in the closed unit disc with all eigenvalues of magnitude 1 lying in $1 \times 1$ blocks.   
(iv) There exists a non-singular matrix $S$ such that $\| S ^ { - 1 } A S \| _ { \infty } \leq 1$ .

Proof. We prove that $( i ) \Rightarrow ( i i ) \Rightarrow ( i i i ) \Rightarrow ( i v ) \Rightarrow ( i )$ . If $A$ is stable but $( i i )$ is not true, then either there exist $\lambda$ and $v \neq 0$ such that $| \lambda | > 1$ and $A v = \lambda v$ , or there exist $\lambda$ , $u \ne 0$ and $\boldsymbol { v }$ such that $| \lambda | = 1$ and $A v = \lambda v + u$ , with $A u \ = \ \lambda u$ . In the first case, $A ^ { n } v \ = \lambda ^ { n } v$ and therefore $\| A ^ { n } \| ~ \geq ~ | \lambda | ^ { n }$ which is not bounded. In the second case, $A ^ { n } v = \lambda ^ { n } v + n \lambda ^ { n - 1 } u$ and therefore $\| A ^ { n } \| \geq n \| u \| / \| v \| - 1$ , which also is not bounded. Given $( i i )$ , it is not possible that the conditions of $( i i i )$ are not satisfied, because the minimal polynomial of any of the Jordan blocks, and therefore of $A$ itself, would have factors that contradict $( i i )$ . If $( i i i )$ is true, then $S$ can be chosen to form $J$ , the Jordan canonical form of $A$ , with the off-diagonal elements chosen sufficiently small so that $\| J \| _ { \infty } \leq 1$ . Finally, if $( i v )$ is true then $A ^ { n } = S ( S ^ { - 1 } A S ) ^ { n } S ^ { - 1 }$ so that $\| A ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } A S \| ^ { n } \cdot \| S ^ { - 1 } \| \leq \| S \| \cdot \| S ^ { - 1 } \|$ . 

Theorem 142D Let A denote an $m \times m$ matrix. The following statements are equivalent

(i) A is convergent.   
(ii) The minimal polynomial of $A$ has all its zeros in the open unit disc.   
(iii) The Jordan canonical form of $A$ has all its diagonal elements in the open unit disc.   
(iv) There exists a non-singular matrix $S$ such that $\| S ^ { - 1 } A S \| _ { \infty } < 1$ .

Proof. We again prove that $( i ) \Rightarrow ( i i ) \Rightarrow ( i i i ) \Rightarrow ( i v ) \Rightarrow ( i )$ . If $A$ is convergent but $( i i )$ is not true, then there exist $\lambda$ and $u \neq 0$ such that $\lambda \geq 1$ and $A u = \lambda u$ . Hence, $A ^ { n } u = \lambda ^ { n } u$ and therefore $\| A ^ { n } \| \ge | \lambda | ^ { n }$ , which does not converge to zero. Given $( i i )$ , it is not possible that the conditions of $( i i i )$ are not satisfied, because the minimal polynomial of any of the Jordan blocks, and therefore of $A$ itself, would have factors that contradict $( i i ) .$ If $( i i i )$ is true, then $S$ can be chosen to form $J$ , the Jordan canonical form of $A$ , with the off-diagonal elements chosen sufficiently small so that $\| J \| _ { \infty } < 1$ . Finally, if $( i v )$ is true then $A ^ { n } = S ( S ^ { - 1 } A S ) ^ { n } S ^ { - 1 }$ so that $\| A ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot \| S ^ { - 1 } A S \| ^ { n } \to 0$ . $\boxed { \begin{array} { r l } \end{array} }$

While the two results we have presented here are related to the convergence of difference equation solutions, the next is introduced only because of its application in later chapters.

Theorem 142E If $A$ is a stable $m \times m$ matrix and $B$ an arbitrary $m \times m$ matrix, then there exists a real $C$ such that

$$
\left\| \left( A + { \frac { 1 } { n } } B \right) ^ { n } \right\| \leq C ,
$$

for $n = 1 , 2 , \ldots .$

Proof. Without loss of generality, assume that $\| \cdot \|$ denotes the norm $\| \cdot \| _ { \infty }$ . Because $S$ exists so that $\| S ^ { - 1 } A S \| \leq 1$ , we have

$$
\begin{array} { r l } {  { \| ( A + \frac { 1 } { n } B ) ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot \| ( S ^ { - 1 } A S + \frac { 1 } { n } S ^ { - 1 } B S ) ^ { n } \| } } \\ & { \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot ( 1 + \frac { 1 } { n } \| S ^ { - 1 } B S \| ) ^ { n } } \\ & { \leq \| S \| \cdot \| S ^ { - 1 } \| \exp ( \| S ^ { - 1 } B S \| ) . } \end{array}
$$

In applying this result to sequences of vectors, the term represented by the matrix $B$ can be replaced by a non-linear function which satisfies suitable conditions. To widen the applicability of the result a non-homogeneous term is included.

Theorem 142F Let $A$ be a stable $m \times m$ matrix and $\phi ~ : ~ \mathbb { R } ^ { m } \ \to \ \mathbb { R } ^ { m }$ be such that $\| \phi ( x ) \| ~ \leq ~ L \| x \|$ , for $L$ a positive constant and $\boldsymbol { x } ~ \in ~ \mathbb { R } ^ { m }$ . If $w = ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } )$ and $v = ( v _ { 0 } , v _ { 1 } , \ldots , v _ { n } )$ are sequences related by

$$
v _ { i } = A v _ { i - 1 } + { \frac { 1 } { n } } \phi ( v _ { i - 1 } ) + w _ { i } , \quad i = 1 , 2 , \ldots , n ,
$$

then

$$
\left\| v _ { n } \right\| \leq C \left( \left\| v _ { 0 } \right\| + \sum _ { i = 1 } ^ { n } \left\| w _ { i } \right\| \right) ,
$$

where $C$ is independent of $n$ .

Proof. Let $S$ be the matrix introduced in the proof of Theorem 142C. From (142a), it follows that

$$
( S ^ { - 1 } v _ { i } ) = ( S ^ { - 1 } A S ) ( S ^ { - 1 } v _ { i - 1 } ) + \frac { 1 } { n } ( S ^ { - 1 } \phi ( v _ { i - 1 } ) ) + ( S ^ { - 1 } w _ { i } )
$$

and hence

$$
\| S ^ { - 1 } v _ { i } \| \leq \| S ^ { - 1 } A S \| \cdot \| S ^ { - 1 } v _ { i - 1 } \| + \frac { 1 } { n } \| S ^ { - 1 } \phi ( v _ { i - 1 } ) \| + \| S ^ { - 1 } w _ { i } \| ,
$$

leading to the bound

$$
\left\| v _ { n } \right\| \leq \left\| S \right\| \cdot \left\| S ^ { - 1 } \right\| \exp \left( L \| S \| \cdot \| S ^ { - 1 } \| \right) \left( \left\| v _ { 0 } \right\| + \sum _ { i = 1 } ^ { n } \| w _ { i } \| \right) .
$$

# Exercises 14

14.1 Find a constant $C$ such that $\| A ^ { n } \| _ { \infty } \leq C$ , for all $n = 0 , 1 , \ldots$ , where

$$
A = \left[ { \begin{array} { r r } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 4 } { 3 } } } \end{array} } \right] .
$$

14.2 For what values of the complex number $\theta$ is the matrix $A$ stable, where

$$
A = { \left[ \begin{array} { l l } { \theta } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } .
$$


<!-- chunk 0002: pages 71-140 -->
