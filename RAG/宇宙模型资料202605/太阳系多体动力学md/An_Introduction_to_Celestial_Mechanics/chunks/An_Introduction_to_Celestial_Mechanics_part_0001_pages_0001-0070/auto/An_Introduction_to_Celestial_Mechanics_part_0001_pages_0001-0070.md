# An Introduction to Celestial Mechanics

Richard Fitzpatrick

# Professor of Physics The University of Texas at Austin

# Contents

1 Introduction 5

# 2 Newtonian Mechanics 7

2.1 Introduction 7   
2.2 Newton’s Laws of Motion . 8   
2.3 Newton’s First Law of Motion 8   
2.4 Newton’s Second Law of Motion 11   
2.5 Newton’s Third Law of Motion 13   
2.6 Non-Isolated Systems . 16   
2.7 Motion in a One-Dimensional Potential 17   
2.8 Simple Harmonic Motion 20   
2.9 Two-Body Problem 22   
2.10 Exercises 23

# 3 Newtonian Gravity 25

3.1 Introduction . 25   
3.2 Gravitational Potential 25   
3.3 Gravitational Potential Energy 27   
3.4 Axially Symmetric Mass Distributions 28   
3.5 Potential Due to a Uniform Sphere . 31   
3.6 Potential Outside a Uniform Spheroid 32   
3.7 Potential Due to a Uniform Ring 35   
3.8 Exercises 35

# 4 Keplerian Orbits 37

4.1 Introduction . . 37   
4.2 Kepler’s Laws 37   
4.3 Conservation Laws 38   
4.4 Polar Coordinates 38   
4.5 Kepler’s Second Law . 40   
4.6 Kepler’s First Law . 41   
4.7 Kepler’s Third Law . 42   
4.8 Orbital Energies 43   
4.9 Kepler Problem 45   
4.10 Orbital Elements . 48   
4.11 Binary Star Systems 51   
4.12 Exercises 53

# 5 Orbits in Central Force-Fields 55

5.1 Introduction . . 55   
5.2 Motion in a General Central Force-Field 55   
5.3 Motion in a Nearly Circular Orbit 55   
5.4 Perihelion Precession of the Planets 58   
5.5 Perihelion Precession of Mercury 61   
5.6 Exercises . . 62

# 6 Rotating Reference Frames 65

6.1 Introduction 65   
6.2 Rotating Reference Frames 65   
6.3 Centrifugal Acceleration 66   
6.4 Coriolis Force 69   
6.5 Rotational Flattening of the Earth 71   
6.6 Tidal Elongation of the Earth . 74   
6.7 Tidal Torques 78   
6.8 Roche Radius 82   
6.9 Exercises . . 83

# 7 Lagrangian Mechanics 85

7.1 Introduction 85   
7.2 Generalized Coordinates 85   
7.3 Generalized Forces 86   
7.4 Lagrange’s Equation . 86   
7.5 Generalized Momenta . 89   
7.6 Exercises 90

# 8 Rigid Body Rotation 93

# 8.1 Introduction . 93

8.2 Fundamental Equations . 93   
8.3 Moment of Inertia Tensor 94   
8.4 Rotational Kinetic Energy 95   
8.5 Principal Axes of Rotation 96   
8.6 Euler’s Equations 97   
8.7 Eulerian Angles 99   
8.8 Free Precession of the Earth 102   
8.9 McCullough’s Formula 103   
8.10 Forced Precession and Nutation of the Earth 104   
8.11 Exercises 112

# 9 Three-Body Problem 115

9.1 Introduction 115   
9.2 Circular Restricted Three-Body Problem 115   
9.3 Jacobi Integral . . 116   
9.4 Tisserand Criterion 117   
9.5 Co-Rotating Frame 119   
9.6 Lagrange Points 121   
9.7 Zero-Velocity Surfaces . . 124   
9.8 Stability of Lagrange Points . 127

# 10 Lunar Motion 133

# 10.1 Historical Background . . 133

10.2 Preliminary Analysis . 134   
10.3 Lunar Equations of Motion 135   
10.4 Unperturbed Lunar Motion 138   
10.5 Perturbed Lunar Motion 139   
10.6 Description of Lunar Motion 144

# 11 Orbital Perturbation Theory 149

11.1 Introduction . . 149   
11.2 Disturbing Function . . 149   
11.3 Osculating Orbital Elements 150   
11.4 Lagrange Brackets . 153   
11.5 Transformation of Lagrange Brackets 154   
11.6 Lagrange’s Planetary Equations 158   
11.7 Transformation of Lagrange’s Equations . 160   
11.8 Expansion of Lagrange’s Equations . 161   
11.9 Expansion of Disturbing Function 164   
11.10 Secular Evolution of Planetary Orbits 172   
11.11 Hirayama Families . 179

# A Vector Algebra and Vector Calculus 185

A.1 Introduction 185   
A.2 Scalars and Vectors 185   
A.3 Vector Algebra 186   
A.4 Cartesian Components of a Vector 187   
A.5 Coordinate Transformations 188   
A.6 Scalar Product . 190   
A.7 Vector Product . . 192   
A.8 Rotation 194   
A.9 Scalar Triple Product 196   
A.10 Vector Triple Product 197   
A.11 Vector Calculus 198   
A.12 Line Integrals 198   
A.13 Vector Line Integrals 201   
A.14 Volume Integrals 202   
A.15 Gradient 203   
A.16 Grad Operator . 206   
A.17 Curvilinear Coordinates 207   
A.18 Exercises . 208

# B Useful Mathematrics 211

B.1 Conic Sections 211   
B.2 Matrix Eigenvalue Theory 214

# 1 Introduction

The aim of this book is to bridge the considerable gap between standard undergraduate treatments of celestial mechanics, which rarely advance much beyond two-body orbit theory, and full-blown graduate treatments, such as that by Murray & Dermott. The material presented here is intended to be intelligible to advanced undergraduate and beginning graduate students. A knowledge of elementary Newtonian mechanics is assumed. However, those non-elementary topics in mechanics that are needed to account for the motions of celestial bodies (e.g., gravitational potential theory, motion in rotating reference frames, Lagrangian mechanics, Eulerian rigid body rotation theory) are derived in the text. This is entirely appropriate, since these many of these topics were originally developed in order to investigate specific problems in celestial mechanics (often, the very problems that they are used to examine in this book.) It is taken for granted that readers are familiar with the fundamentals of integral and differential calculus, ordinary differential equations, and linear algebra. On the other hand, vector analysis plays such a central role in the study of celestial motion that a brief, but fairly comprehensive, review of this subject area is provided in Appendix A.

Celestial mechanics is the branch of astronomy that is concerned with the motions of celestial objects—in particular, the objects that make up the Solar System. The main aim of celestial mechanics is to reconcile these motions with the predictions of Newtonian mechanics. Modern analytic celestial mechanics started in 1687 with the publication of the Principia by Isaac Newton (1643–1727), and was subsequently developed into a mature science by celebrated scientists such as Euler (1707–1783), Clairaut (1713–1765), D’Alembert (1717–1783), Lagrange (1736–1813), Laplace (1749–1827), and Gauss (1777– 1855). This book is largely devoted to the study of the “classical” problems of celestial mechanics that were investigated by these scientists. These problems include the figure of the Earth, the tidal interaction between the Earth and the Moon, the free and forced precession and nutation of the Earth, the three-body problem, the orbit of the Moon, and the effect of interplanetary gravitational interactions on planetary orbits. This book does not discuss positional astronomy: i.e., the branch of astronomy that is concerned with finding the positions of celestial objects in the Earth’s sky at a particular instance in time. Nor does this book discuss the relatively modern (but extremely complicated) developments in celestial mechanics engendered by the advent of cheap fast computers, as well as data from unmanned space probes: e.g., the resonant interaction of planetary moons, chaotic motion, the dynamics of planetary rings. Interested readers are directed to the book by Murray & Dermott.

The major sources for the material appearing in this book are as follows:

An Elementary Treatise on the Lunar Theory, H. Godfray (Macmillan, London UK, 1853).

An Introductory Treatise on the Lunar Theory, E.W. Brown (Cambridge University Press, Cambridge UK, 1896).

Lectures on the Lunar Theory, J.C. Adams (Cambridge University Press, Cambridge UK, 1900).

An Introduction to Celestial Mechanics, F.R. Moulton, 2nd Revised Edition (Macmillan, New York NY, 1914).

Dynamics, H. Lamb, 2nd Edition (Cambridge University Press, Cambridge UK, 1923).

Celestial Mechanics, W.M. Smart (Longmans, London UK, 1953).

An Introductory Treatise on Dynamical Astronomy, H.C. Plummer (Dover, New York NY, 1960).

Methods of Celestial Mechanics, D. Brouwer, and G.M. Clemence (Academic Press, New York NY, 1961).

Celestial Mechanics: Volume II, Part 1: Perturbation Theory, Y. Hagihara (MIT Press, Cambridge MA, 1971).

Analytical Mechanics, G.R. Fowles (Holt, Rinehart, and Winston, New York NY, 1977).

Orbital Motion, A.E. Roy (Wiley, New York NY, 1978).

Solar System Dynamics, C.D. Murray, and S.F. Dermott (Cambridge University Press, Cambridge UK, 1999).

Classical Mechanics, 3rd Edition, H. Goldstein, C. Poole, and J. Safko (Addison-Wesley, San Fransisco CA, 2002).

Classical Dynamics of Particles and Systems, 5th Edition, S.T. Thornton, and J.B. Marion (Brooks/Cole—Thomson Learning, Belmont CA, 2004).

Analytical Mechanics, 7th Edition, G.R. Fowles, and G.L. Cassiday (Brooks/Cole—Thomson Learning, Belmont CA, 2005).

Astronomical Algorithms, J. Meeus, 2nd Edition (Willmann-Bell, Richmond VA, 2005).

# 2 Newtonian Mechanics

# 2.1 Introduction

Newtonian mechanics is a mathematical model whose purpose is to account for the motions of the various objects in the Universe. The general principles of this model were first enunciated by Sir Isaac Newton in a work entitled Philosophiae Naturalis Principia Mathematica (Mathematical Principles of Natural Philosophy). This work, which was published in 1687, is nowadays more commonly referred to as the Principa.1

Up until the beginning of the 20th century, Newtonian mechanics was thought to constitute a complete description of all types of motion occurring in the Universe. We now know that this is not the case. The modern view is that Newton’s model is only an approximation which is valid under certain circumstances. The model breaks down when the velocities of the objects under investigation approach the speed of light in vacuum, and must be modified in accordance with Einstein’s special theory of relativity. The model also fails in regions of space which are sufficiently curved that the propositions of Euclidean geometry do not hold to a good approximation, and must be augmented by Einstein’s general theory of relativity. Finally, the model breaks down on atomic and subatomic length-scales, and must be replaced by quantum mechanics. In this book, we shall neglect relativistic and quantum effects altogether. It follows that we must restrict our investigations to the motions of large (compared to an atom) slow (compared to the speed of light) objects moving in Euclidean space. Fortunately, virtually all of the motions encountered in celestial mechanics fall into this category.

Newton very deliberately modeled his approach in the Principia on that taken in Euclid’s Elements. Indeed, Newton’s theory of motion has much in common with a conventional axiomatic system such as Euclidean geometry. Like all axiomatic systems, Newtonian mechanics starts from a set of terms that are undefined within the system. In this case, the fundamental terms are mass, position, time, and force. It is taken for granted that we understand what these terms mean, and, furthermore, that they correspond to measurable quantities which can be ascribed to, or associated with, objects in the world around us. In particular, it is assumed that the ideas of position in space, distance in space, and position as a function of time in space, are correctly described by the Euclidean vector algebra and vector calculus discussed in Appendix A. The next component of an axiomatic system is a set of axioms. These are a set of unproven propositions, involving the undefined terms, from which all other propositions in the system can be derived via logic and mathematical analysis. In the present case, the axioms are called Newton’s laws of motion, and can only be justified via experimental observation. Note, incidentally, that Newton’s laws, in their primitive form, are only applicable to point objects (i.e., objects of negligible spatial extent). However, these laws can be applied to extended objects by treating them as collections of point objects.

One difference between an axiomatic system and a physical theory is that, in the latter case, even if a given prediction has been shown to follow necessarily from the axioms of the theory, it is still incumbent upon us to test the prediction against experimental observations. Lack of agreement might indicate faulty experimental data, faulty application of the theory (for instance, in the case of Newtonian mechanics, there might be forces at work which we have not identified), or, as a last resort, incorrectness of the theory. Fortunately, Newtonian mechanics has been found to give predictions that are in excellent agreement with experimental observations in all situations in which it would be expected to hold.

In the following, it is assumed that we know how to set up a rigid Cartesian frame of reference, and how to measure the positions of point objects as functions of time within that frame. It is also taken for granted that we have some basic familiarity with the laws of mechanics, and with standard mathematics up to, and including, calculus, as well as the vector analysis outlined in Appendix A.

# 2.2 Newton’s Laws of Motion

Newton’s laws of motion, in the rather obscure language of the Principia, take the following form:

1. Every body continues in its state of rest, or uniform motion in a straight-line, unless compelled to change that state by forces impressed upon it.   
2. The change of motion (i.e., momentum) of an object is proportional to the force impressed upon it, and is made in the direction of the straight-line in which the force is impressed.   
3. To every action there is always opposed an equal reaction; or, the mutual actions of two bodies upon each other are always equal and directed to contrary parts.

Let us now examine how these laws can be applied to a system of point objects.

# 2.3 Newton’s First Law of Motion

Newton’s first law of motion essentially states that a point object subject to zero net external force moves in a straight-line with a constant speed (i.e., it does not accelerate). However, this is only true in special frames of reference called inertial frames. Indeed, we can think of Newton’s first law as the definition of an inertial frame: i.e., an inertial frame of reference is one in which a point object subject to zero net external force moves in a straight-line with constant speed.

![](images/c8c414158c9ff4864612fb64eb624413afd375225a23ab04ee487c1601708ebb.jpg)  
Figure 2.1: A Galilean coordinate transformation.

Suppose that we have found an inertial frame of reference. Let us set up a Cartesian coordinate system in this frame. The motion of a point object can now be specified by giving its position vector, $\mathbf { r } \equiv ( { \boldsymbol { x } } , { \boldsymbol { y } } , z )$ , with respect to the origin of the coordinate system, as a function of time, t. Consider a second frame of reference moving with some constant velocity u with respect to the first frame. Without loss of generality, we can suppose that the Cartesian axes in the second frame are parallel to the corresponding axes in the first frame, that $\mathbf { u } \equiv ( \mathfrak { u } , 0 , 0 )$ , and, finally, that the origins of the two frames instantaneously coincide at $\mathrm {  ~ t ~ } = 0 \mathrm {  ~ \Omega ~ }$ —see Figure 2.1. Suppose that the position vector of our point object is $\mathbf { r } ^ { \prime } \equiv ( \mathrm { x } ^ { \prime } , \mathrm { y } ^ { \prime } , z ^ { \prime } )$ in the second frame of reference. It is evident, from Figure 2.1, that at any given time, t, the coordinates of the object in the two reference frames satisfy

$$
\begin{array} { l } { { { \sf x } ^ { \prime } = { \sf x } - { \sf u } { \sf t } , } } \\ { { { \sf y } ^ { \prime } = { \sf y } , } } \\ { { { \sf z } ^ { \prime } = { \sf z } . } } \end{array}
$$

This coordinate transformation was first discovered by Galileo Galilei, and is known as a Galilean transformation in his honor.

By definition, the instantaneous velocity of the object in our first reference frame is given by $\mathbf v = \mathrm { d } \mathbf r / \mathrm { d t } \equiv ( \mathrm { d } \mathbf x / \mathrm { d t } , \mathrm { d } \mathbf y / \mathrm { d t } , \mathrm { d } z / \mathrm { d t } )$ , with an analogous expression for the velocity, $\mathbf { v } ^ { \prime }$ , in the second frame. It follows from differentiation of Equations (2.1)–(2.3) with respect to time that the velocity components in the two frames satisfy

$$
\begin{array} { r c l } { { \displaystyle \vphantom { \bigg ( } \nu _ { x } ^ { \prime } } } & { { = } } & { { \nu _ { x } - \mathrm { u } , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \vphantom { \bigg ( } \nu _ { y } ^ { \prime } } } & { { = } } & { { \nu _ { y } , } } \\ { { } } & { { } } & { { \displaystyle \vphantom { \bigg ( } \nu _ { z } ^ { \prime } } } & { { = } } & { { \nu _ { z } . } } \end{array}
$$

These equations can be written more succinctly as

$$
\mathbf { v } ^ { \prime } = \mathbf { v } - \mathbf { u } .
$$

Finally, by definition, the instantaneous acceleration of the object in our first reference frame is given by $\mathbf { a } = \mathrm { d } \mathbf { v } / \mathrm { d t } \equiv ( \mathrm { d } \nu _ { x } / \mathrm { d t } , \mathrm { d } \nu _ { \mathrm { y } } / \mathrm { d t } , \mathrm { d } \nu _ { z } / \mathrm { d t } ) _ { \mathrm { \Omega } }$ , with an analogous expression for the acceleration, $\mathbf { a } ^ { \prime }$ , in the second frame. It follows from differentiation of Equations (2.4)– (2.6) with respect to time that the acceleration components in the two frames satisfy

$$
\begin{array} { r l r } { { \bf a } _ { x } ^ { \prime } } & { = } & { { \bf a } _ { x } , } \\ { { \bf a } _ { y } ^ { \prime } } & { = } & { { \bf a } _ { y } , } \\ { { \bf a } _ { z } ^ { \prime } } & { = } & { { \bf a } _ { z } . } \end{array}
$$

These equations can be written more succinctly as

$$
\mathbf { a } ^ { \prime } = \mathbf { a } .
$$

According to Equations (2.7) and (2.11), if an object is moving in a straight-line with constant speed in our original inertial frame (i.e., if $\mathbf { a } = \mathbf { 0 } .$ ) then it also moves in a (different) straight-line with (a different) constant speed in the second frame of reference (i.e., $\mathbf { a } ^ { \prime } = \mathbf { 0 } .$ ). Hence, we conclude that the second frame of reference is also an inertial frame.

A simple extension of the above argument allows us to conclude that there are an infinite number of different inertial frames moving with constant velocities with respect to one another. Newton throught that one of these inertial frames was special, and defined an absolute standard of rest: i.e., a static object in this frame was in a state of absolute rest. However, Einstein showed that this is not the case. In fact, there is no absolute standard of rest: i.e., all motion is relative—hence, the name “relativity” for Einstein’s theory. Consequently, one inertial frame is just as good as another as far as Newtonian mechanics is concerned.

But, what happens if the second frame of reference accelerates with respect to the first? In this case, it is not hard to see that Equation (2.11) generalizes to

$$
\mathbf { a } ^ { \prime } = \mathbf { a } - { \frac { \mathrm { d } \mathbf { u } } { \mathrm { d t } } } ,
$$

where $\mathbf { u ( t ) }$ is the instantaneous velocity of the second frame with respect to the first. According to the above formula, if an object is moving in a straight-line with constant speed in the first frame (i.e., if $\mathbf { a } = \mathbf { 0 } .$ ) then it does not move in a straight-line with constant speed in the second frame (i.e., $\mathbf { a } ^ { \prime } \neq \mathbf { 0 } .$ ). Hence, if the first frame is an inertial frame then the second is not.

A simple extension of the above argument allows us to conclude that any frame of reference which accelerates with respect to a given inertial frame is not itself an inertial frame.

For most practical purposes, when studying the motions of objects close to the Earth’s surface, a reference frame that is fixed with respect to this surface is approximately inertial. However, if the trajectory of a projectile within such a frame is measured to high precision then it will be found to deviate slightly from the predictions of Newtonian mechanics—see Chapter 6. This deviation is due to the fact that the Earth is rotating, and its surface is therefore accelerating towards its axis of rotation. When studying the motions of objects in orbit around the Earth, a reference frame whose origin is the center of the Earth, and whose coordinate axes are fixed with respect to distant stars, is approximately inertial. However, if such orbits are measured to extremely high precision then they will again be found to deviate very slightly from the predictions of Newtonian mechanics. In this case, the deviation is due to the Earth’s orbital motion about the Sun. When studying the orbits of the planets in the Solar System, a reference frame whose origin is the center of the Sun, and whose coordinate axes are fixed with respect to distant stars, is approximately inertial. In this case, any deviations of the orbits from the predictions of Newtonian mechanics due to the orbital motion of the Sun about the galactic center are far too small to be measurable. It should be noted that it is impossible to identify an absolute inertial frame—the best approximation to such a frame would be one in which the cosmic microwave background appears to be (approximately) isotropic. However, for a given dynamical problem, it is always possible to identify an approximate inertial frame. Furthermore, any deviations of such a frame from a true inertial frame can be incorporated into the framework of Newtonian mechanics via the introduction of so-called fictitious forces—see Chapter 6.

# 2.4 Newton’s Second Law of Motion

Newton’s second law of motion essentially states that if a point object is subject to an external force, f, then its equation of motion is given by

$$
\frac { \mathrm { d } \mathbf { p } } { \mathrm { d t } } = \mathbf { f } ,
$$

where the momentum, p, is the product of the object’s inertial mass, m, and its velocity, v. If m is not a function of time then the above expression reduces to the familiar equation

$$
\mathrm { m } { \frac { \mathrm { d } \mathbf { v } } { \mathrm { d t } } } = \mathbf { f } .
$$

Note that this equation is only valid in a inertial frame. Clearly, the inertial mass of an object measures its reluctance to deviate from its preferred state of uniform motion in a straight-line (in an inertial frame). Of course, the above equation of motion can only be solved if we have an independent expression for the force, f (i.e., a law of force). Let us suppose that this is the case.

An important corollary of Newton’s second law is that force is a vector quantity. This must be the case, since the law equates force to the product of a scalar (mass) and a vector (acceleration). Note that acceleration is obviously a vector because it is directly related to displacement, which is the prototype of all vectors—see Appendix A. One consequence of force being a vector is that two forces, $\mathbf { f } _ { 1 }$ and $\mathbf { f } _ { 2 }$ , both acting at a given point, have the same effect as a single force, $\mathbf { f } = \mathbf { f } _ { 1 } + \mathbf { f } _ { 2 }$ , acting at the same point, where the summation is performed according to the laws of vector addition—see Appendix A. Likewise, a single force, f, acting at a given point, has the same effect as two forces, $\mathbf { f } _ { 1 }$ and $\mathbf { f } _ { 2 }$ , acting at the same point, provided that $\mathbf { f } _ { 1 } + \mathbf { f } _ { 2 } = \mathbf { f }$ . This method of combining and splitting forces is known as the resolution of forces, and lies at the heart of many calculations in Newtonian mechanics.

Taking the scalar product of Equation (2.14) with the velocity, $\mathbf { v }$ , we obtain

$$
\mathfrak { m } \mathbf { v } \cdot \frac { \mathrm { d } \mathbf { v } } { \mathrm { d t } } = \frac { \mathfrak { m } } { 2 } \frac { \mathrm { d } ( \mathbf { v } \cdot \mathbf { v } ) } { \mathrm { d t } } = \frac { \mathfrak { m } } { 2 } \frac { \mathrm { d } \nu ^ { 2 } } { \mathrm { d t } } = \mathbf { f } \cdot \mathbf { v } .
$$

This can be written

$$
{ \frac { \mathrm { d } { \mathsf { K } } } { \mathrm { d t } } } = { \mathsf { f } } \cdot { \mathsf { v } } .
$$

where

$$
\mathsf { K } = \frac { 1 } { 2 } \mathsf { m } \nu ^ { 2 } .
$$

The right-hand side of Equation (2.16) represents the rate at which the force does work on the object (see Section A.6): i.e., the rate at which the force transfers energy to the object. The quantity K represents the energy that the object possesses by virtue of its motion. This type of energy is generally known as kinetic energy. Thus, Equation (2.16) states that any work done on point object by an external force goes to increase the object’s kinetic energy.

Suppose that, under the action of the force, f, our object moves from point $\mathsf { P }$ at time t1 to point $\mathrm { Q }$ at time $\mathrm { t } _ { 2 }$ . The net change in the object’s kinetic energy is obtained by integrating Equation (2.16):

$$
\Delta \mathsf { K } = \int _ { \mathrm { t } _ { 1 } } ^ { \mathrm { t } _ { 2 } } \mathbf { f } \cdot \mathbf { v } \mathrm { d t } = \int _ { \mathrm { p } } ^ { \mathrm { Q } } \mathbf { f } \cdot \mathrm { d } \mathbf { r } ,
$$

since $\mathbf { v } = \mathrm { d } \mathbf { r } / \mathrm { d t }$ . Here, dr is an element of the object’s path between points $\mathsf { P }$ and $\mathrm { Q }$ , and the integral in r represents the net work done by the force as the object moves along the path from $\mathsf { P }$ to Q.

As described in Section A.15, there are basically two kinds of forces in nature. Firstly, those for which line integrals of the type $\int _ { \mathsf { P } } ^ { \mathrm { Q } } \mathbf { f } \cdot \mathbf { \partial }$ dr depend on the end points, but not on the path taken between these points. Secondly, those for which line integrals of the type $\int _ { \mathsf { P } } ^ { \mathrm { Q } } \dot { \mathbf { f } } .$ dr depend both on the end points, and the path taken between these points. The first kind of force is termed conservative, whereas the second kind is termed non-conservative. It is also demonstrated in Section A.15 that if the line integral $\int _ { \mathsf { P } } ^ { \mathrm { Q } } \mathbf { f } \cdot \mathbf { \partial }$ · dr is path independent then the force f can always be written as the gradient of a scalar field. In other words, all conservative forces satisfy

$$
\mathbf { f } ( { \mathbf { r } } ) = - \nabla \mathsf { U } ,
$$

for some scalar field $\mathrm { U } ( \mathbf { r } )$ . Note that

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \nabla \mathsf { U } \cdot \mathrm { d } \mathbf { r } \equiv \Delta \mathsf { U } = \mathsf { U } ( \mathsf { Q } ) - \mathsf { U } ( \mathsf { P } ) ,
$$

irrespective of the path taken between $\mathsf { P }$ and Q. Hence, it follows from Equation (2.18) that

$$
\Delta \mathsf { K } = - \Delta \mathsf { U }
$$

for conservative forces. Another way of writing this is

$$
\mathsf { E } = \mathsf { K } + \mathsf { U } = \mathsf { c o n s t a n t } .
$$

Of course, we recognize this as an energy conservation equation: E is the object’s total energy, which is conserved; K is the energy the object has by virtue of its motion, otherwise know as its kinetic energy; and U is the energy the object has by virtue of its position, otherwise known as its potential energy. Note, however, that we can only write such energy conservation equations for conservative forces. Gravity is an obvious example of a conservative force. Non-conservative forces, on the other hand, do not conserve energy. In general, this is because of some sort of frictional energy loss. Note that potential energy is undefined to an arbitrary additive constant. In fact, it is only the difference in potential energy between different points in space that is well-defined.

# 2.5 Newton’s Third Law of Motion

Consider a system of $\mathsf { N }$ mutually interacting point objects. Let the ith object, whose mass is $\mathfrak { m } _ { \mathrm { i } }$ , be located at vector displacement $\mathbf { r } _ { \mathrm { i } }$ . Suppose that this object exerts a force $\mathbf { f } _ { \mathrm { j i } }$ on the jth object. Likewise, suppose that the jth object exerts a force $\mathbf { f } _ { \mathrm { i j } }$ on the ith object. Newton’s third law of motion essentially states that these two forces are equal and opposite, irrespective of their nature. In other words,

$$
\mathbf { f } _ { \mathrm { i j } } = - \mathbf { f } _ { \mathrm { j i } } .
$$

One corollary of Newton’s third law is that an object cannot exert a force on itself. Another corollary is that all forces in the Universe have corresponding reactions. The only exceptions to this rule are the fictitious forces which arise in non-inertial reference frames (e.g., the centrifugal and Coriolis forces which appear in rotating reference frames—see Chapter 6). Fictitious forces do not possess reactions.

It should be noted that Newton’s third law implies action at a distance. In other words, if the force that object i exerts on object j suddenly changes then Newton’s third law demands that there must be an immediate change in the force that object j exerts on object i. Moreover, this must be true irrespective of the distance between the two objects. However, we now know that Einstein’s theory of relativity forbids information from traveling through the Universe faster than the velocity of light in vacuum. Hence, action at a distance is also forbidden. In other words, if the force that object i exerts on object j suddenly changes then there must be a time delay, which is at least as long as it takes a light ray to propagate between the two objects, before the force that object j exerts on object i can respond. Of course, this means that Newton’s third law is not, strictly speaking, correct. However, as long as we restrict our investigations to the motions of dynamical systems on time-scales that are long compared to the time required for light-rays to traverse these systems, Newton’s third law can be regarded as being approximately correct.

In an inertial frame, Newton’s second law of motion applied to the ith object yields

$$
\mathfrak { m } _ { \mathrm { i } } \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } = \sum _ { \mathrm { j = 1 , N } } ^ { \mathrm { j } \ne \mathrm { i } } \mathbf { f } _ { \mathrm { i j } } .
$$

Note that the summation on the right-hand side of the above equation excludes the case $\mathrm { j } = \mathrm { i }$ , since the ith object cannot exert a force on itself. Let us now take the above equation and sum it over all objects. We obtain

$$
\sum _ { \mathrm { i = 1 , N } } { \mathfrak { m } } _ { \mathrm { i } } { \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } } = \sum _ { \mathrm { i , j = 1 , N } } ^ { \mathrm { j } \ne \mathrm { i } } \mathbf { f } _ { \mathrm { i j } } .
$$

Consider the sum over forces on the right-hand side of the above equation. Each element of this sum—fij, say—can be paired with another element— $\mathbf { f } _ { \mathrm { j i } }$ , in this case—which is equal and opposite, according to Newton’s third law. In other words, the elements of the sum all cancel out in pairs. Thus, the net value of the sum is zero. It follows that the above equation can be written

$$
M \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { c m } } } { \mathrm { d t } ^ { 2 } } = \mathbf { 0 } ,
$$

