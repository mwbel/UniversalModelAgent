# Chapter 11

# Perturbations

# 11.1 Introduction

The equation of motion of a perturbed orbit is of the form

$$
\ddot { \tilde { \mathbf { r } } } + \mu \frac { \tilde { \mathbf { z } } } { \tilde { \mathbf { z } } ^ { 3 } } = \mathbf { \mathbb { F } } .
$$

I Chapter Nine the perturbing force $\mathbf { \widehat { F } }$ was derived from the action of other bodies,but it could equally well arise from other causes such as atmospheric drag or the fact that the attracting body was not perfectly spherical. For example,when considering the motion of a close artificial satellite of the Earth we are mainly concerned with the consequences of atmospheric friction and the oblateness of the Earth.

If theright-hand side (11.1.1) is zero,the motion is Keplerian;the deviations from Keplerian motion are perturbations. As an example of a perturbed orbit, consider the hypothetical case of a body of mass m moving in the Newtonian field ofa mass $\tilde { \lambda } \tilde { \mathcal { A } }$ and also subject to a small tangential resistance

$$
R = \frac { c \mathcal { Y } } { { \boldsymbol { \tau } } ^ { 2 } }
$$

per unit mass,where V is the orbital speed and r is the distance from the center of M. If ds is the element of arc length, R can be resolved radially and transversely as

$$
- R \frac { { \dot { a } } \tau } { { \dot { d } } s } \quad { \mathrm { a } } { \mathrm { , } } { \mathrm { \hat { d } } } \quad - R r \frac { { \dot { d } } { \dot { \theta } } } { { \dot { d } } s } ,
$$

(see Figure 11.1）, or, since $v = d s / d t$ ：

$$
- c \frac { 1 } { r ^ { 2 } } \frac { d r } { d \dot { z } } \quad \mathrm { a n d } \quad - c \frac { 1 } { r } \frac { d \dot { \theta } } { d \dot { t } } .
$$

The motion takes place in a plane,and the equations of motion in that plane are

$$
\ddot { r } - r \dot { \theta } ^ { 2 } = - \frac { \mu } { \mathfrak { s } ^ { 2 } } - c \frac { \dot { r } } { \mathfrak { s } ^ { 2 } }
$$

and

$$
\frac { d } { d t } \{ r ^ { 2 } \dot { \theta } \} = - c \dot { \theta } ,
$$

where

$$
\mu = ( \vec { \mathscr { M } } + \gamma \mathscr { n } ) _ { \mathscr { n } } ^ { \gamma 2 } .
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/ea33ab4ba0d5e0395e1b5a69f13d68f7402219437981bce6ead06f960e19d7fb.jpg)  
Figure 11.1

Let H = r²0. Because of the perturbing force, this is not constant, but, integrating (11.1.3),

$$
\tilde { { \cal H } } = \ h - c \theta ,
$$

where $\hslash$ is a constant of integration.

Let $r = 1 / 2 3 ;$ then, as in Section 4.3,

$$
\ddot { r } = - { \cal H } { u ^ { 2 } } \frac { \dot { d } } { d \theta } \left( \bar { \cal H } \frac { \dot { d } u } { d \theta } \right)
$$

and (11.1.2) becomes

$$
{ \frac { d ^ { 2 } u } { d \vartheta ^ { 2 } } } + u = { \frac { \ddot { \mu } } { H ^ { 2 } } } .
$$

Using (11.1.4) we can expand $H ^ { - 2 }$ in powers of $c .$ and since the resisting force is small, $c$ is a small quantity whose square may be neglected. Then

$$
{ \frac { \vec { d } ^ { 2 } u } { \vec { d } \theta ^ { 2 } } } + u = { \frac { \mu } { \hbar ^ { 2 } } } \left( \vec { \bf \tt \tt \tt \tt \tt \equiv } \frac { c } { \hbar } \vartheta \right) .
$$

The solution of this equation is easily verified to be

$$
u = \frac { 1 } { p } \left( 1 + e \cos ( \theta - \omega ) + 2 \frac { c } { h } \theta \right) ,
$$

where e and $\omega$ are constants of integration, and $g = \hbar ^ { 2 } / \mu$ is also constant. We assume that $\varepsilon$ is less than one.

To interpret this solution,suppose that at some point P,where the position and velocity are given by ui,01,(du/dt)i,and (d0/dt)i,the perturbing force suddenly ceases; then m will move in an ellipse defined by these initial values. This is called the osculating ellipse at $\mathcal { P } _ { 1 }$ ；it is the Keplerian orbit having simultaneously the same position and velocity as the true orbit.

Let the osculating orbit at $\mathcal { P } _ { \mathtt { I } }$ have equation

$$
u = \frac { 1 } { p _ { \perp } } [ 1 + e _ { 1 } \cos ( \theta - \omega _ { \perp } ) ] .
$$

(Note: wemust notss it be $u = { \frac { 1 } { p } } [ 1 + e \cos ( \theta - \omega ) ] . )$

The angular momentum h1 must be equal to the value of (r²θ)i, or, from (11.1.4),

$$
\hbar _ { \textrm { r } } = \hbar - c \pmb { \theta } _ { 1 } .
$$

Hence

$$
\begin{array} { c } { { p _ { 1 } = \displaystyle \frac { \hbar _ { 1 } ^ { 2 } } { \mu } = \displaystyle \frac { ( \hbar - \mathcal { O } _ { 1 } ) ^ { 2 } } { \mu } } } \\ { { = p \left( 1 - \displaystyle \frac { c } { \hbar } \theta _ { 1 } \right) ^ { 2 } } } \\ { { = p \left( 1 - 2 \displaystyle \frac { c } { \hbar } \theta _ { 1 } \right) } } \end{array}
$$

where $c ^ { 2 }$ has been neglected.

At Pi,u and du/d0 must be the same both for (11.1.6) and (11.1.7), so that

$$
\frac { 1 } { p _ { 1 } } [ 1 + e _ { 1 } \cos ( \theta _ { 1 } - \omega _ { 1 } ) ] = \frac { 1 } { p } \left[ 1 + e \cos ( \theta _ { 1 } - \omega ) + 2 \frac { c } { h } \theta _ { 1 } \right]
$$

and

$$
\frac { 1 } { p _ { 1 } } [ - e _ { 1 } \sin ( \theta _ { 1 } - \omega _ { 1 } ) ] = \frac { 1 } { p } \left[ - e \sin ( \theta _ { 1 } - \omega ) + 2 \frac { c } { h } \right] .
$$

Using (11.1.8） and neglecting $c ^ { 2 }$ ,we find

$$
e _ { 1 } \cos ( \theta _ { 1 } - \omega _ { 1 } ) = e \cos ( \theta _ { 1 } - \omega ) - 2 \frac { c } { h } e \theta _ { 1 } \cos ( \theta _ { 1 } - \omega )
$$

and

$$
e _ { 1 } \sin ( \theta _ { 1 } - \omega _ { 1 } ) = e \sin ( \theta _ { 1 } - \omega ) - 2 \frac { c } { \hbar } - 2 \frac { c } { \hbar } e \theta _ { 1 } \sin ( \theta _ { 1 } - \omega ) .
$$

Multiply the first of these by $\cos ( \theta _ { \tt I } - \omega )$ and the second by $\sin ( \theta _ { 1 } - \omega )$ ,and add.Then multiply the first by sin(01-w) and the second by cos(01-ω)and subtract.We find

$$
\begin{array} { r } { e _ { 1 } \cos ( \omega _ { 1 } - \omega ) = e - 2 \frac { e } { \hbar } e \theta _ { 1 } - 2 \frac { e } { \hbar } \sin ( \theta _ { 1 } - \omega ) } \end{array}
$$

and

$$
e _ { 1 } \sin ( \omega _ { 1 } - \omega ) = 2 \frac { c } { h } e \cos ( \theta _ { 1 } - \omega ) .
$$

Now let

$$
e _ { \updownarrow } - e = \delta e _ { \updownarrow } \quad \mathrm { a a d } \quad \omega _ { \updownarrow } - \omega = \delta \omega _ { \updownarrow } .
$$

Then， still neglecting $c ^ { 2 }$ ，

$$
\delta e _ { \mathrm { i } } = - 2 \frac { c } { \hbar } [ e \theta _ { \mathrm { i } } + \sin ( \theta _ { \mathrm { i } } - \omega ) ]
$$

and

$$
\delta \omega _ { 1 } = 2 \frac { c } { \hbar } \cos ( \theta _ { \mathrm { i } } \cdots \omega ) .
$$

$e _ { I }$ and $\omega _ { I }$ are two of the osculating elements at $\mathcal { P } _ { 1 }$ From (11.1.9) we see that the variation in $e _ { \tt I }$ ，as $P _ { 1 }$ varies in the true orbit, consists of two parts; the first represents a steady decrease to a circular orbit, while the second is periodic and contributes nothing in the long run. A steady monotonic change is called a secular perturbation. The other terms are periodic perturbations; since their cumulative effect is zero, they can often be ignored, but the secular perturbations, however small; are bound to become important over a long enough period of time.From (11.1.10) we see that $\omega _ { 1 }$ suffers only periodic perturbations.

Let $\Delta p _ { 1 } , \Delta a _ { 1 }$ ，and $\Delta n _ { 3 }$ now be defined as the perturbations in these elements ouer one revolution; the periodic components cancel out and only the secular parts remain. From (11.1.8),

$$
\frac { \Delta { p } _ { 1 } } { p _ { 1 } } = - 4 \pi \frac { c } { h }
$$

$\{ \log \operatorname { l e c } _ { \tt t \exists \exists E } ^ { 2 } c ^ { 2 } \}$ , and from (11.1.9),

$$
\frac { \Delta e _ { \frac { 1 } { 3 } } } { e _ { \frac { 1 } { 3 } } } = - 4 \pi \frac { c } { \hbar } = \frac { \Delta p _ { 1 } } { p _ { 1 } } .
$$

Also ${ p _ { 1 } = a _ { 1 } \{ 1 - e _ { \frac { 2 } { 1 } } ^ { 2 } \} }$ ,so

$$
\begin{array} { r } { \frac { \Delta a _ { \ddagger } } { a _ { 1 } } = \frac { \Delta p _ { 1 } } { p _ { 1 } } + \frac { 2 e _ { 1 } \Delta e _ { 1 } } { \frac { 1 } { 1 } - e _ { 1 } ^ { 2 } } } \\ { = - 4 \pi \frac { c } { h } \frac { \hat { 1 } + e _ { 1 } ^ { 2 } } { \hat { 1 } - e _ { 1 } ^ { 2 } } . } \end{array}
$$

Also, since $n _ { 1 } = \sqrt { \mu } a _ { 1 } ^ { - 3 / 2 }$

$$
\begin{array} { c } { \displaystyle \frac { \Delta n _ { 1 } } { n _ { \perp } } = - \frac { 3 } { 2 } \frac { \Delta a _ { 1 } } { a _ { 1 } } } \\ { \displaystyle = 6 \pi \frac { c } { \tilde { \hbar } } \frac { 1 + e _ { 1 } ^ { 2 } } { 1 - e _ { 1 } ^ { 2 } } . } \end{array}
$$

So $a _ { 1 }$ decreases secularly，and there is $\clubsuit$ corresponding increase in the mean motion; in addition, these quantities willfuctuate periodically about the secular trend.

This form of resistance would be unlikely to be encountered in practice, but the equations have been considered in some detail in order to demonstrate some of the important considerations involved in perturbations. The solution found isa closed analytical solution, correct to the order of magnitude required (we could,without much difficulty,extend the solutions to the order c²).We can find the perturbations and the character of the orbit at any future time simply by substituting the appropriate value of t into the equations; the same would applyif we had found a solution in the form of a series.Thisis the method of general or absolute perturbations. In our example the solution was simple because the perturbing force was deliberately chosen; but normally this can only be expressed as an infinite series of great complexity, and the method of general perturbations involves considerable labor and analysis.

Another approach to perturbations is to integrate the equations of motion, or adaptations of these, by a numerical procedure in order to find out what will happen over some limited time interval. This is the method of special perturbations. It has some obvious practical advantages in that no complicated analytical work is involved and that,anyway, the general form of the solution for all time may be of no interest (as, for instance, in the case of an interplanetary vehicle). Much of this chapter will be devoted to methods of considering special perturbations,but the reader should remember that if a general solution can be found,it will probably be superior to a numerical integration.

In the example the solution described the changes in the osculating elements in time. This type of method is called the variation of the elements, or the variation of the arbitrary constants (since the elements are the arbitrary constants ofthe two-body problem). Alternatively we can work in terms of the coordinates; the solution may give no immediate insight into what is happening to the orbit in a geometrical sense; however,this information may not be required. We shall start by considering some of the methods of special perturbations in which the coordinates are used,and will go on to consider the variation of the elements.

# 11.2 Cowell's Method

The equations of motion of the two-body problem,

$$
\ddot { x } + \mu \frac { x } { y ^ { 3 } } = 0 , \quad \mathrm { e } ^ { \frac { 1 } { 2 } } \mathrm { c } . ,
$$

could be solved numerically,using the methods of Chapter 10,provided the initial conditions were specified. But since the two-body problem has been solved analytically, this procedure would bea waste of time (and not so accurate asa direct substitution).Also,as we remarked before, the solution would Drovide no immediate information about the nature of the orbit.

But the analytical solution of the equations

$$
\ddot { x } + \mu \frac { x } { r ^ { 3 } } = F _ { x } , \quad e t c . ,
$$

is:not,in general, known. Apart from the errors inherent in any numerical integration, the equations can be solved as accurately as required by the methods of Chapter 10. This is known as Cowell's method. Other approaches to the perturbation problem refer to some reference orbit, as we shall see, but Cowel's method is direct. In fact an alternative name, often used,is the direct integration method, but this can include methods of numerical integration other than that used in Cowell's method:any suitable numerical method can, of course, be used to solve the equations. Full details of Cowel's method together with worked examples are given by Herget (Ref. 24) and in Planetary Coordinates (Ref. 48).

Any method of direct integration has the disadvantage that when the motion becomes rapid (near perihelion) or perhaps when the perturbations become severe, smaller intervals of integration and therefore more calculations are necessary, and the errors may be correspondingly increased. For some parts of the work it may be more convenient to change to another method, such as Encke's (see Section 11.3), which involves more labor at each step of the integration but which allows a longer interval to be used.

All the remarks of Section 9.5 about the neglect of some planets in calculating perturbations in the solar system and “throwing the planets into the Sun" are relevant in the direct integration methods and also in Encke's method. Ful practical details are given in Planetary Coordinates.

# 11.3 Encke's Method

Consider the disturbed motion given by

$$
\ddot { \mathfrak { r } } + \mu \frac { \mathfrak { r } } { \mathfrak { r } ^ { 3 } } = \mathfrak { F } .
$$

The equation of undisturbed motion is

$$
\ddot { \rho } + \mu \frac { \rho } { \rho ^ { 3 } } = 0 .
$$

Let

$$
\Delta \mathfrak { r } = \mathfrak { r } - \mathfrak { s } ,
$$

then

$$
\frac { d ^ { 2 } } { d \vec { \tau } ^ { 2 } } \Delta \mathbf { r } = \mathbf { F } + \mu \left( \frac { \rho } { \rho ^ { 3 } } - \frac { \mathbf { r } } { r ^ { 3 } } \right) .
$$

Let the solution of (11.3.2) apply to the osculating orbit at some epoch that will be the start of the integration; this will be used as a reference orbit. Since this solution is fully known,the terms in p in (11.3.4) are known,so that the three equations which it comprises can be integrated numerically to give △r (the deviation from the reference orbit) as a function of time.

The term

$$
\frac { \rho } { \rho ^ { 3 } } - \frac { \tt f } { \tt f ^ { 3 } } \tt _ { \cdot \cdot } \tt : \ : .
$$

is small, but its separate components are not, and it is inconvenient to calculate the difference between two nearly equal quantities; to avoid this the equations are transformed as follows.Let

$$
{ \frac { r ^ { 2 } } { \rho ^ { 2 } } } = 1 + 2 q
$$

and

$$
\begin{array} { c } { { \frac { \rho ^ { 3 } } { \pi ^ { 3 } } = ( 1 + 2 q ) ^ { - 3 / 2 } } } \\ { { = 1 - f q . } } \end{array}
$$

Then

$$
\begin{array} { l } { \displaystyle { q = \frac { r ^ { 2 } - \rho ^ { 2 } } { 2 \rho ^ { 2 } } } } \\ { \displaystyle { \quad = \frac { 1 } { \rho ^ { 2 } } \{ ( \xi + \frac { \frac { 1 } { 2 } } \Delta x ) \Delta x + ( \eta + \frac { 1 } { 2 } \Delta y ) \Delta y + ( \zeta + \frac { 1 } { 2 } \Delta z ) \Delta z \} , } } \end{array}
$$

where p= (8,n,S).fis a function of q (a small quantity) and is tabulated in many references. It is given by the series

$$
f = 3 \left( 1 - { \frac { 5 } { 2 } } q + { \frac { 5 \cdot 7 } { 2 \cdot 3 } } q ^ { 2 } - { \frac { 5 \cdot 7 \cdot 9 } { 2 \cdot 3 \cdot 4 } } q ^ { 3 } \div \cdots \right) .
$$

With these substitutions (11.3.4) becomes

$$
{ \frac { d ^ { 2 } } { d t ^ { 2 } } } \Delta \mathbf { r } = \mathbb { F } + { \frac { \mu } { \rho ^ { 3 } } } \{ \rho - \mathbf { r } ( 1 - f q ) \}
$$

0r

$$
\frac { d ^ { 2 } } { d \xi ^ { 2 } } \Delta \mathbf { r } = \mathbf { E } \div h \mathbf { r } f g - h \Delta \mathbf { r } ,
$$

where $\hbar = \mu / \rho ^ { 3 }$

The advantage of Encke's method is that,as perturbations are usually small, △rand its derivatives are smalland consequently a larger integration interval is possible than in Cowel's method. Near perihelion,when the integration intervals have to be diminished in Cowell'smethod,Encke's method isunaffected. Against this is the fact that each step of Encke's method takes longer.Also, as the perturbations accumulate,△r goes on increasing and the equations may become unmanageable. In this case a new and more up-to-date set of osculating elements must be found, and the integration proceeds with these. This method has been successfully used to calculate orbits from the Earth to the Moon; the osculating elements refer to the time of burn-out of a rocket,and the Moon is considered throughout as the perturbing body.

# 11.4The Osculating Orbit

In this section we shall consider the accuracy of the osculating orbit for making short-term predictions,and shall show how the orders of magnitude of the perturbations from the osculating orbit can be found.

Let the position and velocity at time $t _ { 0 }$ in the orbit,which is described under the equations of motion

$$
\ddot { \bar { \Sigma } } + \mu \frac { \bar { \Sigma } } { \gamma ^ { 3 } } = \mathbb { F } ,
$$

be $\yen 0$ and $\dot { \bf z } _ { 0 }$ . The osculating orbit at $\pmb { t } _ { 0 }$ is the solution of

$$
{ \ddot { \pmb { \rho } } } + \mu { \frac { \pmb { \rho } } { \pmb { \rho } ^ { 3 } } } = { \mathfrak { g } }
$$

having the initial conditions $\rho = \mathfrak { r } _ { 0 }$ and ${ \dot { \boldsymbol { \rho } } } = { \dot { \mathbf { r } } } _ { \mathfrak { V } }$ at $\pmb { \mathrm { \ t } } = \pmb { \mathrm { \ t } } _ { 0 }$ The functions $\pmb { \Sigma }$ and $\pmb { \rho }$ can be expanded in Taylor series about this position as

$$
\begin{array} { r } { \mathbf { r } ( t _ { 0 } + \Delta t ) = \mathbf { r } _ { 0 } + \Delta t \dot { \mathbf { r } } _ { 0 } + \frac { 1 } { 2 } ( \Delta t ) ^ { 2 } \ddot { \mathbf { r } } _ { 0 } \div \cdot \cdot \cdot } \end{array}
$$

and

$$
\begin{array} { r } { \pmb { \rho } ( t _ { 0 } + \Delta t ) = \pmb { \rho } _ { 0 } + \Delta t \dot { \pmb { \rho } } _ { 0 } + \frac { 1 } { 2 } ( \Delta t ) ^ { 2 } \ddot { \pmb { \rho } } _ { 0 } + \cdots } \end{array}
$$

where $j _ { 0 }$ means that $\ddot { \mathbf { r } }$ is evaluated at $t = t _ { 0 }$ . Subtracting these equations and applying the initial conditions,we find

$$
\begin{array} { r } { \Delta \mathbf { r } = \mathbf { r } - \boldsymbol { \rho } = \frac { 1 } { 2 } ( \Delta t ) ^ { 2 } ( \ddot { \mathbf { r } } _ { 0 } - \ddot { \boldsymbol { \rho } } _ { 0 } ) + \boldsymbol { 0 } \{ ( \Delta t ) ^ { 3 } \} . } \end{array}
$$

Suppose that $\Delta t$ is small enough for its cube to be neglected; then,substituting from the equations of motion, we find

$$
\begin{array} { r } { \Delta \mathbf { r } = \frac { 1 } { 2 } ( \Delta t ) ^ { 2 } \mathbf { \overline { { F } } } _ { 0 } . } \end{array}
$$

We shalluse this formula to estimate the extent of perturbations by Jupiter on Mars. Here

$$
\mathbf { F } = m ^ { \prime } k ^ { 2 } \left\{ { \frac { \mathbf { r } ^ { \prime } - \mathbf { r } } { \left| \mathbf { r } ^ { \prime } - \mathbf { r } \right| ^ { 3 } } } - { \frac { \mathbf { r } ^ { \prime } } { r ^ { \prime 3 } } } \right\} ,
$$

where $m ^ { \prime }$ is the mass of Jupiter and $\mathbf { r } ^ { \prime }$ its position vector with respect to the Sun. Let $\alpha$ be the semimajor axis of Mars' orbit; then

$$
\mu = 4 \pi ^ { 2 } \frac { a ^ { 3 } } { P ^ { 2 } } ,
$$

where $P$ is the period of Mars and $\mu = \mathbb { k } ^ { 2 } ( \mathbb { M } \div \mathfrak { m } )$ ： $\pmb { \ M }$ and $\mathcal { W }$ are masses of the Sun and Mars, respectively. Putting

$$
\begin{array} { r l } & { ( \Delta t ) ^ { 2 } = \left( \displaystyle \frac { \Delta t } { P } \right) ^ { 2 } P ^ { 2 } } \\ & { \qquad = \left( \displaystyle \frac { \Delta t } { P } \right) ^ { 2 } 4 \pi ^ { 2 } \displaystyle \frac { a ^ { 3 } } { ( M + m ) k ^ { 2 } } , } \\ & { \qquad \quad \cdot \left( \frac { \Delta t } { P } \right) ^ { 2 } P ^ { 2 } . } \end{array}
$$

(11.4.3) can be written

$$
\Delta \mathbf { r } = 2 \pi ^ { 2 } a ^ { 3 } { \frac { m ^ { \prime } } { M + m } } \left( { \frac { \Delta t } { P } } \right) ^ { 2 } \left\{ { \frac { \mathbf { r } ^ { \prime } - \mathbf { r } } { | \mathbf { r } ^ { \prime } - \mathbf { r } | ^ { 3 } } } - { \frac { \mathbf { r } ^ { \prime } } { r ^ { \prime 3 } } } \right\} .
$$

It should be noted that the perturbations depend on the ratio of the masses of the perturbing body and the Sun.

Consider the perturbations near the time of a conjunction of Mars and Jupiter,as observed from the Sun,when we would expect them to be most severe.Neglecting the relative inclination of the two orbits,let the $\pmb { \mathscr { x } }$ -axispoint along the line of conjunction,and let the conjunction take place at time $t _ { 0 }$ Taking the coordinates of Mars and Jupiter at that time as $\{ 1 . 5 2 , 0 , 0 \}$ and $\{ 5 . 2 1 , 0 , 0 \}$ , where the unit of length is the astronomical $\mathtt { I l } \mathtt { N a i t }$ ,and putting

$$
\frac { m ^ { \prime } } { M + m } = \frac { 1 } { 1 0 4 7 } ,
$$

we find

$$
\Delta x = 2 . 4 _ { \AA } ^ { 4 } \times 1 0 ^ { - 3 } \left( \frac { \Delta t } { P } \right) ^ { 2 } \mathrm { \ A } \mathrm { { \bar { U } } } .
$$

Take

$$
\frac { \Delta t } { P } = 0 . 1
$$

so that we are considering the perturbation over O.188 years; then

$$
\begin{array} { c } { \Delta x = 2 . 4 4 \times 1 0 ^ { - 5 } ~ \mathrm { A U } } \\ { = 3 6 5 0 ~ \mathrm { k m } . } \end{array}
$$

Whether or not this is serious may depend on the job in hand. For example,if Mars is the target for a spacecraft,the osculating orbit may not give asufficiently accurate prediction of its position.But it should be noted that the numerical results were derived from approximate distances for Mars and Jupiter;if these were changed by $3 6 5 0 ~ \mathrm { \AA } ~ \mathrm { \AA } ~ \mathrm { { s m } }$ ,the result would not be altered. Hence,when predicting perturbing forces, the osculating elements may be good enough as long as departures from them are not too severe and as long as we do not approach too closely to the perturbing body.

# 11.5The Effects of Small Impulses on the Elements

Suppose a body moving in a Keplerian orbit to be acted on by a perturbing force $\pmb { \Sigma }$ per unit mass for a time $\bar { d t }$ This impulse will alter the elements of the orbit in a way that we shall now investigate.

Resolve $\pmb { \Sigma }$ along $\hat { \pmb { \mathfrak { x } } }$ $\hat { \bf \lambda } _ { \hat { \bf a } }$ $\hat { \bf \Phi } _ { \bf \hat { \theta } } \times \hat { \bf \Phi } _ { \bf \hat { \theta } }$ so that

$$
\begin{array} { l } { \mathbf { F } = R \hat { \mathbf { r } } \div N \hat { \mathbf { h } } \div B \hat { \mathbf { h } } \times \hat { \mathbf { r } } . } \\ { \quad \cdot } \\ { \quad \cdot \hat { \mathbf { \xi } } ^ { \ast } = \frac { \hat { \mathbf { r } } \times \hat { \mathbf { r } } } { 2 } . \cdot \mathbf { \xi } . } \\ { \quad \cdot \hat { \mathbf { \xi } } ^ { \ast } \mathbf { \xi } ^ { \ast } = \hat { \mathbf { \xi } } . } \end{array}
$$

The moment of $\mathbf { \Sigma } _ { \mathbf { z } } ^ { \mathbf { z } }$ dt gives the change of angular momentum, so

$$
\begin{array} { r l } & { \dot { d } \hat { \mathbf { z } } = \mathbf { r } \times \mathbf { \mathbb { F } } \mathbf { \mathit { d } } t } \\ & { \quad \quad = ( r N d t ) \hat { \mathbf { r } } \times \hat { \mathbf { z } } + ( r B d t ) \hat { \mathbf { h } } . } \end{array}
$$

But

$$
\dot { a } \mathbf { \hat { a } } = \hbar d \hat { \mathbf { a } } + \hat { \mathbf { b } } d \hat { h } ,
$$

so, since dh is perpendicular to $\hat { \bf h }$ we have

$$
\beta \hbar = \hbar \beta d t
$$

and

$$
\hat { a } \hat { \mathbf { \mathcal { \mathbf { S } } } } = \frac { r N \hat { d } \hat { \mathbf { \mathcal { \mathbf { t } } } } } { \hat { \mathbf { \mathcal { \mathbf { k } } } } } \hat { \mathbf { \mathcal { \mathbf { x } } } } \times \hat { \mathbf { \mathcal { \mathbf { b } } } } .
$$

Resolve all vectors along axes ${ \mathcal { Z } } , { \mathcal { Y } } , z$ where $\hat { \mathbf { x } }$ points toward the vernal equinox and $\hat { \pmb z }$ toward the north pole of the ecliptic. Then

$$
\hat { \mathbb { \mathrm { i } } } = \langle \sin \Omega \sin i , - \cos \Omega , \sin i , \cos i \rangle .
$$

From (11.5.3) and (11.5.4) we see that $\mathcal { N }$ is the only component of $\mathbb { E }$ that affects $\Omega$ and $i$ Multiply (11.5.3) scalarly by $\hat { \pmb { \Xi } } \ast _ { \hat { \pmb { \varsigma } } } ^ { * }$ we find

$$
\hat { \bf z } \cdot d \hat { \bf { h } } = \frac { r \tilde { N } d \hat { t } } { \tilde { \mu } } \hat { \bf z } \cdot ( \hat { \bf { x } } \times \hat { \bf { h } } )
$$

0r

$$
- \sin i \overrightarrow { d i } = - \frac { \pi N d { \boldsymbol { \ell } } } { \hbar } \hat { \mathbf { r } } \cdot ( \hat { \mathbf { z } } \times \hat { \mathbf { z } } ) .
$$

Now $\hat { \mathbf { z } } \times \hat { \mathbf { \textmu } }$ has magnitude sin $\begin{array} { r } { \hat { z } } \end{array}$ and the direction of the ascending node; so, since $\hat { \pmb { \tau } }$ makes an angle $\mathfrak { u }$ with the ascending node,

$$
d i = { \frac { N d t } { \hbar } } \tau \cos { \mathfrak { u } } .
$$

Next multiply (11.5.3) by $\hat { \bf \beta } _ { \perp \times }$ and then by $\hat { \pmb { z } } = ;$ we find

$$
\hat { { \bf z } } \cdot ( \hat { \hat { \bf { u } } } \times d \hat { \hat { \bf { u } } } ) = \frac { r \hat { N } \hat { d } \hat { \hat { \bf z } } } { \hat { \hat { \bf z } } } \hat { { \bf z } } \cdot \hat { \hat { \bf { r } } } .
$$

Now $\hat { z } \cdot \hat { \bar { x } }$ is the sine of the celestial latitude of the body;in the notation of Figure 11.2 this is sin $P P ^ { \prime }$ which is equal to sin $\varkappa \mathbb { s i a } \ i$ The left-hand side can be evaluated by differentiating (11.5.4). We find, eventually,

$$
\sin ^ { 2 } i d \Omega = { \frac { i \pi d \pm } { \hbar } } \sin u \sin i
$$

$$
d \Omega = \frac { N \dot { d } \dot { \mathfrak { x } } } { \dot { \mathfrak { x } } } \mathfrak { s i n } \mathfrak { u c s c } \dot { \mathfrak { z } } .
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/e76abb44d3f98225319c1faba5aa209e0a306dc2a3d30194a2a56d090ef9953c.jpg)  
Figure 11.2

