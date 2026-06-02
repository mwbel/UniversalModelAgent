# CHAPTER 8

In Chap. 4 it was shown that the problem of placing a satellite into an orbit is a matter of achieving the required velocity at a specified position in space. For earth-bound orbits the required velocity is in the neighborhood of 25,Ooo ft/sec, whereas for the lunar mission a velocity of approximately 35,0oo ft/sec is necessary. In this chapter we discuss the basic theory of rockets and examine the problems of optimization to meet a specific performance. Missle flexibility as it affects the desired performance will be discussed in Chap. 9.

# 8.1 Performance of Single-Stage Rockets

A rocket is a variable mass vehicle which acquires thrust by theejection of high-speed particles. The force equation for the rocket can be written in the general form

$$
\frac { d \mathbf { v } } { d t } = \frac { \mathbf { T } } { m } + \frac { \mathbf { F } _ { a } } { m } - \dot { \mathbf { g } }
$$

where T is the thrust of the jet and $\mathbf { F } _ { a }$ is the aerodynamic force. Since ${ \bf F } _ { a } / m$ varies inversely as the characteristic length of the rocket, this term is small in comparison to $\mathbf { T } / m$ for large rockets.

Certain parameters of importance can be brought out by studying the behavior ofarocketinverticalflight,neglectingerodynamicfornd

assuming the gravity field tobeaconstant.Referring toFig.8.1-1,we start with the equation,

$$
{ \frac { d v } { d t } } = { \frac { T } { m } } - g
$$

Since the rocket is losing mass,dm/dt is negative,and the thrust becomes,

$$
T = - u { \frac { d m } { d t } }
$$

where the small term due to the difference in pressure has been omitted.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/0fce014b6414b0ddbf53af4abd346c40c1b34711b029bbe9511b8a12c555596c.jpg)  
Fig.8.l-l. Rocket in vertical flight.

Substituting Eq. 8.1-3 into 8.1-2,

$$
d v = - u { \frac { d m } { m } } - g d t
$$

and integrating, the velocity equation becomes

$$
v - v _ { 0 } = u \ln { \frac { m _ { 0 } } { m } } - g t
$$

where $m$ is the mass at any time $t$ By substituting the burnout time $t _ { b 0 }$ and the burnout mass $m _ { b 0 }$ ， the maximum attainable velocity in vertical flight is

$$
v _ { b 0 } - v _ { 0 } = u \ln { \frac { m _ { 0 } } { m _ { b 0 } } } - g t _ { b 0 }
$$

$\ast _ { \mathrm { ~ u ~ } } = - u$

For chemical propellants, the ejection speed $\boldsymbol { u }$ relative to the rocket nozzle depends on the heat energy per pound which must be high,and on the molecular weight which must be small. Its performance is rated by the specific impulse I, defined as the thrust of a pound of propellant multiplied by the number of seconds required to burn it. Its relationship to $u$ is found from the equation,

$$
I = \int _ { 0 } ^ { \ell } T d t = \int _ { 0 } ^ { t } u { \frac { d m } { d t } } d t = \int _ { 0 } ^ { 1 / \ell } u d m = { \frac { u } { g } }
$$

or

$$
u = g I = 3 2 . 2 I \mathrm { f t / s e c }
$$

Some indication as to the merits of certain fuels and their propellant combinations are obtainable from Table 8-1.

Table 8-la   

<table><tr><td>Chemical Propellants</td><td>Type</td><td>Specific Impulse I, sec</td></tr><tr><td>Ammoniumnitraterubber</td><td>Solid</td><td>170-210</td></tr><tr><td>Potassium perchlorite thickol or asphalt</td><td>Solid</td><td>170-210</td></tr><tr><td>Boron metal components and oxidant</td><td>Solid</td><td>200-250</td></tr><tr><td>Liquid oxygen alcohol</td><td></td><td>250-270</td></tr><tr><td>Liquid oxygen fluorine JP4</td><td></td><td>270-330</td></tr><tr><td>Fluorine hydrogen</td><td></td><td>300-385</td></tr></table>

a"Astronautics and its Applications,"Space Handbook,U.S.Govt.PrintingOfce, Wash. D.C. (1959).

It is convenient here to introduce a thrust parameter which establishes the initial acceleration of the rocket. We define thrust ratio $\mathcal { R }$ as the thrust of the rocket divided by theinitial weight,

$$
\mathrm { T h r u s t r a t i o ~ \mathcal { R } = \frac { \it T } { m _ { 0 } g } = \frac { a _ { 0 } } { g } + 1 }
$$

where $a _ { 0 }$ is the initialacceleration inverticalfight.The time durationof the powered flight is then

$$
t _ { b 0 } = g I \Big ( \frac { m _ { 0 } - m _ { b 0 } } { T } \Big ) = \frac { I } { \mathcal { R } } \Big ( 1 - \frac { m _ { b 0 } } { m _ { 0 } } \Big )
$$

Equation 8.1-4 can now be written as,

$$
v _ { b 0 } - v _ { 0 } = g I \biggl [ \ln \frac { m _ { 0 } } { m _ { b 0 } } - \frac { 1 } { \mathcal { R } } \left( 1 - \frac { m _ { b 0 } } { m _ { 0 } } \right) \biggr ]
$$

which indicates that the maximum attainable velocity depends on the mass fraction $m _ { b 0 } / m _ { 0 }$ , on the specific impulse $I$ of the fuelandon the t ratio $\mathcal { R }$

With ${ { \iota } _ { 0 } } = 0$ ， it is possible to plot $\ v _ { b 0 } / g I$ versus $m _ { b 0 } / m _ { 0 } .$ ，with $\mathcal { R }$ as a parameter.Itisstructiveowevertlot ${ \boldsymbol { v } } _ { b 0 }$ versus $m _ { b 0 } / m _ { 0 }$ for given values of I and $\mathcal { R }$ asinFig.8.1-2sincesuchapotindicatestecy of a single-stage rocket for placing a satellite into orbit. As in most designs, a compromise must be established between, $\mathcal { R }$ ， $m _ { b 0 } / m _ { 0 }$ ,and $I$ (i.e., a large thrust ratio requires a heavier structure, and exotic fuels of high $I$ tend to give larger values of $m _ { b 0 } / m _ { 0 }$ .In any event, it is difficult to achieve a number less than 0.1 for $m _ { b 0 } / m _ { 0 }$ and a specific impulse greater than 350 for chemical propellants, which indicates the necessity of multistage rockets for satellite orbits and space missions.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/1ccdfa02ce2651f100b0b75a48f86addb1102ed208447faa34152f495189a030.jpg)  
Fig.8.l-2. Burnout velocity as function of mass ratio, specific impulse $I ,$ and thrust ratio R.

