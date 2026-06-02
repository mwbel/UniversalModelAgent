# CHAPTER I CLASSICAL MATHEMATICAL THEORY

"... halte ich es immer fur besser, nicht mit dem Anfang anzufangen, der immer das Schwerste ist." (B.Riemann copied this from F.Schiller into his notebook)

This first chapter contains the classical theory of differential equations,which we judge useful and important for a profound understanding of numerical processes and phenomena. It will also be the occasion of presenting interesting examples of differential equations and their properties.

We first retrace in Sections I.2-I.6 the historical development of classical integration methods by series expansions, quadrature and elementary functions, from the beginning (Newton and Leibniz) to the era of Euler and Lagrange. The next part (Sections I.7-I.14) deals with theoretical properties of existence， uniqueness， stability， continuity and differentiability of the solutions. This theory was initiated by Cauchy in 1824 and then developed to perfection mainly during the next ioo years. We close with a brief account of boundary value problems, periodic solutions, limit cycles and strange attractors (Sections I.15 and I.16).

# 1.1. Terminology

A differential equation of the first order is an equation of the form

$$
y ^ { \prime } = f \left( x , y \right)
$$

with a given function $f \left( x , y \right)$ . A function $y \left( x \right)$ is called a solution of this equation if for all $x$ ，

$$
y ^ { \prime } ( x ) = f \left( x , y ( x ) \right) .
$$

It was observed very early by Newton, Leibniz and Euler that the solution usually contains a free parameter, so that it is only uniquely determined when an initial value

$$
y ( x _ { 0 } ) = y _ { 0 }
$$

is prescribed. Cauchy's existence and uniqueness proof of this fact will be discussed in Section I.7. Differential equations arise in many applications. We shall see in Section I.2 how the first equations arose

in mechanics, and in Section I.3 how some of them can be solved explicitly.

A differential equation of the second order for $y$ is of the form

$$
y ^ { \prime \prime } = f \left( x , y , y \right) .
$$

Here, the solution usually contains two parameters and is only uniquely determined by two initial values

$$
y \left( x _ { 0 } \right) = y _ { 0 } \ \cdot \ \cdot \qquad y ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } \ .
$$

Equations of the second order can rarely be solved explicitly (see I.3). For their numerical solution, as wel as for theoretical investigations, one usually sets $y _ { 1 } ( x ) { : = } y \left( x \right)$ ， $y _ { 2 } ( x ) { : = } y ^ { \prime } ( x )$ ， so that Equation (1.4) becomes

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = y _ { 2 } } & & { y _ { 1 } ( x _ { 0 } ) = y _ { 0 } } \\ & { y _ { 2 } ^ { \prime } = f \left( x , y _ { 1 } , y _ { 2 } \right) } & & { y _ { 2 } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } . } \end{array}
$$

This is an example of a first order system of differential equations， of dimension $_ { n }$ (see Sections I.6 and 1.9),

$$
y _ { 1 } ^ { \prime } = f _ { 1 } ( x , y _ { 1 } , . . . , y _ { n } ) \qquad y _ { 1 } ( x _ { 0 } ) = y _ { 1 0 }
$$

$$
y _ { n } ^ { \prime } = f _ { n } ( x , y _ { 1 } , . . . , y _ { n } ) \qquad y _ { n } ( x _ { 0 } ) = y _ { n 0 } .
$$

Most of the theory of this book is devoted to the solution of the initial value problem for the system (1.6). At the end of the 19th century (Peano (1890)） it became customary to introduce the vector notation

$$
y = \left( y _ { 1 } , , . . . , y _ { n } \right) ^ { T } , f = \left( f _ { 1 } , . . . , f _ { n } \right) ^ { T }
$$

so that (1.6) becomes $y \prime = f \left( x , y \right)$ , which is again the same as (1.1), but now with y and $f$ interpreted as vectors.

Another possibility for the second order equation (1.4), instead of transforming it into a system $( 1 . 4 ^ { \circ } )$ , is to develop methods specially adapted to second order equations (Nystrom methods). This will be done in special sections of this book. Nothing prevents us, of course, from considering (1.4) as a system of second order equations of dimension n.

If, however， the initial conditions (1.5) are replaced by something like $y \left( x _ { 0 } \right) { = } a$ ， $y \left( x _ { 1 } \right) = b$ ， i.e.， when the conditions deter-mining the particular solution are not all specified at the same point $x _ { 0 }$ , we speak of a boundary value problem. The theory of the existence of a solution and of its numerical computation is here much more complicated. We give some exam ples in Section I.15.

Finally, a problem of the type

$$
{ \frac { \partial u } { \partial t } } = f \left( t , u , { \frac { \partial u } { \partial x } } \ , \ { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } \right)
$$

for an unknown function $u \left( t , x \right)$ of two independent variables will be called a partial differential equation. We can also deal with partial differential equations of higher order, with problems in three or four independent variables, or with systems of partial differential equations. Very often, initial value problems for partial differential equations can conveniently be transformed into a system of ordinary differential equations, for example with finite difference or finite ele-ment approximations in the variable $x$ . In this way, the equation

$$
{ \frac { \partial u } { \partial t } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

would become

$$
\frac { d u _ { i } } { d t } = \frac { a ^ { 2 } } { { \Delta x } ^ { 2 } } ( u _ { i + 1 } { - 2 u _ { i } } { + u _ { i - 1 } } ) \ .
$$

This is called "Rothe's method" (Rothe (1930)), or the "method of lines". We shall see in Section I.6 that this connection is very com-mon since the work of Lagrange.

# I.2. The oldest differential equations

So zum Beispiel die Aufgabe der umgekehrten Tangentenmethode, von welcher auch Descartes eingestand, dass er sie nicht in seiner Gewalt habe. (Leibniz, 27. Aug 1676) ... et on sait que Ies seconds Inventeurs n'ont pas de droit a 'Invention. (Newton, 29 mai 1716) Il ne paroist point que M. Newton ait eu avant moy la characteristique & 'algorithme infinitesimal.. (Leibniz) And by these words he acknowledged that he had not yet found the reduction of problems to differential equations. (Newton)

# Newton

Differential equations are as old as differential calculus. Newton considered them in his treatise on differential calculus (Newton (1671)） and discussed their solution by integration and by series expansion. One of the first examples of a first order equation treated by Newton (see Newton (1671), Problema II, Solutio Casus II, Ex.I) was

$$
y ^ { \prime } = 1 - 3 x + y + x ^ { 2 } + x y .
$$

For each value $x$ and y， such an equation prescribes the derivative $y ^ { \prime }$ of the solutions. We thus obtain a vector field, which, for this particular equation, is sketched in Figure 2.1. (So, contrary to the belief of many people, vector fields existed long before Van Gogh). The solutions are the curves which respect these prescribed directions everywhere.

Newton discusses the solution of this equation by means of infinite series, whose terms he obtains recursively (" .. & ils se jettent sur les series, ou M. Newton m'a precede sans dificulte; mais, Leibniz). The first term

$$
y ~ = 0 + \cdot \cdot \cdot
$$

is the initial value for $x = 0$ . Inserting this into the differential equation (2.1) he obtains

$$
y ^ { \prime } = 1 + \cdots
$$

which, integrated, gives

Sit Equatio 1-3x+y+xx+xy,cujus Terminog:

r- 3x+xx non affectos Relatd Quantitate difpofitos vides in lateralem Seriem primo loco，& reliquos y & x y in finiftra Columnd.

$$
\begin{array} { r l } &  \begin{array} { r } { + \ldots } \\ { + \ s } \\ { \left\lfloor \frac { \textstyle + x } { \textstyle + x - x x + \frac { 1 } { 3 } x ^ { 3 } - \frac { \tau } { 6 } x ^ { 4 } + \frac { 1 } { 3 0 } x ^ { 3 } ; \ \& \& } { \textstyle \mathcal { E } \mathrm { c } } \end{array} \right\} } \\ &  \begin{array} { r } { \frac { \textstyle + x y } { \textstyle \frac { \textstyle + x + x x - x ^ { 3 } + x ^ { 5 } + \frac { \tau } { 3 } x ^ { 4 } - \frac { \tau } { 6 } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 6 } ; \ \& \mathcal { E } \mathrm { c } } { \textstyle \frac { \textstyle + x - x y } { \textstyle \frac { \textstyle + x + x y } { \textstyle \frac { \textstyle + x + x y } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle \delta } { \delta } } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 6 } } } } } } } } } } \\  \frac { \textstyle + x - x x + x x - x ^ { 3 } + \frac { \tau } { 3 } x ^ { 3 } + \frac { \tau } { 3 } x ^ { 4 } - \frac { \frac { \tau } { \textstyle + x } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 5 } ; \ \mathcal { E } \mathrm { c } . } } \\ { \eta = \left| + x - x x + \frac { 1 } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \delta } { \textstyle \delta } } x ^ { 9 } } } } } } + \frac { \tau } { 4 0 } x ^ { 5 } - \frac { \tau } { \textstyle \frac { \mathrm { 1 } } { \textstyle + x } } x ^ { 6 } ; \ \& \mathcal { E } \mathrm { c } . } \end{array}  } \end{array} } \end{\right|array}
$$

Nuno:

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/a72b7444f3b77ee5331509ab8a8fa2745168b0e14bb9b5e3f0e1cea0f2e9161a.jpg)  
Figure 2.1. a) Correct solution vs. approximate solution, b) vector field, c) various solution curves of Equation (2.1)

$$
y = x + \cdots .
$$

Again, from (2.1), we now have

$$
y ^ { \prime } = 1 - 3 x + x + \cdot \cdot \cdot = 1 - 2 x + \cdot \cdot \cdot
$$

and by integration

$$
y = x - x ^ { 2 } + \cdots ,
$$

The next round gives

$$
y ^ { \prime } = 1 - 2 x + x ^ { 2 } + \cdot \cdot \cdot , \qquad y = x - x ^ { 2 } + { \frac { x ^ { 3 } } { 3 } } + \cdot \cdot \cdot .
$$

Continuing this process, he finally arrives at

$$
y \ = x - x x + \frac { 1 } { 3 } x ^ { 3 } - \frac { 1 } { 6 } x ^ { 4 } + \frac { 1 } { 3 0 } x ^ { 5 } - \frac { 1 } { 4 5 } x ^ { 6 } \ , \ \& c \ .
$$

an approximation which, neglecting higher order terms, is plotted in Figure 2.1 together with the correct solution. It can be seen that the approximation is close only for small values of $x$ . For more examples see Exercises 11-13 of Section I.3.

# Leibniz

The second inventor of calculus, Leibniz, was led to differential equations around 1676 by the consideration of geometrical problems such as the inverse tangent problem (Leibniz (1693)): a curve $y \left( x \right)$ is required whose tangent AB is given, say everywhere of constant length $\alpha$ (Figure 2.2). This leads to

$$
y \prime = - \frac { y } { b } = - \frac { y } { \sqrt { a ^ { 2 } - y ^ { 2 } } } \ ,
$$

a first order diferential equation. Leibniz was inspired by a silver pocket watch ("horologio portatili suae thecae argentae") $B$ which is pulled on the table by a watch-chain $A B$ of length $^ a$ and he remarks proudly that none of the best scientists had been able to solve the problem before. It is interesting to note that Leibniz, in order to justify his differential equation (2.3) for the pocket-watch, imagined very small straight movements of the watch (Figure 2.3)， which can today be interpreted as Euler's method for the numerical solution of (2.3). The curious fact that differential equations were originally obtained just by the "inverse procedure" to "Euler polygons", has often occurred in history. A second example for this is the variational calculus.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/50dcf2fe60efc84d31e81303f0a9f6284fea030aac9b53efe3c2c89c1a82b30e.jpg)  
Figures 2.2 and 2.3. Illustrations from Leibniz and Kowalewski

# Variational Calculus

In 1696 Johann Bernouli invited the brightest mathematicians of the world ("Profundioris in primis Mathesos cultori, Salutem!") to solve the brachystochrone (shortest time) problem, mainly in order to fault his brother Jacob, from whom he expected a wrong solution. The problem istofinda curve $y \left( x \right)$ connecting two points $P _ { 0 } , P _ { 1 }$ such that a point gliding on this curve under gravitation reaches $P _ { \mathrm { ~ 1 ~ } }$ in the shortest time possible. In order to solve his problem, Joh. Bernoul (1697b) imagined thin layers of homogeneous media and knew from optics (Fermat’s principle) that a light ray with speed $\nu$ obeying the law of Snellius

$$
\mathrm { s i n } \alpha = K \nu
$$

passes through in the shortest time. Since the speed is known to be proportional to the square root of the falen height, he obtains, by passing to thinner and thinner layers,

$$
\sin \alpha = \frac { 1 } { \sqrt { 1 + { y ^ { \prime } } ^ { 2 } } } = K \sqrt { 2 g \left( y - h \right) } \ ,
$$

a differential equation of the first order.

The solutions of (2.4) can be shown to be cycloids (see Exercise 7 of Section I.3). Jacob, in his reply, aiso furnished a solution, much less elegant but unfortunately correct, and in turn invited his brother Johann to solve a couple of new problems. Jacob's method (see Figure 2.4) was something like today's (inverse) "finite element" method and led to the famous work of Euler (1744), which gives the general solution of the problem

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/a450bd88f3e294c2b0a3f69b31f925ebae19ba28a3e068460276017a42685ac1.jpg)  
Figure 2.4. Solutions of the variational problem (Joh. Bernoulli, Jac. Bermoul-,Euler)

$$
\begin{array} { l } { x _ { 1 } } \\ { \displaystyle \int f \left( x , y , y \right) d x \ = \mathrm { m i n } } \\ { x _ { 0 } } \end{array}
$$

with the help of the differential equation of the second order

$$
f _ { y ^ { \prime } y ^ { \prime } } y ^ { \prime \prime } + f _ { y ^ { \prime } y } y ^ { \prime } + f _ { y ^ { \prime } x } - f _ { y } = 0 ,
$$

and treated 100 variational problems in detail. Equation (2.5), in the special case where $f$ does not depend on $\bar { \bar { \mathbf { \Lambda } } }$ , can be integrated to give

$$
f - f _ { y ^ { \prime } } y ^ { \prime } = K .
$$

Euler's original proof used polygons in order to establish Equation (2.5). Only the ideas of Lagrange, in 1755 at the age of 19, led to the proof which is today the usual one (Funk (1962)， p.6-9, 16-19, Goldstine (1980),p.110). Euler (1756) then gave, in honour of Lagrange, the name "Variational calculus" to the whole subject ("..tamen gloria primae inventionis acutissimo Geometrae Taurinensi La Grange erat reservata").

# Clairaut

A class of equations with interesting properties was found by Clairaut (see Clairaut (1734), Probleme II). He was motivated by the movement of a rectangular wedge (see Figure 2.5), which led him to differential equations of the form

$$
y - x y \prime + f \left( y \prime \right) = 0 .
$$

This was the first implicit differential equation and possesses the particularity that not only the lines $y = C x - f \left( C \right)$ are solutions, but also their enveloping curves (see Exercise 10 of Section I.3). An example is shown in Figure 2.6 with $f \left( C \right) { = } 5 ( C ^ { 3 } { - } C ) / 2$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b286dcdd0eb41586d6c09bee731d0777877a3d1f951db79807f2180a3ed08a93.jpg)  
Figure 2.5. Ilustration from Clairaut (1734)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/5db3198e01da160141692d87fef94bc3ba883ab00e4d8ca4ac96bedf715b2902.jpg)  
Figure 2.6. Solutions of a Clairaut differential equation

Since the equation is of the third degree in $y ^ { \prime } { } _ { j }$ ,a given initial value may allow up to three different solution lines. Furthermore, where a line touches an enveloping curve, the solution may be continued either along the line or along the curve. There is thus a huge variety of different possible solution curves. Today we explain this curiosity by the fact that at these points no Lipschitz condition is satisfied (see also Ince (1944), p. 538-539).

# 1.3. Equations solvable by quadrature and elementary functions

We now discuss some of the simplest types of equations, which can be solved by the computation of integrals.

The equation with separable variables

$$
y ^ { \prime } = f \left( x \right) g \left( y \right) .
$$

Dividing by $g \left( y \right)$ and integrating we obtain the solution (Leibniz 1691, in a leter to Huygens)

$$
\begin{array} { r } { \int \frac { d y } { g \left( y \right) } = \int f \left( x \right) d x + C \ . } \end{array}
$$

A special example of this is the linear equation $y \ ^ { \prime } { = } f \left( x \right) y$ ，which possesses the solution

$$
\begin{array} { r } { y \left( x \right) = C R \left( x \right) , \qquad R \left( x \right) = \exp ( \int f \left( x \right) d x ) . } \end{array}
$$

The inhomogeneous linear equation

$$
y ^ { \prime } = f \left( x \right) y + g \left( x \right) ,
$$

Here, the substitution $y \left( x \right) = c \left( x \right) R \left( x \right)$ leads to $c \ ^ { \prime } ( x \ ) { = } g \left( x \right) / R \ \left( x \right)$ (Joh. Bernoulli (1697)). One thus obtains the solution

$$
y \left( x \right) = R \left( x \right) \left( \intop _ { x _ { 0 } } ^ { x } \frac { g \left( s \right) } { R \left( s \right) } d s + C \right) .
$$

# Total differential equations

An equation of the form

$$
P \left( x , y \right) + Q \left( x , y \right) y ^ { \prime } = 0
$$

is found to be im mediately solvable if

$$
\frac { \partial P } { \partial y } = \frac { \partial Q } { \partial x } .
$$

One can then find by integration a function $F \left( x , y \right)$ such that

$$
\frac { \partial F } { \partial x } = P , \frac { \partial F } { \partial y } = Q .
$$

Therefore (3.4) becomes $\frac { d } { d x } F \left( x \ , \ y \left( x \right) \right) = 0$ ，with the solutions expressed by $F \left( x \ , \ y \left( x \ \right) \right) { = } C$ . For the case when (3.5) is not satisfied, Clairaut and Euler investigated the multiplication of (3.4) by a suitablefactor $M \left( x , y \right)$ ，which sometimes allowsthe equation $M P + M Q y ^ { \prime } { = } 0$ to satisfy (3.5).

# Second order equations

Even more than for first order equations, the solution of second order equations by integration is very seldom possible. Besides linear equations with constant coefficients, whose solutions for the second order case were already known to Newton, several tricks of reduction are possible, as for example the following:

For a linear equation

$$
y \prime \prime = a ( x ) y \prime + b ( x ) y
$$

we make the substitution

$$
\begin{array} { r } { y \ = \exp ( \int p \left( \boldsymbol { x } \right) d \boldsymbol { x } ) \ . } \end{array}
$$

The derivatives of this function contain only derivatives of $p$ of lower order

$$
\begin{array} { r } { y ^ { \prime } = p \exp ( \int p \left( x \right) d x ) , \qquad y ^ { \prime \prime } = [ p ^ { 2 } + p ^ { \prime } ] \exp ( \int p \left( x \right) d x ) } \end{array}
$$

so that the insertion of this into the differential equation,after division by y, leads to a lower order equation

$$
p ^ { 2 } + p ^ { \prime } = a ( x ) p + b ( x )
$$

which, however, is nonlinear (Riccati (1723), Euler (1728)).

If the equation is independent of $y \ , \ y \ ^ { \prime \prime } { = } f \left( x \ , \ y \ \right)$ , it is natural to put $y ^ { \prime } { = } \nu$ which gives $\scriptstyle \nu ^ { \prime } = f \ ( x \ , \ \nu )$

An important case is that of equations independent of x :

$$
y \prime \prime = f \left( y , y \right) .
$$

Here we consider $y ^ { \prime }$ as function of y ${ \mathrm { : ~ } } y ^ { \prime } { = } p \left( y \right)$ . Then the chain rule gives $y \ ^ { \prime \prime } { = } p \ ^ { \prime } p { = } f \ ( y \ , \ p )$ ，which is a first order equation. When the function $p ( y )$ has been found, it remains to integrate $y ^ { \prime } { = } p \left( y \right)$ ,which is an equation of type (3.1) (Riccati (1712): 'Per liberare la premessa formula dalle seconde differenze.., chiamo $p$ la sunnormale BF..", see also Euler (1769), Problema 96, p.33).

The investigation of all possible differential equations which can be integrated by analytical methods was begun by Euler. His results have been collected, in more than 800 pages, in Volumes XXIl and

XXII of Euler's Opera Omnia. For a more recent discussion see Ince (1944)，p.16-61. An irreplaceable document on this subject is the book of Kamke (1942). It contains, besides a description of the solu-tion methods and general properties of the solutions, a systematically ordered list of more than 15oo differential equations with their solu-tions and references to the literature.

The computations, even for very sim ple looking equations, soon become very complicated and one quickly began to understand that elementary solutions would not always be possible. It was Liouville (1841) who gave the first proof of the fact that certain equations, such as $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ ,cannot be solved in terms of elementary functions. Therefore, in the 19th century mathematicians became more and more interested in general existence theorems and in numerical methods for the computation of the solutions.

# Exercises

1. Compute with Newton's method further solutions of (2.1), e.g. satisfying y $( 0 ) { = } 0 . 1$ ， $y \left( 0 \right) { = } 0 . 2$ ， $y \left( 0 \right) { = } 0 . 3$ , and draw them.

2. Solve Newton's equation (2.1) by quadrature.

3. Solve Leibniz' equation (2.3) in terms of elementary functions. Hint: The integral for y might cause trouble. Use the substitution $a ^ { 2 } - y ^ { 2 } = u ^ { 2 }$ ， $- y d y = u d u$

4. Solve and draw the solutions of $y ^ { \prime } { = } f \left( y \right)$ where

$$
f \left( y \right) = { \sqrt { \left| y \right| } } .
$$

5. Solve the master-and-dog problem: a dog runs with speed $w$ in the direction of his master, who walks with speed $\nu$ along the y -axis. This leads to the diferential equation

$$
x y ^ { \prime \prime } = { \frac { \nu } { w } } \left( 1 + { y ^ { \prime } } ^ { 2 } \right) ^ { 1 / 2 } .
$$

6. Solve the equation $m y \ ^ { \prime \prime } { = } { - } k / y ^ { 2 }$ ， which describes a body falling according to Newton's law of gravitation.

7. Verify that the cycloid

$$
x - x _ { 0 } = R \left( \tau - \sin \tau \right) , \quad y - h = R \left( 1 - \cos \tau \right) , \quad R = \frac { 1 } { 4 g K ^ { 2 } } 
$$

satisfies the differential equation (2.4) for the brachystochrone problem. Solving (2.4) in a forward manner， one arrives after some sim plifications at the integral

$$
\int { \left( \frac { y } { 1 - y } \right) } ^ { 1 / 2 } d y ,
$$

which is com puted by the substitution $y = ( \sin t ) ^ { 2 }$

8. Show that the differential equation

$$
x + y y ^ { \prime } = y ^ { \prime } { \sqrt { x ^ { 2 } + y ^ { 2 } - 1 } }
$$

possesses the solutions $2 a y = a ^ { 2 } + 1 - x ^ { 2 }$ for all $^ { a }$ . Sketch these curves and find yet another solution of the equation (from Lagrange (1774)， p.7, which was written to explain the "Clairaut phenomenon").

9. Reduce the "Bernoulli equation” (Jac. Bernoulli (1695)) $y ^ { \prime } + f \left( x \right) y = g \left( x \right) y ^ { n }$ , with the help of the coordinate transformation $z ( x ) = ( y ( x ) ) ^ { q }$ and a suitable choice of $q$ ， to a linear equation (Leibniz, Acta Erud. 1696, p.145, Joh. Bernouli (1697)).

10.Verify that the envelope of the solutions $y = C x - f \left( C \right)$ of the Clairaut equation (2.7) is given in parametric representation by

$$
\begin{array} { l } { { x \left( p \right) = f ^ { \prime } \left( p \right) } } \\ { { y \left( p \right) = p f ^ { \prime } \left( p \right) - f \left( p \right) . } } \end{array}
$$

Show that this envelope is also a solution of (2.7) and calculate it for $f \left( C \right) { = } 5 { \left( C ^ { 3 } { - } C \right) } / 2$ (cf. Figure 2.6).

11.(Newton (1671)， "Problema II, Solutio particulare"). Solve the total differential equation

$$
3 x ^ { 2 } - 2 a x + a y - 3 y ^ { 2 } y ^ { \prime } + a x y ^ { \prime } = 0 .
$$

Solution given by Newton: $x ^ { 3 } - a x ^ { 2 } + a x y - y ^ { 3 } = 0$ . Observe that he missed the arbitrary integration constant $C$

12.(Newton (1671)). Solve the equations

$$
\begin{array} { r l } & { \mathrm { a ) } y ^ { \prime } = 1 + \displaystyle \frac { y } { a } + \frac { x y } { a ^ { 2 } } + \frac { x ^ { 2 } y } { a ^ { 3 } } + \frac { x ^ { 3 } y } { a ^ { 4 } } \mathrm { , ~ } \& c . } \\ & { \mathrm { b ) } y ^ { \prime } = - 3 x + 3 x y + y ^ { 2 } - x y ^ { 2 } + y ^ { 3 } - x y ^ { 3 } + y ^ { 4 } - x y ^ { 4 } + 6 x ^ { 2 } y } \\ & { \qquad - 6 x ^ { 2 } + 8 x ^ { 3 } y - 8 x ^ { 3 } + 1 0 x ^ { 4 } y - 1 0 x ^ { 4 } \mathrm { , ~ } \& c . } \end{array}
$$

Results given by Newton:

$$
\begin{array} { r l } { { \mathrm { a ) } } } & { { y = x + \displaystyle \frac { x ^ { 2 } } { 2 a } + \frac { x ^ { 3 } } { 2 a ^ { 2 } } + \frac { x ^ { 4 } } { 2 a ^ { 3 } } + \frac { x ^ { 5 } } { 2 a ^ { 4 } } + \frac { x ^ { 6 } } { 2 a ^ { 5 } } \ , \ \& c . } } \\ { { \mathrm { b ) } } } & { { y = \displaystyle - \frac { 3 } { 2 } x ^ { 2 } - 2 x ^ { 3 } - \frac { 2 5 } { 8 } x ^ { 4 } - \frac { 9 1 } { 2 0 } x ^ { 5 } - \frac { 1 1 1 } { 1 6 } x ^ { 6 } - \frac { 3 6 7 } { 3 5 } x ^ { 7 } \ , \ \& c . } } \end{array}
$$

13.(Newton). Solve Equation (2.1) with another initial value $y \left( 0 \right) = 1$ Newton's result: $y = 1 + 2 x + x ^ { 3 } + \frac { 1 } { 4 } x ^ { 4 } + \frac { 1 } { 4 } x ^ { 5 }$ ，&c.

14.(Cauchy (1824)). Show that the family $y = C \ ( x + C ) ^ { 2 }$ satisfies the differential equation $( y \prime ) ^ { 3 } { = } 8 y ^ { 2 } { - } 4 x y y \prime$ .Find yet another solution which is not included in this family (see Figure 3.1). Answer: $y = - { \frac { 4 } { 2 7 } } x ^ { 3 }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/44bfe2b0b36590637941fea1b10ad402c2756ab28b4a3d976a35032a8a33e875.jpg)  
Figure 3.1. Solution family of Cauchy's example in Exercise 14

# I.4 Linear differential equations

Lisez Euler, lisez Euler, c'est notre maftre a tous (Laplace)

Following in the footprints of Euler (1743), we want to understand the general solution of $n$ -th order linear differential equations. We say that the equation

$$
L \left( y \right) : = a _ { 0 } ( x ) y ^ { \left( n \right) } + a _ { 1 } ( x ) y ^ { \left( n - 1 \right) } + \cdot \cdot \cdot + a _ { n } ( x ) y = 0
$$

with given functions $a _ { 0 } ( x ) , \dots , a _ { n } ( x )$ is homogeneous. If $_ \pi$ solutions ${ \boldsymbol { \mathfrak { u } } } _ { 1 } ( { \boldsymbol { x } } ) \ , \ \cdot \ \cdot \ , { \boldsymbol { \mathfrak { u } } } _ { n } ( { \boldsymbol { x } } )$ of (4.1) are known, then any linear combination

$$
y ( x ) = C _ { 1 } u _ { 1 } ( x ) + \cdot \cdot \cdot + C _ { n } u _ { n } ( x )
$$

with constant coeficients $c _ { 1 } , \ldots , c _ { n }$ is also a solution of (4.1). This is due to the fact that all derivatives of y appear only linearly in (4.1).

# Equations with constant coefficients

Let us first consider the special case

$$
y ^ { ( n ) } ( x ) = 0 ~ .
$$

This can be integrated once to give $y ^ { ( n - 1 ) } ( x ) { = } C _ { 1 }$ ，then $y ^ { ( n - 2 ) } ( x ) { = } C _ { 1 } x + C _ { 2 } ;$ etc.Replacing at theend the arbitrary constants $C _ { i }$ by new ones, we finally obtain

$$
y \left( x \right) = C _ { 1 } x ^ { n - 1 } + C _ { 2 } x ^ { n - 2 } + \cdot \cdot \cdot + C _ { n } .
$$

Thus there are n "free parameters" in the "general solution" of (4.3). Euler's intuition, after some more examples, also expected the same result for the general equation (4.1). This fact, however, only became completely clear many years later.

We now treat the general equation with constant coefficients,

$$
y ^ { ( n ) } + { A _ { 1 } } y ^ { ( n - 1 ) } + \cdot \cdot \cdot + { A _ { n } } y \ = 0 .
$$

