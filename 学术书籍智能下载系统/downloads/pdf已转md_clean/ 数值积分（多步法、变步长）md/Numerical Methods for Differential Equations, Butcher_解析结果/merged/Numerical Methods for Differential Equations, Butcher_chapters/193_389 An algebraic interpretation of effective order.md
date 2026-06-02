# 389 An algebraic interpretation of effective order

The concept of conjugacy in group theory provides an algebraic interpretation of effective order. Two members of a group, $x$ and $z$ , are conjugate if there exists a member $y$ of the group such that $y x y ^ { - 1 } = z$ . We consider the group $G _ { 1 } / ( 1 + H _ { p } )$ whose members are cosets of $G _ { 1 }$ corresponding to sets of Runge– Kutta methods, which give identical numerical results in a single step to within $O ( h ^ { p + 1 } ) .$ In particular, $E ( 1 + H _ { p } )$ is the coset corresponding to methods which reproduce the exact solution to within $O ( h ^ { p + 1 } )$ . This means that a method, with corresponding group element $\alpha$ , is of order $p$ if

$$
\alpha \in E ( 1 + H _ { p } ) .
$$

If a second method with corresponding group element $\beta$ exists so that the conjugacy relation

$$
\beta \alpha \beta ^ { - 1 } \in E ( 1 + H _ { p } )
$$

holds, then the method corresponding to $\alpha$ has effective order $p$ and the method corresponding to $\beta$ has the role of perturbing method.

We use this interpretation to find conditions for effective orders up to 5. To simplify the calculation, we use a minor result:

Lemma 389A A Runge–Kutta method with corresponding group element $\alpha$ has effective order $p$ if and only if (389a) holds, where $\beta$ is such that $\beta ( \tau ) = 0$ .

Proof. Suppose that (389a) holds with $\beta$ replaced by $\widehat { \beta }$ . Let $\beta = E ^ { ( - \widehat { \beta } ( \tau ) ) } \widehat { \beta }$ , so that $\beta ( \tau ) = 0$ . We then find

$$
\begin{array} { r l } & { \beta \alpha \beta ^ { - 1 } = E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \alpha \left( E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \right) ^ { - 1 } } \\ & { \qquad = E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \alpha \widehat { \beta } ^ { - 1 } E ^ { \widehat { \beta } ( \tau ) } } \\ & { \qquad \in E ^ { - \widehat { \beta } ( \tau ) } E E ^ { \widehat { \beta } ( \tau ) } ( 1 + H _ { p } ) } \\ & { \qquad = E ( 1 + H _ { p } ) . } \end{array}
$$

Once we have found effective order conditions on $\alpha$ and found a corresponding choice of $\beta$ for $\alpha$ satisfying these conditions, we can use Lemma 389A in reverse to construct a family of possible perturbing methods.

To obtain the conditions we need on $\alpha$ we have constructed Table 389(I) based on Table 386(II). In this table, the trees up to order 5 are numbered, just as in the earlier table, and $\beta \alpha \beta ^ { - 1 } \in E ( 1 + H _ { p } )$ is replaced by $\beta \alpha \in E \beta ( 1 + H _ { p } )$ , for convenience. In the order conditions formed from Table 389(I), we regard $\beta _ { 2 }$ , $\beta _ { 3 }$ , . . . as free parameters. Simplifications are achieved by substituting values of $\alpha _ { 1 }$ , $\alpha _ { 2 } , \ldots ,$ as they are found, into later equations that make use of them. The order conditions are