where $\begin{array} { r } { M = \sum _ { \mathrm { i } = 1 } ^ { \mathsf { N } } \mathsf { m } _ { \mathrm { i } } } \end{array}$ is the total mass. The quantity $\mathbf { r } _ { \mathrm { c m } }$ is the vector displacement of the center of mass of the system, which is an imaginary point whose coordinates are the mass weighted averages of the coordinates of the objects that constitute the system: i.e.,

$$
\mathbf { r } _ { \mathrm { c m } } = { \frac { \sum _ { i = 1 } ^ { \mathsf { N } } { \mathsf { m } } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } } { \sum _ { i = 1 } ^ { \mathsf { N } } { \mathsf { m } } _ { \mathrm { i } } } } .
$$

According to Equation (2.26), the center of mass of the system moves in a uniform straightline, in accordance with Newton’s first law of motion, irrespective of the nature of the forces acting between the various components of the system.

Now, if the center of mass moves in a uniform straight-line then the center of mass velocity,

$$
\frac { \mathrm { { d } \mathbf { r } _ { \mathrm { { c m } } } } } { \mathrm { { d t } } } = \frac { \sum _ { \mathrm { { i = 1 } } } ^ { \mathrm { { N } } } \mathsf { m } _ { \mathrm { { i } } } \mathrm { { d } \mathbf { r } _ { \mathrm { { i } } } / \mathrm { { d t } } } } { \sum _ { \mathrm { { i = 1 } } } ^ { \mathrm { { N } } } \mathsf { m } _ { \mathrm { { i } } } } ,
$$

is a constant of the motion. However, the momentum of the ith object takes the form $\pmb { \mathrm { p } } _ { \mathrm { i } } = \pmb { \mathrm { m } } _ { \mathrm { i } } \mathrm { d } \pmb { \mathrm { r } } _ { \mathrm { i } } / \mathrm { d } \pmb { \mathrm { t } }$ . Hence, the total momentum of the system is written

$$
\mathrm { \bf P } = \sum _ { \mathrm { i = 1 } } ^ { \mathrm { N } } \mathrm { m } _ { \mathrm { i } } \frac { \mathrm { d } { \bf r } _ { \mathrm { i } } } { \mathrm { d t } } .
$$

A comparison of Equations (2.28) and (2.29) suggests that $\mathbf { P }$ is also a constant of the motion. In other words, the total momentum of the system is a conserved quantity, irrespective

of the nature of the forces acting between the various components of the system. This result (which only holds if there is no net external force acting on the system) is a direct consequence of Newton’s third law of motion.

Taking the vector product of Equation (2.24) with the position vector $\mathbf { r } _ { \mathrm { { i } } } ,$ we obtain

$$
\mathfrak { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } = \sum _ { \mathrm { j } = 1 , \mathrm { N } } ^ { \mathrm { j } \ne \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times \mathbf { f } _ { \mathrm { i j } } .
$$

However, it is easily seen that

$$
\mathrm { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times { \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } } = { \frac { \mathrm { d } } { \mathrm { d t } } } \bigg ( \mathrm { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times { \frac { \mathrm { d } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } } } \bigg ) = { \frac { \mathrm { d } \mathbf { l } _ { \mathrm { i } } } { \mathrm { d t } } } ,
$$

where

$$
\mathbf { l } _ { \mathrm { i } } = \mathrm { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times { \frac { \mathrm { d } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } } }
$$

is the angular momentum of the ith particle about the origin of our coordinate system. The total angular momentum of the system (about the origin) takes the form

$$
\mathbf { L } = \sum _ { \mathrm { i = 1 , N } } \mathbf { l } _ { \mathrm { i } }
$$

Hence, summing Equation (2.30) over all particles, we obtain

$$
\frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } = \sum _ { \mathrm { i , j = 1 , N } } ^ { \mathrm { i } \neq \mathrm { j } } \mathbf { r } _ { \mathrm { i } } \times \mathbf { f } _ { \mathrm { i j } } .
$$

Consider the sum on the right-hand side of the above equation. A general term, $\mathbf { r } _ { \mathrm { { i } } } \times \mathbf { f } _ { \mathrm { { i } } { \mathrm { { j } } } }$ , in this sum can always be paired with a matching term, $\mathbf { r } _ { \mathrm { { j } } } \times \mathbf { f } _ { \mathrm { { j } \mathrm { { i } } } }$ , in which the indices have been swapped. Making use of Equation (2.23), the sum of a general matched pair can be written

$$
\mathbf { r } _ { \mathrm { { i } } } \times \mathbf { f } _ { \mathrm { { i } } { \mathrm { { j } } } } + \mathbf { r } _ { \mathrm { { j } } } \times \mathbf { f } _ { \mathrm { { j } } { \mathrm { { i } } } } = ( \mathbf { r } _ { \mathrm { { i } } } - \mathbf { r } _ { \mathrm { { j } } } ) \times \mathbf { f } _ { \mathrm { { i } } { \mathrm { { j } } } } .
$$

Let us assume that the forces acting between the various components of the system are central in nature, so that $\mathbf { f } _ { \mathrm { i j } }$ is parallel to $\mathbf { r } _ { \mathrm { { i } } } - \mathbf { r } _ { \mathrm { { j } } }$ . In other words, the force exerted on object j by object i either points directly toward, or directly away from, object i, and vice versa. This is a reasonable assumption, since virtually all of the forces that we encounter in celestial mechanics are of this type (e.g., gravity). It follows that if the forces are central then the vector product on the right-hand side of the above expression is zero. We conclude that

$$
\mathbf { r } _ { \mathrm { { i } } } \times \mathbf { f } _ { \mathrm { { i } { j } } } + \mathbf { r } _ { \mathrm { { j } } } \times \mathbf { f } _ { \mathrm { { j } { i } } } = \mathbf { 0 } ,
$$

for all values of i and j. Thus, the sum on the right-hand side of Equation (2.34) is zero for any kind of central force. We are left with

$$
\frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } = \mathbf { 0 } .
$$

In other words, the total angular momentum of the system is a conserved quantity, provided that the different components of the system interact via central forces (and there is no net external torque acting on the system).

# 2.6 Non-Isolated Systems

Up to now, we have only considered isolated dynamical systems, in which all of the forces acting on the system originate from within the system itself. Let us now generalize our approach to deal with non-isolated dynamical systems, in which some of the forces originate outside the system. Consider a system of $\mathsf { N }$ mutually interacting point objects. Let $\mathfrak { m } _ { \mathrm { i } }$ and $\mathbf { r } _ { \mathrm { i } }$ be the mass and position vector of the ith object, respectively. Suppose that the ith object is subject to two forces. First, an internal force which originates from the other objects in the system, and second an external force which originates outside the system. In other words, let the force acting on the ith object take the form

$$
\mathbf { f } _ { \mathrm { i } } = \sum _ { \mathrm { j = 1 , N } } ^ { \mathrm { j } \neq \mathrm { i } } \mathbf { f } _ { \mathrm { i j } } + \mathbf { F } _ { \mathrm { i } } ,
$$

where $\mathbf { f } _ { \mathrm { i j } }$ is the internal force exerted by object j on object $\mathfrak { i }$ , and $\mathbf { F } _ { \mathrm { i } }$ the net external force acting on object i.

The equation of motion of the ith object is

$$
\mathfrak { m } _ { \mathrm { i } } \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } = \mathbf { f } _ { \mathrm { i } } = \sum _ { \mathrm { j = 1 , N } } ^ { \mathrm { j } \ne \mathrm { i } } \mathbf { f } _ { \mathrm { i j } } + \mathbf { F } _ { \mathrm { i } } .
$$

Summing over all objects, we obtain

$$
\sum _ { \mathrm { i = 1 , N } } \mathrm { m _ { i } \frac { d ^ { 2 } \mathbf { r } _ { i } } { d t ^ { 2 } } = \sum _ { i , j = 1 , N } ^ { j \ne i } \mathbf { f } _ { \mathrm { i j } } + \sum _ { \mathrm { i = 1 , N } } \mathbf { F } _ { \mathrm { i } } , }
$$

which reduces to

$$
\frac { \mathrm { d } \mathbf { P } } { \mathrm { d t } } = \mathbf { F } ,
$$

where

$$
\mathbf { F } = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathbf { F } _ { \mathrm { i } }
$$

is the net external force acting on the system. Here, the sum over the internal forces has cancelled out in pairs due to Newton’s third law of motion (see Section 2.5). We conclude that if there is a net external force acting on the system then the total linear momentum evolves in time according to the simple equation (2.41), but is completely unaffected by any internal forces. The fact that Equation (2.41) is similar in form to Equation (2.13) suggests that the center of mass of a system consisting of many point objects has analogous dynamics to a single point object, whose mass is the total system mass, moving under the action of the net external force.

Taking $\mathbf { r } _ { \mathrm { { i } } } \times$ Equation (2.39), and summing over all objects, we obtain

$$
\frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } = \mathbf { T } ,
$$

where

$$
\mathbf { T } = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathbf { r } _ { \mathrm { i } } \times \mathbf { F } _ { \mathrm { i } }
$$

is the net external torque acting on the system. Here, the sum over the internal torques has cancelled out in pairs, assuming that the internal forces are central in nature (see Section 2.5). We conclude that if there is a net external torque acting on the system then the total angular momentum evolves in time according to the simple equation (2.43), but is completely unaffected by any internal torques.

# 2.7 Motion in a One-Dimensional Potential

As a simple illustration of the application of Newton’s laws of motion, consider a point particle of mass m moving in the $x$ -direction, say, under the action of some $x$ -directed force $\mathsf { f } ( { \boldsymbol { x } } )$ . Suppose that $\mathsf { f } ( { \boldsymbol { x } } )$ is a conservative force: e.g., gravity. In this case, according to Equation (2.19), we can write

$$
\mathsf { f } ( \boldsymbol { x } ) = - \frac { \mathrm { d } \mathsf { U } ( \boldsymbol { x } ) } { \mathrm { d } \boldsymbol { x } } ,
$$

where $\mathrm { U } ( { \boldsymbol { x } } )$ is the potential energy of the particle at position $x$

Let the curve $\mathrm { u } ( \boldsymbol { x } )$ take the form shown in Figure 2.2. For instance, this curve might represent the gravitational potential energy of a cyclist freewheeling in a hilly region. Observe that we have set the potential energy at infinity to zero (which we are generally free to do, since potential energy is undefined to an arbitrary additive constant). This is a fairly common convention. What can we deduce about the motion of the particle in this potential?

Well, we know that the total energy, E—which is the sum of the kinetic energy, $\mathsf { K }$ , and the potential energy, U—is a constant of the motion—see Equation (2.22). Hence, we can write

$$
\mathsf { K } ( \boldsymbol { x } ) = \mathsf { E } - \mathsf { U } ( \boldsymbol { x } ) .
$$

However, we also know that a kinetic energy can never be negative [since $\mathsf { K } = ( 1 / 2 ) \mathsf { m } \nu ^ { 2 }$ , and neither m nor $\nu ^ { 2 }$ can be negative]. Hence, the above expression tells us that the particle’s motion is restricted to the region (or regions) in which the potential energy curve $\mathrm { U } ( { \boldsymbol { x } } )$ falls below the value E. This idea is illustrated in Figure 2.2. Suppose that the total energy of the system is $\mathsf { E } _ { 0 }$ . It is clear, from the figure, that the particle is trapped inside one or other of the two dips in the potential—these dips are generally referred to as potential wells. Suppose that we now raise the energy to $\mathsf { E } _ { 1 }$ . In this case, the particle is free to enter or leave each of the potential wells, but its motion is still bounded to some extent, since it clearly cannot move off to infinity. Finally, let us raise the energy to $\mathsf { E } _ { 2 }$ . Now the particle is unbounded: i.e., it can move off to infinity. In conservative systems in which it makes sense to adopt the convention that the potential energy at infinity is zero, bounded systems are characterized by $\mathsf { E } < 0$ , whereas unbounded systems are characterized by $\mathsf { E } > 0$ .

![](images/f37c41c1007a20fcfbdc214ccb19bcbaaec79fc7bbef54b390c68c75ce21b79c.jpg)  
Figure 2.2: A potential energy curve.

The above discussion suggests that the motion of a particle moving in a potential generally becomes less bounded as the total energy E of the system increases. Conversely, we would expect the motion to become more bounded as E decreases. In fact, if the energy becomes sufficiently small then it appears likely that the system will settle down in some equilibrium state in which the particle remains stationary. Let us try to identify any prospective equilibrium states in Figure 2.2. If the particle remains stationary then it must be subject to zero force (otherwise it would accelerate). Hence, according to Equation (2.45), an equilibrium state is characterized by

$$
\frac { \mathrm { d } \mathrm { U } } { \mathrm { d } x } = 0 .
$$

In other words, a equilibrium state corresponds to either a maximum or a minimum of the potential energy curve $\mathrm { u } ( \boldsymbol { x } )$ . It can be seen that the $\mathrm { u } ( \boldsymbol { x } )$ curve shown in Figure 2.2 has three associated equilibrium states located at ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ , $x = x _ { 1 }$ , and ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 2 }$ .

Let us now make a distinction between stable equilibrium points and unstable equilibrium points. When the particle is slightly displaced from a stable equilibrium point then the resultant force acting on it must always be such as to return it to this point. In other words, if ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ is an equilibrium point then we require

$$
\left. \frac { \mathrm { d } \mathsf { f } } { \mathrm { d } \mathsf { x } } \right| _ { \mathsf { x } _ { 0 } } < 0
$$

for stability: i.e., if the particle is displaced to the right, so that $\mathbf { x } - \mathbf { x } _ { 0 } > 0$ , then the force

![](images/9c4d05b4edd273cbd6b309beb63214eefd5990b6bcf8dbd06c960f660e98ad87.jpg)  
Figure 2.3: Different types of equilibrium point.

must act to the left, so that $\mathsfit { f } < 0$ , and vice versa. Likewise, if

$$
\left. \frac { \mathrm { d } \mathsf { f } } { \mathrm { d } \mathsf { x } } \right| _ { \mathsf { x } _ { 0 } } > 0
$$

then the equilibrium point ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ is unstable. It follows, from Equation (2.45), that stable equilibrium points are characterized by

$$
\frac { \mathrm { d } ^ { 2 } \mathrm { U } } { \mathrm { d } x ^ { 2 } } > 0 .
$$

In other words, a stable equilibrium point corresponds to a minimum of the potential energy curve $\mathrm { u } ( \boldsymbol { x } )$ . Likewise, an unstable equilibrium point corresponds to a maximum of the $\mathrm { U } ( { \boldsymbol { x } } )$ curve. Hence, we conclude that, in Figure 2.2, $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { x } } _ { 0 }$ and ${ \boldsymbol { x } } = x _ { 2 }$ are stable equilibrium points, whereas ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 1 }$ is an unstable equilibrium point. Of course, this makes perfect sense if we think of $\mathrm { U } ( { \boldsymbol { x } } )$ as a gravitational potential energy curve, so that U is directly proportional to height. In this case, all we are saying is that it is easy to confine a low energy mass at the bottom of a smooth valley, but very difficult to balance the same mass on the top of a smooth hill (since any slight displacement of the mass will cause it to slide down the hill). Note, finally, that if

$$
{ \frac { { \mathrm { d } } \mathrm { U } } { { \mathrm { d } } x } } = { \frac { { \mathrm { d } } ^ { 2 } \mathrm { U } } { { \mathrm { d } } x ^ { 2 } } } = 0
$$

at any point (or in any region) then we have what is known as a neutral equilibrium point. We can move the particle slightly away from such a point and it will still remain in equilibrium (i.e., it will neither attempt to return to its initial state, nor will it continue to move). A neutral equilibrium point corresponds to a flat spot in a $\mathrm { u } ( \boldsymbol { x } )$ curve. See Figure 2.3.

The equation of motion of a particle moving in one dimension under the action of a conservative force is, in principle, integrable. Since $\mathsf { K } = ( 1 / 2 ) \mathsf { m } \nu ^ { 2 }$ , the energy conservation equation (2.46) can be rearranged to give

$$
\nu = \pm \left( \frac { 2 \left[ \mathsf { E } - \mathsf { U } ( \mathsf { x } ) \right] } { \mathsf { m } } \right) ^ { 1 / 2 } ,
$$

where the $\pm$ signs correspond to motion to the left and to the right, respectively. However, since $\nu = \mathrm { d } x / \mathrm { d t }$ , this expression can be integrated to give

$$
\mathrm { t } = \pm \left( \frac { \mathfrak { m } } { 2 \mathsf { E } } \right) ^ { 1 / 2 } \int _ { x _ { 0 } } ^ { x } \frac { \mathrm { d } x ^ { \prime } } { \sqrt { 1 - \mathsf { U } ( x ^ { \prime } ) / \mathsf { E } } } ,
$$

where ${ \boldsymbol { x } } ( { \mathrm { t } } = 0 ) = { \boldsymbol { x } } _ { 0 }$ . For sufficiently simple potential functions, $\mathrm { u } ( \boldsymbol { x } )$ , the above equation can be solved to give $x$ as a function of t. For instance, if $\mathsf { U } = ( 1 / 2 ) \mathsf { k } x ^ { 2 }$ , $x _ { 0 } = 0$ , and the plus sign is chosen, then

$$
\mathbf { t } = \left( \frac { \mathbf { m } } { \mathbf { k } } \right) ^ { 1 / 2 } \int _ { 0 } ^ { ( \mathbf { k } / 2 \operatorname { E } ) ^ { 1 / 2 } x } \frac { \mathrm { d } \mathsf { y } } { \sqrt { 1 - \mathsf { y } ^ { 2 } } } = \left( \frac { \mathbf { m } } { \mathbf { k } } \right) ^ { 1 / 2 } \sin ^ { - 1 } \left( \left[ \frac { \mathbf { k } } { 2 \operatorname { E } } \right] ^ { 1 / 2 } x \right) ,
$$

which can be inverted to give

$$
\begin{array} { r } { x = \mathrm { { a } } \sin ( \omega \mathrm { { t } } ) , } \end{array}
$$

where $\mathrm { a } = \sqrt { 2 \mathsf { E } / \mathsf { k } }$ and $\omega = \sqrt { \mathbf { k } / \mathsf { m } }$ . Note that the particle reverses direction each time it reaches one of the so-called turning points ( $\mathbf { \boldsymbol { x } } = \pm \mathbf { \boldsymbol { a } } ,$ ) at which $\mathsf { U } = \mathsf { E }$ (and, so ${ \sf K } = 0 $ ).

# 2.8 Simple Harmonic Motion

Consider the motion of a point particle of mass m, moving in one dimension, that is slightly displaced from a stable equilibrium point located at $\boldsymbol { x } = 0$ . Suppose that the particle is moving in the conservative force-field $\mathsf { f } ( { \boldsymbol { x } } )$ . According to the above analysis, in order for $x = 0$ to correspond to a stable equilibrium point we require both

$$
\mathsf { f } ( 0 ) = 0 ,
$$

and

$$
\frac { \mathrm { d } \mathsf { f } ( 0 ) } { \mathrm { d } x } < 0 .
$$

Now, our particle obeys Newton’s second law of motion,

$$
\mathfrak { m } \frac { \mathrm { d } ^ { 2 } x } { \mathrm { d t } ^ { 2 } } = \mathbf { f } ( x ) .
$$

Let us assume that the particle always stays fairly close to its equilibrium point. In this case, to a good approximation, we can represent $\mathsf { f } ( { \boldsymbol { x } } )$ via a truncated Taylor expansion about this point. In other words,

$$
\mathbf { \boldsymbol { \mathsf { f } } } ( \mathbf { \boldsymbol { x } } ) \simeq \mathbf { \boldsymbol { \mathsf { f } } } ( 0 ) + \frac { \mathrm { d } \mathbf { \boldsymbol { \mathsf { f } } } ( 0 ) } { \mathrm { d } \mathbf { \boldsymbol { x } } } \mathbf { \boldsymbol { x } } + \mathcal { O } ( \mathbf { \boldsymbol { x } } ^ { 2 } ) .
$$

However, according to (2.56) and (2.57), the above expression can be written

$$
\mathsf { f } ( \mathsf { x } ) \simeq - \mathsf { m } \omega _ { 0 } ^ { 2 } \ d { x } ,
$$

where $\mathrm { d } { \mathsf { f } } ( 0 ) / \mathrm { d } { \mathsf { x } } = - \mathsf { m } \omega _ { 0 } ^ { 2 }$ . Hence, we conclude that our particle satisfies the following approximate equation of motion,

$$
\frac { \mathrm { d } ^ { 2 } x } { \mathrm { d t } ^ { 2 } } + \omega _ { 0 } ^ { 2 } x \simeq 0 ,
$$

provided that it does not stray too far from its equilibrium point: i.e., provided $| x |$ does not become too large.

Equation (2.61) is called the simple harmonic equation, and governs the motion of all one-dimensional conservative systems which are slightly perturbed from some stable equilibrium state. The solution of Equation (2.61) is well-known:

$$
\begin{array} { r } { \boldsymbol { x } ( \mathbf { t } ) = \mathbf { a } \sin ( \omega _ { 0 } \mathbf { t } - \phi _ { 0 } ) . } \end{array}
$$

The pattern of motion described by above expression, which is called simple harmonic motion, is periodic in time, with repetition period $\mathsf { T } _ { 0 } = 2 \pi / \omega _ { 0 }$ , and oscillates between ${ \boldsymbol { x } } =$ $\pm \mathbf { a }$ . Here, a is called the amplitude of the motion. The parameter $\Phi _ { 0 }$ , known as the phase angle, simply shifts the pattern of motion backward and forward in time. Figure 2.4 shows some examples of simple harmonic motion. Here, $\Phi _ { 0 } = 0 , + \pi / 4$ , and $- \pi / 4$ correspond to the solid, short-dashed, and long-dashed curves, respectively.

Note that the frequency, $\omega _ { 0 }$ —and, hence, the period, ${ \sf T } _ { 0 }$ —of simple harmonic motion is determined by the parameters appearing in the simple harmonic equation, (2.61). However, the amplitude, a, and the phase angle, $\Phi _ { 0 }$ , are the two integration constants of this second-order ordinary differential equation, and are, thus, determined by the initial conditions: i.e., by the particle’s initial displacement and velocity.

Now, from Equations (2.45) and (2.60), the potential energy of our particle at position $x$ is approximately

$$
{ \sf U } ( { \sf x } ) \simeq \frac { 1 } { 2 } { \sf m } \omega _ { 0 } ^ { 2 } x ^ { 2 } .
$$

Hence, the total energy is written

$$
\mathsf { E } = \mathsf { K } + \mathsf { U } = \frac { 1 } { 2 } \mathsf { m } \left( \frac { \mathrm { d } \mathsf { x } } { \mathrm { d t } } \right) ^ { 2 } + \frac { 1 } { 2 } \mathsf { m } \omega _ { 0 } ^ { 2 } \ d { } \ d { } \mathrm { x } ^ { 2 } ,
$$

giving

$$
\mathsf { E } = \frac { 1 } { 2 } \mathsf { m } \omega _ { 0 } ^ { 2 } \mathsf { a } ^ { 2 } \cos ^ { 2 } ( \omega _ { 0 } \mathsf { t } - \phi _ { 0 } ) + \frac { 1 } { 2 } \mathsf { m } \omega _ { 0 } ^ { 2 } \mathsf { a } ^ { 2 } \sin ^ { 2 } ( \omega _ { 0 } \mathsf { t } - \phi _ { 0 } ) = \frac { 1 } { 2 } \mathsf { m } \omega _ { 0 } ^ { 2 } \mathsf { a } ^ { 2 } ,
$$

