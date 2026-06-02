the solution is

$$
x = e ^ { - \epsilon t } \Bigl ( \cos { \omega t } + \frac { \epsilon } { \omega } \sin { \omega t } \Bigr ) ,
$$

with $\omega : = \sqrt { 1 - \epsilon ^ { 2 } }$ . The solution reveals features that occur over widely separated time scales: there are rapid oscillations over a time scale of order unity, and a slow damping of the envelope over a time scale of order $\epsilon ^ { - 1 } \gg 1 .$ We would like to capture these features with a perturbative analysis of the differential equation.

A straightforward expansion of the solution in powers of $\epsilon$ would fail in this endeavor. Suppose that we write $x = x _ { 0 } ( t ) + \epsilon x _ { 1 } ( t ) + O ( \epsilon ^ { 2 } ) ,$ , insert this within the differential equation, and equate terms of like powers of $\epsilon$ to zero. We would obtain the differential equations $\ddot { x } _ { 0 } + x _ { 0 } = 0 \mathsf { a n d } \ddot { x } _ { 1 } + x _ { 1 } = - 2 \dot { x } _ { 0 } ,$ and these can be integrated in turn for $x _ { 0 } ( t )$ and $x _ { 1 } ( t )$ . Keeping the boundary conditions in mind, we get $x _ { 0 } = \cos t $ and observe that the driving force for $x _ { 1 }$ , equal to $2 \sin t$ , oscillates at the same frequency as the oscillator’s own natural frequency. This creates a resonant behavior that leads to unbounded growth, as can be seen in the solution $x _ { 1 } = \sin t - t \cos t .$ . The end result of this standard perturbative analysis is an approximate solution

$$
x = ( 1 - \epsilon t ) \cos t + \epsilon \sin t + O ( \epsilon ^ { 2 } )
$$

that becomes wholly inaccurate over times $t \simeq \epsilon ^ { - 1 }$ . This approximation, in particular, does not capture the damping that occurs over the long time scale.

In a multi-scale treatment of this problem one introduces a slow-time variable $\widetilde t : = \epsilon t$ in addition to the fast time $t$ , and postulates a solution of the form $x = x _ { 0 } ( \tilde { t } , t ) + \epsilon x _ { 1 } ( \tilde { t } , t ) + O ( \epsilon ^ { 2 } ) .$ , in which $x _ { 0 }$ and $x _ { 1 }$ are assumed to be bounded functions. The original differential equation is generalized in such a way that $\tilde { t }$ and $t$ are treated as independent variables, and the total time derivative is interpreted as

$$
\frac { d } { d t } = \frac { \partial } { \partial t } + \epsilon \frac { \partial } { \partial \tilde { t } } .
$$

In our case we have that $\dot { x } = \partial x _ { 0 } / \partial t + \epsilon \partial x _ { 0 } / \partial \tilde { t } + \epsilon \partial x _ { 1 } / \partial t + O ( \epsilon ^ { 2 } )$ and $\ddot { x } = \partial ^ { 2 } x _ { 0 } / \partial t ^ { 2 } +$ $2 \epsilon \partial ^ { 2 } x _ { 0 } / \partial \tilde { t } \partial t + \epsilon \partial ^ { 2 } x _ { 1 } / \partial t ^ { 2 } + O ( \epsilon ^ { 2 } )$ , and the differential equation becomes the set of equations

$$
\begin{array} { r l r } & { \frac { \partial ^ { 2 } x _ { 0 } } { \partial t ^ { 2 } } + x _ { 0 } = 0 , } & \\ & { \frac { \partial ^ { 2 } x _ { 1 } } { \partial t ^ { 2 } } + x _ { 1 } = - 2 \bigg ( \frac { \partial x _ { 0 } } { \partial t } + \frac { \partial ^ { 2 } x _ { 0 } } { \partial \tilde { t } \partial t } \bigg ) . } & \end{array}
$$

The solution to the first equation is $x _ { 0 } = A ( \tilde { t } ) \cos t$ , in which the function $A ( \tilde { t } )$ plays the role of constant of integration; this function cannot be determined until we proceed to the next order. We observe that a second solution to the differential equation, $B ( \tilde { t } ) \sin t$ , should in principle be added to the first; it will, however, eventually be rejected by the boundary conditions.

At the next order we find that the driving force for $x _ { 1 }$ is now equal to $2 ( A + A ^ { \prime } ) \sin t .$ , in which a prime indicates differentiation with respect to $\tilde { t }$ . We recognize that such a resonant force would produce a growth in $t$ , and that this would violate our assumption that $x _ { 1 }$ should stay bounded. We eliminate this eventuality by demanding that $A ( \tilde { t } )$ be a solution to $A + A ^ { \prime } = 0$ , which implies that $A = A _ { 0 } \exp ( - \tilde { t } )$ . Keeping the boundary conditions in mind, we find that the zeroth-order solution to the differential equation is

$$
x = \exp ( - \tilde { t } ) \cos t + O ( \epsilon ) .
$$

As we can see, this captures the essential aspects of the exact solution, including the damping that occurs over the long time scale.

The zeroth-order solution can be refined by integrating what has become of the first-order differential equation. We now have $\partial ^ { 2 } x _ { 1 } / \partial t ^ { 2 } + x _ { 1 } = 0$ , whose solution is $x _ { 1 } = C ( \tilde { t } ) \sin t$ (up to the addition of a second solution, which we discard by virtue of the boundary conditions). Once more we find that the unknown function $C ( \tilde { t } )$ cannot be determined until we proceed to the next order. It would, however, be determined in the same way, by ensuring that the driving force for $x _ { 2 }$ is free of a resonant term. Such an analysis would reveal that $C = \exp ( - \tilde { t } )$ , and the first-order solution to the differential equation is

$$
x = \exp ( - \tilde { t } ) \big ( \cos t + \epsilon \sin t \big ) + O ( \epsilon ^ { 2 } ) .
$$

This captures even more of the exact solution, but the central message of this exercise is that $x _ { 0 }$ by itself does a very fine job of reproducing the essential behavior of the exact solution.

# General theory of multi-scale orbital evolution

We now perform a multi-scale analysis of the evolution equations for the orbital elements $p$ , $e$ , and $\omega$ . Before we return to the specific situation that concerns us in this section (orbital evolution under radiation reaction), we develop a fairly general formulation that can be applied to many different situations. This formulation was devised by our friend Adam Pound in his PhD dissertation (2010). Similar (but less general) formulations can be found in a 1990 article by Lincoln and Will, and a 2004 paper by Mora and Will.

We collect the orbital elements into the vector $\mu ^ { a }$ , and express their evolution equations as

$$
\frac { d \mu ^ { a } } { d f } = \epsilon F ^ { a } ( f , \mu ^ { b } ) ,
$$

in which $\epsilon$ is a small parameter, and each driving force $F ^ { a }$ is assumed to be periodic in $f$ , so that $F ^ { a } ( f + 2 \pi , \mu ^ { b } ) = F ^ { a } ( f , \mu ^ { b } )$ . These equations are supplemented with

$$
\frac { d t } { d f } = T _ { 0 } ( f , \mu ^ { a } ) + \epsilon T _ { 1 } ( f , \mu ^ { a } ) ,
$$

which governs the behavior of the time function; $T _ { 0 }$ and $T _ { 1 }$ are also assumed to be periodic in $f$ . The exact specifications of $F ^ { a }$ , $T _ { 0 }$ , and $T _ { 1 }$ for our particular problem can be obtained from Eqs. (12.223) and (12.224), but our considerations here are more general.

In a multi-scale analysis of these differential equations we postulate the existence of solutions of the form

$$
\mu ^ { a } = \mu _ { 0 } ^ { a } ( \tilde { f } , f ) + \epsilon \mu _ { 1 } ^ { a } ( \tilde { f } , f ) + \epsilon ^ { 2 } \mu _ { 2 } ^ { a } ( \tilde { f } , f ) + O ( \epsilon ^ { 3 } )
$$

and

$$
t = \epsilon ^ { - 1 } t _ { - 1 } ( \tilde { f } , f ) + t _ { 0 } ( \tilde { f } , f ) + \epsilon t _ { 1 } ( \tilde { f } , f ) + O ( \epsilon ^ { 2 } ) ,
$$

in which $\tilde { f } : = \epsilon f$ is the slow variable. Each function $ { \mu } _ { n } ^ { a }$ and $t _ { n }$ is assumed to be periodic in $f$ . The presence of $\epsilon ^ { - 1 } t _ { - 1 }$ in $t$ is required because the time variable grows secularly even in the absence of a perturbation; when $\tilde { f }$ is of order unity and $f$ of order $\epsilon ^ { - 1 }$ , $t$ also is of order $\epsilon ^ { - 1 }$ .

To proceed with Eqs. (12.228) we treat $\tilde { f }$ and $f$ as independent variables and interpret a total derivative with respect to $f$ as

$$
\frac { d } { d f } = \frac { \partial } { \partial f } + \epsilon \frac { \partial } { \partial \tilde { f } } .
$$

Inserting Eq. (12.230) within the differential equations and equating like powers of $\epsilon$ , we obtain

$$
\begin{array} { c } { { \displaystyle \frac { \partial \mu _ { 0 } ^ { a } } { \partial f } = 0 , } } \\ { { \displaystyle \frac { \partial \mu _ { 0 } ^ { a } } { \partial \tilde { f } } + \frac { \partial \mu _ { 1 } ^ { a } } { \partial f } = F ^ { a } ( f , \mu _ { 0 } ^ { b } ) , } } \\ { { \displaystyle \frac { \partial \mu _ { 1 } ^ { a } } { \partial \tilde { f } } + \frac { \partial \mu _ { 2 } ^ { a } } { \partial f } = \mu _ { 1 } ^ { c } \partial _ { c } F ^ { a } ( f , \mu _ { 0 } ^ { b } ) ; } } \end{array}
$$

in the last equation the driving force $F ^ { a }$ is differentiated with respect to $\mu ^ { c }$ , and the repeated index indicates a summation over all orbital elements.

The equations of the system (12.233) can be integrated in turn. Equation (12.233a) implies that $\mu _ { 0 } ^ { a }$ is a function of the slow variable $\tilde { f }$ only. To integrate Eq. (12.233b) we first average the equation over a complete cycle of the fast variable. We use the notation

$$
\langle q \rangle ( \tilde { f } ) : = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } q ( \tilde { f } , f ) d f
$$

to indicate such an average; since $\tilde { f }$ and $f$ are independent variables the integral is evaluated while keeping $\tilde { f }$ fixed. Because the first term of Eq. (12.233b) is independent of $f$ , its average returns $d \mu _ { 0 } ^ { a } / d \tilde { f }$ . The average of the second term vanishes, because of the assumed periodicity of $\mu _ { 1 } ^ { a }$ . We are left with

$$
\frac { d \mu _ { 0 } ^ { a } } { d \tilde { f } } = \langle F ^ { a } \rangle ( \mu _ { 0 } ^ { b } ) ,
$$

a system of equations that determine $\mu _ { 0 } ^ { a } ( \tilde { f } )$ . Subtracting this from Eq. (12.233b), we next obtain $\partial \mu _ { 1 } ^ { a } / \partial f = F ^ { a } - \langle F ^ { a } \rangle$ , which integrates to

$$
\mu _ { 1 } ^ { a } = \mu _ { 1 , \mathrm { o s c } } ^ { a } ( \tilde { f } , f ) + \mu _ { 1 , \mathrm { s e c } } ^ { a } ( \tilde { f } ) ,
$$

where

$$
\mu _ { 1 , \mathrm { o s c } } ^ { a } = \int \left[ F ^ { a } ( f , \mu _ { 0 } ^ { b } ) - \langle F ^ { a } \rangle ( \mu _ { 0 } ^ { b } ) \right] d f
$$

is a periodic function of $f$ , and $\mu _ { 1 , \mathrm { s e c } } ^ { a }$ acts as a constant of integration. This is determined at the next order, by averaging Eq. (12.233c). The first term gives rise to $d \mu _ { 1 , \mathrm { s e c } } ^ { a } / d \widetilde { f }$ , the second term contributes nothing, and we arrive at

$$
\frac { d \mu _ { 1 , \mathrm { s e c } } ^ { a } } { d \tilde { f } } = \langle \mu _ { 1 , \mathrm { o s c } } ^ { c } \partial _ { c } F ^ { a } ( f , \mu _ { 0 } ^ { b } ) \rangle .
$$

We note that only $\mu _ { 1 , \mathrm { o s c } } ^ { c }$ appears on the right-hand side, instead of the complete expression $\mu _ { 1 } ^ { c }$ , because the average of the term involving $\mu _ { 1 , \mathrm { s e c } } ^ { a }$ vanishes. At this stage we have all the ingredients required in the construction of $\mu ^ { a }$ to first order in $\epsilon$ ; to obtain the terms of order $\epsilon ^ { 2 }$ in Eq. (12.230) we would proceed to the next order.

We follow the same recipe to integrate Eq. (12.229). Skipping over the details, we find that $t _ { - 1 }$ is a function of $\tilde { f }$ only determined by

$$
\frac { d t _ { - 1 } } { d \tilde { f } } = \langle T _ { 0 } \rangle ( \mu _ { 0 } ^ { a } ) ,
$$

and that $t _ { 0 }$ can be expressed as

$$
t _ { 0 } = t _ { 0 , \mathrm { o s c } } ( \tilde { f } , f ) + t _ { 0 , \mathrm { s e c } } ( \tilde { f } )
$$

with

$$
t _ { 0 , \mathrm { o s c } } = \int \left[ T _ { 0 } ( f , \mu _ { 0 } ^ { a } ) - \langle T _ { 0 } \rangle ( \mu _ { 0 } ^ { a } ) \right] d f
$$

and

$$
\frac { d t _ { 0 , \mathrm { s e c } } } { d \tilde { f } } = \big < \mu _ { 1 , \mathrm { o s c } } ^ { b } \partial _ { b } T _ { 0 } ( f , \mu _ { 0 } ^ { a } ) + T _ { 1 } ( f , \mu _ { 0 } ^ { a } ) \big > .
$$

These equations allow us to construct $t$ to zeroth order in $\epsilon$ ; to obtain the terms of order $\epsilon$ in Eq. (12.231) we would proceed to the next order.

The most important pieces of the orbital elements $\mu ^ { a }$ are those that grow secularly and depend on the slow variable $\tilde { f }$ . These are contained in $\mu _ { 0 } ^ { a }$ and $\mu _ { 1 , \mathrm { s e c } } ^ { a }$ , and a useful secular approximation to the orbital elements is given by

$$
\mu _ { \mathrm { s e c } } ^ { a } = \mu _ { 0 } ( \tilde { f } ) + \epsilon \mu _ { 1 , \mathrm { s e c } } ^ { a } ( \tilde { f } ) + O ( \epsilon ^ { 2 } ) ;
$$

this ignores the unimportant periodic oscillations contained in $\mu _ { 1 , \mathrm { o s c } } ^ { a }$ , which average out after each orbital cycle. Similarly, a useful secular approximation to the time function is given by

$$
t _ { \mathrm { s e c } } = \epsilon ^ { - 1 } t _ { - 1 } ( \tilde { f } ) + t _ { 0 , \mathrm { s e c } } ( \tilde { f } ) + O ( \epsilon ) .
$$

It is important to understand that while the oscillatory terms $\mu _ { 1 , \mathrm { o s c } } ^ { a }$ do not appear in these equations, they are nevertheless required in the construction of the secular terms $\mu _ { 1 , \mathrm { s e c } } ^ { a }$ and $t _ { 0 , \mathrm { s e c } }$ . This can be seen from Eqs. (12.238) and (12.242), which reveal that oscillations in $\mu _ { 1 } ^ { a }$ can combine with oscillations in $\partial _ { c } F ^ { a } ( f , \mu _ { 0 } ^ { b } )$ and $\partial _ { b } T _ { 0 } ( f , \mu _ { 0 } ^ { a } )$ to produce secular terms.

# Radiation reaction

We now have all the required tools at our disposal, and we may return to the original problem, the determination of the orbital evolution under radiation reaction. The orbital elements are $\mu ^ { a } : = ( { \mathsf { p } } , e , \omega )$ , and the driving forces $F ^ { a }$ can be extracted from Eq. (12.227). Their averages are easily computed, and Eq. (12.235) returns

$$
\begin{array} { r l } & { \cfrac { d \mathsf { p } _ { 0 } } { d \tilde { f } } = - 8 \mathsf { p } _ { 0 } ^ { - 3 / 2 } \bigg ( 1 + \frac { 7 } { 8 } e _ { 0 } ^ { 2 } \bigg ) , } \\ & { \cfrac { d e _ { 0 } } { d \tilde { f } } = - \cfrac { 3 8 } { 3 } e _ { 0 } \mathsf { p } _ { 0 } ^ { - 5 / 2 } \bigg ( 1 + \frac { 1 2 1 } { 3 0 4 } e _ { 0 } ^ { 2 } \bigg ) , } \\ & { \cfrac { d \omega _ { 0 } } { d \tilde { f } } = 0 , } \end{array}
$$

where $\mu _ { 0 } ^ { a } : = ( { \mathsf p } _ { 0 } , e _ { 0 } , \omega _ { 0 } )$ are the zeroth-order approximations to the orbital elements. From Eq. (12.227) and (12.237) we also obtain the oscillatory first-order corrections,

$$
\begin{array} { l } { { \displaystyle { \mathsf { p } } _ { 1 , \mathrm { o s c } } = - \frac { 1 } { { \mathsf { p } } _ { 0 } ^ { 3 / 2 } } \biggl ( k _ { 1 } ^ { p } \sin f + \frac 1 2 k _ { 2 } ^ { p } \sin 2 f + \frac 1 3 k _ { 3 } ^ { p } \sin 3 f \biggr ) , \qquad ( 1 2 . 2 \hdots ) , } } \\  { \displaystyle { e _ { 1 , \mathrm { o s c } } = - \frac { 1 } { { \mathsf { p } } _ { 0 } ^ { 5 / 2 } } \biggl ( k _ { 1 } ^ { e } \sin f + \frac 1 2 k _ { 2 } ^ { e } \sin 2 f + \frac 1 3 k _ { 3 } ^ { e } \sin 3 f + \frac 1 4 k _ { 4 } ^ { e } \sin 4 f + \frac 1 5 k _ { 5 } ^ { e } \sin 5 f \biggr ) , } } \end{array}
$$

$$
\omega _ { 1 , \mathrm { o s c } } = \frac { 1 } { e _ { 0 } \mathsf { p } _ { 0 } ^ { 5 / 2 } } \bigg ( k _ { 1 } ^ { \omega } \cos f + \frac { 1 } { 2 } k _ { 2 } ^ { \omega } \cos 2 f + \frac { 1 } { 3 } k _ { 3 } ^ { \omega } \cos 3 f + \frac { 1 } { 4 } k _ { 4 } ^ { \omega } \cos 4 f + \frac { 1 } { 5 } k _ { 5 } ^ { \omega } \cos 5 f \bigg ) .
$$

These are combined with derivatives of the driving forces to compute the right-hand side of Eq. (12.238). We obtain

$$
\frac { d \mathsf { p } _ { 1 , \mathrm { s e c } } } { d \tilde { f } } = \frac { d e _ { 1 , \mathrm { s e c } } } { d \tilde { f } } = 0 ,
$$

and conclude that there is no secular growth in $\mathsf { p }$ and $e$ at first order in $\epsilon$ . The calculation reveals also that $d \omega _ { 1 , \mathrm { s e c } } / d \tilde { f } \neq 0$ , but we shall not be concerned with this small amount of secular growth in $\omega$ .

Proceeding with the time function, we insert Eq. (12.226) within Eq. (12.239) and get

$$
\frac { d \mathfrak { t } _ { - 1 } } { d \tilde { f } } = \biggl ( \frac { \mathfrak { p } _ { 0 } } { 1 - e _ { 0 } ^ { 2 } } \biggr ) ^ { 3 / 2 } .
$$

From Eq. (12.242) we next obtain

$$
\frac { d \ t _ { 0 , \mathrm { s e c } } } { d \tilde { f } } = 0 ,
$$

and observe the absence of secular growth at zeroth order in $\epsilon$ .

# Conclusion

The multi-scale analysis of the orbital evolution equations is now completed. We have found that the secular changes in the orbital elements are governed by the system of differential equations

$$
\begin{array} { l } { { \displaystyle \left. \frac { d \Theta } { d f } \right| _ { \mathrm { s e c } } = - \epsilon \frac { 8 } { 9 ^ { 3 / 2 } } \bigg ( 1 + \frac { 7 } { 8 } e ^ { 2 } \bigg ) + { \cal O } ( \epsilon ^ { 3 } ) } , }  \\ { { \displaystyle \left. \frac { d e } { d f } \right| _ { \mathrm { s e c } } = - \epsilon \frac { 3 8 e } { 3 9 ^ { 5 / 2 } } \bigg ( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \bigg ) + { \cal O } ( \epsilon ^ { 3 } ) } , }  \\ { { \displaystyle \left. \frac { d \ t } { d f } \right| _ { \mathrm { s e c } } = \bigg ( \frac { \mit \mathrm { p } } { 1 - e ^ { 2 } } \bigg ) ^ { 3 / 2 } + { \cal O } ( \epsilon ^ { 2 } ) } , }  \end{array}
$$

in which we have removed the now-redundant suffixes on $\mathsf { p } , e$ , and t.

To display the equations in their final form we re-introduce the scales $p ^ { * }$ and $t ^ { * }$ , substitute $\epsilon$ from Eq. (12.225), and eliminate $f$ . This yields

$$
\begin{array} { l } { \displaystyle \frac { d p } { d t } \bigg \vert _ { \mathrm { s e c } } = - \frac { 6 4 } { 5 } \eta c \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 7 } { 8 } e ^ { 2 } \bigg ) , } \\ { \displaystyle \frac { d e } { d t } \bigg \vert _ { \mathrm { s e c } } = - \frac { 3 0 4 } { 1 5 } \eta c \frac { e } { p } \bigg ( \frac { G M } { c ^ { 2 } p } \bigg ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \bigg ) . } \end{array}
$$

These are the same equations that were obtained in Sec. 12.3.3 on the basis of averaged statements of energy and angular-momentum balance – refer to Eqs. (12.86) and (12.87). The treatment given here, based on a multi-scale analysis of the evolution equations, is much more satisfactory than the earlier work: We were able to prove that Eqs. (12.251) do indeed capture the secular behavior of the orbital elements, and that the fractional error incurred is of order $\epsilon ^ { 2 }$ .

In Figs. 12.3 and 12.4 we compare the approximate evolution obtained on the basis of Eqs. (12.250) to an exact numerical integration of Eqs. (12.226). We can see that the agreement is excellent.

# 12.10 Bibliographical notes

Radiation-reaction effects in electromagnetism are discussed in many textbooks, including Jackson’s Classical Electrodynamics (1998). The treatment is usually restricted to point charges, and much space is devoted to the curious fact that the radiation-reaction force depends on the rate of change of the particle’s acceleration. The literature has debated this issue endlessly, and many misconceptions have taken hold — don’t get us started. For a well-balanced overview, refer to Gralla, Harte, and Wald (2009).

The shortwave approximation of Sec. 12.2 was first formulated by Isaacson (1968a and 1968b). The angular-momentum flux of gravitational waves was first calculated by Bryce DeWitt in the early nineteen seventies, and his results were eventually published in DeWitt (2011); the final expression also appeared in Thorne (1980). An alternative approach to the description of radiative losses in general relativity, widely considered to be more rigorous and convincing than the Landau–Lifshitz approach adopted here, was formulated by Bondi and his colleagues. Representative papers are Sachs (1961 and 1962) and Bondi, van der

![](images/14dcd9704fc7df5b27f4a158586539d88d472d1e4d479797655a2e09908fc500.jpg)  
Evolution of the dimensionless semi-latus rectum p under radiation reaction. The evolution begins with $\mathsf { p } = 2 0$ and $e = 0 . 7$ , and it proceeds for 100 orbital cycles with $\epsilon = 0 . 1$ . Time is expressed in units of the initial orbital period $P .$ The exact curve (solid) displays oscillations around the mean curve (dashed), and it was obtained by numerical integration of Eqs. (12.226). These computations were carried out in the Burke–Thorne gauge, with $a = b = 0$ . The mean curve is obtained on the basis of the secular approximation of Eqs. (12.250).

![](images/bb38898e06d838d65a7ea8b6d1fc8fd6d2508a8b2ac6149436a5993d69d6abde.jpg)  
Fig. 12.4 Evolution of the eccentricity e under radiation reaction. The details are as in Fig. 12.3.

Burg, and Metzner (1962). Though different, the Bondi and Landau–Lifshitz approaches yield identical results.

Radiative losses of slowly-moving systems (Sec. 12.3), including binary stars, were first explored by Peters and Mathews (1963), Peters (1964), Bekenstein (1973), and Fitchett (1983). Wiseman’s beaming argument, presented in Box 12.2, was published in Wiseman (1992).

The first binary pulsar (Sec. 12.4) was discovered by Hulse and Taylor in 1974; their discovery paper was published as Hulse and Taylor (1975). The first measurement of the orbital damping caused by radiative losses was reported in Taylor, Fowler, and McCulloch (1979). The numbers for PSR $1 9 1 3 + 1 6$ displayed in Table 12.1 and the following discussion are taken from Weisberg, Nice, and Taylor (2010). The numbers for the double pulsar J0737- 3039 are taken from Kramer et al. (2006). Calculations to high post-Newtonian order of radiative losses for inspiralling compact binaries are reviewed in Blanchet (2006). The papers alluded to at the beginning of Sec. 12.4.3 are Favata, Hughes, and Holz (2004), Baker et al. (2006), and Gonzalez et al. (2007). A recent review of numerical simulations of black-hole superkicks is provided by Zlochower, Campanelli, and Lousto (2011).

The approach adopted in Secs. 12.5–12.7 to calculate radiation-reaction potentials and forces is patterned after Pati and Will (2000 and 2001). The Burke–Thorne gauge featured in Sec. 12.8 was formulated in Thorne (1969), Burke (1971), and Misner, Thorne, and Wheeler (1973); see, however, the criticisms expressed by Walker and Will (1980). The Schafer gauge was formulated in Sch ¨ afer (1983), and the Damour–Deruelle gauge refers ¨ to Damour and Deruelle (1981).

The multi-scale analysis of the orbital evolution of a binary system under radiation reaction, presented in Sec. 12.9, is patterned after Lincoln and Will (1990) and Mora and Will (2004). The general method is introduced in the excellent text by Bender and Orzag (1978), and the application to osculating orbital elements was developed in Pound (2010).

# 12.11 Exercises

12.1 Verify Eq. (12.40).

12.2 Use Eqs. (12.68) and (12.69) to show that the fluxes of energy, linear momentum, and angular momentum from a Newtonian binary system can be expressed in the form

$$
\begin{array} { l } { { \Phi = { \displaystyle { \frac { 8 } { 1 5 } } } \eta ^ { 2 } { \displaystyle { \frac { c ^ { 3 } } { G } } } \bigg ( { \displaystyle { \frac { G m } { c ^ { 2 } r } } } \bigg ) ^ { 4 } \left( 1 2 v ^ { 2 } - 1 1 { \dot { r } } ^ { 2 } \right) , } } \\ { { \Phi ^ { j } = - { \displaystyle { \frac { 8 } { 1 0 5 } } } \Delta \eta ^ { 2 } { \displaystyle { \frac { c } { G } } } \bigg ( { \displaystyle { \frac { G m } { c ^ { 2 } r } } } \bigg ) ^ { 4 } \bigg [ v ^ { j } \bigg ( 5 0 v ^ { 2 } - 3 8 { \dot { r } } ^ { 2 } + 8 { \displaystyle { \frac { G m } { r } } } \bigg ) - { \dot { r } } n ^ { j } \bigg ( 5 5 v ^ { 2 } - 4 5 { \dot { r } } ^ { 2 } + 1 2 { \displaystyle { \frac { G m } { r } } } \bigg ) \bigg ] } } \\ { { \Phi ^ { j } = { \displaystyle { \frac { 8 } { 5 } } } \eta ^ { 2 } { \displaystyle { \frac { c } { G } } } \bigg ( { \displaystyle { \frac { G m } { c ^ { 2 } r } } } \bigg ) ^ { 3 } h ^ { j } \bigg ( 2 v ^ { 2 } - 3 { \dot { r } } ^ { 2 } + 2 { \displaystyle { \frac { G m } { r } } } \bigg ) . } } \end{array}
$$

By incorporating a total time derivative into $P ^ { j } [ 5 ]$ and $J ^ { j } [ 5 ]$ , show that the momentum and angular-momentum fluxes can be written in the simpler forms

$$
\begin{array} { l } { { \displaystyle { \mathcal { F } } ^ { j } = - \frac { 4 } { 1 5 } \Delta \eta ^ { 2 } \frac { c } { G } \left( \frac { G m } { c ^ { 2 } r } \right) ^ { 4 } v ^ { j } \left( 1 3 v ^ { 2 } - 1 5 \dot { r } ^ { 2 } \right) , } } \\ { { \displaystyle { \mathcal { T } } ^ { j } = \frac { 8 } { 5 } \eta ^ { 2 } \frac { c } { G } \left( \frac { G m } { c ^ { 2 } r } \right) ^ { 3 } h ^ { j } \left( 4 v ^ { 2 } - 9 \dot { r } ^ { 2 } \right) , } } \end{array}
$$

and verify that the momentum flux is in the direction of motion of the lighter body.

12.3 Consider a Keplerian, circular orbit of radius $a$ in the $x - y$ plane. Show that when averaged over a complete orbit, the power emitted in gravitational waves per unit solid angle is given by

$$
\frac { d \mathcal { P } } { d \Omega } = \frac { 1 } { 2 \pi } \eta ^ { 2 } \frac { c ^ { 5 } } { G } \left( \frac { G m } { c ^ { 2 } a } \right) ^ { 5 } \left( 1 + 6 \cos ^ { 2 } \theta + \cos ^ { 4 } \theta \right) ,
$$

where $\theta$ is the angle between the $z$ -axis and $N$ , the direction of emission. Verify that the total power integrated over all solid angles agrees with Eq. (12.82a) when $e = 0$ .

12.4 Consider a Keplerian orbit that is circular apart from the slow decrease in radius $a$ caused by the energy lost to gravitational radiation. As a function of $\eta , m$ , and the initial radius $a _ { 0 }$ , calculate the lifetime of the binary system and the number of completed orbits before the radiation reaction brings the radius to zero. Give alternative expressions for the lifetime and number of orbits in terms of $\eta , m$ , and the initial orbital period $P$ . Using these results, carry out the following estimates:

(a) the remaining lifetime of the Hulse–Taylor binary pulsar PSR $1 9 1 3 + 1 6$ , with $M _ { 1 } \approx M _ { 2 } \approx 1 . 4 M _ { \odot }$ and $P = 7 . 7 5$ hours (assume that the orbit is circular);   
(b) the total time and number of cycles in the gravitational-wave signal from an inspiralling binary system of two $1 . 4 M _ { \odot }$ compact objects, from the time it enters the LIGO–Virgo frequency band with a gravitational-wave frequency of $1 0 \ : \mathrm { H z }$ to the end of the inspiral (when $a = 0$ );   
(c) the remaining lifetime of the Earth–Sun system.

12.5 The current eccentricity of the Hulse–Taylor binary pulsar orbit is $e _ { 0 } \approx 0 . 6$ , and its orbital period is 7.75 hours. Estimate the orbital eccentricity when gravitational waves from the system first enter the LIGO–Virgo band at $1 0 \ : \mathrm { H z }$ . You may treat the eccentricity as if it were much smaller than unity when making your estimate.

12.6 Consider a binary pulsar of equal masses, for which the only orbital variables measured initially are the orbital period $P$ and the pericenter advance $\dot { \omega }$ . Using the approximation of small eccentricity, show that the lifetime of the system is given by

$$
T = \frac { 5 } { 1 2 8 } \left( \frac { 6 \pi } { \dot { \omega } } \right) ^ { 5 / 2 } \left( \frac { 1 } { P } \right) ^ { 3 / 2 } .
$$

On the $\dot { \omega } \mathrm { - } P$ plane, plot the curve corresponding to $T = 1$ billion years. Plot the curve from approximately 0.1 to 30 degrees per year for $\dot { \omega }$ , and from approximately 1 to

30 hours for $P$ . How is the curve shifted when the initial orbit has a high eccentricity? How does the curve change if the masses are not equal?

12.7 For an inspiralling circular orbit of two bodies, show that the accumulated velocity of the center-of-mass as a result of radiative recoil is given by

$$
V _ { \mathrm { k i c k } } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \left( \frac { G m } { c ^ { 2 } a } \right) ^ { 4 } c \pmb { n } .
$$

Assume that the time scale for radiative losses is much longer than the orbital period, so that $d \Omega / d t \sim O ( c ^ { - 5 / 2 } ) \Omega ^ { 2 }$ . Find the mass ratio that maximizes the recoil velocity.

12.8 Consider a two-body system on a Newtonian hyperbolic orbit described by

$$
r = \frac { p } { 1 + e \cos \phi } , \qquad \frac { d \phi } { d t } = \sqrt { \frac { G m } { p ^ { 3 } } } ( 1 + e \cos \phi ) ^ { 2 } ,
$$

where $m$ is the total mass, and $p$ is the semi-latus rectum, related to the angular momentum per unit reduced mass $h$ by $h ^ { 2 } = G m p$ . The system’s energy is given by

$$
E = \eta \frac { G m ^ { 2 } } { 2 p } ( e ^ { 2 } - 1 ) .
$$

Note that $e > 1 , E > 0$ , and the orbit comes in from infinity at $\phi = - \operatorname { a r c c o s } ( - 1 / e )$ , reaching pericenter at $\phi = 0$ .

(a) Show that the total energy emitted in gravitational waves by the time the orbit reaches pericenter is given by

$$
\begin{array} { l } { { \Delta E = \displaystyle \frac { 3 2 } { 5 } \eta ^ { 2 } \frac { G m ^ { 2 } } { p } \left( \frac { G m } { c ^ { 2 } p } \right) ^ { 5 / 2 } f ( e ) , } } \\ { { f ( e ) = \left( 1 + \displaystyle \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } \right) \operatorname { a r c c o s } \left( - \displaystyle \frac { 1 } { e } \right) + \displaystyle \frac { 3 0 1 } { 1 4 4 } \left( 1 + \frac { 6 7 3 } { 6 0 2 } e ^ { 2 } \right) \sqrt { e ^ { 2 } - 1 } . } } \end{array}
$$

(b) In the limit where $e$ is close to unity, that is, when $e = 1 + \epsilon \mathrm { w i t h } \epsilon \ll 1$ , show that the energy loss will convert the hyperbolic orbit into a bound orbit before pericenter when the following inequality is satisfied:

$$
\frac { 8 5 \pi \eta } { 3 \epsilon } \left( \frac { G m } { c ^ { 2 } p } \right) ^ { 5 / 2 } > 1 .
$$