$$
\begin{array} { r l } & { \mathrm { ~ G _ { 1 } ~ - } } \\ & { \mathrm { ~ G _ { 2 } ~ - } } \\ & { \mathrm { ~ G _ { 3 } ~ - } } \\ & { \mathrm { ~ C _ { 4 } ~ - } } \\ & { \mathrm { ~ C _ { 4 } ~ - } } \\ & { \mathrm { ~ C _ { 5 } ~ - } } \\ & { \mathrm { ~ C _ { 6 } ~ - } } \\ & { \mathrm { ~ C _ { 7 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ &  \mathrm  ~ C \end{array}
$$

For explicit Runge–Kutta methods with fourth (effective) order, four stages are still necessary, but there is much more freedom than for methods with the same classical order. For fifth effective order there is a real saving in that only five stages are necessary. For the fourth order case, we need to choose the coefficients of the method so that

$$
\begin{array} { l } { \alpha _ { 1 } = 1 , } \\ { \alpha _ { 2 } = \frac { 1 } { 2 } , } \\ { \alpha _ { 4 } = \frac { 1 } { 6 } , } \\ { \alpha _ { 8 } = \frac { 1 } { 2 4 } } \end{array}
$$

Effective order conditions   

<table><tr><td></td><td></td><td>ir(ti) (βa)(ti)</td><td>(Eβ)(ti)</td></tr><tr><td>1</td><td>1</td><td>α1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>α+β</td><td>β+</td></tr><tr><td>3</td><td>3</td><td>α3+β</td><td>β+2β+1</td></tr><tr><td>4</td><td>3</td><td>α4 + βα1+ β4</td><td>β4+β+</td></tr><tr><td>5</td><td>4</td><td>α5+β5</td><td>β5 +3β+3β+</td></tr><tr><td>6</td><td>4</td><td>α6+β2α2+ β6</td><td>β6+β+β+β+</td></tr><tr><td>7</td><td>4</td><td>α7+βα1+β7</td><td>β7+2β4+β+12</td></tr><tr><td>8</td><td>4</td><td>α8+βα2+β4α1+β8</td><td>β8+β+β+</td></tr><tr><td>9</td><td>5</td><td>αg+β</td><td>βg+4β5+6β+4β2+½</td></tr><tr><td>10</td><td>5</td><td>α10 + β2α3+ β10</td><td>β10+2β6+β5+β4+β+2β2+10</td></tr><tr><td>11</td><td>5</td><td>α11 + βα2 + β11</td><td>β11+β7+2β6+2β4+β3+β+15</td></tr><tr><td>12</td><td>5</td><td>α12+β2α3+β4α2+ β12</td><td>β12+β8+β6+β4+β+β+30</td></tr><tr><td>13</td><td>5</td><td>α13+2β2α4+β²α1+ β13</td><td>β13+2β6+β4+β+β+20</td></tr><tr><td>14</td><td>5</td><td>α14 + β5α1+ β14</td><td>β14+3β7+3β4+β+20</td></tr><tr><td>15</td><td>5</td><td>α15 +β2α4++β6α1+ β15</td><td>β15+β8+β+β+β+0</td></tr><tr><td>16</td><td>5</td><td>α16+ βα2+ β7α1+β16</td><td>β16+2β8+β4+β+</td></tr><tr><td>17</td><td></td><td></td><td>α17+β2α4+β4a2+β8α1+β17 β17+β8+1β4+β²+ 120</td></tr></table>

and so that the equation formed by eliminating the various $\beta$ values from the equations for $\alpha _ { 3 }$ , $\alpha _ { 5 }$ , $\alpha _ { 6 }$ an $\alpha _ { 7 }$ is satisfied. This final effective order condition is

$$
\begin{array} { r } { \alpha _ { 3 } - \alpha _ { 5 } + 2 \alpha _ { 6 } - \alpha _ { 7 } = \frac { 1 } { 4 } , } \end{array}
$$

and the five condition equations written in terms of the coefficients in a fourstage method are

$$
\begin{array} { c } { { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } } \\ { { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac 1 2 , } } \\ { { b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } a _ { 4 2 } c _ { 2 } + b _ { 4 } a _ { 4 3 } c _ { 3 } = \frac 1 6 , } } \\ { { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \frac 1 { 2 4 } , } } \\ { { b _ { 2 } c _ { 2 } ^ { 2 } ( 1 - c _ { 2 } ) + b _ { 3 } c _ { 3 } ^ { 2 } ( 1 - c _ { 3 } ) + b _ { 4 } c _ { 4 } ^ { 2 } ( 1 - c _ { 4 } ) } } \\ { { + b _ { 3 } a _ { 3 2 } c _ { 2 } ( 2 c _ { 3 } - c _ { 2 } ) + b _ { 4 } a _ { 4 2 } c _ { 2 } ( 2 c _ { 4 } - c _ { 2 } ) + b _ { 4 } a _ { 4 3 } c _ { 3 } ( 2 c _ { 4 } - c _ { 3 } ) } } \end{array}
$$

Group elements associated with a special effective order 4 method   

<table><tr><td>t</td><td></td><td></td><td>E(t）α(t)β(t)(β-1E)(t)(β-1Eβ())(t)</td><td></td></tr><tr><td>·</td><td>1</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>：</td><td>1</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>?</td><td>N</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>…</td><td></td><td>1 1</td><td>1</td><td>11+r3 72</td></tr><tr><td>Y</td><td>4</td><td>4 1</td><td>1</td><td>26+r4</td></tr><tr><td>?</td><td></td><td>108</td><td></td><td>108</td></tr><tr><td></td><td>1</td><td>品</td><td>1 13</td><td>26+3r³+r4</td></tr><tr><td>丫 i</td><td></td><td>1</td><td>216 108 1 19</td><td>216 19+6r3-r4</td></tr></table>

We do not attempt to find a general solution to these equations, but instead explore a mild deviation from full classical order. In fact, we assume that the perturbing method has $\beta _ { 2 } = \beta _ { 3 } = 0$ , so that we now have the conditions

$$
\begin{array} { r l r } & { } & { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ & { } & { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac { 1 } { 2 } , } \\ & { } & { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } = \frac { 1 } { 3 } , } \\ & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } a _ { 4 2 } c _ { 2 } + b _ { 4 } a _ { 4 3 } c _ { 3 } = \frac { 1 } { 6 } , } \\ & { } & { b _ { 2 } c _ { 2 } ^ { 3 } + b _ { 3 } c _ { 3 } ^ { 3 } + b _ { 4 } c _ { 4 } ^ { 3 } = \frac { 1 } { 4 } , } \\ & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } ( 2 c _ { 3 } - c _ { 2 } ) + b _ { 4 } a _ { 4 2 } c _ { 2 } ( 2 c _ { 4 } - c _ { 2 } ) + b _ { 4 } a _ { 4 3 } c _ { 3 } ( 2 c _ { 4 } - c _ { 3 } ) = \frac { 1 } { 4 } , } \\ & { } & { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } . } \end{array}
$$