To determine the distance traveled during the powered flight, the velocity equation, Eq. 8.1-5, must be integrated. Equation 8.1-5 can be integrated if the variation in $g$ is assumed to be negligible and $m ( t )$ known. A realistic assumption is that of constant rate of fuel consumption leading to constant thrust. We can then let

$$
d t = \frac { d m } { \dot { m } } \qquad \mathrm { a n d } \qquad - \dot { m } = \frac { m _ { 0 } - m _ { b 0 } } { t _ { b 0 } } = \mathrm { c o n s t a n t }
$$

so that

$$
\begin{array} { r } { \int _ { 0 } ^ { t _ { b 0 } } ( \ln m ) d t = \cfrac { 1 } { \dot { m } } \int _ { m _ { 0 } } ^ { m _ { b 0 } } ( \ln m ) d m = \cfrac { m } { \dot { m } } \left( \ln m - 1 \right) \bigg | _ { m _ { 0 } } ^ { m _ { b 0 } } } \\ { = \cfrac { m _ { 0 } - m _ { b 0 } } { \dot { m } } - \cfrac { m _ { 0 } } { \dot { m } } \ln m _ { 0 } + \cfrac { m _ { b 0 } } { \dot { m } } \ln m _ { b 0 } } \end{array}
$$

The distance traveled then becomes,

$$
\begin{array} { r l r } {  { \bar { h } _ { b 0 } = u t _ { b 0 } \bigg [ 1 - \frac { 1 } { ( m _ { 0 } / m _ { b 0 } ) - 1 } \ln \frac { m _ { 0 } } { m _ { b 0 } } \bigg ] + v _ { 0 } t _ { b 0 } - \frac { 1 } { 2 } g _ { 0 } { t _ { b 0 } } ^ { 2 } } } \\ & { } & { = g _ { 0 } \frac { I ^ { 2 } } { \mathcal { R } } \bigg ( 1 - \frac { m _ { b 0 } } { m _ { 0 } } \bigg ) \bigg [ 1 - \frac { 1 } { ( m _ { 0 } / m _ { b 0 } ) - 1 } \ln \frac { m _ { 0 } } { m _ { b 0 } } \bigg ] + v _ { 0 } \frac { I } { \mathcal { R } } \bigg ( 1 - \frac { m _ { b 0 } } { m _ { 0 } } \bigg ) } \\ & { } & { \quad - \frac { 1 } { 2 } g _ { 0 } \frac { I ^ { 2 } } { \mathcal { R } ^ { 2 } } \bigg ( 1 - \frac { m _ { b 0 } } { m _ { 0 } } \bigg ) ^ { 2 } \qquad \quad ( 8 . 1 - 1 ) } \end{array}
$$

After burnout, the rocket is in free flight under the retarding force of gravity. In general, the altitude is sufficiently great so that the variation in $g$ must now be taken into account. Since the system during coasting is conservative, we can equate the kinetic energy at burnout to the work done by the gravity force $m _ { b 0 } g _ { 0 } \left( \frac { R } { r } \right) ^ { 2 }$

$$
g _ { 0 } \int _ { r _ { b 0 } } ^ { r _ { b 0 } + h _ { c } } \left( { \frac { R } { r } } \right) ^ { 2 } d r = { \frac { { v _ { b 0 } } ^ { 2 } } { 2 } }
$$

Thus the equation for the coasting distance becomes,

$$
h _ { c } = \frac { { v _ { b 0 } } ^ { 2 } } { 2 g } \frac { ( R + h _ { b 0 } ) ^ { 2 } } { R ^ { 2 } - ( { v _ { b 0 } } ^ { 2 } / 2 g ) ( R + h _ { b 0 } ) }
$$

where $r _ { b 0 } = R \mathrm { ~ \dot { + } ~ } h _ { b 0 }$ has been substituted. The_total height $h _ { b 0 } + h _ { c }$ reached by a single stage rocket is then the sum of Eqs. 8.1-11 and 8.1-12.

Equations 8.1-10 and 8.1-11 indicate that the performance of a singlestage rocket depends on the specific impulse $I ,$ the thrust ratio $\mathcal { R }$ and the mass ratio $\mu = \frac { m _ { 0 } } { m _ { b 0 } }$ Thefetofvaryingthesequantities ontheburnout velocity or height can be found by considering Eqs. 8.1-10 and 8.1-11 to be in the form,

$$
\begin{array} { r } { v _ { b 0 } , = f _ { 1 } ( I , \mathcal { R } , \mu ) } \\ { h _ { b 0 } = f _ { 2 } ( I , \mathcal { R } , \mu ) } \end{array}
$$

and differentiating. Thus the change in the burnout velocity is determined from the equation

$$
d v _ { b 0 } = \frac { \partial f _ { 1 } } { \partial I } d I + \frac { \partial f _ { 1 } } { \partial \mathcal { R } } d \mathcal { R } + \frac { \partial f _ { 1 } } { \partial \mu } d \mu
$$

For optimum burnout velocity， dvbo = 0, which defines the constraints imposed on the three quantities.

# PROBLEMS

