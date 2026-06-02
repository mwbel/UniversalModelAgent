# 430 Introduction

In contrast to Runge–Kutta methods, in which stability regions are determined by a single stability function, the stability properties of linear multistep methods are inextricably bound up with difference equations. We consider the example of the second order Adams–Bashforth method

$$
y _ { n } = y _ { n - 1 } + { \frac { 3 } { 2 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \frac { 1 } { 2 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) .
$$

For the differential equation $y ^ { \prime } = q y$ , this becomes

$$
y _ { n } = y _ { n - 1 } + { \frac { 3 } { 2 } } h q y _ { n - 1 } - { \frac { 1 } { 2 } } h q y _ { n - 2 } ,
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/acfaf47d423c409db6fa6d46d4f1b01832aab6824c8f03925ca3c5a8ba99abf1.jpg)  
Stability region for the second order Adams–Bashforth method

so that stable behaviour occurs if $h q = z$ , where $z$ is such that the equation

$$
y _ { n } = \Big ( 1 + \frac { 3 } { 2 } z \Big ) y _ { n - 1 } - \frac { 1 } { 2 } z y _ { n - 2 }
$$

has only bounded solutions. This occurs when the polynomial equation

$$
w ^ { 2 } - \Big ( 1 + \frac { 3 } { 2 } z \Big ) w + \frac { 1 } { 2 } z = 0
$$

has each of its two solutions in the closed unit disc and in the interior if they happen to coincide. The stability region for this method turns out to be the unshaded part of the complex plane shown in Figure 430(i), including the boundary.

Just as for Runge–Kutta methods, a consistent explicit linear multistep method has a bounded stability region and therefore cannot be A-stable. We therefore explore implicit methods as a source of appropriate algorithms for the solution of stiff problems. It will be found that A-stability is a very restrictive property in that it is incompatible with an order greater than 2. Also in this section, we consider a non-linear stability property, known as Gstability, which is a multistep counterpart of algebraic stability introduced in Chapter 3.

For a linear multistep method $[ \alpha , \beta ]$ , the difference equation associated with the linear test problem, $y ^ { \prime } = q y$ , is

$$
\begin{array} { r l r } {  { ( 1 - z \beta _ { 0 } ) y _ { n } - ( \alpha _ { 1 } + z \beta _ { 1 } ) y _ { n - 1 } - ( \alpha _ { 2 } + z \beta _ { 1 } ) y _ { n - 2 } - \cdots } } \\ & { } & { \qquad - ( \alpha _ { k } + z \beta _ { k } ) y _ { n - k } = 0 , } \end{array}
$$

and the stability region is the set of points $h q$ in the complex plane for which (431a) has only bounded solutions as $n \longrightarrow \infty$ . To simplify the discussion, we will consider the interior of the stability region so that, for $z$ in this set, all solutions to (431a) converge to zero as $n \longrightarrow \infty$ . We will refer to this interior set as the open stability region. Write the difference equation in the form

$$
\alpha ( E ^ { - 1 } ) - z \beta ( E ^ { - 1 } ) = 0 ,
$$

and we see that the open stability region can be defined in terms of the relation

$$
\alpha ( w ^ { - 1 } ) - z \beta ( w ^ { - 1 } ) = 0 .
$$

That is, $z$ is in the open stability region if there does not exist $w$ outside the open unit disc such that the pair $( z , w )$ satisfies (431b). Stated another way, this means that if $w$ outside the open unit disc this implies that $z$ satisfying (431b) is not in the open stability region.

As a starting point in determining the stability region, it is convenient to evaluate the points on the boundary of the unit circle and to note that the mapping

$$
w \mapsto { \frac { \alpha ( w ^ { - 1 } ) } { \beta ( w ^ { - 1 } ) } }
$$

traces out a set of points which includes the boundary of the stability region. In particular cases it is easy to determine the exact boundary. Since $w \mapsto w ^ { - 1 }$ maps the unit circle to itself, while changing the sense of rotation, it is equivalent to replace (431c) by

$$
w \mapsto { \frac { \alpha ( w ) } { \beta ( w ) } } .
$$

This procedure is known as the ‘boundary locus method’ for determining stability regions, and we give some examples of its use in the next subsection.

A second procedure for determining stability regions is based on the idea of the ‘type of a polynomial’. That is, if $P$ is a polynomial of degree $n$ then the type is a triple $( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ , where $n _ { 1 }$ , $n _ { 2 }$ and $n _ { 3 }$ are non-negative integers with sum exactly $n$ . The interpretation is that $n _ { 1 }$ is the number of zeros of $P$ in the open unit disc, $n _ { 2 }$ is the number of zeros on the unit circle and $n _ { 3 }$ is the number of zeros outside the closed unit disc. If we are willing to concentrate on the open stability region of a specific method, we can simplify the discussion to the question of determining whether or not the type of $P$ is $( n , 0 , 0 )$ . We will refer to such a polynomial as being ‘strongly stable’. Polynomials can be tested for this property recursively, using the following result:

Theorem 431A A polynomial $P _ { n }$ , given by

$$
P _ { n } ( w ) = a _ { 0 } w ^ { n } + a _ { 1 } w ^ { n - 1 } + \cdots + a _ { n - 1 } w + a _ { n } ,
$$

where $a _ { 0 } \neq 0$ and $n \geq 2$ , is strongly stable if and only if

$$
| a _ { 0 } | ^ { 2 } > | a _ { n } | ^ { 2 }
$$

and $P _ { n - 1 }$ is strongly stable, where

$$
\begin{array} { r l } & { P _ { n - 1 } ( w ) } \\ & { \quad = ( \overline { { a } } _ { 0 } a _ { 0 } - a _ { n } \overline { { a } } _ { n } ) w ^ { n - 1 } + ( \overline { { a } } _ { 0 } a _ { 1 } - a _ { n } \overline { { a } } _ { n - 1 } ) w ^ { n - 2 } + \cdot \cdot \cdot + ( \overline { { a } } _ { 0 } a _ { n - 1 } - a _ { n } \overline { { a } } _ { 1 } ) . } \end{array}
$$

Proof. First note that (431e) is necessary for strong stability because if it were not true, the product of the zeros could not have a magnitude less than 1. Hence, we assume that this is the case and it remains to prove that $P _ { n }$ is strongly stable if and only if the same property holds for $P _ { n - 1 }$ . It is easy to verify that

$$
w P _ { n - 1 } ( w ) = \overline { { { a } } } _ { 0 } P _ { n } ( w ) - a _ { n } w ^ { n } \overline { { { P _ { n } ( \overline { { { w } } } ^ { - 1 } ) } } } .
$$

By Rouch´e’s theorem, $w P _ { n - 1 } ( w )$ has $n$ zeros in the open unit disc if and only if the same property is true for $P _ { n } ( w )$ , and the result follows. $\boxed { \begin{array} { r l } \end{array} }$

The result of this theorem is often referred to as the Schur criterion. In the case of $n = 2$ , it leads to the two conditions

$$
\begin{array} { r l r } & { } & { | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } > 0 , } \\ & { } & { ( | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } ) ^ { 2 } - | \overline { { a } } _ { 0 } a _ { 1 } - a _ { 2 } \overline { { a } } _ { 1 } | ^ { 2 } > 0 . } \end{array}
$$

