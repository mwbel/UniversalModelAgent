CHAPTER 5

# STRESS-ENERGY TENSOR AND CONSERVATION LAWS

# \$5.1. TRACK-1 OVERVIEW

“Geometry tells matter how to move,and matter tels geometry how to curve.” However, it will do no good to look into curvature (Part III） and Einstein's law for the production of curvature by mass-energy (Part IV) until a tool can be found to determine how much mass-energy there is in a unit volume. That tool is the stress-energy tensor.It is the focus of attention in this chapter.

The essential features of the stress-energy tensor are summarized in Box 5.l for the benefit of readers who want to rush on into gravitation physics as quickly as possible. Such readers can proceed directly from Box 5.l into Chapter 6-though by doing so,they close the door on several later portions of track two,which lean heavily on material treated in this chapter.

# $\$ 5.2$ . THREE-DIMENSIONAL VOLUMES AND DEFINITION OF THE STRESS-ENERGY TENSOR

The rest of this chapter is   
Track 2. It depends on no preceding   
Track-2 material. It is needed as preparation   
for Chapter 20 (conservation   
laws for mass and angular   
momentum). It will be extremely helpful in   
all applications of gravitation   
theory (Chapters 18-40).

Spacetime contains a flowing “river”of 4-momentum. Each particle carries its 4-momentum vector with itself along its world line. Many particles, on many world lines,viewed in a smeared-out manner (continuum approximation)，produce a continuum flow-a river of 4-momentum.Electromagnetic fields,neutrino fields, meson fields: they too contribute to the river.

How can the flow of the river be quantified? By means of a linear machine: the stress-energy tensor $\pmb { \tau } .$

Choose a small, three-dimensional parallelepiped in spacetime with vectors $\pmb { A }$ ， B, C for edges (Figure 5.l). Ask how much 4-momentum crosses that volume in

# Box 5.1 CHAPTER 5 SUMMARIZED

# A. STRESS-ENERGY TENSOR AS A MACHINE

At each event in spacetime, there exists a stress-energy tensor. It is a machine that contains a knowledge of the energy density，momentum density,and stress as measured by any and al observers at that event. Included are energy, momentum, and stress associated with all forms of matter and all nongravitational fields.

The stress-energy tensor is a linear, symmetric machine with two slots for the insertion of two vectors: $\pmb { \tau } ( \dots , \dots )$ . Its output, for given input, can be summarized as follows.

(l） Insert the 4-velocity $\pmb { u }$ of an observer into one of the slots; leave the other slot empty. The output is

$$
\pmb { \tau } ( u , . . . ) = \pmb { \tau } ( . . . , u ) = - \left( \begin{array} { l } { \mathrm { d e n s i t y ~ o f ~ 4 - m o m e n t u m , } } \\ { \ast \epsilon _ { d } p / d V _ { \ast } ^ { \ast } , \mathrm { i . e . , ~ 4 - m o m e n t u m } } \\ { \mathrm { p e r ~ u n i t ~ o f ~ t h r e e - d i m e n s i o n a l ~ v o l u m e , } } \\ { \mathrm { a s ~ m e a s u r e d ~ i n ~ o b s e r v e r ' s } } \\ { \mathrm { L o r e n t z ~ f r a m e ~ a t ~ e v e n t ~ w h e r e } } \\ { \pmb { \tau } \mathrm { ~ i s ~ c h o s e n } } \end{array} \right) ;
$$

i.e., $T ^ { \alpha } { } _ { \beta } u ^ { \beta } = T _ { \beta } { } ^ { \alpha } u ^ { \beta } = - ( d p ^ { \alpha } / d V )$ for observer with 4-velocity $u ^ { \alpha }$

(2) Insert 4-velocity of observer into one slot; insert an arbitrary unit vector $\pmb { n }$ into the other slot. The output is

$$
\pmb { T } ( \pmb { u } , \pmb { n } ) = \pmb { T } ( \pmb { n } , \pmb { u } ) = - \left( \begin{array} { l l } { \mathrm { c o m p o n e n t , ~ } ^ { \pmb { \mathrm { c o } } } \pmb { n } \cdot d \pmb { p } / d V ^ { \nu , \mp } , \mathrm { ~ o f ~ } } \\ { 4 \mathrm { - m o m e n t u m ~ d e n s i t y ~ a l o n g ~ t h e } } \\ { \pmb { n } \mathrm { ~ d i r e c t i o n , ~ a s ~ m e a s u r e d ~ i n ~ } } \\ { \mathrm { o b s e r v e r ' s ~ L o r e n t z ~ f r a m e ~ } } \end{array} \right) ;
$$

i.e., $T _ { \alpha \beta } u ^ { \alpha } n ^ { \beta } = T _ { \alpha \beta } n ^ { \alpha } u ^ { \beta } = - n _ { \mu } d p ^ { \mu } / d V .$

(3） Insert 4-velocity of observer into both slots. The output is the density of massenergy that he measures in his Lorentz frame:

$$
\pmb { \cal T } ( u , u ) = \binom { \mathrm { m a s s - e n e r g y ~ p e r ~ u n i t ~ v o l u m e ~ a s ~ m e a s u r e d } } { \mathrm { i n ~ f r a m e ~ w i t h ~ 4 \mathrm { - v e l o c i t y } ~ } u } .
$$

(4） Pick an observer and choose two spacelike basis vectors, $\pmb { e } _ { j }$ and ${ \pmb { \theta } } _ { k }$ ,of his Lorentz frame. Insert $\pmb { \theta } _ { j }$ and ${ \pmb \theta } _ { k }$ into the slots of ${ \pmb { \tau } }$ The output is the $^ { j , k }$ component of the stress as measured by that observer:

$$
T _ { j k } = { \pmb { \tau } } ( \pmb { e } _ { j } , \pmb { e } _ { k } ) = { \pmb { \tau } } _ { k j } = { \pmb { \tau } } ( \pmb { e } _ { k } , \pmb { e } _ { j } )
$$

# B. STRESS-ENERGY TENSOR FOR A PERFECT FLUID

One type of matter studied extensively later in this book is a “perfect fluid."A perfect fluid is a fluid or gas that (l) moves through spacetime with a 4-velocity $\pmb { u }$ which may vary from event to event, and (2) exhibits a density of mass-energy $\pmb { \rho }$ and an isotropic pressure $p$ in the rest frame of each fluid element. Shear stresses,anisotropic pressures,and viscosity must be absent, or the fluid is not perfect.The stress-energy tensor for a perfect fluid at a given event can be constructed from the metric tensor, $\pmb { \sigma }$ the 4-velocity, $\pmb { u }$ ,and the rest-frame density and pressure, $\pmb { \rho }$ and $p$ ：

$$
\pmb { \cal T } = ( \rho + p ) \pmb { u } \otimes \pmb { u } + p \pmb { \mathscr { G } } , \qquad \mathrm { o r } ~ T _ { \alpha \beta } = ( \rho + p ) u _ { \alpha } u _ { \beta } + p g _ { \alpha \beta } .
$$

In the fluid's rest frame, the components of this stress-energy tensor have the expected form (insert into a slot of $\pmb { \tau } ,$ as 4-velocity of observer, just the fluid's 4-velocity):

$$
T ^ { \alpha } { } _ { \beta } u ^ { \beta } = [ ( \rho + p ) u ^ { \alpha } u _ { \beta } + p \delta ^ { \alpha } { } _ { \beta } ] u ^ { \beta } = - ( \rho + p ) u ^ { \alpha } + p u ^ { \alpha } = - \rho u ^ { \alpha } ;
$$

i.e.,

$$
\begin{array} { r l } & { T ^ { 0 } { } _ { \beta } u ^ { \beta } = - \rho = - \mathrm { ( m a s s - e n e r g y ~ d e n s i t y ) } = - d p ^ { 0 } / d V , } \\ & { T ^ { j } { } _ { \beta } u ^ { \beta } = 0 = - \mathrm { ( m o m e n t u m ~ d e n s i t y ) } = - d p ^ { j } / d V ; } \end{array}
$$

also

$$
T _ { j k } = T ( e _ { j } , e _ { k } ) = p \delta _ { j k } = \mathrm { s t r e s s \mathrm { - } t e n s o r \ c o m p o n e n t s } .
$$

# C. CONSERVATION OF ENERGY-MOMENTUM

In electrodynamics the conservation of charge can be expressed by the differential equation

$$
\partial ( \mathrm { c h a r g e ~ d e n s i t y } ) / \partial t + { \boldsymbol { \nabla } } \cdot ( \mathrm { c u r r e n t ~ d e n s i t y } ) = 0 ;
$$

i.e.， ${ J ^ { 0 } } _ { , 0 } + \nabla \cdot \boldsymbol { J } = 0$ ；i.e. ${ J ^ { \alpha } } _ { , \alpha } = 0$ ；i.e.， $\begin{array} { r } { \pmb { \nabla } \pmb { \cdot } \pmb { J } = 0 } \end{array}$ Similarly， conservation of energy-momentum can be expressed by the fundamental geometric law

$$
\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { \nabla } \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \ \end{array}
$$

(Because $\pmb { \tau }$ is symmetric,it does not matter on which slot the divergence is taken.) This law plays an important role in gravitation theory.

![](images/c6c88bb418e2691264d6a082c8d9de37f68cd3126bb465f6bfea8de7a1f98e09.jpg)  
Figure 5.1. The“river”of 4-momentum flowing through spacetime,and three different 3-volumes across which it flows.(One dimension is suppressed from the picture；so the 3-volumes look like 2-volumes.） The first 3-volume is the interior of a cubical soap box momentarilyat rest in the depicted Lorentz frame.Its edges are $L { \pmb \theta } _ { z } , L { \pmb e } _ { y } , L { \pmb \theta } _ { z }$ ：and its volume l-form,with“positive”sense toward future ("standard orientation"), is $\xi \stackrel { \cdot } { = } L ^ { 3 } \dot { d t } = - V \pmb { u } ( V = L ^ { 3 } =$ volume as measured in rest frame; $\pmb { \mathscr { u } } = - \pmb { \mathscr { d } } \pmb { \mathscr { t } } = 4$ velocity of box).The second 3-volume is the“world sheet”swept out in time $\pmb { A } \tau$ by the top of a second cubical box.The box top's edges are $L e _ { z }$ and $L \pmb { \theta } _ { z }$ ；and its volume l-form,with“positive”sense away from the box'sinterior,indirectionof increasing $y _ { i }$ is $\pmb { \Sigma } = L ^ { 2 } \Delta \tau d y = a$ △Tg $\scriptstyle \mathcal { Q } = L ^ { 2 } =$ area of box top; $\sigma = d y =$ unit l-form containing world tube).The third 3-volume is an arbitrary one,with edges $\pmb { A }$ ， $\pmb { \cal B }$ ， $\pmb { c }$ and volume l-form $\begin{array} { r } { \Sigma _ { \mu } = \epsilon _ { \mu \alpha \beta \gamma } A ^ { \alpha } B ^ { \beta } C ^ { \gamma } } \end{array}$

its positive sense (i.e.,from its “negative side” toward its “positive side").To calculate the answer:(l) Construct the “volume $\boldsymbol { \mathit { l } }$ -form"

Mathematical representation of 3-volumes

$$
\begin{array} { r } { \textstyle \sum _ { \mu } = + \epsilon _ { \mu \alpha \beta \gamma } A ^ { \alpha } B ^ { \beta } C ^ { \gamma } ; } \end{array}
$$

the parallelepiped lies in one of the 1-form surfaces, and the positive sense across the parallelepiped is defined to be the positive sense of the 1-form $\pmb { \cal \Sigma }$ (2） Insert this volume 1-form into the second slot of the stress-energy tensor $\pmb { \tau }$ The result is

$$
\pmb { \tau } _ { ( . . . , \pmb { \tau } ) } = \pmb { p } = \left( \begin{array} { l } { \mathrm { m o m e n t u m ~ c r o s s i n g ~ f r o m } } \\ { \mathrm { n e g a t i v e ~ s i d e ~ t o w a r d ~ p o s i t i v e ~ s i d e } } \end{array} \right) .
$$

Momentum crossing a 3-volume caiculated,using stress-energy tensor

(3) To get the projection of the 4-momentum along a vector w or l-form $\pmb { \alpha }$ ,insert the volume l-form $\pmb { \cal \Sigma }$ into the second slot and $\pmb { w }$ or $\pmb { \alpha }$ into the first:

$$
\pmb { \tau } ( w , \pmb { \Sigma } ) = w \cdot p , \qquad \pmb { \tau } ( \alpha , \pmb { \Sigma } ) = \langle \alpha , p \rangle .
$$

This defines the stress-energy tensor.

The key features of 3-volumes and the stress-energy tensor are encapsulated by the above three-step procedure. But encapsulation is not sufficient; deep understanding is also required.To gain it, one must study special cases,both of 3-volumes and of the operation of the stress-energy machinery.

# A Special Case

Interior of a soap box:

A soap box moves through spacetime. A man at an event $\mathcal { P } _ { 0 }$ on the box's world line peers inside it,and examines all the soap,air,and electromagnetic fields it eontains. He adds up alltheir 4-momenta to get a grand total $\pmb { p } _ { \mathtt { b o x } \ a \ t \mathcal { P } _ { 0 } }$ . How much is this grand total? One can calculate it by noting that the 4-momentum inside the box at $\mathcal { P } _ { 0 }$ is precisely the 4-momentum crossing the box from past toward future there (Figure 5.1). Hence, the 4-momentum the man measures is

$$
\begin{array} { r } { \pmb { p } _ { \mathrm { b o x \ a t } \mathscr { S } _ { 0 } } = \pmb { \tau } ( \dots , \pmb { \Sigma } ) , } \end{array}
$$

Its volume 1-form

where $\pmb { \cal \Sigma }$ is the box's volume l-form at $\mathcal { P } _ { 0 }$ .But for such a soap box, $\pmb { \cal \Sigma }$ has a magnitude equal to the box's volume $V$ as measured by a man in its momentary rest frame,and the box itself lies in one of the hyperplanes of $\pmb { \cal \Sigma }$ ; equivalently,

$$
\pmb { \Sigma } = - V \pmb { u } ,
$$

Its 4-momentum content

where $\pmb { u }$ is the soap box's 4-velocity at $\mathcal { P } _ { 0 }$ (minus sign because $\pmb { u }$ ,regarded as a 1-form, has positive sense toward the past, $u _ { 0 } < 0$ )； see Box 5.2.Hence,the total 4-momentum inside the box is

$$
\pmb { p } _ { \mathrm { b o x \ a t } \varphi _ { 0 } } = \pmb { \tau } ( \dots , - V \pmb { u } ) = - V \pmb { \tau } ( \dots , \pmb { u } ) ,
$$

or, in component notation,

$$
( p ^ { \alpha } ) _ { \mathrm { b o x \ a t } \varphi _ { 0 } } = - V T ^ { \alpha \beta } u _ { \beta } .
$$

The energy in the box, as measured in its rest frame, is minus the projection of the 4-momentum on the box's 4-velocity:

$$
\begin{array} { r } { E = - \pmb { u } \cdot \pmb { p } _ { \mathrm { b o x } , \alpha \pmb { \imath \jmath } _ { 0 } } = + V T ^ { \alpha \beta } u _ { \alpha } u _ { \beta } = V \pmb { T } ( \pmb { u } , \pmb { u } ) ; } \end{array}
$$

so

Its energy density

$$
{ \begin{array} { r l } & { { \mathrm { e n e r g y ~ d e n s i t y ~ a s } } } \\ & { { \Big | } { \frac { \mathrm { m e a s u r e d ~ i n ~ b o x ^ { \circ } s } } { \mathrm { r e s t ~ f r a m e } } } { \Big | } = \cdot { \frac { E } { V } } = { \pmb { \tau } } ( { \pmb { u } } , { \pmb { u } } ) . } \end{array} }
$$

# Another Special Case

A man riding with the same soap box opens its top and pours out some soap. In a very small interval of time $\pmb { \mathscr { s } } \tau$ ,how much total 4-momentum flows out of the box?

A.General Parallelepiped

1. Edges of parallelepiped are three vectors $\pmb { A }$ ， B, C. One must order the edges; e.g.,“A is followed by $\pmb { B }$ is followed by $\pmb { c }$ ”

![](images/4d9d2112c6c54732aa4898a4e469a256da81b4fcb5538065c9df9cc3b064a176.jpg)  
(One dimension,that orthogonal to the parallelepiped,is suppressed here.)

2. Volume trivector is defined to be $\pmb { A } \wedge \pmb { B } \wedge \pmb { C } .$ It enters into the sophisticated theory of volumes (Chapter 4), but is not used much in the elementary theory.

3. Volume 1-form is defined by $\begin{array} { r } { \Sigma _ { \mu } = \epsilon _ { \mu \alpha \beta \gamma } A ^ { \alpha } B ^ { \beta } C ^ { \gamma } } \end{array}$ (A,B, $\pmb { c }$ must appear here in standard order as chosen in step 1.) Note that the vector “corresponding” to $\pmb { \cal { \Sigma } }$ and the volume trivector are related by $\pmb { \Sigma } = - \mathbf { \nabla } ^ { * } ( \pmb { A } \wedge \pmb { B } \wedge \pmb { C } )$

4. Orientation of the volume is defined to agree with the orientation of its 1-form $\pmb { \cal \Sigma }$ More specifically: the edges A, B, $\pmb { c }$ lie in a hyperplane of $\pmb { \Sigma } ( \langle \pmb { \Sigma } , \pmb { A } \rangle = \langle \pmb { \Sigma } , \pmb { B } \rangle = \langle \pmb { \Sigma } , \pmb { C } \rangle = 0$ no “bongs of bell"). Thus, the volume itself is one of $\pmb { \Sigma } \bar { \pmb { s } }$ hyperplanes！ The positive sense moving away from the volume is defined to be the positive sense of $\pmb { \cal { \Sigma } }$ Note: reversing the order of A, B, $\pmb { c }$ reverses the positive sense!

![](images/47bc5ee36a820b1f7fcc82278706505effb5da28e862e86407c0088fd6494505.jpg)  
(One dimension,that along which $\pmb { c }$ extends,is suppressed here.)

5. The “standard orientation” for a spacelike 3-volume has the positive sense of the 1-form $\pmb { \cal \Sigma }$ toward the future, corresponding to A,B, $\pmb { c }$ forming a righthanded triad of vectors.

# B. 3-Volumes of Arbitrary Shape

Can be analyzed by being broken up into union of paralelepipeds.

# C. Interior of a Soap Box (Example)

1. Analysis in soap box's rest frame. Pick an event on the box's world line. The box's three edges there are three specifc vectors A,B,C.In the box's rest frame they are purely spatial: $A ^ { 0 } = B ^ { 0 } = C ^ { 0 } = 0$ .Hence, the volume l-form has components $\Sigma _ { j } = 0$ and

$\Sigma _ { 0 } = \epsilon _ { 0 i j k } A ^ { i } B ^ { j } C ^ { k } = \operatorname * { d e t } \left| \left| { \cal B } ^ { 1 } \begin{array} { c c c } { { A ^ { 2 } } } & { { A ^ { 3 } } } \\ { { B ^ { 1 } } } & { { B ^ { 2 } } } & { { B ^ { 3 } } } \\ { { C ^ { 1 } } } & { { C ^ { 2 } } } & { { C ^ { 3 } } } \end{array} \right| \right|$   
$\mathbf { \partial } = \pmb { A } \cdot ( \pmb { B } \times \pmb { C } )$ ,in the standard notation of 3-dimensional vector analysis;   
$= + V$ $V =$ volume of box） if $( A , B , C )$ are righthand ordered (positive sense of $\pmb { \cal \Sigma }$ toward future; standard orientation);   
$\ c = - V$ （ $V =$ volume of box) if $( A , B , C )$ are lefthand ordered (positive sense of $\pmb { \cal \Sigma }$ toward past).

2.This result reexpressed in geometric language: Let $\pmb { u }$ be the box's 4-velocity and $V$ be its volume,as measured in its rest frame.Then either

$\pmb { \Sigma } = - \pmb { V } \pmb { u } ,$ ,in which case the“positive side”of the box's 3-surface is the future side, and its edges are ordered in a righthanded manner-the standard orientation;

or else

$\pmb { \Sigma } = + \pmb { V } \pmb { u }$ ,in which case the“positive side”is the past side,and the box's edges are ordered in a lefthanded manner.

# D. 3-Volume Swept Out in Time $\varDelta \tau$ by Two-Dimensional Top of a Soap Box (Example)

1. Analysis in box's rest frame: Pick an event on box's world line. There the two edges of the box top are vectors $\pmb { A }$ and B.In the box's rest frame,orient the space axes so that $\pmb { A }$ and $\pmb { \ 8 }$ lie in the $y , z$ -plane. During the lapse of a proper time $\pmb { \mathscr { \mathbf { \ell } } } _ { \pmb { \mathcal { \mathbf { 4 } } } \tau }$ ，the box top sweeps out a 3-volume whose third edge is u 4r $( { \pmb u } ) =$ 4-velocity of box). In the box's rest-frame, with ordering $^ { 6 6 } { \bf \sf A }$ followed by $\pmb { \cal B }$ followed by $\pmb { u } \pmb { \mathcal { A } } \tau$ ” the volume l-form has components (Note: No standard orientation can be defined in this case,because $\pmb { \cal \Sigma }$ can be carried continuously into $- \pmb { \Sigma }$ by purely spatial rotations.)

![](images/1c9c58df498e92e5da57ed155240d5f8aa6ae468ce6b012526da41b0f09abd16.jpg)

2. This result reexpressed in geometric language: Let $\boldsymbol { \mathcal { Q } }$ be the area of the box top as measured in its rest frame; and let $\pmb { \sigma }$ be a unit 1-form, one of whose surfaces contains the box top and its 4-velocity (i.e.,contains the box top's “world sheet"). Orient the positive sense of $\pmb { \sigma }$ with the (arbitrarily chosen) positive sense of the box-top 3-volume. Then

$$
\pmb { \cal { \Sigma } } = \pmb { \mathcal { Q } } \pmb { \varDelta \tau } \pmb { \sigma } .
$$

To answer this question, consider the three-dimensional volume swept out during $\pmb { A } \tau$ by the box's opened two-dimensional top ("world sheet of top"). The 4-momentum asked for is the 4-momentum that crosses this world sheet in the positive sense (see Figure 5.l); hence, it is

The top of a soap box:

$$
\begin{array} { r } { \pmb { p } _ { \mathrm { f l o w s o u t } } = \pmb { \mathcal { T } } ( \dots , \pmb { \mathcal { T } } ) , } \end{array}
$$

where $\pmb { \cal \Sigma }$ is the world sheet's volume l-form. Let $\boldsymbol { \mathcal { Q } }$ be the area of the box top,and ·Its volume 1-form $\pmb { \sigma }$ be the outward-oriented unit l-form, whose surfaces contain the world sheet (i.e., contain the box top and its momentary 4-velocity vector). Then

$$
\pmb { \xi } = \pmb { \mathcal { Q } } \ \pmb { \varDelta \tau } \ \pmb { \sigma }
$$

(see Box 5.2); so the 4-momentum that flows out during $\pmb { \mathscr { s } } \tau$ is

Its 4-momentum that flows across

$$
\begin{array} { r } { \pmb { p } _ { \mathrm { f l o w s o u t } } = \pmb { \mathcal { Q } } \ \pmb { \Delta \tau } \pmb { \tau } ( . . . , \pmb { \sigma } ) . } \end{array}
$$

# $\$ 5.3$ . COMPONENTS OF STRESS-ENERGY TENSOR

Like all other tensors, the stress-energy tensor is a machine whose definition and significance transcend coordinate systems and reference frames. But any one observer,locked as he is into some one Lorentz frame,pays more attention to the components of $\pmb { \tau }$ than to $\pmb { \tau }$ itself. To each component he ascribes a specific physical significance.Of greatest interest, perhaps, is the “time-time”component. It is the total density of mass-energy as measured in the observer's Lorentz frame:

Physical interpretation of stress-energy tensor's components:

$$
T _ { 0 0 } = \mathrm { ~ - ~ } T _ { 0 } ^ { \mathrm { ~ ~ 0 ~ } } = T ^ { 0 0 } = T ( e _ { \mathrm { 0 } } , \bullet _ { \mathrm { 0 } } ) = \mathrm { d e n s i t y ~ o f ~ m a s s  – e n e r g y }
$$

$\tau ^ { \circ 0 }$ : energy density

(cf.equation5.7, with theobserver's4-velocity $\pmb { u }$ replaced by the basis vector $\pmb { \mathscr { e } } _ { 0 } = \pmb { \mathscr { u } }$ ）

The“spacetime”components $T ^ { j 0 }$ can be interpreted by considering the interior of a soap box at rest in the observer's frame.If its volume is $V ,$ then its volume 1-form is $\pmb { \Sigma } = - V \pmb { u } = + V \pmb { d t }$ ；and the $\mu$ -component of 4-momentum inside it is

$$
p ^ { \mu } = \langle d x ^ { \mu } , p \rangle = { \pmb { T } } ( d x ^ { \mu } , { \pmb { \Sigma } } ) = V { \pmb { T } } ( d x ^ { \mu } , d t ) = V T ^ { \mu 0 } .
$$

Thus,the 4-momentum per unit volume is

$$
p ^ { \mu } / V = T ^ { \mu 0 } ,
$$

or, equivalently:

$$
\begin{array} { r l } & { T ^ { 0 0 } = \mathrm { d e n s i t y ~ o f ~ m a s s \mathrm { - } e n e r g y } } \\ & { \qquad \mathrm { ( u n i t s : ~ g / c m ^ 3 , ~ o r ~ e r g / c m ^ 3 , ~ o r ~ c m ^ { - 2 } ) } ; } \\ & { T ^ { j 0 } = \mathrm { d e n s i t y ~ o f ~ j \mathrm { - } c o m p o n e n t ~ o f ~ m o m e n t u m } } \\ & { \qquad \mathrm { ( u n i t s : ~ g ~ ( c m / s e c ) ~ c m ^ { - 3 } , ~ o r ~ c m ^ { - 2 } ) } . } \end{array}
$$

The components $T ^ { \mu k }$ can be interpreted using a two-dimensional surface of area $\pmb { \mathcal { q } }$ ,at rest in the observer's frame with positive normal pointing in the $k$ -direction.

During the lapse of time $\pmb { \mathscr { s t } }$ ,this 2-surface sweeps out a 3-volume with volume l-form ${ \pmb { \Sigma } } = { \pmb { \mathcal { I } } }$ 4t $\mathbf { \Delta } \mathbf { \ d { d } } x ^ { k }$ (see Box 5.2). The $\mu$ -component of 4-momentum that crosses the 2-surface in time $\pmb { \mathscr { s t } }$ is

$$
p ^ { \mu } = { \pmb { \mathscr { T } } } ( d x ^ { \mu } , { \pmb { \Sigma } } ) = { \mathscr { Q } } ~ A t ~ { \pmb { \tau } } ( d x ^ { \mu } , d x ^ { k } ) = { \mathscr { Q } } ~ A t ~ T ^ { \mu k } .
$$

Thus,the flux of 4-momentum (4-momentum crossing a unit surface oriented perpendicular to $\pmb { e } _ { k }$ ,in unit time） is

$$
( p ^ { \mu } / \mathcal { Q } ~ \varDelta t ) _ { \mathrm { c r o s s i n g ~ s u r f a c e \perp ~ t o ~ } e _ { k } } = T ^ { \mu k } ,
$$

or, equivalently:

${ \cal T } ^ { 0 k }$ : energy flux

$T ^ { 0 k } = k$ component of energy fux (units: erg/ $\mathbf { \tilde { c } m ^ { 2 } }$ sec, or $\mathsf { c m } ^ { - 2 }$ ；

Tik: stress

$T ^ { j k } = j , k$ component of “stress" $\equiv k$ -component of flux of $j .$ component of momentum $\equiv j$ -component of force produced by fields and matter at $x ^ { k } - \epsilon$ acting on fields and matter at $x ^ { k } + \epsilon$ across a unit surface,the perpendicular to which is $\pmb { e } _ { k }$ (units: dynes/ $\mathrm { ^ { \prime } c m ^ { 2 } }$ ，or $\mathsf { c m } ^ { - 2 }$ ).

(Recall that “momentum transfer per second” is the same as “force.")

The stress-energy tensor is necessarily symmetric, $T ^ { \alpha \beta } = T ^ { \beta \alpha }$ ； but the proof of this will be delayed until several illustrations have been examined.

# \$5.4. STRESS-ENERGY TENSOR FOR A SWARM OF PARTICLES

Consider a swarm of particles. Choose some event $\mathcal { P }$ inside the swarm. Divide the particles near $\mathcal { P }$ into categories, $A = 1 , 2 , \ldots , \operatorname { i n }$ 1 such a way that all particles in the same category have the same properties:

$$
\begin{array} { r l r l } & { m _ { ( A ) } , } & & { \mathrm { r e s t ~ m a s s ; } } \\ & { \pmb { \mathscr { u } } _ { ( A ) } , } & & { 4 \mathrm { - v e l o c i t y ; } } \\ & { p _ { ( A ) } = m _ { ( A ) } \pmb { \mathscr { u } } _ { ( A ) } , } & & { 4 \mathrm { - m o m e n t u m . } } \end{array}
$$

Number-flux vector for swarm of particles defined

Let $N _ { \mathbf { \delta } _ { \mathbf { \delta } } }$ be the number of category $\pmb { A }$ particles per unit volume,as measured in the particles’ own rest frame. Then the “number-flux vector” $\pmb { S } _ { \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } } ( \mathbf { \alpha } _ { \mathbf { \alpha } \mathbf { \alpha } } ) .$ defined by

$$
{ \pmb S } _ { ( A ) } \equiv N _ { { \cal U } } { \pmb u } _ { ( A ) } ,
$$

has components with simple physical meanings.In a frame where category $\pmb { A }$ particles have ordinary velocity $v _ { ( A ) } ,$ the meanings are:

$S _ { \cal G } ^ { 0 } = N _ { \cal G } u _ { \cal G } ^ { 0 } = N _ { \cal G } ) \underbrace { [ \mathrm { ~  ~ \ l ~ } - \nu _ { { \cal G } \cup } { } ^ { 2 } ] ^ { - 1 / 2 } } _ { \mathrm { ~ \displaystyle ~ { \cal ~ t } ~ } } = \mathrm { n u m b e r ~ d e n s i t y } ;$ Number density in Lorentz contraction particles'rest frame factor for volume

$$
S _ { ( { \cal A } ) } = N _ { ( { \cal A } ) } u _ { ( { \cal A } ) } = S _ { ( { \cal A } ) } ^ { 0 } \nu _ { ( { \cal A } ) } = \mathrm { f l u x ~ o f ~ p a r t i c l e s } .
$$

Consequently, the 4-momentum density has components

$$
\begin{array} { c } { { T _ { \cal { ( A ) } } ^ { \mu 0 } = p _ { \cal { ( A ) } } ^ { \mu } S _ { ( A ) } ^ { 0 } = m _ { ( A ) } u _ { ( A ) } ^ { \mu } N _ { ( A ) } u _ { ( A ) } ^ { 0 } } } \\ { { = m _ { ( A ) } N _ { ( A ) } u _ { ( A ) } ^ { \mu } u _ { ( A ) } ^ { 0 } ; } } \end{array}
$$

and the flux of $\mu$ -component of momentum across a surface with perpendicular direction $\pmb { e _ { j } }$ is

$$
\begin{array} { c } { { T _ { \mathcal { \mathrm { U } } } ^ { \mu j } = p _ { \mathcal { \mathrm { U } } } ^ { \mu } S _ { \mathcal { \mathrm { U } } } ^ { j } = m _ { \omega } u _ { \mathrm { U } } ^ { \mu } N _ { \omega } u _ { \mathrm { U } } ^ { j } } } \\ { { = m _ { \omega } N _ { \omega } u _ { \mathrm { U } } ^ { \mu } u _ { \mathrm { U } } ^ { j } u _ { \mathrm { U } } ^ { j } . } } \end{array}
$$

These equations are precisely the $\mu , 0$ and $\mu , j$ components of the geometric, frameindependent equation

$$
\pmb { \tau } _ { \scriptscriptstyle ( A ) } = m _ { \scriptscriptstyle ( A ) } N _ { \scriptscriptstyle ( A ) } \pmb { u } _ { \scriptscriptstyle ( A ) } \otimes \pmb { u } _ { \scriptscriptstyle ( A ) } = \pmb { p } _ { \scriptscriptstyle ( A ) } \otimes \pmb { S } _ { \scriptscriptstyle ( A ) } .
$$

Stress-energy tensor for swarm of particles

The total number-flux vector and stressenergy tensor for all particles in the swarm near $\mathcal { P }$ are obtained by summing over all categories:

$$
\begin{array} { r l } & { \pmb { S } = \displaystyle \sum _ { A } N _ { ( A ) } \pmb { u } _ { ( A ) } ; } \\ & { \pmb { T } = \displaystyle \sum _ { \pmb { A } } m _ { ( A ) } N _ { ( A ) } \pmb { u } _ { ( A ) } \otimes \pmb { u } _ { ( A ) } = \displaystyle \sum _ { \pmb { A } } \pmb { p } _ { ( A ) } \otimes \pmb { S } _ { ( A ) } . } \end{array}
$$

# $\$ 5.5$ . STRESS-ENERGY TENSOR FOR A PERFECT FLUID

There is no simpler example of a fluid than a gas of noninteracting particles ("ideal gas") in which the velocities of the particles are distributed isotropically. In the Lorentz frame where isotropy obtains, symmetry argues equality of the diagonal space-space components of the stress-energy tensor,

Ideal gas defined

$$
T _ { x x } = T _ { y y } = T _ { z z } = \sum _ { A } \frac { m _ { ( A ) } v _ { x ( A ) } } { { ( 1 - { \nu _ { ( A ) } } ^ { 2 } ) ^ { 1 / 2 } } } \frac { N _ { ( A ) } v _ { x ( A ) } } { { ( 1 - { \nu _ { ( A ) } } ^ { 2 } ) ^ { 1 / 2 } } } ,
$$

and vanishing of all the off-diagonal components. Moreover,(5.19) represents a product: the number of particles per unit volume.multiplied by velocity in the $x$ -direction (giving flux in the $x$ -direction) and by momentum in the $x$ -direction,

giving the standard kinetic-theory expression for the pressure, $p$ .Therefore, the stress-energy tensor takes the form

$$
T _ { \alpha \beta } = { \left. \begin{array} { l l l l } { \rho } & { 0 } & { 0 } & { 0 } \\ { 0 } & { p } & { 0 } & { 0 } \\ { 0 } & { 0 } & { p } & { 0 } \\ { 0 } & { 0 } & { 0 } & { p } \end{array} \right. }
$$

in this special Lorentz frame-the “rest frame”of the gas. Here the quantity $\pmb { \rho }$ has nothing directly to do with the rest-masses of the constituent particles. It measures the density of rest-plus-kinetic energy of these particles.

Rewrite (5.20) in terms of the 4-velocity $u ^ { \alpha } = ( 1 , 0 , 0 , 0 )$ of the fluid in the gas's rest frame,and find

$$
\begin{array} { c } { T _ { \alpha \beta } = \left. \begin{array} { c c c c } { \rho } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right. + \left. \begin{array} { c c c c } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { p } & { 0 } & { 0 } \\ { 0 } & { 0 } & { p } & { 0 } \\ { 0 } & { 0 } & { 0 } & { p } \end{array} \right. } \\ { = \rho u _ { \alpha } u _ { \beta } + p ( \eta _ { \alpha \beta } + u _ { \alpha } u _ { \beta } ) , } \end{array}
$$

or, in frame-independent, geometric language

Stress-energy tensor for ideal gas or perfect fluid

Perfect fluid defined

$$
T = p \pmb { g } + ( \rho + p ) \pmb { u } \otimes \pmb { u } .
$$

Expression (5.21) has general application. It is exact for the “ideal gas" just considered.It is also exact for any fluid that is“perfect” in the sense that it is free of such transport processes as heat conduction and viscosity,and therefore (in the rest frame） free of shear stress (diagonal stress tensor； diagonal components identical, because if they were not identical, a rotation of the frame of reference would reveal presence of shear stress). However，for a general perfect fluid,density $\pmb { \rho }$ of mass-energy as measured in the fluid's rest frame includes not only rest mass plus kinetic energy of particles, but also energy of compression,energy of nuclear binding, and all other sources of mass-energy [total density of mass-energy as it might be determined by an idealized experiment, such as that depicted in Figure l.12, with the sample mass at the center ofthe sphere,and the test particle executing oscillations of small amplitude about that location, with $\omega ^ { 2 } = ( 4 \pi / 3 ) \rho ]$

# \$5.6. ELECTROMAGNETIC STRESS-ENERGY

Faraday, with his picture of tensions along lines of force and pressures at right angles to them (Figure 5.2), won insight into new features of electromagnetism.In addition to the tension $E ^ { 2 } / 8 \pi$ (or $B ^ { 2 } / 8 \pi )$ along lines of force,and an equal pressure at right angles, one has the Poynting flux $( { \pmb { E } } \times { \pmb { B } } ) / 4 \pi$ and the Max well expression for the energy density, $( E ^ { 2 } + B ^ { 2 } ) / 8 \pi$ 、All these quantities find their places in the Maxwell stress-energy tensor, defined by

![](images/ccc4e97eb8ddaa0a040b609ac2b4613122f7ac3ee71c3fbee28cc247b71028b7.jpg)  
Figure 5.2. Faraday stresses at work.When the electromagnet is connected to an alternating current,the aluminum ring flies into the air.

$$
4 \pi T ^ { \mu \nu } = F ^ { \mu \alpha } { F ^ { \nu } } _ { \alpha } - { \frac { 1 } { 4 } } { \eta } ^ { \mu \nu } F _ { \alpha \beta } F ^ { \alpha \beta } .
$$

Stress-energy tensor for electromagnetic field

# Exercise 5.1.

EXERCISE

Show that expression (5.22), evaluated in a Lorentz coordinate frame, gives

$$
\begin{array} { l } { { \displaystyle T ^ { 0 0 } = ( E _ { \cdot } ^ { 2 } + B ^ { 2 } ) / 8 \pi , \qquad T ^ { 0 j } = T ^ { j 0 } = ( E \times B ) ^ { j } / 4 \pi , } } \\ { { \displaystyle T ^ { j k } = \frac { 1 } { 4 \pi } \biggl [ - ( E ^ { j } E ^ { k } + B ^ { j } B ^ { k } ) + \frac { 1 } { 2 } ( E ^ { 2 } + B ^ { 2 } ) \delta ^ { j k } \biggr ] . } } \end{array}
$$

Show that the stress tensor does describe a tension $( E ^ { 2 } + B ^ { 2 } ) / 8 \pi$ along the field lines and a pressure $( E ^ { 2 } + B ^ { 2 } ) / 8 \pi$ perpendicular to the field lines,as stated in the text.

# $\$ 5.7$ . SYMMETRY OF THE STRESS-ENERGY TENSOR

All the stres-energy tensors explored above were symmetric. That they could not have been otherwise one sees as follows.

Calculate in a specific Lorentz frame. Consider first the momentum density (components $T ^ { j 0 }$ )and the energy flux (components $T ^ { 0 j }$ ).They must be equal because energ $\gamma = \ m \alpha \ s s$ ${ } ^ { " * } E = M c ^ { 2 } = M " ,$ ：

Proof that stress-energy tensor is symmetric

$$
\begin{array} { r l } & { T ^ { 0 j } = ( \mathrm { e n e r g y ~ f l u x } ) } \\ & { \quad = ( \mathrm { e n e r g y ~ d e n s i t y } ) \times ( \mathrm { m e a n ~ v e l o c i t y ~ o f ~ e n e r g y ~ f l o w } ) ^ { j } } \\ & { \quad = ( \mathrm { m a s s ~ d e n s i t y } ) \times ( \mathrm { m e a n ~ v e l o c i t y ~ o f ~ m a s s ~ f l o w } ) ^ { j } } \\ & { \quad = ( \mathrm { m o m e n t u m ~ d e n s i t y } ) = T ^ { j 0 } . } \end{array}
$$

Only the stress tensor $T ^ { j k }$ remains. For it, one uses the same standard argument as in Newtonian theory. Consider a very small cube,of side $L$ ,mass-energy $T ^ { 0 0 } L ^ { 3 }$ ，

and moment of inertia $\sim T ^ { 0 0 } L ^ { 5 }$ . With the space coordinates centered at the cube, the expression for the $z$ -component of torque exerted on the cube by its surroundings is

$$
 \begin{array} { r l } { \tau ^ { \varepsilon } = } & { \underbrace { ( - T ^ { \nu \varepsilon } L ^ { 2 } ) } _ { ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o n ~ p o n ~ e n t ~ } } ) ( { \mathrm {  ~ \scriptstyle \ L / { \nu } ~ e r ~ } } ) } \ + \ \underbrace { ( T ^ { \nu \varepsilon } L ^ { 2 } ) } _ { ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o n ~ p o n ~ e n t ~ } } ) ( { \mathrm {  ~ \scriptstyle \ k e v e r ~ } } ) } } \\ & { ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r c e ~ } } \ \mathrm {  ~ o n ~ } ) ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r ~ } } \ ) } \\ & { + \ \ x \ \mathrm {  ~ f a c e ~ } \ ) ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r e ~ } } ) \ ( { \begin{array} { c } { { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r ~ } } } \\ { { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r e ~ } } } \\ { { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o c e ~ } } } \end{array} } ) ( { \begin{array} { c } { { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r ~ } } } \\ { { \mathrm { \scriptstyle \sqrt { \pi } ~ o r e ~ } } } \\ { { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ f a c e ~ } } } \end{array} } ) \ ( { \begin{array} { c } { { \mathrm {  ~ \scriptstyle ( - ~ L / 2 ) } } } \\ { { \mathrm { \scriptstyle \sqrt { \pi } ~ o r e ~ } } } \\ { { \mathrm { \scriptstyle \sqrt { \pi } ~ o r e ~ } } } \end{array} } ) } \\ &  \ - \ \underbrace { ( - T ^ { \nu } L ^ { 2 } ) } _ { ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o n ~ e n t ~ } } ) ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r ~ } } ) } \ - \ \underbrace { ( T ^ { \nu \varepsilon } L ^ { 2 } ) } _ { ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r e ~ } } ) \ ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ e v ~ } } ) } \\ &  ( { \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ o r e ~ } } \ \mathrm {  ~ \scriptstyle \sqrt { \pi } ~ i s m ~ } ) (  \begin{array} { c }   \mathrm  \end{array} \end{array}
$$

Since the torque decreases only as $L ^ { 3 }$ with decreasing $L$ ,while the moment of inertia decreases as $L ^ { 5 }$ ,the torque will set an arbitrarily small cube into arbitrarily great angular acceleration-which is absurd.To avoid this,the stresses distribute themselves so the torque vanishes:

$$
T ^ { y x } = T ^ { x y } .
$$

Put differently,if the stresses were not so distributed, the resultant infinite angular accelerations would instantaneously redistribute them back to equilibrium. This condition of torque balance, repeated for all other pairs of directions, is equivalent to symmetry of the stresses:

$$
T ^ { j k } = T ^ { k j } .
$$

# $\$ 5.8$ . CONSERVATION OF 4-MOMENTUM: INTEGRAL FORMULATION

Energy-momentum conservation has been a cornerstone of physics for more than a century. Nowhere does its essence shine forth so clearly as in Einstein's geometric formulation of it (Figure 5.3,a). There one examines a four-dimensional region of spacetime $\mathcal { V }$ bounded by a closed, three-dimensional surface $\partial \mathcal { V }$ .As particles and fields flow into $\mathcal { V }$ and later out, they carry 4-momentum. Inside $\mathcal { V }$ the particles collide, break up,radiate; radiation propagates, jiggles particles, produces pairs. But at each stage in this complex maze of physical processes, total energy-momentum is conserved. The energy-momentum lost by particles goes into fields; the energymomentum lost by fields goes into particles. So finally,when the “river”of 4-momentum exits from $\mathcal { V }$ ，it carries out precisely the same energy-momentum as it carried in.

Integral conservation law for   
4-momentum:   
$\oint _ { \tilde { c } ^ { \prime } \tilde { \jmath } ^ { \prime } } \pmb { \tau } \cdot d ^ { 3 } \pmb { \Sigma } = 0$

Restate this equality by asking for the total flux of 4-momentum outward across $\partial \mathcal { V }$ . Count inflowing 4-momentum negatively. Then “inflow equals outflow” means “total outflow vanishes":

![](images/eac337fb6b010736e832537caa3eec887c949d6a17f45ad88655d5dedfac2f71.jpg)  
(a)A four-dimensional region of spacetime $\cdot \tau$ bounded by a closed three-dimensional surface $\partial ^ { . } \gamma ^ { . }$ . The positive sense of $\partial ^ { \bullet } \vec { \jmath } ^ { \cdot }$ is defined to be everywhere outward (away from $\uparrows$ ). Conservation of energymomentum demands that every bit of 4-momentum which flows into $\bar { \cdot } \bar { \cdot }$ through $\hat { c } ^ { \bullet } \bar { V } ^ { \bullet }$ must somewhere flow back out: none can get lost inside:the interior contains no“sinks.”Equivalently、the total flux of 4-momentum across $\partial ^ { \bullet } \mathcal { T }$ in the positive (outward) sense must be zero:

$$
\oint _ { \partial \dot { \gamma } } T ^ { \mu \alpha } d ^ { 3 } \Sigma _ { \alpha } = 0 .
$$

Figures (b).(c).(d),and (e) depict examples to which the text applies this law of conservation of 4-momentum. All symbols $\cdot \intercal ^ { \ast }$ (or $\mathcal { S }$ ） in these figures mean spacetime volumes (or spacelike 3-volumes) with standard orientations. The dotted arrows indicate the positive sense of the closed surface $\hat { c } ^ { \bullet } \vec { \jmath } ^ { \ast }$ used in the text's discussion of $_ 4$ -momentum conservation. How $\hat { c } ^ { * } \tilde { \jmath } ^ { - }$ is constructed from the surfaces $s$ and $\sqrt [ 4 ] { 1 }$ is indicated by formulas below the figures.For example,in case (b), $\hat { c } ^ { \cdot \dagger } = \mathcal { S } _ { \underline { { { \mathbf { \imath } } } } } - \mathcal { S } _ { \underline { { { \mathbf { \imath } } } } }$ means that $\hat { c } ^ { \dagger }$ is made by joining together $s _ { \because }$ with its standard orientation and ${ \mathcal S } _ { \mathfrak l }$ with reversed orientation.

Total flux of 4-momentum outward across a closed three-dimensional surface must vanish.

To calculate the total outward flux in the most elementary of fashions, approximate the closed 3-surface $\partial \mathcal { V }$ bya large number of flat 3-volumes ("boiler plates") with positive direction oriented outward (away from $\mathcal { V }$ ). Then

$$
\pmb { p } _ { \mathrm { t o t a l o u t } } = \sum _ { \mathrm { b o i l e r p l a t e s } A } \pmb { r } ( . . . , \pmb { \Sigma } _ { \boldsymbol { u } ) } = 0 ,
$$

where $\pmb { \Sigma } _ { \mathbf { \mu } \mathbf { \lambda } \mathbf { \lambda } }$ is the volume 1-form of boiler plate $\pmb { A }$ Equivalently,in component notation

$$
p ^ { \mu } _ { \mathrm { \ t o t a l { o u t } } } = \sum _ { A } T ^ { \mu \alpha } \Sigma _ { \mathrm { \it G l { o u t } } } .
$$

To be slightly more sophisticated about the calculation,take the limit as the number of boiler plates goes to infinity and their sizes go to zero. The result is an integral (Box 5.3,at the end of this section),

$$
p _ { \mathrm { \ t o t a l { o u t } } } ^ { \mu } = \oint _ { \partial \cdot \bar { \nu } ^ { \cdot } } T ^ { \mu \alpha } d ^ { 3 } \Sigma _ { \alpha } = 0 .
$$

Think of this (like all component equations) as a convenient way to express a coordinate-independent statement:

$$
p _ { \mathrm { t o t a l o u t } } = \oint _ { \partial \mathcal { V } } { \pmb { r } } \cdot d ^ { 3 } { \pmb { \Sigma } } = 0 .
$$

To be more sophisticated yet (not recommended on first reading of this book) and to simplify the computations in practical cases, interpret the integrands as exterior differential forms (Box 5.4,at the end of this section).

But however one calculates it,and however one interprets the integrands, the statement of the result is simple: the total flux of 4-momentum outward across a closed 3-surface must vanish.

Several special cases of this “integral conservation law,” shown in Figure 5.3,are instructive. There shown,in addition to the general case (a), are:

# Case (b)

The closed 3-surface $\partial \mathcal { V }$ is made up of two slices taken at constant time t of a specific Lorentz frame, plus timelike surfaces at “infinity” that join the two slices together. The surfaces at infinity do not contribute to $\pmb { \phi } _ { \partial \mathcal { V } } T ^ { \mu \alpha } d ^ { 3 } \pmb { \mathcal { Z } } _ { \alpha }$ if the stress-energy tensor dies out rapidly enough there. The boundary $\partial \mathcal { V }$ of the standard-oriented 4-volume $\mathcal { V }$ ,by definition, has its positive sense away from $\mathcal { V }$ .This demands nonstandard orientation of $\mathcal { S } _ { \mathfrak { r } }$ (positive sense toward past),as is indicated by writing $\partial \mathcal { V } =$ $\mathcal { S } _ { 2 } - \mathcal { S } _ { 1 }$ ; and it produces a sign flip in the evaluation of the hypersurface integral

$$
0 = \oint _ { \partial \mathcal { V } } T ^ { \alpha \mu } d ^ { 3 } \varSigma _ { \mu } = - \int _ { S _ { 1 } } T ^ { \alpha 0 } d x d y d z + \int _ { S _ { 2 } } T ^ { \alpha 0 } d x d y d z .
$$

Because $T ^ { \alpha 0 }$ is the density of 4-momentum, this equation says

$$
{ \begin{array} { r l } & { { \left( \begin{array} { l } { { \mathrm { t o t a l ~ 4 - m o m e n t u m ~ i n } } } \\ { { \mathrm { a l l ~ o f ~ s p a c e ~ a t ~ t i m e ~ } } t _ { 1 } } \end{array} \right) } = \int _ { s _ { 1 } } T ^ { \alpha 0 } d x d y d z } \\ & { \qquad = { \binom { { \mathrm { t o t a l ~ 4 - m o m e n t u m ~ i n } } } { \mathrm { a l l ~ o f ~ s p a c e ~ a t ~ t i m e ~ } } } = \int _ { s _ { 2 } } T ^ { \alpha 0 } d x d y d z . } \end{array} }
$$

Total 4-momentum conserved in time

# Case (c)

Here one wants to compare hypersurface integrals over $s$ and $\overline { { s } }$ ，which are slices of constant time, $t =$ const and $\overline { { t } } =$ const in two different Lorentz frames. To form a closed surface,one adds time-like hypersurfaces at infinity and assumes they do not contribute to the integral. The orientations fit together smoothly and give a closed surface

$$
{ \partial { \mathcal V } = \overline { { \mathcal S } } - \mathcal S + ( \mathrm { s u r f a c e s ~ a t ~ i n f i n i t y } } )
$$

only if one takes $\mathcal { V } = \mathcal { V } _ { 2 } - \mathcal { V } _ { 1 }$ --i.e.,only if one uses the nonstandard 4-volume orientation in $\mathcal { V } _ { 1 }$ . (See part A.l of Box 5.3 for “standard”versus “non-standard" orientation.） The integral conservation law then gives

$$
0 = \int _ { \overline { { \boldsymbol { s } } } } \boldsymbol { \tau } \cdot d ^ { 3 } \pmb { \Sigma } - \int _ { s } \boldsymbol { \tau } \cdot d ^ { 3 } \pmb { \Sigma } ,
$$

or, equivalently,

$$
\begin{array} { r l } { \displaystyle \int _ { \bar { \boldsymbol { s } } } \ \boldsymbol { r } \cdot d ^ { 3 } \boldsymbol { \Sigma } = ( \mathrm { t o t a l \ 4 - m o m e n t u m \ } p \mathrm { \ o n \ } \overline { { \boldsymbol { \mathcal { S } } } } ) } & { } \\ { \displaystyle } & { = \int _ { s } \boldsymbol { r } \cdot d ^ { 3 } \boldsymbol { \Sigma } = ( \mathrm { t o t a l \ 4 - m o m e n t u m \ } p \mathrm { \ o n \ } \mathcal { S } ) . } \end{array}
$$

Total 4-momentum the same in all Lorentz frames

This says that observers in different Lorentz frames measure the same total 4-momentum $\pmb { p }$ . It does not mean that they measure the same components $( p ^ { \alpha } \neq p ^ { \bar { \alpha } } )$ ； rather, it means they measure the same geometric vector

$$
\pmb { p } _ { \mathrm { o n } s } = p ^ { \alpha } \pmb { e } _ { \alpha } = \pmb { p } _ { \mathrm { o n } } \bar { s } = p ^ { \bar { \alpha } } \pmb { e } _ { \alpha } ^ { - } ,
$$

a vector whose components are connected by the usual Lorentz transformation law

$$
p ^ { \alpha } = A ^ { \alpha } { } _ { \bar { \beta } } p ^ { \bar { \beta } } .
$$

Total 4-momentum independent of hypersurface where measured

# Case (d)

Change with time of 4-momentum in a box equals flux of 4-momentum across its faces

Here the contribution to the integral comes entirely from two arbitrary spacelike hypersurfaces, $\mathcal { S } _ { A }$ and $\mathcal { S } _ { B }$ , cutting all the way across spacetime.As in cases (a) and (b),the integral form of the conservation law says

$$
\pmb { p } _ { \mathrm { o n } } \mathscr { s } _ { A } = \pmb { p } _ { \mathrm { o n } } \mathscr { s } _ { B } ;
$$

i.e., the total $^ { 4 }$ -momentum on a spacelike slice through spacetime is independent of the specific slice chosen-so long as the energy-momentum flux across the “hypersurface at infinity” connecting $\mathcal { S } _ { A }$ and $\mathcal { S } _ { B }$ is zero.

# Case (e)

This case concerns a box whose walls oscillate and accelerate as time passes. The three-dimensional boundary $\partial \mathcal { V }$ is made up of (l) the interior S of the box,at an initial moment of time $t =$ constant in the box's initial Lorentz frame, taken with nonstandard orientation; (2） the interior $\overline { { s } }$ of the box, at $\overline { { t } } =$ constant in its final Lorentz frame,with standard orientation; (3) the 3-volume $\mathcal { T }$ swept out by the box's two-dimensional faces between the initial and final states,with positive sense oriented outward. The integral conservation law $\begin{array} { r } { \int _ { \partial \mathcal { V } } \pmb { T } \pmb { \cdot } d ^ { 3 } \pmb { \Sigma } = 0 } \end{array}$ says

$$
\begin{array} { r l } { \mathrm { ~ \gamma _ \mathrm { i n ~ b o x ~ a t ~ \overline { { \mathcal { S } } } ~ } ^ { \prime } u m e n t u m } \Big ) - \Big ( \underset { \mathrm { i n ~ b o x ~ a t ~ \mathcal { S } ~ } } { \mathrm { t o t a l ~ 4 - m o m e n t u m } } \Big ) } & { \cdot } \\ & { \quad \mathrm { ~ \ \Gamma _ \mathrm { i n ~ b o x ~ a t ~ \mathcal { S } ~ } ^ { \prime } u m e n t u m } \Big ( \underset { \mathrm { i n ~ f a c e s ~ b e t w e e n ~ s t a t e s ~ \mathcal { S } ~ \mathrm { a n d } ~ \overline { { \mathcal { S } } } ^ { \prime } } } { \mathrm { ~ \ ~ \ ~ } } \mathrm { t h r o u g h } \Big ) . } \end{array}
$$

# \$5.9. CONSERVATION OF 4-MOMENTUM: DIFFERENTIAL FORMULATION

Complementary to any “integral conservation law in flat spacetime”is a“differential conservation law”with identicalinformation content.To pass back and forth between them,one can use Gauss's theorem.

Gauss's theorem in four dimensions,applied to the law of 4-momentum conserva-tion, converts the surface integral of $T ^ { \mu \alpha }$ into a volume integral of $T ^ { \mu \alpha } { } _ { , \alpha }$ ：

$$
0 = \oint _ { \partial \mathcal { V } } T ^ { \mu \alpha } d ^ { 3 } \Sigma _ { \alpha } = \int _ { \mathcal { V } } T ^ { \mu \alpha } { } _ { , \alpha } d t d x d y d z .
$$

(See Box 5.3 for elementary discussion; Box 5.4 for sophisticated discusson.) If the integral of $T ^ { \mu \alpha } { } _ { , \alpha }$ is to vanish,as demanded, for any and every 4-volume $\mathcal { V }$ ，then $T ^ { \mu \alpha } { } _ { , \alpha }$ must itself vanish everywhere in spacetime:

$$
T ^ { \mu \alpha } { } _ { , \alpha } = 0 ; { \mathrm { ~ i . e . , ~ } } \forall \cdot T = 0 { \mathrm { ~ e v e r y w h e r e } } .
$$

# Box 5.3 VOLUME INTEGRALS, SURFACE INTEGRALS,AND GAUSS'S THEOREM IN COMPONENT NOTATION

# A. Volume Integrals in Spacetime

1. By analogy with thre-dimensional space, the volume of a “hyperparallelepiped”with vector edges ${ \pmb A } , { \pmb B } , { \pmb C } , { \pmb D }$ is

$$
{ \begin{array} { r l } { 4 { \mathrm { - v o l u m e } } \equiv \varOmega \equiv \epsilon _ { \alpha \beta \gamma \delta } A ^ { \alpha } B ^ { \beta } C ^ { \gamma } D ^ { \delta } = { \operatorname* { d e t } } { \left\| \begin{array} { l l l l } { A ^ { 0 } } & { A ^ { 1 } } & { A ^ { 2 } } & { A ^ { 3 } } \\ { B ^ { 0 } } & { B ^ { 1 } } & { B ^ { 2 } } & { B ^ { 3 } } \\ { C ^ { 0 } } & { C ^ { 1 } } & { C ^ { 2 } } & { C ^ { 3 } } \\ { D ^ { 0 } } & { D ^ { 1 } } & { D ^ { 2 } } & { D ^ { 3 } } \end{array} \right\| } } \\ { = { \mathrm { \# } } ( A \wedge B \wedge C \wedge D ) . } \end{array} }
$$

Here,as for 3-volumes, orientation matters; interchange of any two edges reverses the sign of $\pmb { \mathcal { a } }$ The standard orientation for any 4-volume is the one which make: $\pmb { \mathcal { A } }$ positive; thus, ${ \pmb e } _ { 0 } \wedge { \pmb e } _ { 1 } \wedge { \pmb e } _ { 2 } \wedge { \pmb e } _ { 3 }$ has standard orientation if ${ \pmb \theta } _ { 0 }$ points toward the future and $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ are a righthanded triad.

2. The “volume element” whose edges in a specific, standard-oriented Lorentz frame are

$$
A ^ { \alpha } = ( 4 t , 0 , 0 , 0 ) , B ^ { \alpha } = ( 0 , 4 x , 0 , 0 ) , C ^ { \alpha } = ( 0 , 0 , 4 y , 0 ) , D ^ { \alpha } = ( 0 , 0 , 0 , 4 z )
$$

has a 4-volume,according to the above definition, given by

$$
\varDelta ^ { 4 } \varOmega = \epsilon _ { 0 1 2 3 } \varDelta t \varDelta x \varDelta y \varDelta z = \varDelta t \varDelta x \varDelta y \varDelta z .
$$

3. Thus, the volume integral of a tensor $\pmb { S }$ over a four-dimensional region $\mathcal { V }$ of spacetime,defined as

$$
\begin{array} { r l } & { \pmb { M } \equiv \mathrm { ~ \sum ~ } \pmb { \operatorname { L i m } } \sum _ { \pmb { \operatorname { a t c e n t e r o f } } \pmb { \operatorname { \sigma } } } ( \mathrm { v o l u m e ~ o f } \mathcal { Q } ) , } \\ & { \qquad ( \mathrm { e l e m e n t a r y } \atop \mathrm { v o l u m e s } ) ( \mathrm { v o l u m e s } \tilde { \mathcal { U } } ) } \\ & { \qquad \infty } \end{array}
$$

can be calculated in a Lorentz frame by

$$
M ^ { \alpha } { } _ { \beta \gamma } = \int _ { \mathcal { V } } S ^ { \alpha } { } _ { \beta \gamma } d ^ { 4 } \itOmega = \int _ { \mathcal { T } } S ^ { \alpha } { } _ { \beta \gamma } d t d x d y d z .
$$

# Box 5.3 (continued)

# B. Integrals over 3-Surfaces in Spacetime

1. Introduce arbitrary coordinates $a , b , c$ on the three-dimensional surface. The elementary volume bounded by coordinate surfaces

$$
\begin{array} { l } { { a _ { 0 } < a < a _ { 0 } + A a , b _ { 0 } < b < b _ { 0 } + A b , } } \\ { { c _ { 0 } < c < c _ { 0 } + A c } } \end{array}
$$

has edges

$$
A ^ { \alpha } = { \frac { \partial x ^ { \alpha } } { \partial a } } A a , B ^ { \beta } = { \frac { \partial x ^ { \beta } } { \partial b } } A b , C ^ { \gamma } = { \frac { \partial x ^ { \gamma } } { \partial c } } A c ;
$$

so its volume l-form is

![](images/a72b060c8d7080277f0912dd304d94aca9534d57cea9db3b195c4747cf0e5249.jpg)

$$
\varDelta ^ { 3 } \Sigma _ { \mu } = \epsilon _ { \mu \alpha \beta \gamma } \frac { \partial x ^ { \alpha } } { \partial a } \frac { \partial x ^ { \beta } } { \partial b } \frac { \partial x ^ { \gamma } } { \partial c } \varDelta a \varDelta b \varDelta c .
$$

2. The integral of a tensor $\pmb { s }$ over the 3-surface $s$ thus has components

$$
N ^ { \alpha } { } _ { \beta } = \int _ { S } S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } S _ { \gamma } = \int _ { S } S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } \epsilon _ { \gamma \mu \nu \lambda } { \frac { \partial x ^ { \mu } } { \partial a } } { \frac { \partial x ^ { \nu } } { \partial b } } { \frac { \partial x ^ { \lambda } } { \partial c } } d a d b d c .
$$

An equivalent formula involving a Jacobian is often used (see exercise 5.5):

$$
N ^ { \alpha } { } _ { \beta } = \int _ { s } \ S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } { \frac { 1 } { 3 ! } } \epsilon _ { \gamma \mu \nu \lambda } { \frac { \partial ( x ^ { \mu } , x ^ { \nu } , x ^ { \lambda } ) } { \partial ( a , b , c ) } } d a d b d c .
$$

# C. Gauss's Theorem Stated

1. Consider a bounded four-dimensional region of spacetime $\mathcal { V }$ with closed boundary $\partial \mathcal { V }$ Orient the volume l-forms on $\partial \mathcal { V }$ so that the "positive sense” is away from $\mathcal { V }$

2. Choose a tensor field $\pmb { S }$ Integrate its divergence over $\mathcal { V }$ ,and integrate it itself over $\partial \mathcal { V }$ The results must be the same (Gauss's theorem):

![](images/c118967097c5043fc5ddeda09a32671d777af2df65cd88ca9f60f5960f551693.jpg)

$$
\int _ { \mathcal { V } } \ : S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } { } _ { , \gamma } d ^ { 4 } \varOmega = \oint _ { \partial \mathcal { V } } \ : S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } \varSigma _ { \gamma } .
$$

# D. Proof of Gauss's Theorem

1. The indices $\pmb { \alpha }$ and $\beta$ of $S ^ { \alpha } { } _ { \beta } { } ^ { \gamma }$ "go along for afree ride,” so one can suppress them from the proof.Then the equation to be derived is

$$
\int _ { \mathcal { V } } \begin{array} { l } { S ^ { \gamma } , \gamma d t d x d y d z = \oint _ { \partial \mathcal { V } } S ^ { \gamma } d ^ { 3 } \it { \Sigma } _ { \gamma } . } \end{array}
$$

2. Since the integral ofaderivative is just the originalfunction,the volume integral of $S ^ { 0 } { } _ { , 0 }$ is

$$
\begin{array} { r l } {  { \int _ { \mathcal { V } } S ^ { 0 } , _ { 0 } d t d x d y d z } } \\ & { = \int _ { \mathcal { A } \backslash \mathfrak { p } ^ { \psi } } S ^ { 0 } d x d y d z - \int _ { \mathfrak { s } _ { \mathtt { d o w n } } , \mathfrak { p } ^ { \psi } } S ^ { 0 } d x d y d z . } \end{array}
$$

![](images/a386efc84a8e1ab3471806ab36f62b088d7cb2c1e2288782d7257ac479efca42.jpg)

3. The surface integral $\textstyle \int _ { \mathfrak { d } \mathcal { V } } S ^ { 0 } d ^ { 3 } \Sigma _ { 0 }$ can be reduced to the same set of terms: a. Use $x , y , z$ as coordinates on $\partial \mathcal { V }$ .On the“up”side, $d ^ { 3 } { \pmb { \Sigma } } _ { 0 }$ must be positive to achieve a“positive” sense pointing away from $\mathcal { V }$ ，so (see part $\mathbf { B }$ above)

$$
d ^ { 3 } { \cal { S } } _ { 0 } = \epsilon _ { 0 \alpha \beta \gamma } \frac { \partial x ^ { \alpha } } { \partial x } \frac { \partial x ^ { \beta } } { \partial y } \frac { \partial x ^ { \gamma } } { \partial z } d x d y d z = \epsilon _ { 0 1 2 3 } d x d y d z = d x d y d z .
$$

b. On the“down” side, $d ^ { 3 } { \pmb { \Sigma } } _ { 0 }$ must be negative, so

$$
d ^ { 3 } { \cal { Z } } _ { 0 } = - d x d y d z .
$$

c. Hence,

$$
\int _ { \partial V } S ^ { 0 } d ^ { 3 } \Sigma _ { 0 } = \int _ { < _ { \mathrm { \scriptsize { u p } } } , " } S ^ { 0 } d x d y d z - \int _ { < _ { \mathrm { \scriptsize { d o w n } } } , " } S ^ { 0 } d x d y d z .
$$

4. Equality is proved for the other components in the same manner. Adding components produces the result desired:

$$
\int _ { \mathcal { V } } \ S ^ { \gamma } { } _ { , \gamma } d ^ { 4 } \varOmega = \oint _ { \partial \ast \mathcal { V } } \ S ^ { \gamma } d ^ { 3 } \varSigma _ { \gamma } .
$$

# FOR THE READER WHO HAS STUDIED CHAPTER 4

# Box 5.4 I. EVERY INTEGRAL IS THE INTEGRAL OF A FORM. II. THE THEOREM OF GAUSS IN THE LANGUAGE OF FORMS.

I. Every integral encountered in Chapter 5 can be interpreted as the integrul of an exterior differential form. This circumstance shows up in fouiiold .ind threetold integrals, for example, in the fact that

$$
d ^ { 4 } \Omega = \varepsilon = { } ^ { * } \mathrm { l } = \varepsilon _ { 0 1 2 3 } d t \wedge d x \wedge d y \wedge d z
$$

and

$$
d ^ { 3 } \Sigma _ { \mu } = \varepsilon _ { \mu | \alpha \beta \gamma | } d x ^ { \alpha } \wedge d x ^ { \beta } \wedge d x ^ { \gamma }
$$

are basis $_ { 4 \cdot }$ and 3-forms. (Recall:the indices $\mathfrak { a } \beta \gamma$ between vertical bars are to be summed only over $0 \leq \alpha < \beta < \gamma \leq 3 .$ ）A more extensive glossary of notations is found in C below.

II. Gauss's Theorem for a tensor integral in flat space reads

$$
\int _ { \mathcal { V } } \left( \pmb { \nabla } \cdot \pmb { \mathcal { S } } \right) d ^ { 4 } \varOmega = \oint _ { \partial \mathcal { V } } \pmb { \mathcal { S } } \cdot d \pmb { \Sigma }
$$

for any tensor, such as $\pmb { S } = S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { e } _ { \gamma }$ (see Box 5.3 for component form). It is an application of the generalized Stokes Theorem $\mathbf { ( B o x ~ 4 . l ) }$ ,and depends on the fact that the basis vectors ${ \pmb e } _ { \pmb { \alpha } }$ and $\pmb { \omega } ^ { \beta }$ of $\pmb { a }$ global Lorentz frame are constants, i.e.,are independent of $x$ .The definitions follow in A; the proof is in B.

A.Tensor-valued integrals can be defined in flat spaces because one uses constant basis vectors. Thus one defines

$$
\int \pmb { S } \cdot d ^ { 3 } \pmb { \Sigma } = \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \int S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } \pmb { \Sigma } _ { \gamma }
$$

for a tensor of the indicated rank. One justifies pulling basis vectors and forms outside the integral sign because they are constants, independent of location in spacetime. Each of the numbers $\int S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } { \Sigma } _ { \gamma }$ (for $\alpha , \beta = 0 , 1 , 2 , 3 )$ is then evaluated by substituting any properly oriented parametrization of the hypersurface into the 3-form $S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } { \Sigma } _ { \gamma }$ as described in Box 4.l (arbitrary curvilinear parametrization in the part of the calculation not involving the “free indices” $\pmb { \alpha }$ and $\beta$ ).In other words, $\pmb { S } \cdot d ^ { 3 } \pmb { \Sigma } = \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes { S ^ { \alpha } } _ { \beta } ^ { \gamma } d ^ { 3 } { \pmb { \Sigma } } _ { \gamma }$ is considered a“tensor-valued 3-form.” Under an integral sign,it is contracted with the hyperplane element tangent to the 3-surface $\mathcal { P } ( \lambda ^ { 1 } , \lambda ^ { 2 } , \lambda ^ { 3 } )$ of integration to form the integral