(c) Instead of the parameterization $( p , \epsilon )$ for the orbit, adopt $( b , v _ { \infty } )$ , in which $b$ is an impact parameter and $v _ { \infty }$ is the orbital velocity at infinite separation. These quantities are defined by $v _ { \infty } ^ { 2 } = ( G m / p ) ( e ^ { 2 } - 1 ) \simeq 2 ( G m / p ) \epsilon$ and $h = b v _ { \infty }$ . Express the criterion of part (b) as an inequality for $^ b$ .

(d) Show that the cross-section $\sigma _ { \mathrm { G W } } : = \pi b _ { \mathrm { c a p t u r e } } ^ { 2 }$ for gravitational-wave capture is given by

$$
\sigma _ { \mathrm { G W } } = \pi \left( \frac { 1 7 0 \pi } { 3 } \eta \right) ^ { 2 / 7 } \left( \frac { G m } { c ^ { 2 } } \right) ^ { 2 } \left( \frac { c } { v _ { \infty } } \right) ^ { 1 8 / 7 } .
$$

Such a process could play an important role in the evolution of dense star clusters.

12.9 Consider the radiation-reaction acceleration for a binary system. Given that it must be a $2 . 5 \mathrm { { P N } }$ correction of the Newtonian acceleration, that it must vanish in the testbody limit, and that it must be related to the mutual accelerations of the bodies, it is possible to show, without doing any work, that it must be of the general form

$$
a [ \mathrm { r r } ] = \frac { 8 \eta } { 5 c ^ { 3 } } \frac { G m } { r ^ { 2 } } \frac { G m } { c ^ { 2 } r } \bigg [ \bigg ( a _ { 1 } v ^ { 2 } + a _ { 2 } \frac { G m } { r } + a _ { 3 } \dot { r } ^ { 2 } \bigg ) \dot { r } n + \bigg ( b _ { 1 } v ^ { 2 } + b _ { 2 } \frac { G m } { r } + b _ { 3 } \dot { r } ^ { 2 } \bigg ) v \bigg ] ,
$$

where $m = M _ { 1 } + M _ { 2 }$ , $\eta = M _ { 1 } M _ { 2 } / m$ , and $a _ { n }$ and $b _ { n }$ are arbitrary parameters.

(a) Justify the form shown above.   
(b) Calculate the energy and angular momentum losses, $d E / d t$ and $d J / d t$ , implied by the proposed radiation-reaction acceleration.   
(c) Using Newtonian theory, prove the following useful identity:

$$
\frac { d } { d t } \left( \frac { v ^ { 2 s } { \dot { r } } ^ { p } } { r ^ { q } } \right) = \frac { v ^ { 2 s - 2 } { \dot { r } } ^ { p - 1 } } { r ^ { q + 1 } } \left[ p v ^ { 4 } - p v ^ { 2 } \frac { G m } { r } - ( p + q ) v ^ { 2 } { \dot { r } } ^ { 2 } - 2 s \frac { G m } { r } { \dot { r } } ^ { 2 } \right] ,
$$

where $p , q$ and $s$ are integers.

(d) By considering the three cases $( p , q , s ) = ( 1 , 2 , 1 ) , ( 3 , 2 , 0 )$ and (1, 3, 0), use the identity to show that the various numerical coefficients in the expressions for $d E / d t$ and $d J / d t$ can be altered by absorbing total time derivatives into $E [ 5 ]$ and $J [ 5 ]$ . Show that the freedom contained in these redefinitions is described by a three-parameter family.

(e) Assume now that $d E / d t$ and $d J / d t$ , as calculated previously, and including the three-parameter family of redefinitions, match the gravitational-wave fluxes of energy and angular momentum, given by

$$
\begin{array} { l } { { \displaystyle { \mathcal { P } = \frac { 8 } { 1 5 } \eta ^ { 2 } \frac { c ^ { 3 } } { G } \left( \frac { G m } { c ^ { 2 } r } \right) ^ { 4 } \left( 1 2 v ^ { 2 } - 1 1 \dot { r } ^ { 2 } \right) } ~ , } } \\ { { \displaystyle { \mathcal { T } ^ { j } = \frac { 8 } { 5 } \eta ^ { 2 } \frac { c } { G } \left( \frac { G m } { c ^ { 2 } r } \right) ^ { 3 } h ^ { j } \left( 2 v ^ { 2 } - 3 \dot { r } ^ { 2 } + 2 \frac { G m } { r } \right) } ~ , } } \end{array}
$$

where $\pmb { h } = \pmb { r } \times \pmb { v }$ . Obtain constraints on the coefficients $a _ { n }$ and $b _ { n }$ in $\pmb { a } [ \mathrm { \mathrm { r r } } ]$ . Show that $a _ { n }$ and $b _ { n }$ can be determined up to two unknown parameters. Show that this freedom corresponds precisely to the two-parameter gauge freedom described in Eq. (12.185), and that one can recover the Burke–Thorne, Schafer, ¨ and Damour–Deruelle expressions for the radiation-reaction acceleration. This approach to finding the radiation-reaction acceleration was taken by Iyer and Will (1995).

12.10 The radiative losses of energy and angular momentum cause the eccentricity of a binary system to decrease. This implies that in the past, the eccentricity must always have been larger. From Eqs. (12.251), which describe the secular evolution of the orbital elements, show that as $t \to - \infty$ , the eccentricity tends to unity and the semi-latus rectum $p$ tends to a constant $p _ { \infty }$ . Show that they evolve

according to

$$
1 - e = \frac { 8 5 } { 7 2 } \ln ( p _ { \infty } / p ) \big [ 1 + O ( 1 - e ) \big ] .
$$

Using Eq. (12.224), show that $f \to - \pi$ in the limit $t \to - \infty$ , and thus that the two bodies were at an infinite separation on a parabolic orbit. A rigorous analysis taking into account the periodic variations in the orbital elements reveals that a generic orbit in the infinite past is actually hyperbolic $( e > 1 )$ ), and that the parabolic orbit is a special case.

From Chapter 5 until now we have confined our attention to Einstein’s general theory of relativity. But general relativity is not the only possible relativistic theory of gravity. Even in the late 1800s, well before Einstein began his epochal work on special and general relativity, there were attempts to devise theories of gravity that went beyond Newtonian theory. Some attempts were modeled on Maxwell’s electrodynamics. Some replaced $\nabla ^ { 2 }$ with a wave operator in Poisson’s equation of Newtonian gravity, in an attempt to formulate a theory that was invariant under Lorentz transformations. None of these attempts was very successful; for example, most theories could not account for the anomalous perihelion advance of Mercury. In 1913, before Einstein completed the general theory of relativity, Nordstrom proposed a theory involving a curved spacetime; the metric was expressed as ¨ $g _ { \alpha \beta } = \Phi \eta _ { \alpha \beta }$ , with the scalar field $\Phi$ satisfying a Lorentz-invariant wave equation. But the theory automatically predicts a zero deflection of light, and ultimately it failed the test of experiment.

Alternative proposals appeared even after the publication of general relativity and the empirical successes with Mercury and the deflection of light. The eminent mathematician and philosopher Alfred North Whitehead formulated such an alternative theory in 1922. Troubled by the fact that in general relativity the causal relationships in spacetime are not known a priori, but only after the metric has been determined for a given distribution of matter, he devised a theory with a background Minkowski metric in order to put causality on a “firmer” ground. Initially, Whitehead’s theory was found to agree with the deflection of light and Mercury’s perihelion advance, and so for many years it was considered a viable, if not particularly attractive, alternative to general relativity. Indeed, it was not shown to be in serious violation of experimental results until 1971.

The continuing weakness of experimental confirmations of general relativity left plenty of openings for alternative proposals. Two influential papers from the early 1960s illustrate the situation: A 1962 review of experiments in gravitation by Bruno Bertotti, Dieter Brill, and Ronald Krotkov demonstrated just how thin was the evidence supporting general relativity, and a review by Gerald Whitrow and Georg Morduch (1965) listed scores of nominally viable alternative theories of gravity.

It was no coincidence that Bertotti, Brill, and Krotkov were working in Robert Dicke’s research group at Princeton University at the time, for Dicke was seriously interested in his own alternative theory of gravity, and he wanted to know exactly what the experimental constraints were. He had published the theory in 1961 with his student Carl Brans. Although it was based in part on earlier theories by Markus Fierz and Pascal Jordan, the theory nevertheless became known as the Brans–Dicke theory, and it had a major impact on the development of theoretical and experimental gravitational physics. It was the simplest modification of general relativity, retaining the concepts of curved spacetime and the Einstein equivalence principle, but modifying the way matter generates curvature by the added effect of a scalar field. As a mathematically consistent and well-motivated theory, it made calculable predictions for experiments, and those were only slightly different from the predictions of general relativity, in all cases within the experimental bounds that were known in the early 1960s. The Brans–Dicke theory played a primary role in a flowering of experimental gravity during the late 1960s and the 1970s. Ironically, this led to the demise of the theory, as experiments continued to support general relativity, and the constraints became too tight to leave much room for the alternative theory.

But recent years have witnessed a resurgence of alternative theories of gravity, or theories that go “beyond” Einstein. Some of this interest comes from the direction of elementary particle physics, especially the development of superstring theory, whose low-energy limit is not general relativity but a variant of Brans–Dicke theory, with a scalar field related to the dilaton and moduli fields that are central ingredients of string theory. Other alternative theories have emerged from attempts to formulate laws of physics in spacetimes of higher dimensionality. The observational evidence that as much as 25 percent of the universe is made up of dark matter has spawned alternative theories that attempt to account for the anomalous rotation curves of galaxies by modifying gravity instead of introducing a distribution of dark matter. The 1998 discovery that the expansion of the universe is accelerating has motivated the development of theories that modify general relativity on the largest scales, while leaving intact its predictions for solar-system and stellar-scale phenomena. Finally, the ongoing search for a quantum theory of gravity leaves open the possibility that the classical limit may be a theory radically different from general relativity.

The subject of alternative theories is too large and too active at the time of writing to do it justice in a single chapter. We merely touch on aspects of alternative theories and their experimental tests for which the post-Newtonian methods developed in this book are most useful. We begin in Sec. 13.1 with a general discussion of metric theories of gravity and their relation to the strong equivalence principle. In Sec. 13.2 we introduce a very general and powerful formalism, the parameterized post-Newtonian framework, to extract the experimental consequences of a broad class of alternative theories and subject them to empirical tests. We describe such tests in Sec. 13.3, and in Sec. 13.4 we explore the physics of gravitational waves in a broad class of alternative theories. Finally, in Sec. 13.5 we examine the predictions of a class of theories known as scalar–tensor gravity, in which the description of the gravitational field involves a scalar field in addition to the usual metric tensor; the Brans–Dicke theory is a particular member of this class of theories.

# 13.1 Metric theories and the strong equivalence principle

We wish to consider alternatives to general relativity, but we shall limit the scope of this generalization by insisting that each theory should satisfy the Einstein equivalence principle and be subjected to the metric-theory principles listed in Sec. 5.1. This defines the class of metric theories of gravitation, to which general relativity belongs.

The central aspect of the Einstein equivalence principle is that matter should couple in a universal manner to a single tensorial gravitational field, the metric $g _ { \alpha \beta }$ . There could be other gravitational fields present in spacetime, but these are prevented from interacting with the matter, and only serve to mediate the manner in which matter generates the metric. The additional fields could be scalars (as in the Brans–Dicke theory), vectors, tensors, or more exotic mathematical objects. They could be dynamical agents, governed by their own field equations, or they could be non-dynamical, fixed in some manner independently of the behavior of matter and fields (as for the Minkowski metric of Whitehead’s theory). Some theories have only the metric as the basic ingredient, as in general relativity, but propose alternative field equations. One class of such theories postulates a gravitational Lagrangian density that is a general function of the Ricci scalar, rather than the Ricci scalar itself; these are called “ $f ( R )$ theories,” devised to alter the behavior of gravity on cosmological scales. Another class of theories adds quadratic and higher-order curvature terms to the general relativistic Lagrangian density; this alters the behavior of the metric on short scales, and the higher-order terms are sometimes viewed as representing quantum corrections to classical general relativity.

Thinking about alternative theories of gravity from this broad but circumscribed point of view, we can draw some general conclusions about the nature of gravity in different metric theories. Consider a local reference frame, moving freely in a spacetime described by a given metric theory of gravity. Let this frame be sufficiently small that inhomogeneities in the external gravitational fields are suitably small throughout its volume. On the other hand, let the frame be sufficiently large that it can contain a system of gravitating matter and its associated gravitational fields; the system could be a star, a black hole, the solar system, or a Cavendish experiment set up to measure Newton’s constant $G$ . This is the kind of frame that was described at length back in Sec. 9.4; call it a “quasi-local Lorentz frame.”

To determine the behavior of the system we must calculate the metric generated by the material bodies and other fields. The computation proceeds in two stages. First, we determine the external behavior of the metric and other gravitational fields, thereby establishing boundary values that must be imposed upon the fields generated by the local system, at the boundary of the quasi-local frame far from the local system. Second, we solve for the fields generated by the local system. Because the metric is coupled directly or indirectly to the other fields of the theory, its structure and evolution inside the quasi-local frame are influenced by the boundary values taken on by these fields. This is true even when we work in a coordinate system in which the asymptotic form of $g _ { \alpha \beta }$ in the boundary region between the local system and the external world is that of the Minkowski metric, modulo tidal potentials from the external bodies. The gravitational environment in which the local system resides can therefore influence the metric generated by the local system via the boundary values of the auxiliary fields. Consequently, the results of local gravitational experiments may depend on the position and velocity of the quasi-local frame relative to the external environment. (A non-gravitational experiment is unaffected, because the gravitational fields it generates are negligible, and because the apparatus couples only to the metric, whose form can always be made locally Minkowskian at a given event in spacetime.) A local gravitational experiment might consist of a Cavendish-type experiment, a measurement of the acceleration of massive self-gravitating bodies, a study of the structure of stars and planets, or an analysis of the periods of planetary orbits.

We can now make a number of statements regarding different kinds of metric theories. First, a theory containing only the metric $g _ { \alpha \beta }$ and no other fields yields a local gravitational physics that is independent of the position and velocity of the local system. This follows from the fact that the only field coupling the local system to the environment is $g _ { \alpha \beta }$ , and it is always possible to find a coordinate system in which $g _ { \alpha \beta }$ takes the Minkowski form at the boundary between the local system and the external environment, modulo tidal potentials. The asymptotic values of $g _ { \alpha \beta }$ are therefore constants independent of position, and they are asymptotically Lorentz invariant, independent of the velocity of the quasi-local Lorentz frame. General relativity is an example of such a theory.

Second, a theory containing the metric $g _ { \alpha \beta }$ and a number of dynamical scalar fields $\phi _ { A }$ yields a local gravitational physics that may depend on the position of the frame but is independent of its velocity. This follows from the asymptotic Lorentz invariance of the Minkowski metric and the scalar fields, but now the asymptotic values of the scalar fields may depend on the position of the frame. An example is Brans–Dicke theory, in which the asymptotic scalar field determines the effective value of the gravitational constant, which therefore varies as $\phi$ varies. The scalar field can vary in time because of cosmological evolution, or it can vary in space because of the proximity of matter outside the quasi-local frame.

Third, a theory containing the metric $g _ { \alpha \beta }$ and additional dynamical or non-dynamical vector or tensor fields yields a local gravitational physics that may have both positionand velocity-dependent effects. For example, a timelike vector field $K ^ { \alpha }$ , whose value is determined by the distribution of matter in the universe, will have only a time component $K ^ { 0 }$ in a reference frame in which the large-scale distribution of matter is isotropic, presumably the rest-frame of the cosmic background radiation. But in a quasi-local Lorentz frame that is moving relative to this frame with a velocity $\pmb { v }$ , the asymptotic form of $K ^ { \alpha }$ will have spatial components $K ^ { j } \propto K ^ { 0 } v ^ { j }$ , and these velocity-dependent components can then feed into the local form of the metric.

These ideas can be framed in the context of the strong equivalence principle:

If a test body is placed at an initial event in spacetime and given an initial velocity there, and if the body subsequently moves freely, then its world line will be independent of its mass, internal structure, and composition, whether it is self-gravitating or not.

The outcome of any local non-gravitational or gravitational test experiment performed by a freely-moving apparatus is independent of the velocity of the apparatus and independent of when and where it is carried out.

Compare this with the statement of the Einstein equivalence principle provided in Sec. 5.1.1. The distinction between the strong and Einstein versions is the inclusion of bodies with selfgravitational interactions (planets, stars) and of experiments involving gravitational forces (Cavendish-type experiments, gravimeter measurements). Note that the strong principle is indeed stronger than the Einstein principle, and contains it in the limit in which local gravitational forces can be ignored. In fact, this principle is so strong that general relativity is one of the very few metric theories that actually satisfy it. Another example is Nordstrom’s¨ theory, which was described previously, and revealed not to be compatible with experimental tests.

Our previous discussion of the coupling of auxiliary fields to local gravitating systems suggests that alternative theories involving additional fields will tend to violate the strong equivalence principle, because the results of gravitational experiments are expected to depend on position and velocity. The discussion also suggests that when the strong equivalence principle is strictly respected, the description of gravity should involve a single universal field, the metric $g _ { \alpha \beta }$ . The argument is only a suggestion, however, and no rigorous proofs of these statements are available at present. Empirically it has been found that every metric theory that introduces auxiliary fields, either dynamical or non-dynamical, predicts violations of the strong equivalence principle at some level.

# 13.2 Parameterized post-Newtonian framework

# 13.2.1 A class of post-Newtonian theories

Metric theories of gravity demand that matter and non-gravitational fields respond only to the metric, and that they be completely oblivious to other fields that the theory might contain. The only gravitational field that can enter the matter’s equations of motion, derived from the conservation equation $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , is therefore the metric $g _ { \alpha \beta }$ ; the other fields are present only to help generate the metric. In this context the metric tensor and the equations of motion for matter become the primary entities for calculating observable effects, and all that distinguishes one metric theory from another is the particular form of the metric generated by a given distribution of matter.

The situation becomes particularly simple when we consider systems involving slow motions and weak gravitational fields. In this post-Newtonian limit, the spacetime metric $g _ { \alpha \beta }$ produced by nearly every metric theory of gravity has the same formal structure. It can be written as an expansion in powers of $c ^ { - 2 }$ about the Minkowski metric $\eta _ { \alpha \beta }$ , in terms of the Newtonian potential $U$ and many of the same post-Newtonian potentials that we encountered back in Chapter 8. (New potentials are required for some theories.) The only aspect that changes from one theory to the next is the numerical value of the various coefficients that appear in front of the potentials.

This is a very fortunate circumstance, because the post-Newtonian limit is sufficient to describe the gravitational physics of the solar system and the experimental tests one can perform there. And to a limited degree, it can also describe the gravity of binary-pulsar systems. If we therefore replace the numerical coefficients in front of all potentials in the post-Newtonian metric of general relativity with arbitrary parameters, and add a few new potentials with their own parameters, we obtain a framework that encompasses a broad spectrum of alternative theories, and that can be used to calculate a wide range of testable phenomena.

This framework is called the parameterized post-Newtonian (PPN) framework, and the main idea originated with Eddington. In his classic 1922 textbook, The Mathematical Theory of Relativity, he parameterized the post-Newtonian limit of the Schwarzschild metric (in isotropic coordinates) by expressing it in the form

$$
d s ^ { 2 } = - \Biggl [ 1 - 2 \alpha { \frac { G M } { c ^ { 2 } r } } + 2 \beta \biggl ( { \frac { G M } { c ^ { 2 } r } } \biggr ) ^ { 2 } \Biggr ] d ( c t ) ^ { 2 } + \Biggl [ 1 + 2 \gamma { \frac { G M } { c ^ { 2 } r } } \Biggr ] \bigl ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } \bigr ) ,
$$

with $\alpha , \beta$ , and $\gamma$ denoting free parameters. Eddington calculated the motion of planets and the trajectories of light rays in this metric, and obtained predictions for various measurable quantities, such as the perihelion advance of Mercury and the deflection of light. He then interpreted the measurements as empirical constraints on the free parameters, with $\alpha = \beta = \gamma = 1$ confirming the predictions of general relativity. Eddington did not realize at the time that $\alpha$ is actually a redundant parameter, because it can always be absorbed into $G M$ , which determines the Newtonian dynamics of the system and can be measured by observing its Keplerian orbital motion.

The modern version of the PPN framework, involving a gravitating system of point masses, was first developed by Kenneth Nordtvedt, Jr. in 1968. The framework was extended by one of us (CMW) to incorporate self-gravitating fluid systems. In 1972 the two approaches were unified by Nordtvedt and Will, and this gave rise to the modern version of the PPN framework, as it is used today.

# 13.2.2 Parameterized post-Newtonian metric

The metric and its potentials are displayed in Box 13.1. As we discussed previously, there is no need to introduce a parameter $\alpha$ in front of the Newtonian potential in $g _ { 0 0 }$ . Setting aside $\Phi ^ { \mathrm { P F } }$ and $\Phi _ { j } ^ { \mathrm { P F } }$ for the moment, we see that there are ten independent potentials in the post-Newtonian part of the metric. In $g _ { 0 0 }$ we recognize $U ^ { 2 }$ and the six potentials in $\psi$ , in $g _ { 0 j }$ we find $U _ { j }$ and $\partial _ { t j } X$ , and in $g _ { j k }$ there is $U$ . There is a one-to-one correspondence with the ten PPN parameters, although the assignment of parameters may appear a little strange at first.

<table><tr><td>Box 13.1</td><td>Parameterized post-Newtonian metric</td></tr><tr><td></td><td>Parameters: γ， β,$,α1,α2,α3， 51， 52， 53，54. Metric:</td></tr><tr><td></td><td>+F+0(c-，, 1</td></tr><tr><td></td><td>s[2(1 +y）+²α1]U- goj = 1</td></tr><tr><td></td><td>++0(（~5）， +</td></tr><tr><td></td><td>gk=(1+U）δ+O(c²）；</td></tr></table>

(continued overleaf)

$$
\begin{array} { l } { { \psi : = { \displaystyle \frac { 1 } { 2 } } ( 2 \gamma + 1 + \alpha _ { 3 } + \zeta _ { 1 } - 2 \xi ) \Phi _ { 1 } - ( 2 \beta - 1 - \zeta _ { 2 } - \xi ) \Phi _ { 2 } + ( 1 + \zeta _ { 3 } ) \Phi _ { 3 } } } \\ { { { } } } \\ { { + ( 3 \gamma + 3 \zeta _ { 4 } - 2 \xi ) \Phi _ { 4 } - { \displaystyle \frac { 1 } { 2 } } ( \zeta _ { 1 } - 2 \xi ) \Phi _ { 6 } - \xi \Phi _ { W } . } } \end{array}
$$

Potentials:

$$
\begin{array} { r l } & { \Phi _ { 1 } = - \bar { d } \int _ { \frac { \partial \xi } { \partial x } } ^ { \infty } \exp ^ { \frac { i \xi } { \hbar } \xi } d x \cdot \ } \\ & { + \varepsilon _ { 2 } = \sqrt { \frac { \hbar } { \hbar } \frac { \partial \xi } { \hbar } \frac { \partial \xi } { \partial x } } } \\ & { \Phi _ { 2 } = - \varepsilon _ { 1 } \left\{ \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \right\} ^ { 2 } , } \\ & { \Phi _ { 3 } = \varepsilon _ { 2 } \left\{ \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \right\} ^ { 2 } , } \\ & { \Phi _ { 4 } = - \varepsilon _ { 2 } \int _ { \frac { \partial \xi } { \partial x } } \varepsilon _ { 1 } ^ { 2 } d x ^ { 2 } , } \\ & { \Phi _ { 5 } = - \varepsilon _ { 2 } \int _ { \frac { \partial \xi } { \partial x } } ^ { \infty } \exp ^ { \frac { i \xi } { \hbar } \xi } \frac { \partial \xi } { \partial x } - \varepsilon _ { 2 } ^ { 2 } d x ^ { 2 } , } \\ & { \Phi _ { 6 } = \varepsilon _ { 3 } \left\{ \bar { \xi } ^ { \prime } \rho _ { 3 } ^ { \prime } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \right\} ^ { 2 } d x ^ { 2 } , } \\ & { - \varepsilon _ { 3 } ^ { 2 } = - \varepsilon _ { 3 } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } } \\ & { \psi = - \varepsilon _ { 2 } ^ { 2 } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } } \\ &  \psi = - \varepsilon _ { 1 } ^ { 2 } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac { \partial \xi } { \partial x } \frac \end{array}
$$

Preferred-frame potentials:

$$
\begin{array} { r l } & { \Phi ^ { \mathrm { P F } } : = ( \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { 2 } U + \alpha _ { 2 } w ^ { j } w ^ { k } \partial _ { j k } X + ( 2 \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { j } U _ { j } , } \\ & { } \\ & { \Phi _ { j } ^ { \mathrm { P F } } : = - \displaystyle \frac { 1 } { 2 } \alpha _ { 1 } w _ { j } U + \alpha _ { 2 } w ^ { k } \partial _ { j k } X . } \end{array}
$$

The quantity $w ^ { j }$ is the velocity of the PPN coordinate frame relative to a universal preferred frame.

When $\beta = \gamma = 1$ and all other parameters vanish, the metric reduces to the familiar post-Newtonian metric of general relativity, as constructed back in Sec. 8.1. The metric, however, does not quite reduce to the form displayed in Eq. (8.2) – see also Eq. (8.9). The reason is that the coordinate system $( c t , x ^ { j } )$ is not harmonic. Indeed, the PPN metric is cast in a generalization of the standard post-Newtonian gauge described back in Sec. 8.3.7. There is no deep reason behind this choice of coordinates; it merely reflects the historical development of the PPN framework.

<table><tr><td colspan="4">Table 13.1 PPN parameters and their physical significance. Note that α3 is listed twice to indicate that it isameasure of two separate effects.</td></tr><tr><td>Parameter</td><td>What it measures relative to GR</td><td>Semi-conservative GR value theories</td><td>Fully-conservative theories</td></tr><tr><td>Y</td><td>How much spatial 1 curvature produced by unit rest mass?</td><td>Y</td><td>Y</td></tr><tr><td>β</td><td>How much 1 &quot;nonlinearity”in the superposition of gravity?</td><td>β</td><td>β</td></tr><tr><td>m</td><td>Preferred-location effects?</td><td>0 m</td><td>m</td></tr><tr><td>α1 α2</td><td>Preferred-frame effects?</td><td>0 α1 0</td><td>0</td></tr><tr><td>α3</td><td>0</td><td>α2 0</td><td>0 0</td></tr><tr><td>α3</td><td>Is total 0</td><td>0</td><td>0</td></tr><tr><td>51</td><td> momentum</td><td>0 0</td><td>0</td></tr><tr><td>52</td><td>conserved? 0</td><td>0</td><td>0</td></tr><tr><td>53</td><td>0</td><td>0</td><td>0</td></tr><tr><td>54</td><td>0</td><td>0</td><td>0</td></tr></table>

The choice of parameters is made (with considerable hindsight, to be sure) to ensure that their values are particularly simple in general relativity, but more importantly, to ensure also that specific physical meanings can be attached to them. These heuristic meanings are summarized in Table 13.1. The parameters $\beta$ and $\gamma$ are directly related to Eddington’s original parameters. Roughly speaking, $\beta$ measures how non-linear gravity is, in that it multiplies the $U ^ { 2 }$ term in $g _ { 0 0 }$ , and $\gamma$ measures the spatial curvature generated by a body relative to what general relativity would predict; specifically, a calculation of the Riemann curvature tensor for the three-dimensional subspace defined by $d t = 0$ gives a result proportional to $\gamma G M / ( c ^ { 2 } r ^ { 3 } )$ . These meanings are not to be taken literally, because they are very much tied to the choice of coordinates. In general relativity, for example, the Schwarzschild metric expressed in the standard Schwarzschild coordinates has no term quadratic in $G M / ( c ^ { 2 } r )$ in $g _ { 0 0 }$ ; the post-Newtonian limit of the metric takes the Eddington form of Eq. (13.1) with $\beta = \gamma = 1$ only in isotropic coordinates. The lesson is that the interpretation of the PPN parameters must only be viewed as a rough heuristic.

The parameters $\alpha _ { n }$ are linked to violations of local Lorentz invariance in gravitational physics, which is predicted by some theories. Suppose that all three parameters vanish. If we perform a post-Galilean transformation of the PPN metric to a coordinate system moving with respect to the first, as we did back in Sec. 8.3.6 for general relativity, we discover that the metric is of the same form in the moving frame as it was in the original frame, with all variables (such as positions, velocities, and densities) referring to the new frame. In this case, the physics of an isolated gravitating system does not depend on its velocity; we can analyze it in a reference frame at rest with respect to the system’s center-of-mass, or in a frame moving relative to it with an arbitrary velocity, and the results are the same.

Now suppose that one or more of the $\alpha _ { n }$ parameters is non-zero. In this case, a post-Galilean transformation of the metric generates new terms, and these are precisely the PF terms displayed in Box 13.1. This implies that the physics of a gravitating system depends explicitly on the system’s velocity relative to our coordinate system. But what can this possibly mean, given that our coordinate system was chosen arbitrarily? It must mean that there is a preferred reference frame in the universe, a frame whose velocity $\pmb { w }$ can be taken to vanish. What is this frame? The answer must be provided by the underlying theory of gravity, and it will differ from theory to theory. An example is a theory with a dynamical timelike vector field $K ^ { \alpha }$ in addition to the metric. If $K ^ { \alpha }$ is determined by some field equations with a source related to the distribution of matter, then in a homogeneous, isotropic universe there exists a reference frame in which the vector has only a time component. By symmetry, this must be the mean rest frame of the large-scale distribution of matter and radiation, or equivalently, the rest frame of the cosmic microwave background radiation. The specifics of how this circumstance arises may vary from theory to theory, but it is reasonable to suppose that in general, the frame in which $K ^ { j } = 0$ can be identified with the preferred reference frame. Because ${ \pmb w } = { \bf 0 }$ in the preferred frame, we would find that the potentials $\Phi ^ { \mathrm { P F } }$ and $\Phi _ { j } ^ { \mathrm { P F } }$ vanish in this frame. But performing a post-Galilean transformation to any other frame automatically introduces the PF terms into the PPN metric, with a velocity $\pmb { w }$ given by the new frame’s velocity with respect to the cosmic background radiation. The PF potentials have observable consequences, and in Sec. 13.3 we see how experiments have placed very tight constraints on the $\alpha _ { n }$ parameters, all consistent with the validity of post-Galilean invariance.

One might worry that the existence of a preferred frame violates the general covariance that is presumably built into all such alternative theories. In fact, general covariance is not broken: as long as the PF potentials are included in the metric, we can perform calculations in any reference frame we like. For example, instead of adopting the solar system’s rest frame to do planetary calculations, we could adopt the rest frame of the galaxy. In this case, the $\pmb { w }$ that appears in the metric would be the velocity of the galaxy relative to the cosmic background radiation, and the velocities of all solar-system bodies would be defined with respect to the galactic center. It turns out in the end that any measurable effect depends only on the velocity of the relevant body relative to the preferred frame; the velocity of the coordinate frame always drops out. The preferred frame comes about as a result of a physical interaction, say between a vector field and the metric; it does not represent a violation of general covariance. Fundamentally, this is no different from our ability to determine the rest frame of the cosmic background radiation by interacting with its photons, except that in alternative theories with preferred-frame effects, the physical mechanism behind the existence of a preferred frame is more subtle and indirect.

The four parameters $\zeta _ { n }$ , together with the parameter $\alpha _ { 3 }$ (which plays a dual role), indicate whether the theory admits a conservation law for the total momentum of an isolated system. Energy is not included in this discussion, because in the present context of 1pn gravity, the relevant energy is rest-mass energy plus Newtonian total energy (the sum of kinetic, gravitational, and internal energies), which is conserved by virtue of the Newtonian dynamics.

Recall the Landau–Lifshitz formulation of the Einstein field equations, as presented back in Sec. 6.1, and the conservation laws that followed from them. The basic idea was that the equations of energy-momentum conservation could be expressed in the form $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ , where $\tau ^ { \alpha \beta }$ is a pseudotensor made up of the matter’s energy-momentum tensor $T ^ { \alpha \beta }$ and a contribution from the gravitational field (the Landau–Lifshitz pseudotensor). It follows from this that the quantity $P ^ { j } : = c ^ { - 1 } \textstyle \int \tau ^ { 0 j } d ^ { 3 } x$ is constant in time, apart from the small effects associated with gravitational radiation. Total momentum is therefore conserved in general relativity, and we wish to see if the conclusion extends to other theories.

In any metric theory the equation of energy-momentum conservation is given by $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , and in the post-Newtonian limit the covariant derivatives can be computed with the PPN metric displayed in $8 0 \mathrm { x } ~ 1 3 . 1$ ; the metric also appears in appropriate places within the energy-momentum tensor. It may then be asked whether one can define an object $\Theta ^ { \alpha \beta }$ such that the conservation equation can be expressed as $\partial _ { \beta } \Theta ^ { \alpha \beta } = 0$ , with partial derivatives replacing the covariant derivatives. Presumably, such an object would take a form such as $( 1 - a U / c ^ { 2 } ) ( T ^ { \alpha \beta } + t ^ { \alpha \beta } )$ , with $a$ a constant to be determined and $t ^ { \alpha \beta }$ a pseudotensor constructed from the various gravitational potentials. If this object exists, then it can be exploited to define a conserved total momentum $\begin{array} { r } { P ^ { j } : = c ^ { - 1 } \int \Theta ^ { 0 j } d ^ { 3 } x } \end{array}$ , and the theory would indeed be compatible with momentum conservation. It turns out that $\Theta ^ { \alpha \beta }$ exists provided that $\zeta _ { 1 } = \zeta _ { 2 } = \zeta _ { 3 } = \zeta _ { 4 } = \alpha _ { 3 } = 0$ . Theories of gravity with this property are called “semi-conservative.” It can be shown that any metric theory whose field equations can be derived from an invariant action principle automatically comes with a conserved momentum.

The equation $\partial _ { \beta } \Theta ^ { \alpha \beta } = 0$ guarantees only that total momentum is conserved. If we further demand that angular momentum should be conserved, and that the center-of-mass should possess a uniform motion, we must also impose that $\Theta ^ { \alpha \beta }$ be a symmetric pseudotensor. It turns out that this requires $\alpha _ { 1 } = \alpha _ { 2 } = 0$ in addition to the other constraints. Theories with this property are called “fully conservative,” and we note that it is possible for a theory formulated in terms of an action principle (especially ones with vector or tensor fields in addition to the metric) to fail to conserve angular momentum. A fully conservative theory is therefore one with no preferred-frame effects (at least at post-Newtonian order). It may seem odd that conservation of total angular momentum $J ^ { \alpha \beta }$ , including the center-of-mass quantity $J ^ { 0 j }$ , should require post-Galilean invariance, but there is nothing surprising about this: since $J ^ { 0 j }$ mixes the time and space components of a tensor, an expectation of its conservation implicitly assumes invariance under boosts.

The final parameter $\xi$ is tied to the potential $\Phi _ { W }$ , called the Whitehead potential because it was first spotted in Whitehead’s theory of gravity, although it was later found to occur in a broad class of similar theories. The potential looks particularly nasty, especially in its integral form, but it can be understood as having a simple origin. We have assumed that the spatial part of the PPN metric is diagonal, given by $g _ { j k } = ( 1 + 2 \gamma U / c ^ { 2 } ) \delta _ { j k }$ . We could, however, have included in $g _ { j k }$ a perfectly acceptable term of the form $2 \lambda \partial _ { j k } X / c ^ { 2 }$ , where $\lambda$ is an arbitrary parameter. But this term can be removed by a coordinate transformation $x ^ { j } = { \bar { x } } ^ { j } - \lambda \partial _ { j } X / c ^ { 2 }$ , which changes the metric according to

$$
\begin{array} { l l r } { { \bar { g } _ { 0 0 } ( \bar { x } ^ { \mu } ) = g _ { 0 0 } ( \bar { x } ^ { \mu } ) + 2 \lambda \Gamma _ { 0 0 } ^ { j } \partial _ { j } X / c ^ { 2 } , } } \\ { { \bar { g } _ { 0 j } ( \bar { x } ^ { \mu } ) = g _ { 0 j } ( \bar { x } ^ { \mu } ) - \lambda \partial _ { t j } X / c ^ { 3 } , } } \\ { { \bar { g } _ { j k } ( \bar { x } ^ { \mu } ) = g _ { j k } ( \bar { x } ^ { \mu } ) - 2 \lambda \partial _ { j k } X / c ^ { 2 } . } } \end{array}
$$

The change in $g _ { 0 j }$ merely modifies the coefficient of the pre-existing term involving $\partial _ { t j } X / c ^ { 3 }$ , but the change in $g _ { 0 0 }$ is more complicated. First, there is the term involving $\Gamma _ { 0 0 } ^ { j }$ . Second, while the Newtonian potential in $g _ { 0 0 }$ is to be evaluated at ${ \bar { x } } ^ { \mu }$ , it is still expressed as an integral over the old coordinate $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ , and we must transform the integration variables. The quantity $\rho ^ { * } d ^ { 3 } x ^ { \prime }$ is invariant, so $\rho ^ { * } d ^ { 3 } x ^ { \prime } = \bar { \rho } ^ { * } d ^ { 3 } \bar { x } ^ { \prime }$ , but we must write

$$
\frac { 1 } { | \bar { \bar { x } } - { \pmb x } ^ { \prime } | } = \frac { 1 } { | \bar { \bar { x } } - \bar { { \pmb x } } ^ { \prime } | } + \frac { \lambda } { c ^ { 2 } } \bar { \nabla } \bigg ( \frac { 1 } { | \bar { \bar { { \pmb x } } } - \bar { { \pmb x } } ^ { \prime } | } \bigg ) \cdot \bar { \nabla } ^ { \prime } \bar { X } ^ { \prime } .
$$

Inserting this within the Newtonian potential, and $\Gamma _ { 0 0 } ^ { j } = - \partial _ { j } U / c ^ { 2 }$ within $\bar { g } _ { 0 0 }$ , we obtain

$$
\begin{array} { l } { { \displaystyle \bar { g } _ { 0 0 } ( \bar { x } ^ { \mu } ) = g _ { 0 0 } ( \bar { x } ^ { \mu } ) - \frac { 2 } { c ^ { 4 } } \lambda \bar { \nabla } \bar { U } \cdot \bar { \nabla } \bar { X } + \frac { 2 G } { c ^ { 4 } } \lambda \bar { \nabla } \cdot \displaystyle \int \frac { \bar { \rho } ^ { * \prime } } { | \bar { x } - \bar { x } ^ { \prime } | } \bar { \nabla } ^ { \prime } \bar { X } ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime } } } \\ { { \displaystyle ~ } } \\ { { \displaystyle ~ = g _ { 0 0 } ( \bar { x } ^ { \mu } ) + \frac { 2 } { c ^ { 4 } } \lambda \big ( \bar { \Phi } _ { W } + \bar { U } ^ { 2 } + \bar { \Phi } _ { 2 } \big ) , } } \end{array}
$$

where $g _ { 0 0 }$ is now expressed entirely in terms of the barred coordinates. So we see that far from being an anomaly, the Whitehead potential can be linked to gauges in which the spatial metric is not diagonal. This occurs even in general relativity: we would pick up a Whitehead term in $g _ { 0 0 }$ if we were to transform the metric from the standard post-Newtonian gauge to one in which $g _ { j k }$ is not diagonal. In fact, there is a close analogy between this coordinate transformation in post-Newtonian theory and the transformation between isotropic and Schwarzschild coordinates for the Schwarzschild metric.

# 13.2.3 Equations of hydrodynamics

We develop the equations of hydrodynamics in the PPN framework just as we did in Chapters 7 and 8 in the case of general relativity. As in Sec 7.1, we introduce a conserved density [refer to Eq. (7.4)]

$$
\rho ^ { * } : = \sqrt { - g } \rho u ^ { 0 } / c ,
$$

where $\rho$ is the proper mass density. Using the normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ and the PPN metric, we find that the densities are related by

$$
\rho = \biggl [ 1 - \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 \gamma U \biggr ) + { \cal O } ( c ^ { - 4 } ) \biggr ] \rho ^ { * } ,
$$

which may be compared with Eq. (7.46). The components of the energy-momentum tensor are given by

$$
\begin{array} { l } { { { \displaystyle c ^ { - 2 } T ^ { 0 0 } = \rho ^ { * } \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } - ( 3 \gamma - 2 ) U + \Pi \bigg ] \bigg \} + { \cal O } ( c ^ { - 2 } ) , } \ ~ } } \\ { { { \displaystyle c ^ { - 1 } T ^ { 0 j } = \rho ^ { * } v ^ { j } \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } - ( 3 \gamma - 2 ) U + \Pi + p / \rho ^ { * } \bigg ] \bigg \} + { \cal O } ( c ^ { - 3 } ) , } \ ~ } } \\ { { { \displaystyle T ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } - ( 3 \gamma - 2 ) U + \Pi + p / \rho ^ { * } \bigg ] \bigg \} } \ ~ } } \\ { { { \displaystyle ~ + p \bigg ( 1 - \frac { 2 } { c ^ { 2 } } \gamma U \bigg ) \delta ^ { j k } + { \cal O } ( c ^ { - 4 } ) , } } } \end{array}
$$