Methods satisfying these more general conditions do not need to have $c _ { 4 } = 1$ and we can find, for example, the tableau

$$
\begin{array}{c} \begin{array} { r } { { \left. \begin{array} { l } { 0 } \\ { \frac { 1 } { 3 } } \\ { \frac { 2 } { 3 } } \\ { \frac { 5 } { 6 } } \end{array} \right| } \ \frac { 1 } { 6 } \quad { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 1 0 } } \quad { \frac { 5 } { 2 4 } } \quad { 0 } \quad { \frac { 5 } { 8 } } } \end{array} \ . \qquad \end{array}
$$

A suitable starting method, which does not advance the solution forward but introduces the correct perturbation so that (389b) faithfully reproduces this perturbation to within order 4, is given by the tableau

$$
\begin{array} { r }  { \left. \begin{array} { c } { 0 } \\ { 1 } \\ { \frac { 2 } { 3 } } \\ { \frac { 1 } { 3 } } \\ { - \frac { 1 } { 2 4 } \end{array}  } _ { \begin{array} { c } { 1 } \\ { \frac { 2 } { 3 } } \\ { - \frac { 1 } { 3 } } \end{array} } \qquad \begin{array} { c } { 2 } \\ { \frac { 2 } { 3 } } \\ { \frac { 1 } { 8 } } \end{array} \qquad . } \end{\right|array} \end{array}
$$

The freedom that lay at our disposal in selecting this starting procedure was used to guarantee a certain simplicity in the choice of finishing procedure. This was in fact decided on first, and has a tableau identical with (389b) except for the $b ^ { \prime }$ vector. The reason for this choice is that no extra work is required to obtain an output value because the stages in the final step will already have been completed. The tableau for this final step is

$$
\begin{array} { r } { { \left. \begin{array} { l } { 0 } \\ { \frac { 1 } { 3 } } \\ { \frac { 2 } { 3 } } \\ { \frac { 5 } { 6 } } \end{array} \right| } _ { \frac { 5 } { 2 4 } } { \left. \begin{array} { l l l l } { 1 } & { } & { } & { } \\ { \frac { 1 } { 3 } } & { } & { } & { } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 2 } } & { } & { } \\ { \frac { 5 } { 2 4 } } & { 0 } & { \frac { 5 } { 8 } } \\ { \frac { 3 } { 2 0 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 4 } } & { \frac { 4 } { 1 5 } } \end{array} \right. } . } \end{array}
$$