1. For a given mass ratio μ and specific impulse I, how does the burnout velocity of a single-stage rocket vary with the thrust ratio $\mathcal { R }$ Assume vertical flight.   
2. Plot $v _ { b 0 } / g _ { 0 } I$ versus $\mu = m _ { 0 } / m _ { b 0 }$ with $v _ { 0 } = 0$ and $\mathcal { R }$ as parameter. Use $\mathcal { R } \simeq 1$ ,2,5.   
3. For a given specific impulse and thrust ratio, plot hbo versus μ = mo/mbo Use $\mathscr { R } = 2$ and $I = 1 5 0$ ,300 and 400 sec.   
4. Determine the burnout speed of a rocket launched vertically,using a fuel of specific impulse 250 sec and a mass fraction of 0.22 with $\mathcal { R } = 3$   
5.For $I = 3 0 0$ sec and $\mathcal { R } = 2$ ， determine the maximum height atained by a single-stage rocket of mass ratio $\mu = 5$   
6. Repeat Prob. 5 for $\mu = 3$ and $\mu = 1 0$ , and plot $h _ { \mathrm { m a x } }$ versus $\mu$   
7. Determine the partial derivatives $\partial f _ { 1 } / \partial I , \partial f _ { 1 } / \partial \mathcal { R }$ ,and $\partial f _ { 1 } / \partial \mu$ of Eq. 8.1-14. How much would the burnout velocity of Prob.5 be changed by changing $I$ to 250 sec;by changing $\mu$ to 6.0.   
8.Determine the partial derivatives $\partial f _ { 2 } / \partial I , \ \partial f _ { 2 } / \partial \mathcal { R }$ ,and $\partial f _ { 2 } / \partial \mu$ from Eq. 8.1-11 and discuss the effect of changing $I , { \mathcal { R } } ,$ or $\mu$   
9. If the burnout velocity of a rocket fired vertically is 85oo ft/sec at a height of h miles， how high will it rise when constant gravitational acceleration is assumed ?   
10. Assuming a burnout velocity of $v _ { b 0 }$ at $r = R + h _ { \ast }$ and an inverse square attractive force, determine the maximum height reached by a rocket. What is the maximum height for data of Prob. 9 under this assumption ?   
I1. If the specific impulse of a rocket engine is doubled by doubling the burning time,keeping the thrust per pound of fuel constant, how does this affect the burnout velocity ?   
l2. If the mass ratio of a rocket is doubled, keeping all other variables constant, how does this affect the burnout height for vertical flight?   
l3.A rocket fired vertically from rest has an initial weight of I0,0oo lb and a burnout weight of 2ooo lb. The flux velocity of the fuel is a constant and equal to 7500 ft/sec,and the total burning time is 55 sec. Determine the velocity and acceleration just before burnout,and calculate the height to which it will rise by equating the kinetic energy to the work done under (a) varying gravity: (b) constant gravity.

14. The efficiency of a rocket engine can be defined as the ratio of the useful power Tu(T = thrust)to the useful power plus thekineticenergy/m'(u - v)2 lost to the surroundings. Show that the rocket efficiency is given by the equation,

$$
\eta = \frac { 2 ( u / v ) } { 1 + ( u / v ) ^ { 2 } }
$$

and find the value of $u / v$ corresponding to its maximum.

15. Repeat Prob. 14 for a jet engine.

# 8.2 Optimization of Multistage Rockets²

A simple calculation with achievable mass ratio, thrust ratio,and specific impulse indicates that satellite velocities cannot be attained by the use of a single-stage rocket. We are thus led to the multistage rocket for space missions.

In a multistage rocket the burnout velocity of the first stage becomes the initial velocity $v _ { 0 }$ of the second stage, and, by casting off the empty first stage, the full burnout velocity of the second stage is available as an additional velocity to the burnout velocity of the first stage. The maximum velocity of a multistage rocket can then be computed as the sum of the single-stage velocities, as given by Eq. 8.1-6.

We will ignore the gravity loss in velocity due to the burning time, in which case the maximum velocity available to the multistage rocket of $N$ stages becomes,

$$
v _ { m } = \sum _ { i = 1 } ^ { N } u _ { i } \ln \mu _ { i }
$$

where $\mu _ { i } = { ( m _ { 0 } / m _ { b 0 } ) } _ { i }$ is the mass ratio of the ith stage. Assuming that this velocity is specified, we have a choice as to how the mass ratios should be assigned to the various stages. The problem is that of minimizing the over-all mass ratio $m _ { 0 1 } / P$ ,where ${ m } _ { 0 1 }$ is the takeoff mass and $P$ the final payload mass.

To determine the mass ratio $\mu _ { i }$ which will lead to a minimum over-all mass ratio $m _ { 0 1 } / P$ for a specified maximum velocity $\tau _ { m }$ ,it is necessary to express $m _ { 0 1 } / P$ in terms of all the $\mu _ { i }$ Since at each burnout the empty structure of the stage is to be discarded,the initial mass of the new stage is equal to the initial mass of the previous stage minus the fuel burned and the empty structure thrown off. For example,the initial mass of the second stage is $m _ { 0 2 } = m _ { 0 1 } - m _ { p 1 } - m _ { s 1 } $ ，where $m _ { p 1 }$ is the propellant mass of stage 1 and $m _ { s 1 }$ the empty structural massof stage i. Thus by writing $m _ { 0 1 } / P$ in the form

$$
\frac { m _ { 0 1 } } { P } = \frac { m _ { 0 1 } } { m _ { 0 1 } - m _ { p 1 } - m _ { s 1 } } \frac { m _ { 0 2 } } { m _ { 0 2 } - m _ { p 2 } - m _ { s 2 } } \cdot \cdot \cdot \frac { m _ { 0 N } } { P }
$$

it is possible to express the over-all mass ratio in terms of all the mass ratios

$$
\mu _ { i } = \frac { m _ { 0 i } } { m _ { 0 i } - m _ { p i } }
$$

and an additional structural factor $\beta _ { i }$ defined as

$$
\beta _ { i } = \frac { m _ { s i } } { m _ { x i } + m _ { s i } }
$$

Examining one of the factors, we can write

$$
\begin{array} { c c } { { \displaystyle \frac { m _ { 0 i } } { m _ { 0 i } - m _ { p i } - m _ { s i } } = \frac { m _ { 0 i } } { m _ { 0 i } - m _ { p i } } \frac { m _ { p i } } { m _ { p i } + m _ { s i } } \frac { ( m _ { 0 i } - m _ { p i } ) ( m _ { p i } + m _ { s i } ) } { m _ { p i } ( m _ { 0 i } - m _ { p i } - m _ { s i } ) } } } \\ { { \displaystyle ~ } } & { { ~ \mathrm { ~ \ ~ \ } = \frac { \mu _ { i } ( 1 - \beta _ { i } ) } { 1 - \mu _ { i } \beta _ { i } } ~ } } \end{array}
$$

Equation 8.2-2 can then be written as

$$
\frac { m _ { 0 1 } } { P } = \frac { \mu _ { 1 } ( 1 - \beta _ { 1 } ) } { 1 - \mu _ { 1 } \beta _ { 1 } } \frac { \mu _ { 2 } ( 1 - \beta _ { 2 } ) } { 1 - \mu _ { 2 } \beta _ { 2 } } \cdot \cdot \cdot \frac { \mu _ { N } ( 1 - \beta _ { N } ) } { 1 - \mu _ { N } \beta _ { N } }
$$

If $m _ { 0 1 } / P$ is to be a minimum, In $( m _ { 0 1 } / P )$ , will also be a minimum, so that we can write,

$$
\ln \frac { m _ { 0 1 } } { P } = \sum _ { i = 1 } ^ { N } \ln \frac { \mu _ { i } ( 1 - \beta _ { i } ) } { ( 1 - \mu _ { i } \beta _ { i } ) } = \sum _ { i = 1 } ^ { N } \left[ \ln \mu _ { i } + \ln \left( 1 - \beta _ { i } \right) - \ln \left( 1 - \mu _ { i } \beta _ { i } \right) \right]
$$

