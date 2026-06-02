# CHAPTER X.

# PERTURBATIONS-ANALYTICAL METHOD.

203.Introductory Remarks. The subject of the mutual perturbations of the motions of the heavenly bodies has been one to which many of the great mathematicians, from Newton's time on,have devoted a great deal of attention. It is needless to say that the problem is very difficult and that many methods of attacking it have been devised. Since the general solutions of the problem have not been obtained it has been necessary to treat special classes of perturbations by special methods. It has been found convenient to divide the cases which arise in the solar system into three general classes, $( a )$ the Lunar Theory and satellite theories; $( b )$ the mutual perturbations of the planets；and $( c )$ the perturbations of comets by planets. The method which will be given in this chapter is applicable to the planetary theories,and it will be shown in the proper places why it is not applicable to the other cases. References were given in the last chapter to treatises on the Lunar Theory,especially to those of Tisserand and Brown. Some hints will be given in this chapter on the method of computing the perturbations of comets.

The chief difficulties which arise in getting an understanding ot the theories of perturbations come from the large number of variables which it is necessary to use，and the very long trans\~ formations which must be made,in order to put the equations in & form suitable for numerical computations. It is not possible, because of the lack of space,to develop here in detail the explicit expressions adapted to computation；and, indeed,it is not desired to emphasize this part,for it is much more important to get an accurate understanding of the nature of the problem, the mathe. matical features of the methods employed,the limitations which are necessary，the exact places where approximations are introduced,if at all,and their character, the origin of the various sorts of terms,and the foundations upon which the celebrated theorems regarding the stability of the solar system rest.

There are two general methods of considering perturbations, $( a )$ as the variations of the coordinates of the various bodies, and $( b )$ as the variations of the elements of their orbits. These two conceptions were explained in the beginning of the preceding chapter. Their analytical development was begun by Euler and Clairaut and was carried to a high degree of perfection by Lagrange and Laplace. Yet there were points at which pure assumptions were made,it having become possible to establish completely the legitimacy of the proceedings,under the proper restrictions,only during the latter half of the nineteenth century by the aid of the work in pure Mathematics of Cauchy，Weierstrass,and Poincaré.

204.Illustrative Example. The mathematical basis for the theory of perturbations is often obscured by the large number of variables and the complicated formulas which must be used. Many of the essential features of the method of computing perturbations can be illustrated by simpler examples which are not subject to the complexities of many variables and involved formulas. One will be selected in which the physical relations are also simple.

Consider the solution of

$$
{ \frac { d ^ { 2 } x } { d t ^ { 2 } } } + k ^ { 2 } x = - \mu \left( { \frac { d x } { d t } } \right) ^ { 3 } + \nu \cos l t ,
$$

where $k ^ { 2 } , \mu , \nu ,$ and $\iota$ are positive constants. If $\pmb { \mu }$ and $\pmb { \nu }$ were zero the differential equation would be that which defines simple harmonic motion. It arises in many physical problems,such as that of the simple pendulum,and of all classes of musical instruments. In order to make the interpretation definite,suppose it belongs to the problem of the vibrations of a tuning fork. The first term in the right member may be interpreted as being due to the resistance of the medium in which the tuning fork vibrates. It is not asserted,of course, that the resistance to the vibrations of a tuning fork varies as the third power of the velocity. An odd power is taken so that the differential equation will have the same form whether the motion is in the positive or negative direction,and the frst power is not taken because then the differential equation would be linear and could be completely integrated in finite terms without any difficulty.

The left member of equation (1） will be considered as defining the undisturbed motion of the tuning fork. The first term on the right introduces a perturbation which depends upon the veiocity of the tuning fork；the second term on the right introduces a perturbation which is independent of the position and velocity of the tuning fork. The first is analogous to the mutual perturbations of the planets,which depend upon their relative positions;the second is more of the nature of the forces which produce the tides,for they are exterior to the earth. The tides are defined by equations analogous to (1).

In order to have equation (1) in the form of the equations which arise in the theory of perturbations,let

$$
\pmb { x } = x _ { 1 } , \frac { d \pmb { x } } { d t } = x _ { 2 } .
$$

Then (1） becomes

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } - x _ { 2 } = 0 , } \\ { \displaystyle \frac { d x _ { 2 } } { d t } + k ^ { 2 } x _ { 1 } = - \mu x _ { 2 } ^ { 3 } + \nu \cos { l t } . } \end{array} \right.
$$

The corresponding differential equations for undisturbed motion are

$$
\left\{ { \begin{array} { l } { \displaystyle { \frac { d x _ { 1 } } { d t } } - x _ { 2 } = 0 , } \\ { \displaystyle { \frac { d x _ { 2 } } { d t } } + k ^ { 2 } x _ { 1 } = 0 . } \end{array} } \right.
$$

Equations (4) are easily integrated,and their general solution is

$$
\left\{ \begin{array} { l l } { x _ { 1 } = + \alpha \cos { k t } + \beta \sin { k t } , } \\ { x _ { 2 } = - \ k \alpha \sin { k t } + k \beta \cos { k t } , } \end{array} \right.
$$

where $\pmb { \alpha }$ and $\beta$ are the arbitrary constants of integration. In the terminology of Celestial Mechanics, $\pmb { \alpha }$ and $\beta$ are the elements of the orbit of the tuning fork.

Now consider the problem of finding the solutions of equations (3)． Physically speaking, the elements $_ \alpha$ and $\beta$ must be so varied that the equations shall be satisfied for all values of $t .$ Mathematically considered，equations (5) are relations between the original dependent variables $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { 2 }$ ，and the new dependent variables $_ { \pmb { \alpha } }$ and $\beta$ which make it possible to transform the differential equations (3) from one set of variables to the other. This would be true whether (5) were solutions of (4) or not,but since (5)are solutions of (4) and (4) are a part of (3),a number of terms drop out after the transformation has been made. On regarding (5)as a set of equations relating the variables $x _ { 1 }$ and $x _ { 2 }$ to $_ { \pmb { \alpha } }$ and $\beta$ ， and making direct substitution in (3),it is found that

$$
\left\{ \begin{array} { l } { { + \cos k t { \frac { d \alpha } { d t } } + \sin k t { \frac { d \beta } { d t } } = 0 , } } \\ { { - \sin k t { \frac { d \alpha } { d t } } + \cos k t { \frac { d \beta } { d t } } = \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } + { \frac { \nu } { k } } \cos l t . } } \end{array} \right.
$$

These equations are ineay in $\frac { d \alpha } { \hat { d t } }$ and $\frac { d \beta } { d t }$ and can be solved for these derivatives because the determinant of their coefficients is unity. The solution is

$$
\begin{array} { r } { \left\{ \cfrac { d \alpha } { d t } = - \ \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } \sin k t - \frac { \nu } { k } \cos l t \sin k t , \right. } \\ { \left. \cfrac { d \beta } { d t } = + \ \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } \cos k t + \frac { \nu } { k } \cos l t \cos k t . \right. } \end{array}
$$

The problem of solving (7) is as diffcult as that of solving (3) because their right members involve the unknown quantities $\pmb { \alpha }$ and $\beta$ in as complicated manner as ${ \boldsymbol { \mathscr { x } } } _ { 1 }$ and $\pmb { x _ { 2 } }$ enter the right members of (3). But suppose $\pmb { \mu }$ and $\pmb { \nu }$ are very small； then,since they enter as factors in the right members of equations (7),the dependent variables $_ \alpha$ and $\beta$ change very siowiv. Consequently, for a considerable time they will be given with sufficient approximation if equations (7) are integrated regarding them as constants in the right members. To assist in seeing this mathematically consider the simpler equation

$$
\frac { d \alpha } { d t } = \mu \alpha ( 1 + k \cos k t ) .
$$

The solution of this equation is

$$
\alpha = C e ^ { \mu ( t + \sin k t ) } ,
$$

where $\pmb { C }$ is the constant of integration. If the right member of this equation is expanded, the expression for $\pmb { \alpha }$ becomes

$$
\alpha = C \left[ 1 + \mu ( t + \sin k t ) + { \frac { \mu ^ { 2 } } { 2 } } ( t + \sin k t ) ^ { 2 } + \cdot \cdot \cdot \right] .
$$

If $\mu$ is very small and if $\pmb { t }$ is not too great the right member of this equation is nearly equal to its first two terms.If it were not for the term $t$ which is not in the trigonometric function no limitations on $\pmb { t }$ would be necessary. But in general such limitations are necessary;and in most cases,though not in the present one, they are necessary in order to secure convergence of the series.

It is observed that the solution (9) is in reality a power series in the parameter $\pmb { \mu } ,$ and the coefficients involve t. If it is desired equation (8) can be integrated directly as a power series in $\pmb { \mu }$ The process is, in fact,a general one which can be used in solving (7),and equations (1O),which follow,are the first terms of the :solution. The conditions of validity of this method of integration :are given in Art.207.

The fact that when $\pmb { \mu }$ is very small $\pmb { \alpha }$ and $\beta$ may be regarded .as constants in the right members of (7) for not too great values .of $\pmb { t }$ can be seen from a physical illustration. Consider the per-·turbation theory. The changes in the elements of an orbit depend upon the elements of the orbits of the mutually disturbing bodies and upon the relative positions of the bodies in their orbits. It is intuitionally clear that only a slight error in the computation of -the mutual disturbances of two planets would be committed if .constant elements were used which differ a little, say a degree in ·the case of angular elements, from the true slowly changing ones.

If equations (7） are integrated regarding $\pmb { \alpha }$ and $\pmb \beta$ as constants in the right members,it is found that

$$
\{ \begin{array} { c } { { \alpha _ { { \mathrm { - } } } \alpha _ { { \mathrm { - } } } = \alpha _ { { \mathrm { - } } } \mu \displaystyle \sum _ { i = 0 } ^ { \infty }  \frac { \partial \alpha _ { i } } { \partial \beta } ( \alpha _ { i } ^ { \mathrm { a } } + \beta \beta ) t + \frac { \partial } { \partial \alpha _ { i } } ( \alpha _ { i } ^ { \mathrm { a } } + \beta \beta ) ( \cos { 2 \mathrm { i } \mathrm { - } } 1 )  } } \\ { {  ( \frac { \partial \beta } { \partial \beta } ) ( \frac { \partial \beta } { \partial \alpha } ) - \beta  ( \cos { 4 \mathrm { i } \mathrm { d } \mathrm { - } } 1 ) } } \\ { { - \frac { \partial \alpha _ { i } ^ { \mathrm { c } } } { \partial \beta } ( \alpha _ { i } ^ { \mathrm { a } } - \beta ) ( \cos { 2 \mathrm { i } \mathrm { \backslash } \mathrm { ~ } } \alpha _ { i } ^ { \mathrm { a } } - 1 ) } } \\ { { - \frac { \partial \alpha _ { i } ^ { \mathrm { c } } } { \partial \beta } ( \alpha _ { i } ^ { \mathrm { a } } + \frac { \partial \alpha _ { i } ^ { \mathrm { c } } } { \partial \beta } ) ( \cos { 2 \mathrm { i } \mathrm { \backslash } \mathrm { ~ } } \alpha _ { i } ^ { \mathrm { a } } - 1 ) } } \\ { { + \frac { \partial } { 2 \mathrm { i } \mathrm {  { \backslash } \mathrm { } \mathrm { ~ } } \alpha _ { i } ^ { \mathrm { a } } } ( \alpha _ { i } ^ { \mathrm { a } } + \frac { \partial \alpha _ { i } ^ { \mathrm { c } } } { \partial \beta } ) ( \cos { 2 \mathrm { i } \mathrm { \backslash } \mathrm { ~ } } \alpha _ { i } ^ { \mathrm { a } } - 1 ) } } \\ { { - \frac { \partial \alpha _ { i } ^ { \mathrm { c } } } { \partial \beta } ( \alpha _ { i } ^ { \mathrm { a } } + \beta ) ( \cos { \mathrm { i } \mathrm { \backslash } \mathrm { ~ } } \alpha _ { i } ^ { \mathrm { b } } - 1 ) } } \\   \beta = \delta _ { { \mathrm { + } } } + \mu \displaystyle \beta ^ { \mathrm { a } } \{ - \frac  \partial \alpha _ { i } ^ { \mathrm { a } } ( \alpha _ { i } ^ { \mathrm { a } } + \beta ) t - \frac { \partial }  \ \end{array}
$$

where $\pmb { \alpha } _ { 0 }$ and $\beta _ { 0 }$ are the values of $_ { \pmb { \alpha } }$ and $\beta$ respectively at $t = 0$ When these values of $_ { \pmb { \alpha } }$ and $\beta$ are substituted in (5) the values of ${ \pmb x } _ { 1 }$ and ${ \pmb x } _ { \mathbf { 2 } }$ are determined approximately for all values of $t$ which are not too remote from the initial time.

Consider equations (1O). The right member of each of them has a term which contains $t$ only asa simple factor,while elsewhere $\pmb { t }$ appears only in the sine and cosine terms. The terms which are proportional to $t$ seem to indicate that $\pmb { \alpha }$ and $\beta$ increase or decrease indefinitely with the time；but it must be remembered that equations (10) are only approximate expressions for $_ \alpha$ and $\beta _ { ; }$ ， which are useful only for a limited time. It might be that the rigorous expressions would contain higher powers of $t ,$ and that the sums would have bounded values, just as

$$
\sin t = t - { \frac { t ^ { 3 } } { 3 ! } } + { \frac { t ^ { 5 } } { 5 ! } } - \cdots
$$

is an expression whose numerical value does not exceed unity, though a consideration of the first term alone would lead to the conclusion that it becomes indefinitely great with t. On the other hand the presence of terms which increase proportionally to the time may indicate an actual indefinite increase of the elements $_ { \pmb { \alpha } }$ and $\beta$ .For example,it was found in the preceding chapter that the line of nodes and the apsides of the moon's orbit respectively regress and advance continually. The terms which change proportionally to $t$ &re called secular terms.

The right members of equations (10) also contain periodic terms having the periods +and $\frac { 2 \pi } { l - k }$ These are known as periodic terms. If $\imath$ and $\pmb { k }$ are nearly equal the terms which involve sines or cosines of $( l - k ) t$ have very long periods,and are called long period terms. Sometimes terms arise which are the products of $\pmb { t }$ and periodic terms. These mixed terms are called Poisson terms because they were encountered by Poisson in the discussion of the variations of the major axes of the planetary orbits. If (10) are substituted in (5) the resulting expressions for $\pmb { x _ { 1 } }$ and ${ \boldsymbol { \mathscr { x } } } _ { 2 }$ contain Poisson terms but no secular terms.

The physical interpretation of equations (1O) is simple. The elements $_ { \alpha }$ and $\beta$ continually decrease because of the secular terms; that is,the amplitudes of the oscillations indicated in (5） continually diminish. This reduction is entirely due to the resistance to the motion as is shown by the fact that these terms contain the coefficient $\mu$ as a factor. There are terms in $x _ { 1 }$ and ${ \pmb x } _ { 2 }$ of period three times and five times the undisturbed period which are also due to the resistance. And the periodic disturbing force introduces in $_ \alpha$ and $\beta$ terms whose periods depend both on the period of the disturbing force and also on the natural period of the tuning fork.But it is noticed that the periods of the terms which they introduce into the expressions for $\pmb { x } _ { 1 }$ and $x _ { 2 }$ are the period of the disturbing force and the natural period of the tuning fork.

205.Equations in the Problem of Three Bodies. Consider the motion of two planets, $m _ { 1 }$ and $m _ { 2 } ,$ ，with respect to the sun, ${ \pmb S } .$ Take the center of the sun as origin and let the coordinates of $\boldsymbol { m } _ { 1 }$ be $( x _ { 1 } , \ y _ { 1 } , \ z _ { 1 } )$ ，and of $m _ { 2 }$ ， $( x _ { 2 } , \ y _ { 2 } , \ z _ { 2 } )$ .Let the distances of $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ from the sun be $\mathbf { \Delta } \mathbf { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ respectively，and let $r _ { 1 , \mathrm { ~ 2 ~ } }$ represent the distance from $m _ { 1 }$ to $m _ { 2 }$ ，Then the differential equations of motion,as derived in Art.148,are

$$
\{ \begin{array} { l l } { \frac { d \hat { x } _ { 0 2 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ A ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 0 2 } } { d t } , } \\ { \frac { d \hat { x } _ { 0 1 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 1 2 } } { d t } , } \\ { \frac { d \hat { x } _ { 0 1 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 0 2 } } { d t } , } \\ { \frac { d \hat { x } _ { 1 2 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 1 2 } } { d t } , } \\ { \frac { d \hat { x } _ { 2 2 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 0 2 } } { d t } , } \\ { \frac { d \hat { x } _ { 0 1 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac { d \hat { x } _ { 0 2 } } { d t } , } \\  \frac { d \hat { x } _ { 0 2 } } { d t } + k ^ { \prime } ( \hat { x } + \mathbf { u } _ { \mathrm { u } } ^ { \mathrm { s } } \cdot \mathbf { x } _ { \mathrm { u } } ^ { \mathrm { ~ B ~ } } ) = m _ { \mathrm { s } } \frac  d  \end{array}
$$

The right members of equations (11） are multiplied by the factors $\pmb { m _ { 1 } }$ and $\mathbf { \nabla } m _ { 2 }$ which are very small compared to $s$ ; therefore they will be of slight importance in comparison with the terms on the left which come from the attraction of the sun,at least for a considerable time.If $m _ { 1 }$ and $\mathbf { \nabla } m _ { 2 }$ are put equal to zero in the right members,the first three equations and the second three form two sets which are independent of each other,and the problem for each set of three equations reduces to that of two bodies,and can be completely solved.

It will be advantageous to reduce the six equations (11) of the second order to twelve of the first order.Let

$$
x ^ { \prime } = \frac { d x } { d t } , \qquad y ^ { \prime } = \frac { d y } { d t } , \qquad z ^ { \prime } = \frac { d z } { d t } ;
$$

then equations (11） become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } - { x _ { 1 } } ^ { \prime } = 0 , } & { \quad \displaystyle \frac { d x _ { 1 } } { d t } ^ { \prime } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x _ { 1 } } , } \\ { \displaystyle \frac { d y _ { 1 } } { d t } - { y _ { 1 } } ^ { \prime } = 0 , } & { \quad \displaystyle \frac { d y _ { 1 } } { d t } ^ { \prime } + k ^ { 2 } ( S + m _ { 1 } ) \frac { y _ { 1 } } { r _ { 1 } ^ { 3 } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y _ { 1 } } , } \\ { \displaystyle \frac { d z _ { 1 } } { d t } - { z _ { 1 } } ^ { \prime } = 0 , } & { \quad \displaystyle \frac { d z _ { 1 } } { d t } ^ { \prime } + k ^ { 2 } ( S + m _ { 1 } ) \frac { z _ { 1 } } { r _ { 1 } ^ { 3 } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 1 } } , } \end{array} \right.
$$

and similar equations in which the subscript is 2.

If the motions of $m _ { 1 }$ and $m _ { 2 }$ were not disturbed by each other equations (12） would become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } - { x _ { 1 } } ^ { \prime } = 0 , \quad } & { \displaystyle \frac { d x _ { 1 } { } ^ { \prime } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } { } ^ { 3 } } = 0 , } \\ { \displaystyle \frac { d y _ { 1 } } { d t } - { y _ { 1 } } ^ { \prime } = 0 , \quad } & { \displaystyle \frac { d y _ { 1 } { } ^ { \prime } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { y _ { 1 } } { r _ { 1 } { } ^ { 3 } } = 0 , } \\ { \displaystyle \frac { d z _ { 1 } } { d t } - z _ { 1 } { } ^ { \prime } = 0 , \quad } & { \displaystyle \frac { d z _ { 1 } { } ^ { \prime } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { z _ { 1 } } { r _ { 1 } { } ^ { 3 } } = 0 , } \end{array} \right.
$$

and an independent system of similar equations in which the. subscript is 2. Let Ω=(x²+y²+z）-k2(S+m1)； then equations (13) take the form

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial x _ { 1 } ^ { \prime } } , } & { \quad \displaystyle \frac { d x _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { \partial x _ { 1 } } , } \\ { \displaystyle \frac { d y _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial y _ { 1 } ^ { \prime } } , } & { \quad \displaystyle \frac { d y _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { d y _ { 1 } } , } \\ { \displaystyle \frac { d z _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial z _ { 1 } ^ { \prime } } , } & { \quad \displaystyle \frac { d z _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { \partial z _ { 1 } } . } \end{array} \right.
$$

This form of the differential equations is convenient in connection with the problem of transforming equations so that the elliptic elements become the dependent variables whose values in terms of $\pmb { t }$ are required.

206.Transformation of Variables. In order to avoid confusion in the analysis,and to be able to say where and how the approximations are introduced, the method of the variation of parameters must be regarded in the first instance as simply a transformation of variables,which is perfectly legitimate for all values of the time for which the equations of transformation are valid. From this point of view the whole process is mathematically simple and lucid, the only trouble arising from the number of variables involved and the complicated relations among them.

In chapter v. it was shown how to express the coordinates in the Problem of Two Bodies in terms of the elements and the time.Let ${ \pmb { \alpha _ { 1 } } }$ ，·….， $\pmb { \alpha _ { 6 } }$ represent the elements of the orbit $m _ { 1 , }$ ， and $\beta _ { 1 } , \cdots , \beta _ { 6 }$ those of $\mathbf { \Delta } m _ { 2 }$ .Then the equations for the coordinates in the Problem of Two Bodies may be written

$$
\left\{ \begin{array} { l l } { x _ { 1 } = f ( \alpha _ { 1 } , \ \cdots , \ \alpha _ { 6 } , \ i ) , } & { \quad x _ { 1 } ^ { \prime } = \theta ( \alpha _ { 1 } , \ \cdots , \ \alpha _ { 6 } , \ i ) , } \\ { y _ { 1 } = g ( \alpha _ { 1 } , \quad \cdots , \ \alpha _ { 6 } , \ i ) , } & { \quad y _ { 1 } ^ { \prime } = \phi ( \alpha _ { 1 } , \ \cdots , \ \alpha _ { 6 } , \ i ) , } \\ { z _ { 1 } = h ( \alpha _ { 1 } , \ \cdots , \ \alpha _ { 6 } , \ i ) , } & { \quad z _ { 1 } ^ { \prime } = \psi ( \alpha _ { 1 } , \ \cdots , \ \alpha _ { 6 } , \ i ) , } \\ { x _ { 2 } = f ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) , } & { \quad x _ { 2 } ^ { \prime } = \theta ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) , } \\ { y _ { 2 } = g ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) , } & { \quad y _ { 2 } ^ { \prime } = \phi ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) , } \\ { z _ { 2 } = h ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) , } & { \quad z _ { 2 } ^ { \prime } = \psi ( \beta _ { 1 } , \ \cdots , \ \beta _ { 6 } , \ i ) . } \end{array} \right.
$$

A transformation of variables in equations (12) will now be made. Let it be forgotten for the moment that equations (15) are the solutions of the Problem of Two Bodies,and that the $\pmb { \alpha _ { i } }$ and $\beta _ { i }$ are the elements of the two orbits；but let (15) be considered as being the equations which transform equations (12) in the old variables, $x _ { 1 } , y _ { 1 } , z _ { 1 } , x _ { 1 } { ' } , y _ { 1 } { ' } , z _ { 1 } { ' } , x _ { 2 } , y _ { 2 } , z _ { 2 } , x _ { 2 } { ' } , y _ { 2 } { ' } , z _ { 2 } { ' }$ ,into an equivalent system in the new variables, $\alpha _ { 1 } , ~ \cdot ~ \cdot ~ , ~ \alpha _ { 6 } , ~ \beta _ { 1 } , ~ \cdot ~ \cdot ~ , ~ \beta _ { 6 } ,$ The transformations are effected by computing the derivatives occurring in (12) and making direct substitutions. The derivatives of equations (15) with respect to $t$ are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } = \frac { \partial x _ { 1 } } { \partial t } + \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { i } } { d t } , } \\ { \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot } \\ { \displaystyle \frac { d x _ { 1 } } { d t } = \frac { \partial x _ { 1 } { } ^ { \prime } } { \partial t } + \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } { } ^ { \prime } } { \partial \alpha _ { i } } \frac { d \alpha _ { i } } { d t } , } \\ { \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \cdot \cdot \mathrm { ~  ~ \cdot ~ } \cdot } \end{array} \right.
$$

The direct substitution of (16) in (12) gives

$$
\left\{ \begin{array} { l l } { \frac { \partial x _ { 1 } } { \partial t } - x _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial x _ { 1 } } { \partial z _ { 1 } } \frac { \partial \alpha _ { 1 } } { \partial t } = 0 , } \\ { \frac { \partial y _ { 1 } } { \partial t } - y _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial y _ { 1 } } { \partial z _ { 1 } } \frac { \partial \alpha _ { 1 } } { \partial t } = 0 , } \\ { \frac { \partial z _ { 1 } } { \partial t } - z _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial z _ { 1 } } { \partial z _ { 1 } } \frac { \partial z _ { 1 } } { \partial t } = 0 , } \\ { \frac { \partial x _ { 1 } ^ { \prime } } { \partial t } + \mathcal { k } ^ { \prime } ( \mathcal { S } + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } + \frac { \epsilon } { 2 } \frac { \partial x _ { 1 } ^ { \prime } } { \partial z _ { 1 } } \frac { \partial \alpha _ { 1 } } { \partial t } = m _ { 3 } \frac { \partial R _ { 1 } , 1 } { \partial x _ { 1 } } , } \\ { \frac { \partial y _ { 1 } ^ { \prime } } { \partial t } + \mathcal { k } ^ { \prime } ( \mathcal { S } + m _ { 1 } ) \frac { y _ { 1 } } { r _ { 1 } ^ { 3 } } + \frac { \epsilon } { 2 } \frac { \partial y _ { 1 } ^ { \prime } } { \partial z _ { 1 } } \frac { \partial \alpha _ { 1 } } { \partial t } = m _ { 2 } \frac { \partial R _ { 1 } , 2 } { \partial y _ { 1 } } , } \\ { \frac { \partial z _ { 1 } ^ { \prime } } { \partial t } + \mathcal { k } ^ { \prime } ( \mathcal { S } + m _ { 1 } ) \frac { z _ { 1 } } { r _ { 1 } ^ { 3 } } + \frac { \epsilon } { 2 } \frac { \partial z _ { 1 } ^ { \prime } } { \partial z _ { 1 } } \frac { \partial z _ { 1 } } { \partial t } = m _ { 2 } \frac { \partial R _ { 1 } , 1 } { \partial z _ { 1 } } , } \end{array} \right.
$$

and similar equations in $\boldsymbol { x } _ { 2 } , \cdots , \boldsymbol { z } _ { 2 } ^ { \prime }$ ,and $\beta _ { 1 } , \cdots , \beta _ { 6 }$ These equations are linear in the derivatives $\frac { d \alpha _ { i } } { d t }$ and can be solved for them, expressing them in terms of $\alpha _ { 1 } , ~ \cdots , ~ \alpha _ { 6 } , ~ \beta _ { 1 } , ~ \cdots , ~ \beta _ { 6 } ,$ and $t _ { : }$ provided the determinant of their coefficients is distinct from zero.

But if equations (15) are the solution of the problem of undisturbed elliptic motion equations (17） are greatly simplified, .for it is seen from (13）that，when $\alpha _ { 1 }$ ，…， $\pmb { \alpha _ { 8 } }$ are constant, -xi' = O for all values of t. The partial derivative $\frac { \partial x _ { 1 } } { \partial t }$ ， when $\alpha _ { 1 } , ~ \cdots , ~ \alpha _ { 8 }$ areregardedarblessti $\frac { d x _ { 1 } } { d t }$ when they are regarded as constants. Therefore $\frac { \partial x _ { 1 } } { \partial t } - x _ { 1 } { ' } \equiv 0$ and similarly $\frac { \partial { x _ { 1 } } ^ { \prime } } { \partial t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { { r _ { 1 } } ^ { 3 } } \equiv 0 ;$ , and similar quations in $\pmb { y }$ and $\pmb { z }$ ：As a consequence of these relations equations (17) reduce to

$$
\left\{ \begin{array} { l l } { \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { i } } { d t } = 0 , \qquad \quad \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } } { \partial \alpha _ { i } } ^ { \prime } \frac { d \alpha _ { i } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x _ { 1 } } } , } } \\ { \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial y _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { i } } { d t } = 0 , \qquad \quad \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial y _ { 1 } } { \partial \alpha _ { i } } ^ { \prime } \frac { d \alpha } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y _ { \downarrow } } } , } } \\ { \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial z _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { i } } { d t } = 0 , \qquad \quad \displaystyle { \sum _ { i = 1 } ^ { 6 } \frac { \partial z _ { 1 } } { \partial \alpha _ { i } } ^ { \prime } \frac { d \alpha _ { i } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 1 } } } , } } \end{array} \right.
$$

and similar equations in the $\beta _ { i }$ .These equations are linear in the derivatives $\frac { d \alpha _ { i } } { d t }$ and can be solved for thcm unless the determinant of their coefficients is zero.But the determinant of the linear system (18) is the Jacobian of the first set of equations (15) with respect to $\alpha _ { 1 } ,$ ：， $\alpha _ { 6 }$ ，and cannot vanish if these functions are independent and give a simple and unique determination of the elements.\* These functions are independent,and in general they give simple and unique values for the elements since they are the expressions for the coordinates in the Problem of Two Bodie... The problem of determining the elements from the values of the coordinates and components of velocity was solved in chap.v.

If $m _ { 2 } = 0$ equations (18) are linear and homogeneous,and since the determinant is not zero they can be satisfied only by $\frac { d \alpha _ { i } } { d t } = 0 ,$ $( i = 1 , \ \cdots , \ 6 )$ ．That is, the elements are constants,which,of course,is nothing new.

On solving equations (18),it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \alpha _ { i } } { d t } = m _ { 2 } \dot { \phi } _ { i } ( \alpha _ { 1 } , \dot { \mathrm {  ~ \cdot ~ } } \cdot \dot { \mathrm {  ~ \cdot ~ } } , \alpha _ { 6 } ; \beta _ { 1 } , \dot { \mathrm {  ~ \cdot ~ } } \cdot \dot { \mathrm {  ~ \cdot ~ } } , \beta _ { 6 } ; t ) , } & { ( i = 1 , \cdots , 6 ) , } \\ { \displaystyle \frac { d \beta _ { i } } { d t } = m _ { 1 } \psi _ { i } ( \alpha _ { 1 } , \dot { \mathrm {  ~ \cdot ~ } } \cdot \dot { \mathrm {  ~ \cdot ~ } } , \alpha _ { 6 } ; \beta _ { 1 } , \dot { \mathrm {  ~ \cdot ~ } } \cdot \dot { \mathrm {  ~ \cdot ~ } } , \beta _ { 6 } ; t ) , } & { ( i = 1 , \dot { \mathrm {  ~ \cdot ~ } } \cdot \dot { \mathrm {  ~ \cdot ~ } } , 6 ) . } \end{array} \right.
$$