where use has been made of Equation (2.62), and the trigonometric identity $\cos ^ { 2 } \theta +$ $\sin ^ { 2 } \theta \ \equiv \ 1$ . Note that the total energy is constant in time, as is to be expected for a conservative system, and is proportional to the amplitude squared of the motion.

![](images/e49e252d2a928775005f6583a049c11aa0aa66638e34feeab8568a00dfc3bd54.jpg)  
Figure 2.4: Simple harmonic motion.

Consider the motion of a point particle of mass m which is slightly displaced from a unstable equilibrium point at $x = 0$ . The fact that the equilibrium is unstable implies that

$$
\mathsf { f } ( 0 ) = 0 ,
$$

and

$$
\frac { \mathrm { d } \mathsf { f } ( 0 ) } { \mathrm { d } x } > 0 .
$$

Now, as long as $| x |$ remains small, our particle’s equation of motion takes the approximate form

$$
\mathfrak { m } \frac { \mathrm { d } ^ { 2 } \mathfrak { x } } { \mathrm { d t } ^ { 2 } } \simeq \mathfrak { f } ( 0 ) + \frac { \mathrm { d } \mathfrak { f } ( 0 ) } { \mathrm { d } \mathfrak { x } } \mathfrak { x } ,
$$

which reduces to

$$
{ \frac { \mathrm { d } ^ { 2 } x } { \mathrm { d t } ^ { 2 } } } \simeq \mathrm { k } ^ { 2 } x ,
$$

where $\mathrm { d } \mathsf { f } ( 0 ) / \mathrm { d } \mathsf { x } = \mathsf { m } \mathsf { k } ^ { 2 }$ . The most general solution to the above equation is

$$
\begin{array} { r } { \boldsymbol { x } ( \mathbf { t } ) = \boldsymbol { A } \mathbf { e } ^ { \mathrm { \scriptsize { k t } } } + \boldsymbol { \mathrm { B } } \mathbf { e } ^ { - \mathrm { \boldsymbol { k } } \mathbf { t } } , } \end{array}
$$

where A and B are arbitrary constants. Thus, unless $\boldsymbol { A }$ is exactly zero, we conclude that the particle’s displacement from the unstable equilibrium point grows exponentially in time.

# 2.9 Two-Body Problem

An isolated dynamical system consisting of two freely moving point masses exerting forces on one another is conventionally termed a two-body problem. Suppose that the first object is of mass $\mathfrak { m } _ { 1 }$ , and is located at position vector $\mathbf { r } _ { 1 }$ . Likewise, the second object is of mass $\mathfrak { m } _ { 2 }$ , and is located at position vector $\mathbf { r } _ { 2 }$ . Let the first object exert a force $\mathbf { f } _ { 2 1 }$ on the second. By Newton’s third law, the second object exerts an equal and opposite force, $\mathbf { f } _ { 1 2 } = - \mathbf { f } _ { 2 1 }$ , on the first. Suppose that there are no other forces in the problem. The equations of motion of our two objects are thus

$$
\begin{array} { r c l } { { \displaystyle { \mathfrak { m } } _ { 1 } \frac { { \mathrm { d } } ^ { 2 } { \mathbf { r } } _ { 1 } } { { \mathrm { d t } } ^ { 2 } } } } & { { = } } & { { - \mathbf { f } , } } \\ { { \displaystyle { \mathfrak { m } } _ { 2 } \frac { { \mathrm { d } } ^ { 2 } { \mathbf { r } } _ { 2 } } { { \mathrm { d t } } ^ { 2 } } } } & { { = } } & { { \mathbf { f } , } } \end{array}
$$

where $\mathbf { f } = \mathbf { f } _ { 2 1 }$

Now, the center of mass of our system is located at

$$
\mathbf { r } _ { \mathrm { c m } } = { \frac { \mathsf { m } _ { 1 } \mathbf { r } _ { 1 } + \mathsf { m } _ { 2 } \mathbf { r } _ { 2 } } { \mathsf { m } _ { 1 } + \mathsf { m } _ { 2 } } } .
$$

Hence, we can write

$$
\begin{array} { r c l } { \mathbf { r } _ { 1 } } & { = } & { \mathbf { r } _ { \mathrm { c m } } - \cfrac { \mathbf { m } _ { 2 } } { \mathbf { m } _ { 1 } + \mathbf { m } _ { 2 } } \mathbf { r } , } \\ { \mathbf { r } _ { 2 } } & { = } & { \mathbf { r } _ { \mathrm { c m } } + \cfrac { \mathbf { m } _ { 1 } } { \mathbf { m } _ { 1 } + \mathbf { m } _ { 2 } } \mathbf { r } , } \end{array}
$$

where $\mathbf { r } = \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 }$ . Substituting the above two equations into Equations (2.71) and (2.72), and making use of the fact that the center of mass of an isolated system does not accelerate (see Section 2.5), we find that both equations yield

$$
\mu \frac { \mathrm { d } ^ { 2 } \mathbf { r } } { \mathrm { d t } ^ { 2 } } = \mathbf { f } ,
$$

where

$$
\mu = \frac { \mathsf { m } _ { 1 } \mathsf { m } _ { 2 } } { \mathsf { m } _ { 1 } + \mathsf { m } _ { 2 } }
$$

is called the reduced mass. Hence, we have effectively converted our original two-body problem into an equivalent one-body problem. In the equivalent problem, the force f is the same as that acting on both objects in the original problem (modulo a minus sign). However, the mass, µ, is different, and is less than either of $\mathfrak { m } _ { 1 }$ or $\mathfrak { m } _ { 2 }$ (which is why it is called the “reduced” mass). We conclude that the dynamics of an isolated system consisting of two interacting point objects can always be reduced to that of an equivalent system consisting of a single point object moving in a fixed potential.

# 2.10 Exercises

2.1. Consider a function of many variables $\mathsf { f } ( { \mathsf { x } } _ { 1 } , { \mathsf { x } } _ { 2 } , \cdots , { \mathsf { x } } _ { \mathrm { n } } )$ . Such a function which satisfies

$$
\mathsf { f } ( \mathtt { t } x _ { 1 } , \mathtt { t } x _ { 2 } , \cdot \cdot \cdot , \mathtt { t } x _ { \mathsf { n } } ) = \mathtt { t } ^ { \mathtt { a } } \mathtt { f } ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { \mathsf { n } } )
$$

for all $\mathrm { t } > 0$ , and all values of the ${ \mathrm { x } } _ { \mathrm { i } }$ , is termed a homogenous function of degree a. Prove the following theorem regarding homogeneous functions:

$$
\sum _ { \mathrm { i = 1 , n } } x _ { \mathrm { i } } { \frac { \partial { \mathsf { f } } } { \partial x _ { \mathrm { i } } } } = \mathbf { a } { \mathsf { f } }
$$

2.2. Consider an isolated system of $\mathsf { N }$ point objects interacting via attractive central forces. Let the mass and position vector of the ith object be $\mathfrak { m } _ { \mathrm { i } }$ and $\mathbf { r } _ { \mathrm { i } }$ , respectively. Suppose that magnitude of the force exerted on object $\mathrm { i }$ by object j is $\mathbf { k } _ { \mathrm { i } } \mathbf { k } _ { \mathrm { j } } | \mathbf { r } _ { \mathrm { i } } - \mathbf { r } _ { \mathrm { j } } | ^ { - \mathrm { n } }$ . Here, the $\boldsymbol { \kappa } _ { \mathrm { i } }$ measure some constant physical property of the particles (e.g., their electric charges). Write an expression for the total potential energy U of the system. Is this a homogenous function? If so, what is its degree? Write the equation of motion of the ith particle. Use the mathematical theorem from the previous exercise to demonstrate that

$$
\frac { 1 } { 2 } \frac { \mathrm { d } ^ { 2 } \mathrm { I } } { \mathrm { d t } ^ { 2 } } = 2 \mathsf { K } + ( \mathsf { n } - 1 ) \mathrm { U } ,
$$

where $\begin{array} { r } { \mathrm { ~ I ~ } = \ \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathsf { m } _ { \mathrm { i } } \mathsf { r } _ { \mathrm { i } } ^ { 2 } } \end{array}$ , and $\mathsf { K }$ is the kinetic energy. This result is known as the virial theorem. Demonstrate that there are no bound steady-state equilibria for the system (i.e., states in which the global system parameters do not evolve in time) when ${ \mathfrak { n } } \geq 3$ .

2.3. A particle of mass m is constrained to move in one dimension such that its instantaneous displacement is $x$ . The particle is released at rest from ${ \boldsymbol { x } } = { \boldsymbol { \mathrm { b } } }$ , and is subject to a force of the form $\mathsf { f } ( \mathsf { x } ) = - \mathsf { k } \mathsf { x } ^ { - 2 }$ . Show that the time required for the particle to reach the origin is

$$
\pi \left( \frac { \mathfrak { m } \mathfrak { b } ^ { 3 } } { 8 \mathfrak { k } } \right) ^ { 1 / 2 } .
$$

2.4. A body of uniform cross-sectional area $\boldsymbol { A }$ and mass density $\rho$ floats in a liquid of density $\rho _ { 0 }$ (where $\rho < \rho _ { 0 } )$ , and at equilibrium displaces a volume $\vee$ . Show that the period of small oscillations about the equilibrium position is

$$
{ \sf T } = 2 \pi \sqrt { \frac { \sf V } { { \sf g } { \sf A } } } .
$$

2.5. Using the notation of Section 2.9, show that the total momentum and angular momentum of a two-body system take the form

$$
{ \begin{array} { l l l } { \mathbf { P } } & { = } & { M \mathbf { r } _ { \mathrm { { c m } } } , } \\ { \mathbf { L } } & { = } & { M \mathbf { r } _ { \mathrm { { c m } } } \times { \dot { \mathbf { r } } } _ { \mathrm { { c m } } } + \mu \mathbf { r } \times { \dot { \mathbf { r } } } , } \end{array} }
$$

respectively, where $M = { \mathfrak { m } } _ { 1 } + { \mathfrak { m } } _ { 2 }$ .

# 3 Newtonian Gravity

# 3.1 Introduction

Classical gravity, which is invariably the dominant force in celestial dynamical systems, was first correctly described in Newton’s Principia. According to Newton, any two point objects exert a gravitational force of attraction on one another. This force points along the line joining the objects, is directly proportional to the product of their masses, and inversely proportional to the square of the distance between them. Consider two point objects of $\mathfrak { m a s s } \mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ that are located at position vectors $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ , respectively. The force $\mathbf { f } _ { 1 2 }$ that mass $\mathfrak { m } _ { 2 }$ exerts on mass $\mathfrak { m } _ { 1 }$ is written

$$
\mathbf { f } _ { 1 2 } = \mathsf { G m } _ { 1 } \mathsf { m } _ { 2 } \frac { \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } } { | \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } | ^ { 3 } } .
$$

The force $\mathbf { f } _ { 2 1 }$ that mass $\mathfrak { m } _ { 1 }$ exerts on mass $\mathfrak { m } _ { 2 }$ is equal and opposite: i.e., ${ \bf f } _ { 2 1 } = - { \bf f } _ { 1 2 }$ . Here, the constant of proportionality, $\sf G$ , is called the universal gravitational constant, and takes the value

$$
\mathrm { G } = 6 . 6 7 3 0 0 \times 1 0 ^ { - 1 1 } \mathrm { m } ^ { 3 } \mathrm { k g } ^ { - 1 } \mathrm { s } ^ { - 2 } .
$$

Incidentally, there is something rather curious about Equation (3.1). According to this law, the gravitational force acting on a given object is directly proportional to that object’s inertial mass. But why should inertia be related to the force of gravity? After all, inertia measures the reluctance of a given body to deviate from its preferred state of uniform motion in a straight-line, in response to some external force. What has this got to do with gravitational attraction? This question perplexed physicists for many years, and was only answered when Albert Einstein published his general theory of relativity in 1916. According to Einstein, inertial mass acts as a sort of gravitational charge since it impossible to distinguish an acceleration produced by a gravitational field from an apparent acceleration generated by observing in a non-inertial reference frame. The assumption that these two types of acceleration are indistinguishable leads directly to all of the strange predictions of general relativity: e.g., clocks in different gravitational potentials run at different rates, mass bends space, etc.

# 3.2 Gravitational Potential

Consider two point masses, m and $\mathfrak { m } ^ { \prime }$ , located at position vectors r and $\mathbf { r } ^ { \prime }$ , respectively. According to the above analysis, the acceleration $\pmb { g }$ of mass m due to the gravitational force exerted on it by mass $\mathfrak { m } ^ { \prime }$ takes the form

$$
\mathbf { g } = \mathsf { G m } ^ { \prime } \frac { \mathbf { r } ^ { \prime } - \mathbf { r } } { | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { 3 } } .
$$

Now, the $x$ -component of this acceleration is written

$$
9 x = \mathsf { G m } ^ { \prime } \frac { ( x ^ { \prime } - x ) } { [ ( x ^ { \prime } - x ) ^ { 2 } + ( \mathsf { y } ^ { \prime } - \mathsf { y } ) ^ { 2 } + ( z ^ { \prime } - z ) ^ { 2 } ] ^ { 3 / 2 } } ,
$$

where $\mathbf { r } = ( x , y , z )$ and $\mathbf { r } ^ { \prime } = ( \mathrm { x } ^ { \prime } , \mathrm { y } ^ { \prime } , z ^ { \prime } )$ . However, as is easily demonstrated,

$$
\frac { ( x ^ { \prime } - x ) } { \prime - x ) ^ { 2 } + ( y ^ { \prime } - y ) ^ { 2 } + ( z ^ { \prime } - z ) ^ { 2 } ] ^ { 3 / 2 } } \equiv \frac { \partial } { \partial x } \Bigg ( \frac { 1 } { [ ( x ^ { \prime } - x ) ^ { 2 } + ( y ^ { \prime } - y ) ^ { 2 } + ( z ^ { \prime } - z ) ^ { 2 } ] ^ { 1 / 2 } } \Bigg )
$$

Hence,

$$
{ \mathfrak { g } } _ { x } = { \textnormal { G m } } ^ { \prime } { \frac { \partial } { \partial x } } { \Bigg ( } { \frac { 1 } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } } { \Bigg ) } ,
$$

with analogous expressions for ${ \mathfrak { g } } _ { \mathfrak { Y } }$ and $g _ { z }$ . It follows that

$$
\mathbf { g } ( \mathbf { r } ) = - \nabla \Phi ,
$$

where

$$
\Phi ( \mathbf { r } ) = - { \frac { \mathbf { G } \mathsf { m } ^ { \prime } } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } }
$$

is termed the gravitational potential. Of course, we can only write $\pmb { g }$ in the form (3.7) because gravity is a conservative force—see Section 2.4.

Now, it is well-known that gravity is a superposable force. In other words, the gravitational force exerted on some point mass by a collection of other point masses is simply the vector sum of the forces exerted on the former mass by each of the latter masses taken in isolation. It follows that the gravitational potential generated by a collection of point masses at a certain location in space is the sum of the potentials generated at that location by each point mass taken in isolation. Hence, using Equation (3.8), if there are $\mathsf { N }$ point masses, $\mathfrak { m } _ { \mathrm { i } }$ (for $\mathfrak { i } = 1 , \mathsf { N } )$ , located at position vectors $\mathbf { r } _ { \mathrm { i } }$ , then the gravitational potential generated at position vector r is simply

$$
\Phi ( \mathbf { r } ) = - \mathsf { G } \sum _ { \mathrm { i } = 1 , \mathrm { N } } \frac { \mathfrak { m } _ { \mathrm { i } } } { | \mathbf { r } _ { \mathrm { i } } - \mathbf { r } | } .
$$

Suppose, finally, that, instead of having a collection of point masses, we have a continuous mass distribution. In other words, let the mass at position vector $\mathbf { r } ^ { \prime }$ be $\boldsymbol \rho ( \boldsymbol \mathbf { r } ^ { \prime } ) \mathrm { d } ^ { 3 } \boldsymbol \mathbf { r } ^ { \prime }$ , where $\boldsymbol { \rho } ( \mathbf { r } ^ { \prime } )$ is the local mass density, and $\mathrm { d } ^ { 3 } \mathbf { r } ^ { \prime }$ a volume element. Summing over all space, and taking the limit ${ \mathrm { d } } ^ { 3 } \mathbf { r } ^ { \prime } \to 0$ , Equation (3.9) yields

$$
\Phi ( \mathbf { r } ) = - \mathsf { G } \int \frac { \rho ( \mathbf { r } ^ { \prime } ) } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } \mathrm { d } ^ { 3 } \mathbf { r } ^ { \prime } ,
$$

where the integral is taken over all space. This is the general expression for the gravitational potential, $\Phi ( \mathbf { r } )$ , generated by a continuous mass distribution, $\rho ( \mathbf { r } )$ .

# 3.3 Gravitational Potential Energy

Consider a collection of $\mathsf { N }$ point masses $\mathfrak { m } _ { \mathrm { i } }$ located at position vectors $\mathbf { r } _ { \mathrm { i } }$ , respectively (where i runs from 1 to $\mathsf { N }$ ). What is the gravitational potential energy stored in such a collection? In other words, how much work would we have to do in order to assemble the masses, starting from an initial state in which they are all at rest and very widely separated?

We have seen that a gravitational field can be expressed in terms of a gravitational potential: i.e.,

$$
\mathbf { g } ( \mathbf { r } ) = - \nabla \Phi .
$$

We also know that the gravitational force acting on a mass m located at position r is written

$$
\mathbf { f } = \ln \mathbf { g } ( \mathbf { r } ) .
$$

The work we would have to do against the gravitational force in order to slowly move the mass from point $\mathsf { P }$ to point $\mathrm { Q }$ is simply

$$
\mathsf { U } = - \int _ { \mathrm { p } } ^ { \mathrm { Q } } \mathbf { f } \cdot \mathrm { d } \mathbf { r } = - \mathsf { m } \int _ { \mathrm { p } } ^ { \mathrm { Q } } \mathbf { g } \cdot \mathrm { d } \mathbf { r } = \mathsf { m } \int _ { \mathrm { p } } ^ { \mathrm { Q } } \nabla \Phi \cdot \mathrm { d } \mathbf { r } = \mathsf { m } \left[ \Phi ( \mathrm { Q } ) - \Phi ( \mathrm { P } ) \right] .
$$

The negative sign in the above expression comes about because we would have to exert a force $- \mathbf { f }$ on the mass, in order to counteract the force exerted by the gravitational field. Recall, finally, that the gravitational potential generated by a point mass $\mathbf { m } ^ { \prime }$ located at position $\mathbf { r } ^ { \prime }$ is

$$
\Phi ( \mathbf { r } ) = - { \frac { \mathbf { G } \mathsf { m } ^ { \prime } } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } } .
$$

Let us build up our collection of masses one by one. It takes no work to bring the first mass from infinity, since there is no gravitational field to fight against. Let us clamp this mass in position at $\mathbf { r } _ { 1 }$ . In order to bring the second mass into position at $\mathbf { r } _ { 2 }$ , we have to do work against the gravitational field generated by the first masss. According to Equations (3.13) and Equations (3.14), this work is given by

$$
\mathsf { U } _ { 2 } = - \frac { \mathsf { G } \mathsf { m } _ { 2 } \mathsf { m } _ { 1 } } { \vert \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 } \vert } .
$$

Let us now bring the third mass into position. Since gravitational fields and gravitational potentials are superposable, the work done whilst moving the third mass from infinity to $\mathbf { r } _ { 3 }$ is simply the sum of the works done against the gravitational fields generated by charges 1 and 2 taken in isolation:

$$
\mathsf { U } _ { 3 } = - \frac { \mathsf { G } \mathsf { m } _ { 3 } \mathsf { m } _ { 1 } } { \left| \mathbf { r } _ { 1 } - \mathbf { r } _ { 3 } \right| } - \frac { \mathsf { G } \mathsf { m } _ { 3 } \mathsf { m } _ { 2 } } { \left| \mathbf { r } _ { 2 } - \mathbf { r } _ { 3 } \right| } .
$$

Thus, the total work done in assembling the arrangement of three masses is given by

$$
\mathsf { U } = - \frac { \mathsf { G } \mathsf { m } _ { 2 } \mathsf { m } _ { 1 } } { \vert \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 } \vert } - \frac { \mathsf { G } \mathsf { m } _ { 3 } \mathsf { m } _ { 1 } } { \vert \mathbf { r } _ { 1 } - \mathbf { r } _ { 3 } \vert } - \frac { \mathsf { G } \mathsf { m } _ { 3 } \mathsf { m } _ { 2 } } { \vert \mathbf { r } _ { 2 } - \mathbf { r } _ { 3 } \vert } .
$$

This result can easily be generalized to an arrangement of $\mathsf { N }$ point masses:

$$
\mathsf { U } = - \sum _ { \mathrm { i = 1 } } ^ { \mathsf { N } } \sum _ { \mathrm { j < i } } ^ { \mathsf { N } } \frac { \mathsf { G } \mathsf { m } _ { \mathrm { i } } \mathsf { m } _ { \mathrm { j } } } { \vert \mathbf { r } _ { \mathrm { j } } - \mathbf { r } _ { \mathrm { i } } \vert } .
$$

The restriction that j must be less than i makes the above summation rather messy. If we were to sum without restriction (other than $\mathrm { j } \neq \mathrm { i } )$ then each pair of masses would be counted twice. It is convenient to do just this, and then to divide the result by two. Thus, we obtain

$$
\mathsf { U } = - \frac { 1 } { 2 } \sum _ { \mathrm { i = 1 } } ^ { \mathsf { N } } \sum _ { \mathrm { j = 1 } \atop \mathrm { j \not = i } } ^ { \mathsf { N } } \frac { \mathsf { G } \mathsf { m } _ { \mathrm { i } } \mathsf { m } _ { \mathrm { j } } } { \vert \mathbf { r } _ { \mathrm { j } } - \mathbf { r } _ { \mathrm { i } } \vert } .
$$

This is the potential energy of an arrangement of point masses. We can think of this quantity as the work required to bring the masses from infinity and assemble them in the required formation. Alternatively, it is the kinetic energy that would be released if the assemblage were dissolved, and the masses returned to infinity.

Equation (3.19) can be written

$$
W = \frac { 1 } { 2 } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { N } } { \sf m } _ { \mathrm { i } } \Phi _ { \mathrm { i } } ,
$$

where

$$
\Phi _ { \mathrm { i } } = - \mathrm { G } \sum _ { { \mathrm { \scriptsize ~ j = 1 } } \atop { \mathrm { \scriptsize ~ j \neq i } } } ^ { \mathrm { \scriptsize ~ N } } \frac { { \mathrm { m } } _ { \mathrm { j } } } { | \mathbf { r } _ { \mathrm { j } } - \mathbf { r } _ { \mathrm { i } } | }
$$

is the gravitational potential experienced by the i th mass due to the other masses in the distribution. For the case of a continuous mass distribution, we can generalize the above result to give

where

$$
\mathsf { U } = \frac { 1 } { 2 } \int \rho ( \boldsymbol { \mathbf { r } } ) \Phi ( \boldsymbol { \mathbf { r } } ) \mathrm { d } ^ { 3 } \boldsymbol { \mathbf { r } } ,
$$

$$
\Phi ( \mathbf { r } ) = - \mathsf { G } \int \frac { \rho ( \mathbf { r } ^ { \prime } ) } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } \mathrm { d } ^ { 3 } \mathbf { r } ^ { \prime }
$$

is the familiar gravitational potential generated by a continuous mass distribution of mass density $\rho ( \mathbf { r } )$ .

# 3.4 Axially Symmetric Mass Distributions

At this point, it is convenient to adopt standard spherical coordinates, $( \boldsymbol r , \boldsymbol \theta , \boldsymbol \Phi )$ , aligned along the $z$ -axis. These coordinates are related to regular Cartesian coordinates as follows

(see Section A.17):

$$
\begin{array} { l c l } { x } & { = } & { \mathrm { { r } } \sin \theta \cos \phi , } \\ { y } & { = } & { \mathrm { { r } } \sin \theta \sin \phi , } \\ { z } & { = } & { \mathrm { { r } } \cos \theta . } \end{array}
$$

Consider an axially symmetric mass distribution: i.e., a $\rho ( \mathbf { r } )$ which is independent of the azimuthal angle, $\Phi$ . We would expect such a mass distribution to generated an axially symmetric gravitational potential, $\Phi ( \boldsymbol { \mathsf { r } } , \boldsymbol { \mathsf { \theta } } )$ . Hence, without loss of generality, we can set $\Phi = 0$ when evaluating $\Phi ( \mathbf { r } )$ from Equation (3.23). In fact, given that $\mathrm { d } ^ { 3 } \mathbf { r } ^ { \prime } = \mathbf { r } ^ { \prime 2 } \sin \theta ^ { \prime } \mathrm { d } \mathbf { r } ^ { \prime } \mathrm { d } \theta ^ { \prime } \mathrm { d } \phi ^ { \prime }$ in spherical coordinates, this equation yields

$$
\Phi ( \mathbf { r } , \theta ) = - \mathbf { G } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { 2 \pi } \frac { \mathbf { r } ^ { \prime 2 } \rho ( \mathbf { r } ^ { \prime } , \theta ^ { \prime } ) \sin \theta ^ { \prime } } { | \mathbf { r } - \mathbf { r } ^ { \prime } | } \mathrm { d } \mathbf { r } ^ { \prime } \mathrm { d } \theta ^ { \prime } \mathrm { d } \phi ^ { \prime } ,
$$

with the right-hand side evaluated at $\Phi = 0$ . However, since $\rho ( \boldsymbol { \mathsf { r } } ^ { \prime } , \boldsymbol { \mathsf { \theta } } ^ { \prime } )$ is independent of $\Phi ^ { \prime }$ , the above equation can also be written

$$
\Phi ( \mathbf { r } , \theta ) = - 2 \pi \mathbf { G } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \pi } \mathbf { r } ^ { \prime 2 } \mathbf { \rho } ( \mathbf { r } ^ { \prime } , \theta ^ { \prime } ) \sin \theta ^ { \prime } \left. \left| \mathbf { r } - \mathbf { r } ^ { \prime } \right| ^ { - 1 } \right. \mathrm { d } \mathbf { r } ^ { \prime } \mathrm { d } \theta ^ { \prime } ,
$$

where $\langle \cdot \cdot \cdot \rangle \equiv \oint ( \cdot \cdot \cdot ) \mathrm { d } \phi ^ { \prime } / 2 \pi$ denotes an average over the azimuthal angle, $\Phi ^ { \prime }$