Our problem is to find a basis of $n$ linearly independent solutions $u _ { 1 } ( x ) , \ldots , u _ { n } ( x )$ . To this end, Euler's inspiration was guided by the transformation (3.6),(3.7) above: if $a \left( x \right)$ and $b \left( x \right)$ are constants, we assume $p$ constant in (3.7) so that $p ^ { \prime }$ vanishes, and we obtain the quadratic equation $p ^ { 2 } { = } a p + b$ For any root of this equation, (3.6) then becomes $y = e ^ { p x }$ . In the general case we thus assume $y = e ^ { p x }$ with an unknown constant $\boldsymbol { p }$ , so that (4.4) leads to the characteristic equation

$$
p ^ { n } + { \cal A } _ { 1 } p ^ { n - 1 } + \cdots + { \cal A } _ { n } = 0 .
$$

If the roots $\rho _ { 1 } , . . . , p _ { n }$ of Equation (4.5) are distinct, all solutions of (4.4) are given by

$$
y \left( x \right) = C _ { 1 } e ^ { p _ { 1 } x } + \cdot \cdot \cdot + C _ { n } e ^ { p _ { n } x } \ .
$$

It is curious to see that the "brightest mathematicians of the world" struggled for many decades to find this solution，which appears so trivial to today's students.

A difficulty arises with the solution (4.6) when (4.5) does not possess $n$ distinct roots. Consider, with Euler, the example

$$
y ^ { \prime \prime } - 2 q y ^ { \prime } + q ^ { 2 } y = 0 \ .
$$

Here $p = q$ is a double root of the corresponding characteristic equation. If we set

$$
y \ = e ^ { q x } u ,
$$

(4.7) becomes $\scriptstyle { u } ^ { \prime \prime } = 0$ , which brings us back to (4.3). So the general solution of (4.7) is given by $y \left( x \right) = e ^ { 4 x } \left( C _ { 1 } x + C _ { 2 } \right)$ (see also Exercise 5 below). After some more examples of this type, one sees that the transformation (4.8) effects a shift of the characteristic polynomial, so minating with that if $q$ is a root of multiplicity $\dots + B u ^ { ( k + 1 ) } + C u ^ { ( k ) } = 0$ $k$ ， we obtain for u an equation ter- Therefore

$$
e ^ { q x } ( C _ { 1 } x ^ { k - 1 } + \cdot \cdot \cdot + C _ { k } )
$$

gives us $k$ independent solutions.

Finally， for a pair of complex roots $p = \alpha \pm i \beta$ the solutions $e ^ { ( \alpha + i \beta ) x } , \stackrel { \cdot } { e } ^ { ( \alpha - i \beta ) x }$ can be replaced by the real functions

$$
e ^ { \mathrm { \normalfont ~ a x } } ( C _ { 1 } { \cos } \beta x + C _ { 2 } { \sin } \beta x ) \ .
$$

The study of the inhomogeneous equation

$$
L \left( y \right) = f \left( x \right)
$$

was begun in Euler (1750), p.13. We mention from this work the case where $f \left( x \right)$ is a polynomial, say for example the equation

$$
A y \ ^ { \prime \prime } + B y \ ^ { \prime } + C y \ = a x ^ { 2 } + b x \ + c .
$$

Here Euler puts $y \left( x \right) = E x ^ { 2 } + F x + G + \nu \left( x \right)$ . Inserting this into (4.10) and eliminating all possible powcrs of $\mathcal { \kappa }$ , one obtains

$$
\begin{array} { c } { { C E \ = \ a , ~ C F + 2 B E \ = b , ~ C G \ + B F + 2 A E \ = c , } } \\ { { { } } } \\ { { A \nu ^ { \prime \prime } + B \nu ^ { \prime } + C \nu \ = 0 , } } \end{array}
$$

This allows us, when $c$ is different from zero, to compute $E , F$ and $G$ and we observe that the general solution of the inhomogeneous equation is the sum of a particular solution of it and of the general solution of the corresponding homogeneous equation. This is also true in the general case and can be verified by trivial linear algebra.

The above method of searching for a particular solution with the help of unknown coefficients also works similarly if $f \left( x \right)$ is com posed of exponential, sine, or cosine functions and is often called the "fast method". We see with pleasure that it was historically the first method to be discovered.

# Variation of constants

The general treatment of the inhomogeneous equation

$$
a _ { 0 } ( x ) y ^ { ( n ) } + \cdot \cdot \cdot + a _ { n } ( x ) y = f \left( x \right)
$$

is due to Lagrange (1775) (".. par une nouvelle methode aussi simple qu'on puisse le desirer.", see also Lagrange (1788), seconde partie, Sec.V.) We assume known n independent solutions ${ \mathfrak { u } } _ { 1 } ( x ) , \ldots , { \mathfrak { u } } _ { n } ( x )$ of the homogeneous equation. We then set, in extension of the method employed for (3.2), instead of (4.2)

$$
y ( x ) = c _ { 1 } ( x ) u _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } ( x ) u _ { n } ( x )
$$

with unknown functions $c _ { i } ( x )$ ("method of variation of constants"). We have to insert (4.12) into (4.11) and thus compute the first derivative

$$
y ^ { \prime } = \sum _ { i } c _ { i } ^ { \prime } u _ { i } + \sum _ { i } c _ { i } \boldsymbol { u } _ { i } ^ { \prime } \ .
$$

If we continue blindly to differentiate in this way, we soon obtain complicated and useless formulas. Therefore Lagrange astutely requires the first term to vanish and puts

$$
\sum _ { i } c _ { i } ^ { \prime } \boldsymbol { \mathsf { u } } _ { i } ^ { \phantom { \dagger } } = 0 \qquad \quad j = 0 , \mathrm { t h e n } \quad j = 1 , \ldots , n - 2 .
$$

Then repeated differentiation of $y$ ， with continued elimination of the undesired terms (4.13), gives

$$
\begin{array} { c } { { y ^ { \prime } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { \prime } \ , \quad \cdots \quad , \ y ^ { ( n - 1 ) } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } ( n - 1 ) } \ , } } \\ { { \phantom { x ^ { \prime } = } y ^ { ( n ) } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { ( n - 1 ) } + \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { ( n ) } \ . } } \end{array}
$$

If we insert this into (4.11)， we observe wonderful cancellations due to the fact that the $u _ { i } ( x )$ satisfy the homogeneous equation, and finally obtain, together with (4.13),

$$
\left( \begin{array} { c c c } { { u _ { 1 } } } & { { \cdots } } & { { u _ { n } } } \\ { { u _ { 1 } ^ { \prime } } } & { { \cdots } } & { { u _ { n } ^ { \prime } } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { u _ { 1 } ^ { \left( n - 1 \right) } } } & { { \cdots } } & { { u _ { n } ^ { \left( n - 1 \right) } } } \end{array} \right) \left( \begin{array} { c } { { c _ { 1 } ^ { \prime } } } \\ { { c _ { 2 } ^ { \prime } } } \\ { { \vdots } } \\ { { c _ { n } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { c } { { 0 } } \\ { { \vdots } } \\ { { 0 } } \\ { { f \left( x \right) / a _ { 0 } ( x ) } } \end{array} \right) .
$$

This is a linear system, whose determinant is called the "Wronskian" and whose solution yields $c _ { 1 } ^ { \prime } ( x ) , \ldots , c _ { n } ^ { \prime } ( x )$ and after integration, $c _ { 1 } ( x ) , \ldots , c _ { n } ( x ) .$

Much more insight into this formula will be possible in Section I.11.

# Exercises

1. Find the solution "huius aequationis differentialis quarti gradus" $a ^ { 4 } y ^ { ( 4 ) } + y = 0 , ~ a ^ { 4 } y ^ { ( 4 ) } - y = 0$ ;solve the equation "septimi gradus" $y ^ { ( 7 ) } + y ^ { ( 5 ) } + y ^ { ( 4 ) } + \bar { y } ^ { ( 3 ) } + \bar { y } ^ { ( 2 ) } + y = 0$ (Euler (1743),Ex.4,5,6).

2. Solve by Euler's method j $\prime \prime - 3 y \prime - 4 y = \cos x$ ， $y \ ^ { \prime \prime } { + } y = \cos x$

Hint: in the first case the particular solution can be searched for in the form E cosx $+ F$ sinx . This, however, does not work in the second case because of resonance. Here one puts $E x \cos x + F x$ sinx just as in the solution of (4.7).

3. Find the solution of

$$
y ^ { \prime \prime } - 3 y ^ { \prime } - 4 y \ = g \left( x \right) \ , \quad g \left( x \right) = \left\{ \begin{array} { l l } { \cos ( x ) } & { 0 \leq x \leq \frac { \pi } { 2 } } \\ { } & { } \\ { 0 } & { \frac { \pi } { 2 } \leq x \ . } \end{array} \right.
$$

such that $y \left( 0 \right) { = } y ^ { \prime } ( 0 ) { = } 0$

a) by using the solution of Exercise 2, b) by the method of Lagrange (variation of constants).

4. (Reduction of the order if one solution is known). Suppose that a nonzero solution $\boldsymbol { \mathfrak { u } } _ { 1 } ( \boldsymbol { x } )$ of

$$
y ^ { \prime \prime } + a _ { 1 } ( x ) y ^ { \prime } + a _ { 2 } ( x ) y ~ = 0
$$

is known. Show that a second independent solution can be found by putting ${ } ^ { u } { } _ { 2 } ( x ) { = } c ( x ) u _ { 1 } ( x ) .$

5. Treat the case of multiple characteristic values (4.7) by consider-ing them as a limiting case $P _ { 2 } {  } \ : P _ { 1 }$ and using the solutions

$$
u _ { 1 } ( x ) = e ^ { p _ { 1 } x } \ , u _ { 2 } ( x ) = \operatorname * { l i m } _ { p _ { 2 }  p _ { 1 } } { \frac { e ^ { p _ { 2 } x } - e ^ { p _ { 1 } x } } { p _ { 2 } - p _ { 1 } } } = { \frac { \partial e ^ { p _ { 1 } x } } { \partial p _ { 1 } } } \ , { \mathrm { e t c . } }
$$

(d'Alembert-(1748), p.284: "Enfin, si les valeurs de $p$ & de $p ^ { \prime }$ sont egales， au lieu de les supposer telles, on supposera $p = a + \alpha$ ， $p ^ { \prime } { = } a - { \alpha }$ , α etant quantite infiniment petite...").

# I.5. Equations with weak singularities

Many equations occuring in applications possess singularities， i.e., points at which the function $f \left( x , y \right)$ of the differential equation becomes infinite. We study in some detail the classical treatment of such equations, since numerical methods, which will be discussed later in this book, often fail at the singular point and work badly in its close neighbourhood.

As a first example, consider the equation

$$
y ^ { \prime } = \frac { q + b x } { x } y , q \neq 0
$$

with a singularity at $x = 0$ . Its solution, using the method of separation of variables (3.1), is

$$
y \left( x \right) = C x ^ { q } e ^ { b x } = C \left( x ^ { q } + b x ^ { q + 1 } + \cdots \right) .
$$

These solutions are plotted in Figure 5.1 for different values of $q$ and show the fundamental difference in the behaviour of the solutions in dependence of $q$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/3408b9c0d6315586992a1f29b6f0f1ef848289b2d4b2ce8a71d63cb26f5650bc.jpg)  
Figure 5.1. Solutions of (5.1) for $b = 1 , q = 3 / 2 , q = 1 / 2 , q = - 1 / 2$

# Linear equations

Euler started a systematic study of equations with singularities. He asked which type of equation of the second order can be conveniently solved by a series as in (5.2) (Euler (1769), Problema 122, p.177,". quas commode per series resolvere licet $\therefore \prime )$ . He found the equation

$$
x ^ { 2 } ( a + b x ) y ^ { n } + x ( c + e x ) y ^ { \prime } + ( f + g x ) y ~ = 0 ~ .
$$

Let us put

$$
y ~ = ~ \sum _ { i = 0 } ^ { \infty } A _ { i } x ^ { q + i } ~ , ~ A _ { ~ 0 } \neq 0
$$

and insert this, similarly to Newton's procedure (2.2), into (5.3). We thereby observe' that the powers $x ^ { 2 }$ and $x$ which are multiplied by $y ^ { \prime \prime }$ and $y ^ { \prime }$ ， respectively， just re-establish what has been lost by the differentiations and obtain

$$
\begin{array} { c c } { { q ( q - 1 ) a + q c + f } } & { { = 0 } } & { { ( 5 . 5 ) } } \\ { { { } } } & { { { } } } \\ { { { [ ( q + i ) ( q + i - 1 ) a + ( q + i ) c + f ] A _ { i } } } } & { { ( 5 . 5 ) } } \\ { { { } } } & { { { } } } \\ { { { } } } & { { = - [ ( q + i - 1 ) ( q + i - 2 ) b + ( q + i - 1 ) e + g ] A _ { i - 1 } } } \end{array}
$$

for $i = 1 , 2 , 3 , \cdots$ . Equation (5.5a) is called the index equation and determines, for $^ a$ different from zero, two characteristic roots - in decreasing order - $q _ { 1 }$ and $q _ { 2 }$ . For each of these, with $\boldsymbol { A } _ { \textup { 0 } }$ arbitrary, (5.5b) then allows the recursive computation of $A _ { 1 } , A _ { 2 }$ ,etc. For the radius of convergence of the series obtained see Exercise 8 below. We thus obtain two linearly independent solutions $u _ { 1 } ( x ) , u _ { 2 } ( x )$ of the differential equation, just what we require (see I.4). There is, however, a case in which the second solution causes trouble, namely when the coefficient of $A _ { i }$ in (5.5b) becomes zero for some i, i.e., when ${ q _ { 1 } - q _ { 2 } }$ is an integer ("Problema 123"). In this case, on the inspiration of some acrobatic heuristics (Euler (1769), p.150: " quod $x ^ { 0 } / 0$ aequivaleat ipsi logx.")， Euler has the idea of searching for the second solution with the help of

$$
u _ { 2 } ( x ) = u _ { 1 } ( x ) \log x + \sum _ { i = 0 } ^ { \infty } { A _ { i } } ^ { ( 2 ) } x ^ { q _ { 2 } + i } \ ,
$$

The insertion of this into (5.3) then allows him to compute the coefficients ${ A _ { i } } ^ { ( 2 ) }$ An example for this case is given in Exercise 1.

Later, Euler (1778) remarked that the recursion formula (5.5b) becomes particularly elegant, if one starts from the differential equation

$$
x \left( 1 - x \right) y ^ { \prime \prime } + \left( c - ( a + b + 1 ) x \right) y ^ { \prime } - a b y \ = 0
$$

instead of from (5.3). Here, the above method leads to

$$
\begin{array} { r c l } { { q \left( q - 1 \right) + c q = 0 \ , \quad } } & { { q _ { 1 } = 0 \ , \quad } } & { { q _ { 2 } = 1 - c \ , } } \\ { { } } & { { } } & { { } } \\ { { A _ { i + 1 } = \frac { \left( a + i \right) \left( b + i \right) } { \left( c + i \right) \left( 1 + i \right) } A _ { i } \quad } } & { { \mathrm { f o r } q _ { 1 } = 0 \ . } } \end{array}
$$

The resulting solutions, later named hypergeometric functions, became particularly famous throughout the 19th century with the work of Gauss (1812).

More generally， the above method works in the case of a differential equation

$$
x ^ { 2 } y ^ { \prime \prime } + x a ( x ) y ^ { \prime } + b ( x ) y = 0 \quad \quad
$$

where $a \left( x \right)$ and $b ( x )$ are regular analytic functions. One then says that O is a regular or weak singular point. Similarly, we say that the equation $( x - x _ { 0 } ) ^ { 2 } y \prime \prime + ( x - x _ { 0 } ) a ( x ) y \prime + b ( x ) y = 0$ possesses the regular singular point $\varepsilon _ { \mathrm { ~ 0 ~ } }$ . In this case solutions can be obtained by the use of algebraic singularities $( x - x _ { 0 } ) ^ { q }$

Finally, we also want to study the behaviour at infinity for an equation of the form

$$
a ( x ) y ^ { \prime \prime } + b ( x ) y ^ { \prime } + c ( x ) y ~ = 0 ~ .
$$

For this, we use the coordinate transformation $t = 1 / x$ ， $z \left( t \right) { \stackrel { } { = } } y \left( x \right)$ which yields

$$
t ^ { 4 } a \left( \frac { 1 } { t } \right) z ^ { \prime \prime } + \left( 2 t ^ { 3 } a \left( \frac { 1 } { t } \right) - t ^ { 2 } b \left( \frac { 1 } { t } \right) \right) z ^ { \prime } + c \left( \frac { 1 } { t } \right) z \ = 0 \ .
$$

$\infty$ is called a regular singular point of (5.10a) if O is a regular singular point of (5.10b). For examples see Exercise 9.

# Nonlinear Equations

"Der Mathematiker weiss sich ohnedies beim Auftreten von singularen Stellen gegebenenfalls leicht zu helfen."

(K. Heun, 1900)

The above method sometimes allows one to obtain, also for nonlinear equations, if not the complete series of the solution, at least a couple of terms.

EXEMPLUM: let us see what happens if we try to solve the classical brachystochrone problem (2.4) by a series solution. We suppose $h = 0$ and the initial value $y \left( 0 \right) { = } 0$ . We write the equation as

$$
{ y ^ { \prime } } ^ { 2 } = { \frac { L } { y } } - 1 \qquad \mathrm { o r } \qquad { y y ^ { \prime } } ^ { 2 } + y = L \quad .
$$

At the initial point $y \left( 0 \right) = 0 , y ^ { \prime }$ becomes infinite and most numerical methods would fail. We search for a solution of the form $\begin{array} { r } { y = \boldsymbol { A } _ { \mathrm { \scriptsize ~ 0 } } x ^ { q } . } \end{array}$ This gives in (5.11) $q ^ { 2 } A \ _ { 0 } ^ { 3 } x ^ { 3 q - 2 } { + } A \ _ { 0 } x ^ { q } = L$ . Due to the initial value we have that $y \left( x \right)$ becomes negligible for small values of $x$ . We thus set the first term equal to $L$ and obtain $3 q - 2 = 0$ and $q ^ { 2 } A \begin{array} { l } { { 3 } } \\ { { 0 } } \end{array} = L$ .So

$$
u \left( x \right) = \left( \frac { 9 L x ^ { 2 } } { 4 } \right) ^ { 1 / 3 }
$$

is a first approximate solution. The idea is now to use (5.12) just to escape from the initial point with a small $x$ , and then to continue the solution with any numerical step-by-step procedure from the later chapters.

A more refined approximation could be tried in the form $y = \boldsymbol { A } _ { 0 } x ^ { q } + \boldsymbol { A } _ { 1 } x ^ { q + r } .$ This gives with (5.11)

$$
q ^ { 2 } A _ { 0 } ^ { ~ 3 } x ^ { 3 q - 2 } + q ( 3 q + 2 r ) A _ { 0 } ^ { ~ 2 } A _ { 1 } x ^ { 3 q + r - 2 } + A _ { 0 } x ^ { q } + \cdot \cdot \cdot = L ~ .
$$

We use the second term to neutralize the third one, which gives $3 q + r - 2 = q$ or $r = q = 2 / 3$ and $5 q ^ { 2 } A _ { 0 } A _ { 1 } = - 1 .$ Therefore

$$
\nu \left( x \right) = \left( \frac { 9 L x ^ { 2 } } { 4 } \right) ^ { 1 / 3 } - \left( \frac { 9 ^ { 2 } x ^ { 4 } } { 4 ^ { 2 } L \ : \varsigma ^ { 3 } } \right) ^ { 1 / 3 }
$$

is a better approximation. The following numerical results illustrate the utility of the approximations (5.12) and (5.13) compared with the correct solution $y \left( x \right)$ from I.3, Exercise 7, with $L = 2$ ：

$x = 0 . 1 0$ y(x)=0.342839 $u \left( x \right) = 0 . 3 5 5 6 8 9$ $\scriptstyle \nu ( x ) = 0 . 3 4 3 0 3 8$   
$x = 0 . 0 1$ y(x)=0.076042 $u \left( x \right) = 0 . 0 7 6 6 3 1$ $\scriptstyle \nu ( x ) = 0 . 0 7 6 0 4 4$

# Exercises

1. Compute the general solution of the equation $x ^ { 2 } y ~ ^ { \prime \prime } { + } x y ~ ^ { \prime } { + } g x ^ { \prime \prime } y = 0$ with $g$ constant (Euler (1769), Problema 123, Exem plum 1).

2. Apply the  method of Euler to the Bessel equation $x ^ { 2 } y ^ { \prime \prime } + x y ~ ^ { \prime } + ( x ^ { 2 } - g ^ { 2 } ) y = 0$ Sketch the solutions obtained for $g = 2 / 3$ and $g = 1 0 / 3$

3. Compute the solutions of the equations $x ^ { 2 } y ~ ^ { \prime \prime } { - } 2 x y ~ ^ { \prime } { + } y { = } 0$ ， $x ^ { 2 } y ~ ^ { \prime \prime } { - } 3 x y ~ ^ { \prime } { + } 4 y = 0$ Equations of this type are often called Euler's or even Cauchy's equation. Its solution， however, was already known to Joh. Bernoulli.

4. (Euler (1769), Probl.123, Exempl. 2). Let

$$
y \left( x \right) = \int _ { 0 } ^ { 2 \pi } \left( \sin ^ { 2 } { s } + x ^ { 2 } \cos ^ { 2 } { s } \right) ^ { 1 / 2 } d s
$$

be the perimeter of the ellipse with axes 1 and $x < 1$

a) Verify that $y \left( x \right)$ satisfies the differential equation

$$
x ( 1 { - } x ^ { 2 } ) y ^ { \prime \prime } - ( 1 { + } x ^ { 2 } ) y ^ { \prime } + x y = 0 .
$$

b) Compute the solutions of this equation.

c) Show that the coordinate change $x ^ { 2 } = t$ ， $y \left( x \right) = z \left( t \right)$ transforms (5.14) to a hypergeometric equation (5.7).

Hint. The computations for a) lead to the integral

$$
\begin{array} { l } { { \displaystyle { \int _ { 0 } ^ { 2 \pi } \frac { 1 - 2 \cos ^ { 2 } s + q ^ { 2 } \cos ^ { 4 } s } { \left( 1 - q ^ { 2 } \cos ^ { 2 } s \right) ^ { 3 / 2 } } d s } } , } \end{array} \qquad q ^ { 2 } = 1 - x ^ { 2 }
$$

which must be shown to be zero. Develop this into a power series in $q ^ { 2 }$

5. Try to solve the equation

$$
x ^ { 2 } y ^ { \prime \prime } + ( 3 x - 1 ) y ^ { \prime } + y \ = 0
$$

with the help of a series (5.4) and study its convergence.

6. Find a series of the type

$$
y = A _ { 0 } x ^ { q } + A _ { 1 } x ^ { q + s } + A _ { 2 } x ^ { q + 2 s } + \cdot \cdot \cdot
$$

which solves the nonlinear "Emden-Fowler equation" of astrophysics $( x ^ { 2 } y \ ) ^ { \prime } + y ^ { 2 } x ^ { - 1 / 2 } { = } 0$ in the neighbourhood of $x = 0$

7. Approximate the solution of Leibniz's equation (2.3) in the neigh-bourhood of the singular initial value $y \left( 0 \right) = a$ by a function of the type $y \left( x \right) { = } a - C x ^ { q }$ . Compare the result with the correct solution of Exercise 3 of I.3.

8. Show that the radius of convergence of series (5.4) is given by

$$
\mathrm { i } ) \quad r = | \frac { a } { b } | \qquad \mathrm { i i } ) \quad r = 1
$$

for the coefficients given by (5.5) and (5.9), respectively.

9. Show that the point $\infty$ is a regular singular point for the hyper-geometric equation (5.7), but not for the Bessel equation of Exercise 2.

10. Consider the initial value problem

$$
y ^ { \prime } = \frac { \lambda } { x } y + g ( x ) , \qquad y ( 0 ) = 0 .
$$

a) Prove that for $\lambda \le 0$ the problem (5.15) possesses a unique soiution for $x \ge 0$

b) If $g \left( x \right)$ is $k$ -times differentiable and $\lambda \le 0$ ， then the solution $y \left( x \right)$ is $( k + 1 )$ )-times differentiable for $x \geq 0$ and we have

$$
y ^ { ( j ) } ( 0 ) = \left( 1 { - } \frac { \lambda } { j } \right) ^ { - 1 } g ^ { ( j - 1 ) } ( 0 ) ~ , ~ j = 1 , 2 , \cdots ~ .
$$

# 1.6. Systems of equations

# Lagrange

The first systems of equations appear in the work of Lagrange (1759). One of the earliest interests of Lagrange was the propagation of sound. Starting from the insuficiency of Newton's approach, he attempted to explain the propagation of sound from known resuits in elasticity. Thus, if we suppose the medium to be a sequence of mass points and denote by $y _ { 1 } ( t ) , y _ { 2 } ( t ) , y _ { 3 } ( t ) , . .$ their displacements from the equilibrium positions (Figure 6.1), we have from Hooke's law of elasticity

$$
\begin{array} { l } { y _ { 1 } ^ { \prime \prime } = K ^ { 2 } ( - 2 y _ { 1 } + y _ { 2 } ) } \\ { y _ { 2 } ^ { \prime \prime } = K ^ { 2 } ( y _ { 1 } - 2 y _ { 2 } + y _ { 3 } ) } \\ { \cdot \cdot \cdot } \\ { y _ { n } ^ { \prime \prime } = K ^ { 2 } ( y _ { n - 1 } - 2 y _ { n } ) \enspace . } \end{array}
$$

This is a system of $n$ linear differential equations. Throughout this section we shall use $t$ for the independent variable (time), in order to avoid confusion with the space variable $x$ of the corresponding partial differential equation. Lagrange observed that the same equations appear, when d'Alembert's (1748) equation

$$
{ \frac { \partial ^ { 2 } u } { { \partial t } ^ { 2 } } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

for the vibrating string (cordis vibrantibus) is modeled by a finite number of mass points attched to a string without mass (Figure 6.1).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/5d54ac7890a580b787d196d00aa2724f0b7898e59548713d86538ff3338945f1.jpg)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b44d563dd69cfee7955c02c5c4a08a7b888784918cf41c6aa7fadc4bc097cb88.jpg)  
Figure 6.1. Model for sound propagation, vibrating and hanging string

Another example treated by Lagrange ((1762)， Nr. 36), was that of mass points attached to a hanging string (Figure 6.1). Here the tension in the string becomes greater in the upper part of the string and we have the following equations of movement

$$
\begin{array} { l } { y _ { 1 } ^ { \prime \prime } = K ^ { 2 } ( - y _ { 1 } + y _ { 2 } ) } \\ { y _ { 2 } ^ { \prime \prime } = K ^ { 2 } ( y _ { 1 } - 3 y _ { 2 } + 2 y _ { 3 } ) } \\ { y _ { 3 } ^ { \prime \prime } = K ^ { 2 } ( 2 y _ { 2 } - 5 y _ { 3 } + 3 y _ { 4 } ) } \end{array}
$$

$$
y _ { n } ^ { \prime \prime } = K ^ { 2 } ( ( n - 1 ) y _ { n - 1 } - ( 2 n - 1 ) y _ { n } ) ,
$$

In all these examples, of course, the deviations $y _ { i }$ are supposed to be "infinitely" small, so that linear models are realistic.

Using a notation which came into use only a century later, we write these equations in the form

$$
y _ { i } ^ { \prime \prime } = \sum _ { j = 1 } ^ { n } \alpha _ { i j } y _ { j } \qquad ( i = 1 , \ldots , n ) \ ,
$$

which represents a system of 2nd order linear equations with constant coefficients.Lagrange solves System (6.3) by puting $\boldsymbol { y } _ { i } ^ { \phantom { } } = \boldsymbol { c } _ { i } ^ { \phantom { } } e ^ { p \boldsymbol { \tau } }$ ，which leads to

$$
{ p ^ { 2 } c _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } c _ { j } } \qquad ( i = 1 , \dots , n )
$$

so that $p ^ { 2 }$ must be an eigenvalue of the matrix A and $\boldsymbol { c } = ( c _ { 1 } , . . . , c _ { n } ) ^ { T }$ the corresponding eigenvector. We see here the first appearance of an eigenvalue problem and also the first use of the "method of lines" for the wave equation.

Lagrange ((1762), Nr.30) then explains that the equations (6.4) are solved by computing $c _ { 2 } / c _ { 1 } , \ldots , c _ { n } / c _ { 1 }$ as functions of $p$ from $n - 1$ equations and by inserting these results into the last one. This leads to a polynomial of degree n (in fact, the characteristic polynomial) to rodth for $p ^ { 2 }$ aWoutusi2tins $y _ { i } ^ { ( j ) } { = } c _ { i } ^ { ( j ) } \mathrm { e x p } ( { \pm } p _ { j } \varepsilon )$ of these.

A complication arises when the characteristic polynomial possesses multiple roots. In this case, Lagrange (in his famous Mecanique Analytique, Lagrange (1788)， seconde partie, sect.VI, No.7) affirms the presence of "secular" terms similar to the formulas following (4.8). This， however, is not completely true, as became clear only a century later (see e.g. Weierstrass (1858), p.243: ". um bei dieser Gelegenheit einen Irrtum zu berichtigen, der sich in der Lagrange'schen Theorie der kleinen Schwingungen, sowie in allen spateren mir bekannten Darstellungen derselben, findet."). We therefore postpone this subject to Section I.12.

We close this section by solving Equations (6.1) in detail, since the results obtained are of particular importance (Lagrange (1759)). The corresponding eigenvalue problem (6.4) becomes in this case $p ^ { 2 } c _ { 1 } { = } K ^ { 2 } ( - \dot { 2 } c _ { 1 } { + } c _ { 2 } )$ ， ${ p ^ { 2 } c _ { i } = } K ^ { 2 } ( c _ { i - 1 } { - 2 } c _ { i } { + } c _ { i + 1 } )$ for $i = 2 , \ldots , n - 1$ and $p ^ { 2 } c _ { n } = K ^ { 2 } ( c _ { n - 1 } - 2 \bar { c } _ { n } )$ We introduce $p ^ { 2 } / K ^ { 2 } + 2 = q$ ,so that