It will be remembered that in determining the coordinates in the Problem of Two Bodies the first step,viz., the computation of the mean anomaly,involved the mean motion,defined by the equation

$$
n _ { i } = \frac { k \sqrt { S + m _ { i } } } { a _ { i } \mathrm { \ l } ^ { 3 } } , ~ ( j = 1 , 2 ) .
$$

Since the $\boldsymbol { n } _ { j }$ involve the masses of the planets the right members of (15),and consequently of (19), involve $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ implicitly.

In order to justify mathematically the precise method of integrating equations (i9） which is employed by astronomers, some remarks are necessary upon $m _ { 1 }$ and $m _ { 2 }$ ，In those places where they occur implicitly in the functions $\varphi _ { i }$ and $\psi _ { i }$ they will be regarded as fixed numbers; as they appear as factors of the $\psi _ { i }$ and $\varphi _ { i }$ respectively they will be regarded as parameters in powers of which the solutions may be expanded. Such a generalization of parameters is clearly permissible because, if a function involves a parameter in two different ways, there is no reason why it may not be expanded with respect to the parameter so far as it is involved in one way and not with respect to it as it is involved in the other.If the function,instead of being given explicitly,is defined by a set of differential equations the same things regarding the expansions in terms of parameters are true. If the attractions of bodies depended on something besides their masses (measured by their inertias) and their distances,as for example,on their rates of rotation or temperatures, then $m _ { 1 }$ and $\mathbf { \nabla } m _ { 2 }$ so far as they enter in the $\varphi _ { i }$ and $\psi _ { i }$ implicitly through $\boldsymbol { n } _ { 1 }$ and $\boldsymbol { n } _ { 2 }$ ，where they would be defined numerically by their individual mutual attractions for the sun,would be different from their values where they occur as factors of the $\varphi _ { \pm }$ and $\psi _ { i }$ ，for in the latter places they would be defined by their attractions fcr each other.

Hence,the values of the masses $m _ { 1 }$ and $m _ { 2 }$ entering implicitly in equations (15) and (19) are treated as fixed numbers,given in advance,and do not need to be retained explicitly;on the other hand, the $m _ { 1 }$ and $m _ { 3 }$ which are factors of the perturbing terms of the equations are retained explicitly,being supposed capable of taking any values not exceeding certain limits.

207.Method of Solution. Equations (11） are the general differential equations of motion for the Problem of Three Bodies. Equations (12) are equally general. No approximations were introduced in making the transformation of variables by (15); therefore equations (19) are general and rigorous. The difference is that if (19) were integrated the elements would be found instead of the coordinates as in (11),but as the latter can always be found from the former this must be regarded as the solution of the problem.

Instead of interrupting the course of mathematical reasoning by working out the explicit forms of (19),it will be preferable to show first by what methods they are solved. Explicit mention will be made at the appropriate times of all points at which assumptions or approximations are made.

When $m _ { 1 }$ and $m _ { 2 }$ are very small compared to $\pmb { S }$ ，as they are in the solar system， the orbits are very nearly fixed ellipses,and therefore $\alpha _ { \ ? }$ and $\beta _ { i }$ change very slowly. Consequently if they were regarded as constants in the right members of (19) and the equations integrated， approximate values of the $\pmb { \alpha _ { i } }$ and the $\beta _ { i }$ would be obtained for values of $t$ not too remote from the initial time. This is the method adopted in the illustrative example of the preceding article,and has been the point of view often taken by astronomers,especially in the pioneer days of Celestial Mechanics. But any theory which is only approximate，even though it is numerically dequate,does not measure up to the ideals of science.

Equations (19) are of the type which Cauchy and Poincaré have shown can be integrated as power series in $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ Cauchy proved that $m _ { 1 } , m _ { 2 } ,$ and $t$ can all be taken so small that the series converge. Poincaré proved the more general theorem\* that if the orbits in which the bodies are instantaneously moving at the initial time do not intersect, then for any finite range of values of $\mathbf { \delta } _ { t , \tiny { \begin{array} { r l } \end{array} } } t _ { \ j }$ the $\mathbf { \Delta } m _ { 1 }$ and $\mathbf { \nabla } m _ { 2 }$ can be taken so small that the solutions converge for every value of $\pmb { t }$ in the interval.However，the masses cannot be chosen arbitrarily small but are given by Nature. Hence the practical importance of the additional theorem that, whatever the values of $\pmb { m _ { 1 } }$ and $^ { m _ { 2 } , }$ there exists a range for $t$ so restricted that the solutions of equations (19) as powei series in the parameters $\pmb { m } _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ converge for every value of $\mathbf { \Delta } _ { t }$ in the range. In general, the larger the values of the parameters the more restricted the range. This is,of course,a special case of a general theorem respecting the expansion of solutions of differential equations of the type to which (19) belong as power series in parameters. $^ { \dagger }$

It follows from the last theorem quoted that, if the range of $\pmb { t }$ is not too great, the solutions of equations (19) can be expressed iu convergent power series in ${ \pmb m } _ { 1 }$ and $^ { m _ { 2 } , }$ of the form

$$
\left\{ \begin{array} { l l } { \displaystyle \alpha _ { i } = \sum _ { j = 0 } ^ { \infty } \sum _ { k = 0 } ^ { \infty } \alpha _ { i } ^ { ( j , k ) } m _ { 1 } ^ { j } m _ { 2 } ^ { k } , } \\ { \displaystyle \beta _ { i } = \sum _ { j = 0 } ^ { \infty } \sum _ { k = 0 } ^ { \infty } \beta _ { i } ^ { ( j , k ) } m _ { 1 } ^ { j } m _ { 2 } ^ { k } , } \end{array} \right.
$$

where the superfixes on the $\pmb { \alpha _ { i } }$ and $\beta _ { i }$ simply indicate the order of the coefficient.The $\alpha _ { i } ( \mathscr { i } , \pmb { \mathscr { k } } )$ and $\beta _ { i } ^ { ( j , ~ k ) }$ are functions of the time which are to be determined.It has been customary in the theory of perturbations to assume without proof that this expansion is valid for any desired length of time. As has been stated, it can be proved that it is valid for a sufficiently small interval of time; but as the method of demonstration gives only a limit within which the series certainly converge，and not the longest time during which they converge,and as the limit is almost certainly far too small,it has never been computed. It is to be understood, therefore,that the method which is just to be explained,is valid fora certain interval of time,which in the planetary theories is doubtless several hundreds of years.

On substituting (20） in (19) and developing with respect to $\pmb { m _ { 1 } }$ and $m _ { 2 }$ ,it is found that

$$
\begin{array} { r } { \Bigg [ \frac { d \alpha _ { \mathrm { i } } ^ { ( 0 , 0 ) } } { d t } + \frac { d \alpha _ { \mathrm { i } } ^ { ( 0 , 1 ) } m _ { 2 } } { d t } + \frac { d \alpha _ { \mathrm { i } } ^ { ( 1 , 0 ) } } { d t } m _ { 1 } + \frac { d \alpha _ { \mathrm { i } } ^ { ( 1 , 1 ) } } { d t } m _ { 1 } m _ { 2 } } \\ { + \frac { d \alpha _ { \mathrm { i } } ^ { ( 0 , 2 ) } } { d t } m _ { 2 } ^ { 2 } + \frac { d \alpha _ { \mathrm { i } } ^ { ( 0 , 0 ) } } { d t } m _ { 1 } ^ { 2 } + \cdots } \\ { = m _ { 2 } \phi _ { \mathrm { i } } ( \alpha _ { 1 } ^ { ( 0 , 0 ) } , \ \cdots , \ \alpha _ { \mathrm { e } } ^ { ( 0 , 0 ) } ; \ \beta _ { 1 } ^ { ( 0 , 0 ) } , \ \cdots , \ \beta _ { \mathrm { e } } ^ { ( 0 , 0 ) } ; \ t ) } \\ { + m _ { 2 } \displaystyle \sum _ { j = 1 } ^ { 6 } \frac { \partial \phi _ { \mathrm { i } } } { \partial \alpha _ { j } } ( \alpha _ { j } ^ { ( 0 , 1 ) } m _ { 2 } + \alpha _ { j } ^ { ( 1 , 0 ) } m _ { 1 } ) } \\ { + m _ { 2 } \displaystyle \sum _ { j = 1 } ^ { 6 } \frac { \partial \phi _ { \mathrm { i } } } { \partial \beta _ { j } } ( \beta _ { i } ^ { ( 0 , 1 ) } m _ { 2 } + \beta _ { i } ^ { ( 1 , 0 ) } m _ { 1 } ) } \end{array}
$$

$$
\left\{ \begin{array} { l l }  \begin{array} { r l } & { \mathrm { ~ - n g u e r ~ p o w e r s ~ I m ~ } m _ { 1 } \mathrm { ~ s n a m ~ } m _ { 2 } , } \\ { \frac { d \beta _ { i } ( \theta , \mathfrak { n } ) } { d t } + \frac { d \beta _ { i } ( \theta , \mathfrak { n } ) } { d t } m _ { 4 } + \frac { d \beta _ { i } ( \mathfrak { n } , \mathfrak { n } ) } { d t } m _ { 1 } + \frac { d \beta _ { i } ( \mathfrak { n } , \mathfrak { n } ) } { d t } m _ { 1 } m _ { 2 } } \\ & { \begin{array} { r l } { + \frac { d \beta _ { i } ( \theta , \mathfrak { n } ) } { d t } m _ { 2 } + \frac { d \beta _ { i } ( \mathfrak { n } , \mathfrak { n } ) } { d t } m _ { 1 } + \cdots } \\ { \quad } & { \mathrm { ~ } } \end{array} } \\ { \begin{array} { r l } & { = m _ { 1 } \psi _ { i } ( \alpha _ { 1 } ^ { ( 0 , 0 ) } , \ \cdots , \ \alpha _ { 0 } ^ { ( 0 , 0 ) } , \ \beta _ { 1 } ^ { ( 0 , 0 ) } , \ \cdots , \ \beta _ { 0 } ^ { ( 0 , 0 ) } ; \ t ) } \\ & { \quad + m _ { 1 } \frac { \mathfrak { L } } { \mathrm { ~ d } \mathrm { ~ d } \mathfrak { n } } \frac { \partial \beta _ { i } } { \partial \alpha _ { i } } ( \alpha _ { i } ^ { ( 0 , 0 , 1 ) } m _ { 2 } + \alpha _ { i } ^ { ( 1 , 0 , 0 ) } m _ { 1 } ) } \\ & { \quad + m _ { 1 } \frac { \mathfrak { L } } { \mathrm { ~ d } \mathrm { ~ d } \mathfrak { n } } ( \beta _ { i } ^ { ( 0 , 0 , 1 ) } m _ { 2 } + \beta _ { i } ^ { ( 1 , 0 ) } m _ { 1 } ) } \end{array} } \end{array} \right. \end{array}
$$

In the partial derivatives it is to be understood that $\alpha _ { i }$ and $\beta _ { i }$ are replaced by $\alpha _ { i } ^ { . ( 0 , \ : 0 ) }$ and $\beta _ { i } ^ { \phantom { } } ^ { ( 0 , \ 0 ) }$ respectively. If $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ were not regarded as fixed numbers in the left members of equations (11), $\phi _ { i } , \psi _ { i } , \frac { \partial \phi _ { i } } { \partial \alpha _ { j } } , \frac { \partial \phi _ { i } } { \partial \beta _ { j } }$ ,ete.ouldhavetbedevelospoer series in $\pmb { m } _ { 1 }$ and ${ \bf { \mathit { m } } _ { 2 } } { \bf { \mathit { n } } _ { 3 } }$ ，thus adding greatly to the complexity of the work.

Within the limits of convergence the coefficients of like powers of $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ on the two sides of the equations are equal. Hence, on equating them,it follows that

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { d \alpha _ { i } ( 0 , 0 ) } { d t } = 0 , ( i = 1 , \cdots , 6 ) } , } \\ { \displaystyle { \frac { d \beta _ { i } ( 0 , 0 ) } { d t } = 0 . } } \end{array} \right.
$$

$$
\begin{array} { r l } & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = \partial _ { \alpha } ( \phi _ { \alpha \beta } ) , \phi _ { \alpha \beta } ( x , x ) , \phi _ { \beta \beta } ( x , x ) , \dots , \hat { \phi } _ { \beta \beta } ( x , x ) , \dots , \hat { \phi } _ { \beta \beta } ( x , y ) ] , } \\ & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = 0 ,  } \\ & {  [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = 0 ,   } \\ & {   \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = 0 ,   } \\ & {   \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = \partial _ { \beta } ( \phi _ { \alpha \beta } , x ) , \dots , \partial _ { \alpha } ( \phi _ { \beta \beta } ) , \hat { \phi } _ { \alpha \beta } ( x , x ) , \dots , \hat { \phi } _ { \beta \beta } ( x , y ) ]  } \\ & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = \frac { \partial _ { \alpha } ( \phi _ { \alpha \beta } , x ) } { \partial x } , \dots , \hat { \phi } _ { \alpha \beta \alpha } ( x , x ) , \dots , \hat { \phi } _ { \beta \alpha \beta } ( x , x ) ] , } \\ & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = \frac { \partial _ { \alpha } ( \phi _ { \alpha \beta } , x ) } { \partial x } , \dots , \hat { \phi } _ { \alpha \beta \alpha } ( x , x ) ] , } \\ & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , x ) } { \partial x } = \frac { \partial _ { \alpha } ( \phi _ { \alpha \beta } , x ) } { \partial x } , \dots , \hat { \phi } _ { \alpha \beta \alpha } ( x , y ) , \dots , \hat { \phi } _ { \alpha \beta \alpha } ( x , y ) ] , } \\ & { [ \frac { \partial \hat { \phi } _ { \alpha \beta } ( x , y ) } { \partial x } = 0 ,  } \\ &   \frac  \partial \hat { \phi } _ { \alpha \beta } ( x , y )  \end{array}
$$

On integrating equations (22) and substituting the values of $\alpha _ { i } ^ { . ( 0 , 0 ) }$ and $\beta _ { i } ^ { \phantom { } ( 0 , 0 ) }$ thus obtained in (23),the latter are reduced to quadratures and can be integrated;on integrating (23) and substituting the expressions for $\alpha _ { i } ( 0 , 1 )$ ， $\alpha _ { i } ^ { \ ( 1 , 0 ) }$ ， $\beta _ { i } ^ { ( 0 , 1 ) }$ ， $\beta _ { i } ^ { ( 1 , 0 ) }$ in (24), the latter are reduced to quadratures and can be integrated; and this process can be continued indefinitely. In this manner the coefficients of the series (2O) can be determined，and the values of $\alpha _ { i }$ and $\beta _ { i }$ can be found to any desired degree of precision for values of the time for which the series converge.

208.Determination of the Constants of Integration. A new constant of integration is introduced when equations (22),(23),·. are integrated for each $\alpha _ { i } { } ^ { ( i , k ) } , \beta _ { i } { } ^ { ( j , k ) }$ .These constants will now be determined.

Let the constant which is introduced with the $\alpha _ { i } ( \textit { i } , \textit { k } )$ be denoted by $- \ a _ { i } ( \textit { i } , \textit { k } )$ and with the $\beta _ { \mathbf { i } } ^ { \mathbf { \Gamma } } ^ { \left( \textit { 1 , k } \right) }$ ， $\mathrm { b y } - b _ { i } ( { \boldsymbol { i } } , { \boldsymbol { k } } )$ .Since the first set of differential equations have $m _ { 2 }$ as a factor in their right members, while the second set have $m _ { 1 }$ as a factor,it follows that

$$
\begin{array} { r l } { { \alpha _ { i } } ^ { ( j , 0 ) } = { a _ { i } } ^ { ( j , 0 ) } , \quad } & { ( j = 0 , \cdots \infty ) , } \\ { { \beta _ { i } } ^ { ( 0 , k ) } = { b _ { i } } ^ { ( 0 , k ) } , \quad } & { ( k = 0 , \cdots \infty ) . } \end{array}
$$

Since the $\alpha _ { i } ( \pmb { i } , \pmb { k } )$ and $\beta _ { i } ^ { \ : ( j , k ) }$ are defined by quadratures all the constants of integration are simply added to functions of $\pmb { t }$ That is, the $\alpha _ { i } ( \pmb { i } , \pmb { k } )$ and $\beta _ { \mathbf { i } } ^ { ( \ i , \ k ) }$ have the form

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \alpha _ { i } ( i , k ) = f _ { \mathrm { i } } ( i , k ) ( t ) - a _ { i } ( i , k ) , } \\ { \beta _ { i } ( j , k ) = g _ { \mathrm { i } } ( i , k ) ( t ) - b _ { i } ( i , k ) . } \end{array} \right. } \end{array}
$$

Therefore equations (20) become

$$
\begin{array}{c} \begin{array} { r } { \left\{ \alpha _ { i } = \displaystyle \sum _ { j = 0 } ^ { \infty } a _ { i } ^ { ( j , 0 ) } m _ { 1 } i + \displaystyle \sum _ { j = 0 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \big ( f _ { i } ( i , k ) - a _ { i } ^ { ( j , k ) } \big ) m _ { 1 } i _ { m _ { 2 } } k , \right.} \\ { \beta _ { i } = \displaystyle \sum _ { k = 0 } ^ { \infty } b _ { i } ^ { ( 0 , k ) } m _ { 2 } { } ^ { k } + \displaystyle \sum _ { j = 1 } ^ { \infty } \sum _ { k = 0 } ^ { \infty } \big ( g _ { i } ( i , k ) - b _ { i } ^ { ( j , k ) } \big ) m _ { 1 } i _ { m _ { 2 } } k . } \end{array}   \end{array}
$$

Let the values of $\alpha _ { i }$ and $\beta _ { i }$ at $t = t _ { 0 }$ be $\alpha _ { i } ^ { . ( 0 ) }$ and $\beta _ { i } ^ { \phantom { } } ^ { ( 0 ) }$ respectively. Then,at $t = t _ { 0 } ,$ equations (25） become

$$
\begin{array} { r } { \left\{ \alpha _ { \mathfrak i } { } ^ { ( 0 ) } = \displaystyle \sum _ { j = 0 } ^ { \infty } a _ { \mathfrak i } { } ^ { ( j , 0 ) } m _ { 1 } { } ^ { j } + \displaystyle \sum _ { j = 0 } ^ { \infty } \displaystyle \sum _ { k = 1 } ^ { \infty } \big ( f _ { \mathfrak i } { } ^ { ( j , k ) } - a _ { \mathfrak i } { } ^ { ( j , k ) } \big ) _ { 0 } m _ { 1 } { } ^ { j } m _ { 2 } { } ^ { k } , \right. } \\ { \left. \beta _ { \mathfrak i } { } ^ { ( 0 ) } = \displaystyle \sum _ { k = 0 } ^ { \infty } b _ { \mathfrak i } { } ^ { ( 0 , k ) } m _ { 2 } { } ^ { k } + \displaystyle \sum _ { j = 1 } ^ { \infty } \displaystyle \sum _ { k = 0 } ^ { \infty } \big ( g _ { \mathfrak i } { } ^ { ( j , k ) } - b _ { \mathfrak i } { } ^ { ( j , k ) } \big ) _ { 0 } m _ { 1 } { } ^ { j } m _ { 2 } { } ^ { k } . \right. } \end{array}
$$

Since these equations must be true for all values of $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ below certain limits, the coefficients of corresponding powers of $m _ { 1 }$ and ${ \mathbf { \nabla } } m _ { 2 }$ in the right and left members are equal; whence

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { a _ { \mathfrak { i } } ^ { ( j , ~ 0 ) } = { \alpha _ { i } } ^ { ( 0 ) } , \qquad a _ { \mathfrak { i } } ^ { ( j , ~ 0 ) } = 0 , \qquad ( j = 1 , ~ \cdots \infty ) , } \\ { b _ { \mathfrak { i } } ^ { ( 0 , ~ 0 ) } = { \beta _ { i } } ^ { ( 0 ) } , \qquad b _ { \mathfrak { i } } ^ { ( 0 , ~ k ) } = 0 , \qquad ( k = 1 , ~ \cdots \infty ) , } \\ { f _ { \mathfrak { i } } ^ { ( i , k ) } ( t _ { 0 } ) - a _ { \mathfrak { i } } ^ { ( i , k ) } = 0 , \qquad ( j = 1 , \cdots \infty ; { k = 1 } , \cdots \infty ) , } \\ { g _ { \mathfrak { i } } ^ { ( i , k ) } ( t _ { 0 } ) - b _ { \mathfrak { i } } ^ { ( i , k ) } = 0 , \qquad ( j = 1 , \cdots \infty ; { k = 1 } , \cdots \infty ) . } \end{array} \right. } \end{array}
$$

Since all the terms of the right members of (25) except the first vanish at $t = t _ { 0 } ,$ it follows that $\alpha _ { i } ( 0 , 0 )$ and $\beta _ { i } ^ { \ : ( 0 , 0 ) }$ are the osculating elements [Art.172] of the orbits of $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ respectively at the time $t = t _ { 0 } ,$ and that the other coefficients of (2O) are the definite integrals of the differential equations which define them taken between the limits $t = t _ { 0 }$ and $t = t .$

209. The Terms of the First Order. The terms of the first order with respect to the masses are defned by equations (23). Since the terms of order zero.are the osculating elements at $\scriptstyle t _ { 0 } ,$ the differential equations become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \alpha _ { i } ( 0 , 1 ) } { d t } = \phi _ { i } ( \alpha _ { 1 } ^ { ( 0 ) } , \cdots , \alpha _ { 6 } ^ { ( 0 ) } ; \ \beta _ { 1 } ^ { ( 0 ) } , \ \cdots , \beta _ { 6 } ^ { ( 0 ) } ; \ t ) , } \\ { \displaystyle \frac { d \beta _ { i } ( 1 , 0 ) } { d t } = \psi _ { i } ( \alpha _ { 1 } ^ { ( 0 ) } , \ \cdots , \alpha _ { 6 } ^ { ( 0 ) } ; \ \beta _ { 1 } ^ { ( 0 ) } , \ \cdots , \beta _ { 6 } ^ { ( 0 ) } ; \ t ) . } \end{array} \right.
$$

The right members of these equations are proportional to the rates at which the several elements of the orbits of the two planets would vary at any time $t _ { i }$ ,if the two planets were moving at that instant strictly in the original ellipses.The integrals of (27) are, therefore,the sums of the instantaneous effects;or,in other words, they are the sums of the changes which would be produced if the forces and their instantaneous results were always exactly equal to those in the undisturbed orbits. Of course the perturbations modify these conditions and produce secondary，tertiary，and higher order effects. They are included in the coefficients of higher powers of $\boldsymbol { m } _ { 1 }$ and $\mathbf { \nabla } m _ { 2 }$ in (20).

The quantities $\alpha _ { i } ^ { \ : ( 0 , 1 ) }$ and $\beta _ { i } ^ { \left( 1 , 0 \right) }$ are usually called perturbations of the first order with respect to the masses. The reason is clearly because they are the coefficients of the first powers of the masses in the series (2O). In the planetary theories it is not necessary to go to perturbations of higher orders except in the case of the larger planets which are near each other,and then comparatively few terms are great enough to be sensible. It is not necessary in the present state of the planetary theories to include terms of the third order except in the mutual perturbations of Jupiter and Saturn.

Instead of there being but two planets and the sun there are eight planets and the sun,so that the actual theory is not quite so simple as that which has been outlined. Yet,as will be shown, the increased complexity comes chiefly in the perturbations of higher orders. If there were a third planet $\mathbf { \nabla } m _ { 3 }$ whose orbit had the elements $\gamma _ { 1 } , \cdots , \gamma _ { 6 } ,$ equations (23) would become

$$
\begin{array} { r }  [ \begin{array} { l l l l l } { \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } } & { 0 , } & { } & { } & { } \\ { + \frac { \partial ^ { 2 } \varphi } { \partial x } } & { 0 , } & { } & { } & { } \\ { - \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } ( \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \partial _ { x } \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , } & { } & { } \\ { + \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } \langle \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \partial _ { x } \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \varphi \mathfrak u _ { x } ^ { ( 1 ) } , \dots , } & { } & { } \\ { \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } \langle \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \varphi \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , } & { } & { } \\ { + \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } \langle \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \dots , \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \partial _ { x } \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , } & { } & { } \\ { \frac { \partial ^ { 2 } \varphi } { \partial x } } & { } & { } & { } & { } \\ { + \frac { \partial ^ { 2 } \varphi } { \partial x } } & { - \partial _ { x } \langle \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , \dots , \dots , \partial _ { x } \mathfrak u _ { x } ^ { ( 1 ) } , } & { } & { } \\ { \frac { \partial ^ { 2 } \varphi } { \partial x } } & { } & { } & { } \\ { + \frac { \partial ^ { 2 } \varphi } { \partial x } } &  - \partial _ { x } \langle \partial _ { x } \ \end{array} \end{array}
$$

If there were more planets more equations of the same type would be added. Consider the perturbations of the frst order of the elements of the orbits $m _ { 1 }$ ； they are composed of two distinct parts given by the second and third equations of (28),one coming from the attraction of $m _ { 2 }$ ,and the other from the attraction of ${ \bf \nabla } m _ { 3 } .$ Therefore,the statement of astronomers that the perturbing effects of the various planets may be considered separately, is true for the perturbations of the first order with respect to the masses.

210. The Terms of the Second Order. It has been shown that $\alpha _ { i } { } ^ { ( 1 , 0 ) } = \alpha _ { i } { } ^ { ( 2 , 0 ) } = \beta _ { i } { } ^ { ( 0 , 1 ) } = \beta _ { i } { } ^ { ( 0 , 2 ) } = 0$ ；therefore it follows from (24) that the terms of the second order with respect to the masses are determined by the equations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \alpha _ { i } ( 1 , 1 ) } { d t } = \sum _ { j = 1 } ^ { 6 } \frac { \partial \phi _ { i } \left( \alpha _ { 1 } ( 0 ) , \cdot \cdot \cdot , \alpha _ { 6 } ( 0 ) , \beta _ { 1 } ( 0 ) , \cdot \cdot \cdot , \beta _ { 6 } ( 0 ) , \cdot \right) } { \partial \beta _ { j } } \beta _ { j } ( ^ { 1 , 0 } ) , } \\ { \displaystyle \frac { d \alpha _ { i } ( 0 , 2 ) } { d t } = \sum _ { j = 1 } ^ { 6 } \frac { \partial \phi _ { i } \left( \alpha _ { 1 } ( 0 ) , \cdot \cdot \cdot , \alpha _ { 6 } ( 0 ) , \cdot \beta _ { 1 } ( 0 ) , \cdot \cdot \cdot , \beta _ { 6 } ( 0 ) , \cdot \right) } { \partial \alpha _ { j } } \alpha _ { i } ^ { \beta _ { 1 } , 1 } ; } \\ { \displaystyle \frac { d \beta _ { i } ( ^ { 1 , 1 ) } } { d t } = \sum _ { j = 1 } ^ { 6 } \frac { \partial \psi _ { i } \left( \alpha _ { 1 } ( 0 ) , \cdot \cdot \cdot , \alpha _ { 6 } ( 0 ) , \cdot \beta _ { 1 } ( ^ { 0 } ) , \cdot \cdot \cdot , \beta _ { 6 } ( ^ { 0 } ) , \cdot \cdot \right) } { \partial \alpha _ { j } } \alpha _ { j } ^ { \beta _ { 1 } , 1 } , } \\ { \displaystyle \frac { d \beta _ { i } ( ^ { 2 , 0 } ) } { d t } = \sum _ { j = 1 } ^ { 6 } \frac { \partial \psi _ { i } \left( \alpha _ { 1 } ( ^ { 0 } ) , \cdot \cdot \cdot , \alpha _ { 6 } ( ^ { 0 } ) , \beta _ { 1 } ( ^ { 0 } ) , \cdot \cdot \cdot , \beta _ { 6 } ( ^ { 0 } ) , \cdot \right) } { \partial \beta _ { j } } \beta _ { j } ^ { \alpha _ { 1 } , 0 } . } \end{array} \right.
$$

The perturbations of the first order are those which would result if the disturbing forces at every instant were the same as they would be if the bodies were moving in the original ellipses. If the bodies $m _ { 1 }$ and $m _ { 2 }$ move in curves differing from the original ellipses the rates at which the elements change at every instant are different from the values given by equations (27). The perturbations of the elements of the orbit of $m _ { 1 }$ due to the fact that $m _ { 2 }$ departs from its original ellipse by perturbations of the first order are given by the equations of the type of the first of (29)，for,if $\beta _ { j } { } ^ { ( 1 , 0 ) } = 0$ ,it follows that $\alpha _ { i } ^ { ( 1 , 1 ) } = 0$ also. The perturbations of the elements of the orbit of $m _ { 1 }$ due to the fact that $m _ { 1 }$ departs from its original ellipse by perturbations of the first order are given by the equations of the type of the second of (29),for,if $\alpha _ { j } ^ { \tiny { ( 0 , 1 ) } } = 0$ it follows that $\alpha _ { i } ^ { ( 0 , 2 ) } = 0$ also.The terms $\beta _ { i } ^ { \mathbf { \Gamma } ( 1 , \ 1 ) }$ and $\beta _ { i } ^ { \mathbf { \Gamma } _ { \left( 2 , \mathbf { 0 } \right) } }$ in the elements of the orbit of $m _ { 2 }$ arise from similar causes. Thus the perturbations of the second order correct the errors in the terms of the first order,and those of the third order correct the errors in the second,and so on.

As has been said, the solutions expressed as power series in the masses converge if the interval of time is taken not too great. In a general way, the smaler the masses of the planets the longer the time during which the series converge. In the Lunar Theory the sun plays the role of the disturbing pianet. Since its mass is very great compared to that of the central body,the earth,the series in powers of the masses as given above would converge for only a very short time,probably only a few months instead of years. Such a Lunar Theory would be entirely unsatisfactory. On this account the perturbations in the Lunar Theory are developed in powers of the ratio of the distances of the moon and the sun from the earth,and special artifices are employed to avoid secular terms in all the elements except the nodes and perigee.

If there is a third planet the perturbations of the second order are considerably more complicated. Let the planets be $m _ { 1 } , ~ m _ { 2 } ,$ and $\displaystyle m _ { 3 }$ ，and consider the perturbations of the second order of the elements of the orbit of $m _ { 1 }$ ，From purely physical considerations it is seen that the following sorts of terms will arise: $( a )$ terms arising from the disturbing action of $m _ { 2 }$ and $\displaystyle m _ { 3 }$ ，due respectively to the perturbations of the frst order of the elements of $m _ { 2 }$ and $\mathbf { \nabla } m _ { \mathfrak { z } }$ by $m _ { 1 } ; ( b )$ terms arising from the disturbing action of $m _ { 2 }$ and $\displaystyle m _ { 3 }$ due to the perturbations of the first order of the elements of the orbit of $m _ { 1 }$ by $m _ { 2 }$ and $\mathbf { \nabla } m _ { 3 }$ ； $( c )$ terms arising from the disturbing action of $m _ { 2 }$ ，due to the perturbations of the first order of the elements of the orbit of $m _ { 1 }$ by $m _ { 3 } ; ~ ( d )$ terms arising from the disturbing action of $m _ { 2 }$ ,due to the perturbations of the frst order of the elements of the orbit of $m _ { 2 }$ by $m _ { 3 }$ ； $( e )$ terms arising from the disturbing action of $m _ { 3 }$ ,due to the perturbations of the first order of the elements of the orbit of $m _ { 1 }$ by $m _ { 2 }$ ； and $( f )$ terms arising from the disturbing action of $m _ { 3 }$ ,due to the perturbations of the first order of the elements of $m _ { 3 }$ by $m _ { 2 }$