The above equation by itself does not contain the constraint imposed by the specified velocity as given by Eq. 8.2-1. This constraint can be imposed on the optimization process by the Lagrange multiplier method, which requires the constraint equation to be multiplied by a constant $\lambda$ and added to the above equation (adding zero), as follows:

$$
\ln \frac { m _ { 0 1 } } { P } = \sum _ { i = 1 } ^ { N } \left\{ \ln \mu _ { i } + \ln \left( 1 - \beta _ { i } \right) - \ln \left( 1 - \mu _ { i } \beta _ { i } \right) + \lambda [ u _ { i } \ln \mu _ { i } - v _ { m } ] \right\}
$$

Differentiation of this equation with respect to $\mu _ { i }$ will lead to the optimum values of $\mu _ { i } .$

Carrying out the differentiation, we obtain $N$ equations of the form

$$
\frac { 1 } { \mu _ { i } } + \frac { \beta _ { i } } { 1 - \mu _ { i } \beta _ { i } } + \lambda \frac { u _ { i } } { \mu _ { i } } = 0
$$

leading to the result

$$
\mu _ { i } = \frac { 1 + \lambda u _ { i } } { \lambda u _ { i } \beta _ { i } }
$$

Substituting this value of into Eq. 8.2-1, the constant $\lambda$ can be found $\mu _ { i }$   
from the equation

$$
v _ { m } = \sum _ { i = 1 } ^ { N } u _ { i } \ln { \frac { 1 + \lambda u _ { i } } { \lambda u _ { i } \beta _ { i } } }
$$

where uis $\beta _ { i } ,$ and $v _ { m }$ are assumed to be known. With λ evaluated, the mass ratio $\mu _ { i }$ of each stage is found from Eq. 8.2-9.

# Example 8.2-l

Consider a special case where the specific impulse is the same for all stages. The $u _ { i }$ are then equal in all stages and Eq. 8.2-i0 becomes

$$
\frac { v _ { m } } { u } = N \ln \left( \frac { 1 + \lambda u } { \lambda u } \right) - \sum _ { i = 1 } ^ { N } \ln \beta _ { i }
$$

$$
\frac { 1 + \lambda u } { \lambda u } = \exp { \left[ \frac { 1 } { N } \bigg ( \frac { v _ { m } } { u } + \sum _ { i = 1 } ^ { N } \ln \beta _ { i } \bigg ) \right] }
$$

Since from Eq. 8.2-9

$$
\mu _ { i } \beta _ { i } = \frac { 1 + \lambda u } { \lambda u }
$$

the mass ratio of stage $i$ is

$$
\mu _ { i } = \frac { 1 } { \beta _ { i } } \exp { \left[ \frac { 1 } { N } \biggl ( \frac { v _ { m } } { u } + \sum _ { i = 1 } ^ { N } \ln \beta _ { i } \biggr ) \right] }
$$

# PROBLEMS

1. Show that if $u _ { i }$ and $\beta _ { i }$ are the same for each stage, the optimum mass ratio is

$$
\mu _ { i } = e ^ { v _ { m } / N u }
$$

2. A two-stage rocket is to attain a maximum speed of 26,0oo ft/sec with $I _ { \mathrm { 1 } } = I _ { \mathrm { 2 } } = \bar { 3 } 0 0$ sec and $\beta _ { 1 } = \beta _ { 2 }$ Determine the mass ratio of each stage.

Ans. $\mu \stackrel { } { = } 3 . 8 5$

3. In Prob. 2, determine the propellant mass per stage in terms of the initial mass of the stageAlsodetermine the structuralfactor $\beta _ { i } ,$ assuming $\begin{array} { r l } { { m _ { s i } } = } \end{array}$ $0 . 1 5 m _ { 0 i } ,$ and show that the optimum over-allmass ratio is equal to $m _ { 0 1 } / P =$ 82.4.

4. In designing a twostage rocketfora maximum speedof 6oft/sec,ssume that $I _ { 1 } = I _ { 2 } = 2 5 0$ sec,and $\beta _ { 1 } = 0 . 1 8$ ， $\beta _ { 2 } = 0 . 1 \acute { 5 }$ .Show that it is capable of boosting a payload of $0 . 0 0 1 7 2 m _ { 0 1 }$

# 8.3 Flight Trajectory Optimization³

We will now consider a more difficult problem of establishing an optimum flight path to place a satelite into orbit. The rocket is assumed to be rigid,and we will neglect the aerodynamic forces.Generallythe

length of the powered flight path is short compared to the earth's radius, and we are justified in replacing thecentral gravitational field by aconstantplane parallel-force field.

The geometry of the problem, ilustrated in Fig. 8.3-1,shows the thrust attitude angle \$ measured from the horizontal, the gravitational force along the negative $y$ directionandthevelocityectortangenttotelight

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/21e8c17b84eae8a5c31c0f33ae74740a1aef6eff9c9564dac79b413ed4c7d00d.jpg)  
Fig.8.3-l. Powered flight trajectory.

trajectory. Letting $u$ and $w$ be the $x$ and $y$ components of the velocity v, the differential equation of motion in rectangular coordinates are,

$$
{ \dot { u } } = { \frac { F } { m } } \cos \phi
$$

$$
\dot { w } = \frac { F } { m } \sin \phi - g
$$

$$
\dot { y } = w
$$

The quantities $F / m$ and $\phi$ are functions of time, and the trajectory depends on how they vary. We will assume that F/mis a known function of time,and define the problem of selecting $\phi ( t )$ for maximum horizontal velocity U at a specified altitude Y. The time T corresponding to the instant y = Y will differ with different Φ(t) and, therefore, will not be specified. We will assume however that all of the fuel be burned prior to the time $T _ { \parallel }$

The problem which we have just defined differs from the previous one of vertical flight in that we must maximize a time integral with constraints. The equation which we are concerned with is the integral of Eq. 8.3-1,

$$
U = u _ { 0 } + \int _ { 0 } ^ { T } { \frac { F } { m } } \cos \phi d t
$$

which we wish to make a maximum at a specifed value of $y$ under the condition $w _ { t = T } = 0$ . Thus Eqs. 8.3-2 and 8.3-3 represent constraints on the allowable variations of Eq. 8.3-4. We write Eqs. 8.3-2 and 8.3-3 in the form

$$
\begin{array} { r } { \dot { \boldsymbol { w } } - \frac { \boldsymbol { F } } { m } \sin \phi + \boldsymbol { g } = 0 } \\ { \dot { \boldsymbol { y } } - \boldsymbol { w } = 0 } \end{array}
$$