Now,

$$
| { \bf r } ^ { \prime } - { \bf r } | ^ { - 1 } = ( { \bf r } ^ { 2 } - 2 { \bf r } \cdot { \bf r } ^ { \prime } + { \bf r } ^ { \prime 2 } ) ^ { - 1 / 2 } ,
$$

and

$$
\mathbf { r } \cdot \mathbf { r } ^ { \prime } = \Upsilon \Upsilon ^ { \prime } \digamma ,
$$

where (at $\Phi = 0 .$ )

$$
\mathsf { F } = \sin \theta \ \sin \theta ^ { \prime } \cos \Phi ^ { \prime } + \cos \theta \ \cos \Theta ^ { \prime } .
$$

Hence,

$$
| \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 } = ( \mathbf { r } ^ { 2 } - 2 \mathsf { r } \mathsf { r } ^ { \prime } \mathsf { F } + \mathbf { r } ^ { \prime 2 } ) ^ { - 1 / 2 } .
$$

Suppose that $\boldsymbol { \mathsf { r } } > \boldsymbol { \mathsf { r } } ^ { \prime }$ . In this case, we can expand $| \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 }$ as a convergent power series in $\boldsymbol { \Upsilon } ^ { \prime } / \boldsymbol { \Upsilon }$ , to give

$$
| \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 } = { \frac { 1 } { \mathrm { r } } } \left[ 1 + \left( { \frac { \mathbf { r } ^ { \prime } } { \mathrm { r } } } \right) \mathsf { F } + { \frac { 1 } { 2 } } \left( { \frac { \mathbf { r } ^ { \prime } } { \mathrm { r } } } \right) ^ { 2 } ( 3 \mathsf { F } ^ { 2 } - 1 ) + O \left( { \frac { \mathbf { r } ^ { \prime } } { \mathrm { r } } } \right) ^ { 3 } \right] .
$$

Let us now average this expression over the azimuthal angle, $\Phi ^ { \prime }$ . Since $\langle 1 \rangle = 1$ , $\left. \cos \Phi ^ { \prime } \right. =$ $0$ , and $\langle \cos ^ { 2 } \Phi ^ { \prime } \rangle = 1 / 2$ , it is easily seen that

$$
\begin{array} { l } { { \langle \mathsf { F } \rangle } } \end{array} = \begin{array} { l } { { \cos \theta \cos \theta ^ { \prime } , } } \\ { { \langle \mathsf { F } ^ { 2 } \rangle } } \end{array} = \begin{array} { l } { { \displaystyle { \frac { 1 } { 2 } } \sin ^ { 2 } \theta \sin ^ { 2 } \theta ^ { \prime } + \cos ^ { 2 } \theta \cos ^ { 2 } \theta ^ { \prime } } } \\ { { \displaystyle = } \begin{array} { l } { { \displaystyle { \frac { 1 } { 3 } } + \frac { 2 } { 3 } \left( \frac { 3 } { 2 } \cos ^ { 2 } \theta - \frac { 1 } { 2 } \right) \left( \frac { 3 } { 2 } \cos ^ { 2 } \theta ^ { \prime } - \frac { 1 } { 2 } \right) } . } \end{array} }  \end{array}
$$

Hence,

$$
\begin{array} { r c l } { \left. \vert \mathbf { r } ^ { \prime } - \mathbf { r } \vert ^ { - 1 } \right. } & { = } & { \displaystyle \frac { 1 } { \mathrm { r } } \left[ 1 + \left( \frac { \mathrm { r } ^ { \prime } } { \mathrm { r } } \right) \cos { \theta } \cos { \Theta ^ { \prime } } \right. } \\ & & { \displaystyle \left. + \left( \frac { \mathrm { r } ^ { \prime } } { \mathrm { r } } \right) ^ { 2 } \left( \frac { 3 } { 2 } \cos ^ { 2 } { \Theta } - \frac { 1 } { 2 } \right) \left( \frac { 3 } { 2 } \cos ^ { 2 } { \Theta ^ { \prime } } - \frac { 1 } { 2 } \right) + \mathcal { O } \left( \frac { \mathrm { r } ^ { \prime } } { \mathrm { r } } \right) ^ { 3 } \right] . } \end{array}
$$

Now, the well-known Legendre polynomials, $\mathsf { P } _ { \mathrm { n } } ( \boldsymbol { \mathsf { x } } )$ , are defined

$$
\mathrm { P _ { n } } ( x ) = \frac { 1 } { 2 ^ { \mathrm { n } } \mathrm { n } ! } \frac { \mathrm { d ^ { n } } } { \mathrm { d } x ^ { \mathrm { n } } } \Big [ ( x ^ { 2 } - 1 ) ^ { \mathrm { n } } \Big ] ,
$$

for $\mathfrak { n } = 0 , \infty$ . It follows that

$$
\begin{array} { l c l } { { \mathsf { P } _ { 0 } ( { \boldsymbol { x } } ) } } & { { = } } & { { 1 , } } \\ { { \mathsf { P } _ { 1 } ( { \boldsymbol { x } } ) } } & { { = } } & { { \boldsymbol { x } , } } \\ { { \mathsf { P } _ { 2 } ( { \boldsymbol { x } } ) } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \left( 3 x ^ { 2 } - 1 \right) , } } \end{array}
$$

etc. The Legendre polynomials are mutually orthogonal: i.e.,

$$
\int _ { - 1 } ^ { 1 } \mathbf { P _ { n } } ( x ) ~ \mathbf { P _ { m } } ( x ) ~ \mathrm { d } x = \int _ { 0 } ^ { \pi } \mathbf { P _ { n } } ( \cos { \theta } ) ~ \mathbf { P _ { m } } ( \cos { \theta } ) ~ \sin { \theta } ~ \mathrm { d } \theta = { \frac { \delta _ { \mathrm { n m } } } { n + 1 / 2 } } .
$$

Here, $\delta _ { \mathrm { { n m } } }$ is 1 if ${ \mathfrak { n } } = { \mathfrak { m } }$ , and 0 otherwise. The Legendre polynomials also form a complete set: i.e., any well-behaved function of $x$ can be represented as a weighted sum of the $\mathsf { P } _ { \mathrm { n } } ( \boldsymbol { x } )$ . Likewise, any well-behaved (even) function of $\theta$ can be represented as a weighted sum of the $\mathsf { P } _ { \mathrm { n } } \big ( \cos \theta \big )$ .

A comparison of Equation (3.36) and Equations (3.38)–(3.40) makes it reasonably clear that, when $\boldsymbol { \mathrm { r } } > \boldsymbol { \mathrm { r } } ^ { \prime }$ , the complete expansion of $\langle | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 } \rangle$ is

$$
\left. | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 } \right. = \frac { 1 } { \mathsf { r } } \sum _ { \mathsf { n } = 0 , \infty } \left( \frac { \mathsf { r } ^ { \prime } } { \mathsf { r } } \right) ^ { \mathsf { n } } \mathsf { P } _ { \mathsf { n } } ( \cos \theta ) \mathsf { P } _ { \mathsf { n } } ( \cos \theta ^ { \prime } ) .
$$

Similarly, when $\boldsymbol { \mathsf { r } } < \boldsymbol { \mathsf { r } } ^ { \prime }$ , we can expand in powers of $\boldsymbol { \mathrm { r } } / \boldsymbol { \mathrm { r } } ^ { \prime }$ to obtain

$$
\left. | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { - 1 } \right. = { \frac { 1 } { \mathbf { r } ^ { \prime } } } \sum _ { \mathrm { n } = 0 , \infty } \left( { \frac { \mathbf { r } } { \mathbf { r } ^ { \prime } } } \right) ^ { \mathrm { n } } \operatorname { P } _ { \mathrm { n } } ( \cos \theta ) \operatorname { P } _ { \mathrm { n } } ( \cos \theta ^ { \prime } ) .
$$

It follows from Equations (3.28), (3.42), and (3.43) that

$$
\Phi ( { \mathfrak { r } } , \theta ) = \sum _ { \mathfrak { n } = 0 , \infty } \Phi _ { \mathfrak { n } } ( { \mathfrak { r } } ) \operatorname { P } _ { \mathfrak { n } } ( \cos \theta ) ,
$$

where

$$
\begin{array} { r c l } { { \Phi _ { \mathrm { n } } ( { \bf r } ) } } & { { = } } & { { \displaystyle - \frac { 2 \pi G } { { \bf r } ^ { n + 1 } } \int _ { 0 } ^ { { \bf r } } \int _ { 0 } ^ { \pi } { \bf r } ^ { \prime } { } ^ { n + 2 } \Theta ( { \bf r } ^ { \prime } , \theta ^ { \prime } ) \mathrm { P } _ { \mathrm { n } } ( \cos \theta ^ { \prime } ) \sin \theta ^ { \prime } \mathrm { d } { \bf r } ^ { \prime } \mathrm { d } \theta ^ { \prime } } } \\ { { } } & { { } } & { { \displaystyle - 2 \pi G { \bf r } ^ { \mathrm { n } } \int _ { { \bf r } } ^ { \infty } \int _ { 0 } ^ { \pi } { \bf r } ^ { \prime } { } ^ { 1 - \mathrm { n } } \Theta ( { \bf r } ^ { \prime } , \theta ^ { \prime } ) \mathrm { P } _ { \mathrm { n } } ( \cos \theta ^ { \prime } ) \sin \theta ^ { \prime } \mathrm { d } { \bf r } ^ { \prime } \mathrm { d } \theta ^ { \prime } . } } \end{array}
$$

Now, given that the $\mathsf { P } _ { \mathrm { n } } \mathopen { } \mathclose \bgroup \left( \cos \theta \aftergroup \egroup \right)$ form a complete set, we can always write

$$
\rho ( \mathfrak { r } , \theta ) = \sum _ { \mathfrak { n } = 0 , \infty } \rho _ { \mathfrak { n } } ( \mathfrak { r } ) \mathsf { P } _ { \mathfrak { n } } ( \cos \theta ) .
$$

This expression can be inverted, with the aid of Equation (3.41), to give

$$
\mathsf { \Pi } _ { \mathsf { P n } } ( { \mathsf { r } } ) = ( { \mathsf { n } } + 1 / 2 ) \int _ { 0 } ^ { \pi } \mathsf { \rho } _ { 0 } ( { \mathsf { r } } , \theta ) \mathsf { P } _ { \mathsf { n } } ( \cos \theta ) \sin \theta \mathrm { ~ d } \theta .
$$

Hence, Equation (3.45) reduces to

$$
\Phi _ { \mathrm { n } } ( { \bf r } ) = - \frac { 2 \pi { \mathsf { G } } } { ( \mathbf { n } + 1 / 2 ) { \mathsf { r } } ^ { \mathrm { n } + 1 } } \int _ { 0 } ^ { \mathsf { r } } { \mathsf { r } } ^ { \prime \mathrm { n } + 2 } \mathsf { \rho } _ { \mathrm { n } } ( { \mathsf { r } } ^ { \prime } ) \mathrm { d } \mathbf { r } ^ { \prime } - \frac { 2 \pi { \mathsf { G } } { \mathsf { r } } ^ { \mathrm { n } } } { \mathsf { n } + 1 / 2 } \int _ { \mathsf { r } } ^ { \infty } { \mathsf { r } } ^ { \prime \mathrm { l } - \mathrm { n } } \mathsf { \rho } _ { \mathrm { n } } ( { \mathsf { r } } ^ { \prime } ) \mathrm { d } \mathbf { r } ^ { \prime } .
$$

Thus, we now have a general expression for the gravitational potential, $\Phi ( \boldsymbol { r } , \boldsymbol { \theta } )$ , generated by any axially symmetric mass distribution, $\boldsymbol { \rho } ( \boldsymbol { \ r } , \boldsymbol { \theta } )$ .

# 3.5 Potential Due to a Uniform Sphere

Let us calculate the gravitational potential generated by a sphere of uniform mass density $\gamma$ and radius a. Expressing $\boldsymbol { \rho } ( \boldsymbol { \ r } , \boldsymbol { \theta } )$ in the form (3.46), it is clear that