Under the supposition that there are three planets, the terms of the second order with respect to the masses are found from equations (19) and (20) to be

$$
\{ \begin{array} { l l } { \displaystyle \frac { \mathrm { d } \omega ^ { ( 4 , 1 ) , \varepsilon } } { \mathrm { d } t } = - \frac { \mathrm { d } } { 2 } \mathrm { d } \omega \mathrm { d } \omega \mathrm { B } _ { 1 } ^ { ( 1 ) , \varepsilon } , \quad \cdots , \quad \omega \mathrm { B } _ { 0 } ^ { ( 2 ) , \varepsilon } \mathrm { B } _ { 2 } ^ { ( 3 , 1 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 3 , 2 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 4 , 3 ) , \varepsilon } , } \\ { \displaystyle \frac { \mathrm { d } \omega ^ { ( 4 , 1 ) , \varepsilon } } { \mathrm { d } t } = - \frac { \mathrm { d } } { 2 } \mathrm { d } \omega \mathrm { d } \omega \mathrm { B } _ { 1 } ^ { ( 2 ) , \varepsilon } , \quad \cdots , \quad \omega \mathrm { B } _ { 0 } ^ { ( 3 ) , \varepsilon } \mathrm { B } _ { 2 } ^ { ( 3 , 1 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 3 , 3 ) , \varepsilon } , } \\ { \displaystyle \frac { \mathrm { d } \omega ^ { ( 4 , 1 ) , \varepsilon } } { \mathrm { d } t } = - \frac { \mathrm { d } } { 2 } \mathrm { d } \omega \mathrm { d } \omega \mathrm { B } _ { 1 } ^ { ( 3 ) , \varepsilon } , \quad \cdots , \quad \omega \mathrm { B } _ { 0 } ^ { ( 4 ) , \varepsilon } \mathrm { B } _ { 2 } ^ { ( 3 , 1 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 3 , 3 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 4 , 4 ) , \varepsilon } , } \\ { \displaystyle \frac { \mathrm { d } \omega ^ { ( 4 , 1 ) , \varepsilon } } { \mathrm { d } t } = - \frac { \mathrm { d } } { 2 } \mathrm { d } \omega \mathrm { d } \omega \mathrm { B } _ { 1 } ^ { ( 3 ) , \varepsilon } , \quad \cdots , \quad \omega \mathrm { B } _ { 0 } ^ { ( 4 ) , \varepsilon } \mathrm { B } _ { 1 } ^ { ( 4 ) , \varepsilon } , \quad \cdots , \quad \mathrm { d } \omega ^ { ( 3 , 4 ) , \varepsilon } , \quad \mathrm { d } \omega ^ { ( 4 , 3 ) , \varepsilon } , } \\  \displaystyle \frac { \mathrm { d } \omega ^ { ( 4 , 1 ) , \varepsilon } } { \mathrm { d } t } = \frac { \mathrm { d } } { 2 } \mathrm { d } \omega \mathrm { B } _ { 1 }  \end{array}
$$

and ilr quations for $\frac { d \beta _ { i } } { d t }$ and $\frac { d { \gamma } _ { i } } { d t }$

The first two equations give the perturbations of the class $( a )$ ， for, $\phi _ { i } ( \alpha , \beta )$ and $\phi _ { i } ( \alpha , \gamma )$ are the portions of the perturbative function given by ${ \mathbf { } } m _ { 2 }$ and $\displaystyle m _ { 3 }$ respectively，while $\beta _ { i } ^ { ( 1 , 0 , 0 ) }$ and $\gamma _ { i } ^ { \ ( 1 , \ 0 , \ 0 ) }$ are the perturbations of the first order of the elements of the orbits of $\scriptstyle { m _ { 2 } }$ and $\mathbf { \nabla } m _ { 3 }$ by $m _ { 1 }$ .Similarly,the third and fourth equations give the perturbations of the class $( b )$ ；the first term of the fifth equation,those of class $( c )$ ； the second term,of class $( d )$ ; the third term,of class $( e )$ ; and the fourth term,of the class $( f )$ ·

It appears from this that the terms of the second order cannot be computed separately for each of the disturbing planets.

The types of terms which will arise in the perturbations of the third order can be similarly predicted from physical considerations,and the predictions can be verified bya detailed discussion of the equations.

# XXV. PROBLEMS.

1. In equations (3) take the term $\pmb { \nu }$ cos $\boldsymbol { \mathbf { \rho } } _ { \boldsymbol { u } }$ to the left member before starting the integration,and include it in equations (4). Carry out the whole process of integration with this variation in the procedure.

2. If equations (7) are integrated as power series in $\pmb { \mu }$ and ${ \pmb \nu }$ what types of functions of $\pmb { t }$ will arise in the terms of the second order?

3.Write the equations defining the terms of order zero,one,and two in the masses when equations (11) are integrated ag series in $m _ { \ell }$ and $\mathbf { \Delta } m _ { 2 }$ Show that the terms of order zero are the coordinates that $m _ { 1 }$ ond $\mathbf { \nabla } m _ { 2 }$ would have if they were particles moving around the sun in ellipses defined by their initial conditions. Show that the equations defining the terms of the first and higher orders are linear and non-homogeneous,instead of being reduced to quadratures as they are after the method of the variation of parameters has been used.

4.Suppose there are four planets, $m _ { 1 } , \ m _ { 2 } , \ m _ { 3 } , \ m _ { 4 }$ writeall the terms of the second order with respect to the magses according to (30) and interpret each.

5.Suppose there are two planets $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ ；write all of the terms of the third order with respect to the masses and interpret each.

6.Suppose $m _ { 1 } = m _ { 2 } = m _ { 3 }$ and that the planets are arranged in the order $m _ { 1 } , ~ m _ { 2 } , ~ :$ $\displaystyle m _ { 3 }$ with respect to their distance from the sun. Show that of the pertuiiations defined by equations (3O) the most important are those given by the first and third equations and the second term of the fth;that the perturbations next in importance are given by the first,third,and fourth terms of the fifth equation；and that the least important are given by the second and fourth equations.

211.Choice of Elements. In order to exhibit the manner in which the various sorts of terms enter in the perturbations of the first order, it willbe necessary to develop equations (19) explicitly. This was deferred,on account of the length of the transformations which are necessary,until a general view of the mathematical principles involved could be given.

If terms of the first order alone are considered the functions $\phi _ { i } ( \alpha , \beta )$ can be considered independently of $\psi _ { i } ( \alpha , \beta )$ . Any independent functions of the elements may be used in place of the ordinary elements.In fact,one of the elements already employed, ${ \pmb { \pi } } = { \pmb { \omega } } + { \pmb { \delta } } { \pmb { \mathrm { \delta } } }$ ， is the sum of two geometrically simpier elements. Now the form of $\phi _ { i } ( \alpha , \beta )$ will depend upon the elements chosen; with certain elements they are rather simple,and with others very complicated. They will be taken in the first example which follows so that those functions shall become as simple as possible.

212. Lagrange's Brackets. Lagrange has made the following transformation which greatly facilitates the computation of (19). Multiply (18) by-αi, ${ \bf b y } - \frac { { \partial x _ { 1 } } ^ { \prime } } { { \partial \alpha _ { 1 } } } , ~ - \frac { { \partial y _ { 1 } } ^ { \prime } } { { \partial \alpha _ { 1 } } }$ $- \frac { \partial z _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } , \frac { \partial x _ { 1 } } { \partial \alpha _ { 1 } } , \frac { \partial y _ { 1 } } { \partial \alpha _ { 1 } } , \frac { \partial z _ { 1 } } { \partial \alpha _ { 1 } }$ respectively and add. The result is

$$
\{ \begin{array} { l }  { \displaystyle \frac { \partial \alpha _ { 2 } } { \partial u } \{ \frac { \partial x _ { 1 } } { \partial \alpha _ { 3 } } \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 2 } } - \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 3 } } \frac { \partial x _ { 2 } } { \partial \alpha _ { 2 } } + \frac { \partial y _ { 1 } } { \partial x _ { 1 } } \frac { \partial y _ { 1 } ^ { \prime } } { \partial \alpha _ { 3 } } - \frac { \partial y _ { 1 } ^ { \prime } } { \partial \alpha _ { 3 } } \frac { \partial y _ { 1 } ^ { \prime } } { \partial \alpha _ { 4 } }  } \\ { { \displaystyle \qquad + \frac { \partial \alpha _ { 4 } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 2 } } { \partial \alpha _ { 2 } } - \frac { \partial z _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial z _ { 1 } } { \partial \alpha _ { 2 } } \Biggr \} } } \\ { { \displaystyle + \frac { \partial \alpha _ { 5 } } { \omega } \{ \frac { \partial x _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 3 } } - \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 1 } } { \partial \alpha _ { 0 } } + \cdots \} } } \\ { { \displaystyle \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot } } \\ { { \displaystyle + \frac { \partial \alpha _ { t } } { \omega } \{ \frac { \partial x _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 2 } } - \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 3 } } + \cdots \} } } \\   \displaystyle \qquad - \ m _ { 3 } \frac { \partial H _ { 1 , 2 } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 2 } } { \partial \alpha _ { 2 } } + m _ { 2 } \frac { \partial H _ { 1 , 3 } } { \partial y _ { 1 } } \frac { \partial y _ { 1 } } { \partial \alpha _ { 1 } } + m _ { 3 } \frac { \partial H _ { 1 , 2 } }  \partial \alpha _  \end{array}
$$

Lagrange's brackets $[ \alpha _ { i } , \alpha _ { i } ]$ are defined by

$$
\begin{array} { r } { [ \alpha _ { i } , \alpha _ { j } ] \equiv \frac { \partial x _ { 1 } } { \partial \alpha _ { i } } \frac { \partial { x _ { 1 } } ^ { \prime } } { \partial \alpha _ { j } } - \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { i } } \frac { \partial x _ { 1 } } { \partial \alpha _ { j } } + \frac { \partial y _ { 1 } } { \partial \alpha _ { i } } \frac { \partial { y _ { 1 } } ^ { \prime } } { \partial \alpha _ { j } } - \frac { \partial { y _ { 1 } } ^ { \prime } } { \partial \alpha _ { i } } \frac { \partial { y _ { 1 } } } { \partial \alpha _ { j } } } \\ { + \frac { \partial z _ { 1 } } { \partial \alpha _ { i } } \frac { \partial { z _ { 1 } } ^ { \prime } } { \partial \alpha _ { j } } - \frac { \partial { z _ { 1 } } ^ { \prime } } { \partial \alpha _ { i } } \frac { \partial { z _ { 1 } } } { \partial \alpha _ { j } } \mathrm { , } } \end{array}
$$

Form the equations corresponding to (31) in $\alpha _ { 2 } , \cdots , \alpha _ { 6 }$ the resulting system of equations is

$$
\left\{ \begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { 6 } \left[ \alpha _ { 1 } , \alpha _ { i } \right] \frac { d \alpha _ { i } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 1 } } } , } \\ { { \displaystyle \sum _ { i = 1 } ^ { 6 } \left[ \alpha _ { 2 } , \alpha _ { i } \right] \frac { d \alpha _ { i } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 2 } } } , } \\ { { ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot ~ \cdot } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 6 } \left[ \alpha _ { 6 } , \alpha _ { i } \right] \frac { d \alpha _ { i } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 6 } } } . } \end{array} \right.
$$

These equations are equivalent to the system (18) and will be used in place of them.

213. Properties of Lagrange's Brackets. It follows at once from the definitions of Lagrange's brackets that

$$
\begin{array} { r } { \left\{ \begin{array} { l l l } { \left[ \alpha _ { i } , \alpha _ { i } \right] = 0 , } \\ { \left[ \alpha _ { i } , \alpha _ { i } \right] = - [ \alpha _ { j } , \alpha _ { i } ] . } \end{array} \right. } \end{array}
$$

A more important property is that they do not contain the time explicitly； that is,

$$
\frac { \partial [ \alpha _ { i } , \alpha _ { j } ] } { \partial t } = 0 , \qquad ( i = 1 , \cdots , 6 ; j = 1 , \cdots , 6 ) ,
$$

as will be proved immediately.

Many complicated expressions will arise in the following discussion which are symmetrical in $x , y$ ,and $\pmb { z }$ In order to abbreviate the writing let $\boldsymbol { \mathrm { \Sigma } }$ ，standing before a function of $_ x$ ,indicate that the same functions of $y$ and $\pmb { \mathscr { z } }$ are to be added. Thus, for example,

$$
\mathrm { S } ( x _ { 1 } x _ { 2 } ^ { \prime } - x _ { 2 } x _ { 1 } ^ { \prime } ) = ( x _ { 1 } { x _ { 2 } } ^ { \prime } - x _ { 2 } { x _ { 1 } } ^ { \prime } ) + ( y _ { 1 } { y _ { 2 } } ^ { \prime } - y _ { 2 } { y _ { 1 } } ^ { \prime } ) + ( z _ { 1 } { z _ { 2 } } ^ { \prime } - z _ { 2 } z _ { 1 } ^ { \prime } ) .
$$

In starting from the defnitions of the brackets and omitting the subscripts of $x , \cdots , z ^ { \prime }$ ，which will not be of use in what follows, it is found that

$$
\begin{array} { r l r } {  { \frac { \beta [ \alpha _ { i } , \alpha _ { j } ] } { \partial t } = S \{ \frac { \partial ^ { 2 } x } { \partial \alpha _ { i } \partial t } \frac { \partial x ^ { \prime } } { \partial \alpha _ { j } } + \frac { \partial x } { \partial \alpha _ { i } } \frac { \partial ^ { 2 } x ^ { \prime } } { \partial \alpha _ { j } \partial t } - \frac { \partial ^ { 2 } x ^ { \prime } } { \partial \alpha _ { i } \partial t } \frac { \partial x } { \partial \alpha _ { i } } - \frac { \partial x ^ { \prime } } { \partial \alpha _ { i } } \frac { \partial ^ { 2 } x } { \partial \alpha _ { j } \partial t } \} } } \\ & { } & { = \frac { \partial } { \partial \alpha _ { i } } S \{ \frac { \partial x } { \partial t } \frac { \partial x ^ { \prime } } { \partial \alpha _ { j } } - \frac { \partial x ^ { \prime } } { \partial t } \frac { \partial x } { \partial \alpha _ { j } } \} + S \{ - \frac { \partial x } { \partial t } \frac { \partial ^ { 2 } x ^ { \prime } } { \partial \alpha _ { i } \partial \alpha _ { j } } + \frac { \partial x ^ { \prime } } { \partial t } \frac { \partial ^ { 2 } x } { \partial \alpha _ { i } \partial \alpha _ { j } } \} } \\ & { } & { + S \{ \frac { \partial x } { \partial \alpha _ { i } } \frac { \partial ^ { 2 } x ^ { \prime } } { \partial \alpha _ { j } \partial t } - \frac { \partial x ^ { \prime } } { \partial \alpha _ { i } } \frac { \partial ^ { 2 } x } { \partial \alpha _ { j } \partial t } \} } \\ & { } & { = \frac { \partial } { \partial \alpha _ { j } } S \{ \frac { \partial x } { \partial t } \frac { \partial x ^ { \prime } } { \partial \alpha _ { j } } - \frac { \partial x ^ { \prime } } { \partial t } \frac { \partial x } { \partial \alpha _ { j } } \} - \frac { \partial } { \partial \alpha _ { j } } S \{ \frac { \partial x } { \partial t } \frac { \partial x ^ { \prime } } { \partial \alpha _ { i } } - \frac { \partial x ^ { \prime } } { \partial t } \frac { \partial x } { \partial \alpha _ { i } } \} . } \end{array}
$$

The partial derivatives of the coordinates with respect to the time are the same in disturbed motion as the total derivatives in undisturbed motion. Therefore this equation becomes as a consequence of (14)

$$
\begin{array} { r l } & { \frac { \partial \left[ \alpha _ { i } , \alpha _ { j } \right] } { \partial t } = \frac { \partial } { \partial \alpha _ { i } } S \left\{ \frac { \partial \Omega } { \partial x } \ \frac { \partial x } { \partial \alpha _ { j } } + \frac { \partial \Omega } { \partial x ^ { \prime } } \ \frac { \partial x ^ { \prime } } { \partial \alpha _ { i } } \right\} - \frac { \partial } { \partial \alpha _ { i } } S \left\{ \frac { \partial \Omega } { \partial x } \ \frac { \partial x } { \partial \alpha _ { i } } + \frac { \partial \Omega } { \partial x ^ { \prime } } \ \frac { \partial x ^ { \prime } } { \partial \alpha _ { i } } \right\} } \\ & { \quad \quad \quad \quad \quad \quad = \frac { \partial } { \partial \alpha _ { i } } \left( \frac { \partial \Omega } { \partial \alpha _ { i } } \right) - \frac { \partial } { \partial \alpha _ { i } } \left( \frac { \partial \Omega } { \partial \alpha _ { i } } \right) = \frac { \partial ^ { 2 } \Omega } { \partial \alpha _ { i } \partial \alpha _ { i } } - \frac { \partial ^ { 2 } \Omega } { \partial \alpha _ { j } \partial \alpha _ { i } } = 0 , } \end{array}
$$

which proves the theorem that the brackets do not contain $\pmb { \theta }$ explicitly. This would hardly be anticipated since each of the quantities which appears in the brackets is an explicit function of $t$

Since the brackets do not contain the time explicitly they may be computed for any epoch whatever,and in particular for $t = t _ { 0 }$ The equations become very simple if the coordinates at the time $t = t _ { 0 }$ are taken for the elements $\alpha _ { 1 } , \cdots , \alpha _ { 6 } .$ ，This is permissible since the ordinary elements are defined by these quantities,and conversely. It must not be supposed that they are constants; they are such quantities that if the elements are computed from them,and then if the coordinates at any time $t$ are computed using these elements,the correct results will be obtained. Since in disturbed motion the elements vary with the time,the values of the coordinates at $t = t _ { 0 }$ also vary.Otherwise considered, if the osculating elements at $t$ are used and if the coordinates at the time $t = t _ { 0 }$ are computed,it will be found in the case of disturbed motion that the coordinates at $t = t _ { 0 }$ vary,and these values of the coordinates are the ones in question.

Let the coordinates at the time $t = t _ { 0 }$ be $\boldsymbol { x } _ { 0 } , \cdots , \boldsymbol { z } _ { 0 } ^ { \prime }$ ； then

$$
\begin{array} { r } { \left[ x _ { 0 } , y _ { 0 } \right] = S \left\{ \frac { \partial x _ { 0 } } { \partial x _ { 0 } } \frac { \partial x _ { 0 } ^ { \prime } } { \partial y _ { 0 } } - \frac { \partial x _ { 0 } ^ { \prime } } { \partial x _ { 0 } } \frac { \partial x _ { 0 } } { \partial y _ { 0 } } \right\} , } \end{array}
$$

which equals zero because ${ x _ { 0 } } ^ { \prime }$ is independent of $y _ { 0 }$ and $\pmb { x _ { 0 } }$ Similarly，

$$
\begin{array} { r } { { \textstyle \int } [ y _ { 0 } , z _ { 0 } ] = [ z _ { 0 } , x _ { 0 } ] = [ x _ { 0 } , y _ { 0 } ^ { \prime } ] = [ y _ { 0 } , z _ { 0 } ^ { \prime } ] = [ z _ { 0 } , x _ { 0 } ^ { \prime } ] = [ x _ { 0 } , y _ { 0 } ] = 0 , } \\ { { \textstyle \binom { x _ { 0 } , y _ { 0 } ^ { \prime } } { x _ { 0 } , y _ { 0 } ^ { \prime } } } = [ x _ { 0 } , z _ { 0 } ^ { \prime } ] = [ y _ { 0 } , x _ { 0 } ^ { \prime } ] = [ y _ { 0 } , z _ { 0 } ^ { \prime } ] = [ z _ { 0 } , x _ { 0 } ^ { \prime } ] = [ z _ { 0 } , y _ { 0 } ^ { \prime } ] = 0 . } \end{array}
$$

But

$$
[ x _ { 0 } , x _ { 0 } { ' } ] = [ y _ { 0 } , y _ { 0 } { ' } ] = [ z _ { 0 } , z _ { 0 } { ' } ] = 1 .
$$

Therefore equations (33) become in this case

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { x _ { 0 } } ^ { \prime } } , \quad } & { \displaystyle \frac { d x _ { 0 } ^ { \prime } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x _ { 0 } } , } \\ { \displaystyle \frac { d y _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { y _ { 0 } } ^ { \prime } } , \quad } & { \displaystyle \frac { d y _ { 0 } ^ { \prime } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y _ { 0 } } , } \\ { \displaystyle \frac { d z _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { z _ { 0 } } ^ { \prime } } , \quad } & { \displaystyle \frac { d z _ { 0 } ^ { \prime } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 0 } } . } \end{array} \right.
$$

Any system of differential equations of the form (38) is known as a canonical system,and they possess properties which make them particularly valuable in theoretical investigations. There is a theorem that any dynamical problem in which the forces can be represented as partial derivatives of a potential function can be expressed in this form；and if it is possible to put a problem in the canonical form it is possble to do so in infinitely many systems of dependent variables.

If equations (38) were solved they would give the values of the coordinates at $\scriptstyle t _ { 0 }$ which would have to be used to obtain the true coordinates at the time $\mathbf { \Delta } _ { t _ { i } }$ ，under the supposition that the planet moved in an undisturbed ellipse during $t - t _ { 0 }$ If the variables were the elliptic elements the solutions of the equations would give the elements which would have to be used to compute the coordinates at the time $t _ { \mathrm { { i } } }$ ，when they are supposed to have been constant during the interval $t - t _ { 0 }$ .Thus,when the elements have been found the remainder of the computation is that of undisturbed motion.

214.Transformation to the Ordinary Elements. The elements used in Astronomy are not the coordinates at $t = t _ { 0 }$ but $\delta \circ , \ i , \ a ,$ $e , \pi ,$ and $\pmb { T }$ (or $\epsilon = \pi - n T ,$ )，which were expressed in terms of the initial ccnditions in Arts. 86,87,and 88. It will be necessary, therefore,to transform equations (38) to the corresponding ones which involve only the elements which are actually in use by astronomers.

Let s represent any one of the elements $\vartheta \vartheta , i , a , e , \pi ,$ e. It may be expressed symbolically in terms of the initial conditions by

$$
s = f ( x _ { 0 } , y _ { 0 } , z _ { 0 } , x _ { 0 } ^ { \prime } , y _ { 0 } ^ { \prime } , z _ { 0 } ^ { \prime } ) .
$$

Hence it follows that