$$
\begin{array} { l } { { \displaystyle { \int } \pmb { \mathscr { S } } \cdot d ^ { 3 } \pmb { \Sigma } = \int \left. \pmb { \mathscr { S } } \cdot d ^ { 3 } \pmb { \Sigma } , \frac { \partial \pmb { \mathscr { S } } } { \partial \lambda ^ { 1 } } \wedge \frac { \partial \pmb { \mathscr { S } } } { \partial \lambda ^ { 2 } } \wedge \frac { \partial \pmb { \mathscr { S } } } { \partial \lambda ^ { 3 } } \right. d \lambda ^ { 1 } d \lambda ^ { 2 } d \lambda ^ { 3 } } } \\ { { \displaystyle \qquad = \pmb { e _ { \alpha } } \otimes \pmb { \omega } ^ { \beta } \int \displaystyle { S ^ { \alpha } } _ { \beta } \gamma _ { \pmb { \varepsilon } _ { \gamma } | \lambda \mu \nu | } \frac { \partial ( \pmb { x } ^ { \lambda } , \pmb { x } ^ { \mu } , \pmb { x } ^ { \nu } ) } { \partial ( \lambda ^ { 1 } , \lambda ^ { 2 } , \lambda ^ { 3 } ) } d \lambda ^ { 1 } d \lambda ^ { 2 } d \lambda ^ { 3 } } . }  \end{array}
$$

