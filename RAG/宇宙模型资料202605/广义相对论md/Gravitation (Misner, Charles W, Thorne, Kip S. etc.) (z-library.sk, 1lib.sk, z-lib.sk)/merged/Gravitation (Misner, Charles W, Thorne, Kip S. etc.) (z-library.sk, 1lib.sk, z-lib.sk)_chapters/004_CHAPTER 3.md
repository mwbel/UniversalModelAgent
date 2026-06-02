# CHAPTER 3

# THE ELECTROMAGNETIC FIELD

The rotating armatures of every generator and every motor in this age of electricity are steadily proclaiming the truth of the relativity theory to all who have ears to hear.

LEIGH PAGE (1941)

# $\pmb { \ S 3 . 1 }$ .THE LORENTZ FORCE AND THE ELECTROMAGNETIC FIELD TENSOR

At the opposite extreme from an impulsive change of momentum in a collision (the last topic of Chapter 2) is the gradual change in the momentum of a charged particle under the action of electric and magnetic forces (the topic treated here).

Let electric and magnetic fields act on a system of charged particles. The accelerations of the particles reveal the electric and magnetic field strengths.In other words, the Lorentz force law, plus measurements on the components of acceleration of test particles,can be viewed as defining the components of the electric and magnetic fields.Once the field components are known from the accelerations of a few test particles,they can be used to predict the accelerations of other test particles (Box 3.1).Thus the Lorentz force law does double service (l) as definer of fields and (2) as predicter of motions.

Lorentz force as definer of fields and predicter of motions

Here and elsewhere in science,as stressed not least by Henri Poincaré, that view is out of date which used to say,“Defne your terms before you proceed."Al the laws and theories of physics,including the Lorentz force law, have this deep and subtle character,that they both define the concepts they use (here $\pmb { B }$ and $\pmb { \cal E }$ ）and make statements about these concepts. Contrariwise, the absence of some body of theory, law,and principle deprives one of the means properly to define or even to use concepts. Any forward step in human knowledge is truly creative in this sense: that theory, concept, law,and method of measurement-forever inseparable-are born into the world in union.

# Box 3.1 LORENTZ FORCE LAW AS BOTH DEFINER OF FIELDS AND PREDICTER OF MOTIONS

How one goes about determining the components of the field from measurements of accelerations is not different in principle for electromagnetism and for gravitation. Compare the equations in the two cases:

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \tau ^ { 2 } } } = { \frac { e } { m } } F _ { ~ \beta } ^ { \alpha } u ^ { \beta } \mathrm { ~ i n ~ a ~ L o r e n t z ~ f r a m e } ,
$$

and

of reference parallel to the direction of motion of this second particle,which will then respond to and measure the components $\pmb { { \cal B } } _ { y }$ and $B _ { z }$ of the magnetic field. Not so $B _ { x }$ ！ The acceleration in the $x$ -direction merely remeasures the already once measured $E _ { z }$ .To evaluate $B _ { x } ,$ a third test particle is required,but it then gives duplicate information about the other field components.The alternative? Use all $N$ particles simultaneously and on the same democratic footing,both in the evaluation of the six $\underset { \bullet } { F } _ { \alpha \beta }$ and in the testing of the Lorentz force, by applying the method of least squares. Thus, write the discrepancy between predicted and observed acceleration of the Kth particle in the form

To make explicit the simpler procedure for electromagnetism will indicate in broad outline how one similarly determines all the components of $R ^ { \alpha } { } _ { \beta \gamma \delta }$ for gravity. Begin by asking how many test particles one needs to determine the three components of $\pmb { B }$ and the three components of $\pmb { { \cal E } }$ in the neighborhood under study.For one particle, three components of acceleration are measurable; for a second particle, three more. Enough? No! The information from the one duplicates in part the information from the other. The proof? Whatever the state of motion of the first test particle,pick one's Lorentz frame to be moving the same way. Having zero velocity in this frame,the particle has a zero response to any magnetic field. The electric field alone acts on the particle. The three components of its acceleration give directly the three components $E _ { x } , ~ E _ { y } , ~ E _ { z }$ of the electric field. The second test particle cannot be at rest if it is to do more than duplicate the information provided by the first test particle. Orient the $x$ -axis of the frame

$$
\dot { u } _ { \alpha } { } ^ { \kappa } - \frac { e } { m } F _ { \alpha \beta } u ^ { \beta , \kappa } = \delta a _ { \alpha } { } ^ { \kappa } .
$$

Take the squared magnitude of this discrepancy and sum over all the particles

$$
S = \sum _ { k } \eta ^ { \alpha \beta } \delta a _ { \alpha } { } ^ { K } \delta a ^ { K } { } _ { \beta } .
$$

In this expression, everything is regarded as known except the six $F _ { \alpha \beta }$ .Minimize with respect to these six unknowns. In this way,arrive at six equations for the components of $\pmb { B }$ and $\pmb { { \cal E } }$ These equations once solved,one goes back to (3) to test the Lorentz force law.

The $6 \times 6$ determinant of the coefficients in the equation for the $F _ { \alpha \beta }$ automatically vanishes when there are only two test particles. The same line of reasoning permits one to determine the minimum number of test particles required to determine all the components of the Riemann curvature tensor.

The Lorentz force law,written in familiar three-dimensional notation, with ${ \pmb { E } } =$ electric field, ${ \pmb B } =$ magnetic feld, ${ \pmb v } =$ ordinary velocity of particle, $p =$ momentum of particle, $e =$ charge of particle, reads

$$
( d { \pmb p } / d t ) = e ( { \pmb E } + { \pmb v } \times { \pmb B } ) .
$$

The three-dimensional version of the Lorentz force law

Useful though this version of the equation may be,it is far from the geometric spirit of Einstein. A fully geometric equation will involve the test particle's energy-momentum 4-vector, ${ \pmb \rho } _ { ; }$ ，not just the spatial part $\pmb { p }$ as measured in a specific Lorentz frame;and it will ask for the rate of change of momentum not as measured by a specific Lorentz observer $( d / d t )$ ,but as measured by the only clock present $\dot { \pmb { a } }$ priori in the problem: the test particle's own clock $( d / d \tau )$ . Thus, the lefthand side of a fully geometric equation will read

$$
\begin{array} { r } { d \pmb { p } / d \tau = . } \end{array}
$$

The righthand side, the Lorentz 4-force,must also be a frame-independent object. It will be linear in the particle's 4-velocity $\pmb { u }$ , since the frame-dependent expression

$$
{ \frac { d p } { d \tau } } = { \frac { 1 } { \sqrt { 1 - { \nu ^ { 2 } } } } } { \frac { d p } { d t } } = { \frac { e } { \sqrt { 1 - { \nu ^ { 2 } } } } } ( E + \nu \times B ) = e ( u ^ { 0 } E + u \times B )
$$

is linear in the components of ${ \pmb u }$ Consequently, there must be a linear machine named Faraday, or $\pmb { F } ,$ or“electromagnetic field tensor,”with a slot into which one inserts the 4-velocity of a test particle. The output of this machine, multiplied by the particle's charge,must be the electromagnetic 4-force that it feels:

Electromagnetic field tensor defined

Geometrical version ofLorentz force law、

$$
\begin{array} { r } { d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) . } \end{array}
$$

By comparing this geometric equation with the original Lorentz force law (equation 3.2a),and with the companion energy-change law

$$
\frac { d p ^ { 0 } } { d \tau } = \frac { 1 } { \sqrt { 1 - \nu ^ { 2 } } } \frac { d E } { d t } = \frac { 1 } { \sqrt { 1 - \nu ^ { 2 } } } e E \cdot \nu = e E \cdot u ,
$$

one can read off the components of $\pmb { F }$ in a specific Lorentz frame. The components of $d _ { P } / d _ { T }$ are $d p ^ { \alpha } / d \tau$ , and the components of $e \pmb { F } ( \pmb { u } )$ can be written (definition of $F ^ { \alpha } { } _ { \beta } ! )$ $e F ^ { \alpha } { } _ { \beta } u ^ { \beta }$ . Consequently

$$
d p ^ { \alpha } / d \tau = e F ^ { \alpha } { } _ { \beta } u ^ { \beta }
$$

must reduce to equations (3.2a,b). Indeed it does if one makes the identification

$$
\begin{array} { r } { { \beta = 0 \quad \beta = 1 \quad \beta = 2 \quad \beta = 3 } } \\ { { \alpha = 0 \quad \left\| \begin{array} { c c c c } { { 0 } } & { { E _ { x } } } & { { E _ { y } } } & { { E _ { z } } } \\ { { E _ { x } } } & { { 0 } } & { { B _ { z } } } & { { - B _ { y } } } \\ { { E _ { y } } } & { { - B _ { z } } } & { { 0 } } & { { B _ { x } } } \\ { { E _ { z } } } & { { B _ { y } } } & { { - B _ { z } } } & { { 0 } } \end{array} \right\| . } } \end{array}
$$