$$
\begin{array} { r } { \rho _ { 0 } ( \mathbf { r } ) = \left\{ \begin{array} { l l } { \gamma \qquad } & { \mathrm { f o r ~ r \leq a ~ } } \\ { 0 \qquad } & { \mathrm { f o r ~ r > a ~ } } \end{array} \right. , } \end{array}
$$

with $\rho _ { \mathrm { n } } ( \boldsymbol { \mathsf { r } } ) = 0$ for $\mathfrak { n } > 0$ . Thus, from (3.48),

$$
\Phi _ { 0 } ( \bf { r } ) = - \frac { 4 \pi G \gamma } { r } \int _ { 0 } ^ { r } r ^ { \prime 2 } d r ^ { \prime } - 4 \pi G \gamma \int _ { r } ^ { a } r ^ { \prime } d r ^ { \prime }
$$

for $\Upsilon \leq a$ , and

$$
\Phi _ { 0 } ( \mathbf { r } ) = - \frac { 4 \pi \mathrm { G } \gamma } { \mathrm { r } } \int _ { 0 } ^ { \mathrm { a } } \mathbf { r } ^ { \prime 2 } \mathrm { d } \mathbf { r } ^ { \prime }
$$

for $\Upsilon > { \mathfrak { a } }$ , with $\Phi _ { \mathrm { n } } ( \boldsymbol { \mathsf { r } } ) = 0$ for $\mathfrak { n } > 0$ . Hence,

$$
\Phi ( \mathbf { r } ) = - { \frac { 2 \pi G \gamma } { 3 } } \left( 3 \mathbf { a } ^ { 2 } - \mathbf { r } ^ { 2 } \right) = - \mathsf { G } M { \frac { ( 3 \mathbf { a } ^ { 2 } - \mathbf { r } ^ { 2 } ) } { 2 \mathbf { a } ^ { 3 } } }
$$

for $\boldsymbol { \mathsf { r } } \le \boldsymbol { \mathsf { a } }$ , and

$$
\Phi ( \mathbf { r } ) = - { \frac { 4 \pi \operatorname { G } \gamma } { 3 } } { \frac { \mathbf { a } ^ { 3 } } { \mathbf { r } } } = - { \frac { \operatorname { G } M } { \Gamma } }
$$

for $\boldsymbol { \Upsilon } > \mathbf { a }$ . Here, $M = \left( 4 \pi / 3 \right) \mathrm { { a } } ^ { 3 } \gamma$ is the total mass of the sphere.

According to Equation (3.53), the gravitational potential outside a uniform sphere of mass $M$ is the same as that generated by a point mass M located at the sphere’s center. It turns out that this is a general result for any finite spherically symmetric mass distribution. Indeed, from the above analysis, it is clear that $\rho ( \boldsymbol { \mathsf { r } } ) \ = \ \rho _ { 0 } ( \boldsymbol { \mathsf { r } } )$ and $\Phi ( \boldsymbol { \mathsf { r } } ) = \Phi _ { 0 } ( \boldsymbol { \mathsf { r } } )$ for a spherically symmetric mass distribution. Suppose that the mass distribution extends out to $\boldsymbol { \Upsilon } = \mathbf { a }$ . It immediately follows, from Equation (3.48), that

$$
\Phi (  { \mathbf { r } } ) = - \frac {  { \mathbf { G } } } {  { \mathbf { r } } } \int _ { 0 } ^ {  { \mathbf { a } } } 4 \pi  { \mathbf { r } } ^ { \prime 2 } \rho (  { \mathbf { r } } ^ { \prime } )  { \mathbf { d } }  { \mathbf { r } } ^ { \prime } = - \frac {  { \mathbf { G } }  { \mathbf { M } } } {  { \mathbf { r } } }
$$

for $r > a$ , where $M$ is the total mass of the distribution. Now the center of mass of a spherically symmetric mass distribution lies at the center of the distribution. Moreover, the translational motion of the center of mass is analogous to that of a point particle, whose mass is equal to that of the whole distribution, moving under the action of the net external force (see Section 2.6). We, thus, conclude that Newton’s laws of motion, in their primitive form, apply not only to point masses, but also to the translational motions of extended spherically symmetric mass distributions interacting via gravity (e.g., the Sun and the Planets).

# 3.6 Potential Outside a Uniform Spheroid

Let us now calculate the gravitational potential generated outside a spheroid of uniform mass density $\gamma$ and mean radius a. A spheroid is the solid body produced by rotating an ellipse about a major or minor axis. Let the axis of rotation coincide with the $z$ -axis, and let the outer boundary of the spheroid satisfy

$$
\boldsymbol { \mathrm { r } } = \mathbf { a } _ { \boldsymbol { \Theta } } ( \boldsymbol { \Theta } ) = \mathbf { a } \left[ 1 - \frac { 2 } { 3 } \epsilon \mathsf { P } _ { 2 } ( \cos { \theta } ) \right] ,
$$

where ǫ is the termed the ellipticity. Here, we are assuming that $| \epsilon | \ll 1$ , so that the spheroid is very close to being a sphere. If $\epsilon > 0$ then the spheroid is slightly squashed along its symmetry axis, and is termed oblate. Likewise, if $\epsilon < 0$ then the spheroid is slightly elongated along its axis, and is termed prolate—see Figure 3.1. Of course, if $\epsilon = 0$ then the spheroid reduces to a sphere.

Now, according to Equation (3.44) and (3.45), the gravitational potential generated outside an axially symmetric mass distribution can be written

$$
\Phi ( { \bf r } , \theta ) = \sum _ { { \bf n } = 0 , \infty } \mathrm { J _ { n } } \frac { { \bf P _ { n } } ( \cos \theta ) } { { \bf r } ^ { n + 1 } } ,
$$

![](images/93aff1e7ddbd5ec7e7e2546ac7db09899f3977d0dc837ed48d9e9933ebd7a903.jpg)  
Figure 3.1: Prolate and oblate spheroids.

where

$$
\mathrm { J _ { n } } = - 2 \pi \mathsf { G } \int \int \mathsf { r } ^ { 2 + \mathrm { n } } \mathsf { \rho } ^ { \mathrm { 2 } } \mathsf { P } ^ { \mathrm { } } \left( \mathsf { r } , \theta \right) \mathsf { P } _ { \mathrm { \mathsf { n } } } ( \cos \theta ) \sin \theta \mathrm { d } \mathrm { \mathsf { r } } \mathrm {  d } \theta .
$$

Here, the integral is taken over the whole cross-section of the distribution in r- $\theta$ space.

It follows that for a uniform spheroid

$$
{ \mathrm { J } } _ { \mathrm { n } } = - 2 \pi { \mathsf { G } } \gamma \int _ { 0 } ^ { \pi } { \mathsf { P } } _ { \mathrm { n } } ( \cos \theta ) \int _ { 0 } ^ { \mathsf { a _ { \theta } } ( \boldsymbol { \theta } ) } \Upsilon ^ { 2 + \mathrm { n } } { \mathrm { d } } \mathbf { r } \sin \theta { \mathrm { d } } \theta
$$

Hence,

$$
\mathrm { J } _ { \mathfrak { n } } = - \frac { 2 \pi \mathsf { G } \gamma } { ( 3 + \mathfrak { n } ) } \int _ { 0 } ^ { \pi } \mathsf { P } _ { \mathfrak { n } } ( \cos \theta ) \mathrm { \mathbf { a } } _ { \theta } ^ { 3 + \mathfrak { n } } ( \theta ) \sin \theta \mathrm { \mathbf { d } } \theta ,
$$

giving

$$
\mathrm { J _ { n } } \simeq - \frac { 2 \pi \mathsf { G } \gamma \mathsf { a } ^ { 3 + \mathrm { n } } } { ( 3 + \mathrm { n } ) } \int _ { 0 } ^ { \pi } \mathrm { P _ { n } } ( \cos { \Theta } ) \left[ \mathrm { P } _ { 0 } ( \cos { \Theta } ) - \frac { 2 } { 3 } \left( 3 + \mathrm { n } \right) \epsilon \mathrm { P } _ { 2 } ( \cos { \Theta } ) \right] \sin { \Theta } \mathrm { d } \Theta ,
$$

to first-order in $\epsilon$ . It is thus clear, from Equation (3.41), that, to first-order in $\epsilon$ , the only non-zero $J _ { \mathfrak { n } }$ are

$$
\begin{array} { r c l } { { \mathrm { J } _ { 0 } } } & { { = } } & { { \displaystyle - \frac { 4 \pi { \sf G } \gamma { \sf a } ^ { 3 } } { 3 } = - { \sf G } { \sf M } , } } \\ { { \mathrm { J } _ { 2 } } } & { { = } } & { { \displaystyle \frac { 8 \pi { \sf G } \gamma { \sf a } ^ { 5 } \epsilon } { 1 5 } = \frac { 2 } { 5 } { \sf G } { \sf M } { \sf a } ^ { 2 } \epsilon , } } \end{array}
$$

where $M = \left( 4 \pi / 3 \right) \mathrm { { a } } ^ { 3 } \gamma$ is the total mass.

Thus, the gravitational potential outside a uniform spheroid of total mass $M$ , mean radius $\mathbf { a }$ , and ellipticity $\epsilon$ , is

$$
\Phi ( { \bf r } , \theta ) = - \frac { \mathsf { G } M } { \mathsf { r } } + \frac { 2 } { 5 } \frac { \mathsf { G } M \mathsf { a } ^ { 2 } } { \mathsf { r } ^ { 3 } } \epsilon \mathsf { P } _ { 2 } ( \cos \theta ) + { \cal O } ( \epsilon ^ { 2 } ) .
$$

In particular, the gravitational potential on the surface of the spheroid is

$$
\Phi ( \mathbf { a } _ { \mathsf { \Theta } } , \theta ) = - \frac { \mathsf { G } M } { \mathbf { a } _ { \mathsf { \Theta } } } + \frac { 2 } { 5 } \frac { \mathsf { G } M \mathbf { a } ^ { 2 } } { \mathbf { a } _ { \mathsf { \Theta } } ^ { 3 } } \epsilon \mathsf { P } _ { 2 } ( \cos \theta ) + \mathcal { O } ( \epsilon ^ { 2 } ) ,
$$

which yields

$$
\Phi ( \mathfrak { a } _ { 6 } , \theta ) \simeq - \frac { \mathsf { G } M } { \mathsf { a } } \left[ 1 + \frac { 4 } { 1 5 } \epsilon \mathsf { P } _ { 2 } ( \cos \theta ) + \mathcal { O } ( \epsilon ^ { 2 } ) \right] ,
$$

where use has been made of Equation (3.55).

Consider a self-gravitating spheroid of mass $M$ , mean radius $\mathbf { a }$ , and ellipticity ǫ: e.g., a star, or a planet. Assuming, for the sake of simplicity, that the spheroid is composed of uniform density incompressible fluid, the gravitational potential on its surface is given by Equation (3.65). However, the condition for an equilibrium state is that the potential be constant over the surface. If this is not the case then there will be gravitational forces acting tangential to the surface. Such forces cannot be balanced by internal pressure, which only acts normal to the surface. Hence, from (3.65), it is clear that the condition for equilibrium is $\epsilon = 0$ . In other words, the equilibrium configuration of a self-gravitating mass is a sphere. Deviations from this configuration can only be caused by forces in addition to self-gravity and internal pressure: e.g., internal tensile forces, centrifugal forces due to rotation, or tidal forces due to orbiting masses (see Chapter 6).

We can estimate how small a rocky asteroid or moon needs to be before its internal tensile strength is sufficient to allow it to retain a significantly non-spherical shape. The typical density of rock is $\gamma \sim 3 \times 1 0 ^ { 3 } \mathrm { k g } \mathrm { m } ^ { - 3 }$ . Moreover, the critical compressional stress at which rock ceases to act like a rigid material, and instead deforms and flows like a liquid, is $\mathsf { P } _ { \mathrm { c } } \sim 1 0 ^ { 7 } \mathrm { N } \mathrm { m } ^ { - 2 }$ . We must compare this critical stress with the pressure at the center of the asteroid or moon. Assuming, for the sake of simplicity, that the asteroid or moon is spherical, of radius $\mathbf { a }$ , and of uniform density $\gamma$ , the central pressure is

$$
\mathsf { P } _ { 0 } = \int _ { 0 } ^ { \mathsf { a } } \gamma \mathsf { g } ( \mathsf { r } ) \mathrm { d } \mathsf { r } ,
$$

where ${ \mathfrak { g } } ( { \mathfrak { r } } ) = ( 4 \pi / 3 ) { \mathfrak { G } } \gamma \mathfrak { r }$ r is the gravitational acceleration at radius r [see Equation (3.52)]. The above result is a simple generalization of the well-known formula $\rho { \mathfrak { g h } }$ for the pressure a depth h below the surface of a fluid. It follows that

$$
\mathsf { P } _ { 0 } = \frac { 2 \pi } { 3 } \mathsf { G } \gamma ^ { 2 } \mathsf { a } ^ { 2 } .
$$

Now, if $\mathsf P _ { 0 } \ll \mathsf P _ { \mathrm c }$ then the internal pressure in the asteroid or moon is not sufficiently high to cause its constituent rock to deform like a liquid. Such an asteroid or moon can therefore retain a significantly non-spherical shape. On the other hand, if $\mathsf P _ { 0 } \gg \mathsf P _ { \mathrm c }$ then the internal pressure is large enough to render the asteroid or moon fluid-like. Such a body cannot withstand the tendency of self-gravity to make it adopt a spherical shape. The condition $\mathsf P _ { 0 } \ll \mathsf P _ { \mathrm c }$ is equivalent to ${ \mathbf { a } \ll \mathbf { a _ { c } } }$ , where

$$
\mathbf { a } _ { \mathrm { c } } = \left( \frac { 3 } { 2 \pi } \frac { \mathsf { P } _ { \mathrm { c } } } { \mathsf { G } \gamma ^ { 2 } } \right) ^ { 1 / 2 } \sim 1 0 0 \mathrm { k m } .
$$

It follows that only a rocky asteroid or moon whose radius is significantly less than about $1 0 0 \mathrm { k m }$ (e.g., the two moons of Mars, Phobos and Deimos) can retain a highly non-spherical shape. On the other hand, an asteroid or moon whose radius is significantly greater than about $1 0 0 \mathrm { k m }$ (e.g., the asteroid Ceres, and the Earth’s moon) is forced to be essentially spherical.

# 3.7 Potential Due to a Uniform Ring

Consider a uniform ring of mass $M$ and radius r, centered on the origin, and lying in the $x$ -y plane. Let us consider the gravitational potential $\Phi ( \boldsymbol { \mathsf { r } } )$ generated by such a ring in the $x$ -y plane (which corresponds to $\theta = 9 0 ^ { \circ }$ ). It follows, from Section 3.4, that for $\boldsymbol { \Upsilon } > a$ ,

$$
\Phi ( { \bf r } ) = - \frac { { \bf G } { \sf M } } { { \bf a } } \sum _ { { \sf n } = 0 , \infty } [ { \sf P } _ { \bf \pi } ( 0 ) ] ^ { 2 } \left( \frac { \bf a } { \sf r } \right) ^ { { \bf n } + 1 } .
$$

However, $\mathsf { P } _ { 0 } ( 0 ) = 1 , \mathsf { P } _ { 1 } ( 0 ) = 0 , \mathsf { P } _ { 2 } ( 0 ) = - 1 / 2 , \mathsf { P } _ { 3 } ( 0 ) = 0 .$ and $\mathsf { P } _ { 4 } ( 0 ) = 3 / 8$ . Hence,

$$
\Phi ( \mathbf { r } ) = - { \frac { \mathsf { G } M } { \mathsf { r } } } \left[ 1 + { \frac { 1 } { 4 } } \left( { \frac { \mathbf { a } } { \mathsf { r } } } \right) ^ { 2 } + { \frac { 9 } { 6 4 } } \left( { \frac { \mathbf { a } } { \mathsf { r } } } \right) ^ { 4 } + \cdots \right] .
$$

Likewise, for $\boldsymbol { \Upsilon } < \mathbf { a }$

$$
\Phi ( { \bf r } ) = - \frac { { \bf G } { \cal M } } { { \bf a } } \sum _ { { \bf n } = 0 , \infty } [ { \bf P } _ { \bf n } ( 0 ) ] ^ { 2 } \left( \frac { { \bf r } } { { \bf a } } \right) ^ { \bf n } ,
$$

giving

$$
\Phi ( \mathbf { r } ) = - \frac { \mathsf { G } M } { \mathbf { a } } \left[ 1 + \frac { 1 } { 4 } \left( \frac { \mathbf { r } } { \mathbf { a } } \right) ^ { 2 } + \frac { \mathsf { 9 } } { 6 4 } \left( \frac { \mathbf { r } } { \mathbf { a } } \right) ^ { 4 } + \cdots \right] .
$$

# 3.8 Exercises

3.1. Consider an isolated system of $\mathsf { N }$ point objects interacting via gravity. Let the mass and position vector of the ith object be $\mathfrak { m } _ { \mathrm { i } }$ and $\mathbf { r } _ { \mathrm { i } }$ , respectively. What is the vector equation of motion of the ith object? Write expressions for the total kinetic energy, K, and potential energy, U, of the system. Demonstrate from the equations of motion that $\mathsf { K } + \mathsf { U }$ is a conserved quantity.

3.2. A particle is projected vertically upward from the Earth’s surface with a velocity which would, if gravity were uniform, carry it to a height h. Show that if the variation of gravity with height is allowed for, but the resistance of air is neglected, then the height reached will be greater by $\mathsf { h } ^ { 2 } / ( \mathsf { R } - \mathsf { h } )$ , where R is the Earth’s radius.

3.3. A particle is projected vertically upward from the Earth’s surface with a velocity just sufficient for it to reach infinity (neglecting air resistance). Prove that the time needed to reach a height $\mathrm { h }$ is

$$
\frac { 1 } { 3 } \left( \frac { 2 \mathrm { R } } { 9 } \right) ^ { 1 / 2 } \left[ \left( 1 + \frac { \mathrm { h } } { \mathrm { R } } \right) ^ { 3 / 2 } - 1 \right] .
$$

where R is the Earth’s radius, and $9$ its surface gravitational acceleration.

3.4. Demonstrate that if a narrow shaft were drilled though the center of a uniform self-gravitating sphere then a test mass moving in this shaft executes simple harmonic motion about the center of the sphere with period

$$
{ \sf T } = 2 \pi \sqrt { \frac { { \sf a } } { { \sf g } } } ,
$$

where a is the radius of the sphere, and $9$ the gravitational acceleration at its surface.

3.5. Demonstrate that the gravitational potential energy of a spherically symmetric mass distribution of mass density $\rho ( \boldsymbol { \mathsf { r } } )$ that extends out to $\boldsymbol { \Upsilon } = \mathbf { a }$ can be written

$$
\mathsf { U } = - 1 6 \pi ^ { 2 } \mathsf { G } \int _ { 0 } ^ { \mathsf { a } } \mathsf { r } \mathsf { \rho } \mathsf { \rho } \mathsf { \rho } \mathsf { \rho } \big ( \mathsf { r } \big ) \int _ { 0 } ^ { \mathsf { r } } \mathsf { r } ^ { \prime 2 } \mathsf { \rho } \mathsf { \rho } \mathsf { \rho } \big ( \mathsf { r } ^ { \prime } \big ) \mathsf { d } \mathsf { r } ^ { \prime } \ : \mathrm { d } \mathsf { r } .
$$

Hence, show that if the mass distribution is such that

$$
\begin{array} { r } { \rho ( \mathbf { r } ) = \left\{ \begin{array} { l l } { \rho _ { 0 } \mathbf { r } ^ { - \alpha } \quad \quad } & { \mathbf { r } \leq \mathbf { a } } \\ { 0 \quad \quad } & { \mathbf { r } > \mathbf { a } } \end{array} \right. , } \end{array}
$$

where $\alpha < 5 / 2$ , then

$$
{ \mathsf { U } } = - \frac { ( 3 - \alpha ) } { ( 5 - 2 \alpha ) } \frac { \mathsf { G } M ^ { 2 } } { \mathsf { a } } ,
$$

where $M$ is the total mass.

3.6. A star can be through of as a spherical system that consists of a very large number of particles interacting via gravity. Show that, for such a system, the virial theorem, introduced in Exercise 2.2, implies that

$$
{ \frac { \mathrm { d } ^ { 2 } \mathrm { I } } { \mathrm { d t } ^ { 2 } } } = - 2 \mathrm { U } + \mathrm { c } ,
$$

where c is a constant, and the ${ \boldsymbol { \mathrm { r } } } _ { \mathrm { i } }$ are measured from the geometric center. Hence, deduce that the angular frequency of small amplitude radial pulsations of the star (in which the radial displacement is directly proportional to the radial distance from the center) takes the form

$$
 \omega = \left( \frac { | \mathrm {  ~ U } _ { 0 } | } { \mathrm {  ~ I } _ { 0 } } \right) ^ { 1 / 2 } ,
$$

where $\mathsf { U } _ { 0 }$ and $\mathrm { I } _ { 0 }$ are the equilibrium values of $\mathrm { u }$ and I. Finally, show that if the mass density within the star varies as $r ^ { - \alpha }$ , where $\boldsymbol { \mathsf { r } }$ is the radial distance from the geometric center, and where $\alpha < 5 / 2$ , then

$$
\omega = \left( \frac { 5 - \alpha } { 5 - 2 \alpha } \frac { { \sf G } M } { { \sf R } ^ { 3 } } \right) ^ { 1 / 2 } ,
$$

where $M$ and $\mathsf { R }$ are the stellar mass and radius, respectively.

# 4 Keplerian Orbits

# 4.1 Introduction

Newtonian mechanics was initially developed in order to account for the motion of the Planets in the Solar System. Let us now examine this problem. Suppose that the Sun, whose mass is M, is located at the origin of our coordinate system. Consider the motion of a general planet, of mass m, that is located at position vector r. Given that the Sun and all of the Planets are approximately spherical, the gravitational force exerted on the planet by the Sun can be written (see Chapter 3)

$$
\mathbf { f } = - { \frac { \mathbf { G } M \mathfrak { m } } { \mathfrak { r } ^ { 3 } } } \mathbf { r } .
$$

An equal and opposite force to (4.1) acts on the Sun. However, we shall assume that the Sun is so much more massive than the planet that this force does not cause the Sun’s position to shift appreciably. Hence, the Sun will always remain at the origin of our coordinate system. Likewise, we shall neglect the gravitational forces exerted on our chosen planet by the other bodies in the Solar System, compared to the gravitational force exerted on it by the Sun. This is reasonable because the Sun is much more massive (by a factor of, at least, $1 0 ^ { 3 } )$ than any other body in the Solar System. Thus, according to Equation (4.1), and Newton’s second law of motion, the equation of motion of our planet (which can effectively be treated as a point object—see Chapter 3) takes the form

$$
{ \frac { \mathrm { d } ^ { 2 } \mathbf { r } } { \mathrm { d t } ^ { 2 } } } = - { \frac { \mathrm { G } M } { \mathrm { r } ^ { 3 } } } \mathbf { r } .
$$

Note that the planet’s mass, m, has canceled out on both sides of the above equation.

# 4.2 Kepler’s Laws

As is well-known, Johannes Kepler was the first astronomer to correctly describe the motion of the Planets in the Solar System (in works published between 1609 and 1619). The motion of the Planets is summed up in three simple laws:

1. The planetary orbits are all ellipses which are confocal with the Sun (i.e., the Sun lies at one of the focii of each ellipse—see Appendix B.1).   
2. The radius vectors connecting each planet to the Sun sweep out equal areas in equal time intervals.   
3. The squares of the orbital periods of the planets are proportional to the cubes of their orbital major radii.

Let us now see if we can derive Kepler’s laws from Equation (4.2).

# 4.3 Conservation Laws

As we have already seen, gravity is a conservative force. Hence, the gravitational force (4.1) can be written (see Section 2.4)

$$
\mathbf { f } = - \nabla \mathsf { U } ,
$$

where the potential energy, $\mathrm { U } ( \mathbf { r } )$ , of our planet in the Sun’s gravitational field takes the form (see Section 3.5)

$$
\mathsf { U } ( \mathbf { r } ) = - \frac { \mathsf { G } M \mathsf { m } } { \mathsf { r } } .
$$

It follows that the total energy of our planet is a conserved quantity—see Section 2.4. In other words,

$$
\mathcal { E } = \frac { \nu ^ { 2 } } { 2 } - \frac { \mathsf { G } M } { \mathsf { r } }
$$

is constant in time. Here, $\mathcal { E }$ is actually the planet’s total energy per unit mass, and ${ \bf v } =$ dr/dt.

Gravity is also a central force. Hence, the angular momentum of our planet is a con served quantity—see Section 2.5. In other words,

$$
\mathbf { h } = \mathbf { r } \times \mathbf { v } ,
$$

which is actually the planet’s angular momentum per unit mass, is constant in time. Taking the scalar product of the above equation with r, we obtain

$$
\mathbf { h } \cdot \mathbf { r } = 0 .
$$

This is the equation of a plane which passes through the origin, and whose normal is parallel to h. Since h is a constant vector, it always points in the same direction. We, therefore, conclude that the motion of our planet is two-dimensional in nature: i.e., it is confined to some fixed plane which passes through the origin. Without loss of generality, we can let this plane coincide with the x-y plane.

# 4.4 Polar Coordinates

We can determine the instantaneous position of our planet in the $x { - } y$ plane in terms of standard Cartesian coordinates, $( \mathfrak { x } , \mathfrak { y } )$ , or polar coordinates, (r, θ), as illustrated in Figure 4.1. Here, $\mathsf { r } = \sqrt { \mathsf { x } ^ { 2 } + \mathsf { y } ^ { 2 } }$ and $\theta = \tan ^ { - 1 } ( { \mathsf { y } } / x )$ . It is helpful to define two unit vectors, ${ \bf e } _ { \mathrm { r } } \equiv { \bf r } / { \mathrm { r } }$ and $\mathbf { e } _ { \theta } \equiv \mathbf { e } _ { z } \times \mathbf { e } _ { \mathrm { r } }$ , at the instantaneous position of the planet. The first always points radially away from the origin, whereas the second is normal to the first, in the direction of increasing θ. As is easily demonstrated, the Cartesian components of $\mathbf { e } _ { \mathrm { r } }$ and $\mathbf { e } _ { \theta }$ are

$$
\begin{array} { r c l } { { { \bf e } _ { \mathrm { r } } } } & { { = } } & { { ( \cos { \theta } , \sin { \theta } ) , } } \\ { { { \bf e } _ { \theta } } } & { { = } } & { { ( - \sin { \theta } , \cos { \theta } ) , } } \end{array}
$$

![](images/68e67a3e4b189235ba01b584ed9edd7087bc14d71f6b6b3d3eca1dc26dee7fde.jpg)  
Figure 4.1: Polar coordinates.

respectively.

We can write the position vector of our planet as

$$
\mathbf { r } = \mathrm { r } \mathbf { e } _ { \mathrm { r } } .
$$

Thus, the planet’s velocity becomes

$$
{ \bf v } = \frac { \mathrm { d } { \bf r } } { \mathrm { d t } } = \dot { \bf r } { \bf e } _ { \mathrm { r } } + { \bf r } \dot { \bf e } _ { \mathrm { r } } ,
$$

where ˙ is shorthand for $\mathrm { d } / \mathrm { d t }$ . Note that $\mathbf { e } _ { \mathrm { r } }$ has a non-zero time-derivative (unlike a Cartesian unit vector) because its direction changes as the planet moves around. As is easily demonstrated, from differentiating Equation (4.8) with respect to time,

$$
{ \dot { \mathbf { e } } } _ { \mathrm { r } } = { \dot { \theta } } \left( - \sin { \theta } , \cos { \theta } \right) = { \dot { \theta } } \ \mathbf { e } _ { \theta } .
$$

Thus,

$$
\mathbf { v } = { \dot { \mathbf { r } } } \ \mathbf { e } _ { \mathrm { r } } + { \mathrm { r } } { \dot { \theta } } \ \mathbf { e } _ { \theta } .
$$

Now, the planet’s acceleration is written

$$
\mathbf { a } = { \frac { \mathrm { d } \mathbf { v } } { \mathrm { d t } } } = { \frac { \mathrm { d } ^ { 2 } \mathbf { r } } { \mathrm { d } \mathbf { t } ^ { 2 } } } = { \ddot { \mathbf { r } } } \mathbf { e } _ { \mathrm { r } } + { \dot { \mathbf { r } } } { \dot { \mathbf { e } } } _ { \mathrm { r } } + \left( { \dot { \mathbf { r } } } { \dot { \theta } } + \mathbf { r } { \ddot { \theta } } \right) \mathbf { e } _ { \theta } + \mathbf { r } { \dot { \theta } } \ { \dot { \mathbf { e } } } _ { \theta } .
$$

Again, $\mathbf { e } _ { \theta }$ has a non-zero time-derivative because its direction changes as the planet moves around. Differentiation of Equation (4.9) with respect to time yields

$$
\dot { \mathbf { e } } _ { \theta } = \dot { \theta } \left( - \cos \theta , - \sin \theta \right) = - \dot { \theta } \mathbf { e } _ { \mathrm { r } } .
$$

Hence,

$$
\mathbf { a } = ( \ddot { \mathbf { r } } - \mathbf { r } \dot { \theta } ^ { 2 } ) \mathbf { e } _ { \mathrm { r } } + ( \mathbf { r } \ddot { \theta } + 2 \dot { \mathbf { r } } \dot { \theta } ) \mathbf { e } _ { \theta } .
$$

![](images/adc8f0963504d1dc5c3d87a3c9190065a841cef3b49c64bca4a46d3b5b4aa319.jpg)  
Figure 4.2: Kepler’s second law.

It follows that the equation of motion of our planet, (4.2), can be written

$$
\mathbf { a } = ( \ddot { \mathfrak { r } } - \mathfrak { r } \dot { \Theta } ^ { 2 } ) \mathbf { e } _ { \mathfrak { r } } + ( \mathfrak { r } \ddot { \Theta } + 2 \dot { \mathfrak { r } } \dot { \Theta } ) \mathbf { e } _ { \Theta } = - \frac { \mathsf { G } M } { \mathfrak { r } ^ { 2 } } \mathbf { e } _ { \mathrm { r } } .
$$

Since $\mathbf { e } _ { \mathrm { r } }$ and $\mathbf { e } _ { \theta }$ are mutually orthogonal, we can separately equate the coefficients of both, in the above equation, to give a radial equation of motion,

$$
{ \ddot { \mathsf { r } } } - { \mathsf { r } } { \dot { \mathsf { \theta } } } ^ { 2 } = - { \frac { \mathsf { G } M } { { \mathsf { r } } ^ { 2 } } } ,
$$

and a tangential equation of motion,

$$
{ \mathrm { r } } { \ddot { \theta } } + 2 { \dot { \mathrm { r } } } { \dot { \theta } } = 0 .
$$

# 4.5 Kepler’s Second Law

Multiplying our planet’s tangential equation of motion, (4.19), by r, we obtain

$$
\boldsymbol { \mathrm { r } } ^ { 2 } \ddot { \boldsymbol { \Theta } } + 2 \boldsymbol { \mathrm { r } } \dot { \boldsymbol { \mathrm { r } } } \dot { \boldsymbol { \Theta } } = 0 .
$$

However, the above equation can be also written

$$
\frac { \mathrm { d } ( \mathrm { r } ^ { 2 } { \dot { \theta } } ) } { \mathrm { d t } } = 0 ,
$$

which implies that

$$
\mathbf { h } = \mathbf { r } ^ { 2 } { \dot { \boldsymbol { \theta } } }
$$

is constant in time. It is easily demonstrated that $\mathrm { \hslash }$ is the magnitude of the vector h defined in Equation (4.6). Thus, the fact that $\mathrm { \hslash }$ is constant in time is equivalent to the statement that the angular momentum of our planet is a constant of its motion. As we have already mentioned, this is the case because gravity is a central force.

Suppose that the radius vector connecting our planet to the origin (i.e., the Sun) sweeps out an angle δθ between times t and $\mathrm { t } + \delta$ t—see Figure 4.2. The approximately triangular region swept out by the radius vector has the area

$$
\delta \mathsf { A } \simeq \frac { 1 } { 2 } \mathsf { r } ^ { 2 } \delta \mathsf { \Theta } ,
$$

since the area of a triangle is half its base $( r \delta \theta )$ times its height (r). Hence, the rate at which the radius vector sweeps out area is

$$
{ \frac { \mathrm { d } A } { \mathrm { d t } } } = \operatorname* { l i m } _ { \delta \mathrm { t } \to 0 } { \frac { \mathrm { r } ^ { 2 } \delta \theta } { 2 \delta \mathrm { t } } } = { \frac { \mathrm { r } ^ { 2 } } { 2 } } { \frac { \mathrm { d } \theta } { \mathrm { d t } } } = { \frac { \mathrm { h } } { 2 } } .
$$

Thus, the radius vector sweeps out area at a constant rate (since $\mathrm { \hslash }$ is constant in time)— this is Kepler’s second law. We conclude that Kepler’s second law of planetary motion is a direct consequence of angular momentum conservation.

# 4.6 Kepler’s First Law

Our planet’s radial equation of motion, (4.18), can be combined with Equation (4.22) to give

$$
{ \ddot { \mathsf { r } } } - { \frac { \mathsf { h } ^ { 2 } } { \mathsf { r } ^ { 3 } } } = - { \frac { \mathsf { G } M } { \mathsf { r } ^ { 2 } } } .
$$

Suppose that $\mathfrak { r } = \mathfrak { u } ^ { - 1 }$ . It follows that

$$
{ \dot { \mathsf { r } } } = - { \frac { \dot { \mathsf { u } } } { { \mathsf { u } } ^ { 2 } } } = - { \mathsf { r } } ^ { 2 } { \frac { { \mathrm { d } } { \mathsf { u } } } { { \mathrm { d } } \theta } } { \frac { { \mathrm { d } } \theta } { { \mathrm { d } } { \mathsf { t } } } } = - { \mathsf { h } } { \frac { { \mathrm { d } } { \mathsf { u } } } { { \mathrm { d } } \theta } } .
$$

Likewise,

$$
\ddot { \boldsymbol { \mathrm { r } } } = - \mathrm { h } \frac { \mathrm { d } ^ { 2 } \mathrm { u } } { \mathrm { d } \Theta ^ { 2 } } \dot { \boldsymbol { \theta } } = - \mathrm { u } ^ { 2 } \mathrm { h } ^ { 2 } \frac { \mathrm { d } ^ { 2 } \mathrm { u } } { \mathrm { d } \Theta ^ { 2 } } .
$$

Hence, Equation (4.25) can be written in the linear form

$$
{ \frac { \mathrm { d } ^ { 2 } \mathrm { u } } { \mathrm { d } \theta ^ { 2 } } } + \mathrm { u } = { \frac { \mathrm { G } M } { \mathrm { h } ^ { 2 } } } .
$$

The general solution to the above equation is

$$
{ \bf { u } } ( \theta ) = { \frac { { \bf { G } } { \bf { M } } } { { \bf { h } } ^ { 2 } } } \left[ { 1 - e \cos ( \theta - \theta _ { 0 } ) } \right] ,
$$

where $e$ and $\theta _ { 0 }$ are arbitrary constants. Without loss of generality, we can set $\theta _ { 0 } = 0$ by rotating our coordinate system about the $z$ -axis. Thus, we obtain

$$
{ \bf r } ( \theta ) = \frac { { \bf r } _ { \mathrm { c } } } { 1 - e \cos \theta } ,
$$

where

$$
\mathfrak { r } _ { \mathrm { c } } = \frac { \mathtt { h } ^ { 2 } } { \mathtt { G } M } .
$$

We immediately recognize Equation (4.30) as the equation of a conic section that is confocal with the origin (i.e., with the Sun)—see Appendix B.1. Specifically, for $e < 1$ , (4.30) is the equation of an ellipse. For $e = 1$ , (4.30) is the equation of a parabola. Finally, for $e > 1$ , (4.30) is the equation of a hyperbola. However, a planet cannot have a parabolic or a hyperbolic orbit, since such orbits are only appropriate to objects which are ultimately able to escape from the Sun’s gravitational field. Thus, the orbit of our planet around the Sun is a confocal ellipse—this is Kepler’s first law of planetary motion

# 4.7 Kepler’s Third Law

We have seen that the radius vector connecting our planet to the origin sweeps out area at the constant rate $\mathrm { d } A / \mathrm { d t } = \mathrm { h } / 2$ [see Equation (4.24)]. We have also seen that the planetary orbit is an ellipse. Suppose that the major and minor radii of the ellipse are a and b, respectively. It follows that the area of the ellipse is $\lambda = \pi { \mathfrak { a } } { \mathfrak { b } }$ . Now, we expect the radius vector to sweep out the whole area of the ellipse in a single orbital period, T . Hence,

$$
\mathsf { T } = \frac { \mathsf { A } } { ( \mathrm { d } \mathsf { A } / \mathrm { d t } ) } = \frac { 2 \pi \mathrm { a } \mathrm { b } } { \mathrm { h } } .
$$

It follows from Equations (B.7), (B.8), and (4.31) that

$$
\mathsf { T } ^ { 2 } = \frac { 4 \pi ^ { 2 } \mathsf { a } ^ { 3 } } { \mathsf { G } M } .
$$

In other words, the square of the orbital period of our planet is proportional to the cube of its orbital major radius—this is Kepler’s third law.

Note that for an elliptical orbit the closest distance to the Sun—the so-called perihelion distance—is [see Equations (B.7) and (4.30)]

$$
{ \bf r } _ { \mathrm { p } } = \frac { { \bf r } _ { \mathrm { c } } } { 1 + e } = { \bf a } ( 1 - e ) .
$$

Likewise, the furthest distance from the Sun—the so-called aphelion distance—is

$$
{ \mathfrak { r } } _ { \mathfrak { a } } = { \frac { { \mathfrak { r } } _ { \mathfrak { c } } } { 1 - e } } = \mathbf { a } ( 1 + e ) .
$$

It follows that the major radius, $\mathbf { a }$ , is simply the mean of the perihelion and aphelion distances,

$$
\mathrm { { a } } = { \frac { \mathrm { { r _ { p } } + \mathrm { { r _ { a } } } } } { 2 } } .
$$

The parameter

$$
e = { \frac { \mathsf { r } _ { \mathrm { a } } - \mathsf { r } _ { \mathrm { p } } } { \mathsf { r } _ { \mathrm { a } } + \mathsf { r } _ { \mathrm { p } } } }
$$

is called the eccentricity, and measures the deviation of the orbit from circularity. Thus, $e = 0$ corresponds to a circular orbit, whereas $e \to 1$ corresponds to an infinitely elongated elliptical orbit.

As is easily demonstrated from the above analysis, Kepler laws of planetary motion can be written in the convenient form

$$
\begin{array} { r c l } { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \end{array} \begin{array} { r c l } { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \end{array} ,
$$

where a is the mean orbital radius (i.e., the major radius), e the orbital eccentricity, and $\mathfrak { n } = 2 \pi / \mathsf { T }$ the mean orbital angular velocity.

# 4.8 Orbital Energies

Let us now generalize our analysis to take into account the orbits of asteroids and comets about the Sun. Such orbits satisfy Equation (4.30), but can be parabolic $( e = 1 )$ ), or even hyperbolic $( e > 1 )$ , as well as elliptical $( e < 1 )$ . According to Equations (4.5) and (4.13), the total energy per unit mass of an object in a general orbit around the Sun is given by

$$
\mathcal { E } = \frac { \dot { \Upsilon } ^ { 2 } + \Upsilon ^ { 2 } \dot { \theta } ^ { 2 } } { 2 } - \frac { \mathsf { G } M } { \Upsilon } .
$$

It follows from Equations (4.22), (4.26), and (4.31) that

$$
\mathcal { E } = \frac { \mathrm { h } ^ { 2 } } { 2 } \left[ \left( \frac { \mathrm { d } \mathrm { u } } { \mathrm { d } \theta } \right) ^ { 2 } + \mathrm { u } ^ { 2 } - 2 \mathrm { u } \mathrm { u } _ { \mathrm { c } } \right] ,
$$

where $\mathfrak { u } = \mathfrak { r } ^ { - 1 }$ , and $\mathfrak { u } _ { \mathrm { c } } = \mathfrak { r } _ { \mathrm { c } } ^ { - 1 }$ . However, according to Equation (4.30),

$$
\mathrm { u } ( \theta ) = \mathrm { u } _ { \mathrm { c } } ( 1 - e \cos \theta ) .
$$

The previous two equations can be combined with Equations (4.31) and (4.34) to give

$$
\mathcal { E } = \frac { \mathrm { u } _ { c } ^ { 2 } \mathrm { h } ^ { 2 } } { 2 } \left( e ^ { 2 } - 1 \right) = \frac { \mathrm { G } \mathsf { M } } { 2 \mathrm { r } _ { \mathrm { p } } } \left( e - 1 \right) .
$$

We conclude that elliptical orbits $( e < 1 )$ ) have negative total energies, whereas parabolic orbits $( e = 1 )$ ) have zero total energies, and hyperbolic orbits $( e > 1 )$ have positive total energies. This makes sense, since in a conservative system in which the potential energy at infinity is set to zero [see Equation (4.4)] we expect bounded orbits to have negative total energies, and unbounded orbits to have positive total energies—see Section 2.7. Thus, elliptical orbits, which are clearly bounded, should indeed have negative total energies, whereas hyperbolic orbits, which are clearly unbounded, should indeed have positive total energies. Parabolic orbits are marginally bounded (i.e., an object executing a parabolic orbit only just escapes from the Sun’s gravitational field), and thus have zero total energy. For the special case of an elliptical orbit, whose major radius a is finite, we can write

$$
\mathcal { E } = - \frac { \mathsf { G } M } { 2 \alpha } .
$$

It follows that the energy of such an orbit is completely determined by the orbital major radius.

Consider an artificial satellite in an elliptical orbit around the Sun (the same considerations also apply to satellites in orbit around the Earth). At perihelion, ${ \dot { \boldsymbol { \mathsf { r } } } } = 0 \qquad $ , and Equations (4.41) and (4.44) can be combined to give

$$
\frac { \nu _ { \mathrm { t } } } { \nu _ { \mathrm { c } } } = \sqrt { 1 + e } .
$$

Here, $\nu _ { \mathrm { t } } = \mathrm { r } { \dot { \Theta } }$ is the satellite’s tangential velocity, and $\nu _ { \mathrm { c } } = \sqrt { \mathrm { G } M / \mathfrak { r } _ { \mathrm { p } } }$ is the tangential velocity that it would need in order to maintain a circular orbit at the perihelion distance. Likewise, at aphelion,

$$
\frac { \nu _ { \mathrm { t } } } { \nu _ { \mathrm { c } } } = \sqrt { 1 - e } ,
$$

where $\nu _ { \mathrm { c } } = \sqrt { \mathsf { G } M / \mathsf { r } _ { \mathrm { a } } }$ is now the tangential velocity that the satellite would need in order to maintain a circular orbit at the aphelion distance.

Suppose that our satellite is initially in a circular orbit of radius $\boldsymbol { \mathrm { r } } _ { 1 }$ , and that we wish to transfer it into a circular orbit of radius $\boldsymbol { \mathsf { r } } _ { 2 }$ , where ${ \boldsymbol { \ r } } _ { 2 } > { \boldsymbol { \ r } } _ { 1 }$ . We can achieve this by temporarily placing the satellite in an elliptical orbit whose perihelion distance is $\boldsymbol { \mathrm { r } } _ { 1 }$ , and whose aphelion distance is $\boldsymbol { \mathrm { r } } _ { 2 }$ . It follows, from Equation (4.37), that the required eccentricity of the elliptical orbit is

$$
e = { \frac { \Upsilon _ { 2 } - \Upsilon _ { 1 } } { \Upsilon _ { 2 } + \Upsilon _ { 1 } } } .
$$

According to Equation (4.46), we can transfer our satellite from its initial circular orbit into the temporary elliptical orbit by increasing its tangential velocity (by briefly switching on the satellite’s rocket motor) by a factor

$$
\alpha _ { 1 } = \sqrt { 1 + e } .
$$

We must next allow the satellite to execute half an orbit, so that it attains its aphelion distance, and then boost the tangential velocity by a factor [see Equation (4.47)]

$$
\alpha _ { 2 } = { \frac { 1 } { \sqrt { 1 - e } } } .
$$

The satellite will now be in a circular orbit at the aphelion distance, $\boldsymbol { \mathrm { r } } _ { 2 }$ . This process is illustrated in Figure 4.3. Obviously, we can transfer our satellite from a larger to a smaller circular orbit by performing the above process in reverse. Note, finally, from Equation (4.46), that if we increase the tangential velocity of a satellite in a circular orbit about the Sun by a factor greater than $\sqrt { 2 }$ then we will transfer it into a hyperbolic orbit $( e > 1 )$ , and it will eventually escape from the Sun’s gravitational field.

![](images/e317aee7e5ca4ed259daf834f3ed2616818a3d2aea9f6f2d1b45e398d8e872f9.jpg)  
Figure 4.3: A transfer orbit between two circular orbits.

# 4.9 Kepler Problem

In a nutshell, the so-called Kepler problem consists of determining the radial and angular coordinates, r and θ, respectively, of an object in an elliptical, parabolic, or hyperbolic orbit about the Sun as a function of time.

Consider an object in a general Keplerian orbit about the Sun which passes through its perihelion point, ${ \boldsymbol { \mathsf { r } } } = { \boldsymbol { \mathsf { r } } } _ { \mathsf { p } }$ and $\theta = 0$ , at $\mathrm { t } = \tau$ . The constant $\tau$ is termed the time of perihelion passage. It follows from the previous analysis that

$$
\Upsilon = { \frac { \Upsilon _ { \mathsf { p } } \left( 1 + e \right) } { 1 + e \cos \theta } } ,
$$

and

$$
\mathcal { E } = \frac { \dot { \mathrm { \Delta r } } ^ { 2 } } { 2 } + \frac { \mathrm { h } ^ { 2 } } { 2 \mathrm { r } ^ { 2 } } - \frac { \mathrm { G } M } { \mathrm { \Delta r } } ,
$$

where e, $\mathsf { h } = \sqrt { \mathsf { G } M \mathsf { r } _ { \mathsf { p } } ( 1 + e ) }$ , and $\mathcal { E } = \mathsf { G } M ( e - 1 ) / ( 2 \mathsf { r } _ { \mathsf { p } } )$ are the orbital eccentricity, angular momentum per unit mass, and energy per unit mass, respectively. The above equation can be rearranged to give

$$
\dot { \mathrm { r } } ^ { 2 } = ( e - 1 ) \frac { \mathrm { G } M } { \mathrm { r } _ { \mathrm { p } } } - ( e + 1 ) \frac { \mathrm { r } _ { \mathrm { p } } \mathrm { G } M } { \mathrm { r } ^ { 2 } } + \frac { 2 \mathrm { G } M } { \mathrm { r } } .
$$

Taking the square-root, and integrating, we obtain

$$
\int _ { \mathrm { r _ { p } } } ^ { \mathrm { r } } \frac { \mathrm { r } \mathrm { d } \mathrm { r } } { [ 2 \mathrm { r } + ( e - 1 ) \mathrm { r } ^ { 2 } / \mathrm { r _ { p } } - ( e + 1 ) \mathrm { r } _ { \mathrm { p } } ] ^ { 1 / 2 } } = \sqrt { \mathsf { G } M } \ ( \mathrm { t } - \tau ) .
$$

Consider an elliptical orbit characterized by $0 < e < 1$ . Let us write

$$
{ \boldsymbol { \mathrm { r } } } = { \frac { \mathsf { r } _ { \mathsf { p } } } { 1 - e } } ( 1 - e \cos \mathsf { E } ) ,
$$

where $\mathsf { E }$ is termed the elliptic anomaly. In fact, $\mathsf { E }$ is an angle which varies between $- \pi$ and $+ \pi$ . Moreover, the perihelion point corresponds to $\mathsf E = 0$ , and the aphelion point to $\mathsf { E } = \pi$ . Now,

$$
\mathrm { d } \mathrm { r } = { \frac { \Upsilon _ { \mathrm { p } } } { 1 - e } } e \sin \mathsf { E } { \mathrm { d } \mathsf { E } } ,
$$

whereas

$$
\begin{array} { r c l } { { 2 \displaystyle { \mathrm { r } + ( e - 1 ) \frac { \mathrm { r } ^ { 2 } } { \mathrm { r } _ { \mathrm { p } } } - ( e + 1 ) \mathrm { r } _ { \mathrm { p } } } } } & { { = } } & { { \displaystyle { \frac { \mathrm { r } _ { \mathrm { p } } } { 1 - e } e ^ { 2 } \left( 1 - \cos ^ { 2 } \mathrm { E } \right) } } } \\ { { } } & { { = } } & { { \displaystyle { \frac { \mathrm { r } _ { \mathrm { p } } } { 1 - e } e ^ { 2 } \sin ^ { 2 } \mathrm { E } . } } } \end{array}
$$

Thus, Equation (4.54) reduces to

$$
\int _ { 0 } ^ { \mathsf { E } } ( 1 - e \cos \mathsf { E } ) \mathrm { d } \mathsf { E } = \left( \frac { \mathsf { G } M } { \mathsf { a } ^ { 3 } } \right) ^ { 1 / 2 } ( \mathbf { t } - \mathsf { \tau } ) ,
$$

where $\alpha = \gamma _ { \mathrm { p } } / ( 1 - e )$ . This equation can immediately be integrated to give

$$
\mathsf { E } - e \sin \mathsf { E } = \mathcal { M } .
$$

Here,

$$
\mathcal { M } = \mathfrak { n } \left( \mathfrak { t } - \tau \right)
$$

is termed the mean anomaly, $\mathfrak { n } = 2 \pi / \mathsf { T }$ is the mean orbital angular velocity, and ${ \mathsf { T } } =$ $2 \pi ( { \bf a } ^ { 3 } / { \sf G } M ) ^ { 1 / 2 }$ is the orbital period. The mean anomaly increases uniformly in time at the rate of $2 \pi$ radians every orbital period. Moreover, the perihelion point corresponds to $\mathcal { M } = 0$ , and the aphelion point to $\mathcal { M } = \pi$ . Incidentally, the angle θ, which determines the true angular location of the orbiting object, is sometimes termed the true anomaly. Equation (4.59), which is known as Kepler’s equation, is a transcendental equation that does not possess a simple analytic solution. Fortunately, it is fairly straightforward to solve numerically. For instance, using an iterative approach, if $\mathsf { E } _ { \mathrm { n } }$ is the nth guess then

$$
\mathsf { E } _ { \mathrm { n } + 1 } = \mathcal { M } + e \sin \mathsf { E } _ { \mathrm { n } } .
$$

The above iteration scheme converges very rapidly (except in the limit $e \to 1 .$ ).

Equations (4.51) and (4.55) can be combined to give

$$
\cos \theta = { \frac { \cos \mathsf { E } - e } { 1 - e \cos \mathsf { E } } } .
$$

Thus,

$$
1 + \cos \theta = 2 \cos ^ { 2 } ( \theta / 2 ) = \frac { 2 ( 1 - e ) \cos ^ { 2 } ( \mathrm { E } / 2 ) } { 1 - e \cos \mathrm { E } } ,
$$

and

$$
1 - \cos \Theta = 2 \sin ^ { 2 } ( \theta / 2 ) = \frac { 2 ( 1 + e ) \sin ^ { 2 } ( \mathsf { E } / 2 ) } { 1 - e \cos \mathsf { E } } .
$$

The previous two equations imply that

$$
\tan ( \theta / 2 ) = \left( { \frac { 1 + e } { 1 - e } } \right) ^ { 1 / 2 } \tan ( \mathsf { E } / 2 ) .
$$

We conclude that, in the case of an elliptical orbit, the solution of the Kepler problem reduces to the solution of the following three equations:

$$
\begin{array} { r c l } { { \mathsf { E } - e \sin \mathsf { E } } } & { { = } } & { { \mathcal { M } , } } \\ { { \mathsf { r } } } & { { = } } & { { \mathsf { a } \left( 1 - e \cos \mathsf { E } \right) , } } \\ { { \mathsf { t a n } ( \theta / 2 ) } } & { { = } } & { { \left( \displaystyle \frac { 1 + e } { 1 - e } \right) ^ { 1 / 2 } \tan ( \mathsf { E } / 2 ) . } } \end{array}
$$

Here, $\mathsf { T } = 2 \pi ( \mathbf { a } ^ { 3 } / \mathsf { G } M ) ^ { 1 / 2 }$ and $\mathfrak { a } = \mathfrak { r } _ { \mathfrak { p } } / ( 1 - e )$ . Incidentally, it is clear that if $\mathrm { ~ t ~ } \to \mathrm { ~ t ~ } + \intercal$ then $\mathcal { M }  \mathcal { M } + 2 \pi$ , $\mathsf { E }  \mathsf { E } + 2 \pi$ , and $\theta  \theta + 2 \pi$ →. In other words, the motion is periodic with period T. Note that since the Planets all have low eccentricity orbits, characterized by $e \ll 1$ , Equations (4.66)–(4.68) can be usefully solved via series expansion in e to give

$$
\begin{array} { r c l } { \displaystyle \mathsf { E } } & { = } & { \displaystyle M + e \sin { \mathcal { M } } + \frac { e ^ { 2 } } { 2 } \sin 2 { \mathcal { M } } + \frac { e ^ { 3 } } { 8 } \left( 3 \sin 3 { \mathcal { M } } - \sin { \mathcal { M } } \right) + { \mathcal O } ( e ^ { 4 } ) , } \\ { \displaystyle \theta } & { = } & { \displaystyle { \mathcal { M } } + 2 e \sin { \mathcal { M } } + \frac { 5 e ^ { 2 } } { 4 } \sin 2 { \mathcal { M } } + \frac { e ^ { 3 } } { 1 2 } \left( 1 3 \sin 3 { \mathcal { M } } - 3 \sin { \mathcal { M } } \right) + { \mathcal O } ( e ^ { 4 } ) } \\ { \displaystyle \frac { \Gamma } { \mathbf { a } } } & { = } & { 1 - e \cos { \mathcal { M } } + \displaystyle \frac { e ^ { 2 } } { 2 } \left( 1 - \cos 2 { \mathcal { M } } \right) + \frac { 3 e ^ { 3 } } { 8 } \left( \cos { \mathcal { M } } - \cos 3 { \mathcal { M } } \right) + { \mathcal O } ( e ^ { 4 } ) . } \end{array}
$$

For the case of a parabolic orbit, characterized by $e = 1$ , similar analysis to the above yields:

$$
\begin{array} { r c l } { { \displaystyle { \sf P } + \frac { { \sf P } ^ { 3 } } { 3 } } } & { { = } } & { { \displaystyle \left( \frac { \sf G { \sf M } } { 2 \sf r _ { p } ^ { 3 } } \right) ^ { 1 / 2 } ( { \sf t } - \sf \tau ) , } } \\ { { \sf r } } & { { = } } & { { \sf r _ { p } ( 1 + \sf P ^ { 2 } ) , } } \\ { { \sf t a n ( \theta / 2 ) } } & { { = } } & { { \sf P . } } \end{array}
$$

Here, P is termed the parabolic anomaly, and varies between $- \infty$ and $+ \infty$ , with the perihelion point corresponding to ${ \textsf { P } } = 0$ . Note that Equation (4.72) is a cubic equation, possessing a single real root, which can, in principle, be solved analytically. However, a numerical solution is generally more convenient.

Finally, for the case of a hyperbolic orbit, characterized by $e > 1$ , we obtain:

$$
\begin{array} { r c l } { { \displaystyle e \sinh { \sf H } - { \sf H } } } & { { = } } & { { \displaystyle \left( \frac { { \sf G } { \sf M } } { { \sf a } ^ { 3 } } \right) ^ { 1 / 2 } ( { \sf t } - { \sf \tau } ) , } } \\ { { \mathrm { r } } } & { { = } } & { { \displaystyle { \mathrm { a } \mathrm { \ ( } e \cosh { \sf H } - 1 \mathrm { ) } } , } } \\ { { \displaystyle \tan ( \theta / 2 ) } } & { { = } } & { { \displaystyle \left( \frac { e + 1 } { e - 1 } \right) ^ { 1 / 2 } \mathrm { t a n h } ( { \sf H } / 2 ) . } } \end{array}
$$

Here, H is termed the hyperbolic anomaly, and varies between $- \infty$ and $+ \infty$ , with the perihelion point corresponding to $\mathsf { H } = 0$ . Moreover, $\alpha = \gamma _ { \mathrm { p } } / ( e - 1 )$ . As in the elliptical case, Equation (4.75) is a transcendental equation which is most easily solved numerically.

# 4.10 Orbital Elements

The previous analysis suffices when considering a single planet orbiting around the Sun. However, it becomes inadequate when dealing with multiple planets whose orbital planes and perihelion directions do not necessarily coincide. Incidentally, for the time being, we are neglecting interplanetary gravitational interactions, which allows us to assume that each planet executes an independent Keplerian orbit about the Sun.

Let us characterize all planetary orbits using a common Cartesian coordinate system (X, Y, Z), centered on the Sun—see Fig. 4.4. The X-Y plane defines a reference plane, which is chosen to be the ecliptic plane (i.e., the plane of the Earth’s orbit), with the Z-axis pointing towards the northern ecliptic pole (i.e., the direction normal to the ecliptic plane in a northward sense). Likewise, the X-axis defines a reference direction, which is chosen to point in the direction of the vernal equinox at the same epoch (i.e., the point in the sky at which the ecliptic plane appears to pass through the extension of the Earth’s equatorial plane from south to north). Suppose that the plane of a given planetary orbit is inclined at an angle I to the reference plane. The point at which this orbit crosses the reference plane in the direction of increasing Z is termed its ascending node. The angle $\Omega$ subtended between the reference direction and the direction of the ascending node is termed the longitude of the ascending node. Finally, the angle, $\omega$ , subtended between the direction of the ascending node and the direction of the orbit’s perihelion is termed the argument of the perihelion.

Let us define a second Cartesian coordinate system $( { \mathfrak { x } } , { \mathfrak { y } } , z )$ , also centered on the Sun. Let the $x { - } y$ plane coincide with the plane of a particular orbit, and let the $x$ -axis point towards the orbit’s perihelion point. Clearly, we can transform from the $( { \mathfrak { x } } , { \mathfrak { y } } , z )$ system to the (X, Y, Z) system via a series of three rotations of the coordinate system. First, a rotation through an angle ω about the $z$ -axis (looking down the axis). Second, a rotation through an angle I about the new $x$ -axis. Finally, a rotation through an angle $\Omega$ about the new $z$ -axis. It, thus, follows from standard coordinate transformation theory (see Section A.5) that

![](images/3cbfaa3873efeb5a49b6eb440c0404c97c5fe300507bc5f5414d5e5bfd301ccf.jpg)  
Figure 4.4: A general planetary orbit.

$$
\begin{array} { r l r } { \mathbf { \Phi } } & { = } & { \left( \begin{array} { c c c } { \cos \Omega } & { - \sin \Omega } & { 0 } \\ { \sin \Omega } & { \cos \Omega } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \ I } & { - \sin \ I } \\ { 0 } & { \sin \ I } & { \cos \ I } \end{array} \right) \left( \begin{array} { c c c } { \cos \omega } & { - \sin \omega } & { 0 } \\ { \sin \omega } & { \cos \omega } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c } { 1 } \\ { 0 } \\ { 0 } \end{array} \right) } \end{array}
$$