$$
c _ { j + 1 } - q c _ { j } + c _ { j - 1 } = 0 ~ , ~ c _ { 0 } = 0 ~ , ~ c _ { n + 1 } = 0 ~ .
$$

This means that the $c _ { i }$ are the solutions of a difference equation and therefore $\scriptstyle c _ { j } = A a ^ { j } + B b ^ { j }$ where a and $^ b$ are the roots of the corresponding characteristic equation $z ^ { 2 } - q z + 1 = 0$ , hence

$$
a + b = q , a b = 1 ,
$$

The condition ${ c _ { 0 } } \mathrm { { = } } 0$ of (6.5),which means $A + B = 0$ ，shows that $c _ { j } ^ { } = a _ { } ( a ^ { j } - b ^ { j } )$ with $A \neq 0$ Thesecondcondition $c _ { n + 1 } = 0$ ,or equivalently $( a / b ) ^ { n + 1 } = 1$ , implies together with $a b = 1$ that

$$
a \ = \ \exp \left( { \frac { k \pi i } { n + 1 } } \right) \ , \qquad b \ = \ \exp \left( { \frac { - k \pi i } { n + 1 } } \right)
$$

for some $k = 1 , \ldots , n .$ Thus we obtain

$$
\begin{array} { l } { { q _ { k } ~ = 2 \cos \displaystyle \frac { \pi k } { n + 1 } ~ , \quad k = 1 \ldots , n ~ , } } \\ { { \displaystyle p _ { k } ^ { 2 } = 2 { \bf K } ^ { 2 } \biggl ( \cos \displaystyle \frac { \pi k } { n + 1 } - 1 \biggr ) = - 4 { \bf K } ^ { 2 } \biggl ( \sin \displaystyle \frac { \pi k } { 2 n + 2 } \biggr ) ^ { 2 } ~ . } } \end{array}
$$

Finally, Euler's formula from 1740, $e ^ { i x } - e ^ { - i x } = 2 i \sin x$ (".. si familiere aujourd'hui aux Geometres") gives for the eigenvectors (with $A = - i / 2$ ）

$$
\begin{array} { r } { c _ { j } ^ { \mathbf { \Upsilon } ( k ) } = \sin \frac { j k \pi } { n + 1 } , \qquad j , k = 1 , \ldots , n . } \end{array}
$$

Since the $p _ { k }$ are purely imaginary, we also use for $\mathrm { e x p } ( \pm p _ { k } t )$ the "familiere" formula and obtain finally the general solution

$$
y _ { j } ( t ) = \sum _ { k = 1 } ^ { n } \sin { \frac { j k \pi } { n + 1 } } ( a _ { k } \cos r _ { k } t + b _ { k } \sin r _ { k } t ) , \quad r _ { k } = 2 K \sin { \frac { \pi k } { 2 n + 2 } } .
$$

Lagrange then observed after some lengthy calculations， which are today seen by using the orthogonality relations

$$
\sum _ { l = 1 } ^ { n } \sin { \frac { l j \pi } { n + 1 } } \sin { \frac { l k \pi } { n + 1 } } = \left\{ \begin{array} { l l } { { 0 } } & { { j \neq k } } \\ { { \displaystyle { \frac { n + 1 } { 2 } } } } & { { j = k } } \end{array} \right. \quad \quad j , k = 1 , \ldots , n
$$

that

$$
\begin{array} { l } { { a _ { k } = \displaystyle \frac { 2 } { n + 1 } \sum _ { j = 1 } ^ { n } \sin \displaystyle \frac { k j \pi } { n + 1 } y _ { j } ( 0 ) ~ , } } \\ { { b _ { k } = \displaystyle \frac { 1 } { r _ { k } } \displaystyle \frac { 2 } { n + 1 } \sum _ { j = 1 } ^ { n } \sin \displaystyle \frac { k j \pi } { n + 1 } y _ { j } ^ { \prime } ( 0 ) } } \end{array}
$$

are determined by the initial positions and velocities of the mass points. He also studied the case where $n$ , the number of mass points, tends to infinity (so that, in the formula for $r _ { k }$ ， sinx can be replaced by $x$ ) and stood, 50 years before Fourier, at the portal of Fourier series theory. "Mit welcher Gewandtheit, mit welchem Aufwande analytischer Kunstgriffe er auch den ersten Theil dieser Untersuchung durchfuhrte, so liess der Uebergang vom Endlichen zum Unendlichen doch viel zu wuinschen iubrig..."(Riem ann (1854)).

# Fourier

J'ajouterai que le livre de Fourier a une importance capitale dans I'histoire des mathematiques. (H. Poincare, 1893)

The first first order systems were motivated by the problem of heat conduction (Biot 1804, Fourier (1807)). Fourier imagined a rod to be a sequence of molecules, whose temperatures we denote by $y _ { i }$ , and deduced from a law of Newton that the energy which a particle passes to its neighbours is proportional to the difference of their temperatures, i.e., ${ \boldsymbol { y } } _ { i - 1 } - { \boldsymbol { y } } _ { i }$ to the left and ${ \boldsymbol { y } } _ { i + 1 } - { \boldsymbol { y } } _ { i }$ to the right ("Lorsque deux molecules d'un méme solide sont extremement voisines et ont des temperatures inégales, la molecule plus echauffee comm unique a celle qui 'est moins une quantite de chaleur exactement exprimee par le produit formé de la duree de l'instant, de la difference extremement petite des temperatures, et d'une certaine fonction de la distance des molecules"). This long sentence means, in formulas, that the total gain of energy of the $i - t h$ molecule is expressed by

$$
y _ { i } ^ { \prime } = K ^ { 2 } ( y _ { i - 1 } - 2 y _ { i } + y _ { i + 1 } ) ~ , ~ 
$$

or, in general

$$
y _ { i } ^ { \prime } = \sum _ { j = 1 } ^ { n } a _ { i j } y _ { i } \qquad i = 1 , \ldots , n .
$$

a first order system with constant coefficients.

By putting $y _ { i } { = } c _ { i } e ^ { p \tau }$ , we now obtain the eigenvalue problem

$$
p c _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } c _ { j } \qquad i = 1 , \dots , n \ .
$$

If we suppose tke rod cooled to zero at both ends $\left( y _ { 0 } \mathrm { = } y _ { n + 1 } \mathrm { = } 0 \right)$ ,we can use Lagrange eigenvectors from above and obtain the solution

$$
y _ { j } ( t ) = \sum _ { k = 1 } ^ { n } \sin { \frac { j k \pi } { n + 1 } } a _ { k } \exp ( - w _ { k } t ) ~ , ~ w _ { k } = 4 K ^ { 2 } \biggl ( \sin { \frac { \pi k } { 2 n + 2 } } \biggr ) ^ { 2 } ~ .
$$

By taking n larger and larger, Fourier arrived from (6.10) (hence: by the inverse "method of lines") at his famous heat equation

$$
{ \frac { \partial u } { \partial t } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

which was the origin of Fourier series theory.

# Exercises

1. Verify that, if $u \left( x \right)$ is sufficiently differentiable,

$$
{ \frac { u ( x - 8 ) - 2 u ( x ) + u ( x + 8 ) } { 8 ^ { 2 } } } = u ^ { \prime \prime } ( x ) + { \frac { 8 ^ { 2 } u ^ { ( 4 ) } ( x ) } { 1 2 } } + { \bf O } ( 8 ^ { 4 } ) .
$$

Hint: use Taylor series expansion for $u \left( x + 8 \right)$ and $u \left( x - 8 \right)$ . This relation establishes the connection between (6.10) and (6.14) as well as between (6.1) and the wave equation.

2. Solve Equation (6.2) for $n = 2$ and $n = 3$ by using the device of Lagrange described above (1762) and discovering naturally the characteristic polynomial of the matrix .

3. Solve the first order system (6.11) with initial values $y _ { i } ( 0 ) = ( - 1 ) ^ { i }$ ， where the matrix A is the same as in Exercise 2 and draw the solutions. Physically, this equation would represent a string with weights hanging, say, in honey.

4. Find the first terms of the development at the singular point $x = 0$ of the following system of nonlinear equations

$$
{ \begin{array} { r l } { x ^ { 2 } y ^ { \prime \prime } + 2 x y ^ { \prime } = 2 y z ^ { 2 } + { \mathsf { A } } x ^ { 2 } y ( y ^ { 2 } - 1 ) } & { \qquad y ( 0 ) { \ = } 0 } \\ { x ^ { 2 } z ^ { \prime \prime } = z ( z ^ { 2 } { - } 1 ) + x ^ { 2 } y ^ { 2 } z } & { \qquad z ( 0 ) { = } 1 } \end{array} }
$$

where 入 is a constant parameter. Equations (6.15) are the Euler equations for the variational problem

$$
I = \int _ { \stackrel { \{ } 0 \} { \displaystyle 0 } } ^ { \infty } \left( { z ^ { \prime } } ^ { 2 } + \frac { { x ^ { 2 } } { y ^ { \prime } } ^ { 2 } } { 2 } + \frac { ( z ^ { 2 } - 1 ) ^ { 2 } } { 2 x ^ { 2 } } + { y ^ { 2 } } { z ^ { 2 } } + \frac { \lambda } { 4 } { x ^ { 2 } } ( { y ^ { 2 } } - 1 ) ^ { 2 } \right) d x ,
$$

$$
y \left( \infty \right) = 1 , z \left( \infty \right) = 0
$$

which gives the mass of a "monopole" in nuclear physics (see 't Hooft (1974)).

# I.7. A general existence theorem

We now enter a new era for our subject, more theoretical than the preceding one. It was inaugurated by the work of Cauchy, who was not as fascinated by long numerical calculations as was， say, Euler, but merely a fanatic for perfect mathem atical rigour and exact-ness. He criticized in the work of his predecessors the use of infinite series and other infinite processes without taking much account of error estimates or convergence results. He therefore established around 1820 a convergence theorem for the polygon method of Euler and, some 15 years later, for the power series method of Newton (see Section I.8). Beyond the estimation of errors, these results also allow the statement of general existence theorems for the solutions of arbitrary differential equations ("d'une equation différentielle quelconque")，whose solutions were only known before in a very few cases. A second important consequence is to provide results about the uniqueness of the solution, which allow one to conclude that the computed solution (numerically or analytically) is the only one with the same initial value and that there are no others. Only then we are allowed to speak of the solution of the problem.

His very first proof has recently been discovered on fragmentary notes (Cauchy (1824)), which were never published in Cauchy's lifetime (did his notes not satisfy the Minister of education?: ".. mais que le second professeur, M. Cauchy, n'a présente que des feuilles qui n'ont pu satisfaire la commission, et qu’il a éte jusqu'a present impossible de l'amener a se rendre au voeu du Conseil et a exécuter la decision du Ministre").

# Convergence of Euler's method

Let us now, with bared head and trembling knees, follow the ideas of this historical proof. We formulate it in a way which generalizes directly to higher dimensional systems.

Starting with the one-dimensional differential equation

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y \left( X \right) = ?
$$

we make use of the method explained by Euler (1768) in the last section of his "Institutiones Calculi Integralis" (Caput VII, p.424), i.e. we consider a subdivision of the interval of integration

$$
x _ { 0 } , x _ { 1 } , \ldots , x _ { n - 1 } , x _ { n } = X
$$

and replace in each subinterval the solution by the first term of its Taylor series

$$
\begin{array} { r } { y _ { 1 } - y _ { 0 } = ( x _ { 1 } - x _ { 0 } ) f ( x _ { 0 } , y _ { 0 } ) } \\ { y _ { 2 } - y _ { 1 } = ( x _ { 2 } - x _ { 1 } ) f ( x _ { 1 } , y _ { 1 } ) } \end{array}
$$

$$
y _ { n } - y _ { n - 1 } = ( x _ { n } - x _ { n - 1 } ) f \left( x _ { n - 1 } , y _ { n - 1 } \right) .
$$

For the subdivision above we also use the notation

$$
\textit { h } = ( h _ { 0 } , h _ { 1 } , \ldots , h _ { n - 1 } )
$$

where $n _ { i } = x _ { i + 1 } - x _ { i }$ . If we connect $y _ { 0 }$ and $y _ { 1 } , y _ { 1 }$ and $y _ { 2 } , \ldots$ etc by straight lines we obtain the Euler polygon

$$
y _ { h } ( x ) = y _ { i } + ( x - x _ { i } ) f ( x _ { i } , y _ { i } ) ~ \mathrm { f o r } ~ x _ { i } { \le } x { \le } x _ { i + 1 } ~ .
$$

Lemma 7.1. A ssume that $\mid f \mid$ is bounded by A on

$$
D \ = \Big \{ ( x , y ) | x _ { 0 } { \le } x { \le } X , | y { - } y _ { 0 } | { \le } b \Big \} \ .
$$

1f $X ^ { - x } _ { 0 } { \le } { b } / A$ then the numerical solution $( x _ { i } , y _ { i } )$ given by (7.3), remains in $D$ for every subdivision (7.2) and we have

$$
| \ y _ { h } ( x ) - y _ { 0 } | \ \leq \ A \cdot | x - x _ { 0 } | ,
$$

$$
\mid y _ { h } ( x ) - ( y _ { 0 } + ( x - x _ { 0 } ) f ( x _ { 0 } , y _ { 0 } ) ) \mid \le \mathtt { e } \cdot \mid x - x _ { 0 } \mid
$$

$$
\begin{array} { r } { i f \left( x , y \right) - f \left( x _ { 0 } , y _ { 0 } \right) \mid \ \leq \ \epsilon \quad o n \ D . } \end{array}
$$

Proof: Both inequalities are obtained by adding up the lines of (7.3) and using the triangle inequality. (7.4) then shows immediately that for A $( x - x _ { 0 } ) \le b$ the polygon remains in $D$ . QED.

Our next problem is to obtain an estimate for the change of $y _ { h } ( x )$ ， when the initial value $y _ { 0 }$ is changed: let $ { { ^ z _ { 0 } } }$ be another initial value and compute

$$
z _ { 1 } - z _ { 0 } = ( x _ { 1 } { - } x _ { 0 } ) f ( x _ { 0 } , z _ { 0 } ) .
$$

We need an estim ate for $\left| z _ { 1 } - y _ { 1 } \right| .$ Subtracting (7.6) from the first line of (7.3) we obtain

$$
z _ { 1 } - y _ { 1 } = z _ { 0 } - y _ { 0 } + ( x _ { 1 } - x _ { 0 } ) \bigg ( f \left( x _ { 0 } , z _ { 0 } \right) - f \left( x _ { 0 } , y _ { 0 } \right) \bigg ) \ .
$$

This shows that we need an estimate for $f \left( x _ { 0 } , z _ { 0 } \right) - f \left( x _ { 0 } , y _ { 0 } \right)$ If we suppose

$$
\mid f \left( x , z \right) - f \left( x , y \right) \mid \ \leq \ L \ \vert z - y \mid
$$

we obtain

$$
\left| z _ { 1 } - y _ { 1 } \right| \ \leq \ ( 1 + ( x _ { 1 } - x _ { 0 } ) L \ ) \left| z _ { 0 } - y _ { 0 } \right| \ .
$$

Lemma 7.2. For a fixed subdivision h let $y _ { h } ( x )$ and $z _ { h } ( x )$ be the Euler potygons corresponding to the initial values $y _ { \mathrm { ~ 0 ~ } } a n d \textit { z } _ { \mathrm { ~ 0 ~ } }$ , respectivety. 1f

$$
\begin{array} { r } { \displaystyle \mid \frac { \partial f } { \partial y } ( x , y ) \mid \le L } \end{array}
$$

in a convex region which contains $( x \ , y _ { h } ( x ) )$ and $( x \ , \ z _ { h } ( x ) )$ for au $x _ { 0 } \leq x \leq X$ ,then

$$
\mid z _ { h } \left( x \right) - y _ { h } \left( x \right) \mid \ \le \ e ^ { L \left( x - x _ { 0 } \right) } \vert z _ { 0 } - y _ { 0 } \vert .
$$

Proof: (7.9) implies (7.7), (7.7) implies (7.8), (7.8) implies (Matth.1.2)

$$
\left| z _ { 1 } - y _ { 1 } \right| \ \leq \ e ^ { L \left( x _ { 1 } - x _ { 0 } \right) } | z _ { 0 } - y _ { 0 } | .
$$

If we repeat the same argument for $z _ { 2 } - y _ { 2 } , \ z _ { 3 } - y _ { 3 }$ ，and so on, we finally obtain (7.10). QED.

Remark: Condition (7.7) is called a "Lipschitz condition". It was Lipschitz (1876) who rediscovered the theory (footnote in the paper of Lipschitz: "L'auteur ne connait pas évidemment les travaux de Cauchy.") and advocated the use of (7.7) instead of the more stringent hypothesis (7.9). Lipschitz's proof is also explained in the classical work of Picard (1891-96), Vol.II, Chap.XI, Sec.I.

If the subdivision (7.2) is refined more and more, so that

$$
\vert h \vert : = \operatorname* { m a x } _ { i = 0 , . . , n - 1 } h _ { i } \to 0 ,
$$

we expect that the Euler polygons converge to a solution of (7.1). Indeed, we have

Theorem 7.3. Let $f \left( x , y \right)$ be continuous, and $\mid f \mid$ be bounded by A and satisfy the Lipschitz condition (7.7) on

$$
\textit { D } = \left\{ ( x , y ) \ : | \ : x \ : _ { 0 } { \le } x { \le } X \ : , \ : | y { - } y \ : _ { 0 } | { \le } b \right\} .
$$

$I f X - x _ { 0 } { \leq } b / A$ , then we have:

a)For $| h   \mathrm { ~ 0 ~ }$ the Euler polygons $y _ { h } \left( x \right)$ converge uniformly to a continu-ous function $\Phi ( x )$   
b） $\Phi ( x )$ is continuously differentiable and is a solution of (7.1） on $x _ { 0 } { \le } x \le X$ ，   
c) There exists no other solution of (7.1) on xo≤ x ≤X .

Proof: a) Take an $\epsilon > 0$ . Since $f$ is uniformly continuous on the compact set $D$ , there exists a $\delta > 0$ such that

$$
| { u } _ { 1 } - { u } _ { 2 } | \ \leq \ 8 \qquad \mathrm { a n d } \qquad | { \nu } _ { 1 } - { \nu } _ { 2 } | \ \leq \ A \ \ 8
$$

imply

$$
\mid f ( u _ { 1 } , \nu _ { 1 } ) - f ( u _ { 2 } , \nu _ { 2 } ) \mid \leq \epsilon .
$$

Suppose now that the subdivision (7.3) satisfies

$$
| x _ { i + 1 } - x _ { i } | \ \leq \ 8 , \mathrm { i . e . } | h | \ \leq \ 8 .
$$

We first study the effect of adding new mesh-points. In a first step, we consider a subdivision $h \left( 1 \right)$ ，which is obtained by adding new points only to the frst subinterval. It follows from (7.5) (applied to this first subinterval) that for the new refined solution $y _ { h ( 1 ) } ( x _ { 1 } )$ we have the estimate $| y _ { h ( 1 ) } ( x _ { 1 } ) - y _ { h } ( x _ { 1 } ) | \leq \epsilon | x _ { 1 } - x _ { 0 } |$ Since the subdivisions $h$ and $h \left( 1 \right)$ are identical on $x _ { 1 } \leq x \leq X$ we can apply Lem ma 7.2 to obtain

$$
\mid y _ { h ( 1 ) } ( x ) - y _ { h } ( x ) \mid \leq e ^ { L ( x - x _ { 1 } ) } ( x _ { 1 } - x _ { 0 } ) \in ~ \mathrm { f o r } ~ x _ { 1 } \leq x \leq X .
$$

We next add further points to the subinterval $( x _ { 1 } , x _ { 2 } )$ and denote the new subdivision by $h \left( 2 \right)$ . In the same way as above this leads to

$$
\mid y _ { h ( 2 ) } ( x _ { 2 } ) - y _ { h ( 1 ) } ( x _ { 2 } ) \mid \le \mathtt { e } \mid x _ { 2 } - x _ { 1 } \mid
$$

and

$$
\mid y _ { h ( 2 ) } ( x ) - y _ { h ( 1 ) } ( x ) \mid \le e ^ { L ( x - x _ { 2 } ) } ( x _ { 2 } { - } x _ { 1 } ) \epsilon ~ \mathrm { f o r } ~ x _ { 2 } \le x \le X .
$$

The entire situation is sketched in Figure 7.1. If we denote by $\hat { h }$ the final refinement, we obtain for xi< x ≤xi +1

$$
\begin{array} { r l r } {  { \mid y _ { \hat { h } } ( x ) - y _ { h } ( x ) \mid } } \\ & { \le } & { \epsilon ( e ^ { L ( x - x _ { 1 } ) } ( x _ { 1 } { - } x _ { 0 } ) + \cdot \cdot \cdot + e ^ { L ( x - x _ { i } ) } ( x _ { i } { - } x _ { i - 1 } ) ) + \epsilon ( x - x _ { i } ) } \\ & { \le } & { \epsilon \int e ^ { L ( x - s ) } d s = \frac { \epsilon } { L } ( e ^ { L ( x - x _ { 0 } ) } - 1 ) ~ . } \\ & { } & { x _ { 0 } } \end{array}
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/9098fbb71cbed06160f8a4db6ea02f7ebb1590a9d0a62f16d9e8c3d1c4888285.jpg)  
Figure 7.1. Lady Windermere's Fan (O. Wilde (1892))

If we now have two different subdivisions h and $\mathbf { \Pi } _ { \hat { h } } ^ { \tilde { h } }$ ，which both satisfy (7.12)， we introduce a third subdivision which is a refinement of both subdivisions (just as is usually done in proving the existence of Riemann's integral)，and apply (7.13) twice. Wc then obtain from (7.13) by the triangle inequality

$$
\mid y _ { h } ( x ) - y _ { \bar { h } } ( x ) \mid \leq 2 \frac { \epsilon } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) .
$$

For $\epsilon > 0$ small enough, this becomes arbitrarily small and shows the uniform convergence of the Euler polygons to a continuous function $\phi ( x )$

b) Let

$$
\begin{array} { r l } & { \epsilon ( \mathfrak { d } ) { : = } \mathrm { s u p } \Bigg \{ \vert \begin{array} { l } { f \left( u _ { 1 } , \nu _ { 1 } \right) - f \left( u _ { 2 } , \nu _ { 2 } \right) \vert } \\ { \vert u _ { 1 } - u _ { 2 } \vert \le \mathfrak { d } \ , \vert \nu _ { 1 } - \nu _ { 2 } \vert \le A \mathfrak { d } \ , ( u _ { i } , \nu _ { i } ) \in D \Bigg \} } \end{array} } \end{array}
$$

be the modulus of continuity. If $\mathcal { L }$ belongs to the subdivision $h$ then we obtain from (7.5) (replace $( x _ { 0 } , y _ { 0 } )$ by $( x \ , y _ { h } ( x \ ) )$ and $x$ by $x + 8$ ）

$$
\mid y _ { h } \left( x + \ S \right) - y _ { h } \left( x \right) - \ S f \left( x , y _ { h } \left( x \right) \right) \mid \le \mathtt { e } \left( \ S \right) \ S \ .
$$

Passing to the limit $| h _ { \mathbf { \alpha } } | _ {  \mathrm { ~ 0 ~ } }$ we get

$$
\mid \Phi ( x + \mathfrak { d } ) - \Phi ( x ) - \mathfrak { d } f \left( x , \Phi ( x ) \right) \mid \le \mathfrak { e } \left( \mathfrak { d } \right) \mathfrak { d } \ .
$$

Since $\epsilon ( \delta ) \to 0$ for $\delta \to ~ 0$ ， this proves the differentiability of $\Phi ( x )$ and $\Phi ^ { \prime } ( x ) { = } f \left( x , \Phi ( x ) \right)$

c) Let $\Psi ( x )$ be a second solution of (7.1) and suppose that the subdivision $^ h$ satisfies (7.12). We then denote by $y _ { h } ^ { ~ ( i ) } ( x )$ the Euler polygon to the initial value $( x _ { i } , \psi ( x _ { i } ) )$ (it is defined for $x _ { i } \leq x \leq X$ ). It follows from

$$
\psi ( x ) = \psi ( x _ { i } ) + \intop _ { x _ { i } } ^ { x } f \left( s , \psi ( s ) \right) d s
$$

and (7.11) that

$$
| \Psi ( x ) - y _ { h } ^ { ( i ) } ( x ) | \leq \epsilon | x - x _ { i } | \mathrm { ~ f o r ~ } x _ { i } \leq x \leq x _ { i + 1 } .
$$

Using Lemma 7.2 we deduce in the same way as in part a) that

$$
| \Psi ( x ) - y _ { h } ( x ) | \leq \frac { \epsilon } { L } \biggl ( e ^ { L \left( x - x _ { 0 } \right) } - 1 \biggr ) \ ,
$$

Passing to the limits $\lvert h \rvert \to 0$ and $\epsilon  0$ we obtain $| \psi ( x ) - \phi ( x ) | \leq 0$ ， proving uniqueness. QED.

Theorem 7.3 is a local existence - and uniqueness - result. However, if we interpret the endpoint of the solution as a new initial value, we can apply Theorem 7.3 again and continue the solution. Repeating this procedure we obtain

Theorem 7.4. Assume U to be an open set in $\mathbb { R } ^ { 2 }$ and let $f$ and af /dy be continuous on $U$ . Then, for every $( x _ { 0 } , y _ { 0 } ) \in U$ ， there exists a unique solution of (7.1)， which can be continued up to the boundary of $U$ (in both directions).

Proof: Clearly, Theorem 7.3 can be rewritten to give a local existence - and uniqueness - result for an interval $( X \ , \ x _ { 0 } )$ to the left of $x _ { 0 }$ . The rest follows from the fact that every point in $U$ has a neighbourhood which satisfies the assum ptions of Theorem 7.3. QED.

It is interesting to mention that Formula (7.13) for $\mid \hat { h _ { \mathbf { \alpha } } } \mid _ {  \mathbf { \alpha } 0 }$ gives the following error estimate

$$
| ~ y ( x ) - y _ { h } ( x ) ~ | \leq ~ { \frac { \epsilon } { L } } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right)
$$

for the Euler polygon ( $\left| h \right. \left| \leq 8 \right|$ ).Here $y \left( x \right)$ stands for the exact solution of (7.1). The next theorem refines the above estimates for the case that $f \left( x , y \right)$ is also differentiable with respect to $x$ ·

Theorem 7.5. Suppose that in a neighbourhood of the solution

$$
\mid f \mid \le A , \mid \frac { \partial f } { \partial y } \mid \le L , \mid \frac { \partial f } { \partial x } \mid \le M .
$$

W e then have the following error estimate for the Euler polygons:

$$
\left| ~ y \left( x \right) - y _ { h } ( x ) \right| \le ~ { \frac { M + A L } { L } } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) \cdot \left| h ~ \right| ~ ,
$$

provided that $\left| h \right|$ is sufficiently small.

Proof: For $\vert u _ { 1 } - u _ { 2 } \vert \leq \vert h \vert$ and $| \nu _ { 1 } - \nu _ { 2 } | { \leq A }$ $\left| h \right|$ we obtain, due to the differentiability of $f$ , the estimate

$$
\mid f \left( u _ { 1 } , \nu _ { 1 } \right) - f \left( u _ { 2 } , \nu _ { 2 } \right) \mid \ \leq \ \left( M + A L \right) \mid h \mid
$$

instead of (7.11). When we insert this amount for $\epsilon$ into (7.16), we obtain the given result. QED.

The estimate (7.18) shows that the global error of Euler's method is proportional to the maximal step size $\left| h \right| .$ Thus, for an accuracy of, say， three decimal digits, we would need about a thousand steps; a precision of six digits will normally require a million steps etc. We see thus that the present method is not recom mended for computations of high precision. In fact, the main subject of Chapter II will be to find methods which converge faster.

# Existence theorem of Peano

Si a est un complexe d'ordre n , et $^ b$ un nombre reel, alors on peut determiner $b ^ { \prime }$ et $f$ ,ou $b ^ { \prime }$ est une quantite plus grande que $b$ ,et $f$ est un signe de fonction qui a chaque nombre de I'intervalle de $b \ a \ b ^ { \prime }$ fait correspondre un complexe (en d'autres mots, $f t$ est un complexe fonction de la variable reelle t , definie pour toutes les valeurs de l'intervalle $\left( b , b \right) )$ ； la valeur de $f t$ pour $\scriptstyle t = b$ est a ; et dans tout l'intervalle $( b , b ^ { \prime } )$ cette fonction $f t$ satisfait a l'équation différentielle donnee.   
(Original version of Peano's Theorem)

The Lipschitz condition (7.7) is a crucial tool in the proof of (7.10) and finally of the Convergence Theorem. If we completely abandon condition (7.7) and only require that $f \left( x , y \right)$ be continuous, the convergence of the Euler polygons is no longer guaranteed.

An exam ple, plotted in Figure 7.2, is given by the equation

$$
y ^ { \prime } = 4 { \biggl ( } \operatorname { s i g n } ( y ) \left| y \right| ^ { 1 / 2 } + \operatorname { m a x } ( 0 , x - { \frac { | y | } { x } } ) \cdot \cos ( { \frac { \pi \log x } { \log 2 } } ) { \biggr ) }
$$

with $y \left( 0 \right) { = } 0$ . It has been constructed such that

$$
\begin{array} { r l r } & { f \left( h , 0 \right) = 4 h \left( - 1 \right) ^ { i } } & { \mathrm { f o r } \quad h = 2 ^ { - i } \ , } \\ & { f \left( x , y \right) = 4 \mathrm { s i g n } ( y ) \cdot \left| y \right| ^ { 1 / 2 } } & { \mathrm { f o r } \ \left| y \right| \geq x ^ { 2 } \ . } \end{array}
$$

There is an infinity of solutions for this initial value, some of which are plotted in Figure 7.2. The Euler polygons converge for $h = 2 ^ { - i }$ and even i to the maximal solution $y = 4 x ^ { 2 }$ ,and for odd $i$ to $y = - 4 x ^ { 2 }$ For other sequences of $h$ all intermediate solutions can be obtained as well.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/0206b1eae4b64112104b6a1d8be2d4793de08209d21ba59c0d512ba561fc08f6.jpg)  
Figure 7.2. Solution curves and Euler polygons for Equation (7.19)

