# Chapter 1

# Differential and Difference Equations

10 Differential Equation Problems

100 Introduction to differential equations

As essential tools in scientific modelling, differential equations are familiar to every educated person. In this introductory discussion we do not attempt to restate what is already known, but rather to express commonly understood ideas in the style that will be used for the rest of this book.

The aim will always be to understand, as much as possible, what we expect to happen to a quantity which satisfies a differential equation. At the most obvious level, this means predicting the value this quantity will have at some future time. However, we are also interested in more general questions such as the adherence to possible conservation laws or perhaps stability of the long-term solution. Since we emphasize numerical methods, we often discuss problems with known solutions mainly to illustrate qualitative and numerical behaviour.

Even though we sometimes refer to ‘time’ as the independent variable, that is, as the variable on which the value of the ‘solution’ depends, there is no reason for insisting on this interpretation. However, we generally use $x$ to denote the ‘independent’ or ‘time’ variable and $y$ to denote the ‘dependent variable’. Hence, differential equations will typically be written in the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

where

$$
y ^ { \prime } = { \frac { d y } { d x } } .
$$

Sometimes, for convenience, we omit the $x$ in $y ( x )$ .

The terminology used in (100a) is misleadingly simple, because y could be a vector-valued function. Thus, if we are working in RN, and x is permitted to take on any real value, then the domain and range of the function f which

defines a differential equation and the solution to this equation are given by

# f : R  R N  R N , y : R → RN .

Since we might be interested in time values that lie only in some interval $[ a , b ] ,$ we sometimes consider problems in which y : $[ a , b ] \to \mathbb { R } ^ { N } ,$ and f : $[ \overline { { a , b } } ]$ ×RN → RN . When dealing with specific problems, it is often convenient to focus, not on the vector-valued functions f and $y ,$ but on individual components. Thus, instead of writing a differential equation system in the form of (100a), we can write coupled equations for the individual components:

A differential equation for which f is a function not of $x ,$ but of y only, is said to be ‘autonomous’. Some equations arising in physical modelling are more naturally expressed in one form or the other, but we emphasize that it is always possible to write a non-autonomous equation in an equivalent autonomous form. All we need to do to change the formulation is to introduce an additional component $y _ { N + 1 }$ into the y vector, and ensure that this can always maintain the same value as $x ,$ by associating it with the differential equation $y _ { N + 1 } ^ { \prime } =$ 1. Thus, the modified system is

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = f _ { 1 } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { y _ { 2 } ^ { \prime } ( x ) = f _ { 2 } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { \qquad \vdots } \\ & { { y _ { N } ^ { \prime } ( x ) = f _ { N } ( y _ { N + 1 } , y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } } \\ & { y _ { N + 1 } ^ { \prime } ( x ) = 1 . } \end{array}
$$

A system of differential equations alone does not generally define a unique solution, and it is necessary to add to the formulation of the problem a number of additional conditions. These are either ‘boundary conditions’, if further information is given at two or more values of $x$ , or ‘initial conditions’, if all components of $y$ are specified at a single value of $x$ .

If the value of $y ( x _ { 0 } ) = y _ { 0 }$ is given, then the pair of equations

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

is known as an ‘initial value problem’. Our main interest in this book is with exactly this problem, where the aim is to obtain approximate values of $y ( x )$

for specific values of $x$ , usually with $x > x _ { 0 }$ , corresponding to the prediction of the future states of a differential equation system.

Note that for an $N$ -dimensional system, the individual components of an initial value vector need to be given specific values. Thus, we might write

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/f7d2e32b346925824aaec87f4e7aaad8c07f787c07282d1bee9db690d134502e.jpg)

When the problem is formally converted to autonomous form (100c), the value of $\eta _ { N + 1 }$ must be identical to $x _ { 0 }$ , otherwise the requirement that $y _ { N + 1 } ( x )$ should always equal $x$ would not be satisfied.

For many naturally occurring phenomena, the most appropriate form in which to express a differential equation is as a high order system. For example, an equation might be of the form

$$
y ^ { ( n ) } = \phi \left( x , y , y ^ { \prime } , y ^ { \prime \prime } , \ldots , y ^ { ( n - 1 ) } \right) ,
$$

with initial values given for $y ( x _ { 0 } ) , y ^ { \prime } ( x _ { 0 } ) , y ^ { \prime \prime } ( x _ { 0 } ) , \ldots , y ^ { ( n - 1 ) } ( x _ { 0 } )$ . Especially important in the modelling of the motion of physical systems subject to forces are equation systems of the form

$$
\begin{array} { c } { y _ { 1 } ^ { \prime \prime } ( x ) = f _ { 1 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ { y _ { 2 } ^ { \prime \prime } ( x ) = f _ { 2 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ { \vdots \qquad \vdots } \\ { y _ { N } ^ { \prime \prime } ( x ) = f _ { N } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \end{array}
$$

where the equations, though second order, do have the advantages of being autonomous and without $y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } , \ldots , y _ { N } ^ { \prime }$ occurring amongst the arguments of $f _ { 1 } , f _ { 2 } , \ldots , f _ { N }$ .

To write (100f) in what will become our standard first order system form, we can introduce additional components $y _ { N + 1 } , y _ { N + 2 } , \ldots , y _ { 2 N } .$ . The differential equation system (100f) can now be written as the first order system

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } ( x ) = y _ { N + 1 } , } \\ & { y _ { 2 } ^ { \prime } ( x ) = y _ { N + 2 } , } \\ & { \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { y _ { N } ^ { \prime } ( x ) = y _ { 2 N } , } \\ & { y _ { N + 1 } ^ { \prime } ( x ) = f _ { 1 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { y _ { N + 2 } ^ { \prime } ( x ) = f _ { 2 } ( y _ { 1 } , y _ { 2 } , \ldots , y _ { N } ) , } \\ & { \quad \quad \quad \quad \quad \quad \quad \vdots } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$