Components of electromagnetic field tensor

More often seen in the literature are the“covariant components,” obtained by lowering an index with the metric components:

$$
F _ { \alpha \beta } = \eta _ { \alpha \gamma } F ^ { \gamma } { } _ { \beta } ;
$$

$$
| | F _ { \alpha \beta } | | = \left. \begin{array} { c c c c } { { 0 } } & { { - E _ { x } } } & { { - E _ { y } } } & { { - E _ { z } | } } \\ { { E _ { x } } } & { { 0 } } & { { B _ { z } } } & { { - B } } \\ { { E _ { y } } } & { { - B _ { z } } } & { { 0 } } & { { B _ { x } } } \\ { { E _ { z } } } & { { B _ { y } } } & { { - B _ { x } } } & { { 0 } } \end{array} \right.
$$

This matrix equation demonstrates the unity of the electric and magnetic felds. Neither one by itself, $\pmb { { \cal E } }$ or $\pmb { B }$ ,is a frame-independent, geometric entity. But merged together into a single entity, $\pmb { F } =$ Faraday, they acquire a meaning and significance that transcends coordinates and reference frames.

# EXERCISE

# Exercise 3.1.

Derive equations (3.5) and (3.7) for the components of Faraday by comparing (3.4) with (3.2a,b),and by using definition (3.6).

# \$3.2. TENSORS IN ALL GENERALITY

Examples of tensors

A digression is in order. Now on the scene are several different tensors: the metric tensor $\pmb { g }$ (S2.4), the Riemann curvature tensor Riemann (S1.6), the electromagnetic field tensor Faraday (S3.1). Each has been defined as a linear machine with input slots for vectors,and with an output that is either a real number, e.g., ${ \pmb g } ( { \pmb u } , { \pmb v } )$ ,or a vector, e.g., Riemann $( \pmb { u } , \pmb { v } , \pmb { w } )$ and Faraday $( { \pmb u } )$

Should one make a distinction between tensors whose outputs are scalars,and tensors whose outputs are vectors? No! A tensor whose output is a vector can be reinterpreted trivially as one whose output is a scalar. Take, for example,Fara-$d a \gamma = F .$ Add a new slot for the insertion of an arbitrary 1-form $\pmb { \sigma }$ ,and gears and wheels that guarantee the output

$$
\pmb { F } ( \pmb { \sigma } , \pmb { u } ) = \langle \pmb { \sigma } , \pmb { F } ( \pmb { u } ) \rangle = \mathrm { r e a l ~ n u m b e r } .
$$

Then permit the user to choose whether he inserts only a vector, and gets out the vector $\pmb { F } ( . . . , \pmb { u } ) = \pmb { F } ( \pmb { u } )$ ,or whether he inserts a form and a vector,and gets out the number ${ \pmb F } ( { \pmb \sigma } , { \pmb u } )$ .The same machine will do both jobs.Moreover,in terms of components in a given Lorentz frame, both jobs are achieved very simply:

By analogy, one defines the most general tensor $\pmb { H }$ and its rank $\textstyle { \binom { n } { m } }$ as follows: $\pmb { H }$ is a linear machine with $\pmb { n }$ input slots for $\pmb { n }$ 1-forms,and $m$ input slots for $m$ vectors; given the requested input, it puts out a real number denoted

Definition of tensor as linear machine that converts vectors and 1-forms into numbers

$$
H ( \underbrace { \sigma , \boldsymbol { A } , \ldots , \boldsymbol { \beta } } _ { n \mathrm { ~ l - f o r m s } } , \underbrace { \pmb { u } , \pmb { v } , \ldots , \pmb { w } } _ { m \mathrm { ~ v e c t o r s } } ) .
$$

For most tensors the output changes when two input vectors are interchanged,

$$
R i e m a n n ( \sigma , u , v , w ) \neq R i e m a n n ( \sigma , v , u , w ) ,
$$

or when two input 1-forms are interchanged.

Choose a specific tensor $\pmb { S }$ of rank $( _ { 1 } ^ { 2 } )$ for explicitness. Into the slots of $\pmb { s }$ insert the basis vectors and 1-forms of a specific Lorentz coordinate frame. The output is a“component of $\pmb { s }$ in that frame":

$$
S ^ { \alpha \beta } { } _ { \gamma } \equiv { } \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { \omega } ^ { \beta } , \pmb { e } _ { \gamma } ) .
$$

Components of a tensor

This defines components. Knowing the components in a specific frame,one can easily calculate the output produced from any input forms and vectors:

$$
\begin{array} { l } { { { \pmb S } ( \sigma , \rho , \pmb v ) = { \pmb S } ( \sigma _ { \alpha } \pmb \omega ^ { \alpha } , \rho _ { \beta } \pmb \omega ^ { \beta } , v ^ { \gamma } { \pmb e } _ { \gamma } ) = \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } { \pmb S } ( \pmb \omega ^ { \alpha } , \pmb \omega ^ { \beta } , \pmb e _ { \gamma } ) } } \\ { { = { \pmb S } ^ { \alpha \beta } { \gamma } ^ { \sigma _ { \alpha } \rho } { _ \beta } v ^ { \gamma } . } } \end{array}
$$

Tensor's machine action expressed in terms of components

And knowing the components of $\pmb { s }$ in one Lorentz frame (unprimed),plus the Lorentz transformation matrices $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and $1 | A ^ { \beta } { } _ { \alpha ^ { \prime } } | |$ which link that frame with another (primed),one can calculate the components in the new (primed) frame. As shown in exercise 3.2,one need only apply a matrix to each index of $\pmb { s }$ , lining up the matrix indices in the logical manner

$$
S ^ { \mu ^ { \prime } \nu ^ { \prime } } { } _ { \lambda ^ { \prime } } = S ^ { \alpha \beta } { } _ { \gamma } A ^ { \mu ^ { \prime } } { } _ { \alpha } A ^ { \nu ^ { \prime } } { } _ { \beta } A ^ { \gamma } { } _ { \lambda ^ { \prime } } .
$$

Lorentz transformation of components

A slight change of the internal gears and wheels inside the tensor enables one of its l-form slots to accept a vector.Allthat is necessary is a mechanism to convert an input vector $\pmb { n }$ into its corresponding l-form $\widetilde { \pmb { n } }$ and then to put that 1-form into the old machinery. Thus,denoting the modified tensor by the same symbol $\pmb { s }$ as was used for the original tensor, one demands

$$
\pmb { S } ( \sigma , n , \pmb { v } ) = \pmb { S } ( \sigma , \widetilde { \pmb { n } } , \pmb { v } ) ;
$$

Modifying a tensor to accept eitheravectorora1-form into each slot

or, in component notation

$$
S ^ { \alpha } { } _ { \beta \gamma } \sigma _ { \alpha } n ^ { \beta } v ^ { \gamma } = S ^ { \alpha \beta } { } _ { \gamma } \sigma _ { \alpha } n _ { \beta } v ^ { \gamma } .
$$

This is achieved if one raises and lowers the indices of $\pmb { s }$ using the components of the metric:

$$
S ^ { \alpha } { } _ { \beta \gamma } = \eta _ { \beta \mu } S ^ { \alpha \mu } { } _ { \gamma } , \qquad S ^ { \alpha \mu } { } _ { \gamma } = \eta ^ { \mu \beta } S ^ { \alpha } { } _ { \beta \gamma } .
$$

(See exercise 3.3 below.) By using the same symbol $\pmb { s }$ for the original tensor and the modified tensor, one allows each slot to accept either a 1-form or a vector, so one loses sight of whether $\pmb { s }$ is a $\mathbf { \Sigma } ( _ { 1 } ^ { 2 } )$ tensor, or a $\textstyle { { \binom { 1 } { 2 } } }$ tensor, or a $\textstyle { \binom { 3 } { 0 } }$ tensor, or a $( \small { \begin{array} { l } { 0 } \\ { 3 } \end{array} } )$ tensor;one only distinguishes its total rank,3. Terminology:an“upstairs index”is calledcontravantdowsair”inexisalldcotsin $S ^ { \alpha } { } _ { \beta \gamma ^ { * } }$ $" \alpha '$ is a contravariant index,while $^ { \bullet \bullet } { \bar { \beta } } ^ { \bullet }$ and“Y’are covariant indices.

Because tensors are nothing but functions,they can be added (if they have the same rank!) and multiplied by numbers in the usual way: the output of the rank-3 tensor $a \pm b \pmb { \mathscr { a } }$ ,when vectors u, v,w are put in, is

$$
( a \pmb { S } + b \pmb { \Omega } ) ( \pmb { u } , \pmb { v } , \pmb { w } ) \equiv a \pmb { S } ( \pmb { u } , \pmb { v } , \pmb { w } ) + b \pmb { \Omega } ( \pmb { u } , \pmb { v } , \pmb { w } ) .
$$

Several other important operations on tensors are explored in the following exercises.   
They and the results of the exercises will be used freely in the material that follows.

# EXERCISES