to the required post-Newtonian order; compare these with Eq. (8.7).

Calculating the Christoffel symbols $\Gamma _ { \beta \gamma } ^ { \alpha }$ from the PPN metric and inserting them into the conservation equation $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , we eventually obtain the PPN version of Euler’s equation,

$$
\begin{array} { r l } { \rho ^ { \star } \frac { d \nu ^ { \prime } } { d t } = - \partial _ { \theta } p + \rho ^ { \star } \partial _ { \theta } U } \\ & { + \frac { 1 } { c ^ { 2 } } \Bigg \lbrace \Bigg [ \frac { 1 } { 2 } \sigma ^ { 2 } + ( 2 - \gamma ) U + \Pi + \frac { p } { \rho ^ { \star } } \Bigg ] \partial _ { \theta } p - \nu ^ { i } \partial _ { \theta } p \Bigg \rbrace } \\ & { + \frac { 1 } { c ^ { 2 } } \rho ^ { \star } \Bigg \lbrace \Bigg \lbrace \gamma \sigma ^ { 2 } - 2 ( \gamma + \beta ) U \Bigg \rbrace \partial _ { \theta } U } \\ & { - \nu ^ { \prime } \Bigg [ ( 2 \gamma + 1 ) \partial _ { \theta } U + 2 ( \gamma + 1 ) \nu ^ { k } \partial _ { \theta } U \Bigg ] } \\ & { + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) \Big [ \partial _ { \theta } U _ { j } + \nu ^ { k } \big ( \partial _ { \theta } U _ { j } - \partial _ { \theta } U _ { k } \big ) \Bigg ] + \partial _ { \theta } \nu \Bigg \rbrace } \\ & { + \frac { 1 } { c ^ { 2 } } \rho ^ { \star } \Bigg [ \frac { 1 } { 2 } \partial _ { \theta } \Phi ^ { m } - \partial _ { \theta } \Phi _ { j } ^ { m } - \nu ^ { \star } \big ( \partial _ { \theta } \Phi _ { j } ^ { m } - \partial _ { \theta } \Phi _ { k } ^ { m } \big ) \Bigg ] } \\ & { + O ( c ^ { - \alpha } ) , } \end{array}
$$

where

$$
\Psi : = \psi + \frac 1 2 ( 1 + \alpha _ { 2 } - \zeta _ { 1 } + 2 \xi ) \partial _ { t t } X ,
$$

and where $\psi , \Phi ^ { \mathrm { P F } }$ , and $\Phi _ { j } ^ { \mathrm { P F } }$ are displayed in Box 13.1. Recall that $\partial _ { t t } X = \Phi _ { 1 } + 2 \Phi _ { 4 } - \Phi _ { 5 } -$ $\Phi _ { 6 }$ . Note that the PPN equation of hydrodynamics parallels closely the general relativistic equation, displayed in Eq. (8.119). The main differences are in the numerical coefficients in front of the post-Newtonian potentials, the inclusion of the Whitehead potential in $\psi$ , and the addition of the “preferred-frame” terms.

# 13.2.4 Motion of isolated bodies

We now wish to obtain equations of motion for a system of isolated, non-rotating bodies, as we did back in Chapter 9 for the post-Newtonian limit of general relativity. The foundation for this work is Eq. (13.8), which closely resembles its general-relativistic counterpart. This implies that much of the machinery developed in Chapter 9 can be directly imported here. Additional work is required to handle the Whitehead potential and the preferred-frame terms.

The idea is to integrate Eq. (13.8) over body $A$ to find the net force acting on its center-ofmass. The force can be decomposed into “self-force” terms involving the variables of body $A$ only, and external forces produced by the other bodies. The 18 integrals of Eqs. (9.88), as evaluated in Eqs. (9.91), make contributions to these forces, and the contribution from the Whitehead potential is

$$
\begin{array} { l } { { \displaystyle F _ { 1 9 } ^ { j } : = - \frac { \xi } { c ^ { 2 } } \int _ { A } \rho ^ { * } \partial _ { j } \Phi _ { W } d ^ { 3 } x } } \\ { { \displaystyle \quad = - \frac { G ^ { 2 } \xi } { c ^ { 2 } } \sum _ { B , C } \int _ { A } \rho ^ { * } \partial _ { j } \int _ { B } \rho ^ { * \prime } \int _ { C } \rho ^ { * \prime \prime } \frac { ( x - x ^ { \prime } ) _ { k } } { | x - x ^ { \prime } | ^ { 3 } } \left[ \frac { ( x - x ^ { \prime \prime } ) ^ { k } } { | x ^ { \prime } - x ^ { \prime \prime } | } - \frac { ( x ^ { \prime } - x ^ { \prime \prime } ) ^ { k } } { | x - x ^ { \prime \prime } | } \right] } } \\ { { \displaystyle \qquad \times d ^ { 3 } x d ^ { 3 } x ^ { \prime } d ^ { 3 } x ^ { \prime \prime } } , } \end{array}
$$

where the double sum over bodies $B$ and $C$ includes body $A$ . When $B$ and $C$ both refer to body $A$ , it is straightforward to see that the integral vanishes because of the assumed reflection symmetry of the density distribution (refer to Sec. 9.1.2). When $B$ refers to body $A$ , while $C$ refers to an external body, we expand $\boldsymbol { x } - \boldsymbol { x } ^ { \prime \prime }$ and $\mathbf { x } ^ { \prime } - \mathbf { x } ^ { \prime \prime }$ about the centerof-mass of body $A$ . The method is very similar to, though slightly more tedious than, the method used to evaluate $F _ { 1 4 } ^ { j }$ in Sec. 9.3.2. We find that some of the double integrals over $\boldsymbol { x }$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ in body $A$ vanish by symmetry, while others lead to terms involving $\Omega _ { A } ^ { j k }$ and $\Omega _ { A }$ . Higher-order terms in the expansions can be neglected because of our assumption that the bodies are well separated. Similar considerations apply when $C$ refers to body $A$ and $B$ refers to an external body, leading to terms involving $\Omega _ { A } ^ { j k }$ and $\Omega _ { A }$ , as well as a term involving $U _ { \neg A }$ evaluated at body $B$ . The final case, with both $B$ and $C$ referring to an external body, involves external potentials only. We denote the collection of terms involving external potentials by $\Phi _ { W , \lnot A }$ , and the final result for $F _ { 1 9 } ^ { j }$ is

$$
c ^ { 2 } F _ { 1 9 } ^ { j } = 6 \Omega _ { \cal A } \partial _ { j } U _ { - { \cal A } } - 3 \Omega _ { \cal A } ^ { j k } \partial _ { k } U _ { - { \cal A } } - \Omega _ { \cal A } ^ { k l } \partial _ { j k l } X _ { - { \cal A } } + m _ { \cal A } \partial _ { j } \Phi _ { W , - { \cal A } } .
$$

The contribution to the force that comes from the preferred-frame potentials is

$$
F _ { \mathrm { P F } } ^ { j } = \frac { 1 } { c ^ { 2 } } \int _ { A } \rho ^ { * } \left( \frac { 1 } { 2 } \partial _ { j } \Phi ^ { \mathrm { P F } } - \partial _ { t } \Phi _ { j } ^ { \mathrm { P F } } - 2 v ^ { k } \partial _ { [ j } \Phi _ { k ] } ^ { \mathrm { P F } } \right) d ^ { 3 } x .
$$

This can be handled in much the same way, with the help of some results from Sec. 9.3. We merely quote the final answer:

$$
\begin{array} { l } { { { \displaystyle c ^ { 2 } F _ { \mathrm { P F } } ^ { j } = \left[ \alpha _ { 1 } H _ { A } \delta ^ { j k } - \alpha _ { 2 } \bigl ( 2 H _ { A } ^ { ( j k ) } - 3 K _ { A } ^ { j k } + H _ { A } \delta ^ { j k } \bigr ) - \alpha _ { 3 } H _ { A } ^ { k j } \right] w ^ { k } } } } \\ { { \mathrm { ~ } + { \displaystyle \frac { 1 } { 2 } ( \alpha _ { 3 } - \alpha _ { 1 } ) m _ { A } w ^ { 2 } \partial _ { j } U _ { - A } + \frac { 1 } { 2 } \alpha _ { 2 } m _ { A } w ^ { k } w ^ { l } \partial _ { j k l } X _ { - A } } } } \\ { { \mathrm { ~ } + { \displaystyle \frac { 1 } { 2 } ( 2 \alpha _ { 3 } - \alpha _ { 1 } ) m _ { A } w ^ { k } \partial _ { j } U _ { k , - A } + \frac { 1 } { 2 } \alpha _ { 1 } m _ { A } w ^ { j } \partial _ { t } U _ { - A } } } } \\ { { \mathrm { ~ } - \alpha _ { 2 } m _ { A } w ^ { k } \partial _ { t j k } X _ { - A } + \alpha _ { 1 } m _ { A } v _ { A } ^ { k } w _ { [ j } \partial _ { k ] } U _ { - A } . } } \end{array}
$$

Collecting results, we find that the acceleration of body $A$ is given by

$$
a _ { \cal A } ^ { j } = \partial _ { j } U _ { \neg { \cal A } } + ( a _ { \cal A } ^ { j } ) _ { \mathrm { s e l f } } + ( a _ { \cal A } ^ { j } ) _ { \mathrm { e x t } } + ( a _ { \cal A } ^ { j } ) _ { \mathrm { P F } } + O ( c ^ { - 4 } ) .
$$

The first term is of course the Newtonian acceleration created by the external bodies. The second term contains all self-interaction effects, including those coming from the preferred-frame potentials:

$$
\begin{array} { r l } & { m _ { \cal A } c ^ { 2 } ( a _ { \cal A } ^ { j } ) _ { \mathrm { s e f f } } = \Big [ 2 L _ { \cal A } ^ { ( j k ) } - ( 2 + \alpha _ { 2 } ) H _ { \cal A } ^ { j k } - ( 2 + \alpha _ { 2 } + \alpha _ { 3 } ) H _ { \cal A } ^ { k j } + 3 ( 1 + \alpha _ { 2 } ) K _ { \cal A } ^ { j k } } \\ & { \phantom { m m m m m m m m m m m m } + ( \alpha _ { 1 } - \alpha _ { 2 } ) \delta ^ { j k } H _ { \cal A } - \delta ^ { j k } \bar { P } _ { \cal A } \Big ] v _ { \cal A } ^ { k } } \\ & { \phantom { m m m m m m m m m m } + \Big [ \alpha _ { 1 } H _ { \cal A } \delta ^ { j k } - \alpha _ { 2 } ( 2 H _ { \cal A } ^ { ( j k ) } - 3 K _ { \cal A } ^ { j k } + H _ { \cal A } \delta ^ { j k } ) - \alpha _ { 3 } H _ { \cal A } ^ { k j } \Big ] w ^ { k } } \\ & { \phantom { m m m m m m m m m m } + \Big [ 2 \gamma T _ { \cal A } + ( 4 \beta - 3 - \alpha _ { 1 } + \alpha _ { 2 } - \zeta _ { 1 } - 4 \xi ) \Omega _ { \cal A } + 3 \gamma P _ { \cal A } \Big ] \partial _ { j } U _ { - { \cal A } } } \\ & { \phantom { m m m m m m m m m m } - \Big [ 4 ( \gamma + 1 ) T _ { \cal A } ^ { j k } + ( 2 \gamma + 2 + \alpha _ { 2 } - \zeta _ { 1 } + \zeta _ { 2 } ) \Omega _ { \cal A } ^ { j k } } \\ & { \phantom { m m m m m m m m m m m } + 2 ( \gamma + 1 ) \delta ^ { j k } P _ { \cal A } \Big ] \partial _ { k } U _ { - \cal A } + \xi \Omega _ { \cal A } ^ { k l } \partial _ { j k l } X _ { - { \cal A } } . } \end{array}
$$

As we did back in Chapter 9, we invoke the conditions (9.10)–(9.12) satisfied by a body in internal dynamical equilibrium,

$$
\begin{array} { r } { 2 \mathcal { T } _ { A } ^ { j k } + \Omega _ { A } ^ { j k } + \delta ^ { j k } P _ { A } = O ( c ^ { - 2 } ) , } \\ { 4 H _ { A } ^ { ( j k ) } - 3 K _ { A } ^ { j k } - 2 L _ { A } ^ { ( j k ) } + \delta ^ { j k } \dot { P } _ { A } = O ( c ^ { - 2 } ) , } \\ { 2 \mathcal { T } _ { A } + \Omega _ { A } + 3 P _ { A } = O ( c ^ { - 2 } ) . } \end{array}
$$

We also invoke the additional steady-state conditions

$$
\begin{array} { l } { { \dot { \Omega } _ { \cal A } ^ { j k } = 2 H _ { \cal A } ^ { ( j k ) } - 3 K _ { \cal A } ^ { j k } = 0 , } } \\ { { \dot { \Omega } _ { \cal A } = - H _ { \cal A } = 0 , } } \end{array}
$$

and obtain the final expression

$$
\begin{array} { l } { { ( a _ { \cal A } ^ { j } ) _ { \mathrm { s e l f } } = - { \displaystyle \frac { \alpha _ { 3 } } { m _ { \cal A } c ^ { 2 } } } H _ { \cal A } ^ { k j } ( w _ { k } + v _ { { \cal A } k } ) } } \\ { ~ } \\ { { ~ + ~ ( 4 \beta - \gamma - 3 - 4 \xi - \alpha _ { 1 } + \alpha _ { 2 } - \zeta _ { 1 } ) { \displaystyle \frac { \Omega _ { \cal A } } { m _ { \cal A } c ^ { 2 } } } \partial _ { j } U _ { - { \cal A } } } } \\ { { ~ - ~ ( \alpha _ { 2 } - \zeta _ { 1 } + \zeta _ { 2 } ) { \displaystyle \frac { \Omega _ { \cal A } ^ { j k } } { m _ { \cal A } c ^ { 2 } } } \partial _ { k } U _ { - { \cal A } } + \xi { \displaystyle \frac { \Omega _ { \cal A } ^ { k l } } { m _ { \cal A } c ^ { 2 } } } \partial _ { j k l } X _ { - { \cal A } } } } \end{array}
$$

for the self-acceleration. The acceleration produced by the external post-Newtonian potentials is given by

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle c ^ { 2 } ( a _ { \cal A } ^ { j } ) _ { \mathrm { e x t } } = \left[ \gamma v _ { \cal A } ^ { 2 } - 2 ( \gamma + \beta ) U _ { - \cal A } \right] \partial _ { j } U _ { - \cal A } } } \\ { { } } & { { } } & { { ~ - v _ { \cal A } ^ { j } \left[ 2 ( \gamma + 1 ) v _ { \cal A } ^ { k } \partial _ { k } U _ { - \cal A } + ( 2 \gamma + 1 ) \partial _ { t } U _ { - \cal A } \right] } } \\ { { } } & { { } } & { { ~ + \displaystyle \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) \left[ \partial _ { t } U _ { - \cal A } ^ { j } + v _ { \cal A } ^ { k } ( \partial _ { k } U _ { j - \cal A } - \partial _ { j } U _ { k - \cal A } ) \right] } } \\ { { } } & { { } } & { { ~ + \partial _ { j } \Psi _ { - \cal A } ~ , } } \end{array}
$$

where

$$
\begin{array} { l } { { \Psi _ { - { \cal A } } = \displaystyle \frac { 1 } { 2 } ( 2 \gamma + 2 + \alpha _ { 2 } + \alpha _ { 3 } ) \Phi _ { 1 , - { \cal A } } - ( 2 \beta - 1 - \zeta _ { 2 } - \xi ) \Phi _ { 2 , - { \cal A } } } } \\ { { \displaystyle ~ + ( 1 + \zeta _ { 3 } ) \Phi _ { 3 , - { \cal A } } + ( 3 \gamma + 1 + \alpha _ { 2 } + 3 \zeta _ { 4 } - \zeta _ { 1 } ) \Phi _ { 4 , - { \cal A } } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 } ( 1 + \alpha _ { 2 } - \zeta _ { 1 } + 2 \xi ) \Phi _ { 5 , - { \cal A } } - \frac { 1 } { 2 } ( 1 + \alpha _ { 2 } ) \Phi _ { 6 , - { \cal A } } - \xi \Phi _ { W , - { \cal A } } , } } \end{array}
$$