N dt does not affect h; nor, since it is perpendicular to the velocity， does it affect the linear momentum. Therefore it has no effect on the other elements except indirectly on w, since this angle is measured from the ascending node. The change in w caused solely by a change d& in the node is

$$
d { \boldsymbol { \omega } } = - \cos i d \Omega .
$$

If $\tilde { \omega }$ is used, then

$$
\begin{array} { r l } & { d \tilde { \omega } = \left( 1 - \cos i \right) d \Omega } \\ & { \quad = 2 \sin ^ { 2 } \frac { 1 } { 2 } i d \Omega . } \end{array}
$$

We can now ignore N and evaluate the effects of R and B. Consider the equations for Keplerian motion

$$
\begin{array} { r } { e \cos v = \frac { \hbar ^ { 2 } } { \mu \xi ^ { * } } - 1 , } \end{array}
$$

and

$$
\begin{array} { r } { e \sin v = \frac { \hbar } { \mu } \dot { \vec { \tau } } . } \end{array}
$$

Since $\mathcal { r }$ isnot instantaneously altered by the impulse,changes in the motion must obey

and

$$
\left. \begin{array} { l } { { d ( e \cos v ) = \displaystyle \frac { 2 h d h } { \mu r } , } } \\ { { } } \\ { { } } \\ { { d ( e \sin v ) = \displaystyle { \dot { r } \frac { d h } { \mu } + \frac { h } { \mu } d \dot { r } } . } } \end{array} \right] \nonumber
$$

From the equation of linear momentum we have

$$
{ a } ^ { 7 } { \dot { \tau } } = \mathbb { R } { d } { \dot { \tau } } .
$$

Now

$$
v = v  - \omega
$$

and as neither $R$ nor $\mathcal { B }$ alters the node, $\mathfrak { U }$ is not instantaneously changed, so that

$$
\check { \psi } \mathrel { \mathop : } \mathrel { = } - \check { d } \omega .
$$

Applying this condition and (11.5.2) to the equations (11.5.9), we find

$$
d e \cos v + d \omega e \sin v = { \frac { 2 \hbar } { \mu \tau } } r B d t
$$

and

$$
d e \sin v - d \omega e \cos v = { \frac { \dot { \gamma } } { \mu } } r B d t + { \frac { \dot { h } } { \mu } } R d t .
$$

Solving these for de and $d \omega$ ,we find

$$
d e = { \frac { h } { \mu } } R d t \sin { v } + \left( { \frac { 2 h } { \mu } } \cos { v } + { \frac { r { \dot { r } } } { \mu } } \sin { v } \right) B d t
$$

and

$$
e d \omega = - { \frac { \hbar } { \mu } } R d t \cos { v } + \left( { \frac { 2 \hbar } { \mu } } \sin { v } - { \frac { \tau { \dot { \tau } } } { \mu } } \cos { v } \right) B d t .
$$

Using the familiar formulas for Keplerian motion, these can be simplified to give

$$
\begin{array} { r } { d e = \displaystyle \frac { n a ^ { 2 } } { \mu } \sqrt { 1 - e ^ { 2 } } \{ R d t \sin v + B d t ( \cos v + \cos E ) \} , } \end{array}
$$

and

$$
d \omega = \frac { n a ^ { 2 } } { \mu e } \sqrt { 1 - e ^ { 2 } } \left\{ - R d t \cos { v } + B d t \left( 1 + \frac { r } { p } \right) \sin { v } \right\} .
$$

Next we find $d a$ from the relation

$$
\alpha \{ 1 - e ^ { 2 } \} = \frac { \hbar ^ { 2 } } { \mu } ,
$$

so that

$$
\bar { d a } ( \mathrm { i } - e ^ { 2 } ) = 2 a e \bar { d e } + \frac { 2 \hbar \bar { d h } } { \mu } .
$$

Substituting for de and dh and simplifying, we find

$$
d a = { \frac { 2 n a ^ { 2 } } { \mu } } \left\{ R d t { \frac { a e } { \sqrt { 1 - e ^ { 2 } } } } \sin v + B d t { \frac { a ^ { 2 } } { r } } { \sqrt { 1 - e ^ { 2 } } } \right\} .
$$

These formulas have been found for isolated impulses. From their form they can be generalized for any forces acting continuously on the body. Then the elements become variables in the differential equations:

$$
\begin{array} { l } { \displaystyle \frac { d \mathfrak { Q } } { d t } = \frac { n a r } { \mu \sqrt { 1 - e ^ { 2 } } } N \sin u \csc i , } \\ { \displaystyle \frac { d i } { d t } = \frac { n a r } { \mu \sqrt { 1 - e ^ { 2 } } } N \cos u , } \\ { \displaystyle \frac { d e } { d t } = \frac { n a ^ { 2 } } { \mu } \sqrt { 1 - e ^ { 2 } } \{ R \sin v + B ( \cos v + \cos E ) \} , } \\ { \displaystyle \frac { d \tilde { \omega } } { d t } = \frac { n a ^ { 2 } } { \mu e } \sqrt { 1 - e ^ { 2 } } \left\{ - R \cos v + B \left( 1 + \frac { r } { p } \right) \sin v \right\} + 2 \sin ^ { 2 } \frac { 1 } { 2 } i \frac { d \mathfrak { Q } } { d t } , } \end{array}
$$

or

$$
\begin{array} { l } { { \displaystyle { \frac { d \omega } { d t } = \frac { n a ^ { 2 } } { \mu e } \sqrt { 1 - e ^ { 2 } } \left\{ - R \cos \upsilon + B \left( 1 + \frac { r } { p } \right) \sin \upsilon \right\} - \cos i \frac { d \Omega } { d t } } , } } \\ { { \displaystyle { \frac { d a } { d t } = \frac { 2 n a ^ { 2 } } { \mu } \left\{ R \frac { a e } { \sqrt { 1 - e ^ { 2 } } } \sin \upsilon + B \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { r } \right\} } , } } \end{array}
$$

or

$$
\frac { \dot { a } \pi } { \dot { d t } } = - \frac { 3 } { 2 } \frac { n } { a } \frac { \dot { d } a } { d \dot { t } } .
$$

These equations omit the element Tor associated elements;these will be discussed in the following section. The equations constitute one form of Lagrange's planetary equations; this particular form is due to Gauss. (For a derivation that is more satisfactory mathematically, in that it avoids “infinitesimals,” see Ref. 27.）Their application will be discussed later and, in particular,will be illustrated in the following chapter.

# 11.6 The Equation for $\boldsymbol \varepsilon$

Continuing along the lines of the preceding section, we can find the equation for the variation of $\mathcal { T }$ by differentiating

$$
\mathfrak { r } = \mathfrak { a } \{ \sharp - e \cos \mathscr { E } \}
$$

to find $a ^ { 3 } = 2 / \vec { a } \vec { t }$ and then differentiating

$$
\begin{array} { r } { \pi ( t - T ) = \overrightarrow { \mathcal { E } } - e \sin \overrightarrow { \mathcal { E } } . } \end{array}
$$

Instead of solving for $d \pmb { \mathcal { T } } ,$ we shall find the variation in the element $\epsilon$ so we use Kepler's equation in the form:

$$
\begin{array} { r } { \pi _ { 2 } ^ { \pm } + \epsilon _ { : } - \tilde { \omega } = \mathcal { E } - e \sin \mathcal { E } . } \\ { \quad \cdot \frac { 1 } { 2 } . } \\ { \frac { 1 } { 2 } . } \end{array}
$$

Here $\Re ^ { \ddag } \div \varepsilon = \ddag$ the mean longitude.

Differentiating (11.6.1）,we find

$$
n + t \frac { d \vec { n } } { d t } + \frac { d \epsilon } { d t } - \frac { d \tilde { \omega } } { d \dot { t } } = ( 1 - e \cos \it { \vec { E } } ) \frac { d \mathcal { E } } { d t } - \sin \it { \vec { E } } \frac { d e } { d \dot { t } } .
$$

Having substituted for $\displaystyle { d \mathscr { n } \big / d \vec { \varepsilon } , \ \vec { d } \tilde { \mathscr { w } } \big / d \vec { \varepsilon } , \ \vec { d } E \big / d \vec { \varepsilon } . }$ and $d e / a _ { t } ^ { 3 }$ ,we have an expression for $d \in \int d ^ { 2 } z$ in which the coefficients of some terms contain t. If we intend $\$ 0$ use these equations over long intervals of time, this will lead to the appearance of disagreeably large quantities.

This difficulty is avoided by the introduction of a new variable, $\notin _ { \tt { I } }$ ,defined bv

$$
\pi z t + \epsilon = \int \pi d t + \epsilon _ { j } .
$$

Differentiating this, we have

$$
\pi \div \frac { \dot { q } \pi } { \dot { q } \dot { t } } \div \frac { \dot { d } \epsilon } { \dot { q } \dot { t } } = \pi \div \frac { \dot { d } \epsilon _ { \mathrm { i } } } { \dot { d } \dot { t } } .
$$

The left-hand side of (11.6.2) becomes

$$
n \div \frac { d \epsilon _ { 1 } } { d t } - \frac { d { \widetilde { \omega } } } { d t } ,
$$

and there are now no embarrassing coeffcients in the equation for $\vec { a } \in _ { 1 } / \vec { a } \vec { \ell }$

It will be seen that when working with $\epsilon _ { \tt I }$ , we are able to assume that $\mathcal { n }$ in the mean anomaly is constant. This is confusing at first, but the advantages will appear more clearly when we consider Lagrange's equations in a different form in Section 11.9.

The derivation of the equation for the variation of $\epsilon _ { 1 }$ is straightforward; the result is

$$
\frac { d \epsilon _ { 1 } } { d \dot { t } } = - \frac { 2 n a r } { \mu } R + \left( 1 - \sqrt { 1 - e ^ { 2 } } \right) \frac { d \widetilde { \omega } } { d t } + 2 \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } \frac { 1 } { 2 } \dot { \imath } \frac { d \Omega } { d t } .
$$