multiply each by undetermined time functions $\lambda$ , and rewrite Eq. 8.3-4 in the form

$$
U = u _ { 0 } + \int _ { 0 } ^ { T } \Bigl [ \frac { F } { m } \cos \phi + \lambda _ { 1 } \Bigl ( \dot { w } - \frac { F } { m } \sin \phi + g \Bigr ) + \lambda _ { 2 } ( \dot { y } - w ) \Bigr ] d t
$$

We must now specify the boundary conditions under which the optimi-zation is to take place.

At $t = T$

$$
\begin{array} { c c } { { y = y _ { 0 } } } & { { x = 0 } } \\ { { } } & { { } } \\ { { u _ { 0 } = v _ { 0 } \cos \theta _ { 0 } } } & { { w _ { 0 } = v _ { 0 } \sin \theta _ { 0 } } } \\ { { } } & { { } } \\ { { y = Y } } & { { w = 0 } } \end{array}
$$

The initial velocity $ { \boldsymbol { { \tau } } } _ { 0 }$ at initial altitude $y _ { 0 }$ will be considered fixed,butthe initial angle $\theta _ { 0 }$ will be leftundetermined,therebyallowingthefisttermof Eq. 8.3-5 to contribute a term at the lower limit $t = 0$

Before applying Eq. C-9 of Appendix $\mathrm { C }$ to Eq. 8.3-5, we will dispense with the first term $u _ { 0 } = v _ { 0 } \cos \theta _ { \mathrm { c } }$ by noting that its contribution to $\delta U$ is $- \boldsymbol { v } _ { 0 }$ sin $\theta _ { 0 } \delta \theta _ { 0 }$ . We are then left with the integral of Eq.8.3-5, where in place of the variable $z$ ,we have $\phi$ ,W,y, $F / m$ ,and $^ { - 1 }$ The equation with which we are concerned is, then,

$$
\delta U = - \boldsymbol { v } _ { 0 } \sin \theta _ { 0 } \delta \theta + \delta \int _ { 0 } ^ { T } f \Big ( \phi , w , \dot { w } , \dot { y } , \frac { F } { m } \Big ) d t
$$

where the variation of the integral is to be determined from Eq. C-9.

For the first problem, $F / m$ is assumed to be a known function of time which is not varied,and we are to find a \$(t) which willresult in a maximun

horizontal velocity $U$ at a given height $Y$ The partial derivatives indicated in Eq. C-9 are determined from Eq.8.3-5 to be

$$
{ \begin{array} { l l } { { \displaystyle { \frac { \partial f } { \partial \phi } } = - { \frac { F } { m } } \left( \sin \phi + \lambda _ { 1 } \cos \phi \right) } } & { { \begin{array} { l } { { \frac { \partial f } { \partial \dot { \phi } } } = 0 } \\ { { \frac { \partial f } { \partial \psi } } = - \lambda _ { 2 } } \end{array} } } \\ { { \frac { \partial f } { \partial \psi } } = 0 } & { { \begin{array} { l } { { \frac { \partial f } { \partial \dot { w } } } = \lambda _ { 1 } } \\ { { \frac { \partial f } { \partial \dot { y } } } = \lambda _ { 2 } } \end{array} } } \end{array} }
$$

The total variation from Eq. C-9 is then

$$
\begin{array} { l } { { \displaystyle  \begin{array} { l } { { \displaystyle \{ { \begin{array} { l } { { \displaystyle \mathcal { V } } = - v _ { 0 } \sin \theta _ { 0 }  \delta \theta _ { 0 } + \lambda _ { 1 }  \delta \psi | _ { 0 } ^ { T } + \lambda _ { 2 }  \delta y | _ { 0 } ^ { T } } } } \\ { { \displaystyle - \int _ { 0 } ^ { T } \Bigl [ \frac { F } { m } ( \sin \phi + \lambda _ { 1 } \cos \phi )  \delta \phi + \frac { d \lambda _ { 2 } } { d t } \delta y + ( \frac { d \lambda _ { 1 } } { d t } + \lambda _ { 2 } )  \delta w ] d t = } } \end{array}  } } } \end{array} \end{array}
$$

Since $y$ at $t = 0$ and $t = T$ are fixed as $y _ { 0 }$ and $Y _ { : }$ ， the variation at the end points must be zero, which eliminates the third term in Eq.8.3-7. For the second term of Eq. 8.3-7, the variation $\delta w$ at $t = 0$ is ( $v _ { 0 }$ is specified as fixed),

$$
\delta w \Big \vert _ { 0 } = \delta ( v _ { 0 } \sin \theta _ { 0 } ) = v _ { 0 } \cos \theta _ { 0 } \delta \theta _ { 0 }
$$

At the terminal time $t = T _ { i }$ w is obtained from the integral of Eq. 8.3-2a to be

$$
w = \int _ { 0 } ^ { T } { \frac { F } { m } } \sin \phi d t - g T + v _ { 0 } \sin \theta _ { 0 }
$$

and its variation at $t = L$ due to variations $\delta \phi$ and $\delta \theta _ { 0 }$ is

$$
\delta w \bigg | ^ { T } { = } \int _ { 0 } ^ { T } \frac { \ d z } { m } \cos \phi \delta \phi d t + v _ { 0 } \delta \theta _ { 0 } \cos \theta _ { 0 }
$$

We note that $w$ for the optimum curve becomes zero at $t = T ,$ whereas for the varied curve $w$ becomes zero at a different time $T + \delta T .$ Since $\frac { F } { m }$ is not varied and is zero for $t > T ,$ the above expression for $\delta w \left| ^ { { \cal Z } } \right.$ must equal $g \delta T .$

$$
\delta U = - v _ { 0 } ( \sin \theta _ { 0 } + \lambda _ { 1 , t = 0 } \cos \theta _ { 0 } ) \delta \theta _ { 0 } + g \lambda _ { 1 , t = T } \delta T
$$

$$
- \int _ { 0 } ^ { \pi } \left[ { \frac { F } { m } } \left( \sin \phi + \lambda _ { 1 } \cos \phi \right) \delta \phi + { \frac { d \lambda _ { 2 } } { d t } } \delta y + \left( { \frac { d \lambda _ { 1 } } { d t } } + \lambda _ { 2 } \right) \delta w \right] d t = 0
$$

Since the variations $\delta \theta _ { 0 }$ ,8T, $\delta \phi$ , etc., are arbitrary, $\delta U$ can be zero only if all their coefficients are zero, or

$$
\begin{array}{c} \begin{array} { l l } { \tan \theta _ { 0 } = - \lambda _ { 1 , t = 0 } } & { { \begin{array} { l } { { \frac { d \lambda _ { 2 } } { d t } } } \end{array} } = 0 } \\ { \lambda _ { 1 , t = { \underline { { { T } } } } } = 0 } \\ { \tan \phi = - \lambda _ { 1 } } \end{array}  & { { \begin{array} { l } { { \frac { d \lambda _ { 1 } } { d t } } + \lambda _ { 2 } = 0 } \end{array} } } \end{array}
$$

From the last two equations we, obtain

$$
\begin{array} { r } { \lambda _ { 2 } = - C _ { 2 } \qquad \mathrm { ( a ~ c o n s t a n t ) } } \\ { \frac { d \lambda _ { 1 } } { d t } - C _ { 2 } = 0 \qquad } \\ { \lambda _ { 1 } = C _ { 1 } + C _ { 2 } t \qquad } \end{array}
$$

Substituting for $\lambda _ { 1 }$ at $t = 0$ ,and $t = T$ from the first two equations, we ind

$$
\begin{array} { r } { C _ { 1 } = - \tan \theta _ { 0 } } \\ { C _ { 2 } = \displaystyle \frac { 1 } { T } \tan \theta _ { 0 } } \end{array}
$$

so that

$$
\lambda _ { 1 } = - \left( 1 - \frac { t } { T } \right) \tan \theta _ { 0 }
$$

The equation for the thrust attitude is then obtained from the third equation to be

$$
\tan \phi = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

and $\phi$ varies from $\theta _ { 0 }$ to zero according to Eq. 8.3-9.

# 8.4 Optimum Program for Propellant Utilization

In the problem just discussed,it was found that, for an arbitrarily defined time variation of $F / m$ ,the optimum program for the thrust attitude, where the initial angle $\theta _ { 0 }$ was also allowed a variation, was found to be

$$
\tan \phi = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

If the initial angle θ, is a given quantity which is not allowed a variation, the optimum thrust atitude willstillbe alinear function of time but of the form (see Prob. 8.4-1),

$$
\tan \phi = \tan \phi _ { 0 } - C _ { 2 } t
$$

In either case, the above thrust atitude programs result in a maximum horizontal velocity U for the specified program of F/m. The maximum U attained will,however,differ with different programs of F/m,or the manner of propellant utilization, and we wish now to establish the optimum program for propellant utilization to obtain the largest of the maximum $U$ attained under optimum thrust atitude variation.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/11b9fba61821ed9396b1d122327481cc3293c3d26173f8c8d2b9d0c76eed0bae.jpg)  
Fig. 8.4-l. Possible variation of V.