and the preferred-frame acceleration is

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle c ^ { 2 } ( a _ { \cal A } ^ { j } ) _ { \mathrm { P F } } = + \displaystyle \frac { 1 } { 2 } ( \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { 2 } \partial _ { j } U _ { - \cal A } + \displaystyle \frac { 1 } { 2 } \alpha _ { 2 } w ^ { k } w ^ { l } \partial _ { j k l } X _ { - { \cal A } } } } \\ { { } } & { { } } & { { ~ + \displaystyle \frac { 1 } { 2 } ( 2 \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { k } \partial _ { j } U _ { k , - { \cal A } } + \displaystyle \frac { 1 } { 2 } \alpha _ { 1 } w ^ { j } \partial _ { t } U _ { - { \cal A } } } } \\ { { } } & { { } } & { { ~ - \alpha _ { 2 } w ^ { k } \partial _ { t j k } X _ { - { \cal A } } + \alpha _ { 1 } v _ { \cal A } ^ { k } w _ { [ j } \partial _ { k ] } U _ { - \cal A } . } } \end{array}
$$

We must now evaluate the derivatives of the external potentials. Again we find that most of the hard work has already been carried out in Chapter 9, and the results of Eqs. (9.103) can all be imported here. The only additional work required is to evaluate $\partial _ { j } \Phi _ { W , \lnot A }$ . When $B$ and $C$ refer to different external bodies, we can treat each body as a point mass and calculate the gradient of the potential directly in terms of the masses and separations. But when $B$ and $C$ both refer to the same external body $B$ , we must expand $\boldsymbol { x } - \boldsymbol { x } ^ { \prime }$ and $\boldsymbol { x } - \boldsymbol { x } ^ { \prime \prime }$ about the center-of-mass of body $B$ . This generates a structure-dependent term proportional to $\Omega _ { B } { \pmb n } _ { A B } / r _ { A B } ^ { 2 }$ . A similar term arises when $B$ is in an external body and $C$ refers to body $A$ . The final result is

$$
\begin{array} { l } { { \partial _ { j } \Phi _ { W , \neg A } = - \displaystyle \sum _ { B \not = A } { \frac { 2 G \Omega _ { B } n _ { A B } ^ { j } } { r _ { A B } ^ { 2 } } } - \displaystyle \sum _ { B \not = A } { \frac { G ^ { 2 } m _ { A } m _ { B } n _ { A B } ^ { j } } { r _ { A B } ^ { 3 } } } } } \\ { { + \displaystyle \sum _ { B \not = A } \displaystyle \sum _ { C \not = A , B } { \frac { G ^ { 2 } m _ { B } m _ { C } } { r _ { A B } ^ { 2 } } } \left\{ { \frac { \delta ^ { j k } - 3 n _ { A B } ^ { j } n _ { A B } ^ { k } } { r _ { A B } } } { \left[ { \frac { r _ { B C } } { r _ { A C } } } n _ { B C } ^ { k } - { \frac { r _ { A C } } { r _ { B C } } } n _ { A C } ^ { k } \right]  } } } \\ \right.{ { \left. \qquad - { \frac { n _ { A B } ^ { k } } { r _ { A C } } } { \left[ { \frac { r _ { A C } } { r _ { B C } } } \delta ^ { j k } + { \frac { r _ { B C } } { r _ { A C } } } n _ { A C } ^ { j } n _ { B C } ^ { k } \right] } } . } } \en\right\ d{array} \end{array}
$$

Collecting results, we obtain an explicit expression for the acceleration of body $A$ . As we did back in Sec. 9.3.5, we decompose it as

$$
\begin{array} { r } { \pmb { a } _ { \cal A } = \pmb { a } _ { \cal A } [ \mathrm { E X T } ] + \pmb { a } _ { \cal A } [ \mathrm { s T R } ] + O ( c ^ { - 4 } ) , \ } \\ { \pmb { a } _ { \cal A } [ \mathrm { E X T } ] = \pmb { a } _ { \cal A } [ 0 \mathrm { P N } ] + \pmb { a } _ { \cal A } [ 1 \mathrm { P N } ] , \ \quad \quad } \end{array}
$$

where $\pmb { a } _ { A } [ 0 \mathrm { P N } ]$ is the Newtonian acceleration, $\pmb { a } _ { \ r { A } } [ 1 \mathrm { P N } ]$ groups all the post-Newtonian corrections that do not depend on the internal structures of the bodies, and $\pmb { a } _ { A } [ \mathrm { \bf S T R } ]$ contains all the structure-dependent terms. As we also did back in Sec. 9.3.5, we pull out a term

$$
{ \bf { a } } _ { A } [ \mathrm { { s T R } } ] ^ { \prime } = - \sum _ { B \ne A } { \frac { G ( E _ { B } / c ^ { 2 } ) } { r _ { A B } ^ { 2 } } } { \bf { n } } _ { A B } ,
$$

from $\pmb { a } _ { A } [ \mathbf { S } \mathbf { T } \mathbf { R } ]$ , where $E _ { B } = \mathcal { T } _ { B } + \Omega _ { B } + E _ { B } ^ { \mathrm { i n t } }$ is the total energy of body $B$ , and combine it with the $0 \mathrm { P N }$ term to obtain

$$
{ \pmb a } _ { \cal A } [ 0 \mathrm { P N } ] + { \pmb a } _ { \cal A } [ \mathrm { S T R } ] ^ { \prime } = - \sum _ { B \not = A } { \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } { \pmb n } _ { A B } ,
$$

where $M _ { B } : = m _ { B } + E _ { B } / c ^ { 2 } + O ( c ^ { - 4 } )$ is the total gravitational mass of body $B$ . We can then insert $m _ { B } = M _ { B } + O ( c ^ { - 2 } )$ in all post-Newtonian terms in the acceleration without changing the equations of motion at 1pn order. In Chapter 9 this procedure eliminated all structure-dependent terms from the equations of motion. Here, in contrast, the remaining terms are given by

$$
\begin{array} { l } { { { \displaystyle { \cal E } ^ { 2 } { \sigma } _ { A } ^ { f } [ 5 \pi ] = - \frac { \alpha _ { S } ^ { 3 } } { M _ { A } } { \cal H } _ { A } ^ { H } ( w _ { k } + v _ { A k } ) } } } \\ { { \ ~ + \displaystyle { \sum _ { \scriptstyle \emptyset d \setminus \{ \mathbf { X } _ { F } \} } \Big \{ ( 4 \beta - \gamma - 3 - 4 \xi - \alpha _ { 1 } + \alpha _ { 2 } - \zeta _ { 1 } ) \frac { \Omega _ { A } } { M _ { A } } \partial _ { j } ( r _ { A k } ) ^ { - 1 } } } } \\ { ~ } \\ { { \ ~ - \left( \alpha _ { 2 } - \zeta _ { 1 } + \zeta _ { 2 } \right) \frac { \Omega _ { A } ^ { H } } { M _ { A } } \partial _ { k } ( r _ { A k } ) ^ { - 1 } + \frac { \sum _ { \scriptstyle \emptyset \neq \{ \lambda \} } ^ { \{ \pm \lambda \} } } { M _ { A } } \partial _ { j k } r _ { A k } } } \\ { { \ ~ + \left( 4 \beta - \gamma - 3 - 4 \xi - \frac { 1 } { 2 } \alpha _ { 3 } - 2 \zeta _ { 2 } \right) \frac { \Omega _ { B } } { M _ { B } } \partial _ { j } ( r _ { A k } ) ^ { - 1 } } } \\ { { \ ~ + \left( \xi - \frac { 1 } { 2 } \zeta _ { 1 } \right) \frac { \Omega _ { A } ^ { H } } { M _ { B } } \partial _ { j k } r _ { A k } - \zeta _ { 3 } \frac { E _ { \{ \lambda \} } ^ { H } } { M _ { B } } \partial _ { j } ( r _ { A k } ) ^ { - 1 } } }  \\ { { \ ~ + \left( \frac { 3 } { 2 } \alpha _ { 3 } - 3 \zeta _ { 4 } + \zeta _ { 1 } \right) \frac { P _ { B } } { M _ { B } } \partial _ { j } ( r _ { A k } ) ^ { - 1 } \ . } } \end{array}
$$

These structure-dependent terms all vanish when the PPN parameters take their generalrelativistic values. In general, however, the acceleration of a body in the field of other bodies can depend on its internal structure (dependence on $\Omega _ { A }$ ), and can even contain a component in a direction perpendicular to the direction of the other body (dependence on $\Omega _ { A } ^ { j k }$ ). Furthermore, the gravitational attraction produced by an external body can depend on its own internal structure (dependence on $\Omega _ { B }$ , $E _ { B } ^ { \mathrm { i n t } } , P _ { B } )$ . These violations of the strong equivalence principle can persist even in a fully conservative theory $\textstyle ( \alpha _ { n } = \zeta _ { n } = 0$ ), depending on the values of $\gamma , \beta$ , and $\xi$ . We notice the remarkable fact that the term proportional to $\alpha _ { 3 }$ depends on the body’s net velocity ${ \pmb w } + { \pmb v } _ { A }$ relative to the preferred frame; as we have observed before, general covariance implies that the equations of motion cannot depend on the velocity of the PPN frame relative to the preferred frame.

The remaining terms in the post-Newtonian equations of motion are the $N$ -body terms analogous to those displayed in Eq. (9.127):

$$
\begin{array} { l } { { \displaystyle { \pmb a } _ { { \cal A } } [ \mathrm { { E X T } } ] = - \sum _ { B \not = { \cal A } } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } { \pmb n } _ { A B } } } \\ { { \displaystyle ~ + \frac { 1 } { c ^ { 2 } } \left[ - \sum _ { B \not = { \cal A } } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } \biggl \{ \gamma v _ { A } ^ { 2 } - ( 2 \gamma + 2 ) ( { \pmb v } _ { A } \cdot { \pmb v } _ { B } ) + ( \gamma + 1 ) v _ { B } ^ { 2 } \biggr . \right. } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { r l } & { - \frac { 2 } { 3 } ( \alpha _ { k } - \omega ^ { 2 } ) ^ { 2 } + \frac { 1 } { 3 } \alpha _ { k } - \omega ^ { 2 } + \frac { 1 } { 2 } \gamma - \omega ^ { 2 } + \omega ^ { 2 } + \omega ^ { 2 } + \omega ^ { 2 } } \\ & { - \frac { 1 } { 2 } \frac { \omega } { 2 } ( \omega + \omega ^ { 2 } ) \omega + \omega ^ { 2 } - \frac { \omega ^ { 2 } } { 3 } ( \omega + \omega ^ { 2 } ) \omega ^ { 2 } + \frac { \omega ^ { 2 } } { 3 } ( \omega - \omega ^ { 2 } ) ^ { 2 } } \\ & { \qquad \Big ( \alpha _ { k } + 1 \big ) ^ { 2 } \alpha _ { k } + \frac { \omega ^ { 2 } } { 3 } \left( \alpha _ { k } + \omega ^ { 2 } \right) ^ { 2 } + \frac { \omega ^ { 2 } } { 3 } ( \omega + \omega ^ { 2 } ) ^ { 2 } + 2 \Gamma _ { k } ^ { 2 } \Gamma _ { k } ^ { 2 } \Gamma _ { k } ^ { 2 } \Big ( \omega + \omega ^ { 2 } \Big ) ^ { 2 } \Gamma _ { k } ^ { 2 } , } \\ & { + \sum _ { s = 1 } ^ { 2 } \frac { \omega } { 2 } \bigg [ \mathrm { s i n } \bigg \{ 1 + \Gamma _ { s } ^ { 2 } ( \omega + \omega ^ { 2 } ) + \Gamma _ { s } ^ { 2 } ( \omega + \omega ^ { 2 } ) \Big \} \Big ( 1 + \Gamma _ { s } ^ { 2 } \omega + \Gamma _ { s } ^ { 2 } \Big ) } \\ & { - \sum _ { s = 1 } ^ { 2 } \frac { \omega } { 2 } \bigg [ \mathrm { s i n } \bigg \{ 1 + \Gamma _ { s } ^ { 2 } ( \omega + \omega ^ { 2 } ) - \frac { \omega ^ { 2 } } { 3 } ( \omega - \omega ^ { 2 } ) \Big \} \Big ( 1 + \Gamma _ { s } ^ { 2 } \omega + \Gamma _ { s } ^ { 2 } \Big ) } \\ & { + \sum _ { s = 1 } ^ { 2 } \frac { \omega } { 2 } \bigg ( \mathrm { s i n } \bigg \{ 1 + \Gamma _ { s } ^ { 2 } ( \omega + \omega ^ { 2 } ) + \frac { \omega } { 3 } ( \omega - \omega ^ { 2 } ) \Gamma _ { k } ^ { 2 } ( \omega + \omega ^ { 2 } ) } \\ &  - \sum _ { s = 1 } ^ { 2 } \frac { \omega ^ { 2 } } { \gamma } \bigg ( \mathrm { s i n } \bigg  \end{array}
$$

Setting the PPN parameters equal to their general relativistic values allows us to recover Eq. (9.127).

The appearance of structure-dependent terms in the equations of motion is a radical departure from general relativity. We conclude this section with a discussion of this remarkable phenomenon. In discussions of the equivalence principle in Newtonian gravitation, it can be useful to identify three types of mass that characterize gravitating bodies: the inertial mass $M _ { \mathcal { T } }$ , which relates momentum to velocity, or force to acceleration; the passive gravitational mass $M _ { \mathcal { P } }$ , which relates gravitational force to the gradient of the potential; and the active gravitational mass $M _ { A }$ , which determines the potential of the gravitating body. With these definitions, we write

$$
{ \bf F } _ { \cal A } = ( M _ { \cal T } ) _ { \cal A } \frac { d { \pmb v } _ { \cal A } } { d t } = ( M _ { \cal P } ) _ { \cal A } { \pmb \nabla } \sum _ { B \not = { \cal A } } \frac { ( M _ { \cal A } ) _ { B } } { r _ { \cal A B } } ,
$$

or

$$
{ \pmb a } _ { A } = \left( \frac { M _ { \mathcal { P } } } { M _ { \mathcal { T } } } \right) _ { A } \sum _ { B \neq A } { \nabla \frac { ( M _ { A } ) _ { B } } { r _ { A B } } } .
$$

So if the inertial and passive masses of body $A$ are not equal, the motion of body $A$ will depend on its internal structure. From Eq. (13.26) we see not only that the masses are not generally equal in PPN gravity, but that they are actually tensorial in nature. We

also observe that the active mass of each body is tensorial and structure-dependent. When each body is spherically symmetric we can use the fact that $\begin{array} { r } { \Omega _ { A } ^ { j k } = \frac { 1 } { 3 } \delta ^ { j k } \Omega _ { A } } \end{array}$ to simplify the structure-dependent terms. In this case the active and passive masses reduce to

$$
\begin{array} { r l } & { \frac { ( M _ { \mathcal { P } } ) _ { A } } { M _ { A } } = 1 + \bigg ( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } \bigg ) \frac { \Omega _ { A } } { M _ { A } c ^ { 2 } } , } \\ & { \frac { ( M _ { A } ) _ { B } } { M _ { B } } = 1 + \bigg ( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \frac { 1 } { 2 } \alpha _ { 3 } - \frac { 1 } { 3 } \zeta _ { 1 } - 2 \zeta _ { 2 } \bigg ) \frac { \Omega _ { B } } { M _ { B } c ^ { 2 } } } \\ & { \quad \quad \quad + \zeta _ { 3 } \frac { E _ { B } ^ { \mathrm { i n t } } } { M _ { B } c ^ { 2 } } - \bigg ( \frac { 3 } { 2 } \alpha _ { 3 } + \zeta _ { 1 } - 3 \zeta _ { 4 } \bigg ) \frac { P _ { B } } { M _ { B } c ^ { 2 } } . } \end{array}
$$

We now observe that when we sum Eq. (13.28) over all bodies, we obtain

$$
\sum _ { A } ( M _ { \bar { \mathcal { I } } } ) _ { A } \frac { d \pmb { v } _ { A } } { d t } = \sum _ { A } \sum _ { B \neq A } ( M _ { \mathcal { P } } ) _ { A } ( M _ { A } ) _ { B } \frac { \pmb { n } _ { A B } } { r _ { A B } ^ { 2 } } .
$$

The double sum vanishes when the product $( M _ { \mathcal { P } } ) _ { A } ( M _ { \mathcal { A } } ) _ { B }$ is symmetric under an exchange of $A$ and $B$ ; under such a circumstance the system’s total momentum is conserved, and the center-of-mass moves uniformly with a constant speed. This occurs, for example, when the active mass of each body is equal to its passive mass, and this is an expression of Newton’s third law. When do we expect this to occur for PPN gravity? If we examine Eq. (13.26) and impose the constraints of a fully conservative theory of gravity, $\alpha _ { n } = \zeta _ { n } = 0$ , we see that the structure-dependent terms depend only on $\Omega _ { A } , \Omega _ { B }$ and their associated tensors, and that the contributions are then symmetric in $A$ and $B$ . Under such a circumstance we have that the sum $\textstyle \sum _ { A } M _ { A } a _ { A } ^ { j }$ [str] vanishes, and the same is true for $\begin{array} { r l } { \sum _ { A } M _ { A } a _ { A } ^ { j } [ \mathrm { E X T } ] } \end{array}$ . There are therefore theories that violate the strong equivalence principle $M _ { \mathcal { P } } \neq M _ { \mathcal { I } }$ ) but still satisfy Newton’s third law $M _ { \mathcal { P } } = M _ { \mathcal { A } }$ ).

# 13.2.5 Motion of light

To the post-Newtonian order required to describe the deflection of light and the Shapiro time delay, we can approximate the PPN metric to

$$
d s ^ { 2 } = - ( 1 - 2 U / c ^ { 2 } ) d ( c t ) ^ { 2 } + ( 1 + 2 \gamma U / c ^ { 2 } ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ) .
$$

The null condition $g _ { \alpha \beta } v ^ { \alpha } v ^ { \beta } = 0$ implies that $( v / c ) ^ { 2 } = 1 - 2 ( 1 + \gamma ) U / c ^ { 2 } + O ( c ^ { - 3 } )$ , and $\pmb { v }$ can therefore be expressed as

$$
\pmb { v } = c \left[ 1 - ( 1 + \gamma ) \frac { U } { c ^ { 2 } } \right] \pmb { n } + O ( c ^ { - 3 } ) ,
$$

in terms of a unit vector $\pmb { n }$ . Calculating the Christoffel symbols to the appropriate order and inserting them into the geodesic equation produces

$$
\frac { d n ^ { j } } { d t } = \frac { 1 + \gamma } { c } \big ( \delta ^ { j k } - n ^ { j } n ^ { k } \big ) \partial _ { k } U + O ( c ^ { - 2 } )
$$

after making use of Eq. (13.33). Comparing this with the general relativistic equations displayed in Eqs. (8.17) and (8.19), we see that the factor 2 in each equation has been

replaced by $1 + \gamma$ . Otherwise, the equations that describe the propagation of light in PPN gravity are the same as in general relativity.

# 13.2.6 Metric near a moving body and local gravitational constant

Back in Sec. 9.4 we carried out a transformation of the general relativistic post-Newtonian metric to a non-inertial frame that moved with one body in a system of isolated bodies. With a suitable choice of transformation functions we could make the metric in the region outside the selected body look precisely like the Schwarzschild metric (expanded to 1pn order), plus correction terms proportional to $\bar { r } ^ { 2 }$ representing tidal potentials created by the other bodies in the system $\bar { r }$ is the distance away from the selected body). To make this work we had to set the acceleration of the moving frame to be precisely equal to the 1pn acceleration of the selected body. Furthermore, the body’s internal structure played no role in the analysis (although we did assume that it was spherically symmetric for simplicity); we only used the fact that its exterior geometry could be described by the Schwarzschild metric, apart from the tidal corrections. This exercise illustrated the notion that in general relativity, the equations of motion of an isolated body can be obtained by exploiting only the vacuum field equations, which apply between bodies, an idea that goes all the way back to the famous 1938 paper by Einstein, Infeld and Hoffmann. But it illustrated also the validity of the strong equivalence principle in general relativity, because the motion of the body was seen to be manifestly independent of its internal structure.

This exercise can be repeated using the PPN metric, but the results are very different, and they lead to additional tests of gravitational theories. The calculation is long and tedious, and we will not trouble the reader with it here. For simplicity we assume that the body does not have a significant gravitational binding energy. As before we find that we must require the non-inertial frame to move with an acceleration equal to the PPN acceleration, as given by Eq. (13.27). The final form of the transformed metric to 1pn order is

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + 2 { \displaystyle \frac { G _ { \mathrm { e f f } } M } { c ^ { 2 } \bar { r } } } - 2 \beta \left( { \displaystyle \frac { G _ { \mathrm { e f f } } M } { c ^ { 2 } \bar { r } } } \right) ^ { 2 } + { \cal O } ( \bar { r } ^ { 2 } ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { g _ { 0 j } = - \displaystyle \frac { 1 } { 2 } \alpha _ { 1 } ( w + v ) _ { j } { \displaystyle \frac { G _ { \mathrm { e f f } } M } { c ^ { 2 } \bar { r } } } + { \cal O } ( \bar { r } ^ { 2 } ) + { \cal O } ( c ^ { - 5 } ) , } } \\ { { g _ { j k } = \left( 1 + 2 \gamma { \displaystyle \frac { G _ { \mathrm { e f f } } M } { c ^ { 2 } \bar { r } } } \right) \delta _ { j k } + { \cal O } ( \bar { r } ^ { 2 } ) + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where the effective gravitational “constant” $G _ { \mathrm { e f f } }$ is given by

$$
\begin{array} { l } { { G _ { \mathrm { e f f } } : = { \cal G } \displaystyle \left\{ 1 - \frac { 1 } { c ^ { 2 } } ( 4 \beta - \gamma - 3 - 4 \xi - \zeta _ { 2 } ) \hat { U } _ { \mathrm { e x t } } - \frac { 1 } { c ^ { 2 } } \xi \bar { n } ^ { j } \bar { n } ^ { k } \partial _ { \bar { j } \bar { k } } \hat { X } _ { \mathrm { e x t } } \right. } } \\ { { \displaystyle ~ - \left. \frac { 1 } { 2 c ^ { 2 } } ( \alpha _ { 1 } - \alpha _ { 2 } - \alpha _ { 3 } ) ( w + v ) ^ { 2 } - \frac { 1 } { 2 c ^ { 2 } } \alpha _ { 2 } \big [ ( w + v ) \cdot \bar { n } \big ] ^ { 2 } \right. } } \\ { { \displaystyle ~ - \left. \frac { 1 } { 2 c ^ { 2 } } ( 4 \beta - \gamma - 3 - 4 \xi + \alpha _ { 2 } - \zeta _ { 1 } ) \bar { x } ^ { k } \partial _ { \bar { k } } \hat { U } _ { \mathrm { e x t } } \right. } } \\ { { \displaystyle ~ - \left. \frac { 1 } { 2 c ^ { 2 } } \xi \bar { r } \bar { n } ^ { j } \bar { n } ^ { k } \bar { n } ^ { l } \partial _ { \bar { j } \bar { k } \bar { l } } \hat { X } _ { \mathrm { e x t } } \right\} , } } \end{array}
$$

where $\bar { n } ^ { j } = \bar { x } ^ { j } / \bar { r }$ and the “hatted potentials” were introduced in Sec. 8.3; they denote the original external potentials (the ones that appear in the inertial-frame metric) evaluated at the center-of-mass position of the moving body.

There are several interesting observations to be made about this result. The first is that in general relativity $\beta = \gamma = 1$ , all other parameters vanishing), the coordinate transformation eliminates all reference to the external universe, up to the expected tidal terms at order $\bar { r } ^ { 2 }$ , and returns the post-Newtonian limit of the Schwarzschild metric with $G _ { \mathrm { e f f } } = G$ . This reproduces what we found back in Sec. 9.4. But this is not so in a generic alternative theory: external bodies and the existence of a preferred frame can influence the geometry of our local frame. This is a clear example of a violation of the strong equivalence principle, as it was introduced in Sec. 13.1. The violations can be encapsulated in an effective gravitational parameter $G _ { \mathrm { e f f } }$ , which is no longer constant, and an additional gravitomagnetic term in $g _ { 0 j }$ .

The second observation is that the metric and $G _ { \mathrm { e f f } }$ depend on the combination ${ \pmb w } + { \pmb v }$ , the body’s velocity relative to the preferred universal frame; the arbitrarily chosen velocity $\pmb { w }$ of the initial PPN frame is by itself irrelevant. The third observation is that $G _ { \mathrm { e f f } }$ varies with time as $\hat { U } _ { \mathrm { e x t } }$ or $\pmb { v }$ vary, and that it also varies with direction, as represented by the unit vector $\bar { n }$ ; we see this in the terms involving $\bar { n } ^ { j } \bar { n } ^ { k } \partial _ { \bar { \jmath } \bar { k } } \hat { X } _ { \mathrm { e x t } }$ and $[ ( { \pmb w } + { \pmb v } ) \cdot { \pmb \bar { n } } ] ^ { 2 }$ . There is also a variation with $\bar { r }$ seen in the last two terms.

Our expression for $G _ { \mathrm { e f f } }$ is not an artifact of the coordinate transformation from the inertial frame to the body’s comoving frame. It can be obtained in an invariant manner with an alternative calculation. The gravitational constant is a physically measurable quantity, determined with a Cavendish-type experiment, in which the force between two known masses at a determined separation is measured; Newton’s constant is then the measured coefficient in the expression $F = G m _ { 1 } m _ { 2 } / r ^ { 2 }$ . To be more precise, we imagine a situation in which a body of mass $M$ moves freely through spacetime, while a test body of negligible mass is held at a fixed proper distance $s$ from the source mass by a four-acceleration $a ^ { \mu }$ ; the test body is assumed to be non-rotating relative to the source body. An invariant radial unit vector $e ^ { \mu }$ points from the test body to the source. The gravitational constant is then defined by Newton’s law, which states that $a ^ { \mu } e _ { \mu } = G _ { L } M / s ^ { 2 }$ , where we use the notation $G _ { L }$ to indicate that this is the invariant, locally-measured gravitational constant. A detailed calculation of $G _ { L }$ using the PPN metric and equations of motion reveals that $G _ { L } = G _ { \mathrm { e f f } }$ , as given by Eq. (13.36).

# 13.2.7 Spin dynamics

The methods that were exploited to derive the equations of motion of spinning bodies in general relativity can be carried over to the PPN framework with only a few modifications, which come from the new parameters and the addition of the Whitehead and preferred-frame potentials.

We again define the spin tensor and vector of each body by Eqs. (9.167) and (9.168), and expand all potentials about the center-of-mass of each body, as defined by Eq. (9.3). We keep terms that involve products of $\bar { v } ^ { k }$ with ${ \bar { x } } ^ { j }$ , along with the usual “self-terms” involving $H _ { A } ^ { i j }$ , $\Omega _ { A }$ , and so on. But we discard terms that vanish in the limit in which the size of each body tends to zero. The integrals of Eqs. (9.192) and (9.193) carry over to this calculation, with the caveat that some coefficients in the expressions must be replaced with their PPN counterparts. We also have to calculate the spin contributions to the preferred-frame terms in Eq. (13.12); these are given by

$$
c ^ { 2 } \Delta F _ { \mathrm { P F } } ^ { j } = - \frac { 1 } { 4 } \alpha _ { 1 } w ^ { k } S _ { A } ^ { l k } \partial _ { j l } U _ { - A } + \frac { 1 } { 2 } ( 2 \alpha _ { 3 } - \alpha _ { 1 } ) M _ { A } w ^ { k } \partial _ { k } U _ { - A } ^ { j } .
$$

The Whitehead potential makes no spin contribution to the equations of motion, because it is independent of velocity.

Collecting results, we find that the PPN spin–orbit and spin–spin accelerations are given by

$$
\begin{array} { l } { { \displaystyle { a _ { \mathcal { A } } ^ { \prime } [ 8 0 ] = \frac { 3 } { 2 \sigma ^ { 2 } } \sum _ { \nu \neq i } \frac { G M _ { \beta } } { \nu ^ { 3 } } \left\{ n _ { \mathcal { A } \kappa } ^ { 3 } \left[ v _ { i } ^ { \nu } \left( ( 2 \gamma + 1 ) \hat { S } _ { \mathcal { A } } ^ { \nu \mu } + ( 2 \gamma + 2 ) \hat { S } _ { \mathcal { B } } ^ { \nu \mu } \right) \right. \right. } } } \\ { { \displaystyle \left. \qquad - v _ { \beta } ^ { \nu } \left( ( 2 \gamma + 1 ) \hat { S } _ { \mathcal { A } } ^ { \nu \mu } + ( 2 \gamma + 2 ) \hat { S } _ { \mathcal { A } } ^ { \nu \mu } \right) \right] } } \\ { { \displaystyle \qquad + n _ { \mathcal { A } } ^ { \nu \beta } ( v _ { \mathcal { A } } - v _ { \mathcal { B } } ) ^ { \nu } \left( ( 2 \gamma + 1 ) \hat { S } _ { \mathcal { A } } ^ { \nu \mu } + ( 2 \gamma + 2 ) \hat { S } _ { \mathcal { B } } ^ { \nu \beta } \right) } } \\ { { \displaystyle \left. \qquad + \frac { 1 } { 2 } \alpha n _ { \mathcal { A } } \hat { \nu } _ { \mathcal { A } } ^ { \mathrm { ( i f f ) } } \left( w + v _ { \mathcal { A } } \right) ^ { \nu } \hat { S } _ { \mathcal { B } } ^ { \nu \mu } - ( w + v _ { \mathcal { B } } ) ^ { \nu } \hat { S } _ { \mathcal { A } } ^ { \nu \mu } \right) } } \\ { { \displaystyle \qquad + \frac { 1 } { 2 } \alpha n _ { \mathcal { A } } \eta _ { \mathcal { A } } ^ { \mu \nu } ( v _ { \mathcal { A } } - v _ { \mathcal { A } } ) ^ { \nu } \hat { S } _ { \mathcal { B } } ^ { \nu \mu } - \alpha , v _ { \mathcal { A } } ^ { ( i f ) } ( w + v _ { \mathcal { B } } ) ^ { \nu } \hat { S } _ { \mathcal { B } } ^ { \nu \mu } \Bigg \} } , } \\   \displaystyle  a _ { \mathcal { A } } ^ { \prime } [ 8 s ] = - \frac { 1 5 } { 8 \epsilon ^ { 2 } } ( 4 \gamma + 4 + \alpha _ { 1 } ) \sum _ { \nu \neq i } \frac { G M _ { \mathcal { A } } } { \nu ^ { 4 } } \hat { S } _ { \mathcal { A } } ^ { \nu \mu } \hat { S } _   \end{array}
$$

where $\hat { S } _ { A } ^ { j k } : = S _ { A } ^ { j k } / M _ { A }$ and $M _ { A }$ is the total mass-energy of body $A$ . Comparing with Eqs. (9.189) and (9.190), we see that the coefficients of 3 and 4 in the spin–orbit terms have been replaced by $( 2 \gamma + 1 )$ and $( 2 \gamma + 2 )$ , respectively, and that the spin–spin term is now modulated by the factor $\textstyle { \frac { 1 } { 8 } } ( 4 \gamma + 4 + \alpha _ { 1 } )$ . The terms involving the preferred-frame parameters $\alpha _ { 1 }$ and $\alpha _ { 3 }$ depend either on the combinations ${ \pmb w } + { \pmb v } _ { A }$ or ${ \pmb w } + { \pmb v } _ { B }$ , or on the difference ${ \pmb v } _ { A } - { \pmb v } _ { B }$ , showing that all velocities are measured relative to the preferred universal frame or to each other; once more we find that the arbitrary velocity of the PPN frame is irrelevant.

In the same manner we can derive the PPN equations for the evolution of each spin vector. We begin with the general form of Eq. (9.203),

$$
\frac { d S _ { A } ^ { j } } { d t } = \frac { 1 } { c ^ { 2 } } \epsilon ^ { j p q } \sum _ { i = 1 } ^ { 1 1 } G _ { n } ^ { p q } + { \cal O } ( c ^ { - 4 } ) ,
$$

and for $n$ ranging from 1 to 9 we can import $G _ { n } ^ { p q }$ directly from Eqs. (9.205), with the appropriate insertion of PPN parameters. A tenth contribution, from the Whitehead potential, is found most simply by adopting the second form displayed in Box 13.1,

$$
\Phi _ { W } = - U ^ { 2 } - \Phi _ { 2 } - \nabla U \cdot \nabla X + G \nabla \cdot \int { \frac { \rho ^ { * / } } { | { \boldsymbol { x } } - { \boldsymbol { x } } ^ { \prime } | } } \nabla ^ { \prime } X ^ { \prime } d ^ { 3 } x ^ { \prime } .
$$

After some tedious calculations we arrive at

$$
\begin{array} { l } { { \displaystyle c ^ { 2 } G _ { 1 0 } ^ { j k } = \xi \frac { d } { d t } \int _ { A } \rho ^ { * } \big ( \bar { x } ^ { j } \bar { v } ^ { l } \partial _ { k l } \bar { X } _ { A } + \bar { v } ^ { j } \partial _ { k } \bar { X } _ { A } \big ) d ^ { 3 } \bar { x } - 2 \xi \int _ { A } p \bar { x } ^ { j } \partial _ { k } \bar { U } _ { A } d ^ { 3 } \bar { x } } } \\ { { \displaystyle ~ - \xi \int _ { A } \rho ^ { * } \big ( \bar { v } ^ { j } \partial _ { t k } \bar { X } _ { A } + 2 \bar { v } ^ { j } \bar { v } ^ { l } \partial _ { k l } \bar { X } _ { A } + \bar { x } ^ { j } \bar { v } ^ { l } \partial _ { t k l } \bar { X } _ { A } + \bar { x } ^ { j } \bar { v } ^ { l } \bar { v } ^ { m } \partial _ { k l m } \bar { X } _ { A } \big ) d ^ { 3 } \bar { x } ~ } } \\ { { \displaystyle ~ + 2 \xi \Omega _ { A } ^ { j l } \partial _ { k l } X _ { - A } . } } \end{array}
$$

The eleventh and final contribution comes from the preferred-frame terms in Eq. (13.8). Collecting results, we find three classes of terms, those that involve integrals over the variables of body $A$ only, those that involve $\Omega _ { A }$ and external variables such as ${ \pmb v } _ { A }$ , and spin terms. Most, but not all, of the self-terms can be manipulated to obtain a total time derivative, with the result

$$
\begin{array} { r l r } {  { ( \frac { d S _ { \cal A } ^ { j } } { d t } ) _ { \mathrm { s e l f } } = - \epsilon ^ { j p q } \frac { 1 } { c ^ { 2 } } \frac { d } { d t } \int _ { \cal A } \rho ^ { * } \bar { x } ^ { p } \biggl [ \bar { v } ^ { q } ( \frac { 1 } { 2 } \bar { v } ^ { 2 } + ( 2 \gamma + 1 ) U _ { \cal A } + \Pi + \frac { p } { \rho ^ { * } } ) } } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) U _ { \cal A } ^ { q } - \frac { 1 } { 2 } ( 1 + \alpha _ { 2 } ) \partial _ { t q } X _ { \cal A } \biggr ] d ^ { 3 } \bar { x } } \\ & { } & { \quad \quad \quad \quad \quad + \epsilon ^ { j p q } \frac { 1 } { c ^ { 2 } } \int _ { \cal A } \rho ^ { * } \bar { x } ^ { p } \biggl [ \frac { 1 } { 2 } \alpha _ { 3 } \partial _ { q } \Phi _ { 1 \cal A } + \zeta _ { 2 } \partial _ { q } \Phi _ { 2 \cal A } + \zeta _ { 3 } \partial _ { q } \Phi _ { 3 \cal A } } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad + ( 3 \zeta _ { 4 } - \zeta _ { 1 } ) \partial _ { q } \Phi _ { 4 \cal A } + \frac { 1 } { 2 } \zeta _ { 1 } \partial _ { q } \Phi _ { 5 \cal A } \biggr ] d ^ { 3 } \bar { x } . } \end{array}
$$

As before, the total time derivative can be moved to the left-hand side of the spin-evolution equation and absorbed into an internal correction $\Delta _ { \mathrm { i n t } } S _ { A } ^ { j }$ of the spin vector. The remaining terms are present only in non-conservative theories. For a body that is spherically symmetric to a good approximation, the integrals will all be proportional to $\delta ^ { p q }$ , which is killed by the contraction with $\epsilon ^ { j p q }$ . For a stationary axisymmetric body, the only quantities available to construct a two-index tensor are $\delta ^ { p q }$ and $e ^ { p } e ^ { q }$ , where $_ e$ is a unit vector in the direction of the symmetry axis, and these also are killed by a contraction with $\epsilon ^ { j p q }$ . The strange non-conservative precessions are therefore relevant only for rather oddly shaped bodies.

Other spin-evolution terms involve the body’s self-gravitational energy $\Omega _ { A }$ ; they are given by

$$
\left( \frac { d S _ { A } ^ { j } } { d t } \right) _ { \Omega _ { 4 } } = \epsilon ^ { j p q } \frac { 1 } { c ^ { 2 } } \Omega _ { A } ^ { p n } \biggl [ \alpha _ { 2 } ( w + v _ { A } ) ^ { q } ( w + v _ { A } ) ^ { n } - 2 \xi \sum _ { B \ne A } \frac { m _ { B } } { r _ { A B } } n _ { A B } ^ { q n } \biggr ] .
$$

The first term depends on the velocity of body $A$ relative to the preferred frame, and the second term is the contribution from the Whitehead potential. For a spherically symmetric body, both terms are killed by the contraction with $\epsilon ^ { j p q }$ .

Finally, we collect the spin-evolution terms that depend only on the spins. By defining the proper spin $\bar { \pmb S } _ { A }$ according to [compare with Eq. (9.217)]

$$
\bar { S } _ { \it d } : = S _ { \it d } + \Delta _ { \mathrm { e x t } } S _ { \it d } = S _ { \it d } + \frac { 1 } { c ^ { 2 } } \Bigg \{ \Big [ v _ { \it d } ^ { 2 } + ( 2 \gamma + 1 ) U _ {  \it d } \Big ] S _ { \it d } - \frac { 1 } { 2 } ( v _ { \it d } \cdot S _ { \it d } ) v _ { \it d } \Bigg \} ,
$$

we obtain the PPN equation of spin precession,

$$
\frac { d \bar { \pmb S } _ { A } } { d t } = \pmb \Omega _ { A } \times \bar { \pmb S } _ { A } + O ( c ^ { - 4 } ) ,
$$

where

$$
\begin{array} { c } { { \displaystyle \Omega _ { \scriptscriptstyle { \cal A } } = \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { s o } \right] + \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { s s } \right] + \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { p r } \right] , } } \\ { { \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { s o } \right] = \displaystyle \frac { 1 } { 2 c ^ { 2 } } \sum _ { \scriptscriptstyle { \cal B } \neq \cal A } \frac { G M _ { \scriptscriptstyle { \cal B } } } { r _ { \scriptscriptstyle { \cal A } \scriptscriptstyle { \cal B } } ^ { 2 } } n _ { \scriptscriptstyle { \cal A B } } \times \left[ \left( 2 \gamma + 1 \right) { \bf { v } } _ { \scriptscriptstyle { \cal A } } - \left( 2 \gamma + 2 \right) { \bf { v } } _ { \scriptscriptstyle { \cal B } } \right] , } } \\ { { \displaystyle \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { s s } \right] = \displaystyle \frac { 4 \gamma + 4 + \alpha _ { 1 } } { 8 c ^ { 2 } } \sum _ { \scriptscriptstyle { \cal B } \neq \cal A } \frac { G } { r _ { \scriptscriptstyle { \cal A } \scriptscriptstyle { \cal B } } ^ { 3 } } \left[ 3 n _ { \scriptscriptstyle { \cal A B } } \left( n _ { \scriptscriptstyle { \cal A B } } \cdot \bar { \bf S } _ { \scriptscriptstyle { \cal B } } \right) - \bar { \bf S } _ { \scriptscriptstyle { \cal B } } \right] , } } \\ { { \displaystyle \Omega _ { \scriptscriptstyle { \cal A } } \left[ \mathrm { p r } \right] = - \frac { \alpha _ { 1 } } { 4 c ^ { 2 } } \sum _ { \scriptscriptstyle { \cal B } \neq \cal A } \frac { G M _ { \scriptscriptstyle { \cal B } } } { r _ { \scriptscriptstyle { \cal A B } } ^ { 2 } } n _ { \scriptscriptstyle { \cal A B } } \times \left( { \bf w } + { \bf v } _ { \scriptscriptstyle { \cal B } } \right) . } } \end{array}
$$

The spin–orbit and spin–spin pieces of $\pmb { \Omega } _ { A }$ can be compared with Eqs. (9.199); the preferredframe piece is new.

Applying these equations to the Gravity Probe B experiment, we may choose to work in a PPN frame at rest with respect to the Earth, and set ${ \pmb v } _ { B } = 0$ . Comparing Eqs. (13.46) with Eqs. (9.199), we can see that the spin–orbit precession is proportional to the PPN coefficient $\textstyle { \frac { 1 } { 3 } } ( 2 \gamma + 1 )$ , while the spin–spin precession is proportional to $\frac { 1 } { 8 } ( 4 \gamma + 4 + \alpha _ { 1 } )$ . The implications for an experiment like Gravity Probe B can be explored by reviewing the discussion of Sec. 10.4.1. The preferred-frame precession produces a purely periodic motion of the gyroscopes that is too small to be detected.

# 13.3 Experimental tests of gravitational theories

# 13.3.1 Two-body problem and pericenter advance

We now specialize the PPN equations of motion obtained in Sec. 13.2.4 to a system of two bodies, such as the Sun–Mercury system or a binary-star system. To keep things simple we drop the preferred-frame terms from the equations of motion; these can be studied separately, as we shall do in Sec. 13.3.4. We include the structure dependence on the passive and active gravitational masses, assuming the bodies to be spherically symmetric. With these simplifications, the equations of motion for the first body become

$$
\begin{array} { l } { { \displaystyle { \pmb a } _ { 1 } = - \bigg ( \frac { M _ { \mathcal { P } } } { M } \bigg ) _ { 1 } \frac { G ( M _ { \mathcal { A } } ) _ { 2 } } { r ^ { 2 } } { \pmb n } } } \\ { { \displaystyle ~ + \frac { 1 } { c ^ { 2 } } \left[ - \frac { G M _ { 2 } } { r ^ { 2 } } \bigg [ \gamma v _ { 1 } ^ { 2 } - \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) ( { \pmb v } _ { 1 } \cdot { \pmb v } _ { 2 } ) \right. } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { c c } { { } } & { { + \displaystyle \frac { 1 } { 2 } ( 2 \gamma + 2 + \alpha _ { 2 } + \alpha _ { 3 } ) v _ { 2 } ^ { 2 } - \frac { 3 } { 2 } ( 1 + \alpha _ { 2 } ) ( n \cdot v _ { 2 } ) ^ { 2 } } } \\ { { } } & { { - \left( 2 \gamma + 2 \beta + 1 + \displaystyle \frac { 1 } { 2 } \alpha _ { 1 } - \zeta _ { 2 } \right) \displaystyle \frac { G M _ { 1 } } { r } - ( 2 \gamma + 2 \beta ) \displaystyle \frac { G M _ { 2 } } { r } \Bigg ] n } } \\ { { } } & { { + \displaystyle \frac { G M _ { 2 } } { r ^ { 2 } } \left\{ n \cdot \left[ ( 2 \gamma + 2 ) v _ { 1 } - ( 2 \gamma + 1 ) v _ { 2 } \right] \right\} v _ { 1 } } } \\ { { } } & { { - \displaystyle \frac { 1 } { 2 } \displaystyle \frac { G M _ { 2 } } { r ^ { 2 } } \left\{ n \cdot \left[ ( 4 \gamma + 4 + \alpha _ { 1 } ) v _ { 1 } - ( 4 \gamma + 2 + \alpha _ { 1 } - 2 \alpha _ { 2 } ) v _ { 2 } \right] \right\} v _ { 2 } \Bigg ] } } \\ { { } } & { { } } \\ { { + \displaystyle O ( c ^ { - 4 } ) , } } & { { ( 1 3 . 4 ! } } \end{array}
$$

where $r : = r _ { 1 } - r _ { 2 }$ , $r : = | r | , ~ \pmb { n } : = \pmb { r } / r$ , and $M _ { \mathcal { P } }$ , $M _ { A }$ for each body are given by Eqs. (13.30). The equations of motion for the second body are obtained by interchanging the variables according to $M _ { 1 }  M _ { 2 }$ , ${ \pmb v } _ { 1 }  { \pmb v } _ { 2 }$ , and $n  - n$ .

We wish to convert the equations of motion into an effective one-body problem, as we did back in Sec. 9.3.7. We have to be careful when we are not working with a conservative theory of gravity, because the system’s barycenter will not necessarily be at rest or move uniformly. But this failure occurs at post-Newtonian order, and since we need to relate ${ \pmb v } _ { 1 }$ and ${ \pmb v } _ { 2 }$ to the relative velocity $\pmb { v }$ in 1pn terms only, the non-conservative effects are beyond our order of approximation. We can therefore choose our PPN coordinate system so that the barycenter is approximately at rest – we set $M _ { 1 } \pmb { v } _ { 1 } + M _ { 2 } \pmb { v } _ { 2 } = O ( c ^ { - 2 } )$ . Defining $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ and $m : = { M } _ { 1 } + { M } _ { 2 }$ , we can to sufficient accuracy replace ${ \pmb v } _ { 1 }$ and ${ \pmb v } _ { 2 }$ in the 1pn terms by the relations

$$
{ \pmb v } _ { 1 } = \frac { M _ { 2 } } { m } { \pmb v } + O ( c ^ { - 2 } ) , \qquad { \pmb v } _ { 2 } = - \frac { M _ { 1 } } { m } { \pmb v } + O ( c ^ { - 2 } ) ,
$$

and obtain an expression for the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ . We find

$$
\begin{array} { c } { { a = \displaystyle - \frac { G m ^ { * } } { r ^ { 2 } } n - \frac { G m } { r ^ { 2 } c ^ { 2 } } \bigg \{ \bigg [ \Big ( \gamma + \frac { 1 } { 2 } \eta [ 6 + \alpha _ { 1 } + \alpha _ { 2 } + \alpha _ { 3 } ] \Big ) v ^ { 2 } } } \\ { { - \frac { 3 } { 2 } \eta ( 1 + \alpha _ { 2 } ) ( n \cdot v ) ^ { 2 } - \big ( 2 \gamma + 2 \beta + \eta [ 2 + \alpha _ { 1 } - 2 \zeta _ { 2 } ] \big ) \frac { G m } { r } \bigg ] n } } \\ { { - \big ( 2 \gamma + 2 - \eta [ 2 - \alpha _ { 1 } - \alpha _ { 2 } ] \big ) ( n \cdot v ) v \bigg \} + { \cal O } ( c ^ { - 4 } ) , \qquad ( 1 3 . 4 9 \times \alpha ^ { - 1 } ) . } } \end{array}
$$

where $\eta : = { M _ { 1 } M _ { 2 } } / { m ^ { 2 } }$ and

$$
\begin{array} { r l } & { m ^ { * } : = \left( \cfrac { M _ { \mathcal { P } } } { M } \right) _ { 1 } ( M _ { \cal A } ) _ { 2 } + \left( \cfrac { M _ { \mathcal { P } } } { M } \right) _ { 2 } ( M _ { \cal A } ) _ { 1 } } \\ & { \quad = m + O ( c ^ { - 2 } ) \times \left[ \mathrm { s t r u c t u r e - d e p e n d e n t ~ t e r m s } \right] . } \end{array}
$$

Note that it is $m ^ { * }$ that now plays the role of the Kepler-measured mass of the two-body system; because it differs from $m$ by 1pn corrections, we can replace $m$ by $m ^ { * }$ in all 1pn terms. The bottom line is that the structure-dependent effects are unmeasurable in a two-body system. We can therefore drop the distinction between $m ^ { * }$ and $m$ , and express a entirely in terms of $m$ . Equation (13.49) then has exactly the same form as Eq. (10.1), except for the numerical coefficients in front of each term.

We next involve the acceleration of Eq. (13.49) in a calculation of the orbital motion. We adopt the methods of Sec. 10.1.3: the post-Newtonian terms in the acceleration are collected into a perturbing force $f$ , and the motion is described using the formalism of osculating orbital elements. We shall not go into the details here, but simply state that over a complete orbital period, the only orbital element that undergoes a net change is the longitude of pericenter $\omega$ . The PPN equations of motion imply that it advances by

$$
\Delta \omega = \frac { 6 \pi G m } { p c ^ { 2 } } \bigg [ \frac { 1 } { 3 } ( 2 + 2 \gamma - \beta ) + \frac { 1 } { 6 } ( 2 \alpha _ { 1 } - \alpha _ { 2 } + \alpha _ { 3 } + 2 \zeta _ { 2 } ) \eta \bigg ]
$$

in the course of each orbit. Because the perturbing force involves terms proportional to either $\pmb { n }$ or $\pmb { v }$ , the orientation of the orbital plane is unaffected by the perturbation. The second term in Eq. (13.51) vanishes in any fully conservative theory of gravity $\left( \alpha _ { n } = \zeta _ { 2 } = 0 \right.$ ). It is also negligible in the case of Mercury orbiting the Sun, because $\eta \simeq 2 \times 1 0 ^ { - 7 }$ . The predicted PPN perihelion advance of Mercury is therefore

$$
\left( \frac { d \omega } { d t } \right) _ { \mathrm { s e c } } = 4 2 . 9 8 \bigg [ \frac { 1 } { 3 } ( 2 + 2 \gamma - \beta ) \bigg ] \mathrm { a s / c e n t u r y } .
$$

As we saw back in Sec. 10.1.4, the advance of Mercury’s perihelion beyond what can be explained by planetary perturbations is 42.98 arcseconds per century, accurate to about one part in $1 0 ^ { 3 }$ . Data from helioseismology have shown that the complicating effect of a solar quadrupole moment is an order of magnitude smaller than the observational error (refer to Sec. 3.4.3). Combining these data with the bound on $\gamma$ obtained below in Sec. 13.3.2 – it must be equal to unity at the level of parts in $1 0 ^ { 5 }$ – we see that $\beta$ must be equal to unity to about 3 parts in $1 0 ^ { 3 }$ .

# 13.3.2 Light deflection and Shapiro time delay

As we saw back in Sec. 13.2.5, the propagation of light in the PPN framework is the same as in general relativity, except that the overall magnitude of any post-Newtonian effect is proportional to the factor $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ . The deflection of a photon by a body of mass $M$ is therefore described by the vector

$$
\pmb { \alpha } ( t ) = - \biggl ( \frac { 1 + \gamma } { 2 } \biggr ) \frac { 4 G M } { c ^ { 2 } } \frac { \pmb { b } } { b ^ { 2 } } \frac { 1 + \cos \Phi ( t ) } { 2 } ,
$$

which is imported directly from Eq. (10.66). Here $\pmb { b }$ is a vector that points from the body to the photon’s point of closest approach, $b : = | \pmb { b } |$ is the impact parameter, and $\Phi ( t )$ is the angle between the photon’s current position and its initial direction (see Fig. 10.1). The total deflection angle at $t \to \infty$ is then

$$
\alpha = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 4 G M } { c ^ { 2 } b } ,
$$