Although constant basis vectors ${ \pmb e } _ { \alpha } , { \pmb \omega } ^ { \beta }$ derived from rectangular coordinates are essential here, a completely general parametrization of the hypersurface may be used. B. The proof of Gauss's Theorem is a computation:

$$
\begin{array} { r l } { \displaystyle \oint _ { \partial \mathcal { V } } S \cdot d ^ { 3 } E = e _ { \alpha } \otimes \omega ^ { \beta } \displaystyle \int _ { \partial \mathcal { V } } S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } \Sigma _ { \gamma } } \\ { = e _ { \alpha } \otimes \omega ^ { \beta } \displaystyle \int _ { \mathcal { V } } d ( S ^ { \alpha } { } _ { \beta } ^ { \gamma } d ^ { 3 } \Sigma _ { \gamma } ) } \\ { = e _ { \alpha } \otimes \omega ^ { \beta } \displaystyle \int _ { \mathcal { V } } S ^ { \alpha } { } _ { \beta } ^ { \gamma } { } _ { , \gamma } * 1 } \\ { = \displaystyle \int _ { \mathcal { V } } ( \nabla \cdot S ) d ^ { 3 } \varOmega . } \end{array}
$$

(Stokes Theorem)

(merely notation)

The missing computational step above is

$$
\begin{array} { c } { { d ( S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } d ^ { 3 } \Sigma _ { \gamma } ) = ( \partial S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } / \partial x ^ { \rho } ) d x ^ { \rho } \wedge d ^ { 3 } \Sigma _ { \gamma } } } \\ { { = ( \partial S ^ { \alpha } { } _ { \beta } { } ^ { \gamma } / \partial x ^ { \gamma } ) ^ { \ast } 1 . } } \end{array}
$$