We recognize here that the theoretically attainable velocity $V _ { k }$ in the absence of all forces other than thrust, is essentially a function of the specific impulse $I$ of the fuel and the mass ratio of the rocket (see Sec. 8.1)

$$
V _ { \ast } = g I \ln \frac { m _ { 0 } } { m _ { b 0 } }
$$

where it is assumed that the specific impulse is independent of the manner in which the fuel is utilized. It is then convenient to make the following substitution

$$
\begin{array} { c } { { \displaystyle { \frac { d V } { d t } } = \frac { F } { m } } } \\ { { \displaystyle V = \int _ { 0 } ^ { t } { \frac { F } { m } } d t } } \end{array}
$$

where $V$ is the rocket thrust velocity with the maximum attainable value equal to $V _ { k }$ It is evident that $V$ is a function only of time, and depends on the manner in which the fuel is consumed. Thus for any program of propellant utilization, any curve between $V = 0$ and $\boldsymbol { V } _ { k }$ with positive slope (including zero), as shown in Fig. 8.4-1, is a possible curve. Since F and m are both positive quantities, the slope dV/dt is bounded between 0 (for $F = 0$ ) to infinity (for instantaneous burning).

We will assume the initial value of $\boldsymbol { \tau } _ { 0 }$ and $\theta _ { 0 }$ to be fixed and, that the optimum thrust attitude variation indicated by Eq. 8.4-2 is to be followed. The integral to be maximized is from Eq. 8.3-5,

$$
U = \int _ { 0 } ^ { T } \biggl [ ( \cos \phi - \lambda _ { 1 } \sin \phi ) { \frac { d V } { d t } } + \lambda _ { 1 } ( \dot { w } + g ) + \lambda _ { 2 } ( \dot { y } - w ) \biggr ] d t
$$

and since the optimum thrust attitude is to be followed,allof the variations have been considered in the previous problem except $\delta V ,$ which requires us to consider only the first term of this integral.

To determine the terms of Eq. C-9, we need the following:

$$
{ \frac { \partial f } { \partial V } } = 0 \qquad { \frac { \partial f } { \partial { \dot { V } } } } = ( \cos \phi - \lambda _ { 1 } \sin \phi )
$$

and since $\delta V$ at $t = 0$ and $t = T$ is zero, we obtain the variation

$$
\begin{array} { l } { \displaystyle \delta U = - \int _ { 0 } ^ { T } \frac { d } { d t } ( \cos \phi - \lambda _ { 1 } \sin \phi ) \delta V d t } \\ { \displaystyle = \int _ { 0 } ^ { T } \biggl [ ( \sin \phi + \lambda _ { 1 } \cos \phi ) \dot { \phi } + \sin \phi \frac { d \lambda _ { 1 } } { d t } \biggr ] \delta V d t } \end{array}
$$

From Eqs. 8.4-5 and 8.4-2 we have

$$
\begin{array} { r l r } { \lambda _ { 1 } = - \tan \phi = - \tan \phi _ { 0 } + C _ { 2 } t } \\ { \frac { d \lambda _ { 1 } } { d t } = - \frac { \dot { \phi } } { \cos ^ { 2 } \phi } = C _ { 2 } } \end{array}
$$

from which

$$
\begin{array} { l } { { \displaystyle \delta U = C _ { 2 } \int _ { 0 } ^ { T } ( \sin \phi ) \delta V d t } } \\ { ~ } \\ { { \displaystyle ~ = C _ { 2 } \int _ { 0 } ^ { T } \frac { \tan \phi _ { 0 } - C _ { 2 } t } { \sqrt { 1 + ( \tan \phi _ { 0 } - C _ { 2 } t ) ^ { 2 } } } \delta V d t } } \\ { { \displaystyle ~ = C _ { 2 } \int _ { 0 } ^ { T } \Phi \delta V d t = 0 } } \end{array}
$$

It is evident here that the integrand

