# 200 Introduction to the Euler methods

The famous method of Euler was published in his three-volume work Institutiones Calculi Integralis in the years 1768 to 1770, republished in his collected works (Euler, 1913). This fundamental idea is based on a very simple principle. Suppose that a particle is moving in such a way that, at time $x _ { 0 }$ , its position is equal to $y _ { 0 }$ and that, at this time, the velocity is known to be $v _ { 0 }$ . The simple principle is that, in a short period of time, so short that there has not been time for the velocity to change significantly from $v _ { 0 }$ , the change in position will be approximately equal to the change in time multiplied by $v _ { 0 }$ .

If the motion of the particle is governed by a differential equation, the value of $v _ { 0 }$ will be known as a function of $x _ { 0 }$ and $y _ { 0 }$ . Hence, given $x _ { 0 }$ and $y _ { 0 }$ , the solution at $x _ { 1 }$ , assumed to be close to $x _ { 0 }$ , can be calculated as

$$
y _ { 1 } = y _ { 0 } + ( x _ { 1 } - x _ { 0 } ) v _ { 0 } ,
$$

which can be found from known values only of $x _ { 0 }$ , $x _ { 1 }$ and $y _ { 0 }$ . Assuming that $v _ { 1 }$ , found using the differential equation from the values $x _ { 1 }$ and $y _ { 1 }$ , is sufficiently accurate, a second step can be taken to find $y _ { 2 }$ , an approximate solution at $x _ { 2 }$ , using the formula

$$
y _ { 2 } = y _ { 1 } + ( x _ { 2 } - x _ { 1 } ) v _ { 1 } .
$$

A sequence of approximations $y _ { 1 }$ , $y _ { 2 }$ , $y _ { 3 }$ , . . . to the solution of the differential equation at $x _ { 1 }$ , $x _ { 2 }$ , $x _ { 3 }$ , . . . is intended to lead eventually to acceptable approximations, at increasingly distant times from where the initial data was given.

Of course, the interpretation of the Euler method is much wider than in the description of the motion of a single particle, moving in time along a line. Even though the independent variable, which we denote by $x$ , will not always have the meaning of physical time, we will often refer to it as the ‘time variable’. The dependent variable $y$ need not have the meaning of distance and need not even be scalar. If $y$ is vector-valued, then it can be interpreted as a collection of scalar-valued components $y _ { 1 }$ , $y _ { 2 } , \ldots$ , $y _ { N }$ . Thus, we can write

$$
\begin{array} { r } { y ( x ) = \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { N } ( x ) } \end{array} \right] . } \end{array}
$$

The differential equation, and the initial information, which together determine the values of the $y$ components as the time variable varies, can be written in the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } .
$$

In the vector-valued case, the function $f$ is defined on $\mathbb { R } \times \mathbb { R } ^ { N }$ to $\mathbb { R } ^ { N }$ . However, it is often convenient to write the individual components of $f$ as scalar-valued functions of $x$ and the vector $y ( x )$ ; or, what is equivalent, of the individual components of $y ( x )$ . Similarly, the initial information can also be written in terms of individual components $y _ { 1 0 }$ , $y _ { 2 0 }$ , $\cdot \cdot \cdot$ , $y _ { N 0 }$ of $y _ { 0 }$ . There is a potential for confusion in the use of subscripts to denote either individual components of $y$ , or individual values of $x$ , at which $y$ is evaluated or approximated. This confusion will be avoided by using each notation only in a context which makes the meaning clear, or else, where it becomes necessary, by refining the notation.

With the freedom we have to write $y$ as a vector or as an ensemble of scalars, we see that (200a) can be written in one of several equivalent forms. We can write out the components of $y ( x )$ in $f ( x , y ( x ) )$ to emphasize the dependence of $y ^ { \prime } ( x )$ on each of these components:

$$
y ^ { \prime } ( x ) = f ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \ldots , y _ { N } ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

or we can take this a step further by writing out the individual components of $y ^ { \prime } ( x )$ :

$$
{ \left[ \begin{array} { l } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \\ { \vdots } \\ { y _ { N } ^ { \prime } ( x ) } \end{array} \right] } = f ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \ldots , y _ { N } ( x ) ) , \qquad y ( x _ { 0 } ) = { \left[ \begin{array} { l } { y _ { 1 0 } } \\ { y _ { 2 0 } } \\ { \vdots } \\ { y _ { N 0 } } \end{array} \right] } .
$$

Finally, we obtain a very detailed formulation by writing everything in terms of individual components:

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/9d041549e8ffb818f2fdca0ebe720318c79512fff55a7f8fe904e82eec4910d8.jpg)  
An example of the Euler method

$$
\begin{array} { r } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \\ { \vdots } \\ { y _ { N } ^ { \prime } ( x ) } \end{array} = \left[ \begin{array} { c } { f _ { 1 } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \\ { f _ { 2 } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \\ { \vdots } \\ { f _ { N } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \end{array} \right] , \left[ \begin{array} { c } { y _ { 1 } ( x _ { 0 } ) } \\ { y _ { 2 } ( x _ { 0 } ) } \\ { \vdots } \\ { y _ { N } ( x _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { c } { y _ { 1 0 } } \\ { y _ { 2 0 } } \\ { \vdots } \\ { y _ { N 0 } } \end{array} \right] .
$$

An important special case is that $f \mathrm { ~ - ~ } \mathrm { o r }$ , for vector problems, each of the functions $f _ { 1 }$ , $f _ { 2 }$ , . . . , $f _ { N } - \mathrm { d o e s }$ not depend on the time variable at all. In this case, we refer to the problem as being ‘autonomous’, and write it in the form

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

or in one of the expanded forms.

To conclude this subsection, we present a pictorial illustration of the use of the Euler method, for the scalar initial value problem

$$
\frac { d y } { d x } = \frac { y - 2 x y ^ { 2 } } { 1 + x } , \qquad y ( 0 ) = \frac { 2 } { 5 } .
$$

Five steps with the method, using equally sized time steps $\textstyle { \frac { 1 } { 5 } }$ , are taken and shown against a background of solutions with varying initial values. The general solution to this problem is given by

$$
y ( x ) = \frac { 1 + x } { C + x ^ { 2 } } ,
$$

for $C$ an arbitrary constant, and the exact and approximate solutions are shown in Figure 200(i).
