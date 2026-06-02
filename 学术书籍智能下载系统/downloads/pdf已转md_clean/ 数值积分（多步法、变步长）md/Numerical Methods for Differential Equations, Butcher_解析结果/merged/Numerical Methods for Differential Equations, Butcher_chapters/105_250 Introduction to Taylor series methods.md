# 250 Introduction to Taylor series methods

A differential equation $y ^ { \prime } ( x ) = f ( x , y ( x ) )$ , characterized by the function $f$ , is presented to a computer in the form of a procedure, function or subroutine for computing values of $f ( u , v )$ for given arguments $u$ and $v$ . The program carries out the evaluation of this procedure in a manner that exactly corresponds to the occurrence of the function $f$ , in the mathematical formulation of the numerical method. In this brief introduction, we consider the use of procedures that evaluate, for given values of $x$ and $y ( x )$ , not only the value of $y ^ { \prime } ( x )$ , but also the value of $y ^ { \prime \prime } ( x )$ and possibly also $y ^ { \prime \prime \prime } ( x )$ and other higher derivatives.

With such facilities available, there is a wide range of possible methods, but the natural and straightforward choice of Taylor series is almost always followed. By repeated differentiation, we can find functions $f _ { 2 } ( x , y ( x ) )$ , $f _ { 3 } ( x , y ( x ) ) ,$ . . . , $f _ { m } ( x , y ( x ) )$ , which give values, respectively, of $y ^ { \prime \prime } ( x )$ , $y ^ { \prime \prime \prime } ( x )$ , . . . , $y ^ { ( m ) } ( x )$ .

The order $m$ formula for computing $y ( x _ { n } ) \ = \ y ( x _ { n - 1 } + h )$ using these functions, evaluated at $x = x _ { n - 1 }$ and $y = y _ { n - 1 }$ , is

$$
y _ { n } = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) + { \frac { h ^ { 2 } } { 2 ! } } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } )
$$

Most serious investigations of this method have been concerned, above all, with the automatic generation of procedures for generating the second, third, . . derivative functions $f _ { 2 }$ , $f _ { 3 }$ , . . . from a given first derivative function $f$ . While this aspect of the Taylor series method is more within the scope of algebraic manipulation than of numerical analysis, there are other important aspects which arise, just as for other methods. These include error estimation, order selection and stepsize control.

Although many individuals and teams have made important contributions to the use of Taylor series methods, we mention three in particular. The program of Gibbons (1960), using a computer with the limited memory available at that time, used a recursive technique to generate the Taylor coefficients automatically. A similar approach using greater sophistication and more powerful computational tools was used by Barton, Willers and Zahar (1971). The work of Moore (1964) is especially interesting, in that it uses interval arithmetic and supplies rigorous error bounds for the computed solution.