However, $\mathtt { x } = \mathtt { r } \cos \theta$ , ${ \mathfrak { y } } = { \mathfrak { r } }$ sin θ, and $z = 0$ . Hence,

$$
\begin{array} { l r l } { X } & { = } & { \mathrm { r } \left[ \cos \Omega \cos ( \omega + \theta ) - \sin \Omega \sin ( \omega + \theta ) \cos \mathrm { I } \right] , } \\ { \mathrm { Y } } & { = } & { \mathrm { r } \left[ \sin \Omega \cos ( \omega + \theta ) + \cos \Omega \sin ( \omega + \theta ) \cos \mathrm { I } \right] , } \\ { Z } & { = } & { \mathrm { r } \sin ( \omega + \theta ) \sin \mathrm { I } . } \end{array}
$$

Thus, a general planetary orbit is determined by Equations (4.66)–(4.68) and (4.79)– (4.81), and is therefore parameterized by six orbital elements: the minor radius, a; the eccentricity, $e$ ; the time of perihelion passage, τ; the inclination, I; the longitude of the ascending node, $\Omega$ ; and the argument of the perihelion, ω. (The orbital angular velocity, in radians per year, is $\mathrm { n } = 2 \pi / \mathrm { a } ^ { 3 / 2 }$ , where a is measured in astronomical units—the major radius of the Earth’s orbit is defined to be 1 AU.) The argument of the perihelion is

<table><tr><td>Planet</td><td>a(au)</td><td>e</td><td>入（）</td><td>1（）</td><td>Ω()</td><td>@()</td><td>m/M</td></tr><tr><td>Mercury</td><td>0.3871</td><td>0.20564</td><td>252.25</td><td>7.006</td><td>48.34</td><td>77.46</td><td>1.659 × 10-7</td></tr><tr><td>Venus</td><td>0.7233</td><td>0.00676</td><td>181.98</td><td>3.398</td><td>76.67</td><td>131.77</td><td>2.447 × 10-6</td></tr><tr><td>Earth</td><td>1.0000</td><td>0.01673</td><td>100.47</td><td>0.000</td><td>344.89</td><td>102.93</td><td>3.039 ×10-6</td></tr><tr><td>Mars</td><td>1.5237</td><td>0.09337</td><td>355.43</td><td>1.852</td><td>49.71</td><td>336.08</td><td>3.226 × 10-7</td></tr><tr><td>Jupiter</td><td>5.2025</td><td>0.04854</td><td>34.33</td><td>1.299</td><td>100.29</td><td>14.21</td><td>9.542 × 10-4</td></tr><tr><td> Saturn</td><td>9.5415</td><td>0.05551</td><td>50.08</td><td>2.494</td><td>113.64</td><td>93.00</td><td>2.857 × 10-4</td></tr><tr><td>Uranus</td><td>19.188</td><td>0.04686</td><td>314.20</td><td>0.773</td><td>73.96</td><td>173.41</td><td>4.353 × 10-5</td></tr><tr><td>Neptune</td><td>30.070</td><td>0.00895</td><td>304.22</td><td>1.770</td><td>131.79</td><td>46.00</td><td>5.165 × 10-5</td></tr></table>

Table 4.1: Orbital elements of the major planets at J2000. Here, a is the major radius (in astronomical units), e the eccentricity, $\bar { \lambda } _ { 0 }$ the mean longitude at epoch, I the inclination, $\Omega$ the longitude of the ascending node, and $\varpi$ the longitude of the perihelion. The last column gives the mass of each planet as a fraction of the solar mass. [E.M. Standish, et al., Orbital Ephemeris of the Sun, Moon, and Planets, in Explanatory Supplement to the Astronomical Almanac, ed. P.K. Seidelmann (University Science Books, Mill Valley CA, 1992.)]

sometimes replaced by

$$
\varpi = \Omega + \omega ,
$$

which is termed the longitude of the perihelion. Likewise, the time of perihelion passage, τ, is often replaced by the mean longitude at $\mathrm { t } = 0$ , where the mean longitude is defined

$$
{ \bar { \lambda } } = \varpi + { \cal M } = \varpi + { \sf n } { \left( { \sf t } - { \sf \tau } \right) } .
$$

Thus, if $\bar { \lambda } _ { 0 }$ denotes the mean longitude at epoch $( \mathrm { t } = 0 )$ , then

$$
\bar { \lambda } = \bar { \lambda } _ { 0 } + \mathfrak { n } \mathfrak { t } ,
$$

where $\bar { \lambda } _ { 0 } = \varpi - \mathfrak { n } \tau$ . The orbital elements of the major planets at the epoch J2000 (i.e., at 00:00 UT on January 1st, 2000) are given in Table 4.1.

The heliocentric (i.e., as seen from the Sun) position of a planet is most conveniently expressed in terms of its ecliptic longitude, $\lambda _ { \perp }$ , and ecliptic latitude, $\beta$ . This type of longitude and latitude is referred to the ecliptic plane, with the Sun as the origin. It follows that

$$
\begin{array} { l } { \displaystyle \tan \lambda ~ = ~ \frac { \Upsilon } { \chi } , } \\ { \displaystyle \sin \beta ~ = ~ \frac { Z } { \sqrt { X ^ { 2 } + Y ^ { 2 } } } , } \end{array}
$$

where (X, Y, Z) are the heliocentric Cartesian coordinates of the planet.

# 4.11 Binary Star Systems

Approximately half of the stars in our galaxy are members of so-called binary star systems. Such systems consist of two stars, of $\mathrm { { m a s s ~ m } } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , and position vectors $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 2 }$ , respectively, orbiting about their common center of mass. The distance separating the stars is always much less than the distance to the nearest neighbor star. Hence, a binary star system can be treated as a two-body dynamical system to a very good approximation.

In a binary star system, the gravitational force which the first star exerts on the second is

$$
\mathbf { f } = - { \frac { \mathbf { G } { \mathfrak { m } } _ { 1 } { \mathfrak { m } } _ { 2 } } { \mathfrak { r } ^ { 3 } } } \mathbf { r } ,
$$

where $\mathbf { r } = \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 }$ . As we have seen, a two-body system can be reduced to an equivalent onebody system whose equation of motion is of the form (2.76), where $\mu = \eta _ { 1 } \eta _ { 2 } / ( \eta _ { 1 } + \eta _ { 2 } )$ . Hence, in this particular case, we can write

$$
\frac { { \mathfrak { m } } _ { 1 } { \mathfrak { m } } _ { 2 } } { { \mathfrak { m } } _ { 1 } + { \mathfrak { m } } _ { 2 } } \frac { \mathrm { d } ^ { 2 } { \mathbf { r } } } { \mathrm { d } { \mathrm { t } } ^ { 2 } } = - \frac { \textsf { G m } _ { 1 } { \mathfrak { m } } _ { 2 } } { { \mathfrak { r } } ^ { 3 } } { \mathbf { r } } ,
$$

which gives

$$
{ \frac { \mathrm { d } ^ { 2 } \mathbf { r } } { \mathrm { d t } ^ { 2 } } } = - { \frac { \mathrm { G } M } { \mathrm { r } ^ { 3 } } } \mathbf { r } ,
$$

where

$$
\begin{array} { r } { M = \mathfrak { m } _ { 1 } + \mathfrak { m } _ { 2 } . } \end{array}
$$

Equation (4.89) is identical to Equation (4.2), which we have already solved. Hence, we can immediately write down the solution:

$$
{ \bf r } = ( { \mathrm r } \cos \theta , { \mathrm r } \sin \theta , 0 ) ,
$$

where

$$
\displaystyle \boldsymbol { \mathrm { r } } = \frac { \mathbf { a } \left( 1 - e ^ { 2 } \right) } { 1 - e \ \cos \theta } ,
$$

and

$$
{ \frac { { \mathrm { d } } \theta } { { \mathrm { d t } } } } = { \frac { \mathrm { h } } { \Gamma ^ { 2 } } } ,
$$

with

$$
\mathbf { a } = { \frac { \mathsf { h } ^ { 2 } } { ( 1 - e ^ { 2 } ) \mathsf { G } M } } .
$$

Here, h is a constant, and we have aligned our Cartesian axes so that the plane of the orbit coincides with the $x { - } y$ plane. According to the above solution, the second star executes a Keplerian elliptical orbit, with major radius a and eccentricity $e$ , relative to the first star, and vice versa. From Equation (4.33), the period of revolution, $\mathsf { T }$ , is given by

$$
\mathsf { T } = \sqrt { \frac { 4 \pi ^ { 2 } \mathsf { a } ^ { 3 } } { \mathsf { G } M } } .
$$