Here the first step uses ${ \pmb d } ( d ^ { 3 } { \pmb { \Sigma } } _ { \gamma } ) = 0$ (which follows from $\varepsilon _ { \mu \alpha \beta \gamma } =$ const in flat spacetime).The second step uses

$$
d x ^ { \rho } \wedge d ^ { 3 } \Sigma _ { \gamma } = \delta _ { \gamma } ^ { \rho } { } ^ { * } 1 .
$$

[Write the lefthand side of this identity as $\varepsilon _ { \gamma \vert \mu \nu \lambda \vert } d x ^ { \rho } \wedge d x ^ { \mu } \wedge d x ^ { \nu } \wedge d x ^ { \lambda }$ The only possible non-zero term in the sum over $\mu \nu \lambda$ is the one with $\mu < \nu < \lambda$ all different from $\pmb \rho$ . The righthand side is the value of this term.]

C. Glossary of notations.

Charge density 3-form:

$$
{ } ^ { * } J = J ^ { \mu } d ^ { 3 } { \cal { \Sigma } } _ { \mu } = J \cdot d ^ { 3 } { \cal { \Sigma } }  \\  \underbrace { \phantom { * } = J _ { \therefore } ^ { \mu } \varepsilon _ { \mu \alpha \beta \gamma } d x ^ { \alpha } \wedge d x ^ { \beta } \wedge d x ^ { \gamma } / 3 ! } _ { d ^ { 3 } { \cal { J } } _ { \mu } } ,
$$