$$
{ \frac { d s } { d t } } = S \left\{ { \frac { \partial f } { \partial x _ { 0 } } } { \frac { d x _ { 0 } } { d t } } + { \frac { \partial f } { \partial x _ { 0 } } } { \frac { d x _ { 0 } { ' } } { d t } } \right\} ;
$$

or, because of (38),

$$
\frac { d s } { d t } = m _ { 2 } S \left\{ \frac { \partial f } { \partial x _ { 0 } } \frac { \partial R _ { 1 , ~ 2 } } { \partial x _ { 0 } ^ { \prime } } - \frac { \partial f } { \partial x _ { 0 } ^ { \prime } } \frac { \partial R _ { 1 , ~ 2 } } { \partial x _ { 0 } } \right\} .
$$

The partial derivatives of $\scriptstyle R _ { 1 , \ 2 }$ are expressed in terms of the partial derivatives with respect to the new variables by the equations

$$
\left\{ \begin{array} { r } { \frac { \partial R _ { 1 , \ 2 } } { \partial x _ { 0 } } = \frac { \partial R _ { 1 , \ 2 } } { \partial \otimes \partial } \frac { \partial \otimes } { \partial x _ { 0 } } + \frac { \partial R _ { 1 , \ 2 } } { \partial i } \frac { \partial i } { \partial x _ { 0 } } + \frac { \partial R _ { 1 , \ 2 } } { \partial a } \frac { \partial a } { \partial x _ { 0 } } + \frac { \partial R _ { 1 , \ 2 } } { \partial e } \frac { \partial e } { \partial e } } \\ { + \frac { \partial R _ { 1 , \ 2 } } { \partial \pi } \frac { \partial \pi } { \partial x _ { 0 } } + \frac { \partial R _ { 1 , \ 2 } } { \partial \epsilon } \frac { \partial \epsilon } { \partial x _ { 0 } } , } \\ { \cdot \ \cdot \cdot \ \cdot \ \cdot \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \cdot \ \ \ \cdot \ \ \cdot \ \ \ \cdot \ \ \cdot \ \ \ \cdot \ \ \cdot \ \ \ \cdot \ \ \cdot \ \ \ \cdot } \\ { \frac { \partial R _ { 1 , \ 2 } } { \partial z _ { 0 } ^ { \prime } } = \frac { \partial R _ { 1 , \ 2 } } { \partial \otimes \partial } \frac { \partial \otimes } { \partial z _ { 0 } ^ { \prime } } + \frac { \partial R _ { 1 , \ 2 } } { \partial i } \frac { \partial i } { \partial z _ { 0 } ^ { \prime } } + \frac { \partial R _ { 1 , \ 2 } } { \partial a } \frac { \partial a } { \partial z _ { 0 } ^ { \prime } } + \frac { \partial R _ { 1 , \ 2 } } { \partial e } \frac { \partial e } { \partial z _ { 0 } ^ { \prime } } } \\ { + \frac { \partial R _ { 1 , \ 2 } } { \partial \pi } \frac { \partial \pi } { \partial z _ { 0 } ^ { \prime } } + \frac { \partial R _ { 1 , \ 2 } } { \partial \epsilon } \frac { \partial \epsilon } { \partial z _ { 0 } ^ { \prime } } . } \end{array} \right.
$$

On carrying out the complicated computations of ${ \frac { \partial s } { \partial { x _ { 0 } } } } , \ \cdots , \ { \frac { \partial s } { \partial { z _ { 0 } } ^ { \prime } } }$ by means of the equations given in Arts.86,87,and 88,and expressing all the partial derivatives in terms of the new variables, the partial derivatives $\textstyle { \frac { \partial R _ { 1 , ~ 2 } } { \partial x _ { 0 } } } , ~ \cdots , { \frac { \partial R _ { 1 , ~ 2 } } { \partial z _ { 0 } ^ { \prime } } }$ are found in terms of the elements and $\frac { \partial R _ { 1 , ~ 2 } } { \partial \otimes } , \ldots , \frac { \partial R _ { 1 , ~ 2 } } { \partial \epsilon }$ On substituting in (40) and expressing ${ \frac { \partial f } { \partial { x _ { 0 } } } } , \ldots , { \frac { \partial { f } } { \partial { z _ { 0 } } ^ { \prime } } }$ in terms of the ements, $\frac { d s } { d t }$ is found in terms of the elements and the derivatives of the perturbative function, $R _ { 1 , \ 2 } ,$ with respect to the elements.

215.Method of Direct Computation of Lagrange's Brackets. The transformations required in the method of the preceding article are very laborious,and the direct computation of the brackets, though considerably involved, is to be preferred from a practical point of view. All of the computation in the transformations of this sort might be avoided by using canonical variables;but, in order to employ them,a lengthy digression upon the properties of canonical systems would be necessary,and such a discussion is outside the limits of this work． Still, the labor may be notably reduced by first taking elements somewhat different from those defined in chapter V.,and then transforming to those in more ordinary use. The following is based on Tisserand's exposition of Lagrange's method.\*

\* Tisserand's Mecanique Celeste,vol.1., p.179.

Let the xy-plane be the plane of the ecliptic, $\boldsymbol { \delta \mathcal { P } }$ the projectior: of the orbit upon the celestial sphere, $\pi$ the projection of the perihelion point,and $P$ the projection of the position of the planet at the time $t .$ In place of $\pmb { \pi }$ and $\epsilon$ ,adopt the new elements $\omega$ and $\pmb { \sigma } ^ { - }$ defined by the equations

$$
\left\{ { \begin{array} { l } { \omega = \pi - \Omega , } \\ { \sigma = - n T . } \end{array} } \right.
$$

![](images/0e2d53c10223a4f32bf5e30966186651852f12d46d5998884a9b4bc2a39ea96e.jpg)  
Fig. 60.

The following equations are either given in Art.98,or are obtained from Fig. 60 by the fundamental formulas of Trigonometry:

$$
\left\{ \begin{array} { l l } { \begin{array} { r l } & { n - \frac { k \cdot \sqrt { S } + m } { \sigma ^ { 4 } } , } \\ & { R - \epsilon \sin B - \eta + \sigma } \\ & { \tau = a ( 1 - \epsilon \cos B ) , } \\ { \tan \frac { \eta } { 2 } - \sqrt { \frac { 1 + \epsilon } { 1 - \epsilon } } \epsilon \sin B , } \end{array} } \\ { \begin{array} { r l } { \epsilon \cos \eta } & { \epsilon = \frac { \cos E - \epsilon } { 1 - \epsilon \cos B } , } \\ { \sin \theta } & { \epsilon = \frac { \sin B - \epsilon } { 1 - \epsilon \cos B } , } \\ { \epsilon \sin \theta } & { \epsilon = \frac { \sin B } { \sqrt { 1 - \epsilon } } \epsilon \sin B , } \end{array} } \\ { \begin{array} { r l } { \pi = \eta \cos \left( \epsilon + \omega \right) \cos } & { \epsilon } \\ { \theta = \tau \sin \left( \theta + \omega \right) \sin } & { \epsilon = \frac { \sin B + \epsilon } { \sqrt { 1 - \epsilon } } \epsilon \sin B } \end{array} } \\ { \begin{array} { r l } { \epsilon = \pi \sin \left( \epsilon + \omega \right) \sin } & { \epsilon = \frac { \sin B + \epsilon } { \sqrt { 1 - \epsilon } } \epsilon \sin B } \\ { \epsilon = \pi \sin \left( \epsilon + \omega \right) \sin } & { \epsilon = \frac { \sin B + \epsilon } { \sqrt { 1 - \epsilon } } \epsilon \sin B } \end{array} } \end{array} \right.
$$

From these equations and their derivatives with respect to the time the partial derivatives of the coordinates with respect to the elements can be computed. The elements have been chosen in such a manner that they are divided into two groups having distinct properties; $\delta \boldsymbol { \mathbf { \rho } } , i ,$ and $\omega$ define the position of the plane of motion and the orientation of the orbit in the plane,and $a , \ e ,$ and $\pmb { \sigma }$ define the dimensions and shape of the orbit and the position of the planet in its orbit. Therefore the coordinates in the orbit can be expressed in terms of the elements of the second group alone,and from them, the coördinates in space can be found by means of the first group alone.

Take a new system of axes with the origin at the sun,the positive end of the $\xi$ -axis directed to the perihelion point,the $\pmb { \eta }$ -axis $9 0 ^ { \circ }$ forward in the plane of the orbit,and the $\boldsymbol { \zeta }$ -axis perpendicular to the plane of the orbit. Let the direction cosines between the $\pmb { x }$ -axis and the $\xi , \eta ,$ and $\boldsymbol { \zeta }$ -axes be $\alpha , \alpha ^ { \prime } , \alpha ^ { \prime \prime }$ ;between the $y .$ -axis and the $\xi , \ \eta ,$ and $\boldsymbol { \zeta } \mathrm { . }$ -axes be $\beta , \ \beta ^ { \prime } , \ \beta ^ { \prime \prime }$ ； and between the ${ \pmb z } .$ -axis and the $\xi , \eta ,$ and $\boldsymbol { \xi }$ -axes be $\gamma , \gamma ^ { \prime } , \gamma ^ { \prime \prime }$ ．Then it follows from Fig. 60 that

$$
\left\{ \begin{array} { l l } { \alpha = \cos \omega \cos \bigotimes \bigtriangleup - \sin \omega \sin \bigtriangleup \cos { i } , } \\ { \beta = \cos \omega \sin \bigtriangleup \big + \sin \omega \cos \bigtriangleup \cos { i } , } \\ { \gamma = \sin \omega \sin { i } , } \\ { \alpha ^ { \prime } = - \sin \omega \cos \bigtriangleup - \cos \omega \sin \bigtriangleup \cos { i } , } \\ { \beta ^ { \prime } = - \sin \omega \sin \bigtriangleup + \cos \omega \cos \bigtriangleup \cos { i } , } \\ { \gamma ^ { \prime } = \cos \omega \sin { i } , } \\ { \alpha ^ { \prime \prime } = \sin \bigtriangleup \sin { i } , } \\ { \beta ^ { \prime \prime } = - \cos \bigtriangleup \bigtriangleup \sin { i } , } \\ { \gamma ^ { \prime \prime } = \cos { i } . } \end{array} \right.
$$

There exist among these nine direction cosines,as can easily be verified,the relations

$$
\left\{ \begin{array} { l l } { \qquad \alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { 2 } = 1 , } & { \qquad \alpha \alpha ^ { \prime } + \beta \beta ^ { \prime } + \gamma \gamma ^ { \prime } = 0 , } \\ { \qquad \alpha ^ { \prime } { } ^ { 2 } + \beta ^ { \prime } { } ^ { 2 } + \gamma ^ { \prime } { } ^ { 2 } = 1 , } & { \qquad \alpha ^ { \prime } \alpha ^ { \prime \prime } + \beta ^ { \prime } \beta ^ { \prime \prime } + \gamma ^ { \prime } \gamma ^ { \prime \prime } = 0 , } \\ { \alpha ^ { \prime \prime } { } ^ { 2 } + \beta ^ { \prime \prime } { } ^ { 2 } + \gamma ^ { \prime \prime } { } ^ { 2 } = 1 , } & { \qquad \alpha ^ { \prime \prime } \alpha + \beta ^ { \prime \prime } \beta + \gamma ^ { \prime \prime } \gamma = 0 , } \\ { \alpha = \beta ^ { \prime } \gamma ^ { \prime \prime } - \gamma ^ { \prime } \beta ^ { \prime \prime } , } & { \alpha ^ { \prime } = \beta ^ { \prime \prime } \gamma - \gamma ^ { \prime \prime } \beta , \quad \alpha ^ { \prime \prime } = \beta \gamma ^ { \prime } - \gamma \beta ^ { \prime } , } \\ { \beta = \gamma ^ { \prime } \alpha ^ { \prime \prime } - \alpha ^ { \prime } \gamma ^ { \prime \prime } , } & { \beta ^ { \prime } = \gamma ^ { \prime \prime } \alpha - \alpha ^ { \prime \prime } \gamma , \quad \beta ^ { \prime \prime } = \gamma \alpha ^ { \prime } - \alpha \gamma ^ { \prime } , } \\ { \gamma = \alpha ^ { \prime } \beta ^ { \prime \prime } - \beta ^ { \prime } \alpha ^ { \prime \prime } , } & { \gamma ^ { \prime } = \alpha ^ { \prime \prime } \beta - \beta ^ { \prime \prime } \alpha , \quad \gamma ^ { \prime \prime } = \alpha \beta ^ { \prime } - \beta \alpha ^ { \prime } . } \end{array} \right.
$$

It follows from (43) and (44) and the definition of the new system of axes that

$$
\left\{ \begin{array} { l l } { \displaystyle \xi = r \cos v = a ( \cos B - e ) , \quad \eta = a \sqrt { 1 - e ^ { a } } \sin B , } \\ { \displaystyle \frac { \partial B } { \partial t } = \frac { n } { 1 - e \cos B } , } \\ { \displaystyle \xi ^ { \prime } = \frac { - \pi a \sin B } { 1 - e \cos B } = \frac { - k \sqrt { 1 + m } \sin B } { \sqrt { a } ( 1 - e \cos B ) } , } \\ { \displaystyle \eta ^ { \prime } = \frac { n a \sqrt { 1 - e ^ { a } } \cos B } { 1 - e \cos B } = \frac { k \sqrt { 3 + m } \sin \sqrt { 1 - e ^ { a } } \cos B } { \sqrt { a } ( 1 - e \cos B ) } , } \\ { \displaystyle x = \alpha \xi + \alpha \eta , \quad y = \beta \xi , \quad z = \gamma \xi + \gamma \eta , } \\ { \displaystyle x ^ { \prime } = \alpha \xi ^ { \prime } + \alpha ^ { \prime \prime } , \quad y ^ { \prime } = \beta \xi ^ { \prime } + \beta ^ { \prime \prime } , \quad z ^ { \prime } = \gamma \xi ^ { \prime } + \gamma \eta ^ { \prime } , } \end{array} \right.
$$

where the accents on ${ \pmb x } , ~ { \pmb y } , ~ { \pmb z } , ~ { \pmb \xi } , ~ { \pmb \eta } ,$ and $\pmb { \zeta }$ indicate first derivatives with respect to $\pmb { t }$

The partial derivatives of $\alpha , \cdots , \gamma ^ { \prime \prime }$ with respect to the elements may be computed once for all; they are found from (44) to be

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \omega } = \alpha ^ { \prime } , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \omega } = - \alpha , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime \prime } } { \partial \omega } = 0 , } \\ { \displaystyle \frac { \partial \beta } { \partial \omega } = \beta ^ { \prime } , \quad } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \omega } = - \beta , \quad } & { \displaystyle \frac { \partial \beta ^ { \prime \prime } } { \partial \omega } = 0 , } \\ { \displaystyle \frac { \partial \gamma } { \partial \omega } = \gamma ^ { \prime } , \quad } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \omega } = - \gamma , \quad } & { \displaystyle \frac { \partial \gamma ^ { \prime \prime } } { \partial \omega } = 0 ; } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \bigotimes } = - \ \beta , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \bigotimes } = \ - \ \beta ^ { \prime } , \quad \quad \frac { \partial \alpha ^ { \prime \prime } } { \partial \bigotimes } = \ - \ \beta ^ { \prime \prime } , } \\ { \displaystyle \frac { \partial \beta } { \partial \bigotimes } = \alpha , \quad } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \bigotimes } = \alpha ^ { \prime } , \quad \qquad \frac { \partial \beta ^ { \prime \prime } } { \partial \bigotimes } = \alpha ^ { \prime \prime } , } \\ { \displaystyle \frac { \partial \gamma } { \partial \bigotimes } = 0 , \quad } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \bigotimes } = 0 , \quad \qquad \quad \frac { \partial \gamma ^ { \prime \prime } } { \partial \bigotimes } = 0 ; } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \dot { \iota } } = \alpha ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \dot { \iota } } = \alpha ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \alpha ^ { \prime \prime } } { \partial \dot { \iota } } = + \sin \Omega \cos \dot { \iota } , } \\ { \displaystyle \frac { \partial \beta } { \partial \dot { \iota } } = \beta ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \dot { \iota } } = \beta ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \beta ^ { \prime \prime } } { \partial \dot { \iota } } = - \cos \Omega \cos \dot { \iota } , } \\ { \displaystyle \frac { \partial \gamma } { \partial \dot { \iota } } = \gamma ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \dot { \iota } } = \gamma ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \gamma ^ { \prime \prime } } { \partial \dot { \iota } } = - \sin \dot { \iota } . } \end{array} \right.
$$

There are as many brackets to be computed as there are combinations of the six elements taken two at a time, or $\frac { 6 ! } { 2 ! 4 ! } = 1 5 .$ Three of them involve elements of only the frst group;nine,one element of the first group and one of the second;and three,elements of only the second group.Let $\kappa$ and $L$ represent any of the elements of the first group, $\vartheta , i , \omega _ { \astrosun }$ and $P$ and $Q$ any of the elements of the second group, $a , \ e , \ \sigma$ ，Then the Lagrangian brackets to be computed are

$$
\left\{ \begin{array} { l l } { \displaystyle ( a ) } & { \displaystyle \left[ K , L \right] = S \left\{ \frac { \partial x } { \partial K } \frac { \partial x ^ { \prime } } { \partial L } - \frac { \partial x ^ { \prime } } { \partial K } \frac { \partial x } { \partial L } \right\} , } & { \mathrm { ( 3 ~ e ~ } \partial x \mathrm { ~ e ~ } \partial x ) } \\ { \displaystyle ( b ) } & { \displaystyle \left[ K , P \right] = S \left\{ \frac { \partial x } { \partial K } \frac { \partial x ^ { \prime } } { \partial P } - \frac { \partial x ^ { \prime } } { \partial K } \frac { \partial x } { \partial P } \right\} , } & { \mathrm { ( 9 ~ e ~ } \partial x \mathrm { ~ e ~ } \partial x ) } \\ { \displaystyle ( c ) } & { \displaystyle \left[ P , \ Q \right] = S \left\{ \frac { \partial x } { \partial P } \frac { \partial x ^ { \prime } } { \partial Q } - \frac { \partial x ^ { \prime } } { \partial P } \frac { \partial x } { \partial Q } \right\} , } & { \mathrm { ( 3 ~ e ~ } \partial x \mathrm { ~ e ~ } \partial x ) } \end{array} \right.
$$

It is found from (46) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial x } { \partial K } = \xi \displaystyle \frac { \partial \alpha } { \partial K } + \eta \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial K } , \quad } & { \displaystyle \frac { \partial x ^ { \prime } } { \partial K } = \xi ^ { \prime } \displaystyle \frac { \partial \alpha } { \partial K } + \eta ^ { \prime } \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial K } , } \\ { \displaystyle \frac { \partial x } { \partial P } = \alpha \displaystyle \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \displaystyle \frac { \partial \eta } { \partial P } , \quad } & { \displaystyle \frac { \partial x ^ { \prime } } { \partial P } = \alpha \displaystyle \frac { \partial \xi ^ { \prime } } { \partial P } + \alpha ^ { \prime } \displaystyle \frac { \partial \eta ^ { \prime } } { \partial P } , } \end{array} \right.
$$

and similar equations in $y$ and $\pmb { z }$

216.Computation of $[ \omega , \ \delta ] , \ [ \delta , \ i ] , \ [ i , \ \omega ]$ Let $\boldsymbol { s }$ indicate that the sum of the functions,symmetrical in $\alpha , ~ \beta .$ and $\gamma$ ,is to be taken. Then the first equation of (5O) becomes as a consequence of (51)

$$
\begin{array} { r } { \left[ K , L \right] = ( \xi \eta ^ { \prime } - \eta \xi ^ { \prime } ) S \left\{ \frac { \partial \alpha } { \partial K } \frac { \partial \alpha ^ { \prime } } { \partial L } - \frac { \partial \alpha ^ { \prime } } { \partial K } \frac { \partial \alpha } { \partial L } \right\} . } \end{array}
$$

But the law of areas [Art.89] gives

$$
\xi \eta ^ { \prime } - \eta \xi ^ { \prime } = \xi \frac { d \eta } { d t } - \eta \frac { d \xi } { d t } = k \sqrt { ( S + m _ { 1 } ) a ( 1 - e ^ { 2 } ) } = n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } .
$$

Therefore

$$
{ } ^ { \left[ { \cal K } , { \cal L } \right] } = n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } S \left\{ \frac { \partial \alpha } { \partial { \cal K } } \frac { \partial \alpha ^ { \prime } } { \partial { \cal L } } - \frac { \partial \alpha ^ { \prime } } { \partial { \cal K } } \frac { \partial \alpha } { \partial { \cal L } } \right\} .
$$

On computing theright member of this equation by means of (47),

(48),and (49),and reducing by means of (45),the brackets involving elements of only the first group are found to be

$$
\{ \begin{array} { l l } { { [ \omega , \otimes ] = n a ^ { 2 } \sqrt { 1 - { \ e ^ { 2 } } } ( - \alpha \beta - \alpha ^ { \prime } \beta ^ { \prime } + \alpha \beta + \alpha ^ { \prime } \beta ^ { \prime } ) = 0 , } } \\ { { [ \mathscr { B } , ~ i ] = n a ^ { 2 } \sqrt { 1 - { \ e ^ { 2 } } } \{ ( \alpha \beta ^ { \prime \prime } - \beta \alpha ^ { \prime \prime } ) \cos \omega  } } \\ { { \qquad \quad  + ( \beta ^ { \prime } \alpha ^ { \prime \prime } - \alpha ^ { \prime } \beta ^ { \prime \prime } ) \sin \omega \} } } \\ { { \qquad = n a ^ { 2 } \sqrt { 1 - { e ^ { 2 } } } ( - \gamma ^ { \prime } \cos \omega - \gamma \sin \omega ) } } \\ { { \qquad = - n a ^ { 2 } \sqrt { 1 - { e ^ { 2 } } } \sin i , } } \\ { { [ i  , ~ \omega ] = - n a ^ { 2 } \sqrt { 1 - { e ^ { 2 } } } \{ ( \alpha ^ { \prime \prime } + \beta ^ { \prime } \beta ^ { \prime \prime } + \gamma ^ { \prime } \gamma ^ { \prime \prime } ) \cos \omega  } }  \\ { { \qquad \quad  ~ + ( \alpha ^ { \prime \prime } \alpha + \beta ^ { \prime \prime } \beta + \gamma ^ { \prime \prime } \gamma ) \sin \omega \} = 0 . } } \end{array} 
$$

217. Computation of $\textstyle [ K , P ]$ .The second equations of (50) become,as a consequence of (51),

$$
\begin{array} { r l } { \left[ K , P \right] = } & { S \Bigg \{ \left[ \xi \frac { \partial \alpha } { \partial K } + \eta \frac { \partial \alpha ^ { \prime } } { \partial K } \right] \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial P } \right] } \\ & { \qquad - \left[ \xi ^ { \prime } \frac { \partial \alpha } { \partial K } + \eta \frac { \partial \alpha ^ { \prime } } { \partial K } \right] \left[ \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial P } \right] \Bigg \} } \\ & { = + \left[ \alpha \frac { \partial \alpha } { \partial K } + \beta \frac { \partial \beta } { \partial K } + \gamma \frac { \partial \gamma } { \partial K } \right] \left[ \xi \frac { \partial \xi ^ { \prime } } { \partial P } - \xi ^ { \prime } \frac { \partial \xi } { \partial P } \right] } \\ & { \qquad + \left[ \alpha ^ { \prime } \frac { \partial \alpha ^ { \prime } } { \partial K } + \beta ^ { \prime } \frac { \partial \beta ^ { \prime } } { \partial K } + \gamma \frac { \partial \gamma ^ { \prime } } { \partial K } \right] \left[ \eta \frac { \partial \eta ^ { \prime } } { \partial P } - \eta ^ { \prime } \frac { \partial \eta } { \partial P } \right] } \\ & { \qquad + \left[ \alpha \frac { \partial \alpha ^ { \prime } } { \partial K } + \beta \frac { \partial \beta ^ { \prime } } { \partial K } + \gamma \frac { \partial \gamma ^ { \prime } } { \partial K } \right] \left[ \eta \frac { \partial \xi ^ { \prime } } { \partial P } - \eta ^ { \prime } \frac { \partial \xi } { \partial P } \right] } \\ & { \qquad + \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial K } + \beta ^ { \prime } \frac { \partial \beta } { \partial K } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial K } \right] \left[ \xi \frac { \partial \eta ^ { \prime } } { \partial P } - \xi ^ { \prime } \frac { \partial \eta } { \partial P } \right] . } \end{array}
$$

It follows from equations (45),(47), (48),and (49) that

$$
\begin{array} { c } { { \alpha \displaystyle \frac { \partial \alpha } { \partial { \cal K } } + \beta \displaystyle \frac { \partial \beta } { \partial { \cal K } } + \gamma \displaystyle \frac { \partial \gamma } { \partial { \cal K } } = 0 , } } \\ { { \alpha ^ { \prime } \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial { \cal K } } + \beta ^ { \prime } \displaystyle \frac { \partial \beta ^ { \prime } } { \partial { \cal K } } + \gamma ^ { \prime } \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial { \cal K } } = 0 , } } \\ { { \alpha \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial { \cal K } } + \beta \displaystyle \frac { \partial \beta ^ { \prime } } { \partial { \cal K } } + \gamma \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial { \cal K } } = - \left[ \alpha ^ { \prime } \displaystyle \frac { \partial \alpha } { \partial { \cal K } } + \beta ^ { \prime } \displaystyle \frac { \partial \beta } { \partial { \cal K } } + \gamma ^ { \prime } \displaystyle \frac { \partial \gamma } { \partial { \cal K } } \right] . } } \end{array}
$$

Therefore

$$
\left\{ \begin{array} { l } { { [ K , P ] = \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \bar { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \bar { K } } + \gamma ^ { \prime } \frac { \partial \zeta } { \partial \bar { K } } \right] } } \\ { { \qquad \times \left[ \xi \frac { \partial \eta ^ { \prime } } { \partial \bar { P } } + \eta ^ { \prime } \frac { \partial \xi } { \partial \bar { P } } - \xi ^ { \prime } \frac { \partial \eta } { \partial \bar { P } } - \eta \frac { \partial \xi ^ { \prime } } { \partial \bar { P } } \right] } } \\ { { \qquad = \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \bar { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \bar { K } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \bar { K } } \right] \frac { \partial ( \xi \eta ^ { \prime } - \eta \xi ^ { \prime } ) } { \partial \bar { P } } } } \\ { { \qquad = k \sqrt { S + m _ { 1 } } \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \bar { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \bar { K } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \bar { K } } \right] \frac { \partial \sqrt { p } } { \partial \bar { P } } . } } \end{array} \right.
$$

Let $P = a , e , \sigma$ in succession. Then it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle k \sqrt { S + m _ { 1 } } \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial a } = \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } , } \\ { \displaystyle k \sqrt { S + m _ { 1 } } \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial e } = - \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } , } \\ { \displaystyle k \sqrt { S + m _ { 1 } } \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial \sigma } = 0 . } \end{array} \right.
$$

Let $K = \omega , \ \delta \circ , i$ in turn in (54),and make use of (55); then it is found that

$$
\left\{ \begin{array} { l l } { \displaystyle [ \omega , a ] = \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } , \qquad \displaystyle [ \omega , e ] = \frac { - n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } , \qquad \displaystyle [ \omega , \sigma ] = 0 , } \\ { \displaystyle [ \otimes , a ] = \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \cos i , \qquad \displaystyle [ i , a ] = 0 , \qquad [ i , e ] = 0 , } \\ { \displaystyle [ \bigotimes , e ] = \frac { - n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } \cos i , \qquad \displaystyle [ \otimes , \sigma ] = 0 , \qquad [ i , \sigma ] = 0 . } \end{array} \right.
$$

218.Computation of $[ a , ~ e ] , ~ [ e , ~ \sigma ] , ~ [ \sigma , ~ a ]$ ，The third equation of (50) becomes,as a consequence of (51),

$$
\begin{array} { r l } & { [ P , Q ] = S \left\{ \left[ \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial P } \right] \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial Q } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial Q } \right] \right. } \\ & { \qquad \left. - \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial P } \right] \left[ \alpha \frac { \partial \xi } { \partial Q } + \alpha ^ { \prime } \frac { \partial \eta } { \partial Q } \right] \right\} } \\ & { = + \left( \alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { 2 } \right) \left[ \frac { \partial \xi } { \partial P } \frac { \partial \xi ^ { \prime } } { \partial Q } - \frac { \partial \xi } { \partial Q } \frac { \partial \xi ^ { \prime } } { \partial P } \right] } \\ & { \qquad + \left( \alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { 2 } \right) \left[ \frac { \partial \eta } { \partial P } \frac { \partial \eta ^ { \prime } } { \partial Q } - \frac { \partial \eta } { \partial Q } \frac { \partial \eta ^ { \prime } } { \partial P } \right] } \\ & { \qquad + \left( \alpha \alpha ^ { \prime } + \beta \beta ^ { \prime } + \gamma \gamma ^ { \prime } \right) \left[ \frac { \partial \xi } { \partial P } \frac { \partial \eta ^ { \prime } } { \partial Q } - \frac { \partial \xi } { \partial Q } \frac { \partial \eta ^ { \prime } } { \partial P } + \frac { \partial \xi ^ { \prime } } { \partial Q } \frac { \partial \xi ^ { \prime } } { \partial P } - \frac { \partial \xi ^ { \prime } } { \partial P } \frac { \partial \eta } { \partial Q } \right] . } \end{array}
$$

As a consequence of equations (45),the right member of this equation reduces to

$$
\left[ P , Q \right] = \frac { \partial \xi } { \partial P } \frac { \partial \xi ^ { \prime } } { \partial Q } - \frac { \partial \xi } { \partial Q } \frac { \partial \xi ^ { \prime } } { \partial P } + \frac { \partial \eta } { \partial P } \frac { \partial \eta ^ { \prime } } { \partial Q } - \frac { \partial \eta } { \partial Q } \frac { \partial \eta ^ { \prime } } { \partial P } .
$$

Since the brackets do not contain the time explicitly $\pmb { t }$ may be given any value after the partial derivatives have been formed. The partial derivatives become the simplest when $\mathbf { \nabla } t = T$ ,the time of perihelion passage. For this value of $t , E = 0 ;$ $r = a ( { \bf 1 } - e ) _ { \mathrm { : } }$ and it is found from equations (46) that\*

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { \partial \xi } { \partial a } } = { 1 - e } , } & { \displaystyle { \frac { \partial \eta } { \partial a } } = 0 , \frac { \partial \xi ^ { \prime } } { \partial a } = 0 , \frac { \partial \eta ^ { \prime } } { \partial a } = - \frac { n } { 2 } \sqrt { \frac { 1 + e } { 1 - e } } , } \\ { \displaystyle { \frac { \partial \xi } { \partial e } } = - a , } & { \displaystyle { \frac { \partial \eta } { \partial e } } = 0 , \frac { \partial \xi ^ { \prime } } { \partial e } = 0 , \frac { \partial \eta ^ { \prime } } { \partial e } = \frac { 1 } { 1 - e } \cdot \frac { n a } { \sqrt { 1 - e ^ { 2 } } } , } \\ { \displaystyle { \frac { \partial \xi } { \partial \sigma } } = 0 , \quad \displaystyle { \frac { \partial \eta } { \partial \sigma } } = a \sqrt { \frac { 1 + e } { 1 - e } } , \frac { \partial \xi ^ { \prime } } { \partial \sigma } = \frac { - n a } { ( 1 - e ) ^ { 2 } } , \frac { \partial \eta ^ { \prime } } { \partial \sigma } = 0 } \end{array} \right.
$$

Then equation (57） gives

$$
\left[ a , e \right] = 0 , \qquad \left[ e , \sigma \right] = 0 , \qquad \left[ \sigma , a \right] = \frac { n a } { 2 } .
$$

On making use of the fact that $[ \alpha _ { i } , \alpha _ { i } ] = - [ \alpha _ { i } , \alpha _ { i } ]$ and equations (53),(56),and (59),equations (33) become

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \frac { d a } { d t } - \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } \frac { d e } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \omega } , } } \\ { \displaystyle { - \ n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin i \frac { d i } { d t } + \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \cos i \frac { d a } { d t } } } \\ { \displaystyle { - \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } \cos i \frac { d e } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \ S _ { 0 } } , } } \\ { \displaystyle { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin i \frac { d \otimes } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial i } , } } \end{array} \right.
$$

\* It hould be remembered that $^ { a }$ and $\pmb { e }$ enter explicitly and also implicitly through $\pmb { \mathscr { L } }$ and $\pmb { n }$ ,for $\pmb { \cal E }$ is defined by the equation

$$
E \mathrm { ~ - ~ } e \sin E \mathrm { ~ = ~ } n ( t \mathrm { ~ - ~ } T ) \mathrm { ~ = ~ } \frac { k \sqrt { S + m _ { 1 } } } { a \dag } ( t \mathrm { ~ - ~ } T ) .
$$

Then,e.g., ${ \frac { \partial \xi } { \partial a } } = \cos { \cal E } - e - a$ sin $\pmb { \cal E } \frac { \partial \pmb { \cal E } } { \partial \pmb { a } } = { \bf 1 } - e$ when $\mathbf { \nabla } _ { t } = \mathbf { \nabla } _ { T }$ ete.

$$
\left\{ \begin{array} { l l } { - \displaystyle \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \displaystyle \frac { d \omega } { d t } - \displaystyle \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \cos i \displaystyle \frac { d \Omega } { \partial t } - \displaystyle \frac { n a } { 2 } \displaystyle \frac { d \sigma } { d t } = m _ { \mathrm { \mathfrak { z } } } \displaystyle \frac { \partial R _ { 1 , \mathrm { ~ 2 } } } { \partial a } , } \\ { \displaystyle \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } \displaystyle \frac { d \omega } { d t } + \displaystyle \frac { n a ^ { 2 } e \cos i } { \sqrt { 1 - e ^ { 2 } } } \displaystyle \frac { d \Omega } { d t } = m _ { \mathrm { z } } \displaystyle \frac { \partial R _ { 1 , \mathrm { ~ 2 } } } { \partial e } , } \\ { \displaystyle \frac { n a } { 2 } \displaystyle \frac { d a } { d t } = m _ { \mathrm { z } } \displaystyle \frac { \partial R _ { 1 , \mathrm { ~ 2 } } } { \partial \sigma } . } \end{array} \right.
$$

These equations are easily solved for the derivatives,and give

$$
\begin{array} { r l } & { [ \frac { d \hat { \Omega } _ { 3 } } { d t } = \frac { m _ { 2 } } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } } \sin i } \frac { \partial R _ { 1 , 2 } } { \partial i } ,  } \\ & {  [ \frac { d \vec { i } } { d t }   = \frac { m _ { 2 } \cos i } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } \sin i } } \frac { \partial R _ { 1 , 2 } } { \partial i } - \frac { m _ { 2 } } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } \sin i } } \frac { \partial R _ { 1 , 2 } } { \partial \Delta } ,   } \\ & {   [ \frac { d \omega } { d t }   - \frac { m _ { 2 } \cos i } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } \sin i } } \frac { \partial R _ { 1 , 2 } } { \partial i } + \frac { m _ { 2 } \sqrt { 1 - \ell ^ { 2 } } } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } \cos i } } \frac { \partial R _ { 1 , 2 } } { \partial \theta } ,    } \\ & {     ] \frac { d \alpha } { d t }    = \frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , 2 } } { \partial \sigma } ,   } \\ & {   [ \frac { d \vec { i } } { d t }    = \frac { m _ { 2 } ( 1 - \ell ^ { 2 } ) } { n a ^ { 2 } \sqrt { 1 - \ell ^ { 2 } } } \frac { \partial R _ { 1 , 2 } } { \partial \sigma } - \frac { m _ { 2 } \sqrt { 1 - \ell ^ { 2 } } } { n a ^ { 2 } \sqrt { \ell ^ { 2 } } } \frac { \partial R _ { 1 , 2 } } { \partial \omega } ,    } \\ & {    \frac { d \vec { i } } { d t }   - \frac { m _ { 2 } ( 1 - \ell ^ { 2 } ) } { n a ^ { 2 } \sqrt { \ell ^ { 2 } } } \frac { \partial R _ { 1 , 2 } } { \partial \theta } - \frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , 2 } } { \partial \theta } \frac { \partial R _ { 1 , 2 } } { \partial \theta } .  } \\ &    \frac { d \vec { i } }  d t  \end{array}
$$

The perturbative function $\scriptstyle R _ { 1 , \ 2 }$ involves the element $^ { a }$ explicitly, and also implicitly through $\mathscr { n }$ which enters only in the combination $n t + \sigma$ ，Consequently the last equation of (61） becomes

$$
\frac { d \sigma } { d t } = - \frac { m _ { 2 } ( 1 - e ^ { 2 } ) } { n a ^ { 2 } e } \frac { \partial R _ { 1 , ~ 2 } } { \partial e } - \frac { 2 m _ { 2 } } { n a } \left( \frac { \partial R _ { 1 , ~ 2 } } { \partial a } \right) - \frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , ~ 2 } } { \partial n } \frac { \partial n } { \partial a } ,
$$

where the partial derivative in parenthesis indicates the derivative is taken only so far as the parameter appears explicitly.

It follows from the combination $n t + \sigma$ that

$$
\frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , ~ 2 } } { \partial n } = \frac { 2 m _ { 2 } t } { n a } \frac { \partial R _ { 1 , ~ 2 } } { \partial \sigma } = t \frac { d a } { d t } .
$$

It will be shown [Arts. 225-227] that R1,2 s a sum of periodic terms; therefore $\pmb { \sigma }$ ，as defined by (62)，contains terms which are the products of $t$ and trigonometric terms. It is obvious that such an element is inconvenient when large values of $\pmb { t }$ are to be used.

In order to avoid this difficulty Leverrier used\* in place of $\pmb { \sigma }$ the mean longitude from the perihelion as an element. It is defined by

$$
l = \int n d t + \sigma ,
$$

whence

$$
\frac { d l } { d \sp { \prime } } = n + i \frac { d n } { d t } + \frac { d \sigma } { d t } .
$$

Since $n = { \frac { k { \sqrt { S + m _ { 1 } } } } { a ^ { \frac { 3 } { 2 } } } }$ , it follows that

$$
{ \frac { \partial n } { \partial a } } = - { \frac { 3 } { 2 } } { \frac { n } { a } } , \quad \quad \quad { \frac { d n } { d t } } = - { \frac { 3 n } { 2 a } } { \frac { d a } { d t } } \cdotp
$$

Therefore equation (65) becomes,on making use of (62),