# 11.7 Modifications When Components Are Tangential and Normal -Drag-Perturbed Orbits

Instead of $R$ and $B$ ,consider components $\mathcal { T }$ along the tangent to the orbit and $S$ perpendicular to $z$ and in the instantaneous plane of the orbit, pointing away from the origin. (The appearances of $\tilde { \bar { x } }$ are not affected, and it can be ignored.）

To find the effects of $z$ and $\bar { s }$ , it is possible to proceed from first principles. The change in the speed is

$$
\vec { a } \cdot \vec { V } = \vec { \pm } \cdot \vec { \pmb { \mathscr { z } } } ;
$$

differentiating the energy equation

$$
V ^ { 2 } = \mu \left( \frac { 2 } { r } - \frac { 1 } { a } \right)
$$

we find

$$
2 V d V = \mu { \frac { d a } { a ^ { 2 } } } ,
$$

so that

$$
\frac { d \alpha } { d \vec { \tau } } = \frac { 2 \mathcal { V } \alpha ^ { 2 } } { \mu } \mathcal { T } .
$$

And so on.

Alternatively, we can proceed directly from equations (11.5.13) by resolving $\mathcal { R }$ and $\mathcal { B }$ in the new directions.If $\mathbb { X }$ is the angle between the radius vector and tangent,then

$$
\begin{array} { r } { R = \mathcal { T } \cos \chi + S \sin \chi , } \\ { B = \mathcal { T } \sin \chi - S \cos \chi . . } \end{array}
$$

To find sin $\chi$ and $\cos \chi .$ consider Figure 11.3. Let $\mathbf { \vec { f } }$ and $Q$ be neighboring

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/5495305909e78690bc434177c5f608ab79924d6a3a5a045ebd95f721260c5404.jpg)  
Figure 11.3

positions on the path,and let the perpendicular from $P$ on to $O Q$ meet $O Q$ at $\mathcal { R }$ Then $P Q = d \boldsymbol { s }$ $Q R = d$ ,and $R P = r d v$ The sides of the triangle $P Q R$ are therefore proportional to $\pmb { \ V }$ $\dot { \pmb { \tau } }$ and $p g = h f r$ .Then

$$
\cos \chi : \sin \chi : 1 = \dot { r } : \frac { \hbar } { r } : V
$$

and, substituting for $\dot { \gamma ^ { 2 } }$ ,we find

$$
\sin \chi = { \frac { \hbar } { r V } } , \quad \cos \chi = { \frac { e \mu \sin v } { \hbar V } } .
$$

Animmediate application of these results concerns orbits that are perturbed by drag. If we neglect the effects of the Earth's rotation on the upper atmosphere,the orbit of a close satellite of the Earth will be subject to a negative tangential force, or a drag.This will not affect the plane of the orbit,and here we shall consider only the equations for the variation in $a , e _ { i }$ and $\omega$ Including only the termsin T,we find

$$
\begin{array} { l } { { \displaystyle { \frac { d a } { d t } } = { \frac { 2 V a ^ { 2 } } { \mu } } \mathcal { T } } , } \\ { { \displaystyle { \frac { d \omega } { d t } } = { \frac { 2 \sin v } { e V } } T } , } \\ { { \displaystyle { \frac { d e } { d t } } = 2 \frac { \cos v + e } { V } T } . } \end{array}
$$

Since $T$ is negative, $\pmb { \mathcal { a } }$ is secularly decreased for any law of resistance, but the form of this law will affect what happens to $\mathcal { C }$ and $\omega$ Consider the example of Section 11.1 for which $T = - c ( V / r ^ { 2 } )$ Changing the independent variable from $t$ to $\mathfrak { V }$ ,(11.7.3) and (11.7.4) become

$$
\frac { d \omega } { d v } = - c \frac { 2 \sin v } { e h } , \quad \frac { d e } { d v } = - \frac { 2 c } { h } ( \cos v + e ) ,
$$

and these can be integrated immediately, provided that the elements appearing on the right-hand sides are held constant.

For a satellite moving close to the Earth's surface, the law of resistance is

$$
m \mathcal { T } = - \textstyle \frac { 1 } { 2 } C _ { \mathcal { D } } A \rho \varPsi ^ { 2 } ,
$$

where $A$ is the cross-sectional area, $C _ { \mathcal { D } }$ is the (dimensionless) aerodynamic drag coefficient, with value of the order of one, and $\pmb { \rho }$ is the atmospheric density. m is the mass of the satellite and appears because $\pmb { \updownarrow }$ in the formulas is $\mathtt { a }$ force per unit mass. The equation for the variation of $\pmb { a }$ is

$$
\frac { d a } { d t } = - \frac { C _ { \it 3 } A \rho a ^ { 2 } } { \mu \pi a } V ^ { 3 } .
$$

Now

$$
\begin{array} { c } { { \displaystyle \bar { \gamma } ^ { 2 } = \mu \left( \frac 2 \sigma - \frac 1 \alpha \right) } } \\ { { = \displaystyle \frac { \mu } { a } \frac { 1 + e \cos { E } } { 1 - e \cos { E } } , } } \end{array}
$$

and

$$
\begin{array} { c } { { d \bar { t } = \displaystyle \frac { 1 } { n } d \bar { E } ( 1 - e \cos \bar { E } ) } } \\ { { = \displaystyle \frac { \alpha ^ { 3 / 2 } } { \sqrt { \bar { \mu } } } d \bar { E } ( \bar { \Sigma } - e \cos \bar { E } ) . } } \end{array}
$$

Hence

$$
\frac { d a } { d \mathcal { E } } = - \frac { C _ { D } A \rho a ^ { 2 } } { m } \frac { ( 1 + e \cos \mathcal { E } ) ^ { 3 / 2 } } { ( 1 - e \cos \mathcal { E } ) ^ { 1 / 2 } } .
$$

f $\Delta \alpha$ is the perturbation over one revolution,

$$
\Delta a = - \frac { C _ { D } A a ^ { 2 } } { m } \int _ { 0 } ^ { 2 \pi } \rho \frac { ( \mathbb { 1 } \div e \cos \mathcal { E } ) ^ { 3 / 2 } } { ( \mathbb { 1 } - e \cos \mathcal { E } ) ^ { 1 / 2 } } d \mathcal { E } ,
$$

a result due to Sterne.

In the same way,

$$
\Delta e = - \frac { C _ { D } A a ( 1 - e ^ { 2 } ) } { m } \int _ { 0 } ^ { \pi } \rho \cos { E } \frac { ( 1 + e \cos { E } ) ^ { 1 / 2 } } { ( 1 - e \cos { E } ) ^ { 1 / 2 } } d E ,
$$

and

$$
\Delta \omega = 0 .
$$

# 11.8Hansen's Method

Earlier we considered approaches to the problem of perturbations which involved rectangular coordinates. It is possible to use polar coordinates,and the fundamental method in which these are used is due to Hansen.We have left mention of this until now because Hansen's method combines the variation of coordinates with the variation of the elements. Only the general idea involving the reference orbit will be described here. The reader will find accounts in several references;a recent one is given by Musen in the Astronomical Journal (Ref. 57).

The motion of the osculating plane of the orbit is governed by the component offorce $\mathcal { N }$ ，perpendicular to this plane. Hansen devised a method of finding special perturbations in which the motion of the osculating plane is found from the eguations of the variation of the elements,involving $\mathcal { N }$ ,and the motion in the osculating plane is considered as a two-dimensional perturbation problem ofthe coordinates. The reference orbit isa Keplerian ellipse fixed in the plane of the osculating orbit.Suppose this to be described by $\mathtt { a }$ fictitious planet,with position vector $\pmb { \tau } _ { \hat { \mathbf { i } } } \left( \pmb { \updownarrow } \right)$ ；then the perturbations are the deviations between this and the true orbit $\mathfrak { T } \{ \mathfrak { t } \}$ Now both orbits take place in the same plane,so that the directions fand $\hat { \pmb { \tau } } _ { 1 }$ can be the same but not for the same instant;then we have

$$
\hat { \mathbf { r } } ( \pmb { \mathrm { \updownarrow } } ) = \hat { \mathbf { r } } _ { 1 } \{ \pmb { \mathrm { \updownarrow } } _ { 1 } \} .
$$

Define $\pmb { \nu }$ by

$$
r ( t ) = ( 1 \div \nu ) r _ { 1 } ( \div _ { 1 } ) ,
$$

then vand $\{ \pmb { \dot { \ell } } - \pmb { \dot { \ell } } _ { \Xi } \}$ ,the perturbation in the time,are sufficient to determine the perturbations.

# 11.9The Equations in Terms of $\partial ^ { \infty } / \partial a ,$ etc.

When calculating the disturbing force $\overrightarrow { \mathbfit { x } }$ ,we start off with a set of elements for the perturbed body and a knowledge of the disturbance,whether it be the action of other planets,atmospheric drag, or the effect of the Earth's equatorial bulge,etc. The set of elements is used to calculate the position and time, this calculated position is used to find $\mathbf { \overrightarrow { x } }$ ; therefore $\pmb { \mathbb { F } }$ can be considered as a function of the elements and time. For numerical work it will probably be convenient to resolve $\mathbf { F }$ into $\mathcal { R } , B$ and $\mathcal { N }$ but analytically there are advantages in expressing it in terms of the elements.

Suppose $\mathbf { F }$ to arise from a force function $\Re$ Instead of working with $\Im$ and its components, it is possible to work in terms of $\Re$ and its partial derivatives with respect to the elements. First we shallfind the relations between these partial derivatives and $R , B$ ，and $N$

Let the force $\overrightarrow { \mathbfit { x } }$ change its point of application by small distances $\delta \boldsymbol { \mathfrak { r } } , \boldsymbol { \mathfrak { r } } \delta \boldsymbol { \ b }$ ： and $\gamma \delta n$ in the directions of $R , B$ ,and $\mathcal { N }$ Then it is said to have performed the virtual work

$$
\delta W = R \delta r + B r \delta \dot { b } + N r \delta n .
$$

Now consider $\Re$ as a function of the elements,and interpret the change in the point of application as being due to changes in the elements (the time being kept constant).'We shall suppose that the elements used to calculate the position are $\Omega , \tilde { \omega } , i , a , e ,$ and the mean longitude $l = \pi z + \epsilon$ A change in $\pmb { \xi }$ given by a change in the elements is $\delta \tilde { \iota } = \tilde { \iota } \delta \tilde { \iota } \div \delta \varepsilon = \delta \varepsilon _ { \tilde { \iota } }$ .Then

$$
\delta W = \frac { \partial \Re } { \partial a } \delta a + \frac { \partial \Re } { \partial e } \delta e + \frac { \partial \Re } { \partial ( n t + \epsilon ) } \delta \epsilon _ { 1 } + \frac { \partial \Re } { \partial \tilde { \omega } } \delta \tilde { \omega } + \frac { \partial \Re } { \partial \Omega } \delta \Omega + \frac { \partial \Re } { \partial \dot { a } } \delta \dot { a } .
$$

Before we can equate these two expressions, we must find what changes in the elements correspond to the changes in position, $\delta \mathfrak { F } , \delta \mathfrak { b }$ and $\delta \mathfrak { n }$ Consider the relations between the changes $\delta r , \delta b$ and $\delta \mathfrak { r }$ and those in the position $\mathcal { P }$ of the body as given by changes in $r , \ z$ $\dot { z }$ and $\mathcal { U }$ $\delta r$ obviously presents no difficulties.From Figure $1 3 . 4 a$ we see that

$$
\delta \dot { \boldsymbol { \mathfrak { b } } } = \delta \Omega \cos i + \delta \mathfrak { u } .
$$

To find the effect of $\delta \mathfrak { a }$ we see that if $\gimel$ remains constant (Figure 11.4b), and $i$ changes, $P$ moves to $P ^ { \prime }$ and $P P ^ { \prime } = \delta \Re$ So, in this case,

$$
\delta n _ { ( \Omega \mathrm { \ c o r s t a n t } ) } = \sin u \delta i .
$$

$$
\delta n _ { \left\{ i \cos s \div \mathrm { a n s } \right\} } = - \sin i \cos u \delta \Omega .
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/419e3379c5eab5ce8156a39f19fffab0cd5d40df09c8ea1ef06115eefead16d0.jpg)  
Figure 11.4

(We must remember that we are dealing with spherical triangles.） Now let i stay constant,and vary &；the effect of this is not seen so directly. Let the node shift from $\mathcal { N }$ to $\smash { \vec { s } } ^ { \smash { \vec { s } } ^ { \prime } }$ (Figure 11.4c）and let $\pmb { \mathcal { P } }$ shift to $P ^ { \prime \prime }$ so that $P P ^ { \prime \prime } = \delta \pi$ The great circles $\tilde { \mathcal { N } } \mathcal { P }$ and $\tilde { \Lambda } ^ { t t } \tilde { \mathcal { P } } ^ { t t }$ will meet ina point $o$ where $N ^ { i } O = 9 0 ^ { \circ }$ .Let $Q$ lie on the arc $\tilde { \hat { x } } \tilde { \hat { x } }$ such that $N ^ { f } Q$ is an arc of the great circle of which $o$ is $a$ pole; then

$$
{ \mathcal P } { \mathcal P } ^ { \prime \prime } = \tilde { N } ^ { \prime } Q \cos \mathfrak { U } .
$$

Also from the triangle $\Im \Im ^ { \prime } Q$ since $\hat { \vec { \mathbf { \psi } } } _ { i } ^ { \nabla } \vec { \mathbf { \psi } } ^ { \prime } = \delta \hat { \mathbf { \psi } } _ { i }$ ,we have

$$
\widetilde { N } ^ { \prime } Q = \sin i \delta \Omega .
$$

But we notice that a positive $\delta \Omega _ { \ell }$ leads to a negative $\delta \mathfrak { n }$ ,so that

Finally we have, in general,

$$
\delta \pi = \sin u \delta i - \sin i \cos u \delta \Omega .
$$

Now

$$
r = a ( 1 - e \cos \mathcal { E } ) \quad \mathrm { a n d } \quad M = \mathcal { E } - e \sin \mathcal { E } ,
$$

so that

$$
\delta \mathcal { F } = \frac { \pi } { a } \delta a - a \cos \mathcal { E } \delta e + a e \sin \mathcal { E } \delta \mathcal { E }
$$

and

$$
\delta \vec { E } = \frac { a } { r } \delta \vec { M } + \frac { a } { r } \sin \vec { E } \delta e .
$$

Therefore

$$
\begin{array} { l } { { \delta r = \displaystyle \frac { r } { a } \delta a + \frac { a ^ { 2 } e \sin E } { r } \delta M + a \left( - \cos E + \frac { a e } { r } \sin ^ { 2 } E \right) \delta e } } \\ { { \mathrm { , ~ \ } = \displaystyle \frac { r } { a } \delta a + \frac { a e \sin v } { \sqrt { 1 - e ^ { 2 } } } \delta M + a \frac { - \cos E + e } { 1 - e \cos E } \delta e } } \\ { { \mathrm { = } \displaystyle \frac { r } { a } \delta a + \frac { a e \sin v } { \sqrt { 1 - e ^ { 2 } } } \delta M - a \cos v \delta e . } } \end{array}
$$

Now

$$
\delta M = \delta \epsilon _ { 1 } - \delta \tilde { \omega }
$$

so we have finally

$$
\delta r = { \frac { r } { \alpha } } \delta a \dot { + } \frac { a e \sin v } { \sqrt { 1 - e ^ { 2 } } } ( \delta \epsilon _ { 1 } - \delta \tilde { \omega } ) - a \cos v \delta e .
$$

Since

$$
\begin{array} { c } { { \tilde { u } = v + \tilde { \omega } - \Omega , } } \\ { { { } } } \\ { { \delta \tilde { \left} \tilde { u } = \delta \tilde { v } + \delta \tilde { \omega } - \delta \Omega . \right. } } \end{array}
$$

Consider the equation

$$
\tan { \frac { v } { 2 } } = { \sqrt { \frac { 1 + e } { 1 - e } } } \tan { \frac { \mathcal { E } } { 2 } } .
$$

Take logs and differentiate; we find

$$
\begin{array} { r l } & { \frac { \delta v } { \sin v } = \frac { \delta e } { 1 - e ^ { 2 } } + \frac { \delta \mathcal { E } } { \sin \mathcal { E } } } \\ & { \phantom { \frac { 1 } { 1 } } = \left( \frac { 1 } { \frac { 1 } { 4 } - e ^ { 2 } } + \frac { a } { r } \right) \delta e + \frac { a } { r \sin \mathcal { E } } \delta \mathcal { M } , } \end{array}
$$

from (11.9.5). Now

s0

$$
{ \mathrm {  ~ \bar { { \varepsilon } } ~ } } _ { \mathrm { s i r a } } v = a \sqrt { \dot { \Xi } - e ^ { 2 } } \sin { \cal E } ,
$$

$$
\delta u = \delta \tilde { \omega } - \delta \Omega + \sin { v } \left( \frac { 1 } { 1 - e ^ { 2 } } + \frac { a } { r } \right) \delta e + \frac { a } { r } \sqrt { 1 - e ^ { 2 } } ( \delta \epsilon _ { \perp } - \delta \tilde { \omega } ) .
$$

Then from (11.9.3) we have

$$
\begin{array} { r } { \delta \bar { b } = \sin v \left( \cfrac { 1 } { 1 - e ^ { 2 } } + \frac { a } { r } \right) \delta e + \cfrac { a ^ { 2 } } { r ^ { 2 } } \sqrt { 1 - e ^ { 2 } } \delta \epsilon _ { 1 } } \\ { + \left( 1 - \cfrac { a ^ { 2 } } { r ^ { 2 } } \sqrt { 1 - e ^ { 2 } } \right) \delta \bar { \omega } - ( 1 - \cos i ) \delta \Omega . } \end{array}
$$

Equations (11.9.4), (11.9.6),and (11.9.7) are now substituted into (11.9.1), and this expression for $\delta \mathcal { W }$ is equated with that of (11.9.2). The variations in the elements are independent, so that we can then equate their coefficients to zero:the six resulting equations give the values of $\delta \mathfrak { R } / \delta a _ { \mathfrak { s } } \cdot \cdot \cdot \delta \mathfrak { R } / \delta \mathfrak { i }$ in terms of $\mathcal { R } , \ N$ and $\mathcal { B }$ Before writing them down, we notice that since $\epsilon$ never occurs except in the form $\left( \pi \frac { \ d } { \ d t } + \epsilon \right)$ ，

$$
\frac { \partial \mathfrak { R } } { \partial ( n \mathrm { t } + \epsilon ) } = \frac { \partial \mathfrak { R } } { \partial \epsilon } .
$$

Also,provided we work with $\bar { d } \epsilon _ { 1 } / \bar { d } \bar { \varepsilon } , \partial \Re / \partial a$ is taken with reference to $\pmb { \mathcal { Q } }$ only as it occurs explicitly and not as it occurs through $\mathfrak { P }$ ; this means that in differentiating with respect to $\pmb { \alpha }$ ，we treat $\pmb { \mathscr { T } }$ in the mean longitude as constant.

We find

$$
\begin{array} { r l } & { \frac { \partial \hat { N } } { \partial \alpha } = R _ { \alpha } ^ { \top } , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = R _ { \alpha } ^ { \top } , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = - R a \cos \mathfrak { v } + D a \left( \frac { r } { p } + 1 \right) \mathrm { s i n } \mathfrak { v } , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = R _ { \gamma } \frac { \alpha \epsilon } { \sqrt { 1 - e ^ { 2 } } } \sin \mathfrak { x } + B \frac { \alpha ^ { 2 } } { \tau } \sqrt { 1 - e ^ { 2 } } , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = - R _ { \gamma } \frac { \alpha \epsilon } { \sqrt { 1 - e ^ { 2 } } } \sin \mathfrak { v } - B \frac { \alpha ^ { 2 } } { \sqrt { 1 - e ^ { 2 } } } \sqrt { 1 - e ^ { 2 } } + \mathcal { B } r , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = - B r \sin ^ { 2 } \frac { 1 } { 2 } i - N \gamma \sin \mathrm { i z } \cos \mathfrak { u } , } \\ & { \frac { \partial \hat { N } } { \partial \alpha } = N r \sin \mathfrak { u } . } \end{array}
$$

These equations can now be substituted into (11.5.13) and (11.6.4). The substitutions are straightforward,although the equation in (11.5.13) for $a c / a _ { i } t$ requires some rearrangement. The results are

$$
\begin{array} { l } { \displaystyle \frac { d a } { d t } = 2 \frac { n a ^ { 2 } } { \mu } \frac { \partial \Re } { \partial \epsilon } , } \\ { \displaystyle \frac { d e } { d t } = \frac { n a ( 1 - e ^ { 2 } ) } { \mu e } \frac { \partial \Re } { \partial \epsilon } - \frac { n a \sqrt { 1 - e ^ { 2 } } } { \mu e } \left( \frac { \partial \Re } { \partial \epsilon } + \frac { \partial \Re } { \partial \tilde { \omega } } \right) , } \\ { \displaystyle \frac { d \tilde { \omega } } { d t } = \frac { n a \sqrt { 1 - e ^ { 2 } } } { \mu e } \frac { \partial \Re } { \partial e } + \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \tan \frac 1 2 i \frac { \partial \Re } { \partial i } , } \end{array}
$$

or

$$
\begin{array} { r l } & { \frac { d \omega } { d t } = \frac { n a \sqrt { 1 - \epsilon ^ { 2 } } } { \mu e ^ { t } } \frac { \partial \widehat { \mathbb { R } } } { \partial \epsilon } - \frac { n a } { \mu \sqrt { 1 - \epsilon ^ { 2 } } } \cos \tt t \frac { \partial \widehat \mathbb { R } } { \partial \widehat { \mathbb { A } } } , } \\ & { \frac { d \epsilon _ { 1 } } { d t } = - \frac { 2 n a ^ { 2 } } { \mu } \frac { \partial \widehat { \mathbb { R } } } { \partial a } + \frac { n a \sqrt { 1 - \epsilon ^ { 2 } } } { \mu e } ( 1 - \sqrt { 1 - \epsilon ^ { 2 } } ) \frac { \partial \widehat { \mathbb { R } } } { \partial \epsilon } } \\ & { \phantom { \frac { d \omega } { d t } = } + \frac { n a } { \mu \sqrt { 1 - \epsilon ^ { 2 } } } \tan \tt \frac { 1 } { 2 } \frac { \partial \widehat { \mathbb { R } } } { \partial \widehat { \mathbb { A } } } , } \\ & { \frac { d \lambda } { d t } = \frac { n a } { \mu \sqrt { 1 - \epsilon ^ { 2 } } } \cos \tt t \frac { \partial \widehat { \mathbb { R } } } { \partial \widehat { \mathbb { A } } } , } \\ & { \frac { d \widehat { \mathbb { A } } } { d t } = - \frac { n a } { \mu \sqrt { 1 - \epsilon ^ { 2 } } } \left\{ \operatorname { c s c } + \frac { \partial \widehat { \mathbb { A } } } { \partial \widehat { \mathbb { A } } } + \tan \tt \frac { 1 } { 2 } \left( \frac { \partial \widehat { \mathbb { X } } } { \partial \epsilon } + \frac { \partial \mathbb { A } } { \partial \widehat { \mathbb { A } } } \right) \right\} , } \end{array}
$$

or

$$
\frac { d i } { d t } = - \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \left\{ \csc i \frac { \partial \Re } { \partial \Omega } - \cot i \frac { \partial \Re } { \partial \omega } \right\} .
$$

It is normal to expand $\Re$ as a Fourier series of cosines in which the mean anomaly,nt, and multiples of this appear,among other terms, in the arguments. (See Section 11.12.) In this case the partial differentiation $\partial \Re / \partial \boldsymbol { a }$ will produce factors

$$
\pm \left( { \frac { d n } { d a } } \right)
$$

outside the trigonometric functions (now sines). It is to avoid these coefficients, which could become too large and unwieldy, that we find the variation in $\epsilon _ { \mp }$ accordingly when differentiating with respect to $\pmb { \alpha }$ n is considered constant whenever it appears in the argument of a term in the expansion of .

It isa normal procedure in texts on celestial mechanics to derive the equations (11.9.9) first by analytical methods (which are outside the scope of this present text)；for this approach the reader should consult the texts by Smart or Plummer (Refs.29 and 26). Also, the equations (11.9.8) can be derived differently; the method used here, which the author prefers, is taken from Brown's Lunar Theory (Ref. 55).

# 11.10 Substitutions for Small $e$ ori

In the solar system,e and i are often small,so that some of the denominators in the equations for the variation of the elements become small This diffculty is avoided by the following substitutions.

f $\mathtt { e }$ is small, let

$$
\tilde { h } _ { 1 } = e \sin \tilde { \omega } , \quad \tilde { \kappa } _ { \tilde { \perp } } = e \cos \tilde { \omega } ,
$$

when the equations for e and $\tilde { \omega }$ are replaced by

$$
\begin{array} { l } { \displaystyle \frac { d h _ { 1 } } { d t } = \frac { a n } { \mu } \sqrt { 1 - e ^ { 2 } } \frac { \partial \mathfrak { R } } { \partial k _ { 1 } } + \frac { a n } { \mu } \frac { k _ { 1 } } { \sqrt { 1 - e ^ { 2 } } } \tan \frac { 1 } { 2 } { i } \frac { \partial \mathfrak { R } } { \partial i } } \\ { \displaystyle ~ - \frac { a n h _ { 1 } } { \mu } \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } \frac { \partial \mathfrak { R } } { \partial \epsilon } , } \\ { \displaystyle \frac { d \vec { k } _ { 1 } } { d t } = - \frac { a n } { \mu } \sqrt { 1 - e ^ { 2 } } \frac { \partial \mathfrak { R } } { \partial h _ { 1 } } - \frac { a n } { \mu } \frac { h _ { 1 } } { \sqrt { 1 - e ^ { 2 } } } \tan \frac { 1 } { 2 } { i } \frac { \partial \mathfrak { R } } { \partial i } } \\ { \displaystyle ~ - \frac { a n k _ { 1 } } { \mu } \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } \frac { \partial \mathfrak { R } } { \partial \epsilon } . } \end{array}
$$