Theorem 7.6. (Peano (1890)). Let $f \left( x , y \right)$ be continuous and $\mid f \mid$ be bounded by A on

$$
D \ = \ \left\{ ( x , y ) | x _ { 0 } { \le } x \le X \ , | y - y _ { 0 } | \ { \le } \ b \right\} \ .
$$

1f $X ^ { - x } _ { 0 } { \le } { b } / A$ ， then there is a subsequence of the sequence of the Euler polygons which converges to a solution of the differential equation.

The original proof of Peano is, in its crucial part on the conver-gence result, very brief and not clear to unexperienced readers such as we. Arzela (1895)，who took up the subject again, explains his ideas in more detail and emphasizes the need for an equicontinuity of the sequence. The proof usually given nowadays (for what has become the theorem of Arzela-Ascoli), was only introduced later (see e.g. Perron (1918), Hahn (1921), p.303) and is sketched as follows:

Proof: Let

$$
\nu _ { 1 } ( x ) ~ , ~ \nu _ { 2 } ( x ) ~ , ~ \nu _ { 3 } ( x ) , \cdot \cdot \cdot
$$

be a sequence of Euler polygons for decreasing step sizes. It follows from (7.4) that for fixed $x$ this sequence is bounded. We choose a sequence of numbers $r _ { 1 } , r _ { 2 } , r _ { 3 } , . .$ dense in the interval $( x _ { 0 } , X )$ . There is now a subsequence of (7.20) which converges for $\boldsymbol { x } - \boldsymbol { r } _ { 1 }$ (Bolzano-Weierstrass), say

$$
\nu _ { 1 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \nu _ { 2 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \nu _ { 3 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \cdot \cdot \cdot
$$

We next select a subsequence of (7.21) which converges for $\boldsymbol { x } = \boldsymbol { r } _ { 2 }$

$$
\nu _ { 1 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 2 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 3 } ^ { \ ( 2 ) } ( x ) \ , \ \cdots
$$

and so on. Then take the "diagonal" sequence

$$
\nu _ { 1 } ^ { \ ( 1 ) } ( x ) \ , \quad \nu _ { 2 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 3 } ^ { \ ( 3 ) } ( x ) \ , \ \cdot \ \cdot \ 
$$

which, apart from a finite number of terms, is a subscquence of all these sequences, and thus converges for all $r _ { i }$ . Finally, with the estimate

$$
| \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) | \leq A ~ | x - r _ { j } |
$$

(see (7.4))， which expresses the equicontinuity of the sequence, we obtain

$$
\begin{array} { r l } & { \vert \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { m } ^ { ( m ) } ( x ) \vert } \\ & { \leq \vert \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { n } ^ { ( n ) } ( r _ { j } ) \vert + \vert \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) \vert } \\ & { \phantom { = } + \vert \nu _ { m } ^ { ( m ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( x ) \vert } \\ & { \leq 2 A \vert x - r _ { j } \vert + \vert \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) \vert \ . } \end{array}
$$

For fixed $\epsilon > 0$ we then choose a finite subset $R$ of $\{ \boldsymbol { r } _ { 1 }$ ， $r _ { 2 } , \ldots \}$ satisfying $\operatorname* { m i n } \{ | x - r _ { j } | \vert r _ { j } \in R \ , \ x _ { 0 } { \le } x \le X \} { \le } \epsilon / A$ and secondly we choose $N$ such that

$$
| \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) | \leq \ e \quad \mathrm { ~ f o r ~ } \ n , m \geq N \quad \mathrm { a n d ~ } \ r _ { j } \in { \cal R } .
$$

This shows the uniform convergence of (7.23). In the same way as in part b) of the proof of Theorem 7.3 it follows that the limit function is a solution of (7.1). One only has to add an $\mathbf { O } ( \mid h \mid )$ -term in (7.14), if $x$ is not a subdivision point. QED.

# Exercises

1. Apply Euler's method with constant step size $x _ { i + 1 } - x _ { i } = 1 / n$ to the differential equation $y ^ { \prime } { = } k y$ ， $y \left( 0 \right) = 1$ and obtain a classical approxi-mation for the solution $y \left( 1 \right) = e ^ { k } .$ Give an estimate of the error.

2. Apply Euler's method with constant step size to

$$
\begin{array} { l l } { { ) } } & { { y ^ { \prime } = y ^ { 2 } , \qquad y ( 0 ) = 1 , \qquad y ( \displaystyle \frac { 1 } { 2 } ) = ? } } \\ { { ) } } & { { y ^ { \prime } = x ^ { 2 } + y ^ { 2 } , \qquad y ( 0 ) = 0 , \quad y ( \displaystyle \frac { 1 } { 2 } ) = ? } } \end{array}
$$

Make rigorous error estimates using Theorem 7.4 and compare these estimates with the actual errors. The main difficulty is to find a suitable region in which the estimates of Theorem $7 . 4 \ \mathrm { h o l d }$ ， without making the constants $A \ , \ L \ , \ M$ too large and, at the same time,ensuring that the solution curves remain inside this region (see also I.8, Exercise 3).

3. Prove the result: if the differential equation $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 }$ with $f$ continuous, possesses a unique solution, then the Euler polygons converge to this solution.

4. "There is an elementary proof of Peano's existence theorem" (Walter (1971)). Suppose that A is a bound for $\mid f$ 1. Then the sequence

$$
y _ { i + 1 } = y _ { i } + h \operatorname* { m a x } \{ f \left( x , y \right) \mid x _ { i } \leq x \leq x _ { i + 1 } , y _ { i } - 3 A h \leq y \leq y _ { i } + A h \}
$$

converges for all continuous $f$ to a (the maximal) solution. Try to prove this. Unfortunately， this proof does not extend to systems of equations, unless they are "quasimonotone" (see Section I.10, Exercise 3).

# 1.8. Existence Theory using Iteration Methods and Taylor series

A second access to existence theory is possible with the help of an iterative refinement of approximate solutions. The first appearances of the idea are very old. For instance many examples of this type can be found in the work of Lagrange, above all in his astronomical calculations. Let us consider here the following illustrative example of a Riccati equation

$$
y ^ { \prime } = x ^ { 2 } + y + 0 . 1 y ^ { 2 } ~ , ~ y ( 0 ) = 0 ~ .
$$

Due to the presence of the quadratic term, there is no elementary solution. A very natural idea is therefore to neglect this term，which in fact is very small at the beginning,and to solve for the moment

$$
y _ { 1 } ^ { \prime } = x ^ { 2 } + y _ { 1 } ~ , ~ y _ { 1 } ( 0 ) = 0 ~ .
$$

This gives, with the help of Formula (3.3), a first solution

$$
y _ { 1 } ( x ) = 2 e ^ { x } - ( x ^ { 2 } + 2 x + 2 ) \ .
$$

With the help of this solution, we now know more about the initially neglected term $0 . 1 y ^ { 2 } ;$ it will be close to $0 . 1 y _ { 1 } ^ { 2 }$ . So the idea lies at hand to reintroduce this solution into (8.1) and now solve the differential equation

$$
y _ { 2 } ^ { \prime } = x ^ { 2 } + y _ { 2 } + 0 . 1 \bigl ( y _ { 1 } ( x ) \bigr ) ^ { 2 } , y _ { 2 } ( 0 ) = 0 \ ,
$$

We can use Formula (3.3) again and obtain after some calculations

$$
\begin{array} { l } { { y _ { 2 } ( x ) = y _ { 1 } ( x ) + \displaystyle \frac { 2 } { 5 } e ^ { 2 x } - \displaystyle \frac { 2 } { 1 5 } e ^ { x } ( x ^ { 3 } + 3 x ^ { 2 } + 6 x - 5 4 ) } } \\ { { - \displaystyle \frac { 1 } { 1 0 } ( x ^ { 4 } + 8 x ^ { 3 } + 3 2 x ^ { 2 } + 7 2 x + 7 6 ) . } } \end{array}
$$

This is already much closer to the correct solution, as can be seen from the following comparison of the errors $e _ { 1 } { = } y ( x ) { - } y _ { 1 } ( x )$ and $e _ { 2 } { = } y ( x ) { - } y _ { 2 } ( x )$ ：

$$
\begin{array} { l l l } { { x = 0 . 2 } } & { { \ e _ { 1 } = 0 . 2 2 8 \times 1 0 ^ { - 0 7 } } } & { { e _ { 2 } = 0 . 2 3 3 \times 1 0 ^ { - 1 2 } } } \\ { { x = 0 . 4 } } & { { e _ { 1 } = 0 . 3 2 7 \times 1 0 ^ { - 0 5 } } } & { { e _ { 2 } = 0 . 5 6 6 \times 1 0 ^ { - 0 9 } } } \\ { { x = 0 . 8 } } & { { e _ { 1 } = 0 . 5 3 4 \times 1 0 ^ { - 0 3 } } } & { { e _ { 2 } = 0 . 1 6 5 \times 1 0 ^ { - 0 5 } \ , } } \end{array}
$$

It looks promising to continue this process, but the computations soon become very tedious.

# Picard iteration

The general formulation of the method is the following: we try, if possible, to split up the function $f \left( x , y \right)$ of the differential equation

$$
y ^ { \prime } = f ( x , y ) = f _ { 1 } ( x , y ) + f _ { 2 } ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 }
$$

so that any differential equation of the form $y ^ { \prime } { = } f _ { 1 } ( x , y ) { + } g \left( x \right)$ can be solved analytically and so that $f _ { 2 } ( x , y )$ is small. Then we start with a first approxim ation $y _ { 0 } ( x )$ and compute successively $y _ { 1 } ( x )$ ， $y _ { 2 } ( x ) , . . . .$ by solving

$$
y _ { i + 1 } ^ { \prime } = f _ { 1 } ( x , y _ { i + 1 } ) + f _ { 2 } ( x , y _ { i } ( x ) ) \ , y _ { i + 1 } ( x _ { 0 } ) = y _ { 0 } \ .
$$

The most primitive form of this process is obtained by choosing $f _ { 1 } { = } 0 , f _ { 2 } { = } f$ ，in which case (8.6) is immediately integrated and becomes

$$
y _ { i + 1 } ( x ) = y _ { 0 } + \intop _ { x _ { 0 } } ^ { x } f \left( s , y _ { i } ( s ) \right) d s .
$$

This is called the Picard iteration method. It appeared several times in the literature, e.g. in Liouville (1838)， Cauchy， Peano (1888), Lindelof (1894)， Bendixson (1893). Picard (1890) considered it merely as a by-product of a similar idea for partial differential equations and analyzed it thoroughly in his famous treatise Picard (1891- 96), Vol.II, Chap.XI, Sect.III.

The main practical drawback of the method is the need for the repeated computation of integrals, which is usually not very convenient, if at all possible， and soon becomes very tedious. On the other hand, the method is a good tool for theoretical investigations.

Its fast convergence, for $| x - x _ { 0 } |$ small, is readily seen: if we subtract formula (8.7) from the same with i replaced by $i - 1$ , we have

$$
y _ { i + 1 } ( x ) - y _ { i } ( x ) = \int _ { x _ { 0 } } ^ { x } \biggl ( f \left( s , y _ { i } ( s ) \right) - f \left( s , y _ { i - 1 } ( s ) \right) \biggr ) d s .
$$

We now apply the Lipschitz condition (7.7) and the triangle inequality to obtain

$$
| y _ { i + 1 } ( x ) - y _ { i } ( x ) | \leq L \intop _ { x _ { 0 } } ^ { x } | y _ { i } ( s ) - y _ { i - 1 } ( s ) | d s .
$$

When we assume $y _ { 0 } ( x ) \equiv y _ { 0 } ,$ ， we have from the triangle inequality

applied to (8.7) with $i = 0$ the estim ate

$$
| y _ { 1 } ( x ) - y _ { \ 0 } ( x ) | \le A \ | x - x _ { 0 } |
$$

where A is, as in Section I.7, a bound for $\left| f \right|$ . We next insert this into the right hand side of (8.9) repeatedly to obtain finally the estimate

$$
| y _ { i } ( x ) - y _ { i - 1 } ( x ) | \leq A L ^ { i - 1 } { \frac { | x - x _ { 0 } | ^ { i } } { i ! } } ~ .
$$

Theright-handsideiaterof theTaylorseriesforexl which converges for all $\mathcal { A }$ ; we therefore conclude that $| y _ { i + k } - y _ { i } |$ becomes arbitrarily small when i is large. The error is bounded by the remainder of the above exponential series. So the sequence $y _ { i } ( x )$ converges uniformly to the solution $y \left( x \right)$ . For example, if $L \ | x - x _ { 0 } | \leq 1 / 1 0$ and the constant A is moderate, 10 iterations would provide a numerical solution with about 17 correct digits.

# Taylor Series

"Apres avoir montre l'insufsance des methodes d'integration fondees sur le developpement en series, il me reste a dire en peu de mots ce qu’on peut leur substituer."   
(Cauchy)

A third possible existence proof can be based on a study of the convergence of the Taylor series of the solutions. This was mentioned in a footnote of Liouville (1836, p.255)， and brought to perfection by Cauchy (1839-42).

We have already seen the recursive computation of the Taylor coefficients in the work of Newton (see Section I.2). Euler (1768) then formulated the general procedure for the higher derivatives of the solution of

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

which, by successive differentiation, are obtained as

$$
\begin{array} { c } { y ^ { \prime \prime } = f _ { x } + f _ { y } y ^ { \prime } = f _ { x } + f _ { y } f } \\ { y ^ { \prime \prime \prime } = f _ { x x } + 2 f _ { x y } f + f _ { y y } f ^ { 2 } + f _ { y } ( f _ { x } + f _ { y } f ) } \end{array}
$$

etc. Then the solution is

$$
y \left( x _ { 0 } \mathbf { + } h \right) = y \left( x _ { 0 } \right) + y ^ { \prime } ( x _ { 0 } ) h + y ^ { \prime \prime } ( x _ { 0 } ) { \frac { h ^ { 2 } } { 2 ! } } + \cdot \cdot \cdot .
$$

The formulas (8.12) for higher derivatives soon become very complicated. Euler therefore proposed to use only a few terms of this series with $h$ sufficiently small and to repeat the computations from the point ${ { x } _ { 1 } } ^ { = } { { x } _ { 0 } } ^ { + h }$ ("analytic continuation").

# Convergence proof

We shall now outline the main ideas of Cauchy's convergence proof for the series (8.13). We suppose that $f \left( x , y \right)$ is analytic in the neighbourhood of the initial value $x _ { 0 } , y _ { 0 }$ , which for simplicity of notation we assume located at the origin ${ x _ { 0 } } \mathrm { { = } } { y _ { 0 } } \mathrm { { = } } 0$ ：

$$
f ( x , y ) = \sum _ { i , j \geq 0 } a _ { i j } x ^ { i } y ^ { j } ,
$$

where the $a _ { i j }$ are multiples of the partial derivatives occurring in (8.12). If the series (8.14) is assumed to converge for $\{ x \mid \leq r , \mid y \mid \leq r$ then the Cauchy inequalities from classical complex analysis give

$$
| a _ { i j } | ~ \leq ~ { \frac { M } { r ^ { i + j } } } ~ , \quad \mathrm { w h e r e } ~ M ~ = ~ \operatorname* { m a x } _ { \left| x ~ \left| \leq r ~ , ~ \right| y ~ \right| \leq r } \left| f \left( x ~ , y \right) \right| ~ .
$$

The idea is now the following: since all signs in (8.12) are positive, we obtain the worst possible result if we replace in (8.14)al $a _ { i j }$ by the largest possible values (8.15) ("method of majorants"):

$$
f \left( x , y \right) \to \sum _ { i , j \geq 0 } M \frac { x ^ { i } y ^ { j } } { r ^ { i + j } } = \frac { M } { \left( 1 - x / r \right) \left( 1 - y / r \right) } .
$$

However, the majorizing differential equation

$$
y ~ ^ { \prime } = ~ { \frac { M } { ( 1 - x ~ / r ) ( 1 - y ~ / r ) } } ~ , \qquad y ( 0 ) { = } 0
$$

is readily integrated by separation of variables (see Section I.3) and has the solution

$$
y ~ = r \left( 1 - \left( 1 + 2 M \log ( 1 - \frac { x } { r } ) \right) ^ { 1 / 2 } \right) ~ ,
$$

This solution has a power series which converges for all $x$ such that $| 2 M \log ( 1 { - } x / r ) | { < } 1$ .Therefore, the series (8.13) also converges at least for all $\mid h \mid < r ( 1 { - } \exp ( - 1 / 2 M ) )$ . QED.

# Recursive Computation of Taylor Coefficients

"...dieses Verfahren praktisch nicht in Frage kommen kann".   
(Runge-Konig, 1924)   
"The exact opposite is true, if we use the right approach .."   
(R.E. Moore, 1979)

The "right approach" is, in fact, an extension of Newton's approach and has been rediscovered several times (e.g. Steffensen (1956)) and implemented in generality into computer programs by Gibbons (1960) and Moore (1966). For a more extensive bibliography see the references in Wanner (1969), p.10-20.

The idea is the following: let

$$
Y _ { i } = \frac { 1 } { i ! } y ^ { ( i ) } ( x _ { 0 } ) , F _ { i } = \frac { 1 } { i ! } \bigg ( f \left( x , y \left( x \right) \right) \bigg ) ^ { ( i ) } \vert _ { x = x _ { 0 } }
$$

be the Taylor coefficients of $y \left( x \right)$ and of $f \left( x , y \left( x \right) \right)$ , so that (8.13) becomes

$$
y \left( x _ { 0 } { + } h \right) = \sum _ { i = 0 } ^ { \infty } h ^ { i } Y _ { i } .
$$

Then, from (8.11),

$$
Y _ { i + 1 } = { \frac { 1 } { i + 1 } } F _ { i } .
$$

Now suppose that $f \left( x , y \right)$ is the composition of a sequence of algebraic operations and elementary functions. This leads to a sequence of items,

$$
x , y , p , q , r \ , \ldots , \mathrm { ~ a n d ~ f i n a l l y } \ f .
$$

For each of these items we find formulas for generating the $i - t h$ Taylor coefficient from the preceding ones as follows:

a) $r = p \pm q$

$$
R _ { i } = P _ { i } \pm Q _ { i } \qquad i = 0 , 1 , \cdots
$$

b) $r = p q$

$$
R _ { i } = \sum _ { j = 0 } ^ { i } P _ { j } Q _ { i - j } i = 0 , 1 , \cdots
$$

(the Cauchy product).

c） $r \ = p / q$ : write $p = r q$ , use formula b) and solve for $R _ { i }$ ：

$$
R _ { i } = { \frac { 1 } { Q _ { 0 } } } \biggl ( P _ { i } - \sum _ { j = 0 } ^ { i - 1 } R _ { j } Q _ { i - j } \biggr ) \qquad i = 0 , 1 , \cdots ,
$$

There also exist formulas for many elementary functions (in fact, because these functions are themselves solutions of rational differential equations). Examples:

d） $r = \exp ( p )$ : use $r ^ { \prime } { = } p ^ { \prime } { \cdot } r$ and apply (8.20.b). This gives (for $i = 1 , 2 , \ldots ,$

$$
R _ { 0 } = \exp ( P _ { 0 } ) , ~ R _ { i } = \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i { - } j ) R _ { j } P _ { i { - } j } ~ .
$$

e） $r = \log ( p )$ : use $p { = } \mathbf { e x p } ( r )$ and rearrange formula d). This gives

$$
R _ { 0 } = \log ( P _ { 0 } ) , \quad R _ { i } = \frac { 1 } { P _ { 0 } } \biggl ( P _ { i } - \frac { 1 } { i } \sum _ { j = 1 } ^ { i - 1 } ( i - j ) P _ { j } R _ { i - j } \biggr ) \ .
$$

f） $r = p ^ { c } , c \neq 1$ constant. Use $\boldsymbol { r ^ { \prime } } { = } \boldsymbol { c p } ^ { c - 1 } \boldsymbol { p }$ ',i.e. ${ p r } ^ { \prime } { = } c r p ^ { \prime }$ and apply (8.20.b)

$$
R _ { 0 } ^ { c } ~ , ~ R _ { i } ^ { } ~ = ~ { \frac { 1 } { i P _ { 0 } } } \bigg ( \sum _ { j = 0 } ^ { i - 1 } ( c i - ( c + 1 ) j ) R _ { j } ^ { } P _ { i - j } ^ { } \bigg ) ~ .
$$

g） $r = \cos ( p ) , s = \sin ( p ) ;$ as in d) we have

$$
\begin{array} { l } { { \displaystyle { R _ { 0 } = \mathrm { c o s } P _ { 0 } , \quad R _ { i } = - \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i - j ) S _ { j } P _ { i - j } } . } } \\ { { \displaystyle { S _ { 0 } = \mathrm { s i n } P _ { 0 } , \quad S _ { i } = \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i - j ) R _ { j } P _ { i - j } } . } } \end{array}
$$

The alternating use of (8.20) and (8.18) then allows us to compute the Taylor coefcients for (8.17) to any wanted order in a very economical way. It is not difficult to write subroutines for the above formulas, which have to be called in the same order as the differential equation (8.11) is composed of elementary operations. There also exist computer programs which "compile" Fortran statements for $f \left( x , y \right)$ into this list of subroutine calls. One has been written by T.Szym anski and J.H.Gray (see Knapp-Wanner (1969)).

Example. The diferential equation $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ leads to the recursion $\scriptstyle { Y _ { 0 } = y ( 0 ) }$ ，

$$
Y _ { i + 1 } = { \frac { 1 } { i + 1 } } \left( P _ { i } + \sum _ { j = 0 } ^ { i } Y _ { j } Y _ { i - j } \right) \qquad i = 0 , 1 , \ \cdot \ \cdot \ .
$$

where ${ \bar { P } } _ { i } = 1$ for $i = 2$ and ${ \boldsymbol { P } } _ { i } = 0$ for $i \neq 2$ are the coefficients for $x ^ { 2 }$ .One can imagine how much easier this is than Formulas (8.12).

An important property of this approach is that it can be executed in interval analysis and thus allows us to obtain reliable error bounds by

the use of Lagrange's error formula for Taylor series. We refer to the books by R.E. Moore (1966) and (1979) for more details.

# Exercises

1. Obtain from (8.10) the estimate

$$
| y _ { i } ( x ) - y _ { 0 } | ~ \le ~ \frac { 1 } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) A
$$

and explain the similarity of this result with (7.16).

2. Apply the method of Picard to the problem $y ^ { \prime } { = } K y$ ， $y \left( 0 \right) { = } 1$

3. Compute three Picard iterations for the problem $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ ， $y \left( 0 \right) { = } 0$ ， $y \left( 1 / 2 \right) = ?$ and make a rigorous error estimate. Compare the result with the correct solution y(1/2)=0.041791146154681863220768806849179 .

4. Compute with an iteration method the solution of

$$
y ^ { \prime } = \sqrt { x } + \sqrt { y } , \qquad y \left( 0 \right) = 0
$$

and observe that the method can work well for equations which pose serious problems with other methods. An even greater difference occurs for the equations

$$
y ^ { \prime } = \sqrt { x } + { y ^ { 2 } } , y ( 0 ) = 0 \mathrm { ~ a n d ~ } y ^ { \prime } = \frac { 1 } { \sqrt { x } } + { y ^ { 2 } } , y ( 0 ) = 0 .
$$

5. Define $f \left( x , y \right)$ by

$$
f \left( x , y \right) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { f o r ~ } x \leq 0 } \\ { \displaystyle 2 x } & { \mathrm { f o r ~ } x > 0 ~ , \quad y < 0 } \\ { \displaystyle 2 x - \frac { 4 y } { x } } & { \mathrm { f o r ~ } x > 0 ~ , \quad 0 \leq y \leq x ^ { 2 } } \\ { \displaystyle - 2 x } & { \mathrm { f o r ~ } x > 0 ~ , \quad x ^ { 2 } < y ~ . } \end{array} \right.
$$

a) Show that $f \left( x , y \right)$ is continuous, but not Lipschitz.

b) Show that for the problem $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( 0 \right) { = } 0$ the iteration method does not converge.

c) Show that there is a unique solution and that the Euler polygons converge.

6. Use the method of Picard iteration to prove: If $f \left( x , y \right)$ is continuous and satisfies a Lipschitz condition (7.7)

on the infinite strip $D = \{ ( x \ , \ y ) ; x _ { 0 } { \leq } x { \leq } X \}$ , then the initial value problem $y ^ { \prime } { = } f \left( x \ , \ y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 }$ possesses a unique solution on $x _ { 0 } \leq x \leq X$

Compare this global result with Theorem 7.3.

7. Define a function $y \left( x \right)$ (the "inverse error function") by the relation

$$
x : = \frac { 2 } { \sqrt { \pi } } \int _ { 0 } ^ { y } e ^ { - t ^ { 2 } } d t
$$

and show that it satisfies the differential equation

$$
y ^ { \prime } = \frac { \sqrt { \pi } } { 2 } e ^ { y ^ { 2 } } , \qquad y \left( 0 \right) { = } 0 .
$$

Obtain recursion formulas for its Taylor coefficients.

I.9. Existence theory for systems of equations

The first treatment of an existence theory for simultaneous systems of differential equations was undertaken in the last existing pages (p.123-136) of Cauchy (1824). Using the index notation, which at that time was not yet en vogue, we write the equations as

$$
\begin{array} { c c c } { { y _ { 1 } ^ { \prime } = f _ { 1 } ( x , y _ { 1 } , \ldots , y _ { n } ) ~ , } } & { { } } & { { y _ { 1 } ( x _ { 0 } ) = y _ { 1 0 } ~ , } } \\ { { \ldots } } & { { } } & { { \ldots } } \\ { { y _ { n } ^ { \prime } = f _ { n } ( x , y _ { 1 } , \ldots , y _ { n } ) ~ , } } & { { } } & { { y _ { n } ( x _ { 0 } ) = y _ { n 0 } ~ , } } & { { y _ { n } ( X ) = 7 } } \end{array}
$$

and ask for the existence of the n solutions $y _ { 1 } ( x ) , \ldots , y _ { n } ( x ) .$ As the equations (9.1) prescribe, for any given $y _ { 1 } , \ldots , y _ { n }$ , the derivatives of these functions, it is again natural to consider, in analogy to (7.3), the method of Euler

$$
y _ { k , i + 1 } = y _ { k i } + ( x _ { i + 1 } - x _ { i } ) \cdot f _ { k } ( x _ { i } , y _ { 1 i } , . . . , y _ { n i } )
$$

$$
k = 1 , . . . , n , \quad i = 0 , 1 , 2 , \cdot \cdot \cdot ,
$$

Here $y _ { k i }$ is intended to approximate $y _ { k } \left( x _ { i } \right)$ ,where $x _ { 0 } { < } x _ { 1 } { < } x _ { 2 } { ~ } { \cdot } { } ~ { \cdot } ~ .$ is a subdivision of the interval of integration as in (7.2).

We now try to carry over everything we have done in Section I.7 to the new situation. Although we have no problem in extending (7.4) to the estim ate

$$
| y _ { k i } - y _ { k 0 } | \ \leq \ A _ { k } \ | x _ { i } - x _ { 0 } | \qquad \mathrm { i f } \quad | f _ { k } \left( x \ , y _ { 1 } \ldots , y _ { n } \right) | \ \leq \ A _ { k } \ ,
$$

things become a little more complicated for (7.7): we have to estimate

$$
\begin{array} { r l r } {  { f _ { k } ( x , z _ { 1 } , \dots , z _ { n } ) - f _ { k } ( x , y _ { 1 } , \dots , y _ { n } ) } } \\ & { } & { \quad = \frac { \partial f _ { k } } { \partial y _ { 1 } } { \cdot } ( z _ { 1 } { - } y _ { 1 } ) + \cdot \cdot \cdot + \frac { \partial f _ { k } } { \partial y _ { n } } ( z _ { n } { - } y _ { n } ) \ , } \end{array}
$$

where the derivatives $\partial f _ { k } / \partial y _ { i }$ are taken at suitable intermediate points. Here Cauchy uses the inequality which he invented just before and which now is called the "Cauchy-Schwarz inequality" ("Enfin, il resulte de la formule (13) de la 11e lecon du calcul differentiel ..") to obtain

$$
| f _ { k } ( x , z _ { 1 } , . . . , z _ { n } ) - f _ { k } ( x , y _ { 1 } , . . . , y _ { n } ) |
$$

$$
\leq \left( { \bigl ( } { \frac { \partial f _ { k } } { \partial y _ { 1 } } } { \bigr ) } ^ { 2 } + \cdot \cdot \cdot + { \bigl ( } { \frac { \partial f _ { k } } { \partial y _ { n } } } { \bigr ) } ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( { \bigl ( } z _ { 1 } { - } y _ { 1 } { \bigr ) } ^ { 2 } + \cdot \cdot \cdot + { \bigl ( } z _ { n } { - } y _ { n } { \bigr ) } ^ { 2 } \right) ^ { \frac { 1 } { 2 } } .
$$

At this stage, we begin to feel that further development is advisable only after the introduction of vector notation.

# Vector notation

This was promoted in our subject by the papers of Peano, (1888) and (1890)，who was influenced, as he says, by the famous "Ausdehnungslehre" of Grassmann and the work of Hamilton, Cayley, and Sylvester. We introduce the vectors (Peano called them "complexes")

$$
y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T } , y _ { i } = ( y _ { 1 i } , \ldots , y _ { n i } ) ^ { T } , z = ( z _ { 1 } , \ldots , z _ { n } ) ^ { T }
$$