$$
\frac { d l } { d t } = n - \frac { m _ { 2 } ( 1 - e ^ { 2 } ) } { n a ^ { 2 } e } \frac { \partial R _ { 1 , 2 } } { \partial e } - \frac { 2 m _ { 2 } } { n a } \left( \frac { \partial R _ { 1 , 2 } } { \partial a } \right) .
$$

Since $\frac { \partial R _ { 1 , ~ 2 } } { \partial \sigma } = \frac { \partial R _ { 1 , ~ 2 } } { \partial l }$ thefourthndfoea the partial derivative of $R _ { 1 , \ 2 }$ with respect to $\pmb { \sigma }$ occurs,will not be changed in form. Hence,if $\iota$ is used in place of $\pmb { \sigma }$ throughout (61), the equations will be unchanged in form,and the partial derivative of $R _ { 1 , \textbf { 2 } }$ with respect to $^ { a }$ is to be taken only so far as $^ { a }$ occurs explicitly.

219.Change from $\delta \circ , \ \omega ,$ and $\pmb { \sigma }$ to $\delta , ~ \pi ,$ and e. The transformation from the elements $\delta \circ , \ \omega _ { : }$ and $\pmb { \sigma }$ to $\delta \delta , \ \pi ,$ and $\pmb { \epsilon }$ is readily made because the relations between the $\omega$ and $\pmb { \sigma }$ and the $\pmb { \pi }$ and e are very simple. It follows from the definitions of Arts. 214 and 215 that

$$
\left\{ \begin{array} { l l } { \displaystyle { \delta = \delta } , } \\ { \displaystyle { \omega = \pi - \delta } , } \\ { \displaystyle { \sigma = \epsilon - \pi } ; } \end{array} \right.
$$

whence

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d \otimes } { d t } = \frac { d \otimes } { d t } , } \\ { \displaystyle \frac { d \omega } { d t } = \frac { d \pi } { d t } - \frac { d \otimes } { d t } , } \\ { \displaystyle \frac { d \sigma } { d t } = \frac { d \epsilon } { d t } - \frac { d \pi } { d t } . } \end{array} \right.
$$

On solving (68) for $\delta \circ , \pi ,$ and $\epsilon$ in terms of $\delta \circ , \omega ,$ and $\pmb { \sigma }$ ,it is found that

\* Annales de l'Observatoire de Paris, vol.I., p. 255.

$$
\left\{ \begin{array} { l l } { \delta = \delta , } \\ { \pi = \omega + \delta , } \\ { \epsilon = \sigma + \pi = \sigma + \omega + \delta . } \end{array} \right.
$$

Hence the transformations in the partial derivatives are given by the equations

$$
\left\{ \begin{array} { l l } { \frac { \partial R _ { 1 , 2 } } { \partial \Omega } = \left( \frac { \partial R _ { 1 , 2 } } { \partial \Omega } \right) \frac { \partial \tilde { \mathcal { Q } } _ { \Lambda } } { \partial \tilde { \mathcal { Q } } } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) \frac { \partial \pi } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } \right) \frac { \partial \epsilon } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } } \\ { \quad = \left( \frac { \partial R _ { 1 , 2 } } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } \right) + \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) + \left( \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \right) , } \\ { \frac { \partial R _ { 1 , 2 } } { \partial \omega } = \left( \frac { \partial R _ { 1 , 2 } } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } \right) \frac { \partial \tilde { \mathcal { Q } } _ { \Lambda } } { \partial \omega } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) \frac { \partial \pi } { \partial \omega } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \right) \frac { \partial \epsilon } { \partial \omega } } \\ { \quad = \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) + \left( \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \right) , } \\ { \frac { \partial R _ { 1 , 2 } } { \partial \sigma } = \left( \frac { \partial R _ { 1 , 2 } } { \partial \tilde { \mathcal { Q } } _ { \Lambda } } \right) \frac { \partial \tilde { \mathcal { Q } } _ { \Lambda } } { \partial \sigma } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) \frac { \partial \pi } { \partial \sigma } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \right) \frac { \partial \epsilon } { \partial \sigma } } \\ { \quad = \left( \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \right) . } \end{array} \right.
$$

On substituting (69)and (71) in (61) and omitting the parentheses around the partial derivatives,and on solving for the derivatives of the elements with respect to $\pmb { t }$ ,it is found that

$$
\begin{array} { r }  \{ \begin{array} { l l }  \frac { d \vec { u } _ { \perp } } { d t } - \frac { m _ { 3 } }  u ^ { \alpha } \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 \Theta } } { \sqrt { 1 - e ^ { 2 } \Theta \frac { \theta } { \sqrt { 1 \Theta } } { \sqrt { 1 - e ^ { 2 \Theta \frac { \theta } { \sqrt { 1 \Theta } } { \sqrt { 1 - e \Theta } } } } } } } } } } } } } } } } } } } } } } } \\ { \frac { d \vec { u } } { d t } - \frac { m _ { 3 } } } { u ^ { \alpha \alpha } \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \Theta \sqrt { 1 - e ^ { 2 } \Theta } } } } } } } } } } } } } } \\ { \frac { d \vec { u } } { d t } - \frac { m _ { 5 } \tan \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \Theta } } } } } } } } } } } { \alpha ^ { 2 } } + \frac { m _ { 5 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \sin \frac { \theta } { \sqrt { 1 - e ^ { 2 } \Theta } } } } } } } { \alpha ^ { 2 } } } \\  \frac { d \vec { u } } { d t } - \frac { 2 m _ { 3 } } { \alpha } \frac { \partial \vec { u } _ { \perp } } { \partial t } ,  \end{array} \end{array}
$$

These equations,\* together with the corresponding ones for the elements of the planet $m _ { 2 }$ ，constitute a rigorous system of differential equations for the determination of the motion of the planets $\mathbf { \Delta } m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ with respect to the sun when there are no other forces than the mutual attractions of the three bodies.

If $R _ { 1 , \ 2 }$ is expressed in terms of the time and the osculating elements at the epoch $t _ { 0 ; }$ ，equations (72） become the explicit expressions for the first half of the system (27),and define the perturbations of the elements which are of the first order with respect to the masses.

220. Introduction of Rectangular Components of the Disturbing Acceleration. Equations (72) require for their application that $R _ { 1 , \ 2 }$ shall be expressed first in terms of the elements,after which the partial derivatives must be formed. In some cases,especially in the orbits of comets,it is advantageous to have the rates of variation of the elements expressed in terms of three rectangular components of the disturbing acceleration.

The disturbing acceleration will be resolved into three rectangular components $W , \ S , \ R$ ，where $W$ is the component of acceleration perpendicular to the plane of the orbit with the positive direction toward the north pole; $\boldsymbol { s }$ is the component in the plane of the orbit which acts at right angles to the radius vector with the positive direction making an angle less than $9 0 ^ { \circ }$ with the direction of motion; $\boldsymbol { R }$ is the component acting along the radius vector with the positive direction away from the sun. The components used in the preceding chapter evidently might be employed here instead of these, but the resulting equations would be less simple.

In order to obtain the desired equations it is only necessary to express the partial derivatives of $R _ { 1 , \ 2 }$ with respect to the elements·in terms of $W , s ,$ and $\boldsymbol { R }$ ，and to substitute them in (61) or (72)，depending upon the set of elements used. The transformation will be made for the elements used in equations (61).

The quantities $m _ { 2 } \frac { \partial R _ { 1 , ~ 2 } } { \partial x }$ ， $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y }$ $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z }$ are the components of the disturbing acceleration parallel to the fixed axes of reference. It follows from the elementary properties of the resolution and composition of accelerations that $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x }$ is equal to the sum of the projections of $W , s ,$ and $\scriptstyle { R }$ upon the $\pmb { x }$ -axis,and similarly for the others.

Let $\boldsymbol { u }$ represent the argument of the latitude,or the distance from the ascending node to the planet $P$ ,Fig.61.Then it follows from the fundamental formulas of Trigonometry that

![](images/19383d61cdc983ec6979eb5200860b43357ce7fc920a3205c7f3bd3b26bcbcfd.jpg)  
Fig. 61.

$$
\left\{ \begin{array} { l l } { m _ { 2 } \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial x } = \mathrm { + } R ( \cos u \cos \theta \cdot \cos \theta - \sin u \sin \theta \cos \theta ) } \\ { \qquad - \mathrm { } S ( \sin u \cos \theta \cdot \sin \theta \sin \theta \cos \theta ) } \\ { \qquad + \mathrm { } W \sin \theta \sin i , } \\ { m _ { 2 } \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial y } = \mathrm { + } R ( \cos u \sin \theta \cdot \sin \theta \cos \theta \cos i ) } \\ { \qquad - \mathrm { } S ( \sin u \sin \theta - \cos u \cos \theta \cos \theta ) } \\ { \qquad - \mathrm { } W \cos \otimes \sin i , } \\ { m _ { 2 } \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial z } = \mathrm { + } R \sin u \sin i + \mathrm { } S \cos u \sin i + W \cos i . } \end{array} \right.
$$

Let s represent any of the elements $\Omega , \cdots , \sigma _ { \mathrm { . } }$ then

$$
\small \frac { \partial R _ { 1 , 2 } } { \partial s } = \frac { \partial R _ { 1 , 2 } } { \partial x } \frac { \partial x } { \partial s } + \frac { \partial R _ { 1 , 2 } } { \partial y } \frac { \partial y } { \partial s } + \frac { \partial R _ { 1 , 2 } } { \partial z } \frac { \partial z } { \partial s } .
$$

The derivatives $\frac { \partial R _ { 1 , ~ 2 } } { \partial x } , \frac { \partial R _ { 1 , ~ 2 } } { \partial y } , \frac { \partial R _ { 1 , ~ 2 } } { \partial z }$ are given in (73) and when ${ \frac { \partial x } { \partial s } } , { \frac { \partial y } { \partial s } }$ ， and $\frac { \partial z } { \partial s }$ have be found,thetransformationcabecom pleted at once.


<!-- chunk 0007: pages 421-454 -->
It follows from equations (51) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial x } { \partial K } = \xi \frac { \partial \alpha } { \partial K } + \eta \frac { \partial \alpha ^ { \prime } } { \partial K } , \quad } & { \displaystyle \frac { \partial x } { \partial P } = \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial P } , } \\ { \displaystyle \frac { \partial y } { \partial K } = \xi \frac { \partial \beta } { \partial K } + \eta \frac { \partial \beta ^ { \prime } } { \partial K } , \quad } & { \displaystyle \frac { \partial y } { \partial P } = \beta \frac { \partial \xi } { \partial P } + \beta ^ { \prime } \frac { \partial \eta } { \partial P } , } \\ { \displaystyle \frac { \partial z } { \partial K } = \xi \frac { \partial \gamma } { \partial K } + \eta \frac { \partial \gamma ^ { \prime } } { \partial K } , \quad } & { \displaystyle \frac { \partial z } { \partial P } = \gamma \frac { \partial \xi } { \partial P } + \gamma ^ { \prime } \frac { \partial \eta } { \partial P } , } \end{array} \right.
$$

where $\kappa$ is any of the elements $\delta \boldsymbol { \mathbf { \mathit { 3 } } } , i , \omega _ { \mathrm { : } }$ and $P$ any of the elements $a , e , \sigma$ .The quantities $\alpha , \cdots , \gamma ^ { \prime }$ are defined in (44),and their derivatives are given in (47), (48),and (49);the derivatives $\frac { \partial \xi } { \partial P }$ and $\frac { \partial \eta } { \partial P }$ are to be computed from (46).

It is found after some rather long but simple reductions that

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \Omega } = \delta r \cos \mathfrak { i } - W r \cos \mathfrak { u } \sin \mathfrak { i } , } \\ { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \dot { \mathfrak { t } } } = W r \sin \mathfrak { u } , } \\ { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { w } } = \delta r , } \\ { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { u } } = R _ { \mathfrak { t } } \frac { r } { \partial \mathfrak { t } } , } \\ { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { t } } = R _ { \mathfrak { t } } \frac { \partial R _ { 1 , 3 } } { \partial \mathfrak { t } } = \delta \left[ 1 + \frac { r } { p } \right] a \sin \mathfrak { v } , } \\ { \displaystyle \mathfrak { m } _ { \mathfrak { t } } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { t } } = \frac { R a \mathfrak { c } } { \sqrt { 1 - \mathfrak { c } ^ { 2 } } } \sin \mathfrak { v } + \delta \frac { \alpha ^ { 2 } } { \mathcal { T } } \frac { \mathfrak { s } } { \sqrt { 1 - \mathfrak { c } ^ { 2 } } } . } \end{array} \right. } \end{array}
$$

Therefore equations (61) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \Omega } { d t } = \frac { r \sin { u } } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin { i } } W , } \\ { \displaystyle \frac { d i } { d t } = \frac { r \cos { u } } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } W , } \\ { \displaystyle \frac { d \omega } { d t } = \frac { - \sqrt { 1 - e ^ { 2 } } \cos { v } } { n a e } R + \frac { \sqrt { 1 - e ^ { 2 } } } { n a e } \bigg [ 1 + \frac { r } { p } \bigg ] \sin { v } S } \\ { \quad \quad \quad } & { \quad \quad - \frac { r \sin { u } \ : \omega \ : i } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } W , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d a } { d t } = \frac { 2 e \sin v } { n \sqrt { 1 - e ^ { 2 } } } R + \frac { 2 a \sqrt { 1 - e ^ { 2 } } } { n r } S , } \\ { \displaystyle \frac { d e } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } \sin v } { n a } R + \frac { \sqrt { 1 - e ^ { 2 } } } { n a ^ { 2 } e } \Big [ \frac { a ^ { 2 } ( 1 - e ^ { 2 } ) } { r } - r \Big ] S , } \\ { \displaystyle \frac { d \sigma } { d t } = - \frac { 1 } { n a } \Big [ \frac { 2 r } { a } - \frac { 1 - e ^ { 2 } } { e } \cos v \Big ] R } \\ { \displaystyle \qquad - \frac { ( 1 - e ^ { 2 } ) } { n a e } \Big [ 1 + \frac { r } { p } \Big ] \sin v S . } \end{array} \right.
$$

# XXVI. PROBLEMS.

1.Find the components $s$ and $\scriptstyle { \pmb R }$ of this chapter in terms of $\pmb { T }$ and $N$ ， which were used in chapter Ix.,Art.174.

$$
\left\{ { \begin{array} { l } { S = { \frac { \left( 1 + e \cos v \right) } { \sqrt { 1 + e ^ { 2 } + 2 e \cos v } } } T + { \frac { e \sin v } { \sqrt { 1 + e ^ { 2 } + 2 e \cos v } } } N , } \\ { R = { \frac { e \sin v } { \sqrt { 1 + e ^ { 2 } + 2 e \cos v } } } T - { \frac { 1 + e \cos v } { \sqrt { 1 + e ^ { 2 } + 2 e \cos v } } } N . } \end{array} } \right.
$$

2.By means of the equations of problem 1 express the variations of the elements $\Omega , \cdots , \sigma$ in terms of $\pmb { T }$ and $N$ ,and verify all the results contained in the Table of Art.182.

3. Explain why $\frac { d \omega } { d t }$ contains a term depending upon $\pmb { W }$

4.Suppose the disturbed body moves in a resisting medium； find the equations for the variations of the elements.

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \frac { d G } { d t } = 0 , } \\ { \frac { d \vec { u } } { d t } = 0 , } \\ { \frac { d \vec { w } } { d t } = \frac { 2 \sqrt { 1 - e ^ { 2 } } } { n o t } \frac { \sin { \psi } } { \sqrt { 1 + e ^ { 2 } + 2 \vec { \epsilon } \cos { \psi } } } T , } \\ { \frac { d \vec { u } } { d t } = \frac { 2 \sqrt { 1 + e ^ { 2 } + 2 \vec { \epsilon } \cos { \psi } } } { n \sqrt { 1 - e ^ { 2 } } } T , } \\ { \frac { d \vec { u } } { d t } = \frac { 2 \sqrt { 1 - e ^ { 2 } } ( \cos { \psi } + \vec { \epsilon } ) } { n o t \sqrt { 1 + e ^ { 2 } + 2 \vec { \epsilon } \cos { \psi } } } T , } \\ { \frac { d \vec { w } } { d t } = - \frac { 2 ( 1 - e ^ { 2 } ) ( 1 + e ^ { \vec { w } } + \vec { \epsilon } \cos { \psi } ) } { n o t ( 1 + e ^ { \vec { w } } + \vec { \epsilon } \cos { \psi } ) \sqrt { 1 + e ^ { \vec { w } } + 2 \vec { \epsilon } \cos { \psi } } } T . } \end{array} \right. } \end{array}
$$

5.Discuss the way in which the elements vary in the last problem,including the values of $v$ for which the maxima and minima in their rates of change occur,when $\pmb { T }$ is a constant,and when it varies as the square of the velocity.

6. Derive the equations corresponding to (77) for the elements &,i, π, ${ \pmb \alpha } , \ldots$ and $\pmb { \epsilon }$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \Delta } { d t } = \frac { r \sin u } { n \alpha + 1 - e ^ { 2 } \sin i } W , } \\ { \displaystyle \frac { d \Delta } { d t } = \frac { r \cos u } { n \alpha + 1 - e ^ { 2 } \sin i } W , } \\ { \displaystyle \frac { d \mathbf { r } } { d t } = 2 \sin \frac { i } { 2 } \frac { d \Delta } { d t } + \frac { \sqrt { 1 - e ^ { 2 } } } { n \alpha + 2 } \left\{ - \ R \cos v + \delta \left( 1 + \frac { r } { p } \right) \sin v \right\} , } \\ { \displaystyle \frac { d \Delta } { d t } = \frac { 2 } { n \sqrt { 1 - e ^ { 2 } } } \left( R e \sin v + \delta \frac { p } { r } \right) , } \\ { \displaystyle \frac { d \Delta } { d t } - \frac { \sqrt { 1 - e ^ { 2 } } } { n \alpha } \left\{ R \sin v + \delta \left( \frac { e + \cos v } { 1 + e \cos v } + \cos v \right) \right\} , } \\ { \displaystyle \frac { d \epsilon } { d t } - \frac { 2 r R } { n \alpha ^ { 2 } } + \frac { e ^ { 3 } } { 1 + \sqrt { 1 - e ^ { 2 } } } \frac { d \pi } { d t } + 2 \sqrt { 1 - e } \sin \frac { i } { 2 } \frac { d \Delta } { d t } . } \end{array} \right.
$$

221.Development of the Perturbative Function. In order to apply equations (72) the perturbative function $\scriptstyle R _ { 1 , \ 2 }$ must be developed explicitly in terms of the elements and the time. From this point on only perturbations of the first order will be considered； therefore,in accordance with the results of Art.208, the elements which appear in $\scriptstyle R _ { 1 , \ 2 }$ are the osculating elements at the time $t _ { 0 }$

In the notation of Art. 205 the perturbative function is

$$
\left\{ \begin{array} { l l } { R _ { 1 , 2 } = k ^ { 2 } \left[ \displaystyle \frac { 1 } { r _ { 1 , 2 } } - \frac { x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 2 } + z _ { 1 } z _ { 2 } } { { r _ { 2 } } ^ { 3 } } \right] , } \\ { r _ { 1 , 2 } = \sqrt { ( x _ { 2 } - x _ { 1 } ) ^ { 2 } + ( y _ { 2 } - y _ { 1 } ) ^ { 2 } + ( z _ { 2 } - z _ { 1 } ) ^ { 2 } } , } \\ { \quad r _ { 2 } = \sqrt { x _ { 2 } { } ^ { 2 } + { y _ { 2 } } ^ { 2 } + { z _ { 2 } } ^ { 2 } } . } \end{array} \right.
$$

The perturbing forces evidently depend upon the mutual inclinations of the orbits,rather than upon their inclinations independently to the fixed plane of reference. It will be convenient, therefore,to develop $R _ { 1 , \ 2 }$ in terms of the mutual inclination. Since this angle is expressible in terms of $i _ { 1 } , i _ { 2 } , \ldots$ and $\begin{array} { r } { \partial \mathbf { 2 } ; } \end{array}$ the partial derivatives of $R _ { 1 , \ 2 }$ with respect to these elements will depend in part on their occurring implicitly in this angle.

The development of the perturbative function consists of three steps:\*

\* There are many more or less important variations of the method outlined here,which is based on the work of Leverrier in the Annales de l'Observatoire de Paris, vol 1.

$( a )$ Development of $R _ { 1 , \ 2 }$ as a power series in the square of the sine of half the mutual inclination of the orbits. $( b )$ Development of the coefficients of the series obtained in $( a )$ into power series in $\scriptstyle { e _ { 1 } }$ and $e _ { 2 }$ (c）Development of the coefficients of the preceding series into Fourier series in the mean longitudes of the two planets and the angular variables $\pi _ { 1 } , \pi _ { 2 } , \ \delta _ { 3 1 }$ and $\Omega _ { 2 }$

In the little space available here it will not be possible to give more than a general outline of the operations which are necessary to effect the complete development. A detailed discussion is given in Tisserand's Mécanique Celeste, vol. 1.， chapters X11. to XVIII. inclusive.

222. $( a )$ Development of $R _ { 1 , \mathrm { ~ 2 ~ } }$ in the Mutual Inclination. Let $\mathfrak { s }$ represent the angle between the radii $\boldsymbol { r } _ { 1 }$ and $\mathbf { \nabla } _ { r _ { 2 } }$ ； then

$$
\frac { 1 } { r _ { 1 , 2 } } = ( r _ { 1 } { } ^ { 2 } + { r _ { 2 } } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos { S } ) ^ { - \frac { 1 } { 2 } } .
$$

![](images/6a5148b0b4b1fd719a288a904cc71c82f66e36492d5f50d2c7cbe4b8d4da32ce.jpg)  
Fig. 62.

Let the angles between $r _ { 1 }$ and the $x , y ;$ and ${ \pmb z } \cdot$ -axes be $\alpha _ { 1 } , \beta _ { 1 }$ ， $\gamma _ { 1 }$ respectively,and in the case of $r _ { 2 } , \alpha _ { 2 } , \beta _ { 2 } ,$ and $\gamma _ { 2 }$ Then it follows that

$$
x _ { 1 } = r _ { 1 } \cos { \alpha _ { 1 } } , \qquad y _ { 1 } = r _ { 1 } \cos { \beta _ { 1 } } , \qquad z _ { 1 } = r _ { 1 } \cos { \gamma _ { 1 } } ,
$$

$$
\begin{array} { r } { x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 2 } + z _ { 1 } z _ { 2 } = r _ { 1 } r _ { 2 } ( \cos \alpha _ { 1 } \cos \alpha _ { 2 } + \cos \beta _ { 1 } \cos \beta _ { 2 } \qquad } \\ { + \cos \gamma _ { 1 } \cos \gamma _ { 2 } ) = r _ { 1 } r _ { 2 } \cos \beta . } \end{array}
$$

Let $\pmb { I }$ represent the angle between the two orbits,and $\tau _ { 1 }$ and $\pmb { \tau _ { 8 } }$

the distances from their ascending nodes to their point of intersection. From the spherical triangle $P _ { 1 } P _ { 2 } C$ the value of cos $\pmb { S }$ is found to be

$$
\left\{ \begin{array} { l l } { \cos ~ S = \cos \left( u _ { 1 } - \tau _ { 1 } \right) \cos \left( u _ { 2 } - \tau _ { 2 } \right) } \\ { \qquad \quad + \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \cos { I } , \quad \mathrm { o r } } \\ { \cos ~ S = \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) } \\ { \qquad \quad - 2 \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { I } { 2 } , } \\ { u _ { 1 } - \tau _ { 1 } = v _ { 1 } + \pi _ { 1 } - \triangle _ { 1 } - \tau _ { 1 } , } \\ { u _ { 2 } - \tau _ { 2 } = v _ { 2 } + \pi _ { 2 } - \triangle _ { 2 } - \tau _ { 2 } . } \end{array} \right.
$$

The quantities $I , \ \tau _ { 1 } ,$ and $\pmb { \tau _ { 2 } }$ are determined by the formulas of Gauss applied to the triangle $\Omega _ { 1 } \partial \Omega _ { 2 } C$ ：

$$
\begin{array} { r l } & { \left\{ \sin I \sin \tau _ { 1 } = \sin i _ { 2 } \sin \big ( \Omega _ { 1 } - \Omega _ { 2 } \big ) , \right. } \\ & { \left\{ \sin I \sin \tau _ { 2 } = \sin i _ { 1 } \sin \big ( \Omega _ { 1 } - \Omega _ { 2 } \big ) , \right. } \\ & { \left\{ \sin I \cos \tau _ { 1 } = \sin i _ { 1 } \cos i _ { 2 } - \cos i _ { 1 } \sin i _ { 2 } \cos \big ( \Omega _ { 1 } - \Omega _ { 2 } \big ) , \right. } \\ & { \left. \sin I \cos \tau _ { 2 } = - \cos i _ { 1 } \sin i _ { 2 } + \sin i _ { 1 } \cos i _ { 2 } \cos \big ( \Omega _ { 1 } - \Omega _ { 2 } \big ) , \right. } \\ & { \left. \cos I \ = \cos i _ { 1 } \cos i _ { 2 } + \sin i _ { 1 } \sin i _ { 2 } \cos \big ( \Omega _ { 1 } - \Omega _ { 2 } \big ) . \right. } \end{array}
$$

For simplicity $I , \tau _ { 1 } ,$ and $\pmb { \tau _ { 2 } }$ will be retained,but it must be remembered when the partial derivatives of $R _ { 1 , \ 2 }$ are taken that they are functions of $i _ { 1 } , i _ { 2 } , \ \delta \mathrm { a } _ { 1 } ,$ and $\displaystyle { \delta \boldsymbol { \mathbf { \sigma } } _ { 2 } }$

As a consequence of (79)，(81)，and (82)，the perturbative function can be written in the form

$$
\left\{ \begin{array} { l } { { R _ { 1 , 2 } = \left[ r _ { 1 } { } ^ { 2 } + r _ { 2 } { } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) \right] ^ { - \sharp } } } \\ { { \qquad \ } } \\ { { \qquad \times \left[ 1 + \displaystyle \frac { 4 r _ { 1 } r _ { 2 } \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { I } { 2 } } { r _ { \mathrm { i } } ^ { 2 } + r _ { 2 } { } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) } \right] ^ { - \sharp } } } \\ { { \qquad \ - \displaystyle \frac { r _ { 1 } } { r _ { 2 } { } ^ { 2 } } \left[ \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) \right. } } \\ { { \qquad \quad \qquad \left. - 2 \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { I } { 2 } \right] . } } \end{array} \right.
$$

The radii $\pmb { r _ { 1 } }$ and $\mathbf { \boldsymbol { r } _ { 2 } }$ are independent of $\boldsymbol { \mathit { I } }$ .The second factor of the first term of the right member of this equation can be expanded by the binomial theorem into an absolutely converging power series in $\sin ^ { 2 } { \frac { I } { 2 } }$ so lng as the numerical value of

$$
\frac { 4 r _ { 1 } r _ { 2 } \sin { ( u _ { 1 } - \tau _ { 1 } ) } \sin { ( u _ { 2 } - \tau _ { 2 } ) } \sin ^ { 2 } { \frac { I } { 2 } } } { \ldots ^ { 2 } + r _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos { ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) } }
$$

is less than unity. This fraction is less than,or at most equal to,

$$
{ \frac { 4 r _ { 1 } r _ { 2 } \sin ^ { 2 } { \frac { I } { 2 } } } { ( r _ { 2 } - r _ { 1 } ) ^ { 2 } } } .
$$

If this expression is less than unity for all the values which $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ can take in the given eilipses the expansion of (84) is valid for all values of the time. In the case of the major planets it is always very small, the greatest value of $\sin ^ { 2 } { \frac { I } { 2 } }$ being for Mercury and Mars,O.0118. In the perturbations of the planetoids by Jupiter it often fails,for $\pmb { I }$ is sometimes of considerable magnitude while $r _ { 2 } \mathrm { ~ - ~ } r _ { 1 }$ may become very small. In the case of Mars and Eros $r _ { 2 } \mathrm { ~ - ~ } r _ { 1 }$ may actually vanish and this mode of development consequently fails. It is needless to say that it is not generally applicable in the cometary orbits.

In those cases in which the expansion of (84) does not fail, the expression for $R _ { 1 , \ 2 }$ becomes

$$
\left\{ \begin{array} { c } { { R _ { 1 , 2 } = + [ r _ { 1 } { ^ 2 } + r _ { 2 } { ^ 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) ] ^ { \ast } } } \\ { { \mathrm { } \qquad - r _ { 1 } r _ { 2 } [ r _ { 1 } { ^ 2 } + r _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) ] ^ { \ast } } } \\ { { \mathrm { } \qquad \times 2 \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { I } { 2 } } } \\ { { \mathrm { } \qquad + r _ { 1 } { ^ { 2 } } r _ { 2 } ^ { 2 } [ r _ { 1 } { ^ 2 } + r _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) ] ^ { \ast } } } \\ { { \mathrm { } \qquad \times 6 \sin ^ { 2 } \left( u _ { 1 } - \tau _ { 1 } \right) \sin ^ { 2 } \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 4 } \frac { I } { 2 } } } \\ { { \mathrm { } \qquad + \mathrm { } \quad \cdot \mathrm { } \quad \cdot \mathrm { ~ \cdot } \quad \cdot \mathrm { ~ \cdot } \quad \cdot \mathrm { ~ \cdot } \quad \cdot \mathrm { ~ \cdot } \quad \mathrm { ~ \cdot } \quad \cdot \mathrm { ~ \cdot } \quad \mathrm { ~ \cdot } \quad \cdot \mathrm { ~ \cdot } \quad \mathrm { ~ \cdot } \quad } } \\ { { \mathrm { } \qquad - \frac { r _ { 1 } } { r _ { 2 } ^ { 2 } } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) } } \end{array} \right.
$$

