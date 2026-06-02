# 443 Order arrows for linear multistep methods

Given a relationship between complex numbers $z$ and $w$ defined by an equation of the form

$$
\Phi ( w \exp ( z ) , z ) = 0 ,
$$

we can define order arrows as the set of points for which $w$ is real and positive. In particular, the order arrows that emanate from zero correspond to $w$ with increasing real parts (the up arrows) and, on these arrows, $w \in ( 1 , \infty )$ , or decreasing real parts (the down arrows) and for which $w \in [ 0 , 1 )$ .

Order arrows on Riemann surfaces are illustrated for the BDF2 method (Figure 443(i)) and for the BDF3 method (Figure 443(ii)). Just as for Runge– Kutta methods, the up arrows either terminate at the pole $z = \beta _ { 0 } ^ { - 1 }$ or at $- \infty$ , and down arrows terminate at the zero $z = - \alpha _ { k } \beta _ { k } ^ { - 1 }$ or at $+ \infty$ . In interpreting these remarks, we need to allow for the possibility that the path traced out by an up or down arrow meets another arrow at a branch point of the Riemann surface. However, this special case is easily included in the general rule with a possible freedom to choose between two continuations of the incoming arrow.

The ‘principal sheet’ of the Riemann surface will refer to a neighbourhood of $( 0 , 1 )$ for which the relationship between $z$ and $w$ is injective; that is, it behaves as though $w$ is a function of $z$ . As long as $\Phi ( w , 0 )$ has only a single zero with value $w = 1$ , this idea makes sense. On the principal sheet, $w \exp ( z ) = \exp ( z ) + { \cal O } ( z ^ { p + 1 } )$ , and the behaviour at zero is similar to what happens for one-step methods. These simple ideas are enough to prove the Dahlquist second order bound:

Theorem 443A An A-stable linear multistep method cannot have order greater than 2.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/a6c48597940bcb930de1e2bc67a55aae50a0c81c3c6e4be3b281c5a5b6bb9dca.jpg)  
Order arrows for order 2 BDF method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/caa015d4de9e48f4ea8095f1af08bf2c09164480b8a81be6793de475a78e01f0.jpg)  
Order arrows for order 3 BDF method

Proof. If the order were greater than 2, there would be more than three up arrows emanating from the origin. At least three of these up arrows would come out in the positive direction (or possibly would be tangential to the imaginary axis). Since there is only one pole, at least two of these arrows would cross the imaginary axis (or be tangential to it). Hence, the stability region does not include all of the imaginary axis and the method is not Astable. 

We can make this result more precise by obtaining a bound on the error constant for second order A-stable methods. The result yields an optimal role for the second order Adams–Moulton method, for which the error constant is $- { \frac { 1 } { 1 2 } }$ , because

$$
\exp ( z ) - \frac { 1 + \frac { 1 } { 2 } z } { 1 - \frac { 1 } { 2 } z } = - \frac { 1 } { 1 2 } z ^ { 3 } + O ( z ^ { 4 } ) .
$$

It is not possible to obtain a positive error constant amongst A-stable second order methods, and it is not possible to obtain an error constant smaller in magnitude than for the one-step Adams–Moulton method. To prove the result we use, in place of $\exp ( z )$ , the special stability function $( 1 + \textstyle { \frac { 1 } { 2 } } z ) / ( 1 - \textstyle { \frac { 1 } { 2 } } z )$ in forming a relative stability function.

Theorem 443B Let $C$ denote the error constant for an $A$ -stable second order linear multistep method. Then

$$
C \leq - { \frac { 1 } { 1 2 } } ,
$$

with equality only in the case of the second order Adams–Moulton method.

Proof. Consider the relation

$$
\Phi \left( w \frac { 1 + \frac { 1 } { 2 } z } { 1 - \frac { 1 } { 2 } z } , z \right) = 0 .
$$

On the principal sheet, $w = 1 - ( C + { \textstyle { \frac { 1 } { 1 2 } } } ) z ^ { 3 } + O ( z ^ { 4 } )$ . It is not possible that $\begin{array} { r } { C + \frac { 1 } { 1 2 } = 0 } \end{array}$ , because there would then be at least four up arrows emanating from 0 and, as in the proof of Theorem 443A, this is impossible because there is at most one pole in the right half-plane. On the other hand, if $C + { \textstyle { \frac { 1 } { 1 2 } } } > 0$ , there would be at least two up arrows emanating from zero in the positive direction and these must cross the imaginary axis. 

# Exercises 44

44.1 Show that, for a stable linear multistep method with order $k + 2$ , all zeros of $\alpha$ are on the unit circle.

44.2 Show that the BDF3 method is not A-stable, by selecting a complex number $x$ with negative real part for which the corresponding difference equation is not stable.