and hope that the reader will not confuse the components $y _ { i }$ of a vector y with vectors with indices. We consider the "vector function" $f \left( x , y \right) = \left( f _ { 1 } ( x , y ) , \ldots , f _ { n } \left( x , y \right) \right) ^ { T }$ , so that Equations (9.1) become

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y \left( X \right) = ?
$$

and Euler's method (9.2) is

$$
y _ { i + 1 } = y _ { i } + ( x _ { i + 1 } - x _ { i } ) f ( x _ { i } , y _ { i } ) \ \quad \quad i = 0 , 1 , 2 , { \mathrm { ~ e t c } } \ .
$$

There is no longer any difference in notation with the onedimensional cases (7.1) and (7.3).

$y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T }$ trce

$$
\parallel y \parallel = { \bigl ( y _ { 1 } ^ { ~ 2 } + \dots + y _ { n } ^ { ~ 2 } \bigr ) ^ { 1 / 2 } }
$$

which satisfies all the usual properties of a norm, for exam ple the tri-angle inequality

$$
\| { \textbf { \it y } } + z \| \ \leq \ \| { \textbf { \it y } } \| + \| { \textbf { \it z } } \| , \| \sum _ { i = 1 } ^ { m } \| \leq \sum _ { i = 1 } ^ { m } \| { \textbf { \it y } } _ { i } \| .
$$

We now are able to formulate Estimates (9.3) and (9.5) as follows, in perfect analogy with (7.4) and (7.7):

Theorem 9.1. Suppose that $\left| \left| ~ f \left( x , y \right) \right| \right| \leq A$ ; then we have for the $y _ { i }$ defined by (9.2') the estimate

$$
\begin{array} { r } { \left| \left| ~ y _ { i } - y _ { 0 } \right| \right| ~ \leq ~ A ~ | x _ { i } - x _ { 0 } | ~ . } \\ { I f ~ | ~ \frac { \partial f _ { k } } { \partial y _ { i } } | ~ \leq ~ q _ { k i } , { t h e n } ~ } \end{array}
$$

$$
\begin{array} { r l } { { \left\| \begin{array} { l } { f \left( x , z \right) - f \left( x , y \right) | } \end{array} } } & {\right\ { } \leq L \ \left\| \begin{array} { l } { z - y } \end{array} \right\| } \\ { } & { { } } \\ { w h e r e \quad L } & { { } = \bigg ( \sum _ { i , k } q _ { k i } ^ { 2 } \bigg ) ^ { 1 / 2 } . } \end{array}
$$

Proof: (9.9) is obtained by squaring (9.5) and adding up for $k = 1 , \ldots , n$ . QED.

The estimate (9.9) is called the "mean value theorem" and can be found in many books on analysis.

The Euclidean norm (9.6) is not the only one possible, we also use ("on pourrait aussi definir par $m x$ la plus grande des valeurs absolues des elements de x ; alors les proprietes des modules sont presqu'evidentes." (Peano))

$$
\parallel y \parallel = \operatorname* { m a x } ( \mid y _ { 1 } \mid , . . . , \mid y _ { n } \mid ) .
$$

In this case, in order to establish (9.9), we estimate (9.4) in the following way:

$$
| f _ { k } ( x , z ) - f _ { k } ( x , y ) | \leq \bigg ( | \frac { \partial f _ { k } } { \partial y _ { 1 } } | + \cdot \cdot \cdot + | \frac { \partial f _ { k } } { \partial y _ { n } } | \bigg ) \cdot \operatorname* { m a x } _ { i } ( | z _ { i } - y _ { i } | ) ~ .
$$

Therefore, Theorem 9.1 remains true if we replace (9.10) by

$$
L \ = \ \operatorname* { m a x } _ { k } \left( \sum _ { i } | q _ { k i } | \right) .
$$

Finally, if we want to use the norm

$$
\parallel y \parallel = | y _ { 1 } | + \cdot \cdot \cdot + | y _ { n } | ,
$$

(9.10) of Theorem 9.1 has to be replaced by

$$
L \ = \operatorname* { m a x } _ { i } \left( \sum _ { k } | q _ { k i } | \right) .
$$

In all three cases, we have established a perfect analogy with (7.5) and (7.7) of Section I.7. Al that remains to do is, Da capo al fine, read Sections I.7 and I.8 again: Theorems 7.2, 7.3, 7.4, 7.5, and 7.6 together with their proofs and the estimates (7.10), (7.13),(7.15), (7.16), (7.17), and (7.18) carry over to the more general case with the only changes that some absolute values are to be replaced by norms.

# Subordinate matrix norms

Denote by $Q$ the matrix with elements $q _ { k i } .$ The constant defined in (9.10'), which we now denote by

$$
\parallel \boldsymbol { \mathcal { Q } } \parallel = \operatorname* { m a x } _ { k } \left( \sum _ { i } | q _ { k i } | \right)
$$

is callcd the matrix norm subordinate to the vector norm (9.6'). It is the smallest number which allows the estim ate

$$
\| ~ Q y ~ \| ~ \leq ~ \| ~ Q ~ \| ~ \| ~ y ~ \|
$$

for all vectors y, or, in other words,

$$
\parallel { \cal Q } \parallel = \operatorname* { s u p } _ { y \neq 0 } \frac { \parallel \boldsymbol { Q } y \parallel } { \parallel y \parallel } \mathrm { ~ , ~ }
$$

Similarly, the matrix norm subordinate to the norm (9.6") appears in (9.10"), i.e.

$$
\parallel Q \parallel = \operatorname* { m a x } _ { i } \left( \sum _ { k } | q _ { k i } | \right) .
$$

However, (9.10) (which is called the "Schur norm") is nol subordinate to the norm (9.6), since,although it satisfies (9.12), it is not the smallest possible bound. Here, the subordinate norm is given by

$$
\parallel \boldsymbol { \mathcal { Q } } \parallel = \sqrt { \mathsf { A } _ { \operatorname* { m a x } } } \mathrm { ~ , ~ }
$$

where $\lambda _ { \operatorname* { m a x } }$ is the largest eigenvalue of $Q ^ { T } Q$ . This can be seen from

$$
\parallel Q y \parallel ^ { 2 } = y ^ { T } Q ^ { T } Q y
$$

with the help of an orthogonal transformation of $Q ^ { T } Q$ to diagonal form.

Au these formulas remain valid for complex matrices. Only $Q ^ { T }$ has to be replaced by $Q ^ { * }$ (transposed and complex conjugate). See e.g. Wilkinson (1965), p.55-61, Bakhvalov (1976), Chap. VI, Par. 3.

# Picard iteration for systems

The iteration method of Picard also carres over to systems of equations when in (8.7) we interpret $y _ { i + 1 } ( x ) , y _ { 0 }$ and $f \left( s , y _ { i } ( s ) \right)$ as vectors， integrated componentwise. The convergence result with the estimate (8.10) also remains the same; for its proof we have to use, between (8.8) and (8.9), the inequality

$$
\| \int _ { a } ^ { b } g ( x ) d x \parallel \leq \int _ { a } ^ { b } \| g ( x ) \| d x
$$

for a vector valued function $g \left( x \right) = ( g _ { 1 } ( x ) , \ldots , g _ { n } ( x ) ) ^ { T }$ Equation (9.14) is proved by applying the triangle inequality (9.7) to the finite Riemann sums which define the two integrals.

The Taylor series method, its convergence proof, and the recursive generation of the Taylor coefficients also generalize in a straightforward manner to systems of equations.


<!-- chunk 0002: pages 71-140 -->
# Exercises

1. Solve the system

$$
\begin{array} { c c } { { y _ { 1 } ^ { \prime } = - y _ { 2 } , } } & { { \qquad y _ { 1 } ( 0 ) = 1 } } \\ { { { } } } & { { { } } } \\ { { y _ { 2 } ^ { \prime } = + y _ { 1 } , } } & { { \qquad y _ { 2 } ( 0 ) = 0 } } \end{array}
$$

by the methods of Euler and Picard, establish rigorous error estimates for all three norms mentioned. Verify the results using the correct solution $y _ { 1 } ( x ) { = } \mathrm { c o s } x$ ， $y _ { 2 } ( x ) { = } \mathrm { s i n } x$

2. Consider the differential equations

$$
\begin{array} { r l } & { y _ { 1 \ } ^ { \prime } = - 1 0 0 y _ { 1 \ } + y _ { 2 \ } , \qquad y _ { 1 } ( 0 ) = 1 \ , \qquad y _ { 1 } ( 1 ) = ? } \\ & { y _ { 2 \ } ^ { \prime } = y _ { 1 \ } - 1 0 0 y _ { 2 \ } , \qquad y _ { 2 } ( 0 ) = 0 \ , \qquad y _ { 2 } ( 1 ) = ? } \end{array}
$$

a) Compute the exact solution $y \left( x \right)$ by the method explained in Section I.6.

b) Compute the error bound for $| \begin{array} { l l l l } \end{array} | z ( x \begin{array} { r l } \end{array} ) - y ( x \begin{array} { r l } \end{array} ) | | \begin{array} { r l } \end{array} $ ,where $z \left( x \right) { = } 0$ ， obtained from (7.10).

c) Apply the method of Euler to this equation with $h = 1 / 1 0$ d) Apply Picard's iteration method.

3. Compute the Taylor series solution of the system with constant coefficients $y ^ { \prime } { = } A y$ ， ${ \boldsymbol { y } } \left( 0 \right) = { \boldsymbol { y } } _ { 0 }$ .Prove that this series converges for all $x$ . Apply this series to the equation of Exercise 1. R esult:

$$
y ( x ) = \sum _ { i = 0 } ^ { \infty } \frac { x ^ { i } } { i ! } { A ^ { i } y _ { 0 } } = : e ^ { A x } y _ { 0 } .
$$

# 1.10. Differential inequalities

An elegant instrument for a better understanding of Equations (7.10),(7.17) and much new insight is that of differential inequalities. This subject was inaugurated in the paper, once again, Peano (1890) and further developed by Perron (1915)，Muller (1926)， Kamke (1930). A classical treatise on the subject is the book of Walter (1970).

# Introduction

The basic idea is the following: let $\nu \left( x \right)$ denote the Euler polygon defined in (7.3) or (9.2), so that

$$
\nu ^ { \prime } ( x ) = f ( x _ { i } , y _ { i } ) \quad \mathrm { f o r } x _ { i } < x < x _ { i + 1 } .
$$

For any chosen norm， we investigate the error

$$
m \left( x \right) = \left. \nu \left( x \right) - y \left( x \right) \right.
$$

as a function of $x$ and we naturally try to estimate its growth.

Unfortunately, $m \left( x \right)$ is not necessarily differentiable, due firstly to the corners in the Euler polygons and secondly， to corners originating from the norms, especially the norms (9.6') and (9.6"). Therefore we consider the so-called $D$ ini derivates defined as

$$
\begin{array} { l } { { D ^ { + } m \left( x \right) = \displaystyle \operatorname* { l i m s u p } _ { h > 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D ^ { - } m \left( x \right) = \displaystyle \operatorname* { l i m s u p } _ { h < 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D _ { + } m \left( x \right) = \displaystyle \operatorname* { l i m i n f } _ { h > 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D _ { - } m \left( x \right) = \displaystyle \operatorname* { l i m i n f } _ { h < 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \end{array}
$$

(see e.g. Scheeffer (1884), Hobson (1921), Chap.V, \$260, \$280). The properties

$$
\begin{array} { r l r } { \left\| ~ w \left( x + h \right) \right\| ~ - \left\| ~ w \left( x \right) \right\| } & { \leq } & { \left\| ~ w \left( x + h \right) - w \left( x \right) \right\| } \\ { \left\| ~ w \left( x \right) \right\| ~ - \left\| ~ w \left( x + h \right) \right\| } & { \leq } & { \left\| ~ w \left( x + h \right) - w \left( x \right) \right\| } \end{array}
$$

are simple consequences of the triangle inequality (9.7). If we divide (10.3) by $h > 0$ , we obtain the estimates

$$
D _ { + } | | ~ w ( x ) ~ | | ~ \leq ~ | | ~ w ^ { \prime } ( x ) ~ | | ~ , ~ D ^ { + } | | ~ w ( x ) ~ | | ~ \leq ~ | | ~ w ^ { \prime } ( x ) ~ | | ~ ,
$$

where $w ^ { \prime } ( x )$ is the right derivative of the vector function $w \left( x \right)$ If we apply this to $m \left( x \right)$ of (10.2), we obtain

$$
\begin{array} { r l } {  { D _ { + } m ( x ) \ \leq \  \ \nu ^ { \prime } ( x ) - y ^ { \prime } ( x )   } } \\ & { =  \ \nu ^ { \prime } ( x ) - f ( x , \nu ( x ) ) + f ( x , \nu ( x ) ) - f ( x , y ( x ) )  } \end{array}
$$

and, using the triangle inequality and the Lipschitz condition (9.9),

$$
D _ { + } m \left( x \right) \leq 8 ( x ) + L m \left( x \right) .
$$

Here, we have introduced

$$
\delta ( x ) = \parallel \nu ^ { \prime } ( x ) - f \left( x , \nu ( x ) \right) \parallel
$$

which is called the defect of the approximate solution $\nu \left( x \right)$ This fundamental quantity measures the extent to which the function $\nu \left( x \right)$ does not satisfy the imposed differential equation. (7.11) tels us together with (10.1） that $\mathfrak { F } ( x ) \le \epsilon$ ， so that (10.5) can be further estimated to become

$$
D _ { + } m \left( x \right) \leq L m \left( x \right) + \epsilon , m \left( x _ { 0 } \right) = 0 .
$$

(10.7) (or (10.5)) is what one calls a differential inequality. The question is: are we allowed to replace "≤" by "=", i.e. to solve instead of (10.7) the equation

$$
u ^ { \prime } = L u + \epsilon , \qquad u ( x _ { 0 } ) = 0
$$

and to conclude that $m ( x ) \leq u ( x ) \}$ This would mean, by the formu-las of Section I.3 or I.5,

$$
m \left( x \right) \ { \le \ } \ \frac { \epsilon } { L } \bigg ( e ^ { L \left( x - x _ { 0 } \right) } - 1 \bigg ) \ .
$$

We would thus have obtained (7.17) in a natural way and furthermore discovered an elegant and powerful tool for many kinds of new estimates.

# The fundamental theorems

A general theorem of the type

$$
\begin{array} { r l } & { D _ { + } m \left( x \right) \leq \varrho \left( x , m \left( x \right) \right) } \\ & { D _ { + } u \left( x \right) \geq \varrho \left( x , u \left( x \right) \right) } \\ & { m \left( x _ { 0 } \right) \leq u \left( x _ { 0 } \right) } \end{array} \Bigg \} \begin{array} { r l } & { \mathrm { i m p l i e s } \quad m \left( x \right) \leq u \left( x \right) } \\ { \mathrm { f o r } x _ { 0 } \leq x } \end{array}
$$

cannot be true. Counter-examples are provided by any differential equation with non-unique solutions, such as

$$
g \left( x , y \right) = \sqrt { y } , m \left( x \right) = \frac { x ^ { 2 } } { 4 } , u \left( x \right) = 0 .
$$

The important observation, due to Peano and Perron， which allows us to overcome this difficulty, is that one of the first two inequalities must be replaced by a strict inequality (see Peano (1890), \$3, Lemme 1):

Theorem 10.1. Suppose that the functions $m \left( x \right)$ and $u \left( x \right)$ are continuous and satisfy $f o r \ x _ { 0 } { \le } x < X$

$$
\begin{array} { r l } { \mathrm { a } ) } & { { } D _ { + } m \left( x \right) \leq \ g \left( x , m \left( x \right) \right) } \\ { \mathrm { b } ) } & { { } D _ { + } u \left( x \right) > \ g \left( x , u \left( x \right) \right) } \\ { \mathrm { c } ) } & { { } m \left( x _ { 0 } \right) \leq \ u \left( x _ { 0 } \right) \ . } \end{array}
$$

Then

$$
m \left( x \right) \leq u \left( x \right) \qquad f o r \ x _ { \ 0 } \leq \ x \ \leq \ X \ .
$$

The same conclusion is true if both $D _ { + }$ are replaced by $D ^ { + }$

Proof: In order to be able to compare the derivatives $D _ { + } m$ and $D _ { + } \mu$ in (10.12),we consider points at which $m \left( x \right) = u \left( x \right) .$ This is the main idea.

If (10.13) were not true, we could choose a point $x _ { 2 }$ with $m \left( { x _ { 2 } } \right) > u \left( { x _ { 2 } } \right)$ and look for the first point $x _ { 1 }$ to the left of $x _ { 2 }$ with $m \left( x _ { 1 } \right) { = } u \left( x _ { 1 } \right) .$ Then for sm all $h > 0$ we would have

$$
\frac { m \left( x _ { 1 } + h \right) - m \left( x _ { 1 } \right) } { h } > \frac { u \left( x _ { 1 } + h \right) - u \left( x _ { 1 } \right) } { h }
$$

and, by taking limits, $D _ { + } m \left( x _ { 1 } \right) \geq D _ { + } u \left( x _ { 1 } \right) .$ This, however, contradicts a) and b), which give

$$
D _ { + } m \left( x _ { 1 } \right) \leq g \left( x _ { 1 } , m \left( x _ { 1 } \right) \right) = g \left( x _ { 1 } , u \left( x _ { 1 } \right) \right) < D _ { + } u \left( x _ { 1 } \right) .
$$

QED.

Many variant forms of this theorem are possible, for example by using left Dini derivates (Walter (1970), Chap.II, \$8, Theorem V). The developments of the introduction now lead to

Theorem 10.2. (The "fundamental lemma"). Suppose that $\nu \left( x \right)$ is an approximate solution of the system of diferential equations $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 } .$ satisfying

$$
\begin{array} { r l } { \mathrm { a } ) } & { \parallel \nu \left( x _ { 0 } \right) - y \left( x _ { 0 } \right) \parallel \leq \mathsf { p } } \\ { \mathrm { b } ) } & { \parallel \nu ^ { \prime } ( x ) - f \left( x , \nu \left( x \right) \right) \parallel \leq \mathsf { \epsilon } } \\ { \mathrm { c } ) } & { \parallel f \left( x , \nu \right) - f \left( x , y \right) \parallel \leq L \parallel \nu - y \parallel . } \\ { T h e n , f o r x \geq x _ { 0 } \mathrm { , } \mathrm { ~ } \mathsf { n } a \nu e \mathrm { ~ } t h e \mathrm { ~ } e r r o r e s t i m a t e } \\ { \parallel y \left( x \right) - \nu \left( x \right) \parallel \leq \mathsf { p } e ^ { L \left( x - x _ { 0 } \right) } + \frac { \mathsf { \epsilon } } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) . } \end{array}
$$

Remark: The two terms in (10.14) express, respectively, the influence of the error p in the initial values and the influence of the defect ∈ to the error of the approximate solution. It implies that the error depends continuously on both, and that for $\rho = \epsilon = 0$ we have $y \left( x \right) = y \left( x \right) ,$ i.e. uniqueness of the solution.

Proof: We put $m \left( x \right) = \left| \right| y \left( x \right) - \nu \left( x \right) \right| \left|$ and obtain, as in (10.7),

$$
D _ { + } m \left( x \right) \leq L m \left( x \right) + \epsilon , \qquad m \left( x _ { 0 } \right) \leq \textsf { \textsf { p } } ,
$$

We shall try to compare this with the differential equation

$$
u ^ { \prime } = L u + \epsilon , \qquad u ( x _ { 0 } ) = \rho .
$$

Theorem 10.1 is not directly applicable. We therefore replace in (10.15) $\epsilon$ by $\epsilon + \eta$ ， $\eta > 0$ and solve instead

$$
u ^ { \prime } = L u + \tt { \epsilon } + \tt { \eta } \eta > L u + \tt { \epsilon } \ , \qquad u \left( x \leq \alpha _ { 0 } \right) = \alpha _ { 0 } \ .
$$

Now Theorem 10.1 gives the estimate (10.14) with ∈ replaced by $\epsilon + \eta$ . Since this estimate is true for $a l l \ \eta > 0$ , it is also true for $\eta = 0$ QED.

Variant form of Theorem 10.2. The conditions

imply for x≥ x0

$$
\begin{array} { r }  | \begin{array} { l } { y ( x ) - \nu ( x ) | \displaystyle | \begin{array} { l } { \leq e ^ { L ( x ) } \Biggl [ \displaystyle \rho + \int _ { x _ { 0 } } ^ { x } e ^ { - L ( s ) } \mathfrak { f } ( s ) d s \Biggr ] , L ( x ) = \int _ { x _ { 0 } } ^ { x } l ( s ) d s } \end{array}  } \end{array} \end{array}
$$

Proof: This is nothing but Formula (3.3). QED.

Theorem 10.3. If the function $g \left( x , y \right)$ is continuous and satisfies a Lipschiz condition, then the implication (1O.1O) is true for continuous fonctions $m \left( x \right)$ and u $\left( x \right)$ ·

Proof: Define functions $w _ { n } ( x ) , \nu _ { n } ( x )$ by

$$
\begin{array} { r l r } { { w _ { n } ^ { \prime } ( x ) = g \left( x , w _ { n } ( x ) \right) + \frac { 1 } { n } \ , } } & { { } { w _ { n } ( x _ { 0 } ) = m \left( x _ { 0 } \right) \ , } } & { { } } \\ { { \nu _ { n } ^ { \prime } ( x ) = g \left( x , \nu _ { n } ( x ) \right) - \frac { 1 } { n } \ , } } & { { \nu _ { n } ( x _ { 0 } ) = u \left( x _ { 0 } \right) \ , } } \end{array}
$$

so that from Theorem 10.1

$$
m \left( x \right) \leq w _ { n } \left( x \right) , \quad \nu _ { n } \left( x \right) \leq u \left( x \right) \quad \mathrm { ~ f o r ~ } \quad x _ { 0 } \leq x \leq X ,
$$

It follows from Theorem 10.2 that the functions $w _ { n } \left( x \right)$ and $\nu _ { n } ( x )$ converge for $n  \infty$ to the solutions of

$$
\begin{array} { c c } { { w ^ { \prime } ( x ) = g \left( x , w \left( x \right) \right) , } } & { { w \left( x _ { 0 } \right) = m \left( x _ { 0 } \right) , } } \\ { { { } } } & { { { } } } \\ { { \nu ^ { \prime } ( x ) = g \left( x , \nu \left( x \right) \right) , } } & { { { } } } \\ { { { } } } & { { { } } } \end{array}
$$

since the defect is $\pm ~ 1 / n$ . Finally， because of $m \left( x _ { 0 } \right) \leq u \left( x _ { 0 } \right)$ and uniqueness we have $w \left( x \right) \leq \nu \left( x \right)$ .Passing to the limit $n  \infty$ in (10.16) thus gives $m \left( x \right) \leq u \left( x \right) .$ QED.

A further generalization of Theorem 10.2 is possible if the Lipschitz condition c) is replaced by something nonlinear such as

$$
\left| \left| \begin{array} { l } { f \left( x , \nu \right) - f \left( x , y \right) } \end{array} \right| \right| \ \leq \ \omega ( x , \left\| \nu - y \right\| ) \ .
$$

Then the differential inequality for the error $m \left( x \right)$ is to be compared with the solution of

$$
u ^ { \prime } = \omega ( x , u ) + \delta ( x ) + \eta , \qquad u ( x _ { 0 } ) = \rho , \qquad \eta > 0 .
$$

See Walter (1970), Chap. II, δ11 for more details.

# Estimates using one-sided Lipschitz conditions

As we already observed in Exercice 2 of I.9, and as was known for a long time, much information about the errors can be lost by the use of positive Lipschitz constants $L$ (e.g (9.10), (9.10'), 0r (9.10")) in the estimates (7.16), (7.17), or (7.18). The estimates all grow exponentially with $x$ , even if the solutions and errors decay. Therefore many efforts have been made to obtain better error estimates, as for example the papers Eltermann (1955)， Uhlmann (1957), Dahlquist (1959), and the references therein. We follow with great pleasure the particularly clear presentation of Dahlquist.

Let us estimate the derivative of $m ( x ) = | \downarrow \ \nu ( x ) - y ( x )  |$ with more care than we did in (10.5): for $h > 0$ we have

$$
\begin{array} { r l r } {  { m ( x + h ) = \| \begin{array} { l l } { \nu ( x + h ) - y ( x + h ) \| } & { ( 1 0 . 1 ) } \\ { * ( x ) - y ( x ) + h ( \nu ^ { \prime } ( x ) - y ^ { \prime } ( x ) ) \| } & { + \mathbf { O } ( h ^ { 2 } ) } \end{array}  } } \\ & { \leq } & { \| \begin{array} { l } { \nu ( x ) - y ( x ) + h [ f ( x , \nu ( x ) ) - f ( x , y ( x ) ) ] \| } \\ { * h \ S ( x ) + \mathbf { O } ( h ^ { 2 } ) } \end{array}  } \\ & { } & { + h \delta ( x ) + \mathbf { O } ( h ^ { 2 } ) } \end{array}
$$

by the use of (10.6) and (9.7). Here, we apply the mean value theorem to the function $\boldsymbol { y } + h \boldsymbol { f } \left( \boldsymbol { x } \mathrm { ~ , ~ } \boldsymbol { y } \right)$ and obtain

$$
n \left( x + h \right) \leq \ \left( \operatorname* { m a x } _ { \eta \in \left[ y \left( x \right) , \nu \left( x \right) \right] } \| \ I + h \frac { \partial f } { \partial y } ( x \cdot \eta ) \| \ \right) m \left( x \right) + h \vartheta ( x ) + \mathbf { O } ( h ^ { 2 } )
$$

and finally for $h > 0$

$$
\frac { m \left( x + h \right) - m \left( x \right) } { h } \leq \operatorname* { m a x } _ { \mathfrak { N } ^ { \mathfrak { c } } \left[ y \left( x \right) , \nu \left( x \right) \right] } \frac { \parallel I + h \frac { \partial f } { \partial y } ( x , \mathfrak { N } ) \parallel - 1 } { h } m \left( x \right)
$$

The expression on the right hand side of (10.18) leads us to the following definition:

Definition 10.4. Let $Q$ be a square matrix, then we call

$$
\mu ( Q ) = \operatorname* { l i m } _ { h  0 , h > 0 } { \frac { \parallel I + h Q \parallel - 1 } { h } }
$$

the logarithmic norm of $Q$ ·

Following are formulas for its computation (Dahlquist (1959), p.11, Eltermann (1955), p.498,499):

Theorem 10.5. The logarithmic norm (10.19) is obtained by the fol-lowing formulas: for the Euclidean norm (9.6),

$$
\begin{array} { c l } { { \displaystyle \mu ( Q ) = \lambda _ { \mathrm { m a x } } = } } & { { { \displaystyle l a r g e s t ~ e i g e n \nu a l u e ~ o f ~ { \displaystyle \frac { 1 } { 2 } } ( Q ^ { T } + Q ) ~ } . } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { o r } ~ t h e ~ m a x - n o r m ~ ( 9 . \delta ^ { \prime } ) , } } \\ { { \displaystyle \mu ( Q ) = \operatorname* { m a x } _ { k } \left( q _ { k k } ~ + \sum _ { i \neq k } | q _ { k i } | \right) ~ . } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \displaystyle o r ~ t h e ~ n o r m ~ ( 9 . \delta ^ { \prime \prime } ) , } } \\ { { \displaystyle \mu ( Q ) = \operatorname* { m a x } _ { i } \left( q _ { i i } ~ + \sum _ { k \neq i } | q _ { k i } | \right) ~ . } } \end{array}
$$

Proofs: (10.20') and $( 1 0 . 2 0 ^ { \circ } )$ ） follow quite trivially from (9.11') and (9.11") and the definition (10.19). The point is that the presence of $_ { I }$ suppresses, for $h$ sufficiently small, the absolute values for the

diagonal elements. (10.20) is seen from the fact that the eigenvalues of

$$
\left( I + h Q \right) ^ { T } \left( I + h Q \right) = I + h \left( \boldsymbol { Q } ^ { T } + \boldsymbol { Q } \right) + h ^ { 2 } \boldsymbol { Q } ^ { T } \boldsymbol { Q } \mathrm { ~ , ~ }
$$

for $h  ~ 0$ ， converge to $1 + h \wedge _ { i }$ ，where $\lambda _ { i }$ are the eigenvalues of $Q ^ { T } + Q$ . QED.

Remark: For complex-valued matrices the above formulas become

$$
\begin{array} { r l } & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \quad \underset { i } { \mathrm { l a r g e s t ~ e i g e n v a l u e ~ o f } } \quad \frac { 1 } { 2 } ( \boldsymbol { \mathcal { Q } } ^ { * } + \boldsymbol { \mathcal { Q } } ) \ , } \\ & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \underset { k } { \mathrm { m a x } } \left( \mathrm { R e } q _ { k k } + \underset { i \neq k } { \sum } \vert q _ { k i } \vert \right) \ , } \\ & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \underset { i } { \mathrm { m a x } } \left( \mathrm { R e } q _ { i i } + \underset { k \neq i } { \sum } \vert q _ { k i } \vert \right) \ . } \end{array}
$$

We now obtain from (10.18) the following improvement of Theorem 10.3.

Theorem 10.6. Suppose that we have the estimates