If $\mathbf { \chi } _ { i } ^ { \bullet }$ is small, let

$$
\hbar _ { 2 } = \sin i \sin \Omega , \quad \vec { k } _ { 2 } = \sin i \cos \Omega ,
$$

when the equations for $\mathbf { \chi } _ { i } ^ { \mathbf { \bullet } }$ and $\mathfrak { F }$ are replaced by

$$
\begin{array} { r l } & { \frac { d h _ { 2 } } { d t } = \frac { a \pi \cos i } { \mu \sqrt { 1 - e ^ { 2 } } } \frac { \partial \Re } { \partial k _ { 2 } } - \frac { a n } { \mu } \frac { \ddot { h } _ { 2 } \cos i } { \sqrt { 1 - e ^ { 2 } } ( 1 + \cos i ) } \left( \frac { \partial \Re } { \partial \tilde { \omega } } + \frac { \partial \Re } { \partial \epsilon } \right) , } \\ & { \frac { d k _ { 2 } } { d t } = - \frac { a n \cos i } { \mu \sqrt { 1 - e ^ { 2 } } } \frac { \partial \Re } { \partial h _ { 2 } } - \frac { a n } { \mu } \frac { \dot { k } _ { 2 } \cos i } { \sqrt { 1 - e ^ { 2 } } ( 1 + \cos i ) } \left( \frac { \partial \Re } { \partial \tilde { \omega } } + \frac { \partial \Re } { \partial \epsilon } \right) . } \end{array}
$$

The verification of these is left as an exercise.

# 11.11 The General Approach to the Solution of Lagrange's Planetary Equations

Before considering any application of the planetary equations, we shall consider quite generally the approach to their solution. This approach is,almost inevitably,one involving successive approximations.

All the quantities in the planetary equations vary, but with the exception of the time, they vary slowly. Suppose the perturbations to be caused by a planet; the perturbing forces will contain a factor that is the ratio of the mass of the perturbing planet to the mass of the Sun; in the solar system this is a 10-, at most.However the perturbations are caused, R will have some small coefficient, Q. say, as a factor,and the right-hand sides of the planetary equations will be small, of the order of $\alpha$ We might expect the solution for an element, $a _ { \mathfrak { s } }$ say, to be of the form

$$
a = a _ { 0 } + \delta _ { 1 } a _ { 0 } + \delta _ { 2 } a _ { 0 } + \delta _ { 3 } a _ { 0 } \div \cdots
$$

where ao is constant and Siao,S2ao, etc.,are functions of the time of the order of α,α²,etc. To find Siao， it is suffcient to assume that all the elements occurring on the right-hand sides of the planetary equations are constant, the only variable being the time as it occurs explicitly. Then we find

$$
a = a _ { \mathrm { 0 } } + \delta _ { \mathrm { 1 } } a _ { \mathrm { 0 } } ,
$$

which is said to be the first-order solution for $a$

To find $\delta _ { 2 } a _ { 0 }$ the first-order solutionsfor all the elements are substituted into theright-hand sides of the planetary equations,and terms in $\alpha ^ { 2 }$ areretained. The terms in $\alpha$ willbe exactly the same as the terms from which the first-order solutions were found;with the inclusion of terms in $\alpha ^ { 2 }$ ,we find the second-order solution:

$$
a = \alpha _ { 0 } + \delta _ { 1 } a _ { 0 } \div \delta _ { 2 } a _ { 0 } ,
$$

with similar expressions for the other elements. We can continue, formally, to any order of accuracy, building up the series (11.11.1). Since $\alpha$ is usually very small,a solution of low order will probably suffice.

$$
\begin{array} { r } { \frac { d \left( \delta _ { \vec { \mathbf { r } } } A _ { m 0 } \right) } { d t } = \alpha \mathcal { F } _ { \vec { m } } ( A _ { i o } ) . } \\ { . . . . } \end{array}
$$

To put the situation more explicitly,let the elements be $A _ { 1 } , A _ { 2 } , \dotsc A _ { 8 }$ ,and let the equation for $A _ { m }$ be

$$
\frac { d A _ { m } } { d \dot { t } } = \alpha F _ { m } ( A _ { 1 } , A _ { 2 } , \cdot \cdot \cdot A _ { 6 } ) \equiv \alpha F _ { m } ( A _ { i } ) .
$$

Then each side can be expanded:

$$
\begin{array} { l } { \displaystyle { \frac { d A _ { m 0 } } { d t } + \frac { d \left( \delta _ { 1 } A _ { m 0 } \right) } { d t } + \frac { d \left( \delta _ { 2 } A _ { m 0 } \right) } { d t } + \cdots } } \\ { \displaystyle { \qquad = \alpha \left\{ F _ { m } \left( A _ { i 0 } \right) + \sum _ { i = 1 } ^ { 6 } \left( \frac { \partial F _ { m } } { \partial A _ { i } } \right) _ { 0 } \delta A _ { i 0 } + \cdots \right\} } } \end{array}
$$

where

$$
\begin{array} { c } { \hat { A } _ { m } = \hat { A } _ { m 0 } + \delta \hat { A } _ { m 0 } } \\ { = \hat { A } _ { m 0 } + \delta _ { 1 } \hat { A } _ { m 0 } + \delta _ { 2 } \hat { A } _ { m 0 } + \cdot \cdot \cdot } \end{array}
$$

Since $A _ { m } = 0$ is constant, the first term on the left-hand side of (11.11.5) would not normally appear.

The equations for the first-order solution are found from the terms in (11.11.5) of the order of $\alpha .$ theyare

The equations for the second-order solution (of the order of α²) are

$$
\frac { d ( \delta _ { 2 } A _ { m 0 } ) } { d t } = \alpha \sum _ { i = 1 } ^ { 6 } \left( \frac { \partial F _ { m } } { \partial A _ { i } } \right) _ { 0 } \delta _ { \frac { 1 } { 2 } } A _ { i 0 } ,
$$

and so on.

# 11.12 The Disturbing Function

In this section we shall consider the type of expression obtained when the disturbing function  is expressed in terms of the elements of the disturbed and disturbing body,in this casea planet.Fuller treatments of this matter are given in various texts, but a complete treatment would require a text of its own. Here we are concerned with the nature of the function, and shall consider it only very generally. The results will be used in the following section.

Suppose a planet of mass m to be perturbed by another planet of mass m'. The disturbing function is, from Section 9.4

$$
\mathfrak { R } = m ^ { \prime } \left( \frac { 3 } { \Delta } - \frac { r \cos S } { e ^ { \alpha ^ { \prime 2 } } } \right) ,
$$

where r and r' are the radius vectors of the two planets with respect to the Sun. $\boldsymbol { s }$ is theangle between them,and

$$
\Delta ^ { 2 } = r ^ { 2 } + r ^ { \prime 2 } - 2 r r ^ { \prime } \cos S .
$$

Theunit of time is chosen to make $k = \vec { \hat { \mathbf { \ell } } }$

Let us suppose, for a start, that the planets move in the same plane in circular orbits,and that a'>a.Then

$$
\begin{array} { l } { { \displaystyle \mathfrak { R } = \frac { m ^ { \prime } } { ( a ^ { 2 } + a ^ { \prime 2 } + 2 a a ^ { \prime } \cos S ) ^ { 1 / 2 } } - \frac { m ^ { \prime } a \cos S } { a ^ { \prime 2 } } } } \\ { { \displaystyle ~ = \frac { m ^ { \prime } } { a ^ { \prime } } \left[ 1 - 2 \frac { a } { a ^ { \prime } } \cos S + \left( \frac { a } { a ^ { \prime } } \right) ^ { 2 } \right] ^ { - 1 / 2 } - \frac { m ^ { \prime } } { a ^ { \prime } } \left( \frac { a } { a ^ { \prime } } \right) \cos S } } \\ { { \displaystyle ~ = \frac { m ^ { \prime } } { a ^ { \prime } } \left\{ 1 - \frac { 1 } { 2 } \left( \frac { a } { a ^ { \prime } } \right) ^ { 2 } + \frac { 3 } { 8 } \left[ 2 \left( \frac { a } { a ^ { \prime } } \right) \cos S - \left( \frac { a } { a ^ { \prime } } \right) ^ { 2 } \right] ^ { 2 } + \cdots \right\} . } } \end{array}
$$

The powers of cos S are expressed in terms of cosines of multiples of S; we then havea series of the form

$$
\Re { = \sum _ { i } C _ { i } \cos i S . }
$$

The coefficients C: are expanded in powers of a/a'; the number of terms needed depends naturally on the smallness of a/a'.

For the example above, S is simply the difference between the anomalies. Now suppose that the orbits are.still circular but that they no longer lie in the

same plane; then S willalso depend on the mutual inclination of the two orbits. Let this be i; then if u and u' are measured from the node,

$$
\begin{array} { c } { { \cos S = \cos u \cos u ^ { \prime } + \cos i \sin u \sin u ^ { \prime } } } \\ { { = \cos ^ { 2 } { \frac { i } { 2 } } \cos ( u - u ^ { \prime } ) + \sin ^ { 2 } { \frac { i } { 2 } } \cos ( u + u ^ { \prime } ) . } } \end{array}
$$

now takes the form

$$
{ \Re } = \sum _ { j j ^ { \prime } } C _ { j j ^ { \prime } } \cos ( j u + j ^ { \prime } u ^ { \prime } ) .
$$

The Cj now depend on i as well as on α and a'; if the ecliptic is taken as the plane of reference, they will depend on i,i',a,and a'.

Now let us introduce elliptic orbits. Instead of $\mathcal { U }$ and ${ \hat { \mathbf { \Omega } } } _ { \hat { \mathbf { L } } } ^ { f }$ we write $\tilde { \omega } - \Omega \div \mathfrak { v }$ and @'-&'+u.The C's now involver and r',and these, as wellas v and v,can beexpanded in Fourier series in the mean anomalies M and M',in which the coefficients involve powers of the eccentricities (which,with luck,will be small). Terms such as cos(ju+ j'u') can be expanded in Fourier series such that the arguments involve the angles M,,&,and M',@',S',and the coefficients involve a,e,a',e'.The C's have been similarly expanded, except that here the coefficients involve $\dot { \pmb { \hat { \varepsilon } } }$ and $\hat { \mathfrak { z } } ^ { \vec { \prime } }$ inaddition.Finally the whole expression can be put into the form

$$
\begin{array} { r } { \mathfrak { R } = \sum \mathcal { C } \cos \mathcal { D } , } \end{array}
$$

where

$$
C = A e ^ { q _ { 1 } } e ^ { ^ { j q _ { 2 } } ( \frac { \cdot } { 1 } \widehat { \sf { a } } \widehat { \sf { a } } ) \widehat { \sf { a } } \widehat { \sf { a } } \widehat { \sf { a } } \widehat { \sf { a } } ^ { \dagger } ) ^ { q _ { 3 } } } ,
$$

$A$ being a function of $a$ and $a ^ { \prime }$ , homogeneous and of degree $- I$ ,and

$$
\begin{array} { r } { D = p ( M + \widetilde { \omega } - M ^ { \prime } - \widetilde { \omega } ^ { \prime } ) + p _ { 1 } M + P _ { 2 } M ^ { \prime } + p _ { 3 } ( M + \widetilde { \omega } - \Omega ) \qquad } \\ { + p _ { 4 } ( M ^ { \prime } + \widetilde { \omega } ^ { \prime } - \Omega ^ { \prime } ) . } \end{array}
$$

The q's and p's are integers; some of the p's can be negative. There are restrictions on their possible values,as follows:

$$
q _ { i } - | p _ { i } | , \quad { \mathrm { w h e r e ~ } } i = 1 , 2 , 3 , 4 ,
$$