$$
\begin{array} { l } { { \displaystyle - \frac { r _ { 1 } } { { r _ { 2 } } ^ { 2 } } \cos \left( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } \right) } } \\ { { \displaystyle + \frac { 2 r _ { 1 } } { { r _ { 2 } } ^ { 2 } } \sin \left( u _ { 1 } - \tau _ { 1 } \right) \sin \left( u _ { 2 } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { I } { 2 } . } } \end{array}
$$

223. $( b )$ Development of the Coefficients in powers of $\pmb { e _ { 1 } }$ and $\pmb { \ell _ { 2 } }$ The radii $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ vary from $a _ { 1 } ( 1 - e _ { 1 } )$ and $a _ { 2 } ( 1 - e _ { 2 } )$ to $a _ { 1 } ( 1 + e _ { 1 } )$ and $a _ { 2 } ( 1 + e _ { 2 } )$ respectively.Let

$$
\left\{ { r _ { 1 } = a _ { 1 } ( 1 + \rho _ { 1 } ) , } \right.
$$

The angles ${ \pmb u } _ { 1 }$ and $\pmb { u } _ { 2 }$ are expressed in terms of the true anomalies, ${ \pmb v } _ { 1 }$ and ${ \pmb v _ { 2 } } ,$ and the elements by (82). The true anomalies are equal to the mean anomalies plus the equations of the center，which may be denoted by ${ \boldsymbol { w } } _ { 1 }$ and ${ \boldsymbol { w } } _ { 2 }$ Let $l _ { 1 }$ and $l _ { 2 }$ represent the mean longitudes counted from the $\pmb { x }$ -axis [Fig. (62)}； then

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { u _ { 1 } - \tau _ { 1 } = l _ { 1 } - \Omega _ { 1 } - \tau _ { 1 } + w _ { 1 } , } \\ { u _ { 2 } - \tau _ { 2 } = l _ { 2 } - \Omega _ { 2 } - \tau _ { 2 } + w _ { 2 } . } \end{array} \right. } \end{array}
$$

It follows from (81) that $R _ { 1 , \ 2 }$ can be written in the form

$$
R _ { 1 , ~ 2 } = F [ a _ { 1 } ( 1 + \rho _ { 1 } ) , a _ { 2 } ( 1 + \rho _ { 2 } ) ] ,
$$

where $\pmb { F }$ is a homogeneous function of ${ \pmb a } _ { \bf 1 }$ and ${ \pmb a } _ { \mathbf { 2 } }$ of degree - 1. Therefore

$$
R _ { 1 , 2 } = \frac { 1 } { 1 + \rho _ { 2 } } F \left[ a _ { 1 } + a _ { 1 } \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } , a _ { 2 } \right] .
$$

The right member of this equation can be developed by Taylor's formula, giving

$$
\begin{array} { c } { { R _ { 1 , 2 } = \displaystyle \frac { 1 } { 1 + \rho _ { 2 } } \bigg \{ F ( a _ { 1 } , ~ a _ { 2 } ) + \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \frac { a _ { 1 } } { 1 } \frac { \partial F ( a _ { 1 } , ~ a _ { 2 } ) } { \partial a _ { 1 } } } } \\ { { + \left( \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \right) ^ { 2 } \frac { { a _ { 1 } } ^ { 2 } } { 1 \cdot 2 } \frac { \partial ^ { 2 } F ( a _ { 1 } , ~ a _ { 2 } ) } { { \partial a _ { 1 } } ^ { 2 } } + \cdots \bigg \} . } } \end{array}
$$

The expresions $\displaystyle { \left( \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \right) ^ { i } }$ can be developedaspowereries in $\pmb { \rho _ { 1 } }$ and $\pmb { \rho _ { 2 } }$ But in Art.100,equation (62), $\pmb { \rho }$ is given as a power series in e whose coefficients are cosines of multiples of the mean anomaly. On making these expansions and substitutions in (91), $R _ { 1 , \ 2 }$ can be arranged as a power series in $\pmb { e _ { 1 } }$ and $\pmb { \ell _ { 2 } }$ These operations are to be actually performed upon the separate terms of the series (87)，so the resulting series is arranged according to powers of $\pmb { e _ { 1 } } , \pmb { e _ { 2 } } ,$ and $\sin ^ { 2 } { \frac { I } { 2 } }$ · The angles ${ \boldsymbol { w } } _ { 1 }$ and ${ \boldsymbol { w } } _ { 2 }$ also depend upon $\pmb { e _ { 1 } }$ and $\pmb { e _ { 2 } }$ respectively,but their developments will not be introduced until after the next step.

224. $( c )$ Developments in Fourier Series. The first term within the bracket of (91) is obtained by replacing $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ by ${ a } _ { 1 }$ and ${ \pmb a } _ { 2 }$ respectively in (87). The higher terms involve the derivatives of the first with respect to ${ { a } _ { 1 } }$ ，On referring to the explicit series in (87),it is seen that the development of the expressions of the type

$$
( a _ { 1 } a _ { 2 } ) ^ { \frac { \nu - 1 } { 2 } } [ a _ { 1 } ^ { ~ 2 } + a _ { 2 } ^ { ~ 2 } - 2 a _ { 1 } a _ { 2 } \cos { ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) } ] ^ { - \frac { \nu } { 2 } } ,
$$

where $\pmb { \nu }$ is an odd integer,must be considered.

Let $u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } = \psi$ 、It is known from the theory of Fourier series when ${ \pmb a } _ { 1 }$ and ${ \pmb a } _ { 2 }$ are unequal,as is assumed, that $[ { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } - 2 { a _ { 1 } } { a _ { 2 } } \cos { \psi } ] ^ { - { \frac { \nu } { 2 } } }$ can be developed into a series of cosines of multiples of $\psi$ ,which is convergent for all values of $\psi$ That is,

$$
( a _ { 1 } a _ { 2 } ) ^ { \frac { \nu - 1 } { 2 } } [ a _ { 1 } ^ { \ : 2 } + a _ { 2 } ^ { \ : 2 } - 2 a _ { 1 } a _ { 2 } \cos \psi ] ^ { - \frac { \nu } { 2 } } = \frac { 1 } { 2 } \sum _ { i = - \infty } ^ { + \infty } B _ { \nu } ^ { ( i ) } \cos i \psi ,
$$

where $B _ { \nu } ^ { ( i ) } = B _ { \nu } ^ { ( - i ) }$

The coefficients $B _ { \nu } ^ { ( i ) }$ are of course given by Fourier's integral

$$
B _ { \nu } ^ { ( \mathfrak { i } ) } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \left( a _ { 1 } a _ { 2 } \right) ^ { \frac { \nu - 1 } { 2 } } [ a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } - 2 a _ { 1 } a _ { 2 } \cos \psi ] ^ { - \frac { \nu } { 2 } } \cos i \psi d \psi ,
$$

but the difficulty of finding the integral makes it advisable in this particular problem to proceed otherwise.

Let $z = \overline { { e ^ { \sqrt { - 1 } \psi } } }$ ，where $^ e$ represents the Napierian base. Then

$$
2 \cos \psi = z + z ^ { - 1 } , ~ 2 \cos i \psi = z ^ { i } + z ^ { - 4 } .
$$

Suppose $a _ { 2 } > a _ { 1 }$ and let $\frac { a _ { 1 } } { a _ { 2 } } = \alpha$ ； then (92) becomes

$$
\frac { \alpha ^ { \frac { \nu - 1 } { 2 } } } { a _ { 2 } } \left( 1 + \alpha ^ { 2 } - 2 \alpha \cos \psi \right) ^ { - \frac { \nu } { 2 } } = \frac { 1 } { 2 } \sum _ { i = - \infty } ^ { + \infty } B _ { \nu } ^ { \left( i \right) } \cos i \psi .
$$

Let

$( 1 + \alpha ^ { 2 } - 2 \alpha \cos \psi ) ^ { - \frac { \psi } { 2 } } = ( 1 - \alpha z ) ^ { - \frac { \psi } { 2 } } ( 1 - \alpha z ^ { - 1 } ) ^ { - \frac { \psi } { 2 } } = \frac { 1 } { 2 } \sum _ { i = - \infty } ^ { + \infty } b _ { \nu } { } ^ { ( i ) } z ^ { i } { } _ { \nu }$ therefore

$$
B _ { \nu } ^ { ( \mathfrak { i } ) } = \frac { \alpha ^ { \frac { \nu - 1 } { 2 } } } { a _ { 2 } } b _ { \nu } ^ { ( \mathfrak { i } ) } .
$$

Since the absolute values of $\pmb { \alpha } \pmb { \alpha }$ and $\pmb { \alpha } \pmb { z } ^ { - 1 }$ are less than unity for all real values of $\psi$ ，the factors $( 1 - \alpha z ) ^ { - \frac { \nu } { 2 } }$ and $( 1 - \alpha z ^ { - 1 } ) ^ { - \frac { \nu } { 2 } } \mathrm { c a n }$ be expanded by the binomial theorem into convergent power series in $\pmb { \alpha } \pmb { \mathrm { z } }$ and $\pmb { \alpha } \pmb { z } ^ { - 1 }$ The coefficient of $z ^ { i }$ in the product of these series is $\begin{array} { l } { { \frac { 1 } { 2 } } b _ { \nu } ^ { ( \bullet ) } } \end{array}$ ，after which $B _ { \nu } ^ { \scriptscriptstyle ( \mathfrak { d } ) }$ is obtained from (94).The general term of the product of the expansions is easily found to be

$$
\begin{array} { r } { \frac { 1 } { 2 } b _ { \nu } ^ { \quad ( i ) } = \frac { \displaystyle \frac { \frac { \nu } { 2 } \left( \frac { \nu } { 2 } + 1 \right) \cdot \cdot \cdot \left( \frac { \nu } { 2 } + i - 1 \right) } { i ! } \alpha ^ { i } \left[ 1 + \displaystyle \frac { \frac { \nu } { 2 } } { 1 } \cdot \frac { \frac { \nu } { 2 } + i } { i + 1 } \alpha ^ { 2 } \right. } { \left. + \displaystyle \frac { \frac { \nu } { 2 } \left( \frac { \nu } { 2 } + 1 \right) } { 1 \cdot 2 } \cdot \frac { \left( \frac { \nu } { 2 } + i \right) \left( \frac { \nu } { 2 } + i + 1 \right) } { ( i + 1 ) ( i + 2 ) } \alpha ^ { 4 } + \cdot \cdot \cdot \right] } . } \end{array}
$$

Inthismanerthecoefcientsof $\rho _ { 1 } \mathrm { } ^ { j _ { 1 } } \rho _ { 2 } \mathrm { } ^ { j _ { 2 } } \left( \mathrm { s i n } ^ { 2 } \frac { I } { 2 } \right) ^ { k }$ are developed in Fourier series in cos $\smash { i ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) }$ .But these functions are multiplied by the factors sin $( u _ { 1 } - \tau _ { 1 } )$ sin $( u _ { 2 } \ : - \tau _ { 2 } )$ raised to diferent powers [equation (87)]. These powers of sines are to be reduced to sines and cosines of multiples of tle arguments,and the products formed with cos $\dot { \iota } ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } )$ ， and the reduction again made to sines and cosines of multiples of arcs. The fnal trigonometrical terms will have the form cos $( j _ { 1 } u _ { 1 } + j _ { 2 } u _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } )$ , where $j _ { 1 } , j _ { 2 } , k _ { 1 } ,$ and $k _ { 2 }$ are integers. As a consequence of (89) this expression can be developed into

$$
\left\{ \begin{array} { l l } { \cos \left( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Omega _ { 1 } - j _ { 2 } \Omega _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } + j _ { 1 } w _ { 1 } + j _ { 2 } w _ { 2 } \right. } \\ { = \cos \left( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Omega _ { 1 } - j _ { 2 } \Omega _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } \right) } \\ { \qquad \times \left\{ \cos \left( j _ { 1 } w _ { 1 } \right) \cos \left( j _ { 2 } w _ { 2 } \right) - \sin \left( j _ { 1 } w _ { 1 } \right) \sin \left( j _ { 2 } w _ { 2 } \right) \right\} } \\ { \qquad - \sin \left( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Omega _ { 1 } - j _ { 2 } \Omega _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } \right) } \\ { \qquad \times \left\{ \sin \left( j _ { 1 } w _ { 1 } \right) \cos \left( j _ { 2 } w _ { 2 } \right) + \cos \left( j _ { 1 } w _ { 1 } \right) \sin \left( j _ { 2 } w _ { 2 } \right) \right\} . } \end{array} \right.
$$

Since

$$
\begin{array} { r } { \int l _ { 1 } = \Omega _ { 1 } + \omega _ { 1 } + n _ { 1 } ( t _ { 0 } - T _ { 1 } ) + n _ { 1 } ( t - t _ { 0 } ) = n _ { 1 } t + \epsilon _ { 1 } , } \\ { ~ \int _ { l _ { 2 } } = \Omega _ { 2 } + \omega _ { 2 } + n _ { 2 } ( t _ { 0 } - T _ { 2 } ) + n _ { 2 } ( t - t _ { 0 } ) = n _ { 2 } t + \epsilon _ { 2 } , } \end{array}
$$

the first factors of the terms in the right member of this equation are independent of $e _ { 1 }$ and $\mathbf { \epsilon } _ { e \mathbf { 2 } }$ Cos $( j _ { 1 } w _ { 1 } )$ ,etc.,are to be expanded into power series in $w _ { 1 }$ and $w _ { 2 }$ by the usual methods. Now $w _ { 1 } = v _ { 1 } - M _ { 1 ; }$ 、 $w _ { 2 } = v _ { 2 } - M _ { 2 } ,$ and these quantities were developed into power series in $e _ { 1 }$ and $e _ { 2 }$ [Art.100,eq.(64)] whose coeffcients were Fourier series with multiples of the mean anomaly as arguments.On substituting these series for $w _ { 1 }$ and $w _ { 2 }$ in the expansions of the second factors of the terms of the right member of (96),and reducing the powers of sines and cosines of the mean anomaly to sines and cosines of multiples of the mean anomaly,and multiplying by the factors

$$
( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - \jmath _ { 1 } \Omega _ { 1 } - j _ { 2 } \Omega _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } )
$$

and

$$
\sin { ( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Omega _ { 1 } - j _ { 2 } \Omega _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } ) } ,
$$

and again reducing to sines and cosines of multiples of the arguments,the expression (96) is developed as a power series in $\pmb { e _ { 1 } }$ and $\pmb { e _ { 2 } }$ whose coefficients are series in sines and cosines of sums of multiples of $l _ { 1 } , \ l _ { 2 } , \ \Omega _ { 3 1 } , \ \Omega _ { 3 2 } , \ \tau _ { 1 } , \ \tau _ { 2 } , \ M _ { 1 } , \ M _ { 2 } .$ But $M _ { 1 } = l _ { 1 } - \pi _ { 1 } ,$ $M _ { 2 } = l _ { 2 } - \pi _ { 2 }$ ；therefore the arguments will be $l _ { 1 } , l _ { 2 } , \Omega _ { 1 } , \Omega _ { 2 } ,$ ${ \tau _ { 1 } } , \ { \tau _ { 2 } } , \ { \pi _ { 1 } } , \ { \pi _ { 2 } }$ ，where $\tau _ { 1 }$ and $\tau _ { 2 }$ are functions of $\delta \mathrm { ~  ~ 1 ~ } , \delta \mathrm { ~  ~ 2 ~ } , i _ { 1 } ,$ and $i _ { 2 }$ defined by (83).

When the several expansions and reductions which have been described have all been made, $R _ { 1 , \ 2 }$ will be developed in a power series in $e _ { 1 } , ~ e _ { 2 } ,$ and $\sin ^ { 2 } { \frac { I } { 2 } }$ the coefficients of which are series of sines and cosines of multiples of $l _ { 1 } , l _ { 2 } , \ \Omega _ { 3 } { _ 1 } , \ \Omega _ { 2 } , \ \tau _ { 1 } , \ \tau _ { 2 } , \ \pi _ { 1 } , \ \pi _ { 2 } ,$ the coeffcient of each trigonometric term depending upon the ratio of the major semi-axes. If the signs of $\Omega _ { 1 } , \Omega _ { 2 } , \pi _ { 1 } , \pi _ { 2 } , \tau _ { 1 } , \tau _ { 2 } ,$ $\epsilon _ { 1 } , ~ \epsilon _ { 2 } ,$ and $t$ are changed the value of $R _ { 1 , \ 2 , \ }$ as defined in (84), obviously is unchanged； therefore the expansion in question contains only cosines of the argument. Hence

$$
\left\{ \begin{array} { l l } { { R _ { 1 , \ 2 } = \Sigma C \cos D , } } \\ { { \ } } \\ { { D = j _ { 1 } ( n _ { 1 } t + \epsilon _ { 1 } ) + j _ { 2 } ( n _ { 2 } t + \epsilon _ { 2 } ) - j _ { 1 } { ' } \Omega _ { 1 } - j _ { 2 } { ' } \Omega _ { 2 } } } \\ { { \ } } \\ { { \qquad + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } + k _ { 1 } { ' } \pi _ { 1 } + k _ { 2 } { ' } \pi _ { : } , } } \\ { { \ } } \\ { { C = f \left( a _ { 1 } , \ a _ { 2 } , \ e _ { 1 } , \ e _ { 2 } , \ \sin ^ { 2 } \frac { I } { 2 } \right) , } } \end{array} \right.
$$

in which ${ j _ { 1 } , \cdots , k _ { 2 } ^ { \prime } }$ take all integral values, positive, negative, and zero,the summation being extended over all of these terms.

It is clear from the foregoing that the series for $R _ { 1 , \ 2 }$ is very complicated and that much labor is required to expand it in any particular case. Leverrier has carried out the literal development of all terms up to the seventh order inclusive in ei, $\mathbf { \epsilon } _ { \mathbf { \mathcal { C } 2 } }$ $\sin ^ { 2 } { \frac { I } { 2 } }$ and the length of the work is such that fifty-three quarto pages of the first volume of the Annales de l'Observatoire de Paris are required in order to write out the result.

225.Periodic Variations. It follows from equations (72) and (97) that the rates of change of the elements of $\pmb { m _ { 1 } }$ are given by

$$
\begin{array} { r } { d ^ { ( 2 ) } { \boldsymbol { \mathrm { \texttt { - } } } } \ p _ { 0 , 0 } \boldsymbol { { \Psi } } \boldsymbol { 1 } - \ e _ { \theta } ^ { \lambda _ { 0 } } \boldsymbol { \mathrm { \texttt { - } } } [ \mathrm { i } \lambda _ { 0 } ^ { ( \lambda _ { \mathrm { { \texttt { e } } } } ) } e ^ { \lambda _ { 0 } } ] \boldsymbol { \epsilon } \sin \beta _ { \mathrm { { \texttt { p } } } } ] , } \\ { [ \frac { \delta _ { \mathrm { { i n } } } } { \delta t } \mathrm { \texttt { - } } \frac { \hbar \boldsymbol { \mathrm { \texttt { - } } } \boldsymbol { \mathrm { \texttt { 0 } } } _ { \mathrm { B } } } { \hbar \omega _ { 0 } ^ { \lambda _ { \mathrm { { \texttt { e } } } } } \hbar \omega _ { 0 } ^ { \lambda _ { \mathrm { { \texttt { e } } } } } } [ \mathrm { i } \frac { \partial _ { \mathrm { { i n } } } } { \partial t } \mathrm { \texttt { - } } \frac { \hbar \partial _ { \mathrm { { i n } } } } { \partial t } \mathrm { \texttt { - } } \lambda _ { 0 } \frac { \partial _ { \mathrm { { i n } } } } { \partial t } ] \boldsymbol { \epsilon } \sin \beta _ { \mathrm { { \texttt { p } } } } ] } \\ { \frac { \delta _ { \mathrm { { i n } } } } { \delta t } { \boldsymbol { \cdot } } \frac { \hbar \boldsymbol { \mathrm { \texttt { - } } } \boldsymbol { \mathrm { \texttt { 0 } } } _ { \mathrm { B } } } { \hbar \omega _ { 0 } ^ { \lambda _ { \mathrm { { \texttt { e } } } } } \hbar \omega _ { 0 } ^ { \lambda _ { \mathrm { { \texttt { e } } } } } } } \\  + \frac  \hbar \boldsymbol { \mathrm { \texttt { 0 } } } _ { \mathrm { { i n } } } \frac { \delta _ { \mathrm { { i n } } } } { \hbar \omega _ { 0 } ^ { \lambda _ { \mathrm { { \texttt { e } } } } } \hbar } \sum \{ \mathrm { i } \boldsymbol { \cdot } \boldsymbol { \mathrm { \texttt { + } } } \hbar \frac { \partial _ { \mathrm { { i n } } } } { \partial t } \mathrm { \texttt { - } } \boldsymbol { \mathrm { \texttt { 0 } } } _ { \mathrm { B } } \frac { \delta _ { \mathrm { { i n } } } } { \delta \omega _ { \mathrm { { \texttt { e } } } } \} } \\  \frac { \delta { \boldsymbol { \pi } } } { \delta t }  \end{array}
$$$$
\left\{ \begin{array} { l l } { \frac { d \alpha _ { 1 } } { d t } = \frac { m _ { 2 } \tan { \frac { i \alpha _ { 1 } } { 2 } } } { n _ { 1 } \alpha _ { 1 } ^ { 2 } \cdot \sqrt { 1 - \epsilon _ { 2 } } } \sum \left\{ \frac { \partial C } { \partial \tilde { \alpha } _ { 1 } } \cos { D } - \left[ k _ { 1 } \frac { \partial \tau _ { 3 1 } } { \partial \tilde { \alpha } _ { 1 } } + k _ { 2 } \frac { \partial \tau _ { 3 2 } } { \partial \tilde { \alpha } _ { 1 } } \right] \right. } \\ { \quad } \\ { \left. \times { C } \sin { D } \right\} + \frac { m _ { 3 } \sqrt { 1 - \epsilon _ { 1 } ^ { 2 } } } { n _ { 1 } \alpha _ { 1 } ^ { 2 } \epsilon _ { 1 } } \sum \frac { \partial C } { \partial \epsilon _ { 4 } } \cos { D } , } \\ { \frac { d \alpha _ { 1 } } { d t } - \frac { \displaystyle - 2 m _ { 2 } } { n _ { 1 } \alpha _ { 1 } } \sum _ { j _ { 1 } } c \sin { D } , } \\ { \frac { d \alpha _ { 1 } } { d t } = n _ { 3 } \sqrt { 1 - \epsilon _ { 1 } } \frac { \frac { 1 } { n _ { 1 } } - \frac { \epsilon _ { 1 } } { n _ { 1 } \alpha _ { 1 } ^ { 2 } \epsilon _ { 1 } } } { n _ { 1 } \alpha _ { 1 } ^ { 2 } \epsilon _ { 1 } } \sum _ { j , l } c \sin { D } } \\ { \quad } & { \quad + \frac { m _ { 2 } \sqrt { 1 - \epsilon _ { 2 } } } { n _ { 1 } \alpha _ { 1 } ^ { 2 } \epsilon _ { 1 } } \sum \left\{ k _ { 1 } ^ { \prime } + k _ { 1 } \frac { \partial \tau _ { 1 } } { \partial \tau _ { 1 } } + k _ { 2 } \frac { \partial \tau _ { 2 } } { \partial \tau _ { 1 } } \right\} { C } \sin { D } , } \\ { \quad \left. \frac { d \alpha _ { 1 } } { d t } \tan { \frac { i \alpha _ { 1 } } { 2 } } \right\} . } \end{array} \right.
$$

$$
\begin{array} { r } { \left. \begin{array} { c } { \frac { d \epsilon _ { 1 } } { d t } = \frac { m _ { 2 } \tan \frac { i _ { 1 } } { 2 } } { { n _ { 1 } a _ { 1 } } ^ { 2 } \sqrt { 1 - e _ { 1 } } ^ { 2 } } \sum \left\{ \frac { \partial C } { \partial i _ { 1 } } \cos D - \left[ k _ { 1 } \frac { \partial \tau _ { 1 } } { \partial \dot { i } _ { 1 } } + k _ { 2 } \frac { \partial \tau _ { 2 } } { \partial \dot { i } _ { 1 } } \right] \right. } \\ { \left. \times C \sin D \right\} + m _ { 2 } \sqrt { 1 - e _ { 1 } } ^ { 2 } \frac { 1 - \sqrt { 1 - e _ { 1 } } ^ { 2 } } { { n _ { 1 } a _ { 1 } } ^ { 2 } e _ { 1 } } \sum \frac { \partial C } { \partial e _ { 1 } } \cos D } \\ { \left. - \frac { 2 m _ { 2 } } { n _ { 1 } a _ { 1 } } \sum \frac { \partial C } { \partial a _ { 1 } } \cos D . \right. } \end{array} \right. } \end{array}
$$

The perturbations of the elements of the orbit of $\pmb { m _ { 1 } }$ of the first order with respect to the mass $\scriptstyle { m _ { 2 } }$ are the integrals of these equations regarding the elements as constants in the right members. Similar terms must be added for each disturbing planet.

There are terms in $R _ { 1 , \ 2 }$ of three classes: $( a )$ those in which $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ is distinct from zero and not small; $( b )$ those in which $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ is very small, but distinct from zero;and $( c )$ those in which $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ equals zero. Denote the fact that $\scriptstyle R _ { 1 , \ 2 }$ contains these three sorts of terms by writing

$$
R _ { 1 , 2 } = \Sigma C _ { 0 } \cos D _ { 0 } + \Sigma C _ { 1 } \cos D _ { 1 } + \Sigma C _ { 2 } \cos D _ { 2 } ,
$$

where the three sums in the right member include these three classes of terms respectively. Hence the perturbations of the elements of $\mathbf { m _ { 1 } }$ by $\mathbf { \Delta } m _ { 2 }$ of the first order and of the first class are

