# 320 Methods of orders less than 4

It will be shown in Subsection 324 that, for an explicit method to have order $p$ , at least $s = p$ stages are necessary. We derive methods up to $p = 3$ , with exactly $p$ stages, and then discuss briefly the advantages of using $s = p + 1$ .

For $s = p = 1$ there is no choice beyond the Euler method with tableau

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/9618c77e2502a58024623115b20e87f83cfa797f034b711167351b780177be93.jpg)

For $s = p = 2$ , we have a one-parameter family of methods of the form

$$
\frac { 0 } { \frac { c _ { 2 } } { 1 - \frac { 1 } { 2 c _ { 2 } } ~ \frac { 1 } { 2 c _ { 2 } } } }
$$

which satisfies the conditions $b _ { 1 } + b _ { 2 } = 1$ and $\begin{array} { r } { b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , corresponding to the trees and .

For $s = p = 3$ , we must satisfy four conditions, which are shown together with the corresponding trees as follows:

$$
\begin{array} { c c c } { \cdot } & { b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 , } \\ { \vdots } & { } & { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \displaystyle { \frac { 1 } { 2 } } , } \\ { \big \nvee } & { } & { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \displaystyle { \frac { 1 } { 3 } } , } \\ { \vdots } & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } = \displaystyle { \frac { 1 } { 6 } } . } \end{array}
$$

To solve these equations in the most straightforward manner, it is convenient to treat $c _ { 2 }$ and $c _ { 3 }$ as free parameters and to carry out three steps. First, solve for $b _ { 2 }$ and $b _ { 3 }$ from the linear system given by (320b) and (320c). Secondly, evaluate $b _ { 1 }$ from (320a). Finally, solve for $a _ { 3 2 }$ from (320d). This plan will run into difficulties if the matrix of coefficients in (320b) and (320c) is singular; that is, if $c _ { 2 } c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = 0$ . Assuming this does not occur, we have a further difficulty if the solution to (320b) and (320c) results in $b _ { 3 } = 0$ . This anomaly, which occurs if $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , makes it impossible to solve (320d). A more careful analysis is necessary to resolve these difficulties, and it is possible to identify three cases where a solution can be found. These are

$$
\begin{array} { l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \neq 0 \neq c _ { 3 } \neq c _ { 2 } \neq \frac { 2 } { 3 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { c _ { 2 } = c _ { 3 } = \frac { 2 } { 3 } , b _ { 3 } \neq 0 , } } \\ { { \mathrm { ~ I I I ~ } } } & { { c _ { 2 } = \frac { 2 } { 3 } , c _ { 3 } = 0 , b _ { 3 } \neq 0 . } } \end{array}
$$

The coefficient tableaux for the three cases are summarized as follows, with the general form of the tableau given in each case: for case I we have

for case II,

$$
{ \frac { \displaystyle { \frac { 2 } { 3 } } } { \displaystyle { \frac { 2 } { 3 } } - { \frac { 1 } { 4 b _ { 3 } } } } } { \frac { \frac { 2 } { 3 } } { \frac { 2 } { 4 } } } { \frac { \frac { 2 } { 3 } } { \frac { 1 } { 4 } - b _ { 3 } } } { \frac { \frac { 1 } { 6 } } { b _ { 3 } } }  ; 
$$

and for case III,