$$
\Phi = { \frac { \tan \phi _ { 0 } - C _ { 2 } t } { \sqrt { 1 + ( \tan \phi _ { 0 } - C _ { 2 } t ) ^ { 2 } } } }
$$

can be positive, negative, or vary from plus to minus as t varies from O to $T$ ， so that,for the integral $\delta U$ to be zero, the function $V ( t )$ must be a


<!-- chunk 0005: pages 281-350 -->
discontinuous function of time (i.e., the fuel must be burned instantaneously). We will consider three possible cases:

1. If Φ is always positive, all of the propellant must be burned instantaneously at the beginning, and the optimum program for V is the heavy discontinuous curve of Fig. 8.4-2. For $V ( t )$ to be optimum, $\delta U$ must be negative for any variation of $V$ from the optimum. For instance, any variation $\delta V$ from the optimum curve of Fig. 8.4-2, such as the dotted curve,must be negative, which means that $\delta U$ would be negative. A positive variation $\delta V$ is not possible from the optimum curve shown, since $V _ { k }$ is the maximum available rocket thrust velocity fixed by the specific impulse and the mass ratio. These arguments, therefore, establish the optimum program for the propellant utilization corresponding to positive $\Phi$ to be that of instantaneous burning at $t = 0$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0005_pages_0281-0350/auto/images/ff3efa72d01c0d356074866650e79a52f5f4cb27e0e75541703cef11aad377b0.jpg)  
Fig. 8.4-2. Instantaneous burning at $t = 0$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0005_pages_0281-0350/auto/images/3c64d647a7b7993cd2be7ed175c192db37ef029c8ab50ca79aa9888b6c5478ca.jpg)  
Fig. 8.4-3. Instantaneous burning at $t = T ,$

2. If $\Phi$ is negative, the optimum curve for $V ( t )$ must be as shown in Fig. 8.4-3,which implies instantaneous burning at t = T. Any variation δV from this curve would be positive, which would result in a negative $\delta U$ cr a smaller value of $\upsilon$

3. If $\Phi$ changes sign from plus to minus, the optimum curve for $V$ must appear as in Fig. 8.4 4,and part of the fuel must be burned instantaneously at $t = 0$ ,and the remainder at $t = T$ ， Again,any varied curve which has zero or positive slope is allowable,and if a positive $\delta U$ cannot be produced, the discontinuous curve of Fig. 8.4-4 must stand as the optimum curve.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0005_pages_0281-0350/auto/images/3c99568b0f0b600da7bb304289a5de5853bfc01a41a618755997b4c2674ba973.jpg)  
Fig. 8.4-4. Instantaneous burning at $t = 0$ and $t = T ,$

# PROBLEMS

1. For a specified program of fuel utilization, $F / m$ is a known function of time which allows no variation in the quantity $F / m$ . Assume now that both the initial velocity $v _ { 0 }$ and its inclination $\theta _ { 0 }$ to be specified,and show that the optimum program for the thrust attitude $\phi ( t )$ is

$$
\tan \phi = \tan \phi _ { 0 } - C _ { 2 } t
$$

2. Show that,if a body is projected upwards with an initial velocity at an angle $\theta _ { 0 }$ , the tangent to the flight path will be

$$
\tan \theta = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

where $T =$ time for maximum height.

3. For the case $\phi _ { 0 } = \theta _ { 0 } ,$ show that $\Phi$ in Eq.8.4-7 is always positive,and that for optimum utilization of the propellant all of the fuel must be burned instantaneously at the beginning.

4. Assuming that $v _ { 0 }$ is zero,and all of the fuel is burned at the initial instant, determine the time $T$ at which maximum horizontal velocity is attained at height $Y _ { c }$

5.Determine the time required to deliver a satelite to a height $Y = 3 0 0$ miles witha horizontal velocity of $V = 2 2 , 0 0 0$ ft/sec.

6.In Prob.4,showthattheinitial thrust attitudeshould besin $\phi _ { 0 } = ( 1 / V _ { \mathit { k } } ) \ \times$ ${ \sqrt { 2 g Y } } ,$ and that $\nu _ { k }$ mustbegreaterthanthevelocitynecessaryforproecting a body vertically upwards to a height $\boldsymbol { \underline { \boldsymbol { \gamma } } } .$

7. In Prob.5, determine the initial angle $\phi _ { 0 }$ and the total rocket velocity $V _ { k }$ ：

8. For the case where the variation of Φ is from positive to negative, discuss how you would find V or the portion of the fuel to be burned at the initial instant.   
9. Determine the optimum fuel utilization program to achieve maximum height for a rocket shot vertically.   
10. Determine the optimum fuel utilization program for maximum height of a two-stage rocket of equal stages.   
11. Discusstheproblem of obtaining the greatest altitude for a specified horizontal velocity.   
12. Discuss the problem of minimum propellant consumption for a specified horizontal velocity and altitude.

# 8.5 Gravity Turn1

In the previous section it was shown that the optimum thrust attitude for placing a satellite into orbit is given by the equation,

$$
\tan \phi = \left( 1 - { \frac { t } { T } } \right) \tan \theta _ { 0 }
$$

Likewise, the optimum thrust atitude for maximum range (balistic missile) can be shown to be $\phi =$ constant. These conditions may be satisfactory for a rocket traveling in vacuum but, owing to the large angle of attack $( \phi - \theta )$ which results from such trajectories, they are not feasible through the atmosphere. Thus for flight through the atmosphere， a trajectory known as gravity turn is generally used. In a gravity turn the thrust vector is kept parallel to the velocity vector at all times, starting with some nonvertical initial velocity $v _ { 0 }$ .Thus the gravity turn is also one of zero angle of attack or zero lift.

It is convenient here to measure the angle made by the velocity vector from the vertical, as shown in Fig. 8.5-1. Again assuming zero aerodynamic drag and constant gravity field, we write equations for the forces in the tangential and normal directions to the trajectory.

$$
{ \begin{array} { l } { { \frac { 1 } { g } } { \frac { d v } { d t } } = { \frac { F } { m g } } - \cos \psi } \\ { { \frac { v } { g } } { \frac { d \psi } { d t } } = \sin \psi } \end{array} }
$$

These equations are nonlinear and no analytical solution is known when $F / m g$ varies with time. A reasonable assumption for $F / m g$ is $F =$ constant, and $m = m _ { 0 } - m ^ { \prime } t .$