and evaluating this for the Sun gives

$$
\alpha = 1 . 7 5 0 4 \bigg ( \frac { 1 + \gamma } { 2 } \bigg ) \frac { R _ { \odot } } { b } \mathrm { a s } .
$$

These results can be compared with Eq. (10.68).

The PPN expressions for the light deflection complement our discussion of the “Newtonian deflection” in Box 10.3. In the factor $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ , the $^ { 6 6 } 1 / 2 ^ { , 3 }$ piece comes from $g _ { 0 0 }$ , the Newtonian part of the metric, and this corresponds to the Newtonian deflection. The $^ { * } \gamma / 2 ^ { , * }$ piece comes from $g _ { j k }$ , and this reflects the impact of spatial curvature, which bends locally straight lines (spatial geodesics) near the Sun relative to locally straight lines far from the Sun. The total deflection is the sum of these two effects. Only the part resulting from the spatial curvature can vary from one metric theory to another. It is entirely coincidental that the two parts happen to be equal in general relativity.

The expression for the Shapiro time delay is altered from Eq. (10.100) by the same overall factor. The propagation time of a light signal between an emitter at position $r _ { e }$ and an observer at position $r _ { \mathrm { o b s } }$ is therefore given by

$$
t _ { \mathrm { o b s } } - t _ { e } = \frac { 1 } { c } | \boldsymbol { r } _ { \mathrm { o b s } } - \boldsymbol { r } _ { e } | + \left( \frac { 1 + \gamma } { 2 } \right) \frac { 2 G M } { c ^ { 3 } } \ln \left[ \frac { ( \boldsymbol { r } _ { \mathrm { o b s } } + \boldsymbol { r } _ { \mathrm { o b s } } \cdot \boldsymbol { k } ) ( \boldsymbol { r } _ { e } - \boldsymbol { r } _ { e } \cdot \boldsymbol { k } ) } { b ^ { 2 } } \right] ,
$$

where $\pmb { k }$ is the initial direction of the light signal. We can use high-precision measurements of the deflection of light and Shapiro time delay to place bounds on the parameter $\gamma$ . These experiments were described in Secs. 10.2.3 and 10.2.5. The best current limit, obtained from Doppler tracking measurements of the Cassini spacecraft, is $| \gamma - 1 | < 4 \times 1 0 ^ { - 5 }$ , in excellent agreement with general relativity.

Gravitational lensing also scales by the $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ factor. Because of the large uncertainties in the gravitational potential of the lensing galaxies and clusters, it is more useful to exploit the high-precision bounds on $\gamma$ from solar-system measurements to turn lensing into a tool for mapping the gravitational potential, and thus for mapping the distribution of dark matter in and around galaxies and clusters. One remarkable test of $\gamma$ on galactic scales was nevertheless reported in 2006. This interesting measurement used data on gravitational lensing by 15 elliptical galaxies, collected by the Sloan Digital Sky Survey. The Newtonian potential $U$ of each lensing galaxy (including the contribution from dark matter) could be determined using a Newtonian model derived from the observed velocity dispersion of stars in the galaxy, essentially exploiting the virial theorem which relates $v ^ { 2 }$ to $U$ . Comparing the observations with the lensing predicted by the models provided a 10 percent bound on $\gamma$ , in agreement with general relativity. Unlike the much tighter bound described previously, which was obtained on the scale of the solar system, this bound was obtained on a galactic scale.

# 13.3.3 Tests of the strong equivalence principle: Nordtvedt effect

We have seen that the structure-dependent contributions to the active and passive masses of a body are unobservable in a two-body system. They are, however, observable in a three-body system, and the corresponding effect, known as the Nordtvedt effect, has given rise to an important test of general relativity.

Working at the level of Newtonian gravity, but allowing the inertial, passive, and active masses of bodies to be different from each other, we write down the equations of motion of a two-body system in the presence of a third body [refer to Eqs. (3.73) and (3.74) for a strictly Newtonian formulation],

$$
\begin{array} { r } { \pmb { a } _ { 1 } = - \left( \frac { M _ { P } } { M } \right) _ { 1 } \left[ G ( M _ { \mathcal { A } } ) _ { 2 } \frac { \pmb { r } _ { 1 2 } } { r _ { 1 2 } ^ { 3 } } + G ( M _ { \mathcal { A } } ) _ { 3 } \frac { \pmb { r } _ { 1 3 } } { r _ { 1 3 } ^ { 3 } } \right] , } \\ { \pmb { a } _ { 2 } = \left( \frac { M _ { P } } { M } \right) _ { 2 } \left[ G ( M _ { \mathcal { A } } ) _ { 1 } \frac { \pmb { r } _ { 1 2 } } { r _ { 1 2 } ^ { 3 } } - G ( M _ { \mathcal { A } } ) _ { 3 } \frac { \pmb { r } _ { 2 3 } } { r _ { 2 3 } ^ { 3 } } \right] . } \end{array}
$$

We denote the barycentric position of the two-body system by

$$
\pmb { r } _ { c } : = \frac { M _ { 1 } } { m } \pmb { r } _ { 1 } + \frac { M _ { 2 } } { m } \pmb { r } _ { 2 } ,
$$

where $m : = { M } _ { 1 } + { M } _ { 2 }$ , and assuming that $r _ { 1 2 } \ll r _ { 2 3 }$ , we expand

$$
\frac { r _ { 1 3 } ^ { j } } { r _ { 1 3 } ^ { 3 } } = \frac { r _ { c 3 } ^ { j } } { r _ { c 3 } ^ { 3 } } - \sum _ { \ell = 1 } ^ { \infty } \frac { 1 } { \ell ! } r _ { 1 c } ^ { L } \partial ^ { \langle j L \rangle } \left( \frac { 1 } { r _ { c 3 } } \right) ,
$$

where $\pmb { r } _ { c 3 } : = \pmb { r } _ { c } - \pmb { r } _ { 3 }$ and $\pmb { r } _ { 1 c } : = \pmb { r } _ { 1 } - \pmb { r } _ { c }$ ; we develop a similar expansion for $r _ { 2 3 } ^ { j } / r _ { 2 3 } ^ { 3 }$ . We define $R : = r _ { c 3 } = | r _ { c 3 } |$ ${ \mathrm { \Omega } } _ { \ast 3 } = \vert r _ { c 3 } \vert , N : = { r } _ { c 3 } / { r _ { c 3 } } , r _ { 1 c } : = \vert r _ { 1 c } \vert , { n _ { 1 c } } : = { r } _ { 1 c } / { r _ { 1 c } } , { r _ { 2 c } } : = \vert r _ { 2 c } \vert , { n _ { 2 c } }$ $\mathbf { \nabla } _ { \pmb { n } _ { 2 c } } : =$ $r _ { 2 c } / r _ { 2 c }$ , and note that

$$
r _ { 1 c } = ( M _ { 2 } / m ) r , \qquad r _ { 2 c } = - ( M _ { 1 } / m ) r , \qquad n _ { 1 c } = - n _ { 2 c } = n ,
$$

where $r : = | r _ { 1 2 } |$ and $\pmb { n } : = \pmb { r } _ { 1 2 } / r _ { 1 2 }$ . With this notation we find that the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ is given by

$$
\begin{array} { c } { { a ^ { j } = - \displaystyle \frac { G m ^ { * } } { r ^ { 2 } } n ^ { j } - \displaystyle \frac { G M _ { 3 } } { R ^ { 2 } } N ^ { j } \left[ \left( \displaystyle \frac { M _ { \mathcal { P } } } { M } \right) _ { 1 } - \left( \displaystyle \frac { M _ { \mathcal { P } } } { M } \right) _ { 2 } \right] } } \\ { { - \displaystyle \frac { G M _ { 3 } } { R ^ { 2 } } \sum _ { \ell = 1 } ^ { \infty } \displaystyle \frac { ( - 1 ) ^ { \ell } ( 2 \ell + 1 ) ! ! } { \ell ! } \left( \displaystyle \frac { r } { R } \right) ^ { \ell } n ^ { L } N ^ { \ell j L } } } \\ { { \times \left[ \left( \displaystyle \frac { M _ { \mathcal { P } } } { M } \right) _ { 1 } \left( \displaystyle \frac { M _ { 2 } } { M } \right) ^ { \ell } - ( - 1 ) ^ { \ell } \left( \displaystyle \frac { M _ { \mathcal { P } } } { M } \right) _ { 2 } \left( \displaystyle \frac { M _ { 1 } } { M } \right) ^ { \ell } \right] , } } \end{array}
$$

where $m ^ { * }$ is defined by Eq. (13.50), and we have dropped the $\mathcal { A }$ subscript on $M _ { 3 }$ . Introducing now

$$
\begin{array} { c l c r } { { \alpha : = \displaystyle \frac { 1 } { 2 } \left[ \left( \frac { M _ { P } } { M } \right) _ { 1 } + \left( \frac { M _ { P } } { M } \right) _ { 2 } \right] , } } \\ { { \delta : = \left[ \left( \frac { M _ { P } } { M } \right) _ { 1 } - \left( \frac { M _ { P } } { M } \right) _ { 2 } \right] , } } \end{array}
$$

and keeping terms only through $\ell = 2$ in Eq. (13.61), we obtain

$$
\begin{array} { c } { { a ^ { j } = \displaystyle - \frac { G m ^ { * } } { r ^ { 2 } } n ^ { j } - \delta \frac { G M _ { 3 } } { R ^ { 2 } } N ^ { j } + 3 \alpha \frac { G M _ { 3 } r } { R ^ { 3 } } n ^ { k } N ^ { \langle j k \rangle } - \frac { 1 5 } { 2 } \alpha \Delta \frac { G M _ { 3 } r ^ { 2 } } { R ^ { 4 } } n ^ { p q } N ^ { \langle j p q \rangle } } } \\ { { + \displaystyle \frac { 3 } { 2 } \delta \Delta \frac { G M _ { 3 } r } { R ^ { 3 } } n ^ { k } N ^ { \langle j k \rangle } - \frac { 1 5 } { 4 } \delta ( 1 - 2 \eta ) \frac { G M _ { 3 } r ^ { 2 } } { R ^ { 4 } } n ^ { p q } N ^ { \langle j p q \rangle } , } } \end{array}
$$

where $\Delta : = ( M _ { 1 } - M _ { 2 } ) / ( M _ { 1 } + M _ { 2 } )$ and $\eta : = { M _ { 1 } M _ { 2 } } / { ( M _ { 1 } + M _ { 2 } ) }$ . The first term in Eq. (13.63) is the standard Newtonian acceleration; as we saw previously, the fact that $m ^ { * }$ incorporates structure-dependent corrections is irrelevant since it is $m ^ { * }$ that represents the Kepler-measured mass of the two-body system. The second term is a relative acceleration that stretches or shrinks the orbit along a line directed toward the third body. Whether the stretching occurs when $\pmb { n }$ is parallel or antiparallel to $N$ depends on the sign of δ. From Eq. (13.30a) we have that

$$
\delta = \left( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } \right) \left( \frac { \Omega _ { 1 } } { M _ { 1 } c ^ { 2 } } - \frac { \Omega _ { 2 } } { M _ { 2 } c ^ { 2 } } \right) ,
$$

from which we conclude that the sign of $\delta$ depends on the PPN parameters and the sign of the difference between gravitational binding energies. The third and fourth terms originate from the tidal interactions with the third body; note that $\alpha = 1 + O ( \Omega _ { A } / M _ { A } c ^ { 2 } )$ . The final two terms are corrections to these tidal perturbations that result from a non-zero $\delta$ .

We apply the equations of motion to the Earth–Moon system, with the Sun making up the third body. We set $M _ { 1 } = M _ { \oplus }$ , $M _ { 2 } = M$ , $M _ { 3 } = M _ { \odot }$ , and we first estimate the size of the various terms in the equations of motion. We recall that $G m ^ { * } / r ^ { 3 } \approx M _ { \oplus } / r ^ { 3 } \approx \omega _ { \oplus } ^ { 2 }$ and $G M _ { \odot } / R ^ { 3 } \approx \omega _ { \odot } ^ { 2 }$ , where $\omega _ { \oplus }$ is the angular velocity of the Moon around the Earth, and $\omega _ { \odot }$ is the angular velocity of the Earth around the Sun, with $\omega _ { \oplus } / \omega _ { \odot } \approx 1 3 . 4$ . We also have

$$
\begin{array} { r } { \frac { \Omega _ { \oplus } } { M _ { \oplus } c ^ { 2 } } = - 4 . 6 \times 1 0 ^ { - 1 0 } , } \\ { \frac { \Omega } { M c ^ { 2 } } = - 0 . 2 \times 1 0 ^ { - 1 0 } , } \end{array}
$$

and $R / r \approx 3 9 5$ . As a consequence of these numerical relations, we find that the second term in Eq. (13.63) is smaller than the first by a factor of $( \omega _ { \odot } / \omega _ { \oplus } ) ^ { 2 } ( R / r ) \delta \sim 1 0 ^ { - 1 0 }$ . The next two terms are smaller than the first by factors $( \omega _ { \odot } / \omega _ { \oplus } ) ^ { 2 } \sim ( 1 / 1 3 . 4 ) ^ { 2 } \sim 5 \times 1 0 ^ { - 3 }$ and $( \omega _ { \odot } / \omega _ { \oplus } ) ^ { 2 } ( r / R ) \sim 1 . 4 \times 1 0 ^ { - 5 }$ . And the final two terms are smaller than these by an additional factor of $1 0 ^ { - 1 0 }$ . Dropping these final terms and setting $\alpha = 1$ , the equations of motion for the Earth–Moon system reduce to

$$
\begin{array} { c } { { { \pmb a } = - \displaystyle \frac { G m ^ { * } } { r ^ { 2 } } { \pmb n } - \delta \displaystyle \frac { G M _ { 3 } } { R ^ { 2 } } N + \displaystyle \frac { G M _ { 3 } r } { R ^ { 3 } } \big [ 3 N ( N \cdot n ) - n \big ] } } \\ { { - \displaystyle \frac { 3 } { 2 } \displaystyle \frac { G M _ { 3 } r ^ { 2 } } { R ^ { 4 } } \Delta \big [ 5 N ( N \cdot n ) ^ { 2 } - 2 { \pmb n } ( N \cdot n ) - N \big ] . } } \end{array}
$$

The second term, proportional to $\delta$ , is a structure-dependent contribution to the acceleration, and it is this term that gives rise to the Nordtvedt effect. The remaining terms originate from the tidal interactions with the Sun, and they give rise to orbital perturbations that are actually larger than the Nordtvedt effect.

To analyze the violation of the strong equivalence principle on the lunar orbit, we consider a simplified situation in which the Moon–Earth and Earth–Sun orbits lie in the same plane (their actual relative inclination is about 5 degrees), and are approximately circular (the eccentricity of the Moon–Earth orbit is 0.055, and the eccentricity of the Earth–Sun orbit is 0.017). We calculate the first-order perturbations of the lunar orbit created by the last three terms in Eq. (13.66). In the limit of small eccentricity, we can write $d \phi / d t = \omega _ { \oplus } = { \it \Omega }$ constant, so that

$$
\begin{array} { r l } & { r = a ( 1 - e \cos f ) + O ( e ^ { 2 } ) , } \\ & { f = \phi - \omega = \omega _ { \oplus } t - \omega + O ( e ) , } \\ & { n = e _ { X } \cos ( \omega _ { \oplus } t ) + e _ { Y } \sin ( \omega _ { \oplus } t ) + O ( e ) , } \\ & { \lambda = - e _ { X } \sin ( \omega _ { \oplus } t ) + e _ { Y } \cos ( \omega _ { \oplus } t ) + O ( e ) , } \\ & { N = e _ { X } \cos ( \omega _ { \odot } t - \Phi ) + e _ { Y } \sin ( \omega _ { \odot } t - \Phi ) , } \end{array}
$$

in which $e$ is the eccentricity of the lunar orbit, and $\Phi$ is the initial phase of the Earth’s orbit around the Sun, which we take to be perfectly circular. Note that

$$
\begin{array} { r c l } { { } } & { { } } & { { \pmb { n } \cdot N = \cos ( \Lambda t + \Phi ) , } } \\ { { } } & { { } } & { { \lambda \cdot N = - \sin ( \Lambda t + \Phi ) , } } \end{array}
$$

where $\Lambda : = \omega _ { \oplus } - \omega _ { \odot }$ is the synodic frequency, the angular frequency of the lunar orbit relative to the Sun. This is to be distinguished from the sidereal frequency $\omega _ { \oplus }$ , which refers to the barycentric frame.

We wish to involve $\pmb { f } : = \pmb { a } + G m ^ { * } \pmb { n } / r ^ { 2 }$ in a perturbative calculation of the orbital motion, making use of the formalism of osculating orbital elements reviewed in Sec. 3.3.2. The formalism must be applied with some care, because the orbital eccentricity is small, and $\omega$ loses its meaning when $e \to 0$ . In such cases it is best to use the alternative variables $A : = e \cos \omega$ and $\boldsymbol { B } : = \boldsymbol { e } \sin \omega$ , and to re-express the osculating equations in terms of $A$ and $B$ . We therefore write

$$
r = a \big [ 1 - A \cos ( \omega _ { \oplus } t ) - B \sin ( \omega _ { \oplus } t ) \big ] + O ( e ^ { 2 } ) ,
$$

and convert Eqs. (3.64) to the form

$$
\begin{array} { r l } & { \cfrac { d a } { d t } = \cfrac { 2 } { \omega _ { \oplus } } S + O ( e ) , } \\ & { \cfrac { d A } { d t } = \cfrac { 1 } { \omega _ { \oplus } a } \Big [ \mathcal { R } \sin ( \omega _ { \oplus } t ) + 2 S \cos ( \omega _ { \oplus } t ) \Big ] + O ( e ) , } \\ & { \cfrac { d B } { d t } = \cfrac { 1 } { \omega _ { \oplus } a } \Big [ - \mathcal { R } \cos ( \omega _ { \oplus } t ) + 2 S \sin ( \omega _ { \oplus } t ) \Big ] + O ( e ) , } \end{array}
$$

where $\mathcal { R }$ and $s$ are the radial and tangential components of the perturbing acceleration. To lowest order in $e$ they are given by

$$
\begin{array} { r l r } {  { \mathcal { R } = \omega _ { \odot } ^ { 2 } a \Bigg \{ \big [ 3 \cos ^ { 2 } ( \Lambda t + \Phi ) - 1 \big ] - \frac { 3 } { 2 } \zeta \cos ( \Lambda t + \Phi ) \big [ 5 \cos ^ { 2 } ( \Lambda t + \Phi ) - 3 \big ] } } \\ & { } & \\ & { } & { \qquad - \delta ( R / a ) \cos ( \Lambda t + \Phi ) \Bigg \} , } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad ( 1 3 . 7 \times \omega ) ^ { 2 } \Bigg \{ \frac { \sin ^ { 2 } ( \Lambda t + \Phi ) } { 2 } } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

where $\zeta : = \Delta ( a / R )$ . Because the orbital planes are taken to coincide, there are no perturbations to the inclination $\iota$ or line of nodes $\Omega$ .

Substituting Eqs. (13.71b) into Eqs. (13.70), integrating subject to the boundary conditions $a = a _ { 0 }$ , $A = 0$ , $B = 0$ at $t = 0$ , and inserting the results within Eq. (13.69), we eventually obtain

$$
\begin{array} { r l } & { \delta r ( t ) = a _ { 0 } \left( \frac { \omega _ { \odot } } { \omega _ { \oplus } } \right) ^ { 2 } \Bigg \{ \frac { 3 } { 2 } \frac { \omega _ { \oplus } ^ { 2 } ( 1 + \omega _ { \oplus } / \Lambda ) } { \omega _ { \oplus } ^ { 2 } - 4 \Lambda ^ { 2 } } \cos 2 ( \Lambda t + \Phi ) } \\ & { \hphantom { \frac { \omega _ { \odot } ^ { 2 } ( 1 + \omega _ { \oplus } / \Lambda ) } { 2 } } - \zeta \Bigg [ \frac { 3 } { 8 } \frac { \omega _ { \oplus } ^ { 2 } ( 3 + 2 \omega _ { \oplus } / \Lambda ) } { \omega _ { \oplus } ^ { 2 } - \Lambda ^ { 2 } } \cos ( \Lambda t + \Phi ) } \\ & { \hphantom { \frac { \omega _ { \odot } ^ { 2 } ( 1 + \omega _ { \oplus } / \Lambda ) } { 2 } } + \frac { 5 } { 8 } \frac { \omega _ { \oplus } ^ { 2 } ( 3 + 2 \omega _ { \oplus } / \Lambda ) } { \omega _ { \oplus } ^ { 2 } - 9 \Lambda ^ { 2 } } \cos 3 ( \Lambda t + \Phi ) \Bigg ] } \\ & { \hphantom { \frac { \omega _ { \odot } ^ { 2 } ( 1 + \omega _ { \oplus } / \Lambda ) } { 2 } } - \delta \frac { R } { a _ { 0 } } \frac { \omega _ { \oplus } ^ { 2 } ( 1 + 2 \omega _ { \oplus } / \Lambda ) } { \omega _ { \oplus } ^ { 2 } - \Lambda ^ { 2 } } \cos ( \Lambda t + \Phi ) \Bigg \} } \end{array}
$$

for the perturbation in the Earth–Moon distance. Not surprisingly, because we have a sinusoidal driving force acting on a sinusoidal oscillator, the perturbation takes the form of a resonant response, with denominators of the form $1 / ( \omega _ { \oplus } ^ { 2 } - N ^ { 2 } \Lambda ^ { 2 } )$ , with $N$ representing the harmonic degree. Note that if we had taken the Sun to be fixed in space, with $\omega _ { \odot } = 0$ , then $\Lambda = \omega _ { \oplus }$ and the response of the fundamental harmonic would have produced a linear growth in the semi-major axis. Here the response is strictly harmonic, but because $\omega _ { \odot } = \omega _ { \oplus } / 1 3 . 4$ , the response to the $\cos ( \Lambda t + \Phi )$ harmonic is enhanced by the resonant factor $\omega _ { \oplus } ^ { 2 } / ( \omega _ { \oplus } ^ { 2 } - \Lambda ^ { 2 } ) \approx 7 . 0$ .

Inserting the relevant numbers for the Earth–Moon system, setting $\delta \simeq 4 . 2 \times 1 0 ^ { - 1 0 }$ [refer to Eq. (13.65)], and taking into account the fact that $a _ { 0 } \approx 3 . 8 4 \times 1 0 ^ { 5 } { \mathrm { k m } }$ , we see that the two tidal perturbations and the Nordtvedt effect have approximate amplitudes of $2 7 0 0 \mathrm { k m }$ , $7 3 \mathrm { k m }$ , and 8 meters, respectively. The leading tidal perturbation occurs at twice the synodic frequency $( 2 \Lambda )$ , whereas the Nordtvedt effect occurs at the synodic frequency; the tidal perturbation is much larger, but it can be cleanly separated from the Nordtvedt effect by observing many lunar orbits. The subleading tidal perturbation, however, has contributions at frequencies $\Lambda$ and $3 \Lambda$ , albeit at a much smaller amplitude of $7 3 \ \mathrm { k m }$ . Because this perturbation depends on parameters $( \omega _ { \oplus } , \omega _ { \odot } , R , a _ { 0 } , \Delta )$ that are very accurately measured by other means, it can be predicted in advance to an accuracy well below the amplitude of the Nordtvedt effect.

In fact, an accurate calculation of the relevant amplitudes would require us to go beyond the first-order perturbation analysis carried out here. The perturbations induced by each term affect the behavior of the other terms, and so it is necessary to go to higher order in the orbital perturbation equations, and to include higher values of the multipole index . The problem is that the solar perturbation of the lunar orbit is so large, as seen by the $2 7 0 0 ~ \mathrm { k m }$ leading tidal amplitude, that one must employ more sophisticated techniques, such as the Hill–Brown lunar theory, in order to find a sequence of perturbations that converges in a reasonable way. The final conclusion of such calculations is that the effective amplitude of the Nordtvedt term is increased from the amplitude shown in Eq. (13.72) by a factor approximately equal to $1 + 2 \omega _ { \odot } / \omega _ { \oplus } \simeq 1 . 1 5$ , leading to an amplitude of 9.2 meters. Similarly, the amplitude of the competing synodic term is increased from $7 5 \mathrm { k m }$ to $1 1 0 \mathrm { k m }$ , but it can still be predicted accurately enough to be subtracted from the data.

Inserting the values for $\Omega / ( M c ^ { 2 } )$ for the Earth and Moon, the resulting prediction for the Nordtvedt effect is

$$
\delta r ( t ) \simeq 9 . 2 \eta _ { N } \cos ( \Lambda t + \Phi ) \mathrm { m } ,
$$

where $\eta _ { N }$ is the Nordtvedt parameter

$$
\eta _ { N } : = 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } .
$$

As we explain in Box 13.2, long-term monitoring of the lunar orbit has revealed no sign of a Nordtvedt effect, and $\eta _ { N }$ is currently constrained to be smaller than $4 . 4 \times 1 0 ^ { - 4 }$ . This implies that violations of the strong equivalence principle are very small in the Earth–Moon–Sun system. And this, of course, is compatible with general relativity, which predicts $\eta _ { N } = 0$ .

# Box 13.2

# Lunar laser ranging and the Nordtvedt effect

Lunar laser ranging (LLR) illustrates the importance of new technology and broad theoretical frameworks in the program to test general relativity.

Except for the de Sitter precession of the lunar orbit, described in Sec. 10.1.6, most general relativistic effects on the lunar orbit are so small as to be virtually undetectable. But in the late 1950s, Robert Dicke was thinking beyond Einstein, and he wondered whether one could measure a variation with time of Newton’s constant $G$ , a feature that he would soon incorporate into his own alternative theory of gravity. By the early 1960s, the development of pulsed ruby lasers and the rapid build-up of the lunar space program led him and others to propose making very accurate measurements of the Earth–Moon distance by bouncing laser pulses off specially designed reflectors, to be placed on the lunar surface by either unmanned or manned landers. Such measurements would provide tests of general relativity, but they would also have other important scientific benefits, such as improving our understanding of the Earth–Moon orbit, the librations of the Moon, and even the motions of the Earth-bound laser sources resulting from continental drift.

The theoretical discovery of the Nordtvedt effect added to the science case. The discovery required a broader theoretical framework than general relativity; if the focus had never deviated from general relativity, there would have been no case. The Nordtvedt effect and the possibility that $G$ could vary with time provided specific experimental targets, even if the conventional expectation (though perhaps not Dicke’s) was for the answers to be “zero” in both cases. (As Ken Nordtvedt was fond of saying, zero is as good as any other number.)

The first retroreflector was deployed on the Moon by US astronaut Neil Armstrong on July 21, 1969, and within a month, the first successful acquisition was made of a reflected laser signal. Two other US and two French-built reflectors were subsequently placed on the Moon by US astronauts and Soviet unmanned landers. Strangely, the French reflectors were never detected via laser bounces, until just recently.

Since that time a worldwide network of observatories has made regular measurements of the round-trip travel time to the three US lunar retroreflectors, with accuracies that are routinely at the 50 ps (1 cm) level, and that are approaching 5 ps (1 mm). These measurements are fitted using the method of least-squares to a theoretical model for the lunar motion that takes into account perturbations created by the Sun and the other planets, tidal interactions, and post-Newtonian gravitational effects. The predicted round-trip travel times between retroreflector and telescope also take into account the librations of the Moon, the orientation of the Earth, the location of the observatories, and atmospheric effects on the signal propagation. The Nordtvedt parameter is then estimated in the least-squares fit, along with several other important parameters of the model.

From the first published analyses of LLR data in 1976 to the present, there has been absolutely no evidence, within experimental uncertainty, for the Nordtvedt effect. The best current bound on the Nordtvedt parameter is

$$
\eta _ { N } = ( 4 . 4 \pm 4 . 5 ) \times 1 0 ^ { - 4 } .
$$

This is equivalent to an orbital perturbation $\delta r ( t ) = ( 2 . 8 \pm 4 . 1 ) \mathrm { m m } \cos ( \Lambda t + \Phi )$ , and represents a limit on a possible violation of the strong equivalence principle of about 2 parts in $1 0 ^ { 1 3 }$ .

At this level of precision, however, we cannot regard the results of LLR as a completely “clean” test of the Nordtvedt effect until we consider the possibility of a compensating violation of the weak equivalence principle for the Earth and Moon. This is because the chemical compositions of the Earth and Moon differ: the Earth is richer in the iron group elements, while the Moon is richer in silicates. To address this issue, the Eot-Wash ¨ group at the University of Washington in Seattle (refer to Box 1.1) carried out a novel torsion-balance test of the weak equivalence principle by fabricating laboratory bodies whose chemical compositions mimic that of the Earth and Moon. They found that the mini-Earth and mini-Moon fell with the same acceleration to 1.4 parts in $1 0 ^ { 1 3 }$ . The uncertainty implied by this possible effect has been incorporated into the bound on $\eta _ { N }$ quoted above.

The Apache Point Observatory for Lunar Laser ranging Operation (APOLLO) project, a joint effort by researchers from the University of Washington, Seattle, and the University of California, San Diego, is using enhanced laser and telescope technology, together with a good, high-altitude site in New Mexico, to improve the LLR bound by as much as an order of magnitude.

Tests of the Nordtvedt effect for neutron stars have also been carried out using a class of systems known as wide-orbit binary millisecond pulsars (WBMSP), which are pulsar–white-dwarf binary systems with small orbital eccentricities. In the gravitational field of the galaxy, a non-zero Nordtvedt effect can induce an anomalous eccentricity pointed toward the galactic center. This can be bounded using statistical methods, given a sufficient number of WBMSPs. Using data from 21 WBMSPs, including recently discovered highly circular systems, Ingrid Stairs and her colleagues obtained the bound $| \eta _ { N } ( \Omega / M c ^ { 2 } ) _ { \mathrm { N S } } | < 5 . 6 \times 1 0 ^ { - 3 }$ . Because $( \Omega / M c ^ { 2 } ) _ { \mathrm { N S } } \sim 0 . 1$ for typical neutron stars, this bound on $\eta _ { N }$ does not compete with the bound from LLR; on the other hand, the presence of neutron stars implies that these systems test the strong equivalence principle in the strong-field regime.

Lunar laser ranging also demonstrated that $G$ is not changing significantly; the bound is $| \dot { G } / G | < 9 \times$ $1 0 ^ { - 1 3 } \mathrm { y r } ^ { - 1 }$ , a limit 83 times smaller than the inverse age of the universe.

# 13.3.4 Tests of the strong equivalence principle: preferred-frame and preferred-location effects