![](images/5ec18410d10e502127e6bf7c61ddad2bd99c9e440378f71edbff1d3f58f24913.jpg)  
Figure 4.5: An example binary star orbit.

Moreover, if $\mathfrak { n } = 2 \pi / \mathsf { T }$ then

$$
\mathfrak { n } = \frac { \sqrt { \mathsf { G } M } } { \mathbf { a } ^ { 3 / 2 } } .
$$

In the inertial frame of reference whose origin always coincides with the center of mass—the so-called center of mass frame—the position vectors of the two stars are

$$
\begin{array} { r c l } { \mathbf { r } _ { 1 } } & { = } & { \displaystyle - \frac { { \bf m } _ { 2 } } { { \bf m } _ { 1 } + { \bf m } _ { 2 } } \mathbf { r } , } \\ { \mathbf { r } _ { 2 } } & { = } & { \displaystyle \frac { { \bf m } _ { 1 } } { { \bf m } _ { 1 } + { \bf m } _ { 2 } } \mathbf { r } , } \end{array}
$$

where r is specified above. Figure 4.5 shows an example binary star orbit, in the center of mass frame, calculated with $\mathfrak { m } _ { 1 } / \mathfrak { m } _ { 2 } = 0 . 5$ and $e = 0 . 2$ . Here, the triangles and squares denote the positions of the first and second star, respectively (which are always diagrammatically opposite one another, relative to the origin, as indicated by the arrows). It can be seen that both stars execute elliptical orbits about their common center of mass.

Binary star systems have been very useful to astronomers, since it is possible to determine the masses of both stars in such a system by careful observation. The sum of the masses of the two stars, $M = { \mathfrak { m } } _ { 1 } + { \mathfrak { m } } _ { 2 }$ , can be found from Equation (4.95) after a measurement of the major radius, a (which is the mean of the greatest and smallest distance apart of the two stars during their orbit), and the orbital period, T . The ratio of the masses of the two stars, ${ \mathfrak { m } } _ { 1 } / { \mathfrak { m } } _ { 2 }$ , can be determined from Equations (4.97) and (4.98) by observing the fixed ratio of the relative distances of the two stars from the common center of mass about which they both appear to rotate. Obviously, given the sum of the masses, and the ratio of the masses, the individual masses themselves can then be calculated.

# 4.12 Exercises

4.1. Halley’s comet has an orbital eccentricity of $e = 0 . 9 6 7$ and a perihelion distance of 55, 000, 000 miles. Find the orbital period, and the comet’s speed at perihelion and aphelion.

4.2. A comet is first seen at a distance of d astronomical units (1 astronomical unit is the mean Earth-Sun distance) from the Sun, and is traveling with a speed of $\mathsf { q }$ times the Earth’s mean speed. Show that the orbit of the comet is hyperbolic, parabolic, or elliptical, depending on whether the quantity ${ \mathsf q } ^ { 2 } { \mathsf d }$ is greater than, equal to, or less than 2, respectively.

4.3. Consider a planet in a Keplerian orbit of major radius a and eccentricity e about the Sun. Suppose that the eccentricity of the orbit is small (i.e., $0 < e \ll 1 \AA$ ), as is indeed the case for all of the planets except Mercury and Pluto. Demonstrate that, to first-order in $e$ , the orbit can be approximated as a circle whose center is shifted a distance e a from the Sun, and that the planet’s angular motion appears uniform when viewed from a point (called the Equant) which is shifted a distance 2 e a from the Sun, in the same direction as the center of the circle. This theorem is the basis of the Ptolomaic model of planetary motion.

4.4. How long (in days) does it take the Sun-Earth radius vector to rotate through $9 0 ^ { \circ }$ , starting at the perihelion point? How long does it take starting at the aphelion point? The period and eccentricity of the Earth’s orbit are $\mathsf { T } = 3 6 5 . 2 4$ days, and $e = 0 . 0 1 6 7 3$ , respectively.

4.5. Solve the Kepler problem for a parabolic orbit to obtain Equations (4.72)–(4.74).

4.6. Solve the Kepler problem for a hyperbolic orbit to obtain Equations (4.75)–(4.77).

4.7. A comet is in a parabolic orbit lying in the plane of the Earth’s orbit. Regarding the Earth’s orbit as a circle of radius $\mathbf { a }$ , show that the points where the comet intersects the Earth’s orbit are given by

$$
\cos \theta = - 1 + \frac { 2 \mathfrak { p } } { \mathfrak { a } } ,
$$

where p is the perihelion distance of the comet, defined at $\theta = 0$ . Show that the time interval that the comet remains inside the Earth’s orbit is the faction

$$
\frac { 2 ^ { 1 / 2 } } { 3 \pi } \left( \frac { 2 \mathfrak { p } } { \mathfrak { a } } + 1 \right) \left( 1 - \frac { \mathfrak { p } } { \mathfrak { a } } \right) ^ { 1 / 2 }
$$

of a year, and that the maximum value of this time interval is $2 / 3 \pi$ year, or about 11 weeks.

# 5 Orbits in Central Force-Fields

# 5.1 Introduction

This chapter examines the motion of a celestial body in a general central potential (i.e., a potential that is a function of r, but does not necessarily vary as $1 / \mathfrak { r } )$ .

# 5.2 Motion in a General Central Force-Field

Consider the motion of an object in a general (attractive) central force-field characterized by the potential energy per unit mass function $\mathsf { V } ( \mathsf { r } )$ . Since the force-field is central, it still remains true that

$$
\mathbf { h } = \mathbf { r } ^ { 2 } { \dot { \boldsymbol { \theta } } }
$$

is a constant of the motion (see Section 4.5). As is easily demonstrated, Equation (4.28) generalizes to

$$
\frac { \mathrm { d } ^ { 2 } \mathrm { u } } { \mathrm { d } \theta ^ { 2 } } + \mathrm { u } = - \frac { 1 } { \mathrm { h } ^ { 2 } } \frac { \mathrm { d } \mathrm { V } } { \mathrm { d } \mathrm { u } } ,
$$

where $\mathfrak { u } = \mathfrak { r } ^ { - 1 }$ .

Suppose, for instance, that we wish to find the potential $\mathsf { V } ( \mathsf { r } )$ that causes an object to execute the spiral orbit

$$
{ \boldsymbol { \Upsilon } } = { \boldsymbol { \Upsilon } } _ { 0 } \theta ^ { 2 } .
$$

Substitution of $\mathfrak { u } = ( \mathfrak { r } _ { 0 } \theta ^ { 2 } ) ^ { - 1 }$ into Equation (5.2) yields

$$
\frac { \mathrm { d } \mathsf { V } } { \mathrm { d u } } = - \mathsf { h } ^ { 2 } \left( 6 \mathsf { r } _ { 0 } \mathsf { u } ^ { 2 } + \mathsf { u } \right) .
$$

Integrating, we obtain

$$
{ \sf V } ( { \bf u } ) = - { \sf h } ^ { 2 } \left( 2 { \sf r } _ { 0 } { \sf u } ^ { 3 } + \frac { { \sf u } ^ { 2 } } { 2 } \right) ,
$$

or

$$
V ( \boldsymbol { \mathbf { r } } ) = - \boldsymbol { \mathbf { \acute { h } } } ^ { 2 } \left( \frac { 2 \boldsymbol { \mathbf { r } } _ { 0 } } { \boldsymbol { \mathbf { r } } ^ { 3 } } + \frac { 1 } { 2 \boldsymbol { \mathbf { r } } ^ { 2 } } \right) .
$$

In other words, the spiral pattern (5.3) is obtained from a mixture of an inverse-square and inverse-cube potential.

# 5.3 Motion in a Nearly Circular Orbit

In principle, a circular orbit is a possible orbit for any attractive central force. However, not all such forces result in stable circular orbits. Let us now consider the stability of circular

orbits in a general central force-field. Equation (4.25) generalizes to

$$
{ \ddot { \mathfrak { r } } } - { \frac { { \mathrm { h } } ^ { 2 } } { { \mathrm { r } } ^ { 3 } } } = { \mathfrak { r } } ( { \mathfrak { r } } ) ,
$$

where $\mathsf { f } ( \mathsf { r } )$ is the radial force per unit mass. For a circular orbit, ${ \ddot { r } } = 0$ , and the above equation reduces to

$$
- \frac { \mathrm { l } ^ { 2 } } { \mathrm { r } _ { c } ^ { 3 } } = \mathbf { f } ( \mathbf { r } _ { c } ) ,
$$

where $\boldsymbol { \mathrm { r } } _ { \mathrm { c } }$ is the radius of the orbit.

Let us now consider small departures from circularity. Let

$$
\boldsymbol { \mathrm { x } } = \boldsymbol { \mathrm { r } } - \boldsymbol { \mathrm { r } } _ { \mathrm { c } } .
$$

Equation (5.7) can be written

$$
{ \ddot { \mathfrak { x } } } - { \frac { \mathsf { h } ^ { 2 } } { ( \mathsf { r } _ { \mathfrak { c } } + \mathfrak { x } ) ^ { 3 } } } = \mathsf { f } ( \mathsf { r } _ { \mathfrak { c } } + \mathfrak { x } ) .
$$

Expanding the two terms involving $\boldsymbol { \Upsilon } _ { \mathrm { c } } + \boldsymbol { x }$ as power series in ${ \boldsymbol { x } } / { \boldsymbol { \mathsf { r } } _ { \mathrm { c } } }$ , and keeping all terms up to first order, we obtain

$$
\ddot { \mathbf { x } } - \frac { \mathrm { h } ^ { 2 } } { \mathrm { r } _ { c } ^ { 3 } } \left( 1 - 3 \frac { \mathbf { \nabla } x } { \mathrm { r } _ { \mathrm { c } } } \right) = \mathbf { f } ( \mathbf { r } _ { \mathrm { c } } ) + \mathbf { f } ^ { \prime } ( \mathbf { r } _ { \mathrm { c } } ) \mathbf { x } ,
$$

where ′ denotes a derivative. Making use of Equation (5.8), the above equation reduces to

$$
\ddot { \mathbf { x } } + \left[ - \frac { 3 \mathsf { f } ( \mathsf { r } _ { \mathrm { c } } ) } { \mathsf { r } _ { \mathrm { c } } } - \mathsf { f } ^ { \prime } ( \mathsf { r } _ { \mathrm { c } } ) \right] \mathbf { x } = 0 .
$$

If the term in square brackets is positive then we obtain a simple harmonic equation, which we already know has bounded solutions (see Section 2.8)—i.e., the orbit is stable to small perturbations. On the other hand, if the term is square brackets is negative then we obtain an equation whose solutions grow exponentially in time (see Section 2.8)—i.e., the orbit is unstable to small oscillations. Thus, the stability criterion for a circular orbit of radius $\boldsymbol { \mathrm { r } } _ { \mathrm { c } }$ in a central force-field characterized by a radial force (per unit mass) function ${ \sf f } ( { \sf r } )$ i s

$$
\mathsf { f } \bigl ( \mathsf { r } _ { \mathrm { c } } \bigr ) + \frac { \mathsf { r } _ { \mathrm { c } } } { 3 } \mathsf { f } ^ { \prime } \bigl ( \mathsf { r } _ { \mathrm { c } } \bigr ) < 0 .
$$

For example, consider an attractive power-law force function of the form

$$
\mathsf { f } ( \mathsf { c } ) = - \mathsf { c } \mathsf { r } ^ { \mathsf { n } } ,
$$

where ${ \mathfrak { c } } > 0$ . Substituting into the above stability criterion, we obtain

$$
- \mathbf { c } \mathsf { r } _ { \mathrm { c } } ^ { \mathrm { n } } - \frac { \mathbf { c } \mathsf { n } } { 3 } \mathsf { r } _ { \mathrm { c } } ^ { \mathrm { n } } < 0 ,
$$

or

$$
{ \mathfrak { n } } > - 3 .
$$

We conclude that circular orbits in attractive central force-fields that decay faster than $\Upsilon ^ { - 3 }$ are unstable. The case ${ \mathfrak { n } } = - 3$ is special, since the first-order terms in the expansion of Equation (5.10) cancel out exactly, and it is necessary to retain the second-order terms. Doing this, it is easily demonstrated that circular orbits are also unstable for inverse-cube $( \mathfrak { n } = - 3 )$ ) forces.

An apsis (plural, apsides) is a point in an orbit at which the radial distance, r, assumes either a maximum or a minimum value. Thus, the perihelion and aphelion points are the apsides of planetary orbits. The angle through which the radius vector rotates in going between two consecutive apsides is called the apsidal angle. Thus, the apsidal angle for elliptical orbits in an inverse-square force-field is $\pi$ .

For the case of stable nearly circular orbits, we have seen that r oscillates sinusoidally about its mean value, $\boldsymbol { \mathrm { r } } _ { \mathrm { c } }$ . Indeed, it is clear from Equation (5.12) that the period of the oscillation is

$$
\mathsf { T } = \frac { 2 \pi } { [ - 3 \mathsf { f } ( \mathsf { r } _ { \mathrm { c } } ) / \mathsf { r } _ { \mathrm { c } } - \mathsf { f } ^ { \prime } ( \mathsf { r } _ { \mathrm { c } } ) ] ^ { 1 / 2 } } .
$$

The apsidal angle is the amount by which $\theta$ increases in going between a maximum and a minimum of r. The time taken to achieve this is clearly $\mathsf { T } / 2$ . Now, $\dot { \Theta } = \mathsf { h } / \mathsf { r } ^ { 2 }$ , where $\mathrm { \hslash }$ is a constant of the motion, and $\boldsymbol { \mathsf { r } }$ is almost constant. Thus, $\dot { \theta }$ is approximately constant. In fact,

$$
\dot { \theta } \simeq \frac { \mathrm { h } } { \mathrm { r } _ { \mathrm { c } } ^ { 2 } } = \left[ - \frac { \mathrm { f ( r _ { c } ) } } { \mathrm { r _ { c } } } \right] ^ { 1 / 2 } ,
$$

where use has been made of Equation (5.8). Thus, the apsidal angle, $\psi$ , is given by

$$
\Psi = \frac { \sf T } { 2 } \dot { \theta } = \pi \left[ 3 + \sf r _ { c } \frac { { \sf f ^ { \prime } ( \vec { r } _ { c } ) } } { \sf f \big ( \vec { r } _ { c } \big ) } \right] ^ { - 1 / 2 }
$$

For the case of attractive power-law central forces of the form $\mathsf { f } ( \mathsf { r } ) \mathsf { \Lambda } = - \mathsf { c } \mathsf { r } ^ { \mathsf { n } }$ , where ${ \mathfrak { c } } > 0$ , the apsidal angle becomes

$$
\Psi = \frac { \pi } { ( 3 + \mathsf { n } ) ^ { 1 / 2 } } .
$$

Now, it should be clear that if an orbit is going to close on itself then the apsidal angle needs to be a rational fraction of $2 \pi$ . There are, in fact, only two small integer values of the power-law index, n, for which this is the case. As we have seen, for an inverse-square force law (i.e., ${ \mathfrak { n } } = - 2 )$ ), the apsidal angle is $\pi$ . For a linear force law (i.e., ${ \mathfrak { n } } = 1 \mathbf { \cdot }$ ), the apsidal angle is $\pi / 2$ . However, for quadratic (i.e., ${ \mathfrak { n } } = 2 { \mathfrak { r } }$ ) or cubic (i.e., ${ \mathfrak { n } } = 3 { \mathfrak { . } }$ ) force laws, the apsidal angle is an irrational fraction of $2 \pi$ , which means that non-circular orbits in such force-fields never close on themselves.

# 5.4 Perihelion Precession of the Planets

The Solar System consists of eight major planets (Mercury to Neptune) moving around the Sun in slightly elliptical orbits that are approximately co-planar with one another. According to Chapter 4, if we neglect the relatively weak interplanetary gravitational interactions then the perihelia of the various planets (i.e., the points on their orbits at which they are closest to the Sun) remain fixed in space. However, once these interactions are taken into account, it turns out that the planetary perihelia all slowly precess around the Sun. We can calculate the approximate rate of perihelion precession of a given planet by treating the other planets as uniform concentric rings, centered on the Sun, of mass equal to the planetary mass, and radius equal to the mean orbital radius. This method of calculation, which is due to Gauss, is equivalent to averaging the interplanetary gravitational interactions over the orbits of the other planets. It is reasonable to do this because the precession period in question is very much longer than the orbital period of any planet in the Solar System. Thus, by treating the other planets as rings, we can calculate the mean gravitational perturbation due to these planets, and, thereby, determine the desired precession rate.

We can conveniently index the planets in the Solar System such that Mercury is planet 1, and Neptune planet 8. Let the $M _ { \mathrm { i } }$ and the $\mathsf { R } _ { \mathrm { i } } ,$ for $i = 1 , 8$ , be the planetary masses and orbital radii, respectively. Furthermore, let $M _ { 0 }$ be the mass of the Sun. It follows, from Section 3.7, that the gravitational potential generated at the ith planet by the Sun and the other planets is

$$
\begin{array} { r c l } { { \Phi ( \mathrm { { R } } _ { \mathrm { { i } } } ) } } & { { = } } & { { \displaystyle - \frac { \mathsf { G } \ M _ { 0 } } { \mathrm { R } _ { \mathrm { i } } } - \mathsf { G } \sum _ { \mathrm { j } < \mathrm { i } } \frac { M _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \left[ 1 + \frac { 1 } { 4 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 2 } + \frac { 9 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 4 } + \cdots \right] } } \\ { { } } & { { } } & { { \displaystyle - \mathsf { G } \sum _ { \mathrm { j } > \mathrm { i } } \frac { M _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { j } } } \left[ 1 + \frac { 1 } { 4 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 2 } + \frac { 9 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 4 } + \cdots \right] . } } \end{array}
$$

Now, the radial force per unit mass acting on the ith planet is written $\mathsf { f } ( \mathsf { R } _ { \mathrm { i } } ) = - \mathrm { d } \Phi ( \mathsf { R } _ { \mathrm { i } } ) / \mathrm { d } \mathsf { r } _ { \mathrm { i } }$ , giving

$$
\begin{array} { r c l } { { \mathrm { f ( R _ { i } ) } } } & { { = } } & { { \displaystyle - \frac { \mathsf { G } M _ { 0 } } { \mathsf { R } _ { i } ^ { 2 } } - \frac { \mathsf { G } } { \mathsf { R } _ { i } ^ { 2 } } \sum _ { j < i } M _ { j } \left[ 1 + \frac { 3 } { 4 } \left( \frac { \mathsf { R } _ { \mathrm { j } } } { \mathsf { R } _ { \mathrm { i } } } \right) ^ { 2 } + \frac { 4 5 } { 6 4 } \left( \frac { \mathsf { R } _ { \mathrm { j } } } { \mathsf { R } _ { \mathrm { i } } } \right) ^ { 4 } + \cdots \right] } } \\ { { } } & { { } } & { { \displaystyle + \frac { \mathsf { G } } { \mathsf { R } _ { \mathrm { i } } ^ { 2 } } \sum _ { j > i } M _ { \mathrm { j } } \left( \frac { \mathsf { R } _ { \mathrm { i } } } { \mathsf { R } _ { \mathrm { j } } } \right) \left[ \frac { 1 } { 2 } \left( \frac { \mathsf { R } _ { \mathrm { i } } } { \mathsf { R } _ { \mathrm { j } } } \right) ^ { 2 } + \frac { 9 } { 1 6 } \left( \frac { \mathsf { R } _ { \mathrm { i } } } { \mathsf { R } _ { \mathrm { j } } } \right) ^ { 4 } + \cdots \right] . } } \end{array}
$$

Hence, we obtain

$$
\mathrm { R _ { i } \Delta f ^ { \prime } ( R _ { i } ) \ = \ \frac { 2 \ G \ M _ { 0 } } { R _ { i } ^ { 2 } } + \frac { G } { R _ { i } ^ { 2 } } \sum _ { j < i } M _ { j } \left[ 2 + 3 \left( \frac { R _ { j } } { R _ { i } } \right) ^ { 2 } + \frac { 1 3 5 } { 3 2 } \left( \frac { R _ { j } } { R _ { i } } \right) ^ { 4 } + \cdots \right] }
$$

$$
\mathrm { + \frac { G } { R _ { i } ^ { 2 } } \sum _ { j > i } M _ { j } \left( \frac { R _ { i } } { R _ { j } } \right) \left[ \frac { 1 } { 2 } \left( \frac { R _ { i } } { R _ { j } } \right) ^ { 2 } + \frac { 2 7 } { 1 6 } \left( \frac { R _ { i } } { R _ { j } } \right) ^ { 4 } + \cdot \cdot \cdot \right] , }
$$

where $\ l ^ { \prime } \equiv \mathrm { d } / \mathrm { d } \ r { \ r }$ . It follows that

