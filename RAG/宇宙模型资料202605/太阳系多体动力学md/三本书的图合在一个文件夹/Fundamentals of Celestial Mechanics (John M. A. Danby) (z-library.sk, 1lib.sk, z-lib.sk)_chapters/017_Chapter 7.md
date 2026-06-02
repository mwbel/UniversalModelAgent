# Chapter 7

# The Determination of Orbits

# 7.1Introduction

In Chapter Six we have seen how, once the elements of an orbit are known, the geocentric position on the celestial sphere can be calculated for any time. In this chapter we shall be concerned with the reverse situation, that of finding the elements of an orbit from observations. For convenience we shall refer to the observed body asa comet, but it could equally well bea minor planet or aninterplanetary spacecraft；with slight modifications to the methods used,it could be an artificial satellite. The roughest glance at the process of ephemeris computation described in Section 6.16 will show that the work cannot practically be reversed,so that some new technique must be found. In fact no direct way is known for finding the elements of an orbit from observations,and it is necessary to proceed byapproximations.

We divide the subject into two parts:finding a preliminary,approximate orbit froma minimum of observations,and,secondly,using many observations to improve the orbit. The second part is by far the more important;in fact the detailed analysis of many observations yields not only a definitive orbit,but also knowledge of the dynamical environment in which the motion takes place; ie.,the relevant forces,gravitational or otherwise. This is too big an area for the present text,and will be only briefly looked at in sections 7.4-7.6.

The classical problem of the determination of orbits is to find a preliminary orbit of a newly discovered comet or minor planet using data from three observations,each one comprising time, right ascension and declination. It has been argued forcibly that this is no longer an important problem;but it is one that still evokes a lot of interest,and it can be solved, elegantly and without drudgery，on the microcomputer. It is none the worse for having a long and sometimes romantic history. The potential solver faces some danger. Solution may be impossible if the observations are too close together in time, or if they are unfavorably placed geometrically relative to each other. The situation is complicated by the fact that the observations will contain errors.How do you locate the“position”ofa fuzzy object with a little tail? All methods of solution proceed by successive approximations. So in this work you will with inaccurate data, be using mathematical steps that may not converge to find a solution that may not exist. With that understood,let us be optimists, relax and enjoy the shiect.Otherwise,skip to section 7.4!

There are two traditional approaches to the subject,following the approaches of Laplace and Gauss. Laplace's method will be discussed, but without a program,although details of a program should be fairly clear. In section 7.3 two methods that have evolved from Gauss'approach will be described,with programing discussed.

An observer on another star would recognize the bodies in the solar system as moving in elliptic orbits about the Sun; but observations from the Earth are affected by the motion of the Earth. The observed geocentric path will obviously not be an ellipse,and Figure 7.1, showing part of the path of comet Arend-Roland (1956 h),demonstrates how complicated the observed path will become. The position of the Earth in the solar system at any time is,of course,accurately known. If we could observe the distance of the comet, then there would be no difficulty in calculating its position in the solar system; unfortunately only its direction can be observed,and the calculation of its distance is one of the processes of orbit determination. In astrodynamics more and different information may be available from observations. The processes of orbit determination can be modified (and simplified) to take advantage of this extra information.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/36b5089bac6a304e0d11f5216efbbf6bd9f2a5093410ea3b53143f6067370c4a.jpg)  
Figure 7.1 The chart is a central projection, so that all great circles appear as straight lines.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/aeb3d3c79d45e81274345ff46e237a998d7dcef8c79e4830a71f30aa236d155b.jpg)  
Figure 7.2

For interest we shall describe in principle the method used by Kepler to find the distance,and thence the orbit,of Mars.The sidereal period of Mars wasaccurately known,and Figure 7.2 shows the situation for two observations separated by one sidereal period, so that Mars has returned to the same position inthe solar system.Since the sidereal period is 1.88 years,the Earth will have revolved through approximately $6 7 7 ^ { \circ }$ ,so that the angle $E _ { 1 } S E _ { 2 }$ is known,as is the distance $\mathcal { E } _ { \mathrm { 1 } } \mathcal { E } _ { 2 }$ (but only in terms of the astronomical unit). Observations furnish the angles $\mathbb { E } _ { \ 1 } \mathbb { E } _ { 2 } \mathbb { M }$ and $\mathbb { E } _ { 2 } \mathbb { E } _ { 1 } \mathbb { M }$ ，so that the triangle $E _ { 1 } E _ { 2 }$ can be solved to find the lengths of the sides,and ultimately the distance ${ \tilde { \beta } } { \tilde { \beta } } { \tilde { S } } .$

The price of the simplicity ofKepler'smethod is that observations are needed over many revolutions, and this is a luxury that we cannot afford. The history ofthe discovery of Ceres willillustrate this. Ceres,the first of the minor planets tobe discovered,was found by Piazzi in 1801,but only a few observations were possible before it approached conjunction and became too close to the Sun to be observed. Ceres is a faint object,and it was obviously important to predict when and where it could be observed again; this prediction could not be based on the leisurely study of several revolutions but had to depend on a small arc of one revolution. In this case the occasion was doubly historic because Gauss evolved a new method for orbit determination;the principles of this will be described later.

A single observation yields two angles and the time. Since six unknowns must be found before the orbit is determined,a minimum of three observations isnecessary. An accurate orbit, the definitive orbit, is found from many more observations, but since three are enough,we shall be concerned here with the problem of determining the orbit from these.

It is instructive at this stage lo consider the observed path geometrically. Throughout this chapter we shall use the notation of Figure 7.3, where $S , E .$ and Capply to the Sun, the Earth,and the comet,respectively.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/f874540e66157fdbb76ac0d263d7eafc1e6fa66bbea44256b5acce4574636c8c.jpg)  
Figure 7.3

The observed quantity is the unit vector β,and it traces out a curve on the celestial sphere (which we assume to have unit radius). Then

$$
\begin{array} { r } { \frac { \vec { d } \hat { \pmb { \rho } } } { \vec { d s } } = \hat { \pmb { \rho } } ^ { \prime } = \hat { \pmb { \ t } } , } \end{array}
$$

where s is the distance measured along the curve and $\widehat { \pmb { \xi } }$ is the unit vector tangent to the curve at p. (The prime will denote differentiation with respect to s in this section only.）) Let

$$
\hat { \mathbf { \hat { \mathbf { \mathbf { \mathbf { 1 } } } } } } = \hat { \mathbf { \mathbf { \mathbf { \mathbf { \beta } } } } } \times \hat { \mathbf { \mathbf { \mathbf { t } } } } .
$$

Since $\widehat { t } ^ { \prime }$ is perpendicular to $\widehat { \sf t } _ { \sf s }$ it can be resolved along $\hat { \pmb { \mathscr { P } } }$ and $\hat { \mathfrak { A } }$ so that

$$
\hat { \dot { \bf t } } ^ { \prime } = \lambda \hat { \underline { { \rho } } } \div \kappa \hat { \underline { { \bf { \ n } } } } ,
$$

where,by differentiating p·t= O, we see that X=-1. The component of t' at right angles to the line of sight is kf,and Figure 7.4 shows the situation where K is positive;in this case the curve is concave toward the direction n.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/72b04a5c39c329a88dfe92dd7bc16576ddf864db5b13bf9e5e98c2b0939a5102.jpg)  
Figure 7.4

When $\kappa$ is negative, the curve is convex toward n. Now

$$
\begin{array} { r } { \mathbf { \vec { s } } + \mathbf { \vec { a } } = \pmb { \rho } = \rho , } \end{array}
$$

$$
\begin{array} { r l } & { \dot { \bar { \mathbf { r } } } + \dot { \bar { \mathbf { R } } } = \dot { \rho } \hat { \rho } + \rho \dot { \hat { \rho } } } \\ & { \qquad = \dot { \rho } \hat { \rho } + \rho \frac { \dot { d } s } { d \hat { \varepsilon } } \hat { \mathbf { \varepsilon } } , \quad ( \bar { d } \hat { \varepsilon } \operatorname { r e f e r s } \mathrm { ~ } \hat { \rho } \mathrm { ~ t a ~ t i n e ~ t i m e } ) } \end{array}
$$

and

$$
\ddot { \bar { \varepsilon } } + \ddot { \bar { \mathcal { R } } } = \ddot { \rho } \hat { \rho } + 2 \dot { \rho } \frac { \dot { d } s } { \dot { d } \hat { \varepsilon } } \hat { \bar { \varepsilon } } + \rho \frac { \dot { d } ^ { 2 } s } { \dot { d } \hat { \varepsilon } ^ { 2 } } \hat { \bar { \varepsilon } } + \rho \left( \frac { \dot { d } s } { \dot { d } \hat { \varepsilon } } \right) ^ { 2 } ( - \hat { \rho } + \kappa \hat { \mathbf { n } } ) .
$$

Multiply by·n；then

$$
( \overleftrightarrow { \mathbf { r } } \div \overleftrightarrow { \mathbf { R } } ) \cdot \widehat { \mathbf { n } } = \rho \left( \frac { d s } { d \widehat { t } } \right) ^ { 2 } \kappa .
$$

Now both the Earth and the comet move subject to the gravitational attraction of the Sun,and the mass of each can be neglected compared with the mass of the Sun. Hence

$$
{ \ddot { \mathfrak { x } } } = - \mu { \frac { \mathfrak { x } } { r ^ { 3 } } } \quad { \mathrm { a n d } } \quad { \ddot { \mathbb { R } } } = - \mu { \frac { \mathbb { R } } { { \frac { 2 } { R ^ { 3 } } } } } ,
$$

and so

$$
\begin{array} { l } { { \displaystyle { \ddot { \bar { \bf r } } } + { \ddot { \bar { \bf R } } } = - \mu \left( \frac { \bar { \bf r } } { r ^ { 3 } } + \frac { \bar { \bf R } } { R ^ { 3 } } \right) } } \\ { ~ = - \mu \left( \frac { \rho - { \bf R } } { r ^ { 3 } } + \frac { \bar { \bf R } } { R ^ { 3 } } \right) . } \end{array}
$$