$$
\begin{array} { r l } { \mathbb { i } \left\lfloor \frac { \mathcal { I } _ { f } } { \partial y } ( x , \eta ) \right\rfloor } & { \leq \ l ( x ) \quad f o r \quad \eta \in \left[ \mathrm { y } \left( x \right) , \nu \left( x \right) \right] \quad \mathrm { a n d } \quad } & { \mathrm { ( f ) } } \\ { \Big \| \nu ^ { \prime } ( x ) - f \left( x , \nu \left( x \right) \right) \Big \| } & { \leq 8 \left( x \right) , \ \Big \| \ \nu \left( x _ { 0 } \right) - y \left( x _ { 0 } \right) \Big \| } & { \leq \mathrm { p } \ . } \\ { T h e n f o r x > x _ { 0 } \ w e \ h a v e } \\ { \Big \| \ y \left( x \right) - \nu \left( x \right) \Big \| } & { \leq \ e ^ { L \left( x \right) } \bigg ( \mathrm { p } + \displaystyle \int _ { x _ { 0 } } ^ { x } e ^ { - L \left( s \right) } \delta ( s ) d s \bigg ) \ , \qquad \mathrm { ( f ) } } \\ { \quad \times \Big \| \ h \ \mathscr { L } \left( x \right) - \displaystyle \int _ { x _ { 0 } } ^ { x } \Big \vert \left( s \right) d s \ . } \end{array}
$$

Proof: Since, for a fixed $x$ , the interval $[ \nu \left( x \right) , y \left( x \right) ]$ is compact,

$$
K \ = \mathrm { m } \underset { i } { \mathrm { a x } } \ \underset { [ v ( x ) , y ( x ) ] } { \mathrm { m a x } } \ | \ \frac { \partial f _ { i } } { \partial y _ { i } } |
$$

is finite. Then (see the proof of Theorem 10.5)

$$
{ \frac { \parallel I + h { \frac { \partial f } { \partial y } } ( x , \cdot \mathsf { \bar { n } } ) \parallel - 1 } { h } } = \mu { \frac { \partial f } { \partial y } } ( x , \cdot \mathsf { \bar { n } } ) ) + \mathbf { O } ( h )
$$

where the $\mathbb { O } ( h )$ -term is uniformly bounded in $\eta$ (For the norms $\left( 9 . 6 ^ { \prime } \right)$ and $\left( 9 . 6 ^ { \circ \mathfrak { V } } \right)$ this term is in fact zero for $h < 1 / K$ ). Thus the condition (10.21) inserted into (10.18) gives

$$
D _ { + } m \left( x \right) \leq l ( x ) m \left( x \right) + \ S ( x ) .
$$

Now the estimate (10.22) follows in the same way as that of Theorem 10.3. QED.

# Exercises

1. Apply Theorem 10.5 to the example of Exercise 2 of I.9. Observe the substantial improvement of the estim ates.

2. Prove the following (a variant form of the famous "Gronwall lemma", Gronwall(1919)): suppose that a positive function $m \left( x \right)$ satisfies

$$
m \left( x \right) \leq \textsf { p } + \epsilon ( x - x _ { 0 } ) + L \intop _ { x _ { 0 } } ^ { x } m \left( s \right) d s \ = : w \left( x \right)
$$

then

$$
m \left( x \right) \leq \mathsf { p } e ^ { L \left( x - x _ { 0 } \right) } + \frac { \epsilon } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) ;
$$

a) directly, by subtracting from (10.23)

$$
u \left( x \right) = \rho + \epsilon ( x - x _ { 0 } ) + L \intop _ { x _ { 0 } } ^ { x } u \left( s \right) d s \ ;
$$

b) by differentiating $w \left( x \right)$ in (10.23) and using Theorem 10.1.

c) Prove Theorem 10.2 with the help of the above lemma of Gronwall. The same interrelations are, of course, also valid in more general situations.

3. Observe, using an example of the form

$$
y _ { 1 } ^ { \prime } = y _ { 2 } ~ , ~ y _ { 2 } ^ { \prime } = - y _ { 1 } ~ ,
$$

that a generalization of Theorem 10.1 to systems of first order differential equations, with inequalities interpreted componentwise, is not true in general (Muller (1926)).

However, it is possible to prove such a generalization of Theorem 10.1under the additional hypothesis that the functions $g _ { i } ( x , y _ { 1 } , \ldots , y _ { n } )$ are quasimonotone, i.e. that

$$
\begin{array} { r l } & { g _ { i } ( x , y _ { 1 } , \dotsc , y _ { j } , \dotsc , y _ { n } ) \leq g _ { i } ( x , y _ { 1 } , \dotsc , z _ { j } , \dotsc , y _ { n } ) } \\ & { \qquad \mathrm { i f } \quad y _ { j } < z _ { j } \qquad \mathrm { f o r ~ a l l } \quad j \neq i \ . } \end{array}
$$

Try to prove this.

An important fact is that many systems from parabolic differential equations, such as Equation (6.10)， are quasimonotone. This

allows many interesting applications of the ideas of this section (see Walter (1970), Chapter IV).

4. Prove the following properties of the logarithmic norm

$$
\begin{array} { r l } & { \mathrm { a ) } \quad \mu ( \alpha Q ) = \alpha \mu ( Q ) \ \mathrm { f o r ~ \alpha ~ \geq ~ 0 ~ } } \\ & { \mathrm { b ) } \quad - \parallel \mathcal { Q } \parallel \leq \ \mu ( Q ) \leq \parallel \mathcal { Q } \parallel } \\ & { \mathrm { c ) } \quad \mu ( Q + P ) \leq \hslash ( Q ) + \mu ( P ) \ , \quad \mu ( \int Q \left( t \right) d t ) \leq \int \mu ( Q \left( t \right) ) d t } \\ & { \mathrm { d ) } \quad \left| \mu ( Q ) - \mu ( P ) \right| \leq \parallel Q - P \parallel } \end{array}
$$

5. For the Euclidean norm (10.20), $\mu ( Q )$ is the smallest number satisfying

$$
< \nu , Q \nu > \leq \mu ( Q ) \parallel \nu \parallel ^ { 2 } .
$$

This property is valid for all norms associated with a scalar product. Prove this.

6. Show that for the Euclidean norm the condition (10.21） is equivalent to

$$
< y - z \mathrm { , ~ } f ( x \mathrm { , ~ } y ) - f ( x \mathrm { , ~ } z ) > \leq l ( x \mathrm { ) | | ~ } y - z \mathrm { ~ | | ~ } ^ { 2 } \mathrm { ~ . ~ }
$$

# 1.11. Systems of linear differential equations

With more knowledge about existence and uniqueness, and with more ability in linear algebra, we shall now, as did the mathematicians of the 19th century, better understand many points which had been left a litte mysterious in Sections I.4 and I.6 about linear differential equations of higher order.

Equation (4.9) divided by $\boldsymbol { a } _ { 0 } ( \boldsymbol { x } )$ (which is $\neq 0$ away from singular points) becomes

$$
y ^ { ( n ) } + a _ { 1 } ( x ) y ^ { ( n - 1 ) } + \cdot \cdot \cdot + a _ { n } ( x ) y = f \left( x \right) .
$$

Introducing $y = y _ { 1 } , y ^ { \prime } = y _ { 2 } , . . . , y ^ { ( n - 1 ) } = y _ { n }$ we ariveat

$$
( \begin{array} { c } { { y _ { 1 } ^ { \prime } } } \\ { { y _ { 2 } ^ { \prime } } } \\ { { \vdots } } \\ { { y _ { n } ^ { \prime } } } \end{array} ) = ( \begin{array} { c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { 0 } } & { { } } & { { } } & { { } } \\ { { } } & { { \vdots } } & { { \ddots } } & { { \vdots } } & { { } } \\ { { - a _ { n } ( x ) } } & { { - a _ { n - 1 } ( x ) } } & { { \cdots } } & { { - a _ { 1 } ( x ) } } \end{array} ) ( \begin{array} { c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \\ { { \vdots } } \\ { { y _ { n } } } \end{array} ) + ( \begin{array} { c } { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \\ { { f ( x ) } } \end{array} ) \begin{array} { c } { { x _ { 1 } } } \\ { { y _ { 2 } } } \\ { { f _ { 1 } } } \end{array} ) .
$$

We again denote by y the vector $( y _ { 1 } , \dots , y _ { n } ) ^ { I }$ and by $f \left( x \right)$ the inhomogeneity,sothat (11.1)becomesaspecial caseof thefollowing sy tem of linear differential equations

$$
y ^ { \prime } = A \left( x \right) y + f \left( x \right) ,
$$

$$
A \left( x \right) = ( a _ { i j } ( x ) ) , f \left( x \right) = ( f _ { i } ( x ) ) , i , j = 1 , \ldots , n .
$$

Here, the theorems of Section I.9 and I.10 apply without difficulty. Since the partial derivatives of the right hand side of (11.2) with respect to $y _ { i }$ are given by $a _ { k i } ( x )$ , we have the Lipschitz estimate (see Condition c) of the variant form of Theorem 10.2)， where $l ( x ) = \parallel A \left( x \right) \parallel$ in any subordinate matrix norm (9.11, $1 1 ^ { \circ }$ , 11"). We apply Theorem 7.4， and the variant form of Theorem 10.2 with $\nu \left( x \right) = 0$ as "approximate solution". We may also take $l ( x ) = \mu ( A \left( x \right) )$ (see $( 1 0 . 2 2 , 2 2 ^ { \prime } , 2 2 ^ { \prime \prime } )$ ） and apply Theorem 10.6.

Theorem 11.1. Suppose that A $( x$ ) is continuous on an interval $[ x _ { 0 } , X ]$ Then for any initial values $y _ { 0 } = ( y _ { 1 0 } , \ldots , y _ { n 0 } ) ^ { T }$ there exists for au $x _ { 0 } \leq x \leq X$ a unique solution of (11.2) satisfying

$$
\begin{array} { r } { \|  { y } ( x ) \| \ \le \ e ^ { L \left( x \right) } \bigg [ \|  { y } _ { 0 } \| + \displaystyle \int _ { x _ { 0 } } ^ { x } e ^ { - L \left( s \right) } \|  { f } ( s ) \| \ d s \bigg ] } \end{array}
$$

$$
L \left( x \right) = \int _ { x _ { 0 } } ^ { x } l ( s ) d s , l ( x ) = \mid \mid A \left( x \right) \mid \mid \quad o r l ( x ) = \mu ( A \left( x \right) ) .
$$

For $f \left( x \right) { \equiv } 0$ ， $y \left( x \right)$ depends linearly on the initial values, i.e. there is a matrix $R$ $( x , x _ { 0 } )$ (the "resolvent"), such that

$$
y ( x ) = R ( x , x _ { 0 } ) y _ { 0 } .
$$

Proof: Since $l ( x )$ is continuous and therefore bounded on any compact interval $[ x _ { 0 } , X ]$ , the estimate (11.3) shows that the solutions can be continued until the end. The linear dependence follows from the fact that, for $f \equiv 0$ ， linear combinations of solutions are again solutions, and from uniqueness. QED.

Also from uniqueness we have that the solutions with initial values $y _ { 0 }$ at $ { { \varepsilon } } _ { 0 }$ and ${ \boldsymbol { y } } _ { 1 } = { \boldsymbol { R } }$ $( x _ { \mathit { \mathrm { ~ 1 ~ } } } , x _ { \mathit { \mathrm { ~ 0 ~ } } } ) y _ { \mathit { \mathrm { ~ 0 ~ } } }$ at $x _ { 1 }$ must be the same. Hence we have

$$
\begin{array} { r } { R \left( x _ { 2 } , x _ { 0 } \right) = R \left( x _ { 2 } , x _ { 1 } \right) R \left( x _ { 1 } , x _ { 0 } \right) } \end{array}
$$

for $x _ { 0 } { \le } x _ { 1 } { \le } x _ { 2 }$ . Finally by integrating backward from $x _ { 1 } , y _ { 1 } ,$ i.e. by the coordinate transformation ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 1 } - t$ ， $0 \leq t \leq x _ { 1 } - x _ { 0 } ,$ we must arrive, again by uniqueness, at the starting values. Hence

$$
\textit { R } ( x _ { 0 } , x _ { 1 } ) = \left( \boldsymbol { R } \left( x _ { 1 } , x _ { 0 } \right) \right) ^ { - 1 }
$$

and (11.5) is true in general.

# The Wronskian

Let $y _ { i } ( x ) = ( y _ { 1 i } ( x ) , \ldots , y _ { n i } ( x ) ) ^ { t } ( i = 1 , \ldots , n )$ be a set of n solu-tions of the homogeneous differential equation

$$
y ^ { \prime } = A \left( x \right) y
$$

which are linearly independent at $\boldsymbol { x } - \boldsymbol { x } _ { \textup { \scriptsize 0 } }$ (i.e., they form a fundamental system). We form the W ronskian matrix (Wronski (1810))

$$
W \left( x \right) = \left( \begin{array} { c c } { { y _ { 1 1 } ( x ) } } & { { \ldots } } & { { y _ { 1 n } ( x ) } } \\ { { } } & { { } } \\ { { \vdots } } & { { } } \\ { { y _ { n 1 } ( x ) } } & { { \ldots } } & { { y _ { n n } ( x ) } } \end{array} \right) ,
$$

so that

$$
W ^ { \prime } ( x ) = A \left( x \right) W \left( x \right)
$$

and all solutions can be written as

$$
c _ { 1 } y _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } y _ { n } ( x ) = W \left( x \right) \cdot c \mathrm { ~ w h e r e ~ } c = \left( c _ { 1 } ^ { } , \cdot \cdot \cdot , c _ { n } ^ { } \right) ^ { T } .
$$

If this solution must satisfy the initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ , we obtain $c = W ^ { - 1 } ( x _ { 0 } ) y _ { 0 }$ and we have the formula

$$
R \left( x , x _ { 0 } \right) = W \left( x \right) W ^ { - 1 } ( x _ { 0 } ) \ .
$$

Therefore all solutions are known if one has found n linearly independent solutions. For their construction, however, nearly nothing is known for general non-constant A $( x )$ ·

# The Abel-Liouville-Jacobi-Ostrograds kii identity

We already know from (11.6) that $W \left( x \right)$ remains regular for all $x$ . We now show that the determinant of $W \left( x \right)$ can be given explicitly as follows (Abel (1827), Liouville (1838), Jacobi (1845), \$17):

$$
\operatorname* { d e t } ( W \left( x \right) ) = \operatorname* { d e t } ( W \left( x _ { 0 } \right) ) \cdot \exp \left( \int _ { x _ { 0 } } ^ { x } { T r \left( A \left( s \right) \right) d s } \right) \mathrm { ~ , ~ }
$$

$$
T r ( A { \bf \Psi } ( x ) ) = a _ { 1 1 } ( x ) + a _ { 2 2 } ( x ) + \cdot \cdot \cdot + a _ { n n } ( x )
$$

which connects the determinant of $W \left( x \right)$ to the trace of A .

${ \frac { d } { d x } } \operatorname* { d e t } ( W \left( x \right) )$ $\operatorname* { d e t } ( W \left( x \right) )$ the Leibniz rule) is a sum of $n$ terms, whose first is

$$
T _ { 1 } = \operatorname* { d e t } { \left( \begin{array} { l l l l } { y _ { 1 1 } ^ { \prime } } & { y _ { 1 2 } ^ { \prime } } & { \cdots } & { y _ { 1 n } ^ { \prime } } \\ { y _ { 2 1 } } & { y _ { 2 2 } } & { y _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { y _ { n 1 } } & { y _ { n 2 } } & { \cdots } & { y _ { n n } } \end{array} \right) } ~ .
$$

We insert $y _ { 1 i } ^ { \prime } { = } a _ { 1 1 } y _ { 1 i } { + } \cdot \cdot \cdot { + } a _ { 1 n } y _ { n i }$ from (117). All terms ${ a _ { 1 2 } y _ { 2 i } }$ ， $\dots , a _ { 1 n } y _ { n i }$ disappear by subtracting multiples of lines 2 to $n$ , so that $\boldsymbol { T } _ { 1 } { ^ { = } } \boldsymbol { a } _ { 1 1 } \mathrm { d e t } ( \boldsymbol { W } \left( \boldsymbol { x } \right) )$ . Summing all these terms we obtain finally

$$
{ \frac { d } { d x } } \mathrm { d e t } ( W ( x ) ) = ( a _ { 1 1 } ( x ) + \cdot \cdot \cdot + a _ { n n } ( x ) ) \cdot \mathrm { d e t } ( W ( x ) )
$$

and (11.10) follows by integration. QED.

# Inhomogeneous linear equations

Extending the idea of Joh. Bernoulli for (3.2) and Lagrange for (4.9),we now compute the solutions of the inhomogeneous equation (11.2) by leting c be "variable" in the "general solution" (11.8): ${ \boldsymbol { y } } \left( { \boldsymbol { x } } \right) = { \boldsymbol { W } } \left( { \boldsymbol { x } } \right) { \boldsymbol { c } } \left( { \boldsymbol { x } } \right)$ (Liouville (1838)). Exactly as in Section I.3 for (3.2) we obtain from (11.2) and (11.7) by differentiation

$$
y ^ { \prime } = W ^ { \prime } c + W c ^ { \prime } = A W c + W c ^ { \prime } = A W c + f . 
$$

Hence $c ^ { \prime } { = } W ^ { - 1 } f$ . If we integrate this with integration constants $c$ ，we obtain

$$
y \left( x \right) = W \left( x \right) \intop _ { x _ { 0 } } ^ { x } { W \left( { s } \right) f \left( { s } \right) d s + W \left( x \right) \cdot c } .
$$

The initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ imply $c = W ^ { - 1 } ( x _ { 0 } ) y _ { 0 }$ and we obtain:

Theorem 11.2. ("Variation of constants formula"). Let A $\mathbf { \Psi } ( x \mathbf { \Psi } )$ and $f \left( x \right)$ be continuous. Then the solution of the inhomogeneous equation $y ^ { \prime } { = } A \left( x \right) y + f \left( x \right)$ satisfying the initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ is given by

$$
\begin{array} { l } { { \displaystyle y \left( x \right) = W \left( x \right) \left[ W ^ { - 1 } ( x _ { 0 } ) y _ { 0 } + \displaystyle \int W ^ { - 1 } ( s ) f \left( s \right) d s \right] } } \\ { { \displaystyle x _ { 0 } } } \\ { { \displaystyle = R \left( x , x _ { 0 } \right) y _ { 0 } + \int R \left( x , s \right) f \left( s \right) d s } } \\ { { \displaystyle x _ { 0 } } } \end{array} .
$$

# Exercises

1. Compute the resolvent matrix R $( x \mathrm { ~ , ~ } x _ { \mathrm { ~ 0 ~ } } )$ for the systems

$$
\begin{array} { c c c } { { \mathrm { a ) } } } & { { { \begin{array} { l } { y _ { 1 } ^ { \prime } = y _ { 1 } } \\ { y _ { 2 } ^ { \prime } = 3 y _ { 2 } } \end{array} } } } & { { \begin{array} { l } { { \mathrm { b ) } } } \end{array} } } & { { { \begin{array} { l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } \\ { { y _ { 2 } ^ { \prime } = - y _ { 1 } } } \end{array} } } } \end{array}
$$

and check the validity of (11.5), (11.6) as well as (11.10).

2. Reconstruct Abel's original proof for (11.10), which was for the case

$$
y _ { 1 } ^ { \prime \prime } + p y _ { ~ 1 } ^ { \prime } + q y _ { 1 } = 0 ~ , ~ y _ { 2 } ^ { \prime \prime } + p y _ { ~ 2 } ^ { \prime } + q y _ { 2 } = 0 ~ ;
$$

multiply the equations by $y _ { 2 }$ and $y _ { 1 }$ respectively and subtract to

eliminate $q$ . Then integrate. Use the result to obtain an identity for the two integrals

$$
y _ { 1 } ( a ) = \int _ { 0 } ^ { \infty } e ^ { a x - x ^ { 2 } } x ^ { \alpha - 1 } d x , { } ~ y _ { 2 } ( a ) = \intop e ^ { - a x - x ^ { 2 } } x ^ { \alpha - 1 } d x ,
$$

which both satisfy

$$
\frac { d ^ { 2 } y _ { i } } { d a ^ { 2 } } - \frac { a } { 2 } \frac { d y _ { i } } { d a } - \frac { { \bf a } } { 2 } y _ { i } = 0 { . }
$$

Hint: To verify (11.13), integrate from 0 to infinity the expression for ${ \frac { d } { d x } } ( \exp ( a x - x ^ { 2 } ) x ^ { \alpha } )$ (Abel (1827), case IV).

3. (Kummer (1839)). Show that the general solution of the equation

$$
{ \bf \chi } _ { y } ^ { ( n ) } ( x ) = x ^ { m } y ( x )
$$

can be obtained by quadrature.

Hint: Differentiate (11.14) to obtain

$$
y ^ { \left( n + 1 \right) } = x ^ { m } y ^ { \prime } + m x ^ { m - 1 } y .
$$

Suppose by recursion that the general solution of

$$
\Psi ^ { ( n + 1 ) } = x ^ { m - 1 } \Psi ~ , ~ \mathrm { i . e . } ~ \frac { d ^ { n + 1 } } { d x ^ { n + 1 } } \Psi ( x u ) = x ^ { m - 1 } u ^ { m + n } \Psi ( x u )
$$

is already known. Show that then

$$
y \left( x \right) = \intop _ { 0 } ^ { \infty } u ^ { m - 1 } \mathrm { e x p } \biggl ( - \begin{array} { c } { { u ^ { m + n } } } \\ { { m + n } } \end{array} \biggr ) \psi ( x u ) d x
$$

is the general solution of (11.15), and, under some conditions on the parameters,also of (11.14). To simplify the computations, consider the function

$$
g ( u ) = u ^ { m } \exp \bigg ( - \frac { u ^ { m + n } } { m + n } \bigg ) \Psi ( x u ) \ ,
$$

compute its derivative with respect to $\boldsymbol { \mu }$ ，multiply by $x ^ { m - 1 }$ ,and integrate from O to infinity.

4. (Weak singularities for systems). Show that the linear system

$$
y ^ { \prime } = { \frac { 1 } { x } } \biggl ( A _ { \ 0 } + A _ { \ 1 } x + A _ { \ 2 } x ^ { 2 } + \cdots \biggr ) y
$$

possesses solutions of the form

$$
y ( x ) = x ^ { \mathsf { p } } \biggl ( \nu _ { 0 } + \nu _ { 1 } x + \nu _ { 2 } x ^ { 2 } + \cdot \cdot \cdot \biggr )
$$

where $\nu _ { 0 }$ ， $\nu _ { \textrm { 1 } } , .$ . are vectors. Determine first p and ${ \boldsymbol \nu } _ { 0 }$ ,then recursively $\nu _ { 1 } , \nu _ { 2 }$ ， etc. Observe that there exist $n$ independent solutions of the form (11.18) if the eigenvalues of $\textit { A } _ { 0 }$ satisfy $\lambda _ { i } \neq \lambda _ { j }$ mod(Z) (Fuchs (1866)).

5. Find the general solution of thc weakly singular systems

$$
y ^ { \prime } = { \frac { 1 } { x } } \left( { \frac { 3 } { 4 } } \quad 1 \right) \quad \quad \mathrm { a n d } \quad \quad y ^ { \prime } = { \frac { 1 } { x } } \left( { \begin{array} { l l } { { { \frac { 3 } { 4 } } } } & { { 1 } } \\ { { } } & { { } } \\ { { { \frac { 1 } { 4 } } } } & { { - { \frac { 1 } { 4 } } } } \end{array} } \right) \quad y \quad \quad \mathrm { a n d } \quad \quad y ^ { \prime } = { \frac { 1 } { x } } \left( { \begin{array} { l l } { { { \frac { 3 } { 4 } } } } & { { 1 } } \\ { { } } & { { } } \\ { { - { \frac { 1 } { 4 } } } } & { { - { \frac { 1 } { 4 } } } } \end{array} } \right) \quad y \enspace .
$$

Hint: While the first is easy from Exercise 4, the second needs an additional idea (see Formula (5.6)). A second possibility is to use the transformation $x = e ^ { t } , y \left( x \right) = z \left( t \right)$ ， and apply the methods of Section I.12.

# 1.12. Systems with constant coefficients

"Die Technik der Integration der linearen Differentialgleichungen mit constanten Coeffzienten wird hier auf das Hochste entwickelt."   
(F. Klein in Routh (1898))

# Linearization

Systems of linear differential equations with constant coefficients form a class of equations for which the resolvent $R$ $( x , x _ { 0 } )$ can be computed explicitly. They generally occur by linearization of timeindependent (i.e. autonomous or permanent) nonlinear differential equations

$$
y _ { i } ^ { \prime } = f _ { i } ( y _ { 1 } , . . . , y _ { n } ) \quad { \mathrm { ~ o r ~ } } \quad y _ { i } ^ { \prime \prime } = f _ { i } ( y _ { 1 } , . . . , y _ { n } )
$$

in the neighbourhood of a stationary point (Lagrange (1788), see also Routh (1860), Chap.IX, Thomson and Tait (1879)). We choose the coordinates so that the stationary point under consideration is the origin, i.e. ${ f _ { i } } ( 0 , \dots , 0 ) { = } 0$ . We then expand $f _ { i }$ in its Taylor series and neglect all nonlinear terms:

$$
y _ { i } ^ { \prime } = \sum _ { k } { \frac { \partial f _ { i } } { \partial y _ { k } } } ( 0 ) y _ { k } \qquad { \mathrm { o r } } \quad y _ { i } ^ { \prime \prime } = \sum _ { k } { \frac { \partial f _ { i } } { \partial y _ { k } } } ( 0 ) y _ { k } ~ .
$$

This is a system of equations with constant coefficients, as introduced in Section I.6 (see (6.3), (6.11)),

$$
y ^ { \prime } = A y \qquad { \mathrm { o r } } \quad y ^ { \prime \prime } = A y .
$$

Autonomous systems are invariant under a shift $x \to x + C$ . We may therefore always assume that ${ { x } _ { 0 } } \mathrm { { = } } 0$ . For arbitrary $\boldsymbol { \mathscr { x } } _ { \mathrm { ~ 0 ~ } }$ the resolvent is given by

$$
R \left( x , x _ { 0 } \right) = R \left( x - x _ { 0 } , 0 \right) .
$$

# Diagonalization

We have seen in Section I.6 that the assumption $y \left( x \right) = y \cdot e ^ { \lambda x }$ leads to

$$
A \nu = \lambda \nu \qquad \mathrm { o r } \quad A \nu = \lambda ^ { 2 } \nu ,
$$

hence $\nu \neq 0$ must be an eigenvector of A and λ the corresponding eigenvalue (in the first case; a square root of the eigenvalue in the

second case, which we do not consider any longer). From (12.3) we obtain by subtraction that there exists such a $\nu \neq 0$ if and only if the determinant

$$
\chi _ { A } \left( \lambda \right) : = { \mathrm { d e t } } ( \lambda I - A { \bf \Gamma } ) = \left( \lambda - \lambda _ { 1 } \right) \left( \lambda - \lambda _ { 2 } \right) \cdot \cdot \cdot \left( \lambda - \lambda _ { n } \right) = 0 ~ .
$$

This determinant is called the characteristic polynomial of A .

Suppose now that for the n eigenvalues $\lambda _ { i }$ the n eigenvectors $\nu _ { i }$ can be chosen linearly independent. We then have from (12.3)

$$
A \left( \nu _ { 1 } \nu _ { 2 } \cdots \nu _ { n } \right) = \left( \nu _ { 1 } \nu _ { 2 } \cdots \nu _ { n } \right) \mathrm { d i a g } \left( \mathsf { \boldsymbol { k } } _ { 1 } , \mathsf { \boldsymbol { k } } _ { 2 } , \ldots , \mathsf { \boldsymbol { k } } _ { n } \right) ,
$$

or,if $T$ is the matrix whose columns are the eigenvectors of A ，

$$
\begin{array} { r } { T ^ { - 1 } A T \ = \ \mathrm { d i a g } \biggl ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { n } \biggr ) \ . } \end{array}
$$

On com paring (12.5） with $( 1 2 . 1 ^ { , 3 9 } )$ ， we see that the differential equation sim plifies considerably if we use the coordinate transformation

$$
y \left( x \right) = T z \left( x \right) , \qquad y ^ { \prime } ( x ) = T z ^ { \prime } ( x )
$$

which leads to

$$
z ^ { \prime } ( x ) = \mathrm { d i a g } \left( \mathbb { \lambda } _ { 1 } , \lambda _ { 2 } , \ldots , \mathbb { \lambda } _ { n } \right) z \left( x \right) \ .
$$

Thus the original system of differential equations decomposes into n single equations which are readily integrated to give

$$
z ( x ) = \mathrm { d i a g } \Big ( \exp ( \mathsf { \boldsymbol { \lambda } } _ { 1 } x ) , \exp ( \mathsf { \boldsymbol { \lambda } } _ { 2 } x ) , \ldots , \exp ( \mathsf { \boldsymbol { \lambda } } _ { n } x ) \Big ) \ z _ { 0 } \ ,
$$

from which (12.6), yields

$$
y \left( x \right) = T \mathrm { d i a g } \biggl ( \exp ( \mathsf { \mathsf { A } } _ { 1 } x ) , \exp ( \mathsf { \mathsf { A } } _ { 2 } x ) , \ldots , \exp ( \mathsf { \mathsf { A } } _ { n } x ) \biggr ) T ^ { - 1 } y _ { 0 } .
$$

# The Schur decomposition

"Der Beweis ist leicht zu erbringen". (Schur, 1909)

The foregoing theory， beautiful as it may appear， has several drawbacks:

a) Not all $n \times n$ matrices have a set of n linearly independent eigenvectors;

b) Even if it is invertible, the matrix T can behave very badly (see Exercise 1).