To apply the Schur criterion to the determination of the stability region for a $k$ -step method, we need to ask for which $z$ the polynomial given by

$$
P ( w ) = w ^ { k } ( \alpha ( w ^ { - 1 } ) - z \beta ( w ^ { - 1 } ) )
$$

is strongly stable. We present some examples of the use of this test in Subsection 433.

Algorithm $\mathbf { 4 3 2 } \alpha$ Boundary locus method for low order Adams–Bashforth methods   

<table><tr><td></td><td>% Second order</td></tr><tr><td>%</td><td></td></tr><tr><td></td><td>W = exp(i*linspace(O,2*pi));</td></tr><tr><td></td><td>Z = 2*W.*(w-1)./(3*w-1);</td></tr><tr><td>plot(z)</td><td></td></tr><tr><td></td><td>% Third order</td></tr><tr><td>%</td><td></td></tr><tr><td></td><td>W=exp(i*linspace(O,2*pi));</td></tr><tr><td>plot(z)</td><td>Z=12*(1-w)./(23*w-16*w.^2+5*w.^3);</td></tr><tr><td></td><td></td></tr><tr><td></td><td>% Fourth order</td></tr><tr><td>%</td><td>w=exp(i*linspace(O,2*pi));</td></tr><tr><td></td><td>Z=24*(1-w)./(55*w-59*w.^2+37*W.^3-9*W.^4);</td></tr><tr><td>plot(z)</td><td></td></tr></table>