Back in Sec. 13.2.6 we saw that the metric near a body moving in the field of external bodies can be expressed as in Eq. (13.35), with an effective gravitational parameter $G _ { \mathrm { e f f } }$ that varies with time and position. The various contributions to $G _ { \mathrm { e f f } }$ , as displayed in Eq. (13.36), have observable consequences. The most dramatic come from the anisotropies contained in the terms involving $\bar { n } ^ { j } \bar { n } ^ { k } \partial _ { \bar { \jmath } \bar { k } } \hat { X } _ { \mathrm { e x t } }$ and $[ ( { \pmb w } + { \pmb v } ) \cdot { \pmb \bar { n } } ] ^ { 2 }$ . For a body such as the Earth, these terms make the gravitational forces holding the body together weaker in one direction than in another, with the result that the Earth is distorted into an elliptical shape; this is quite analogous to the effects of the luni-solar tides. A gravimeter will then measure a varying acceleration $g$ as the Earth rotates. Assuming that $\pmb { w }$ is the velocity of the solar system relative to the cosmic background radiation, with magnitude $3 7 5 \mathrm { k m / s }$ , then $w ^ { 2 } / c ^ { 2 } \simeq 1 0 ^ { - 6 }$ . From the point of view of the Earth, the dominant external body is actually the galaxy, with $\hat { U } _ { \mathrm { g a l } } \simeq 5 \times 1 0 ^ { - 7 }$ (only the anisotropic part of the potential is relevant, so the much more massive dark matter halo that reportedly surrounds the galaxy can be ignored, as can the mass distribution on larger cosmic scales).

The local $g$ reading of a gravimeter will actually be affected by three factors. The first is the raw variation in $G _ { \mathrm { e f f } }$ . The second is the distortion of the Earth generated by the variation in $G _ { \mathrm { e f f } }$ , which displaces the gravimeter toward or away from the Earth’s center, thus causing the local $g$ to vary. The third is the redistribution of matter caused by the distortion. The latter two effects are controlled by the Love numbers $h$ and $k$ – refer to Sec. 2.4 – whose values depend on the detailed structure of the Earth. The overall factor in gravimeter readings is approximately 1.16 times the raw variation in $G _ { \mathrm { e f f } }$ . Of course, the Sun and Moon generate similar effects via their tidal gravitational fields, called “solid Earth tides” to distinguish them from the more complex oceanic tides. The effect of tides on gravimeters is governed by the same Love numbers. But whereas the PPN variations are oriented relative to the directions of $\pmb { w }$ and the galactic center, which are fixed in inertial space, the luni-solar tides are oriented toward the Sun and Moon, which revolve around the Earth (as seen from the Earth’s point of view). The PPN effects therefore vary dominantly at multiples of a sidereal day, while the luni-solar tides vary at multiples of the solar and lunar day. One can in principle separate the PPN effects from the luni-solar tides by exploiting their slightly different time dependences. In fact, because of the slight inclination of the lunar orbit relative to the ecliptic, and the small eccentricities of the lunar and terrestrial orbits, there are smaller sidebands of the luni-solar tides at the same sidereal frequencies as the PPN tides. But tidal theory is sufficiently advanced that these Newtonian tides can be predicted quite accurately.

The dominant luni-solar tides have amplitudes $\Delta g / g \sim 2 \times 1 0 ^ { - 8 }$ , and measurements using arrays of superconducting gravimeters in the western USA during the middle 1970s showed that there were no anomalous solid tides at the sidereal frequencies, down to the $\Delta g / g \sim 4 \times 1 0 ^ { - 1 0 }$ level. These experiments place upper bounds on the PPN parameters, given by

$$
| \alpha _ { 2 } | < 4 \times 1 0 ^ { - 4 } , \qquad | \xi | < 1 0 ^ { - 3 } .
$$

Another bound can be obtained by examining the cross-term $w \cdot v$ in $G _ { \mathrm { e f f } }$ . As the Earth orbits the Sun, this term varies annually with an amplitude of around $1 0 ^ { - 7 }$ . This variation in the magnitude of $G _ { \mathrm { e f f } }$ causes the Earth to “breathe” in and out; the resulting variations in its moment of inertia cause its rotation rate to vary on an annual basis. Annual variations in the Earth’s rotation rate are well measured, and are known to be related to seasonal changes in atmospheric winds. Again measurements show no evidence of an anomaly, and an upper limit on a combination of $\alpha _ { 1 }$ , $\alpha _ { 2 }$ , and $\alpha _ { 3 }$ could be obtained at the level of about 0.02.

The term involving $\hat { U } _ { \mathrm { e x t } }$ in $G _ { \mathrm { e f f } }$ is intrinsically interesting, because it reveals that nearby matter can affect the locally measured constant of gravitation. But it is not so interesting observationally, because it is approximately constant in time, and of order $1 0 ^ { - 8 }$ for the Sun; because the absolute value of $G$ is known to about one part in $1 0 ^ { 5 }$ , such constant factors are unmeasurable. Even the variation in $\hat { U } _ { \mathrm { e x t } }$ at the level of $1 0 ^ { - 1 0 }$ , because of the eccentricity of the Earth’s orbit, is too small to have any measurable consequences. The final two terms in Eq. (13.36) are also too small, in the context of the Earth, to provide useful tests.

# 13.4 Gravitational radiation in alternative theories of gravity

Back in Sec. 11.1 we learned that in general relativity, the gravitational-wave field in the far-away wave zone is characterized by two polarization modes, $A _ { + } ( \tau )$ and $A _ { \times } ( \tau )$ . For a wave traveling in the $z$ -direction, this means that the non-vanishing components of the wave field are $h ^ { x x } = - h ^ { y y } = G A _ { + } / ( c ^ { 4 } R )$ and $h ^ { x y } = h ^ { y x } = G A _ { \times } / ( c ^ { 4 } R )$ ; the wave is transverse to the direction of propagation, and it satisfies a tracefree condition. Here $R$ is the distance to the source, and $\tau : = t - R / c$ is retarded time.

We wish to generalize this discussion to a class of alternative metric theories of gravity, and we will show that in this context, the most general gravitational wave is characterized by six modes of polarization. The only assumptions we make are that we are examining the spacetime metric in the far-away wave zone, that the field equations reduce to wave equations in the far-away wave zone, and that the propagation speed of the waves is the same as the speed of light. This last assumption is somewhat restrictive, because many alternative theories of gravity predict that gravitational waves have a speed that differs from $c$ . Some predict a speed that varies with the wavelength $\lambda$ , as if the hypothetical quantum particle associated with the waves – the graviton – possessed a non-zero mass; in such a case the speed of gravitational waves would be given by $v _ { g } / c = \sqrt { 1 - ( \lambda / \lambda _ { c } ) ^ { 2 } }$ , where $\lambda _ { c } = h / ( m c )$ is the Compton wavelength of a particle of mass $m$ . Some theories predict that gravitational waves propagate along the null cones of a second metric, distinct from the metric that couples to matter and light. Nevertheless, for simplicity we shall restrict our attention to theories for which gravitational waves propagate at the speed of light. As a matter of fact, our conclusions about the polarization modes do not depend much on the speed of the waves, and similar conclusions would be reached in a more general setting.

# 13.4.1 Gravitational potentials in the far-away wave zone

We choose a reference frame in which the center-of-mass of the system is at rest, and we first examine the metric of a stationary system in this frame. Inspecting Box 13.1, we see that the leading contribution to the 1pn metric when $R \to \infty$ is given by

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 G M } { c ^ { 2 } R } + \frac { G M } { c ^ { 4 } R } \Big [ ( \alpha _ { 2 } + \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { 2 } - \alpha _ { 2 } ( { \pmb w } \cdot { \bf N } ) ^ { 2 } \Big ] \ : , } } \\ { { \displaystyle g _ { 0 j } = \frac { G M } { 2 c ^ { 3 } R } w ^ { k } \Big [ ( 2 \alpha _ { 2 } - \alpha _ { 1 } ) \delta _ { j k } - 2 \alpha _ { 2 } N _ { j } N _ { k } \Big ] \ : , } } \\ { { \displaystyle g _ { j k } = \bigg ( 1 + \frac { 2 \gamma G M } { c ^ { 2 } R } \bigg ) \delta _ { j k } \ : , } } \end{array}
$$

where $M$ is the (active) gravitational mass of the stationary source, $\pmb { w }$ is the velocity of the chosen frame relative to the preferred universal frame, $R : = | { \boldsymbol { x } } |$ , and $N : = x / R$ . From this we can construct the gravitational potentials

$$
h ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - \sqrt { - g } g ^ { \alpha \beta } ,
$$

which formed the basis of our development of post-Minkowskian theory in Chapter 6, and our discussion of gravitational radiation in Chapter 11. To order $c ^ { - 3 }$ we find that the potentials are given by

$$
\begin{array} { l } { { \displaystyle h ^ { 0 0 } = ( 3 \gamma + 1 ) \frac { G M } { c ^ { 2 } R } + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle h ^ { 0 j } = \frac { G M } { 2 c ^ { 3 } R } w ^ { k } \Big [ ( 2 \alpha _ { 2 } - \alpha _ { 1 } ) \delta _ { j k } - 2 \alpha _ { 2 } N _ { j } N _ { k } \Big ] + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle h ^ { j k } = ( 1 - \gamma ) \frac { G M } { c ^ { 2 } R } \delta ^ { j k } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

We see that there is a $c ^ { - 2 }$ contribution to $h ^ { j k }$ whenever $\gamma \neq 1$ ; in general relativity this term vanishes, and indeed, when $\gamma = 1$ and $\alpha _ { 1 } = \alpha _ { 2 } = 0$ we recover the stationary limit of the expressions listed in Eq. (11.6).

We next allow the source to be time-dependent, and to emit gravitational waves. We assume that in such a situation, the stationary potentials in the far-away wave zone are supplemented by

$$
\Delta h ^ { \alpha \beta } = \frac { G } { c ^ { 4 } R } { \cal A } ^ { \alpha \beta } ( \tau , N ) .
$$

We assume specifically that the field equations of the alternative theory reduce in a suitable way to wave equations in the far-away wave zone, and that the propagation speed is equal to $c$ ; this accounts for the assumed dependence of the amplitudes $A ^ { \alpha \beta }$ on retarded time $\tau$ . (We could allow for a different speed $v _ { g }$ and generalize the definition of retarded time to $t - R / v _ { g }$ , but this would have little impact on our discussion of polarization modes, as observed previously.)

We wish to identify the physical meaning of the amplitudes $A ^ { \alpha \beta }$ . When we performed this exercise in Sec. 11.1 in the context of general relativity, we eliminated the redundant components of $A ^ { \alpha \beta }$ by appealing to the harmonic gauge condition $\partial _ { \beta } h ^ { \alpha \beta } = 0$ and its further refinement to the transverse-tracefree gauge; we ended up with two physical polarization modes encoded in $A _ { \mathrm { T T } } ^ { j k }$ . The situation is more complicated in a generic metric theory of gravity. In this case we cannot rely on the harmonic gauge condition, and the number of polarization modes is larger. We can, nevertheless, simplify the description of these modes by appealing to the standard freedom to transform the coordinates.

To effect this simplification we follow the approach described back in Sec. 11.1.3. We decompose $\Delta h ^ { \alpha \beta }$ into irreducible pieces according to

$$
\begin{array} { l } { { \displaystyle \Delta h ^ { 0 0 } = \frac { G } { c ^ { 4 } R } C ( \tau , N ) , } } \\ { { \displaystyle \Delta h ^ { 0 j } = \frac { G } { c ^ { 4 } R } D ^ { j } ( \tau , N ) , } } \\ { { \displaystyle \Delta h ^ { j k } = \frac { G } { c ^ { 4 } R } A ^ { j k } ( \tau , N ) , } } \end{array}
$$

and

$$
\begin{array} { l } { { D ^ { j } = D N ^ { j } + D _ { \mathrm { T } } ^ { j } , } } \\ { { A ^ { j k } = \displaystyle \frac { 1 } { 3 } \delta ^ { j k } A + \left( N ^ { j } N ^ { k } - \displaystyle \frac { 1 } { 3 } \delta ^ { j k } \right) B + 2 N ^ { ( j } A _ { \mathrm { T } } ^ { k ) } + A _ { \mathrm { T T } } ^ { j k } , } } \end{array}
$$

in which $A _ { \mathrm { T } } ^ { j }$ and $D _ { \mathrm { T } } ^ { j }$ are transverse vector fields satisfying $N _ { j } A _ { \mathrm { T } } ^ { j } = N _ { j } D _ { \mathrm { T } } ^ { j } = 0$ , and $A _ { \mathrm { T T } } ^ { j k }$ is a transverse-tracefree tensor field satisfying $N _ { j } A _ { \mathrm { T T } } ^ { j k } = \delta _ { j k } \dot { A _ { \mathrm { T T } } } ^ { j k } = 0$ . The decomposition involves ten independent functions of $\tau$ and $N$ .

The freedom to transform the coordinates must be restricted by the requirement that in the far-away wave zone, $h ^ { \alpha \beta }$ must always be of the general form described by Eqs. (13.78) and (13.79). This implies that the allowed transformations are small deformations described by $x ^ { \alpha } \to x ^ { \prime \alpha } = x ^ { \alpha } + \zeta ^ { \alpha } ( x ^ { \beta } )$ , with a gauge vector $\zeta ^ { \alpha }$ restricted to be of the general form

$$
\begin{array} { l } { { \displaystyle { \zeta ^ { 0 } = \frac { G } { c ^ { 3 } R } \alpha ( \tau , N ) + O ( R ^ { - 2 } ) } , } } \\ { { \displaystyle { \zeta ^ { j } = \frac { G } { c ^ { 3 } R } \beta ^ { j } ( \tau , N ) + O ( R ^ { - 2 } ) } , } } \end{array}
$$

first introduced in Sec. 11.1.5. Note that the gauge vector field satisfies the wave equation $\boxed { 1 } \zeta ^ { \alpha } = O ( R ^ { - 2 } )$ . This does not occur because of a requirement to keep $x ^ { \prime \alpha }$ within the class of harmonic coordinates, as was the case back in Sec. 11.1.5. Instead, this is an automatic property of the assumed form for $\zeta ^ { \alpha }$ , which is designed to preserve the form of the gravitational potentials.

We decompose $\beta ^ { j }$ into longitudinal and transverse pieces, $\beta ^ { j } = N ^ { j } \beta + \beta _ { \mathrm { T } } ^ { j }$ , and performing the gauge transformation on the potentials, we find that

$$
\begin{array} { l } { { \Delta h ^ { \prime 0 0 } = \displaystyle \frac { G } { c ^ { 4 } R } C ^ { \prime } ( \tau , N ) , } } \\ { { \Delta h ^ { \prime 0 j } = \displaystyle \frac { G } { c ^ { 4 } R } D ^ { \prime j } ( \tau , N ) , } } \\ { { \Delta h ^ { \prime j k } = \displaystyle \frac { G } { c ^ { 4 } R } A ^ { \prime j k } ( \tau , N ) , } } \end{array}
$$

with

$$
\begin{array} { l } { { C ^ { \prime } = C + \partial _ { \tau } ( \alpha + \beta ) , } } \\ { { { } } } \\ { { D ^ { \prime } = D + \partial _ { \tau } ( \alpha + \beta ) , } } \\ { { { } } } \\ { { D _ { \mathrm { T } } ^ { \prime \prime } = D _ { \mathrm { T } } ^ { j } + \partial _ { \tau } \beta _ { \mathrm { T } } ^ { j } , } } \\ { { { } } } \\ { { { } A ^ { \prime } = A + \partial _ { \tau } ( 3 \alpha - \beta ) , } } \\ { { { } } } \\ { { { } B ^ { \prime } = B + 2 \partial _ { \tau } \beta , } } \\ { { { } A _ { \mathrm { T } } ^ { \prime \prime } = A _ { \mathrm { T } } ^ { j } + \partial _ { \tau } \beta _ { \mathrm { T } } ^ { j } , } } \\ { { { } } } \\ { { A _ { \mathrm { T } } ^ { \prime \prime k } = A _ { \mathrm { T } } ^ { j k } . } } \end{array}
$$

With the freedom to specify the four functions $\alpha , \beta$ , and $\beta _ { \mathrm { T } } ^ { j }$ , we could decide to make $A ^ { \prime } { } ^ { j k }$ purely transverse and tracefree, but in this case we would find that $C ^ { \prime }$ and $D ^ { \prime j }$ do not vanish. Alternatively, we could decide to make $D ^ { \prime j }$ vanish, but in this case $C ^ { \prime }$ cannot be set equal to zero, and while the remaining freedom could be used to eliminate either $A ^ { \prime }$ or $B ^ { \prime }$ , we cannot achieve both, and we cannot eliminate $A _ { \mathrm { T } } ^ { \prime j }$ . The bottom line is that no matter what choices are made, six independent degrees of freedom remain in the specification of $A ^ { \prime \alpha \beta }$ .

# 13.4.2 Polarizations

The physical meaning of these six degrees of freedom is best identified by examining how a gravitational wave interacts with an actual detector. As we reviewed back in Sec. 11.1.6, the interaction with a short detector is governed by the equation of geodesic deviation,

$$
\frac { d ^ { 2 } \xi _ { j } } { d t ^ { 2 } } = - c ^ { 2 } R _ { 0 j 0 k } \xi ^ { k } ,
$$

in which the components $R _ { 0 j 0 k }$ of the linearized Riemann tensor are given by

$$
R _ { 0 j 0 k } = - \frac { 1 } { 2 } \left( \partial _ { 0 0 } h ^ { j k } - \frac { 1 } { 2 } \partial _ { 0 0 } h \delta _ { j k } + \partial _ { j k } h ^ { 0 0 } + \frac { 1 } { 2 } \partial _ { j k } h + \partial _ { 0 j } h ^ { 0 k } + \partial _ { 0 k } h ^ { 0 j } \right) ,
$$

where $h : = \eta _ { \alpha \beta } h ^ { \alpha \beta } = - h ^ { 0 0 } + h ^ { k k }$ . In general relativity $R _ { 0 j 0 k }$ can be expressed entirely in terms of $h _ { \mathrm { T T } } ^ { j k }$ , the transverse-tracefree piece of the gravitational potentials. In the current context we have instead

$$
c ^ { 2 } R _ { 0 j 0 k } = - { \frac { G } { 2 c ^ { 4 } R } } { \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } } S ^ { j k } ( \tau , N ) ,
$$

where

$$
S ^ { j k } : = \left( \delta ^ { j k } - N ^ { j } N ^ { k } \right) A _ { \mathrm { S } } + N ^ { j } N ^ { k } A _ { \mathrm { L } } + 2 N ^ { ( j } A _ { \mathrm { V } } ^ { k ) } + A _ { \mathrm { T T } } ^ { j k } ,
$$

with

$$
\begin{array} { l } { \displaystyle { A _ { \mathrm { S } } : = - \frac 1 6 ( A + 2 B - 3 C ) , } } \\ { \displaystyle { A _ { \mathrm { L } } : = \frac 1 3 ( A + 2 B + 3 C - 6 D ) , } } \\ { \displaystyle { A _ { \mathrm { V } } ^ { k } : = A _ { \mathrm { T } } ^ { k } - D _ { \mathrm { T } } ^ { k } . } } \end{array}
$$

To arrive at this result we have made use of the fact that for a function $f$ of $\tau$ and $N$ , $\partial _ { j } f = - c ^ { - 1 } N _ { j } \partial _ { \tau } f + O ( R ^ { - 2 } )$ . It can be checked that $A _ { \mathrm { S } } , A _ { \mathrm { L } } , A _ { \mathrm { V } } ^ { j }$ , and $A _ { \mathrm { T T } } ^ { j k }$ are all invariant under a gauge transformation described by Eq. (13.82). This is as it should be, because the linearized Riemann tensor is necessarily gauge invariant, and the equation of geodesic deviation describes physically measurable motions. In general relativity, the conditions $C = D$ , $A + 2 B = 3 D$ , and $D _ { \mathrm { T } } ^ { k } = A _ { \mathrm { T } } ^ { k }$ that arise from the harmonic-gauge condition – refer to Eq. (11.14) – imply that $A _ { \mathrm { S } } , A _ { \mathrm { V } } ^ { j }$ , and $A _ { \mathrm { { L } } }$ all vanish.

Integrating the equation of geodesic deviation to first order in the displacement yields

$$
\xi ^ { j } ( t ) = \xi ^ { j } ( 0 ) + \frac { G } { 2 c ^ { 4 } R } S ^ { j k } ( \tau , N ) \xi ^ { k } ( 0 ) .
$$

We see that the detector’s response is governed by a number of gravitational-wave modes: a scalar mode $A _ { \mathrm { S } }$ which is transverse to the direction of propagation (but not tracefree), a longitudinal mode $A _ { \mathrm { { L } } }$ , two vector modes $A _ { \mathrm { V } } ^ { j }$ which are partly longitudinal and partly transverse, and the familiar transverse-tracefree modes $A _ { \mathrm { T T } } ^ { j k }$ . In general relativity the absence of scalar, longitudinal, and vector modes implies that the response is governed entirely by the transverse-tracefree modes.

To describe the gravitational-wave modes in more concrete terms, we make use of the vector basis $( N , \pmb { \vartheta } , \pmb { \varphi } )$ first introduced in Sec. 11.1.7. Employing the polar angles $( \vartheta , \varphi )$ t o describe the direction of propagation, we write

$$
\begin{array} { r l } & { N : = \left[ \sin \vartheta \cos \varphi , \sin \vartheta \sin \varphi , \cos \vartheta \right] , } \\ & { \vartheta : = \left[ \cos \vartheta \cos \varphi , \cos \vartheta \sin \varphi , - \sin \vartheta \right] , } \\ & { \varphi : = \left[ - \sin \varphi , \cos \varphi , 0 \right] , } \end{array}
$$

and we define the gravitational-wave polarizations

$$
\begin{array} { l } { { { \displaystyle { \cal A } _ { \mathrm { V 1 } } : = \vartheta _ { k } { \cal A } _ { \mathrm { V } } ^ { k } } , } } \\ { { { \displaystyle { \cal A } _ { \mathrm { V 2 } } : = \varphi _ { k } { \cal A } _ { \mathrm { V } } ^ { k } , } } } \\ { { { \displaystyle { \cal A } _ { + } : = \frac { 1 } { 2 } \big ( \vartheta _ { j } \vartheta _ { k } - \varphi _ { j } \varphi _ { k } \big ) { \cal A } _ { \mathrm { T T } } ^ { j k } , } } } \\ { { { \displaystyle { \cal A } _ { \mathrm { x } } : = \frac { 1 } { 2 } \big ( \vartheta _ { j } \varphi _ { k } + \varphi _ { j } \vartheta _ { k } \big ) { \cal A } _ { \mathrm { T T } } ^ { j k } . } } } \end{array}
$$

Making the substitutions in $S ^ { j k }$ , we obtain

$$
\begin{array} { r l } & { S ^ { j k } = A _ { \mathrm { S } } \big ( \vartheta ^ { j } \vartheta ^ { k } + \varphi ^ { j } \varphi ^ { k } \big ) + A _ { \mathrm { L } } N ^ { j } N ^ { k } } \\ & { \qquad + 2 A _ { \mathrm { V 1 } } N ^ { ( j } \vartheta ^ { k ) } + 2 A _ { \mathrm { V 2 } } N ^ { ( j } \varphi ^ { k ) } } \\ & { \qquad + A _ { + } \big ( \vartheta ^ { j } \vartheta ^ { k } - \varphi ^ { j } \varphi ^ { k } \big ) + A _ { \times } \big ( \vartheta ^ { j } \varphi ^ { k } + \varphi ^ { j } \vartheta ^ { k } \big ) . } \end{array}
$$

For a wave traveling in the $z$ -direction, $S ^ { j k }$ can be displayed as the matrix

$$
S ^ { j k } = \left( \begin{array} { c c c } { { A _ { \mathrm { { S } } } + A _ { + } } } & { { A _ { \times } } } & { { A _ { \mathrm { { V } 1 } } } } \\ { { A _ { \times } } } & { { A _ { \mathrm { { S } } } - A _ { + } } } & { { A _ { \mathrm { { V } 2 } } } } \\ { { A _ { \mathrm { { V } 1 } } } } & { { A _ { \mathrm { { V } 2 } } } } & { { A _ { \mathrm { { L } } } } } \end{array} \right) .
$$

# Box 13.3

# Distortion of a ring of particles by a gravitational wave

The discussion of Sec. 11.1.8 can be generalized to the case in which a gravitational wave includes all six polarization modes. For a gravitational wave traveling in the $z$ -direction past an initially circular ring of particles, the displacement of a given particle from the center of the ring is given by Eq. (13.90). In terms of the $( x , y , z )$ components of the vector $\pmb { \xi }$ , we have

$$
\begin{array} { l } { { \displaystyle x ( t ) = x _ { 0 } + \frac { G } { 2 c ^ { 4 } R } \Big [ ( A _ { \mathrm { S } } + A _ { + } ) x _ { 0 } + A _ { \mathrm { x } } y _ { 0 } + A _ { \mathrm { V } 1 } z _ { 0 } \Big ] \ : , } } \\ { { \displaystyle y ( t ) = y _ { 0 } + \frac { G } { 2 c ^ { 4 } R } \Big [ A _ { \mathrm { x } } x _ { 0 } + ( A _ { \mathrm { S } } - A _ { + } ) y _ { 0 } + A _ { \mathrm { V } 2 } z _ { 0 } \Big ] \ : , } } \\ { { \displaystyle z ( t ) = z _ { 0 } + \frac { G } { 2 c ^ { 4 } R } \Big [ A _ { \mathrm { V } 1 } x _ { 0 } + A _ { \mathrm { V } 2 } y _ { 0 } + A _ { \mathrm { L } } z _ { 0 } \Big ] \ : , } } \end{array}
$$

with $\pmb { \xi } ( 0 ) = [ x _ { 0 } , y _ { 0 } , z _ { 0 } ]$ . For pure + or × modes, the patterns are as previously displayed in Eqs. (11.50). A pure S mode is also transverse, and causes a circle in the $x - y$ plane to shrink and grow while remaining a circle. A V1 mode distorts a circle in the $x \mathrm { - } z$ plane into an ellipse rotated by 45 degrees, while a V2 mode does the same to a circle in the $y - z$ plane. Finally, an L mode takes a circle in any plane parallel to the $z$ -axis and stretches and shrinks it in the $z$ -direction. These deformations are illustrated in Fig. 13.1.

# 13.4.3 Interaction with a laser interferometer

The interaction of a gravitational wave with a laser interferometer was described back in Sec. 11.5 in the context of general relativity. This discussion can easily be generalized to incorporate all six polarization modes allowed by a generic alternative theory. In Sec. 11.5 we found that the detector’s response, measured by the phase difference between the light signals traveling in both arms of the interferometer, is given by $\Delta \Phi = ( 4 \pi \nu G L _ { 0 } / c ^ { 5 } R ) S ( t )$ , where $\nu$ is the frequency of the laser light, $L _ { 0 }$ is the length of the unperturbed interferometer arm, $R$ is the distance from the source, and $S ( t )$ is the detector’s response function. In general relativity this was given by Eq. (11.313). In a generic alternative theory the response function is given instead by

$$
S ( t ) = { \frac { 1 } { 2 } } \bigl ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \bigr ) S ^ { j k } ( \tau , N ) ,
$$

![](images/18b0d2981de7098d25cae4531ea66d1dd19a56c29e409c7060940cb50afda3aa.jpg)

# Fig. 13.1

Effect of the S, L, and V gravitational-wave polarizations on a circular ring of freely-moving particles. The wave travels in the z-direction. The effect of the $^ +$ and $\times$ polarizations was displayed in Fig. 11.1. For the S mode, the wave propagates into the page, and the ring is placed in the x-y plane. For the L mode, the wave propagates from left to right (in the direction of the arrow), and the ring is placed either in the x-z plane or in the y-z plane. For the V modes, the wave also propagates from left to right; in the case of the V1 mode, the ring is placed in the x-z plane, and in the case of the $\forall 2$ mode, the ring is placed in the y-z plane.

where $e _ { 1 }$ and $\boldsymbol { e } _ { 2 }$ are unit vectors pointing in the direction of the interferometer arms, and $S ^ { j k }$ is given by Eqs. (13.88) or (13.93).

Adopting the same vectorial basis as in Sec. 11.5, we write

$$
\begin{array} { r l } & { S ^ { j k } = \big ( e _ { X } ^ { j } e _ { X } ^ { k } + e _ { Y } ^ { j } e _ { Y } ^ { k } \big ) A _ { \mathrm { S } } + e _ { Z } ^ { j } e _ { Z } ^ { k } A _ { \mathrm { L } } } \\ & { \phantom { A _ { X } ^ { j } = } + \big ( e _ { X } ^ { j } e _ { Z } ^ { k } + e _ { Z } ^ { j } e _ { X } ^ { k } \big ) A _ { \mathrm { V } 1 } + \big ( e _ { Y } ^ { j } e _ { Z } ^ { k } + e _ { Z } ^ { j } e _ { Y } ^ { k } \big ) A _ { \mathrm { V } 2 } } \\ & { \phantom { A _ { X } ^ { j } = } + \big ( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \big ) A _ { + } + \big ( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \big ) A _ { \times } , } \end{array}
$$

and we insert the expressions for $e _ { 1 }$ and $\scriptstyle { e _ { 2 } }$ displayed in Eq. (11.319). After some manipulations we obtain

$$
S ( t ) = F _ { \mathrm { S } } A _ { \mathrm { S } } + F _ { \mathrm { L } } A _ { \mathrm { L } } + F _ { \mathrm { V 1 } } A _ { \mathrm { V 1 } } + F _ { \mathrm { V 2 } } A _ { \mathrm { V 2 } } + F _ { + } A _ { + } + F _ { \times } A _ { \times } ,
$$

where the angular pattern functions $F _ { A } ( \theta , \phi , \psi )$ are given by

$$
\begin{array} { r l } & { F _ { \mathrm { S } } = - \frac { 1 } { 2 } \sin ^ { 2 } \theta \cos 2 \phi , } \\ & { F _ { \mathrm { L } } = \frac { 1 } { 2 } \sin ^ { 2 } \theta \cos 2 \phi , } \\ & { F _ { \mathrm { V I } } = - \sin \theta ( \cos \theta \cos 2 \phi \cos \psi - \sin 2 \phi \sin \psi ) , } \\ & { F _ { \mathrm { V } 2 } = - \sin \theta ( \cos \theta \cos 2 \phi \sin \psi + \sin 2 \phi \cos \psi ) , } \\ & { F _ { \mathrm { + } } = \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \cos 2 \psi - \cos \theta \sin 2 \phi \sin 2 \psi , } \\ & { F _ { \mathrm { x } } = \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \sin 2 \psi + \cos \theta \sin 2 \phi \cos 2 \psi . } \end{array}
$$

The clear detection of a scalar, longitudinal, or vector polarization in a gravitational-wave interferometer would provide serious evidence against general relativity.

# 13.4.4 Multipolar structure of gravitational waves

In Chapter 11 we learned that in general relativity, the gravitational waves emitted by a slowly-moving system are dominantly quadrupolar; the waves are generated mostly by variations in the quadrupole-moment tensor of the mass distribution, and there is no monopole or dipole radiation. As we discussed back in Sec. 7.1.4, this is because the field equations of general relativity insist that the monopole moment of the gravitational field in the wave zone be the total mass of the system, which is constant up to small changes resulting from radiative losses. The field equations also demand that the time derivative of the dipole moment be the total momentum of the system, which is also constant up to radiative losses, and can be set to zero by a suitable choice of reference frame. It is therefore the quadrupole moment that leads off in generating gravitational waves. As we have also seen, in general relativity the gravitational waves are described by two modes of polarizations, $h _ { + }$ and $h _ { \times }$ , and the radiative fluxes of energy, momentum, and angular momentum can all be obtained from $h _ { + }$ and $h _ { \times }$ .

No such rules apply in alternative metric theories of gravity. There is no reason to expect that a generic theory will predict the suppression of monopole and dipole radiation, and as we have seen, there is every reason to expect that the gravitational waves will display more than two polarization modes. In addition, the radiative fluxes can be a lot more complicated, involving all polarization modes and the additional fields that might be present in the theory. It is therefore difficult to make general statements about the generation of gravitational waves in alternative theories of gravity, and one is forced to explore the predictions of each theory separately. Studies carried out in the wake of the discovery of the Hulse–Taylor binary pulsar in 1974 revealed the unusual fact that a number of otherwise respectable theories actually predicted the emission of negative energy. Once the orbital period of the binary pulsar was shown to decrease (as opposed to increase) in response to the emission of gravitational waves, these theories found themselves in the gravitational dust-bin. But one class of alternative theories has stubbornly refused to die, in spite of all the strong empirical evidence in support of general relativity. This is the class of scalar–tensor theories, to which we turn next.

# 13.5 Scalar–tensor gravity

One of the simplest ways to formulate an alternative metric theory of gravity is to postulate that the gravitational field is represented by a scalar $\phi$ in addition to the metric $g _ { \alpha \beta }$ . As we have emphasized previously in Sec. 13.1, the matter fields are still assumed to respond only to the metric, and there is no direct interaction with the scalar field. But the field equations relating the matter distribution to the gravitational field will involve this additional degree of freedom. The first scalar–tensor theory of gravitation was formulated by Brans and Dicke, building on previous work by Fierz and Jordan. The theory introduced here is a generalization of the original Brans–Dicke theory; it is in fact the most general theory involving a scalar field in addition to the metric tensor. We shall study a few aspects of this theory, including its predictions regarding weak-field and slow-motion situations, and the generation of gravitational radiation.

# 13.5.1 Field equations

The field equations of scalar–tensor gravity are best obtained by formulating an action principle, much as we did back in Sec. 5.4 in the case of general relativity. The complete action functional for the gravitating system is

$$
S = S _ { \mathrm { g r a v } } + S _ { \mathrm { m a t t e r } } ,
$$

with a gravitational action given by

$$
S _ { \mathrm { g r a v } } = \frac { c ^ { 3 } } { 1 6 \pi G _ { 0 } } \int \biggl [ \phi R - \frac { \omega ( \phi ) } { \phi } g ^ { \alpha \beta } \partial _ { \alpha } \phi \partial _ { \beta } \phi - U ( \phi ) \biggr ] \sqrt { - g } d ^ { 4 } x ,
$$

where $G _ { 0 }$ is a “bare” gravitational constant that will later be related to the locally measured constant $G$ , and $\omega$ and $U$ are arbitrary functions of the scalar field. Note that the coupling between the scalar field and the metric appears in two guises. First, there is a factor of $\phi$ in front of the Ricci scalar, and this can be thought of as a local redefinition of the gravitational constant, $G _ { 0 }  G _ { 0 } / \phi$ , which may now depend on position in spacetime. Second, the metric appears in the kinetic-energy term for the scalar field, proportional to $\partial _ { \alpha } \phi \partial _ { \beta } \phi$ . The matter action is given by