are even positive integers, or zero,and (ps +p4),and therefore, (q3 + q4） are always even. A series of the type (11.12.4) with these restrictions is called a $D$ Alembert series.

The argument $\beta$ can be written:

$$
D = q \tilde { M } + q ^ { I } \tilde { M } ^ { I } - \dot { \jmath } _ { 1 } \tilde { \omega } - \dot { \jmath } _ { 2 } \tilde { \omega } ^ { I } - \dot { \jmath } _ { 3 } \Omega - \dot { \jmath } _ { 4 } \Omega ^ { I } .
$$

It follows that

$$
p _ { 1 } = q + j _ { 1 } , \quad p _ { 2 } = q ^ { \prime } + j _ { 2 } , \quad p _ { 3 } = j _ { 3 } , \quad p _ { 4 } = j _ { 4 } .
$$

In the new form the restrictions become

$$
q _ { 1 } - \frac { 1 } { 4 } q + \dot { \bar { j } } _ { 1 } \frac { 1 } { 4 } , \quad q _ { 2 } - \frac { 1 } { 4 } q ^ { \prime } + \dot { j } _ { 2 } \frac { 1 } { 4 } , \quad q _ { i } - \lvert \dot { j } _ { i } \rvert \quad \mathrm { w i n e r e } \ i = 3 , \frac { \dot { s } } { 4 } ,
$$

are even positive integers, or zero, and $( j _ { 3 } + j _ { 4 } )$ , and therefore, $( g _ { 3 } + g _ { 4 } )$ are always even.

These restrictions are not much of a comfort. The series are very complicated,and at this stage it is unrewarding to consider them further. But even from such a general expression as (11.12.4) it is possible to find out something about the general character of the first-order solutions of the planetary equations.

# 11.13 General Discussion of the First-Order Solution of the Planetary Equations

Consider the disturbing function in the form (11.12.4) where now

$$
D = q \left( \int n d t + \epsilon _ { 1 } \right) + q ^ { \prime } \left( \int n ^ { \prime } d t + \epsilon _ { 1 } ^ { \prime } \right) - j _ { 1 } \tilde { \omega } - j _ { 2 } \tilde { \omega } ^ { \prime } - j _ { 3 } \Omega - j _ { 4 } \Omega ^ { \prime } .
$$

When differentiating partially with respect to $a , n$ is kept constant. Two cases must be considered which can make a $\mathfrak { D }$ independent of the time:

$$
\mathcal { G } = \mathcal { G } ^ { \prime } = \emptyset .
$$

This will happen for one term, ${ \bf \vec { \mathcal { D } } _ { \mathfrak { V } } }$

$$
q n + q ^ { \prime } n ^ { \prime } = 0 \mathrm { f o r ~ s o m e ~ v a l u e s ~ o f ~ } q , q ^ { \prime } .
$$

This can only happen exceptionally; also, since all the quantities are slowly varying, it can only happen instantaneously. In practice we are concerned with the case

$$
g n + q ^ { \prime } n ^ { \prime } \ i s \ s m a { l l } \ f o r \ s o m e \ v a \not u e s \ o f \ q , \ q ^ { \prime } .
$$

Let $\hat { A } _ { \ I }$ be one of $\tilde { \omega } , \varepsilon _ { \ I }$ ,and $\Updownarrow$ , and consider the equations for $a ^ { 2 } + ( d ^ { 2 } )$ from (11.9.9). The partial differentiations on the right-hand sides will affect only the $C ^ { \bullet } { \mathbf { s } } ,$ so we shall have equations of the form

$$
\frac { d A _ { 1 } } { d t } = \sum C _ { 1 } \cos D + C _ { 1 0 } \cos D _ { 0 } ,
$$

where the summation excludes $\mathfrak { g } = \mathfrak { g } ^ { \prime } = \mathfrak { d }$ Since we are interested here only in the frst-order solutions, all quantities but $\pmb { \dot { \tau } }$ are constant, and these equations can be integrated term by term (assuming suitable convergence of the series) to give

$$
A _ { 1 } = \sum C _ { 1 } \frac { 1 } { q n + q ^ { \prime } n ^ { \prime } } \sin \cal { D } + t C _ { 1 0 } \cos \cal { D } \ o _ { 0 } + \mathrm { c o r s t a n t } .
$$

Let A2 be one of e and i. Now the partial differentiations affect only the $D ^ { s } s$ so that

$$
\frac { d \vec { A } _ { 2 } } { d \vec { t } } = \sum C _ { 2 } \sin D + C _ { 2 0 } \sin D _ { 0 }
$$

and, on integration, we find

$$
A _ { 2 } = - \sum C _ { 2 } \frac { 1 } { q n + q ^ { \prime } n ^ { \prime } } \cos { D } + i C _ { 2 0 } \sin { D } _ { 0 } + \mathrm { c o n s t a n t } .
$$

Finally consider the equation for α. This contains no term that is independent of the time (as long as qn + q'n'/ O) because Do does not contain e. Hence

$$
\frac { \dot { a } a } { \dot { d } \dot { \varepsilon } } = \sum C _ { 3 } ( g + q ^ { \prime } ) \sin \mathcal { D }
$$

so that

$$
a = - \sum C _ { 3 } \frac { q + q ^ { \prime } } { q n + q ^ { \prime } n ^ { \prime } } \cos { \mathcal D } + \mathrm { c o n s t a n i t } .
$$

Accordingly.every perturbation except that of $\pmb { \alpha }$ contains $\mathtt { a }$ secular term as wellas periodic terms. In fact it can be shown that a has no secular perturbation of the second order (Poisson's theorem)；this is important when considering the stability of the solar system over long periods of time.

The solutions found are only of the first-order;second-order solutions will introduce terms in $\ell ^ { 2 }$ into the perturbations of all elements except a.Higher order solutions lead to the appearance of higher powers of t. As they stand, the first-order solutions will clearly not be valid for large $\ddagger$ but the fact that the general solution involves a power series in t suggests that the terms in t in (11.13.2) and (11.13.3) are merely the first terms in series for functions, such as sine functions, which remain bounded for all t,and might oscillate. This can be shown to be the case (for the disturbing function considered here) for the elements $i$ and $e$ Forexample,the eccentricity of the Earth's orbit is gradually being diminished by planetary perturbations at the present time,but in about 24,000 years it will start to increase.

It remains to consider the case when ng+n'g'is small.When it is zero,all the elements have additional secular terms,but since $\pmb { \mathscr { z } }$ and $\gamma ^ { \prime }$ are not constant, this is of academic interest only. But when it is small for some pair of values $\mathscr { q }$ and $q ^ { j }$ (there may be several such pairs which are significant),a denominator in each solution becomes small, so that the corresponding periodic term has large amplitude. The period of such a term is

$$
\frac { 2 \pi } { \mathfrak { R } \mathfrak { Q } + \mathfrak { N } ^ { \prime } \mathfrak { Q } ^ { \prime } }
$$

which is large; these terms are known as long-period inequalities.

Given any $\pmb { \mathcal { Y } }$ and $\gamma ^ { \prime }$ $n g + n ^ { \prime } g ^ { \prime }$ can be made arbitrarily small by suitable ${ \mathfrak { q } }$ and $q ^ { q }$ : but to achieve this at least one of the latter may have to be made very large, and,looking back at the general derivation of the perturbing function, we see that this implies a very small $\pmb { C }$ Hence we are interested in the possibility of small ng+ n'g' when q and q' are not too large numerically. This happens in some minor planet orbits, but the values of a that would make n for a minor planet commensurable for $\mathfrak { X } \mathfrak { z }$ for Jupiter are not mostly popular. Similarly, gaps are observed in Saturn's rings,where particles would be in resonance with the inner satellites of Saturn.

The most famous case of a long-period inequality occurs in the mutual perturbations of Jupiter and Saturn. For the two planets we have n = 299".13 and $\mathfrak { r } ^ { \prime } = 1 2 0 ^ { \prime \prime } . 4 5$ If $q = - 2$ and $g ^ { \prime } = 5$ ，then

$$
{ \mathfrak { q } } { \mathfrak { z } } + { \mathfrak { q } } ^ { \prime } { \mathfrak { x } } ^ { \prime } = 3 ^ { \prime \prime } . 9 9 .
$$

The resulting period is about $\mathfrak { G O }$ years. We also have

$$
- 2 9 \pi + 7 2 \pi ^ { \prime } = 2 ^ { \prime \prime } . 3 7 ,
$$

but this is not so important, since the $\pmb q$ s are too large for the corresponding $\pmb { C }$ s to be of much consequence.

The expression for the mean longitude $\pmb { \xi }$ involves

$$
\int \pi d t = \rho , s a y .
$$

Substituting for $\Im$ ,we have

$$
\rho = \sqrt { \mu } \int a ^ { - 3 / 2 } d t
$$

so that

$$
\begin{array} { c } { { \frac { d ^ { 2 } \rho } { d \dot { t } ^ { 2 } } = - \frac { 3 } { 2 } \sqrt { \mu } a ^ { - 5 / 2 } \frac { d a } { d t } } } \\ { { = - \frac { 3 } { a ^ { 2 } } \frac { \partial \Re } { \partial \epsilon } , } } \end{array}
$$

from (11.9.9). Hence

$$
\rho = - 3 \int \int \frac { 1 } { a ^ { 2 } } \frac { \partial \mathfrak { R } } { \partial \varepsilon } d \vec { \tau } d \vec { \tau } .
$$

The double integration means that instead of $3 3 y + 1 2 ^ { 7 } \textcircled { 3 }$ appearing ina denominator, we have $\{ \Im \Im \} \div \Im ^ { \prime } \{ \tilde { q } ^ { \prime } \} ^ { 2 }$ Hence the most noticeable effect of a long-period inequality is in the mean longitude. Jupiter and Saturn are perturbed by $2 1 ^ { \prime }$ and $\mathring { \mathfrak { L } } \mathfrak { P } ^ { \prime }$ ,respectively, in this way. The correct explanation of this was first given by Laplace.

# 11.14 Secular Perturbations

From the preceding section we see that the secular terms found in the firstorder solution arise from the constant term in the disturbing function, when the

latter is expanded in a Fourier series in the mean anomalies of the disturbed and disturbing planets. We may find this term from the integral

$$
\frac { 1 } { 4 \pi ^ { 2 } } \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } \Re d M d M ^ { \prime }
$$

since all but the constant term vanishes.

In this section we shall consider an important interpretation of the equation forsecular perturbations,which is due to Gauss.As an example,consider the secular variation in $\dot { \varepsilon }$ the equation for the first-order perturbation of $\textit { i }$ is of the form

$$
\frac { d i } { d \dot { t } } = A _ { 0 0 } + \sum _ { j \neq 0 \atop j ^ { t } \neq 0 } A _ { j j ^ { \prime } } \cos ( j M + j ^ { \prime } \tilde { M } ^ { f } + q )
$$

so that

$$
i - i _ { 0 } = { \cal A } _ { 0 0 } t + \sum _ { \stackrel { j \neq 0 } { j \neq 0 } } { \cal A } _ { j j ^ { \prime } } { \frac { \sin ( j M + j ^ { \prime } M ^ { \prime } + q ) } { j \pi + j ^ { \prime } \pi ^ { \prime } } } ,
$$

so it is the term $\frac { A } { 2 } \textcircled { > } 0$ in which we are interested. Multiply both sides of(11.14.1) by $d \mathscr { M } d \mathscr { M } ^ { \prime }$ and integrate from $\Updownarrow$ to $2 \pi$ foreach anomaly;we find

$$
\int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } { \frac { d i } { d t } } d M d M ^ { \prime } = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } A _ { 0 0 } d M d M ^ { \prime } = { \frac { 4 \pi ^ { 2 } } { 4 \pi } } { \cal A } _ { 0 0 } ,
$$

so that

$$
A _ { 0 0 } = \frac { 1 } { 4 \pi ^ { 2 } } \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { d i } { d t } d \bar { M } d M ^ { \prime } .
$$

Using the equation for $\sin i \int d \overrightarrow { i }$ from (11.5.13), we find

$$
A _ { 0 9 } = \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \frac { 1 } { 4 \pi ^ { 2 } } \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 2 \pi } r \cos u N d M d M ^ { \prime }
$$

and, since $\mu = a ^ { 3 } \mathfrak { z } ^ { 2 }$ , this can be writen:

$$
\hat { A } _ { 0 3 } = \frac { 1 } { 2 \pi n a ^ { 2 } \sqrt { \frac { 1 } { 4 } - e ^ { 2 } } } \int _ { 0 } ^ { 2 \pi } r \cos \sin \left\{ \frac { \frac { 1 } { 2 \pi } } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \tilde { N } \hat { d } \tilde { M } ^ { \prime } \right\} \hat { d } \tilde { M } .
$$

Define $\lambda _ { \mathfrak { d } } ^ { \vec { r } }$ by

$$
N _ { \ell 3 } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \bar { N } ^ { \bar { \ell } \bar { M } ^ { \prime } } ,
$$

with similar expressions for $R _ { 0 }$ and $\mathcal { B } _ { \mathfrak { d } }$ Then

$$
\stackrel { A } { \scriptscriptstyle A } _ { 0 0 } = \frac { 1 } { 2 \pi n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \int _ { 0 } ^ { 2 \pi } \tilde { N } _ { 0 } r \cos \psi d \tilde { \cal M } .
$$

Consider a definite point $\mathcal { P }$ in the orbit of ${ \mathcal { H } } _ { \ell }$ ,the perturbed body,and the value of $\mathcal { N }$ that is exerted at $\mathcal { P }$ by ${ \mathfrak { M } } ^ { j }$ ,the perturbing body. If we consider the average of this value over a complete revolution of ${ \mathfrak { M } } ^ { \sharp }$ ,we find it to be

$$
\frac { \displaystyle \int _ { 0 } ^ { 2 \pi } { \cal N } d { \cal M } ^ { \prime } } { \displaystyle \int _ { 0 } ^ { 2 \pi } d { \cal M } ^ { \prime } } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } { \cal N } d { \cal M } ^ { \prime } = { \cal N } _ { 0 } .
$$

Now consider the elliptic orbit of $m ^ { \prime }$ as a thin wire, of which the line density of an element of length $\vec { a } s ^ { \prime }$ is proportional to the time $d \acute { t }$ spent by $m ^ { \prime }$ in traversing $\vec { d } \hat { \mathbf { s } } ^ { \prime }$ in its orbit.The density can be written

$$
\rho = \frac { c } { 2 \pi } \frac { d \vec { A } \cdot \vec { i } ^ { j } } { d s ^ { j } } ,
$$

where $\mathfrak { c }$ is some constant. Then the total mass of the wire is

$$
\int p d s ^ { \prime } = \frac { c } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \dot { d M } ^ { \prime } = c .
$$

Now suppose the mass $m ^ { \prime }$ to be distributed over the wire in this way; then $c = m ^ { \prime }$ .The value of the normal force exerted by the wire at $P$ will be

$$
\int _ { 0 } ^ { 2 \pi } \rho \left( \frac { N } { m ^ { \prime } } \right) d s ^ { \prime } = \int _ { 0 } ^ { 2 \pi } \frac { m ^ { \prime } } { 2 \pi } \frac { d M ^ { \prime } } { d s ^ { \prime } } \frac { N ^ { \prime } } { m ^ { \prime } } d s ^ { \prime } = N _ { 0 } ,
$$

since $N f _ { \max }$ is the normal force per unit mass of the disturbing planet.

Hence the configuration obtained by spreading out the mass of the disturbing planet ${ \widehat { \pmb { \mathscr { E } } } } ^ { \prime }$ around its orbit,in sucha way that the mass of an element is proportional to the time spent by ${ \mathfrak { M } } ^ { \sharp }$ in that element in its orbit, will reproduce the secular perturbations suffered by another planet through the action of $m ^ { \prime }$

This is the basis of Gauss’method for the calculation of secular perturbations.For further details the reader should consult the texts by Smart and Plummer (Refs.29 and 26).The simplification introduced is that the mean anomaly of the disturbing planet can be dispensed with in the equations; but expressions must be evolved for finding the forces exerted by the“loaded"elliptic wires. The method was not translated into practical form by Gauss. This wasaccomplished later,in particular by Hill.

# 11.15 The Motion of a Satellite in the Field of an Oblate Planet

We shall assume that a satellite of negligible mass moves around a primary that is slightly distorted from a sphere, but which has symmetry about an axis.Atmospheric dragis entirely neglected.From (5.6.9） the potential of the primary can be expressed as

$$
V = - { \frac { \mu } { r } } \left\{ 1 - { \frac { 1 } { r ^ { 2 } } } J _ { 2 } { \frac { 1 } { 2 } } ( 3 \sin ^ { 2 } \delta - 1 ) - { \frac { 1 } { r ^ { 3 } } } { \tilde { J } } _ { 3 } { \frac { 1 } { 2 } } ( 5 \sin ^ { 3 } \delta - 3 \sin \delta ) - \cdots \right\}
$$

where μ = MG, M being the mass of the primary,and δ is the declination measured from the equator of the primary. The unit of length here is the Earth's equatorial radius. For an oblate planet,J2 is positive.

Initially we shallneglect all the small coeffcients except J2. The disturbing fnntion ic then

$$
\begin{array} { r } { \frac { 3 3 } { 3 2 } = - \frac { \mu } { 2 r ^ { 3 } } \mathcal { J } _ { 2 } ( 3 \sin ^ { 2 } \delta - 1 ) . } \end{array}
$$

But

$$
\begin{array} { c } { \sin \delta = \sin i \sin \alpha } \\ { = \sin i \sin ( \omega + v ) , } \end{array}
$$

So

$$
\Re = - \frac { \mu } { 2 r ^ { 3 } } \mathcal { J } _ { 2 } ( 3 \sin ^ { 2 } i \sin ^ { 2 } ( \omega + v ) - 1 ) .
$$

If r and v are expressed in terms of the elements and mean anomaly by suitable series,then R is in a form that is ready for the application of the formulas (11.9.9).

Readers requiring a complete treatment of the problem using the planetary equations should consult an article by Kozai in the Astronomical Journal (Ref. 58).Here we shall find the first-order secular perturbations and discuss also those of long- and short-period.

To find the secular perturbations,we remember that the part of $\Re$ responsible for these is given by the constant term in the Fourier expansion of $\Re$ in terms of M. Hence

$$
\Re _ { s } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \Re d \Im A .
$$

Using the following relations (which the reader may confirm):

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { 1 } { r ^ { 3 } } d M = \frac { \frac { 1 } { \lambda } } { a ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } }
$$

and

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { 1 } { r ^ { 3 } } \cos 2 ( \omega + v ) d M = 0 ,
$$

we find

