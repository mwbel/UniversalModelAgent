<!-- source: An_Introduction_to_Celestial_Mechanics.pdf -->

<!-- pdf_type: normal; pages: 216; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
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


<!-- chunk 0002: pages 71-140 -->
![](images/5e9766753f1cb995350dbf17b69a6af0d5174272ab097ec32ca2d08d72ee00a7.jpg)  
Figure 6.3: A cyclone in the northern hemisphere.

The Coriolis force has a significant effect on terrestrial weather patterns. Near equatorial regions, the intense heating of the Earth’s surface due to the Sun results in hot air rising. In the northern hemisphere, this causes cooler air to move in a southerly direction toward the equator. The Coriolis force deflects this moving air in a clockwise sense (looking from above), resulting in the trade winds, which blow toward the southwest. In the southern hemisphere, the cooler air moves northward, and is deflected by the Coriolis force in a counter-clockwise sense, resulting in trade winds which blow toward the northwest.

Furthermore, as air flows from high to low pressure regions, the Coriolis force deflects the air in a clockwise/counter-clockwise manner in the northern/southern hemisphere, producing cyclonic rotation—see Figure 6.3. It follows that cyclonic rotation is counterclockwise in the northern hemisphere, and clockwise in the southern hemisphere. Thus, this is the direction of rotation of tropical storms (e.g., hurricanes, typhoons) in each hemisphere.

# 6.5 Rotational Flattening of the Earth

Consider the equilibrium configuration of a self-gravitating celestial body, composed of uniform density incompressible fluid, which is rotating steadily and uniformly about some fixed axis. Let the outer boundary of the body be spheroidal. Furthermore, let $M$ be the body’s total mass, a its mean radius, ǫ its ellipticity, and $\Omega$ its angular velocity of rotation. Finally, let the body’s axis of rotation coincide with its axis of symmetry, which is assumed to run along the $z$ -axis.

Let us transform to a non-inertial frame of reference which co-rotates with the body about the $z$ -axis, and in which the body consequently appears to be stationary. From

Section 6.3, the problem is now analogous to that of a non-rotating body, except that the surface acceleration is written ${ \bf g } = { \bf g } _ { \mathrm { q } } + { \bf g } _ { \mathrm { c } }$ , where $\mathbf { g } _ { 9 } = - \nabla \Phi ( \boldsymbol { \mathbf { r } } , \theta )$ is the gravitational acceleration, and $\pmb { g } _ { \mathrm { c } }$ the centrifugal acceleration. The latter acceleration is of magnitude r sin $\ 0 \ \Omega ^ { 2 }$ , and is everywhere directed away from the axis of rotation (see Section 6.2). The acceleration thus has components

$$
{ \bf g } _ { \mathrm { c } } = \mathrm { r } \Omega ^ { 2 } \sin \theta ( \sin \theta , \cos \theta , 0 )
$$

in spherical polar coordinates. It follows that $\begin{array} { r } { { \bf g } _ { \mathrm { c } } = - \nabla \chi _ { \mathrm { ~ } } } \end{array}$ , where

$$
\chi ( \mathsf { r } , \theta ) = - { \frac { \Omega ^ { 2 } \mathsf { r } ^ { 2 } } { 2 } } \sin ^ { 2 } \theta = - { \frac { \Omega ^ { 2 } \mathsf { r } ^ { 2 } } { 3 } } \left[ \mathsf { I } - \mathsf { P } _ { 2 } ( \cos \theta ) \right]
$$

can be thought of as a sort of centrifugal potential. Hence, the total surface acceleration is

$$
\begin{array} { r } { { \mathbf { g } } = - \nabla ( \Phi + \boldsymbol { \chi } ) . } \end{array}
$$

As before (see Section 3.6), the criterion for an equilibrium state is that the surface lie at a constant total potential, so as to eliminate tangential surface forces which cannot be balanced by internal pressure. Hence, assuming that the surface satisfies Equation (3.55), the equilibrium configuration is specified by

$$
\Phi ( { \bf a } _ { \theta } , \theta ) + \chi ( { \bf a } _ { \theta } , \theta ) = { \tt c } ,
$$

where c is a constant. It follows from Equations (3.65) and (6.34) that, to first-order in ǫ and $\Omega ^ { 2 }$ ,

$$
- \frac { \mathsf { G } M } { \mathsf { a } } \left[ 1 + \frac { 4 } { 1 5 } \epsilon \mathsf { P } _ { 2 } ( \cos \theta ) \right] - \frac { \Omega ^ { 2 } \mathrm { a } ^ { 2 } } { 3 } \left[ 1 - \mathsf { P } _ { 2 } ( \cos \theta ) \right] \simeq \mathsf { c } ,
$$

which yields

$$
\epsilon = \frac { 5 } { 4 } \frac { \Omega ^ { 2 } { \bf a } ^ { 3 } } { \mathrm { ~ G ~ } M } .
$$

We conclude, from the above expression, that the equilibrium configuration of a (relatively slowly) rotating self-gravitating fluid mass is an oblate spheroid: i.e., a sphere which is slightly flattened along its axis of rotation. The degree of flattening is proportional to the square of the rotation rate. Now, from (3.55), the mean radius of the spheroid is a, the radius at the poles (i.e., along the axis of rotation) is ${ \mathfrak { a } } _ { \mathfrak { p } } = { \mathfrak { a } } \left( 1 - 2 \epsilon / 3 \right)$ , and the radius at the equator (i.e., perpendicular to the axis of rotation) is $\mathfrak { a } _ { e } = \mathfrak { a } \left( 1 + \epsilon / 3 \right)$ —see Figure 6.4. Hence, the degree of rotational flattening can be written

$$
\frac { { \bf a } _ { e } - { \bf a } _ { \mathrm { p } } } { { \bf a } } = \epsilon = \frac { 5 } { 4 } \frac { \Omega ^ { 2 } { \bf a } ^ { 3 } } { { \sf G } M } .
$$

Incidentally, it is reasonable to apply the above analysis to a non-fluid self-gravitating celestial body, such as the Earth, as long as the body in question is significantly larger in diameter than about $5 0 \mathrm { k m }$ , since above this critical diameter the internal pressures that develop as a consequence of self-gravity are sufficiently large to cause most solid materials to deform like liquids (see Section 3.6). Now, for the case of the Earth, $\mathbf { a } = 6 . 3 7 \times 1 0 ^ { 6 } \mathrm { m } .$ , $\Omega = 7 . 2 7 \times 1 0 ^ { - 5 }$ rad./s, and $M = 5 . 9 7 \times 1 0 ^ { 2 4 } { \mathrm { k g } }$ . Thus, we predict that

![](images/bcb394090cd4690aab76cef6215ac7a03b53034863bd746848aa206ae16296a5.jpg)  
Figure 6.4: Rotational flattening.

$$
\epsilon = 0 . 0 0 4 2 9 ,
$$

corresponding to a difference between equatorial and polar radii of

$$
\Delta { \bf a } = { \bf a } _ { e } - { \bf a } _ { \mathrm { p } } = \epsilon { \bf a } = 2 7 . 3 \mathrm { k m } .
$$

In fact, the observed degree of flattening of the Earth is $\epsilon = 0 . 0 0 3 3 5$ , corresponding to a difference between equatorial and polar radii of $2 1 . 4 \mathrm { k m }$ . The main reason that our analysis has overestimated the degree of rotational flattening of the Earth is that it models the terrestrial interior as a uniform density incompressible fluid. In reality, the Earth’s core is much denser than its crust (see Exercise 6.1).

For Jupiter, $\mathbf { a } = 6 . 9 2 \times 1 0 ^ { 7 } \mathrm { m }$ , $\Omega = 1 . 7 6 \times 1 0 ^ { - 4 }$ rad./s, and $M = 1 . 9 0 \times 1 0 ^ { 2 7 } { \mathrm { k g } }$ . Hence, we predict that

$$
\epsilon = 0 . 1 0 1 .
$$

Note that this degree of flattening is much larger than that of the Earth, due to Jupiter’s relatively large radius (about 10 times that of Earth), combined with its relatively short rotation period (about 0.4 days). In fact, the polar flattening of Jupiter is clearly apparent from images of this planet. The observed degree of polar flattening of Jupiter is actually $\epsilon = 0 . 0 6 5$ . Our estimate of $\epsilon$ is probably slightly too large because Jupiter, which is mostly gaseous, has a mass distribution which is strongly concentrated at its core (see Exercise 12.1).

![](images/000d65605dac077f4fed9bc87c86789143379c9c2ef90ea8665b81661e58b02c.jpg)  
Figure 6.5: Two orbiting masses.

# 6.6 Tidal Elongation of the Earth

Consider two point masses, m and $\mathfrak { m } ^ { \prime }$ , executing circular orbits about their common center of mass, C, with angular velocity $\omega$ . Let $\mathsf { R }$ be the distance between the masses, and $\rho$ the distance between point C and mass m—see Figure 6.5. We know, from Section 4.11, that

$$
\omega ^ { 2 } = { \frac { \mathsf { G } M } { \mathsf { R } ^ { 3 } } } ,
$$

and

$$
\rho = \frac { \mathfrak { m } ^ { \prime } } { M } \ R ,
$$

where $M = { \mathfrak { m } } + { \mathfrak { m } } ^ { \prime }$

Let us transform to a non-inertial frame of reference which rotates, about an axis perpendicular to the orbital plane and passing through C, at the angular velocity ω. In this reference frame, both masses appear to be stationary. Consider mass m. In the rotating frame, this mass experiences a gravitational acceleration

$$
{ \bf a } _ { 9 } = \frac { \bf G \ m ^ { \prime } } { \bf R ^ { 2 } }
$$

directed toward the center of mass, and a centrifugal acceleration (see Section 6.3)

$$
\mathbf { a } _ { \mathrm { c } } = \omega ^ { 2 } \rho
$$

directed away from the center of mass. However, it is easily demonstrated, using Equations (6.43) and (6.44), that

$$
\mathbf { a } _ { \mathrm { c } } = \mathbf { a } _ { \mathrm { g } } .
$$

In other words, the gravitational and centrifugal accelerations balance, as must be the case if mass m is to remain stationary in the rotating frame. Let us investigate how this balance is affected if the masses m and $\mathfrak { m } ^ { \prime }$ have finite spatial extents.

Let the center of the mass distribution $\mathfrak { m } ^ { \prime }$ lie at $\boldsymbol { A }$ , the center of the mass distribution m at B, and the center of mass at C—see Figure 6.6. We wish to calculate the centrifugal and gravitational accelerations at some point $_ \mathrm { D }$ in the vicinity of point B. It is convenient to adopt spherical coordinates, centered on point B, and aligned such that the $z$ -axis coincides with the line BA.

![](images/adfabf56f7913a68f91830a08fb0488bc7f6c3752f6391b979544f5875299628.jpg)  
Figure 6.6: Calculation of tidal forces.

Let us assume that the mass distribution m is orbiting around C, but is not rotating about an axis passing through its center, in order to exclude rotational flattening from our analysis. If this is the case then it is easily seen that each constituent point of m executes circular motion of angular velocity $\omega$ and radius $\rho$ —see Figure 6.7. Hence, each constituent point experiences the same centrifugal acceleration: i.e.,

$$
\mathbf { g } _ { \mathrm { c } } = - \omega ^ { 2 } \rho \mathbf { e } _ { z } .
$$

It follows that

$$
\begin{array} { r } { { \bf g } _ { \mathrm { c } } = - \nabla \chi , } \end{array}
$$

where

$$
\ x = \omega ^ { 2 } \rho z
$$

is the centrifugal potential, and $z = \Upsilon \cos { \theta }$ . The centrifugal potential can also be written

$$
\chi = \frac { \mathsf { G } \mathsf { m } ^ { \prime } } { \mathsf { R } } \frac { \mathsf { r } } { \mathsf { R } } \mathsf { P } _ { 1 } ( \cos \theta ) .
$$

The gravitational acceleration at point $_ \mathrm { D }$ due to mass $\mathfrak { m } ^ { \prime }$ is given by

$$
\begin{array} { r } { \mathbf { g } _ { \mathrm { g } } = - \nabla \Phi ^ { \prime } , } \end{array}
$$

where the gravitational potential takes the form

$$
\Phi ^ { \prime } = - \frac { \mathsf { G } \mathsf { m } ^ { \prime } } { \mathsf { R } ^ { \prime } } .
$$

Here, $\mathsf { R } ^ { \prime }$ is the distance between points $\mathsf { A }$ and D. Note that the gravitational potential generated by the mass distribution $\mathfrak { m } ^ { \prime }$ is the same as that generated by an equivalent point mass at $\boldsymbol { \mathsf { A } }$ , as long as the distribution is spherically symmetric, which we shall assume to be the case.

Now,

$$
\mathbf { R } ^ { \prime } = \mathbf { R } - \mathbf { r } ,
$$

where $\mathbf { R } ^ { \prime }$ is the vector $\mathsf { D } \mathsf { A }$ , and R the vector →BA—see Figure 6.6. It follows that

$$
\mathbf { R } ^ { \prime - 1 } = \left( \mathbf { R } ^ { 2 } - 2 \mathbf { R } \cdot \mathbf { r } + \mathbf { r } ^ { 2 } \right) ^ { - 1 / 2 } = \left( \mathbf { R } ^ { 2 } - 2 \mathbf { R } \thinspace \mathbf { r } \cos \theta + \mathbf { r } ^ { 2 } \right) ^ { - 1 / 2 } .
$$

![](images/08f4064fc914d173af8394ab2a8b47b9568be46cf5d235402622e1f93e81923d.jpg)  
Figure 6.7: The center B of the mass distribution m orbits about the center of mass C in a circle of radius ρ. If the mass distribution is non-rotating then a non-central point D must maintain a constant spatial relationship to B. It follows that point D orbits some point $C ^ { \prime }$ , which has the same spatial relationship to C that D has to B, in a circle of radius ρ.

Expanding in powers of ${ \boldsymbol { \Upsilon } } / { \mathsf { R } }$ , we obtain

$$
\mathsf { R } ^ { \prime - 1 } = \frac { 1 } { \mathsf { R } } \sum _ { \mathsf { n } = 0 , \infty } \left( \frac { \mathsf { r } } { \mathsf { R } } \right) ^ { \mathsf { n } } \mathsf { P } _ { \mathsf { n } } ( \cos \theta ) .
$$

Hence,

$$
\Phi ^ { \prime } \simeq - \frac { \mathsf { G m } ^ { \prime } } { \mathsf { R } } \left[ 1 + \frac { \mathsf { r } } { \mathsf { R } } \mathsf { P } _ { 1 } ( \cos \theta ) + \frac { \mathsf { r } ^ { 2 } } { \mathsf { R } ^ { 2 } } \mathsf { P } _ { 2 } ( \cos \theta ) \right]
$$

to second-order in $\Upsilon / \mathsf { R }$ .

Adding $\boldsymbol { x }$ and $\Phi ^ { \prime }$ , we obtain

$$
\chi + \Phi ^ { \prime } \simeq - \frac { \mathrm { \bf ~ G ~ m } ^ { \prime } } { \mathrm { \bf ~ R } } \left[ 1 + \frac { { \mathrm { \bf ~ r } } ^ { 2 } } { \mathrm { \bf ~ R } ^ { 2 } } { \mathrm { \bf ~ P } } _ { 2 } ( \cos \theta ) \right]
$$

to second-order in $\Upsilon / \mathsf { R }$ . Note that $\chi + \Phi ^ { \prime }$ is the potential due to the net external force acting on the mass distribution m. This potential is constant up to first-order in ${ \boldsymbol { \Upsilon } } / { \mathsf { R } }$ , because the first-order variations in $\chi$ and $\Phi ^ { \prime }$ cancel one another. The cancellation is a manifestation of the balance between the centrifugal and gravitational accelerations in the equivalent point mass problem discussed above. However, this balance is only exact at the center of the mass distribution m. Away from the center, the centrifugal acceleration remains constant, whereas the gravitational acceleration increases with increasing $z$ . Hence, at positive $z$ , the gravitational acceleration is larger than the centrifugal, giving rise to a net acceleration in the $+ z$ -direction. Likewise, at negative $z$ , the centrifugal acceleration is larger than the gravitational, giving rise to a net acceleration in the $- z$ -direction. It follows that the mass distribution m is subject to a residual acceleration, represented by the second-order variation in Equation (6.58), which acts to elongate it along the $z$ -axis. This effect is known as tidal elongation.

![](images/b984211c0faf12c7d5d73778c5c601ea9efa122e67cfd6b0ca83119eaa7d76ad.jpg)  
Figure 6.8: Tidal elongation.

In order to calculate the tidal elongation of the mass distribution m we need to add the potential, $\chi + \Phi ^ { \prime }$ , due to the external forces, to the gravitational potential, $\Phi$ , generated by the distribution itself. Assuming that the mass distribution is spheroidal with uniform density, mass m, mean radius $\mathbf { a }$ , and ellipticity $\epsilon$ , it follows from Equations (3.55), (3.65), and (6.58) that the total surface potential is given by

$$
\begin{array} { r c l } { \displaystyle \chi + \Phi ^ { \prime } + \Phi } & { \displaystyle \simeq } & { \displaystyle - \frac { { \sf G } { \sf m } } { { \sf a } } - \frac { { \sf G } { \sf m } ^ { \prime } } { { \sf R } } } \\ & & { \displaystyle - \frac { 4 } { 1 5 } \frac { { \sf G } { \sf m } } { { \sf a } } \epsilon { \sf P } _ { 2 } ( \cos \theta ) - \frac { { \sf G } { \sf m } ^ { \prime } { \sf a } ^ { 2 } } { { \sf R } ^ { 3 } } { \sf P } _ { 2 } ( \cos \theta ) , } \end{array}
$$

where we have treated $\epsilon$ and ${ \mathfrak { a } } / { \mathfrak { R } }$ as small quantities. As before, the condition for equilibrium is that the total potential be constant over the surface of the spheroid. Hence, we obtain

$$
\epsilon = - \frac { 1 5 } { 4 } \frac { \mathrm { m } ^ { \prime } } { \mathrm { m } } \left( \frac { \mathrm { a } } { \mathrm { R } } \right) ^ { 3 }
$$

as our prediction for the ellipticity induced in a self-gravitating spherical mass distribution of total mass m and radius a by a second mass, $\mathfrak { m } ^ { \prime }$ , which is in a circular orbit of radius R about the distribution. Thus, if ${ \bf { a } } _ { + }$ is the maximum radius of the distribution, and ${ \bf { a } } _ { - }$ the minimum radius (see Figure 6.8), then

$$
\frac { { \bf a } _ { + } - { \bf a } _ { - } } { { \bf a } } = - \epsilon = \frac { 1 5 } { 4 } \frac { { \bf m } ^ { \prime } } { { \bf m } } \left( \frac { { \bf a } } { \sf R } \right) ^ { 3 } .
$$

Consider the tidal elongation of the Earth due to the Moon. In this case, we have $\mathbf { a } = 6 . 3 7 \times 1 0 ^ { 6 } \mathrm { m } .$ , ${ \sf R } = 3 . 8 4 \times 1 0 ^ { 8 } { \mathrm { m } } .$ , $\mathrm { m } = 5 . 9 7 \times 1 0 ^ { 2 4 } \mathrm { k g }$ , and $\mathbf { m } ^ { \prime } = 7 . 3 5 \times 1 0 ^ { 2 2 } \mathbf { k g }$ . Hence, we calculate that $- \epsilon = 2 . 1 \times 1 0 ^ { - 7 }$ , or

$$
\Delta { \tt a } = { \tt a } _ { + } - { \tt a } _ { - } = - \epsilon { \tt a } = 1 . 3 4 \mathrm { m } .
$$

We, thus, predict that tidal forces due to the Moon cause the Earth to elongate along the axis joining its center to the Moon by about 1.3 meters. Since water is obviously more fluid than rock (especially on relatively short time-scales) most of this elongation takes place in the oceans rather than in the underlying land. Hence, the oceans rise, relative to the land, in the region of the Earth closest to the Moon, and also in the region furthest away. Since the Earth is rotating, whilst the tidal bulge of the oceans remains relatively stationary, the Moon’s tidal force causes the ocean at a given point on the Earth’s surface to rise and fall, by about a meter, twice daily, giving rise to the phenomenon known as the tides.

Consider the tidal elongation of the Earth due to the Sun. In this case, we have ${ \bf { a } } =$ $6 . 3 7 \times 1 0 ^ { 6 } \mathrm { m }$ , $\mathrm { R } = 1 . 5 0 \times 1 0 ^ { 1 1 } \mathrm { m }$ , $\mathrm { m } = 5 . 9 7 \times 1 0 ^ { 2 4 } \mathrm { k g } .$ , and $\mathbf { m } ^ { \prime } = 1 . 9 9 \times 1 0 ^ { 3 0 } \mathbf { k g }$ . Hence, we calculate that $- \epsilon = 9 . 6 \times 1 0 ^ { - 8 }$ , or

$$
\Delta { \bf a } = { \bf a } _ { + } - { \bf a } _ { - } = - \epsilon { \bf a } = 0 . 6 1 \mathrm { m } .
$$

Thus, the tidal elongation due to the Sun is about half that due to the Moon. It follows that the tides are particularly high when the Sun, the Earth, and the Moon lie approximately in a straight-line, so that the tidal effects of the Sun and the Moon reinforce one another. This occurs at a new moon, or at a full moon. These type of tides are called spring tides (note that the name has nothing to do with the season). Conversely, the tides are particularly low when the Sun, the Earth, and the Moon form a right-angle, so that the tidal effects of the Sun and the Moon partially cancel one another. These type of tides are called neap tides. Generally speaking, we would expect two spring tides and two neap tides per month.

In reality, the amplitude of the tides varies significantly from place to place on the Earth’s surface, due to the presence of the continents, which impede the flow of the oceanic tidal bulge around the Earth. Moreover, there is an average time-lag of roughly 12 minutes between the Moon passing directly overhead (or directly below) and high tide, because of the finite inertia of the oceans. Similarly, the time-lag between a spring tide and a full moon, or a new moon, can be up to 2 days.

# 6.7 Tidal Torques

The fact that there is a time-lag between the Moon passing overhead and the occurrence of a high tide suggests the physical scenario illustrated in Figure 6.9. According to this scenario, the Moon, which is of mass $\mathfrak { m } ^ { \prime }$ , and which is treated as a point particle, orbits the Earth (it actually orbits the center of mass of the Earth-Moon system, but this amounts to almost the same thing) in an approximately circular orbit of radius R. Moreover, the orbital angular velocity of the Moon is [see Equation (6.43)]

$$
 \omega = \frac { \left( \mathsf { G } M \right) ^ { 1 / 2 } } { \mathsf { R } ^ { 3 / 2 } } ,
$$

where $M = { \mathfrak { m } } + { \mathfrak { m } } ^ { \prime }$ is the total mass of the Earth-Moon system. The Earth is treated as a sphere of mass m, and radius $\mathbf { a }$ , that rotates daily about its axis (which is approximately normal to the orbital plane of the Moon) at the angular velocity Ω. Note, incidentally, that the Earth rotates in the same sense that the Moon orbits, as indicated in the figure. Now, as we saw in the previous section, spatial gradients in the Moon’s gravitational field produce a slight tidal elongation of the Earth. However, because of the finite inertia of the oceans, this elongation does not quite line up along the axis joining the centers of the Earth and Moon. In fact, since $\Omega > \omega$ , the tidal elongation is carried ahead (in the sense defined by the Earth’s rotation) of this axis by some small angle δ (say), as shown in the figure.

![](images/23831bc48013b1040a1bcfc2103a831bc75246c9037f432f4f7ec638d6bde082.jpg)  
Figure 6.9: Origin of tidal torque.

Defining a spherical coordinate system, r, θ, $\Phi$ , whose origin is the center of the Earth, and which is orientated such that the Earth-Moon axis always corresponds to $\theta = 0$ (see Figure 6.6), the Earth’s external gravitational potential is $[ c f .$ , Equation (3.63)]

$$
\Phi ( { \mathsf { r } } , \theta ) = - \frac { \mathsf { G m } } { { \mathsf { r } } } + \frac { 2 } { 5 } \frac { \mathsf { G m } \alpha ^ { 2 } } { { \mathsf { r } } ^ { 3 } } \epsilon \left[ 3 \cos ^ { 2 } ( \theta - \delta ) - 1 \right] ,
$$

where ǫ is the ellipticity induced by the tidal field of the Moon. Note that the second term on the right-hand side of the above expression is the contribution of the Earth’s tidal bulge, which attains its maximum amplitude at $\theta = \delta$ , rather than $\theta = 0$ , because of the aforementioned misalignment between the bulge and the Earth-Moon axis. Equations (6.60) and (6.65) can be combined to give

$$
\Phi ( { \bf r } , \theta ) = - \frac { \mathsf { G } \mathfrak { m } } { \mathfrak { r } } - \frac { 3 } { 4 } \frac { \mathsf { G } \mathfrak { m } ^ { \prime } \mathfrak { a } ^ { 2 } } { { \mathfrak { r } } ^ { 3 } } \left( \frac { \mathfrak { a } } { \mathsf { R } } \right) ^ { 3 } \left[ 3 \cos ^ { 2 } ( \theta - \delta ) - 1 \right] .
$$

Now, from (3.7), the torque that the Earth’s gravitational field exerts on the Moon is

$$
\tau = - \mathfrak { m } ^ { \prime } \frac { \partial \Phi } { \partial \boldsymbol { \theta } } \bigg \vert _ { \boldsymbol { \theta = 0 } , \mathrm { r = R } } \simeq \frac { 9 } { 2 } \frac { \mathrm { G } \mathfrak { m } ^ { \prime 2 } } { \mathbf { a } } \left( \frac { \mathbf { a } } { \mathsf { R } } \right) ^ { 6 } \delta ,
$$

where use has been made of Equation (6.66), as well as the fact that δ is a small angle. Note that there is zero torque in the absence of a misalignment between the Earth’s tidal bulge and the Earth-Moon axis. The torque $\tau$ acts to increase the Moon’s orbital angular momentum. By conservation of angular momentum, an equal and opposite torque, −τ, is applied to the Earth, and acts to decrease its rotational angular momentum. Note that if the Moon were sufficiently close to the Earth that its orbital angular velocity exceeded the Earth’s rotational angular velocity (i.e., if $\omega > \Omega$ ) then the phase-lag between the tides and the Moon would cause the tidal bulge to fall slightly behind the Earth-Moon axis (i.e., $\delta < 0 ]$ . In this case, the gravitational torque would act to reduce the Moon’s orbital angular momentum, and to increase the Earth’s rotational angular momentum.

The Earth’s rotational equation of motion is

$$
\operatorname { I } { \dot { \Omega } } = - \tau ,
$$

where I is its moment of inertia. Very crudely approximating the Earth as a uniform sphere, we have $\mathrm { I } = ( 2 / 5 ) \mathrm { m } \mathrm { a } ^ { 2 }$ . Hence, the previous two equations can be combined to give

$$
{ \frac { \dot { \Omega } } { \Omega } } \simeq - { \frac { 4 5 } { 4 } } { \frac { \omega ^ { 2 } } { \Omega } } \left( { \frac { \mathfrak { m } ^ { \prime } } { \mathfrak { m } } } \right) ^ { 2 } \left( { \frac { \mathfrak { a } } { \mathfrak { R } } } \right) ^ { 3 } \delta ,
$$

where use has been made of Equation (6.64), as well as the fact that $\mathbf { m } \gg \mathbf { m } ^ { \prime }$ . Now, a time-lag of 12 minutes between the Moon being overhead and the occurrence of a hightide implies a phase-lag of $\delta \sim 0 . 0 5$ radians (i.e., $\delta \sim 3 ^ { \circ } )$ ). Hence, employing the observed values $\mathrm { m } = 5 . 9 7 \times 1 0 ^ { 2 4 } \mathrm { k g }$ , $\begin{array} { r } { \mathbf { m } ^ { \prime } = 7 . 3 5 \times 1 0 ^ { 2 2 } \mathbf { k g } , } \end{array}$ $\mathbf { a } = 6 . 3 7 \times 1 0 ^ { 6 } \mathrm { m }$ , ${ \sf R } = 3 . 8 4 \times 1 0 ^ { 8 } { \mathrm { m } } .$ , $\Omega = 7 . 2 7 \times 1 0 ^ { - 5 }$ rad./s, and $\omega = 2 . 6 7 \times 1 0 ^ { - 6 } \mathrm { r a d . } / s$ , we find that

$$
\frac { \dot { \Omega } } { \Omega } \simeq - 3 . 8 \times 1 0 ^ { - 1 7 } s ^ { - 1 } .
$$

It follows that, under the influence of the tidal torque, the Earth’s rotation is gradually decelerating. Indeed, according to the above estimate, the length of a day should be increasing at the rate of about 10 milliseconds a century. (In fact, as a consequence of the severe approximations made in the our calculation, this estimate is about a factor of 5 too high.) The time-scale for the tidal torque to significantly reduce the Earth’s rotational angular velocity is estimated to be

$$
{ \mathsf { T } } \simeq { \frac { \Omega } { | { \dot { \Omega } } | } } \sim 8 \times 1 0 ^ { 8 } { \mathrm { y e a r s } } .
$$

This time-scale is comparable with the Earth’s age, which is thought to be $4 . 5 \times 1 0 ^ { 9 }$ years. Hence, we conclude that, whilst the Earth is certainly old enough for the tidal torque to have significantly reduced its rotational angular velocity, it is plausible (especially when we take into account that our estimate for $| \dot { \Omega } |$ is 5 times too high) that it is not sufficiently old for the torque to have driven the Earth-Moon system to a final steady-state. Such a state, in which the Earth’s rotational angular velocity matches the Moon’s orbital angular velocity, is termed synchronous. In a synchronous state, the Moon would appear stationary to an observer on the Earth’s surface, and, hence, there would be no tides (from the observer’s perspective), no phase-lag, and no tidal torque.

Up to now, we have concentrated on the effect of the tidal torque on the rotation of the Earth. Let us now examine its effect on the orbit of the Moon. Now, the total angular momentum of the Earth-Moon system is

$$
{ \mathsf { L } } \simeq \frac { 2 } { 5 } \mathsf { m } \mathsf { a } ^ { 2 } \Omega + \mathsf { m } ^ { \prime } \mathsf { R } ^ { 2 } \omega ,
$$

where the first term on the right-hand side is the rotational angular momentum of the Earth, and the second the orbital angular momentum of the Moon. Of course, L is a conserved quantity. Moreover, ω and R are related according to Equation (6.64). It follows that

$$
\frac { \dot { \mathsf { R } } } { \mathsf { R } } \simeq - \frac { 4 } { 5 } \frac { \mathsf { m } } { \mathsf { m } ^ { \prime } } \left( \frac { \mathbf { a } } { \mathsf { R } } \right) ^ { 2 } \frac { \dot { \Omega } } { \omega } \simeq 1 . 9 \times 1 0 ^ { - 1 7 } \mathsf { s } ^ { - 1 } ,
$$

where use has been made of (6.70). In other words, the tidal torque causes the radius of the Moon’s orbit to gradually increase. According to the above estimate, this increase should take place at the rate of about $2 2 \mathrm { c m }$ a year. (Again, this estimate is a factor of 5 too large.) We also have

$$
\frac { \dot { \omega } } { \omega } = - \frac { 3 } { 2 } \frac { \dot { \mathsf { R } } } { \mathsf { R } } \sim - 2 . 8 \times 1 0 ^ { - 1 7 } { \mathsf { s } } ^ { - 1 } .
$$

In other words, the tidal torque produces a gradual angular deceleration in the Moon’s orbital motion. According to the above estimate, this deceleration should take place at the rate of 150 arc seconds per century squared. (As before, this estimate is a factor of 5 too large.)

The net rate at which the tidal torques acting on the Moon and the Earth do work is

$$
\dot { \mathsf { E } } = \tau ( \boldsymbol { \omega } - \boldsymbol { \Omega } ) .
$$

Note that $\dot { \mathsf { E } } < 0$ , since $\tau > 0$ and $\Omega > \omega$ . This implies that the deceleration of the Earth’s rotation, and the Moon’s orbital motion, that are induced by the tidal torques are necessarily associated with the dissipation of energy. Most of this dissipation occurs in a turbulent boundary layer at the bottoms of shallow seas such as the European shelf around the British Isles, the Patagonian shelf off Argentina, and the Bering Sea. In the absence of dissipation, there can be no steady phase-lag between the Moon and the Earth’s tidal bulge, and, therefore, no tidal torques.

Of course, we would expect spatial gradients in the gravitational field of the Earth to generate a tidal bulge in the Moon. We would also expect dissipative effects to generate a phase-lag between this bulge and the Earth. This would allow the Earth to exert a gravitational torque that acts to drive the Moon toward a synchronous state in which its rotational angular velocity matches its orbital angular velocity. By analogy with the previous analysis, the de-spinning rate of the Moon is estimated to be

$$
\frac { \dot { \Omega } ^ { \prime } } { \Omega ^ { \prime } } \simeq - \frac { 4 5 } { 4 } \frac { \omega ^ { 2 } } { \Omega ^ { \prime } } \frac { \mathrm { m } } { \mathrm { m } ^ { \prime } } \left( \frac { \mathrm { a } ^ { \prime } } { \mathsf { R } } \right) ^ { 3 } \ : \delta \sim - 2 . 3 \times 1 0 ^ { - 1 3 } \ : s ^ { - 1 } ,
$$

where $\Omega ^ { \prime }$ is the Moon’s rotational angular velocity, $\mathbf { a } ^ { \prime } = 1 . 7 4 \times 1 0 ^ { 6 } \mathrm { m }$ the lunar radius, and δ the phase-lag. The above numerical estimate is made with the guesses $\Omega ^ { \prime } = 1 0 \omega$ and $\delta = 0 . 0 1$ . Thus, the time required for the Moon to achieve a synchronous state is

$$
\mathsf { T } ^ { \prime } \simeq \frac { \Omega ^ { \prime } } { | \dot { \Omega } ^ { \prime } | } \sim 1 0 ^ { 5 } \mathrm { y e a r s } .
$$

This is considerably less than the age of the Moon. Hence, it is not surprising that the Moon has actually achieved a synchronous state, as evidenced by the fact that the same side of the Moon is always visible from the Earth.

# 6.8 Roche Radius

Consider a spherical moon of mass m and radius a which is in a circular orbit of radius R about a spherical planet of mass $\mathfrak { m } ^ { \prime }$ and radius $\mathbf { { a } ^ { \prime } }$ . (Strictly speaking, the moon and the planet execute circular orbits about their common center of mass. However, if the planet is much more massive than the moon then the center of mass lies very close to the planet’s center.) According to the analysis in Section 6.6, a constituent element of the moon experiences a force per unit mass, due to the gravitational field of the planet, which takes the form

$$
\begin{array} { r } { \mathbf { g } ^ { \prime } = - \nabla ( \chi + \Phi ^ { \prime } ) , } \end{array}
$$

where

$$
\chi + \Phi ^ { \prime } = - \frac { \mathsf { G } \mathfrak { m } ^ { \prime } } { \mathsf { R } ^ { 3 } } \left( z ^ { 2 } - x ^ { 2 } / 2 - \mathsf { y } ^ { 2 } / 2 \right) + \mathrm { c o n s t . }
$$

Here, $( x , y , z )$ is a Cartesian coordinate system whose origin is the center of the moon, and whose $z$ -axis always points toward the center of the planet. It follows that

$$
\mathbf { g } ^ { \prime } = \frac { 2 \textrm { G m } ^ { \prime } } { \mathsf { R } ^ { 3 } } \left( - \frac { x } { 2 } \mathbf { e } _ { x } - \frac { y } { 2 } \mathbf { e } _ { y } + z \mathbf { e } _ { z } \right) .
$$

This so-called tidal force is generated by the spatial variation of the planet’s gravitational field over the interior of the moon, and acts to elongate the moon along an axis joining its center to that of the planet, and to compress it in any direction perpendicular to this axis. Note that the magnitude of the tidal force increases strongly as the radius, R, of the moon’s orbit decreases. In fact, if the tidal force becomes sufficiently strong then it can overcome the moon’s self-gravity, and thereby rip the moon apart. It follows that there is a minimum radius, generally referred to as the Roche radius, at which a moon can orbit a planet without being destroyed by tidal forces.

Let us derive an expression for the Roche radius. Consider a small mass element at the point on the surface of the moon which lies closest to the planet, and at which the tidal force is consequently largest (i.e., $\mathtt { x } = \mathtt { y } = 0$ , $z = \mathbf { a }$ ). According to Equation (6.80), the mass experiences an upward (from the moon’s surface) tidal acceleration due to the gravitational attraction of the planet of the form

$$
\mathbf { g } ^ { \prime } = \frac { 2 \mathsf { G } \mathsf { m } ^ { \prime } \mathbf { a } } { \mathsf { R } ^ { 3 } } \mathbf { e } _ { z } .
$$

The mass also experiences a downward gravitational acceleration due to the gravitational influence of the moon which is written

$$
\mathbf { g } = - { \frac { \mathsf { G } { \mathsf { m } } } { { \mathsf { a } } ^ { 2 } } } \mathbf { e } _ { z } .
$$

Thus, the effective surface gravity at the point in question is

$$
{ \sf g } _ { \mathrm { e f f } } = \frac { { \sf G } { \sf m } } { { \sf a } ^ { 2 } } \left( 1 - 2 \frac { { \sf m } ^ { \prime } } { { \sf m } } \frac { { \sf a } ^ { 3 } } { { \sf R } ^ { 3 } } \right) .
$$

Note that if ${ \sf R } < { \sf R } _ { \sf c }$ , where

$$
\mathrm { R } _ { \mathrm { c } } = \left( 2 \frac { \mathrm { m } ^ { \prime } } { \mathrm { m } } \right) ^ { 1 / 3 } \mathrm { a } ,
$$

then the effective gravity is negative. In other words, the tidal force due to the planet is strong enough to overcome surface gravity and lift objects off the moon’s surface. If this is the case, and the tensile strength of the moon is negligible, then it is fairly clear that the tidal force will start to break the moon apart. Hence, $\mathsf { R } _ { \mathrm { c } }$ is the Roche radius. Now, $\mathfrak { m } ^ { \prime } / \mathfrak { m } = ( \rho ^ { \prime } / \rho ) ( \mathbf { a } ^ { \prime } / \mathbf { a } ) ^ { 3 }$ , where $\rho$ and $\rho ^ { \prime }$ are the mean mass densities of the moon and planet, respectively. Thus, the above expression for the Roche radius can also be written

$$
\mathsf { R } _ { c } = 1 . 4 1 \left( \frac { \rho ^ { \prime } } { \rho } \right) ^ { 1 / 3 } \alpha ^ { \prime } .
$$

The above calculation is somewhat inaccurate, since it fails to take into account the inevitable distortion of the moon’s shape in the presence of strong tidal forces. (In fact, the calculation assumes that the moon always remains spherical.) A more accurate calculation, which treats the moon as a self-gravitating incompressible fluid, yields 1

$$
\mathsf { R } _ { c } = 2 . 4 4 \left( \frac { \rho ^ { \prime } } { \rho } \right) ^ { 1 / 3 } \alpha ^ { \prime } .
$$

It follows that if the planet and the moon have the same mean density then the Roche radius is 2.44 times the planet’s radius. Note that small orbital bodies such as rocks, or even very small moons, can survive intact within the Roche radius because they are held together by internal tensile forces rather than gravitational attraction. However, this mechanism becomes progressively less effective as the size of the body in question increases (see Section 3.6). Not surprisingly, virtually all large planetary moons occurring in the Solar System have orbital radii which exceed the relevant Roche radius, whereas virtually all planetary ring systems (which consist of myriads of small orbiting rocks) have radii which lie inside the relevant Roche radius.

# 6.9 Exercises

6.1. A pebble is dropped down an elevator shaft in the Empire State Building $( \mathsf { h } = 1 2 5 0$ ft, latitude $= 4 1 ^ { \circ } \mathrm { ~ N ~ }$ ). Find the pebble’s horizontal deflection (magnitude and direction) due to the Coriolis force at the bottom of the shaft. Neglect air resistance.

6.2. If a bullet is fired due east, at an elevation angle $\alpha$ , from a point on the Earth whose latitude is $+ \lambda$ show that it will strike the Earth with a lateral deflection $4 \Omega \nu _ { 0 } ^ { 3 } \sin \lambda \sin ^ { 2 } \propto \cos \alpha / g ^ { 2 }$ . Is the deflection northward or southward? Here, $\Omega$ is the Earth’s angular velocity, $\nu _ { 0 }$ is the bullet’s initial speed, and $9$ is the acceleration due to gravity. Neglect air resistance.

6.3. A particle is thrown vertically with initial speed $\nu _ { 0 } ,$ , reaches a maximum height, and falls back to the ground. Show that the horizontal Coriolis deflection of the particle when it returns to the ground is opposite in direction, and four times greater in magnitude, than the Coriolis deflection when it is dropped at rest from the same maximum height. Neglect air resistance.

6.4. A satellite is in a circular orbit of radius a about the Earth. Let us define a set of co-moving Cartesian coordinates, centered on the satellite, such that the $x$ -axis always points toward the center of the Earth, the $y$ -axis in the direction of the satellite’s orbital motion, and the $z$ -axis in the direction of the satellite’s orbital angular velocity, $\omega$ . Demonstrate that the equation of motion of a small mass in orbit about the satellite are

$$
\begin{array} { l c l } { { \ddot { x } } } & { { = } } & { { 3 \omega ^ { 2 } x + 2 \omega \dot { y } , } } \\ { { \ddot { y } } } & { { = } } & { { - 2 \omega \dot { x } , } } \end{array}
$$

assuming that $| x | / a \ll 1$ and $| y | / a \ll 1$ . You may neglect the gravitational attraction between the satellite and the mass. Show that the mass executes a retrograde (i.e., in the opposite sense to the satellite’s orbital rotation) elliptical orbit about the satellite whose period matches that of the satellite’s orbit, and whose major and minor axes are in the ratio $2 : 1$ , and are aligned along the $y$ - and $x$ -axes, respectively.

6.5. Show that

$$
\epsilon = \frac { 5 - \alpha } { 4 } \frac { \Omega ^ { 2 } { \bf a } ^ { 3 } } { \mathrm { ~ G ~ M ~ } } .
$$

for a self-gravitating, rotating spheroid of ellipticity $\epsilon \ll 1$ , mass $M$ , mean radius a, and angular velocity $\Omega$ whose mass density varies as $r ^ { - \alpha }$ (where $\alpha < 3$ ). Demonstrate that the above formula matches the observed rotational flattening of the Earth when $\alpha = 1 . 0 9$ and of Jupiter when $\alpha = 1 . 7 9$ .

6.6. The Moon’s orbital period about the Earth is approximately 27.3 days, and is in the same direction as the Earth’s axial rotation (whose period is 24 hours). Use this data to show that high tides at a given point on the Earth occur every 12 hours and 26 minutes.

6.7. Estimate the tidal elongation of the Moon due to the Earth.

# 7 Lagrangian Mechanics

# 7.1 Introduction

This chapter describes an elegant reformulation of the laws of Newtonian mechanics that is due to the French-Italian scientist Joseph Louis Lagrange. This reformulation is particularly useful for finding the equations of motion of complicated dynamical systems.

# 7.2 Generalized Coordinates

Let the ${ \mathfrak { q } } _ { \mathrm { i } } ,$ for $\mathfrak { i } = 1 , \mathcal { F } _ { : }$ , be a set of coordinates which uniquely specifies the instantaneous configuration of some dynamical system. Here, it is assumed that each of the ${ \mathfrak { q } } _ { \mathrm { i } }$ can vary independently. The ${ \mathfrak { q } } _ { \mathrm { i } }$ might be Cartesian coordinates, or polar coordinates, or angles, or some mixture of all three types of coordinate, and are, therefore, termed generalized coordinates. A dynamical system whose instantaneous configuration is fully specified by $\mathcal { F }$ independent generalized coordinates is said to have $\mathcal { F }$ degrees of freedom. For instance, the instantaneous position of a particle moving freely in three dimensions is completely specified by its three Cartesian coordinates, $x , y$ , and $z$ . Moreover, these coordinates are clearly independent of one another. Hence, a dynamical system consisting of a single particle moving freely in three dimensions has three degrees of freedom. If there are two freely moving particles then the system has six degrees of freedom, and so on.

Suppose that we have a dynamical system consisting of $\mathsf { N }$ particles moving freely in three dimensions. This is an $\mathcal { F } = 3 \Nu$ degree of freedom system whose instantaneous configuration can be specified by $\mathcal { F }$ Cartesian coordinates. Let us denote these coordinates the $x _ { \mathrm { j } }$ , for $\mathrm { j } = 1 , { \mathcal { F } }$ . Thus, $\mathbf { \boldsymbol { x } } _ { 1 } , \mathbf { \boldsymbol { x } } _ { 2 } , \mathbf { \boldsymbol { x } } _ { 3 }$ are the Cartesian coordinates of the first particle, ${ \mathrm { x } } _ { 4 } , { \mathrm { x } } _ { 5 } , { \mathrm { x } } _ { 6 }$ the Cartesian coordinates of the second particle, etc. Suppose that the instantaneous configuration of the system can also be specified by $\mathcal { F }$ generalized coordinates, which we shall denote the ${ \mathfrak { q } } _ { \mathrm { i } }$ , for $\mathfrak { i } = 1 , \mathcal { F }$ . Thus, the ${ \mathfrak { q } } _ { \mathrm { i } }$ might be the spherical coordinates of the particles. In general, we expect the $x _ { \mathrm { j } }$ to be functions of the ${ \mathfrak { q } } _ { \mathrm { i } }$ . In other words,

$$
x _ { \mathrm { j } } = x _ { \mathrm { j } } ( { \bf q } _ { 1 } , { \bf q } _ { 2 } , \cdots , { \bf q } _ { \mathcal { F } } , { \bf t } )
$$

for $\mathrm { ~ j ~ } = 1 , \mathcal { F }$ . Here, for the sake of generality, we have included the possibility that the functional relationship between the $x _ { \mathrm { j } }$ and the ${ \mathfrak { q } } _ { \mathrm { i } }$ might depend on the time, t, explicitly. This would be the case if the dynamical system were subject to time varying constraints. For instance, a system consisting of a particle constrained to move on a surface which is itself moving. Finally, by the chain rule, the variation of the $x _ { \mathrm { j } }$ due to a variation of the ${ \mathfrak { q } } _ { \mathrm { i } }$ (at constant t) is given by

$$
\delta { \bf x } _ { \mathrm { j } } = \sum _ { \mathrm { i } = 1 , \mathcal { F } } \frac { \partial { \bf x } _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } } \delta { \bf q } _ { \mathrm { i } } ,
$$

for $\mathrm { j } = 1 , { \mathcal { F } } .$

# 7.3 Generalized Forces

The work done on the dynamical system when its Cartesian coordinates change by $\delta \mathrm { { x } _ { j } }$ is simply

$$
\delta W = \sum _ { \mathrm { j } = 1 , \mathcal { F } } \mathrm { f _ { j } } \delta x _ { \mathrm { j } }
$$

Here, the $\mathsf { f } _ { \mathrm { j } }$ are the Cartesian components of the forces acting on the various particles making up the system. Thus, $\mathsf { f } _ { 1 } , \mathsf { f } _ { 2 } , \mathsf { f } _ { 3 }$ are the components of the force acting on the first particle, $\mathrm { f } _ { 4 } , \mathrm { f } _ { 5 } , \mathrm { f } _ { 6 }$ the components of the force acting on the second particle, etc. Using Equation (7.2), we can also write

$$
\delta W = \sum _ { \mathrm { j } = 1 , \mathcal { F } } \mathrm { f } _ { \mathrm { j } } \sum _ { \mathrm { i } = 1 , \mathcal { F } } \frac { \partial \mathrm { x } _ { \mathrm { j } } } { \partial \mathrm { q } _ { \mathrm { i } } } \delta \mathrm { q } _ { \mathrm { i } } .
$$

The above expression can be rearranged to give

$$
\delta W = \sum _ { \mathrm { i } = 1 , \mathcal { F } } \mathrm { Q } _ { \mathrm { i } } \delta \mathbf { q } _ { \mathrm { i } } ,
$$

where

$$
\mathrm { Q } _ { \mathrm { i } } = \sum _ { \mathrm { j = 1 } , \mathcal { F } } \mathrm { f } _ { \mathrm { j } } \frac { \partial { x } _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } } .
$$

Here, the $\mathrm { Q } _ { \mathrm { i } }$ are termed generalized forces. Note that a generalized force does not necessarily have the dimensions of force. However, the product $\mathrm { Q } _ { \mathrm { i } } { \bf q } _ { \mathrm { i } }$ must have the dimensions of work. Thus, if a particular ${ \mathfrak { q } } _ { \mathrm { i } }$ is a Cartesian coordinate then the associated $\mathrm { Q } _ { \mathrm { i } }$ is a force. Conversely, if a particular ${ \mathfrak { q } } _ { \mathrm { i } }$ is an angle then the associated $\mathrm { Q _ { i } }$ is a torque.

Suppose that the dynamical system in question is conservative. It follows that

$$
\mathsf { f } _ { \mathrm { j } } = - \frac { \mathsf { \partial _ { \mathrm { 0 } } u } } { \mathsf { \partial _ { \mathrm { 0 } } } \mathsf { x _ { \mathrm { j } } } } ,
$$

for $\mathrm {  ~ j ~ } = 1 , \mathcal { F } _ { \mathrm { \scriptsize ~ } }$ , where $\mathsf { U } ( \mathsf { x } _ { 1 } , \mathsf { x } _ { 2 } , \cdots , \mathsf { x } _ { \mathcal { F } } , \mathsf { t } )$ is the system’s potential energy. Hence, according to Equation (7.6),

$$
\mathrm { Q _ { i } } = - \sum _ { \mathrm { j = 1 } , \mathcal { F } } \frac { \partial \mathrm { U } } { \partial \mathrm { x _ { j } } } \frac { \partial \mathrm { x _ { j } } } { \partial \mathrm { q _ { i } } } = - \frac { \partial \mathrm { U } } { \partial \mathrm { q _ { i } } } ,
$$

for $\mathfrak { i } = 1 , \mathcal { F }$ .

# 7.4 Lagrange’s Equation

The Cartesian equations of motion of our system take the form

$$
\mathfrak { m } _ { \mathrm { j } } \ddot { \mathfrak { x } } _ { \mathrm { j } } = \mathfrak { f } _ { \mathrm { j } } ,
$$

for $\mathrm {  ~ j ~ } = 1 , \mathcal { F } _ { \mathrm { \scriptsize { ) } } }$ , where $\mathfrak { m } _ { 1 } , \mathfrak { m } _ { 2 } , \mathfrak { m } _ { 3 }$ are each equal to the mass of the first particle, $\mathfrak { m } _ { 4 } , \mathfrak { m } _ { 5 }$ , $\mathfrak { m } _ { 6 }$ are each equal to the mass of the second particle, etc. Furthermore, the kinetic energy of the system can be written

$$
\mathsf { K } = \frac { 1 } { 2 } \sum _ { \mathrm { j } = 1 , \mathcal { F } } \mathsf { m } _ { \mathrm { j } } \dot { \mathsf { x } } _ { \mathrm { j } } ^ { 2 } .
$$

Now, since $\boldsymbol { x } _ { \mathrm { j } } = \boldsymbol { x } _ { \mathrm { j } } ( \boldsymbol { \mathsf { q } } _ { 1 } , \boldsymbol { \mathsf { q } } _ { 2 } , \cdots , \boldsymbol { \mathsf { q } } _ { \mathcal { F } } , \boldsymbol { \mathsf { t } } ) .$ , we can write

$$
\dot { { \boldsymbol { \mathrm { x } } } } _ { \mathrm { j } } = \sum _ { \mathrm { i = 1 } , { \mathcal { F } } } \frac { \partial { \boldsymbol { \mathrm { x } } } _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } } \dot { { \boldsymbol { \mathrm { q } } } } _ { \mathrm { i } } + \frac { \partial { \boldsymbol { \mathrm { x } } } _ { \mathrm { j } } } { \partial { \bf t } } ,
$$

for $\mathrm {  ~ j ~ } = 1 , \mathcal { F }$ . Hence, it follows that $\dot { x } _ { \mathrm { j } } = \dot { x } _ { \mathrm { j } } ( \dot { \bf q } _ { 1 } , \dot { \bf q } _ { 2 } , \dot { \bf \Xi } \cdot \dot { \bf \Xi } , \dot { \bf q } _ { \mathcal { F } } , { \bf q } _ { 1 } , { \bf q } _ { 2 } , \dot { \bf \Xi } \cdot \dot { \bf \Xi } , { \bf q } _ { \mathcal { F } } , { \bf t } )$ . According to the above equation,

$$
\frac { \partial \dot { \mathrm { x } } _ { \mathrm { j } } } { \partial \dot { \mathrm { q } } _ { \mathrm { i } } } = \frac { \partial \mathrm { x } _ { \mathrm { j } } } { \partial \mathrm { q } _ { \mathrm { i } } } ,
$$

where we are treating the $\dot { \mathsf { q } } _ { \mathrm { i } }$ and the ${ \mathfrak { q } } _ { \mathrm { i } }$ as independent variables.

Multiplying Equation (7.12) by $\dot { x } _ { \mathrm { j } }$ , and then differentiating with respect to time, we obtain

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \bigg ( \dot { x } _ { \mathrm { j } } { \frac { \partial \dot { x } _ { \mathrm { j } } } { \partial \dot { q } _ { \mathrm { i } } } } \bigg ) = { \frac { \mathrm { d } } { \mathrm { d t } } } \bigg ( \dot { x } _ { \mathrm { j } } { \frac { \partial x _ { \mathrm { j } } } { \partial { q } _ { \mathrm { i } } } } \bigg ) = \ddot { x } _ { \mathrm { j } } { \frac { \partial x _ { \mathrm { j } } } { \partial { q } _ { \mathrm { i } } } } + \dot { x } _ { \mathrm { j } } { \frac { \mathrm { d } } { \mathrm { d t } } } \bigg ( { \frac { \partial x _ { \mathrm { j } } } { \partial { q } _ { \mathrm { i } } } } \bigg ) .
$$

Now,

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \biggl ( { \frac { \partial x _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } } } \biggr ) = \sum _ { { \bf k } = 1 , { \mathcal { F } } } { \frac { \partial ^ { 2 } x _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } \partial { \bf q } _ { \mathrm { k } } } } { \dot { \bf q } } _ { \mathrm { k } } + { \frac { \partial ^ { 2 } x _ { \mathrm { j } } } { \partial { \bf q } _ { \mathrm { i } } \partial { \bf t } } } .
$$

Furthermore,

$$
\frac { 1 } { 2 } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { j } } ^ { 2 } } { \partial \dot { \mathrm { q } } _ { \mathrm { i } } } = \dot { \mathrm { x } } _ { \mathrm { j } } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { j } } } { \partial \dot { \mathrm { q } } _ { \mathrm { i } } } ,
$$

and

$$
\begin{array} { r c l } { \displaystyle \frac { 1 } { 2 } \frac { \partial \dot { \bf x } _ { \boldsymbol { \mathbf { j } } } ^ { 2 } } { \partial { \bf q } _ { \mathrm { i } } } = \dot { \bf x } _ { \boldsymbol { \mathbf { j } } } \frac { \partial \dot { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf q } _ { \mathrm { i } } } } & { = } & { \dot { { \bf x } } _ { \boldsymbol { \mathbf { j } } } \frac { \partial } { \partial { \bf q } _ { \mathrm { i } } } \left( \sum _ { { \bf k } = 1 , F } \frac { \partial { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf q } _ { \mathrm { k } } } \dot { \bf q } _ { \mathrm { k } } + \frac { \partial { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf t } } \right) } \\ & { = } & { \dot { { \bf x } } _ { \boldsymbol { \mathbf { j } } } \left( \sum _ { { \bf k } = 1 , F } \frac { \partial ^ { 2 } { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf q } _ { \mathrm { i } } \partial { \bf q } _ { \mathrm { k } } } \dot { \bf q } _ { \mathrm { k } } + \frac { \partial ^ { 2 } { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf q } _ { \mathrm { i } } \partial { \bf t } } \right) } \\ & { = } & { \dot { { \bf x } } _ { \boldsymbol { \mathbf { j } } } \frac { \mathrm { d } } { \mathrm { d t } } \left( \frac { \partial { \bf x } _ { \boldsymbol { \mathbf { j } } } } { \partial { \bf q } _ { \mathrm { i } } } \right) , } \end{array}
$$

where use has been made of Equation (7.14). Thus, it follows from Equations (7.13), (7.15), and (7.16) that

$$
\frac { \mathrm { d } } { \mathrm { d t } } \bigg ( \frac { 1 } { 2 } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { j } } ^ { 2 } } { \partial \dot { \mathrm { q } } _ { \mathrm { i } } } \bigg ) = \ddot { \mathrm { x } } _ { \mathrm { j } } \frac { \partial \mathrm { x } _ { \mathrm { j } } } { \partial \mathrm { q } _ { \mathrm { i } } } + \frac { 1 } { 2 } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { j } } ^ { 2 } } { \partial \mathrm { q } _ { \mathrm { i } } } .
$$

Let us take the above equation, multiply by ${ \mathfrak { m } } _ { \mathrm { j } }$ , and then sum over all j. We obtain

$$
\frac { \mathrm { d } } { \mathrm { d t } } \left( \frac { \partial \mathsf { K } } { \partial \dot { \mathsf { q } } _ { \mathrm { i } } } \right) = \sum _ { \mathrm { j } = 1 , \mathcal { F } } \mathsf { f } _ { \mathrm { j } } \frac { \partial \mathsf { x } _ { \mathrm { j } } } { \partial \mathsf { q } _ { \mathrm { i } } } + \frac { \partial \mathsf { K } } { \partial \mathsf { q } _ { \mathrm { i } } } ,
$$

where use has been made of Equations (7.9) and (7.10). Thus, it follows from Equation (7.6) that

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \left( { \frac { \partial { \mathsf { K } } } { \partial { \dot { \mathsf { q } } } _ { \mathrm { i } } } } \right) = \mathsf { Q } _ { \mathrm { i } } + { \frac { \partial { \mathsf { K } } } { \partial \mathsf { q } _ { \mathrm { i } } } } .
$$

Finally, making use of Equation (7.8), we get

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \biggl ( { \frac { \partial \mathsf { K } } { \partial { \dot { \mathsf { q } } } _ { \mathrm { i } } } } \biggr ) = - { \frac { \partial \mathsf { U } } { \partial \mathsf { q } _ { \mathrm { i } } } } + { \frac { \partial \mathsf { K } } { \partial \mathsf { q } _ { \mathrm { i } } } } .
$$

It is helpful to introduce a function L, called the Lagrangian, which is defined as the difference between the kinetic and potential energies of the dynamical system under investigation:

$$
{ \mathsf { L } } = { \mathsf { K } } - { \mathsf { U } } .
$$

Since the potential energy U is clearly independent of the $\dot { \mathsf { q } } _ { \mathrm { i } }$ , it follows from Equation (7.20) that

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \left( { \frac { \partial \mathrm { L } } { \partial { \dot { \mathbf { q } } } _ { \mathrm { i } } } } \right) - { \frac { \partial \mathrm { L } } { \partial \mathbf { q } _ { \mathrm { i } } } } = 0 ,
$$

for $\mathfrak { i } = 1 , \mathcal { F }$ . This equation is known as Lagrange’s equation.

According to the above analysis, if we can express the kinetic and potential energies of our dynamical system solely in terms of our generalized coordinates and their time derivatives then we can immediately write down the equations of motion of the system, expressed in terms of the generalized coordinates, using Lagrange’s equation, (7.22). Unfortunately, this scheme only works for conservative systems. Let us now consider some examples.

Consider a particle of mass m moving in two dimensions in the central potential $\mathsf { U } ( \boldsymbol { \mathsf { r } } )$ . This is clearly a two degree of freedom dynamical system. As described in Section 4.4, the particle’s instantaneous position is most conveniently specified in terms of the plane polar coordinates r and θ. These are our two generalized coordinates. According to Equation (4.13), the square of the particle’s velocity can be written

$$
\nu ^ { 2 } = \dot { \mathsf { r } } ^ { 2 } + ( \mathsf { r } \dot { \mathsf { \Theta } } ) ^ { 2 } .
$$

Hence, the Lagrangian of the system takes the form

$$
\mathsf { L } = \frac { 1 } { 2 } \mathsf { m } ( \dot { \mathsf { r } } ^ { 2 } + \mathsf { r } ^ { 2 } \dot { \Theta } ^ { 2 } ) - \mathsf { U } ( \mathsf { r } ) .
$$

Note that

$$
\begin{array} { c c } { { \displaystyle \frac { \partial \mathrm { L } } { \partial \dot { \mathbf { r } } } = \mathfrak { m } \dot { \mathfrak { r } } , \qquad } } & { { \displaystyle \frac { \partial \mathrm { L } } { \partial \mathfrak { r } } = \mathfrak { m } \Upsilon \dot { \theta } ^ { 2 } - \frac { \mathrm { d } \mathrm { U } } { \mathrm { d } \mathfrak { r } } , } } \\ { { \displaystyle \frac { \partial \mathrm { L } } { \partial \dot { \theta } } = \mathfrak { m } \mathfrak { r } ^ { 2 } \dot { \theta } , \qquad } } & { { \displaystyle \frac { \partial \mathrm { L } } { \partial \theta } = 0 . } } \end{array}
$$

Now, Lagrange’s equation (7.22) yields the equations of motion,

$$
\begin{array} { r l r } { \displaystyle \frac { \mathrm { d } } { \mathrm { d t } } \bigg ( \frac { \partial \mathrm { L } } { \partial \dot { \mathrm { r } } } \bigg ) - \frac { \partial \mathrm { L } } { \partial \mathrm { r } } } & { = } & { 0 , } \\ { \displaystyle \frac { \mathrm { d } } { \mathrm { d t } } \bigg ( \frac { \partial \mathrm { L } } { \partial \dot { \theta } } \bigg ) - \frac { \partial \mathrm { L } } { \partial \theta } } & { = } & { 0 . } \end{array}
$$

Hence, we obtain

$$
\begin{array} { r c l } { \displaystyle \frac { \mathrm { d } } { \mathrm { d t } } ( { \mathsf { m } } \dot { \mathsf { r } } ) - \mathsf { m r } \dot { \theta } ^ { 2 } + \frac { \mathrm { d } \mathsf { U } } { \mathrm { d r } } } & { = } & { 0 , } \\ { \displaystyle \frac { \mathrm { d } } { \mathrm { d t } } \big ( { \mathsf { m } } { \mathsf { r } } ^ { 2 } \dot { \theta } \big ) = 0 , } \end{array}
$$

or

$$
\begin{array} { r c l } { { \displaystyle { \ddot { r } } - r { \dot { \theta } } ^ { 2 } } } & { { = } } & { { \displaystyle - { \frac { \mathrm { d } V } { \mathrm { d } r } } , } } \\ { { \displaystyle r ^ { 2 } { \dot { \theta } } } } & { { = } } & { { \mathrm { h } , } } \end{array}
$$

where $\lor = \mathrm { u } / \mathrm { m }$ , and $\mathrm { \hslash }$ is a constant. We recognize Equations (7.31) and (7.32) as the equations we derived in Chapter 4 for motion in a central potential. The advantage of the Lagrangian method of deriving these equations is that we avoid having to express the acceleration in terms of the generalized coordinates r and θ.

# 7.5 Generalized Momenta

Consider the motion of a single particle moving in one dimension. The kinetic energy is

$$
\mathsf { K } = \frac { 1 } { 2 } \mathsf { m } \dot { \mathsf { x } } ^ { 2 } ,
$$

where m is the mass of the particle, and $x$ its displacement. Now, the particle’s linear momentum is ${ \mathfrak { p } } = { \mathfrak { m } } { \dot { \mathfrak { x } } }$ . However, this can also be written

$$
{ \mathfrak { p } } = { \frac { \partial { \mathsf { K } } } { \partial { \dot { \mathfrak { x } } } } } = { \frac { \partial { \mathsf { L } } } { \partial { \dot { \mathfrak { x } } } } } ,
$$

since ${ \mathsf { L } } = { \mathsf { K } } - { \mathsf { U } }$ , and the potential energy $\mathrm { u }$ is independent of $\dot { x }$ .

Consider a dynamical system described by $\mathcal { F }$ generalized coordinates ${ \mathfrak { q } } _ { \mathrm { i } }$ , for $\mathfrak { i } = 1 , \mathcal { F }$ By analogy with the above expression, we can define generalized momenta of the form

$$
{ \mathfrak { p } } _ { \mathrm { i } } = { \frac { \partial { \mathrm { L } } } { \partial { \dot { \mathbf { q } } } _ { \mathrm { i } } } } ,
$$

for $\mathfrak { i } = 1 , \mathcal { F }$ . Here, ${ \mathfrak { p } } _ { \mathrm { i } }$ is sometimes called the momentum conjugate to the coordinate ${ \mathfrak { q } } _ { \mathrm { i } }$ . Hence, Lagrange’s equation (7.22) can be written

$$
\frac { \mathrm { d } \mathsf { p } _ { \mathrm { i } } } { \mathrm { d t } } = \frac { \partial \mathsf { L } } { \partial \mathsf { q } _ { \mathrm { i } } } ,
$$

for $\mathfrak { i } = 1 , \mathcal { F }$ . Note that a generalized momentum does not necessarily have the dimensions of linear momentum.

Suppose that the Lagrangian L does not depend explicitly on some coordinate ${ \bf q } _ { \bf k }$ . It follows from Equation (7.36) that

$$
\frac { \mathrm { d } \mathsf { p } _ { \mathrm { k } } } { \mathrm { d t } } = \frac { \partial \mathrm { L } } { \partial \mathsf { q } _ { \mathrm { k } } } = 0 .
$$

Hence,

$$
\mathsf { p } _ { \mathrm { k } } = \mathsf { c o n s t . }
$$

The coordinate ${ \mathfrak { q } } _ { \mathtt { k } }$ is said to be ignorable in this case. Thus, we conclude that the generalized momentum associated with an ignorable coordinate is a constant of the motion.

For example, the Lagrangian (7.24) for a particle moving in a central potential is inde pendent of the angular coordinate θ. Thus, $\theta$ is an ignorable coordinate, and

$$
{ \mathfrak { p } } _ { \Theta } = { \frac { \partial { \mathsf { L } } } { \partial { \dot { \Theta } } } } = { \mathfrak { m } } \ r ^ { 2 } { \dot { \Theta } }
$$

is a constant of the motion. Of course, ${ \tt p } _ { \theta }$ is the angular momentum about the origin. This is conserved because a central force exerts no torque about the origin.

# 7.6 Exercises

7.1. A horizontal rod AB rotates with constant angular velocity $\omega$ about its midpoint O. A particle $\mathsf { P }$ is attached to it by equal strings AP, BP. If θ is the inclination of the plane APB to the vertical, prove that

$$
{ \frac { \mathrm { d } ^ { 2 } \theta } { \mathrm { d t } ^ { 2 } } } - \omega ^ { 2 } \sin { \theta } \cos { \theta } = - { \frac { 9 } { 1 } } \sin { \theta } ,
$$

where ${ \mathsf { l } } = { \mathsf { O P } }$ . Deduce the condition that the vertical position of OP should be stable.

7.2. A double pendulum consists of two simple pendula, with one pendulum suspended from the bob of the other. If the two pendula have equal lengths, l, and have bobs of equal mass, m, and if both pendula are confined to move in the same vertical plane, find Lagrange’s equations of motion for the system. Use $\theta$ and $\Phi$ —the angles the upper and lower pendulums make with the downward vertical (respectively)—as the generalized coordinates. Do not assume small angles.

7.3. Find Lagrange’s equations of motion for an elastic pendulum consisting of a particle of mass m attached to an elastic string of stiffness $\boldsymbol { \mathrm { k } }$ and unstretched length $\mathsf { l } _ { 0 }$ . Assume that the motion takes place in a vertical plane.

7.4. A disk of mass $M$ and radius R rolls without slipping down a plane inclined at an angle $\propto$ to the horizontal. The disk has a short weightless axle of negligible radius. From this axle is suspended a simple pendulum of length $\mathrm { \Delta } \mathrm { l } < \mathrm { R }$ whose bob is of mass m. Assume that the motion of the pendulum takes place in the plane of the disk. Find Lagrange’s equations of motion of the system.

![](images/6c6ddd5a5f575aba7a905aaa599b5247cd46fe4dde00bae204aae364f1760a02.jpg)

7.5. A vertical circular hoop of radius a is rotated in a vertical plane about a point $\mathsf { P }$ on its circumference at the constant angular velocity ω. A bead of mass m slides without friction on the hoop. Find the kinetic energy, the potential energy, the Lagrangian, and Largrange’s equation of motion of the bead, respectively, in terms of the angular coordinate $\theta$ shown in the above diagram. Here, $x$ is a horizontal Cartesian coordinate, $z$ a vertical Cartesian coordinate, and C the center of the hoop.

7.6. The kinetic energy of a rotating rigid object with an axis of symmetry can be written

$$
\mathsf { K } = \frac { 1 } { 2 } \left[ \mathsf { I } _ { \perp } \dot { \theta } ^ { 2 } + \left( \mathsf { I } _ { \perp } \sin ^ { 2 } \theta + \mathsf { I } _ { \| } \cos ^ { 2 } \theta \right) \dot { \phi } ^ { 2 } + 2 \mathsf { I } _ { \| } \cos \theta \dot { \phi } \dot { \psi } + \mathsf { I } _ { \| } \dot { \Psi } ^ { 2 } \right] ,
$$

where $\mathrm { I } _ { \parallel }$ is the moment of inertia about the symmetry axis, $\mathrm { I _ { \perp } }$ is the moment of inertia about an axis perpendicular to the symmetry axis, and $\theta , \Phi ,$ $\Phi , \Psi$ are the three Euler angles. Suppose that the object is rotating freely. Find the momenta conjugate to the Euler angles. Which of these momenta are conserved? Find Lagrange’s equations of motion for the system. Demonstrate that if the system is precessing steadily (which implies that $\theta , { \dot { \Phi } }$ , and $\dot { \Psi }$ are constants) then

$$
\dot { \Psi } = \left( \frac { \mathrm { I } _ { \perp } - \mathrm { I } _ { \parallel } } { \mathrm { I } _ { \parallel } } \right) \cos \theta \dot { \Phi } .
$$

# 8 Rigid Body Rotation

# 8.1 Introduction

This chapter examines the rotation of rigid bodies (e.g., the Planets) in three dimensions.

# 8.2 Fundamental Equations

We can think of a rigid body as a collection of a large number of small mass elements which all maintain a fixed spatial relationship with respect to one another. Let there be $\mathsf { N }$ elements, and let the ith element be of mass $\mathfrak { m } _ { \mathrm { i } }$ , and instantaneous position vector $\mathbf { r } _ { \mathrm { i } }$ . The equation of motion of the ith element is written

$$
\mathfrak { m } _ { \mathrm { i } } \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } ^ { 2 } } = \sum _ { \mathrm { j = 1 , N } } ^ { \mathrm { j } \ne \mathrm { i } } \mathbf { f } _ { \mathrm { i j } } + \mathbf { F } _ { \mathrm { i } } .
$$

Here, $\mathbf { f } _ { \mathrm { i j } }$ is the internal force exerted on the ith element by the jth element, and $\mathbf { F } _ { \mathrm { i } }$ the external force acting on the ith element. The internal forces $\mathbf { f } _ { \mathrm { i j } }$ represent the stresses which develop within the body in order to ensure that its various elements maintain a constant spatial relationship with respect to one another. Of course, $\mathbf { f } _ { \mathrm { i j } } = - \mathbf { f } _ { \mathrm { j i } }$ , by Newton’s third law. The external forces represent forces which originate outside the body.

Repeating the analysis of Section 2.6, we can sum Equation (8.1) over all mass elements to obtain

$$
M \frac { \mathrm { d } ^ { 2 } \mathbf { r } _ { \mathrm { c m } } } { \mathrm { d t } ^ { 2 } } = \mathbf { F } .
$$

Here, $\begin{array} { r } { M = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathfrak { m } _ { \mathrm { i } } } \end{array}$ is the total mass, $\mathbf { r } _ { \mathrm { c m } }$ the position vector of the center of mass [see Equation (2.27)], and $\begin{array} { r } { \mathbf { F } = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathbf { F } _ { \mathrm { i } } } \end{array}$ the total external force. It can be seen that the center of mass of a rigid body moves under the action of the external forces like a point particle whose mass is identical with that of the body.

Again repeating the analysis of Section 2.6, we can sum $\mathbf { r } _ { \mathrm { { i } } } \times$ Equation (8.1) over all mass elements to obtain

$$
\frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } = \mathbf { T } .
$$

Here, $\begin{array} { r } { \mathbf { L } = \sum _ { \mathrm { i = 1 , N } } \mathfrak { m } _ { \mathrm { i } } \mathfrak { r } _ { \mathrm { i } } \times \mathrm { d } \mathbf { r } _ { \mathrm { i } } / \mathrm { d t } } \end{array}$ is the total angular momentum of the body (about the origin), and $\begin{array} { r } { \mathbf { T } = \sum _ { \mathrm { i = 1 , N } } \mathbf { r } _ { \mathrm { i } } \times \mathbf { F } _ { \mathrm { i } } } \end{array}$ the total external torque (about the origin). Note that the above equation is only valid if the internal forces are central in nature. However, this is not a particularly onerous constraint. Equation (8.3) describes how the angular momentum of a rigid body evolves in time under the action of the external torques.

In the following, we shall only consider the rotational motion of rigid bodies, since their translational motion is similar to that of point particles [see Equation (8.2)], and, therefore, fairly straightforward in nature.

![](images/caec2de9bf93ce863d05e407210bf5b175f28d847a8682a453a971135ef14e55.jpg)  
Figure 8.1: A rigid rotating body.

# 8.3 Moment of Inertia Tensor

Consider a rigid body rotating with fixed angular velocity $\omega$ about an axis which passes through the origin—see Figure 8.1. Let $\mathbf { r } _ { \mathrm { i } }$ be the position vector of the ith mass element, whose mass is $\mathfrak { m } _ { \mathrm { i } }$ . We expect this position vector to precess about the axis of rotation (which is parallel to $\omega$ ) with angular velocity $\omega$ . It, therefore, follows from Equation (A.49) that

$$
{ \frac { \mathrm { d } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } } } = { \boldsymbol { \omega } } \times \mathbf { r } _ { \mathrm { i } } .
$$

Thus, the above equation specifies the velocity, $\mathbf { v } _ { \mathrm { i } } = \mathrm { d } \mathbf { r } _ { \mathrm { i } } / \mathrm { d t }$ , of each mass element as the body rotates with fixed angular velocity $\omega$ about an axis passing through the origin.

The total angular momentum of the body (about the origin) is written

$$
\mathbf { L } = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathrm { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times { \frac { \mathrm { d } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } } } = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathrm { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times ( \boldsymbol { \omega } \times \mathbf { r } _ { \mathrm { i } } ) = \sum _ { \mathrm { i } = 1 , \mathrm { N } } \mathrm { m } _ { \mathrm { i } } \left[ \mathbf { r } _ { \mathrm { i } } ^ { 2 } \boldsymbol { \omega } - \left( \mathbf { r } _ { \mathrm { i } } \cdot { \boldsymbol { \omega } } \right) \mathbf { r } _ { \mathrm { i } } \right] ,
$$

where use has been made of Equation (8.4), and some standard vector identities (see Section A.10). The above formula can be written as a matrix equation of the form

$$
\left( \begin{array} { l } { \mathrm { L } _ { x } } \\ { \mathrm { L } _ { y } } \\ { \mathrm { L } _ { z } } \end{array} \right) = \left( \begin{array} { l l l } { \mathrm { I } _ { x x } } & { \mathrm { I } _ { x y } } & { \mathrm { I } _ { x z } } \\ { \mathrm { I } _ { y x } } & { \mathrm { I } _ { y y } } & { \mathrm { I } _ { y z } } \\ { \mathrm { I } _ { z x } } & { \mathrm { I } _ { z y } } & { \mathrm { I } _ { z z } } \end{array} \right) \left( \begin{array} { l } { \omega _ { x } } \\ { \omega _ { y } } \\ { \omega _ { z } } \end{array} \right) ,
$$

where

$$
\begin{array} { r l r } { \mathrm { I } _ { x x } } & { = } & { \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } ( \mathsf { y } _ { \mathrm { i } } ^ { 2 } + z _ { \mathrm { i } } ^ { 2 } ) \mathsf { m } _ { \mathrm { i } } = \int ( \mathsf { y } ^ { 2 } + z ^ { 2 } ) \mathsf { d } \mathsf { m } , } \\ { \mathrm { I } _ { \mathsf { y y } } } & { = } & { \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } ( \mathsf { x } _ { \mathrm { i } } ^ { 2 } + z _ { \mathrm { i } } ^ { 2 } ) \mathsf { m } _ { \mathrm { i } } = \int ( \mathsf { x } ^ { 2 } + z ^ { 2 } ) \mathsf { d } \mathsf { m } , } \end{array}
$$

$$
\begin{array} { r l } { { \mathrm { I } _ { z z } } } & { = \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } { \mathrm { ( x _ \mathrm { i } ^ 2 + y _ \mathrm { i } ^ 2 ) } } { \mathrm { m } } _ { \mathrm { i } } = \displaystyle \int ( x ^ { 2 } + y ^ { 2 } ) { \mathrm { d } } { \mathrm { m } } , } \\ { { \mathrm { I } _ { \mathrm { x y } } } = { \mathrm { I } _ { \mathrm { y x } } } } & { = - \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } { \mathrm { x } _ { \mathrm { i } } \mathrm { y } _ { \mathrm { i } } { \mathrm { m } } _ { \mathrm { i } } } = - \int { \mathrm { x y } \mathrm { d } } { \mathrm { m } } , } \\ { { \mathrm { I } _ { \mathrm { y z } } } = { \mathrm { I } _ { \mathrm { z y } } } } & { = - \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } { \mathrm { y } _ { \mathrm { i } } { z } _ { \mathrm { i } } { \mathrm { m } } _ { \mathrm { i } } } = - \int { \mathrm { y } z } \mathrm { d } { \mathrm { m } } , } \\ { { \mathrm { I } _ { \mathrm { x z } } } = { \mathrm { I } _ { \mathrm { z x } } } } & { = - \displaystyle \sum _ { \mathrm { i } = 1 , \mathrm { N } } { \mathrm { x } _ { \mathrm { i } } { z } _ { \mathrm { i } } { \mathrm { m } } _ { \mathrm { i } } } = - \int { \mathrm { x } z } \mathrm { d } { \mathrm { m } } . } \end{array}
$$

Here, $\mathrm { I } _ { x x }$ is called the moment of inertia about the $x$ -axis, $\mathrm { I _ { y y } }$ the moment of inertia about the $_ { 9 }$ -axis, $\mathrm { I } _ { \mathrm { x y } }$ the $_ { x y }$ product of inertia, $\mathrm { I } _ { \mathsf { y } z }$ the $_ { 9 z }$ product of inertia, etc. The matrix of the $\mathrm { I _ { i j } }$ values is known as the moment of inertia tensor.1 Note that each component of the moment of inertia tensor can be written as either a sum over separate mass elements, or as an integral over infinitesimal mass elements. In the integrals, $\mathrm { d } \mathrm { m } = \rho \mathrm { d } \mathrm { V }$ , where $\rho$ is the mass density, and $\mathtt { d V }$ a volume element. Equation (8.6) can be written more succinctly as

$$
\mathbf { L } = \tilde { \mathbf { I } } \omega .
$$

Here, it is understood that $\mathbf { L }$ and $\omega$ are both column vectors, and $\tilde { \mathbf { I } }$ is the matrix of the $\mathrm { I _ { i j } }$ values. Note that ˜I is a real symmetric matrix: i.e., $\mathrm { I } _ { \mathrm { i } } ^ { \ast } = \mathrm { I } _ { \mathrm { i } } { } _ { \mathrm { j } }$ and $\mathrm { I _ { j i } = I _ { i j } }$ .

In general, the angular momentum vector, $\mathbf { L } ,$ obtained from Equation (8.13), points in a different direction to the angular velocity vector, $\omega$ . In other words, $\mathbf { L }$ is generally not parallel to ω.

Finally, although the above results were obtained assuming a fixed angular velocity, they remain valid at each instant in time if the angular velocity varies.

# 8.4 Rotational Kinetic Energy

The instantaneous rotational kinetic energy of a rotating rigid body is written

$$
\mathsf { K } = \frac { 1 } { 2 } \sum _ { \mathrm { i } = 1 , \mathsf { N } } \mathsf { m } _ { \mathrm { i } } \left( \frac { \mathrm { d } \mathbf { r } _ { \mathrm { i } } } { \mathrm { d t } } \right) ^ { 2 } .
$$

Making use of Equation (8.4), and some vector identities (see Section A.9), the kinetic energy takes the form

$$
\mathsf { K } = \frac { 1 } { 2 } \sum _ { \mathrm { i } = 1 , \mathsf { N } } \mathsf { m } _ { \mathrm { i } } \left( \boldsymbol { \omega } \times \mathbf { r } _ { \mathrm { i } } \right) \cdot \left( \boldsymbol { \omega } \times \mathbf { r } _ { \mathrm { i } } \right) = \frac { 1 } { 2 } \boldsymbol { \omega } \cdot \sum _ { \mathrm { i } = 1 , \mathsf { N } } \mathsf { m } _ { \mathrm { i } } \mathbf { r } _ { \mathrm { i } } \times \left( \boldsymbol { \omega } \times \mathbf { r } _ { \mathrm { i } } \right) .
$$

Hence, it follows from (8.5) that

$$
\mathsf { K } = \frac { 1 } { 2 } \mathsf { \Gamma } \omega \cdot \mathbf { L } .
$$

Making use of Equation (8.13), we can also write

$$
{ \sf K } = \frac { 1 } { 2 } { \sf \Gamma } { \sf \Gamma } ^ { \sf { I } } { \sf { I } } { \sf { W } } .
$$

Here, $\omega ^ { \intercal }$ is the row vector of the Cartesian components $\omega _ { x } , \omega _ { y } , \omega _ { z } ,$ which is, of course, the transpose (denoted T ) of the column vector $\omega$ . When written in component form, the above equation yields

$$
\mathsf { K } = \frac { 1 } { 2 } \left( \mathrm { I } _ { x x } \omega _ { x } ^ { 2 } + \mathrm { I } _ { y y } \omega _ { y } ^ { 2 } + \mathrm { I } _ { z z } \omega _ { z } ^ { 2 } + 2 \mathrm { I } _ { x y } \omega _ { x } \omega _ { y } + 2 \mathrm { I } _ { y z } \omega _ { y } \omega _ { z } + 2 \mathrm { I } _ { x z } \omega _ { x } \omega _ { z } \right) .
$$

# 8.5 Principal Axes of Rotation

We have seen that the moment of inertia tensor, ˜I, defined in Section 8.3, takes the form of a real symmetric three-dimensional matrix. It therefore follows, from the standard matrix theory discussed in Section B.2, that the moment of inertia tensor possesses three mutually orthogonal eigenvectors which are associated with three real eigenvalues. Let the ith eigenvector (which can be normalized to be a unit vector) be denoted $\widehat { \mathbf { \omega } } _ { \mathrm { { i } } } ^ { } .$ , and the ith eigenvalue $\lambda _ { \mathrm { i } }$ . It then follows that

$$
\widetilde { \mathbf { I } } \widehat { \mathbf { \omega } } _ { \mathrm { i } } = \lambda _ { \mathrm { i } } \widehat { \mathbf { \omega } } _ { \mathrm { i } } ,
$$

for $i = 1 , 3$

The directions of the three mutually orthogonal unit vectors $\widehat { \mathbf { \omega } } _ { \mathrm { { i } } }$ define the three socalled principal axes of rotation of the rigid body under investigation. These axes are special because when the body rotates about one of them (i.e., when ω is parallel to one of them) the angular momentum vector $\mathbf { L }$ becomes parallel to the angular velocity vector ω. This can be seen from a comparison of Equation (8.13) and Equation (8.19).

Suppose that we reorient our Cartesian coordinate axes such the they coincide with the mutually orthogonal principal axes of rotation. In this new reference frame, the eigenvectors of ˜I are the unit vectors, $\mathbf { e } _ { x } , \mathbf { e } _ { y }$ , and $\mathbf { e } _ { z }$ , and the eigenvalues are the moments of inertia about these axes, $\mathrm { I } _ { x x } , ~ \mathrm { I } _ { y y }$ , and $\mathrm { I } _ { z z }$ , respectively. These latter quantities are referred to as the principal moments of inertia. Note that the products of inertia are all zero in the new reference frame. Hence, in this frame, the moment of inertia tensor takes the form of a diagonal matrix: i.e.,

$$
\tilde { \bf I } = \left( \begin{array} { c c c } { \mathrm { I } _ { x x } } & { 0 } & { 0 } \\ { 0 } & { \mathrm { I } _ { y y } } & { 0 } \\ { 0 } & { 0 } & { \mathrm { I } _ { z z } } \end{array} \right) .
$$

Incidentally, it is easy to verify that $\mathbf { e } _ { x } , \mathbf { e } _ { y }$ , and $\mathbf { e } _ { z }$ are indeed the eigenvectors of the above matrix, with the eigenvalues $\mathrm { I } _ { \mathrm { x x } } , \ \mathrm { I } _ { \mathrm { y y } }$ , and $\mathrm { I } _ { z z }$ , respectively, and that $\mathbf { L } = \tilde { \mathbf { I } } \boldsymbol { \omega }$ is indeed parallel to ω whenever $\omega$ is directed along $\mathbf { e } _ { \mathrm { x } } , \mathbf { e } _ { \mathrm { y } }$ , or $\mathbf { e } _ { z }$ .

When expressed in our new coordinate system, Equation (8.13) yields

$$
\mathbf { L } = \left( \mathrm { I } _ { x x } \omega _ { x } , \mathrm { I } _ { y y } \omega _ { y } , \mathrm { I } _ { z z } \omega _ { z } \right) ,
$$

whereas Equation (8.18) reduces to

$$
\mathsf { K } = \frac { 1 } { 2 } \left( \mathrm { I } _ { x x } \boldsymbol { \omega } _ { x } ^ { 2 } + \mathrm { I } _ { y y } \boldsymbol { \omega } _ { y } ^ { 2 } + \mathrm { I } _ { z z } \boldsymbol { \omega } _ { z } ^ { 2 } \right) .
$$

In conclusion, there are many great simplifications to be had by choosing a coordinate system whose axes coincide with the principal axes of rotation of the rigid body under investigation.

# 8.6 Euler’s Equations

The fundamental equation of motion of a rotating body [see Equation (8.3)],

$$
\mathbf { T } = { \frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } } ,
$$

is only valid in an inertial frame. However, we have seen that L is most simply expressed in a frame of reference whose axes are aligned along the principal axes of rotation of the body. Such a frame of reference rotates with the body, and is, therefore, non-inertial. Thus, it is helpful to define two Cartesian coordinate systems with the same origins. The first, with coordinates $x , y , z ,$ , is a fixed inertial frame—let us denote this the fixed frame. The second, with coordinates $\ x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ , co-rotates with the body in such a manner that the $x ^ { \prime } .$ -, $y ^ { \prime } .$ -, and $z ^ { \prime }$ -axes are always pointing along its principal axes of rotation—we shall refer to this as the body frame. Since the body frame co-rotates with the body, its instantaneous angular velocity is the same as that of the body. Hence, it follows from the analysis in Section 6.2 that

$$
\frac { \mathrm { d } \mathbf { L } } { \mathrm { d t } } = \frac { \mathrm { d } \mathbf { L } } { \mathrm { d t ^ { \prime } } } + \omega \times \mathbf { L } .
$$

Here, $\mathrm { d } / \mathrm { d t }$ is the time derivative in the fixed frame, and $\mathrm { d } / \mathrm { d t } ^ { \prime }$ the time derivative in the body frame. Combining Equations (8.23) and (8.24), we obtain

$$
\mathbf { T } = { \frac { \mathrm { { d } } \mathbf { L } } { \mathrm { { d t } } ^ { \prime } } } + { \boldsymbol { \omega } } \times \mathbf { L } .
$$

Now, in the body frame let $\mathbf { T } = ( \mathbb { T } _ { \mathrm { x ^ { \prime } } } , \mathbb { T } _ { \mathrm { y ^ { \prime } } } , \mathbb { T } _ { \mathrm { z ^ { \prime } } } )$ and $\mathbf { \omega } \omega = ( \omega _ { x ^ { \prime } } , \omega _ { y ^ { \prime } } , \omega _ { z ^ { \prime } } )$ . It follows that $\mathbf { L } = \left( \mathrm { I } _ { x ^ { \prime } x ^ { \prime } } \omega _ { x ^ { \prime } } , \mathrm { I } _ { \mathrm { y ^ { \prime } y ^ { \prime } } } \omega _ { \mathrm { y ^ { \prime } } } , \mathrm { I } _ { z ^ { \prime } z ^ { \prime } } \omega _ { z ^ { \prime } } \right)$ , where $\mathrm { I } _ { \tt X ^ { \prime } \tt X ^ { \prime } } , \ \mathrm { I } _ { \tt y ^ { \prime } \tt y ^ { \prime } }$ and $\mathrm { I } _ { z ^ { \prime } z ^ { \prime } }$ are the principal moments of inertia. Hence, in the body frame, the components of Equation (8.25) yield

$$
\begin{array} { r l r } { { \sf T } _ { x ^ { \prime } } } & { = } & { { \sf I } _ { x ^ { \prime } x ^ { \prime } } \dot { \omega } _ { x ^ { \prime } } - \left( { \sf I } _ { y ^ { \prime } y ^ { \prime } } - { \sf I } _ { z ^ { \prime } z ^ { \prime } } \right) \omega _ { y ^ { \prime } } \omega _ { z ^ { \prime } } , } \\ { { \sf T } _ { y ^ { \prime } } } & { = } & { { \sf I } _ { y ^ { \prime } y ^ { \prime } } \dot { \omega } _ { y ^ { \prime } } - \left( { \sf I } _ { z ^ { \prime } z ^ { \prime } } - { \sf I } _ { x ^ { \prime } x ^ { \prime } } \right) \omega _ { z ^ { \prime } } \omega _ { x ^ { \prime } } , } \\ { { \sf T } _ { z ^ { \prime } } } & { = } & { { \sf I } _ { z ^ { \prime } z ^ { \prime } } \dot { \omega } _ { z ^ { \prime } } - \left( { \sf I } _ { x ^ { \prime } x ^ { \prime } } - { \sf I } _ { y ^ { \prime } y ^ { \prime } } \right) \omega _ { x ^ { \prime } } \omega _ { y ^ { \prime } } , } \end{array}
$$

where $\dot { { \bf { \theta } } } = \mathrm { d } / \mathrm { d } { \bf { t } } ^ { \prime }$ . Here, we have made use of the fact that the moments of inertia of a rigid body are constant in time in the co-rotating body frame. The above equations are known as Euler’s equations.

Consider a body that is freely rotating: i.e., in the absence of external torques. Furthermore, let the body be rotationally symmetric about the $z ^ { \prime }$ -axis. It follows that $\mathrm { I } _ { \tt X ^ { \prime } \tt X ^ { \prime } } = \mathrm { I } _ { \tt y ^ { \prime } \tt y ^ { \prime } } =$ $\mathrm { I _ { \perp } }$ . Likewise, we can write $\mathrm { I } _ { z ^ { \prime } z ^ { \prime } } = \mathrm { I } _ { \parallel }$ . In general, however, $\mathrm { I } _ { \perp } \neq \mathrm { I } _ { \| }$ . Thus, Euler’s equations yield

$$
\begin{array} { r l r } { \displaystyle \mathrm { I } _ { \perp } \frac { \mathrm { d } \omega _ { x ^ { \prime } } } { \mathrm { d } \mathrm { t } ^ { \prime } } + \left( \mathrm { I } _ { \| } - \mathrm { I } _ { \perp } \right) \omega _ { z ^ { \prime } } \omega _ { \mathsf { y } ^ { \prime } } } & { = } & { 0 , } \\ { \displaystyle \mathrm { I } _ { \perp } \frac { \mathrm { d } \omega _ { \mathsf { y ^ { \prime } } } } { \mathrm { d } \mathrm { t } ^ { \prime } } - \left( \mathrm { I } _ { \| } - \mathrm { I } _ { \perp } \right) \omega _ { z ^ { \prime } } \omega _ { \mathsf { x ^ { \prime } } } } & { = } & { 0 , } \\ { \displaystyle \frac { \mathrm { d } \omega _ { z ^ { \prime } } } { \mathrm { d } \mathrm { t } ^ { \prime } } } & { = } & { 0 . } \end{array}
$$

Clearly, $\omega _ { z ^ { \prime } }$ is a constant of the motion. Equation (8.29) and (8.30) can be written

$$
\begin{array} { r c l } { { \displaystyle \frac { \mathrm { d } \omega _ { x ^ { \prime } } } { \mathrm { d } \mathrm { t ^ { \prime } } } + \Omega \omega _ { y ^ { \prime } } } } & { { = } } & { { 0 , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \frac { \mathrm { d } \omega _ { y ^ { \prime } } } { \mathrm { d } \mathrm { t ^ { \prime } } } - \Omega \omega _ { x ^ { \prime } } } } & { { = } } & { { 0 , } } \end{array}
$$

where $\Omega = \left( \mathrm { I } _ { \| } / \mathrm { I } _ { \perp } - 1 \right) \omega _ { z ^ { \prime } }$ . As is easily demonstrated, the solution to the above equations is

$$
\begin{array} { r l r } { \omega _ { x ^ { \prime } } } & { = } & { \omega _ { \perp } \cos ( \Omega \mathfrak { t } ^ { \prime } ) , } \\ { \omega _ { \mathfrak { y ^ { \prime } } } } & { = } & { \omega _ { \perp } \sin ( \Omega \mathfrak { t } ^ { \prime } ) , } \end{array}
$$

where $\omega _ { \perp }$ is a constant. Thus, the projection of the angular velocity vector onto the $\mathsf { x } ^ { \prime } \ – \mathsf { y } ^ { \prime }$ plane has the fixed length $\omega _ { \perp }$ , and rotates steadily about the $z ^ { \prime }$ -axis with angular velocity $\Omega$ . It follows that the length of the angular velocity vector, $\omega = ( \omega _ { x ^ { \prime } } ^ { 2 } + \omega _ { y ^ { \prime } } ^ { 2 } + \omega _ { z ^ { \prime } } ^ { 2 } ) ^ { 1 / 2 }$ , is a constant of the motion. Clearly, the angular velocity vector subtends some constant angle, $\alpha$ , with the $z ^ { \prime }$ -axis, which implies that $\omega _ { z ^ { \prime } } = \omega$ cos $\propto$ and $\omega _ { \perp } = \omega$ sin $\propto$ . Hence, the components of the angular velocity vector are

$$
\begin{array} { r c l } { { \omega _ { x ^ { \prime } } } } & { { = } } & { { \omega \sin \alpha \cos ( \Omega \mathbf { t } ^ { \prime } ) , } } \\ { { } } & { { } } & { { } } \\ { { \omega _ { y ^ { \prime } } } } & { { = } } & { { \omega \sin \alpha \sin ( \Omega \mathbf { t } ^ { \prime } ) , } } \\ { { } } & { { } } & { { } } \\ { { \omega _ { z ^ { \prime } } } } & { { = } } & { { \omega \cos \alpha , } } \end{array}
$$

where

$$
\Omega = \omega \cos \propto \left( \frac { \mathrm { I } _ { \| } } { \mathrm { I } _ { \perp } } - 1 \right) .
$$

We conclude that, in the body frame, the angular velocity vector precesses about the symmetry axis (i.e., the $z ^ { \prime }$ -axis) with the angular frequency $\Omega$ . Now, the components of the

angular momentum vector are

$$
\begin{array} { r c l } { \mathrm { L } _ { x ^ { \prime } } } & { = } & { \mathrm { I } _ { \perp } \omega \sin \alpha \cos ( \Omega \mathrm { t } ^ { \prime } ) , } \\ { \mathrm { L } _ { \mathrm { y ^ { \prime } } } } & { = } & { \mathrm { I } _ { \perp } \omega \sin \alpha \sin ( \Omega \mathrm { t } ^ { \prime } ) , } \\ { \mathrm { L } _ { z ^ { \prime } } } & { = } & { \mathrm { I } _ { \parallel } \omega \cos \alpha . } \end{array}
$$

Thus, in the body frame, the angular momentum vector is also of constant length, and precesses about the symmetry axis with the angular frequency $\Omega$ . Furthermore, the angular momentum vector subtends a constant angle $\theta$ with the symmetry axis, where

$$
\tan \theta = { \frac { \mathrm { I _ { \perp } } } { \mathrm { I _ { \parallel } } } } \tan \alpha .
$$

Note that the angular momentum vector, the angular velocity vector, and the symmetry axis all lie in the same plane: i.e., $\mathbf { e } _ { z ^ { \prime } } \cdot \mathbf { L } \times \omega = 0$ , as can easily be verified. Moreover, the angular momentum vector lies between the angular velocity vector and the symmetry axis (i.e., $\theta < \alpha )$ for a flattened (or oblate) body (i.e., $\mathrm { I _ { \perp } } < \mathrm { I _ { \parallel } } )$ , whereas the angular velocity vector lies between the angular momentum vector and the symmetry axis (i.e., $\theta > \alpha \mathrm { ] }$ ) for an elongated (or prolate) body (i.e., $\mathrm { I _ { \perp } } > \mathrm { I _ { \parallel } } )$ .

# 8.7 Eulerian Angles

We have seen how we can solve Euler’s equations to determine the properties of a rotating body in the co-rotating body frame. Let us now investigate how we can determine the same properties in the inertial fixed frame.

The fixed frame and the body frame share the same origin. Hence, we can transform from one to the other by means of an appropriate rotation of our coordinate axes. In general, if we restrict ourselves to rotations about one of the Cartesian axes, three successive rotations are required to transform the fixed frame into the body frame. There are, in fact, many different ways to combined three successive rotations in order to achieve this. In the following, we shall describe the most widely used method, which is due to Euler.

We start in the fixed frame, which has coordinates $x , y , z$ , and unit vectors $\mathbf { e } _ { x }$ , $\mathbf { e } _ { \mathfrak { y } }$ , $\mathbf { e } _ { z }$ . Our first rotation is counterclockwise (looking down the axis) through an angle $\Phi$ about the $z$ -axis. The new frame has coordinates $x ^ { \prime \prime }$ , $\ y ^ { \prime \prime } , z ^ { \prime \prime }$ , and unit vectors $\mathbf { e } _ { \mathrm { x ^ { \prime \prime } } }$ , ${ \bf { e } } _ { \bf { y } ^ { \prime \prime } }$ , $\mathbf { e } _ { z ^ { \prime \prime } }$ . According to Equations (A.17)–(A.19), the transformation of coordinates can be represented as follows:

$$
\left( \begin{array} { c } { x ^ { \prime \prime } } \\ { \mathsf { y } ^ { \prime \prime } } \\ { z ^ { \prime \prime } } \end{array} \right) = \left( \begin{array} { c c c } { \cos \Phi } & { \sin \Phi } & { 0 } \\ { - \sin \Phi } & { \cos \Phi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c } { x } \\ { \mathsf { y } } \\ { z } \end{array} \right) .
$$

The angular velocity vector associated with $\Phi$ has the magnitude $\dot { \Phi }$ , and is directed along $\mathbf { e } _ { z }$ (i.e., along the axis of rotation). Hence, we can write

$$
\begin{array} { r } { \omega _ { \phi } = \dot { \Phi } \mathbf { e } _ { z } . } \end{array}
$$

Clearly, $\dot { \Phi }$ is the precession rate about the $z$ -axis, as seen in the fixed frame.

The second rotation is counterclockwise (looking down the axis) through an angle $\theta$ about the $x ^ { \prime \prime }$ -axis. The new frame has coordinates $\cdot ^ { \prime \prime \prime }$ , $\ y ^ { \prime \prime \prime } , z ^ { \prime \prime \prime }$ , and unit vectors $\mathbf { e } _ { x ^ { \prime \prime \prime } }$ , $\mathbf { e _ { \mathrm { y ^ { \prime \prime \prime } } } }$ , $\mathbf { e } _ { z ^ { \prime \prime \prime } }$ . By analogy with Equation (8.44), the transformation of coordinates can be represented as follows:

$$
\left( \begin{array} { c } { { x ^ { \prime \prime \prime } } } \\ { { y ^ { \prime \prime \prime } } } \\ { { z ^ { \prime \prime \prime } } } \end{array} \right) = \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \cos \Theta } } & { { \sin \Theta } } \\ { { 0 } } & { { - \sin \Theta } } & { { \cos \Theta } } \end{array} \right) \left( \begin{array} { c } { { x ^ { \prime \prime } } } \\ { { y ^ { \prime \prime } } } \\ { { z ^ { \prime \prime } } } \end{array} \right) .
$$

The angular velocity vector associated with θ has the magnitude $\dot { \theta }$ , and is directed along $\mathbf { e } _ { \mathrm { x ^ { \prime \prime } } }$ (i.e., along the axis of rotation). Hence, we can write

$$
\mathbf { \omega } \omega _ { \theta } = \dot { \theta } \mathbf { e } _ { x ^ { \prime \prime } } .
$$

The third rotation is counterclockwise (looking down the axis) through an angle $\psi$ about the $z ^ { \prime \prime \prime }$ -axis. The new frame is the body frame, which has coordinates $\ x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ , and unit vectors $\mathbf { \Sigma } _ { \subset { \bf x } ^ { \prime } } ^ { \bullet } , \mathbf { e } _ { \bf y ^ { \prime } } , \mathbf { e } _ { z ^ { \prime } }$ . The transformation of coordinates can be represented as follows:

$$
\begin{array} { r } { \left( \begin{array} { c } { x ^ { \prime } } \\ { \mathsf { y } ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c } { \cos \psi } & { \sin \psi } & { 0 } \\ { - \sin \psi } & { \cos \psi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c } { x ^ { \prime \prime \prime } } \\ { \mathsf { y } ^ { \prime \prime \prime } } \\ { z ^ { \prime \prime \prime } } \end{array} \right) . } \end{array}
$$

The angular velocity vector associated with $\psi$ has the magnitude $\dot { \Psi }$ , and is directed along $\mathbf { e } _ { z ^ { \prime \prime } }$ (i.e., along the axis of rotation). Note that $\mathbf { e } _ { z ^ { \prime \prime \prime } } = \mathbf { e } _ { z ^ { \prime } }$ , since the third rotation is about $\mathbf { e } _ { z ^ { \prime \prime \prime } }$ . Hence, we can write

$$
\begin{array} { r } { \omega _ { \Psi } = \dot { \Psi } \mathbf { e } _ { z ^ { \prime } } . } \end{array}
$$

Clearly, $\dot { \Psi }$ is minus the precession rate about the $z ^ { \prime }$ -axis, as seen in the body frame.

The full transformation between the fixed frame and the body frame is rather complicated. However, the following results can easily be verified:

$$
{ \begin{array} { r c l } { { \mathbf { e } } _ { z } } & { = } & { \sin \Psi \sin \theta \mathbf { e } _ { x ^ { \prime } } + \cos \Psi \sin \theta \mathbf { e } _ { \mathrm { y ^ { \prime } } } + \cos \theta \mathbf { e } _ { z ^ { \prime } } , } \\ { } & { } & { } \\ { { \mathbf { e } } _ { x ^ { \prime \prime } } } & { = } & { \cos \Psi \mathbf { e } _ { x ^ { \prime } } - \sin \Psi \mathbf { e } _ { \mathrm { y ^ { \prime } } } . } \end{array} }
$$

It follows from Equation (8.50) that ${ \bf e } _ { z } \cdot { \bf e } _ { z ^ { \prime } } = \cos \theta$ . In other words, θ is the angle of inclination between the $z -$ and $z ^ { \prime }$ -axes. Finally, since the total angular velocity can be written

$$
\begin{array} { r } { \mathbf { \omega } = \mathbf { \omega } \omega _ { \phi } + \mathbf { \omega } \omega _ { \theta } + \mathbf { \omega } \omega _ { \psi } , } \end{array}
$$

Equations (8.45), (8.47), and (8.49)–(8.51) yield

$$
\begin{array} { r c l } { { \omega _ { x ^ { \prime } } } } & { { = } } & { { \sin \psi \sin \theta \dot { \phi } + \cos \psi \dot { \theta } , } } \\ { { \omega _ { \psi ^ { \prime } } } } & { { = } } & { { \cos \psi \sin \theta \dot { \phi } - \sin \psi \dot { \theta } , } } \\ { { \omega _ { z ^ { \prime } } } } & { { = } } & { { \cos \theta \dot { \phi } + \dot { \psi } . } } \end{array}
$$

The angles $\Phi , \theta$ , and $\psi$ are termed Eulerian angles. Each has a clear physical interpretation: $\Phi$ is the angle of precession about the $z$ -axis in the fixed frame, $\psi$ is minus the angle of precession about the $z ^ { \prime }$ -axis in the body frame, and θ is the angle of inclination between the $z -$ and $z ^ { \prime }$ -axes. Moreover, we can express the components of the angular velocity vector ω in the body frame entirely in terms of the Eulerian angles, and their time derivatives [see Equations (8.53)–(8.55)].

Consider a freely rotating body that is rotationally symmetric about one axis (the $z ^ { \prime }$ - axis). In the absence of an external torque, the angular momentum vector $\mathbf { L }$ is a constant of the motion [see Equation (8.3)]. Let $\mathbf { L }$ point along the $z$ -axis. In the previous section, we saw that the angular momentum vector subtends a constant angle θ with the axis of symmetry: i.e., with the $z ^ { \prime }$ -axis. Hence, the time derivative of the Eulerian angle θ is zero. We also saw that the angular momentum vector, the axis of symmetry, and the angular velocity vector are coplanar. Consider an instant in time at which all of these vectors lie in the $y ^ { \prime } – z ^ { \prime }$ plane. This implies that $\omega _ { \mathrm { x ^ { \prime } } } = 0$ . According to the previous section, the angular velocity vector subtends a constant angle $\propto$ with the symmetry axis. It follows that $\omega _ { \mathsf { y ^ { \prime } } } = \omega$ sin $\propto$ and $\omega _ { z ^ { \prime } } = \omega \cos \alpha$ . Equation (8.53) gives $\psi = 0$ . Hence, Equation (8.54) yields

$$
\omega \sin \alpha = \sin \theta { \dot { \phi } } .
$$

This can be combined with Equation (8.43) to give

$$
\dot { \Phi } = \omega \left[ 1 + \left( \frac { \mathrm { I } _ { \parallel } ^ { 2 } } { \mathrm { I } _ { \perp } ^ { 2 } } - 1 \right) \cos ^ { 2 } \alpha \right] ^ { 1 / 2 } .
$$

Finally, Equation (8.55), together with (8.43) and (8.56), yields

$$
\dot { \psi } = \omega \cos \alpha - \cos \theta \dot { \phi } = \omega \cos \alpha \left( 1 - \frac { \tan \alpha } { \tan \theta } \right) = \omega \cos \alpha \left( 1 - \frac { \mathrm { I } _ { \parallel } } { \mathrm { I } _ { \perp } } \right) .
$$

A comparison of the above equation with Equation (8.39) gives

$$
\dot { \Psi } = - { \Omega } .
$$

Thus, as expected, $\dot { \Psi }$ is minus the precession rate (of the angular momentum and angular velocity vectors) in the body frame. On the other hand, $\dot { \Phi }$ is the precession rate (of the angular velocity vector and the symmetry axis) in the fixed frame. Note that $\dot { \Phi }$ and $\Omega$ are quite dissimilar. For instance, $\Omega$ is negative for elongated bodies $( \mathrm { I } _ { \parallel } < \mathrm { I } _ { \perp } )$ whereas $\dot { \Phi }$ is positive definite. It follows that the precession is always in the same sense as $\mathrm { L } _ { z }$ in the fixed frame, whereas the precession in the body frame is in the opposite sense to $\mathrm { L } _ { z ^ { \prime } }$ for elongated bodies. We found, in the previous section, that for a flattened body the angular momentum vector lies between the angular velocity vector and the symmetry axis. This means that, in the fixed frame, the angular velocity vector and the symmetry axis lie on opposite sides of the fixed angular momentum vector. On the other hand, for an elongated body we found that the angular velocity vector lies between the angular momentum vector and the symmetry axis. This means that, in the fixed frame, the angular velocity vector and the symmetry axis lie on the same side of the fixed angular momentum vector. (Recall that the angular momentum vector, the angular velocity vector, and the symmetry axis, are coplanar.)

# 8.8 Free Precession of the Earth

It is known that the Earth’s axis of rotation is very slightly inclined to its symmetry axis (which passes through the two geographic poles). The angle $\propto$ is approximately 0.2 seconds of an arc (which corresponds to a distance of about $6 \mathrm { m }$ on the Earth’s surface). It is also known that the ratio of the terrestrial moments of inertia is about $\mathrm { I } _ { \parallel } / \mathrm { I } _ { \perp } = 1 . 0 0 3 2 7 _ { \perp }$ , as determined from the Earth’s oblateness—see Section 8.9. Hence, from (8.39), the precession rate of the angular velocity vector about the symmetry axis, as viewed in a geostationary reference frame, is

$$
\Omega = 0 . 0 0 3 2 7 \omega ,
$$

giving a precession period of

$$
\mathsf { T } ^ { \prime } = \frac { 2 \pi } { \Omega } = 3 0 5 \ \mathrm { d a y s } .
$$

(Of course, $2 \pi / \omega = 1$ day.) The observed period of precession is about 440 days. The disagreement between theory and observation is attributed to the fact that the Earth is not perfectly rigid. The Earth’s symmetry axis subtends an angle $\theta \simeq \alpha = 0 . 2 ^ { \prime \prime }$ [see (8.43)] with its angular momentum vector, but lies on the opposite side of this vector to the angular velocity vector. This implies that, as viewed from space, the Earth’s angular velocity vector is almost parallel to its fixed angular momentum vector, whereas its symmetry axis subtends an angle of $0 . 2 "$ with both vectors, and precesses about them. The (theoretical) precession rate of the Earth’s symmetry axis, as seen from space, is given by Equation (8.57):

$$
\dot { \Phi } = 1 . 0 0 3 2 7 \omega .
$$

The associated precession period is

$$
\mathsf { T } = \frac { 2 \pi } { \dot { \Phi } } = 0 . 9 9 7 \mathrm { d a y s } .
$$

The free precession of the Earth’s symmetry axis in space, which is known as the Chandler wobble, since it was discovered by the American astronomer Seth Chandler in 1891, is superimposed on a much slower forced precession, with a period of about 26,000 years, caused by the small gravitational torque exerted on the Earth by the Sun and the Moon, as a consequence of the Earth’s slight oblateness—see Section 8.10.

# 8.9 McCullough’s Formula

According to Equations (3.57) and (3.62), if the Earth is modeled as spheroid of uniform density $\gamma$ then its ellipticity is given by

$$
\epsilon = - \int \mathrm { r } ^ { 2 } \gamma \mathrm { P } _ { 2 } ( \cos { \theta } ) \mathrm { d } ^ { 3 } \mathbf { r } \bigg / \mathrm { I } _ { 0 } = - \mathrm { \frac { 1 } { 2 } } \int \mathrm { r } ^ { 2 } \gamma \left( 3 \cos ^ { 2 } { \theta } - 1 \right) \mathrm { d } ^ { 3 } \mathbf { r } \bigg / \mathrm { I } _ { 0 } ,
$$

where the integral is over the whole volume of the Earth, and $\mathrm { I } _ { 0 } = ( 2 / 5 ) \mathrm { M } \mathrm { a } ^ { 2 }$ would be the Earth’s moment of inertia were it exactly spherical. Now, the Earth’s moment of inertia about its axis of rotation is given by

$$
\mathrm { I } _ { \parallel } = \int ( x ^ { 2 } + y ^ { 2 } ) \gamma \mathrm { d } ^ { 3 } \mathbf { r } = \int \mathbf { r } ^ { 2 } \gamma \left( 1 - \cos ^ { 2 } \theta \right) \mathrm { d } ^ { 3 } \mathbf { r } .
$$

Here, use has been made of Equations (3.24)–(3.26). Likewise, the Earth’s moment of inertia about an axis perpendicular to its axis of rotation (and passing through the Earth’s center) is

$$
{ \begin{array} { r l } { { \mathrm { I } } _ { \perp } } & { = { \phantom { - } } \displaystyle \int ( \mathbf { y } ^ { 2 } + z ^ { 2 } ) \gamma \mathbf { d } ^ { 3 } \mathbf { r } = \int \mathbf { r } ^ { 2 } \gamma \left( \sin ^ { 2 } \theta \sin ^ { 2 } \phi + \cos ^ { 2 } \theta \right) \mathbf { d } ^ { 3 } \mathbf { r } } \\ & { = { \phantom { - } } \displaystyle \int \mathbf { r } ^ { 2 } \gamma \left( { \frac { 1 } { 2 } } \sin ^ { 2 } \theta + \cos ^ { 2 } \theta \right) \mathbf { d } ^ { 3 } \mathbf { r } = { \frac { 1 } { 2 } } \int \mathbf { r } ^ { 2 } \gamma \left( 1 + \cos ^ { 2 } \theta \right) \mathbf { d } ^ { 3 } \mathbf { r } , } \end{array} }
$$

since the average of $\sin ^ { 2 } \Phi$ is $1 / 2$ for an axisymmetric mass distribution. It follows from the above three equations that

$$
\epsilon = \frac { \mathrm { I } _ { \parallel } - \mathrm { I } _ { \perp } } { \mathrm { I } _ { 0 } } \simeq \frac { \mathrm { I } _ { \parallel } - \mathrm { I } _ { \perp } } { \mathrm { I } _ { \parallel } } .
$$

This result, which is known as McCullough’s formula, demonstrates that the Earth’s ellipticity is directly related to the difference between its principle moments of inertia. It turns out that McCullough’s formula holds for any axially symmetric mass distribution, and not just a spheroidal distribution with uniform density. Finally, McCullough’s formula can be combined with Equation (3.63) to give

$$
\Phi ( { \mathsf { r } } , \theta ) = - { \frac { \mathsf { G } M } { { \mathsf { r } } } } + { \frac { \mathsf { G } ( { \mathsf { I } } _ { \parallel } - { \mathsf { I } } _ { \perp } ) } { { \mathsf { r } } ^ { 3 } } } { \mathsf { P } } _ { 2 } ( \cos \theta ) .
$$

This is the general expression for the gravitational potential generated outside an axially symmetric mass distribution. The first term on the right-hand side is the monopole gravitational field which would be generated if all of the mass in the distribution were concentrated at its center of mass, whereas the second term is the quadrupole field generated by any deviation from spherical symmetry in the distribution.

![](images/0aad5e1f46652077019f55870a8b9535c9a084ce5870dabc0b2e6fc512ca27f5.jpg)  
Figure 8.2: The Earth-Sun system.

# 8.10 Forced Precession and Nutation of the Earth

Consider the Earth-Sun system—see Figure 8.2. From a geocentric viewpoint, the Sun orbits the Earth counter-clockwise (looking from the north), once per year, in an approximately circular orbit of radius $\mathrm { a } _ { s } = 1 . 5 0 \times 1 0 ^ { 1 1 } \mathrm { m }$ . In astronomy, the plane of the Sun’s apparent orbit relative to the Earth is known as the ecliptic plane. Let us define non-rotating Cartesian coordinates, centered on the Earth, which are such that the $x -$ and $_ { 9 }$ -axes lie in the ecliptic plane, and the $z$ -axis is normal to this plane (in the sense that the Earth’s north pole lies at positive $z { \dot { } }$ ). It follows that the $z$ -axis is directed toward a point in the sky (located in the constellation Draco) known as the north ecliptic pole. In the following, we shall treat the $\mathrm { O } { \tt x } { \tt y } z$ system as inertial. This is a reasonable approximation because the orbital acceleration of the Earth is much smaller than the acceleration due to its diurnal rotation. It is convenient to parameterize the instantaneous position of the Sun in terms of a counter-clockwise (looking from the north) azimuthal angle $\lambda _ { s }$ that is zero on the positive $x$ -axis—see Figure 8.2.

Let ω be the Earth’s angular velocity vector due to its daily rotation. This vector makes an angle θ with the $z$ -axis, where $\theta = 2 3 . 4 4 ^ { \circ }$ is the mean inclination of the ecliptic to the Earth’s equatorial plane. Suppose that the projection of ω onto the ecliptic plane subtends an angle $\Phi$ with the $_ { 9 }$ -axis, where $\Phi$ is measured in a counter-clockwise (looking from the north) sense—see Figure 8.2. The orientation of the Earth’s axis of rotation (which is, of course, parallel to $\omega$ ) is thus determined by the two angles θ and $\Phi$ . Note, however, that these two angles are also Euler angles, in the sense given in Section 8.7. Let us examine the Earth-Sun system at an instant in time, $\mathrm { \Delta t } = 0$ , when $\Phi = 0$ : i.e., when ω lies in the $y - z$ plane. At this particular instant, the $x$ -axis points towards the so-called vernal equinox, which is defined as the point in the sky where the ecliptic plane crosses the projection of the Earth’s equator (i.e., the plane normal to $\omega$ ) from south to north. A counter-clockwise (looking from the north) angle in the ecliptic plane that is zero at the vernal equinox is generally known as an ecliptic longitude. Thus, $\lambda _ { s }$ is the Sun’s ecliptic longitude.

According to Equation (8.68), the potential energy of the Earth-Sun system is written

$$
\mathsf { U } = M _ { s } \Phi = - \frac { \mathsf { G } M _ { s } M } { \mathsf { a } _ { s } } + \frac { \mathsf { G } M _ { s } ( \mathrm { I } _ { \parallel } - \mathrm { I } _ { \perp } ) } { \mathsf { a } _ { s } ^ { 3 } } \mathsf { P } _ { 2 } [ \cos ( \gamma _ { s } ) ] ,
$$

where $M _ { s }$ is the mass of the Sun, $M$ the mass of the Earth, $\mathrm { I } _ { \parallel }$ the Earth’s moment of inertia about its axis of rotation, $\mathrm { I _ { \perp } }$ the Earth’s moment of inertia about an axis lying in its equatorial plane, and $\mathsf { P } _ { 2 } ( \mathsf { x } ) = \left( 1 / 2 \right) \left( 3 \mathsf { x } ^ { 2 } - 1 \right)$ . Furthermore, $\gamma _ { s }$ is the angle subtended between ω and $\mathbf { r } _ { s }$ , where $\mathbf { r } _ { s }$ is the position vector of the Sun relative to the Earth.

It is easily demonstrated that (with $\boldsymbol \Phi = 0 ^ { \cdot }$ )

$$
\begin{array} { r } { \mathbf { \Delta } \mathbf { \omega } = \Delta \big ( 0 , \sin \theta , \cos \theta \big ) , } \end{array}
$$

and

$$
{ \bf r } _ { s } = { \bf a } _ { s } ( \cos \lambda _ { s } , \sin \lambda _ { s } , 0 ) .
$$

Hence,

$$
\cos \gamma _ { s } = { \frac { \mathbf { \boldsymbol { w } } \cdot \mathbf { \boldsymbol { r } } _ { s } } { | \mathbf { \boldsymbol { w } } | | \mathbf { \boldsymbol { r } } _ { s } | } } = \sin \theta \ \sin \lambda _ { s } ,
$$

giving

$$
\mathsf { U } = - \frac { \mathsf { G } M _ { s } M } { \mathsf { a } _ { s } } + \frac { \mathsf { G } M _ { s } ( \mathrm { I } _ { \parallel } - \mathrm { I } _ { \perp } ) } { 2 \mathsf { a } _ { s } ^ { 3 } } ( 3 \sin ^ { 2 } \theta \sin ^ { 2 } \lambda _ { s } - 1 ) .
$$

Now, we are primarily interested in the motion of the Earth’s axis of rotation over timescales that are much longer than a year, so we can average the above expression over the Sun’s orbit to give

$$
\mathsf { U } = - \frac { \mathsf { G } M _ { s } M } { \mathsf { a } _ { s } } + \frac { \mathsf { G } M _ { s } \left( \mathrm { I _ { \parallel } } - \mathrm { I _ { \perp } } \right) } { 2 \mathsf { a } _ { s } ^ { 3 } } \left( \frac { 3 } { 2 } \sin ^ { 2 } \theta - 1 \right)
$$

(since the average of $\sin ^ { 2 } \lambda _ { s }$ over a year is $1 / 2 )$ . Thus, we obtain

$$
\mathsf { U } = \mathsf { U } _ { 0 } - \epsilon \alpha _ { s } \cos ( 2 \theta ) ,
$$

where $\mathsf { U } _ { 0 }$ is a constant, and

$$
\alpha _ { s } = \frac { 3 } { 8 } \operatorname { I } _ { \parallel } \mathsf { n } _ { s } ^ { 2 } .
$$

Here,

$$
\epsilon = \frac { \mathrm { I _ { \parallel } - I _ { \perp } } } { \mathrm { I _ { \parallel } } } = 0 . 0 0 3 3 5
$$

is the Earth’s ellipticity, and

$$
{ \boldsymbol { \mathrm { n } _ { s } } } = { \frac { \mathrm { { d } } { \lambda _ { s } } } { \mathrm { { d t } } } } = \left( { \frac { \mathrm { { G } } { M _ { s } } } { \mathrm { { a } } _ { s } ^ { 3 } } } \right) ^ { 1 / 2 }
$$

the Sun’s apparent orbital angular velocity.

The rotational kinetic energy of the Earth can be written (see Section 8.4)

$$
\mathsf { K } = \frac { 1 } { 2 } \left( \mathrm { I } _ { \perp } \boldsymbol { \omega } _ { x ^ { \prime } } ^ { 2 } + \mathrm { I } _ { \perp } \boldsymbol { \omega } _ { y ^ { \prime } } ^ { 2 } + \mathrm { I } _ { \| } \boldsymbol { \omega } _ { z ^ { \prime } } ^ { 2 } \right) ,
$$

which reduces to

$$
\mathsf { K } = \frac { 1 } { 2 } \left( \mathrm { I } _ { \perp } \dot { \theta } ^ { 2 } + \mathrm { I } _ { \perp } \sin ^ { 2 } \theta \dot { \phi } ^ { 2 } + \mathrm { I } _ { \| } \omega ^ { 2 } \right)
$$

with the aid of Equations (8.53)–(8.55). Here,

$$
\omega = \cos \theta \dot { \phi } + \dot { \Psi } ,
$$

and $\psi$ is the third Euler angle. Hence, the Earth’s Lagrangian takes the form

$$
\mathcal { L } = \mathsf { K } - \mathsf { U } = \frac { 1 } { 2 } \left( \mathrm { I } _ { \perp } \dot { \Theta } ^ { 2 } + \mathrm { I } _ { \perp } \sin ^ { 2 } \theta \dot { \Phi } ^ { 2 } + \mathrm { I } _ { \| } \omega ^ { 2 } \right) + \epsilon \alpha _ { s } \cos ( 2 \Theta )
$$

where any constant terms have been neglected. Note that the Lagrangian does not depend explicitly on the angular coordinate $\psi$ . It follows that the conjugate momentum is a constant of the motion (see Section 7.5). In other words,

$$
{ \mathsf { p } } _ { \Psi } = { \frac { \partial { \mathcal { L } } } { \partial { \dot { \Psi } } } } = { \mathrm { I } } _ { \| } \omega
$$

is a constant of the motion, implying that $\omega$ is also a constant of the motion. Note that $\omega$ is effectively the Earth’s angular velocity of rotation about its axis (since $| \omega _ { \mathrm { x ^ { \prime } } } | , | \omega _ { \mathrm { y ^ { \prime } } } | \ll$ $\omega _ { z ^ { \prime } } = \omega$ , which follows because $| \dot { \Phi } | , | \dot { \theta } | \ll \dot { \Psi } .$ ). Another equation of motion that can be derived from the Lagrangian is

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \left( { \frac { \partial { \mathcal { L } } } { \partial { \dot { \theta } } } } \right) - { \frac { \partial { \mathcal { L } } } { \partial \theta } } = 0 ,
$$

which reduces to

$$
\operatorname { I } _ { \perp } { \ddot { \theta } } - { \frac { \partial { \mathcal { L } } } { \partial \theta } } = 0 .
$$

Consider steady precession of the Earth’s rotational axis, which is characterized by $\dot { \Theta } = 0$ , with both $\dot { \Phi }$ and $\dot { \Psi }$ constant. It follows, from the above equation, that such motion must satisfy the constraint

$$
\frac { \partial \mathcal { L } } { \partial \theta } = 0 .
$$

Thus, we obtain

$$
\frac { 1 } { 2 } \operatorname { I } _ { \perp } \sin ( 2 \theta ) \dot { \Phi } ^ { 2 } - \operatorname { I } _ { \| } \sin \theta \omega \dot { \Phi } - 2 \epsilon \alpha _ { s } \sin ( 2 \theta ) = 0 ,
$$

where use has been made of Equations (8.81) and (8.82). Now, as can easily be verified after the fact, $| \dot { \Phi } | \ll \omega$ , so the above equation reduces to

$$
\dot { \Phi } \simeq - \frac { 4 \epsilon \alpha _ { s } \cos \theta } { \mathrm { I } _ { \parallel } \omega } = \Omega _ { \Phi } ,
$$

which can be integrated to give

$$
\Phi \simeq - \Omega _ { \Phi } \mathrm { t } ,
$$

where

$$
\Omega _ { \Phi } = \frac { 3 } { 2 } \frac { \epsilon { \mathsf n } _ { s } ^ { 2 } } { \omega } \cos \theta ,
$$

and use has been made of Equation (8.76). According to the above expression, the mutual interaction between the Sun and the quadrupole gravitational field generated by the Earth’s slight oblateness causes the Earth’s axis of rotation to precess steadily about the normal to the ecliptic plane at the rate $- \Omega _ { \phi }$ . The fact that $- \Omega _ { \phi }$ is negative implies that the precession is in the opposite direction to the direction of the Earth’s rotation and the Sun’s apparent orbit about the Earth. Incidentally, the interaction causes a precession of the Earth’s rotational axis, rather than the plane of the Sun’s orbit, because the Earth’s axial moment of inertia is much less than the Sun’s orbital moment of inertia. The precession period in years is given by

$$
{ \sf T } _ { \phi } ( { \bf y } { \bf r } ) = \frac { { \sf n } _ { s } } { \Omega _ { \phi } } = \frac { 2 { \sf T } _ { s } ( { \sf d a y } ) } { 3 \epsilon \mathrm { ~ c o s ~ } \theta } ,
$$

where $\mathsf { T } _ { s } ( \mathrm { d } \mathsf { a } \mathsf { y } ) = \mathsf { a } \mu / \mathsf { n } _ { s } = 3 6 5 . 2 4$ is the Sun’s orbital period in days. Thus, given that $\epsilon = 0 . 0 0 3 3 5$ and $\theta = 2 3 . 4 4 ^ { \circ }$ , we obtain

$$
\mathsf { T } _ { \Phi } \simeq 7 9 , 2 0 0 \ : \mathrm { y e a r s } .
$$

Unfortunately, the observed precession period of the Earth’s axis of rotation about the normal to the ecliptic plane is approximately 25,800 years, so something is clearly missing from our model. It turns out that the missing factor is the influence of the Moon.

Using analogous arguments to those given above, the potential energy of the Earth-Moon system can be written

$$
\mathsf { U } = - \frac { \mathsf { G } M _ { \mathrm { m } } M } { \mathsf { a } _ { \mathrm { m } } } + \frac { \mathsf { G } M _ { \mathrm { m } } \left( \mathrm { I _ { \parallel } } - \mathrm { I _ { \perp } } \right) } { \mathsf { a } _ { \mathrm { m } } ^ { 3 } } \mathsf { P } _ { 2 } [ \cos ( \gamma _ { \mathrm { m } } ) ] ,
$$

where $M _ { \mathfrak { m } }$ is the lunar mass, and ${ \mathfrak { a } } _ { \mathfrak { m } }$ the radius of the Moon’s (approximately circular) orbit. Furthermore, $\gamma _ { \mathfrak { m } }$ is the angle subtended between $\omega$ and ${ \bf r } _ { \mathrm { m } }$ , where

$$
\mathbf { \omega } \omega = \omega \ ( - \sin \theta \ \sin \phi , \sin \theta \ \cos \phi , \cos \theta )
$$

is the Earth’s angular velocity vector, and ${ \bf r } _ { \mathrm { m } }$ is the position vector of the Moon relative to the Earth. Here, for the moment, we have retained the $\Phi$ dependence in our expression for $\omega$ (since we shall presently differentiate by $\Phi$ , before setting $\Phi = 0 .$ ). Now, the Moon’s orbital plane is actually slightly inclined to the ecliptic plane, the angle of inclination being $\mathfrak { l } _ { \mathfrak { m } } = 5 . 1 6 ^ { \circ }$ . Hence, we can write

$$
{ \bf r } _ { \mathrm { m } } \simeq { \bf a } _ { \mathrm { m } } \ : ( \cos \lambda _ { \mathrm { m } } , \sin \lambda _ { \mathrm { m } } , \ : { \sf t } _ { \mathrm { m } } \ : \sin ( \lambda _ { \mathrm { m } } - \varpi _ { \mathrm { n } } ) ) ,
$$

to first order in $\mathfrak { L } _ { \mathfrak { m } }$ , where $\lambda _ { \mathfrak { m } }$ is the Moon’s ecliptic longitude, and $\varpi _ { \mathfrak { n } }$ is the ecliptic longitude of the lunar ascending node, which is defined as the point on the lunar orbit where

the Moon crosses the ecliptic plane from south to north. Of course, $\lambda _ { \mathfrak { m } }$ increases at the rate ${ \mathfrak { n } } _ { \mathfrak { m } }$ , where

$$
{ \mathfrak { n } } _ { \mathfrak { m } } = { \frac { \mathrm { d } \lambda _ { \mathfrak { m } } } { \mathrm { d t } } } \simeq \left( { \frac { \mathrm { G } M } { { \mathfrak { a } } _ { \mathfrak { m } } ^ { 3 } } } \right) ^ { 1 / 2 }
$$

is the Moon’s orbital angular velocity. It turns out that the lunar ascending node precesses steadily, in the opposite direction to the Moon’s orbital rotation, in such a manner that it completes a full circuit every 18.6 years. This precession is caused by the perturbing influence of the Sun—see Chapter 10. It follows that

$$
\frac { \mathrm { d } \varpi _ { \mathfrak { n } } } { \mathrm { d t } } = - \Omega _ { \mathfrak { n } } ,
$$

where $2 \pi / \Omega _ { \mathrm { n } } = 1 8 . 6$ years. Now, from (8.94) and (8.95),

$$
\cos \gamma _ { \mathrm { m } } = { \frac { \omega \cdot \mathbf { r } _ { \mathrm { m } } } { | \omega | \left| \mathbf { r } _ { \mathrm { m } } \right| } } = \sin \theta \ \sin ( \lambda _ { \mathrm { m } } - \Phi ) + \mathfrak { \iota } _ { \mathrm { m } } \cos \Theta \ \sin ( \lambda _ { \mathrm { m } } - \varpi _ { \mathrm { n } } ) ,
$$

so (8.93) yields

$$
\begin{array} { r c l } { \mathrm { ~ U ~ } \simeq } & { - \frac { \mathsf { G } M _ { \mathrm { m } } M } { \alpha _ { \mathrm { m } } } + \frac { \mathsf { G } M _ { \mathrm { m } } \left( \mathrm { I _ { \parallel } } - \mathrm { I _ { \perp } } \right) } { 2 \alpha _ { \mathrm { m } } ^ { 3 } } \left[ 3 \sin ^ { 2 } \theta \sin ^ { 2 } ( \lambda _ { \mathrm { m } } - \Phi ) \right. } \\ & { \left. + 3 \iota _ { \mathrm { m } } \sin ( 2 \theta ) \sin ( \lambda _ { \mathrm { m } } - \Phi ) \sin ( \lambda _ { \mathrm { m } } - \varpi _ { \mathrm { n } } ) - 1 \right] } \end{array}
$$

to first order in $\mathfrak { L } _ { \mathfrak { m } }$ . Given that we are interested in the motion of the Earth’s axis of rotation on time-scales that are much longer than a month, we can average the above expression over the Moon’s orbit to give

$$
\begin{array} { r } { \mathsf { U } \simeq \mathsf { U } _ { 0 } ^ { \prime } - \epsilon \alpha _ { \mathsf { m } } \cos ( 2 \theta ) + \epsilon \beta _ { \mathsf { m } } \sin ( 2 \theta ) \cos ( \varpi _ { \mathsf { n } } - \Phi ) , } \end{array}
$$

[since the average of $\sin ^ { 2 } ( \lambda _ { \mathrm { m } } - \phi )$ over a month is $1 / 2$ , whereas that of $\sin ( \lambda _ { \mathrm { m } } - \Phi ) \sin ( \lambda _ { \mathrm { m } } -$ $\varpi _ { \mathrm { m } } )$ is $( 1 / 2 ) \cos ( \varpi _ { \mathrm { m } } - \Phi ) ]$ . Here, ${ \sf U } _ { 0 } ^ { \prime }$ is a constant,

$$
\begin{array} { r c l } { { \displaystyle \alpha _ { \mathrm { m } } } } & { { = } } & { { \displaystyle \frac { 3 } { 8 } \mathrm { I } _ { \parallel } \mu _ { \mathrm { m } } { \bf n } _ { \mathrm { m } } ^ { 2 } , } } \\ { { \displaystyle \beta _ { \mathrm { m } } } } & { { = } } & { { \displaystyle \frac { 3 } { 4 } \mathrm { I } _ { \parallel } \iota _ { \mathrm { m } } \mu _ { \mathrm { m } } { \bf n } _ { \mathrm { m } } ^ { 2 } , } } \end{array}
$$

and

$$
\mu _ { \mathrm { m } } = \frac { M _ { \mathrm { m } } } { M } = 0 . 0 1 2 3
$$

is the ratio of the lunar to the terrestrial mass. Now, gravity is a superposable force, so the total potential energy of the Earth-Moon-Sun system is the sum of Equations (8.75) and (8.100). In other words,

$$
\mathtt { U } = \mathtt { U } _ { 0 } ^ { \prime \prime } - \epsilon \propto \cos ( 2 \theta ) + \epsilon \beta _ { \mathfrak { m } } \sin ( 2 \theta ) \cos ( \varpi _ { \mathfrak { n } } - \Phi ) ,
$$

where $\mathrm { U } _ { 0 } ^ { \prime \prime }$ is a constant, and

$$
\alpha = \alpha _ { s } + \alpha _ { \mathrm { m } } .
$$

Finally, making use of (8.80), the Lagrangian of the Earth is written

$$
 { \bf \Gamma } : = \frac 1 2 \left( \mathrm { I } _ { \perp } \dot { \theta } ^ { 2 } + \mathrm { I } _ { \perp } \sin ^ { 2 } \theta \dot { \phi } ^ { 2 } + \mathrm { I } _ { \| } \omega ^ { 2 } \right) + \epsilon \propto \cos ( 2 \theta ) - \epsilon \beta _ { \mathrm { m } } \sin ( 2 \theta ) \cos ( \varpi _ { \mathrm { n } } - \phi ) ,
$$

where any constant terms have been neglected. Recall that $\omega$ is given by (8.81), and is a constant of the motion.

Two equations of motion that can immediately be derived from the above Lagrangian are

$$
\begin{array} { r c l } { { \displaystyle { \frac { \mathrm { d } } { \mathrm { d t } } } \left( \frac { \partial \mathcal { L } } { \partial \dot { \Theta } } \right) - \frac { \partial \mathcal { L } } { \partial \Theta } ~ = ~ 0 , } }  \\ { { \displaystyle { \frac { \mathrm { d } } { \mathrm { d t } } } \left( \frac { \partial \mathcal { L } } { \partial \dot { \Phi } } \right) - \frac { \partial \mathcal { L } } { \partial \Phi } ~ = ~ 0 . } } \end{array}
$$

(The third equation, involving $\psi$ , merely confirms that $\omega$ is a constant of the motion.) The above two equations yield

$$
\begin{array} { r c l } { { 0 } } & { { = } } & { { \displaystyle { \mathrm { I } _ { \perp } } { \ddot { \Theta } } - \frac { 1 } { 2 } { \mathrm { I } _ { \perp } } \sin ( 2 \Theta ) { \dot { \Theta } } ^ { 2 } + \mathrm { I _ { \parallel } } \sin \theta \omega { \dot { \Theta } } + 2 \epsilon \propto \sin ( 2 \Theta ) } } \\ { { } } & { { } } & { { \displaystyle + 2 \epsilon \otimes _ { \mathrm { m } } \cos ( 2 \Theta ) \cos ( \varpi _ { \mathrm { n } } - \Phi ) , } } \\ { { 0 } } & { { = } } & { { \displaystyle { \cfrac { \mathrm { d } } { { \mathrm { d t } } } \big ( \mathrm { I } _ { \perp } \sin ^ { 2 } \Theta { \dot { \phi } } + \mathrm { I _ { \parallel } } \cos \theta \omega \big ) + \epsilon \beta _ { \mathrm { m } } \sin ( 2 \Theta ) \sin ( \varpi _ { \mathrm { n } } - \Phi ) , } } } \end{array}
$$

respectively. Let

$$
\begin{array} { r c l } { { \theta ( { \bf t } ) } } & { { = } } & { { \theta _ { 0 } + \epsilon \theta _ { 1 } ( { \bf t } ) , } } \\ { { \phi ( { \bf t } ) } } & { { = } } & { { \epsilon \ \Phi _ { 1 } ( { \bf t } ) , } } \end{array}
$$

where $\theta _ { 0 } = 2 3 . 4 4 ^ { \circ }$ is the mean inclination of the ecliptic to the Earth’s equatorial plane. To first order in $\epsilon$ , Equations (8.109) and (8.110) reduce to

$$
\begin{array} { r c l } { 0 } & { \simeq } & { \mathrm { I _ { \perp } } \ddot { \Theta } _ { 1 } + \mathrm { I _ { \parallel } } \sin \Theta _ { 0 } \omega \dot { \phi } _ { 1 } + 2 \alpha \sin ( 2 \Theta _ { 0 } ) + 2 \beta _ { \mathrm { m } } \cos ( 2 \Theta _ { 0 } ) \cos ( \Omega _ { \mathrm { n } } \mathrm { t } ) , } \\ { 0 } & { \simeq } & { \mathrm { I _ { \perp } } \sin ^ { 2 } \Theta _ { 0 } \ddot { \phi } _ { 1 } - \mathrm { I _ { \parallel } } \sin \Theta _ { 0 } \omega \dot { \Theta } _ { 1 } - \beta _ { \mathrm { m } } \sin ( 2 \Theta _ { 0 } ) \sin ( \Omega _ { \mathrm { n } } \mathrm { t } ) , } \end{array}
$$

respectively, where use has been made of Equation (8.97). However, as can easily be verified after the fact, $\mathrm { d } / \mathrm { d t } \ll \omega$ , so we obtain

$$
\begin{array} { r c l } { \dot { \phi } _ { 1 } } & { \simeq } & { \displaystyle - \frac { 4 \alpha \cos \theta _ { 0 } } { \ I _ { \parallel } \ \omega } - \frac { 2 \beta _ { \mathrm { m } } \cos ( 2 \theta _ { 0 } ) } { \ I _ { \parallel } \ \omega \ \sin \theta _ { 0 } } \cos ( \Omega _ { \mathrm { n } } \operatorname { t } ) , } \\ { \dot { \theta } _ { 1 } } & { \simeq } & { \displaystyle - \frac { 2 \beta _ { \mathrm { m } } \cos \theta _ { 0 } } { \ I _ { \parallel } \ \omega } \sin ( \Omega _ { \mathrm { n } } \operatorname { t } ) . } \end{array}
$$

The above equations can be integrated, and then combined with Equations (8.111) and (8.112), to give

$$
\begin{array} { r c l } { { \Phi ( \mathbf { t } ) } } & { { = } } & { { - \Omega _ { \Phi } \mathbf { t } - \delta \Phi \sin ( \Omega _ { \mathrm { n } } \mathbf { t } ) , } } \\ { { \theta ( \mathbf { t } ) } } & { { = } } & { { \theta _ { 0 } + \delta \Theta \cos ( \Omega _ { \mathrm { n } } \mathbf { t } ) , } } \end{array}
$$

where

$$
\begin{array} { r c l } { { \Omega _ { \Phi } } } & { { = } } & { { \displaystyle \frac { 3 } { 2 } \frac { \epsilon ( { \bf n } _ { s } ^ { 2 } + \mu _ { \mathrm { m } } \Omega _ { \mathrm { m } } ^ { 2 } ) } { \omega } \cos \theta _ { 0 } , } } \\ { { } } & { { } } & { { } } \\ { { \delta \Phi } } & { { = } } & { { \displaystyle \frac { 3 } { 2 } \frac { \epsilon \iota _ { \mathrm { m } } \mu _ { \mathrm { m } } { \bf n } _ { \mathrm { m } } ^ { 2 } } { \omega \Omega _ { \mathrm { n } } } \frac { \cos ( 2 \theta _ { 0 } ) } { \sin \theta _ { 0 } } , } } \\ { { } } & { { } } & { { } } \\ { { \delta \Theta } } & { { = } } & { { \displaystyle \frac { 3 } { 2 } \frac { \epsilon \iota _ { \mathrm { m } } \mu _ { \mathrm { m } } { \bf n } _ { \mathrm { m } } ^ { 2 } } { \omega \Omega _ { \mathrm { n } } } \cos \theta _ { 0 } . } } \end{array}
$$

Incidentally, in the above, we have assumed that the lunar ascending node coincides with the vernal equinox at time $\mathrm { t } = 0$ (i.e., $\varpi _ { \mathfrak { m } } = 0$ at $\mathrm { t } = 0 \mathrm { . }$ ), in accordance with our previous assumption that $\Phi = 0$ at $\mathrm { t } = 0$ .

According to Equation (8.117), the combined gravitational interaction of the Sun and the Moon with the quadrupole field generated by the Earth’s slight oblateness causes the Earth’s axis of rotation to precess steadily about the normal to the ecliptic plane at the rate $- \Omega _ { \phi }$ . As before, the negative sign indicates that the precession is in the opposite direction to the (apparent) orbital motion of the sun and moon. The period of the precession in years is given by

$$
\mathsf { T } _ { \Phi } ( \mathbf { y } \mathbf { r } ) = \frac { \mathsf { n } _ { s } } { \Omega _ { \Phi } } = \frac { 2 \mathsf { T } _ { s } ( \mathrm { d } \mathbf { a } \mathbf { y } ) } { \epsilon ( 1 + \mu _ { \mathrm { m } } / [ \mathsf { T } _ { \mathrm { m } } ( \mathbf { y } \mathbf { r } ) ] ^ { 2 } ) \cos \theta _ { 0 } } ,
$$

where ${ \sf T } _ { \mathrm { m } } ( { \bf y } { \bf r } ) = { \sf n } _ { s } / { \sf n } _ { \sf m } = 0 . 0 8 1$ is the Moon’s (synodic) orbital period in years. Given that $\epsilon = 0 . 0 0 3 3 5$ , $\theta _ { 0 } = 2 3 . 4 4 ^ { \circ }$ , $ { \mathsf { T } } _ { s } (  { \mathrm { d a y } } ) = 3 6 5 . 2 4$ , and $\mu _ { \mathrm { m } } = 0 . 0 1 2 3$ , we obtain

$$
\mathsf { T } _ { \Phi } \simeq 2 7 , 6 0 0 \mathsf { y e a r s } .
$$

This prediction is fairly close to the observed precession period of 25, 800 years. The main reason that our estimate is slightly inaccurate is because we have neglected to take into account the small eccentricities of the Earth’s orbit around the Sun, and the Moon’s orbit around the Earth.

The point in the sky toward which the Earth’s axis of rotation points is known as the north celestial pole. Currently, this point lies within about a degree of the fairly bright star Polaris, which is consequently sometimes known as the north star or the pole star. It follows that Polaris appears to be almost stationary in the sky, always lying due north, and can thus be used for navigational purposes. Indeed, mariners have relied on the north star for many hundreds of years to determine direction at sea. Unfortunately, because of the precession of the Earth’s axis of rotation, the north celestial pole is not a fixed point in the sky, but instead traces out a circle, of angular radius $2 3 . 4 4 ^ { \circ }$ , about the north ecliptic pole, with a period of 25,800 years. Hence, a few thousand years from now, the north celestial pole will no longer coincide with Polaris, and there will be no convenient way of telling direction from the stars.

The projection of the ecliptic plane onto the sky is called the ecliptic, and coincides with the apparent path of the Sun against the backdrop of the stars. Furthermore, the projection of the Earth’s equator onto the sky is known as the celestial equator. As has been previously mentioned, the ecliptic is inclined at $2 3 . 4 4 ^ { \circ }$ to the celestial equator. The two points in the sky at which the ecliptic crosses the celestial equator are called the equinoxes, since night and day are equally long when the Sun lies at these points. Thus, the Sun reaches the vernal equinox on about March 21st, and this traditionally marks the beginning of spring. Likewise, the Sun reaches the autumn equinox on about September 22nd, and this traditionally marks the beginning of autumn. However, the precession of the Earth’s axis of rotation causes the celestial equator (which is always normal to this axis) to precess in the sky, and thus also causes the equinoxes to precess along the ecliptic. This effect is known as the precession of the equinoxes. The precession is in the opposite direction to the Sun’s apparent motion around the ecliptic, and is of magnitude $1 . 4 ^ { \circ }$ per century. Amazingly, this miniscule effect was discovered by the Ancient Greeks (with the help of ancient Babylonian observations). In about 2000 BC, when the science of astronomy originated in ancient Egypt and Babylonia, the vernal equinox lay in the constellation Aries. Indeed, the vernal equinox is still sometimes called the first point of Aries in astronomical texts. About 90 BC, the vernal equinox moved into the constellation Pisces, where it still remains. The equinox will move into the constellation Aquarius (marking the beginning of the much heralded “Age of Aquarius”) in about 2600 AD. Incidentally, the position of the vernal equinox in the sky is of great significance in astronomy, since it is used as the zero of celestial longitude (much as Greenwich is used as the zero of terrestrial longitude).

Equations (8.117) and (8.118) indicate that the small inclination of the lunar orbit to the ecliptic plane, combined with the precession of the lunar ascending node, causes the Earth’s axis of rotation to wobble sightly. This wobble is known as nutation (from the Latin nutare, to nod), and is superimposed on the aforementioned precession. In the absence of precession, nutation would cause the north celestial pole to periodically trace out a small ellipse on the sky, the sense of rotation being counter-clockwise. The nutation period is 18.6 years: i.e., the same as the precession period of the lunar ascending node. The nutation amplitudes in the polar and azimuthal angles θ and $\Phi$ are

$$
\begin{array} { r c l } { { \delta \Theta } } & { { = } } & { { \displaystyle \frac { 3 \mathrm {  ~ \epsilon ~ } \epsilon \iota _ { \mathrm { m } } \mu _ { \mathrm { m } } { \sf T } _ { \mathrm { n } } ( \mathrm { y r } ) } { 2 } \mathrm { c o s } \theta _ { 0 } , } } \\ { { \delta \Phi } } & { { = } } & { { \displaystyle \frac { 3 } { 2 } \frac { \mathrm {  ~ \epsilon ~ } \iota _ { \mathrm { m } } \mu _ { \mathrm { m } } { \sf T } _ { \mathrm { n } } ( \mathrm { y r } ) } { \sf T } \frac { \mathrm { c o s } ( 2 \theta _ { 0 } ) } { \sin \theta _ { 0 } } , } } \end{array}
$$

respectively, where ${ \sf T } _ { \mathrm { n } } ( { \bf y } { \bf r } ) = { \sf n } _ { s } / { \Omega _ { \mathrm { n } } } = 1 8 . 6$ . Given that $\epsilon = 0 . 0 0 3 3 5$ , $\theta _ { 0 } = 2 3 . 4 4 ^ { \circ }$ , $\mathfrak { l } _ { \mathfrak { m } } =$ $5 . 1 6 ^ { \circ }$ , $ { \mathsf { T } } _ { s } (  { \mathrm { d a y } } ) = 3 6 5 . 2 4$ , $\mathsf { T } _ { \mathrm { m } } ( \mathsf { y } \mathbf { r } ) = 0 . 0 8 1$ , and $\mu _ { \mathrm { m } } = 0 . 0 1 2 3$ , we obtain

$$
\begin{array} { r c l } { { \delta \theta } } & { { = } } & { { 8 . 2 ^ { \prime \prime } , } } \\ { { \delta \Phi } } & { { = } } & { { 1 5 . 3 ^ { \prime \prime } . } } \end{array}
$$

The observed nutation amplitudes are $9 . 2 ^ { \prime \prime }$ and $1 7 . 2 ^ { \prime \prime }$ , respectively. Hence, our estimates are quite close to the mark. Any inaccuracy is mainly due to the fact that we have neglected to take into account the small eccentricities of the Earth’s orbit around the Sun, and the Moon’s orbit around the Earth. The nutation of the Earth was discovered in 1728 by the English astronomer James Bradley, and was explained theoretically about 20 years later by d’Alembert and Euler. Nutation is important because the corresponding gyration of the Earth’s rotation axis appears to be transferred to celestial objects when they are viewed using terrestrial telescopes. This effect causes the celestial longitudes and latitudes of heavenly objects to oscillate sinusoidally by up to $2 0 ^ { \prime \prime }$ (i.e., about the maximum apparent angular size of Saturn) with a period of 18.6 years. It is necessary to correct for this oscillation in order to accurately guide terrestrial telescopes to particular objects.

# 8.11 Exercises

8.1. A rigid body having an axis of symmetry rotates freely about a fixed point under no torques. If $\propto$ is the angle between the symmetry axis and the instantaneous axis of rotation, show that the angle between the axis of rotation and the invariable line (the L vector) is

$$
\tan ^ { - 1 } \left[ \frac { ( \mathrm { I _ { \parallel } - I _ { \perp } } ) \tan \alpha } { \mathrm { I _ { \parallel } + I _ { \perp } \tan ^ { 2 } \alpha } } \right]
$$

where $\mathrm { I } _ { \parallel }$ (the moment of inertia about the symmetry axis) is greater than $\mathrm { I _ { \perp } }$ (the moment of inertia about an axis normal to the symmetry axis).

8.2. Since the greatest value of $\mathrm { I _ { \parallel } / I _ { \perp } }$ is 2 (symmetrical lamina) show from the previous result that the angle between the angular velocity and angular momentum vectors cannot exceed $\tan ^ { - 1 } ( 1 / { \sqrt { 8 } } ) \simeq 1 9 . 5 ^ { \circ }$ . Find the corresponding value of $\propto$ .

8.3. A thin uniform rod of length l and mass m is constrained to rotate with constant angular velocity $\omega$ about an axis passing through the center of the rod, and making an angle $\propto$ with the rod. Show that the angular momentum about the center of the rod is perpendicular to the rod, and is of magnitude $( \mathsf { m } \mathsf { l } ^ { 2 } \omega / 1 2 )$ sin $\propto$ . Show that the torque is perpendicular to both the rod and the angular momentum vector, and is of magnitude $( \mathsf { m } \mathsf { l } ^ { 2 } \omega ^ { 2 } / 1 2 )$ sin $\propto$ cos $\propto$ .

8.4. A thin uniform disk of radius a and mass m is constrained to rotate with constant angular velocity ω about an axis passing through its center, and making an angle $\propto$ with the normal to the disk. Find the angular momentum about the center of the disk, as well as the torque acting on the disk.

8.5. Consider an artificial satellite in a circular orbit of radius $\mathrm { L }$ about the Earth. Suppose that the normal to the plane of the orbit subtends an angle θ with the Earth’s axis of rotation. By approximating the orbiting satellite as a uniform ring, demonstrate that the Earth’s oblateness causes the plane of the satellite’s orbit to precess about the Earth’s rotational axis at the rate

$$
\frac { \dot { \Phi } } { \omega } \simeq - \frac { 1 } { 2 } \epsilon \left( \frac { \mathrm { \tiny ~ R } } { \mathrm { \tiny ~ L } } \right) ^ { 2 } \cos \theta .
$$

Here, ω is the satellite’s orbital angular velocity, $\epsilon = 0 . 0 0 3 3 5$ the Earth’s ellipticity, and $\mathsf { R }$ the Earth’s radius. Note that the Earth’s axial moment of inertial is $\mathrm { I } _ { \| } \simeq ( 1 / 3 ) \mathsf { M } \mathsf { R } ^ { 2 }$ , where $M$ is the mass of the Earth.

8.6. A sun-synchronous satellite is one which always passes over a given point on the Earth at the same local solar time. This is achieved by fixing the precession rate of the satellite’s orbital plane such that it matches the rate at which the Sun appears to move against the background of the stars. What orbital altitude above the surface of the Earth would such a satellite need to have in order to fly over all latitudes between $5 0 ^ { \circ } \mathrm { ~ N ~ }$ and $5 0 ^ { \circ }$ S? Is the direction of the satellite orbit in the same sense as the Earth’s rotation (prograde), or the opposite sense (retrograde)?

# 9 Three-Body Problem

# 9.1 Introduction

We saw earlier, in Section 2.9, that an isolated dynamical system consisting of two freely moving point masses exerting forces on one another—which is usually referred to as a twobody problem—can always be converted into an equivalent one-body problem. In particular, this implies that we can exactly solve a dynamical system containing two gravitationally interacting point masses, since the equivalent one-body problem is exactly soluble—see Sections 2.9 and 4.11. What about a system containing three gravitationally interacting point masses? Despite hundreds of years of research, no exact solution of this famous problem—which is generally known as the three-body problem—has ever been found. It is, however, possible to make some progress by severely restricting the problem’s scope.

# 9.2 Circular Restricted Three-Body Problem

Consider an isolated dynamical system consisting of three gravitationally interacting point masses, $\mathfrak { m } _ { 1 }$ , $\mathfrak { m } _ { 2 }$ , and $\mathfrak { m } _ { 3 }$ . Suppose, however, that the third mass, $\mathfrak { m } _ { 3 }$ , is so much smaller than the other two that it has a negligible effect on their motion. Suppose, further, that the first two masses, $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , execute circular orbits about their common center of mass. In the following, we shall investigate this simplified problem, which is generally known as the circular restricted three-body problem.

Let us define a Cartesian coordinate system $( \xi , \eta , \zeta )$ in an inertial reference frame whose origin coincides with the center of mass, C, of the two orbiting masses. Furthermore, let the orbital plane of these masses coincide with the $\xi \cdot \boldsymbol { \eta }$ plane, and let them both lie on the $\xi$ -axis at time $\mathrm {  ~ t ~ } = 0 \mathrm {  ~ \Omega ~ }$ —see Figure 9.1. Suppose that R is the constant distance between the two orbiting masses, $\boldsymbol { \mathsf { r } } _ { 1 }$ the constant distance between mass $\mathfrak { m } _ { 1 }$ and the origin, and $\boldsymbol { \Upsilon } _ { 2 }$ the constant distance between mass $\mathfrak { m } _ { 2 }$ and the origin. Moreover, let $\omega$ be the constant orbital angular velocity. It follows, from Section 4.11, that

$$
{ \begin{array} { r c l } { \omega ^ { 2 } } & { = } & { { \frac { \mathsf { G } \mathsf { M } } { \mathsf { R } ^ { 3 } } } , } \\ { { \frac { \mathsf { r } _ { 1 } } { \mathsf { r } _ { 2 } } } } & { = } & { { \frac { \mathsf { m } _ { 2 } } { \mathsf { m } _ { 1 } } } , } \end{array} }
$$

where $M = { \mathfrak { m } } _ { 1 } + { \mathfrak { m } } _ { 2 }$

It is convenient to choose our unit of length such that ${ \sf R } = 1$ , and our unit of mass such that $G M = 1$ . It follows, from Equation (9.1), that $\omega = 1$ . However, we shall continue to retain ω in our equations, for the sake of clarity. Let $\mu _ { 1 } = \mathsf { G m } _ { 1 }$ , and $\mu _ { 2 } = \mathsf { G } \mathsf { m } _ { 2 } = 1 - \mu _ { 1 }$ . It is easily demonstrated that $\mathfrak { r } _ { 1 } = \mu _ { 2 }$ , and $\boldsymbol { \mathsf { r } } _ { 2 } = 1 - \boldsymbol { \mathsf { r } } _ { 1 } = \boldsymbol { \mathsf { \mu } } _ { 1 }$ . Hence, the two orbiting masses, $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , have position vectors $\mathbf { r } _ { 1 } = \left( \boldsymbol { \xi } _ { 1 } , \boldsymbol { \eta } _ { 1 } , 0 \right)$ and $\mathbf { r } _ { 2 } = \left( \xi _ { 2 } , \eta _ { 2 } , 0 \right)$ , respectively, where (see Figure 9.1)

![](images/93cf846d3c94dfd006310238544a9cfe30713043e799fa534956125565b0168b.jpg)  
Figure 9.1: The circular restricted three-body problem.

$$
\begin{array} { r c l } { { { \bf r } _ { 1 } } } & { { = } } & { { \mu _ { 2 } \left( - \cos \omega t , - \sin \omega t , 0 \right) , } } \\ { { { \bf r } _ { 2 } } } & { { = } } & { { \mu _ { 1 } \left( \cos \omega t , \sin \omega t , 0 \right) . } } \end{array}
$$

Let the third mass have position vector $\mathbf { r } = ( \xi , \eta , \zeta )$ . The Cartesian components of the equation of motion of this mass are thus

$$
\begin{array} { r c l } { \displaystyle \ddot { \xi } } & { = } & { \displaystyle - \mathsf { \mu } _ { 1 } \frac { \left( \xi - \xi _ { 1 } \right) } { \rho _ { 1 } ^ { 3 } } - \mathsf { \mu } _ { 2 } \frac { \left( \xi - \xi _ { 2 } \right) } { \rho _ { 2 } ^ { 3 } } , } \\ { \displaystyle \ddot { \eta } } & { = } & { \displaystyle - \mathsf { \mu } _ { 1 } \frac { \left( \eta - \eta _ { 1 } \right) } { \rho _ { 1 } ^ { 3 } } - \mathsf { \mu } _ { 2 } \frac { \left( \eta - \eta _ { 2 } \right) } { \rho _ { 2 } ^ { 3 } } , } \\ { \displaystyle \ddot { \zeta } } & { = } & { \displaystyle - \mathsf { \mu } _ { 1 } \frac { \zeta } { \rho _ { 1 } ^ { 3 } } - \mathsf { \mu } _ { 2 } \frac { \zeta } { \rho _ { 2 } ^ { 3 } } , } \end{array}
$$

where

$$
\begin{array} { r l r } { \rho _ { 1 } ^ { 2 } } & { = } & { ( \xi - \xi _ { 1 } ) ^ { 2 } + ( \eta - \eta _ { 1 } ) ^ { 2 } + \zeta ^ { 2 } , } \\ { \rho _ { 2 } ^ { 2 } } & { = } & { ( \xi - \xi _ { 2 } ) ^ { 2 } + ( \eta - \eta _ { 2 } ) ^ { 2 } + \zeta ^ { 2 } . } \end{array}
$$

# 9.3 Jacobi Integral

Consider the function

$$
\mathsf C = 2 \left( \frac { \mathsf { \partial } \mathsf { k } _ { 1 } } { \mathsf { \partial } \mathsf { \partial } \mathsf { p } _ { 1 } } + \frac { \mathsf { \partial } \mathsf { k } _ { 2 } } { \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } } \right) + 2 \mathsf { \partial } \mathsf { \omega } ( \boldsymbol { \xi } , \dot { \boldsymbol { \eta } } - \boldsymbol { \eta } \dot { \boldsymbol { \xi } } ) - \dot { \boldsymbol { \xi } } ^ { 2 } - \dot { \boldsymbol { \eta } } ^ { 2 } - \dot { \boldsymbol { \zeta } } ^ { 2 } .
$$

The time derivative of this function is written

$$
\dot { C } = - \frac { 2 \mu _ { 1 } \dot { \rho } _ { 1 } } { \rho _ { 1 } ^ { 2 } } - \frac { 2 \mu _ { 2 } \dot { \rho } _ { 2 } } { \rho _ { 2 } ^ { 2 } } + 2 \omega \left( \xi , \ddot { \eta } - \eta \ddot { \xi } \right) - 2 \dot { \xi } , \ddot { \xi } - 2 \dot { \eta } \ddot { \eta } - 2 \dot { \zeta } \ddot { \zeta } .
$$

Moreover, it follows, from Equations (9.3)–(9.4) and (9.8)–(9.9), that

$$
\begin{array} { r l r } { \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Sigma } \mathsf { \Sigma } ( \mathsf { \Sigma } ) \mathsf { \Sigma } ( \mathsf { \Sigma } ) } & { = } & { - ( \xi _ { 1 } \dot { \xi } + \mathsf { \Pi } \mathsf { \Pi } \dot { \mathsf { \Sigma } } + \mathsf { \Pi } \mathsf { \Sigma } \mathsf { \Sigma } \mathsf { \Sigma } \mathsf { \Sigma } ( \xi , \mathsf { \Pi } ) + \mathsf { \Sigma } ( \xi , \mathsf { \Pi } ) \mathsf { \Sigma } ( \xi , \mathsf { \Sigma } ) + \xi , \dot { \xi } + \mathsf { \Pi } \dot { \mathsf { \Sigma } } + \mathsf { \Pi } \dot { \mathsf { \Sigma } } \dot { \zeta } , } \\ { \mathsf { \Pi } \mathsf { \Sigma } \dot { \mathsf { \Sigma } } \mathsf { \Sigma } ( \mathsf { \Sigma } ) } & { = } & { - ( \xi _ { 2 } \dot { \xi } + \mathsf { \Pi } \mathsf { \Sigma } \mathsf { \Pi } \dot { \mathsf { \Sigma } } ) + \mathsf { \Delta } ( \xi , \mathsf { \Pi } ) - \mathsf { \Pi } \xi _ { 2 } \mathsf { \Sigma } ) + \xi , \dot { \xi } + \mathsf { \Pi } \dot { \mathsf { \Sigma } } + \zeta \dot { \zeta } . } \end{array}
$$

Combining Equations (9.5)–(9.7) with the above three expressions, we obtain (after considerable algebra)

$$
{ \dot { C } } = 0 .
$$

In other words, the function C—which is usually referred to as the Jacobi integral—is a constant of the motion.

Now, we can rearrange Equation (9.10) to give

$$
{ \mathcal { E } } \equiv { \frac { 1 } { 2 } } \left( { \dot { \xi } } ^ { 2 } + { \dot { \eta } } ^ { 2 } + { \dot { \zeta } } ^ { 2 } \right) - \left( { \frac { \mu _ { 1 } } { \rho _ { 1 } } } + { \frac { \mu _ { 2 } } { \rho _ { 2 } } } \right) = \mathbf { { \boldsymbol { \omega } } } \cdot \mathbf { h } - { \frac { \zeta } { 2 } } ,
$$

where $\mathcal { E }$ is the energy (per unit mass) of $\mathrm { \ m a s s \ m } _ { 3 }$ , $\mathbf { h } = \mathbf { r } \times \dot { \mathbf { r } }$ its angular momentum (per unit mass), and ${ \boldsymbol { \omega } } = ( 0 , 0 , \omega )$ the orbital angular velocity of the other two masses. Note, however, that $\mathbf { h }$ is not a constant of the motion. Hence, $\mathcal { E }$ is not a constant of the motion either. In fact, the Jacobi integral is the only constant of the motion in the circular restricted three-body problem. Incidentally, the energy of mass $\mathfrak { m } _ { 3 }$ is not a conserved quantity because the other two masses in the system are moving.

# 9.4 Tisserand Criterion

Consider a dynamical system consisting of three gravitationally interacting point masses, $\mathfrak { m } _ { 1 }$ , $\mathfrak { m } _ { 2 }$ , and $\mathfrak { m } _ { 3 }$ . Let mass $\mathfrak { m } _ { 1 }$ represent the Sun, mass $\mathfrak { m } _ { 2 }$ the planet Jupiter, and mass $\mathfrak { m } _ { 3 }$ a comet. Since the mass of a comet is very much less than that of the Sun or Jupiter, and the Sun and Jupiter are in (almost) circular orbits about their common center of mass, the dynamical system in question satisfies all of the necessary criteria to be considered an example of a restricted three-body problem.

Now, the mass of the Sun is much greater than that of Jupiter. It follows that the gravitational effect of Jupiter on the cometary orbit is negligible unless the comet makes a very close approach to Jupiter. Hence, as described in Chapter 4, before and after such an approach, the comet executes a standard elliptical orbit about the Sun with fixed orbital parameters: i.e., fixed major radius, eccentricity, and inclination to the ecliptic plane. However, in general, the orbital parameters before and after the close approach will not be the same as one another. Let us investigate further.

Now, since $\mathfrak { m } _ { 1 } \ \gg \ \mathfrak { m } _ { 2 }$ , we have $\mu _ { 1 } = \mathsf { G m } _ { 1 } \simeq \mathsf { G } \left( \mathsf { m } _ { 1 } + \mathsf { m } _ { 2 } \right) = 1$ , and $\rho _ { 1 } \simeq \tau$ . Hence, according to Equations (4.35) and (4.44), the (approximately) conserved energy (per unit mass) of the comet before and after its close approach to Jupiter is

$$
\mathcal { E } \equiv \frac { 1 } { 2 } \left( \dot { \xi } ^ { 2 } + \dot { \eta } ^ { 2 } + \dot { \zeta } ^ { 2 } \right) - \frac { 1 } { \tau } = - \frac { 1 } { 2 \alpha } .
$$

Note that the comet’s orbital energy is entirely determined by its major radius, a. (Incidentally, we are working in units such that the major radius of Jupiter’s orbit is unity.) Furthermore, the (approximately) conserved angular momentum (per unit mass) of the comet before and after its approach to Jupiter is written $\mathbf { h }$ , where h is directed normal to the comet’s orbital plane, and, from Equations (B.7) and (4.31),

$$
{ \mathsf { h } } ^ { 2 } = { \mathsf { a } } ( 1 - e ^ { 2 } ) .
$$

Here, e is the comet’s orbital eccentricity. It follows that

$$
\mathbf { \omega } \mathbf { \omega } \cdot \mathbf { h } = { \omega \mathrm { ~ h ~ } } \cos \mathrm { { I } } = { \sqrt { \mathrm { { a } } \left( 1 - e ^ { 2 } \right) } } \cos \mathrm { { I } } ,
$$

since $\omega = 1$ in our adopted system of units. Here, I is the angle of inclination of the normal to the comet’s orbital plane to that of Jupiter’s orbital plane.

Let a, e, and I be the major radius, eccentricity, and inclination angle of the cometary orbit before the close encounter with Jupiter, and let ${ \mathrm {  ~ a } } ^ { \prime } , { \mathrm {  ~ } e } ^ { \prime }$ , and $\mathrm { I ^ { \prime } }$ be the corresponding parameters after the encounter. It follows from Equations (9.15), (9.16), and (9.18), and the fact that C is conserved during the encounter, whereas $\mathcal { E }$ and $\mathrm { \hslash }$ are not, that

$$
{ \frac { 1 } { 2 \mathrm { a } } } + { \sqrt { \mathrm { a } \left( 1 - e ^ { 2 } \right) } } \cos \mathrm { I } = { \frac { 1 } { 2 \mathrm { a } ^ { \prime } } } + { \sqrt { \mathrm { a } ^ { \prime } \left( 1 - e ^ { \prime 2 } \right) } } \cos \mathrm { I } ^ { \prime } .
$$

This result is known as the Tisserand criterion, after the French astronomer Felix Tisserand (1845-1896) who discovered it, and restricts the possible changes in the orbital parameters of a comet due to a close encounter with Jupiter (or any other massive planet).

The Tisserand criterion is very useful. For instance, whenever a new comet is discovered, astronomers immediately calculate its Tisserand parameter,

$$
\mathsf { T } _ { \mathrm { J } } = \frac { 1 } { \mathrm { a } } + 2 \sqrt { \mathrm { a } \left( 1 - e ^ { 2 } \right) } \cos \mathrm { I } .
$$

If this parameter has the same value as that of a previously observed comet then it is quite likely that the new comet is, in fact, the same comet, but that its orbital parameters have changed since it was last observed, due to a close encounter with Jupiter. Incidentally, the subscript J in the above formula is to remind us that we are dealing with the Tisserand parameter for close encounters with Jupiter. (The parameter is, thus, evaluated in a system of units in which the major radius of Jupiter’s orbit is unity). Obviously, it is also possible to calculate Tisserand parameters for close encounters with other planets.

The Tisserand criterion is also applicable to so-called gravity assists, in which a spacecraft gains energy due to a close encounter with a moving planet. Such assists are often employed in missions to the outer planets to reduce the amount of fuel which the spacecraft must carry in order to reach its destination. In fact, it is clear, from Equations (9.16) and (9.19), that a space-craft can make use of a close encounter with a moving planet to increase (or decrease) its orbital major radius a, and, hence, to increase (or decrease) its total orbital energy.

![](images/2e59383b180276f7d5ad01249568a31f4c0ea1171e7b2af12f78d5a6aa0b2c26.jpg)  
Figure 9.2: The co-rotating frame.

# 9.5 Co-Rotating Frame

Let us transform to a non-inertial frame of reference rotating with angular velocity $\omega$ about an axis normal to the orbital plane of masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , and passing through their center of mass. It follows that masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ appear stationary in this new reference frame. Let us define a Cartesian coordinate system $( x , y , z )$ in the rotating frame of reference which is such that masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ always lie on the $x$ -axis, and the $z$ -axis is parallel to the previously defined $\zeta$ -axis. It follows that masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ have the fixed position vectors $\mathbf { r } _ { 1 } = \mu _ { 2 } \left( - 1 , 0 , 0 \right)$ and $\mathbf { r } _ { 2 } = \mu _ { 1 } \left( 1 , 0 , 0 \right)$ in our new coordinate system. Finally, let the position vector of mass $\mathfrak { m } _ { 3 }$ be $\mathbf { r } = ( x , y , z )$ —see Figure 9.2.

According to Section 6.2, the equation of motion of mass $\mathfrak { m } _ { 3 }$ in the rotating reference frame takes the form

$$
\ddot { \bf r } + 2 { \bf \delta } \omega \times \dot { \bf r } = - { \bf \mu } _ { 1 } \frac { ( { \bf r } - { \bf r } _ { 1 } ) } { \rho _ { 1 } ^ { 3 } } - { \bf \mu } _ { 2 } \frac { ( { \bf r } - { \bf r } _ { 2 } ) } { \rho _ { 2 } ^ { 3 } } - { \bf  } \times ( { \bf \boldsymbol { \omega } } \times { \bf r } ) ,
$$

where ${ \boldsymbol { \omega } } = ( 0 , 0 , \omega )$ , and

$$
\begin{array} { r l r } { \rho _ { 1 } ^ { 2 } } & { = } & { ( \kappa + \mu _ { 2 } ) ^ { 2 } + \mathfrak { y } ^ { 2 } + z ^ { 2 } , } \\ { \rho _ { 2 } ^ { 2 } } & { = } & { ( \kappa - \mu _ { 1 } ) ^ { 2 } + \mathfrak { y } ^ { 2 } + z ^ { 2 } . } \end{array}
$$

Here, the second term on the left-hand side of Equation (9.21) is the Coriolis acceleration, whereas the final term on the right-hand side is the centrifugal acceleration. The

components of Equation (9.21) reduce to

$$
\begin{array} { r c l } { \ddot { x } - 2 \omega \dot { y } } & { = } & { - \frac { \mu _ { 1 } \left( x + \mu _ { 2 } \right) } { \rho _ { 1 } ^ { 3 } } - \frac { \mu _ { 2 } \left( x - \mu _ { 1 } \right) } { \rho _ { 2 } ^ { 3 } } + \omega ^ { 2 } x , } \\ { \ddot { y } + 2 \omega \dot { x } } & { = } & { - \frac { \mu _ { 1 } \psi } { \rho _ { 1 } ^ { 3 } } - \frac { \mu _ { 2 } \psi } { \rho _ { 2 } ^ { 3 } } + \omega ^ { 2 } y , } \\ { \ddot { z } } & { = } & { - \frac { \mu _ { 1 } z } { \rho _ { 1 } ^ { 3 } } - \frac { \mu _ { 2 } z } { \rho _ { 2 } ^ { 3 } } , } \end{array}
$$

which yield

$$
\begin{array} { r l r } { \ddot { \mathnormal { x } } - 2 \omega \dot { \mathfrak { y } } } & { = } & { - \frac { \partial \mathsf { U } } { \partial \mathfrak { x } } , } \\ { \ddot { \mathfrak { y } } + 2 \omega \dot { \mathfrak { x } } } & { = } & { - \frac { \partial \mathsf { U } } { \partial \mathfrak { y } } , } \\ { \ddot { \mathnormal { z } } } & { = } & { - \frac { \partial \mathsf { U } } { \partial \mathfrak { z } } , } \end{array}
$$

where

$$
{ \sf U } = - \frac { { \sf u } _ { 1 } } { { \sf \rho } _ { 1 } } - \frac { { \sf u } _ { 2 } } { { \sf \rho } _ { 2 } } - \frac { \omega ^ { 2 } } { 2 } \left( x ^ { 2 } + y ^ { 2 } \right)
$$

is the sum of the gravitational and centrifugal potentials.

Now, it follows from Equations (9.27)–(9.29) that

$$
\begin{array} { r l r } { \ddot { x } \dot { x } - 2 \omega \dot { x } \dot { y } } & { = } & { - \dot { x } \frac { \partial \mathsf { U } } { \partial x } , } \\ { \ddot { y } \dot { y } + 2 \omega \dot { x } \dot { y } } & { = } & { - \dot { y } \frac { \partial \mathsf { U } } { \partial y } , } \\ { \ddot { z } \dot { z } } & { = } & { - \dot { z } \frac { \partial \mathsf { U } } { \partial z } . } \end{array}
$$

Summing the above three equations, we obtain

$$
\frac { \mathrm { d } } { \mathrm { d t } } \left[ \frac { 1 } { 2 } \left( \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } \right) + \mathrm { u } \right] = 0 .
$$

In other words,

$$
\mathsf { C } = - 2 \mathsf { U } - \mathsf { \nu } \mathsf { \nu } ^ { 2 }
$$

is a constant of the motion, where $\nu ^ { 2 } = \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 }$ . In fact, $C$ is the Jacobi integral introduced in Section 9.3 [it is easily demonstrated that Equations (9.10) and (9.35) are identical]. Note, finally, that the mass $\mathfrak { m } _ { 3 }$ is restricted to regions in which

$$
- 2 \mathsf { U } \geq \mathsf { C } ,
$$

since $\nu ^ { 2 }$ is a positive definite quantity.

# 9.6 Lagrange Points

Let us search for possible equilibrium points of the mass $\mathfrak { m } _ { 3 }$ in the rotating reference frame. Such points are termed Lagrange points. Thus, in the rotating frame, the mass $\mathfrak { m } _ { 3 }$ would remain at rest if placed at one of the Lagrange points. It is, thus, clear that these points are fixed in the rotating frame. Conversely, in the inertial reference frame, the Lagrange points rotate about the center of mass with angular velocity $\omega$ , and the $\mathrm { \ m a s s \ m _ { 3 } }$ would consequently also rotate about the center of mass with angular velocity $\omega$ if placed at one of these points (with the appropriate velocity). In the following, we shall assume, without loss of generality, that $\mathfrak { m } _ { 1 } \geq \mathfrak { m } _ { 2 }$ .

The Lagrange points satisfy $\dot { \mathbf { r } } = \ddot { \mathbf { r } } = \mathbf { 0 }$ in the rotating frame. It thus follows, from Equations (9.27)–(9.29), that the Lagrange points are the solutions of

$$
\frac { \partial \mathrm { U } } { \partial \boldsymbol { x } } = \frac { \partial \mathrm { U } } { \partial \boldsymbol { y } } = \frac { \partial \mathrm { U } } { \partial z } = 0 .
$$

Now, it is easily seen that

$$
\frac { \partial \mathrm { u } } { \partial z } = \left( \frac { \mu _ { 1 } } { \rho _ { 1 } ^ { 3 } } + \frac { \mu _ { 2 } } { \rho _ { 2 } ^ { 3 } } \right) z .
$$

Since the term in brackets is positive definite, we conclude that the only solution to the above equation is $z = 0$ . Hence, all of the Lagrange points lie in the $x { - } y$ plane.

If $z = 0$ then it is readily demonstrated that

$$
\mu _ { 1 } \rho _ { 1 } ^ { 2 } + \mu _ { 2 } \rho _ { 2 } ^ { 2 } = { x } ^ { 2 } + { y } ^ { 2 } + \mu _ { 1 } \mu _ { 2 } ,
$$

where use has been made of the fact that $\mu _ { 1 } + \mu _ { 2 } = 1$ . Hence, Equation (9.30) can also be written

$$
\mathsf { U } = - \mu _ { 1 } \left( \frac { 1 } { \rho _ { 1 } } + \frac { \rho _ { 1 } ^ { 2 } } { 2 } \right) - \mu _ { 2 } \left( \frac { 1 } { \rho _ { 2 } } + \frac { \rho _ { 2 } ^ { 2 } } { 2 } \right) + \frac { \mu _ { 1 } \mu _ { 2 } } { 2 } .
$$

The Lagrange points thus satisfy

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial \mathsf { U } } { \partial \boldsymbol { x } } } } & { { = } } & { { \displaystyle \frac { \partial \mathsf { U } } { \partial \boldsymbol { \rho } _ { 1 } } \frac { \partial \boldsymbol { \rho } _ { 1 } } { \partial \boldsymbol { x } } + \frac { \partial \mathsf { U } } { \partial \boldsymbol { \rho } _ { 2 } } \frac { \partial \boldsymbol { \rho } _ { 2 } } { \partial \boldsymbol { x } } = 0 , } } \\ { { \displaystyle \frac { \partial \mathsf { U } } { \partial \boldsymbol { \mu } } } } & { { = } } & { { \displaystyle \frac { \partial \mathsf { U } } { \partial \boldsymbol { \rho } _ { 1 } } \frac { \partial \boldsymbol { \rho } _ { 1 } } { \partial \boldsymbol { \nu } } + \frac { \partial \mathsf { U } } { \partial \boldsymbol { \rho } _ { 2 } } \frac { \partial \boldsymbol { \rho } _ { 2 } } { \partial \boldsymbol { \mu } } = 0 , } } \end{array}
$$

which reduce to

$$
\begin{array} { r l r } { \mu _ { 1 } \left( \frac { 1 - \rho _ { 1 } ^ { 3 } } { \rho _ { 1 } ^ { 2 } } \right) \left( \frac { x + \mu _ { 2 } } { \rho _ { 1 } } \right) + \mu _ { 2 } \left( \frac { 1 - \rho _ { 2 } ^ { 3 } } { \rho _ { 2 } ^ { 2 } } \right) \left( \frac { x - \mu _ { 1 } } { \rho _ { 2 } } \right) } & { = } & { 0 , } \\ { \mu _ { 1 } \left( \frac { 1 - \rho _ { 1 } ^ { 3 } } { \rho _ { 1 } ^ { 2 } } \right) \left( \frac { \ y } { \rho _ { 1 } } \right) + \mu _ { 2 } \left( \frac { 1 - \rho _ { 2 } ^ { 3 } } { \rho _ { 2 } ^ { 2 } } \right) \left( \frac { \ y } { \rho _ { 2 } } \right) } & { = } & { 0 . } \end{array}
$$

Now, one obvious solution of Equation (9.44) is ${ \mathfrak { y } } = 0$ , corresponding to a Lagrange point which lies on the $x$ -axis. It turns out that there are three such points. $\mathrm { L } _ { 1 }$ lies between

masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , $\mathrm { L } _ { 2 }$ lies to the right of mass $\mathfrak { m } _ { 2 }$ , and $\mathrm { L } _ { 3 }$ lies to the left of mass $\mathfrak { m } _ { 1 }$ —see Figure 9.2. At the $\mathrm { L } _ { 1 }$ point, we have ${ \sf x } = - { \sf u } _ { 2 } + { \sf \rho } _ { 1 } = { \sf \mu } _ { 1 } - { \sf \rho } _ { 2 }$ and $\rho _ { 1 } = 1 - \rho _ { 2 }$ . Hence, from Equation (9.43),

$$
\frac { \mu _ { 2 } } { 3 \mu _ { 1 } } = \frac { \rho _ { 2 } ^ { 3 } \left( 1 - \rho _ { 2 } + \rho _ { 2 } ^ { 2 } / 3 \right) } { \left( 1 + \rho _ { 2 } + \rho _ { 2 } ^ { 2 } \right) \left( 1 - \rho _ { 2 } \right) ^ { 3 } } .
$$

Assuming that $\rho _ { 2 } \ll 1$ , we can find an approximate solution of Equation (9.45) by expanding in powers of $\rho _ { 2 }$ :

$$
\alpha = \rho _ { 2 } + \frac { \rho _ { 2 } ^ { 2 } } { 3 } + \frac { \rho _ { 2 } ^ { 3 } } { 3 } + \frac { 5 1 \mathrm { \ p } _ { 2 } ^ { 4 } } { 8 1 } + { \mathcal O } ( \mathrm { \ p } _ { 2 } ^ { 5 } ) .
$$

This equation can be inverted to give

$$
\rho _ { 2 } = \alpha - \frac { \alpha ^ { 2 } } 3 - \frac { \alpha ^ { 3 } } { 9 } - \frac { 2 3 \alpha ^ { 4 } } { 8 1 } + \mathcal { O } ( \alpha ^ { 5 } ) ,
$$

where

$$
\alpha = \left( \frac { \mu _ { 2 } } { 3 \mu _ { 1 } } \right) ^ { 1 / 3 } .
$$

is assumed to be a small parameter.

At the $\mathrm { L } _ { 2 }$ point, we have ${ \sf x } = - { \sf u } _ { 2 } + { \sf \rho } _ { 1 } = { \sf \mu } _ { 1 } + { \sf \rho } _ { 2 }$ and $\rho _ { 1 } = 1 + \rho _ { 2 }$ . Hence, from Equation (9.43),

$$
\frac { \mu _ { 2 } } { 3 \mu _ { 1 } } = \frac { \rho _ { 2 } ^ { 3 } \left( 1 + \rho _ { 2 } + \rho _ { 2 } ^ { 2 } / 3 \right) } { ( 1 + \rho _ { 2 } ) ^ { 2 } \left( 1 - \rho _ { 2 } ^ { 3 } \right) } .
$$

Again, expanding in powers of $\rho _ { 2 }$ , we obtain

$$
\begin{array} { r c l } { { \displaystyle \alpha } } & { { = } } & { { \displaystyle \mathsf { \rho } _ { 2 } - \frac { \mathsf { \rho } _ { 2 } ^ { 2 } } { 3 } + \frac { \mathsf { \rho } _ { 2 } ^ { 3 } } { 3 } + \frac { \mathsf { \rho } _ { 2 } ^ { 4 } } { 8 1 } + \mathcal { O } ( \mathsf { \rho } _ { 2 } ^ { 5 } ) , } } \\ { { \displaystyle \mathsf { \rho } _ { 2 } } } & { { = } } & { { \displaystyle \alpha + \frac { \alpha ^ { 2 } } { 3 } - \frac { \alpha ^ { 3 } } { 9 } - \frac { 3 1 \mathrm { \ } \alpha ^ { 4 } } { 8 1 } + \mathcal { O } ( \alpha ^ { 5 } ) . } } \end{array}
$$

Finally, at the $\mathrm { L } _ { 3 }$ point, we have ${ \sf x } = - { \sf \mu } _ { 2 } - { \sf \rho } _ { 1 } = { \sf \mu } _ { 1 } - { \sf \rho } _ { 2 }$ and $\rho _ { 2 } = 1 + \rho _ { 1 }$ . Hence, from Equation (9.43),

$$
\frac { \mu _ { 2 } } { \mu _ { 1 } } = \frac { \left( 1 - \rho _ { 1 } ^ { 3 } \right) ( 1 + \rho _ { 1 } ) ^ { 2 } } { \rho _ { 1 } ^ { 3 } \left( \rho _ { 1 } ^ { 2 } + 3 \rho _ { 1 } + 3 \right) } .
$$

Let $\rho _ { 1 } = 1 - \beta$ . Expanding in powers of $\beta$ , we obtain

$$
\begin{array} { r c l } { { \frac { \mu _ { 2 } } { \mu _ { 1 } } } } & { { = } } & { { \displaystyle \frac { 1 2 \beta } { 7 } + \frac { 1 4 4 \beta ^ { 2 } } { 4 9 } + \frac { 1 5 6 7 \beta ^ { 3 } } { 3 4 3 } + { \mathcal O } ( \beta ^ { 4 } ) , } } \\ { { \beta } } & { { = } } & { { \displaystyle \frac { 7 } { 1 2 } \left( \frac { \mu _ { 2 } } { \mu _ { 1 } } \right) - \frac { 7 } { 1 2 } \left( \frac { \mu _ { 2 } } { \mu _ { 1 } } \right) ^ { 2 } + \frac { 1 3 2 2 3 } { 2 0 7 3 6 } \left( \frac { \mu _ { 2 } } { \mu _ { 1 } } \right) ^ { 3 } + { \mathcal O } \left( \frac { \mu _ { 2 } } { \mu _ { 1 } } \right) ^ { 4 } , } } \end{array}
$$

where $\mu _ { 2 } / \mu _ { 1 }$ is assumed to be a small parameter.

![](images/85dd24041f750c79d0ff0275609e5b3df7ab5a6068383f7a7d55ef7fbcc2cd5c.jpg)  
Figure 9.3: The masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 } ,$ and the five Lagrange points, $\mathrm { L } _ { 1 }$ to $\mathrm { L } _ { 5 } ,$ calculated for $\mu _ { 2 } = 0 . 1$ .

Let us now search for Lagrange points which do not lie on the $x$ -axis. One obvious solution of Equations (9.41) and (9.42) is

$$
\frac { \partial \mathsf { U } } { \partial \rho _ { 1 } } = \frac { \partial \mathsf { U } } { \partial \rho _ { 2 } } = 0 ,
$$

giving, from Equation (9.40),

$$
\rho _ { 1 } = \rho _ { 2 } = 1 ,
$$

or

$$
( x + \mu _ { 2 } ) ^ { 2 } + \mathbf { y } ^ { 2 } = ( { \mathsf { x } } - 1 + \mu _ { 2 } ) ^ { 2 } + \mathbf { y } ^ { 2 } = 1 ,
$$

since $\mu _ { 1 } = 1 - \mu _ { 2 }$ . The two solutions of the above equation are

$$
\begin{array} { r c l } { { x } } & { { = } } & { { { \displaystyle \frac { 1 } { 2 } } - \mu _ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { y } } & { { = } } & { { \pm \displaystyle \frac { \sqrt { 3 } } { 2 } , } } \end{array}
$$

and specify the positions of the Lagrange points designated $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ . Note that point $\mathrm { L } _ { 4 }$ and the masses $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ lie at the apexes of an equilateral triangle. The same is true for point $\mathrm { L } _ { 5 }$ . We have now found all of the possible Lagrange points.

Figure 9.3 shows the positions of the two masses, $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , and the five Lagrange points, $\mathrm { L } _ { 1 }$ to $\mathrm { L } _ { 5 }$ , calculated for the case where $\mu _ { 2 } = 0 . 1$ .

# 9.7 Zero-Velocity Surfaces

Consider the surface

$$
{ \mathsf { V } } ( { \boldsymbol { x } } , { \boldsymbol { y } } , z ) = { \mathsf { C } } ,
$$

where

$$
V = - 2 \operatorname { U } = \frac { 2 \mu _ { 1 } } { \rho _ { 1 } } + \frac { 2 \mu _ { 2 } } { \rho _ { 2 } } + \boldsymbol { x } ^ { 2 } + \boldsymbol { y } ^ { 2 } .
$$

Note that $\vee \geq 0$ . It follows, from Equation (9.35), that if the mass $\mathfrak { m } _ { 3 }$ has the Jacobi integral $C$ , and lies on the surface specified in Equation (9.60), then it must have zero velocity. Hence, such a surface is termed a zero-velocity surface. The zero-velocity surfaces are important because they form the boundary of regions from which the mass $\mathfrak { m } _ { 3 }$ is dynamically excluded: i.e., regions in which ${ \mathsf { V } } < { \mathsf { C } }$ . Generally speaking, the regions from which $\mathfrak { m } _ { 3 }$ is excluded grow in area as C increases, and vice versa.

Let $C _ { \mathrm { i } }$ be the value of $\vee$ at the $\mathrm { L } _ { \mathrm { i } }$ Lagrange point, for $i = 1 , 5$ . When $\mu _ { 2 } \ll 1$ , it is easily demonstrated that

$$
\begin{array} { r c l } { { { \bf C } _ { 1 } } } & { { \simeq } } & { { 3 + 3 ^ { 4 / 3 } \mu _ { 2 } ^ { 2 / 3 } - 1 0 \mu _ { 2 } / 3 , } } \\ { { } } & { { } } & { { } } \\ { { { \bf C } _ { 2 } } } & { { \simeq } } & { { 3 + 3 ^ { 4 / 3 } \mu _ { 2 } ^ { 2 / 3 } - 1 4 \mu _ { 2 } / 3 , } } \\ { { } } & { { } } & { { } } \\ { { { \bf C } _ { 3 } } } & { { \simeq } } & { { 3 + \mu _ { 2 } , } } \\ { { } } & { { } } & { { { \bf C } _ { 4 } } } & { { \simeq } } & { { 3 - \mu _ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { { \bf C } _ { 4 } } } & { { \simeq } } & { { 3 - \mu _ { 2 } . } } \end{array}
$$

Note that $\mathrm { C } _ { 1 } > \mathrm { C } _ { 2 } > \mathrm { C } _ { 3 } > \mathrm { C } _ { 4 } = \mathrm { C } _ { 5 }$ .

Figures $9 . 4 \ – 9 . 8$ show the intersection of the zero-velocity surface ${ \mathsf { V } } = { \mathsf { C } }$ with the $x { - } y$ plane for various different values of C, and illustrate how the region from which $\mathfrak { m } _ { 3 }$ is dynamically excluded—which we shall term the excluded region—evolves as the value of C is varied. Of course, any point not in the excluded region is in the so-called allowed region. For $C > C _ { 1 }$ , the allowed region consists of two separate oval regions centered on $\mathfrak { m } _ { 1 }$ and $\mathfrak { m } _ { 2 }$ , respectively, plus an outer region which lies beyond a large circle centered on the origin. All three allowed regions are separated from one another by an excluded region—see Figure 9.4. When $C = C _ { 1 }$ , the two inner allowed regions merge at the $\mathrm { L } _ { 1 }$ point—see Figure 9.5. When $C = C _ { 2 }$ , the inner and outer allowed regions merge at the $\mathrm { L } _ { 2 }$ point, forming a horseshoe-like excluded region—see Figure 9.6. When $C = C _ { 3 }$ , the excluded region splits in two at the $\mathrm { L } _ { 3 }$ point—see Figure 9.7. For ${ \mathsf C } _ { 4 } < { \mathsf C } < { \mathsf C } _ { 3 }$ , the two excluded regions are localized about the $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ points—see Figure 9.8. Finally, for $C < C _ { 4 }$ , there is no excluded region.

Figure 9.9 shows the zero-velocity surfaces and Lagrange points calculated for the case $\mu _ { 2 } = 0 . 0 1$ . It can be seen that, at very small values of $\mu _ { 2 }$ , the $\mathrm { L } _ { 1 }$ and $\mathrm { L } _ { 2 }$ Lagrange points are almost equidistant from mass $\mathfrak { m } _ { 2 }$ . Furthermore, $\mathrm { m a s s } \ \mathsf { m } _ { 2 }$ , and the $\mathrm { L } _ { 3 } , \mathrm { L } _ { 4 }$ , and $\mathrm { L } _ { 5 }$ Lagrange points all lie approximately on a unit circle, centered on mass $\mathfrak { m } _ { 1 }$ . It follows that, when $\mu _ { 2 }$ is small, the Lagrange points $\mathrm { L } _ { 3 }$ , $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ all share the orbit of mass $\mathfrak { m } _ { 2 }$ about $\mathfrak { m } _ { 1 }$ (in the inertial frame) with $C _ { 3 }$ being directly opposite $\mathfrak { m } _ { 2 } , \mathrm { ~ L _ { 4 } ~ }$ (by convention) $6 0 ^ { \circ }$ ahead of $\mathfrak { m } _ { 2 }$ , and $\mathrm { L } _ { 5 } 6 0 ^ { \circ }$ behind.

![](images/66e6983483f5831006737bb525dbda3e830ed2cd1ed55a1633390e65e955e25d.jpg)  
Figure 9.4: The zero-velocity surface ${ \mathrm {  ~ V ~ } } = { \mathrm {  ~ C ~ } } ,$ where ${ \mathrm { { C } } } > { \mathrm { { C } } } _ { 1 } ,$ calculated for $\mu _ { 2 } = 0 . 1$ . The mass $\mathfrak { m } _ { 3 }$ is excluded from the region lying between the two inner curves and the outer curve.

![](images/a3cc57fac564fbf499d6862ef81b9eeb4174fe35fb5062a08ebf02d1d3c1751a.jpg)  
Figure 9.5: The zero-velocity surface ${ \mathrm {  ~ V ~ } } = { \mathrm {  ~ C ~ } } ,$ , where ${ \mathrm { { C } } } = { \mathrm { { C } } } _ { 1 } ,$ calculated for $\mu _ { 2 } = 0 . 1$ . The mass $\mathfrak { m } _ { 3 }$ is excluded from the region lying between the inner and outer curves.

![](images/f0307f396a0aee29e61c8c9cc68b422426cb157d49715b8a5595e4ac4c77f14d.jpg)  
Figure 9.6: The zero-velocity surface ${ \mathrm {  ~ V ~ } } = { \mathrm {  ~ C ~ } } ,$ where $C = C _ { 2 } ,$ calculated for $\mu _ { 2 } = 0 . 1$ . The mass $\mathfrak { m } _ { 3 }$ is excluded from the region lying between the inner and outer curve.

![](images/535c4acda8ba2a6599a386f73f546c0f68a4c12f7a97e37a0e84a88c5eeb3f73.jpg)  
Figure 9.7: The zero-velocity surface ${ \mathrm {  ~ V ~ } } = { \mathrm {  ~ C ~ } } ,$ , where ${ \mathrm { { C } } } = { \mathrm { { C } } } _ { 3 } { \mathrm { { , } } }$ calculated for $\mu _ { 2 } = 0 . 1$ . The mass $\mathfrak { m } _ { 3 }$ is excluded from the regions lying inside the curve.

![](images/5adc893ed4b2dd4b8e6f85472890e8d9c6971a9404fcba17f2c257e692344d03.jpg)  
Figure 9.8: The zero-velocity surface ${ \mathrm { V } } = { \mathrm { C } } ,$ , where $\begin{array} { r } { C _ { 4 } < C < C _ { 3 } , } \end{array}$ calculated for $\mu _ { 2 } = 0 . 1$ . The mass $\mathfrak { m } _ { 3 }$ is excluded from the regions lying inside the two curves.

# 9.8 Stability of Lagrange Points

We have seen that the five Lagrange points, $\mathrm { L } _ { 1 }$ to $\mathrm { L } _ { 5 }$ , are the equilibrium points of mass $\mathfrak { m } _ { 3 }$ in the co-rotating frame. Let us now determine whether or not these equilibrium points are stable to small displacements.

Now, the equations of motion of mass $\mathfrak { m } _ { 3 }$ in the co-rotating frame are specified in Equations (9.27)–(9.29). Note that the motion in the $x { - } y$ plane is complicated by presence of the Coriolis acceleration. However, the motion parallel to the $z$ -axis simply corresponds to motion in the potential U. Hence, the condition for the stability of the Lagrange points (which all lie at $z = 0$ ) to small displacements parallel to the $z$ -axis is simply (see Section 2.7)

$$
\left( \frac { \partial ^ { 2 } \mathsf { U } } { \partial z ^ { 2 } } \right) _ { z = 0 } = \frac { \mu _ { 1 } } { \rho _ { 1 } ^ { 3 } } + \frac { \mu _ { 2 } } { \rho _ { 2 } ^ { 3 } } > 0 .
$$

This condition is satisfied everywhere in the $x { - } y$ plane. Hence, the Lagrange points are all stable to small displacements parallel to the $z$ -axis. It, thus, remains to investigate their stability to small displacements lying within the $x { - } y$ plane.

Suppose that a Lagrange point is situated in the $x { - } y$ plane at coordinates $\left( \mathsf { x } _ { 0 } , \mathsf { y } _ { 0 } , 0 \right)$ . Let us consider small amplitude $x$ -y motion in the vicinity of this point by writing

$$
\begin{array} { r } { \mathrm { ~  ~ x ~ } = \mathrm { ~  ~ x ~ } _ { 0 } + \delta { \sf x } , } \end{array}
$$

![](images/0a861988955a25a67bdf6982e86a02eb34cc291e1acecf4ed0bb132b18f79571.jpg)  
Figure 9.9: The zero-velocity surfaces and Lagrange points calculated for $\mu _ { 2 } = 0 . 0 1$

$$
\begin{array} { r c l } { { \texttt y } } & { { = } } & { { \texttt y _ { 0 } + \delta \mathfrak y , } } \\ { { z } } & { { = } } & { { 0 , } } \end{array}
$$

where $\delta \ b { x }$ and $\delta \boldsymbol { \mu }$ are infinitesimal. Expanding $\mathsf { U } ( x , y , 0 )$ about the Lagrange point as a Taylor series, and retaining terms up to second-order in small quantities, we obtain

$$
\mathrm { U } = \mathrm { U } _ { 0 } + \mathrm { U } _ { x } \delta x + \mathrm { U } _ { \mathrm { y } } \delta \mathrm { y } + \frac { 1 } { 2 } \mathrm { U } _ { x x } \left( \delta x \right) ^ { 2 } + \mathrm { U } _ { x y } \delta x \delta \mathrm { y } + \frac { 1 } { 2 } \mathrm { U } _ { \mathrm { y y } } \left( \delta \mathrm { y } \right) ^ { 2 } ,
$$

where ${ \sf U } _ { 0 } = { \sf U } ( x _ { 0 } , y _ { 0 } , 0 )$ $\begin{array} { r } { \mathfrak { L } ( x _ { 0 } , \mathfrak { y } _ { 0 } , 0 ) , \mathrm { U } _ { x } = \partial \mathrm { U } ( x _ { 0 } , \mathfrak { y } _ { 0 } , 0 ) / \partial x , \mathrm { U } _ { x x } = \partial ^ { 2 } \mathrm { U } ( x _ { 0 } , \mathfrak { y } _ { 0 } , 0 ) / \partial x ^ { 2 } , } \end{array}$ etc. However, by definition, ${ \sf U } _ { \sf x } = { \sf U } _ { \sf y } = 0$ at a Lagrange point, so the expansion simplifies to

$$
{ \sf U } = { \sf U } _ { 0 } + \frac { 1 } { 2 } { \sf U } _ { x x } ( \delta { \sf x } ) ^ { 2 } + { \sf U } _ { x y } \delta { \sf x } \delta { \sf y } + \frac { 1 } { 2 } { \sf U } _ { y y } ( \delta { \sf y } ) ^ { 2 } .
$$

Finally, substitution of Equations (9.68)–(9.70), and (9.72) into the equations of $x$ -y motion, (9.27) and (9.28), yields

$$
\begin{array} { r l r } { \delta \ddot { \bf x } - 2 \delta \dot { \bf y } } & { = } & { - { \sf U } _ { x x } \delta x - { \sf U } _ { x y } \delta { \bf y } , } \\ { \delta \ddot { \bf y } + 2 \delta \dot { \bf x } } & { = } & { - { \sf U } _ { x y } \delta { \bf x } - { \sf U } _ { y y } \delta { \bf y } , } \end{array}
$$

since $\omega = 1$ .

Let us search for a solution of the above pair of equations of the form $\delta \mathbf { x ( t ) } = \delta \mathbf { x } _ { 0 } \exp ( \gamma \mathbf { t } )$ and $\delta \mathfrak { y } ( \mathfrak { t } ) = \delta \mathfrak { y } _ { 0 } \exp ( \gamma \mathfrak { t } )$ . We obtain

$$
\left( \begin{array} { l l } { \gamma ^ { 2 } + \mathsf { U } _ { x x } } & { - 2 \gamma + \mathsf { U } _ { x y } } \\ { 2 \gamma + \mathsf { U } _ { x y } } & { \gamma ^ { 2 } + \mathsf { U } _ { y y } } \end{array} \right) \left( \begin{array} { l } { \delta x _ { 0 } } \\ { \delta y _ { 0 } } \end{array} \right) = \left( \begin{array} { l } { 0 } \\ { 0 } \end{array} \right) .
$$

This equation only has a non-trivial solution if the determinant of the matrix is zero. Hence, we get

$$
\gamma ^ { 4 } + ( 4 + \mathsf { U } _ { x x } + \mathsf { U } _ { y y } ) \gamma ^ { 2 } + ( \mathsf { U } _ { x x } \mathsf { U } _ { y y } - \mathsf { U } _ { x y } ^ { 2 } ) = 0 .
$$

Now, it is convenient to define

$$
\begin{array} { r l } { \mathsf { A } } & { = \begin{array} { r l } { \frac { \mu _ { 1 } } { \rho _ { 1 } ^ { 3 } } + \frac { \mu _ { 2 } } { \rho _ { 2 } ^ { 3 } } , } \end{array} } \\ { \mathsf { B } } & { = \begin{array} { r l } { 3 \left[ \frac { \mu _ { 1 } } { \rho _ { 1 } ^ { 5 } } + \frac { \mu _ { 2 } } { \rho _ { 2 } ^ { 5 } } \right] \ y ^ { 2 } , } \end{array} } \\ { \mathsf { C } } & { = \begin{array} { r l } { 3 \left[ \frac { \mu _ { 1 } \left( x + \mu _ { 2 } \right) } { \rho _ { 1 } ^ { 5 } } + \frac { \mu _ { 2 } \left( x - \mu _ { 1 } \right) } { \rho _ { 2 } ^ { 5 } } \right] \ y , } \end{array} } \\ { \mathsf { D } } & { = \begin{array} { r l } { 3 \left[ \frac { \mu _ { 1 } \left( x + \mu _ { 2 } \right) ^ { 2 } } { \rho _ { 1 } ^ { 3 } } + \frac { \mu _ { 2 } \left( x - \mu _ { 1 } \right) ^ { 2 } } { \rho _ { 2 } ^ { 3 } } \right] , } \end{array} } \end{array}
$$

where all terms are evaluated at the point $\left( \mathsf { x } _ { 0 } , \mathsf { y } _ { 0 } , 0 \right)$ . It thus follows that

$$
\begin{array} { r c l } { \mathsf { U } _ { x x } } & { = } & { \mathsf { A } - \mathsf { D } - 1 , } \\ { \mathsf { U } _ { y y } } & { = } & { \mathsf { A } - \mathsf { B } - 1 , } \\ { \mathsf { U } _ { x y } } & { = } & { - \mathsf { C } . } \end{array}
$$

Consider the co-linear Lagrange points, $\mathrm { L } _ { 1 } , \mathrm { L } _ { 2 }$ , and $\mathrm { L } _ { 3 }$ . These all lie on the $x$ -axis, and are thus characterized by ${ \mathfrak { y } } = 0$ , $\rho _ { 1 } ^ { 2 } = ( \nu + \mu _ { 2 } ) ^ { 2 }$ , and $\rho _ { 2 } ^ { 2 } = ( \nu - \mu _ { 1 } ) ^ { 2 }$ . It follows, from the above equations, that $\mathtt { B } = \mathtt { C } = 0$ and $\mathrm { D } = 3 A$ . Hence, ${ \sf U } _ { x x } = - 1 - 2 A$ , $\mathrm { u } _ { \mathsf { y y } } = \mathsf { A } - 1$ , and $\mathsf { U } _ { \mathsf { x y } } = 0$ . Equation (9.76) thus yields

$$
\Gamma ^ { 2 } + ( 2 - \cal { A } ) \Gamma + ( 1 - \cal { A } ) ( 1 + 2 \cal { A } ) = 0 ,
$$

where $\Gamma = \gamma ^ { 2 }$ . Now, in order for a Lagrange point to be stable to small displacements, all four of the roots, $\gamma$ , of Equation (9.76) must be purely imaginary. This, in turn, implies that the two roots of the above equation,

$$
\Gamma = \frac { { A - 2 \pm \sqrt { \mathsf { A } \left( \vartheta \mathsf { A } - 8 \right) } } } { 2 } ,
$$

must both be real and negative. Thus, the stability criterion is

$$
\frac { 8 } { 9 } \leq A \leq 1 .
$$

Figure 9.10 shows A calculated at the three co-linear Lagrange points as a function of $\mu _ { 2 }$ , for all allowed values of this parameter (i.e., $0 < \mu _ { 2 } \leq 0 . 5 )$ . It can be seen that $\boldsymbol { \mathsf { A } }$ is always greater than unity for all three points. Hence, we conclude that the co-linear Lagrange points, $\mathrm { L } _ { 1 } , \mathrm { L } _ { 2 }$ , and $\mathrm { L } _ { 3 }$ , are intrinsically unstable equilibrium points in the co-rotating frame.

Let us now consider the triangular Lagrange points, $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ . These points are characterized by $\rho _ { 1 } = \rho _ { 2 } = 1$ . It follows that $\lambda = 1$ , $\mathrm { B } = 9 / 4$ , $\mathsf { C } = \pm \sqrt { 2 7 / 1 6 } \left( 1 - 2 \mu _ { 2 } \right)$ , and $\mathrm { D } = 3 / 4$ . Hence, $\mathrm { U } _ { x x } = - 3 / 4 , \mathrm { U } _ { y y } = - 9 / 4$ , and $\mathrm { U _ { \it x y \_ } = \mp \sqrt { 2 7 / 1 6 } ( 1 - 2 \mu _ { 2 } ) }$ , where the upper/lower signs corresponds to $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ , respectively. Equation (9.76) thus yields

$$
\Gamma ^ { 2 } + \Gamma + \frac { 2 7 } { 4 } \mu _ { 2 } \left( 1 - \mu _ { 2 } \right) = 0
$$

for both points, where $\Gamma = \gamma ^ { 2 }$ . As before, the stability criterion is that the two roots of the above equation must both be real and negative. This is the case provided that $1 > 2 7 \mu _ { 2 } \left( 1 - \mu _ { 2 } \right)$ , which yields the stability criterion

$$
\mu _ { 2 } < \frac { 1 } { 2 } \left( 1 - \sqrt { \frac { 2 3 } { 2 7 } } \right) = 0 . 0 3 8 5 .
$$

![](images/57c98999c0e111d9163711089578f85781a838fa360a87c8c43a08d6cd85a945.jpg)  
Figure 9.10: The solid, short-dashed, and long-dashed curves show A as a function of $\mu _ { 2 }$ at the L1, L2, and $\mathrm { L } _ { 3 }$ Lagrange points.

In unnormalized units, this criterion becomes

$$
\frac { \mathfrak { m } _ { 2 } } { \mathfrak { m } _ { 1 } + \mathfrak { m } _ { 2 } } < 0 . 0 3 8 5 .
$$

We thus conclude that the $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ Lagrange points are stable equilibrium points, in the co-rotating frame, provided that mass $\mathfrak { m } _ { 2 }$ is less than about $4 \%$ of $\mathfrak { m a s s } \ \mathfrak { m } _ { 1 }$ . If this is the case then mass $\mathfrak { m } _ { 3 }$ can orbit around these points indefinitely. In the inertial frame, the mass will share the orbit of mass $\mathfrak { m } _ { 2 }$ about mass $\mathfrak { m } _ { 1 }$ , but will stay approximately $6 0 ^ { \circ }$ ahead of mass $\mathfrak { m } _ { 2 }$ , if it is orbiting the $\mathrm { L } _ { 4 }$ point, or $6 0 ^ { \circ }$ behind, if it is orbiting the $\mathrm { L } _ { 5 }$ point—see Figure 9.9. This type of behavior has been observed in the Solar System. For instance, there is a sub-class of asteroids, known as the Trojan asteroids, which are trapped in the vicinity of the $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ points of the Sun-Jupiter system [which easily satisfies the stability criterion (9.89)], and consequently share Jupiter’s orbit around the Sun, staying approximately $6 0 ^ { \circ }$ ahead of, and $6 0 ^ { \circ }$ behind, Jupiter, respectively. Furthermore, the $\mathrm { L } _ { 4 }$ and $\mathrm { L } _ { 5 }$ points of the Sun-Earth system are occupied by clouds of dust.

# 10 Lunar Motion

# 10.1 Historical Background

The motion of the Planets around the Sun is fairly accurately described by Kepler’s laws (see Chapter 4). Likewise, to a first approximation, the motion of the Moon around the Earth can also be accounted for via these laws. However, unlike the planetary orbits, the deviations of the lunar orbit from a Keplerian ellipse are sufficiently large that they are easily apparent to the naked eye. Indeed, the largest of these deviations, which is generally known as evection, was discovered in ancient times by the Alexandrian astronomer Claudius Ptolemy (90–168 AD). Moreover, the next largest deviation, which is called variation, was first observed by Tycho Brahe (1546–1601) without the aid of a telescope. Another non-Keplerian feature of the lunar orbit, which is sufficient obvious that it was known to the ancient Greeks, is the fact that the lunar perigee (i.e., the point of closest approach to the Earth) precesses (i.e., orbits about the Earth in the same direction as the Moon) at such a rate that it completes a full circuit every 8.85 years.1 The ancient Greeks also noticed that the lunar ascending node (i.e., the point at which the Moon passes through the fixed plane of the Earth’s orbit around the Sun from south to north) regresses (i.e., orbits about the Earth in the opposite direction to the Moon) at such a rate that it completes a full circuit every 18.6 years. Of course, according to standard two-body orbit theory, both the lunar perigee and ascending node should be stationary (see Chapter 4).

Newton demonstrated, in Book III of his Principia, that the deviations of the lunar orbit from a Keplerian ellipse are due to the gravitational influence of the Sun, which is sufficiently large that it is not completely negligible compared with the mutual gravitational attraction of the Earth and the Moon. However, Newton was not able to give a complete account of these deviations, due to the complexity of the equations of motion which arise in a system of three mutually gravitating bodies (see Chapter 9). In fact, Clairaut (1713– 1765) is generally credited with the first reasonably accurate and complete theoretical explanation of the Moon’s orbit. His method of calculation made use of an expansion of the lunar equations of motion in terms of various small parameters. Clairaut, however, initially experienced difficulty in accounting for the precession of the lunar perigee. Indeed, his first calculation overestimated the period of this precession by a factor of about two, leading him to question Newton’s inverse-square law of gravitation. Later on, he realized that he could indeed account for the precession, in terms of standard Newtonian dynamics, by continuing his expansion in small parameters to higher order. After Clairaut, the theory of lunar motion was further elaborated in major works by D’Alembert (1717–1783), Euler (1707–1783), Laplace (1749–1827), Damoiseau (1768–1846), Plana (1781–1864), Poisson (1781–1840), Hansen (1795–1874), De Pont´ecoulant (1795–1824),

J. Herschel (1792–1871), Airy (1801–1892), Delaunay (1816–1872), G.W. Hill (1836– 1914), and E.W. Brown (1836–1938). The fact that so many celebrated mathematicians and astronomers devoted so much time and effort to lunar theory is a tribute to its inherent difficulty, as well as its great theoretical and practical interest. Indeed, for a period of about one hundred years (between 1767 and about 1850) the so-called method of lunar distance was the principal means used by mariners to determine longitude at sea. This method depends crucially on a precise knowledge of the position of the Moon in the sky as a function of time. Consequently, astronomers and mathematicians during the period in question were spurred to make ever more accurate observations of the Moon’s orbit, and to develop lunar theory to greater and greater precision. An important outcome of these activities were various tables of lunar motion (e.g., those of Mayer, Damoiseau, Plana, Hansen, and Brown), most of which were published at public expense.

This chapter contains an introduction to lunar theory in which approximate expressions for evection, variation, the precession of the perigee, and the regression of the ascending node, are derived from the laws of Newtonian mechanics.

# 10.2 Preliminary Analysis

Let $\pmb { \mathrm { r } } _ { \mathsf { E } }$ and $\mathbf { r } _ { M }$ be the position vectors of the Earth and Moon, respectively, in a non-rotating reference frame in which the Sun is at rest at the origin. Treating this reference frame as inertial (which is an excellent approximation, given that the mass of the Sun is very much greater than that of the Earth or the Moon), the Earth’s equation of motion becomes (see Chapter 4)

$$
\ddot { \mathbf { r } } _ { \mathrm { E } } = - { \boldsymbol { \mathrm { n } } } ^ { \prime } { } ^ { 2 } { \boldsymbol { \mathrm { a } } } ^ { \prime } { } ^ { 3 } \frac { \mathbf { r } _ { \mathrm { E } } } { | \mathbf { r } _ { \mathrm { E } } | ^ { 3 } } ,
$$

where $\mathfrak { n } ^ { \prime } = 0 . 9 8 5 6 0 0 2 5 ^ { \circ }$ per day and $\mathbf { a } ^ { \prime } = 1 4 9 , 5 9 8 , 2 6 1 \mathrm { k m }$ are the mean angular velocity and major radius, respectively, of the terrestrial orbit about the Sun. Here, $\ddot { \bf \Phi } \equiv \mathrm { d } ^ { 2 } / \mathrm { d t } ^ { 2 }$ . On the other hand, the Moon’s equation of motion takes the form

$$
\ddot { \mathbf { r } } _ { M } = - \mathsf { n } ^ { 2 } \mathbf { a } ^ { 3 } \frac { ( \mathbf { r } _ { M } - \mathbf { r } _ { \mathrm { E } } ) } { | \mathbf { r } _ { M } - \mathbf { r } _ { \mathrm { E } } | ^ { 3 } } - \mathsf { n } ^ { \prime 2 } \mathbf { a } ^ { \prime 3 } \frac { \mathbf { r } _ { M } } { | \mathbf { r } _ { M } | ^ { 3 } } ,
$$

where $n = 1 3 . 1 7 6 3 9 6 4 6 ^ { \circ }$ per day and $\mathbf { a } = 3 8 4 , 3 9 9 \mathrm { k m }$ are the mean angular velocity and major radius, respectively, of the lunar orbit about the Earth. Note that we have retained the acceleration due to the Earth in the lunar equation of motion, (10.2), whilst neglecting the acceleration due to the Moon in the terrestrial equation of motion, (10.1), since the former acceleration is significantly greater (by a factor $M _ { \mathrm { E } } / M _ { M } \simeq 8 1$ , where $M _ { \mathrm { E } }$ is the mass of the Earth, and $M _ { M }$ the mass of the Moon) than the latter.

Let

$$
\begin{array} { r c l } { { { \bf r } } } & { { = } } & { { { \bf r } _ { \mathrm { M } } - { \bf r } _ { \mathrm { E } } , } } \\ { { } } & { { } } & { { } } \\ { { { \bf r } ^ { \prime } } } & { { = } } & { { - { \bf r } _ { \mathrm { E } } , } } \end{array}
$$

be the position vectors of the Moon and Sun, respectively, relative to the Earth. It follows, from Equations (10.1)–(10.4), that in a non-inertial reference frame, S (say), in which the Earth is at rest at the origin, but the coordinate axes point in fixed directions, the lunar and solar equations of motion take the form

$$
\begin{array} { r l r } { \ddot { \bf r } } & { = } & { - \mathrm { \ n } ^ { 2 } \mathrm { \bf ~ a } ^ { 3 } \frac { \mathrm { \bf ~ r } } { | \mathrm { \bf ~ r } | ^ { 3 } } + \mathrm { \bf ~ n } ^ { \prime 2 } \mathrm { \bf ~ a } ^ { \prime 3 } \left[ \frac { ( \mathrm { \bf ~ r } ^ { \prime } - \mathrm { \bf ~ r } ) } { | \mathrm { \bf ~ r } ^ { \prime } - \mathrm { \bf ~ r } | ^ { 3 } } - \frac { \mathrm { \bf ~ r } ^ { \prime } } { | \mathrm { \bf ~ r } ^ { \prime } | ^ { 3 } } \right] , } \\ & { \ddot { \bf r } ^ { \prime } } & { = } & { - \mathrm { \bf ~ n } ^ { \prime 2 } \mathrm { \bf ~ a } ^ { \prime 3 } \frac { \mathrm { \bf ~ r } ^ { \prime } } { | \mathrm { \bf ~ r } ^ { \prime } | ^ { 3 } } , } \end{array}
$$

respectively.

Let us set up a conventional Cartesian coordinate system in S which is such that the (apparent) orbit of the Sun about the Earth lies in the $x { - } y$ plane. This implies that the $x { - } y$ plane corresponds to the so-called ecliptic plane. Accordingly, in S, the Sun appears to orbit the Earth at the mean angular velocity ${ \bf { \omega } } \omega ^ { \prime } = { \bf { n } } ^ { \prime } { \bf e } _ { z }$ (assuming that the $z$ -axis points toward the so-called north ecliptic pole), whereas the projection of the Moon onto the ecliptic plane orbits the Earth at the mean angular velocity $\ \omega = \mathfrak { n } \mathbf { e } _ { z }$ .

In the following, for the sake of simplicity, we shall neglect the small eccentricity, $e ^ { \prime } =$ 0.016711, of the Sun’s apparent orbit about the Earth (which is actually the eccentricity of the Earth’s orbit about the Sun), and approximate the solar orbit as a circle, centered on the Earth. Thus, if $\ x ^ { \prime } , \ y ^ { \prime } ,$ $z ^ { \prime }$ are the Cartesian coordinates of the Sun in S then an appropriate solution of the solar equation of motion, (10.6), is

$$
{ \begin{array} { r c l } { x ^ { \prime } } & { = } & { \mathbf { a } ^ { \prime } \cos ( \mathbf { n } ^ { \prime } \mathbf { t } ) , } \\ { \mathbf { y } ^ { \prime } } & { = } & { \mathbf { a } ^ { \prime } \sin ( \mathbf { n } ^ { \prime } \mathbf { t } ) , } \\ { z ^ { \prime } } & { = } & { 0 . } \end{array} }
$$

# 10.3 Lunar Equations of Motion

It is convenient to solve the lunar equation of motion, (10.5), in a geocentric frame of reference, $S _ { 1 }$ (say), which rotates with respect to S at the fixed angular velocity ω. Thus, if the lunar orbit were a circle, centered on the Earth, and lying in the ecliptic plane, then the Moon would appear stationary in $S _ { 1 }$ . In fact, the small eccentricity of the lunar orbit, $e = 0 . 0 5 4 8 8$ , combined with its slight inclination to the ecliptic plane, $\mathsf { \iota } = 5 . 1 6 1 ^ { \circ }$ , causes the Moon to execute a small periodic orbit about the stationary point.

Let x, y, $z$ and $x _ { 1 } , y _ { 1 } , z _ { 1 }$ be the Cartesian coordinates of the Moon in S and $S _ { 1 }$ , respectively. It is easily demonstrated that (see Section A.16)

$$
\begin{array} { r c l } { x } & { = } & { x _ { 1 } \cos ( \mathrm { n t } ) - y _ { 1 } \sin ( \mathrm { n t } ) , } \\ { \nmid } & { = } & { x _ { 1 } \sin ( \mathrm { n t } ) + y _ { 1 } \cos ( \mathrm { n t } ) , } \\ { z } & { = } & { z _ { 1 } . } \end{array}
$$

Moreover, if $x _ { 1 } ^ { \prime } , y _ { 1 } ^ { \prime } , z _ { 1 } ^ { \prime }$ are the Cartesian components of the Sun in $S _ { 1 }$ then (see Section A.5)

$$
\begin{array} { r c l } { { x _ { 1 } ^ { \prime } } } & { { = } } & { { x ^ { \prime } \cos ( \mathrm { n t } ) + y ^ { \prime } \sin ( \mathrm { n t } ) , } } \\ { { } } & { { } } & { { } } \\ { { y _ { 1 } ^ { \prime } } } & { { = } } & { { - x ^ { \prime } \sin ( \mathrm { n t } ) + y ^ { \prime } \cos ( \mathrm { n t } ) , } } \\ { { } } & { { } } & { { } } \\ { { z _ { 1 } ^ { \prime } } } & { { = } } & { { z ^ { \prime } , } } \end{array}
$$

giving

$$
\begin{array} { r c l } { { \displaystyle x _ { 1 } ^ { \prime } } } & { { = } } & { { \bf a ^ { \prime } \cos [ ( n - n ^ { \prime } ) t ] , } } \\ { { \displaystyle y _ { 1 } ^ { \prime } } } & { { = } } & { { - \bf a ^ { \prime } \sin [ ( n - n ^ { \prime } ) t ] , } } \\ { { \displaystyle z _ { 1 } ^ { \prime } } } & { { = } } & { { 0 , } } \end{array}
$$

where use has been made of Equations (10.7)–(10.9).

Now, in the rotating frame $S _ { 1 }$ , the lunar equation of motion (10.5) transforms to (see Section 6.2)

$$
\ddot { \mathbf { r } } + 2 \boldsymbol { \omega } \times \dot { \mathbf { r } } + \boldsymbol { \omega } \times ( \mathbf { \omega } \times \mathbf { r } ) = - \mathrm { n } ^ { 2 } \mathrm { a } ^ { 3 } \frac { \mathbf { r } } { | \mathbf { r } | ^ { 3 } } + \mathrm { n } ^ { \prime 2 } \mathrm { a } ^ { \prime 3 } \left[ \frac { ( \mathbf { r } ^ { \prime } - \mathbf { r } ) } { | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { 3 } } - \frac { \mathbf { r } ^ { \prime } } { | \mathbf { r } ^ { \prime } | ^ { 3 } } \right] ,
$$

where $\mathbf { \bar { \rho } } \equiv \mathrm { d } / \mathrm { d } \mathrm { t }$ . Furthermore, expanding the final term on the right-hand side of (10.19) to lowest order in the small parameter $\mathbf { a } / \mathbf { a } ^ { \prime } = 0 . 0 0 2 5 7$ , we obtain

$$
\ddot { \mathbf { r } } + 2 \boldsymbol { \omega } \times \dot { \mathbf { r } } + \boldsymbol { \omega } \times ( \boldsymbol { \omega } \times \mathbf { r } ) \simeq - \mathrm { n } ^ { 2 } \mathrm { a } ^ { 3 } \frac { \mathbf { r } } { | \mathbf { r } | ^ { 3 } } + \frac { \mathrm { n } ^ { \prime 2 } \mathrm { a } ^ { \prime 3 } } { | \mathbf { r } ^ { \prime } | ^ { 3 } } \left[ \frac { ( 3 \mathbf { r } \cdot \mathbf { r } ^ { \prime } ) \mathbf { r } ^ { \prime } } { | \mathbf { r } ^ { \prime } | ^ { 2 } } - \mathbf { r } \right] .
$$

When written in terms of Cartesian coordinates, the above equation yields

$$
\begin{array} { r c l } { \displaystyle \ddot { x } _ { 1 } - 2 { \bf n } \dot { \bf y } _ { 1 } - \left( { \bf n } ^ { 2 } + { \bf n } ^ { \prime 2 } / 2 \right) x _ { 1 } } & { \simeq } & { - { \bf n } ^ { 2 } { \bf a } ^ { 3 } \frac { x _ { 1 } } { \bf r } ^ { 3 } + \frac { 3 } { 2 } { \bf n } ^ { \prime 2 } \cos [ 2 \left( { \bf n } - { \bf n } ^ { \prime } \right) { \bf t } ] x _ { 1 } } \\ & & & { - \frac { 3 } { 2 } { \bf n } ^ { \prime 2 } \sin [ 2 \left( \left( { \bf n } - { \bf n } ^ { \prime } \right) { \bf t } \right] y _ { 1 } , } \\ & & & { \ddot { y } _ { 1 } + 2 { \bf n } \dot { x } _ { 1 } - \left( { \bf n } ^ { 2 } + { \bf n } ^ { \prime 2 } / 2 \right) y _ { 1 } } & { \simeq } & { - { \bf n } ^ { 2 } { \bf a } ^ { 3 } \frac { y _ { 1 } } { \bf r } ^ { 3 } - \frac { 3 } { 2 } { \bf n } ^ { \prime 2 } \sin [ 2 \left( { \bf n } - { \bf n } ^ { \prime } \right) { \bf t } ] x _ { 1 } } \\ & & & { - \frac { 3 } { 2 } { \bf n } ^ { \prime 2 } \cos [ 2 \left( { \bf n } - { \bf n } ^ { \prime } \right) { \bf t } ] y _ { 1 } , } \\ { \displaystyle \ddot { z } _ { 1 } + { \bf n } ^ { \prime 2 } z _ { 1 } } & { \simeq } & { - { \bf n } ^ { 2 } { \bf a } ^ { 3 } \frac { z _ { 1 } } { \bf r } ^ { 3 } , } \end{array}
$$

where $\mathfrak { r } = ( \mathfrak { x } _ { 1 } ^ { 2 } + \mathfrak { y } _ { 1 } ^ { 2 } + z _ { 1 } ^ { 2 } ) ^ { 1 / 2 }$ , and use has been made of Equations (10.16)–(10.18).

It is convenient, at this stage, to normalize all lengths to $\mathbf { a }$ , and all times to $\mathfrak { n } ^ { - 1 }$ . Accordingly, let

$$
\begin{array} { r } { \begin{array} { r c l } { \textsf { X } } & { = } & { x _ { 1 } / \mathbf { a } , } \\ { } & { } & { } \\ { \textsf { Y } } & { = } & { y _ { 1 } / \mathbf { a } , } \\ { } & { } & { } \\ { Z } & { = } & { z _ { 1 } / \mathbf { a } , } \end{array} } \end{array}
$$

and $\boldsymbol { \mathrm { r } } / \boldsymbol { \mathrm { a } } = \boldsymbol { \mathrm { R } } = ( X ^ { 2 } + \mathsf { Y } ^ { 2 } + Z ^ { 2 } ) ^ { 1 / 2 }$ , and ${ \mathsf { T } } = { \mathsf { n t } }$ . In normalized form, Equations (10.21)– (10.23) become

$$
\begin{array} { r c l } { \displaystyle \ddot { X } - 2 \dot { Y } - ( 1 + \mathfrak { m } ^ { 2 } / 2 ) X } & { \simeq } & { \displaystyle - \frac { X } { \mathbb { R } ^ { 3 } } + \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \Pi ] X } \\ & & { } & { \displaystyle - \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \sin [ 2 \left( 1 - \mathfrak { m } \right) \Pi ] Y , } \\ { \displaystyle \ddot { Y } + 2 \dot { X } - ( 1 + \mathfrak { m } ^ { 2 } / 2 ) Y } & { \simeq } & { \displaystyle - \frac { Y } { \mathbb { R } ^ { 3 } } - \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \sin [ 2 \left( 1 - \mathfrak { m } \right) \Pi ] X } \\ & & { } & { \displaystyle - \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \Pi ] Y , } \\ { \displaystyle \ddot { Z } + \mathfrak { m } ^ { 2 } Z } & { \simeq } & { \displaystyle - \frac { Z } { \mathbb { R } ^ { 3 } } , } \end{array}
$$

respectively, where $\mathfrak { m } = \mathfrak { n } ^ { \prime } / \mathfrak { n } = 0 . 0 7 4 8 0$ is a measure of the perturbing influence of the Sun on the lunar orbit. Here, $\ddot { \mathbf { \Omega } } \equiv \mathsf { d } ^ { 2 } / \mathsf { d } \mathsf { T } ^ { 2 }$ and $\mathbf { \dot { \eta } } \equiv \mathbf { d } / \mathbf { d } \mathsf { T }$ .

Finally, let us write

$$
\begin{array} { r c l } { { \sf X } } & { { = } } & { { \sf X } _ { 0 } + \delta { \sf X } , } \\ { { \sf Y } } & { { = } } & { { \delta \sf Y } , } \\ { { \sf Z } } & { { = } } & { { \delta \sf Z } , } \end{array}
$$

where $X _ { 0 } ~ = ~ ( 1 + \mathsf { m } ^ { 2 } / 2 ) ^ { - 1 / 3 }$ , and $\lvert \delta \boldsymbol { \mathrm { X } } \rvert , \lvert \delta \boldsymbol { \mathrm { Y } } \rvert , \lvert \delta \boldsymbol { \mathrm { Z } } \rvert \ll \boldsymbol { \mathrm { X } } _ { 0 }$ . Thus, if the lunar orbit were a circle, centered on the Earth, and lying in the ecliptic plane, then, in the rotating frame $S _ { 1 }$ , the Moon would appear stationary at the point $( \mathsf { X } _ { 0 } , 0 , 0 )$ . Expanding Equations (10.27)– (10.29) to second-order in δX, δY, δZ, and neglecting terms of order $\mathfrak { m } ^ { 4 }$ and $\mathrm { m } ^ { 2 } \delta X ^ { 2 }$ , etc., we obtain

$$
\begin{array} { r l r } { 2 \delta \dot { \mathsf { Y } } - 3 \left( 1 + \mathfrak { m } ^ { 2 } / 2 \right) \delta \mathsf { X } } & { \simeq } & { \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \mathsf { T } ] + \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \mathsf { T } ] \delta \mathsf { X } } \\ & { } & { - \frac { 3 } { 2 } \mathfrak { m } ^ { 2 } \sin [ 2 \left( 1 - \mathfrak { m } \right) \mathsf { T } ] \delta \mathsf { Y } - 3 \delta \mathsf { X } ^ { 2 } + \frac { 3 } { 2 } \left( \delta \mathsf { Y } ^ { 2 } + \delta \mathsf { Z } ^ { 2 } + \pi \mathsf { T } \right) \mathsf { X } \delta \mathsf { X } } \end{array}
$$

$$
\begin{array} { r c l } { { \delta \ddot { \Upsilon } + 2 \delta \dot { X } ~ \simeq } } & { { - \displaystyle { \frac { 3 } { 2 } } \mathfrak { m } ^ { 2 } \sin [ 2 \left( 1 - \mathfrak { m } \right) \Pi - \displaystyle { \frac { 3 } { 2 } } \mathfrak { m } ^ { 2 } \sin [ 2 \left( 1 - \mathfrak { m } \right) \Pi \delta { \^ { \underline { { { X } } } } } ] } } \\ { { } } & { { - \displaystyle { \frac { 3 } { 2 } } \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \Pi \delta { \^ { } } + 3 \delta { \^ { } } \delta { \^ { \underline { { { X } } } } } ] } } & { { ( 1 \delta \mathfrak { m } ^ { 2 } ) } } \\ { { \delta \ddot { Z } + \left( 1 + 3 \mathfrak { m } ^ { 2 } / 2 \right) \delta { \ Z } } } & { { \simeq } } & { { 3 \delta { \^ { } } \delta { \ Z } . } } & { { ( 1 \delta \mathcal { Z } ) } } \\ { { } } & { { } } & { { } } & { { } } \end{array}
$$

Now, once the above three equations have been solved for δX, δY, and δZ, the Cartesian coordinates, $x , y , z ,$ , of the Moon in the non-rotating geocentric frame S are obtained from Equations (10.10)–(10.12), (10.24)–(10.26), and (10.30)–(10.32). However, it is more convenient to write $x = \mathrm { r }$ cos θ, ${ \mathfrak { y } } = { \mathfrak { r } }$ sin θ, and $z = \mathrm { r }$ sin $\beta$ , where $\boldsymbol { \mathsf { r } }$ is the radial distance between the Earth and Moon, and θ and $\beta$ are termed the Moon’s geocentric (i.e., centered on the Earth) ecliptic longitude and ecliptic latitude, respectively. Moreover, it is easily seen that, to second-order in δX, δY, δZ, and neglecting terms of order $\mathfrak { m } ^ { 4 }$ ,

$$
\begin{array} { r c l } { { \displaystyle { \frac { \Upsilon } { \alpha } } - 1 + \frac { \mathfrak { m } ^ { 2 } } { 6 } } } & { { \simeq } } & { { \displaystyle { \delta \Upsilon + \frac { 1 } { 2 } \delta \Upsilon ^ { 2 } + \frac { 1 } { 2 } \delta Z ^ { 2 } } , } } \\ { { \displaystyle { \theta - \mathfrak { n } \mathfrak { t } } } } & { { \simeq } } & { { \displaystyle { \delta \Upsilon - \delta \Upsilon \delta \Upsilon , } } } \\ { { \displaystyle { \beta } } } & { { \simeq } } & { { \displaystyle { \delta Z - \delta \Upsilon \delta \mathrm { Z } . } } } \end{array}
$$

# 10.4 Unperturbed Lunar Motion

Let us, first of all, neglect the perturbing influence of the Sun on the Moon’s orbit by setting $\mathfrak { m } = 0$ in the lunar equations of motion (10.33)–(10.35). For the sake of simplicity, let us also neglect nonlinear effects in these equations by setting $\delta { \sf X } ^ { 2 } = \delta { \sf Y } ^ { 2 } = \delta { \sf Z } ^ { 2 } = \delta { \sf X } \delta { \sf Y } =$ $\delta { \sf X } \delta Z = 0$ . In this case, the equations reduce to

$$
\begin{array} { r l r } { \delta \ddot { X } - 2 \delta \dot { \mathsf { Y } } - 3 \delta { X } } & { \simeq } & { 0 , } \\ { \delta \ddot { \mathsf { Y } } + 2 \delta \dot { \mathsf { X } } } & { \simeq } & { 0 , } \\ { \delta \ddot { Z } + \delta { Z } } & { \simeq } & { 0 . } \end{array}
$$

By inspection, appropriate solutions are

$$
\begin{array} { r c l } { { \delta { \sf X } } } & { { \simeq } } & { { - e \cos ( { \sf T } - \alpha _ { 0 } ) , } } \\ { { } } & { { } } & { { } } \\ { { \delta { \sf Y } } } & { { \simeq } } & { { 2 e \sin ( { \sf T } - \alpha _ { 0 } ) , } } \\ { { } } & { { } } & { { \delta { \sf Z } \simeq \mathrm { ~ i ~ } \sin ( { \sf T } - \gamma _ { 0 } ) , } } \end{array}
$$

where $e$ , $\alpha _ { 0 }$ , i, and $\gamma _ { 0 }$ are arbitrary constants. Recalling that ${ \mathsf { T } } = { \mathsf { n t } }$ , it follows from (10.36)–(10.38) that

$$
\begin{array} { r c l } { { \mathrm {  ~ r ~ } } } & { { \simeq } } & { { { \bf a } \left[ 1 - e \cos ( n { \sf t } - \alpha _ { 0 } ) \right] , } } \\ { { \mathrm {  ~ \theta ~ } } } & { { \simeq } } & { { { \bf n } { \sf t } + 2 e \sin ( n { \sf t } - \alpha _ { 0 } ) , } } \\ { { \mathrm {  ~ \beta ~ } } } & { { \simeq } } & { { \mathrm {  ~ \iota ~ } \sin ( n { \sf t } - \gamma _ { 0 } ) . } } \end{array}
$$

However, Equations (10.45) and (10.46) are simply first-order $( \mathrm { i n } ~ e )$ approximations to the familiar Keplerian laws (see Chapter 4)

$$
\begin{array} { r c l } { { \mathrm { r } } } & { { = } } & { { \displaystyle \frac { \mathrm {  ~ a ~ } ( 1 - e ^ { 2 } ) } { 1 + e \cos ( \mathrm {  ~ \theta ~ } - \alpha _ { 0 } ) } , } } \\ { { \mathrm { r } ^ { 2 } \dot { \Theta } } } & { { = } } & { { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } { \mathrm { n a } } ^ { 2 } , } } \end{array}
$$

where $\mathbf { \dot { \mathbf { \rho } } } \equiv \mathbf { d } / \mathbf { d t }$ . Of course, the above two laws describe a body which executes an elliptical orbit, confocal with the Earth, of major radius a, mean angular velocity $\mathfrak { n }$ , and eccentricity e, such that the radius vector connecting the body to the Earth sweeps out equal areas in equal time intervals. We conclude, unsurprisingly, that the unperturbed lunar orbit is a Keplerian ellipse. Note that the lunar perigee lies at the fixed ecliptic longitude $\theta = \alpha _ { 0 }$ . Equation (10.47) is the first-order approximation to

$$
\beta = \iota \sin ( \theta - \gamma _ { 0 } ) .
$$

This expression implies that the unperturbed lunar orbit is co-planar, but is inclined at an angle ι to the ecliptic plane. Moreover, the ascending node lies at the fixed ecliptic longitude $\theta = \gamma _ { 0 }$ . Incidentally, the neglect of nonlinear terms in Equations (10.39)–(10.41) is only valid as long as e, $\mathfrak { L } \ll 1$ : i.e., provided that the unperturbed lunar orbit is only slightly elliptical, and slightly inclined to the ecliptic plane. In fact, the observed values of e and ι are 0.05488 and 0.09008 radians, respectively, so this is indeed the case.

# 10.5 Perturbed Lunar Motion

The perturbed nonlinear lunar equations of motion, (10.33)–(10.35), take the general form

$$
\begin{array} { r l r } { \delta \ddot { X } - 2 \delta \dot { Y } - 3 ( 1 + \mathfrak { m } ^ { 2 } / 2 ) \delta X } & { \simeq } & { \mathsf { R } _ { X } , } \\ { \delta \ddot { \mathsf { Y } } + 2 \delta \dot { X } } & { \simeq } & { \mathsf { R } _ { \mathsf { Y } } , } \\ { \delta \ddot { Z } + ( 1 + 3 \mathsf { m } ^ { 2 } / 2 ) \delta Z } & { \simeq } & { \mathsf { R } _ { Z } , } \end{array}
$$

where

$$
\begin{array} { r c l } { { \displaystyle { \sf R } _ { X } } } & { { = } } & { { \displaystyle { \bf a } _ { 0 } + \sum _ { \mathrm { j } > 0 } { \bf a } _ { \mathrm { j } } \cos ( { \bf \omega } _ { 0 } \mathrm { T } - { \bf \alpha } _ { \mathrm { N } } ) , } } \\ { { } } & { { } } & { { } } \\ { { { \sf R } _ { Y } } } & { { = } } & { { \displaystyle \sum _ { \mathrm { j } > 0 } { \bf b } _ { \mathrm { j } } \sin ( { \bf \omega } _ { 0 } \mathrm { T } - { \bf \alpha } _ { \mathrm { N } } ) , } } \\ { { } } & { { } } & { { } } \\ { { { \sf R } _ { Z } } } & { { = } } & { { \displaystyle \sum _ { \mathrm { j } > 0 } { c } _ { \mathrm { j } } \sin ( { \Omega } _ { \mathrm { j } } \mathrm { T } - \gamma _ { \mathrm { j } } ) . } } \end{array}
$$

Let us search for solutions of the general form

$$
\begin{array} { r c l } { { \delta { \sf X } } } & { { = } } & { { \displaystyle { x _ { 0 } + \sum _ { j > 0 } x _ { j } \cos ( \omega _ { j } { \sf T } - \alpha _ { j } ) } , } } \\ { { } } & { { } } & { { } } \\ { { \delta { \sf Y } } } & { { = } } & { { \displaystyle { \sum _ { j > 0 } y _ { j } \sin ( \omega _ { j } { \sf T } - \alpha _ { j } ) } , } } \\ { { } } & { { } } & { { } } \\ { { \delta { \sf Z } } } & { { = } } & { { \displaystyle { \sum _ { j > 0 } z _ { j } \sin ( \Omega _ { j } { \sf T } - \gamma _ { j } ) } . } } \end{array}
$$

<table><tr><td>j</td><td>Wj</td><td>双j</td><td>0j</td><td>Yi</td></tr><tr><td>1</td><td>1+c m²</td><td>8</td><td>1+gm²</td><td>Y0</td></tr><tr><td>2</td><td>2(1+cm²)</td><td>2α0</td><td>(c-g) m²</td><td>α-Yo</td></tr><tr><td>3</td><td>2(1+ g m²)</td><td>2Y0</td><td>2+(c+g)m²</td><td>α+Yo</td></tr><tr><td>4</td><td>2-2m</td><td>0</td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td>1-2m-cm² -α 1-2m-gm²</td><td>1Y0</td></tr></table>

Table 10.1: Angular frequencies and phase-shifts associated with the principal periodic driving terms appearing in the perturbed nonlinear lunar equations of motion.

Substituting expressions (10.54)–(10.59) into Equations (10.51)–(10.53), it is easily demonstrated that

$$
\begin{array} { r c l } { { \mathrm { x } _ { 0 } } } & { { = } } & { { - \displaystyle \frac { \mathrm { a } _ { 0 } } { 3 \left( 1 + \mathrm { m } ^ { 2 } / 2 \right) } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { x } _ { j } } } & { { = } } & { { \displaystyle \frac { \omega _ { j } \mathrm { a } _ { j } - 2 \mathrm { b } _ { j } } { \omega _ { j } \left( 1 - 3 \mathrm { m } ^ { 2 } / 2 - \omega _ { j } ^ { 2 } \right) } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { y } _ { j } } } & { { = } } & { { \displaystyle \frac { \left( \omega _ { j } ^ { 2 } + 3 + 3 \mathrm { m } ^ { 2 } / 2 \right) \mathrm { b } _ { j } - 2 \omega _ { j } \mathrm { a } _ { j } } { \omega _ { j } ^ { 2 } \left( 1 - 3 \mathrm { m } ^ { 2 } / 2 - \omega _ { j } ^ { 2 } \right) } , } } \\ { { } } & { { } } & { { } } \\ { { z _ { j } } } & { { = } } & { { \displaystyle \frac { c _ { j } } { 1 + 3 \mathrm { m } ^ { 2 } / 2 - \Omega _ { j } ^ { 2 } } , } } \end{array}
$$

where $\mathrm { j } > 0$

The angular frequencies, $\omega _ { \mathrm { j } } , \Omega _ { \mathrm { j } }$ , and phase shifts, $\alpha _ { \mathrm { j } } , \gamma _ { \mathrm { j } }$ , of the principal periodic driving terms that appear on the right-hand sides of the perturbed nonlinear lunar equations of motion, (10.51)–(10.53), are specified in Table 10.1. Here, c and $^ { 9 }$ are, as yet, unspecified $\mathcal { O } ( 1 )$ constants associated with the precession of the lunar perigee, and the regression of the ascending node, respectively. Note that $\omega _ { 1 }$ and $\Omega _ { 1 }$ are the frequencies of the Moon’s unforced motion in ecliptic longitude and latitude, respectively. Moreover, $\omega _ { 4 }$ is the forcing frequency associated with the perturbing influence of the Sun. All other frequencies appearing in Table 10.1 are combinations of these three fundamental frequencies. In fact, $\omega _ { 2 } = 2 \omega _ { 1 }$ , $\omega _ { 3 } = 2 \Omega _ { 1 }$ , $\omega _ { 5 } = \omega _ { 4 } - \omega _ { 1 }$ , $\Omega _ { 2 } = \omega _ { 1 } - \Omega _ { 1 }$ , $\Omega _ { 3 } = \omega _ { 1 } + \Omega _ { 1 }$ , and $\Omega _ { 5 } = \omega _ { 4 } - \Omega _ { 1 }$ . Note that there is no $\Omega _ { 4 }$ .

Now, a comparison of Equations (10.33)–(10.35), (10.51)–(10.53), and Table 10.1 reveals that

$$
\begin{array} { l l l } { { \displaystyle { \mathbb { R } _ { X } } } } & { { = } } & { { \displaystyle { \frac { 3 } { 2 } } \operatorname { m } ^ { 2 } \cos ( \omega _ { 4 } { \sf T } - \alpha _ { 4 } ) + \frac { 3 } { 2 } \operatorname { m } ^ { 2 } \cos ( \omega _ { 4 } { \sf T } - \alpha _ { 4 } ) \delta { \sf X } } } \\ { { } } & { { } } & { { \displaystyle - \frac { 3 } { 2 } \operatorname { m } ^ { 2 } \sin ( \omega _ { 4 } { \sf T } - \alpha _ { 4 } ) \delta { \sf Y } - 3 \delta { \sf X } ^ { 2 } + \frac { 3 } { 2 } \left( \delta { \sf Y } ^ { 2 } + \delta { \sf Z } ^ { 2 } \right) , } } \\ { { \displaystyle { \mathbb { R } _ { Y } } } } & { { = } } & { { \displaystyle - \frac { 3 } { 2 } \operatorname { m } ^ { 2 } \sin ( \omega _ { 4 } { \sf T } - \alpha _ { 4 } ) - \frac { 3 } { 2 } \operatorname { m } ^ { 2 } \sin ( \omega _ { 4 } { \sf T } - \alpha _ { 4 } ) \delta { \sf X } } } \end{array}
$$


<!-- chunk 0003: pages 141-210 -->
<table><tr><td>j</td><td>aj</td><td>b;</td><td>Cj</td></tr><tr><td>0</td><td colspan="3">2e²+2</td></tr><tr><td>1</td><td>m²x5-³m²ys-3x4x5+2y4y5-m²x5+³m²ys+y4x5- 4</td><td>y5X4</td><td>3-23-2 X4Z5</td></tr><tr><td>2</td><td>9 e²</td><td>-3e²</td><td>e</td></tr><tr><td>3</td><td>3 2</td><td>0</td><td>el</td></tr><tr><td>4</td><td>3 m²</td><td>-2m</td><td>0</td></tr><tr><td>5</td><td>-m²e+3ex4+3ey4</td><td>m²e-3ex4-2ey4</td><td>-x4</td></tr></table>

Table 10.2: Amplitudes of the periodic driving terms appearing in the perturbed nonlinear lunar equations of motion.

$$
\begin{array} { c c l } { { } } & { { } } & { { - \displaystyle \frac { 3 } { 2 } \mathrm { m } ^ { 2 } \cos ( \omega _ { 4 } \sf T - \alpha _ { 4 } ) \delta \sf Y + 3 \delta \sf X \delta \sf Y , } } \\ { { } } & { { } } & { { { \sf R } _ { Z } ~ = ~ \ 3 \delta \sf X \delta Z . } } \end{array}
$$

Substitution of the solutions (10.57)–(10.59) into the above equations, followed by a comparison with expressions (10.54)–(10.56), yields the amplitudes ${ \mathfrak { a } } _ { \mathrm { j } } , { \mathfrak { b } } _ { \mathrm { j } }$ , and $\mathrm { c } _ { \mathrm { j } }$ specified in Table 10.2. Note that, in calculating these amplitudes, we have neglected all contributions to the periodic driving terms, appearing in Equations (10.51)–(10.53) which involve cubic, or higher order, combinations of $e , \mathsf { \iota } _ { \mathsf { i } } , \mathsf { m } ^ { 2 } , \mathsf { x } _ { \mathsf { j } } , \mathsf { y } _ { \mathsf { j } }$ , and $z _ { \mathrm { j } }$ , since we only expanded Equations (10.33)–(10.35) to second-order in δX, δY, and $\delta Z$ .

For $\mathrm { j } = 0$ , it follows from Equation (10.60) and Table 10.2 that

$$
x _ { 0 } = - \frac { 1 } { 2 } e ^ { 2 } - \frac { 1 } { 4 } \iota ^ { 2 } .
$$

For ${ \mathrm { j } } = 2$ , making the approximation $\omega _ { 2 } \simeq 2$ (see Table 10.1), it follows from Equations (10.61), (10.62) and Table 10.2 that

$$
\begin{array} { r c l } { { x _ { 2 } } } & { { \simeq } } & { { \displaystyle \frac { 1 } { 2 } e ^ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { y _ { 2 } } } & { { \simeq } } & { { \displaystyle \frac { 1 } { 4 } e ^ { 2 } . } } \end{array}
$$

Likewise, making the approximation $\Omega _ { 2 } \simeq 0$ (see Table 10.1), it follows from Equation (10.63) and Table 10.2 that

$$
z _ { 2 } \simeq \frac { 3 } { 2 } e _ { l } .
$$

For $j = 3$ , making the approximation $\omega _ { 3 } \simeq 2$ (see Table 10.1), it follows from Equations (10.61), (10.62) and Table 10.2 that

$$
\begin{array} { r c l } { { \displaystyle x _ { 3 } } } & { { \simeq } } & { { \displaystyle \frac { 1 } { 4 } \mathfrak { L } ^ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle y _ { 3 } } } & { { \simeq } } & { { \displaystyle - \frac { 1 } { 4 } \mathfrak { L } ^ { 2 } . } } \end{array}
$$

Likewise, making the approximation $\Omega _ { 3 } \simeq 2$ (see Table 10.1), it follows from Equation (10.63) and Table 10.2 that

$$
z _ { 3 } \simeq \frac { 1 } { 2 } e _ { l } .
$$

For $j = 4$ , making the approximation $\omega _ { 4 } \simeq 2$ (see Table 10.1), it follows from Equations (10.61), (10.62) and Table 10.2 that

$$
\begin{array} { r c l } { { \displaystyle x _ { 4 } } } & { { \simeq } } & { { \displaystyle - \mathsf { m } ^ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle y _ { 4 } } } & { { \simeq } } & { { \displaystyle \frac { 1 1 } { 8 } \mathsf { m } ^ { 2 } . } } \end{array}
$$

Thus, according to Table 10.2,

$$
\begin{array} { r c l } { { \mathrm { a } _ { 5 } } } & { { \simeq } } & { { - \displaystyle \frac { 9 } { 8 } \mathrm { m } ^ { 2 } e , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { b } _ { 5 } } } & { { \simeq } } & { { \displaystyle \frac { 5 1 } { 1 6 } \mathrm { m } ^ { 2 } e , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle c _ { 5 } } } & { { \simeq } } & { { \displaystyle \frac { 3 } { 2 } \mathrm { m } ^ { 2 } \iota . } } \end{array}
$$

For $j = 5$ , making the approximation $\omega _ { 5 } \simeq 1 - 2  { \mathrm { m } }$ (see Table 10.1), it follows from Equations (10.61), (10.62), (10.76), and (10.77) that

$$
\begin{array} { r c l } { { \displaystyle x _ { 5 } } } & { { \simeq } } & { { \displaystyle - \frac { 1 5 } { 8 } { \sf m } e , } } \\ { { \displaystyle y _ { 5 } } } & { { \simeq } } & { { \displaystyle \frac { 1 5 } { 4 } { \sf m } e . } } \end{array}
$$

Likewise, making the approximation $\Omega _ { 5 } \simeq 1 - 2  { \mathrm { m } }$ (see Table 10.1), it follows from Equa tions (10.63) and (10.78) that

$$
z _ { 5 } \simeq \frac { 3 } { 8 } \mathfrak { m } \mathfrak { L }
$$

Thus, according to Table 10.2,

$$
\begin{array} { r c l } { { \displaystyle { \bf a } _ { 1 } } } & { { = } } & { { \displaystyle - \frac { 1 3 5 } { 6 4 } { \mathrm m } ^ { 3 } e , } } \\ { { } } & { { } } & { { } } \\ { { { \bf b } _ { 1 } } } & { { = } } & { { \displaystyle \frac { 7 6 5 } { 1 2 8 } { \mathrm m } ^ { 3 } e , } } \\ { { } } & { { } } & { { } } \\ { { { \bf c } _ { 1 } } } & { { = } } & { { \displaystyle \frac { 9 } { 1 6 } { \mathrm m } ^ { 3 } { \mathrm {  t } } . } } \end{array}
$$

Finally, for $j = 1$ , by analogy with Equations (10.42)–(10.44), we expect

$$
\begin{array} { r c l } { { \bf a } _ { 1 } } & { { = } } & { { - e , } } \\ { { } } & { { } } & { { } } \\ { { { \bf b } _ { 1 } } } & { { = } } & { { 2 e , } } \\ { { } } & { { } } & { { } } \\ { { { \bf c } _ { 1 } } } & { { = } } & { { { \bf \epsilon } _ { 1 . } } } \end{array}
$$

Thus, since $\omega _ { 1 } = 1 + \mathtt { c m } ^ { 2 }$ (see Table 10.1), it follows from Equations (10.61), (10.82), (10.83), and (10.85) that

$$
- e \simeq \frac { - ( 2 2 5 / 1 6 ) \mathfrak { m } ^ { 3 } e } { - ( 3 / 2 ) \mathfrak { m } ^ { 2 } - 2 \mathfrak { c } \mathfrak { m } ^ { 2 } } ,
$$

which yields

$$
\mathbf { c } \simeq - \frac { 3 } { 4 } - \frac { 2 2 5 } { 3 2 } \mathbf { m } + \mathcal { O } ( \mathbf { m } ^ { 2 } ) .
$$

Likewise, since $\Omega _ { 1 } = 1 + 9 \ : \mathsf { m } ^ { 2 }$ (see Table 10.1), it follows from Equations (10.63), (10.84), and (10.87) that

$$
\iota \simeq \frac { ( 9 / 1 6 ) \mathsf { m } ^ { 3 } \iota } { ( 3 / 2 ) \mathsf { m } ^ { 2 } - 2 \mathsf { g } \mathsf { m } ^ { 2 } } ,
$$

which yields

$$
9 \simeq \frac 3 4 + \frac 9 { 3 2 } \mathsf { m } + \mathcal { O } ( \mathsf { m } ^ { 2 } ) .
$$

According to the above analysis, our final expressions for δX, δY, and δZ are

$$
\begin{array} { r l } { \left. \mathbf { X } \right. } & { = - \frac { 1 } { 2 } \gamma ^ { 5 } - \frac { 1 } { 4 } \gamma ^ { 5 } - \epsilon \cos ( \sin ( 1 + \cos ^ { 3 } ) \Gamma - \cos ) + \frac { 1 } { 2 } \zeta ^ { 2 } \cos 2 ( 2 ( 1 - \epsilon ) } \\ & { + \frac { 1 } { 4 } \zeta ^ { 2 } \cos 2 \Gamma ) + \mathbf { I } \cos 2 \left( \Gamma + 2 \gamma \right) - \left( \epsilon - \pi \right) \cos ^ { 2 } \left( 2 ( 1 - \pi ) ! \right) } \\ & { - \frac { 1 } { 1 5 } m _ { \mathrm { e } } \cos ( 5 \left( 1 - 2 \pi ) - \cos ^ { 2 } \left( 1 + \omega _ { \mathrm { p } } \right) \right) } \\ { \left. \mathbf { X } \right. } & { = - 2 \epsilon \sin ( 1 + \cos ^ { 3 } ) \left( 1 - \omega _ { \mathrm { E } } \right) - \frac { 1 } { 4 } \epsilon ^ { 5 } \sin ^ { 2 } \left( 1 + \sin ^ { 3 } \left( 1 - 2 \omega _ { \mathrm { E } } \right) \right) } \\ & { - \frac { 1 } { 4 } \gamma ^ { 5 } \sin 2 ( 1 + \sin ^ { 3 } \left( 1 + 2 \pi \right) + 1 ) \cos ^ { 2 } \left( \frac { \pi } { 2 } \right) - \left( \frac { \epsilon - \pi } { 2 } \right) } \\ & { + \frac { 1 } { 1 5 } \left( 1 + \cos ^ { 3 } \left( 1 + \cos ^ { 3 } \left( 1 + \omega _ { \mathrm { p } } \right) \right) \right) } \\ { \left. \mathbf { Z } \right. } & { = - \mathbf { I } \sin ( 1 ) + \mathbf { Z } \cos ^ { 2 } \left( \Gamma - \cos \left( 1 \right) ^ { 2 } \right) \Gamma + \mathbf { I } \sin \left( 1 - \left( \omega _ { \mathrm { p } } \right) \right) \mathbf { I } \cos ^ { 2 } \left( 1 - \omega _ { \mathrm { E } } \right) } \\ & { + \frac { 1 } { 2 } \epsilon ^ { 5 } \cos \left( 2 \pi \right) \left( 1 - \cos ^ { 2 } \left( 1 + \omega _ { \mathrm { p } } \right) \right) } \\ { \left. \mathbf { Z } \right. } & { = \sin ( 1 + \mathbf { Z } \cos ^ { 2 } \left( \Gamma + \pi \right) + \mathbf { I } \cos ^ { 2 } \left( 1 - \omega _ { \mathrm { P } } \right) \left( \Gamma - \cos ^ { 2 } \left( \Gamma \right) \right) } \\ &  + \frac \end{array}
$$

Thus, making use of Equations (10.36)–(10.38), we find that

$$
\begin{array} { r c l } { \frac { \Gamma } { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt \mathtt { \mathtt \mathtt \Pi } } } } } } } } } } } } } } & { = } & { 1 - e \cos [ ( 1 + \mathtt { c } \mathfrak { m } ^ { 2 } ) \mathsf { T } - \alpha _ { 0 } ] + \displaystyle \frac { 1 } { 2 } e ^ { 2 } - \displaystyle \frac { 1 } { 6 } \mathfrak { m } ^ { 2 } - \frac { 1 } { 2 } e ^ { 2 } \cos [ 2 \left( 1 + \mathtt { c } \mathfrak { m } ^ { 2 } \right) \mathsf { T } - 2 } \\ & & { - \mathfrak { m } ^ { 2 } \cos [ 2 \left( 1 - \mathfrak { m } \right) \mathsf { T } ] - \displaystyle \frac { 1 5 } { 8 } \mathfrak { m } e \cos [ ( 1 - 2 \mathfrak { m } - \mathtt { c } \mathfrak { m } ^ { 2 } ) \mathsf { T } + \alpha _ { 0 } ] , } \end{array}
$$

$$
\begin{array} { r c l } { { \Theta } } & { { = } } & { { \mathsf { T } + 2 \mathsf { e } \sin [ ( 1 + \mathsf { c } \mathsf { m } ^ { 2 } ) \mathsf { T } - \alpha _ { 0 } ] + \frac { 5 } { 4 } \mathsf { e } ^ { 2 } \sin [ 2 \left( 1 + \mathsf { c } \mathsf { m } ^ { 2 } \right) \mathsf { T } - 2 \alpha _ { 0 } ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \frac { 1 } { 4 } \mathsf { t } ^ { 2 } \sin [ 2 \left( 1 + \mathsf { g } \mathsf { m } ^ { 2 } \right) \mathsf { T } - 2 \gamma _ { 0 } ] + \frac { 1 1 } { 8 } \mathsf { m } ^ { 2 } \sin [ 2 \left( 1 - \mathsf { m } \right) \mathsf { T } ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \frac { 1 5 } { 4 } \mathsf { m } \mathsf { e } \sin [ \left( 1 - 2 \mathsf { m } - \mathsf { c } \mathsf { m } ^ { 2 } \right) \mathsf { T } + \alpha _ { 0 } ] , } } \\ { { } } & { { } } & { { } } \\ { { \beta } } & { { = } } & { { \iota \sin [ [ 1 + \mathsf { g } \mathsf { m } ^ { 2 } ) \mathsf { T } - \gamma _ { 0 } ] + \mathsf { e } \iota \sin [ \left( \alpha - \mathsf { g } \right) \mathsf { m } ^ { 2 } \mathsf { T } - \alpha _ { 0 } + \gamma _ { 0 } ] } } \\ { { } } & { { } } & { { + \mathsf { e } \iota \sin [ [ 2 + \mathsf { c } \mathsf { m } ^ { 2 } + \mathsf { g } \mathsf { m } ^ { 2 } ) \mathsf { T } - \alpha _ { 0 } - \gamma _ { 0 } ] } } \\ { { } } & { { } } & { { + \frac { 3 } { 8 } \mathsf { m } \iota \sin [ \left( 1 - 2 \mathsf { m } - \mathsf { g } \mathsf { m } ^ { 2 } \right) \mathsf { T } + \gamma _ { 0 } ] . } } \end{array}
$$

The above expressions are accurate up to second-order in the small parameters e, ι, and m.

# 10.6 Description of Lunar Motion

In order to better understand the perturbed lunar motion derived in the previous section, it is helpful to introduce the concept of the mean moon. This is an imaginary body which orbits the Earth, in the ecliptic plane, at a steady angular velocity that is equal to the Moon’s mean orbital angular velocity, n. Likewise, the mean sun is a second imaginary body which orbits the Earth, in the ecliptic plane, at a steady angular velocity that is equal to the Sun’s mean orbital angular velocity, $\mathfrak { n ^ { \prime } }$ . Thus, the ecliptic longitudes of the mean moon and the mean sun are

$$
\begin{array} { r c l } { { \bar { \theta } } } & { { = } } & { { \mathrm { n \dag , } } } \\ { { \bar { \theta } ^ { \prime } } } & { { = } } & { { \mathrm { n ^ { \prime } \dag , } } } \end{array}
$$

respectively. Here, for the sake of simplicity, and also for the sake of consistency with our previous analysis, we have assumed that both objects are located at ecliptic longitude $0 ^ { \circ }$ at time $\mathrm { t } = 0$ .

Now, from Equation (10.95), to first-order in small parameters, the lunar perigee corresponds to $( 1 + { \mathsf { c } } \mathsf { m } ^ { 2 } ) \mathsf { n } \mathsf { t } - \mathsf { \alpha } _ { 0 } = \mathsf { j } 2 \pi ,$ , where $\mathrm { j }$ is an integer. However, this condition can also be written $\bar { \mathsf { \theta } } = \boldsymbol { \alpha }$ , where

$$
\alpha = \alpha _ { 0 } + \alpha _ { 1 } \mathrm { n ^ { \prime } t } ,
$$

and, making use of Equation (10.89), together with the definition $\mathfrak { m } = \mathfrak { n } ^ { \prime } / \mathfrak { n }$ ,

$$
\alpha _ { 1 } = \frac { 3 } { 4 } \mathrm { m } + \frac { 2 5 5 } { 3 2 } \mathrm { m } ^ { 2 } + \mathcal { O } ( \mathrm { m } ^ { 3 } ) .
$$

Thus, we can identify $\propto$ as the mean ecliptic longitude of the perigee. Moreover, according to Equation (10.100), the perigee precesses (i.e., its longitude increases in time) at the mean rate of $3 6 0 \alpha _ { 1 }$ degrees per year. (Of course, a year corresponds to $\Delta \mathrm { t } = 2 \pi / \mathrm { n } ^ { \prime } . )$ Furthermore, it is clear that this precession is entirely due to the perturbing influence of the

Sun, since it only depends on the parameter m, which is a measure of this influence. Given that $\mathfrak { m } = 0 . 0 7 4 8 0$ , we find that the perigee advances by $3 4 . 3 6 ^ { \circ }$ degrees per year. Hence, we predict that the perigee completes a full circuit about the Earth every $1 / \alpha _ { 1 } = 1 0 . 5$ years. In fact, the lunar perigee completes a full circuit every 8.85 years. Our prediction is somewhat inaccurate because our previous analysis neglected $\mathcal { O } ( \mathfrak { m } ^ { 2 } )$ , and smaller, contributions to the parameter c [see Equation (10.89)], and these turn out to be significant.

From Equation (10.97), to first-order in small parameters, the Moon passes through its ascending node when $( 1 + { \mathfrak { g } } \mathfrak { m } ^ { 2 } ) \mathfrak { n } \mathfrak { t } - \gamma _ { 0 } = \gamma _ { 0 } + \mathfrak { j } 2 \pi _ { : }$ , where j is an integer. However, this condition can also be written $\bar { \theta } = \gamma$ , where

$$
\gamma = \gamma _ { 0 } - \gamma _ { 1 } \mathrm { n ^ { \prime } t } ,
$$

and, making use of Equation (10.91),

$$
\gamma _ { 1 } = \frac { 3 } { 4 } \mathsf { m } - \frac { 9 } { 3 2 } \mathsf { m } ^ { 2 } + \mathcal { O } ( \mathsf { m } ^ { 3 } ) .
$$

Thus, we can identify $\gamma$ as the mean ecliptic longitude of the ascending node. Moreover, according to Equation (10.102), the ascending node regresses (i.e., its longitude decreases in time) at the mean rate of $3 6 0 \gamma _ { 1 }$ degrees per year. As before, it is clear that this regression is entirely due to the perturbing influence of the Sun. Moreover, we find that the ascending node retreats by $1 9 . 6 3 ^ { \circ }$ degrees per year. Hence, we predict that the ascending node completes a full circuit about the Earth every $1 / \gamma _ { 1 } = 1 8 . 3$ years. In fact, the lunar ascending node completes a full circuit every 18.6 years, so our prediction is fairly accurate.

It is helpful to introduce the lunar mean anomaly,

$$
M = { \bar { \theta } } - \alpha ,
$$

which is defined as the angular distance (in longitude) between the mean Moon and the perigee. It is also helpful to introduce the lunar mean argument of latitude,

$$
\mathsf { F } = \bar { \mathsf { \boldsymbol { \theta } } } - \boldsymbol { \gamma } ,
$$

which is defined as the angular distance (in longitude) between the mean Moon and the ascending node. Finally, it is helpful to introduce the mean elongation of the Moon,

$$
{ \mathrm { D } } = { \bar { \Theta } } - { \bar { \theta } } ^ { \prime } ,
$$

which is defined as the difference between the longitudes of the mean Moon and the mean Sun.

When expressed in terms of $M , \mathsf { F } _ { : }$ , and $_ \mathrm { D }$ , our previous expression (10.96) for the true ecliptic longitude of the Moon becomes

$$
\theta = { \bar { \theta } } + \lambda ,
$$

where

$$
\lambda ~ = ~ 2 e \sin M + { \frac { 5 } { 4 } } e ^ { 2 } \sin 2 M - { \frac { 1 } { 4 } } \iota ^ { 2 } \sin 2 \mathsf { F } + { \frac { 1 1 } { 8 } } \mathsf { m } ^ { 2 } \sin 2 \mathsf { D } + { \frac { 1 5 } { 4 } } \mathsf { m } e \sin ( 2 \mathsf { D } \times \mathsf { B } ) ,
$$

is the angular distance (in longitude) between the Moon and the mean Moon. The first three terms on the right-hand side of the above expression are Keplerian (i.e., they are independent of the perturbing action of the Sun). In fact, the first is due to the eccentricity of the lunar orbit (i.e., the fact that the geometric center of the orbit is slightly shifted from the Earth), the second is due to the ellipticity of the orbit (i.e., the fact that the orbit is slightly non-circular), and the third is due to the slight inclination of the orbit to the ecliptic plane. However, the final two terms are caused by the perturbing action of the Sun. In fact, the fourth term corresponds to variation, whilst the fifth corresponds to evection. Note that variation attains its maximal amplitude around the so-called octant points, at which the Moon’s disk is either one-quarter or three-quarters illuminated (i.e., when $\mathrm { D } = 4 5 ^ { \circ }$ , $1 3 5 ^ { \circ }$ , $2 2 5 ^ { \circ }$ , or $3 1 5 ^ { \circ } .$ ). Conversely, the amplitude of variation is zero around the so-called quadrant points, at which the Moon’s disk is either fully illuminated, half illuminated, or not illuminated at all (i.e., when $\mathrm { D } = 0 ^ { \circ }$ , $9 0 ^ { \circ }$ , $1 8 0 ^ { \circ }$ , or $2 7 0 ^ { \circ } .$ ). Evection can be thought of as causing a slight reduction in the eccentricity of the lunar orbit around the times of the new moon and the full moon (i.e., $\mathrm { \Delta D } = 0 ^ { \circ }$ and $\mathrm { ~ D ~ = ~ } 1 8 0 ^ { \circ } \mathrm { ~ }$ ), and causing a corresponding slight increase in the eccentricity around the times of the first and last quarter moons (i.e., $\mathrm { ~ D ~ = ~ } 9 0 ^ { \circ }$ and $\mathrm { ~ D ~ } = 2 7 0 ^ { \circ } )$ . This follows because the evection term in Equation (10.108) augments the eccentricity term, $2 e \sin M$ , when c $\mathtt { o s } 2 \mathsf { D } = - 1$ , and reduces the term when cos $2 \mathrm { D } ~ = ~ + 1$ . The variation and evection terms appearing in expression (10.108) oscillate sinusoidally with periods of half a synodic month,2 or 14.8 days, and 31.8 days, respectively. These periods are in good agreement with observations. Finally, the amplitudes of the variation and evection terms (calculated using $\mathfrak { m } = 0 . 0 7 4 8 0$ and $e \ : = \ : 0 . 0 5 4 8 8 )$ ) are 1630 and 3218 arc seconds, respectively. However, the observed amplitudes are 2370 and 4586 arc seconds, respectively. It turns out that our expressions for these amplitudes are somewhat inaccurate because, for the sake of simplicity, we have only calculated the lowest order (in m) contributions to them. Recall that we also neglected the slight eccentricity, $e ^ { \prime } = 0 . 0 1 6 7 1 1$ , of the Sun’s apparent orbit about the Earth in our calculation. In fact, the eccentricity of the solar orbit gives rise to a small addition term $- 3 \mathfrak { m } e ^ { \prime }$ sin $M ^ { \prime }$ on the right-hand side of (10.108), where $M ^ { \prime }$ is the Sun’s mean anomaly. This term, which is known as the annual equation, oscillates with a period of a solar year, and has an amplitude of 772 arc seconds.

When expressed in terms of $_ \mathrm { D }$ and $\digamma$ our previous expression (10.97) for the ecliptic latitude of the Moon becomes

$$
\beta = \mathfrak { t } \sin ( \mathsf { F } + \lambda ) + \frac { 3 } { 8 } \mathfrak { m } \mathfrak { c } \sin ( 2 \mathrm { D } - \mathsf { F } ) .
$$

The first term on the right-hand side of this expression is Keplerian (i.e., it is independent of the perturbing influence of the Sun). However, the final term, which is known as evection in latitude, is due to the Sun’s action. Evection in latitude can be thought of as causing a slight increase in the inclination of the lunar orbit to the ecliptic at the times of the first and last quarter moons, and a slight decrease at the times of the new moon and the full moon. The evection in latitude term oscillates sinusoidally with a period of 32.3 days, and has an amplitude of 521 arc seconds. This period is in good agreement with observations. However, the observed amplitude of the evection in latitude term is 624 arc seconds. As before, our expression for the amplitude is somewhat inaccurate because we have only calculated the lowest order (in m) contribution.

# 11 Orbital Perturbation Theory

# 11.1 Introduction

The two-body orbit theory described in Chapter 4 neglects the gravitational interactions between the various different planets in the Solar System, whilst retaining those between each individual planet and the Sun. This is an excellent first approximation, since the former interactions are much weaker than the latter, as a consequence of the small masses of the Planets relative to the Sun (see Table 4.1). Nevertheless, interplanetary gravitational interactions do have a profound influence on planetary orbits when integrated over long periods of time. The aim of this chapter is to examine this influence in a systematic fashion using a branch of celestial mechanics known as perturbation theory.

# 11.2 Disturbing Function

For the moment, let us consider a simplified Solar System that consists of the Sun and two planets—see Figure 11.1. Let the Sun be of mass $M$ , and position vector $\mathbf { R } _ { s }$ . Likewise, let the two planets have masses m and $\mathfrak { m } ^ { \prime }$ , and position vectors $\mathbf { R }$ and $\mathbf { R } ^ { \prime }$ , respectively. Here, we are assuming that m, $\mathfrak { m } ^ { \prime } \ll M$ . Let ${ \bf r } = { \bf R } - { \bf R } _ { s }$ and $\mathbf { r } ^ { \prime } = \mathbf { R } ^ { \prime } - \mathbf { R } _ { s }$ , be the position vector of each planet relative to the Sun. Without loss of generality, we can assume that ${ \boldsymbol { \mathrm { r } } } ^ { \prime } > { \boldsymbol { \mathrm { r } } }$ .

Now, the equations of motion of the various elements of our simplified Solar System are

$$
\begin{array} { r c l } { { { \sf M } \ddot { \bf R } _ { s } } } & { { = } } & { { { \sf G } { \sf M } \mathrm { m } \frac { { \bf r } } { \mathrm { r } ^ { 3 } } + { \sf G } { \sf M } \mathrm { m } ^ { \prime } \frac { { \bf r } ^ { \prime } } { \mathrm { r } ^ { \prime 3 } } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { m } \ddot { \bf R } } } & { { = } } & { { { \sf G } \mathrm { m } \mathrm { m } ^ { \prime } \frac { { \bf r } ^ { \prime } - { \bf r } } { | { \bf r } ^ { \prime } - { \bf r } | ^ { 3 } } - { \sf G } \mathrm { m } { \cal M } \frac { { \bf r } } { \mathrm { r } ^ { 3 } } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { m } ^ { \prime } \ddot { \bf R } ^ { \prime } } } & { { = } } & { { { \sf G } \mathrm { m } ^ { \prime } \mathrm { m } \frac { { \bf r } - { \bf r } ^ { \prime } } { | { \bf r } - { \bf r } ^ { \prime } | ^ { 3 } } - { \sf G } \mathrm { m } ^ { \prime } { \sf M } \frac { { \bf r } ^ { \prime } } { \mathrm { r } ^ { \prime 3 } } , } } \end{array}
$$

It thus follows that

$$
\begin{array} { r c l } { { \displaystyle { \ddot { \bf r } } + \mu \frac { { \bf r } } { \Gamma ^ { 3 } } } } & { { = } } & { { \mathsf { G } \mathrm { m } ^ { \prime } \left( \frac { { \bf r } ^ { \prime } - { \bf r } } { | { \bf r } ^ { \prime } - { \bf r } | ^ { 3 } } - \frac { { \bf r } ^ { \prime } } { \Gamma ^ { \prime 3 } } \right) , } } \\ { { \displaystyle { \ddot { \bf r } } ^ { \prime } + \mu ^ { \prime } \frac { { \bf r } ^ { \prime } } { \Gamma ^ { \prime 3 } } } } & { { = } } & { { \mathsf { G } \mathrm { m } \left( \frac { { \bf r } - { \bf r } ^ { \prime } } { | { \bf r } - { \bf r } ^ { \prime } | ^ { 3 } } - \frac { { \bf r } } { \Gamma ^ { 3 } } \right) , } } \end{array}
$$

where $\mu = \epsilon \left( M + \mu \right)$ , and $\mu ^ { \prime } = \mathsf { G } \left( M + \mathsf { m } ^ { \prime } \right)$ . The right-hand sides of the above equations specify the interplanetary interaction forces that were neglected in our previous analysis.

![](images/49fa864574e3950de099335938b6bc1cd487a6da4f7cf13a9dc16650c82d7cc6.jpg)  
Figure 11.1: A simplified model of the Solar System.

These right-hand sides can be conveniently expressed as the gradients of potentials: i.e.,

$$
\begin{array} { r c l } { { \displaystyle { \ddot { \bf r } } + \mu \frac { \bf r } { \Gamma ^ { 3 } } } } & { { = } } & { { \nabla \mathcal R , } } \\ { { \displaystyle { \ddot { \bf r } } ^ { \prime } + \mu ^ { \prime } \frac { \bf r ^ { \prime } } { \Gamma ^ { \prime 3 } } } } & { { = } } & { { \nabla ^ { \prime } \mathcal R ^ { \prime } , } } \end{array}
$$

where

$$
\begin{array} { r l r } { \mathcal { R } ( \mathbf { r } , \mathbf { r } ^ { \prime } ) } & { = } & { \tilde { \mu } ^ { \prime } \left( \frac { 1 } { \left| \mathbf { r } - \mathbf { r } ^ { \prime } \right| } - \frac { \mathbf { r } \cdot \mathbf { r } ^ { \prime } } { \mathbf { r } ^ { \prime 3 } } \right) , } \\ { \mathcal { R } ^ { \prime } ( \mathbf { r } , \mathbf { r } ^ { \prime } ) } & { = } & { \tilde { \mu } \left( \frac { 1 } { \left| \mathbf { r } - \mathbf { r } ^ { \prime } \right| } - \frac { \mathbf { r } \cdot \mathbf { r } ^ { \prime } } { \mathbf { r } ^ { 3 } } \right) , } \end{array}
$$

with $\tilde { \mu } = G \mathfrak { m }$ , and $\tilde { \mu } ^ { \prime } = \mathsf { G } \mathsf { m } ^ { \prime }$ . Here, $\mathcal { R } ( \mathbf { r } , \mathbf { r } ^ { \prime } )$ and $\mathcal { R } ^ { \prime } ( \mathbf { r } , \mathbf { r } ^ { \prime } )$ are termed disturbing functions. Moreover, $\nabla$ and $\nabla ^ { \prime }$ are the gradient operators involving the unprimed and primed coordinates, respectively.

# 11.3 Osculating Orbital Elements

Consider Equation (11.6), which can be written

$$
\begin{array} { r l r } { \ddot { \displaystyle x } + \mu \frac { x } { \displaystyle r ^ { 3 } } } & { = } & { \displaystyle \frac { \partial { \mathcal R } } { \partial \displaystyle x } , } \\ { \ddot { \displaystyle y } + \mu \frac { y } { \displaystyle r ^ { 3 } } } & { = } & { \displaystyle \frac { \partial { \mathcal R } } { \partial \displaystyle y } , } \\ { \ddot { \displaystyle z } + \mu \frac { z } { \displaystyle r ^ { 3 } } } & { = } & { \displaystyle \frac { \partial { \mathcal R } } { \partial \displaystyle z } . } \end{array}
$$

If the right-hand sides of the above equations are set to zero then the problem reduces to that considered in Chapter 4, and we thus have solutions which can be written in the form

$$
\begin{array} { r c l } { x } & { = } & { \mathbf { f } _ { 1 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) , } \\ { \mathbf { y } } & { = } & { \mathbf { f } _ { 2 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) , } \\ { z } & { = } & { \mathbf { f } _ { 3 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) , } \\ { \dot { x } } & { = } & { g _ { 1 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) , } \\ { \dot { \mathbf { y } } } & { = } & { g _ { 2 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) , } \\ { \dot { z } } & { = } & { g _ { 3 } \big ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } , \mathbf { t } \big ) . } \end{array}
$$

Here, $\mathbf { c } _ { 1 } , \cdots , \mathbf { c } _ { 6 }$ are the six orbital elements of the first planet (see Section 4.10), which can be thought of as constants of its motion. It follows that

$$
{ \mathfrak { g } } _ { \mathrm { k } } = { \frac { \partial { \mathfrak { f } } _ { \mathrm { k } } } { \partial { \mathrm { t } } } } ,
$$

for $\mathtt { k } = 1 , 2 , 3$ .

Let us now take the right-hand sides of Equations (11.10)–(11.12) into account. The orbital elements, ${ \bf c } _ { 1 } , \ldots , { \bf c } _ { 6 }$ , are no longer constants of the motion. However, we would expect them to be relatively slowly varying functions of time, given the relative smallness of the right-hand sides. Let us derive evolution equations for these so-called osculating orbital elements.

According to Equation (11.13), we have

$$
\frac { \mathrm { d } x } { \mathrm { d t } } = \frac { \partial \mathsf { f } _ { 1 } } { \partial \mathrm { t } } + \sum _ { \mathrm { k } = 1 , 6 } \frac { \partial \mathsf { f } _ { 1 } } { \partial \mathsf { c } _ { \mathrm { k } } } \frac { \mathrm { d } \mathsf { c } _ { \mathrm { k } } } { \mathrm { d t } } .
$$

If this expression, and the analogous expressions for $\mathrm { d } \mathfrak { y } / \mathrm { d t }$ and $\mathtt { d } z / \mathtt { d t }$ , were differentiated in time, and the results substituted into Equations (11.10)–(11.12), then we would obtain three time evolution equations for the six variables $\mathbf { c } _ { 1 } , \cdots , \mathbf { c } _ { 6 }$ . In order to make the problem definite, three additional conditions must be introduced into the problem. It is convenient to choose

$$
\sum _ { \mathrm { k = 1 , 6 } } \frac { \partial \mathrm { f _ { l } } } { \partial \mathrm { c _ { k } } } \frac { \mathrm { d } \mathrm { c _ { k } } } { \mathrm { d t } } = 0 ,
$$

for $\mathsf { l } = 1 , 2 , 3$ . Hence, it follows that

$$
\begin{array} { r l r } { \displaystyle { \frac { \mathrm { d } x } { \mathrm { d t } } } } & { = } & { \displaystyle { \frac { \partial \mathsf { f } _ { 1 } } { \partial \mathsf { t } } } = \mathsf { g } _ { 1 } , } \\ { \displaystyle { \frac { \mathrm { d } \mathsf { y } } { \mathrm { d t } } } } & { = } & { \displaystyle { \frac { \partial \mathsf { f } _ { 2 } } { \partial \mathsf { t } } } = \mathsf { g } _ { 2 } , } \\ { \displaystyle { \frac { \mathrm { d } z } { \mathrm { d t } } } } & { = } & { \displaystyle { \frac { \partial \mathsf { f } _ { 3 } } { \partial \mathsf { t } } } = \mathsf { g } _ { 3 } . } \end{array}
$$

Differentiation of the above equations with respect to time yields

$$
{ \begin{array} { r l r } { { \frac { \mathrm { d } ^ { 2 } x } { \mathrm { d } { \mathrm { t } } ^ { 2 } } } } & { = } & { { \frac { \partial ^ { 2 } \mathsf { f } _ { 1 } } { \partial { \mathrm { t } } ^ { 2 } } } + \displaystyle \sum _ { { \mathrm { k } } = 1 , 6 } { \frac { \partial \mathsf { g } _ { 1 } } { \partial \mathsf { c } _ { \mathrm { k } } } } { \frac { \mathrm { d } \mathsf { c } _ { \mathrm { k } } } { \mathrm { d } { \mathrm { t } } } } , } \\ { { \frac { \mathrm { d } ^ { 2 } \mathsf { y } } { \mathrm { d } { \mathrm { t } } ^ { 2 } } } } & { = } & { { \frac { \partial ^ { 2 } \mathsf { f } _ { 2 } } { \partial { \mathrm { t } } ^ { 2 } } } + \displaystyle \sum _ { { \mathrm { k } } = 1 , 6 } { \frac { \partial \mathsf { g } _ { 2 } } { \partial \mathsf { c } _ { \mathrm { k } } } } { \frac { \mathrm { d } \mathsf { c } _ { \mathrm { k } } } { \mathrm { d t } } } , } \\ { { \frac { \mathrm { d } ^ { 2 } z } { \mathrm { d } { \mathrm { t } } ^ { 2 } } } } & { = } & { { \frac { \partial ^ { 2 } \mathsf { f } _ { 3 } } { \partial { \mathrm { t } } ^ { 2 } } } + \displaystyle \sum _ { { \mathrm { k } } = 1 , 6 } { \frac { \partial \mathsf { g } _ { 3 } } { \partial \mathsf { c } _ { \mathrm { k } } } } { \frac { \mathrm { d } \mathsf { c } _ { \mathrm { k } } } { \mathrm { d t } } } . } \end{array} }
$$

Substitution into Equations (11.10)–(11.12) gives

$$
\begin{array} { r l } { \frac { \partial ^ { 2 } \mathbf { f } _ { 1 } } { \partial \mathbf { t } ^ { 2 } } + \mu \frac { \mathbf { f } _ { 1 } } { \mathbf { r } ^ { 3 } } + \displaystyle \sum _ { \mathbf { k } = 1 , 6 } \frac { \partial \mathbf { g } _ { 1 } } { \partial \mathbf { c } _ { \mathbf { k } } } \frac { \mathrm { d } \mathbf { c } _ { \mathbf { k } } } { \mathrm { d } \mathbf { t } } } & { = ~ \frac { \partial \mathcal { R } } { \partial x } , } \\ { \frac { \partial ^ { 2 } \mathbf { f } _ { 2 } } { \partial \mathbf { t } ^ { 2 } } + \mu \frac { \mathbf { f } _ { 2 } } { \mathbf { r } ^ { 3 } } + \displaystyle \sum _ { \mathbf { k } = 1 , 6 } \frac { \partial \mathbf { g } _ { 2 } } { \partial \mathbf { c } _ { \mathbf { k } } } \frac { \mathrm { d } \mathbf { c } _ { \mathbf { k } } } { \mathrm { d } \mathbf { t } } } & { = ~ \frac { \partial \mathcal { R } } { \partial y } , } \\ { \frac { \partial ^ { 2 } \mathbf { f } _ { 3 } } { \partial \mathbf { t } ^ { 2 } } + \mu \frac { \mathbf { f } _ { 3 } } { \mathbf { r } ^ { 3 } } + \displaystyle \sum _ { \mathbf { k } = 1 , 6 } \frac { \partial \mathbf { g } _ { 3 } } { \partial \mathbf { c } _ { \mathbf { k } } } \frac { \mathrm { d } \mathbf { c } _ { \mathbf { k } } } { \mathrm { d } \mathbf { t } } } & { = ~ \frac { \partial \mathcal { R } } { \partial z } , } \end{array}
$$

where $\boldsymbol { \mathsf { r } } = ( \mathsf { f } _ { 1 } ^ { 2 } + \mathsf { f } _ { 2 } ^ { 2 } + \mathsf { f } _ { 3 } ^ { 2 } ) ^ { 1 / 2 }$ . Since $\mathsf { f } _ { 1 } , \mathsf { f } _ { 2 }$ , and $\mathsf { f } _ { 3 }$ are the respective solutions to the above equations when the right-hand sides are zero, and the orbital elements are thus constants, it follows that the first two terms in each equation cancel one another. Hence, writing $\mathsf { f } _ { 1 }$ as $x$ , and $9 1$ as $\dot { x }$ , etc., Equations (11.21) and (11.28)–(11.30) yield

$$
\begin{array} { r l } { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf x } } { \partial \alpha _ { i } } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ 0 , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf y } _ { i } } { \partial \alpha _ { i } } \frac { \partial { \bf z } _ { i } } { \partial \bf t } } & { = ~ 0 , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf z } _ { i } } { \partial \bf z } \frac { \partial { \bf z } _ { i } } { \partial \bf t } } & { = ~ 9 , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf x } _ { i } } { \partial \bf t } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ 9 . } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf x } _ { i } } { \partial \bf t } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ \frac { \partial { \bf R } } { \partial { \bf x } } , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf y } _ { i } } { \partial \bf t } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ \frac { \partial { \bf R } } { \partial { \bf y } } , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf y } _ { i } } { \partial \bf t } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ \frac { \partial { \bf R } } { \partial { \bf y } } , } \\ { \displaystyle \sum _ { i < \nu } \frac { \partial { \bf z } } { \partial \bf t } \frac { \partial { \bf x } _ { i } } { \partial \bf t } } & { = ~ \frac { \partial { \bf R } } { \partial { \bf z } } . } \end{array}
$$

These six equations are equivalent to the three original equations of motion, (11.10)– (11.12).

# 11.4 Lagrange Brackets

Six new equations can be derived from Equations (11.31)–(11.36) by multiplying them successively by $- { \partial \dot { \mathrm { x } } } / { \partial { c _ { \mathrm { j } } } } , ~ - { \partial \dot { \mathrm { y } } } / { \partial { c _ { \mathrm { j } } } } , ~ - { \partial \dot { z } } / { \partial { c _ { \mathrm { j } } } } , ~ { \partial { x } } / { \partial { c _ { \mathrm { j } } } } , ~ { \partial \mathrm { y } } / { \partial { c _ { \mathrm { j } } } } , ~ { \partial z } / { \partial { c _ { \mathrm { j } } } } .$ , and summing the resulting equations. The right-hand sides of the new equations are

$$
\frac { \partial \mathcal { R } } { \partial x } \frac { \partial x } { \partial c _ { \mathrm { j } } } + \frac { \partial \mathcal { R } } { \partial y } \frac { \partial y } { \partial c _ { \mathrm { j } } } + \frac { \partial \mathcal { R } } { \partial z } \frac { \partial z } { \partial c _ { \mathrm { j } } } \equiv \frac { \partial \mathcal { R } } { \partial c _ { \mathrm { j } } } .
$$

The new equations can be written in a more compact form via the introduction of Lagrange brackets, which are defined

$$
[ c _ { \mathrm { j } } , c _ { \mathrm { k } } ] = \sum _ { \mathrm { l = l } , 3 } \left( \frac { \partial x _ { \mathrm { l } } } { \partial c _ { \mathrm { j } } } \frac { \partial \dot { x } _ { \mathrm { l } } } { \partial c _ { \mathrm { k } } } - \frac { \partial x _ { \mathrm { l } } } { \partial c _ { \mathrm { k } } } \frac { \partial \dot { x } _ { \mathrm { l } } } { \partial c _ { \mathrm { j } } } \right) ,
$$

where $x _ { \mathrm { i } } \equiv x$ , $x _ { 2 } \equiv { } y$ , and $x _ { 3 } \equiv z$ . Thus, the new equations become

$$
\sum _ { \mathrm { k } = 1 , 6 } [ \mathrm { c } _ { \mathrm { j } } , \mathrm { c } _ { \mathrm { k } } ] \frac { \mathrm { d } \mathrm { c } _ { \mathrm { k } } } { \mathrm { d t } } = \frac { \partial \mathcal { R } } { \partial \mathrm { c } _ { \mathrm { j } } } ,
$$

for ${ \mathrm { j } } = 1 , 6 .$ . Note, incidentally, that

$$
\begin{array} { r c l } { { [ c _ { \mathrm { j } } , c _ { \mathrm { j } } ] } } & { { = } } & { { 0 , } } \\ { { { } } } & { { { } } } & { { { } } } \\ { { [ c _ { \mathrm { j } } , c _ { \mathrm { k } } ] } } & { { = } } & { { - [ c _ { \mathrm { k } } , c _ { \mathrm { j } } ] . } } \end{array}
$$

Let

$$
[ \mathfrak { p } , \mathfrak { q } ] = \sum _ { \mathfrak { l } = 1 , 3 } \left( \frac { \partial { \mathfrak { x } } _ { \mathfrak { l } } } { \partial \mathfrak { p } } \frac { \partial \dot { \mathfrak { x } } _ { \mathfrak { l } } } { \partial \mathfrak { q } } - \frac { \partial { \mathfrak { x } } _ { \mathfrak { l } } } { \partial \mathfrak { q } } \frac { \partial \dot { \mathfrak { x } } _ { \mathfrak { l } } } { \partial \mathfrak { p } } \right) ,
$$

where $\mathfrak { p }$ and $\mathsf { q }$ are two orbital elements. It follows that

$$
\frac { \partial } { \partial \mathrm { t } } [ \boldsymbol { \mathrm { p } } , \boldsymbol { \mathrm { q } } ] = \sum _ { \lfloor = 1 , 3 } \left( \frac { \partial ^ { 2 } x _ { \lfloor } } { \partial \boldsymbol { \mathrm { p } } \partial \mathrm { t } } \frac { \partial \dot { x } _ { \lfloor } } { \partial \boldsymbol { \mathrm { q } } } + \frac { \partial x _ { \lfloor } } { \partial \boldsymbol { \mathrm { p } } } \frac { \partial ^ { 2 } \dot { x } _ { \lfloor } } { \partial \boldsymbol { \mathrm { q } } \partial \mathrm { t } } - \frac { \partial ^ { 2 } x _ { \lfloor } } { \partial \boldsymbol { \mathrm { q } } \partial \mathrm { t } } \frac { \partial \dot { x } _ { \lfloor } } { \partial \boldsymbol { \mathrm { p } } } - \frac { \partial x _ { \lfloor } } { \partial \boldsymbol { \mathrm { q } } } \frac { \partial ^ { 2 } \dot { x } _ { \lfloor } } { \partial \boldsymbol { \mathrm { p } } \partial \mathrm { t } } \right) ,
$$

or

$$
\frac { \partial } { \partial \mathrm { t } } [ \mathsf { p } , \mathsf { q } ] = \sum _ { \mathsf { l } = 1 , \mathsf { \Omega } } \left[ \frac { \partial } { \partial \mathsf { p } } \left( \frac { \partial \mathrm { x } _ { \mathrm { l } } } { \partial \mathrm { t } } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { l } } } { \partial \mathsf { q } } - \frac { \partial \mathrm { x } _ { \mathrm { l } } } { \partial \mathrm { q } } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { l } } } { \partial \mathrm { t } } \right) - \frac { \partial } { \partial \mathrm { q } } \left( \frac { \partial \mathrm { x } _ { \mathrm { l } } } { \partial \mathrm { t } } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { l } } } { \partial \mathsf { p } } - \frac { \partial \mathrm { x } _ { \mathrm { l } } } { \partial \mathsf { p } } \frac { \partial \dot { \mathrm { x } } _ { \mathrm { l } } } { \partial \mathrm { t } } \right) \right] .
$$

However, in the above expression, $x _ { \mathrm { l } }$ and $\dot { x } _ { \mathrm { l } }$ stand for coordinates and velocities of Keplerian orbits calculated with $\mathbf { c } _ { 1 } , \cdots , \mathbf { c } _ { 6 }$ treated as constants. Thus, we can write $\partial \mathbf { x } _ { \mathrm { l } } / \partial \mathbf { t } \equiv \dot { \mathbf { x } } _ { \mathrm { l } }$ and $\partial \dot { \mathbf { x } } / \partial \mathrm { t } \equiv \ddot { \mathbf { x } } _ { \mathrm { l } } .$ giving

$$
\frac { \partial } { \partial \mathbf { t } } [ \mathfrak { p } , \mathbf { q } ] = \sum _ { \mathfrak { l } = 1 , 3 } \left[ \frac { \partial } { \partial \mathfrak { p } } \left( \frac { 1 } { 2 } \frac { \partial \dot { x } _ { \mathfrak { l } } ^ { 2 } } { \partial \mathbf { q } } - \frac { \partial \mathsf { F } _ { 0 } } { \partial \mathfrak { x } _ { \mathfrak { l } } } \frac { \partial \mathfrak { x } _ { \mathfrak { l } } } { \partial \mathbf { q } } \right) - \frac { \partial } { \partial \mathbf { q } } \left( \frac { 1 } { 2 } \frac { \partial \dot { x } _ { \mathfrak { l } } ^ { 2 } } { \partial \mathfrak { p } } - \frac { \partial \mathsf { F } _ { 0 } } { \partial \mathfrak { x } _ { \mathfrak { l } } } \frac { \partial \mathfrak { x } _ { \mathfrak { l } } } { \partial \mathfrak { p } } \right) \right] ,
$$

since

$$
\ddot { \mathrm { x } } _ { \mathrm { l } } = \frac { \partial \mathsf { F } _ { 0 } } { \partial \mathrm { x } _ { \mathrm { l } } } ,
$$

where $\mathsf { F } _ { 0 } = \mu / \tau$ . Expression (11.45) reduces to

$$
\frac { \partial } { \partial \mathbf { t } } [ \mathsf { p } , \mathsf { q } ] = \frac { 1 } { 2 } \frac { \partial ^ { 2 } \nu ^ { 2 } } { \partial \mathsf { p } \partial \mathsf { q } } - \frac { \partial ^ { 2 } \mathsf { F } _ { 0 } } { \partial \mathsf { p } \partial \mathsf { q } } - \frac { 1 } { 2 } \frac { \partial ^ { 2 } \nu ^ { 2 } } { \partial \mathsf { q } \partial \mathsf { p } } + \frac { \partial ^ { 2 } \mathsf { F } _ { 0 } } { \partial \mathsf { q } \partial \mathsf { p } } = 0 ,
$$

where $\begin{array} { r } { \nu ^ { 2 } = \sum _ { \mathrm { l } = 1 , 3 } \dot { \mathrm { x } } _ { \mathrm { l } } ^ { 2 } } \end{array}$ . Hence, we conclude that Largrange brackets are functions of the osculating orbital elements, ${ \bf c } _ { 1 } , \ldots , { \bf c } _ { 6 } .$ , but are not explicit functions of t. It follows that we can evaluate these brackets at any convenient point in the orbit.

# 11.5 Transformation of Lagrange Brackets

Let our six orbital elements be the major radius, a, the eccentricity, $e$ , the mean longitude at epoch, $\bar { \lambda } _ { 0 }$ , the inclination, I, the longitude of the ascending node, $\Omega$ , and the longitude of the perihelion, $\varpi$ —see Section 4.10. The mean orbital angular velocity is $\boldsymbol { \mathrm { n } } = ( \mu / a ^ { 3 } ) ^ { 1 / 2 }$ [see Equation (4.96)]. Consider how a particular Lagrange bracket transforms under a rotation of the coordinate system (X, Y, Z), which was introduced in Section 4.10, about the $Z$ -axis (looking up the axis). We can write

$$
[ \mathrm { p } , \mathrm { q } ] = \frac { \partial ( X , \dot { X } ) } { \partial ( \mathrm { p } , \mathrm { q } ) } + \frac { \partial ( \Upsilon , \dot { \Upsilon } ) } { \partial ( \mathrm { p } , \mathrm { q } ) } + \frac { \partial ( Z , \dot { Z } ) } { \partial ( \mathrm { p } , \mathrm { q } ) } ,
$$

where

$$
{ \frac { \partial ( { \mathrm { a } } , { \mathrm { b } } ) } { \partial ( { \mathrm { c } } , { \mathrm { d } } ) } } \equiv { \frac { \partial { \mathrm { a } } } { \partial { \mathrm { c } } } } { \frac { \partial { \mathrm { b } } } { \partial { \mathrm { d } } } } - { \frac { \partial { \mathrm { a } } } { \partial { \mathrm { d } } } } { \frac { \partial { \mathrm { b } } } { \partial { \mathrm { c } } } } .
$$

Let the new coordinate system be $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ . A rotation about the Z-axis though an angle $\Omega$ brings the ascending node to the $x ^ { \prime }$ -axis—see Figure 4.4. The relation between the old and new coordinates is

$$
\begin{array} { r c l } { { \sf X } } & { { = } } & { { \sf x ^ { \prime } \cos \Omega - y ^ { \prime } \sin \Omega , } } \\ { { \sf Y } } & { { = } } & { { \sf x ^ { \prime } \sin \Omega + y ^ { \prime } \cos \Omega , } } \\ { { \sf Z } } & { { = } } & { { \sf z ^ { \prime } . } } \end{array}
$$

The partial derivatives with respect to $\mathfrak { p }$ can be written

$$
\begin{array} { r c l } { \displaystyle \frac { \partial { \boldsymbol X } } { \partial { \boldsymbol p } } } & { = } & { A _ { 1 } \cos \Omega - \mathsf { B } _ { 1 } \sin \Omega , } \\ { \displaystyle } & { } & \\ { \displaystyle \frac { \partial { \boldsymbol Y } } { \partial { \boldsymbol p } } } & { = } & { \mathsf { B } _ { 1 } \cos \Omega + A _ { 1 } \sin \Omega , } \\ { \displaystyle } & { } & \\ { \displaystyle \frac { \partial \dot { \boldsymbol X } } { \partial { \boldsymbol p } } } & { = } & { \mathsf { C } _ { 1 } \cos \Omega - \mathsf { D } _ { 1 } \sin \Omega , } \\ { \displaystyle } & { } & \\ { \displaystyle \frac { \partial \dot { \boldsymbol Y } } { \partial { \boldsymbol p } } } & { = } & { \mathsf { D } _ { 1 } \cos \Omega + \mathsf { C } _ { 1 } \sin \Omega , } \end{array}
$$

where

$$
\begin{array} { r l r } { \mathsf { A } _ { 1 } } & { = } & { \frac { \partial \hat { \mathbf { x } } ^ { \prime } } { \partial \mathbf { p } } - \mathbf { y } ^ { \prime } \frac { \partial \boldsymbol { \Omega } } { \partial \mathbf { p } } , } \\ { \mathsf { B } _ { 1 } } & { = } & { \frac { \partial \mathbf { y } ^ { \prime } } { \partial \mathbf { p } } + \mathbf { x } ^ { \prime } \frac { \partial \boldsymbol { \Omega } } { \partial \mathbf { p } } , } \\ { \mathsf { C } _ { 1 } } & { = } & { \frac { \partial \hat { \mathbf { x } } ^ { \prime } } { \partial \mathbf { p } } - \dot { \mathbf { y } } ^ { \prime } \frac { \partial \boldsymbol { \Omega } } { \partial \mathbf { p } } , } \\ { \mathsf { D } _ { 1 } } & { = } & { \frac { \partial \dot { \mathbf { y } } ^ { \prime } } { \partial \mathbf { p } } + \dot { \mathbf { x } } ^ { \prime } \frac { \partial \boldsymbol { \Omega } } { \partial \mathbf { p } } . } \end{array}
$$

Let $A _ { 2 } , \mathrm { ~ B } _ { 2 } , \mathrm { ~ C } _ { 2 }$ , and $\mathrm { D } _ { 2 }$ be the equivalent quantities obtained by replacing $\mathfrak { p }$ by $\mathsf { q }$ in the above equations. It thus follows that

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial ( X , \dot { X } ) } { \partial ( \boldsymbol { \mathbf { p } } , \boldsymbol { \mathbf { q } } ) } } } & { { = } } & { { \left( A _ { 1 } \mathrm { ~ C } _ { 2 } - A _ { 2 } \mathrm { ~ C } _ { 1 } \right) \cos ^ { 2 } \Omega + \left( \mathrm { B } _ { 1 } \mathrm { ~ D } _ { 2 } - \mathrm { B } _ { 2 } \mathrm { ~ D } _ { 1 } \right) \sin ^ { 2 } \Omega } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + ( - A _ { 1 } \mathrm { ~ D } _ { 2 } - \mathrm { ~ B } _ { 1 } \mathrm { ~ C } _ { 2 } + A _ { 2 } \mathrm { ~ D } _ { 1 } + \mathrm { B } _ { 2 } \mathrm { ~ C } _ { 1 } ) \sin \Omega \cos \Omega , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \frac { \partial ( \mathrm { Y } , \dot { \mathrm { Y } } ) } { \partial ( \boldsymbol { \mathbf { p } } , \boldsymbol { \mathbf { q } } ) } } } & { { = } } & { { \left( \mathrm { B } _ { 1 } \mathrm { ~ D } _ { 2 } - \mathrm { ~ B } _ { 2 } \mathrm { ~ D } _ { 1 } \right) \cos ^ { 2 } \Omega + \left( A _ { 1 } \mathrm { ~ C } _ { 2 } - A _ { 2 } \mathrm { ~ C } _ { 1 } \right) \sin ^ { 2 } \Omega } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \left( A _ { 1 } \mathrm { ~ D } _ { 2 } + \mathrm { B } _ { 1 } \mathrm { ~ C } _ { 2 } - A _ { 2 } \mathrm { ~ D } _ { 1 } - \mathrm { B } _ { 2 } \mathrm { ~ C } _ { 1 } \right) \sin \Omega \cos \Omega . } } \end{array}
$$

Hence,

$$
[ \bf p , q ] = A _ { 1 } C _ { 2 } - A _ { 2 } C _ { 1 } + B _ { 1 } D _ { 2 } - B _ { 2 } D _ { 1 } + { \frac { \partial ( Z , \dot { Z } ) } { \partial ( p , q ) } } .
$$

Now,

$$
\begin{array} { r c l } { { \lambda _ { 1 } { \bf C } _ { 2 } - { \bf A } _ { 2 } { \bf C } _ { 1 } } } & { { = } } & { { \displaystyle \left( { \frac { \partial { \bf x } ^ { \prime } } { \partial { \bf p } } } - { \bf y } ^ { \prime } \frac { \partial \Omega } { \partial { \bf p } } \right) \left( { \frac { \partial \dot { { \bf x } } ^ { \prime } } { \partial { \bf q } } } - { \bf \dot { y } } ^ { \prime } \frac { \partial \Omega } { \partial { \bf q } } \right) } } \\ { { } } & { { } } & { { \displaystyle - \left( { \frac { \partial { \bf x } ^ { \prime } } { \partial { \bf q } } } - { \bf y } ^ { \prime } \frac { \partial \Omega } { \partial { \bf q } } \right) \left( { \frac { \partial \dot { { \bf x } } ^ { \prime } } { \partial { \bf p } } } - { \bf \dot { y } } ^ { \prime } \frac { \partial \Omega } { \partial { \bf p } } \right) } } \\ { { } } & { { } } &  { \displaystyle = \ { \frac { \partial ( { \bf x } ^ { \prime } , \dot { \bf x } ^ { \prime } ) } { \partial ( { \bf p } , { \bf q } ) } + \left( - { \bf y } ^ { \prime } \frac { \partial \dot { \bf x } ^ { \prime } } { \partial { \bf q } } + { \bf \dot { y } } ^ { \prime } \frac { \partial { \bf x } ^ { \prime } } { \partial { \bf q } } \right) \frac { \partial \Omega } { \partial { \bf p } } + \left( - { \bf \dot { y } } ^ { \prime } \frac { \partial { \bf x } ^ { \prime } } { \partial { \bf p } } + { \bf y } ^ { \prime } \frac { \partial \dot { \bf x } ^ { \prime } } { \partial { \bf p } } \right) \frac { \partial \Omega } { \partial { \bf p } } . } } \end{array}
$$

Similarly,

$$
\begin{array} { r c l } { { \mathrm { D } _ { 2 } - \mathrm { B } _ { 2 } \mathrm { D } _ { 1 } } } & { { = } } & { { \displaystyle \left( { \frac { \partial \mathbf { y } ^ { \prime } } { \partial \mathbf { p } } } + x ^ { \prime } { \frac { \partial \Omega } { \partial \mathbf { p } } } \right) \left( { \frac { \partial \dot { \mathbf { y } } ^ { \prime } } { \partial \mathbf { q } } } + \dot { x } ^ { \prime } { \frac { \partial \Omega } { \partial \mathbf { q } } } \right) } } \\ { { } } & { { } } & { { \displaystyle - \left( { \frac { \partial \mathbf { y } ^ { \prime } } { \partial \mathbf { q } } } + x ^ { \prime } { \frac { \partial \Omega } { \partial \mathbf { q } } } \right) \left( { \frac { \partial \dot { \mathbf { y } } ^ { \prime } } { \partial \mathbf { p } } } + \dot { x } ^ { \prime } { \frac { \partial \Omega } { \partial \mathbf { p } } } \right) } } \\ { { } } & { { = } } & { { \displaystyle { \frac { \partial ( \mathbf { y } ^ { \prime } , \dot { \mathbf { y } } ^ { \prime } ) } { \partial ( \mathbf { p } , \mathbf { q } ) } } + \left( x ^ { \prime } { \frac { \partial \dot { \mathbf { y } } ^ { \prime } } { \partial \mathbf { q } } } - \dot { x } ^ { \prime } { \frac { \partial \mathbf { y } ^ { \prime } } { \partial \mathbf { q } } } \right) { \frac { \partial \Omega } { \partial \mathbf { p } } } + \left( \dot { x } ^ { \prime } { \frac { \partial \mathbf { y } ^ { \prime } } { \partial \mathbf { p } } } - { { \bf x } ^ { \prime } } { \frac { \partial \dot { \mathbf { y } } ^ { \prime } } { \partial \mathbf { p } } } \right) { \frac { \partial \Omega } { \partial \mathbf { q } } } . } } \end{array}
$$

Let

$$
[ \mathfrak { p } , { \mathfrak { q } } ] ^ { \prime } = \frac { \partial ( x ^ { \prime } , \dot { x } ^ { \prime } ) } { \partial ( \mathfrak { p } , { \mathfrak { q } } ) } + \frac { \partial ( \mathfrak { y } ^ { \prime } , \dot { \mathfrak { y } } ^ { \prime } ) } { \partial ( \mathfrak { p } , { \mathfrak { q } } ) } + \frac { \partial ( z ^ { \prime } , \dot { z } ^ { \prime } ) } { \partial ( \mathfrak { p } , { \mathfrak { q } } ) } .
$$

Since $Z = z ^ { \prime }$ and $\dot { Z } = \dot { z } ^ { \prime }$ , it follows that

$$
\begin{array} { l l l } { [ { \bf p } , { \bf q } ] } & { = } & { [ { \bf p } , { \bf q } ] ^ { \prime } + \left( x ^ { \prime } \frac { \partial \dot { \bf y } ^ { \prime } } { \partial { \bf q } } + \dot { \bf y } ^ { \prime } \frac { \partial x ^ { \prime } } { \partial { \bf q } } - { \bf y } ^ { \prime } \frac { \partial \dot { x } ^ { \prime } } { \partial { \bf q } } - \dot { x } ^ { \prime } \frac { \partial { \bf y } ^ { \prime } } { \partial { \bf q } } \right) \frac { \partial \Omega } { \partial { \bf p } } } \\ & & { - \left( x ^ { \prime } \frac { \partial \dot { \bf y } ^ { \prime } } { \partial { \bf p } } + \dot { \bf y } ^ { \prime } \frac { \partial x ^ { \prime } } { \partial { \bf p } } - { \bf y } ^ { \prime } \frac { \partial \dot { x } ^ { \prime } } { \partial { \bf p } } - \dot { x } ^ { \prime } \frac { \partial { \bf y } ^ { \prime } } { \partial { \bf p } } \right) \frac { \partial \Omega } { \partial { \bf q } } } \\ & { = } & { [ { \bf p } , { \bf q } ] ^ { \prime } + \frac { \partial \left( \Omega , x ^ { \prime } \dot { \bf y } ^ { \prime } - { \bf y } ^ { \prime } \dot { x } ^ { \prime } \right) } { \partial \left( { \bf p } , { \bf q } \right) } . } \end{array}
$$

However,

$$
x ^ { \prime } \dot { \mathfrak { y } } ^ { \prime } - \mathfrak { y } ^ { \prime } \dot { x } ^ { \prime } = \mathtt { h } \mathrm { c o s ~ I } = [ \mu \textbf { a } ( 1 - e ^ { 2 } ) ] ^ { 1 / 2 } \mathrm { ~ c o s ~ I } \equiv \mathcal { G } ,
$$

because the left-hand side is the component of the angular momentum along the $z ^ { \prime }$ -axis. Of course, this axis is inclined at an angle I to the $z$ -axis, which is parallel to the angular momentum vector. Thus, we obtain

$$
[ { \mathfrak { p } } , { \mathfrak { q } } ] = [ { \mathfrak { p } } , { \mathfrak { q } } ] ^ { \prime } + { \frac { \partial ( \Omega , { \mathcal { G } } ) } { \partial ( { \mathfrak { p } } , { \mathfrak { q } } ) } } .
$$

Consider a rotation of the coordinate system about the $x ^ { \prime }$ -axis. Let the new coordinate system be $( \mathsf { x } ^ { \prime \prime } , \ \mathsf { y } ^ { \prime \prime } , \ z ^ { \prime \prime } )$ . A rotation through an angle I brings the orbit into the $x ^ { \prime \prime } – y ^ { \prime \prime }$ plane—see Figure 4.4. By analogy with the previous analysis,

$$
[ \mathfrak { p } , \mathfrak { q } ] ^ { \prime } = [ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime } + \frac { \partial ( \mathrm { I } , \mathfrak { y } ^ { \prime \prime } \dot { z } ^ { \prime \prime } - z ^ { \prime \prime } \dot { \mathfrak { y } } ^ { \prime \prime } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } .
$$

However, $z ^ { \prime \prime }$ and $\dot { z } ^ { \prime \prime }$ are both zero, since the orbit lies in the $x ^ { \prime \prime } – y ^ { \prime \prime }$ plane. Hence,

$$
[ { \bf p } , { \bf q } ] ^ { \prime } = [ { \bf p } , { \bf q } ] ^ { \prime \prime } .
$$

Consider, finally, a rotation of the coordinate system about the $z ^ { \prime \prime }$ -axis. Let the final coordinate system be $( x , y , z )$ . A rotation through an angle $\varpi - \Omega$ brings the perihelion to the $x$ -axis—see Figure 4.4. By analogy with the previous analysis,

$$
[ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime } = [ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime \prime } + \frac { \partial ( \varpi - \Omega , x \dot { \mathfrak { y } } - \mathfrak { y } \dot { x } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } .
$$

However,

$$
x \dot { \mathfrak { y } } - \mathfrak { y } \dot { \mathfrak { x } } = \mathtt { h } = [ \mu \textbf { a } ( 1 - e ^ { 2 } ) ] ^ { 1 / 2 } \equiv \mathsf { H } ,
$$

so, from (11.69) and (11.71),

$$
[ \mathfrak { p } , \mathfrak { q } ] = [ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime \prime } + \frac { \partial ( \varpi - \Omega , \mathsf { H } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } + \frac { \partial ( \Omega , \mathcal { G } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } .
$$

It thus remains to calculate

$$
[ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime \prime } = \frac { \partial \mathfrak { x } } { \partial \mathfrak { p } } \frac { \partial \dot { \mathfrak { x } } } { \partial \mathfrak { q } } - \frac { \partial \mathfrak { x } } { \partial \mathfrak { q } } \frac { \partial \dot { \mathfrak { x } } } { \partial \mathfrak { p } } + \frac { \partial \mathfrak { y } } { \partial \mathfrak { p } } \frac { \partial \dot { \mathfrak { y } } } { \partial \mathfrak { q } } - \frac { \partial \mathfrak { y } } { \partial \mathfrak { q } } \frac { \partial \dot { \mathfrak { y } } } { \partial \mathfrak { p } } .
$$

The coordinates $x = \Upsilon \cos { \theta }$ and $y = r \sin \theta$ , where $\boldsymbol { \mathsf { r } }$ is radial distance from the Sun, and θ the true anomaly, are functions of the major radius, $\mathbf { a }$ , the ellipticity, $e _ { \scriptscriptstyle \cdot }$ , and the mean anomaly $\mathcal { M } = \bar { \lambda } _ { 0 } - \varpi + \mathfrak { n } \mathfrak { t }$ . Since the Lagrange brackets are independent of time, it is sufficient to evaluate them at $\mathcal { M } = 0$ : i.e., at the perihelion point. Now, it is easily demonstrated from Equations (4.69)–(4.71) that

$$
\begin{array} { r c l } { \displaystyle x } & { = } & { \displaystyle \mathbf { a } \left( 1 - e \right) + \mathcal { O } ( \mathcal { M } ^ { 2 } ) , } \\ { \displaystyle y } & { = } & { \displaystyle \mathbf { a } \mathcal { M } \left( \frac { 1 + e } { 1 - e } \right) ^ { 1 / 2 } + \mathcal { O } ( \mathcal { M } ^ { 3 } ) , } \\ { \displaystyle \dot { x } } & { = } & { \displaystyle - \mathbf { a } \mathrm { n } \frac { \mathcal { M } } { ( 1 - e ) ^ { 2 } } + \mathcal { O } ( \mathcal { M } ^ { 3 } ) , } \\ { \displaystyle \dot { \mathfrak { y } } } & { = } & { \displaystyle \mathbf { a } \mathrm { n } \left( \frac { 1 + e } { 1 - e } \right) ^ { 1 / 2 } + \mathcal { O } ( \mathcal { M } ^ { 2 } ) } \end{array}
$$

at small $\mathcal { M }$ . Hence, at $\mathcal { M } = 0$ ,

$$
\begin{array} { r l } { \frac { \partial \mathbf { x } } { \partial \mathbf { a } } } & { = \ 1 - \epsilon , } \\ { \frac { \partial \mathbf { x } } { \partial \mathbf { c } } } & { = \ - \mathbf { a } , } \\ { \frac { \partial \mathbf { y } } { \partial ( \lambda _ { \partial } - \mathbf { m } ) } } & { = \ \mathbf { a } \left( \frac { 1 + \epsilon } { 1 - \epsilon } \right) ^ { 1 / 2 } , } \\ { \frac { \partial \mathbf { x } } { \partial ( \lambda _ { \partial } - \mathbf { w } ) } } & { = \ - \frac { \mathbf { a } \mathbf { n } } { \left[ 1 - \epsilon \right] ^ { 2 } } , } \\ { \frac { \partial \hat { \mathbf { y } } } { \partial \mathbf { a } } } & { = \ - \frac { \mathbf { n } } { 2 } \left( \frac { 1 + \epsilon } { 1 - \epsilon } \right) ^ { 1 / 2 } , } \\ { \frac { \partial \hat { \mathbf { u } } } { \partial \mathbf { e } } } & { = \ \mathbf { a } \left( 1 + \epsilon \right) ^ { - 1 / 2 } , } \end{array}
$$

because $\textbf { n } \propto \textbf { a } ^ { - 3 / 2 }$ . All other partial derivatives are zero. Now, since in the $\left( { \mathfrak { x } } , ~ { \mathfrak { y } } , ~ z \right)$ coordinate system the orbit only depends on the elements ${ \mathfrak { a } } , { \mathfrak { e } } _ { \mathrm { : } }$ , and $\bar { \lambda } _ { 0 } - \varpi$ , we can write

$$
\begin{array} { r c l } { { [ { \bf p } , { \bf q } ] ^ { \prime \prime \prime } } } & { { = } } & { { \displaystyle \frac { \partial ( { \bf a } , e ) } { \partial ( { \bf p } , { \bf q } ) } \left[ \frac { \partial ( x , \dot { x } ) } { \partial ( { \bf a } , e ) } + \frac { \partial ( { \bf y } , \dot { { \bf y } } ) } { \partial ( { \bf a } , e ) } \right] } } \\ { { } } & { { } } & { { \displaystyle + \frac { \partial ( e , \bar { \lambda } _ { 0 } - \varpi ) } { \partial ( { \bf p } , { \bf q } ) } \left[ \frac { \partial ( x , \dot { x } ) } { \partial ( e , \bar { \lambda } _ { 0 } - \varpi ) } + \frac { \partial ( { \bf y } , \dot { { \bf y } } ) } { \partial ( e , \bar { \lambda } _ { 0 } - \varpi ) } \right] } } \\ { { } } & { { } } & { { \displaystyle + \frac { \partial ( \bar { \lambda } _ { 0 } - \varpi , { \bf a } ) } { \partial ( { \bf p } , { \bf q } ) } \left[ \frac { \partial ( x , \dot { x } ) } { \partial ( \bar { \lambda } _ { 0 } - \varpi , { \bf a } ) } + \frac { \partial ( \bar { \bf y } , \dot { { \bf y } } ) } { \partial ( \bar { \lambda } _ { 0 } - \varpi , { \bf a } ) } \right] . } } \end{array}
$$

Substitution of the values of the derivatives evaluated at $\mathcal { M } = 0$ into the above expression yields

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial ( x , \dot { x } ) } { \partial ( a , e ) } + \frac { \partial ( { \bf y } , \dot { { \bf y } } ) } { \partial ( a , e ) } } } & { { = } } & { { 0 , } } \\ { { \displaystyle \frac { \partial ( x , \dot { x } ) } { \partial ( e , \bar { \lambda } _ { 0 } - \varpi ) } + \frac { \partial ( { \bf y } , \dot { { \bf y } } ) } { \partial ( e , \bar { \lambda } _ { 0 } - \varpi ) } } } & { { = } } & { { 0 , } } \\ { { \displaystyle \frac { \partial ( x , \dot { x } ) } { \partial ( \bar { \lambda } _ { 0 } - \varpi , { \bf a } ) } + \frac { \partial ( { \bf y } , \dot { { \bf y } } ) } { \partial ( \bar { \lambda } _ { 0 } - \varpi , { \bf a } ) } } } & { { = } } & { { \displaystyle \frac { { \bf a \ n } } { 2 } . } } \end{array}
$$

Thus,

$$
[ \mathfrak { p } , \mathfrak { q } ] ^ { \prime \prime \prime } = \frac { \partial ( \bar { \lambda } _ { 0 } - \varpi , \mathfrak { a } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } \frac { \mathfrak { n } \mathfrak { a } } { 2 } = \frac { \partial ( \bar { \lambda } _ { 0 } - \varpi , \mathfrak { a } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } \frac { \mathfrak { k } ^ { 1 / 2 } } { 2 \mathfrak { a } ^ { 1 / 2 } } = \frac { \partial ( \bar { \lambda } _ { 0 } - \varpi , \mathrm { L } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } ,
$$

where $\mathsf { L } = ( \mu \alpha ) ^ { 1 / 2 }$ . Hence, from (11.74), we obtain

$$
[ \mathfrak { p } , \mathfrak { q } ] = \frac { \partial ( \bar { \lambda } _ { 0 } - \mathfrak {varpi } , \mathrm { L } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } + \frac { \partial ( \varpi - \Omega , \mathsf { H } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } + \frac { \partial ( \Omega , \mathcal { G } ) } { \partial ( \mathfrak { p } , \mathfrak { q } ) } .
$$

# 11.6 Lagrange’s Planetary Equations

Now,

$$
\begin{array} { r c l } { \mathrm { ~ L ~ } } & { = } & { ( \mu \alpha ) ^ { 1 / 2 } , } \\ { \mathrm { ~ H ~ } } & { = } & { [ \mu \alpha ( 1 - e ^ { 2 } ) ] ^ { 1 / 2 } , } \\ { \mathcal { G } } & { = } & { [ \mu \alpha ( 1 - e ^ { 2 } ) ] ^ { 1 / 2 } \cos \mathrm { I } , } \end{array}
$$

and n $\mathbf { a } = ( \mu / \alpha ) ^ { 1 / 2 }$ . Hence,

$$
\begin{array} { r l } { \frac { \partial \mathrm { L } } { \partial \mathbf { a } } } & { = \begin{array} { r l } { \frac { \mathrm { n } \mathrm { a } } { 2 } , } \\ { \frac { \mathrm { n } \mathrm { e } } { 2 } , } \end{array} } \\ { \frac { \partial \mathrm { H } } { \partial \mathbf { a } } } &  = \begin{array} { r l } { \frac { \mathrm { n } \mathrm { a } } { 2 } ( 1 - \mathrm { e } ^ { 2 } ) ^ { 1 / 2 } , } \\ { \frac { \partial \mathrm { H } } { \partial \mathbf { e } } } & { = - \mathrm { n } \mathrm { a } ^ { 2 } \epsilon ( 1 - \mathrm { e } ^ { 2 } ) ^ { - 1 / 2 } , } \\ { \frac { \partial \mathrm { G } } { \partial \mathbf { a } } } & { = \begin{array} { r l } { \frac { \mathrm { n } \mathrm { a } } { 2 } ( 1 - \mathrm { e } ^ { 2 } ) ^ { 1 / 2 } \mathrm { c o s } \mathrm { I } , } \\ { \frac { \partial \mathrm { G } } { \partial \mathbf { e } } } & { = - \mathrm { n } \mathrm { a } ^ { 2 } \epsilon ( 1 - \mathrm { e } ^ { 2 } ) ^ { - 1 / 2 } \mathrm { c o s } \mathrm { I } , } \end{array} } \\ { \frac { \partial \mathcal { G } } { \partial \mathbf { I } } } & { = \begin{array} { r l } { \frac { \mathrm { n } \mathrm { a } } { 2 } } & { \mathrm { n } \mathrm { a } } \end{array} } \end{array} \end{array}
$$

with all other partial derivatives zero. Thus, from (11.91), the only non-zero Lagrange brackets are

$$
\begin{array} { r l } { \overline { { \lambda } } _ { 0 } , { \bf a } ] = - [ { \bf a } , \overline { { \lambda } } _ { 0 } ] } & { = \ \frac { \mathrm { \bf { n } } \mathrm { \bf { a } } } { 2 } , } \\ { \left[ \overline { { \lambda } } , { \bf a } \right] = - [ { \bf a } , \overline { { \Omega } } ] } & { = \ - \frac { \mathrm { \bf { n } } \mathrm { \bf { a } } } { 2 } [ 1 - \bigl ( 1 - \mathrm { \bf { e } } ^ { 2 } \bigr ) ^ { 1 / 2 } ] , } \\ { \left[ { \Omega } , { \bf a } \right] = - [ { \bf a } , \Omega ] } & { = \ - \frac { \mathrm { \bf { n } } \mathrm { \bf { a } } } { 2 } ( 1 - \mathrm { \bf { e } } ^ { 2 } ) ^ { 1 / 2 } ( 1 - \cos { \Omega } ] , } \\ { \left[ \overline { { \alpha } } , { \bf e } \right] = - [ { \bf e } , \overline { { \Omega } } ] } & { = \ - \mathrm { \bf { n } } \mathrm { \bf { a } } ^ { 2 } e ( 1 - \mathrm { \bf { e } } ^ { 2 } ) ^ { - 1 / 2 } , } \\ { \left[ { \Omega } , { \bf e } \right] = - [ { \bf e } , \Omega ] } & { = \ \mathrm { \bf { n } } \mathrm { \bf { a } } ^ { 2 } e ( 1 - \mathrm { \bf { e } } ^ { 2 } ) ^ { - 1 / 2 } ( 1 - \cos { \Omega } ] , } \\ { \left[ { \Omega } , \mathrm { \bf { I } } \right] = - [ { \bf { I } } , \Omega ] } & { = \ - \mathrm { \bf { n } } \mathrm { \bf { a } } ^ { 2 } ( 1 - \mathrm { \bf { e } } ^ { 2 } ) ^ { 1 / 2 } \sin { \mathrm { I } } . } \end{array}
$$

Hence, Equations (11.39) yield

$$
\begin{array} { r l } { | \mathbf { a } , \bar { \mathbf { b } } _ { 0 } | \displaystyle { \frac { \mathrm { d } \bar { \mathbf { b } } _ { 0 } } { \mathrm { d t } } } + [ \mathbf { a } , \varpi ] \displaystyle { \frac { \mathrm { d } \varpi } { \mathrm { d t } } } + [ \mathbf { a } , \Omega ] \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \mathbf { a } } } , } \\ { [ \mathbf { e } , \varpi ] \displaystyle { \frac { \mathrm { d } \varpi } { \mathrm { d t } } } + [ \mathbf { e } , \Omega ] \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \mathbf { e } } } , } \\ { | \bar { \mathbf { b } } _ { 0 } , \mathbf { a } | \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \bar { \mathbf { b } } _ { 0 } } } , } \\ { | \mathbf { I } , \Omega | \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \mathbf { I } } } , } \\ { [ \Omega , \mathfrak { a } ] \displaystyle { \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } + [ \Omega , \mathfrak { e } ] \displaystyle { \frac { \mathrm { d } \Gamma } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \Omega } } , } \\ { [ \varpi , \mathfrak { a } ] \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } + [ \varpi , \mathfrak { a } ] \displaystyle { \frac { \mathrm { d } \Omega } { \mathrm { d t } } } } & { = \displaystyle { \frac { \partial \mathbf { R } } { \partial \Omega } } . } \end{array}
$$

Finally, Equations (11.101)–(11.112) can be rearranged to give

$$
\begin{array} { r l } & { \frac { \mathrm { d } a } { \mathrm { d t } } = \mathrm { ~ \frac { 2 } { n n } ~ } \frac { \partial R } { \partial \lambda _ { \mathrm { v } } } , } \\ & { \frac { \mathrm { d } e } { \mathrm { d t } } = \mathrm { ~ - ~ } \frac { [ 1 - e ^ { 2 } ] ^ { 1 / 2 } } { n \mathfrak { a } ^ { 2 } \mathfrak { e } } [ 1 - ( 1 - e ^ { 2 } ) ^ { 1 / 2 } ] \frac { \partial \mathcal { R } } { \partial \lambda _ { \mathrm { v } } } - \frac { [ 1 - e ^ { 2 } ] ^ { 1 / 2 } } { n \mathfrak { a } ^ { 2 } \mathfrak { e } } \frac { \partial R } { \partial \mathfrak { c } } , } \\ & { \frac { \mathrm { d } \bar { \lambda } _ { \mathrm { v } } } { \mathrm { d t } } = \mathrm { ~ - ~ } \frac { 2 } { n \mathfrak { a } } \frac { \partial R } { \partial \mathfrak { a } } + \frac { [ 1 - e ^ { 2 } ] ^ { 1 / 2 } [ 1 - ( 1 - e ^ { 2 } ) ^ { 1 / 2 } ] } { n \mathfrak { a } ^ { 2 } \mathfrak { e } } \frac { \partial R } { \partial \mathfrak { c } } } \\ & { \qquad + \frac { \mathrm { d } \mathfrak { a } ( 1 / 2 ) } { n \mathfrak { a } ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } \frac { \partial R } { \partial \mathfrak { t } } , } \\ & { \frac { \mathrm { d } \bar { \mathfrak { I } } } { \mathrm { d t } } = \mathrm { ~ - ~ } \frac { \mathrm { t r a n } ( 1 / 2 ) } { n \mathfrak { a } ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } \left( \frac { \partial \mathcal { R } } { \partial \lambda _ { \mathrm { v } } } + \frac { \partial \mathcal { R } } { \partial \mathfrak { a } } \right) - \frac { ( 1 - e ^ { 2 } ) ^ { - 1 / 2 } } { n \mathfrak { a } ^ { 2 } \sin { T } } \frac { \partial \mathcal { R } } { \partial \Omega } , } \\ &  \frac { \mathrm { d } \bar { \Omega } } { \mathrm { d t } } = \mathrm { ~ \frac { 1 } { n \mathfrak { a } ^ { 2 } [ 1 - e ^ { 2 } ] ^ { 1 / 2 } } \sin { \frac { \partial \mathcal { R } } { \partial \mathfrak { I } } } , } \end{array}
$$

$$
\frac { \mathrm { d } \varpi } { \mathrm { d t } } = \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { { \textrm { n a } } ^ { 2 } e } \frac { \partial \mathcal { R } } { \partial e } + \frac { \tan ( \mathrm { I } / 2 ) } { { \textrm { n a } } ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } \frac { \partial \mathcal { R } } { \partial \mathrm { I } } .
$$

Equations (11.113)–(11.118), which specify the time evolution of the osculating orbital elements of the first planet due to the disturbing influence of the second, are known collectively as Lagrange’s planetary equations. Obviously, there is an analogous set of equations, involving primed quantities, that specify the time evolution of the osculating elements of the second planet due to the influence of the first.

# 11.7 Transformation of Lagrange’s Equations

It can be seen, from Equations (11.113)–(11.118), that in the limit of small eccentricity, e, and small inclination, I, certain terms on the right-hand sides of Lagrange’s equations become singular. This problem can be alleviated by defining the alternative orbital elements,

$$
\begin{array} { l r c l } { \mathbf { h } } & { = } & { e \sin \varpi , } \\ { \mathbf { k } } & { = } & { e \cos \varpi , } \\ { \mathbf { p } } & { = } & { \sin \mathrm { ~ I ~ } \sin \Omega , } \\ { \mathbf { q } } & { = } & { \sin \mathrm { ~ I ~ } \cos \Omega . } \end{array}
$$

If we write Lagrange’s equations in terms of these new elements, we obtain

$$
\begin{array} { r l } { \frac { d C } { d t } } & { = \frac { 2 } { \pi n + 4 } \frac { \partial C } { \partial x } , } \\ { \frac { d S } { d t } } & { = - \frac { 2 } { \pi n } \frac { \partial C } { \partial x } - \frac { ( 1 - e ^ { - \theta } ) ^ { 2 } ( 2 ) } { \pi e ^ { 2 } } \left( \frac { n \overline { { \mathcal { K } } } } { \partial x } - \frac { n \overline { { \mathcal { K } } } } { \partial x } \right) , } \\ { \frac { d S } { d t } } & { = - \frac { 2 } { \pi n } \frac { \partial C } { \partial x } - \frac { \partial C } { \partial x } , } \\ & { + \frac { 2 } { \pi n \overline { { \mathcal { K } } } } \frac { \partial C } { \partial x } \frac { \partial C } { \partial x } \frac { \partial } { \partial x } \frac { \partial } { \partial x } \left( e ^ { - \theta } \frac { \partial \overline { { \mathcal { K } } } } { \partial y } - \frac { \partial \overline { { \mathcal { K } } } } { \partial x } \right) , } \\ { \frac { d C } { d t } } & { = - \frac { 2 } { \pi n + 4 } \frac { \theta } { \pi n } \frac { \partial C } { \partial x } \frac { \partial } { \partial x } \frac { \partial } { \partial x } - \frac { \partial \overline { { \mathcal { K } } } } { \partial x } \frac { \partial } { \partial x } \frac { \partial } { \partial y } \frac { \partial } { \partial x } } \\ & { + \frac { 2 } { \pi n \overline { { \mathcal { K } } } } \frac { \partial C } { \partial x } \frac { \partial \overline { { \mathcal { K } } } } { \partial y } \frac { \partial } { \partial x } \left\{ \partial y \right\} \frac { \partial } { \partial y } \frac { \partial } { \partial y } + \frac { \partial \overline { { \mathcal { K } } } } { \partial y } } ,  \\ { \frac { d S } { d t } } & { = - \frac { 2 } { \pi n \overline { { \mathcal { K } } } } \frac { \partial C } { \partial x } \frac { \partial } { \partial x } \frac { \partial } { \partial x } \frac { \partial } { \partial y } \frac { \partial } { \partial x } \frac { \partial } { \partial y } \frac { \partial } { \partial x } \frac { \partial } { \partial y } } \\ &  - \frac { 2 } { \pi n \overline { { \mathcal { K } } } ^ { 2 } } \frac { \partial } { \partial x } \frac { \partial } { \partial x } \frac { \partial }  \partial x \end{array}
$$

$$
\begin{array} { r l } & { + \frac { \cos { \mathrm { I } } } { \mathfrak { n } \mathfrak { a } ^ { 2 } \left( 1 - \mathfrak { e } ^ { 2 } \right) ^ { 1 / 2 } } \frac { \partial \mathcal { R } } { \partial \mathfrak { q } } , } \\ { \frac { \mathrm { d } \mathfrak { q } } { \mathrm { d t } } } & { = \begin{array} { c } { \cos { \mathrm { I } } } \\ { - \frac { 2 \mathfrak { n } \mathfrak { a } ^ { 2 } \cos ^ { 2 } ( \mathrm { I } / 2 ) \left( 1 - \mathfrak { e } ^ { 2 } \right) ^ { 1 / 2 } } { \mathfrak { n } \mathfrak { a } ^ { 2 } \left( 1 - \mathfrak { e } ^ { 2 } \right) ^ { 1 / 2 } } \mathfrak { q } \left( \frac { \partial \mathcal { R } } { \partial \bar { \lambda } _ { 0 } } + \mathtt { k } \frac { \partial \mathcal { R } } { \partial \mathfrak { h } } - \mathrm { h } \frac { \partial \mathcal { R } } { \partial \mathtt { k } } \right) } \end{array} } \\ & { \quad - \frac { \cos { \mathrm { I } } } { \mathfrak { n } \mathfrak { a } ^ { 2 } \left( 1 - \mathfrak { e } ^ { 2 } \right) ^ { 1 / 2 } } \frac { \partial \mathcal { R } } { \partial \mathfrak { p } } . } \end{array}
$$

Note that the transformed equations now contain no singular terms in the limit $e , \operatorname { I } \to 0$ .

As we shall see in Section 11.9, the disturbing function takes the form $\mathcal { R } ( \mathbf { a } , \mathrm { h } , \mathrm { k } , \mathrm { p } , \mathbf { q } , \bar { \lambda } )$ where $\bar { \lambda } = \bar { \lambda } _ { 0 } + { \mathfrak { n } } \mathfrak { t }$ . It follows that

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial { \mathcal R } } { \partial \bar { \lambda } _ { 0 } } } } } & { { = } } & { { \displaystyle { \frac { \partial { \mathcal R } } { \partial \bar { \lambda } } } , } } \\ { { \displaystyle { \frac { \partial { \mathcal R } } { \partial { \bf a } } } } } & { { = } } & { { \displaystyle { \frac { \partial { \mathcal R } } { \partial { \bf a } } } + \frac { \partial { \mathcal R } } { \partial \bar { \lambda } } \displaystyle { \frac { \mathrm { d n } } { \mathrm { d a } } } { \bf t } . } } \end{array}
$$

The explicit factor t appearing in the above equation is problematic. Fortunately, it can easily be eliminated by replacing the variable $\bar { \lambda } _ { 0 }$ by $\bar { \lambda }$ . In this scheme, Equations (11.123) and (11.124) transform to

$$
\begin{array} { r l } { \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } & { = \mathrm { ~ \displaystyle ~ \frac { 2 } { { n } \mathbf { a } } ~ } \frac { \partial \mathcal { R } } { \partial \bar { \lambda } } , } \\ { \frac { \mathrm { d } \bar { \lambda } } { \mathrm { d t } } } & { = \mathrm { ~ } { \displaystyle n - \frac { 2 } { { n } \mathbf { a } } ~ } \frac { \partial \mathcal { R } } { \partial \mathbf { a } } + \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { { n } \mathbf { a } ^ { 2 } [ 1 + ( 1 - e ^ { 2 } ) ^ { 1 / 2 } ] } \left( { \mathrm { h } } \frac { \partial \mathcal { R } } { \partial \mathrm { h } } + { \mathrm k } \frac { \partial \mathcal { R } } { \partial \mathrm { k } } \right) } \\ & { + \frac { \cos { \mathrm { I } } } { 2 \mathrm { ~ } { \mathrm { n } \mathbf { a } } ^ { 2 } \cos ^ { 2 } [ [ / 2 ] \left( 1 - e ^ { 2 } \right) ^ { 1 / 2 } } \left( { \mathrm p } \frac { \partial \mathcal { R } } { \partial \mathrm { p } } + { \mathrm q } \frac { \partial \mathcal { R } } { \partial \mathrm { q } } \right) , } \end{array}
$$

respectively, where $\partial / \partial { \bar { \lambda } }$ is taken at constant $\mathbf { a }$ , and $\partial / \partial { \mathfrak { a } }$ at constant $\bar { \lambda }$

# 11.8 Expansion of Lagrange’s Equations

According to expression (11.8), the first planet’s disturbing function can be written in the form

$$
\mathcal { R } = \frac { \tilde { \mu } ^ { \prime } } { \mathbf { a } ^ { \prime } } \mathcal { S } ,
$$

where $\boldsymbol { \mathcal { S } }$ is $\mathcal { O } ( 1 )$ . Thus, since $\mu = \mathsf { n } ^ { 2 } \mathsf { a } ^ { 3 }$ , Lagrange’s equations for the first planet reduce to

$$
\begin{array} { r c l } { \displaystyle \frac { \mathrm { d } \ln \mathrm { a } } { \mathrm { d t } } } & { = } & { \displaystyle 2 \mathsf { n } \epsilon ^ { \prime } \alpha \frac { \partial S } { \partial \bar { \lambda } } , } \\ { \displaystyle \frac { \mathrm { d } \bar { \lambda } } { \mathrm { d t } } } & { = } & { \displaystyle \mathsf { n } - 2 \mathsf { n } \epsilon ^ { \prime } \alpha ^ { 2 } \frac { \partial S } { \partial \alpha } + \frac { \mathsf { n } \epsilon ^ { \prime } \alpha ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { [ 1 + ( 1 - e ^ { 2 } ) ^ { 1 / 2 } ] } \left( \mathsf { h } \frac { \partial S } { \partial \mathsf { h } } + \mathsf { k } \frac { \partial S } { \partial \mathsf { k } } \right) } \end{array}
$$

$$
+ \frac { \mathfrak { n } \ : \epsilon ^ { \prime } \alpha \ : \cos \mathrm { I } } { 2 \ : \cos ^ { 2 } ( \mathrm { I } / 2 ) \left( 1 \ : - \ : e ^ { 2 } \right) ^ { 1 / 2 } } \left( \mathfrak { p } \ : \frac { \partial S } { \partial \mathfrak { p } } + \mathfrak { q } \ : \frac { \partial S } { \partial \mathfrak { q } } \right) ,
$$

$$
\begin{array} { r l } { \frac { \Delta \tau } { 2 \Delta z } } & { = \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) } \frac { \partial \Delta \tau } { \partial z } - \epsilon _ { 2 } \epsilon _ { 2 } \epsilon _ { 3 } } \\ { \frac { \Delta \tau } { 2 \Delta z } } & { = \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1 / 2 , 1 ) } \frac { \partial \Delta \tau } { \partial z } - \epsilon _ { 3 } ( \epsilon _ { 1 } / 1 - \epsilon _ { 1 } ^ { \prime \prime } ) \frac { \partial \Delta \tau } { \partial z } } \\ & { \qquad \quad + \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1 / 2 , 1 ) } } \\ { \frac { \Delta \tau } { 2 \Delta z } } & { = \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1 / 2 , 1 ) } \frac { \partial \lambda } { \partial z } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } ^ { \prime \prime } \epsilon _ { 1 } ^ { \prime \prime } \epsilon _ { 1 } ^ { \prime \prime } } \\ { \frac { \Delta \tau } { 2 \Delta z } } & { = \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1 / 2 , 1 ) } \frac { \partial \lambda } { \partial z } - \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } \epsilon _ { 1 } ^ { \prime \prime } \epsilon _ { 1 } ^ { \prime \prime } \frac { \partial \Delta \tau } { \partial z } } \\ & { \qquad \quad - \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) } { \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1 / 2 , 1 ) } \frac { \partial \lambda } { \partial z } \epsilon _ { 2 } \frac { \partial \Delta \tau } { \partial z } } \\ &  \qquad \quad - \frac { \eta \alpha \epsilon _ { 1 } ( 1 / 2 , 1 ) }  \epsilon _ { 1 } ( 1 / 2 , 1 ) \epsilon _ { 1 } ( 1  \end{array}
$$

Here,

$$
\begin{array} { l } { { \epsilon ^ { \prime } = \displaystyle \frac { \mathfrak { m } ^ { \prime } } { M + \mathfrak { m } } , } } \\ { { \alpha = \displaystyle \frac { \mathfrak { a } } { \mathfrak { a } ^ { \prime } } . } } \end{array}
$$

Now, the Sun is much more massive than any planet in the Solar System. It follows that the parameter $\epsilon ^ { \prime }$ is very small compared to unity. Expansion of Equations (11.134)– (11.139) to first-order in $\epsilon ^ { \prime }$ yields

$$
\bar { \lambda } ( \mathbf { t } ) = \bar { \lambda } _ { 0 } + \mathfrak { n } \mathbf { t } + \bar { \lambda } ^ { ( 1 ) } ( \mathbf { t } ) ,
$$

where $\lambda ^ { ( 1 ) } \sim \mathcal { O } ( \epsilon ^ { \prime } )$ , and

$$
\begin{array} { r c l } { { { \displaystyle \frac { \mathrm { d } \mathrm { a } } { \mathrm { d t } } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ 2 \alpha { \displaystyle \frac { \partial S } { \partial \bar { \lambda } ^ { ( 0 ) } } } \right] , } } \\ { { { \displaystyle \frac { \mathrm { d } \bar { \lambda } ^ { ( 1 ) } } { \mathrm { d t } } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { 3 } { 2 } \mathrm { a } - 2 \alpha ^ { 2 } \frac { \partial S } { \partial \alpha } + \frac { \alpha ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { [ 1 + ( 1 - e ^ { 2 } ) ^ { 1 / 2 } ] } \left( \mathrm { h } \frac { \partial S } { \partial \mathrm { h } } + \mathrm { k } \frac { \partial S } { \partial \mathrm { k } } \right) \right. } } \\ { { } } & { { } } & { { \left. + \frac { \alpha \cos \mathrm { I } } { 2 \cos ^ { 2 } ( \mathrm { I } / 2 ) ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } \left( \mathrm { p } \frac { \partial S } { \partial \mathrm { p } } + \mathrm { q } \frac { \partial S } { \partial \mathrm { q } } \right) \right] , } } \end{array}
$$

$$
\begin{array} { r l } { \frac { \mathrm { d } \mathbf { h } } { \mathrm { d } t } } &  = \mathrm { ~ } \mathrm { e ~ n } { \Bigg [ \displaystyle - \frac { ( 1 - e ^ { - \sigma / 2 } ) ^ { 2 } } { | \mathbf { \sigma } | \cdot | \mathbf { \sigma } | ^ { 2 } + | \mathbf { \sigma } | ^ { 2 } } \frac { h \mathrm { d } \mathbf { x } } { \mathrm { d } t } - \mathrm { a } 1 1 - e ^ { - \sigma / 2 } \mathrm { ~ s } \overline { { \mathbf { a } } } \mathbf { x } } \\ & { \qquad \mathrm { ~ } - \frac { \mathrm { v } } { 2 \sigma \sigma \sigma \sigma \sigma \sigma \cdot [ ( 1 - e ^ { - \sigma / 2 } ) ] ^ { 2 } } \left( \frac { h \mathrm { d } \mathbf { x } } { \mathrm { d } t } - \mathrm { a } 1 \overline { { \mathbf { a } } } \overline { { \mathbf { a } } } \overline { { \mathbf { b } } } \right) \cdot \frac { \mathrm { d } \mathbf { x } } { \mathrm { d } t } } \\ & { \qquad \mathrm { ~ } - \frac { \mathrm { v } } { 2 \sigma \sigma \sigma \sigma \sigma \cdot [ ( 1 - e ^ { - \sigma / 2 } ) ] ^ { 2 } + | \mathbf { \sigma } | \cdot | \mathbf { \sigma } | ^ { 2 } + | \mathbf { \sigma } | ^ { 2 } } \left( \frac { h \mathrm { d } \mathbf { x } } { \mathrm { d } t } - \mathrm { a } 1 \overline { { \mathbf { a } } } \overline { { \mathbf { a } } } \overline { { \mathbf { b } } } \right) \cdot \ } \\ { \mathrm { ~ d } \mathbf { i } } & { = \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \sigma { ~ } { \Bigg [ \frac { - 1 } { \sigma } + | \mathbf { \sigma } | \cdot \sigma } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } { \sigma | \cdot } } \\ &  \qquad \mathrm { ~ } - \frac { \mathrm { v } }  2 \sigma \sigma \sigma \cdot [ ( 1 - e ^ { - \sigma / 2 } ) ] ^ { 2 } + | \mathbf { \sigma } | \cdot | \sigma | \cdot | \sigma | \cdot | \sigma \end{array}
$$

where $\bar { \lambda } ^ { ( 0 ) } = \bar { \lambda } _ { 0 } + { \mathfrak n } \mathfrak t$ . In the following, for ease of notation, $\bar { \lambda } ^ { ( 0 ) }$ is written simply as $\bar { \lambda }$

It can be seen from Table 4.1 that the Planets all possess orbits whose eccentricities, $e$ , and inclinations, I (in radians), are small compared to unity, but large compared to the ratio of any planetary mass to that of the Sun. It follows that

$$
1 \gg e , 1 \gg \epsilon ^ { \prime } ,
$$

which is our fundamental ordering of small quantities. Assuming that $\mathrm { I } \sim \mathcal { O } ( e )$ , we can perform a secondary expansion in the small parameter e. It turns out that when the disturbing function is expanded to second-order in e it takes the general form (see Section 11.9)

$$
S = S _ { 0 } ( \alpha , \bar { \lambda } ) + S _ { 1 } ( \alpha , \bar { \lambda } , { \bf h } , { \bf k } ) + S _ { 2 } ( \alpha , \bar { \lambda } , { \bf h } , { \bf k } , { \bf p } , { \bf q } ) .
$$

Here, $S _ { \mathrm { n } }$ is $\mathcal { O } ( e ^ { \mathfrak { n } } )$ . So, if we expand the right-hand sides of Equations (11.143)–(11.148) to first-order in $e$ then we obtain

$$
\begin{array} { r c l } { { \displaystyle \frac { \mathrm { d } \mathrm { a } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon ^ { \prime } \mathrm { n } \left[ 2 \alpha \frac { \partial ( S _ { 0 } + S _ { 1 } ) } { \partial \bar { \lambda } } \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \bar { \lambda } ^ { ( 1 ) } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { 3 } { 2 } \mathrm { a } - 2 \alpha ^ { 2 } \frac { \partial ( S _ { 0 } + S _ { 1 } ) } { \partial \alpha } + \alpha \left( \mathrm { h } \frac { \partial S _ { 1 } } { \partial \mathrm { h } } + \mathrm { k } \frac { \partial S _ { 1 } } { \partial \mathrm { k } } \right) \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \mathrm { h } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon ^ { \prime } \mathrm { n } \left[ - \alpha \mathrm { h } \frac { \partial S _ { 0 } } { \partial \bar { \lambda } } + \alpha \frac { \partial ( S _ { 1 } + S _ { 2 } ) } { \partial \mathrm { k } } \right] , } } \end{array}
$$

$$
\begin{array} { r c l } { { { \displaystyle \frac { \mathrm { d } \mathrm { k } } { \mathrm { d t } } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \alpha \mathrm { k } \frac { \partial S _ { 0 } } { \partial \bar { \lambda } } - \alpha \frac { \partial ( S _ { 1 } + S _ { 2 } ) } { \partial \mathrm { h } } \right] , } } \\ { { { \displaystyle \frac { \mathrm { d } \mathrm { p } } { \mathrm { d t } } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { \alpha } { 2 } \mathrm { p } \frac { \partial S _ { 0 } } { \partial \bar { \lambda } } + \alpha \frac { \partial S _ { 2 } } { \partial \mathrm { q } } \right] , } } \\ { { { \displaystyle \frac { \mathrm { d } \mathrm { q } } { \mathrm { d t } } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { \alpha } { 2 } \mathrm { q } \frac { \partial S _ { 0 } } { \partial \bar { \lambda } } - \alpha \frac { \partial S _ { 2 } } { \partial \mathrm { p } } \right] . } } \end{array}
$$

Note that $\mathbf { h } , \mathbf { k } , \mathbf { p } , \mathbf { q }$ are $\mathcal O ( e )$ , whereas $\propto$ and $\bar { \lambda }$ are $\mathcal { O } ( 1 )$ .

Analogous arguments reveal that Lagrange’s equations for the orbital elements of the second planet take the form

$$
\begin{array} { r l } { \frac { \mathrm { d } \mathrm { d } \mathfrak { c ^ { \prime } } } { \mathrm { d t } } } & { = \mathrm { e n ^ { \prime } } [ 2 \alpha ^ { - 1 } \frac { \partial ( S _ { + } ^ { \prime } - S _ { 1 } ^ { \prime } ) } { \partial \lambda ^ { \prime } } ] , } \\ { \frac { \mathrm { d } \overline { { \lambda } } ^ { \mathrm { ( i ) ^ { \prime } } } } { \mathrm { d t } } } & { = \mathrm { e n ^ { \prime } } [ - \frac { 3 } { 2 } \alpha ^ { \prime } + 2 \frac { \partial ( S _ { + } ^ { \prime } + S _ { 1 } ^ { \prime } ) } { \partial \alpha } + \alpha ^ { - 1 } ( \mathrm { h } ^ { \prime } \frac { \partial S _ { 1 } ^ { \prime } } { \partial \mathrm { h ^ { \prime } } } + \mathrm { k ^ { \prime } } \frac { \partial S _ { 1 } ^ { \prime } } { \partial \mathrm { k ^ { \prime } } } ) ] , } \\ { \frac { \mathrm { d } \overline { { \lambda } } ^ { \mathrm { ( r ) } } } { \mathrm { d t } } } & { = \mathrm { e n ^ { \prime } } [ - \alpha ^ { - 1 } \mathrm { h } ^ { \prime } \frac { \partial S _ { + } ^ { \prime } } { \partial \overline { { \lambda } } ^ { \prime } } + \alpha ^ { - 1 } \frac { \partial ( S _ { + } ^ { \prime } + S _ { 2 } ^ { \prime } ) } { \partial \overline { { \lambda } } ^ { \prime } } ] , } \\ { \frac { \mathrm { d } \overline { { \lambda } } ^ { \mathrm { ( r ) } } } { \mathrm { d t } } } & { = \mathrm { e n ^ { \prime } } [ - \alpha ^ { - 1 } \mathrm { k } ^ { \prime } \frac { \partial S _ { - } ^ { \prime } } { \partial \overline { { \lambda } } ^ { \prime } } - \alpha ^ { - 1 } \frac { \partial ( S _ { + } ^ { \prime } + S _ { 2 } ^ { \prime } ) } { \partial \mathrm { h ^ { \prime } } } ] , } \\ { \frac { \mathrm { d } \overline { { \lambda } } ^ { \mathrm { ( r ) } } } { \mathrm { d t } } } &  = \mathrm { e n ^ { \prime } } [ - \frac { \alpha ^ { - 1 } \mathrm { p ^ { \prime } } } { 2 } \mathrm { p ^ { \prime } } \frac { \partial S _ { - } ^ { \prime } }  \partial \overline { { \lambda } } ^   \end{array}
$$

Here, all primed quantities have analogous definitions to the corresponding unprimed quantities, and vice versa.

# 11.9 Expansion of Disturbing Function

We now need to evaluate the disturbing functions for both planets, and then expand them to second-order in e, I, $e ^ { \prime }$ , and $\mathrm { I ^ { \prime } }$ . In the following, it is assumed that $\operatorname { I } , e ^ { \prime }$ , $\mathrm { I } ^ { \prime } \sim \mathcal { O } ( e )$ .

The disturbing functions (11.8) and (11.9) can be written $\mathcal { R } = \left( \tilde { \mu } ^ { \prime } / a ^ { \prime } \right) S$ and $\mathcal { R } ^ { \prime } =$ $( \tilde { \mu } / \alpha ) S ^ { \prime }$ , where

$$
\begin{array} { r c l } { { \displaystyle \mathcal { S } } } & { { = } } & { { S _ { \mathrm { D } } + \alpha S _ { \mathrm { E } } , } } \\ { { \displaystyle S ^ { \prime } } } & { { = } } & { { \alpha S _ { \mathrm { D } } + \alpha ^ { - 1 } S _ { \mathrm { I } } . } } \end{array}
$$

Here,

$$
S _ { \mathrm { { D } } } = { \frac { \mathbf { a } ^ { \prime } } { | \mathbf { r } ^ { \prime } - \mathbf { r } | } } ,
$$

and

$$
\begin{array} { r c l } { { \displaystyle { \mathcal S } _ { \mathrm { E } } } } & { { = } } & { { \displaystyle - \left( \frac { \Upsilon } { \ a } \right) \left( \frac { \ a ^ { \prime } } { \Upsilon ^ { \prime } } \right) ^ { 2 } \cos \Psi , } } \\ { { \displaystyle { \mathcal S } _ { \mathrm { I } } } } & { { = } } & { { \displaystyle - \left( \frac { \Upsilon ^ { \prime } } { \ a ^ { \prime } } \right) \left( \frac { \ a } { \Upsilon } \right) ^ { 2 } \cos \Psi . } } \end{array}
$$

In the above, $\psi$ is the angle subtended between the directions of r and $\mathbf { r } ^ { \prime }$ .

Now

$$
\begin{array} { r } { S _ { \mathrm { D } } = { \bf a } ^ { \prime } \left[ { \bf r } ^ { \prime } { } ^ { 2 } - 2 { \bf r } ^ { \prime } { \bf r } \cos \Psi + { \bf r } ^ { 2 } \right] ^ { - 1 / 2 } . } \end{array}
$$

Let

$$
\begin{array} { r c l } { { \zeta } } & { { = } } & { { \displaystyle \frac { \Upsilon - \alpha } { \alpha } , } } \\ { { } } & { { } } & { { } } \\ { { \zeta ^ { \prime } } } & { { = } } & { { \displaystyle \frac { \Upsilon ^ { \prime } - \alpha ^ { \prime } } { \alpha ^ { \prime } } , } } \\ { { } } & { { } } & { { } } \\ { { \delta } } & { { = } } & { { \cos \Psi - \cos ( \vartheta - \vartheta ^ { \prime } ) , } } \end{array}
$$

where $\vartheta = \varpi + \theta$ and $\vartheta ^ { \prime } = \varpi ^ { \prime } + \theta ^ { \prime \prime }$ . Here, $\theta$ and $\theta ^ { \prime }$ are the true anomalies of the first and second planets, respectively. We expect $\zeta$ and $\zeta ^ { \prime }$ to both be $\mathcal O ( e )$ [see Equation (11.181)], and δ to be $\mathcal { O } ( e ^ { 2 } )$ [see Equation (11.191)]. We can write

$$
S _ { \mathrm { D } } = ( 1 + \zeta ^ { \prime } ) ^ { - 1 } \left[ 1 - 2 \tilde { \alpha } \cos ( \vartheta - \vartheta ^ { \prime } ) + \tilde { \alpha } ^ { 2 } - 2 \tilde { \alpha } \delta \right] ^ { - 1 / 2 } ,
$$

where

$$
\tilde { \alpha } = \left( \frac { 1 + \zeta } { 1 + \zeta ^ { \prime } } \right) \alpha .
$$

Expanding in $e$ , and only retaining terms up to $\mathcal { O } ( e ^ { 2 } )$ , we obtain

$$
S _ { \mathrm { { D } } } \simeq ( 1 + \zeta ^ { \prime } ) ^ { - 1 } \left[ { \mathsf { F } } + ( { \tilde { \alpha } } - \alpha ) { \mathsf { D } } { \mathsf { F } } + { \frac { 1 } { 2 } } ( { \tilde { \alpha } } - \alpha ) ^ { 2 } { \mathsf { D } } ^ { 2 } { \mathsf { F } } \right] + \delta \alpha { \mathsf { F } } ^ { 3 } ,
$$

where $\mathrm { D } \equiv \partial / \partial \alpha ,$ and

$$
{ \sf F } ( \alpha , \vartheta - \vartheta ^ { \prime } ) = \frac { 1 } { [ 1 - 2 \alpha \cos ( \vartheta - \vartheta ^ { \prime } ) + \alpha ^ { 2 } ] ^ { 1 / 2 } } .
$$

Hence,

$$
\begin{array} { r c l } { { \displaystyle { \mathcal { S } } _ { \mathrm { D } } } } & { { \simeq } } & { { \displaystyle \bigg [ ( 1 - \zeta ^ { \prime } + \zeta ^ { \prime } { } ^ { 2 } ) + \left( \zeta - \zeta ^ { \prime } - 2 \zeta \zeta ^ { \prime } + 2 \zeta ^ { \prime } { } ^ { 2 } \right) \alpha \mathrm { D } + \frac { 1 } { 2 } ( \zeta ^ { 2 } - 2 \zeta \zeta ^ { \prime } + \zeta ^ { \prime } { } ^ { 2 } ) \alpha } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \delta \alpha \mathrm { F } ^ { 3 } . } } \end{array}
$$

Now, we can expand $\digamma$ and $\mathsf { F } ^ { 3 }$ as Fourier series in $\vartheta - \vartheta ^ { \prime }$ :

$$
\begin{array} { r c l } { { \displaystyle { \sf F } ( \alpha , \vartheta - \vartheta ^ { \prime } ) } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } \sum _ { j = - \infty , \infty } { { \bf b } _ { 1 / 2 } ^ { ( j ) } ( \alpha ) \cos [ { \bf j } ( \vartheta - \vartheta ^ { \prime } ) ] } } , } } \\ { { \displaystyle { \sf F } ^ { 3 } ( \alpha , \vartheta - \vartheta ^ { \prime } ) } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } \sum _ { j = - \infty , \infty } { { \bf b } _ { 3 / 2 } ^ { ( j ) } ( \alpha ) \cos [ { \bf j } ( \vartheta - \vartheta ^ { \prime } ) ] } } , } } \end{array}
$$

where

$$
{ \sf b } _ { s } ^ { ( \mathrm { j ) } } ( \alpha ) = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \frac { \cos ( \mathrm { j } \Psi ) \mathrm { d } \Psi } { [ 1 - 2 \alpha \cos \Psi + \alpha ^ { 2 } ] ^ { s } } .
$$

Incidentally, the $\mathbf { b } _ { s } ^ { ( \mathrm { j } ) }$ are known as Laplace coefficients. Thus,

$$
\begin{array} { r c l } { { S _ { \mathrm { D } } } } & { { \simeq } } & { { \displaystyle \frac { 1 } { 2 } \sum _ { \mathrm { j } = - \infty , \infty } \left\{ \left[ ( 1 - \zeta ^ { \prime } + \zeta ^ { \prime 2 } ) + ( \zeta - \zeta ^ { \prime } - 2 \zeta \zeta ^ { \prime } + 2 \zeta ^ { \prime 2 } ) \alpha \mathrm { D } \right. \right. } } \\ { { } } & { { } } & { { \left. \left. + \displaystyle \frac { 1 } { 2 } ( \zeta ^ { 2 } - 2 \zeta \zeta ^ { \prime } + \zeta ^ { \prime 2 } ) \alpha ^ { 2 } \mathrm { D } ^ { 2 } \right] \mathrm { b } _ { 1 / 2 } ^ { ( \mathrm { j } ) } ( \alpha ) + \delta \alpha \mathrm { b } _ { 3 / 2 } ^ { ( \mathrm { j } ) } ( \alpha ) \right\} \mathrm { c o s } [ \mathrm { j } \left( \vartheta - \vartheta ^ { \prime } \right) ] , } } \end{array}
$$

where D now denotes $\mathrm { d } / \mathrm { d } \alpha$ .

Equation (4.71) gives

$$
\begin{array} { l l l } { { \zeta } } & { { \equiv } } & { { \displaystyle \frac { \Upsilon } { \alpha } - 1 \simeq - e \cos { \mathcal { M } } + \frac { e ^ { 2 } } { 2 } \left( 1 - \cos { 2 \mathcal { M } } \right) } } \\ { { } } & { { } } & { { } } \\ { { \simeq } } & { { - e \cos ( \bar { \lambda } - \varpi ) + \displaystyle \frac { e ^ { 2 } } { 2 } \left[ 1 - \cos ( 2 \bar { \lambda } - 2 \varpi ) \right] } } \end{array}
$$

to $\mathcal { O } ( e ^ { 2 } )$ . Here, $\mathcal { M } = \bar { \lambda } - \varpi$ is the mean anomaly, and $\bar { \lambda } = \bar { \lambda } _ { 0 } + { \mathfrak { n } } \mathfrak { t }$ t the mean ecliptic longitude. Obviously, there is an analogous equation for $\zeta ^ { \prime }$ . Moreover, from Equation (4.70), we have

$$
\begin{array} { l l l } { \displaystyle \sin \theta } & { \displaystyle \simeq } & { \sin { \mathcal { M } } + e \sin 2 { \mathcal { M } } + \frac { e ^ { 2 } } { 8 } \left( 9 \sin 3 { \mathcal { M } } - 7 \sin { \mathcal { M } } \right) , } \\ { \displaystyle \cos \theta } & { \displaystyle \simeq } & { \cos { \mathcal { M } } + e \left( \cos 2 { \mathcal { M } } - 1 \right) + \frac { e ^ { 2 } } { 8 } \left( 9 \cos 3 { \mathcal { M } } - 9 \cos { \mathcal { M } } \right) . } \end{array}
$$

Hence,

$$
\begin{array} { r c l } { \cos ( \omega + \theta ) } & { \equiv } & { \cos \omega \cos \theta - \sin \omega \sin \theta } \\ & { \simeq } & { \cos ( \omega + \mathcal { M } ) + e \ \left[ \cos ( \omega + 2 \mathcal { M } ) - \cos \omega \right] } \\ & & { \ + \displaystyle \frac { e ^ { 2 } } { 8 } \left[ - 8 \cos ( \omega + \mathcal { M } ) - \cos ( \omega - \mathcal { M } ) + 9 \ \cos ( \omega + 3 \mathcal { M } ) \right] , } \end{array}
$$

and

$$
\begin{array} { r c l } { \sin ( \omega + \theta ) } & { \equiv } & { \sin \omega \ \cos \theta + \cos \omega \ \sin \theta } \\ & { \simeq } & { \sin ( \omega + \mathcal { M } ) + e \ [ \sin ( \omega + 2 \mathcal { M } ) - \sin \omega ] } \\ & & { \ + \displaystyle \frac { e ^ { 2 } } { 8 } \left[ - 8 \sin ( \omega + \mathcal { M } ) + \sin ( \omega - \mathcal { M } ) + 9 \sin ( \omega + 3 \mathcal { M } ) \right] . } \end{array}
$$

Thus, Equations (4.79)–(4.81) yield

$$
\begin{array} { r l } { \frac { \boldsymbol { \Upsilon } } { \tau } } & { \simeq \ \cos ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) + \epsilon \left[ \cos ( \omega + \boldsymbol { \Omega } + 2 \boldsymbol { \mathcal { M } } ) - \cos ( \omega + \boldsymbol { \Omega } ) \right] } \\ & { \quad + \frac { \epsilon ^ { 2 } } { 8 } \left| 9 \cos ( \omega + \boldsymbol { \Omega } + 3 \boldsymbol { \mathcal { M } } ) - \cos ( \omega + \boldsymbol { \Omega } - \boldsymbol { \mathcal { M } } ) - \ \delta \cos ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) \right| } \\ & { \quad + s ^ { 2 } \left[ \cos ( \omega - \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) - \cos ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) \right] , } \\ { \frac { \boldsymbol { \Upsilon } } { \tau } } & { \simeq \ \sin ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) + \epsilon \left[ \sin ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) - \sin ( \omega + \boldsymbol { \Omega } ) \right] } \\ & { \quad + \frac { \epsilon ^ { 2 } } { 8 } \left| 9 \sin ( \omega + \boldsymbol { \Omega } + 3 \boldsymbol { \mathcal { M } } ) - \sin ( \omega + \boldsymbol { \Omega } - \boldsymbol { \mathcal { M } } ) - \vartheta \sin ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) \right| } \\ & { \quad - s ^ { 2 } \left[ \sin ( \omega - \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) + \sin ( \omega + \boldsymbol { \Omega } + \boldsymbol { \mathcal { M } } ) \right] , } \\ { \frac { \boldsymbol { \mathcal { Q } } } { \tau } } & { \simeq \ 2 s \sin ( \omega + \boldsymbol { \mathcal { M } } ) + 2 \epsilon s \left[ \sin ( \omega + 2 \boldsymbol { \mathcal { M } } ) - \sin \omega \right] , } \end{array}
$$

where $s \equiv \sin ( \mathrm { I } / 2 )$ is assumed to be $\mathcal O ( e )$ . Here, X, Y, Z are the Cartesian component of r. There are, of course, completely analogous expressions for the Cartesian components of $\mathbf { r } ^ { \prime }$ .

Now,

$$
\cos \Psi = { \frac { \chi } { r } } { \frac { X ^ { \prime } } { \Gamma ^ { \prime } } } + { \frac { \Upsilon } { r } } { \frac { \Upsilon ^ { \prime } } { \Gamma ^ { \prime } } } + { \frac { Z } { r } } { \frac { Z ^ { \prime } } { \Gamma ^ { \prime } } } ,
$$

so

$$
\begin{array} { r c l } { { \cos \mathfrak { s } \mathfrak { s } \mathfrak { s } } } & { { \simeq } } & { { ( 1 - { \bf e } ^ { 2 } - { \bf e } ^ { \prime 2 } - { \bf s } ^ { 2 } - { \bf s } ^ { \prime 2 } ) \cos ( \bar { \lambda } - \bar { \lambda } ^ { \prime } ) + { \bf e } ^ { \prime } \cos ( 2 \bar { \lambda } - 2 \bar { \lambda } ^ { \prime } - \varpi + \varpi ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + { \bf e } ^ { \prime } \cos ( \varpi - \varpi ^ { \prime } ) + 2 \mathrm { { \bf s } } ^ { \prime } \cos ( \bar { \lambda } - \bar { \lambda } ^ { \prime } - \Omega + \Omega ^ { \prime } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \mathrm { e } \cos ( 2 \bar { \lambda } - \bar { \lambda } ^ { \prime } - \varpi ) - \mathrm { e } \cos ( \bar { \lambda } ^ { \prime } - \varpi ) + \mathrm { e } ^ { \prime } \cos ( \bar { \lambda } - 2 \bar { \lambda } ^ { \prime } + \varpi ^ { \prime } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - { \bf e } ^ { \prime } \cos ( \bar { \lambda } - \varpi ^ { \prime } ) + \frac { 9 \epsilon ^ { 2 } } { 8 } \cos ( 3 \bar { \lambda } - \bar { \lambda } ^ { \prime } - 2 \varpi ) - \frac { \epsilon ^ { 2 } } { 8 } \cos ( \bar { \lambda } + \bar { \lambda } ^ { \prime } - 2 \varpi ) ; } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \frac { 9 \epsilon ^ { \prime 2 } } { 8 } \cos ( \bar { \lambda } - 3 \bar { \lambda } ^ { \prime } + 2 \varpi ^ { \prime } ) - \frac { { \epsilon } ^ { \prime 2 } } { 8 } \cos ( \bar { \lambda } + \bar { \lambda } ^ { \prime } - 2 \varpi ^ { \prime } ) } } \\ { { } } & { { } } & { { - \mathrm { e } \mathrm { e } ^ { \prime } \cos ( 2 \bar { \lambda } - \varpi - \varpi ^ { \prime } ) - \mathrm { e } \mathrm { e } ^ { \prime } \cos ( 2 \bar { \lambda } ^ { \prime } - \varpi - \varpi ^ { \prime } ) } } \\ \end{array}
$$

It is easily demonstrated that $\cos ( \vartheta - \vartheta ^ { \prime } )$ represents the value taken by cos $\psi$ when $s =$ $s ^ { \prime } = 0$ . Hence, from (11.171) and (11.190),

$$
\begin{array} { r c l } { { \delta } } & { { \simeq } } & { { s ^ { 2 } \left[ \cos ( \bar { \lambda } + \bar { \lambda } ^ { \prime } - 2 \Omega ) - \cos ( \bar { \lambda } - \bar { \lambda } ^ { \prime } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 2 s s ^ { \prime } \left[ \cos ( \bar { \lambda } - \bar { \lambda } ^ { \prime } - \Omega + \Omega ^ { \prime } ) - \cos ( \bar { \lambda } + \bar { \lambda } ^ { \prime } - \Omega - \Omega ^ { \prime } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + s ^ { \prime 2 } \left[ \cos ( \bar { \lambda } + \bar { \lambda } ^ { \prime } - 2 \Omega ^ { \prime } ) - \cos ( \bar { \lambda } - \bar { \lambda } ^ { \prime } ) \right] . } } \end{array}
$$

Now,

$$
\cos [ { \mathfrak { j } } \left( { \mathfrak { d } } - { \mathfrak { d } } ^ { \prime } \right) ] \equiv \cos ( { \mathfrak { j } } \vartheta ) \cos ( { \mathfrak { j } } \vartheta ^ { \prime } ) + \sin ( { \mathfrak { j } } \vartheta ) \sin ( { \mathfrak { j } } \vartheta ^ { \prime } ) .
$$

However, from (4.70),

$$
\begin{array} { r c l } { { \cos ( \mathfrak { j } \mathfrak { d } ) } } & { { \equiv } } & { { \cos [ \mathfrak { j } ( \varpi + \mathfrak { d } ) ] } } \\ { { } } & { { \simeq } } & { { ( 1 - \mathfrak { j } ^ { 2 } e ^ { 2 } ) \cos ( \mathfrak { j } \bar { \lambda } ) + e ^ { 2 } \left( \frac { \mathfrak { j } ^ { 2 } } { 2 } - \frac { 5 \mathfrak { j } } { 8 } \right) \cos [ ( 2 - \mathfrak { j } ) \bar { \lambda } - 2 \varpi ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + e ^ { 2 } \left( \frac { \mathfrak { j } ^ { 2 } } { 2 } + \frac { 5 \mathfrak { j } } { 8 } \right) \cos [ ( 2 + \mathfrak { j } ) \bar { \lambda } - 2 \varpi ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \mathfrak { j } e \cos [ ( 1 - \mathfrak { j } ) \bar { \lambda } - \varpi ] + \mathfrak { j } e \cos [ ( \mathtt { j } + \mathfrak { j } ) \bar { \lambda } - \varpi ) ] , } } \end{array}
$$

since $\mathcal { M } = \bar { \lambda } - \varpi$ . Likewise,

$$
\begin{array} { r c l } { { \sin ( { \bf j } \vartheta ) } } & { { \equiv } } & { { \sin [ { \bf j } \left( \varpi + { \bf 6 } \right) ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \simeq } } & { { ( 1 - { \bf j } ^ { 2 } e ^ { 2 } ) \sin ( { \bf j } \bar { \lambda } ) + e ^ { 2 } \left( \frac { 5 { \bf j } } { 8 } - \frac { { \bf j } ^ { 2 } } { 2 } \right) \sin [ ( 2 - { \bf j } ) \bar { \lambda } - 2 \varpi ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + e ^ { 2 } \left( \frac { 5 { \bf j } } { 8 } + \frac { { \bf j } ^ { 2 } } { 2 } \right) \sin [ ( 2 + { \bf j } ) \bar { \lambda } - 2 \varpi ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + { \bf j } e \sin [ ( 1 - { \bf j } ) \bar { \lambda } - \varpi ] + { \bf j } e \sin [ ( 1 + { \bf j } ) \bar { \lambda } - \varpi ] . } } \end{array}
$$

Hence, we obtain

$$
\begin{array} { l l l } { { \displaystyle \cos [ \frac { } { } ] \left( \vartheta - \vartheta ^ { \prime } \right) ] } } & { { \simeq } } & { { \displaystyle ( 1 - j ^ { 2 } e ^ { 2 } - j ^ { 2 } e ^ { \prime 2 } ) \cos [ \vert \bar { \lambda } - \bar { \lambda } ^ { \prime } ) ] } } \\ { { } } & { { } } & { { \displaystyle + e ^ { 2 } \left( \frac { 5 j } { 8 } + \frac { j ^ { 2 } } { 2 } \right) \cos [ ( 2 + j ) \bar { \lambda } - j \bar { \lambda } ^ { \prime } - 2 \varpi ] } } \\ { { } } & { { } } & { { \displaystyle + e ^ { 2 } \left( \frac { j ^ { 2 } } { 2 } - \frac { 5 j } { 8 } \right) \cos [ ( 2 - j ) \bar { \lambda } + j \bar { \lambda } ^ { \prime } - 2 \varpi ] } } \\ { { } } & { { } } & { { \displaystyle + \ j \ e \cos [ ( 1 + j ) \bar { \lambda } - \mathrm { \textstyle ~ j } \bar { \lambda } ^ { \prime } - \varpi ] - \mathrm { \textstyle ~ j ~ } e \cos [ ( 1 - j ) \bar { \lambda } + \mathrm { \textstyle ~ j } \bar { \lambda } ^ { \prime } - \varpi ] } } \\ { { } } & { { } } & { { \displaystyle + e ^ { \prime 2 } \left( \frac { j ^ { 2 } } { 2 } - \frac { 5 j } { 8 } \right) \cos [ \bar { \lambda } + ( 2 - j ) \bar { \lambda } ^ { \prime } - 2 \varpi ^ { \prime } ] } } \end{array}
$$

$$
\begin{array} { l } { + e ^ { \prime 2 } \left( \frac { 5 \bar { 5 } } { 8 } + \frac { \bar { 9 } ^ { 2 } } { 2 } \right) \cos [ \bar { 3 } - ( 2 + \mathrm { j } ) \bar { \lambda } ^ { \prime } + 2 \varpi ^ { \prime } ] } \\ { - \mathrm { j } e ^ { \prime } \cos [ \bar { 3 } - ( 1 - \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi ^ { \prime } ] + \mathrm { j } e ^ { \prime } \cos [ \bar { 3 } - ( 1 + \mathrm { j } ) \bar { \lambda } ^ { \prime } + \varpi ^ { \prime } ] } \\ { - \mathrm { j } ^ { 2 } e ^ { \prime } \cos [ ( 1 + \mathrm { j } ) \bar { \lambda } + ( 1 - \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi - \varpi ^ { \prime } ] } \\ { - \mathrm { j } ^ { 2 } e ^ { \prime } \cos [ ( 1 - \mathrm { j } ) \bar { \lambda } + ( 1 + \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi - \varpi ^ { \prime } ] } \\ { + \mathrm { j } ^ { 2 } e ^ { \prime } \cos [ ( 1 + \mathrm { j } ) \bar { \lambda } - ( 1 + \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi + \varpi ^ { \prime } ] } \\ { + \mathrm { j } ^ { 2 } e \mathrm { e } ^ { \prime } \cos [ ( 1 + \mathrm { j } ) \bar { \lambda } - ( 1 + \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi + \varpi ^ { \prime } ] } \\ { + \mathrm { j } ^ { 2 } e \mathrm { e } ^ { \prime } \cos [ ( 1 - \mathrm { j } ) \bar { \lambda } - ( 1 - \mathrm { j } ) \bar { \lambda } ^ { \prime } - \varpi + \varpi ^ { \prime } ] . } \end{array}
$$

Equations (11.180), (11.181), (11.191), and (11.195) yield

$$
S _ { \mathrm { { D } } } = \sum _ { \mathrm { { j } = - \infty , \infty } } S ^ { ( \mathrm { j } ) } ,
$$

where

$$
\begin{array} { r l } { \Gamma _ { 1 } ^ { \prime } } & { : = \langle \mathbf { \Delta } _ { x } ^ { 0 } : \mathbf { \Delta } _ { x } ^ { 0 } : \mathbf { \Delta } _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \mathbf { \Delta } _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } } \\ & { - \frac { 1 } { 4 } \| \mathbf { \Delta } _ { x } ^ { 0 } : \mathbf { \Delta } _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } } \\ &  \frac { 1 } { 4 } \| \mathbf { \Delta } _ { x } ^ { 0 } : \partial _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \nabla _ { x } ^ { 0 } : \ \end{array}
$$

Likewise, Equations (11.166), (11.167), (11.181), and (11.190) give

$$
S _ { \mathrm { { E } } } ~ \simeq ~ \left( - 1 + \frac { e ^ { 2 } } { 2 } + \frac { e ^ { \prime 2 } } { 2 } + s ^ { 2 } + s ^ { \prime 2 } \right) \cos ( \bar { \lambda } ^ { \prime } - \bar { \lambda } )
$$

$$
\begin{array} { l } { { - e ^ { \prime } \cos ( 2 \bar { \lambda } ^ { \prime } - 2 \bar { \lambda } - \varpi ^ { \prime } + \varpi ) - 2 s s ^ { \prime } \cos ( \bar { \lambda } ^ { \prime } - \bar { \lambda } - \Omega ^ { \prime } + \Omega ) } } \\ { { - \frac { e } { 2 } \cos ( \bar { \lambda } ^ { \prime } - 2 \bar { \lambda } + \varpi ) + \frac { 3 e } { 2 } \cos ( \bar { \lambda } ^ { \prime } - \varpi ) - 2 e ^ { \prime } \cos ( 2 \bar { \lambda } ^ { \prime } - \bar { \lambda } - \varpi ^ { \prime } ) } } \\ { { - \frac { 3 e ^ { 2 } } { 8 } \cos ( \bar { \lambda } ^ { \prime } - 3 \bar { \lambda } + 2 \varpi ) - \frac { e ^ { 2 } } { 8 } \cos ( \bar { \lambda } ^ { \prime } + \bar { \lambda } - 2 \varpi ) } } \\ { { + 3 e e ^ { \prime } \cos ( 2 \bar { \lambda } - \varpi ^ { \prime } - \varpi ) - \frac { e ^ { \prime 2 } } { 8 } \cos ( \bar { \lambda } ^ { \prime } + \bar { \lambda } - 2 \varpi ^ { \prime } ) } } \\ { { - \frac { 2 7 e ^ { \prime 2 } } { 8 } \cos ( 3 \bar { \lambda } ^ { \prime } - \bar { \lambda } - 2 \varpi ^ { \prime } ) - s ^ { 2 } \cos ( \bar { \lambda } ^ { \prime } + \bar { \lambda } - 2 \varpi ) } } \\ { { + 2 s s ^ { \prime } \cos ( \bar { \lambda } ^ { \prime } + \bar { \lambda } - \Omega ^ { \prime } - \Omega ) - s ^ { \prime 2 } \cos ( \bar { \lambda } ^ { \prime } + \bar { \lambda } - 2 \Omega ^ { \prime } ) , } } \end{array}
$$

and

$$
\begin{array} { r c l } { { S _ { 1 } } } & { { \simeq } } & { { \left( - 1 + \frac { \mathcal { C } ^ { 2 } } { 2 } + \frac { \mathcal { C } ^ { 2 } } { 2 } + s ^ { 2 } + s ^ { \prime 2 } \right) \cos ( \widetilde { \lambda } ^ { \prime } - \widetilde { \lambda } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - e ^ { \mathcal { C } ^ { \prime } } \cos ( 2 \widetilde { \lambda } ^ { \prime } - 2 \widetilde { \lambda } - \varpi ^ { \prime } ) + \Omega s ^ { \prime } ) \cos ( \widetilde { \lambda } ^ { \prime } - \widetilde { \lambda } - \Omega ^ { \prime } + \Omega ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - 2 e \cos ( \widetilde { \lambda } ^ { \prime } - 2 \widetilde { \lambda } + \varpi ) + \frac { 3 \mathcal { C } ^ { \prime } } { 2 } \cos ( \widetilde { \lambda } - \varpi ^ { \prime } ) - \frac { \Theta ^ { \prime } } { 2 } \cos ( 2 \widetilde { \lambda } ^ { \prime } - \widetilde { \lambda } - \varpi ^ { \prime } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \frac { 2 7 \mathcal { C } ^ { \prime } e } { 8 } \cos ( \widetilde { \lambda } ^ { \prime } - 3 \widetilde { \lambda } + 2 \varpi ) - \frac { e ^ { 2 } } { 8 } \cos ( \widetilde { \lambda } ^ { \prime } + \widetilde { \lambda } - 2 \varpi ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 3 \mathrm { e ~ c ~ } ^ { \prime } \cos ( 2 \widetilde { \lambda } - \varpi ^ { \prime } - \widetilde { \Omega } ) - \frac { \Theta ^ { \prime } } { 8 } \cos ( \widetilde { \lambda } ^ { \prime } + \widetilde { \lambda } - 2 \varpi ^ { \prime } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \frac { 3 \mathcal { C } ^ { \prime } } { 8 } \cos ( 3 \widetilde { \lambda } ^ { \prime } - \widetilde { \lambda } - 2 \varpi ^ { \prime } ) - s ^ { 2 } \cos ( \widetilde { \lambda } ^ { \prime } + \widetilde { \lambda } - 2 \Omega ) } } \\ { { } } & { { } } &   + 2 s ^ { \prime } \cos [ \widetilde   \end{array}
$$

We can distinguish two different types of term that appear in our expansion of the disturbing function. Periodic terms vary sinusoidally in time as our two planets orbit the Sun (i.e., they depend on the mean ecliptic longitudes, $\bar { \lambda }$ and $\bar { \lambda } ^ { \prime }$ ), whereas secular terms remain constant in time (i.e., they do not depend on $\bar { \lambda }$ and $\bar { \lambda } ^ { \prime }$ ). We expect the periodic terms to give rise to relatively short-period (i.e., of order the orbital periods) oscillations in the osculating orbital elements of our planets. On the other hand, we expect the secular terms to produce an initially linear increase in these elements with time. Since such an increase can become significant over a long period, even if the rate of increase is small, it is necessary to evaluate the secular terms in the disturbing function to higher order than the periodic terms. Hence, in the following, we shall evaluate periodic terms to $\mathcal O ( e )$ , and secular terms to $\mathcal { O } ( e ^ { 2 } )$ .

Making use of Equations (11.150), (11.163), and (11.196)–(11.198), as well as the definitions (11.119)–(11.122) (with ${ \mathfrak { p } } \simeq { \textrm { I } } \sin \Omega$ and $\mathsf { q } \simeq \mathrm { ~ I ~ } \cos \omega \mathrm { ) }$ ), the order by order expansion (in e) of the disturbing function of the first planet is

$$
\begin{array} { r l } { S _ { 5 } } & { = \frac { 1 } { 7 } \sum _ { i = 1 } ^ { n } g _ { i , i } ^ { X } , \qquad \mathrm { o r d i d } \ \overline { { \Lambda } } - \lambda ^ { \prime } \big ] - \alpha \cos { ( \overline { { \Lambda } } - \overline { { \Lambda } } ) } , } \\ { S _ { 5 } } & { = \frac { 1 } { 7 } \sum _ { i = 1 } ^ { n } g _ { i , i } ^ { X } , } \\ { S _ { 1 } } & { = \frac { 1 } { 7 } \sum _ { i = 1 } ^ { n } g _ { i , i } ^ { X } , } \\ & { \quad + \Pi _ { 1 } ( - 2 ) - \alpha \operatorname { W I } _ { 0 } ^ { X } , } \\ & { \quad + \frac { \alpha \epsilon } { 1 2 } ( - \alpha + \alpha ^ { 2 } ) \operatorname { w I } _ { 0 } ^ { X } , } \\ & { \quad + \frac { \alpha \epsilon } { 1 2 } ( - \alpha + \alpha ^ { 2 } ) \operatorname { w I } _ { 0 } ^ { X } , } \\ & { \quad + \frac { \alpha \epsilon } { 1 2 } ( - \alpha + \alpha ^ { 2 } ) \operatorname { w I } _ { 1 } ^ { X } , } \\ & { \quad + \frac { \alpha } { 2 } \Big \{ - \coth \leq ( 2 \overline { { \Lambda } } - \overline { { \Lambda } } ) - \sin { ( 2 \overline { { \Lambda } } ) } + 3 \epsilon - 3 \overline { { \Lambda } } \Big \} , } \\ & { \quad - 2 \zeta ^ { \prime } c c \alpha \big ( \overline { { \Lambda } } - \overline { { \Lambda } } - 4 \overline { { \Lambda } } ^ { \prime } + 4 \beta ^ { \prime } \operatorname { a r f } _ { 0 } ^ { X } - 2 \overline { { \Lambda } } ^ { \prime } \big ) , } \\ { S _ { 2 } } & { = \frac { 1 } { 3 } \Big ( \overline { { \Lambda } } ^ { \prime } - \overline { { \Lambda } } ^ { \prime } + \lambda ^ { \prime \prime } \partial ^ { 2 } ( 2 \pi ) \big ( - 4 \overline { { \Lambda } } ^ { \prime \prime } ) \big ) \Big \} \ , } \\ &  \quad + \frac { \alpha } { 1 2 } \left( \overline { { \Lambda } } + \overline { { \Lambda } } ^ { \prime \prime } + 2 \overline { { \Lambda } } ^ { \prime \prime } \coth ^ { \prime \prime } \right) \Big ( - 2 \overline { { \Lambda } } ^ { \prime \prime } + \overline { { \Lambda } } ^ { \prime \prime } + \overline   \Lambda \end{array}
$$

Likewise, the order by order expansion of the disturbing function of the second planet is

$$
\begin{array} { r l } { \bar { S } ^ { * } } & { = \frac { \kappa } { 2 } \displaystyle \sum _ { j = 1 } ^ { N } \Bigg \{ \kappa ( \gamma - 2 ) + \alpha \Pi \tilde { S } \Bigg \} \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \mathrm { e x e s i } \{ \Lambda ^ { * } + \} ( - 1 / \lambda ) } \\ & { + \alpha \left( - 2 \tilde { S } ^ { * } + \alpha \right) \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \lambda + \left( 1 - j \right) \tilde { \lambda } } \\ & { \quad + \left( \gamma ^ { 2 } - 1 \right) \left( 2 + \alpha \right) \left( \kappa \right) \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \left( \kappa - \mathrm { a } \right) \tilde { \lambda } ^ { * } \left( 1 - \tilde { \nu } \right) \tilde { \lambda } } \\ & { \quad + \left( \kappa ^ { 2 } - 1 / \lambda ^ { 2 } \right) \left( \kappa \right) \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \kappa _ { \mathrm { t r } j } ^ { \mathrm { H } } \lambda + \mathrm { s i n } \left\{ \kappa ^ { 2 } - \tilde { \nu } \right\} \left( \kappa - \mathrm { a } \right) \tilde { \lambda } ^ { * } } \\ & { + \frac { \kappa } { 2 } \left( \gamma - \kappa ^ { 2 } / \kappa \right) \left( \kappa \right) \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \kappa _ { \mathrm { t r } j } ^ { \mathrm { H } } \lambda + \mathrm { s i n } \left\{ \kappa ^ { 2 } - \tilde { \nu } \right\} + 3 \nu ^ { \mathrm { t } } \nu \mathrm { s i n } \tilde { \lambda } } \\ & { - \kappa \mathrm { t e x } \left\{ \tilde { N } - 2 \tilde { \lambda } - \kappa \right\} - \lambda \kappa \left\{ \alpha \right\} \{ \tilde { \lambda } ^ { * } - \tilde { \lambda } ^ { * } \left( \kappa ^ { 2 } - \tilde { \nu } \right) \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \nu _ { \mathrm { t r } j } ^ { \mathrm { H } } \lambda + 3 \nu ^ { \mathrm { t } } \mathrm { s i n } \tilde { \nu } \mathrm { s i n } \tilde { \lambda } } \\ { \mathrm { S } _ { 2 } ^ { * } } &  = \frac { 1 } { 8 } \left( \kappa ^ { 2 } - \kappa ^ { 2 } - \kappa ^ { 2 } \right) \kappa \mathrm { s i n } \{ \tilde  \ \end{array}
$$

# 11.10 Secular Evolution of Planetary Orbits

As a specific example of the use of perturbation theory, let evaluate the long term evolution of the osculating orbital elements of the planets in our model Solar System due to the secular terms in their disturbing functions. This is equivalent to averaging the osculating elements over the relatively short time-scales associated with the periodic terms. From Equations (11.200)–(11.202), the secular part of the first planet’s disturbing function takes the form

$$
\begin{array} { r c l } { { \hat { \gamma } _ { \mathrm { s } } } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } } { \bf b } _ { 1 / 2 } ^ { ( 0 ) } + { \frac { 1 } { 8 } } \left( { \bf h } ^ { 2 } + { \bf k } ^ { 2 } + { \bf h } ^ { \prime 2 } + { \bf k } ^ { \prime 2 } \right) \alpha { \bf b } _ { 3 / 2 } ^ { ( 1 ) } - { \frac { 1 } { 8 } } \left( { \bf p } ^ { 2 } + { \bf q } ^ { 2 } + { \bf p } ^ { \prime 2 } + { \bf q } ^ { \prime 2 } \right) \alpha { \bf b } _ { 3 / 2 } ^ { ( 1 ) } } } \\ { { } } & { { } } & { { \displaystyle - { \frac { 1 } { 4 } } \left( { \bf k } { \bf k } ^ { \prime } + { \bf h } { \bf h } ^ { \prime } \right) \alpha { \bf b } _ { 3 / 2 } ^ { ( 2 ) } + { \frac { 1 } { 4 } } \left( { \bf p } { \bf p } ^ { \prime } + { \bf q } { \bf q } ^ { \prime } \right) \alpha { \bf b } _ { 3 / 2 } ^ { ( 1 ) } , } } \end{array}
$$

since, as is easily demonstrated,

$$
\begin{array} { r c l } { { ( 2 \propto \mathsf { D } + \alpha ^ { 2 } \mathsf { D } ^ { 2 } ) { \bf b } _ { 1 / 2 } ^ { ( 0 ) } } } & { { = } } & { { \alpha { \bf b } _ { 3 / 2 } ^ { ( 1 ) } , } } \\ { { } } & { { } } & { { } } \\ { { ( 2 - 2 \propto \mathsf { D } - \alpha ^ { 2 } \mathsf { D } ^ { 2 } ) { \bf b } _ { 1 / 2 } ^ { ( 0 ) } } } & { { = } } & { { - \alpha { \bf b } _ { 3 / 2 } ^ { ( 2 ) } . } } \end{array}
$$

Evaluating the right-hand sides of Equations (11.151)–(11.156) to $\mathcal O ( e )$ , we find that

$$
\begin{array} { r l } & { \frac { \mathrm { d } \mathrm { d } \mathrm { u } } { \mathrm { d } \mathrm { t } } = \ 0 , } \\ & { \frac { \mathrm { d } \overline { { \lambda } } ^ { ( 1 ) } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { 3 } { 2 } \alpha - 2 \alpha ^ { 2 } \frac { \mathrm { d } S _ { \widetilde { \mathcal { M } } } } { 3 \alpha } \right] , } \\ & { \frac { \mathrm { d } \overline { { \lambda } } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ \alpha \frac { \partial S _ { \widetilde { \mathcal { M } } } } { \partial \mathrm { k } } \right] , } \\ & { \frac { \mathrm { d } \overline { { \lambda } } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ - \alpha \frac { \partial S _ { \widetilde { \mathcal { M } } } } { \partial \mathrm { h } } \right] , } \\ & { \frac { \mathrm { d } \overline { { \phi } } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ \alpha \frac { \partial S _ { \widetilde { \mathcal { N } } } } { \partial \mathrm { q } } \right] , } \\ & { \frac { \mathrm { d } \overline { { \mathrm { d } \mathrm { t } } } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ - \alpha \frac { \partial S _ { \widetilde { \mathcal { N } } } } { \partial \mathrm { p } } \right] , } \\ & { \frac { \mathrm { d } \overline { { \mathrm { d } \mathrm { t } } } } { \mathrm { d } \mathrm { t } } = \ \epsilon ^ { \prime } \mathrm { n } \left[ - \alpha \frac { \partial S _ { \widetilde { \mathcal { N } } } } { \partial \mathrm { p } } \right] , } \end{array}
$$

since $\partial { \cal S } _ { s } / \partial \bar { \lambda } = 0$ . It follows that

$$
\begin{array} { r c l } { { { \bf a } } } & { { = } } & { { { \bf a } _ { 0 } - \epsilon ^ { \prime } { \bf n } \left[ \displaystyle \frac { 2 } { 3 } \alpha ^ { 2 } { \bf D } { \bf b } _ { 1 / 2 } ^ { ( 0 ) } \right] , } } \\ { { } } & { { } } & { { } } \\ { { \bar { \lambda } _ { s } ^ { ( 1 ) } } } & { { = } } & { { 0 , } } \\ { { } } & { { } } & { { \displaystyle \frac { \mathrm { d } { \bf h } } { \mathrm { d t } } ~ = } } & { { \epsilon ^ { \prime } { \bf n } \left[ \displaystyle \frac { 1 } { 4 } \mathrm { k } \alpha ^ { 2 } { \bf b } _ { 3 / 2 } ^ { ( 1 ) } - \displaystyle \frac { 1 } { 4 } \mathrm { k } ^ { \prime } \alpha ^ { 2 } { \bf b } _ { 3 / 2 } ^ { ( 2 ) } \right] , } } \end{array}
$$

$$
\begin{array} { r c l } { { \displaystyle \frac { \mathrm { d } \mathtt { k } } { \mathrm { d t } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { 1 } { 4 } \mathrm { h } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } + \frac { 1 } { 4 } \mathrm { h } ^ { \prime } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 2 ) } \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \mathtt { p } } { \mathrm { d t } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ - \frac { 1 } { 4 } \mathrm { q } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } + \frac { 1 } { 4 } \mathrm { q } ^ { \prime } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \mathtt { q } } { \mathrm { d t } } } } & { { = } } & { { \epsilon ^ { \prime } \mathrm { n } \left[ \frac { 1 } { 4 } \mathrm { p } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } - \frac { 1 } { 4 } \mathrm { p } ^ { \prime } \alpha ^ { 2 } \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } \right] , } } \end{array}
$$

where ${ \mathfrak { a } } _ { 0 }$ is a constant. Here, we have assumed, without loss of generality, that the first planet’s mean orbital angular velocity is not changed by the perturbation (i.e., $\mathrm { d } \bar { \lambda } _ { s } ^ { ( 1 ) } / \mathrm { d t } =$ 0). Note that the first planet’s major radius, a, remains constant in time.

From Equations (11.203)–(11.205), the secular part of the second planet’s disturbing function takes the form

$$
\begin{array} { r c l } { { S _ { s } ^ { \prime } } } & { { = } } &  { \displaystyle { \frac { 1 } { 2 } \alpha \mathbf { b } _ { 1 / 2 } ^ { ( 0 ) } + \frac { 1 } { 8 } \left( \mathbf { h } ^ { 2 } + \mathbf { k } ^ { 2 } + \mathbf { h } ^ { \prime 2 } + \mathbf { k } ^ { \prime 2 } \right) \alpha ^ { 2 } \mathbf { b } _ { 3 / 2 } ^ { ( 1 ) } - \frac { 1 } { 8 } \left( \mathbf { p } ^ { 2 } + \mathbf { q } ^ { 2 } + \mathbf { p } ^ { \prime 2 } + \mathbf { q } ^ { \prime 2 } \right) \alpha ^ { 2 } \mathbf { b } ^ { ( 2 ) } } } \\ { { } } & { { } } &  { \displaystyle { - \frac { 1 } { 4 } \left( \mathbf { k } \mathbf { k } ^ { \prime } + \mathbf { h } \mathbf { h } ^ { \prime } \right) \alpha ^ { 2 } \mathbf { b } _ { 3 / 2 } ^ { ( 2 ) } + \frac { 1 } { 4 } \left( \mathbf { p } \mathbf { p } ^ { \prime } + \mathbf { q } \mathbf { \Delta } \mathbf { q } ^ { \prime } \right) \alpha ^ { 2 } \mathbf { b } _ { 3 / 2 } ^ { ( 1 ) } . } } \end{array}
$$

Evaluating the right-hand sides of Equations (11.157)–(11.162) to $\mathcal O ( e )$ , we find that

$$
\begin{array} { r l } { \frac { \mathrm { d } a ^ { \prime \prime } } { \mathrm { d } t } } & { = 0 , } \\ { \frac { \mathrm { d } \hat { \lambda } ^ { \prime \prime \prime } } { \mathrm { d } t } } & { = \mathrm { ~ \epsilon n { ' } ~ } \biggl [ - \frac { 3 } { 2 } \mathrm { a ^ { \prime } } + 2 \frac { \partial S _ { z } ^ { \prime } } { \partial z } \biggr ] , } \\ { \frac { \mathrm { d } \hat { \lambda } ^ { \prime } } { \mathrm { d } t } } & { = \mathrm { ~ \epsilon n { ' } ~ } \biggl [ \frac { - 1 } { \Delta ^ { \prime } } \frac { \partial S _ { z } ^ { \prime } } { \partial \Delta ^ { \prime } } \biggr ] , } \\ { \frac { \mathrm { d } k ^ { \prime } } { \mathrm { d } t } } & { = \mathrm { ~ \epsilon n { ' } ~ } \biggl [ - \alpha ^ { \prime \prime } } & { 0 . 8 \epsilon \biggr ] , } \\ { \frac { \mathrm { d } p ^ { \prime } } { \mathrm { d } t } } & { = \mathrm { ~ \epsilon n { ' } ~ } \biggl [ \mathrm { a ^ { \prime } ~ } \frac { \partial S _ { z } ^ { \prime } } { \partial \hat { q } ^ { \prime } } \biggr ] , } \\ { \frac { \mathrm { d } q ^ { \prime } } { \mathrm { d } t } } & { = \mathrm { ~ \epsilon n { ' } ~ } \biggl [ - \alpha ^ { \prime \prime } \frac { 1 } { \Delta p ^ { \prime } } \biggr ] . } \end{array}
$$

It follows that

$$
\begin{array} { r c l } { { { \bf a } ^ { \prime } } } & { { = } } & { { { \bf a } _ { 0 } ^ { \prime } + \epsilon { \bf n } ^ { \prime } \left[ \displaystyle \frac { 2 } { 3 } { \bf D } \left( \alpha { \bf b } _ { 1 / 2 } ^ { ( 0 ) } \right) \right] , } } \\ { { } } & { { } } & { { } } \\ { { \bar { \lambda } ^ { ( 1 ) ^ { \prime } } } } & { { = } } & { { 0 , } } \\ { { \displaystyle \frac { \mathrm { d } { \bf h } ^ { \prime } } { \mathrm { d t } } } } & { { = } } & { { \epsilon { \bf n } ^ { \prime } \left[ \displaystyle \frac { 1 } { 4 } { \bf k } ^ { \prime } \alpha { \bf b } _ { 3 / 2 } ^ { ( 1 ) } - \displaystyle \frac { 1 } { 4 } { \bf k } \alpha { \bf b } _ { 3 / 2 } ^ { ( 2 ) } \right] , } } \end{array}
$$

$$
\begin{array} { r c l } { { \displaystyle \frac { \mathrm { d } \mathrm { k } ^ { \prime } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon \mathrm { n } ^ { \prime } \left[ - \frac { 1 } { 4 } \mathrm { h } ^ { \prime } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } + \frac { 1 } { 4 } \mathrm { h } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 2 ) } \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \mathrm { p } ^ { \prime } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon \mathrm { n } ^ { \prime } \left[ - \frac { 1 } { 4 } \mathrm { q } ^ { \prime } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } + \frac { 1 } { 4 } \mathrm { q } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } \right] , } } \\ { { \displaystyle \frac { \mathrm { d } \mathrm { q } ^ { \prime } } { \mathrm { d t } } } } & { { = } } & { { \displaystyle \epsilon \mathrm { n } ^ { \prime } \left[ \frac { 1 } { 4 } \mathrm { p } ^ { \prime } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } - \frac { 1 } { 4 } \mathrm { p } \alpha \mathrm { b } _ { 3 / 2 } ^ { ( 1 ) } \right] , } } \end{array}
$$

where $\mathbf { a } _ { 0 } ^ { \prime }$ is a constant. Note that the second planet’s major radius, $\mathbf { { a } ^ { \prime } }$ , also remains constant in time.

Let us now generalize the above analysis to take all of the major planets in the Solar System into account. Let planet i have mass $\mathfrak { m } _ { \mathrm { i } }$ , major radius $\mathbf { a } _ { \mathrm { i } }$ , eccentricity $e _ { \mathrm { i } }$ , longitude of the perihelion $\varpi _ { \mathrm { i } } ,$ orbital inclination $\mathrm { I } _ { \mathrm { i } }$ , and longitude of the ascending node $\Omega _ { \mathrm { i } }$ . As we have seen, it is helpful to define the alternative orbital elements $\mathsf { h } _ { \mathrm { i } } = \mathsf { e } _ { \mathrm { i } }$ sin $\varpi _ { \mathrm { i } }$ , $\mathtt { k _ { i } } =$ $e _ { \mathrm { i } }$ cos $\varpi _ { \mathrm { i } }$ , $\mathsf { p } _ { \mathrm { i } } = \sin \mathrm { I } _ { \mathrm { i } }$ sin $\Omega _ { \mathrm { i } }$ and ${ \mathfrak { q } } _ { \mathrm { i } } = { \sin } { \mathrm { I } } _ { \mathrm { i } }$ cos $\Omega _ { \mathrm { i } }$ . It is also helpful to define the following parameters:

$$
\begin{array} { r } { \alpha _ { \mathrm { i j } } = \left\{ \begin{array} { l l } { \mathrm { a _ { i } / a _ { j } } \quad } & { \mathrm { ~ a _ { j } > a _ { i } ~ } } \\ { \mathrm { a _ { j } / a _ { i } } \quad } & { \mathrm { ~ a _ { j } < a _ { i } ~ } } \end{array} \right. , } \end{array}
$$

and

$$
\begin{array} { r } { \bar { \alpha } _ { \mathrm { i j } } = \left\{ \begin{array} { l l } { \mathrm { a _ { i } / a _ { j } } \quad \quad \quad } & { \mathrm { a _ { j } > a _ { i } } } \\ { 1 \quad \quad \quad } & { \mathrm { a _ { j } < a _ { i } } } \end{array} \right. , } \end{array}
$$

as well as

$$
\epsilon _ { \mathrm { i j } } = \frac { { \mathfrak { m } } _ { \mathrm { j } } } { M + { \mathfrak { m } } _ { \mathrm { i } } } ,
$$

where $M$ is the mass of the Sun. It then follows, from the above analysis, that the secular terms in the planetary disturbing functions cause the $\mathbf { h } _ { \mathrm { i } } , \mathbf { k } _ { \mathrm { i } } , \mathbf { p } _ { \mathrm { i } } ,$ and ${ \mathfrak { q } } _ { \mathrm { i } }$ to vary in time as

$$
\begin{array} { r l r } { \displaystyle \frac { \mathrm { d } \mathrm { h } _ { \mathrm { i } } } { \mathrm { d t } } } & { = } & { \displaystyle \sum _ { j = 1 , 8 } \boldsymbol { A } _ { \mathrm { i j } } \boldsymbol { \mathrm { k } } _ { j } , } \\ { \displaystyle \frac { \mathrm { d } \mathrm { k } _ { \mathrm { i } } } { \mathrm { d t } } } & { = } & { - \displaystyle \sum _ { j = 1 , 8 } \boldsymbol { A } _ { \mathrm { i j } } \mathrm { h } _ { \mathrm { j } } , } \\ { \displaystyle \frac { \mathrm { d } \mathrm { p } _ { \mathrm { i } } } { \mathrm { d t } } } & { = } & { \displaystyle \sum _ { j = 1 , 8 } \mathrm { B } _ { \mathrm { i j } } \mathrm { q } _ { \mathrm { j } } , } \\ { \displaystyle \frac { \mathrm { d } \mathrm { q } _ { \mathrm { i } } } { \mathrm { d t } } } & { = } & { - \displaystyle \sum _ { j = 1 , 8 } \mathrm { B } _ { \mathrm { i j } } \mathrm { p } _ { \mathrm { j } } , } \end{array}
$$

where

$$
\mathrm { { \cal A } _ { \mathrm { i i } } ~ = ~ \sum _ { j \ne i } \frac { n _ { i } } { 4 } \epsilon _ { i j } \alpha _ { i j } \bar { \alpha } _ { i j } \ b _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { i j } ) , }
$$

$$
\begin{array} { r c l } { { \displaystyle { A _ { \mathrm { i j } } } } } & { { = } } & { { \displaystyle { - \frac { \Omega _ { \mathrm { i } } } { 4 } \epsilon _ { \mathrm { i j } } \alpha _ { \mathrm { i j } } \bar { \alpha } _ { \mathrm { i j } } { \bf b } _ { 3 / 2 } ^ { ( 2 ) } ( \alpha _ { \mathrm { i j } } ) } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { B _ { \mathrm { i i } } } } } & { { = } } & { { \displaystyle { - \sum _ { \mathrm { j \neq i } } \frac { \Omega _ { \mathrm { i } } } { 4 } \epsilon _ { \mathrm { i j } } \alpha _ { \mathrm { i j } } \bar { \alpha } _ { \mathrm { i j } } { \bf b } _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { \mathrm { i j } } ) } , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { B _ { \mathrm { i j } } } } } & { { = } } & { { \displaystyle { \frac { \Omega _ { \mathrm { i } } } { 4 } \epsilon _ { \mathrm { i j } } \alpha _ { \mathrm { i j } } \bar { \alpha } _ { \mathrm { i j } } { \bf b } _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { \mathrm { i j } } ) } , } } \end{array}
$$

for $\mathrm { ~ j ~ } \neq \mathrm { ~ i ~ }$ . Here, Mercury is planet 1, Venus is planet 2, etc., and Neptune is planet 8. Note that the time evolution of the $\mathsf { h } _ { \mathrm { i } }$ and the $\mathrm { k _ { i } } .$ , which determine the eccentricities of the planetary orbits, is decoupled from that of the ${ \mathfrak { p } } _ { \mathrm { i } }$ and the ${ \mathfrak { q } } _ { \mathrm { i } }$ , which determine the inclinations. Let us search for normal mode solutions to Equations (11.237)–(11.240) of the form

$$
\begin{array} { r l } { \mathbf { h } _ { \mathrm { i } } } & { = \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { e } _ { \mathrm { i } 1 } \sin ( 9 \mathrm { t } + \beta _ { 1 } ) , } \\ { \mathbf { k } _ { \mathrm { i } } } & { = \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { e } _ { \mathrm { i } 1 } \cos ( 9 \mathrm { t } + \beta _ { 1 } ) , } \\ { \mathbf { p } _ { \mathrm { i } } } & { = \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { I } _ { \mathrm { i } 1 } \sin ( \mathbf { f } _ { \mathrm { i } } \mathrm { t } + \gamma _ { \mathrm { i } } ) , } \\ { \mathbf { q } _ { \mathrm { i } } } & { = \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { I } _ { \mathrm { i } 1 } \cos ( \mathbf { f } _ { \mathrm { i } } \mathrm { t } + \gamma _ { \mathrm { i } } ) . } \end{array}
$$

It follows that

$$
\begin{array} { r c l } { { \displaystyle \sum _ { \mathrm { j = 1 } , 8 } \left( \mathsf { A } _ { \mathrm { i j } } - \delta _ { \mathrm { i j } } \mathsf { g } _ { \mathrm { l } } \right) \mathsf { e } _ { \mathrm { j l } } } } & { { = } } & { { 0 , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \sum _ { \mathrm { j = 1 } , 8 } \left( \mathsf { B } _ { \mathrm { i j } } - \delta _ { \mathrm { i j } } \mathsf { f } _ { \mathrm { l } } \right) \mathsf { I } _ { \mathrm { j l } } } } & { { = } } & { { 0 . } } \end{array}
$$

At this stage, we have effectively reduced the problem of determining the secular evolution of the planetary orbits to a pair of matrix eigenvalue equations that can be solved via standard numerical methods. Once we have determined the eigenfrequencies, $\mathsf { f } _ { \mathrm { l } }$ and ${ \mathfrak { g } } _ { \mathfrak { l } }$ , and the corresponding eigenvectors, $e _ { \mathrm { i l } }$ and $\mathrm { I } _ { \mathrm { i l . } }$ , the phase angles $\beta _ { \mathrm { l } }$ and $\gamma _ { \mathrm { l } }$ are found by demanding that, at $\mathrm { t } = 0$ , Equations (11.245)–(11.248) lead to the values of $e _ { \mathrm { i } } , \mathrm { I } _ { \mathrm { i } } , \Omega _ { \mathrm { i } } ,$ and $\varpi _ { \mathrm { i } }$ given in Table 4.1.

The theory outlined above is generally referred to as Laplace-Lagrange secular evolution theory. The eigenfrequencies, eigenvectors, and phase angles obtained from this theory are shown in Tables 11.1–11.3. Note that the largest eigenfrequency is of magnitude 25.89 arc seconds per year, which translates to an oscillation period of about $5 \times 1 0 ^ { 4 }$ years. In other words, the time-scale over which the secular evolution of the Solar System predicted by Laplace-Lagrange theory takes place is at least $5 \times 1 0 ^ { 4 }$ years.

Note that one of the inclination eigenfrequencies, $\mathsf { f } _ { 5 }$ , takes the value zero. This is a consequence of the conservation of angular momentum. Since the Solar System is effectively an isolated dynamical system, its net angular momentum vector, L, is constant in both magnitude and direction. The plane normal to L that passes through the center of mass of the Solar System (which lies very close to the Sun) is known as the invariable plane. If all of the planetary orbits were to lie in the invariable plane then the net angular velocity vector of the Solar System would be parallel to the fixed net angular momentum vector. Moreover, the angular momentum vector would be parallel to one of the Solar System’s principle axes of rotation. In this situation, we would expect the Solar System to remain in a steady state (see Chapter 8). In other words, we would not expect any time evolution of the planetary inclinations. (Of course, lack of time variation implies an eigenfrequency of zero.) According to Equations (11.247) and (11.248), and the data shown in Tables 11.1 and 11.3, if the Solar System were in the inclination eigenstate associated with the null eigenfrequency $\mathsf { f } _ { 5 }$ then we would have

<table><tr><td>1 gt(&quot;y-1)</td><td>fi(&quot;y-1)</td><td>β(°) Y(°)</td></tr><tr><td>1 5.460</td><td>-5.199</td><td>89.64 20.23</td></tr><tr><td>2 7.343</td><td>-6.568</td><td>195.0 318.3</td></tr><tr><td>3 17.32</td><td>-18.74</td><td>336.2 255.6</td></tr><tr><td>4 18.00</td><td>-17.63</td><td>319.0 296.9</td></tr><tr><td>5 3.723</td><td>0.000</td><td>30.14 107.5</td></tr><tr><td>6 22.43</td><td>-25.89</td><td>131.1 127.3</td></tr><tr><td>7 2.709</td><td>-2.911</td><td>110.5 315.6</td></tr><tr><td>8 0.6336</td><td>-0.6780</td><td>67.19 202.8</td></tr></table>

$$
\begin{array} { r } { \begin{array} { l c l } { { \tt p } _ { \mathrm { i } } } & { = } & { 2 . 7 5 1 \times 1 0 ^ { - 2 } \sin \gamma _ { 5 } , } \\ { { \tt q } _ { \mathrm { i } } } & { = } & { 2 . 7 5 1 \times 1 0 ^ { - 2 } \cos \gamma _ { 5 } , } \end{array} } \end{array}
$$

for $i = 1 , 8$ . Since $\mathsf { p } _ { \mathrm { i } } = \sin \mathrm { I } _ { \mathrm { i } } \sin \Omega _ { \mathrm { i } }$ and ${ \bf q } _ { \mathrm { i } } = \sin { \mathrm { I } _ { \mathrm { i } } } \cos { \Omega _ { \mathrm { i } } } ,$ it follows that all of the planetary orbits would lie in the same plane, and this plane—which is, of course, the invariable plane—is inclined at $\mathrm { I } _ { 5 } = \sin ^ { - 1 } ( 2 . 7 5 1 \times 1 0 ^ { - 2 } ) = 1 . 5 7 6 ^ { \circ }$ to the ecliptic plane. Furthermore, the longitude of the ascending node of the invariable plane, with respect to the ecliptic plane, is $\Omega _ { 5 } = \gamma _ { 5 } = 1 0 7 . 5 ^ { \circ }$ . Actually, it is generally more convenient to measure the inclinations of the planetary orbits with respect to the invariable plane, rather than the ecliptic plane, since the inclination of the latter plane varies in time. We can achieve this goal by simply omitting the fifth inclination eigenstate when calculating orbital inclinations from Equations (11.247) and (11.248).

Consider the ith planet. Suppose one of the $e _ { \mathrm { i l } }$ coefficients— $\cdot e _ { \mathrm { i k } }$ , say—is sufficiently

<table><tr><td></td><td>i=1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>l=1</td><td>18131</td><td>629</td><td>404</td><td>65</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-2328</td><td>1917</td><td>1496</td><td>265</td><td>-1</td><td>-1</td><td>0</td><td>0</td></tr><tr><td>3</td><td>154</td><td>-1262</td><td>1046</td><td>2978</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>-169</td><td>1489</td><td>-1485</td><td>7286</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>2445</td><td>1635</td><td>1634</td><td>1877</td><td>4330</td><td>3415</td><td>-4395</td><td>158</td></tr><tr><td>6</td><td>10</td><td>-51</td><td>243</td><td>1566</td><td>-1563</td><td>4840</td><td>-181</td><td>-13</td></tr><tr><td>7</td><td>58</td><td>57</td><td>60</td><td>80</td><td>202</td><td>185</td><td>2934</td><td>-314</td></tr><tr><td>8</td><td>0</td><td>1</td><td>1</td><td>2</td><td>6</td><td>6</td><td>143</td><td>943</td></tr></table>

Table 11.2: Components of the eccentricity eigenvectors $e _ { \mathrm { i l } }$ obtained from Laplace-Lagrange secular evolution theory. All components have been multiplied by $1 0 ^ { 5 }$ .

large that

$$
\vert e _ { \mathrm { i k } } \vert > \sum _ { \mathrm { l } = 1 , 8 } ^ { \mathrm { l } \neq \mathrm { k } } \vert e _ { \mathrm { i l } } \vert .
$$

This is known as the Lagrange condition. As is easily demonstrated, if the Lagrange condition is satisfied then the eccentricity of the ith planet’s orbit varies between the minimum value

$$
e _ { \mathrm { i m i n } } = \left| e _ { \mathrm { i k } } \right| - \sum _ { \mathrm { l } = 1 , 8 } ^ { \mathrm { l } \ne \mathrm { k } } \left| e _ { \mathrm { i l } } \right|
$$

and the maximum value

$$
e _ { \mathrm { i m a x } } = \left| e _ { \mathrm { i k } } \right| + \sum _ { \mathrm { l } = 1 , 8 } ^ { \mathrm { l } \ne \mathrm { k } } | e _ { \mathrm { i l } } | .
$$

Moreover, on average, the perihelion point precesses at the associated eigenfrequency, ${ 9 \mathrm { k } }$ . The precession is prograde (i.e., in the same direction as the orbital motion) if the frequency is positive, and retrograde (i.e., in the opposite direction) if the frequency is negative. If the Lagrange condition is not satisfied then all we can say is that the maximum eccentricity is given by Equation (11.255), and there is no minimum eccentricity (i.e., the eccentricity can vary all the way down to zero). Furthermore, no mean precession rate of the perihelion point can be identified. It can be seen from Table 11.2 that the Lagrange condition for the orbital eccentricities is satisfied for all planets except for Venus and the Earth. The maximum and minimum eccentricities, and mean perihelion precession rates, of the Planets (when they exist) are given in Table 11.4. Note that Jupiter and Uranus have the same mean perihelion precession rates, and that all planets that possess mean precession rates exhibit prograde precession.

There is also a Lagrange condition associated with the inclinations of the planetary orbits. This condition is satisfied for the ith planet if one of the $\mathrm { I } _ { \mathrm { i l } } - \mathrm { I } _ { \mathrm { i k } }$ , say—is sufficiently

<table><tr><td></td><td>i=1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>l=1</td><td>12549</td><td>1180</td><td>850</td><td>180</td><td>-2</td><td>-2</td><td>2</td><td>0</td></tr><tr><td>2</td><td>-3547</td><td>1007</td><td>811</td><td>180</td><td>-1</td><td>-1</td><td>0</td><td>0</td></tr><tr><td>3</td><td>409</td><td>-2684</td><td>2445</td><td>-3596</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>116</td><td>-685</td><td>451</td><td>5022</td><td>0</td><td>-1</td><td>0</td><td>0</td></tr><tr><td>5</td><td>2751</td><td>2751</td><td>2751</td><td>2751</td><td>2751</td><td>2751</td><td>2751</td><td>2751</td></tr><tr><td>6</td><td>27</td><td>14</td><td>279</td><td>954</td><td>-636</td><td>1587</td><td>-69</td><td>-7</td></tr><tr><td>7</td><td>-332</td><td>-191</td><td>-172</td><td>-125</td><td>-95</td><td>-77</td><td>1757</td><td>-205</td></tr><tr><td>8</td><td>-144</td><td>-132</td><td>-129</td><td>-123</td><td>-117</td><td>-112</td><td>109</td><td>1181</td></tr></table>

Table 11.3: Components of the inclination eigenvectors $\mathrm { I _ { i l } }$ obtained from Laplace-Lagrange secular evolution theory. All components have been multiplied by $1 0 ^ { 5 }$ .

large that

$$
| \mathrm { I _ { i k } } | > \sum _ { \ l = 1 , 8 } ^ { \ l \neq \ k , \ l \neq 5 } | \mathrm { I _ { i l } } | .
$$

Note that the fifth inclination eigenmode is omitted from the above summation because we are now measuring inclinations relative to the invariable plane. If the Lagrange condition is satisfied then the inclination of the ith planet’s orbit with respect to the invariable plane varies between the minimum value

$$
\mathrm { I _ { i m i n } = s i n ^ { - 1 } \left[ | I _ { i k } | - \sum _ { l = 1 , 8 } ^ { l \ne k , l \ne 5 } | I _ { i l } | \right] }
$$

and the maximum value

$$
\mathrm { I _ { i m a x } = s i n ^ { - 1 } \left[ | I _ { i k } | + \sum _ { l = 1 , 8 } ^ { 1 \neq k , l \neq 5 } | I _ { i l } | \right] . }
$$

Moreover, on average, the ascending node precesses at the associated eigenfrequency, $\mathsf { f } _ { \mathsf { k } }$ . The precession is prograde (i.e., in the same direction as the orbital motion) if the frequency is positive, and retrograde (i.e., in the opposite direction) if the frequency is negative. If the Lagrange condition is not satisfied then all we can say is that the maximum inclination is given by Equation (11.258), and there is no minimum inclination (i.e., the inclination can vary all the way down to zero). Furthermore, no mean precession rate of the ascending node can be identified. It can be seen from Table 11.3 that the Lagrange condition for the orbital inclinations is satisfied for all planets except for Venus, the Earth, and Mars. The maximum and minimum inclinations, and mean nodal precession rates, of the Planets (when they exist) are given in Table 11.4. It can be seen that the four outer planets, which possess most of the mass of the Solar System, all have orbits whose inclinations to the invariable plane remain small. On the other hand, the four relatively light inner planets have orbits whose inclinations to the invariable plane can become relatively

<table><tr><td>Planet</td><td>emax</td><td>emin</td><td>{@)</td><td>Imax(°)</td><td>Imin(°)</td><td>(5)</td></tr><tr><td>Mercury</td><td>0.233</td><td>0.130</td><td>91</td><td>9.86</td><td>4.57</td><td>f1</td></tr><tr><td>Venus</td><td>0.00704</td><td>1</td><td>1</td><td>3.38</td><td>1</td><td>1</td></tr><tr><td>Earth</td><td>0.0637</td><td>1</td><td>1</td><td>2.95</td><td>1</td><td>1</td></tr><tr><td>Mars</td><td>0.141</td><td>0.0450</td><td>94</td><td>5.84</td><td>1</td><td>1</td></tr><tr><td>Jupiter</td><td>0.0610</td><td>0.0256</td><td>95</td><td>0.488</td><td>0.241</td><td>f6</td></tr><tr><td>Saturn</td><td>0.0845</td><td>0.0123</td><td>96</td><td>1.02</td><td>0.797</td><td>f6</td></tr><tr><td>Uranus</td><td>0.0765</td><td>0.0114</td><td>95</td><td>1.11</td><td>0.904</td><td>f7</td></tr><tr><td>Neptune</td><td>0.0143</td><td>0.00456</td><td>g8</td><td>0.799</td><td>0.555</td><td>f8</td></tr></table>

Table 11.4: Maximum and minimum eccentricities and inclinations of the planetary orbits, as well as mean perihelion and nodal precession rates, obtained from Laplace-Lagrange secular evolution theory. All inclinations are relative to the invariable plane.

large. Note that Jupiter and Saturn have the same mean nodal precession rates, and that all planets that possess mean precession rates exhibit retrograde precession.

# 11.11 Hirayama Families

Let us now consider the perturbing influence of the Planets on the orbit of an asteroid. Since all asteroids have masses that are much smaller than those of the Planets, it is reasonable to suppose that the perturbing influence of the asteroid on the planetary orbits is negligible. Let the asteroid have the osculating orbital elements a, e, $\bar { \lambda _ { 0 } }$ , I, $\Omega$ , $\varpi$ —see Section 4.10—and the alternative elements h, k, p, $\mathsf { q }$ —see Section 11.7. Thus, the mean orbital angular velocity of the asteroid is $\boldsymbol { \mathrm { n } } = ( \mathsf { G } M / \mathsf { a } ^ { 3 } ) ^ { 1 / 2 }$ . Likewise, let the eight planets have the osculating orbital elements ${ \mathrm { a } } _ { \mathrm { i } } , e _ { \mathrm { i } } , \bar { \lambda } _ { 0 \mathrm { i } } , { \mathrm { I } } _ { \mathrm { i } } , \Omega _ { \mathrm { i } } , \varpi _ { \mathrm { i } } ,$ , and the alternative elements $\mathsf { h } _ { \mathrm { i } ; }$ , $\mathbb { k } _ { \mathrm { i } } , { \mathfrak { p } } _ { \mathrm { i } } , { \mathfrak { q } } _ { \mathrm { i } } ;$ , for $i = 1 , 8$ . It is helpful to define the following parameters:

and

$$
\alpha _ { \mathrm { i } } = \left\{ \begin{array} { l l } { \mathrm { a / a _ { \mathrm { i } } } \quad \quad } & { \mathrm { a _ { \mathrm { i } } > a } } \\ { \mathrm { a _ { \mathrm { i } } / a } \quad \quad } & { \mathrm { a _ { \mathrm { i } } < a } } \end{array} \right. ,
$$

$$
\begin{array} { r } { \bar { \alpha } _ { \mathrm { i } } = \left\{ \begin{array} { c l } { \mathrm { a / { a _ { \mathrm { i } } } } } & { \qquad \mathrm { a _ { \mathrm { i } } > a } } \\ { 1 } & { \qquad \mathrm { a _ { \mathrm { i } } < a } } \end{array} \right. , } \end{array}
$$

as well as

$$
\epsilon _ { \mathrm { i } } = \frac { { \mathfrak { m } } _ { \mathrm { i } } } { M } ,
$$

where M is the mass of the Sun.

By analogy with the analysis in the previous section, the secular terms in the disturbing function of the asteroid, generated by the perturbing influence of the Planets, cause the

![](images/bd32c9c12af18fe9bda35d2bb1d24f5b2ee4b624a527cdcc2a314b6d147ba425.jpg)  
Figure 11.2: Osculating eccentricity plotted against the sine of the osculating inclination (relative to the J2000 equinox and ecliptic) for the orbits of the first 100,000 numbered asteroids at MJD 55400. Data from JPL.

asteroid’s osculating orbital elements to evolve in time as

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } { \mathbf { h } } } { \mathrm { d t } } ~ = ~ { \mathsf { A } } { \mathbf { k } } + \sum _ { \mathrm { i } = 1 , 8 } { \mathsf { A } } _ { \mathrm { i } } { \mathbf { k } } _ { \mathrm { i } } , } \\ { \displaystyle \frac { \mathrm { d } { \mathbf { k } } } { \mathrm { d t } } ~ = ~ - { \mathsf { A } } { \mathsf { h } } - \sum _ { \mathrm { i } = 1 , 8 } { \mathsf { A } } _ { \mathrm { i } } { \mathsf { h } } _ { \mathrm { i } } , } \\ { \displaystyle \frac { \mathrm { d } { \mathbf { p } } } { \mathrm { d t } } ~ = ~ { \mathsf { B } } { \mathsf { q } } + \sum _ { \mathrm { i } = 1 , 8 } { \mathsf { B } } _ { \mathrm { i } } { \mathsf { q } } _ { \mathrm { i } } , } \\ { \displaystyle \frac { \mathrm { d } { \mathbf { q } } } { \mathrm { d t } } ~ = ~ - { \mathsf { B } } { \mathsf { p } } - \sum _ { \mathrm { i } = 1 , 8 } { \mathsf { B } } _ { \mathrm { i } } { \mathsf { p } } _ { \mathrm { i } } , } \end{array}
$$

where

$$
\begin{array} { r c l } { { \displaystyle { \cal A } } } & { { = } } & { { \displaystyle \sum _ { i = 1 , 8 } \frac { \displaystyle \Pi } { 4 } \epsilon _ { \mathrm { i } } \alpha _ { \mathrm { i } } \bar { \alpha } _ { \mathrm { i } } \mathfrak { b } _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { \mathrm { i } } ) , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle { \cal A } _ { \mathrm { i } } } } & { { = } } & { { - \displaystyle \frac { \Pi } { 4 } \epsilon _ { \mathrm { i } } \alpha _ { \mathrm { i } } \bar { \alpha } _ { \mathrm { i } } \mathfrak { b } _ { 3 / 2 } ^ { ( 2 ) } ( \alpha _ { \mathrm { i } } ) , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { \bf \ B } } } & { { = } } & { { \displaystyle - \sum _ { i = 1 , 8 } \frac { \displaystyle \Pi } { 4 } \epsilon _ { \mathrm { i } } \alpha _ { \mathrm { i } } \bar { \alpha } _ { \mathrm { i } } \mathfrak { b } _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { \mathrm { i } } ) , } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { \bf B } _ { \mathrm { i } } } } & { { = } } & { { \displaystyle \frac { \Pi } { 4 } \epsilon _ { \mathrm { i } } \alpha _ { \mathrm { i } } \bar { \alpha } _ { \mathrm { i } } \mathfrak { b } _ { 3 / 2 } ^ { ( 1 ) } ( \alpha _ { \mathrm { i } } ) . } } \end{array}
$$

However, as we have seen, the planetary osculating elements themselves evolve in time as

$$
\begin{array} { r l } { \mathbf { h } _ { \mathrm { i } } } & { = ~ \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { e } _ { \mathrm { i } 1 } \sin ( \mathbf { g } _ { \mathrm { i } } \mathbf { t } + \boldsymbol { \beta } _ { \mathrm { I } } ) , } \\ { \mathbf { k } _ { \mathrm { i } } } & { = ~ \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { e } _ { \mathrm { i } 1 } \cos ( \mathbf { g } _ { \mathrm { i } } \mathbf { t } + \boldsymbol { \beta } _ { \mathrm { I } } ) , } \\ { \mathbf { p } _ { \mathrm { i } } } & { = ~ \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { I } _ { \mathrm { i } 1 } \sin ( \mathbf { f } _ { \mathrm { i } } \mathbf { t } + \boldsymbol { \gamma } _ { \mathrm { i } } ) , } \\ { \mathbf { q } _ { \mathrm { i } } } & { = ~ \displaystyle \sum _ { 1 = 1 , 8 } \mathbf { I } _ { \mathrm { i } 1 } \cos ( \mathbf { f } _ { \mathrm { i } } \mathbf { t } + \boldsymbol { \gamma } _ { \mathrm { i } } ) . } \end{array}
$$

Equations (11.262)–(11.265) can be solved to give

$$
\begin{array} { r c l } { { \bf h } ( \mathrm { t } ) } & { = } & { e _ { \mathrm { f r e e } } \mathrm {  ~ \ s i n } ( \cal { A } \mathrm { t } + \beta _ { \mathrm { f r e e } } ) + \ h _ { \mathrm { f o r c e d } } ( \mathrm { t } ) , } \\ { { \bf k } ( \mathrm { t } ) } & { = } & { e _ { \mathrm { f r e e } } \mathrm { \ c o s } ( \cal { A } \mathrm { t } + \beta _ { \mathrm { f r e e } } ) + \ k _ { \mathrm { f o r c e d } } ( \mathrm { t } ) , } \\ { { \bf p } ( \mathrm { t } ) } & { = } & { \mathrm { s i n } \mathrm { I } _ { \mathrm { f r e e } } \mathrm { \ s i n } ( { \bf B } \mathrm { t } + \gamma _ { \mathrm { f r e e } } ) + \ p _ { \mathrm { f o r c e d } } ( \mathrm { t } ) , } \\ { { \bf q } ( \mathrm { t } ) } & { = } & { \mathrm { s i n } \mathrm { I } _ { \mathrm { f r e e } } \mathrm { \ c o s } ( { \bf B } \mathrm { t } + \gamma _ { \mathrm { f r e e } } ) + { \bf q } _ { \mathrm { f o r c e d } } ( \mathrm { t } ) , } \end{array}
$$

where

$$
\begin{array} { r l r } { \displaystyle \mathsf { h } _ { \mathrm { f o r e d } } } & { = } & { - \displaystyle \sum _ { \lfloor - 1 , 8 \rfloor } \frac { \mathsf { v } _ { 1 } } { A - \mathsf { g } _ { \mathrm { l } } } \sin ( \mathsf { g } _ { \mathrm { l } } \mathsf { t } + \beta _ { \mathrm { l } } ) , } \\ { \displaystyle \mathsf { k } _ { \mathrm { f o r e d } } } & { = } & { - \displaystyle \sum _ { \lfloor - 1 , 8 \rfloor } \frac { \mathsf { v } _ { 1 } } { A - \mathsf { g } _ { \mathrm { l } } } \cos ( \mathsf { g } _ { \mathrm { l } } \mathsf { t } + \beta _ { \mathrm { l } } ) , } \\ { \displaystyle \mathsf { p } _ { \mathrm { f o r e d } } } & { = } & { - \displaystyle \sum _ { \lfloor - 1 , 8 \rfloor } \frac { \mathsf { \mu } _ { \mathrm { l } } } { 8 - \mathsf { f } _ { \mathrm { l } } } \sin ( \mathsf { f } _ { \mathrm { l } } \mathsf { t } + \gamma _ { \mathrm { l } } ) , } \\ { \displaystyle \mathsf { q } _ { \mathrm { f o r e d } } } & { = } & { - \displaystyle \sum _ { \lfloor - 1 , 8 \rfloor } \frac { \mathsf { \mu } _ { \mathrm { l } } } { 8 - \mathsf { f } _ { \mathrm { l } } } \cos ( \mathsf { f } _ { \mathrm { l } } \mathsf { t } + \gamma _ { \mathrm { l } } ) , } \end{array}
$$

and

$$
\begin{array} { l l l } { { { \bf v } _ { \mathrm { l } } } } & { { = } } & { { \displaystyle \sum _ { \mathrm { i } = 1 , 8 } { \cal A } _ { \mathrm { i } } e _ { \mathrm { i l } } , } } \\ { { { \bf \mu } _ { \mathrm { l } } } } & { { = } } & { { \displaystyle \sum _ { \mathrm { i } = 1 , 8 } { \bf B } _ { \mathrm { i } } \mathrm { I } _ { \mathrm { i l } } . } } \end{array}
$$

The parameters, $e _ { \mathrm { f r e e } }$ and $\mathrm { I _ { f r e e } }$ , appearing in Equations (11.274)–(11.277), are the eccentricity and inclination, respectively, that the asteroid orbit would possess were it not for the perturbing influence of the Planets. Roughly speaking, the planetary perturbations cause the osculating eccentricity, $e = [ { \mathsf h } ^ { 2 } + { \mathsf k } ^ { 2 } ] ^ { 1 / 2 }$ , and inclination, $\bar { \mathrm { I } } = \sin ^ { - 1 } \bar { ( [ p ^ { 2 } + q ^ { 2 } ] ^ { 1 / 2 } ) }$ , to oscillate about the intrinsic values $e _ { \mathrm { f r e e } }$ and $\mathrm { I _ { f r e e } }$ , respectively.

Figure 11.2 shows the osculating eccentricity plotted against the sine of the osculating inclination for the orbits of the first 100,000 numbered asteroids (asteroids are numbered in order of their discovery). No particular patten is apparent. Figure 11.3 shows the free eccentricity plotted against the sine of the free inclination for the same 100,000 orbits. It can be seen that many of the points representing the asteroid orbits have condensed into clumps. These clumps are known as Hirayama families, after their discoverer, the Japanese astronomer Kiyotsugu Hirayama (1874-1943). It is thought that the asteroids making up a given family had a common origin—most likely due to the break up of some much larger body. As a consequence of this origin, the asteroids originally had similar orbital elements. However, as time progressed, these elements were jumbled by the perturbing influence of the Planets. Thus, it is only when this influence is removed that the commonality of the orbits becomes apparent. Hirayama families are named after their largest member. The most prominent families are the (4) Vesta, (15) Eunomia, (24) Themis, (44) Nysa, (158) Koronis, (221) Eos, and (1272) Gefion families. (The number in brackets is that of the corresponding asteroid.)

![](images/48e13f5d21938f210ff1ea968c3a95803d795880a790fc7980c2ab62f2e7afdb.jpg)  
Figure 11.3: Free eccentricity plotted against the sine of the free inclination (relative to the J2000 equinox and ecliptic) for the orbits of the first 100,000 numbered asteroids at MJD 55400. Data from JPL. The most prominent Hiroyama families are labeled.

# A Vector Algebra and Vector Calculus

# A.1 Introduction

This appendix contains a brief outline of vector algebra and vector calculus. The essential purpose of vector algebra is to convert the propositions of Euclidean geometry in threedimensional space into a convenient algebraic form. Vector calculus allows us to define the instantaneous velocity and acceleration of a moving object in three-dimensional space, as well as the work done when such an object travels along a general curved trajectory in a force field. Vector calculus also introduces the concept of a scalar field: e.g., the potential energy associated with a conservative force field.

# A.2 Scalars and Vectors

Many physical quantities (e.g., mass, energy) are entirely defined by a numerical magnitude (in appropriate units). Such quantities, which have no directional element, are known as scalars. Moreover, since scalars can be represented by real numbers, it follows that they obey the familiar laws of ordinary algebra. However, there exits a second class of physical quantities (e.g., velocity, acceleration, force) which are only completely defined when both a numerical magnitude and a direction in space is specified. Such quantities are known as vectors. By definition, a vector obeys the same algebra as a displacement in space, and may thus be represented geometrically by a straight-line, →PQ (say), where the arrow indicates the direction of the displacement (i.e., from point $\mathsf { P }$ to point Q)—see Figure A.1. The magnitude of the vector is represented by the length of the straight-line.

It is conventional to denote vectors by bold-faced symbols (e.g., a, F) and scalars by non-bold-faced symbols (e.g., r, S). The magnitude of a general vector, a, is denoted |a|, or just $\mathbf { a }$ , and is, by definition, always greater than or equal to zero. It is convenient to define a vector with zero magnitude—this is denoted 0, and has no direction. Finally, two vectors, a and b, are said to be equal when their magnitudes and directions are identical.

![](images/b5a6534c6326a232377dc89a9512ac8b43dff0199833f8d7d4c451af925fd264.jpg)  
Figure A.1: A vector.

![](images/8db73f0ad8c110099a8b378a03309785cc29a6ed4ae9a64ad0c559664786458d.jpg)  
Figure A.2: Vector addition.

# A.3 Vector Algebra

Suppose that the displacements $\mathsf { P Q }$ and $\overrightarrow { \mathrm { Q R } }$ represent the vectors a and b, respectively— see Figure A.2. It can be seen that the result of combining these two displacements is to give the net displacement →PR. Hence, if →PR represents the vector c then we can write

$$
\mathbf { c } = \mathbf { a } + \mathbf { b } .
$$

This defines vector addition. By completing the parallelogram PQRS, we can also see that

$$
\overrightarrow { \sf P R } = \overrightarrow { \sf P Q } + \overrightarrow { \sf Q R } = \overrightarrow { \sf P S } + \overrightarrow { \sf S R } .
$$

However, →PS has the same length and direction as $\vec { \mathrm { Q R } }$ , and, thus, represents the same vector, b. Likewise, $\vec { \mathsf { P Q } }$ and →SR both represent the vector a. Thus, the above equation is equivalent to

$$
\mathbf { c } = \mathbf { a } + \mathbf { b } = \mathbf { b } + \mathbf { a } .
$$

We conclude that the addition of vectors is commutative. It can also be shown that the associative law holds: i.e.,

$$
\mathbf { a } + ( \mathbf { b } + \mathbf { c } ) = ( \mathbf { a } + \mathbf { b } ) + \mathbf { c } .
$$

The null vector, 0, is represented by a displacement of zero length and arbitrary direction. Since the result of combining such a displacement with a finite length displacement is the same as the latter displacement by itself, it follows that

$$
\mathbf { a } + \mathbf { 0 } = \mathbf { a } ,
$$

where a is a general vector. The negative of a is defined as that vector which has the same magnitude, but acts in the opposite direction, and is denoted −a. The sum of a and −a is thus the null vector: i.e.,

$$
\mathbf { a } + \left( - \mathbf { a } \right) = \mathbf { 0 } .
$$

![](images/ff189337d61f618107347c2c87b840d5947013e6acf78554489f51c8e5d2f021.jpg)  
Figure A.3: Vector subtraction.

We can also define the difference of two vectors, a and b, as

$$
\mathbf { c } = \mathbf { a } - \mathbf { b } = \mathbf { a } + ( - \mathbf { b } ) .
$$

This definition of vector subtraction is illustrated in Figure A.3.

If $\mathfrak { n } > 0$ is a scalar then the expression n a denotes a vector whose direction is the same as a, and whose magnitude is n times that of a. (This definition becomes obvious when n is an integer.) If n is negative then, since n $\mathbf { \nabla } _ { \cdot } \mathbf { a } = \left| \mathbf { n } \right| ( - \mathbf { a } ) _ { : }$ , it follows that n a is a vector whose magnitude is $| { \boldsymbol { \mathrm { n } } } |$ times that of a, and whose direction is opposite to a. These definitions imply that if $\mathfrak { n }$ and $\mathfrak { m }$ are two scalars then

$$
{ \begin{array} { r c l } { \mathbf { n } \left( \mathbf { m } \mathbf { a } \right) } & { = } & { \mathbf { n } \mathbf { m } \mathbf { a } = \mathbf { m } \left( \mathbf { n } \mathbf { a } \right) , } \\ { \left( \mathbf { n } + \mathbf { m } \right) \mathbf { a } } & { = } & { \mathbf { n } \mathbf { a } + \mathbf { m } \mathbf { a } , } \\ { \mathbf { n } \left( \mathbf { a } + \mathbf { b } \right) } & { = } & { \mathbf { n } \mathbf { a } + \mathbf { n } \mathbf { b } . } \end{array} }
$$

# A.4 Cartesian Components of a Vector

Consider a Cartesian coordinate system $\boldsymbol { \mathrm { O } } \boldsymbol { x } \boldsymbol { \mathrm { y } } z$ consisting of an origin, O, and three mutually perpendicular coordinate axes, $\mathrm { O x }$ , $\mathrm { O y }$ , and $\mathrm { O } z$ —see Figure A.4. Such a system is said to be right-handed if, when looking along the $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ direction, a $9 0 ^ { \circ }$ clockwise rotation about $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ is required to take $\mathrm { O x }$ into $\mathrm { O y }$ . Otherwise, it is said to be left-handed. In physics, it is conventional to always use right-handed coordinate systems.

It is convenient to define unit vectors, $\mathbf { e } _ { \mathrm { x } } , \mathbf { e } _ { \mathrm { y } }$ , and $\mathbf { e } _ { z }$ , parallel to $\mathrm { O x , \ O y }$ , and $O z ,$ respectively. Incidentally, a unit vector is a vector whose magnitude is unity. The position vector, r, of some general point $\mathsf { P }$ whose Cartesian coordinates are $( x , y , z )$ is then given by

$$
\mathbf { r } = { \boldsymbol { \mathrm { x } } } \mathbf { e } _ { z } + { \boldsymbol { \mathrm { y } } } \mathbf { e } _ { \mathrm { y } } + z \mathbf { e } _ { z } .
$$

In other words, we can get from $\mathrm { o }$ to $\mathsf { P }$ by moving a distance $x$ parallel to $\mathrm { O x }$ , then a distance $_ { 9 }$ parallel to $\mathrm { O y }$ , and then a distance $z$ parallel to $\hphantom { - } O z$ . Similarly, if a is an arbitrary vector then

$$
\mathbf { a } = \mathbf { a } _ { x } \mathbf { e } _ { x } + \mathbf { a } _ { y } \mathbf { e } _ { y } + \mathbf { a } _ { z } \mathbf { e } _ { z } ,
$$

![](images/e0e85b8f8ea3578df19db989d5caf928a3232074f1081256bb322f61ed0ef5a0.jpg)  
Figure A.4: A right-handed Cartesian coordinate system.

where ${ \mathrm { a } } _ { \mathrm { x } } , { \mathrm { a } } _ { \mathrm { y } }$ , and $\mathbf { a } _ { z }$ are termed the Cartesian components of a. It is coventional to write $\mathbf { a } \equiv ( \mathbf { a } _ { x } , \mathbf { a } _ { y } , \mathbf { a } _ { z } )$ . It follows that $\mathbf { e } _ { \mathrm { x } } \equiv ( 1 , 0 , 0 )$ , $\mathbf { e } _ { \mathsf { y } } \equiv ( 0 , 1 , 0 )$ , and $\mathbf { e } _ { z } \equiv ( 0 , 0 , 1 )$ . Of course, $\mathbf { 0 } \equiv ( 0 , 0 , 0 )$ .

According to the three-dimensional generalization of the Pythagorean theorem, the distance ${ \bf O } { \bf P } \equiv { \bf \left| { \bf r } \right| } = { \bf r }$ is given by

$$
\mathfrak { r } = \sqrt { x ^ { 2 } + \mathfrak { y } ^ { 2 } + z ^ { 2 } } .
$$

By analogy, the magnitude of a general vector a takes the form

$$
\mathbf { a } = \sqrt { \mathbf { a } _ { x } ^ { 2 } + \mathbf { a } _ { y } ^ { 2 } + \mathbf { a } _ { z } ^ { 2 } } .
$$

If $\mathbf { a } \equiv ( \mathbf { a } _ { x } , \mathbf { a } _ { y } , \mathbf { a } _ { z } )$ and $\mathbf { b } \equiv ( \mathsf { b } _ { x } , \mathsf { b } _ { y } , \mathsf { b } _ { z } )$ then it is easily demonstrated that

$$
\mathbf { a } + \mathbf { b } \equiv ( \mathbf { a } _ { x } + \mathbf { b } _ { x } , \mathbf { a } _ { y } + \mathbf { b } _ { y } , \mathbf { a } _ { z } + \mathbf { b } _ { z } ) .
$$

Furthermore, if ${ \mathfrak { n } }$ is a scalar then it is apparent that

$$
\mathrm { { \bf ~ \mathscr { n } } } \mathbf { a } \equiv ( \mathrm { n } \mathbf { a } _ { x } , \mathrm { n } \mathbf { a } _ { y } , \mathrm { n } \mathbf { a } _ { z } ) .
$$

# A.5 Coordinate Transformations

A Cartesian coordinate system allows position and direction in space to be represented in a very convenient manner. Unfortunately, such a coordinate system also introduces arbitrary elements into our analysis. After all, two independent observers might well choose coordinate systems with different origins, and different orientations of the coordinate axes. In general, a given vector a will have different sets of components in these two coordinate systems. However, the direction and magnitude of a are the same in both cases. Hence, the two sets of components must be related to one another in a very particular fashion. Actually, since vectors are represented by moveable line elements in space (i.e., in Figure A.2, $\begin{array} { r l r l } {  } & { { } \cdots } & { } & { { } \longrightarrow } \end{array}$ →PQ and →SR represent the same vector), it follows that the components of a general vector are not affected by a simple shift in the origin of a Cartesian coordinate system. On the other hand, the components are modified when the coordinate axes are rotated.

![](images/5b5090e1a7970dc7868b6c53830227086b3042bc27d204ded9609411f2865fb2.jpg)  
Figure A.5: Rotation of the coordinate axes about $\mathtt { O z }$ .

Suppose that we transform to a new coordinate system, $\mathrm { O x ^ { \prime } y ^ { \prime } } z ^ { \prime }$ , which has the same origin as $0 { \tt x y z }$ , and is obtained by rotating the coordinate axes of $\boldsymbol { \mathrm { O } } \boldsymbol { x } \boldsymbol { \mathrm { y } } z$ through an angle θ about $\mathrm { O } z$ —see Figure A.5. Let the coordinates of a general point $\mathsf { P }$ be $( x , y , z )$ in $\mathrm { O } { \tt x } { \tt y } z$ and $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ in $\mathrm { O x ^ { \prime } y ^ { \prime } } z ^ { \prime }$ . According to simple trigonometry, these two sets of coordinates are related to one another via the transformation:

$$
{ \begin{array} { r c l } { { \ d x ^ { \prime } } } & { { = } } & { { \times \cos \theta + y \sin \theta , } } \\ { { \ d y ^ { \prime } } } & { { = } } & { { - \ d x \sin \theta + y \cos \theta , } } \\ { { \ d z ^ { \prime } } } & { { = } } & { { \ d z . } } \end{array} }
$$

Consider the vector displacement $\mathbf { r } \equiv \stackrel { \longrightarrow } { \mathrm { O P } }$ . Note that this displacement is represented by the same symbol, r, in both coordinate systems, since the magnitude and direction of r are manifestly independent of the orientation of the coordinate axes. The coordinates of r do depend on the orientation of the axes: i.e., $\mathbf { r } \equiv ( { \boldsymbol { x } } , { \boldsymbol { y } } , z )$ in $0 { \tt x y z }$ , and $\mathbf { r } \equiv ( \mathrm { x } ^ { \prime } , \mathrm { y } ^ { \prime } , z ^ { \prime } )$ i n $\mathrm { O x ^ { \prime } y ^ { \prime } } z ^ { \prime }$ . However, they must depend in a very specific manner [i.e., Equations (A.17)– (A.19)] which preserves the magnitude and direction of r.

The components of a general vector a transform in an analogous manner to Equations (A.17)–(A.19): i.e.,

$$
\begin{array} { r c l } { { { \bf { a } } _ { x ^ { \prime } } } } & { { = } } & { { { \bf { a } } _ { x } \cos \theta + { \bf { a } } _ { y } \sin \theta , } } \\ { { } } & { { } } & { { } } \\ { { { \bf { a } } _ { y ^ { \prime } } } } & { { = } } & { { - { \bf { a } } _ { x } \sin \theta + { \bf { a } } _ { y } \cos \theta , } } \\ { { } } & { { } } & { { } } \\ { { { \bf { a } } _ { z ^ { \prime } } } } & { { = } } & { { { \bf { a } } _ { z } . } } \end{array}
$$

Moreover, there are similar transformation rules for rotation about $\mathrm { O x }$ and $\mathrm { O y }$ . Equations (A.20)–(A.22) effectively constitute the definition of a vector: i.e., the three quantities $( \mathbf { a } _ { \mathrm { x } } , \mathbf { a } _ { \mathrm { y } } , \mathbf { a } _ { z } )$ are the components of a vector provided that they transform under rotation of the coordinate axes about $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ in accordance with Equations (A.20)–(A.22). (And also transform correctly under rotation about $\mathrm { O x }$ and $\mathrm { O } { \mathfrak { y } } .$ ). Conversely, $( \mathbf { a } _ { \mathrm { x } } , \mathbf { a } _ { \mathrm { y } } , \mathbf { a } _ { z } )$ cannot be the components of a vector if they do not transform in accordance with Equations (A.20)– (A.22). Of course, scalar quantities are invariant under rotation of the coordinate axes. Thus, the individual components of a vector $\left( \mathbf { a } _ { x } ^ { \phantom { } } \right)$ , say) are real numbers, but they are not scalars. Displacement vectors, and all vectors derived from displacements (e.g., velocity, acceleration), automatically satisfy Equations (A.20)–(A.22). There are, however, other physical quantities which have both magnitude and direction, but which are not obviously related to displacements. We need to check carefully to see whether these quantities are really vectors (see Section A.8).

# A.6 Scalar Product

A scalar quantity is invariant under all possible rotational transformations. The individual components of a vector are not scalars because they change under transformation. Can we form a scalar out of some combination of the components of one, or more, vectors? Suppose that we were to define the “percent” product,

$$
\mathbf { a } \% \mathbf { b } \equiv \mathbf { a } _ { x } \mathbf { b } _ { z } + \mathbf { a } _ { y } \mathbf { b } _ { x } + \mathbf { a } _ { z } \mathbf { b } _ { y } = \mathrm { s c a l a r \ n u m b e r } ,
$$

for general vectors a and b. Is a % b invariant under transformation, as must be the case if it is a scalar number? Let us consider an example. Suppose that $\mathbf { a } \equiv ( 0 , 1 , 0 )$ and $\mathbf { b } \equiv$ (1, 0, 0). It is easily seen that $\mathbf { a } \% \mathbf { b } = 1$ . Let us now rotate the coordinate axes through $4 5 ^ { \circ }$ about $\hphantom { - } O z$ . In the new coordinate system, $\mathbf { a } \equiv ( 1 / \sqrt { 2 } , 1 / \sqrt { 2 } , 0 )$ and $\boldsymbol { \mathbf { b } } \equiv ( 1 / \sqrt { 2 } , - 1 / \sqrt { 2 } , 0 ) .$ , giving $\mathbf { a } \% \mathbf { b } = 1 / 2$ . Clearly, $\mathbf { a } \%$ b is not invariant under rotational transformation, so the above definition is a bad one.

Consider, now, the dot product or scalar product:

$$
\mathbf { a } \cdot \mathbf { b } \equiv \mathbf { a } _ { x } \mathbf { b } _ { x } + \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { \mathrm { y } } + \mathbf { a } _ { z } \mathbf { b } _ { z } = { \mathrm { s c a l a r ~ n u m b e r } } .
$$

Let us rotate the coordinate axes though $\theta$ degrees about $\hphantom { - } O z$ . According to Equations (A.20)– (A.22), a $\mathbf { \nabla } \cdot \mathbf { b }$ takes the form

$$
{ \begin{array} { r l } { \mathbf { a } \cdot \mathbf { b } } & { = ~ \left( \mathbf { a } _ { x } \cos \theta + \mathbf { a } _ { y } \sin \theta \right) \left( \mathbf { b } _ { x } \cos \theta + \mathbf { b } _ { y } \sin \theta \right) } \\ & { + ( - \mathbf { a } _ { x } \sin \theta + \mathbf { a } _ { y } \cos \theta ) \left( - \mathbf { b } _ { x } \sin \theta + \mathbf { b } _ { y } \cos \theta \right) + \mathbf { a } _ { z } \mathbf { b } _ { z } } \\ & { = ~ \mathbf { a } _ { x } \mathbf { b } _ { x } + \mathbf { a } _ { y } \mathbf { b } _ { y } + \mathbf { a } _ { z } \mathbf { b } _ { z } } \end{array} }
$$

in the new coordinate system. Thus, a $\cdot$ b is invariant under rotation about $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ . It can easily be shown that it is also invariant under rotation about $\mathrm { O x }$ and $\mathrm { O y }$ . We conclude that a $\mathbf { \nabla } \cdot \mathbf { b }$ is a true scalar, and that the above definition is a good one. Incidentally, a · b is the only simple combination of the components of two vectors which transforms like a scalar. It is easily shown that the dot product is commutative and distributive: i.e.,

$$
\begin{array} { r c l } { \mathbf { a } \cdot \mathbf { b } } & { = } & { \mathbf { b } \cdot \mathbf { a } , } \\ { \mathbf { a } \cdot ( \mathbf { b } + \mathbf { c } ) } & { = } & { \mathbf { a } \cdot \mathbf { b } + \mathbf { a } \cdot \mathbf { c } . } \end{array}
$$

![](images/513555906a99f76e62cead83237249e08dbe325fb58e3d30785dbb2cb268b5f1.jpg)  
Figure A.6: A vector triangle.

The associative property is meaningless for the dot product, because we cannot have (a · $\mathbf { b } ) \cdot \mathbf { c } ,$ , since a $\cdot$ b is scalar.

We have shown that the dot product a $\mathbf { \nabla } \cdot \mathbf { b }$ is coordinate independent. But what is the geometric significance of this? Well, in the special case where $\mathbf { a } = \mathbf { b }$ , we get

$$
\mathbf { a } \cdot \mathbf { b } = \mathbf { a } _ { x } ^ { 2 } + \mathbf { a } _ { y } ^ { 2 } + \mathbf { a } _ { z } ^ { 2 } = | \mathbf { a } | ^ { 2 } = \mathbf { a } ^ { 2 } .
$$

So, the invariance of a·a is equivalent to the invariance of the magnitude of vector a under transformation.

Let us now investigate the general case. The length squared of AB in the vector triangle shown in Figure A.6 is

$$
( \mathbf { b } - \mathbf { a } ) \cdot ( \mathbf { b } - \mathbf { a } ) = | \mathbf { a } | ^ { 2 } + | \mathbf { b } | ^ { 2 } - 2 \mathbf { a } \cdot \mathbf { b } .
$$

However, according to the “cosine rule” of trigonometry,

$$
( A \mathrm { B } ) ^ { 2 } = ( \mathrm { O } A ) ^ { 2 } + ( \mathrm { O } \mathrm { B } ) ^ { 2 } - 2 ( \mathrm { O } A ) ( \mathrm { O } \mathrm { B } ) \cos { \theta } ,
$$

where (AB) denotes the length of side AB. It follows that

$$
\mathbf { a } \cdot \mathbf { b } = \left| \mathbf { a } \right| \left| \mathbf { b } \right| \cos \theta .
$$

In this case, the invariance of a $\mathbf { \nabla } \cdot \mathbf { b }$ under transformation is equivalent to the invariance of the angle subtended between the two vectors. Note that if $\mathbf { a } \cdot \mathbf { b } = 0$ then either $| \mathbf { a } | = 0$ , $| \mathbf { b } | = 0$ , or the vectors a and b are mutually perpendicular. The angle subtended between two vectors can easily be obtained from the dot product: i.e.,

$$
\cos \theta = { \frac { \mathbf { a } \cdot \mathbf { b } } { \left| \mathbf { a } \right| \left| \mathbf { b } \right| } } .
$$

The work $\boldsymbol { W }$ performed by a constant force $\mathbf { F }$ which moves an object through a displacement r is the product of the magnitude of $\mathbf { F }$ times the displacement in the direction of F. If the angle subtended between $\mathbf { F }$ and $\mathbf { r }$ is θ then

$$
W = \left| \mathbf { F } \right| \left( \left| \mathbf { r } \right| \cos \theta \right) = \mathbf { F } \cdot \mathbf { r } .
$$

The work dW performed by a non-constant force f which moves an object through an infinitesimal displacement dr in a time interval dt is $\mathrm { d } { \cal W } = { \bf f } \cdot { \bf \Omega }$ dr. Thus, the rate at which the force does work on the object, which is usually referred to as the power, is $\mathsf { P } = \mathrm { d } \mathsf { W } / \mathrm { d t } = \mathsf { f } \cdot \mathrm { d } \mathsf { r } / \mathrm { d t }$ , or $\mathbf { P } = \mathbf { f } \cdot \mathbf { v }$ , where $\mathbf { v } = \mathrm { d } \mathbf { r } / \mathrm { d t }$ is the object’s instantaneous velocity.

# A.7 Vector Product

We have discovered how to construct a scalar from the components of two general vectors a and b. Can we also construct a vector which is not just a linear combination of a and b? Consider the following definition:

$$
\mathbf { a } * \mathbf { b } \equiv ( \mathbf { a } _ { x } \mathbf { b } _ { x } , \mathbf { a } _ { y } \mathbf { b } _ { y } , \mathbf { a } _ { z } \mathbf { b } _ { z } ) .
$$

Is $\mathbf { a } * \mathbf { b }$ a proper vector? Suppose that $\mathbf { a } = ( 0 , 1 , 0 )$ , $\mathbf { b } = ( 1 , 0 , 0 )$ . In this case, ${ \mathbf a } * { \mathbf b } = { \mathbf 0 }$ . However, if we rotate the coordinate axes through $4 5 ^ { \circ }$ about $\hphantom { - } O z$ then $\mathbf { a } = ( 1 / \sqrt { 2 } , 1 / \sqrt { 2 } , 0 )$ , $\boldsymbol { \mathbf { b } } = ( 1 / \sqrt { 2 } , - 1 / \sqrt { 2 } , 0 )$ , and $\mathbf { a } * \mathbf { b } = ( 1 / 2 , - 1 / 2 , 0 )$ . Thus, $\mathbf { a } * \mathbf { b }$ does not transform like a vector, because its magnitude depends on the choice of axes. So, above definition is a bad one.

Consider, now, the cross product or vector product:

$$
\mathbf { a } \times \mathbf { b } \equiv ( \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { z } - \mathbf { a } _ { z } \mathbf { b } _ { \mathrm { y } } , \mathbf { a } _ { z } \mathbf { b } _ { x } - \mathbf { a } _ { x } \mathbf { b } _ { z } , \mathbf { a } _ { x } \mathbf { b } _ { \mathrm { y } } - \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { \mathrm { x } } ) = \mathbf { c } .
$$

Does this rather unlikely combination transform like a vector? Let us try rotating the coordinate axes through an angle $\theta$ about $\hphantom { - } O z$ using Equations (A.20)–(A.22). In the new coordinate system,

$$
{ \begin{array} { l l l } { c _ { x ^ { \prime } } } & { = } & { \left( - \mathbf { a } _ { x } \sin \theta + \mathbf { a } _ { y } \cos \theta \right) \mathbf { b } _ { z } - \mathbf { a } _ { z } \left( - \mathbf { b } _ { x } \sin \theta + \mathbf { b } _ { y } \cos \theta \right) } \\ & { = } & { \left( \mathbf { a } _ { y } \mathbf { b } _ { z } - \mathbf { a } _ { z } \mathbf { b } _ { y } \right) \cos \theta + \left( \mathbf { a } _ { z } \mathbf { b } _ { x } - \mathbf { a } _ { x } \mathbf { b } _ { z } \right) \sin \theta } \\ & { = } & { c _ { x } \cos \theta + c _ { y } \sin \theta . } \end{array} }
$$

Thus, the $x$ -component of $\mathbf { a } \times \mathbf { b }$ transforms correctly. It can easily be shown that the other components transform correctly as well, and that all components also transform correctly under rotation about $\mathrm { O x }$ and $\mathrm { O y }$ . Thus, $\mathbf { a } \times \mathbf { b }$ is a proper vector. Incidentally, $\mathbf { a } \times \mathbf { b }$ is the only simple combination of the components of two vectors that transforms like a vector (which is non-coplanar with a and b). The cross product is anticommutative,

$$
\mathbf { a } \times \mathbf { b } = - \mathbf { b } \times \mathbf { a } ,
$$

distributive,

$$
\mathbf { a } \times ( \mathbf { b } + \mathbf { c } ) = \mathbf { a } \times \mathbf { b } + \mathbf { a } \times \mathbf { c } ,
$$

but is not associative,

$$
\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) \neq ( \mathbf { a } \times \mathbf { b } ) \times \mathbf { c } .
$$

The cross product transforms like a vector, which means that it must have a welldefined direction and magnitude. We can show that $\mathbf { a } \times \mathbf { b }$ is perpendicular to both a and b. Consider $\mathbf { a } \cdot \mathbf { a } \times \mathbf { b }$ . If this is zero then the cross product must be perpendicular to a. Now,

$$
{ \begin{array} { l l l } { \mathbf { a } \cdot \mathbf { a } \times \mathbf { b } } & { = } & { \mathbf { a } _ { x } \left( \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { z } - \mathbf { a } _ { z } \mathbf { b } _ { \mathrm { y } } \right) + \mathbf { a } _ { \mathrm { y } } \left( \mathbf { a } _ { z } \mathbf { b } _ { \mathrm { x } } - \mathbf { a } _ { \mathrm { x } } \mathbf { b } _ { z } \right) + \mathbf { a } _ { z } \left( \mathbf { a } _ { \mathrm { x } } \mathbf { b } _ { \mathrm { y } } - \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { \mathrm { x } } \right) } \\ & { = } & { 0 . } \end{array} }
$$

![](images/44b9e62e23fbaa3fa7c75980510bb70b90685bd27c3fb6d7cfa963ff602add53.jpg)  
Figure A.7: The right-hand rule for cross products. Here, θ is less that $1 8 0 ^ { \circ }$ .

Therefore, $\mathbf { a } \times \mathbf { b }$ is perpendicular to a. Likewise, it can be demonstrated that $\mathbf { a } \times \mathbf { b }$ is perpendicular to b. The vectors a, b, and $\mathbf { a } \times \mathbf { b }$ form a right-handed set, like the unit vectors $\mathbf { e } _ { x }$ , $\mathbf { e } _ { \mathfrak { y } }$ , and $\mathbf { e } _ { z }$ . In fact, $\mathbf { e } _ { \mathrm { x } } \times \mathbf { e } _ { \mathrm { y } } = \mathbf { e } _ { z }$ . This defines a unique direction for $\mathbf { a } \times \mathbf { b } _ { \mathrm { ~ } }$ , which is obtained from a right-hand rule—see Figure A.7.

Let us now evaluate the magnitude of $\mathbf { a } \times \mathbf { b }$ . We have

$$
{ \begin{array} { l l l } { ( \mathbf { a } \times \mathbf { b } ) ^ { 2 } } & { = } & { ( \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { z } - \mathbf { a } _ { z } \mathbf { b } _ { \mathrm { y } } ) ^ { 2 } + ( \mathbf { a } _ { z } \mathbf { b } _ { x } - \mathbf { a } _ { x } \mathbf { b } _ { z } ) ^ { 2 } + ( \mathbf { a } _ { \mathrm { x } } \mathbf { b } _ { \mathrm { y } } - \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { \mathrm { x } } ) ^ { 2 } } \\ & { = } & { ( \mathbf { a } _ { \mathrm { x } } ^ { 2 } + \mathbf { a } _ { \mathrm { y } } ^ { 2 } + \mathbf { a } _ { z } ^ { 2 } ) ( \mathbf { b } _ { \mathrm { x } } ^ { 2 } + \mathbf { b } _ { \mathrm { y } } ^ { 2 } + \mathbf { b } _ { z } ^ { 2 } ) - ( \mathbf { a } _ { \mathrm { x } } \mathbf { b } _ { x } + \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { \mathrm { y } } + \mathbf { a } _ { z } \mathbf { b } _ { z } ) ^ { 2 } } \\ & { = } & { | \mathbf { a } | ^ { 2 } | \mathbf { b } | ^ { 2 } - ( \mathbf { a } \cdot \mathbf { b } ) ^ { 2 } } \\ & { = } & { | \mathbf { a } | ^ { 2 } | \mathbf { b } | ^ { 2 } - | \mathbf { a } | ^ { 2 } | \mathbf { b } | ^ { 2 } \cos ^ { 2 } \theta = | \mathbf { a } | ^ { 2 } | \mathbf { b } | ^ { 2 } \sin ^ { 2 } \theta . } \end{array} }
$$

Thus,

$$
| \mathbf { a } \times \mathbf { b } | = | \mathbf { a } | | \mathbf { b } | \sin \theta ,
$$

where $\theta$ is the angle subtended between a and b. Clearly, $\mathbf { a } \times \mathbf { a } = \mathbf { 0 }$ for any vector, since $\theta$ is always zero in this case. Also, if $\mathbf { a } \times \mathbf { b } = \mathbf { 0 }$ then either $| \mathbf { a } | = 0$ , $| \mathbf { b } | = 0$ , or $\mathbf { b }$ is parallel (or antiparallel) to a.

Consider the parallelogram defined by the vectors a and b—see Figure A.8. The scalar area of the parallelogram is a b sin θ. By convention, the vector area has the magnitude of the scalar area, and is normal to the plane of the parallelogram, in the sense obtained from a right-hand circulation rule by rotating a on to b (through an acute angle): i.e., if the fingers of the right-hand circulate in the direction of rotation then the thumb of the right-hand indicates the direction of the vector area. So, the vector area is coming out of the page in Figure A.8. It follows that

$$
{ \pmb S } = { \bf a } \times { \bf b } ,
$$

Suppose that a force $\mathbf { F }$ is applied at position r—see Figure A.9. The torque about the origin O is the product of the magnitude of the force and the length of the lever arm OQ. Thus, the magnitude of the torque is $\mathbf { \left| F \right| } \left| \mathbf { r } \right| \sin \theta$ . The direction of the torque is conventionally defined as the direction of the axis through O about which the force tries to rotate objects, in the sense determined by a right-hand circulation rule. Hence, the torque is out of the page in Figure A.9. It follows that the vector torque is given by

$$
{ \pmb { \tau } } = { \bf { r } } \times { \bf { F } } .
$$

The angular momentum, l, of a particle of linear momentum $\mathbf { p }$ and position vector r is simply defined as the moment of its momentum about the origin: i.e.,

$$
\mathbf { l } = \mathbf { r } \times \mathbf { p } .
$$

# A.8 Rotation

Let us try to define a rotation vector θ whose magnitude is the angle of the rotation, θ, and whose direction is parallel to the axis of rotation, in the sense determined by a right-hand circulation rule. Unfortunately, this is not a good vector. The problem is that the addition of rotations is not commutative, whereas vector addition is commuative. Figure A.10 shows the effect of applying two successive $9 0 ^ { \circ }$ rotations, one about $\mathrm { O } x$ , and the other about the $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ , to a standard six-sided die. In the left-hand case, the $z$ -rotation is applied before the $x$ -rotation, and vice versa in the right-hand case. It can be seen that the die ends up in two completely different states. In other words, the $z$ -rotation plus the $x$ - rotation does not equal the $x$ -rotation plus the $z$ -rotation. This non-commuting algebra cannot be represented by vectors. So, although rotations have a well-defined magnitude and direction, they are not vector quantities.

But, this is not quite the end of the story. Suppose that we take a general vector a and rotate it about $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ by a small angle $\delta \mathsf { { \boldsymbol { \theta } } } _ { z }$ . This is equivalent to rotating the coordinate axes about the $\hphantom { - } O z$ by $- \delta \theta _ { z }$ . According to Equations (A.20)–(A.22), we have

$$
\mathbf { a } ^ { \prime } \simeq \mathbf { a } + \delta \theta _ { z } \mathbf { e } _ { z } \times \mathbf { a } ,
$$

where use has been made of the small angle approximations s $\mathrm { i n } \theta \simeq \theta$ and cos $\theta \simeq 1$ . The above equation can easily be generalized to allow small rotations about $\mathrm { O x }$ and $\mathrm { O y }$ by $\delta \mathsf { { \boldsymbol { \theta } } } _ { \mathsf { x } }$ and $\delta \theta _ { \mathfrak { y } }$ , respectively. We find that

$$
\mathbf { a } ^ { \prime } \simeq \mathbf { a } + \delta \boldsymbol { \Theta } \times \mathbf { a } ,
$$

![](images/0e21aafb35843adf8369f1d2a8537b96c8991ca6d5a5e45f3f502cb472a0399f.jpg)  
Figure A.8: A vector parallelogram.

![](images/762b8ad30a13a8464bed4c745fa1cbcd9c314ab6b6008b967105216d13a0c550.jpg)  
Figure A.9: A torque.

![](images/8220453703d1704b74e346032fbca80eb4cea24bd238935807bb19f9ae5830b5.jpg)  
Figure A.10: Effect of successive rotations about perpendicular axes on a six-sided die.

where

$$
\delta \mathbf { \boldsymbol { \Theta } } = \delta \boldsymbol { \Theta } _ { x } \mathbf { e } _ { x } + \delta \boldsymbol { \Theta } _ { y } \mathbf { e } _ { y } + \delta \boldsymbol { \Theta } _ { z } \mathbf { e } _ { z } .
$$

Clearly, we can define a rotation vector, δθ, but it only works for small angle rotations (i.e., sufficiently small that the small angle approximations of sine and cosine are good). According to the above equation, a small $z$ -rotation plus a small $x$ -rotation is (approximately) equal to the two rotations applied in the opposite order. The fact that infinitesimal rotation is a vector implies that angular velocity,

$$
\omega = \operatorname* { l i m } _ { \delta \mathrm { t } \to 0 } \frac { \delta \Theta } { \delta \mathrm { t } } ,
$$

must be a vector as well. Also, if $\mathbf { a } ^ { \prime }$ is interpreted as $\mathbf { a } ( \mathrm { t } + \delta \mathrm { t } )$ in Equation (A.46) then it follows that the equation of motion of a vector which precesses about the origin with some angular velocity ω is

$$
{ \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } = { \boldsymbol { \omega } } \times \mathbf { a } .
$$

# A.9 Scalar Triple Product

Consider three vectors a, b, and c. The scalar triple product is defined a $\mathbf { \nabla } \cdot \mathbf { b } \times \mathbf { c }$ . Now, $ { \mathbf { b } } \times  { \mathbf { c } }$ is the vector area of the parallelogram defined by b and c. So, $\mathbf { a } \cdot \mathbf { b } \times \mathbf { c }$ is the scalar area of this parallelogram multiplied by the component of a in the direction of its normal. It follows that a $\mathbf { \nabla } \cdot \mathbf { b } \times \mathbf { c }$ is the volume of the parallelepiped defined by vectors a, b, and c—see Figure A.11. This volume is independent of how the triple product is formed from a, b, and c, except that

$$
\mathbf { a } \cdot \mathbf { b } \times \mathbf { c } = - \mathbf { a } \cdot \mathbf { c } \times \mathbf { b } .
$$

So, the “volume” is positive if a, b, and c form a right-handed set (i.e., if a lies above the plane of b and c, in the sense determined from a right-hand circulation rule by rotating b onto c) and negative if they form a left-handed set. The triple product is unchanged if the dot and cross product operators are interchanged,

$$
\mathbf { a } \cdot \mathbf { b } \times \mathbf { c } = \mathbf { a } \times \mathbf { b } \cdot \mathbf { c } .
$$

The triple product is also invariant under any cyclic permutation of a, b, and c,

$$
\mathbf { a } \cdot \mathbf { b } \times \mathbf { c } = \mathbf { b } \cdot \mathbf { c } \times \mathbf { a } = \mathbf { c } \cdot \mathbf { a } \times \mathbf { b } ,
$$

but any anti-cyclic permutation causes it to change sign,

$$
\mathbf { a } \cdot \mathbf { b } \times \mathbf { c } = - \mathbf { b } \cdot \mathbf { a } \times \mathbf { c } .
$$

The scalar triple product is zero if any two of a, b, and c are parallel, or if a, b, and c are coplanar.

![](images/512530c38190f9b06b9bde59fefa7169a5d06fbfbd92f4707e171db023aefad7.jpg)  
Figure A.11: A vector parallelepiped.

If a, b, and c are non-coplanar then any vector r can be written in terms of them: i.e.,

$$
\mathbf { r } = \alpha \mathbf { a } + \beta \mathbf { b } + \gamma \mathbf { c } .
$$

Forming the dot product of this equation with $\mathbf { b } \times \mathbf { c } _ { \mathrm { : } }$ , we then obtain

$$
\mathbf { r } \cdot \mathbf { b } \times \mathbf { c } = \alpha \mathbf { a } \cdot \mathbf { b } \times \mathbf { c } ,
$$

so

$$
\alpha = \frac { \mathbf { r } \cdot \mathbf { b } \times \mathbf { c } } { \mathbf { a } \cdot \mathbf { b } \times \mathbf { c } } .
$$

Analogous expressions can be written for $\beta$ and $\gamma$ . The parameters $\alpha , \beta$ , and $\gamma$ are uniquely determined provided $\mathbf { a } \cdot \mathbf { b } \times \mathbf { c } \neq 0$ : i.e., provided that the three vectors are non-coplanar.

# A.10 Vector Triple Product

For three vectors a, b, and c, the vector triple product is defined $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } )$ . The brackets are important because $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) \neq ( \mathbf { a } \times \mathbf { b } ) \times \mathbf { c }$ . In fact, it can be demonstrated that

$$
\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) \equiv ( \mathbf { a } \cdot \mathbf { c } ) \mathbf { b } - ( \mathbf { a } \cdot \mathbf { b } ) \mathbf { c }
$$

and

$$
( \mathbf { a } \times \mathbf { b } ) \times \mathbf { c } \equiv ( \mathbf { a } \cdot \mathbf { c } ) \mathbf { b } - ( \mathbf { b } \cdot \mathbf { c } ) \mathbf { a } .
$$

Let us try to prove the first of the above theorems. The left-hand side and the right-hand side are both proper vectors, so if we can prove this result in one particular coordinate system then it must be true in general. Let us take convenient axes such that $\mathrm { O x }$ lies along b, and c lies in the $x { - } y$ plane. It follows that $\mathbf { b } \equiv ( \mathsf { b } _ { x } , 0 , 0 )$ , $\mathbf { c } \equiv ( \mathrm { c } _ { x } , \mathrm { c } _ { y } , 0 )$ , and $\mathbf { a } \equiv ( \mathbf { a } _ { x } , \mathbf { a } _ { y } , \mathbf { a } _ { z } )$ . The vector $\mathbf { b } \times \mathbf { c }$ is directed along $\boldsymbol { \mathrm { O } } \boldsymbol { z }$ : i.e., $\mathbf { b } \times \mathbf { c } \equiv ( 0 , 0 , \mathtt { b _ { x } c _ { y } } )$ . Hence, $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } )$ lies in the $x { - } y$ plane: i.e., $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) \equiv ( \mathbf { a } _ { \mathrm { y } } \mathbf { b } _ { x } \mathbf { c } _ { \mathrm { y } } , - \mathbf { a } _ { x } \mathbf { b } _ { x } \mathbf { c } _ { \mathrm { y } } , 0 ) .$ . This is the left-hand side of Equation (A.57) in our convenient coordinate system. To evaluate the right-hand side, we need $\mathbf { a } \cdot \mathbf { c } = \mathbf { a } _ { x } \mathbf { c } _ { x } + \mathbf { a } _ { y } \mathbf { c } _ { y }$ and a $\mathbf { \nabla } \cdot \mathbf { b } = \mathbf { a } _ { x } \mathbf { b } _ { x }$ . It follows that the righthand side is

$$
\begin{array} { l l l } { { \mathrm { R H S } } } & { { = } } & { { \left( \ \left[ { \bf { a } } _ { x } { \bf { c } } _ { x } + { \bf { a } } _ { y } { \bf { c } } _ { y } \right] { \bf { b } } _ { x } , 0 , 0 \right) - \left( { \bf { a } } _ { x } { \bf { b } } _ { x } { \bf { c } } _ { x } , { \bf { a } } _ { x } { \bf { b } } _ { x } { \bf { c } } _ { y } , 0 \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \left( { \bf { a } } _ { y } { \bf { c } } _ { y } { \bf { b } } _ { x } , - { \bf { a } } _ { x } { \bf { b } } _ { x } { \bf { c } } _ { y } , 0 \right) = { \bf { \mathrm { L H S } } } , } } \end{array}
$$

which proves the theorem.

# A.11 Vector Calculus

Suppose that vector a varies with time, so that $\mathbf { a } = \mathbf { a } ( \mathbf { t } )$ . The time derivative of the vector is defined

$$
\frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } = \operatorname* { l i m } _ { \delta \mathrm { t } \to 0 } \left[ \frac { \mathbf { a } ( \mathrm { t } + \delta \mathrm { t } ) - \mathbf { a } ( \mathrm { t } ) } { \delta \mathrm { t } } \right] .
$$

When written out in component form this becomes

$$
\frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } \equiv \left( \frac { \mathrm { d } \mathbf { a } _ { x } } { \mathrm { d t } } , \frac { \mathrm { d } \mathbf { a } _ { y } } { \mathrm { d t } } , \frac { \mathrm { d } \mathbf { a } _ { z } } { \mathrm { d t } } \right) .
$$

Suppose that a is, in fact, the product of a scalar $\Phi ( \mathbf { t } )$ and another vector ${ \bf b } ( \mathbf t )$ . What now is the time derivative of a? We have

$$
\frac { \mathrm { d } \mathbf { a } _ { x } } { \mathrm { d t } } = \frac { \mathrm { d } } { \mathrm { d t } } ( \phi \mathbf { b } _ { x } ) = \frac { \mathrm { d } \Phi } { \mathrm { d t } } \mathbf { b } _ { x } + \Phi \frac { \mathrm { d } \mathbf { b } _ { x } } { \mathrm { d t } } ,
$$

which implies that

$$
{ \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } = { \frac { \mathrm { d } \Phi } { \mathrm { d t } } } \mathbf { b } + \Phi { \frac { \mathrm { d } \mathbf { b } } { \mathrm { d t } } } .
$$

Moreover, it is easily demonstrated that

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \left( \mathbf { a } \cdot \mathbf { b } \right) = { \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } \cdot \mathbf { b } + \mathbf { a } \cdot { \frac { \mathrm { d } \mathbf { b } } { \mathrm { d t } } } ,
$$

and

$$
{ \frac { \mathrm { d } } { \mathrm { d t } } } \left( \mathbf { a } \times \mathbf { b } \right) = { \frac { \mathrm { d } \mathbf { a } } { \mathrm { d t } } } \times \mathbf { b } + \mathbf { a } \times { \frac { \mathrm { d } \mathbf { b } } { \mathrm { d t } } } .
$$

Hence, it can be seen that the laws of vector differentiation are analogous to those in conventional calculus.

# A.12 Line Integrals

Consider a two-dimensional function $\mathsf { f } ( { \mathsf { x } } , { \mathsf { y } } )$ which is defined for all $x$ and $_ { 9 }$ . What is meant by the integral of $\mathsf { f }$ along a given curve joining the points $\mathsf { P }$ and Q in the $x$ -y plane? Well, we first draw out f as a function of length l along the path—see Figure A.12. The integral is then simply given by

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \mathsf { f } ( x , y ) \mathrm { d } \mathsf { l } = \mathsf { A r e a u n d e r t h e c u r v e } ,
$$

where $\mathrm { d } \mathsf { l } = \sqrt { \mathrm { d } \mathsf { x } ^ { 2 } + \mathrm { d } \mathsf { y } ^ { 2 } }$ .

![](images/f0b244334cc64f2f73ad4bfeb4ea2d48d1f8dbb3223d2dd8dad750fd0ae89bd1.jpg)  
Figure A.12: A line integral.

![](images/a8e774f041cc11e4b0f9fc690d43aed0c3b7901969a3870fe2ee7a5d6b43177a.jpg)  
Figure A.13: An example line integral.

As an example of this, consider the integral of $\mathsf { f } ( \mathsf { x } , \mathsf { y } ) = \mathsf { x } \mathsf { y } ^ { 2 }$ between $\mathsf { P }$ and $\mathrm { Q }$ along the two routes indicated in Figure A.13. Along route 1 we have ${ \mathfrak { x } } = { \mathfrak { y } }$ , so ${ \mathrm { d } } 1 = { \sqrt { 2 } } { \mathrm { d } } x$ . Thus,

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } x \mathsf { y } ^ { 2 } \mathrm { d } \mathsf { l } = \int _ { 0 } ^ { 1 } x ^ { 3 } \sqrt { 2 } \mathrm { d } x = \frac { \sqrt { 2 } } { 4 } .
$$

The integration along route 2 gives

$$
{ \begin{array} { r l l } { \displaystyle \int _ { \mathsf { P } } ^ { \mathsf { Q } } x \ y ^ { 2 } { \mathrm { d } } { \mathsf { l } } } & { = } & { \displaystyle \int _ { 0 } ^ { 1 } x \ y ^ { 2 } { \mathrm { d } } x { \Biggl | } _ { { \mathsf { y } } = 0 } + \int _ { 0 } ^ { 1 } x \ y ^ { 2 } { \mathrm { d } } { \mathsf { y } } { \Biggl | } _ { x = 1 } } \\ & { = } & { 0 + \displaystyle \int _ { 0 } ^ { 1 } { \mathsf { y } } ^ { 2 } { \mathrm { d } } { \mathsf { y } } = { \frac { 1 } { 3 } } . } \end{array} }
$$

Note that the integral depends on the route taken between the initial and final points.

The most common type of line integral is that in which the contributions from dx and dy are evaluated separately, rather that through the path length dl: i.e.,

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \left[ \mathsf { f } \left( \mathsf { x } , \mathsf { y } \right) \mathrm { d } \mathsf { x } + \mathsf { g } ( \mathsf { x } , \mathsf { y } ) \ \mathrm { d } \mathsf { y } \right] .
$$

![](images/e2189d63c11d68fa110b38cc21c4ad63e6f3813d5a615d9f83031f4f32a2d728.jpg)  
Figure A.14: An example line integral.

As an example of this, consider the integral

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \left[ \mathsf { y } \mathrm { d } \mathsf { x } + \mathsf { x } ^ { 3 } \mathrm { d } \mathsf { y } \right]
$$

along the two routes indicated in Figure A.14. Along route 1 we have $x = y + 1$ and $\mathrm { d } x = \mathrm { d } y$ , so

$$
\int _ { \mathrm { p } } ^ { \mathrm { Q } } { \bigl [ } { \mathfrak { y } } \mathrm { { d } } { \mathfrak { x } } + { \mathfrak { x } } ^ { 3 } \mathrm { { d } } { \mathfrak { y } } { \bigr ] } = \int _ { 0 } ^ { 1 } { \bigl [ } { \mathfrak { y } } \mathrm { { d } } { \mathfrak { y } } + ( { \mathfrak { y } } + 1 ) ^ { 3 } \mathrm { { d } } { \mathfrak { y } } { \bigr ] } = { \frac { 1 7 } { 4 } } .
$$

Along route 2,

$$
\int _ { \mathsf { p } } ^ { \mathsf { Q } } \left[ \mathsf { y } \mathrm { d } x + x ^ { 3 } \mathrm { d } \mathsf { y } \right] = \int _ { 0 } ^ { 1 } x ^ { 3 } \mathrm { d } \mathsf { y } \bigg \vert _ { x = 1 } + \int _ { 1 } ^ { 2 } \mathsf { y } \mathrm { d } \mathsf { x } \bigg \vert _ { \mathsf { y } = 1 } = \frac { 7 } { 4 } .
$$

Again, the integral depends on the path of integration.

Suppose that we have a line integral which does not depend on the path of integration. It follows that

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \left( \mathsf { f } \mathrm { d } \mathsf { x } + \mathsf { g } \mathrm { d } \mathsf { y } \right) = \mathsf { F } ( \mathsf { Q } ) - \mathsf { F } ( \mathsf { P } )
$$

for some function F. Given $\mathsf { F } ( \mathsf { P } )$ for one point $\mathsf { P }$ in the $x { - } y$ plane, then

$$
\mathsf { F } ( \mathsf { Q } ) = \mathsf { F } ( \mathsf { P } ) + \int _ { \mathsf { P } } ^ { \mathsf { Q } } \big ( \mathsf { f } \ : \mathrm { d } \mathsf { x } + \mathsf { g } \ : \mathrm { d } \mathsf { y } \big )
$$

defines $\mathsf { F } ( \mathrm { Q } )$ for all other points in the plane. We can then draw a contour map of $\mathsf { F } ( { \boldsymbol { \mathsf { x } } } , { \boldsymbol { \mathsf { y } } } )$ . The line integral between points $\mathsf { P }$ and $\mathrm { Q }$ is simply the change in height in the contour map between these two points:

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \big ( \mathsf { f } \ : \mathrm { d } x + \mathsf { g } \ : \mathrm { d } \mathsf { y } \big ) = \int _ { \mathsf { P } } ^ { \mathsf { Q } } \mathrm { d } \mathsf { F } ( x , \mathsf { y } ) = \mathsf { F } ( \mathsf { Q } ) - \mathsf { F } ( \mathsf { P } ) .
$$

Thus,

$$
\mathrm { d } \mathsf { F } ( x , y ) = \mathsf { f } ( x , y ) \mathrm { d } x + \mathsf { g } ( x , y ) \mathrm { d } y .
$$

For instance, if $\mathsf { F } = \mathsf { x } ^ { 3 } \mathsf { y }$ then $\mathrm { d } \mathsf { F } = 3 x ^ { 2 } y \mathrm { d } x + x ^ { 3 } \mathrm { d } y$ and

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \left( 3 x ^ { 2 } y \mathrm { d } x + x ^ { 3 } \mathrm { d } y \right) = \left[ x ^ { 3 } y \right] _ { \mathsf { P } } ^ { \mathsf { Q } }
$$

is independent of the path of integration.

It is clear that there are two distinct types of line integral. Those which depend only on their endpoints and not on the path of integration, and those which depend both on their endpoints and the integration path. Later on, we shall learn how to distinguish between these two types (see Section A.15).

# A.13 Vector Line Integrals

A vector field is defined as a set of vectors associated with each point in space. For instance, the velocity $\mathbf { v } ( \mathbf { r } )$ in a moving liquid (e.g., a whirlpool) constitutes a vector field. By analogy, a scalar field is a set of scalars associated with each point in space. An example of a scalar field is the temperature distribution ${ { \sf T } } ( { \bf r } )$ in a furnace.

Consider a general vector field $\mathbf { A } ( \mathbf { r } )$ . Let $\mathbf { d r } \equiv ( \mathrm { d } \mathsf { x } , \mathrm { d } \mathsf { y } , \mathrm { d } z )$ be the vector element of line length. Vector line integrals often arise as

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } \mathbf { A } \cdot \mathrm { d } \mathbf { r } = \int _ { \mathsf { P } } ^ { \mathsf { Q } } ( { \mathsf { A } } _ { x } \mathrm { d } x + { \mathsf { A } } _ { \mathsf { y } } \mathrm { d } \mathsf { y } + { \mathsf { A } } _ { z } \mathrm { d } z ) .
$$

For instance, if A is a force-field then the line integral is the work done in going from $\mathsf { P }$ to Q.

As an example, consider the work done by a repulsive inverse-square central field, ${ \bf F } = - { \bf r } / | { \bf r } ^ { 3 } |$ . The element of work done is $\mathrm { d } { \boldsymbol { W } } = \mathbf { F } .$ ·dr. Take $\mathsf { P } = ( \infty , 0 , 0 )$ and $Q = ( \mathbf { a } , 0 , 0 )$ . Route 1 is along the $x$ -axis, so

$$
W = \int _ { \infty } ^ { \mathrm { a } } \left( - { \frac { 1 } { x ^ { 2 } } } \right) \mathrm { d } x = \left[ { \frac { 1 } { x } } \right] _ { \infty } ^ { \mathrm { a } } = { \frac { 1 } { \mathrm { a } } } .
$$

The second route is, firstly, around a large circle $\mathbf { \hat { r } = }$ constant) to the point $( \mathrm { a } , \infty , 0 )$ , and then parallel to the $_ { 9 }$ -axis—see Figure A.15. In the first part, no work is done, since $\mathbf { F }$ is perpendicular to dr. In the second part,

$$
W = \int _ { \infty } ^ { 0 } { \frac { - y \mathrm { \ d y } } { ( \mathbf { a } ^ { 2 } + \mathbf { y } ^ { 2 } ) ^ { 3 / 2 } } } = \left[ { \frac { 1 } { ( { \mathbf { y } } ^ { 2 } + \mathbf { a } ^ { 2 } ) ^ { 1 / 2 } } } \right] _ { \infty } ^ { \circ } = { \frac { 1 } { \mathbf { a } } } .
$$

In this case, the integral is independent of the path. However, not all vector line integrals are path independent.

![](images/52af1814a15e5d56ae8d5f849904f8c18830c6d604e26cc3aa0311a4e2ca09da.jpg)  
Figure A.15: An example vector line integral.

# A.14 Volume Integrals

A volume integral takes the form

$$
\iint \int _ { \mathsf { V } } \boldsymbol { \mathsf { f } } ( x , y , z ) \mathrm { d } \mathsf { V } ,
$$

where $\vee$ is some volume, and $\mathrm { d } \mathrm { V } = \mathrm { d } { \tt x } \mathrm { d } { \tt y } \mathrm { d } z$ is a small volume element. The volume element is sometimes written $\mathrm { d } ^ { 3 } \mathbf { r } _ { ; }$ , or even $\mathtt { d } \tau$ .

As an example of a volume integral, let us evaluate the center of gravity of a solid pyramid. Suppose that the pyramid has a square base of side a, a height a, and is composed of material of uniform density. Let the centroid of the base lie at the origin, and let the apex lie at $( 0 , 0 , \mathfrak { a } )$ . By symmetry, the center of mass lies on the line joining the centroid to the apex. In fact, the height of the center of mass is given by

$$
{ \overline { { z } } } = \operatorname { \mathrm { \iint } } \int z \operatorname { d V } { \bigg / } \int \operatorname { \mathrm { \iint } } \mathrm { d V } .
$$

The bottom integral is just the volume of the pyramid, and can be written

$$
\begin{array} { r c l } { \displaystyle \iint \mathrm { d } V } & { = } & { \displaystyle \int _ { 0 } ^ { \mathrm { a } } \mathrm { d } z \int _ { - ( \mathrm { a } - z ) / 2 } ^ { ( \mathrm { a } - z ) / 2 } \mathrm { d } \mathsf { y } \int _ { - ( \mathrm { a } - z ) / 2 } ^ { ( \mathrm { a } - z ) / 2 } \mathrm { d } x = \displaystyle \int _ { 0 } ^ { \mathrm { a } } ( \mathrm { a } - z ) ^ { 2 } \mathrm { d } z = \int _ { 0 } ^ { \mathrm { a } } ( \mathrm { a } ^ { 2 } - 2 \mathrm { a } z + z ^ { 2 } ) } \\ & { = } & { \displaystyle \left[ \mathrm { a } ^ { 2 } z - \mathrm { a } z ^ { 2 } + z ^ { 3 } / 3 \right] _ { 0 } ^ { \mathrm { a } } = \frac { 1 } { 3 } \mathrm { a } ^ { 3 } . } \end{array}
$$

Here, we have evaluated the $z$ -integral last because the limits of the $x -$ and $_ { 9 }$ - integrals are $z$ -dependent. The top integral takes the form

$$
\begin{array} { r c l } { { \displaystyle \iint z \mathrm { d } V } } & { { = } } & { { \displaystyle \int _ { 0 } ^ { \mathrm { a } } z \mathrm { d } z \int _ { - ( \mathrm { a } - z ) / 2 } ^ { ( \mathrm { a } - z ) / 2 } \mathrm { d } \mathrm { y } \int _ { - ( \mathrm { a } - z ) / 2 } ^ { ( \mathrm { a } - z ) / 2 } \mathrm { d } x = \int _ { 0 } ^ { \mathrm { a } } z \left( \mathrm { a } - z \right) ^ { 2 } \mathrm { d } z = \int _ { 0 } ^ { \mathrm { a } } \left( z \mathrm { a } ^ { 2 } - 2 \alpha z ^ { 2 } \right) } } \\ { { } } & { { = } } & { { \left[ \mathrm { a } ^ { 2 } z ^ { 2 } / 2 - 2 \mathrm { a } z ^ { 3 } / 3 + z ^ { 4 } / 4 \right] _ { \diamond } ^ { \mathrm { a } } = \displaystyle \frac { 1 } { 1 2 } \mathrm { a } ^ { 4 } . } } \end{array}
$$

![](images/b366104e957726088192993f8b4e485d9d1713f1ba5bec6c5f40bc0bc373c23b.jpg)  
Figure A.16: A two-dimensional gradient.

Thus,

$$
\bar { z } = \frac { 1 } { 1 2 } { \bf a } ^ { 4 } \bigg / \frac { 1 } { 3 } { \bf a } ^ { 3 } = \frac { 1 } { 4 } { \bf a } .
$$

In other words, the center of mass of a pyramid lies one quarter of the way between the centroid of the base and the apex.

# A.15 Gradient

A one-dimensional function $\mathsf { f } ( { \boldsymbol { x } } )$ has a gradient $\operatorname { d f } / \operatorname { d x }$ which is defined as the slope of the tangent to the curve at $x$ . We wish to extend this idea to cover scalar fields in two and three dimensions.

Consider a two-dimensional scalar field $\mathtt { h } ( \mathtt { x } , \mathtt { y } )$ , which is (say) height above sea-level in a hilly region. Let $\mathrm { d } \mathbf { r } \equiv ( \mathrm { d } \mathsf { x } , \ \mathrm { d } \mathsf { y } )$ be an element of horizontal distance. Consider dh/dr, where dh is the change in height after moving an infinitesimal distance dr. This quantity is somewhat like the one-dimensional gradient, except that dh depends on the direction of dr, as well as its magnitude. In the immediate vicinity of some point P, the slope reduces to an inclined plane—see Figure A.16. The largest value of $\operatorname { d h } / \operatorname { d r }$ is straight up the slope. It is easily shown that for any other direction

$$
\frac { \mathrm { d } \mathrm { h } } { \mathrm { d } \mathrm { r } } = \left( \frac { \mathrm { d } \mathrm { h } } { \mathrm { d } \mathrm { r } } \right) _ { \mathrm { m a x } } \cos { \theta } ,
$$

where θ is the angle shown in Figure A.16. Let us define a two-dimensional vector, grad h, called the gradient of $\mathsf { h }$ , whose magnitude is $( \mathrm { d h / d r } ) _ { \mathrm { m a x } }$ , and whose direction is the direction of steepest ascent. The cos θ variation exhibited in the above expression ensures that the component of grad h in any direction is equal to $\operatorname { d h } / \operatorname { d r }$ for that direction.

The component of $\operatorname { d h } / \operatorname { d r }$ in the $x$ -direction can be obtained by plotting out the profile of $\mathrm { \hslash }$ at constant $_ { 9 }$ , and then finding the slope of the tangent to the curve at given $x$ . This quantity is known as the partial derivative of $\mathrm { \hslash }$ with respect to $x$ at constant $_ { 9 }$ , and is denoted $\left( \partial \mathsf { h } / \partial \mathsf { x } \right) _ { \mathsf { y } }$ . Likewise, the gradient of the profile at constant $x$ is written $( \mathsf { { 0 h } } / \mathsf { { 0 y } } ) _ { x }$ . Note that the subscripts denoting constant- $x$ and constant- $^ { \cdot 9 }$ are usually omitted, unless there is any ambiguity. If follows that in component form

$$
{ \bf g r a d } { \bf h } \equiv \left( \frac { \partial { \bf h } } { \partial x } , \frac { \partial { \bf h } } { \partial y } \right) .
$$

Now, the equation of the tangent plane at $\mathsf { P } = \left( \mathsf { x } _ { 0 } , \mathsf { y } _ { 0 } \right)$ i s

$$
\mathrm { h } _ { \mathsf { T } } ( { \boldsymbol { x } } , { \boldsymbol { y } } ) = \mathrm { h } ( x _ { 0 } , \mathsf { y } _ { 0 } ) + \alpha ( { \boldsymbol { x } } - { \boldsymbol { x } } _ { 0 } ) + \beta ( \mathsf { y } - \mathsf { y } _ { 0 } ) .
$$

This has the same local gradients as $\mathtt { h } ( \mathtt { x } , \mathtt { y } )$ , so

$$
\alpha = \frac { \partial \mathrm { h } } { \partial \mathrm { x } } , \beta = \frac { \partial \mathrm { h } } { \partial \mathrm { y } } ,
$$

by differentiation of the above. For small $\mathrm { d } \boldsymbol { \mathrm { x } } = \boldsymbol { \mathrm { x } } - \boldsymbol { \mathrm { x } } _ { 0 }$ and $\mathrm { d } \mathsf { y } = \mathsf { y } - \mathsf { y } _ { 0 }$ , the function $\mathrm { \hslash }$ is coincident with the tangent plane, so

$$
\mathrm { d } \mathrm { h } = \frac { \partial \mathrm { h } } { \partial \mathrm { x } } \mathrm { d } \mathrm { x } + \frac { \partial \mathrm { h } } { \partial \mathrm { y } } \mathrm { d } \mathrm { y } .
$$

But, grad $\mathsf { h } \equiv ( \partial \mathsf { h } / \partial \mathsf { x } , \partial \mathsf { h } / \partial \mathsf { y } )$ and $\mathrm { d } \mathbf { r } \equiv ( \mathrm { d } \mathsf { x } , \ \mathrm { d } \mathsf { y } )$ , so

$$
\mathrm { d h } = \mathbf { g r a d h } \cdot \mathrm { d r } .
$$

Incidentally, the above equation demonstrates that grad $\mathrm { \hslash }$ is a proper vector, since the lefthand side is a scalar, and, according to the properties of the dot product, the right-hand side is also a scalar provided that dr and grad h are both proper vectors (dr is an obvious vector, because it is directly derived from displacements).

Consider, now, a three-dimensional temperature distribution $\mathsf { T } ( \boldsymbol { x } , \boldsymbol { y } , z )$ in (say) a reaction vessel. Let us define grad T, as before, as a vector whose magnitude is $( \mathrm { d } \mathsf { T } / \mathrm { d } \mathsf { r } ) _ { \mathrm { m a x } }$ , and whose direction is the direction of the maximum gradient. This vector is written in component form

$$
\mathbf { g r a d } \top \equiv \left( { \frac { \partial \mathsf { T } } { \partial x } } , { \frac { \partial \mathsf { T } } { \partial y } } , { \frac { \partial \mathsf { T } } { \partial z } } \right) .
$$

Here, $\partial \mathsf { T } / \partial x \equiv ( \partial \mathsf { T } / \partial x ) _ { \mathsf { y } , z }$ is the gradient of the one-dimensional temperature profile at constant $_ { 9 }$ and $z$ . The change in $\intercal$ in going from point $\mathsf { P }$ to a neighbouring point offset by $\mathrm { d } \mathbf { r } \equiv ( \mathrm { d } \mathsf { x } , \ \mathrm { d } \mathsf { y } , \ \mathrm { d } z )$ i s

$$
\mathrm { d } \mathsf { T } = \frac { \partial \mathsf { T } } { \partial \boldsymbol { x } } \mathrm { d } \boldsymbol { x } + \frac { \partial \mathsf { T } } { \partial \boldsymbol { y } } \mathrm { d } \boldsymbol { y } + \frac { \partial \mathsf { T } } { \partial \boldsymbol { z } } \mathrm { d } \boldsymbol { z } .
$$

In vector form, this becomes

$$
\mathrm { d } \mathsf { T } = \mathbf { g r a d } \mathsf { T } \cdot \mathrm { d } \mathbf { r } .
$$

![](images/b38a24dccf3342ec5471841a8940794c24761b298b504f675bfde3e6a566c815.jpg)  
Figure A.17: Isotherms.

Suppose that $\mathrm { d } \mathsf { T } = 0$ for some dr. It follows that

$$
\mathbf { d } \mathsf { T } = \mathbf { g r a d } \mathsf { T } \cdot \mathbf { d r } = 0 .
$$

So, dr is perpendicular to grad T. Since $\mathrm { d } \mathsf { T } = 0$ along so-called “isotherms” (i.e., contours of the temperature), we conclude that the isotherms (contours) are everywhere perpendicular to grad T—see Figure A.17.

It is, of course, possible to integrate dT . For instance, the line integral of dT between points $\mathsf { P }$ and $\mathrm { Q }$ is written

$$
\int _ { \mathsf { P } } ^ { \mathsf { Q } } { \mathrm { d } \mathsf { T } } = \int _ { \mathsf { P } } ^ { \mathsf { Q } } { \mathbf { g r a d } \mathsf { T } } \cdot { \mathrm { d } \mathsf { r } } = \mathsf { T } ( \mathsf { Q } ) - \mathsf { T } ( \mathsf { P } ) .
$$

This integral is clearly independent of the path taken between $\mathsf { P }$ and $\mathrm { Q }$ , so $\int _ { \mathbb { P } } ^ { \mathrm { Q } } \mathbf { g r a d T } \cdot \mathrm { d } \mathbf { r }$ must be path independent.

Consider a vector field $\mathbf { A } ( \mathbf { r } )$ . In general, the line integral $\int _ { \mathsf { P } } ^ { \mathrm { Q } } \mathbf { A } \cdot \mathrm { d } \mathbf { r }$ depends on the path taken between the end points, but for some special vector fields the integral is path independent. Such fields are called conservative fields. It can be shown that if A is a conservative field then $\mathbf { A } = \mathbf { g r a d } \mathrm { V }$ for some scalar field $\vee$ . The proof of this is straightforward. Keeping $\mathsf { P }$ fixed, we have

$$
\int _ { \mathbb { P } } ^ { \mathbb { Q } } \mathbf { A } \cdot \mathrm { d } \mathbf { r } = \mathsf { V } ( \mathbb { Q } ) ,
$$

where $\mathsf { V } ( \mathrm { Q } )$ is a well-defined function, due to the path independent nature of the line integral. Consider moving the position of the end point by an infinitesimal amount $\mathtt { d } x$ in the $x$ -direction. We have

$$
V ( \mathbf { Q } + \mathbf { d } \mathbf { x } ) = V ( \mathbf { Q } ) + \int _ { \mathbf { Q } } ^ { \mathbf { Q } + \mathrm { d } \mathbf { x } } \mathbf { A } \cdot \mathbf { d } \mathbf { r } = \mathbf { V } ( \mathbf { Q } ) + A _ { \mathbf { x } } \mathbf { d } \mathbf { x } .
$$

Hence,

$$
\frac { \partial V } { \partial x } = \lambda _ { x } ,
$$

with analogous relations for the other components of A. It follows that

$$
\mathbf { A } = \mathbf { g r a d } \mathrm { V } .
$$

In Newtonian dynamics, the force due to gravity is a good example of a conservative field. Now, if $\mathbf { A } ( \mathbf { r } )$ is a force-field then $\int \mathbf { A } \cdot \mathrm { d } \mathbf { r }$ is the work done in traversing some path. If A is conservative then

$$
\oint \mathbf { A } \cdot \mathrm { d } \mathbf { r } = 0 ,
$$

where $\oint$ corresponds to the line integral around a closed loop. The fact that zero net work is done in going around a closed loop is equivalent to the conservation of energy (which is why conservative fields are called “conservative”). A good example of a non-conservative field is the force due to friction. Clearly, a frictional system loses energy in going around a closed cycle, so $\oint \mathbf { A } \cdot \mathrm { d } \mathbf { r } \neq 0$ .

# A.16 Grad Operator

It is useful to define the vector operator

$$
\nabla \equiv \left( \frac { \partial } { \partial x } , \frac { \partial } { \partial y } , \frac { \partial } { \partial z } \right) ,
$$

which is usually called the grad or del operator. This operator acts on everything to its right in a expression, until the end of the expression or a closing bracket is reached. For instance,

$$
{ \bf { g r a d f } } = \nabla \mathsf { f } \equiv \left( { \frac { \partial \mathsf { f } } { \partial \mathsf { x } } } , { \frac { \partial \mathsf { f } } { \partial \mathsf { y } } } , { \frac { \partial \mathsf { f } } { \partial z } } \right) .
$$

For two scalar fields $\Phi$ and $\psi$ ,

$$
\mathbf { g r a d } \left( \Phi \Psi \right) = \Phi \mathbf { \Psi } \mathbf { g r a d } \Psi + \Psi \mathbf { \Psi } \mathbf { \overrightarrow { g r a d } } \Phi
$$

can be written more succinctly as

$$
\nabla ( \Phi \Psi ) = \Phi \nabla \Psi + \Psi \nabla \Phi .
$$

Suppose that we rotate the coordinate axes through an angle $\theta$ about $\hphantom { - } O z$ . By analogy with Equations (A.17)–(A.19), the old coordinates $\left( x , ~ y , ~ z \right)$ are related to the new ones $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ via

$$
\begin{array}{c} { \begin{array} { l } { { \mathfrak { x } } } \end{array} } = \ x ^ { \prime } \cos \theta - { \mathfrak { y ^ { \prime } } } \sin \theta ,  \\ { { \mathfrak { y } } } \ = \ x ^ { \prime } \sin \theta + { \mathfrak { y ^ { \prime } } } \cos \theta ,  \\ { z \ = \ z ^ { \prime } . } \end{array} 
$$

![](images/5b466fdf3f144fbbfa0c8ee74e2d435afc10b8fb9526282963df6242e7577482.jpg)  
Figure A.18: Cylindrical polar coordinates.

Now,

$$
\frac { \partial } { \partial x ^ { \prime } } = \left( \frac { \partial x } { \partial x ^ { \prime } } \right) _ { \mathsf { y } ^ { \prime } , z ^ { \prime } } \frac { \partial } { \partial x } + \left( \frac { \partial \mathsf { y } } { \partial x ^ { \prime } } \right) _ { \mathsf { y } ^ { \prime } , z ^ { \prime } } \frac { \partial } { \partial \mathsf { y } } + \left( \frac { \partial z } { \partial x ^ { \prime } } \right) _ { \mathsf { y } ^ { \prime } , z ^ { \prime } } \frac { \partial } { \partial z } ,
$$

giving

$$
\frac { \partial } { \partial x ^ { \prime } } = \cos \theta \frac { \partial } { \partial x } + \sin \theta \frac { \partial } { \partial y } ,
$$

and

$$
\nabla _ { x ^ { \prime } } = \cos \theta \nabla _ { x } + \sin \theta \nabla _ { y } .
$$

It can be seen, from Equations (A.20)–(A.22), that the differential operator $\nabla$ transforms in an analogous manner to a vector. This is another proof that $\nabla \mathsf { f }$ is a good vector.

# A.17 Curvilinear Coordinates

In the cylindrical coordinate system, the Cartesian coordinates $x$ and $_ { 9 }$ are replaced by $\mathsf { r } = \sqrt { \mathsf { x } ^ { 2 } + \mathsf { y } ^ { 2 } }$ and $\theta = \tan ^ { - 1 } ( y / x )$ . Here, $\boldsymbol { \mathsf { r } }$ is the perpendicular distance from the $z$ -axis, and $\theta$ the angle subtended between the perpendicular radius vector and the $x$ -axis—see Figure A.18. A general vector A is thus written

$$
\mathbf { A } = \mathsf { A } _ { \mathrm { r } } \mathbf { e } _ { \mathrm { r } } + \mathsf { A } _ { \theta } \mathbf { e } _ { \theta } + \mathsf { A } _ { z } \mathbf { e } _ { z } ,
$$

where $\mathbf { e } _ { \mathrm { { r } } } = \nabla \mathrm { r } / | \nabla \mathrm { r } |$ and $\begin{array} { r } { \mathbf { e } _ { \theta } = \nabla \theta / | \nabla \theta | . } \end{array}$ —see Figure A.18. Note that the unit vectors $\mathbf { e } _ { \mathrm { r } }$ , $\mathbf { e } _ { \theta }$ , and $\mathbf { e } _ { z }$ are mutually orthogonal. Hence, $\lambda _ { \mathrm { r } } = { \bf A } \cdot { \bf e } _ { \mathrm { r } }$ , etc. The volume element in this coordinate system is $\mathrm { d } ^ { 3 } \mathbf { r } = \mathrm { r } \mathop { } \mathrm { d } \mathrm { r } \mathop { } \mathrm { d } \theta \mathop { } \mathrm { d } z$ . Moreover, the gradient of a general scalar field $\mathsf { V } ( \mathbf { r } )$ takes the form

$$
\nabla \mathsf { V } = \frac { \partial \mathsf { V } } { \partial \mathsf { r } } \mathbf { e } _ { \mathrm { r } } + \frac { 1 } { r } \frac { \partial \mathsf { V } } { \partial \theta } \mathbf { e } _ { \theta } + \frac { \partial \mathsf { V } } { \partial z } \mathbf { e } _ { z } .
$$

![](images/e5ab8fa82945928e43d4cc95877609caea13ba40c1ac3c76b92145634ee3445a.jpg)  
Figure A.19: Spherical polar coordinates.

In the spherical coordinate system, the Cartesian coordinates $x , y$ , and $z$ are replaced by $\mathfrak { r } = \sqrt { \mathfrak { x } ^ { 2 } + \mathfrak { y } ^ { 2 } + z ^ { 2 } }$ , $\theta = \cos ^ { - 1 } ( z / r )$ , and $\Phi = \tan ^ { - 1 } ( { \mathsf { y } } / { \mathsf { x } } )$ . Here, $\boldsymbol { \mathsf { r } }$ is the radial distance from the origin, θ the angle subtended between the radius vector and the $z$ -axis, and $\Phi$ the angle subtended between the projection of the radius vector onto the $x { - } y$ plane and the $x$ -axis—see Figure A.19. Note that r and $\theta$ in the spherical system are not the same as their counterparts in the cylindrical system. A general vector A is written

$$
\mathbf { A } = \mathsf { A } _ { \mathrm { r } } \mathbf { e } _ { \mathrm { r } } + \mathsf { A } _ { \theta } \mathbf { e } _ { \theta } + \mathsf { A } _ { \phi } \mathbf { e } _ { \phi } ,
$$

where $\mathbf { e } _ { \mathrm { { r } } } = \nabla \mathrm { r } / | \nabla \mathrm { r } |$ , $\mathbf { e } _ { \theta } = \nabla \theta / | \nabla \theta | .$ , and $\mathbf { e } _ { \Phi } = \nabla \Phi / | \nabla \Phi |$ . The unit vectors $\mathbf { e } _ { \mathrm { r } } , \mathbf { e } _ { \mathrm { \theta } }$ , and $\mathbf { e } _ { \phi }$ are mutually orthogonal. Hence, $\lambda _ { \mathrm { r } } = { \bf A } \cdot { \bf e } _ { \mathrm { r } }$ , etc. The volume element in this coordinate system is $\mathrm { d } ^ { 3 } \mathbf { r } = \mathrm { r } ^ { 2 }$ sin θ dr dθ dφ. Moreover, the gradient of a general scalar field $\mathsf { V } ( \mathbf { r } )$ takes the form

$$
\nabla \mathsf { V } = \frac { \partial \mathsf { V } } { \partial \mathsf { r } } \mathbf { e } _ { \mathrm { r } } + \frac { 1 } { r } \frac { \partial \mathsf { V } } { \partial \theta } \mathbf { e } _ { \theta } + \frac { 1 } { r \sin \theta } \frac { \partial \mathsf { V } } { \partial \phi } \mathbf { e } _ { \phi } .
$$

# A.18 Exercises

A.1. The position vectors of the four points A, B, C, and $_ \mathrm { D }$ are a, b, $3 \mathbf { a } + 2 \mathbf { b }$ , and a − 3 b, respectively. Express →AC, →DB, →BC, and $\begin{array} { r l r l } {  } & { { }  } & {  } & { { } } \end{array}$ $\vec { \mathrm { C D } }$ in terms of a and b.

A.2. Prove the trigonometric law of sines

$$
{ \frac { \sin \mathbf { a } } { \mathbf { A } } } = { \frac { \sin \mathbf { b } } { \mathbf { B } } } = { \frac { \sin \mathbf { c } } { \mathbf { C } } }
$$

using vector methods. Here, ${ \mathfrak { a } } , { \mathfrak { b } }$ , and c are the three angles of a plane triangle, and A, B, and C the lengths of the corresponding opposite sides.

A.3. Demonstrate using vectors that the diagonals of a parallelogram bisect one another. In addition, show that if the diagonals of a quadrilateral bisect one another then it is a parallelogram.

A.4. From the inequality

$$
\mathbf { a } \cdot \mathbf { b } = | \mathbf { a } | | \mathbf { b } | \cos \theta \leq | \mathbf { a } | | \mathbf { b } |
$$

deduce the triangle inequality

$$
| \mathbf { a } + \mathbf { b } | \leq | \mathbf { a } | + | \mathbf { b } | .
$$

A.5. Find the scalar product a $\cdot$ b and the vector product $\mathbf { a } \times \mathbf { b }$ when

$$
\begin{array} { r l } & { \mathbf { a } = \mathbf { e } _ { x } + 3 \mathbf { e } _ { y } - \mathbf { e } _ { z } , \quad \mathbf { b } = 3 \mathbf { e } _ { x } + 2 \mathbf { e } _ { y } + \mathbf { e } _ { z } , } \\ & { \mathbf { a } = \mathbf { e } _ { x } - 2 \mathbf { e } _ { y } + \mathbf { e } _ { z } , \quad \mathbf { b } = 2 \mathbf { e } _ { x } + \mathbf { e } _ { y } + \mathbf { e } _ { z } . } \end{array}
$$

A.6. Which of the following statements regarding the three general vectors a, b, and c are true?

(a) $\mathbf { c } \cdot ( \mathbf { a } \times \mathbf { b } ) = ( \mathbf { b } \times \mathbf { a } ) \cdot \mathbf { c } .$   
(b) $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) = ( \mathbf { a } \times \mathbf { b } ) \times \mathbf { c } .$   
(c) $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) = ( \mathbf { a } \cdot \mathbf { c } ) \mathbf { b } - ( \mathbf { a } \cdot \mathbf { b } ) \mathbf { c } .$   
(d) $\mathbf { d } = \lambda \mathbf { a } + \mu \mathbf { b }$ implies that $( { \mathbf { a } } \times { \mathbf { b } } ) \cdot { \mathbf { d } } = 0$ .   
(e) $\mathbf { a } \times \mathbf { c } = \mathbf { b } \times \mathbf { c }$ implies that $\mathbf { c } \cdot \mathbf { a } - \mathbf { c } \cdot \mathbf { b } = \mathbf { c } \left| \mathbf { a } - \mathbf { b } \right|$ . (f) $( \mathbf { a } \times \mathbf { b } ) \times ( \mathbf { c } \times \mathbf { b } ) = [ \mathbf { b } \cdot ( \mathbf { c } \times \mathbf { a } ) ] \mathbf { b } .$

A.7. Prove that the length of the shortest straight-line from point a to the straight-line joining points $\mathbf { b }$ and c is

$$
{ \frac { | \mathbf { a } \times \mathbf { b } + \mathbf { b } \times \mathbf { c } + \mathbf { c } \times \mathbf { a } | } { | \mathbf { b } - \mathbf { c } | } } .
$$

A.8. Identify the following surfaces:

(a) $\scriptstyle { \begin{array} { l } { | \mathbf { r } | = \mathbf { a } , } \\ { \mathbf { r } \cdot \mathbf { n } = \mathbf { b } , } \\ { \mathbf { r } \cdot \mathbf { n } = c \left| \mathbf { r } \right| , } \\ { \left| \mathbf { r } - \left( \mathbf { r } \cdot \mathbf { n } \right) \mathbf { n } \right| = { \frac { } { } } } \end{array} }$ (b) (c) (d)

Here, $\mathbf { r }$ is the position vector, a, b, c, and $\mathrm { d }$ are positive constants, and n is a fixed unit vector.

A.9. Let a, $\mathbf { b }$ , and c be coplanar vectors related via

$$
\alpha \mathbf { a } + \beta \mathbf { b } + \gamma \mathbf { c } = \mathbf { 0 } ,
$$

where $\alpha , ~ \beta$ , and $\gamma$ are not all zero. Show that the condition for the points with position vectors u a, $\nu \mathbf { b }$ , and $_ { w \mathbf { c } }$ to be colinear is

$$
\frac { \alpha } { \mathrm { u } } + \frac { \beta } { \nu } + \frac { \gamma } { \nu } = 0 .
$$

A.10. If p, q, and $\mathbf { r }$ are any vectors, demonstrate that $\mathbf { a } = \mathbf { q } + \lambda \mathbf { r }$ , $\mathbf { b } = \mathbf { r } + \mu \mathbf { p }$ , and $\mathbf { c } = \mathbf { p } + \mathsf { v } \mathbf { q }$ are coplanar provided that $\lambda \mu \nu = - 1$ , where $\lambda , \mu ,$ and $\boldsymbol { \mathsf { v } }$ are scalars. Show that this condition is satisfied when a is perpendicular to $\mathbf { p }$ , b to $\mathbf { q } .$ , and c to r.

A.11. The vectors a, b, and c are non-coplanar, and form a non-orthogonal vector base. The vectors A, B, and C, defined by

$$
\mathbf { A } = { \frac { \mathbf { b } \times \mathbf { c } } { \mathbf { a } \cdot \mathbf { b } \times \mathbf { c } } } ,
$$

plus cyclic permutations, are said to be reciprocal vectors. Show that

$$
\mathbf { a } = ( \mathbf { B } \times \mathbf { C } ) / ( \mathbf { A } \cdot \mathbf { B } \times \mathbf { C } ) ,
$$

plus cyclic permutations.

A.12. In the notation of the previous question, demonstrate that the plane passing through points ${ \mathbf a } / { \alpha } , { \mathbf b } / { \boldsymbol { \beta } }$ , and $\mathbf { c } / \gamma$ is normal to the direction of the vector

$$
\mathbf { h } = \alpha \mathbf { A } + \beta \mathbf { B } + \gamma \mathbf { C } .
$$

In addition, show that the perpendicular distance of the plane from the origin is $| \mathbf { h } | ^ { - 1 }$ .

A.13. Evaluate $\oint \mathbf { A } \cdot$ dr for

$$
\mathbf { A } = { \frac { \mathbf { x e } _ { x } + \mathbf { y e } _ { y } } { \sqrt { x ^ { 2 } + { y } ^ { 2 } } } }
$$

around the square whose sides are $\mathbf { x } = 0 , \mathbf { x } = \mathbf { a } , \mathbf { y } = 0 , \mathbf { y } = \mathbf { a } .$

A.14. Find the gradients of the following scalar functions of the position vector $\mathbf { r } = ( x , y , z )$

(a) $\begin{array} { r l } & { \mathbf { k } \cdot \mathbf { r } , } \\ & { | \mathbf { r } | ^ { n } , } \\ & { | \mathbf { r } - \mathbf { k } | ^ { - \mathrm { n } } , } \\ & { { \cos } ( \mathbf { k } \cdot \mathbf { r } ) . } \end{array}$ (b) (c) (d)

Here, $\mathbf { k }$ is a fixed vector.


<!-- chunk 0004: pages 211-216 -->
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