$$
{ \begin{array} { r l } & { { 3 } + { \frac { \mathrm { R _ { \mathrm { i } } \mathrm { f ^ { \prime } } ( \mathrm { R _ { i } } ) } } { \mathrm { f } ( \mathrm { R _ { i } } ) } } { \displaystyle { \int } ^ { - 1 / 2 } } = 1 + { \frac { 3 } { 4 } } \sum _ { \mathrm { j < i } } ( { \frac { \mathrm { M _ { \mathrm { j } } } } { \mathrm { M _ { \mathrm { o } } } } } ) ( { \frac { \mathrm { R _ { \mathrm { j } } } } { \mathrm { R _ { i } } } } ) ^ { 2 } [ 1 + { \frac { 1 5 } { 8 } } ( { \frac { \mathrm { R _ { \mathrm { j } } } } { \mathrm { R _ { i } } } } ) ^ { 2 } + { \frac { 1 7 5 } { 6 4 } } ( { \frac { \mathrm { R _ { \mathrm { j } } } } { \mathrm { R _ { i } } } } ) ^ { 4 } + \cdot \cdot \cdot \cdot } \\ & { { \mathrm { i } } { \frac { { 3 } } { 4 } } \sum _ { \mathrm { j > i } } ( { \frac { \mathrm { M _ { \mathrm { j } } } } { \mathrm { M _ { \mathrm { o } } } } } ) ( { \frac { \mathrm { R _ { \mathrm { i } } } } { \mathrm { R _ { j } } } } ) ^ { 3 } [ 1 + { \frac { 1 5 } { 8 } } ( { \frac { \mathrm { R _ { \mathrm { i } } } } { \mathrm { R _ { j } } } } ) ^ { 2 } + { \frac { 1 7 5 } { 6 4 } } ( { \frac { \mathrm { R _ { i } } } { \mathrm { R _ { j } } } } ) ^ { 4 } + \cdot \cdot \cdot ] . } \end{array} }
$$

Thus, according to Equation (5.19), the apsidal angle for the ith planet is

$$
\begin{array} { r l r } { \Psi _ { \mathrm { i } } } & { = } & { \pi + { \frac { 3 \pi } { 4 } } \displaystyle \sum _ { \mathrm { j < i } } \left( \frac { { \bf M } _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { { \bf R } _ { \mathrm { j } } } { { \bf R } _ { \mathrm { i } } } \right) ^ { 2 } \left[ 1 + { \frac { 1 5 } { 8 } } \left( \frac { { \bf R } _ { \mathrm { j } } } { { \bf R } _ { \mathrm { i } } } \right) ^ { 2 } + { \frac { 1 7 5 } { 6 4 } } \left( \frac { { \bf R } _ { \mathrm { j } } } { { \bf R } _ { \mathrm { i } } } \right) ^ { 4 } + \cdot \cdot \cdot \right] } \\ & { } & { + { \frac { 3 \pi } { 4 } } \displaystyle \sum _ { \mathrm { j > i } } \left( \frac { { \bf M } _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { { \bf R } _ { \mathrm { i } } } { { \bf R } _ { \mathrm { j } } } \right) ^ { 3 } \left[ 1 + { \frac { 1 5 } { 8 } } \left( \frac { { \bf R } _ { \mathrm { i } } } { { \bf R } _ { \mathrm { j } } } \right) ^ { 2 } + { \frac { 1 7 5 } { 6 4 } } \left( \frac { { \bf R } _ { \mathrm { i } } } { { \bf R } _ { \mathrm { j } } } \right) ^ { 4 } + \cdot \cdot \cdot \right] . } \end{array}
$$

Hence, the perihelion of the ith planet advances by

$$
\begin{array} { r c l } { \delta \Psi _ { \mathrm { i } } } & { = } & { \displaystyle \frac { 3 \pi } { 2 } \sum _ { \mathrm { j < i } } \left( \frac { M _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 2 } \left[ 1 + \frac { 1 5 } { 8 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 2 } + \frac { 1 7 5 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 4 } + \cdots \right] } \\ & & { \displaystyle + \frac { 3 \pi } { 2 } \sum _ { \mathrm { j > i } } \left( \frac { M _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 3 } \left[ 1 + \frac { 1 5 } { 8 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 2 } + \frac { 1 7 5 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 4 } + \cdots \right] } \end{array}
$$

radians per revolution around the Sun. Now, the time for one revolution is ${ \sf T } _ { \mathrm { i } } = 2 \pi / \omega _ { \mathrm { i } }$ , where $\omega _ { \mathrm { i } } ^ { 2 } = \mathsf { G } M _ { 0 } / \mathsf { R } _ { \mathrm { i } } ^ { 3 }$ . Thus, the rate of perihelion precession, in arc seconds per year, is given by

$$
\begin{array} { r c l } { \delta \dot { \Psi } _ { \mathrm { i } } } & { = } & { \frac { 7 5 } { \mathrm { T } _ { \mathrm { i } } \left( \mathrm { y r } \right) } \left\{ \sum _ { \mathrm { j } < \mathrm { i } } \left( \frac { M _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 2 } \left[ 1 + \frac { 1 5 } { 8 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 2 } + \frac { 1 7 5 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { j } } } { \mathrm { R } _ { \mathrm { i } } } \right) ^ { 4 } + \cdots \right] \right. } \\ & & { \left. + \sum _ { \mathrm { j } > \mathrm { i } } \left( \frac { M _ { \mathrm { j } } } { M _ { 0 } } \right) \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 3 } \left[ 1 + \frac { 1 5 } { 8 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 2 } + \frac { 1 7 5 } { 6 4 } \left( \frac { \mathrm { R } _ { \mathrm { i } } } { \mathrm { R } _ { \mathrm { j } } } \right) ^ { 4 } + \cdots \right] \right\} . } \end{array}
$$

Table 5.2 and Figure 5.1 compare the observed perihelion precession rates with the theoretical rates calculated from Equation (5.27) and the planetary data given in Table 5.1. It can be seen that there is excellent agreement between the two, except for the planet Venus. The main reason for this is that Venus has an unusually low eccentricity $\left( e \right. =$ 0.0068), which renders its perihelion point extremely sensitive to small perturbations.

<table><tr><td>Planet</td><td>M/Mo</td><td>T(yr)</td><td>R(au)</td></tr><tr><td>Mercury</td><td>1.66 × 10-7</td><td>0.241</td><td>0.387</td></tr><tr><td>Venus</td><td>2.45 × 10-6</td><td>0.615</td><td>0.723</td></tr><tr><td>Earth</td><td>3.04 × 10-6</td><td>1.000</td><td>1.00</td></tr><tr><td>Mars</td><td>3.23 × 10-7</td><td>1.881</td><td>1.52</td></tr><tr><td>Jupiter</td><td>9.55 × 10-4</td><td>11.86</td><td>5.20</td></tr><tr><td>Saturn</td><td>2.86 × 10-4</td><td>29.46</td><td>9.54</td></tr><tr><td>Uranus</td><td>4.36 × 10-5</td><td>84.01</td><td>19.19</td></tr><tr><td>Neptune</td><td>5.18 × 10-5</td><td>164.8</td><td>30.07</td></tr></table>

<table><tr><td>Planet</td><td>(84)obs</td><td>(s4)th</td></tr><tr><td>Mercury</td><td>5.75</td><td>5.50</td></tr><tr><td>Venus</td><td>2.04</td><td>10.75</td></tr><tr><td>Earth</td><td>11.45</td><td>11.87</td></tr><tr><td>Mars</td><td>16.28</td><td>17.60</td></tr><tr><td>Jupiter</td><td>6.55</td><td>7.42</td></tr><tr><td> Saturn</td><td>19.50</td><td>18.36</td></tr><tr><td>Uranus</td><td>3.34</td><td>2.72</td></tr><tr><td>Neptune</td><td>0.36</td><td>0.65</td></tr></table>

![](images/6452b94252c5b731ae2801d649bf7b464383ccc16f3de4b8aafcefe61b6912f6.jpg)  
Figure 5.1: The triangular points show the observed perihelion precession rates of the major planets in the Solar System, whereas the square points show the theoretical rates calculated from Equation (5.27) and Table 5.1. The precession rates are in arc seconds per year.

# 5.5 Perihelion Precession of Mercury

If the calculation described in the previous section is carried out more accurately, taking into account the slight eccentricities of the planetary orbits, as well as their small mutual inclinations, and retaining many more terms in the expansions (3.70) and (3.72), then the perihelion precession rate of the planet Mercury is found to be 5.32 arc seconds per year.1 However, the observed precession rate is 5.75 arc seconds per year. It turns out that the cause of this discrepancy is the general relativistic correction to Newtonian gravity.

General relativity gives rise to a small correction to the force per unit mass exerted by the Sun (mass M) on a planet in a circular orbit of radius $\boldsymbol { \mathsf { r } } _ { : }$ , and angular momentum per unit mass h. This correction is due to the curvature of space in the immediate vicinity of the Sun. In fact, the modified formula for f is

$$
\mathsf { f } \simeq - \frac { \mathsf { G } M } { \mathsf { r } ^ { 2 } } - \frac { 3 \mathsf { G } M \mathsf { h } ^ { 2 } } { \mathsf { c } ^ { 2 } \mathsf { r } ^ { 4 } } ,
$$

where c is the velocity of light in vacuum. It follows that

$$
\frac { \mathrm { \Delta r f ^ { \prime } } } { \mathrm { \Delta f } } = - 2 \left( 1 + \frac { 3 \mathrm { h } ^ { 2 } } { \mathrm { c } ^ { 2 } \mathrm { r } ^ { 2 } } + \cdot \cdot \cdot \right) .
$$

Hence, from Equation (5.19), the apsidal angle is

$$
\Psi \simeq \pi \left( 1 + \frac { 3 { \mathsf { h } } ^ { 2 } } { \mathsf { c } ^ { 2 } \mathsf { r } ^ { 2 } } \right) .
$$

Thus, the perihelion advances by

$$
\delta \Psi \simeq { \frac { 6 \pi \mathrm { G } M } { \mathrm { c } ^ { 2 } \mathrm { r } } }
$$

radians per revolution due to the general relativistic correction to Newtonian gravity. Here, use has been made of $ { \mathsf { h } } ^ { 2 } = \mathsf { G } M  { \mathsf { r } }$ . It follows that the rate of perihelion precession due to the general relativistic correction is

$$
\delta \dot { \Psi } \simeq \frac { 0 . 0 3 8 3 } { \mathrm { \textrm { R T } } }
$$

arc seconds per year, where R is the mean orbital radius in mean Earth orbital radii (i.e., astronomical units), and $\intercal$ is the orbital period in years. Hence, from Table 5.1, the general relativistic contribution to $\delta \dot { \boldsymbol { \psi } }$ for Mercury is 0.41 arc seconds per year. It is easily demonstrated that the corresponding contribution is negligible for the other planets in the Solar System. If the above calculation is carried out sightly more accurately, taking the eccentricity of Mercury’s orbit into account, then the general relativistic contribution to $\delta \dot { \boldsymbol { \psi } }$ becomes 0.43 arc seconds per year. It follows that the total perihelion precession rate for Mercury is $5 . 3 2 + 0 . 4 3 = 5 . 7 5$ arc seconds per year. This is in exact agreement with the observed precession rate. Indeed, the ability of general relativity to explain the discrepancy between the observed perihelion precession rate of Mercury, and that calculated from Newtonian mechanics, was one of the first major successes of this theory.

# 5.6 Exercises

5.1. Prove that in the case of a central force varying inversely as the cube of the distance

$$
\boldsymbol { \mathrm { r } } ^ { 2 } = \boldsymbol { A } \boldsymbol { \mathrm { t } } ^ { 2 } + \boldsymbol { \mathrm { B } } \boldsymbol { \mathrm { t } } + \boldsymbol { \mathrm { C } } ,
$$

where A, B, C are constants.

5.2. The orbit of a particle moving in a central field is a circle passing through the origin, namely ${ \boldsymbol { \ r } } = { \boldsymbol { \ r } } _ { 0 }$ cos θ. Show that the force law is inverse-fifth power.

5.3. A particle moving in a central field describes a spiral orbit ${ \mathfrak { r } } = { \mathfrak { r } } _ { 0 } \exp ( { \mathrm { k } } \theta )$ . Show that the force law is inverse-cube, and that θ varies logarithmically with t. Show that there are two other possible types of orbit in this force-field, and give their equations.

5.4. A particle moves in a spiral orbit given by $\boldsymbol { \mathrm { r } } = \boldsymbol { \mathrm { a } } \boldsymbol { \Theta }$ . Suppose that θ increases linearly with t. Is the force acting on the particle central in nature? If not, determine how $\theta$ would have to vary with t in order to make the force central.

5.5. A particle moves in a circular orbit of radius $\boldsymbol { \mathrm { r } } _ { 0 }$ in an attractive central force-field of the form $\mathsf { f } ( \mathsf { r } ) = - { \mathsf { c } } \ \mathrm { e x p } ( - \mathsf { r } / { \mathsf { a } } ) / \mathsf { r } ^ { 2 }$ , where $c > 0$ and ${ \mathfrak { a } } > 0$ . Demonstrate that the orbit is only stable provided that $\boldsymbol { \Upsilon } _ { 0 } < \mathbf { a }$ .

5.6. A particle moves in a circular orbit in an attractive central force-field of the form ${ \sf f } ( { \sf r } ) =$ $- \mathbf { c } \mathbf { r } ^ { - 3 }$ , where ${ \mathfrak { c } } > 0$ . Demonstrate that the orbit is unstable to small perturbations.

5.7. If the Solar System were embedded in a uniform dust cloud, what would the apsidal angle of a planet be for motion in a nearly circular orbit? Express your answer in terms of the ratio of the mass of dust contained in a sphere, centered on the Sun, whose radius is that of the orbit, to the mass of the Sun. This model was once suggested as a possible explanation for the advance of the perihelion of Mercury.

5.8. The potential energy per unit mass of a particle in the gravitational field of an oblate spheroid, like the Earth, is

$$
V ( \boldsymbol { \mathsf { r } } ) = - \frac { \mathsf { G } M } { \boldsymbol { \mathsf { r } } } \left( 1 + \frac { \epsilon } { \mathsf { r } ^ { 2 } } \right) ,
$$

where r refers to distances in the equatorial plane, $M$ is the Earth’s mass, and $\epsilon = ( 2 / 5 ) \ : \mathsf { R } \Delta \mathsf { R } .$ . Here, $\mathtt { R } = 4 0 0 0 \mathrm { m i }$ is the Earth’s equatorial radius, and $\Delta { \sf R } = 1 3 \mathrm { m i }$ the difference between the equatorial and polar radii. Find the apsidal angle for a satellite moving in a nearly circular orbit in the equatorial plane of the Earth.

# 6 Rotating Reference Frames

# 6.1 Introduction

As we saw in Chapter 2, Newton’s second law of motion is only valid in inertial frames of reference. However, it is sometimes convenient to observe motion in non-inertial rotating reference frames. For instance, it is most convenient for us to observe the motions of objects close to the Earth’s surface in a reference frame which is fixed relative to this surface. Such a frame is non-inertial in nature, since it accelerates with respect to a standard inertial frame due to the Earth’s daily rotation about its axis. (Note that the accelerations of this frame due to the Earth’s orbital motion about the Sun, or the Sun’s orbital motion about the galactic center, etc., are negligible compared to the acceleration due to the Earth’s axial rotation.) Let us investigate motion in such rotating reference frames.

# 6.2 Rotating Reference Frames

Suppose that a given object has position vector r in some inertial (i.e., non-rotating) reference frame. Let us observe the motion of this object in a non-inertial reference frame which rotates with constant angular velocity $\Omega$ about an axis passing through the origin of the inertial frame. Suppose, first of all, that our object appears stationary in the rotating reference frame. Hence, in the non-rotating frame, the object’s position vector r will appear to precess about the origin with angular velocity $\Omega$ . It follows, from Equation (A.49), that in the non-rotating reference frame

$$
\frac { \mathrm { d } \mathbf { r } } { \mathrm { d t } } = \pmb { \Omega } \times \mathbf { r } .
$$

Suppose, now, that our object appears to move in the rotating reference frame with instantaneous velocity $\mathbf { v } ^ { \prime }$ . It is fairly obvious that the appropriate generalization of the above equation is simply

$$
\frac { \mathrm { d } \mathbf { r } } { \mathrm { d t } } = \mathbf { v } ^ { \prime } + \boldsymbol \Omega \times \mathbf { r } .
$$

Let and $\mathrm { d } / \mathrm { d t }$ and $\mathrm { d } / \mathrm { d t } ^ { \prime }$ denote apparent time derivatives in the non-rotating and rotating frames of reference, respectively. Since an object which is stationary in the rotating reference frame appears to move in the non-rotating frame, it is clear that $\mathrm { d } / \mathrm { d t } \ne \mathrm { d } / \mathrm { d t } ^ { \prime }$ . Writing the apparent velocity, $\mathbf { v } ^ { \prime }$ , of our object in the rotating reference frame as $\mathrm { d } \mathbf { r } / \mathrm { d } \mathrm { t } ^ { \prime }$ , the above equation takes the form

$$
\frac { \mathrm { d } \mathbf { r } } { \mathrm { d t } } = \frac { \mathrm { d } \mathbf { r } } { \mathrm { d t ^ { \prime } } } + \pmb { \Omega } \times \mathbf { r } ,
$$

$$
\frac { \mathrm { d } } { \mathrm { d t } } = \frac { \mathrm { d } } { \mathrm { d t ^ { \prime } } } + \Omega \times ,
$$

since r is a general position vector. Equation (6.4) expresses the relationship between apparent time derivatives in the non-rotating and rotating reference frames.

Operating on the general position vector r with the time derivative (6.4), we get

$$
\mathbf { v } = \mathbf { v } ^ { \prime } + \boldsymbol { \Omega } \times \mathbf { r } .
$$

This equation relates the apparent velocity, $\mathbf { v } = \mathrm { d } \mathbf { r } / \mathrm { d t }$ , of an object with position vector r in the non-rotating reference frame to its apparent velocity, $\mathbf { v } ^ { \prime } = \mathrm { d } \mathbf { r } / \mathrm { d } \mathrm { t } ^ { \prime }$ , in the rotating reference frame.

Operating twice on the position vector r with the time derivative (6.4), we obtain

$$
\mathbf { a } = \left( \frac { \mathrm { d } } { \mathrm { d t } ^ { \prime } } + \pmb { \Omega } \times \right) \left( \mathbf { v } ^ { \prime } + \pmb { \Omega } \times \mathbf { r } \right) ,
$$

or

$$
\mathbf { a } = \mathbf { a } ^ { \prime } + \pmb { \Omega } \times ( \pmb { \Omega } \times \mathbf { r } ) + 2 \pmb { \Omega } \times \mathbf { v } ^ { \prime } .
$$

This equation relates the apparent acceleration, $\mathbf { a } = \mathrm { d } ^ { 2 } \mathbf { r } / \mathrm { d t } ^ { 2 }$ , of an object with position vector r in the non-rotating reference frame to its apparent acceleration, $\mathbf { a } ^ { \prime } = \mathbf { d } ^ { 2 } \mathbf { r } / { \mathsf { d } } \mathbf { t } ^ { \prime 2 }$ , in the rotating reference frame.

Applying Newton’s second law of motion in the inertial (i.e., non-rotating) reference frame, we obtain

$$
{ \mathfrak { m } } \mathbf { a } = \mathbf { f } .
$$

Here, m is the mass of our object, and f is the (non-fictitious) force acting on it. Note that these quantities are the same in both reference frames. Making use of Equation (6.7), the apparent equation of motion of our object in the rotating reference frame takes the form

$$
\mathrm { m } \mathbf { a } ^ { \prime } = \mathbf { f } - \mathrm { m } { \boldsymbol { \Omega } } \times ( { \boldsymbol { \Omega } } \times \mathbf { r } ) - 2 \mathrm { m } { \boldsymbol { \Omega } } \times \mathbf { v } ^ { \prime } .
$$

The last two terms in the above equation are so-called “fictitious forces”. Such forces are always needed to account for motion observed in non-inertial reference frames. Note that fictitious forces can always be distinguished from non-fictitious forces in Newtonian mechanics because the former have no associated reactions. Let us now investigate the two fictitious forces appearing in Equation (6.9).

# 6.3 Centrifugal Acceleration

Let our non-rotating inertial frame be one whose origin lies at the center of the Earth, and let our rotating frame be one whose origin is fixed with respect to some point, of latitude $\lambda _ { \perp }$ , on the Earth’s surface—see Figure 6.1. The latter reference frame thus rotates with respect to the former (about an axis passing through the Earth’s center) with an angular velocity vector, $\Omega$ , which points from the center of the Earth toward its north pole, and is of magnitude

$$
\Omega = \frac { 2 \pi } { 2 4 \ \mathrm { h r s } } = 7 . 2 7 \times 1 0 ^ { - 5 } \mathrm { r a d . / s } .
$$

![](images/fa14e7a01ce71c8a5fa07466a37702d99b16299ffbbcb0f113e6a294ef61091e.jpg)  
Figure 6.1: Inertial and non-inertial reference frames.

Consider an object which appears stationary in our rotating reference frame: i.e., an object which is stationary with respect to the Earth’s surface. According to Equation (6.9), the object’s apparent equation of motion in the rotating frame takes the form

$$
\mathfrak { m } \mathbf { a } ^ { \prime } = \mathbf { f } - \mathfrak { m } \Omega \times ( \Omega \times \mathbf { r } ) .
$$

Let the non-fictitious force acting on our object be the force of gravity, $\mathbf { f } = \mathrm { m } \mathbf { g }$ . Here, the local gravitational acceleration, g, points directly toward the center of the Earth. It follows, from the above, that the apparent gravitational acceleration in the rotating frame is written

$$
\mathbf { g } ^ { \prime } = \mathbf { g } - \pmb { \Omega } \times ( \pmb { \Omega } \times \mathbf { R } ) ,
$$

where R is the displacement vector of the origin of the rotating frame (which lies on the Earth’s surface) with respect to the center of the Earth. Here, we are assuming that our object is situated relatively close to the Earth’s surface (i.e., ${ \bf r } \simeq { \bf R } )$ ).

It can be seen, from Equation (6.12), that the apparent gravitational acceleration of a stationary object close to the Earth’s surface has two components. First, the true gravitational acceleration, $\pmb { g } \mathrm { . }$ , of magnitude $9 \simeq 9 . 8 \mathrm { m } / \mathrm { s } ^ { 2 }$ , which always points directly toward the center of the Earth. Second, the so-called centrifugal acceleration, $- \pmb { \Omega } \times ( \pmb { \Omega } \times \pmb { \mathrm { R } } )$ . This acceleration is normal to the Earth’s axis of rotation, and always points directly away from this axis. The magnitude of the centrifugal acceleration is $\Omega ^ { 2 } \rho = \Omega ^ { 2 } \ R \cos \lambda$ , where $\rho$ is the perpendicular distance to the Earth’s rotation axis, and $\mathsf { R } = 6 . 3 7 \times 1 0 ^ { 6 } \mathrm { m }$ is the Earth’s radius—see Figure 6.2.

It is convenient to define Cartesian axes in the rotating reference frame such that the $z ^ { \prime }$ -axis points vertically upward, and $x ^ { \prime } .$ - and $\mathfrak { y ^ { \prime } }$ -axes are horizontal, with the $x ^ { \prime }$ -axis pointing directly northward, and the $\mathfrak { Y } ^ { \prime }$ -axis pointing directly westward—see Figure 6.1. The Cartesian components of the Earth’s angular velocity are thus

$$
\Omega = \Omega ( \cos \lambda , 0 , \sin \lambda ) ,
$$

![](images/c88b8acf7a92cbddfaba343f784bfc9b540eb6a55afc0225c35fddf3e8515e8e.jpg)  
Figure 6.2: Centrifugal acceleration.

whilst the vectors R and $\pmb { g }$ are written

$$
\begin{array} { r c l } { { { \bf R } } } & { { = } } & { { ( 0 , 0 , { \bf R } ) , } } \\ { { { \bf g } } } & { { = } } & { { ( 0 , 0 , - g ) , } } \end{array}
$$

respectively. It follows that the Cartesian coordinates of the apparent gravitational acceleration, (6.12), are

$$
{ \bf g } ^ { \prime } = \left( - \Omega ^ { 2 } { \sf R } \cos \lambda \sin \lambda , 0 , - { \bf g } + \Omega ^ { 2 } { \sf R } \cos ^ { 2 } \lambda \right) .
$$

The magnitude of this acceleration is approximately

$$
{ \mathfrak { g } } ^ { \prime } \simeq { \mathfrak { g } } - \Omega ^ { 2 } { \textsf { R } } \cos ^ { 2 } \lambda \simeq 9 . 8 - 0 . 0 3 4 \cos ^ { 2 } \lambda \ { \mathrm { m } } / { \mathrm { s } } ^ { 2 } .
$$

According to the above equation, the centrifugal acceleration causes the magnitude of the apparent gravitational acceleration on the Earth’s surface to vary by about $0 . 3 \%$ , being largest at the poles, and smallest at the equator. This variation in apparent gravitational acceleration, due (ultimately) to the Earth’s rotation, causes the Earth itself to bulge slightly at the equator (see Section 6.5), which has the effect of further intensifying the variation, since a point on the surface of the Earth at the equator is slightly further away from the Earth’s center than a similar point at one of the poles (and, hence, the true gravitational acceleration is slightly weaker in the former case).

Another consequence of centrifugal acceleration is that the apparent gravitational acceleration on the Earth’s surface has a horizontal component aligned in the north/south direction. This horizontal component ensures that the apparent gravitational acceleration does not point directly toward the center of the Earth. In other words, a plumb-line on the surface of the Earth does not point vertically downward, but is deflected slightly away from a true vertical in the north/south direction. The angular deviation from true vertical can easily be calculated from Equation (6.16):

$$
\theta _ { { \tt d e v } } \simeq - \frac { \Omega ^ { 2 } { \sf R } } { 2 \sf g } \sin ( 2 \lambda ) \simeq - 0 . 1 ^ { \circ } \sin ( 2 \lambda ) .
$$

Here, a positive angle denotes a northward deflection, and vice versa. Thus, the deflection is southward in the northern hemisphere (i.e., $\lambda > 0$ ) and northward in the southern hemisphere (i.e., $\lambda < 0 ,$ ). The deflection is zero at the poles and at the equator, and reaches its maximum magnitude (which is very small) at middle latitudes.

# 6.4 Coriolis Force

We have now accounted for the first fictitious force, $- \boldsymbol { \mathrm { m } } \pmb { \Omega } \times ( \pmb { \Omega } \times \pmb { \mathrm r } )$ , in Equation (6.9). Let us now investigate the second, which takes the form $- 2 \boldsymbol { \mathrm { m } } \Omega \times \mathbf { v } ^ { \prime }$ , and is called the Coriolis force. Obviously, this force only affects objects which are moving in the rotating reference frame.

Consider a particle of mass m free-falling under gravity in our rotating reference frame. As before, we define Cartesian axes in the rotating frame such that the $z ^ { \prime }$ -axis points vertically upward, and the $x ^ { \prime }$ - and $\mathfrak { Y } ^ { \prime }$ -axes are horizontal, with the $x ^ { \prime }$ -axis pointing directly northward, and the $\mathfrak { Y } ^ { \prime }$ -axis pointing directly westward. It follows, from Equation (6.9), that the Cartesian equations of motion of the particle in the rotating reference frame take the form:

$$
\begin{array} { r c l } { { \ddot { x } ^ { \prime } } } & { { = } } & { { 2 \Omega \sin \lambda \dot { y } ^ { \prime } , } } \\ { { } } & { { } } & { { } } \\ { { \ddot { y } ^ { \prime } } } & { { = } } & { { - 2 \Omega \sin \lambda \dot { x } ^ { \prime } + 2 \Omega \cos \lambda \dot { z } ^ { \prime } , } } \\ { { } } & { { } } & { { } } \\ { { \ddot { z } ^ { \prime } } } & { { = } } & { { - { \bf g } - 2 \Omega \cos \lambda \dot { y } ^ { \prime } . } } \end{array}
$$

Here, $\mathbf { \bar { \rho } } \equiv \mathrm { ~ d } / \mathrm { d } \mathrm { t }$ , and $^ { 9 }$ is the local acceleration due to gravity. In the above, we have neglected the centrifugal acceleration, for the sake of simplicity. This is reasonable, since the only effect of the centrifugal acceleration is to slightly modify the magnitude and direction of the local gravitational acceleration. We have also neglected air resistance, which is less reasonable.

Consider a particle which is dropped (at $\mathrm { t } = 0 \mathrm { . }$ ) from rest a height h above the Earth’s surface. The following solution method exploits the fact that the Coriolis force is much smaller in magnitude that the force of gravity: hence, $\Omega$ can be treated as a small parameter. To lowest order (i.e., neglecting $\Omega$ ), the particle’s vertical motion satisfies $\ddot { z } ^ { \prime } = - 9$ , which can be solved, subject to the initial conditions, to give

$$
z ^ { \prime } = \mathsf { h } - \frac { \mathsf { g t } ^ { 2 } } { 2 } .
$$

Substituting this expression into Equations (6.19) and (6.20), neglecting terms involving $\Omega ^ { 2 }$ , and solving subject to the initial conditions, we obtain $x ^ { \prime } \simeq 0$ , and

$$
y ^ { \prime } \simeq - 9 \Omega \cos \lambda \frac { { \sf t } ^ { 3 } } { 3 } .
$$

In other words, the particle is deflected eastward (i.e., in the negative $\mathfrak { Y } ^ { \prime }$ -direction). Now, the particle hits the ground when $\mathrm { t } \simeq \sqrt { 2 \mathrm { h } / \mathrm { g } }$ . Hence, the net eastward deflection of the particle as strikes the ground is

$$
\mathrm { d } _ { e { \mathrm { a s t } } } = { \frac { \Omega } { 3 } } \cos \lambda \left( { \frac { 8 \hbar ^ { 3 } } { 9 } } \right) ^ { 1 / 2 } .
$$

Note that this deflection is in the same direction as the Earth’s rotation (i.e., west to east), and is greatest at the equator, and zero at the poles. A particle dropped from a height of $1 0 0 \mathrm { m }$ at the equator is deflected by about $2 . 2 \mathrm { c m }$ .

Consider a particle launched horizontally with some fairly large velocity

$$
{ \bf V } = { \bf V } _ { 0 } \left( \cos \theta , - \sin \theta , 0 \right) .
$$

Here, θ is the compass bearing of the velocity vector (so north is $0 ^ { \circ }$ , east is $9 0 ^ { \circ }$ , etc.). Neglecting any vertical motion, Equations (6.19) and (6.20) yield

$$
\begin{array} { r l r } { \dot { \nu } _ { x ^ { \prime } } } & { \simeq } & { - 2 \Omega \lor _ { 0 } \sin \lambda \sin \theta , } \\ { \dot { \nu } _ { y } ^ { \prime } } & { \simeq } & { - 2 \Omega \lor _ { 0 } \sin \lambda \cos \theta , } \end{array}
$$

which can be integrated to give

$$
\begin{array} { r c l } { { \nu _ { x ^ { \prime } } } } & { { \simeq } } & { { \mathrm { V } _ { 0 } \cos \theta - 2 \Omega \mathrm { V } _ { 0 } \sin \lambda \sin \theta \mathrm { t } , } } \\ { { } } & { { } } & { { } } \\ { { \nu _ { y ^ { \prime } } } } & { { \simeq } } & { { - \mathrm { V } _ { 0 } \sin \theta - 2 \Omega \mathrm { V } _ { 0 } \sin \lambda \cos \theta \mathrm { t } . } } \end{array}
$$

To lowest order in $\Omega$ , the above equations are equivalent to

$$
\begin{array} { r c l } { { \nu _ { x ^ { \prime } } } } & { { \simeq } } & { { V _ { 0 } \cos ( \theta + 2 \Omega \sin \lambda t ) , } } \\ { { } } & { { } } & { { } } \\ { { \nu _ { y ^ { \prime } } } } & { { \simeq } } & { { - V _ { 0 } \sin ( \theta + 2 \Omega \sin \lambda t ) . } } \end{array}
$$

If follows that the Coriolis force causes the compass bearing of the particle’s velocity vector to rotate steadily as time progresses. The rotation rate is

$$
\frac { \mathrm { d } \theta } { \mathrm { d t } } \simeq 2 \Omega \sin \lambda .
$$

Hence, the rotation is clockwise (looking from above) in the northern hemisphere, and counter-clockwise in the southern hemisphere. The rotation rate is zero at the equator, and greatest at the poles.