$$
S _ { \mathrm { m a t t e r } } = \int { \mathcal L } ( \mathsf { m } , g _ { \alpha \beta } ) \sqrt { - g } d ^ { 4 } x ,
$$

in which $\mathcal { L }$ is a Lagrangian density involving the matter variables $\mathsf { m }$ and the metric $g _ { \alpha \beta }$ . Note that $\phi$ does not appear in the matter action; this is the statement that the scalar field does not couple directly to the matter variables.

It is a straightforward exercise to vary $S$ with respect to the field variables $\phi$ and $g _ { \alpha \beta }$ to obtain the field equations of scalar–tensor gravity. The resulting equations, however, are rather complicated and not the most useful for practical calculations. For an optimal formulation of the field equations we introduce an auxiliary metric $\tilde { g } _ { \alpha \beta }$ related to the physical metric $g _ { \alpha \beta }$ by the conformal transformation

$$
g _ { \alpha \beta } : = \left( \phi _ { 0 } / \phi \right) \tilde { g } _ { \alpha \beta } ,
$$

in which $\phi _ { 0 }$ is an arbitrary constant that will be selected in later applications. The transformation to the new metric represents a rescaling of spatial and temporal intervals by a factor $( \phi / \phi _ { 0 } ) ^ { 1 / 2 }$ that depends on position in spacetime, but we attach no physical significance to $\tilde { g } _ { \alpha \beta }$ ; it is merely a convenient auxiliary quantity that will be involved in computations, before all final results are expressed in terms of the physical metric $g _ { \alpha \beta }$ . The conformal transformation implies that $g ^ { \alpha \beta } = ( \phi / \phi _ { 0 } ) \tilde { g } ^ { \alpha \beta }$ and $\sqrt { - g } = ( \phi _ { 0 } / \phi ) ^ { 2 } \sqrt { - \tilde { g } }$ , and it can be shown that the Ricci scalar transforms according to

$$
R = ( \phi / \phi _ { 0 } ) ^ { 2 } \big ( \tilde { R } + 6 \tilde { \nabla } _ { \alpha } \tilde { B } ^ { \alpha } - 6 \tilde { B } _ { \alpha } \tilde { B } ^ { \alpha } \big ) ,
$$

in which $\tilde { R }$ and $\tilde { \nabla } _ { \alpha }$ are the Ricci scalar and covariant derivative defined in terms of $\tilde { g } _ { \alpha \beta }$ , respectively, $\begin{array} { r } { \tilde { B } _ { \alpha } : = \frac { 1 } { 2 } \partial _ { \alpha } \ln \phi } \end{array}$ , and $\tilde { B } ^ { \alpha } : = \tilde { g } ^ { \alpha \beta } \tilde { B } _ { \beta }$ .

The gravitational action becomes

$$
S _ { \mathrm { g r a v } } = \frac { c ^ { 3 } } { 1 6 \pi \tilde { G } } \int \left[ \tilde { R } - \frac { 2 \omega ( \phi ) + 3 } { 2 \phi ^ { 2 } } \tilde { g } ^ { \alpha \beta } \partial _ { \alpha } \phi \partial _ { \beta } \phi - V ( \phi ) \right] \sqrt { - \tilde { g } } d ^ { 4 } x ,
$$

in which $\tilde { G } : = G _ { 0 } / \phi _ { 0 }$ and $V ( \phi ) : = \phi _ { 0 } U ( \phi ) / \phi ^ { 2 }$ . To arrive at this result we have eliminated the term $6 \tilde { \nabla } _ { \alpha } \tilde { B } ^ { \alpha }$ from the action, because by the four-dimensional version of Gauss’s theorem, it can be expressed as an irrelevant surface integral. Note that $\phi$ no longer appears in front of the Ricci scalar; this has the virtue of simplifying the field equations, and the conformal transformation was introduced for this specific purpose. The matter action becomes

$$
S _ { \mathrm { m a t t e r } } = \int ( \phi _ { 0 } / \phi ) ^ { 2 } { \mathcal L } \big ( \mathsf { m } , \phi , \tilde { g } _ { \alpha \beta } \big ) \sqrt { - \tilde { g } } d ^ { 4 } x .
$$

Note that the scalar field now makes an appearance in the matter action; but the coupling between $\mathsf { m }$ and $\tilde { g } _ { \alpha \beta }$ in $\mathcal { L }$ is still required to occur through the physical metric $( \phi _ { 0 } / \phi ) \tilde { g } _ { \alpha \beta }$ .

Variation of $S$ with respect to the auxiliary metric $\tilde { g } _ { \alpha \beta }$ gives rise to the tensorial field equation

$$
{ \tilde { G } } _ { \alpha \beta } - \frac { 1 } { 2 } { \tilde { \Theta } } _ { \alpha \beta } = \frac { 8 \pi { \tilde { G } } } { c ^ { 4 } } { \tilde { T } } _ { \alpha \beta } ,
$$

in which $\tilde { G } _ { \alpha \beta }$ is the Einstein tensor associated with the auxiliary metric,

$$
\tilde { \Theta } _ { \alpha \beta } : = \frac { 2 \omega + 3 } { \phi ^ { 2 } } \biggl ( \partial _ { \alpha } \phi \partial _ { \beta } \phi - \frac { 1 } { 2 } \tilde { g } _ { \alpha \beta } \tilde { g } ^ { \mu \nu } \partial _ { \mu } \phi \partial _ { \nu } \phi \biggr ) - V ( \phi ) \tilde { g } _ { \alpha \beta } ,
$$

and $\tilde { T } _ { \alpha \beta } : = ( \phi _ { 0 } / \phi ) T _ { \alpha \beta }$ is an auxiliary energy-momentum tensor obtained from the variation of $S _ { \mathrm { m a t t e r } }$ ; $T _ { \alpha \beta }$ is the physical energy-momentum tensor. Variation of $S$ with respect to the scalar field $\phi$ yields the scalar field equation

$$
\tilde { g } ^ { \alpha \beta } \tilde { \nabla } _ { \alpha } \tilde { \nabla } _ { \beta } \phi + \tilde { F } = { \frac { 8 \pi \tilde { G } } { c ^ { 4 } } } { \frac { \phi } { 2 \omega + 3 } } \tilde { T } ,
$$

in which

$$
\tilde { F } : = \frac { 1 } { 2 } \frac { d } { d \phi } \biggl [ \ln \biggl ( \frac { 2 \omega + 3 } { \phi ^ { 2 } } \biggr ) \biggr ] \tilde { g } ^ { \alpha \beta } \partial _ { \alpha } \phi \partial _ { \beta } \phi - \frac { \phi ^ { 2 } } { 2 \omega + 3 } \frac { d V } { d \phi } ,
$$

and $\tilde { T } : = \tilde { g } ^ { \alpha \beta } \tilde { T } _ { \alpha \beta }$ . These are the field equations of scalar–tensor gravity.

# 13.5.2 Post-Minkowskian formulation

We wish to explore the consequences of scalar–tensor gravity in the post-Newtonian regime, both in the near zone, where they will be related to the PPN framework of Sec. 13.2, and in the far-away wave zone, where they will be related to the general discussion of gravitational waves in Sec. 13.4. To perform the required calculations it is advantageous to rely on techniques that proved so powerful in the context of general relativity. We shall therefore subject the field equations of scalar–tensor gravity to a post-Minkowskian reformulation, relying on lessons learned in Chapter 6. We shall next carry out a post-Newtonian expansion of these equations, relying on techniques introduced in Chapter 7.

We adapt the post-Minkowskian techniques of Chapter 6 to the current situation by working in terms of the auxiliary metric $\tilde { g } _ { \alpha \beta }$ instead of the physical metric $g _ { \alpha \beta }$ . We introduce the gothic inverse metric

$$
\tilde { \mathfrak { g } } ^ { \alpha \beta } : = \sqrt { - \tilde { g } } \tilde { g } ^ { \alpha \beta } ,
$$

the tensor density

$$
\tilde { H } ^ { \alpha \mu \beta \nu } : = \tilde { \mathfrak { g } } ^ { \alpha \beta } \tilde { \mathfrak { g } } ^ { \mu \nu } - \tilde { \mathfrak { g } } ^ { \alpha \nu } \tilde { \mathfrak { g } } ^ { \beta \mu } ,
$$

and we rely on the identity of Eq. (6.4),

$$
\partial _ { \mu \nu } \tilde { H } ^ { \alpha \mu \beta \nu } = 2 ( - \tilde { g } ) \tilde { G } ^ { \alpha \beta } + \frac { 1 6 \pi \tilde { G } } { c ^ { 4 } } ( - \tilde { g } ) \tilde { t } _ { \mathrm { L L } } ^ { \alpha \beta } ,
$$

in which $\tilde { t } _ { \mathrm { L L } } ^ { \alpha \beta }$ is a Landau–Lifshitz pseudotensor defined as in Eq. (6.5), but in terms of the auxiliary metric. Making the substitutions in Eq. (13.106) produces

$$
\partial _ { \mu \nu } \tilde { H } ^ { \alpha \mu \beta \nu } = { \frac { 1 6 \pi \tilde { G } } { c ^ { 4 } } } ( - \tilde { g } ) \left( \tilde { T } ^ { \alpha \beta } + \tilde { t } _ { \phi } ^ { \alpha \beta } + \tilde { t } _ { \mathrm { L L } } ^ { \alpha \beta } \right) ,
$$

where

$$
\tilde { t } _ { \phi } ^ { \alpha \beta } : = \frac { c ^ { 4 } } { 1 6 \pi \tilde { G } } \tilde { \Theta } ^ { \alpha \beta } .
$$

At this stage we introduce the potentials

$$
\tilde { h } ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - \tilde { \mathfrak { g } } ^ { \alpha \beta } ,
$$

impose the conformal harmonic gauge condition

$$
\partial _ { \beta } \tilde { h } ^ { \alpha \beta } = 0 ,
$$

and make use of the identity

$$
\partial _ { \mu \nu } \tilde { H } ^ { \alpha \mu \beta \nu } = - \sqcap { \tilde { h } ^ { \alpha \beta } } - \frac { 1 6 \pi \tilde { G } } { c ^ { 4 } } ( - \tilde { g } ) \tilde { t } _ { \mathrm { H } } ^ { \alpha \beta } ,
$$

where $\tilde { t } _ { \mathrm { H } } ^ { \alpha \beta }$ is a harmonic-gauge pseudotensor defined as in Eq. (6.53), but in terms of the potentials $\tilde { h } ^ { \alpha \beta }$ . All this produces the wave equation

$$
\sqcap \tilde { h } ^ { \alpha \beta } = - \frac { 1 6 \pi \tilde { G } } { c ^ { 4 } } \tilde { \tau } ^ { \alpha \beta } ,
$$

in which

$$
\tilde { \tau } ^ { \alpha \beta } : = ( - \tilde { g } ) \Big ( \tilde { T } ^ { \alpha \beta } + \tilde { t } _ { \phi } ^ { \alpha \beta } + \tilde { t } _ { \mathrm { L L } } ^ { \alpha \beta } + \tilde { t } _ { \mathrm { H } } ^ { \alpha \beta } \Big )
$$

plays the role of an effective energy-momentum pseudotensor. The wave equation can be compared with Eq. (6.51); the only differences concern the definition of the potentials, which involves the auxiliary metric instead of the physical metric, and the additional

contribution to $\tilde { \tau } ^ { \alpha \beta }$ that comes from the scalar field. Note that as in Eq. (6.54), the effective energy-momentum pseudotensor necessarily satisfies the conservation identity

$$
\partial _ { \beta } \tilde { \tau } ^ { \alpha \beta } = 0 .
$$

This is equivalent to the conservation equation $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ for the physical energymomentum tensor.

The scalar field equation (13.108) can also be expressed in the form of a wave equation in flat spacetime. For this we rely on the identity

$$
\tilde { g } ^ { \alpha \beta } \tilde { \nabla } _ { \alpha } \tilde { \nabla } _ { \beta } \phi = \frac { 1 } { \sqrt { - \tilde { g } } } \partial _ { \alpha } \bigl ( \tilde { \mathfrak { g } } ^ { \alpha \beta } \partial _ { \beta } \phi \bigr ) = \frac { 1 } { \sqrt { - \tilde { g } } } \bigl ( \big _ { \bf { \perp } } \phi - \tilde { h } ^ { \alpha \beta } \partial _ { \alpha \beta } \phi \bigr ) ,
$$

where we make use of Eq. (13.116) in the second step. Making the substitution in Eq. (13.108), we arrive at

$$
\sqcap \phi = - \frac { 8 \pi { \tilde { G } } } { c ^ { 4 } } \tau _ { \mathrm { s } } ,
$$

in which

$$
\begin{array} { c } { { \tau _ { \mathrm { s } } = - \sqrt { - \tilde { g } } \displaystyle \frac { \phi } { 2 \omega + 3 } \tilde { T } + \displaystyle \frac { c ^ { 4 } } { 1 6 \pi \tilde { G } } \displaystyle \frac { d } { d \phi } \biggl [ \mathrm { l n } \biggl ( \displaystyle \frac { 2 \omega + 3 } { \phi ^ { 2 } } \biggr ) \biggr ] \bigl ( \eta ^ { \alpha \beta } - \tilde { h } ^ { \alpha \beta } \bigr ) \partial _ { \alpha } \phi \partial _ { \beta } \phi } } \\ { { - \displaystyle \frac { c ^ { 4 } } { 8 \pi \tilde { G } } \biggl ( \tilde { h } ^ { \alpha \beta } \partial _ { \alpha \beta } \phi + \sqrt { - \tilde { g } } \displaystyle \frac { \phi ^ { 2 } } { 2 \omega + 3 } \displaystyle \frac { d V } { d \phi } \biggr ) } } \end{array}
$$

is an effective source for the scalar field.

# 13.5.3 Slow-motion condition

To proceed with the integration of Eqs. (13.118) and (13.123), we set $V ( \phi ) = 0$ for simplicity, and assume that the matter distribution is subjected to a slow-motion condition, so that $v _ { c } \ll c$ , with $v _ { c }$ denoting a characteristic velocity of the matter variables. As we discussed back in Sec. 7.1, this assumption implies the existence of a hierarchy between the components of the energy-momentum tensor, so that $T ^ { 0 0 } = { \cal O } ( c ^ { 2 } )$ , $T ^ { 0 j } = { O } ( c )$ , and $T ^ { j k } = O ( 1 )$ . The hierarchy is inherited by the gravitational potentials, and to reflect this we introduce the notation

$$
\begin{array} { l } { { \displaystyle { { \tilde { h } } } ^ { 0 0 } : = \frac { 4 } { c ^ { 2 } } { \tilde { V } } , } } \\ { { \displaystyle { { \tilde { h } } } ^ { 0 j } : = \frac { 4 } { c ^ { 3 } } { \tilde { V } } ^ { j } , } } \\ { { \displaystyle { { \tilde { h } } } ^ { j k } : = \frac { 4 } { c ^ { 4 } } { \tilde { W } } ^ { j k } , } } \end{array}
$$

in which $\tilde { V } , \tilde { V } ^ { j }$ , and $\tilde { W } ^ { j k }$ are assumed to scale as $O ( 1 )$ . We also introduce the notation

$$
\phi = \phi _ { 0 } \bigg ( 1 + \frac { 2 } { c ^ { 2 } } f \bigg )
$$

for the scalar field, which reflects the expectation that variations in $\phi$ will scale as $O ( c ^ { - 2 } )$ . Taking $f$ to approach zero as $r  \infty$ , the expression also assigns a meaning to the constant $\phi _ { 0 }$ introduced in Eq. (13.102): it represents the asymptotic value $\phi ( \infty )$ of the scalar field far away from the matter distribution. In principle this could depend on time, because $\phi ( \infty )$ is determined by the conditions that prevail in the asymptotic regions of the spacetime. For example, the asymptotic behavior of the scalar field could be tied to the cosmological expansion, which would dictate that $\phi ( \infty )$ should indeed depend on time. But this dependence can be ignored whenever its characteristic time scale is very long compared with the dynamical time scale associated with the system itself. Under such circumstances, we can safely take $\phi ( \infty )$ to be a constant, and associate it with $\phi _ { 0 }$ .

The relations displayed in Eq. (7.24) allow us to express the auxiliary metric in terms of the potentials $\tilde { V } , \tilde { V } ^ { j }$ , and $\tilde { W } ^ { j k }$ . We have

$$
\begin{array} { l } { { \displaystyle \tilde { g } _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } \tilde { V } + \frac { 2 } { c ^ { 4 } } \big ( \tilde { W } - 3 \tilde { V } ^ { 2 } \big ) + O ( c ^ { - 6 } ) , } } \\ { { \displaystyle \tilde { g } _ { 0 j } = - \frac { 4 } { c ^ { 3 } } \tilde { V } ^ { j } + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle \tilde { g } _ { j k } = \delta _ { j k } \bigg ( 1 + \frac { 2 } { c ^ { 2 } } \tilde { V } \bigg ) + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle ( - \tilde { g } ) = 1 + \frac { 4 } { c ^ { 2 } } \tilde { V } + O ( c ^ { - 4 } ) , } } \end{array}
$$

in which $\tilde { W } : = \delta _ { j k } \tilde { W } ^ { j k }$ . From Eqs. (13.102) and (13.125) we can then obtain the components of the physical metric:

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 } { c ^ { 2 } } \big ( { \tilde { V } } + f \big ) + \frac { 2 } { c ^ { 4 } } \big ( { \tilde { W } } - 3 { \tilde { V } } ^ { 2 } - 2 f { \tilde { V } } - 2 f ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } { \tilde { V } } ^ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \bigg [ 1 + \frac { 2 } { c ^ { 2 } } \big ( { \tilde { V } } - f \big ) \bigg ] + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

The next order of business is to compute the effective energy-momentum pseudotensor $\tilde { \tau } ^ { \alpha \beta }$ . We begin with an examination of the matter contribution, assuming that the matter consists of a perfect fluid. The physical energy-momentum tensor $T ^ { \alpha \beta }$ is expressed as in Sec. 7.1.1, in terms of the metric $g _ { \alpha \beta }$ and the matter variables $\mathfrak { m } = \{ \rho ^ { * } , p , \Pi , \pmb { v } \}$ – refer to Eq. (7.1) and the following equations. The field equations, however, involve the auxiliary energy-momentum tensor

$$
\tilde { T } ^ { \alpha \beta } = \left( \phi _ { 0 } / \phi \right) ^ { 3 } T ^ { \alpha \beta } .
$$

Using the techniques developed in Secs. 7.2.1 and 7.3.1, and incorporating the metric of Eq. (13.127), we quickly obtain

$$
\begin{array} { l } { { c ^ { - 2 } ( - \tilde { g } ) \tilde { T } ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \displaystyle \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 \tilde { V } + \Pi - f \biggr ) + { \cal O } ( c ^ { - 4 } ) \biggr ] , } } \\ { { c ^ { - 1 } ( - \tilde { g } ) \tilde { T } ^ { 0 j } = \rho ^ { * } v ^ { j } + { \cal O } ( c ^ { - 2 } ) , } } \\ { { ( - \tilde { g } ) \tilde { T } ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + { \cal O } ( c ^ { - 2 } ) , } } \end{array}
$$

for the components of the energy-momentum tensor, expressed to a sufficient degree of accuracy as post-Newtonian expansions.

The contribution from the scalar field can be obtained from Eqs. (13.107), (13.114), (13.125), and (13.126). The calculation relies on an expansion of the arbitrary function $\omega ( \phi )$ in powers of $c ^ { - 2 }$ , which can be expressed as

$$
\omega ( \phi ) = \omega _ { 0 } + \frac { 2 } { c ^ { 2 } } \phi _ { 0 } \omega _ { 0 } ^ { \prime } f + { \cal O } ( c ^ { - 4 } ) ,
$$

in which

$$
\omega _ { 0 } : = \omega ( \phi _ { 0 } ) , \qquad \omega _ { 0 } ^ { \prime } : = \frac { d \omega } { d \phi } \bigg | _ { \phi _ { 0 } } .
$$

A straightforward computation returns

$$
\begin{array} { r l } & { c ^ { - 2 } ( - \tilde { g } ) t _ { \phi } ^ { 0 0 } = \displaystyle \frac { 2 \omega _ { 0 } + 3 } { 8 \pi \tilde { G } c ^ { 2 } } \partial _ { n } f \partial _ { n } f + O ( c ^ { - 4 } ) , } \\ & { c ^ { - 1 } ( - \tilde { g } ) t _ { \phi } ^ { 0 j } = O ( c ^ { - 2 } ) , } \\ & { ( - \tilde { g } ) t _ { \phi } ^ { j k } = \displaystyle \frac { 2 \omega _ { 0 } + 3 } { 4 \pi \tilde { G } c ^ { 2 } } \bigg ( \partial _ { j } f \partial _ { k } f - \frac { 1 } { 2 } \delta _ { j k } \partial _ { n } f \partial _ { n } f \bigg ) + O ( c ^ { - 2 } ) . } \end{array}
$$

The Landau–Lifshitz contribution to the effective energy-momentum pseudotensor can be obtained directly from Eq. (7.48b) and the listing of potentials provided in Eq. (13.124). We get

$$
\begin{array} { r c l } { { } } & { { } } & { { c ^ { - 2 } ( - \tilde { g } ) t _ { \mathrm { L L } } ^ { 0 0 } = - \displaystyle \frac { 7 } { 8 \pi \tilde { G } c ^ { 2 } } \partial _ { n } \tilde { V } \partial _ { n } \tilde { V } + { \cal O } ( c ^ { - 4 } ) , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle c ^ { - 1 } ( - \tilde { g } ) t _ { \mathrm { L L } } ^ { 0 j } = { \cal O } ( c ^ { - 2 } ) , } } \\ { { } } & { { } } & { { ( - \tilde { g } ) t _ { \mathrm { L L } } ^ { j k } = \displaystyle \frac { 1 } { 4 \pi \tilde { G } } \biggl ( \partial _ { j } \tilde { V } \partial _ { k } \tilde { V } - \displaystyle \frac { 1 } { 2 } \delta _ { j k } \partial _ { n } \tilde { V } \partial _ { n } \tilde { V } \biggr ) + { \cal O } ( c ^ { - 2 } ) . } } \end{array}
$$

Similarly, the harmonic-gauge contribution can be obtained directly from Eq. (7.52), and we get

$$
\begin{array} { r } { c ^ { - 2 } ( - \tilde { g } ) t _ { \mathrm { H } } ^ { 0 0 } = O ( c ^ { - 4 } ) , } \\ { c ^ { - 1 } ( - \tilde { g } ) t _ { \mathrm { H } } ^ { 0 j } = O ( c ^ { - 4 } ) , } \\ { ( - \tilde { g } ) t _ { \mathrm { H } } ^ { j k } = O ( c ^ { - 2 } ) . } \end{array}
$$

Collecting results, we arrive at complete expressions for the components of the effective energy-momentum pseudotensor,

$$
\begin{array} { r l } & { c ^ { - 2 } \tilde { \tau } ^ { 0 0 } = \rho ^ { * } \bigg [ 1 + \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } \nu ^ { 2 } + 3 \tilde { V } + \Pi - f \bigg ) \bigg ] } \\ & { \qquad + \frac { 1 } { 4 \pi \tilde { G } c ^ { 2 } } \bigg [ - \frac { 7 } { 2 } \partial _ { n } \tilde { V } \partial _ { n } \tilde { V } + \frac { 1 } { 2 } ( 2 \omega _ { 0 } + 3 ) \partial _ { n } f \partial _ { n } f \bigg ] + O ( c ^ { - 4 } ) , } \\ & { c ^ { - 1 } \tilde { \tau } ^ { 0 j } = \rho ^ { * } \nu ^ { j } + O ( c ^ { - 2 } ) , ~ } \\ & { \qquad \tilde { \tau } ^ { j k } = \rho ^ { * } \nu ^ { j } \nu ^ { k } + p \delta ^ { j k } + \frac { 1 } { 4 \pi \tilde { G } } \bigg [ \partial _ { j } \tilde { V } \partial _ { k } \tilde { V } - \frac { 1 } { 2 } \delta _ { j k } \partial _ { n } \tilde { V } \partial _ { n } \tilde { V } } \\ & { \qquad + ( 2 \omega _ { 0 } + 3 ) \Big ( \partial _ { j } f \partial _ { k } f - \frac { 1 } { 2 } \delta _ { j k } \partial _ { n } f \partial _ { n } f \Big ) \bigg ] + O ( c ^ { - 2 } ) . } \end{array}
$$

The same expansion techniques can be used to compute the scalar source of Eq. (13.123). Here we find that only the first two terms contribute at the required order, and we get

$$
\begin{array} { c c } { { c ^ { - 2 } \tau _ { \mathrm { s } } = { \displaystyle \frac { \phi _ { 0 } \rho ^ { * } } { 2 \omega _ { 0 } + 3 } } \biggl [ 1 - \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + \tilde { V } - \Pi + 3 p / \rho ^ { * } \biggr ) + \frac { 1 } { c ^ { 2 } } \biggl ( 1 - \frac { 4 \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { 2 \omega _ { 0 } + 3 } \biggr ) f \biggr ] } } \\ { { - \displaystyle \frac { \phi _ { 0 } } { 2 \pi \tilde { G } c ^ { 2 } } \biggl ( 1 - \frac { \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { 2 \omega _ { 0 } + 3 } \biggr ) \partial _ { n } f \partial _ { n } f + O ( c ^ { - 4 } ) . } } \end{array}
$$

The source terms for the wave equations have now been computed to the required degree of accuracy. The next task is the integration of these equations.

# 13.5.4 Near-zone solution: PPN metric

We employ the techniques developed in Sec. 6.3 to integrate the wave equations (13.118) and (13.122). Each equation is of the form $\square \psi = - 4 \pi \mu$ , and we recall that $\psi ( t , { \boldsymbol { x } } )$ can be expressed as an integral over the past light cone of the field point $( t , \boldsymbol { x } )$ . The domain of integration $\mathcal { C }$ is decomposed as $\mathcal { C } = \mathcal { N } + \mathcal { W }$ , into a near-zone domain $\mathcal { N }$ and a wavezone domain $\mathcal { W }$ , and $\psi$ is similarly decomposed as $\psi = \psi _ { \mathcal { N } } + \psi _ { \mathcal { W } }$ . With $( t , \boldsymbol { x } )$ situated in the near zone, an expression for $\psi _ { \mathcal { N } }$ was displayed in Eq. (6.92), and the discussion of Sec. 7.3.4 indicates that $\psi _ { \mathcal { H } }$ makes no contribution at 1pn order, the level of accuracy maintained in our computations. With all this in mind, the near-zone solution to the wave equation can be expressed as

$$
\begin{array} { l } { \displaystyle \psi ( t , \pmb { x } ) = \int _ { \mathcal { M } } \frac { \mu ( t , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } - \frac { 1 } { c } \frac { d } { d t } \int _ { \mathcal { M } } \mu ( t , \pmb { x } ^ { \prime } ) d ^ { 3 } x ^ { \prime } } \\ { \displaystyle \qquad + \frac { 1 } { 2 c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int _ { \mathcal { M } } \mu ( t , \pmb { x } ^ { \prime } ) | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } + { \cal O } ( c ^ { - 3 } ) , } \end{array}
$$

where the domain of integration $\mathcal { M }$ is described by $| x ^ { \prime } | < \mathcal { R }$ , with $\mathcal { R }$ denoting the arbitrary radius of the boundary between the near and wave zones. To evaluate the right-hand side of Eq. (13.137) we require an expression for $\mu ( t , \mathbf { \boldsymbol { x } } ^ { \prime } )$ in the near zone, and such expressions for $\tilde { \tau } ^ { \alpha \beta }$ and $\tau _ { \mathrm { s } }$ were obtained in the preceding subsection.

Before we proceed we introduce the notation

$$
\zeta : = \frac { 1 } { 2 \omega _ { 0 } + 4 } , \qquad \lambda : = \frac { \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { ( 2 \omega _ { 0 } + 3 ) ( 2 \omega _ { 0 } + 4 ) } .
$$

These new quantities act as substitutes for $\omega _ { 0 }$ and $\omega _ { 0 } ^ { \prime }$ , as defined by Eq. (13.131). In terms of $\zeta$ and $\lambda$ we have that $2 \omega _ { 0 } + 3 = ( 1 - \zeta ) / \zeta$ and $\phi _ { 0 } \omega _ { 0 } ^ { \prime } = \lambda ( 1 - \zeta ) / \zeta ^ { 2 }$ .

Inspection of Eqs. (13.135) and (13.136) reveals that the source functions $\tilde { \tau } ^ { \alpha \beta }$ and $\tau _ { \mathrm { s } }$ involve the variables $\tilde { V }$ and $f$ that appear on the left-hand side of the wave equations. This situation is familiar from the post-Minkowskian formulation of general relativity reviewed in Chapter 6, and to handle it we rely on the iterative strategy described in Sec. 6.2.3. To obtain $\tilde { V }$ and $f$ to leading order in a post-Newtonian expansion we set $c ^ { - 2 } \tilde { \tau } ^ { 0 0 } = \rho ^ { * } + { \cal O } ( c ^ { - 2 } )$ and $c ^ { - 2 } \tau _ { \mathrm { s } } = \zeta \phi _ { 0 } \rho ^ { * } / ( 1 - \zeta ) + O ( c ^ { - 2 } )$ , insert Eqs. (13.124) and (13.125) within Eqs. (13.118) and (13.122), and get the solutions from Eq. (13.137). We

find

$$
\begin{array} { l } { \displaystyle \tilde { V } = \tilde { G } \int \frac { \rho ^ { * } ( t , \boldsymbol { x } ^ { \prime } ) } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } \boldsymbol { x } ^ { \prime } + O ( c ^ { - 2 } ) , } \\ { \displaystyle f = \frac { \zeta \tilde { G } } { 1 - \zeta } \int \frac { \rho ^ { * } ( t , \boldsymbol { x } ^ { \prime } ) } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } \boldsymbol { x } ^ { \prime } + O ( c ^ { - 2 } ) , } \end{array}
$$

and we note that $\tilde { V }$ and $f$ bear a striking resemblance to the Newtonian potential

$$
U = G \int \frac { \rho ^ { * } ( t , { \boldsymbol { x } } ^ { \prime } ) } { | { \boldsymbol { x } } - { \boldsymbol { x } } ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

which is defined in terms of the physically measured gravitational constant $G$ . The Newtonian potential is formally defined in terms of the physical metric by $g _ { 0 0 } =$ $- 1 + 2 U / c ^ { 2 } + { \cal O } ( c ^ { - 4 } )$ , and the precise relationship with $\tilde { V }$ and $f$ is given by Eq. (13.127), which reveals that

$$
U = \tilde { V } + f = \frac { \tilde { G } } { 1 - \zeta } \int \frac { \rho ^ { * } ( t , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

Comparison with Eq. (13.140) gives us

$$
G = \frac { \tilde { G } } { 1 - \zeta } = \frac { 2 \omega _ { 0 } + 4 } { 2 \omega _ { 0 } + 3 } \tilde { G } ,
$$

the relationship between the theoretical parameter $\tilde { G } = G _ { 0 } / \phi _ { 0 }$ and the physically measured gravitational constant.

We next proceed with the second iteration of the wave equations. We insert ${ \tilde { G } } = ( 1 -$ $\zeta ) G$ , $\tilde { V } = ( 1 - \zeta ) U + O ( c ^ { - 2 } )$ , and $f = \zeta U + O ( c ^ { - 2 } )$ within Eqs. (13.135) and (13.136), and obtain new expressions for the source functions:

$$
\begin{array} { r l } { \displaystyle c ^ { - 2 } \bar { \tau } ^ { 0 0 } = \rho ^ { * } \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } + ( 3 - 4 \xi ) U + \Pi \bigg ] \bigg \} - \frac { 7 - 8 \xi } { 8 \pi G c ^ { 2 } } \partial _ { k } U \partial _ { k } U } & { } \\ { \displaystyle + O ( c ^ { - 4 } ) , } & { \mathrm { ( } } \\ { \displaystyle c ^ { - 1 } \bar { \tau } ^ { 0 j } = \rho ^ { * } v ^ { j } + O ( c ^ { - 2 } ) , } & { \mathrm { ( } } \\ { \displaystyle \bar { \tau } ^ { k k } = \rho ^ { * } v ^ { 2 } + 3 p - \frac { 1 } { 8 \pi G } \partial _ { k } U \partial _ { k } U + O ( c ^ { - 2 } ) , } \\ { \displaystyle c ^ { - 2 } \tau _ { \mathrm { s } } = \frac { \xi \phi _ { 0 } } { 1 - \xi } \bigg [ \rho ^ { * } \bigg \{ 1 - \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } + ( 1 - 2 \xi + 4 \lambda ) U - \Pi + 3 p / \rho ^ { * } \bigg ] \bigg \} } & { } \\ { \displaystyle - \frac { \xi - \lambda } { 2 \pi G c ^ { 2 } } \partial _ { k } U \partial _ { k } U \bigg ] + O ( c ^ { - 4 } ) ; } & { \mathrm { ( } } \end{array}
$$

we shall not need a complete expression for $\tilde { \tau } ^ { j k }$ , because our main goal is to obtain the near-zone metric, which involves only $\tilde { W } : = \delta _ { j k } \tilde { W } ^ { j k }$ . The source functions can also be

expressed as

$$
\begin{array} { r l } & { c ^ { - 2 } \tilde { \tau } ^ { 0 0 } = \rho ^ { * } \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \bigg ] \bigg \} - \frac { 7 - 8 \xi } { 1 6 \pi G \epsilon ^ { 2 } } \nabla ^ { 2 } U ^ { 2 } + O ( c ^ { - 4 } ) , } \\ & { c ^ { - 1 } \tilde { \tau } ^ { 0 j } = \rho ^ { * } v ^ { j } + O ( c ^ { - 2 } ) , } \\ & { \qquad \tilde { \tau } ^ { k k } = \rho ^ { * } \bigg ( v ^ { 2 } - \frac { 1 } { 2 } U \bigg ) + 3 p - \frac { 1 } { 1 6 \pi G } \nabla ^ { 2 } U ^ { 2 } + O ( c ^ { - 2 } ) , } \\ & { c ^ { - 2 } \tau _ { s } = \frac { \xi \phi _ { 0 } } { 1 - \xi } \left\{ \rho ^ { * } \bigg \{ 1 - \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } v ^ { 2 } + ( 1 + 2 \lambda ) U - \Pi + 3 p / \rho ^ { * } \bigg ] \right\} } \\ & { \qquad - \frac { \xi - \lambda } { 4 \pi G \epsilon c ^ { 2 } } \nabla ^ { 2 } U ^ { 2 } \bigg ] + O ( c ^ { - 4 } ) , } \end{array}
$$

by invoking the identity $\begin{array} { r } { \partial _ { k } U \partial _ { k } U = \frac { 1 } { 2 } \nabla ^ { 2 } U ^ { 2 } + 4 \pi G \rho ^ { * } U } \end{array}$ first encountered in Eq. (7.70).