Exercise 3.2. TRANSFORMATION LAW FOR COMPONENTS OF A TENSOR From the transformation laws for components of vectors and 1-forms,derive the transformation law (3.14).

# Exercise 3.3. RAISING AND LOWERING INDICES

Derive equations (3.16) from equation (3.15'） plus the law ${ \pmb { n } } _ { \alpha } = { \pmb { \eta } } _ { \alpha \beta } { \pmb { n } } ^ { \beta }$ for getting the components of the 1-form n from the components of its corresponding vector $\pmb { n }$

# Exercise 3.4. TENSOR PRODUCT

Given any two vectors $\pmb { u }$ and $\pmb { \nu } _ { \pmb { \imath } }$ ,one defines the second-rank tensor $\pmb { \nu } \otimes \pmb { \nu }$ ("tensor product of $\pmb { u }$ with $\pmb { v } ^ { \prime \prime }$ ）to be a machine,with two input slots,whose output is the number

$$
( \pmb { \mathscr { u } } \otimes \pmb { \mathscr { v } } ) ( \pmb { \sigma } , \pmb { \lambda } ) = \langle \pmb { \sigma } , \pmb { \mathscr { u } } \rangle \langle \pmb { \lambda } , \pmb { \mathscr { v } } \rangle
$$

when 1-forms $\pmb { \sigma }$ and $\pmb { \lambda }$ are inserted. Show that the components of ${ \pmb { \tau } } = { \pmb { \upsilon } } \otimes { \pmb { \ v } }$ are the products of the components of $\pmb { u }$ and $\pmb { v } \mathrm { : }$

$$
T ^ { \alpha \beta } = u ^ { \alpha } v ^ { \beta } , \qquad T _ { \alpha } { } ^ { \beta } = u _ { \alpha } v ^ { \beta } , \qquad T _ { \alpha \beta } = u _ { \alpha } v _ { \beta } .
$$

Extend the definition to several vectors and forms,

$$
( \pmb { u } \otimes \pmb { v } \otimes \pmb { \beta } \otimes \pmb { w } ) ( \pmb { \sigma } , \pmb { A } , \pmb { n } , \pmb { \zeta } ) = \langle \pmb { \sigma } , \pmb { u } \rangle \langle \pmb { A } , \pmb { v } \rangle \langle \pmb { \beta } , \pmb { n } \rangle \langle \pmb { \zeta } , \pmb { w } \rangle ,
$$

and show that the product rule for components still holds:

$$
\begin{array} { c } { { \pmb S = \pmb u \otimes \pmb v \otimes \pmb \beta \otimes \pmb w \mathrm { \mathrm { \bf ~ h a s ~ c o m p o n e n t s } } } } \\ { { \pmb S ^ { \mu \nu } { } _ { \lambda } { } ^ { \sharp } = u ^ { \mu } v ^ { \nu } \beta _ { \lambda } w ^ { \xi } . } } \end{array}
$$

# Exercise 3.5. BASIS TENSORS

Show that a tensor $\pmb { M }$ with components $M ^ { \alpha \beta } { } _ { \gamma } { } ^ { \delta }$ in a given Lorentz frame can be reconstructed from its components and from the basis 1-forms and vectors of that frame as follows:

$$
{ \bf \partial } ^ { \cdot } M = M ^ { \alpha \beta } { } _ { \gamma } { } ^ { \delta } e _ { \alpha } \otimes e _ { \beta } \otimes \omega ^ { \gamma } \otimes e _ { \delta } .
$$

(For a special case of this, see Box 3.2.)

# Box 3.2 THE METRIC IN DIFFERENT LANGUAGES

# A. Geometric Language

$\pmb { \mathscr { g } }$ is a linear,symmetric machine with two slots for insertion of vectors. When vectors ${ \pmb u }$ and $\pmb { v }$ are inserted, the output of $\pmb { g }$ is their scalar product:

$$
\begin{array} { r } { \pmb { g } ( \pmb { u } , \pmb { v } ) = \pmb { u } \cdot \pmb { v } . } \end{array}
$$

# B. Component Language

$\eta _ { \mu \nu }$ are the metric components. They are used to calculate the scalar product of two vectors from components in a specific Lorentz frame:

$$
u \cdot v = \eta _ { \mu \nu } u ^ { \mu } v ^ { \nu } .
$$

# C. Coordinate-Based Geometric Language

The metric $\pmb { g }$ can be writen,in terms of basis 1-forms of a specific Lorentz fram, as

$$
g = \eta _ { \mu \nu } \varpi ^ { \mu } \otimes \varpi ^ { \nu } = \eta _ { \mu \nu } \ / d x ^ { \mu } \otimes d x ^ { \nu }
$$

[see equations (2.18) and (3.2).

# D. Connection to the Elementary Concept of Line Element

$\tt B o x 2 . 3$ demonstrated the correspondence between the gradient df of a function, and the elementary concept df of a differential change of $f$ in some unspecified direction. There is a similar correspondence between the metric, writen as $\eta _ { \mu } , d x ^ { \mu }$ $\otimes \ d x ^ { \nu }$ ,and the elementary concept of “line element,” written as $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ This elementary line element,as expounded in many special relativity texts,represents the squared length of the displacement $\ " d x \mu \ v { r } { }$ in an unspecified direction. The metric $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ does the same. Pick a specific infinitesimal displacement vector $\pmb { \xi }$ ,and insert it into the slots of $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ . The output will be $\xi ^ { 2 } = \eta _ { \mu \nu } \xi ^ { \mu } \xi ^ { \nu }$ ， the squared length of the displacement. Before $\pmb { \xi }$ is inserted, $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ has the potential to tell the squared length of any vector; the insertion of $\pmb { \xi }$ converts potentiality into actuality: the numerical value of $\xi ^ { 2 }$

Because the metric $\eta _ { \mu \nu } d x ^ { \mu } \otimes d x ^ { \nu }$ and the line element $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ perform this same function of representing the squared length of an unspecified infinitesimal displacement, there is no conceptual distinction between them. One sometimes uses the symbols $\mathbf { d } s ^ { 2 }$ to denote the metric; one sometimes gets pressed and writes it as $d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu }$ ,omitting the $" \otimes "$ ； and one sometimes even gets so pressed as to use nonbold characters,so that no notational distinction remains at all between metric and elementary line element:

$$
g = d s ^ { 2 } = d s ^ { 2 } = \eta _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } .
$$

# Exercise 3.6. Faraday MACHINERY AT WORK

An observer with 4-velocity $\pmb { u }$ picks out three directions in spacetime that are orthogonal and purely spatial (no time part) as seen in his frame. Let $\pmb { e } _ { \hat { 1 } }$ ， ${ \pmb e } _ { \hat { \bf 2 } } , { \pmb e } _ { \hat { \bf 3 } }$ be unit vectors in those directions and let them be oriented in a righthanded way $( \pmb { e } _ { \hat { 1 } } \cdot \pmb { e } _ { \hat { 2 } } \times \pmb { e } _ { \hat { 3 } } = + 1$ in three-dimensional language).Why do the following relations hold?

$$
{ \pmb e } _ { j } \cdot { \pmb u } = 0 , \qquad { \pmb e } _ { j } \cdot { \pmb e } _ { \hat { k } } = \delta _ { j k } .
$$

What vectors are to be inserted in the two slots of the electromagnetic field tensor Faraday if one wants to get out the electric field along $\pmb { e } _ { j }$ as measured by this observer? What vectors must be inserted to get the magnetic field he measures along ${ \pmb e } _ { j } { \pmb \mathrm { : \theta } }$

# \$3.3. THREE-PLUS-ONE VIEW VERSUS GEOMETRIC VIEW

The power of the geometric view of physics

Great computational and conceptual power resides in Einstein's geometric view of physics. Ideas that seem complex when viewed in the everyday “space-plus-time” or $" 3 + 1 "$ manner become elegant and simple when viewed as relations between geometric objects in four-dimensional spacetime. Derivations that are difficult in $3 + 1$ language simplify in geometric language.

Example of electromagnetism

The electromagnetic field is a good example. In geometric language, it is described by a second-rank,antisymmetric tensor ("2-form") $\pmb { F } _ { i }$ ，which requires no coordinates for its definition. This tensor produces a 4-force on any charged particle given by

$$
\begin{array} { r } { d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) . } \end{array}
$$

It is all so simple!

By contrast, consider the $" 3 + 1 "$ viewpoint. In a given Lorentz frame, there is an electric field $\pmb { { \cal E } }$ and a magnetic field $\pmb { B }$ They push on a particle in accordance with

Transformation law for electric and magnetic fields

$$
d { p } / d t = e ( { \cal E } + \nu \times { \cal B } ) .
$$

But the values of $\underline { { \boldsymbol { p } } } , \pmb { \cal E } , \pmb { \nu } ,$ and $\pmb { B }$ all change when one passes from the given Lorentz frame to a new one. For example, the electric and magnetic fields viewed from a rocket ship ("barred” frame) are related to those viewed in the laboratory ("unbarred” frame) by