Multiply by ·n; then from (7.1.1） we find

$$
\mu \left( { \frac { \hat { \mathbf { i } } } { \pi ^ { 3 } } } - { \frac { 1 } { R ^ { 3 } } } \right) \mathbf { R } \cdot { \hat { \mathbf { n } } } = \rho \left( { \frac { d s } { d t } } \right) ^ { 2 } \kappa .
$$

Now suppose K is positive;then $( \gamma - R )$ and $\sum \cdot \hat { \mathbf { \nabla } }$ have opposite signs.If >R,then the direction of the Sun makesan angle of more than $9 0 ^ { \circ }$ with $\hat { \pmb { \mathfrak { x } } }$ and the curve is convex toward the Sun.If $\gamma < \mathcal { Z }$ then the curve is concave toward the Sun.These results are not altered if $\kappa$ isnegative. Hence we have Lambert's theorem that the apparent path is convex toward the Sun when ，R and concave toward the Sun when $r < \ R$ This is illustrated in Figure

From the triangle $\mathcal { S E C }$ we have

$$
\begin{array} { r } { \tau ^ { 2 } = \rho ^ { 2 } + R ^ { 2 } - 2 R \rho \cos \psi , } \end{array}
$$

and,formally, this and (7.1.2） can be solved for the two unknowns r and $\boldsymbol { \rho }$ But this will be impossible if $\kappa = \ell$ ；then, the three observations will lie on a great circle,and the six quantities will not be independent,so more than three observations are needed.There will be trouble if $\kappa$ is small.In fact the ability todetermine an orbit from three observations depends upon the extent to which the observed arc departs from $\hat { \pmb { \alpha } } _ { }$ great circle.

# 7.2Laplace's Method

The basic formulas for Laplace's method are

$$
\begin{array} { r } { \mathfrak { X } \overset { * } { \underset { \mathtt { f } } { \le } } \cdot \mathfrak { Z } = \rho \hat { \mathscr { P } } _ { \mathfrak { I } } , } \end{array}
$$

$$
\mathbf { r } ^ { \prime } + \mathbb { R } ^ { \prime } = \boldsymbol { \rho } ^ { \prime } \hat { \boldsymbol { \rho } } \stackrel { ! } { + } \boldsymbol { \rho } \hat { \boldsymbol { \rho } } ^ { \prime } ,
$$

$$
- \frac { \rho } { r ^ { 3 } } + \left( \frac { \mathbb { i } } { r ^ { 3 } } - \frac { 1 } { R ^ { 3 } } \right) \mathbb { R } = \rho ^ { \prime \prime } \hat { \rho } + 2 \rho ^ { \prime } \hat { \rho } ^ { \prime } + \rho \hat { \rho } ^ { \prime \prime } ,
$$

and

$$
\begin{array} { r } { \tau ^ { 2 } = \rho ^ { 2 } + \mathcal { R } ^ { 2 } - 2 \mathcal { R } \rho \cos \psi . } \end{array}
$$

Here we have chosen the unit of time to make k = 1,and the unit of mass to be the mass of the Sun. If the modified time is referred to as T,measured from some epoch $t _ { \updownarrow }$ then

$$
\tau = k \{ t - \dot { \tau } _ { 0 } \} .
$$

A prime will denote differentiation with respect to $\pmb { \tau }$

The observations furnish three values of p for three values of r. The four formulas given above represent exactly the geometrical and gravitational aspects of the motion. The initial approximation in Laplace's method involves finding values for p' and p" at some instant. Let this instant be to;then for smallr, $\hat { \pmb { \rho } }$ can be expanded bya Taylor seriesas

$$
\hat { \rho } = ( \hat { \rho } ) _ { \tau = 0 }  \tau ( \hat { \rho } ^ { \prime } ) _ { 0 } \div \frac { 1 } { 2 } \tau ^ { 2 } ( \hat { \rho } ^ { \prime \prime } ) _ { 0 } + \cdot \cdot \cdot
$$

If this series is truncated after the third term, then three observations are necessary to determine (')o and (p")o. These values are not exact, so that the observed positions (and therefore the geometry of the problem) will not be represented accurately. It is best to choose to as the arithmetic mean of the three times,so that the errors are minimized. (See problems 10 and 11 at the end of the section.)A simpler,but less satisfactory choice is to put $\ddagger _ { 0 }$ equal to time of the central observation. If more than three observations are available, we can,of course,find better values for $( \hat { \pmb { \rho } } ^ { \prime } ) _ { \hat { \pmb { \ 0 } } }$ and $( \hat { \pmb { \mathscr { P } } } ^ { \prime \prime } ) _ { \hat { \pmb { \jmath } } }$

Let us assume that $\hat { \rho } ^ { i }$ and $\hat { \mathcal { P } } ^ { \prime i }$ have been found. Taking $( \hat { \rho } \times \hat { \rho } ^ { \prime } )$ (7.2.3), we find

$$
\left( \frac { 1 } { r ^ { 3 } } - \frac { 1 } { R ^ { 3 } } \right) [ \hat { \rho } , \hat { \rho } ^ { \prime } , \mathbb { R } ] = \rho [ \hat { \rho } , \hat { \rho } ^ { \prime } , \hat { \rho } ^ { \prime \prime } ] ,
$$

an equation which is similar to (7.1.2). Also from (p × p")·(7.2.3), we find

$$
\left( \frac { \hat { \lambda } } { r ^ { 3 } } - \frac { 1 } { R ^ { 3 } } \right) [ \hat { \rho } , \hat { \rho } ^ { \prime \prime } , \mathbb { R } ] = - 2 \rho ^ { \prime } [ \hat { \rho } , \hat { \rho } ^ { \prime } , \hat { \rho } ^ { \prime \prime } ] .
$$

Assuming that (7.2.4) and (7.2.6) can be solved for r and p,(7.2.7) can then be solved for p.Then from (7.2.1) and (7.2.2),r and rcan be found,and the elements of the orbit can be calculated from these.

If these elements are then used to predict the positions at the times of observation the answers will not agree with the original observations. This is because we truncated the series (7.2.5). Some method must be found to improve the orbit,but before discussing this,we shallconsider in more detail the solution of (7.2.4) and （7.2.6) from a theoretical angle;their practical solution isdescribed in problem 4at the end of this section.

心 By eliminating $\mathfrak { F }$ ,we can obtain an algebraic equation of the eighth degree in p, but rather than attempting to solve this, it is easier to make the follwing substitutions. From the triangle SEC we have (see Figure 7.3)

$$
\frac { R } { \sin \phi } = \frac { r } { \sin \psi } = \frac { \rho } { \sin ( \phi + \psi ) } .
$$

Write（7.2.6） in the form

$$
\rho = A \left( \frac { \tt { j } } { R ^ { 3 } } - \frac { \tt { j } } { r ^ { 3 } } \right) ;
$$

then,using (7.2.8),we find

$$
R \sin \psi \cos \phi + \left( R \cos \psi - \frac { A } { R ^ { 3 } } \right) \sin \phi = - \frac { A } { R ^ { 3 } } \frac { \sin ^ { 4 } \phi } { \sin ^ { 3 } \psi } .
$$

in.order to simplify this,let

$$
\begin{array} { c } { { N \sin m = R \sin \psi , } } \\ { { N \cos m = R \cos \psi - \displaystyle \frac { A } { R ^ { 3 } } , } } \\ { { M = - \displaystyle \frac { N R ^ { 3 } } { A } \sin ^ { 3 } \psi , } } \end{array}
$$

where the sign $\mathcal { N }$ is chosen to make $\mathbb { M }$ positive. Substituting into (7.2.9） and simplifying,we find,eventually,

$$
\sin ^ { 4 } \phi = \tt \AA \sin ( \phi + \hbar \eta ) .
$$

The quantities M and m are known; assuming that a unique solution exists, 7.2.11) can be solved by successive approximations. (See problem 3 at the end f this section.)

It can easily be verified that the position of the observer satisfies the equations so that $\dot { \phi } = \pi - \psi$ is $^ \mathrm { a }$ solution that must be rejected.Also, from the geometry of the triangle $S E C ,$

$$
\phi < \pi - \psi .
$$

The solutions of (7.2.11) are the intersections of the curves

$$
_ { \tilde { y } _ { 1 } } = \sin ^ { \frac { 4 } { 3 } } \phi
$$

$$
y _ { 2 } = M \sin ( \phi + \pi z ) .
$$

Figure 7.5 shows these curves for m negative and $\mathbb { M }$ somewhat less than one. In this case there are three solutions,and in general we shall have either one orthree real solutions for lying between O and π. But if there is only one solution,it must be  = π-; then no solution is left for the comet and the Droblem has no meaning.

Consider the case when A is positive. Then r >R,and since sin is not negative, N must be negative; then m lies in the third or fourth quadrant. Figure 7.5 shows m in the fourth quadrant; as m decreases, the curve y2 slides to the right and there wil be a critical value of m,after which there is only one real solution (see problem 5). Since we require three roots,m certainly cannot be in the third quadrant.Similarly,if A is negative,it can be shown that m must certainly lie in the first quadrant.

Let the three roots be $\phi _ { 1 }$ ， $\phi _ { 2 }$ ，and $\phi _ { 3 }$ where $\dot { \varphi } _ { 1 } \leq \phi _ { 2 } \leq \dot { \varphi } _ { 3 }$ .If $\dot { \phi } _ { \mathtt { i } } = \pi - \mathfrak { P } _ { \mathtt { i } }$ the problem has no solution. If $\phi _ { 2 } = \pi - \psi$ ,there isa unique solution, $\phi _ { \ I }$ ; this can be found without difficulty by solving (7.2.11）.If $\phi _ { 3 } = \pi - \psi$ ，there are two possible solutions, $\phi _ { \ I }$ and $\dot { \phi } _ { 2 }$ It might be possible to judge between these, since one might require a solution for $\mathcal { F }$ which would be unreasonably large, but it may be necessary to use a fourth observation. In the latter case (7.2.11) might be formed for two choices of three dates from the four,having a common central date; the solution common to both would be used. (Or see problem 12 at the end of this section.)

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/6fc60170c9d733204ad6390f7995bce7595f091b67552aef237f485395984fc9.jpg)  
Figure 7.5

Suppose A to be positive. If there are three solutions, we see from Figure 7.5 that

$$
\frac { \partial \bar { \kappa } ( \phi _ { 2 } ) } { \partial \phi } > 0 .
$$

The derivatives at the other two roots are negative, so that for a unique solution it isnecessary and sufficient that

$$
\phi _ { 2 } = \pi - \psi
$$

and

$$
- \frac { 4 } { 5 } \sin ^ { 3 } \psi \cos \psi + \hat { M } \cos ( \psi - m ) > 0 .
$$

Using(7.2.10）,this becomes

$$
\frac { 4 M A \cos \psi } { N R ^ { 3 } } + \frac { M } { N } \left\{ \cos \psi \left( R \cos \psi - \frac { A } { R ^ { 3 } } \right) + R \sin ^ { 2 } \psi \right\} > 0
$$

$$
\frac { \partial F } { \partial \dot { \phi } } \equiv 4 \sin ^ { 3 } \phi \cos \phi - M \cos ( \phi + m ) .
$$

$$
\frac { \vec { M } R } { N } \left( 1 + \frac { 3 A \cos \psi } { R ^ { 4 } } \right) > 0 .
$$

Then, since $\pmb { \mathcal { N } }$ is negative, we have

$$
1 \div \frac { 3 A \cos \psi } { R ^ { 4 } } < 0 .
$$

；can be shown that the same condition holds if $A$ is negative

Consider the limiting case when

$$
1 \div \frac { 3 A \cos \psi } { B ^ { 4 } } = 0 .
$$

Eliminating cos $\tilde { \psi }$ by means of (7.2.4), and using (7.2.9), we find

$$
\rho ^ { 2 } = \tau ^ { 2 } + \frac { 2 } { 3 } \frac { \mathcal { R } ^ { 5 } } { \tau ^ { 3 } } - \frac { 5 } { 3 } \mathcal { R } ^ { 2 } .
$$

To find the condition for a unique solution, consider

$$
\dot { \mathcal { F } } ( \phi ) \equiv \sin ^ { 4 } \phi - M \sin ( \phi + \pi ) ,
$$

so that

This is the equation of a surface of revolution about the lirre $S \mathbb { E } .$ A section through SEis shownin Figure 7.6. The sign of the left-hand side of(7.2.12) changes on crossing the surface,and it can be verified that the inequality is satisfied in the shaded areas of the figure.

We shall next consider the problem of improving the approximate orbit. Now that we have approximate valuesofor $\boldsymbol { \beta }$ we can adjust for parallax and forplanetary aberration.But the adjustments will not affect the discrepancies between the computed and observed positions for the first and third times of observation,and the removal of these is the main problem. The method given below is due to Leuschner. We assume $\ddagger _ { \Updownarrow }$ ,the time of approximation using （7.2.5） to be the central, or second, time of observation.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0081-0120/ocr/images/6cc584b7934298f08c2beba63b9e6d03cc642a12525514526461fdc0a0a35faf.jpg)  
Figure 7.6

To find the predicted right ascension and declination for the two times of observation, we use the f and $\mathbf { g }$ functions,

$$
\mathfrak { r } = \mathfrak { f r } _ { \Omega } \div \mathfrak { g r } _ { \Omega } ^ { \sharp }
$$

to find the values of r. $\sum q$ and ${ \boldsymbol { \Sigma } } _ { \boldsymbol { \mathfrak { 0 } } } ^ { \prime }$ apply to the second observation and are known.） Then we use the formulas (6.16.2) and (6.16.3) to find $\alpha$ and $\delta$ Let the subscripts $\ddagger$ and $\mathfrak { z }$ apply to the first and third times of observation,and let $\Delta \alpha _ { 1 }$ and $\Delta \delta _ { \ I }$ ， etc.,be the discrepancies between the observed and calculated values in the sense that they are corrections to be added to the calculated values. We then have four residuals, $\Delta \alpha _ { \bar { 1 } } , \Delta \delta _ { \bar { 1 } } , \Delta \alpha _ { 3 } .$ and $\Delta \delta _ { 3 }$

The errors in r stem from an incorrect value of $\boldsymbol { \rho }$ while those in $\gamma ^ { \prime }$ are due to a variety of causes; hence we want to find corrections $\Delta \rho$ and $\Delta \mathbf { \vec { z } } ^ { \prime }$ (four in all) in terms of the four residuals. $\Re$ is,of course,not affected; so,from (7.2.1) we have, in general,

$$
\Delta \mathfrak { r } = \Delta \rho = \Delta \rho \hat { \varrho } \div \rho \Delta \hat { \varrho } .
$$

Multiply by $= 0$ ：then

$$
\Delta \rho = \hat { \rho } \cdot \Delta \mathbf { r }
$$

$$
\rho { \mit \Delta } \hat { \beta } = { \mit \Delta } \tt { r } - \hat { \beta } \big ( \hat { \beta } \cdot { \mit \Delta } \tt { r } \big ) .
$$

△r here is the correction to be applied to $\pmb { \mathbb { z } }$ If we assume that all corrections are of the first order of small quantities, and we neglect their squares and products,

we find,from the equation of motion for the comet,

$$
\mathtt { r } ^ { i \mathrm { \prime } } \overset { . } { \ + } \Delta \mathtt { r } ^ { \prime \prime } = - \frac { \mathtt { r } } { \tau ^ { 3 } } - \frac { \Delta \mathtt { r } } { \tau ^ { 3 } } + 3 \mathtt { r } \frac { \Delta \mathtt { r } } { \tau ^ { 4 } } ,
$$

so.that

$$
\Delta \boldsymbol { \mathrm { r } } ^ { \prime \prime } = - \frac { \Delta \boldsymbol { \mathrm { r } } } { r ^ { 3 } } + 3 \boldsymbol { \mathrm { r } } \frac { \Delta \boldsymbol { r } } { r ^ { 4 } } .
$$

But from (7.2.4),

$$
r \Delta r = ( \rho - R \cos \psi ) \Delta \rho .
$$

Now let △r" be evaluated at the time of the second observation, when △p=0; so $\Delta \hat { \mathbf { z } } = \hat { \pmb { \rho } } \Delta \rho$ Then

$$
\begin{array} { l } { \Delta \mathbf { r } ^ { \prime \prime } = \left\{ - \frac { \hat { \boldsymbol { \rho } } } { r ^ { 3 } } + \frac { 3 \mathbf { r } } { r ^ { 5 } } ( \boldsymbol { \rho } - \mathcal { R } \cos \psi ) \right\} \Delta \boldsymbol { \rho } } \\ { = \mathbb { H } \Delta \boldsymbol { \rho } , \quad \mathrm { s a y } . } \end{array}
$$

$$
\begin{array} { r } { \Delta \mathfrak { r } _ { 1 } = \Delta \mathfrak { r } + \Delta \mathfrak { r } ^ { \prime } \tau _ { 1 } + \frac { 1 } { 2 } \Delta \mathfrak { r } ^ { \prime \prime } \tau _ { 1 } ^ { 2 } + \cdot \cdot \cdot . . } \end{array}
$$

and,ignoring terms of the order $\boldsymbol { \mathfrak { F } } _ { \mathtt { I } } ^ { 3 }$ we have

$$
\begin{array} { r } { \Delta \mathbf { r } _ { \mathrm { 1 } } = ( \hat { \pmb { \rho } } \ + \frac { 1 } { 2 } \mathbf { \mathbb { H } } \tau _ { \mathrm { 1 } } ^ { 2 } ) \Delta \boldsymbol { \rho } \div \boldsymbol { \tau } _ { \mathrm { 1 } } \Delta \mathbf { r } ^ { \prime } . } \end{array}
$$

Substituting into (7.2.15), we have the three equations that are components of

$$
\rho _ { 1 } \Delta \hat { \rho } _ { \perp } = \Delta \mathbf { r } _ { \perp } - \hat { \rho } _ { 1 } ( \hat { \rho } _ { 1 } \cdot \Delta \mathbf { r } _ { \perp } )
$$

for the first time of observation,and another three for the third.The residuals △pand△are kmown（if we letp=(λ,μ,v），they are△i,△p1,△v1,etc.）， and it appears for a moment that we have six equations for the four unknowns Ap and △r'. But the six equations are not independent, and it is better to work with the residuals $\Delta \alpha$ and $\Delta \delta$ where we have

$$
\begin{array} { r l } & { \cos ^ { 2 } \delta _ { 1 } \Delta \alpha _ { 1 } = \lambda _ { 1 } \Delta \mu _ { 1 } - \mu _ { 1 } \Delta \lambda _ { 1 } , } \\ & { \phantom { \cos ^ { 2 } \delta _ { 1 } \Delta \alpha _ { 1 } = } \cos \delta _ { 1 } , } \\ & { \cos ^ { 2 } \delta _ { 3 } \Delta \alpha _ { 3 } = \lambda _ { 3 } \Delta \mu _ { 3 } - \mu _ { 3 } \Delta \lambda _ { 3 } , } \\ & { \phantom { \cos ^ { 2 } \delta _ { 3 } \Delta \alpha _ { 3 } = \lambda _ { 1 } \Delta \alpha _ { 1 } = \lambda _ { 2 } \Delta \nu _ { 3 } . } } \end{array}
$$

Substituting from （7.2.19) for the components $\Delta \lambda _ { 1 } , \Delta \mu _ { 1 } , \Delta \nu _ { \mathrm { i } } .$ and doing the same for the third observation,we have four linear simultaneous equations for theunknowns $\Delta \rho$ and $\Delta \bar { \mathbf { z } ^ { \prime } }$ and these can be solved by the use of a program like the one listed in Appendix E.

If these residuals are applied as corrections to the original values of r and abetter orbit will have been found, but it may still not be successful in predicting the observations for the first and third dates; however, the residuals should be less than they were in the first place. The entire process can now be


<!-- chunk 0004: pages 121-160 -->
repeated and this is continued until the residuals become negligible. It should be noted that once the equations (7.2.20) have been set up, the coefficients of △pand △r' will not vary through the successive approximations,so that later approximations can be accomplished relatively easily.

If extra observations are available, more residuals can be found;we are then able to set up more equations than there are unknowns, and these can be solved by the method of least squares. The resulting corrections to the orbit arise from data of more than three observations and are therefore more dependable than those found above. Observations over a longer arc can be used $\mathbf { \widehat { \widehat { a } } _ { 2 } ^ { \varepsilon } } ,$ instead of the truncated series (7.2.17),the $\hat { \pmb f }$ and $g$ functions are used, so that

$$
\Delta \mathbf { r } = \mathbf { r } _ { 0 } \Delta f + \mathbf { r } _ { 0 } ^ { \prime } \Delta g + f \Delta \mathbf { r } _ { 0 } + g \Delta \mathbf { r } _ { 0 } ^ { \prime } .
$$

The resulting equations are more complicated than those described above; they are given by Herget (Ref. 24).

# Problems

1. Show how the value of $\cos \phi$ can be calculated directly from the observationsand from appropriate tables.   
2.Discuss the problem of orbit determination,using (7.2.6) instead of(7.1.2). Show the relationships between the determinants of (7.2.6)and quantities such as K or $\sum \cdot \hat { \mathbf { u } }$   
3.Consider the solution (7.2.11). If an approximate value $\phi _ { \Game }$ is found,show that a correction $\Delta \phi _ { \mathfrak { V } }$ can be calculated from

$$
\Delta \phi _ { 0 } = - \frac { \sin ^ { 4 } \phi _ { 0 } - M \sin ( \phi _ { 0 } + m ) } { 4 \sin ^ { 3 } \phi _ { 0 } \cos \phi _ { 0 } - M \cos ( \phi _ { 0 } + m ) } .
$$

Discuss the case when the denominator is small.

4. Show that the equations (7.2.4) and (7.2.6) can be solved by substituting trial values of $\beta$ into（7.2.4） to find $\mathfrak { F }$ and then substituting this value of $\gamma$ into（7.2.6） to find $\beta$ Use this method to solve

$$
\begin{array} { c } { { r ^ { 2 } = 0 . 9 7 3 4 + 1 . 1 4 9 3 \rho + \rho ^ { 2 } , } } \\ { { \rho = 2 . 7 0 3 - \displaystyle \frac { 2 . 5 9 6 } { r ^ { 3 } } . } } \end{array}
$$

(The answer is $\beta = 2 . 6 3 1 .$

5.Show that the condition for (7.2.1l) to have a double root is

$$
4 \sin ^ { 3 } \phi \cos \phi - \hat { M } \cos ( \phi + m ) = 0 .
$$

Hence show that $\yen 1$ should satisfy the inequality

$$
9 - \mathtt { i } 6 \mathtt { t a m } ^ { 2 } \mathfrak { m } \ge \mathbb { 0 } ,
$$

for there to be a possible solution to the problem,and find the possible limits of m and the corresponding limits of . Finally show that the maximum value of M which can result in (7.2.11) having three real roots isapproximately1.431.

6.Derive the inequality (7.2.12） when $A$ is negative.

7. Show that the left-hand side of (7.2.12) changes sign on crossing a boundary in Figure 7.6,and that the solution for p is unique in the shaded region of the figure.

8.Find the octic equation for $\beta _ { 2 }$ by eliminating $\mathfrak { F } _ { 2 }$ between (7.2.4） and (7.2.6).

9.Consider the solution of (7.2.4) and (7.2.6) as follows: take, for convenience, $R = \sharp$ and(7.2.6)in the form

$$
i \rho = 1 - { \frac { 1 } { r ^ { 3 } } } .
$$

Eliminate p, obtaining an octic in r,in which the coefficients of ri for $i = 1 , 2 , 4 , 5 , 7$ are zero. Show that if the coefficient of $z ^ { 8 }$ is positive,then that of $\gamma ^ { 6 }$ is negative and that of $\mathfrak { r } ^ { 3 }$ is positive. Hence, from the theory ofequations, show that the octic has three positive,one negative,and four complex roots.Show that r=1 is a real root,and that if the other two positive roots lie on either side of 1, then it is possible to distinguish between them in the solution. Show that the condition for this is that

$$
\{ \{ \{ i = 3 \cos \psi \} < \{ \} .
$$

10.Suppose we have three observations of $\lambda , \lambda _ { 1 } , \lambda _ { 2 }$ ,and $\lambda _ { 3 } ,$ and that values $\lambda _ { G } , \lambda _ { G } ^ { \ell }$ and $\lambda _ { \Updownarrow } ^ { a i }$ ,for time $\ddagger _ { 0 }$ are found by assuming

$$
\lambda = \lambda _ { 0 } + \lambda _ { 0 } ^ { \prime } \tau _ { \bar { 0 } } + { \textstyle { \frac { 1 } { 2 } } } \lambda _ { 0 } ^ { \prime \prime } \tau _ { \bar { 0 } } ^ { 2 } .
$$

Better values, $\lambda _ { 0 } \mathrel { + } \Delta \lambda _ { \perp }$ , etc., would be found if we could'assume

$$
\begin{array} { r } { \lambda = \lambda _ { 0 } + \lambda _ { 0 } ^ { \prime } \tau _ { 0 } + \frac { 1 } { 2 } \lambda _ { 0 } ^ { \prime \prime } \tau _ { 0 } ^ { 2 } + \frac { 1 } { 6 } \lambda _ { 0 } ^ { \prime \prime \prime } \tau _ { 0 } ^ { 3 } + \frac { 1 } { 2 4 } \lambda _ { 0 } ^ { \prime \prime \prime \prime } \tau _ { 0 } ^ { 4 } . } \end{array}
$$

Find $\Delta \lambda _ { 0 } , \Delta \lambda _ { \theta } ^ { i }$ and $\Delta \lambda _ { 0 } ^ { \prime \prime }$ in terms of $\lambda _ { \Updownarrow } ^ { \prime \prime \prime }$ and $\lambda _ { \Updownarrow } ^ { \prime \prime \prime 4 }$ ,and discuss the errors involved in finding $\lambda _ { \Updownarrow } , \lambda _ { \Updownarrow } ^ { \prime }$ ,and $\lambda _ { \Updownarrow } ^ { \prime \prime }$ from three observations (of which $t _ { \Updownarrow }$ need not be $\clubsuit$ time of observation).Show that the error in $\lambda _ { \mathrm { 0 } } ^ { \prime \prime }$ isminimized f

$$
\begin{array} { r } { \tau _ { 1 } \div \tau _ { 2 } ^ { \circ } \div \tau _ { 3 } = \Omega . } \end{array}
$$

and find the corresponding value of $\ddagger _ { \mathfrak { V } }$

repeated and this is continued until the residuals become negligible. It should be noted that once the equations (7.2.20) have been set up, the coefficients of △p and △r' will not vary through the successive approximations, so that later approximations can be accomplished relatively easily.

If extra observations are available, more residuals can be found;we are then able to set up more equations than there are unknowns,and these can be solved by the method of least squares. The resulting corrections to the orbit arise from data of more than three observations and are therefore more dependable than those found above. Observations over a longer arc can be used if, instead of the truncated series (7.2.17),the $f$ and $g$ functions are used, so that

$$
\Delta \mathbf { r } = \mathbf { r } _ { 0 } \Delta f + \mathbf { r } _ { 0 } ^ { \prime } \Delta g + f \Delta \mathbf { r } _ { 0 } + g \Delta \mathbf { r } _ { 0 } ^ { \prime } .
$$

The resulting equations are more complicated than those described above; they are given by Herget (Ref. 24).

# Problems

1. Show how the value of $\cos \psi$ can be calculated directly from the observations and from appropriate tables.

2.Discuss the problem of orbit determination, using (7.2.6) instead of(7.1.2). Show the relationships between the determinants of (7.2.6) and quantities such as $\kappa$ or $\sum \cdot \hat { \mathbf { n } }$

3.Consider the solution (7.2.11). If an approximate value $\$ 9$ is found,show that a correction $\Delta \phi _ { \Theta }$ can be calculated from

$$
\Delta \phi _ { 0 } = - \frac { \sin ^ { 4 } \phi _ { 0 } - M \sin ( \phi _ { 0 } + m ) } { \frac { 4 } { 4 } \sin ^ { 3 } \phi _ { 0 } \cos \phi _ { 0 } - M \cos ( \phi _ { 0 } + m ) } .
$$

Discuss the case when the denominator is small.

4. Show that the equations (7.2.4) and (7.2.6) can be solved by substituting trial values of $\beta$ into (7.2.4） to find $\mathfrak { P }$ and then substituting this value of $\ P$ into （7.2.6） to find $\beta$ Use this method to solve

$$
\begin{array} { l } { { \displaystyle { r ^ { 2 } = 0 . 9 7 3 4 + \frac { 1 . 1 4 9 3 \rho + \rho ^ { 2 } } { r ^ { 3 } } } , } } \\ { { \displaystyle { \rho = 2 . 7 0 3 - \frac { 2 . 5 9 6 } { r ^ { 3 } } } . } } \end{array}
$$

(The answer is ${ \mathfrak { P } } = 2 . 6 3 1 .$

5.Show that the condition for (7.2.11) to have a double root is

$$
4 \sin ^ { 3 } \phi \cos \phi - M \cos ( \phi \div m ) = 0 .
$$

Hence show that $\yen 3$ should satisfy the inequality

$$
9 - 1 6 \tan ^ { 2 } { \mathfrak { s u } } \geq 0 ,
$$

for there to be a possible solution to the problem,and find the possible limits of m and the corresponding limits of \$. Finally show that the maximum value of M which can result in (7.2.11) having three real roots isapproximately1.431.

6.Derive the inequality (7.2.12) when A is negative.

7. Show that the left-hand side of (7.2.12) changes sign on crossing a boundary in Figure 7.6,and that the solution for p is unique in the shaded region of the figure.

8.Find the octic equation for $\beta _ { 2 }$ by eliminating $r _ { 2 }$ between (7.2.4） and (7.2.6).

9.Consider the solution of(7.2.4) and (7.2.6) as follows:take, for convenience, $\mathcal { R } = \mathbb { 1 }$ and(7.2.6)in the form

$$
i \rho = 1 - { \frac { \frac { 1 } { 3 } } { \pi ^ { 3 } } } .
$$

Eliminate p, obtaining an octic in r, in which the coefficients of r for i=1,2,4,5,7 are zero. Show that if the coefficient of r is positive, then that of $r ^ { 6 }$ is negative and that of $\gamma ^ { 3 }$ is positive.Hence, from the theory of eguations,show that the octic has three positive,one negative，and four complex roots.Show that r=1 isa real root,and that if the other two positive roots lie on either side of 1,then it is possible to distinguish between them in the solution. Show that the condition for thisis that

$$
\{ ( \bar { \iota } - 3 \cos \psi ) < \mathbb { G } .
$$

10.Suppose we have three observations of λ, X1, X2，and Ag,and that values $\lambda _ { \Updownarrow } , \lambda _ { \Updownarrow } ^ { \prime }$ ,and $\lambda _ { 0 } ^ { \prime \prime }$ ,for time $t _ { \mathbb { G } }$ are found by assuming

$$
\lambda = \lambda _ { 0 } + \lambda _ { 0 } ^ { \prime } \tau _ { 0 } \div \frac { 1 } { 2 } \lambda _ { 0 } ^ { \prime \prime } \tau _ { 0 } ^ { 2 } .
$$

Better values, $\lambda _ { \Updownarrow } + \Delta \lambda _ { \Updownarrow }$ , etc., would be found if we could' assume

$$
\begin{array} { r } { \lambda = \lambda _ { 0 } + \lambda _ { 0 } ^ { \prime } \tau _ { 0 } + \frac { 1 } { 2 } \lambda _ { 0 } ^ { \prime \prime } \tau _ { 0 } ^ { 2 } + \frac { 1 } { 6 } \lambda _ { 0 } ^ { \prime \prime \prime } \tau _ { 0 } ^ { 3 } + \frac { 1 } { 2 4 } \lambda _ { 0 } ^ { \prime \prime \prime \prime } \tau _ { 0 } ^ { 4 } . } \end{array}
$$

Find $\Delta \lambda _ { 0 } , \Delta \lambda _ { 0 } ^ { \prime } ,$ and $\Delta \lambda _ { \Updownarrow } ^ { \prime \prime }$ in terms of $\lambda _ { 0 } ^ { i j t }$ and $\lambda _ { \Omega } ^ { \prime f \beta \prime }$ , and discuss the errors involved in finding $\lambda _ { \Updownarrow } , \lambda _ { \Updownarrow } ^ { \ 3 }$ and $\lambda _ { \Updownarrow } ^ { \prime \prime }$ from three observations (of which $t _ { 0 }$ need not bea time of observation). Show that the error in $\lambda _ { \textcircled { 7 } } ^ { 7 7 }$ isminimized if

$$
\tau _ { 1 } \div \tau _ { 2 } ^ { \circ } \div \tau _ { 3 } = 0
$$

and find the corresponding value of $\ddagger _ { 0 }$

11. Suppose we have four observations of X from which we want to find values ofXo,X and X.Show that the error in X is minimized if

$$
\sum _ { i < j = 1 } ^ { 4 } \tau _ { i } \tau _ { j } = 0 .
$$

Show that this leads to a quadratic in $\ddagger _ { 0 }$ with real roots.

12.Given four observations, show that $\beta$ can be found in the following way. From(7.2.6) and (7.2.7) we can find an expression of the form $\boldsymbol { \rho } ^ { \prime } = \boldsymbol { \mathcal { B } } \boldsymbol { \rho }$ ： B depends on the derivatives of the direction cosines up to the second. Now,by differentiating this,we find p"=(B'+B²)p；B' involves third derivatives, but these can be found from four observations. Now find another relation between $\boldsymbol { \rho }$ and $\rho ^ { \prime \beta }$ $\left( 1 3 \dot { 1 } \eta \ g \ 7 . 2 . 3 \right) _ { . }$ of the form ${ \rho ^ { \prime } } ^ { \prime } = C + D \rho$ Hence solve for $p$ by eliminating $\rho ^ { \prime \prime }$

13.Find approximations for the first and second derivatives of the direction cosines for the time of the second observation for the following set of observations:

Nov. 7.8205+0.902897 $+ 0 . 0 6 0 6 0 6$ +0.425562   
Nov.26.7480+0.922476+0.051857 +0.382554   
Dec.18.6262 $+ 0 . 9 3 4 7 6 8$ $\pm 0 . 0 8 0 2 2 7$ $+ 0 . 3 4 6 0 8 0$

$$
\begin{array} { c c c } { { \lambda = + 0 . 0 2 4 \ 9 2 \lambda } } & { { \mu \ - \ + 0 . 0 2 0 \cup 0 0 } } & { { \nu \ - \ - \textsc { { o . } } \mathrm { { . } } \mathrm { { . } } \mathrm { { . } } \mathrm { { . } } \mathrm { { . } } \mathrm { { } } } } \\ { { \lambda ^ { \prime \prime } = - 0 . 0 7 8 2 5 0 } } & { { \mu ^ { \prime \prime } = + 0 . 2 9 1 3 3 9 } } & { { \nu ^ { \prime \prime } = + 0 . 1 0 0 \ 2 5 \bar { { \sf { 1 } } } . \mathrm { { . } } \mathrm { { . } } } } \end{array}
$$

14.If the apparent path of a body on the celestial sphere hasa point of inflection,show that the tangent at that point passes through the Sun.

# 7.3 Gauss'Method

“Gauss'method” is a phrase applied to a class of methods originating with the ideas of Gauss,and further evolved by Gauss and many others. Two modern variants will be described here; they are based ona discussion byB.G.Marsden (Ref.41） whom Iwould like to thank for his help and suggestions concerning the material for this section.After nearly two hundred years of polishing in the hands of experts,Gauss'method now forms one of the most beautiful structures in celestial mechanics.

The method starts with the geometrical condition that the vectors $\pmb { \tilde { z } } _ { \mathfrak { T } }$ ， $\pmb { \Sigma } _ { 2 }$ and $\yen 3$ liein a plane.Consequently,there exist scalars $c _ { \tt I }$ and $c _ { 3 }$ ,independent ofthe coordinate system used, such that

$$
\begin{array} { r } { \mathfrak { r } _ { 2 } \equiv c _ { \frac { 1 } { 2 } } \mathfrak { r } _ { \frac { 3 } { 2 } } + c _ { 3 } \mathfrak { r } _ { 3 } . } \end{array}
$$

To introduce the dynamics,let

$$
\begin{array} { r } { \mathbf { r } _ { 1 } = f _ { 1 } \mathbf { r } _ { 2 } + g _ { 1 } \mathbf { v } _ { 2 } , } \\ { \mathbf { r } _ { 3 } = f _ { 3 } \mathbf { r } _ { 2 } + g _ { 3 } \mathbf { v } _ { 2 } , } \end{array}
$$

from which

$$
{ \mathfrak { r } } _ { 2 } = c _ { 1 } ( f _ { 1 } { \mathfrak { r } } _ { 2 } + g _ { 1 } { \mathfrak { v } } _ { 2 } ) + c _ { 3 } ( f _ { 3 } { \mathfrak { r } } _ { 2 } + g _ { 3 } { \mathfrak { v } } _ { 2 } ) .
$$

Ifthis is successively multiplied by $\times \ y _ { 2 }$ and $\pmb { \Sigma } _ { 2 } \times$ ,then there result

$$
{ \begin{array} { l l l } { { \ddot { \downarrow } } = c _ { \downarrow } f _ { \updownarrow } + c _ { \mathrm { 3 } } f _ { \mathrm { 3 } } } & { { \mathrm { a n d } } } & { 0 = c _ { \mathrm { 1 } } g _ { \updownarrow } + c _ { \mathrm { 3 } } g _ { \mathrm { 3 } } , } \end{array} }
$$

from which

and

$$
\begin{array} { l } { { c _ { 1 } = \frac { g _ { 3 } } { f _ { 1 } g _ { 3 } - g _ { 1 } f _ { 3 } } , } } \\ { { } } \\ { { c _ { 3 } = - \frac { g _ { 1 } } { f _ { 1 } g _ { 3 } - g _ { 1 } f _ { 3 } } . } } \end{array} \left] ~ \right.
$$

Alternative expressions for $c _ { \vec { \mathbf { i } } }$ and $c _ { 3 }$ involve Gauss’ sector-triangle ratios. Let ri,rjl denote the area of the triangle formed by $\pmb { \Sigma } _ { i }$ and $\sum j$ and $( \ I _ { i } , \ I _ { j } )$ the orbital area swept out by the radius vector between the two vectors. Then

$$
{ \begin{array} { r l } & { c _ { 1 } = { \frac { \left| \mathbf { r } _ { 2 } \times \mathbf { r } _ { 3 } \right| } { \left| \mathbf { r } _ { 1 } \times \mathbf { r } _ { 3 } \right| } } = { \frac { \left[ \mathbf { r } _ { 2 } , \mathbf { r } _ { 3 } \right] } { \left[ \mathbf { r } _ { 1 } , \mathbf { r } _ { 3 } \right] } } } \\ & { } \\ & { c _ { 3 } = { \frac { \left| \mathbf { r } _ { 1 } \times \mathbf { r } _ { 2 } \right| } { \left| \mathbf { r } _ { 1 } \times \mathbf { r } _ { 3 } \right| } } = { \frac { \left[ \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } \right] } { \left[ \mathbf { r } _ { 1 } , \mathbf { r } _ { 3 } \right] } } . } \end{array} }
$$

$$
y _ { 1 } = { \frac { ( \mathbf { r } _ { 2 } , \mathbf { r } _ { 3 } ) } { [ \mathbf { r } _ { 2 } , \mathbf { r } _ { 3 } ] } } , \quad y _ { 2 } = { \frac { ( \mathbf { r } _ { 1 } , \mathbf { r } _ { 3 } ) } { [ \mathbf { r } _ { 1 } , \mathbf { r } _ { 3 } ] } } , \quad y _ { 3 } = { \frac { ( \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } ) } { [ \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } ] } } .
$$

$$
c _ { 1 } = { \frac { ( { \mathfrak { r } } _ { 2 } , { \mathfrak { r } } _ { 3 } ) } { ( { \mathfrak { r } } _ { 1 } , { \mathfrak { r } } _ { 3 } ) } } { \frac { [ { \mathfrak { r } } _ { 2 } , { \mathfrak { r } } _ { 3 } ] } { ( { \mathfrak { r } } _ { 2 } , { \mathfrak { r } } _ { 3 } ) } } { \frac { ( { \mathfrak { r } } _ { 1 } , { \mathfrak { r } } _ { 3 } ) } { [ { \mathfrak { r } } _ { 1 } , { \mathfrak { r } } _ { 3 } ] } } \quad \quad .
$$

the same way,

$$
\begin{array} { r } { = \frac { \left( t _ { 3 } - t _ { 2 } \right) } { \left( t _ { 3 } - t _ { 1 } \right) } \frac { y _ { 2 } } { y _ { 1 } } . } \\ { c _ { 3 } = \frac { \left( t _ { 2 } - t _ { 1 } \right) } { \left( t _ { 3 } - t _ { 1 } \right) } \frac { y _ { 2 } } { y _ { 3 } } . } \end{array}
$$

In deriving these formulas we have used the law of areas. Introducing the observer into (7.3.1),we have

$$
c _ { 1 } \rho _ { 1 } \hat { \rho } _ { 1 } - \rho _ { 2 } \hat { \rho } _ { 2 } + c _ { 3 } \rho _ { 3 } \hat { \rho } _ { 3 } = c _ { 1 } \mathbb { R } _ { 1 } - \mathbb { R } _ { 2 } + c _ { 3 } \mathbb { R } _ { 3 } .
$$

Similarly, from equations (7.3.2),

$$
\begin{array} { r l r } & { } & { f _ { \hat { \mathbb { Z } } } \mathbb { r } _ { 2 } + g _ { \hat { \mathbb { Z } } } \mathbb { v } _ { 2 } = \rho _ { \hat { \mathbb { Z } } } \hat { \pmb { \rho } } _ { \hat { \mathbb { Z } } } - \mathbb { R } _ { 1 } , ] } \\ & { } & { = \rho _ { 2 } \hat { \pmb { \rho } } _ { 2 } - \mathbb { R } _ { 2 } , } \\ & { } & { f _ { 3 } \mathbb { r } _ { 2 } + g _ { 3 } \mathbb { v } _ { 2 } = \rho _ { 3 } \hat { \pmb { \rho } } _ { 3 } - \mathbb { R } _ { 3 } . . } \end{array}
$$

We shall see shortly that one way to determine the orbit is to solve the three scalar equations in (7.3.8) for the three geocentric distances using approximations for c1 and cg.These equations will be illconditioned; before being treated numerically, they will be changed to a triangular form using a beautiful geometrical transformation due to L.E. Cunningham. We introduce axes 8,n and G,with the -axis pointing toward the frst observed position (i.e., parallel to Pi,so that = pi), and so that the direction of the third observation,p, intersects the positive -axis. See Figure 7.7.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/b94caafabedbf08f205909ee23a83921cb7dafa2faaff21fe75e2ed7886b241d.jpg)  
Figure 7.7

Then

$$
\begin{array} { r } { \hat { \eta } = \frac { \hat { \rho } _ { 1 } \times \{ \hat { \rho } _ { 3 } \times \hat { \rho } _ { \frac { 1 } { 2 } } \} } { | \hat { \rho } _ { 1 } \times ( \hat { \rho } _ { 3 } \times \hat { \rho } _ { \frac { 1 } { 2 } } ) | } \cdot \cdot } \\ { = \frac { \hat { \rho } _ { 3 } - \hat { \rho } _ { 1 } ( \hat { \rho } _ { 3 } \cdot \hat { \rho } _ { 1 } ) } { \sqrt { 1 - ( \hat { \rho } _ { 3 } \cdot \hat { \rho } _ { 1 } ) ^ { 2 } } } , } \end{array}
$$

and

$$
\hat { \zeta } = \hat { \xi } \times \hat { \mathfrak { g } } .
$$

Let us define a rotation matrix RM having as its rows the components of $\sum \limits _ { i = 1 } ^ { 2 } \widehat { \pi }$ and $\hat { \pmb \zeta }$ If some vector is resolved initially in the equatorial system (and written as a column),then premultiplication by RM will give its components inthe new system.All vectors in (7.3.8) and (7.3.9) must be resolved in this way.In particular, the components of the unit vectors in the directions of the observations become

$$
\hat { \boldsymbol { \hat { \rho } } } _ { 1 } = \left[ \begin{array} { l } { \lambda _ { 1 } } \\ { \mu _ { 1 } } \\ { \nu _ { 1 } } \end{array} \right] = \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \end{array} \right] , \quad \hat { \boldsymbol { \rho } } _ { 2 } = \left[ \begin{array} { l } { \lambda _ { 2 } } \\ { \mu _ { 2 } } \\ { \nu _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { \hat { \boldsymbol { \rho } } _ { 2 } \cdot \hat { \boldsymbol { \xi } } } \\ { \hat { \boldsymbol { \rho } } _ { 2 } \cdot \hat { \boldsymbol { \eta } } } \\ { \hat { \boldsymbol { \rho } } _ { 2 } \cdot \hat { \boldsymbol { \zeta } } } \end{array} \right] , \quad \hat { \boldsymbol { \rho } } _ { 3 } = \left[ \begin{array} { l } { \lambda _ { 3 } } \\ { \mu _ { 3 } } \\ { \nu _ { 3 } } \end{array} \right] = \left[ \begin{array} { l } { \hat { \boldsymbol { \rho } } _ { 3 } \cdot \hat { \boldsymbol { \xi } } } \\ { \hat { \boldsymbol { \rho } } _ { 3 } \cdot \hat { \boldsymbol { \eta } } } \\ { \hat { \boldsymbol { \mathbb { 0 } } } } \end{array} \right] .
$$

(Inthe program listing that follows, the equatorial components of these vectors form the rows of a matrix RH. The components just found are called L(I)，M(I) and N(I） for $\vec { \underline { { { \tau } } } } \ = \ \mathbf { \textstyle \frac { 3 } { 4 } } , 2 , 3 .$ ）

The first treatment of these equations is characterized by Marsden as the “Gauss-Encke-Merton method”or simply by GEM, giving credit to the principal contributors.The operations start with approximations to $c _ { I }$ and $c _ { 3 }$ .The most primitive approximation uses just the opening terms in the $f$ and $g$ series, (6.7.11). Let

$$
\begin{array} { r } { \tau _ { 1 } = k ( t _ { 1 } - t _ { 2 } ) , \quad \tau _ { 2 } = k ( t _ { 3 } - t _ { 1 } ) , \quad \tau _ { 3 } = k ( t _ { 3 } - t _ { 2 } ) . } \end{array}
$$

Then for the first approximation, put

$$
c _ { 1 } = \frac { \tau _ { 3 } } { \tau _ { 3 } - \tau _ { 1 } } , ~ c _ { 3 } = - \frac { \tau _ { 1 } } { \tau _ { 3 } - \tau _ { 1 } } .
$$

Gauss’method has been criticized (see Ref. 30) as being weak, or even invalid, because of the limited convergence of the $f$ and $g$ series,expanded in powers ofthe time. But these series are irrelevant for most purposes today. After aninitial approximation,such as (7.3.14),needed to get things started,the rigorous expressions(7.3.7） for $\mathbb { C } _ { \mathfrak { T } }$ and $c _ { 3 }$ will be used.

We address equation (7.3.8). From the $\zeta$ component, using (7.3.12), we have

$$
- \rho _ { 2 } \nu _ { 2 } = c _ { 1 } Z _ { \frac { 1 } { 2 } } - Z _ { 2 } \div c _ { 3 } Z _ { 3 } .
$$

$\hat { \rho } _ { 2 }$ can be found in terms of $\pmb { C } \mathbf { 1 }$ and $c _ { 3 }$ as

$$
\rho _ { 2 } = \frac { - c _ { 1 } Z _ { 1 } + Z _ { 2 } - c _ { 3 } Z _ { 3 } } { \nu _ { 2 } } .
$$

Note the division by $y _ { 2 }$ . The magnitude of $z _ { 2 }$ is a measure of the departure of the observed arc from a great circle; if it is too small then there is little hope of finding a useful orbit from the observations. From the $\Im$ component of （7.3.8） we find

$$
\rho _ { 3 } = { \frac { \rho _ { 2 } \mu _ { 2 } + c _ { \mathrm { { i } } } Y _ { 1 } - Y _ { 2 } + c _ { 3 } Y _ { 3 } } { c _ { 3 } \mu _ { 3 } } } .
$$

Finally, from the $\boldsymbol { \xi }$ -component,

$$
\rho _ { \hat { z } } = { \frac { \rho _ { 2 } \lambda _ { 2 } - c _ { 3 } \rho _ { 3 } \lambda _ { 3 } + c _ { \hat { z } } { X _ { \hat { z } } } - { X _ { 2 } } \pm c _ { 3 } { X _ { 3 } } } { c _ { \hat { z } } } } .
$$

We have simply solved (7.3.8), transformed into triangular form, by back substitution.

With these values for the geocentric distances, the heliocentric vectors $\Xi _ { i }$ can be found from r = p:-Ri. The program must have a subroutine similar to the program in section 6.12 for calculating the sector triangle ratio,y. Then (7.3.6) and (7.3.7) are used to find new values for c1 and c2,and the cycle of calculations is repeated. The operation may end in disaster;it is not a bad idea to have the program exhibit the latest geocentric distances and to ask “do you want me to continue?” Then the operator might say “yes,” or give it up, or insert geocentric distances of his own. Once the process is converging toward the correct solution,that convergence is slow but linear.Therefore it can be speeded up using Steffensen's method:three successive values of $\varepsilon _ { \tt A }$ and cg are needed,and then a formula based on (6.6.17) is used to find the next pair of values. Be warned that the process may converge to a spurious solution with negative geocentric distances. It may then be necessary to start the iteration,not using (7.3.14),but with plausible values for the geocentric distances. Marsden warns that early iterations can be wild, with fluctuating signs for some geocentric distances, before finally settling down.

Once the process has been considered to have converged sufficiently, take values of $\mathbf { r } _ { i }$ that go with the sector-triangle ratio most recently calculated.Then use this information to find the $j ^ { \prime }$ and $g$ functionsrelating the two times,and thence the velocity at one of the times. Finally,the elements are found,using the components of position and velocity.

The following listing contains the essential components of the GEM procedure using(7.3.14) to start the iterations.

REM THIS PROGRAN APPLIES THE GEN METHOD FROK THE TEXT.REM THE LISTING DOES NOT INCLUDE THE CALCULATION OF THEREH SECTOR-TRIANGLE RATIO （SEE SECTION 6.12) NOR THEREM CALCULATION OF ELEMENTS，GIVEN COHPONENTS OFREH POSITION AND VELOCITY.THE DECLARATIONS OF DOUBLEREM PRECISION VARIABLES AND INTEGERS HAVE ALSO BEENREM OMITTED.REN  
90 REM YOU ARE ASSUMED TO HAVE ENTERED VALUES OF  
100 REM PARAHETERS SUCH AS PI，GK,THE GAUSSIAN  
110 REM GRAVITATIONAL CONSTANT,AND OBL,THE  
120 REM OBLIQUITY OF THE ECLIPTIC.  
130 REM  
140 REH YOU ARE ASSUKED TO HAVE ENTERED THE TIHE,  
150 REMT(I)，RIGHT ASCENSION,A(I),AND DECLINATION,  
160 REHD(I),FORI=1 TO 3.CONVERT ANGLES TO RADIANS.  
170 REN THE TIMES MIGHT BE CONVERTED TO JULIAN DATES.  
180 REH  
190 REH FIND DIRECTION COSINES IN EQUATORIAL COORDINATES.  
200 FOR I= 1、T0 3  
210 RH（I,1)=COS(D（I））\*COS（A（I））  
220 RHCI,2）=COS(D（I））\*SIN（A（I））  
230 RH（I,3）=SIN（D(I））  
240 NEXT I  
250 REN NEXT,SET UP THE HATRIX RH.  
260 1=0  
270 FORJ=1T03  
280 RM（1,J）=RH（1,J）  
290 W1=Vi+RH（1,J）\*RH（3,J）  
300 NEXT J : REM LOOP FOR XI.  
310 W2=SQR（1#-V1\*W1）  
320 FOR J = 1 TO 3  
330 RM（2,J）=（RH（3,J）- W1\*RH（1,J））/W2

340 NEXT J:REN LOOP FOR ETA.SEE（7.3.10）.  
350H（3,1）=（1,2）\*（2,3）-RH（1,3）\*（2,2）  
360R3）=（1\*（2-\*2  
3703（1  
380 REH COHPONENTS OF ZETA.SEE（7.3.11）  
390 REK EXT,FIND THE DIRECTION COSINES LAHBDA,  
400 REM HU ND NUGIVEN IN（7.3.12）.  
410FORI=1T03  
420 L（）=O:N(I）=O\*:N（I）=O\*  
430NEXTI  
440L（1）=1#  
450FORI=1T03  
460 L（2）=L(2）+R（1,I）\*RH（2,I）  
470 L=3（1\*3  
480 （2=（（2\*2  
490 H3)=3）+（2\*RH（3）  
500 （2)=（2）÷RH（3,I）\*RH（2,I）  
510NEXTI  
520 REH ENTER AND ROTATE SOLAR COORDINATES，PUTTING  
530 REH INTO THE ARRAY SC(I,J）,ROW BY ROW  
540FORI=103  
550 REK ENTER OR CALCULATE SOLAR COORDINATES  
560 REH FOR THE TINE T（I.THESE SHOULD BE  
570 REN CORRECTED FOR THE POSITION OF THE OBSERVER,  
580 REH USING （6.17.1）AND (6.17.2）.CALL THESE  
590 EH SUN(1），SUN(2),AND SUN3）.  
600 FORJ=1T03  
610 SC（I,）=0  
620 FORK=1T03  
630 SC（I,j）=SC（I,J）+RH（J,K）\*SUN(K）  
640 NEXTK  
650 NEXTJ  
660 NEXTI  
670Ti=GK\*（T（1）-T（2））  
680T3=GK\*（T（3)-T(2））:REN（7.3.13）.  
690C1=T3/(T3-T1)  
700C3=-T1/（T3-T1）  
710 REM THESE ARE INITIAL APPROXIHATIONS,USING （7.3.14）.  
720 REH NEXT,FIND NEV GEOCENTRIC DISTANCES,AND THE SUH  
730 REHOFTHE ABSOLUTE VALUES OFOLD-NEGEOCENTRIC  
740 REHDISTANCES,DENOTED BELOV BY W2.IT HAY BE  
750 REH NECESSARYTO INITIALIZE THESE TO ZERO AT THE  
760 REM START OF THE PROGRAN. PROVIDED THE GEOCENTRIC  
770 REN DISTANCES ARE REASONABLE,THE TIKES SHOULD BE  
780 REHHODIFIED USING （7.3.26）  
7901=（-C1\*SC（1,3）+SC(2,3)-C3\*SC（3,3））/N(2）  
8002=ABS(-GD(2））  
810GD(2）=1:RE（7.3.15）.  
8201=（GD(2）\*（2）+C1\*SC（12）-SC(2,2）  
C3\*SC（3,2）)/（C3\*3））  
8302=2+ABS（-GD（3））  
840GD(3）=1RE（7.3.16）  
850W=（GD(2）\*L（2）-C3\*GD(3）\*L(3）+C1\*SC（1,1）  
-SC(2,）+C3\*SC(3,1））/1  
860W2=2+ABS（H-G（1）  
870G(1）=E（7.3.17）  
880FORI=1T03  
890 PRINT GD（I）  
900NEXTI  
910IF2.00001#THEN1380  
920 REM THE PROCESS HAS CONVERGED SUFFICIENTLY,  
930 REM AND THE ELEHENTS ARE TO BE FOUND.THE CHOICE  
940 REH OF THE "SHALL QUANTITY" IS YOURS.  
950 REM  
960 REN FIND THE HELIOCENTRIC COORDINATES.  
970FOR103  
980 =（）\*（）SC（）  
990   
1000 （3）=GD（I）\*N（I）-SC（i,3）  
1010NEXTI  
1020 REH NEXT FIND THE SECTOR-TRIANGLE RATIOS  
1001  
1050 ORJ=103  
1060P=x（2,J）\*x（2,J）

1070 R2=R2+X（3,J）\*X（3,J）  
1080 KAY=KAY+X（2,J）\*X（3,J）  
1090 NEXT J  
11001=SqR（R1）:R2=SQR（R2）  
1110 KAY=SQB（2\*KAY+2\*R1\*B2）  
1120DT=T（3）-T（2）  
1130G0SUB 4000:Y1=YG1  
1140R1=O:R2=0:KAY=0#  
1150FO =1T3  
1160 Ri=R1+X（1,J）\*X（1,J）  
1170 R2=R2+（3\*x（3）  
1180 KAY=KAY÷X（i,J）\*X（3,J）  
1190 NEXTJ  
1200 R1= SQR（R1):R2= SQR（R2)  
1210KAY=SQR(2\*KAY+2#\*R1\*R2）  
1220DT=T（3）-T（1）  
1230G0SUB 4000:Y2=YG1  
1240R1=O:R2=O:KAY=0#  
1250F0RJ=1TO3  
1260 Ri=R1÷x（1,J）\*X（1,J）  
1270 R2=R2+X（2J）\*x（2,J）  
1280 KAY=KAY+（1,J）\*X(2,J）  
1290EXTJ  
1300 R1=SQR（R1):R2=SQR（R2）  
1310 KAY=SQR（2\*KAY+2\*R1\*R2）  
1320 DT=T(2）-T（1）  
1330G0SUB 4000 :Y3=YG1  
1340 PRITATIOSY1Y2.Y3  
1350C1=（Y2/Y1\*（（T（3）-T（2）)/（T（3）-T（1）））  
1360C3=（Y2/Y3）\*（（T（2)-T（1SS/T（3）-（133）:REH（7.3.7）  
1370G0TD_790  
1380 REM FIND HELIOCENTRIC COORDINATES IN ECLIPTIC  
1390 REM COORDINATES FOR TIHES T(1) AND T（2).  
1400X=0:x2=0  
1410FORK=1T03  
1420 X=X+RH（K,1）\*X（1,K）  
1430 X2=X2÷RM（K,1）\*X（2,K）  
1440 NEXTK  
1450Y=0:Y2=0#  
1460FORK=1T03  
1470 Y=Y+RN（K,2）\*（1,K）  
1480 Y2=Y2+RH（K,2）\*X（2,K）  
1490 HEXTK  
1500Z=0:22=0  
1510 FORX=1T03  
1520 Z=2+RM（K,3）\*X（1,K）  
1530 Z2=22+RM（K,3）\*X（2,K）  
1540 NEXTK  
1550YT=Y\*COS(OBL)+Z\*SIN（OBL）  
1560Z=-Y\*SIN（OBL)+Z\*COS（OBL):Y=YT  
1570YT= Y2\*COS(OBL）+Z2\*SIN（OBL）  
1580 Z2= - Y2\*SIN（OBL)+Z2\*COS（OBL):Y2=YT  
1590R=SQR（X\*X÷Y\*Y+Z\*Z)  
1600F= 1-2\*DT\*DT\*MU/（KAY\*KAY\*YG1\*YG1\*R）  
1610G=DT/YG1  
1620xY=（x2-F\*X）/G  
1630Y=（Y2-\*/  
1640 2v=(22-F\*2）/G  
1650 REMX,Y,Z,XV,YV AND ZV ARE  
1660 REM COMPONENTS OF POSITION AND VELOCITY AT TIHE T（1).  
1670 REM FINALLY,CALL A SUBROUTINE TO CALCULATE THE  
1680 REN ELENENTS.  
1690 END  
4000 REH SUBROUTINE FOR FINDING THE SECTOR-TRIANGLE RATIO.

The other method to be described is called the “Moulton-Vaisala-Cunningham”method by Marsden,or MVC for short. This uses equations (7.3.9) with components again resolved using the rotation matrix RM. In this reference system,let $\yen 2$ and $\yen 2$ be

$$
\begin{array} { r } { \mathbf { r } _ { 2 } = ( \xi _ { 2 } , \eta _ { 2 } , \zeta _ { 2 } ) \quad \mathrm { a }  \mathbf { v } _ { 2 } = ( v \xi _ { 2 } , v \eta _ { 2 } , v \zeta _ { 2 } ) . } \end{array}
$$

First,we shall resolve the equations in an order that will facilitate discussion:

$$
\begin{array} { r } { \xi _ { 2 } = \rho _ { 2 } \lambda _ { 2 } - X _ { 2 } , } \\ { \eta _ { 2 } = \rho _ { 2 } \mu _ { 2 } - Y _ { 2 } , } \\ { \zeta _ { 2 } = \rho _ { 2 } \nu _ { 2 } - Z _ { 2 } , . } \end{array}
$$

$$
\begin{array} { r } { \dot { f } _ { 1 } \zeta _ { 2 } + g _ { 1 } v \zeta _ { 2 } = - Z _ { 1 } , } \\ { \dot { f } _ { 3 } \zeta _ { 2 } + g _ { 3 } v \zeta _ { 2 } = - Z _ { 3 } , } \end{array}
$$

$$
\begin{array} { r l } & { f _ { 1 } \eta _ { 2 } + g _ { 1 } v \eta _ { 2 } = - Y _ { 1 } , } \\ & { f _ { 3 } \eta _ { 2 } + g _ { 3 } v \eta _ { 2 } = \rho _ { 3 } \mu _ { 3 } - Y _ { 3 } , } \\ & { f _ { 3 } \xi _ { 2 } + g _ { 3 } v \xi _ { 2 } = \rho _ { 3 } \lambda _ { 3 } - X _ { 3 } , } \\ & { f _ { 1 } \xi _ { 2 } + g _ { 1 } v \xi _ { 2 } = \rho _ { 1 } - X _ { 1 } . } \end{array}
$$

his method uses the $f$ and $g$ functions rather than the sector-triangle ratios. ）(7.3.15) and (7.3.4) are combined to give

$$
\rho _ { 2 } = \frac { 1 } { \nu _ { 2 } } \bigg \{ \frac { - g _ { 3 } Z _ { 1 } + g _ { 1 } Z _ { 3 } } { f _ { 1 } g _ { 3 } - g _ { 1 } f _ { 3 } } + Z _ { 2 } \bigg \} .
$$

Finally, as initial approximations to the $\hat { \pmb { \ j } }$ and $g$ functions,

$$
\begin{array} { r } { ⨏ _ { 1 } = 1 - \frac { 1 } { 2 } \tau _ { 1 } ^ { 2 } r _ { 2 } ^ { - 3 } , \quad g _ { 1 } = ( \tau _ { 1 } - \frac { 1 } { 6 } \tau _ { 1 } ^ { 3 } r _ { 2 } ^ { - 3 } ) / k , } \\ { \ f _ { 3 } = 1 - \frac { 1 } { 2 } \tau _ { 3 } ^ { 2 } r _ { 2 } ^ { - 3 } , \quad g _ { 3 } = ( \tau _ { 3 } - \frac { 1 } { 6 } \tau _ { 3 } ^ { 3 } r _ { 2 } ^ { - 3 } ) / k . . } \end{array}
$$

The basic quantity to bc varied in the iteration is $\hat { p } _ { 2 }$ , the geocentric distance $\ddagger _ { 2 }$ . So that method of solution starts with an estimate of $\beta \gamma$ This might befound from (7.3.15) as in the GEM method, or it might be an cducated guess. From then on, there is $\widehat { \mathbf { \Omega } } _ { \widehat { \mathbf { \Omega } } }$ choice of routes that can be taken:

If the observations are close enough together in time for the approximations in (7.3.23) to be adequate, then the following steps might be taken

A1. Start with a value for $\beta _ { 2 }$

A2. Find $\mathfrak { T } _ { 2 }$ from (7.3.19).

A3. Find f1, $g _ { 1 }$ ,f,and $^ { g _ { 3 } }$ for (7.3.23).

A4.Either

A4(a). Find $\beta _ { 2 }$ from (7.3.22), return to A1, and interate; the process of iteration might be speeded up through the use of Steffensen's method. or

$A _ { 2 } = ( b )$ .Find separate values for the quantity ${ \bar { v } } { \bar { \zeta } } _ { 3 }$ from the two equations in (7.3.20).The difference between these is a function of the value of $\rho _ { 2 }$ used in A1:

$$
\dot { \Delta } ( \rho _ { 2 } ^ { ' } ) = \frac { - Z _ { 1 } - f _ { 1 } \zeta _ { 2 } } { g _ { 1 } } + \frac { Z _ { 3 } + f _ { 3 } \zeta _ { 2 } } { g _ { 3 } } .
$$

The equation △(p2) = O can then be solved using the secant method.

A5. Once a satisfactory value for p2 has been found, the successive application of the members of (7.3.21) will provide values for the components of $\yen 2$ ， An approximate orbit has now been found.This might be improved by the use of f and g functions,as described under B.

B. The feature of this approach is that after an initial approximation (B2), the f and g functions are used. These steps may or may not be used after those of A.

B1. Start with a value for $\rho _ { 2 }$

B2.Take steps A2 and A3.

B3. Take an average value of the discrepant values of ug2 found from (7.3.20)

$$
v \zeta _ { 2 } = \left( \frac { - Z _ { 1 } - f _ { 1 } \zeta _ { 2 } } { g _ { 1 } } \tau _ { 3 } + \frac { - Z _ { 3 } - f _ { 3 } \zeta _ { 2 } } { g _ { 3 } } \tau _ { 1 } \right) \frac { 1 } { \tau _ { 1 } + \tau _ { 3 } } .
$$

B4.Take the steps of A5.

B5.Using the $f$ and $g$ functions,find values for $f _ { 1 } , g _ { 1 } , f _ { 3 }$ ,and $g _ { 3 }$

B6.Find $\rho _ { 2 }$ from (7.3.22） and $\zeta _ { 2 }$ from the last equation in (7.3.19).

B7. Return to B3, and iterate. As before, if successive values for p2 are progressing smoothly, then the process can be speeded up through the use of Steffensen's method.If an iteration is not going well, the operator can start again with a different initial guess for p2. In this respect, the method is more versatile than GEM.Universal variables should be used for the computation of the $\hat { \pmb { \jmath } }$ and $\mathfrak { g }$ functions even if the final orbit is confidently expected to be elliptic.During an erratic iteration,hyperbolic orbitsare likely to appear temporarily.

In either method,as soon as estimates are found for the geocentric distances, the times should be corrected for planetary aberration by subtracting

$$
\delta \varepsilon _ { \mathrm { d a y s } } = 0 . 0 0 5 7 6 8 \rho ,
$$

pbeing measured in astronomical units. Right from the start the solar coordinates should be corrected for the position of the observer (the topocentric correction) using (6.17.1) and (6.17.2).

You will have seen that many different routes can be taken in solving this problem of orbit determination. There are, of course, many more that have not been mentioned here. For example, if an orbit is known to be nearly parabolic, the condition (α = O) can be imposed to stabilize the iterations. This sort ofdevice introduces an element of art to the process. When you are learning these methods,enjoy them, but do not expect that the automation of just one method will solve every problem.

# 74Herget's Method for a Preliminary Orbit Using More Than Three Observations.

An orbit determined from three observations might satisfy those observations precisely，but show an alarming discrepancy with a fourth observation. This is because any observation has an associated error. We can only begin to“smooth out” the effects of the errors when many observations are treated. Eventually,the “best”orbit to be found will not satisfy any one observation precisely, but the residuals will be distributed among the observations in a way that is satisfactory statistically.

Herget's method (Ref. 42） is a compromise; two observations (which are hosen by the operator)are satisfied precisely,and the residuals are distributed among the remainder according to the method of least squares. Consider a set ofnobservations, $\{ \alpha _ { 1 } , \delta _ { \bar { 2 } } \}$ at times $\acute { \bar { z } } _ { i }$ $i = 1 , 2 , \dots , \pi$ These do not need to be any special order. For these times we have

$$
\begin{array} { r l } { \mathbf { \phi } _ { t _ { 1 } } : } & { \mathbf { r } _ { 1 } = \rho _ { 1 } \hat { \rho } _ { 1 } - \mathbf { R } _ { 1 } , } \\ { \mathbf { \phi } _ { t _ { 2 } } : } & { \mathbf { r } _ { 2 } = \rho _ { 2 } \hat { \rho } _ { 2 } - \mathbf { R } _ { 2 } , } \\ { : } & { } \\ { \vdots } & { } \\ { \mathbf { \phi } _ { t _ { i } } : } & { \mathbf { r } _ { i } = \rho _ { i } \hat { \rho } _ { i } - \mathbf { R } _ { i } , } \\ { : } & { } \\ { \vdots } & { } \\ { \mathbf { \phi } _ { t _ { n - 1 } } : \mathbf { r } _ { n - 1 } = \rho _ { n - 1 } \hat { \rho } _ { n - 1 } - \mathbf { R } _ { n - 1 } , } \\ { \mathbf { \phi } _ { t _ { n } } : } & { \mathbf { r } _ { n } = \rho _ { n } \hat { \rho } _ { n } - \mathbf { R } _ { n } . } \end{array}
$$

he observations at times $\ddagger _ { \overline { { \xi } } }$ and $\scriptstyle { \frac { 3 } { 2 } } _ { 3 }$ are to be satisfied precisely, and iterations re to be made by varying the quantities ${ \pmb \beta } _ { 1 }$ and $\rho _ { \pi }$

If $\pmb { \rho } _ { 1 }$ and $\beta _ { \mathfrak { T } }$ are assigned values, then $\Xi _ { \ I }$ and $\mathfrak { r } _ { \mathfrak { a } }$ can be found. Then the velocity at one of the times,'say, $\ddagger _ { \mathfrak { I } }$ , can be found using one of the methods of sections 6.11-6.13,and the $f$ and $g$ functions used to find ${ \mathfrak { r } } _ { i } = { \mathfrak { r } } \{ { \vec { \mathfrak { \tau } } } _ { i } \}$ at the remaining times. (Herget suggests using the sector-triangle ratios for all the times; but the course just outlined seems to be more direct, and uses programs that you already have.) The values calculated for $\mathfrak { r } _ { \mathfrak { i } }$ will lead to inconsistencies when substituted into (7.4.1). To quantify these, introduce the unit vectors

$$
\begin{array} { r l } & { \frac { 1 } { \mathrm { S i } } = [ - \sin \alpha _ { i } , \cos \alpha _ { i } , 0 ] , } \\ & { \frac { 1 } { \mathrm { S i } } = [ - \sin \alpha _ { i } , \cos \alpha _ { i } , - \sin \delta _ { i } \sin \alpha _ { i } , \cos \delta _ { i } ] , } \\ & { \frac { 1 } { \mathrm { S i } } = [ - \sin \delta _ { i } \cos \alpha _ { i } , - \sin \delta _ { i } \sin \alpha _ { i } , \cos \delta _ { i } ] , } \end{array} \quad i = 2 , 3 , \ldots , ( n - 1 ) .
$$

ote that for each $\dot { z }$ these form an orthogonal set with $\hat { \pmb { \rho } } _ { i }$ Define

$$
\begin{array} { r l } & { \mathbf { \nabla } \cdot P _ { i } = P _ { i } ( \rho _ { 1 } , \rho _ { n } ) = ( \mathbf { r } _ { i } + \mathbf { R } _ { i } ) \cdot \mathbf { A } _ { i } , } \\ & { Q _ { i } = Q _ { i } ( \rho _ { 1 } , \rho _ { n } ) = ( \mathbf { r } _ { i } + \mathbf { R } _ { i } ) \cdot \mathbf { D } _ { i } , } \end{array} \quad i = 2 , 3 , \ldots , ( n - 1 ) .
$$

Were we dealing with preeise observations and a correct orbit, the $P _ { i }$ and would allbe zero. As it is,each $\therefore \frac { x } { y }$ ill be a non-zero."residual". $7 7 a$ need $\$ 0$

find values of p1 and pn so that these residuals are, frstly,as smallas possible, and.secondly. distributed in a way that is statistically reasonable.

To start the discussion,assume for the moment that the observations are exact, so that p1 and pn are to be found to satisfy the equations

$$
\begin{array} { r l } { P _ { i } ( \rho _ { \hat { 1 } } , \rho _ { n } ) = 0 , \bigg ] } & { { } i = 2 , 3 , \ldots , ( n - 1 ) . } \end{array}
$$

We shall use Newton's method. Starting with approximate values $\beta _ { \ I } ^ { \alpha }$ and $\rho _ { \pi } ^ { \alpha }$ ,we must find corrections $\Delta \rho _ { \tt I }$ and $\Delta \rho _ { \eta }$ so that $\rho _ { 1 } = \rho _ { 1 } ^ { \alpha } \div \Delta \rho _ { 1 }$ and $\rho _ { \tau _ { 3 } } = \rho _ { \tau _ { 3 } } ^ { a } \div \Delta \rho _ { \tau }$ reduce the $P _ { i }$ and $Q _ { i }$ Ideally,we would like to have

$$
\begin{array} { r l } & { P _ { i } ( \rho _ { 1 } ^ { a } + \Delta \rho _ { 1 } , \rho _ { n } ^ { a } + \Delta \rho _ { n } ) = 0 , } \\ & { Q _ { i } ( \rho _ { 1 } ^ { a } + \Delta \rho _ { 1 } , \rho _ { n } ^ { a } + \Delta \rho _ { n } ) = 0 , } \end{array} \bigg ] \quad i = 2 , 3 , \ldots , ( n - 1 ) .
$$

In Newton's method these are linearized, $\mathbf { s } \mathbf { \textsigma } $ that $\Delta \rho _ { \tt I }$ and $\Delta \rho _ { \mathfrak { z } }$ are found from

$$
\begin{array} { l l } { { P _ { i } ( \rho _ { 1 } ^ { a } , \rho _ { n } ^ { a } ) + \displaystyle \frac { \partial P _ { i } } { \partial \rho _ { 1 } } \Delta \rho _ { 1 } + \displaystyle \frac { \partial P _ { i } } { \partial \rho _ { n } } \Delta \rho _ { n } = 0 , \Bigg ] } } & { { ~ i = 2 , \ldots , ( n - 1 ) . } } \\ { { Q _ { i } ( \rho _ { 1 } ^ { a } , \rho _ { n } ^ { a } ) + \displaystyle \frac { \partial Q _ { i } } { \partial \rho _ { 1 } } \Delta \rho _ { 1 } + \displaystyle \frac { \partial Q _ { i } } { \partial \rho _ { n } } \Delta \rho _ { n } = 0 , \Bigg ] } } & { { ~ } } \end{array}
$$

To deal with these equations,two questions must be answered: how do we find values for the partial derivatives,and how do we deal with $( 2 \pi - 4 )$ equations when there are only two unknowns?

The derivatives are found from the approximations:

$$
\begin{array} { r } { \left. \begin{array} { r l } { \frac { \partial P _ { i } } { \partial \rho _ { 1 } } \simeq \frac { P _ { i } \left( \rho _ { 1 } + \Delta , \rho _ { n } \right) - P _ { i } \left( \rho _ { i } - \Delta , \rho _ { n } \right) } { 2 \Delta } , } & { } \\ { \frac { \partial P _ { i } } { \partial \rho _ { n } } \simeq \frac { P _ { i } \left( \rho _ { 1 } , \rho _ { n } + \Delta \right) - P _ { i } \left( \rho _ { 1 } , \rho _ { n } - \Delta \right) } { 2 \Delta } , } & { } \\ { \frac { \partial Q _ { i } } { \partial \rho _ { 1 } } \simeq \frac { Q _ { i } \left( \rho _ { 1 } + \Delta , \rho _ { n } \right) - Q _ { i } \left( \rho _ { 1 } - \Delta , \rho _ { n } \right) } { 2 \Delta } , } & { } \\ { \frac { \partial Q _ { i } } { \partial \rho _ { n } } \simeq \frac { Q _ { i } \left( \rho _ { 1 } , \rho _ { n } + \Delta \right) - Q _ { i } \left( \rho _ { 1 } , \rho _ { n } - \Delta \right) } { 2 \Delta } } & { } \end{array} \right\} \begin{array} { r } { i = 2 , \ldots , ( n - 1 ) . } \\ { i = 2 , \ldots , ( n - 1 ) . } \end{array} } \end{array}
$$

The error in these approximations depends on $\Delta ^ { 3 }$ Herget suggests $\Delta = \emptyset . \bar { 1 }$ with lower values when the geocentric distances are small. If $\Delta$ is too small, then the round-off errors incurred in the subtraction of nearly equal quantities can become serious； but with double precision calculation,a value △= 0.001 should suffice for most purposes. But be carefull To use (7.4.7) a subroutine is needed that computes the $\mathcal { P } _ { \dot { z } }$ and $Q _ { i }$ with input quantities $\beta _ { \ I }$ and $\rho _ { \pi }$ .This subroutine must be run five times,with inputs successively:

$$
( \rho _ { 1 } , \rho _ { n } ) , \quad ( \rho _ { 1 } + \Delta , \rho _ { n } ) , \quad ( \rho _ { 1 } - \Delta , \rho _ { n } ) , \quad ( \rho _ { 1 } , \rho _ { n } + \Delta ) , \quad ( \rho _ { 1 } , \rho _ { n } - \Delta ) .
$$

Next, write the equations (7.4.6) as

$$
\begin{array} { r } { \bar { b } _ { 1 } + a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } = 0 , } \\ { \bar { b } _ { 2 } + a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } = 0 , } \\ { \vdots \qquad \vdots } \\ { \bar { b } _ { k } + a _ { k 1 } x _ { 1 } + a _ { k 2 } x _ { 2 } = 0 . } \end{array}
$$

nparticular, $x _ { \tt i } = \Delta \rho _ { \tt i }$ ${ \mathfrak { x } } _ { 2 } = \Delta \rho _ {  }$ and $\acute { \iota } = 2 \Im , - \acute { \iota }$ These are called “equations of condition":they cannot be solved.For any $\mathfrak { X } \mathfrak { I }$ and $x _ { 2 }$ , each equation will have $\texttt { a }$ residual, $\boldsymbol { \mathscr { T } } _ { \vec { \mathfrak { Z } } }$ where

$$
\tau _ { i } ( x _ { 1 } , x _ { 2 } ) = b _ { i } + a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } , \quad i = 1 , . . . , k .
$$

the method of least squares, the “best” values for $\mathfrak { X } _ { \mathtt { I } }$ and $x _ { 2 }$ are those that nake the sum of the squares of the residuals a minimum. Let

$$
\begin{array} { l } { { \displaystyle { \cal L } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 1 } ^ { k } r _ { i } ^ { 2 } } } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { k } ( b _ { i } + a _ { i 1 } + a _ { i 2 } x _ { 2 } ) ^ { 2 } } . } \end{array}
$$

Forthis to bea minimum,it is necessary that the partial derivatives of $\mathrm { L }$ with respect to $\mathfrak { X } _ { \mathfrak { T } }$ and $\mathfrak { X } _ { 2 }$ be zero.Then

$$
\sum _ { i = 1 } ^ { k } { a _ { i , \ j } \{ b _ { i } + a _ { i , \ 1 } x _ { \ j } + a _ { i , \ 2 } x _ { \ 2 } \} } = 0 ,
$$

and similarly

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { k } a _ { i 1 } b _ { i } + x _ { 1 } \sum _ { i = 1 } ^ { k } a _ { i 1 } ^ { 2 } + x _ { 2 } \sum _ { i = 1 } ^ { k } a _ { i 1 } a _ { i 2 } = 0 , } } \\ { { } } \\ { { \displaystyle \sum _ { i = 1 } ^ { k } a _ { i 2 } b _ { i } + x _ { 1 } \sum _ { i = 1 } ^ { k } a _ { i 1 } a _ { i 2 } + x _ { 2 } \sum _ { i = 1 } ^ { k } a _ { i 2 } ^ { 2 } = 0 . } } \end{array}
$$

hese are called the “normal equations” and they are solved for $\mathcal { X } \mathfrak { z }$ and $x _ { 2 }$ 1 rfor the corrections, $\Delta \rho _ { 1 }$ and $\Delta \rho _ { \mathfrak { z } }$

The procedure can now be summarized. From a set of observations two are chosen to be represented exactly;if in doubt, choose the first and last. Geocentric distances for these times must be estimated. (These might have been inherited from an earlier calculation based on three observations, or from some.plausible argument.） The basic subroutine referred to above is now run five times to find the ${ \vec { z } } _ { i }$ $Q _ { i }$ and their derivatives. These are substituted into the normal equations (7.4.11), which are solved for the correction for the geocentric distances. With these corrected values, the whole process is repeated, and repetitions continue until the changes from one iteration to the next can be neglected.

# Exercises

1.Set up a program for implementing this method.To debug it,begin with a model where the observations are exact, but start with values of the geocentric distances slightly different from the correct ones. Successively start with poorer initial values to get some idea of the convergence of the method. Once the program has run well with correct observations, introduce observational errors, using a random number generator,controlling the rms value of the generator. (See Appendix F.) Experiment with different rms values.Herget comments that “when.the observations are inconsistent, the successive iterations rapidly tend toward the solution $\rho _ { \perp } = \rho _ { \it 2 } = 0$ ” Can you confirm this? Try including one very wrong observation.

2.Write equations (7.4.8) in the condensed form b+ Ax_= 0. Show that the normal equations can then be written as ATb + ATAx= 0, so that the least squares solution is $\mathbf { x } = - ( \mathbf { A } ^ { \mathbb { T } } \mathbf { A } ) ^ { - 1 } \mathbf { A } ^ { \mathbb { T } } \mathbf { b }$ Suppose now that $\napprox$ has m components instead of two. Show that the same notation gives the correct least squares solution.

# 7.5The Differential Correction of Orbits

This subject merits an entire text; so the discussion that follows will be general and superficial. But I hope that it will contain enough detail to enable areader to construct and run non-trivial programs.

Fundamental to the discussion is the assumption that we are dealing with some “model” which can be specified by giving numerical values to a set of parameters; through the use of observations, we want to derive improved values for these parameters. In dealing with orbital motion, the model might be that of the problem of two bodies, when the parameters might consist of a set of six Keplerian elements; but in more complicated cases the model might include masses of perturbing bodies,or parameters describing the effects of the nonsphericity of the Earth；or it might include a set of initial conditions,position and velocity，at a starting time. All of the parameters involved in describing the model will be included in a vector X. Using the model, and a numerical set of parameters,we can predict numerical values for a set of observations: this set will makeup the vector Y.(The word “vector”is used here in the conventional sense of linear algebra to denote a matrix consisting of a single column.) For the model we assume that there is a subroutine that will calculate Y, given X. Thiscan be described bya fowchart

X Y MODEL INPUT OUTPUT

# Flowchart 7.1

an equation.

$$
\mathbb { Y } _ { c } = \mathbb { Y } \{ \mathbb { X } \} .
$$

The subscript c in (7.5.1） stands for calculated. The corresponding quantities will also be observed, and the observed values will be written as $\yen 0$ $Y _ { o }$ and Yewill not be equal; this can be due to errors of observation,errors in the parameters and errors in the model. In the discussion that follows,we assume that:the model is correct.We want to use the discrepancy between $\gamma _ { o }$ and $\yen 6$ toimprove thevalue of $\mathbf { x }$

We start the discussion by temporarily assuming that there are no errors of observation. Then the problem of finding $\mathbf { x }$ given $\yen 0$ ,is equivalent to trying tsolve

$$
\mathbb { Y } _ { o } = \mathbb { Y } ( \mathbb { X } )
$$

orX.The process of solution begins with an estimate for $\mathbf { x }$ :call it $\mathbb { X } _ { \hat { \mathbb { S } } }$ .From his we calculate values for the observations

$$
{ \tt Y } _ { \tt c } = { \tt Y } _ { \tt ( X _ { \tt G } ) } ^ { \prime } .
$$

Wethen calculate the residual

$$
\begin{array} { r } { \mathbf { y } = \mathbf { Y } _ { o } - \mathbf { Y } _ { c } . } \end{array}
$$

With a correct model and no observational error, there will be a correct value of X where

$$
{ \mathbb X } = { \mathbb X } _ { \mathbb { G } } \div { \mathbb X } .
$$

We are to use y to find an approximation for $\mathbf { x }$ ,under the assumption that the quare and products of the members of the vector $\mathbf { x }$ can be neglected. Now 7.5.2) becomes

$$
\mathbb { Y } _ { o } = \mathbb { Y } \{ \mathbb { X } _ { \emptyset } \div \mathbb { x } \} .
$$

$$
\bar { \mathbf { \beta } } = \frac { \partial \mathbb { Y } } { \partial \mathbb { X } }
$$

be the Jacobian matrix having typical element $\partial Y _ { i } / \partial X _ { j }$ , evaluated using the parameters $\mathbb { X } _ { \mathfrak { d } }$ Then, neglecting $\mathbf { x } ^ { 2 }$ , and higher powers, we have the approximation

$$
\mathbb { Y } ( \mathbb { X } _ { 0 } + \mathbb { x } ) \simeq \mathbb { Y } ( \mathbb { X } _ { 0 } ) + \mathbb { J } \mathbb { x } .
$$

This uses the diferential Jx to approximate the difference Y(Xo+x)-Y(Xo); hence the phrase “differential correction.” The method of correction is Newton's method.If (7.5.8) is taken to be precise, we then have the equation

$$
{ \mathfrak { F } } \mathbf { x } = \mathbf { y } .
$$

If the number of observations is equal to the number of unknowns (the method of“minimum data") then J will be square; if,in addition,Jis invertible, then (7.5.9)can be solved for x. The adjusted value (Xo +x) may need further improvement.

The requirement that J (if square) be invertible is equivalent to a requirement that the problem (given Y,find X) is “well defined.”This is well ex-pressed by the phrase that the observations must be able to “see” the components of X,and,one can add,put them into focus.For example, the inclination of the orbital plane of a spectroscopic binary to the plane of the sky (perpendicular to the line of sight） cannot be found from observations of radial velocity; so that inclination must not be included among the parameters to be corrected. If the eccentricity of an orbit is small, then there will be numerical difficulties in trying to locate the position of pericenter. If too short an arc of an orbit is observed,it can be impossible to separate the members of X and put them into “focus.”In each of these cases,there isa geometrical problem that will be revealed by the numerical difficulties encountered in solving (7.5.9).

In the discussion that follows it will be assumed that the numbers of components in X and Y are m and n,respectively. Normally, n is much larger thanm.The“optics” through which the observations“see”the parameters to be corrected are contained in the matrix J.There are several ways in which to find its components. If the model is that of Keplerian motion,explicit formulas are available. (See Ref. 35). They can be found as the solutions of special differential equations. The simplest way in which to approximate them is that used in the preceding section:

$$
\begin{array} { l } { { \displaystyle { \frac { \partial Y _ { i } } { \partial X _ { j } } = J _ { i j } } } } \\ { { \displaystyle { \qquad \simeq \frac { 1 } { 2 \delta _ { j } } [ Y _ { i } ( X _ { 1 } , \ldots , X _ { j - 1 } , X _ { j } + \delta _ { j } , X _ { j + 1 } , \ldots , X _ { m } ) } } } \\ { { \displaystyle { \qquad - Y _ { i } ( X _ { 1 } , \ldots , X _ { j - 1 } , X _ { j } - \delta _ { j } , X _ { j + 1 } , \ldots , X _ { m } ) ] } . } } \end{array}
$$

Suppose that (7.5.1) is invoked by a subroutine called MoDEL(X,Y).(The FORTRAN terminology will make the steps more explicit.） Let

$$
\begin{array} { r } { \overrightarrow { \delta } _ { k } = \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \vdots } \\ { \delta _ { k } } \\ { \vdots } \\ { 0 } \end{array} \right] } \end{array}
$$

Let us successively CALL MODEL $( \mathbf { X } + \overline { { \delta } } _ { k } , \mathbf { Y } _ { 1 } )$ and CALL MODEL $\{ \mathbf { X } - \overline { { \hat { \theta } } } _ { \vec { \pi } } , \ Y 2 \}$ ,and let y= Y1-Y2. Using differentials, approximately

$$
\begin{array} { r } { \left[ \begin{array} { l l l l } { J _ { 1 1 } } & { J _ { 1 2 } } & { \dots } & { J _ { 1 k } } & { \dots } & { J _ { 1 m } } \\ { J _ { 2 1 } } & { J _ { 2 2 } } & { \dots } & { J _ { 2 k } } & { \dots } & { J _ { 2 m } } \\ { \vdots } & & & { \vdots } \\ { \vdots } & & & { \vdots } \\ { \vdots } & & & { \vdots } \\ { \vdots } & & & { \vdots } \\ { J _ { n 1 } } & { J _ { n 2 } } & { \dots } & { J _ { n k } } & { \dots } & { J _ { n m } } \end{array} \right] \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \vdots } \\ { 2 \delta _ { k } } \\ { \vdots } \\ { 0 } \end{array} \right] \simeq \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] . } \end{array}
$$

# Therefore

$$
\left[ \begin{array} { c } { J _ { 1 k } } \\ { J _ { 2 k } } \\ { \vdots } \\ { \vdots } \\ { J _ { n k } } \end{array} \right] \simeq \left[ \begin{array} { c } { \frac { \mathcal { Y } _ { 1 } } { 2 \delta _ { k } } } \\ { \frac { \mathcal { Y } _ { 2 } } { 2 \delta _ { k } } } \\ { \vdots } \\ { \frac { \mathcal { Y } _ { n } } { 2 \delta _ { k } } } \end{array} \right]
$$

The following listing may help clarify the procedure. The component $\tilde { \beta } _ { i k }$ has een replaced by JAC(I,K).

D02K=1,NX（K）=X(x）+DEL（K）CALLHODEL(X,Y1）（x）=X（K）-2\*DEL（K）CALL HODEL（XY2）  
D01I=1,NJAC(I,K）=（Y1（I）-Y2（I））/（2\*DEL（K））  
X（K）=X（K）÷DEL（K）

Ajudicious choice of the size of the “tweak,”DEL(K),may not be easily made; it will depend, among other things, on the order of magnitude of the corresponding component, $X _ { \{ \pm \} } ^ { \prime } \{ \pmb { \chi } \}$ If the $\mathbf { x }$ vector includes components of position and velocity, then these may have considerably disparate orders of magnitude. (It can be.an advantage to use units internally in a calculation so that these orders of magnitude are similar.) If the order of magnitude of X(K) is M(K), then,as a rule of thumb, I recommend trying $\tt D E I ( X ) \phi = \tt N f ( X ) * \tt i O ^ { - 4 }$ ；but experimentation may be needed. In particular, over long arcs, smaller DEL may be needed.

We.can now return to the equations of condition (7.5.9). Since there will be more equations $\{ \mathfrak { R } \}$ than unknowns $\{ \mathfrak { M } \}$ ,it will beimpossible tosatisfy allof these equations, and they must be "solved" by some compromise, as were the equations (7.4.8) in the preceding section. Again, we use the method of least squares. Before outlining the procedure, let me point out again that we are using a linearized approximation to improve the estimate $\mathbb { X } _ { \mathfrak { a } }$ of the parameters of the model; additional improvement may be necessary to compensate for the linearization.

Let us assume that the only reason that the equations of condition cannot be satisfied is that there are unavoidable errors of observation in the Y. (So we are assuming that the model itself is correct.) This means that an estimate of the vector x is equivalent to an estimate of the errors of observations, $\Im$ ， where

$$
\mathbb { V } = \mathbb { J } \mathbb { x } - \mathbb { y } .
$$

If x were given its“correct”value,then (7.5.12） would give the actual errors of observation.But observational errors are samples of random variables,and, through （7.5.1） $\mathbf { x }$ becomes also associated with random variables;we can only estimate x;but then we may be able to use statistical reasoning to evaluate the quality of the estimate.

Let $\mathbf { x } ^ { * }$ be the “best”estimate of $\mathbf { x }$ (subject to assumptions to be described shortly)；then we have a “best” estimate of the observational errors, $\begin{array} { r l } { \pmb { \mathbb { Y } } ^ { \ast } } & { { } = } \end{array}$ $\ J _ { \mathbf { x } } ^ { * } - \ y$ .Weassume each observational error to bea sample value of a random variable with Gaussian probability distribution given by

$$
\mathrm { e x p } \left\{ - { \textstyle \frac { 1 } { 2 } } v _ { i } ^ { 2 } / \sigma _ { i } ^ { 2 } \right\} .
$$

Note that this implies that there is no bias, or systematic error in the observations.

The probability of the error $v _ { i }$ is given by $\mathrm { e x p } \left\{ - \frac { 1 } { 2 } v _ { i } ^ { 2 } / \sigma _ { i } ^ { 2 } \right\}$ and the joint probability of the errors ${ \mathfrak { V } } _ { \mathtt { I } }$ $s _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ is

$$
\exp \left( - { \textstyle \frac { 1 } { 2 } } ( v _ { 1 } ^ { 2 } / \sigma _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 } / \sigma _ { 2 } ^ { 2 } + \cdot \cdot \cdot + v _ { n } ^ { 2 } / \sigma _ { n } ^ { 2 } ) \right) .
$$

Here we have assumed that there is no correlation between the errors of different observations; this may be too optimistic.The“best” estimate of $\mathfrak { v }$ is that which makes the joint probability $\hat { \mathbf { a } }$ maximum, or, equivalently, the sum of the squares

$$
\frac { v _ { \bar { 1 } } ^ { 2 } } { \sigma _ { 1 } ^ { 2 } } + \frac { v _ { 2 } ^ { 2 } } { \sigma _ { 2 } ^ { 2 } } + \ldots + \frac { v _ { n } ^ { 2 } } { \sigma _ { n } ^ { 2 } }
$$

a minimum. The condition for this, found by elementary calculus,again leads to a set of normal equations.

Probably, thenumbers $\sigma _ { i }$ will not be known; but an estimate may be possible of their relative values. Let

$$
w _ { i } = \frac { k } { \sigma _ { i } } , \quad i = 1 , 2 , \ldots , n .
$$

These are relative weights. Let the diagonal matrix W be defined by

$$
\begin{array} { r } { \mathbb { W } = \left[ \begin{array} { l l l l } { w _ { 1 } } & { 0 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { w _ { 2 } } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { w _ { 3 } } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { \cdots } & { w _ { n } } \end{array} \right] . } \end{array}
$$

$$
\tilde { \bar { \mathbf { J } } } = \mathbb { W } \mathbb { J } \quad \mathrm { a } \mathrm { a } \bar { \mathrm { d } } \quad \tilde { \mathbf { y } } = \mathbb { W } \mathbf { y } .
$$

The “weighted” equations of condition can be written as

$$
\tilde { \bar { \mathbf { y } } } \mathbf { x } = \tilde { \mathbf { y } }
$$

ind the normal equations as

$$
\tilde { \bar { \mathbf { J } } } ^ { \tilde { \bar { \mathbf { J } } } } \tilde { \bar { \mathbf { J } } } \mathbf { x } = \tilde { \bar { \mathbf { J } } } ^ { \tilde { \bar { \mathbf { J } } } } \tilde { \bar { \mathbf { y } } } ,
$$

ith their solution being the “best” estimate

$$
\mathbf { x } ^ { * } = ( \tilde { \bar { \mathbf { J } } } ^ { \mathcal { T } } \tilde { \bar { \mathbf { J } } } ) ^ { - 1 } \tilde { \bar { \mathbf { J } } } ^ { \mathcal { T } } \tilde { \bar { \mathbf { y } } } .
$$

The quality of this solution will depend on the residuals that result when ie solution is substituted into the equations of condition.Define

$$
\sigma = \sqrt { \frac { 1 } { n - m } \sum _ { i = 1 } ^ { n } w _ { i } ^ { 2 } v _ { i } ^ { 2 } } .
$$

This is the $\mathrm { \textmu } _ { \mathrm { { T I D S } } }$ error of unit weight". ( $\mathrm { \overline { { { \varepsilon } } } } _ { \mathrm { F I D S } } \mathrm { { \varepsilon } } ^ { \mathrm { { * } } }$ stands for “root mean square.") Note the appearance of $\{ \mathfrak { r } - \mathfrak { n } \}$ in the denominator. If $\mathfrak { r }$ is less than $\overrightarrow { z } \overrightarrow { z }$ ,no reasonable solution by these means is possible; if $ \pi =  \Im \Im$ ， then we have the situation of “minimum data"; a solution may be possible, but no statistical information about that solution can be found. Let the $\ j ^ { - }$ th diagonal element in (jTj)-1 be s². Then the rms error associated with the estimate x is gsi. Two other matrices are of importance. The covariance matrix of the estimate is

$$
\mathbb { P } = \sigma ^ { 2 } \{ \tilde { \Im } ^ { \Im } \tilde { \Im } \} ^ { - 1 } .
$$

If this matrix has typical element $\widehat { \mathcal { P } } \dot { z } \dot { \mathfrak { f } }$ , then the correlation matrix, $\mathbf { C }$ has typical element $c _ { i j } = g _ { i j } / ( \mathcal { p } _ { i \dot { z } } \mathcal { p } _ { \dot { j } \dot { \beta } } ) ^ { 1 / 2 }$ The terms of the principal diagonal of $\Sigma$ areall equal to one; if any off-diagonal term approaches one, then this correlation coeffcient indicates a possible strong correlation (or lack of independence) between the errors of the corresponding observations.

The assumptions of independence,Gaussian distributions, and no bias (or systematic error) in these distributions can weaken the conclusions, which should.anyway,be treated with reserve.

We have used the language of “rms errors.” It is common in astronomical applications to use “probable errors”. There is nothing intrinsically “probable” about a probable error; it is a number such that, assuming a Gaussian distribution (7.5.13), the error is equally likely to be larger or smaller (in absolute magnitude). For a Gaussian distribution with rms error o, the probable error is

$$
{ \mathfrak { P } } ^ { * } \simeq { \mathfrak { O } } . { \mathfrak { O } } ^ { 7 4 5 \sigma . }
$$

We finish with an additional FORTRAN listing designed to implement this procedure. The matrix A(I,J) is JTJ,and B(I） is JTy.

JAC(I,J），I=1,..N，J=1,,K.ALTERNATIVELY, $I = \pm \cdots , X _ { 2 }$   
THESE HIGHT BE FOUND IN THE LOOP OVER INDIVIDUAL  
INITIALIZE A(J,K)AND B（J),J,K=1,...,H,TO ZERO.  
D0 13 $\texttt { J } \equiv \texttt { 1 } _ { \tt 2 } \texttt { N }$   
C APPLY VEIGHTS,W（I）.D011J=1,  
11JAC（I,J）=（I）\*JAC（I,J）Y（I）=（I）\*Y（I）  
C AUGNENT THE MATRICES A AND B.D012J=1,B（J）=B（J)+JAC（I,J）\*Y（I）D012K=1,H  
12 A（J,K）=A（J,K)+JAC（I,J）\*JAC（I,K）  
13 CONTINUE  
SFI FRSEA IVERSE）.SIGHA =0D021I=1,NV=-Y(I)D0 20J=1,  
2 V=V +JAC（I,J）\*X（J）SIGHA = SIGMA  V\*VSIGMA $=$ DSQRT(SIGMA/DFLOAT（N-N)）CALCULATE RMS ERRORS OF THE ESTIHATE.APPLY THE CORRECTIONS,X（J)，TO THE INITIAL ESTIHATESOFTHE PARAMETERS.IF THE CORRECTIONS ARE CONSIDEREDTOO LARGE，THEN ANOTHER ITERATION VILL BE NEEDED.

# 7.5.1 Projects

These are designed so that you can,by stages,learn,program and debug the procedures. The “model” can be that of Keplerian motion. The parameters,X, can be Keplerian elements, or components of position and velocity at some given time.The observations might be geocentric right ascension and declination, or quantities such as range and range-rate.

1. For the first experiment with the Jacobian matrix J, take X to consist of components of position and velocity at time to,and Y to consist of the same components at time t. J will then be a 6×6 matrix. In this special case (do not generalize) J is a type of matrix called symplectic. A consequence is that if $\mathfrak { J }$ is subdivided into four $3 \times 3$ matrices as

$$
\mathbb { J } = \left[ \begin{array} { c c c c } { \mathbb { U } } & { \mathbb { V } } \\ { \mathbb { W } } & { \mathbb { Y } } \end{array} \right] , \quad \mathrm { t h e n } \quad \mathbb { J } ^ { - 1 } = \left[ { \texttt { Y } } ^ { T } - \mathbb { V } ^ { T } \right] .
$$

That is, the inverse of $\mathfrak { J }$ can be found by a rearrangement of its terms and some changes of sign.Find $\mathfrak { J }$ rearrange to find $J ^ { - 1 }$ Calculate the product of the two matrices and verify that one is truly the inverse of the other.Don't go any further until this is correct.

2.This is a continuation of the first project. You will already have computed   
Y,given X. Now introduce small changes into every component of $\mathbf { x }$ ，to give $\mathbf { X } + \mathbf { x } ,$ and find the resulting components of position and velocity at time $\ddagger _ { 1 }$ ，and then $\mathfrak { y }$ thedifference between these numbers and the components of $\mathbb { Y }$ Verify that approximately $\Im \times \simeq \Im$

3.Experiment with different “tweak” sizes for the effects on the components ofJ.Consider cases where $\tt f _ { \tt 1 } - \tt t _ { \tt 0 }$ spans at least one complete revolution.

4.If a tweaked orbit is sufficiently close to the reference,or untweaked orbit, then the linear approximation for the difference between the orbits will be adequate. But ifa tweaked orbit strays too far from the reference orbit, the linear approximation is lost.One method of procedure is as follows. If the magnitude of the difference between the orbits exceeds a given amount, then all of the differences (in position and velocity)are reduced bya factor of ten. Then the tweaked orbit remains within the linear region around the reference orbit.When finding derivatives for times after this reduction,the quantities $\delta _ { j }$ in（7.5.10）or DEL(K）in the listing must be reduced bya factor of ten.Experiment with this procedure, using orbits extending over several revolutions.

5. Consider the application of $\mathbb { J }$ as formulated above, to the two-point boundary value problem. We want to find the orbit that connects positions $\mathfrak { r } _ { \mathfrak { V } }$ at time $\ddagger _ { 0 }$ and $\mathfrak { X } _ { \mathfrak { Z } }$ at time $\fallingdotseq$ We have an approximate value for the initial velocity $\yen 0$ ,and this needs to be improved. $\mathtt { r _ { 0 } }$ and this approximation for $\yen 0$ constitute the vector X.Using these as initial conditions, the value of r at $\ddagger _ { 1 }$ can be found; let the difference between this value and $\Xi _ { \vec { \mathfrak { L } } }$ be $\delta \pmb { \tau } _ { \pmb { \updownarrow } }$ Show how $\pmb { \tilde { \jmath } }$ (more specifically, the components $\mathfrak { T }$ and $\mathbb { V }$ from the first project) can be used to find a correction to the approximate velocityat $\ddagger _ { 0 }$ in terms of $\delta \mathbf { z } _ { \mathtt { I } }$

5.Let $\mathbf { x }$ contain six Keplerian elements and $\mathbb { Y }$ the observations at three different times. J will be a $6 \times 6$ matrix. Start this project with a set of elements $X _ { z }$ and calculate a set, $\mathbb { Y } _ { \mathfrak { p } }$ ， $\mathfrak { O } ^ { \mathfrak { T } }$ (correct) observations. Now let X consist ofa set of elementschanged slightly but deliberately from $X _ { y }$ Use this set to find calculated values of the observations, $\mathbb { Y } _ { c }$ .f $\mathbf { y } = \mathbb { Y } _ { \mathfrak { p } } - \mathbb { Y } _ { \mathfrak { c } }$ then corrections to take $\mathbb { x }$ to $\mathbb { X } _ { \mathfrak { p } }$ should satisfy $\Im \mathbf { x } = \Re$ Verify that this is true. Find $\mathbf { z } = \mathbf { \Im } ^ { - 1 } \mathbf { \Im } ^ { \prime }$ Lf $\mathbb { X } \neq \mathbb { x }$ is close to $X _ { 3 }$ but not close enough, another iteration may be necessary. Show how this procedure might be used in orbit determination once an approximate solution is known.

7.Generalize the preceding problem. Let Y contain observations for more than three times. J no longer has an inverse, now $\mathbf { x } = ( \mathbb { J } ^ { T } \mathbb { J } ) ^ { - 1 } \mathbb { J } ^ { T } \mathbb { y }$ You will be using the program for setting up the normal equations. Verify that the solution is correct.

8. Again, we generalize the preceding problem. But now, instead of using the“perfect”observations,Yp,add random errors to each component to produce true observations,Y= Yp+e. The numbers in e can be generated by a subroutine that produces sample values of a Gaussian distribution.See Appendix F.For a start,use just one such distribution, so that all observations share the same rms error,and have, therefore, equal weights. Now your estimate of the corrections to X can include statistics.Also, the sum of the square of the residuals,Ui, should be such that

$$
\sqrt { \frac { 1 } { n - m } \sum _ { i = 1 } ^ { n } v _ { i } ^ { 2 } }
$$

should be close to the rms error that you inserted into the observations.

9.Continue to generalize. Different observations can be given errors with different rms values. Experiment with the use of different weights in the normal equations. Then introduce a greater variety of types of observation. They will have a greater variety of rms errors, and there will be more scope for weighting.

Note that these projects have all involved situations that have been artificially contrived; that is,we know the “true” answers.I suggest that they are worthwhile in order to gain experience and confidence.

# 7.6Using a Previous Estimate: Recursive Methods

At the conclusion of the estimation described in the preceding section,we had the “best” estimate itself,and also the covariance matrix $\mathbf { \vec { g } }$ ,of (7.5.21) that contained the statistics of that estimate. The covariance matrix of the errors of observation was

$$
\mathbf { Q } = \left[ \begin{array} { l l l l l } { \sigma _ { 1 } ^ { 2 } } & { 0 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { \sigma _ { 2 } ^ { 2 } } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { \sigma _ { 3 } ^ { 2 } } & { \cdots } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { \cdots } & { \sigma _ { n } ^ { 2 } } \end{array} \right] .
$$

Starting with equations of condition Jx = y (7.5.9), the normal equations (7.5.18) would be JTQ-1Jx =.JTQ-1y. This assumes that the oi are known a priori, and the assumption will be made in the discussion that follows.

Suppose that two mutually independent sets of observations, $\mathbb { Y } _ { \ I }$ and $\yen 2$ ： re to be combined. If the sets have covariance matrices of errors $\pmb { \mathcal { Q } } _ { 1 }$ and $\ Q _ { 2 } ,$ espectively, then the combined set of observations is contained in the vector

$$
\begin{array} { r } { \mathbb { Y } = \left[ \begin{array} { l } { \mathbb { Y } _ { 1 } } \\ { \mathbb { Y } _ { 2 } } \end{array} \right] } \end{array}
$$

having the covariance matrix of errors

$$
\mathbf { Q } = \left[ \begin{array} { l l } { \mathbf { Q } _ { 1 } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { Q } _ { 2 } } \end{array} \right] .
$$

(The zero matrices here are rectangular.) If the two sets were to be processed separately, then the associated equations of condition would be

$$
{ \mathfrak { J } } _ { \mathrm { i } } \mathbf { x } = \mathbf { { y } } _ { \mathrm { i } } , \quad { \mathrm { a n d } } \quad { \mathrm { J } } _ { 2 } \mathbf { x } = \mathbf { { y } } _ { 2 } ,
$$

and the corresponding normal equations would be

$$
\begin{array} { r } { \mathfrak { J } _ { 1 } ^ { T } \mathbf { Q } _ { 1 } ^ { - 1 } \mathfrak { J } _ { 1 } \mathbf { x } = \mathfrak { J } _ { 1 } ^ { T } \mathbf { Q } _ { 1 } ^ { - 1 } \mathbf { y } _ { 1 } , \quad \mathrm { a n d } \quad \mathfrak { J } _ { 2 } ^ { T } \mathbf { Q } _ { 2 } ^ { - 1 } \mathfrak { J } _ { 2 } \mathbf { x } = \mathfrak { J } _ { 2 } ^ { T } \mathbf { Q } _ { 2 } ^ { - 1 } \mathbf { y } _ { 2 } . } \end{array}
$$

Combined, the equations of condition are

$$
\left\{ \begin{array} { l } { \mathbf { \vec { j } } _ { 1 } } \\ { \mathbf { \vec { j } } _ { 2 } } \end{array} \right\} \mathbf { x } = \left[ \begin{array} { l } { \mathbf { \vec { y } _ { 1 } } } \\ { \mathbf { \vec { y } _ { 2 } } } \end{array} \right] ,
$$

with normal equations

$$
\left[ \mathbb { J } _ { 1 } ^ { T } \ \mathbb { J } _ { 2 } ^ { T } \right] \left[ \begin{array} { c c } { \mathbf { Q } _ { 1 } ^ { - 1 } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { Q } _ { 2 } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \mathbb { J } _ { 1 } } \\ { \mathbb { J } _ { 2 } } \end{array} \right] \mathbf { x } = \left[ \mathbb { J } _ { 1 } ^ { T } \ \mathbf { J } _ { 2 } ^ { T } \right] \left[ \begin{array} { c c } { \mathbf { Q } _ { 1 } ^ { - 1 } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { Q } _ { 2 } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \mathbf { y } _ { 2 } } \end{array} \right]
$$

$$
\begin{array} { r } { ( \Im _ { 1 } ^ { T } \mathbb { Q } _ { 1 } ^ { - 1 , \Im _ { 1 } } + \Im _ { 2 } ^ { T } \mathbb { Q } _ { 2 } ^ { - 1 } \Im _ { 2 } ) \mathbf { x } = \Im _ { 1 } ^ { T } \mathbb { Q } _ { 1 } ^ { - 1 } \mathbf { y } _ { 1 } + \Im _ { 2 } ^ { T } \mathbb { Q } _ { 2 } ^ { - 1 } \mathbf { y } _ { 2 } . } \end{array}
$$

So, normal equations for the entire set can be derived by adding together the normal equations for the separate sets. But remember that we have assumed that there is no correlation between the two sets.

Next, suppose that the normal equations for the first set have been solved, with the solution

$$
\begin{array} { r } { \mathbf { x } _ { 1 } ^ { * } = ( \bar { \mathbf { J } } _ { 1 } ^ { T } \mathbf { Q } _ { 1 } ^ { - 1 } \bar { \mathbf { J } } _ { 1 } ) ^ { - 1 } \bar { \mathbf { J } } _ { 1 } ^ { T } \mathbf { Q } _ { 1 } ^ { - 1 } \mathbf { y } _ { 1 } } \\ { = \mathbb { P } _ { 1 } \bar { \mathbf { J } } _ { 1 } ^ { T } \mathbf { Q } _ { 1 } ^ { - 1 } \mathbf { y } _ { 1 } , \quad \quad } \end{array}
$$

Where P1 is the covariance matrix of errors of the estimate $\mathbf { x } _ { \mathfrak { I } } ^ { * }$ .Then the normal equations for the first set could be written as

$$
\begin{array} { r } { \mathbb { P } _ { \widehat { \mathfrak { T } } } ^ { - \widehat { \mathfrak { T } } } \mathbb { x } _ { \widehat { \mathfrak { T } } } ^ { * } = \mathbb { \widehat { \mathfrak { s } } } _ { \widehat { \mathfrak { T } } } ^ { \widehat { \mathfrak { T } } } \mathbb { Q } _ { \widehat { \mathfrak { T } } } ^ { \widehat { - \mathfrak { T } } } \mathbb { \mathbb { y } } _ { \widehat { \mathfrak { T } } } } \end{array}
$$

and consequently the normal equations for the entire set can be writen as

$$
( \mathbf { P } _ { 1 } ^ { - 1 } + \Im _ { 2 } ^ { T } \mathbf { Q } _ { 2 } ^ { - 1 } \Im _ { 2 } ) \mathbf { x } = \Re _ { \frac { 1 } { 3 } } ^ { - 1 } \mathbf { x } _ { \frac { 1 } { 3 } } ^ { * } + \Im _ { 2 } ^ { T } \mathbf { Q } _ { 2 } ^ { - { \frac { 1 } { 3 } } } \mathbf { y } _ { 2 } .
$$

This leads to the following reinterpretation. We have a “best” estimate, $\mathbf { x } _ { 1 } ^ { * }$ together with its statistics, $\mathbb { P } _ { 1 }$ Then we have a further set of observations, Y2,and its statistics, Q2. (7.6.9) tels us how the previous estimate can be incorporated into the use of $\mathbb { Y } _ { 2 }$ toimprove the estimate further.

In some respects one can say that the first set of observations is not required since $\mathbf { x } _ { \mathtt { i } } ^ { * }$ and $\mathbb { P } _ { \mathfrak { T } }$ are available. But the discarding of observations is never desirable (their statistics can no longer be tested). Also we are solving a linearproblem here,and may eventually have to iterate in order to satisfy the fundamental non-linear generating problem.

Another way to derive this result is to treat the previous estimate as an “observation.” We shall change the notation slightly. Suppose that we have an estimate, $\mathtt { x } _ { \mathtt { 0 } }$ ,together with its statistics, $\mathfrak { P } _ { 0 }$ Now we havea new set of observations, $\mathbb { Y }$ ,with residuals $\Im$ and statistics $a$ Treating the initial elements as an observation leads to the equations of condition

$$
\mathbf { J x } = \mathbf { y } \quad { \mathrm { a n d } } \quad \mathbf { x } = \mathbf { x } _ { 0 }
$$

or

$$
\left[ \begin{array} { l } { \mathbf { \vec { y } } } \\ { \mathbf { \vec { z } } _ { m } } \end{array} \right] \mathbf { x } = \left[ \begin{array} { l } { \mathbf { \vec { y } } } \\ { \mathbf { \vec { x } } _ { \theta } } \end{array} \right] .
$$

The covariance matrix of errors of all the “observations” is

$$
\left[ { \begin{array} { l l } { \mathbf { Q } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { P } _ { 0 } } \end{array} } \right]
$$

so that the normal equations are

$$
\left[ \mathbb { J } ^ { T } \mathbb { I } _ { m } \right] \left[ \begin{array} { c c } { \mathbb { Q } ^ { - 1 } } & { \mathbb { Q } } \\ { \mathbb { Q } } & { \mathbb { P } _ { 0 } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \mathbb { J } } \\ { \mathbb { I } _ { m } } \end{array} \right] \mathbf { x } = \left[ \mathbb { J } ^ { T } \mathbb { I } _ { m } \right] \left[ \begin{array} { c c } { \mathbb { Q } ^ { - 1 } } & { \mathbb { 0 } } \\ { \mathbb { 0 } } & { \mathbb { P } _ { 0 } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { \mathbf { y } } \\ { \mathbf { x } _ { 0 } } \end{array} \right]
$$

or

$$
( \Im ^ { T } \mathbb { Q } ^ { - 1 } \mathbb { J } + \mathbb { P } _ { 0 } ^ { - 1 } ) \mathbf { x } = ( \Im ^ { T } \mathbb { Q } ^ { - 1 } \mathbf { y } + \mathbb { P } _ { 0 } ^ { - 1 } \mathbf { x } _ { 0 } ) ,
$$

which is the equivalent of (7.6.9). Its solution is

$$
\mathbf { x } ^ { * } = ( \mathbb { P } _ { 0 } ^ { - 1 } + \mathbb { J } ^ { T } \mathbb { Q } ^ { - 1 } \mathbb { J } ) ^ { - 1 } ( \mathbb { P } _ { 0 } ^ { - 1 } \mathbf { x } _ { 0 } + \mathbb { J } ^ { T } \mathbb { Q } ^ { - 1 } \mathbf { y } )
$$

with covariance matrix of errors

$$
\begin{array} { r } { \mathbb { P } = ( \mathbb { P } _ { 0 } ^ { - 1 } + \mathbb { J } ^ { \mathcal { T } } \mathbb { Q } ^ { - 1 } \mathbb { J } ) ^ { - 1 } . } \end{array}
$$

$\mathbf { P }$ can also be written in the alternative form

$$
\mathfrak { P } = \mathbb { P } _ { 0 } - \mathfrak { P } _ { 0 } \mathfrak { J } ^ { T } ( \mathfrak { I } \mathfrak { P } _ { 0 } \mathfrak { I } ^ { T } \div \mathbf { Q } ) ^ { - 1 } \mathfrak { J } \mathbb { P } _ { 0 } .
$$

show this it is sufficient to show the truth of

$$
\begin{array} { r } { \{ \mathbf { P } _ { 0 } ^ { - 1 } + \mathbf { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbf { J } \} [ \mathbf { P } _ { 0 } - \mathbf { P } _ { 0 } \mathbf { J } ^ { T } ( \mathbf { J } \mathbf { P } _ { 0 } \mathbf { J } ^ { T } + \mathbf { Q } ) ^ { - 1 } \mathbf { J } \mathbf { P } _ { 0 } ] = \mathbb { I } _ { m } . } \end{array}
$$

So we can write (7.6.12) as

$$
\mathbf { x } ^ { * } = \mathbb { P } ( \mathbf { \vec { s } } _ { 0 } ^ { - 1 } \mathbf { x } _ { 0 } + \mathbf { \vec { s } } ^ { \mathcal { T } } \mathbf { Q } ^ { - 1 } \mathbf { y } ) ,
$$

with P given by (7.6.14).

X has m components so in (7.6.14) we invert an m-by-m matrix. If Y has n components, remember that we are using them to improve a previous estimate, so there is no reason why $\pmb { \mathcal { R } }$ should not be less than m. So the use of (7.6.14) may look more complicated,but can lead to the inversion of a matrix of lower order.No truly algebraic problems of ill-conditioning are removed,but the arithmetic can be less hazardous.

Now consider the mathematics involved in “updating” the parameters after an estimate, and using the new values to predict the following observations. The whole process starts with an estimate, $\mathbf { X } _ { 0 }$ which isused to predict the early observations,and as a result we find a correction $\mathbf { x } _ { \mathfrak { Q } } ^ { * }$ We then use this best estimate in $\mathbb { Y } _ { c } \{ \mathbb { X } _ { 0 } \} \times \mathbb { x } _ { 0 } ^ { * } \}$ to find residuals

$$
\mathbf { y } ^ { * } = \mathbf { Y } _ { o } - \mathbf { Y } _ { c } ( \mathbf { X } _ { 0 } \div \mathbf { x } _ { 0 } ^ { * } ) .
$$

The improved parameters should also be used in the calculation of $\Im$ ,to make the updating as efficient as possible. Linearizing (7.6.17),

$$
\mathbf { y } ^ { * } = \mathbf { Y } _ { o } - \mathbf { Y } _ { c } ( \mathbf { X } _ { 0 } ) - \bar { \mathbf { y } } \mathbf { x } _ { 0 } ^ { * }
$$

$$
\begin{array} { r } { \mathbf { y } = \mathbf { J } \mathbf { x } _ { \mathrm { 0 } } ^ { * } + \mathbf { y } ^ { * } . } \end{array}
$$

Then using (7.6.16) and (7.6.13),

$$
\begin{array} { r l } & { \mathbf { x } ^ { * } = \mathbb { P } [ \mathbb { P } _ { 0 } ^ { - 1 } \mathbf { x } _ { 0 } ^ { * } + \mathbb { J } ^ { T } \mathbf { Q } ^ { - 1 } ( \mathbb { J } \mathbf { x } _ { 0 } ^ { * } + \mathbf { y } ^ { * } ) ] } \\ & { \quad = ( \mathbb { P } _ { 0 } ^ { - 1 } + \mathbb { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbb { J } ) ^ { - 1 } ( \mathbb { P } _ { 0 } ^ { - 1 } \mathbf { x } _ { 0 } ^ { * } + \mathbb { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbb { J } \mathbf { x } _ { 0 } ^ { * } ) + \mathbb { P } \mathbb { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbf { y } ^ { * } } \\ & { \quad = \mathbf { x } _ { 0 } ^ { * } + \mathbb { P } \mathbb { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbf { y } ^ { * } . } \end{array}
$$

Using (7.6.14) this can be put into the alternative form

$$
\begin{array} { r l } & { \mathbf { x } ^ { * } = \mathbf { x } _ { 0 } ^ { * } + [ \mathbf { P } _ { 0 } - \mathbf { P } _ { 0 } \mathbf { J } ^ { T } ( \mathbf { J } \mathbf { P } _ { 0 } \mathbf { J } ^ { T } + \mathbf { Q } ) ^ { - 1 } \mathbf { J } \mathbf { P } _ { 0 } ] \mathbf { J } ^ { T } \mathbf { Q } ^ { - 1 } \mathbf { y } ^ { * } } \\ & { \quad = \mathbf { x } _ { 0 } ^ { * } + \mathbf { P } _ { 0 } \mathbf { J } ^ { T } [ \mathbf { I } _ { n } - ( \mathbf { J } \mathbf { P } _ { 0 } \mathbf { J } ^ { T } + \mathbf { Q } ) ^ { - 1 } ( \mathbf { J } \mathbf { P } _ { 0 } \mathbf { J } _ { T } + \mathbf { Q } - \mathbf { Q } ) ] \mathbf { Q } ^ { - 1 } \mathbf { y } ^ { * } } \\ & { \quad = \mathbf { x } _ { 0 } ^ { * } + \mathbf { P } _ { 0 } \mathbf { J } ^ { T } ( \mathbf { J } \mathbf { P } _ { 0 } \mathbf { J } ^ { T } + \mathbf { Q } ) ^ { - 1 } \mathbf { y } ^ { * } . } \end{array}
$$

Pis found from (7.6.14) as before. Remember again that $y ^ { * }$ is found by using the current best estimate of the parameters.

The formulas just described have no particular merit in most problems of diferential correction. But they can be useful if estimates are required in a hurry while the observations are being made. To carry the point further, we shall introduce time explicitly into the model. Let us suppose that the set of elements to be determined consists of the coordinates in phase space (that is, Components of position and velocity), Xo at time to,of the body whose motion is being observed. (It is quite simple to modify the formulas so that Xg might apply to osculating Keplerian elements at to.） Assume observations to be made at times t1, t2，.... As a result of observations made prior to time tk，we have made an estimate X,k-1 with statistics Po,k-1. Using this latest estimate, as we did in (7.6.17),we predict the observations Yc for the time tk,and we also observe $\yen 0$ for the same time,deriving the usual residual $\mathbb { y } _ { k }$ We want to use yk to improve the estimate of the conditions at time to: i.e., we want to find an estimate $\mathbf { x } _ { 0 , k } ^ { * }$ to add to $\mathbf { X _ { \mathfrak { d } } }$

From (7.6.20), we than have

$$
\mathbf { x } _ { 0 , k } ^ { * } = \mathbf { x } _ { 0 , k - 1 } ^ { * } + \mathbb { P } _ { 0 , k - 1 } \mathbb { J } _ { k } ^ { T } ( \mathbb { J } _ { k } \mathbb { P } _ { 0 , k - 1 } \mathbb { J } _ { k } ^ { T } + \mathbb { Q } _ { k } ) ^ { - 1 } \mathbb { J } _ { k } .
$$

Here $\mathbb { Q } _ { k }$ is the covariance matrix of the errors of the observations $\yen 9$ made at time $\ddagger _ { k }$ ， $\pmb { \mathcal { J } } _ { k }$ is the Jacobian matrix relating small changes in ${ \bf { X } } _ { \mathbb { 0 } }$ (or,better, $\{ \mathbf { X } _ { 0 } \div \mathbf { x } _ { k = 1 } ^ { * } \} \}$ to consequent changes in $\yen 1$ at time $\ddagger _ { \lambda }$ Then

$$
\begin{array} { l } { { \displaystyle { \mathbb J } _ { k } = \frac { \partial { \mathbb Y } _ { c } \left( t _ { k } \right) } { \partial { \mathbf X } \left( t _ { 0 } \right) } } } \\ { ~ = \frac { \partial { \mathbf Y } _ { c } \left( t _ { k } \right) } { \partial { \mathbf X } \left( t _ { k } \right) } \frac { \partial { \mathbf X } \left( t _ { k } \right) } { \partial { \mathbf X } \left( t _ { 0 } \right) } } \\ { ~ = { \mathbf M } _ { k } \Omega \left( t _ { k } , t _ { 0 } \right) . } \end{array}
$$

Since $Y _ { c } ( t _ { k } )$ is likely to be found from $\mathbb { X } ( \sharp _ { k } )$ byelementary formulas,which are easily differentiated, $\mathbb { M } _ { \ k }$ should be simple to compute.

$$
\Omega ( t _ { k } , t _ { 0 } ) = \frac { \partial \mathbf { X } ( t _ { k } ) } { \partial \mathbf { X } ( t _ { 0 } ) }
$$

is the matrizant or state transition matrix. Its computation and some of its properties were considered in Project 1 of the preceding section. It will be further discussed in section 11.18. From (7.6.21) and (7.6.22),

$$
\begin{array} { r } { { \bf x } _ { 0 , k } ^ { * } = { \bf x } _ { 0 , k - 1 } ^ { * } + { \bf P } _ { 0 , k - 1 } \Omega ^ { T } ( t _ { k } , t _ { 0 } ) { \bf M } _ { k } ^ { T } \mathrm { N } ( t _ { k } , t _ { 0 } ) { \bf y } _ { k } , } \end{array}
$$

where

$$
\begin{array} { r } { \mathbb { N } ( t _ { k } , t _ { 0 } ) = [ \mathbb { M } _ { k } \Omega ( t _ { k } , t _ { 0 } ) \mathbb { P } _ { 0 , k - 1 } \Omega ^ { T } ( t _ { k } , t _ { 0 } ) \mathbb { M } _ { k } ^ { T } + \mathbb { Q } _ { k } ] ^ { - 1 } . } \end{array}
$$

The covariance matrix of errors of the estimate can be written as

$$
\begin{array} { r } { \mathbf { P } _ { 0 , k } = \mathbb { P } _ { 0 , k - 1 } - \mathbf { P } _ { 0 , k - 1 } \Omega ^ { T } ( t _ { k } , t _ { 0 } ) \mathbf { M } _ { k } ^ { T } \mathbf { N } \big ( t _ { k } , t _ { 0 } \big ) \mathbf { M } _ { k } \Omega \big ( t _ { k } , t _ { 0 } \big ) \mathbf { P } _ { 0 , k - 1 } . } \end{array}
$$

These formulas can appear very complicated. It is best if you rederive ther, justifying each algebraic step. Once you are used to the method, the formulas are not hard to program, and the use of this recursive “filtering”can be very versatile. Methods of this kind are often referred to under the general label “Kalman filter";they are widely used.

# 7.6.1 Exercises

1.Justify the identity (7.6.15).

2.Suppose that just one observation is processed,uncorrelated with the preceding observations,and having rms error g. Show that J is just a rowvector and that

$$
\mathbf { p } ^ { - 1 } = \sigma ^ { - 2 } \mathbf { J } ^ { \mathcal { T } } \mathbf { J } + \mathbf { P } _ { \boldsymbol { \updownarrow } } ^ { - \boldsymbol { \updownarrow } } .
$$

Deduce from this that,for algebraic reasons,the rms errors of the estimated parameters must decrease as more observations are processed. This is a weaknessin the method.If there is an error in the model, the estimates can actually be getting worse, while the statistics say that the reverse is the case. Further, show that as the rms errors for the estimated quantities become smaller,the ability of later observations to inffuence theresults is diminished.In some operations,over many observations, the $P$ matrix isperiodically increased in magnitude.

Show that the method might be applied if only therelative weights of the observational errors are initially known.Discuss the ultimate estimation of the true rms errors of observation.

Set up a program for the use of formulas (7.6.23)-(7.6.25). At the start, you will have an estimate of X,but no statistics.One way to express this mathematically, is to let the initial $\pmb { \mathcal { P } }$ matrix be diagonal with very large components.

The method using equations $( 7 . 6 . 2 3 ) - ( 7 . 6 . 2 5 )$ involves improving initial parameters at the initial time $\ddagger _ { 0 }$ Suppose that the observations are for a mission having a motive (such as a rendezvous) at a final time $t _ { f }$ Set up equations so that values of the parameters at $\ddagger _ { f }$ are estimated recursively.

Consider the following situation. Observations are made at times $t _ { 1 } , \ t _ { 2 }$ ....As a result of observations made prior to $\ddagger _ { \star }$ ,an estimate has been madeof $\mathbb { x }$ (components of position and velocity) at time $t _ { k - 1 }$ ； call this $\mathbf { X } _ { k - 1 } ^ { \star }$ Weshallalsoveitssatistsinthecovacemt $\mathbf { \vec { \tau } } _ { k - 1 } ^ { * }$ Using this estimate, the value of $\mathbf { x }$ at time $\ddagger _ { k }$ will be found (call it $\mathbb { X } _ { k } ^ { \prime }$ ） andalso the predicted observation $\ Y _ { c } \{ t _ { k } \}$ .But $\mathbb { Y }$ will also be observed at time $\dot { \pmb { \tau } } _ { \pmb { k } }$ ,leading to a residual $\ y _ { k }$ We want to use $y _ { k }$ to find an estimate $\mathbf { X } _ { \mathbf { k } } ^ { * }$ and its statistics $\mathbb { P } _ { k } ^ { * }$ Show that the covariance matrix for ${ \bf X } _ { k } ^ { \prime }$ is

$$
\mathbf { \vec { P } } _ { k } ^ { \prime } = \Omega ( \vec { \tau } _ { k } , \vec { \tau } _ { k - 1 } ) \mathbf { \vec { P } } _ { k - 1 } ^ { * } \Omega ^ { T } ( \vec { \tau } _ { k } , \vec { \tau } _ { k - 1 } )
$$

and that if ${ \mathbb X } _ { k } ^ { * } = { \mathbb X } _ { k } ^ { \prime } \div { \mathbb X } _ { k } ^ { * }$ ：

$$
\mathbf { x } _ { k } ^ { * } = \mathbb { P } _ { k } ^ { \prime } \mathbb { M } _ { k } ^ { \mathcal { T } } ( \mathbb { M } _ { k } \mathbb { P } _ { k } ^ { \prime } \mathbb { M } _ { k } ^ { \mathcal { T } } \div \mathbb { Q } _ { k } ) ^ { - \frac { 1 } { 4 } } \mathbf { y } _ { k } ,
$$

and

with

$$
\begin{array} { r l } & { \mathfrak { P } _ { k } ^ { * } = \mathbb { P } _ { k } ^ { \prime } - \mathbb { P } _ { k } ^ { \prime } \mathbb { M } _ { k } ^ { \mathcal { T } } ( \mathbb { M } _ { k } \mathbb { P } _ { k } ^ { \prime } \mathbb { M } _ { k } ^ { \mathcal { T } } + \mathbb { Q } _ { k } ) ^ { - 1 } \mathbb { M } _ { k } \mathbb { P } _ { k } ^ { \prime } , } \\ & { \quad \quad \quad \quad \quad \quad \mathbb { M } _ { k } ^ { \mathcal { T } } = \frac { \partial \mathbb { Y } _ { c } \left( t _ { k } \right) } { \partial \mathbb { X } \left( t _ { k } \right) } . } \end{array}
$$

# The Three-Body Problem

# The Restricted Three-Body Problem - Jacobi's Integral

The general problem of the motion of three bodies (assumed to be point masses), subject only to their mutual gravitational attractions has not been solved,although many particular solutions have been found. We shall start witha discussion of the “restricted three-body problem”；here two bodies of finitemass revolve around one another in circular orbits,and a third body of infinitesimal mass moves in their field; this situation is approximately realized inmany instances in the solar system.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/d415068fb4ff18ba0b05ddfd32635e5084d265cf01a626b4b9010aba9af83903.jpg)  
Figure 8.1

Let the origin be at the center of mass of the two finite masses and take axes rotating with the masses, such that they lie along the $\mathscr { L }$ -axis. Take the unit of mass to be the sum of their masses, and let the separate masses be $\mu$ and (1-μ）,where $\mu \leq \frac { \frac { 1 } { 2 } } { 2 }$ The axes will be rotating with constant angular velocity, w, say, and the bodies will be fixed at $\{ { \underline { { x } } } _ { 2 } , { \widehat { 0 } } , { \widehat { 0 } } \}$ and $\{ x _ { I } , 0 , 0 \}$ ，where isnegative. (See Figure 8.1.） Let the unit of distance be $( - x _ { 1 } + x _ { 2 } )$ ,and let the unit of time be such as to make $k = 1$ . Then, in these units,

$$
\begin{array} { c } { { \omega = k \sqrt [ ] { \frac { ( 1 - \mu ) + \mu } { ( - x _ { 1 } + x _ { 2 } ) ^ { 3 } } } } } \\ { { = 1 . } } \end{array}
$$

Let the infinitesimal mass be at $( x , y , z )$ and let

$$
( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } = r _ { 1 } ^ { 2 }
$$

and

$$
\left( x - x _ { 2 } \right) ^ { 2 } \div y ^ { 2 } + z ^ { 2 } = r _ { 2 } ^ { 2 } .
$$

If $\mathfrak { V }$ is the speed of the infinitesimal mass with respect to the moving axes,

$$
v ^ { 2 } = { \dot { z } } ^ { 2 } + { \dot { y } } ^ { 2 } + { \dot { z } } ^ { 2 }
$$

and the modified energy integral (see (3.4.8)) is

$$
v ^ { 2 } = x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( 1 - \mu ) } { r _ { 1 } } } \div { \frac { 2 \mu } { r _ { 2 } } } - C ;
$$

where $C$ is a constant. (8.1.1) is Jacobi's integral.

Five more integrals are needed to complete the solution (angular momentum obviously tells us nothing here), but these are not known.However,many properties of the motion can be found from a discussion of (8.1.1),and the following few sections will be devoted to this.

# 8.2Tisserand's Criterion for the Identification of Comets

Let the infinitesimal mass have position vector $\sum ^ { q }$ with respect to nonrotating axes,with the same origin as before; then if $\hat { \pmb z }$ is the axis of rotation,

$$
\frac { d \pmb { \updownarrow } } { d t } = \frac { d \pmb { \updownarrow } ^ { \prime } } { d t } - \hat { \pmb { \ z } } \times \pmb { \rho } ,
$$

where $p$ is the vector with components $\{ { \mathfrak { x } } ^ { \sharp } , { \mathfrak { y } } ^ { \prime } , \emptyset \}$ or $\{ \mathfrak { x } , \mathfrak { y } , \emptyset \}$ .Then

$$
\begin{array} { r l } & { \left( \frac { d \mathbf { r } } { d t } \right) ^ { 2 } = \left( \frac { d \mathbf { r } ^ { \prime } } { d t } \right) ^ { 2 } - 2 \left( \frac { d \mathbf { r } ^ { \prime } } { d t } \right) \cdot ( \hat { \mathbf { z } } \times \boldsymbol { \rho } ) + \boldsymbol { \rho } ^ { 2 } } \\ & { \qquad = \left( \frac { d \mathbf { r } ^ { \prime } } { d t } \right) ^ { 2 } - 2 \hat { \mathbf { z } } \cdot \left( \boldsymbol { \rho } \times \frac { d \mathbf { r } ^ { \prime } } { d t } \right) + \boldsymbol { \rho } ^ { 2 } } \\ & { \qquad = \left( \frac { d \mathbf { r } ^ { \prime } } { d t } \right) ^ { 2 } - 2 \hat { \mathbf { z } } \cdot \left( \mathbf { r } ^ { \prime } \times \frac { d \mathbf { r } ^ { \prime } } { d t } \right) ^ { \hat { \mathbf { z } } } + \boldsymbol { x } ^ { 2 } + \boldsymbol { y } ^ { 2 } . } \end{array}
$$

Jacobi's integral becomes

$$
\dot { \bar { \mathbf { x } } } ^ { r 2 } - 2 \hat { \mathbf { z } } \cdot ( \mathbf { r } ^ { \prime } \times \hat { \bar { \mathbf { x } } } ^ { \prime } ) = \frac { 2 ( 1 - \mu ) } { r _ { 1 } } + \frac { 2 \mu } { r _ { 2 } } - C .
$$

Now let the infinitesimal mass be a periodic comet,and $\{ 1 - \mu \}$ and $\mathcal { Y }$ the masses of the Sun and Jupiter,respectively,so that $\mu \sim 1 0 ^ { - 3 }$ If we find the

osition and velocity of the comet at any time, from observations,wc shall lrnlate elements from

$$
\dot { \bar { \mathbf { r } } } ^ { 2 2 } = \frac { 2 } { \bar { \mathbf { z } } } - \frac { 1 } { \bar { \mathbf { z } } }
$$

$$
\hat { { \bf z } } \cdot ( { \bf r ^ { \prime } } \times \dot { \bf r ^ { \prime } } ) = \hat { { \bf z } } \cdot { \bf h } = \sqrt { a ( 1 - e ^ { 2 } ) } \cos i .
$$

Substituting these expressions into (8.2.1)， we find

$$
\frac { 1 } { a } + 2 \sqrt { a ( \frac { 1 } { 2 } - e ^ { 2 } ) } \cos i = \frac { 2 } { r } - \frac { 2 ( 1 - \mu ) } { r _ { 1 } } - \frac { 2 \mu } { r _ { 2 } } + C .
$$

Now $\scriptstyle { \mathfrak { p } }$ is nearly equal to $\pmb { \gamma } _ { \mathtt { I } }$ so that, approximately,

$$
\frac { \ddagger { } } { a } + 2 \sqrt { a ( 1 - e ^ { 2 } ) } \cos i = 2 \mu \left( \frac { \Bbbk } { r _ { 1 } } - \frac { \lambda } { r _ { 2 } } \right) + C .
$$

Suppose the comet to be observed before and after a close approach to upiter;provided the comet is far from Jupiter when observed,r1 and r2 will elarge and nearly equal, and we have approximately

$$
\frac { 1 } { a } + 2 \sqrt { a ( 1 - e ^ { 2 } ) } \cos i = C .
$$

Now,because of perturbations by Jupiter, the elements of the comet will have changed, and it is possible that they will have changed so considerably that identification is difficult (i.e., we are not sure whether it is the old comet or a new one). But C is constant throughout,so if a1,e1,i1 refer to the old orbit anda2,e2,i2 to the new orbit,we must have approximately

$$
\frac { \mathbb { 1 } } { a _ { 1 } } + 2 \sqrt { a _ { 1 } ( 1 - e _ { 1 } ^ { 2 } ) } \cos i _ { 1 } = \frac { 1 } { a _ { 2 } } + 2 \sqrt { a ( 1 - e _ { 2 } ^ { 2 } ) } \cos i _ { 2 } .
$$

This criterion is due to Tisserand.

# The Surfaces of Zero Relative Velocity

we put $v = 0$ in (8.1.1), we have the equation

$$
x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( \ I - \mu ) } { r _ { 1 } } } + { \frac { 2 \mu } { r _ { 2 } } } = C .
$$

For some value of $C$ this will be the locus of surfaces in space to be described shortly. If we consider (8.1.1) as a function of ${ \mathfrak { v } } ^ { 2 }$ , then we see that ${ \mathfrak { Y } } ^ { 2 }$ changes sign when a surface is crossed (as long as the crossing does not take place at a double point). Hence the motion can take place on one side of the surface but not on the other.This is similar to the theorem in the problem of two bodies, that the finite motion is restricted within a circle of radius $2 a$ (also deduced from the energy integral). The construction of the surfaces is described in some detail in Moulton (Ref.11,pp.281-290)；we shall give only a rough description here. If C is large (it must,of course, be positive), we have the three alternatives:

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/39c53b75da9f417ba5b408ca1cce120476f0ac939665183fdb1f30202b632e8c.jpg)  
Figure 8.3

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/f0a809f8593212762399c103e2f8d3660cef44591f8fe887a0c1024d42e39be3.jpg)  
Figure 8.2

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/a389771e625a2e21fc21074944ee2500159ca044b2600dc4f79780b75f18912f.jpg)  
Figure 8.4

$$
x ^ { 2 } + y ^ { 2 } = C { \pmod { \frac { 1 } { 4 } } } y \colon
$$

or

$\mathfrak { F } _ { \mathfrak { T } }$ is very small

Hence we have,roughly, $\mathtt { a }$ cylinder with circular cross-section, parallel to the $z$ -axis,and two small ovoids surrounding the finite masses. The larger ovoid is around the heavier mass, $I - \mu$ For this value of $C$ the motion of the infinitesimal body can take place outside the cylinder or inside one of the ovoids. The situation in the $x - y$ plane is illustrated in Figure $8 . 2 a$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/ccfccb4cffc4cefad81e6efe839a82e943e4df8f7197ad70dba1ac6014c65b15.jpg)  
Figure 8.5

Now let $C$ decrease. The “cylinder" shrinks (and acquiresa“waist” in the x-y plane)， and the ovoids expand until they coalesce; this will take place in the x-y plane at a point closer to $\beta$ than to $1 - \mu$ This is illustrated in Figure $8 . 2 \%$

As $C$ decreases further, the wall of the cylinder meets the smaller and later the larger of the ovoids (see Figures 8.2c and 8.2d). Finally we are left with two tadpole-like shapes that eventually shrink to points (see Figure 8.2e). The parts of Figure 8.2 can be combined into one,and this is shown in Figure 8.3. Similar sections in the $_ { x - z }$ and $y - z$ planes are shown in Figures 8.4 and 8.5.

Figures 8.6 and 8.7 show two aspects of the surface

$$
z = x ^ { 2 } + y ^ { 2 } + { \frac { 2 ( \pm - \mu ) } { r _ { 1 } } } + { \frac { 2 \mu } { r _ { 2 } } }
$$

vherer²=（x+μ）²+y²， $r _ { 2 } ^ { 2 } = ( x - 1 + \mu ) ^ { 2 } + y ^ { 2 }$ with $z = 0 . 4$ The level curves orrespond to curves of zero velocity in Figure 8.3.

These limiting surfaces were first discussed by Hillin relation to the motion the Moon.

If you have graphics facilities on your computer, you should write a program to generate these curves. See Ref. 45 for some remarkable computer-generated representations of the three-dimensional surfaces.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/9d8de7effaa55a07770e6ee6b634259567cdf77cf3f4d2e4a1acbb673ce0a90a.jpg)  
Figure 8.6

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/032fda83a017f7e070d975bb1b6e3c8e4992ebd0d632debe8e7e407d966819b8.jpg)  
Figure 8.7

# 8.4The Positions of Equilibrium

All the double points involved in the surfaces discussed in Section 8.3 occur in the x-y plane. We might expect these to have some significance in the solution, and they are, in fact, positions of equilibrium, as we shall now show.

Let $\pmb { \gamma }$ be the“modified potential"；then

$$
- \sqrt { \frac { 1 } { 2 } ( x ^ { 2 } + y ^ { 2 } ) + \frac { 1 - \mu } { r _ { 1 } } } + \frac { \mu } { r _ { 2 } } .
$$

The equation of motion is

$$
\ddot { \bar { x } } + 2 \hat { \bar { z } } \times \dot { \bar { \rho } } = - \nabla \bar { \mathcal { V } } . \qquad \overset { \overset { \cdot } { \longleftarrow } } { \overleftarrow { \bar { \bar { \bar { \tau } } } \cdot \bar { \bar { \bar { \tau } } } - \bar { \bar { \Psi } } } } .
$$

Suppose the infinitesimal body to be initially at rest (with respect to the rotating axes)； it will start to move off in the direction of $- \nabla \Vdash$ The surfaces described in Section 8.3 are given by the function

$$
\begin{array} { r } { F ( x , y , z ) \equiv V \div \frac { 1 } { 2 } C = 0 . } \end{array}
$$

Now the normal at any point on a surface has direction cosines that are proportional to dF/dx,aF/dy,and aF/dz,so it is in the direction of-VV. Therefore,the infinitesimal body,initially at rest,will start to move off in the direction of the normal to the surface through the point which it occupies. But suppose this is to be a double point;then there is not a unique normal. The body has no reason for moving off in one direction rather than another,and unless it receivesa small nudge it will stay where it is. (This is similar to the situation of the student, who, having two lectures of equal importance at the same time,goes to neither.) The double points are therefore positions of equilibrium. The double points occur at stationary values of $\pmb { \xi }$ the condition for this being

$$
\frac { \partial \mathcal { F } } { \partial x } = \frac { \partial \mathcal { F } } { \partial y } = \frac { \partial \mathcal { F } } { \partial z } = 0 .
$$

Now we have

$$
\frac { \partial \bar { F } } { \partial z } \equiv z \left( \frac { 1 - \mu } { r _ { \perp } ^ { 3 } } \div \frac { \mu } { r _ { 2 } ^ { 3 } } \right)
$$

so that any double point occurs in the $x - y$ plane,for which $z = 0$ Then we can put $z = 0$ ,and find the conditions for $\partial \mathcal { F } / \partial \boldsymbol { x } = \boldsymbol { \updownarrow }$ and $\partial \mathscr { F } / \partial \mathscr { y } = \mathscr { G }$ They are

$$
x - ( \mathrm { i } - \mu ) \frac { x - x _ { 1 } } { r _ { 1 } ^ { 3 } } - \mu \frac { x - x _ { 2 } } { r _ { 2 } ^ { 3 } } = 0
$$

and

$$
\begin{array} { r } { y - ( \mathtt { i } - \mathtt { i } \mathtt { i } ) \frac { \mathtt { j } } { \mathtt { j } \mathtt { i } } - \mu \frac { y } { \tau _ { 2 } ^ { 3 } } = 0 . } \end{array}
$$

(8.4.5) is satisfied if $y = 0$ ,and in this case (8.4.4) becomes

$$
z - ( \mathrm { i } - \mu ) \frac { x - x _ { 1 } } { \vert x - x _ { 1 } \vert ^ { 3 } } - \mu \frac { x - x _ { 2 } } { \vert x - x _ { 2 } \vert ^ { 3 } } = 0 .
$$

(Here lal indicates that the positive value of a is used.） The left-hand side of (8.4.6), considered asa function of x, has a graph of the form shown in Figure 8.8.The verification of this graph (after the fashion of that of Figure 5.6) is left as an exercise to the reader. There are, then, three real roots,and this was tobe expected from the three double points on the $\boldsymbol { \mathfrak { x } }$ -axisappearing in Figure 8.3.These are called the Lagrangian points, $\mathbb { L } _ { \ I } , \mathbb { L } _ { 2 }$ ,and $\mathbb { L } _ { 3 }$ ，

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0121-0160/ocr/images/15d50b3f1c4d1eb2156c3ef40778d85503dfd5621cbe593878cd6bd79220e060.jpg)  
Figure 8.8

Now consider what happens when $y \neq 0$ (8.4.5） becomes

$$
1 - \frac { 1 - \mu } { r _ { 1 } ^ { 3 } } - \frac { \mu } { r _ { 2 } ^ { 3 } } = 0 .
$$

ultiply this by $\{ \mathfrak { z } - \mathfrak { z } _ { 2 } \}$ and $\{ \mathfrak { x } - \mathfrak { x } _ { \mathtt { i } } \}$ and subtract the products separately rom (8.4.4）.We find

$$
x _ { 2 } - ( 1 - \mu ) \frac { x _ { 2 } - x _ { 1 } } { r _ { 1 } ^ { 3 } } = 0
$$

$$
x _ { 1 } - \mu \frac { x _ { 1 } - x _ { 2 } } { r _ { 1 } ^ { 3 } } = 0 . \nonumber
$$

3ut ${ \mathfrak { X } } _ { 2 } = { \mathfrak { I } } - { \mathfrak {mu } }$ and $x _ { 1 } = - \mu$ since the6rigin is at the center of mass of the mite masses,so that these equationsreduce to

These points of equilibrium form equilateral triangles in the $x - y$ plane with the two finite masses. They are the Lagrangian points $\pmb { \mathcal { Z } } _ { 4 }$ （ $\dot { \mathfrak { x } }$ positive) and $\pm _ { 5 }$ 美

# 8.5The Stability of the Points of Equilibrium

In the preceding section we argued that the infinitesimal body would remain at a double point unless it received a slight nudge. If,for any such nudge, the motion that follows consists of small oscillations about the double point,the position of equilibrium is said to be stable; if,for some possible nudges,the body recedes indefinitely from the double point, the position is unstable. Therefore, tofind out whether a position of equilibrium found above is stable,we must investigate the motion of the infinitesimal body if it is slightly displaced from that position. In practice (unless we assume the three bodies to be totally isolated) this will be constantly happening as a result of perturbations.

The word “stability” has many interpretations. Here, we consider “linear stability."

Let the position of equilibrium be at $\{ x , y , z \}$ and let the body be displaced to $( x \div \xi , y + \eta , z \div \zeta )$ where $\xi , \eta$ and $5$ are small; we assume,until it may be proved to the contrary, that these quantities remain small. If we neglect their squares and products and remember that ${ \partial V } / { \partial x } = 0 .$ etc.,at $\{ x , y , z \}$ ,then the equations of motion are

$$
\begin{array} { r l r } & { } & { \ddot { \xi } - 2 \dot { \eta } = - \xi V _ { x x } - \eta V _ { x y } - \zeta V _ { x z } , } \\ & { } & { \ddot { \eta } + 2 \dot { \xi } = - \xi V _ { y z } - \eta V _ { y y } - \zeta V _ { y z } , } \\ & { } & { \ddot { \zeta } \quad = - \xi V _ { z z } - \eta V _ { z y } - \zeta V _ { z z } , } \end{array}
$$

where $V _ { y z }$ stands for $\partial ^ { 2 } V / \partial y \partial z$ ,etc., and these quantities are evaluated at the point of equilibrium so that they have constant values.

Now

$$
\begin{array} { c } { { - V = \frac 1 2 ( x ^ { 2 } + y ^ { 2 } ) + ( 1 - \mu ) \{ ( x - x _ { 1 } ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } \} ^ { - 1 / 2 } } } \\ { { + \mu \{ ( x - x _ { 2 } ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } \} ^ { - 1 / 2 } . } } \end{array}
$$

Define $\alpha$ and $\beta$ by

$$
\alpha = \frac { 1 - \mu } { r _ { 1 } ^ { 3 } } + \frac { \mu } { r _ { 2 } ^ { 3 } }
$$

and

$$
\beta = \frac { 1 - \mu } { r _ { 1 } ^ { 5 } } + \frac { \mu } { r _ { 2 } ^ { 5 } } ;
$$

then we find

$$
\begin{array} { r l } & { V _ { x x } = - 1 + \alpha - 3 ( 1 - \mu ) \frac { ( x - x _ { 1 } ) ^ { 2 } } { r _ { 1 } ^ { 5 } } - 3 \mu \frac { ( x - x _ { 2 } ) ^ { 2 } } { r _ { 2 } ^ { 5 } } , } \\ & { V _ { y y } = - 1 + \alpha - 3 y ^ { 2 } \beta , } \\ & { V _ { z z } = \alpha - 3 z ^ { 2 } \beta , } \\ & { V _ { y z } = - 3 y z \beta , } \end{array}
$$

$$
\begin{array} { r l } & { V _ { z x } = - 3 ( 1 - \mu ) \frac { z \left( x - x _ { 1 } \right) } { \tau _ { 1 } ^ { 5 } } - 3 \mu \frac { z \left( x - x _ { 2 } \right) } { \tau _ { 2 } ^ { 5 } } , } \\ & { V _ { z y } = - 3 ( 1 - \mu ) \frac { y \left( x - x _ { 1 } \right) } { \tau _ { 1 } ^ { 5 } } - 3 \mu \frac { y \left( x - x _ { 2 } \right) } { \tau _ { 2 } ^ { 5 } } . } \end{array}
$$

For a straight-line solution for which $\mathfrak { Y } ^ { \prime } = z = \mathbb { 0 }$ and ${ \mathfrak { X } } = { \mathfrak { Z } } _ { 0 }$ ,say， we have

$$
r _ { \bar { \tau } } ^ { 2 } = ( x _ { 0 } - x _ { \bar { 1 } } ) ^ { 2 } \mathrm { a r a d } r _ { 2 } ^ { 2 } = ( x _ { 0 } - x _ { 2 } ) ^ { 2 } .
$$

$$
\bar { \mathbb { V } } _ { y z } = \mathbb { V } _ { z x } = \mathbb { V } _ { z y } = \mathbb { 0 } ,
$$

othe equations of motion following a small displacement are

$$
\begin{array} { c } { { \ddot { \xi } - 2 \dot { \eta } = \xi ( 1 + 2 \alpha ) , } } \\ { { \ddot { \eta } + 2 \dot { \xi } = \eta ( 1 - \alpha ) , } } \\ { { \ddot { \zeta } = - \zeta \alpha . } } \end{array}
$$

Since $\alpha$ is positive, the oscillations in the $z$ -direction are finite and small, and herefore stable,and we can concentrate on the first two equations.

Wetry a solution $\xi = K e ^ { \lambda t }$ ， $\mathfrak { A } = \mathcal { L } e ^ { \lambda \mathfrak { L } }$ .If $\lambda$ is purely imaginary, then the solution can be put entirely in the form of sines and cosines,and the motion, consisting of finite oscillations,will be stable. Otherwise the solution must involve hyperbolic functions; then $\xi$ and $\eta$ will increase without limit,and the motion is unstable. Substituting the trial solutions into the equations of motion, we have

$$
{ \cal K } \lambda ^ { 2 } - 2 \bar { \lambda } \lambda = { \cal K } ( \bar { \lambda } + 2 \alpha )
$$

$$
\bar { \mathcal { L } } \lambda ^ { 2 } + 2 \mathcal { K } \lambda = \bar { \mathcal { L } } \{ 1 - \alpha \} .
$$

Eliminating $\kappa$ and $\pmb { \bar { \mathcal { L } } }$ we fnd

$$
\left| \begin{array} { c c } { { \lambda ^ { 2 } - ( 1 + 2 \alpha ) } } & { { - 2 \lambda } } \\ { { 2 \lambda } } & { { \lambda ^ { 2 } - ( \mathtt { i } - \alpha ) } } \end{array} \right| = 0
$$

$$
\lambda ^ { 4 } \div \lambda ^ { 2 } ( 2 - \alpha ) + ( 1 + 2 \alpha ) ( 1 - \alpha ) = 0 .
$$

For stability $\lambda$ must be purely imaginary so that there must be two real negative reotsfor $\lambda ^ { 2 }$ ;for this to be so,we must at least have

$$
z - \alpha > 0 ,
$$

since the product of the roots must be positive, or

$$
\frac { \mathbb { i } } { \varepsilon } - \frac { \mathbb { i } } { r _ { 1 } ^ { 3 } } \div \mu \left( \frac { \mathbb { i } } { r _ { 1 } ^ { 3 } } - \frac { \mathbb { i } } { r _ { 2 } ^ { 3 } } \right) > \mathbb { 0 } .
$$

From Figure 8.6 we see that (8.4.6) has:

a positive root greater than $\mathfrak { X } _ { 2 }$ ,when $\pmb { \mathcal { F } } _ { \mathfrak { T } }$ is greater than $\uparrow _ { 2 }$ a positive root between $\boldsymbol { \mathcal { Z } } _ { \mathtt { I } }$ and $x _ { 2 }$ ,when $\gamma _ { \gimel }$ is greater than $\tau _ { 2 }$ ： $\bigstar$ a negative root less than $\pmb { \mathcal { Z } } _ { \mathfrak { I } }$ ,when $\mathfrak { F } _ { \mathfrak { T } }$ is less than ${ \mathfrak { T } } _ { 2 }$

Now (8.4.6) can be written in the form

$$
x _ { 0 } ( 1 - \alpha ) + ( 1 - \mu ) \frac { x _ { 1 } } { x _ { 1 } ^ { 3 } } + \mu \frac { x _ { 2 } } { x _ { 2 } ^ { 3 } } = 0
$$

or, since $x _ { I } = - \mu$ and $x _ { 2 } = 1 - \mu ,$

$$
x _ { 0 } ( \mathrm { \vec { i } } - \alpha ) - \mu ( \mathrm { \vec { i } } - \mu ) \left\{ \frac { \mathrm { \vec { i } } } { r _ { 1 } ^ { 3 } } - \frac { 1 } { r _ { 2 } ^ { 3 } } \right\} = 0 .
$$

So

$$
( 1 - \alpha ) = \frac { \mu ( 1 - \mu ) } { x _ { 0 } } \left\{ \frac { 1 } { r _ { 1 } ^ { 3 } } - \frac { \vec { \mathtt { j } } } { r _ { 2 } ^ { 3 } } \right\} .
$$

It is clear from inspection that for each solution $\{ I - \alpha \}$ is negative. Therefore the straight-line solutions are unstable. Actually some displacements lead to finite oscillations (such as.the oscillations in the $z \cdot$ direction),but for stability all possible displacements must lead to these. When testing for stability, it is not sufficient to try some special displacements.

If we assume that the orbit of the Earth around the Sun is circular, we can find the three straight-line positions of equilibrium, one of which is on the side of the Earth away from the Sun. It has been argued that meteoric material may be temporarily trapped in this position and that this explainsa very faint glow seen in the night sky in a position exactly opposite the (invisible) Sun,called the gegenschein; the glow would be the reflection of sunlight from the trapped material. A meteoric particle trapped in this position must remain there for a short time if it were lucky in its perturbations, but it would eventually move away. The reader may object to the statement made earlier that the particle would “recede indefinitely” from the position of equilibrium;the objection is valid,since in this example the displaced meteoric material will remain indefinitely within the solar system. But the phrase is intended to apply only to the perturbed equations (8.5.1), which are approximate,and not necessarily to motion farther afield.

Next consider the stability of the triangular solutions. We have ${ \mathfrak { r } } _ { \sharp } = { \mathfrak { r } } _ { 2 } = { \mathfrak { z } }$ so that

$$
x = { \frac { 1 } { 2 } } ( 1 - 2 \mu ) , y = \pm { \frac { \sqrt { 3 } } { 2 } } , a n d z = 0 .
$$

We can take the positive sign for $y$ without loss of generality. The values of $\mathbb { V } _ { i j }$ that are not zero are

$$
\mathbb { V } _ { z x } = - \frac { 3 } { 4 } ,
$$

$$
\begin{array} { l } { { \displaystyle V _ { y y } = - \frac { 9 } { 4 } , } } \\ { { \displaystyle V _ { z z } = 1 , } } \\ { { \displaystyle V _ { x y } = - \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) . } } \end{array}
$$

The equations of motion are

$$
\begin{array} { c } { { \displaystyle { \ddot { \xi } - 2 \dot { \eta } = \frac { 3 } { 4 } \xi + \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) \eta , } } } \\ { { \displaystyle { \ddot { \eta } + 2 \dot { \xi } = \frac { 9 } { 4 } \eta + \frac { 3 \sqrt { 3 } } { 4 } ( 1 - 2 \mu ) \xi , } } } \\ { { \displaystyle { \ddot { \zeta } = - \zeta . } } } \end{array}
$$

The oscillations in the $z$ direction are stable,the period being the same as that of the revolution of the finite bodies. To investigate the first two equations, we again try $\xi = K e ^ { \lambda t }$ ： $\mathfrak { z } \mathfrak { z } = \underline { { \mathtt { L } } } e ^ { \lambda \mathfrak { z } }$ Substituting, and eliminating $\kappa$ and $L$ as before,we find

$$
\lambda ^ { 4 } \div \lambda ^ { 2 } \div \frac { 2 7 } { 4 } \mu ( 1 - \mu ) = 0 .
$$

Considered as a quadratic for $\lambda ^ { 2 }$ ,this equation must have real negative roots for stability. But the sum of the roots is negative and their product is positive; so, provided the roots are real, they must be negative. Hence,to find the condition for stability, it is sufficient to find the condition for real roots. This is

$$
1 - \frac { \mathscr { s } } { \mathscr { s } } \cdot \frac { 2 \mathscr { T } } { \mathscr { s } } \mu \{ 1 - \mathscr { s } \} > 0
$$

$$
1 - 2 7 \mu ( 1 - \mu ) > 0 .
$$

Putting the left-hand side equal to ε, and solving the resulting quadratic for μ, we find

$$
\mu = \frac { 1 } { 2 } \pm \sqrt { \frac { 2 3 \div 4 \varepsilon } { 1 0 8 } } .
$$

ince $\begin{array} { r } { \mu \leq \frac { 1 } { 2 } } \end{array}$ , we take the lower sign. The condition for stability is $\varepsilon > 0$ or

$$
\mu < \frac { 1 } { 2 } - \sqrt { \frac { 2 3 } { 1 0 8 } } = 0 . 3 8 5 \ldots = \mu _ { 1 } .
$$

This condition is satisfied for Jupiter and the $\mathtt { S z m }$ and in fact we do find some minor planets, called the Trojans, oscillating about the triangular positions. These oscillations are considerable, amounting to as much as $2 0 ^ { \circ }$ in longitude so that the small oscillations considered above cannot be applied to the actual motion; they merely ensure linear stability.

The investigation of general, non-linear stability requires mathematics and industry of $\gtrdot$ higher order than that applied here. The triangular points have been proved stable for $0 < \mu < \mu _ { 1 }$ excluding the values $\begin{array} { r } { \mu _ { 2 } = \frac { 3 } { 2 } \overline { { \left( 1 - \frac { 3 } { 4 5 } \sqrt { 1 8 3 3 } \right) } } = } \end{array}$ 0.0243..and $\begin{array} { r } { \mu _ { 3 } = \frac { 3 } { 2 } \left( \mathbb { 1 } - \frac { 2 } { 4 5 } \sqrt { \mathbb { 1 } \mathbb { 1 } 7 } \right) = 0 . 0 \mathbb { 1 } 3 5 . . } \end{array}$ See problem 26at the end of this chapter. $\therefore \because$

# 8.6The Lagrangian Solutions for the Motion of Three Finite Bodies

The equations of motion for three finite bodies are

$$
\begin{array} { r l } & { \ddot { \bar { \mathbf { r } } } _ { \mathrm { I } } = - m _ { 2 } \frac { \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 } } { r _ { 1 2 } ^ { 3 } } - m _ { 3 } \frac { \mathbf { r } _ { 1 } - \mathbf { r } _ { 3 } } { r _ { 1 3 } ^ { 3 } } , } \\ & { \ddot { \bar { \mathbf { r } } } _ { 2 } = - m _ { 3 } \frac { \mathbf { r } _ { 2 } - \mathbf { r } _ { 3 } } { r _ { 2 3 } ^ { 3 } } - m _ { 1 } \frac { \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } } { r _ { 2 1 } ^ { 3 } } , } \\ & { \ddot { \bar { \mathbf { x } } } _ { 3 } = - m _ { 1 } \frac { \mathbf { r } _ { 3 } - \mathbf { r } _ { 1 } } { r _ { 3 1 } ^ { 3 } } - m _ { 2 } \frac { \mathbf { r } _ { 3 } - \mathbf { r } _ { 2 } } { r _ { 3 2 } ^ { 3 } } . } \end{array}
$$

Here ${ \mathfrak { r } } _ { i j } = \left\{ { \mathfrak { r } } _ { j } \cdots { \mathfrak { r } } _ { i } \right\} .$ the unit of time is chosen to make $\acute { \kappa } = \acute { \bar { \kappa } }$

If the equations are multiplied by $\gamma _ { \uparrow \uparrow , \ \uparrow \uparrow \cdot \ 2 }$ ,and $\yen 3$ ,respectively，and added, the terms on the right-hand side vanish,and the equation can be integrated to yield the fact that the center of mass of the three bodies moves in a straight line with constant speed. We can,then, take the center of mass as a new origin, so that

$$
m _ { \updownarrow } { \updownarrow } _ { 1 } + m _ { 2 } { \updownarrow } _ { 2 } + { \uparrow } n _ { 3 } { \updownarrow } _ { 3 } = 0 .
$$

We shall look for solutions for which the geometrical form of the configuration remains the same. The scale can change and the figure can rotate, but that is all. A solution of this type is called a homographic solution. We have already found two such solutions for the restricted three-body problem,where the scale remains constant. We shall start by seeing if the equations (8.6.1) can be satisfied if the configuration is an equilateral triangle. In this case,

$$
r _ { 2 3 } = r _ { 3 1 } = r _ { 1 2 } = \mathfrak { r } ,
$$

where $\mathfrak { P }$ need not be constant. On substitution, the frst equation of (8.6.1) becomes

$$
\ddot { \bf r } _ { 1 } = - \frac { \hat { 1 } } { r ^ { 3 } } [ m _ { 2 } ( { \bf r } _ { 1 } - { \bf r } _ { 2 } ) + m _ { 3 } ( { \bf r } _ { 1 } - { \bf r } _ { 3 } ) ] .
$$

From (8.6.2) we have

$$
m _ { 2 } ( { \bf r } _ { 1 } - { \bf r } _ { 2 } ) + m _ { 3 } ( { \bf r } _ { 1 } - { \bf r } _ { 3 } ) = { \bf r } _ { 1 } ( m _ { 1 } + m _ { 2 } + m _ { 3 } ) ~ .
$$

so that (8.6.3) becomes

$$
{ \ddot { x } } _ { 1 } = - ( m _ { 1 } + m _ { 2 } + m _ { 3 } ) { \frac { { \pmb { \tau } } _ { 1 } } { p ^ { 3 } } } .
$$

Squaring (8.6.4), we find

$$
\begin{array} { c } { { \tt r _ { 1 } ^ { 2 } ( m _ { 1 } + m _ { 2 } + m _ { 3 } ) ^ { 2 } = m _ { 2 } ^ { 2 } r _ { 1 2 } ^ { 2 } + 2 m _ { 2 } m _ { 3 } r _ { 1 2 } r _ { 1 3 } \cos 6 0 ^ { \circ } + m _ { 3 } ^ { 2 } r _ { 1 3 } ^ { 2 } } } \\ { { = r ^ { 2 } ( m _ { 2 } ^ { 2 } + m _ { 2 } m _ { 3 } + m _ { 3 } ^ { 2 } ) . } } \end{array}
$$

So (8.6.5） becomes

$$
\begin{array} { r } { \ddot { \bar { \mathbf { r } } } _ { \vdots } = - \hat { M } _ { \vdots } \frac { \bar { \mathbf { r } } _ { \vdots } } { \bar { r } _ { \vdots } ^ { 3 } } , } \end{array}
$$

$$
M _ { 1 } = \frac { ( m _ { 2 } ^ { 2 } + m _ { 2 } m _ { 3 } + m _ { 3 } ^ { 2 } ) ^ { 3 / 2 } } { ( m _ { 1 } + m _ { 2 } + m _ { 3 } ) ^ { 2 } } .
$$

Hence $\mathcal { W } \mathbb { 1 }$ moves in a central orbit around the fixed center of mass as though amass $M _ { 1 }$ were located there; it will continue to do so as long as the configuration of the three bodies is maintained. Similar results follow for the other two bodies.Then,as long as the initial conditions are right, the equations of motion will ensure that the fgure remains an equilateral triangle. Initially, we must obviously have the masses at the apices of an equilateral triangle, and the velocities must be such as to cause the figure to remain an equilateral triangle, independently of the accelerations caused by the gravitational forces. For this tobe so,the initial velocitiesmust be proportional to the distances $\gamma _ { \hat { \textbf { 2 } } }$ and must make equal angles with the directions $\hat { \pmb { \tau } } _ { i }$

We notice that in the case considered above, the resultant force $\mathbb { E } _ { i }$ acting on m, passes through the center of mass, and that if $\Sigma _ { i }$ is force per unit mass, then

$$
{ \bar { \mathcal { F } } } _ { 1 } : { \mathcal { F } } _ { 2 } : { \bar { \mathcal { F } } } _ { 3 } = { r } _ { 1 } : { \bar { \tau } } _ { 2 } : { r } _ { 3 } .
$$

These two conditions,together with those ensuring that the initial conditions areright,are necessary and suffcient for the configuration of masses to remain inthe same original geometrical form,aswe shall now show.

The motion of a homographic solution is confined to a plane. I know of no soncise proof that this is the case,and it will be assumed in this discussion. For aproof that is not concise,see Ref. 44).

We:start by showing that the frst condition is necessary. The fact that the shape of the configuration is maintained means that the relative distances are given by

$$
\begin{array} { r } { \frac { \tilde { r } _ { 2 3 } } { \tilde { r } _ { 2 3 } } = \frac { \tilde { r } _ { 3 1 } } { \tilde { r } _ { 3 1 } } = \frac { \tilde { r } _ { 1 2 } } { \tilde { r } _ { 1 2 } } = \lambda ( t ) , } \end{array}
$$

where the zero superscript indicates the value at $t _ { \Updownarrow }$ (8.6.4) is true generally; squaring both sides we find

$$
\begin{array} { r l } & { \frac { 1 } { 2 } ( 2 + \gamma + 2 ) ( \frac { 2 \gamma } { 1 2 } + m _ { 2 } + m _ { 3 } ) ^ { 2 } r _ { 1 } ^ { 2 } = m _ { 2 } ^ { 2 } r _ { 1 2 } ^ { 2 } + m _ { 3 } ^ { 2 } r _ { 1 3 } ^ { 2 } + 2 m _ { 2 } m _ { 3 } r _ { 1 2 } r _ { 1 3 } \cos { \theta _ { 2 3 } } } \\ & { \frac { 1 } { 2 } ( 2 + \gamma + 3 ) ( m _ { 2 } + m _ { 3 } ) ^ { 2 } r _ { 1 } ^ { 2 } = \langle \lambda ( t ) \rangle ^ { 2 } ( m _ { 2 } ^ { 2 } \hat { r } _ { 1 2 } ^ { 2 } + m _ { 3 } ^ { 2 } r _ { 1 3 } ^ { 2 } + 2 m _ { 2 } m _ { 3 } \hat { r } _ { 1 2 } \hat { r } _ { 1 3 } \cos { \theta _ { 2 3 } } ) . } \end{array}
$$

Here023 is the angle between $\{ \pmb { \tau } _ { 1 } - \pmb { \tau } _ { 2 } \}$ and $\{ { \tt r } _ { 1 } - { \tt r } _ { 3 } \}$ ; since this angle is constant we deduce

$$
{ \mathfrak { r } } _ { \mathtt { i } } = { \mathfrak { F } } _ { \mathtt { i } } \lambda \{ { \mathfrak { t } } \} ,
$$

# and,generally,

$$
{ r } _ { i } = { \tilde { r } } _ { i } \lambda ( t ) .
$$

It follows that the shape of a triangle formed by the origin and any two masses is constant, and therefore that the angle subtended at the origin by the line joining any two masses is.constant. Then if $\dot { \theta } _ { i }$ is the angular velocity of $\gamma _ { 3 } \lambda _ { i }$ about the origin, we must have

But the total angular momentum of the system about the origin is constant and eaual to

$$
( m _ { 1 } { \hat { r } } _ { 1 } ^ { 2 } + m _ { 2 } { \hat { r } } _ { 2 } ^ { 2 } + m _ { 3 } { \hat { r } } _ { 3 } ^ { 2 } ) \lambda ^ { 2 } { \dot { \hat { \theta } } } .
$$

Hence the angular momentum of each individual mass about the origin is con-stant,so that the net force acting on that mass passes through the origin.

The equation of motion for $\mathfrak { T } \mathfrak { T } _ { \mathfrak { L } _ { \mathfrak { L } } } .$ can be written

$$
\begin{array} { l } { { m _ { i } F _ { i } = m _ { i } \big ( \ddot { r } _ { i } - r _ { i } \dot { \theta } _ { i } ^ { 2 } \big ) } } \\ { { = r _ { i } m _ { i } \left( \displaystyle \frac { \ddot { \lambda } } { \lambda } - \dot { \theta } ^ { 2 } \right) . } } \end{array}
$$

Hence we have the condition (8.6.7), which must, therefore,be necessary.

To show that the conditions are sufficient, we simply follow up their consequences. We have $\pmb { \tau } _ { 1 } \times \pmb { \Sigma } _ { 1 } = \pmb { \emptyset }$ ,or $\underline { { \boldsymbol { \mathfrak { r } } } } _ { \perp } \times \breve { \underline { { \boldsymbol { \tau } } } } _ { \perp } = \boldsymbol { \mathfrak { V } }$ Applying this condition to the frst equation of (8.6.1) we find

$$
{ \mathfrak { r } } _ { \mathrm { { 1 } } } \times \left\{ { \frac { { \mathfrak { m } } _ { 2 } { \mathfrak { L } } _ { 2 } } { r _ { 1 2 } ^ { 3 } } } + { \frac { { \mathfrak { M } } _ { 3 } { \mathfrak { r } } _ { 3 } } { r _ { 1 3 } ^ { 3 } } } \right\} = 0
$$

or,using (8.6.2),

$$
\pi _ { 2 } \mathtt { r } _ { \mathtt { f } } \times \mathtt { r } _ { 2 } \left\{ \frac { 1 } { r _ { \mathtt { f } 2 } ^ { 3 } } - \frac { \mathtt { j } } { r _ { \mathtt { l } 3 } ^ { 3 } } \right\} = \mathtt { 0 } ,
$$

with similar results for the other masses. For these equations to be satisfied, we must either have

$$
r _ { 2 3 } = r _ { 3 1 } = r _ { 1 2 } ,
$$

the case that we have already investigated, or

$$
{ \mathfrak { r } } _ { 2 } \times { \mathfrak { r } } _ { 3 } = { \mathfrak { r } } _ { 3 } \times { \mathfrak { r } } _ { 1 } = { \mathfrak { r } } _ { 1 } \times { \mathfrak { r } } _ { 2 } = \mathbb { 0 } ,
$$

so that the particles lie in a straight line; this satisfies our geometrical conditions. There are no other possibilities.

We might have suspected'the possibility of straight-line solutions by analogy with the restricted three-body problem; now we have to justify them for the motion of three finite bodies and find the number of possible solutions.Let the line be the $\pmb { \mathcal { X } }$ -axis,and let it rotate with angular velocity $\dot { \theta }$ We have $\mathfrak { x } _ { \mathrm { i } } = \mathring { \mathfrak { x } } _ { \mathrm { i } } \backslash \{ \mathfrak { k } \}$ The force acting on $m _ { 1 }$ is

$$
\begin{array} { r l } & { F _ { 1 } = - m _ { 2 } \frac { x _ { 1 } - x _ { 2 } } { x _ { 1 2 } ^ { 3 } } - m _ { 3 } \frac { x _ { 1 } - x _ { 2 } } { x _ { 1 3 } ^ { 3 } } } \\ & { \quad = - \frac { 1 } { \lambda ^ { 2 } } \left\{ m _ { 2 } \frac { \hat { x } _ { 1 } - \hat { x } _ { 2 } } { x _ { 1 2 } ^ { 3 } } - m _ { 3 } \frac { \hat { x } _ { 1 } - \hat { x } _ { 3 } } { x _ { 1 3 } ^ { 3 } } \right\} . } \end{array}
$$

Now $\lambda$ is proportional to the distance, so that $m _ { 1 }$ is effectively acted upon by a force directed toward the center of mass and obeying the inverse square law; it will move in $\hat { \mathbf { z } }$ conic orbit and so will the other two masses.

To show that this solution is possible, we must impose the condition

$$
{ \mathcal { F } } _ { 1 } : { \mathcal { E } } _ { 2 } : { \mathcal { F } } _ { 3 } = x _ { 1 } : x _ { 2 } : x _ { 3 } .
$$

Ifthisis true initially, it will always be true, so it is sufficient to prove that for the initial conditions,

$$
\begin{array} { r } { R x _ { 1 } = m _ { 2 } \frac { x _ { 1 } - x _ { 2 } } { x _ { 1 2 } ^ { 3 } } + m _ { 3 } \frac { x _ { 1 } - x _ { 3 } } { x _ { 1 3 } ^ { 3 } } , } \\ { R x _ { 2 } = m _ { 3 } \frac { x _ { 2 } - x _ { 3 } } { x _ { 2 3 } ^ { 3 } } + m _ { 1 } \frac { x _ { 2 } - x _ { 1 } } { x _ { 2 1 } ^ { 3 } } , } \\ { R x _ { 3 } = m _ { 1 } \frac { x _ { 3 } - x _ { 1 } } { x _ { 3 1 } ^ { 3 } } + m _ { 2 } \frac { x _ { 3 } - x _ { 2 } } { x _ { 3 2 } ^ { 3 } } . } \end{array}
$$

eR is a constant that depends on the initial conditions

Let us prescribe a scale such that the initial distance ${ \mathfrak { x } } _ { 1 } - { \mathfrak { x } } _ { 2 } = 1$ We need show that the third body can be given some value of $\pmb { x }$ such that the initial onditions are satisfied.Let

$$
z _ { 2 } - x _ { 3 } = X .
$$

We shall investigate whether there is an $\pmb { \mathcal { Z } } 3$ such that $x _ { 2 }$ lies between $\pmb { \mathcal { X } } _ { \mathfrak { I } }$ and $\$ 3$ ： in this case $\pmb { \chi }$ must be positive. Subtracting (8.6.9) from (8.6.8),and (8.6.10) from（8.6.9），we find

$$
\begin{array} { c } { { R = m _ { 1 } + m _ { 2 } - \displaystyle \frac { m _ { 3 } } { X ^ { 2 } } + \displaystyle \frac { m _ { 3 } } { ( 1 + X ) ^ { 2 } } , } } \\ { { { } } } \\ { { R X = \displaystyle \frac { m _ { 3 } } { X ^ { 2 } } - m _ { 1 } + \displaystyle \frac { m _ { 1 } } { ( 1 + X ) ^ { 2 } } + \displaystyle \frac { m _ { 2 } } { X ^ { 2 } } . } } \end{array}
$$

weeliminate $\pmb { \mathcal { R } }$ remove fractions, and arrange in powers of $X$ , we obtain the quintic

$$
\begin{array} { l } { { \ddot { \imath } _ { \pm } + m _ { 2 } ) X ^ { \bar { 0 } } + ( 3 m _ { 1 } + 2 m _ { 2 } ) X ^ { 4 } + ( 3 m _ { 1 } + m _ { 2 } ) X ^ { 3 } } } \\ { { \qquad - ( m _ { 2 } + 3 m _ { 3 } ) X ^ { 2 } - ( 2 m _ { 2 } + 3 m _ { 3 } ) X - ( m _ { 2 } + m _ { 3 } ) = 0 . } } \end{array}
$$

The coefficients of the powers of $\boldsymbol { \chi }$ change sign only once, so that by Descartes' rule of signs there is one positive root and one only. Hence there is one and only one position of $\mathfrak { M } _ { 3 }$ such that ${ \mathfrak { X } } _ { 1 } > { \mathfrak { X } } _ { 2 } > { \mathfrak { X } } _ { 3 }$ If we want $x _ { 3 }$ to lie between $x _  \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt \tt$ and 2equations (8.6.11) are slightly different, but we again finish with a quintic that has only one relevant root. The same applies if we want $x _ { 1 }$ to lie between 2 and xg. Accordingly, there are three possible straight-line configurations and three only; these correspond to those found for the restricted three-body problem

This completes the discussion of these solutions, called the Lagrangian solutions, to the three-body problem. The equilateral triangle solutions and the straight-line solutions are the only ones satisfying the geometrical conditions that there can only be rotation and change of scale. If there is no change of scale, the solutions are called stationary, and the positions of the bodies are called libration points. Thus the Trojan planets oscillate about libration points, and the gegenschein (if the suggested explanation is correct） is at a libration point,the other bodies being the Sun and Jupiter,and the Sun and the Earth, respectively.

# 8.7Problems

1.Amend the criterion for the recognition of comets to apply to parabolic orbits.Show that the perturbations by Jupiter on a parabolic comet moving in the plane of Jupiter's orbit cannot result in the orbit's remaining parabolic,and find the relation between $\pmb { a }$ and $e$ of the resulting orbit. Consider some particular cases.

2.Show that if a parabolic comet is perturbed by Jupiter into another parabolic orbit, the relation between the old and new inclinations is given by

$$
\cos i _ { 1 } = { \sqrt { 2 } } \cos i _ { 2 } .
$$

3.Show analytically that the double point in the restricted three-body problem,which lies between the two finite masses,is closer to the lighter of the masses,and also that it is closer to $\mathcal { J } ^ { k }$ than the double point lying on the far side.

4.Investigate the straight-line solution on the far side of the lighter mass when $\mu$ is small. Show that if $x = 1 - \mu + \beta .$ then $\boldsymbol { \beta }$ can be expanded in a power series in $\mu ^ { 1 / 3 }$ ,in which the first three terms are

$$
\rho = \left( \frac { \mu } { 3 } \right) ^ { 1 / 3 } \pm \frac { 1 } { 3 } \left( \frac { \mu } { 3 } \right) ^ { 2 / 3 } - \frac { 1 } { 9 } \left( \frac { \mu } { 3 } \right) ^ { 3 / 3 } .
$$

5. Find series, corresponding to that in problem 4,for the other straight-line solutions.

6.Assuming that the suggestion made in the text about the gegenschein is correct,verify that the position of the libration point is not such that the meteors will lie in the Earth's shadow.

7.Consider motion in the $x - y$ plane in the restricted three-body problem. Show that the equation of $\gtrdot$ limiting curve can be written

$$
( 1 - \mu ) \left( r _ { 1 } ^ { 2 } + \frac { 2 } { r _ { 1 } } \right) + \mu \left( r _ { 2 } ^ { 2 } + \frac { 2 } { r _ { 2 } } \right) = C + \mu ( 1 - \mu ) ,
$$

and hence show that the minimum value of $C$ is $3 - \mu ( \tilde { \lambda } - \mu )$

8.Show that, to the first order of small quantities,periodic orbits exist in the x-y plane about the straight-line points of libration in the restricted three-body problem.Also show that these are elipses with major axes parallel to the y-axis,and are such that the eccentricity is independent of the initial displacement,but depends only on the distribution of the   
masses.

9.If $\{ 1 - \mu \}$ and $\mathcal { Y }$ are the Sun and the Earth， respectively， prove that the period of oscillation parallel to the $z \cdot$ -axis for an infinitesimal body slightly displaced from the point of libration opposite the Sun is 183.304 mean solar days.

10.For the situation of problem 9,show that the period of small oscillations in the $\pmb { \mathscr { Z } }$ yplane is177.0 days.

Show that for small values of $\sharp$ the periods of oscillation both parallel to the $z$ axis and in the x-y plane are,in general, longest for the point opposite to $\mu$ with respect to $( 1 - \mu )$ as origin;next longest for the point opposite to $\{ \mathfrak { T } - \mu \}$ with respect to $\mu$ as origin;and shortest for the point between $( 1 - \mu )$ and $\sharp$

2.Three bodies move in accordance with a Lagrangian solution. Show that the orbit of any one about any other, taken as origin,isa conic. Suppose that the masses are equal and that they form an equilateral triangle at any time. Let $\mathcal { P }$ be the period in which they revolve around their center ofmass and $\pmb { \mathcal { \alpha } }$ bethe semi-majoraxis of the orbit ofany one body taken with respect to any other. Show that the radius of the circle in which a particle would revolve around one of the bodies in the time Pis a·3-1/3.

13.Show that the equilateral triangle circular solutions hold for the law of force $\mu _ { f } ^ { \smash { \scriptstyle \sharp \vec { r } } }$ .Investigate the general equilateral triangle solutions for this law,and also consider more complicated laws of central force.

14.Find the number of colinear solutions for the law of force $\mu _ { j } \int q ^ { - \pi } d t$

15.Investigate the colinear solutions when the law of force is $\mu / r ^ { 3 }$

6.Show that when the law of force varies inversely with the fifth power of the distance, one solution is that each of the bodies moves in a circle through their center of mass in such a way that the three bodies are always at the vertices of an equilateral triangle.

Show that if the three bodies are placed at rest in any one of the configurations admitting circular solutions,they will fall to the center of mass inthe same time in straight lines.

Find the distribution of mass among the three bodies for which the time offalling to their center of mass (see problem 17) will be (a) the least and (b) the greatest.

19.Solve completely the three-body problem when the law of force is proportional to the distance.

20.Investigate the possibility of a solution to the four-body problem when the masses are at the vertices of a regular tetrahedron.

21.Consider Jacobi's integral when applied approximately to the Sun,the Earth,and the (massless) Moon. Find the value of $C$ and investigate the size and shape of the Hill limiting surface for the motion of the Moon.

22.Consider small oscillations about the libration points for the Trojan planets.Show that of the two periods one is nearly the same as that of Jupiter, and the other is nearly 148 years. Considering the oscillation of longer period (usually known as the libration),show that the approximate ratio of the amplitudes along and perpendicular to the radius vector is $3 \sqrt { \mu } : \mathbb { I }$ ： or $1 : 1 8 . 7$

23. If we define

$$
\Phi ( x , y , z ) = \frac { 1 } { 2 } ( x ^ { 2 } + y ^ { 2 } ) + \frac { 1 - \mu } { r _ { 1 } } + \frac { \mu } { r _ { 2 } } + \frac { 1 } { 2 } \mu ( 1 - \mu ) ,
$$

show that Jacobi's integral can be written in the form

$$
\dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } = 2 \Phi - C .
$$

Show that $C$ takes the same value at $\pmb { \mathcal { L } } _ { 4 }$ and $\mathbb { Z } _ { 5 }$ ,independent of $\sharp$ ,and find this value. Show also that

$$
2 \Phi = \left( \operatorname { I } - \mu \right) \left( r _ { 1 } ^ { 2 } + { \frac { 2 } { r _ { 1 } } } \right) + \mu \left( r _ { 2 } ^ { 2 } + { \frac { 2 } { r _ { 2 } } } \right) .
$$

24. Write a program to find the values of $C$ corresponding to $\xi _ { 3 } , \bar { \xi } _ { 2 }$ ,and $\mathbb { Z } _ { 3 }$ for any given value of $\ddagger ^ { \ddagger }$

25.A spacecraft is in a circular orbit around the Earth,with altitude 100 km.It is to be given an additional tangential velocity,and the consequent orbit is to take it to the Moon.Find the minimum velocity forwhich this might be possible on the basis of Jacobi's integral. (Assume the orbit of the Moon to be circular. You need to find the energy corresponding to $I _ { I }$ ）

26.For $\mu < 0 . 0 3 8 5 .$ ..there are oscillations around $\pmb { \mathcal { Z } } _ { 4 }$ ,according to the linear theory,with two different frequencies, say $\omega _ { \updownarrow }$ and $\omega _ { 2 }$ Find the values of $\mu$ for which $\omega _ { 1 } = 2 \omega _ { 2 } , a \ i \mathcal { A } \ i = 3 \omega _ { 2 }$ For these values of $\mathcal { Y }$ it has beenproved by non-linearanalysis that $I _ { 4 }$ and $\mathbb { L } _ { 5 }$ areunstable.