Maxwell and Faraday 2-forms:

$$
\begin{array} { l } { { \displaystyle { } ^ { * } F = \frac { 1 } { 2 } F ^ { \mu \nu } d ^ { 2 } S _ { \mu \nu } ; } } \\ { { } } \\ { { \displaystyle F = \frac { 1 } { 2 } F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } . } } \end{array}
$$

Basis 2-forms:

$$
\begin{array} { l } { { { \pmb d x ^ { \alpha } } \wedge { \pmb d x ^ { \beta } } ; } } \\ { { { \pmb d } ^ { 2 } S _ { \mu \nu } = \varepsilon _ { \mu \nu | \alpha \beta | } { \pmb d x ^ { \alpha } } \wedge { \pmb d x ^ { \beta } } . } } \end{array} \nonumber
$$

Energy-momentum density 3-form:

$$
\begin{array} { c } { { { \pmb { T } } { \cdot } d ^ { 3 } { \pmb { \Sigma } } \equiv e _ { \mu } T ^ { \mu \nu } d ^ { 3 } { \pmb { \Sigma } } _ { \nu } \equiv { \pmb { \cdots } } { \pmb { T } } ; } } \\ { { \widetilde { \mathrm { d u a l ~ o n ~ l a s t ~ i n d e x , } } ( { \pmb { \cdots } } T ) _ { ~ \alpha \beta \gamma } ^ { \mu } = T ^ { \mu \nu } \varepsilon _ { \nu \alpha \beta \gamma } . } } \end{array}
$$