$$
\begin{array} { r l r } & { \boldsymbol { \bar { E } } _ { \parallel } = \boldsymbol { E } _ { \parallel } , \quad } & { \boldsymbol { \bar { E } } _ { \perp } = \frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } ( \boldsymbol { E } _ { \perp } + \boldsymbol { \beta } \times \boldsymbol { B } _ { \perp } ) , } \\ & { \boldsymbol { \bar { B } } _ { \parallel } = \boldsymbol { B } _ { \parallel } , \quad } & { \boldsymbol { \bar { B } } _ { \perp } = \frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } ( \boldsymbol { B } _ { \perp } - \boldsymbol { \beta } \times \boldsymbol { E } _ { \perp } ) . } \end{array}
$$

(Here“ll" means component along direction of rocket's motion;“⊥"means perpendicular component; and $\beta ^ { j } = d x _ { \mathrm { ~ r o c k e t } } ^ { j } / d t$ is the rocket's ordinary velocity.） The analogous transformation laws for the particle's momentum $\pmb { p }$ and ordinary velocity $\pmb { \nu }$ ，and for the coordinate time $t$ ,all conspire-as if by magic, it seems,from the $3 + 1$ viewpoint-to maintain the validity of the Lorentz force law in all frames.

Not only is the geometric view far simpler than the $3 + 1$ view, it can even derive the $3 + 1$ equations with greater ease than can the $3 + 1$ view itself. Consider,for example,the transformation law (3.23） for the electric and magnetic fields.The geometric view derives it as follows: (l) Orient the axes of the two frames so their relative motion is in the $z$ -direction. (2） Perform a simple Lorentz transformation (equation 2.45) on the components of the electromagnetic field tensor:

$$
\begin{array} { r l } & { \bar { E } _ { 1 1 } = \bar { E } _ { z } = F _ { \overline { { 3 0 } } } = A ^ { \alpha } _ { \overline { { 3 } } } A ^ { \beta } _ { \overline { { 0 } } } F _ { \alpha \beta } = \gamma ^ { 2 } F _ { 3 0 } + \beta ^ { 2 } \gamma ^ { 2 } F _ { 0 3 } } \\ & { \quad = ( 1 - \beta ^ { 2 } ) \gamma ^ { 2 } F _ { 3 0 } = F _ { 3 0 } = E _ { z } = E _ { 1 \mid } , } \\ & { \bar { E } _ { x } = F _ { \overline { { 1 0 } } } = A ^ { \alpha } _ { \overline { { 1 } } } A ^ { \beta } _ { \overline { { 0 } } } F _ { \alpha \beta } = \gamma F _ { 1 0 } + \beta \gamma F _ { 1 3 } = \gamma ( E _ { x } - \beta B _ { y } ) , } \end{array}
$$

By contrast, the $3 + 1$ view shows much more work.A standard approach is based on the Lorentz force law and energy-change law (3.2a,b), written in the slightly modified form

$$
m \frac { d ^ { 2 } \overline { { x } } } { d \tau ^ { 2 } } = e \bigg ( \bar { E } _ { x } \frac { d \overline { { t } } } { d \tau } + 0 \frac { d \overline { { x } } } { d \tau } + \bar { B } _ { z } \frac { d \overline { { y } } } { d \tau } - \bar { B } _ { y } \frac { d \overline { { z } } } { d \tau } \bigg ) ,
$$

... (three additional equations)....

It proceeds as follows (details omitted because of their great length!):

(1） Substitute for the $d ^ { 2 } \overline { { x } } / d \tau ^ { 2 }$ , etc.,the expression for these quantities in terms of the $d ^ { 2 } x / d \tau ^ { 2 }$ ... (Lorentz transformation).   
(2） Substitute for the $d ^ { 2 } x / d \tau ^ { 2 }$ ,... the expression for these accelerations in terms of the laboratory $\pmb { { \cal E } }$ and $\pmb { B }$ (Lorentz force law).   
(3） In these expressions,wherever the components $d x / d \tau$ of the 4-velocity in the laboratory frame appear, substitute expressions in terms of the 4-velocities in the rocket frame (inverse Lorentz transformation).   
(4) In (3.25) as thus transformed, demand equality of left and right sides for all values of the $d \overline { { x } } / d \tau$ ,etc.(validity for all test particles).   
(5)In this way arrive at the expressions (3.23) for the $\bar { E }$ and $\bar { \pmb { B } }$ in terms of the $\pmb { { \cal E } }$ and $\pmb { B }$

The contrast in difficulty is obvious!

# $\ S 3 . 4$ .MAXWELL'S EQUATIONS

Turn now from the action of the field on a charge,and ask about the action of a charge on the field,or, more generally,ask about the dynamics of the electromagnetic

# Magnetodynamics derived from magnetostatics

feld, charge or no charge.Begin with the simplest of Maxwel's equations in a specific Lorentz frame, the one that says there are no free magnetic poles:

$$
\nabla \cdot B \equiv \mathrm { d i v } \ : B = \frac { \partial B _ { x } } { \partial x } + \frac { \partial B _ { y } } { \partial y } + \frac { \partial B _ { z } } { \partial z } = 0 .
$$

This statement has to be true in all Lorentz frames. It is therefore true in the rocket frame:

$$
\frac { \partial \overline { { B } } _ { z } } { \partial \overline { { x } } } + \frac { \partial \overline { { B } } _ { y } } { \partial \overline { { y } } } + \frac { \partial \overline { { B } } _ { z } } { \partial \overline { { z } } } = 0 .
$$

For an infinitesimal Lorentz transformation in the $x$ -direction (nonrelativistic velocity $\beta$ ),one has (see Box 2.4 and equations 3.23)

$$
\begin{array} { r l r } & { \overline { { B } } _ { x } = B _ { x } , \qquad \overline { { B } } _ { y } = B _ { y } + \beta E _ { z } , \qquad \overline { { B } } _ { z } = B _ { z } - \beta E _ { y } ; } & \\ & { \frac { \partial } { \partial \overline { { x } } } = \frac { \partial } { \partial x } + \beta \frac { \partial } { \partial t } , \qquad \frac { \partial } { \partial \overline { { y } } } = \frac { \partial } { \partial y } , \qquad \frac { \partial } { \partial \overline { { z } } } = \frac { \partial } { \partial z } . } & \end{array}
$$

Substitute into the condition of zero divergence in the rocket frame. Recover the original condition of zero divergence in the laboratory frame, plus the following additional information (requirement for the vanishing of the coefficient of the arbitrary small velocity $\beta$ ：

$$
\frac { \partial B _ { z } } { \partial t } + \frac { \partial E _ { z } } { \partial y } - \frac { \partial E _ { y } } { \partial z } = 0 .
$$

Had the velocity of transformation been directed in the y- or $z$ directions,a similar equation would have been obtained for $\partial B _ { y } / \partial t$ or $\partial B _ { z } / \partial t$ In the language of threedimensional vectors, these three equations reduce to the one equation

$$
\begin{array} { r } { \frac { \partial \boldsymbol { B } } { \partial t } + \boldsymbol { \nabla } \times \boldsymbol { E } \equiv \frac { \partial \boldsymbol { B } } { \partial t } + \operatorname { c u r l } \boldsymbol { E } = \boldsymbol { 0 } . } \end{array}
$$

Magnetodynamicsand magnetostatics unified in one geometric law

How beautiful that (1) the principle of covariance (laws of physics are the same in every Lorentz reference system, which is equivalent to the geometric view of physics） plus (2） the principle that magnetic tubes of force never end,gives (3) Maxwel's dynamic law for the time-rate of change of the magnetic field! This suggests that the magnetostatic law $\pmb { \nabla } \cdot \pmb { B } = 0$ and the magnetodynamic law $\partial { \pmb B } / \partial t + \pmb { \nabla } \times { \pmb E } = 0$ must be wrapped up together in a single frame-independent, geometric law.In terms of components of the field tensor $\pmb { F } ,$ that geometric law must read

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 ,
$$

since this reduces to $\pmb { \nabla } \cdot \pmb { B } = 0$ when one takes $\alpha = 1 , \beta = 2 , \gamma = 3$ and it reduces to $\partial { \pmb B } / \partial t + \pmb { \nabla } \times { \pmb E } = 0$ when one sets any index, e.g., $\pmb { \alpha }$ , equal to zero (see exercise 3.7 below). In frame-independent geometric language, this law is written (see $\ S 3 . 5$ ， exercise 3.l4,and Chapter 4 for notation)

and it says,“Take the electromagnetic 2-form $\pmb { F }$ (a geometric object defined even in absence of coordinates); from it construct a new geometric object dF (called the “exterior derivative of $\pmb { F } ^ { \prime }$ ）； $\pmb { d } \pmb { F }$ must vanish. The details of this coordinate-free process will be spelled out in exercise 3.15 and in $\ S 4 . 5$ (track 2).

Two of Maxwell's equations remain: the electrostatic equation

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { E } = 4 \pi \pmb { \rho } , } \end{array}
$$

and the electrodynamic equation

$$
\partial { \pmb { E } } / \partial t - { \pmb { \nabla } } \times { \pmb { B } } = - 4 \pi { \pmb { J } } .
$$

They, like the magnetostatic and magnetodynamic equations, are actually two different parts of a single geometric law. Written in terms of feld components, that law says

Electrodynamics and electrostatics unified in one geometric law

$$
F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha } { } ,
$$

where the components of the “4-current" $\pmb { J }$ are

$$
\begin{array} { c } { { J ^ { 0 } = \rho = \mathrm { c h a r g e ~ d e n s i t y } , } } \\ { { ( J ^ { 1 } , J ^ { 2 } , J ^ { 3 } ) = \mathrm { c o m p o n e n t s ~ o f ~ c u r r e n t ~ d e n s i t y } . } } \end{array}
$$

Writen in coordinate-free, geometric language, this electrodynamic law says

$$
{ \pmb d } ^ { * } { \pmb F } = 4 \pi ^ { * } { \pmb J } \mathrm { o r } , \mathrm { e q u i v a l e n t l y } , \pmb \nabla \cdot { \pmb F } = 4 \pi { \pmb J } .
$$

(For full discussion, see exercise 3.15 and $\ S 4 . 5$ ，which is on Track 2.)

# Exercise 3.7. MAXWELL'S EQUATIONS

Show, by explicit examination of components,that the geometric laws

EXERCISE

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 , \qquad F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha } ,
$$

do reduce to Maxwel's equations (3.26), (3.31), (3.34), (3.35),as claimed above.

# $\$ 3.5$ WORKING WITH TENSORS

Another mathematical digression is needed. Given an arbitrary tensor field,S,of arbitrary rank (choose rank $= 3$ for concreteness)， one can construct new tensor fields by a variety of operations.

One operation is the gradient $\blacktriangledown$ . (The symbol $\pmb { d }$ is reserved for gradients of scalars, in which case $\mathbf { v } f \equiv \mathbf { d } f$ and for“exterior derivatives of differential forms;”a Track-2

Ways to produce new tensors from old:

Gradient

concept, on which see $\ S 4 . 5 .$ ）Like S,VS is a machine. It has four slots,whereas $\pmb { s }$ has three. It describes how $\pmb { s }$ changes from point to point. Specifically, if one desires to know how the number $\pmb { S } ( \pmb { u } , \pmb { v } , \pmb { w } )$ for fixed $\pmb { u }$ ， $\pmb { \nu } ,$ w changes under a displacement $\pmb { \xi }$ ，one inserts ${ \pmb u } , { \pmb v } , { \pmb w } , { \pmb \xi }$ into the four slots of $\pmb { \triangledown } \pmb { \cal S }$

$$
\begin{array} { r l } & { \nabla S ( u , v , w , \xi ) \equiv \widehat { \circ } _ { \xi } S ( u , v , w ) \mathrm { ~ w i t h ~ } u , v , w \mathrm { ~ f i x e d ~ } } \\ & { \qquad \simeq + \mathrm { ~ } \{ \mathrm { v a l u e ~ o f ~ } S ( u , v , w ) \mathrm { ~ a t ~ t i p ~ o f ~ } \xi \} } \\ & { \qquad - \mathrm { ~ } \{ \mathrm { v a l u e ~ o f ~ } S ( u , v , w ) \mathrm { ~ a t ~ t a i l ~ o f ~ } \xi \} . } \end{array}
$$

In component notation in a Lorentz frame, this says

$$
\begin{array} { l } { { \nabla S ( u , v , w , \xi ) \equiv \hat { \sigma } _ { \xi } ( S _ { \alpha \beta \gamma } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } ) = \left( \frac { \hat { \partial } S _ { \alpha \beta \gamma } } { \partial x ^ { \delta } } \xi ^ { \delta } \right) u ^ { \alpha } v ^ { \beta } w ^ { \gamma } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = S _ { \alpha \beta \gamma , \delta } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } \xi ^ { \delta } . } } \end{array}
$$

Thus, the Lorentz-frame components of VS are nothing but the partial derivatives of the components of $\pmb { s }$ . Notice that the gradient raises the rank of a tensor by l (from 3 to 4 for $\pmb { s }$ ）.

Contraction

Contraction is another process that produces a new tensor from an old one. It seals off ("contracts") two of the old tensor's slots, thereby reducing the rank by two. Specifically, if $\pmb R$ is a fourth-rank tensor and $\pmb { \mathscr { M } }$ is obtained by contracting the first and third slots of $\pmb R$ ,then the output of M is given by (definition!)

$$
M ( u , v ) = \sum _ { \alpha = 0 } ^ { 3 } \bar { R } ( e _ { \alpha } , u , \omega ^ { \alpha } , v ) .
$$

Here ${ \pmb { e } } _ { \alpha }$ and ${ \pmb { \omega } } ^ { \alpha }$ are the basis vectors and l-forms of a specific but arbitrary Lorentz coordinate frame.It makes no difference which frame is chosen; the result willalways be the same (exercise 3.8 below). In terms of components in any Lorentz frame, equation (3.40) says (exercise 3.8)

$$
M ( u , v ) = M _ { \mu \nu } u ^ { \mu } v ^ { \nu } = R _ { \alpha \mu } { } ^ { \alpha } { } _ { \nu } u ^ { \mu } v ^ { \nu } ,
$$

so that

$$
M _ { \mu \nu } = { R _ { \alpha \mu } } _ { \nu } ^ { \alpha } .
$$

Thus, in terms of components, contraction amounts to putting one index up and the other down,and then summing on them.

Divergence is a third process for creating new tensors from old.It is accomplished by taking the gradient, then contracting the gradient's slot with one of the original slots:

(divergence of $\pmb { s }$ on first $\mathbf { \sigma } _ { \mathrm { { s l o t } } } ) \equiv \mathbf { \boldsymbol { v } } \cdot \mathbf { \boldsymbol { s } }$ is a machine such that

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { S } ( \pmb { u } , \pmb { \dot { v } } ) = \pmb { \nabla } \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { u } , \pmb { v } , \pmb { e } _ { \alpha } ) = { S } ^ { \alpha } { } _ { \beta \gamma , \alpha } \pmb { u } ^ { \beta } \pmb { v } ^ { \gamma } ; } \end{array}
$$

i.e. $\pmb { \bigtriangledown } \cdot \pmb { S }$ has components $S ^ { \alpha } { } _ { \beta \gamma , \alpha ^ { . } }$

Transpose is a fourth, rather trivial process for creating'new tensors. It merely interchanges two slots:

Transpose

N obtained by transposing second and third slots of $\pmb { S } \Longrightarrow$

$$
\pmb { N } ( \pmb { u } , \pmb { v } , \pmb { w } ) = \pmb { S } ( \pmb { u } , \pmb { w } , \pmb { v } ) .
$$

Symmetrization and antisymmetrization are fth and sixth processes for producing new tensors from old.A tensor is completely symmetric if its output is unaffected by an interchange of two input vectors or l-forms:

$$
\mathcal { S } ( u , v , w ) = \mathcal { S } ( v , u , w ) = \mathcal { S } ( v , w , u ) = \cdot \cdot \cdot .
$$

Symmetrization and antisymmetrization

It is completely antisymmetric if it reverses sign on each interchange of input

$$
\mathcal S ( u , v , w ) = - \mathcal S ( v , u , w ) = + \mathcal S ( v , w , u ) = \cdot \cdot \cdot .
$$

Any tensor can be symmetrized or antisymmetrized by constructing an appropriate linear combination of it and its transposes; see exercise 3.12.

Wedge product is a seventh process for producing new tensors from old. It is merely an antisymmetrized tensor product: given two vectors ${ \pmb u }$ and $\pmb { v } ,$ ,their wedge product, the “bivector" $\mu \wedge v ,$ is defined by

Wedge product

Bivector

$$
\pmb { \iota } \wedge \pmb { v } \equiv \pmb { \iota } \otimes \pmb { v } - \pmb { v } \otimes \pmb { u } ;
$$

similarly,the“2-form” $\alpha \wedge \beta$ constructed from two l-forms is

2-form

$$
\alpha \wedge \beta \equiv \alpha \otimes \beta - \beta \otimes \alpha .
$$

From three vectors $\psi , v ,$ w one constructs the “triuector”

Trivector

$$
{ \begin{array} { r l } { u \wedge v \wedge w \equiv ( u \wedge v ) \wedge w \equiv u \wedge ( v \wedge w ) } \\ & { \qquad = u \otimes v \otimes w + { \mathrm { t e r m s ~ t h a t ~ g u a r a n t e e ~ c o m p l e t e } } } \\ & { \qquad = u \otimes v \otimes w + v \otimes w \otimes u + w \otimes u \otimes v } \\ & { \qquad - v \otimes u \otimes w - u \otimes w \otimes v - w \otimes v \otimes u . } \end{array} }
$$

From 1-forms $\pmb { \alpha } , \pmb { \beta } , \pmb { \gamma }$ one similarly constructs the“3-forms" $\alpha \wedge \beta \wedge \gamma$ .The wedge product gives a simple way to test for coplanarity (linear dependence) of vectors: if ${ \pmb u }$ and $\pmb { \nu }$ are collinear, so ${ \bf \nabla } \cdot { \bf u } = a { \bf v } _ { \mathrm { : } }$ then

$$
u \wedge v = a v \wedge v = 0 ( { \mathfrak { b } } \mathrm { y } \mathrm { ~ a n t i s y m m e t r y ~ o f ~ } ^ { \ast \ast } \wedge ^ { \prime \ast } ) .
$$

f $\boldsymbol { \mathsf { w } }$ is coplanar with $\pmb { u }$ and $\pmb { v } \ s _ { 0 } \ \pmb { w } = a \pmb { u } + b \pmb { v }$ ("collapsed box"), then

$$
\pmb { w } \wedge \pmb { u } \wedge \pmb { v } = a \pmb { u } \wedge \pmb { u } \wedge \pmb { v } + b \pmb { v } \wedge \pmb { u } \wedge \pmb { v } = 0 .
$$

The symbol $" \wedge "$ is called a“hat” or “wedge”or“exterior product sign."Its properties are investigated in Chapter 4.

Taking the dual is an eighth process for constructing new tensors. It plays aDual fundamental role in Track 2 of this book,but since it is not needed for Track 1, its defnition and properties are treated only in the exercises (3.14 and 3.15).

Because the frame-independent geometric notation is somewhat ambiguous (which slots are being contracted? on which slot is the divergence taken? which slots are being transposed?), one often uses component notation to express coordinate-inde-pendent, geometric relations between geometric objects. For example,

$$
J _ { \beta \gamma } = S ^ { \alpha } { } _ { \beta \gamma , \alpha }
$$

means $\blacktriangleleft$ is a tensor obtained by taking the divergence on the first slot of the tensor $\pmb { S } ^ { \prime \prime }$ Also,

$$
v ^ { \gamma } = ( F _ { \mu \nu } F ^ { \mu \nu } ) ^ { , \gamma } \equiv ( F _ { \mu \nu } F ^ { \mu \nu } ) _ { , \beta } \eta ^ { \beta \gamma }
$$

means $\cdots$ is a vector obtained by(l） constructing the tensor product ${ \pmb F } \otimes { \pmb F }$ of $\pmb { F }$ with itself, (2） contracting ${ \pmb F } \otimes { \pmb F }$ on its first and third slots,and also on its second and fourth,(3) taking the gradient of the resultant scalar function, (4) converting that gradient, which is a l-form, into the corresponding vector."

Index gymnastics

“Index gymnastics,” the technique of extracting the content from geometric equations by working in component notation and rearranging indices as required, must be mastered if one wishes to do diffcult calculations in relativity,special or general. Box 3.3 expounds some of the short cuts in index gymnastics,and exercises 3.8-3.18 offer practice.

# EXERCISES

# Exercise 3.8. CONTRACTION IS FRAME-INDEPENDENT

Show that contraction,as defined in equation (3.40),does not depend on which Lorentz frame ${ \pmb e } _ { \pmb { \alpha } }$ and $\pmb { \omega } ^ { \alpha }$ are taken from.Also show that equation (3.40) implies

$$
{ \pmb M } ( { \pmb u } , { \pmb v } ) = R _ { \alpha \mu } { } ^ { \alpha } { } _ { \nu } u ^ { \mu } v ^ { \nu } .
$$

# Exercise 3.9. DIFFERENTIATION

(a)Justify the formula

$$
d ( u _ { \mu } v ^ { \nu } ) / d \tau = ( d u _ { \mu } / d \tau ) v ^ { \nu } + u _ { \mu } ( d v ^ { \nu } / d \tau ) .
$$

by considering the special case $\mu = 0 , \nu = 1$

(b) Explain why

$$
( T ^ { \alpha \beta } v _ { \beta } ) _ { , \mu } = T ^ { \alpha \beta } { } _ { , \mu } v _ { \beta } + T ^ { \alpha \beta } v _ { \beta , \mu } .
$$

# Exercise 3.10. MORE DIFFERENTIATION

(a) Justify the formula,

$$
d ( u ^ { \mu } u _ { \mu } ) / d \tau = 2 u _ { \mu } ( d u ^ { \mu } / d \tau ) ,
$$

by writing out the summation $u ^ { \mu } u _ { \mu } \equiv \eta _ { \mu \nu } u ^ { \mu } u ^ { \nu }$ explicitly.

(b)Let δ indicate a variation or small change,and justify the formula

$$
\delta ( F _ { \alpha \beta } F ^ { \alpha \beta } ) = 2 F _ { \alpha \beta } \delta F ^ { \alpha \beta } .
$$

(c) Compute $( F _ { \alpha \beta } F ^ { \alpha \beta } ) _ { , \mu } = ?$

<table><tr><td colspan="2">Box 3.3 TECHNIQUES OF INDEX GYMNASTICS</td></tr><tr><td>Equation</td><td>Name and Discussion</td></tr><tr><td>Sβγ = S(wα,e,ey)</td><td>Computing components.</td></tr><tr><td>Saβ= S(wα,wβ,ey)</td><td>Computing other components.</td></tr><tr><td>S = Sβγe wβwY</td><td>Reconstructing the rank-() version of S.</td></tr><tr><td>S= SaβYeeeγ</td><td>Reconstructing the rank-() version of S. [Recall: one does not usually distinguish between the various versions; see equa- tion (3.15) and associated discussion.]</td></tr><tr><td>SaB =nBuSauy</td><td>Raising an index.</td></tr><tr><td>Saμy = nμBSaBy</td><td>Lowering an index.</td></tr><tr><td>M = Sa</td><td>Contraction of S to form a new tensor M.</td></tr><tr><td>Taβ = SaβM</td><td>Tensor product of S with M to form a new tensor T.</td></tr><tr><td>A²= AA</td><td>Squared length of vector A produced by forming tensor product A A and then contracting,which is the same as forming the</td></tr><tr><td>manBY = 8Y</td><td>correspondingl-formAandthenpiercing:A² = (A,A&gt;= AaA. The matrix formed from the metric&#x27;s “covariant components.” lmβll,is the inverse of that formed from its“contravariant components,” Iinβ. Equivalently, raising one index of the</td></tr><tr><td>SBy= N@BY</td><td>metric naβ produces the Kronecker delta. Gradient of N to form a new tensor S.</td></tr><tr><td>R = Nβ</td><td>Divergence of N to form a new tensor R.</td></tr><tr><td>Nβ,y=(nBμNau），= nβμNau</td><td>Taking gradients and raising or lowering indices are operations that commute.</td></tr><tr><td>NY= NaB.nμY</td><td>Contravariant index on a gradient is obtained by raising covari-</td></tr><tr><td>(RMβ)y=Ra,yM+RMβ,Y</td><td>ant index. Gradient of a tensor product; says V(R  M) =</td></tr><tr><td>Gβ=Faβ]三（Faβ-FBa）</td><td>Transpose(VR  M) + R ∀M. Antisymmetrizing a tensor F to produce a new tensor G.</td></tr><tr><td>Hβ=FaB）=（Faβ+Fβa)</td><td>Symmetrizing a tensor F to produce a new tensor H.</td></tr><tr><td>*Jp-= JreμaBY</td><td>Forming the rank-3 tensor that is dual to a vector (exercise</td></tr><tr><td>*Faβ=Fuμvaβ</td><td>3.14). Forming the antisymmetric rank-2 tensor that is dual toa given</td></tr><tr><td>*B=1B^uexμα</td><td>antisymmetric rank-2 tensor (exercise 3.14). Forming the l-form that is dual to an antisymmetric rank-3 tensor (exercise 3.14).</td></tr></table>

# Exercise 3.11. SYMMETRIES

Let $A _ { \mu \nu }$ be an antisymmetric tensor so that $A _ { \mu \nu } = - A _ { \nu \mu }$ and let $S ^ { \mu \nu }$ be a symmetric tensor so that $S ^ { \mu \nu } = S ^ { \nu \mu }$

(a) Justify the equations $A _ { \mu \nu } S ^ { \mu \nu } = 0$ in two ways: first, by writing out the sum explicitly (all sixteen terms) and showing how the terms in the sum cancel in pairs;second,by giving an argument to justify each equals sign in the following string:

$$
A _ { \mu \nu } S ^ { \mu \nu } = - A _ { \nu \mu } S ^ { \mu \nu } = - A _ { \nu \mu } S ^ { \nu \mu } = - A _ { \alpha \beta } S ^ { \alpha \beta } = - A _ { \mu \nu } S ^ { \mu \nu } = 0 .
$$

(b)Establish the following two identites foranyarbitrary tensor $V _ { \mu \nu }$

$$
V ^ { \mu \nu } A _ { \mu \nu } = \frac { 1 } { 2 } ( V ^ { \mu \nu } - V ^ { \nu \mu } ) A _ { \mu \nu } , \qquad V ^ { \mu \nu } S _ { \mu \nu } = \frac { 1 } { 2 } ( V ^ { \mu \nu } + V ^ { \nu \mu } ) S _ { \mu \nu } .
$$

# Exercise 3.12. SYMMETRIZATION AND ANTISYMMETRIZATION

To"symmetrize”a tensor,one averages it with all of its transposes.The components of the new,symmetrized tensor are distinguished by round brackets:

$$
\begin{array} { l } { { \displaystyle V _ { ( \mu ^ { p } ) } \equiv \frac { 1 } { 2 } ( V _ { \mu ^ { p } } + V _ { \nu _ { \mu } } ) } ; } \\ { ~ } \\ { { \displaystyle V _ { ( \mu \nu \lambda ) } \equiv \frac { 1 } { 3 ! } ( V _ { \mu \nu \lambda } + V _ { \nu \lambda \mu } + V _ { \lambda \mu \nu } + V _ { \nu _ { \mu \lambda } } + V _ { \mu \lambda \nu } + V _ { \lambda \nu \mu } ) } . } \end{array}
$$

One “antisymmetrizes” a tensor (square brackets) similarly:

$$
\begin{array} { l } { { \displaystyle V _ { [ \mu \nu ] } \equiv \frac { 1 } { 2 } ( V _ { \mu \nu } - V _ { \nu \mu } ) } ; } \\ { ~ } \\ { { \displaystyle V _ { [ \mu \nu \lambda ] } \equiv \frac { 1 } { 3 ! } ( V _ { \mu \nu \lambda } + V _ { \nu \lambda \mu } + V _ { \lambda \mu } , - V _ { \nu \mu \lambda } - V _ { \mu \lambda \nu } - V _ { \lambda \nu \mu } ) } . } \end{array}
$$

(a) Show that such symmetrized and antisymmetrized tensors are, indeed,symmetric and antisymmetric under interchange of the vectors inserted into their slots:

$$
\begin{array} { r l } & { V _ { ( \alpha \beta \gamma ) } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } = + V _ { ( \alpha \beta \gamma ) } v ^ { \alpha } u ^ { \beta } w ^ { \gamma } = \cdot \cdot \cdot , } \\ & { V _ { [ \alpha \beta \gamma ] } u ^ { \alpha } v ^ { \beta } w ^ { \gamma } = - V _ { [ \alpha \beta \gamma ] } v ^ { \alpha } u ^ { \beta } w ^ { \gamma } = \cdot \cdot \cdot . } \end{array}
$$

(b) Show that a second-rank tensor can be reconstructed from its symmetric and antisymmetric parts,

$$
V _ { \mu \nu } = V _ { ( \mu \nu ) } + V _ { [ \mu \nu ] } ,
$$

but that a third-rank tensor cannot; $V _ { \{ \alpha \beta \gamma \} }$ and $V _ { [ \alpha \beta \gamma ] }$ contain together “less information” than $V _ { \alpha \beta \gamma }$ “Young diagrams"(see,e.g.,Messiah [196l],appendix D) describe other symmetries,more subtle than these two,which contain the missing information.

(c) Show that the electromagnetic field tensor satisfies

$$
F _ { ( \alpha \beta ) } = 0 , \qquad F _ { \alpha \beta } = F _ { [ \alpha \beta ] } .
$$

(d) Show that Maxwell's “magnetic” equations

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0
$$

can be rewritten in the form

$$
F _ { [ \alpha \beta , \gamma ] } = 0 .
$$

# Exercise 3.13. LEVI-CIVITA TENSOR

The“Levi-Civita tensor” $\pmb { \varepsilon }$ in spacetime is a fourth-rank, completely antisymmetric tensor:

Choose an arbitrary but specific Lorentz frame, with ${ \pmb \theta } _ { 0 }$ pointing toward the future and with $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ a righthanded set of spatial basis vectors. The covariant components of $\pmb { \varepsilon }$ in this frame are

$$
\varepsilon _ { 0 1 2 3 } = \varepsilon ( e _ { 0 } , e _ { 1 } , e _ { 2 } , e _ { 3 } ) = + 1 .
$$

[Note: In an $_ { n }$ -dimensional space, $\pmb { \varepsilon }$ is the analogous completely antisymmetric rank- $_ n$ tensor. Its components are

$$
\varepsilon _ { 1 2 \ldots , n } = \varepsilon ( e _ { 1 } , e _ { 2 } , \ldots , e _ { n } ) = + 1 ,
$$

when computed on a“positively oriented,”orthonormal basis $\pmb { e } _ { 1 } , \ldots , \pmb { e } _ { n } . ]$

(a) Use the antisymmetry to show that

$$
\begin{array} { c } { \varepsilon _ { \alpha \beta \gamma \delta } = 0 \ \mathrm { u n l e s s } \ \alpha , \beta , \gamma , \delta \ \mathrm { a r e \ a l l \ d i f f e r e n t } , } \\ { { \mathrm { } } } \\ { { \mathrm { } : _ { \pi \ L { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } = \left\{ \begin{array} { l l } { { + 1 \ \mathrm { f o r \ e v e n \ p e r m u t a t i o n s \ o f \ 0 , \ l , \ 2 , \ 3 , \ a n d } } } \\ { { - 1 \ \mathrm { f o r \ o d d \ p e r m u t a t i o n s } . } } \end{array} \right. } } \end{array}
$$

(b) Show that

$$
\varepsilon ^ { \pi _ { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } = - \varepsilon _ { \pi _ { 0 } \pi _ { 1 } \pi _ { 2 } \pi _ { 3 } } .
$$

(c) By means of a Lorentz transformation show that $\varepsilon ^ { \overline { { \alpha } } \overline { { \beta } } \overline { { \gamma \delta } } }$ and $\varepsilon _ { \overline { { { \alpha } } } \overline { { { \beta } } } } \overline { { { \gamma } } } \overline { { { \delta } } }$ have these same values in any other Lorentz frame with $\pmb { e } _ { 0 }$ pointing toward the future and with $\pmb { e } _ { \bar { 1 } } , \ \pmb { e } _ { \bar { 2 } } , \ \pmb { e } _ { \bar { 3 } } \ \cdot$ a righthanded set. Hint: show that

$$
\varepsilon ^ { \alpha \beta \gamma \delta } A _ { \alpha } ^ { \overline { { { 0 } } } } A _ { \beta } ^ { \overline { { { 1 } } } } A _ { \gamma } ^ { \overline { { { 2 } } } } A _ { \delta } ^ { \overline { { { 3 } } } } = - { \operatorname * { d e t } } | A _ { \nu } ^ { \overline { { { \mu } } } } | ;
$$

from $A ^ { T } \eta A = \eta$ ，show that d $\mathsf { e t } | \bar { \Lambda ^ { \mu } } _ { \nu } | = \pm 1$ ； and verify that the determinant is $+ 1$ for transformations between frames with ${ \pmb { e } } _ { 0 }$ and ${ \pmb e } _ { \overline { { 0 } } }$ future-pointing, and with $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ and $e _ { \mathrm { { 1 } } } , e _ { \mathrm { { 2 } } } ,$ ${ \pmb e } _ { \overline { { 3 } } }$ righthanded.

(d） What are the components of $\pmb { \varepsilon }$ in a Lorentz frame with past-pointing ${ \pmb e } _ { \bar { 0 } } { \dagger }$ with lefthanded $\mathscr { e } _ { \bar { 1 } } , \mathscr { e } _ { \bar { 2 } } , \mathscr { e } _ { \bar { 3 } } ?$

(e） From the Levi-Civita tensor,one can construct several“permutation tensors.”In index notation:

$$
\begin{array} { c } { { \delta ^ { \alpha \beta \gamma } { } _ { \mu \nu \lambda } \equiv - \varepsilon ^ { \alpha \beta \gamma \rho } \varepsilon _ { \mu \nu \lambda \rho } ; } } \\ { { { } } } \\ { { \delta ^ { \alpha \beta } { } _ { \mu \nu } \equiv { \displaystyle \frac { 1 } { 2 } } \delta ^ { \alpha \beta \lambda } { } _ { \mu \nu \lambda } = - \frac { 1 } { 2 } \varepsilon ^ { \alpha \beta \lambda \rho } \varepsilon _ { \mu \nu \lambda \rho } ; } } \\ { { { } } } \\ { { \delta ^ { \alpha } { } _ { \mu } \equiv { \displaystyle \frac { 1 } { 3 } } \delta ^ { \alpha \beta } { } _ { \mu \beta } = { \displaystyle \frac { 1 } { 6 } } \delta ^ { \alpha \beta \lambda } { } _ { \mu \beta \lambda } = - \frac { 1 } { 6 } \varepsilon ^ { \alpha \beta \lambda \rho } \varepsilon _ { \mu \beta \lambda \rho } . } } \end{array}
$$

Show that:

$$
\delta ^ { \alpha \beta \gamma } { } _ { \mu \nu \lambda } = { \left\{ \begin{array} { l l } { + { \textrm { l i f } } \alpha \beta \gamma { \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } } \mu \nu \lambda , } \\ { - { \textrm { l i f } } \alpha \beta \gamma { \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } } \mu \nu \lambda , } \\ { 0 { \mathrm { ~ o t h e r w i s e } } ; } \end{array} \right. }
$$

$$
\begin{array} { r l } & { \delta ^ { \alpha \beta } { } _ { \mu \nu } = \delta ^ { \alpha } { } _ { \mu } \delta ^ { \beta } { } _ { \nu } - \delta ^ { \alpha } { } _ { \nu } \delta ^ { \beta } { } _ { \mu } } \\ & { \qquad = \left\{ \begin{array} { l l } { \displaystyle + 1 \mathrm { ~ i f ~ } \alpha \beta \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } \mu \nu , } \\ { \displaystyle - 1 \mathrm { ~ i f ~ } \alpha \beta \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } \mu \nu , } \\ { \qquad \displaystyle 0 \mathrm { ~ o t h e r w i s e } ; } \end{array} \right. } \\ & { \delta ^ { \alpha } { } _ { \mu } = \left\{ \begin{array} { l l } { \displaystyle + 1 \mathrm { ~ i f ~ } \alpha = \mu , } \\ { \displaystyle 0 \mathrm { ~ o t h e r w i s e } . } \end{array} \right. } \end{array}
$$

Exercise 3.14. DUALS

From any vector $\pmb { J }$ ,any second-rank antisymmetric tensor $\pmb { F } ( F _ { \alpha \beta } = F _ { [ \alpha \beta ] } )$ ,and any third-rank antisymmetric tensor $\pmb { \cal B } ( B _ { \alpha \beta \gamma } = B _ { [ \alpha \beta \gamma ] } )$ ,one can construct new tensors defined by

$$
{ } ^ { * } J _ { \alpha \beta \gamma } = J ^ { \mu } \varepsilon _ { \mu \alpha \beta \gamma } , \qquad { } ^ { * } F _ { \alpha \beta } = \frac 1 2 F ^ { \mu \nu } \varepsilon _ { \mu \nu \alpha \beta } , \qquad { } ^ { * } B _ { \alpha } = \frac 1 { 3 ! } B ^ { \lambda \mu \nu } \varepsilon _ { \lambda \mu \nu \alpha } .
$$

One calls $^ { * }$ the“dual”of ${ \pmb J } , \pmb { \imath F }$ the dual of $\pmb { F } ,$ and $\yen 8$ the dual of $\pmb { \ 8 }$ [A previous and entirely distinct use of the word “dual” $( \ S 2 . 7 )$ called a set of basis one-forms $\{ \pmb { \omega } ^ { \alpha } \}$ dual to a set of basis vectors $\{ \pmb { e } _ { \alpha } \}$ if $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { e } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ .Fortunately there are no grounds for confusion between the two types of duality. One relates sets of vectors to sets of l-forms. The other relates antisymmetric tensors of rank $\pmb { p }$ to antisymmetric tensors of rank $4 - p . ]$

(a) Show that

$$
\cdots J = J , \qquad \cdots F = - F , \qquad \cdots B = B .
$$

so (aside from sign） one can recover any completely antisymmetric tensor $\pmb { H }$ from its dual $^ { * } M$ by taking the dual once again, $^ { \ast \ast } M .$ This shows that $\pmb { H }$ and $^ { \ast } M$ contain precisely the same information.

(b) Make explicit this fact of same-information-content by writing out the components $^ \bullet A ^ { \alpha \beta \gamma }$ in terms of $A ^ { \alpha }$ ，also $^ { * } F ^ { \alpha \beta }$ in terms of $F ^ { \alpha \beta }$ also $" B ^ { \alpha }$ in terms of $B ^ { \alpha \beta \Upsilon }$

# Exercise 3.15. GEOMETRIC VERSIONS OF MAXWELL EQUATIONS

Show that, if $\pmb { F }$ is the electromagnetic field tensor, then $\pmb { \nabla } \pmb { \cdot } \pmb { \cdot } \pmb { F } = 0$ is a geometric frame-independent version of the Maxwell equations

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 .
$$

Similarly show that $\pmb { \nabla } \cdot \pmb { F } = 4 \pi \pmb { J }$ (divergence on second slot of $\pmb { F }$ ） is a geometric version of $F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha }$

# Exercise 3.16. CHARGE CONSERVATION

From Maxwel's equations $F ^ { \alpha \beta } { } _ { , \beta } = 4 \pi J ^ { \alpha }$ ，derivehe“eqatiofcargecoseatio”

$$
{ J ^ { \alpha } } _ { , \alpha } = 0 .
$$

Show that this equation does, indeed, correspond to conservation of charge. It will be studied further in Chapter 5.

# Exercise 3.17. VECTOR POTENTIAL

The vector potential $\pmb { A }$ of electromagnetic theory generates the electromagnetic field tensor via the geometric equation

$$
{ \pmb F } = - ( \mathrm { a n t i s y m m e t r i c ~ p a r t ~ o f ~ } { \pmb v } { \pmb A } ) ,
$$

$$
F _ { \mu p } = A _ { \nu , \mu } - A _ { \mu , \nu } .
$$

(a) Show that the electric and magnetic felds in a specific Lorentz frame are given by

$$
\pmb { { \cal B } } = \pmb { \nabla } \times \pmb { A } , \pmb { { \cal E } } = - \partial \pmb { A } / \partial t - \pmb { \nabla } \pmb { A } ^ { 0 } .
$$

(b) Show that $\pmb { \ F }$ will satisfy Maxwel's equations if and only if $\pmb { A }$ satisfies

$$
{ \cal A } ^ { \alpha , \mu } { } _ { , \mu } - { \cal A } ^ { \mu } { } _ { , \mu } { } ^ { , \alpha } = - 4 \pi J ^ { \alpha } { } .
$$

(c) Show that “gauge transformations"

$$
A _ { \mathrm { N E W } } = A _ { \mathrm { 0 L D } } + d \phi , \qquad \phi = \mathrm { a r b i t r a r y ~ f u n c t i o n } ,
$$

leave $\pmb { F }$ unaffected.

(d) Show that one can adjust the gauge so that

$$
\begin{array} { c } { { \pmb { \nabla } \cdot \pmb { A } = 0 ~ ( \mathrm { ^ { * } L o r e n t z ~ \underline { { { g } } } a u g e ^ { * } } ) , } } \\ { { \sqcup _ { \pmb { A } } = - 4 \pi \pmb { J } . } } \end{array}
$$

Here $\sqcap$ is the wave operator ("d'Alembertian"):

$$
\begin{array} { r } { \bigtriangledown \pmb { A } = A ^ { \alpha , \mu } , } \end{array}
$$

# Exercise 3.18. DIVERGENCE OF ELECTROMAGNETIC STRESS-ENERGY TENSOR

From an electromagnetic field tensor $\pmb { F } ,$ one constructs a second-rank,symmetric tensor $\pmb { \tau }$ ("stress-energy tensor,” to be studied in Chapter 5) as follows:

$$
T ^ { \mu \nu } = \frac { 1 } { 4 \pi } \Big ( F ^ { \mu \alpha } { F ^ { \nu } } _ { \alpha } - \frac { 1 } { 4 } \eta ^ { \mu \nu } F _ { \alpha \beta } F ^ { \alpha \beta } \Big ) .
$$

As an exercise in index gymnastics:

(a) Show that $\pmb { \nabla } \pmb { \cdot } \pmb { \tau }$ has components

$$
T ^ { \mu \nu } { } _ { , \nu } = \frac { 1 } { 4 \pi } \bigg [ F ^ { \mu \alpha } { } _ { , \nu } F _ { \alpha } ^ { \nu } + F ^ { \mu \alpha } F _ { \alpha , \nu } ^ { \nu } - \frac { 1 } { 2 } F _ { \alpha \beta } { } ^ { , \mu } F ^ { \alpha \beta } \bigg ] .
$$

(b)Manipulate this expression into the form

$$
T _ { \mu } ^ { \nu } { } _ { , \nu } ^ { \nu } = \frac 1 { 4 \pi } \biggl [ - F _ { \mu \alpha } F ^ { \alpha \nu } { } _ { , \nu } - \frac 1 2 F ^ { \alpha \beta } ( F _ { \alpha \beta , \mu } + F _ { \mu \alpha , \beta } + F _ { \beta \mu , \alpha } ) \biggr ] ;
$$

note that the first term of (3.62) arises directly from the second term of (3.61).

(c) Use Maxwell's equations to conclude that

$$
T ^ { \mu \nu } { } _ { , \nu } = - F ^ { \mu \alpha } J _ { \alpha } .
$$
