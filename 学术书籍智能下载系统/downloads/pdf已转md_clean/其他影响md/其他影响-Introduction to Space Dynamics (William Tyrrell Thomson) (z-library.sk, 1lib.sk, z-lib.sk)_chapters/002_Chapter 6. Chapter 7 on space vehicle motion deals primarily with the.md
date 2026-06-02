Chapter 6. Chapter 7 on space vehicle motion deals primarily with the
attitude of spinning rockets, missiles, and satellites. The effect of
thrust misalignment, unbalance in inertia, variable mass, and changing
configuration are analyzed. Special techniques for the transformation of
motion from body coordinates to inertial coordinates are covered in this
chapter. Optimization with respect to performance of rockets is a
subject which can be treated at great length. Chapter 8 is a brief
introduction to this subject, first in terms of multistage rockets in
vertical flight and, later, in terms of single-stage rockets moving
along curved trajectories. Aerodynamic forces are omitted in the
discussion, not because they are unimportant but because their inclusion
renders the problem unmanageable from the analytical point of view.
Finally, the last chapter presents the generalized theories of Hamilton
and Lagrange which unite the field of mechanics in an over-all
formulation. The presentation is from the variational approach which has
the advantage of providing greater generality and clarity.

This book can be used at the intermediate or graduate level of
instruction. Although matrices, dyadics, Laplace transformations, and
the calculus of variations are occasionally encountered, it is my belief
that they are introduced in a manner which is understandable to the
beginner and will serve as an introduction to the use of these
mathematical techniques.

Finally I wish to acknowledge my indebtedness to many persons with whom
I have enjoyed working and learning—students, colleagues, and associates
at Space Technology Laboratories.

  
  

<span class="i">September, 1961</span>

WILLIAM T. THOMSON

</div>

<span id="e9780486140520_toc01.html"></span>

<div class="toc">

<span id="e9780486140520_toc01.html_title149"></span>

# Table of Contents

<div class="toc_entry">

  
<a href="#e9780486140520_fm01.html" class="toc_entry_frontMatter"><span
class="b">DOVER BOOKS ON ENGINEERING</span></a>  
<a href="#e9780486140520_tp01.html" class="toc_entry_titlePage">Title
Page</a>  
<a href="#e9780486140520_cop01.html" class="toc_entry_pubInfo">Copyright
Page</a>  
<a href="#e9780486140520_ded01.html"
class="toc_entry_dedicationPage">Dedication</a>  
<a href="#e9780486140520_fm02.html" class="toc_entry_frontMatter"><span
class="b">Preface to the Dover Edition</span></a>  
<a href="#e9780486140520_fm03.html" class="toc_entry_frontMatter"><span
class="b">Preface to the First Edition</span></a>  
<a href="#e9780486140520_c01.html" class="toc_entry_chapter"><span
class="b">CHAPTER 1</span> - <span class="b">Introduction</span></a>  
<a href="#e9780486140520_c02.html" class="toc_entry_chapter"><span
class="b">CHAPTER 2</span> - <span class="b">Kinematics</span></a>  
<a href="#e9780486140520_c03.html" class="toc_entry_chapter"><span
class="b">CHAPTER 3</span> - <span class="b">Transformation of
Coordinates</span></a>  
<a href="#e9780486140520_c04.html" class="toc_entry_chapter"><span
class="b">CHAPTER 4</span> - <span class="b">Particle Dynamics
(Satellite Orbits)</span></a>  
<a href="#e9780486140520_c05.html" class="toc_entry_chapter"><span
class="b">CHAPTER 5</span> - <span class="b">Gyrodynamics</span></a>  
<a href="#e9780486140520_c06.html" class="toc_entry_chapter"><span
class="b">CHAPTER 6</span> - <span class="b">Dynamics of Gyroscopic
Instruments</span></a>  
<a href="#e9780486140520_c07.html" class="toc_entry_chapter"><span
class="b">CHAPTER 7</span> - <span class="b">Space Vehicle
Motion</span></a>  
<a href="#e9780486140520_c08.html" class="toc_entry_chapter"><span
class="b">CHAPTER 8</span> - <span class="b">Performance and
Optimization</span></a>  
<a href="#e9780486140520_c09.html" class="toc_entry_chapter"><span
class="b">CHAPTER 9</span> - <span class="b">Generalized Theories of
Mechanics</span></a>  
<a href="#e9780486140520_bm01.html" class="toc_entry_backMatter"><span
class="b">General References</span></a>  
<a href="#e9780486140520_app01.html" class="toc_entry_appendix"><span
class="b">APPENDIX A</span> - <span class="b">Matrices</span></a>  
<a href="#e9780486140520_app02.html" class="toc_entry_appendix"><span
class="b">APPENDIX B</span> - <span class="b">Dyadics</span></a>  
<a href="#e9780486140520_app03.html" class="toc_entry_appendix"><span
class="b">APPENDIX C</span> - <span class="b">The Variational
Calculus</span></a>  
<a href="#e9780486140520_ind01.html" class="toc_entry_index"><span
class="b">Index</span></a>  
<a href="#e9780486140520_bm02.html" class="toc_entry_backMatter"><span
class="b">A CATALOG OF SELECTED DOVER BOOKS IN SCIENCE AND
MATHEMATICS</span></a>  
<a href="#e9780486140520_bm03.html" class="toc_entry_backMatter"><span
class="b">DOVER BOOKS ON ASTRONOMY</span></a>  
  

</div>

</div>

<span id="e9780486140520_c01.html"></span>

<div class="chapter">

<span id="e9780486140520_c01.html_title4"></span>

# <span class="b">CHAPTER 1</span>

# <span class="b">Introduction</span>

<div class="section1">

<span id="e9780486140520_c01.html_title5"></span>

# <span class="b">I.I Basic Concepts</span>

The basic concepts of mechanics are space, time, and mass or force,
which are more or less understood intuitively by most beginning
students. To be useful for quantitative analysis, however, these notions
must be viewed as mathematical concepts related to each other by
fundamental laws. Such a formulation was introduced by Sir Isaac Newton
(1642-1727) in his three laws of motion which have become the foundation
for the classical or Newtonian mechanics.

Newton’s laws were formulated for a single particle. Our notion of a
particle is that of a material body of infinitely small dimensions. In
mechanics we can expand this notion to include any material body whose
dimensions are small in comparison with distances or lengths involved in
defining its position or motion. Thus planets can be considered to be
particles when their position in the solar system is under
consideration.

In defining the position of a particle in space, a frame of reference is
necessary. For this purpose, three mutually perpendicular lines
intersecting at a common point called the origin are adequate. The
position of the particle can then be defined in terms of distances along
these lines.

To describe the motion of a particle, the concept of time is required.
By noting the position of the particle as a function of time, its
motion—described by its displacement, velocity, and acceleration—is
completely defined.

Force is known to us intuitively as a push or pull. It represents the
action of one body on another, exerted by contact or through a distance
as in the case of gravitational or magnetic force. To describe a force,
it is necessary to know its magnitude, its direction, and its point of
application.

Mass is a property possessed by all material bodies. It is a property
which describes the effort necessary in giving the body a change in
motion. Its precise definition is embodied in Newton’s second law, which
may be stated as follows. “A particle acted upon by a force
<span class="b">F</span> will move with an acceleration
<span class="b">a</span> proportional to and in the direction of the
force; the ratio <span class="b">F/a</span> being constant for any
particle.” Thus for a given particle we can write,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0002.jpg](images/e9780486140520_i0002.jpg)

</div>

</div>

where <span class="b">F</span> and <span class="b">a</span> are in
consistent set of units. The ratio <span class="b">F/a</span> which is
found to be a constant for any given particle, is a property of the
particle, which is designated as mass. We can therefore write Newton’s
second law as,

<div class="blocktext">

<span class="b">F = <span class="i">m</span>a</span>

</div>

Newton’s first law is a special case of the second law when
<span class="b">F</span> = 0. It states that if no force acts on the
particle, it will remain at rest or continue to move in a straight line
with constant velocity. The equilibrium concept in statics is based on
the first law, and the converse of the above statement requires that the
resultant of all the forces acting on a particle in equilibrium must be
zero.

The extension of Newton’s laws to a group of particles necessarily
involves the action between particles. Actual bodies can be viewed as a
group of particles, and to deduce the behavior of such bodies, Newton
introduced his third law which states that, “For every action, there is
an equal and opposite reaction.” Thus if particle 1 exerts a force
f<sub>12</sub> on particle 2, particle 2 must exert a force
f<sub>21</sub> on particle 1, where f<sub>21</sub> = −f<sub>12</sub>.

From his interest in astronomy, Newton formulated the law of gravitation
between two particles. The law states that any two particles attract one
another with a force of magnitude,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0003.jpg](images/e9780486140520_i0003.jpg)

</div>

</div>

where <span class="i">m</span><sub>1</sub> and
<span class="i">m</span><sub>2</sub> are the masses of the particles,
<span class="i">r</span> is the distance between them, and
<span class="i">G</span> is the universal constant of gravitation.
Application of this law to a particle on the earth’s surface gives us an
understanding of the relationship existing between mass and weight.
Letting <span class="i">M</span> and <span class="i">m</span> be the
mass of the earth and that of another body at the earth’s surface, a
distance equal to the radius <span class="i">r</span> =
<span class="i">R</span> from the center, the attraction of the earth on
the body, which is called weight, is given by the above equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0004.jpg](images/e9780486140520_i0004.jpg)

</div>

</div>

If this force is not opposed by a support of some kind, the body will
fall toward the center of the earth with an acceleration
<span class="i">g</span>. Thus from Newton’s second law, we can write,

<div class="blocktext">

<span class="i">W = mg</span>

</div>

and by comparison with the previous equation, we arrive at the result,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0005.jpg](images/e9780486140520_i0005.jpg)

</div>

</div>

We find then that the acceleration of gravity <span class="i">g</span>
will vary inversely with <span class="i">R</span><sup>2</sup>. Since
<span class="i">m</span> is a property of the body which is fixed, its
weight will then vary with <span class="i">g</span> or
<span class="i">R</span>, and so we find a given body weighing somewhat
different amounts at different places on the earth’s surface. At the
earth’s surface, <span class="i">g</span> is very nearly 32.2
ft/sec<sup>2</sup>.

So far we have avoided one very important question regarding the frame
of reference used in the measurement of the motion. Newton assumed that
there was a frame of reference whose absolute motion was zero. He
considered such an <span class="i">inertial frame</span> fixed relative
to the stars to be one of absolute zero motion, and his laws of motion
to be valid when referred to such a reference. Controversies regarding
the existence of such a reference frame of absolute zero motion led to
the formulation of the theories of relativity for which Newtonian
mechanics is a special case.

In arriving at the concept of weight, it was necessary to measure g
relative to the surface of the earth which is not at rest. Thus the
acceleration of the earth’s surface due to its rotation must be
accounted for in a more exact analysis. For many problems this error is
insignificant, in which case the earth’s surface will be found to be an
adequate reference. There are other problems, however, such as
navigation for space flight, where the earth’s surface cannot be
considered stationary. In general, problems in space dynamics are
involved with rotating and accelerating coordinates, and the subject of
relative motion and transformation of coordinates plays an important
role.

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title6"></span>

# <span class="b">1.2 Scalar and Vector Quantities</span>

In our discussion so far we have encountered two types of physical
quantities. The first type can be adequately expressed by a single
number denoting so many units; i.e., temperature, density, mass, time,
and energy. Such quantities are known as <span class="i">scalar</span>
quantities.

The second type cannot be fully represented by a number only, and
further information is required. For instance, a displacement in space
requires in addition to its numerical value a statement as to its
starting point and its direction. Such additional information is
necessary to describe completely many physical quantities such as force,
velocity, and acceleration. Physical quantities possessing magnitude and
direction and satisfying certain necessary requirements are called
<span class="i">vector</span> quantities.

Vectors are further subdivided into <span class="i">free</span> and
<span class="i">bound</span> vectors. Free vectors are those which can
be shifted about as long as their magnitude and direction are not
altered. Vectors in rigid body mechanics are in general free vectors.
Bound vectors are those which cannot be moved without altering the
results sought. For instance, in determining the stress distribution in
a deformable solid, the applied force cannot be moved without altering
the results.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0006.jpg](images/e9780486140520_i0006.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_1"
id="e9780486140520_c01.html_int_1" class="label_int"><span
class="b">Fig. 1.2-1</span></a><span class="b">.</span> Right-handed
coordinate system.

</div>

</div>

Vector quantity will be denoted by a bold face roman letter, whereas a
scalar quantity will be indicated by a light-face italic letter.
Frequently we are not concerned with the direction of the vector
quantity, in which case the italic letter will be used to indicate its
magnitude. This situation may occur when all the vectors are collinear
or when we are concerned with components of a vector along specified
directions. To distinguish vector quantities at the blackboard or in
hand-written material, an overhead bar or arrow can be used.

Graphically, a vector is represented by a straight line with an arrow
referenced to some coordinate system. When rectangular axes
<span class="i">x, y, z</span> are used, the right-handed coordinate
system of <a href="#e9780486140520_c01.html#int_1"
id="e9780486140520_c01.html_ref_int_1" class="ref_int">Fig. 1.2-1</a>
will be adopted. A left-handed coordinate system would have the
<span class="i">Oz</span> axis in the opposite sense, or the
<span class="i">x</span> and <span class="i">y</span> axes interchanged.

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title7"></span>

# <span class="b">1.3 Properties of a Vector</span>

<div class="section2">

<span id="e9780486140520_c01.html_title8"></span>

# <span class="i">Addition</span>

Not every quantity possessing magnitude and direction can be treated as
a vector. To qualify as a vector, such quantities must obey the law of
composition which states that the sum of two vectors is represented by
the diagonal of a parallelogram formed by the two vectors as sides.
Subtraction can be viewed as an addition of the vector directed in the
opposite sense. Moreover, vector addition must be commutative
(independent of the order of summation).

As an example of a directed quantity that will not obey the law of
composition, we can mention the finite angular rotation of a rigid body.
It has magnitude equal to the angle of rotation, which can be directed
along the axis of rotation. However, two such rotations along different
axes are not commutative and will not add up to the diagonal of a
parallelogram, as we can readily demonstrate by rotating a book 90°
about the x and y axes and repeating the procedure in the reverse order
about <span class="i">y</span> and x.

Aside from being commutative, vector addition is associative (may be
grouped in any order), and these two properties enable the parallelogram
law to be successively applied to any pair of vectors for the addition
of several vectors.

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title9"></span>

# <span class="i">Resolution</span>

Resolution of a vector is the reverse of composition. Since different
components could have the same resultant, a vector can be resolved in an
infinite number of different ways. Resolution of a vector into
rectangular components often leads to a simpler formulation.

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title10"></span>

# <span class="i">Unit vector</span>

A vector <span class="b">r</span> multiplied by a scalar
<span class="i">n</span> is equal to nr. Its direction is unchanged and
its magnitude is <span class="i">n</span> times the original magnitude.
The unit vector <span class="b">1,</span> or <span class="b">i, j,
k,</span> is constantly used to define the orientation of a vector
quantity. A vector r, expressed in terms of its rectangular components,
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0007.jpg](images/e9780486140520_i0007.jpg)

</div>

</div>

The unit vector in the direction <span class="b">r</span> is thus
identified as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0008.jpg](images/e9780486140520_i0008.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0009.jpg](images/e9780486140520_i0009.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_2"
id="e9780486140520_c01.html_int_2" class="label_int"><span
class="b">Fig. 1.3-1</span></a><span class="b">.</span> Component of
<span class="b">r</span> along <span class="b">1</span> by dot product.

</div>

</div>

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title11"></span>

# <span class="i">Scalar “dot” product</span>

The <span class="i">dot</span> product of two vectors
<span class="b">a</span> and <span class="b">b</span> with angle
<span class="i">φ</span> between them is a scalar quantity defined by
the equation,

<div class="blocktext">

<span class="b">a • b</span> = <span class="i">ab</span> cos
<span class="i">φ</span>

</div>

The result is not dependent on the order of multiplication and, hence,
the dot product is commutative.

<div class="blocktext">

<span class="b">a • b = b • a</span>

</div>

The equation suggests a convenient procedure for determining the
component of a vector <span class="b">r</span> along any chosen
direction <span class="b">1,</span> the result being,

<div class="blocktext">

<span class="b">r • 1</span> = <span class="i">r</span> cos
<span class="i">φ</span>

</div>

as shown in <a href="#e9780486140520_c01.html#int_2"
id="e9780486140520_c01.html_ref_int_2" class="ref_int">Fig. 1.3-1</a>.

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title12"></span>

# <span class="i">Vector “cross” product</span>

The <span class="i">cross product</span> of two vectors
<span class="b">a</span> and <span class="b">b</span> is a vector
defined by the equation,

<div class="blocktext">

<span class="b">a × b</span> = (<span class="i">ab</span> sin
<span class="i">φ</span>)<span class="b">1</span>

</div>

where <span class="b">1</span> is a unit vector in a direction
perpendicular to both <span class="b">a</span> and
<span class="b">b</span>. From <a href="#e9780486140520_c01.html#int_3"
id="e9780486140520_c01.html_ref_int_3" class="ref_int">Fig. 1.3-2</a> it
is seen that the magnitude is equal to the product of the length of one
of the two vectors and the projection of the other on a line
perpendicular to the first vector, which is equal to the area of the
parallelogram formed with <span class="b">a</span> and
<span class="b">b</span> as sides.

To establish the direction of the cross-product vector, the three-finger
rule of the right hand, as illustrated in
<a href="#e9780486140520_c01.html#int_3" class="ref_int">Fig. 1.3-2</a>,
is helpful. The first vector <span class="b">a</span> is represented by
the thumb; the second vector <span class="b">b</span> (or its component
<span class="i">b</span> sin <span class="i">φ</span> perpendicular to
<span class="b">a</span>) by the index finger; and the product vector
perpendicular to the previous two by the third finger. We note here that
the cross product is noncommutative, and the following rule holds:

<div class="blocktext">

<span class="b">a ×</span> <span class="b">b = −b × a</span>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0010.jpg](images/e9780486140520_i0010.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_3"
id="e9780486140520_c01.html_int_3" class="label_int"><span
class="b">Fig. 1.3-2.</span></a> Cross product of two vectors is normal
to the plane of the two vectors.

</div>

</div>

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title13"></span>

# <span class="i">Products in rectangular components</span>

When resolved into rectangular components, the dot and cross products
become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0011.jpg](images/e9780486140520_i0011.jpg)

</div>

</div>

The result of the cross product can be conveniently expressed by the
following determinant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0012.jpg](images/e9780486140520_i0012.jpg)

</div>

</div>

</div>

<div class="section2">

<span id="e9780486140520_c01.html_title14"></span>

# <span class="i">Multiple products</span>

Certain multiple products of vectors are occasionally encountered and we
list two of the most common ones in the following:

<div class="blocktext">

<span class="b">a •</span> (<span class="b">b × c</span>) =
<span class="b">b</span> • (<span class="b">c × a</span>)
<span class="b">= c •</span> (<span class="b">a × b</span>)

</div>

This product can be interpreted geometrically as being equal to the
volume of a parallelopiped of sides <span class="i">a, b,</span> and
<span class="i">c</span>.

The second multiple product is,

<div class="blocktext">

<span class="b">a ×</span> (<span class="b">b × c</span>) = (a • c)b −
(a • b)c

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title15"></span>

# <span class="b">1.4 Moment of a Vector</span>

Consider a vector <span class="b">F</span> and any point
<span class="i">O</span> in space. If we draw a vector
<span class="b">r</span> from <span class="i">O</span> to any point on
<span class="b">F</span> or on the line of action of
<span class="b">F,</span> as shown in
<a href="#e9780486140520_c01.html#int_4"
id="e9780486140520_c01.html_ref_int_4" class="ref_int">Fig. 1.4-1</a>,
and form the cross product with r as the first vector, then the result
will be a moment <span class="b">M</span> about an axis through
<span class="b"><span class="i">O</span></span> in a direction
perpendicular to the plane containing <span class="b">r</span> and
<span class="b">F</span>, the direction of which is indicated by the
unit vector <span class="b">1.</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0013.jpg](images/e9780486140520_i0013.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_4"
id="e9780486140520_c01.html_int_4" class="label_int"><span
class="b">Fig. 1.4-1</span></a>. Moment vector <span class="b">M</span>
normal to plane of <span class="b">r</span> and <span class="b">F</span>
is <span class="b">r × F.</span>

</div>

</div>

<div class="blocktext">

<span class="b">M = r × F</span>=(<span class="i">Fr</span> sin
<span class="i">φ</span>)<span class="b">1</span>

</div>

The moment <span class="b">M</span> will be independent of where
<span class="b">r</span> terminates on <span class="b">F</span> or on
its line of action, as can easily be shown.

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title16"></span>

# <span class="b">1.5 Angular Velocity Vectors</span>

It was pointed out previously that finite angles of rotation, although
representable by a vector, are not commutative and, hence, will not obey
the rules of vector addition. Infinitesimal rotations however can be
shown to be commutative and to possess all the properties of a vector.
To show this, consider the displacement of a point
<span class="i">p</span> due to two infinitesimal rotations
<span class="i">ω</span><sub>1</sub> <span class="i">dt</span> and
<span class="i">ω</span><sub>2</sub> <span class="i">dt</span> about any
two axes, where <span class="i">ω</span><sub>1</sub> and
<span class="i">ω</span><sub>2</sub> are their respective rotational
speeds. Let the direction of each of the axes of rotation be indicated
by unit vectors
<span class="b">1</span><sub><span class="b">1</span></sub> and
<span class="b">1</span><sub><span class="b">2</span></sub><span class="b">,</span>
as shown in <a href="#e9780486140520_c01.html#int_5"
id="e9780486140520_c01.html_ref_int_5" class="ref_int">Fig. 1.5-1</a>,
and we will perform the rotations in the order 1 and 2 then repeat in
the reverse order to examine the final result.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0014.jpg](images/e9780486140520_i0014.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_5"
id="e9780486140520_c01.html_int_5" class="label_int"><span
class="b">Fig. 1.5-1</span></a><span class="b">.</span> Angular velocity
represented by vector.

</div>

</div>

Because of the infinitesimal rotation
(<span class="i">ω</span><sub>1</sub>
<span class="i">dt</span>)<span class="b">1</span><sub>1</sub><span class="i">,</span>
the end of the displacement vector <span class="b">r</span> defining the
position <span class="i">p</span> will be displaced by an amount,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0015.jpg](images/e9780486140520_i0015.jpg)

</div>

<div class="caption">

(1.5-1)

</div>

</div>

and the new position is defined by the vector,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0016.jpg](images/e9780486140520_i0016.jpg)

</div>

<div class="caption">

(1.5-2)

</div>

</div>

Next allow the second infinitesimal rotation
(<span class="i">ω</span><sub>2</sub>
<span class="i">dt</span>)<span class="b">1</span><sub>2</sub><span class="i">,</span>
in which case the final position of <span class="i">p</span> is defined
by the vector
<span class="b">r</span><sub><span class="b">2</span></sub>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0017.jpg](images/e9780486140520_i0017.jpg)

</div>

<div class="caption">

(1.5-3)

</div>

</div>

Neglecting the second-order term
(<span class="i">ω</span><sub>2</sub><span class="i">ω</span><sub>1</sub>
<span class="i">dt dt</span>)<span class="i">,</span> we arrive at the
result,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0018.jpg](images/e9780486140520_i0018.jpg)

</div>

<div class="caption">

(1.5-4)

</div>

</div>

If we repeat the operation in the reverse order, we will find the
equation for <span class="b">r</span><sub>2</sub> to be identical to the
previous case, indicating that infinitesimal rotations are commutative.
In effect, we have represented an angular velocity by a vector
<span class="b">ω</span> =
<span class="i">ω</span><span class="b">1</span> according to the
right-hand screw convention, as shown in
<a href="#e9780486140520_c01.html#int_6"
id="e9780486140520_c01.html_ref_int_6" class="ref_int">Fig. 1.5-2</a>.
The fingers in this case indicate the rotation sense, and the positive
direction of the vector <span class="b">ω</span> is represented by the
thumb.

Since angular velocities obey all the rules of vectors, they can be
compounded by the parallelogram rule to a single resultant vector. Thus
the two infinitesimal rotations of
<a href="#e9780486140520_c01.html#int_5" class="ref_int">Fig. 1.5-1</a>
can also be reduced to a single rotation which is evident by rewriting
the equation for
<span class="b">r</span><sub><span class="b">2</span></sub> as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0019.jpg](images/e9780486140520_i0019.jpg)

</div>

<div class="caption">

(1.5–5)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0020.jpg](images/e9780486140520_i0020.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_6"
id="e9780486140520_c01.html_int_6" class="label_int"><span
class="b">Fig. 1.5-2</span></a>. Right-hand rule for angular velocity.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title17"></span>

# <span class="b">1.6 Derivative of a Vector</span>

In differentiating a vector, the usual rules of the limiting process
apply.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0021.jpg](images/e9780486140520_i0021.jpg)

</div>

<div class="caption">

(1.6–1)

</div>

</div>

If the vector <span class="b">r</span> is referenced to a fixed
coordinate system, the <span class="b">Δr</span> is the vector change
relative to the coordinates which is also the total change, and Eq.
1.6–1 is the total derivative of <span class="b">r.</span>

If the vector <span class="b">r</span> is referenced to a rotating
coordinate system such as the one shown in
<a href="#e9780486140520_c01.html#int_7"
id="e9780486140520_c01.html_ref_int_7" class="ref_int">Fig. 1.6-1</a>,
the vector <span class="b">r</span> remaining stationary relative to the
rotating axes will undergo a change

<div class="blocktext">

Δ<span class="i">θr</span> sin <span class="i">φ</span>

</div>

along the tangent to the dotted circle, and its rate of change is
established by the limit,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0022.jpg](images/e9780486140520_i0022.jpg)

</div>

</div>

where <span class="b">1</span> is a unit vector along the tangent.

Since this expression is equal to the cross product of
<span class="b">ω</span> and <span class="b">r,</span> we conclude that
due to rotation <span class="b">ω</span> of the coordinate system the
vector <span class="b">r</span> undergoes a rate of change of

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0023.jpg](images/e9780486140520_i0023.jpg)

</div>

<div class="caption">

(1.6-2)

</div>

</div>

This term occurs in addition to the vector change relative to the
coordinate system, so that the total derivative relative to inertial
axes is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0024.jpg](images/e9780486140520_i0024.jpg)

</div>

<div class="caption">

(1.6-3)<sup><a href="#e9780486140520_ftn01.html#ftn_fn1"
id="e9780486140520_c01.html_ref_ftn_fn1">a</a></sup>

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0025.jpg](images/e9780486140520_i0025.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c01.html#ref_int_7"
id="e9780486140520_c01.html_int_7" class="label_int"><span
class="b">Fig. 1.6-1</span></a> Differentiation of a vector
<span class="b">r</span> referenced to rotating coordinates.

</div>

</div>

Equation 1.6-3 applies to any vector quantity and is of fundamental
importance to dynamics where body-fixed axes are often used.

We mention finally that the derivatives of the dot and cross products
are treated as in products of scalar quantities, except that the order
of the cross product must be maintained. These rules are illustrated by
the following equations.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0026.jpg](images/e9780486140520_i0026.jpg)

</div>

<div class="caption">

(1.6–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0027.jpg](images/e9780486140520_i0027.jpg)

</div>

<div class="caption">

(1.6–5)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c01.html_title18"></span>

# <span class="b">PROBLEMS</span>

1.  . Determine the unit vector along <span class="b">r</span> =
    3<span class="b">i</span> − 2<span class="b">j</span> +
    2<span class="b">k</span>.
2.  Determine the angles <span class="i">α, β,</span> and
    <span class="i">y</span> between <span class="b">r</span> of Prob. 1
    and the <span class="i">x, y,</span> and <span class="i">z</span>
    axes.
3.  Determine the dot product of the vectors
    <span class="b">r</span><sub><span class="b">1</span></sub>
    <span class="b">= 4i − 3j + k;
    r</span><sub><span class="b">2</span></sub> <span class="b">= − 2i +
    2j + 3k.</span>
4.  . Determine the angle between <span class="b">r</span><sub>1</sub>
    and <span class="b">r</span><sub>2</sub> of Prob. 3.
5.  . Determine the cross product
    <span class="b">r</span><sub><span class="b">1</span></sub>
    <span class="b">x r</span><sub><span class="b">2</span></sub> of
    Prob. 3. Show by means of dot products between the cross product
    vector and <span class="b">r</span><sub>1</sub> and
    <span class="b">r</span><sub>2</sub> that the cross product is
    perpendicular to each of vectors
    <span class="b">r</span><sub>1</sub> and
    <span class="b">r</span><sub>2</sub>.
6.  Show by vector means that any inscribed angle in a semicircle is a
    right angle.
7.  . What is the geometric interpretation of <span class="b">(a +
    b)</span><sup><span class="b">2</span></sup><span class="b">.</span>
8.  If <span class="i">a</span> and <span class="i">b</span> are
    absolute values of vectors <span class="b">a</span> and
    <span class="b">b</span>, express the scalar quantity
    <span class="i">a</span><sup>2</sup><span class="i">b</span><sup>2</sup>
    by using only the dot and cross products of <span class="b">a</span>
    and <span class="b">b.</span>
9.  Write the equation of a plane, a distance <span class="b">c</span>
    from a given point <span class="i">O,</span> in terms of the radius
    vector <span class="b">r</span> from <span class="i">O</span> to any
    point in the plane, and the unit vector <span class="b">1</span>
    normal to the plane.
10. Determine the various angles between the spatial diagonals of a unit
    cube of sides <span class="b">i, j</span>, and
    <span class="b">k.</span>
11. Find the area of a triangle specified by the two vectors
    <span class="b">r</span><sub>1</sub> = <span class="b">3i</span> +
    4<span class="b">j</span>; <span class="b">r</span><sub>2</sub> =
    −<span class="b">5</span>i + 7<span class="b">j</span> +
    2<span class="b">k.</span>
12. Show that the moment <span class="b">r x F</span> about
    <span class="i">O</span> is independent of how r is drawn from
    <span class="i">O</span> as long as it terminates along the line of
    action of <span class="b">F.</span> (<span class="i">Hint:</span>
    Consider two vectors <span class="b">r</span><sub>1</sub> and
    <span class="b">r</span><sub>2</sub> =
    <span class="b">r</span><sub>1</sub> +
    <span class="b">r</span><sub>3</sub> both terminating along
    <span class="b">F.</span>)
13. Determine the derivative of the dot product of the vectors
    r<sub>1</sub> = 2<span class="i">t</span>i −
    3<span class="i">t</span><sup>2</sup>j;
    <span class="b">r</span><sub>2</sub> = −4<span class="b">i</span> +
    2<span class="i">t</span><span class="b">j</span>, and compare with
    the derivative determined from Eq. 1.6-4.
14. Repeat Prob. 13 for the cross product, using Eq. 1.6-5.
15. A vector r = 3<span class="i">t</span><span class="b">i</span> -
    4<span class="b">j</span> + <span class="b">k</span> is referenced
    to a coordinate system which is rotating at a speed ω =
    2<span class="i">t</span><span class="b">k</span>. Determine its
    derivative.
16. Prove the equations given on p. 8 for the multiple products.
17. Complete the derivation for Eq. 1.5–3 when the order of rotation is
    2 and 1. Under what conditions are the two equations equal?
18. Determine the relative magnitudes of the terms of Eq. 1.5-3 when
    <span class="b">r</span> = 4i + 3<span class="b">j</span>;
    <span class="i">ω</span><sub>1</sub> = 2;
    <span class="i">ω</span><sub>2</sub> = −<span class="b">1</span>;
    <span class="b">1<sub>1</sub></span> = <span class="b">i</span> and
    <span class="b">1<sub>2</sub></span> = <span class="b">j.</span>
19. In Prob. 18, determine the value of <span class="i">dt</span>
    necessary to reduce the term
    (<span class="i">ω</span><sub><span class="i">2</span></sub>
    <span class="i">dt</span>)1<sub>2</sub> x
    (<span class="i">ω</span><sub>1</sub>
    <span class="i">dt</span>)1<sub>1</sub> × r to 1% of the magnitude
    of the smallest vector component.

</div>

</div>

<span id="e9780486140520_c02.html"></span>

<div class="chapter">

<span id="e9780486140520_c02.html_title19"></span>

# <span class="b">CHAPTER 2</span>

# <span class="b">Kinematics</span>

<div class="section1">

<span id="e9780486140520_c02.html_title20"></span>

# <span class="b">2.1 Velocity and Acceleration</span>

The subject of kinematics is the study of motion. It is concerned with
space and time, and with the time rate of change of vector quantities
relating to the geometry of motion.

We consider first the motion of a point in a fixed coordinate system
<span class="i">xyz.</span> The position of a point
<span class="i">p</span> which is in continuous motion along a curve
such as <span class="i">s</span> in
<a href="#e9780486140520_c02.html#int_8"
id="e9780486140520_c02.html_ref_int_8" class="ref_int">Fig. 2.1-1</a> is
specified by its position vector r, the magnitude and direction of which
are functions of time. In time Δ<span class="i">t</span>,
<span class="b">r</span> changes to <span class="b">r</span> +
Δ<span class="b">r</span>, and its velocity v is given by the time
derivative,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0029.jpg](images/e9780486140520_i0029.jpg)

</div>

<div class="caption">

(2.1-1)

</div>

</div>

The direction of v can be shown to coincide with the limiting direction
of Δ<span class="b">r</span> as it approaches zero, or the tangent to
the curve <span class="i">s at p.</span> By rewriting
<span class="b">v</span> in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0030.jpg](images/e9780486140520_i0030.jpg)

</div>

</div>

the limiting value of
Δ<span class="b">r</span>/Δ<span class="i">s</span> is a unit vector
along the tangent to the curve, so that the velocity can also be written
as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0031.jpg](images/e9780486140520_i0031.jpg)

</div>

<div class="caption">

(2.1-2)

</div>

</div>

If r is represented in terms of its rectangular components, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0032.jpg](images/e9780486140520_i0032.jpg)

</div>

<div class="caption">

(2.1-3)

</div>

</div>

where
<span class="i">r</span><sub><span class="i">x</span></sub><span class="i">,
r</span><sub><span class="i">y</span></sub><span class="i">,</span> and
<span class="i">r</span><sub><span class="i">z</span></sub> are
components of r along the fixed <span class="i">xyz</span> coordinates,
and <span class="b">i, j,</span> and <span class="b">k</span> are their
corresponding unit vectors. Differentiating, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0033.jpg](images/e9780486140520_i0033.jpg)

</div>

<div class="caption">

(2.1-4)

</div>

</div>

where <span class="b">i, j,</span> and <span class="b">k</span>, are
treated as constants.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0034.jpg](images/e9780486140520_i0034.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_8"
id="e9780486140520_c02.html_int_8" class="label_int"><span
class="b">Fig. 2.1-1</span></a>. Time rate of change of a vector
<span class="b">r</span>.

</div>

</div>

Acceleration is the time rate of change of velocity
<span class="b">v</span>, and by observing the vector change from
<span class="b">v</span> to <span class="b">v</span> +
<span class="b">Δv</span> in time Δ<span class="b">t</span>, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0035.jpg](images/e9780486140520_i0035.jpg)

</div>

<div class="caption">

(2.1-5)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c02.html_title21"></span>

# <span class="b">2.2 Plane Motion (Radial and Transverse Components)</span>

Consider a particle <span class="i">p</span> moving along a curve
<span class="i">s</span> fixed in a stationary
<span class="i">Oxy</span> plane, as shown in
<a href="#e9780486140520_c02.html#int_9"
id="e9780486140520_c02.html_ref_int_9" class="ref_int">Fig. 2.2-1</a>.
The position of <span class="i">p</span> is established by the position
vector

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0036.jpg](images/e9780486140520_i0036.jpg)

</div>

<div class="caption">

(2.2-1)

</div>

</div>

where <span class="b">1,.</span> is a unit vector which is always
oriented along <span class="b">r.</span>

To determine the velocity of <span class="i">p,</span> we differentiate
<span class="b">r,</span> recognizing that
<span class="b">1</span><sub><span class="b">r</span></sub> chanees in
direction.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0037.jpg](images/e9780486140520_i0037.jpg)

</div>

<div class="caption">

(2.2-2)

</div>

</div>

The unit vector
<span class="b">1</span><sub><span class="b">r</span></sub> is one of
fixed magnitude which is rotating with angular velocity
<span class="b">θ</span> about an axis through the origin perpendicular
to the xy plane. Its derivative or its velocity is the cross product of
the vectors <span class="b">θ</span> and
<span class="b">1</span><sub><span class="b">r</span></sub>, which is a
vector perpendicular to <span class="b">r</span>, or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0038.jpg](images/e9780486140520_i0038.jpg)

</div>

<div class="caption">

(2.2-3)

</div>

</div>

where <span class="b">1</span><sub><span class="i">θ</span></sub> is a
unit vector in the direction perpendicular to <span class="b">r.</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0039.jpg](images/e9780486140520_i0039.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_9"
id="e9780486140520_c02.html_int_9" class="label_int"><span
class="b">Fig. 2.2-1</span></a><span class="b">.</span> Unit vectors
<span class="b">1</span><sub><span class="b">r</span></sub> and
<span class="b">1</span><sub><span class="i">θ</span></sub> moving with
r in the <span class="i">x, y</span> plane.

</div>

</div>

Equation 2.2-2 may then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0040.jpg](images/e9780486140520_i0040.jpg)

</div>

<div class="caption">

(2.2-4)

</div>

</div>

which expresses the velocity in terms of the radial and transverse
components.

We can view this problem as that of a point <span class="i">p</span>
moving along a set of rotating axes with direction
<span class="b">1</span><sub><span class="i"><span class="b">r</span></span></sub>
and
<span class="b">1</span><sub><span class="i">θ</span></sub><span class="b">.</span>
The point <span class="i">p</span> always moves along the
<span class="b">1,</span> axis, and its relative velocity along it is r
which corresponds to the first term of Eq. 2.2-4. The second term
<span class="imageinline">![e9780486140520_i0041.jpg](images/e9780486140520_i0041.jpg)</span>
is the velocity of the coincident point <span class="i">p</span> due to
rotation
<span class="imageinline">![e9780486140520_i0042.jpg](images/e9780486140520_i0042.jpg)</span><span class="b">.</span>

The acceleration of <span class="i">p</span> can be determined by
differentiating Eq. 2.2–4.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0043.jpg](images/e9780486140520_i0043.jpg)

</div>

<div class="caption">

(2.2-5)

</div>

</div>

As before, the derivative of a unit vector rotates it 90° and multiplies
it with its angular rate
<span class="imageinline">![e9780486140520_i0044.jpg](images/e9780486140520_i0044.jpg)</span><span class="b">,</span>
so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0045.jpg](images/e9780486140520_i0045.jpg)

</div>

<div class="caption">

(2.2-6)

</div>

</div>

Thus Eq. 2.2–5 reduces to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0046.jpg](images/e9780486140520_i0046.jpg)

</div>

<div class="caption">

(2.2-7)

</div>

</div>

which expresses the acceleration in terms of the radial and transverse
components. We note here the term
<span class="imageinline">![e9780486140520_i0047.jpg](images/e9780486140520_i0047.jpg)</span><span class="i">,</span>
which is known as the Coriolis acceleration, and which will be referred
to again in the more general case.

</div>

<div class="section1">

<span id="e9780486140520_c02.html_title22"></span>

# <span class="b">2.3 Tangential and Normal Components</span>

To resolve the acceleration into tangential and normal components, we
start with Eq. 2.1—2.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0048.jpg](images/e9780486140520_i0048.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_10"
id="e9780486140520_c02.html_int_10" class="label_int">Fig. <span
class="b">2.3-1</span></a><span class="b">.</span> Unit vectors
1<sub>n</sub>. and 1<sub><span class="i">t</span></sub> moving along
curve s, in x, <span class="i">y</span> plane.

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0049.jpg](images/e9780486140520_i0049.jpg)

</div>

<div class="caption">

(2.3-1)

</div>

</div>

Differentiating and noting that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0050.jpg](images/e9780486140520_i0050.jpg)

</div>

<div class="caption">

(2.3-2)

</div>

</div>

where <span class="b">1</span><sub><span class="i">n</span></sub> is a
unit vector along the radius of curvature which is normal to the tangent
to the curve <span class="i">s</span> at <span class="i">p</span>, and φ
is the angular rate of the radius of curvature as shown in
<a href="#e9780486140520_c02.html#int_10"
id="e9780486140520_c02.html_ref_int_10" class="ref_int">Fig. 2.3-1</a>,
we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0051.jpg](images/e9780486140520_i0051.jpg)

</div>

<div class="caption">

(2.3-3)

</div>

</div>

Since the length Δ<span class="i">s</span> is related to the radius of
curvature <span class="i">p</span> and to the angle
<span class="b">Δ</span><span class="i">φ</span> swept out by
<span class="i">p,</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0052.jpg](images/e9780486140520_i0052.jpg)

</div>

<div class="caption">

(2.3-4)

</div>

</div>

the acceleration, Eq. 2.3–3, can be expressed in the following alternate
forms

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0053.jpg](images/e9780486140520_i0053.jpg)

</div>

<div class="caption">

(2.3–5)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0054.jpg](images/e9780486140520_i0054.jpg)

</div>

<div class="caption">

(2.3–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0055.jpg](images/e9780486140520_i0055.jpg)

</div>

<div class="caption">

(2.3–7)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  The position of a particle in a plane is given by the equations

    <div class="blocktext">

    <span class="i">x</span> = 6<span class="i">t y</span> =
    4<span class="i">t</span><sup><span class="i">2</span></sup>

    </div>

    Determine the rectangular components of its velocity and
    acceleration as a function of time.

2.  A projectile is fired with speed
    <span class="i">v</span><sub><span class="i">0</span></sub> at an
    angle <span class="i">θ</span><sub>o</sub> above the horizon.
    Neglecting air friction and the rotation of the earth, the
    acceleration components are
    <span class="i">a</span><sub><span class="i">y</span></sub>
    <span class="i">=</span> −<span class="i">g</span> and
    <span class="i">a</span><sub><span class="i">x</span></sub> = 0.
    Determine the equation for its trajectory, the range
    <span class="i">R</span>, and the maximum height
    <span class="i">H</span>.

3.  A rock is thrown at an angle of 45° with the horizontal, and it just
    clears a wall 24 ft high and 40 ft away. Determine the initial speed
    of the rock.

4.  Find the greatest distance that a stone can be thrown inside a
    horizontal tunnel 15 ft high with an initial speed of 80 ft/sec.
    Find also the corresponding time of flight.

5.  For a gun with a given muzzle speed
    <span class="i">v</span><sub>0</sub>, show that a point
    (<span class="i">x, y</span>) can be hit by two different
    trajectories with initial elevation
    <span class="i">θ</span><sub>1</sub> and
    <span class="i">θ</span><sub>2</sub>.

6.  Derive the equation for the envelope of a series of trajectories of
    a projectile fired with constant speed
    <span class="i">v</span><sub>0</sub> and varying angles
    <span class="i">θ</span><sub>0</sub>.
    <div class="illustype_image_text_net">

    <div class="image_text_net">

    ![e9780486140520_i0056.jpg](images/e9780486140520_i0056.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob.6</span>

    </div>

    </div>

7.  A point moves so that <span class="i">r</span> = 20 + 10t and
    <span class="i">θ</span> = 0.20t<sup>2</sup>. Determine the radial
    and transverse components of the velocity and acceleration at
    <span class="i">t =</span> 2 sec.

8.  A spiral fixed in a plane is given by the equation
    <span class="i">r</span> =
    10<span class="i">e</span><sup>0.2<span class="i">θ</span></sup> If
    a particle moves along the spiral according to the equation
    <span class="i">θ</span> = 0.5<span class="i">t</span><sup>2</sup>,
    determine the radial and transverse components of the velocity and
    acceleration at <span class="i">t</span> = 2.0 sec.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0057.jpg](images/e9780486140520_i0057.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob.8</span>

    </div>

    </div>

9.  In Prob. 8, determine the tangential and normal components of the
    velocity and acceleration, and compare the resultant for the two
    problems.

10. A particle moves along the circumference of a circle of radius
    <span class="i"><span class="b">R</span></span> at constant speed
    <span class="i">v</span><sub>0</sub>. Determine its radial and
    transverse velocity with respect to an origin on the circumference.
    Find the radial and transverse components of the acceleration and
    show that their resultant passes through the center of the circle.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0058.jpg](images/e9780486140520_i0058.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 10</span>

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c02.html_title23"></span>

# <span class="b">2.4 Plane Motion Along a Curve Rotating About 0 (Relative Motion)</span>

A point p moves along a curve s which is rotating with angular velocity
<span class="b">ω</span> and angular acceleration
<span class="imageinline">![e9780486140520_i0059.jpg](images/e9780486140520_i0059.jpg)</span>.
We will attach axes 1 and 2 to curve <span class="i">s</span> so that 1,
2, and <span class="i">s</span> rotate together with
<span class="b">ω</span> and
<span class="imageinline">![e9780486140520_i0060.jpg](images/e9780486140520_i0060.jpg)</span>,
as shown in <a href="#e9780486140520_c02.html#int_11"
id="e9780486140520_c02.html_ref_int_11" class="ref_int">Fig. 2.4-1</a>.

The velocity of <span class="i">p</span> may be determined as follows.
If the point <span class="i">p</span> remained fixed on
<span class="i">s,</span> its velocity due to the angular velocity
<span class="b">ω</span> of the curve and attached coordinate axes is
<span class="b">ω</span> × <span class="b">r</span> which is
perpendicular to r. The motion of p along <span class="i">s</span>
results in an additional velocity <span class="i">dr/dt</span> =
<span class="i"><span class="b">ṡ</span></span><span class="b">1</span><sub><span class="i"><span class="b">t</span></span></sub>
directed along the tangent to <span class="i">s.</span> This latter
component is the velocity relative to the curve <span class="i">s</span>
and can be determined as if the curve <span class="i">s</span> were held
stationary. Thus the sum of the above two components represents the
velocity of point <span class="i">p</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0061.jpg](images/e9780486140520_i0061.jpg)

</div>

<div class="caption">

(2.4-1)

</div>

</div>

and the above equation conforms to Eq. 1.6-3 for the derivative of a
vector referenced to a rotating coordinate
system.<sup><a href="#e9780486140520_ftn01.html#ftn_fn2"
id="e9780486140520_c02.html_ref_ftn_fn2">b</a></sup>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0062.jpg](images/e9780486140520_i0062.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_11"
id="e9780486140520_c02.html_int_11" class="label_int"><span
class="b">Fig. 2.4-1</span></a><span class="b">.</span> Motion along a
rotating curve <span class="i">s</span> in a plane.

</div>

</div>

The acceleration of point <span class="i">p</span> is determined by the
derivative of v or of its two components in Eq. 2.4-1. Since the
coordinates are rotating with angular speed <span class="b">ω</span> ,
the acceleration is given by the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0063.jpg](images/e9780486140520_i0063.jpg)

</div>

<div class="caption">

(2.4-2)

</div>

</div>

which can be interpreted in terms of the two components of
<span class="b">v.</span>

Considering first the component
<span class="i">ṡ</span><span class="b">1</span><sub><span class="i">t</span></sub>,
if the curve is held stationary and <span class="i">p</span> is allowed
to move along it, the acceleration relative to the curve
<span class="i">s</span> would be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0064.jpg](images/e9780486140520_i0064.jpg)

</div>

<div class="caption">

(2.4-3)

</div>

</div>

as in Eq. 2.3-5. The rotation of the coordinate system at
<span class="b">a</span> rate <span class="b">ω</span> introduces an
additional term

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0065.jpg](images/e9780486140520_i0065.jpg)

</div>

<div class="caption">

(2.4-4)

</div>

</div>

which is normal to
<span class="i">ṡ</span><span class="b">1</span><sub><span class="i">t</span></sub>.
Thus we obtain three components of acceleration from the tangential
velocity vector.

The remaining velocity vector <span class="b">ω</span> ×
<span class="b">r</span> is treated similarly. Relative to the
coordinates we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0066.jpg](images/e9780486140520_i0066.jpg)

</div>

<div class="caption">

(2.4-5)

</div>

</div>

The rotation of the coordinates introduces the additional component

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0067.jpg](images/e9780486140520_i0067.jpg)

</div>

<div class="caption">

(2.4-6)

</div>

</div>

which is directed towards the negative <span class="b">r</span>
direction.

Summing all these terms, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0068.jpg](images/e9780486140520_i0068.jpg)

</div>

<div class="caption">

(2.4-7)

</div>

</div>

In this equation the first two terms represent the acceleration of
<span class="i">p</span> relative to the curve <span class="i">s</span>.
The next two terms represent the acceleration of the coincident point
due to angular velocity and angular acceleration of the coordinate
system and the curve <span class="i">s</span> fixed to it. The last term
is known as the Coriolis acceleration, and it is perpendicular to the
relative velocity
<span class="i">ṡ</span><span class="b">1</span><sub><span class="i">t</span></sub>.
The various components of Eq. 2.4-7 are shown in
<a href="#e9780486140520_c02.html#int_11" class="ref_int">Fig. 2.4-1</a>.

</div>

<div class="section1">

<span id="e9780486140520_c02.html_title24"></span>

# <span class="b">2.5 General Case of Space Motion</span>

We now consider the general case of the motion of a particle
<span class="i">p</span> moving with respect to a rigid body which is
itself in motion with respect to a fixed coordinate system, as shown in
<a href="#e9780486140520_c02.html#int_12"
id="e9780486140520_c02.html_ref_int_12" class="ref_int">Fig. 2.5-1</a>.

We will designate the fixed coordinate system by capital letters
<span class="i">X</span><span class="b">,</span>
<span class="i">Y</span><span class="b">,</span>
<span class="i">Z</span><span class="b">,</span> and attach a set of
axes <span class="i">x, y, z</span> on the moving body, calling them the
<span class="i">body axes.</span> Thus the motion of the rigid body is
established by the motion of the origin of the body axes
<span class="i">x, y, z,</span> and a rotation <span class="b">ω</span>
with respect to <span class="i">XYZ.</span> The vector
<span class="b">ω</span> will, in general, vary in magnitude and
direction, both of which can be referenced with respect to the fixed
<span class="i">X</span>, <span class="i">Y, Z</span> axes. Thus the
absolute motion of the particle <span class="i">p</span>, referred to
the <span class="i">X, Y, Z</span> axes, will be equal to the motion of
the particle relative to the body axes x, <span class="i">y, z</span>
(or the body itself) plus the motion of the coincident point (a point on
the body momentarily coinciding with <span class="i">p</span>), which is
further equal to the motion of the moving origin and the additional
motion of the coincident point due to rotations <span class="b">ω</span>
and
<span class="imageinline">![e9780486140520_i0069.jpg](images/e9780486140520_i0069.jpg)</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0070.jpg](images/e9780486140520_i0070.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_12"
id="e9780486140520_c02.html_int_12" class="label_int"><span
class="b">Fig. 2.5-1</span></a><span class="b">.</span> General case of
space motion in terms of body axes <span class="i">x, y, z,</span> and
inertial axes <span class="i">X, Y,</span> <span class="i">Z.</span>

</div>

</div>

To visualize the motion, let the motion of the particle
<span class="i">p</span> with respect to the rigid body be indicated
along a curve <span class="i">s</span> fixed in the body. Thus, this
curve is also fixed with respect to the body axes
<span class="i">x</span>, <span class="i">y, z.</span> An observer
sitting on the body would see only the motion of
<span class="i">p</span> along the curve s.

Let the position of <span class="i">p</span> relative to the
<span class="i">x,</span> <span class="i">y, z</span> axes be
represented by the vector

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0071.jpg](images/e9780486140520_i0071.jpg)

</div>

<div class="caption">

(2.5-1)

</div>

</div>

where <span class="b">i, j,</span> and <span class="b">k</span> are unit
vectors along x, <span class="i">y, z,</span> and, hence, must be
treated as variables due to their changing direction. If we
differentiate r, we will obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0072.jpg](images/e9780486140520_i0072.jpg)

</div>

<div class="caption">

(2.5-2)

</div>

</div>

Since
<span class="i">d</span><span class="b">i</span>/<span class="i">dt</span>
= ω <span class="b">× i</span>,
<span class="i">d</span><span class="b">j</span>/<span class="i">dt</span>
= <span class="b">ω × j,</span>
<span class="i">d</span><span class="b">k</span>/<span class="i">dt</span>
= <span class="b">ω × k</span>, this expression can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0073.jpg](images/e9780486140520_i0073.jpg)

</div>

<div class="caption">

(2.5-3)

</div>

</div>

Interpreting this equation, the first term \[<span class="b">ṙ</span>\]
represents differentiation holding <span class="b">i, j, k</span>
constant and, hence, is the velocity of <span class="i">p</span>
relative to the rotating <span class="i">x, y, z</span> axes, or the
velocity which an observer stationed on the <span class="i">x, y,
z</span> axes is able to detect as the particle moves along the curve s.
The second term <span class="b">ω</span> × <span class="b">r</span> is
the velocity of the coincident point relative to the origin, due to
rotation <span class="b">ω.</span> Finally, we add to the above the
velocity <span class="b">v</span><sub>0</sub> of the moving origin, in
which case the absolute velocity of <span class="i">p</span> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0074.jpg](images/e9780486140520_i0074.jpg)

</div>

<div class="caption">

(2.5-4)

</div>

</div>

To determine the acceleration, we start with the velocity
<span class="b">ṙ</span>, of Eq. 2.5-3, relative to the moving origin,
and differentiate once more

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0075.jpg](images/e9780486140520_i0075.jpg)

</div>

<div class="caption">

(2.5-5)

</div>

</div>

The first two terms result from the differentiation of the first term
\[<span class="i">ẋ</span><span class="b">i</span> +
<span class="i">ẏ</span><span class="b">j</span> +
z<span class="b">k\]</span>, whereas the differentiation of the second
term <span class="b">ω ×</span>
(<span class="i">x</span><span class="b">i</span> +
<span class="i">y</span><span class="b">j</span> +
z<span class="b">k</span>) results in the remaining three terms. We can
now group these terms together as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0076.jpg](images/e9780486140520_i0076.jpg)

</div>

<div class="caption">

(2.5-6)

</div>

</div>

where \[v\] = \[ṙ\] =
\[<span class="i">ẋ</span><span class="b">i</span> +
<span class="i">ẏ</span><span class="b">j</span> +
<span class="i">ż</span><span class="b">k</span>\] is the velocity of
<span class="i">p</span> relative to the body axes
\[<span class="b">a</span>\] =
\[<span class="i">ẍ</span><span class="b">i</span> +
<span class="i">ÿ</span><span class="b">j</span> +
<span class="i">z</span><span class="b">k</span>\] is the acceleration
of <span class="i">p</span> relative to the body axes

We now add the acceleration <span class="b">a</span><sub>0</sub> of the
origin, to
<span class="imageinline">![e9780486140520_i0077.jpg](images/e9780486140520_i0077.jpg)</span>
to obtain the total acceleration

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0078.jpg](images/e9780486140520_i0078.jpg)

</div>

<div class="caption">

(2.5-7)

</div>

</div>

The terms ω <span class="b">×</span> ω <span class="b">×</span> r and ώ
<span class="b">×</span> r are the acceleration of the coincident point
and 2ω <span class="b">×</span> \[v\] is the Coriolis acceleration which
is directed normal to the plane containing the vectors
<span class="b">ω</span> and relative velocity \[v\], as given by the
three-finger rule.

The vector Eqs. 2.5–4 and 2.5–7 are in the most compact form for
defining the general case of space motion. All special cases can be
deduced directly from these equations.

<span class="b">  
  
PROBLEMS</span>

1.  A wheel having a 2-ft radius rolls on a belt which is moving to the
    right with a speed of 1 ft/sec. To an observer standing on the
    ground, the center of the wheel appears to move to the left with a
    speed of 3 ft/sec. Determine the velocity of point
    <span class="i">p</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0079.jpg](images/e9780486140520_i0079.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 1</span>

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0080.jpg](images/e9780486140520_i0080.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 2</span>

    </div>

    </div>
2.  At a given instant, bar <span class="i">AC</span> is horizontal and
    bar <span class="i">DB</span> has an angular velocity of 3 rad/sec
    clockwise and angular acceleration of 2 rad/sec<sup>2</sup>
    counterclockwise. Determine the velocity of the slider
    <span class="i">B</span> relative to bar <span class="i">AC</span>
    and the angular velocity and angular acceleration of
    <span class="i">AC.</span>
3.  Pin <span class="i">p</span> which slides on arm
    <span class="i">OC</span> is made to move along the slot
    <span class="i">AB</span> in a disk. If the disk is held stationary
    and <span class="i">OC</span> has an angular velocity of 3 rad/sec
    clockwise, when <span class="i">θ</span> = 30°, determine the
    velocity of <span class="i">p</span> relative to
    <span class="i">OC</span> and also its absolute velocity.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0081.jpg](images/e9780486140520_i0081.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob.3</span>

    </div>

    </div>
4.  Determine the absolute acceleration of <span class="i">p</span> of
    Prob. 3 if, in addition to the data given, the arm
    <span class="i">OC</span> has an angular acceleration of 4
    rad/sec<sup>2</sup> in the counterclockwise direction. Specify all
    its components.
5.  If in Probs. 3 and 4 the data given are relative to the disk which
    is rotating with angular velocity and acceleration of 2 rad/sec and
    4 rad/sec<sup>2</sup> both clockwise, determine the absolute
    velocity and acceleration of <span class="i">p</span>.
6.  A particle moves with velocity <span class="i">kr</span> outward
    along a spoke of a wheel rotating with angular speed
    <span class="imageinline">![e9780486140520_i0082.jpg](images/e9780486140520_i0082.jpg)</span>
    and angular acceleration
    <span class="imageinline">![e9780486140520_i0083.jpg](images/e9780486140520_i0083.jpg)</span>
    Determine its absolute velocity and acceleration, identifying each
    component by a diagram.
7.  An airplane travels overhead at constant altitude
    <span class="i">h</span> and constant horizontal speed
    <span class="i">v</span>. Determine the angular velocity
    <span class="imageinline">![e9780486140520_i0084.jpg](images/e9780486140520_i0084.jpg)</span>
    and angular acceleration
    <span class="imageinline">![e9780486140520_i0085.jpg](images/e9780486140520_i0085.jpg)</span>
    the line of sight of a tracking device on the ground, where
    <span class="i">θ</span> is the angle measured from zenith. How fast
    is the distance to the plane increasing at <span class="i">θ</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0086.jpg](images/e9780486140520_i0086.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 7</span>

    </div>

    </div>
8.  A bomber flying at constant speed
    <span class="i">v</span><sub><span class="i">b</span></sub> and
    constant altitude
    <span class="i">h</span><sub><span class="i">b</span></sub> sees an
    enemy plane flying in the same direction with velocity
    <span class="i">v</span><sub>e</sub> and at a lower altitude
    <span class="i">h</span><sub>e</sub>. Assuming that
    <span class="i">v</span><sub>b</sub> \>
    <span class="i">v</span><sub>e</sub>, show that the angle
    <span class="i">θ</span> of the line of sight at the instant at
    which the bomb should be released must be
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0087.jpg](images/e9780486140520_i0087.jpg)

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0088.jpg](images/e9780486140520_i0088.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 8</span>

    </div>

    </div>
9.  An airplane traveling at constant altitude <span class="i">h</span>
    and constant speed <span class="i">v</span> is observed by a radar
    station a distance <span class="i">s</span> from the vertical plane
    of travel of the airplane. Determine the angular velocity of the
    radar dish about the horizontal and vertical axes from the instant
    when the plane is closest to the station.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0089.jpg](images/e9780486140520_i0089.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob.9</span>

    </div>

    </div>
10. In Prob. 9 determine the angular rates if <span class="i">v</span> =
    450 mph, <span class="i">h</span> = 12,000 ft; <span class="i">s
    =</span> ½ mile, and <span class="i">t =</span> 15 sec.
11. Fuel flows out along the impeller blade of a turbo pump at a speed
    of 100 ft/sec and acceleration of 120 ft/sec<sup>2</sup> relative to
    the blade. If the turbo wheel is running clockwise at 2400 rpm,
    determine the absolute velocity and acceleration of the fuel just
    before it leaves the impeller.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0090.jpg](images/e9780486140520_i0090.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 11</span>

    </div>

    </div>
12. The large wheel of the quick-return mechanism rotates in the
    counterclockwise direction at a constant speed of 120 rpm. Determine
    the velocity of point <span class="i">p</span> as a function of the
    angle <span class="i">θ</span> and the relative velocity of the
    slider <span class="i">s</span>.
13. Determine the angular acceleration of the arm
    <span class="i">Op</span> of Prob. 12 when the crank arm makes an
    angle 30° with the horizontal in the first quadrant.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0091.jpg](images/e9780486140520_i0091.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 12</span>

    </div>

    </div>
14. A bomber traveling with constant speed <span class="i">v</span> at
    constant altitude <span class="i">h</span> spots an enemy plane at a
    lower altitude <span class="i">he</span> and traveling along a line
    perpendicular to his. Assuming <span class="i">he</span> and
    <span class="i">v</span><sub><span class="i">e</span></sub> to be
    constant, determine how far ahead of the intersecting vertical and
    perpendicular planes the bomb should be released.
15. A satellite in a S-to-Npolar orbit of 120 minis observed to travel
    from horizon to horizon in 25 min and pass directly over an
    observation station at latitude 35° N. Determine the direction of
    the path of the satellite relative to the meridian plane passing
    through the station.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0092.jpg](images/e9780486140520_i0092.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 15</span>

    </div>

    </div>
16. A satellite traveling in a circular polar orbit of altitude
    <span class="i">h</span> around the earth has a period of 120 min.
    An observer on the earth’s surface tracks the satellite and finds
    that it is moving at a rate of 15°/min when directly overhead.
    Determine its altitude <span class="i">h.</span>

</div>

<div class="section1">

<span id="e9780486140520_c02.html_title25"></span>

# <span class="b">2.6 Motion Relative to the Rotating Earth</span>

The center of the earth as it moves afound the sun is accelerating
toward the sun. We, however, neglect this acceleration and place a set
of nonrotating axes with origin at the earth’s center as an inertial
system.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0093.jpg](images/e9780486140520_i0093.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c02.html#ref_int_13"
id="e9780486140520_c02.html_int_13" class="label_int"><span
class="b">Fig. 2.6-1</span></a><span class="b">.</span> Motion relative
to earth using axes <span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span> fixed to earth’s surface.

</div>

</div>

We are often interested in the motion of a body relative to the earth’s
surface. Placing a set of axes at a given point <span class="i">O</span>
on the earth’s surface, we orient the <span class="i">z</span> axis
along the plumb line which, for simplicity, we assume to be equal to the
geocentric line. The <span class="i">x</span> and the
<span class="i">y</span> axes then lie in the horizontal plane, and we
orient <span class="i">x</span> along the meridian plane pointing south
and <span class="i">y</span> along the latitude line pointing east as
shown in <a href="#e9780486140520_c02.html#int_13"
id="e9780486140520_c02.html_ref_int_13" class="ref_int">Fig. 2.6-1</a>.

The acceleration of <span class="i">O</span> is <span class="b">Ω × Ω ×
R =</span> −(Ω<sup>2</sup><span class="i">R</span> sin
<span class="i">λ</span> cos <span class="i">λ</span>)i -
(Ω<sup>2</sup><span class="i">R</span> cos<sup>2</sup>
<span class="i">λ</span>)<span class="b">k</span> where the angular
velocity of the earth-fixed coordinate system <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> is
<span class="b">Ω</span>, the earth’s rotational velocity with
components:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0094.jpg](images/e9780486140520_i0094.jpg)

</div>

<div class="caption">

(2.6–1)

</div>

</div>

The acceleration relative to the inertial system is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0095.jpg](images/e9780486140520_i0095.jpg)

</div>

<div class="caption">

(2.6-2)

</div>

</div>

If the only force acting on the body is its weight, then
<span class="b">F</span>/<span class="i">m</span> =
−<span class="i">g</span><span class="b">k</span>, and the acceleration
\[a\] relative to the rotating earth is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0096.jpg](images/e9780486140520_i0096.jpg)

</div>

<div class="caption">

(2.6-3)

</div>

</div>

Since Ω<sup>2</sup> is (0.729 × 10<sup>−4</sup> rad/sec)<sup>2</sup>, it
can be neglected, leaving

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0097.jpg](images/e9780486140520_i0097.jpg)

</div>

<div class="caption">

(2.6-4)

</div>

</div>

Displacements relative to the earth can be found by two integrations of
Eq. 2.6–4. expressed in terms of the <span class="i">x</span>,
<span class="i">y</span>, and <span class="i">z</span> components.

<span class="b">PROBLEMS</span>

1.  Determine, due to the earth’s rotation, the angular deviation of a
    plumb line from the geocentric line at latitude
    <span class="i">λ</span>° N. At what latitude is this deviation a
    maximum?
2.  A particle is dropped from rest at a height of 1 mile at latitude
    32° N. Neglecting air friction and using the
    <span class="i">x</span>, <span class="i">y</span>,
    <span class="i">z</span> coordinate system of
    <a href="#e9780486140520_c02.html#int_13" class="ref_int">Fig. 2.6-1</a>,
    determine where the particle will land.
3.  A bullet is fired vertically at a latitude of 50° N with a muzzle
    speed of 2000 ft/sec. Neglecting air friction, determine the landing
    point of the bullet.
4.  A rocket is fired vertically upward at a point on the earth’s
    surface of latitude <span class="i">λ</span>° N. Determine the
    Coriolis deviation at its maximum height <span class="i">h</span>.
    What is the numerical value of this deviation if
    <span class="i">h</span> = 150 miles and <span class="i">λ</span> =
    35° N.
5.  In Prob. 4, determine the Coriolis deviation during the downward
    flight and compare it with that at maximum height.
    (<span class="i">Caution:</span> Initial lateral velocity for
    downward flight is not zero.)
6.  An airplane is traveling with speed <span class="i">v</span> due
    south with constant altitude at latitude
    <span class="i">λ</span>° N. Determine the Coriolis acceleration
    relative to earth.
7.  At latitude <span class="i">λ</span>° S, a projectile is fired with
    speed <span class="i">v</span><sub>0</sub> in the east-west vertical
    plane at an elevation <span class="i">θ</span><sub>0</sub> in the
    easterly direction. Determine the latitude deviation.

</div>

</div>

<span id="e9780486140520_c03.html"></span>

<div class="chapter">

<span id="e9780486140520_c03.html_title26"></span>

# <span class="b">CHAPTER 3</span>

# <span class="b">Transformation of Coordinates</span>

<div class="section1">

<span id="e9780486140520_c03.html_title27"></span>

# <span class="b">3.1 Transformation of Displacements</span>

Consider a case where the position of a particle
<span class="i">p</span> in space is defined in terms of the
displacement vector <span class="b">r</span> relative to the moving
coordinates <span class="i">xyz</span>, shown in
<a href="#e9780486140520_c03.html#int_14"
id="e9780486140520_c03.html_ref_int_14" class="ref_int">Fig. 3.1-1</a>.
If the displacement of the origin of the moving coordinate system is
<span class="b">R</span><sub>0</sub>, the displacement of
<span class="i">p</span> relative to the fixed coordinates
<span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0098.jpg](images/e9780486140520_i0098.jpg)

</div>

<div class="caption">

(3.1–1)

</div>

</div>

Letting unit vectors along the fixed and moving axes be designated by
<span class="b">i, j, k</span> and <span class="b">i</span>′,
<span class="b">j</span>′, <span class="b">k</span>′ respectively, the
above equation can be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0099.jpg](images/e9780486140520_i0099.jpg)

</div>

<div class="caption">

(3.1-2)

</div>

</div>

We can determine the component of the above vector in any direction by
forming the dot product of the above equation with a unit vector in the
desired direction. For example, the <span class="i">X</span> component
is obtained by the dot product of the above equation with i, etc. The
three rectangular components along the fixed coordinates are, then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0100.jpg](images/e9780486140520_i0100.jpg)

</div>

<div class="caption">

(3.1-3)

</div>

</div>

where the dot product of the various unit vectors represents the
direction cosine between the coordinates.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0101.jpg](images/e9780486140520_i0101.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_14"
id="e9780486140520_c03.html_int_14" class="label_int"><span
class="b">Fig. 3.1-1</span></a>. Transformation between coordinates
<span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span> and <span class="i">X</span>,
<span class="i">Y</span>, <span class="i">Z</span>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0102.jpg](images/e9780486140520_i0102.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_15"
id="e9780486140520_c03.html_int_15" class="label_int"><span
class="b">Fig. 3.1-2</span></a>. Coordinate transformation in a plane.

</div>

</div>

For plane motion with <span class="i">Z</span> =
<span class="i">z</span> = 0 shown in
<a href="#e9780486140520_c03.html#int_15"
id="e9780486140520_c03.html_ref_int_15" class="ref_int">Fig. 3.1-2</a>,
the direction cosines involved are,

<div class="blocktext">

i ∙ i′ = cos<span class="i">θ</span> = j ∙ j′

i ∙ j′ = −sin<span class="i">θ</span> = −j ∙ i′

</div>

so that Eq. 3.1-3 reduces to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0103.jpg](images/e9780486140520_i0103.jpg)

</div>

<div class="caption">

(3.1-4)

</div>

</div>

A convenient way to express the above equations is by the following
matrix equation,<sup><a href="#e9780486140520_ftn01.html#ftn_fn3"
id="e9780486140520_c03.html_ref_ftn_fn3">c</a></sup>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0104.jpg](images/e9780486140520_i0104.jpg)

</div>

<div class="caption">

(3.1-5)

</div>

</div>

The square matrix with the direction cosines for elements is called the
transfer matrix which, in this case, transforms the body coordinates to
the fixed inertial coordinates.

To obtain the inverse transformation from the fixed coordinate system to
the moving coordinate system, we can start with Eq. 3.1–2 arranged as
follows :

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0105.jpg](images/e9780486140520_i0105.jpg)

</div>

<div class="caption">

(3.1-6)

</div>

</div>

and form the dot product with i′ and j′

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0106.jpg](images/e9780486140520_i0106.jpg)

</div>

<div class="caption">

(3.1-7)

</div>

</div>

The above equations in matrix notation become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0107.jpg](images/e9780486140520_i0107.jpg)

</div>

<div class="caption">

(3.1-8)

</div>

</div>

which is the inverse of Eq. 3.1–5. The transfer matrix is here the
inverse of the transfer matrix of Eq. 3.1–5.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0108.jpg](images/e9780486140520_i0108.jpg)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c03.html_title28"></span>

# <span class="b">3.2 Transformation of Velocities</span>

The velocity of any arbitrary <span class="i">fixed point</span> on the
moving coordinate system <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> with respect to the
fixed-axis system is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0109.jpg](images/e9780486140520_i0109.jpg)

</div>

<div class="caption">

(3.2–1)

</div>

</div>

This equation indicates that we can start with the displacement equation
in terms of the rectangular components and differentiate, holding
<span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span> as constants. For instance, if we differentiate
Eq. 3.1–4, with <span class="i">x</span> and <span class="i">y</span>
held constant, we obtain the velocity equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0110.jpg](images/e9780486140520_i0110.jpg)

</div>

<div class="caption">

(3.2-2)

</div>

</div>

Comparing with Eq. 3.1–4, these equations can also be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0111.jpg](images/e9780486140520_i0111.jpg)

</div>

<div class="caption">

(3.2-3)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c03.html_title29"></span>

# <span class="b">3.3 Instantaneous Center</span>

If we define an instantaneous center as a point of zero velocity, we can
find its coordinates in the <span class="i">XY</span> plane by letting
<span class="i">Ẋ</span> = <span class="i">Ẏ</span> = 0 in Eq. 3.2–3.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0112.jpg](images/e9780486140520_i0112.jpg)

</div>

<div class="caption">

(3.3–1)

</div>

</div>

The locus of such points in the fixed plane is the space centrode or the
<span class="i">herpolhode</span> curve. The locus of the instantaneous
center on the moving <span class="i">xy</span> plane is called the body
centrode or the <span class="i">polhode</span> curve.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0113.jpg](images/e9780486140520_i0113.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_16"
id="e9780486140520_c03.html_int_16" class="label_int">Fig. 3.3-1</a>.
Polhode curve rolls on the herpolhode curve.

</div>

</div>

As an illustration, consider a bar <span class="i">AB,</span> shown in
<a href="#e9780486140520_c03.html#int_16"
id="e9780486140520_c03.html_ref_int_16" class="ref_int">Fig. 3.3-1</a>,
the ends of which must move along the vertical and horizontal guides.
Placing the moving coordinates <span class="i">z, y</span> as shown with
the origin coinciding with point <span class="i">A, X</span><sub>0</sub>
= <span class="i">Ẋ</span><sub>0</sub> = 0. We therefore have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0114.jpg](images/e9780486140520_i0114.jpg)

</div>

</div>

which indicates that the locus of the instantaneous center (herpolhode)
in the <span class="i">XY</span> plane is a quarter-circle of radius
equal to the length <span class="i">AB<span class="b">.</span></span>

If for every position of the bar <span class="i">AB</span> a hole is
punched through the two planes at the instantaneous center, the set of
holes on the moving plane will trace out the polhode curve, which in
this case is a half-circle of diameter <span class="i">AB.</span> It is
evident, then, that the polhode curve rolls without slipping on the
herpolhode curve.

</div>

<div class="section1">

<span id="e9780486140520_c03.html_title30"></span>

# <span class="b">3.4 Euler’s Angles</span>

A point on a rigid body can be defined in terms of body-fixed axes
<span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span>. To determine the orientation of the body
itself, we now introduce Euler’s angles <span class="i">ψ</span>,
<span class="i">ϕ</span>, <span class="i">θ</span> which are three
independent quantities capable of defining the position of the
<span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span>, body axes relative to the inertial
<span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> axes, as shown in
<a href="#e9780486140520_c03.html#int_17"
id="e9780486140520_c03.html_ref_int_17" class="ref_int">Fig. 3.4-1</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0115.jpg](images/e9780486140520_i0115.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_17"
id="e9780486140520_c03.html_int_17" class="label_int"><span
class="b">Fig. 3.4-1</span></a> Body axes <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> defined relative to
inertial axes <span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> by Euler’s angles <span class="i">ψ</span>,
<span class="i">ϕ</span>, <span class="i">θ</span>.

</div>

</div>

The position of the body axes can be arrived at by three rotations which
will also define other coordinates often encountered in rigid body
dynamics.

With the <span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span>, axes coinciding with the
<span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> axes, allow the <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> coordinates to rotate
about the <span class="i">Z</span> axis through an angle
<span class="i">ψ</span> so as to take up the position
<span class="i">ξ′η′ζ′</span>, shown in
<a href="#e9780486140520_c03.html#int_18"
id="e9780486140520_c03.html_ref_int_18" class="ref_int">Fig. 3.4-2</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0116.jpg](images/e9780486140520_i0116.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_18"
id="e9780486140520_c03.html_int_18" class="label_int"><span
class="b">Fig. 3.4-2</span></a>. Rotation about <span class="i">Z</span>
axis through angle <span class="i">ψ</span>.

</div>

</div>

The relationship between the two coordinates is then given by the
transfer matrix

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0117.jpg](images/e9780486140520_i0117.jpg)

</div>

<div class="caption">

(3.4-1)

</div>

</div>

We next allow a rotation <span class="i">θ</span> about the
<span class="i">ξ′</span> axis as shown in
<a href="#e9780486140520_c03.html#int_19"
id="e9780486140520_c03.html_ref_int_19" class="ref_int">Fig. 3.4-3</a>,
and let the new position of the <span class="i">ξ′</span>,
<span class="i">η′</span>, <span class="i">ζ′</span> axes be
<span class="i">ξ</span>, <span class="i">η</span>,
<span class="i">ζ</span> with transfer matrix

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0118.jpg](images/e9780486140520_i0118.jpg)

</div>

<div class="caption">

(3.4-2)

</div>

</div>

Finally we allow a spin <span class="i">ϕ</span> about the axis
<span class="i">ζ</span>, as shown in
<a href="#e9780486140520_c03.html#int_20"
id="e9780486140520_c03.html_ref_int_20" class="ref_int">Fig. 3.4-4</a>,
to arrive at the body axes <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span>. The transfer matrix
for this rotation is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0119.jpg](images/e9780486140520_i0119.jpg)

</div>

<div class="caption">

(3.4-3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0120.jpg](images/e9780486140520_i0120.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_19"
id="e9780486140520_c03.html_int_19" class="label_int"><span
class="b">Fig. 3.4-3</span></a>. Rotation about node axis
<span class="i">ξ′</span> = <span class="i">ξ</span> through angle
<span class="i">θ.</span>

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0121.jpg](images/e9780486140520_i0121.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_20"
id="e9780486140520_c03.html_int_20" class="label_int"><span
class="b">Fig. 3.4-4</span></a>. Rotation about <span class="i">z</span>
= <span class="i">ζ</span> axis through spin angle
<span class="i">ϕ</span>.

</div>

</div>

In arriving at the final position of the body axes, we have encountered
four sets of orthogonal axes: <span class="i">X, Y, Z; ξ′, η′, ζ′; ξ, η,
ζ;</span> and <span class="i">x, y, z.</span> Some of these axes
coincide, such as the <span class="i">Zζ′,</span> the
<span class="i">ζz,</span> and the <span class="i">ξ′ξ</span>; however
both letters will be retained to identify the coordinate system referred
to. Of particular interest is the <span class="i">ξ′ξ</span> axis,
called the <span class="i">line of nodes.</span> It represents the
intersection of the transverse body plane <span class="i">xy</span> and
the horizontal inertial plane <span class="i">XY.</span>

Other transformations between these coordinates can be obtained by the
multiplication of two or more transfer matrices. For instance, by
substituting Eq. 3.4–1 into Eq. 3.4-2 we obtain the following
transformation <sup><a href="#e9780486140520_ftn01.html#ftn_fn4"
id="e9780486140520_c03.html_ref_ftn_fn4">d</a></sup> between the
<span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> and the <span class="i">ξ</span>,
<span class="i">η</span>, <span class="i">ζ</span> axes:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0122.jpg](images/e9780486140520_i0122.jpg)

</div>

<div class="caption">

(3.4–4)

</div>

</div>

Substituting Eq. 3.4–4 into Eq. 3.4–3, we obtain the transformation from
the <span class="i">XYZ</span> axes to the body axes
<span class="i">xyz</span>:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0123.jpg](images/e9780486140520_i0123.jpg)

</div>

<div class="caption">

(3.4–5)

</div>

</div>

The inverse transformation from the <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> body axes to the
<span class="i">X</span>, <span class="i">Y</span>,
<span class="i">Z</span> inertial axes can be obtained in a similar
manner by writing Eqs. 3.4–1, 3.4–2 and 3.4–3 in the inverse order,
i.e.,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0124.jpg](images/e9780486140520_i0124.jpg)

</div>

<div class="caption">

(3.4–6)

</div>

</div>

etc. Rules are also available for the direct inversion of matrices. The
inverse of Eq. 3.4–5 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0125.jpg](images/e9780486140520_i0125.jpg)

</div>

<div class="caption">

(3.4–7)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c03.html_title31"></span>

# <span class="b">3.5 Transformation of Angular Velocities</span>

Frequently we need to express the angular velocities
<span class="i">ω</span><sub><span class="i">x</span></sub>
<span class="i">ω</span><sub><span class="i">y</span></sub>
<span class="i">ω</span><sub><span class="i">z</span></sub> about the
body axes <span class="i">x, y, z</span> in terms of Euler’s angles. The
transformation may be pursued as follows.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0126.jpg](images/e9780486140520_i0126.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c03.html#ref_int_21"
id="e9780486140520_c03.html_int_21" class="label_int"><span
class="b">Fig. 3.5-1</span></a> Angular rates of Euler angles.

</div>

</div>

Resolve the angular velocity
<span class="imageinline">![e9780486140520_i0127.jpg](images/e9780486140520_i0127.jpg)</span>
along then <span class="i">ζ</span> and <span class="i">η</span> axes so
that the orthogonal components of
<span class="imageinline">![e9780486140520_i0128.jpg](images/e9780486140520_i0128.jpg)</span>,
<span class="imageinline">![e9780486140520_i0129.jpg](images/e9780486140520_i0129.jpg)</span>,
and
<span class="imageinline">![e9780486140520_i0130.jpg](images/e9780486140520_i0130.jpg)</span>
are
<span class="imageinline">![e9780486140520_i0131.jpg](images/e9780486140520_i0131.jpg)</span>
along <span class="i">ξ</span>,
<span class="imageinline">![e9780486140520_i0132.jpg](images/e9780486140520_i0132.jpg)</span>
sin <span class="i">θ</span> along <span class="i">η</span>, and
<span class="imageinline">![e9780486140520_i0133.jpg](images/e9780486140520_i0133.jpg)</span> +
<span class="imageinline">![e9780486140520_i0134.jpg](images/e9780486140520_i0134.jpg)</span>
cos <span class="i">θ</span> along <span class="i">ζ</span>, as shown in
<a href="#e9780486140520_c03.html#int_21"
id="e9780486140520_c03.html_ref_int_21" class="ref_int">Fig. 3.5-1</a>.

Next resolve the components along the <span class="i">ξ</span> and
<span class="i">η</span> axes to the <span class="i">x</span> and
<span class="i">y</span> directions, the result being

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0135.jpg](images/e9780486140520_i0135.jpg)

</div>

<div class="caption">

(3.5–1)

</div>

</div>

or in its inverse form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0136.jpg](images/e9780486140520_i0136.jpg)

</div>

<div class="caption">

(3.5–2)

</div>

</div>

Arranged in matrix form, these equations become

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0137.jpg](images/e9780486140520_i0137.jpg)

</div>

<div class="caption">

(3.5–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0138.jpg](images/e9780486140520_i0138.jpg)

</div>

<div class="caption">

(3.5–4)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A point <span class="i">P</span> in the inertial space is defined by
    its components <span class="i">X</span><sub>1</sub>,
    <span class="i">Y</span><sub>1</sub>, and
    <span class="i">Z</span><sub>1</sub>. From <span class="i">P</span>
    a perpendicular <span class="i">PN</span> is drawn to a line whose
    direction is specified by the angles <span class="i">α, β,</span>
    and <span class="i">γ.</span> Determine the lengths
    <span class="i">ON</span> and <span class="i">PN.</span>
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0139.jpg](images/e9780486140520_i0139.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 1</span>

    </div>

    </div>

2.  Determine the inertial components of a point (3, 4, 5) in the
    rotating coordinate system <span class="i">x, y, z,</span> specified
    by the Euler angles <span class="i">θ</span> = 30°,
    <span class="i">ψ</span> = 45°, and <span class="i">ϕ</span> = 30°.

3.  Using body-fixed axes along a bar of length <span class="i">I</span>
    whose ends slide along a smooth vertical wall and horizontal floor,
    determine the acceleration of its midpoint.

4.  One end <span class="i">A</span> of a bar <span class="i">AB</span>
    moves along a vertical wall while some intermediate point slides
    over the corner of a step a distance <span class="i">s</span> from
    the wall. Derive the equation for the herpolhode and polhode curves.
    (Use fixed coordinates through the corner <span class="i">O,</span>
    and let <span class="i">Z, Y,</span> be coordinates of the space
    centrode.)
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0140.jpg](images/e9780486140520_i0140.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 4</span>

    </div>

    </div>

5.  The center of a wheel of radius <span class="i">R</span> is moving
    to the right with velocity <span class="i">v</span><sub>0</sub>
    while the angular speed of the wheel is
    <span class="i">ω</span><sub>0</sub> in the counterclockwise
    direction. Using body-fixed axes <span class="i">x′, y′</span> and
    inertial axes <span class="i">X, Y</span> as shown, determine the
    polhode and herpolhode curves.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0141.jpg](images/e9780486140520_i0141.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 5</span>

    </div>

    </div>

6.  The ends of a link of length <span class="i">l</span> =
    <span class="i">kR</span> moves along the circumference and the
    diameter of a circle of radius <span class="i">R.</span> Determine
    the instantaneous center as a function of the angle
    <span class="i">θ.</span>
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0142.jpg](images/e9780486140520_i0142.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 6</span>

    </div>

    </div>

7.  A rod moves in a vertical plane, with the lower end along the
    horizontal and an intermediate point resting against a small pin at
    height <span class="i">h.</span> Determine the instantaneous center
    as a function of <span class="i">θ</span> and plot the polhode and
    herpolhode curves.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0143.jpg](images/e9780486140520_i0143.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 7</span>

    </div>

    </div>

8.  At a given instant a man in a parachute is 60 ft above a 20°
    inclined hillside.

    If his horizontal and vertical velocities are constant and equal to
    10 ft/sec and 20 ft/sec respectively, determine his coordinate as a
    function of time: (<span class="i">a</span>) in the
    <span class="i">X, Y</span> system; (<span class="i">b</span>) in
    the <span class="i">x, y</span> system. Determine the time and place
    of landing on the hillside.

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0144.jpg](images/e9780486140520_i0144.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 8</span>

    </div>

    </div>

9.  A convenient coordinate system for surface navigation on earth is
    the longitude-latitude system with the origin coinciding with the
    moving vehicle shown in the sketch. The <span class="i">x, y</span>
    axes lie in the horizontal plane along the latitude and longitude
    lines. Show that the angular velocities along the coordinates are
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0145.jpg](images/e9780486140520_i0145.jpg)

    </div>

    </div>

    where the i, j, k vectors are along the <span class="i">x, y,
    z</span> directions, and Ω is the earth’s rotational speed.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0146.jpg](images/e9780486140520_i0146.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 9</span>

    </div>

    </div>

10. For the system of Prob. 9, determine the <span class="i">x, y,
    z</span> components of the acceleration.

11. A satellite s circles the earth with the orbit plane making an angle
    α with the earth’s equatorial plane. The <span class="i">X</span>
    axis is oriented so that it passes through the intersection of the
    orbit and equatorial planes. The position of the satellite at any
    time can be given in terms of
    <span class="i">r</span><sub><span class="i">s</span></sub>, the
    distance from the earth’s center,
    <span class="i">ψ</span><sub>s</sub> the angle of the meridian plane
    measured from the <span class="i">X</span> axis,
    <span class="i">and</span> λ<sub><span class="i">s</span></sub> the
    latitude; the corresponding coordinates of an observation station O
    are <span class="i">R</span><sub>0</sub>,
    <span class="i">ψ</span><sub>0</sub><span class="i">,</span> and
    <span class="i">λ</span><sub>0</sub>.

    (<span class="i">a</span>) Determine the angle
    <span class="i">ϕ</span> measured from the <span class="i">X</span>
    axis to <span class="i">r</span><sub>s</sub> in the plane of the
    orbit, in terms of
    <span class="i">ψ</span><sub><span class="i">s</span></sub>,
    <span class="i">λ</span><sub><span class="i">s</span></sub>, and
    <span class="i">α</span>.

    (<span class="i">b</span>) Determine the cosine of the angle between
    <span class="i">R</span><sub>0</sub> and
    <span class="i">r</span><sub><span class="i">s</span></sub>, and the
    straight-line distance between <span class="i">O</span> and
    <span class="i">S</span>. Use <span class="i">h</span> for altitude.

    (<span class="i">c</span>) Determine the direction cosine of the
    line <span class="i">OS</span> relative to <span class="i">X, Y,
    Z</span>.

    (<span class="i">d</span>) Determine the direction cosine of the
    line <span class="i">OS</span> relative to a coordinate system
    <span class="i">x, y, z,</span> with the origin at the observation
    station as shown.

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0147.jpg](images/e9780486140520_i0147.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 11</span>

    </div>

    </div>

12. A vehicle moving relative to the earth is located in terms of its
    position vector <span class="i">r</span> from the center of earth.
    Place the <span class="i">x, y, z</span> axes with the origin
    coinciding with the moving vehicle, but with
    <span class="i">z</span> parallel to r. If the angular velocity of
    the <span class="i">x, y, z</span> coordinate axes is
    <span class="i">ω</span> =
    <span class="i">ω</span><sub><span class="i">x</span></sub><span class="b">i</span> +
    <span class="i">ω</span><sub>y</sub><span class="b">j</span> +
    <span class="i">ω</span><sub><span class="i">z</span></sub><span class="b">k</span>,
    show that the <span class="i">x, y, z</span> components of the
    absolute acceleration of the vehicle are,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0148.jpg](images/e9780486140520_i0148.jpg)

    </div>

    </div>

13. Letting the direction cosines of a rotating coordinate system
    <span class="i">x</span>, <span class="i">y</span>,
    <span class="i">z</span> be specified by
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0149.jpg](images/e9780486140520_i0149.jpg)

    </div>

    </div>

    where <span class="i">l</span><sub><span class="i">Xy</span></sub>
    is the cosine of the angle between <span class="i">X</span> and
    <span class="i">y</span>, determine the equations for the unit
    vectors <span class="b">i′, j′, k′,</span> along <span class="i">x,
    y, z,</span> in terms of the unit vectors <span class="b">i, j,
    k,</span> along <span class="i">X, Y, Z.</span>

14. If the <span class="i">x, y, z</span> coordinate system is rotating
    with angular velocity ω =
    <span class="i">ω</span><sub><span class="i">x</span></sub>i′ +
    <span class="i">ω</span><sub><span class="i">y</span></sub>j′ +
    <span class="i">ω</span><sub><span class="i">z</span></sub><span class="b">k</span>′,
    show that the velocities of the unit vectors are
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0150.jpg](images/e9780486140520_i0150.jpg)

    </div>

    </div>

15. From Probs. 13 and 14, show that the rate of change of the direction
    cosines between the <span class="i">X, Y, Z</span> and
    <span class="i">x, y, z</span> axes is,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0151.jpg](images/e9780486140520_i0151.jpg)

    </div>

    </div>

    etc. Complete the other seven equations.

16. The following relationship for the unit vector k’ can be written.

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0152.jpg](images/e9780486140520_i0152.jpg)

    </div>

    </div>

    This equation leads to the scalar equation

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0153.jpg](images/e9780486140520_i0153.jpg)

    </div>

    </div>

    and two others. Complete the nine scalar relationships of this type.

17. Derive the matrix Eq. 3.4–7.

</div>

</div>

<span id="e9780486140520_c04.html"></span>

<div class="chapter">

<span id="e9780486140520_c04.html_title32"></span>

# <span class="b">CHAPTER 4</span>

# <span class="b">Particle Dynamics (Satellite Orbits)</span>

<div class="section1">

<span id="e9780486140520_c04.html_title33"></span>

# <span class="b">4.1 Force and Momentum</span>

Newton’s laws of motion were formulated for a single particle. If the
mass <span class="i">m</span> of the particle is multiplied by its
velocity <span class="i">v,</span> the resulting product is called the
linear momentum.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0154.jpg](images/e9780486140520_i0154.jpg)

</div>

<div class="caption">

(4.1-1)

</div>

</div>

The velocity v here is measured with respect to an inertial frame of
reference so that, if the position of the particle is defined by its
displacement vector <span class="b">r</span>, the velocity is
<span class="b">v</span> = <span class="b">ṙ</span>.

Newton’s second law states that the time rate of change of momentum is
equal to the force producing it, and this change takes place in the
direction in which the force acts.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0155.jpg](images/e9780486140520_i0155.jpg)

</div>

<div class="caption">

(4.1–2)

</div>

</div>

With <span class="i">m</span> a constant, this equation can also be
written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0156.jpg](images/e9780486140520_i0156.jpg)

</div>

<div class="caption">

(4.1–3)

</div>

</div>

Newton’s first law, which forms the basis for statics, is a special case
of the second law when the force <span class="b">F</span> is zero. It
states that, if the forces acting on a particle balance to give a
resultant force of zero (<span class="b">F</span> =
<span class="b">ṗ</span> = 0), the particle remains at rest
(<span class="b">p</span> = 0), or continues to move in a straight line
with constant velocity or momentum (<span class="b">p</span> =
constant).

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title34"></span>

# <span class="b">4.2 Impulse and Momentum</span>

If the force <span class="b">F</span> is multiplied by the time
<span class="i">dt</span> and integrated, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0157.jpg](images/e9780486140520_i0157.jpg)

</div>

<div class="caption">

(4.2-1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0158.jpg](images/e9780486140520_i0158.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_22"
id="e9780486140520_c04.html_int_22" class="label_int"><span
class="b">Fig.4.2-1</span></a>. Momentum before impact is equal to
momentum after impact.

</div>

</div>

The time integral on the left side of the equation is called the impulse
of the force, so that the above equation states that the change in
momentum of a particle is equal to the impulse of the force acting on
the particle.

When two bodies collide, a large force
<span class="b">f</span>(<span class="i">t</span>) acts for a short
time, and the impulse ʃ <span class="b">f</span>
<span class="i">dt</span> exerted on the two bodies must be equal and
opposite according to Newton’s third law. Since impulse is equal to the
change in momentum, for the two bodies considered together as a system,
the impulses of collision cancel each other. Thus the change in momentum
of the system is zero, and the momentum before impact must equal the
momentum after impact. Energy however, is generally dissipated during
impact, in which case the impulse during relaxation is less than the
impulse during compression. For central impact we let this ratio be
<span class="i">e</span>, the coefficient of restitution, and it can be
shown that <span class="i">e</span> is also expressible in terms of the
velocities as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0159.jpg](images/e9780486140520_i0159.jpg)

</div>

<div class="caption">

(4.2-2)

</div>

</div>

where the sequence of events is illustrated in
<a href="#e9780486140520_c04.html#int_22"
id="e9780486140520_c04.html_ref_int_22" class="ref_int">Fig. 4.2-1</a>.
Thus when no energy is dissipated, the impact is elastic and
<span class="i">e</span> = 1, whereas for the completely plastic impact
the relaxation impulse is zero and <span class="i">e</span> = 0. In
general <span class="i">e</span> depends on the material, shape and the
velocities of the two bodies.

  
  
<span class="b">Example 4.2</span>–<span class="b">1</span>

A honeycomb plastic has a crushing stress of
σ<sub><span class="i">c</span></sub> 1b/in.<sup>2</sup> If a package of
mass <span class="i">m</span> is to be dropped through a height
<span class="i">h</span> without exceeding a deceleration of
<span class="i">ng</span>, determine the cross-sectional area and the
thickness required.

Referring to the sketch, we let ξ be the crushing displacement of the
honeycomb material. The force equation becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0160.jpg](images/e9780486140520_i0160.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

and its integral is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0161.jpg](images/e9780486140520_i0161.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0162.jpg](images/e9780486140520_i0162.jpg)

</div>

<div class="caption">

<span class="b">Ex. 4.2</span>–<span class="b">1.</span>

</div>

</div>

From (<span class="i">a</span>) the required area is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0163.jpg](images/e9780486140520_i0163.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

which substituted into (<span class="i">b</span>) becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0164.jpg](images/e9780486140520_i0164.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

Maximum crushing is attained when
<span class="imageinline">![e9780486140520_i0165.jpg](images/e9780486140520_i0165.jpg)</span>
= 0, or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0166.jpg](images/e9780486140520_i0166.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

Integrating (<span class="i">d</span>) and substituting
(<span class="i">e</span>), the material crushed is given by the
equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0167.jpg](images/e9780486140520_i0167.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title35"></span>

# <span class="b">4.3 Work and Energy</span>

If the force <span class="b">F</span> acting on a particle moves through
a distance <span class="i">d</span><span class="b">r</span>, the work
done is equal to the scalar product <span class="b">F</span> ∙
<span class="i">d</span><span class="b">r</span>. The total work done in
going from <span class="b">r</span><sub>1</sub>, to
<span class="b">r</span><sub>2</sub>, is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0168.jpg](images/e9780486140520_i0168.jpg)

</div>

<div class="caption">

(4.3-1)

</div>

</div>

By substituting for F and changing the variable of integration to time
by <span class="i">d</span><span class="b">r</span> =
<span class="b">v</span> <span class="i">dt</span>, the expression for
work becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0169.jpg](images/e9780486140520_i0169.jpg)

</div>

<div class="caption">

(4.3–2)

</div>

</div>

The scalar quantity
<span class="imageinline">![e9780486140520_i0170.jpg](images/e9780486140520_i0170.jpg)</span>
is called the kinetic energy of the particle, so the work done on the
particle by the force is equal to the change in kinetic energy of the
particle.

We now define a conservative force system as one in which the work done
is a function only of the position, and independent of the path taken by
the force. It follows then that the work done by a conservative force
system around any closed path must be zero.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0171.jpg](images/e9780486140520_i0171.jpg)

</div>

<div class="caption">

(4.3-3)

</div>

</div>

We will now define the potential energy
<span class="i">U</span>(<span class="b">r</span><sub>1</sub>) as the
work done by the conservative force in going from any point
<span class="b">r</span><sub>1</sub> to some reference point
r<sub>0</sub>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0172.jpg](images/e9780486140520_i0172.jpg)

</div>

<div class="caption">

(4.3-4)

</div>

</div>

Thus every point in space can be assigned a scalar potential
<span class="i">U</span>(<span class="b">r</span>) which will depend on
the reference point.

Consider next the work done by a conservative force in going from
<span class="b">r</span><sub>1</sub> to
<span class="b">r</span><sub>2</sub>. Since the work done is independent
of the path taken, we can go from <span class="b">r</span><sub>1</sub>
to <span class="b">r</span><sub>0</sub> to r<sub>2</sub> as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0173.jpg](images/e9780486140520_i0173.jpg)

</div>

<div class="caption">

(4.3-5)

</div>

</div>

Thus the work done in going from <span class="b">r</span><sub>1</sub> to
<span class="b">r</span><sub>2</sub> is the difference in the scalar
potential
−\[<span class="i">U</span>(<span class="b">r</span><sub>2</sub>) −
<span class="i">U</span>(<span class="b">r</span><sub>1</sub>)\], and it
is evident that the result is independent of the reference point. In
terms of the differential displacement, the above equation can be
written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0174.jpg](images/e9780486140520_i0174.jpg)

</div>

<div class="caption">

(4.3-6)

</div>

</div>

which expresses the conservative force in terms of the potential or the
potential energy. This discussion clearly indicates why the reference
point for the potential energy is arbitrary in setting up the
differential equations of motion, which are force or moment equations.

In a conservative system, the total energy is a constant. If we
designate the kinetic energy by the letter <span class="i">T</span>, Eq.
4.3-2 can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0175.jpg](images/e9780486140520_i0175.jpg)

</div>

<div class="caption">

(4.3–7)

</div>

</div>

Rearranging, the total energies at 1 and 2 are seen to be equal,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0176.jpg](images/e9780486140520_i0176.jpg)

</div>

<div class="caption">

(4.3-8)

</div>

</div>

which illustrates the principle of conservation of energy for the
conservative system.

As an example of a conservative force system, we have the gravitational
attraction of the earth, which is inversely proportional to the square
of the distance from the earth’s center,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0177.jpg](images/e9780486140520_i0177.jpg)

</div>

<div class="caption">

(4.3-9)

</div>

</div>

where <span class="b">g</span> and <span class="i">R</span> are the
acceleration of gravity at the earth’s surface and radius of the earth
respectively. If we use the earth’s surface as the reference, the
potential energy, or the potential of a mass <span class="i">m</span> at
height <span class="i">h</span> above the earth’s surface is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0178.jpg](images/e9780486140520_i0178.jpg)

</div>

<div class="caption">

(4.3-10)

</div>

</div>

Thus, for the moderate heights <span class="i">h</span> above the
earth’s surface, <span class="i">h/R</span> is small, and we have for
the potential energy the simple equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0179.jpg](images/e9780486140520_i0179.jpg)

</div>

<div class="caption">

(4.3-11)

</div>

</div>

The moment about an arbitrary point <span class="i">O</span> of the
momentum <span class="b">p</span> =
<span class="i">m</span><span class="b">Ṙ</span> of a particle is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0180.jpg](images/e9780486140520_i0180.jpg)

</div>

<div class="caption">

(4.4–1)

</div>

</div>

where <span class="b">Ṙ</span> is the absolute velocity of
<span class="i">m</span> and <span class="b">r</span> is drawn from
<span class="i">O</span> as shown in
<a href="#e9780486140520_c04.html#int_23"
id="e9780486140520_c04.html_ref_int_23" class="ref_int">Fig. 4.4-1</a>.
Differentiating this equation, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0181.jpg](images/e9780486140520_i0181.jpg)

</div>

<div class="caption">

(4.4–2)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0182.jpg](images/e9780486140520_i0182.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_23"
id="e9780486140520_c04.html_int_23" class="label_int"><span
class="b">Fig. 4.4-1</span></a>. Moment about <span class="i">O</span>
of momentum <span class="i">m</span><span class="b">Ṙ</span> is
<span class="b">r ×</span>
<span class="i">m</span><span class="b">Ṙ</span>.

</div>

</div>

Substituting <span class="b">Ṙ</span> =
<span class="b">Ṙ</span><sub>0</sub> + <span class="b">ṙ</span> and
noting that <span class="b">ṙ</span> × <span class="b">ṙ</span> = 0,
this equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0183.jpg](images/e9780486140520_i0183.jpg)

</div>

<div class="caption">

(4.4-3)

</div>

</div>

To establish the relationship between
<span class="b">ḣ</span><sub>0</sub> and the moment
<span class="b">M</span><sub>0</sub> of the forces
<span class="imageinline">![e9780486140520_i0184.jpg](images/e9780486140520_i0184.jpg)</span>
acting on <span class="i">m</span>, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0185.jpg](images/e9780486140520_i0185.jpg)

</div>

<div class="caption">

(4.4-4)

</div>

</div>

Substituting
<span class="imageinline">![e9780486140520_i0186.jpg](images/e9780486140520_i0186.jpg)</span>
into Eq. 4.4–3, we can also write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0187.jpg](images/e9780486140520_i0187.jpg)

</div>

<div class="caption">

(4.4–5)

</div>

</div>

Several interesting conclusions can be drawn from Eqs. 4.4–4 and 4.4–5
as follows:

a\. If point <span class="i">O</span> is fixed in space, then
<span class="imageinline">![e9780486140520_i0188.jpg](images/e9780486140520_i0188.jpg)</span>
and <span class="b">ṙ</span> = <span class="b">Ṙ</span>, which results
in the simplified equation

<div class="blocktext">

M<sub>0</sub> = ḣ<sub>0</sub>

</div>

b\. If point <span class="i">O</span> is moving with constant velocity,
<span class="imageinline">![e9780486140520_i0189.jpg](images/e9780486140520_i0189.jpg)</span>,
and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0190.jpg](images/e9780486140520_i0190.jpg)

</div>

</div>

which states that the moment is equal to the rate of change of the
apparent moment of momentum expressed in terms of the relative velocity
<span class="b">ṙ</span>.

c\. If either
<span class="imageinline">![e9780486140520_i0191.jpg](images/e9780486140520_i0191.jpg)</span>
and <span class="b">ṙ</span> or <span class="b">Ṙ</span><sub>0</sub> and
<span class="b">ṙ</span> are parallel, again the simplified equations
are valid.

d\. If the system consists of more than one mass, then the second term
of Eq. 4.4–4 becomes
<span class="imageinline">![e9780486140520_i0192.jpg](images/e9780486140520_i0192.jpg)</span>
<span class="i">m</span><span class="b">r</span> which is zero (∑
<span class="i">m</span><span class="b">r</span> = 0) when the point
<span class="i">O</span> coincides with the center of mass. The moment
equation is then the same as in case (<span class="i">b</span>).

  
  

<span class="b">Example 4.4</span>–<span class="b">1</span>

A dumbbell idealized by two masses on a stiff, weightless rod of length
<span class="i">l</span> is dropped without rotation, and the left mass
strikes a ledge with velocity <span class="i">υ</span>. Assuming the
coefficient of restitution to be <span class="i">e</span>, determine the
angular rotation of the dumbbell immediately after impact.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0193.jpg](images/e9780486140520_i0193.jpg)

</div>

<div class="caption">

<span class="b">Ex. 4.4</span>-1

</div>

</div>

The sketch shows the dumbbell immediately after impact. The velocity of
the center of mass immediately after impact is <span class="i">eυ
−</span><span class="imageinline">![e9780486140520_i0194.jpg](images/e9780486140520_i0194.jpg)</span>
, and the change in the linear momentum is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0195.jpg](images/e9780486140520_i0195.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

The change in the moment of momentum about the center of mass is equal
to the moment about the center of mass of the impulse,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0196.jpg](images/e9780486140520_i0196.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

Eliminating the impulse integral, the angular velocity immediately after
impact is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0197.jpg](images/e9780486140520_i0197.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  Assuming that meteors attracted by the earth start at infinity with
    zero speed, determine the speed with which they will strike the
    earth, neglecting friction (radius of earth = 3960 miles).

2.  The acceleration
    <span class="imageinline">![e9780486140520_i0198.jpg](images/e9780486140520_i0198.jpg)</span>
    of a particle acted upon by a central force
    <span class="imageinline">![e9780486140520_i0199.jpg](images/e9780486140520_i0199.jpg)</span>
    , where
    <span class="imageinline">![e9780486140520_i0200.jpg](images/e9780486140520_i0200.jpg)</span>
    is a unit vector along <span class="b">r</span>, is

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0201.jpg](images/e9780486140520_i0201.jpg)

    </div>

    </div>

    Show by the vector method that equal areas are swept out by
    <span class="b">r</span> per unit of time.
    <span class="i">Hint</span>:

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0202.jpg](images/e9780486140520_i0202.jpg)

    </div>

    </div>

3.  A force field in a plane is defined by the equation
    <span class="b">F</span> =
    −<span class="imageinline">![e9780486140520_i0203.jpg](images/e9780486140520_i0203.jpg)</span>
    <span class="b">1</span><sub><span class="i">θ</span></sub> where
    <span class="i">r</span> and <span class="i">θ</span> are polar
    coordinates. Show that the above force does not have a potential
    when the path encloses the origin. Alternatively, describe a closed
    path exclusive of the origin and show that a potential exists.

4.  Show that the moment of momentum about an arbitrary point 0 for a
    system of particles is equal to
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0204.jpg](images/e9780486140520_i0204.jpg)

    </div>

    </div>

    where the notation is that of
    <a href="#e9780486140520_c04.html#int_23" class="ref_int">Fig. 4.4-1</a>.

5.  If a tempered–steel ball, weighing 0.01 lb will support a dead
    weight of 800 lb without being crushed, what is the greatest speed
    with which it can be projected without rupture, perpendicularly
    against a plane for which <span class="i">e</span> = 0.75, assuming
    that the actual pressure is never greater than twice the average
    pressure, and the impact lasts 0.005 sec.

6.  In Ex. 4.4–1 the dumbbell in the horizontal position just prior to
    impact has an angular velocity of 0.2 rad/sec counterclockwise.
    Determine the angular velocity immediately after impact.

7.  In Ex. 4.4–1 determine the velocity of each mass before and after
    impact and prove that the change in the moment of momentum about the
    mass center is
    <span class="imageinline">![e9780486140520_i0205.jpg](images/e9780486140520_i0205.jpg)</span>.

8.  During impact (see
    <a href="#e9780486140520_c04.html#int_22" class="ref_int">Fig. 4.2-1</a>)
    the relative velocity of the two masses becomes equal to zero at the
    instant of maximum compression. Letting the common velocity of the
    masses at this instant be <span class="b">V</span><sub>0</sub>, it
    is possible to write for <span class="i">m</span><sub>1</sub> the
    equations
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0206.jpg](images/e9780486140520_i0206.jpg)

    </div>

    </div>

    and likewise a similar set for <span class="i">m</span><sub>2</sub>.
    Derive Eq. 4.2–2. <span class="i">Hint</span>: When two fractions
    are equal, the two numerators and the two denominators may be added
    without altering their ratio.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title36"></span>

# <span class="b">4.5 Motion Under a Central Force</span>

A force which is always directed towards a fixed point is called a
central force. Choosing the origin <span class="i">O</span> of polar
coordinates as the fixed point, the moment of the central force about 0
must be zero.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0207.jpg](images/e9780486140520_i0207.jpg)

</div>

<div class="caption">

(4.5–1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0208.jpg](images/e9780486140520_i0208.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_24"
id="e9780486140520_c04.html_int_24" class="label_int"><span
class="b">Fig. 4.5-1</span></a>. Radial and transverse components of
orbit velocity.

</div>

</div>

The moment of momentum about <span class="i">O</span> must therefore be
constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0209.jpg](images/e9780486140520_i0209.jpg)

</div>

<div class="caption">

(4.5–2)

</div>

</div>

As shown in <a href="#e9780486140520_c04.html#int_24"
id="e9780486140520_c04.html_ref_int_24" class="ref_int">Fig. 4.5-1</a>,
the magnitude of the cross product

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0210.jpg](images/e9780486140520_i0210.jpg)

</div>

</div>

is equal to twice the area swept out by the radial line per unit time.
It is equal to the moment of momentum per unit mass, and we will
designate it by the letter <span class="i">h.</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0211.jpg](images/e9780486140520_i0211.jpg)

</div>

<div class="caption">

(4.5–3)

</div>

</div>

We will now examine the motion under a central force
<span class="i">F</span>(<span class="i">r</span>) which is some
arbitrary function of <span class="i">r</span> for a unit mass. The
acceleration in the radial and transverse directions are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0212.jpg](images/e9780486140520_i0212.jpg)

</div>

<div class="caption">

(4.5–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0213.jpg](images/e9780486140520_i0213.jpg)

</div>

<div class="caption">

(4.5–5)

</div>

</div>

From the second equation we obtain the integral corresponding to Eq.
4.5–3

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0214.jpg](images/e9780486140520_i0214.jpg)

</div>

</div>

Substituting
<span class="imageinline">![e9780486140520_i0215.jpg](images/e9780486140520_i0215.jpg)</span>
into the first equation, it can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0216.jpg](images/e9780486140520_i0216.jpg)

</div>

<div class="caption">

(4.5–6)

</div>

</div>

or, since

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0217.jpg](images/e9780486140520_i0217.jpg)

</div>

<div class="caption">

(4.5–7)

</div>

</div>

Integrating,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0218.jpg](images/e9780486140520_i0218.jpg)

</div>

<div class="caption">

(4.5–8)

</div>

</div>

To eliminate the time, we note that <span class="i">ṙ</span> =
(<span class="i">dr</span>/<span class="i">dθ</span>)<span class="imageinline">![e9780486140520_i0219.jpg](images/e9780486140520_i0219.jpg)</span>
=
(<span class="i">dr</span>/<span class="i">dθ</span>)(<span class="i">h</span>/<span class="i">r</span><sup>2</sup>).
Thus Eq. 4.5–8 can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0220.jpg](images/e9780486140520_i0220.jpg)

</div>

<div class="caption">

(4.5–9)

</div>

</div>

When <span class="i">F</span>(<span class="i">r</span>) is specified,
the orbit equation is obtained by the integration of the above equation.

Another equation of interest is the speed equation which can be
determined from its two components as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0221.jpg](images/e9780486140520_i0221.jpg)

</div>

<div class="caption">

<span class="b">(4.5–10)</span>

</div>

</div>

Since the direction of <span class="b">h</span> as well as the magnitude
must be a constant, the orbit plane, perpendicular to
<span class="b">h</span>, must also remain fixed. Thus, the motion under
a central force requires a constant area rate and a fixed orientation of
the orbit plane. The motion of planets, as stated by Kepler’s second
law, closely conforms to the above requirements.

<span class="b">PROBLEMS</span>

1.  Determine the equation for the central attractive force
    <span class="i">f</span>(<span class="i">r</span>) for which all
    circular orbits have the same areal rate <span class="i">λ</span>.
2.  Show that a particle in a central repulsive force field varying
    inversely as the square of the distance from the focus will move
    along a branch of a hyperbola.
3.  If a particle describes a circle with the center of force on the
    circumference, determine the law of force.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title37"></span>

# <span class="b">4.6 The Two–Body Problem</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0222.jpg](images/e9780486140520_i0222.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_25"
id="e9780486140520_c04.html_int_25" class="label_int"><span
class="b">Fig. 4.6-1</span></a>. Displacement vectors of two masses and
their center of mass <span class="i">c</span>.

</div>

</div>

Consider two bodies assumed as particles and moving under the influence
of a mutual attractive force. Letting
<span class="b">r</span><sub>1</sub>,
<span class="b">r</span><sub>2</sub>, and
<span class="b">r</span><sub><span class="i">c</span></sub> be the
displacement vectors of each mass and their center of mass, as shown in
<a href="#e9780486140520_c04.html#int_25"
id="e9780486140520_c04.html_ref_int_25" class="ref_int">Fig. 4.6-1</a>,
the vector <span class="b">r</span> =
<span class="b">r</span><sub>1</sub>, −
<span class="b">r</span><sub>2</sub> will define their separation
distance. The distance of each mass from their center of mass is
\[<span class="i">m</span><sub>2</sub>/(<span class="i">m</span><sub>1</sub> +
<span class="i">m</span><sub>2</sub>)\]r and
\[<span class="i">m</span><sub>1</sub>/(<span class="i">m</span><sub>1</sub> +
<span class="i">m</span><sub>2</sub>)\]<span class="b">r</span> so that
<span class="b">r</span><sub>1</sub> and
<span class="b">r</span><sub>2</sub> can be expressed in terms of
<span class="b">r</span><sub><span class="i">c</span></sub> and
<span class="b">r</span> as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0223.jpg](images/e9780486140520_i0223.jpg)

</div>

<div class="caption">

(4.6–1)

</div>

</div>

We now let <span class="b">F</span><sub>1</sub> and
<span class="b">F</span><sub>2</sub> be forces acting on
<span class="i">m</span><sub>1</sub> and
<span class="i">m</span><sub>2</sub> respectively, and write Newton’s
equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0224.jpg](images/e9780486140520_i0224.jpg)

</div>

<div class="caption">

(4.6–2)

</div>

</div>

In addition we can write the equation for the kinetic energy.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0225.jpg](images/e9780486140520_i0225.jpg)

</div>

<div class="caption">

(4.6–3)

</div>

</div>

If we specify that the system is isolated from external forces, then the
resultant force <span class="b">F</span> =
<span class="b">F</span><sub>1</sub> +
<span class="b">F</span><sub>2</sub> = 0, which requires that the
acceleration
<span class="imageinline">![e9780486140520_i0226.jpg](images/e9780486140520_i0226.jpg)</span>
of its center of mass must be zero. The force equations then reduce to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0227.jpg](images/e9780486140520_i0227.jpg)

</div>

<div class="caption">

(4.6–4)

</div>

</div>

Eqs. 4.6–3 and 4.6–4 indicate that the two–body problem can be reduced
to that of a single body with an equivalent mass
(<span class="i">m</span><sub>1</sub><span class="i">m</span><sub>2</sub>)/(m<sub>1</sub> +
<span class="i">m</span><sub>2</sub>) at a distance r from the center of
mass which is either stationary or in uniform motion along a straight
line. It should be noted that the requirement
<span class="b">F</span><sub>1</sub> =
−<span class="b">F</span><sub>2</sub> does not restrict the forces to be
collinear, so that the force system may be a couple as well as a
collinear mutual attraction.

If one of the masses is very large compared to the other, the equivalent
mass
(<span class="i">m</span><sub>1</sub>,<span class="i">m</span><sub>2</sub>)/<span class="i">(m</span><sub>1</sub> +
<span class="i">m</span><sub>2</sub>) reduces to that of the smaller
mass moving relative to the center of the larger mass. This is
essentially the condition encountered when a satellite is placed into an
orbit around the earth. It is, however, of interest to recognize that we
have a two–body problem which can be analyzed exactly in terms of an
equivalent one–body problem.

<span class="b">Example 4.6</span><span class="b">–1</span>

Assume that the ratio of the mass of the moon to that of the moon plus
earth is known as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0228.jpg](images/e9780486140520_i0228.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0229.jpg](images/e9780486140520_i0229.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_26"
id="e9780486140520_c04.html_int_26" class="label_int"><span
class="b">Fig. 4.6-2</span></a> Earth–moon system and their center of
mass.

</div>

</div>

By observation relative to the fixed stars, the angular velocity
<span class="i">ω</span> of the line joining the centers of the earth
and moon can be measured as <span class="i">ω</span> = 2.66 x
10<sup>−6</sup> rad/sec. Show that the distance between the two bodies
is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0230.jpg](images/e9780486140520_i0230.jpg)

</div>

</div>

Referring to <a href="#e9780486140520_c04.html#int_26"
id="e9780486140520_c04.html_ref_int_26" class="ref_int">Fig. 4.6-2</a>,
the center of mass is given by the equation

<div class="blocktext">

<span class="i">m</span><sub>1</sub><span class="i">x</span> =
(<span class="i">D</span> −
<span class="i">x</span>)<span class="i">m</span><sub>2</sub>
<span class="i">x</span> = <span class="i">Dμ</span>

</div>

Equating the force in Eq. 4.6–4 to Newton’s gravitational force, we
obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0231.jpg](images/e9780486140520_i0231.jpg)

</div>

</div>

Substituting 1 − <span class="i">μ</span> =
<span class="i">m</span><sub>1</sub>/(<span class="i">m</span><sub>1</sub> +
<span class="i">m</span><sub>2</sub>), and <span class="i">K</span> =
<span class="i">gR</span><sup>2</sup>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0232.jpg](images/e9780486140520_i0232.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  If the mass of the moon is
    <span class="imageinline">![e9780486140520_i0233.jpg](images/e9780486140520_i0233.jpg)</span>
    times that of the earth and its period is 27.32 days, determine the
    distance in miles between their centers, using
    <span class="i">R</span> = 3960 miles for earth.
2.  Determine the distance from the earth’s center to the center of mass
    of the earth–moon system.
3.  Determine the distance from the center of earth to the neutral point
    where the attractions of the earth and moon balance each other.
4.  Derive the equation,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0234.jpg](images/e9780486140520_i0234.jpg)

    </div>

    </div>

    for the earth–moon system, where
    <span class="i">m</span><sub>2</sub> and
    <span class="i">m</span><sub>1</sub> are the mass of the moon and
    earth respectively, <span class="i">r</span> the distance between
    their centers, and <span class="i">τ</span> the period of rotation
    of the moon about the earth.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title38"></span>

# <span class="b">4.7 Orbits of Planets and Satellites</span>

In the two–body problem where one of the masses is very large compared
to the other, the motion of the smaller mass takes place about the
larger mass whose gravitational attraction is an inverse–square central
force. For an artificial satellite moving around the earth as its focal
center, the gravitational attraction is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0235.jpg](images/e9780486140520_i0235.jpg)

</div>

<div class="caption">

(4.7–1)

</div>

</div>

where <span class="i">M</span> and <span class="i">m</span> are the
masses of the earth and satellite, <span class="i">G</span> is a
constant, and <span class="i">r</span> is the distance of
<span class="i">m</span> from the center of the earth. Equation 4.7–1
also applies to the earth–sun and the moon–earth system. The constant
<span class="i">GM</span> can be evaluated from a simple experiment of a
falling body at the earth’s surface. If the measured acceleration of the
falling body at <span class="i">r</span> = <span class="i">R</span> is
<span class="i">g</span>, then
<span class="i">F</span>/<span class="i">m</span> =
−<span class="i">g</span> =
−<span class="i">GM</span>/<span class="i">R</span><sup>2</sup>. We will
now replace the constant <span class="i">GM</span> =
<span class="i">gR</span><sup>2</sup> by the letter
<span class="i">K</span>. The constant <span class="i">K</span> can also
be calculated from measured observations of earthbound satellite orbits.

Assuming the satellite to be successfully launched, its motion is
governed by the following equations of force;

Radial force

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0236.jpg](images/e9780486140520_i0236.jpg)

</div>

<div class="caption">

(4.7–2)

</div>

</div>

Transverse force

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0237.jpg](images/e9780486140520_i0237.jpg)

</div>

<div class="caption">

(4.7–3)

</div>

</div>

The second equation leads to the statement of conservation of moment of
momentum per unit mass
<span class="imageinline">![e9780486140520_i0238.jpg](images/e9780486140520_i0238.jpg)</span>
= <span class="i">h</span>.

Since our interest is centered about the shape of the orbit, it is
advisable to eliminate the independent variable <span class="i">t</span>
in terms of <span class="i">θ</span> as follows,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0239.jpg](images/e9780486140520_i0239.jpg)

</div>

</div>

Thus by letting 1/<span class="i">r</span> = <span class="i">u</span>,
the following terms are converted to the new variables,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0240.jpg](images/e9780486140520_i0240.jpg)

</div>

</div>

Substituting these quantities into the radial force equation, the
differential equation for the orbit becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0241.jpg](images/e9780486140520_i0241.jpg)

</div>

<div class="caption">

(4.7–4)

</div>

</div>

Equation 4.7–4, being a second–order differential equation, requires two
arbitrary constants in the general solution. The general solution for
this differential equation is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0242.jpg](images/e9780486140520_i0242.jpg)

</div>

<div class="caption">

(4.7–5)

</div>

</div>

where <span class="i">K</span>/<span class="i">h</span><sup>2</sup> is
the particular integral. The constant
<span class="i">θ</span><sub>0</sub> can be made equal to zero by
measuring <span class="i">θ</span> from perigee (a point of minimum
distance from the origin of <span class="i">r</span>).

The evaluation of the constant <span class="i">C</span> can be made from
the energy equation. For a body at heights beyond the influence of the
atmosphere, the system is conservative and the total energy
<span class="i">E</span> = <span class="i">T</span> +
<span class="i">U</span> of any orbit is a constant. In this equation it
is convenient to consider the energies as those associated with a unit
mass.

For the determination of the potential energy per unit mass, we choose
the point at infinity for reference, and from Eq. 4.7—1 we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0243.jpg](images/e9780486140520_i0243.jpg)

</div>

<div class="caption">

(4.7–6)

</div>

</div>

Adding this to the kinetic energy per unit mass, the total energy
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0244.jpg](images/e9780486140520_i0244.jpg)

</div>

<div class="caption">

(4.7–7)

</div>

</div>

In terms of <span class="i">u</span> and <span class="i">θ</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0245.jpg](images/e9780486140520_i0245.jpg)

</div>

<div class="caption">

(4.7–8)

</div>

</div>

so that substituting Eqs. 4.7–8 and 4.7–5 into Eq. 4.7–7 results in

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0246.jpg](images/e9780486140520_i0246.jpg)

</div>

<div class="caption">

(4.7–9)

</div>

</div>

The equation for <span class="i">u</span> can now be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0247.jpg](images/e9780486140520_i0247.jpg)

</div>

<div class="caption">

(4.7–10)

</div>

</div>

where

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0248.jpg](images/e9780486140520_i0248.jpg)

</div>

<div class="caption">

(4.7–11)

</div>

</div>

Equations 4.7–10 and 4.7–11 apply to the general case for the motion
under the inverse–square central force, and the type of orbit is
established by the numerical value of e as follows:

<div class="tableau">

|  |  |
|:---|:---|
| Hyperbola | if <span class="i">e</span> \> 1 |
| Parabola | if <span class="i">e</span> = 1 |
| Ellipse | if 0 \< <span class="i">e</span> \< 1 (perigee corresponding to <span class="i">θ</span> = 0) |
| Circle | if <span class="i">e</span> = 0 |
| Subcircular ellipse | if −1 \< <span class="i">e</span> \< 0 (apogee—point of maximum distance from the origin of r corresponding to θ = 0) |

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title39"></span>

# <span class="b">4.8 Geometry of Conic Sections</span>

Motion under central force results in an orbit which is one of the conic
sections. The conic is the locus of a point whose distance from a fixed
point <span class="i">F</span> and a fixed line
<span class="i">DD</span>′ have a constant ratio
<span class="i">e.</span> The fixed point <span class="i">F</span> is
called the focus, the fixed line <span class="i">DD</span>′ the
directrix, and the ratio e the eccentricity.

Letting <span class="i">m</span> be the distance from the focus to the
directrix <span class="i">DD</span>,′ the polar equation for the conic
is or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0250.jpg](images/e9780486140520_i0250.jpg)

</div>

<div class="caption">

(4.8-1 )

</div>

</div>

By letting <span class="i">θ</span> = 0°, 90°, 180°, and
tan<sup>−1</sup> (<span class="i">b/a</span>), important distances are
found. These are shown in <a href="#e9780486140520_c04.html#int_27"
id="e9780486140520_c04.html_ref_int_27" class="ref_int">Figs. 4.8-1</a>,
<a href="#e9780486140520_c04.html#int_28"
id="e9780486140520_c04.html_ref_int_28" class="ref_int">4.8-2</a>, and
<a href="#e9780486140520_c04.html#int_29"
id="e9780486140520_c04.html_ref_int_29" class="ref_int">4.8-3</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0251.jpg](images/e9780486140520_i0251.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_27"
id="e9780486140520_c04.html_int_27" class="label_int"><span
class="b">Fig. 4.8-1</span></a>. Geometry of the ellipse.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0252.jpg](images/e9780486140520_i0252.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_28"
id="e9780486140520_c04.html_int_28" class="label_int"><span
class="b">Fig. 4.8-2</span></a><span class="b">.</span> Geometry of the
hyperbola.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0253.jpg](images/e9780486140520_i0253.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_29"
id="e9780486140520_c04.html_int_29" class="label_int"><span
class="b">Fig. 4.8-3</span></a><span class="b">.</span> Geometry of the
parabola.

</div>

</div>

<span class="b">PROBLEMS</span>

1.  If <span class="i">x</span> and <span class="i">y</span> are
    rectangular coordinates of a point on the ellipse as shown in
    <a href="#e9780486140520_c04.html#int_27" class="ref_int">Fig. 4.8-1</a>,
    show that <span class="i">x</span> = <span class="i">a</span> cos ψ
    and <span class="i">y</span> = <span class="i">b</span> sin
    <span class="i">ψ,</span> where the angle <span class="i">ψ</span>
    is called the <span class="i">eccentric anomaly. Hint:</span> Use
    equation of ellipse in rectangular coordinates to relate
    <span class="i">y</span> in terms of <span class="i">x.</span>
2.  Show that cos <span class="i">ψ</span> = <span class="i">(a − r)/ae.
    Hint:</span> From
    <a href="#e9780486140520_c04.html#int_27" class="ref_int">Fig. 4.8-1</a>,
    <span class="i">r cos θ</span> = <span class="i">−</span>
    (<span class="i">ae − a</span> cos <span class="i">ψ</span>).
    Combine with <span class="i">r</span> =
    \[<span class="i">a</span>(<span class="i">1 −
    e</span><sup><span class="i">2</span></sup>)\]/(<span class="i">1 +
    e cos θ</span>) to eliminate cos <span class="i">θ</span>.
3.  Prove the relationship
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0254.jpg](images/e9780486140520_i0254.jpg)

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title40"></span>

# <span class="b">4.9 Orbit Established from Initial Conditions</span>

The initial conditions at rocket burnout are:

<div class="blocktext">

<span class="i">r</span> = <span class="i">r</span><sub>0</sub>  
<span class="i">ν</span> = <span class="i">ν</span><sub>0</sub>  
<span class="i">β</span> = <span class="i">β</span><sub>0</sub>

</div>

where <span class="i">β</span> is the heading angle, measured outward
from the normal to <span class="i">r</span>, as shown in
<a href="#e9780486140520_c04.html#int_30"
id="e9780486140520_c04.html_ref_int_30" class="ref_int">Fig. 4.9-1</a>.
From this information we would like to determine the value of the
eccentricity <span class="i">e,</span> which establishes the type of
orbit, and <span class="i">θ</span><sub>0</sub><span class="i">,</span>
the angle between perigee and <span class="i">r</span><sub>0</sub>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0255.jpg](images/e9780486140520_i0255.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_30"
id="e9780486140520_c04.html_int_30" class="label_int"><span
class="b">Fig. 4.9-1</span></a>. Initial conditions at injection into
orbit.

</div>

</div>

We will let <span class="i">r</span><sub><span class="i">n</span></sub>
be the perigee distance at <span class="i">θ</span> = 0 (when
<span class="i">e</span> is negative, <span class="i">θ = 0</span> 0
corresponds to apogee with distance
<span class="i">r</span><sub>e</sub><span class="i">)</span> in which
case we have from Eq. 4.7—10

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0256.jpg](images/e9780486140520_i0256.jpg)

</div>

<div class="caption">

(4.9–1)

</div>

</div>

Equation 4.7–10 can then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0257.jpg](images/e9780486140520_i0257.jpg)

</div>

<div class="caption">

(4.9–2)

</div>

</div>

The components of the initial velocity are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0258.jpg](images/e9780486140520_i0258.jpg)

</div>

<div class="caption">

(4.9–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0259.jpg](images/e9780486140520_i0259.jpg)

</div>

<div class="caption">

(4.9–4)

</div>

</div>

Since from Eq. 4.7–10 we can write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0260.jpg](images/e9780486140520_i0260.jpg)

</div>

<div class="caption">

(4.9–5)

</div>

</div>

substitution for h<sup>2</sup> from Eq. 4.9–3 results in the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0261.jpg](images/e9780486140520_i0261.jpg)

</div>

<div class="caption">

(4.9–6)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0262.jpg](images/e9780486140520_i0262.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_31"
id="e9780486140520_c04.html_int_31" class="label_int"><span
class="b">Fig. 4.9-2</span></a><span class="b">.</span> Orbit
eccentricity established from initial values <span class="i">of β</span>
and
<span class="i">rν</span><sup><span class="i">2</span></sup><span class="i">/K.</span>

</div>

</div>

Solving for <span class="i">e</span> sin
<span class="i">θ</span><sub>0</sub> and <span class="i">e</span> cos
<span class="i">θ</span><sub>0</sub> in Eqs. 4.9–4 and 4.9–6 and
dividing, the angular position from perigee is found

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0263.jpg](images/e9780486140520_i0263.jpg)

</div>

<div class="caption">

(4.9–7)

</div>

</div>

By adding the squares of <span class="i">e</span> sin
<span class="i">θ</span><sub>0</sub> and <span class="i">e</span> cos
<span class="i">θ</span><sub>0</sub><span class="i">,
e</span><sup><span class="i">2</span></sup> is obtained

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0264.jpg](images/e9780486140520_i0264.jpg)

</div>

<div class="caption">

(4.9–8)

</div>

</div>

Equations 4.9–7 and 4.9–8 completely establish the orbit for any initial
conditions
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup><span class="i">2</span></sup><span class="i">/K</span>
and <span class="i">β</span><sub>0</sub> arranged in nondimensional
form. In addition, the total orbit energy established from Eq. 4.7–7 at
burnout is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0265.jpg](images/e9780486140520_i0265.jpg)

</div>

<div class="caption">

(4.9–9)

</div>

</div>

A plot of Eq. 4.9–8 showing e as a function of
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup><span class="i">2</span></sup><span class="i">/K</span>
with <span class="i">β</span><sub>0</sub> as parameter is presented in
<a href="#e9780486140520_c04.html#int_31"
id="e9780486140520_c04.html_ref_int_31" class="ref_int">Fig. 4.9-2</a>.
It is evident that, if <span class="i">β</span><sub>0</sub>
<span class="i">≠</span> 0, <span class="i">e</span> can never become
zero, so that a circular orbit is not possible. Equation 4.9–7 indicates
that, when
<span class="i">(r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K)</span>
cos<sup>2</sup> <span class="i">β</span><sub>0</sub> = 1,
<span class="i">θ</span><sub>0</sub> = 90°. For
<span class="i">(r</span><sub>0</sub><span class="i">ν</span><sub><span class="i">0</span></sub><sup>2</sup><span class="i">/K)</span>
cos<sup>2</sup> <span class="i">β</span><sub>0</sub> \< I and
<span class="i">β</span><sub>0</sub> \> <span class="i">0,
θ</span><sub>0</sub> is in the second quadrant.

<span class="b">PROBLEMS</span>

1.  Explorer No. 7 launched in October 1959 resulted in the following
    observations.

    Apogee distance above earth surface = 664 miles,

    Perigee distance above earth surface = 346 miles,

    Orbit period = 101.2 min.

    Using mean radius of earth to be 3960 miles, calculate
    <span class="i">K</span> for earth.

2.  For Prob. 1, determine the eccentricity and the perigee and apogee
    speeds.

3.  Determine the circular orbit radius for which a satellite will
    remain stationary with respect to earth.

4.  Explorer No. 6 launched in August 1959 is reported to have perigee
    and apogee heights above the earth’s surface of 157 miles and 26,400
    miles. Calculate the orbit period, its eccentricity, and the maximum
    speed.

5.  If the initial conditions for a satellite at rocket burnout are
    <span class="i">β</span><sub>0</sub><span class="i">,
    r</span><sub>0</sub><span class="i">/R,</span> and
    <span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K,</span>
    show that the perigee and apogee distances from the center of the
    earth are given by the equation
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0266.jpg](images/e9780486140520_i0266.jpg)

    </div>

    </div>

    where—corresponds to perigee and + to apogee. Plot
    <span class="i">r</span><sub><span class="i">p</span></sub>/<span class="i">r</span><sub>0</sub>
    and
    <span class="i">r</span><sub>a</sub><span class="i">/r</span><sub>0</sub>
    versus
    <span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K
    \>̅</span> 1 for <span class="i">β</span> = 1 ° and 5°.

6.  Assess the effect of the heading angle error
    <span class="i">β</span><sub><span class="i">0</span></sub> on the
    perigee height when the velocity at rocket burnout is equal to the
    circular orbit value.

7.  Plot <span class="i">θ</span><sub>0</sub> versus
    <span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K,</span>
    with <span class="i">β</span><sub>0</sub> as parameter. Use a range
    of 0 \<
    <span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K</span>
    \< 2 <span class="i">and β</span><sub>0</sub>
    <span class="i">=</span> ½°, 1°, 5°, 10°, 30°.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title41"></span>

# <span class="b">4.10 Satellite Launched with</span> <span class="i"><span class="b">β</span></span><sub>0</sub> <span class="b">= 0</span>

The special case of a satellite launched with
<span class="i">β</span><sub>0</sub> = 0 is instructive because of its
simplicity of interpretation. From Eq. 4.9–7 it is evident that
<span class="i">θ</span><sub>0</sub> = 0, so that the launch point
corresponds with perigee. Equation 4.9–8 now becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0267.jpg](images/e9780486140520_i0267.jpg)

</div>

<div class="caption">

(4.10–1)

</div>

</div>

which is represented by the straight line for
<span class="i">β</span><sub>0</sub> = 0 in
<a href="#e9780486140520_c04.html#int_31" class="ref_int">Fig. 4.9-2</a>.
Equation 4.10–1 indicates that a circular orbit (e = 0) is obtained only
when
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K</span>
= 1 and, <span class="i">β</span><sub>0</sub> = 0. If
<span class="i">v</span><sub>0</sub> or
<span class="i">r</span><sub>0</sub> is increased so that 1 \<
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K</span>
\< 2, the orbit will be an ellipse. For values of
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K</span>
\> 2, the orbit will become a hyperbola and the satellite will escape
from the earth. Thus
<span class="i">r</span><sub>0</sub><span class="i">ν</span><sub>0</sub><sup>2</sup><span class="i">/K</span>
= 2 corresponds to the velocity of escape at height
<span class="i">r</span><sub>0</sub> = <span class="i">R</span> +
<span class="i">z</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0268.jpg](images/e9780486140520_i0268.jpg)

</div>

<div class="caption">

(4.10–2)

</div>

</div>

Considering the geometry of the elliptic orbit, the semimajor and
semiminor axes are:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0269.jpg](images/e9780486140520_i0269.jpg)

</div>

<div class="caption">

(4.10–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0270.jpg](images/e9780486140520_i0270.jpg)

</div>

<div class="caption">

(4.10–4)

</div>

</div>

The apogee distance is:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0271.jpg](images/e9780486140520_i0271.jpg)

</div>

<div class="caption">

(4.10–5)

</div>

</div>

and in terms of the altitude <span class="i">z</span> above the earth’s
surface, the apogee and perigee altitudes are:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0272.jpg](images/e9780486140520_i0272.jpg)

</div>

<div class="caption">

(4.10–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0273.jpg](images/e9780486140520_i0273.jpg)

</div>

<div class="caption">

(4.10–7)

</div>

</div>

Numerical values for small <span class="i">e</span> are given in the
following table to show the nearly circular shape of such elliptic
orbits in spite of the large difference in the apogee and perigee
heights.

<div class="illustype_image_tab">

<div class="caption">

<span class="b">Table 4.10–1</span><span class="b">. Calculations for
Launching Altitude
r</span><sub><span class="b">0</span></sub><span class="b">/R =
1.10</span>

</div>

<div class="image_tab">

![e9780486140520_i0274.jpg](images/e9780486140520_i0274.jpg)

</div>

</div>

For an eccentricity of 0.20, the apogee height is 6.50 times the perigee
height when the launch height is <span class="i">r</span><sub>0</sub> =
1.10<span class="i">R</span>, or approximately 400 miles above the
earth’s surface.

We can next examine the case
<span class="i">r</span><sub>0</sub><span class="i">v</span><sub>0</sub><sup>2</sup><span class="i">/K
\<</span> 1. Equation 4.7–10 with negative e shows that we have an
ellipse with the starting point corresponding to apogee, and perigee is
at <span class="i">θ</span> = 180°. The speed is then not sufficient to
balance the attractive force of the earth, and the satellite distance
<span class="i">r</span> will diminish from its initial value
<span class="i">r</span><sub><span class="i">0</span></sub><span class="i">.</span>
With negative <span class="i">e,</span> the center of the ellipse falls
between the origin and the launching point. It is evident from the
previous set of numbers that the satellite will fall into a region where
atmospheric drag becomes important, even for small negative
<span class="i">e.</span> <a href="#e9780486140520_c04.html#int_32"
id="e9780486140520_c04.html_ref_int_32" class="ref_int">Figure
4.10-1</a> shows one such orbit along with orbits for positive
<span class="i">e.</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0275.jpg](images/e9780486140520_i0275.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_32"
id="e9780486140520_c04.html_int_32" class="label_int"><span
class="b">Fig. 4.10-1</span></a><span class="b">.</span> Satellites
launched with <span class="i">β</span><sub>0</sub> = 0.

</div>

</div>

The period of closed orbits, ellipses, or circles can be found by
dividing the enclosed area by the areal rate <span class="i">h/2.</span>
The area of the ellipse is <span class="i">πab.</span> The semiminor
axis, from
<a href="#e9780486140520_c04.html#int_27" class="ref_int">Fig. 4.8-1</a>,
is <span class="i">b =</span> a
<span class="imageinline">![e9780486140520_i0276.jpg](images/e9780486140520_i0276.jpg)</span>
and <span class="i">h</span> from Eq. 4.9–5 at θ = 0 is
<span class="i">h</span> =
<span class="imageinline">![e9780486140520_i0277.jpg](images/e9780486140520_i0277.jpg)</span>
Thus the equation for the period becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0278.jpg](images/e9780486140520_i0278.jpg)

</div>

<div class="caption">

(4.10–8)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A satellite is launched parallel to the earth’s surface at
    <span class="i">r/R</span> = 1.10 with
    <span class="i">rν</span><sup><span class="i">2</span></sup><span class="i">/K</span>
    = 1.20. Determine the apogee distance and the ratio of the apogee to
    perigee heights above the earth’s surface.
2.  A satellite is launched parallel to the earth’s surface with a
    velocity of 18,000 mph at a height of 400 miles. Calculate the
    apogee height above the earth’s surface and the period.
3.  Plot the escape velocity from the earth as a function of the
    altitude.
4.  Determine and plot the orbit energy level
    <span class="i">Er</span><sub><span class="i">0</span></sub><span class="i">/K</span>
    of circular orbits as a function of the altitude
    <span class="i">z.</span>
5.  For Prob. 4, plot the period versus <span class="i">z.</span>
6.  For bodies launched <span class="i">with β</span><sub>0</sub> = 0 at
    height
    <span class="i">r</span><sub>0</sub><span class="i">/R,</span>
    determine the equation for the apogee distance
    <span class="i">r</span><sub>a</sub> as function of the velocity
    parameter
    <span class="i">rν</span><sup>2</sup><span class="i">/K</span> at
    perigee.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title42"></span>

# <span class="b">4.11 Cotangential Transfer between Coplanar Circular Orbits</span>

Transfer between coplanar circular orbits can be effected by an elliptic
orbit with perigee and apogee distances equal to the radii of the
respective circles, as shown in
<a href="#e9780486140520_c04.html#int_33"
id="e9780486140520_c04.html_ref_int_33" class="ref_int">Fig. 4.11-1</a>.
The cotangential ellipse is known as the

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0279.jpg](images/e9780486140520_i0279.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_33"
id="e9780486140520_c04.html_int_33" class="label_int"><span
class="b">Fig. 4.11-1</span></a><span class="b">.</span> Hohmann
transfer orbit.

</div>

</div>

Hohmann transfer orbit, and it can be shown to be a minimum energy orbit
for transfer between the coplanar circular orbits.

Assuming transfer to take place from 1 to 2, we can obtain the ratio
<span class="i">r</span><sub><span class="i">a</span></sub>/<span class="i">r</span><sub><span class="i">p</span></sub>
from Eq. 4.7–10. Letting θ = 180°, <span class="i">u</span> =
1/<span class="i">r</span><sub><span class="i">a</span></sub> so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0280.jpg](images/e9780486140520_i0280.jpg)

</div>

<div class="caption">

(4.11–1)

</div>

</div>

From Eq. 4.10–1, <span class="i">e</span> can be eliminated in terms of
<span class="i">r</span><sub>p</sub>ν<sub>p</sub><sup><span class="i">2</span></sup><span class="i">/K</span>
as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0281.jpg](images/e9780486140520_i0281.jpg)

</div>

<div class="caption">

(4.11–2)

</div>

</div>

Substituting Eq. 4.11–1 into 4.11–2, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0282.jpg](images/e9780486140520_i0282.jpg)

</div>

<div class="caption">

(4.11–3)

</div>

</div>

which is plotted in <a href="#e9780486140520_c04.html#int_34"
id="e9780486140520_c04.html_ref_int_34" class="ref_int">Fig. 4.11-2</a>.

In interpreting these results, we can assume the space vehicle to be
initially orbiting around the inner circle of radius r<sub>p</sub>. This
requires
<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">ν</span><sub><span class="i">p</span></sub><sup><span class="i">2</span></sup><span class="i">/K</span>
to be equal to 1.0. To escape from the inner circular orbit and travel
along the elliptic transfer orbit of ratio
<span class="i">r</span><sub><span class="i">a</span></sub>/<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">,
r</span><sub><span class="i">p</span></sub><span class="i">ν</span><sub><span class="i">p</span></sub><sup><span class="i">2</span></sup><span class="i">/K</span>
must be increased to a value given by Eq. 4.11–3. This may be
accomplished by firing a rocket in the tangential direction, the
required increase in velocity being

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0283.jpg](images/e9780486140520_i0283.jpg)

</div>

<div class="caption">

(4.11–4)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0284.jpg](images/e9780486140520_i0284.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_34"
id="e9780486140520_c04.html_int_34" class="label_int"><span
class="b">Fig. 4.11-2</span></a>.
<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">ν</span><sub><span class="i">p</span></sub><sup>2</sup><span class="i">/K</span>
necessary for Hohmann transfer between orbits
<span class="i">r</span><sub><span class="i">a</span></sub><span class="i">/r</span><sub><span class="i">p</span></sub><span class="i">.</span>

</div>

</div>

On reaching point 2, the apogee velocity, which can be found by equating
the angular momentum at 1 and 2, i.e.,
<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">ν</span><sub><span class="i">p</span></sub>
=
<span class="i">r</span><sub><span class="i">a</span></sub><span class="i">ν</span><sub><span class="i">a</span></sub>,
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0285.jpg](images/e9780486140520_i0285.jpg)

</div>

<div class="caption">

(4.11–5)

</div>

</div>

Since the circular orbit velocity for radius
<span class="i">r</span><sub><span class="i">a</span></sub> is
<span class="i">r</span><sub><span class="i">a</span></sub><span class="i">v</span><sub><span class="i">a</span></sub><sup><span class="i">2</span></sup><span class="i">/K</span>
= 1, and the apogee velocity as given by Eq. 4.11–5 is less than 1,
another thrust in the forward direction is necessary. The increment in
velocity required at point 2 to go into the circular orbit is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0286.jpg](images/e9780486140520_i0286.jpg)

</div>

<div class="caption">

(4.11–6)

</div>

</div>

Thus the total impulse which must be applied in the direction of motion
is determined by
<span class="i">Δν</span><sub><span class="i">p</span></sub> +
<span class="i">Δν</span><sub><span class="i">a</span></sub><span class="i">,</span>
and the fuel energy corresponding to it is proportional to
(<span class="i">Δν</span><sub><span class="i">p</span></sub> +
<span class="i">Δν</span><sub><span class="i">a</span></sub>)<sup>2</sup>.

It is of interest to compare the total velocity increment to transfer
from orbit 1 to orbit 2 with that of the velocity increment for escape
from orbit 1. The parabolic orbit velocity of escape from radius
<span class="i">r</span><sub><span class="i">p</span></sub> is found
from
<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">ν</span><sub><span class="i">p</span></sub><sup><span class="i">2</span></sup><span class="i">/K</span>
= 2 to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0287.jpg](images/e9780486140520_i0287.jpg)

</div>

<div class="caption">

(4.11–7)

</div>

</div>

which requires a velocity increment of

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0288.jpg](images/e9780486140520_i0288.jpg)

</div>

<div class="caption">

(4.11–8)

</div>

</div>

acquired under a single impulsive thrust.

The total velocity increment for the Hohmann transfer orbit obtained by
adding Eqs. 4.11–4 and 4.11–6 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0289.jpg](images/e9780486140520_i0289.jpg)

</div>

<div class="caption">

(4.11–9)

</div>

</div>

Equating Eqs. 4.11–8 and 4.11–9 we find
<span class="i">r</span><sub><span class="i">a</span></sub>/<span class="i">r</span><sub><span class="i">p</span></sub>
= 3.4. Thus transfer between circular orbits of
<span class="i">r</span><sub><span class="i">a</span></sub>/<span class="i">r</span><sub><span class="i">p</span></sub>
\> 3.4 will require rocket energy in excess of the orbit escape energy.

<div class="section2">

<span id="e9780486140520_c04.html_title43"></span>

# <span class="i">Heliocentric orbits</span>

In considering planetary orbits, the large mass of the sun (99.2 % of
the total mass of the solar system) enables one to ignore all other
forces. Although planetary orbits are ellipses with their orbit planes
inclined slightly from the ecliptic (earth’s orbit plane), great
simplification results from assuming the orbit to be circular and
coplanar.

Assuming coplanar circular orbits, the equations for the Hohmann
transfer orbit are applicable with the numerical values of
<span class="i">K</span> corresponding to the sun.
<span class="i">K</span> for the sun can be found from measured data
pertaining to any planet. Assuming a circular orbit of radius
<span class="i">r</span> for the earth, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0290.jpg](images/e9780486140520_i0290.jpg)

</div>

<div class="caption">

(4.11–10)

</div>

</div>

where <span class="i">r</span> = 490.5 x 10<sup>9</sup> ft = 93 x
10<sup>6</sup> miles

<div class="blocktext">

<span class="i">K</span> =
<span class="i">GM</span><sub><span class="i">s</span></sub> for the
sun  
<span class="i">v</span> =
<span class="i">2πr</span>/<span class="i">τ</span> = velocity of
earth  
<span class="i">τ</span> = 365.25 x 86,400 sec = period of the earth
around the sun

</div>

Substituting these figures into Eq. 4.11–10, <span class="i">K</span>
for the heliocentric system is found to be 4.68 x 10<sup>21</sup>
ft<sup>3</sup>/sec<sup>2</sup>.

Another convenient set of units for planetary and interplanetary orbits
is one referenced to the earth’s orbit, with <span class="i">r</span> =
1 astronomical unit and <span class="i">τ</span> = 1 year. Substituting
unity for these quantities in the period equation
<span class="i">τ</span> =
<span class="imageinline">![e9780486140520_i0291.jpg](images/e9780486140520_i0291.jpg)</span>
the heliocentric constant <span class="i">K</span> becomes equal to
<span class="i">4π</span><sup><span class="i">2</span></sup>
astronomical units cubed per year squared.

<span class="b">PROBLEMS</span>

1.  Discuss how a space vehicle traveling around a circular orbit of
    radius <span class="i">r</span><sub>2</sub> can transfer to a
    coplanar circular orbit of radius
    <span class="i">r</span><sub>1</sub>, where
    <span class="i">r</span><sub>1</sub> \<
    <span class="i">r</span><sub>2</sub><span class="i">.</span>
2.  Show that, if
    <span class="i">r</span><sub>1</sub><span class="i">/r</span><sub>2</sub>
    \< 0.50, the velocity increment necessary for the transfer to the
    inner orbit will exceed that of escape from the outer orbit.
3.  Determine the time of flight for the Hohmann transfer orbit.
4.  Determine the equation for the velocity
    ν/<span class="i">ν</span><sub><span class="i">c</span></sub> versus
    distance
    <span class="i">r</span>/<span class="i">r</span><sub><span class="i">p</span></sub>
    for the Hohmann transfer orbit, where departure is from the inner
    orbit of radius
    <span class="i">r</span><sub><span class="i">p</span></sub> and
    circular orbit speed
    <span class="i">υ</span><sub><span class="i">c</span></sub>.
5.  A rocket traveling in a circular orbit
    <span class="i">r</span><sub>1</sub><span class="i">υ</span><sub>1</sub><sup>2</sup><span class="i">/K</span>
    = 1 is given an impulsive thrust normal to the orbit so that the
    resultant velocity vector makes an angle
    <span class="i">β</span><sub>0</sub> outward from the trangent to
    the departing circular orbit. Determine the new orbit, specifying
    the perigee and apogee distances and the eccentricity. Determine
    <span class="i">θ</span><sub>0</sub> to perigee.
6.  For the maneuver of Prob. 5, determine the areal rate and show that
    the area enclosed from the point of maneuver to apogee is given by
    the equation
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0292.jpg](images/e9780486140520_i0292.jpg)

    </div>

    </div>
7.  A rocket traveling at 18,300 mph at perigee, fires a retrorocket at
    perigee height of 300 miles. What velocity change is necessary to
    reach minimum altitude of 100 miles during the first circuit?
8.  The following table gives the distances of some of the planets from
    the sun.
    <div class="tableau">

    | Planet  | Mean Distance from Sun          |
    |:--------|:--------------------------------|
    | Mercury | 0.39                            |
    | Venus   | 0.72                            |
    | Earth   | 1.0 = 93 x 10<sup>6</sup> miles |
    | Mars    | 1.52                            |
    | Jupiter | 5.2                             |

    </div>

    Assuming the two orbits to be in the same plane, determine the
    Hohmann transfer orbit from earth to Mars and compute the time
    required for transit. Determine the position of Mars in its orbit
    relative to earth for interception to take place.
9.  For the transfer orbit of Prob. 1, determine the velocity increments
    necessary on departure and on arrival.
10. Determine the spherical region around earth where the earth’s
    gravitational attraction dominates over that of the sun.
11. Determine the equation for the escape velocity from the solar
    system. What is its value at the earth’s orbit.

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title44"></span>

# <span class="b">4.12 Transfer Between Coplanar Coaxial Elliptic Orbits</span>

<a href="#e9780486140520_c04.html#int_35"
id="e9780486140520_c04.html_ref_int_35" class="ref_int">Figure
4.12-1</a> shows two coaxial elliptic orbits in the same plane. To
transfer from the inner orbit 1 to the outer orbit 2, it can be shown
that for minimum expenditure of energy, the thrust should be impulsive
at perigee of the inner orbit and apogee of the outer orbit.

We will assume that the orbit parameters <span class="i">e</span> and
<span class="i">a</span> of the two orbits are given. The perigee and
apogee distances are then known from the relationships
<span class="i">r</span><sub><span class="i">p</span></sub> =
<span class="i">a</span>(1 − <span class="i">e</span>)
<span class="i">and r</span><sub><span class="i">α</span></sub> =
<span class="i">a</span>(1 + <span class="i">e</span>).

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0294.jpg](images/e9780486140520_i0294.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_35"
id="e9780486140520_c04.html_int_35" class="label_int"><span
class="b">Fig. 4.12-1</span></a>. Transfer between coplanar, coaxial,
elliptic orbits.

</div>

</div>

Before impulse, the velocity at <span class="i">p</span><sub>1</sub> can
be obtained from Eq. 4.9–6 by letting <span class="i">β =</span> 0 and
<span class="i">θ = 0,</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0295.jpg](images/e9780486140520_i0295.jpg)

</div>

<div class="caption">

(4.12–1)

</div>

</div>

For the transfer orbit, the necessary velocity at perigee can be found
from Eq. 4.11–3 to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0296.jpg](images/e9780486140520_i0296.jpg)

</div>

<div class="caption">

(4.12–2)

</div>

</div>

The increment in velocity required at perigee of the inner orbit is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0297.jpg](images/e9780486140520_i0297.jpg)

</div>

<div class="caption">

(4.12–3)

</div>

</div>

After departure, the vehicle proceeds along the transfer orbit until it
reaches apogee. The velocity as it approaches apogee is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0298.jpg](images/e9780486140520_i0298.jpg)

</div>

<div class="caption">

(4.12–4)

</div>

</div>

The apogee velocity for orbit 2 can be found from Eq. 4.9–6, letting
<span class="i">β</span> = 0 and <span class="i">θ</span> = 180°,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0299.jpg](images/e9780486140520_i0299.jpg)

</div>

<div class="caption">

(4.12–5)

</div>

</div>

The increment in velocity necessary to transfer from orbit
(<span class="i">t</span>) to orbit (2) at apogee is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0300.jpg](images/e9780486140520_i0300.jpg)

</div>

<div class="caption">

(4.12–6)

</div>

</div>

and the total increment in velocity in the tangential direction is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0301.jpg](images/e9780486140520_i0301.jpg)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title45"></span>

# <span class="b">4.13 Orbital Change Due to Impulsive Thrust</span>

In this section we will consider the general problem of changing an
existing orbit to another of a given specification. Such changes may
range from small corrections to an existing orbit, to large changes in
the orbit for maneuvers. It will be assumed that the change will take
place under impulsive thrust; e.g., a change in the direction and
magnitude of the velocity vector takes place under negligible change in
the displacement vector. This idealization is generally acceptable when
the distance traveled during thrust is negligible in comparison to the
radius vector.

In general, our concern is with elliptic and hyperbolic orbits, the
circle and the parabola being special limiting cases. The relationship
between the velocity <span class="i">v,</span> the angular position
<span class="i">θ,</span> the heading angle <span class="i">β,</span>
and the eccentricity <span class="i">e,</span> shown in
<a href="#e9780486140520_c04.html#int_36"
id="e9780486140520_c04.html_ref_int_36" class="ref_int">Fig. 4.13-1</a>,
is already available from Eqs. 4.9–7 and 4.9–8, which are rewritten as
follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0302.jpg](images/e9780486140520_i0302.jpg)

</div>

<div class="caption">

(4.13–1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0303.jpg](images/e9780486140520_i0303.jpg)

</div>

<div class="caption">

(4.13–2)

</div>

</div>

By holding <span class="i">θ</span> constant and varying
<span class="i">β,
rv</span><sup><span class="i">2</span></sup><span class="i">/K</span>
can be computed from Eq. 4.13–1 rearranged as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0304.jpg](images/e9780486140520_i0304.jpg)

</div>

<div class="caption">

(4.13–3)

</div>

</div>

By holding e constant and varying β, the curve for
rυ<sup>2</sup><span class="i">/</span>K versus <span class="i">β</span>
can be computed from Eq. 4.13–2 rearranged as Eq. 4.13–4:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0305.jpg](images/e9780486140520_i0305.jpg)

</div>

<div class="caption">

(4.13–4)

</div>

</div>

These results for the ellipse and the hyperbola are plotted as shown in
<a href="#e9780486140520_c04.html#int_37"
id="e9780486140520_c04.html_ref_int_37" class="ref_int">Figs. 4.13-2</a>
and <a href="#e9780486140520_c04.html#int_38"
id="e9780486140520_c04.html_ref_int_38" class="ref_int">4.13-3</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0306.jpg](images/e9780486140520_i0306.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_36"
id="e9780486140520_c04.html_int_36" class="label_int"><span
class="b">Fig. 4.13-1</span></a>. Displacement, velocity and heading
angle <span class="i">β</span> at any position <span class="i">θ.</span>

</div>

</div>

In addition to these two equations we have the energy relationship of
Eq. 4.7–7,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0307.jpg](images/e9780486140520_i0307.jpg)

</div>

<div class="caption">

(4.13–5)

</div>

</div>

Since E is constant for a given orbit, we can evaluate it at perigee.
Letting θ = <span class="i">β</span> = 0 in Eqs. 4.13–1 and 4.13–2,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0308.jpg](images/e9780486140520_i0308.jpg)

</div>

<div class="caption">

(4.13–6)

</div>

</div>

which substituted into Eq. 4.13–5 with <span class="i">r</span> =
<span class="i">r</span><sub><span class="i">p</span></sub> results in

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0309.jpg](images/e9780486140520_i0309.jpg)

</div>

<div class="caption">

(4.13–7)

</div>

</div>

Since <span class="i">r</span><sub><span class="i">p</span></sub> =
<span class="i">a</span>(1–<span class="i">e</span>) for the ellipse and
<span class="i">r</span><sub><span class="i">p</span></sub> =
<span class="i">a</span>(<span class="i">e</span> − 1) for the hyperbola
(see Sec. 4.8), the energy <span class="i">E</span> can be expressed in
terms of <span class="i">a</span> as follows.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0310.jpg](images/e9780486140520_i0310.jpg)

</div>

<div class="caption">

(4.13–8)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0311.jpg](images/e9780486140520_i0311.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_37"
id="e9780486140520_c04.html_int_37" class="label_int"><span
class="b">Fig. 4.13-2</span></a><span class="b">.</span> Relation
between <span class="i">β</span> and
<span class="i">rν</span><sup><span class="i">2</span></sup><span class="i">/K</span>
with <span class="i">e</span> and <span class="i">θ</span> as parameters
for elliptic orbits.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0312.jpg](images/e9780486140520_i0312.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_38"
id="e9780486140520_c04.html_int_38" class="label_int"><span
class="b">Fig. 4.13-3</span></a><span class="b">.</span> Relation
between <span class="i">β</span> and
<span class="i">rν</span><sup><span class="i">2</span></sup><span class="i">/K</span>
with <span class="i">e</span> and <span class="i">θ</span> as parameters
for hyperbolic orbits.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0313.jpg](images/e9780486140520_i0313.jpg)

</div>

</div>

Substituting these values into Eq. 4.13–5, the energy equation can be
written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0314.jpg](images/e9780486140520_i0314.jpg)

</div>

<div class="caption">

(4.13–9)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0315.jpg](images/e9780486140520_i0315.jpg)

</div>

<div class="caption">

(4.13–10)

</div>

</div>

Finally, we need an equation from which the time elapsed during travel
along an orbit can be computed. For this we examine the equation for the
moment of momentum,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0316.jpg](images/e9780486140520_i0316.jpg)

</div>

<div class="caption">

(4.13–11)

</div>

</div>

and rearrange it as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0317.jpg](images/e9780486140520_i0317.jpg)

</div>

</div>

For <span class="i">e</span> \< 1, the integral of the left side is (see
Peirce, Short Table of
Integrals,<sup><a href="#e9780486140520_app02.html#end_en1"
id="e9780486140520_c04.html_ref_end_en1">1</a></sup> no. 308 and no.
300),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0318.jpg](images/e9780486140520_i0318.jpg)

</div>

</div>

For <span class="i">e</span> \> 1,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0319.jpg](images/e9780486140520_i0319.jpg)

</div>

</div>

Replacing <span class="i">r</span><sub><span class="i">p</span></sub> in
terms of <span class="i">a</span> and <span class="i">e</span> as
before, the equation for the time becomes:

For elliptic orbits (<span class="i">e</span> \< 1)

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0320.jpg](images/e9780486140520_i0320.jpg)

</div>

<div class="caption">

(4.13–12)

</div>

</div>

For hyperbolic orbits (<span class="i">e</span> \> 1)

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0321.jpg](images/e9780486140520_i0321.jpg)

</div>

<div class="caption">

(4.13–13)

</div>

</div>

<sup>[1](#e9780486140520_app02.html#end_en1)</sup> Third revised
edition, Ginn & Co. 1929.

<div class="illustype_fullpage_image_text">

<div class="fullpage_image_text">

![e9780486140520_i0322.jpg](images/e9780486140520_i0322.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_39"
id="e9780486140520_c04.html_int_39" class="label_int"><span
class="b">Fig. 4.13-4</span></a><span class="b">.</span> Dimensionless
time for elliptic orbits.

</div>

</div>

These equations in nondimensional form,
<span class="imageinline">![e9780486140520_i0323.jpg](images/e9780486140520_i0323.jpg)</span>
and <span class="i">τ</span><sub><span class="i">h</span></sub> =
<span class="imageinline">![e9780486140520_i0324.jpg](images/e9780486140520_i0324.jpg)</span>
have been computed and plotted by
Augenstein<sup>[1](#e9780486140520_app02.html#end_en1)</sup> and are
reproduced here as <a href="#e9780486140520_c04.html#int_39"
id="e9780486140520_c04.html_ref_int_39" class="ref_int">Figs. 4.13-4</a>
and <a href="#e9780486140520_c04.html#int_40"
id="e9780486140520_c04.html_ref_int_40" class="ref_int">4.13-5</a>.

A somewhat simpler expression for the time along the elliptic orbit is
available in terms of the eccentric anomaly <span class="i">ψ.</span>
For its derivation we need the following relationships:

<div class="illustype_fullpage_image_text">

<div class="fullpage_image_text">

![e9780486140520_i0325.jpg](images/e9780486140520_i0325.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_40"
id="e9780486140520_c04.html_int_40" class="label_int"><span
class="b">Fig. 4.13-5</span></a>. Dimensionless time for hyperbolic
orbits.

</div>

</div>

From the equation of the ellipse

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0326.jpg](images/e9780486140520_i0326.jpg)

</div>

</div>

we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0327.jpg](images/e9780486140520_i0327.jpg)

</div>

<div class="caption">

(4.13–14)

</div>

</div>

From Eq. 4.7–11 for the eccentricity, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0328.jpg](images/e9780486140520_i0328.jpg)

</div>

<div class="caption">

(4.13–15)

</div>

</div>

From the invariance of the moment of momentum,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0329.jpg](images/e9780486140520_i0329.jpg)

</div>

<div class="caption">

(4.13–16)

</div>

</div>

From the equation cos <span class="i">ψ</span> =
(<span class="i">a</span> −
<span class="i">r</span>)/<span class="i">ae</span> (see Prob. 2, p.
60),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0330.jpg](images/e9780486140520_i0330.jpg)

</div>

<div class="caption">

(4.13–17)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0331.jpg](images/e9780486140520_i0331.jpg)

</div>

<div class="caption">

(4.13–18)

</div>

</div>

We now write the total energy equation, Eq. 4.7–7, noting that
<span class="imageinline">![e9780486140520_i0332.jpg](images/e9780486140520_i0332.jpg)</span>,
as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0333.jpg](images/e9780486140520_i0333.jpg)

</div>

<div class="caption">

(4.13–19<span class="i">a</span>)

</div>

</div>

Using Eqs. 4.13–14, 4.13–15, and 4.13–16, this equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0334.jpg](images/e9780486140520_i0334.jpg)

</div>

<div class="caption">

(4.13–19<span class="i">b</span>)

</div>

</div>

Substituting Eqs. 4.13–17 and 4.13–18 into Eq.
4.13–19<span class="i">b</span>, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0335.jpg](images/e9780486140520_i0335.jpg)

</div>

<div class="caption">

(4.13–20)

</div>

</div>

Replacing <span class="i">r</span> from the equation cos
<span class="i">ψ</span> = (<span class="i">a</span> −
<span class="i">r</span>)/<span class="i">ae</span>, and rearranging,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0336.jpg](images/e9780486140520_i0336.jpg)

</div>

</div>

which integrates to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0337.jpg](images/e9780486140520_i0337.jpg)

</div>

<div class="caption">

(4.13–21)

</div>

</div>

The constant of integration <span class="i">C</span> is zero if time is
measured from perigee. Equation 4.13–21 is the well–known Kepler
equation for planetary motion.

  
  

<span class="b">Example 4.13—1</span>

A satellite is launched with the following initial conditions:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0338.jpg](images/e9780486140520_i0338.jpg)

</div>

</div>

Determine the orbit parameters <span class="i">e</span> and
<span class="i">a/R,</span> and establish the initial position with
respect to perigee.

From Eqs. 4.13–2 and 4.13–1

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0339.jpg](images/e9780486140520_i0339.jpg)

</div>

</div>

These values agree with those of the graph of
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a>.

From Eq. 4.13–9

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0340.jpg](images/e9780486140520_i0340.jpg)

</div>

</div>

<span class="b">Example</span> <span class="b">4.13—2</span>

The satellite orbit of Example 4.13–1 was characterized by
<span class="i">e</span> = 0.508 and <span class="i">a/R</span> = 3.34,
and its launch point was
<span class="i">r</span><sub>0</sub><span class="i">/R</span> = 2.0, 0 =
62°23’. If the satellite continues along this orbit to
<span class="i">θ</span> = 150°, at which time the orbit is to be
increased to a value <span class="i">a</span>/<span class="i">R</span> =
3.60 without rotating the apse line, determine the required increment in
the velocity and its direction.

We first determine the value of
<span class="i">rν</span><sup>2</sup><span class="i">/K</span> and
<span class="i">β</span> before impulse for <span class="i">θ</span> =
150° and <span class="i">e</span> = 0.508. Using subscripts 1 and 2 for
before and after impulse, we find from
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0341.jpg](images/e9780486140520_i0341.jpg)

</div>

</div>

From Eq. 4.13–9 we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0342.jpg](images/e9780486140520_i0342.jpg)

</div>

</div>

Therefore

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0343.jpg](images/e9780486140520_i0343.jpg)

</div>

</div>

To maintain no rotation of the apse line, the new values of
<span class="i">r</span><sub>2</sub><span class="i">υ</span><sub>2</sub><sup><span class="i">2</span></sup><span class="i">/K</span>
and <span class="i">β</span><sub>2</sub> after impulse must lie along
the <span class="i">θ</span> = 150° line in
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a>. (Note that <span class="i">r</span><sub>2</sub>
<span class="i">= r</span><sub>1</sub> for the instantaneous impulse.)
The value of <span class="i">a</span>/<span class="i">R</span> after
impulse is specified as 3.60, so from Eq. 4.13–9 we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0344.jpg](images/e9780486140520_i0344.jpg)

</div>

</div>

Therefore

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0345.jpg](images/e9780486140520_i0345.jpg)

</div>

</div>

The new eccentricity and heading angle corresponding to
<span class="i">r</span><sub>1</sub><span class="i">υ</span><sub>2</sub><sup>2</sup><span class="i">/K</span>
= 0.78 and <span class="i">θ</span> = 150° is, from
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a>,

<div class="blocktext">

<span class="i">e</span><sub>2</sub> = 0.30
<span class="i">β</span><sub>2</sub> = 11°

</div>

(Note <span class="i">e</span><sub>2</sub> = 0.77 and
<span class="i">β</span><sub>2</sub> = 49° is also a solution but one
which requires a larger velocity increment.)
<a href="#e9780486140520_c04.html#int_41"
id="e9780486140520_c04.html_ref_int_41" class="ref_int">Figure
4.13-6</a> shows a rough sketch of the two orbits.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0346.jpg](images/e9780486140520_i0346.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_41"
id="e9780486140520_c04.html_int_41" class="label_int"><span
class="b">Fig. 4.13-6</span></a><span class="b">.</span> Impulsive orbit
change without changing apse line.

</div>

</div>

From the vector diagram of the velocities, the tangential and normal
components of the required velocity increments are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0347.jpg](images/e9780486140520_i0347.jpg)

</div>

</div>

and the total velocity increment is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0348.jpg](images/e9780486140520_i0348.jpg)

</div>

</div>

or 0.202 times the circular velocity at a radial distance
<span class="i">r</span><sub>1</sub>.

  
  
<span class="b">PROBLEMS</span>

1.  If in Example 4.13–2 the impulse of
    <span class="imageinline">![e9780486140520_i0349.jpg](images/e9780486140520_i0349.jpg)</span>
    is applied in the tangential direction, determine the new orbit
    parameters e and a/R and the rotation of the apse line.
2.  In Example 4.13–2 determine the time required for the satellite to
    reach <span class="i">θ</span> = 150° from the initial position of
    <span class="i">θ</span> = 62°23’.
3.  In Prob. 2 determine the eccentric anomaly <span class="i">ψ</span>
    corresponding to the two angles and check the time from Kepler’s
    equation.
4.  A satellite is launched at a height of 400 miles with
    <span class="i">rv</span><sup>2</sup>/<span class="i">K</span> =
    1.50 and <span class="i">β</span><sub>0</sub> = 10°. Determine the
    eccentricity <span class="i">e,</span> the orbit parameter
    <span class="i">a</span>/<span class="i">R</span>, and the position
    <span class="i">θ</span><sub>0</sub>.
5.  If in Prob. 4 the satellite is given an increment in velocity of
    Δ<span class="i">υ</span> = 2000 ft/sec at apogee, determine the new
    orbit, <span class="i">e</span>,
    <span class="i">a</span>/<span class="i">R</span>, and
    <span class="i">θ.</span>
6.  A satellite is placed into an orbit of <span class="i">e</span> =
    0.60 at perigee of height
    <span class="i">r</span>/<span class="i">R</span> = 1.2 with
    <span class="i">υ</span><sup>2</sup> =
    1.6<span class="i">υ</span><sub>0</sub><sup>2</sup><span class="i">,</span>
    where <span class="i">υ</span><sub>0</sub> is the circular velocity
    at this height. Determine <span class="i">a/R</span> of the orbit
    and <span class="i">r</span>/<span class="i">R</span> at
    <span class="i">θ</span> = 100°.
7.  If the satellite of Prob. 6 is to reduce the size of the orbit to
    <span class="i">a/R</span> = 2.23 without rotating the line of apse,
    by an increment of velocity at the position <span class="i">θ</span>
    = 100°, determine the new eccentricity and the components of the
    velocity increment along the tangent and normal to it.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title46"></span>

# <span class="b">4.14 Perturbation of Orbital Parameters</span>

The motion of a space vehicle moving along a specified orbit is
completely defined by the following three equations:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0350.jpg](images/e9780486140520_i0350.jpg)

</div>

<div class="caption">

(4.14—1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0351.jpg](images/e9780486140520_i0351.jpg)

</div>

<div class="caption">

(4.14–2)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0352.jpg](images/e9780486140520_i0352.jpg)

</div>

<div class="caption">

(4.14–3)

</div>

</div>

If at a specified position in the orbit a small impulsive thrust is
imparted, in what way will the orbit parameters be affected? To answer
this question we can examine each of the above equations separately.

Equation 4.14–1 indicates that the angular position of the apse line is
a function of
<span class="i">rυ</span><sup><span class="i">2</span></sup><span class="i">/K</span>
and <span class="i">β,</span> so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0353.jpg](images/e9780486140520_i0353.jpg)

</div>

</div>

Differentiating,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0354.jpg](images/e9780486140520_i0354.jpg)

</div>

<div class="caption">

(4.14–4)

</div>

</div>

The first term of this equation represents a variation of
<span class="i">θ</span> due to a variation in the velocity (i.e.,
<span class="i">r</span> is not changed during impulsive thrust),
holding <span class="i">β</span> constant. This is equivalent to moving
the point in
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a> along the horizontal line.
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Figure
4.13-2</a> shows that, if
<span class="i">rv</span><sup><span class="i">2</span></sup><span class="i">/K</span>
is increased along a horizontal line, then θ decreases, and vice versa.
With larger velocities, the semimajor axis <span class="i">a</span> will
also increase according to Eq. 4.14–3.
<a href="#e9780486140520_c04.html#int_42"
id="e9780486140520_c04.html_ref_int_42" class="ref_int">Figure
4.14-1</a> illustrates how these orbits change with increasing velocity
in the tangential direction. All orbits will be tangent to the velocity
line.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0355.jpg](images/e9780486140520_i0355.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_42"
id="e9780486140520_c04.html_int_42" class="label_int"><span
class="b">Fig. 4.14-1</span></a>. Orbit variation by tangential thrust.

</div>

</div>

To evaluate quantitatively the rotation of the apse line due to an
increment in the tangential velocity, we can differentiate Eq. 4.14–1,
holding <span class="i">β</span> constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0356.jpg](images/e9780486140520_i0356.jpg)

</div>

<div class="caption">

(4.14–5)

</div>

</div>

To reduce this equation further, we first replace the denominator from
Eq. 4.14–1

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0357.jpg](images/e9780486140520_i0357.jpg)

</div>

</div>

then eliminate sin <span class="i">β</span> cos <span class="i">β</span>
=
(<span class="i">K</span>/<span class="i">rυ</span><sup><span class="i">2</span></sup>)<span class="i">e</span>
sin <span class="i">θ</span> (see Eq. 4.9–4) to obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0358.jpg](images/e9780486140520_i0358.jpg)

</div>

<div class="caption">

(4.14–6)

</div>

</div>

If <span class="i">υ</span> is eliminated by Eq. 4.14–3, Eq. 4.14–6 can
also be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0359.jpg](images/e9780486140520_i0359.jpg)

</div>

<div class="caption">

(4.14–7)

</div>

</div>

If next the perturbation of the apse line is desired due to a small
change in <span class="i">β</span>, while holding the magnitude of the
velocity constant, the change in <span class="i">θ</span> can be found
from <a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a> by moving the point along the vertical line. Such a change
corresponds to the second term of Eq. 4.14–4, and the required increment
in the velocity vector is <span class="i">dv,</span> = <span class="i">υ
dβ</span>.

The perturbation in the eccentricity e due to a small increment in the
tangential velocity is again available from
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a> by moving the point along the horizontal
(<span class="i">β</span> = constant) line. It can be determined
analytically by differentiating Eq. 4.14–2, holding β constant. The
result is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0360.jpg](images/e9780486140520_i0360.jpg)

</div>

<div class="caption">

(4.14–8)

</div>

</div>

When the thrust is continuous over a finite length of time, it can be
visualized as a series of small impulses, and the orbit change can be
obtained by a succession of small changes.

<span class="b">PROBLEMS</span>

1.  Holding <span class="i">β</span> constant, integrate the second form
    of Eq. 4.14–5 and compare the rotation of the apse line in Prob.
    4.13–1 with this equation.
2.  Show that Eq. 4.14–8 can be expressed in the form which indicates
    that
    <span class="imageinline">![e9780486140520_i0361.jpg](images/e9780486140520_i0361.jpg)</span>
    = 0 for cos <span class="i">θ</span> =–<span class="i">e</span>.
    Verify points on
    <a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
    4.13-2</a> for which this is true.
3.  According to
    <a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
    4.13-2</a>, for <span class="i">θ</span> greater than a certain
    value there is a value of
    <span class="i">rv</span><sup><span class="i">2</span></sup><span class="i">/K,
    e,</span> and <span class="i">β</span> at which
    <span class="i">dθ/de</span> and <span class="i">dv/de</span> are
    zero. Determine the locus of
    <span class="i">rv</span><sup><span class="i">2</span></sup><span class="i">/K,
    e,</span> and <span class="i">β</span> for such values.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title47"></span>

# <span class="b">4.15 Stability of Small Oscillations about a Circular Orbit</span>

In a central force system, the circular orbit is always possible at a
proper speed when the centrifugal force is balanced by the attractive
force.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0362.jpg](images/e9780486140520_i0362.jpg)

</div>

<div class="caption">

(4.15–1)

</div>

</div>

To determine the stability of such an orbit to a small radial
disturbance <span class="i">r</span><sub>1</sub>, we start with the
general equation for the radial force

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0363.jpg](images/e9780486140520_i0363.jpg)

</div>

<div class="caption">

(4.15–2)

</div>

</div>

and eliminate
<span class="imageinline">![e9780486140520_i0364.jpg](images/e9780486140520_i0364.jpg)</span>
from the condition that the moment of momentum
<span class="imageinline">![e9780486140520_i0365.jpg](images/e9780486140520_i0365.jpg)</span>
must be a constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0366.jpg](images/e9780486140520_i0366.jpg)

</div>

<div class="caption">

(4.15–3)

</div>

</div>

We now let <span class="i">r</span> =
<span class="i">r</span><sub>0</sub> +
<span class="i">r</span><sub>1</sub> =
<span class="i">r</span><sub>0</sub>\[1 +
(<span class="i">r</span><sub>1</sub>/<span class="i">r</span><sub>0</sub>)\],
so that
<span class="imageinline">![e9780486140520_i0367.jpg](images/e9780486140520_i0367.jpg)</span>
and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0368.jpg](images/e9780486140520_i0368.jpg)

</div>

</div>

Also expand <span class="i">F</span>(<span class="i">r</span>) about
<span class="i">r</span><sub>0</sub> by the Taylor series

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0369.jpg](images/e9780486140520_i0369.jpg)

</div>

</div>

Substituting these expansions, ignoring higher-order terms, and noting
that
−<span class="i">h</span><sup>2</sup>/<span class="i">r</span><sub>0</sub><sup>3</sup>
= <span class="i">F</span>(<span class="i">r</span><sub>0</sub>), we
arrive at the differential equation for small oscillations about
<span class="i">r</span><sub>0</sub>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0370.jpg](images/e9780486140520_i0370.jpg)

</div>

<div class="caption">

(4.15–4)

</div>

</div>

This is a well known second order differential equation for harmonic
oscillation
provided—<span class="imageinline">![e9780486140520_i0371.jpg](images/e9780486140520_i0371.jpg)</span>
is a positive number; i.e., for stable oscillations we must have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0372.jpg](images/e9780486140520_i0372.jpg)

</div>

<div class="caption">

(4.15–5)

</div>

</div>

If
<span class="imageinline">![e9780486140520_i0373.jpg](images/e9780486140520_i0373.jpg)</span>
, then the solution is an exponentially increasing function of time and
the system is unstable.

<span class="b">Example 4.15–1</span>

Determine the differential equation for small oscillations about a
circular orbit when the attractive force is
−<span class="i">K</span>/<span class="i">r</span><sup>2</sup>.

We have <span class="i">F</span>(<span class="i">r</span>) = −
<span class="i">K</span>/<span class="i">r</span><sup>2</sup>.
Differentiating,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0374.jpg](images/e9780486140520_i0374.jpg)

</div>

</div>

The differential equation of small oscillations is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0375.jpg](images/e9780486140520_i0375.jpg)

</div>

</div>

and the solution for an initial disturbance of
<span class="i">r</span><sub>1</sub>(0) with
<span class="i">ṙ</span><sub>1</sub>(0) = 0 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0376.jpg](images/e9780486140520_i0376.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  For a central force–<span class="i">K/r</span><sup>n</sup>, show
    that a stable circular orbit is possible only for
    <span class="i">n</span> \< 3.
2.  A body is moving in a circular orbit of radius
    <span class="i">r</span><sub>0</sub> under a central force
    −<span class="i">K</span>/<span class="i">r</span><sup>2</sup>. If
    the body is given a disturbance
    <span class="i">r</span><sub>1</sub>(0), show that the angular speed
    becomes
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0377.jpg](images/e9780486140520_i0377.jpg)

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title48"></span>

# <span class="b">4.16 Interception and Rendezvous</span>

<div class="section2">

<span id="e9780486140520_c04.html_title49"></span>

# <span class="i">Problem 1.</span> (<span class="i">Circular orbits</span>)

We will consider first the problem of two vehicles moving in the same
circular orbit <span class="i">r/R</span>, one leading the other by a
specified angle <span class="i">φ</span><sub>12</sub> as shown in
<a href="#e9780486140520_c04.html#int_43"
id="e9780486140520_c04.html_ref_int_43" class="ref_int">Fig. 4.16-1</a>.
We will let 1 and 2 be the pursuer and the pursued respectively. Since
the orbit is circular,
<span class="i">rυ</span><sub>1</sub><sup>2</sup><span class="i">/K
=</span> 1, <span class="i">β =</span> 0 for both vehicles, and
<span class="i">φ</span><sub>12</sub> remains unchanged until altered by
thrust.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0378.jpg](images/e9780486140520_i0378.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_43"
id="e9780486140520_c04.html_int_43" class="label_int"><span
class="b">Fig. 4.16-1</span></a>. Intercepting and rendezvous on
circular orbit.

</div>

</div>

We wish now for 1 to overtake 2 at some position 3, indicated by angle
<span class="i">φ</span><sub>23</sub><span class="i">,</span> and to
rendezvous with it along the circular orbit. What impulsive velocity
increments are necessary at 1 and 3 ?

The problem is solved in the following manner. First the time required
for 2 to travel to 3 is determined as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0379.jpg](images/e9780486140520_i0379.jpg)

</div>

<div class="caption">

(4.16–1)

</div>

</div>

Vehicle 1 must travel to 3 on a new orbit which will require the same
time. Due to equal radial distances 01 and 03, the perigee for the new
orbit must bisect the angle <span class="i">φ</span><sub>12</sub> +
<span class="i">φ</span><sub>23</sub>. Thus <span class="i">θ</span>
measured from perigee to 3 is
<span class="i">½</span>(<span class="i">φ</span><sub>12</sub> +
<span class="i">φ</span><sub>23</sub>)<span class="i">,</span> as shown
in <a href="#e9780486140520_c04.html#int_43" class="ref_int">Fig.
4.16-1</a>.

We must now choose a value of <span class="i">e</span> for the new orbit
and, together with <span class="i">6,</span> determine
<span class="i">n</span> =
<span class="i">a</span>/<span class="i">R</span> for the time equation.
If <span class="i">e</span> \> 1, we use the hyperbolic formula.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0380.jpg](images/e9780486140520_i0380.jpg)

</div>

<div class="caption">

(4.16–2)

</div>

</div>

From <a href="#e9780486140520_c04.html#int_40" class="ref_int">Fig.
4.13-5</a> we find
<span class="imageinline">![e9780486140520_i0381.jpg](images/e9780486140520_i0381.jpg)</span>
and compute the time for vehicle 1 to travel from
<span class="i">θ</span> = 0 to point 3.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0382.jpg](images/e9780486140520_i0382.jpg)

</div>

<div class="caption">

(4.16–3)<sup>\*</sup>

</div>

</div>

If this value disagrees with ½<span class="i">t</span><sub>23</sub>, a
new <span class="i">e</span> is chosen and the procedure is repeated
until agreement is found.

With <span class="i">e</span> and <span class="i">θ</span> known,
<span class="i">rv</span><sup>2</sup>/K and <span class="i">β</span> are
found from
<a href="#e9780486140520_c04.html#int_38" class="ref_int">Fig.
4.13-3</a>. Since <span class="i">β</span> is zero for the circular
orbit, the new <span class="i">β</span> is the angle between the two
velocity vectors at 3, and the increment in velocity is determined from
the vector triangle as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0383.jpg](images/e9780486140520_i0383.jpg)

</div>

<div class="caption">

(4.16–4)

</div>

</div>

where
<span class="imageinline">![e9780486140520_i0384.jpg](images/e9780486140520_i0384.jpg)</span>
is the circular velocity. Due to symmetry the same
<span class="i">Δυ</span> is applied at 1 to initiate the maneuver, and
at 3 to rendezvous, as shown in
<a href="#e9780486140520_c04.html#int_43" class="ref_int">Fig.
4.16-1</a>.

<span class="b">Example 4.16–1</span>

Given two vehicles on the same circular orbit of
<span class="i">r/R</span> = 3.0, with vehicle 1 lagging vehicle 2 by
80°. It is desired for 1 to intercept and rendezvous with 2 at a
position 3 which is 40° ahead of 2. Determine the transfer orbit and the
required increments of velocity.

We have <span class="i">φ</span><sub>12</sub> = 80°, and
<span class="i">φ</span><sub>23</sub> = 40°, so that perigee for the
transfer orbit is <span class="i">θ</span> = 60°, bisecting angle 103.
The time for 2 to travel to 3 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0385.jpg](images/e9780486140520_i0385.jpg)

</div>

</div>

and the half time is 1465 sec.

As an initial guess, we choose <span class="i">e</span> = 2.0, and from
Eq. 4.16–2 we find <span class="i">a/R.</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0386.jpg](images/e9780486140520_i0386.jpg)

</div>

</div>

From <a href="#e9780486140520_c04.html#int_40" class="ref_int">Fig.
4.13-5</a>, <span class="i">τ</span><sub><span class="i">h</span></sub>
= 0.80 for <span class="i">θ</span> = 60° and <span class="i">e</span> =
2.0. The half time of flight from 1 to 3 is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0387.jpg](images/e9780486140520_i0387.jpg)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0388.jpg](images/e9780486140520_i0388.jpg)

</div>

</div>

Since this is larger than 1465, the orbit is too slow and we seek a
faster one by choosing a larger <span class="i">e</span>. A few trials
result in

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0389.jpg](images/e9780486140520_i0389.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_44"
id="e9780486140520_c04.html_int_44" class="label_int"><span
class="b">Fig. 4.16-2</span></a>. Vehicle (1) intercepting vehicle (2)
at (3).

</div>

</div>

The circular and hyperbolic velocities at 3 are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0390.jpg](images/e9780486140520_i0390.jpg)

</div>

</div>

and the required incremental velocity is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0391.jpg](images/e9780486140520_i0391.jpg)

</div>

</div>

The geometry of the maneuver is shown in
<a href="#e9780486140520_c04.html#int_44"
id="e9780486140520_c04.html_ref_int_44" class="ref_int">Fig. 4.16-2</a>.

</div>

<div class="section2">

<span id="e9780486140520_c04.html_title50"></span>

# <span class="i">Problem 2.</span> (<span class="i">Elliptic orbits</span>)

If the orbit on which the two vehicles are travelingis an ellipse, the
problem becomes somewhat more complicated because the perigee for the
transfer

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0392.jpg](images/e9780486140520_i0392.jpg)

</div>

</div>

orbit cannot be found by inspection as in the circular–orbit case. Using
the same notation as in Prob. 1, the time required for 2 to reach 3 in
<a href="#e9780486140520_c04.html#int_45"
id="e9780486140520_c04.html_ref_int_45" class="ref_int">Fig. 4.16-3</a>
is shown by the shaded areas subtended by the angle 203. A maneuver at 1
must put vehicle 1 on a new orbit, and its subtended angle 103 must
result in the same time. Although angle 103 = <span class="i">φ</span>
is known, the perigee angle <span class="i">θ</span><sub>1</sub> is not
known except in the special case <span class="i">r</span><sub>1</sub> =
<span class="i">r</span><sub>3</sub>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0393.jpg](images/e9780486140520_i0393.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_45"
id="e9780486140520_c04.html_int_45" class="label_int"><span
class="b">Fig. 4.16-3</span></a>. Vehicle (1) intercepting vehicle (2)
at (3) on elliptic orbit.

</div>

</div>

The solution is possible by trial as follows. For the new orbit we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0394.jpg](images/e9780486140520_i0394.jpg)

</div>

<div class="caption">

(4.16–5)

</div>

</div>

Choosing a value of <span class="i">θ</span><sub>1</sub>, the
eccentricity <span class="i">e</span>′ can be found.
<span class="imageinline">![e9780486140520_i0395.jpg](images/e9780486140520_i0395.jpg)</span>
can be found from
<span class="imageinline">![e9780486140520_i0396.jpg](images/e9780486140520_i0396.jpg)</span>
where + is used for <span class="i">e</span>′ \> 1 and − for
<span class="i">e</span>′ \< 1. The angles
<span class="i">θ</span><sub>1</sub>,
<span class="i">θ</span><sub>1</sub> + <span class="i">φ</span>, and
<span class="i">e’</span> will establish
<span class="i">τ</span><sub>1</sub> and
<span class="i">τ</span><sub>3</sub> in
<a href="#e9780486140520_c04.html#int_39" class="ref_int">Fig.
4.13-4</a> or
<a href="#e9780486140520_c04.html#int_40" class="ref_int">4.13-5</a>.
With the value of <span class="i">a</span>/<span class="i">R</span> =
<span class="i">n</span>, the elapsed time is found as in Prob. 1.

When agreement is established between the two elapsed times, the values
of <span class="i">e</span>′ and <span class="i">θ</span><sub>1</sub>
for the transfer orbit will result in
<span class="i">rυ</span><sup><span class="i">2</span></sup>/<span class="i">K</span>
and <span class="i">β</span>′, which can be found from
<a href="#e9780486140520_c04.html#int_37" class="ref_int">Fig.
4.13-2</a> or
<a href="#e9780486140520_c04.html#int_38" class="ref_int">4.13-3</a>.
The remainder of the solution is then straightforward.

</div>

<div class="section2">

<span id="e9780486140520_c04.html_title51"></span>

# <span class="i">Problem 3. (Noncoplanar interception)</span>

Vehicle 2 at <span class="i">t</span> = 0 is at latitude 0 and longitude
0, traveling in a circular polar orbit of
<span class="i">r</span>/<span class="i">R</span> = 2.5 and headed
toward the north. Vehicle 1 at <span class="i">t</span> = 0 is at
latitude 0 and longitude 90° west, and traveling eastward in an
equatorial elliptic orbit of <span class="i">e</span> = 0.50, as shown
in <a href="#e9780486140520_c04.html#int_46"
id="e9780486140520_c04.html_ref_int_46" class="ref_int">Fig. 4.16-4</a>.
The above position of vehicle 1 corresponds to perigee for which
<span class="i">r</span>/<span class="i">R</span> = 1.5. Determine the
impulsive velocity increment at 1 to intercept vehicle 2 at 3 when its
latitude is 30° N.

The procedure for the solution of this problem is very much similar to
that of Prob. 2. The transfer orbit 1, 3 is inclined 30° to the
equatorial plane,
<span class="i">r</span><sub>1</sub>/<span class="i">R</span> = 1.5, and
<span class="i">r</span><sub>3</sub>/<span class="i">R</span> = 2.5, the
angle between r<sub>1</sub> and <span class="i">r</span><sub>3</sub>
being 90°. Perigee for the transfer orbit is again unknown and its
position from <span class="i">r</span><sub>1</sub> is
<span class="i">θ</span><sub>1</sub>.

The elapsed time from 1 to 3 must equal that from 2 to 3, which is

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0397.jpg](images/e9780486140520_i0397.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_46"
id="e9780486140520_c04.html_int_46" class="label_int"><span
class="b">Fig. 4.16-4</span></a>. Interception for noncoplanar orbits.

</div>

</div>

From the general equation of the orbit, we have for the two points on
the transfer orbit,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0398.jpg](images/e9780486140520_i0398.jpg)

</div>

<div class="caption">

(4.16–6)

</div>

</div>

or

<div class="blocktext">

0.666 = <span class="i">e</span>′(cos
<span class="i">θ</span><sub>1</sub> + 1.666 sin
<span class="i">θ</span><sub>1</sub>)

</div>

Choosing a value of <span class="i">θ</span><sub>1</sub>, the
eccentricity of the transfer orbit <span class="i">e</span>′ can be
found from the above equation. With these two values of
<span class="i">e</span>′ and <span class="i">θ</span><sub>1</sub>, we
can compute <span class="i">n</span> from

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0399.jpg](images/e9780486140520_i0399.jpg)

</div>

<div class="caption">

(4.16—7)

</div>

</div>

where + is used for <span class="i">e</span>′ \> 1 and − for
<span class="i">e</span>′ \< 1.

The nondimensional time
<span class="i">τ</span><sub><span class="i">h</span></sub> is next
found from
<a href="#e9780486140520_c04.html#int_40" class="ref_int">Fig.
4.13-5</a> and, with <span class="i">a</span>/<span class="i">R</span>
known, the elapsed time is computed and compared to the required time.

As a first choice of <span class="i">θ</span><sub>1</sub>, try 340°.
Equation 4.16–6 gives <span class="i">e</span>′ = 1.803 and Eq. 4.16—7
gives <span class="i">n =</span>
<span class="imageinline">![e9780486140520_i0400.jpg](images/e9780486140520_i0400.jpg)</span>
<span class="i">=</span> 1.795. From
<a href="#e9780486140520_c04.html#int_40" class="ref_int">Fig.
4.13-5</a>, <span class="i">τ</span><sub><span class="i">h</span></sub>
= 0.15 for <span class="i">θ</span><sub>1</sub> = 340° (same as for
+20°) and <span class="i">τ</span><sub><span class="i">h</span></sub> =
0.80 for <span class="i">θ</span><sub>3</sub> = 70°, making a total for
the elapsed time of
<span class="i">τ</span><sub><span class="i">h</span></sub> = 0.95. The
actual elapsed time is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0401.jpg](images/e9780486140520_i0401.jpg)

</div>

</div>

Since this time is larger than 1670 sec, the orbit is too slow. A few
trials result in the following:

<div class="blocktext">

<span class="i">θ</span><sub>1</sub> = 338° <span class="i">e′</span> =
2.20

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0402.jpg](images/e9780486140520_i0402.jpg)

</div>

</div>

To find the velocity increment, let <span class="i">x</span>,
<span class="i">y</span>, z be radial, transverse, and normal to the
equatorial plane at point 1. Then the components of
<span class="i">υ</span><sub>1</sub> are (see
<a href="#e9780486140520_c04.html#int_47"
id="e9780486140520_c04.html_ref_int_47" class="ref_int">Fig. 4.16-5</a>):

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0403.jpg](images/e9780486140520_i0403.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_47"
id="e9780486140520_c04.html_int_47" class="label_int"><span
class="b">Fig. 4.16-5</span></a>. Velocity increment required at (1) of
<a href="#e9780486140520_c04.html#int_46" class="ref_int">Fig.
4.16-4</a>.

</div>

</div>

The original velocity is entirely in the y direction, and since the
initial orbit was an ellipse with <span class="i">e</span> = 0.50,
<span class="i">r</span><sub><span class="i">p</span></sub><span class="i">υ</span><sub>0</sub><sup>2</sup>/<span class="i">K</span>
= (1 + <span class="i">e</span>) = 1.50 and
<span class="i">υ</span><sub>0</sub> =
<span class="imageinline">![e9780486140520_i0404.jpg](images/e9780486140520_i0404.jpg)</span>
.

The <span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span> components of the velocity increment at 1 are
then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0405.jpg](images/e9780486140520_i0405.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  Two satellites 1 and 2 are in the same circular orbit of
    <span class="i">r/R</span> = <span class="i">a/R</span> = 2 in the
    same plane, but 2 is leading I by the angle
    <span class="i">φ</span><sub>12</sub> = 30°. What velocity
    increments are necessary to intercept and rendezvous when 2 has
    traveled through 45°.

2.  Repeat Prob. I when 2 has traveled 90°.

3.  Two satellites 1 and 2 are in the same circular orbit of
    <span class="i">a</span>/<span class="i">R</span> =
    <span class="i">n</span><sub><span class="i">0</span></sub> in the
    same plane, but 2 is leading 1 by the angle
    <span class="i">φ</span><sub>12</sub>. If 1 fires a retrorocket in
    the tangential direction, show that, in order for the two satellites
    to intercept after 1 has completed one revolution of its subcircular
    orbit, the necessary increment in the velocity is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0406.jpg](images/e9780486140520_i0406.jpg)

    </div>

    </div>

    where <span class="i">υ</span><sub>c</sub> is the circular orbit
    velocity.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0407.jpg](images/e9780486140520_i0407.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 3</span>

    </div>

    </div>

4.  If in Prob. 3 the rocket is fired towards the rear so as to increase
    the velocity, determine the Δ<span class="i">υ</span> necessary to
    intercept vehicle 2 on the <span class="i">N</span>th visit to 1.
    <span class="i">Hint:</span> The time for the
    <span class="i">N</span>th visit of vehicle 2 at point 1 is
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0408.jpg](images/e9780486140520_i0408.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 4</span>

    </div>

    </div>

5.  Two satellites 1 and 2 are traveling in the same elliptic orbit in
    the same plane. The orbit is characterized by
    <span class="i">e</span> = 0.60 and
    <span class="i">a</span>/<span class="i">R</span> = 3.0. When 1 is
    at 150°, 2 is at 170°. If interception and rendezvous are desired
    when 2 reaches <span class="i">θ</span> = 210°, determine the
    transfer orbit and the increments in velocity.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0409.jpg](images/e9780486140520_i0409.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 5</span>

    </div>

    </div>

6.  Satellite 2 is leading satellite 1 by an angle
    <span class="i">φ</span><sub>12</sub> in an elliptic orbit (see
    <a href="#e9780486140520_c04.html#int_45" class="ref_int">Fig.
    4.16-3</a>). To overtake 2 in a decreasingly short time, the
    eccentricity of the transfer orbit must increase to a large value.
    Show that in the limit as <span class="i">e</span> → ∞, the perigee
    of the transfer orbit can be determined from the equation

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0410.jpg](images/e9780486140520_i0410.jpg)

    </div>

    </div>

    For fast transfer orbits, the actual
    <span class="i">θ</span><sub>1</sub> will be close to the above
    value.

7.  Satellite 2 is traveling east in an equatorial circular orbit of
    <span class="i">a</span>/<span class="i">R</span> = 2, being at
    position longitude 0, latitude 0 at time <span class="i">t</span>
    = 0. Satellite 1 at <span class="i">t</span> = 0 is at latitude 90°
    and traveling in an elliptical orbit in the plane, longitude 0, with
    a/<span class="i">R</span> = 2 and e = 0.30. If it is desired for 1
    to intercept 2 at longitude 330°, determine the transfer orbit and
    the components of the velocity increment. The position of 1 at
    <span class="i">t</span> = 0 corresponds to perigee for the elliptic
    orbit.

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title52"></span>

# <span class="b">4.17 Long–Range Ballistic Trajectories</span>

Since the shortest distance between two points on the surface of a
sphere is along a great circle, ballistic trajectories are also
considered in the great circle plane.
<a href="#e9780486140520_c04.html#int_48"
id="e9780486140520_c04.html_ref_int_48" class="ref_int">Figure
4.17-1</a> shows the pertinent geometry of a ballistic trajectory which
is an ellipse with the center of the earth as focus. Perigee is then
inside the earth while the point of maximum height coincides with
apogee.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0411.jpg](images/e9780486140520_i0411.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_48"
id="e9780486140520_c04.html_int_48" class="label_int"><span
class="b">Fig. 4.17-1</span></a>. Geometry of a ballistic trajectory.

</div>

</div>

Of interest here is the determination of the range
<span class="i">Rφ,</span> the height <span class="i">H</span>, and the
time <span class="i">t</span><sub><span class="i">b</span></sub> as
function of the initial conditions which are
<span class="i">r</span><sub><span class="i">0</span></sub> =
<span class="i">R</span>,
<span class="i">υ</span><sub><span class="i">0</span></sub>, and
<span class="i">β</span><sub>0</sub>. We have at our disposal Eqs. 4.9–7
and 4.9–8 as developed in the initial–value problem of Sec. 4.9. The
eccentricity is determined from the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0412.jpg](images/e9780486140520_i0412.jpg)

</div>

<div class="caption">

(4.17–1)

</div>

</div>

<div class="illustype_fullpage_image_text">

<div class="fullpage_image_text">

![e9780486140520_i0413.jpg](images/e9780486140520_i0413.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_49"
id="e9780486140520_c04.html_int_49" class="label_int"><span
class="b">Fig. 4.17-2</span></a>. Plot of Eq. 4.17–2 for the ballistic
trajectory. (<span class="i">φ</span> versus
<span class="i">β</span><sub>0</sub> with
<span class="i">Rυ</span><sup><span class="i">2</span></sup><span class="i">/K</span>
as parameter.

</div>

</div>

Since <span class="i">φ</span>/2 =
180°–θ<sub>0</sub><span class="i">,</span> tan
<span class="i">θ</span><sub>0</sub> =–tan (<span class="i">φ</span>/2),
and Eq. 4.9–7 can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0414.jpg](images/e9780486140520_i0414.jpg)

</div>

<div class="caption">

(4.17–2)

</div>

</div>

<a href="#e9780486140520_c04.html#int_49"
id="e9780486140520_c04.html_ref_int_49" class="ref_int">Figure
4.17-2</a> is a plot of <span class="i">φ</span> versus
<span class="i">β</span><sub>0</sub> with
<span class="i">Rυ</span><sub><span class="i">0</span></sub><sup><span class="i">2</span></sup>/<span class="i">K
as</span> parameter. The height <span class="i">H</span> can be
determined from its geometry.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0415.jpg](images/e9780486140520_i0415.jpg)

</div>

<div class="caption">

(4.17–3)

</div>

</div>

From the equation of the ellipse, we have for
<span class="i">θ</span><sub>0</sub> = 180° −
<span class="i">φ</span>/2,
<span class="i">r</span><sub><span class="i">0</span></sub> =
<span class="i">R.</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0416.jpg](images/e9780486140520_i0416.jpg)

</div>

<div class="caption">

(4.17–4)

</div>

</div>

which, substituted into Eq. 4.17–3, results in

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0417.jpg](images/e9780486140520_i0417.jpg)

</div>

<div class="caption">

(4.17–5)

</div>

</div>

The time of flight is determined by subtracting the time required to go
from perigee to <span class="i">θ</span> =
<span class="i">θ</span><sub>0</sub> from half the orbit period and
doubling this figure, which from Eq. 4.13–12 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0418.jpg](images/e9780486140520_i0418.jpg)

</div>

<div class="caption">

(4.17–6)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  For
    <span class="i">Rυ</span><sub><span class="i">0</span></sub><sup><span class="i">2</span></sup><span class="i">/K</span>
    \> 1, show that the launching point corresponds to perigee if
    <span class="i">β</span><sub><span class="i">0</span></sub> = 0.
2.  For a given initial velocity
    <span class="i"><span class="b">Rυ</span></span><sub><span class="i"><span class="b">0</span></span></sub><sup><span class="i"><span class="b">2</span></span></sup><span class="i"><span class="b">/K</span></span>
    \< 1, determine the angle <span class="i">β</span><sub>0</sub> for
    maximum range.
3.  Relate the maximum range to the optimum heading angle
    <span class="i">β</span><sub>0</sub> and specified velocity
    <span class="i">Rυ</span><sub><span class="i">0</span></sub><sup><span class="i">2</span></sup><span class="i">/K.</span>
4.  For a given range show that the minimum required velocity is related
    to <span class="i">β</span><sub>0</sub> by the equation
    (<span class="i">Rυ</span><sup><span class="i">2</span></sup><span class="i">/K)</span><sub><span class="i">min</span></sub>
    =
    <span class="imageinline">![e9780486140520_i0419.jpg](images/e9780486140520_i0419.jpg)</span>
    .
5.  For a range of 5000 miles, determine the optimum angle
    <span class="i">β</span><sub>0</sub> the height
    <span class="i">H</span>, and the velocity
    <span class="i">Rυ</span><sub><span class="i">0</span></sub><sup><span class="i">2</span></sup><span class="i">/K.</span>
6.  For Prob. 5, determine the time of flight.
7.  Discuss the effect of the earth’s rotation on the motion of the
    ballistic missile.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0420.jpg](images/e9780486140520_i0420.jpg)

</div>

<div class="caption">

<span class="b">Prob. 6</span>

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title53"></span>

# <span class="b">4.18 Effect of the Earth’s Oblateness</span>

Due to the rotation of the earth from west to east, there is a speed
advantage in launching a satellite in a direction with an easterly
component. Such an orbit will precess in a westerly direction due to the
earth’s equatorial bulge, and thus a closed orbit is really not
possible. The revolving satellite is like a gyroscope and, as shown in
<a href="#e9780486140520_c04.html#int_50"
id="e9780486140520_c04.html_ref_int_50" class="ref_int">Fig. 4.18-1</a>,
its angular momentum vector
<span class="b">h</span><sub><span class="i">s</span></sub>,
perpendicular to its orbit plane and directed towards the northern
hemisphere, must slowly revolve about the north polar axis due to the
moment exerted by the excess mass over the sphere near the equator. The
rate of precession will depend on the orbit angle with respect to the
equator and, to a somewhat smaller extent, on the altitude.

The moment due to the equatorial bulge responsible for the precession of
the satellite orbit can be determined as follows:

Referring to <a href="#e9780486140520_c04.html#int_51"
id="e9780486140520_c04.html_ref_int_51" class="ref_int">Fig. 4.18-2</a>
the satellite <span class="i">m</span><sub>s</sub> is attracted towards
the mass element <span class="i">dm</span> of the earth according to the
equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0421.jpg](images/e9780486140520_i0421.jpg)

</div>

<div class="caption">

(4.18–1)

</div>

</div>

where <span class="i">K</span> = <span class="i">Gm</span> and
<span class="i">m</span> is the mass of the earth.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0422.jpg](images/e9780486140520_i0422.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_50"
id="e9780486140520_c04.html_int_50" class="label_int"><span
class="b">Fig. 4.18-1</span></a>. Precession of orbit plane due to
earth’s oblateness.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0423.jpg](images/e9780486140520_i0423.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_51"
id="e9780486140520_c04.html_int_51" class="label_int"><span
class="b">Fig. 4.18-2</span></a>. Satellite <span class="i">m</span>,
attracted by element <span class="i">dm</span> of earth.

</div>

</div>

Resolving <span class="b">r</span> into components, <span class="b">r =
a–ρ</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0424.jpg](images/e9780486140520_i0424.jpg)

</div>

<div class="caption">

(4.18—2)

</div>

</div>

where <span class="i">θ</span> is the angle between the orbit plane and
the equatorial plane and <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> are the components of
<span class="b">ρ</span>. The moment becomes,
<span class="i">d</span><span class="b"><span class="i">M</span></span>=
<span class="b">ρ</span> ×
<span class="i">d</span><span class="b">F</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0425.jpg](images/e9780486140520_i0425.jpg)

</div>

<div class="caption">

(4.18–3)

</div>

</div>

The quantity 1/<span class="i">r</span><sup>3</sup> can be obtained by
the following steps:

<div class="blocktext">

<span class="i">r</span><sup>2</sup> = (a–ρ) · (a–ρ) =
<span class="i">a</span><sup>2</sup> + ρ<sup>2</sup>–2ρ · a

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0426.jpg](images/e9780486140520_i0426.jpg)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0427.jpg](images/e9780486140520_i0427.jpg)

</div>

<div class="caption">

(4.18–4)

</div>

</div>

and its substitution into the moment equation leads to a complicated
expression for integration. The expression however can be simplified if
<span class="i">a</span> is much larger than
<span class="i">p</span>(<span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span>), in which case we
neglect the term
(<span class="i">p</span>/<span class="i">a</span>)<sup><span class="i">2</span></sup>
in 1/<span class="i">r</span><sup>3</sup>, expand the remaining terms by
the binomial theorem, and retain only the first terms. We then obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0428.jpg](images/e9780486140520_i0428.jpg)

</div>

<div class="caption">

(4.18–5)

</div>

</div>

and its substitution into the moment equation results in
<span class="i">M</span><sub><span class="i">x</span></sub>,
<span class="i">M</span><sub><span class="i">y</span></sub><span class="i">,</span>
and
<span class="i">M</span><sub><span class="i">z</span></sub><span class="i">.</span>
The <span class="i">x</span> component of the moment is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0429.jpg](images/e9780486140520_i0429.jpg)

</div>

<div class="caption">

(4.18–6)

</div>

</div>

where 6 and <span class="i">ϕ</span> are held constant during
integration. It is evident that the first integral is zero due to
symmetry of the oblate spheroid. Also all cross products of the form
<span class="i">xy, xz</span>, <span class="i">yz</span> will integrate
to zero due to symmetry. We are then left with the integral,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0430.jpg](images/e9780486140520_i0430.jpg)

</div>

<div class="caption">

(4.18–7)

</div>

</div>

where <span class="i">C and A</span> are the moments of inertia of the
earth about the polar and equatorial axes respectively.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0431.jpg](images/e9780486140520_i0431.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c04.html#ref_int_52"
id="e9780486140520_c04.html_int_52" class="label_int"><span
class="b">Fig. 4.18-3</span></a>. Precession of vector
<span class="b">h</span><sub><span class="b">s</span></sub> due to
moments <span class="i">M</span><sub><span class="i">x</span></sub> and
<span class="i">M</span><sub><span class="i">y</span></sub>.

</div>

</div>

Similarly, the moment about the <span class="i">y</span> axis is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0432.jpg](images/e9780486140520_i0432.jpg)

</div>

<div class="caption">

(4.18–8)

</div>

</div>

and the moment about the <span class="i">z</span> axis is zero.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0433.jpg](images/e9780486140520_i0433.jpg)

</div>

<div class="caption">

(4.18–9)

</div>

</div>

These equations indicate that the moment
<span class="i">M</span><sub><span class="i">y</span></sub> is negative
for 0 ≤ <span class="i">ϕ</span> ≤ π/2, and positive for
<span class="i">π</span>/2 ≤ <span class="i">ϕ</span> ≤
<span class="i">π</span>, the cycle repeating itself over
<span class="i">π</span> to 2<span class="i">π</span>. Thus the net
moment <span class="i">M</span><sub><span class="i">y</span></sub> over
a complete cycle is zero. The moment
<span class="i">M</span><sub><span class="i">x</span></sub><span class="i">,</span>
however, is always positive and varying as sin<sup>2</sup>
<span class="i">ϕ.</span>

<a href="#e9780486140520_c04.html#int_52"
id="e9780486140520_c04.html_ref_int_52" class="ref_int">Figure
4.18-3</a> shows the orbit plane, the satellite
<span class="i">m</span><sub><span class="i">s</span></sub>, and the
moments <span class="i">M</span><sub><span class="i">x</span></sub> and
<span class="i">M</span><sub><span class="i">y</span></sub> exerted by
the earth on the satellite. To determine the precession of the satellite
orbit plane, we note that the angular momentum of the satellite has the
value <span class="i">h</span><sub><span class="i">s</span></sub> =
<span class="imageinline">![e9780486140520_i0434.jpg](images/e9780486140520_i0434.jpg)</span>
, which is normal to the orbit plane. The action of the moment
<span class="i">M</span><sub><span class="i">y</span></sub> on
<span class="b">h</span><sub>s</sub> is oscillatory and zero over a
complete cycle, but
<span class="i">M</span><sub><span class="i">x</span></sub> requires the
rate of change of <span class="b">h</span><sub>s</sub> over the cycle to
be cumulative in the <span class="i">x</span> direction.

Measuring the regression of the node line <span class="i">ψ</span> in
the equatorial plane, the rate of precession
<span class="imageinline">![e9780486140520_i0435.jpg](images/e9780486140520_i0435.jpg)</span>
is directed along the −<span class="i">z</span> axis with components
<span class="i">y</span> sin <span class="i">θ</span> in the plane of
the orbit, and
<span class="imageinline">![e9780486140520_i0436.jpg](images/e9780486140520_i0436.jpg)</span>
cos <span class="i">θ</span> normal to it. The component
<span class="imageinline">![e9780486140520_i0437.jpg](images/e9780486140520_i0437.jpg)</span>
sin <span class="i">θ</span> rotates the vector
<span class="b">h</span><sub>s</sub> to give

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0438.jpg](images/e9780486140520_i0438.jpg)

</div>

<div class="caption">

(4.18—10)

</div>

</div>

from which the rate of precession of the orbit plane becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0439.jpg](images/e9780486140520_i0439.jpg)

</div>

</div>

Since the moment of inertia of a sphere of radius
<span class="i">R</span> is
<span class="imageinline">![e9780486140520_i0440.jpg](images/e9780486140520_i0440.jpg)</span>
, we can introduce <span class="i">C</span> =
<span class="imageinline">![e9780486140520_i0441.jpg](images/e9780486140520_i0441.jpg)</span>
, where <span class="i">R</span> is the mean radius of earth, and
rewrite
<span class="imageinline">![e9780486140520_i0442.jpg](images/e9780486140520_i0442.jpg)</span>
as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0443.jpg](images/e9780486140520_i0443.jpg)

</div>

<div class="caption">

(4.18–11)

</div>

</div>

Assuming a circular orbit, the angular rate around the orbit, is a
constant,
<span class="imageinline">![e9780486140520_i0444.jpg](images/e9780486140520_i0444.jpg)</span>
, where τ is the orbit period equal to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0445.jpg](images/e9780486140520_i0445.jpg)

</div>

</div>

Thus <span class="i">ϕ</span> can be replaced by
(2<span class="i">π</span>/<span class="i">τ</span>)<span class="i">t</span>,
and the precession angle measured in the equatorial plane per revolution
of the satellite becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0446.jpg](images/e9780486140520_i0446.jpg)

</div>

<div class="caption">

(4.18–12)

</div>

</div>

The quantity (<span class="i">C</span> −
<span class="i">A</span>)/<span class="i">C</span> for earth is 0.0032,
so that the node line of the orbit regresses westward by the amount

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0447.jpg](images/e9780486140520_i0447.jpg)

</div>

<div class="caption">

(4.18–13)

</div>

</div>

for each revolution of the satellite around the earth.

We can compare this equation with the equation given by
Blitzer,<sup>2</sup> which is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0448.jpg](images/e9780486140520_i0448.jpg)

</div>

</div>

Translated into our notation with <span class="i">J</span> = 1.637 x
10<sup>–3</sup> (see ref. 5) Blitzer’s equation is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0449.jpg](images/e9780486140520_i0449.jpg)

</div>

</div>

which indicates fair agreement for our approximate equation, Eq.
4.18–13.

The reverse problem to the above is the precession of the earth’s polar
axis due to the moment exerted by the satellite on the earth. When the
satellite is a sizeable mass, such as the moon, its influence is a
measurable quantity. The problem of the precession of the earth’s polar
axis due to the sun and the moon is taken up in Chap. 5, Sec. 15.

<span class="b">PROBLEMS</span>

1.  Examination of Eq. 4.18–7 indicates that no restriction as to the
    density variation of earth was imposed; however in letting
    <span class="imageinline">![e9780486140520_i0450.jpg](images/e9780486140520_i0450.jpg)</span>
    just before Eq. 4.18–11, uniform density is implied. Indicate what
    would be changed in Eq. 4.18–12 if the density of the earth varied
    with the distance from its center.
2.  If the term (<span class="i">p/a</span>)<sup>2</sup> in Eq. 4.18–4
    is retained to the first term of the binomial expansion, determine
    the correction to Eq. 4.18–5.
3.  For a satellite launched southeasterly in a circular orbit at an
    angle of 35° with the equator and at an altitude of 400 miles,
    determine the regression of the node per revolution taking into
    account the rotation of the earth during the period.
4.  Show that the attraction of a thin spherical shell of constant
    density is equal to that of a particle of the same mass concentrated
    at its center.
5.  Assuming that (<span class="i">C</span> −
    <span class="i">A</span>)/<span class="i">C</span> =
    <span class="i">N</span> differs from zero due to a narrow band
    around the equator of a perfect sphere, show that the mass of this
    narrow band must equal,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0451.jpg](images/e9780486140520_i0451.jpg)

    </div>

    </div>

    where <span class="i">m</span><sub><span class="i">0</span></sub> is
    the total mass of the sphere plus the narrow band.

</div>

<div class="section1">

<span id="e9780486140520_c04.html_title54"></span>

# <span class="b">REFERENCES</span>

1.  Augenstein, B. W., “Dynamics Problems Associated with Satellite
    Orbit Control,” <span class="i">Trans. ASME,</span> Series B (Nov.
    1959), 281–288.
2.  Blitzer, L., M. Weisfield, and D. Wheelon, “Perturbation of a
    Satellite Orbit Due to the Earth’s Oblateness,” <span class="i">J.
    Appl. Physics</span> 27, No. 10 (Oct. 1956), 1141—1149.
3.  Ehricke, Krafft A., “Interplanetary Operations,”
    <span class="i">Space Technology,</span> John Wiley and Sons, New
    York (1959), Chapter 8.
4.  Ehricke, Krafft A., <span class="i">Space Flight,</span> Vol. 1, D.
    van Nostrand, Princeton, N.J. (1960).
5.  King–Hele, D. G., and D. M. C. Walker, “Methods for Predicting the
    Orbits of Near Earth–Satellites,” <span class="i">J. British
    Interplanetary Soc.,</span> 17, No. 1 (Jan.–Feb. 1959), 2—14.
6.  Moulton, F. R., <span class="i">Celestial Mechanics,</span>
    Macmillan Co., New York (1914).
7.  Ramsey, A. S., <span class="i">Dynamics</span>—<span class="i">Part
    II,</span> Cambridge University Press, New York (1956), Chapter 1.

</div>

</div>

<span id="e9780486140520_c05.html"></span>

<div class="chapter">

<span id="e9780486140520_c05.html_title55"></span>

# <span class="b">CHAPTER 5</span>

# <span class="b">Gyrodynamics</span>

<div class="section1">

<span id="e9780486140520_c05.html_title56"></span>

# <span class="b">5.1 Displacement of a Rigid Body</span>

A rigid body can be viewed as a system of particles where the relative
distances between particles are fixed. The position of a rigid body is
defined by any three points on it, not in the same straight line.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0452.jpg](images/e9780486140520_i0452.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_53"
id="e9780486140520_c05.html_int_53" class="label_int"><span
class="b">Fig. 5.1-1</span></a>. Displacement of a rigid body.

</div>

</div>

The motion of a rigid body can be described by a translation of some
reference point 0, plus a rotation about some axis through 0. Consider
three arbitrary noncolinear points 1, 2, 3, in the initial and final
positions 1’, 2’, 3’, as shown in
<a href="#e9780486140520_c05.html#int_53"
id="e9780486140520_c05.html_ref_int_53" class="ref_int">Fig. 5.1-1</a>.
The first point 1 can be brought to 1’ by a translation so that the new
position is 1’, 2”, 3”. Next, rotate about an axis through 1’ which is
perpendicular to the plane 1’, 2”, 2’, bringing 2” to coincide with 2’.
Finally, rotate about an axis through 1’ and 2’, to bring 3‴ to 3′.

We will now show Euler’s proof that the two individual rotations can be
replaced by a single rotation. Draw a unit sphere about point 1’ and
where the two rotation axes pierce it, connect the points by a great
circle as shown in <a href="#e9780486140520_c05.html#int_54"
id="e9780486140520_c05.html_ref_int_54" class="ref_int">Fig. 5.1-2</a>.
Measure off ½θ<sub>1</sub> on each side of the great circle at axis 1,
drawing two other great circles, and do likewise with angle
<span class="i">θ</span><sub>2</sub> at axis 2. Now a rotation of
<span class="i">θ</span><sub>1</sub> about axis 1 will bring point
<span class="i">a</span> to <span class="i">b,</span> and a rotation
<span class="i">θ</span><sub>2</sub> about axis 2 will bring
<span class="i">b</span> back to <span class="i">a</span>. Thus
1’<span class="i">a</span> is an undisturbed line during rotation
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub>, and therefore it must be the
resultant axis of rotation. Note that 1’<span class="i">a</span> is not
in the plane containing the axes of rotation
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub>, which again points out the fact
that finite rotations do not possess the properties of vectors.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0453.jpg](images/e9780486140520_i0453.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_54"
id="e9780486140520_c05.html_int_54" class="label_int"><span
class="b">Fig. 5.1-2</span></a><span class="b">.</span> Resultant
rotation axis by Euler’s proof.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title57"></span>

# <span class="b">5.2 Moment of Momentum of a Rigid Body (About a Fixed Point or the Moving Center of Mass)</span>

Let body axes <span class="i">x, y, z</span> be attached to the body
with the origin <span class="i">O</span> at any point. The velocity of
any point <span class="i">i</span> on the body is then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0454.jpg](images/e9780486140520_i0454.jpg)

</div>

<div class="caption">

(5.2–1)

</div>

</div>

where <span class="b">ω</span> is the angular velocity of the body.

The moment of momentum about the origin <span class="i">O</span> of the
<span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span>, system is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0455.jpg](images/e9780486140520_i0455.jpg)

</div>

<div class="caption">

(5.2–2)

</div>

</div>

If the reference point <span class="i">O</span> is stationary,
<span class="b">v</span><sub>0</sub> = 0, whereas if
<span class="i">O</span> coincides with the center of mass,
Σ<sub>i</sub><span class="i">m</span><sub>i</sub><span class="b">r</span><sub>i</sub>
= 0. Thus, if <span class="i">O</span> is fixed, or a center of mass,
the angular momentum is given by the first term of the above equation,
which can be expressed by the following integral,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0456.jpg](images/e9780486140520_i0456.jpg)

</div>

<div class="caption">

(5.2–3)

</div>

</div>

To evaluate this integral, we note that the first cross product ω
<span class="b">× r</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0457.jpg](images/e9780486140520_i0457.jpg)

</div>

<div class="caption">

(5.2–4)

</div>

</div>

Multiplying by <span class="i">dm</span>, we have the <span class="i">x,
y, z,</span> components of the momentum of <span class="i">dm</span>, as
shown in <a href="#e9780486140520_c05.html#int_55"
id="e9780486140520_c05.html_ref_int_55" class="ref_int">Fig. 5.2-1</a>.

The cross product r × (ω × r) <span class="i">dm</span> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0458.jpg](images/e9780486140520_i0458.jpg)

</div>

<div class="caption">

(5.2–5)

</div>

</div>

which represent the moment about the <span class="i">x, y, z,</span>
axes of the momentum vectors shown in
<a href="#e9780486140520_c05.html#int_55" class="ref_int">Fig. 5.2-1</a>.
Integrating over the body, we arrive at the <span class="i">x, y,
z,</span> components of the moment of momentum of the body.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0459.jpg](images/e9780486140520_i0459.jpg)

</div>

<div class="caption">

(5.2–6)

</div>

</div>

We now define the moment of inertia of the body about the
<span class="i">x, y, z,</span> axes as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0460.jpg](images/e9780486140520_i0460.jpg)

</div>

</div>

and the products of inertia as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0461.jpg](images/e9780486140520_i0461.jpg)

</div>

</div>

in which case the moment of momentum components along the
<span class="i">x, y, z,</span> axes become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0462.jpg](images/e9780486140520_i0462.jpg)

</div>

<div class="caption">

(5.2–7)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0463.jpg](images/e9780486140520_i0463.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_55"
id="e9780486140520_c05.html_int_55" class="label_int"><span
class="b">Fig. 5.2-1</span></a>. Components of momentum (ω × r)
<span class="i">dm</span>.

</div>

</div>

The moments and products of inertia can be concisely presented by an
inertia dyadic as
follows:<sup><a href="#e9780486140520_ftn01.html#ftn_fn5"
id="e9780486140520_c05.html_ref_ftn_fn5">e</a></sup>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0464.jpg](images/e9780486140520_i0464.jpg)

</div>

<div class="caption">

(5.2–8)

</div>

</div>

If we form the dot product of the inertia dyadic with the angular
velocity vector

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0465.jpg](images/e9780486140520_i0465.jpg)

</div>

</div>

we would obtain the moment of momentum

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0466.jpg](images/e9780486140520_i0466.jpg)

</div>

<div class="caption">

(5.2–9)

</div>

</div>

The order of the dot product must be preserved with the following
interpretation,

<div class="blocktext">

<span class="b">ij · i</span> =
<span class="b">i</span>(<span class="b">j · i</span>) =
<span class="b">0</span>  
<span class="b">ji · i</span> =
<span class="b">j</span>(<span class="b">i · i</span>) =
<span class="b">j</span>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title58"></span>

# <span class="b">5.3 Kinetic Energy of a Rigid Body</span>

Consider a rigid body moving through space, and attach to it a set of
body axes <span class="i">x, y, z,</span> with its origin coinciding
with its center of mass. Then any point <span class="b">r</span> will
have a velocity equal to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0467.jpg](images/e9780486140520_i0467.jpg)

</div>

<div class="caption">

(5.3–1)

</div>

</div>

The square of the velocity is obtained by the dot product of its vector,

<div class="blocktext">

υ<sup>2</sup> = v · v = υ<sub>0</sub><sup>2</sup> + (ω × r) · (ω × r) +
2v<sub>0</sub> · (ω × r)

</div>

Thus, the kinetic energy of the body is given as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0468.jpg](images/e9780486140520_i0468.jpg)

</div>

<div class="caption">

(5.3–2)

</div>

</div>

where ∫ r <span class="i">dm</span> = 0 for the origin of the body axes
coinciding with the center of mass. We have thus found that the kinetic
energy of translation is determined as if the entire mass is
concentrated at the center of mass as a particle, and the second term is
the kinetic energy of rotation about an axis <span class="b">ω</span>
through the center of mass.

Focusing our attention to the kinetic energy of rotation, we examine the
quantity (ω <span class="b">×</span> r) · (ω <span class="b">×</span>
r). Resolving ω <span class="b">×</span> r into components along the
body axes, the dot product is given by the square of the
<span class="b">i</span>, <span class="b">j</span>,
<span class="b">k</span> components.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0469.jpg](images/e9780486140520_i0469.jpg)

</div>

</div>

Thus

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0470.jpg](images/e9780486140520_i0470.jpg)

</div>

<div class="caption">

(5.3–3)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title59"></span>

# <span class="b">5.4 Moment of Inertia about a Rotated Axis</span>

If <span class="i">I</span><sub>ξξ</sub> is the moment of inertia of a
body about any axis ξ, with angular velocity <span class="b">ω</span>,
we can write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0471.jpg](images/e9780486140520_i0471.jpg)

</div>

<div class="caption">

(5.4–1)

</div>

</div>

Substituting Eq. 5.3–3 into the above equation, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0472.jpg](images/e9780486140520_i0472.jpg)

</div>

<div class="caption">

(5.4–2)

</div>

</div>

By letting
<span class="i">I</span><sub><span class="i">ξx</span></sub><span class="i">,
I</span><sub><span class="i">ξy</span></sub><span class="i">,
I</span><sub><span class="i">ξz</span></sub> be direction cosines of the
vector <span class="b">ω</span> or axis ξ with respect to the
<span class="i">x, y, z</span> axes, the above equation can be written
as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0473.jpg](images/e9780486140520_i0473.jpg)

</div>

<div class="caption">

(5.4–3)

</div>

</div>

Equation 5.4–3 can be concisely written in terms of a double summation
as follows

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0474.jpg](images/e9780486140520_i0474.jpg)

</div>

<div class="caption">

(5.4—4)

</div>

</div>

where α and <span class="i">β</span> take on the letters
<span class="i">x, y, z</span> with
<span class="i">I</span><sub><span class="i">αα</span></sub> interpreted
as <span class="i">I</span><sub><span class="i">xx</span></sub> =
<span class="i">I</span><sub><span class="i">x</span></sub><span class="i">,
I</span><sub><span class="i">yy</span></sub><span class="i">,</span>
etc., and <span class="i">I</span><sub><span class="i">αβ</span></sub>
as
<span class="i">–I</span><sub><span class="i">xy</span></sub>,–<span class="i">I</span><sub>yz</sub>,
<span class="i">–I</span><sub>xz</sub>. In fact Eq. 5.4–4 can be changed
slightly to apply to products of inertia as well by the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0475.jpg](images/e9780486140520_i0475.jpg)

</div>

<div class="caption">

(5.4–5)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0476.jpg](images/e9780486140520_i0476.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_56"
id="e9780486140520_c05.html_int_56" class="label_int"><span
class="b">Fig. 5.4-1</span></a>. Components of r in two coordinate
systems.

</div>

</div>

The direction cosines
<span class="i">I</span><sub><span class="i">ξα</span></sub> to be used
in Eq. 5.4–4 or 5.4–5 can be formed most conveniently from the
transformation matrix between the two coordinate systems. If the two
coordinate systems are <span class="i">x, y, z</span> and
<span class="i">x′, y′, z′</span> with unit vectors
<span class="b">i</span>, <span class="b">j</span>,
<span class="b">k</span> and <span class="b">i′</span>,
<span class="b">j′</span>, <span class="b">k′</span>, a point in space
can be expressed in terms of either coordinate system as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0477.jpg](images/e9780486140520_i0477.jpg)

</div>

<div class="caption">

(5.4–6)

</div>

</div>

as shown in <a href="#e9780486140520_c05.html#int_56"
id="e9780486140520_c05.html_ref_int_56" class="ref_int">Fig. 5.4-1</a>.

Scalar multiplication of Eq. 5.4–6 by <span class="b">i</span>,
<span class="b">j</span>, and <span class="b">k</span> results in

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0478.jpg](images/e9780486140520_i0478.jpg)

</div>

<div class="caption">

(5.4–7)

</div>

</div>

which, in matrix notation, is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0479.jpg](images/e9780486140520_i0479.jpg)

</div>

<div class="caption">

(5.4–8)

</div>

</div>

Thus when the transfer matrix between the two coordinates is known, the
elements of the matrix are the direction cosines.

We note further that the equation for the kinetic energy can be
expressed by the dot product of the angular velocity and the moment of
momentum,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0480.jpg](images/e9780486140520_i0480.jpg)

</div>

<div class="caption">

(5.4—9)

</div>

</div>

Since h<sub>0</sub> can be expressed in terms of the momental dyadic
(see Eq. 5.2–9), the above equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0481.jpg](images/e9780486140520_i0481.jpg)

</div>

<div class="caption">

(5.4–10)

</div>

</div>

Again letting
<span class="imageinline">![e9780486140520_i0482.jpg](images/e9780486140520_i0482.jpg)</span>
, the above double dot product is interpreted as

<div class="blocktext">

(ω ∙·A)(B ∙ ω)

</div>

which is a product of two scalars and, therefore, a pure number.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title60"></span>

# <span class="b">5.5 Principal Axes</span>

We define the principal axes of the body, 1, 2, 3, as those about which
the products of inertia vanish, and let <span class="i">A</span>,
<span class="i">B</span>, <span class="i">C</span>, be the moment of
inertia about the 1, 2, 3 axes respectively. The moment of inertia about
the instantaneous axes of rotation <span class="i">ξ</span>, in terms of
<span class="i">A</span>, <span class="i">B</span>,
<span class="i">C</span> then becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0483.jpg](images/e9780486140520_i0483.jpg)

</div>

<div class="caption">

(5.5—1)

</div>

</div>

where <span class="i">l</span><sub><span class="i">ξ1</span></sub>,
<span class="i">l</span><sub><span class="i">ξ</span>2</sub>,
<span class="i">l</span><sub><span class="i">ξ3</span></sub> are the
direction cosines of the vector ω, or axis ξ and the principal axes 1,
2, 3. Since the axes 1, 2, 3 are fixed in the body, <span class="i">A,
B</span>, <span class="i">C</span> are constants. However, as the
instantaneous axis ξ is moved,
<span class="i">l</span><sub><span class="i">ξ</span>1</sub>,
<span class="i">l</span><sub><span class="i">ξ</span>2</sub>,
<span class="i">l</span><sub><span class="i">ξ</span>3</sub> change, and
so will the value of <span class="i">I</span> about the ξ axis.

If we let
<span class="imageinline">![e9780486140520_i0484.jpg](images/e9780486140520_i0484.jpg)</span>
, and lay off <span class="i">p</span> and <span class="i">ξ</span>, and
do this for every orientation of the instantaneous axis
<span class="i">ξ</span>, we would obtain an ellipsoid of inertia.

Dividing the above equation by
<span class="i">I</span><sub><span class="i">ξ</span></sub> and noting
that
<span class="imageinline">![e9780486140520_i0485.jpg](images/e9780486140520_i0485.jpg)</span>,
<span class="i">l</span><sub><span class="i">ξ2</span></sub><span class="i">ρ</span>
= <span class="i">y</span>,
<span class="i">l</span><sub><span class="i">ξ3</span></sub>ρ = z are
the principal coordinates of the equation for the ellipsoid of inertia,
Eq. 5.5–1 becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0486.jpg](images/e9780486140520_i0486.jpg)

</div>

<div class="caption">

(5.5—2)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  . For the slender uniform bar of length <span class="i">l</span> and
    mass <span class="i">m</span> oriented in the position shown,
    determine the moment and product of inertia about each of the axes.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0487.jpg](images/e9780486140520_i0487.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 1</span>

    </div>

    </div>
2.  If the bar of Prob. 1 is rotated about the <span class="i">z</span>
    axis with angular velocity ω, determine the angular momentum about
    the three axes.
3.  While getting into position for takeoff, a small aeroplane with two
    bladed propellers turns about its vertical axis as shown. Determine
    the <span class="i">x, y, z</span> components of the angular
    momentum of the left propeller. Assume the propeller to be a uniform
    slender rod of length <span class="i">l</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0488.jpg](images/e9780486140520_i0488.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 3</span>

    </div>

    </div>
4.  Find the moments of inertia of six 10-1b weights arranged
    symmetrically on the <span class="i">x, y, z</span> axes as follows:
    <span class="i">x</span> = ±5, <span class="i">y</span> = ±2,
    <span class="i">z</span> = ±6.
5.  Find the moment of inertia of the configuration of Prob. 4 about an
    axis through the origin and the point (1, 2, 2).
6.  A thin disk of radius <span class="i">R</span> is mounted on a shaft
    which deviates by an angle α from the normal. Choose orthogonal axes
    through the shaft and disk and determine the moment and product of
    inertia about each axis.
7.  Determine the moment of inertia about the <span class="i">ξ, η,
    ζ</span> axes for a cube of sides <span class="i">c</span>, if ζ is
    placed along the diagonal and the <span class="i">ξ,</span> η axes
    normal to ζ are rotated into a position such that
    <span class="i">I</span><sub><span class="i">ξ</span></sub> =
    <span class="i">I</span><sub><span class="i">η</span></sub><span class="i">.</span>
    What will be the direction cosines of ξ and <span class="i">η</span>
    so placed?
8.  Determine the length of a uniform cylinder of radius
    <span class="i">R</span> such that its principal moments of inertia
    are equal.
9.  If <span class="i">A,</span> <span class="i">B, C</span> are
    principal moments of inertia of a given body, show that
    <span class="i">A</span> + <span class="i">B</span> is larger than
    <span class="i">C</span>.
10. A space vehicle makes a landing on a hillside with velocities
    υ<sub><span class="i">z</span></sub> and
    υ<sub><span class="i">x</span></sub> just before impact as shown. If
    a leg strikes a boulder and the vehicle pivots about this point,
    show that the angular velocities immediately after impact are
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0489.jpg](images/e9780486140520_i0489.jpg)

    </div>

    </div>

    where the <span class="i">x, y, z</span> coordinates are oriented
    with <span class="i">z</span> vertical, <span class="i">x</span>
    parallel to the horizontal velocity υ<sub>x</sub>, and
    <span class="i">y</span> horizontal.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0490.jpg](images/e9780486140520_i0490.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 10</span>

    </div>

    </div>
11. . Assume that the moments and products of inertia about the
    <span class="i">x, y, z</span> axes are known. Determine the
    equation for the moment of inertia about the ξ, η, ζ axes by noting
    that <span class="i">ρξ</span><sup><span class="i">2</span></sup> =
    <span class="i">ρ</span><sup><span class="i">2</span></sup>–ξ<sup>2</sup>
    = <span class="i">ρ</span><sup><span class="i">2</span></sup>
    <span class="i">–</span> (ρ ·
    <span class="b">i</span>′)<sup>2</sup>, ρ =
    x<span class="b">i</span> + y<span class="b">j</span> +
    z<span class="b">k</span>, and
    <span class="i">I</span><sub><span class="i">ξξ</span></sub> = ∫
    ρξ<sup>2</sup> <span class="i">dm</span>, etc.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0491.jpg](images/e9780486140520_i0491.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 11</span>

    </div>

    </div>
12. In the same manner as in Prob. 11, determine the equation for the
    product of inertia <span class="i">I</span><sub>ξη</sub>,
    <span class="i">I</span><sub>ξζ</sub>, and
    <span class="i">I</span><sub>ηζ</sub>.
13. An airplane of mass <span class="i">M</span> and moments of inertia
    <span class="i">A</span>, <span class="i">B</span>,
    <span class="i">C</span> about principal axes drops at a uniform
    rate of <span class="i">V</span> ft/sec, and at the same time spins
    at the rate of 10 rpm about an axis which makes equal angles with
    the three principal axes. Determine its total kinetic energy.
14. Show that the moment of inertia of three equal masses 120° apart as
    shown in the sketch is equal to
    <span class="imageinline">![e9780486140520_i0492.jpg](images/e9780486140520_i0492.jpg)</span>
    about any axis in its plane.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0493.jpg](images/e9780486140520_i0493.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 14</span>

    </div>

    </div>
15. With the <span class="i">x, y, z</span> axes passing through the
    center of mass of a body shown in the sketch, prove that the moment
    of inertia about any axis <span class="i">n</span> through the
    origin is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0494.jpg](images/e9780486140520_i0494.jpg)

    </div>

    </div>

    where <span class="b">n</span> =
    <span class="i">n</span><sub>x</sub><span class="b">i</span> +
    <span class="i">n</span><sub>y</sub><span class="b">j</span> +
    <span class="i">n</span><sub>z</sub><span class="b">k</span> is a
    unit vector along the axis <span class="b">n</span>.
    <span class="i">Hint</span>: Start with
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0495.jpg](images/e9780486140520_i0495.jpg)

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0496.jpg](images/e9780486140520_i0496.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 15</span>

    </div>

    </div>
16. Starting with
    <span class="imageinline">![e9780486140520_i0497.jpg](images/e9780486140520_i0497.jpg)</span>
    , derive the equation for the moment of inertia about an axis
    <span class="i">n’</span> parallel to <span class="i">n</span>, and
    displaced by the vector <span class="b">r</span><sub>0</sub>.
17. By actually multiplying, using the rule <span class="b">ij</span> ·
    <span class="b">i</span> = 0, <span class="b">ij</span> ·
    <span class="b">j</span> = <span class="b">i</span>, etc., show that
    <span class="imageinline">![e9780486140520_i0498.jpg](images/e9780486140520_i0498.jpg)</span>.
18. Show that
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0499.jpg](images/e9780486140520_i0499.jpg)

    </div>

    </div>

    where
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0500.jpg](images/e9780486140520_i0500.jpg)

    </div>

    </div>
19. Determine the total time derivative
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0501.jpg](images/e9780486140520_i0501.jpg)

    </div>

    </div>

    with respect to inertial coordinates, and show that it is equal to
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0502.jpg](images/e9780486140520_i0502.jpg)

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title61"></span>

# <span class="b">5.6 Euler’s Moment Equation</span>

We have shown previously that the moment about the mass center is equal
to the time derivative of the moment of momentum about this point. With
<span class="b">h</span><sub>c</sub> =
<span class="i">h</span><sub>x</sub><span class="b">i</span> +
<span class="i">h</span><sub>y</sub><span class="b">j</span> +
<span class="i">h</span><sub>z</sub><span class="b">k</span>, we can
differentiate, noting that <span class="b">i</span>,
<span class="b">j</span>, <span class="b">k</span> rotate with the body.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0503.jpg](images/e9780486140520_i0503.jpg)

</div>

<div class="caption">

(5.6–1)

</div>

</div>

The cross product <span class="b">ω ×</span>
<span class="b">h</span><sub>c</sub> can easily be visualized as the
rotation of the vectors
<span class="i">h</span><sub><span class="i">x</span></sub><span class="b">i</span>,
<span class="i">h</span><sub>y</sub><span class="b">j</span>,
<span class="i">h</span><sub><span class="i">z</span></sub><span class="b">k</span>,
due to <span class="i">ω</span><sub>x</sub>,
<span class="i">ω</span><sub><span class="i">y</span></sub>,
<span class="i">ω</span><sub><span class="i">z</span></sub>, as shown in
<a href="#e9780486140520_c05.html#int_57"
id="e9780486140520_c05.html_ref_int_57" class="ref_int">Fig. 5.6-1</a>.
Thus, by adding vectors along the <span class="i">x, y, z</span>
directions, the above equation becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0504.jpg](images/e9780486140520_i0504.jpg)

</div>

<div class="caption">

(5.6–2)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0505.jpg](images/e9780486140520_i0505.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_57"
id="e9780486140520_c05.html_int_57" class="label_int"><span
class="b">Fig. 5.6-1</span></a>. Components of moment of momentum and
their rate of change.

</div>

</div>

The component equations, known as Euler’s moment equations, are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0506.jpg](images/e9780486140520_i0506.jpg)

</div>

<div class="caption">

(5.6–3)

</div>

</div>

where the <span class="i">x, y, z</span> axes with the origin coinciding
with the center of mass rotate with angular velocity
<span class="b">ω</span>.

Equation 5.6–1 or 5.6–3 for the moment is applicable to any coordinate
system with a fixed origin or a moving origin coinciding with the center
of mass. The angular velocity ω is that of the coordinate system and, if
the axes are fixed in the body, the moments and products of inertia are
constant.

For a body of revolution with moments of inertia <span class="i">A, A,
C</span> about principal axes, <span class="i">A</span> about any
transverse axis is the same, and so we might choose a set of transverse
axes rotating at a speed different from that of the body without
introducing a variable moment of inertia with time. We can for instance
use the node axis system <span class="i">ξ, η, ζ,</span> in which case
the moments are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0507.jpg](images/e9780486140520_i0507.jpg)

</div>

<div class="caption">

(5.6–4)

</div>

</div>

These equations are known as Euler’s modified equations.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title62"></span>

# <span class="b">5.7 Euler’s Equation for Principal Axes</span>

With the origin of the body axes coinciding with the center of mass, we
can orient the <span class="i">x, y, z</span> axes to coincide with the
principal axes 1, 2, 3 of the body to eliminate the products of inertia
terms in the moment of momentum expressions. We then have,

<div class="blocktext">

<span class="i">h</span><sub>1</sub> =
<span class="i">Aω</span><sub>1</sub>
<span class="i">h</span><sub>2</sub> =
<span class="i">Bω</span><sub>2</sub>
<span class="i">h</span><sub>3</sub> =
<span class="i">Cω</span><sub>3</sub>

</div>

<span class="i">h</span><sub>1</sub> =
<span class="i">Aω</span><sub>1</sub>
<span class="i">h</span><sub>2</sub> =
<span class="i">Bω</span><sub>2</sub>
<span class="i">h</span><sub>3</sub> =
<span class="i">Cω</span><sub>3</sub> where <span class="i">A, B,
C,</span> are principal moments of inertia which are constant since 1,
2, 3 are fixed in the body. The moment equations are then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0508.jpg](images/e9780486140520_i0508.jpg)

</div>

</div>

which are called the Euler’s equations for principal axes. The general
solution of these equations is difficult, and in the sections to follow
we will consider some special cases which enable an analytical solution.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title63"></span>

# <span class="b">5.8 Body with <span class="i">A = B</span> and Zero External Moment (Body Coordinates)</span>

We will consider here a cylindrical disk with axis 3 normal to the
circular face, as shown in <a href="#e9780486140520_c05.html#int_58"
id="e9780486140520_c05.html_ref_int_58" class="ref_int">Fig. 5.8-1</a>.
The moment of inertia about the three body axes are,

<div class="blocktext">

<span class="i">B</span> = <span class="i">A</span> about 1 and 2  
and <span class="i">C</span> about 3

</div>

Euler’s equation then becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0509.jpg](images/e9780486140520_i0509.jpg)

</div>

<div class="caption">

(5.8–1)

</div>

</div>

From the third of these equations, we conclude that ω<sub>3</sub> must
be a constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0510.jpg](images/e9780486140520_i0510.jpg)

</div>

<div class="caption">

(5.8–2)

</div>

</div>

Making the substitution,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0511.jpg](images/e9780486140520_i0511.jpg)

</div>

<div class="caption">

(5.8–3)

</div>

</div>

the first two equations can be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0512.jpg](images/e9780486140520_i0512.jpg)

</div>

<div class="caption">

(5.8–4)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0513.jpg](images/e9780486140520_i0513.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_58"
id="e9780486140520_c05.html_int_58" class="label_int"><span
class="b">Fig. 5.8-1</span></a>. Body of revolution with principal axes
1, 2, 3.

</div>

</div>

Multiplying the first equation by ω<sub>1</sub> and the second by
ω<sub>2</sub>, and adding, we obtain the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0514.jpg](images/e9780486140520_i0514.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0515.jpg](images/e9780486140520_i0515.jpg)

</div>

<div class="caption">

(5.8–5)

</div>

</div>

Thus the magnitude of the resultant angular velocity vector ω is a
constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0516.jpg](images/e9780486140520_i0516.jpg)

</div>

<div class="caption">

(5.8–6)

</div>

</div>

Since there is no moment acting on the body, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0517.jpg](images/e9780486140520_i0517.jpg)

</div>

<div class="caption">

(5.8–7)

</div>

</div>

which requires that the angular momentum vector h be a constant, fixed
in space. It is evident that <span class="b">h</span> must lie in the
plane containing axis 3 and <span class="b">ω</span>, since the
component of <span class="b">h</span> in the 1, 2–plane is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0518.jpg](images/e9780486140520_i0518.jpg)

</div>

<div class="caption">

(5.8—8)

</div>

</div>

which has the same direction as the component of
<span class="b">ω</span> in the 1, 2–plane. Thus, the plane containing
axis 3 and the <span class="b">ω</span> vector rotates about the fixed
<span class="b">h</span> vector, as shown in
<a href="#e9780486140520_c05.html#int_59"
id="e9780486140520_c05.html_ref_int_59" class="ref_int">Fig. 5.8-2</a>.
The motion can be visualized by the rolling of the body cone on the
space cone, which is fixed in space by the vector
<span class="b">h.</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0519.jpg](images/e9780486140520_i0519.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_59"
id="e9780486140520_c05.html_int_59" class="label_int"><span
class="b">Fig. 5.8-2</span></a>. Body cone rolls on space cone.

</div>

</div>

The speed of rotation of the plane containing <span class="b">ω</span>
and axis 3 about the line <span class="b">h</span> can be found as
follows. Differentiating the first of Eq. 5.8–4, and substituting from
the second, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0520.jpg](images/e9780486140520_i0520.jpg)

</div>

<div class="caption">

(5.8–9)

</div>

</div>

Letting ω<sub>1</sub>(0) and
<span class="imageinline">![e9780486140520_i0521.jpg](images/e9780486140520_i0521.jpg)</span>
be the initial conditions at <span class="i">t</span> = 0, the solution
of this equation is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0522.jpg](images/e9780486140520_i0522.jpg)

</div>

<div class="caption">

(5.8–10)

</div>

</div>

Also, from this set of equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0523.jpg](images/e9780486140520_i0523.jpg)

</div>

<div class="caption">

(5.8–11)

</div>

</div>

From the last equation we obtain for <span class="i">t</span> = 0,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0524.jpg](images/e9780486140520_i0524.jpg)

</div>

</div>

We note further that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0525.jpg](images/e9780486140520_i0525.jpg)

</div>

<div class="caption">

(5.8–12)

</div>

</div>

where
<span class="imageinline">![e9780486140520_i0526.jpg](images/e9780486140520_i0526.jpg)</span>
so that, another form of the solution is obtained by adding
ω<sub>1</sub> and ω<sub>2</sub> in quadrature

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0527.jpg](images/e9780486140520_i0527.jpg)

</div>

<div class="caption">

(5.8–13)

</div>

</div>

These equations all indicate that the vector
<span class="imageinline">![e9780486140520_i0528.jpg](images/e9780486140520_i0528.jpg)</span>
in the 1, 2–plane, rotates at a speed equal to <span class="i">λ</span>
rad/sec, with respect to the rotating body axes 1, 2, 3.
<span class="i">λ</span> is then the angular velocity of the
<span class="b">ω</span> vector as viewed by an observer stationed on
the body at the axis of symmetry.

The angle <span class="i">θ</span> between <span class="b">h</span> and
axis 3 is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0529.jpg](images/e9780486140520_i0529.jpg)

</div>

<div class="caption">

(5.8–14)

</div>

</div>

The angle <span class="i">y</span> between <span class="b">ω</span> and
axis 3 is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0530.jpg](images/e9780486140520_i0530.jpg)

</div>

<div class="caption">

(5.8–15)

</div>

</div>

By comparison we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0531.jpg](images/e9780486140520_i0531.jpg)

</div>

<div class="caption">

(5.8–16)

</div>

</div>

If <span class="i">C</span> \> <span class="i">A</span>, then
<span class="i">y</span> will be greater than <span class="i">θ</span>,
as shown in
<a href="#e9780486140520_c05.html#int_59" class="ref_int">Fig. 5.8-2</a>,
and <span class="b">h</span> will lie between axis 3 and
<span class="b">ω</span>. If <span class="i">C</span> \<
<span class="i">A</span>, <span class="i">y</span> will be smaller than
<span class="i">θ</span> and <span class="b">ω</span> will lie between
<span class="b">h</span> and axis 3.

The equations derived in this section all refer to the body axes which
are in motion with the body. They do not tell us how the body moves in
space. However, the following conclusions were obtained.

1\. The vectors <span class="b">ω, h,</span> and axis 3 lie in the same
plane.

2\. In the plane of <span class="b">ω, h</span> and axis 3, the angle
<span class="i">θ</span> between 03 and <span class="b">h</span> is
constant.

3\. The angle <span class="i">y</span> between 03 and
<span class="b">ω</span> is constant.

4\. The vector <span class="b">h</span> is constant or fixed in
direction and magnitude.

5\. The vector <span class="b">ω</span> has constant magnitude
<span class="imageinline">![e9780486140520_i0532.jpg](images/e9780486140520_i0532.jpg)</span>
.

6\. The plane containing the three vectors rotates relative to the body
axes at an angular speed <span class="i">λ</span>.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title64"></span>

# <span class="b">5.9 Body of Revolution with Zero Moment, in Terms of Euler’s Angles</span>

We will consider the previous problem of Section 5.8, by introducing the
Euler angles <span class="i">ψ</span>, <span class="i">θ</span>,
<span class="i">ϕ</span>, in order to establish the motion with respect
to fixed axes. Since h is fixed in space, we will orient it along the
<span class="i">OZ</span> axis, in which case
<span class="imageinline">![e9780486140520_i0533.jpg](images/e9780486140520_i0533.jpg)</span>
becomes the angular velocity of the node line and the spin axis about
the <span class="i">OZ</span> direction. We also had
<span class="imageinline">![e9780486140520_i0534.jpg](images/e9780486140520_i0534.jpg)</span>
from the previous section, so that Eq. 3.5–1 becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0535.jpg](images/e9780486140520_i0535.jpg)

</div>

<div class="caption">

(5.9–1)

</div>

</div>

Differentiating with
<span class="imageinline">![e9780486140520_i0536.jpg](images/e9780486140520_i0536.jpg)</span>,
the angular accelerations are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0537.jpg](images/e9780486140520_i0537.jpg)

</div>

<div class="caption">

(5.9–2)

</div>

</div>

Substituting into the first of Eq. 5.8–1, we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0538.jpg](images/e9780486140520_i0538.jpg)

</div>

<div class="caption">

(5.9–3)

</div>

</div>

Thus, the precession velocity in terms of the spin velocity
<span class="imageinline">![e9780486140520_i0539.jpg](images/e9780486140520_i0539.jpg)</span>
, <span class="i">C</span>, <span class="i">A</span>, and
<span class="i">θ</span> becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0540.jpg](images/e9780486140520_i0540.jpg)

</div>

<div class="caption">

(5.9–4)

</div>

</div>

Equation 5.9–4 states that the roll axis (also plane containing z and
<span class="b">ω</span>) rotates about a fixed
<span class="i">OZ</span> or <span class="b">h</span> axis with a speed
of
<span class="imageinline">![e9780486140520_i0541.jpg](images/e9780486140520_i0541.jpg)</span>
proportional to the angular velocity of spin
<span class="imageinline">![e9780486140520_i0542.jpg](images/e9780486140520_i0542.jpg)</span>
. If <span class="i">C</span> \> <span class="i">A</span>, the spin must
be negative, since
<span class="imageinline">![e9780486140520_i0543.jpg](images/e9780486140520_i0543.jpg)</span>
was drawn in the positive direction. Thus if <span class="i">C</span> \>
<span class="i">A</span>, the spin is opposite in sense to the
precession, and we call the case <span class="i">retrograde
precession.</span> If <span class="i">C \< A</span>, then
<span class="imageinline">![e9780486140520_i0544.jpg](images/e9780486140520_i0544.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0545.jpg](images/e9780486140520_i0545.jpg)</span>
have the same sense, and we have <span class="i">direct
precession.</span> Thus a flat disk spinning about an axis perpendicular
to its plane will have retrograde precession, whereas a slender rod
spinning about its longitudinal axis will have direct precession. The
space and body cones for the two cases are shown in
<a href="#e9780486140520_c05.html#int_60"
id="e9780486140520_c05.html_ref_int_60" class="ref_int">Figs. 5.9-1</a>
and <a href="#e9780486140520_c05.html#int_61"
id="e9780486140520_c05.html_ref_int_61" class="ref_int">5.9-2</a>. It
should be noted also that, when <span class="i">C</span> \>
<span class="i">A</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0546.jpg](images/e9780486140520_i0546.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0547.jpg](images/e9780486140520_i0547.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_60"
id="e9780486140520_c05.html_int_60" class="label_int"><span
class="b">Fig. 5.9-1</span></a>. Retrograde precession
<span class="i">C</span> \> <span class="i">A</span>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0548.jpg](images/e9780486140520_i0548.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_61"
id="e9780486140520_c05.html_int_61" class="label_int"><span
class="b">Fig. 5.9-2</span></a><span class="b">.</span> Direct
precession <span class="i">C</span> \< <span class="i">A</span>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0549.jpg](images/e9780486140520_i0549.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_62"
id="e9780486140520_c05.html_int_62" class="label_int"><span
class="b">Fig. 5.9-3</span></a>. For steady precession
<span class="b">ω</span> is the vector sum of
<span class="imageinline">![e9780486140520_i0550.jpg](images/e9780486140520_i0550.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0551.jpg](images/e9780486140520_i0551.jpg)</span>
.

</div>

</div>

Therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0552.jpg](images/e9780486140520_i0552.jpg)

</div>

</div>

As <span class="i">θ</span> → 90°,
<span class="imageinline">![e9780486140520_i0553.jpg](images/e9780486140520_i0553.jpg)</span>
becomes very large compared to
<span class="imageinline">![e9780486140520_i0554.jpg](images/e9780486140520_i0554.jpg)</span>
. Since
<span class="imageinline">![e9780486140520_i0555.jpg](images/e9780486140520_i0555.jpg)</span>
= 0, the resultant angular velocity <span class="b">ω</span> is the
vector sum of
<span class="imageinline">![e9780486140520_i0556.jpg](images/e9780486140520_i0556.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0557.jpg](images/e9780486140520_i0557.jpg)</span>
, as shown in <a href="#e9780486140520_c05.html#int_62"
id="e9780486140520_c05.html_ref_int_62" class="ref_int">Fig. 5.9-3</a>.

<span class="b">PROBLEMS</span>

1.  Show that a thin disk thrown spinning with its plane nearly parallel
    will make two wobbles to every cycle of spin.
2.  A thin disk thrown into the air is seen to wobble so that its normal
    generates a cone of 20° twice per second. Determine the rate of spin
    and the total angular velocity vector with respect to the inertial
    coordinates.
3.  A thin disk is spun about an axis making an angle
    <span class="i">y</span> with the normal to the disk and then
    released. Assuming the disk to be moment free, find the half–angle
    of the cone generated by the disk normal, and the time required for
    one complete rotation of the normal around the cone. Is the
    precession direct or retrograde ?
4.  A cylindrical disk has a thickness equal to
    <span class="i">R</span>/2 where <span class="i">R</span> is the
    radius. If it is spinning and precessing with its normal generating
    a cone angle of 15° with a fixed direction in space, determine the
    cone angle in space generated by the angular velocity vector. If the
    magnitude of ω is 10<span class="i">π</span> rad/sec, determine its
    component ω<sub>12</sub> in the plane of the disk.
5.  In Prob. 2, determine the equations for the angular velocities about
    the body axes 1, 2, 3, where 1 and 2 are in the plane of the disk
    and 3 is normal to it.
6.  In Prob. 2, determine the equations for the angular acceleration
    about the axes 1, 2, and 3.
7.  Letting <span class="i">m</span> be the mass of the disk of Prob. 4,
    write the equations for the vectors <span class="b">ω</span> and
    <span class="b">h,</span> and determine the kinetic energy of
    rotation.
8.  A uniform disk of radius <span class="i">R</span> and mass
    <span class="i">m</span> is mounted through its center to a shaft so
    that its normal makes an angle α with the shaft. If the shaft
    rotates at speed <span class="i">ω</span> between bearings a
    distance <span class="i">l</span> apart, determine the bearing
    reactions.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0558.jpg](images/e9780486140520_i0558.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 8</span>

    </div>

    </div>
9.  A thin rectangular plate of sides <span class="i">a</span> and
    <span class="i">b</span> is mounted on a shaft in the plane of the
    plate through its center. The shaft makes an angle α with the long
    side <span class="i">b</span>. Determine the bearing reactions when
    the shaft rotates at speed ω. The distance between bearings is
    <span class="i">l</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0559.jpg](images/e9780486140520_i0559.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 9</span>

    </div>

    </div>
10. Let <span class="i">x, y, z</span> be the principal axes through the
    center of gravity of an airplane, with <span class="i">A</span>,
    <span class="i">B, C</span> as principal moments of inertia. Show
    that in order for the airplane to make a turn of radius
    <span class="i">R</span> about a vertical line, with speed
    <span class="i">V</span>, it must bank at an angle
    <span class="i">θ</span> = tan<sup>–1</sup>
    <span class="i">V</span><sup>2</sup>/<span class="i">Rg</span> and
    supply a rolling moment in the same direction as
    <span class="i">θ</span>, equal to
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0560.jpg](images/e9780486140520_i0560.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 10</span>

    </div>

    </div>
11. Determine the gyroscopic moment necessary for the airplane of Prob.
    10 to spin with speed
    <span class="imageinline">![e9780486140520_i0561.jpg](images/e9780486140520_i0561.jpg)</span>
    about the vertical <span class="i">OZ</span> axis, when the nose of
    the airplane is inclined at an angle α below the horizontal.
12. If the spin
    <span class="imageinline">![e9780486140520_i0562.jpg](images/e9780486140520_i0562.jpg)</span>
    takes place about an axis through the center of gravity making
    angles <span class="i">α</span>, <span class="i">β</span>,
    <span class="i">y</span>, with respect to the
    <span class="i">x,</span> <span class="i">y</span>,
    <span class="i">z</span> axes of the airplane, write the
    differential equations for the moments
    <span class="i">M</span><sub><span class="i">x</span></sub>,
    <span class="i">M</span><sub><span class="i">y</span></sub>, and
    <span class="i">M</span><sub><span class="i">z</span></sub>.
13. A slender rod of mass <span class="i">m</span> and length
    <span class="i">l</span> is welded to a shaft at its ⅓ point at an
    angle <span class="i">θ</span>. Determine the bearing reactions when
    the shaft rotates with speed <span class="i">ω</span>, and the
    distance between bearings is 2<span class="i">c</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0563.jpg](images/e9780486140520_i0563.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 13</span>

    </div>

    </div>
14. A missile with
    <span class="imageinline">![e9780486140520_i0564.jpg](images/e9780486140520_i0564.jpg)</span>
    is spinning at speed <span class="i">n</span> =
    10<span class="i">π</span> rad/sec and precessing at an angle 0 = 5°
    with a fixed direction in space. Determine the precession speed
    <span class="imageinline">![e9780486140520_i0565.jpg](images/e9780486140520_i0565.jpg)</span>
    and the angle between the resultant angular velocity vector and the
    longitudinal axis. Draw the body and space cones. What can you
    conclude regarding the precessional speed of slender bodies?

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title65"></span>

# <span class="b">5.10 Unsymmetrical Body with Zero External Moment (Poinsot’s Geometric Solution)</span>

In the general case of a body without an axis of revolution, the
principal moments of inertia are unequal, so that Euler’s equations for
no external torque become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0566.jpg](images/e9780486140520_i0566.jpg)

</div>

<div class="caption">

(5.1–0<span class="b">)</span>

</div>

</div>

where 1, 2, 3 are body–fixed axes coinciding with the principal axis.
The solution of these equations involve elliptic functions, and is taken
up in Sec. 5.11. The following is a geometric discussion of the solution
due to Poinsot.

With no external torque, the kinetic energy and the moment of momentum
about the center of mass <span class="i">C</span> are constants.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0567.jpg](images/e9780486140520_i0567.jpg)

</div>

<div class="caption">

(5.10–2)

</div>

</div>

No work is done on the body, therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0568.jpg](images/e9780486140520_i0568.jpg)

</div>

<div class="caption">

(5.10–3)

</div>

</div>

The expression for <span class="b">ω</span> and <span class="b">h</span>
are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0569.jpg](images/e9780486140520_i0569.jpg)

</div>

<div class="caption">

(5.10–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0570.jpg](images/e9780486140520_i0570.jpg)

</div>

<div class="caption">

(5.10–5)

</div>

</div>

from which we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0571.jpg](images/e9780486140520_i0571.jpg)

</div>

<div class="caption">

(5.10–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0572.jpg](images/e9780486140520_i0572.jpg)

</div>

<div class="caption">

(5.10–7)

</div>

</div>

With <span class="b">h</span> drawn in a specified direction, its unit
vector is <span class="b">h</span>/<span class="i">h</span>, and the
component of <span class="b">ω</span> along <span class="b">h</span>
will be given by

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0573.jpg](images/e9780486140520_i0573.jpg)

</div>

<div class="caption">

(5.10–8)

</div>

</div>

Thus <span class="i">N</span> is a fixed point along the direction of
<span class="b">h</span>, as shown in
<a href="#e9780486140520_c05.html#int_63"
id="e9780486140520_c05.html_ref_int_63" class="ref_int">Fig. 5.10-1</a>,
and the end of the <span class="b">ω</span> vector must lie in a plane
through <span class="i">N</span> perpendicular to
<span class="i">ON</span>. The line <span class="i">ON</span> is
referred to as the <span class="i">invariable line,</span> and the
perpendicular plane the <span class="i">invariable plane</span>. Thus
the end of the vector <span class="b">ω</span> must move in this
invariable plane.

Letting the coordinates of <span class="b">ω</span> be
<span class="i">ξ′</span>, <span class="i">η′</span>,
<span class="i">ζ′</span>, we have <span class="i">ω</span><sub>1</sub>
= <span class="i">ξ’</span>, <span class="i">ω</span><sub>2</sub> =
<span class="i">η′</span>, and <span class="i">ω</span><sub>3</sub> =
<span class="i">ξ’</span>. The equation for 2<span class="i">T</span>
may then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0574.jpg](images/e9780486140520_i0574.jpg)

</div>

<div class="caption">

(5.10–9)

</div>

</div>

which is called the Poinsot ellipsoid.
<a href="#e9780486140520_c05.html#int_64"
id="e9780486140520_c05.html_ref_int_64" class="ref_int">Figure
5.10-2</a> is an illustration of the ellipsoid.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0575.jpg](images/e9780486140520_i0575.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_63"
id="e9780486140520_c05.html_int_63" class="label_int"><span
class="b">Fig. 5.10-1</span></a>. Invariable line
<span class="i">ON</span> and invariable plane <span class="i">s</span>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0576.jpg](images/e9780486140520_i0576.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_64"
id="e9780486140520_c05.html_int_64" class="label_int"><span
class="b">Fig. 5.10-2</span></a>. Poinsot ellipsoid.

</div>

</div>

We next examine the inertia ellipsoid which was previously described as
the locus of <span class="i">ρ</span> = 1/√I laid off along the
<span class="b">ω</span> vector. Letting the coordinates of p be
<span class="i">ξ</span>, <span class="i">η</span>,
<span class="i">ζ</span>, the equation for the inertia ellipsoid from
Eq. 5.5–2 becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0577.jpg](images/e9780486140520_i0577.jpg)

</div>

<div class="caption">

(5.10–10)

</div>

</div>

We thus see that the Poinsot ellipsoid is proportional to the inertia
ellipsoid with its coordinates equal to
<span class="imageinline">![e9780486140520_i0578.jpg](images/e9780486140520_i0578.jpg)</span>
times the coordinates of the inertia ellipsoid.

The Poinsot ellipsoid can be shown to roll on the invariable plane with
its center a distance <span class="i">ON</span> =
2<span class="i">T/h</span> from it. Starting with the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0579.jpg](images/e9780486140520_i0579.jpg)

</div>

<div class="caption">

(5.10–11)

</div>

</div>

and remembering that <span class="b">h</span> and
<span class="i">T</span> are constant, we can obtain the following
differential relationship.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0580.jpg](images/e9780486140520_i0580.jpg)

</div>

<div class="caption">

(5.10–12)

</div>

</div>

Since the vanishing of the dot product of two vectors
<span class="i">dω</span> and <span class="b">h</span> requires that the
cosine of the angle between them be zero, we conclude that
<span class="i">dω</span> and <span class="b">h</span> are perpendicular
to each other. With the end point of <span class="b">ω</span> moving in
the invariable plane, any change <span class="i">dω</span> of
<span class="b">ω</span> is perpendicular to <span class="b">h,</span>
and since the locus of <span class="b">ω</span>
(<span class="i">ξ′</span>, <span class="i">η′</span>,
<span class="i">ζ′</span>) corresponds to the Poinsot ellipsoid, it must
be tangent to the invariable plane. Thus to an observer stationed to a
fixed coordinate system, the motion of the body is described by the
rolling of the Poinsot ellipsoid (or inertia ellipsoid with
<span class="i">ξ, η</span>, <span class="i">ζ</span> coordinates
increased by
<span class="imageinline">![e9780486140520_i0581.jpg](images/e9780486140520_i0581.jpg)</span>)
on the invariable plane.

If we wish to examine the motion from the point of view of an observer
stationed on the moving body, the invariable plane will now appear to
move with respect to the body. From the angular momentum equation, Eq.
5.10–7, we can rearrange the terms to form the angular momentum
ellipsoid as follows.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0582.jpg](images/e9780486140520_i0582.jpg)

</div>

<div class="caption">

(5.10–13)

</div>

</div>

The curve traced by the end of the ω vector is then defined by the
intersection of the Poinsot, ellipsoid Eq. 5.10–9, and the angular
momentum Eq. 5.10–13, ellipsoid.

The instantaneous axis <span class="b">ω</span> passes through the point
of contact between the Poinsot ellipsoid and the invariable plane. It
therefore generates simultaneously two cones, one in the fixed space,
and the other in the body or the Poinsot ellipsoid. These cones, called
the herpolhode and the polhode cones respectively, are shown in
<a href="#e9780486140520_c05.html#int_65"
id="e9780486140520_c05.html_ref_int_65" class="ref_int">Fig. 5.10-3</a>.

Since <span class="b">ω</span> is common to both the Poinsot ellipsoid
and the momentum ellipsoid, the equation for the body cone can be
obtained by subtracting Eq. 5.10–9 from 5.10–13 and multiplying by
<span class="i">h</span><sup>2</sup>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0583.jpg](images/e9780486140520_i0583.jpg)

</div>

<div class="caption">

(5.10–14)

</div>

</div>

This equation indicates that for the body cone to be real,
<span class="i">h</span><sup><span class="i">2</span></sup>/2<span class="i">T</span>
must lie between the greatest and least values of
<span class="i">A</span>, <span class="i">B</span>, and
<span class="i">C</span>. For instance, if we let
<span class="i">A</span> \> <span class="i">B</span> \>
<span class="i">C,</span> then
<span class="i">h</span><sup>2</sup>/2<span class="i">T</span> must
satisfy the relation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0584.jpg](images/e9780486140520_i0584.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0585.jpg](images/e9780486140520_i0585.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_65"
id="e9780486140520_c05.html_int_65" class="label_int"><span
class="b">Fig. 5.10-3</span></a>. Poinsot ellipsoid rolls on the
invariable plane s.

</div>

</div>

To find the polhode curves, we let the Poinsot ellipsoid intersect the
polhode cone. The form of these curves is best visualized by looking at
their principal plane projections, obtained by eliminating in turn one
of the coordinates between Eqs. 5.10–14 and 5.10–9. The three equations
so obtained are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0586.jpg](images/e9780486140520_i0586.jpg)

</div>

<div class="caption">

(5.10–15)

</div>

</div>

If <span class="i">h</span><sup>2</sup>/2<span class="i">T</span> =
<span class="i">C</span>, the first equation can be satisfied for
<span class="i">ξ′</span> = <span class="i">η′</span> = 0. The polhode
curve then degenerates to a point on the <span class="i">ζ′</span> axis.

If <span class="i">h</span><sup>2</sup>/2<span class="i">T</span> =
<span class="i">B</span>, we obtain from the second of the three
equations

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0587.jpg](images/e9780486140520_i0587.jpg)

</div>

<div class="caption">

(5.10–16)

</div>

</div>

which indicates two planes passing through <span class="i">η′</span>
axis. The <span class="i">ξ′η′</span> and the
<span class="i">η′ζ′</span> projections from the other two equations,
are ellipses.

If
<span class="i">h</span><sup><span class="i">2</span></sup><span class="i">/</span>2<span class="i">T</span>
= <span class="i">A</span>, the third of the three equations can only be
satisfied if <span class="i">η′</span> = <span class="i">ζ′</span> = 0,
and the polhode curve degenerates to a point on the
<span class="i">ξ′</span> axis.

If
<span class="i">h</span><sup><span class="i">2</span></sup>/2<span class="i">T</span>
lies between <span class="i">B</span> and <span class="i">C</span>, the
polhodes lie between the planes of Eq. 5.10–16 and the
<span class="i">ζ′</span> axis. Their <span class="i">ξ′η′</span>
projections are ellipses.

If
<span class="i">h</span><sup>2</sup><span class="i">l</span>2<span class="i">T</span>
lies between <span class="i">A</span> and <span class="i">B</span>, the
polhodes lie in the central part of the ellipsoid between the planes of
Eq. 5.10–16. Their <span class="i">η’ζ’</span> projections are ellipses
and their <span class="i">ξ’ζ’</span> projections are hyperbolas. The
general nature of the polhode curve for the various cases are shown in
<a href="#e9780486140520_c05.html#int_66"
id="e9780486140520_c05.html_ref_int_66" class="ref_int">Fig. 5.10-4</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0588.jpg](images/e9780486140520_i0588.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_66"
id="e9780486140520_c05.html_int_66" class="label_int"><span
class="b">Fig. 5.10-4</span></a>. Polhode curves.

</div>

</div>

If we write Eqs. 5.10–6 and 5.10–7 in terms of momentum components,
<span class="i">h</span><sub>1</sub>,
<span class="i">h</span><sub>2</sub>,
<span class="i">h</span><sub>3</sub>, they become

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0589.jpg](images/e9780486140520_i0589.jpg)

</div>

<div class="caption">

(5.10–17)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0590.jpg](images/e9780486140520_i0590.jpg)

</div>

<div class="caption">

(5.10–18)

</div>

</div>

and their simultaneous solution give the intersection of the Poinsot
ellipsoid, Eq. 5.10–17, and the momentum sphere, Eq. 5.10–18, in terms
of the momentum coordinates. Since Eqs. 5.10–14 and 5.10–15 are also
solutions to the same problem, we need only to rewrite these equations
in terms of <span class="i">h</span><sub>1</sub>,
<span class="i">h</span><sub>2</sub>, and
<span class="i">h</span><sub>3</sub>. Thus Eq. 5.10–14 rewritten in
terms of momentum coordinates is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0591.jpg](images/e9780486140520_i0591.jpg)

</div>

<div class="caption">

(5.10–19)

</div>

</div>

<a href="#e9780486140520_c05.html#int_67"
id="e9780486140520_c05.html_ref_int_67" class="ref_int">Figure
5.10-5</a> is a plot of Eq. 5.10–19 showing the locus of the
<span class="b">h</span> vector on the momentum sphere for various
values of
<span class="i">h</span><sup>2</sup>/2<span class="i">T</span>, where A
\> B \> C, and <span class="i">A</span> ≥
<span class="i">h</span><sup>2</sup>/2<span class="i">T</span> \>
<span class="i">C</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0592.jpg](images/e9780486140520_i0592.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_67"
id="e9780486140520_c05.html_int_67" class="label_int"><span
class="b">Fig. 5.10-5</span></a><span class="b">.</span> Locus of
<span class="b">h</span> on momentum sphere.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title66"></span>

# <span class="b">5.11 Unequal Moments of Inertia with Zero Moment (Analytic Solution)</span>

When the moments of inertia <span class="i">A</span>,
<span class="i">B</span>, <span class="i">C</span> are unequal, the
general solution of Eqs. 5.10–1 results in elliptic functions. We take
advantage of Eqs. 5.10–6 and 5.10–7 which are integrals of the Euler
equations, and obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0593.jpg](images/e9780486140520_i0593.jpg)

</div>

<div class="caption">

(5.11–1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0594.jpg](images/e9780486140520_i0594.jpg)

</div>

<div class="caption">

(5.11–2)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0595.jpg](images/e9780486140520_i0595.jpg)

</div>

<div class="caption">

(5.11–3)

</div>

</div>

If we assume <span class="i">A</span> \> <span class="i">B</span> \> C,
Eq. 5.11–1 is always negative, Eq. 5.11–3 is always positive, and Eq.
5.11–2 may be either positive or negative. From Eqs. 5.11–1 and 3, we
write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0596.jpg](images/e9780486140520_i0596.jpg)

</div>

<div class="caption">

(5.11–4)

</div>

</div>

We now let

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0597.jpg](images/e9780486140520_i0597.jpg)

</div>

<div class="caption">

(5.11–5)

</div>

</div>

so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0598.jpg](images/e9780486140520_i0598.jpg)

</div>

<div class="caption">

(5.11–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0599.jpg](images/e9780486140520_i0599.jpg)

</div>

<div class="caption">

(5.11–7)

</div>

</div>

Substituting these into the second of Eq. 5.10–1, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0600.jpg](images/e9780486140520_i0600.jpg)

</div>

<div class="caption">

(5.11–8)

</div>

</div>

which is recognized as an elliptic integral of the first kind,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0601.jpg](images/e9780486140520_i0601.jpg)

</div>

<div class="caption">

(5.11–9)

</div>

</div>

where <span class="i">t</span> is measured from the instant when
<span class="i">ω</span><sub>2</sub> = 0. On letting
<span class="i">y</span> = sin <span class="i">φ</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0602.jpg](images/e9780486140520_i0602.jpg)

</div>

<div class="caption">

(5.11–10)

</div>

</div>

and <span class="i">u</span> becomes a function of the modulus
<span class="i">k</span> and the amplitude <span class="i">φ</span>.
Conversely, <span class="i">y</span> is a function of
<span class="i">u</span> = <span class="i">Nt</span> and
<span class="i">k</span>, and is available as a tabulated function for 0
≤ <span class="i">k</span> \< 1, where <span class="i">N</span> is
defined by Eq. 5.11–9.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0603.jpg](images/e9780486140520_i0603.jpg)

</div>

<div class="caption">

(5.11–11)

</div>

</div>

Thus from Eq. 5.11–5 the solution for
<span class="i">ω</span><sub>2</sub> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0604.jpg](images/e9780486140520_i0604.jpg)

</div>

<div class="caption">

(5.11–12)

</div>

</div>

Likewise, it can be shown that the solution for the angular velocities
about the other two axes are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0605.jpg](images/e9780486140520_i0605.jpg)

</div>

<div class="caption">

(5.11–13)

</div>

</div>

where the
<span class="imageinline">![e9780486140520_i0606.jpg](images/e9780486140520_i0606.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0607.jpg](images/e9780486140520_i0607.jpg)</span>
functions are related to the
<span class="imageinline">![e9780486140520_i0608.jpg](images/e9780486140520_i0608.jpg)</span>
function by the equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0609.jpg](images/e9780486140520_i0609.jpg)

</div>

<div class="caption">

(5.11–14)

</div>

</div>

These solutions correspond to the case
<span class="i">h</span><sup>2</sup> \< 2<span class="i">TB</span> which
is required for 0 ≤ <span class="i">K</span> ≤ 1.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0610.jpg](images/e9780486140520_i0610.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_68"
id="e9780486140520_c05.html_int_68" class="label_int"><span
class="b">Fig. 5.11-1</span></a>. Plot of elliptic functions.  
<a href="#e9780486140520_c05.html#ref_int_69"
id="e9780486140520_c05.html_int_69" class="label_int"><span
class="b">Fig. 5.11-2</span></a><span class="b">.</span> Plot of
elliptic functions.

</div>

</div>

For small values of <span class="i">k</span> → 0 (i.e.,
<span class="i">A</span> approaching <span class="i">B</span>), the
elliptic functions approach the trigonometric functions,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0611.jpg](images/e9780486140520_i0611.jpg)

</div>

</div>

Thus when <span class="i">A</span> = <span class="i">B</span>, the
angular velocities reduce to the form:

<div class="blocktext">

ω<sub>2</sub> = <span class="i">β</span> sin
(<span class="i">Nt</span>)  
<span class="i">ω</span><sub>1</sub> = <span class="i">β</span> cos
(<span class="i">Nt</span>)  
<span class="i">ω</span><sub>3</sub> = <span class="i">n</span>

</div>

which agree with the results of Sec. 5.8.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0612.jpg](images/e9780486140520_i0612.jpg)

</div>

<div class="caption">

Table of
<span class="imageinline">![e9780486140520_i0613.jpg](images/e9780486140520_i0613.jpg)</span>
Taken from Peirce’s Table of Integrals 3rd Revised Ed. p. 122

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0614.jpg](images/e9780486140520_i0614.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_70"
id="e9780486140520_c05.html_int_70" class="label_int"><span
class="b">Fig. 5.11-3</span></a>. Plot of elliptic function
<span class="imageinline">![e9780486140520_i0615.jpg](images/e9780486140520_i0615.jpg)</span>
.

</div>

</div>

To show the effect of <span class="i">A</span> ≠
<span class="i">B</span>, a plot of the elliptic function for
<span class="i">k</span> = ½ is compared to the trigonometric functions
in <a href="#e9780486140520_c05.html#int_68"
id="e9780486140520_c05.html_ref_int_68" class="ref_int">Fig. 5.11-1</a>.
If <span class="i">y</span> = sin <span class="i">φ</span> =
<span class="imageinline">![e9780486140520_i0616.jpg](images/e9780486140520_i0616.jpg)</span>
is plotted against <span class="i">u</span> = <span class="i">Nt</span>
for various values of <span class="i">k</span>, with
<span class="i">u</span> normalized to unity at <span class="i">φ</span>
= 90°, the plot of
<span class="imageinline">![e9780486140520_i0617.jpg](images/e9780486140520_i0617.jpg)</span>
will appear as in <a href="#e9780486140520_c05.html#int_69"
id="e9780486140520_c05.html_ref_int_69" class="ref_int">Figs. 5.11-2</a>
and <a href="#e9780486140520_c05.html#int_70"
id="e9780486140520_c05.html_ref_int_70" class="ref_int">5.11-3</a>.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title67"></span>

# <span class="b">5.12 Stability of Rotation about Principal Axes</span>

If we write Euler’s equations for no external moment in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0618.jpg](images/e9780486140520_i0618.jpg)

</div>

<div class="caption">

(5.12–1)

</div>

</div>

we find that,

<div class="blocktext">

<span class="i">ω</span><sub>1</sub> = constant if
<span class="i">ω</span><sub>2</sub> =
<span class="i">ω</span><sub>3</sub> = 0  
<span class="i">ω</span><sub>2</sub> = constant if
<span class="i">ω</span><sub>1</sub> =
<span class="i">ω</span><sub>3</sub> = 0  
<span class="i">ω</span><sub>3</sub> = constant if
<span class="i">ω</span><sub>1</sub> =
<span class="i">ω</span><sub>2</sub> = 0

</div>

indicating that permanent rotations are possible about each of the
principal axes. We will now show that these permanent rotations are
stable about the axes of maximum and minimum moments of inertia, and
unstable about the axis of intermediate moment of inertia.

We will assume constant rotation about one of the axes, say axis 1, and
allow a small perturbation to determine its stability. We then have an
initial condition <span class="i">ω</span><sub>1</sub> =
<span class="i">ω</span><sub><span class="i">0</span></sub><span class="i">,
ω</span><sub><span class="i">2</span></sub> =
<span class="i">ω</span><sub><span class="i">3</span></sub> = 0, and a
perturbed condition, <span class="i">ω</span><sub>1</sub> =
ω<sub>0</sub> + e, with ω<sub>2</sub> and ω<sub>3</sub> small. The
linearized equations are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0619.jpg](images/e9780486140520_i0619.jpg)

</div>

<div class="caption">

(5.12–2)

</div>

</div>

Differentiating the second and third of Eq. 5.12–2, we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0620.jpg](images/e9780486140520_i0620.jpg)

</div>

<div class="caption">

(5.12–3)

</div>

</div>

which are stable provided
(<span class="i">A</span>–<span class="i">B</span>)(<span class="i">A</span>–<span class="i">C</span>)
is positive. We see that this condition is satisfied provided
<span class="i">A</span> \> <span class="i">B,</span> and
<span class="i">A</span> \> C <span class="i">(A</span> a major
principal axis), <span class="i">or B</span> \>
<span class="i">A</span>, and C \> <span class="i">A</span>
(<span class="i">A</span> a minor principal axis). When
<span class="i">A</span> is an intermediate value between
<span class="i">B</span> and C,
(<span class="i">A</span>–<span class="i">B</span>)(<span class="i">A</span>–<span class="i">C</span>)
is negative, and small values of ω<sub>2</sub> and ω<sub>3</sub> will
increase. The first of Eq. 5.12–2 requires that the small perturbation ∊
remain constant, and, hence, if axis 1 is either a major or minor
principal axis, the rotation is stable. If axis 1 is an intermediate
axis, <span class="i">ω</span><sub>2</sub> and
<span class="i">ω</span><sub>3</sub> will increase, resulting in an
unstable oscillation. The above conclusions can be simply demonstrated
by dropping an eraser spinning about each of the principal axes.
Situations requiring modification of these conclusions are discussed in
Sec. 7.6.

<span class="b">PROBLEMS</span>

1.  Determine the ellipsoid of inertia for the configuration of Prob.
    5.5–4.

2.  Determine the ellipsoid of inertia for a solid uniform cylinder of
    radius <span class="i">R</span> and length
    2<span class="i">R</span>. What is its moment of inertia about a
    line passing through its geometric center and the perifery of one
    end.

3.  Consider a spinning body with <span class="i">A</span> \>
    <span class="i">B</span> \> <span class="i">C</span>. With initial
    conditions ω<sub>1</sub> = <span class="i">p</span><sub>0</sub>,
    ω<sub>2</sub> = 0, ω<sub>3</sub> =
    <span class="i">r</span><sub><span class="i">0</span></sub>, find
    <span class="i">ω</span><sub>1</sub>,
    <span class="i">ω</span><sub>2</sub>, and
    <span class="i">ω</span><sub>3</sub> for a motion characterized by
    one of the plane polhodes
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0621.jpg](images/e9780486140520_i0621.jpg)

    </div>

    </div>

    Show that, with t approaching ∞, the motion tends to a permanent
    rotation about axis 2.

4.  Show that, for a body with principal moments of inertia
    <span class="i">A</span>, B, C, the polhodes are closed curves while
    the herpolhodes generated on the invariable plane are generally open
    curves.

5.  Derive the equations for <span class="i">ω</span><sub>1</sub>,
    <span class="i">ω</span><sub>2</sub>,
    <span class="i">ω</span><sub>3</sub>, when
    <span class="i">h</span><sup>2</sup> \> 2<span class="i">TB</span>
    and <span class="i">A</span> \> B \> C.

6.  Discuss the stability of rotation of an unsymmetric body in the
    moment–free case in terms of the polhode curves of
    <a href="#e9780486140520_c05.html#int_66" class="ref_int">Fig.
    5.10-4</a>.

7.  Solve for the exact solution of a simple pendulum oscillating
    through large amplitudes. Express the equation for the period in
    terms of an elliptical integral and its series approximation.

8.  For <span class="i">h</span><sup>2</sup>/2<span class="i">T</span>
    \< <span class="i">B</span>, where <span class="i">A</span> \>
    <span class="i">B</span> \> <span class="i">C</span>, the angle
    <span class="i">θ</span><sub>3</sub> made by the h vector and the
    <span class="i">h</span><sub>3</sub> axis is defined by the equation
    (see <a href="#e9780486140520_c05.html#int_67" class="ref_int">Fig.
    5.10-5</a>)

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0622.jpg](images/e9780486140520_i0622.jpg)

    </div>

    </div>

    Show that the value of <span class="i">θ</span><sub>3</sub> varies
    between

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0623.jpg](images/e9780486140520_i0623.jpg)

    </div>

    </div>

    <span class="i">Hint</span>: Rewrite Eqs. 5.10–15 in terms of
    <span class="i">h</span><sub>1</sub>,
    <span class="i">h</span><sub>2</sub>,
    <span class="i">h</span><sub>3</sub>.

9.  Derive the equations for <span class="i">ω</span><sub>1</sub>,
    <span class="i">ω</span><sub>2</sub>, ω<sub>3</sub> when
    <span class="i">C</span> \> <span class="i">B \> A</span> and
    examine the conditions <span class="i">h</span><sup>2</sup> \<
    2<span class="i">TB</span> and <span class="i">h</span><sup>2</sup>
    \> 2<span class="i">TB</span>.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title68"></span>

# <span class="b">5.13 General Motion of a Symmetric Gyro or Top</span>

<a href="#e9780486140520_c05.html#int_71"
id="e9780486140520_c05.html_ref_int_71" class="ref_int">Figure
5.13-1</a> shows a symmetric gyro spinning about axis
<span class="i">ζ</span> and supported by two gimbals. The inner gimbal
allows a pitching rotation of the spin axis about the horizontal
bearings <span class="i">ξ</span>, while the outer gimbal is free to
rotate about the vertical <span class="i">Z</span> axis. The gyro is
then pivoted about the stationary geometric center of the gimbal system,
and the center of mass does not coincide with the fixed center
<span class="i">O</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0624.jpg](images/e9780486140520_i0624.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_71"
id="e9780486140520_c05.html_int_71" class="label_int"><span
class="b">Fig. 5.13-1</span></a><span class="b">.</span> Symmetric
gyro–angular momentum about gimbal axes.

</div>

</div>

We will now define precession and nutation in the following manner. The
rotation
<span class="imageinline">![e9780486140520_i0625.jpg](images/e9780486140520_i0625.jpg)</span>
of the horizontal axis ξ (node axis) about the vertical
<span class="i">Z</span> axis is called precession. If the angle 6 is
held constant, the spin axis will generate a cone due to precession. The
rotation
<span class="imageinline">![e9780486140520_i0626.jpg](images/e9780486140520_i0626.jpg)</span>
of the inner gimbal about the node axis <span class="i">ξ</span> is
called nutation. The term signifies a nodding of the spin axis. In the
general case, both precession and nutation may exist simultaneously.

We will at first neglect the mass of the gimbals, in which case we would
have only the spinning wheel free to rotate in any manner about the
stationary geometric center <span class="i">O,</span> as shown in
<a href="#e9780486140520_c05.html#int_71" class="ref_int">Fig.
5.13-1</a><span class="i">b</span>. The system is then identical to that
of a spinning top pivoted about a fixed point <span class="i">O,</span>
and subject to a gravity torque <span class="i">Wl</span> sin
<span class="i">θ</span> about the axis <span class="i">ξ</span>. If
<span class="i">I</span> = 0, we have the special case of a gyro free to
rotate about the center of gravity.

<span class="i">It</span> is convenient here to write the moment
equations about the cartesian coordinates through the geometric center
with the line of nodes ξ as one of the axes. We will let the moment of
inertia of the wheel about the node axis system
<span class="i">ξ</span>, <span class="i">η</span>, and ζ be
<span class="i">A</span>, <span class="i">A</span>,
<span class="i">C.</span> The angular velocities of the
<span class="i">ξ</span>, <span class="i">η</span>,
<span class="i">ζ</span> axes and the angular momentum about them are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0627.jpg](images/e9780486140520_i0627.jpg)

</div>

<div class="caption">

(5.13–1)

</div>

</div>

where <span class="i">ϕ</span> is the spin angle of the body axes 1, 2,
referenced to the node axis <span class="i">ξ</span>.

The components of the moment equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0628.jpg](images/e9780486140520_i0628.jpg)

</div>

<div class="caption">

(5.13–2)

</div>

</div>

can be immediately written down by examination of
<a href="#e9780486140520_c05.html#int_71" class="ref_int">Fig.
5.13-1</a><span class="i">c</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0629.jpg](images/e9780486140520_i0629.jpg)

</div>

<div class="caption">

(5.13–3)

</div>

</div>

Substituting for the components of <span class="b">h</span> and
<span class="b">M,</span> these equations become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0630.jpg](images/e9780486140520_i0630.jpg)

</div>

<div class="caption">

(5.13–4)

</div>

</div>

The last equation indicates that
<span class="imageinline">![e9780486140520_i0631.jpg](images/e9780486140520_i0631.jpg)</span>
is a constant, and we will let it equal <span class="i">n.</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0632.jpg](images/e9780486140520_i0632.jpg)

</div>

<div class="caption">

(5.13–5)

</div>

</div>

With this substitution, the first two equations of Eq. 5.13–4 can be
integrated with proper integrating factors. We will, however, consider
an alternative approach based on certain integrals of the equations of
motion which are constant. These are the conservation of total energy,
and the conservation of angular momentum about the vertical
<span class="i">Z</span> axis which is moment–free.

If we examine the equations for the angular velocities about the body
axes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0633.jpg](images/e9780486140520_i0633.jpg)

</div>

<div class="caption">

(5.13–6)

</div>

</div>

we would find that by adding the squares of the first two, that the
square of the resultant velocity in the equatorial plane, in terms of
Euler’s angles is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0634.jpg](images/e9780486140520_i0634.jpg)

</div>

<div class="caption">

(5.13–7)

</div>

</div>

Since <span class="i">ω</span><sub>3</sub> is constant and equal to
<span class="i">n</span>, the kinetic energy can now be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0635.jpg](images/e9780486140520_i0635.jpg)

</div>

<div class="caption">

(5.13–8)

</div>

</div>

Referencing the potential energy to the level of the origin of the
coordinate system.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0636.jpg](images/e9780486140520_i0636.jpg)

</div>

<div class="caption">

(5.13–9)

</div>

</div>

and the total energy <span class="i">E,</span> which must be a constant,
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0637.jpg](images/e9780486140520_i0637.jpg)

</div>

<div class="caption">

(5.13–10)

</div>

</div>

which is one of the first integrals of the differential equations of
motion.

With the moment about the <span class="i">Z</span> axis equal to zero,
the momentum <span class="i">h</span><sub>Z</sub> =
<span class="i">h</span><sub><span class="i">ζ</span></sub> cos
<span class="i">θ</span> +
<span class="i">h</span><sub><span class="i">η</span></sub> sin θ must
be a constant,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0638.jpg](images/e9780486140520_i0638.jpg)

</div>

<div class="caption">

(5.13–11)

</div>

</div>

This equation could also be obtained from the Lagrangian approach since
the generalized coordinate <span class="i">ψ</span> is a cyclic
coordinate with
<span class="i">M</span><sub><span class="i">z</span></sub> = 0 (see
Chap. 9) Solving for
<span class="imageinline">![e9780486140520_i0639.jpg](images/e9780486140520_i0639.jpg)</span>
from the above equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0640.jpg](images/e9780486140520_i0640.jpg)

</div>

<div class="caption">

(5.13–12)

</div>

</div>

and substituting into Eq. 5.13–10, we obtain the following form of the
energy equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0641.jpg](images/e9780486140520_i0641.jpg)

</div>

<div class="caption">

(5.13–13)

</div>

</div>

Equation 5.13–13 is entirely in terms of <span class="i">θ</span>, and
its solution substituted into Eq. 5.13–10 completely describes the
motion of the system.

We now make the following substitution of symbols:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0642.jpg](images/e9780486140520_i0642.jpg)

</div>

</div>

which enables Eq. 5.13–13 to be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0643.jpg](images/e9780486140520_i0643.jpg)

</div>

<div class="caption">

(5.13–14)

</div>

</div>

In terms of <span class="i">u</span>, the equation becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0644.jpg](images/e9780486140520_i0644.jpg)

</div>

<div class="caption">

(5.13–15)

</div>

</div>

The solution of the above equation is given by the following integral
which can be evaluated in terms of elliptic functions.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0645.jpg](images/e9780486140520_i0645.jpg)

</div>

<div class="caption">

(5.13–16)

</div>

</div>

The mathematical solution resulting from the above elliptical integral
is difficult to interpret, however; fortunately it is not necessary to
carry out the above solution to evaluate the behavior of the gyro. If we
let,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0646.jpg](images/e9780486140520_i0646.jpg)

</div>

<div class="caption">

(5.13–17)

</div>

</div>

Equation 5.13–15 can be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0647.jpg](images/e9780486140520_i0647.jpg)

</div>

<div class="caption">

(5.13–18)

</div>

</div>

and the roots of this equation will tell us a great deal about the
motion of the gyro.

Although <span class="i">u</span> = cos <span class="i">θ</span> is
limited between ± 1 for the physical problem, mathematically
<span class="i">u</span> can extend outside this region. For large
values of <span class="i">u</span>, the dominant term in
<span class="i">ƒ</span>(<span class="i">u</span>) is
β<span class="i">u</span><sup>3</sup>, thus
<span class="i">ƒ</span>(<span class="i">u</span>) must be positive for
large positive <span class="i">u</span>, and negative for large negative
<span class="i">u</span>, as shown in
<a href="#e9780486140520_c05.html#int_72"
id="e9780486140520_c05.html_ref_int_72" class="ref_int">Fig. 5.13-2</a>.
Also at <span class="i">u</span> = 1, the first term drops out, leaving,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0648.jpg](images/e9780486140520_i0648.jpg)

</div>

</div>

It is evident then that
<span class="i">ƒ</span>(<span class="i">u</span>) at
<span class="i">u</span> = ±1 must always be negative. Looking at the
expression for <span class="i">ƒ</span>(<span class="i">u</span>) in
terms of <span class="i">θ</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0649.jpg](images/e9780486140520_i0649.jpg)

</div>

<div class="caption">

(5.13–19)

</div>

</div>

we find that, for real values of <span class="i">θ</span> and
<span class="imageinline">![e9780486140520_i0650.jpg](images/e9780486140520_i0650.jpg)</span>
, <span class="i">ƒ</span>(<span class="i">u</span>) must be positive.
We therefore conclude that, for the physical problem,
<span class="i">u</span> = cos <span class="i">θ</span>, must always lie
between <span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub> for which
<span class="i">ƒ</span>(<span class="i">u</span>) is positive.

We note next that for <span class="i">θ</span> \> 0,
<span class="imageinline">![e9780486140520_i0651.jpg](images/e9780486140520_i0651.jpg)</span>
must be zero at <span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub>, which requires that the spin axis
<span class="i">O</span>ζ move between the bounding circles
<span class="i">u</span><sub>1</sub> = cos
<span class="i">θ</span><sub>1</sub>, and
<span class="i">u</span><sub>2</sub> = cos
<span class="i">θ</span><sub>2</sub>, as shown in
<a href="#e9780486140520_c05.html#int_73"
id="e9780486140520_c05.html_ref_int_73" class="ref_int">Fig. 5.13-3</a>.

The type of curve traced by the spin axis in the region
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub>, depends on the relative values of
<span class="i">y</span> and <span class="i">N.</span> For example, Eq.
5.13–12 can be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0652.jpg](images/e9780486140520_i0652.jpg)

</div>

</div>

and since <span class="i">u</span> is less than 1 between
<span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub>, the sign of
<span class="imageinline">![e9780486140520_i0653.jpg](images/e9780486140520_i0653.jpg)</span>
depends on γ–<span class="i">Nu</span>. If <span class="i">y</span> =
<span class="i">Nu</span><sub>1</sub>, then
<span class="imageinline">![e9780486140520_i0654.jpg](images/e9780486140520_i0654.jpg)</span>
must be zero at the upper bounding circle and positive for 0 greater
than θ<sub>1</sub>, as shown in
<a href="#e9780486140520_c05.html#int_74"
id="e9780486140520_c05.html_ref_int_74" class="ref_int">Fig. 5.13-4</a>.
To obtain the curve of <a href="#e9780486140520_c05.html#int_75"
id="e9780486140520_c05.html_ref_int_75" class="ref_int">Fig. 5.13-5</a>,
<span class="imageinline">![e9780486140520_i0655.jpg](images/e9780486140520_i0655.jpg)</span>
must change sign for some value of <span class="i">u</span> between
<span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub>. Thus for this case, γ −
<span class="i">Nu</span><sub>i</sub> = 0 for
<span class="i">u</span><sub>2</sub> \<
<span class="i">u</span><sub><span class="i">i</span></sub> \<
<span class="i">u</span><sub>1</sub>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0656.jpg](images/e9780486140520_i0656.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_72"
id="e9780486140520_c05.html_int_72" class="label_int"><span
class="b">Fig. 5.13-2</span></a><span class="b">.</span> Cubic equation
representing motion of symmetric gyro.

</div>

</div>

<div class="section2">

<span id="e9780486140520_c05.html_title69"></span>

# <span class="i">Initial conditions</span>

If a gyro or top is started at <span class="i">t</span> = 0 with 0 =
<span class="i">θ</span><sub>0</sub> and
<span class="imageinline">![e9780486140520_i0657.jpg](images/e9780486140520_i0657.jpg)</span>,
the values of the two constants of the system, <span class="i">E</span>
and <span class="i">h</span><sub><span class="i">Z</span></sub> are
found from Eqs. 5.13–12 and 5.13–13, to be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0658.jpg](images/e9780486140520_i0658.jpg)

</div>

</div>

Substituting into Eqs. 5.13–12 and 5.13–13, the equations for the
precession and nutation are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0659.jpg](images/e9780486140520_i0659.jpg)

</div>

<div class="caption">

(5.13–20)

</div>

</div>

These equations both agree with the initial conditions imposed on the
system. The second of the above equations indicates that the right side
of the equation must always be positive, therefore
<span class="i">θ</span><sub>0</sub> must correspond to the highest
elevation of the spin axis, or the upper bounding circle. The lower
bounding circle is found by letting
<span class="imageinline">![e9780486140520_i0660.jpg](images/e9780486140520_i0660.jpg)</span>
= 0 and solving for cos <span class="i">θ</span>. The result is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0661.jpg](images/e9780486140520_i0661.jpg)

</div>

<div class="caption">

(5.13–21)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0662.jpg](images/e9780486140520_i0662.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_73"
id="e9780486140520_c05.html_int_73" class="label_int"><span
class="b">Fig. 5.13-3</span></a><span class="b">.</span> Oscillation
bounded between <span class="i">θ</span><sub>1</sub>, and
<span class="i">θ</span><sub>2</sub> with <span class="i">y</span> \>
<span class="i">Nu</span><sub>1</sub>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0663.jpg](images/e9780486140520_i0663.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_74"
id="e9780486140520_c05.html_int_74" class="label_int"><span
class="b">Fig. 5.13-4</span></a>. Oscillation bounded between
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub> with y =
<span class="i">Nu</span><sub>1</sub>.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0664.jpg](images/e9780486140520_i0664.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_75"
id="e9780486140520_c05.html_int_75" class="label_int"><span
class="b">Fig. 5.13-5</span></a><span class="i"><span class="b">.</span></span>
Oscillation bounded between <span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub> with <span class="i">y</span> =
<span class="i">Nu</span><sub>i</sub>, where
<span class="i">u</span><sub>2</sub> \<
<span class="i">U</span><sub>i</sub> \<
<span class="i">u</span><sub>1</sub>.

</div>

</div>

It can be shown that the sign before the radical must be negative. For
instance, since cos <span class="i">θ</span><sub>0</sub> is less than 1,
the radical is greater than

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0665.jpg](images/e9780486140520_i0665.jpg)

</div>

</div>

Thus if the positive sign is used, this would require that,

<div class="blocktext">

cos <span class="i">θ</span> \> 1

</div>

which is an impossibility. Thus <span class="i">θ</span><sub>2</sub>
corresponding to the lower bounding circle is given by the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0666.jpg](images/e9780486140520_i0666.jpg)

</div>

<div class="caption">

(5.13-21)

</div>

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title70"></span>

# <span class="b">5.14 Steady Precession of a Symmetric Gyro or Top</span>

In the previous section it was shown that the spinning top pivoted about
a fixed point is able to move in such a manner that its axis of symmetry
<span class="i">Oζ</span>, occupies a zone between
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub> corresponding to the roots of
<span class="i">f</span>(<span class="i">u</span>) = 0 at
<span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub>. It is evident then that as
<span class="i">u</span><sub>1</sub> and
<span class="i">u</span><sub>2</sub> approach each other, the annular
zone between <span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub> will narrow until eventually they
merge to a single value
<span class="i">θ</span><sub><span class="i">s</span></sub>, as shown in
<a href="#e9780486140520_c05.html#int_76"
id="e9780486140520_c05.html_ref_int_76" class="ref_int">Fig. 5.14-1</a>.
Physically, this is the angle of steady precession which can be
initiated by the initial conditions, <span class="i">θ</span> =
<span class="i">θ</span><sub><span class="i">s</span></sub>,
<span class="imageinline">![e9780486140520_i0667.jpg](images/e9780486140520_i0667.jpg)</span>,
and
<span class="imageinline">![e9780486140520_i0668.jpg](images/e9780486140520_i0668.jpg)</span>.

The analysis for this special case is probably one of the simplest cases
of the spinning top, which will now be investigated. Although the
problem can be approached mathematically from the two equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0669.jpg](images/e9780486140520_i0669.jpg)

</div>

</div>

it will be more instructive to examine the problem from a physical basis
as follows.

For steady precession,
<span class="imageinline">![e9780486140520_i0670.jpg](images/e9780486140520_i0670.jpg)</span>
, and the angular velocities about the <span class="i">ξ</span>,
<span class="i">η</span>, ζ axes, shown in
<a href="#e9780486140520_c05.html#int_71" class="ref_int">Fig.
5.13-1</a><span class="i">c</span>, are

<div class="blocktext">

ω<sub>ξ</sub> = 0  
<span class="imageinline">![e9780486140520_i0671.jpg](images/e9780486140520_i0671.jpg)</span>  
<span class="imageinline">![e9780486140520_i0672.jpg](images/e9780486140520_i0672.jpg)</span>

</div>

The angular momentum about the corresponding axes are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0673.jpg](images/e9780486140520_i0673.jpg)

</div>

<div class="caption">

(5.14–1)

</div>

</div>

and the moment about the <span class="i">ξ</span> axis becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0674.jpg](images/e9780486140520_i0674.jpg)

</div>

<div class="caption">

(5.14–2)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0675.jpg](images/e9780486140520_i0675.jpg)

</div>

<div class="caption">

(5.14–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0676.jpg](images/e9780486140520_i0676.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_76"
id="e9780486140520_c05.html_int_76" class="label_int"><span
class="b">Fig.</span> <span class="b">5.14-1</span></a><span class="b">.</span>
Steady precession corresponding to <span class="i">u</span><sub>1</sub>
= <span class="i">u</span><sub>2</sub> =
<span class="i">u</span><sub>s</sub>.

</div>

</div>

The two precessional speeds are then given by the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0677.jpg](images/e9780486140520_i0677.jpg)

</div>

<div class="caption">

(5.14–4)

</div>

</div>

provided the spin is great enough to keep the radical of the above
equation positive. This requirement is satisfied if,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0678.jpg](images/e9780486140520_i0678.jpg)

</div>

<div class="caption">

(5.14–5)

</div>

</div>

Further insight to the problem is obtained by plotting
<span class="i">M</span><sub><span class="i">ξ</span></sub> versus
<span class="imageinline">![e9780486140520_i0679.jpg](images/e9780486140520_i0679.jpg)</span>
from Eq. 5.14–2, as shown in <a href="#e9780486140520_c05.html#int_77"
id="e9780486140520_c05.html_ref_int_77" class="ref_int">Fig. 5.14-2</a>.
The curve is a parabola and for any value of
<span class="i">M</span><sub><span class="i">ξ</span></sub> there
correspond two precessional speeds. When
<span class="i">M</span><sub><span class="i">ξ</span></sub> = 0, the
precessional speeds are zero and
<span class="imageinline">![e9780486140520_i0680.jpg](images/e9780486140520_i0680.jpg)</span>
. This value of the precessional speed is given by the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0681.jpg](images/e9780486140520_i0681.jpg)

</div>

<div class="caption">

(5.14–6)

</div>

</div>

which agree with that of the moment–free gyro (see Eq. 5.9–4). The
precessional speed corresponding to the peak moment is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0682.jpg](images/e9780486140520_i0682.jpg)

</div>

<div class="caption">

(5.14–7)

</div>

</div>

and the corresponding peak moment is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0683.jpg](images/e9780486140520_i0683.jpg)

</div>

<div class="caption">

(5.14–8)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0684.jpg](images/e9780486140520_i0684.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_77"
id="e9780486140520_c05.html_int_77" class="label_int"><span
class="b">Fig. 5.14-2</span></a>. Constant moment
<span class="i">M</span><sub><span class="i">ξ</span></sub> results in
two possible precessional speeds
<span class="imageinline">![e9780486140520_i0685.jpg](images/e9780486140520_i0685.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0686.jpg](images/e9780486140520_i0686.jpg)</span>
.

</div>

</div>

For intermediate moment
<span class="i">M</span><sub><span class="i">ξ</span></sub>, the two
precessional speeds
<span class="imageinline">![e9780486140520_i0687.jpg](images/e9780486140520_i0687.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0688.jpg](images/e9780486140520_i0688.jpg)</span>
are referred to as the slow and the fast precession. In general, the
fast precession is not attained due to the high kinetic energy required,
and the precession of a spinning top is usually slow precession.

<div class="section2">

<span id="e9780486140520_c05.html_title71"></span>

# <span class="i">Limiting cases</span>

For
<span class="imageinline">![e9780486140520_i0689.jpg](images/e9780486140520_i0689.jpg)</span>
to be real, it is necessary for the terms under the radical of Eq.
5.14–4 to be greater than zero, or,

<div class="blocktext">

<sub><span class="i">C</span></sub><sup>2</sup><sub><span class="i">n</span></sub><sup>2</sup>
≥ 4<span class="i">WlA</span> cos <span class="i">θ</span>

</div>

If <span class="i">θ</span> = 90°, Eq. 5.14–5 indicates that the minimum
required <span class="i">n</span> is zero. However, Eq. 5.14–4 indicates
<span class="imageinline">![e9780486140520_i0690.jpg](images/e9780486140520_i0690.jpg)</span>that
then is indeterminate. This limiting case can be resolved for
<span class="i">n</span> greater than zero by the elementary
consideration of <a href="#e9780486140520_c05.html#int_78"
id="e9780486140520_c05.html_ref_int_78" class="ref_int">Fig. 5.14-3</a>.
The rate of change of the angular momentum vector
<span class="i">h</span><sub>ζ</sub> <span class="i">= Cn</span>, is
equal to the moment
<span class="i">M</span><sub><span class="i">ξ</span></sub> =
<span class="i">Wl</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0691.jpg](images/e9780486140520_i0691.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0692.jpg](images/e9780486140520_i0692.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_78"
id="e9780486140520_c05.html_int_78" class="label_int"><span
class="b">Fig. 5.14-3</span></a>. Limiting case <span class="i">θ</span>
= 90°.

</div>

</div>

The whirling speed
<span class="imageinline">![e9780486140520_i0693.jpg](images/e9780486140520_i0693.jpg)</span>for
<span class="i">θ</span> = 90° is therefore equal to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0694.jpg](images/e9780486140520_i0694.jpg)

</div>

<div class="caption">

(5.14–9)

</div>

</div>

and as long as <span class="i">n</span> is finite,
<span class="imageinline">![e9780486140520_i0695.jpg](images/e9780486140520_i0695.jpg)</span>
will also remain finite.

The same result can also be obtained from Eq. 5.14–3, for as cos → 0,
the term
<span class="imageinline">![e9780486140520_i0696.jpg](images/e9780486140520_i0696.jpg)</span>
is negligible compared to the other two.

For <span class="i">θ</span> = 0°, the required value of
<span class="i">n</span> from Eq. 5.14–5 must satisfy the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0697.jpg](images/e9780486140520_i0697.jpg)

</div>

<div class="caption">

(5.14–10)

</div>

</div>

in which case we have the sleeping top. Equation 5.14–10 is often used
to determine the spin of a missile or a projectile necessary for
stability. Referring to <a href="#e9780486140520_c05.html#int_79"
id="e9780486140520_c05.html_ref_int_79" class="ref_int">Fig. 5.14-4</a>,
as long as the spin axis <span class="i">Oζ</span> coincides with the
velocity vector of the missile, the drag force will also coincide with
<span class="i">Oζ</span>. However, if the spin axis deviates slightly
from the velocity vector by a small angle <span class="i">θ,</span> the
drag force, which acts at the center of pressure, a distance
<span class="i">/</span> ahead of the center of mass, will have a moment
<span class="i">Rl</span> sin <span class="i">θ</span> about the center
of mass. Thus this problem is identical to that of the sleeping top with
<span class="i">Wl</span> replaced by <span class="i">Rl.</span> The
missile or projectile will hence be stable if the spin is great enough
as established by,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0698.jpg](images/e9780486140520_i0698.jpg)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0699.jpg](images/e9780486140520_i0699.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_79"
id="e9780486140520_c05.html_int_79" class="label_int"><span
class="b">Fig. 5.14-4</span></a>. Spin stabilization of missiles and
projectiles.

</div>

</div>

<span class="b">PROBLEMS</span>

1.  . A symmetrical gyro is mounted on two weightless gimbals. What are
    the expressions for the moment of momentum about the
    <span class="i">ξ</span>, <span class="i">η</span>,
    <span class="i">ζ</span>, and <span class="i">Z</span> axes. Write
    the differential equation for the moment about the above axes.

2.  . For the symmetrical gyro or top, with moment due to gravity,
    determine the equation for the phase plane plot
    <span class="imageinline">![e9780486140520_i0700.jpg](images/e9780486140520_i0700.jpg)</span>
    versus <span class="i">u,</span> and express the equation for the
    period of nutation in terms of,
    <span class="i">ƒ</span>(<span class="i">u</span>).

3.  . The condition for the sleeping top, <span class="i">u</span> = cos
    0° = 1, can be satisfied by either of the curves shown below. Show
    that (<span class="i">a</span>) is stable and
    (<span class="i">b</span>) is unstable by considering a small
    variation of the curves as indicated by the dotted lines.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0701.jpg](images/e9780486140520_i0701.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 3</span>

    </div>

    </div>

4.  . If the stability of the sleeping top is indicated by
    (<span class="i">a</span>) in the Fig. for Prob. 3, deduce the
    relationship
    <span class="imageinline">![e9780486140520_i0702.jpg](images/e9780486140520_i0702.jpg)</span>
    by noting that,
    <div class="blocktext">

    <span class="i">u</span> = 1
    <span class="i">ƒ</span>(<span class="i">u</span>)
    <span class="i">=</span> (−<span class="i">θ</span> sin
    <span class="i">θ</span>)<sup>2</sup> = 0

    </div>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0703.jpg](images/e9780486140520_i0703.jpg)

    </div>

    </div>

5.  . Show that the equation for the steady precession of a top can be
    written as
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0704.jpg](images/e9780486140520_i0704.jpg)

    </div>

    </div>

6.  . Show that for large <span class="i">n</span>, the lower and higher
    precessional speeds become
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0705.jpg](images/e9780486140520_i0705.jpg)

    </div>

    </div>

    Why is the lower precessional speed independent of
    <span class="i">θ</span>?

7.  . For steady precession, show that the angle between the momentum
    vector h and the spin axis is given by the equation,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0706.jpg](images/e9780486140520_i0706.jpg)

    </div>

    </div>

    where the minus sign must be used for the slow precession.

8.  . Show that for large <span class="i">n</span>, the angle
    <span class="i">α</span> corresponding to the slow and fast
    precessional speeds are,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0707.jpg](images/e9780486140520_i0707.jpg)

    </div>

    </div>

9.  . What is the expression for α corresponding to the minimum value of
    <span class="i">n</span> consistent with steady precession?

10. . Determine the conditions necessary for small oscillation of the
    spin axis of a gyro, between two annular circles
    <span class="i">θ</span><sub>1</sub> and
    <span class="i">θ</span><sub>2</sub>, such that
    <span class="imageinline">![e9780486140520_i0708.jpg](images/e9780486140520_i0708.jpg)</span>is
    the same at the two circles.

11. . The end of the spin axis of a top spinning about a fixed pivot
    describes on a sphere the curve shown. If
    <span class="i">Cn/A</span> = <span class="i">N</span> is given,
    determine the following quantities in terms of
    <span class="i">N</span>.

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0709.jpg](images/e9780486140520_i0709.jpg)

    </div>

    <div class="caption">

    (<span class="i">a</span>)

    </div>

    </div>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0710.jpg](images/e9780486140520_i0710.jpg)

    </div>

    <div class="caption">

    (<span class="i">b</span>)

    </div>

    </div>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0711.jpg](images/e9780486140520_i0711.jpg)

    </div>

    <div class="caption">

    (<span class="i">c</span>)

    </div>

    </div>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0712.jpg](images/e9780486140520_i0712.jpg)

    </div>

    <div class="caption">

    (<span class="i">d</span>)

    </div>

    </div>

    Show in general that a motion with the sharp cusp at
    <span class="i">θ</span><sub>2</sub> \>
    <span class="i">θ</span><sub>1</sub> cannot take place.

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0713.jpg](images/e9780486140520_i0713.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 11</span>

    </div>

    </div>

12. . A thin disk of radius r and mass <span class="i">m</span> has a
    stem of length <span class="i">a</span> which is pinned to a
    vertical shaft as shown. Show that if <span class="i">r</span> \<
    2<span class="i">a</span>, it will be unstable if
    <span class="imageinline">![e9780486140520_i0714.jpg](images/e9780486140520_i0714.jpg)</span>
    . Show also that it will be stable at all
    <span class="imageinline">![e9780486140520_i0715.jpg](images/e9780486140520_i0715.jpg)</span>if
    <span class="i">r</span> \> 2<span class="i">a</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0716.jpg](images/e9780486140520_i0716.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 12</span>

    </div>

    </div>

13. . A flywheel with axes <span class="i">x</span>,
    <span class="i">y</span>, <span class="i">z</span> has moment of
    inertia <span class="i">I</span><sub>x</sub>,
    <span class="i">I</span><sub><span class="i">y</span></sub> =
    <span class="i">I</span><sub>z</sub>, and is spinning with high
    speed <span class="i">ω.</span> If it is oscillating in pitch and
    yaw with the center of gravity stationary, set up the equations of
    motion with restraining moments equal to
    <span class="i">K</span><sub><span class="i">p</span></sub><span class="i">θ</span>
    in pitch and
    <span class="i">K</span><sub><span class="i">y</span></sub><span class="i">Ψ</span>
    in yaw.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0717.jpg](images/e9780486140520_i0717.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 13</span>

    </div>

    </div>

14. . The ore crusher wheel of weight <span class="i">W</span> and
    radius R has moments of inertia <span class="i">C</span> and
    <span class="i">A</span> about its polar axis and an axis through
    <span class="i">O</span> parallel to the diametric axes. The spin
    axis <span class="i">z</span> on which the crusher wheel is free to
    rotate, precesses at speed
    <span class="imageinline">![e9780486140520_i0718.jpg](images/e9780486140520_i0718.jpg)</span>
    about the vertical <span class="i">OZ</span> axis.
    - (<span class="i">a</span>) show that the spin velocity of the
      wheel with respect to the axle is
      <div class="illustype_image_math">

      <div class="image_math">

      ![e9780486140520_i0719.jpg](images/e9780486140520_i0719.jpg)

      </div>

      </div>
    - (<span class="i">b</span>) Show that the velocity of the center of
      the wheel is equal to
      <span class="imageinline">![e9780486140520_i0720.jpg](images/e9780486140520_i0720.jpg)</span>
      <div class="illustype_image_text">

      <div class="image_text">

      ![e9780486140520_i0721.jpg](images/e9780486140520_i0721.jpg)

      </div>

      <div class="caption">

      <span class="b">Prob. 14</span>

      </div>

      </div>

15. . For the ore crusher of Prob. 14, write the equation for the moment
    about the pin <span class="i">O</span>, and show that the normal
    force between the wheel and the inclined track is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0722.jpg](images/e9780486140520_i0722.jpg)

    </div>

    </div>

16. . From the result of Prob. 15, show that the crushing force
    <span class="i">F</span> has a maximum or minimum between
    <span class="i">θ</span> = 45° and 90°, or between
    <span class="i">θ</span> = 135° and 180°. Since the force due to
    gravity is a maximum at <span class="i">θ</span> = 90°, we can
    reason that the maximum occurs for <span class="i">θ</span> = 45° to
    90°, or actually between 0° and 45° with the horizontal. Determine
    the optimum axle tilt above the horizontal for a crusher of the
    following dimensions.
    <div class="blocktext">

    <span class="i">R</span> = 18 in. <span class="i">l</span> = 3 ft
    (from center plane of wheel  
    to pin O)  
    <span class="i">b</span> = 12 in.
    <span class="imageinline">![e9780486140520_i0723.jpg](images/e9780486140520_i0723.jpg)</span>

    </div>

17. . Determine the velocity and acceleration of the top of the crusher
    wheel for the dimensions given in Prob. 16.

18. . The general equation for the symmetrical gyro is given by Eq.
    5.13–18. Show that
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0724.jpg](images/e9780486140520_i0724.jpg)

    </div>

    </div>

19. . For steady precession
    <span class="imageinline">![e9780486140520_i0725.jpg](images/e9780486140520_i0725.jpg)</span>
    , which requires that
    <span class="i">ƒ</span>(<span class="i">u</span>) =
    <span class="i">ƒ</span>′(<span class="i">u</span>) = 0. From these
    two equations show that the steady precession is defined by the
    quadratic,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0726.jpg](images/e9780486140520_i0726.jpg)

    </div>

    </div>

    with the following restriction
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0727.jpg](images/e9780486140520_i0727.jpg)

    </div>

    </div>

20. . A gyro of weight <span class="i">mg</span>, spinning with angular
    speed <span class="i">n</span> is tied to a string of length
    <span class="i">l</span><sub>1</sub> and precesses around the
    vertical axis with constant speed Ω. If <span class="i">C</span> and
    <span class="i">A</span> are moments of inertia about the spin axis
    and its normal through the center of mass, determine the three
    equations of motion.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0728.jpg](images/e9780486140520_i0728.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob</span>. <span class="b">20</span>

    </div>

    </div>

21. . The outer frame of a toy gyro is symmetric about the three axes
    through its geometric center, and has a moment of inertia
    <span class="i">C</span><sub>2</sub>. If when the rotor is spinning
    with speed
    <span class="imageinline">![e9780486140520_i0729.jpg](images/e9780486140520_i0729.jpg)</span>
    , the outer frame also spins at a different speed
    <span class="imageinline">![e9780486140520_i0730.jpg](images/e9780486140520_i0730.jpg)</span>
    in the same direction, write the new momentum and moment equations
    for steady precession.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0731.jpg](images/e9780486140520_i0731.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 21</span>

    </div>

    </div>

22. . If the outer frame of the toy gyro is a single ring in one plane,
    the moment of inertia about an axis normal to the plane of the ring
    will be 2<span class="i">C</span><sub>2</sub>. How does this affect
    the equations of Prob. 21 ?

</div>

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title72"></span>

# <span class="b">5.15 Precession and Nutation of the Earth’s Polar Axis</span>

In Sec. 4.18, we derived the equations for the moment exerted by the
earth, due to its oblateness, on a satellite revolving around the earth.
According to Newton’s third law, the satellite must exert an equal and
opposite moment on the earth, but, due to the large mass of the earth in
comparison to that of the satellite, its effect is measurable only on
the satellite motion.

The moment equations from Sec. 4.18, with opposite signs for moment
exerted by the satellite on earth, are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0732.jpg](images/e9780486140520_i0732.jpg)

</div>

<div class="caption">

(5.15–1)

</div>

</div>

These equations apply to any two bodies oriented as in Sec. 4.18, and,
therefore, are applicable to the sun and earth, or the moon and earth.
The fact that the earth’s polar axis is inclined from the normal to the
plane of the ecliptic by 23° 27’ results in a moment exerted by the sun
on the earth as shown in <a href="#e9780486140520_c05.html#int_80"
id="e9780486140520_c05.html_ref_int_80" class="ref_int">Fig. 5.15-1</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0733.jpg](images/e9780486140520_i0733.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_80"
id="e9780486140520_c05.html_int_80" class="label_int"><span
class="b">Fig. 5.15-1</span></a><span class="b">.</span> Moments
<span class="i">M</span><sub>x</sub> and
<span class="i">M</span><sub>y</sub> exerted by sun on earth.

</div>

</div>

The angular momentum vector of the spinning earth is
<span class="i">C</span>Ω, and the moment
<span class="i">M</span><sub>y</sub> causes the end of the vector
<span class="i">C</span>Ω to move in the same direction and, therefore,
change the angle <span class="i">θ</span>. Since
<span class="i">M</span><sub><span class="i">y</span></sub> is
oscillatory with net result per cycle equal to zero, its effect is to
produce an oscillatory nutation of zero net angle per cycle.

The moment <span class="i">M</span><sub>x</sub> is oscillatory but
cumulative along the negative <span class="i">x</span> axis, which
requires a net precession per cycle. Letting
<span class="imageinline">![e9780486140520_i0734.jpg](images/e9780486140520_i0734.jpg)</span>
be the precession rate normal to the plane of the ecliptic, the
component
<span class="imageinline">![e9780486140520_i0735.jpg](images/e9780486140520_i0735.jpg)</span>
sin <span class="i">θ</span> along the negative <span class="i">y</span>
direction will rotate the angular momentum vector
<span class="i">C</span>Ω in the direction
<span class="i">M</span><sub><span class="i">x</span></sub> to give

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0736.jpg](images/e9780486140520_i0736.jpg)

</div>

<div class="caption">

(5.15–2)

</div>

</div>

The precession rate from Eq. 5.15–1 is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0737.jpg](images/e9780486140520_i0737.jpg)

</div>

<div class="caption">

(5.15–3)

</div>

</div>

The quantity
<span class="i">Km</span><sub><span class="i">s</span></sub>/<span class="i">m</span>
= <span class="i">Gm</span><sub><span class="i">s</span></sub> in this
equation, where
<span class="i">m</span><sub><span class="i">s</span></sub> and
<span class="i">m</span> are the mass of the sun and earth respectively,
can be eliminated from the equation of the central force between the sun
and the earth as follows.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0738.jpg](images/e9780486140520_i0738.jpg)

</div>

<div class="caption">

(5.15–4)

</div>

</div>

Also the average value of sin<sup>2</sup> <span class="i">ϕ</span> for 0
≤ ϕ ≤ 2<span class="i">π</span> is ½, so that the average precession
rate per year due to the sun is given by the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0739.jpg](images/e9780486140520_i0739.jpg)

</div>

<div class="caption">

(5.15–5)

</div>

</div>

where Ω is the spin rate (relative to inertial space) of the earth,
<span class="i">τ</span> is the period of the earth around the sun,
<span class="i">θ</span> = 23° 27’, and
(<span class="i">C</span>–<span class="i">A</span>)/<span class="i">C</span>
= 0.0032 for the oblateness of the earth.

Equation 5.15–3 applies also to the earth–moon system, where
<span class="i">m</span><sub><span class="i">s</span></sub> now becomes
the mass of the moon. However, in eliminating the quantity
<span class="i">Km</span><sub><span class="i">s</span></sub><span class="i">/ma</span><sup>3</sup><span class="i">,</span>
the attractive force between the earth and moon given by Eq. 4.6–4 must
be used as follows.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0740.jpg](images/e9780486140520_i0740.jpg)

</div>

<div class="caption">

(5.15–6)

</div>

</div>

Thus
(<span class="i">Km</span><sub><span class="i">s</span></sub>/<span class="i">ma</span><sup>3</sup>)
=
\[<span class="i">m</span><sub><span class="i">s</span></sub>/(<span class="i">m</span> +
<span class="i">m</span><sub><span class="i">s</span></sub>)\](2<span class="i">π</span>/<span class="i">τ</span>)<sup>2</sup>
and the equation for the average precession rate of the earth’s polar
axis per revolution of the moon around the earth becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0741.jpg](images/e9780486140520_i0741.jpg)

</div>

<div class="caption">

(5.15–7)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  <span class="b">.</span> The earth’s spin rate is Ω =
    2<span class="i">π</span> × 366.25 rad/year. Show that the earth’s
    polar axis precesses 0.0000765 rad/year due to the sun.
2.  . The mass of the moon is
    <span class="imageinline">![e9780486140520_i0742.jpg](images/e9780486140520_i0742.jpg)</span>
    that of earth, and its period is 27.32 days. Its orbit plane
    <span class="i">θ</span> varies between 18° 19’ and 28° 35’, with an
    average value of 23° 27’. Determine the precession of the earth’s
    polar axis per year due to the moon. Determine the combined
    precession due to the sun and moon and show that the period of the
    precession of the earth’s axis is approximately 26,000 years.
3.  Consider the earth and moon alone with the moon’s orbit plane
    inclined from the Earth’s equatorial plane by an average of 23° 27’.
    Determine the period of regression of the moon’s node and show that
    its period is approximately 18 yrs.

</div>

<div class="section1">

<span id="e9780486140520_c05.html_title73"></span>

# <span class="b">5.16 General Motion of a Rigid Body</span>

So far we have considered problems in which the motion about the center
of mass or a fixed point can be determined independently by the moment
equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0743.jpg](images/e9780486140520_i0743.jpg)

</div>

<div class="caption">

(5.16–1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0744.jpg](images/e9780486140520_i0744.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_81"
id="e9780486140520_c05.html_int_81" class="label_int"><span
class="b">Fig. 5.16-1</span></a>. Rolling of a thin disk on a plane.

</div>

</div>

However in the more general type of motion the force

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0745.jpg](images/e9780486140520_i0745.jpg)

</div>

<div class="caption">

(5.16–2)

</div>

</div>

may contribute to the moment <span class="b">M</span> and the two
equations are no longer independent. With each of the above equations
resolved into three components, we have in general six interrelated
equations which must be solved simultaneously. Such problems are, of
course, more difficult to solve; however, the general procedure can be
illustrated by the following simple problems.

<div class="section2">

<span id="e9780486140520_c05.html_title74"></span>

# <span class="i">Rolling of a thin circular disk on a rough horizontal plane</span>

The configuration of the rolling disk is shown in
<a href="#e9780486140520_c05.html#int_81"
id="e9780486140520_c05.html_ref_int_81" class="ref_int">Fig. 5.16-1</a>.
We will use two sets of axes with origin coinciding with the center of
the disk; the <span class="i">X,</span> Y, <span class="i">Z</span> axes
with fixed direction, and the <span class="i">ξ</span>,
<span class="i">η</span>, <span class="i">ζ</span> axes moving with the
disk. Then <span class="i">ζ</span> axis is normal to the plane of the
disk, and the <span class="i">ξ</span>, <span class="i">η</span> axes
are in the plane of the disk witch <span class="i">ξ</span> along the
horizontal. It is convenient to introduce the <span class="i">η</span>′
axis so that <span class="i">ξ, η’</span>, <span class="i">Z</span> form
a third set rotated from the <span class="i">X, Y, Z</span> axes about
the <span class="i">Z</span> axis. The <span class="i">η′</span> axis so
defined is the horizontal projection of axis <span class="i">η</span>.
The orientation of then <span class="i">ζ</span> and
<span class="i">ξ</span> axes are defined by the rotation
<span class="i">θ</span> about then <span class="i">ξ</span> axis for
<span class="i">ζ</span>, and a rotation <span class="i">ψ</span> about
the <span class="i">Z</span> axis for <span class="i">ξ</span>.

The constraint force of the floor consists of the normal reaction
<span class="i">ƒ</span><sub><span class="i">Z</span></sub>, and a
friction force <span class="i">ƒ,</span> which is resolved into
components <span class="i">ƒ</span><sub><span class="i">ξ</span></sub>
and <span class="i">ƒ</span><sub><span class="i">η′</span></sub>
parallel and perpendicular to the <span class="i">ξ</span> axis.

With <span class="i">A, A, C</span> as moments of inertia about the
<span class="i">ξ</span>, <span class="i">η</span>,
<span class="i">ζ</span>, axes respectively, and
<span class="i">R</span> as the radius of the disk, the moment equations
are;

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0746.jpg](images/e9780486140520_i0746.jpg)

</div>

<div class="caption">

(5.16–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0747.jpg](images/e9780486140520_i0747.jpg)

</div>

<div class="caption">

(5.16–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0748.jpg](images/e9780486140520_i0748.jpg)

</div>

<div class="caption">

(5.16–5)

</div>

</div>

where
<span class="imageinline">![e9780486140520_i0749.jpg](images/e9780486140520_i0749.jpg)</span>
in the negative <span class="i">ζ</span> direction.

Equation 5.16–4 can be rearranged as follows,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0750.jpg](images/e9780486140520_i0750.jpg)

</div>

<div class="caption">

(5.16–6)

</div>

</div>

which indicates that, if
<span class="imageinline">![e9780486140520_i0751.jpg](images/e9780486140520_i0751.jpg)</span>
is negative (i.e., disk falling), then
<span class="imageinline">![e9780486140520_i0752.jpg](images/e9780486140520_i0752.jpg)</span>
increases, or the spin about the vertical <span class="i">Z</span> axis
increases, and the disk rolls into a tighter circle.

We assume no slipping of the disk relative to the floor, in which case
the velocity of the disk center has the following components.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0753.jpg](images/e9780486140520_i0753.jpg)

</div>

<div class="caption">

(5.16–7)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0754.jpg](images/e9780486140520_i0754.jpg)

</div>

<div class="caption">

(5.16–8)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0755.jpg](images/e9780486140520_i0755.jpg)

</div>

<div class="caption">

(5.16–9)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0756.jpg](images/e9780486140520_i0756.jpg)

</div>

<div class="caption">

(5.16–10)

</div>

</div>

which are shown in <a href="#e9780486140520_c05.html#int_82"
id="e9780486140520_c05.html_ref_int_82" class="ref_int">Fig. 5.16-2</a>.
The force equation can then be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0757.jpg](images/e9780486140520_i0757.jpg)

</div>

<div class="caption">

(5.16–11)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0758.jpg](images/e9780486140520_i0758.jpg)

</div>

<div class="caption">

(5.16–12)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0759.jpg](images/e9780486140520_i0759.jpg)

</div>

<div class="caption">

(5.16–13)

</div>

</div>

Equations 5.16–3, 5.16–4, 5.16–5 and 5.16–11, 5.16–12, 5.16–13 are the
six component equations which must be solved simultaneously. However
these equations have simple solutions only for certain special
conditions which are;

<div class="tableau">

|  |  |
|:---|:---|
| <span class="i">θ</span> ≅ 90° | and <span class="i">ω</span><sub><span class="i">ζ</span></sub> large |
| <span class="i">θ ≅</span> 90° | and <span class="i">ω</span><sub><span class="i">ζ</span></sub> → 0,<span class="imageinline">![e9780486140520_i0761.jpg](images/e9780486140520_i0761.jpg)</span> large |
| <span class="i">θ</span> ≅ 0° | and <span class="i">ω</span><sub><span class="i">ζ</span></sub> small,<span class="imageinline">![e9780486140520_i0762.jpg](images/e9780486140520_i0762.jpg)</span> large |

</div>

The first case represents a rolling of the disk with its plane nearly
vertical; the second case corresponds to the upright spinning of the
disk about its vertical diameter; and the last case represents the disk
spinning with its face nearly horizontal.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0763.jpg](images/e9780486140520_i0763.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c05.html#ref_int_82"
id="e9780486140520_c05.html_int_82" class="label_int"><span
class="b">Fig. 5.16-2</span></a>. Components of velocity.

</div>

</div>

</div>

<div class="section2">

<span id="e9780486140520_c05.html_title75"></span>

# <span class="i">Rolling of a disk with plane of the disk nearly vertical</span>

Consider the disk rolling with the plane of the disk nearly vertical.
Here the angular velocities
<span class="imageinline">![e9780486140520_i0764.jpg](images/e9780486140520_i0764.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0765.jpg](images/e9780486140520_i0765.jpg)</span>
will be small in comparison with
<span class="i">ω</span><sub><span class="i">ζ</span></sub>. Also sin
<span class="i">θ</span> ≅ 1, and cos <span class="i">θ</span> =
<span class="i">α</span>, where <span class="i">α</span> is the
complimentary angle <span class="i">α</span> =
(<span class="i">π</span>/2) − <span class="i">θ</span>. We can
therefore replace
<span class="imageinline">![e9780486140520_i0766.jpg](images/e9780486140520_i0766.jpg)</span>
and 6 by −
<span class="imageinline">![e9780486140520_i0767.jpg](images/e9780486140520_i0767.jpg)</span>
and −
<span class="imageinline">![e9780486140520_i0768.jpg](images/e9780486140520_i0768.jpg)</span>
respectively. The force and moment equations can then be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0769.jpg](images/e9780486140520_i0769.jpg)

</div>

<div class="caption">

(5.16–14)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0770.jpg](images/e9780486140520_i0770.jpg)

</div>

<div class="caption">

(5.16–15)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0771.jpg](images/e9780486140520_i0771.jpg)

</div>

<div class="caption">

(5.16–16)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0772.jpg](images/e9780486140520_i0772.jpg)

</div>

<div class="caption">

(5.16–17)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0773.jpg](images/e9780486140520_i0773.jpg)

</div>

<div class="caption">

(5.16–18)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0774.jpg](images/e9780486140520_i0774.jpg)

</div>

<div class="caption">

(5.16–19)

</div>

</div>

From Eqs. 5.16–14 and 5.16–17, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0775.jpg](images/e9780486140520_i0775.jpg)

</div>

</div>

Therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0776.jpg](images/e9780486140520_i0776.jpg)

</div>

<div class="caption">

(5.16–20)

</div>

</div>

With the initial conditions
<span class="imageinline">![e9780486140520_i0777.jpg](images/e9780486140520_i0777.jpg)</span>
, and <span class="i">α</span> = 0 (i.e., disk started in a straight
path with its plane vertical), we integrate Eq. 5.16–15 to obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0778.jpg](images/e9780486140520_i0778.jpg)

</div>

<div class="caption">

(5.16–21)

</div>

</div>

We next substitute Eqs. 5.16–18, 5.16–19, and 5.16–21 into Eq. 5.16–16
and obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0779.jpg](images/e9780486140520_i0779.jpg)

</div>

<div class="caption">

(5.16–22)

</div>

</div>

This equation indicates that the plane of the disk wobbles in and out of
the vertical, provided the spin is great enough to satisfy the
inequality,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0780.jpg](images/e9780486140520_i0780.jpg)

</div>

<div class="caption">

(5.16–23)

</div>

</div>

Equation 5.16–21 also indicates that
<span class="imageinline">![e9780486140520_i0781.jpg](images/e9780486140520_i0781.jpg)</span>
is proportional to <span class="i">α,</span> and hence the precession
also wobbles sinusoidally. The disk then rolls in a wavy line which is
nearly straight.

</div>

<div class="section2">

<span id="e9780486140520_c05.html_title76"></span>

# <span class="i">Upright spinning of the disk</span>

We next consider the case where the main motion of the disk is a spin
about the vertical axis. Due to some disturbance, the disk will move in
a small circle, but it is evident that
<span class="i">ω</span><sub><span class="i">ζ</span></sub> will be
small and
<span class="imageinline">![e9780486140520_i0782.jpg](images/e9780486140520_i0782.jpg)</span>
large. <span class="i">θ</span> will, however, remain nearly 90°, so
that again sin <span class="i">θ</span> ≅ 1 and cos
<span class="i">θ</span> ≅ <span class="i">α</span>, where
<span class="i">α</span> is a small angle.

With these approximations, the moment and force equations become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0783.jpg](images/e9780486140520_i0783.jpg)

</div>

<div class="caption">

(5.16–24)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0784.jpg](images/e9780486140520_i0784.jpg)

</div>

<div class="caption">

(5.16–25)

</div>

</div>

Therefore
<span class="imageinline">![e9780486140520_i0785.jpg](images/e9780486140520_i0785.jpg)</span>
= constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0786.jpg](images/e9780486140520_i0786.jpg)

</div>

<div class="caption">

(5.16–26)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0787.jpg](images/e9780486140520_i0787.jpg)

</div>

<div class="caption">

(5.16–27)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0788.jpg](images/e9780486140520_i0788.jpg)

</div>

<div class="caption">

(5.16–28)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0789.jpg](images/e9780486140520_i0789.jpg)

</div>

<div class="caption">

(5.16–29)

</div>

</div>

From Eqs. 5.16–24 and 5.16–27, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0790.jpg](images/e9780486140520_i0790.jpg)

</div>

<div class="caption">

(5.16–30)

</div>

</div>

With initial values of
<span class="i">ω</span><sub><span class="i">ζ</span></sub> and
<span class="i">α</span> equal to zero, we integrate the above equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0791.jpg](images/e9780486140520_i0791.jpg)

</div>

<div class="caption">

(5.16–31)

</div>

</div>

Substituting Eqs. 5.16–28, 5.16–29, and 5.16–31 into Eq. 5.16–26, the
final equation becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0792.jpg](images/e9780486140520_i0792.jpg)

</div>

<div class="caption">

(5.16–32)

</div>

</div>

Interpreting this equation, the spinning motion is stable as long as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0793.jpg](images/e9780486140520_i0793.jpg)

</div>

<div class="caption">

(5.16–33)

</div>

</div>

With this inequality satisfied, the disk oscillates sinusoidally with a
small angle <span class="i">α</span> about the <span class="i">ξ</span>
axis which is spinning around the vertical axis with speed
<span class="imageinline">![e9780486140520_i0794.jpg](images/e9780486140520_i0794.jpg)</span>
.

</div>

<div class="section2">

<span id="e9780486140520_c05.html_title77"></span>

# <span class="i">Disk spinning nearly horizontally</span>

Spin a coin about a vertical line and watch its final stages when the
plane of the coin is nearly horizontal. You will be able to detect from
the sound that the frequency increases very rapidly during the last
stage of oscillation. You can also observe that the point of contact
with the table spins around a circle of diameter nearly equal to that of
the coin, and that
<span class="i">ω</span><sub><span class="i">ζ</span></sub> is very
small (i.e., the face on the coin is rotating very slowly). Then
<span class="i">ζ</span> axis is nearly vertical so that
<span class="i">θ</span> is very small. However, the end of then
<span class="i">ζ</span> axis is precessing around the vertical very
rapidly so that
<span class="imageinline">![e9780486140520_i0795.jpg](images/e9780486140520_i0795.jpg)</span>
is very large.

With these assumptions, the moment and force equations become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0796.jpg](images/e9780486140520_i0796.jpg)

</div>

<div class="caption">

(5.16–34)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0797.jpg](images/e9780486140520_i0797.jpg)

</div>

<div class="caption">

(5.16–35)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0798.jpg](images/e9780486140520_i0798.jpg)

</div>

<div class="caption">

(5.16–36)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0799.jpg](images/e9780486140520_i0799.jpg)

</div>

<div class="caption">

(5.16–37)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0800.jpg](images/e9780486140520_i0800.jpg)

</div>

<div class="caption">

(5.16–38)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0801.jpg](images/e9780486140520_i0801.jpg)

</div>

<div class="caption">

(5.16–39

</div>

</div>

From Eqs. 5.16–34 and 5.16–37 we find that
<span class="i">ω</span><sub><span class="i">ζ</span></sub> must be a
constant.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0802.jpg](images/e9780486140520_i0802.jpg)

</div>

<div class="caption">

(5.16–40)

</div>

</div>

From Eq. 5.16–35 we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0803.jpg](images/e9780486140520_i0803.jpg)

</div>

<div class="caption">

(5.16–41)

</div>

</div>

Integrating with initial conditions
<span class="imageinline">![e9780486140520_i0804.jpg](images/e9780486140520_i0804.jpg)</span>
and <span class="i">θ</span><sub>0</sub>, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0805.jpg](images/e9780486140520_i0805.jpg)

</div>

</div>

Therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0806.jpg](images/e9780486140520_i0806.jpg)

</div>

<div class="caption">

(5.16–42)

</div>

</div>

Substituting Eqs. 5.16–38, 5.16–39, and 5.16–42 into Eq. 5.16–36, we
arrive at the differential equation for <span class="i">θ</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0807.jpg](images/e9780486140520_i0807.jpg)

</div>

<div class="caption">

(5.16–43)

</div>

</div>

Due to <span class="i">θ</span> and <span class="i">θ</span><sup>3</sup>
in the denominator, the acceleration
<span class="imageinline">![e9780486140520_i0808.jpg](images/e9780486140520_i0808.jpg)</span>
increases as <span class="i">θ</span> approaches zero. Equation 5.16–42
indicates that the precession also increases to infinity as
<span class="i">θ</span> goes to zero.

<span class="b">PROBLEMS</span>

1.  . Determine the least spin about a vertical axis for a 50–cent coin
    by making the necessary measurements.
2.  . Determine the equation for the least spin about the vertical
    diameter of a circular hoop of radius <span class="i">R</span>.
    Compare with that of a solid disk of same radius.
3.  . Determine the least rolling velocity of a 50–cent coin.
4.  . Determine the least rolling velocity of a circular hoop of radius
    <span class="i">R</span>.
5.  . With <span class="i">υ</span><sub><span class="i">ξ</span></sub>,
    <span class="i">υ</span><sub><span class="i">η</span>′</sub>,
    <span class="i">υ</span><sub><span class="i">Z</span></sub> given as
    in <a href="#e9780486140520_c05.html#int_82" class="ref_int">Fig.
    5.16-2</a>, verify the accelerations of Eqs. 5.16–11, 5.16–12,
    5.16–13 as
    <span class="imageinline">![e9780486140520_i0809.jpg](images/e9780486140520_i0809.jpg)</span>
    where the components of <span class="i">ω</span> are
    <span class="i">ω</span><sub><span class="i">ξ</span></sub> =
    <span class="i">θ</span>,
    <span class="i">ω</span><sub><span class="i">η′</span></sub> = 0,
    and
    <span class="imageinline">![e9780486140520_i0810.jpg](images/e9780486140520_i0810.jpg)</span>
    .

</div>

</div>

</div>

<span id="e9780486140520_c06.html"></span>

<div class="chapter">

<span id="e9780486140520_c06.html_title78"></span>

# <span class="b">CHAPTER 6</span>

# <span class="b">Dynamics of Gyroscopic Instruments</span>

<div class="section1">

<span id="e9780486140520_c06.html_title79"></span>

# <span class="b">6.1 Small Oscillations of Gyros</span>

If the gyro or top of
<a href="#e9780486140520_c05.html#int_71" class="ref_int">Fig.
5.13-1</a> is given a slight disturbance from its steady state, we can
show that the oscillations about the steady values will be harmonic.

We can begin with Eqs. 5.13–4, which are the moment equations about the
node system coordinates shown in
<a href="#e9780486140520_c06.html#int_83"
id="e9780486140520_c06.html_ref_int_83" class="ref_int">Fig. 6.1-1</a>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0811.jpg](images/e9780486140520_i0811.jpg)

</div>

<div class="caption">

(6.1–1)

</div>

</div>

Letting the steady–state values of <span class="i">6</span> and
<span class="imageinline">![e9780486140520_i0812.jpg](images/e9780486140520_i0812.jpg)</span>
be <span class="i">θ</span><sub>0</sub> and
<span class="imageinline">![e9780486140520_i0813.jpg](images/e9780486140520_i0813.jpg)</span>
, and designating the deviations about the steady values by
<span class="i">θ</span><sub>∼</sub> and
<span class="imageinline">![e9780486140520_i0814.jpg](images/e9780486140520_i0814.jpg)</span>
, the instantaneous values of <span class="i">θ</span> and
<span class="imageinline">![e9780486140520_i0815.jpg](images/e9780486140520_i0815.jpg)</span>
are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0816.jpg](images/e9780486140520_i0816.jpg)

</div>

</div>

For small oscillations we can make the following approximations.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0817.jpg](images/e9780486140520_i0817.jpg)

</div>

</div>

Substituting these expressions into the second of Eq. 6.1–1 and
neglecting products and squares of the small deviations, we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0818.jpg](images/e9780486140520_i0818.jpg)

</div>

<div class="caption">

(6.1–2)

</div>

</div>

Integrating,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0819.jpg](images/e9780486140520_i0819.jpg)

</div>

<div class="caption">

(6.1–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0820.jpg](images/e9780486140520_i0820.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_83"
id="e9780486140520_c06.html_int_83" class="label_int"><span
class="b">Fig. 6.1-1</span></a> Angular momentum along node system
coordinates.

</div>

</div>

Likewise, from the first of Eq. 6.1–1, we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0821.jpg](images/e9780486140520_i0821.jpg)

</div>

<div class="caption">

(6.1–4)

</div>

</div>

However, for steady precession
<span class="imageinline">![e9780486140520_i0822.jpg](images/e9780486140520_i0822.jpg)</span>
is zero, and the steady components of Eq. 6.1–4 are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0823.jpg](images/e9780486140520_i0823.jpg)

</div>

</div>

Thus by striking out these terms in Eq. 6.1–4 and introducing Eq. 6.1–3
to eliminate
<span class="imageinline">![e9780486140520_i0824.jpg](images/e9780486140520_i0824.jpg)</span>
, we arrive at the second–order differential equation in
<span class="i">θ</span><sub>∼</sub>:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0825.jpg](images/e9780486140520_i0825.jpg)

</div>

<div class="caption">

(6.1–5)

</div>

</div>

The nodding oscillations are therefore sinusoidal with period equal to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0826.jpg](images/e9780486140520_i0826.jpg)

</div>

<div class="caption">

(6.1–6)

</div>

</div>

If <span class="i">n</span> is very large, the nutation period reduces
to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0827.jpg](images/e9780486140520_i0827.jpg)

</div>

<div class="caption">

(6.1–7)

</div>

</div>

The precession period is also the same since, from Eq. 6.1–3,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0828.jpg](images/e9780486140520_i0828.jpg)

</div>

<div class="caption">

(6.1–8)

</div>

</div>

and
<span class="imageinline">![e9780486140520_i0829.jpg](images/e9780486140520_i0829.jpg)</span>
is proportional to <span class="i">θ</span><sub>∼</sub>.

When cos <span class="i">θ</span><sub>0</sub> = 1, we have the sleeping
top and, in order for the denominator of Eq. 6.1–6 to be real,
(<span class="i">Cn</span>)<sup>2</sup> must be greater than
4<span class="i">AWl.</span> Thus, again, we verify the stability
requirement for the sleeping top, which is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0830.jpg](images/e9780486140520_i0830.jpg)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title80"></span>

# <span class="b">6.2 Oscillations About Gimbal Axes</span>

<a href="#e9780486140520_c06.html#int_84"
id="e9780486140520_c06.html_ref_int_84" class="ref_int">Figure 6.2-1</a>
shows the two gimbal gyro with the mass center coinciding with the
geometric center of the gimbals. We wish now to write the moment
equations about the gimbal bearing axes. Neglecting again the mass of
the gimbals, the moments of inertia about the <span class="i">ξ</span>,
<span class="i">η</span>, <span class="i">ζ</span> axes are
<span class="i">A, A, C</span>, of the wheel.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0831.jpg](images/e9780486140520_i0831.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_84"
id="e9780486140520_c06.html_int_84" class="label_int"><span
class="b">Fig. 6.2-1</span></a> Symmetric gyro with gimbal axes
<span class="i">ξ</span> and <span class="i">Z</span>.

</div>

</div>

The angular velocities and angular momentum about the
<span class="i">ξ</span>, <span class="i">η</span>,
<span class="i">ζ</span> axes are the same as in Sec. 5.13, and the
moment equations about the <span class="i">ξ</span>,
<span class="i">η</span>, <span class="i">ζ</span> axes are rewritten in
the following form.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0832.jpg](images/e9780486140520_i0832.jpg)

</div>

<div class="caption">

(6.2–1)

</div>

</div>

The moments <span class="i">M</span><sub><span class="i">n</span></sub>
and <span class="i">M</span><sub><span class="i">ζ</span></sub> can be
resolved along the vertical <span class="i">Z</span> axis and in the
horizontal plane. The <span class="i">Z</span> component is (i.e.,
<span class="i">M</span><sub><span class="i">ζ</span></sub> = 0),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0833.jpg](images/e9780486140520_i0833.jpg)

</div>

<div class="caption">

(6.2–2)

</div>

</div>

These nonlinear equations can be linearized under certain simplifying
assumptions. Usually the spin
<span class="imageinline">![e9780486140520_i0834.jpg](images/e9780486140520_i0834.jpg)</span>
is very large in comparison to
<span class="imageinline">![e9780486140520_i0835.jpg](images/e9780486140520_i0835.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0836.jpg](images/e9780486140520_i0836.jpg)</span>.
The spin
<span class="imageinline">![e9780486140520_i0837.jpg](images/e9780486140520_i0837.jpg)</span>
is then approximately equal to <span class="i">n</span> which is a
constant of large magnitude. Neglecting the squares and products of the
smaller quantities
<span class="imageinline">![e9780486140520_i0838.jpg](images/e9780486140520_i0838.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0839.jpg](images/e9780486140520_i0839.jpg)</span>
, the simplified equations of interest are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0840.jpg](images/e9780486140520_i0840.jpg)

</div>

<div class="caption">

(6.2–3)

</div>

</div>

Several interesting solutions of the above equations are possible
depending on the type of excitation. We can first examine the steady
precession condition,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0841.jpg](images/e9780486140520_i0841.jpg)

</div>

</div>

The above equations then become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0842.jpg](images/e9780486140520_i0842.jpg)

</div>

<div class="caption">

(6.2–4)

</div>

</div>

which requires a constant torque
<span class="i">M</span><sub><span class="i">ξ</span>0</sub> about the
horizontal gimbal axis, as found previously in Sec. 5.14.

We can now consider the problem where the spin axis under steady
precession is given a disturbance by a moment
<span class="i">M</span><sub><span class="i">ξ</span></sub>(<span class="i">t</span>).

We will assume small oscillations and introduce the equations,

<div class="blocktext">

<span class="i">θ</span> = <span class="i">θ</span><sub>0</sub> +
<span class="i">θ</span><sub>∼</sub> sin <span class="i">θ</span> = sin
<span class="i">θ</span><sub>0</sub> +
<span class="i">θ</span><sub>∼</sub> cos
<span class="i">θ</span><sub>0</sub>  
<span class="imageinline">![e9780486140520_i0843.jpg](images/e9780486140520_i0843.jpg)</span>
cos<span class="i">θ</span> =
cos<span class="i">θ</span><sub>0</sub>−<span class="i">θ</span><sub>∼</sub>sin<span class="i">θ</span>0

</div>

Again neglecting products of the small oscillatory terms, Eqs. 6.2–3
become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0844.jpg](images/e9780486140520_i0844.jpg)

</div>

<div class="caption">

(6.2–5)

</div>

</div>

Eliminating the steady–state terms, Eq. 6.2–4, from the above, and
letting <span class="i">Cn/A</span> = <span class="i">p,</span> we have
the final form of the differential equations for the disturbance about
the steady precession:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0845.jpg](images/e9780486140520_i0845.jpg)

</div>

<div class="caption">

(6.2–6)

</div>

</div>

The solution of these equations is most conveniently obtained by the use
of Laplace transforms with <span class="i">θ</span><sub>∼</sub> and
<span class="imageinline">![e9780486140520_i0846.jpg](images/e9780486140520_i0846.jpg)</span>
as dependent variables.<sup>10</sup> Since initially
<span class="i">θ</span> = <span class="i">θ</span><sub>0</sub>, 0 = 0,
and
<span class="imageinline">![e9780486140520_i0847.jpg](images/e9780486140520_i0847.jpg)</span>,
and the transform equations are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0848.jpg](images/e9780486140520_i0848.jpg)

</div>

<div class="caption">

(6.2–7)

</div>

</div>

By Cramer’s rule, the equations for
<span class="imageinline">![e9780486140520_i0849.jpg](images/e9780486140520_i0849.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0850.jpg](images/e9780486140520_i0850.jpg)</span>
are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0851.jpg](images/e9780486140520_i0851.jpg)

</div>

<div class="caption">

(6.2–8)

</div>

</div>

which may be solved for any excitation
<span class="i">M</span><sub><span class="i">ξ</span></sub>(<span class="i">t</span>),
and any angle <span class="i">θ</span><sub>0</sub>.

<span class="b">Example 6.2–1</span>

When the spin axis is at rest at <span class="i">θ</span><sub>0</sub> =
<span class="i">π</span>/2, an impulse is applied to the spin axis,
resulting in an impulsive moment
<span class="imageinline">![e9780486140520_i0852.jpg](images/e9780486140520_i0852.jpg)</span>
, where <span class="i">δ</span>(<span class="i">t</span>) is a delta
function with the unit per second and
<span class="imageinline">![e9780486140520_i0853.jpg](images/e9780486140520_i0853.jpg)</span>
is the moment impulse in lb–in. sec. From Eqs. 6.2–8, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0854.jpg](images/e9780486140520_i0854.jpg)

</div>

</div>

and their time solutions are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0855.jpg](images/e9780486140520_i0855.jpg)

</div>

</div>

The actual position of the spin axis at any time is then equal to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0856.jpg](images/e9780486140520_i0856.jpg)

</div>

</div>

These results can be interpreted as follows. Assume first that the spin
axis is stationary so that
<span class="imageinline">![e9780486140520_i0857.jpg](images/e9780486140520_i0857.jpg)</span>
. The moment impulse
<span class="imageinline">![e9780486140520_i0858.jpg](images/e9780486140520_i0858.jpg)</span>
suddenly shifts the angular momentum vector <span class="i">Cn</span>
along the equator by an angle
<span class="imageinline">![e9780486140520_i0859.jpg](images/e9780486140520_i0859.jpg)</span>.
The spin axis however cannot change instantaneously, but develops a
downward velocity of
<span class="imageinline">![e9780486140520_i0860.jpg](images/e9780486140520_i0860.jpg)</span>from
the equatorial position. Thus the rotation of the spin axis around the
new resultant angular momentum vector generates a cone of base radius
<span class="imageinline">![e9780486140520_i0861.jpg](images/e9780486140520_i0861.jpg)</span>
, as shown in <a href="#e9780486140520_c06.html#int_85"
id="e9780486140520_c06.html_ref_int_85" class="ref_int">Fig. 6.2-2</a>.
This is, of course, consistent with the conclusions of Sec. 5.8 which
indicates that, with zero moment (with a delta function moment, the
moment is zero at all <span class="i">t</span> except
<span class="i">t</span> = 0), the angular momentum vector is constant
and stationary, and the spin axis will precess around it.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0862.jpg](images/e9780486140520_i0862.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_85"
id="e9780486140520_c06.html_int_85" class="label_int"><span
class="b">Fig. 6.2-2</span></a> Motion of spin axis due to delta
function impulse (initial moment is zero).

</div>

</div>

If next we consider an initial steady precession with the spin axis at
<span class="i">θ</span><sub>0</sub> = <span class="i">π</span>/2 due to
a constant moment
<span class="imageinline">![e9780486140520_i0863.jpg](images/e9780486140520_i0863.jpg)</span>
, the resultant angular momentum vector h will be above the equator by
the moment component
<span class="imageinline">![e9780486140520_i0864.jpg](images/e9780486140520_i0864.jpg)</span>.
The moment impulse
<span class="imageinline">![e9780486140520_i0865.jpg](images/e9780486140520_i0865.jpg)</span>
will again suddenly shift the resultant <span class="b">h</span>
horizontally by an amount
<span class="imageinline">![e9780486140520_i0866.jpg](images/e9780486140520_i0866.jpg)</span>
along the latitude
<span class="imageinline">![e9780486140520_i0867.jpg](images/e9780486140520_i0867.jpg)</span>,
as shown in <a href="#e9780486140520_c06.html#int_86"
id="e9780486140520_c06.html_ref_int_86" class="ref_int">Fig. 6.2-3</a>.
At time <span class="i">t</span> = 0+, the spin axis will have angular
velocity components
<span class="imageinline">![e9780486140520_i0868.jpg](images/e9780486140520_i0868.jpg)</span>
<span class="imageinline">![e9780486140520_i0869.jpg](images/e9780486140520_i0869.jpg)</span>
vertically, and
<span class="imageinline">![e9780486140520_i0870.jpg](images/e9780486140520_i0870.jpg)</span>
horizontally. Their resultant will however be normal to the radial line
from the h vector, as shown in
<a href="#e9780486140520_c06.html#int_86" class="ref_int">Fig. 6.2-3</a>.
Thus the h vector of approximate length <span class="i">Cn</span> will
precess steadily along the latitude <span class="i">λ</span> =
<span class="imageinline">![e9780486140520_i0871.jpg](images/e9780486140520_i0871.jpg)</span><span class="i">/Cn</span>
with angular velocity
<span class="imageinline">![e9780486140520_i0872.jpg](images/e9780486140520_i0872.jpg)</span>
while the spin axis will rotate around h in a circle of radius
<span class="imageinline">![e9780486140520_i0873.jpg](images/e9780486140520_i0873.jpg)</span>.
The result is a combined nutation and precession, and the curve
described by the spin axis depends on the relative magnitudes of the
initial velocity components
<span class="imageinline">![e9780486140520_i0874.jpg](images/e9780486140520_i0874.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0875.jpg](images/e9780486140520_i0875.jpg)</span>
. This behavior is somewhat similar to the problem of the disturbed top,
the difference being that we have here imposed a constant moment about
the node axis <span class="i">ξ</span>, whereas in the problem of the
top, the gravity moment will change with <span class="i">θ</span>. For
small disturbances, however, the motions are identical.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0876.jpg](images/e9780486140520_i0876.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_86"
id="e9780486140520_c06.html_int_86" class="label_int"><span
class="b">Fig. 6.2-3</span></a>. Motion of spin axis dues to delta
function impulse (initial moment is contant, with steady precession
<span class="imageinline">![e9780486140520_i0877.jpg](images/e9780486140520_i0877.jpg)</span>
).

</div>

</div>

<span class="b">PROBLEMS</span>

1.  With the axes initially at rest with <span class="i">θ</span> =
    <span class="i">π</span>/2, a constant moment is applied to then
    <span class="i">ξ</span> axis. Determine its solution.

2.  Repeat Prob. 1 if <span class="i">M</span> is a delta function
    <span class="imageinline">![e9780486140520_i0878.jpg](images/e9780486140520_i0878.jpg)</span>
    .

3.  With the system initially at rest at an angle
    <span class="i">θ</span><sub>0</sub>, a constant moment is applied
    to the <span class="i">OZ</span> axis. Determine its motion,
    assuming <span class="i">Cn</span> to be very large.

4.  Consider
    <span class="imageinline">![e9780486140520_i0879.jpg](images/e9780486140520_i0879.jpg)</span>
    to be the only angular momentum of importance for
    <span class="imageinline">![e9780486140520_i0880.jpg](images/e9780486140520_i0880.jpg)</span>
    large, and determine the time required for then
    <span class="i">ζ</span> axis to rotate from the horizontal to the
    vertical position due to a constant moment
    <span class="i">M</span><sub><span class="i">Z</span></sub> about
    the <span class="i">Z</span> axis.

5.  A satellite with spin moment of inertia <span class="i">C</span> and
    equal transverse moment of inertia <span class="i">B</span> =
    <span class="i">A</span> has at the initial moment three collinear
    vectors, <span class="b">h</span>, <span class="b">ω</span>, and
    <span class="b">k</span>, along the spin axis. To change its
    attitude, an impulsive torque
    <span class="imageinline">![e9780486140520_i0881.jpg](images/e9780486140520_i0881.jpg)</span>
    is applied to the transverse pitch axis. Determine the relative
    position of the three vectors immediately after impulse and the
    subsequent motion of the satellite.

6.  Show that the three vectors of Prob. 5 can again be made collinear
    by applying an equal impulsive torque
    <span class="imageinline">![e9780486140520_i0882.jpg](images/e9780486140520_i0882.jpg)</span>
    in the same direction after a half–cycle of precession, thereby
    producing an attitude change of
    <span class="imageinline">![e9780486140520_i0883.jpg](images/e9780486140520_i0883.jpg)</span>
    with no precession (see
    <a href="#e9780486140520_c06.html#int_85" class="ref_int">Fig. 6.2-2</a>).
    Determine the spacing in time of the impulses.

7.  It is proposed to change the attitude of the spin axis of a
    satellite with angular momentum <span class="i">h</span> =
    <span class="i">Cn</span> by an angle of 90° with a series of
    <span class="i">N</span> equal impulses, ending up with the h,
    <span class="b">ω</span>, and k vectors collinear. Determine the
    magnitude of the impulses and their time spacing.

8.  Starting with Eq. 3.5–4 for the transformation between the body
    angular velocities
    <span class="i">ω</span><sub><span class="i">x</span></sub>,
    <span class="i">ω</span><sub><span class="i">y</span></sub>,
    <span class="i">ω</span><sub><span class="i">z</span></sub>, and the
    Euler angular rates,
    <span class="imageinline">![e9780486140520_i0884.jpg](images/e9780486140520_i0884.jpg)</span>
    ,
    <span class="imageinline">![e9780486140520_i0885.jpg](images/e9780486140520_i0885.jpg)</span>
    ,
    <span class="imageinline">![e9780486140520_i0886.jpg](images/e9780486140520_i0886.jpg)</span>
    , show that the general solution for the Euler angles are given by
    the equations,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0887.jpg](images/e9780486140520_i0887.jpg)

    </div>

    </div>

9.  For small oscillations with
    <span class="imageinline">![e9780486140520_i0888.jpg](images/e9780486140520_i0888.jpg)</span>
    = constant, discuss the solution for <span class="i">θ</span> and
    <span class="i">ψ</span> of Prob. 8 as influenced by the value of
    <span class="i">θ</span><sub>0</sub> which may be arbitrarily
    chosen. Why is <span class="i">θ</span><sub>0</sub> =
    <span class="i">π</span>/2 desirable for small angle solutions?

10. With <span class="i">θ</span><sub>0</sub> =
    <span class="i">π</span>/2 in the equations of Prob. 8, solve Prob.
    5 for <span class="i">θ</span> and <span class="i">ψ</span> by first
    determining the angular rates about the body–fixed axes
    <span class="i">x</span> and <span class="i">y</span>.

11. Assume that the rotor of
    <a href="#e9780486140520_c06.html#int_84" class="ref_int">Fig. 6.2-1</a>
    is misaligned so that its normal (axis <span class="i">z</span>)
    makes an angle <span class="i">α</span> with the spin axis
    <span class="i">ζ</span>. Let <span class="i">x</span> be an axis
    normal to both <span class="i">z</span> and
    <span class="i">ζ</span>, <span class="i">y</span> the third axis of
    the <span class="i">x</span>, <span class="i">y</span>,
    <span class="i">z</span> set, and show that the angular velocities
    along <span class="i">x</span>, <span class="i">y</span>,
    <span class="i">z</span>, are;

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0889.jpg](images/e9780486140520_i0889.jpg)

    </div>

    </div>

    Since the moments of inertia of the rotor are <span class="i">A, A,
    C</span>, the angular momentum along <span class="i">x</span>,
    <span class="i">y</span>, <span class="i">z</span> are;
    <span class="i">h</span><sub><span class="i">x</span></sub> =
    <span class="i">Aω</span><sub><span class="i">x</span></sub><span class="i">,
    h</span><sub><span class="i">y</span></sub> =
    <span class="i">Aω</span><sub><span class="i">y</span></sub>,
    <span class="i">h</span><sub><span class="i">z</span></sub> =
    <span class="i">Cω</span><sub><span class="i">z</span></sub>.

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0890.jpg](images/e9780486140520_i0890.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. II</span>

    </div>

    </div>

12. Resolve the angular momentum
    <span class="i">h</span><sub><span class="i">x</span></sub>,
    <span class="i">h</span><sub><span class="i">y</span></sub><span class="i">,
    h</span><sub><span class="i">z</span></sub> of Prob. 11 along the
    gyro gimbal axes ξ,
    <span class="i"><span class="b">Z</span></span><span class="b">,</span>
    and <span class="b">ζ,</span> assuming <span class="b">α</span> to
    be small (see
    <a href="#e9780486140520_c06.html#int_84" class="ref_int">Fig. 6.2-1</a>).

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title81"></span>

# <span class="b">6.3 Gimbal Masses Included (Perturbation Technique)</span>

Referring to
<a href="#e9780486140520_c06.html#int_84" class="ref_int">Fig. 6.2-1</a>,
the moment of inertia of the rotor about the ξ, <span class="i">η,
ζ</span> axes were <span class="i">A, A,</span>
<span class="i">C</span>. In addition, we introduce the moment of
inertia of the gimbals as follows. The moment of inertia of the inner
gimbal about the <span class="i">ξ, η, ζ</span> axes are
<span class="i">A</span><sub><span class="i">i</span></sub><span class="i">.
B</span><sub><span class="i">i</span></sub><span class="i">,
C</span><sub><span class="i">i</span></sub> respectively. The moment of
inertia of the outer gimbal about the <span class="i">OZ</span> axis is
<span class="i">C</span><sub><span class="b">0</span></sub><span class="b">.</span>

Noting that the <span class="i">ξ, η, ζ,</span> axes rotate with angular
speeds
<span class="imageinline">![e9780486140520_i0891.jpg](images/e9780486140520_i0891.jpg)</span>
,
<span class="imageinline">![e9780486140520_i0892.jpg](images/e9780486140520_i0892.jpg)</span>
sin θ.
<span class="imageinline">![e9780486140520_i0893.jpg](images/e9780486140520_i0893.jpg)</span>
cos <span class="i">θ,</span> and noting the masses which rotate due to
these components, the moment of inertia about the three axes are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0894.jpg](images/e9780486140520_i0894.jpg)

</div>

<div class="caption">

(6.3–1)

</div>

</div>

The direction cosines of the <span class="i">OZ</span> axis with respect
to <span class="i">ξ, η, ζ,</span> are
<span class="i">l</span><sub><span class="i">Zξ</span></sub> = 0,
<span class="i">l</span><sub><span class="i">Zη</span></sub> = sin
<span class="i">θ</span>,
<span class="i">l</span><sub><span class="i">Zζ</span></sub> = cos θ, so
that the moment of inertia about the <span class="i">Z</span> axis
becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0895.jpg](images/e9780486140520_i0895.jpg)

</div>

<div class="caption">

(6.3–2)

</div>

</div>

We next determine the angular momenta about the <span class="i">ξ, η,
ζ</span> axes, which are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0896.jpg](images/e9780486140520_i0896.jpg)

</div>

<div class="caption">

(6.3–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0897.jpg](images/e9780486140520_i0897.jpg)

</div>

<div class="caption">

(6.3–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0898.jpg](images/e9780486140520_i0898.jpg)

</div>

<div class="caption">

(6.3–5)

</div>

</div>

The moment about then ζ axis can be separated into two parts, thus:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0899.jpg](images/e9780486140520_i0899.jpg)

</div>

<div class="caption">

(6.3–6)

</div>

</div>

where
<span class="imageinline">![e9780486140520_i0900.jpg](images/e9780486140520_i0900.jpg)</span>
is the moment on the rotor axis, and
<span class="i">M</span><sub><span class="i">ζ</span></sub><span class="i">″</span>
is the moment due to the forces exerted on the inner gimbal axis by the
outer gimbal, as shown in <a href="#e9780486140520_c06.html#int_87"
id="e9780486140520_c06.html_ref_int_87" class="ref_int">Fig. 6.3-1</a>.
We will assume
<span class="imageinline">![e9780486140520_i0901.jpg](images/e9780486140520_i0901.jpg)</span>
to be zero, in which case the rotor angular momentum will be a constant.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0902.jpg](images/e9780486140520_i0902.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_87"
id="e9780486140520_c06.html_int_87" class="label_int"><span
class="b">Fig. 6.3-1</span></a><span class="b">.</span> Moments on inner
gimbal and rotor.

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0903.jpg](images/e9780486140520_i0903.jpg)

</div>

<div class="caption">

(6.3–7)

</div>

</div>

The angular momentum components along ξ, η, ζ, shown in
<a href="#e9780486140520_c06.html#int_88"
id="e9780486140520_c06.html_ref_int_88" class="ref_int">Fig. 6.3-2</a>,
can be resolved along the <span class="i">ξ′, η′, ζ′</span> axes by
noting the vertical and horizontal components of
<span class="i">h</span><sub><span class="i">n</span></sub> and
<span class="i">h</span><sub><span class="i">ζ</span></sub><span class="i">.</span>
The <span class="i">h</span><sub><span class="i">ξ</span></sub> and
<span class="i">h</span><sub><span class="i">η′</span></sub> components
now rotate about the <span class="i">OZ</span> axis with angular speed
<span class="imageinline">![e9780486140520_i0904.jpg](images/e9780486140520_i0904.jpg)</span>
, as shown in
<a href="#e9780486140520_c06.html#int_88" class="ref_int">Fig. 6.3-2</a>.
The components of h along the <span class="i">ξ′, η′, ζ′</span> axes
are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0905.jpg](images/e9780486140520_i0905.jpg)

</div>

<div class="caption">

(6.3–8)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0906.jpg](images/e9780486140520_i0906.jpg)

</div>

<div class="caption">

(6.3–9)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0907.jpg](images/e9780486140520_i0907.jpg)

</div>

<div class="caption">

(6.3–10)

</div>

</div>

We can now write the moment equations about the ζ′ and ξ′ axes as
follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0908.jpg](images/e9780486140520_i0908.jpg)

</div>

<div class="caption">

(6.3–11)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0909.jpg](images/e9780486140520_i0909.jpg)

</div>

<div class="caption">

(6.3–12)

</div>

</div>

We next investigate the problem for which the axes are initially at
rest, and the inner gimbal axis in position
<span class="i">θ</span><sub>0</sub> is given an initial angular
velocity
<span class="imageinline">![e9780486140520_i0910.jpg](images/e9780486140520_i0910.jpg)</span>,
by an impulsive moment in the form of a delta function about then ξ
axis. The time <span class="i">t</span> = 0 is referenced to the instant
after the impulse, in which case
<span class="i">M</span><sub><span class="i">ξ</span></sub> =
<span class="i">M</span><sub><span class="i">Z</span></sub> = 0, and the
initial conditions are ψ(0) = 0,
<span class="imageinline">![e9780486140520_i0911.jpg](images/e9780486140520_i0911.jpg)</span>,
θ(0) = θ<sub>0</sub>, 6(0) = α. We can safely assume that
<span class="imageinline">![e9780486140520_i0912.jpg](images/e9780486140520_i0912.jpg)</span>,
since the initial velocity α results in a gyroscopic moment about the
<span class="i">Z</span> axis (through reaction of ξ bearings) which is
not impulsive.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0913.jpg](images/e9780486140520_i0913.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_88"
id="e9780486140520_c06.html_int_88" class="label_int"><span
class="b">Fig. 6.3-2</span></a> Resolution of angular velocity and
angular momentum.

</div>

</div>

With the outer gimbal axis unrestrained,
<span class="i">M</span><sub><span class="i">Z</span></sub> = 0, and Eq.
6.3–11 can be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0914.jpg](images/e9780486140520_i0914.jpg)

</div>

<div class="caption">

(6.3–13)

</div>

</div>

Integrating and noting that
<span class="imageinline">![e9780486140520_i0915.jpg](images/e9780486140520_i0915.jpg)</span>
at <span class="i">t</span> = 0 is zero, we obtain the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0916.jpg](images/e9780486140520_i0916.jpg)

</div>

<div class="caption">

(6.3–14)

</div>

</div>

We now make the small oscillation approximation,

<div class="blocktext">

θ = θ<sub>0</sub> + θ<sub>∼</sub>  
sin θ ≅ sin θ<sub>0</sub> + θ<sub>∼</sub> cos θ<sub>0</sub>  
cos θ ≅ cos θ<sub>0</sub> − θ<sub>∼</sub> sin θ<sub>0</sub>  
sin 0 cos θ ≅ sin
<span class="i">θ</span><sub><span class="i">0</span></sub> cos
θ<sub>0</sub> + θ<sub>∼</sub>(cos<sup>2</sup> θ<sub>0</sub> −
sin<sup>2</sup> θ<sub>0</sub>)

</div>

and rewrite Eqs. 6.3–2, 6.3–14, and 6.3–12 as Eqs. 6.3–15, 6.3–16, and
6.3–17

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0917.jpg](images/e9780486140520_i0917.jpg)

</div>

<div class="caption">

(6.3–15)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0918.jpg](images/e9780486140520_i0918.jpg)

</div>

<div class="caption">

(6.3–16)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0919.jpg](images/e9780486140520_i0919.jpg)

</div>

<div class="caption">

(6.3–17)

</div>

</div>

Equations 6.3–16 and 6.3–17 are nonlinear due to the last term in each
equation. They can be solved by the perturbation
technique<sup>1,3,8</sup> which will be illustrated by the following
simple example. Consider a first–order nonlinear equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0920.jpg](images/e9780486140520_i0920.jpg)

</div>

<div class="caption">

<span class="i">(a)</span>

</div>

</div>

where the coefficient <span class="i">b</span> of the nonlinear term is
a small quantity. We will now consider a similar equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0921.jpg](images/e9780486140520_i0921.jpg)

</div>

<div class="caption">

<span class="i">(b)</span>

</div>

</div>

which differs from the previous equation by an additional factor
<span class="i">µ</span> which may be any positive number. If the
solution of Eq. <span class="i">b</span> is found, then the solution of
the previous equation, Eq. <span class="i">a,</span> is found by letting
<span class="i">µ</span> = 1.

We seek now a solution in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0922.jpg](images/e9780486140520_i0922.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

Substituting <span class="i">c</span> into <span class="i">b</span> we
obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0923.jpg](images/e9780486140520_i0923.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

Rearranging, this equation can be written in terms of equal powers of µ
as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0924.jpg](images/e9780486140520_i0924.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

We note now that, if µ = 0, we obtain
<span class="i">y</span><sub><span class="i">0</span></sub> as the
solution of the linear equation. The solution
<span class="i">y</span><sub><span class="i">0</span></sub> is called
the <span class="i">generating solution,</span> and it can be fitted to
the initial conditions of the problem. If <span class="i">µ</span> is
allowed to increase from zero, Eq. <span class="i">e</span> can be
satisfied only if the coefficients of <span class="i">µ</span> raised to
the various powers are zero. We thus obtain the following equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0925.jpg](images/e9780486140520_i0925.jpg)

</div>

<div class="caption">

(<span class="i">ƒ</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0926.jpg](images/e9780486140520_i0926.jpg)

</div>

<div class="caption">

(<span class="i">g</span>)

</div>

</div>

which can be solved for
<span class="i">y</span><sub><span class="i">1</span></sub><span class="i">,
y</span><sub>2</sub>, etc.

We will now apply this technique to Eqs. 6.3–16 and 6.3–17, but will
carry out the solution only to the first–order correction. Since Eq.
6.3–16 and 6.3–17 already have the symbol
<span class="i">θ</span><sub>0</sub>, we will let the solution to the
linear equation (corresponding to
<span class="i">y</span><sub><span class="i">0</span></sub>) be
<span class="i">θ</span><sub>00</sub> and
<span class="imageinline">![e9780486140520_i0927.jpg](images/e9780486140520_i0927.jpg)</span>
The linear equations are then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0928.jpg](images/e9780486140520_i0928.jpg)

</div>

<div class="caption">

(6.3–16<span class="i">a</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0929.jpg](images/e9780486140520_i0929.jpg)

</div>

<div class="caption">

(6.3–17<span class="i">a</span>)

</div>

</div>

Eliminating
<span class="imageinline">![e9780486140520_i0930.jpg](images/e9780486140520_i0930.jpg)</span>
we obtain the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0931.jpg](images/e9780486140520_i0931.jpg)

</div>

<div class="caption">

(6.3–18)

</div>

</div>

Letting

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0932.jpg](images/e9780486140520_i0932.jpg)

</div>

<div class="caption">

(6.3–19)

</div>

</div>

the generating solution fitting the initial conditions is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0933.jpg](images/e9780486140520_i0933.jpg)

</div>

<div class="caption">

(6.3–20)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0934.jpg](images/e9780486140520_i0934.jpg)

</div>

<div class="caption">

(6.3–21)

</div>

</div>

We next consider the first–order correction corresponding to
<span class="i">y</span><sub><span class="i">1</span></sub> in Eq.
<span class="i">ƒ</span>. From the generating solution we determine the
nonlinear terms

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0935.jpg](images/e9780486140520_i0935.jpg)

</div>

</div>

which, substituted into Eqs. 6.3–16 and 6.3–17, results in a new set of
differential equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0936.jpg](images/e9780486140520_i0936.jpg)

</div>

<div class="caption">

(6.3–16<span class="i">b</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0937.jpg](images/e9780486140520_i0937.jpg)

</div>

<div class="caption">

(6.3–17<span class="i">b</span>)

</div>

</div>

We will now eliminate θ<sub>1</sub>. From Eq.
6.3–16<span class="i">b</span> we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0938.jpg](images/e9780486140520_i0938.jpg)

</div>

</div>

Substituting into Eq. 6.3–17<span class="i">b</span>, we obtain the
differential equation for ψ<sub>1</sub>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0939.jpg](images/e9780486140520_i0939.jpg)

</div>

</div>

In examining this equation, the solution of the homogeneous equation for
<span class="imageinline">![e9780486140520_i0940.jpg](images/e9780486140520_i0940.jpg)</span>
is again harmonic of frequency ω as given by Eq. 6.3–19. The particular
solution will have harmonic terms of frequency 2ω and, in addition, a
constant term equal to the constant term on the right side of the
equation divided by the coefficient of
<span class="imageinline">![e9780486140520_i0941.jpg](images/e9780486140520_i0941.jpg)</span>
on the left side. We are interested in the constant term since it
results in a steady drift which rotates the outer gimbal according to
the equation
<span class="imageinline">![e9780486140520_i0942.jpg](images/e9780486140520_i0942.jpg)</span>

The constant term of the solution is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0943.jpg](images/e9780486140520_i0943.jpg)

</div>

</div>

Substituting for <span class="i">I</span><sub>0</sub> from Eq. 6.3–15,
it reduces to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0944.jpg](images/e9780486140520_i0944.jpg)

</div>

<div class="caption">

(6.3–22)

</div>

</div>

It is evident, then, that the outer gimbal oscillates and drifts in a
negative direction, a phenomenon referred to as “gimbal
walk.”<sup>6</sup> It should be noted that gimbal walk cannot take place
at <span class="i">θ</span><sub><span class="i">0</span></sub> = 90° or
if the moment of inertia (<span class="i">C</span><sub>0</sub> +
<span class="i">C</span><sub><span class="i">i</span></sub><span class="i">)</span>
is zero.

<span class="b">PROBLEMS</span>

1.  The periodic solution for Eq. 6.3–17<span class="i">c</span> is

    <div class="blocktext">

    <span class="imageinline">![e9780486140520_i0945.jpg](images/e9780486140520_i0945.jpg)</span>

    </div>

    Evaluate the coefficient β.

2.  Discuss the solution of a nonhomogeneous equation,
    <div class="blocktext">

    <span class="imageinline">![e9780486140520_i0946.jpg](images/e9780486140520_i0946.jpg)</span>

    </div>

    by the procedure of Sec. 6.3.

3.  Solve the nonlinear differential equation,
    <div class="blocktext">

    <span class="i">my + ky–by</span><sup><span class="i">3</span></sup>
    <span class="i">= F sin pt</span>

    </div>

    by the perturbation method outlined in Sec. 6.3. The solution with
    the use of only two terms, <span class="i">y</span> =
    <span class="i">y</span><sub><span class="i">0</span></sub> +
    µ<span class="i">y</span><sub>1</sub><span class="i">,</span> is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0947.jpg](images/e9780486140520_i0947.jpg)

    </div>

    </div>

    where
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0948.jpg](images/e9780486140520_i0948.jpg)

    </div>

    </div>

4.  Show that if only the first term <span class="i">y</span> =
    <span class="i">a</span> sin <span class="i">pt</span> of Prob. 3 is
    substituted into the differential equation, the amplitude
    relationship
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0949.jpg](images/e9780486140520_i0949.jpg)

    </div>

    </div>

    is obtained. Letting the ordinate <span class="i">v</span> =
    (3<span class="i">b</span>/4<span class="i">mω</span><sup>2</sup>)<span class="i">a</span><sup>3</sup>
    be plotted against <span class="i">a</span>, discuss the solution
    for the amplitude <span class="i">a</span> versus
    <span class="i">p/ω,</span> where ω<sup>2</sup> =
    <span class="i">k/m.</span>

5.  For the problem of Sec. 6.3, investigate the equation for
    <span class="imageinline">![e9780486140520_i0950.jpg](images/e9780486140520_i0950.jpg)</span>
    and establish whether there is a unidirectional motion about the
    node axis.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title82"></span>

# <span class="b">6.4 The Gyrocompass</span>

The requirement of a gyrocompass is to point north at any latitude at
any time. The high–speed, two–gimballed gyro, with a pendulous weight
<span class="i">w</span> on the–η axis to give it moment
<span class="i">w</span>/ cos 0 about the ξ axis when the axis is tilted
above the horizon, as shown in <a href="#e9780486140520_c06.html#int_89"
id="e9780486140520_c06.html_ref_int_89" class="ref_int">Fig. 6.4-1</a>,
will satisfy this requirement.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0951.jpg](images/e9780486140520_i0951.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_89"
id="e9780486140520_c06.html_int_89" class="label_int"><span
class="b">Fig. 6.4-1</span></a> Gyrocompass and angular velocity
components.

</div>

</div>

In
<a href="#e9780486140520_c06.html#int_89" class="ref_int">Fig. 6.4-1</a>,
the rotation of the earth from west to east is indicated by the angular
rotation vector Ω pointing in the northerly direction. Its numerical
value is Ω = 2π/(24 x 3600) = 7.27 x 10<sup>–5</sup> rad/sec. At any
latitude λ, Ω will have components in the meridian plane, equal to Ω cos
λ horizontally, and Ω sin λ vertically.

With the Z axis of the gyrocompass in the local vertical direction, in
order for then ζ axis to remain in the meridian plane, and hence point
north, the outer gimbal must precess steadily by an amount
<span class="imageinline">![e9780486140520_i0952.jpg](images/e9780486140520_i0952.jpg)</span>
and in addition have an angular velocity Ω cos λ about the–η axis
perpendicular to the outer gimbal plane. We assume that the gyro is
constrained to move in this manner, and investigate the moment
requirement satisfying the motion.

Letting θ = 90° − α<sub>0</sub>, where α<sub>0</sub> is a small angle
above the horizontal plane at latitude λ, the angular velocities of the
ξ, η, ζ axes are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0953.jpg](images/e9780486140520_i0953.jpg)

</div>

<div class="caption">

(6.4–1)

</div>

</div>

Assuming the spin to be very large, we can neglect all other components
of h. With M<sub><span class="i">Z</span></sub> = 0,
<span class="imageinline">![e9780486140520_i0954.jpg](images/e9780486140520_i0954.jpg)</span>
= constant. The required moment about the ξ axis, is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0955.jpg](images/e9780486140520_i0955.jpg)

</div>

<div class="caption">

(6.4–2)

</div>

</div>

Dividing by sin α<sub>0</sub>, the required inclination of the spin axis
above the horizon is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0956.jpg](images/e9780486140520_i0956.jpg)

</div>

<div class="caption">

(6.4–3)

</div>

</div>

which depends on the latitude λ.

The moment required for the angular velocity Ω cos λ about the–η′ axis
is supplied by the reaction of the bearings on the outer gimbal axis Z.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title83"></span>

# <span class="b">6.5 Oscillation of the Gyrocompass</span>

If the axis of the gyrocompass is disturbed from the meridian plane, as
shown in <a href="#e9780486140520_c06.html#int_90"
id="e9780486140520_c06.html_ref_int_90" class="ref_int">Fig. 6.5-1</a>,
the oscillation which takes place will have two components, one
perpendicular to the meridian plane and the other in the meridian plane.
Both oscillations will have the same frequency, and so the end of the
axis of the gyrocompass will describe an ellipse.

Letting ψ be the angular deviation of the spin axis out of the meridian
plane, and α its inclination above the horizontal, we will assume both
these angles to be small, in which case the angular velocities about the
ξ, η, ζ axes will be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0957.jpg](images/e9780486140520_i0957.jpg)

</div>

<div class="caption">

(6.5—1)

</div>

</div>

We will also assume the spin to be large and the angular momentum about
the ξ and η axes to be negligible in comparison.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0958.jpg](images/e9780486140520_i0958.jpg)

</div>

</div>

The moment equations of interest are then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0959.jpg](images/e9780486140520_i0959.jpg)

</div>

<div class="caption">

(6.5–2)

</div>

</div>

where <span class="i">wl</span> is the mass unbalance of the pendulous
weight on the −η axis. Rearranging these equations, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0960.jpg](images/e9780486140520_i0960.jpg)

</div>

<div class="caption">

(6.5–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0961.jpg](images/e9780486140520_i0961.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_90"
id="e9780486140520_c06.html_int_90" class="label_int"><span
class="b">Fig. 6.5-1</span></a><span class="b">.</span> Vector
components for the gyrocompass.

</div>

</div>

Eliminating ψ between these equations, the differential equation for α
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0962.jpg](images/e9780486140520_i0962.jpg)

</div>

<div class="caption">

(6.5–4)

</div>

</div>

with the general solution,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0963.jpg](images/e9780486140520_i0963.jpg)

</div>

<div class="caption">

(6.5–5)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0964.jpg](images/e9780486140520_i0964.jpg)

</div>

<div class="caption">

(6.5–6)

</div>

</div>

From Eq. 6.5–3, the equation for ψ is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0965.jpg](images/e9780486140520_i0965.jpg)

</div>

<div class="caption">

(6.5–7)

</div>

</div>

These equations indicate that the spin axis oscillates horizontally
about the meridian plane and vertically about the stationary angle
α<sub>0</sub>, given by Eq. 6.4–3. The frequency of oscillation, Eq.
6.5–6 is a function of the latitude λ, and is very small due to
<span class="imageinline">![e9780486140520_i0966.jpg](images/e9780486140520_i0966.jpg)</span>
in the denominator. The frequency <span class="i">p</span> approaches
zero, as the gyrocompass nears the north polar axis, where the
reliability of the instrument diminishes.

<div class="section2">

<span id="e9780486140520_c06.html_title84"></span>

# <span class="i">High–frequency oscillation</span>

In addition to the slow oscillation given by the foregoing equations,
there is a high–frequency oscillation which was not revealed because the
angular momentum about ξ and η were assumed to be zero. By adding
<span class="imageinline">![e9780486140520_i0967.jpg](images/e9780486140520_i0967.jpg)</span>
and
<span class="imageinline">![e9780486140520_i0968.jpg](images/e9780486140520_i0968.jpg)</span>
to Eqs. 6.5–2, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0969.jpg](images/e9780486140520_i0969.jpg)

</div>

<div class="caption">

(6.5–8)

</div>

</div>

Rearranging, and letting,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0970.jpg](images/e9780486140520_i0970.jpg)

</div>

</div>

the above equations become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0971.jpg](images/e9780486140520_i0971.jpg)

</div>

<div class="caption">

(6.5–9)

</div>

</div>

Assuming harmonic oscillations,
<span class="i">e</span><sup><span class="i">ipt</span></sup>, the
natural frequencies are given by the determinant,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0972.jpg](images/e9780486140520_i0972.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0973.jpg](images/e9780486140520_i0973.jpg)

</div>

<div class="caption">

(6.5–10)

</div>

</div>

Since
<span class="imageinline">![e9780486140520_i0974.jpg](images/e9780486140520_i0974.jpg)</span>
is very much larger than
<span class="i">aI</span><sub><span class="i">ξ</span></sub> or
<span class="i">bI</span><sub><span class="i">η</span></sub><span class="i">,</span>
the natural frequency equation simplifies to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0975.jpg](images/e9780486140520_i0975.jpg)

</div>

<div class="caption">

(6.5–11)

</div>

</div>

The two frequencies are, therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0976.jpg](images/e9780486140520_i0976.jpg)

</div>

<div class="caption">

(6.5–12)

</div>

</div>

We find then that
<span class="i">p</span><sub><span class="i">1</span></sub> corresponds
to Eq. 6.5–6, and an additional high–frequency oscillation of frequency
<span class="i">p</span><sub>2</sub> is introduced. With
<span class="i">h</span><sub><span class="i">ξ</span></sub> =
<span class="i">h</span><sub><span class="i">n</span></sub> = 0,
<span class="i">p</span><sub>2</sub> = ∞ did not enter into the previous
solution. The amplitude of the high–frequency oscillation, however, is
extremely small, and hence, the slow oscillation at frequency
<span class="i">p</span> <sub><span class="i">1</span></sub> is
generally the only one detectable.

</div>

<div class="section2">

<span id="e9780486140520_c06.html_title85"></span>

# <span class="i">Effect of damping</span>

Damping for the slow oscillation of the gyrocompass can be provided by
introducing a moment about the η axis as follows. We move the pendulous
weight w a distance e to the east of the center line so that its
coordinate (ξ, η, ζ) = (−<span class="i">e</span>, −/, 0). The equation
for the moment about the axis is then modified as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0977.jpg](images/e9780486140520_i0977.jpg)

</div>

<div class="caption">

(6.5–13)

</div>

</div>

or,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0978.jpg](images/e9780486140520_i0978.jpg)

</div>

<div class="caption">

(6.5–14)

</div>

</div>

Differentiating the equation for
<span class="i">M</span><sub><span class="i">ξ</span></sub> (second of
Eq. 6.5–8 without
<span class="imageinline">![e9780486140520_i0979.jpg](images/e9780486140520_i0979.jpg)</span>
term), and substituting for
<span class="imageinline">![e9780486140520_i0980.jpg](images/e9780486140520_i0980.jpg)</span>
from above and α from <span class="i">M</span><sub>ξ</sub>, we arrive at
the following differential equation for ψ:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0981.jpg](images/e9780486140520_i0981.jpg)

</div>

<div class="caption">

(6.5–15)

</div>

</div>

The effect of the offset e is then to damp the ψ oscillations and shift
the equilibrium position to the east by the angle,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0982.jpg](images/e9780486140520_i0982.jpg)

</div>

<div class="caption">

(6.5–16)

</div>

</div>

</div>

<div class="section2">

<span id="e9780486140520_c06.html_title86"></span>

# <span class="i">Compass heading error due to vehicle motion</span>

When a vehicle carrying a gyrocompass moves in a northerly direction
along a meridian with velocity v, an angular velocity
<span class="i">v/R</span> pointing west, where <span class="i">R</span>
is the radius of the earth, is introduced. By combining this vector with
the horizontal component of the earth’s rotation Ω cos λ, the resultant
angular velocity in the horizontal plane deviates to the west by an
angle

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0983.jpg](images/e9780486140520_i0983.jpg)

</div>

</div>

and the gyrocompass will now point in the direction of the resultant,
introducing a heading error of γ.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0984.jpg](images/e9780486140520_i0984.jpg)

</div>

<div class="caption">

<span class="b">Fig</span>. <span class="b">6.5–2.</span> Angular
velocities in horizontal plane due to vehicle motion v.

</div>

</div>

If the vehicle is traveling in a direction making an angle θ with the
meridian plane, <span class="i">v</span> can be replaced by
<span class="i">v</span> cos θ to give,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i0985.jpg](images/e9780486140520_i0985.jpg)

</div>

</div>

where the effect of the component <span class="i">v</span> sin θ is
neglected due to the fact that it is small in comparison to Ω cos λ.

<span class="b">PROBLEMS</span>

1.  Resolve <span class="i">h</span> =
    <span class="imageinline">![e9780486140520_i0986.jpg](images/e9780486140520_i0986.jpg)</span>
    along the vertical and horizontal directions, so that we have the
    vector diagram shown. Derive Eq. 6.4–3 from this configuration.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0987.jpg](images/e9780486140520_i0987.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. I</span>

    </div>

    </div>

2.  Determine the reactions on the outer gimbal bearing ξ for the
    gyrocompass of Sec. 6.4 (see
    <a href="#e9780486140520_c06.html#int_89" class="ref_int">Fig. 6.4-1</a>).

3.  If the gyrocompass axis ξ is clamped at the angle α<sub>0</sub>,
    show that the frequency of oscillation becomes,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0988.jpg](images/e9780486140520_i0988.jpg)

    </div>

    </div>

4.  The following data are given for a gyrocompass.

    <div class="blocktext">

    C = 3.0 in. lb sec<sup>2</sup>  
    A = 1.80 in. lb sec<sup>2</sup>  
    <span class="imageinline">![e9780486140520_i0989.jpg](images/e9780486140520_i0989.jpg)</span>  
    <span class="i">wl</span> = 75 lb in.

    </div>

    Determine
    <span class="i">p</span><sub><span class="i">1</span></sub>,
    <span class="i">p</span><sub>2</sub>, and α<sub>0</sub> for any
    latitude λ.

5.  Determine the gyrocompass heading error for a ship traveling at a
    constant speed of 15 knots in a direction N 20° E at latitude 48° N.
    Would the heading error be different if the ships direction were N
    20° W?

6.  Derive the equation for the heading error of a gyrocompass, taking
    into account the latitude component <span class="i">v</span> sin θ
    of the carrier vehicle.

7.  A gyropendulum is a spherical pendulum with a spinning disk with
    angular momentum <span class="i">Cn</span> along its pendulum length
    /, as shown in the sketch. Letting <span class="i">A</span> be the
    moment of inertia through O perpendicular to
    <span class="i">l,</span> show that the moment equations for small
    angles are,
    <span class="imageinline">![e9780486140520_i0990.jpg](images/e9780486140520_i0990.jpg)</span>
    <div class="blocktext">

    <span class="imageinline">![e9780486140520_i0991.jpg](images/e9780486140520_i0991.jpg)</span>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0992.jpg](images/e9780486140520_i0992.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 7</span>

    </div>

    </div>

8.  Show that the gyropendulum of Prob. 7 has natural frequencies given
    by the equation,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0993.jpg](images/e9780486140520_i0993.jpg)

    </div>

    </div>

    Approximate equations for the lower and higher natural frequencies,
    neglecting the term
    <span class="i">AWl/C</span><sup><span class="i">2</span></sup><span class="i">n</span><sup><span class="i">2</span></sup><span class="i">,</span>
    are,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0994.jpg](images/e9780486140520_i0994.jpg)

    </div>

    </div>

9.  The gyropendulum of Prob. 7 is mounted on a vehicle traveling in the
    x direction (a great circle) with velocity <span class="i">v</span>.
    Show that the pendulum must tilt through a small angle ϕ about the x
    axis according to the equation,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0995.jpg](images/e9780486140520_i0995.jpg)

    </div>

    </div>

    where <span class="i">R</span> is the radius of earth.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i0996.jpg](images/e9780486140520_i0996.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 9</span>

    </div>

    </div>

10. If the vehicle of Prob. 9 accelerates along the x axis so that
    <span class="i">dv/dt</span> =
    <span class="i">a</span><sub><span class="i">x</span></sub><span class="i">,</span>
    show that

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0997.jpg](images/e9780486140520_i0997.jpg)

    </div>

    </div>

    The lower natural period of the pendulum, according to Prob. 8, now
    becomes,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i0998.jpg](images/e9780486140520_i0998.jpg)

    </div>

    </div>

    which is called the Schuler period, after Max Schuler of Germany,
    who extensively studied the problem.

</div>

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title87"></span>

# <span class="b">6.6 The Rate Gyro</span>

High–speed gyros serve as basic elements in many instruments for
guidance and control of moving vehicles.
<a href="#e9780486140520_c06.html#int_91"
id="e9780486140520_c06.html_ref_int_91" class="ref_int">Figure 6.6-1</a>
shows the essential elements of a rate gyro. The inner gimbal supporting
the spinning wheel is restrained by a spring which permits a limited
rotation about the outer gimbal which is fixed in the vehicle. The
<span class="i">Z</span> axis about which the vehicle turns is called
the input axis, and the axis of rotation of the inner gimbal is called
the output axis.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i0999.jpg](images/e9780486140520_i0999.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_91"
id="e9780486140520_c06.html_int_91" class="label_int"><span
class="b">Fig. 6.6-1</span></a><span class="b">. Rate gyro.</span>

</div>

</div>

If the vehicle makes a steady turn about the input axis at a rate
<span class="imageinline">![e9780486140520_i1000.jpg](images/e9780486140520_i1000.jpg)</span>
the rate of change of the angular momentum vector
<span class="i">Cn</span> is
<span class="imageinline">![e9780486140520_i1001.jpg](images/e9780486140520_i1001.jpg)</span>
which requires a moment equal to it about the output axis. This moment
is supplied by the torsional spring of stiffness
<span class="i">K</span>, as the output axis tilts by a small angle θ,
as shown in
<a href="#e9780486140520_c06.html#int_91" class="ref_int">Fig. 6.6-1</a>.
Equating the two moments, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1002.jpg](images/e9780486140520_i1002.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1003.jpg](images/e9780486140520_i1003.jpg)

</div>

<div class="caption">

(6.6–1)

</div>

</div>

and the output angle θ is proportional to the rate of turn
<span class="imageinline">![e9780486140520_i1004.jpg](images/e9780486140520_i1004.jpg)</span>
of the input axis or the vehicle itself.

The output angle θ is in general read electrically by a pickoff device.
One such device is the E–pickoff shown in
<a href="#e9780486140520_c06.html#int_92"
id="e9780486140520_c06.html_ref_int_92" class="ref_int">Fig. 6.6-2</a>.
The middle leg of the E is supplied by an alternating current, generally
of 400 cps. The two outer legs of the E are wound in opposition, so that
when the armature, attached to the output axis, is centered about the
middle leg, no voltage appears across the opposed outer coils connected
in series. When the armature is displaced due to θ, the magnetic flux
path is unbalanced, resulting in a voltage reading in the outer coils.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1005.jpg](images/e9780486140520_i1005.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_92"
id="e9780486140520_c06.html_int_92" class="label_int"><span
class="b">Fig. 6.6-2</span></a><span class="b">.</span> E–pickoff on
shaft.

</div>

</div>

In the undamped instrument, the output axis will overshoot the steady
angle θ and oscillate about it. To prevent this undesirable condition,
damping is generally provided, and its behavior can be established from
the following differential equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1006.jpg](images/e9780486140520_i1006.jpg)

</div>

<div class="caption">

(6.6–2)

</div>

</div>

where <span class="i">A</span> is the moment of inertia of the wheel and
inner gimbal about the output axis, and c the coefficient of viscous
damping. Thus the transient characteristics of the instrument can be
obtained from the homogeneous equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1007.jpg](images/e9780486140520_i1007.jpg)

</div>

<div class="caption">

(6.6–3)

</div>

</div>

where

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1008.jpg](images/e9780486140520_i1008.jpg)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title88"></span>

# <span class="b">6.7 The Integrating Gyros</span>

If the torsional spring restraining the output is replaced by a viscous
damper, the instrument becomes an integrating gyro. Equating the rate of
change of angular momentum to the viscous damping torque,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1009.jpg](images/e9780486140520_i1009.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1010.jpg](images/e9780486140520_i1010.jpg)

</div>

<div class="caption">

(6.7–1)

</div>

</div>

Thus the output angle θ is proportional to the integral of the input
angular rate which is the input angle itself.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title89"></span>

# <span class="b">6.8 The Stable Platform</span>

The principal function of the stable platform is to maintain a
space–fixed angular reference. It is an essential part of an inertial
guidance system. The platform makes use of the property of the
gyroscope, that a torque about an input axis (excluding the spin axis)
produces an angular velocity about the orthogonal (output) axis. In
general, three single–degree–of–freedom gyros oriented in mutually
perpendicular directions are mounted on the platform, as shown in
<a href="#e9780486140520_c06.html#int_93"
id="e9780486140520_c06.html_ref_int_93" class="ref_int">Fig. 6.8-1</a>.
The platform, in turn, is mounted on two gimbals which allow it three
degrees of angular freedom. If the platform is perfectly balanced and
the bearings are frictionless, no torque will be experienced by the
platform, and its orientation will be maintained regardless of the
motion of the carrier. However, due to unbalance and friction which
cannot be eliminated entirely, disturbing torques will be felt by the
platform. It is the function of the gyros to sense this disturbance and,
through a servo system, counteract the disturbing torque to produce
essentially a torque–free system.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1011.jpg](images/e9780486140520_i1011.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_93"
id="e9780486140520_c06.html_int_93" class="label_int"><span
class="b">Fig. 6.8-1</span></a><span class="b">.</span> Stable platform
for inertial guidance.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1012.jpg](images/e9780486140520_i1012.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_94"
id="e9780486140520_c06.html_int_94" class="label_int"><span
class="b">Fig. 6.8-2</span></a> Single–axis platform to maintain angular
orientation about <span class="i">y</span> axis.

</div>

</div>

The understanding of the dynamics of the stable platform can be obtained
by a discussion of the single–axis platform shown in
<a href="#e9780486140520_c06.html#int_94"
id="e9780486140520_c06.html_ref_int_94" class="ref_int">Fig. 6.8-2</a>,<sup>4</sup>
where the <span class="i">y</span> axis is the input axis and the x axis
(rotation of the spin axis) is the output axis. A disturbing torque
<span class="i">T</span><sub><span class="i">y</span></sub> about the
<span class="i">y</span> axis will rotate the spin axis, and, therefore,
<span class="b">h</span> through the angle 0, and the applied torque
minus the inertia torque about the <span class="i">y</span> axis must
equal the rate of change of the angular momentum h according to the
equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1013.jpg](images/e9780486140520_i1013.jpg)

</div>

<div class="caption">

(6.8–1)

</div>

</div>

where J<sub><span class="i">y</span></sub> is the moment of inertia of
the platform, and the gyro with its frame about the
<span class="i">y</span> axis. In the above equation, small angle
approximation is used for the right side which is justified since θ is
seldom allowed to become greater than 1°.

The precession
<span class="imageinline">![e9780486140520_i1014.jpg](images/e9780486140520_i1014.jpg)</span>
which is developed by
<span class="i">T</span><sub><span class="i">y</span></sub> results also
in a torque equation about the <span class="i">x</span> axis as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1015.jpg](images/e9780486140520_i1015.jpg)

</div>

<div class="caption">

(6.8–2)

</div>

</div>

where <span class="i">I</span><sub><span class="i">x</span></sub> is the
moment of inertia of the gyro and its frame about the x axis.

Using the Laplace transform notation
<span class="imageinline">![e9780486140520_i1016.jpg](images/e9780486140520_i1016.jpg)</span>
<span class="i">,</span> the two equations can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1017.jpg](images/e9780486140520_i1017.jpg)

</div>

<div class="caption">

(6.8–3)

</div>

</div>

Eliminating
<span class="imageinline">![e9780486140520_i1018.jpg](images/e9780486140520_i1018.jpg)</span>
we obtain the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1019.jpg](images/e9780486140520_i1019.jpg)

</div>

<div class="caption">

(6.8–4)

</div>

</div>

which defines the transfer function between the output
<span class="imageinline">![e9780486140520_i1020.jpg](images/e9780486140520_i1020.jpg)</span>
and the input disturbing torque
<span class="imageinline">![e9780486140520_i1021.jpg](images/e9780486140520_i1021.jpg)</span>
.

The angular velocity 6 of the gyro relative to the platform is sensed by
the electric pickoff, amplified and fed to a servomotor which applies a
counter torque
<span class="i">T</span><sub><span class="i">s</span></sub> opposing the
disturbing torque
<span class="i">T</span><sub><span class="i">y</span></sub><span class="i">.</span>
Generally the platform inertia
<span class="i">J</span><sub><span class="i">y</span></sub> is large so
that the nutation frequency
<span class="imageinline">![e9780486140520_i1022.jpg](images/e9780486140520_i1022.jpg)</span>
(see Eq. 6.3–19) is negligible. The approximate transfer function is
then equal to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1023.jpg](images/e9780486140520_i1023.jpg)

</div>

<div class="caption">

(6.8–5)

</div>

</div>

which enables the platform servosystem to be represented by the block
diagram of <a href="#e9780486140520_c06.html#int_95"
id="e9780486140520_c06.html_ref_int_95" class="ref_int">Fig. 6.8-3</a>,
where <span class="i">A(s)</span> is the transfer function of the
electric pickoff, amplifier, and the servo motor. With
<span class="i">A(s)</span> known, the stable platform’s dynamical
behavior can be studied for stability and drift characteristics.

The three–axis stable platform can be considered to be an assembly of
three single–axis platforms similar to those of the previous section,
but mounted in a single stable unit, as shown in
<a href="#e9780486140520_c06.html#int_93" class="ref_int">Fig. 6.8-1</a>.<sup>4</sup>
The analysis is more complex due to coupling between the three
rotations. For the discussion of the inertial guidance system, it is
sufficient to assume that there is a platform which will successfully
maintain a given orientation in space.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1024.jpg](images/e9780486140520_i1024.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_95"
id="e9780486140520_c06.html_int_95" class="label_int"><span
class="b">Fig. 6.8-3</span></a><span class="b">.</span> Block diagram
for the single–axis platform.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title90"></span>

# <span class="b">6.9 Three–Axis Platform (Resolution of Motion)</span>

The analysis of a three–axis platform is more complex owing to coupling
between the three rotations and the necessity of resolution of the
platform pickoff signals because of nonalignment of the gimbal and
platform axes.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1025.jpg](images/e9780486140520_i1025.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_96"
id="e9780486140520_c06.html_int_96" class="label_int"><span
class="b">Fig. 6.9-1</span></a><span class="b">.</span> Coupling in
three–axis platform.

</div>

</div>

<a href="#e9780486140520_c06.html#int_96"
id="e9780486140520_c06.html_ref_int_96" class="ref_int">Figure 6.9-1</a>
shows the angular momentum vectors of the x, <span class="i">y,</span> z
gyros. Letting θ<sub>x</sub>,
<span class="i">θ</span><sub><span class="i">y</span></sub><span class="i">,</span>
θ<sub>z</sub> be the outputs of the x, <span class="i">y,</span> z gyros
due to rotations φ<sub>x</sub>, φ<sub>y</sub>, φ<sub>z</sub> of the
input axes, the pickoff of each gyro must be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1026.jpg](images/e9780486140520_i1026.jpg)

</div>

<div class="caption">

(6.9–1)

</div>

</div>

With the gimbal axes lined up with the platform axes, the counteracting
torques called for by the pickoff signals are of the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1027.jpg](images/e9780486140520_i1027.jpg)

</div>

<div class="caption">

(6.9–2)

</div>

</div>

where
<span class="i">A</span><sub><span class="i">y</span></sub>(<span class="i">s</span>)
is the transfer function of the y servosystem. Thus the behavior of the
single axis platform is modified by the coupling term of the form
<span class="i">A</span><sub><span class="i">y</span></sub><span class="i">(s)
φ</span><sub><span class="i">x</span></sub><span class="i">(s).</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1028.jpg](images/e9780486140520_i1028.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_97"
id="e9780486140520_c06.html_int_97" class="label_int"><span
class="b">Fig. 6.9-2</span></a><span class="b">.</span> Block diagram of
three–axis platform

</div>

</div>

The block diagram of the three–axis platform consists of the three
uncoupled circuits of the form shown in
<a href="#e9780486140520_c06.html#int_95" class="ref_int">Fig. 6.8-3</a>
with additional connections corresponding to the coupling terms, −
<span class="i">A</span><sub><span class="i">x</span></sub>(<span class="i">s</span>)
<span class="i">φ</span><sub><span class="i">y</span></sub><span class="i">(s),
A</span><sub><span class="i">y</span></sub><span class="i">(s)
φ</span><sub><span class="i">x</span></sub><span class="i">(s),</span>
and
−<span class="i">A</span><sub><span class="i">z</span></sub><span class="i">(s)
φ</span><sub><span class="i">y</span></sub><span class="i">(s),</span>
as shown in <a href="#e9780486140520_c06.html#int_97"
id="e9780486140520_c06.html_ref_int_97" class="ref_int">Fig. 6.9-2</a>.

Assuming that the outer gimbal axis, originally parallel to the platform
x axis, is attached to the vehicle, as shown in
<a href="#e9780486140520_c06.html#int_98"
id="e9780486140520_c06.html_ref_int_98" class="ref_int">Fig. 6.9-3</a>,
and assuming that the vehicle is roll–stabilized, the motion of the
vehicle in pitch and yaw will cause the gimbal axes to deviate from the
platform axes. It is evident then that the platform torques
<span class="i">T</span><sub><span class="i">x</span></sub><span class="i">,
T</span><sub><span class="i">y</span></sub><span class="i">,
T</span><sub><span class="i">z</span></sub> must now be resolved along
the displaced gimbal axes where the torque servomotors act. Since the
countertorques are proportional to the platform pickoff signals, the
proper torques about the new gimbal axes are found by resolution of the
platform pickoff signals along the gimbal axes.

With the vehicle roll–stabilized, we first allow the vehicle to nose
down through a pitch angle Φ<sub>y</sub>. Letting the new gimbal axes be
indicated by primes, the components of the platform pickoff signals
along the gimbal axes are

<div class="blocktext">

<span class="i"><span class="b">ϭ</span></span><sub><span class="i"><span class="b">x′</span></span></sub>
= ϭ<sub>x</sub> cos Φ<sub><span class="i">y</span></sub> − ϭ<sub>z</sub>
sin Φ<sub>y</sub>  
ϭ<sub>y′</sub> = ϭ<sub><span class="i">y</span></sub>  
ϭ<sub>z’</sub> = ϭ<sub>x</sub> sin Φ<sub>y</sub> + ϭ<sub>z</sub> cos
Φ<sub>y</sub>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1029.jpg](images/e9780486140520_i1029.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_98"
id="e9780486140520_c06.html_int_98" class="label_int"><span
class="b">Fig. 6.9-3</span></a><span class="b">.</span> Gimbal rotation
requires resolution of torque.

</div>

</div>

Next allow a rotation Φ<sub>z</sub> in yaw about the z′ axis, and
resolve ϭ<sub>x′</sub> along the pitch gimbal axis and the new roll
axis,

<div class="blocktext">

<span class="imageinline">![e9780486140520_i1030.jpg](images/e9780486140520_i1030.jpg)</span>  
ϭ<sub>pitch</sub> =–ϭ<sub>x′</sub> tan Φ<sub>z</sub>

</div>

The resulting signal about the new gimbal axes of roll, pitch, and yaw
due to both Φ<sub>y</sub> and Φ<sub>z</sub> are, then,

<div class="blocktext">

ϭ<sub>roll</sub> = (ϭ<sub>x</sub> cos Φ<sub>y</sub> −
<span class="i">ϭ</span><sub><span class="i">z</span></sub> sin
Φ<sub>y</sub>) sec
<span class="i">Φ</span><sub><span class="i">z</span></sub>  
ϭ<sub>pitch</sub> = −(ϭ<sub>x</sub> cos Φ<sub>y</sub> − ϭ<sub>z</sub>
sin Φ<sub>y</sub>) tan Φ<sub>z</sub> + ϭ<sub>y</sub>  
ϭ<sub>yaw</sub> = (ϭ<sub>x</sub> sin Φ<sub>y</sub> + ϭ<sub>z</sub> cos
Φ<sub>y</sub>) = ϭ<sub>z′</sub>

</div>

which can be expressed in the following matrix notation.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1031.jpg](images/e9780486140520_i1031.jpg)

</div>

</div>

The function of the resolver is then to resolve the platform pickoff
signals ϭ<sub>x</sub>, ϭ<sub>y</sub>, ϭ<sub>z</sub> to the components
<span class="i">ϭ</span><sub><span class="i">roll</span></sub>,
ϭ<sub>pitch</sub>, ϭ<sub>yaw</sub> along the displaced gimbal axes
housing the roll, pitch, and yaw servomotors.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title91"></span>

# <span class="b">6.10 Inertial Navigation</span>

Navigation is the science of directing a vehicle to a destination by
determining its position. In inertial navigation this task is
accomplished without observation of landmarks, celestial bodies or radio
beams.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1032.jpg](images/e9780486140520_i1032.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_99"
id="e9780486140520_c06.html_int_99" class="label_int"><span
class="b">Fig. 6.10-1</span></a><span class="b">.</span> Accelerometer
and integrator.

</div>

</div>

A vehicle moving in space possesses six degrees of freedom, three
translational and three rotational. Consequently, six sensors are
needed. The stable platform discussed in Sec. 6.8 offers a reference for
the rotational motion, whereas the accelerometer is an instrument
capable of detecting translational motion. In fact, the three gyros of
the stable platform and the three accelerometers oriented in mutually
perpendicular directions can supply all the information for establishing
the motion of a rigid body, and the high degree of accuracy with which
this is being done has made inertial navigation a practical
reality.<sup>2,5,7</sup>

<a href="#e9780486140520_c06.html#int_99"
id="e9780486140520_c06.html_ref_int_99" class="ref_int">Figure
6.10-1</a> shows a schematic of an accelerometer and integrator.
Acceleration along its axis displaces the mass against the spring
according to Newton’s equation <span class="i">F</span> =
<span class="i">ma,</span> where <span class="i">F</span> is the spring
force. The displacement of the mass which is proportional to the
acceleration is picked off by a potentiometer and integrated to velocity
and displacement of the vehicle.

The accelerometers are mounted on a table which is always maintained
normal to the local radius of the earth. This is accomplished by means
of a computer and a clock which rotates the table relative to the stable
platform, as indicated in <a href="#e9780486140520_c06.html#int_100"
id="e9780486140520_c06.html_ref_int_100" class="ref_int">Fig. 6.10-2</a>.
In some cases the accelerometers are mounted directly on the stable
platform which is torqued to the normal position.

To obtain an understanding of how the inertial navigator works, we
assume that the vehicle starts at the equator and that the plane of the
stable platform is horizontal with the arrow pointing in the N polar
direction. If the vehicle moves towards the north along a longitude, and
the accelerometer table is always kept normal to the geocentric radius
r, the <span class="i">N–S</span> accelerometer will measure the
acceleration <span class="i">a</span><sub><span class="i">x</span></sub>
(see <a href="#e9780486140520_c06.html#int_100" class="ref_int">Fig.
6.10-2</a>). The proper rate of rotation of the table about the
<span class="i">y</span> axis is then
<span class="i">ω</span><sub><span class="i">y</span></sub> =
υ<sub>x</sub>/<span class="i">r</span>, where
<span class="i">v</span><sub><span class="i">x</span></sub> is
determined from the first integral of
<span class="i">a</span><sub><span class="i">x</span></sub><span class="i">.</span>
The latitude motor B then rotates the table at a rate ω<sub>y</sub> to
keep the <span class="i">N–S</span> line on the table normal to
<span class="i">r</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1033.jpg](images/e9780486140520_i1033.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_100"
id="e9780486140520_c06.html_int_100" class="label_int"><span
class="b">Fig. 6.10-2</span></a><span class="b">.</span> Components of
an inertial navigator.

</div>

</div>

Due to rotation of the earth towards the east, the
<span class="i">E</span>–<span class="i">W</span> line of the table must
be rotated by the longitude motor <span class="i">A</span> to unwind the
earth’s rotation. Since during the motion of the vehicle the orientation
of the stable platform remains fixed in inertial space (towards the N
star) the required rotation of the accelerometer table about the x axis
of the stable platform at any latitude is Ω or 15°/hr.

To this rotation must be added the rotation about the platform
<span class="i">x</span> axis due to the E–W motion of the vehicle
relative to the original longitude. By integrating the output of the E–W
accelerometer and dividing by <span class="i">r</span> cos λ, the
additional rotation to maintain the E–W line of the table normal to r is
<span class="i">ω</span><sub><span class="i">x</span></sub> =
ν<sub><span class="i">y</span></sub><span class="i">/r</span> cos λ.

These computations are performed by a computer which must be an integral
part of the inertial system. Thus the inertial navigator must consist of
the stable platform, accelerometers with integrators, a computer to
compute the proper angular rates of the table due to vehicle motion, a
clock to unwind the earth’s rotation, and the servomotors to actually
carry out these functions.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title92"></span>

# <span class="b">6.11 Oscillation of Navigational Errors</span>

The accelerometers mounted on the vehicle measure only the
nongravitational force
<span class="i">F</span><sub><span class="i">ng</span></sub> acting on
the vehicle, and therefore one must add to it the gravitational force
<span class="i">F</span><sub><span class="i">g</span></sub> in order to
determine the total force which determines the acceleration
a<sub>ν</sub> of the vehicle.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1034.jpg](images/e9780486140520_i1034.jpg)

</div>

<div class="caption">

(6.11–1)

</div>

</div>

For example if the vehicle is resting on the surface of the earth, the
verticle accelerometer will indicate the upward force (thrust) of the
ground on the vehicle, or
<span class="b">F</span><sub><span class="i">ng</span></sub> =
<span class="b">W.</span> To this must be added the gravitational
attraction of the earth on the vehicle
<span class="b">F</span><sub><span class="i">g</span></sub> =
−<span class="b">W</span> which results in the zero acceleration of the
vehicle.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1035.jpg](images/e9780486140520_i1035.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_101"
id="e9780486140520_c06.html_int_101" class="label_int"><span
class="b">Fig. 6.11-1</span></a>. Simplified block diagram of gravity
and position computation.

</div>

</div>

Equation 6.11–1 can be expressed entirely in terms of acceleration by
dividing by <span class="i">m</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1036.jpg](images/e9780486140520_i1036.jpg)

</div>

<div class="caption">

(6.11–2)

</div>

</div>

where <span class="b">A</span><sub><span class="i">ng</span></sub> is
the nongravitational (thrust) acceleration indicated by the
accelerometers. The vehicle position is then found by a double
integration of the vehicle acceleration
<span class="i">a</span><sub><span class="i">ν</span></sub> as shown by
the simplified block diagram of
<a href="#e9780486140520_c06.html#int_101"
id="e9780486140520_c06.html_ref_int_101" class="ref_int">Fig. 6.11-1</a>.
The gravitational acceleration a<sub><span class="i">g</span></sub>
which depends only on the position <span class="b">r</span> is computed
and added to the output of the accelerometers to give the vehicle
acceleration a<sub>ν</sub><span class="i">.</span>

It is evident that an accelerometer error would result in incorrect
rotation rates of the accelerometer table which would result in a
position error, an incorrect value of
a<sub><span class="i">g</span></sub>, and a deviation of the
accelerometer table from the normal to the true geocentric radius
<span class="b">r</span>. These errors are oscillatory for subsatellite
speeds, and we will now investigate their nature.

We will define the correct position of the vehicle by a vector
<span class="b">r</span> referenced to inertial coordinates with origin
at the center of earth. We will also define another set of coordinates
<span class="i">x, y, z</span> with origin coinciding with the correct
position of the vehicle and with the <span class="i">z</span> axis
parallel to <span class="b">r</span> as shown in
<a href="#e9780486140520_c06.html#int_102"
id="e9780486140520_c06.html_ref_int_102" class="ref_int">Fig. 6.11-2</a>.
Thus the angular velocity of the vehicle is specified by
<span class="i">ω</span><sub><span class="i">x</span></sub><span class="i">,
ω</span><sub><span class="i">y</span></sub><span class="i">,
ω</span><sub><span class="i">z</span></sub> respectively and the
<span class="i">xy</span> plane is always normal to the local geocentric
radius <span class="b">r</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1037.jpg](images/e9780486140520_i1037.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c06.html#ref_int_102"
id="e9780486140520_c06.html_int_102" class="label_int"><span
class="b">Fig. 6.11-2</span></a>. Vehicle position indicated by
<span class="b">r</span>. Origin of <span class="i">x, y, z</span>
coinciding with vehicle.

</div>

</div>

We now assume that the position of the vehicle is in error by

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1038.jpg](images/e9780486140520_i1038.jpg)

</div>

<div class="caption">

(6.11–3)

</div>

</div>

and examine first the error in
<span class="b">a</span><sub><span class="i">g</span></sub> =
−<span class="b">g</span>. Since <span class="b">g</span> is inversely
proportional to the square of the distance from the center of the earth,
the incorrect components of <span class="b">g</span> computed from
<span class="b">r</span> + <span class="b">Δr</span> are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1039.jpg](images/e9780486140520_i1039.jpg)

</div>

<div class="caption">

(6.11–4)

</div>

</div>

where −<span class="i">g</span> is the correct value and
ω<sub>0</sub><sup>2</sup> = <span class="i">g/r.</span>

The acceleration error of the vehicle can be determined from the general
equation for acceleration by replacing <span class="b">r</span> by
<span class="b">Δr</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1040.jpg](images/e9780486140520_i1040.jpg)

</div>

<div class="caption">

(6.11–5)

</div>

</div>

Substituting these quantities into the error equation,

<div class="blocktext">

Δa<sub>v</sub> = ΔA + Δg

</div>

its component equations can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1041.jpg](images/e9780486140520_i1041.jpg)

</div>

<div class="caption">

(6.11–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1042.jpg](images/e9780486140520_i1042.jpg)

</div>

<div class="caption">

(6.11–7)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1043.jpg](images/e9780486140520_i1043.jpg)

</div>

<div class="caption">

(6.11–8)

</div>

</div>

To interpret these equations, assume the vehicle to be traveling with
velocity <span class="i">v</span> in the <span class="i">y</span>
direction along a great circle at constant altitude. Then
<span class="i">ω</span><sub><span class="i">y</span></sub> =
<span class="i">ω</span><sub><span class="i">z</span></sub> = 0, and
<span class="i">ω</span><sub><span class="i">x</span></sub> =
−<span class="i">v/r.</span> The above equations reduce to,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1044.jpg](images/e9780486140520_i1044.jpg)

</div>

<div class="caption">

(6.11–9)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1045.jpg](images/e9780486140520_i1045.jpg)

</div>

<div class="caption">

(6.11–10)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1046.jpg](images/e9780486140520_i1046.jpg)

</div>

<div class="caption">

(6.11–11)

</div>

</div>

The first two equations have solutions which are harmonic oscillations
of frequency
<span class="imageinline">![e9780486140520_i1047.jpg](images/e9780486140520_i1047.jpg)</span>and
<span class="imageinline">![e9780486140520_i1048.jpg](images/e9780486140520_i1048.jpg)</span>The
solution of the third equation is hyperbolic and
Δ<span class="i">z</span> must diverge.

For ordinary altitudes, the period as computed from ω<sub>0</sub> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1049.jpg](images/e9780486140520_i1049.jpg)

</div>

<div class="caption">

(6.11–12)

</div>

</div>

and the inertial system is often referred to as the 84–min Schuler
pendulum. As v approaches orbital speeds for satellites,
ω<sub>0</sub><sup>2</sup>–(<span class="i">υ</span><sup><span class="i">2</span></sup><span class="i">/r</span><sup><span class="i">2</span></sup>)
will approach zero and the desirable oscillatory nature of the position
error disappears.

In addition, we might mention briefly the error introduced by the
deviation from normal of the acceleration table. If the table tilts by a
small angle Φ = φ<sub>x</sub>i + φ<sub>y</sub>j + φ<sub>z</sub>k, the
error in the accelerometer output will be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1050.jpg](images/e9780486140520_i1050.jpg)

</div>

<div class="caption">

(6.11–13)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  An aircraft directional gyro has a spin angular momentum of
    <span class="i">h</span> = 3.0 Ib–in./sec. If the drift rate is
    specified as 0.01 °/hr, determine the torque producing the drift.
2.  An inertial system is to guide an airplane traveling at a speed of
    600 mph to a destination of 1000 miles with an accuracy of ½ mile.
    Determine the allowable drift rate.
3.  Assume that for the single–axis stable platform of
    <a href="#e9780486140520_c06.html#int_94" class="ref_int">Fig. 6.8-2</a>
    there is damping and spring stiffness restraining the rotation of
    the output axis. Write the equation for the torque about the output
    axis.
4.  Write the subsidiary equation for the single–axis platform including
    damping and spring stiffness, and draw the new block diagram.
5.  For the single–axis platform of Prob. 3, determine the transfer
    function <span class="i">θ(s)/φ(s)</span> and discuss the special
    cases when: (<span class="i">a</span>) damping = 0;
    (<span class="i">b</span>) spring stiffness = 0;
    <span class="i">(c)</span> damping and spring stiffness = 0.
    Indicate the type of gyro obtained in each case.
6.  . For case (<span class="i">c</span>) of Prob. 5, obtain the
    transfer function
    <span class="i">T</span><sub><span class="i">s</span></sub><span class="i">/T</span><sub><span class="i">d</span></sub><span class="i">,</span>
    where <span class="i">T</span><sub><span class="i">d</span></sub>
    and <span class="i">T</span><sub><span class="i">s</span></sub> are
    the disturbing torque and the servo countertorque, and discuss the
    influence of <span class="i">A(s)</span> on the system.
7.  Obtain the stiffness characteristics of the single–axis platform by
    examining the transfer functions
    <span class="i">T</span><sub><span class="i">d</span></sub>(<span class="i">s</span>)/<span class="i">θ</span>(<span class="i">s</span>)
    and
    <span class="i">T</span><sub><span class="i">d</span></sub>(<span class="i">s</span>)/<span class="i">φ</span>(<span class="i">s</span>).
8.  A three–axis stable platform has gyros mounted as shown in the
    sketch. Identify which are the <span class="i">x, y,</span> and
    <span class="i">z</span> gyros and determine the equations for the
    pickoff signals, using
    <span class="i">φ</span><sub><span class="i">i</span></sub> for
    input and
    <span class="i">θ</span><sub><span class="i">i</span></sub> for
    output.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1051.jpg](images/e9780486140520_i1051.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 8</span>

    </div>

    </div>
9.  If the three–axis platform has gyros arranged as shown, identify the
    <span class="i">x, y,</span> and <span class="i">z</span> gyros and
    determine the equations for the pickoff signals.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1052.jpg](images/e9780486140520_i1052.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 9</span>

    </div>

    </div>
10. Draw a block diagram for the dynamics of the platform of Prob. 9.
11. If the platform of Prob. 9 is mounted on a missile with the
    roll–stabilized axis along the x axis, determine the equations for
    the resolver signal along the servo roll, pitch, and yaw axes due to
    angular rotations φ<sub><span class="i">y</span></sub> and
    φ<sub><span class="i">z</span></sub>.
12. An airplane with an inertial navigator is headed in the direction N
    60° W at latitude 32° N, at speed 600 mph. Determine the angular
    rates about the meridian and latitude axes due to the motion and the
    required angular rates of the accelerometer table.
13. A rocket ship guided by an inertial navigator is traveling along a
    great circle route at constant altitude of 100 miles and at a speed
    of 12,000 mph. With the horizontal axis <span class="i">y</span>
    oriented along the flight path, discuss the nature of the
    navigational errors and calculate the frequency of the oscillatory
    error.

</div>

<div class="section1">

<span id="e9780486140520_c06.html_title93"></span>

# <span class="b">REFERENCES</span>

1.  Cunningham, W. J., <span class="i">Nonlinear Analysis</span>,
    McGraw–Hill Book Co., New York (1958), p. 125.
2.  Frye, E., “Fundamentals of Inertial Guidance and Navigation,” J.
    <span class="i">Astronaut. Sci.,</span> V, No. 1 (1958), 1.
3.  Malkin, I. G., “Some Problems in the Theory of Nonlinear
    Oscillations,” Translation Series, <span class="i">Atomic Energy
    Commission, AEC–tr–3766</span> (Book 1), Chapter 1.
4.  Mitsutomi, T., “Characteristics and Stabilization of an Inertial
    Platform,” <span class="i">Trans. IRE, Aeronautical and Navigational
    Electronics</span> (June 1958), 95–105.
5.  O’Donnell, C. F., “Inertial Navigation,” <span class="i">J. Franklin
    Institute</span>, 266, Nos. 4 and 5 (Oct. and Nov. 1958).
6.  Plymale, B. T., and Goodstein, R., “Nutation of a Free Gyro Subject
    to an Impulse,” <span class="i">J. Appl. Mech.</span>, 22, No. 3
    (Sept. 1955), 365–366.
7.  Slater, J. M., and Duncan, D. B., “Inertial Navigation,”
    <span class="i">Aeronaut. Eng. Review,</span> 15, No. 1 (Jan. 1956).
8.  Stoker, J. J., <span class="i">Nonlinear Vibrations</span>,
    Interscience Publishers, New York (1950), p. 98.
9.  Streeter, J. R., “Error Analysis of an Inertial System in Vehicles
    of High Speed,” Master of Science Thesis in Engineering, University
    of California, Los Angeles (June 1960).
10. Thomson, W. T., <span class="i">Laplace Transformation</span> (2nd
    ed.), Prentice–Hall, Englewood Cliffs, N.J. (1960).
11. Wrigley, W., Woodbury, R. B., and Hovorka, J., “Application of
    Inertial Guidance Principles” Automatic Control, 7, No. 1, 22 (July
    1957).
12. Pitman, G. R., “Inertial Guidance” John Wiley & Sons, Inc. New York
    (1962).

</div>

</div>

<span id="e9780486140520_c07.html"></span>

<div class="chapter">

<span id="e9780486140520_c07.html_title94"></span>

# <span class="b">CHAPTER 7</span>

# <span class="b">Space Vehicle Motion</span>

<div class="section1">

<span id="e9780486140520_c07.html_title95"></span>

# <span class="b">7.1 General Equations in Body Coordinates</span>

For rockets and space vehicles it is often necessary to consider the
general problem of the spinning body under thrust. The concern here is
the body attitude and the motion of the center of mass. We will first
consider problems where the rate of mass variation is small enough to be
negligible.

To outline the problem at hand, we will consider a rigid body and define
a set of body–fixed axes x, y, z rotating with angular velocity ω, and
with the origin coinciding with the center of mass. Although it is
always desirable to let the body axes coincide with the principal axes,
this is often not possible, so that, in the general case, the moments
and products of inertia will be defined as

<div class="blocktext">

<span class="i">I</span><sub><span class="i">x</span></sub>
<span class="i">= A I</span><sub><span class="i">xy</span></sub>
<span class="i">= D</span>  
<span class="i">I</span><sub><span class="i">y</span></sub>
<span class="i">= B I</span><sub><span class="i">xz</span></sub>
<span class="i">= E</span>  
<span class="i">I</span><sub><span class="i">z</span></sub>
<span class="i">= C I</span><sub><span class="i">yx</span></sub>
<span class="i">= F</span>

</div>

The angular momentum (Eq. 5.2–7) in the above notation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1053.jpg](images/e9780486140520_i1053.jpg)

</div>

<div class="caption">

(7.1–1)

</div>

</div>

and the moment equation about the body axes

<div class="blocktext">

<span class="b">M = \[ḣ\] + ω × h</span>

</div>

can be written out in terms of the components given by Eq. 5.6–3 as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1054.jpg](images/e9780486140520_i1054.jpg)

</div>

<div class="caption">

(7.1–2)

</div>

</div>

We next let the velocity of the center of mass be expressed by the
equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1055.jpg](images/e9780486140520_i1055.jpg)

</div>

<div class="caption">

(7.1–3)

</div>

</div>

and the force as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1056.jpg](images/e9780486140520_i1056.jpg)

</div>

<div class="caption">

(7.1–4)

</div>

</div>

Since the <span class="i">x, y, z</span> coordinates are rotating with
the body, the force components in the <span class="i">x, y, z</span>
directions are determined from the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1057.jpg](images/e9780486140520_i1057.jpg)

</div>

<div class="caption">

(7.1–5)

</div>

</div>

to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1058.jpg](images/e9780486140520_i1058.jpg)

</div>

<div class="caption">

(7.1–6)

</div>

</div>

If the resultant of the above forces does not pass through the center of
mass coinciding with the origin of the <span class="i">x, y, z,</span>
axes, Eqs. (7.1–2) and (7.1–6) become coupled owing to the moment of the
force. Also these equations define the motion of the body only in terms
of the linear and angular velocities referred to body axes, and their
solution and transformation to displacements and angles relative to
inertial coordinates are problems of considerable difficulty which can
be accomplished only under simplifying assumptions.

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title96"></span>

# <span class="b">7.2 Thrust Misalignment</span>

We will consider first a simple problem of a spinning missile with a
misalignment of the thrust line. We will assume that the missile is
symmetric so that the <span class="i">x, y, z</span>, axes coincide with
the principal axes 1, 2, 3 with
<span class="i">I</span><sub><span class="i">1</span></sub> =
<span class="i">I</span><sub><span class="i">2</span></sub>
<span class="i">= A</span> and
<span class="i">I</span><sub><span class="i">3</span></sub>
<span class="i">= C.</span> With <span class="i">A = B</span>, we can
rotate the 1, 2 axes so that one of these axes, say 1, is perpendicular
to the plane containing the thrust and axis 3, as shown in
<a href="#e9780486140520_c07.html#int_103"
id="e9780486140520_c07.html_ref_int_103" class="ref_int">Fig. 7.2-1</a>.

Euler’s equation for the missile is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1059.jpg](images/e9780486140520_i1059.jpg)

</div>

<div class="caption">

(7.2–1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1060.jpg](images/e9780486140520_i1060.jpg)

</div>

<div class="caption">

(7.2–2)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1061.jpg](images/e9780486140520_i1061.jpg)

</div>

<div class="caption">

(7.2–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1062.jpg](images/e9780486140520_i1062.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_103"
id="e9780486140520_c07.html_int_103" class="label_int"><span
class="b">Fig. 7.2-1</span></a>. Thrust misalignment resulting in moment
M<sub>1</sub>.

</div>

</div>

The third equation tells us that
<span class="i">ω</span><sub><span class="i">3</span></sub>
<span class="i">= n</span>, a constant. Although
<span class="i">C</span> is generally less than <span class="i">A</span>
for missiles, we let

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1063.jpg](images/e9780486140520_i1063.jpg)

</div>

<div class="caption">

(7.2–4)

</div>

</div>

as in Sec. 5.8–3 and rewrite the first two equations as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1064.jpg](images/e9780486140520_i1064.jpg)

</div>

<div class="caption">

(7.2–5)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1065.jpg](images/e9780486140520_i1065.jpg)

</div>

<div class="caption">

(7.2–6)

</div>

</div>

For the solution of these equations, we will use the technique used in
Sec. 5.8 of adding
<span class="i">ω</span><sub><span class="i">1</span></sub> and
<span class="i">ω</span><sub><span class="i">2</span></sub> in
quadrature. Multiplying Eq. 7.2–6 by i =
<span class="imageinline">![e9780486140520_i1066.jpg](images/e9780486140520_i1066.jpg)</span>adding
it to Eq. 7.2–5, and letting <span class="i">ω</span><sub>12</sub>
<span class="i">= ω</span><sub>1</sub> <span class="i">+
iω</span><sub>2</sub>, the two equations for
<span class="i">ω</span><sub>1</sub> and
<span class="i">ω</span><sub>2</sub> are replaced by one

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1067.jpg](images/e9780486140520_i1067.jpg)

</div>

<div class="caption">

(7.2–7)

</div>

</div>

Using the method of Laplace transformation, its subsidiary equation
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1068.jpg](images/e9780486140520_i1068.jpg)

</div>

<div class="caption">

(7.2–8)

</div>

</div>

and its solution given by its inverse is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1069.jpg](images/e9780486140520_i1069.jpg)

</div>

<div class="caption">

(7.2–9)

</div>

</div>

The separation of this equation to ω<sub>1</sub> and ω<sub>2</sub> is
easily accomplished by noting its real and imaginary parts.

<span class="b">PROBLEMS</span>

1.  From Eq. 7.2–6,
    <span class="imageinline">![e9780486140520_i1070.jpg](images/e9780486140520_i1070.jpg)</span>.
    Substitution into Eq. 7.2–5 results in

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1071.jpg](images/e9780486140520_i1071.jpg)

    </div>

    </div>

    Solve this equation for
    <span class="i">ω</span><sub><span class="i">2</span></sub> and show
    that

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1072.jpg](images/e9780486140520_i1072.jpg)

    </div>

    </div>

2.  . From <span class="i">ω</span><sub>1</sub> = (1/λ)ὼ<sub>2</sub> and
    the solution of Prob. 1, determine the solution for
    <span class="i">ω</span><sub>1</sub>(<span class="i">t</span>).

3.  . Note that the procedure of Prob. 2 encounters differentiation of
    an integral.

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1073.jpg](images/e9780486140520_i1073.jpg)

    </div>

    </div>

    The result is

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1074.jpg](images/e9780486140520_i1074.jpg)

    </div>

    </div>

4.  . Separate the Eq. 7.2–9, <span class="i">ω</span><sub>12</sub>
    <span class="i">= ω</span><sub>1</sub> <span class="i">+
    iω</span><sub>2</sub>, into its real and imaginary parts and verify
    the solutions for <span class="i">ω</span><sub>1</sub> and
    <span class="i">ω</span><sub>2</sub> of Probs. 1, 2, and 3.

5.  . A symmetric body, <span class="i">A, A, C</span>, is damped with
    moments about the body–fixed axes as follows:
    <span class="i">M</span><sub>1</sub> =
    −<span class="i">kω</span><sub>1</sub><span class="i">,
    M</span><sub>2</sub> = −<span class="i">kω</span><sub>2</sub>,
    <span class="i">M</span><sub>3</sub> =
    −<span class="i">kω</span><sub>3</sub>. Show that the angle between
    the spin axis, (axis 3) and the angular momentum vector is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1075.jpg](images/e9780486140520_i1075.jpg)

    </div>

    </div>

6.  A symmetrical satellite with moments of inertia <span class="i">A,
    A, C</span> is spinning with angular velocity ω about the axis of
    <span class="i">C</span>. If a constant torque
    <span class="i">M</span><sub>1</sub> is applied to the transverse
    body–fixed pitch axis, show that the angular velocity of the
    satellite is
    <span class="i">ω</span><sub><span class="i">z</span></sub>
    <span class="i">= n</span>
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1076.jpg](images/e9780486140520_i1076.jpg)

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title97"></span>

# <span class="b">7.3 Rotations Referred to Inertial Coordinates</span>

The solution of the previous problem is in terms of body–fixed
coordinates which are rotating. In order to transform from the
body–fixed coordinates to the inertial coordinates <span class="i">X, Y,
Z</span> it is necessary to introduce Euler’s angles. From Eq. 3.5–1 the
transformation is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1077.jpg](images/e9780486140520_i1077.jpg)

</div>

<div class="caption">

(7.3–1)

</div>

</div>

Adding <span class="i">ω</span><sub>1</sub> and
<span class="i">ω</span><sub>2</sub> in quadrature,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1078.jpg](images/e9780486140520_i1078.jpg)

</div>

<div class="caption">

(7.3–2)

</div>

</div>

From <span class="i">ω</span><sub>3</sub>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1079.jpg](images/e9780486140520_i1079.jpg)

</div>

<div class="caption">

(7.3–3)

</div>

</div>

which, substituted into Eq. 7.3–2, results in

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1080.jpg](images/e9780486140520_i1080.jpg)

</div>

<div class="caption">

(7.3–4)

</div>

</div>

Although this equation relates the angular velocity
<span class="i">ω</span><sub>12</sub> about the body–fixed coordinates
in terms of Euler’s angles referenced to inertial axes, further
simplification generally requires a small angle approximation for
<span class="i">θ</span>. Such an approximation is often justified when
dealing with rockets and missiles whose spin axis must not deviate
greatly from a fixed direction of flight.

When <span class="i">θ</span> is small tan <span class="i">θ</span> can
be replaced by <span class="i">θ</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1081.jpg](images/e9780486140520_i1081.jpg)

</div>

<div class="caption">

(7.3–5)

</div>

</div>

At this point we introduce a complex angle of attack, proposed by H.
Leon<sup>4</sup>·<sup>5</sup>, which uncouples Eq. 7.3–5.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1082.jpg](images/e9780486140520_i1082.jpg)

</div>

<div class="caption">

(7.3–6)

</div>

</div>

Differentiating

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1083.jpg](images/e9780486140520_i1083.jpg)

</div>

<div class="caption">

(7.3–7)

</div>

</div>

Equation 7.3–5 can then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1084.jpg](images/e9780486140520_i1084.jpg)

</div>

<div class="caption">

(7.3–8)

</div>

</div>

so that when <span class="i">ω</span><sub>12</sub> is a known function
of time we have a first–order ordinary differential equation in
<span class="i">θ</span><sub>12</sub> to solve. It must be remembered
however that the above procedure is limited to problems where
<span class="i">θ</span> is small.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1085.jpg](images/e9780486140520_i1085.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_104"
id="e9780486140520_c07.html_int_104" class="label_int"><span
class="b">Fig. 7.3-1</span></a><span class="b">.</span> Velocity
components in transverse plane tilted by angle <span class="i">θ</span>.

</div>

</div>

At this point the significance of the term e<sup>−iϕ</sup> appearing in
the various equations should be pointed out. For example, consider Eq.
7.3–2, which is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1086.jpg](images/e9780486140520_i1086.jpg)

</div>

</div>

All of the components in this equation lie in the tilted transverse
plane which are shown in <a href="#e9780486140520_c07.html#int_104"
id="e9780486140520_c07.html_ref_int_104" class="ref_int">Fig. 7.3-1</a>.

Writing e<sup>−<span class="i">iϕ</span></sup> = (cos
<span class="i">ϕ</span> − i sin <span class="i">ϕ</span>),
ω<sub>12</sub> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1087.jpg](images/e9780486140520_i1087.jpg)

</div>

<div class="caption">

(7.3–9)

</div>

</div>

The real and imaginary parts of this equation are, however, equal to the
components of 6 and
<span class="imageinline">![e9780486140520_i1088.jpg](images/e9780486140520_i1088.jpg)</span>
sin <span class="i">θ</span> along axes 1 and 2. Thus the multiplication
of the components
<span class="imageinline">![e9780486140520_i1089.jpg](images/e9780486140520_i1089.jpg)</span>along
the node coordinate system by e<sup>−<span class="i">iϕ</span></sup>
results in <span class="i">ω</span><sub>1</sub> <span class="i">+
iω</span><sub>2</sub><span class="i">,</span> the components along the
body–fixed axes rotated through an angle <span class="i">ϕ</span> from
the node axis. It follows logically then that, if we multiply the
components <span class="i">ω</span><sub>1</sub> <span class="i">+
iω</span><sub>2</sub> along the body axes by
<span class="i">e</span><sup><span class="i">iϕ</span></sup>, we should
obtain the vector <span class="i">ω</span><sub>12</sub> in terms of the
node axis components as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1090.jpg](images/e9780486140520_i1090.jpg)

</div>

<div class="caption">

(7.3–10)

</div>

</div>

We can now attach physical significance to the complex angle of attack
<span class="i">θ</span><sub>12</sub> <span class="i">=
θe</span><sup><span class="i">−iϕ</span></sup>. Since
<span class="i">θ</span> is multiplied by
<span class="i">e</span><sup><span class="i">−iϕ</span></sup><span class="i">,
θ</span><sub>12</sub> is resolved into components along the body–fixed
axes 1 and 2. (Although an angle is strictly not representable as a
vector, we have assumed <span class="i">θ</span> to be small, thereby
justifying its vector presentation.) To restore <span class="i">θ</span>
along its node axis we multiply <span class="i">θ</span><sub>12</sub> by
<span class="i">e</span><sup><span class="i">iϕ</span></sup><span class="i">,
i.e., θ =
θ</span><sub>12</sub><span class="i">e</span><sup><span class="i">iϕ</span></sup>.
Furthermore, if we wish to examine <span class="i">θ</span><sub>12</sub>
in terms of inertial components, we need only to multiply
<span class="i">θ</span> by
<span class="i">e</span><sup><span class="i">iϕ</span></sup> (assuming
<span class="i">ψ</span> measured in the <span class="i">XY</span> plane
to be equal to that measured in the tilted plane for
<span class="i">θ</span> small), or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1091.jpg](images/e9780486140520_i1091.jpg)

</div>

<div class="caption">

(7.3–11)

</div>

</div>

where

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1092.jpg](images/e9780486140520_i1092.jpg)

</div>

</div>

<span class="b">Example 7.3–1</span>

For a body of revolution <span class="i">A, A, C,</span> under
moment–free condition, the complex angular rate from Eq. 7.2–9 is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1093.jpg](images/e9780486140520_i1093.jpg)

</div>

<div class="caption">

<span class="i">(a)</span>

</div>

</div>

where <span class="i">λ</span> =
<span class="i">n</span>\[(<span class="i">C</span> −
<span class="i">A</span>)/<span class="i">A</span>\]. Substitution into
Eq. 7.3–8 results in the differential equation for the complex angle of
attack

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1094.jpg](images/e9780486140520_i1094.jpg)

</div>

<div class="caption">

<span class="i">(b)</span>

</div>

</div>

Letting <span class="i">θ</span><sub>12</sub><span class="i">(s)</span>
be the Laplace transform of
<span class="i">θ</span><sub>12</sub><span class="i">(t)</span>, the
subsidiary equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1095.jpg](images/e9780486140520_i1095.jpg)

</div>

<div class="caption">

<span class="i">(c)</span>

</div>

</div>

From its inverse, the solution for
<span class="i">θ</span><sub>12</sub><span class="i">(t)</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1096.jpg](images/e9780486140520_i1096.jpg)

</div>

<div class="caption">

<span class="i">(d)</span>

</div>

</div>

which is referred to body–fixed axes.

To examine the angle of attack in terms of the inertial axes, we
multiply by
<span class="i">e</span><sup><span class="i">int</span></sup> to obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1097.jpg](images/e9780486140520_i1097.jpg)

</div>

<div class="caption">

<span class="i">(e)</span>

</div>

</div>

The real and imaginary components of
<span class="i">θ</span><sub>12</sub><span class="i">(t)</span> are
along the X and <span class="i">Y</span> axes, the end of the vector
<span class="i">θ</span><sub><span class="i">XY</span></sub><span class="i">(t)</span>
prescribing a circle of radius
\[<span class="i">ω</span><sub><span class="i">12</span></sub>(0)\]/<span class="i">(n +
λ)</span> about the center <span class="i">θ</span><sub>12</sub>(0) +
<span class="i">i</span>\[<span class="i">ω</span><sub>12</sub>(0)\]/<span class="i">(n +
λ)</span>, as shown in <a href="#e9780486140520_c07.html#int_105"
id="e9780486140520_c07.html_ref_int_105" class="ref_int">Fig. 7.3-2</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1098.jpg](images/e9780486140520_i1098.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_105"
id="e9780486140520_c07.html_int_105" class="label_int"><span
class="b">Fig. 7.3-2</span></a>. Inertial components of angle of attack
<span class="i">θ.</span>

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title98"></span>

# <span class="b">7.4 Near Symmetric Body of Revolution with Zero Moment</span>

When the geometric axes <span class="i">x, y, z</span> corresponding to
yaw, pitch, and spin of a missile are not principal axes, the solution
in terms of such body coordinates will require the solving of the
general Eq. 7.1–2. These equations do not lead to a simple solution,
even for small products of inertia, and it is desirable to take a
different approach.

We recognize first that every body has a set of principal axes 1, 2, 3.
For the near symmetric body, the principal axis 3 deviates only by a
small angle <span class="i">β</span> from the spin axis
<span class="i">z</span>, as shown in
<a href="#e9780486140520_c07.html#int_106"
id="e9780486140520_c07.html_ref_int_106" class="ref_int">Fig. 7.4-1</a>.
Without loss of generality, the transverse axis <span class="i">x</span>
can be chosen normal to the plane <span class="i">z</span>03, and the
other two axes 1 and 2 are defined by the angle Φ between axis 1 and the
transverse axis x which intersects the planes 1, 2 and
<span class="i">xy</span>. Since both the 1, 2, 3 and <span class="i">x,
y, z</span> axes are body–fixed axes, <span class="i">β</span> and Φ are
constants.

If we assume that the principal inertias
<span class="i">I</span><sub><span class="i">1</span></sub> ≅
<span class="i">I</span><sub>2</sub>, then elementary solutions are
available in terms of principal axes 1, 2, 3. The motion of the
geometric axes <span class="i">x, y, z</span> can then be obtained by a
transformation of coordinates with <span class="i">β</span> and Φ known.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1099.jpg](images/e9780486140520_i1099.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_106"
id="e9780486140520_c07.html_int_106" class="label_int"><span
class="b">Fig. 7.4-1</span></a>. Principal axes 1, 2, 3 displaced from
missile axes <span class="i">x, y, z</span>. Axis x is normal to plane
z03.

</div>

</div>

We will assume that the moments and products of inertia about the
missile axes <span class="i">x, y, z</span> are

<div class="blocktext">

<span class="i">I</span><sub><span class="i">x</span></sub><span class="i">=
A</span>  
<span class="i">I</span><sub><span class="i">xy</span></sub><span class="i">=
D</span>  
<span class="i">I</span><sub><span class="i">y</span></sub><span class="i">=
B</span>  
<span class="i">I</span><sub><span class="i">xz</span></sub><span class="i">=
E</span>  
<span class="i">I</span><sub><span class="i">z</span></sub><span class="i">=
C</span>  
<span class="i">I</span><sub><span class="i">yz</span></sub><span class="i">=
F</span>

</div>

They are related to the principal moments of inertia
<span class="i">I</span><sub>1</sub><span class="i">,
I</span><sub>2</sub><span class="i">, I</span><sub>3</sub> by the
equations of Sec. 5.4 as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1100.jpg](images/e9780486140520_i1100.jpg)

</div>

<div class="caption">

(7.4–1)

</div>

</div>

The direction cosines used in the above equations are obtained from the
matrix transformation between coordinates <span class="i">x, y, z</span>
and 1, 2, 3 with lengths <span class="i">x′, y′, z′</span> along it (see
Sec. 5.4). Since <span class="i">β</span> is small, the approximation
sin <span class="i">β = β</span> and cos <span class="i">β</span> = I is
used:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1101.jpg](images/e9780486140520_i1101.jpg)

</div>

<div class="caption">

(7.4–2)

</div>

</div>

If we assume <span class="i">I</span><sub>1</sub> =
<span class="i">I</span><sub>2</sub>, Eqs. 7.4–1 reduce to the following

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1102.jpg](images/e9780486140520_i1102.jpg)

</div>

<div class="caption">

(7.4–3)

</div>

</div>

and the angle <span class="i">β</span> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1103.jpg](images/e9780486140520_i1103.jpg)

</div>

<div class="caption">

(7.4–4)

</div>

</div>

To solve for the angular velocities, we first write down the
transformation from the missile axes to the principal axes, assuming
<span class="i">β</span> to be small:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1104.jpg](images/e9780486140520_i1104.jpg)

</div>

<div class="caption">

(7.4–5)

</div>

</div>

Adding <span class="i">ω</span><sub>1</sub> and
<span class="i">iω</span><sub>2</sub>, where <span class="i">i</span> =
<span class="imageinline">![e9780486140520_i1105.jpg](images/e9780486140520_i1105.jpg)</span>,we
obtain the complex angular velocity

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1106.jpg](images/e9780486140520_i1106.jpg)

</div>

<div class="caption">

(7.4–6)

</div>

</div>

where <span class="i">ω</span><sub><span class="i">z</span></sub>
<span class="i">≅ n</span>. By multiplying Eq. 7.4–6 by
<span class="i">e</span><sup><span class="i">iφ</span></sup>, this
equation may also be written in the inverse form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1107.jpg](images/e9780486140520_i1107.jpg)

</div>

<div class="caption">

(7.4–7)

</div>

</div>

<a href="#e9780486140520_c07.html#int_107"
id="e9780486140520_c07.html_ref_int_107" class="ref_int">Figure
7.4-2</a> shows the relationship between the missile axes
<span class="i">x, y, z,</span> the principal axes 1, 2, 3, the inertial
axes X, <span class="i">Y, Z</span>, and the line of nodes
<span class="i">ξ</span>. The missile axis x is normal to axes 3 and z,
whereas the line of nodes <span class="i">ξ</span> is normal to axes
<span class="i">z</span> and <span class="i">Z</span>. The position of
the missile axes <span class="i">x, y, z</span> is obtained by starting
with the missile spin axis z coinciding with <span class="i">Z</span>
and performing three rotations as follows: (1) rotation of
<span class="i">ψ</span> about <span class="i">Z</span>; (2) rotation of
<span class="i">θ</span> about <span class="i">ξ;</span> and (3)
rotation of <span class="i">ϕ</span> about the spin axis
<span class="i">z</span>. The principal axes 1, 2, 3 are then referenced
to the <span class="i">x, y, z</span> axes by the fixed angles
<span class="i">β</span> and Φ.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1108.jpg](images/e9780486140520_i1108.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_107"
id="e9780486140520_c07.html_int_107" class="label_int"><span
class="b">Fig. 7.4-2</span></a>. Principal axes 1, 2, 3 referred to
missile axes <span class="i">x, y, z</span>, which, in turn, are
referred to node axis <span class="i">ξ</span> and inertial axes
<span class="i">X, Y, Z</span>.

</div>

</div>

From Ex. 7.3–1 we have the solution for the moment–free body in terms of
the principal axes with <span class="i">I</span><sub>1</sub> =
<span class="i">I</span><sub>2</sub>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1109.jpg](images/e9780486140520_i1109.jpg)

</div>

<div class="caption">

(7.4–8)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1110.jpg](images/e9780486140520_i1110.jpg)

</div>

<div class="caption">

(7.4–9)

</div>

</div>

where <span class="i">λ</span> =
<span class="i">n</span>\[(<span class="i">I</span><sub>3</sub>–<span class="i">I</span><sub>1</sub>)/<span class="i">I</span><sub>1</sub>\].
From Eq. 7.4–6, the initial value
<span class="i">ω</span><sub>12</sub>(0) is found to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1111.jpg](images/e9780486140520_i1111.jpg)

</div>

<div class="caption">

(7.4–10)

</div>

</div>

Substituting Eq. 7.4–10 into Eq. 7.4–8, and Eq. 7.4–8 into Eq. 7.4–7, we
have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1112.jpg](images/e9780486140520_i1112.jpg)

</div>

<div class="caption">

(7.4–11)

</div>

</div>

which transforms the complex angular rate solution to the missile axes
<span class="i">x, y, z.</span>

As discussed in Sec. 7.3,
<span class="i">θ</span><sub><span class="i">xy</span></sub> =
<span class="i">θe</span><sup><span class="i">−iϕ</span></sup> resolves
0 into components along the body–fixed axes <span class="i">x, y</span>.
It is also noted (see
<a href="#e9780486140520_c07.html#int_107" class="ref_int">Fig.
7.4-2</a>) that the angle <span class="i">β</span> is a vector along
axis <span class="i">x</span> so that the components of
<span class="i">θ</span> and <span class="i">β</span> along the
<span class="i">x</span> and <span class="i">y</span> axes are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1113.jpg](images/e9780486140520_i1113.jpg)

</div>

<div class="caption">

(7.4–12)

</div>

</div>

To reference
<span class="i">θ</span><sub><span class="i">xy</span></sub>
<span class="i">+ β</span> to the principal axes 1, 2, we multiply by
<span class="i">e</span><sup><span class="i">−iφ</span></sup> and
designate it as <span class="i">θ</span><sub>12</sub> :

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1114.jpg](images/e9780486140520_i1114.jpg)

</div>

<div class="caption">

(7.4–13)

</div>

</div>

Multiplying Eq. 7.4–13 by
<span class="i">e</span><sup><span class="i">iφ</span></sup>, we obtain
its inverse

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1115.jpg](images/e9780486140520_i1115.jpg)

</div>

<div class="caption">

(7.4–14)

</div>

</div>

Substituting for <span class="i">θ</span><sub>12</sub> from Eq. 7.4–9,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1116.jpg](images/e9780486140520_i1116.jpg)

</div>

<div class="caption">

(7.4–15)

</div>

</div>

However, from Eq. 7.4–13,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1117.jpg](images/e9780486140520_i1117.jpg)

</div>

<div class="caption">

(7.4–16)

</div>

</div>

so by substituting from Eqs. 7.4–10 and 7.4–16 into Eq. 7.4–15,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1118.jpg](images/e9780486140520_i1118.jpg)

</div>

<div class="caption">

(7.4–17)

</div>

</div>

Equation 7.4–17 expresses the angle <span class="i">θ</span> between the
missile spin axis and the inertial <span class="i">Z</span> axis as a
vector in the transverse plane with components along the rotating
<span class="i">x</span> and <span class="i">y</span> axes, with
<span class="i">x</span> real and <span class="i">y</span> imaginary. To
examine this vector in the transverse inertial plane XY, we multiply
<span class="i">θ</span><sub><span class="i">xy</span></sub> by
<span class="i">e</span><sup><span class="i">int</span></sup> to obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1119.jpg](images/e9780486140520_i1119.jpg)

</div>

<div class="caption">

(7.4–18)

</div>

</div>

Comparing Eq. 7.4–18 with Eq. 7.3<span class="i">e</span>, we find that
the vector <span class="i">θ</span> in the inertial plane has an added
term due to <span class="i">β</span>. In addition to the precession
speed <span class="i">(n + λ)</span>, the effect of the product of
inertia has introduced a component
<span class="i">βe</span><sup><span class="i">int</span></sup> which
rotates at the spin speed <span class="i">n</span>. The result is a
motion of the spin axis indicated by a curve, as shown in
<a href="#e9780486140520_c07.html#int_108"
id="e9780486140520_c07.html_ref_int_108" class="ref_int">Fig. 7.4-3</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1120.jpg](images/e9780486140520_i1120.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_108"
id="e9780486140520_c07.html_int_108" class="label_int"><span
class="b">Fig. 7.4-3</span></a>. Possible motion of spin axis projected
on inertial plane X, <span class="i">Y</span>.

</div>

</div>

<span class="b">PROBLEMS</span>

1.  . Assume that the fuel consumption rate of a given missile with
    <span class="i">A</span> = 10<span class="i">C</span> is small
    enough to justify a constant mass analysis. If the thrust
    misalignment in the body coordinates is a constant and equal to
    <span class="i">Te</span>, where <span class="i">T</span> is the
    thrust parallel to the longitudinal axis, and e is its offset,
    determine the equation for the complex angular velocity
    <span class="i">ω</span><sub>12</sub>.
2.  . When <span class="i">θ</span>, the angle between the principal
    axis 3 and an inertial axis <span class="i">Z</span> is small, it
    can be represented as a vector. Along what axis do we represent this
    vector, and how do we resolve it into components along the rotating
    body axes with spin velocity
    <span class="imageinline">![e9780486140520_i1121.jpg](images/e9780486140520_i1121.jpg)</span>.How
    do we resolve it into components along the inertial
    <span class="i">X Y</span> axes.
3.  . If we assume the velocity vector <span class="b">V</span> of the
    center of mass of a missile to be fixed in space, determine for the
    moment–free missile the angle between <span class="b">V</span> and
    the angular momentum vector <span class="b">h</span>.
4.  . Defining the angle of attack of a missile as the angle between the
    longitudinal axis and the velocity vector <span class="b">V</span>,
    show how this varies for the moment–free missile.
5.  . For a body of revolution <span class="i">(A, A, C)</span>, the
    motion under moment–free conditions is described by a constant
    precession angle <span class="i">θ</span>, the plane containing the
    angular momentum <span class="b">h</span>, the angular velocity ω,
    and the spin axis 3 rotating about the fixed
    <span class="b">h</span> vector at a rate
    <span class="imageinline">![e9780486140520_i1122.jpg](images/e9780486140520_i1122.jpg)</span>.
    Show that the results of Example 7.3–1 are consistent with this
    requirement provided <span class="i">θ</span><sub>12</sub>, the
    angle of attack is small.
6.  . If the missile of Prob. 1 is spinning at a rate <span class="i">n
    = 2π</span> rad/sec, determine the complex angle of attack relative
    to inertial space, and plot the results in the
    <span class="i">XY</span> plane.
7.  . If the geometric axes <span class="i">x, y, z</span> of a near
    symmetric missile deviates from the principal axes 1, 2, 3 by the
    angles <span class="i">β</span> and Φ, where
    <span class="i">β</span> is a small angle between the z axis and the
    principal axis 3, show that the assumption of
    <span class="i">I</span><sub>1</sub> ≅
    <span class="i">I</span><sub>2</sub> results in Φ =
    <span class="i">n</span>. Physically what does this mean?
8.  . Show that in the general case for small <span class="i">β</span>,
    where Φ may not be π, Eq. 7.4–1 can be solved for
    <span class="i">β</span> as
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1123.jpg](images/e9780486140520_i1123.jpg)

    </div>

    </div>
9.  . The principal moment of inertia ratio
    <span class="i">I</span><sub>3</sub>/<span class="i">I</span><sub>1</sub>
    for a near symmetrical satellite is given as 1.20, and the principal
    axis 3 is tilted from the geometric axis z by the angle
    <span class="i">β</span> = 0.05 rad. If the spin rate
    <span class="i">n</span> = 2π rad/sec and
    \[<span class="i">ω</span><sub><span class="i">xy</span></sub>(0)\]/<span class="i">n</span>
    =
    <span class="imageinline">![e9780486140520_i1124.jpg](images/e9780486140520_i1124.jpg)</span>,
    determine the complex angle of attack relative to inertial space and
    show how the geometric axis z is moving in a plane normal to the
    velocity vector.
10. . Using the equation for
    <span class="i">ω</span><sub>12</sub><span class="i">(t)</span> of
    Prob. 6, p. 198, in Eq. 7.3–8 shows that the angle
    <span class="i">θ</span><sub><span class="i">XY</span></sub>
    referred to inertial axes is given by the equation
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1125.jpg](images/e9780486140520_i1125.jpg)

    </div>

    </div>
11. . Body axes <span class="i">x, y</span>, and
    <span class="i">z</span> initially coinciding with the inertial axes
    <span class="i">X, Y,</span> and <span class="i">Z</span> are given
    the following sequence of rotations. Rotation
    <span class="i">θ</span><sub>3</sub> about <span class="i">z</span>
    followed by rotation <span class="i">θ</span><sub>2</sub> about the
    displaced <span class="i">y</span> axis and a rotation
    <span class="i">θ</span><sub><span class="i">1</span></sub> about
    the final position of the <span class="i">x</span> axis. Derive the
    transfer matrix expressing the body axes in terms of the inertial
    axes, and its inverse.
12. . Assume angular velocities
    <span class="imageinline">![e9780486140520_i1126.jpg](images/e9780486140520_i1126.jpg)</span><sub>3</sub>,
    <span class="imageinline">![e9780486140520_i1127.jpg](images/e9780486140520_i1127.jpg)</span>and
    <span class="imageinline">![e9780486140520_i1128.jpg](images/e9780486140520_i1128.jpg)</span>about
    axes <span class="i">z, y</span>, and <span class="i">x</span> in
    the sequence given by Prob. 11, and write the equations for the
    angular velocities
    <span class="i">ω</span><sub>1</sub><span class="i">,
    ω</span><sub>2</sub><span class="i">,</span> and
    <span class="i">ω</span><sub>3</sub> about the final position of the
    body axes <span class="i">x, y, z.</span>
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1129.jpg](images/e9780486140520_i1129.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 12</span>

    </div>

    </div>
13. . Referring to the figure of Prob. 12, assume the missile to be
    symmetric so that
    <span class="i">I</span><sub><span class="i">y</span></sub>
    <span class="i">=
    I</span><sub><span class="i">z</span></sub><span class="i">,</span>
    and determine the equation for the attitude deviation
    <span class="i">θ</span><sub>2</sub> +
    <span class="i">iθ</span><sub>3</sub> of the longitudinal axis due
    to a constant yawing torque
    <span class="i">M</span><sub><span class="i">z</span></sub>.
14. . A space vehicle of moment of inertia
    <span class="i">I</span><sub>1</sub>,
    <span class="i">I</span><sub>2</sub>, and
    <span class="i">I</span><sub>3</sub> is in a circular orbit with
    constant angular velocity <span class="i">ω</span><sub>0</sub> about
    the axis 2 to maintain the direction of axis I always tangent to the
    orbit as shown in the sketch. Assuming small disturbances
    <span class="imageinline">![e9780486140520_i1130.jpg](images/e9780486140520_i1130.jpg)</span>derive
    the differential equation of motion for the torques about the body
    axes 1, 2, and 3.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1131.jpg](images/e9780486140520_i1131.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 14</span>

    </div>

    </div>
15. Assume the body axes 1, 2, and 3 of the space vehicle of Prob. 14 to
    deviate from the orbit axes 1’, 2’ and 3’ by angles
    <span class="i">θ</span><sub>3</sub><span class="i">,
    θ</span><sub>2</sub>, and <span class="i">θ</span><sub>1</sub> in
    the sequence specified in Prob. 11. Using the procedure of Sec. 4.18
    and a spherical earth, show that the gravity force on the space
    vehicle results in torques about the body axes equal to
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1132.jpg](images/e9780486140520_i1132.jpg)

    </div>

    </div>

    where <span class="i">K =
    Gm</span><sub><span class="i">e</span></sub> and
    <span class="i">R</span><sub><span class="i">0</span></sub> is
    distance from the center of earth to the vehicle center of mass.

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title99"></span>

# <span class="b">7.5 Despinning of Satellites</span>

In the design of satellites it is often necessary to provide means for
reducing the spin of a spin–stabilized satellite while in orbit to allow
proper functioning of instruments.
<a href="#e9780486140520_c07.html#int_109"
id="e9780486140520_c07.html_ref_int_109" class="ref_int">Figure
7.5-1</a> <sup><a href="#e9780486140520_ftn01.html#ftn_fn6"
id="e9780486140520_c07.html_ref_ftn_fn6">f</a></sup> shows a simple
device,<sup>7</sup> used in the Pioneer III lunar probe, which is
capable of reducing the spin to zero. It consists of a small mass
<span class="i">m</span> on the end of a light cord wrapped around the
symmetrical spinning body. With the satellite spinning with speed
<span class="i">ω</span><sub>0</sub> about its axis of symmetry, the
mass <span class="i">m</span> is released. The cord will now unwind and
the angular speed of the satellite will gradually decrease.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1133.jpg](images/e9780486140520_i1133.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_109"
id="e9780486140520_c07.html_int_109" class="label_int"><span
class="b">Fig. 7.5-1</span></a>. Despinning device for a satellite.

</div>

</div>

When the cord is completely unwound, it is released and allowed to fly
away. By choosing the length of the cord properly, the spin of the
satellite can be reduced to any value less than the initial value.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1134.jpg](images/e9780486140520_i1134.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_110"
id="e9780486140520_c07.html_int_110" class="label_int"><span
class="b">Fig. 7.5-2</span></a>. Unwinding of mass
<span class="i">m</span>.

</div>

</div>

The device may be analyzed as follows. Since <span class="i">m</span> is
small, the body may be assumed to spin about the geometric axis of
symmetry of the body 0, with moment of inertia <span class="i">I</span>
and angular velocity <span class="i">ω.</span> We attach the X,
<span class="i">Y</span> coordinate axes to the body and allow a second
set of axes <span class="i">x, y</span> to rotate relative to the body
so that the <span class="i">y</span> axis always passes through the
tangent point of the cord, as shown in
<a href="#e9780486140520_c07.html#int_110"
id="e9780486140520_c07.html_ref_int_110" class="ref_int">Fig. 7.5-2</a>.

We will assume that initially <span class="i">m</span> was in contact
with the cylinder at the <span class="i">X</span> axis, in which case
the length of cord extending beyond the tangent point is equal to the
arc length <span class="i">Rφ.</span> The position of
<span class="i">m</span> is then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1135.jpg](images/e9780486140520_i1135.jpg)

</div>

<div class="caption">

(7.5–1)

</div>

</div>

Since the axes <span class="i">x, y</span> are rotating with speed
<span class="imageinline">![e9780486140520_i1136.jpg](images/e9780486140520_i1136.jpg)</span>,
the velocity of <span class="i">m</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1137.jpg](images/e9780486140520_i1137.jpg)

</div>

<div class="caption">

(7.5–2)

</div>

</div>

The angular momentum of the mass <span class="i">m</span> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1138.jpg](images/e9780486140520_i1138.jpg)

</div>

<div class="caption">

(7.5–3)

</div>

</div>

and the total angular momentum is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1139.jpg](images/e9780486140520_i1139.jpg)

</div>

<div class="caption">

(7.5–4)

</div>

</div>

The system kinetic energy <span class="i">T</span> is the sum of the
kinetic energy of the satellite and <span class="i">m</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1140.jpg](images/e9780486140520_i1140.jpg)

</div>

<div class="caption">

(7.5–5)

</div>

</div>

Since the system has no external forces and no dissipation of energy,
the kinetic energy and angular momentum must remain constant and equal
to their initial values. Letting the spin rate at
<span class="i">t</span> = 0 be <span class="i">ω</span><sub>0</sub>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1141.jpg](images/e9780486140520_i1141.jpg)

</div>

<div class="caption">

(7.5–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1142.jpg](images/e9780486140520_i1142.jpg)

</div>

<div class="caption">

(7.5–7)

</div>

</div>

Dividing through by <span class="i">mR</span><sup>2</sup> the two
equations become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1143.jpg](images/e9780486140520_i1143.jpg)

</div>

<div class="caption">

(7.5–8)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1144.jpg](images/e9780486140520_i1144.jpg)

</div>

<div class="caption">

(7.5–9)

</div>

</div>

where

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1145.jpg](images/e9780486140520_i1145.jpg)

</div>

<div class="caption">

(7.5–10)

</div>

</div>

Dividing the first equation by the second, we find,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1146.jpg](images/e9780486140520_i1146.jpg)

</div>

</div>

Therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1147.jpg](images/e9780486140520_i1147.jpg)

</div>

<div class="caption">

(7.5–11)

</div>

</div>

which tells us that the mass m unwinds at a constant rate. Substituting
for <span class="i">φ</span> and <span class="i">φ</span> in Eq. 7.5–9,
the spin rate at any time becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1148.jpg](images/e9780486140520_i1148.jpg)

</div>

<div class="caption">

(7.5–12)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1149.jpg](images/e9780486140520_i1149.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_111"
id="e9780486140520_c07.html_int_111" class="label_int"><span
class="b">Fig. 7.5-3</span></a>. Despinning of satellites.

</div>

</div>

The spin may be reduced to any desired value
<span class="i">ω</span><sub><span class="i">ƒ</span></sub> by choosing
the proper length of cord, and releasing it when completely unwound. If
<span class="i">l</span><sub><span class="i">ƒ</span></sub> is the
length selected, the terminal value of <span class="i">φ</span> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1150.jpg](images/e9780486140520_i1150.jpg)

</div>

<div class="caption">

(7.5–13)

</div>

</div>

and from Eq. 7.5–12,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1151.jpg](images/e9780486140520_i1151.jpg)

</div>

<div class="caption">

(7.5–14)

</div>

</div>

Solving for
<span class="i">l</span><sub><span class="i">f</span></sub><span class="i">,</span>
the required length of cord is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1152.jpg](images/e9780486140520_i1152.jpg)

</div>

<div class="caption">

(7.5–15)

</div>

</div>

If the terminal angular velocity is to be zero,
<span class="i">l</span><sub><span class="i">f</span></sub> becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1153.jpg](images/e9780486140520_i1153.jpg)

</div>

<div class="caption">

(7.5–16)

</div>

</div>

For symmetry, two cords with masses <span class="i">½m</span> can be
used as shown in <a href="#e9780486140520_c07.html#int_111"
id="e9780486140520_c07.html_ref_int_111" class="ref_int">Fig. 7.5-3</a>,
the result being the same as that for one mass of value
<span class="i">m</span>.

<span class="b">Example 7.5–1</span>

The Pioneer III lunar probe was launched with an initial spin rate of
400 rpm. It was desired to reduce this to 5.5 rpm by using a yo–yo with
two weights of 0.2 oz each.

For Pioneer III

<div class="blocktext">

<span class="i">gl</span> = 92 lb in.<sup>2</sup>

<span class="i">R =</span> 5 in.

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1154.jpg](images/e9780486140520_i1154.jpg)

</div>

</div>

From Eq. 7.5–15 the proper length of cord is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1155.jpg](images/e9780486140520_i1155.jpg)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title100"></span>

# <span class="b">7.6 Attitude Drift of Space Vehicles</span><sup><span class="b">8</span></sup>

The attitude of a body of revolution spinning in the absence of external
forces is not a constant when energy dissipation takes place. Elastic
vibrations, induced by gyroscopic action, result in a dissipation of
energy and a change in the precession cone angle
<span class="i">θ</span>. In this section we examine the effect of
energy dissipation on the spinning body and evaluate the time required
for a body of given configuration to undergo a specified change in
attitude.<sup>8</sup>

The moment–free motion of an unsymmetric body with principal moments of
inertia <span class="i">A, B, C</span> is an unsteady periodic
precession and nutation about the resultant angular momentum vector
<span class="b">h</span> fixed in space. Steady rotation is possible
only about the principal axis of maximum or minimum moment of inertia,
the principal axis of intermediate moment of inertia being unstable.

For a body of revolution <span class="i">A, A, C</span>, the moment–free
motion is a steady precession of the spin axis at a constant angle
<span class="i">θ</span> about the resultant angular momentum vector
<span class="b">h</span> fixed in space. Steady rotation is again
possible about the axis of maximum or minimum moment of inertia, and the
axis of intermediate moment of inertia does not exist.

In either case, the axis of maximum or minimum moment of inertia is
considered to be stable in that, if the spin axis deviates slightly from
the resultant angular momentum vector, there is no tendency for this
deviation to grow. This statement is true only for a perfectly rigid
body in the absence of external moment.

In an elastic body, deformation between particles will always take
place, resulting in some dissipation of energy. When the dissipation of
energy is taken into account, we must revise our statement of stability
in that it is possible for a small deviation of the spin axis to grow
into a large one and, eventually, to result in a complete change in
attitude of the body. For such bodies, only the principal axis of
maximum moment of inertia is stable, and the axis of minimum moment of
inertia is one of unstable equilibrium.

These facts were actually observed in the Explorer I
satellite,<sup>6</sup> which was spin–stabilized about the longitudinal
axis of minimum moment of inertia. The flexible antennas of the
satellite provided an excellent source for energy dissipation, and in
one revolution around its orbit (approximately 90 min) the Explorer I
was observed to be tumbling at an attitude of <span class="i">θ</span> =
60° instead of spinning about its longitudinal axis at
<span class="i">θ</span> = 0. The remedy for this behavior is obviously
to shorten the longitudinal dimensions of the satellite so that the
moment of inertia about the longitudinal spin axis is greater than that
about the transverse pitch or yaw axis. However, the problem still
exists for missiles which are long, slender bodies and inherently
unstable about the spin axis. Here the important question is how long
can the spinning missile coast in a moment–free condition without an
appreciable change in its attitude.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1156.jpg](images/e9780486140520_i1156.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_112"
id="e9780486140520_c07.html_int_112" class="label_int"><span
class="b">Fig. 7.6-1</span></a><span class="b">.</span> Coordinate
system of body axes 1, 2, 3.

</div>

</div>

  
  

<span class="i">Energy considerations of stability</span>

We will now examine the basis for stability from an energy point of
view. For a body of revolution with principal moments of inertia
<span class="i">A, A, C,</span> as shown in
<a href="#e9780486140520_c07.html#int_112"
id="e9780486140520_c07.html_ref_int_112" class="ref_int">Fig. 7.6-1</a>,
the moment–free motion is that of steady precession described by the
equations

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1157.jpg](images/e9780486140520_i1157.jpg)

</div>

<div class="caption">

(7.6–1)

</div>

</div>

Since the moment is zero, the angular momentum vector h is a constant
and we can write for the square of its magnitude the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1158.jpg](images/e9780486140520_i1158.jpg)

</div>

<div class="caption">

(7.6–2)

</div>

</div>

We next examine the kinetic energy of rotation, T, which is given by the
equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1159.jpg](images/e9780486140520_i1159.jpg)

</div>

<div class="caption">

(7.6–3)

</div>

</div>

Multiplying Eq. 7.6–3 by <span class="i">A</span> and subtracting from
Eq. 7.6–2,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1160.jpg](images/e9780486140520_i1160.jpg)

</div>

<div class="caption">

(7.6–4)

</div>

</div>

and since <span class="i">Cω</span><sub>3</sub> =
<span class="i">h</span> cos <span class="i">θ</span>, we obtain the
relationship for cos θ in terms of <span class="i">h</span> and
<span class="i">T</span> as follows

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1161.jpg](images/e9780486140520_i1161.jpg)

</div>

<div class="caption">

(7.6–5)

</div>

</div>

Equation 7.6–5 indicates that <span class="i">θ</span> remains constant
provided <span class="i">T</span> and <span class="i">h</span> are
constant. However energy dissipation under zero external moment is
possible, in which case <span class="i">T</span> must decrease while
<span class="i">h</span> remains constant. Differentiating Eq. 7.6–5, we
obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1162.jpg](images/e9780486140520_i1162.jpg)

</div>

<div class="caption">

(7.6–6)

</div>

</div>

and with <span class="i">Ṫ</span> a negative quantity,
<span class="imageinline">![e9780486140520_i1163.jpg](images/e9780486140520_i1163.jpg)</span>
is negative for <span class="i">C/A</span> \> 1 and positive for
<span class="i">C/A</span> \< 1. Thus the principal axis of minimum
moment of inertia is one of unstable equilibrium, and a small deviation
of the spin axis will increase due to energy dissipation when
<span class="i">C/A</span> \< 1.

  
  
  

<span class="i">Dissipation of energy</span>

  
  

Assuming an elastic body, the energy dissipated per unit volume per
cycle of stress can be assumed to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1164.jpg](images/e9780486140520_i1164.jpg)

</div>

<div class="caption">

(7.6–7)

</div>

</div>

where <span class="i">γ</span> is a hysteretic damping factor
establishing the fraction of the elastic energy which is dissipated as
shown by the shaded area in <a href="#e9780486140520_c07.html#int_113"
id="e9780486140520_c07.html_ref_int_113" class="ref_int">Fig. 7.6-2</a>.
Dividing by the time <span class="i">t</span><sub>0</sub> per cycle of
stress, and integrating over the entire structure, the rate of energy
dissipation can be found. Thus the equation to be solved is of the
general form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1165.jpg](images/e9780486140520_i1165.jpg)

</div>

<div class="caption">

(7.6–8)

</div>

</div>

In examining the source of cyclic stressing, free vibrations can be
discarded since they will soon damp out. Steady cycling of stress is
however induced by the gyroscopic precession, and these stresses are
repeated at the rate
<span class="imageinline">![e9780486140520_i1166.jpg](images/e9780486140520_i1166.jpg)</span>
and
<span class="imageinline">![e9780486140520_i1167.jpg](images/e9780486140520_i1167.jpg)</span>as
we will presently show.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1168.jpg](images/e9780486140520_i1168.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_113"
id="e9780486140520_c07.html_int_113" class="label_int"><span
class="b">Fig. 7.6-2</span></a>. Energy dissipated by hysteresis
damping.

</div>

</div>

The excitation for the cyclic stress is the acceleration. Choosing an
arbitrary point on the structure and orienting the plane 1, 0, 3 through
it, the position vector for the specified point is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1169.jpg](images/e9780486140520_i1169.jpg)

</div>

<div class="caption">

(7.6–9)

</div>

</div>

With
<span class="imageinline">![e9780486140520_i1170.jpg](images/e9780486140520_i1170.jpg)</span>
small, the angular velocity and acceleration of the coordinate axes 1,
2, 3 are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1171.jpg](images/e9780486140520_i1171.jpg)

</div>

<div class="caption">

(7.6–10)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1172.jpg](images/e9780486140520_i1172.jpg)

</div>

<div class="caption">

(7.6–11)

</div>

</div>

Substituting into the general vector equation for the acceleration

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1173.jpg](images/e9780486140520_i1173.jpg)

</div>

<div class="caption">

(7.6–12)

</div>

</div>

and noting that the following quantities are zero

<div class="blocktext">

<span class="b">a</span><sub>0</sub> = \[<span class="b">a</span>\] =
\[<span class="b">v</span>\] = 0

</div>

the result after some algebraic reduction is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1174.jpg](images/e9780486140520_i1174.jpg)

</div>

<div class="caption">

(7.6–13)

</div>

</div>

A somewhat more convenient form of Eq. 7.6–13 results by eliminating
<span class="imageinline">![e9780486140520_i1175.jpg](images/e9780486140520_i1175.jpg)</span>
and
<span class="imageinline">![e9780486140520_i1176.jpg](images/e9780486140520_i1176.jpg)</span>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1177.jpg](images/e9780486140520_i1177.jpg)

</div>

<div class="caption">

(7.6–14)

</div>

</div>

Since the only time–varying quantity in Eq. 7.6–14 (assuming
<span class="imageinline">![e9780486140520_i1178.jpg](images/e9780486140520_i1178.jpg)</span>to
be negligible) is <span class="i">ϕ</span> =
<span class="imageinline">![e9780486140520_i1179.jpg](images/e9780486140520_i1179.jpg)</span>it
is evident that the cyclic stress is repeated at a rate
<span class="imageinline">![e9780486140520_i1180.jpg](images/e9780486140520_i1180.jpg)</span>and
<span class="imageinline">![e9780486140520_i1181.jpg](images/e9780486140520_i1181.jpg)</span>
It should be pointed out that, for slender bodies like missiles,
<span class="i">C/A</span> is small compared to unity, and the
predominant variable acceleration term is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1182.jpg](images/e9780486140520_i1182.jpg)

</div>

<div class="caption">

(7.6–14a)

</div>

</div>

which is repeated in the time

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1183.jpg](images/e9780486140520_i1183.jpg)

</div>

<div class="caption">

(7.6–15)

</div>

</div>

<span class="b">Example 7.6–1</span>

As an example of the simplest kind, we will consider two solid disks
connected by a flexible tube, as shown in
<a href="#e9780486140520_c07.html#int_114"
id="e9780486140520_c07.html_ref_int_114" class="ref_int">Fig. 7.6-3</a>.
We will let <span class="i">C</span><sub>1</sub> and
<span class="i">A</span><sub>1</sub> be the moments of inertia of each
disk about its own polar and diametric axes. The gyroscopic moment
required by each disk is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1184.jpg](images/e9780486140520_i1184.jpg)

</div>

<div class="caption">

<span class="i">(a)</span>

</div>

</div>

Since the moments of inertia about the center of mass of the body are

<div class="blocktext">

<span class="i">C = 2C</span><sub>1</sub>  
<span class="i">A ≅ 2(A</span><sub>1</sub> <span class="i">+
m</span><sub>1</sub><span class="i">l</span><sup><span class="i">2</span></sup><span class="i">)</span>

</div>

Equation a can be rewritten as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1185.jpg](images/e9780486140520_i1185.jpg)

</div>

</div>

The first term, however, is the moment about the center of mass which is
zero and from which Eq. 7.6–1 is obtained. We are thus left with

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1186.jpg](images/e9780486140520_i1186.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

where <span class="i">F</span> =
<span class="imageinline">![e9780486140520_i1187.jpg](images/e9780486140520_i1187.jpg)</span>
sin <span class="i">θ</span> is the centripital force of the precessing
disk.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1188.jpg](images/e9780486140520_i1188.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_114"
id="e9780486140520_c07.html_int_114" class="label_int"><span
class="b">Fig. 7.6-3</span></a><span class="b">.</span> Satellite
configuration, displacement, and moment distribution.

</div>

</div>

The effect of
<span class="i">M</span><sub><span class="i">g</span></sub> and
<span class="i">F</span> on the flexible tube is shown in
<a href="#e9780486140520_c07.html#int_114" class="ref_int">Fig.
7.6-3</a>. At point <span class="i">z</span> along the tube, measured
from the center of mass, the bending moment is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1189.jpg](images/e9780486140520_i1189.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

and the expression for the maximum stress becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1190.jpg](images/e9780486140520_i1190.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

which is repeated at the rate given by Eq. 7.6–15. The rate of energy
dissipation as given by the left side of Eq. 7.6–8 is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1191.jpg](images/e9780486140520_i1191.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

and the rate of change of the attitude angle <span class="i">θ</span>
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1192.jpg](images/e9780486140520_i1192.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

A plot of Eq. <span class="i">f</span> is shown in
<a href="#e9780486140520_c07.html#int_115"
id="e9780486140520_c07.html_ref_int_115" class="ref_int">Fig. 7.6-4</a>.
Since <span class="i">6</span> is zero for <span class="i">θ</span> = 0,
tumbling cannot be initiated unless the initial value of
<span class="i">θ</span> is finite. However θ = 0 is never attainable in
practice for many reasons, and θ will build up when
<span class="i">C/A</span> is less than unity. By differentiating Eq.
<span class="i">f, θ</span> can be shown to have a maximum at
<span class="i">θ</span> = tan<sup>−1</sup> 1/√2 = 35° 20’. Due to
cos<sup>2</sup> <span class="i">θ</span>, <span class="i">θ</span> will
diminish to a small value near <span class="i">θ</span> = 90°, and an
infinite time will be required to reach this angle.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1193.jpg](images/e9780486140520_i1193.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_115"
id="e9780486140520_c07.html_int_115" class="label_int"><span
class="b">Fig. 7.6-4</span></a><span class="b">.</span> Variation in the
rate of tumbling.

</div>

</div>

For small values of <span class="i">θ</span>, Eq.
<span class="i">f</span> is approximately equal to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1194.jpg](images/e9780486140520_i1194.jpg)

</div>

<div class="caption">

(<span class="i">g</span>)

</div>

</div>

and the time required for the attitude angle to change from
<span class="i">θ</span><sub>0</sub> to
<span class="i">θ</span><sub>1</sub> is &

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1195.jpg](images/e9780486140520_i1195.jpg)

</div>

<div class="caption">

(<span class="i">h</span>)

</div>

</div>

<span class="i">Numerical example</span>

Let the two solid disks be aluminum, ½in. thick and 24 in. diameter, and
the flexible tube be 0.032 in. stainless steel, 6 in. in diameter and 24
in. long. The quantities required for the computation of
<span class="i">K</span> are:

<div class="blocktext">

<span class="i">C</span> = 8.16 Ib–in.–sec<sup>2</sup>  
<span class="i">A</span> = 20.44 lb–in.–sec<sup>2</sup>  
<span class="i">m</span> = 0.1136 Ib–in.<sup>−1</sup>–sec<sup>2</sup>  
<span class="i">V</span> = 14.5 in.<sup>3</sup> = volume of flexed
tube  
<span class="i">ξ</span> = 3.0 in.  
<span class="i">I</span> = 2.71 in.4  
<span class="i">l</span> = 12.0 in.  
<span class="i">E</span> = 29 x 10<sup>6</sup> lb–in.<sup>−2</sup>

</div>

Assuming <span class="i">y</span> = 0.05 and
<span class="i">ω</span><sub>0</sub> = 50<span class="i">π</span>/sec,
the value of <span class="i">K</span> is 662 × 10<sup>6</sup>. Thus for
the body to undergo an attitude change from 1° to 10°, the time
required, as calculated from Eq. <span class="i">h</span>, is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1196.jpg](images/e9780486140520_i1196.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A satellite has a moment of inertia of <span class="i">I</span> =
    1.20 lb–in.–sec<sup>2</sup> about its spin axis. It is desired to
    reduce the initial spin of 200 rpm to zero by two weights of
    <span class="imageinline">![e9780486140520_i1197.jpg](images/e9780486140520_i1197.jpg)</span>
    each wrapped around a section having a radius of 10 in. Determine
    the proper length of cord.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1198.jpg](images/e9780486140520_i1198.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 2</span>

    </div>

    </div>

2.  In Prob. 1, determine the speed of the
    <span class="imageinline">![e9780486140520_i1199.jpg](images/e9780486140520_i1199.jpg)</span>
    weights as they fly off. As shown in the sketch, the pin holding the
    string will slide out when the string goes beyond the tangent to the
    circle.

3.  It is proposed to despin a satellite by four weights of mass
    <span class="i">m</span> each, hinged by stiff arms as shown in the
    sketch. Show that the spin is given by
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1200.jpg](images/e9780486140520_i1200.jpg)

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1201.jpg](images/e9780486140520_i1201.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 3</span>

    </div>

    </div>

4.  Determine the <span class="b">i, j, k</span> components of the
    acceleration of <span class="i">m</span> in Prob. 3.

5.  Verify the relations given by Eq. 7.6–8.

6.  Verify Eq. 7.6—14.

7.  Equation 7.6–5 can be written as

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1202.jpg](images/e9780486140520_i1202.jpg)

    </div>

    </div>

    Plot <span class="i">T</span> versus <span class="i">θ</span> for
    <span class="imageinline">![e9780486140520_i1203.jpg](images/e9780486140520_i1203.jpg)</span>
    when (a) <span class="i">C/A</span> \> 1; (b)
    <span class="i">C/A</span> \< 1, and discuss its stability.

8.  For a symmetric body <span class="i">A, A, C</span> acted upon by
    moments <span class="i">M</span><sub>1</sub>,
    <span class="i">M</span><sub>2</sub><span class="i">,
    M</span><sub>3</sub> about body axes 1, 2, 3, show that the
    dissipation rate of energy is equal to
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1204.jpg](images/e9780486140520_i1204.jpg)

    </div>

    </div>

9.  Show that the hysteretic damping factor <span class="i">γ</span> of
    Eq. 7.6–7 is related to the structural damping factor α by the
    relationship <span class="i">α</span> =
    <span class="i">y</span>/2<span class="i">π</span>.

    <span class="i">Hint:</span> The work done per cycle by a damping
    force <span class="i">F</span><sub><span class="i">d</span></sub>
    for harmonic oscillations is <span class="i">W =
    πF</span><sub><span class="i">d</span></sub><span class="i">X,</span>
    where <span class="i">X</span> is the amplitude leading the damping
    force by 90°. The structural damping force can be taken as
    <span class="i">iαkx,</span> where <span class="i">k</span> is the
    stiffness.

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title101"></span>

# <span class="b">7.7 Variable Mass</span>

In the previous sections we have limited our discussion to a
constant–mass system. In many cases the mass variation rate is large,
which requires us to consider the problem of variable mass.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1205.jpg](images/e9780486140520_i1205.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_116"
id="e9780486140520_c07.html_int_116" class="label_int"><span
class="b">Fig. 7.7-1</span></a><span class="b">.</span> Momentum of the
system at times <span class="i">t</span> and <span class="i">t</span> +
Δ<span class="i">t</span>.

</div>

</div>

Newton’s second law, <span class="b">F</span> =
ṗ<span class="b">,</span> which states that force is equal to the time
rate of change of momentum, is intended to apply only to a system of
definite mass. However, the equation can be applied to a system of
varying mass provided the same mass is examined for the change in
momentum at two instances of time.

We will consider a mass <span class="i">m</span> moving with velocity v
at time <span class="i">t</span>, and assume that our system is
accumulating mass continually at a rate ṁ (if the system is losing mass
as in a rocket, ṁ is negative). We will define our system to be the mass
<span class="i">m</span> + <span class="i">Δm</span> at time
<span class="i">t</span> as shown in
<a href="#e9780486140520_c07.html#int_116"
id="e9780486140520_c07.html_ref_int_116" class="ref_int">Fig. 7.7-1</a>.
Its initial momentum at time <span class="i">t</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1206.jpg](images/e9780486140520_i1206.jpg)

</div>

<div class="caption">

(7.7-1)

</div>

</div>

where <span class="b">v</span><sub>0</sub> is the initial velocity of
<span class="i">Δm</span> before it is acquired by
<span class="i">m.</span> The momentum at time t
<span class="i">+</span> Δ<span class="i">t</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1207.jpg](images/e9780486140520_i1207.jpg)

</div>

<div class="caption">

(7.7–2)

</div>

</div>

where the negligible second–order term
(Δ<span class="i">m</span>)(Δ<span class="i">v</span>) has been omitted.
Subtracting to determine the change in momentum and dividing by
Δ<span class="i">t</span>, the equation for the variable mass system
becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1208.jpg](images/e9780486140520_i1208.jpg)

</div>

<div class="caption">

(7.7–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1209.jpg](images/e9780486140520_i1209.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_117"
id="e9780486140520_c07.html_int_117" class="label_int"><span
class="b">Fig. 7.7-2</span></a><span class="b">.</span> Forces on a
rocket.

</div>

</div>

Equation 7.7–3 indicates that the force <span class="b">F</span> is
expended in accelerating the mass <span class="i">m</span> and changing
the momentum of the acquired mass from
<span class="b">v</span><sub>0</sub> <span class="i">dm</span> to
<span class="i">v dm.</span> dm

For rockets
<span class="imageinline">![e9780486140520_i1210.jpg](images/e9780486140520_i1210.jpg)</span>is
the thrust exerted by the jet, where <span class="b">u</span> =
−(<span class="b">v</span> − <span class="b">v</span><sub>0</sub>) is
the velocity of the gas jet relative to the
engine.<sup><a href="#e9780486140520_ftn01.html#ftn_fn7"
id="e9780486140520_c07.html_ref_ftn_fn7">g</a></sup> Thus the equation
for the rocket in rectilinear motion,
<a href="#e9780486140520_c07.html#int_117"
id="e9780486140520_c07.html_ref_int_117" class="ref_int">Fig. 7.7-2</a>,
can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1211.jpg](images/e9780486140520_i1211.jpg)

</div>

<div class="caption">

(7.7–4)

</div>

</div>

where the external forces of gravity and aerodynamic drag can be
included in <span class="b">F</span>. If the rocket is not spinning or
turning and <span class="b">T</span> acts through the center of mass,
the moment on the rocket is zero, and we are concerned only with its
translational motion.

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title102"></span>

# <span class="b">7.8 Jet Damping (Nonspinning Variable Mass Rocket)</span>

When a nonspinning rocket rotates about a transverse axis, as shown in
<a href="#e9780486140520_c07.html#int_118"
id="e9780486140520_c07.html_ref_int_118" class="ref_int">Fig. 7.8-1</a>,
the ejected gas acquires a momentum component–ṁlω perpendicular to the
longitudinal axis, where <span class="i">m</span> is the mass of the
rocket at any time, ṁ = <span class="i">dm/dt</span> is its rate of
change ṁ is negative), and <span class="i">lω</span> is the transverse
velocity of the nozzle exit due to rotational velocity ω. Letting the
transverse rotational axis coincide at all times with the center of mass
and letting the moment of inertia of the rocket about this axis be
<span class="i">I</span> =
<span class="i">mk</span><sup>2</sup><span class="i">,</span> where
<span class="i">k</span> is the radius of gyration about the transverse
axis, the moment <span class="i">M</span> about this axis must supply
the change in angular momentum of the rocket and the ejected mass as
follows;

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1212.jpg](images/e9780486140520_i1212.jpg)

</div>

<div class="caption">

(7.8–1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1213.jpg](images/e9780486140520_i1213.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_118"
id="e9780486140520_c07.html_int_118" class="label_int"><span
class="b">Fig. 7.8-1</span></a><span class="b">.</span> Jet damping of
nonspinning rocket.

</div>

</div>

Substituting for <span class="i">I</span> and carrying out the
differentiation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1214.jpg](images/e9780486140520_i1214.jpg)

</div>

<div class="caption">

(7.8–2)

</div>

</div>

Assuming the applied moment <span class="i">M</span> to be zero and
<span class="imageinline">![e9780486140520_i1215.jpg](images/e9780486140520_i1215.jpg)</span>
to be negligible (i.e., burning proceeds radially), this equation can be
solved in the following manner:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1216.jpg](images/e9780486140520_i1216.jpg)

</div>

<div class="caption">

(7.8–3)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1217.jpg](images/e9780486140520_i1217.jpg)

</div>

<div class="caption">

(7.8—4)

</div>

</div>

Thus with an initial angular rate of
<span class="i">ω</span><sub>0</sub>, the angular speed
<span class="i">ω</span> decreases if l/<span class="i">k</span> is
greater than unity and increases if
<span class="i">l</span>/<span class="i">k</span> is less than unity.
Since in most configurations <span class="i">l/k</span> \> 1, the
angular speed decreases and the action of the jet is that of a damper.
<a href="#e9780486140520_c07.html#int_119"
id="e9780486140520_c07.html_ref_int_119" class="ref_int">Figure
7.8-2</a> shows how the angular speed changes with mass ratio for
various values of <span class="i">l/k.</span>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1218.jpg](images/e9780486140520_i1218.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_119"
id="e9780486140520_c07.html_int_119" class="label_int"><span
class="b">Fig. 7.8-2</span></a><span class="b">.</span> Change in pitch
angular rate of nonspinning rocket due to jet damping.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title103"></span>

# <span class="b">7.9 Euler’s Dynamical Equations for Spinning Rockets</span><sup><span class="b">2</span></sup>

The statement that the force is equal to the time rate of change of
momentum can be applied to problems of varying mass provided the
momentum of a definite mass is examined for its rate of change. The
result is the rate of change of the momentum of the varying mass plus
the rate of momentum transfer from the varying mass. The moment of the
force about its center of mass is then the time rate of change of the
moment of momentum which, can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1219.jpg](images/e9780486140520_i1219.jpg)

</div>

<div class="caption">

(7.9—1)

</div>

</div>

Consider a general motion of a symmetric rocket with body axes
<span class="i">x, y, z</span> fixed in the rocket with the origin at
the center of mass. The jet is considered to be ejected through a
cluster of nozzles, the center of each being defined by the vector
<span class="b">r</span><sub><span class="i">i</span></sub> =
<span class="i">x</span><sub><span class="i">i</span></sub><span class="b">i</span> +
<span class="i">y</span><sub><span class="i">i</span></sub><span class="b">j</span>–<span class="i">l</span><span class="b">k</span>,
as shown in <a href="#e9780486140520_c07.html#int_120"
id="e9780486140520_c07.html_ref_int_120" class="ref_int">Fig. 7.9-2</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1220.jpg](images/e9780486140520_i1220.jpg)

</div>

<div class="caption">

<span class="b">Fig. 7.9-1</span><span class="b">.</span> Jet damping of
spinning rocket.

</div>

</div>

With the <span class="i">x, y, z</span> axes coinciding with the
principal axes of the rocket, the angular momentum components are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1221.jpg](images/e9780486140520_i1221.jpg)

</div>

<div class="caption">

(7.9–2)

</div>

</div>

where <span class="i">I</span><sub><span class="i">x</span></sub>
<span class="i">I</span><sub><span class="i">y</span></sub><span class="i">,</span>
and <span class="i">I</span><sub><span class="i">z</span></sub> are
instantaneous values of the principal moments of inertia. The rate of
change of the angular momentum of the rocket is

<div class="blocktext">

<span class="b">\[h\]</span> + <span class="b">ω × h</span>

</div>

which results in the components

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1222.jpg](images/e9780486140520_i1222.jpg)

</div>

<div class="caption">

(7.9–3)

</div>

</div>

In considering the angular momentum imparted to the jet, the cluster of
nozzles is assumed to be symmetrically located relative to the
<span class="i">z</span> axis. If all the angular velocities of the
missile are zero, the angular momentum imparted to the jet is zero. The
velocity of the nozzle exit due to
<span class="i">ω</span><sub><span class="i">x</span></sub><span class="i">,
ω</span><sub><span class="i">y</span></sub><span class="i">,</span> and
<span class="i">ω</span><sub><span class="i">z</span></sub> is shown in
<a href="#e9780486140520_c07.html#int_120" class="ref_int">Fig.
7.9-2</a>. Multiplying these velocities by their mass rate of flow ṁ, we
obtain the linear momentum rates in the direction of the velocities,
from which the angular momentum rates can be determined by multiplying
with proper distances from the coordinate axes.

For the <span class="i">i</span>th nozzle, the linear momentum rate due
to <span class="i">ω</span><sub><span class="i">z</span></sub>
is–ṁ<sub>i</sub>r<sub>i</sub>ω<sub>z</sub>, and its angular momentum
rate about the <span class="i">z</span> axis
is–ṁ<sub>i</sub><span class="i">r</span><sub><span class="i">i</span></sub><sup>2</sup>ωz,
where <span class="i">ṁ</span><sub><span class="i">i</span></sub> =
<span class="i">dm</span><sub><span class="i">i</span></sub><span class="i">/dt</span>
(a negative quantity). Summing over all nozzles, the total rate of
angular momentum transfer to the jet, about the <span class="i">z</span>
axis is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1223.jpg](images/e9780486140520_i1223.jpg)

</div>

</div>

where

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1224.jpg](images/e9780486140520_i1224.jpg)

</div>

<div class="caption">

(7.9–4)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1225.jpg](images/e9780486140520_i1225.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_120"
id="e9780486140520_c07.html_int_120" class="label_int"><span
class="b">Fig. 7.9-2</span></a><span class="b">.</span> Velocity of
nozzle due to pitch and spin.

</div>

</div>

Due to <span class="i">ω</span><sub><span class="i">x</span></sub> the
rate of change of the momentum of the <span class="i">i</span>th jet is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1226.jpg](images/e9780486140520_i1226.jpg)

</div>

</div>

and its moment is
<span class="imageinline">![e9780486140520_i1227.jpg](images/e9780486140520_i1227.jpg)</span> +
Summing over all nozzles, the total rate of change of the angular
momentum of the jet about the <span class="i">x</span> axis is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1228.jpg](images/e9780486140520_i1228.jpg)

</div>

<div class="caption">

(7.9–5)

</div>

</div>

In a similar manner, the rate of change of the angular momentum of the
jet about the <span class="i">y</span> axis is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1229.jpg](images/e9780486140520_i1229.jpg)

</div>

<div class="caption">

(7.9–6)

</div>

</div>

Putting together all these terms, the moment equations become

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1230.jpg](images/e9780486140520_i1230.jpg)

</div>

<div class="caption">

(7.9–7)

</div>

</div>

Substituting <span class="i">I</span><sub>x</sub> =
<span class="imageinline">![e9780486140520_i1231.jpg](images/e9780486140520_i1231.jpg)</span>
, we have
<span class="imageinline">![e9780486140520_i1232.jpg](images/e9780486140520_i1232.jpg)</span>,
and the above equations can be rewritten as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1233.jpg](images/e9780486140520_i1233.jpg)

</div>

<div class="caption">

(7.9–8)

</div>

</div>

We find, therefore, that the usual Euler’s equations are supplemented by
additional terms related to jet damping and the variable moment of
inertia.

  
  

<span class="b">Example 7.9—1</span>

Consider the moment–free motion of a symmetrical missile, I<sub>x</sub>
= I<sub><span class="i">y</span></sub> = I<span class="i">,</span> with
initial spin velocity
<span class="i">ω</span><sub><span class="i">z</span></sub>(0) =
<span class="i">n</span>. We will assume that the fuel burns in such a
manner that the variations in
<span class="i">k</span><sub><span class="i">x</span></sub><span class="i">,
k</span><sub><span class="i">d</span></sub><span class="i">,</span> and
<span class="i">k</span><sub><span class="i">z</span></sub> are
negligible.

From the third of Eq. 7.9–8, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1234.jpg](images/e9780486140520_i1234.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

which leads to the solution,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1235.jpg](images/e9780486140520_i1235.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

We now multiply the second of Eq. 7.9–8 by <span class="i">i</span> =
√–1 and add it to the first equation letting

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1236.jpg](images/e9780486140520_i1236.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

The first two equations of Eq. 7.9–8 then reduce to the following, where
<span class="i">ω</span><sub><span class="i">z</span></sub> from above
has been substituted.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1237.jpg](images/e9780486140520_i1237.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

If we assume <span class="i">m</span> to vary linearly with time so that
<span class="i">m</span> =
<span class="i">m</span><sub><span class="i">o</span></sub>
<span class="i">− m’t</span>, this equation reduces to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1238.jpg](images/e9780486140520_i1238.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

By letting
1–(<span class="i">m′/m</span><sub><span class="i">0</span></sub>)<span class="i">t</span>
= <span class="i">ξ</span> and
\[(<span class="i">p</span><sup>2</sup>/<span class="i">k</span><sub><span class="i">z</span></sub><sup>2</sup>)–1\]
= <span class="i">K,</span> the last integral is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1239.jpg](images/e9780486140520_i1239.jpg)

</div>

</div>

and the solution becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1240.jpg](images/e9780486140520_i1240.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1241.jpg](images/e9780486140520_i1241.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

<a href="#e9780486140520_c07.html#int_121"
id="e9780486140520_c07.html_ref_int_121" class="ref_int">Figure
7.9-3</a> shows how the various terms of Eq. <span class="i">f</span>
vary with time. The oscillatory amplitude of
<span class="i">ω</span><sub><span class="i">xy</span></sub> diminishes
with time due to jet damping, and the frequency of oscillation
increases.<sup>1,3</sup>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1242.jpg](images/e9780486140520_i1242.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_121"
id="e9780486140520_c07.html_int_121" class="label_int"><span
class="b">Fig. 7.9-3</span></a><span class="b">.</span> Terms of Eq.
<span class="i">f</span>.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title104"></span>

# <span class="b">7.10 Angle of Attack of the Missile</span>

The angular velocity
<span class="i">ω</span><sub><span class="i">xy</span></sub> is referred
to coordinates <span class="i">x, y,</span> which are rotating with the
missile. To establish the angle of attack of the missile, it is
necessary to determine the Euler angle <span class="i">θ</span> measured
from a fixed inertial axis. For this determination we start with the
angular velocities
<span class="i">ω</span><sub><span class="i">x</span></sub>,
<span class="i">ω</span><sub><span class="i">y</span></sub>,
<span class="i">ω</span><sub><span class="i">z</span></sub> expressed in
terms of Euler’s angles

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1243.jpg](images/e9780486140520_i1243.jpg)

</div>

<div class="caption">

(7.10—1)

</div>

</div>

Adding the first two in quadrature, we have

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1244.jpg](images/e9780486140520_i1244.jpg)

</div>

<div class="caption">

(7.10–2)

</div>

</div>

From Eq. 7.9–b and the third of the above equations, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1245.jpg](images/e9780486140520_i1245.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1246.jpg](images/e9780486140520_i1246.jpg)

</div>

<div class="caption">

(7.10—3)

</div>

</div>

By substituting into the equation for
<span class="i">ω</span><sub><span class="i">xy</span></sub>, Eq.
7.10–2,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1247.jpg](images/e9780486140520_i1247.jpg)

</div>

<div class="caption">

(7.10—4)

</div>

</div>

We now introduce the transformation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1248.jpg](images/e9780486140520_i1248.jpg)

</div>

<div class="caption">

(7.10–5)

</div>

</div>

proposed by H. Leon,<sup>4</sup> which differentiates into

<div class="blocktext">

<span class="imageinline">![e9780486140520_i1249.jpg](images/e9780486140520_i1249.jpg)</span>

</div>

Thus this equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1250.jpg](images/e9780486140520_i1250.jpg)

</div>

<div class="caption">

(7.10–6)

</div>

</div>

where the previous solution for
<span class="i">ω</span><sub><span class="i">xy</span></sub>, Eq.
<span class="i">f</span> has been substituted.

This equation differs from that of the constant mass missile, first, by
the fact that the coefficient of
<span class="i">θ</span><sub><span class="i">xy</span></sub> which is
<span class="i">in</span> for the constant mass missile, is now a time
function,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1251.jpg](images/e9780486140520_i1251.jpg)

</div>

</div>

and, secondly, by the right–hand forcing term which is also different
due to ω<sub>z</sub> slowing down by jet damping and variable mass. The
equation is a time–variable linear differential equation which can be
solved for
<span class="i">θ</span><sub><span class="i">xy</span></sub>.<sup><a href="#e9780486140520_ftn01.html#ftn_fn8"
id="e9780486140520_c07.html_ref_ftn_fn8">h</a></sup>

The angle <span class="i">θ</span><sub><span class="i">xy</span></sub>
is referenced to the rotating body axes <span class="i">x, y</span> and
must be multiplied by
<span class="imageinline">![e9780486140520_i1253.jpg](images/e9780486140520_i1253.jpg)</span>
<span class="i">t</span> = in order to reference with respect to the
inertial axes. Thus the complete solution for the angle of attack as a
function of time and the variation of mass is possible by the foregoing
procedure.

<span class="b">PROBLEMS</span>

1.  Water is flowing out relative to the nozzle shown in the sketch at a
    speed of 30 ft/sec, and at a rate of 0.10 ft<sup>3</sup>/sec for
    each nozzle. If <span class="i">R</span> = 1.5 ft and the nozzles
    are rotated at 60 rpm, determine the torque necessary.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1254.jpg](images/e9780486140520_i1254.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob.1</span>

    </div>

    </div>

2.  The ends of the nozzle of Prob. 1 are bent back 30° so that the
    sprinkler will rotate by itself. If the resisting torque due to
    friction is 1.72 ft. lb, determine the speed in rpm with which the
    sprinkler will rotate.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1255.jpg](images/e9780486140520_i1255.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 2</span>

    </div>

    </div>

3.  A jet engine takes in air at a rate ṁ<sub>a</sub>, compresses it,
    mixes it with kerosene at a rate
    <span class="imageinline">![e9780486140520_i1256.jpg](images/e9780486140520_i1256.jpg)</span>
    , and ejects the ignited mixture at a speed <span class="i">u</span>
    relative to the nozzle. If the jet plane is traveling at a speed of
    ν, show that the thrust of the engine is
    <div class="blocktext">

    <span class="i">T</span> = ṁ<sub>k</sub>u + ṁ<sub>a</sub>(u–ν)

    </div>

4.  A nonspinning rocket of total mass
    <span class="i">m</span><sub><span class="i">0</span></sub>, half of
    which is fuel, is rotating about the pitch axis with an initial
    angular velocity of 0.5 rad/sec. If <span class="i">l/k</span> for
    the rocket remains constant at 2, determine the pitch rate at
    burnout.

5.  If in Prob. 4 the radius of gyration about the pitch axis decreased
    with time, would the pitch rate at burnout be larger or smaller?

6.  The ratio of the fuel to the total mass for a particular missile is
    0.70, and burning takes place with negligible change in the value of
    l/k = √3. If the rate of fuel consumption is
    <span class="i">m′/m</span><sub><span class="i">0</span></sub> =
    <span class="imageinline">![e9780486140520_i1257.jpg](images/e9780486140520_i1257.jpg)</span>
    sec<sup>−1</sup>, and the missile is rotating about a transverse
    axis without spin, plot the variation in its rotation speed against
    time.

7.  If for the spinning rocket with variable mass, the ratio
    <span class="i">p</span>/<span class="i">k</span><sub>z</sub> = 1
    and the quantity <span class="i">p/k</span> is negligible compared
    to <span class="i">l/k,</span> show that the equation for the
    complex angular velocity is

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1258.jpg](images/e9780486140520_i1258.jpg)

    </div>

    </div>

    How does this equation differ from that of the nonrotating rocket?

8.  For the case
    <span class="i">ρ</span><sup>2</sup><span class="i">/k</span><sub><span class="i">z</span></sub><sup>2</sup>
    = I and
    <span class="i">k</span><sub><span class="i">z</span></sub><sup>2</sup><span class="i">/k</span><sup>2</sup>
    is negligible compared to unity, the differential equation for the
    complex angle of attack, (Eq. 7.10–6) reduces to (see also Prob. 7),

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1259.jpg](images/e9780486140520_i1259.jpg)

    </div>

    </div>

    Letting
    <span class="i">m/m</span><sub><span class="i">0</span></sub> = I −
    \[(<span class="i">m</span>′/<span class="i">m</span><sub><span class="i">0</span></sub>)<span class="i">t</span>\],
    a closed form solution is possible when
    <span class="i">l</span><sup>2</sup><span class="i">/k</span><sup>2</sup>
    is an integer. Letting
    <span class="i">l</span><sup>2</sup><span class="i">/k</span><sup>2</sup>
    = 4, carry out this solution and show that the motion of the missile
    longitudinal axis is a converging spiral.

9.  Assuming the angle of attack <span class="i">θ</span> of a spinning
    missile to be small (angle of attack is measured from the velocity
    vector V which can be considered fixed in space) draw the inertial
    coordinates <span class="i">X</span>, <span class="i">Y</span>,
    <span class="i">Z</span>, the node axis <span class="i">ξ</span>,
    and the rotating body axes <span class="i">x</span>,
    <span class="i">y</span>, <span class="i">z</span>, where
    <span class="i">z</span> is the longitudinal axis of the missile at
    an angle <span class="i">θ</span> from the vector V placed along the
    Z axis. On this diagram show the complex angular velocity
    <span class="i">ω</span><sub><span class="i">xy</span></sub>,
    <span class="i">ω</span><sub><span class="i">z</span></sub>, and the
    resultant angular velocity <span class="i">ω</span>.

10. Assuming small angle of attack, determine the inertial components of
    the angular velocity <span class="i">ω</span> of Prob. 9, by
    resolving it along the Z axis and in the XY plane.

11. If the moment of inertia of the missile about the transverse and
    longitudinal axes are <span class="i">A</span> and
    <span class="i">C</span>, determine the position of the angular
    momentum vector for Prob. 9, and find the angle between it and the
    velocity vector. How does the angular momentum vector vary in the
    inertial space?

12. Compare the solution for the complex angle of attack
    <span class="i">θ</span><sub>xy</sub> of a missile with constant
    thrust misalignment <span class="i">M</span><sub>1</sub> (Prob. 10,
    Sec. 7.4) with that of the near symmetrical missile with principal
    axis misalignment of <span class="i">β</span>. Determine the product
    of inertia <span class="i">F</span> in terms of the misalignment
    moment <span class="i">M</span><sub>1</sub>, which will give the
    same motion.

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title105"></span>

# <span class="b">7.11 General Motion of Spinning Bodies with Varying Configuration and Mass</span>

In the previous sections the origin of the body axes always coincided
with the mass center. In the most general case, a body under translation
and rotation may have relative motion between particles leading to a
varying configuration, and may be undergoing a change in mass with time.
The origin of the body coordinates attached to the system will then not
coincide with the center of mass at all times. Relative motion between
particles could take place when motors and other moving parts are
present or when the body contains liquids such as fuel. Vibration due to
flexibility is another contributing factor. Mass variation would take
place owing to jets ejected from the body.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1260.jpg](images/e9780486140520_i1260.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_122"
id="e9780486140520_c07.html_int_122" class="label_int"><span
class="b">Fig. 7.11-1</span></a><span class="b">.</span> Body of varying
mass and configuration.

</div>

</div>

To examine the motion of such a general system, it is advisable to view
the problem as a system of particles with the origin of the body axes
not coinciding with the center of
mass.<sup>9<sup><a href="#e9780486140520_ftn01.html#ftn_fn9"
id="e9780486140520_c07.html_ref_ftn_fn9">i</a></sup></sup> Such a
procedure will account for every conceivable configuration of the system
and eliminate the possibility of omitting terms. In spite of this
generality, the terms of the equation can be regrouped to more familiar
forms of rigid body, jet ejection, center of mass shift, and relative
motion.

We define the system by a group of particles within a specified boundary
with body coordinates <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span> moving with the
system as shown in <a href="#e9780486140520_c07.html#int_122"
id="e9780486140520_c07.html_ref_int_122" class="ref_int">Fig. 7.11-1</a>.
Variation in mass is allowed by particles leaving the system through the
boundary. The angular momentum of the system about the moving origin 0
at time <span class="i">t</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1261.jpg](images/e9780486140520_i1261.jpg)

</div>

<div class="caption">

(7.11–1)

</div>

</div>

where <span class="b">r</span><sub><span class="i">i</span></sub> is
drawn from the moving origin 0, and Ṙ<sub>i</sub> is the absolute
velocity of <span class="i">m</span><sub><span class="i">i</span></sub>
referenced to the inertial axes <span class="b">X</span>,
<span class="b">Y</span>, <span class="b">Z</span>. If we differentiate
this equation, we obtain,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1262.jpg](images/e9780486140520_i1262.jpg)

</div>

<div class="caption">

(7.11–2)

</div>

</div>

From <a href="#e9780486140520_c07.html#int_122" class="ref_int">Fig.
7.11-1</a>, <span class="b">R</span><sub><span class="i">i</span></sub>
= <span class="b">R</span><sub>0</sub> +
<span class="b">r</span><sub><span class="i">i</span></sub>, and the
last term of Eq. 7.11–2 can be reduced by the following steps,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1263.jpg](images/e9780486140520_i1263.jpg)

</div>

</div>

where <span class="i">m</span> is the total mass at time
<span class="i">t,</span> and
<span class="imageinline">![e9780486140520_i1264.jpg](images/e9780486140520_i1264.jpg)</span>
its center of mass relative to the body axes.

Referring to the first term of Eq. 7.11–2,
(d/dt)(m<sub>i</sub>Ṙ<sub>i</sub>) is equal to the force applied to the
mass
<span class="i">m</span><sub><span class="i">i</span></sub><span class="i">,</span>
and its cross product with
<span class="b">r</span><sub><span class="i">i</span></sub> is the
moment about 0. Equation 7.11–2 can then be rewritten as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1265.jpg](images/e9780486140520_i1265.jpg)

</div>

<div class="caption">

(7.11–3)

</div>

</div>

which states that the moment about an arbitrary point 0 is equal to the
rate of change of the angular momentum
<span class="b">h</span><sub>0</sub> plus a term depending on the
velocity of the origin and the velocity of the center of mass with
respect to the origin. It is evident, then, that the moment is equal to
the rate of change of the angular momentum only under the following
conditions: (1) When 0 is stationary; (2) when the velocity of the
center of mass relative to the origin is zero; or (3) when the two
velocities Ṙ<sub>0</sub> and
<span class="imageinline">![e9780486140520_i1266.jpg](images/e9780486140520_i1266.jpg)</span>
are parallel.

The moment equation for the general system can be found directly from
the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1267.jpg](images/e9780486140520_i1267.jpg)

</div>

<div class="caption">

(7.11–4)

</div>

</div>

However, to clarify certain concepts, we will examine the angular
momentum at two instances of time and determine ḣ<sub>0</sub> to be
substituted into Eq. 7.11–3.

<a href="#e9780486140520_c07.html#int_123"
id="e9780486140520_c07.html_ref_int_123" class="ref_int">Figure
7.11-2</a> shows a mass
<span class="i">m</span><sub><span class="i">i</span></sub> at time
<span class="i">t</span>, which at a later time <span class="i">t</span>
= Δ<span class="i">t</span> occupies a different position
(<span class="b">r</span><sub><span class="i">i</span></sub> +
Δ<span class="b">r</span><sub><span class="i">i</span></sub>) and has
separated into two parts,
<span class="i">m</span><sub><span class="i">i</span></sub> +
ṁ<sub>i</sub> Δt and ∆t), with relative velocity
u<sub><span class="i">i</span></sub> between them. In separating into
two parts, <span class="i">m</span> is decreasing and ṁ =
<span class="i">dm/dt</span> is a negative quantity. The angular
momentum at <span class="i">t</span> + Δ<span class="i">t</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1268.jpg](images/e9780486140520_i1268.jpg)

</div>

<div class="caption">

(7.11–5) <sup><a href="#e9780486140520_ftn01.html#ftn_fn10"
id="e9780486140520_c07.html_ref_ftn_fn10">j</a></sup>

</div>

</div>

and, by neglecting higher order infinitesimals and approaching the limit
Δ<span class="b">h</span><sub>0</sub>/Δ<span class="i">t</span>, as
(Δ<span class="i">t</span> → 0) the rate of change of the angular
momentum becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1269.jpg](images/e9780486140520_i1269.jpg)

</div>

<div class="caption">

(7.11–6)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1270.jpg](images/e9780486140520_i1270.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_123"
id="e9780486140520_c07.html_int_123" class="label_int"><span
class="b">Fig. 7.11-2</span></a>. Angular momentum of element
<span class="i">m</span> at times <span class="i">t</span> and
<span class="i">t</span> + Δ<span class="i">t</span>.

</div>

</div>

Substituting Eq. 7.11–6 into 7.11–3, the moment equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1271.jpg](images/e9780486140520_i1271.jpg)

</div>

<div class="caption">

(7.11–7)

</div>

</div>

which could have been obtained directly from Eq. 7.11—4 by recognizing
that (<span class="i">d/dt</span>)(m<sub>i</sub>Ṙ<sub>i</sub>) =
ṁ<sub>i</sub>u<sub>i</sub> (see Sec. 7.7).\*

We now replace
<span class="imageinline">![e9780486140520_i1272.jpg](images/e9780486140520_i1272.jpg)</span>
by the general expression for acceleration,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1273.jpg](images/e9780486140520_i1273.jpg)

</div>

<div class="caption">

(7.11–8)

</div>

</div>

where \[<span class="b">r</span>\] and
<span class="imageinline">![e9780486140520_i1274.jpg](images/e9780486140520_i1274.jpg)</span>
are velocity and acceleration relative to the moving coordinate system,

<div class="illustype_image_text_net">

<div class="image_text_net">

![e9780486140520_i1275.jpg](images/e9780486140520_i1275.jpg)

</div>

<div class="caption">

(7.11–9)

</div>

</div>

To recognize the moment equation in terms of familiar expressions, we
<span class="imageinline">![e9780486140520_i1276.jpg](images/e9780486140520_i1276.jpg)</span>
= applied external force, therefore
<span class="i">M</span><sub><span class="i">0</span></sub> is the
moment of the externally applied force.

introduce the moment of inertia diadic of Sec. 5.2 and identify the
following:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1277.jpg](images/e9780486140520_i1277.jpg)

</div>

<div class="caption">

(7.11–10)<sup><a href="#e9780486140520_ftn01.html#ftn_fn12"
id="e9780486140520_c07.html_ref_ftn_fn12">k</a></sup>

</div>

</div>

Supplying the missing terms by adding and subtracting, the moment
equation can be written in the following forms:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1278.jpg](images/e9780486140520_i1278.jpg)

</div>

<div class="caption">

(7.11–12)

</div>

</div>

A third and a more convenient form can be found by reducing the first
two terms of the second line in Eq. 7.11–12 into a single term by the
following equation.<sup><a href="#e9780486140520_ftn01.html#ftn_fn11"
id="e9780486140520_c07.html_ref_ftn_fn11">l</a></sup>

<div class="blocktext">

<span class="b">a ×</span> (<span class="b">b × c</span>) +
(<span class="b">b × a</span>) <span class="b">× c</span> =
<span class="b">b ×</span> (<span class="b">a × c</span>)

<span class="b">Σ r</span><sub><span class="i">i</span></sub>
<span class="b">×</span>
<span class="i">m</span><sub><span class="i">i</span></sub>(<span class="b">ω</span>
× \[ṙ<sub>i</sub>\] + Σ
<span class="i">m</span><sub><span class="i">i</span></sub>(<span class="b">ω
× r</span><sub><span class="i">i</span></sub>) <span class="b">×</span>
\[ṙ<sub>i</sub>\] = <span class="b">ω × Σ</span>
(<span class="b">r</span><sub><span class="i">i</span></sub>
<span class="b">×</span> m<sub>i</sub>\[ṙ<sub>i</sub>\])

</div>

The third form of the moment equation then becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1279.jpg](images/e9780486140520_i1279.jpg)

</div>

<div class="caption">

(7.11–13)

</div>

</div>

The various terms of these equations can now be identified. We have in
the first term the effect of the origin of the body coordinates not
coinciding with the mass center. The terms
<span class="imageinline">![e9780486140520_i1280.jpg](images/e9780486140520_i1280.jpg)</span>correspond
to the usual Euler equation, whereas
<span class="imageinline">![e9780486140520_i1281.jpg](images/e9780486140520_i1281.jpg)</span>
includes the additional term
<span class="imageinline">![e9780486140520_i1282.jpg](images/e9780486140520_i1282.jpg)</span>
which accounts for the rate of change of the inertia diadic resulting
from the position change of the particles in relative motion and the
variation of mass. The term Σr<sub><span class="i">i</span></sub> ×
<span class="i">ṁ</span><sub><span class="i">i</span></sub>u<sub><span class="i">i</span></sub>
is the thrust misalignment
moment,<sup><a href="#e9780486140520_ftn01.html#ftn_fn13"
id="e9780486140520_c07.html_ref_ftn_fn13">m</a></sup> while the
term–∑r<sub><span class="i">i</span></sub> ×
<span class="i">ṁ</span><sub><span class="i">i</span></sub>(ω ×
r<sub><span class="i">i</span></sub>) is the jet damping due to rotation
of the body. All other terms are due to relative motion of particles.
The three forms of the moment equation, Eqs. 7.11–11, 7.11–12, and
7.11–13 are presented here to show the origin of the various terms, some
of which were inserted due to
<span class="imageinline">![e9780486140520_i1283.jpg](images/e9780486140520_i1283.jpg)</span>.

To complete the discussion, it must be recognized that the external
moment may result from the forces not directed through the origin of the
body coordinates. The external forces accelerate the instantaneous
center of mass and change the linear momentum of the ejected particles
according to the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1284.jpg](images/e9780486140520_i1284.jpg)

</div>

<div class="caption">

(7.11–14)

</div>

</div>

Thus, in the general case, the force equations are coupled to the moment
equations.

<span class="b">Example 7.11—1</span>

A space vehicle is moving under a force–free condition. If a motor
located at <span class="b">r</span><sub>1</sub> is started, determine
its perturbation torque.

The perturbation torque is the contribution from the relative motion
terms of Eqs. 7.11—11, 7.11—12, or 7.11–13. We will use the form given
by Eq. 7.11–13, which is (with total mass a constant, ṁ = 0)

<div class="blocktext">

<span class="imageinline">![e9780486140520_i1285.jpg](images/e9780486140520_i1285.jpg)</span>

</div>

Owing to the symmetry of the motor rotor, the change in the inertia
diadic relative to the body coordinates resulting from the spin of the
rotor is zero, which eliminates the first term
<span class="imageinline">![e9780486140520_i1286.jpg](images/e9780486140520_i1286.jpg)</span>
.

From <a href="#e9780486140520_c07.html#int_124"
id="e9780486140520_c07.html_ref_int_124" class="ref_int">Fig. 7.11-3</a>,
we have,

<div class="blocktext">

<span class="b">r</span><sub><span class="i">i</span></sub> =
<span class="b">r</span><sub>1</sub> +
<span class="b">ρ</span><sub><span class="i">i</span></sub>  
\[ṙ<sub>i</sub>\] = <span class="b">ω</span><sub>1</sub> x
ρ<sub>i</sub>  
<span class="imageinline">![e9780486140520_i1287.jpg](images/e9780486140520_i1287.jpg)</span>

</div>

and noting that <span class="b">Σ</span>
<span class="i">m</span><sub><span class="i">i</span></sub><span class="i">ρ</span><sub><span class="i">i</span></sub>
= 0 for a symmetrical wheel, the equation for the perturbation torque
becomes,

<div class="blocktext">

Since <span class="i">M</span><sub><span class="i">p</span></sub> = ω ×
\[Σρ<sub><span class="i">i</span></sub> × (ω<sub>1</sub> ×
<span class="i">m</span><sub><span class="i">i</span></sub><span class="i">ρ</span><sub><span class="i">i</span></sub>\] +
Σ ρ<span class="i">i</span> ×
<span class="imageinline">![e9780486140520_i1288.jpg](images/e9780486140520_i1288.jpg)</span>
Σ ρ<sub><span class="i">i</span></sub> × (ω<sub>1</sub> ×
<span class="i">m</span><sub><span class="i">i</span></sub><span class="i">ρ</span><sub><span class="i">i</span></sub>)
=
<span class="imageinline">![e9780486140520_i1289.jpg](images/e9780486140520_i1289.jpg)</span>=
(<span class="i">C</span><sub>1</sub><span class="i">ω</span><sub>1</sub>)k<sub>1</sub>
= h<sub>1</sub>

</div>

the equation for M<sub><span class="i">p</span></sub> can be written as

<div class="blocktext">

M<sub><span class="i">p</span></sub> = \[ḣ<sub>1</sub>\] + ω ×
h<sub>1</sub>

</div>

where h<sub>1</sub> is the angular momentum of the rotor wheel. Thus the
perturbation torque is the result of the angular acceleration of the
wheel, and the precession of the angular momentum vector of the wheel
caused by the rotation ω of the body coordinates.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1290.jpg](images/e9780486140520_i1290.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c07.html#ref_int_124"
id="e9780486140520_c07.html_int_124" class="label_int"><span
class="b">Fig. 7.11-3</span></a> Perturbation torque due to rotation of
wheel.

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A uniform rigid bar of length <span class="i">l</span> and mass
    <span class="i">m</span> is translating with constant velocity
    Ṙ<sub>0</sub> in a direction normal to its length. At the same time
    a mass <span class="i">m</span><sub><span class="i">0</span></sub>
    is sliding from one end to the other with velocity \[ṙ\]. Placing
    body coordinates as indicated in the sketch, verify from Eq. 7.11—3
    that the moment about <span class="i">O</span> is zero. Describe the
    motion of <span class="i">0</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1291.jpg](images/e9780486140520_i1291.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 1</span>

    </div>

    </div>

2.  The center of mass of a uniform rigid bar of length l is moving with
    constant velocity Ṙ along a straight line, while the bar rotates
    with constant angular velocity ω. Placing body axes as shown, verify
    from Eq. 7.11–3 that the moment about <span class="i">O</span> is
    zero.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1292.jpg](images/e9780486140520_i1292.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 2</span>

    </div>

    </div>

3.  For a system of particles which is not changing in mass, write the
    equation for the moment about its center of mass when relative
    motion betweeen particles is allowed.

4.  Consider a constant–mass system such as a satellite in orbit, and
    assume body axes <span class="i">x</span>, <span class="i">y</span>,
    <span class="i">z</span> through its center of mass and coinciding
    with the principal axes. There is a motor on the pitch axis
    <span class="i">x</span>, a distance
    <span class="i">x</span><sub>0</sub> from <span class="i">O</span>
    with its axis of rotation parallel to the <span class="i">y</span>
    axis. Let the rotor moment of inertia be
    <span class="imageinline">![e9780486140520_i1293.jpg](images/e9780486140520_i1293.jpg)</span>
    and that of the entire satellite including the motor to be
    <span class="i">A, A, C</span> about <span class="i">x</span>,
    <span class="i">y</span>, <span class="i">z</span> respectively. If
    the motor is started with angular acceleration
    <span class="imageinline">![e9780486140520_i1294.jpg](images/e9780486140520_i1294.jpg)</span>
    , define the terms in Eq. 7.11—11 which apply to the problem, and
    write the components of the moment equation.

5.  Show that the angular momentum of a group of particles about an
    arbitrary origin is equal to

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1295.jpg](images/e9780486140520_i1295.jpg)

    </div>

    </div>

    where
    <span class="imageinline">![e9780486140520_i1296.jpg](images/e9780486140520_i1296.jpg)</span>
    = <span class="b">∫ r ×</span> (<span class="b">ω x r</span>)
    <span class="i">dm</span> and \[ṙ\] is the velocity relative to the
    rotating body axes.

6.  Show that the terms of the equation

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1297.jpg](images/e9780486140520_i1297.jpg)

    </div>

    </div>

    can be identified as

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1298.jpg](images/e9780486140520_i1298.jpg)

    </div>

    </div>

7.  . Show that

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1299.jpg](images/e9780486140520_i1299.jpg)

    </div>

    </div>

    Combining the results of Prob. 5 and 6, two of the terms add to give
    2 ∫ r × (ω × \[ṙ\]) <span class="i">dm</span>, while the terms ∫ (w
    × r) × \[ṙ\] <span class="i">dm</span> cancel each other. Now
    clarify the interpretation of Eqs. 7.11–9, 7.11–10, 7.11–11, and
    7.11–12.

8.  Write the component equations for the two terms
    <div class="blocktext">

    −Σ \[ṙ<sub>i</sub>\] ×
    <span class="i">m</span><sub><span class="i">i</span></sub>(ω ×
    r<sub><span class="i">i</span></sub>) + Σ
    r<sub><span class="i">i</span></sub> ×
    <span class="i">m</span><sub><span class="i">i</span></sub>(ω ×
    \[ṙ<sub>i</sub>\])

    </div>

    of Eq. 7.11–12.

9.  Write out the component terms of
    <span class="imageinline">![e9780486140520_i1300.jpg](images/e9780486140520_i1300.jpg)</span>
    and show that they represent the time derivative of
    <span class="imageinline">![e9780486140520_i1301.jpg](images/e9780486140520_i1301.jpg)</span>
    relative to the body coordinates. Identify the parts due to relative
    motion of the particles and those due to mass variation.

10. Show that
    <span class="imageinline">![e9780486140520_i1302.jpg](images/e9780486140520_i1302.jpg)</span>
    = Σ
    <span class="i">m</span><sub><span class="i">i</span></sub>(r<sub><span class="i">i·</span></sub>
    r<sub>i</sub>ℰ–<span class="b">r</span><sub><span class="i">i</span></sub><span class="b">r</span><sub><span class="i">i</span></sub>),
    where <span class="i">ℰ</span> = ii + jj + kk is a unit diad. Show
    also that
    <div class="blocktext">

    <span class="imageinline">![e9780486140520_i1303.jpg](images/e9780486140520_i1303.jpg)</span>
    = ∑ṁ<sub>i</sub>(r<sub><span class="i">i</span></sub> ·
    r<sub><span class="i">i</span></sub>ℰ −
    r<sub><span class="i">i</span></sub>r<sub><span class="i">i</span></sub>) +
    Σ
    <span class="i">m</span><sub><span class="i">i</span></sub><span class="i">(ṙ</span><sub><span class="i">i</span></sub>
    <span class="i">•
    r</span><sub><span class="i">i</span></sub><span class="i">ℰ</span> +
    r<sub>i</sub> • ṙ<sub>i</sub>ℰ–ṙ<sub>i</sub>r<sub>i–</sub>
    r<sub>i</sub>ṙ<sub>i</sub>)

    </div>

11. Derive Eqs. 7.9–7 and 7.9–8 as a special case of the general
    equation, Eq. 7.11–12. State the restrictions imposed on Eq. 7.11—12
    in arriving at the above equations.

12. A symmetrical spinning satellite in orbit has moments of inertia
    <span class="i">A, A, C</span> about the <span class="i">x</span>,
    <span class="i">y</span>, <span class="i">z</span> axes (including
    <span class="i">m</span><sub><span class="i">0</span></sub> at
    position <span class="i">ζ</span> = 0), as shown in the sketch.

    If the mass
    <span class="i">m</span><sub><span class="i">0</span></sub> is
    restricted to move in the z direction and has a restoring spring
    stiffness of <span class="i">k</span> with viscous damping
    <span class="i">c</span>, show that the differential equations of
    motion are:

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1304.jpg](images/e9780486140520_i1304.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 12</span>

    </div>

    </div>

    <span class="i">Moment:</span>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1305.jpg](images/e9780486140520_i1305.jpg)

    </div>

    </div>

    <span class="i">Force on mass
    m</span><sub><span class="i">0</span></sub> <span class="i">in z
    direction:</span>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1306.jpg](images/e9780486140520_i1306.jpg)

    </div>

    </div>

    <span class="i">Acceleration of origin:</span>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1307.jpg](images/e9780486140520_i1307.jpg)

    </div>

    </div>

</div>

<div class="section1">

<span id="e9780486140520_c07.html_title106"></span>

# <span class="b">REFERENCES</span>

1.  H. J. Cohen, “The Effect of Jet Damping on the Motion of the Able–1
    Third Stage,” Space Technology Laboratories Interoffice
    Correspondence (April 15, 1960).
2.  Ellis, J. W., and C. W. McArthur, “Applicability of Euler’s
    Dynamical Equations to Rocket Motion,” <span class="i">ARS
    Jour.,</span> <span class="b">29</span>, No. 11 (Nov. 1959),
    863–864.
3.  Jarmolow, K., “Dynamics of a Spinning Rocket with Varying Inertia
    and Applied Moment,” <span class="i">J. Appl. Phys.,</span>
    <span class="b">28</span>, No. 3 (1957), 308–313.
4.  Leon, H., “Angle of Attack Convergence of a Spinning Missile
    Descending Through the Atmosphere,” <span class="i">J. Aero/Space
    Sci.,</span> <span class="b">25</span>, No. 8 (Aug. 1958), 480–484.
5.  Leon, H., “Spin Dynamics of Rockets and Space Vehicles in Vacuum,”
    <span class="i">TR 59—0000— 00787,</span> Space Technology
    Laboratories (Sept. 16, 1959).
6.  Pilkington, W. C., “Vehicle Motion as Inferred from
    Radio–Signal–Strength Records,” <span class="i">External Publication
    No. 551,</span> Jet Propulsion Laboratory, Pasadena, Calif. (Sept.
    5, 1958).
7.  Reiter, G., <span class="i">Space Technology Laboratories
    Memo</span> (June 17, 1959).
8.  Thomson, W. T., and G. S. Reiter, “Attitude Drift of Space
    Vehicles,” <span class="i">J. Astronaut. Sci.,</span>
    <span class="b">VII</span>, No. 2 (1960), 29–34.
9.  Roberson, R. E., “Torques on a Satellite Vehicle from Internal
    Moving Parts,” <span class="i">J. Appl. Mech.,</span>
    <span class="b">25</span>, No. 2 (June 1958), 196–200.

</div>

</div>

<span id="e9780486140520_c08.html"></span>

<div class="chapter">

<span id="e9780486140520_c08.html_title107"></span>

# <span class="b">CHAPTER 8</span>

# <span class="b">Performance and Optimization</span>

In Chap. 4 it was shown that the problem of placing a satellite into an
orbit is a matter of achieving the required velocity at a specified
position in space. For earth–bound orbits the required velocity is in
the neighborhood of 25,000 ft/sec, whereas for the lunar mission a
velocity of approximately 35,000 ft/sec is necessary. In this chapter we
discuss the basic theory of rockets and examine the problems of
optimization to meet a specific performance. Missile flexibility as it
affects the desired performance will be discussed in Chap. 9.

<div class="section1">

<span id="e9780486140520_c08.html_title108"></span>

# <span class="b">8.1 Performance of Single–Stage Rockets</span>

A rocket is a variable mass vehicle which acquires thrust by the
ejection of high–speed particles. The force equation for the rocket can
be written in the general form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1308.jpg](images/e9780486140520_i1308.jpg)

</div>

<div class="caption">

\(1\)

</div>

</div>

where <span class="b">T</span> is the thrust of the jet and
<span class="b">F</span><sub><span class="i">a</span></sub> is the
aerodynamic force. Since
<span class="b">F</span><sub>a</sub>/<span class="i">m</span> varies
inversely as the characteristic length of the rocket, this term is small
in comparison to <span class="b">T</span>/<span class="i">m</span> for
large rockets.

Certain parameters of importance can be brought out by studying the
behavior of a rocket in vertical flight, neglecting aerodynamic forces,
and assuming the gravity field to be a constant. Referring to
<a href="#e9780486140520_c08.html#int_125"
id="e9780486140520_c08.html_ref_int_125" class="ref_int">Fig. 8.1-1</a>,
we start with the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1309.jpg](images/e9780486140520_i1309.jpg)

</div>

<div class="caption">

(8.1–2)

</div>

</div>

Since the rocket is losing mass,
<span class="i">dm</span>/<span class="i">dt</span> is negative, and the
thrust becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1310.jpg](images/e9780486140520_i1310.jpg)

</div>

<div class="caption">

(8.1–3) <sup><a href="#e9780486140520_ftn01.html#ftn_fn14"
id="e9780486140520_c08.html_ref_ftn_fn14">n</a></sup>

</div>

</div>

where the small term due to the difference in pressure has been omitted.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1311.jpg](images/e9780486140520_i1311.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_125"
id="e9780486140520_c08.html_int_125" class="label_int"><span
class="b">Fig. 8.1-1</span></a><span class="b">.</span> Rocket in
vertical Hight.

</div>

</div>

Substituting Eq. 8.1–3 into 8.1–2,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1312.jpg](images/e9780486140520_i1312.jpg)

</div>

<div class="caption">

(8.1–4)

</div>

</div>

and integrating, the velocity equation becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1313.jpg](images/e9780486140520_i1313.jpg)

</div>

<div class="caption">

(8.1–5)

</div>

</div>

where <span class="i">m</span> is the mass at any time
<span class="i">t</span>. By substituting the burnout time
<span class="i">t</span><sub><span class="i">b</span>0</sub> and the
burnout mass
<span class="i">m</span><sub><span class="i">b</span>0</sub>, the
maximum attainable velocity in vertical flight is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1314.jpg](images/e9780486140520_i1314.jpg)

</div>

<div class="caption">

(8.1–6)

</div>

</div>

For chemical propellants, the ejection speed <span class="i">u</span>
relative to the rocket nozzle depends on the heat energy per pound which
must be high, and on the molecular weight which must be small. Its
performance is rated by the <span class="i">specific impulse I,</span>
defined as the thrust of a pound of propellant multiplied by the number
of seconds required to burn it. Its relationship to
<span class="i">u</span> is found from the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1315.jpg](images/e9780486140520_i1315.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1316.jpg](images/e9780486140520_i1316.jpg)

</div>

<div class="caption">

(8.1–7)

</div>

</div>

Some indication as to the merits of certain fuels and their propellant
combinations are obtainable from
<a href="#e9780486140520_c08.html#int_126"
id="e9780486140520_c08.html_ref_int_126" class="ref_int">Table 8-1</a>.

<div class="tableau">

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_126"
id="e9780486140520_c08.html_int_126" class="label_int"><span
class="b">Table 8-1</span></a><sup>a</sup>

</div>

| Chemical Propellants                     | Type  | Specific Impulse I, sec |
|:-----------------------------------------|:-----:|:-----------------------:|
| Ammonium nitrate rubber                  | Solid |         170–210         |
| Potassium perchlorite thickol or asphalt | Solid |         170—210         |
| Boron metal components and oxidant       | Solid |         200–250         |
| Liquid oxygen alcohol                    |       |         250–270         |
| Liquid oxygen fluorine JP4               |       |         270–330         |
| Fluorine hydrogen                        |       |         300–385         |

</div>

<sup>a</sup> “Astronautics and its Applications,” <span class="i">Space
Handbook,</span> U.S. Govt. Printing Office, Wash. D.C. (1959).

  
  

It is convenient here to introduce a thrust parameter which establishes
the initial acceleration of the rocket. We define thrust ratio
<span class="i">ℛ</span> as the thrust of the rocket divided by the
initial weight,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1318.jpg](images/e9780486140520_i1318.jpg)

</div>

<div class="caption">

(8.1–8)

</div>

</div>

where <span class="i">a</span><sub>0</sub> is the initial acceleration
in vertical flight. The time duration of the powered flight is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1319.jpg](images/e9780486140520_i1319.jpg)

</div>

<div class="caption">

(8.1—9)

</div>

</div>

Equation 8.1–4 can now be written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1320.jpg](images/e9780486140520_i1320.jpg)

</div>

<div class="caption">

(8.1–10)

</div>

</div>

which indicates that the maximum attainable velocity depends on the mass
fraction
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>,
on the specific impulse I of the fuel, and on the thrust ratio ℛ.

With ν<sub>0</sub> = 0, it is possible to plot
ν<sub><span class="i">b</span>0</sub>/<span class="i">gI</span> versus
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>,
with ℛ as a parameter. It is instructive, however, to plot
ν<sub><span class="i">b</span>0</sub> versus
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>
for given values of <span class="i">I</span> and ℛ as in
<a href="#e9780486140520_c08.html#int_127"
id="e9780486140520_c08.html_ref_int_127" class="ref_int">Fig. 8.1-2</a>,
since such a plot indicates the inadequacy

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1321.jpg](images/e9780486140520_i1321.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_127"
id="e9780486140520_c08.html_int_127" class="label_int"><span
class="b">Fig. 8.1-2</span></a><span class="b">.</span> Burnout velocity
as function of mass ratio, specific impulse <span class="i">I</span>,
and thrust ratio ℛ.

</div>

</div>

of a single–stage rocket for placing a satellite into orbit. As in most
designs, a compromise must be established between, ℛ,
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>,
and <span class="i">I</span> (i.e., a large thrust ratio requires a
heavier structure, and exotic fuels of high <span class="i">I</span>
tend to give larger values of
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>.
In any event, it is difficult to achieve a number less than 0.1 for
<span class="i">m</span><sub><span class="i">b</span>0</sub>/<span class="i">m</span><sub>0</sub>
and a specific impulse greater than 350 for chemical propellants, which
indicates the necessity of multistage rockets for satellite orbits and
space missions.

To determine the distance traveled during the powered flight, the
velocity equation, Eq. 8.1–5, must be integrated. Equation 8.1–5 can be
integrated if the variation in g is assumed to be negligible and
<span class="i">m</span>(<span class="i">t</span>) known. A realistic
assumption is that of constant rate of fuel consumption leading to
constant thrust. We can then let

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1322.jpg](images/e9780486140520_i1322.jpg)

</div>

</div>

so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1323.jpg](images/e9780486140520_i1323.jpg)

</div>

</div>

The distance traveled then becomes,

<div class="illustype_image_text_net">

<div class="image_text_net">

![e9780486140520_i1324.jpg](images/e9780486140520_i1324.jpg)

</div>

<div class="caption">

(8.1—11)

</div>

</div>

After burnout, the rocket is in free flight under the retarding force of
gravity. In general, the altitude is sufficiently great so that the
variation in g must now be taken into account. Since the system during
coasting is conservative, we can equate the kinetic energy at burnout to
the work done by the gravity force m<sub>b0</sub>g<sub>0</sub>
<span class="imageinline">![e9780486140520_i1325.jpg](images/e9780486140520_i1325.jpg)</span>
<sub>.</sub>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1326.jpg](images/e9780486140520_i1326.jpg)

</div>

</div>

Thus the equation for the coasting distance becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1327.jpg](images/e9780486140520_i1327.jpg)

</div>

<div class="caption">

(8.1–12)

</div>

</div>

where <span class="i">r</span><sub><span class="i">b</span>0</sub> =
<span class="i">R</span> +
<span class="i">h</span><sub><span class="i">b</span>0</sub> has been
substituted. The total height
<span class="i">h</span><sub><span class="i">b</span>0</sub> +
<span class="i">h</span><sub><span class="i">c</span></sub> reached by a
single stage rocket is then the sum of Eqs. 8.1–11 and 8.1–12.

Equations 8.1–10 and 8.1–11 indicate that the performance of a
single–stage rocket depends on the specific impulse I, the thrust ratio
ℛ, and the mass ratio
<span class="imageinline">![e9780486140520_i1328.jpg](images/e9780486140520_i1328.jpg)</span>
. The effect of varying these quantities on the burnout velocity or
height can be found by considering Eqs. 8.1–10 and 8.1–11 to be in the
form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1329.jpg](images/e9780486140520_i1329.jpg)

</div>

<div class="caption">

(8.1–13)

</div>

</div>

and differentiating. Thus the change in the burnout velocity is
determined from the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1330.jpg](images/e9780486140520_i1330.jpg)

</div>

<div class="caption">

(8.1–14)

</div>

</div>

For optimum burnout velocity,
<span class="i">dν</span><sub><span class="i">b</span>0</sub> = 0, which
defines the constraints imposed on the three quantities.

<span class="b">PROBLEMS</span>

1.  For a given mass ratio µ and specific impulse
    <span class="i">I</span>, how does the burnout velocity of a
    single–stage rocket vary with the thrust ratio ℛ. Assume vertical
    flight.
2.  Plot
    ν<sub><span class="i">b</span>0</sub>/<span class="i">g</span><sub>0</sub><span class="i">I</span>
    versus <span class="i">µ</span> =
    <span class="i">m</span><sub>0</sub>/<span class="i">m</span><sub><span class="i">b</span>0</sub>,
    with ν<sub>0</sub> = 0 and ℛ as parameter. Use ℛ = 1, 2, 5.
3.  For a given specific impulse and thrust ratio, plot
    <span class="i">h</span><sub><span class="i">b</span>0</sub> versus
    <span class="i">µ</span> =
    <span class="i">m</span><sub>0</sub>/<span class="i">m</span><sub><span class="i">b</span>0</sub>.
    Use ℛ = 2 and <span class="i">I</span> = 150, 300 and 400 sec.
4.  Determine the burnout speed of a rocket launched vertically, using a
    fuel of specific impulse 250 sec and a mass fraction of 0.22 with ℛ
    = 3.
5.  For <span class="i">I</span> = 300 sec and ℛ = 2, determine the
    maximum height attained by a single–stage rocket of mass ratio
    <span class="i">µ</span> = 5.
6.  Repeat Prob. 5 for <span class="i">µ</span> = 3 and
    <span class="i">µ</span> = 10, and plot
    <span class="i">h</span><sub>max</sub> versus
    <span class="i">µ</span>.
7.  Determine the partial derivatives
    <span class="i">∂f</span><sub>1</sub>/<span class="i">∂I</span>,
    <span class="i">∂f</span><sub>1</sub>/<span class="i">∂</span>ℛ, and
    <span class="i">∂</span>f<sub>1</sub>/<span class="i">∂µ</span> of
    Eq. 8.1–14. How much would the burnout velocity of Prob. 5 be
    changed by changing <span class="i">I</span> to 250 sec; by changing
    <span class="i">µ</span> to 6.0.
8.  Determine the partial derivatives
    <span class="i">∂f</span><sub>2</sub>/<span class="i">∂I</span>,
    <span class="i">∂f</span><sub>2</sub>/<span class="i">∂</span>ℛ, and
    <span class="i">∂f</span><sub>2</sub>/<span class="i">∂µ</span> from
    Eq. 8.1–11 and discuss the effect of changing
    <span class="i">I</span>, ℛ, or <span class="i">µ</span>.
9.  If the burnout velocity of a rocket fired vertically is 8500 ft/sec
    at a height of <span class="i">h</span> miles, how high will it rise
    when constant gravitational acceleration is assumed?
10. Assuming a burnout velocity of ν<sub><span class="i">b</span>0</sub>
    at <span class="i">r</span> = <span class="i">R</span> +
    <span class="i">h</span>, and an inverse square attractive force,
    determine the maximum height reached by a rocket. What is the
    maximum height for data of Prob. 9 under this assumption?
11. If the specific impulse of a rocket engine is doubled by doubling
    the burning time, keeping the thrust per pound of fuel constant, how
    does this affect the burnout velocity?
12. If the mass ratio of a rocket is doubled, keeping all other
    variables constant, how does this affect the burnout height for
    vertical flight?
13. A rocket fired vertically from rest has an initial weight of 10,000
    lb and a burnout weight of 2000 lb. The flux velocity of the fuel is
    a constant and equal to 7500 ft/sec, and the total burning time is
    55 sec. Determine the velocity and acceleration just before burnout,
    and calculate the height to which it will rise by equating the
    kinetic energy to the work done under (a) varying gravity:
    (<span class="i">b</span>) constant gravity.
14. The efficiency of a rocket engine can be defined as the ratio of the
    useful power <span class="i">Tυ</span> (<span class="i">T</span> =
    thrust) to the useful power plus the kinetic energy
    ½<span class="i">m</span>′(<span class="i">u</span> − ν)<sup>2</sup>
    lost to the surroundings. Show that the rocket efficiency is given
    by the equation.
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1331.jpg](images/e9780486140520_i1331.jpg)

    </div>

    </div>

    and find the value of
    <span class="i">u</span>/<span class="i">υ</span> corresponding to
    its maximum.
15. Repeat Prob. 14 for a jet engine.

</div>

<div class="section1">

<span id="e9780486140520_c08.html_title109"></span>

# <span class="b">8.2 Optimization of Multistage Rockets</span><sup>2</sup>

A simple calculation with achievable mass ratio, thrust ratio, and
specific impulse indicates that satellite velocities cannot be attained
by the use of a single–stage rocket. We are thus led to the multistage
rocket for space missions.

In a multistage rocket the burnout velocity of the first stage becomes
the initial velocity <span class="i">υ</span><sub>0</sub> of the second
stage, and, by casting off the empty first stage, the full burnout
velocity of the second stage is available as an additional velocity to
the burnout velocity of the first stage. The maximum velocity of a
multistage rocket can then be computed as the sum of the single–stage
velocities, as given by Eq. 8.1–6.

We will ignore the gravity loss in velocity due to the burning time, in
which case the maximum velocity available to the multistage rocket of
<span class="i">N</span> stages becomes.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1332.jpg](images/e9780486140520_i1332.jpg)

</div>

<div class="caption">

(8.2–1)

</div>

</div>

where µ<sub><span class="i">i</span></sub> =
(<span class="i">m</span><sub>0</sub>/<span class="i">m</span><sub><span class="i">b</span>0</sub>)<sub>i</sub>
is the mass ratio of the ith stage. Assuming that this velocity is
specified, we have a choice as to how the mass ratios should be assigned
to the various stages. The problem is that of minimizing the over–all
mass ratio
<span class="i">m</span><sub>01</sub>/<span class="i">P</span>, where
<span class="i">m</span><sub>01</sub> is the takeoff mass and
<span class="i">P</span> the final payload mass.

To determine the mass ratio µ<sub><span class="i">i</span></sub> which
will lead to a minimum over–all mass ratio
<span class="i">m</span><sub>01</sub>/<span class="i">P</span> for a
specified maximum velocity
<span class="i">v</span><sub><span class="i">m</span></sub>, it is
necessary to express
<span class="i">m</span><sub>01</sub>/<span class="i">P</span> in terms
of all the µ<sub><span class="i">i</span></sub>. Since at each burnout
the empty structure of the stage is to be discarded, the initial mass of
the new stage is equal to the initial mass of the previous stage minus
the fuel burned and the empty structure thrown off. For example, the
initial mass of the second stage is
<span class="i">m</span><sub>02</sub> =
<span class="i">m</span><sub>01</sub> −
<span class="i">m</span><sub><span class="i">p</span>1</sub> −
<span class="i">m</span><sub><span class="i">s</span>1</sub>, where
<span class="i">m</span><sub><span class="i">p</span>1</sub> is the
propellant mass of stage 1 and
<span class="i">m</span><sub><span class="i">s</span>1</sub> the empty
structural mass of stage 1. Thus by writing
<span class="i">m</span><sub>01</sub>/<span class="i">P</span> in the
form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1333.jpg](images/e9780486140520_i1333.jpg)

</div>

<div class="caption">

(8.2–2)

</div>

</div>

it is possible to express the over–all mass ratio in terms of all the
mass ratios

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1334.jpg](images/e9780486140520_i1334.jpg)

</div>

<div class="caption">

(8.2–3)

</div>

</div>

and an additional structural factor <span class="i">β</span><sub>i</sub>
defined as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1335.jpg](images/e9780486140520_i1335.jpg)

</div>

<div class="caption">

(8.2—4)

</div>

</div>

Examining one of the factors, we can write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1336.jpg](images/e9780486140520_i1336.jpg)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1337.jpg](images/e9780486140520_i1337.jpg)

</div>

<div class="caption">

(8.2–5)

</div>

</div>

Equation 8.2–2 can then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1338.jpg](images/e9780486140520_i1338.jpg)

</div>

<div class="caption">

(8.2–6)

</div>

</div>

If <span class="i">m</span><sub>01</sub>/<span class="i">P</span> is to
be a minimum, ln
(<span class="i">m</span><sub>01</sub>/<span class="i">P</span>), will
also be a minimum, so that we can write,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1339.jpg](images/e9780486140520_i1339.jpg)

</div>

<div class="caption">

(8.2–7)

</div>

</div>

The above equation by itself does not contain the constraint imposed by
the specified velocity as given by Eq. 8.2–1. This constraint can be
imposed on the optimization process by the Lagrange multiplier method,
which requires the constraint equation to be multiplied by a constant
<span class="i">λ</span> and added to the above equation (adding zero),
as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1340.jpg](images/e9780486140520_i1340.jpg)

</div>

<div class="caption">

(8.2–8)

</div>

</div>

Differentiation of this equation with respect to
µ<sub><span class="i">i</span></sub> will lead to the optimum values of
µ<sub><span class="i">i</span></sub>.

Carrying out the differentiation, we obtain N equations of the form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1341.jpg](images/e9780486140520_i1341.jpg)

</div>

</div>

leading to the result

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1342.jpg](images/e9780486140520_i1342.jpg)

</div>

<div class="caption">

(8.2–9)

</div>

</div>

Substituting this value of µ<sub><span class="i">i</span></sub> into Eq.
8.2–1, the constant <span class="i">λ</span> can be found from the
equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1343.jpg](images/e9780486140520_i1343.jpg)

</div>

<div class="caption">

(8.2–10)

</div>

</div>

where <span class="i">u</span><sub><span class="i">i</span></sub>,
<span class="i">β</span><sub><span class="i">i</span></sub>, and
<span class="i">v</span><sub><span class="i">m</span></sub> are assumed
to be known. With <span class="i">λ</span> evaluated, the mass ratio
<span class="i">µ</span><sub><span class="i">i</span></sub> of each
stage is found from Eq. 8.2–9.

<span class="b">Example 8.2—1</span>

Consider a special case where the specific impulse is the same for all
stages. The u<sub>i</sub> are then equal in all stages and Eq. 8.2–10
becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1344.jpg](images/e9780486140520_i1344.jpg)

</div>

</div>

Since from Eq. 8.2–9

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1345.jpg](images/e9780486140520_i1345.jpg)

</div>

</div>

the mass ratio of stage <span class="i">i</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1346.jpg](images/e9780486140520_i1346.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  Show that if
    <span class="i">u</span><sub><span class="i">i</span></sub> and
    <span class="i">β</span><sub><span class="i">i</span></sub> are the
    same for each stage, the optimum mass ratio is
    <div class="blocktext">

    <span class="i">µ</span><sub><span class="i">i</span></sub> =
    <sub><span class="i">e</span></sub><span class="i">ν</span><sub><span class="i">m</span></sub>/<span class="i"><sup>Nu</sup></span>

    </div>
2.  A two–stage rocket is to attain a maximum speed of 26,000 ft/sec
    with <span class="i">I</span><sub>1</sub> =
    <span class="i">I</span><sub><span class="i">2</span></sub> = 300
    sec and <span class="i">β</span><sub>1</sub> =
    <span class="i">β</span><sub>2</sub>. Determine the mass ratio of
    each stage.
    <div class="blocktext">

    Ans. µ = 3.85.

    </div>
3.  In Prob. 2, determine the propellant mass per stage in terms of the
    initial mass of the stage. Also determine the structural factor
    <span class="i">β</span><sub><span class="i">i</span></sub>,
    assuming
    <span class="i">m</span><sub><span class="i">si</span></sub> =
    0.15<span class="i">m</span><sub>0<span class="i">i</span></sub>,
    and show that the optimum over–all mass ratio is equal to
    <span class="i">m</span><sub>01</sub>/<span class="i">P</span> =
    82.4.
4.  In designing a two–stage rocket for a maximum speed of 26,000
    ft/sec, assume that <span class="i">I</span><sub>1</sub> =
    <span class="i">I</span><sub>2</sub> = 250 sec, and
    <span class="i">β</span><sub>1</sub> = 0.18,
    <span class="i">β</span><sub>2</sub> = 0.15. Show that it is capable
    of boosting a payload of
    0.00172<span class="i">m</span><sub>01</sub>.

</div>

<div class="section1">

<span id="e9780486140520_c08.html_title110"></span>

# <span class="b">8.3 Flight Trajectory Optimization</span><sup><span class="b">3</span></sup>

We will now consider a more difficult problem of establishing an optimum
flight path to place a satellite into orbit. The rocket is assumed to be
rigid, and we will neglect the aerodynamic forces. Generally, the length
of the powered flight path is short compared to the earth’s radius, and
we are justified in replacing the central gravitational field by a
constant–plane parallel–force field.

The geometry of the problem, illustrated in
<a href="#e9780486140520_c08.html#int_128"
id="e9780486140520_c08.html_ref_int_128" class="ref_int">Fig. 8.3-1</a>,
shows the thrust attitude angle <span class="i">φ</span> measured from
the horizontal, the gravitational force along the negative
<span class="i">y</span> direction, and the velocity vector tangent to
the flight trajectory. Letting <span class="i">u</span> and
<span class="i">w</span> be the <span class="i">x</span> and
<span class="i">y</span> components of the velocity
<span class="i">v</span>, the differential equation of motion in
rectangular coordinates are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1347.jpg](images/e9780486140520_i1347.jpg)

</div>

<div class="caption">

(8.3–1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1348.jpg](images/e9780486140520_i1348.jpg)

</div>

<div class="caption">

(8.3–2)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1349.jpg](images/e9780486140520_i1349.jpg)

</div>

<div class="caption">

(8.3–3)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1350.jpg](images/e9780486140520_i1350.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_128"
id="e9780486140520_c08.html_int_128" class="label_int"><span
class="b">Fig. 8.3-1</span></a><span class="b">.</span> Powered flight
trajectory.

</div>

</div>

The quantities <span class="i">F</span>/<span class="i">m</span> and
<span class="i">φ</span> are functions of time, and the trajectory
depends on how they vary. We will assume that
<span class="i">F</span>/<span class="i">m</span> is a known function of
time, and define the problem of selecting
<span class="i">φ</span>(<span class="i">t</span>) for maximum
horizontal velocity <span class="i">U</span> at a specified altitude
<span class="i">Y</span>. The time <span class="i">T</span>
corresponding to the instant <span class="i">y</span> =
<span class="i">Y</span> will differ with different
<span class="i">φ</span>(<span class="i">t</span>) and, therefore, will
not be specified. We will assume however that all of the fuel be burned
prior to the time <span class="i">T</span>.

The problem which we have just defined differs from the previous one of
vertical flight in that we must maximize a time integral with
constraints. The equation which we are concerned with is the integral of
Eq. 8.3–1,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1351.jpg](images/e9780486140520_i1351.jpg)

</div>

<div class="caption">

(8.3–4)

</div>

</div>

which we wish to make a maximum at a specified value of
<span class="i">y</span> under the condition
<span class="i">w</span><sub><span class="i">t</span>=<span class="i">T</span></sub>
= 0. Thus Eqs. 8.3–2 and 8.3–3 represent constraints on the allowable
variations of Eq. 8.3–4. We write Eqs. 8.3–2 and 8.3–3 in the form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1352.jpg](images/e9780486140520_i1352.jpg)

</div>

<div class="caption">

(8.3–2a)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1353.jpg](images/e9780486140520_i1353.jpg)

</div>

<div class="caption">

(8.3–3a)

</div>

</div>

multiply each by undetermined time functions <span class="i">λ</span>,
and rewrite Eq. 8.3–4 in the form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1354.jpg](images/e9780486140520_i1354.jpg)

</div>

<div class="caption">

(8.3–5)

</div>

</div>

We must now specify the boundary conditions under which the optimization
is to take place.

At <span class="i">t</span> = 0

<div class="blocktext">

<span class="i">y</span> =
<span class="i">y</span><sub><span class="i">0</span></sub>  
<span class="i">u</span><sub>0</sub> = ν<sub>0</sub> cos
<span class="i">θ</span><sub>0</sub>  
<span class="i">x</span> = 0  
<span class="i">w</span><sub>0</sub> = υ<sub>0</sub> sin
<span class="i">θ</span><sub>0</sub>

</div>

At <span class="i">t</span> = <span class="i">T</span>

<div class="blocktext">

  
<span class="i">y</span> = <span class="i">Y</span>  
<span class="i">w</span> = 0

</div>

The initial velocity ν<sub>0</sub> at initial altitude
<span class="i">y</span><sub>0</sub> will be considered fixed, but the
initial angle <span class="i">θ</span><sub>0</sub> will be left
undetermined, thereby allowing the first term of Eq. 8.3–5 to contribute
a term at the lower limit <span class="i">t</span> = 0.

Before applying Eq. C–9 of Appendix C to Eq. 8.3–5, we will dispense
with the first term <span class="i">u</span><sub>0</sub> = υ<sub>0</sub>
cos <span class="i">θ</span><sub>0</sub> by noting that its contribution
to <span class="i">δU</span> is <span class="i">−υ</span><sub>0</sub>
sin <span class="i">θ</span><sub>0</sub>
<span class="i">δθ</span><sub>0</sub>. We are then left with the
integral of Eq. 8.3–5, where in place of the variable
<span class="i">z</span>, we have <span class="i">φ</span>,
<span class="i">w</span>, <span class="i">y</span>,
<span class="i">F</span>/<span class="i">m</span>, and
<span class="i">T</span>. The equation with which we are concerned is,
then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1355.jpg](images/e9780486140520_i1355.jpg)

</div>

<div class="caption">

(8.3–6)

</div>

</div>

where the variation of the integral is to be determined from Eq. C–9.

For the first problem, <span class="i">F</span>/<span class="i">m</span>
is assumed to be a known function of time which is not varied, and we
are to find a <span class="i">φ</span>(<span class="i">t</span>) which
will result in a maximum horizontal velocity <span class="i">U</span> at
a given height <span class="i">Y</span>. The partial derivatives
indicated in Eq. C–9 are determined from Eq. 8.3–5 to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1356.jpg](images/e9780486140520_i1356.jpg)

</div>

</div>

The total variation from Eq. C–9 is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1357.jpg](images/e9780486140520_i1357.jpg)

</div>

<div class="caption">

(8.3–7)

</div>

</div>

Since <span class="i">y</span> at <span class="i">t</span> = 0 and
<span class="i">t</span> = <span class="i">T</span> are fixed as
<span class="i">y</span><sub>0</sub> and <span class="i">Y</span>, the
variation at the end points must be zero, which eliminates the third
term in Eq. 8.3–7. For the second term of Eq. 8.3–7, the variation δw at
<span class="i">t</span> = 0 is (υ<sub>0</sub> is specified as fixed),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1358.jpg](images/e9780486140520_i1358.jpg)

</div>

</div>

At the terminal time <span class="i">t</span> =
<span class="i">T</span>, <span class="i">w</span> is obtained from the
integral of Eq. 8.3–2a to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1359.jpg](images/e9780486140520_i1359.jpg)

</div>

</div>

and its variation at <span class="i">t</span> = <span class="i">T</span>
due to variations <span class="i">δφ</span> and
<span class="i">δθ</span><sub>0</sub> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1360.jpg](images/e9780486140520_i1360.jpg)

</div>

</div>

We note that w for the optimum curve becomes zero at
<span class="i">t</span> = <span class="i">T</span>, whereas for the
varied curve <span class="i">w</span> becomes zero at a different time
<span class="i">T</span> + <span class="i">δT</span>. Since
<span class="imageinline">![e9780486140520_i1361.jpg](images/e9780486140520_i1361.jpg)</span>is
not varied and is zero for <span class="i">t</span> \>
<span class="i">T</span>, the above expression for
<span class="i">δw</span>▕<sup><span class="i">T</span></sup> must equal
g δT.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1362.jpg](images/e9780486140520_i1362.jpg)

</div>

<div class="caption">

(8.3–8)

</div>

</div>

Since the variations <span class="i">δθ</span><sub>0</sub>,
<span class="i">δT</span>, <span class="i">δφ</span>, etc., are
arbitrary, <span class="i">δU</span> can be zero only if all their
coefficients are zero, or

<div class="blocktext">

tan <span class="i">θ</span><sub>0</sub> = −
<span class="i">λ</span><sub>1,<span class="i">t</span>=0</sub>  
λ<sub>1,<span class="i">t</span>=<span class="i">T</span></sub> = 0  
tan <span class="i">φ</span> = −<span class="i">λ</span><sub>1</sub>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1363.jpg](images/e9780486140520_i1363.jpg)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1364.jpg](images/e9780486140520_i1364.jpg)

</div>

</div>

From the last two equations we, obtain

<div class="blocktext">

<span class="i">λ</span><sub>2</sub> =
−<span class="i">C</span><sub>2</sub> (a constant)

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1365.jpg](images/e9780486140520_i1365.jpg)

</div>

</div>

Substituting for <span class="i">λ</span><sub>1</sub> at
<span class="i">t</span> = 0, and <span class="i">t</span> =
<span class="i">T</span> from the first two equations, we find

<div class="blocktext">

<span class="i">C</span><sub>1</sub> =–tan
<span class="i">θ</span><sub>0</sub>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1366.jpg](images/e9780486140520_i1366.jpg)

</div>

</div>

so that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1367.jpg](images/e9780486140520_i1367.jpg)

</div>

</div>

The equation for the thrust attitude is then obtained from the third
equation to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1368.jpg](images/e9780486140520_i1368.jpg)

</div>

<div class="caption">

(8.3–9)

</div>

</div>

and <span class="i">φ</span> varies from
<span class="i">θ</span><sub>0</sub> to zero according to Eq. 8.3–9.

</div>

<div class="section1">

<span id="e9780486140520_c08.html_title111"></span>

# <span class="b">8.4 Optimum Program for Propellant Utilization</span>

In the problem just discussed, it was found that, for an arbitrarily
defined time variation of
<span class="i">F</span>/<span class="i">m</span>, the optimum program
for the thrust attitude, where the initial angle
<span class="i">θ</span><sub>0</sub> was also allowed a variation, was
found to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1369.jpg](images/e9780486140520_i1369.jpg)

</div>

<div class="caption">

(8.4–1)

</div>

</div>

If the initial angle <span class="i">θ</span><sub>0</sub> is a given
quantity which is not allowed a variation, the optimum thrust attitude
will still be a linear function of time but of the form (see Prob.
8.4–1),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1370.jpg](images/e9780486140520_i1370.jpg)

</div>

<div class="caption">

(8.4–2)

</div>

</div>

In either case, the above thrust attitude programs result in a maximum
horizontal velocity <span class="i">U</span> for the specified program
of <span class="i">F</span>/<span class="i">m</span>. The maximum
<span class="i">U</span> attained will, however, differ with different
programs of <span class="i">F</span>/<span class="i">m</span>, or the
manner of propellant utilization, and we wish now to establish the
optimum program for propellant utilization to obtain the largest of the
maximum <span class="i">U</span> attained under optimum thrust attitude
variation.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1371.jpg](images/e9780486140520_i1371.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_129"
id="e9780486140520_c08.html_int_129" class="label_int"><span
class="b">Fig. 8.4-1</span></a><span class="b">.</span> Possible
variation of <span class="i">V</span>.

</div>

</div>

We recognize here that the theoretically attainable velocity
<span class="i">V</span><sub><span class="i">k</span></sub> in the
absence of all forces other than thrust, is essentially a function of
the specific impulse <span class="i">I</span> of the fuel and the mass
ratio of the rocket (see Sec. 8.1)

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1372.jpg](images/e9780486140520_i1372.jpg)

</div>

</div>

where it is assumed that the specific impulse is independent of the
manner in which the fuel is utilized. It is then convenient to make the
following substitution

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1373.jpg](images/e9780486140520_i1373.jpg)

</div>

<div class="caption">

(8.4–3)

</div>

</div>

where <span class="i">V</span> is the rocket thrust velocity with the
maximum attainable value equal to
<span class="i">V</span><sub><span class="i">k</span></sub>. It is
evident that <span class="i">V</span> is a function only of time, and
depends on the manner in which the fuel is consumed. Thus for any
program of propellant utilization, any curve between
<span class="i">V</span> = 0 and
<span class="i">V</span><sub><span class="i">k</span></sub> with
positive slope (including zero), as shown in
<a href="#e9780486140520_c08.html#int_129"
id="e9780486140520_c08.html_ref_int_129" class="ref_int">Fig. 8.4-1</a>,
is a possible curve. Since <span class="i">F</span> and
<span class="i">m</span> are both positive quantities, the slope
<span class="i">dV</span>/<span class="i">dt</span> is bounded between 0
(for <span class="i">F</span> = 0) to infinity (for instantaneous
burning).

We will assume the initial value of υ<sub>0</sub> and
<span class="i">θ</span><sub>0</sub> to be fixed and, that the optimum
thrust attitude variation indicated by Eq. 8.4–2 is to be followed. The
integral to be maximized is from Eq. 8.3–5,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1374.jpg](images/e9780486140520_i1374.jpg)

</div>

<div class="caption">

(8.4–4)

</div>

</div>

and since the optimum thrust attitude is to be followed, all of the
variations have been considered in the previous problem except
<span class="i">δV</span>, which requires us to consider only the first
term of this integral.

To determine the terms of Eq. C–9, we need the following:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1375.jpg](images/e9780486140520_i1375.jpg)

</div>

</div>

and since <span class="i">δV</span> at <span class="i">t</span> = 0 and
<span class="i">t</span> = <span class="i">T</span> is zero, we obtain
the variation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1376.jpg](images/e9780486140520_i1376.jpg)

</div>

<div class="caption">

(8.4–5)

</div>

</div>

From Eqs. 8.4–5 and 8.4–2 we have

<div class="blocktext">

<span class="i">λ</span><sub>1</sub> = — tan <span class="i">φ</span>
=–tan <span class="i">φ</span><sub>0</sub> +
<span class="i">C</span><sub>2</sub><span class="i">t</span>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1377.jpg](images/e9780486140520_i1377.jpg)

</div>

</div>

from which

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1378.jpg](images/e9780486140520_i1378.jpg)

</div>

<div class="caption">

(8.4–6)

</div>

</div>

It is evident here that the integrand

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1379.jpg](images/e9780486140520_i1379.jpg)

</div>

<div class="caption">

(8.4–7)

</div>

</div>

can be positive, negative, or vary from plus to minus as t varies from 0
to <span class="i">T</span>, so that, for the integral
<span class="i">δU</span> to be zero, the function
<span class="i">V</span>(<span class="i">t</span>) must be a
discontinuous function of time (i.e., the fuel must be burned
instantaneously). We will consider three possible cases:

1\. If Φ is always positive, all of the propellant must be burned
instantaneously at the beginning, and the optimum program for
<span class="i">V</span> is the heavy discontinuous curve of
<a href="#e9780486140520_c08.html#int_130"
id="e9780486140520_c08.html_ref_int_130" class="ref_int">Fig. 8.4-2</a>.
For <span class="i">V</span>(<span class="i">t</span>) to be optimum,
<span class="i">δU</span> must be negative for any variation of
<span class="i">V</span> from the optimum. For instance, any variation
δV from the optimum curve of
<a href="#e9780486140520_c08.html#int_130" class="ref_int">Fig.
8.4-2</a>, such as the dotted curve, must be negative, which means that
<span class="i">δU</span> would be negative. A positive variation
<span class="i">δV</span> is not possible from the optimum curve shown,
since <span class="i">V</span><sub><span class="i">k</span></sub> is the
maximum available rocket thrust velocity fixed by the specific impulse
and the mass ratio. These arguments, therefore, establish the optimum
program for the propellant utilization corresponding to positive Φ to be
that of instantaneous burning at <span class="i">t</span> = 0.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1380.jpg](images/e9780486140520_i1380.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_130"
id="e9780486140520_c08.html_int_130" class="label_int"><span
class="b">Fig. 8.4-2</span></a><span class="b">.</span> Instantaneous
burning at <span class="i">t</span> = 0.

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1381.jpg](images/e9780486140520_i1381.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_131"
id="e9780486140520_c08.html_int_131" class="label_int"><span
class="b">Fig. 8.4-3</span></a><span class="b">.</span> Instantaneous
burning at <span class="i">t</span> = <span class="i">T</span>.

</div>

</div>

2\. If Φ is negative, the optimum curve for V(t) must be as shown in
<a href="#e9780486140520_c08.html#int_131"
id="e9780486140520_c08.html_ref_int_131" class="ref_int">Fig. 8.4-3</a>,
which implies instantaneous burning at <span class="i">t</span> =
<span class="i">T</span>. Any variation <span class="i">δV</span> from
this curve would be positive, which would result in a negative
<span class="i">δU</span> or a smaller value of
<span class="i">U</span>.

3\. If Φ changes sign from plus to minus, the optimum curve for
<span class="i">V</span> must appear as in
<a href="#e9780486140520_c08.html#int_132"
id="e9780486140520_c08.html_ref_int_132" class="ref_int">Fig. 8.4-4</a>,
and part of the fuel must be burned instantaneously at
<span class="i">t</span> = 0, and the remainder at
<span class="i">t</span> = <span class="i">T</span>. Again, any varied
curve which has zero or positive slope is allowable, and if a positive
<span class="i">δU</span> cannot be produced, the discontinuous curve of
<a href="#e9780486140520_c08.html#int_132" class="ref_int">Fig.
8.4-4</a> must stand as the optimum curve.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1382.jpg](images/e9780486140520_i1382.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_132"
id="e9780486140520_c08.html_int_132" class="label_int"><span
class="b">Fig. 8.4-4</span></a><span class="b">.</span> Instantaneous
burning at <span class="i">t</span> = 0 and <span class="i">t</span> =
<span class="i">T</span>.

</div>

</div>

<span class="b">PROBLEMS</span>

1.  For a specified program of fuel utilization,
    <span class="i">F</span>/<span class="i">m</span> is a known
    function of time which allows no variation in the quantity
    <span class="i">F</span>/<span class="i">m</span>. Assume now that
    both the initial velocity υ<sub>0</sub> and its inclination
    <span class="i">θ</span><sub>0</sub>, to be specified, and show that
    the optimum program for the thrust attitude
    <span class="i">φ</span>(<span class="i">t</span>) is
    <div class="blocktext">

    tan <span class="i">φ</span> = tan
    <span class="i">φ</span><sub>0</sub> −
    <span class="i">C</span><sub>2</sub><span class="i">t</span>

    </div>
2.  Show that, if a body is projected upwards with an initial velocity
    at an angle <span class="i">θ</span><sub>0</sub>, the tangent to the
    flight path will be
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1383.jpg](images/e9780486140520_i1383.jpg)

    </div>

    </div>

    where <span class="i">T</span> = time for maximum height.
3.  For the case <span class="i">φ</span><sub>0</sub> =
    <span class="i">θ</span><sub>0</sub>, show that Φ in Eq. 8.4–7 is
    always positive, and that for optimum utilization of the propellant
    all of the fuel must be burned instantaneously at the beginning.
4.  Assuming that υ<sub>0</sub> is zero, and all of the fuel is burned
    at the initial instant, determine the time <span class="i">T</span>
    at which maximum horizontal velocity is attained at height
    <span class="i">Y</span>.
5.  Determine the time required to deliver a satellite to a height
    <span class="i">Y</span> = 300 miles with a horizontal velocity of
    <span class="i">V</span> = 22,000 ft/sec.
6.  In Prob. 4, show that the initial thrust attitude should be sin
    <span class="i">φ</span><sub>0</sub> = (1/
    <span class="i">V</span><sub><span class="i">k</span></sub>) x
    <span class="imageinline">![e9780486140520_i1384.jpg](images/e9780486140520_i1384.jpg)</span>
    , and that
    <span class="i">V</span><sub><span class="i">k</span></sub> must be
    greater than the velocity necessary for projecting a body vertically
    upwards to a height <span class="i">Y</span>.
7.  In Prob. 5, determine the initial angle
    <span class="i">φ</span><sub>0</sub> and the total rocket velocity
    <span class="i">V</span><sub><span class="i">k</span></sub>.
8.  For the case where the variation of Φ is from positive to negative,
    discuss how you would find <span class="i">V</span><sub>1</sub> or
    the portion of the fuel to be burned at the initial instant.
9.  Determine the optimum fuel utilization program to achieve maximum
    height for a rocket shot vertically.
10. Determine the optimum fuel utilization program for maximum height of
    a two–stage rocket of equal stages.
11. Discuss the problem of obtaining the greatest altitude for a
    specified horizontal velocity.
12. Discuss the problem of minimum propellant consumption for a
    specified horizontal velocity and altitude.

</div>

<div class="section1">

<span id="e9780486140520_c08.html_title112"></span>

# <span class="b">8.5 Gravity Turn</span><sup>[1](#e9780486140520_app02.html#end_en1)</sup>

In the previous section it was shown that the optimum thrust attitude
for placing a satellite into orbit is given by the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1385.jpg](images/e9780486140520_i1385.jpg)

</div>

<div class="caption">

(8.5–1)

</div>

</div>

Likewise, the optimum thrust attitude for maximum range (ballistic
missile) can be shown to be <span class="i">φ</span> = constant. These
conditions may be satisfactory for a rocket traveling in vacuum but,
owing to the large angle of attack (<span class="i">φ</span> −
<span class="i">θ</span>) which results from such trajectories, they are
not feasible through the atmosphere. Thus for flight through the
atmosphere, a trajectory known as <span class="i">gravity turn</span> is
generally used. In a gravity turn the thrust vector is kept parallel to
the velocity vector at all times, starting with some nonvertical initial
velocity υ<sub>0</sub>. Thus the gravity turn is also one of zero angle
of attack or zero lift.

It is convenient here to measure the angle made by the velocity vector
from the vertical, as shown in
<a href="#e9780486140520_c08.html#int_133"
id="e9780486140520_c08.html_ref_int_133" class="ref_int">Fig. 8.5-1</a>.
Again assuming zero aerodynamic drag and constant gravity field, we
write equations for the forces in the tangential and normal directions
to the trajectory.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1386.jpg](images/e9780486140520_i1386.jpg)

</div>

</div>

<div class="blocktext">

(8.5–1)

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1387.jpg](images/e9780486140520_i1387.jpg)

</div>

<div class="caption">

(8.5–2)

</div>

</div>

These equations are nonlinear and no analytical solution is known when
<span class="i">F</span>/<span class="i">mg</span> varies with time. A
reasonable assumption for
<span class="i">F</span>/<span class="i">mg</span> is
<span class="i">F</span> = constant, and <span class="i">m</span> =
<span class="i">m</span><sub>0</sub> −
<span class="i">m</span>′<span class="i">t</span>.

When <span class="i">F</span>/<span class="i">mg</span> is a constant,
these nonlinear equations can be solved analytically. For
<span class="i">F</span>/<span class="i">mg</span> to be constant, the
thrust <span class="i">F</span> must decrease with time to conform to
the decreasing mass. If
<span class="i">F</span>/<span class="i">mg</span> is a varying function
of time, we can assume
<span class="i">F</span>/<span class="i">mg</span> to be constant over
short intervals of time, and we can carry out a step–by–step numerical
integration, using the analytical solution over each interval. It is
evident, then, that the analytical solution for constant
<span class="i">F</span>/<span class="i">mg</span> is of practical
interest, and we consider its development as follows :

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1388.jpg](images/e9780486140520_i1388.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c08.html#ref_int_133"
id="e9780486140520_c08.html_int_133" class="label_int"><span
class="b">Fig. 8.5-1</span></a><span class="b">.</span> Gravity turn
trajectory.

</div>

</div>

Let <span class="i">F</span>/<span class="i">mg</span> =
<span class="i">n</span> over a short increment of the flight path. We
introduce

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1389.jpg](images/e9780486140520_i1389.jpg)

</div>

<div class="caption">

(8.5–3)

</div>

</div>

Then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1390.jpg](images/e9780486140520_i1390.jpg)

</div>

</div>

and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1391.jpg](images/e9780486140520_i1391.jpg)

</div>

</div>

Differentiating Eq. 8.5–3,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1392.jpg](images/e9780486140520_i1392.jpg)

</div>

</div>

Therefore,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1393.jpg](images/e9780486140520_i1393.jpg)

</div>

</div>

By substitution into Eqs. 8.5–1 and 8.5–2, they become,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1394.jpg](images/e9780486140520_i1394.jpg)

</div>

<div class="caption">

(8.5–4)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1395.jpg](images/e9780486140520_i1395.jpg)

</div>

<div class="caption">

(8.5–5)

</div>

</div>

Eliminating <span class="i">dt</span> between the above equations,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1396.jpg](images/e9780486140520_i1396.jpg)

</div>

<div class="caption">

(8.5–6)

</div>

</div>

Integrating, we have (see
Peirce<sup><a href="#e9780486140520_ftn01.html#ftn_fn15"
id="e9780486140520_c08.html_ref_ftn_fn15">o</a></sup> nos. 53 and 55),

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1397.jpg](images/e9780486140520_i1397.jpg)

</div>

</div>

or

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1398.jpg](images/e9780486140520_i1398.jpg)

</div>

<div class="caption">

(8.5–7)

</div>

</div>

The constant <span class="i">C</span> can be evaluated from initial
conditions to be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1399.jpg](images/e9780486140520_i1399.jpg)

</div>

<div class="caption">

(8.5–8)

</div>

</div>

Substituting Eq. 8.5–7 into 8.5–5 and integrating,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1400.jpg](images/e9780486140520_i1400.jpg)

</div>

<div class="caption">

(8.5–9)

</div>

</div>

Equation 8.5–9 gives t as a function of z = tan ½ψ for any initial
condition C. Thus, conversely, <span class="i">ψ</span> is known in
terms of <span class="i">t</span> and <span class="i">C</span>. Equation
8.5–7 gives <span class="i">v</span> as a function of
<span class="i">z</span> and <span class="i">C</span>, so that
<span class="i">v</span> is also known in terms of
<span class="i">t</span> and <span class="i">C</span>. Thus Eqs. 8.5–7,
8.5–8, and 8.5–9 represent the solution for the gravity turn trajectory
when the thrust–to–weight ratio
<span class="i">F</span>/<span class="i">mg</span> is a constant n.

To apply these equations for a varying
<span class="i">F</span>/<span class="i">mg</span>, we start with the
initial conditions expressed by Eqs. 8.5–3 and 8.5–8, and
<span class="i">F</span>/<span class="i">mg</span> =
<span class="i">n</span> at <span class="i">t</span> = 0. Choosing a
value of <span class="i">ψ</span> slightly greater than
<span class="i">ψ</span><sub>0</sub>, determine v from Eq. 8.5–7 and ∆t
from Eq. 8.5–9. The increment in the displacement is, then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1401.jpg](images/e9780486140520_i1401.jpg)

</div>

</div>

The procedure can now be repeated with the values at the new point as
initial condition.

<span class="b">PROBLEMS</span>

1.  By reversing the force <span class="i">F</span>, show that the
    motion of a body hurled into a resisting medium can be solved by the
    techniques of this section.
2.  If <span class="i">F</span>/<span class="i">mg</span> is constant
    throughout flight, what is the effect of changing the initial angle
    <span class="i">ψ</span><sub>0</sub> on; (<span class="i">a</span>)
    the final velocity; (<span class="i">b</span>) the time of flight.
3.  For constant value of
    <span class="i">F</span>/<span class="i">mg</span>, the velocity and
    its inclination ψ were observed at a given time. If the initial
    angle is doubled, how would the above quantities differ at the same
    time.
4.  From Eqs. 8.5–1 and 8.5–2 derive the ballistic equation of a rocket
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1402.jpg](images/e9780486140520_i1402.jpg)

    </div>

    </div>

    where D is the aerodynamic drag. <span class="i">Hint</span>: The
    normal and tangential accelerations can be written as
    <div class="blocktext">

    <span class="imageinline">![e9780486140520_i1403.jpg](images/e9780486140520_i1403.jpg)</span>
    = υ<sup>2</sup>/<span class="i">R</span>

    </div>

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1404.jpg](images/e9780486140520_i1404.jpg)

    </div>

    </div>

    where <span class="i">R</span> is the radius of curvature of the
    trajectory, and <span class="i">ds</span> = <span class="i">R
    dψ</span>.

</div>

<div class="section1">

<span id="e9780486140520_c08.html_title113"></span>

# <span class="b">REFERENCES</span>

1.  Culler, G. J., and B. D. Fried, “Universal Gravity Turn
    Trajectories,” <span class="i">J. Appl. Physics,</span>
    <span class="b">28</span>, No. 6 (June 1957), 672–676
2.  Hall, H. H., and E. D. Zambelli, “On the Optimization of Multistage
    Rockets,” <span class="i">Jet Propulsion,</span>
    <span class="b">28</span> (July 1958), 463–465.
3.  Okhotsimskii, <span class="b">D</span>. E., and T. M. Eneev, “Some
    Variation Problems Connected with the Launching of Artificial
    Satellites of the Earth,” <span class="i">J. British Interplanetary
    Soc.,</span> <span class="b">16</span> (5), (Jan.–Feb. 1958),
    263–294.
4.  Bellman, <span class="b">R</span>. and Dreyfus,
    <span class="b">S</span>., “An Application of Dynamic Programming of
    the Determination of Optimal Satellite Trajectories”
    <span class="i">J. British Interplanetary Society,</span> Vol. 16
    No. 3–4 (1959), p. 78–83.
5.  Leitmann, G., “Optimization Techniques with Applications to
    Aerospace Systems” Academic Press, New York, 1962.

</div>

</div>

<span id="e9780486140520_c09.html"></span>

<div class="chapter">

<span id="e9780486140520_c09.html_title114"></span>

# <span class="b">CHAPTER 9</span>

# <span class="b">Generalized Theories of Mechanics</span>

<div class="section1">

<span id="e9780486140520_c09.html_title115"></span>

# <span class="b">9.1 Introduction</span>

Experience indicates that our learning process consists of first
assimilating simple bits of information and, second, of comprehending
the relationships between the various bits of information. As a result
there begins to emerge an over–all pattern of behavior predictable from
a theory. Simple theories are necessary for the beginner, in spite of
the fact that they are limited in scope and incapable of extension
beyond the bounds for which they are intended.

Beyond this stage must be a more general theory which encompasses and
unites all special theories into a harmonious understanding. Such a
generalized theory of mechanics was developed by Hamilton and Lagrange.
It encompasses all of classical mechanics, and an understanding of this
important work is an essential part of advanced dynamics.

Preliminary to the discussion of the generalized theories, it is
necessary to have clearly in mind the basic concepts of coordinates and
their classification.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title116"></span>

# <span class="b">9.2 System with Constraints</span>

The degrees of freedom of a body correspond to the minimum number of
independent coordinates required to define its position. For a particle
free to move in space, three coordinates are necessary to define its
position. They may be rectangular coordinates <span class="i">x</span>,
<span class="i">y</span>, <span class="i">z</span>, spherical
coordinates <span class="i">r</span>, <span class="i">θ</span>,
<span class="i">φ</span>, or some other system of coordinates, but three
are necessary, and each coordinate may be varied independently. We say
then that the free particle has three degrees of freedom.

If, next, the particle is constrained to move on a specified surface,
only two coordinates are necessary to define its position, and we say
that it has two degrees of freedom. For instance, the latitude and
longitude completely define a position of a particle on the earth’s
surface. If the particle is further constrained to move along a
specified line on the surface, one coordinate—such as the distance along
this line—will define its position, and such a particle will have one
degree of freedom. Here we have placed two constraints on the particle,
one to restrict it to a surface, and another to confine the motion along
some line on the surface. In each case the three degrees of freedom of a
free particle have been reduced by the number of constraints imposed on
the particle.

The constraints of a system can be expressed analytically in terms of
its geometry. For example, a particle a distance l from the fixed end of
a string is constrained to move on a spherical surface, the equation of
which is,

<div class="blocktext">

<span class="i">x</span><sup>2</sup> +
<span class="i">y</span><sup>2</sup> +
<span class="i">z</span><sup>2</sup> =
<span class="i">l</span><sup>2</sup>

</div>

In the general case, the equation of constraint restricting a particle
to any surface is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1405.jpg](images/e9780486140520_i1405.jpg)

</div>

<div class="caption">

(9.2–1)

</div>

</div>

When the particle is constrained to move along a curve in space, the
curve can be considered to be the intersection of two surfaces, so that
the two constraint equations to be satisfied are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1406.jpg](images/e9780486140520_i1406.jpg)

</div>

<div class="caption">

(9.2–2)

</div>

</div>

An elementary example of two constraints is illustrated by the simple
pendulum whose circular path in the vertical plane is the intersection
of a sphere and a vertical plane through its center. The constraint
equation, <span class="i">x</span><sup>2</sup> +
<span class="i">y</span><sup>2</sup> =
<span class="i">l</span><sup>2</sup>, is actually the result of two
equations,

<div class="tableau">

|  |  |
|:---|---:|
| Sphere | <span class="i">x</span><sup>2</sup> + <span class="i">y</span><sup>2</sup> + <span class="i">z</span><sup>2</sup> = <span class="i">l</span><sup>2</sup> |
| Plane | <span class="i">z</span> = 0 |

</div>

with the coordinates oriented as shown in
<a href="#e9780486140520_c09.html#int_134"
id="e9780486140520_c09.html_ref_int_134" class="ref_int">Fig. 9.2-1</a>.

Sometimes a constraint equation will also depend on time. For instance,
if the support point of the simple pendulum is given a motion
x<sub>0</sub>(t), the constraint equation would have to be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1408.jpg](images/e9780486140520_i1408.jpg)

</div>

</div>

It is evident, then, that for a time–dependent constraint, the equation
may be written in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1409.jpg](images/e9780486140520_i1409.jpg)

</div>

<div class="caption">

(9.2–3)

</div>

</div>

Constraints may also be imposed between particles; e.g., two particles
whose distance between them is always constant. The first particle has
three degrees of freedom. The second particle has two degrees of
freedom. Thus we have 3 + 2 = 5 degrees of freedom for the two particles
bound to each other a given distance apart. Actually two free particles
would have six degrees of freedom; however a constraint has been
introduced, specifying the distance between them, so that the degrees of
freedom have been reduced by one.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1410.jpg](images/e9780486140520_i1410.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_134"
id="e9780486140520_c09.html_int_134" class="label_int"><span
class="b">Fig. 9.2-1</span></a><span class="b">.</span> Intersection of
the <span class="i">x</span>, <span class="i">y</span> plane and a
sphere of radius <span class="i">l</span> defines the path of the simple
pendulum mass.

</div>

</div>

The position of a rigid body is known if we know the position of three
noncollinear points on it. The three points, if free, would have nine
degrees of freedom, but since there are three rigid constraints between
them, a rigid body has six degrees of freedom. Another way of arriving
at the same result is to choose the first point arbitrarily, in which
case it will have three degrees of freedom. The second point must move
in a sphere about the first, so it has two degrees of freedom. The third
point must now move in a circular line about 1 and 2 as axis, which adds
another degree of freedom, making a total of six degrees of freedom.

The general rule for <span class="i">N</span> particles can be stated as
follows. If <span class="i">N</span> particles have
<span class="i">c</span> constraints restricting their freedom, the
number of degrees of freedom <span class="i">n</span> will be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1411.jpg](images/e9780486140520_i1411.jpg)

</div>

<div class="caption">

(9.2–4)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title117"></span>

# <span class="b">9.3 Generalized Coordinates</span>

A simple pendulum is defined as a point mass on the end of a weightless,
inextensible string, which is made to move in a vertical plane, as shown
in <a href="#e9780486140520_c09.html#int_135"
id="e9780486140520_c09.html_ref_int_135" class="ref_int">Fig. 9.3-1</a>.
The point mass must move on a circular line in the plane, and has one
degree of freedom. The position of the mass may be specified by
rectangular coordinates <span class="i">x</span>,
<span class="i">y</span>, which are not independent but subject to the
constraint equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1412.jpg](images/e9780486140520_i1412.jpg)

</div>

<div class="caption">

(9.3–1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1413.jpg](images/e9780486140520_i1413.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_135"
id="e9780486140520_c09.html_int_135" class="label_int"><span
class="b">Fig. 9.3-1</span></a><span class="b">.</span> Simple pendulum.

</div>

</div>

It is simpler, however, to specify its position by the angle
<span class="i">θ,</span> which is independent and free of any
constraint equation. Such independent coordinates are called
<span class="i">generalized coordinates,</span> and the number of such
coordinates corresponds to the degrees of freedom of the system.

Consider next the double pendulum of
<a href="#e9780486140520_c09.html#int_136"
id="e9780486140520_c09.html_ref_int_136" class="ref_int">Fig. 9.3-2</a>,
which is a system of two degrees of freedom. If the position of each
mass is to be defined in terms of rectangular coordinates, four
coordinates, <span class="i">x</span><sub>1</sub>,
<span class="i">y</span><sub>1</sub>,
<span class="i">x</span><sub>2</sub>,
<span class="i">y</span><sub>2</sub>, would be necessary. There are
however, two constraint equations between the coordinates,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1414.jpg](images/e9780486140520_i1414.jpg)

</div>

<div class="caption">

(9.3–2)

</div>

</div>

and the number of coordinates minus the number of constraints again
agree with the degrees of freedom of the system. Any two of the four
rectangular coordinates can be considered independent, but the remaining
two must be related by the above constraint equations.

The double pendulum can also be defined by two angles,
<span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub>. Each <span class="i">θ</span> can
be varied independently and, therefore, no constraints exist between
them. <span class="i">θ</span><sub>1</sub> and
<span class="i">θ</span><sub>2</sub> are thus generalized coordinates
for the double pendulum.

For a system of <span class="i">n</span> degrees of freedom, there are
<span class="i">n</span> generalized coordinates,
<span class="i">q</span><sub>1</sub>,
<span class="i">q</span><sub>2</sub>,
<span class="i">q</span><sub>3</sub>,
<span class="i">q</span><sub>4</sub>, . . . ,
<span class="i">q</span><sub><span class="i">n</span></sub><span class="i">.</span>
They are independent coordinates free from any constraints. They are not
necessarily lengths or angles, but can be any independent set of
quantities which describe completely the motion of the system.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1415.jpg](images/e9780486140520_i1415.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_136"
id="e9780486140520_c09.html_int_136" class="label_int"><span
class="b">Fig. 9.3-2</span></a><span class="b">.</span> Double pendulum.

</div>

</div>

It is always possible to relate the rectangular coordinates as some
function of the generalized coordinates. For instance, in the case of
the double pendulum, the rectangular coordinates expressed in terms of
the generalized coordinates <span class="i">q</span><sub>1</sub> =
<span class="i">θ</span><sub>1</sub> and
<span class="i">q</span><sub>2</sub> =
<span class="i">θ</span><sub>2</sub> are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1416.jpg](images/e9780486140520_i1416.jpg)

</div>

<div class="caption">

(9.3–3)

</div>

</div>

In the more general case, the relationships between the various position
coordinates <span class="i">x</span>, <span class="i">y</span>,
<span class="i">z</span> and the generalized coordinates can be
expressed by the functional equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1417.jpg](images/e9780486140520_i1417.jpg)

</div>

<div class="caption">

(9.3–4)

</div>

</div>

where <span class="i">n</span> is the number of degrees of freedom of
the system.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title118"></span>

# <span class="b">9.4 Holonomic and Nonholonomic System</span>

When the constraints are expressible as functions of the coordinates or
coordinates and time, the system is said to be holonomic. Sometimes the
constraints are expressed in terms of the velocities; however, if such
expressions are integrable, we obtain the constraint equations as
function of the coordinates or coordinates and time, so again we have a
holonomic system.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1418.jpg](images/e9780486140520_i1418.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_137"
id="e9780486140520_c09.html_int_137" class="label_int"><span
class="b">Fig. 9.4-1</span></a><span class="b">.</span> Example of
holomonic system.

</div>

</div>

As an example, consider a wheel rolling without slipping along a
specified straight line, as shown in
<a href="#e9780486140520_c09.html#int_137"
id="e9780486140520_c09.html_ref_int_137" class="ref_int">Fig. 9.4-1</a>.
The velocity of the center is <span class="i">x</span> =
<span class="i">rφ</span>, which can be integrated to
<span class="i">x</span> = <span class="i">rφ</span> +
<span class="i">c</span>. The system is hence holonomic.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1419.jpg](images/e9780486140520_i1419.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_138"
id="e9780486140520_c09.html_int_138" class="label_int"><span
class="b">Fig. 9.4-2</span></a><span class="b">.</span> Example of
nonholonomic system.

</div>

</div>

If the same wheel rolls without slipping on a plane, and is allowed to
pivot about a vertical axis through the point of contact, as shown in
<a href="#e9780486140520_c09.html#int_138"
id="e9780486140520_c09.html_ref_int_138" class="ref_int">Fig. 9.4-2</a>,
the relationship between the velocities will be found to be
nonintegrable, and hence the system must be classified as nonholonomic.
We have, for instance, the equations for the velocity normal and
parallel to the path as,

<div class="blocktext">

<span class="i">ẋ</span> sin<span class="i">θ</span> −
<span class="i">ẏ</span> cos <span class="i">θ</span> = 0  
<span class="i">ẋ</span> cos <span class="i">θ</span> +
<span class="i">ẏ</span> sin <span class="i">θ</span> =
<span class="imageinline">![e9780486140520_i1420.jpg](images/e9780486140520_i1420.jpg)</span>

</div>

and it is not possible to integrate these expressions to obtain
relationships between the coordinates. It is possible, for instance, to
roll the wheel to another point with a different value of
<span class="i">x</span>, but with the other coordinates
<span class="i">y</span>, <span class="i">θ</span>, and
<span class="i">φ</span> unchanged. It is evident, then, that
<span class="i">x</span> cannot be functionally related to the remaining
coordinates. Each of the other coordinates can be singled out in the
same manner, so that there can be no unique relationship existing
between them. We have only a relationship between the infinitesimals
which can be written as

<div class="blocktext">

sin <span class="i">θ dx</span> − cos <span class="i">θ</span>
d<span class="i">y</span> = 0  
cos <span class="i">θ dx</span> + sin <span class="i">θ dy − r dφ</span>
= 0

</div>

In a holonomic system, the constraint equations are in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1421.jpg](images/e9780486140520_i1421.jpg)

</div>

<div class="caption">

(9.4–1)

</div>

</div>

Moreover, the differential of the constraint equation is exact and
expressible as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1422.jpg](images/e9780486140520_i1422.jpg)

</div>

<div class="caption">

(9.4–2)

</div>

</div>

It is also possible in the holonomic system to reduce the number of the
dependent variables
<span class="i">r</span><sub><span class="i">i</span></sub> by the
number of constraint equations to the number of the degrees of freedom
of the system. These are then expressible in terms of the
<span class="i">n</span> generalized coordinates, equal to the number of
degrees of freedom of the system, and independent of each other. Thus,
provided we are able to find the <span class="i">n</span> generalized
coordinates of the system, the problem reduces to that of solving
<span class="i">n</span> independent equations in
<span class="i">q</span><sub><span class="i">i</span></sub>, without
concern of the constraints of the system.

In the nonholonomic system, the constraints are not expressible in terms
of the coordinates or coordinates and time, as in Eq. 9.4–1. The
constraint equations are available only as relationships between the
infinitesimals,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1423.jpg](images/e9780486140520_i1423.jpg)

</div>

<div class="caption">

(9.4–3)

</div>

</div>

which are nonintegrable. Thus, if we transform the dependent variables
<span class="i">r</span><sub><span class="i">i</span></sub> into the
equation

<div class="blocktext">

<span class="i">r</span><sub><span class="i">i</span></sub> =
<span class="i">r</span><sub><span class="i">i</span></sub>(<span class="i">q</span><sub>1</sub>,
<span class="i">q</span><sub>2</sub>, . . . , <span class="i">t</span>)

</div>

we would find that not all the q are independent. Special procedures to
be used under these conditions are discussed in Sec. 9.9.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title119"></span>

# <span class="b">9.5 Principle of Virtual Work</span>

A virtual displacement <span class="i">δx, δθ, δq,</span> etc., is an
infinitesimal change in the coordinate, which may be conceived in any
manner irrespective of the time <span class="i">t.</span> It may or may
not coincide with the actual displacement, <span class="i">dx, dθ,
dq.</span>

In the case of constrained motion, the virtual displacement must be
compatible with the constraints. For instance, if a particle is
constrained to move on a surface, the virtual displacement must be
confined to the surface. If the constraint equation for this case is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1424.jpg](images/e9780486140520_i1424.jpg)

</div>

<div class="caption">

(9.5–1)

</div>

</div>

the virtual displacement must satisfy the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1425.jpg](images/e9780486140520_i1425.jpg)

</div>

<div class="caption">

(9.5–2)

</div>

</div>

For a nonholonomic constraint, the restriction is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1426.jpg](images/e9780486140520_i1426.jpg)

</div>

<div class="caption">

(9.5–3)

</div>

</div>

Since virtual displacements are made irrespective of time, the above
expression must be independent of time <span class="i">t</span>.

Consider a particle acted upon by several forces. If the particle is in
equilibrium, the resultant <span class="b">R</span> of the forces must
vanish, and the work done by the forces in a virtual displacement
<span class="i">δ</span><span class="b">r</span> is zero.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1427.jpg](images/e9780486140520_i1427.jpg)

</div>

<div class="caption">

(9.5–4)

</div>

</div>

If the particle is constrained, the force <span class="b">R</span> may
be separated into an applied force <span class="b">F</span> and a
constraint force <span class="b">f.</span> For equilibrium,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1428.jpg](images/e9780486140520_i1428.jpg)

</div>

<div class="caption">

(9.5–5)

</div>

</div>

and the applied force is balanced by the constraint force. The virtual
work is then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1429.jpg](images/e9780486140520_i1429.jpg)

</div>

<div class="caption">

(9.5–6)

</div>

</div>

But now the virtual displacement
<span class="i">δ</span><span class="b">r</span> must be consistent with
the constraint, which requires that <span class="b">f ·</span>
<span class="i">δ</span><span class="b">r</span> = 0. For instance, a
particle made to move along a smooth wire would have a constraint force
of the wire acting normal to the wire and hence to the virtual
displacement. Thus the constraint force cannot contribute to the work,
and we are left with the result,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1430.jpg](images/e9780486140520_i1430.jpg)

</div>

<div class="caption">

(9.5–7)

</div>

</div>

which states that, if the particle is in equilibrium, the work done by
the applied forces due to a virtual displacement is zero.

For a system of particles in equilibrium, the sum of the forces acting
on each particle must vanish. The virtual work of the system is the sum
of the virtual work done on each particle, which must also be zero.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1431.jpg](images/e9780486140520_i1431.jpg)

</div>

<div class="caption">

(9.5–8)

</div>

</div>

The force <span class="b">R</span><sub><span class="i">i</span></sub>,
can again be separated into the applied force
<span class="b">F</span><sub><span class="i">i</span></sub> and the
force of constraint
<span class="b">f</span><sub><span class="i">i</span></sub>, and since
<span class="imageinline">![e9780486140520_i1432.jpg](images/e9780486140520_i1432.jpg)</span><span class="b">f</span><sub><span class="i">i</span></sub>
·
<span class="i">δ</span><span class="b">r</span><sub><span class="i">i</span></sub>
= 0, we obtain the virtual work for the system of particles to be,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1433.jpg](images/e9780486140520_i1433.jpg)

</div>

<div class="caption">

(9.5–9)

</div>

</div>

where <span class="b">F</span><sub><span class="i">i</span></sub> and
<span class="i">δ</span><span class="b">r</span><sub><span class="i">i</span></sub>
are the applied force and the virtual displacement associated with
particle <span class="i">i</span>. Thus the principle of virtual work as
presented by Jean Bernoulli (1717) can be stated as follows: If a system
of forces are in equilibrium, the work done by the applied forces in a
virtual displacement compatible with the constraints is zero.

For a rigid body or a system of interconnected rigid bodies, internal
forces, which always appear in equal and opposite pairs, must do no
work. Thus, with the principle of virtual work, we can ignore all
internal forces and reaction forces of constraints, and equate the
virtual work of the applied forces to zero.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title120"></span>

# <span class="b">9.6 D’Alembert’s Principle</span>

The principle of virtual work, established for the case of static
equilibrium, can be extended to dynamics by a reasoning advanced by
D’Alembert (1743). We will let <span class="b">p</span> be the momentum
of a particle in the system, and separate the forces acting on it into
an applied force F and a constraint force <span class="b">f</span>. The
equation of motion of the particle can then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1434.jpg](images/e9780486140520_i1434.jpg)

</div>

<div class="caption">

(9.6–1)

</div>

</div>

which states that the forces are in equilibrium with the kinetic
reaction–<span class="b">ṗ</span>. The quantity
<span class="b">–ṗ</span> is sometimes referred to as the “reverse
effective force” because the force effective in producing the motion is
equal to <span class="b">ṗ</span>, and, if such a force is applied in
the reverse sense, the motion could be nullified to produce a state of
static equilibrium. As before, the virtual work of the constraint force
is zero since f and δr are mutually perpendicular. The virtual work of
the forces acting on the particle is, then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1435.jpg](images/e9780486140520_i1435.jpg)

</div>

<div class="caption">

(9.6–2)

</div>

</div>

and for the system of <span class="i">N</span> particles, we sum to
obtain the result

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1436.jpg](images/e9780486140520_i1436.jpg)

</div>

<div class="caption">

(9.6–3)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A constraint is scleronomic if time–independent, and it is rheonomic
    if time–dependent. If a particle of mass <span class="i">m</span> is
    free to slide on a smooth hoop of radius <span class="i">r</span>,
    which is rotated with constant speed Ω about a verticle diameter,
    discuss the degrees of freedom and the type of constraint,
    holonomic, nonholonomic, scleronomic, or rheonomic.

2.  The vertical diameter of a wheel rolling on a rough horizontal floor
    is rotated at a constant rate to form a circular path for the
    contact point. Is the constraint holonomic or nonholonomic?

3.  A sphere of radius <span class="i">a</span>, rolling on a rough,
    horizontal plane is a nonholonomic system. Attach body axes
    <span class="i">x, y, z</span> to the center of the sphere, defining
    their position by the Euler angles <span class="i">θ, ψ, ϕ.</span>
    Show that the angular velocity of the sphere with respect to fixed
    axes <span class="i">X, Y, Z</span> is <span class="i">ω</span> =
    <span class="i">ω</span><sub><span class="i">x</span></sub><span class="b">I</span> +
    <span class="i">ω</span><sub><span class="i">Y</span></sub><span class="b">J</span> +
    <span class="i">ω</span><sub>2</sub><span class="b">K</span> where,
    <span class="imageinline">![e9780486140520_i1437.jpg](images/e9780486140520_i1437.jpg)</span>
    <span class="imageinline">![e9780486140520_i1438.jpg](images/e9780486140520_i1438.jpg)</span>
    <span class="imageinline">![e9780486140520_i1439.jpg](images/e9780486140520_i1439.jpg)</span>

    Show also that the constraint equation for no slipping is

    <div class="blocktext">

    V<sub>o</sub> + <span class="i">ω</span> × <span class="b">r</span>
    = 0

    </div>

    where V<sub>0</sub> is the velocity of the center of the sphere, and
    <span class="b">r</span>
    =–<span class="i">a</span><span class="b">K</span>.

4.  In Prob. 3, determine the variation of the constraint equation along
    the <span class="i">X</span> and <span class="i">Y</span> axes.

5.  Virtual work for a system of <span class="i">N</span> particles can
    be expressed by the equation
    <span class="imageinline">![e9780486140520_i1440.jpg](images/e9780486140520_i1440.jpg)</span>.
    Discuss the interpretation of this equation for a system of free
    particles versus a system of constrained particles.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title121"></span>

# <span class="b">9.7 Hamilton’s Principle</span>

The principle of virtual work together with D’Alembert’s principle was
viewed by W. R. Hamilton (1805–1865) as a basis for his variational
approach, leading to one of the most general statements of mechanics
known as the Hamilton’s Principle. It reduces the formulation of
problems in dynamics to that of the variation of a scalar integral,
irrespective of coordinates and for conservative and nonconservative
systems.

We start with N discrete mass particles, coupled by either holonomic or
nonholonomic forces of constraints, and write the virtual work equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1441.jpg](images/e9780486140520_i1441.jpg)

</div>

<div class="caption">

(9.7–1)

</div>

</div>

We recognize in this equation that
<span class="imageinline">![e9780486140520_i1442.jpg](images/e9780486140520_i1442.jpg)</span>
<span class="i"><span class="b">F</span></span><sub><span class="i">i</span></sub>
·
<span class="i">δ</span><span class="b">r</span><sub><span class="i">i</span></sub>
is the work done by the external forces in a virtual displacement, which
could include nonconservative forces.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1443.jpg](images/e9780486140520_i1443.jpg)

</div>

<div class="caption">

(9.7–2)

</div>

</div>

Relating to the first term of Eq. 9.7–1, the following differential
relationships exist:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1444.jpg](images/e9780486140520_i1444.jpg)

</div>

<div class="caption">

(9.7–3)

</div>

</div>

The first term of Eq. 9.7–1 can then be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1445.jpg](images/e9780486140520_i1445.jpg)

</div>

<div class="caption">

(9.7–4)

</div>

</div>

and Eq. 9.7–1 becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1446.jpg](images/e9780486140520_i1446.jpg)

</div>

<div class="caption">

(9.7–5)

</div>

</div>

Consider times <span class="i">t</span> = 0 and <span class="i">t</span>
= <span class="i">t</span><sub>1</sub> at which
<span class="i">δ</span><span class="b">r</span><sub><span class="i">i</span></sub>
= 0, and integrate Eq. 9.7–5:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1447.jpg](images/e9780486140520_i1447.jpg)

</div>

<div class="caption">

(9.7–6)

</div>

</div>

The left side of this equation is equal to the integrand evaluated at
the upper and lower limits:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1448.jpg](images/e9780486140520_i1448.jpg)

</div>

<div class="caption">

(9.7–7)

</div>

</div>

But since
<span class="i">δ</span><span class="b">r</span><sub><span class="i">i</span></sub>
equals zero at <span class="i">t</span> = 0 and
<span class="i">t</span><sub>1</sub>, the left side of Eq. 9.7–7 is
zero, and we arrive at the final result

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1449.jpg](images/e9780486140520_i1449.jpg)

</div>

<div class="caption">

(9.7–8)

</div>

</div>

We will review now the variational principle leading to Eq. 9.7–8. The
motion of the system defined by the time variation of the
<span class="i">N</span>
<span class="b">r</span><sub><span class="i">i</span></sub> is defined
as the dynamical path. At any time <span class="i">t</span> between
<span class="i">t</span> = 0 and <span class="i">t</span><sub>1</sub>,
the <span class="i">N</span>–valued <span class="b">r</span><sub>i</sub>
are given a virtual displacement
<span class="i">δ</span><span class="b">r</span>, thereby varying the
dynamical path under the restriction <span class="i">δt</span> = 0. In
the varied configuration, <span class="i">T</span> and
<span class="i">W</span> undergo variations <span class="i">δT</span>
and <span class="i">δW</span> due to the variation in the coordinates
and their velocities. Of all the possible variations, the dynamical path
corresponds to the one which leads to a stationary value of the integral
in Eq. 9.7–8 which is Hamilton’s principle.

When the system is conservative the work can be expressed in terms of
the potential energy in which case Eq. 9.7–8 reduces to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1450.jpg](images/e9780486140520_i1450.jpg)

</div>

<div class="caption">

(9.7–9)

</div>

</div>

Hamilton’s principle states that, if the configuration of the system at
two instants <span class="i">t</span> = 0 and
<span class="i">t</span><sub>1</sub> is known, the motion of the system
is given by the stationarity of the scalar integral. Hamilton’s
principle does not provide the solution to the dynamical problem, but
formulates the equations of motion in a general manner irrespective of
the coordinate system. It embodies both the Lagrange equation and the
theorem of conservation of energy.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title122"></span>

# <span class="b">9.8 Lagrange’s Equation (Holonomic System)</span>

For a holonomic system, the dependent–variables
<span class="b">r</span><sub><span class="i">i</span></sub> can be
expressed entirely in terms of the <span class="i">n</span>–generalized
coordinates <span class="i">q</span><sub><span class="i">k</span></sub>
and time <span class="i">t</span>, corresponding to the
<span class="i">n</span> degrees of freedom.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1451.jpg](images/e9780486140520_i1451.jpg)

</div>

<div class="caption">

(9.8–1)

</div>

</div>

The <span class="i">q</span><sub><span class="i">k</span></sub> in the
above equation are independent and no constraint equation exists between
them.

Differentiating Eq. 9.8–1, the velocity can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1452.jpg](images/e9780486140520_i1452.jpg)

</div>

<div class="caption">

(9.8–2)

</div>

</div>

By squaring and summing over all the particles of the system, the
kinetic energy becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1453.jpg](images/e9780486140520_i1453.jpg)

</div>

<div class="caption">

(9.8–3)

</div>

</div>

It is evident then that <span class="i">T</span> is a function of
<span class="i">q</span><sub><span class="i">k</span></sub>,
<span class="imageinline">![e9780486140520_i1454.jpg](images/e9780486140520_i1454.jpg)</span>,
and <span class="i">t</span>, and we may write

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1455.jpg](images/e9780486140520_i1455.jpg)

</div>

<div class="caption">

(9.8–4)

</div>

</div>

We will now consider the variation <span class="i">δT</span> in
Hamilton’s equation, holding <span class="i">t</span> fixed

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1456.jpg](images/e9780486140520_i1456.jpg)

</div>

<div class="caption">

(9.8–5)

</div>

</div>

and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1457.jpg](images/e9780486140520_i1457.jpg)

</div>

<div class="caption">

(9.8–6)

</div>

</div>

Writing the last integral in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1458.jpg](images/e9780486140520_i1458.jpg)

</div>

</div>

we integrate by parts, letting

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1459.jpg](images/e9780486140520_i1459.jpg)

</div>

</div>

Then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1460.jpg](images/e9780486140520_i1460.jpg)

</div>

</div>

and the integral becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1461.jpg](images/e9780486140520_i1461.jpg)

</div>

</div>

Since <span class="i">δq</span><sub><span class="i">i</span></sub> = 0
at <span class="i">t</span> = 0 and
<span class="i">t</span><sub>1</sub>, the first term on the right is
zero and Eq. 9.8–6 becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1462.jpg](images/e9780486140520_i1462.jpg)

</div>

<div class="caption">

(9.8–7)

</div>

</div>

Consider next the variation <span class="i">δW</span> due to the
<span class="i">m</span> forces acting on the system

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1463.jpg](images/e9780486140520_i1463.jpg)

</div>

<div class="caption">

(9.8–8)

</div>

</div>

The virtual displacement
<span class="i">δr</span><sub><span class="i">j</span></sub> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1464.jpg](images/e9780486140520_i1464.jpg)

</div>

<div class="caption">

(9.8–9)

</div>

</div>

so that <span class="i">δW</span> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1465.jpg](images/e9780486140520_i1465.jpg)

</div>

<div class="caption">

(9.8–10)

</div>

</div>

We can now define the generalized force
<span class="i">Q</span><sub><span class="i">i</span></sub> associated
with <span class="i">q</span><sub><span class="i">i</span></sub> to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1466.jpg](images/e9780486140520_i1466.jpg)

</div>

<div class="caption">

(9.8–11)

</div>

</div>

which enables Eq. 9.8–10 to be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1467.jpg](images/e9780486140520_i1467.jpg)

</div>

<div class="caption">

(9.8–12)

</div>

</div>

We now substitute Eqs. 9.8–7 and 9.8–12 into Hamilton’s equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1468.jpg](images/e9780486140520_i1468.jpg)

</div>

<div class="caption">

(9.8–13)

</div>

</div>

and since all the
<span class="i">δq</span><sub><span class="i">i</span></sub> are
independent and arbitrary, we can let all the
<span class="i">δq</span><sub><span class="i">i</span></sub> equal zero
except for
<span class="i">δq</span><sub><span class="i">k</span></sub><span class="i">,</span>
which will be specified as not equal to zero. Then in order to satisfy
the above equation, the coefficient of
<span class="i">δq</span><sub><span class="i">k</span></sub> must be
zero, and we arrive at Lagrange’s equation for the holonomic system.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1469.jpg](images/e9780486140520_i1469.jpg)

</div>

<div class="caption">

(9.8–14)

</div>

</div>

So far we have not stated whether the forces
<span class="b">F</span><sub><span class="i">j</span></sub> are
conservative or nonconservative. For a conservative system, the work is
expressible in terms of the potential energy <span class="i">U</span>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1470.jpg](images/e9780486140520_i1470.jpg)

</div>

<div class="caption">

(9.8–15)

</div>

</div>

and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1471.jpg](images/e9780486140520_i1471.jpg)

</div>

<div class="caption">

(9.8–16)

</div>

</div>

It is evident then that Lagrange’s equation for the conservative system
is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1472.jpg](images/e9780486140520_i1472.jpg)

</div>

<div class="caption">

(9.8–17)

</div>

</div>

It is now convenient to define the Lagrangian as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1473.jpg](images/e9780486140520_i1473.jpg)

</div>

<div class="caption">

(9.8–18)

</div>

</div>

and since
<span class="i">∂U/∂</span><span class="imageinline">![e9780486140520_i1474.jpg](images/e9780486140520_i1474.jpg)</span>
= 0, Eq. 9.8–17 can be written in terms of the Lagrangian as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1475.jpg](images/e9780486140520_i1475.jpg)

</div>

<div class="caption">

(9.8–19)

</div>

</div>

When both conservative and nonconservative forces act on a system, we
can separate the virtual work into terms like Eqs. 9.8–12 and 9.8–16,
and write Lagrange’s equation as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1476.jpg](images/e9780486140520_i1476.jpg)

</div>

<div class="caption">

(9.8–20)

</div>

</div>

<span class="b">Example 9.8–1</span>

The pendulum analogy is used in the simplified analysis of many
dynamical problems, including the sloshing of liquid fuel in missiles.
As an application of Lagrange’s equation, we will consider here the
spherical pendulum of <a href="#e9780486140520_c09.html#int_139"
id="e9780486140520_c09.html_ref_int_139" class="ref_int">Fig. 9.8-1</a>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1477.jpg](images/e9780486140520_i1477.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_139"
id="e9780486140520_c09.html_int_139" class="label_int"><span
class="b">Fig. 9.8-1</span></a>. Spherical pendulum.

</div>

</div>

The position of the mass, at a distance <span class="i">l</span> from
the center, can be specified by the generalized coordinates
<span class="i">θ</span> and <span class="i">ϕ,</span> which can be
varied independently.

The kinetic and potential energies are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1478.jpg](images/e9780486140520_i1478.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1479.jpg](images/e9780486140520_i1479.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

and the Lagrangian becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1480.jpg](images/e9780486140520_i1480.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

Substituting into Lagrange’s equation, the equations of motion are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1481.jpg](images/e9780486140520_i1481.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1482.jpg](images/e9780486140520_i1482.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

The solution of these equations can be obtained in the following manner.
Equation e can be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1483.jpg](images/e9780486140520_i1483.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

If we examine the Lagrangian, we would note that
<span class="i">L</span> is independent of <span class="i">ϕ</span>, so
that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1484.jpg](images/e9780486140520_i1484.jpg)

</div>

</div>

We should then expect Lagrange’s equation for the coordinate to reduce
to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1485.jpg](images/e9780486140520_i1485.jpg)

</div>

</div>

and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1486.jpg](images/e9780486140520_i1486.jpg)

</div>

</div>

Equation <span class="i">f</span> then is the direct consequence of
∂L/∂ϕ <span class="i">=</span> 0.

We can now make a general statement as follows: If the Lagrangian is not
a function of the generalized coordinate
<span class="i">q</span><sub><span class="i">k</span></sub>, then
∂<span class="i">L/∂q</span><sub><span class="i">k</span></sub> = 0, and
Lagrange’s equation for
<span class="i">q</span><sub><span class="i">k</span></sub> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1487.jpg](images/e9780486140520_i1487.jpg)

</div>

<div class="caption">

(<span class="i">g</span>)

</div>

</div>

Its integral is then immediately available as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1488.jpg](images/e9780486140520_i1488.jpg)

</div>

<div class="caption">

(<span class="i">h</span>)

</div>

</div>

where <span class="i">p</span><sub><span class="i">k</span></sub> is the
generalized momentum for coordinate
<span class="i">q</span><sub><span class="i">k</span></sub>. Such
coordinates are called cyclic coordinates.

Returning to the solution of the two equations of motion, we substitute
<span class="imageinline">![e9780486140520_i1489.jpg](images/e9780486140520_i1489.jpg)</span>
from Eq. <span class="i">f</span> into Eq. <span class="i">d</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1490.jpg](images/e9780486140520_i1490.jpg)

</div>

<div class="caption">

(<span class="i">i</span>)

</div>

</div>

We solve this equation in the usual way by multiplying by 2
<span class="imageinline">![e9780486140520_i1491.jpg](images/e9780486140520_i1491.jpg)</span>
and integrating.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1492.jpg](images/e9780486140520_i1492.jpg)

</div>

</div>

The solution for
<span class="imageinline">![e9780486140520_i1493.jpg](images/e9780486140520_i1493.jpg)</span>
is then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1494.jpg](images/e9780486140520_i1494.jpg)

</div>

<div class="caption">

(<span class="i">j</span>)

</div>

</div>

We have so far identified the constant
<span class="i">C</span><sub>1</sub> as the generalized momentum
<span class="i">p</span><sub><span class="i">ϕ</span></sub>. We will
show now that the constant <span class="i">C</span><sub>2</sub> is
associated with the total energy <span class="i">E</span> of the
conservative system, which is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1495.jpg](images/e9780486140520_i1495.jpg)

</div>

<div class="caption">

(<span class="i">k</span>)

</div>

</div>

We have from.Eqs. <span class="i">a, b,</span> and
<span class="i">c</span>,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1496.jpg](images/e9780486140520_i1496.jpg)

</div>

</div>

Eliminating
<span class="imageinline">![e9780486140520_i1497.jpg](images/e9780486140520_i1497.jpg)</span>
from Eq. <span class="i">f,</span> we arrive at the result

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1498.jpg](images/e9780486140520_i1498.jpg)

</div>

<div class="caption">

(<span class="i">l</span>)

</div>

</div>

By comparison with Eq. <span class="i">j</span>, we find that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1499.jpg](images/e9780486140520_i1499.jpg)

</div>

</div>

<span class="b">Example 9.8–2</span>

A spinning satellite with moments of inertia <span class="i">A</span>,
<span class="i">A</span>, <span class="i">C</span>, with
<span class="i">C</span> \< <span class="i">A,</span> has whip antennas
which are free to vibrate in the <span class="i">z</span> direction, as
shown in <a href="#e9780486140520_c09.html#int_140"
id="e9780486140520_c09.html_ref_int_140" class="ref_int">Fig. 9.8-2</a>.
Set up the vibration equation, using generalized coordinates associated
with the normal modes of the antenna beam, and outline a procedure to
establish the attitude drift of the spin axis.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1500.jpg](images/e9780486140520_i1500.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_140"
id="e9780486140520_c09.html_int_140" class="label_int"><span
class="b">Fig. 9.8-2</span></a> Energy dissipation by whip antennas of a
satellite.

</div>

</div>

We will assume the beam to have structural damping, which can be
accounted for by a complex stiffness <span class="i">EI</span>(1 +
<span class="i">iα</span>), where <span class="i">α</span> is the
structural damping factor. Letting <span class="i">m</span> be the mass
per unit length of the antenna, and <span class="i">w</span> the elastic
deflection in the <span class="i">z</span> direction, the differential
equation of motion is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1501.jpg](images/e9780486140520_i1501.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

The acceleration
<span class="i">a</span><sub><span class="i">z</span></sub> is that of a
point along the undeformed antenna, which from Eq.
7.6–14<span class="i">a</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1502.jpg](images/e9780486140520_i1502.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

We will express the deflection in terms of generalized coordinates
<span class="i">q</span><sub><span class="i">n</span></sub>(<span class="i">t</span>)
and the normal modes
<span class="i">ϕ</span><sub><span class="i">n</span></sub>(<span class="i">x</span>)
of the antenna,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1503.jpg](images/e9780486140520_i1503.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

The normal modes are vibration shapes associated with the undamped
harmonic oscillations at the natural frequencies
Ω<sub><span class="i">n</span></sub>, which obey the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1504.jpg](images/e9780486140520_i1504.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

We now substitute Eq. <span class="i">c</span> into
<span class="i">a</span> and replace
<span class="i">EI</span>(<span class="i">d</span><sup>4</sup><span class="i">ϕ</span><sub><span class="i">n</span></sub>/<span class="i">dx</span><sup>4</sup>)
by
<span class="i">m</span>Ω<sub><span class="i">n</span></sub><sup>2</sup><span class="i">ϕ</span><sub><span class="i">n</span></sub>
of Eq. <span class="i">d</span> to obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1505.jpg](images/e9780486140520_i1505.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

Multiplying Eq. <span class="i">e</span> by
<span class="i">ϕ</span><sub><span class="i">k</span></sub>
<span class="i">dx</span> and integrating over <span class="i">x</span>
= 0 to <span class="i">l,</span> and noting the orthogonality
relationship of the normal modes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1506.jpg](images/e9780486140520_i1506.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

The result is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1507.jpg](images/e9780486140520_i1507.jpg)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1508.jpg](images/e9780486140520_i1508.jpg)

</div>

</div>

where

<div class="illustype_image_math">

<div class="caption">

(<span class="i">g</span>)

</div>

<div class="image_math">

![e9780486140520_i1509.jpg](images/e9780486140520_i1509.jpg)

</div>

</div>

The steady–state oscillation of the antenna is then established as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1510.jpg](images/e9780486140520_i1510.jpg)

</div>

<div class="caption">

(<span class="i">h</span>)

</div>

</div>

To determine the energy dissipated per cycle, we start with the strain
energy

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1511.jpg](images/e9780486140520_i1511.jpg)

</div>

<div class="caption">

(<span class="i">i</span>)

</div>

</div>

Using only the first mode and noting that (see Sec. 7.6)

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1512.jpg](images/e9780486140520_i1512.jpg)

</div>

<div class="caption">

(<span class="i">j</span>)

</div>

</div>

the equation for the energy dissipated per cycle is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1513.jpg](images/e9780486140520_i1513.jpg)

</div>

<div class="caption">

(<span class="i">k</span>)

</div>

</div>

Equating this to <span class="i">Ṫ</span> of Eq. 7.6–6, the rate of
drift of the attitude angle can be expressed as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1514.jpg](images/e9780486140520_i1514.jpg)

</div>

<div class="caption">

(<span class="i">l</span>)

</div>

</div>

where the many constants of the problem have been lumped into
<span class="i">K</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1515.jpg](images/e9780486140520_i1515.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_141"
id="e9780486140520_c09.html_int_141" class="label_int"><span
class="b">Fig. 9.8-3</span></a> Resonance in attitude drift rate due to
whip antennas.

</div>

</div>

This result should be compared to that of Example 7.6–1. Since θ
generally starts from some small angle θ<sub>0</sub> and increases for
<span class="i">C</span>/<span class="i">A</span> \< 1, there is a
possibility of resonance if <span class="i">R</span><sub>1</sub> is
greater than unity. The peak values, however, are expressible as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1516.jpg](images/e9780486140520_i1516.jpg)

</div>

<div class="caption">

(<span class="i">m</span>)

</div>

</div>

which is similar in form to Eq. <span class="i">f</span> of Ex. 7.6—1,
although the <span class="i">K</span> are different. A plot of the drift
rate is shown in <a href="#e9780486140520_c09.html#int_141"
id="e9780486140520_c09.html_ref_int_141" class="ref_int">Fig. 9.8-3</a>.

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title123"></span>

# <span class="b">9.9 Nonholonomic Systems</span>

The development of the previous section for the holonomic system, Eqs.
9.8–1 to 9.8–13, apply equally well to nonholonomic systems. The
difference here is that for the nonholonomic system the
<span class="i">q</span><sub><span class="i">i</span></sub> of Eq. 9.8–1
are not all independent. However, the requirement for the independence
of the <span class="i">q</span><sub><span class="i">i</span></sub> for
the holonomic system was not imposed in the development of the previous
section until the step between Eqs. 9.8–13 and 9.8–14 was required.

For the nonholonomic system, the
<span class="i">q</span><sub><span class="i">i</span></sub> are
restricted by the constraint equations of the form

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1517.jpg](images/e9780486140520_i1517.jpg)

</div>

<div class="caption">

(9.9–1)

</div>

</div>

which are nonintegrable. Holonomic constraints may also be present, but
we will assume that they have been used to reduce the
<span class="i">q</span><sub><span class="i">i</span></sub> to
independent quantities, of which there will be <span class="i">n</span>
− <span class="i">m</span>, where <span class="i">m</span> is the number
of nonholonomic constraints.

We will assume for convenience that there are just two
(<span class="i">m</span> = 2) nonholonomic constraints and write their
variation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1518.jpg](images/e9780486140520_i1518.jpg)

</div>

<div class="caption">

(9.9–2)

</div>

</div>

Since the variation is one of configuration, holding time constant,
<span class="i">t</span> does not enter into Eq. 9.9–2. Two of the
<span class="i">q</span><sub><span class="i">i</span></sub> are now
related by Eq. 9.9–2, leaving <span class="i">n</span> − 2 of the
<span class="i">q</span><sub><span class="i">i</span></sub> as
independent quantities.

We will now multiply each of Eq. 9.9–2 by an undetermined multiplier
<span class="i">λ</span> and integrate between <span class="i">t
=</span> 0 and
<span class="i">t</span><sub><span class="i">1</span></sub> as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1519.jpg](images/e9780486140520_i1519.jpg)

</div>

<div class="caption">

(9.9–3)

</div>

</div>

(Note that the λ could be a function of time as well as constants.)
Including these terms in Eq. 9.8—13, we can write,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1520.jpg](images/e9780486140520_i1520.jpg)

</div>

<div class="caption">

(9.9–4)

</div>

</div>

Since <span class="i">n</span>–2 of the
<span class="i">δq</span><sub><span class="i">i</span></sub> are
independent, we will separate the above integrals to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1521.jpg](images/e9780486140520_i1521.jpg)

</div>

<div class="caption">

(9.9–5)

</div>

</div>

where the two
<span class="i">δq</span><sub><span class="i">i</span></sub> of the last
integral are fixed by the constraint equations and, therefore, are not
arbitrary. We can however, make the integrand of the last integral zero
by a proper choice of λ<sub>1</sub> and λ<sub>2</sub>. Each of the
integrand of the first integral can be shown to be zero by assuming one
of the arbitrary
<span class="i">δq</span><sub><span class="i">i</span></sub> to be
nonzero and the remaining <span class="i">δq</span><sub>i</sub> to be
all zero, repeating this procedure for each of the
(<span class="i">n</span>–2) δq<sub>i</sub>. We then arrive at
<span class="i">n</span> equations of the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1522.jpg](images/e9780486140520_i1522.jpg)

</div>

<div class="caption">

(9.9–6)

</div>

</div>

Since we have two additional unknowns λ<sub>1</sub> and λ<sub>2</sub>
.besides the <span class="i">n
q</span><sub><span class="i">i</span></sub><span class="i">,</span> we
need two other equations, which are furnished by the constraint
equations, Eq. 9.9–1, written in the form,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1523.jpg](images/e9780486140520_i1523.jpg)

</div>

<div class="caption">

(9.9–7)

</div>

</div>

These <span class="i">n</span> + 2 equations are then sufficient for the
solution of the problem.

In the development of this section, we have illustrated the method of
Lagrange’s undetermined multipliers, λ, which is not restricted to the
nonholonomic system, and can be applied equally well to holonomic
systems. Occasionally it is not convenient to reduce the variables of
the holonomic system to independent quantities by the use of the
constraint equations, in which case the Lagrange multiplier method can
be used. In such a case, the Lagrange multiplier method will also
provide a solution for the constraint forces, which are sometimes
required.

<span class="b">Example 9.9–1</span>

A thin disk of radius <span class="i">r</span> rolls down an inclined
plane of small angle x with the horizontal. If the plane of the disk is
always normal to the inclined plane, and capable of rotation about the
normal, determine the <span class="i">x, y</span> motion of the disk.

Referring to <a href="#e9780486140520_c09.html#int_142"
id="e9780486140520_c09.html_ref_int_142" class="ref_int">Fig. 9.9-1</a>,
the coordinates of the problem are <span class="i">ψ, x,</span> and
<span class="i">φ.</span> The equations for the kinetic and potential
energies are,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1524.jpg](images/e9780486140520_i1524.jpg)

</div>

<div class="caption">

(<span class="i">a</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1525.jpg](images/e9780486140520_i1525.jpg)

</div>

<div class="caption">

(<span class="i">b</span>)

</div>

</div>

and the constraint equation is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1526.jpg](images/e9780486140520_i1526.jpg)

</div>

<div class="caption">

(<span class="i">c</span>)

</div>

</div>

The Lagrange equations are then,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1527.jpg](images/e9780486140520_i1527.jpg)

</div>

<div class="caption">

(<span class="i">d</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1528.jpg](images/e9780486140520_i1528.jpg)

</div>

<div class="caption">

(<span class="i">e</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1529.jpg](images/e9780486140520_i1529.jpg)

</div>

<div class="caption">

(<span class="i">f</span>)

</div>

</div>

From (<span class="i">d</span>), <span class="i">ψ</span> is a constant
<span class="i">n</span>, and its integral is <span class="i">ψ</span> =
<span class="i">ψ</span><sub>0</sub> + <span class="i">nt</span>.
Substituting for <span class="i">ψ</span> in (<span class="i">e</span>),
the equation for λ becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1530.jpg](images/e9780486140520_i1530.jpg)

</div>

<div class="caption">

(<span class="i">g</span>)

</div>

</div>

With λ substituted into (<span class="i">f</span>), its integral is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1531.jpg](images/e9780486140520_i1531.jpg)

</div>

<div class="caption">

(<span class="i">h</span>)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1532.jpg](images/e9780486140520_i1532.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_142"
id="e9780486140520_c09.html_int_142" class="label_int"><span
class="b">Fig. 9.9-1</span></a><span class="b">.</span> Coordinates
<span class="i">y</span>, <span class="i">x,</span> and
<span class="i">φ</span> are related by nonholonomic constraint.

</div>

</div>

The <span class="i">x</span> and <span class="i">y</span> displacements
can be found from the integrals of

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1533.jpg](images/e9780486140520_i1533.jpg)

</div>

<div class="caption">

(<span class="i">i</span>)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1534.jpg](images/e9780486140520_i1534.jpg)

</div>

<div class="caption">

(<span class="i">j</span>)

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title124"></span>

# <span class="b">9.10 Lagrange’s Equation for Impulsive Forces</span>

During impact of one body on another, a very large force acts for a very
short time. Such forces are said to be impulsive. As the time of contact
diminishes to zero, the force tends to infinity; however, like the delta
function, the time integral of the impulsive force is finite.

When an impulsive force acts on a body, the velocity of the body
undergoes an instantaneous change over an infinitesimal change in
displacement. Thus, generalized velocities
<span class="imageinline">![e9780486140520_i1535.jpg](images/e9780486140520_i1535.jpg)</span>
will change instantaneously, whereas generalized coordinates
<span class="i">q</span><sub><span class="i">i</span></sub> will not.
The system is nonconservative since energy is generally dissipated
during impact.

In applying Lagrange’s equation to impulsive force systems, we approach
it by a limiting process. Starting with the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1536.jpg](images/e9780486140520_i1536.jpg)

</div>

<div class="caption">

(9.10–1)

</div>

</div>

we multiply by <span class="i">dt</span> and integrate over the impact
time.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1537.jpg](images/e9780486140520_i1537.jpg)

</div>

<div class="caption">

(9.10—2)

</div>

</div>

The second integral contain terms associated with the generalized
coordinate <span class="i">q</span><sub><span class="i">i</span></sub>
which do not change during the impact. Thus, in the limiting case when ∊
→ 0, the second integral vanishes, and we obtain the relationship,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1538.jpg](images/e9780486140520_i1538.jpg)

</div>

<div class="caption">

(9.10–3)

</div>

</div>

This equation states that the change in the generalized momentum is
equal to the generalized impulse.

<span class="b">Example 9.10–1</span>

Four equal bars, each of mass <span class="i">m</span> and length
2<span class="i">a</span>, lie on a smooth, horizontal floor, hinged
together in the form of a rhombus, as shown in the sketch. If an
impulsive force
<span class="imageinline">![e9780486140520_i1539.jpg](images/e9780486140520_i1539.jpg)</span>lb–sec.
is applied at <span class="i">A</span> in the direction
<span class="i">CA,</span> determine the initial angular velocity of the
bars.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1540.jpg](images/e9780486140520_i1540.jpg)

</div>

<div class="caption">

<span class="b">Fig. 9.10-1</span><span class="b">.</span> Impulsively
loaded structure.

</div>

</div>

Place coordinates <span class="i">x</span>, <span class="i">y</span>
with origin <span class="i">O</span> at the center of mass.

The <span class="i">x</span> and <span class="i">y</span> coordinates of
the center <span class="i">G</span> of the bar are,

<div class="blocktext">

<span class="i">x</span><sub><span class="i">G</span></sub> =
<span class="i">a</span> sin <span class="i">θ y</span><sub>G</sub> = a
cos <span class="i">θ</span>

</div>

and the velocity of the center of mass of the bars becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1541.jpg](images/e9780486140520_i1541.jpg)

</div>

</div>

where the minus sign applies to <span class="i">AB</span> and
<span class="i">AD</span> and the plus sign to <span class="i">CB</span>
and <span class="i">CD</span>.

The kinetic energy of the bars is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1542.jpg](images/e9780486140520_i1542.jpg)

</div>

</div>

and the change in the generalized momentum becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1543.jpg](images/e9780486140520_i1543.jpg)

</div>

</div>

The generalized force
<span class="imageinline">![e9780486140520_i1544.jpg](images/e9780486140520_i1544.jpg)</span>
is found from the virtual work of the impulse. Due to virtual
displacements <span class="i">δy</span><sub>0</sub> and
<span class="i">δθ,</span> the point <span class="i">A</span> undergoes
a displacement

<div class="blocktext">

<span class="i">δ</span>(<span class="i">y</span><sub>0</sub> +
2<span class="i">a</span> cos <span class="i">θ</span>) =
<span class="i">δy</span><sub>0</sub>–2<span class="i">a</span> sin
<span class="i">θ δθ</span>

</div>

and the virtual work of
<span class="imageinline">![e9780486140520_i1545.jpg](images/e9780486140520_i1545.jpg)</span>
is

<div class="blocktext">

<span class="i">δW</span> =
<span class="imageinline">![e9780486140520_i1546.jpg](images/e9780486140520_i1546.jpg)</span>(<span class="i">δy</span><sub>0</sub>–2<span class="i">a</span>
sin <span class="i">θ δθ</span>)

</div>

The generalized force due to <span class="i">δθ</span> is then

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1547.jpg](images/e9780486140520_i1547.jpg)

</div>

</div>

and, by substituting into Eq. 8.14–3, we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1548.jpg](images/e9780486140520_i1548.jpg)

</div>

</div>

and

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1549.jpg](images/e9780486140520_i1549.jpg)

</div>

</div>

<span class="b">PROBLEMS</span>

1.  A particle moving in space is defined by the spherical coordinates
    <span class="i">r, θ,</span> and <span class="i">(ϕ.</span>
    Determine the generalized forces associated with the spherical
    coordinates, and establish the component forces in the radial,
    meridian, and latitude directions.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1550.jpg](images/e9780486140520_i1550.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 1</span>

    </div>

    </div>

2.  A satellite moves in a plane orbit under the influence of an inverse
    square attraction. Derive the orbit equation from Lagrange’s
    formulation. Is there a cyclic coordinate for the system and, if so,
    what does it imply ?
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1551.jpg](images/e9780486140520_i1551.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 2</span>

    </div>

    </div>

3.  A spherical pendulum of length / is set up on the earth’s surface at
    latitude λ, with the z axis in the vertical direction and x axis
    pointing north. Show that the Lagrangian is
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1552.jpg](images/e9780486140520_i1552.jpg)

    </div>

    </div>

    where Ω. is the rotation speed of the earth and
    <span class="i">R</span> = radius of earth.

4.  Determine the Lagrangian for the symmetric top spinning about a
    fixed pivot on the floor. Establish the cyclic (ignorable)
    coordinates and write directly the resulting integrals.

5.  For a system of <span class="i">N</span> particles, the kinetic
    energy can be written in the form

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1553.jpg](images/e9780486140520_i1553.jpg)

    </div>

    </div>

    where

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1554.jpg](images/e9780486140520_i1554.jpg)

    </div>

    </div>

    Prove that for a scleronomic conservative system,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1555.jpg](images/e9780486140520_i1555.jpg)

    </div>

    </div>

6.  For a conservative system of <span class="i">N</span> particles,
    prove that the conservation of energy holds only if the time
    <span class="i">t</span> does not appear explicitly in the
    Lagrangian, in which case,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1556.jpg](images/e9780486140520_i1556.jpg)

    </div>

    </div>

7.  Using the Lagrangian approach, deduce Eulers dynamical equations for
    an arbitrary rigid body subjected to moments about the body axes.

    <span class="i">Hint: T</span> =
    ½(<span class="i">Aω</span><sub><span class="i">x</span></sub><sup>2</sup> +
    <span class="i">Bωy</span><sup><span class="i">2</span></sup> +
    <span class="i">Cω</span><sub><span class="i">z</span></sub><sup>2</sup>).
    Express the angular velocites in terms of Eulers angles. The
    generalized force can be determined by giving each of the Euler
    angles virtual displacement with the other two equal to zero.

8.  A mass is suspended from a weightless spring of stiffness
    <span class="i">k</span> lb/in. Write Lagrange’s equations and
    discuss the motion for small oscillations in the vertical plane.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1557.jpg](images/e9780486140520_i1557.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 8</span>

    </div>

    </div>

9.  Using Lagrange’s method, set up the equations for the motion of a
    bar suspended by a string and oscillating in a plane.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1558.jpg](images/e9780486140520_i1558.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 9</span>

    </div>

    </div>

10. A uniform bar of mass <span class="i">m</span> and length
    <span class="i">l</span> is suspended from one end by a spring of
    stiffness <span class="i">k</span> lb/in. The bar can swing freely
    only in one vertical plane and the spring <span class="i">x</span>
    is constrained to move only in the vertical direction. Set up the
    Lagrange equations of motion.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1559.jpg](images/e9780486140520_i1559.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 10</span>

    </div>

    </div>

11. A centrifugal pendulum of mass <span class="i">m</span> and length
    <span class="i">r</span> is attached to a flywheel of moment of
    inertia <span class="i">I.</span> Show that the kinetic energy of
    the system is,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1560.jpg](images/e9780486140520_i1560.jpg)

    </div>

    </div>

    where
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1561.jpg](images/e9780486140520_i1561.jpg)

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1562.jpg](images/e9780486140520_i1562.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 11</span>

    </div>

    </div>

12. A particle of mass <span class="i">m</span> slides without friction
    on a hoop of radius <span class="i">r,</span> which is rotated with
    constant speed Ω about a vertical diameter. A single coordinate
    <span class="i">θ</span> is sufficient to describe the position of
    <span class="i">m;</span> however, we have a moving constraint.
    Compare the total energy of the system with that determined from
    <span class="i">T</span> + <span class="i">U</span> =
    <span class="i">θ</span><span class="i">(∂L/∂θ</span>)–<span class="i">L</span>
    and discuss this discrepancy.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1563.jpg](images/e9780486140520_i1563.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 12</span>

    </div>

    </div>

13. A uniform bar of length 21 and mass <span class="i">m</span> is
    dropped from a height <span class="i">h</span> onto a horizontal
    floor. The bar descends without rotation and at an angle
    <span class="i">θ</span><sub>0</sub> with the floor. If the
    coefficient of restitution between the floor and bar is
    <span class="i">e</span>, determine the velocity of the center of
    the bar and its angular velocity immediately after impact.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1564.jpg](images/e9780486140520_i1564.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 13</span>

    </div>

    </div>

14. In Prob. 13, determine the time elapsed after the first impact when
    the opposite side of the bar strikes the floor. What is the angle
    <span class="i">θ</span> when it strikes?

15. A simplified two–dimensional version of a space craft in landing is
    shown in the sketch, where the two legs are restrained from rotation
    by a torsional spring of stiffness <span class="i">K</span>
    lb–in./rad. If the legs strike the smooth inelastic plane with
    velocity <span class="i">v</span>, determine the rotational velocity
    <span class="i">6</span> immediately after impact. Assume
    <span class="i">θ</span> = 0 before impact and the torsional spring
    to be exerting a moment <span class="i">C</span><sub>0</sub>,
    holding the legs against the stop.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1565.jpg](images/e9780486140520_i1565.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 15</span>

    </div>

    </div>

16. For the system shown, show that, if one incorrectly takes
    <span class="i">y</span> and <span class="i">θ</span> as independent
    generalized coordinates <span class="i">q</span><sub>1</sub> and
    <span class="i">q</span><sub>2</sub> then the resulting two Lagrange
    equations are also incorrect. Demonstrate the use of the Lagrangian
    multiplier by establishing the correct equation, using
    <span class="i">y</span> and <span class="i">6</span>, and a
    constraint equation.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1566.jpg](images/e9780486140520_i1566.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 16</span>

    </div>

    </div>

17. Two uniform bars of mass <span class="i">m</span> and length
    <span class="i">/</span> are hinged as shown, and lie on a smooth
    horizontal plane. If an impulsive force strikes the bar normally at
    one end, determine the angular velocities of the two bars and the
    velocity of the hinge.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1567.jpg](images/e9780486140520_i1567.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 17</span>

    </div>

    </div>

18. Four hinged bars, each of length <span class="i">/</span> and mass
    <span class="i">m,</span> fall in translation and strike a
    horizontal inelastic ground. Taking <span class="i">y</span> and
    <span class="i">θ</span> as generalized coordinates, find the motion
    immediately after impact.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1568.jpg](images/e9780486140520_i1568.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 18</span>

    </div>

    </div>

19. A rigid pendulum of length <span class="i">/</span> and mass
    <span class="i">m</span> can swing around the horizontal axis
    <span class="i">AA</span> which is mounted in a frame that can
    rotate freely around the vertical axis <span class="i">BB.</span>
    The moment of inertia of the frame and horizontal axle about the
    vertical axis is <span class="i">/.</span> At the instant
    <span class="i">t</span> = 0, the pendulum in the vertical position
    is given an initial velocity v<sub>0</sub>, and the frame is given
    an initial angular velocity <span class="i">ω</span><sub>0</sub>.
    (<span class="i">a</span>) Set up the equations of motion, noting
    that the momentum and energy are conserved ;
    (<span class="i">b</span>) simplify the results of
    (<span class="i">a</span>) by assuming small angles, sin
    <span class="i">θ = θ,</span> and cos <span class="i">θ</span> =
    1–½θ<sup>2</sup>; (<span class="i">c</span>) discuss the motion of
    the simplified system for
    <span class="i">ω</span><sub>0</sub><sup>2</sup> \<
    <span class="i">g/l</span> and
    <span class="i">ω</span><sub>0</sub><sup>2</sup> \>
    <span class="i">g/l</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1569.jpg](images/e9780486140520_i1569.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 19</span>

    </div>

    </div>

20. A spherical pendulum of length <span class="i">l</span> and mass
    <span class="i">m</span> is suspended from end 0 of a horizontal arm
    of length <span class="i">e</span> that rotates with constant
    angular velocity <span class="i">ω</span> about a fixed vertical
    axis <span class="i">C</span>, as shown in the sketch. Assuming
    small oscillatory amplitudes and a damping equal to ζ × critical
    damping in a plane pendulum oscillation, show that the equations of
    motion of the pendulum bob are
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1570.jpg](images/e9780486140520_i1570.jpg)

    </div>

    </div>

    where <span class="i">p</span><sup>2</sup> =
    <span class="i">g</span>/<span class="i">l</span>.
    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1571.jpg](images/e9780486140520_i1571.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 20</span>

    </div>

    </div>

21. In Prob. 20, let <span class="i">z</span> =
    <span class="i">x–x</span><sub>0</sub> + <span class="i">iy</span>
    and <span class="i">x</span><sub>0</sub> =
    <span class="i">eω</span><sup>2</sup>/(<span class="i">p</span><sup>2</sup>–<span class="i">ω</span><sup>2</sup>),
    where <span class="i">x</span><sub>0</sub> denotes the position of
    static equilibrium (not necessarily stable), and show that the two
    equations can be reduced to a single homogeneous equation in z with
    a general solution
    <div class="blocktext">

    <span class="i">z</span> = <span class="i">Ae</span>
    (–<span class="i">ζ–</span>)(<span class="i">ρ</span>+<span class="i">ω</span>)t +
    <span class="i">Be</span><sup>(−ζ+i)(<span class="i">ρ</span>–<span class="i">ω</span>)<span class="i">t</span></sup>
    <span class="i">ζ</span> \<\< 1

    </div>

    where terms of order <span class="i">ζ</span><sup>2</sup> have been
    neglected. Discuss the criteria for stability of small oscillations.

22. A one–wheel trailer shown in the sketch is towed with velocity
    <span class="i">v.</span> If the trailer hitch has a lateral
    stiffness <span class="i">k,</span> and the radius of gyration of
    the trailer about the center of mass <span class="i">G</span> is
    <span class="i">p,</span> write the two equations of motion and the
    constraint equation for no lateral sliding of the trailer wheel.
    Determine the stability of the trailer for small
    <span class="i">θ</span> (i.e., roots of the characteristic equation
    must not have positive real parts).

23. Carry out the solution for <span class="i">x</span> and
    <span class="i">y</span> in Example 9.9–1. Show that, if the initial
    conditions are zero, the curve traced out will be a cycloid.

24. The spin axis of a space station with <span class="i">C</span> =
    <span class="i">kA</span> (for a thin disk <span class="i">k</span>
    = 2) is initially pointing to the north star. It is desired to
    change the direction of the spin axis by <span class="i">θ</span>°
    in a specified direction without inducing a precession about the new
    direction. This can be done by two properly timed impulsive blasts
    from a single rocket engine on the rim and pointing parallel to the
    spin axis. If the initial angular momentum of the station is
    <span class="i">h</span> = <span class="i">Cω</span><sub>0</sub>,
    determine the timing of the first and second blasts in relation to
    the desired direction change and their magnitude.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1572.jpg](images/e9780486140520_i1572.jpg)

</div>

<div class="caption">

<span class="b">Prob. 22</span>

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1573.jpg](images/e9780486140520_i1573.jpg)

</div>

<div class="caption">

<span class="b">Prob. 24</span>

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title125"></span>

# <span class="b">9.11 Lagrange’s Equations for Rotating Coordinates</span>

In the dynamic analysis of flexible missiles, it is convenient to use a
set of coordinates moving with the missile. The missile can be
considered a system of particles whose position relative to the moving
axes can be defined by generalized coordinates
<span class="i">q</span><sub><span class="i">i</span></sub><span class="i">.</span>

In setting up the equations of motion, it is often simpler to start from
the kinetic and potential energies of the system, using Lagrange’s
equation. For rotating coordinates, these equations differ from the
usual Lagrange equations for fixed coordinates ; however, since their
rigorous derivation is
lengthy,<sup><a href="#e9780486140520_ftn01.html#ftn_fn16"
id="e9780486140520_c09.html_ref_ftn_fn16">p</a></sup> we will only
present the equations and justify each term.

The position of the origin relative to the system of particles and the
orientation of the axes are arbitrary choices which will influence the
final form of the equations of motion. We will place the moving axes as
shown in <a href="#e9780486140520_c09.html#int_143"
id="e9780486140520_c09.html_ref_int_143" class="ref_int">Fig. 9.11-1</a>,
with the origin at the center of mass and the <span class="i">x</span>
axis coinciding with the missile longitudinal axis in the undeformed
state. Aside from the coordinates
<span class="i">q</span><sub><span class="i">i</span></sub> for the
relative motion, the coordinate axes in plane motion will have three
degrees of freedom, <span class="i">x</span><sub>0</sub>,
<span class="i">y</span><sub>0</sub>, and <span class="i">θ</span>,
which can be varied independently. The Lagrange equations can then be
written as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1574.jpg](images/e9780486140520_i1574.jpg)

</div>

<div class="caption">

(9.11-1)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1575.jpg](images/e9780486140520_i1575.jpg)

</div>

<div class="caption">

(9.11–2)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1576.jpg](images/e9780486140520_i1576.jpg)

</div>

<div class="caption">

(9.11–3)

</div>

</div>

The equation for
<span class="i">q</span><sub><span class="i">i</span></sub> remain
unaltered in form.

In accounting for the terms in these equations, we recognize
∂<span class="i">T</span>/∂<span class="i">ẋ</span><sub>0</sub> and
<span class="i">∂T/∂ẏ</span><sub>0</sub> as the generalized momenta, and
<span class="i">∂T</span>/∂<span class="imageinline">![e9780486140520_i1577.jpg](images/e9780486140520_i1577.jpg)</span>
as the generalized angular momentum. We will then represent the linear
momentum by

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1578.jpg](images/e9780486140520_i1578.jpg)

</div>

<div class="caption">

(9.11–4)

</div>

</div>

As the force equation is the rate of change of the linear momentum,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1579.jpg](images/e9780486140520_i1579.jpg)

</div>

<div class="caption">

(9.11–5)

</div>

</div>

the terms of Eq. 9.11–1 and 9.11–2 are immediately accounted for.

The terms of Eq. 9.11–3 can be identified from Eq. 7.11–3, which can be
written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1580.jpg](images/e9780486140520_i1580.jpg)

</div>

<div class="caption">

(9.11–6)

</div>

</div>

The term
<span class="i">∂T/</span>∂<span class="imageinline">![e9780486140520_i1581.jpg](images/e9780486140520_i1581.jpg)</span>
is the angular momentum h<sub>0</sub>, and the remaining two terms are
equal to <span class="b">Ṙ</span><sub>0</sub> <span class="b">×</span> ∑
<span class="i">m</span><sub><span class="i">i</span></sub><span class="b">ṙ</span><sub>i</sub>,
where <span class="b">Ṙ</span><sub>0</sub> =
<span class="i">ẋ</span><sub>0</sub><span class="b">i</span> +
<span class="i">ẏ</span><sub>0</sub><span class="b">j</span>.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1582.jpg](images/e9780486140520_i1582.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_143"
id="e9780486140520_c09.html_int_143" class="label_int"><span
class="b">Fig. 9.11-1</span></a><span class="b">.</span> Rotating
coordinate system.

</div>

</div>

</div>

<div class="section1">

<span id="e9780486140520_c09.html_title126"></span>

# <span class="b">9.12 Missile Dynamic Analysis</span>

Missiles are, in general, flexible structures, weight being of primary
concern. Vibrational problems are thus likely to plague their
performance, and it is in general necessary to make a dynamical analysis
of a vehicle in flight. Such an analysis consists of formulating the
equations of motion in all their details to account for the interaction
of the bending of the flexible missile with the rigid body motion, the
reaction of the swiveling engine, the sloshing of the propellant, the
excitation of the aerodynamic forces and gusts, and the coupling of the
servosystem controlling the stability of its attitude. The equations of
motion must then be linearized and programmed for machine computation,
i.e., the missile is theoretically flown on the high–speed computer.

It is evident that a detailed formulation of all the factors pertinent
to the dynamical analysis is beyond the scope of this text. It is
possible, however, to discuss a greatly simplified problem which will
serve to illustrate the dynamical techniques employed in the general
analysis.

We will consider here the problem of a flexible missile of constant
mass, where the propellant is treated as a solid to avoid the
complications of sloshing. The engine will be considered to be
gimballed, and the motion will be restricted to the vertical plane of
the trajectory, as shown in <a href="#e9780486140520_c09.html#int_144"
id="e9780486140520_c09.html_ref_int_144" class="ref_int">Fig. 9.12-1</a>.
The coupling of the servosystem, actuating the gimballed engine
attitude, will also be neglected.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1583.jpg](images/e9780486140520_i1583.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_144"
id="e9780486140520_c09.html_int_144" class="label_int"><span
class="b">Fig. 9.12-1</span></a><span class="b">.</span> Geometry of
flexible missile and coordinates.

</div>

</div>

<div class="section2">

<span id="e9780486140520_c09.html_title127"></span>

# <span class="i">Coordinate system</span>

The choice of the coordinate system is an important one which depends on
the vibrational data available. The missile can be treated as a
free–free beam, and its normal modes, computed with engine locked on,
will be assumed to be available from a previous analysis. Such modes are
orthogonal and possess the property of zero linear and angular momenta
about the missile vibrational axis (axis coinciding with the undeformed
missile with engine locked on, from which vibrational displacements are
measured) passing through its center of mass. In actual analysis, the
shear deformation and rotatory inertia terms are accounted for in the
normal mode analysis; however, for simplicity of discussion we will omit
these terms.

The <span class="i">x</span>, <span class="i">y</span> coordinate axes
will be chosen with the origin at the center of mass, the x axis
coinciding with the missile vibrational axis. It is evident, then, that
the missile longitudinal axis will undergo an additional displacement
due to the rotation of the engine. The nature of this additional
displacement is readily understood by considering a rigid missile whose
engine section is given a rotational velocity
<span class="imageinline">![e9780486140520_i1584.jpg](images/e9780486140520_i1584.jpg)</span>
by an internal hinge moment, as shown in
<a href="#e9780486140520_c09.html#int_145"
id="e9780486140520_c09.html_ref_int_145" class="ref_int">Fig. 9.12-2</a>.
If <span class="i">m</span> and
<span class="i">m</span><sub><span class="i">e</span></sub> are the
total mass and the engine mass respectively, the maintenance of zero
linear momentum (since there is no external force) can be expressed by
the equation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1585.jpg](images/e9780486140520_i1585.jpg)

</div>

<div class="caption">

(9.12–1)

</div>

</div>

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1586.jpg](images/e9780486140520_i1586.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_c09.html#ref_int_145"
id="e9780486140520_c09.html_int_145" class="label_int"><span
class="b">Fig. 9.12-2</span></a>. Conservation of linear and angular
momenta.

</div>

</div>

Letting <span class="i">c</span> be a point on the missile longitudinal
axis coinciding with the center of mass of the missile in the undeformed
state, and <span class="i">e</span> be the center of mass of the engine,
or section aft of the hinge, the above equation becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1587.jpg](images/e9780486140520_i1587.jpg)

</div>

<div class="caption">

(9.12–2)

</div>

</div>

It is evident then that point <span class="i">c</span> is displaced
laterally by the amount

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1588.jpg](images/e9780486140520_i1588.jpg)

</div>

<div class="caption">

(9.12–3)

</div>

</div>

The small displacement of <span class="i">c</span> in the
<span class="i">x</span> direction due to <span class="i">δ</span> is of
second order and will be neglected.

In addition to the lateral displacement
<span class="i">y</span><sub><span class="i">c</span></sub>, there will
be rotations of the sections forward and aft of the hinge to maintain
zero angular momentum about the mass center of the missile. Letting the
angular velocity of the missile forward of the hinge be
<span class="imageinline">![e9780486140520_i1589.jpg](images/e9780486140520_i1589.jpg)</span>,
<span class="i">I</span><sub>0</sub> the mass moments of inertia of the
entire missile about the center of mass, and
<span class="i">I</span><sub><span class="i">h</span></sub> the mass
moment of inertia of the engine about the hinge, the angular momentum
equation is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1590.jpg](images/e9780486140520_i1590.jpg)

</div>

<div class="caption">

(9.12–4)

</div>

</div>

Since <span class="i">ẏ</span> =
<span class="i">ẏ</span><sub><span class="i">c</span></sub>–<span class="i">x</span>
<span class="imageinline">![e9780486140520_i1591.jpg](images/e9780486140520_i1591.jpg)</span>
and <span class="i">x</span> =–(l<sub><span class="i">h</span></sub> +
<span class="i">z</span>) and
<span class="imageinline">![e9780486140520_i1592.jpg](images/e9780486140520_i1592.jpg)</span><span class="i">x
dm</span> = 0, the equation reduces to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1593.jpg](images/e9780486140520_i1593.jpg)

</div>

</div>

from which

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1594.jpg](images/e9780486140520_i1594.jpg)

</div>

<div class="caption">

(9.12–5)

</div>

</div>

These displacements can be considered to be the rigid missile
displacements due to hinge rotation <span class="i">δ</span>, which must
be added to the vibrational displacements to obtain the total
displacement of the flexible missile center line. They are, therefore,
equivalent to translating and rotating the missile vibrational axis by
<span class="i">y</span><sub><span class="i">c</span></sub> and
<span class="i">θ</span><sub><span class="i">f</span></sub>, and the
total lateral displacement <span class="i">y</span> of the flexible
center line from the moving coordinate axis <span class="i">x</span> is,
at point x

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1595.jpg](images/e9780486140520_i1595.jpg)

</div>

<div class="caption">

(9.12–6)

</div>

</div>

where the vibrational displacement is represented by the sum of the
normal modes
<span class="i">φ</span><sub><span class="i">i</span></sub>(<span class="i">x</span>)
multiplied by the generalized coordinate
<span class="i">q</span><sub><span class="i">i</span></sub>(<span class="i">t</span>)
associated with the mode.

With the displacement relative to the coordinate system established, we
next examine the motion of the coordinate axes themselves. The
<span class="i">x</span> axis, which coincides with the missile
vibrational axis or the missile longitudinal axis with
<span class="i">δ</span> = 0, makes an angle <span class="i">ɵ</span>
with the vertical, as shown in
<a href="#e9780486140520_c09.html#int_144" class="ref_int">Fig.
9.12-1</a>. The rate of rotation of the coordinate axes is then
<span class="i">ω</span> =
<span class="imageinline">![e9780486140520_i1596.jpg](images/e9780486140520_i1596.jpg)</span>.

The origin of the coordinate axes, coinciding with the center of mass at
all times, has a velocity v<sub>0</sub> tangent to the trajectory. The
angle α between v<sub>0</sub> and the x axis is the angle of attack of
the missile’s longitudinal axis (the local angle of attack will differ
from α by <span class="i">dy</span>/<span class="i">dx</span>). Due to
the changing direction of the trajectory tangent, the acceleration of
the origin will be
<span class="imageinline">![e9780486140520_i1597.jpg](images/e9780486140520_i1597.jpg)</span>
parallel to v<sub>0</sub>, and <span class="i">υ</span><sub>0</sub>
<span class="imageinline">![e9780486140520_i1598.jpg](images/e9780486140520_i1598.jpg)</span>
perpendicular to v<sub>0</sub>, where <span class="i">β</span> is the
angle made by v<sub>0</sub> and the vertical.

</div>

<div class="section2">

<span id="e9780486140520_c09.html_title128"></span>

# <span class="i">Equations of motion</span>

With the coordinate system defined in the foregoing, the equations of
motion can be formulated by determining the kinetic and potential
energies of the missile to be substituted into Lagrange’s equation,
taking note of the fact that the coordinates are rotating (see Sec.
9.11).

The velocity of a point <span class="b">r</span> =
<span class="i">x</span><span class="b">i</span> +
<span class="i">y</span><span class="b">j</span> in the rotating
coordinate system is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1599.jpg](images/e9780486140520_i1599.jpg)

</div>

<div class="caption">

(9.12–7)

</div>

</div>

For any point <span class="i">x</span>, <span class="i">y</span> forward
of the hinge <span class="i">h</span>, the x and
<span class="i">y</span> components are

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1600.jpg](images/e9780486140520_i1600.jpg)

</div>

</div>

(The relative velocity <span class="i">ẋ</span> of a point on the
missile is of second order compared to <span class="i">y</span> and is,
therefore, neglected.) The velocity of a point aft of the hinge can be
found from the above equations by replacing <span class="i">y</span> by
<span class="i">y</span> − <span class="i">zδ</span>.

In writing the kinetic energy equation of the missile with the swiveling
engine, we need the squares of the velocity as follows:

Forward of the hinge

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1601.jpg](images/e9780486140520_i1601.jpg)

</div>

<div class="caption">

(9.12–8)

</div>

</div>

Aft of the hinge

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1602.jpg](images/e9780486140520_i1602.jpg)

</div>

<div class="caption">

(9.12–9)

</div>

</div>

Thus part of <span class="i">v</span><sup>2</sup> aft of the hinge has
the same form as that forward of the hinge, which enables
<span class="i">T</span> to be written in the form
<span class="i">T</span> = <span class="i">T</span><sub>0</sub> +
<span class="i">T</span><sub><span class="i">δ</span></sub>, where the
quantity <span class="i">δ</span> appears only in
<span class="i">T</span><sub><span class="i">δ</span></sub>.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1603.jpg](images/e9780486140520_i1603.jpg)

</div>

<div class="caption">

(9.12–10)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1604.jpg](images/e9780486140520_i1604.jpg)

</div>

<div class="caption">

(9.12–11)

</div>

</div>

In these equations the generalized coordinates are
<span class="i">x</span><sub>0</sub>,
<span class="i">y</span><sub>0</sub>, <span class="i">θ</span>,
<span class="i">δ</span>, and
<span class="i">q</span><sub><span class="i">i</span></sub>, and it must
be remembered that <span class="i">y</span> is related to
<span class="i">δ</span> and
<span class="i">q</span><sub><span class="i">i</span></sub> through Eq.
9.12–6.

The equations of motion relating to the generalized coordinates
<span class="i">x</span><sub>0</sub>,
<span class="i">y</span><sub>0</sub>, and <span class="i">ɵ</span> can
be determined from Lagrange’s equations, Eqs. 9.11–1, 9.11–2, and
9.11–3, however, since the linear and angular momenta relative to the
coordinate system are zero, the sums of the external forces and moments
must equal the rate of change of the linear and angular momenta of the
rigid missile, which are related to the linear and angular accelerations
of the <span class="i">x</span>, <span class="i">y</span> coordinate
system with origin at the center of mass. These equations can therefore
be written as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1605.jpg](images/e9780486140520_i1605.jpg)

</div>

<div class="caption">

(9.12–12)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1606.jpg](images/e9780486140520_i1606.jpg)

</div>

<div class="caption">

(9.12–13)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1607.jpg](images/e9780486140520_i1607.jpg)

</div>

<div class="caption">

(9.12–14)

</div>

</div>

where <span class="i">F</span><sub><span class="i">e</span></sub> is the
engine thrust, <span class="i">D</span>\*, <span class="i">L</span>\*,
and <span class="i">M</span><sub>0</sub>\* are the drag and lift
components of the aerodynamic force and its moment about 0,
<span class="i">y</span><sub><span class="i">h</span></sub>′ =
(<span class="i">dy</span>/<span class="i">dx</span>)<sub><span class="i">h</span></sub>,
and <span class="i">a</span><sub>0<span class="i">x</span></sub> and
<span class="i">a</span><sub>0<span class="i">y</span></sub> represent
the acceleration of the center of mass 0, which is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1608.jpg](images/e9780486140520_i1608.jpg)

</div>

<div class="caption">

(9.12–15)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1609.jpg](images/e9780486140520_i1609.jpg)

</div>

<div class="caption">

(9.12–16)

</div>

</div>

To demonstrate that these equations can also be determined from
Lagrange’s equations for rotating coordinates, the first of the above
equation, for the sum of the forces in the <span class="i">x</span>
direction, will be derived from Eq. 9.11–1. Differentiating the kinetic
energy, we have,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1610.jpg](images/e9780486140520_i1610.jpg)

</div>

<div class="caption">

(9.12–17)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1611.jpg](images/e9780486140520_i1611.jpg)

</div>

<div class="caption">

(9.12–18)

</div>

</div>

Substituting into equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1612.jpg](images/e9780486140520_i1612.jpg)

</div>

<div class="caption">

(9.12–19)

</div>

</div>

we obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1613.jpg](images/e9780486140520_i1613.jpg)

</div>

<div class="caption">

(9.12–20)

</div>

</div>

This equation can be rearranged as follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1614.jpg](images/e9780486140520_i1614.jpg)

</div>

<div class="caption">

(9.12–21)

</div>

</div>

Since the second and third terms on the left side of this equation are
the linear momentum relative to the coordinates, or the condition for
the <span class="i">x</span> axis passing through the center of mass
(see Eq. 9.12–4), they are zero. The term
<span class="imageinline">![e9780486140520_i1615.jpg](images/e9780486140520_i1615.jpg)</span>
is also a negligibly small term. We have, therefore, demonstrated the
use of the Lagrange’s equation for rotating coordinates.

For the beam equation relating to the generalized coordinate
<span class="i">q</span><sub><span class="i">i</span></sub> and the
engine rotation equation relating to <span class="i">δ</span>, the usual
form of Lagrange’s equation applies. We need, however, the equation for
the potential or strain energy due to bending, which is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1616.jpg](images/e9780486140520_i1616.jpg)

</div>

<div class="caption">

(9.12–22

</div>

</div>

From Eq. 9.12–6 the curvature is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1617.jpg](images/e9780486140520_i1617.jpg)

</div>

<div class="caption">

(9.12–23)

</div>

</div>

where the primes stand for differentiation with respect to
<span class="i">x</span>. Substituting into <span class="i">U</span> and
making use of the orthogonality relation,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1618.jpg](images/e9780486140520_i1618.jpg)

</div>

<div class="caption">

(9.12–24)

</div>

</div>

The equation for the strain energy becomes,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1619.jpg](images/e9780486140520_i1619.jpg)

</div>

<div class="caption">

(9.12–25)

</div>

</div>

The various partial derivatives needed for Lagrange’s equation are:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1620.jpg](images/e9780486140520_i1620.jpg)

</div>

</div>

We note here that
<span class="imageinline">![e9780486140520_i1621.jpg](images/e9780486140520_i1621.jpg)</span>
is a very small quantity, and terms multiplied by it can be neglected.
Substituting for <span class="i">y</span> from Eq. 9.12—6, taking into
account the orthogonality condition, and noting that the linear and
angular momenta of the vibration modes are zero,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1622.jpg](images/e9780486140520_i1622.jpg)

</div>

<div class="caption">

(9.12–26)

</div>

</div>

we arrive at the result,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1623.jpg](images/e9780486140520_i1623.jpg)

</div>

<div class="caption">

(9.12–27)

</div>

</div>

where the right side of the equation is established from the generalized
force

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1624.jpg](images/e9780486140520_i1624.jpg)

</div>

<div class="caption">

(9.12–28)

</div>

</div>

In a similar manner, the engine rotation equation is determined from

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1625.jpg](images/e9780486140520_i1625.jpg)

</div>

<div class="caption">

(9.12–29)

</div>

</div>

which gives

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1626.jpg](images/e9780486140520_i1626.jpg)

</div>

<div class="caption">

(9.12–30)

</div>

</div>

where the generalized force
<span class="i">Q</span><sub><span class="i">δ</span></sub> =
<span class="i">M</span><sub><span class="i">A</span></sub>(<span class="i">δ</span><sub><span class="i">A</span></sub>
− <span class="i">δ</span>) −
<span class="imageinline">![e9780486140520_i1627.jpg](images/e9780486140520_i1627.jpg)</span>
ci–ated with
<span class="i">M</span><sub><span class="i">δ</span></sub>, the spring
moment per unit angle of the hinge when locked,
<span class="i">M</span><sub><span class="i">D</span></sub> with the
damping moment of the hinge,
<span class="i">M</span><sub><span class="i">A</span></sub> with the
engine actuator moment, and
<span class="i">δ</span><sub><span class="i">A</span></sub> with the
engine actuator position called by the autopilot. The autopilot
actuating the engine attitude <span class="i">δ</span> operates from
signals generated by the rate gyros in the missile in such a way that
the missile motion at the position of the rate gyro, which depends on
all of the generalized coordinates, is coupled to the previous equation
through the engine attitude <span class="i">δ</span>.

<span class="b">PROBLEMS</span>

1.  Assume that the mass of a portion of the missile is represented by a
    lumped mass
    <span class="i">m</span><sub><span class="i">j</span></sub> mounted
    on a spring of stiffness <span class="i">k</span> against lateral
    motion <span class="i">ζ</span><sub><span class="i">j</span></sub>
    from the center line at
    <span class="i">x</span><sub><span class="i">j</span></sub>. Derive
    the equation for the additional kinetic energy of the missile due to
    <span class="i">ζ</span><sub><span class="i">j</span></sub>.

2.  Derive Eq. 9.12–13 by the use of Lagrange’s equation,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1628.jpg](images/e9780486140520_i1628.jpg)

    </div>

    </div>

3.  Derive Eq. 9.12–14 by the use of Lagrange’s equation,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1629.jpg](images/e9780486140520_i1629.jpg)

    </div>

    </div>

4.  Prove Eqs. 9.12–24 and 9.12–25.

5.  Derive Eq. 9.12–30 for the engine rotation.

6.  An elastic uniform bar of mass <span class="i">m</span> and length
    <span class="i">l</span> is supported from its upper end by a smooth
    pin. A constant force P is suddenly applied normal to the bar at its
    mid–length. Using generalized coordinates q<sub>i</sub>, and three
    arbitrary modes,
    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1630.jpg](images/e9780486140520_i1630.jpg)

    </div>

    </div>

    determine the equation of motion, the natural frequencies, and the
    mode shapes.

7.  It is proposed to determine the natural frequencies of the two span
    beams of unequal length by assuming the deflection to be expressible
    by the equation,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1631.jpg](images/e9780486140520_i1631.jpg)

    </div>

    </div>

    where

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1632.jpg](images/e9780486140520_i1632.jpg)

    </div>

    </div>

    <div class="illustype_image_text">

    <div class="image_text">

    ![e9780486140520_i1633.jpg](images/e9780486140520_i1633.jpg)

    </div>

    <div class="caption">

    <span class="b">Prob. 7</span>

    </div>

    </div>

    Show that the constraint equation
    ∑<sub><span class="i">i</span></sub>
    <span class="i">q</span><sub><span class="i">i</span></sub>
    <span class="i">ϕ</span><sub><span class="i">i</span></sub>(<span class="i">c</span>)
    = 0, must be imposed and that the equation for the natural
    frequencies is,

    <div class="illustype_image_math">

    <div class="image_math">

    ![e9780486140520_i1634.jpg](images/e9780486140520_i1634.jpg)

    </div>

    </div>

</div>

</div>

</div>

<span id="e9780486140520_bm01.html"></span>

<div class="backMatter">

<span id="e9780486140520_bm01.html_title129"></span>

# <span class="b">General References</span>

1.  Davis, L., D. Follin, and L. Blitzer, Exterior Ballistics of
    Rockets, D. Van Nostrand, Princeton, N. J. (1958).
2.  Deimel, R. F., <span class="i">Mechanics of the Gyroscope,</span>
    The Macmillan Book Co., New York (1929). Reprinted by Dover
    Publications.
3.  Ehricke, H. A., <span class="i">Space Flight,</span> Vol. 1, D. Van
    Nostrand, New York (1960).
4.  Goldstein, H., <span class="i">Classical Mechanics,</span>
    Addison–Wesley Publishing Co., Reading, Mass. (1951).
5.  Gray, A., A <span class="i">Treatise on Gyrostatics and Rotational
    Motion,</span> The Macmillan Book Co., New York (1918). Reprinted by
    Dover Publications.
6.  Lanczos, C, <span class="i">The Variational Principle of
    Mechanics,</span> The University of Toronto Press, Toronto (1949).
7.  McCuskey, S. W., <span class="i">Introduction to Advanced
    Dynamics,</span> Addison–Wesley Publishing Co., Reading, Mass.
    (1958).
8.  Moulton, F. R., <span class="i">Introduction to Celestial
    Mechanics,</span> 2nd. ed., The Macmillan Book Co., New York (1914).
9.  Osgood, W. F., <span class="i">Mechanics,</span> The Macmillan Book
    Co., New York (1948).
10. Rosser, J. B., R. R. Newton, and G. L. Gross,
    <span class="i">Mathematical Theory of Rocket Flight,</span>
    McGraw–Hill Book Co., New York (1947).
11. Routh, E. J., <span class="i">Advanced Dynamics of a System of Rigid
    Bodies,</span> 6th ed., The Macmillan Book Co., London (1905).
    Reprinted by Dover Publications.
12. Scarborough, J. B., <span class="i">The Gyroscope,</span>
    Interscience Publishers, New York (1958).
13. Seifert, H. S., <span class="i">et al., Space Technology,</span>
    John Wiley and Sons, New York (1959).
14. Smart, E. H., <span class="i">Advanced Dynamics,</span> The
    Macmillan Book Co., New York (1951).
15. Sommerfeld, A., <span class="i">Mechanics,</span> Academic Press,
    New York (1952).
16. Synge, J. L., and B. A. Griffith, <span class="i">Principles of
    Mechanics,</span> 3rd ed., McGraw–Hill Book Co., New York (1959).
17. Timoshenko, S., and D. H. Young, <span class="i">Advanced
    Dynamics,</span> McGraw–Hill Book Co., New York (1948).
18. Webster, A. G., <span class="i">The Dynamics of Particles,</span>
    2nd ed. B. G. Teubner, Leipzig, (1912). Reprinted by Dover
    Publications.

</div>

<span id="e9780486140520_app01.html"></span>

<div class="appendix">

<span id="e9780486140520_app01.html_title130"></span>

# <span class="b">APPENDIX A</span>

# <span class="b">Matrices</span>

A system of linear equations

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1635.jpg](images/e9780486140520_i1635.jpg)

</div>

<div class="caption">

(A—1)

</div>

</div>

can be arranged into the matrix notation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1636.jpg](images/e9780486140520_i1636.jpg)

</div>

<div class="caption">

(A–2)

</div>

</div>

where the rule for the matrix multiplication is evident from the
original equations. For Eq. A–2 to equal Eq. A—1, the terms of each row
must be multiplied by the terms of the column x<sub>1</sub>,
x<sub>2</sub>, x<sub>3</sub>. We can then view the matrix equation, Eq.
A–2, as a convenient notation which may be further abbreviated to

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1637.jpg](images/e9780486140520_i1637.jpg)

</div>

<div class="caption">

(A–3)

</div>

</div>

We will next consider another set of linear equations like that of Eq.
A—1, relating <span class="i">x</span> to <span class="i">z</span>, and
write its matrix form as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1638.jpg](images/e9780486140520_i1638.jpg)

</div>

<div class="caption">

(A—4)

</div>

</div>

where \[<span class="i">b</span>\] is a square matrix like that of Eq.
A–2. If we wish to relate <span class="i">y</span> to
<span class="i">z</span>, Eq. A–4 can be substituted into Eq. A–3 as
follows:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1639.jpg](images/e9780486140520_i1639.jpg)

</div>

<div class="caption">

(A–5)

</div>

</div>

The elements of \[c\] can then be shown to be available from the
equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1640.jpg](images/e9780486140520_i1640.jpg)

</div>

<div class="caption">

(A–6)

</div>

</div>

i.e., the third element of the second row is

<div class="blocktext">

<span class="i">c</span><sub>23</sub> =
<span class="i">a</span><sub>21</sub><span class="i">b</span><sub>13</sub> +
<span class="i">a</span><sub>22</sub><span class="i">b</span><sub>23</sub> +
<span class="i">a</span><sub>23</sub><span class="i">b</span><sub>33</sub>

</div>

There are many theorems relating to the manipulation of matrix
equations; however for the purposes of linear transformation of
coordinates, as treated in this text, the simple algebraic concepts
discussed above are sufficient.

<div class="section1">

<span id="e9780486140520_app01.html_title131"></span>

# <span class="b">REFERENCES</span>

1.  Frazer, R. A., W. J. Duncan, and A. R. Collar,
    <span class="i">Elementary Matrices,</span> Cambridge University
    Press, New York (1938).
2.  Pipes, L. A., <span class="i">Applied Mathematics for Engineers and
    Physicists,</span> 2nd ed., McGraw–Hill Book Co., New York (1958),
    Chap. 4.

</div>

</div>

<span id="e9780486140520_app02.html"></span>

<div class="appendix">

<span id="e9780486140520_app02.html_title132"></span>

# <span class="b">APPENDIX B</span>

# <span class="b">Dyadics</span>

We occasionally encounter a quantity which has nine components in a
three–dimensional space. In elasticity we encounter nine components of
stress at a point, whereas in dynamics we find nine components of
inertia.

For our purposes we can define a dyadic as a nine–component quantity
which can be formed by multiplying two vectors, ignoring the dot–or
cross–product rule. Thus the product of two vectors
<span class="b">a</span> and <span class="b">b</span> is,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1641.jpg](images/e9780486140520_i1641.jpg)

</div>

<div class="caption">

(B—1)

</div>

</div>

Although the above dyadic was formed by the multiplication of the two
vectors a and b, the elements of the dyadic (called dyads) need not be
related to the two vectors. Furthermore, it is convenient to arrange
such terms in matrix form, so that a dyadic is in general expressible
as,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1642.jpg](images/e9780486140520_i1642.jpg)

</div>

<div class="caption">

(B–2)

</div>

</div>

As an example of a dyadic not related to any vector, we have the inertia
dyadic,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1643.jpg](images/e9780486140520_i1643.jpg)

</div>

<div class="caption">

(B–3)

</div>

</div>

To illustrate the general rule for the dot or cross product of a dyadic
with a vector, we assume that the dyadic is formed by the product of two
vectors as

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1644.jpg](images/e9780486140520_i1644.jpg)

</div>

<div class="caption">

(B–4)

</div>

</div>

Its dot and cross product with a vector <span class="b">r</span> is then
dependent on the order of the product, and its interpretation is made
clear by the following examples:

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1645.jpg](images/e9780486140520_i1645.jpg)

</div>

<div class="caption">

(B–5)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1646.jpg](images/e9780486140520_i1646.jpg)

</div>

<div class="caption">

(B–6)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1647.jpg](images/e9780486140520_i1647.jpg)

</div>

<div class="caption">

(B–7)

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1648.jpg](images/e9780486140520_i1648.jpg)

</div>

<div class="caption">

(B–8)

</div>

</div>

If we form the dot product of the inertia dyadic with the angular
velocity vector <span class="b">ω</span> =
<span class="i">ω</span><sub><span class="i">x</span></sub><span class="b">i</span> +
<span class="i">ω</span><sub><span class="i">y</span></sub><span class="b">j</span> +
<span class="i">ω</span><sub><span class="i"><span class="b">z</span></span></sub><span class="b">k</span>,
the result will be the angular momentum vector.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1649.jpg](images/e9780486140520_i1649.jpg)

</div>

<div class="caption">

(B–9)

</div>

</div>

Here we encounter dot products such as,

<div class="blocktext">

<span class="b">ji</span> • <span class="b">i</span> =
<span class="b">j</span>(<span class="b">i</span> •
<span class="b">i</span>) = <span class="b">j</span>  
<span class="b">ji</span> • <span class="b">j</span> =
<span class="b">j</span>(<span class="b">i</span> •
<span class="b">j</span>) = 0, etc.

</div>

which are evident from the general rule, and recognize that the
subscripts of the inertia are interchangeable, i.e.,
<span class="i">I</span><sub><span class="i">xy</span></sub> =
<span class="i">I</span><sub><span class="i">yx</span></sub>. If,
furthermore, we dot the angular velocity vector into the angular
momentum vector, the result is a scalar, which in this case is twice the
kinetic energy.

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1650.jpg](images/e9780486140520_i1650.jpg)

</div>

<div class="caption">

(B–10)

</div>

</div>

In summary, the dyadic is a special form of a tensor; however, our
simple definition of the dyadic and its product with a vector requires
no new rules of vector algebra, which appears to be adequate for the
dynamical problems encountered in this text. For further reading on the
subject, see reference.

<div class="section1">

<span id="e9780486140520_app02.html_title133"></span>

# <span class="b">REFERENCE</span>

<div class="endnotes">

<div class="endnote">

<a href="#e9780486140520_c04.html#ref_end_en1"
id="e9780486140520_app02.html_end_en1">1</a>

Weatherburn, C. E., <span class="i">Advanced Vector Analysis,</span> G.
Bell & Sons, Ltd., London (1947), Chapter 5, and p. 207.

</div>

</div>

</div>

</div>

<span id="e9780486140520_app03.html"></span>

<div class="appendix">

<span id="e9780486140520_app03.html_title134"></span>

# <span class="b">APPENDIX C</span>

# <span class="b">The Variational Calculus</span>

Many problems in Dynamics are formulated in terms of maxima and minima
of quantities expressed by an integral. In this section we will briefly
discuss the essentials of the variational calculus which are encountered
for such problems.

Consider the integral,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1651.jpg](images/e9780486140520_i1651.jpg)

</div>

<div class="caption">

(C—1)

</div>

</div>

taken along a curve <span class="i">z</span> =
ψ(<span class="i">t</span>). The quantity <span class="i">z</span> can
stand for any number of variables, such as position
<span class="i">x</span>, <span class="i">y</span>, and the thrust
attitude <span class="i">φ</span> of the missile problem. The value of
the integral <span class="i">I</span> will depend on the curve
<span class="i">z</span> =
<span class="i">ψ</span>(<span class="i">t</span>) which we wish to find
for the condition of maxima or minima of the integral C—1.

Assuming that <span class="i">z</span> = ψ(<span class="i">t</span>)
along curve <span class="i">ab</span> of
<a href="#e9780486140520_app03.html#int_146"
id="e9780486140520_app03.html_ref_int_146" class="ref_int">Fig. C-1</a>
to be the optimum curve, we draw curve 1 along
<span class="i">ab</span><sub>1</sub> as the varied curve. The quantity
z along the varied curve is represented by

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1652.jpg](images/e9780486140520_i1652.jpg)

</div>

<div class="caption">

(C–2)

</div>

</div>

where <span class="i">δz</span> is the variation of
<span class="i">z</span>. The variation <span class="i">δz</span>
differs from <span class="i">dz</span> in that <span class="i">dz</span>
is the increment along the curve <span class="i">z</span> due to an
increment <span class="i">dt</span>, whereas <span class="i">δz</span>
is the difference in the <span class="i">z</span> between the two curves
for any given time <span class="i">t</span>. We can also define the
difference in the slopes of the <span class="i">z</span> curves at any
time <span class="i">t</span> to be

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1653.jpg](images/e9780486140520_i1653.jpg)

</div>

<div class="caption">

(C–3)

</div>

</div>

If δz is assumed to be a continuous function of time, we can
differentiate Eq. C–2 and obtain

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1654.jpg](images/e9780486140520_i1654.jpg)

</div>

<div class="caption">

(C–4)

</div>

</div>

Comparing Eqs. C–3 and C–4, we find that

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1655.jpg](images/e9780486140520_i1655.jpg)

</div>

<div class="caption">

(C–5)

</div>

</div>

which indicates that the orders of operation of <span class="i">δ</span>
and d/<span class="i">dt</span> are interchangeable. Likewise, it can be
shown that the interchangeability rule applies to integrals.

<div class="illustype_image_text">

<div class="image_text">

![e9780486140520_i1656.jpg](images/e9780486140520_i1656.jpg)

</div>

<div class="caption">

<a href="#e9780486140520_app03.html#ref_int_146"
id="e9780486140520_app03.html_int_146" class="label_int"><span
class="b">Fig. C-1</span></a>. Curve (1) is the varied curve of
<span class="i">ab</span>.

</div>

</div>

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1657.jpg](images/e9780486140520_i1657.jpg)

</div>

<div class="caption">

(C–6)

</div>

</div>

With this understanding of <span class="i">b</span>, we now express f
along the varied curve by expanding it about the original curve. By
Taylor series we can write,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1658.jpg](images/e9780486140520_i1658.jpg)

</div>

<div class="caption">

(C–7)

</div>

</div>

Considering only the first order variation, the variation of the
integral <span class="i">I</span> is

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1659.jpg](images/e9780486140520_i1659.jpg)

</div>

<div class="caption">

(C–8)

</div>

</div>

The second term in this variation can be integrated by parts so that the
final expression for <span class="i">δI</span> becomes

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1660.jpg](images/e9780486140520_i1660.jpg)

</div>

<div class="caption">

(C–9)

</div>

</div>

For the curve <span class="i">z</span> = <span class="i">ψ(t)</span> to
be the optimum curve resulting in a maximum or minimum of
<span class="i">I</span>, the variation <span class="i">δI</span> must
equal zero.

Most texts treat the case where the variation <span class="i">δz</span>
is zero at the end points <span class="i">a</span> and
<span class="i">b</span> (i.e., <span class="i">b</span><sub>1</sub>
coincides with <span class="i">b</span>). In such cases the first term
of Eq. C–9 vanishes, and we are left only with the integral. Since
<span class="i">δz</span> in the integral is arbitrary and not zero over
the interval <span class="i">a</span> to <span class="i">b</span>, for
the integrand to be zero, <span class="i">δI</span> = 0, and we obtain
Euler’s equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1661.jpg](images/e9780486140520_i1661.jpg)

</div>

<div class="caption">

(C–10)

</div>

</div>

The satisfaction of Euler’s equation insures that the integral I is a
maximum or minimum. For the more general case where δz is not zero at
the end points, we must retain the first term and consider the entire
expression <span class="i">δI</span> = 0, of Eq. C–9.

<div class="section1">

<span id="e9780486140520_app03.html_title135"></span>

# <span class="b">Variation with Constraints</span>

We often encounter problems of optimization where the integral
<span class="i">I</span> must be maximized or minimized under conditions
of constraints,

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1662.jpg](images/e9780486140520_i1662.jpg)

</div>

<div class="caption">

(C—11)

</div>

</div>

The procedure to be followed is then to multiply the constraint
equations by arbitrary functions <span class="i">λ</span>, and maximize
or minimize the equation

<div class="illustype_image_math">

<div class="image_math">

![e9780486140520_i1663.jpg](images/e9780486140520_i1663.jpg)

</div>

<div class="caption">

(C–12)

</div>

</div>

which insures the satisfaction of the conditions of constraints in the
process of optimization. The quantities <span class="i">λ</span> are
also functions of the variables of the problem and, since they are
multiplied by zeros, the expression for <span class="i">I</span> is
unaltered. Equation C–9 is again applicable where
<span class="i">f</span> now stands for the entire integrand of Eq.
C—12.

</div>

</div>

<span id="e9780486140520_ind01.html"></span>

<div class="index">

<span id="e9780486140520_ind01.html_title136"></span>

# <span class="b">Index</span>

<div class="index_section">

Acceleration, components

<div class="index_section">

definition

of general motion

</div>

Accelerometer

Altitude of, launching

<div class="index_section">

rocket burnout

vertical coasting

</div>

Angular, momentum (moment of momentum)

<div class="index_section">

momentum ellipsoid

velocity referred to inertial coordinates

velocity vector

</div>

Angle of attack of missile

Anomaly

Antenna, energy dissipation of

Apogee

Apse line

Astronomical unit

Attitude control by flywheel

Attitude drift

</div>

<div class="index_section">

Ballistic, equation for missile

<div class="index_section">

flight time

range chart

trajectory

</div>

Beam vibration of missile

Bernoulli, Jean

Block diagram of, single axis platform

<div class="index_section">

three axis platform

</div>

Body fixed axes

<div class="index_section">

angular velocity of

</div>

Burnout velocity of rockets

</div>

<div class="index_section">

Center of mass, earth–moon system

Central force field

Charts for orbit computation

Chemical propellants

Circular orbit interception and rendezvous

Circular orbit speed

Coasting height of rockets

Coin spinning

Complex angle of attack

Complex angular velocity

Computer for inertial guidance

Cone, body

<div class="index_section">

space

</div>

Conic section

Conservation of energy

Conservation of momentum

Constraint

<div class="index_section">

equations for

forces

variational method with

</div>

Coordinate systems

<div class="index_section">

cyclic

transformation of

</div>

Coriolis acceleration

Coupling in three axis platform

Cross product

Crushable material

Cubic equation for symmetric gyro

</div>

<div class="index_section">

D’Alembert

Damped oscillation of gyrocompass

Degrees of freedom

Derivative of a vector

Despinning of satellites

Direct precession

Direction cosine

Directrix

Disk rolling on inclined plane

Displacement of a rigid body

Drift of body attitude

Drop test

Dyadics of inertia

</div>

<div class="index_section">

Earth, oblateness of

<div class="index_section">

precession of

</div>

Eccentric anomaly

Eccentricity, orbital

Ecliptic plane

Efficiency of rockets

Ellipse

<div class="index_section">

orbit transfer time

</div>

Ellipsoid of inertia

Elliptic integrals

Energy

<div class="index_section">

conservation of

dissipation effect on attitude

dissipation by hysteresis

kinetic

orbital

potential

</div>

Equations of, Euler

<div class="index_section">

Hamilton

Lagrange

</div>

Equatorial bulge

Equivalent mass of two body problem

Escape velocity

Euler’s, angles

<div class="index_section">

differential equation

moment equation

</div>

Euler’s, moment equation about principal axes

Exhaust velocity

</div>

<div class="index_section">

Flexible missile

Flight trajectory optimization

Focus

Forces, central

<div class="index_section">

conservative

of constraint

</div>

Fuel, rocket

</div>

<div class="index_section">

General motion of rigid body

Generalized coordinates

Generalized force

Generalized impulse

Generalized momentum

Geometry of conic sections

Gimbal, axis of gyro

<div class="index_section">

mass effect

walk

</div>

Gravitational constant for sun

Gravitational law

Gravitational torque

Gravity, torque of bodies

<div class="index_section">

torque due to oblateness

turn trajectory

</div>

Guidance, inertial

Gyroscope, cubic equation for

<div class="index_section">

gimbals with mass

precession and nutation

</div>

Gyropendulum

Gyropickoffs

</div>

<div class="index_section">

Hamilton

Heading angle

Heliocentric orbit

Herpolhode curve, cone

Hohmann transfer orbit

Holonomic system

Hydrogen fuel

Hyperbola

Hyperbolic transfer time

Hysteresis energy dissipation

</div>

<div class="index_section">

Impact, central

Impulse

<div class="index_section">

specific of fuel

</div>

Impulsive, equation of Lagrange

<div class="index_section">

moment on gyro

</div>

Inertia, dyadic

<div class="index_section">

ellipsoid

moment of

product of

</div>

Inertial, coordinates

<div class="index_section">

guidance

navigation

</div>

Initial conditions for satellite injection

Injection velocity

Instantaneous burning of fuel.

Instantaneous center

Instruments, gyroscopic

Integrating gyro

Interception of satellite, circular orbit

<div class="index_section">

elliptic orbit

noncoplanar orbit

</div>

Invariable plane, line

Invariance, of kinetic energy

<div class="index_section">

of moment of momentum

</div>

</div>

<div class="index_section">

Jet damping of rocket

</div>

<div class="index_section">

Kepler’s equation

<div class="index_section">

law

</div>

Kinetic energy, in generalized coordinates

<div class="index_section">

of rigid bodies

of two body system

</div>

</div>

<div class="index_section">

Lagrange

<div class="index_section">

equations

equations for impulsive force

equations for rotating coordinates

multiplier

</div>

Lagrangian

Launching parameters

Line integral

Linear equation with variable coefficients

</div>

<div class="index_section">

Mass, definition of

Mass ratio of rocket

Matrices

Missile dynamics

Moment

<div class="index_section">

of inertia

of momentum

</div>

Moment, of a vector

Moments for steady precession of gyro

Momentum, conservation of

<div class="index_section">

linear

sphere

theorems

</div>

Motion, about body axes

<div class="index_section">

about a fixed point

due to central forces

under zero moment

</div>

</div>

<div class="index_section">

Navigation, inertial

Navigation errors

Near symmetric body

<div class="index_section">

inertia relationship

motion referred to inertial coordinates

</div>

Newton’s law of gravitation

Newton’s laws of motion

Node line

Noncoplanar orbit interception

Nonholonomic system

Nonlinear equation techniques

Normal modes

Nutation of earth

</div>

<div class="index_section">

Oblateness of earth

Optimization of, multistage payload

<div class="index_section">

thrust attitude

</div>

Orbit, change due to impulse

<div class="index_section">

computation charts

eccentricity

equation

parameters

transfer time

</div>

Ore crusher

Oscillation of, navigation errors

<div class="index_section">

symmetric gyro

</div>

</div>

<div class="index_section">

Parabola

Particle

Particle dynamics

Payload

Pendulum, centrifugal

<div class="index_section">

double

Schuler

spherical

tuned

</div>

Performance, of rockets

<div class="index_section">

multistage optimization

powered trajectory

</div>

Perigee

Period of elliptic orbit

Perturbation, of orbit parameters

<div class="index_section">

technique for nonlinear systems

</div>

Pickoff, gyro

Plane motion

Planets, distances from sun

<div class="index_section">

orbits of

</div>

Poinsot ’s geometric solution

Poinsot’s ellipsoid

Polar coordinates

Polhode curves, cones

Position error of platform

Potential

Potential energy

Powered flight trajectory

Precession

<div class="index_section">

of earth

</div>

Principal axes

Propellant, mass

<div class="index_section">

specific impulse

sloshing

types

utilization

</div>

</div>

<div class="index_section">

Radial components of velocity, acceleration

Radius of curvature

Range, ballistic

Rate gyro

Ratio, mass

<div class="index_section">

thrust

</div>

Regression of node line

Relative motion

<div class="index_section">

to rotating earth

</div>

Rendezvous of satellites

Resolution of platform torque

Resonance of spinning antenna

Restitution, coefficient of

Retrograde precession

Rheonomic

Right–handed coordinate system

Rigid body

<div class="index_section">

kinetic energy of

</div>

Rocket, efficiency

<div class="index_section">

multistage

theory

</div>

Rolling of disk

Rotated coordinates

<div class="index_section">

moments and products of inertia about

</div>

Rotating curve

Rotation referred to inertial coordinates

</div>

<div class="index_section">

Satellite, interception

<div class="index_section">

launching conditions

orbits

rendezvous

</div>

Scalar dot product

Scalar quantity

Schuler pendulum

Scleronomic

Semimajor, minor axes of ellipse

Simple pendulum

Single axis platform

Single stage rocket

Sleeping top

Small oscillations of gyros

Solar system

Solid fuel

Solution by Laplace transform

Space, equations of motion

<div class="index_section">

vehicle motion

</div>

Specific impulse of fuels

Spin requirement for gyro

Spinning disk

Spinning rocket

Stable platform

Stability, energy consideration of

<div class="index_section">

of orbits

of rotation about principal axes

</div>

Staging of rockets

Steady precession of gyros

Structural damping

Structural factor for rockets

</div>

<div class="index_section">

Thrust, attitude of

<div class="index_section">

misalignment

ratio of rockets

of rockets

</div>

Time of ballistic flight

Time of orbit travel

Trajectory, gravity turn

<div class="index_section">

optimum

</div>

Transfer, functions for platforms

<div class="index_section">

matrix

</div>

Transfer orbit, coaxial ellipse

<div class="index_section">

Hohmann

hyperbolic

noncoplanar

time

</div>

Transformation of, coordinates

<div class="index_section">

moments and products of inertia

velocity

</div>

Transverse components, velocity and acceleration

Tumbling, rate of

Tuned absorber

Two body problem

</div>

<div class="index_section">

Undetermined multipliers

Unit vector

</div>

<div class="index_section">

Variable mass body

Variational method

Vector properties, addition

<div class="index_section">

bound

components

</div>

Vector properties, cross products

<div class="index_section">

derivative of

dot product

free

moment of

multiple product of

quantity

rectangular components

resolution

</div>

Vehicle motion, effect on gyrocompass

Velocity, definition

Velocity impulse for Hohmann transfer

Vibration of missiles

Virtual work

</div>

<div class="index_section">

Weight

Work

<div class="index_section">

virtual

</div>

</div>

<div class="index_section">

Zero lift trajectory

</div>

</div>

<span id="e9780486140520_bm02.html"></span>

<div class="backMatter">

<span id="e9780486140520_bm02.html_title137"></span>

# <span class="b">A CATALOG OF SELECTED DOVER BOOKS IN SCIENCE AND MATHEMATICS</span>

<div class="illustype_image">

<div class="image">

![e9780486140520_i1664.jpg](images/e9780486140520_i1664.jpg)

</div>

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title138"></span>

# <span class="i"><span class="b">Astronomy</span></span>

BURNHAM’S CELESTIAL HANDBOOK, Robert Burnham, Jr. Thorough guide to the
stars beyond our solar system. Exhaustive treatment. Alphabetical by
constellation: Andromeda to Cetus in Vol. 1; Chamaeleon to Orion in Vol.
2; and Pavo to Vulpecula in Vol. 3. Hundreds of illustrations. Index in
Vol. 3. 2,000pp. 6⅛ x 9¼.

23567–X, 23568–8, 23673–0 Three–vol. set

  
  
THE EXTRATERRESTRIAL LIFE DEBATE, 1750–1900, Michael J. Crowe. First
detailed, scholarly study in English of the many ideas that developed
from 1750 to 1900 regarding the existence of intelligent
extraterrestrial life. Examines ideas of Kant, Herschel, Voltaire,
Percival Lowell, many other scientists and thinkers. 16 illustrations.
704pp. 5⅜ x 8½

40675–X

  
  
A HISTORY OF ASTRONOMY, A. Pannekoek. Well–balanced, carefully reasoned
study covers such topics as Ptolemaic theory, work of Copernicus,
Kepler, Newton, Eddington’s work on stars, much more. Illustrated.
References. 521pp. 5⅜ x 8½.

65994–1

  
  
AMATEUR ASTRONOMER’S HANDBOOK, J. B. Sidgwick. Timeless, comprehensive
coverage of telescopes, mirrors, lenses, mountings, telescope drives,
micrometers, spectroscopes, more. 189 illustrations. 576pp. 5⅜ x 8¼.
(Available in U.S. only.)

24034–7

  
  
STARS AND RELATIVITY, Ya. B. Zel’dovich and I. D. Novikov. Vol. 1 of
<span class="i">Relativistic Astrophysics</span> by famed Russian
scientists. General relativity, properties of matter under astrophysical
conditions, stars, and stellar systems. Deep physical insights, clear
presentation. 1971 edition. References. 544pp. 5⅜ x 8¼.

69424–0

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title139"></span>

# <span class="i"><span class="b">Chemistry</span></span>

CHEMICAL MAGIC, Leonard A. Ford. Second Edition, Revised by E. Winston
Grundmeier. Over 100 unusual stunts demonstrating cold fire, dust
explosions, much more. Text explains scientific principles and stresses
safety precautions. 128pp. 5⅜ x 8½.

67628–5

  
  
THE DEVELOPMENT OF MODERN CHEMISTRY, Aaron J. Ihde. Authoritative
history of chemistry from ancient Greek theory to 20th–century
innovation. Covers major chemists and their discoveries. 209
illustrations. 14 tables. Bibliographies. Indices. Appendices. 851pp. 5⅜
x 8½.

64235–6

  
  
CATALYSIS IN CHEMISTRY AND ENZYMOLOGY, William P. Jencks. Exceptionally
clear coverage of mechanisms for catalysis, forces in aqueous solution,
carbonyl–and acyl–group reactions, practical kinetics, more. 864pp. 5⅜ x
8½.

65460–5

THE HISTORICAL BACKGROUND OF CHEMISTRY, Henry M. Leicester. Evolution of
ideas, not individual biography. Concentrates on formulation of a
coherent set of chemical laws. 260pp. 5⅜ x 8½.

61053–5

  
  
A SHORT HISTORY OF CHEMISTRY, J. R. Partington. Classic exposition
explores origins of chemistry, alchemy, early medical chemistry, nature
of atmosphere, theory of valency, laws and structure of atomic theory,
much more. 428pp. 5⅜ x 8½. (Available in U.S. only.)

65977–1

  
  
GENERAL CHEMISTRY, Linus Pauling. Revised 3rd edition of classic
first–year text by Nobel laureate. Atomic and molecular structure,
quantum mechanics, statistical mechanics, thermodynamics correlated with
descriptive chemistry. Problems. 992pp. 5⅜ x 8½.

65622–5

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title140"></span>

# <span class="i"><span class="b">Engineering</span></span>

DE RE METALLICA, Georgius Agricola. The famous Hoover translation of
greatest treatise on technological chemistry, engineering, geology,
mining of early modern times (1556). All 289 original woodcuts. 638pp.
6¾ x 11.

60006–8

  
  
FUNDAMENTALS OF ASTRODYNAMICS, Roger Bate et al. Modern approach
developed by U.S. Air Force Academy. Designed as a first course.
Problems, exercises. Numerous illustrations. 455pp. 5⅜ x 8½.

60061–0

DYNAMICS OF FLUIDS IN POROUS MEDIA, Jacob Bear. For advanced students of
ground water hydrology, soil mechanics and physics, drainage and
irrigation engineering and more. 335 illustrations. Exercises, with
answers. 784pp. 6⅛ x 9¼.

65675–6

  
  
ANALYTICAL MECHANICS OF GEARS, Earle Buckingham. Indispensable reference
for modern gear manufacture covers conjugate gear–tooth action,
gear–tooth profiles of various gears, many other topics. 263 figures.
102 tables. 546pp. 5⅜ x 8½.

65712–4

  
  
MECHANICS, J. P. Den Hartog. A classic introductory text or refresher.
Hundreds of applications and design problems illuminate fundamentals of
trusses, loaded beams and cables, etc. 334 answered problems. 462pp. 5⅜
x 8½.

60754–2

  
  
MECHANICAL VIBRATIONS, J. P. Den Hartog. Classic textbook offers lucid
explanations and illustrative models, applying theories of vibrations to
a variety of practical industrial engineering problems. Numerous
figures. 233 problems, solutions. Appendix. Index. Preface. 436pp. 5⅜ x
8½.

64785–4

  
  
STRENGTH OF MATERIALS, J. P. Den Hartog. Full, clear treatment of basic
material (tension, torsion, bending, etc.) plus advanced material on
engineering methods, applications. 350 answered problems. 323pp. 5⅜ x
8½.

60755–0

  
  
A HISTORY OF MECHANICS, René Dugas. Monumental study of mechanical
principles from antiquity to quantum mechanics. Contributions of ancient
Greeks, Galileo, Leonardo, Kepler, Lagrange, many others. 671pp. 5⅜ x
8½.

65632–2

METAL FATIGUE, N. E. Frost, K.J. Marsh, and L. P. Pook. Definitive,
clearly written, and well–illustrated volume addresses all aspects of
the subject, from the historical development of understanding metal
fatigue to vital concepts of the cyclic stress that causes a crack to
grow. Includes 7 appendixes. 544pp. 5⅜ x 8½.

40927–9

  
  
STATISTICAL MECHANICS: Principles and Applications, Terrell L. Hill.
Standard text covers fundamentals of statistical mechanics, applications
to fluctuation theory, imperfect gases, distribution functions, more.
448pp. 5⅜ x 8½.

65390–0

  
  
THE VARIATIONAL PRINCIPLES OF MECHANICS, Cornelius Lanczos. Graduate
level coverage of calculus of variations, equations of motion,
relativistic mechanics, more. First inexpensive paperbound edition of
classic treatise. Index. Bibliography. 418pp. 5⅜ x 8½.

65067–7

THE VARIOUS AND INGENIOUS MACHINES OF AGOSTINO RAMELLI: A Classic
Sixteenth–Century Illustrated Treatise on Technology, Agostino Ramelli.
One of the most widely known and copied works on machinery in the 16th
century. 194 detailed plates of water pumps, grain mills, cranes, more.
608pp. 9 x 12.

28180–9

  
  
ORDINARY DIFFERENTIAL EQUATIONS AND STABILITY THEORY: An Introduction,
David A. Sanchez. Brief, modern treatment. Linear equation, stability
theory for autonomous and nonautonomous systems, etc. 164pp. 5⅜ x 8¼.

63828–6

  
  
ROTARY WING AERODYNAMICS, W. Z. Stepniewski. Clear, concise text covers
aerodynamic phenomena of the rotor and offers guidelines for helicopter
performance evaluation. Originally prepared for NASA. 537 figures.
640pp. 6⅛ x 9¼.

64647–5

  
  
INTRODUCTION TO SPACE DYNAMICS, William Tyrrell Thomson. Comprehensive,
classic introduction to space–flight engineering for advanced
undergraduate and graduate students. Includes vector algebra,
kinematics, transformation of coordinates. Bibliography. Index. 352pp.
5⅜ x 8½.

65113–4

  
  
HISTORY OF STRENGTH OF MATERIALS, Stephen P. Timoshenko. Excellent
historical survey of the strength of materials with many references to
the theories of elasticity and structure. 245 figures. 452pp. 5⅜ x 8½.

61187–6

  
  
ANALYTICAL FRACTURE MECHANICS, David J. Unger. Self–contained text
supplements standard fracture mechanics texts by focusing on analytical
methods for determining crack–tip stress and strain fields. 336pp. 6⅛ x
9¼.

41737–9

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title141"></span>

# <span class="i"><span class="b">Mathematics</span></span>

HANDBOOK OF MATHEMATICAL FUNCTIONS WITH FORMULAS, GRAPHS, AND
MATHEMATICAL TABLES, edited by Milton Abramowitz and Irene A. Stegun.
Vast compendium: 29 sets of tables, some to as high as 20 places.
1,046pp. 8 x 10½.

61272–4

  
  
APPLIED COMPLEX VARIABLES, John W. Dettman. Step–by–step coverage of
fundamentals of analytic function theory–plus lucid exposition of five
important applications: Potential Theory; Ordinary Differential
Equations; Fourier Transforms; Laplace Transforms; Asymptotic
Expansions. 66 figures. Exercises at chapter ends. 512pp. 5⅜ x 8½.

64670–X

  
  
INTRODUCTION TO LINEAR ALGEBRA AND DIFFERENTIAL EQUATIONS, John W.
Dettman. Excellent text covers complex numbers, determinants,
orthonormal bases, Laplace transforms, much more. Exercises with
solutions. Undergraduate level. 416pp. 5⅜ x 8½.

65191–6

  
  
MATHEMATICAL METHODS IN PHYSICS AND ENGINEERING, John W. Dettman.
Algebraically based approach to vectors, mapping, diffraction, other
topics in applied math. Also generalized functions, analytic function
theory, more. Exercises. 448pp. 5⅜ x 8¼.

65649–7

  
  
CALCULUS OF VARIATIONS WITH APPLICATIONS, George M. Ewing.
Applications–oriented introduction to variational theory develops
insight and promotes understanding of specialized books, research
papers. Suitable for advanced undergraduate/graduate students as
primary, supplementary text. 352pp. 5⅜ x 8½.

64856–7

  
  
COMPLEX VARIABLES, Francis J. Flanigan. Unusual approach, delaying
complex algebra till harmonic functions have been analyzed from real
variable viewpoint. Includes problems with answers. 364pp. 5⅜ x 8½.

61388–7

  
  
AN INTRODUCTION TO THE CALCULUS OF VARIATIONS, Charles Fox.
Graduate–level text covers variations of an integral, isoperimetrical
problems, least action, special relativity, approximations, more.
References. 279pp. 5⅜ x 8½.

65499–0

  
  
CATASTROPHE THEORY FOR SCIENTISTS AND ENGINEERS, Robert Gilmore.
Advanced–level treatment describes mathematics of theory grounded in the
work of Poincaré, R. Thom, other mathematicians. Also important
applications to problems in mathematics, physics, chemistry and
engineering. 1981 edition. References. 28 tables. 397 black–and–white
illustrations. xvii + 666pp. 6⅛ x 9¼.

67539–4

  
  
INTRODUCTION TO DIFFERENCE EQUATIONS, Samuel Goldberg. Exceptionally
clear exposition of important discipline with applications to sociology,
psychology, economics. Many illustrative examples; over 250 problems.
260pp. 5⅜ x 8½.

65084–7

  
  
NUMERICAL METHODS FOR SCIENTISTS AND ENGINEERS, Richard Hamming. Classic
text stresses frequency approach in coverage of algorithms, polynomial
approximation, Fourier approximation, exponential approximation, other
topics. Revised and enlarged 2nd edition. 721pp. 5⅜ x 8½.

65241–6

  
  
INTRODUCTION TO NUMERICAL ANALYSIS (2nd Edition), F. B. Hildebrand.
Classic, fundamental treatment covers computation, approximation,
interpolation, numerical differentiation and integration, other topics.
150 new problems. 669pp. 5⅜ x 8½.

65363–3

  
  
THE FUNCTIONS OF MATHEMATICAL PHYSICS, Harry Hochstadt. Comprehensive
treatment of orthogonal polynomials, hypergeometric functions, Hill’s
equation, much more. Bibliography. Index. 322pp. 5⅜ x 8½.

65214–9

  
  
THREE PEARLS OF NUMBER THEORY, A. Y. Khinchin. Three compelling puzzles
require proof of a basic law governing the world of numbers. Challenges
concern van der Waerden’s theorem, the Landau–Schnirelmann hypothesis
and Mann’s theorem, and a solution to Waring’s problem. Solutions
included. 64pp. 5⅜ x 8⅛.

40026–3

  
  
CALCULUS REFRESHER FOR TECHNICAL PEOPLE, A. Albert Klaf. Covers
important aspects of integral and differential calculus via 756
questions. 566 problems, most answered. 431pp. 5⅜ x 8½.

20370–0

  
  
THE PHILOSOPHY OF MATHEMATICS: An Introductory Essay, Stephan Körner.
Surveys the views of Plato, Aristotle, Leibniz & Kant concerning
propositions and theories of applied and pure mathematics. Introduction.
Two appendices. Index. 198pp. 5⅜ x 8½.

25048–2

  
  
INTRODUCTORY REAL ANALYSIS, A.N. Kolmogorov, S. V. Fomin. Translated by
Richard A. Silverman. Self–contained, evenly paced introduction to real
and functional analysis. Some 350 problems. 403pp. 5⅜ x 8½.

61226–0

  
  
APPLIED ANALYSIS, Cornelius Lanczos. Classic work on analysis and design
of finite processes for approximating solution of analytical problems.
Algebraic equations, matrices, harmonic analysis, quadrature methods,
much more. 559pp. 5⅜ x 8½.

65656–X

  
  
AN INTRODUCTION TO ALGEBRAIC STRUCTURES, Joseph Landin. Superb
self–contained text covers “abstract algebra”: sets and numbers, theory
of groups, theory of rings, much more. Numerous well–chosen examples,
exercises. 247pp. 5⅜ x 8½.

65940–2

  
  
SPECIAL FUNCTIONS, N. N. Lebedev. Translated by Richard Silverman.
Famous Russian work treating more important special functions, with
applications to specific problems of physics and engineering. 38
figures. 308pp. 5⅜ x 8½.

60624–4

  
  
QUALITATIVE THEORY OF DIFFERENTIAL EQUATIONS, V. V. Nemytskii and V.V.
Stepanov. Classic graduate–level text by two prominent Soviet
mathematicians covers classical differential equations as well as
topological dynamics and ergodic theory. Bibliographies. 523pp. 5⅜ x 8½.

65954–2

  
  
NUMBER THEORY AND ITS HISTORY, Oystein Ore. Unusually clear, accessible
introduction covers counting, properties of numbers, prime numbers, much
more. Bibliography. 380pp. 5⅜ x 8½.

65620–9

THEORY OF MATRICES, Sam Perlis. Outstanding text covering rank,
nonsingu–larity and inverses in connection with the development of
canonical matrices under the relation of equivalence, and without the
intervention of determinants. Includes exercises. 237pp. 5⅜ x 8½.

66810–X

  
  
POPULAR LECTURES ON MATHEMATICAL LOGIC, Hao Wang. Noted logician’s lucid
treatment of historical developments, set theory, model theory,
recursion theory and constructivism, proof theory, more. 3 appendixes.
Bibliography. 1981 edition. ix + 283pp. 5⅜ x 8½.

67632–3

  
  
CALCULUS OF VARIATIONS, Robert Weinstock. Basic introduction covering
isoperimetric problems, theory of elasticity, quantum mechanics,
electrostatics, etc. Exercises throughout. 326pp. 5⅜ x 8½.

63069–2

  
  
THE CONTINUUM: A Critical Examination of the Foundation of Analysis,
Hermann Weyl. Classic of 20th–century foundational research deals with
the conceptual problem posed by the continuum. 156pp. 5⅜ x 8½.

67982–9

  
  
CHALLENGING MATHEMATICAL PROBLEMS WITH ELEMENTARY SOLUTIONS, A. M.
Yaglom and I. M. Yaglom. Over 170 challenging problems on probability
theory, combinatorial analysis, points and lines, topology, convex
polygons, many other topics. Solutions. Total of 445pp. 5⅜ x 8½.
Two–vol. set.

Vol. I: 65536–9 Vol. II: 65537–7

  
  
A SURVEY OF NUMERICAL MATHEMATICS, David M. Young and Robert Todd
Gregory. Broad self–contained coverage of computer–oriented numerical
algorithms for solving various types of mathematical problems in linear
algebra, ordinary and partial, differential equations, much more.
Exercises. Total of 1,248pp. 5⅜ x 8½. Two volumes.

Vol. I: 65691–8 Vol. II: 65692–6

  
  
INTRODUCTION TO PARTIAL DIFFERENTIAL EQUATIONS WITH APPLICATIONS, E. C.
Zachmanoglou and Dale W. Thoe. Essentials of partial differential
equations applied to common problems in engineering and the physical
sciences. Problems and answers. 416pp. 5⅜ x 8½.

65251–3

  
  
THE THEORY OF GROUPS, Hans J. Zassenhaus. Well–written graduate–level
text acquaints reader with group–theoretic methods and demonstrates
their usefulness in mathematics. Axioms, the calculus of complexes,
homomorphic mapping, p–group theory, more. Many proofs shorter and more
transparent than older ones. 276pp. 5⅜ x 8½.

40922–8

  
  
DISTRIBUTION THEORY AND TRANSFORM ANALYSIS: An Introduction to
Generalized Functions, with Applications, A. H. Zemanian. Provides
basics of distribution theory, describes generalized Fourier and Laplace
transformations. Numerous problems. 384pp. 5⅜ x 8½.

65479–6

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title142"></span>

# <span class="i"><span class="b">Math–Decision Theory, Statistics, Probability</span></span>

ELEMENTARY DECISION THEORY, Herman Chernoff and Lincoln E. Moses. Clear
introduction to statistics and statistical theory covers data
processing, probability and random variables, testing hypotheses, much
more. Exercises. 364pp. 5⅜ x 8½.

65218–1

</div>

<div class="section1">

<span id="e9780486140520_bm02.html_title143"></span>

# <span class="b">Physics</span>

OPTICAL RESONANCE AND TWO–LEVEL ATOMS, L. Allen and J. H. Eberly. Clear,
comprehensive introduction to basic principles behind all quantum
optical resonance phenomena. 53 illustrations. Preface. Index. 256pp. 5⅜
x 8½.

65533–4

  
  
ULTRASONIC ABSORPTION: An Introduction to the Theory of Sound Absorption
and Dispersion in Gases, Liquids and Solids, A. B. Bhatia. Standard
reference in the field provides a clear, systematically organized
introductory review of fundamental concepts for advanced graduate
students, research workers. Numerous diagrams. Bibliography. 440pp. 5⅜ x
8½.

64917–2

  
  
QUANTUM THEORY, David Bohm. This advanced undergraduate–level text
presents the quantum theory in terms of qualitative and imaginative
concepts, followed by specific applications worked out in mathematical
detail. Preface. Index. 655pp. 5⅜ x 8½.

65969–0

  
  
ATOMIC PHYSICS (8th edition), Max Born. Nobel laureate’s lucid treatment
of kinetic theory of gases, elementary particles, nuclear atom,
wave–corpuscles, atomic structure and spectral lines, much more. Over 40
appendices, bibliography. 495pp. 5⅜ x 8½

65984–4

  
  
AN INTRODUCTION TO HAMILTONIAN OPTICS, H. A. Buchdahl. Detailed account
of the Hamiltonian treatment of aberration theory in geometrical optics.
Many classes of optical systems defined in terms of the symmetries they
possess. Problems with detailed solutions. 1970 edition. xv + 360pp. 5⅜
x 8½.

67597–1

  
  
THIRTY YEARS THAT SHOOK PHYSICS: The Story of Quantum Theory, George
Gamow. Lucid, accessible introduction to influential theory of energy
and matter. Careful explanations of Dirac’s anti–particles, Bohr’s model
of the atom, much more. 12 plates. Numerous drawings. 240pp. 5⅜ x 8½.

24895–X

  
  
ELECTRONIC STRUCTURE AND THE PROPERTIES OF SOLIDS: The Physics of the
Chemical Bond, Walter A. Harrison. Innovative text offers basic
understanding of the electronic structure of covalent and ionic solids,
simple metals, transition metals and their compounds. Problems. 1980
edition. 582pp. 6⅛ x 9¼.

66021–4

  
  
HYDRODYNAMIC AND HYDROMAGNETIC STABILITY, S. Chandrasekhar. Lucid
examination of the Rayleigh–Benard problem; clear coverage of the theory
of instabilities causing convection. 704pp. 5⅜ x 8¼.

64071–X

  
  
INVESTIGATIONS ON THE THEORY OF THE BROWNIAN MOVEMENT, Albert Einstein.
Five papers (1905–8) investigating dynamics of Brownian motion and
evolving elementary theory. Notes by R. Furth. 122pp. 5⅜ x 8½.

60304–0

  
  
THE PHYSICS OF WAVES, William C. Elmore and Mark A. Heald. Unique
overview of classical wave theory. Acoustics, optics, electromagnetic
radiation, more. Ideal as classroom text or for self–study. Problems.
477pp. 5⅜ x 8½.

64926–1

METHODS OF THERMODYNAMICS, Howard Reiss. Outstanding text focuses on
physical technique of thermodynamics, typical problem areas of
understanding, and significance and use of thermodynamic potential. 1965
edition. 238pp. 5⅜ x 8½.

69445–3

  
  
TENSOR ANALYSIS FOR PHYSICISTS, J. A. Schouten. Concise exposition of
the mathematical basis of tensor analysis, integrated with well–chosen
physical examples of the theory. Exercises. Index. Bibliography. 289pp.
5⅜ x 8½.

65582–2

  
  
RELATIVITY IN ILLUSTRATIONS, Jacob T. Schwartz. Clear nontechnical
treatment makes relativity more accessible than ever before. Over 60
drawings illustrate concepts more clearly than text alone. Only high
school geometry needed. Bibliography. 128pp. 6⅛ x 9¼.

25965–X

  
  
THE ELECTROMAGNETIC FIELD, Albert Shadowitz. Comprehensive undergraduate
text covers basics of electric and magnetic fields, builds up to
electromagnetic theory. Also related topics, including relativity. Over
900 problems. 768pp. 5⅜ x 8¼.

65660–8

  
  
GREAT EXPERIMENTS IN PHYSICS: Firsthand Accounts from Galileo to
Einstein, edited by Morris H. Shamos. 25 crucial discoveries: Newton’s
laws of motion, Chadwick’s study of the neutron, Hertz on
electromagnetic waves, more. Original accounts clearly annotated. 370pp.
5⅜ x 8½.

25346–5

  
  
RELATIVITY, THERMODYNAMICS AND COSMOLOGY, Richard C. Tolman. Landmark
study extends thermodynamics to special, general relativity; also
applications of relativistic mechanics, thermodynamics to cosmological
models. 501pp. 5⅜ x 8½.

65383–8

  
  
LIGHT SCATTERING BY SMALL PARTICLES, H. C. van de Hulst. Comprehensive
treatment including full range of useful approximation methods for
researchers in chemistry, meteorology and astronomy. 44 illustrations.
470pp. 5⅜ x 8½.

64228–3

  
  
STATISTICAL PHYSICS, Gregory H. Wannier. Classic text combines
thermodynamics, statistical mechanics and kinetic theory in one unified
presentation of thermal physics. Problems with solutions. Bibliography.
532pp. 5⅜ x 8½.

65401–X

  
  
  
  
Paperbound unless otherwise indicated. Available at your book dealer,
online at
<span class="b">[www.doverpublications.com](http://www.doverpublications.com),</span>
or by writing to Dept. GI, Dover Publications, Inc., 31 East 2nd Street,
Mineola, NY 11501. For current price information or for free catalogues
(please indicate field of interest), write to Dover Publications or log
on to
<span class="b">[www.doverpublications.com](http://www.doverpublications.com)</span>
and see every Dover book in print. Dover publishes more than 500 books
each year on science, elementary and advanced mathematics, biology,
music, art, literary history, social sciences, and other areas.

</div>

</div>

<span id="e9780486140520_bm03.html"></span>

<div class="backMatter">

<span id="e9780486140520_bm03.html_title144"></span>

# <span class="b">DOVER BOOKS ON ASTRONOMY</span>

STAR Names: THEIR Lore AND MEANING, Richard H. Allen. (0–486–21079–0)

COPERNICUS AND Modern ASTRONOMY, Angus Armitage. (0–486–43907–0)

BURNHAM’S CELESTIAL Handbook, Robert Burnham, Jr. Three–volume set
(0–486–23567–X, 0–486–23568–8, 0–486–23673–0)

Comets: Speculation AND Discovery, Nigel Calder. (0–486–27879–4)

KEPLER, Max Caspar. (0–486–67605–6)

AN Introduction TO THE STUDY OF STELLAR STRUCTURE, S. Chandrasekhar.
(0–486–60413–6)

RADIATIVE Transfer, S. Chandrasekhar. (0–486–60590–6)

Exploring THE MOON Through BINOCULARS AND SMALL TELESCOPES, Ernest H.
Cherrington, Jr. (0–486–24491–1)

THE EXTRATERRESTRIAL LIFE DEBATE, 1750–1900, Michael J. Crowe.
(0–486–40675–X)

MODERN THEORIES of the UNIVERSE, from HERSCHEL TO HUBBLE, Michael J.
Crowe. (0–486–27880–8)

PLANETS, STARS AND Galaxies, A. E. Fanning. (0–486–21680–2)

DIALOGUES CONCERNING Two New Sciences, Galileo Galilei. (0–486–60099–8)

GREEK ASTRONOMY, Sir Thomas L. Heath. (0–486–26620–6)

THE Astronomical Revolution: COPERNICUS—KEPLER—BORELLI, Alexandre Koyré.
(Available in U.S. only.) (0–486–27095–5)

ASTROLOGY AND ASTRONOMY: A PICTORIAL Archive of SIGNS AND SYMBOLS, Ernst
and Johanna Lehner. (0–486–43981–X)

THE FRIENDLY STARS, Martha E. Martin and Donald H. Menzel.
(0–486–21099–5)

AN Introduction to CELESTIAL Mechanics, Forest Ray Moulton.
(0–486–64687–4)

A HISTORY of ASTRONOMY, A. Pannekoek. (0–486–65994–1)

THE STARRY Room: NAKED EYE ASTRONOMY IN THE INTIMATE Universe, Fred
Schaaf. (0–486–42553–3)

Wonders OF THE SKY: OBSERVING Rainbows, Comets, Eclipses, THE Stars AND
OTHER PHENOMENA, Fred Schaaf. (0–486–24402–4)

AMATEUR ASTRONOMER’S Handbook, J. B. Sidgwick. (Available in U.S. only.)
(0–486–24034–7)

STARS AND RELATIVITY, Ya B. Zel’dovich and I. D. Novikov.
(0–486–69424–0)

  
  
Paperbound unless otherwise indicated. Available at your book dealer,
online at
<span class="b">[www.doverpublications.com](http://www.doverpublications.com),</span>
or by writing to Dept. 23, Dover Publications, Inc., 31 East 2nd Street,
Mineola, NY 11501. For current price information or for free catalogs
(please indicate field of interest), write to Dover Publications or log
on to
<span class="b">[www.doverpublications.com](http://www.doverpublications.com)</span>
and see every Dover book in print. Each year Dover publishes over 500
books on fine art, music, crafts and needlework, antiques, languages,
literature, children’s books, chess, cookery, nature, anthropology,
science, mathematics, and other areas.

<span class="i">Manufactured in the U.S.A.</span>

</div>

<span id="e9780486140520_ftn01.html"></span>

<div class="footnotes">

<span id="e9780486140520_ftn01.html_title150"></span>

<div class="footnote">

<div class="illustype_image_math">

<div class="image_math">

</div>

</div>

<a href="#e9780486140520_c01.html#ref_ftn_fn1"
id="e9780486140520_ftn01.html_ftn_fn1">a</a>

A convenient notation to distinguish between differentiation in the
inertial and rotating coordinates is to use brackets, or parenthesis
around the latter, i.e.,

![e9780486140520_i0028.jpg](images/e9780486140520_i0028.jpg)

This notation will be used in this book.

</div>

<div class="footnote">

<a href="#e9780486140520_c02.html#ref_ftn_fn2"
id="e9780486140520_ftn01.html_ftn_fn2">b</a>

Differentiation relative to the moving coordinates is indicated by \[
\].

</div>

<div class="footnote">

<a href="#e9780486140520_c03.html#ref_ftn_fn3"
id="e9780486140520_ftn01.html_ftn_fn3">c</a>

See Appendix A.

</div>

<div class="footnote">

<a href="#e9780486140520_c03.html#ref_ftn_fn4"
id="e9780486140520_ftn01.html_ftn_fn4">d</a>

See Appendix A.

</div>

<div class="footnote">

<a href="#e9780486140520_c05.html#ref_ftn_fn5"
id="e9780486140520_ftn01.html_ftn_fn5">e</a>

See Appendix B.

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn6"
id="e9780486140520_ftn01.html_ftn_fn6">f</a>

To maintain symmetry two such masses are released.

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn7"
id="e9780486140520_ftn01.html_ftn_fn7">g</a>

u is the velocity of the jet relative to the nozzle. When it is positive
we have a retro–rocket. ṁ is negative for any rocket.

</div>

<div class="footnote">

<div class="blocktext">

</div>

<div class="blocktext">

</div>

<a href="#e9780486140520_c07.html#ref_ftn_fn8"
id="e9780486140520_ftn01.html_ftn_fn8">h</a>

The equation is in the form

<span class="imageinline">![e9780486140520_i1252.jpg](images/e9780486140520_i1252.jpg)</span> +
<span class="i">P</span>(<span class="i">t</span>)θ<sub>xy</sub> =
<span class="i">Q</span>(<span class="i">t</span>)

with solution

<span class="i">θ</span><sub><span class="i">xy</span></sub> = e−<sup>∫p
<span class="i">dt</span></sup>∫Qe<sup>∫P
<span class="i">dt</span></sup>dt + Ce<sup>−∫<span class="i">P
dt</span></sup>

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn9"
id="e9780486140520_ftn01.html_ftn_fn9">i</a>

In Ref. 9 the origin for the moment is chosen to coincide with the
center of mass and the various subbodies are considered to be rigid.
Also no provision is made for the variation of the total system mass.

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn10"
id="e9780486140520_ftn01.html_ftn_fn10">j</a>

u<sub><span class="i">i</span></sub> is negative when mass is ejected in
the opposite sense to Ṙ (see p. 221).

</div>

<div class="footnote">

<div class="blocktext">

</div>

<a href="#e9780486140520_c07.html#ref_ftn_fn11"
id="e9780486140520_ftn01.html_ftn_fn11">l</a>

This equation results from the application of the relationship

a × (b × c) = b(a ∙ c)–c(a ∙ b).

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn12"
id="e9780486140520_ftn01.html_ftn_fn12">k</a>

See Probs. 18 and 19 p. 111.

</div>

<div class="footnote">

<a href="#e9780486140520_c07.html#ref_ftn_fn13"
id="e9780486140520_ftn01.html_ftn_fn13">m</a>

Letting M<sub><span class="i">T</span></sub> = <span class="b">Σ
r</span><sub><span class="i">i</span></sub> × ṁ<sub>i</sub>u<sub>i</sub>
= moment of the thrusting jet, the moment acting on the varying mass is
M<sub>0</sub> + M<sub><span class="i">T</span></sub>.

</div>

<div class="footnote">

<a href="#e9780486140520_c08.html#ref_ftn_fn14"
id="e9780486140520_ftn01.html_ftn_fn14">n</a>

<span class="b">u</span> = − u

</div>

<div class="footnote">

<a href="#e9780486140520_c08.html#ref_ftn_fn15"
id="e9780486140520_ftn01.html_ftn_fn15">o</a>

Short Table of Integrals (3rd rev. ed), Ginn & Co., Boston (1929).

</div>

<div class="footnote">

<a href="#e9780486140520_c09.html#ref_ftn_fn16"
id="e9780486140520_ftn01.html_ftn_fn16">p</a>

Thomson, W. T., “Lagrange’s Equations for Moving Coordinates,” Space
Technology Laboratories Report No. <span class="i">EM 9–15
TR–59–000–00768</span>, Los Angeles (July 1959).

</div>

</div>