$$
\Re _ { s } = - \frac { \mu J _ { 2 } } { 2 a ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( \frac { 3 } { 2 } \sin ^ { 2 } i - \frac { 1 } { 2 } \right) .
$$

We see immediately from this that ${ \mathcal { Q } } , { \mathcal { C } } ,$ and $\dot { \mathfrak { z } }$ suffer no secular perturbations. Instead of workingwith $\epsilon _ { \tt A }$ ,we shall find the perturbation in the mean anomaly,

$$
M = \epsilon _ { 1 } + \int \pi d \ell - \tilde { \omega } .
$$

Then we have

$$
\frac { d M } { d t } = \pi - \frac { \pi a } { \mu } \frac { 1 - e ^ { 2 } } { e } \frac { \partial \Re } { \partial e } - \frac { 2 \pi a ^ { 2 } } { \mu } \frac { \partial \Re } { \partial a } ,
$$

where n, the first term on the right-hand side,must be considered a variable even in the first-order work; this assumes that the perturbations in a are known, but,as far as secular perturbations are concerned,these are zero.

Using the expression for $\mathfrak { R } _ { s }$ ,we find the secular perturbations from

$$
\begin{array} { l } { d \omega _ { s } = - \displaystyle \frac { 3 n J _ { 2 } } { 2 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } ( \frac 5 2 \sin ^ { 2 } i - 2 ) d t , } \\ { \cdot d \mathfrak { T } _ { s } = - \displaystyle \frac { 3 n J _ { 2 } } { 2 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \cos i d t , } \\ { d \mathcal { M } _ { s } = n d t  1 - \displaystyle \frac { 3 J _ { 2 } } { 2 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } ( \frac 3 2 \sin ^ { 2 } i - 1 )  \cdot | } \end{array}
$$

Hence for an oblate planet, the nodes regress. The line of apsides advances or regresses, depending on whether i is less than or greater than the critical value given by sini= 2/√5. The perturbation in M can be interpreted as a perturbation of the period; i.e.,we can allow for it by usinga slightly different or perturbed value of n. Observations of an artificial satellite made over a long enough period will yield the secular perturbations,particularly that of the node, and if they are interpreted according to equations (11.15.6), they will lead to a first-order estimate of ${ \pmb J } _ { 2 }$ for the Earth.

That part of $\Re$ remaining after $\Re _ { s }$ has been subtracted is

$$
\mathfrak { R } _ { p } = - \frac { \mu J _ { 2 } } 2 \left( \frac 3 2 \sin ^ { 2 } i - 1 \right) \left( \frac 1 { r ^ { 3 } } - \frac 1 { a ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \right) + \frac { 3 \mu J _ { 2 } } { 4 r ^ { 3 } } \sin ^ { 2 } i \cos 2 ( \omega + v ) .
$$

This will produce periodic perturbations, and to illustrate its application we shall find the short-period perturbations in i,which is the simplest case. The expansions ofr and u involve a,e,and M but not w,so that Op/dw can be written down directly from (11.15.7).The equation for $i$ is

$$
\begin{array} { c } { \frac { d i _ { p } } { d t } = \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \cot i \frac { \partial \mathfrak { R } _ { p } } { \partial \omega } } \\ { = - \frac { 3 n a J _ { 2 } } { 4 \sqrt { 1 - e ^ { 2 } } } \sin 2 i \frac { s i n 2 ( \omega + v ) } { r ^ { 3 } } . } \end{array}
$$

To integrate this, change from $\vec { a } \vec { \tau }$ to $\tilde { \phi ^ { } } { \mathfrak { z } }$ ,using

$$
\tau ^ { 2 } \frac { d v } { d \dot { \bar { t } } } = \eta \dot { z } ^ { 2 } \sqrt { 1 - e ^ { 2 } } ,
$$

and then put

$$
{ \frac { 1 } { r ^ { 2 } } } = { \frac { 1 + e \cos v } { a ( 1 - e ^ { 2 } ) } } .
$$

We find

$$
\begin{array} { l } { { d \displaystyle { \bar { \imath } _ { p } = - \frac { 3 J _ { 2 } } { 4 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \sin 2 i ( 1 + e \cos v ) \sin 2 ( \omega + v ) d v } } } \\ { { = - \displaystyle { \frac { 3 J _ { 2 } } { 4 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \sin 2 i \left\{ \sin ( 2 \omega + 2 v ) + \displaystyle { \frac { e } { 2 } \sin ( 2 \omega + 3 v ) + \displaystyle { \frac { e } { 2 } \sin ( 2 \omega + v ) } } d v } . } } } \\right\end{array}
$$

Then

$$
\begin{array} { l } { { \displaystyle \Delta i _ { p } = \int d i _ { p } } } \\ { { \displaystyle \quad = \frac { 3 \mathcal { I } _ { 2 } } { 8 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \sin 2 i \left\{ \cos ( 2 \omega + 2 v ) + \frac { e } { 3 } \cos ( 2 \omega + 3 v ) + e \cos ( 2 \omega + v ) \right\} . } } \end{array}
$$

Now the mean value of △ip taken over one revolution is not zero; in fact we find

$$
\overline { { \Delta i _ { p } } } = - \frac { J _ { 2 } } { 8 a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \sin 2 i \cos 2 \omega \frac { ( 1 - \sqrt { 1 - e ^ { 2 } } ) ^ { 2 } } { e ^ { 2 } } ( 1 + 2 \sqrt { 1 - e ^ { 2 } } ) .
$$

It is about this mean value that i fuctuates with short-period. But we have seen that w has a secular variation, so that the trigonometric terms that include w in the argument contribute long-period perturbations of i. (11.15.9) shows some of the long-period perturbations in iof the first-order; a complete solution would take more space that we can afford here.

Now consider the consequences of including the third harmonic,with coefficient $J _ { 3 }$ inthe disturbing function.The additional term in $\Re$ is

$$
\Re _ { 3 } = - { \frac { \mu J _ { 3 } } { 2 r ^ { 4 } } } \sin i \sin ( v + \omega ) \{ 5 \sin ^ { 2 } i \sin ^ { 2 } ( v + \omega ) - 3 \} .
$$

This produces long- and short-periodic perturbations but no secular perturbation.The short-period perturbations result from the variation of M around the orbit; they are of order Js, so they are very small and difficult to observe. But we can reasonably hope that some of the long-period perturbations, resulting from the secular variation of w, may have amplitudes large enough to be observed. For these perturbations we are concerned with the changes of w and not of M; therefore we can take the mean value of the disturbing function with respect to M.The term in  due to the third harmonic can be written:

$$
\Re _ { 3 } = - \frac { \mu J _ { 3 } } { 8 r ^ { 4 } } \sin i \{ 3 ( 5 \sin ^ { 2 } i - 4 ) \sin ( v + \omega ) - 5 \sin ^ { 2 } i \sin ( 3 \upsilon + 3 \omega ) \} ,
$$

and using the following mean values with respect to M:

$$
( \frac { a } { r } ) ^ { 4 } \cos v = e ( 1 - e ^ { 2 } ) ^ { - 5 / 2 }
$$

$$
{ \overline { { \left( { \frac { a } { r } } \right) ^ { 4 } \sin v } } } = { \overline { { \left( { \frac { a } { r } } \right) ^ { 4 } \cos 3 v } } } = { \overline { { \left( { \frac { a } { r } } \right) ^ { 4 } \sin 3 v } } } = 0 ,
$$

we find the mean value of this term to be

$$
\overline { { \mathfrak { R } _ { 3 } } } = - \frac { 3 \mu \bar { J } _ { 3 } } { 2 \alpha ^ { \frac 4 2 } } \sin i \left( \frac { 5 } { 4 } \sin ^ { 2 } i - 1 \right) \frac { e } { ( \mathrm { 1 } - e ^ { 2 } ) ^ { 5 / 2 } } \sin \omega \mathrm { . }
$$

The equation for the corresponding long-period perturbation of $j$ is

$$
\begin{array} { l } { \displaystyle \frac { d \dot { a } _ { 3 } } { d \dot { t } } = \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \cot i \frac { \partial \widehat { \mathfrak { R } _ { 3 } } } { \partial \omega } } \\ { \displaystyle = - \frac { 3 n J _ { 3 } } { 2 a ^ { 3 } } \frac { e } { ( 1 - e ^ { 2 } ) ^ { 3 } } \cos i \left( \frac { 5 } { 4 } \sin ^ { 2 } i - 1 \right) \cos \omega . } \end{array}
$$

To integrate this, we put

$$
\frac { d i _ { 3 } } { d t } = \frac { d \dot { a } _ { 3 } } { d \omega } \frac { d \omega } { d t } = - \frac { 3 n J _ { 2 } } { a ^ { 2 } ( 1 - e ^ { 2 } ) ^ { 2 } } \left( \frac { 5 } { 4 } \sin ^ { 2 } i - 1 \right) \frac { d \dot { a } _ { 3 } } { d \omega } ,
$$

from (11.15.6).Then

$$
d i _ { 3 } = { \frac { J _ { 3 } } { 2 J _ { 2 } } } { \frac { e } { a ( 1 - e ^ { 2 } ) } } \cos i \cos \omega d \omega
$$

and

$$
\begin{array} { c } { { \Delta i _ { 3 } = \displaystyle \int d i _ { 3 } } } \\ { { = \displaystyle \frac { { \bar { \mathcal J } } _ { 3 } } { 2 { \bar { \mathcal J } } _ { 2 } } \displaystyle \frac e { a ( 1 - e ^ { 2 } ) } \cos i \sin \omega . } } \end{array}
$$

It is from perturbations of this kind,and notably from a long-period perturbationin the eccentricity,that ${ \pmb J } _ { 3 }$ has been found.

The division of the right-hand sides of the planetary equations by $\sin ^ { 3 } i \cos ^ { 2 } j \frac { 5 } { 6 } t$ when finding long-period perturbations has two important consequences. If we consider only the second harmonic in the disturbing function and form the equations for the second-order solution, (11.11.8), then the right-hand sides contain the factor J2.But a division by du/dt will leave only J2.Therefore some of the long-period perturbations of order J2 come from the second-order solution of the planetary equations.In addition the factor $\left( \frac { 5 } { 4 } \sin ^ { 2 } i - 1 \right)$ may be left in the denominators of some perturbations,which means that the results arenot valid for i= sin-1(2/√5),and are not reliable for inclinations close to this critical value.

# 11.16 The Computation of the Variations of the Elements

Equations of the form (11.5.13) can be integrated numerically. The amount of computation required for the “function” evaluations is considerable,and ：

Runge-Kutta methods should be avoided. It is arguable that the equations for the variation of the elements are valuable for theoretical, but not numerical, work. There is great interest in following how the elements may change in a perturbed orbit, because we gain a geometrical feeling for what is happening. But you can integrate the equations of motion in their cartesian form, and at any step calculate the osculating elements from the components of position and velocity.

There are many alternative procedures for the computation of the variation of the elements. Details of five (including worked examples) are given in Planetary Coordinates (Ref. 48),and Herget (Ref. 24) gives a numerical example. Here we shall discuss only the general problem of determining the perturbation in the mean anomaly. From the definition

$$
M = M _ { 0 } + n ( t - t _ { 0 } ) ,
$$

where $I ^ { \sqrt { 2 } } t$ the value of the mean anomaly at time $\$ 0$ ,is itself a function of the time.At time $t + d t$ ， $M$ has been increased by $d \pmb { \mathbb { M } }$ ,where

$$
d M = d M _ { 0 } + d n ( t - t _ { 0 } ) + n d t .
$$

Let $\pmb { n }$ have the value $\mathfrak { N } _ { \widehat { \mathfrak { V } } }$ at $\ddagger _ { 0 }$ ; then at time $\ddagger$ ，

$$
\begin{array} { l } { { \displaystyle { \boldsymbol { \pi } } = n _ { 0 } + \Delta n } } \\ { { \displaystyle \quad = n _ { 0 } + \int _ { t _ { 0 } } ^ { t } \frac { d n } { d t } d t } . } \end{array}
$$

Hence

$$
\frac { d M } { d t } = \frac { d M _ { 0 } } { d t } + ( t - t _ { 0 } ) \frac { d x } { d t } + n _ { 0 } + \int _ { t _ { 0 } } ^ { t } \frac { d n } { d t } d t .
$$

Multiplying through by $d _ { t } ^ { \dagger }$ and integrating between $\ddagger _ { \mathfrak { Q } }$ and $\ddagger$ we find

$$
\Delta M = \Delta M _ { 0 } + n _ { 0 } ( t - t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } ( t - t _ { 0 } ) \frac { d n _ { e } } { d t } d t + \int _ { t _ { 0 } } ^ { t } \int \frac { d n } { d t } d t ^ { 2 } ,
$$

where

$$
\Delta M = \int _ { t _ { 0 } } ^ { t } \frac { d M } { d t } d t
$$

and

$$
\Delta \bar { M } _ { \bar { 0 } } = \int _ { t _ { 0 } } ^ { t } \frac { \bar { d } \bar { M } _ { \bar { 0 } } } { \bar { d t } } \ : d t .
$$

The value of $\mathbb { M }$ at any instant is $M _ { \widehat { \Omega } \widehat { \mathbb { G } } } + \Delta \widehat { \mathbb { M } }$ where $\mathbb { M } _ { \tt G Q }$ is the value of $\mathbb { A } _ { \mathfrak { G } }$ at $t _ { 0 }$

Now suppose that by assuming $\mathfrak { P }$ to be constant in the differential equations; we find a perturbation $d ^ { 2 }$ ; then

$$
d \bar { \mathcal { M } } _ { 1 2 1 } = d \bar { M } \div n d \bar { t } , ~ .
$$

S0

$$
d M _ { 0 1 } + n d t = d \vec { x } \mathcal { M } _ { 0 } + n d \vec { x } + d n ( \vec { t } - \vec { \tau } _ { 0 } ) .
$$

Then

$$
\begin{array} { l } { \displaystyle \Delta \mathcal { M } _ { 0 1 } = \int _ { i _ { 0 } } ^ { t } \frac { d M _ { 0 1 } } { d t ^ { i } } d t } \\ { \displaystyle = \Delta M _ { 0 } + \int _ { i _ { 0 } } ^ { t } ( t - t _ { 0 } ) \frac { d n } { d t ^ { i } } d t . } \end{array}
$$

Hence we have, from (11.16.4),

$$
\hat { M } = \hat { M } _ { 0 0 } + \Delta \hat { M } _ { 0 1 } + n _ { 0 } ( t - t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } \int \frac { d n } { d t } d t ^ { 2 } .
$$

This is the expression normally used. An alternative form, due to Laplace, which avoids the double integration, can be derived as follows: integrating by parts,we have

$$
\int _ { t _ { 0 } } ^ { t } ( t - { t _ { 0 } } ) { \frac { d n } { d t } } d t = ( t - { t _ { 0 } } ) \int _ { t _ { 0 } } ^ { t } { \frac { d n } { d t } } d t - \int _ { t _ { 0 } } ^ { t } \int { \frac { d n } { d t } } d t ^ { 2 } .
$$

Accordingly, (11.16.4) becomes

$$
\Delta M = \Delta M _ { 0 } + n _ { 0 } ( t - t _ { 0 } ) + ( t - t _ { 0 } ) \int _ { t _ { 0 } } ^ { t } \frac { d n } { d t } d t ,
$$

an equation that can also be deduced from first principles.

Watson (Ref.31, pp. 530-532) compares these formulas in a numerical example,obtaining results that differ appreciably. He attributes this difference to the factor (t-to） of the integral in (11.16.7),and reasons that the formula (11.16.6) is to be preferred.However,Herrick (Ref.61) has recently shown that the difference is apparently due toa numerical error on the part of Watson,and that the two formulas are equally accurate.

In this work it is usual to treat the time as the independent variable. In a recent modification (Ref.62) Merton uses the mean anomaly as the independent variable; he points out that inaccurate values for the mean motion have led to unsatisfactory results in the former method,but that this weakness can be overcome by making the time one of the perturbed elements,and the mean anomaly, the independent variable. The modifications to the differential equationsare straightforward;each is multiplied by dt/dM.The perturbation in the time can be derived as follows:differentiating (11.16.1) with respect to M, we find

$$
1 = \frac { d M _ { 0 } } { d M } + ( t - \dot { \varepsilon } _ { 0 } ) \frac { d \pi } { d \tilde { M } } + \pi \frac { d \dot { \varepsilon } } { d \tilde { M } } ,
$$

or,from (11.16.5）

$$
\therefore \frac { d \vec { x } } { d \vec { y } } + n \frac { d \vec { z } } { d \vec { z } \vec { z } } .
$$

Hence

$$
\frac { d \vec { t } } { d \mathcal { M } } = \frac { 1 } { n } \left( \mathbb { i } - \frac { d M _ { \mathrm { 0 i } } } { d \mathcal { M } } \right)
$$

and

$$
\begin{array} { r } { \vec { \tau } = \vec { \tau } _ { 0 } \div \displaystyle \int _ { \mathbb { M } _ { 0 } } ^ { \mathbb { M } } \frac { \vec { d } \vec { \tau } } { d \vec { M } } \vec { d } \vec { M } . } \end{array}
$$

A complete description of this method and $\mathbf { a }$ list of formulas for computation will be found in the original paper and in Planetary Coordinates (Ref.48).

In another important modification (Ref. 59) Herrick introduces the parameters

$$
\begin{array} { r l } & { a _ { x } = e P _ { x } , \quad a _ { y } = e P _ { y } , \quad a _ { z } = e P _ { z } , } \\ & { b _ { x } = e \sqrt { p } Q _ { x } , \quad b _ { y } = e \sqrt { p } Q _ { y } , \quad b _ { z } = e \sqrt { p } Q _ { z } , } \\ & { \quad u = r \dot { r } , } \\ & { w = r - p . } \end{array}
$$

The perturbations are found in rectangular coordinates,and these are related to those in $\mathcal { U }$ and $\mathfrak { W }$ and hence to the $a$ 'sand b'sand to perturbations in M and $\pmb { \mathcal { I } }$ The relevant formulas and $\mathtt { a }$ specimen calculation are given in Planetary Coordinates.

# 11.17 The Activity Sphere

If a comet passes very closely to a perturbing body such as Jupiter, the perturbing force may become so great that inconveniently small time intervals have to be used between steps in the computation of the perturbations. In this case it may be easier to consider the comet as moving in an orbit about Jupiter, perturbed by the Sun from the motion required by the inverse square law (hyperbolic in this case). This contingency is remote in astronomy, but in astronautics the close approach to a planet may very well be the prime purpose of a mission.

We shall discuss the situation in the following way: a rocket $\mathcal { R }$ of negligible mass approaches close to a planet $\mathcal { P }$ of mass $\mathcal { W }$ Both rocket and planet are subject to the Newtonian field of the Sun $s$ of mass $\tilde { \it 1 4 }$ Let

$$
\begin{array} { r } { \cdot \mathrm { ~  ~ \mathcal ~ { ~ S ~ R ~ } ~ } = { \bf r } , \quad { \bf S } { \bf P } = { \bf r } _ { \perp } , \quad \mathrm { a n d } \quad { \bf P } { \bf R } = \rho . } \end{array}
$$

Then

$$
{ \mathfrak { x } } = { \mathfrak { x } } _ { \mathtt { i } } + { \mathfrak { P } } .
$$

Treating the planet as the perturbing body, we have

$$
\ddot { \bar { x } } + \bar { M } \bar { k } ^ { 2 } \frac { \bar { x } } { \bar { x } ^ { 3 } } = \eta k \bar { k } ^ { 2 } \left( - \frac { \rho } { \rho ^ { 3 } } - \frac { \bar { x } _ { 1 } } { \bar { x } _ { 1 } ^ { 3 } } \right)
$$

$$
\ddot { \pmb { \tau } } + \pmb { \Sigma } _ { 1 } = \pmb { \nu } _ { 1 } ^ { \prime } ,
$$

say，where $\mathbb { E } ^ { \ell } { } _ { \mathfrak { I } }$ is.the perturbing force.

Treating the Sun as the perturbing body， we have

$$
{ \ddot { \rho } } \div \pi { \dot { k } } ^ { 2 } { \frac { \rho } { \rho ^ { 3 } } } = M { \dot { k } } ^ { 2 } \left( - { \frac { \mathtt { F } } { r ^ { 3 } } } + { \frac { { \mathtt { r } } _ { \mathtt { l } } } { r _ { \mathtt { i } } ^ { 3 } } } \right)
$$

or

$$
\ddot { \pmb { \rho } } + \pmb { \Sigma } _ { 2 } = \pmb { \mathbb { F } } _ { 2 } ^ { \prime } .
$$

At great distances from $\mathcal { P }$ (11.17.1) is obviously superior to (11.17.3). But as the rocket approaches $P , \mathcal { E } _ { \widehat { \lambda } } ^ { \widehat { \prime } }$ becomes larger and ${ \vec { \pmb { \mathscr { F } } } } _ { 2 } ^ { \prime }$ diminishes;if we reach a stage when the ratio $\widehat { \pmb { f } } _ { 1 } ^ { \prime } : \widehat { \pmb { f } } _ { 1 } ^ { \prime }$ is greater than $\mathbb { F } _ { 2 } ^ { \prime } : \mathbb { F } _ { 2 }$ ,then (11.17.1) loses its advantage over (11.17.3).Hence, for

$$
\frac { \overline { { \xi _ { 1 } } } } { \overline { { \xi _ { 2 } } } } > \frac { \overline { { \xi _ { 1 } ^ { j } } } } { \overline { { \xi _ { 2 } ^ { j } } } }
$$

we use (11.17.1), and for

$$
\frac { \vec { \mathcal { F } } _ { \perp } ^ { \prime } } { \vec { \mathcal { F } } _ { 2 } } < \frac { \vec { \mathcal { F } } _ { 1 } ^ { \prime } } { \vec { \mathcal { F } } _ { 2 } ^ { \prime } }
$$

we use (11.17.3).

The limit

$$
\frac { \bar { \varepsilon } _ { \mathrm { 1 } } ^ { \prime } } { \bar { \varepsilon } _ { \mathrm { 2 } } } = \frac { \bar { F } _ { \mathrm { 1 } } ^ { \prime } } { \bar { F } _ { \mathrm { 2 } } ^ { \prime } }
$$

can be shown to define, very nearly, a locus that is a sphere of radius

$$
r _ { \mathrm { a c t } } = r _ { \mathrm { 1 } } \left( { \frac { \hbar \lambda } { \hbar } } \right) ^ { 2 / 5 } .
$$

This is known as the activity sphere of the planet.

# 11.18 General Methods

The word “perturbation” normally has a much more general meaning than that applied here (i.e., the deviation from Keplerian motion).For instance, when considering the stability of the positions of equilibrium in the restricted three-body problem,we considered perturbations of the motion about these positions.In this section we shall consider, only very generally,some other examples of perturbed equations; these examples arise in the following two problems:

1. Let x represent the vector with components $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \}$ , and suppose that the solution to the $\mathfrak { P e }$ equations

$$
\pmb { \dot { x } _ { i } } = f _ { i } ( \mathbf { x } , t ) \quad i = \mathbb { i } , 2 , \ldots , n
$$

is known for the initial conditions x=at t= to.How can this solution be used to find the solution for the slightly different initial conditions x=x+att=to？

2. How can the solution to (11.18:1) be used to solve the equations

$$
\dot { x } _ { i } = f _ { i } ( \mathbf { x } , \pmb { \underline { { t } } } ) + g _ { i } ( \mathbf { x } , \pmb { \underline { { t } } } ) ,
$$

where, over an appropriate range of time,lfl> lgl?

Consider problem (1). For economy of space we shall work with only two unknowns, xi and x2； the generalization for n unknowns is straightforward. The equations to be solved are

$$
{ \dot { x } } _ { 1 } = f _ { 1 } ( x _ { 1 } , x _ { 2 } , t ) \quad { \mathrm { a n d } } \quad { \dot { x } } _ { 2 } = f _ { 2 } ( x _ { 1 } , x _ { 2 } , t ) .
$$

The solution with the initial conditions

$$
x _ { 1 } = \hat { x } _ { 1 } \quad \mathrm { a n d } \quad x _ { 2 } = \hat { x } _ { 2 } \quad \mathrm { a t ~ } \hat { t } = \hat { t } _ { 0 }
$$

is known to be, say,

$$
x _ { 1 } = x _ { 1 } ( t ) \quad \mathrm { a a d } \quad x _ { 2 } = x _ { 2 } ( t ) .
$$

We require the solution

$$
x _ { 1 } = x _ { 1 } ( t ) + \delta x _ { 1 } ( t ) \quad \mathrm { a n d } \quad x _ { 2 } = x _ { 2 } ( t ) + \delta x _ { 2 } ( t )
$$

which has the initial conditions

$$
x _ { 1 } = \mathring { x } _ { 1 } + \delta \mathring { x } _ { 1 } \quad \mathrm { a n d } \quad x _ { 2 } = \mathring { x } _ { 2 } + \delta \mathring { x } _ { 2 } \quad \mathrm { a t \ } t = \dot { t } _ { 0 } .
$$

As long as the differences remain small, we can expand each side of the equations (11.18.3) in Taylor series; neglecting (δx)²,the equation for x1 becomes

$$
\dot { x } _ { 1 } + \delta \dot { x } _ { 1 } = f _ { 1 } \big ( x _ { 1 } , x _ { 2 } , t \big ) + \frac { \partial \frac { f _ { 1 } } { f _ { 1 } } } { \partial x _ { 1 } } \delta x _ { 1 } + \frac { \partial \frac { f _ { 1 } } { f _ { 1 } } } { \partial x _ { 2 } } \delta x _ { 2 } ,
$$

where

$$
\delta \dot { x } _ { \bar { 1 } } = \frac { \dot { a } } { \dot { a } _ { \bar { 2 } } ^ { \bar { 2 } } } \big ( \delta x _ { \bar { 1 } } \big ) .
$$

Remembering that x1(t） and x2(t) satisfy the differential equations, we find

and

$$
\begin{array} { l } { \displaystyle { \delta \dot { x } _ { 1 } = \frac { \partial f _ { 1 } } { \partial x _ { 1 } } \delta x _ { 1 } + \frac { \partial f _ { 1 } } { \partial x _ { 2 } } \delta x _ { 2 } \mathrm { , } } } \\ { \displaystyle { } } \\ { \displaystyle { \delta \dot { x } _ { 2 } = \frac { \partial f _ { 2 } } { \partial x _ { 1 } } \delta x _ { 1 } + \frac { \partial f _ { 2 } } { \partial x _ { 2 } } \delta x _ { 2 } \mathrm { . } } } \\ { \displaystyle { ~ \qquad \quad \cdot \frac { \dot { x } _ { 3 } \dot { x } _ { 2 } } { \dot { x } _ { 3 } \dot { x } _ { 3 } } \mathrm { . } } } \end{array}
$$

These equations are the first variation of the given system. The quantities dfi/dxj are evaluated from the solution (11.18.4). These equations can be solved numerically for any given set of initial conditions,but an important modification enables the solution to be found once and for all for any set of initial conditions.

Since we are dealing with differentials, we have

$$
\begin{array} { r } { \Big [ \delta x _ { 1 } ( t ) \Big ] = \left[ \begin{array} { l } { \displaystyle \frac { \partial x _ { 1 } ( t ) } { \partial x _ { 1 } ( t _ { 0 } ) } \frac { \partial x _ { 1 } ( t ) } { \partial x _ { 2 } ( t _ { 0 } ) } \Bigg ] } \\ { \displaystyle \frac { \partial x _ { 2 } ( t ) } { \partial x _ { 1 } ( t _ { 0 } ) } \frac { \partial x _ { 2 } ( t ) } { \partial x _ { 2 } ( t _ { 0 } ) } \Bigg ] } \end{array} \right[ \delta x _ { 2 } ( t _ { 0 } ) \Big ] . } \end{array}
$$

The square matrix in (11.18.6) is a Jacobian matrix that can be written in condensed notation as

$$
\tilde { \mathbf { \mathbf { \rho } } } = \frac { \partial \mathbf { x } ( t ) } { \partial \mathbf { x } ( t _ { 0 } ) } .
$$

Our object is to find J so that any initial conditions can be applied without further calculation.

Suppose that equations (11.18.5) are solved with initial conditions

$$
 [ \begin{array} { l } { \delta x _ { 1 } ( t _ { 0 } ) } \\ { \delta x _ { 2 } ( t _ { 0 } ) } \end{array} ] = [ \begin{array} { l } { 1 } \\ { 0 } \end{array} ] .
$$

(These are homogeneous, so there is no limitation on the magnitude of the dependent variables.）Then the resulting solution will provide the first column ofJ.Similarly,with initial conditions

$$
\left[ \begin{array} { l } { \delta x _ { 1 } ( t _ { 0 } ) } \\ { \delta x _ { 2 } ( t _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right]
$$

the second column of $\Im$ will be generated.

This can be generalized. Starting with (11.18.1),the first variational equations can be written as

$$
\begin{array} { r } { \delta \dot { \mathbf { x } } = \mathbb { A } \delta \mathbf { x } , } \end{array}
$$

where the matrix A has typical component dfi/dxj. The separate columns of J themselves satisfy this equation, so $\mathbb { J }$ itself will satisfy

$$
\dot { \bar { \mathbf { z } } } = \mathbb { A } \bar { \mathbf { \mathcal { \mathbf { J } } } } .
$$

This is solved with initial condition of ${ \mathfrak { J } } = { \mathfrak { J } } .$ the $\mathfrak { x }$ -by $\curvearrowleft$ identity matrix.

J found in this way relates small changes in the quantities xi at an initial time, to resulting small changes at a later time. Then J is often referred to as the matrizant for the system (11.18.1),and written Ω(t,to).Then

$$
\begin{array} { r l } { { \mathfrak { s } } _ { : } } & { { } \quad : : \cdot \langle \delta \mathbf { \dot { x } } ( t ) = \Omega ( t , t _ { 0 } ) \delta \mathbf { x } ( t _ { 0 } ) . } \\ { { \mathfrak { s } } _ { : } } & { { } \quad : \cdot \langle \mathbf { \dot { x } } ( t _ { 0 } ) , } \\ { { \mathfrak { s } } _ { : } } & { { } \quad : \cdot \langle \mathbf { \dot { x } } ( t _ { 0 } ) , } \end{array}
$$

(Other names abound, such as “state transition matrix.") Since

$$
\delta \mathbf { x } ( \vec { \imath } _ { 2 } ) = \Omega ( \vec { \imath } _ { 2 } , \vec { \imath } _ { 0 } ) \delta \mathbf { x } ( \vec { \imath } _ { 0 } )
$$

and

$$
\delta { \mathbf { x } } ( t _ { 2 } ) = \Omega ( t _ { 2 } , t _ { 1 } ) \delta { \mathbf { x } } ( t _ { 1 } ) = \Omega ( t _ { 2 } , t _ { 1 } ) \Omega ( t _ { 1 } , t _ { 0 } ) \delta { \mathbf { x } } ( t _ { 0 } ) ,
$$

it follows that

$$
\Omega ( { t _ { 2 } } , { t _ { 0 } } ) = \Omega ( { t _ { 2 } } , { t _ { 1 } } ) \Omega ( { t _ { 1 } } , { t _ { 0 } } ) .
$$

(This also follows directly from the chain rule, for Ω is a Jacobian matrix.） Also.

$$
\mathfrak { Q } ^ { - 1 } ( \mathfrak { t } _ { 1 } , \mathfrak { t } _ { 2 } ) = \Omega ( \mathfrak { t } _ { 2 } , \mathfrak { t } _ { 1 } ) .
$$

Ω is useful in many orbital applications; analyzing the effects of errors, for instance, or in mid-course guidance. It, and other Jacobian matrices were considered in Section 7.5,where they were derived by the method of “tweaks." The iumerical solution of the variational equations,repeated n times to build up the n columns of the matrizant,is more extravagant, but it does produce the true partial derivatives. Suppose that the solution started at time to, and it is desired to compare small changes between times t1 and t2. Then we need

$$
\begin{array} { c } { { \Omega ( t _ { 2 } , t _ { 1 } ) = \Omega ( t _ { 2 } , t _ { 0 } ) \Omega ( t _ { 0 } , t _ { 1 } ) } } \\ { { = \Omega ( t _ { 2 } , t _ { 0 } ) \Omega ^ { - 1 } ( t _ { 1 } , t _ { 0 } ) . } } \end{array}
$$

The inversion can be avoided by solving a set of differential equations for the inverse matrix. Let

$$
\begin{array} { r } { \mathfrak { T } ( t , t _ { 0 } ) = \Omega ^ { - 1 } ( t , t _ { 0 } ) , \quad \mathrm { s o } \quad \mathfrak { T } ( t , t _ { 0 } ) \Omega ( t , t _ { 0 } ) = \mathfrak { I } . } \end{array}
$$

Differentiating,and using the fact that Ω= AΩ, we find

$$
\dot { \overline { { \mathfrak { T } } } } = - \mathfrak { T } \mathbb { A } .
$$

These are called the adjoint equations for the system. They have been applied in many contexts from numerical analysis to ballistics.

To illustrate setting up the variational equations,let us start with dynamical equations

$$
\ddot { z } = X , \quad \ddot { y } = Y , \quad \ddot { z } = Z ,
$$

where the forces, X,Y, Z may depend on position, velocity and time. Defne

$$
x _ { 1 } = x , \ x _ { 2 } = y , \ x _ { 3 } = z , \ x _ { 4 } = \dot { x } , \ x _ { 5 } = \dot { y } , \ x _ { 6 } = \dot { z } .
$$

Equations (11.18.15) can now be written as the system

$$
\begin{array} { r } { \frac { d } { d t } \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \\ { x _ { 5 } } \\ { x _ { 6 } } \end{array} \right] = \left[ \begin{array} { c } { f _ { 1 } } \\ { f _ { 2 } } \\ { f _ { 3 } } \\ { f _ { 4 } } \\ { f _ { 5 } } \\ { f _ { 6 } } \end{array} \right] = \left[ \begin{array} { c } { x _ { 4 } } \\ { x _ { 5 } } \\ { x _ { 6 } } \\ { X ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , x _ { 5 } , x _ { 6 } , t ) } \\ { Y ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , x _ { 5 } , x _ { 6 } , t ) } \\ { Z ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , x _ { 5 } , x _ { 6 } , t ) } \end{array} \right] . } \end{array}
$$

Using subscripts to denote partial derivatives, the variational equations are

$$
\begin{array} { r } { \frac { d } { d t } \left[ \begin{array} { l } { \delta x _ { 1 } } \\ { \delta x _ { 2 } } \\ { \delta x _ { 3 } } \\ { \delta x _ { 4 } } \\ { \delta x _ { 5 } } \\ { \delta x _ { 6 } } \end{array} \right] = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { X _ { 1 } } & { X _ { 2 } } & { X _ { 3 } } & { X _ { 4 } } & { X _ { 5 } } & { X _ { 6 } } \\ { Y _ { 1 } } & { Y _ { 2 } } & { Y _ { 3 } } & { Y _ { 4 } } & { Y _ { 5 } } & { Y _ { 6 } } \\ { Z _ { 1 } } & { Z _ { 2 } } & { Z _ { 3 } } & { Z _ { 4 } } & { Z _ { 5 } } & { Z _ { 6 } } \end{array} \right] \left[ \begin{array} { l } { \delta x _ { 1 } } \\ { \delta x _ { 2 } } \\ { \delta x _ { 3 } } \\ { \delta x _ { 4 } } \\ { \delta x _ { 5 } } \\ { \delta x _ { 6 } } \end{array} \right] . } \end{array}
$$

Now consider problem (2). If $\mathbf { x }$ is the solution of (11.18.1), and $\mathbf { x } + \delta \mathbf { x }$ the solution of (11.18.2), then as long as $\left. \delta \mathbf { x } \right.$ remains small, we find

$$
\delta \dot { x } _ { i } = \sum _ { j = 1 } ^ { n } \frac { \partial f _ { i } } { \partial x _ { j } } \delta x _ { j } + g _ { i } ( \mathbf { x } , t ) .
$$

As before, the quantities $\partial f _ { i } / \partial x _ { j }$ are evaluated from the solution of (11.18.1), and,to this order of accuracy, this solution may also be used in the evaluation of the $\widehat { g } _ { \widehat { z } }$ The equations (11.18.19) can be written in the form

$$
\delta \dot { \mathbf { x } } = \mathbb { A } \delta \mathbf { x } \div \mathbf { \vec { y } } ( \vec { \tau } ) .
$$

The homogeneous part has solution

$$
\delta \mathbf { x } ( t ) = \Omega ( t , t _ { 0 } ) \mathbb { c }
$$

for arbitrary constant c. For the fullequation we use variation of parameters, so with variable $\pmb { \mathfrak { c } }$ ：

$$
\delta \dot { \mathbf x } = \dot { \Omega } c + \Omega \dot { \mathbf c } = \mathbf A \Omega \boldsymbol c + \Omega \dot { \boldsymbol c } .
$$

Substituting into (11.18.20),

$$
A B C + B C = A B C + B ,
$$

so that

$$
c = \int \limits _ { 0 } ^ { \infty } \{ g ^ { - 1 } b d t .
$$

Substituting into (11.18.21),we find the detailed solution

$$
\delta { \bf x } ( t ) = \Omega ( t , t _ { 0 } ) \delta { \bf x } ( t _ { 0 } ) + \Omega ( t , t _ { 0 } ) \int _ { t _ { 0 } } ^ { t } \Omega ^ { - 1 } ( \tau , t _ { 0 } ) { \bf b } ( \tau ) d \tau .
$$

Other forms are

$$
\delta { \bf x } ( t ) = \Omega ( t , \dot { \tau } _ { 0 } ) \delta { \bf x } ( t _ { 0 } ) \div \int _ { t _ { 0 } } ^ { t } \Omega ( t , \tau ) \mathrm { b } ( \tau ) d \tau ,
$$

and

$$
\delta { \bf x } ( t ) = \Omega ( t , t _ { 0 } ) \delta { \bf x } ( t _ { 0 } ) + \Omega ( t , s ) \int _ { t _ { 0 } } ^ { t } \Omega ( s , \tau ) { \bf b } ( \tau ) d \tau ,
$$

where s is arbitrary and may be chosen out of convenience. If the particular solution (i.e., the second term) is required numericaly, then (11.18.20) should he solved numerically，with all the initial components of Sx(to) equal to zero.

We shall finish by discussing very briefly two important approaches to problem (2). The first is that of Lagrange.

Let equation (11.18.1) have the general solution

$$
x _ { i } = X _ { i } [ c _ { 1 } , c _ { 2 } , \cdots , c _ { n } , t ] \equiv X _ { i } [ \underline { { \mathrm { c } } } , t ] ,
$$

where the c's are the arbitrary constants of integration. Let this solution be substituted into (11.18.2),where now the c's become functions of the time. We have'

$$
x _ { i } = X _ { i } \{ \mathbf { c } \{ t \} , t \} \}
$$

and

$$
\dot { x } _ { \mathrm { i } } = \frac { \partial X _ { i } } { \partial \dddot { t } } + \sum _ { j = 1 } ^ { n } \frac { \partial X _ { i } } { \partial c _ { j } } \dot { c } _ { j } .
$$

Equating this to

$$
f _ { i } \{ { \bf x } , t \} + g _ { i } \{ { \bf x } , t \} ,
$$

and applying (11.18.1),we find

$$
\sum _ { j = 1 } ^ { n } \frac { \partial X _ { i } } { \partial c _ { j } } \dot { c } _ { j } = g _ { i } \{ { \bf x } , t \} .
$$

This is the method of the “variation of arbitrary constants.”

Another approach,due to Poisson,assumes that the equations (1 have been solved by finding the $\mathfrak { X }$ integrals

$$
a _ { i } \{ { \bf x } , \dot { \imath } \} = c _ { i } .
$$

If these are solved for the $\boldsymbol { \mathfrak { X } } _ { i }$ ,we find,as before

$$
x _ { i } = X _ { i } [ \mathbb { C } , \boldsymbol { \sharp } ]
$$

and the conditions for this are the identities

$$
a _ { i } \{ \mathbf { X } [ \mathbb { C } , { i } ] , t \} \equiv c _ { i } .
$$

As before,this solution is substituted into equation (11.18.2)，where the c's are now functions of the time. Differentiating the identities (1i.18.28) with respect to $\ddagger$ we find

$$
\frac { d } { d t } c _ { i } ( t ) = \frac { \partial } { \partial t } a _ { i } ( { \bf X } \{ { \bf c } ( t ) \} , \dot { t } ) + \sum _ { j = 1 } ^ { n } \frac { \partial } { \partial x _ { j } } a _ { i } ( { \bf X } \{ { \bf c } ( t ) \} , t ) \frac { d x _ { j } } { d t } .
$$

But $\mathbf { x }$ is now to satisfy (11.18.2); so,

$$
\frac { d } { d t } c _ { i } ( t ) = \frac { \partial } { \partial t } a _ { i } \big ( { \bf X } [ { \bf c } ( t ) ] , t ) + \sum _ { j = 1 } ^ { n } \frac { \partial } { \partial x _ { j } } a _ { i } \big ( { \bf X } [ { \bf c } ( t ) ] , t \big ) \{ f _ { j } ( { \bf x } , t ) + g _ { j } ( { \bf x } , t ) \} .
$$

Now,in the solution to (11.18.1),the c's are constants, and

$$
0 = \frac { \partial } { \partial t } a _ { i } ( { \bf X } [ { \bf c } ( t ) ] , t ) + \sum _ { j = 1 } ^ { n } \frac { \partial } { \partial x _ { j } } a _ { i } ( { \bf X } [ { \bf c } ( t ) ] , t ) f _ { j } ( { \bf x } , t ) .
$$

This is true for arbitrary c, so it will be true for c(t). Hence we can substitute $\mathfrak { c } ( \ddagger )$ for $\mathbf { c }$ in (11.18.18) and subtract the result from (11.18.28), leaving

$$
\frac { d } { d \dot { t } } c _ { i } ( \dot { t } ) = \sum _ { j = 1 } ^ { n } \frac { \partial a _ { i } } { \partial x _ { j } } g _ { j } ,
$$

where the terms on the right-hand side are evaluated by using the solutions (11.18.27). This form is similar to that of equations (11.9.9).

The equations (11.18.31) and (11.18.25) are clearly related. Full details of the relations between them,and of the applications of these methods in celestial mechanics,are given in the texts by Smart and Plummer (Refs. 29 and 26).

# 11.19 Problems

1. Find the periodic perturbations in α for the case of eliptic motion perturbed by a resisting force $c ^ { \gamma } / { \tau ^ { 2 } }$

2.Consider the modification due to the theory of relativity produced in the equation of the orbit in an inverse square feld. (See Section 4.5.) Use the methods of Section 11.1 to interpret the solution,considering the variations from Keplerian motion as perturbations. Hence find the resulting secular and periodic perturbations in the elements.

3. Justify the series (11.3.6).

4.Assuming that Jupiter remains fixed during one complete revolution of Mars,find,by dividing the orbit of Mars into ten sections,and using the methods of Section 11.4, the perturbations in the coordinates of Mars for the cases when the line of apsides points toward Jupiter and perihelion is (a) pointing toward Jupiter and (b) pointing away from Jupiter, and (c) when the line of apsides is at right angles to the line joining the Sun and Jupiter.

5.Investigate by the methods of Section 11.4 the perturbations in the coordinates of each planet taken separately, which are inflicted by each of the other planets taken separately.

28.Find the amplitude of the short-term oscillations ofi for 1957 β1, given that $w = \frac { 4 } { 2 } 2 . 8 ^ { \circ }$

29. Show that the third harmonic in the Earth's field gives rise to no secular perturbations.

30.Find the secular perturbations produced by the fourth harmonic in the Earth's field.

31. Find the long-period perturbation in the eccentricity of a satellite in the Earth's field which is of order J/J2. If the ratio is 2.5 ×10-3,consider the possibility of observing the efect of this perturbation on the perigee distance.

32.Consider the application of the formulas of Section 11.10 to satellite orbits with small $e$ ori.

33.The line of apsides of the fth satelite of Jupiter (181,500 km from the center of Jupiter; assume its orbit to be equatorial and nearly circular) advances through 9Oo° per year. Supposing Jupiter to be a spheroid composed of homogeneous incompressible fluid,of density 1.34 and total mass 1/1047 solar masses;find the shape of Jupiter which would account for this apsidal motion,and also find the uniform angular velocity which would account for this shape. Discuss your answer in relation to the actual figures for Jupiter.

34.That part of the motion of Mercury's line of apsides left unexplained by Newton's law of gravitation amounts to 43" per century. Assume that this is caused by the oblateness of the Sun, and that this oblateness is the result of the rotation of an incompressible fluid mass of density 1.41. Find the oblateness and the angular velocity of rotation. Comment on thefeasibility of the actual rotation of the Sun providing an appreciable portion of this $4 3 ^ { 3 9 }$ ，

35.Two equal stars of mass M, composed of homogeneous incompressible fuid of density p, revolve around each other in nearly circular orbits; the axis of rotation of each is perpendicular to the orbital plane, and the angular velocity of rotation of each is equal to the mean motion in the orbit.The distortion of the stars may be considered only to the first-order of small quantities, but should include both tidal and rotational effects. Assuming that the fuid is not viscous,find the perturbations.

36.Let the stars in problem 35 suddenly become solid; how will the perturbations be affected?

37.Consider qualitatively the perturbations of problem 35 when the fluid is viscous.

38.Suppose the orbit of a comet passes near Jupiter's orbit at one of its nodes;under what conditions will the inclination of the comet's orbit be decreased? Show that if the major axis remains constant while the inclination is decreased,then the eccentricity is increased.

39.Investigate qualitatively the effect of the gradual accretion of meteoric matter bya planet on the major axis of its orbit.

40.A planet is perturbed by the action of another planet more distant from the Sun. Assuming that both move in circular orbits in the same plane, describe the perturbations that would be observed from a third planet, the orbit of which lies within the other two. Show how the perturbing force could be deduced from these observations,and that,if the distance of the outer planet is assumed, then its direction and mass can be found. (Thisisa highly oversimplified introduction to the theory involved in the discovery of Neptune,when the deviations of Uranus from a Keplerian orbit were used by Leverrier and Adams to predict where a new planet was to be found,in addition to its orbit and mass.They assumed the distance of Neptune to be given by Bode's law.)

41.Consider qualitatively the perturbations that would be produced on the orbits of the planets in the solar system if the entire system were to pass through an interstellar cloud ofuniform density with relative velocity (a) in the plane of the ecliptic and (b)at right angles to the plane of the ecliptic.Could perturbations of this kind,over a very long-period,help to account for some of the regularities of the solar system, or would they tend to destroy them?

42.Consider qualitatively the perturbations that would be produced on the orbits of the planets in the solar system by a distant passing star,where the star moves (a） in the ecliptic and (b)at right angles to the ecliptic.What would be the cumulative effects of such encounters, where the directions of motion of the passing stars are oriented at random?

43.Find the perturbations that would be produced on the orbits of the planets as the result of a steady loss of mass by the Sun.

44.Investigate the first-order secular perturbations of the orbit of a satellite revolving around a primary that isin the form of an ellipsoid with three slightly unequal axes. Apply your results to a satellite revolving close to the surface of the Moon.

45.Suppose the perturbations inflicted by Jupiter on a comet's orbit are to beinvestigated by the method of the variation of the elements of the orbit.Consider the problem of expressing,at any time, the coordinates of the comet and of Jupiter with respect to axes,with the $\pmb { \mathscr { x } }$ axis pointing toward perihelion of the osculating orbit,and the $z$ -axis pointing toward h.Write down the components $R , N$ and $\pmb { B }$ in terms of the coordinates defined by these axes.

46.In Section 11.17 let the angle between $\mathcal { P S }$ and $p _ { \mathfrak { R } }$ be $\boldsymbol { S }$ If powers of $( \rho / r )$ greater than the first are neglected,show that

$$
\left| - \frac { r } { r ^ { 3 } } + \frac { r _ { \bar { 1 } } } { r _ { 1 } ^ { 3 } } \right| \simeq r ^ { - 3 } ( \bar { 1 } + 3 \cos ^ { 2 } S ) ^ { 1 / 2 } .
$$

Hence show that on the border of the “activity sphere”

$$
\rho \simeq r ( \pi / M ) ^ { 2 / 5 } ( 1 + 3 \cos ^ { 2 } S ) ^ { - 1 / 1 0 } .
$$

Investigate the differences between this and the approximation given in that section.

47.Find the radii of the activity spheres of all the major planets,and of the Moon (where the Earth and Moon replace the Sun and planet).

48.A body subject to no forces moves in a straight line with uniform speed. The elements of this orbit are the constants defining the position of the line,the speed,the direction of motion in the line,and the position at time T. Show that they can be expressed in terms of six independent constants,and that it is permissible in the problem of two bodies to regard one body as always movingwith respect to the other in a straight line whose position continually changes. Find the expressions for these line elements in terms of the time in the case of elliptic motion.

49.Show from general considerations based on problem 48 that the methods of the variation of coordinates and the variation of arbitrary constants are essentially the same,differing only in the variables used in defining the coordinates and velocities of the bodies.

50. Show that the equation $x = A ( t ) x$ can be solved in the successive approximations

$$
\mathbf { x } _ { \mathrm { i } } = { \hat { \mathbf { x } } } + { \hat { \mathbf { A } } } _ { 1 } { \hat { \mathbf { x } } } , \quad \mathbf { w } _ { \mathrm { i } } ^ { \dagger } \mathrm { e r e } \ { \hat { \mathbf { A } } } _ { 1 } = \int _ { t _ { 0 } } ^ { t } { \mathbf { A } } d t ,
$$

$$
\mathbf { x } _ { 2 } = { \frac { \circ } { \mathbf { x } } } + { \hat { \mathbf { A } } } _ { 1 } { \frac { \circ } { \mathbf { x } } } + { \hat { \mathbf { A } } } _ { 2 } { \frac { \circ } { \mathbf { x } } } , \quad { \mathrm { w h e r e ~ } } { \hat { \mathbf { A } } } _ { 2 } = \int _ { t _ { 0 } } ^ { t } { \hat { \mathbf { A } } } { \hat { \mathbf { A } } } _ { 1 } d t ,
$$

and find an expression for $\mathbf { x } _ { \mathfrak { n } }$

51.Let $\mathbf { x }$ be a matrix with columns consisting of $\mathfrak { P }$ independent solutions of

Show that $x = \tt { A X }$ and that the general solution is $\mathtt { x a }$ where a is an arbitrary vector.

$$
\dot { \mathbf { z } } = \mathbb { A } \{ \pm \} \mathbf { z } .
$$

52. In the notation of the previous two problems, show that

$$
{ \bf X } \{ \{ \pmb { \imath } \} = \sum _ { i = 0 } ^ { \infty } { \bf A } _ { i } \{ \pmb { t } \} ,
$$

assuming suitable convergence.

53. Consider the equation

$$
\begin{array} { r } { \dot { { \bf x } } = { \mathbb { A } } \{ \dot { \bar { \tau } } \} { \bf x } + { \mathbb { B } } \{ \dot { \bar { \tau } } \} . } \end{array}
$$

Show by Lagrange's or Poisson's method of the variation $0 . \frac { 5 } { 2 }$ parameters, or otherwise,that $\hat { \mathbf { \Omega } }$ particular solution is

$$
\mathbf { x } = \mathbb { X } ^ { \widehat { \mathbf { x } } } + \mathbb { X } \int _ { t _ { 0 } } ^ { t } \mathbf { X } ^ { - 1 } \mathbf { \widehat { b } } d t .
$$

Hence find the general solution.

54.Apply the methods discussed in the problems above to the equation

$$
{ \dot { \mathbf { x } } } = \mathbf { x } .
$$

55. Integrate the equation of motion

$$
\ddot { x } = - x + \alpha x ^ { 2 } , \quad | \alpha | \ll \bar { 1 } ,
$$

$\{ \mathfrak { a } \}$ by Lagrange's method of variation of parameters, $( 3 )$ by Poisson's method of variation of parameters, (c) by expansion in powers of $\alpha$ ,a constant.

56. $\dot { \bar { \textbf { x } } } = \textbf { A x }$ and $\dot { \mathbf { y } } = - \mathbf { y } \mathbf { A }$ are adjoint equations, $\mathbf { x }$ and $\mathbf { y }$ being square matrices. Show that $\mathbb { y } \mathbf { x }$ is a constant matrix.

57.If $\dot { \pmb { \Omega } } = \mathbb { A }$ ： $\mathfrak { D }$ is the determinant of $\pmb { \Omega }$ and $\sum \gamma _ { i } ( A )$ is the trace of A (i.e., the sum of the terms in the principal diagonal),then it is the case that $\dot { \mathcal { D } } = \{ \mathcal { T r } ( \mathbb { A } ) \} \mathcal { D }$ See if you can justify this. Use this to show that if the forces in (11.18.14)are independent of the velocities, then the determinant of the matrizant always is equal to one.

58. If the forces in (11.18.4) are the components of the gradient of a scalar function of $\pmb { \mathcal { X } }$ ， $\mathfrak { Y }$ and $z$ ,show that the matrizant is symplectic. (See Section 7.5,problem 1.）

59.Consider Einstein's equation, (4.5.1),written as $z ^ { \prime \prime } + u = \ell + \alpha v ^ { 2 }$ Show that this can be written as two equations: ${ \mathfrak { U } } ^ { \beta } = { \mathfrak { v } }$ ， $v ^ { \prime } = - u + \ell + \alpha v ^ { 2 }$ ,and that the solution with $\alpha = \beta$ can be written as $\boldsymbol { \mathfrak { u } } = \ell \{ ( { \vec { 1 } } + e \cos ( \theta - \omega ) \}$ ： $v = - \ell e \sin ( \theta - \omega )$ with constants $\pmb { \mathcal { e } }$ and $\omega$ If these constants become variable parameters in the complete equation, show that

$$
\begin{array} { r l } { e _ { < } ^ { t } , = } & { { } e _ { < } ^ { t } \mathrm { e s i n } ( \theta - \omega ) \{ 1 + e \cos ( \theta - \omega ) \} _ { < } ^ { 2 } } \\ { , \quad \cdot , : } \end{array} ,
$$

and

$$
e \omega ^ { \prime } = \alpha \ell \cos ( \theta - \omega ) \{ 1 + e \cos ( \theta - \omega ) \} ^ { 2 } .
$$

Solve these to the first-order,and verify the result of section 4.5 for the advance of perihelion.

60.Suppose that we have a radial perturbing force $\mathcal { R } = - \alpha \hbar ^ { 2 } / \uparrow ^ { 4 }$ (with $\mathcal { B } =$ $N = 0$ Write down the radial component of the equation of motion, and use the transformations of section 4.3. Show that Einstein's equation, （4.5.1),results.Now substitute this expression for $\mathcal { R }$ into the equations for the variation of elements. Solve the equations to the first-order,and compare results with those found previously.

61.We shall examine the Poynting-Robertson effect. A small particle moves in the solar system,subject to the gravitational attraction of the Sun and to radiation pressure from the Sun. At frst sight, the radiation pressure would appear to be radial, and proportional to the inverse square of the distance from the Sun,and so could be accounted for just bya diminution in the apparent mass of the Sun. The perturbations to consider are departures from this case. Firstly,because of the aberration of light,the particle will “see” the Sun as displaced forward in the direction of motion; this leads to a transverse drag component of the radiation force, proportional to the transverse component of velocity,divided by the speed of light.(This is a Newtonian approximation； relativistic expressions involve higher powers of the ratio u/c.） Next,consider radial motion away from the Sun with speed r. Because of this, the particle will absorb less radiative energy in unit time than it would if it were at rest.Also, the radiation that it receives is diluted by the Doppler effect.So,relative to the “unperturbed” model, we have a radial drag force proportional to $2 \dot { \gamma } \smash { f ^ { 2 } }$ The equations of motion in the plane of the orbit can then be written:

$$
\ddot { r } - r \dot { \theta } ^ { 2 } = - \frac { \mu } { r ^ { 2 } } - \frac { 2 \alpha \dot { r } } { r ^ { 2 } } , \quad \frac { \ddot { \mathrm { 1 } } } { r } \frac { d } { d t } \big ( r ^ { 2 } \dot { \theta } \big ) = - \frac { \alpha \dot { \theta } } { r } ,
$$

where $_ \alpha$ is a small quantity depending in part on the physical characteristics of the particle, and ${ \mu = \mu _ { 0 } - \alpha c }$ ： ${ \mu } _ { \mathbb { S } } = G$ (solar mass).

With expressions for $\mathcal { R }$ and $\mathcal { B }$ ,find first-order solutions of the equations for the variations of $a , e$ and $\omega$

Show that $\bar { \mathcal { H } } = \mathcal { r } ^ { 2 } \dot { \mathcal { \theta } } = \lambda - \alpha \mathcal { \theta }$ where $\hslash$ is constant. Then,if $z = 1 / 3 ^ { 2 }$ show that

$$
u ^ { \prime \prime } \div \frac { \alpha } { \overline { { { \mathcal { H } } } } } u ^ { \prime } \div u = \frac { \mu } { \overline { { { \mathcal { H } } ^ { 2 } } } } ,
$$

the differentiation being with respect to $\pmb \theta$ $\alpha \theta / \hbar \ll 1$ this is,approximately,

$$
u ^ { n } + \frac { \alpha } { \hbar } u ^ { t } \div u = \frac { \mu } { \hbar ^ { 2 } } \left( 1 + 2 \frac { \alpha } { \hbar } \theta \right) .
$$

Solve this equation, and compare results with those just found.

62.A formula for the force exerted by radiation by the Sun on a body presenting a cross-sectional area $A \mathrm { c m } ^ { 2 }$ at $\mathtt { a }$ distance of $\mathcal { R }$ astronomical units from the Sun is

$$
{ \bar { \varepsilon } } _ { R } = 2 A { \frac { S C } { \pi R ^ { 2 } c } } { \mathrm { ~ d y n e s } } .
$$

$S C$ is the solar constant, that is,the amount of radiative energy falling on unit area in unit time one astronomical unit from the Sun.The formula assumes that the radiation is totally reflected leading to the factor of 2. If M is the mass of the body in grams, then the resulting perturbative acceleration is,numerically,

$$
A _ { R } = 9 . 1 \times \mathrm { { i } } \time 1 0 ^ { - 5 } { \frac { A } { M } } { \mathrm { ~ c m / s e c } } ^ { 2 } .
$$

This shows the importance of the ratio (surface area)/(mass). Using this formula, investigate the lifetimes of small grains in the solar system, with difference $\{ A / \lambda \}$ and starting at various distances from the Sun.

63. Consider the system of equations $x = f ( x , t ) \div g ( x , p , t )$ where $p$ is $\mathtt { a }$ constant parameter for which the numerical value is to be improved. Show that the derivatives $\partial x _ { i } ( t ) _ { j } / \partial p$ can be found by solving

$$
\delta \dot { x } = A \delta x + \frac { \partial g } { \partial p } ,
$$

with initial conditions $\delta x \{ t _ { 0 } \} = 0$ Here $A = \partial f / \partial x$

64.Write a program for using Encke's method (using universal variables). Apply it to a problem such as Sun-Jupiter-asteroid. Compare it, for timing and accuracy,with the direct integration of the equations of motion. Experiment with different policies for rectification.

65.Perform a numerical integration of a perturbed problem, and at each step calculate the osculating Keplerian elements. Use these results to set up and debuga program for calculating the variation of elements. Compare efficiencies of the two methods.

66.Investigate the motion of an artificial satellite numerically, using either of the approaches considered in the preceding project. Compare your results with the first-order approximations of the text.

67. In the motion of an artificial satelite the perigee advances or regresses, as we have seen;but close to the critical inclination it oscillates. (This is why the method of solution used in the text breaks down.） See if you can confirm this numerically;use a value of $\tilde { \ j } _ { 2 }$ that is large enough to show the effect easily. Be warned that the oscillation can seem very slow.There is a parallel here with the motion of a simple pendulum, where the pendulum can circulate one way or the other,with libration (or oscillation) separating the two directions of circulation. This parallel is veryimportant in dynamics.

68.Calculate the matrizant numerically (solving the differential equations) for some problems. Then find the same partial derivatives using tweaks of the initial conditions. Compare accuracy and effciency of the two methods.

69.This is a description of a method for numerically investigating some dynamical systems, due to H. Poincaré. The system should have two degrees of freedom, and should have an integral that involves just the four variables,x,y，,y.A good example is the restricted problem of three bodies in two dimensions, and this is used in the following illustration. Consider Jacobi's integral in the form (8.1.1） with $v ^ { 2 } = { \dot { x } } ^ { 2 } + { \dot { y } } ^ { 2 }$ ， $\mu$ will remain constant throughout the calculations. For an experiment choose a defnite numerical value for $C$ Given this value,note that if $x , y$ and $\dot { \mathfrak R }$ are known,then $j$ can be calculated;then it is sufficient to consider orbits in the three-dimensional space $\pmb { \mathcal { x } }$ y，.While one of these orbits is being described,record just those points for which $\mathfrak { Y } = \mathfrak { G }$ The result will be a set of points in the x- plane. It is possible that the orbit in the x, $\mathfrak { Y }$ space lies on a torus; then the points in the $\hat { x } { - } \dot { \hat { x } }$ plane will lie on two “circles,” called invariant curves. Conversely， the appearance that the points lie on such curves is an indication that the motion lies on a torus. Alternatively,the points may seem to be distributed in a manner that is chaotic. Calculating successive points is easy numerically (you must use Newton's method to find the points for which $y = 0$ ，and particularly rewarding if you have graphics.

The routine might be as follows: first choose $C$ ;this will not be varied. Next choose values for $\pmb { \mathcal { x } }$ and $\dot { x }$ put $y = 0$ and use the integral to find $y$ (choosing,say, the positive value). These form the initial conditions for an orbit which will be numerically integrated. Record and plot all crossings. At any stage you should be able to stop the integration, and choose new initial conditions without clearing the screen.

The first major paper in this area was by M. Henon and C. Heiles (Ref. 63)； this is a readable paper and well worth looking up. Many papers have been written using this technique (which has not been described in proper generality here); these include two by this author (Refs. 64, 65).

70. Consider the equation for the two-body problem, (6.2.3), but with slowly changing.μ. This could be interpreted as a changing gravitational “constant,” (which is to be expected in some theories) or as changing mass. Show that if $\mathcal { P }$ isdefined by (6.2.5),then $\dot { \overline { { \boldsymbol { z } } } } = - \dot { \mu } \hat { \bar { \boldsymbol { z } } }$ from this derive an equation for é. Similarly， if $\pmb { \alpha }$ is defined by the usual integral of energy, derive an equation for $\dot { a }$ Assume the basic motion to be elliptic,and take theaverages of the right-hand sides over a complete revolution. Solve the resulting equations. What general conclusions can you draw?

For the particular case μ = μo/(1 + αt),with constant μo and α, I. V. Meshchersky has shown that if $\pmb { \geqslant }$ and $\boldsymbol { \mathscr { T } }$ are defined by

$$
\rho = \frac { \tt { r } } { 1 + \alpha t } , \quad \tau = \frac { 1 } { \alpha ( 1 + \alpha t ) } ,
$$

then the equation of motion can be transformed into

$$
\frac { d ^ { 2 } \beta } { d \tau ^ { 2 } } = - \frac { \mu _ { 0 } \rho } { \rho ^ { 3 } } ,
$$

which can, of course, be solved. Using $\hat { \mathbf { \Omega } }$ solution for this, follow the corresponding progress in $\pmb { \Sigma }$ and $\pmb { \ell }$

In concluding this chapter, I want to stress that there is nothing wrong in using numerical work in preference to analytical work, and in many cases mumerical integration should come first. Additional projects to do with orbits will be found in Ref. 52.