Integration of the wave equations is now straightforward. Once more we insert Eqs. (13.124) and (13.125) within Eqs. (13.118) and (13.122), and get the solutions from Eq. (13.137). Each Poisson integral involving the fluid variables gives rise to one of the potentials listed in Box 13.1, and the Poisson integral involving $\nabla ^ { 2 } U ^ { 2 }$ is evaluated as in Eq. (7.75). We arrive at

$$
\begin{array} { l } { { \displaystyle \tilde { V } = ( 1 - \zeta ) U + \frac { 1 - \zeta } { c ^ { 2 } } \biggl [ \frac 1 2 \Phi _ { 1 } - \frac 1 2 \Phi _ { 2 } + \Phi _ { 3 } + \frac 1 4 ( 7 - 8 \zeta ) U ^ { 2 } + \frac 1 2 \partial _ { t t } X \biggr ] } } \\ { { \mathrm { } } } \\ { { \mathrm { } + O ( c ^ { - 3 } ) , \qquad } } \\ { { \displaystyle \tilde { V } ^ { j } = ( 1 - \zeta ) U ^ { j } + O ( c ^ { - 2 } ) , \qquad } } \\ { { \displaystyle \tilde { W } = ( 1 - \zeta ) \biggl [ \Phi _ { 1 } - \frac 1 2 \Phi _ { 2 } + 3 \Phi _ { 4 } + \frac 1 4 U ^ { 2 } \biggr ] + O ( c ^ { - 1 } ) , \qquad } } \\ { { \mathrm { } } } \\ { { \mathrm { } f = \zeta U + \frac { \zeta } { c ^ { 2 } } \biggl [ - \frac 1 2 \Phi _ { 1 } - ( 1 + 2 \lambda ) \Phi _ { 2 } + \Phi _ { 3 } - 3 \Phi _ { 4 } + ( \zeta - \lambda ) U ^ { 2 } + \frac 1 2 \partial _ { t t } X \biggr ] } } \\ { { \mathrm { } + O ( c ^ { - 3 } ) . \qquad } } \end{array}
$$

Making the substitutions within Eq. (13.127) produces

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \biggl [ \psi - ( 1 + \zeta \lambda ) U ^ { 2 } + \frac { 1 } { 2 } \partial _ { t t } X \biggr ] + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } ( 1 - \zeta ) U ^ { j } + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \biggl [ 1 + \frac { 2 } { c ^ { 2 } } ( 1 - 2 \zeta ) U \biggr ] + O ( c ^ { - 3 } ) , } } \end{array}
$$

in which

$$
\psi : = \frac 1 2 ( 3 - 4 \zeta ) \Phi _ { 1 } - ( 1 + 2 \zeta \lambda ) \Phi _ { 2 } + \Phi _ { 3 } + 3 ( 1 - 2 \zeta ) \Phi _ { 4 } .
$$

The physical metric is presented in the conformal harmonic gauge introduced in Eq. (13.116). To bring it to the standard post-Newtonian gauge of $8 0 \mathbf { x } \ 1 3 . 1$ we implement the coordinate transformation $\begin{array} { r } { t = \bar { t } + \frac { 1 } { 2 } c ^ { - 4 } \partial _ { \bar { t } } X + O ( c ^ { - 6 } ) } \end{array}$ and $x ^ { j } = \bar { x } ^ { j }$ , which was

first encountered in Sec. 8.3.7. When we transform the metric to the new coordinates $( \bar { t } , \bar { x } ^ { j } )$ and drop the overbars on the new variables, we obtain

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \Big [ \psi - ( 1 + \zeta \lambda ) U ^ { 2 } \Big ] + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } ( 1 - \zeta ) U ^ { j } - \frac { 1 } { 2 c ^ { 3 } } \partial _ { t j } X + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \bigg [ 1 + \frac { 2 } { c ^ { 2 } } ( 1 - 2 \zeta ) U \bigg ] + O ( c ^ { - 3 } ) . } } \end{array}
$$

This is the near-zone metric produced by a generic scalar–tensor theory of gravity. It is parameterized by two numbers, $\lambda$ and $\zeta$ , which are related by Eqs. (13.131) and (13.138) to the theory’s coupling function $\omega ( \phi )$ .

The metric can be compared with the PPN metric displayed in Box 13.1. This reveals that the PPN parameters of scalar–tensor gravity are given by

$$
\beta = 1 + \zeta \lambda = 1 + \frac { \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { ( 2 \omega _ { 0 } + 3 ) ( 2 \omega _ { 0 } + 4 ) ^ { 2 } }
$$

and

$$
\gamma = 1 - 2 \zeta = \frac { \omega _ { 0 } + 1 } { \omega _ { 0 } + 2 } ,
$$

together with $\xi = \alpha _ { n } = \zeta _ { n } = 0$ . The vanishing of the preferred-frame parameters $\alpha _ { n }$ should not come as a surprise, because a scalar field is invariant under Lorentz transformations, and there is no way for a preferred frame to be selected by the theory. The vanishing of $\zeta _ { n }$ is a consequence of the fact that scalar–tensor gravity is based on the action principle of Eq. (13.100), which necessarily makes it a conservative theory. There is no fundamental reason why the Whitehead parameter $\xi$ should vanish in scalar–tensor gravity; this is probably due to the simplicity of the theory. The best empirical constraint on the parameters of scalar–tensor gravity comes from the experimental bound on $\gamma$ provided by the Cassini tracking measurement of the Shapiro time delay. From $| \gamma - 1 | = | 2 \zeta | < 2 . 3 \times 1 0 ^ { - 5 }$ we can conclude that $\omega _ { 0 } > 4 0 0 0 0$ .

# Box 13.4

# Nordtvedt effect and the variation of Geff

Two important features of the post-Newtonian limit of scalar–tensor gravity should be emphasized, both representing violations of the strong equivalence principle. The first is that the theory predicts a non-vanishing Nordtvedt effect; from Eq. (13.74) we see that the Nordtvedt parameter is given by

$$
\eta _ { N } = 2 \zeta ( 1 + 2 \lambda ) = \frac { 1 } { \omega _ { 0 } + 2 } \biggl [ 1 + \frac { \phi _ { 0 } \omega _ { 0 } ^ { \prime } } { ( \omega _ { 0 } + 2 ) ( 2 \omega _ { 0 } + 3 ) } \biggr ] .
$$

The second is that the effective, or locally measured, gravitational constant depends on the presence of nearby matter; from Eq. (13.36) we find that

$$
G _ { \mathrm { e f f } } = G \bigg ( 1 - \eta _ { N } \frac { \hat { U } _ { \mathrm { e x t } } } { c ^ { 2 } } \bigg ) ,
$$

where we have ignored the small term linear in $\bar { r }$ .

The fact that the variation in $G _ { \mathrm { e f f } }$ depends on the same parameter as the Nordtvedt effect is no coincidence. Soon after Nordtvedt informed Dicke (around 1967) that his theory predicted a violation of the strong equivalence principle for self-gravitating bodies, Dicke overcame his initial skepticism by devising an elegant energy-conservation argument that showed that it must be so. The argument goes as follows.

Consider a collection of $N$ particles, each of mass $m$ , on the surface of the Earth. Extract from a reservoir a sufficient amount of energy, $N m g h$ , to raise the particles to a height $h$ , where $g$ is the acceleration of gravity. At this height, assemble the particles into a gravitationally bound body of mass $M = N m - E _ { B } ( h ) / c ^ { 2 } ,$ , where $E _ { B } ( h )$ is the body’s binding energy, and convert the released binding energy into more particles. Let these particles fall to the ground, convert their mass into energy, and add this together with the accumulated kinetic energy to the reservoir, which thereby acquires an energy $E _ { B } ( h ) ( 1 + g h / c ^ { 2 } )$ . Now let the selfgravitating body fall to the ground, but to be open minded, let its acceleration be $a$ instead of $g$ . The kinetic energy it has when it reaches the surface is given by M ah. Add this energy to the reservoir. Now extract enough energy $E _ { B } ( 0 )$ from the reservoir to pull the body apart and return it to the $N$ separate particles, each of mass m. We have returned the system to its initial state, and if energy is to be conserved (otherwise we would have a perpetual motion machine and would make zillions of dollars), the reservoir must now be empty. Doing the accounting, we see that

$$
- N m g h + E _ { B } ( h ) ( 1 + g h / c ^ { 2 } ) + M a h - E _ { B } ( 0 ) = 0 ,
$$

and this implies that

$$
a = g + \frac { E _ { B } ( h ) - E _ { B } ( 0 ) } { M h } .
$$

But the binding energy depends on the local value of the gravitational constant. If we postulate that $G _ { \mathrm { e f f } } =$ $G ( 1 - \eta _ { N } U _ { \oplus } / c ^ { 2 } )$ in the vicinity of the Earth, where $\eta _ { N }$ is an arbitrary parameter, and if we use the properties that $E _ { B } \propto G _ { \mathrm { e f f } }$ and $d U _ { \oplus } / d h = g$ , then we can show that

$$
\begin{array} { l } { { a = g + \displaystyle \frac { 1 } { M } \displaystyle \frac { d E _ { B } } { d h } = g + \displaystyle \frac { 1 } { M } \displaystyle \frac { d E _ { B } } { d G _ { \mathrm { e f f } } } \displaystyle \frac { d G _ { \mathrm { e f f } } } { d h } = g + \displaystyle \frac { 1 } { M } \displaystyle \frac { E _ { B } } { G } \left( - \displaystyle \frac { \eta _ { N } g } { c ^ { 2 } } \right) G } } \\ { { = g \left( 1 - \eta _ { N } \displaystyle \frac { E _ { B } } { M c ^ { 2 } } \right) . } } \end{array}
$$

This is precisely a description of the Nordtvedt effect, and we see that it is indeed tied to the variation of $G _ { \mathrm { e f f } }$ .

We next move to the far-away wave zone and examine the predictions of scalar–tensor gravity regarding the generation of gravitational waves. We rely on the discussion of Sec. 7.1.4, which reveals that when the field point $( t , \boldsymbol { x } )$ is in the far-away wave zone, the

potentials $\tilde { h } ^ { \alpha \beta }$ can be expressed as the multipole expansion

$$
\begin{array} { l } { { \displaystyle { \tilde { h } } ^ { 0 0 } = \frac { 4 \tilde { G } \tilde { M } } { c ^ { 2 } R } + \frac { 2 \tilde { G } } { c ^ { 4 } R } \tilde { \bar { \mathcal { Z } } } ^ { j k } N _ { j } N _ { k } + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle { \tilde { h } } ^ { 0 j } = \frac { 2 \tilde { G } } { c ^ { 4 } R } \tilde { \bar { \mathcal { Z } } } ^ { j k } N _ { k } + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle { \tilde { h } } ^ { j k } = \frac { 2 \tilde { G } } { c ^ { 4 } R } \tilde { \bar { \mathcal { Z } } } ^ { j k } + O ( c ^ { - 5 } ) , } } \end{array}
$$

in which $R : = | { \boldsymbol { x } } | , N : = { \boldsymbol { x } } / R$ ,

$$
\tilde { M } : = \int _ { \mathcal M } c ^ { - 2 } \tilde { \tau } ^ { 0 0 } ( \tau , x ) d ^ { 3 } x \ ,
$$

and

$$
\tilde { \mathcal { Z } } ^ { j k } ( \tau ) : = \int _ { \mathcal { M } } c ^ { - 2 } \tilde { \tau } ^ { 0 0 } ( \tau , \pmb { x } ) x ^ { j } x ^ { k } d ^ { 3 } x ,
$$

where $\tau : = t - R / c$ . The multipole expansion incorporates the conservation equation $\partial _ { \beta } \tilde { \tau } ^ { \alpha \beta } = 0$ , which implies that $\tilde { M }$ is constant up to small radiation-reaction effects, and that the dipole moment $\begin{array} { r } { \tilde { I } ^ { j } : = \int _ { \mathcal { M } } c ^ { - 2 } \tilde { \tau } ^ { 0 0 } x ^ { j } d ^ { 3 } x } \end{array}$ can be set equal to zero (also up to small radiations reaction effects). The potentials because, as was discovered bac $\tilde { h } ^ { \alpha \beta }$ are identified with the near-zone contr Sec. 7.4, the wave-zone contributions $\tilde { h } _ { \mathcal { N } } ^ { \alpha \beta }$ $\tilde { h } _ { \mathcal { W } } ^ { \alpha \beta }$ produce terms that fall off as at the relevant post-Newtonian order; these can be neglected in the far-away wave zone. The potentials of Eq. (13.151) can be compared with the general relativistic expressions displayed in Box 7.7.

The “tensor mass” $\tilde { M }$ can be evaluated by inserting $c ^ { - 2 } \tilde { \tau } ^ { 0 0 }$ from Eqs. (13.144) into Eq. (13.152). The term involving $\nabla ^ { 2 } U ^ { 2 }$ produces a surface integral that scales as $\mathcal { R } ^ { - 1 }$ and therefore makes no $\mathcal { R }$ -independent contribution to the potentials. Discarding this term, we find that

$$
\tilde { M } = M + { \cal O } ( c ^ { - 3 } ) ,
$$

in which $M$ is the total mass-energy of the system, as defined in general relativity by Eq. (7.63). We also find that to leading order in a post-Newtonian expansion,

$$
\tilde { \cal Z } ^ { j k } = I ^ { j k } + { \cal O } ( c ^ { - 2 } ) ,
$$

where $\begin{array} { r } { I ^ { j k } : = \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x } \end{array}$ is the Newtonian quadrupole-moment tensor.

Similarly, the solution to the scalar wave equation can be expressed as

$$
\phi = \phi _ { 0 } + \frac { 2 \tilde { G } } { c ^ { 2 } R } \biggl [ \mathcal { T } _ { \mathrm { s } } + \frac { 1 } { c } \dot { \mathcal { T } } _ { \mathrm { s } } ^ { j } N _ { j } + \frac { 1 } { 2 c ^ { 2 } } \ddot { \mathcal { T } } _ { \mathrm { s } } ^ { j k } N _ { j } N _ { k } + O ( c ^ { - 3 } ) \biggr ] ,
$$

where

$$
\begin{array} { r l } & { \mathcal { Z } _ { s } ( \tau ) : = \displaystyle \int _ { \mathcal { M } } \tau _ { s } ( \tau , x ) d ^ { 3 } x \ , } \\ & { \mathcal { Z } _ { s } ^ { j } ( \tau ) : = \displaystyle \int _ { \mathcal { M } } \tau _ { s } ( \tau , x ) x ^ { j } d ^ { 3 } x \ , } \\ & { \mathcal { Z } _ { s } ^ { j k } ( \tau ) : = \displaystyle \int _ { \mathcal { M } } \tau _ { s } ( \tau , x ) x ^ { j } x ^ { k } d ^ { 3 } x \ , } \end{array}
$$

are the multipole moments of the scalar source $\tau _ { \mathrm { s } }$ . Because this does not satisfy any conservation equation, the monopole moment $\mathcal { T } _ { \mathrm { s } }$ cannot be expected to be constant, and the dipole moment $\mathcal { T } _ { \mathrm { s } } ^ { j }$ cannot be set equal to zero.

To evaluate these moments it is useful to introduce an effective energy density $\mu$ defined by the relation

$$
c ^ { - 2 } \tau _ { \mathrm { s } } = \frac { \zeta \phi _ { 0 } } { 1 - \zeta } \biggl [ c ^ { - 2 } \tilde { \tau } ^ { 0 0 } - \frac { 1 } { c ^ { 2 } } \mu + { \cal O } ( c ^ { - 3 } ) \biggr ] .
$$

This expresses the fact, apparent from Eqs. (13.144), that $\tau _ { \mathrm { s } }$ and $\zeta \phi _ { 0 } \tilde { \tau } ^ { 0 0 } / ( 1 - \zeta )$ are equal to each other to leading order in a post-Newtonian expansion, and differ by a post-Newtonian correction. We have

$$
\mu = \rho ^ { * } \bigg [ v ^ { 2 } + \Big ( \frac { 1 } { 2 } + 2 \lambda \Big ) U \bigg ] + 3 p - \frac { 1 } { 4 \pi G c ^ { 2 } } \bigg ( \frac { 7 } { 4 } - 3 \zeta + \lambda \bigg ) \nabla ^ { 2 } U ^ { 2 } .
$$

We define multipole moments associated with $\mu$

$$
\begin{array} { c } { { \displaystyle \mathcal E ( \tau ) : = \int _ { \mathcal M } \mu ( \tau , x ) d ^ { 3 } x \ : , } } \\ { { \displaystyle \mathcal E ^ { j } ( \tau ) : = \int _ { \mathcal M } \mu ( \tau , x ) x ^ { j } d ^ { 3 } x \ : , } } \\ { { \displaystyle \mathcal E ^ { j k } ( \tau ) : = \int _ { \mathcal M } \mu ( \tau , x ) x ^ { j } x ^ { k } d ^ { 3 } x \ : , } } \end{array}
$$

and write

$$
\begin{array} { l } { \displaystyle { \mathcal { T } _ { \mathrm { s } } = \frac { \zeta \phi _ { 0 } } { 1 - \zeta } \bigg [ \tilde { M } - \frac { 1 } { c ^ { 2 } } \mathcal { E } + O ( c ^ { - 3 } ) \bigg ] , } } \\ { \displaystyle { \mathcal { T } _ { \mathrm { s } } ^ { j } = \frac { \zeta \phi _ { 0 } } { 1 - \zeta } \bigg [ - \frac { 1 } { c ^ { 2 } } \mathcal { E } ^ { j } + O ( c ^ { - 3 } ) \bigg ] , } } \\ { \displaystyle { \mathcal { T } _ { \mathrm { s } } ^ { j k } = \frac { \zeta \phi _ { 0 } } { 1 - \zeta } \bigg [ \tilde { \mathcal { Z } } ^ { j k } - \frac { 1 } { c ^ { 2 } } \mathcal { E } ^ { j k } + O ( c ^ { - 3 } ) \bigg ] . } } \end{array}
$$

From Eq. (13.159) we find that

$$
\begin{array} { l } { { \displaystyle \mathcal { E } = \int \rho ^ { * } \biggl [ v ^ { 2 } + \Bigl ( \frac { 1 } { 2 } + 2 \lambda \Bigr ) U + 3 p / \rho ^ { * } \biggr ] d ^ { 3 } x \ , } } \\ { { \displaystyle \mathcal { E } ^ { j } = \int \rho ^ { * } \biggl [ v ^ { 2 } + \Bigl ( \frac { 1 } { 2 } + 2 \lambda \Bigr ) U + 3 p / \rho ^ { * } \biggr ] x ^ { j } d ^ { 3 } x \ , } } \end{array}
$$

and we shall not need an explicit expression for $\mathcal { E } ^ { j k }$ ; the term involving $\nabla ^ { 2 } U ^ { 2 }$ in $\mu$ makes no $\mathcal { R }$ -independent contributions to the monopole and dipole moments.

Making the substitutions in Eq. (13.156) returns

$$
\phi / \phi _ { 0 } = 1 + { \frac { 2 \zeta G } { c ^ { 2 } R } } \Bigg [ M - { \frac { 1 } { c ^ { 2 } } } A ( \tau , N ) + { \cal O } ( c ^ { - 3 } ) \Bigg ] ,
$$

where

$$
\mathcal { A } : = \mathcal { E } ( \tau ) + \frac { 1 } { c } \dot { \mathcal { E } } ^ { j } ( \tau ) N _ { j } - \frac { 1 } { 2 } \ddot { I } ^ { j k } ( \tau ) N _ { j } N _ { k }
$$

is the radiative piece of the scalar field. To arrive at this result we have incorporated the information displayed in Eqs. (13.154) and (13.155). Note that the term involving the dipole moment $\mathcal { E } ^ { j }$ has been retained in the expression for $\mathcal { A }$ , in spite of the fact that it is formally of order $c ^ { - 3 }$ and therefore of the same order as the neglected terms in Eq. (13.163). The reason for this is revealed below.

We are now ready to convert these results into a description of gravitational waves in scalar–tensor gravity. As was reviewed back in Secs. 13.4.1 and 13.4.2, the gravitationalwave polarizations can be extracted from potentials $h ^ { \alpha \beta }$ defined in terms of the physical metric $g _ { \alpha \beta }$ by Eq. (13.77). The relation with $\tilde { h } ^ { \alpha \beta }$ is provided by Eqs. (13.102) and (13.115), and we get

$$
h ^ { \alpha \beta } = ( \phi _ { 0 } / \phi ) \tilde { h } ^ { \alpha \beta } + ( 1 - \phi _ { 0 } / \phi ) \eta ^ { \alpha \beta } .
$$

Making the substitutions from Eqs. (13.151) and (13.163), we arrive at

$$
\begin{array} { l } { { h ^ { 0 0 } = 2 ( 2 - 3 \zeta ) \displaystyle \frac { G M } { c ^ { 2 } R } + \displaystyle \frac { G } { c ^ { 4 } R } \biggl [ 2 ( 1 - \zeta ) \ddot { I } ^ { j k } N _ { j } N _ { k } + 2 \zeta \mathcal { A } + O ( c ^ { - 1 } ) \biggr ] \ : , } } \\ { { h ^ { 0 j } = \displaystyle \frac { G } { c ^ { 4 } R } \biggl [ 2 ( 1 - \zeta ) \ddot { I } ^ { j k } N _ { k } + O ( c ^ { - 1 } ) \biggr ] \ : , } } \\ { { h ^ { j k } = 2 \zeta \displaystyle \frac { G M } { c ^ { 2 } R } \delta ^ { j k } + \displaystyle \frac { G } { c ^ { 4 } R } \biggl [ 2 ( 1 - \zeta ) \ddot { I } ^ { j k } - 2 \zeta \mathcal { A } \delta ^ { j k } + O ( c ^ { - 1 } ) \biggr ] \ : . } } \end{array}
$$

The assignments of Eqs. (13.149) and (13.150) ensure that the stationary terms, involving the total mass-energy $M$ , agree with the general expression of Eq. (13.78). Comparison with Eq. (13.80) then allows us to read off the radiative fields $C , D ^ { j }$ , and $A ^ { j k }$ , which are decomposed into irreducible pieces as in Eqs. (13.81). We get

$$
\begin{array} { r l } & { \quad A = 2 ( 1 - \zeta ) ^ { \bar { j } p p } - 6 \zeta \mathcal { A } , } \\ & { \quad B = 3 ( 1 - \zeta ) ^ { \bar { j } ( i j k ) } N _ { j } N _ { k } , } \\ & { \quad C = 2 ( 1 - \zeta ) ^ { \bar { j } ( i j k ) } N _ { j } N _ { k } + \frac { 2 } { 3 } ( 1 - \zeta ) ^ { \bar { j } p p } + 2 \zeta \mathcal { A } , } \\ & { \quad D = 2 ( 1 - \zeta ) ^ { \bar { j } ( i j k ) } N _ { j } N _ { k } + \frac { 2 } { 3 } ( 1 - \zeta ) ^ { \bar { j } p p } , } \\ & { \quad A _ { \mathrm { r } } ^ { j } = 2 ( 1 - \zeta ) P _ { j } ^ { j } \tilde { l } ^ { ( j k ) } N _ { k } , } \\ & { \quad D _ { \mathrm { r } } ^ { j } = 2 ( 1 - \zeta ) P _ { j } ^ { j } \tilde { l } ^ { ( j k ) } N _ { k } , } \\ & { \quad A _ { \mathrm { r } } ^ { j } = 2 ( 1 - \zeta ) ^ { \bar { j } } \tilde { l } _ { \mathrm { r } } ^ { j p } . } \end{array}
$$

in which $P _ { j k } : = \delta _ { j k } - N _ { j } N _ { k }$ is the projector to the subspace transverse to $N ^ { j }$ . Finally, Eq. (13.89) allows us to obtain the gauge-invariant gravitational-wave amplitudes,

$$
\begin{array} { r l } & { { \cal A } _ { \mathrm { S } } = 2 \zeta { \cal A } , } \\ & { { \cal A } _ { \mathrm { L } } = 0 , } \\ & { { \cal A } _ { \mathrm { V } } ^ { j } = 0 , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { j k } = 2 ( 1 - \zeta ) \ddot { I } _ { \mathrm { T T } } ^ { j k } . } \end{array}
$$

We see that in addition to the familiar transverse-tracefree polarizations involving the quadrupole-moment tensor, scalar–tensor gravity gives rise to a scalar mode involving the combination of monopole, dipole, and quadrupole moments contained in $\mathcal { A }$ .

The generation of monopole and dipole waves in scalar–tensor gravity is a major departure from general relativity, and we conclude this section with a discussion of these new features. The monopole and dipole moments $\mathcal { E }$ and $\mathcal { E } ^ { j }$ are defined by Eq. (13.162), and for the purpose of this discussion we evaluate them for a system of well-separated bodies, using techniques developed in Chapter 9 – refer to Sec. 9.3.6. We find that the monopole moment evaluates to

$$
\mathcal { E } = \sum _ { A } \biggl [ 2 \mathcal { T } _ { A } - ( 1 + 4 \lambda ) \Omega _ { A } + 3 P _ { A } + m _ { A } v _ { A } ^ { 2 } + \frac { 1 } { 2 } ( 1 + 4 \lambda ) m _ { A } U _ { - A } \biggr ] ,
$$

in which $\mathcal { T } _ { A }$ is the total kinetic energy of body $A , \Omega _ { A }$ its gravitational potential energy, $P _ { A }$ the integrated pressure, and $U _ { \neg A }$ the gravitational potential of the external bodies evaluated at the position of body $A$ . This becomes

$$
\mathcal { E } = - 2 ( 1 + 2 \lambda ) \sum _ { A } \Omega _ { A } + \sum _ { A } M _ { A } v _ { A } ^ { 2 } + ( 1 + 4 \lambda ) \sum _ { A } \sum _ { B \ne A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } + O ( c ^ { - 2 } )
$$

after we make use of the virial theorem of Eq. (13.16), insert the familiar expression for the external potential, and make the replacements $m _ { A } = M _ { A } + O ( c ^ { - 2 } )$ . For a binary system the monopole moment reduces to

$$
\mathcal { E } = - 2 ( 1 + 2 \lambda ) ( \Omega _ { 1 } + \Omega _ { 2 } ) + \eta m \bigg [ v ^ { 2 } + ( 1 + 4 \lambda ) \frac { G m } { r } \bigg ] + O ( c ^ { - 2 } ) ,
$$

in which $m : = M _ { 1 } + M _ { 2 } , \eta : = M _ { 1 } M _ { 2 } / m ^ { 2 } , r : = | { \pmb r } _ { 1 } - { \pmb r } _ { 2 } |$ , and $\pmb { v } : = | \pmb { v } _ { 1 } - \pmb { v } _ { 2 } |$ . The monopole moment contains a contribution from each body’s gravitational potential energy $\Omega _ { A }$ , and neglecting tidal interactions between bodies, this is constant for bodies in hydrodynamical equilibrium; these terms do not participate in the generation of gravitational waves. The remaining terms, however, coming from the orbital motion of each body, are time-dependent and do participate in the production of gravitational waves. It is easy to see that the monopole term in $\mathcal { A }$ is of the same order of magnitude as the quadrupole term $\frac { 1 } { 2 } \ddot { I } ^ { j k } N _ { j } N _ { k }$ .

After making use of the virial theorem, we find that the dipole moment is given by

$$
\begin{array} { l } { { \displaystyle { \mathcal E } ^ { j } = - 2 ( 1 + 2 \lambda ) \sum _ { A } \Omega _ { A } r _ { A } ^ { j } + \sum _ { A } M _ { A } v _ { A } ^ { 2 } r ^ { j } } } \\ { { \displaystyle ~ + ( 1 + 4 \lambda ) \sum _ { A } \sum _ { B \ne A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } r _ { A } ^ { j } + O ( c ^ { - 2 } ) } } \end{array}
$$

for a system of well-separated bodies. For a binary system this reduces to

$$
\mathcal { E } ^ { j } = - 2 ( 1 + 2 \lambda ) \eta m c ^ { 2 } S r ^ { j } - \eta \Delta m \biggl [ v ^ { 2 } + ( 1 + 4 \lambda ) \frac { G m } { 2 r } \biggr ] r ^ { j } + O ( c ^ { - 2 } ) ,
$$

where $r : = r _ { 1 } - r _ { 2 }$ , $\Delta : = ( M _ { 1 } - M _ { 2 } ) / m$ , and

$$
{ \cal S } : = \frac { \Omega _ { 1 } } { M _ { 1 } c ^ { 2 } } - \frac { \Omega _ { 2 } } { M _ { 2 } c ^ { 2 } } .
$$

We find that the dipole moment also contains terms involving the gravitational potential energies in addition to orbital terms. These terms come now with a time-dependent separation vector $r$ , and they do participate in the production of gravitational waves. For weakly bound bodies, $\Omega _ { A } / ( M _ { A } c ^ { 2 } )$ is of the same order of magnitude as $( v _ { A } / c ) ^ { 2 }$ and $G M _ { B } / ( c ^ { 2 } r _ { A B } )$ , and the dipole term in $\mathcal { A }$ can be seen to be a factor $v _ { c } / c$ smaller than the monopole and quadrupole terms (with $v _ { c }$ denoting a characteristic orbital velocity). In this case the dipole term should be lumped together with the error terms of order $c ^ { - 1 }$ in Eq. (13.166).

The situation changes dramatically when the bodies are compact, as in the case of neutron stars. In this situation $\Omega _ { A } / ( M _ { A } c ^ { 2 } ) \sim 0 . 1$ , and the internal terms strongly dominate over the orbital terms in the dipole moment. In this case we find that the dipole term in $\mathcal { A }$ is a factor $c / v _ { c }$ larger than the monopole and quadrupole terms. The orbital motion of compact bodies, therefore, can in principle give rise to gravitational waves that are dominantly dipolar, thanks to the dependence of the dipole moment on each body’s gravitational potential energy. In practice, however, the effect can be strongly suppressed. For a binary system the dipolar radiation is controlled by the difference in $\Omega / ( M c ^ { 2 } )$ between bodies, and it is suppressed whenever the bodies are very similar. This occurs, for example, for most binary pulsars, which involve neutron stars with masses that are tightly clustered around $1 . 4 M _ { \odot }$ , producing very small values of $s$ . Furthermore, $\mathcal { A }$ is multiplied by $\zeta$ in the gravitational-wave field, and $\zeta$ is already constrained to be small by solar-system measurements of the Shapiro time delay. As a result, binary neutron-star systems have yet to provide interesting tests of scalar–tensor gravity, except for theories that come with anomalously large values of the parameter $\lambda$ . It is possible, however, to test scalar–tensor gravity with the few binary-pulsar systems that are known to involve a white-dwarf companion. With $\Omega _ { A } / ( M _ { A } c ^ { 2 } ) \sim 1 0 ^ { - 4 }$ for a white dwarf, $s$ is numerically large, and the emission of dipole radiation can be important. Data from one such system, known as $\mathbf { J 1 7 3 8 + } 0 3 3 3$ , provides a bound on $\zeta$ that is beginning to compete with constraints from the solar system.

# 13.6 Bibliographical notes

The literature on alternative theories of gravity and their experimental tests is far too vast to attempt even a partial summary. At the risk of self-promotion, we refer the reader to the book Theory and Experiment in Gravitational Physics by one of us (CMW) (1993), which gives a lot more detail than we were able to provide in this chapter. In addition, Will’s Living Reviews article (2006b) describes the experimental situation up to that time; it is scheduled to be updated by 2014. Another useful resource is Will (2010), an annotated compilation of almost 100 references on tests of gravitational theories.

Nordstrom’s relativistic theory of gravity, mentioned in the introduction to the chapter, is ¨ published as Nordstrom (1913). Whitehead’s theory, involving a non-dynamical Minkowski ¨ metric in addition to a dynamical metric, was proposed in his 1922 book; its multiple deaths are described in Gibbons and Will (2008). The experimental basis of general relativity and alternative theories in the early nineteen sixties is reviewed in Bertotti, Brill, and Krotkov (1962) and Whitrow and Morduch (1965). The Brans–Dicke theory originates in their 1961 article, which built upon previous work by Fierz (1956) and Jordan (1959).

The parameterized post-Newtonian framework, reviewed in Sec. 13.2, was first initiated in Eddington (1922). It was developed systematically by Nordtvedt (1968a and 1968b) for systems of point particles, and by Thorne and Will (1970) and Will (1971a, 1971b, and 1971c) for perfect-fluid systems. The two versions of the formalism were consolidated in Will and Nordtvedt (1972a and 1972b).

The measurement of the PPN parameter $\gamma$ on galactic scales using gravitational lensing, described in Sec. 13.3.2, is reported in Bolton, Rappaport, and Burles (2006). The effect on the lunar orbit of a failure of the strong equivalence principle (Sec. 13.3.3) was first discovered by Nordtvedt (1968c), who also proposed a detection scheme based on laser ranging. The state of the art on lunar laser ranging and the measurement of the Nordtvedt effect (Box 13.2) is summarized in Nordtvedt (1999), Williams, Turyshev, and Boggs (2009), and Merkowitz (2010). The Eot-Wash test of the weak equivalence principle on ¨ a mini-Moon and mini-Earth system was described in Baessler et al. (1999). Tests of the Nordtvedt effect on pulsar–white dwarf systems were reported by Stairs et al. (2005).

The discussion of gravitational-wave polarizations in alternative theories of gravity, provided in Sec. 13.4.2, is based on Eardley et al. (1973).

Our treatment of scalar–tensor gravity in Sec. 13.5 was inspired by the seminal 1992 paper by Damour and Esposito-Farese. Dicke’s argument of Box 13.4, connecting the variation \` of $G _ { \mathrm { e f f } }$ to the Nordtvedt effect, originated in Dicke (1970); an expanded version of the argument is presented in the Appendix of Will (1971a). The proof that the stationary black holes of scalar–tensor gravity are the same as those of general relativity (Exercise 13.5) was formulated by Hawking (1972) in the case of Brans–Dicke theory, and by Sotiriou and Faraoni (2012) in the general case.

# 13.7 Exercises

13.1 Consider a semi-conservative theory of gravity, with $\alpha _ { 3 } = \zeta _ { n } = 0$ . Using the PPN equation of hydrodynamics, Eq. (13.8), and making use of the method described in Sec. 8.4.6, show that the total momentum defined by

$$
\begin{array} { l } { { P ^ { j } : = \displaystyle \int \rho ^ { * } v ^ { j } \Big [ 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi + p / \rho ^ { * } \Big ) \Big ] d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \Phi ^ { j } d ^ { 3 } x ~ } } \\ { { \displaystyle ~ - \frac { 1 } { 2 c ^ { 2 } } \alpha _ { 1 } \int \rho ^ { * } ( v ^ { j } + w ^ { j } ) U d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \alpha _ { 2 } \int \rho ^ { * } \big ( \partial _ { t j } X - w ^ { k } \partial _ { j k } X \big ) d ^ { 3 } x } } \\ { { \displaystyle ~ + O ( c ^ { - 4 } ) } } \end{array}
$$

is conserved.