This example method has not been optimized in any way, and is therefore not proposed for a practical computation. On the other hand, it shows that the search for efficient methods need not be restricted to the class of Runge– Kutta methods satisfying classical order conditions. It might be argued that methods with only effective order cannot be used in practice because stepsize change is not possible without carrying out a finishing step followed by a new start with the modified stepsize. However, if, after carrying out a step with the method introduced here, a stepsize change from $h$ to $r h$ is required, then this can be done by simply adding one additional stage and choosing the vector $b ^ { \top }$ which depends on $r$ . The tableau for this $h$ -adjusting step is

<table><tr><td></td><td colspan="5"></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>5</td><td></td></tr><tr><td></td><td>1</td><td>1</td><td>4</td><td></td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td></tr><tr><td>3+r3-2r4 20</td><td>2-3r3+4r4 6</td><td>1-3r3+2r4 4</td><td>4+3r3-r4 r3-r4 15</td></tr></table>

Rather than carry out detailed derivations of the various tableaux we have introduced, we present in Table 389(II) the values of the group elements in $G _ { 1 } / ( 1 + H _ { 4 } )$ that arise in the computations. These group elements are $\beta$ , corresponding to the starting method (389c), $\alpha$ for the main method (389b), $\beta ^ { - 1 } E$ corresponding to the finishing method (389d) and, finally, $\beta ^ { - 1 } E \beta ^ { ( r ) }$ for the stepsize-adjusting method (389e). For convenience in checking the computations, $E$ is also provided.

# Exercises 38

38.1 Find the B-series for the Euler method

$$
{ \frac { 0 \ \biggr \vert \ 0 } { \biggl \vert \ 1 } } \ .
$$

38.2 Find the B-series for the implicit Euler method

$$
{ \frac { 1 \left| 1 \right| } { 1 } } \ .
$$

38.3 Show that the two Runge–Kutta methods

$$
{ \begin{array} { r l r l r l r l r l } { 0 } & { 0 } & & { 0 } & & { } & & { 0 } \\ { 1 } & { 1 } & { - 1 } & & { 1 } & & { } & & { 1 } \\ { \frac { 1 } { 2 } } & { 1 } & { 1 } & { - 1 } & { } & & { } & & { 0 } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } & { \frac { 1 } { 4 } } & { } & & { } & & { } \end{array} } \qquad { \begin{array} { r l r l r l } { 0 } & { { } } & { 0 } & { { } } & { 1 } & { } & { 0 } & { } \\ { 1 } & { { } } & { { } } & { 0 } & { { } } & { { \frac { 1 } { 4 } } } & { } \\ { 2 } & { { } } & { 0 } & { - 2 } & { } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { { } } & { 1 } & { } & { { } } \end{array} }
$$

are P-equivalent. Find a method with only two stages equivalent to each of them.

38.4 Let $m _ { 1 }$ and $m _ { 2 }$ denote the Runge–Kutta methods

$$
\begin{array} { c }  { { \frac { 1 } { 2 } - \frac { 1 } { 6 } \sqrt { 3 } \left| \begin{array} { c c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \frac { 1 } { 6 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \frac { 1 } { 4 } } } \end{array} \right| \begin{array} { c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 6 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \frac { 1 } { 4 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \frac { 1 } { 4 } } } \end{array} , } } \\ { { { \frac { 1 } { 2 } } } } &  { { \frac { 1 } { 6 } } } \\ { { m _ { 2 } = \underbrace { - \frac { 1 } { 2 } + \frac { 1 } { 6 } \sqrt { 3 } } } } & { { \left| \begin{array} { c c } { { \ - \frac { 1 } { 4 } } } & { { \ - \frac { 1 } { 4 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \ - \frac { 1 } { 4 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \ - \frac { 1 } { 4 } } } \end{array} \right| \begin{array} { c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 6 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \ - \frac { 1 } { 2 } } } & { { \ - \frac { 1 } { 2 } } } \end{array} . } } \end{array}
$$

Show that $[ m _ { 2 } ] = [ m _ { 1 } ] ^ { - 1 }$ .

38.5 Show that $D \in X$ is the homomorphic partner of $[ m ]$ , where

$$
m = { \frac { 0 } { 0 } } \left| { \begin{array} { l } { 0 } \\ { 1 } \end{array} } \right. .
$$
