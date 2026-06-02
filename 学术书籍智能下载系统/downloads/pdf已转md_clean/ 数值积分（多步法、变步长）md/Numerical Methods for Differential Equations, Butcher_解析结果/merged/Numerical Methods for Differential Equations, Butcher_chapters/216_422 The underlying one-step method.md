# 422 The underlying one-step method

Although linear multistep methods seem to be at the opposite end of the spectrum from Runge–Kutta methods, there is a very close link between them. Suppose the method $\lfloor \alpha , \beta \rfloor$ is preconsistent and stable, and consider the equation

$$
\begin{array} { r l } & { 1 - \alpha _ { 1 } \eta ^ { - 1 } - \alpha _ { 2 } \eta ^ { - 2 } - \cdot \cdot \cdot - \alpha _ { k } \eta ^ { - k } } \\ & { \qquad - \beta _ { 0 } D - \beta _ { 1 } \eta ^ { - 1 } D - \beta _ { 2 } \eta ^ { - 2 } D - \cdot \cdot \cdot - \beta _ { k } \eta ^ { - k } D = 0 , } \end{array}
$$

where $\eta ~ \in ~ G _ { 1 }$ . In Theorem 422A, we will show that (422a) has a unique solution.

Although $\eta$ does not represent a Runge–Kutta method, it does represent a process for progressing a numerical approximation through a single time step. Suppose that the method is started using

$$
y _ { i } = y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { \eta ^ { i } ( t ) h ^ { r ( t ) } } { \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) ) , \quad i = 0 , 1 , 2 , \ldots , k - 1 ,
$$

corresponding to the group element $\eta ^ { i }$ ; then this value of $y _ { i }$ will persist for $i = k , k + 1 , \ldots .$ We will show this formally in Theorem 422C.

In the meantime, we remark that convergence of the formal series associated with $\eta ^ { i }$ is not assured, even for $i = 1$ , unless the function $f$ and the value of $h$ are restricted in some appropriate way. In this sense we can regard these ‘B-series’ as formal Taylor series.

What we really want is not $\eta$ satisfying (422a) but the mapping $\Phi$ , say, which corresponds to it. If exponentiation of $\Phi$ is taken to denote compositions, or, for negative powers, compositions of the inverse mapping, then we want to be able to define $\Phi$ by

$$
\begin{array} { r l } & { \mathrm { i d } - \alpha _ { 1 } \Phi ^ { - 1 } - \alpha _ { 2 } \Phi ^ { - 2 } - \cdot \cdot \cdot - \alpha _ { k } \Phi ^ { - k } } \\ & { \quad - h \beta _ { 0 } f - h \beta _ { 1 } ( f \circ \Phi ^ { - 1 } ) - h \beta _ { 2 } ( f \circ \Phi ^ { - 2 } ) - \cdot \cdot \cdot - h \beta _ { k } ( f \circ \Phi ^ { - k } ) = 0 . } \end{array}
$$

Because the corresponding member of $G _ { 1 }$ can be evaluated up to any required order of tree, it is regarded as satisfactory to concentrate on this representation.

Theorem 422A For any preconsistent, stable linear multistep method $\lfloor \alpha , \beta \rfloor$ , there exists a member of the group $G _ { 1 }$ satisfying (422a).

P By preconsistency, $\textstyle \sum _ { i = 1 } ^ { k } \alpha _ { i } = 1$ . Hence, (422a) is satisfied in the case $t = \emptyset$ they each evaluate to zero. Now consider a tree $t$ with $r ( t ) > 0$ and assume

that

$$
\begin{array} { r l } & { 1 ( u ) - \alpha _ { 1 } \eta ^ { - 1 } ( u ) - \alpha _ { 2 } \eta ^ { - 2 } ( u ) - \cdot \cdot \cdot - \alpha _ { k } \eta ^ { - k } ( u ) } \\ & { \qquad - \beta _ { 0 } D ( u ) - \beta _ { 1 } \eta ^ { - 1 } D ( u ) - \beta _ { 2 } \eta ^ { - 2 } D ( u ) - \cdot \cdot \cdot - \beta _ { k } \eta ^ { - k } D ( u ) = 0 , } \end{array}
$$

is satisfied for every tree $u$ satisfying $r ( u ) < r ( t )$ . We will prove that there exists a value of $\eta ( t )$ such that this equation is also satisfied if $u$ is replaced by $t$ . The coefficient of $\eta ( t )$ in $\eta ^ { - \tau } ( t )$ is equal to $i ( - 1 ) ^ { r ( t ) }$ and there are no other terms in $\eta ^ { - i } ( t )$ with orders greater than $r ( t ) - 1$ . Furthermore, all terms on the right-hand side contain only terms with orders less than $r ( t )$ . Hence, to satisfy (422a), with both sides evaluated at $t$ , it is only necessary to solve the equation

$$
( - 1 ) ^ { r ( t ) - 1 } \sum _ { i = 1 } ^ { k } i \alpha _ { i } \eta ( t ) = C ,
$$

where $C$ depends only on lower order trees. The proof by induction on $r ( t )$ is now complete, because the coefficient of $\eta ( t )$ is non-zero, by the stability of the method. $\boxed { \begin{array} { r l } \end{array} }$

Definition 422B Corresponding to a linear multistep method $\lfloor \alpha , \beta \rfloor$ , the member of $G _ { 1 }$ represents the ‘underlying one-step method’.

As we have already remarked, the mapping $\Phi$ in (422b), if it exists in more than a notional sense, is really the object of interest and this really is the underlying one-step method.

Theorem 422C Let $[ \alpha , \beta ]$ denote a preconsistent, stable linear multistep method and let $\eta$ denote a solution of (422a). Suppose that $y _ { i }$ is represented by $\eta ^ { i }$ for $i = 0 , 1 , 2 , \ldots , k - 1$ ; then $y _ { i }$ is represented by $\eta ^ { i }$ for $i = k , k + 1 , \ldots .$ .

Proof. The proof is by induction, and it will only be necessary to show that $y _ { k }$ is represented by $\eta ^ { k }$ , since this is a typical case. Multiply (422a) on the left by $\eta ^ { k }$ and we find that

$$
\begin{array} { r } { \eta ^ { k } - \alpha _ { 1 } \eta ^ { k - 1 } - \alpha _ { 2 } \eta ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } \qquad } \\ { - \beta _ { 0 } \eta ^ { k } D - \beta _ { 1 } \eta ^ { k - 1 } D - \beta _ { 2 } \eta ^ { k - 2 } D - \cdot \cdot \cdot - \beta _ { k } D = 0 , } \end{array}
$$

so that $y _ { k }$ is represented by $\eta ^ { k }$ .

The concept of an underlying one-step method was introduced by Kirchgraber (1986). Although the underlying method cannot be represented as a Runge–Kutta method, it can be represented as a B-series or, what is equivalent, in the manner that has been introduced here. Of more recent developments, the extension to general linear methods (Stoffer, 1993) is of particular interest. This generalization will be considered in Subsection 535.