$$
\begin{array} { r }  [ \begin{array} { c c c } { ( \triangle \otimes \alpha ^ { ( 1 ) } - \langle \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha ) } \\ { \times \sum \{ \frac { \partial K ( \alpha ) } { \partial \alpha } , \frac { \sin \alpha } { \partial \sin } \alpha \} \alpha + [ k _ { 1 } \frac { \partial \sin \alpha } { \partial \alpha } + k _ { 2 } \frac { \partial \sin \alpha } { \partial \alpha } ] \frac { C _ { 1 } } { 2 \sin \alpha } \sin \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha } \\ { \langle \otimes \alpha ^ { ( 1 ) } - ( \delta ) ^ { \alpha } \rangle \otimes \alpha = \frac { \sin \alpha \otimes \alpha \otimes \alpha \otimes \alpha } { \alpha \otimes \alpha \otimes \alpha \otimes \alpha } \frac { \sin \alpha } { \alpha } \alpha - \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha } \\  \times \sum \{ \frac { \partial K ( \alpha ^ { ( 1 ) } - k _ { 2 } \sin \alpha ^ { ( 2 ) } - k _ { 2 } \sin \alpha ^ { ( 2 ) } - k _ { 2 } \sin \alpha ^ { ( 2 ) } \alpha + \frac { \partial \sin \alpha \otimes \alpha } { \partial \alpha \otimes \alpha } \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha  } \\  - \frac { \operatorname* { m a x } \alpha \otimes \alpha \otimes \alpha } { \alpha \otimes \alpha ^ { ( 1 ) } - \alpha \otimes \alpha \otimes \alpha ^ { ( 1 ) } - \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha \otimes \alpha  } \\   \langle \otimes \alpha ^ { ( 1 ) } - ( \varsigma ) ^ { \alpha } \rangle \otimes \alpha - \frac { \sin \alpha \otimes \alpha } { \alpha \otimes \alpha ^ { ( 1 ) } - \alpha \otimes \alpha ^ { ( 1 ) } } \sum \{ \alpha \otimes \alpha \otimes \alpha \otimes \end{array} \end{array}
$$$$
\begin{array} { r }  \rho _ { \mathrm { e f f } } ( \mathbf { r } ) = [ \begin{array} { c } { \rho _ { \mathrm { e f f } } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) - \omega _ { i } ^ { \mathrm { e f f } } \Omega \cdot \mathbf { i } } \\ { \mathbf { R } \cdot \mathbf { b } _ { i } ^ { \mathrm { e f f } } \Omega \cdot \mathbf { k } _ { i } - \omega _ { i } ^ { \mathrm { e f f } } \Omega \cdot \mathbf { k } _ { i } \omega _ { i } ^ { \mathrm { e f f } } \mathcal { I } _ { i , j , k } + \mathcal { I } _ { 0 0 } \mathbf { r } \mathcal { R } } \\  - \frac { \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ^ { \mathrm { e f f } } \Omega }  \gamma _ { 0 0 } \omega _ { i } ^ { \mathrm { e f f } } +  \mathbf { r }  \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \mathbf { r } _ { i } ( \mathbf { r } ) \cdot \mathbf { r } _ { j } ( \mathbf { r } ) \cdot \ \end{array} \end{array}
$$

$$
\begin{array} { r }  \{ \begin{array} { l l } { \qquad + \mathrm { e } _ { \perp \perp \perp } ^ { \mathrm { o u t } } \leq \mathrm { e } _ { \perp \perp \perp } ^ { \mathrm { o u t } } \geq \frac { \mathrm { i } \omega _ { \mathrm { ~ c } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } \leq \mathrm { i } \frac { \omega _ { \mathrm { c } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } , \qquad \mathrm { e } _ { \perp \mathrm { o } } ^ { \mathrm { i } \mathrm { ~ o u t } } > \mathrm { i } \frac { \omega _ { \mathrm { c } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } , } \\ { \qquad \quad + ( \alpha _ { \mathrm { { i } } } ^ { \mathrm { o u t } } ) ^ { \mathrm { s _ { i } } - \mathrm { o u t } } > \mathrm { i } \frac { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } \geq \mathrm { i } \frac { \omega _ { \mathrm { c } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } \leq \mathrm { i } \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } , } \\ { \qquad \quad - ( \alpha _ { \mathrm { { i } } } ^ { \mathrm { o u t } } ) - ( \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } - \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } ) - \mathrm { i } \frac { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } - \mathrm { i } \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } \geq \mathrm { i } \frac { C _ { \mathrm { c o v } } \mathrm { o u t } _ { \mathrm { o u t } } } { \omega _ { \mathrm { i } } ^ { \mathrm { o u t } } } } \\  \qquad \quad - \frac { m _ { \mathrm { d i } } ^ { \mathrm { o u t } } - m _ { \mathrm { d i } } ^ { \mathrm { o u t } } } { \omega _ { \mathrm { { i } } } ^ { \mathrm { o u t } } } \geq \{ \mathbf { \bar { \mathbf { \Phi } } } ^ { \dag } + \mathbf { \bar { \mathbf { \Phi } } } _ { \mathrm { { i } } } \frac  \mathbf { \bar { \mathbf { \Phi } } } _ { \mathrm { d i } } \end{array} \end{array}
$$

These terms are purely periodic with periods jn+jn， and constitute the periodic variations. Every element is subject to them,depending upon an infinity of such terms whose periods are different. The larger $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ is,the shorter is the period of the term and in general the smaller is its coefficient.

The method of representing the motion of the planets by a series of periodic terms is somewhat analogous to the epicyeloid theory of Ptolemy,for each term alone is equivalent to the adding of a small circular motion to that previously existing. This theory is more complex than that of Ptolemy in that it adds epicycloid upon epicycloid without limit; it is simpler than that of Ptolemy in that it flows from one simple principle,the law of gravitation.

226.Long Period Variations. The letters $j _ { 1 }$ and $j _ { 2 }$ represent all positive and negative integers and zero. Therefore，unless $\pmb { n _ { 1 } }$ and $\pmb { n _ { 2 } }$ are incommensurable $j _ { 1 }$ and $j _ { 2 }$ exist such that $j _ { 1 } n _ { 1 } +$ $j _ { 2 } n _ { 2 } = 0$ ,where $j _ { 1 }$ and $j _ { 2 }$ are not zero．But then $D$ is a constant and the integral is not formed this way. However,whether $\pmb { n } _ { 1 }$ and $\pmb { n _ { 2 } }$ areincommensurable or not,such a pair of numbers can be found that $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ is very small. The corresponding term will be large unless its $c$ is very small. It is shown in a complete discussion of the development of $\scriptstyle R _ { 1 , \ 2 }$ that the order of $c$ in $e _ { 1 } , \ e _ { 2 } ,$ $\sin ^ { 2 } { \frac { I } { 2 } }$ is at the least equal to the numerical value of $j _ { 1 } + j _ { 2 }$ (see Tisserand's Méc. Cel., vol. 1., p. 308). Since $\pmb { n _ { 1 } }$ and $\pmb { n _ { 2 } }$ are both positive,one of the numbers $j _ { 1 } , j _ { 2 }$ must be positive and the other negative in order that the sum $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ shall be small. The more nearly equal $j _ { 1 }$ and $j _ { 2 }$ are numerically the smaller the numerical value of $j _ { 1 } + j _ { 2 }$ is,and consequently，the larger $\boldsymbol { c }$ will be. When the mean motions of the two planets are such that they are nearly commensurable with the ratio of $\pmb { n _ { 1 } }$ to $\pmb { n _ { 2 } }$ expressible in small integers,then large terms in the perturbations will arise from the presence of these small divisors. The period of such a term is $\frac { 2 \pi } { j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } }$ which is very great，whence the appellation long period. These terms are given by equations of the same form as (99),but with the restriction that $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 }$ shall be very small.

Geometrically considered,the condition that the periods shall be nearly commensurable with the ratio expressible in small integers means that the points of conjunction occur at nearly the same part of the orbits with only a few other conjunctions intervening. The extreme case is that in which there are no conjunctions intervening,i.e., when $j _ { 1 }$ and $j _ { 2 }$ differ in numerical value by unity.

The mean motions of Jupiter and Saturn are nearly in the ratio of five to two. Consequently $j _ { 1 } = 2$ $j _ { 2 } = - 5$ gives a long period term，and the order of the coefficient $\pmb { C }$ is the absolute value of ${ \bf 2 } - { \bf 5 }$ ，or 3.The cause of the long period inequality of Jupiter and Saturn was discovered by Laplace in 1784 in computing the perturbations of the third order in ${ \pmb e } _ { 1 }$ and $\pmb { e _ { 2 } }$ The ‘ength of the period in the case of these two planets is about 850 years.

227. Secular Variations. The expression $\pmb { D }$ is independent of the time for all of those terms in which $\ j _ { 1 } = j _ { 2 } = 0$ The partial derivatives of $\pmb { D }$ with respect to the elements are also independent of the time; hence,on taking these terms of (98) and integrating,it is found that

$$
\{ \begin{array} { c } { { [ \Delta _ { 1 } ^ { \mathrm { s } , \mathrm { s } , \mathrm { a } } ] = \displaystyle \frac { m _ { \mathrm { s } } } { n _ { 0 } \alpha _ { 1 } ^ { \mathrm { s } + 1 } - e ^ { \mathrm { i } \omega } \mathrm { i } n _ { \mathrm { i } } } \mathrm { i } _ { \mathrm { a } } \sum _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } \in \mathcal { S } _ { \mathrm { B } } } D _ { \bullet } } } \\ { { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { \mathrm { \normalfont ~ i } _ { \widetilde { \sigma } ^ { \mathrm { s } , \mathrm { s } } } ^ { \mathrm { a } } - \displaystyle \frac { - m _ { \mathrm { s } } } { n _ { 0 } \alpha _ { 1 } ^ { \mathrm { s } } + 1 } \mathrm { i } _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } \in \mathcal { S } _ { \mathrm { B } } } \mathrm { i } _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } } \Big ] C _ { \mathrm { s } } \mathrm { s i n } D _ { \bullet } \Bigg \} ( \mathrm { i } _ { - } l _ { 0 } ) , } } \\ { { \mathrm { \normalfont ~ i } _ { \widetilde { \sigma } ^ { \mathrm { s } , \mathrm { s } } } ^ { \mathrm { a } } - \displaystyle \frac { - m _ { \mathrm { s } } } { n _ { 0 } \alpha _ { 1 } ^ { \mathrm { s } } + 1 } \mathrm { i } _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } \in \mathcal { S } _ { \mathrm { B } } } \mathrm { i } _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } } \Bigg \} \Big \{ j _ { \mathrm { s } } ^ { \mathrm { s } } - k _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } } \mathrm { i } _ { \widetilde { \sigma } _ { 1 } ^ { \mathrm { s } } } } } \\  { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  { \qquad \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\   \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array}{c} \{ \begin{array} { c } { \displaystyle { \begin{array} { c } { \frac { m _ { 2 } \tan \frac { i _ { 1 } } { 2 } } { n _ { 1 } a _ { 1 } ^ { 2 } \sqrt { 1 - \epsilon _ { 1 } } } \sum \{ k _ { i ^ { \prime } } + k _ { 1 } \frac { \partial \tau _ { 1 } } { \partial \tau _ { 1 } }  } \\ {  + k _ { 2 } \frac { \partial \tau _ { 2 } } { \partial \tau _ { 1 } } \} C _ { 2 } \sin D _ { 2 } \cdot ( \ell - \ell _ { 0 } ) , } \end{array} } } \\ { \displaystyle { \begin{array} { c } { \frac { m _ { 2 } \tan \frac { i _ { 1 } } { 2 } } { \pi _ { 1 } a _ { 1 } ^ { 2 } \sqrt { 1 - \epsilon _ { 1 } } } \sum \{ \frac { \partial C _ { 2 } } { \partial \tilde { \tau } _ { 1 } } \cos D _ { 2 }  } \\ {  \frac { \partial C _ { 2 } } { \partial \tilde { \tau } _ { 1 } } \cos D _ { 1 }  } \end{array} } } \\ { \displaystyle { [ \pi _ { 1 } ^ { ( \theta , 1 ) } = \frac {  \overline { { n } } _ { 2 } \tan \frac { i _ { 1 } } { 2 } } { \pi _ { 1 } a _ { 1 } ^ { 2 } \sqrt { 1 - \epsilon _ { 1 } } } \sum \{ \frac { \partial C _ { 2 } } { \partial \tilde { \tau } _ { 1 } } \cos D _ { 2 }  } \\ { -  [ h _ { 1 } \frac { \partial \tau _ { 1 } } { \partial \tilde { \tau } _ { 1 } } + k _ { 2 } \frac { \partial \tau _ { 2 } } { \partial \tilde { \tau } _ { 2 } } ] C _ { 2 } \sin D _ { 2 } \} ( \ell - \ell _ { 0 } ) } } \\ { \displaystyle { + \frac { m _ { 2 } \sqrt { 1 - \epsilon _ { 1 } } - \overline { { n } } _ { 2 } ^ { 2 } } { \pi _ { 1 } a _ { 1 } \epsilon _ { 1 } ^ { 2 } \epsilon _ { 1 } } \sum \frac { \partial C _ { 2 } } { \partial \epsilon _ { 1 } } \cos D _ { 2 } \cdot ( \ell - \ell _ { 0 } ) , } } \end{array}   \end{array} 
$$

$$
\{ \begin{array} { l l } { [ a _ { 0 } , a _ { 1 } ^ { \prime \prime \prime } ] = 0 , } \\ { [ a _ { 0 } , a _ { 1 } ^ { \prime \prime \prime } ] = \frac { m _ { 0 } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } { \pi a _ { 0 } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } \sum \{ k _ { 1 } ^ { \prime } + k _ { 0 } \frac { \partial \Omega } { \partial \Omega _ { 1 } }  } \\ { \qquad + k _ { 0 } \frac { \partial \Omega } { \partial \pi _ { 0 } } \} C \sin { D _ { 1 } } \cdot ( \ell - \ell _ { 0 } ) , } \\ { [ c _ { 0 } , a _ { 1 } ^ { \prime \prime \prime } ] = \frac { m _ { 0 } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } { \pi a _ { 0 } a _ { 1 } ^ { \prime } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } \sum \{ \begin{array} { l l } { \tilde { a } _ { 0 } ^ { \prime \prime } \cos { D _ { 1 } } } \\ { \tilde { a } _ { 1 } ^ { \prime \prime } \cos { D _ { 2 } } } \end{array}  } \\ { [ \begin{array} { l l } { \tilde { a } _ { 0 } ^ { \prime \prime \prime } } & { \cos { D _ { 1 } } } \\ { \sin { \frac { \theta _ { 0 } } { \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } } + k _ { 0 } \frac { \partial \Omega } { \partial \theta _ { 1 } ^ { \prime } } } \end{array} ] C _ { \mathrm { S i a n } } D _ { \mathrm { S i } } \} ( \ell - \ell _ { 0 } ) } \\ { \qquad + m _ { 0 } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } \frac { 1 - \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } { \pi a _ { 0 } \sqrt { 1 - \epsilon _ { 0 } ^ { \prime } } } } \\ { \qquad \sum \tilde { a } _ { 0 } ^ { \prime } \cos { D _ { 2 } } \cdot ( \ell - \ell _ { 0 } ) } \\ { \qquad - \frac { 2 m _ { 0 } } { \pi a _ { 0 } } \sum \tilde { a } _ { 0 } ^ { \prime \prime } \cos { D _ { 2 } } \cdot ( \ell - \ell ) } \end{array} 
$$

It follows that there are no secular terms of this type of the first order with respect to the masses in the perturbations of $^ { a }$ This constitutes the first theorem on the stability of the solar system. It was proved up to the second powers of the eccentricities by Laplace in $^ { 1 7 7 3 , \ast }$ when he was but twenty-four years of age,in a memoir upon the mutual perturbations of Jupiter and Saturn; it was shown by Lagrange in 1776 that it is true for all powers of the eccentricities. $^ \dagger$ It was proved by Poisson in 1809 that there are no secular terms in $^ { a }$ in the perturbations of the second order with respect to the masses,but that there are terms of the type $\pmb { t }$ cos $\pmb { D }$ ，where $D$ contains the time.t Terms of this type are commonly called Poisson terms.

All of the elements except $^ { \pmb { a } }$ have secular terms. It appears to have been supposed that the secular terms,which apparently cause the elements to change without limit,alone prevent the use of equations (72) for computing the perturbations for any time however great. Many methods of computing perturbations have been devised in order to avoid the appearance of secular terms; yet it is clear that,whether or not terms proportional to the time appear, the method is strictly valid for only those values of the time for which the series (20) of Art. 207 are convergent.

Secular terms may enter in another way,usually not considered. If $j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } = 0$ with $j _ { 1 } \neq 0 , j _ { 2 } \neq 0 , D$ is independent of the time and the corresponding terms are secular. In this case $D$ is not independent of $\epsilon _ { 1 }$ and there will be secular terms in the perturbations of $^ { a }$ .As has been remarked, this condition will always be fulfilled by an infinity of values of $j _ { 1 }$ and $j _ { 2 }$ if $\pmb { n _ { 1 } }$ and $\boldsymbol { n } _ { 2 }$ are not incommensurable. But it is impossible to determine from observations whether or not $\boldsymbol { n } _ { 1 }$ and $\boldsymbol { n } _ { 2 }$ are incommensurable, for there is always a limit to the accuracy with which observations can be made，and within this limit there exist infinitely many commensurable and incommensurable numbers. There is as much reason,therefore,to say that secular terms in $^ { a }$ of this type exist as that they do not. However，they are of no practical importance because the ratio of $\pmb { n } _ { 1 }$ to $\pmb { n _ { 2 } }$ cannot be expressed in small integers,and the coefficients of these terms,if they do exist,are so small that they are not sensible for such values of the time as are ordinarily used.

228. Terms of the Second Order with Respect to the Masses. The terms of the second order are defined by equations (29), Art.210. The right members of these equations are the products of the partial derivatives,with respect to the elements,of the right members which occur in the terms of the first order，and the perturbations of the first order of the corresponding elements. Thus,the second order perturbations of the node are determined by the equations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \Omega _ { 1 } ( 0 , \mathfrak { z } ) } { d t } = \frac { m _ { 2 } } { { n _ { 1 } } { a _ { 1 } } ^ { 2 } \sqrt { 1 - { e _ { 1 } } ^ { 2 } } \sin i _ { 1 } } \sum _ { i _ { 1 } } \frac { \partial ^ { 2 } R _ { 1 , 2 } } { \partial i _ { 1 } \partial s _ { 1 } } s _ { 1 } ^ { _ { 1 } ( 0 , 1 ) } , } \\ { \displaystyle \frac { d \Omega _ { 1 } ( 1 , 1 ) } { d t } = \frac { m _ { 2 } } { { n _ { 1 } } { a _ { 1 } } ^ { 2 } \sqrt { 1 - { e _ { 1 } } ^ { 2 } } \sin i _ { 1 } } \sum _ { s _ { 2 } } \frac { \partial ^ { 2 } R _ { 1 , 2 } } { \partial i _ { 1 } \partial s _ { 2 } } s _ { 2 } ^ { _ { 2 } ( 1 , 0 ) } , } \end{array} \right.
$$

where ${ \pmb s } _ { 1 }$ and ${ \pmb S } _ { 2 }$ represent the elements of the orbits of $m _ { 1 }$ and ${ \bf \mathscr { m } _ { 2 } }$ respectively. The partial derivative $\frac { \partial ^ { 2 } R _ { 1 , ~ 2 } } { \partial i _ { 1 } \partial s _ { 1 } }$ is a sum of periodic and constant terms; ${ \ s _ { 1 } } ^ { ( 0 , 1 ) }$ and $\mathbf { \delta } _ { \mathbf { \delta } ^ { 8 } \mathbf { 2 } } ^ { ( 1 , 0 ) }$ are sums of periodic terms and terms containing the time to the first degree as a factor. The products $\frac { \partial ^ { 2 } R _ { 1 , \ 2 } } { \partial i _ { 1 } \partial s _ { 1 } } \ s _ { 1 } ( 0 , 1 )$ and $\frac { \partial ^ { 2 } R _ { 1 , \ 2 } } { \partial i _ { 1 } \partial s _ { 2 } } \ s _ { 2 } ( { \bf 1 } , 0 )$ therefore contain terms of four types: $( a ) \mathsf { \Pi } _ { \mathsf { c o s } } ^ { \mathsf { s i n } } D$ where $D$ contains the time; $( b ) \ t _ { \mathrm { \ell { c o s } } } ^ { \mathrm { s i n } } D ;$ $( c ) \begin{array} { l } { \sin } \\ { \cos } \end{array} D _ { 2 } ,$ where $D _ { 2 }$ is independent of the time; and $( d ) \ t _ { \cos } ^ { \sin } \ D _ { \mathbf { \varepsilon } } .$ The integrals of these four types are respectively:

$$
\begin{array} { l c c } { { { } } } & { { - \displaystyle \cos D } } & { { { } \mathrm { - \cos { } } D } } \\ { { { } } } & { { { \displaystyle \frac { \sin D } { j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } } } ; \qquad ( b ) } } & { { t \displaystyle \frac { \sin D } { j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } } + \displaystyle \frac { \cos D } { ( j _ { 1 } n _ { 1 } + j _ { 2 } n _ { 2 } ) ^ { 2 } } ; } } \\ { { { } } } & { { { } } } & { { t \displaystyle \frac { \sin } { 2 } D _ { 2 } ; } } \end{array}
$$

Therefore,the perturbations of the second order with respect to the masses have purely periodic terms；Poisson terms,or terms in which the trigonometric terms are multiplied by the time; secular terms where the time occurs to the first degree;and secular terms where the time occurs to the second degree. This is true for all of the elements except the major semi-axis,in the case of which the coefficients of the terms of the third and fourth types are zero,as Poisson first proved.

In the terms of the third order with respect to the masses there are secular terms in the perturbations of all the elements except $\mathbf { a _ { 1 } } _ { \mathrm { : } }$ ,which are proportional to the third power of the time,and so on.

229.Lagrange's Treatment of the Secular Variations. The presence of the secular terms in the expressions for the elements seems to indicate that,if it is assumed that the series represent the elements for all values of the time,then the elements change without limit with the time. But this conclusion is by no means necessarily true. For example,consider the function

$$
\sin { ( c m t ) } = c m t - { \frac { c ^ { 3 } m ^ { 3 } t ^ { 3 } } { 3 ! } } + \cdots ,
$$

where $\pmb { c }$ is a constant and m a very small factor which may take the place of a mass. The series in the right member converges for all values of $\scriptstyle { \mathbf { \alpha } } _ { t }$ This function is never greater than unity for any value of the time;yet if its expansion in powers of m were given, and if the first few terms were considered without the law of the coefficients being known,it might seem that the series represents a function which increases indefinitely in numerical value with the time.

On following out the idea that the secular terms may be expansions of functions which are always finite,Lagrange has shown (see Collected Works,vols.v.and vI.),under certain assumptions which have not been logically justified, that the secular terms are in reality the expansions of periodic terms of very long period. These terms differ from the long period variations (Art.226） in that they come from the small uncompensated parts of the periodic variations，instead of directly from special conditions of conjunctions. As a rule these terms are very small,and their periods are much longer than those of the sensible long period terms. It will not be possible to give here more than a very general idea of the method of Lagrange.

The first step in the method of Lagrange is a transformation of variables by the equations

and

$$
\begin{array} { c } { { \displaystyle { \int } h _ { i } = e _ { i } \sin \pi _ { j } , } } \\ { { \displaystyle { \bigcup _ { l _ { i } } } = e _ { i } \cos \pi _ { j } , } } \\ { { \displaystyle { \int } p _ { i } = \tan i _ { i } \sin \bigotimes _ { i } , } } \\ { { \displaystyle { \bigcup _ { q _ { i } } } = \tan i _ { i } \cos \bigotimes _ { i } } , } \end{array}
$$

where $e _ { j } , \pi _ { j } ,$ etc.,are the elements of the orbit of $m _ { i } ,$ and $l _ { j }$ is a new variable not to be confused with the mean longitude. These transformations are to be made simultaneously in the elements of the orbits of all of the planets. The elements ${ \pmb a } _ { i }$ and $\epsilon _ { j }$ remain without transformation. On omitting the subscripts,it is found from (103)and (104) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d h } { d t } = + e \cos \pi \frac { d x } { d t } + \sin \pi \frac { d e } { d t } , } \\ { \displaystyle \frac { d \vec { l } } { d t } = - e \sin \pi \frac { d \pi } { d t } + \cos \pi \frac { d e } { d t } , } \\ { \displaystyle \frac { d R } { d e } = \frac { d R } { d t } \frac { \partial \vec { l } } { d e } + \frac { \partial R } { d t } \frac { \partial \vec { l } } { \partial e } - \sin \pi \frac { \partial R } { \partial h } + \cos \pi \frac { \partial R } { \partial t } , } \\ { \displaystyle \frac { \partial R } { \partial x } = \frac { \partial R } { \partial h } \frac { \partial h } { \partial \pi } + \frac { \partial R } { \partial t } \frac { \partial L } { \partial \pi } = e \cos \pi \frac { \partial R } { \partial h } - \epsilon \sin \pi \frac { \partial R } { \partial t } , } \\ { \displaystyle \frac { d p } { d t } = + \tan \left( \omega \Delta \omega \delta \frac { d \vec { l } } { d t } + \sec ^ { 2 } \dot { \omega } \sin \delta \frac { d \vec { l } } { d t } , \right. } \\ { \displaystyle \left. \frac { d \vec { l } } { d t } - \tan \dot { s } \sin \delta \frac { d \vec { l } } { d t } + \omega \omega ^ { \alpha } \dot { s } \cos \delta \frac { d \vec { l } } { d t } , \right. } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \displaystyle \frac { \partial R } { \partial \delta } = \frac { \partial R } { \partial p } \frac { \partial p } { \partial \delta } + \frac { \partial R } { \partial q } \frac { \partial q } { \partial \delta } } \\ { \displaystyle \quad = \tan i \cos \delta \frac { \partial R } { \partial p } - \tan i \sin \delta \frac { \partial R } { \partial q } , } \\ { \displaystyle \frac { \partial R } { \partial \dot { x } } = \frac { \partial R } { \partial p } \frac { \partial p } { \partial \dot { x } } + \frac { \partial R } { \partial q } \frac { \partial q } { \partial \dot { x } } } \\ { \displaystyle \quad = \sec ^ { 2 } i \sin \delta \frac { \partial R } { \partial p } + \sec ^ { 2 } i \cos \delta \frac { \partial R } { \partial q } . } \end{array} \right.
$$

Then it follows from (72) that

$$
\begin{array} { r l } &  \left\{ \begin{array} { l l } { \frac { d \vec { u } } { d t } = \frac { m _ { 1 } \cdot \vec { \nabla } - \vec { p } - \frac { \partial \vec { u } } { \partial t } } { 1 - \mu ^ { \xi } } \frac { \partial \vec { u } } { \partial t } } \\  \quad - \frac { \vec { p } \cdot \vec { \nabla } - \vec { u } - \vec { \nabla } - \vec { \nabla } \cdot \vec { \textbf { u } } } { 1 + \sqrt { 1 - \mu - \vec { \nabla } - \vec { p } } \frac { \partial \vec { u } } { \partial t } } \\  \quad - \frac { \vec { p } \cdot \vec { \nabla } - \vec { p } } { \mu \cdot \vec { \nabla } - \vec { \nabla } - \vec { \textbf { u } } } \frac { \vec { p } } { 1 + \sqrt { 1 - \mu - \vec { \nabla } - \vec { p } } \frac { \partial \vec { u } } { \partial t } } \\ { \quad + \frac { m _ { 2 } \cdot \vec { \nabla } - \vec { p } } { \mu \cdot \vec { \nabla } - \vec { \nabla } - \vec { \textbf { p } } \frac { \partial \vec { u } } { \partial t } } \end{array} \right. } \\ & { \frac { d } { d t } - \frac { - m _ { 3 } \cdot \vec { \nabla } - \vec { \nabla } \cdot \vec { \textbf { u } } } { \mu \cdot \vec { \nabla } - \vec { \textbf { u } } } } \\ & { \qquad \frac { \partial \vec { u } } { \partial t } \frac { \partial \vec { p } } { \partial t } { \partial t } } \\ &  \qquad - \frac { m _ { 1 } \cdot \vec { \nabla } - \vec { \textbf { p } } \cdot \vec { \textbf { u } } } { 1 + \sqrt { 1 - \mu - \vec { \nabla } - \vec { \textbf { p } } } \frac { \partial \vec { u } } { \partial t } } \\ & { \qquad - \frac { m _ { 3 } \cdot \vec { \textbf { p } } \cdot \vec { \textbf { u } } \frac { \partial \vec { p } } { \partial t } } { \partial t } \frac { \partial \vec { u } } { \partial t } } \\  \frac { d \vec { u } } { d t } - \frac { m _ { 2 } \cdot \vec { \textbf { u } } } { m _ { 3 } ^ { + } \textbf { f } - \vec { \textbf { p } } \frac { \partial \vec { u } } { \partial t } } & { \qquad \frac { \partial \vec { u } } { \partial t } } \end{array}
$$$$
\{ \begin{array} { l l } { \frac { d } { d t } = - \frac { - \omega _ { \mathrm { s } } \hbar \cdot k - \frac { - \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } } { \omega _ { \mathrm { s } } ^ { \delta } } } & { 0 } \\ { - \frac { - \omega _ { \mathrm { s } } \hbar \cdot k - \frac { \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } } { 1 - \omega _ { \mathrm { s } } ^ { \delta } } } & { 0 } \\ { - \frac { \omega _ { \mathrm { s } } \hbar \cdot k - \frac { \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } - \hbar \cdot ( - \delta \cdot \mathbf { k } - \delta ) } { 1 + \sqrt { 1 - k ^ { 2 } - \hbar } } \frac { \delta \cdot k } { \omega _ { \mathrm { s } } } } & { 0 } \\ { - \frac { \omega _ { \mathrm { s } } \hbar \cdot k - \frac { \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } } { \omega _ { \mathrm { s } } ^ { \delta } + \hbar \cdot ( 1 - k ^ { 2 } - \hbar ) } \frac { \delta \cdot k } { \omega _ { \mathrm { s } } ^ { \delta } } } & { 0 } \\ { \frac { d \delta } { d t } = \frac { \delta } { - \omega _ { \mathrm { s } } \hbar \cdot k - \frac { \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } - \hbar \omega _ { \mathrm { s } } \cdot k } \frac { \delta \cdot k } { \omega _ { \mathrm { s } } ^ { \delta } } } & { 0 } \\ { - \frac { \delta \cdot k } { 2 \omega _ { \mathrm { s } } \cdot k - \hbar \omega _ { \mathrm { s } } \cdot k } \frac { \delta \cdot k } { \omega _ { \mathrm { s } } \cdot k } \cos \omega _ { \mathrm { s } } ^ { \delta } \frac { [ \frac { \delta } { \omega } + \frac { \delta \cdot \mathbf { k } } { 2 } ] } { \omega _ { \mathrm { s } } ^ { \delta } } , } & { 0 } \\  \frac { d } { d t } = \frac { - \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { \omega _ { \mathrm { s } } \cdot k - \hbar \omega _ { \mathrm { s } } \cos { ( \frac { \delta } { \omega } + \frac { \delta \cdot \mathbf { k } } { 2 } ) } } & { 0 } \\  - \frac { \hbar \cdot ( - \delta \cdot \mathbf { k } ) } { 2 } \frac { \delta \cdot k } { \omega _ { \mathrm { s } } \cdot k } \cos \end{array}
$$

On developing the right members of these equations and neglecting all terms of degree higher than the frst\* in $\begin{array} { r } { h , l , p . } \end{array}$ and ${ \pmb q } .$ these

\*The terms of order higher than the first are neglected throughout in a later step in the method

equations reduce to

$$
\begin{array} { r } { \left\{ \begin{array} { l } { \frac { d h } { d t } = + \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial R } { \partial l } , } \\ { \frac { d l } { d t } = - \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial R } { \partial h } , } \\ { \frac { d p } { d t } = + \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial R } { \partial q } , } \\ { \frac { d q } { d t } = - \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial R } { \partial p } . } \end{array} \right. } \end{array}
$$

The terms which involve the derivative of $\pmb { R }$ with respect to ∈, $\dot { \iota _ { s } }$ and $\pmb { \pi }$ do not appear in these equations because they involve $h , l ,$ $\pmb { p }$ ,or $\pmb q$ as a factor. This fact follows from the properties of $\pmb { C }$ given in Art. 226 and the form of equations (103) and (104).

Each perturbing planet contributes terms in the right members of equations (1O7) similar to the ones written which come from $\mathbf { \nabla } m _ { 2 }$ These differential equations are not strictly correct，since the first approximation has already been made in neglecting the higher powers of the vaiiables.

The second step is in the method of treating the differential equations. The expansions of the $R _ { i , ~ i }$ contain certain terms which are independent of the time,which in the ordinary method give rise to the secular terms. Let ${ R ^ { ( 0 ) } } _ { i , ~ i }$ represent these terms. Lagrange then treated the differential equations by neglecting the periodic terms in $R _ { i , j } ,$ and writing

$$
\begin{array}{c} \begin{array} { r l } & { \left\{ \cfrac { d h _ { i } } { d t } = + \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial R ^ { ( 0 ) } { } _ { i } , j } { \partial l _ { i } } , \qquad ( \dot { \iota } = 1 , { } \right.} \end{array} \dots , n ; \dot { j } + i ) ,   \\ & { \left\{ \cfrac { d l _ { \dot { \iota } } } { d t } = - \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial R ^ { ( 0 ) } { } _ { i } , j } { \partial \dot { h } _ { i } } , \right. } \\ & { \left\{ \cfrac { d p _ { \dot { \iota } } } { d t } = + \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } \frac { \partial R ^ { ( 0 ) } { } _ { i } , j } { \partial q _ { \dot { \iota } } } , \right. } \\ & { \left. \cfrac { d q _ { \dot { \iota } } } { d t } = - \displaystyle \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial R ^ { ( 0 ) } { } _ { i } , j } { \partial p _ { \dot { \iota } } } . \right. } \end{array}
$$