When $F / m g$ is a constant, these nonlinear equations can be solved analytically. For F/mg to be constant, the thrust F must decrease with time to conform to the decreasing mass. If $F / m g$ is a varying function of time, we can assume $F / m g$ to be constant over short intervals of time, and we can carry out a step-by-step numerical integration, using the analytical solution over each interval. It is evident, then, that the analytical solution for constant $F / m g$ is of practical interest, and we consider its development as follows:

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0005_pages_0281-0350/auto/images/8abc6878757198db6767e934fe428a95470a88c7ad914641b1da5123ec7d5aaf.jpg)  
Fig. 8.5-l. Gravity turn trajectory.

Let $F / m g = n$ over a short increment of the flight path. We introduce

$$
z = \tan { \frac { 1 } { 2 } } \psi = { \sqrt { \frac { 1 - \cos \psi } { 1 + \cos \psi } } } = { \frac { \sin \psi } { 1 + \cos \psi } }
$$

Then

$$
z ^ { 2 } = { \frac { 1 - \cos \psi } { 1 + \cos \psi } }
$$

and

Differentiating Eq. 8.5-3,

Therefore,

$$
{ \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } } = \cos \psi
$$

$$
{ \frac { d z } { d t } } = { \frac { 1 } { 2 \cos ^ { 2 } \left( \psi / 2 \right) } } { \frac { d \psi } { d t } }
$$

$$
\frac { d \psi } { d t } = ( 1 + \cos \psi ) \frac { d z } { d t }
$$

By substitution into Eqs. 8.5-1 and 8.5-2, they become,

$$
\begin{array} { l } { { \displaystyle { \frac { 1 } { g } \frac { d v } { d t } = n - \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } } } } \\ { { \displaystyle { \frac { v } { g } \frac { d z } { d t } = z } } } \end{array}
$$

Eliminating $d t$ between the above equations,

$$
\frac { d v } { v } = n \frac { d z } { z } - \frac { 1 - z ^ { 2 } } { 1 + z ^ { 2 } } \frac { d z } { z }
$$

Integrating, we have (see Peirce\* nos. 53 and 55),

$$
\ln v = \ln z ^ { n } + \ln { \frac { 1 + z ^ { 2 } } { z } } + \ln C ^ { \prime }
$$

or

$$
v = C z ^ { n - 1 } ( 1 + z ^ { 2 } )
$$

The constant $C$ can be evaluated from initial conditions to be,

$$
C = \frac { v _ { 0 } } { z _ { 0 } ^ { n - 1 } ( 1 + { z _ { 0 } } ^ { 2 } ) }
$$

Substituting Eq. 8.5-7 into 8.5-5 and integrating,

$$
\begin{array} { l } { { \displaystyle t = \frac { C } { g } \int _ { z _ { 0 } } ^ { z } z ^ { n - 2 } ( 1 + z ^ { 2 } ) d z } } \\ { { \displaystyle \quad = \frac { C } { g } z ^ { n - 1 } \left( \frac { 1 } { n - 1 } + \frac { z ^ { 2 } } { n + 1 } \right) \bigg \vert _ { z _ { 0 } } ^ { z } } } \end{array}
$$

Equation 8.5-9 gives $t$ as a function of $z = \tan { \frac { 1 } { 2 \psi } }$ for any initial condition $C$ .Thus, conversely, $\psi$ is known in terms of $t$ and $C$ Equation 8.5-7 gives $v$ as a function of $z$ and $C$ ,so that $\boldsymbol { v }$ is also known in terms of $t$ and $C$ Thus Eqs. 8.5-7, 8.5-8, and 8.5-9 represent the solution for the gravity turn trajectory when the thrust-to-weight ratio $F / m g$ is a constant $n$

To apply these equations for a varying $F / m g$ ,we start with the initial conditions expressed by Eqs. 8.5-3 and 8.5-8, and $F / m g = n$ at $t = 0$ Choosing a value of $\psi$ slightly greater than $\psi _ { 0 }$ ,determine $\boldsymbol { v }$ from Eq. 8.5-7 and $\Delta t$ from Eq. 8.5-9. The increment in the displacement is, then,

$$
\begin{array} { r } { \Delta x = \frac { 1 } { 2 } ( v _ { 0 } \sin \psi _ { 0 } + v \sin \psi ) \Delta t } \\ { \Delta y = \frac { 1 } { 2 } ( v _ { 0 } \cos \psi _ { 0 } + v \cos \psi ) \Delta t } \end{array}
$$

The procedure can now be repeated with the values at the new point as initial condition.

# PROBLEMS

1. By reversing the force $F _ { s }$ show that the motion of a body hurled into a resisting medium can be solved by the techniques of this section.   
2.If $F / m g$ is constant throughout flight, what is the effect of changing the initial angle $\psi _ { 0 }$ on; (a) the final velocity; $( b )$ the time of flight.   
3. For constant value of $F / m g$ , the velocity and its inclination $\psi$ were observed at a given time. If the initial angle is doubled, how would the above quantities differ at the same time.

4. From Eqs. 8.5-1 and 8.5--2 derive the ballistic equation of a rocket

$$
{ \frac { 1 } { v } } { \frac { d v } { d \psi } } = \left( { \frac { F - D } { m g } } \right) { \frac { 1 } { \sin \psi } } - { \frac { 1 } { \tan \psi } }
$$

where $D$ is the aerodynamic drag.

Hint: The normal and tangential accelerations can be written as

$$
{ \begin{array} { r c l } { } & { } & { { v { \dot { \psi } } } = v ^ { 2 } / R } \\ { } & { } & { { \dot { v } } = { \cfrac { d v } { d \psi } } \cfrac { d \psi } { d s } \cfrac { d s } { d t } = \operatorname * { \frac { v } { R } } \cfrac { d v } { d \psi } } \end{array} }
$$

where $R$ is the radius of curvature of the trajectory, and $d s = R d \psi$

# REFERENCES

1. Culer, G. J. and B. D. Fried,“Universal Gravity Turn Trajectories,” J. Appl. Physics,28,No. 6 (June 1957), 672-676   
2.Hall, H. H.,and E. D. Zambeli,“On the Optimization of Multistage Rockets," Jet Propulsion,28 (July 1958),463-465.   
3. Okhotsimskii, D.E.,and T. M. Eneev,“Some Variation Problems Connected with theLaunching of Artificial Satelites of the Earth,”J.British InterplanetarySoc., 16 (5), (Jan.-Feb. 1958), 263-294.   
4.Bellman, R. and Dreyfus, S.,"An Application of Dynamic Programming of the DetermnationofOptimal Satelite Trajectories J.British InterplanetarySociety Vol. 16 No. 3-4 (1959), p. 78-83.   
5. Leitmann,G."Optimization Techniques with Appications to AerospaceSytem" Academic Press, New York,1962.

# Generalized Theories of Mechanics