However， for symmetric matrices a classical theory tells that A can always be diagonalized by orthogonal transformations. Let us therefore, with Schur (1909), extend this classical theory to non-symmetric matrices. A real matrix $\boldsymbol { Q }$ is called orthogonal if its column vectors are pair-wise orthogonal and of norm 1, i.e. if $Q ^ { T } Q = I$ or $Q ^ { T } = Q ^ { - 1 }$ A complex matrix $Q$ is called unitary if $Q ^ { \ast } Q = I$ or ${ Q } ^ { * } { = } { Q } ^ { - 1 }$ ,where $Q ^ { * }$ is the adjoint matrix of $Q$ , i.e. transposed and complex conjugate.

# Theorem 12.1.

a) (Schur). For each complex matrix A there exists a unitary matrix $Q$ such that

$$
\varrho ^ { * } A Q \ = \left( \begin{array} { c c c } { { \star _ { 1 } \times \hfill } } & { { \times \hfill } } & { { \times \hfill } } \\ { { } } & { { } } & { { \ddots \hfill } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \ddots \hfill } } & { { \hfill } } \\ { { } } & { { } } & { { \ddots \hfill } } \\ { { } } & { { } } & { { } } \end{array} \right) \ ;
$$

b) (Wintner-Murnaghan (1931)). For a real matrix A the matrix $Q$ can be chosen real and orthogonal, if for each pair of conjugate eigenvalues λ, $\stackrel { \_ } { \lambda } = \alpha \pm \textit { i } \beta$ one allows the block

$$
\left( \begin{array} { c c } { { \lambda } } & { { \times } } \\ { { } } & { { \overline { { { \lambda } } } } } \end{array} \right) \qquad t o \ b e \ r e p l a c e { d \ b y } \qquad \left( \begin{array} { c c } { { \times } } & { { \times } } \\ { { \times } } & { { \times } } \end{array} \right) \ .
$$

Proof: a) The matrix A has at least one eigenvector with eigenvalue $\lambda _ { 1 }$ . We use this (normalized) vector as the first column of a matrix $Q _ { 1 }$ . Its other columns are then chosen by arbitrarily completing the first one to an orthonormal basis. Then

$$
A Q _ { 1 } = Q _ { 1 } \left( { \brace { - - { \frac { 1 } { \imath } } \dots { - } \dots } ^ { \vdots \ddots \cdot x _ { n } } } \right) \ .
$$

We then apply the same argument to the $( n - 1 )$ -dimensional matrix A . This leads to

$$
\tilde { A } \tilde { \mathcal { Q } } _ { 2 } = \tilde { \mathcal { Q } } _ { 2 } \left( \left. \begin{array} { l l l l } { \lambda _ { 2 } | \times } & { \cdot \cdot \cdot } & { \times } \\ { - \frac { 1 } { 2 } | } & { \cdot \cdot \cdot } & { - \cdot } \\ { \phantom { - } | \times } & { \cdot \cdot \cdot } & { \times } \\ { 0 } & { | } & { \vdots } & { } \\ { \phantom { - } | } & { \cdot \cdot } & { \times } \end{array} \right| \right) \enspace .
$$

With the unitary matrix

$$
\boldsymbol { Q } _ { 2 } = \left( \begin{array} { l } { 1 \mathrm { ~ i ~ } 0 } \\ { - \mathrm { - + -- } } \\ { 0 \mathrm { ~ i ~ } \tilde { \mathcal { Q } } _ { 2 } } \end{array} \right)
$$

we obtain

$$
\mathcal { Q } _ { 1 } ^ { * } A \mathcal { Q } _ { 1 } \mathcal { Q } _ { 2 } = \mathcal { Q } _ { 2 } \left( \frac { \lambda _ { 1 } } { 1 } \begin{array} { l l l l } { * } & { \times \frac { 1 } { 1 } } & { \times } & { \dots } & { \times } \\ & { \lambda _ { 2 } \stackrel { 1 } { \mapsto } 1 \times } & { \dots } & { \times } \\ & { - } & { - } & { \dots } \\ & & { \mid \times } & { \dots } & { \times } \\ { 0 } & { \overset { 1 } { \downarrow } : } & { \vdots } \\ & { \vdots } & & { \ddots } \end{array} \right) .
$$

A continuation of this process leads finally to a triangular matrix as in (12.9) with Q =Q122' @n-1

b) Suppose A to be a real matrix. If $\lambda _ { 1 }$ is real, $\boldsymbol { Q } _ { 1 }$ can be chosen real and orthogonal. Now let $\lambda _ { 1 } = \alpha + i \beta$ （ $\beta \neq 0$ ） be a non-real eigenvalue with a corresponding eigenvector $\mu + i \nu$ ,i.e.

$$
A \left( u \pm i \nu \right) = ( \alpha \pm i \beta ) ( u \pm i \nu )
$$

or

$$
A u \ = \alpha u - \beta \nu , A \nu \ = \ \beta u \ + \alpha \nu ,
$$

Since $\beta \neq 0$ ,u and $\nu$ are linearly independent. We choose an orthogonal basis $\hat { u } ~ , ~ \hat { \nu }$ of the subspace spanned by $\pmb { \mu }$ and $\nu$ and take $\hat { \mu }$ ， $\hat { \nu }$ as the first two columns of the orthogonal matrix $Q _ { 1 }$ .We then have from (12.11')

$$
A Q _ { 1 } = Q _ { 1 } ( | \begin{array} { c c c c } { { \times } } & { { \times \mid \times } } & { { \cdots } } & { { \times } } \\ { { } } & { { \mid } } & { { } } & { { } } \\ { { \times } } & { { \times \mid \times } } & { { \cdots } } & { { \times } } \\ { { - - - \mathrm { 1 } - -- } } & { { - - - - } } & { { - } } \\ { { } } & { { \mid } } & { { \tilde { A } } } & { { } } \end{array} | \quad ,
$$

QED.

Schur himself was not very proud of "his" decomposition, he just derived it as a tool for proving interesting properties of eigenvalues (see e.g. Exercise 2).

Clearly, if A is real and symmetric, $Q ^ { T } A Q$ will also be symmetric, and therefore diagonal (see also Exercise 3).

# N umerical computations

The above theoretical proof is still not of much practical use. It requires that one know the eigenvalues, but the computation of eigenvalues from the characteristic polynomial is one of the bestknown stupidities of numerical analysis. Good numerical analysis turns it the other way round: the real matrix A is directly reduced, first to Hessenberg form， and then by a sequence of orthogonal transformations to the real Schur form of Wintner-Murnaghan ("QRalgorithm" of Francis, coded by Martin-Peters-Wilkinson, contribution Ii/14 in Wilkinson-Reinsch (1970)). The eigenvalues then drop out. However, the produced code, called "HQR2", does not give the Schur form of A ， since it continues for the eigenvectors of A . Some manipulations have therefore to be done to interrupt the code at the right moment (in the FORTRAN translation HQR2 of Eispack (1974), for example, the $" 3 4 0 "$ of statement labelled $" 6 0 "$ has to be replaced by "1001"). Happy "Matlab"-users just call "SCHUR".

Whenever the Schur form has been obtained, the transformation $y \left( x \right) = Q z \left( x \right) ,$ y $\prime ( x ) { = } Q z ^ { \prime } ( x )$ (see (12.6)) leads to

$$
\begin{array} { r } { \left( \begin{array} { c } { z _ { 1 } ^ { \prime } } \\ { \vdots } \\ { z _ { n - 1 } ^ { \prime } } \\ { z _ { n - 1 } ^ { \prime } } \\ { z _ { n } ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c c } { \mathsf { A } _ { 1 } } & { b _ { 1 2 } } & { \cdots } & { b _ { 1 , n - 1 } } & { b _ { 1 n } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { b _ { n - 1 , n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } \end{array} \right) \left( \begin{array} { c } { z _ { 1 } } \\ { \vdots } \\ { z _ { n - 1 } } \\ { z _ { n } } \end{array} \right) . } \end{array}
$$

The last equation here is $z _ { n } ^ { \prime } = \lambda _ { n } z _ { n }$ and can be integrated to give $z _ { n } = \exp ( \lambda _ { n } x ) z _ { n 0 } .$ Next, the equation for $z _ { n - 1 }$ is

$$
z _ { n - 1 } ^ { \prime } = \lambda _ { n - 1 } z _ { n - 1 } + b _ { n - 1 , n } z _ { n }
$$

with $z _ { n }$ known. This is a linear equation (inhomogeneous, if $b _ { n - 1 , n } \neq 0 )$ which can be solved by Euler's method explained in Sec-tion 1.4. Two different cases arise:

$\lambda _ { n - 1 } \neq \lambda _ { n }$ wa put $z _ { n - 1 } { = } E \exp ( \operatorname { \lambda } _ { n - 1 } x ) + F \exp ( \operatorname { \lambda } _ { n } x )$ $F = b _ { n - 1 , n } z _ { n 0 } / ( \lambda _ { n } - \lambda _ { n - 1 } )$ and $\scriptstyle { E = z _ { n - 1 , 0 } - F }$

b）If $\lambda _ { n - 1 } = \lambda _ { n }$ we set $z _ { n - 1 } { = } ( E + F x ) \exp ( \lambda _ { n } x )$ and obtain $F = b _ { n - 1 , n } z _ { n 0 }$ and $E = _ { z _ { n - 1 , 0 } }$

The next stage, following the same ideas， gives $z _ { n - 2 }$ , etc. Simple recursive formulas for the elements of the resolvent, which work in the case $\lambda _ { i } \neq \lambda _ { j } ,$ are obtained as follows (Parlett (1976)): we assume

$$
z _ { i } ( x ) = \sum _ { j = i } ^ { n } E _ { i j } \mathrm { e x p } ( \lambda _ { j } x )
$$

and insert this into (12.12). After comparing coefficients, we obtain for $i = n , n - 1 , n - 2 ,$ etc.

$$
\begin{array} { l l } { { E _ { i k } = \displaystyle \frac { 1 } { \mathsf { k } _ { k } - \mathsf { k } _ { i } } \Biggl ( \sum _ { j = i + 1 } ^ { k } b _ { i j } E _ { j k } \Biggr ) \quad } } & { { k = i + 1 , i + 2 , \cdot \cdot \cdot } } \\ { { E _ { i i } = z _ { i , 0 } - \displaystyle \sum _ { j = i + 1 } ^ { n } E _ { i j } ~ . } } & { { } } \end{array}
$$

The Jordan canonical form "Simpler Than You Thought" (Amer. Math. Monthly 1980)

Whenever one is not afraid of badly conditioned matrices (see Exercise 1),and many mathematicians are not, the Schur form obtained above can be further transformed into the famous Jordan canonical form :

Theorem 12.2. (Jordan (1870), Livre deuxieme, $\ S \ S$ and 6). For every matrix A there exists a non-singular matrix $T$ such that

$$
T ^ { - 1 } { \cal A } T = \mathrm { d i a g } \left\{ \left[ \begin{array} { l l l } { { \lambda _ { 1 } } } & { { 1 } } & { { } } \\ { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { \ddots } } \end{array} \right] , \left[ \begin{array} { l l l } { { \lambda _ { 2 } } } & { { 1 } } & { { } } \\ { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { \ddots } } \\ { { } } & { { } } & { { \lambda _ { 2 } } } \end{array} \right] , \cdots \right\} .
$$

(The dimension of the blocks may vary and the $\lambda _ { i }$ are not necessarily distinct).

Proof (Fletcher-Sorensen (1983)): We may suppose that the matrix is already in the Schur form. This is of course possible in such a way that identical eigenvalues are grouped together on the principal diagonal.

The next step is to remove all nonzero elements outside the upper-triangular blocks containing identical eigenvalues. We demon-strate this on the following example: $\lambda _ { 1 } \neq \lambda _ { 2 }$ and

$$
\begin{array} { r } { A = \left( \begin{array} { c c c } { \lambda _ { 1 } } & { a } & { b } & { c } \\ & { \lambda _ { 1 } } & { d } & { e } \\ & & { \lambda _ { 2 } } & { f } \\ & & & { \lambda _ { 2 } } \end{array} \right) \ . } \end{array}
$$

Our task is to find a transformation matrix such that $b , c , d$ and $e$ disappear; we search for it in the form

$$
\left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { a \stackrel { \mid } { \mid } b } } & { { c } } \\ { { } } & { { \lambda _ { 1 } \stackrel { \mid } { \mid } d } } & { { e } } \\ { { -- -- - \ -- \ \displaystyle \frac { 1 } { 1 } -- \ -- \int } } \\ { { \mid \lambda _ { 2 } } } & { { f } } \\ { { \mid } } & { { \lambda _ { 2 } } } \end{array} \right) \left( \begin{array} { c c c } { { \mid p } } & { { q } } \\ { { I \mid } } & { { r } } \\ { { -- - \ \displaystyle \frac { 1 } { 0 } - \ -- \ } } \\ { { 0 \stackrel { \mid } { \mid } \ - \ \displaystyle \frac { 1 } { I } } I } \end{array} \right) = \left( \begin{array} { c c c } { { \mid p \ q } } \\ { { I \mid } } & { { r \ q } } \\ { { - - \ -- \ \mid r } } & { { s } } \\ { { 0 \mid \stackrel { \mid } { \mid } I } } & { { I } } \end{array} \right) \left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { a \stackrel { \mid } { \mid } 0 } } & { { 0 } } \\ { { } } & { { \mid \mid } } & { { 0 } } \\ { { - \lambda _ { 1 } \stackrel { \mid } { \mid } 0 } } & { { 0 } } \\ { { - -- \ \ \mid \ -- \ } } & { { \mid \lambda _ { 2 } } } & { { f } } \\ { { \mid \lambda _ { 1 } \mid } } & { { \lambda _ { 2 } } } \end{array} \right) .
$$

All elem ents $c _ { i j }$ of these matrices already coincide, with the exception of the right upper $2 \times 2$ submatrix ( $i = 1 , 2$ and $j = 3$ , 4). Multiplying out we obtain $\lambda _ { 1 } p + a r + b = \lambda _ { 2 } p , \lambda _ { 1 } r + d = \lambda _ { 2 } r$ (and a similar set of equations for $q$ and $s$ ). These are of triangular structure and since $\lambda _ { 1 } \neq \lambda _ { 2 }$ they can easily be solved for $r$ and $p$ , then for $s$ and $q$ . More general situations are now obvious (try an example!).

In the following steps we treat each of the remaining blocks separately: we thus assume that all diagonal elements are equal and transform the block recursively to the form stated in the theorem.

We suppose the matrix A is of form

$$
\begin{array} { r l r } { A } & { { } = } & { \left( \frac { \mathsf { A } _ { \mathsf { \Pi } } ^ { \dagger } a ^ { T } } { \mathsf { I } - \mathsf { I } - \mathsf { \Pi } _ { \mathsf { 1 } } ^ { - } - \mathsf { \Pi } _ { \mathsf { 1 } } } \right) } \\ { } & { { } } & { \left( \mathsf { I } _ { \mathsf { \Pi } _ { \mathsf { 1 } } } ^ { \dagger } A _ { \mathsf { 1 } } ^ { T } \right) } \end{array}
$$

and assume, by the induction hypothesis, that $\boldsymbol { A } _ { \textup { 1 } }$ can be transformed to Jordan form by a matrix $T _ { 1 ^ { \cdot } }$ Then

$$
\begin{array} { r } { ( \underbrace { \lambda _ { \quad 1 } ^ { \mid } a ^ { T } } _ { \begin{array} { l } { 0 } \\ { \dots \dots \dots } \\ { 0 _ { \mid } ^ { \mid } A _ { 1 } } \end{array} } ) ( \underbrace { 1 } _ { \begin{array} { l } { 0 } \\ { 0 } \\ { \mid T _ { 1 } } \end{array} } ^ { \mid } - \underbrace { ( \begin{array} { l } { 1 } \\ { 0 } \\ { \dots } \\ { 0 } \end{array} ) } _ { \begin{array} { l } { 1 } \\ { 1 } \end{array} } = ( \underbrace { 1 } _ { \begin{array} { l } { ( \begin{array} { l } { 1 } \\ { 0 } \\ { \dots } \\ { 0 } \end{array} } ) } _ { \begin{array} { l } { 1 } \\ { 0 } \end{array} } ) ( \begin{array} { l l l l } { \lambda _ { \quad 1 } ^ { \mid } b _ { \lambda } } & { b _ { \lambda } } & { b _ { 3 } } & { \dots } \\ { - \dots } & { - \dots } & { - \dots } & { - } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { 1 } & { } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { } & { } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { } & { } \\ { 1 } & { } & { \lambda } & { \dots } \end{array} ) } \end{array} \end{array}
$$

where the vector $^ b$ is given by $b = T _ { 1 } ^ { T } a$ . Next, the matrix on the right can be sim plified as

$$
\begin{array} { r } { \left( \begin{array} { l l l l l } { \wedge \ \ \vert b _ { 1 } } & { b _ { 2 } \vert b _ { 3 } } & { \dotsc } \\ { \neg \neg \dots - \dots \dots \dots } \\ { 0 \vert \wedge \ \mathbf { \Lambda } \vert } & { \vert } \\ { 0 \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \neg \vert } & { \mathbf { \Lambda } \vert } \\ { \neg \vert } & { \dots - \dots - \dots \vert } \\ { \vdots } & { \vert \mathbf { \Lambda } \vert } & { \dotsc } \\ { \neg \vert } & { \vert \mathbf { \Lambda } \vert } \end{array} \right) \left( \begin{array} { l l l l } { 1 \ \vert b _ { 2 } } & { 0 \vert \mathbf { \Lambda } \vert } \\ { - - \frac { 1 } { 1 } - 2 - \frac { 1 } { 1 } - } \\ { \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { - \vert } & { - - \dots - \vert } \\ { \vert } & { \vert } & { \vert } \end{array} \right) = \left( \begin{array} { l } { 1 \vert b _ { 2 } } & { 0 \vert \mathbf { \Lambda } \vert } \\ { - - \frac { 1 } { 1 } - 2 - - \frac { 1 } { 1 } - } \\ { \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \vert } & { 1 } \\ { \vert } & { \vert } \\ { - \vert } & { 1 \vert } \\ { \vert } & { \vert } \end{array} \right) \left( \begin{array} { l l l l } { \underset { 1 } { } ^ { 1 } } & { 0 \vert \ b _ { 1 } } & { 0 \vert \ b _ { 3 } } & { \dotsc } \\ { \vdots - \vert } & { \vert } & { \vert \mathbf { \Lambda } \vert } \\ { 0 \vert \mathbf { \Lambda } \vert } & { 1 } & { \vert } \\ { 0 \vert } & { 1 } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { \dotsc - \vert } & { - \vert } & { \vert } \\ { \vdots } & { \vert } & { \vert } \end{array} \right) } \end{array}
$$

Here we distinguish two cases:

a） $b _ { 1 } = 0$ : in this case we exchange the first two (block-)lines and columns and are again back at the induction hypothesis.

b） $b _ { 1 } \neq 0$ : here we use a diagonal scaling matrix to replace $b _ { 1 }$ by 1 (Exercise 4). Our last task is to remove $b _ { 3 } , b _ { 4 } , . .$ . These terms are pushed down to the right as follows:

$$
{ \left| \begin{array} { l l l } { 1 } & { { \left| \begin{array} { l l } { b _ { 3 } } & { b _ { 4 } } \\ { | } & { | } \end{array} \right| } } \\ { \lambda } & { 1 } \\ { | } & { | } \\ { - -- } & { - } & { - } \\ { - } & { - } & { - } \\ { | } & { \lambda } & { 1 } \\ { | } & { | } & { | } \end{array} \right| } \left( { \left| \begin{array} { l l l } { ~ } & { | } & { 0 } & { 0 } \\ { ~ } & { | } & { - | } & { - b _ { 3 } } & { - b _ { 4 } } \\ { ~ } & { | } & { - } & { - } & { 0 } \\ { ~ } & { | } & { 0 } & { 0 } \\ { -- } & { - } & { - } & { - } & { 0 } \\ { | } & { 1 } & { 0 } & { 0 } \\ { | } & { | } & { 0 } & { 1 } \end{array} \right| } \right) = \left( { \begin{array} { l l l } { ~ } & { | } & { 0 } & { 0 } \\ { ~ } & { | } & { 1 } & { 0 } \\ { ~ } & { | } & { - b _ { 3 } } & { - b _ { 4 } } \\ { ~ } & { | } & { | } & { 0 } \\ { -- } & { - } & { - } & { 0 } \\ { | } & { 1 } & { 0 } \\ { | } & { | } & { 1 } \end{array} } \right) \left( { \begin{array} { l l l } { \lambda } & { 1 } & { | } & { | } & { | } \\ { ~ \lambda } & { 1 } & { | } & { b _ { 3 } } \\ { ~ } & { ~ } & { 1 } & { - } & { - } \\ { ~ } & { \lambda } & { 1 } & { - } & { - } \\ { - } & { - } & { - } & { - } & { - } \\ { 1 } & { 1 } & { 0 } \\ { | } & { | } & { 1 } & { - } & { - } \end{array} } \right) ,
$$

and so on. In order that by this procedure all $b _ { i }$ finally die out, we have to assume that the first block is not smaller than the following ones. This has to be arranged in the beginning by permutations.

The product of all these transformation matrices is then the m atrix $T$ in (12.14). QED.

Corollary 12.3. For every matrix A and for every number E≠ O there exists a non-singular matrix $T$ (depending on e ) such that

$$
T ^ { - 1 } { \cal A } T = \mathrm { d i a g } \left\{ \left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { \epsilon } } & { { } } \\ { { } } & { { \ddots } } & { { \epsilon } } \\ { { } } & { { } } & { { \lambda _ { 1 } } } \end{array} \right) , \left( \begin{array} { c c c } { { \lambda _ { 2 } } } & { { \epsilon } } & { { } } \\ { { } } & { { \ddots } } & { { \epsilon } } \\ { { } } & { { } } & { { \lambda _ { 2 } } } \end{array} \right) , \cdots \right\} ,
$$

Proof: Multiply Equation (12.14) from the right by $D = \mathrm { d i a g \bar { ( } 1 , \epsilon , \epsilon ^ { 2 } , \epsilon ^ { 3 } , \dots ) }$ and from the left by $D ^ { - 1 }$ QED.

Numerical difficulties in determining the Jordan canonical form are described in Golub-Wilkinson (1976). There exist also several computer programs, for example the one described in Kaogstrom-Ruhe (1980).

When the matrix A has been transformed to Jordan canonical form (12.14), the solutions of the differential equation $y ^ { \prime } { = } A y$ can be calculated by the method explained in (12.12'), case b):

$$
y \left( x \right) = T D T ^ { - 1 } y _ { 0 }
$$

where $D$ is a block-diagonal matrix with blocks of the form

$$
\begin{array} { r } { \left( \begin{array} { l l l l l } { e ^ { \lambda _ { 1 } x } } & { x e ^ { \lambda _ { 1 } x } } & { \dots } & { \displaystyle \frac { x ^ { k } } { k ! } e ^ { \lambda _ { 1 } x } } \\ & & & { \ddots } \\ & & & & { e ^ { \lambda _ { 1 } x } } \end{array} \right) } \end{array}
$$

This is an extension of Formula (12.8).

# Geometric representation

The geometric shapes of the solution curves of $y ^ { \prime } { = } A y$ are presented in Figure 12.1 for dimension $n = 2$ They are plotted as paths in the phase-space $( y _ { 1 } , y _ { 2 } )$ . The cases a), b),c) and e) are the linearized equations of (12.16) at the four critical points (see Figure 12.2).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/43a4e9328f6af560885f78d1b8bde92ba3da66af1506af55afc98aad5608e4f2.jpg)

Figure 12.1. Solutions of linear two dimensional systems

Much of this structure remains valid also for nonlinear systems (12.1) in the neighbourhood of equilibrium points. Exceptions may be "structurally unstable" cases such as complex eigenvalues with $\scriptstyle \alpha = \operatorname { R e } ( \lambda ) = 0$ . This has been the subject of many papers discussing "critical points" or "singularities" (see e.g. the famous treatise of Poincare (1881,82,85)).

In Figure 12.2 we show solutions of the quadratic system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = \displaystyle \frac { 1 } { 3 } ( y _ { 1 } - y _ { 2 } ) ( 1 - y _ { 1 } - y _ { 2 } ) } } \\ { { { } } } \\ { { y _ { 2 } ^ { \prime } = y _ { 1 } ( 2 - y _ { 2 } ) } } \end{array}
$$

which possesses four critical points of all four possible structurally stable types (Exercise 4).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/2daa316fb039c030610dd29a52434b167abe86ff36e3bc472b8be91561e82867.jpg)  
Figure 12.2. Solution flow of System (12.16)

# Exercises

1. a) Compute the eigenvectors of the matrix

$$
\begin{array} { r } { A } \\ { A } \end{array} = \left( \begin{array} { l l l l l l } { - 1 } & { 2 0 } & & & & \\ & { - 2 } & { 2 0 } & & & \\ & & { - 3 } & { 2 0 } & & \\ & & & { \ddots } & { \ddots } & \\ & & & & { - 1 9 } & { 2 0 } \\ & & & & & { - 2 0 } \end{array} \right)
$$

by solving $( A - \lambda _ { i } I ) _ { \underline { { \nu } } _ { i } } { = } 0$   
Result. $\boldsymbol { \nu } _ { 1 } { = } ( 1 , 0 , \ldots ) ^ { T } ,$ $\nu _ { 2 } { = } ( 1 , - 1 / 2 0 , 0 , . . . ) ^ { T } ,$ $\nu _ { 3 } = ( 1 , - \bar { 2 } / 2 0 , 2 / 4 0 0 , 0 _ { \bar { , } \bar { \dots } } ) ^ { T }$ ，   
$\nu _ { 4 } \mathrm { = } ( 1 , - 3 / 2 0 , 6 / 4 0 0 , - 6 / 8 0 0 0 , 0 , . . . ) ^ { T } ,$ etc.

b) Compute, numerically the inverse of $T = ( \nu _ { 1 } , \nu _ { 2 } , \ldots , \nu _ { n } )$ and determine its largest element (answer: $4 . 5 \times 1 0 ^ { 1 2 }$ ). The matrix $T$ is thus very badly conditioned.

c) Compute numerically or analytically from (12.13) the solutions of

$$
y ^ { \prime } = A y , \qquad y _ { i } ( 0 ) = 1 , \qquad i = 1 , \ldots , 2 0 .
$$

Observe the "hump" (Moler and Van Loan (1978)): although all eigenvalues of A are negative, the solutions first grow enormously before decaying to zero. This is typical of non-symmetric matrices and is connected with the bad condition of $^ T \cdot$ (See Figure 12.3, which shows the solutions in logarithmic scale ()). Result

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/b22a38445b32b718026d5286304730615eb24f7063b4ff9342626cb1954d4222.jpg)  
Figure 12.3. Solutions of Equation (12.18) with Matrix (12.17)

2. (Schur). Prove that the eigenvalues of a matrix A satisfy the esti-

$$
\sum _ { i = 1 } ^ { n } { | \lambda _ { i } | } ^ { 2 } \leq \sum _ { i , j = 1 } ^ { n } { | a _ { i j } | } ^ { 2 }
$$

and that equality holds iff $A$ is orthogonally diagonizabie (see also Exercise 3).

Hint. $\textstyle \sum _ { i , j } | a _ { i j } | ^ { 2 }$ is the trace of $A ^ { * } A$ and thus invariant under uni-tary transformations ${ \boldsymbol { Q } } ^ { * } { \boldsymbol { A } } { \boldsymbol { Q } }$

3. Show that the Schur decomposition ${ \boldsymbol { S } } = { \boldsymbol { Q } } ^ { * } { \boldsymbol { A } } { \boldsymbol { Q } }$ is diagonal iff $A ^ { * } A = A A ^ { * }$ Such matrices are called normal. Hint. The condition is equivalent to ${ \boldsymbol { S } } ^ { * } { \boldsymbol { S } } = { \boldsymbol { S } } { \boldsymbol { S } } ^ { * }$ Show that skew-symmetric matrices are normal.

4. Let $b \neq 0$ be given. Determine α such that

$$
\begin{array} { r } { \left( \begin{array} { l l } { \lambda } & { b } \\ & { \lambda } \end{array} \right) \left( \begin{array} { l l } { 1 } & { 0 } \\ & { \alpha } \end{array} \right) = \left( \begin{array} { l l } { 1 } & { 0 } \\ & { \alpha } \end{array} \right) \left( \begin{array} { l l } { \lambda } & { 1 } \\ & { \lambda } \end{array} \right) \textrm { . } } \end{array}
$$

5. Compute the four critical points of System (12.16), and for each of these points the eigenvalues and eigenvectors of the matrix $\partial f / \partial y$ . Compare the results with Figures 12.2 and 12.1.

6. Compute a Schur decomposition and the Jordan canonical form of the matrix

$$
A \ = \frac 1 9 \left( \begin{array} { l l l } { { 1 4 } } & { { 4 } } & { { 2 } } \\ { { - 2 } } & { { 2 0 } } & { { 1 } } \\ { { - 4 } } & { { 4 } } & { { 2 0 } } \end{array} \right) \ .
$$

R esult. The Jordan canonical form is

$$
\left( \begin{array} { c c c } { { 2 } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { } } \\ { { 2 } } & { { } } & { { } } \\ { { } } & { { } } & { { 2 } } \end{array} \right) ~ ,
$$

7. Reduce the matrices

$$
\begin{array} { r } { A = \left( \begin{array} { c c c } { \mathrm {  ~ \lambda ~ } _ { 1 } } & { b } & { c } \\ & { \mathrm {  ~ \lambda ~ } _ { 1 } } & { d } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } } \end{array} \right) , \quad A = \left( \begin{array} { c c c } { \mathrm {  ~ \lambda ~ } _ { 1 } } & { b } & { c } \\ & { \mathrm {  ~ \lambda ~ } _ { 0 } } & { d } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & & { \mathrm {  ~ \lambda ~ } _ { \mathrm {  ~ \lambda ~ } } } \end{array} \right) } \end{array}
$$