Angular momentum density 3-form:

$$
\begin{array} { c } { { \displaystyle { \mathcal { J } } \cdot d ^ { 3 } { \pmb \Sigma } \equiv \frac { 1 } { 2 } { \pmb e } _ { \mu } \wedge { \pmb e } _ { \nu } { \mathcal { J } } ^ { \mu \nu \alpha } d ^ { 3 } { \pmb \Sigma } _ { \alpha } \equiv { } ^ { * } { \mathcal { J } } ; } } \\ { { { } } } \\ { { ( { \bf { \bar { \kappa } } } { \mathcal { J } } ) ^ { \mu \nu } { } _ { \alpha \beta \gamma } = { \mathcal { J } } ^ { \mu \nu \lambda } \varepsilon _ { \lambda \alpha \beta \gamma } . } } \end{array}
$$

(In the frame-independent equation $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \end{array}$ ，one need not worry about which slot of $\pmb { \tau }$ to take the divergence on; the slots are symmetric, so either can be used.)

The equation $\pmb { \nabla } \cdot \pmb { r } = 0$ is the differential formulation of the law of 4-momentum conservation.It is also called the equation of motion for stress-energy, because it places constraints on the dynamic evolution of the stress-energy tensor. To examine these constraints for simple systems is to realize the beauty and power of the equation $\begin{array} { r } { \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { r } = 0 } \end{array}$

Newtonian fluid characterized by $| v ^ { j } | \ll 1 , p \ll \rho$

# \$5.10. SAMPLE APPLICATIONS OF $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \ \end{array}$

The equation of motion $\pmb { \nabla } \cdot \pmb { r } = 0$ makes contact with the classical (Newtonian) equations of hydrodynamics, when applied to a nearly Newtonian fluid.Such a fluid has low velocities relative to the Lorentz frame used, $| v ^ { j } | \leqslant 1$ ；and in its rest frame its pressure is small compared to its density of mass-energy, $p / \rho = p / \rho c ^ { 2 } \ll 1 .$ For example, the air in a hurricane has

$$
| v ^ { j } | \sim 1 0 0 \mathrm { ~ k m } / \mathrm { h o u r } \sim 3 , 0 0 0 \mathrm { ~ c m } / \sec \sim 1 0 ^ { - 7 } \ c = 1 0 ^ { - 7 } \ \ll 1 ,
$$

$$
{ \frac { p } { \rho } } \sim { \frac { 1 \ { \mathrm { a t m o s p h e r e } } } { 1 0 ^ { - 3 } \ { \mathrm { g / c m } } ^ { 3 } } } \sim { \frac { 1 0 ^ { 6 } \ { \mathrm { d y n e s / c m } } ^ { 2 } } { 1 0 ^ { - 3 } \ { \mathrm { g / c m } } ^ { 3 } } } = 1 0 ^ { 9 } \ { \frac { \mathrm { c m } ^ { 2 } } { { \mathrm { s e c } } ^ { 2 } } } \sim 1 0 ^ { - 1 2 } \ c ^ { 2 } = 1 0 ^ { - 1 2 } \ { \mathrm { d } } \ 1 .
$$

Stress-energy tensor and equation of motion for a Newtonian fluid

The stress-energy tensor for such a fluid has components

$$
\begin{array} { r l } & { T ^ { 0 0 } = ( \rho + p ) u ^ { 0 } u ^ { 0 } - p \approx \rho , } \\ & { T ^ { 0 j } = T ^ { j 0 } = ( \rho + p ) u ^ { 0 } u ^ { j } \approx \rho v ^ { j } , } \\ & { T ^ { j k } = ( \rho + p ) u ^ { j } u ^ { k } + p \delta ^ { j k } \approx \rho v ^ { j } v ^ { k } + p \delta ^ { j k } ; } \end{array}
$$

and the equation of motion $\pmb { \nabla } \cdot \pmb { r } = 0$ has components

$$
{ T ^ { 0 0 } } _ { , 0 } + { T ^ { 0 j } } _ { , j } = \partial \rho / \partial t + \nabla \cdot \left( \rho \boldsymbol { \nu } \right) = 0
$$

and

$$
T ^ { j 0 } \mathrm { , } \mathrm { , } \mathrm { ~ } r ^ { j k } \mathrm { , } \mathrm { ~ } k = \partial ( \rho v ^ { j } ) / \partial t + \partial ( \rho v ^ { j } v ^ { k } ) / \partial x ^ { k } \mathrm { ~ } + \partial p / \partial x ^ { j } = 0 \mathrm { , ~ }
$$

or,equivalently (by combining with the equation of continuity),

$$
\begin{array} { r } { { \frac { \partial { \pmb v } } { \partial t } } + ( { \pmb v } \cdot { \pmb \nabla } ) { \pmb v } = - { \frac { 1 } { \rho } } { \pmb \nabla } p } \end{array}
$$

Application of $\begin{array} { r } { \pmb { \nabla } \pmb { \cdot } \pmb { r } = 0 } \end{array}$ to an electrically charged, vibrating rubber block

Box 5.5 derives and discusses these results from the Newtonian viewpoint.

As a second application of $\begin{array} { r } { \mathbf { \nabla } \mathbf { \cdot } \mathbf { \nabla } \pmb { r } = 0 . } \end{array}$ ，consider a composite system: a block of rubber with electrically charged beads imbedded in it, interacting with an electromagnetic field. The block of rubber vibrates,and its accelerating beads radiate electromagnetic waves; at the same time, incoming electromagnetic waves push on the beads,altering the pattern of vibration of the block of rubber.The interactions shove 4-momentum back and forth between beaded block and electromagnetic field.

# Box 5.5 NEWTONIAN HYDRODYNAMICS REVIEWED

Consider a classical, nonrelativistic, perfect fluid.Apply Newton's law $\mathbf { \nabla } \mathbf { F } = m \mathbf { a }$ to a “fluid particle"； that is,to a small fixed mass of fluid followed in its progress through space:

$$
{ \begin{array} { r l } & { { \frac { d } { d t } } \left( { \mathrm { m o m e n t u m ~ p e r ~ u n i t ~ m a s s } } \right) = \left( { \mathrm { f o r c e ~ p e r ~ u n i t ~ m a s s } } \right) } \\ & { \qquad = { \frac { \left( { \mathrm { f o r c e ~ p e r ~ u n i t ~ v o l u m e } } \right) } { \left( { \mathrm { d e n s i t y } } \right) } } = { \frac { - \left( { \mathrm { g r a d i e n t ~ o f ~ p r e s s u r e } } \right) } { \left( { \mathrm { d e n s i t y } } \right) } } } \end{array} }
$$

or

$$
\begin{array} { r } { \frac { d v } { d t } = - \frac { 1 } { \rho } \nabla p . } \end{array}
$$

Translate from time-rate of change following the fluid to time-rate of change as measured at a fixed location, finding

$$
{ \binom { \mathrm { r a t e ~ o f ~ c h a n g e } } { \mathrm { w i t h ~ t i m e } } } = { \binom { \mathrm { r a t e ~ o f ~ c h a n g e } } { \mathrm { w i t h ~ t i m e ~ a t } } } + { \binom { \mathrm { v e l o c i t y } } { \mathrm { o f ~ f u i d } } } \cdot { \binom { \mathrm { r a t e ~ o f ~ c h a n g e } } { \mathrm { w i t h ~ p o s i t i o n } } }
$$

or

$$
\begin{array} { r } { { \frac { \partial { \pmb v } } { \partial t } } + ( { \pmb v } \cdot { \pmb \nabla } ) { \pmb v } = - { \frac { 1 } { \rho } } { \pmb \nabla } p } \end{array}
$$

or

$$
\frac { \partial v _ { i } } { \partial t } + v _ { i , k } v _ { k } = - \frac { 1 } { \rho } p _ { , i } .
$$

(Latin indices run from 1 to 3; summation convention; upper and lower indices used indifferently for space dimensions in flat space!) This is Euler's fundamental equation for the hydrodynamics of a perfect fluid.

Two further equations are needed to complete the description of a perfect fluid. One states the absence of heat transfer by requiring that the specific entropy (entropy per unit mass) be constant for each fluid “particle":

$$
\frac { d s } { d t } = 0 , \qquad \mathrm { o r } \qquad \frac { \partial s } { \partial t } + ( \boldsymbol { v } \cdot \nabla ) s = 0 .
$$

The final equation expresses the conservation of mass:

$$
\frac { \partial \rho } { \partial t } + \nabla \cdot ( \dot { \rho } \boldsymbol { v } ) = 0 ,
$$

$$
\frac { \partial \rho } { \partial t } + \left( \rho v _ { k } \right) _ { , k } = 0 ;
$$

it is analagous in every way'to the equation that expresses conservation of charge in electrodynamics and that bears the same name,“equation of continuity.”

The Newtonian stress-energy tensor, like its relativistic counterpart, is linked to conservation of momentum and mass Therefore examine the time-rate of change of the density of fluid momentum, $\rho v _ { i }$ ,contained in a unit volume; thus,

$$
\partial ( \rho v _ { \mathrm { i } } ) / \partial t = - ( \rho v _ { \mathrm { i } } v _ { \boldsymbol { k } } ) _ { , \boldsymbol { k } } - p _ { , i } .
$$