The values of $h _ { i } , \ l _ { i } , \ p _ { i } ,$ and ${ { q } _ { i } }$ determined from equations (108）are used instead of the secular terms obtained by the method of Art.227. The process of breaking up a differential equation in this manner is not permissible except as a first approximation，and any conclusions based on it are open to suspicion.

In spite of the logical defects of the method and the fact that it cannot be generally applied,there is little doubt that in the present case it gives an accurate idea of the actual manner in which the elements vary.

The right members of equations (108)are expanded in powers of $h _ { i } , l _ { i } , p _ { i } ,$ and $q _ { \mathfrak { i } } ,$ and all of the terms except those of the first degree are neglected；consequently the terms omitted in (1O7） would have disappeared here if they had been retained up to this point. The system becomes linear，and the detailed discussion of the $R _ { i , ~ i }$ shows that it is homogeneous,giving equations of the form

$$
\begin{array} { r }  \{ \begin{array} { l } { \displaystyle \frac { d \vec { h } _ { 1 } } { d t } - \sum _ { j = 1 } ^ { n } c _ { 1 j } l _ { i } ^ { - 1 } = 0 , } \\ { \displaystyle \frac { d \vec { h } _ { 1 } } { d t } + \sum _ { j = 1 } ^ { n } c _ { 1 j } h _ { i j } = 0 , } \\ { \displaystyle \{ \frac { d \vec { h } _ { 2 } } { d t } - \sum _ { j = 1 } ^ { n } c _ { 2 j } l _ { i } = 0 ,  } \\ { \displaystyle \frac { d \vec { h } _ { 2 } } { d t } + \sum _ { j = 1 } ^ { n } c _ { 2 j } h _ { i j } = 0 , } \\ { \displaystyle \{ \begin{array} { l l l } { \displaystyle \frac { d \vec { h } _ { 3 } } { d t } + \sum _ { j = 1 } ^ { n } c _ { 3 j } h _ { i j } = 0 , } \\ { \displaystyle \frac { d \vec { h } _ { 4 } } { d t } - \sum _ { j = 1 } ^ { n } c _ { 3 j } h _ { i j } = 0 , } \\ { \displaystyle \frac { d \vec { h } _ { 5 } } { d t } - \sum _ { j = 1 } ^ { n } c _ { 3 j } h _ { i j } = 0 , } \\ { \displaystyle \frac { d \vec { h } _ { 6 } } { d t } + \sum _ { j = 1 } ^ { n } c _ { 3 j } h _ { i j } = 0 , } \end{array}  } \end{array} \end{array}
$$

and a similar system of equations in the $p _ { j }$ and the ${ \pmb q } _ { j }$

The coefficients $\pmb { c _ { i j } }$ depend only on the major axes (the $\epsilon _ { j }$ not appearing in the secular terms) which are considered as being constants,since the major axes have no secular terms in the perturbations of the first and second orders with respect to the masses. It is to be noted here that the assumption that the $\pmb { c _ { i j } }$ are constants is not strictly true because the major axes have periodic perturbations which may be of considerable magnitude.

When these linear equations are solved by the method used in Art.160, the values of the variables are found in the form

$$
\begin{array} { l c r } { { \displaystyle h _ { i } = \sum _ { j = 1 } ^ { n } H _ { i j } e ^ { \lambda _ { j } t } , \qquad } } & { { l _ { i } = \sum _ { j = 1 } ^ { n } L _ { i j } e ^ { \lambda _ { j } t } , } } \\ { { \displaystyle p _ { i } = \sum _ { j = 1 } ^ { n } P _ { i j } e ^ { \mu _ { j } t } , \qquad } } & { { q _ { i } = \sum _ { j = 1 } ^ { n } Q _ { i j } e ^ { \mu _ { j } t } , } } \end{array}
$$

where the $H _ { i j } , L _ { i j } , P _ { i j } ,$ and $Q _ { i j } ,$ are constants depending upon the initial conditions.A detailed discussion shows that the $\lambda _ { j }$ and $\mu _ { \mathrm { j } }$ are all pure imaginaries with very small absolute values； therefore the $h _ { i } , \ l _ { i } , \ p _ { i } ,$ and $q _ { i }$ oscillate around mean values with very long periods.Or,since the $e _ { j }$ and tan $i _ { j }$ are expressible as the sums of squares of the $h _ { i } , \ l _ { j } , \ p _ { i } .$ and ${ { q } _ { i } }$ ,it follows that they also perform small oscillations with long periods；for example，the eccentricity of the earth's orbit is now decreasing and will continue to decrease for about 24,000 years.

Equations (1O9) admit integrals first found by Laplace in 1784, which lead practically to the same theorem. They are

$$
\left\{ \begin{array} { l l } { { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { i } { } ^ { 2 } ( h _ { j } { } ^ { 2 } + \mathit { l } _ { i } { } ^ { 2 } ) = \mathrm { C o n s t a n t } = C , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } n _ { i } a _ { i } { } ^ { 2 } ( p _ { i } { } ^ { 2 } + q _ { i } { } ^ { 2 } ) = C ^ { \prime } ; } } \end{array} \right.
$$

or, because of (103) and (104),

$$
\left\{ \begin{array} { r } { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { i } ^ { \ : 2 } e _ { j } ^ { \ : 2 } = C } , } \\ { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { i } ^ { \ : 2 } \tan ^ { 2 } i _ { j } = C ^ { \prime } } , } \end{array} \right.
$$

where $\boldsymbol { n } _ { j }$ is the mean motion of $m _ { j } .$ The constants $c$ and $c ^ { \prime }$ as determined by the initial conditions are very small,and since the left members of (112) are made up of positive terms alone, no $e _ { \gimel }$ or $i _ { j }$ can ever become very great. There might be an exception if the corresponding $\mathbf { \nabla } m _ { j }$ were very small compared to the others.

Equations (112) give the celebrated theorems of Laplace that the eccentricities and inclinations cannot vary except within very narrow limits. Although the demonstration lacks complete rigor, yet the results must be considered as remarkable and significant. Equations (1l2) do not give the periods and amplitudes of the oscillations as do equations (110).

230. Computation of Perturbations by Mechanical Quadratures. If the second term of the second factor of (84) in absolute value is greater than unity,the series (87) does not converge and cannot be used in computing perturbations. The expansions may fail because $\pmb { r _ { 1 } }$ and $\pmb { r _ { 2 } }$ are very nearly equal; or, sometimes when they are not nearly equal， because $\boldsymbol { \mathit { I } }$ is large.In the latter case another mode of expansion sometimes can be employed,\* but there are cases in which neither method leads to valid results. They both fail if the two orbits placed in the same plane would intersect, for in this case

$$
r ^ { 2 } _ { 1 , ~ 2 } = r _ { 1 } { } ^ { 2 } + r _ { 2 } { } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos { ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) } ,
$$

would vanish when the two bodies arrive at a point of intersection of their orbits at the same time. Unless the periods are commensurable in a special way this would always happen. Of course,it is not necessary that $\boldsymbol { r } _ { 1 , \mathrm { ~ 2 ~ } }$ should actually vanish in order that the expansion of (84) should fail to converge.

Perturbations can be computed by the method of mechanical quadratures without expanding the perturbative function explicitly in terms of the time. Consequently,this method can be used in computing the disturbing effects of planets on comets and in other cases where the expansion of $R _ { 1 , \ 2 }$ fails altogether or converges slowly.Let s represent an element of the orbit of $\pmb { m _ { 1 } }$ ；then equations (77) can be written in the form

$$
\frac { d s } { d t } = f _ { s } ( t ) ,
$$

and the perturbations of the frst order in the interval $t _ { n } - t _ { 0 }$ are

$$
s = s _ { 0 } + \int _ { t _ { 0 } } ^ { t _ { n } } f _ { \bullet } ( t ) d t ,
$$

where ${ \pmb { \mathscr { s } } } _ { \pmb { 0 } }$ is the value of $\pmb { \mathscr { s } }$ at $t = t _ { 0 }$ ·

The only difficulty in computing perturbations is in forming the integrals indicated in (113). When the perturbative function cannot be expanded explicitly in terms of $\pmb { t }$ the primitive of the function $f _ { s } ( t )$ cannot be found. But in any case the values of $f _ { \mathfrak { s } } ( t )$ can be found for any values of $\mathbf { \Delta } _ { t }$ ，and from the values of $f _ { s } ( t )$ for special values of $\pmb { t }$ an approximation to the integral can be obtained.Geometrically considered，the integral (113) is the area comprised between the $\scriptstyle t .$ axis and the curve $f = f _ { s } ( t )$ and the ordinates $\scriptstyle t _ { 0 }$ and $t _ { n }$ .An approximate value of the integral is

$$
s \doteq s _ { 0 } + f _ { s } ( t _ { 0 } ) ( t _ { 1 } - t _ { 0 } ) + f _ { s } ( t _ { 1 } ) ( t _ { 2 } - t _ { 1 } ) + \cdots + f _ { s } ( t _ { n - 1 } ) ( t _ { n } - t _ { n - 1 } ) .
$$

The intervals $t _ { 1 } - t _ { 0 } , t _ { 2 } - t _ { 1 } , \cdot \cdot \cdot , t _ { n } - t _ { n - 1 }$ can be taken so small that the approximation will be as close as may be desired.

Another method of obtaining an approximate value of the integral is to replace the curve fs(t),whose explicit value in convenient form may not be obtainable,by a polynomial curve of the nth degree which agrees in value with $f _ { s } ( t )$ at $t = t _ { 0 } , t _ { 1 } , \ldots , t _ { n }$ The equation of this polynomial is

$$
\begin{array} { r l r } { f _ { s } = \displaystyle + \frac { ( t - t _ { 1 } ) ( t - t _ { 2 } ) \cdot \cdot \cdot \cdot ( t - t _ { n } ) } { ( t _ { 0 } - t _ { 1 } ) ( t _ { 0 } - t _ { 2 } ) \cdot \cdot \cdot \cdot ( t _ { 0 } - t _ { n } ) } f _ { s } ( t _ { 0 } ) } & { } & \\ { + \frac { ( t - t _ { 0 } ) ( t - t _ { 2 } ) \cdot \cdot \cdot \cdot ( t - t _ { n } ) } { ( t _ { 1 } - t _ { 0 } ) ( t _ { 1 } - t _ { 2 } ) \cdot \cdot \cdot \cdot ( t _ { 1 } - t _ { n } ) } f _ { s } ( t _ { 1 } ) } & \\ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } & \\ { + \frac { ( t - t _ { 0 } ) ( t - t _ { 1 } ) \cdot \cdot \cdot \cdot \cdot ( t - t _ { n - 1 } ) } { ( t _ { n } - t _ { 0 } ) ( t _ { n } - t _ { 1 } ) \cdot \cdot \cdot \cdot ( t _ { n } - t _ { n - 1 } ) } f _ { s } ( t _ { n } ) . } & \end{array}
$$

Since there is no trouble in forming the integral of a polynomial there is no trouble in computing the perturbation of s for the interval $t _ { n } \mathrm { ~ - ~ } t _ { 0 }$ .If the value of the function $f _ { s } ( t )$ is not changing veryrapidly or irregularly,its representation by a polynomial is very exact provided the intervals $t _ { 1 } - t _ { 0 } ,$ …， $t _ { n } \mathrm { ~ - ~ } t _ { n - 1 }$ are not too great.

However, the area between the polynomial, the $\scriptstyle t$ -axis,and the limiting ordinates is not the best approximation to the value of the integral that can be obtained from the values of $f _ { s } ( t )$ at $t _ { 0 _ { } }$ ， $\cdots , t _ { n }$ .The values of the function give information respecting the nature of the curvature of the curve between the ordinates (this being true,of course，only because the function $f _ { s } ( t )$ isa regular function of $\dot { t }$ ，and corrections of the area due to these curvatures can easily be made. Ordinarily they would involve the derivatives of $f _ { s } ( t )$ at $t _ { 0 } , \cdots , t _ { n } ,$ ，which would require a vast amount of labor to compute；but the derivatives can be expressed with sufficient approximation in terms of the successive differences of the function，and the differences are obtained directly from the tabular values by simple subtraction. The derivation of the most convenient explicit formulas is a lengthy matter and must be omitted.\*

Suppose the computation of the integrals from the values of $f _ { s } ( t )$ at $t = t _ { 0 } , \cdots , t _ { n }$ has not given results which are sufficiently exact. More exact ones can be obtained by dividing the interval $t _ { n } - t _ { 0 }$ into a greater number of sub-intervals. A little experience usually makes it unnecessary to subdivide the intervals first chosen.

There is a second reason why the results obtained by mechanical quadratures may not be suffciently exact. It has so far been assumed that $f _ { \mathfrak { s } } ( t )$ is a function of $t$ alone;or,in other words, that the elements of the orbits on which it depends are constants. This is the assumption in computing perturbations of the first order. If it is not exact enough, new values of $f _ { s } ( t _ { 1 } ) , \cdots , f _ { s } ( t _ { n } )$ can be computed,on using in them the respective values of the elements s which were found by the first integration. From the new values of $f _ { s } ( t _ { 1 } ) , \ \cdots , f _ { s } ( t _ { n } )$ a more approximate value of the integral can be obtained. Unless the interval $t _ { n } \mathrm { ~ - ~ } t _ { 0 }$ is too great this process converges and the integral can be found with any desired degree of approximation，because this method is simply Picard's method of successive approximations whose validity has been established.\* In practice it is always advisable to choose the interval $t _ { n } - t _ { 0 }$ so short that no repetition of the computation with improved values of the function at the ends of the sub-intervals will be required. At each new stage of the integration the values of the elements at the end of the preceding step are employed.It follows that the method,as just explained, enables one to compute not only the perturbations of the first order, but perturbations of all orders except for the limitations that the intervals cannot be taken indefinitely small and the computation cannot be made with indefinitely many places.

The process of computing perturbations by the method of mechanical quadratures,as compared with that of using the expanded form of the perturbative function， has its advantages and its disadvantages. It is an advantage that in employing mechanical quadratures it is not necessary to express the perturbing forces explicitly in terms of the elements and the time. This is sometimes of great importance,for,in cases where the eccentricities and inclinations are large,as in some of the asteroid orbits，these expressions,which are series,are very slowly convergent；and in the case of orbits whose eccentricities exceed 0.6627,or of orbits which have any radius of one equal to any radius of the other the series are divergent and cannot be used. The method of mechanical quadratures is equally applicable to all kinds of orbits,the only restriction being that the intervals shall be taken sufficiently short. It is the method actually employed, in one of its many forms,in computing the perturbations of the orbits of comets.

\* Picard’'s Traite d'Analyse, vol. I1.,chap. X1.,section 2.

The disadvantages are that,in order to find by mechanical quadratures the values of the elements at any particular time, it is necessary to compute them at all of the intermediate epochs. Being purely numerical, it throws no light whatever on the general character of perturbations,and leads to no general theorems regarding the stability of a system. These are questions of great interest，and some of the most brilliant discoveries in Celestial Mechanics have been made respecting them.

231.General Reflections. Astronomy is the oldest science and in a certain sense the parent of all the others. The relatively simple and regularly recurring celestial phenomena first taught men,in the days of the ancient Greeks, that Nature is systematic and orderly. The importance of this lesson can be inferred from the fact that it is the foundation on which all science is based. For a long time progress was painfully slow. Centuries of observations and attempts at theories for explaining them were necessary before it was finally possible for Kepler to derive the laws which are a first approximation to the description of the way in which the planets move. The wonder is that,in spite of the distractions of the constant struggles incident to an unstable social order, there should have been so many men who found their greatest pleasure in patiently making the laborious observations which were necessary to establish the laws of the celestial motions.

The work of Kepler closed the preliminary epoch of two thousand years,or more，and the brilliant discoveries of Newton opened another. The invention of the Calculus by Newton and Leibnitz furnished for the first time mathematical machinery which was at all suitable for grappling with such difficult problems as the disturbing effects of the sun on the motion of the moon,or the mutual perturbations of the planets. It was fortunate that the telescope was invented about the same time; for, without its use, it would not have been possible to have made the accurate observations which furnished the numerical data for the mathematical theories and by which they were tested. The history of Celestial Mechanics during the eighteenth century is one of a continuous series of triumphs. The analytical foundations laid by Clairaut, d'Alembert,and Euler formed the basis for the splendid achievements of Lagrange and Laplace. Their successors in the nineteenth century pushed forward,by the same methods on the whole, the theories of the motions of the moon and planets to higher orders of approximation and compared them with more and better observations. In this connection the names of Leverrier,Delaunay, Hansen,and Newcomb will be especially remembered. Near the close of the nineteenth century a third epoch was entered. It is distinguished by new points of view and new methods which，in power and mathematical rigor，enormously surpass all those used before.It was inaugurated by Hill in his Researches on the Lunar Theory,but owes most to the brilliant contributions of Poincaré to the Problem of Three Bodies.

At the present time Celestial Mechanics is entitled to be regarded as the most perfect science and one of the most splendid achievements of the human mind. No other science is based on so many observations extending over so long a time. In no other science is it possible to test so critically its conclusions,and in no other are theory and experience in so perfect accord. There are thousands of small deviations from conic section motion in the orbits of the planets,satellites,and comets where theory and the observations exactly agree,while the only unexplained irregularities (probably due to unknown forces) are a very few small ones in the motion of the moon and the motion of the perihelion of the orbit of Mercury. Over and over again theory has outrun practise and indicated the existence of peculiarities of motion which had not yet been derived from observations. Its perfection during the time covered by experience inspires confidence in following it back into the past to a time before observations began,and into the future to a time when perhaps they shall have ceased. As the telescope has brought within the range of the eye of man the wonders of an enormous space,so Celestial Mechanics has brought within reach of his reason the no lesser wonders of a correspondingly enormous time. It is not to be marveled at that he finds profound satisfaction in a domain where he is largely freed from the restrictions of both space and time.

# XXVII. PROBLEMS.

1. Suppose $( a )$ that $\scriptstyle { \mathcal { R } } _ { 1 , \mathrm { ~ 2 ~ } }$ is large and nearly constant; $( b )$ that $\smash { \mathcal { R } _ { 1 , 2 } }$ is large and changing rapidly； (c) that $\scriptstyle R _ { 1 , \ 2 }$ is small and nearly constant. If the perturbations are computed by mechanical quadratures how should the $t _ { n } - t _ { 0 }$ be chosen relatively in the three cases,and how should the numbers of subdivisions of $t _ { n } ~ \sim t _ { 0 }$ compare?

2.The perturbative function involves the reciprocal of the distance from the disturbing to the disturbed planets.This is called the principal part and gives the most difficulty in the development.How many separate reciprocal distances must be developed in order to compute,in a system of one sun and $\pmb { n }$ planets, $( a )$ the perturbations of the first order of one planet；(b) the perturbations of the first order of vwo planets;(c) the perturbations of the second order of one planet; and $( d )$ the perturbations of the third order of one planet?

3.What simplifications would there be in the development of the perturbative function if the mutual inclinations of the orbits were zero,and if the orbits were circles?

4.What sorts of terms will in general appear in perturbations of the third order with respect to the masses?

# HISTORICAL SKETCH AND BIBLIOGRAPHY.

The theory of perturbations,as applied to the Lunar Theory,was developed from the geometrical standpoint by Newton. The memoirs of Clairaut and D'Alembert in 1747 contained important advances,making the solutions depend upon the integration of the differential equations in series. Clairaut soon had occasion to apply his processes of integration to the perturbationg of Halley's comet by the planets Jupiter and Saturn. This comet had been observed in 1531,1607,and 1682．If its period were constant it would pass the perihelion again about the middle of 1759.Clairaut computed the perturbations due to the attractions of Jupiter and Saturn,and predicted that the perihelion passage would be April 13,1759．He remarked that the time was uncertain to the extent of a month because of the uncertainties in the masses of Jupiter and Saturn and the possibility of perturbations from unknown planets beyond these two. The comet passed the perihelion March 13, giving a striking proof of the value of Clairaut's methods.

The theory of the perturbations of the planets was begun by Euler,whose memoirs on the mutual perturbations of Jupiter and Saturn gained the prizes of the French Academy in 1748 and 1752. In these memoirs was given the first analytical development of the method of the variation of parameters. The equations were not entirely general as he had not considered the elements as being all simultaneously variables. The first steps in the development of the perturbative function were also given by Euler.

Lagrange,whose contributions to Celestial Mechanics were of the most brillant character，wrote his frst memoir in 1766 on the perturbations of Jupiter and Saturn．In this work he developed still further the method of the variation of parameters,leaving his final equations,however,still incorrect by regarding the major axes and the epochs of the perihelion passages as constants in deriving the equations for the variations. The equations for the inclination，node,and longitude of the perihelion from the node were perfectly correct.In the expressions for the mean longitudes of the planets there were terms proportional to the first and second powers of the time. These were entirely due to the imperfections of the method, their true form being that of the long period terms,as was shown by Laplace in 1784 by considering terms of the third order in the eccentricities. The method of the variation of parameters was completely developed for the first time in 1782 by Lagrange in a prize memoir on the perturbations of cometg moving in elliptical orbits.By far the most extensive use of the method of variation ol parameters is due to Delaunay， whose Lunar Theory is essentially a long succession of the applications of the process, each step of it removing a term from the perturbative function.

In 1773_Laplace presented his first memoir to the French Academy of Sciences.In it he proved his celebrated theorem that，up to the second powers of the eccentricities,the major axes，and consequently the mean motions of the planets,have no secular terms. This theorem was extended by Lagrange in 1774 and 1776 to all powers of the eccentricities and of the sine of the angle of the mutual inclination,for perturbations of the first order with respect to the masses.Poisson proved in 1809 that the major axes have nc purely secular terms in the perturbations of the second order with respect t(. the masses. Haretu proved in his Dissertation at Sorbonne in 1878 that there are secular variations in the expressions for the major axes in the terms of the third order with respect to the masses.In vol.xix.of Annales de l'Observatoire de Paris,Eginitis considered terms of still higher order with respect to the masses.

Lagrange began the study of the secular terms in 1774, introducing the variables $h , \ l , \ p _ { \ast }$ and ${ \pmb q }$ The investigations were carried on by Lagrange and Laplace,each supplementing and extending the work of the other,until 1784 when their work became complete byLaplace's discovery of his celebrated equations

$$
\left\{ \begin{array} { l l } { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { , } n _ { j } a _ { j } ^ { 2 } e _ { j } ^ { \mathrm { \Delta } } = C } , } \\ { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { j } ^ { 2 } \tan ^ { 2 } i _ { j } = C ^ { \prime } } . } \end{array} \right.
$$

These equations were derived by using only the linear terms in the differential equations.Leverrier,Hill,and others have extended the work by methods of successive approximations to terms of higher degree.Newcomb (Smithsonian Contributions to Science,vol.xxi.,1876) has established the more far-reaching results that it is possible,in the case of the planetary perturbations,to represent the elements by purely periodic functions of the time which formally satisfy the differential equations of motion. If these series were convergent the stability of the solar system would be assured;but Poincaré has shown that they are in general divergent (Les Methodes Nouvelles de la Mecanique Celeste, chap. Ix.). Lindstedt and Gylden have also succeeded in integrating the equations of the motion of $^ { n }$ bodies in periodic series，which,however, are in general divergent.

Gauss，Airy，Adams,Leverrier，Hansen，and many others have made important contributions to the planetary theory in Bome of its many aspects. Adams and Leverrier are noteworthy for having predicted the existence and apparent position of Neptune from the unexplained irregularities in the motion of Uranus.More recently Poincaré turned his attention to Celestial Mechanics, publishing a prize memoir in the Acta Mathematica,vol.xi1. This memoir was enlarged and published in book form with the title Les Methodes Nouvelles de la Mécanique Celeste.Poincaré applied to the problem all the resources of modern mathematics with unrivaled genius; he brought into the investigation such a wealth of ideas,and he devised methods of such immense power that the subject in its theoretical aspects has been entirely revolutionized in his hands.It cannot be doubted that much of the work of the next fifty years will be in amplifying and applying the processes which he explained.

The following works should be consulted:

Laplace's Mécanique Celeste,containing practically all that was known of elestial Mechanics at the time it was written (1799-1805).

On the variation of parameters-Annales de l'Observatoire de Paris,vol. 1.; Tisserand's Mécanique Celeste,vol.1.；Brown's Lunar Theory；Dziobek's Planeten-Bewegungen.

On the development of the perturbative function-Annales de l'Observatoire deParis,vol.1.; Tisserand's Mécanique Celeste,vol.1.;Hansen's Entwickelung desProducts einer Potenz des Radius-Vectors mit dem Sinus oder Cosinus eines Vielfachen der wahren Anomalie, etc., Abh.d.K.Sachs.Ges.zu Leipzig,vol.11.; Newcomb's memoir on the General Integrals of Planetary Motion;Poincaré, Les Méthodes Nouvelles,vol.1., chap. VI.

On the stability of the solar system-Tisserand's Mecanique Celeste, vol.1., chaps.X1., xxv., xxvi.,and vol.Iv., chap.xxvI.;Gylden,Traité Analytique des Orbites absolues,vol.1.; Newcomb, Smithsonian Cont.,vol. xxi.;Poincare, Les Méthodes Nouvelles de la Mécanique Celeste,vol.I., chap.x.

On the subject of Celestial Mechanics as a whole there is no better work available than that of Tisserand, which should be in the possession of every one giving special attention to this subject. Another noteworthy work is Charlier's Mechanik des Himmels,which,besides maintaining a high order of general excellence,is unequaled by other treatises in its discussion of periodie solutiong of the Problem of Three Bodies.

# INDEX.

Abbott,66   
Acceleration in rectilinear motion,9 curvilinear motion,11   
Adams,363,432   
Airy，,363,365,432   
Albategnius,32   
Allegret,319   
Almagest,32   
Al-Sufi,32   
Anaximander,31   
Annual equation,348   
Anomaly,eccentric,159 mean,159 true,155   
Appell,7,10,35,97,162   
Archimedes, 33   
Areal velocity,15   
Argument of latitude,162   
Aristarchus,31   
Aristotle,31   
Atmospheres,escape of,46   
Attraction of circular discs,103 ellipsoids 99,122,127 spheres,99,101,104, 114 spheroids,119,132,133

Backhouse,305   
Ball,W.W.R.,35   
Baltzer,376   
Barker's tables,156   
Barnard,305   
Bauschinger,260   
Bernouilli,Daniel,190   
J., 67   
Berry，,35   
Bertrand, 97   
Boltzmann, 3, 67   
Bour,319   
Brorsen,305   
Brown,351,352,365,433   
Bruns,218,276,281   
Buchanan,ne,   
Buchholz，222,260   
Buck,320   
Budde,35   
Burbury,67   
Burnham,85   
Cajori,35   
Calory,60   
Canonical equations, 390   
Cantor,35   
Carmichael,35   
Cauchy,367,378   
Center of gravity,22   
mass,19,20,24   
Central force,69   
Chaldaeans,31   
Chamberlin and Salisbury，68   
Charlier,216,259,427,433   
Chasles,8,   
Chauvenet,190,197   
Circular orbits for three bodies,309   
Clairaut,356,363,364,367,429,431   
Clausius,67   
Contraction theory of sun's heat, 63   
Copernicus, 33   
d'Alembert,3,7,363,429,431   
Damoiseau,364   
Darboux,97,18   
Darwin,68,139,280,281,305,320   
Delambre,35   
Delaunay，364,430,432   
De Pontecoulant,364   
Descartes,190   
Despeyrous,97,138   
Differential crrections,162,220   
Differential equations of orbit,80   
Dirichlet,138   
Disturbing forces,resolution of,324   
Doolittle,Eric,61   
Double points of surfaces of zero ve   
locity,290   
Double star orbits, 85   
Duhring,35   
Dziobek,433   
Eccentric Anomaly,159   
Eginitis,432   
Egyptians,30   
Elements of orbits,146,148,183   
Elements,intermediate,192   
Energy,inetic,potential,59   
Equations of relative motion,142   
Equipotential curves,283   
surfaces, 113   
Eratosthenes,31   
Escape of atmospheres,46   
Euclid,32   
Euler,24，34,138,158,190,258,363,   
364,367,429,431   
Euler's equation,157,275   
Evection,the,359

Falling bodies,36   
Force varying as distance, 90 inversely assquare of distance, 92 fthpower ofdistance,93   
Galileo,3,33,34,67   
Gauss,138,139,153,154,188,190, 193,194,231,238,240,242,243， 244,249,259,260,360,361,432   
Gauss'equations,238,240   
Gegenschein,305   
Gibbs,260   
Glaisher，97   
Grant,35   
Greek philosophers,30,429   
Green,109,138,139   
Griffin,88,97,20   
Gylden,305,432   
Halley,258,348,363   
Halphen,97   
Hamilton,3,275   
Hankel,35   
Hansen,364,430,432,433   
Haretu,432   
Harknessand orley,292   
Harzer,231,232,259   
Heat of sun,59   
Height of projection,45   
Helmholtz,63,68   
Herodotus,30   
Herschel,John,325,65 William,85   
Hertz,3,35   
Hilbert,67   
Hill,68,280,281,287,319,351,352, 356,361,365,430,432   
Hipparchus,31,,9   
Holmes,68   
Homoeoid,100   
Huyghens,34   
Ideler,35   
Independent star-numbers,194   
Infinitesimal body,277   
Integrals of areas,144,264 center of mass141,262   
Integralof energy,267   
Integration in series,172,200,202, 227,377   
Invariable plane,266   
Ivory,116,127,132,138   
Jacobi,139,267,274,275,280,281, 319   
Jacobi's integral,280   
Jeans,67   
Joule,60   
Kepler,33,82,83,152,190,429   
Kepler's equation,159,160,163,165 laws，82 third law,152   
Kinetic theory of gases, 46   
Kirchhoff,3   
Klinkerfues,222,260   
Koenigg,35,97   
Laertius, 30   
Lagrange,7,34,107,132,138,161, 193,227,259,277,312,319,363, 364,387,418,421,423,429,431, 432   
Lagrange's brackets, 387 quintic equation,312   
Lagrangian solutions of the problem ofthreebodies,277,291,309,313   
Lambert,158,258,259   
Lane,68   
Laplace,34,132,138,172,193,194, 231,249,258,259,266,275,319, 348,350,352,362,364,367,418, 425,429,431,432,433   
Laue,35   
Law of areas,69 converse of,73 forcein binary starg,86   
Laws of angular andlinearvelocity，7 Kepler,82 motion,3   
Lebon,35   
Legendre,97,138   
Lehmann-Filhes,319   
Leibnitz,429   
Leonardo da Vinci, 33   
Leuschner,222,231,232,259   
Level surfaces,113   
Leverrier，361,363,400,406,413, 430,432   
Levi-Civita,268   
Linstedt,319,432   
Liouville, 319   
Longperiod inequalities 361,371, 416   
Longley， 320   
Love,35   
Lubbock,364   
Lunar theory，,337   
MacCullagh,138   
Mach,3,6,35   
Maclaurin,34,132,19   
MacMillan,169,20   
Marie,35   
Mathieu,319   
Maxwell,67   
Mayer,Robert,68 Tobias,364   
McCormack,35   
Mean anomaly,159

Mechanical quadratures, 425 Meteoric theory of sun's heat,62 Meton,31 Metonic cycle, 31 Meyer,O.E.,67 Motion of apsides, 352 center of mass, 141, 262 falling particles, 36 Neumann, 139 Newcomb,275,361,430,432,433 Newton,H.A.,62,05 Newton,3,5,6,7,29,33,34,67,82, 84,97,99,101,138,10,258,275, 320,327,350,356,365,429,431 Newton's law of gravitation, 82,84 lawsofmotion,3 Normal form of differential equations, 75 Node,ascending,descending,182 Nyren,318 Qlberg,259 Omar,32 Oppolzer，156,222,242,260,370 Order of differentalquatio,74 Osculating conic, 322 Parabolic motion,.56 Parallactic inequality, 352 Parallelogram of forces,5 Periodic varations,371,413 Perturbations,meaning of,321 by oblate body,333 resisting medium,333 of apsides,352 elements,322,382 frst order,382 inclination, 343 major axis,346 node,342 period,348 Perturbative function,272 resolution of,337, 338,345,402 Peurbach,32 development of,406 Picard,378,428 Plana364 Planck,35 Plummer,302 Poincare,35,139,267,268,275,276, 281,320,367,378,432,433 4,4 Poisson terms,371 Position inelliptic orbits,158 hyperbolic orbits,177 parabolic orbits,155 Potential,109,261 Precession of equinxes, 344 Preston,60

Problem of two bodies,140 three bodies,277 nbodies，261 Ptolemy,32,359 Pythagoras,31 Question of new integrals, 268 Radau, 274, 319 Ratios of triangles,233,237 Rectilinear motion, 36 Regiomontanus,32 Regions of real and imaginary velocity，286 Relativity， rinciple of4 Resolution of disturbing force,337, 338 Risteen,67 Ritter,68 Rodriguez,138 Routh，35,139 Rowland,60 Rutherford, 68 Salmon, 88 Saracens,32 Saros,31 Secular acceleration of moon's motion. 348 Secular variations,360,371,417 Solid angles98 Solution of linear equations by exponentials,41 Solutions of problem of three bodies, 290,309,313 Speed,8 Spencer,59 Stability ofsolutions,298,306 Stader,97 Stevinus,33,67 Stirling，138' Stoney，46 Sturm139 Surfaces of zero relative velocity, 281 Suter,35 Tait,35 Tait and Steele, 35, 97 Tannery,35 Temperatureof meteors, 61 Thales,30,31 Thomson,139 Thomson'and Tait,3,104,139,283 Time aberration,226 Teand97,19,190,260,267,276, 295,296,312,319,365,391,407, 426,427,433 Tisserand's criterion for identity of comets,295 Trueanomaly，155 Tycho Brahe,33,348,350

Uniform motion,8   
Ulugh Beigh,32   
Units,153 canonical,154   
Variation, the,350   
Variation of coordinates,321 elements,322 parameters 50,322   
Vector,5   
Velocity， 8 areal,15 from'infinity,45,46 of escape, 48   
Villarceau, 259

Vis viva integral,78,267   
Voltaire,190   
Waltherus,32   
Waterson,162   
Watson,156,242,260   
Weierstrass,367   
Whewell, 35   
Williamson,161   
Wolf，35   
Woodward, 4   
Work,59

Young, 164