to Jordan canonical form. In the second case distinguish the possibilities $b + d = 0$ and $b + d \neq 0$

# I.13. Stability

The Examiners give notice that the following is the subject of the Prize to be adjudged in 1877: The Criterion of Dynamical Stability.   
(S.G. Phear (Vice-Chancellor), J. Challis, G.G. Stokes, J. Clerk Max well)

# Introduction

"To illustrate the meaning of the question imagine a particle to slide down inside a smooth inclined cylinder along the lowest generating line, or to slide down outside along the highest generating line. In the former case a slight derangement of the motion would merely cause the particle to oscillate about the generating line, while in the latter case the particle would depart from the generating line altogether. The motion in the former case would be, in the sense of the question， stable, in the latter unstable .. what is desired is,a corresponding condition enabling us to decide when a dynamically possible motion of a system is such, that if slightly deranged the motion shall continue to be only slighty departed from." ('The Examiners" in Routh (1877)).

Whenever no analytical solution of a problem is known, numerical solutions can only be obtained for specified initial values. But often one needs information about the stability behaviour of the solutions for all initial values in the neighbourhood of a certain equilibrium point. We again transfer the equilibrium point to the origin and define:

Definition 13.1. Let

$$
y _ { i } ^ { \prime } = f _ { i } ( y _ { 1 } , \dotsc , y _ { n } ) \qquad i = 1 , \dotsc , n
$$

be a system with ${ f _ { i } } ( 0 , \ldots , 0 ) { = } 0$ ， $i = 1 , \ldots , n$ . Then the origin is called stable in the sense of $\scriptstyle L$ iapunov if for any $\epsilon > 0$ there is a $\delta > 0$ such that for the solutions $\mid \mid y ( x _ { 0 } ) \mid \mid < 8$ implies $\left| \left| \begin{array} { l } { y \left( x \right) } \end{array} \right| \right| < \epsilon$ for all $x > x _ { 0 } .$

The first step, undertaken by Routh in his famous Adams Prize essay (Routh (1877)), was to study the linearized equation

$$
y _ { i } ^ { \prime } = \sum _ { j } a _ { i j } y _ { j } , \qquad a _ { i j } ^ { } = \frac { \partial f _ { i } } { \partial y _ { j } } ( 0 ) .
$$

("The quantities $x \ , y \ , z \ , \ \ldots .$ etc are said to be small when their squares can be neglected.") From the general solution of (13.2) obtained in Section I.12, we have immediately

Theorem 13.1. The linearized equation (13.2) is stable (in the sense of Liapunov) iff all roots of the characteristic equation

$$
\operatorname* { d e t } ( \lambda I - A \ ) = a _ { 0 } \mathsf { \lambda } ^ { n } + \alpha _ { 1 } \mathsf { \lambda } ^ { n - 1 } + \cdot \cdot \cdot + a _ { n - 1 } \mathsf { \lambda } + a _ { n } \ = 0
$$

satisfy $\mathrm { R e } ( \lambda ) \leq 0$ ， and the multiple roots, which give rise to Jordan chains, satisfy the strict inequality $\mathrm { R e } ( \lambda ) < 0$

Proof: See (12.12) and (12.15). For Jordan chains the "secular" term (e.g. $E + F x$ in the solution of (12.12), case b)） which tends to infinity for increasing $x$ ， must be "killed" by an exponential with strictly negative exponent. QED.

# The Routh-Hurwitz criterion

The next task, which leads to the famous Routh-Hurwitz criterion， was the verification of the conditions $\mathrm { R e } ( \lambda ) < 0$ directty from the coefficients of (13.3)， without computing the roots. To solve this problem， Routh combined two known ideas: the first was Cauchy's argument principle, saying that the number of roots of a polynomial $p \left( z \right) = u \left( z \right) + i \nu \left( z \right)$ inside a closed contour is equal to the number of (positive) rotations of the vector $\left( u \left( z \right) , \nu \left( z \right) \right)$ ，as $z$ travels along the boundary in the positive sense (cf. e.g. Henrici (1974)， p.276). An example is presented in Figure 13.1 for the polynomial

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/7813648712d1d9f19576fd908ef14df36689c6b33c8c76c2324e3e359ff9b54a.jpg)  
Figure 13.1. Vector field of arg $( p \left( z \right)$ ) for the polynomial $p \left( z \right)$ of (13.4)

$$
\begin{array} { c } { { z ^ { 6 } + 6 z ^ { 5 } + 1 6 z ^ { 4 } + 2 5 z ^ { 3 } + 2 4 z ^ { 2 } + 1 4 z + 4 } } \\ { { { } } } \\ { { = ( z + 1 ) ( z + 2 ) ( z ^ { 2 } + z + 1 ) ( z ^ { 2 } + 2 z + 2 ) \ . } } \end{array}
$$

On the half-circle $z = \mathbf { R e } ^ { i \mathbf { \theta } }$ $\pi / 2 \le \Theta \le 3 \pi / 2$ ， $R$ very large) the argument of $p \left( z \right)$ , due to the dominant term $z ^ { n }$ , makes $n / 2$ positive rotations. In order 'to have all zeros of $p$ in the negative half plane, we therefore need an additional n/2 positive rotations along the ima-ginary axis:

Lemma 13.2. Let $p \left( z \right)$ be a polynomial of degree n and suppose that $p ( i y ) \neq 0$ for $y \in \mathbb { R }$ . Then all roots of $p \left( z \right)$ are in the negative halfplane $i f ,$ along the imaginary axis, $a r g ( p \left( i \right) )$ )makes n/2 positive rotations for y from $- \infty$ to $+ \infty$ .NED.

The second idea was the use of Sturm's theorem (Sturm (1829)) which had its origin in Euclid's algorithm for polynomials. Sturm made the discovery that in the division of the polynomial $p _ { i - 1 } ( y )$ by $p _ { i } ( y )$ it is better to take the remainder $p _ { i + 1 } ( y )$ with negative sign

$$
p _ { i - 1 } ( y ) = p _ { i } ( y ) q _ { i } ( y ) - p _ { i + 1 } ( y ) ~ .
$$

Then, due to the "Sturm sequence property"

$$
s i g n ( p _ { i + 1 } ( y ) ) \ne s i g n ( p _ { i - 1 } ( y ) ) \mathrm { i f } p _ { i } ( y ) = 0 ,
$$

the number of sign changes

$$
w \left( y \right) = \mathrm { ~ N o . ~ o f ~ s i g n ~ c h a n g e s ~ o f } \left( p _ { 0 } ( y ) , p _ { 1 } ( y ) , . . . , p _ { m } ( y ) \right)
$$

does not vary at the zeros of $p _ { 1 } ( y ) , . . . , p _ { m - 1 } ( y )$ . A consequence is the following

Lemma 13.3. Suppose that a sequence $\boldsymbol { p } _ { 0 } ( y ) , \boldsymbol { p } _ { 1 } ( y ) , \dots , \boldsymbol { p } _ { m } ( y )$ of real polynomials satisfies

i） $\deg ( p _ { 0 } ) > \deg ( p _ { 1 } )$ not simutaneosty zer,. $\boldsymbol { p } _ { 0 } ( y )$ $p _ { 1 } ( y )$   
ii) $p _ { m } \left( y \right) \neq 0$ for all y ∈R,   
iv) and the Sturm sequence property (13.6).

Then

$$
\frac { w ( \infty ) - w ( - \infty ) } { 2 }
$$

is equal to the number of rotations， measured in the positive direction， of the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ as y tends from $- \infty \ t o \ + \infty$ ·

Proof: Due to the Sturm sequence property， $w \left( y \right)$ does not change at zeros of $p _ { 1 } ( y ) , \ldots , p _ { m - 1 } ( y )$ By assumption i) also $p _ { m } ( y )$ has no influence. Therefore $w \left( y \right)$ can change only at zeros of $p _ { 0 } ( y )$ · If $w \left( y \right)$ increases by one at $\hat { y }$ , either $p _ { 0 } ( y )$ changes from $^ +$ to - and $p _ { 1 } ( \hat { y } ) > 0$ or it changes from $^ -$ to $^ +$ and $p _ { 1 } ( \hat { y } ) < 0$ $( p _ { 1 } ( \hat { y } ) = 0$ is impossible by i)). In both situations the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ crosses the imaginary axis in the positive direction (see Figure 13.2). If $w \left( y \right)$ decreases by one, $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ ） crosses the imaginary axis in the negative direction. The result now foliows from i)， since the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ is horizontal for $y  - \infty$ and for $y  + \infty$ . QED.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/e3fd2d5ef08a18f5a87cbeee6526f87e4f8ddde5f618a56e628d73e3d9f56dae.jpg)  
Figure 13.2. Rotations of $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ ） compared to $w \left( y \right)$

The two preceding lem mas together give us the desired criterion for stability: let the characteristic polynomial (13.3)

$$
p ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } = 0 \ , \qquad a _ { 0 } > 0
$$

be given. We divide $p \left( i y \right)$ by $i ^ { n }$ and separate real and imaginary parts,

$$
\begin{array} { l } { { p _ { 0 } ( y ) = \displaystyle { \mathrm { R e } } \frac { p \left( i y \right) } { i ^ { n } } = a _ { 0 } y ^ { n } - a _ { 2 } y ^ { n - 2 } + a _ { 4 } y ^ { n - 4 } \pm \cdot \cdot \cdot \quad ( \mathrm { ( } } } \\ { { \mathrm { } } } \\ { { p _ { 1 } ( y ) = - \mathrm { I m } \frac { p \left( i y \right) } { i ^ { n } } = a _ { 1 } y ^ { n - 1 } - a _ { 3 } y ^ { n - 3 } + a _ { 5 } y ^ { n - 5 } \pm \cdot \cdot \cdot \mathrm { . } } } \end{array}
$$

Due to the special structure of these polynomials, the Euclidean algorithm (13.5) is here particularly simple: we write

$$
p _ { i } ( y ) = c _ { i 0 } y ^ { n - i } + c _ { i 1 } y ^ { n - i - 2 } + c _ { i 2 } y ^ { n - i - 4 } + \cdot \cdot \cdot \ ,
$$

and have for the quotient in (13.5) $q _ { i } ( y ) = ( c _ { i - 1 , 0 } / c _ { i 0 } ) y$ , provided that $c _ { i 0 } \neq 0$ Now (13.10) inserted into (13.5) gives the following recursive forulafortemputationftecicits $c _ { i j }$ ：

$$
c _ { i + 1 , j } = c _ { i , j + 1 } \cdot \frac { c _ { i - 1 , 0 } } { c _ { i 0 } } - c _ { i - 1 , j + 1 } = \frac { 1 } { c _ { i 0 } } \operatorname* { d e t } \left( \begin{array} { c c } { { c _ { i - 1 , 0 } } } & { { c _ { i - 1 , j + 1 } } } \\ { { c _ { i , 0 } } } & { { c _ { i , j + 1 } } } \end{array} \right)
$$

If $c _ { i 0 } { = } 0$ for some $i$ , the quotient $q _ { i } ( y )$ is a higher degree polynomial and the Euclidean algorithm stops at $p _ { m } ( y )$ with $m < n$

The sequence $( \boldsymbol { p } _ { i } ( y )$ ） obtained in this way obviously satisfies Conditions i) and iv) of Lemma 13.3. Condition ii) is equivalent to $p \left( i y \right) \neq 0$ for $y \in \mathbb { R } .$ ，and ii) is a consequence of ii since $p _ { m } ( y )$ is the greatest common divisor of $\boldsymbol { p } _ { 0 } ( y$ ) and $p _ { 1 } ( y )$

Theorem 13.4. (Routh (1877)). All roots of the real polynomial (13.3）with $a _ { 0 } > 0$ lie in the negative half plane $\mathrm { R e } \lambda < 0$ if and only if

$$
c _ { i 0 } > 0 \qquad f o r \quad i = 0 , 1 , 2 , \ldots , n \quad ,
$$

Remark: Due to the condition $c _ { i 0 } > 0$ , the division by $c _ { i 0 }$ in Formula (13.11) can be omitted (common positive factor of $p _ { i + 1 } ( y ) ,$ ）， which leads to the same theorem (Routh (1877), p. 27: ". so that by remembering this simple cross-muitiplication we may write down..."). This, however， is not advisable for n large because of possible overflow.

Proof: The coordinate systems $( p _ { 0 } , p _ { 1 } )$ and $( \operatorname { R e } ( p ) , \operatorname { I m } ( p ) )$ are of opposite orientation. Therefore, n/2 positive rotations of $p \left( i y \right)$ correspond to n /2 negative rotations of $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ . If all roots of $p \left( \lambda \right)$ lie in the negative half plane $\mathrm { R e } \lambda < 0$ , it follows from Lemmas 13.2 and 13.3 that $w \left( \infty \right) - w \left( - \infty \right) = - n$ ,which is only possible if $w \left( \infty \right) = 0$ ， $w \left( - \infty \right) = n$ .This implies the positivity of all leading coefficients of $p _ { i } ( y )$

On the other hand,if (3.12)issatifd,westhat $p _ { n } \left( y \right) \equiv c _ { n } 0$ Hence the polynomials $\boldsymbol { p } _ { 0 } ( \boldsymbol { y }$ ）and $p _ { 1 } ( y )$ cannot have a common factor and $p \left( \lambda \right) \neq 0$ on the imaginary axis. We can now apply Lem mas 13.2 and 13.3 again to obtain the result. QED.

A second proof of this Theorem is possible using "positive func-tions" (see Volume II).

Example 1: The Routh tableau (13.11) for Equation (13.4) is given in Table 13.1. It clearly satisfies the conditions for stability.

Example 2: (Routh (1877), p. 27). Express the stability conditions for the biquadratic

$$
z ^ { 4 } + p z ^ { 3 } + q z ^ { 2 } + r z + s = 0 .
$$

The $c _ { i j }$ values (without division) are given in Table 13.2.

Table 13.1. Routh tableau for (13.4)   

<table><tr><td></td><td>j=0</td><td>j=1</td><td>j=2</td><td>j=3</td></tr><tr><td>i=0</td><td>1</td><td>-16</td><td>24</td><td>-4</td></tr><tr><td>i=1</td><td>6</td><td>-25</td><td>14</td><td></td></tr><tr><td>i=2</td><td>11.83</td><td>-21.67</td><td>4</td><td></td></tr><tr><td>i=3</td><td>14.01</td><td>-11.97</td><td></td><td></td></tr><tr><td>i=4</td><td>11.56</td><td>-4</td><td></td><td></td></tr><tr><td>i=5</td><td>7.12</td><td></td><td></td><td></td></tr><tr><td>i=6</td><td>4</td><td></td><td></td><td></td></tr></table>

Table 13.2. Routh tableau for (13.13)   

<table><tr><td></td><td>j=0</td><td>j=1</td><td>j=2</td></tr><tr><td>i=0</td><td>1</td><td>-q</td><td>S</td></tr><tr><td>i=1</td><td>p</td><td>-r</td><td></td></tr><tr><td>i=2</td><td>pq-r</td><td>-ps</td><td></td></tr><tr><td>i=3</td><td>(pq -r)r-p²s</td><td></td><td></td></tr><tr><td>i=4</td><td>((pq-r)r-p²s)ps</td><td></td><td></td></tr></table>

We have stability iff

$$
p > 0 \ , \quad p q - r > 0 \ , \quad ( p q - r ) r - p ^ { 2 } s > 0 \ , s > 0 \ .
$$

# Computational considerations

The actual computational use of Routh's criterion, in spite of its high historical importance and mathematical elegance, has two drawbacks for higher dimensions:

1) It is not easy to compute the characteristic polynomial for higher order matrices;

2) The use of the characteristic polynomial is very dangerous in the presence of rounding errors.

So, whenever one is not working with exact algebra or high precision,it is advisable to avoid the characteristic polynomial and use numerically stable algorithms for the eigenvalue problem (e.g. Eispack (1974)).

Numerical Experiments: 1. The matrix

$$
\begin{array} { r l } { A } & { = \left( \begin{array} { l l l l l } { - . 0 5 } & & { 1 } & { - 1 } & & \\ & { . } & { 1 } & & \\ & { . } & { 1 } & { . } & \\ & & { . } & { 1 } & \\ & & { - . 0 5 } & & { - n } \\ { - . -- } & { - . -- } & { - . -- } & { - n } \\ { 1 } & & { 1 } & { - . 0 5 } & \\ & { . } & { 1 } & & \\ & { . } & { 1 } & { . } & \\ & & { n } & { 1 } & { - . 0 5 } \end{array} \right) } \end{array}
$$

has the characteristic polynomial

$$
p ( z ) = \prod _ { j = 1 } ^ { n } \left( z ^ { 2 } + 0 . 1 z + j ^ { 2 } + 0 . 0 0 2 5 \right) .
$$

We computed the coefficients of $p$ using double precision, and then applied the Routh algorithm in single precision (machine precision ${ \dot { = 1 } } . 5 \times 1 0 ^ { - 8 }$ ).Theresults indicated stability for $n \leq 1 5$ , but not for $n \geq 1 6$ ， although the matrix always has its eigenvalues $- 0 . 0 5 \pm k i$ in the negative half plane. On the other hand, a direct computation of the eigenvalues of A with the use of Eispack subroutines gave no problem for any $n$ ·

2. We also tested the Routh algorithm at the (scaled) numerators of the diagonal Pade approximations to exp(z)

$$
\begin{array} { c } { { 1 + \displaystyle \frac { n } { 2 n } ( n z ) + \displaystyle \frac { n ( n - 1 ) } { ( 2 n ) ( 2 n - 1 ) } \displaystyle \frac { ( n z ) ^ { 2 } } { 2 ! } } } \\ { { + \displaystyle \frac { n ( n - 1 ) ( n - 2 ) } { ( 2 n ) ( 2 n - 1 ) ( 2 n - 2 ) } \displaystyle \frac { ( n z ) ^ { 3 } } { 3 ! } + \cdots ~ , } } \end{array}
$$

which are also known to possess all eigenvalues in $\mathbf { C } ^ { - }$ . Here, the results were correct only for $n \leq 2 1$ ， and wrong for larger $n$ due to rounding errors.

# Liapunov functions

We now consider the question whether the stability of the nonlinear system (13.1) "can really be determined by examination of the terms of the first order only" (Routh (1877), Chapt.VII). This theory, initiated by Routh and Poincaré, was brought to perfection in the famous work cf Liapunov (1892). As a general reference to the enormous theory that has devcloped in the meantime we mention Rouche-Habets-Laloy (1977) and W. Hahn (1967).

Liapunov's (and Routh's) main tools are the so-called Liapunov functions $V \left( y _ { 1 } , \ldots , y _ { n } \right)$ , which should satisfy

$$
\begin{array} { c } { { V \left( y _ { 1 } , \ldots , y _ { n } \right) \geq 0 \ , } } \\ { { { } } } \\ { { V \left( y _ { 1 } , \ldots , y _ { n } \right) = 0 \ \mathrm { i f f } y _ { 1 } = \cdot \ \cdot \ = y _ { n } = 0 } } \end{array}
$$

and along the solutions of (13.1)

$$
{ \frac { d } { d x } } V \left( y _ { 1 } ( x ) , \ldots , y _ { n } ( x ) \right) \leq 0 \ .
$$

Usually $V \left( y \right)$ behaves quadratically for sm all y and Condition (13.15) means that

$$
c \parallel y \parallel ^ { 2 } \leq V ( y ) \leq C \parallel y \parallel ^ { 2 } , \quad \quad C \geq c > 0 .
$$

The existence of such a Liapunov function is then a sufficient condition for stability of the origin.

We start with the construction of a Liapunov function for the linear case

$$
y ^ { \prime } = A y .
$$

This is best done in the basis which is naturally given by the eigenvectors (or Jordan chains) of $A$ . Wc therefore introduce $y = T z$ ， $z = T ^ { - 1 } y$ so that A is transformed to Jordan canonical form (12.14') ${ \boldsymbol { J } } = { \boldsymbol { T } } ^ { - 1 } { \boldsymbol { A } } { \boldsymbol { T } }$ and (13.18) becomes

$$
z ^ { \prime } = J z .
$$

If we put

$$
V _ { 0 } ( z ) = | | z | | ^ { 2 } \quad \mathrm { a n d } \quad V ( y ) = V _ { 0 } ( T ^ { - 1 } y ) = V _ { 0 } ( z ) ,
$$

the derivative of $V \left( y \left( x \right) \right)$ )becomes

$$
\begin{array} { l } { \displaystyle \frac { d } { d x } V \left( y \left( x \right) \right) = \frac { d } { d x } V _ { 0 } ( z \left( x \right) ) = 2 \mathrm { R e } < z \left( x \right) \mathrm { , ~ } z ^ { \prime } ( x ) > \quad \mathrm { ( ~ } \partial _ { x } \mathrm { ~ ) ~ } } \\ { \displaystyle = 2 \mathrm { R e } < z \left( x \right) \mathrm { , ~ } J { z } \left( x \right) > \ \le \ 2 \mu ( J ) V \left( y \left( x \right) \right) \mathrm { . ~ } } \end{array}
$$

By (10.20) the logarithmic norm is given by

$$
2 \mu ( J ) = \mathrm { l a r g e s t ~ e i g e n v a l u e ~ o f } J + J ^ { * } .
$$

The matrix $J + J ^ { * }$ is block-diagonal with tridiagonal blocks

$$
\left( \begin{array} { c c c c c } { { 2 \mathrm { R e } \lambda _ { i } } } & { { \epsilon } } & { { } } & { { } } & { { } } \\ { { \epsilon } } & { { 2 \mathrm { R e } \lambda _ { i } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \varepsilon } } \\ { { } } & { { } } & { { \epsilon } } & { { 2 \mathrm { R e } \lambda _ { i } } } \end{array} \right) ~ .
$$

Subtracting the diagonal and using Formula (6.7a), we see that the eigenvalues of the $m$ -dimensional matrix (13.22) are given by

$$
2 \left( { \tt R e A } _ { i } + \tt { e c o s } \frac { \pi k } { m + 1 } \right) \qquad k = 1 , \ldots , m .
$$

As a consequence of this formula or by the use of Exercise 4 we have:

Lemma 13.5. If all eigenvalues of A satisfy $\mathsf { R e } \lambda _ { i } < - \mathsf { p } < 0$ ，then there exists a (quadratic) Liapunov function for Equation (l3.18) which satisfies

$$
\frac { d } { d x } V \left( y \left( x \right) \right) \leq - \rho V \left( y \left( x \right) \right) .
$$

NED.

This last differential inequality implies that (Theorem 10.1)

$$
V \left( y \left( x \right) \right) \leq \ V \left( y _ { 0 } \right) \cdot \exp ( - \rho \left( x - x _ { 0 } \right) )
$$

and ensures that lim $| | \begin{array} { l } { y } \end{array} ( x \begin{array} { r } \end{array} ) | = 0$ , i.e. asymptotic stability.

# Stability of nonlinear systems

It is now easy to extend the same ideas to nonlinear equations. The following theorem is an example of such a result:

Theorem 13.6. Let the nonlinear system

$$
y ^ { \prime } = A y + g \left( x , y \right)
$$

be given with $\mathsf { R e } \lambda _ { i } < - \mathsf { \rho } < 0$ for all eigenvalues of A . Furher suppose that for each $\epsilon > 0$ there is a $\delta > 0$ such that

$$
\begin{array} { r } { | | \begin{array} { l } { g ( x , y ) } \end{array} | | \ \leq \ \epsilon | | \begin{array} { l } { y } \end{array} | \qquad \mathrm { f o r } \quad | | \begin{array} { l } { y | | < \delta } \end{array}  , \quad x \geq x _ { 0 } \ . } \end{array}
$$

Then the origin is (asymptotically) stable in the sense of Liapunov.

Proof: We use the Liapunov function $V \left( y \right)$ constructed for Lemma 13.5 and obtain from (13.25)

$$
\begin{array} { r } { \displaystyle \frac { d } { d x } V ( y ( x ) ) \leq - \mathsf { p } V ( y ( x ) ) \ ~ } \\ { +  2 \mathrm { R e } < T ^ { - 1 } y ( x ) , T ^ { - 1 } g ( x , y ( x ) ) > \ . } \end{array}
$$

Cauchy's inequality together with (13.26) yields

$$
{ \frac { d } { d x } } V \left( y \left( x \right) \right) \leq \mathbf { \alpha } ( { \mathbf { \bar { \alpha } } } _ { \mathsf { P } } + \parallel T \left. { \mathbf { \beta } } \cdot \right. T ^ { - 1 } \left. { \mathbf { \beta } } \epsilon \right) V \left( y \left( x \right) \right) ~ .
$$

For sufficiently small ε the right hand side is negative and we obtain asymptotic stability. QED.

We see that, for nonlinear systems, stability is onty ensured in a neighbourhood of the origin. This can also be observed in Figure 12.3. Another difference is that the stability for eigenvalues on the imaginary axis can be destroyed. An example for this (Routh (1877), p. 95) is the system

$$
y _ { 1 } ^ { \prime } = - y _ { 2 } + { y ^ { 3 } } _ { 1 } , \qquad y _ { 2 } ^ { \prime } = y _ { 1 } .
$$

Here, with the Liapunov function $V = ( y _ { 1 } ^ { ~ 2 } + y _ { 2 } ^ { ~ 2 } ) / 2$ ，we obtain $V \ ^ { \prime } { = } y \mathbf { \Sigma } _ { 1 } ^ { 4 }$ which is $> 0$ for $y _ { 1 } \neq 0$ . Therefore all solutions with initial value $\neq 0$ increase. A survey of this question ("the centre problem") together with its connection to limit cycles is given in Wanner (1983).

# Stability of non-autonomous systems

When the coefficients are not constant,

$$
y ^ { \prime } = A \left( x \right) y ,
$$

it is not a sufficient test of stability that the eigenvalues of A satisfy the conditions of stability for each instantaneous value of $x$ ·

Examples: 1. (Routh (1877), p. 96)

$$
y _ { 1 } ^ { \prime } = y _ { 2 } , \quad y _ { 2 } ^ { \prime } = - \frac { 1 } { 4 x ^ { 2 } } y _ { 1 }
$$

which is satisfied by $y _ { 1 } ( x ) { = } a { \sqrt { x } }$

2. An example with eigenvalues strictly negative: we start with

$$
B ~ = ~ \left( \begin{array} { c c } { { - 1 } } & { { 0 } } \\ { { 4 } } & { { - 1 } } \end{array} \right) ~ , ~ y ^ { \prime } = B y .
$$

An inspection of the derivative of $V = ( y _ { 1 } ^ { ~ 2 } + y _ { 2 } ^ { ~ 2 } ) / 2$ shows that V increases in the sector

$$
\frac { 1 } { 2 + \sqrt { 3 } } < \frac { y _ { 2 } } { y _ { 1 } } < 2 + \sqrt { 3 } .
$$

The idea is to take the initial value in this region and, for $x$ increasing, to rotate the coordinate system with the same speed as the solution rotates:

$$
y ^ { \prime } = T \left( x \right) B T \left( - x \right) y = A \left( x \right) y , T \left( x \right) = \left( \begin{array} { c c } { \cos a x } & { - \sin a x } \\ { \sin a x } & { \cos a x } \end{array} \right) .
$$

For $y \left( 0 \right) = \left( 1 , 1 \right) ^ { T }$ , the good choice for $a$ is $a = 2$ and (13.32） possesses the solution

$$
y \left( x \right) = \left( \left( \cos 2 x - \sin 2 x \right) e ^ { x } , \left( \cos 2 x + \sin 2 x \right) e ^ { x } \right) ^ { T } .
$$

This solution is clearly unstable, while $- 1$ remains for all $x$ the double eigenvalue of A $( x )$

For a third exam ple see Exercise 6 below.

We observe that stability theory for non autonomous systems is more complicated. Among the cases in which stability can be shown are the following:

1. $a _ { i i } ( x ) < 0$ and A $( x$ ) is diagonally dominant; then $\mu ( A \left( x \right) ) = 0$ and stability follows from Theorem 10.5.

2.A $( x ) = B + C \left( x \right)$ ，with $B$ constant and satisfying $\mathrm { R e } \lambda _ { i } < - \rho < 0$ for its eigenvalues, and $\displaystyle { \left| \mid C \left( x \right) \mid \right| < \epsilon }$ with $\epsilon$ so small that the proof of Theorem 13.6 can be applied.

# Exercices

1. Express the stability conditions for the polynomials $\scriptstyle z ^ { 2 } + p z + q = 0$ and $z ^ { 3 } + p z ^ { 2 } + q z + r = 0$

Result: a) $p > 0$ and $q > 0$ ; b) $p > 0$ ， $r > 0$ and $p q - r > 0$

2. (Hurwitz (1895)). Verify that Condition (13.12) is equivalent to the positivity of the principal minors of the matrix

$$
H = \left( \begin{array} { c c c c c } { a _ { 1 } } & { a _ { 3 } } & { a _ { 5 } } & { \cdots } \\ { a _ { 0 } } & { a _ { 2 } } & { a _ { 4 } } & { \cdots } \\ { } & { a _ { 1 } } & { a _ { 3 } } & { \cdots } \\ { } & { a _ { 0 } } & { a _ { 2 } } & { \cdots } \\ { } & { } & { \cdots } & { \cdots } \end{array} \right) = \left( a _ { 2 j - i } \right) _ { i , j = 1 } ^ { n }
$$

（ $a _ { k } = 0$ for $k < 0$ and $k > n$ ). Understand that Routh's algorithm (13.11) is identical to a sort of Gaussian elimination transforming $H$ to triangular form.