Momentum flows into the litte volume element on the left (“force equals time-rate of change of momentum")and out on the right; similarly at the other faces.Therefore the righthand side of (5) must represent the divergence of this momentum flux:

$$
\hat { \sigma } ( \rho v _ { i } ) / \hat { c } t = - T _ { i k , k } .
$$

Consequently,we take for the momentum flux itself

$$
T ^ { i k } = T _ { i k } = \underbrace { \rho v _ { i } v _ { k } } _ { \mathrm { \cdots c o n v e c t i o n ^ { 3 } } } + \underbrace { \delta _ { i k } p } _ { \mathrm { \cdots p u s h ^ { 3 } } } .
$$

For the momentum density,the Newtonian value is

$$
T ^ { 0 i } = T ^ { i 0 } = \rho v _ { i } .
$$

With this notation, the equation for the time-rate of change of momentum becomes

$$
\partial T ^ { i \mu } / \partial x ^ { \mu } = 0 ;
$$

and with $T ^ { 0 0 } = \rho$ ,the equation of continuity reads

$$
\partial T ^ { 0 \mu } / \partial x ^ { \mu } = 0 .
$$

In conclusion, these Newtonian considerations give a reasonable approximation to the relativistic stress-energy tensor:

$$
\begin{array} { r } { \Bigg \| \rho \begin{array} { l } { \colon \rho v ^ { j } } \\ { \vdots } \\ { \cdots \ldots \ldots \ldots \ldots \ldots } \\ { \cdot } \\ { \rho v ^ { i } \colon \rho v ^ { i } v ^ { j } + \delta ^ { i j } p } \end{array} \Bigg \| \simeq \Bigg \| \begin{array} { l } { \| ( p + \rho ) u ^ { 0 } u ^ { 0 } - p \vdots ( p + \rho ) u ^ { 0 } u ^ { j } } \\ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { \cdot } \\ { ( p + \rho ) u ^ { 0 } u ^ { i } \qquad : ( p + \rho ) u ^ { i } u ^ { j } + \delta ^ { i j } p } \end{array} \Bigg \| } \end{array}
$$

The 4-momentum of neither block nor feld is conserved; neither V·Tblock nor $\pmb { \nabla } \cdot \pmb { T } _ { ( \mathrm { e m \ f i e l d } ) }$ vanishes. But total 4-momentum must be conserved, so

$$
\pmb { \nabla } \cdot ( \pmb { T } _ { \mathrm { ( b l o c k ) } } + \pmb { T } _ { \mathrm { ( e m f i e l d ) } } ) \ \mathrm { m u s t \ v a n i s h } .
$$

For a general electromagnetic field interacting with any source, $\pmb { \nabla } \cdot \pmb { T } _ { ( \mathrm { e m f i e l d } ) }$ has the form

$$
T _ { \mathrm { ( e m \ t i e l d ) } , \nu } ^ { \mu \nu } = - F ^ { \mu \alpha } J _ { \alpha } .
$$

(This was derived in exercise 3.18 by combining $T ^ { \mu \nu } { } _ { , \nu } = 0$ with expression 5.22 for the electromagnetic stress-energy tensor, and with Maxwell's equations.） For our beaded block, $\pmb { J }$ is the 4-current associated with the vibrating, charged beads, and $\pmb { F }$ is the electromagnetic field tensor. The time component of equation (5.40) reads

$$
\begin{array} { r l } & { T _ { \mathrm { ( e m ~ f i e l d ) , } \nu } ^ { 0 \nu } = - F ^ { 0 k } J _ { k } = - E \cdot J } \\ & { \qquad = - { \binom { \mathrm { r a t e ~ a t ~ w h i c h ~ e l e c t r i c ~ f i e l d ~ } E \mathrm { ~ d o e s ~ w o r k } } { \mathrm { o n ~ a ~ u n i t ~ v o l u m e ~ o f ~ c h a r g e d ~ b e a d s } } } . } \end{array}
$$

For comparison, $T _ { \mathrm { ( b l o c k ) , 0 } } ^ { 0 0 }$ is the rate at which the block's energy density changes with time, $- T _ { \mathrm { ( b l o c k ) } , j } ^ { 0 j }$ is the contribution of the block's energy flux to this rate of changefenegestdoseqetlt $T _ { \mathrm { ( b l o c k ) } , \nu } ^ { 0 \nu }$ has the meaning

$$
T _ { ( \mathrm { b l o c k } ) , \nu } ^ { 0 \nu } = { \binom { \mathrm { r a t e ~ a t ~ w h i c h ~ m a s s - e n e r g y ~ o f ~ b l o c k ~ p e r } } { \mathrm { u n i t ~ v o l u m e ~ i n c r e a s e s ~ d u e ~ t o ~ a c t i o n s } } } _ { \begin{array} { l } { { \mathrm { ~ } } } \\ { { \mathrm { ~ o t h e r ~ t h a n ~ i n t e r n a l ~ m e c h a n i c a l ~ f o r c e s } } } \\ { { \mathrm { ~ b e t w e e n ~ o n e ~ p a r t ~ o f ~ b l o c k ~ a n d ~ a n o t h e r } } } \end{array} }  .
$$

Hence,the conservation law

$$
( T _ { \mathrm { ( e m f i e l d ) } } ^ { 0 \nu } + \ : T _ { \mathrm { ( b l o c k ) } } ^ { 0 \nu } ) _ { , \nu } = 0
$$

says that the mass-energy of the block increases at precisely the same rate as the electric field does work on the beads.A similar result holds for momentum:

$$
\begin{array} { r l } & { T _ { ( \mathrm { e m ~ f i e l d } ) , \nu } ^ { k \nu } \pmb { e } _ { k } = - F ^ { k \nu } J _ { \nu } \pmb { e } _ { k } = - ( J ^ { 0 } E + J \times \pmb { B } ) } \\ & { \quad \quad \quad = - \binom { \mathrm { L o r e n t z ~ f o r c e ~ p e r ~ u n i t ~ v o l u m e } } { \mathrm { a c t i n g ~ o n ~ b e a d s } } , } \end{array}
$$

$$
T _ { ( \mathrm { b l o c k } ) , \nu } ^ { k \nu } \pmb { e } _ { k } = \left( \begin{array} { l } { \mathrm { r a t e ~ a t ~ w h i c h ~ m o m e n t u m ~ p e r ~ u n i t ~ v o l u m e } } \\ { \mathrm { o f ~ b l o c k ~ i n c r e a s e s ~ d u e ~ t o ~ a c t i o n s } } \\ { \mathrm { o t h e r ~ t h a n ~ i t s ~ o w n ~ s t r e s s e s } } \end{array} \right) ;
$$

so the conservation law

$$
( T _ { \mathrm { ( e m f i e l d ) } } ^ { k \nu } + \ T _ { \mathrm { ( b l o c k ) } } ^ { k \nu } ) _ { , \nu } = 0
$$

says that the rate of change of the momentum of the block equals the force of the electromagnetic field on its beads.

Angular momentum defined and its integral conservation law derived

# $\pmb { \ S 5 . 1 1 }$ . ANGULAR MOMENTUM

The symmetry, $T ^ { \mu \nu } = T ^ { \nu \mu }$ ，of the stress-energy tensor enables one to define a conserved angular momentum $J ^ { \alpha \beta }$ ，analogous to the linear momentum $p ^ { \alpha }$ . The angular momentum is defined relative to a specific but arbitrary origin-an event $\pmb { \mathcal { q } }$ with coordinates, in a particular Lorentz frame,

$$
x ^ { \alpha } ( { \mathcal { Q } } ) = a ^ { \alpha } .
$$

The angular momentum about $\boldsymbol { \mathcal { Q } }$ is defined using the tensor

$$
\mathcal { J } ^ { \alpha \beta \gamma } = ( x ^ { \alpha } - a ^ { \alpha } ) T ^ { \beta \gamma } - ( x ^ { \beta } - a ^ { \beta } ) T ^ { \alpha \gamma } .
$$

(Note that $x ^ { \alpha } - a ^ { \alpha }$ is the vector separation of the “field point" $x ^ { \alpha }$ from the“origin” $\mathcal { Q } ; T ^ { \alpha \gamma }$ is here evaluated at the “field point".) Because of the symmetry of $\pmb { \tau } , \pmb { \mathcal { J } } ^ { \alpha \beta \gamma }$ has vanishing divergence:

$$
\begin{array} { c l c } { { \mathcal { J } ^ { \alpha \beta \gamma } { } _ { , \gamma } = \delta ^ { \alpha } { } _ { \gamma } T ^ { \beta \gamma } + ( x ^ { \alpha } - a ^ { \alpha } ) \underbrace { T ^ { \beta \gamma } { } _ { , \gamma } } _ { 0 } - \delta ^ { \beta } { } _ { \gamma } T ^ { \alpha \gamma } - ( x ^ { \beta } - a ^ { \beta } ) \underbrace { T ^ { \alpha \gamma } { } _ { , \gamma } } } } \\ { { { } } } & { { { } } } \\ { { { } = T ^ { \beta \alpha } - T ^ { \alpha \beta } = 0 . } } \end{array}
$$

Consequently, its integral over any closed 3-surface vanishes

$$
\oint _ { \partial \cdot \gamma } \mathcal { J } ^ { \alpha \beta \gamma } d ^ { 3 } \varSigma _ { \gamma } = 0
$$

("integral form of the law of conservation of angular momentum").

The integral over a spacelike surface of constant time $t$ is

$$
J ^ { \alpha \beta } = \int { \mathcal { J } } ^ { \alpha \beta 0 } d x d y d z = \int [ ( x ^ { \alpha } - a ^ { \alpha } ) T ^ { \beta 0 } - ( x ^ { \beta } - a ^ { \beta } ) T ^ { \alpha 0 } ] d x d y d z .
$$

Recalling that $T ^ { \beta 0 }$ is momentum density, one sees that (5.49) has the same form as the equation $\mathbf { \mu } ^ { * } J = r \times p ^ { * }$ of Newtonian theory.Hence the name “total angular momentum" for $\scriptstyle J \alpha \beta$ .Various aspects of this conserved angular momentum,including the tie to its Newtonian cousin, are explored in Box 5.6.

# EXERCISES

# Exercise 5.2. CHARGE CONSERVATION

Exercise 3.16 revealed that the charge-current 4-vectorJsatisfies the differential conservation law $\triangledown \cdot \triangledown = 0$ . Write down the corresponding integral conservation law,and interpret it for the four closed surfaces of Fig. 5.3.

# Exercise 5.3. PARTICLE PRODUCTION

Inside highly evolved, massve stars,the temperature is so high that electron-positron pairs are continually produced and destroyed.Let $\pmb { s }$ be the number-flux vector for electrons and positrons,and denote its divergence by

$$
\epsilon \equiv \forall \cdot \mathbb { S } .
$$

# A. Definition of Angular Momentum

(a) Pick an arbitrary spacelike hypersurface $\mathcal { S }$ and an arbitrary event $\boldsymbol { \mathcal { Q } }$ with coordinates $x ^ { \alpha } ( \mathcal { Q } ) \equiv a ^ { \alpha }$ .(Use globally inertial coordinates throughout.) (b) Define “total angular momentum on $s$ about ${ \mathcal { Q } } ^ { s }$ to be

$$
\begin{array} { r l } {  { J ^ { \mu \nu } \equiv \int _ { S } \mathcal { J } ^ { \mu \nu \alpha } d ^ { 3 } \Sigma _ { \alpha } , } } \\ { \quad } \\ { \quad } \\ { \mathcal { J } ^ { \mu \nu \alpha } \equiv ( x ^ { \mu } - a ^ { \mu } ) T ^ { \nu \alpha } - ( x ^ { \nu } - a ^ { \nu } ) T ^ { \mu \alpha } . } \end{array}
$$

![](images/c6f7a3d4c3ddf3660eade65fc0b36d35dcea28385c4b5bf99f093bdffcfaacf8.jpg)

(c) If $s$ is a hypersurface of constant time $t .$ ，this becomes

$$
J ^ { \mu \nu } = \int \mathcal { J } ^ { \mu \nu 0 } d x d y d z .
$$

# B. Conservation of Angular Momentum

(a) $T ^ { \mu \nu } { } _ { , \nu } = 0$ implies ${ \mathcal { J } } ^ { \mu \nu \alpha } { } _ { , \alpha } = 0$   
(b) This means that $J ^ { \mu \nu }$ is independent ofthe hypersurface Son which it is calculated   
(Gauss's theorem):

$$
\begin{array} { l } { { \displaystyle J ^ { \mu \nu } ( \mathcal { S } _ { A } ) - J ^ { \mu \nu } ( \mathcal { S } _ { B } ) } } \\ { { \displaystyle ~ = \int _ { \mathfrak { d } ^ { \mathcal { N } } } \mathcal { J } ^ { \mu \nu \alpha } d ^ { 3 } \mathcal { S } _ { \alpha } } } \\ { { \displaystyle ~ = \int _ { \mathcal { V } } \mathcal { J } ^ { \mu \nu \alpha } , \mathcal { A } ^ { 4 } x = 0 . } } \end{array}
$$

![](images/7678e47ce2702a6f50f3a8261b5e9e6ef41aceaa645bc9578c7f1969aec0297c.jpg)

(Note: $\partial ^ { \aa } \mathcal { V } \equiv$ (boundary of $\mathcal { V }$ ）includes $\mathcal { S } _ { A } , \mathcal { S } _ { B } ,$ and timelike surfaces at spatial infinity; contribution of latter dropped-localized source.)

# C. Change of Point About Which Angular Momentum is Calculated

Let $b ^ { \alpha }$ be vector from $\scriptstyle { \mathcal { Q } } _ { 0 }$ to $\mathcal { Q } _ { 1 } \colon b ^ { \alpha } = { a _ { 1 } } ^ { \alpha } - { a _ { 0 } } ^ { \alpha }$ Then

$$
\begin{array} { r c l } { { } } & { { } } & { { J ^ { \mu \nu } ( \mathrm { a b o u t ~ } { \mathcal Q } _ { 1 } ) - J ^ { \mu \nu } ( \mathrm { a b o u t ~ } { \mathcal Q } _ { 0 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { = - b ^ { \mu } \displaystyle \int _ { s } T ^ { \nu \alpha } d ^ { 3 } { \Sigma } _ { \alpha } + b ^ { \nu } \displaystyle \int _ { s } T ^ { \mu \alpha } d ^ { 3 } { \Sigma } _ { \alpha } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { = - b ^ { \mu } P ^ { \nu } + b ^ { \nu } P ^ { \mu } , } } \end{array}
$$

where $P ^ { \mu }$ is total 4-momentum.

![](images/4b7b281ec177b9d8dc36b09fd39050b67f31e2d18bfcb07b0b636efe7ee0345b.jpg)

# D. Intrinsic Angular Momentum

(a) Work, for a moment, in the system's rest frame, where

$$
P ^ { 0 } = M , \qquad P ^ { j } = 0 , \qquad x _ { c M } { } ^ { j } = \frac { 1 } { M } \int x ^ { j } T ^ { 0 0 } d ^ { 3 } x = \mathrm { l o c a t i o n ~ o f ~ c e n t e r ~ o f ~ m a s s } .
$$

Intrinsic angular momentum is defined as angular momentum about any event $( { a } ^ { 0 } , { x } _ { C M } { ^ j } )$ on center of mass's world line. Its components are denoted $S ^ { \mu \nu }$ and work out to be

$$
S ^ { 0 j } = 0 , S ^ { j k } = \epsilon ^ { j k \ell } S ^ { \ell } ,
$$

where

$$
{ \begin{array} { r l } & { S \equiv \int \left( x - x _ { c u } \right) \times \left( { \mathrm { m o m e n t u m ~ d e n s i t y } } \right) d ^ { 3 } x } \\ & { \quad \equiv { \mathrm { ` i n t r i n s i c ~ a n g u l a r ~ m o m e n t u m ~ v e c t o r . ~ ' } } } \end{array} }
$$

(b) Define “intrinsic angular momentum 4-vector" $S ^ { \mu }$ to be that 4-vector whose components in the rest frame are $( 0 , S )$ ； then the above equations say

$$
S ^ { \mu \nu } = U _ { \alpha } S _ { \beta } { \epsilon } ^ { \alpha \beta \mu \nu } ,
$$

$U _ { \beta } \equiv P _ { \beta } / M = 4 .$ velocity of center of mass,

$$
U _ { \beta } S ^ { \beta } = 0 .
$$

# E. Decomposition of Angular Momentum into Intrinsic and Orbital Parts

(a) Pick an arbitrary event $\boldsymbol { \mathcal { a } }$ ，whose perpendicular displacement from centerof-mass world line is $- Y ^ { \alpha }$ s0

$$
U _ { \beta } Y ^ { \beta } = 0 .
$$

![](images/1074163679c938b8f1d3dc82834ca281aacc7e5f7571758ac778d71ed9ab5ef5.jpg)

(b) Then, by Part C, the angular momentum about $\boldsymbol { \mathcal { Q } }$ is

$$
\begin{array} { r } { J ^ { \mu \nu } = \underbrace { U _ { \alpha } S _ { \beta } \epsilon ^ { \alpha \beta \mu \nu } } _ { S ^ { \mu \nu } ( \mathrm { i n t r i n s i c } ) } + \underbrace { Y ^ { \mu } P ^ { \nu } - Y ^ { \nu } P ^ { \mu } } _ { L ^ { \mu \nu } ( \mathrm { o r b i t a l } ) } . } \end{array}
$$

(c) Knowing the angular momentum about $\boldsymbol { \mathcal { Q } }$ ,and the 4-momentum (and hence 4-velocity),one can calculate the vector from $\boldsymbol { \mathcal { Q } }$ to the center-of-mass world line,

$$
Y ^ { \mu } = - J ^ { \mu \nu } P _ { \nu } / M ^ { 2 } ,
$$

and the intrinsic angular momentum

$$
S _ { \rho } = \frac { 1 } { 2 } U ^ { \sigma } J ^ { \mu \nu } \epsilon _ { \sigma \mu \nu \rho } .
$$

Use Gausss theorem to show that ε is the number of particles created (minus the number destroyed) in a unit four-dimensional volume of spacetime.

# Exercise 5.4. INERTIAL MASS PER UNIT VOLUME

Consider a stressed medium in motion with ordinary velocity $| \nu | \leqslant 1$ with respect to a specific Lorentz frame.

(a) Show by Lorentz transformations that the spatial components of the momentum density are

$$
T ^ { 0 j } = \sum _ { k } m ^ { j k } v ^ { k } ,
$$

where

$$
m ^ { j k } = T ^ { \widetilde { 0 } \widetilde { 0 } } \delta ^ { j k } + T ^ { \widetilde { j k } }
$$

and $T ^ { \tilde { \mu } \overline { { \nu } } }$ are the components of the stress-energy tensor in the rest frame of the medium. Throughout the solar system $T ^ { { \tilde { 0 } } { \tilde { 0 } } } \gg | T ^ { { \tilde { j } } { \tilde { k } } } |$ (see,e.g.,discussion of hurricane in $\ S 5 . 1 0 \AA$ ,so one is accustomed to write $T ^ { 0 j } = T ^ { \overline { { 0 } } \tilde { 0 } } v ^ { j }$ ,i.e.,"(momentum density) $=$ (rest-mass density) $\times$ (velocity)". But inside a neutron star $T ^ { \widetilde { 0 } \widetilde { 0 } }$ may be of the same order of magnitude as $T ^ { \tilde { j } \tilde { k } }$ ，so one must replace “(momentum density) $=$ (rest-mass density) $\times$ (velocity)”by equations (5.51) and (5.52),at low velocities.

(b) Derive equations (5.51) and (5.52) from Newtonian considerations plus the equivalence of mass and energy. (Hint: the total mass-energy carried past the observer by a volume $V$ of the medium includes both the rest mass $T ^ { \overleftarrow { 0 0 } } \bar { V }$ and the work done by forces acting across the volume's faces as they“push” the volume through a distance.)

(c) As a result of relation (5.5l), the force per unit volume required to produce an acceleration $d v ^ { k } / d t$ in a stressed medium,which is at rest with respect to the man who applies the force、is

$$
F ^ { j } = d T ^ { 0 j } / d t = \sum _ { k } m ^ { j k } d v ^ { k } / d t .
$$

This equation suggests that one call $m ^ { j k }$ the “inertial $\mathbf { m a s s }$ per unit volume”of a stressed medium at rest. In general $m ^ { \mathrm { { j } } k }$ is a symmetric 3-tensor. What does it become for the special case of a perfect fluid?

(d) Consider an isolated, stressed body at rest and in equilibrium $( T ^ { \alpha \beta } { } _ { , 0 } = 0 )$ in the :- laboratory frame. Show that its total inertial mass, defined by

$$
M ^ { i j } = \int \mod ( M ^ { i j } d x d y d z ,
$$

is isotropic and equals the rest mass of the body

$$
M ^ { \mathrm { i } j } = \delta ^ { \mathrm { i } j } \int T ^ { 0 0 } d x d y d z .
$$

Exercise 5.5. DETERMINANTS AND JACOBIANS

(a) Write out explicitly the sum defning $d ^ { 2 } S _ { 0 1 }$ in

$$
d ^ { 2 } S _ { \mu \nu } \equiv \epsilon _ { \mu \nu \alpha \beta } \frac { \partial x ^ { \alpha } } { \partial a } \frac { \partial x ^ { \beta } } { \partial b } d a d b .
$$

Thereby establish the formula

$$
d ^ { 2 } S _ { \mu \nu } = \epsilon _ { \mu \nu \mid \alpha \beta \mid } \frac { \partial ( x ^ { \alpha } , x ^ { \beta } ) } { \partial ( a , b ) } d a d b = \frac { 1 } { 2 ! } \epsilon _ { \mu \nu \alpha \beta } \frac { \partial ( x ^ { \alpha } , x ^ { \beta } ) } { \partial ( a , b ) } d a d b .
$$

(Expressions such as these should occur only under integral signs. In this exercise one may either supply an $\textstyle \int \ldots$ wherever necessary.or else interpret the differentials in terms of the exterior calculus,da $d b \longrightarrow d a \wedge d b$ ；see Box 5.4.) The notation used here for Jacobian determinants is

$$
{ \frac { { \boldsymbol { \partial } } ( f , g ) } { { \boldsymbol { \partial } } ( a , b ) } } = \left| { \frac { { \frac { \partial f } { \partial a } } { \boldsymbol { \frac { \partial f } { \partial b } } } } { \frac { \partial g } { \partial a } } } \right| .
$$

(b) By a similar inspection of a specific case, show that

$$
d ^ { 3 } \mathscr { S } _ { \mu } \equiv \epsilon _ { \mu \alpha \beta \gamma } \frac { \partial x ^ { \alpha } } { \partial a } \frac { \partial x ^ { \beta } } { \partial b } \frac { \partial x ^ { \gamma } } { \partial c } d a d b d c = \frac { 1 } { 3 ! } \epsilon _ { \mu \alpha \beta \gamma } \frac { \partial ( x ^ { \alpha } , x ^ { \beta } , x ^ { \gamma } ) } { \partial ( a , b , c ) } d a d b d c .
$$

(c) Cite a precise definition of the value of a determinant as a sum of terms (with suitably alternating signs)，with each term a product containing one factor from each row and simultaneously one factor from each column. Show that this definition can be stated (in the $4 \times 4$ case,with the $p \times p$ case an obvious extension) as

$$
\operatorname* { d e t } { \cal A } \equiv \operatorname* { d e t } { | | A ^ { \lambda } { } _ { \rho } | | } = \epsilon _ { \alpha \beta \gamma \delta } A ^ { \alpha } { } _ { 0 } A ^ { \beta } { } _ { 1 } A ^ { \gamma } { } _ { 2 } A ^ { \delta } { } _ { 3 } .
$$

(d) Show that

$$
\operatorname* { d e t } A = { \frac { 1 } { 4 ! } } \delta _ { \alpha \beta \gamma \delta } ^ { \mu \nu \rho \sigma } A ^ { \alpha } { } _ { \mu } A ^ { \beta } { } _ { \nu } A ^ { \gamma } { } _ { \rho } A ^ { \delta } { } _ { \sigma }
$$

(for a definition of $\delta _ { \alpha \beta \gamma \delta } ^ { \mu \nu \rho \sigma }$ , see exercises 3.13 and 4.12).

(e) Use properties of the $\pmb { \delta }$ -symbol to show that the matrix $\pmb { A } ^ {  1 }$ inverse to $\pmb { A }$ has entries $( A ^ { - 1 } ) ^ { \mu } { } _ { \alpha }$ given by

$$
( A ^ { - 1 } ) ^ { \mu } { } _ { \alpha } ( \operatorname * { d e t } A ) = \frac { 1 } { 3 ! } \delta _ { \alpha \beta \gamma \delta } ^ { \mu \nu \rho \sigma } A ^ { \beta } { } _ { \nu } A ^ { \gamma } { } _ { \rho } A ^ { \delta } { } _ { \sigma } .
$$

(f)By an “index-mechanics”computation, from the formula for det $\pmb { A }$ in part (d) derive the following expression for the derivative of the logarithm of the determinant

$$
d \ln \vert \operatorname* { d e t } A \vert = \operatorname { t r a c e } ( A ^ { - 1 } { \pmb { d } } A ) .
$$

Here dA is the matrix ${ | | d A ^ { \alpha } } _ { \mu } { | | }$ whose entries are l-forms.

# Exercise 5.6. CENTROIDS AND SIZES

Consider an isolated system with stress-energy tensor $T ^ { \mu \nu }$ ,total 4-momentum $P ^ { \alpha }$ ,magnitude of 4-momentum $M = ( - \pmb { P } \cdot \pmb { P } ) ^ { 1 / 2 }$ ,intrinsic angular momentum tensor $S ^ { \alpha \beta }$ ,and intrinsic angular momentum vector $S ^ { \alpha }$ .(See Box 5.6.) An observer with 4-velocity $u ^ { \alpha }$ defines the centroid of the system,at his Lorentz time $x ^ { 0 } = t$ and in his own Lorentz frame,by

$$
X _ { u } ^ { j } ( t ) = ( 1 / P ^ { 0 } ) \int _ { x ^ { 0 } = t } x ^ { j } T ^ { 0 0 } d ^ { 3 } x \qquad \mathrm { i n ~ L o r e n t z ~ f r a m e ~ w h e r e ~ } u = \partial \mathcal { P } / \partial x ^ { 0 } .
$$

This centroid depends on (i) the particular system being studied,(ii) the 4-velocity ${ \pmb u }$ of the observer,and (iii） the time $t$ at which thc system is observed.

(a) Show that the centroid moves with a uniform velocity

$$
d X _ { \pmb { u } } ^ { j } / d t = P ^ { j } / P ^ { 0 } ,
$$

corresponding to the 4-velocity

$$
\pmb { U } = \pmb { P } / M .
$$

Note that this $^ { 6 6 } 4$ velocity ofcentroid”is independent of the 4-velocity $\pmb { u }$ used in defining the centroid.

(b)The centroid associated with the rest frame of the system (i.e.,the centroid defined with $\pmb { u } = \pmb { U }$ ） is called the center of mass; see Box 5.6.Let $\pmb { \xi } _ { \pmb { \mu } }$ be a vector reaching from any event on the center-of-mass world line to any event on the world line of the centroid associated with 4-velocity $\pmb { u }$ ；thus the components of $\pmb { \xi } _ { \pmb { \mu } }$ in any coordinate system are

$$
\xi _ { u } ^ { \alpha } = X _ { u } ^ { \alpha } - X _ { u } ^ { \alpha } .
$$

Show that $\xi _ { \pmb { \mu } }$ satisfies the equation

$$
\begin{array} { r } { \{ ( \xi _ { \pmb { u } } ^ { \alpha } P ^ { \beta } - P ^ { \alpha } \xi _ { \pmb { u } } ^ { \beta } ) - S ^ { \alpha \beta } ] u _ { \beta } = 0 . } \end{array}
$$

$\{ H i n t .$ ：perform the calculation in a Lorentz frame where $\pmb { \upsilon } = \hat { c } \mathcal { S } / \hat { \partial } x ^ { 0 } . ]$

(c) Show that, as seen in the rest-frame of the system at any given moment of time. the above equation reduces to the three-dimensional Euclidean equation

$$
\pmb { \xi } _ { \pmb { u } } = - ( \pmb { \nu } \times \pmb { S } ) / M ,
$$

where $\pmb { \nu } = \pmb { u } / u ^ { 0 }$ is the ordinary velocity of the frame associated with the centroid.

(d) Assume that the energy density measured by any observer anywhere in spacetime is

non-negative $( { \pmb u } \cdot { \pmb T } \cdot { \pmb u } \geq 0$ for all timelike ${ \pmb u }$ ).In the rest frame of the system,construct the smallest possible cylinder that is parallel to $s$ and that contains the entire system $( T _ { \alpha \beta } = 0$ everywhere outside the cylinder). Show that the radius $r _ { 0 }$ of this cylinder is limited by

$$
r _ { 0 } \ge | { \bf S } | / M .
$$

Thus,a system with given intrinsic angular momentum $s$ and given mass $M$ has a minimum possible size $r _ { 0 \mathrm { m i n } } = | \pmb { S } | / M$ as measured in its rest frame.
