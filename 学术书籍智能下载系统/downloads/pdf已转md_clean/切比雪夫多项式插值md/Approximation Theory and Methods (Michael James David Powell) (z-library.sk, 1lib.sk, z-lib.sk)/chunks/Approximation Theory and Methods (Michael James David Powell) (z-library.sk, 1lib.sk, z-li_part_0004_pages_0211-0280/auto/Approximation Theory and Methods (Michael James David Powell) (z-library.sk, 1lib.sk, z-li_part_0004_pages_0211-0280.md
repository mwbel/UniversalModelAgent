# 17

# The uniform boundedness theorem

# 17.1 Preliminary results

If an approximation to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is required to high accuracy, then it is usual to calculate a sequence of approximations $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ ,until the accuracy is achieved. Therefore it may be helpful to know whether the sequence converges uniformly to $f .$ The uniform boundedness theorem gives one of the most useful methods for answering this question.A simple version of it is proved in Section 17.2, which implies that, if the operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , \ldots \right\}$ are linear, then uniform convergence is obtained for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,only if the sequence of norms $\{ \| X _ { n } \|$ ； $n = 0 , 1 , 2 , \ldots \}$ is bounded. Because expressions (13.29) and (16.28) give the inequality

$$
\| R _ { n } \| _ { \infty } > ( 4 / \pi ^ { 2 } ) \ln { ( n + 1 ) } ,
$$

it follows,for example, that there exists $f$ in $\mathcal { C } [ - 1 , 1 ]$ such that the sequence of approximations $\{ R _ { n } f ; n = 0 , 1 , 2 , . . . \}$ fails to converge to $f .$ Moreover, because the work of Section 17.2 applies also to the approximation of functions in $\mathcal { C } _ { 2 \pi } ,$ the bound (16.28) implies that there exist continuous periodic functions whose Fourier series approximations do not converge uniformly.

Therefore Section 17.3 addresses the question whether there is a sequence of operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , . . . \right\}$ for calculating approximations to functions in $\mathcal { C } _ { 2 \pi }$ ，that is more suitable than the Fourier series sequence $\{ S _ { n } ; n = 0 , 1 , 2 , \ldots \}$ .We find the remarkable result that, if $X _ { n }$ is linear, if $X _ { n } f$ is in ${ \mathcal { Q } } _ { n }$ for all $f ,$ and if the projection condition

$$
X _ { n } f = f , \qquad f \in { \mathcal { Q } } _ { n } ,
$$

is satisfied, then the norm $\| X _ { n } \| _ { \infty }$ cannot be less than $\| \pmb { S _ { n } } \| _ { \infty }$ .Hence, in order to obtain uniform convergence, it is necessary to give up the projection condition, or to give up the linearity of the operator. A similar conclusion is reached for approximation by algebraic polynomials in Section 17.4. The main theory of the chapter requires the definitions and elementary results that are mentioned below.

In order to prove the uniform boundedness theorem we make use of ‘Cauchy sequences’ and ‘complete’ normed linear spaces.We note, therefore, that the sequence $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ is a Cauchy sequence if, for any $\pmb \varepsilon > 0$ ,there exists an integer $N$ such that the difference $\| f _ { i } - f _ { j } \|$ is less than $\pmb \varepsilon$ for all $i \geq N$ and $j \geq N .$ Further,a normed linear space is complete if every Cauchy sequence is convergent. In particular, the space $\mathcal { C } [ a , b ]$ is complete when the norm is the $\infty$ -norm,which allows Theorem 17.2 to be applied to $\mathcal { C } [ a , b ]$

We also make use of ‘fundamental sets'. The set $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ in a normed linear space $\mathcal { B }$ is called fundamental if,for any $f$ in $\mathcal { B }$ and any $\pmb \varepsilon > 0$ , there exist an integer $k$ and coefficients $\{ a _ { i } ; i = 0 , 1 , \ldots , k \}$ such that the element

$$
\phi = \sum _ { i = 0 } ^ { k } a _ { i } f _ { i }
$$

satisfies the condition

$$
\left\| f - \phi \right\| < \varepsilon .
$$

For example, the set of polynomials $\{ f _ { i } ( x ) = x ^ { i } ; a \leqslant x \leqslant b ; i = 0 , 1 , 2 , . . . \}$ is fundamental in $\mathcal { C } [ a , b ]$

One application of fundamental sets is to show that two bounded linear operators, $L _ { 1 }$ and $L _ { 2 }$ say, from $\mathscr { B }$ to $\mathcal { B }$ are equal. Clearly, if $\{ f _ { i } ; i =$ $0 , 1 , 2 , \ldots \}$ is a fundamental set, then the operators are equal only if the equations

$$
L _ { 1 } f _ { i } = L _ { 2 } f _ { i } , \qquad i = 0 , 1 , 2 , \ldots ,
$$

are satisfied. The following argument gives the useful result that the conditions (17.5) are sufficient for the operators to be the same.

Suppose that the equations (17.5） hold, but that $L _ { 1 }$ and $\mathbf { { { L } } } _ { 2 }$ are different. Then there exists $f$ in $\mathcal { B }$ such that $L _ { 1 } f$ is not equal to $L _ { 2 } f .$ We let $\pmb \varepsilon$ be the positive number

$$
\varepsilon = \big \| L _ { 1 } f - L _ { 2 } f \big \| / [ \big \| L _ { 1 } \big \| + \big \| L _ { 2 } \big \| ] ,
$$

and we let expression (17.3) be an element of $\mathcal { B }$ that satisfies the bound (17.4). The properties of norms,the linearity of the operators,and

condition (17.5) imply the relation

$$
\begin{array} { r l } & { \left\| L _ { 1 } f - L _ { 2 } f \right\| = \left\| L _ { 1 } ( f - \phi ) - L _ { 2 } ( f - \phi ) \right\| } \\ & { \qquad \leqslant [ \left\| L _ { 1 } \right\| + \left\| L _ { 2 } \right\| ] \| f - \phi \| } \\ & { \qquad < \varepsilon [ \left\| L _ { 1 } \right\| + \left\| L _ { 2 } \right\| ] , } \end{array}
$$

but this relation contradicts the definition (17.6). Therefore the equations (17.5)are suitable for showing that two operators are equal.

# 17.2 Tests for uniform convergence

The two theorems of this section are useful for testing whether a sequence of linear operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , \ldots \right\}$ from $\mathcal { B }$ to $\mathcal { B }$ has the property that $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges to $f$ for all $f$ in $\mathscr { B }$

# Theorem 17.1

Let $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ be a fundamental set in a normed linear space $\mathcal { B }$ ,and let $\left\{ X _ { n } ; n = 0 , 1 , 2 , . . . \right\}$ be a sequence of bounded linear operators from $\mathcal { B }$ to $\mathcal { B }$ .The equations

$$
\operatorname* { l i m } _ { n \to \infty } \big \| f _ { i } - X _ { n } f _ { i } \big \| = 0 , \qquad i = 0 , 1 , 2 , \ldots ,
$$

are necessary and sufficient conditions for the sequence $\{ X _ { n } f ; n =$ $0 , 1 , 2 , \ldots \}$ to converge to $f$ for all $f$ in $\mathscr { B }$

Proof. Clearly the equations are necessary. To prove that they are sufficient, we let $f$ be a general element of $\mathcal { B }$ . The definition of a fundamental set implies that, for any $\varepsilon > 0$ ,there exists a function of the form (17.3) that satisfies the condition

$$
\begin{array} { r } { \left\| f - \phi \right\| \leqslant \frac { 1 } { 2 } \varepsilon / ( M + 1 ) , } \end{array}
$$

where $M$ is a fixed upper bound on the norms $\left\{ \left\| X _ { n } \right\| ; n = 0 , 1 , 2 , \ldots \right\}$ Further, equation (17.8) implies that there is an integer $N ,$ such that the coefficients of expression (17.3) satisfy the bound

$$
\begin{array} { r } { \| f _ { i } - X _ { n } f _ { i } \| \leqslant \frac { 1 } { 2 } \varepsilon \bigg / \underset { j = 0 } { \overset { k } { \sum } } | a _ { j } | , \qquad i = 0 , 1 , \dots , k , } \end{array}
$$

for all $n \geqslant N .$ It follows from the properties of norms,and from the linearity of the operators, that the inequality

$$
\begin{array} { l } { \displaystyle \| f - X _ { n } f \| \leqslant \| ( f - \phi ) - X _ { n } ( f - \phi ) \| + \| \phi - X _ { n } \phi \| } \\ { \displaystyle \leqslant ( M + 1 ) \| f - \phi \| + \| \sum _ { i = 0 } ^ { k } a _ { i } ( f _ { i } - X _ { n } f _ { i } ) \| } \\ { \displaystyle \leqslant ( M + 1 ) \| f - \phi \| + \sum _ { i = 0 } ^ { k } \left| a _ { i } \right| \| f _ { i } - X _ { n } f _ { i } \| } \\ { \displaystyle \leqslant \varepsilon , \qquad n \geqslant N , } \end{array}
$$

is satisfied, which completes the proof of the theorem.

Because many algorithms for calculating spline approximations are bounded linear operators,Theorem 17.1 is useful to the work of the last seven chapters.The next theorem shows that, if the norms $\{ \Vert X _ { n } \Vert$ ； $n =$ $0 , 1 , 2 , \ldots \}$ are unbounded, then there is an unequivocal answer to the convergence question of this section.

# Theorem 17.2 (uniform boundedness)

Let $\mathcal { B }$ be a complete normed linear space,and let $\{ X _ { n } ; n =$ $0 , 1 , 2 , \ldots \}$ be a sequence of linear operators from $\mathcal { B }$ to $\mathcal { B }$ If the sequence of norms $\{ \Vert X _ { n } \Vert$ ； $n = 0 , 1 , 2 , \ldots \}$ is unbounded, then there exists an element, $f ^ { * }$ say, in $\mathcal { B }$ ，such that the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ diverges.

Proof. Because it is sufficient to show that a subsequence of $\{ X _ { n } f ^ { * } ; n = { }$ $0 , 1 , 2 , \ldots \}$ diverges,we may work with a subset of the sequence of operators. We may choose operators whose norms diverge at an arbitrarily fast rate. Therefore we assume, without loss of generality, that the conditions

$$
\| X _ { n } \| \geqslant ( 2 0 n ) 4 ^ { n } , \qquad n = 0 , 1 , 2 , \ldots ,
$$

are satisfied. The method of proof is to use these conditions to construct a Cauchy sequence $\{ f _ { k } ; k = 0 , 1 , 2 , \ldots \} ,$ ，whose limit $f ^ { * }$ is such that the numbers $\left\{ \left\| X _ { n } f ^ { * } \right\| ; n = 0 , 1 , 2 , . . . \right\}$ diverge.

The terms of the Cauchy sequence depend on elements $\{ \phi _ { n } ; n =$ $0 , 1 , 2 , \ldots \}$ of $\mathcal { B }$ that satisfy the conditions

$$
\begin{array} { l } { \displaystyle \| \phi _ { n } \| = 1 } \\ { \displaystyle \| X _ { n } \phi _ { n } \| \geqslant 0 . 8 \| X _ { n } \| } \end{array} \} , \quad n = 0 , 1 , 2 , \ldots .
$$

The definition of $\| X _ { n } \|$ implies that these elements exist. We let $f _ { 0 } = \phi _ { 0 }$ ， and, for $k \geqslant 1 , f _ { k }$ has the form

$$
f _ { k } = \Big \{ \begin{array} { l l } { \mathrm { e i t h e r } f _ { k - 1 } } \\ { \mathrm { o r } f _ { k - 1 } + ( \frac 3 4 ) ( \frac 1 4 ) ^ { k } \phi _ { k } , } \end{array}
$$

where the choice depends on $\| X _ { k } f _ { k - 1 } \|$ and will be made precise later. In all cases expression (17.14) implies that for $j > k$ the bound

$$
\| f _ { j } - f _ { k } \| \leqslant \sum _ { i = k + 1 } ^ { j } \ ( \frac { 3 } { 4 } ) ( \frac { 1 } { 4 } ) ^ { i } \| \phi _ { i } \| < ( \frac { 1 } { 4 } ) ^ { k + 1 }
$$

is obtained. Therefore $\left\{ f _ { k } ; k = 0 , 1 , 2 , \ldots \right\}$ is a Cauchy sequence, and its limit $f ^ { * }$ satisfies the condition

$$
\begin{array} { r } { \left\| f ^ { * } - f _ { k } \right\| \leqslant ( \frac { 1 } { 4 } ) ^ { k + 1 } , \qquad k = 0 , 1 , 2 , \ldots , } \end{array}
$$

which gives the inequality

$$
\begin{array} { r l } {  { \big \| X _ { n } f ^ { * } \big \| \geqslant \big \| X _ { n } f _ { n } \big \| - \big \| X _ { n } ( f ^ { * } - f _ { n } ) \big \| } } \\ & { \geqslant \big \| X _ { n } f _ { n } \big \| - \big ( \frac { 1 } { 4 } \big ) ^ { n + 1 } \big \| X _ { n } \big \| . } \end{array}
$$

It follows that the relation

$$
\begin{array} { r } { \| X _ { k } f _ { k } \| \geqslant k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| , \qquad k = 0 , 1 , 2 , \ldots , } \end{array}
$$

would imply the divergence of the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ .We complete the proof of the theorem by showing that the choice (17.14) allows condition (17.18) to be satisfied.

The value of $f _ { 0 }$ is such that condition (17.18) holds when $k = 0$ ,but this case is unimportant. For $k \geqslant 1$ we let $f _ { k } = f _ { k - 1 }$ if this choice satisfies inequality (17.18). Otherwise,when the bound

$$
\| X _ { k } f _ { k - 1 } \| < k + ( \frac 1 4 ) ^ { k + 1 } \| X _ { k } \|
$$

is obtained, $f _ { k }$ is defined by the second line of expression (17.14). Hence the triangle inequality for norms, expressions (17.13) and (17.19), and the bound (17.12) give the relation

$$
\begin{array} { r l } & { \| X _ { k } f _ { k } \| \geqslant \| ( \frac { 3 } { 4 } ) ^ { \iota } ( \frac { 1 } { 4 } ) ^ { k } X _ { k } \phi _ { k } \| - \| X _ { k } f _ { k - 1 } \| } \\ & { \qquad > 0 . 6 ( \frac { 1 } { 4 } ) ^ { k } \| X _ { k } \| - [ k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| ] } \\ & { \qquad = [ k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| ] + [ 0 . 1 ( \frac { 1 } { 4 } ) ^ { k } \| X _ { k } \| - 2 k ] } \\ & { \qquad \geqslant k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| , } \end{array}
$$

which establishes expression (17.18). Therefore,for reasons given already, the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ diverges,where $f ^ { * }$ is an element of the complete linear space $\mathcal { B }$ □

Because the spaces $\mathcal { C } [ a , b ]$ and $\mathcal { C } _ { 2 \pi }$ are complete,and because the bound (17.1) applies to both $\| R _ { n } \| _ { \infty }$ and $\| \boldsymbol { S _ { n } } \| _ { \infty }$ ,the theorem proves two of the statements that are made in the first paragraph of this chapter, namely that there exists $f$ in $\mathcal { C } [ - 1 , 1 ]$ such that $\{ R _ { n } f ; n = 0 , 1 , 2 , . . . \}$ diverges, and there exists $f$ in $\mathcal { C } _ { 2 \pi }$ such that $\left\{ S _ { n } f ; n = 0 , 1 , 2 , \ldots \right\}$ diverges.These remarks, however, should not deter one from using the operators $\scriptstyle { R _ { n } }$ and $\pmb { S _ { n } }$ ,because the rate of divergence

$$
\left\| R _ { n } \right\| = \left\| S _ { n } \right\| \sim \ln n
$$

is slow, and in any case divergence cannot occur when $f$ is differentiable. From a practical point of view it is more important to keep in mind that it is unusual to calculate polynomial approximations of high degree.

# 17.3 Application to trigonometric polynomials

In this section we prove the result, mentioned in Section 17.1, that, if $L$ is a bounded linear operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { Q } _ { n }$ ，and if the

projection condition

$$
L f = f , \qquad f \in { \mathcal { Q } } _ { n } ,
$$

is satisfied, then $\| \pmb { L } \| _ { \infty }$ is bounded below by $\| \pmb { S _ { n } } \| _ { \infty }$ . The method of proof depends on the displacement operator $\pmb { D } _ { \pmb { \lambda } }$ from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { C } _ { 2 \pi }$ that is defined by the equation

$$
( D _ { \lambda } f ) ( x ) = f ( x + \lambda ) , \qquad - \infty < x < \infty ,
$$

where $\pmb { \lambda }$ is any real parameter, and where $f$ is any function in $\mathcal { C } _ { 2 \pi }$ It also depends on the operator

$$
G = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } D _ { - \lambda } L D _ { \lambda } \mathrm { d } \lambda .
$$

Before beginning the proof of the main result, the meaning of this integral is explained.

For any $f$ in $\mathcal { C } _ { 2 \pi } ,$ we let $f _ { \lambda }$ be the function

$$
f _ { \lambda } = D _ { - \lambda } L D _ { \lambda } f ,
$$

which is also in $\mathcal { C } _ { 2 \pi }$ .For any fixed value of the variable $\pmb { x }$ , we regard $f _ { \lambda } ( x )$ as a function of $\lambda$ .Equation (17.24) means that $G f$ is the function

$$
( G f ) ( x ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f _ { \lambda } ( x ) \mathrm { d } \lambda , \qquad - \infty < x < \infty ,
$$

which is a valid definition, because the following discussion shows that $f _ { \lambda } ( x )$ is a continuous function of $\lambda$

It is straightforward to prove that $D _ { \lambda } f$ depends continuously on $\lambda$ Specifically, because the definition (17.23) implies the equation

$$
( D _ { \mu } f - D _ { \lambda } f ) ( x ) = f ( x + \mu ) - f ( x + \lambda ) , \qquad - \infty < x < \infty ,
$$

we have the bound

$$
\| D _ { \mu } f - D _ { \lambda } f \| _ { \infty } \leqslant \omega _ { f } ( | \mu - \lambda | ) ,
$$

where $\omega _ { f }$ is the modulus of continuity of $f .$ Thus the inequality

$$
\| L D _ { \mu } f - L D _ { \lambda } f \| _ { \infty } \leqslant \| L \| \omega _ { f } ( | \mu - \lambda | )
$$

is satisfied, which shows that the function $L D _ { \lambda } f$ also depends continuously on $\lambda$

To continue the discussion we require the result that the family of functions $\{ L D _ { \lambda } f ; 0 \leqslant \lambda \leqslant 2 \pi \}$ is uniformly continuous.This result holds because the dependence on $\pmb { \lambda }$ is continuous, because the range of $\pmb { \lambda }$ is compact, because each function in the family is continuous in the variable $\pmb { x } ,$ ，and because,due to periodicity,it is sufficient to establish uniform continuity when $x$ is restricted to the compact interval $0 \leqslant x \leqslant 4 \pi$ We let $\omega ^ { * }$ be the modulus of continuity of the family. Therefore,if we replace $f$ by $L D _ { \nu } f$ in expression (17.28), we find that the bound

$$
\begin{array} { r } { \| D _ { \mu } L D _ { \nu } f - D _ { \lambda } L D _ { \nu } f \| \leqslant \omega ^ { * } ( | \mu - \lambda | ) } \end{array}
$$

is obtained for all values of the parameters $\mu , \lambda$ and $\pmb { \nu }$ Moreover expression (17.29),and the fact that the norm of a displacement operator is one,give the condition

$$
\| D _ { - \mu } L D _ { \mu } f - D _ { - \mu } L D _ { \lambda } f \| \leqslant \| L \| \omega _ { f } ( | \mu - \lambda | ) .
$$

We deduce from the last two inequalities and from the definition (17.25) that the relation

$$
\begin{array} { c } { { \left\| f _ { \mu } - f _ { \lambda } \right\| \leqslant \left\| f _ { \mu } - D _ { - \mu } L D _ { \lambda } f \right\| + \left\| D _ { - \mu } L D _ { \lambda } f - f _ { \lambda } \right\| } } \\ { { \leqslant \left\| L \right\| \omega _ { f } ( \left| \mu - \lambda \right| ) + \omega ^ { * } ( \left| \mu - \lambda \right| ) } } \end{array}
$$

holds, which completes the demonstration that $f _ { \lambda }$ is a continuous function of $\lambda$

We note also that the function $G f$ is in $\mathcal { C } _ { 2 \pi }$ ,because it is an average of functions that are in $\mathcal { C } _ { 2 \pi }$ . We are now ready to prove the relation between $\| L \| _ { \infty }$ and $\| S _ { n } \| _ { \infty }$

# Theorem 17.3

If $L$ is any bounded linear operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { Q } _ { n }$ ,that satisfies the projection condition (17.22), then $\| L \| _ { \infty }$ is bounded below by $\| S _ { n } \| _ { \infty }$

Proof. The key to the proof is that,for every operator $L$ that satisfies the conditions of the theorem, the equation

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } D _ { - \lambda } L D _ { \lambda } { \mathrm { ~ d } } \lambda = S _ { n }
$$

is obtained. In order to establish this equation, we recall from Section 17.1 that it is sufficient to prove that the conditions

$$
G f _ { i } = S _ { n } f _ { i } , \qquad i = 0 , 1 , 2 , \ldots ,
$$

hold,where we are using the notation (17.24),and where $\{ f _ { i } ; i =$ $0 , 1 , 2 , \ldots \}$ is any fundamental set in $\mathcal { C } _ { 2 \pi }$ .Theorem 13.1 shows that,in the notation of equations (13.22)-(13.24), the functions $\{ \cos \{ j . \} ; j =$ $0 , 1 , 2 , \ldots \}$ and $\{ \sin \{ j . \} ; j = 1 , 2 , 3 , . . . \}$ together form a fundamental set. Therefore we prove that equation (17.34) is satisfied for each of these functions. We recall from Section 13.2 that the operator $S _ { n }$ gives the equations

$$
S _ { n } f _ { i } = f _ { i } , \qquad f _ { i } \in \mathcal { Q } _ { n } ,
$$

and

$$
\begin{array} { l l } { S _ { n } \cos { \{ j . \} } = 0 } \\ { S _ { n } \sin { \{ j . \} } = 0 } \end{array} \} , \quad \quad j > n ,
$$

which we compare with the equations that are obtained by applying $\pmb { G }$ to the functions in the fundamental set.

When $f _ { i }$ is in $\mathcal { Q } _ { n } ,$ , then $D _ { \lambda } f _ { i }$ is also in ${ \mathcal { Q } } _ { n }$ .Hence the projection condition (17.22) and the definition (17.23) of the displacement operator imply the identity

$$
D _ { - \lambda } L D _ { \lambda } f _ { i } = D _ { - \lambda } D _ { \lambda } f _ { i } = f _ { i } , \qquad f _ { i } \in \mathcal { Q } _ { n } .
$$

It follows that $G f _ { i }$ is equal to expression (17.35).

Next we consider $\pmb { G }$ cos $\{ j . \}$ when $j > n$ . We require the equation

$$
D _ { \lambda } \cos \{ j . \} = \cos ( j \lambda ) \cos \{ j . \} - \sin ( j \lambda ) \sin \{ j . \} ,
$$

and we require the fact that $L$ cos $\{ j . \}$ and $L$ sin $\{ j . \}$ can be expressed in the form

$$
\begin{array} { r } { L \cos \left\{ j . \right\} = \underset { k = 0 } { \overset { n } { \sum } } \left[ a _ { j k } \cos \left\{ k . \right\} + b _ { j k } \sin \left\{ k . \right\} \right] } \\ { L \sin \left\{ j . \right\} = \underset { k = 0 } { \overset { n } { \sum } } \left[ \alpha _ { j k } \cos \left\{ k . \right\} + \beta _ { j k } \sin \left\{ k . \right\} \right] . } \end{array}
$$

Hence we can write $L D _ { \lambda }$ cos $\{ j . \}$ in terms of the basis functions of $\mathcal { Q } _ { n }$ .An obvious continuation of this procedure gives $D _ { - \lambda } L D _ { \lambda }$ cos $\{ j . \}$ in terms of the same basis functions,and we obtain $\pmb { G }$ cos $\{ j . \}$ by integrating this expression over $\pmb { \lambda }$ . Every term of this integral includes a factor of the form

$$
\int _ { 0 } ^ { 2 \pi } \left[ \cos \left( k \lambda \right) \mathrm { o r } \sin \left( k \lambda \right) \right] \times \left[ \cos \left( j \lambda \right) \mathrm { o r } \sin \left( j \lambda \right) \right] \mathrm { d } \lambda .
$$

Because $\pmb { k }$ is in the interval $[ 0 , n ] .$ ,and because $j$ is greater than $\pmb { n }$ ,each of these factors is zero. It follows that $G \cos \left\{ j . \right\}$ is equal to $S _ { n }$ cos $\{ j . \}$ A similar argument gives the equation

$$
G \sin \{ j . \} = S _ { n } \sin \{ j . \} , \qquad j > n ,
$$

which completes the proof that the operators $_ G$ and $S _ { n }$ are the same.

The required lower bound on $\| L \|$ is a consequence of equation (17.33), the properties of norms, and the fact that $\| D _ { \lambda } \|$ is one. By extending the triangle inequality for norms to integrals, it follows from equation (17.33) that the inequality

$$
\lVert S _ { n } \rVert { \leqslant } { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \left. { D _ { - \lambda } L D _ { \lambda } } \right. \mathbf { d } \lambda
$$

is satisfied. The integrand is bounded above by the relation

$$
\| D _ { - \lambda } L D _ { \lambda } \| \leqslant \| D _ { - \lambda } \| \| L \| \| D _ { \lambda } \| = \| L \| .
$$

Therefore $\| \pmb { S _ { n } } \|$ is a lower bound on $\| \pmb { L } \|$

This theorem gives an excellent reason for taking the point of view that $S _ { n }$ is the best of the linear projection operators from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$

# 17.4 Application to algebraic polynomials

An interesting question is to seek the linear operator $L$ from $\mathcal { C } [ \alpha , b ]$ to $\mathcal { P } _ { n }$ that satisfies the projection condition

$$
L f = f , \qquad f \in { \mathcal { P } } _ { n } ,
$$

and whose norm $\| L \| _ { \infty }$ is as small as possible. Equation (17.44) implies the bound

$$
\| L \| _ { \infty } \geqslant 1 ,
$$

which can hold as an equation when $n = 1$ . Specifically, it is shown in Section 3.1 that, if $L f$ is the function in $\mathcal { P } _ { 1 }$ that is defined by the interpolation conditions

$$
\left. \begin{array} { c } { { \left( L f \right) \left( a \right) = f \left( a \right) } } \\ { { \left( L f \right) \left( b \right) = f \left( b \right) } } \end{array} \right\} ,
$$

then $\| L \| _ { \infty }$ is equal to one. It follows that $\| R _ { n } \|$ is not a lower bound on $\| \pmb { L } \|$ The least value of $\| L \|$ for general $\pmb { n }$ is unknown,but the next theorem gives a useful condition that depends on $\| R _ { n } \|$

# Theorem 17.4

If $L$ is any bounded linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ ,that satisfies the projection condition (17.44), then the inequality

$$
\| L \| \geqslant \frac { 1 } { 2 } \| R _ { 0 } + R _ { n } \|
$$

holds.

Proof. Because the proof has much in common with the proof of Theorem 17.3, some of the details are omitted.Instead of the displacement operator $\pmb { D } _ { \pmb { \lambda } }$ ， it is helpful to employ an average of two displacements. Therefore the operator $H _ { \lambda }$ is defined by the equation

$$
\begin{array} { r } { ( H _ { \lambda } f ) ( \cos { \theta } ) = \frac { 1 } { 2 } \{ f ( \cos { [ \theta + \lambda ] } ) + f ( \cos { [ \theta - \lambda ] } ) \} , \qquad 0 \leqslant \theta \leqslant \pi . } \end{array}
$$

It should be clear that $H _ { \lambda } f$ is in $\mathcal { C } [ - 1 , 1 ]$ for every $f$ in $\mathcal { C } [ - 1 , 1 ]$ , and that, if $f$ is in $\mathcal { P } _ { n }$ ,then $H _ { \lambda } f$ is also in $\mathcal { P } _ { n }$ . We take for granted that the operator

$$
G = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } H _ { \lambda } L H _ { \lambda } \mathrm { d } \lambda
$$

is well defined. The key equation in the present proof is the identity

$$
{ \cal G } = { \cal R } _ { 0 } + { \cal R } _ { n } ,
$$

and, to establish it,we make use of the fundamental set $\{ T _ { j } ; j = 0$ ， $1 , 2 , \ldots \} ,$ where $T _ { j }$ is still the Chebyshev polynomial

$$
T _ { j } ( \cos \theta ) = \cos { ( j \theta ) } , \qquad 0 \leqslant \theta \leqslant \pi .
$$

Therefore we recall from Section 12.4 that $\scriptstyle { R _ { n } }$ gives the functions

$$
R _ { n } T _ { j } = \Big \{ { T _ { j } } , \qquad j \in n ,
$$

Moreover, it is important to note that the definition (17.48) implies the relation

$$
H _ { \lambda } T _ { j } = \cos { ( j \lambda ) } T _ { j }
$$

for each scalar $\pmb { \lambda }$ .Hence $G T _ { j }$ and $( R _ { 0 } + R _ { n } ) T _ { j }$ are the same if $j \leqslant n$ ,which depends on the projection condition (17.44). The term $\scriptstyle { R _ { 0 } }$ allows for the fact that the integral of the function $\left\{ \cos ^ { 2 } { \left( j \lambda \right) } ; 0 \leqslant \lambda \leqslant 2 \pi \right\}$ when $j = 0$ is twice the value that occurs when $j$ is a positive integer. When $j > n$ ，we may express $L H _ { \lambda } T _ { j }$ in the form

$$
L H _ { \lambda } T _ { j } = \cos { ( j \lambda ) } \sum _ { k = 0 } ^ { n } a _ { j k } T _ { k } ,
$$

where the coefficients $\{ a _ { j k } ; k = 0 , 1 , \ldots , n \}$ are independent of $\lambda$ . Therefore the equation

$$
H _ { \lambda } L H _ { \lambda } T _ { j } = \sum _ { k = 0 } ^ { n } a _ { j k } \cos { ( j \lambda ) } \cos { ( k \lambda ) } T _ { k }
$$

is satisfied. Because the integral over $\pmb { \lambda }$ of each term of the sum is zero, we find the identity

$$
\begin{array} { l } { { G T _ { j } = 0 } } \\ { { \qquad = ( R _ { 0 } + R _ { n } ) T _ { j } , \qquad j > n , } } \end{array}
$$

which completes the proof of expression (17.50).

Because $\| H _ { \lambda } ^ { \cdot } \|$ is one,equations (17.49) and (17.50) give the bound

$$
\begin{array} { l } { \displaystyle \| R _ { 0 } + R _ { n } \| \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \| { \cal H } _ { \lambda } { \cal L } { \cal H } _ { \lambda } \| \mathrm { d } \lambda } \\ { \displaystyle \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \| { \cal H } _ { \lambda } \| ^ { 2 } \| { \cal L } \| \mathrm { d } \lambda } \\ { \displaystyle = 2 \| { \cal L } \| , } \end{array}
$$

which is the required result.□

By combining this theorem with inequality (17.1),we find that $\| L \| _ { \infty }$ is bounded below by the inequality

$$
\begin{array} { r } { \| L \| _ { \infty } > ( 2 / \pi ^ { 2 } ) \ln { ( n + 1 ) } - \frac { 1 } { 2 } . } \end{array}
$$

It follows from Theorem 17.2 that the sequence $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ does not converge uniformly to $f$ for all $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ if each $X _ { n }$ is any linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ that leaves polynomials of degree $\pmb { n }$ unchanged. However，we recall from Section 6.3 that the Bernstein operators (6.23) give uniform convergence.Perhaps it would be useful to investigate algorithms for calculating polynomial approximations that have bounded norms, that are linear,and that are more accurate than the Bernstein method when $f$ can be differentiated more than once.

# 17 Exercises

17.1 Prove that the space ${ \mathcal { C } } [ a , b ]$ is complete with respect to the 8-norm.

17.2 Let $\{ \xi _ { i } ; i = 2 , 3 , 4 , . . . \}$ be an infinite sequence of numbers in the interval $[ a , b ]$ ,such that every point of $[ a , b ]$ is a limit point of the sequence. Prove that the functions $\{ \phi _ { 0 } ( x ) = 1$ ； $a \leqslant x \leqslant b $ ， $\{ \phi _ { 1 } ( x ) = x$ ； $a \leqslant x \leqslant b \}$ and $\{ \phi _ { i } ( x ) = \left| x - \xi _ { i } \right|$ ； $a \leqslant x \leqslant b$ ； $i = 2 , 3$ ， $4 , \ldots . \}$ are a fundamental set in $\mathcal { C } [ a , b ]$

17.3 Let $\mathcal { B }$ be the space $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ of periodic functions with continuous first derivatives. The Fourier series operators $\{ S _ { n } ; n = 0 , 1$ ， $2 , \ldots \} \operatorname* { m a p } \mathcal { B }$ into $\mathcal { B }$ and the sequence of norms $\smash { \{ \| S _ { n } \| _ { \infty } ; n = 0 , 1 \} }$ ， $2 , \ldots . \}$ diverges.Nevertheless,Theorem 15.1 shows that the sequence of functions $\left\{ S _ { n } f ; n = 0 , 1 , 2 , \ldots \right\}$ converges uniformly to $f$ for all $f$ in $\mathcal { B }$ .Explain why there is not a conflict with the uniform boundedness theorem 17.2.

17.4 Calculate the right-hand side of inequality (17.47) in the case when $n = 1$ . You should find,of course, that it is not greater than one.

17.5Prove that the operator $\pmb { G }$ of equation (17.49) is well defined.

17.6 For every positive integer $\pmb { n }$ ,let $\{ \xi _ { n i } ; i = 0 , 1 , \ldots , 2 n \}$ be a set of distinct points of $[ a , b ] ,$ ，arranged in ascending order,and such that $\xi _ { n 0 } = a$ and $\xi _ { n 2 n } = b$ .For any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ ,the function $X _ { n } f$ is defined to be the piecewise quadratic polynomial that is a single quadratic on each of the intervals $\{ [ \xi _ { n i } , \xi _ { n i + 2 } ]$ ； $i = 0 , 2 , \ldots ,$ $2 n - 2 \}$ ， and that interpolates the function values $\{ f ( \xi _ { n i } ) ; i = 0 \}$ $1 , \ldots , 2 n \}$ . Find necessary and sufficient conditions on the points $[ \{ \xi _ { n i } ; i = 0 , 1 , \ldots , 2 n \}$ ； $n = 1 , 2 , 3 , \ldots ]$ for the sequence $\{ X _ { n } f$ $n = 1 , 2 , 3 , \ldots \}$ to converge uniformly to $f$ for all $f$ in ${ \mathcal { C } } [ a , b ]$

17.7 Prove that the powers $\{ \phi _ { k } ( x ) = x ^ { k } ; - 1 \leqslant x \leqslant 1 ; k = 0 , 2 , 3 ,$ 4,...},excluding the linear function $\{ \phi _ { 1 } ( x ) = x ; - 1 \leqslant x \leqslant 1 \} .$ ， are a fundamental set in $\mathcal { C } [ - 1 , 1 ]$ ，but that the Chebyshev polynomials $\{ T _ { k } ; k = 0 , 2 , 3 , 4 , \ldots \}$ ，excluding the linear term, are not a fundamental set in $\mathcal { C } [ - 1 , 1 ]$

17.8 Let $\{ L _ { n } ; n = 0 , 1 , 2 , \ldots \}$ be a sequence of linear operators from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { C } [ - 1 , 1 ]$ such that, for every $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ the sequence of functions $\{ L _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$ Let $X _ { n }$ be the operator

$$
X _ { n } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } H _ { \lambda } L _ { n } H _ { \lambda } \mathrm { d } \lambda - R _ { 0 } ,
$$

where $H _ { \lambda }$ and $\scriptstyle { R _ { 0 } }$ occur in the proof of Theorem 17.4. Prove that, for every $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ , the sequence $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$ Note that $L _ { n }$ need not be a projection.

17.9 Construct a linear operator $\pmb { L }$ from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { 2 }$ ，satisfying the projection condition (17.44),whose norm $\| L \| _ { \infty }$ is as small as you can make it. By letting $L$ have the form $\scriptstyle { \frac { 1 } { 2 } } ( L _ { \lambda } + L _ { \mu } )$ ,where,for any $f$ in $\mathcal { C } [ - 1 , 1 ] , L _ { \lambda } f$ is the quadratic polynomial that interpolates the function values $\{ f ( - \lambda ) , f ( 0 ) , f ( \lambda ) \}$ ,it is possible for $\| L \| _ { \infty }$ to be less than $\textstyle { \frac { 5 } { 4 } }$

17.10 Let $\bar { \pmb { S } } [ \pmb { n } , \pmb { N } ]$ be the operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that corresponds to the discrete Fourier series method of Section 13.3.Let $L$ be any linear operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that satisfies the projection condition (17.22) and that has the property that,for any $f$ in $\mathcal { C } _ { 2 \pi } ,$ the function $L f$ depends only on the function values $\{ f ( 2 \pi j / N ) ; j = 0 , 1 , \ldots , N - 1 \}$ . Prove that, if $\begin{array} { r } { n < \frac { 1 } { 2 } N , } \end{array}$ then $\| L \| _ { \infty }$ is bounded below by $\| \bar { \pmb { S } } [ n , N ] \| _ { \infty }$

# Interpolation by piecewise polynomials

# 18.1 Local interpolation methods

We have noted several disadvantages of polynomial approximations. In Chapter 3,for example,it is pointed out that they are not well suited to the approximation of the function shown in Figure 1.1, because, if $\{ p ( x ) ; - \infty < x < \infty \}$ is a polynomial whose degree is non-zero, then $\left| p ( x ) \right|$ becomes unbounded as $| x |$ tends to infinity. It is noted also that it can be highly inefficient to use an analytic function to represent a function that is not analytic. Therefore it happens often that, in order to obtain sufficient accuracy by a polynomial approximation, it is necessary to let the degree of the polynomial be high.In this case there may not be sufficient data to determine all the coefficients properly, the effort of calculating the polynomial is increased,and the tendencies towards unboundedness are exacerbated. Really polynomials are quite inappropriate for general use as approximating functions. Because piecewise polynomials are much more successful in practice, they are studied in the next four chapters.

We use the notation $\{ s ( x ) ; a \leqslant x \leqslant b \}$ for a piecewise polynomial. In this chapter $\pmb { s }$ is defined by the interpolation equations

$$
s ( x _ { j } ) = f ( x _ { j } ) , \qquad j = 1 , 2 , \ldots , m ,
$$

where the function values $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ are given, and where the data points satisfy the conditions

$$
a = x _ { 1 } < x _ { 2 } < \ldots < x _ { m } = b .
$$

This section is concerned with interpolation methods that have the property that, for any fixed $x$ ,the function value $\pmb { s } ( \pmb { x } )$ depends on only a few of the data, whose abscissae are close to $\pmb { x }$

The most frequently used method of this type, namely piecewise linear interpolation, has been mentioned already in Section 3.4.In each of the intervals $\{ x _ { j } \leqslant x \leqslant x _ { j + 1 } ; j = 1 , 2 , \ldots , m - 1 \} , s ( x )$ is defined by the formula

$$
s \left( x \right) = f ( x _ { j } ) + \frac { x - x _ { j } } { x _ { j + 1 } - x _ { j } } \left[ f ( x _ { j + 1 } ) - f ( x _ { j } ) \right] ,
$$

which is equivalent to equation (3.29). The main advantages of the method are that $\{ s ( x ) ; a \leqslant x \leqslant b \}$ adapts itself easily to the form of $\{ f ( x )$ ； $a \leqslant x \leqslant b \}$ ,and that the error $ \| f - s \| _ { \infty }$ can be controlled directly by the spacing between data points.However, in order to achieve a prescribed accuracy,piecewise linear interpolation usually requires far more data than some higher order methods.

We consider two higher order methods that are quite useful. Both of them define $\pmb { S }$ to be a cubic polynomial, $s _ { j }$ say,on each of the intervals $\{ x _ { j } \leqslant x \leqslant x _ { j + 1 } ; \ j = 1 , 2 , \ldots , m - 1 \}$ .Therefore there are two degrees of freedom in $s _ { j }$ after equation (18.1) is satisfied. In the first method $s _ { j }$ is defined by interpolating two more function values. If $2 \leqslant j \leqslant m - 2$ ,these values are $f ( x _ { j - 1 } )$ and $f ( x _ { j + 2 } )$ ,but, if $j = 1$ or $m - 1$ , they are $f ( x _ { 3 } )$ and $f ( x _ { 4 } )$ or $f ( x _ { m - 3 } )$ and $f ( x _ { m - 2 } )$ respectively. In the other method the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ are given or are calculated at the beginning of the interpolation procedure. For example, if $3 \leqslant j \leqslant m - 2$ , we may let $\pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ be the derivative at $x _ { j }$ of the quartic polynomial that interpolates the five function values $\{ f ( x _ { k } ) ; k = j - 2 , j - 1 , j , j + 1 , j + 2 \}$ . The derivatives $\pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ and $\pmb { s } ^ { \prime } ( \pmb { x } _ { j + 1 } )$ fix the two degrees of freedom in $s _ { j }$ for each $j .$ Hence $s _ { j } ( x )$ is the cubic polynomial

$$
s _ { j } ( x ) = f ( x _ { j } ) + s ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) + c _ { 2 } ( x - x _ { j } ) ^ { 2 } + c _ { 3 } ( x - x _ { j } ) ^ { 3 } ,
$$

where the coefficients have the values

$$
c _ { 2 } = \frac { 3 [ f ( x _ { j + 1 } ) - f ( x _ { j } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } - \frac { 2 s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) } { x _ { j + 1 } - x _ { j } }
$$

and

$$
c _ { 3 } = \frac { 2 [ f ( x _ { j } ) - f ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 3 } } + \frac { s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } .
$$

It should be clear that each of the three interpolation methods that have been mentioned gives a function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that is continuous, but only the last method makes the first derivative $\{ s ^ { \prime } ( x ) ; a \leqslant x \leqslant b \}$ continuous also.

In order to compare the accuracy of the first two methods, in the case when $f$ has a continuous fourth derivative, we refer to the expression for the error of polynomial interpolation that is stated in Theorem 4.2. If $\pmb { s }$ is the cubic polynomial that interpolates the data $\{ f ( x _ { j - 1 } ) , f ( x _ { j } ) , f ( x _ { j + 1 } ) \}$ $f ( x _ { j + 2 } ) \}$ ,and if $x$ is in the interval $[ x _ { j - 1 } , x _ { j + 2 } ]$ ,then the theorem gives the bound

$$
\begin{array} { r } { \big \vert f ( x ) - s ( x ) \big \vert \leqslant \frac { 1 } { 2 4 } \displaystyle \prod _ { i = j - 1 } ^ { j + 2 } \big \vert x - x _ { i } \big \vert \operatorname* { m a x } _ { x _ { j - 1 } \leqslant \xi \leqslant x _ { j + 2 } } \big \vert f ^ { ( 4 ) } ( \xi ) \big \vert . } \end{array}
$$

This inequality suggests that doubling the number of data can improve the accuracy by a factor of sixteen, but the corresponding result for the interpolation formula (18.3) is that there is only a fourfold increase in accuracy. Therefore piecewise linear interpolation is normally less efficient. In the third method the values of the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j =$ $1 , 2 , \ldots , m \}$ can usually be chosen so that this method gives the best accuracy,which is demonstrated in Exercise 18.1.However, if $f$ is not in $\mathcal { C } ^ { ( 4 ) } [ a , b ] .$ then piecewise inear interpolationmay be preferable,especially if the spacing between data points is irregular.

Because all of these interpolation methods depend linearly on the data, each one can be expressed in the form

$$
s ( x ) = \sum _ { k = 1 } ^ { m } l _ { k } ( x ) f ( x _ { k } ) , \quad a \leqslant x \leqslant b ,
$$

where $l _ { k }$ is a ‘cardinal function’ that depends on the positions of the data points,but that is independent of the given function values.As in equation (4.4), the cardinal functions satisfy the equations

$$
l _ { k } ( x _ { j } ) = \delta _ { k j } ,
$$

in order that the interpolation conditions (18.1) hold.If the interpolation method is‘local'，then $l _ { k } ( x )$ is non-zero only if $x$ is close to $x _ { k }$ A convenient way of obtaining $l _ { k }$ is to apply the interpolation procedure to the data $\{ f ( x _ { j } ) = \delta _ { k j } ; j = 1 , 2 , \ldots , m \}$ .The results of this calculation for the three interpolation methods of this section are shown in Figure 18.1, where $k$ is remote from the ends of the interval $[ 1 , m ]$ ,and where the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ for the last method are obtained in the way that is suggested before equation (18.4).It is clear that only the last method makes $\{ \boldsymbol { s } ^ { \prime } ( \boldsymbol { x } )$ ； $a \leqslant x \leqslant b $ continuous for general data $\{ f ( x _ { j } )$ ； $j = 1 , 2 , \dots , m \}$

The figure suggests that there are many ways of choosing cardinal functions so that equation (18.8) gives a tolerable approximation to $\{ f ( x )$ ； $a \leqslant x \leqslant b $ . The ideal properties for a cardinal function are that it is non-zero over only a small part of the range $[ a , b ] .$ ,it is smooth, the form of $\pmb { S }$ is convenient for computer calculations, $\| l _ { k } \| _ { \infty }$ is not much larger than one,and, if $f$ can be differentiated many times, then the error $\| f - s \| _ { \infty }$ of the approximation (18.8） is small. A good way of achieving the last condition is to ensure that the error is zero when $f$ is a polynomial of suitable order, but the last two conditions can conflict when the spacing between data points is highly irregular.These comments assume that equation (18.9) is satisfied,but we find in Chapter 2O that it can be advantageous to work with an approximation of the form (18.8) that does not interpolate the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$

# 18.2 Cubic spline interpolation

Cubic spline functions are now used widely in computer calculations for the approximation of continuous functions of one variable. We recall from Chapter 3 that a cubic spline $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is composed of cubic polynomial pieces, that are joined so that the second derivative $\{ s ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ is continuous. In Sections 18.2 and 18.3 we consider interpolation by cubic splines to the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ ，when the cubic polynomial pieces meet at the data points. We continue to assume that condition (18.2） is satisfied. Because it is convenient to calculate the value of the spline from expression (18.4) when $x$ is in the interval $[ x _ { j } , x _ { j + 1 } ] _ { 2 }$ ，we study methods for obtaining the derivative values $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ from the data. One important difference between cubic spline interpolation and the methods that are described in the last section is that, if $\pmb { s }$ is a cubic spline, then each of the pieces of $\pmb { s }$ usually depends on all the data.

![](images/5fe051391afc26fd13a87eda269882fdd16561f7e0e778acfcd46b5c09f1f6d1.jpg)  
Figure 18.1. Cardinal functions for three local interpolation methods.

The condition that $s ^ { \prime \prime }$ is continuous at the data points $\{ x _ { k } ; ~ k = 2$ $3 , \ldots , m - 1 \}$ gives equations that have to be satisfied by the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ . In order to derive these equations,we note that expression (18.4) implies the value

$$
\begin{array} { l } { s ^ { \prime \prime } ( x _ { j + 1 } ) = 2 c _ { 2 } + 6 c _ { 3 } ( x _ { j + 1 } - x _ { j } ) \qquad } \\ { \quad = \frac { 6 \left[ f ( x _ { j } ) - f ( x _ { j + 1 } ) \right] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } + \frac { 2 s ^ { \prime } ( x _ { j } ) + 4 s ^ { \prime } ( x _ { j + 1 } ) } { \left( x _ { j + 1 } - x _ { j } \right) } , } \end{array}
$$

which, if $j \leqslant m - 2$ ,has to agree with the second derivative at $x _ { j + 1 }$ of the cubic polynomial that is equal to $\pmb { s }$ on the interval $[ x _ { j + 1 } , \ x _ { j + 2 } ]$ An expression for this polynomial can be obtained by replacing $j$ by $( j + 1 )$ in equations (18.4), (18.5) and (18.6). Hence the relation

$$
\begin{array} { l } { \displaystyle \frac { s ^ { \prime } ( x _ { k - 1 } ) + 2 s ^ { \prime } ( x _ { k } ) } { ( x _ { k } - x _ { k - 1 } ) } + \frac { 2 s ^ { \prime } ( x _ { k } ) + s ^ { \prime } ( x _ { k + 1 } ) } { ( x _ { k + 1 } - x _ { k } ) } } \\ { \displaystyle = \frac { 3 [ f ( x _ { k } ) - f ( x _ { k - 1 } ) ] } { \left( x _ { k } - x _ { k - 1 } \right) ^ { 2 } } + \frac { 3 [ f ( x _ { k + 1 } ) - f ( x _ { k } ) ] } { \left( x _ { k + 1 } - x _ { k } \right) ^ { 2 } } } \end{array}
$$

is the condition for second derivative continuity at $x _ { k }$ .Because we give special attention to the case when the spacing between data points is constant

$$
x _ { j + 1 } - x _ { j } = h , \qquad j = 1 , 2 , \ldots , m - 1 ,
$$

we note that in this case expression (18.11) simplies to the form

$$
s ^ { \prime } ( x _ { k - 1 } ) + 4 s ^ { \prime } ( x _ { k } ) + s ^ { \prime } ( x _ { k + 1 } ) = 3 [ f ( x _ { k + 1 } ) - f ( x _ { k - 1 } ) ] / h .
$$

One method, that is sometimes recommended, for fixing the two degrees of freedom that remain in the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ ， after equation (18.11） is satisfied for $k = 2 , 3 , \ldots , m - 1$ , is to use a separate preliminary procedure to calculate or to estimate $\pmb { s } ^ { \prime } ( \pmb { x } _ { 1 } )$ and $s ^ { \prime } ( x _ { m } )$ . In this case the second derivative continuity conditions give a tridiagonal system of linear equations in the unknowns $\lbrace s ^ { \prime } ( x _ { j } ) ; j =$ $2 , 3 , \ldots , m - 1 \}$ ， which can be solved easily because it is diagonally dominant. Several other methods for fixing the two degrees of freedom are mentioned in the next section.

In the remainder of this section we consider cubic spline interpolation, when there are an infinite number of uniformly spaced data points

$$
x _ { j } = j h , \qquad j = 0 , \pm 1 , \pm 2 , . . . .
$$

This case is studied because it is easy to analyse,and because the cardinal

functions of the interpolation procedure help one to understand some of the main properties of spline approximation. We may express $\pmb { s }$ in the form

$$
s ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad - \infty < x < \infty ,
$$

where each $l _ { j }$ is a cardinal spline function that satisfies the equations

$$
l _ { j } ( x _ { k } ) = \delta _ { j k } , \qquad k = 0 , \pm 1 , \pm 2 , . . . .
$$

Because the range of the variable $x$ is infinite,there is the possibility that $l _ { j }$ is unbounded,which would be unacceptable, because then the approximation (18.15） would be highly sensitive to the function value $f ( x _ { j } )$ .Fortunately it happens that the two degrees of freedom that occur in cubic spline interpolation, when the number of data points is finite,can be used in just one way to make $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ bounded when the data points have the values (18.14). The derivatives $\{ l _ { j } ^ { \prime } ( x _ { k } ) ; k = 0 , \pm 1 , \pm 2 , . . . \}$ of the bounded cardinal spline are found in the following way.

The second derivative continuity conditions that correspond to equation (18.13) have the form

$$
\begin{array} { r l r } {  { l _ { j } ^ { \prime } ( x _ { k - 1 } ) + 4 l _ { j } ^ { \prime } ( x _ { k } ) + l _ { j } ^ { \prime } ( x _ { k + 1 } ) } } \\ & { } & { = 3 [ \delta _ { j k + 1 } - \delta _ { j k - 1 } ] / h , \qquad k = 0 , \pm 1 , \pm 2 , \ldots . } \end{array}
$$

It is important to note that the right-hand side is zero if $k \geqslant j + 2$ It follows from the theory of recurrence relations that the conditions

$$
l _ { j } ^ { \prime } ( x _ { k } ) = \alpha ( - 2 + \sqrt { 3 } ) ^ { k - j } + \beta ( - 2 - \sqrt { 3 } ) ^ { k - j } , \qquad k \geqslant j + 1 ,
$$

hold, where $_ \alpha$ and $\beta$ are constants, and where $( - 2 \pm { \sqrt { 3 } } )$ are the roots of the quadratic equation

$$
1 + 4 \theta + \theta ^ { 2 } = 0 .
$$

In order that $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ is bounded, the value of $\beta$ must be zero. Similarly, because the right-hand side of expression (18.17) is zero for $k \leqslant j - 2$ ,the conditions

$$
l _ { j } ^ { \prime } ( x _ { k } ) = \gamma ( - 2 + \sqrt { 3 } ) ^ { j - k } , \qquad k \leqslant j - 1 ,
$$

must hold also, where $\gamma$ is another constant. The numbers $\alpha , \gamma$ and $l _ { j } ^ { \prime } ( x _ { j } )$ are determined uniquely by giving $k$ the values $j - 1 , ~ j$ and $j + 1$ in equation (18.17). Hence the bounded cardinal spline $l _ { j }$ has the derivatives

$$
\begin{array} { r } { l _ { j } ^ { \prime } ( x _ { k } ) = \left\{ \begin{array} { c c } { - 3 ( - 2 + \sqrt { 3 } ) ^ { j - k } / h , } & { \quad k < j } \\ { 0 , } & { \quad k = j } \\ { 3 ( - 2 + \sqrt { 3 } ) ^ { k - j } / h , } & { \quad k > j . } \end{array} \right. } \end{array}
$$

This cardinal function is shown in Figure 18.2. It is an oscillatory function that decays exponentially by the factor $( { \sqrt { 3 - 2 } } )$ per data point as $x$ moves away from $x _ { j } .$ It follows from equation (18.15) that, if $x$ is not a data point, then $s ( x )$ depends on all the function values $\{ f ( x _ { j } ) ; j = 0 , \pm 1 \}$ $\pm 2 , \ldots . \}$ ，but the contribution from $f ( x _ { j } )$ to $\pmb { s } ( \pmb { x } )$ is usually negligible when ${ \left| x - x _ { j } \right| } / h$ is large.

It is easy to calculate the $\infty$ -norm of the interpolation algorithm (18.15) when expression (18.21) gives the derivatives of the cardinal functions. Because each interval between data points is similar, the norm has the value

$$
\begin{array} { r l } { \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \operatorname* { m a x } _ { \| f \| _ { \infty } \leq 1 } \ \Big | _ { j = - \infty } l _ { j } ( x ) f ( x _ { j } ) \Big | } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \sum _ { j = - \infty } ^ { \infty } | l _ { j } ( x ) | } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \sum _ { j = 0 } ^ { \infty } \ ( - 1 ) ^ { i } [ l _ { - j } ( x ) + l _ { j + 1 } ( x ) ] } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } p ( x ) , } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } p ( x ) , } \end{array}
$$

say, where the third line of this equation depends on the sign properties of the cardinalfunction that are shown in Figure 18.2.The function $\{ p ( { \pmb x } )$ ； $0 \leqslant x \leqslant h \}$ is a cubic polynomial that is defined by the equations

$$
p ( 0 ) = p ( h ) = 1
$$

and

$$
\begin{array} { r } { p ^ { \prime } ( 0 ) = - p ^ { \prime } ( h ) = \underset { k = - \infty } { \overset { \infty } { \sum } } \left| l _ { j } ^ { \prime } ( x _ { k } ) \right| } \\ { = 3 ( \sqrt { 3 } - 1 ) / h . } \end{array}
$$

Hence the $\infty$ -norm has the value $p ( \frac { 1 } { 2 } h ) = ( 1 + 3 \surd 3 ) / 4 \approx 1 . 5 5$ ，which is remarkably small. Therefore cubic spline interpolation to equally spaced

![](images/0fa59eac8d7112b6387a665724b8aa21310c03173cc38c539aacfd7b8dc11989.jpg)  
Figure 18.2.A cubic spline cardinal function.

data on the whole real line is a reliable procedure.It is analysed further in Section 22.4.

# 18.3 End conditions for cubic spline interpolation

It has been noted that, if $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is a cubic spline that has knots at the points $\{ x _ { j } ; j = 2 , 3 , \ldots , m - 1 \}$ , and that satisfes the interpolation conditions (18.1), then there are two degrees of freedom in s.A change in the method that fixes this freedom alters $\pmb { s }$ by a spline, $\sigma$ say, that is zero at all the interpolation points. Therefore,if the data points are equally spaced, then equation (18.13) implies the conditions

$$
\sigma ^ { \prime } ( x _ { k - 1 } ) + 4 \sigma ^ { \prime } ( x _ { k } ) + \sigma ^ { \prime } ( x _ { k + 1 } ) = 0 , \qquad k = 2 , 3 , \ldots , m - 1 .
$$

It follows that, if $\bar { s }$ is any particular cubic spline that interpolates the data, then the general interpolating spline has the derivative values

$$
\begin{array} { c } { { s ^ { \prime } ( x _ { j } ) = \bar { s } ^ { \prime } ( x _ { j } ) + \alpha ( - 2 + \sqrt { 3 } ) ^ { j - 1 } + \beta ( - 2 + \sqrt { 3 } ) ^ { m - j } , } } \\ { { j = 1 , 2 , \ldots , m , } } \end{array}
$$

where $\pmb { \alpha }$ and $\beta$ are constants. This section considers procedures that define the values of $\pmb { \alpha }$ and $\beta$

Expression (18.26) shows that the influence of $_ \alpha$ is strongest at the left-hand end of the range $[ a , b ] ,$ ，while the influence of $\beta$ is strongest at the right-hand end. Therefore, in order that $\pmb { s }$ depends stably on the procedure that fixes $_ { \pmb { \alpha } }$ and $\beta$ ,it is necessary to impose a condition on $\pmb { s }$ at each end of the range. Normally this remark is also true in the general case when the distribution of data points is irregular. Therefore, obtaining the values of $\pmb { s } ^ { \prime } ( \pmb { a } )$ and $s ^ { \prime } ( b )$ from a preliminary calculation,which is suggested in the last section, is a suitable method for determining the free parameters of $\pmb { s }$

A different procedure that is used sometimes is to set $s ^ { \prime \prime } ( a ) = s ^ { \prime \prime } ( b ) = 0$ ， which makes s a ‘natural spline'. Natural splines have some interesting theoretical properties that are studied in Chapter 23,but in practice they are often poor approximating functions, because they waste the accuracy that can be achieved when $f$ is in $\mathcal { C } ^ { ( 4 ) } [ a , b ]$ .When $f ^ { \prime \prime } ( a )$ and $f ^ { \prime \prime } ( b )$ are both non-zero, the error $\| f - s \| _ { \infty }$ of a natural spline approximation is bounded below by a multiple of max ${ \left[ { \left( { { x } _ { 2 } } - { x } _ { 1 } \right) ^ { 2 } } \right. }$ ， $\left( x _ { m } - x _ { m - 1 } \right) ^ { 2 } ] ,$ instead of being of fourth order in the spacing between the data points. It is better to choose two suitable properties that would be obtained by a good spline approximation when $f$ is a polynomial of degree at least three,and to force $\pmb { s }$ to have these properties.

For example, if $f$ is a cubic polynomial, then $\pmb { s }$ is equal to $f$ only if $\pmb { s } ^ { \prime \prime \prime }$ is continuous throughout $[ a , b ]$ . Therefore the property that $\pmb { s }$ can equal a general cubic polynomial is preserved if $_ { \alpha }$ and $\beta$ ,in equation (18.26),are defined by requiring any two of the third derivative discontinuities

$$
d _ { j } = s ^ { \prime \prime \prime } ( x _ { j } + ) - s ^ { \prime \prime } ( x _ { j } - ) , \qquad j = 2 , 3 , \ldots , m - 1 ,
$$

to be zero. Equations (18.4) and (18.6) show that $d _ { j }$ has the value

$$
d _ { j } = \frac { 1 2 [ f ( x _ { j } ) - f ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 3 } } + \frac { 6 [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } }
$$

$$
- \frac { 1 2 [ f ( x _ { j - 1 } ) - f ( x _ { j } ) ] } { \left( x _ { j } - x _ { j - 1 } \right) ^ { 3 } } - \frac { 6 [ s ^ { \prime } ( x _ { j - 1 } ) + s ^ { \prime } ( x _ { j } ) ] } { \left( x _ { j } - x _ { j - 1 } \right) ^ { 2 } } .
$$

A good method for determining $\pmb { s }$ is to set $d _ { 2 } = d _ { m - 1 } = 0$ ,in addition to satisfying condition (18.11) for $k = 2 , 3 , \ldots , m - 1$ .Hence the required derivatives $\{ \pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ $; j = 1 , 2 , \ldots , m \}$ are defined by a square system of linear equations,that is easy to solve, because it is almost tridiagonal and almost diagonally dominant. Another technique for fixing the values of the parameters $_ { \alpha }$ and $\beta$ is to set $d _ { 2 } = d _ { 3 }$ and $d _ { m - 2 } = d _ { m - 1 } ,$ . It has the strong advantage that it minimizes the error $ \| f - s \| _ { \infty }$ when the spacing between data points is uniform and $f$ is any quartic polynomial.

Two important and related questions,which we consider in the case when the data points have the constant spacing (18.12),are the effect that the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ have on the parameters $_ { \alpha }$ and $\beta$ ,and the effect that $_ { \pmb { \alpha } }$ and $\beta$ have on the spline $\{ s ( x ) ; a \leqslant x \leqslant b \}$ In order that the values of $_ { \alpha }$ and $\beta$ are unambiguous,it is necessary to choose a particular function $\tilde { s }$ in equation (18.26). Because of the nice properties that are obtained by the interpolating spline (18.15) when the cardinal functions have the form shown in Figure 18.2,we define $\bar { s }$ in the following way. We continue the uniform spacing of data points along the whole real line,and we assign fixed values to $f ( x _ { j } )$ at the new data points. For instance,these function values may be set to zero,if it is not important to preserve continuity in the extension of $f .$ We let $\bar { s }$ be the part of the function (18.15) that is relevant to the range $[ a , b ]$

The two conditions on $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that fix the parameters $\pmb { \alpha }$ and $\beta$ give these parameters non-zero values only if the required conditions on $\pmb { s }$ are not obtained by s. The equation

$$
{ \bar { s } } ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad a \leqslant x \leqslant b ,
$$

shows directly the contribution from $f ( x _ { j } )$ to $\bar { s } ( \boldsymbol { x } )$ ，and we note the presence of the scaling factor $l _ { j } ( x )$ . Therefore,in the usual case when $\pmb { \alpha }$ and $\beta$ depend on the form of $\bar { s }$ near the ends of the range $[ a , b ] ,$ , it follows from Figure 18.2 and equation (18.21),that the contribution from $f ( x _ { j } )$ to $\pmb { \alpha }$ or $\beta$ includes the factor $( 2 - { \sqrt { 3 } } ) ^ { j }$ or $( 2 - \sqrt { 3 } ) ^ { m - j }$ .Hence the values of $\pmb { \alpha }$ and $\beta$ depend mainly on the data that are near the ends of the interval $[ a , b ]$ . Moreover,equation (18.26) shows that the effect of the end conditions on $s ( x )$ decays exponentially if $x$ is moved towards the centre of the range $[ a , b ]$

These remarks suggest that, when $x$ is well inside the interval $[ a , b ] ,$ then it is usually adequate to regard $s ( x )$ as the value of a cubic spline that interpolates $f$ on the infinite range $- \infty < x < \infty$ . Thus one can obtain useful error estimates,and one can study the behaviour of the error as $h$ tends to zero,in a way that avoids the complications that come from the choice of end conditions.

# 18.4 Interpolating splines of other degrees

In most of this section we consider interpolation by quadratic splines.It is possible to satisfy the conditions (18.1） by letting $\pmb { s }$ be a quadratic polynomial on each of the intervals $\{ [ x _ { j } , x _ { j + 1 } ]$ ； $j = 1 , 2 , \dots ,$ $m - 1 \}$ ，where the joins of the quadratic pieces are such that the frst derivative $\{ s ^ { \prime } ( x ) ; a \leqslant x \leqslant b \}$ is continuous. This procedure, however, has some severe disadvantages. In particular, the following example shows that there are difficulties in adapting the distribution of data points to the form of $f .$

We let $f$ be the continuous function

$$
f ( x ) = \left\{ { \begin{array} { l l } { 0 , \qquad - 1 \leqslant x \leqslant 0 } \\ { x , \qquad 0 \leqslant x \leqslant 1 . } \end{array} } \right.
$$

We suppose that the number of data points $^ m$ is given,and that we are free to choose the positions of the data points, subject to the conditions

$$
- 1 = x _ { 1 } < x _ { 2 } < \ldots < x _ { m } = 1 ,
$$

and subject to the restriction that one of the data points, $x _ { n }$ say, is at zero. If $\pmb { s }$ is to be a quadratic spline that satisfies the conditions of the previous paragraph, we find that, because $x _ { n }$ is zero,it is not possible to make the error $\| f - s \| _ { \infty }$ very small by clustering the data points near the first derivative discontinuity of $f ,$ even though $f$ is equal to a single segment of a quadratic spline on each side of the discontinuity. In order to reach this conclusion we note that, because $\pmb { s }$ is a quadratic function on each of the intervals $\{ [ x _ { j } , x _ { j + 1 } ] ; j = 1 , 2 , \dots , m - 1 \}$ , the equations

$$
\begin{array} { r } { \frac { 1 } { 2 } [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] = [ s ( x _ { j + 1 } ) - s ( x _ { j } ) ] / ( x _ { j + 1 } - x _ { j } ) , \qquad } \\ { j = 1 , 2 , \ldots , m - 1 , } \end{array}
$$

are satisfied. Thus expressions (18.1) and (18.30) give the conditions

$$
\begin{array} { r } { \frac 1 2 [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] = \left\{ \begin{array} { l l } { 0 , } & { \quad j < n } \\ { 1 , } & { \quad j \geq n , } \end{array} \right. } \end{array}
$$

which imply the identities

$$
s ^ { \prime } ( x _ { j + 2 } ) = s ^ { \prime } ( x _ { j } ) , \qquad j \neq n - 1 .
$$

In particular, the derivatives $\{ s ^ { \prime } ( x _ { n } ) , s ^ { \prime } ( x _ { n \pm 2 } ) , s ^ { \prime } ( x _ { n \pm 4 } ) , . . . \}$ are all equal. It follows that $\pmb { S }$ cannot adapt itself efficiently to the slopes of both of the straight line sections of $f .$ The difficulty is due to the fact that the cardinal functions of quadratic spline interpolation do not usually become small when $x$ is remote from the data point at which the cardinal function is equal to one. For example, Figure 18.3 shows a symmetric cardinal function, where the distribution of data points is uniform.

However, there is a way of making quadratic spline interpolation a flexible procedure.It is to position the knots of $\pmb { s }$ midway between the data points.We study this technique in the case when the range of $\boldsymbol { x }$ is the whole real line,and when the data points have the equally spaced values $\{ x _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , . . . \} .$ As in Section 3.4, the notation

$$
\xi _ { j } = \textstyle { \frac { 1 } { 2 } } ( x _ { j } + x _ { j + 1 } ) , \qquad j = 0 , \pm 1 , \pm 2 , . . . ,
$$

is used for the knots of the spline.Because $s ( x _ { j } )$ is equal to $f ( x _ { j } )$ ,and because $x _ { j }$ is the mid-point of the interval $[ \xi _ { j - 1 } , \xi _ { j } ] _ { : }$ ,the quadratic function $\{ s _ { j } ( x ) = s ( x ) ; \xi _ { j - 1 } \leqslant x \leqslant \xi _ { j } \}$ is the expression

$$
\begin{array} { l } { { s _ { j } ( x ) = f ( x _ { j } ) + ( x - x _ { j } ) [ s ( \xi _ { j } ) - s ( \xi _ { j - 1 } ) ] / h } } \\ { { \qquad + 2 ( x - x _ { j } ) ^ { 2 } [ s ( \xi _ { j } ) - 2 f ( x _ { j } ) + s ( \xi _ { j - 1 } ) ] / h ^ { 2 } . } } \end{array}
$$

Therefore,in order to define $\{ s ( x ) ; \ - \infty < x < \infty \}$ ，it is convenient to calculate the function values $\{ s ( \xi _ { j } ) ; j = 0 , \pm 1 , \pm 2 , . . . \}$ . The first deriva-

![](images/895015c4c4e8e6131f7f395b556056e720fc43f4518cdc8ff272f186818b2abc.jpg)  
Figure 18.3.A quadratic cardinal function whose knots are at the data points.

tive continuity condition $s _ { j } ^ { \prime } ( \pmb { \xi } _ { j } ) = s _ { j + 1 } ^ { \prime } \left( \pmb { \xi } _ { j } \right)$ and equation (18.36) imply that the recurrence relations

$$
\begin{array} { c } { { s ( \xi _ { k - 1 } ) + 6 s ( \xi _ { k } ) + s ( \xi _ { k + 1 } ) = 4 [ f ( x _ { k } ) + f ( x _ { k + 1 } ) ] , } } \\ { { { } } } \\ { { k = 0 , \pm 1 , \pm 2 , . . . , } } \end{array}
$$

are obtained. Therefore the cardinal function $l _ { j } ,$ that satisfies equation (18.16) at the interpolation points,also satisfies the conditions

$$
\begin{array} { c } { { l _ { j } ( \xi _ { k - 1 } ) + 6 l _ { j } ( \xi _ { k } ) + l _ { j } ( \xi _ { k + 1 } ) = 4 [ \delta _ { j k } + \delta _ { j k + 1 } ] , } } \\ { { { } } } \\ { { k = 0 , \pm 1 , \pm 2 , . . . . . } } \end{array}
$$

As in Section 18.2 there is only one bounded solution to this system, which is that the cardinal function takes the values

$$
l _ { j } ( \pmb { \xi } _ { k } ) = \Big \{ \begin{array} { l l } { ( 2 - \sqrt { 2 } ) ( 2 \sqrt { 2 } - 3 ) ^ { j - 1 - k } , \qquad k \leqslant j - 1 } \\ { ( 2 - \sqrt { 2 } ) ( 2 \sqrt { 2 } - 3 ) ^ { k - j } , \qquad k \geqslant j , } \end{array}
$$

at the knots. Hence $l _ { j }$ has the form that is shown in Figure 18.4. The localization properties are even better than those of the cardinal function of Figure 18.2, because the exponential decay factor $| 2 { \sqrt { 2 - 3 } } |$ is less than $| { \sqrt { 3 - 2 } } |$ . Therefore quadratic spline interpolation is a very useful procedure, if the knots are placed between the data points.

When there are a finite number of data points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ ,and when $\pmb { s }$ is an interpolating quadratic spline, then the knot positions

$$
\xi _ { j } = \textstyle { \frac { 1 } { 2 } } ( x _ { j } + x _ { j + 1 } ) , \qquad j = 2 , 3 , \ldots , m - 2 ,
$$

are usually suitable. Because there are no knots in the intervals $[ x _ { 1 } , x _ { 2 } ]$ and $[ x _ { m - 1 } , x _ { m } ] ,$ ， the number of parameters of the spline is equal to the number of data. The Schoenberg-Whitney theorem,which is proved in Section 19.5, shows that the interpolation conditions (18.1) determine the parameters uniquely. Hence the knots (18.40) take up the degrees of freedom in the quadratic spline that correspond to the end conditions that are discussed in Section 18.3.This approximation method is usually successful in practice.

![](images/23ef7f6df6162b5db8ebee92731f12362d9672a0f042de4c006fafaffa309298.jpg)  
Figure 18.4. A quadratic cardinal function whose knots are midway between the data points.

Interpolation by splines of degree greater than three is rare. One of the main reasons is that increasing the degree of a spline normally makes the localization properties less good, because the tails of the cardinal functions decay at a slower exponential rate.Another reason is that there are many computer programs available for interpolation by cubic splines. However,splines of greater degree can be very useful when high accuracy is required. The work of the next chapter is sufficiently general to provide a suitable method of calculation.

# 18 Exercises

18.1 Let the data points of the interpolation procedures of Section 18.1 have the equally spaced values $\{ x _ { j } = j h ; j = 1 , 2 , \ldots , m \}$ Calculate the values of the cardinal functions of Figure 18.1 at the points that are midway between the interpolation points. Hence, for each of the three interpolation procedures, identify the coefficients $\{ c _ { k j } ; j = 1 , 2 , \dots , m \}$ of the equation

$$
s ( x _ { k } + { \textstyle \frac 1 2 } h ) = \sum _ { j = 1 } ^ { m } c _ { k j } f ( x _ { j } ) ,
$$

where $\pmb { s }$ is the interpolating function,and where $k$ is remote from the ends of the interval $[ 1 , m ]$ . Thus compare the accuracy of the three interpolation methods when $f$ is a quartic polynomial.

18.2 Show that both of the piecewise cubic interpolation procedures of Section 18.1 have the property that, depending on the distribution of the data points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ ,the $\infty$ -norm of the interpolation operator can be arbitrarily large.

18.3 Let the data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ be equally spaced, let $f$ be a quartic polynomial, and let $\pmb { s }$ be the cubic spline,whose knots are at the data points, that satisfies the interpolation equations (18.1) and the end conditions $d _ { 2 } = d _ { 3 }$ and $d _ { m - 2 } = d _ { m - 1 }$ ， where $d _ { j }$ is the third derivative discontinuity (18.27). Prove that the equations $\{ s ^ { \prime } ( x _ { j } ) = f ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , . . . , m \}$ are obtained, and that the third derivative discontinuities of $\pmb { s }$ have the constant values

$$
d _ { j } = h f ^ { ( 4 ) } ( x _ { j } ) , \qquad j = 2 , 3 , \ldots , m - 1 ,
$$

where $h$ is the spacing between data points.

18.4 Let $\pmb { s }$ be a cubic spline that satisfies the interpolation conditions (18.1), where the knots of $s$ are at the data points,and where the data points are equally spaced. If the function values $f ( \frac { 1 } { 2 } { \ [ x _ { 1 } + }$ $x _ { 2 } ] ) = f ( x _ { 1 { \frac { 1 } { 2 } } } )$ and $f ( { \frac { 1 } { 2 } } [ x _ { 2 } + x _ { 3 } ] ) = f ( x _ { 2 { \frac { 1 } { 2 } } } )$ are known, then two useful methods for fixing one of the degrees of freedom in $\pmb { s }$ are as follows.In one method $\pmb { s } ^ { \prime } ( \pmb { x } _ { 2 } )$ is made equal to the first derivative at $x _ { 2 }$ of the polynomial in ${ \mathcal { P } } _ { 4 }$ that interpolates the function values $\{ f ( x _ { j } ) ; j = 1 , 1 _ { 2 } ^ { \scriptscriptstyle 1 } , 2 , 2 _ { 2 } ^ { \scriptscriptstyle 1 } , 3 \} .$ ，and in the other method the equation

$$
f ( x _ { 2 _ { 2 } ^ { 1 } } ) - s ( x _ { 2 _ { 2 } ^ { 1 } } ) = f ( x _ { 1 _ { 2 } ^ { 1 } } ) - s ( x _ { 1 _ { 2 } ^ { 1 } } )
$$

is satisfied. Prove that these methods are equivalent.

18.5 For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $X f$ be the quadratic spline that has knots at the points $\{ \xi _ { j } = ( j + \textstyle { \frac { 1 } { 2 } } ) h ; j = 0$ ，±1，±2,...},and that interpolates the function values $\{ f ( j h ) ; ~ j = 0 , ~ \pm 1 , ~ \pm 2 , . ~ . . \} .$ where $h$ is a positive constant. Prove that the $\infty$ -norm of $X$ has the value $\| X \| _ { \infty } = { \sqrt { 2 } }$

18.6 For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { s }$ be a cubic spline that is defined by equation (18.15),where the data points have the values (18.14), and where each function $\{ l _ { j } ( x ) ; ~ - \infty < x < \infty \}$ satisfies the cardinality conditions (18.16). Show that, if $\pmb { s }$ is allowed to have knots not only at the data points $\{ j h ; j = 0 , \pm 1 , \pm 2 , . . . \}$ but also at the mid-points $\{ ( j + \textstyle { \frac { 1 } { 2 } } ) h ; j = 0 , \pm 1 , \pm 2 , . . . \} .$ ,then it is possible for each $l _ { j }$ to be non-zero only on the interval $( x _ { j } - 3 h , x _ { j } + 3 h )$ ， and for $\pmb { S }$ to be equal to $f$ when $f$ is any cubic polynomial.

18.7 Let $\{ s ( x ) ; 0 \leqslant x < \infty \}$ be a non-zero cubic spline function that has knots at the points $\{ x _ { j } = \mu ^ { j } ; j = 0 , 1 , 2 , . . . \}$ ,and that is zero at every knot, where $\pmb { \mu }$ is a constant that is not less than one.Prove that it is possible for the derivatives $\{ | s ^ { \prime } ( x _ { j } ) | ; j = 0 , 1 , 2 , . . . \}$ to be bounded for any value of $\pmb { \mu }$ ,but that it is possible for $\pmb { s }$ to be bounded only if $\mu \leqslant \frac { 1 } { 2 } ( 3 + \sqrt { 5 } )$

18.8 For any bounded function $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { S }$ be the spline function (18.15),where each cardinal function has the form that is shown in Figure 18.2,and where the spacing between data points, $h$ ,that is given in equation (18.14),is a parameter.Prove that,as $h$ tends to zero, $\pmb { s }$ converges uniformly to $f .$

18.9 Let $f$ be a cubic polynomial, and let s be the quadratic spline with knots at the points (18.40) that interpolates the function values $\{ f ( x _ { j } ) ; \ j = 1 , 2 , \ldots , m \}$ ，where the spacing between the data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ is constant. Sketch the form of the error function $\{ f ( { \pmb x } ) - { \pmb s } ( { \pmb x } )$ ； $x _ { 1 } \leqslant x \leqslant x _ { m } \}$ .Propose an algorithm for quadratic spline interpolation that does not cause an increase in the error function near the ends of the range $[ x _ { 1 } , x _ { m } ]$ when $f$ is a cubic polynomial.

18.10 Given two sets of data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ and $\{ y _ { k } ; k =$ $1 , 2 , \ldots , n \}$ that satisfy conditions (18.2） and the inequalities $a = y _ { 1 } < y _ { 2 } < . ~ . ~ . < y _ { n } = b$ ,an algorithm is chosen for cubic spline interpolation on each set of points.Let the cardinal functions of the algorithms be $\{ l _ { j } ( x ) ; a \leqslant x \leqslant b ; j = 1 , 2 , . . . m \}$ and $\{ \lambda _ { k } ( y )$ ； $a \leqslant y \leqslant b ; k = 1 , 2 , \ldots , n \Bigr \}$ . For any function $\{ f ( x , y )$ ； $a \leqslant x \leqslant b$ ； $a \leqslant y \leqslant b \}$ of two variables, the approximation

$$
s ( x , y ) = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { n } l _ { j } ( x ) \lambda _ { k } ( y ) f ( x _ { j } , y _ { k } ) , \qquad a \leqslant x \leqslant b , \qquad a \leqslant y \leqslant b ,
$$

is called a ‘bicubic spline’ approximation to $f .$ Investigate its properties, giving particular attention to the accuracy of the method when $f$ is differentiable,and to procedures for calculating the value of $\pmb { s } ( \pmb { x } , \pmb { y } )$ for any $x$ and $y$ directly from the data $\{ f ( x _ { j } , y _ { k } ) ; j = 1 , 2 , . . . m ; k = 1 , 2 , . . . , n \}$

#

# B-splines

# 19.1 The parameters of a spline function

Most of the results of this chapter and of Chapter 2O apply to general spline functions, that are not necessarily defined by interpolation conditions. As in Section 3.4,we let $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ be the linear space of splines of degree $k$ ,whose knots are $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ .The range of the variable is still the interval $[ a , b ] ,$ ,and it is assumed that the conditions

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b
$$

are satisfied. Sometimes the name of the space is shortened to $\mathcal { S }$ Equation (3.31) states that each function in this space can be expressed in the form

$$
s ( x ) = \sum _ { j = 0 } ^ { k } c _ { j } x ^ { j } + \frac { 1 } { k ! } \sum _ { j = 1 } ^ { n - 1 } d _ { j } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where $\{ c _ { j } ; j = 0 , 1 , \ldots , k \} \quad { \mathrm { a n d } } \quad \{ d _ { j } ; j = 1 , 2 , \ldots , n - 1 \}$ arereal parameters. Therefore the dimension of the space is $( k + n )$ . The main purpose of this chapter is to describe a general method for defining an element of $\mathcal { S }$ that is highly convenient for computer calculations.

First an example is given to show that it can be quite unsuitable to specify a spline by the values of the coefficients $\{ c _ { j } ; j = 0 , 1 , \ldots , k \}$ and $\{ d _ { j } ; j = 1 , 2 , \dots , n - 1 \}$ . We let $\pmb { s }$ be the piecewise cubic polynomial, whose knots are the integers $\{ \xi _ { j } = j ; j = 0 , 1 , \ldots , n \}$ ,that is defined by the equations

$$
\left. \begin{array} { l } { { s ( \xi _ { j } ) = 0 } } \\ { { s ^ { \prime } ( \xi _ { j } ) = ( \sqrt { 3 - 2 } ) ^ { j } } } \end{array} \right\} , \qquad j = 0 , 1 , \ldots , n .
$$

It is a cubic spline because it is a multiple of the tail of the cardinal

function that is given in Figure 18.2.Therefore,there is an expression for $\pmb { s }$ of the form (19.2),which is the function

$$
s ( x ) = x - \sqrt { 3 x ^ { 2 } + ( \sqrt { 3 } - 1 ) x ^ { 3 } + 2 \sqrt { 3 \sum _ { j = 1 } ^ { n - 1 } ( \sqrt { 3 - 2 } ) ^ { j } ( x - j ) _ { + } ^ { 3 } } } ,
$$

If we calculate $s ( 1 0 . 5 )$ , for example, from this equation, then the third term contributes the number $( \sqrt { 3 - 1 } ) ( 1 0 . 5 ) ^ { 3 } \approx 8 4 7$ ，but, because $s ( x )$ decreases exponentially as $x$ is increased by whole integers, the actual value of $s ( 1 0 . 5 )$ is $( \sqrt { 3 } - 2 ) ^ { 1 0 } s ( 0 . 5 ) \approx 3 . 0 2 \times { 1 0 } ^ { - 7 }$ . Hence nine decimal digits are lost in cancellation if expression (19.4) is evaluated. Excellent accuracy can be obtained, however, from the data (19.3). Therefore it is better to work with the function and derivative values $\{ s ( \pmb { \xi } _ { j } ) ; j = 0 \}$ ， $1 , \ldots , n \}$ and $\{ s ^ { \prime } ( \xi _ { j } ) ; j = 0 , 1 , \ldots , n \}$ ， instead of with the coefficients $\{ c _ { j } ; j = 0 , 1 , \ldots , k \}$ and $\{ d _ { j } ; j = 1 , 2 , \dots , n - 1 \}$ ·

There are disadvantages,however, in defining $\pmb { s }$ by function and derivative values when $\dot { \kappa } = 3$ . In particular， the second derivative continuity conditions are artificial, and, if $_ n$ is large,then the number of parameters that specify an element of $\mathcal { S }$ is almost twice the dimension of ${ \mathcal { S } } .$ Therefore, except in a few special cases such as interpolation to $f$ at the knots of $\pmb { S }$ , there are more unknowns than necessary in the calculation of a particular cubic spline from data, which can increase greatly the length of the calculation. Further, for larger values of $k$ , it would be necessary to take account of higher derivatives, for instance $\{ s ^ { \prime \prime } ( \xi _ { j } ) ; j = 0 , 1 , \ldots , n \}$ ， which would make the disadvantages worse.

In order that the number of parameters of $\pmb { s }$ is the same as the dimen-sion of $\mathcal { S } ,$ , we may choose any fixed basis of $\mathcal { S } , \{ \phi _ { j } ; j = 1 , 2 , \dotsc , k + n \} \mathtt { s a } _ { \mathrm { { + } } }$ y， and we express $\pmb { S }$ in the form

$$
s ( x ) = \sum _ { j = 1 } ^ { k + n } \lambda _ { j } \phi _ { j } ( x ) , \qquad a \leqslant x \leqslant b .
$$

The coefficients $\left\{ \lambda _ { j } ; j = 1 , 2 , \ldots , k + n \right\}$ are the parameters that characterize ${ \pmb S } .$ .The example (19.4） shows that the basis functions $\{ \phi _ { j } ( x ) =$ $( x - \xi _ { j } ) _ { + } ^ { k }$ ， $a \leqslant x \leqslant b ; j = 1 , 2 , \ldots , n - 1 \}$ and $\{ \phi _ { j } ( { \pmb x } ) = { \pmb x } ^ { j - n }$ ， $a \leqslant x \leqslant b ; j =$ $n , n + 1 , \ldots , n + k \}$ can give severe difficulties in practice, but many other choices of basis can be made. We find that a basis of $^ { \bullet } B$ -splines’ is particularly suitable, not only because it prevents severe loss of accuracy due to cancellation, but also because it reduces the amount of calculation, and it helps the convergence analysis of Chapter 20.

# 19.2 The form of $\pmb { B }$ -splines

One way of introducing $\pmb { B }$ -splines is to address the question of choosing the basis functions $\{ \phi _ { j } ; j = 1 , 2 , \ldots , k + n \}$ in expression (19.5), so that each function $\{ \phi _ { j } ( \pmb { x } )$ ； $a \leqslant x \leqslant b \}$ is identically zero over a large part of the range $a \leqslant x \leqslant b$ .Therefore we consider the problem of finding an element of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is zero on the intervals $[ \xi _ { 0 } , \xi _ { p } ]$ and $[ \xi _ { q } , \xi _ { n } ]$ ,but that is non-zero on $( \xi _ { p } , \xi _ { q } \cdot )$ , where $0 < p < q < n$ f $\pmb { s }$ is such a function it can be expressed in the form

$$
s ( x ) = \sum _ { j = p } ^ { q } d _ { j } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where the parameters $d _ { j }$ have to satisfy the condition

$$
\sum _ { j = p } ^ { q } d _ { j } ( x - \xi _ { j } ) ^ { k } = 0 , \qquad \xi _ { q } \leqslant x \leqslant b .
$$

It follows that the equations

$$
\sum _ { j = p } ^ { q } d _ { j } \xi _ { j } ^ { i } = 0 , \qquad i = 0 , 1 , \dots , k ,
$$

must hold. These equations have a non-zero solution if $q \geq p + k + 1$ ， because then the number of coefficients $\{ d _ { j } \}$ is greater than the number of equations. The identity (4.11） shows that， if $q = p + k + 1$ ，then the coefficients

$$
d _ { j } = \prod _ { \stackrel { i = p } { i \neq j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } , \qquad j = p , p + 1 , \ldots , p + k + 1 ,
$$

are suitable. We note that the sign of expression (19.9) is such that $d _ { p }$ is positive. The spline function

$$
B _ { p } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \prod _ { \stackrel { i = p } { i \neq j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } { \Big ] } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad - \infty < x < \infty ,
$$

is called a $^ { \ell } B \cdot$ spline'. The subscript $p$ on $B _ { p } ( { \boldsymbol { x } } )$ denotes that $B _ { p } ( { \boldsymbol { x } } )$ is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$

Figure 19.1 shows $\pmb { B }$ -splines of degrees one, two and three when the spacing between knots is constant. We note that the value of each spline is positive,except where it is constrained to be zero.The following theorem proves that this property is obtained by all $\pmb { B }$ -splines,and it gives a useful condition on the number of zeros of some other spline functions.

# Theorem 19.1

Let $\pmb { S }$ be a function in the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ，that is identically zero on the intervals $[ \xi _ { 0 } , \xi _ { p } ] \mathrm { a n d } [ \xi _ { q } , \xi _ { n } ] ,$ and that has $r$ zeros in the open interval $( \xi _ { p } , \xi _ { q } )$ ，where $p$ and $q$ are integers that satisfy the condition $0 < p < q < n$ ,and where $r$ is finite.Then the number of zeros is bounded by the inequality

$$
r \leqslant q - ( p + k + 1 ) .
$$

Proof. When $\pmb { s }$ is composed of straight line segments, then it has at most one zero in each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = p , p + 1 , \ldots , q - 1 \}$ Because $s ( \xi _ { p } )$ and $s ( \xi _ { q } )$ are both zero, it follows that the total number of zeros in the open interval $( \xi _ { p } , \xi _ { q } )$ is at most $( q - p - 2 )$ . Therefore the theorem is true when $k = 1$

In order to treat larger values of $k$ ,we require an upper bound on the number of sign changes of a linear spline, $\pmb { \sigma }$ say,that is in the space $\mathcal { S } ( 1 , \xi _ { p } , \xi _ { p + 1 } , . . . , \xi _ { q } )$ ，and that is zero at $\xi _ { p }$ and $\xi _ { q } .$ ，Because no sign changes can occur in the intervals $[ \xi _ { p } , \xi _ { p + 1 } ]$ and $[ \xi _ { q - 1 } , \xi _ { q } ] ,$ ，and because each of the other intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = p + 1 , p + 2 , \ldots , q - 2 \}$ contributes at most one sign change,the total number of sign changes is also bounded above by $( q - p - 2 )$ . An important difference between this result and the one given in the previous paragraph is that some of the linear sections of $\pmb { \sigma }$ are allowed to be identically zero.

![](images/58591ea408dbeb92ecc1a8bc6b049440802bb1d669ceabe56961c13fb50bd775.jpg)  
Figure 19.1. $B$ -splines of degrees one, two and three.

To complete the proof of the theorem for $k \geqslant 2$ ，we let $\pmb { \sigma }$ be the function $\{ s ^ { ( k - 1 ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ and we do some counting. Since, by definition, the function $s$ has $r$ zeros in $( \xi _ { p } , \xi _ { q } )$ , and since $s ( \xi _ { p } )$ and $s ( \xi _ { q } )$ are both zero, the first derivative $\{ s ^ { \prime } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ changes sign at least $( r + 1 )$ times. If $k \geqslant 3$ ,we consider next the second derivative $\{  { s } ^ { \prime \prime } (  { \boldsymbol { { x } } } ) ;  { \boldsymbol { \xi } } _ { p } \leqslant$ $x \leqslant \xi _ { q } \}$ . Because $s ^ { \prime } ( \xi _ { p } )$ and $s ^ { \prime } ( \xi _ { q } )$ are both zero,the number of sign changes of the second derivative is at least one more than the number of sign changes of the first derivative.Hence $s ^ { \prime \prime }$ changes sign at least $( r + 2 )$ times. If $k \geqslant 4$ , we continue this argument inductively. It follows that, for all $k \geqslant 2$ ,the function $\{ \sigma ( x ) = s ^ { ( k - 1 ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ changes sign at least $\left( r + k - 1 \right)$ times. Combining this statement with the result of the previous paragraph gives the inequality

$$
( r + k - 1 ) \leqslant ( q - p - 2 ) .
$$

Therefore the theorem is true.

The theorem implies that $q$ cannot be less than $\left( p + k + 1 \right)$ . Moreover, the proof of the theorem shows that,if $\pmb { s }$ is the $B$ -spline (19.10), then, not only is $r$ equal to zero, but also all the inequalities that lead to condition (19.12）are satisfied as equations.Hence,for $j = 0 , 1 , \ldots , k - 1$ ，the derivative $\{ B _ { p } ^ { ( j ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { p + k + 1 } \}$ changes sign exactly $j$ times. Therefore Schoenberg made the highly descriptive remark that $^ { \bullet } B$ -splines are bell-shaped'.

# 19.3 $\pmb { B }$ -splines as basis functions

The fact that the $B$ -spline (19.1O) is non-zero only in the interval $[ \xi _ { p } , \xi _ { p + k + 1 } ]$ can be very useful in practical computer calculations. Therefore we seek a basis of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is composed of $\pmb { B }$ -splines.We include the functions $\{ B _ { p } ; p = 0 , 1 , \dotsc , n - k - 1 \}$ in the basis,because they are linearly independent and they are all in ${ \mathcal { S } } .$ The dimension of the space that is spanned by these functions, however,is $( n - k )$ ,while the dimension of $\mathcal { S }$ is $( n + k )$ .Therefore another $_ { 2 k }$ basis functions are required.A convenient way of choosing them so that they are also $B$ -splines is to introduce some extra knots outside the interval $[ a , b ]$ .Specifically，, we let $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , - 1 \}$ and $\{ \xi _ { j } ; j = n + 1$ ， $n + 2 , \ldots , n + k \}$ be any points on the real line that satisfy the conditions

$$
\begin{array} { r l } & { \xi _ { - k } < \xi _ { - k + 1 } < . . . < \xi _ { - 1 } < \xi _ { 0 } = a } \\ & { b = \xi _ { n } < \xi _ { n + 1 } < \xi _ { n + 2 } < . . . < \xi _ { n + k } } \end{array} \biggr \} .
$$

For example, we may set $\{ \xi _ { j } = \xi _ { 0 } + j ( \xi _ { 1 } - \xi _ { 0 } ) ; j = - 1 , - 2 , \ldots , - k \}$ and $\{ \xi _ { j } = \xi _ { n } + ( j - n ) ( \xi _ { n } - \xi _ { n - 1 } ) ; j = n + 1 , n + 2 , \ldots , n + k \} .$ . We now define $B _ { p }$ by equation(19.10) for p = -k,-k +1,...,n -1, but we make use of the function value $B _ { p } ( x )$ only if $x$ is in the interval $[ a , b ]$ .Hence the total number of $B$ -splines is equal to the dimension of $\mathcal { S } .$ The following theorem shows that every element of $\mathcal { S }$ can be expressed in the form

$$
s ( x ) = \sum _ { j = - k } ^ { n - 1 } \lambda _ { j } B _ { j } ( x ) , \qquad a \leqslant x \leqslant b .
$$

# Theorem 19.2

Let the points $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , n + k \}$ satisfy conditions (19.1）and (19.13)，and let $\scriptstyle B _ { p }$ be defined by equation (19.10) for $p = - k , - k + 1 , \ldots , n - 1 .$ Then the functions $\{ B _ { p } ( x ) , a \leqslant x \leqslant b ; p = - k ,$ $- k + 1 , \ldots , n - 1 \}$ are a basis of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$

Proof. The definition (19.1O) implies that each of the functions $\{ B _ { p } ( x )$ $, a \leqslant x \leqslant b ; p = - k , - k + 1 , . . . , n - 1 \}$ isin $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ， and we have noted already that the number of functions is equal to the dimension of ${ \mathcal { S } } .$ It is therefore sufficient to show that the functions are linearly independent. We follow the normal method of proof, which is to show that, if the spline

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x ) \cdot
$$

is zero on $a \leqslant x \leqslant b$ ，then all the coefficients $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots \right.$ ， $n - 1 \}$ are zero.

Let $\xi _ { - k - 1 }$ be any real number that is less than $\xi _ { - k }$ . We consider the spline $\{ s ( x ) ; \xi _ { - k - 1 } \leqslant x \leqslant \xi _ { 1 } \}$ ，where $s ( x )$ has the value (19.15). The definition (19.10) implies $\{ s ( x ) = 0 ; \xi _ { - k - 1 } \leqslant x \leqslant \xi _ { - k } \}$ .Therefore,if $s ( x )$ is also zero for $\xi _ { 0 } \leqslant x \leqslant \xi _ { 1 }$ , it follows from the remark,made immediately after the proof of Theorem 19.1, that $\pmb { s }$ is identically zero on $[ \xi _ { - k - 1 } , \xi _ { 1 } ]$ Hence it is sufficient to show that the condition $\{ s ( \boldsymbol { x } ) = 0$ ； $\xi _ { - k } \leqslant x \leqslant b \}$ implies $\left\{ \lambda _ { p } = 0 ; p = - k , - k + 1 , \ldots , n - 1 \right\}$

Alternatively we may prove the equivalent result that, if any of the numbers $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ are non-zero, then $s$ is not identically zero on $[ \xi _ { - k } , b ]$ .We let $q$ be the smallest integer such that $\lambda _ { q }$ is non-zero. It follows from the definitions (19.10) and (19.15) that the equation

$$
\begin{array} { r } { s ( x ) = \lambda _ { q } B _ { q } ( x ) , \qquad \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } , } \end{array}
$$

is satisfied. Hence $s ( x )$ is non-zero for $\xi _ { q } < x \leqslant \xi _ { q + 1 }$ , which completes the proof of the theorem.□

In order to demonstrate the way in which a $\pmb { B }$ -spline basis can be used, we consider the problem of expressing the cardinal function of Figure 18.2 in the form

$$
l _ { j } ( x ) = \sum _ { p = - \infty } ^ { \infty } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty .
$$

Because the knots are the points $\{ \xi _ { i } = i h ; i = 0 , \pm 1 , \pm 2 , \ldots \} ,$ ,the $\pmb { B }$ -spline $\scriptstyle B _ { p }$ is the function

$$
\begin{array} { c } { { B _ { p } ( x ) = \displaystyle \frac { 1 } { 2 4 h ^ { 4 } } [ ( x - \xi _ { p } ) _ { + } ^ { 3 } - 4 ( x - \xi _ { p + 1 } ) _ { + } ^ { 3 } + 6 ( x - \xi _ { p + 2 } ) _ { + } ^ { 3 } } } \\ { { - 4 ( x - \xi _ { p + 3 } ) _ { + } ^ { 3 } + ( x - \xi _ { p + 4 } ) _ { + } ^ { 3 } ] , ~ - \infty < x < \infty . } } \end{array}
$$

In particular the equations

$$
\left. \begin{array} { l } { B _ { p } ( \xi _ { p + 1 } ) = 1 / \left( 2 4 h \right) } \\ { B _ { p } ( \xi _ { p + 2 } ) = 1 / ( 6 h ) } \\ { B _ { p } ( \xi _ { p + 3 } ) = 1 / \left( 2 4 h \right) } \end{array} \right\}
$$

are satisfied.Because $\scriptstyle B _ { p }$ is zero at all the other knots, it follows from equation (19.17) that $l _ { j } ( \pmb { \xi } _ { i } )$ has the value

$$
l _ { j } ( \xi _ { i } ) = [ \lambda _ { i - 1 } + 4 \lambda _ { i - 2 } + \lambda _ { i - 3 } ] / 2 4 h .
$$

Therefore the cardinality conditions $\{ l _ { j } ( \pmb { \xi } _ { i } ) = \delta _ { i j } ; i = 0 , \pm 1 , \pm 2 , . . . \}$ give the equations

$$
\lambda _ { i - 1 } + 4 \lambda _ { i - 2 } + \lambda _ { i - 3 } = 2 4 h \delta _ { i j } , \qquad i = 0 , \pm 1 , \pm 2 , \ldots .
$$

This recurrence relation has just one bounded solution, namely the values

$$
\lambda _ { p } = 4 \sqrt { 3 ( \sqrt { 3 } - 2 ) ^ { | j - 2 - p | } } h , \qquad p = 0 , \pm 1 , \pm 2 , . . . ,
$$

which are the required coefficients of expression (19.17). Two advantages of using $\pmb { B }$ -splines are that the method of calculating cardinal functions can be extended easily to splines of higher degree,and, for any $x ,$ the number of non-zero terms in the sum (19.17) or (19.14) is finite.

It is interesting also to express the function (19.4) in terms of $\pmb { B }$ -splines. Therefore we introduce extra knots at the points $\{ \xi _ { j } = j ; j = - 3$ ， $- 2 , \ : - 1 , \ : n + 1 , \ : n + 2 , \ : n + 3 \}$ .Because the shape of the spline (19.4) is the same as the tail of the cardinal function (19.17),the required expression has the form

$$
s ( x ) = \alpha \sum _ { p = - 3 } ^ { n - 1 } ( \sqrt { 3 - 2 } ) ^ { p } B _ { p } ( x ) , \qquad 0 \leqslant x \leqslant n ,
$$

where $_ { \pmb { \alpha } }$ is a constant. Equation (19.18) and the property $s ^ { \prime } ( 0 ) = 1$ give the value $\scriptstyle \alpha = { \frac { 4 } { 3 } } ( 7 { \sqrt { 3 - 1 2 } } )$ .If $s ( 1 0 . 5 )$ is calculated numerically from expression (19.23), then a small number is found, because of the factor $( { \sqrt { 3 - 2 } } ) ^ { p }$ and because the first non-zero term of the sum occurs when $p = 7$ . Hence the $B$ -spline basis avoids the very serious cancellation that occurs when equation (19.4) is used to evaluate $s ( 1 0 . 5 )$

# 19.4 A recurrence relation for $\pmb { { \cal B } }$ -splines

In many algorithms for approximation and data fitting it is necessary to calculate the values of $\pmb { B }$ -splines for several values of the variable $x$ . One possible method is to calculate directly the expression

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \bigg [ \prod _ { \stackrel { i = p } { i \ne j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } \bigg ] ( x - \xi _ { j } ) _ { + } ^ { k } ,
$$

which is the same as equation (19.1O),except that the superscript $k$ on the left-hand side shows the degree of the $\pmb { B }$ -spline explicitly. If one allows for the fact that the term in square brackets is independent of $x$ ,then this method is quite suitable, unless $x$ is very close to $\xi _ { p + k + 1 }$ . The difficulty in this case is that $B _ { p } ^ { k } ( x )$ should tend to zero as $x$ tends to $\xi _ { p + k + 1 }$ , butformula (19.24) relies on cancellation to give this property. It would be better to make use of the fact that $B _ { p } ^ { k } ( x )$ is a multiple of $( x - \xi _ { p + k + 1 } ) ^ { k }$ when $x$ is in the interval $[ \xi _ { p + k } , \xi _ { p + k + 1 } ]$ 、A procedure that is efficient in all cases is described in this section. It depends on the following recurrence relation.

# Theorem 19.3

Let $k$ be an integer that is greater than one, and let $\{ \xi _ { j } ; j = p ;$ $p + 1 , \ldots , p + k + 1 \}$ be a set of distinct real numbers, which we assume are in ascending order. Then the function (19.24) satisfies the equation

$$
B _ { p } ^ { k } ( x ) = \frac { ( x - \xi _ { p } ) B _ { p } ^ { k - 1 } ( x ) + ( \xi _ { p + k + 1 } - x ) B _ { p + 1 } ^ { k - 1 } ( x ) } { ( \xi _ { p + k + 1 } - \xi _ { p } ) } ,
$$

for all real values of $x$

Proof. Let $s ( x )$ be the right-hand side of expression (19.25).The function $\{ s ( x ) ; - \infty < x < \infty \}$ is composed of polynomial pieces, each of degree at most $k$ ，that are joined at the knots $\left\{ \xi _ { j } ; \ j = p , p + 1 , \ldots , \right.$ $p + k + 1 \}$ . By the definition of a $\pmb { B }$ -spline,this function is identically zero for $x \leqslant \xi _ { p }$ and $x \geqslant \xi _ { p + k + 1 }$ . When $x$ is in the interval $[ \xi _ { p } , \xi _ { p + 1 } ] ,$ ，the definition (19.24) implies the identity

$$
\boldsymbol { B } _ { p } ^ { k } ( \boldsymbol { x } ) = \frac { ( \boldsymbol { x } - \boldsymbol { \xi } _ { p } ) } { ( \boldsymbol { \xi } _ { p + k + 1 } - \boldsymbol { \xi } _ { p } ) } \boldsymbol { B } _ { p } ^ { k - 1 } ( \boldsymbol { x } ) ,
$$

and $B _ { p + 1 } ^ { k - 1 } \left( x \right)$ is zero. Therefore the equation $\{ s ( x ) = B _ { p } ^ { k } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { p + 1 } \}$ is satisfied. In order to prove that the conditions $\{ s ( x ) = B _ { p } ^ { k } ( x )$ ； $\xi _ { j } \leqslant x \leqslant$ $\xi _ { j + 1 } ; j = p _ { , } + 1 , p + 2 , \ldots , p + k \}$ hold also, it is sufficient to show that the change in $\pmb { s }$ at the knots $\{ \xi _ { j } ; j = p + 1 , p + 2 , \ldots , p + k \}$ agrees with the change that is given in equation (19.24). This result is obtained by straightforward algebra from the definitions of $B _ { p } ^ { k - 1 } ( x ) , B _ { p + 1 } ^ { k - 1 } ( x )$ and $\pmb { s } ( \pmb { x } )$ . When $j$ is in $[ p + 1 , p + k ]$ ，we find that the change in $\pmb { s }$ at $\xi _ { j }$ is the polynomial $( x - \xi _ { j } ) ^ { k - 1 } / ( \xi _ { p + k + 1 } - \xi _ { p } )$ multiplied by the factor

$$
\begin{array} { l } { { ( x - \xi _ { p } ) \overset { p \ \not \mapsto k } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } + ( \xi _ { p + k + 1 } - x ) \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { i } ) } } } \\ { { \ } } \\ { { = [ ( x - \xi _ { p } ) ( \xi _ { p + k + 1 } - \xi _ { i } ) + ( \xi _ { p + k + 1 } - x ) ( \xi _ { p } - \xi _ { i } ) ] \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } } } \\ { { \ } } \\ { { \ } } \\ { { = ( x - \xi _ { i } ) ( \xi _ { p + k + 1 } - \xi _ { p } ) \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { i } ) } . } } \end{array}
$$

Hence the change in $\pmb { s }$ is the same as the change in ${ B } _ { p } ^ { k }$ ， which completes the proof of the theorem.□

Equation (19.25) is similar to the recurrence formula (5.14) for divided differences. Therefore a convenient method for calculating $B _ { p } ^ { k } ( x )$ for a fixed value of $x$ is to compute the columns of the tableau

in sequence. If $x$ is in the interval $[ \xi _ { i } , \xi _ { i + 1 } ] ,$ ,then the numbers in the first column have the values

$$
\left. \begin{array} { l } { { B _ { j } ^ { 1 } ( x ) = 0 , \qquad j \neq i - 1 , \qquad j \neq i } } \\ { { B _ { i - 1 } ^ { 1 } ( x ) = ( \xi _ { i + 1 } - x ) / [ ( \xi _ { i + 1 } - \xi _ { i - 1 } ) ( \xi _ { i + 1 } - \xi _ { i } ) ] \Bigg \} . } } \\ { { B _ { i } ^ { 1 } ( x ) = ( x - \xi _ { i } ) / [ ( \xi _ { i + 1 } - \xi _ { i } ) ( \xi _ { i + 2 } - \xi _ { i } ) ] } } \end{array} \right.
$$

The remaining entries in the table (19.28) are obtained from equation (19.25),which gives $B _ { p } ^ { k } ( x )$ in the final column. This procedure is highly suitable for numerical computation， because,except for differences between values of the variables, there is no cancellation. Moreover, it is easy to extend the table to provide $B _ { p } ^ { k } ( x )$ for a range of values of $p$

There are other relations between $\pmb { B }$ -splines and divided differences. One of them is so fundamental that it is used sometimes to introduce $B$ -splines. It comes from a property of the function

$$
f ( \xi ) = ( - 1 ) ^ { k + 1 } ( x - \xi ) _ { + } ^ { k } , \qquad - \infty < \xi < \infty ,
$$

where $x$ is any fixed number.We recall from Chapter 5 that the divided difference $f [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { p + { \dot { k } } + 1 } ]$ is the coefficient of $\xi ^ { k + 1 }$ in the polynomial of degree at most $k + 1$ that interpolates the function values $\{ f ( \xi _ { j } ) ; j = p , p + 1 , \ldots , p + k + 1 \}$ . Therefore,if we make the definition

$$
B _ { p } ^ { k } ( x ) = f [ \xi _ { p } , \xi _ { p + 1 } , . . . , \xi _ { p + k + 1 } ] ,
$$

it follows that $B _ { p } ^ { k } ( x )$ is zero when $x \leqslant \xi _ { p }$ and when $x ^ { \prime } \geq \xi _ { p + k + 1 }$ . Further, because the divided difference is a linear combination of the function values $\{ f ( \xi _ { j } ) ; j = p , p + 1 , \ldots , p + k + 1 \}$ ，the function $\{ B _ { p } ^ { k } ( x ) ; - \infty < x <$ $\infty \}$ is a spline of degree $k$ whose knots are the points $\{ \xi _ { j } ; j = p , p + 1 \}$ $\cdots , p + k + 1 \}$ . Hence ${ B } _ { p } ^ { k }$ isa $\pmb { B }$ -spline. An alternative and less interesting method of reaching this conclusion is to deduce from equations (5.2),(19.30) and (19.31) that $B _ { p } ^ { k } ( x )$ has the value

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \frac { ( - 1 ) ^ { k + 1 } ( x - \xi _ { j } ) _ { + } ^ { k } } { \underset { i = p } { \prod } ( \xi _ { j } - \xi _ { i } ) } ,
$$

which is equivalent to the definition (19.24).

There are some advantages in taking the point of view that $B _ { p } ^ { k } ( x )$ is the divided difference (19.31). In particular, a neat proof of Theorem 19.3 can be obtained by letting $\pmb { g }$ and $h$ be the functions

$$
\begin{array} { l } { { g ( \xi ) = ( \xi - x ) , \qquad - \infty < \xi < \infty , \nonumber } } \\ { { h ( \xi ) = ( - 1 ) ^ { k } ( x - \xi ) _ { + } ^ { k - 1 } , \qquad - \infty < \xi < \infty } } \end{array} \biggr \} ,
$$

and by calculating expression (19.31) from the product formula

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } g [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { j } ] h [ \xi _ { j } , \xi _ { j + 1 } , \ldots , \xi _ { p + k + 1 } ] ,
$$

which is given in Exercise 5.9.

# 19.5 The Schoenberg-Whitney theorem

A convenient method for calculating an approximation from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ is to inter-

polate some function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , n + k \}$ . We let the interpolation points be in ascending order

$$
a \leqslant x _ { 1 } < x _ { 2 } < . . . < x _ { n + k } \leqslant b ,
$$

but there is no need for any of them to be at knot positions. Because the number of function values is equal to the dimension of ${ \mathcal { S } } ,$ it is important to ask whether there is just one element $\pmb { s }$ in $\mathcal { S }$ that satisfies the equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k .
$$

We introduce extra knots outside the interval $[ a , b ] ,$ in order that every element of $\mathcal { S }$ can be expressed as a linear combination of the $\pmb { B }$ -splines $\{ B _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \}$ Useful necessary and sufficient conditions for $\pmb { s }$ to be unique are given in the following theorem.

# Theorem 19.4 (Schoenberg-Whitney)

Let the real numbers $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , n + k \}$ be in strictly ascending order,and,for $p = - k , - k + 1 , \ldots , n - 1$ ,let $\{ B _ { p } ( x ) ; - \infty < x <$ $\infty \}$ be defined by equation (19.10). Let the interpolation points $\{ x _ { i } ; i =$ $1 , 2 , \ldots , n + k \}$ also be in strictly ascending order.Then,for any function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , n + k \}$ , the equations

$$
\sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k ,
$$

have a unique solution $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ , if and only if all the numbers $\{ B _ { j - k - 1 } ( x _ { j } ) ; j = 1 , 2 , \ldots , n + k \}$ are non-zero.

Proof. Suppose that $B _ { j - k - 1 } ( x _ { j } )$ is zero.Then either the inequality $x _ { j } \leqslant \xi _ { j - k - 1 }$ or the inequality $x _ { j } \geqslant \xi _ { j }$ is satisfied.In the first case $B _ { p } ( { \boldsymbol { x } } )$ is zero if the conditions $p \geqslant j - k - 1$ and $x \leqslant x _ { j }$ both hold. It follows that the first $j$ of the equations (19.37) have the form

$$
\sum _ { p = - k } ^ { j - k - 2 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , j .
$$

Because these $j$ equations depend on only $( j - 1 )$ unknowns, they do not have a solutioh for a general right-hand side. Similarly, if $x _ { j } \geqslant \xi _ { j } ,$ then the last $( n + k + 1 - j )$ equations have the form

$$
\sum _ { p = j - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = j , j + 1 , \ldots , n + k ,
$$

so again the number of unknowns is insuffcient. Therefore the conditions

$$
B _ { j - k - 1 } ( x _ { j } ) \neq 0 , \qquad j = 1 , 2 , \ldots , n + k ,
$$

are necessary for the system (19.37) to have a solution for any $f .$

The equations (19.37) do not have a unique solution if and only if there exist parameters $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ ，that are not all zero, such that the function

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty ,
$$

satisfies the conditions

$$
s ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , n + k .
$$

In this case Theorem 19.2 states that the function (19.41) is not identically zero.Therefore,to prove the second half of the theorem,it is sufficient to show that conditions (19.40), (19.41) and (19.42) do not allow $\pmb { s }$ to be a non-zero spline function.

We suppose that these conditions hold, but that $\pmb { s }$ is non-zero. As $x$ ranges over the real line, there are some intervals,including $x \leqslant \xi _ { - k }$ and $x \geq \xi _ { n + k } ,$ on which $\pmb { s }$ is identically zero,but in other parts of the range the number of zeros of $\pmb { s }$ is finite. Therefore there are knots, $\xi _ { p }$ and $\xi _ { q } ,$ such that $\pmb { s }$ is identically zero on $[ \xi _ { p - 1 } , \xi _ { p } ]$ and $[ \xi _ { q } , \xi _ { q + 1 } ] ,$ ，while, in the open interval $( \xi _ { p } , \xi _ { q } )$ ， $\pmb { s }$ has only a finite number of zeros, $r$ say. It may be necessary to introduce two more artificial knots $\xi _ { - k - 1 }$ and $\xi _ { n + k + 1 }$ satisfying the conditions $\xi _ { - k - 1 } < \xi _ { - k }$ and $\xi _ { n + k + 1 } > \xi _ { n + k }$ .In any case,the proof of Theorem 19.1 shows that inequality (19.11) is obtained.However, the $\pmb { B }$ -splines $\{ B _ { j } ; j = p , p + 1 , \ldots , q - k - 1 \}$ take non-zero values only if the variable $x$ is in the interval $( \xi _ { p } , \xi _ { q } )$ . Therefore condition (19.40) implies that the points $\{ x _ { j + k + 1 } ; j = p , p + 1 , \dots , q - k - 1 \}$ are all in this interval. It follows from equation (19.42) that the number of zeros of $\pmb { s }$ in $( \xi _ { p } , \xi _ { q } )$ is at least $\left( q - p - k \right)$ ，which contradicts inequality (19.11). Therefore the theorem is true.□

The calculation of the spline $s$ in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the equations (19.36) shows the usefulness of many of the results of this chapter. The Schoenberg-Whitney theorem makes it easy to check whether the equations have a solution.We may use the ideas of Section 19.3 to express $\pmb { s }$ as a linear combination of $\pmb { B }$ -splines. Therefore we have to calculate the parameters $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ that are defined by the system (19.37). This system is easy to solve,because the properties of $\pmb { B }$ -splines, given in Section 19.2,imply that, for each $i ,$ at most $( k + 1 )$ of the matrix elements $\{ B _ { p } ( x _ { i } ) ; p = - k , - k + 1 , \ldots , n - 1 \}$ are non-zero. The non-zero matrix elements can be obtained conveniently from the recurrence relation that is described in Section 19.4. Hence,after the knots of the spline and the points $\{ x _ { i } ; i = 1 , 2 , \ldots , n + k \}$ are chosen,it is straightforward to calculate spline approximations by interpolation.

# 19 Exercises

19.1 Let $V$ be a polyhedron in $\mathcal { R } ^ { k + 1 }$ that has $( k + 2 )$ vertices, for example a tetrahedron in $\mathcal { R } ^ { 3 }$ . Let d be a fixed non-zero vector in $\mathcal { R } ^ { k + 1 }$ ,and,foranyrealnumber $\theta _ { i }$ let $U ( \pmb \theta )$ be the linear manifold $\{ \mathbf { x } \colon \mathbf { x } ^ { \mathrm { T } } \mathbf { d } = \theta , \mathbf { x } \in \mathcal { R } ^ { k + 1 } \}$ , which is a slice of $\mathcal { R } ^ { k + 1 }$ that is orthogonal to the direction d. Let $s ( \theta )$ be the volume (or area) of the intersection of $U ( \pmb \theta )$ and $V .$ Prove that, if no linear manifold $U ( \theta )$ contains more than one vertex of the polyhedron, then the function $\{ s ( \theta ) ; - \infty < \theta < \infty \}$ is a $\pmb { B }$ -spline of degree $k$ ·

19.2 Let $k = 3$ ， $n = 1 0$ and $\{ \xi _ { j } = j ; j = - 3 , - 2 , \ldots , 1 3 \}$ in the statement of Theorem 19.2.Express the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant$ $1 0 \}$ as a linear combination of the $\pmb { B }$ -splines $\{ B _ { p }$ ； $p = - 3$ ， $- 2 , \ldots , 9 \}$ .Check the calculation of the coefficients by evaluating your expression at $\begin{array} { r } { x = l + \frac { 1 } { 2 } , } \end{array}$ ,where $\iota$ is any integer in the range [0, 9].

19.3 Express the first derivative of the $\pmb { B }$ -spline (19.10) in terms of two $\pmb { B }$ -splines of degree $( k - 1 )$

19.4 Let ${ B } _ { p } ^ { k }$ be the $\pmb { B }$ -spline of degree $k$ whose knots have the values $\left\{ \xi _ { j } = j ; j = p , p + 1 , \ldots ; p + k + 1 \right\}$ ，Use the recurrence relation (19.25) to determine the value of the $\pmb { B }$ -spline at its knots for $k = 1 , 2 , 3 , \ldots , 7$ . A convenient check on your calculations is that the equation

$$
\sum _ { j = p + 1 } ^ { p + k } B _ { p } ^ { k } ( \xi _ { j } ) = 1 / ( k + 1 )
$$

should be satisfied, which is a consequence of Theorem 20.1.

9.5 Let $\pmb { n }$ be a positive integer, let $\pmb { \alpha }$ be a constant from the interval (0,1),and let the points $\{ \xi _ { j } \}$ and $\{ x _ { i } \}$ have the values $\{ \xi _ { j } = j ; j =$ $0 , 1 , \ldots , n \}$ ， $\left\{ x _ { i } = \alpha + i - 1 ; i = 1 , 2 , \ldots , n \right\}$ and $x _ { n + 1 } = n$ . Show that, for any function $f$ in $\textstyle \mathcal { C } [ 0 , n ] ,$ ,there is a linear spline in the space $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that interpolates the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , n + 1 \}$ . Sketch the cardinal functions of the interpolation procedure. It should be clear that the $\infty$ -norm of the interpolation operator is large if $\pmb { \alpha }$ is near one, but that it is of moderate size if $\alpha < \frac { 1 } { 2 }$

19.6 Let $\pmb { s }$ be an approximation from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ]$ ，where the knots satisfy the conditions (19.1). Prove that $\pmb { s }$ is a best minimax approximation from $\mathcal { S }$ to $f$ if and only if there exist integers $p$ and $q$ in $[ 0 , n ]$ and points $\{ \zeta _ { i } ; i = 0 , 1 , . . . , q - p + k \}$ such that the following conditions are obtained:

$$
\xi _ { p } \leqslant \zeta _ { 0 } < \zeta _ { 1 } < . . . < \zeta _ { q - p + k } \leqslant \xi _ { q } ,
$$

$$
| f ( \zeta _ { i } ) - s ( \zeta _ { i } ) | = \| f - s \| _ { \infty } , \qquad 0 \leqslant i \leqslant q - p + k ,
$$

$$
[ f ( \zeta _ { i } ) - s ( \zeta _ { i } ) ] = - [ f ( \zeta _ { i - 1 } ) - s ( \zeta _ { i - 1 } ) ] , \qquad 1 \leqslant i \leqslant q - p + k .
$$

19.7 Prove Theorem 19.3 by the method that is suggested in the last paragraph of Section 19.4.

19.8 Let ${ B } _ { p } ^ { k }$ be the spline function (19.10),where the superscript shows the degree of the spline,and where we allow $k$ to be any non-negative integer. Let $x$ be any point in the interval $( \xi _ { p } , \xi _ { p + k + 1 } ]$ ，and let the integer $q$ be defined by the condition $\xi _ { q } < x \leqslant \xi _ { q + 1 }$ . Prove that the indefinite integral of ${ B } _ { p } ^ { k }$ has the value

$$
\int _ { \xi _ { p } } ^ { x } B _ { p } ^ { k } ( \theta ) \mathrm { d } \theta = \frac { 1 } { k + 1 } \sum _ { j = 0 } ^ { q - p } \left( x - \xi _ { p + j } \right) B _ { p + j } ^ { k - j } ( x ) .
$$

This formula allows the integral to be calculated without any cancellation from the bottom entries of the columns of the tableau (19.28).

19.9 Let $k$ and $_ n$ be positive integers such that $( k + n )$ is even, and let the knots $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ satisfy inequality (19.1).Let $f$ be a function in $\mathcal { C } ^ { ( 1 ) } [ a , b ]$ and let $\{ x _ { i } ; i = 1 , 2 , \ldots , { \textstyle { \frac { 1 } { 2 } } } ( k + n ) \}$ be a set of distinct points in $[ a , b ]$ Obtain necessary and suffcient conditions on these points that imply that a unique spline in $\mathcal { S }$ is defined by the equations $\{ s ( x _ { i } ) = f ( x _ { i } ) , s ^ { \prime } ( x _ { i } ) = f ^ { \prime } ( x _ { i } ) ; i = 1 , 2 , \ldots , { \frac { 1 } { 2 } } ( k + n ) \}$

19.10 Let $\mathcal { S }$ be the space of quadratic splines that have the knots $\{ \xi _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , \ldots \} ,$ ，let $f$ be a bounded function in $\mathcal { C } ( - \infty , \infty )$ ,and let the function

$$
s ( x ) = \sum _ { p = - \infty } ^ { \infty } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty ,
$$

be the best least squares approximation from $\mathcal { S }$ to $f .$ Calculate the elements of the matrix of the normal equations.Hence deduce that there exist multipliers $\{ \mu _ { l } ; l = 0 , \pm 1 , \pm 2 , \ldots \}$ such that $\lambda _ { p }$ has the value

$$
\lambda _ { p } = \sum _ { l = - \infty } ^ { \infty } \mu _ { l } \int _ { \xi _ { p + l } } ^ { \xi _ { p + l + 3 } } B _ { p + l } ( x ) f ( x ) \mathrm { d } x , \qquad p = 0 , \pm 1 , \pm 2 , . . . ,
$$

and that the order of magnitude of $\left| \mu _ { l } \right|$ is $( 0 . 4 3 0 6 ) ^ { | l | } h$

# Convergence properties of spline approximations

# 20.1 Uniform convergence

If one requires a spline approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ , then it is useful sometimes to have bounds on the least maximum error

$$
d ^ { * } ( { \mathcal { S } } , f ) = \operatorname* { m i n } _ { s \in { \mathcal { S } } } \| f - s \| _ { \infty } .
$$

They are studied in this chapter, including the case when $f$ is differentiable. It is assumed that the numbers $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy the conditions

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b ,
$$

and we let $\boldsymbol { h }$ be the maximum interval between knots

$$
h = \operatorname* { m a x } _ { i = 1 , 2 , \ldots , n } ( \xi _ { i } - \xi _ { i - 1 } ) .
$$

The main purpose of this section is to derive the inequality

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant \omega ( { \frac { 1 } { 2 } } [ k + 1 ] h ) ,
$$

where $\pmb { \omega }$ is the modulus of continuity of $f .$ It follows that any continuous function can be approximated to arbitrarily high accuracy by a spline function of degree $k _ { : }$ ， provided that the spacing between knots is sufficiently small.

In order to express spline functions as linear combinations of $\pmb { B }$ - splines, we introduce extra knots that satisfy condition (19.13). Instead of using $\smash { B _ { p ; \mathrm { ~ \scriptsize ~ . ~ } } ^ { k } }$ ,however, it is more convenient to work with the function

$$
N _ { p } ^ { k } ( x ) \cdot = ( \xi _ { p + k + 1 } - \xi _ { p } ) \sum _ { { j = p \atop \prod _ { i = p } ^ { p + k + 1 } } \atop { i \ne j } } ^ { p + k + 1 } { \frac { ( x - \xi _ { j } ) _ { + } ^ { k } } { p + k + 1 } } , \qquad a \leqslant x \leqslant b ,
$$

which is just $B _ { p } ^ { k } ( x )$ multiplied by the factor $( \xi _ { p + k + 1 } - \xi _ { p } )$ . Therefore the splines $\{ N _ { p } ^ { k } ; p = - k , \ - k + 1 , \ldots , n - 1 \}$ are a basis of ${ \mathcal { S } } ,$ and $N _ { p } ^ { k } ( x )$ is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$ . It is important to notice also that Theorem 19.1 and equation (20.5) imply the condition

$$
N _ { p } ^ { k } ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b .
$$

Because the function $\{ s ( x ) = 1 ; a \leqslant x \leqslant b \}$ is in $\mathcal { S } ,$ it can be expressed in terms of the basis functions.The factor $( \xi _ { p + k + 1 } - \xi _ { k } )$ is present in equation (20.5) in order that this expression has the following simple form.

# Theorem 20.1

For all positive integers $k$ ， the functions $\{ N _ { p } ^ { k } ; p = - k , - k + 1 \}$ $\cdots , n - 1 \}$ satisfy the identity

$$
\sum _ { p = - k } ^ { n - 1 } N _ { p } ^ { k } \left( x \right) = 1 , \qquad a \leqslant x \leqslant b .
$$

Proof. Theorem 19.3 allows a proof by induction. By changing the notation from $\boldsymbol { B } _ { p } ^ { k }$ to $\boldsymbol { N } _ { p } ^ { k }$ in expression (19.25), we find that the equation

$$
N _ { p } ^ { k } \left( x \right) = \frac { \left( x - \xi _ { p } \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) + \frac { \left( \xi _ { p + k + 1 } - x \right) } { \left( \xi _ { p + k + 1 } - \xi _ { p + 1 } \right) } N _ { p + 1 } ^ { k - 1 } \left( x \right)
$$

holds for $p = - k , - k + 1 , \ldots , n - 1$ .The two sides of this equation are summed over $\pmb { p }$ , and we make use of the identities $\{ N _ { - k } ^ { k - 1 } ( x ) = 0$ ； $a \leqslant x \leqslant$ $^  b \}$ and $\{ N _ { n } ^ { k - 1 } \left( x \right) = 0$ $a \leqslant x \leqslant b \}$ . Hence, for $k \geqslant 2$ , we find the relation

$$
\begin{array} { c } { { \displaystyle \sum _ { p = - k } ^ { n - 1 } N _ { p } ^ { k } \left( x \right) = \sum _ { p = - k } ^ { n - 1 } \frac { \left( x - \xi _ { p } \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) } } \\ { { + \displaystyle \sum _ { p = - k + 1 } ^ { n } \frac { \left( \xi _ { p + k } - x \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) } } \end{array}
$$

$$
\quad = \sum _ { p = - k + 1 } ^ { n - 1 } N _ { p } ^ { k - 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Therefore,if equation (20.7) holds for $k = 1$ ,then it is satisfied for all positive integers $k$ In the case $k = 1$ the function $\smash { N _ { p } ^ { k } ( x ) }$ is equal to ${ \cal B } _ { p } ^ { 1 } ( x )$ multiplied by $( \xi _ { p + 2 } - \xi _ { p } )$ . It follows from expression (19.29) that equation (20.7) is valid for $k = 1$ , which completes the proof.□

The following theorem shows that the properties of $\pmb { B }$ -splines and equation (20.7) provide an elementary proof of the useful bound (20.4).

# Theorem 20.2

For every function $f$ in $\mathcal { C } [ a , b ] .$ ,the least maximum error (20.1) satisfies condition (20.4).

Proof.It is suffcient to find an element $\pmb { s }$ in $\mathcal { S }$ such that the inequality

$$
\| f - s \| _ { \infty } \leqslant \omega ( { \frac { 1 } { 2 } } [ k + 1 ] h )
$$

is obtained. We let $\pmb { s }$ be the spline function

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } f ( x _ { p } ) N _ { p } ^ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\scriptstyle { \mathfrak { x } } _ { p }$ is the number in the range $[ a , b ]$ that is closest to $\frac { 1 } { 2 } \big ( \xi _ { p } + \xi _ { p + k + 1 } \big )$ · Therefore $\scriptstyle { \pmb { x _ { p } } }$ is one of the three numbers $a , b$ and $\frac { 1 } { 2 } ( \xi _ { p } + \xi _ { p + k + 1 } )$ . Equations (20.7) and (20.11) imply the relation

$$
f ( x ) - s ( x ) = \sum _ { p = - k } ^ { n - 1 } { \bigl [ } f ( x ) - f ( x _ { p } ) { \bigr ] } N _ { p } ^ { k } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Because the term under the summation sign is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$ , the definitions of $x _ { p }$ and $h$ give the bound

$$
\begin{array} { r l } & { \big | f ( x ) - f ( x _ { p } ) \big | \big | N _ { p } ^ { k } ( x ) \big | \leqslant \omega \big ( \frac { 1 } { 2 } [ \xi _ { p + k + 1 } - \xi _ { p } ] \big ) \big | N _ { p } ^ { k } ( x ) \big | } \\ & { \qquad \leqslant \omega \big ( \frac { 1 } { 2 } [ k + 1 ] h \big ) \big | N _ { p } ^ { k } ( x ) \big | , \qquad a \leqslant x \leqslant b . } \end{array}
$$

It follows from expressions (20.12),(20.6) and (20.7) that the inequality

$$
\begin{array} { r l r } {  {  f ( x ) - s ( x )  \leqslant \omega ( \frac { 1 } { 2 } [ k + 1 ] h ) \sum _ { p = - k } ^ { n - 1 }  N _ { p } ^ { k } ( x )  } } \\ & { } & { = \omega ( \frac { 1 } { 2 } [ k + 1 ] h ) , \qquad a \leqslant x \leqslant b , } \end{array}
$$

is satisfied, which is the required result.[

This proof demonstrates that $B$ -splines are useful, not only for simplifying the numerical calculation of spline approximations, but also for theoretical analysis. Their properties imply that the function value $s ( x )$ ， defined by equation (20.11), is independent of $x _ { p } ,$ unless $\left| x - x _ { p } \right|$ is less than ${ \frac { 1 } { 2 } } [ k + 1 ] h$ .Therefore we have a spline approximation whose local properties are similar to those that are given by the interpolation procedures of Section 18.1. The spline function (20.11), however, does not satisfy any obvious interpolation conditions.

# 20.2 The order of convergence when $f$ is differentiable

It is proved in this section that, if $f$ is a differentiable function, then there are upper bounds on the least maximum error (20.1) of the form

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c h ^ { q } \ \| f ^ { ( j ) } \| _ { \infty } ,
$$

for certain positive integers $\pmb q$ and $j ,$ where $c$ is a number that is independent of $f$ and of the positions of the knots $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ ,and

where $h$ is still the maximum distance between adjacent knots. For example, if $f$ is in $\mathcal { C } ^ { ( 1 ) } [ a , b ] .$ , then expression (20.4) and the definition of the modulus of continuity give the bound

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant { \frac { 1 } { 2 } } ( k + 1 ) h \ \| f ^ { \prime } \| _ { \infty } .
$$

An advantage of this kind of bound is that it indicates the improvement in accuracy that can be obtained by increasing the number of knots. It is therefore advantageous if $q$ is as large as possible in expression (20.15). The following argument shows, however, that, even if $f$ can be differentiated more than $j$ times, then $\pmb q$ is equal to $j .$

Let $f$ be a function in $\mathcal { C } ^ { ( j ) } [ a , b ]$ such that $d ^ { * } ( \mathcal { S } , f )$ is positive. We make the change of variable $\{ \bar { x } = \alpha x$ ； $a \leqslant x \leqslant b $ ，where $\pmb { \alpha }$ is any positive constant. Let $\bar { f }$ be the function $\{ \bar { f } ( \bar { x } ) = f ( \bar { x } / \alpha )$ ； $\alpha a \leqslant \bar { x } \leqslant \alpha b \}$ ,let $\bar { \mathcal { S } }$ be the space $\mathcal { S } ( k , \alpha \xi _ { 0 } , \alpha \xi _ { 1 } , . . . , \alpha \xi _ { n } )$ , and let ${ \bar { s } } ^ { * }$ be a best approximation to $\bar { f }$ from ${ \mathcal { \bar { S } } } .$ We note that the function $\{ s ^ { * } ( x ) = \bar { s } ^ { * } ( \alpha x )$ ； $a \leqslant x \leqslant b \}$ is in $\mathcal { S } _ { \ast }$ Therefore the inequality

$$
\begin{array} { r } { d ^ { * } ( \mathcal { S } , f ) \leqslant \left\| f - s ^ { * } \right\| _ { \infty } } \\ { = \left\| \bar { f } - \bar { s } ^ { * } \right\| _ { \infty } } \\ { = d ^ { * } ( \bar { \mathcal { S } } , \bar { f } ) } \end{array}
$$

is satisfied, where the $\infty$ -norm is applied to two different spaces. We may apply condition (20.15) to $d ^ { * } ( { \bar { \mathcal { S } } } , { \bar { f } } )$ ,when $c$ is independent of $f$ and of the numbers $\left\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \right\}$ .Because the maximum distance between adjacent knots in the space $\mathcal { \bar { S } }$ is $\alpha h$ ,it follows from inequality (20.17) that the bound

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c \left( \alpha h \right) ^ { q } \left\| \bar { f } ^ { ( j ) } \right\| _ { \infty }
$$

is obtained. Therefore, because the definition of $\bar { f }$ implies that $\| \bar { f } ^ { ( j ) } \| _ { \infty }$ is equal to $\pmb { \alpha } ^ { - j } \| f ^ { ( j ) } \| _ { \infty }$ ,the relation

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c h ^ { q } \alpha ^ { q - j } \| f ^ { ( j ) } \| _ { \infty }
$$

holds for all positive values of $\pmb { \alpha }$ . However, the left-hand side of this expression is a positive number that is independent of $\pmb { \alpha }$ ,and,if $q$ is not equal to $j ,$ the right-hand side can be made arbitrarily small by choosing an extreme value of $_ \alpha$ .Hence,even if the restriction is relaxed that $q$ is to be an integer, $q$ cannot be different from $j$ in inequality (20.15).

Therefore, we would like $j$ to be as large as possible. Of course $j$ may not exceed the number of times $f$ can be differentiated, and also it cannot be larger than $( k + 1 )$ ,because inequality (20.15) has to hold in the special case when $f$ is the polynomial $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b \}$ . Therefore the values of $j$ that are given in the following theorem are optimal. Another nice feature of the theorem is that the proof is elementary,although the spacing between knots is allowed to be irregular.

# Theorem 20.3

Let $k$ and $l$ be positive integers. For every function $f$ in $\mathcal { C } ^ { ( l ) } [ a , b ] ,$ and for every integer $j$ in the range [1, $\operatorname* { m i n } ( l , k + 1 ) ]$ ，the least maximum error (20.1) satisfies the condition

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant \frac { ( k + 1 ) ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j } \| f ^ { ( j ) } \| _ { \infty } .
$$

Proof. The proof is by induction,and it is similar to the proof of Theorem 3.2. For the general step of the induction we let the values of both $j$ and $k$ be greater than or equal to two,and we assume that condition (20.20) is satisfied if $j$ and $k$ are replaced by $( j - 1 )$ and $( k - 1 )$ This assumption implies the inequality

$$
\| f ^ { \prime } - \sigma \| _ { \infty } \leqslant \frac { k ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j - 1 } \| f ^ { ( j ) } \| _ { \infty } ,
$$

where $\pmb { \sigma }$ is a best approximation to $f ^ { \prime }$ from the space ${ \mathcal { S } } ( k - 1 ,$ $\xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . We let $\pmb { s }$ be an indefinite integral of $\pmb { \sigma } .$ ,and we let $s ^ { * }$ be a best approximation to $( f - s )$ from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . Therefore inequalities (20.16) and (20.21) give the bound

$$
\begin{array} { r l } { \underset { a \leqslant x \leqslant b } { \operatorname* { m a x } } \left| f ( x ) - s ( x ) - s ^ { * } ( x ) \right| \leqslant \frac { 1 } { 2 } ( k + 1 ) h \left\| f ^ { \prime } - \sigma \right\| _ { \infty } } & { } \\ { \leqslant \frac { ( k + 1 ) ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j } \left\| f ^ { ( j ) } \right\| _ { \infty } . } \end{array}
$$

Because $( \pmb { \mathscr { s } } + \pmb { \mathscr { s } } ^ { * } )$ is in ${ \mathcal { S } } ,$ it follows that inequality (20.20) is satisfied. It remains to establish suitable conditions to begin the inductive argument.

When $j = 1$ ,we find that condition (20.2O) is the same as inequality (20.16),which is valid for $k \geqslant 1$ . It follows that the theorem is true if $k \geq j \geq 1$ . However, in order that the inductive argument can be applied also to the important special case when $j = k + 1$ ,we have to show that inequality (20.20) is valid when $k = 1$ and $j = 2$ . In this case we let $\pmb { s }$ be the function in $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions $\{ s ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \}$ .Because each piece of $\mathcal { S }$ is a linear function, it follows from Theorem 4.2 that, if $x$ is in the interval $[ \xi _ { i } , \xi _ { i + 1 } ] ,$ ，where $i$ is any integer from $[ 0 , n - 1 ] ,$ ，then the equation

$$
f ( x ) - s ( x ) = { \textstyle { \frac { 1 } { 2 } } } ( x - \xi _ { i } ) ( x - \xi _ { i + 1 } ) f ^ { \prime \prime } ( \xi )
$$

holds, where $\xi$ is a point in $[ \xi _ { i } , \xi _ { i + 1 } ]$ that depends on $x$ .Hence we deduce the inequality

$$
\begin{array} { r } { d ^ { * } ( \mathcal { S } , f ) \leqslant \| f - s \| _ { \infty } \leqslant \frac { 1 } { 8 } h ^ { 2 } \| f ^ { \prime \prime } \| _ { \infty } . } \end{array}
$$

Because this condition is stronger than expression (20.20), the proof of the theorem is complete.□

This theorem is useful because it indicates the order of magnitude of the error of a spline approximation when $h$ is small. We recall, however, from Chapter 3, that bounds of the form (20.2O) fail to show that it can be highly advantageous to adapt the distribution of knots to the form of $f .$

# 20.3 Local spline interpolation

If one is selecting a method to calculate an approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ] .$ ,one should ask if there are any sudden changes in the form of $f ,$ for example a derivative discontinuity. For many approximation algorithms, the effect of a discontinuity is to introduce a wave in the spline that decays in magnitude away from the discontinuity. However, if the spacing between knots is increased away from the discontinuity, then the rate of decay is usually diminished. In this kind of situation it can be helpful to select an approximation method that has the property that, if $\pmb { x }$ is any point of $[ a , b ]$ that is separated from the discontinuity by a certain number of knots, then the value of the spline at $x$ is independent of the discontinuity. The following interpolation method is suitable.

We choose $( k + 1 )$ different points in each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] \}$ $j = 0 , ( k + 1 ) , 2 ( k + 1 ) , \ldots , r ( k + 1 ) \} _ { \mathrm { { z } } }$ where $r$ is the greatest integer that satisfies the bound

$$
r ( k + 1 ) \leqslant n - 1 ,
$$

and,if the bound holds as a strict inequality,we also choose $[ n - 1 -$ $r ( k + 1 ) ]$ different points in $[ \xi _ { n - 1 } , \xi _ { n } ] ,$ ，where the last of the points is greater than $\xi _ { n - 1 }$ . Thus the total number of points is equal to $( n + k )$ ， which is the dimension of $\mathcal { S } .$ Therefore,because the conditions of Theorem 19.4 are satisfied, we may define $\pmb { s }$ to be the element of $\mathcal { S }$ that interpolates $f$ at the points. The main property of this procedure is that, on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , ( k + 1 ) , 2 ( k + 1 ) , \ldots , r ( k + 1 ) \} ,$ the number of interpolation points is such that the polynomial segment $\{ s ( x ) ; \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } \}$ is defined completely by the values of $f$ in the interval. Therefore there are no degrees of freedom that allow the form of $\pmb { s }$ in $[ a , \xi _ { j } )$ to be related to the form of $\pmb { s }$ in $( \xi _ { j + 1 } , b ]$ .Hence,if a perturbation to $\pmb { s }$ is generated by a discontinuity in $f ,$ then the effect of the perturbation cannot pass through any of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , ( k + 1 ) \}$ ， $2 ( k + 1 ) , \ldots , r ( k + 1 ) \}$ Thus,if $x$ is any point in $[ a , b ] ,$ ，then the value $\pmb { s } ( \pmb { x } )$ depends only on the form of $f$ in the interval $[ \operatorname* { m a x } \left( \xi _ { q - k } , a \right) ,$ ， min $( \pmb { \xi } _ { q + k + 1 } , \pmb { b } ) ]$ , where the integer $q$ is such that $x$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$

One reason for mentioning this interpolation procedure is that it can be used to derive bounds of the form (20.15), in a way that is more direct than the inductive proof of Theorem 20.3. The bounds are given in the following theorem.

# Theorem 20.4

Given the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ，let $( n + k )$ interpolation points be chosen in the way that has just been described,and let $L$ be the operator from $\mathcal { C } [ a , b ]$ to $\mathcal { S }$ such that, for any $f$ in $\ell [ a , b ] ,$ ,the function $L f$ is the spline that is defined by the interpolation conditions. If $f$ is in the space $\mathcal { C } ^ { ( j ) } [ a , b ] ,$ ，where $j$ is any integer in the range $[ 1 , k + 1 ]$ ，then the inequality

$$
d ^ { * } ( { \mathcal { S } } , f ) { \leqslant } \frac { 1 } { j ! } { \| L \| } _ { \infty } ( k + 1 ) ^ { j } h ^ { j } \| f ^ { ( j ) } \| _ { \infty }
$$

is satisfied.

Proof. It is sufficient to prove that $\| f - s \| _ { \infty }$ is bounded above by the right-hand side of expression (20.26), where $\pmb { s }$ is the spline $L f .$ We let $\pmb { \zeta }$ be any fixed point in $[ a , b ] ,$ , and we let $\phi$ be the polynomial

$$
\phi \left( x \right) = f ( \zeta ) + \frac { \left( x - \zeta \right) } { 1 ! } f ^ { \prime } ( \zeta ) + \ldots + \frac { \left( x - \zeta \right) ^ { j - 1 } } { ( j - 1 ) ! } f ^ { ( j - 1 ) } ( \zeta ) ,
$$

Because $\phi$ is in ${ \mathcal { S } } ,$ the spline $L \phi$ is the polynomial $\phi$ .Further, $\phi ( \zeta )$ is equal to $f ( \zeta )$ .Hence the error at $\pmb { \zeta }$ of the approximation $s = L f$ to $f$ has the value

$$
\begin{array} { r } { f ( \zeta ) - s ( \zeta ) = \phi ( \zeta ) - ( L f ) ( \zeta ) } \\ { = ( L \{ \phi - f \} ) ( \zeta ) . } \end{array}
$$

It is important to notice that the function $( \phi - f )$ takes very small values when the variable is near $\zeta ,$ and to recall that $( L \{ \phi - f \} ) ( \zeta )$ depends only on the form of $( \phi - f )$ in the interval

$$
[ a _ { \xi } , b _ { \zeta } ] = [ \operatorname* { m a x } \ ( \xi _ { q - k } , a ) , \operatorname* { m i n } \ ( \xi _ { q + k + 1 } , b ) ] ,
$$

where the integer $q$ is such that $\pmb { \zeta }$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$ . In order to

make use of these remarks, we note that the mean value theorem gives the bound

$$
{ \big | } f ( x ) - \phi ( x ) { \big | } \leqslant { \frac { 1 } { j ! } } { \big | } x - \zeta { \big | } ^ { j } \| f ^ { ( j ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b .
$$

Therefore, if $\psi _ { \zeta }$ is the function in ${ \mathcal { C } } [ a , b ]$ that satisfes the equation

$$
\psi _ { \zeta } ( x ) = \phi ( x ) - f ( x ) , \qquad a _ { \zeta } \leqslant x \leqslant b _ { \zeta } ,
$$

and that is constant on each of the intervals $[ a , a _ { \zeta } ]$ and $[ b _ { \zeta } , b ] ,$ then the inequality

$$
\begin{array} { l } { \displaystyle \| \psi _ { \zeta } \| _ { \infty } \leqslant \frac { 1 } { j ! } \operatorname* { m a x } \left[ \left| \zeta - a _ { \zeta } \right| ^ { j } , \left| b _ { \zeta } - \zeta \right| ^ { j } \right] \| f ^ { ( j ) } \| _ { \infty } } \\ { \displaystyle \leqslant \frac { 1 } { j ! } \operatorname* { m a x } \left[ \left| \xi _ { q + 1 } - a _ { \zeta } \right| ^ { j } , \left| b _ { \zeta } - \xi _ { q } \right| ^ { j } \right] \| f ^ { ( j ) } \| _ { \infty } } \\ { \displaystyle \leqslant \frac { 1 } { j ! } \left( k + 1 \right) ^ { j } h ^ { i } \left\| f ^ { ( j ) } \right\| _ { \infty } } \end{array}
$$

holds,where the last line depends on the definitions (2O.3) and (20.29). Because expressions (20.31) and (20.32) imply the bound

$$
\begin{array} { r l r } {  { \big | ( L \{ \phi - f \} ) ( \zeta ) \big | = \big | ( L \psi _ { \zeta } ) ( \zeta ) \big | } } \\ & { } & { \leqslant \| L \| _ { \infty } \| \psi _ { \zeta } \| _ { \infty } } \\ & { } & { \leqslant \displaystyle \frac { 1 } { j ! } \| L \| _ { \infty } ( k + 1 ) ^ { j } h ^ { j } \| f ^ { ( j ) } \| _ { \infty } , } \end{array}
$$

and because the right-hand side of this inequality is independent of $\zeta ,$ it follows from equation (20.28) that the theorem is true.□

This theorem is less useful than Theorem 20.3,because the interpolation procedure is such that there is no upper bound on $\| L \| _ { \infty }$ that is independent of the knot positions $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ .Really the main value of the theorem is to show that it is possible to deduce bounds of the form (20.26) from equation (20.28),by letting $\phi$ be the function (20.27), provided that the operator $L$ has the property that, for any $\pmb { \zeta }$ in $[ a , b ]$ ,the function value $( L f ) ( \zeta )$ is independent of $f ( x )$ if $\left| x - \zeta \right|$ exceeds a constant multiple of $h$ .This technique is used again in the next section.

# 20.4 Cubic splines with constant knot spacing

There are several methods for calculating spline approximations with good localization properties that do not make use of interpolation conditions. A procedure is developed in this section for the special case when $k = 3$ and the knots satisfy condition (20.2) and the equation

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = - 3 , - 2 , \ldots , n + 3 .
$$

It shows another technique for spline approximation that obtains high order accuracy when $f$ is sufficiently differentiable.We assume that the function to be approximated is defined on the interval $[ a - 2 h , b + 2 h ] ,$ Because the $\pmb { B }$ -spline $\{ N _ { p } ^ { 3 } ( x ) ; - \infty < x < \infty \}$ is symmetric about the point $x = \xi _ { p + 2 }$ ,we let $\pmb { s _ { 0 } }$ ${ \bf \Gamma } _ { 0 } \left( = L _ { 0 } f , \right.$ ，say) be the spline function

$$
s _ { 0 } ( x ) = \sum _ { p = - 3 } ^ { n - 1 } f ( \xi _ { p + 2 } ) N _ { p } ^ { 3 } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

which is similar to the one that is used to prove Theorem 20.2.In order to apply the idea that is used to prove Theorem 20.4, we seek the greatest value of $j$ such that the equation

$$
\phi = L _ { 0 } \phi , \qquad \phi \in { \mathcal { P } } _ { j - 1 } ,
$$

is satisfied.

Because expression (19.18) implies the equations $N _ { p } ^ { 3 } ( \xi _ { p + 1 } ) =$ $\begin{array} { r } { N _ { p } ^ { 3 } \left( \xi _ { p + 3 } \right) = \frac { 1 } { 6 } } \end{array}$ and $\begin{array} { r } { N _ { p } ^ { 3 } \left( \xi _ { p + 2 } \right) = \frac { 2 } { 3 } , } \end{array}$ ,the spline (20.35) takes the values

$$
\begin{array} { r } { s _ { 0 } ( \xi _ { i } ) = \frac { 1 } { 6 } f ( \xi _ { i - 1 } ) + \frac { 2 } { 3 } f ( \xi _ { i } ) + \frac { 1 } { 6 } f ( \xi _ { i + 1 } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

at the knots.Hence, if $f$ is in the space $\mathcal { P } _ { 1 }$ ,then ${ \pmb s } _ { 0 } ( { \pmb \xi } _ { i } )$ is equal to $f ( \xi _ { i } )$ ,but, if $f$ is a quadratic function, then the error

$$
\begin{array} { r } { f ( \xi _ { i } ) - s _ { 0 } ( \xi _ { i } ) = - \frac { 1 } { 6 } h ^ { 2 } f ^ { \prime \prime } ( \xi _ { i } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

occurs. Similarly, the spline approximation

$$
s _ { 1 } ( x ) = \frac { 1 } { 2 } \sum _ { p = - 3 } ^ { n - 1 } \left[ f ( \xi _ { p + 1 } ) + f ( \xi _ { p + 3 } ) \right] N _ { p } ^ { 3 } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

has the value

$$
\begin{array} { r } { s _ { 1 } ( \xi _ { i } ) = \frac { 1 } { 1 2 } [ f ( \xi _ { i - 2 } ) + 4 f ( \xi _ { i - 1 } ) + 2 f ( \xi _ { i } ) + 4 f ( \xi _ { i + 1 } ) + f ( \xi _ { i + 2 } ) ] , } \end{array}
$$

which implies the error

$$
\begin{array} { r } { f ( \xi _ { i } ) - s _ { 1 } ( \xi _ { i } ) = - \frac { 2 } { 3 } h ^ { 2 } f ^ { \prime \prime } ( \xi _ { i } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

when $f$ is in $\mathcal { P } _ { 2 }$ . The spline approximation that is studied in this section is obtained by forming the linear combination of $\pmb { s _ { 0 } }$ and $\pmb { S } _ { 1 }$ that eliminates the error terms (20.38) and (20.41).Hence it is the function

$$
\begin{array} { r } { s \left( x \right) = \displaystyle \sum _ { p = - 3 } ^ { n - 1 } \left[ - \frac { 1 } { 6 } f ( \xi _ { p + 1 } ) + \frac { 4 } { 3 } f ( \xi _ { p + 2 } ) - \frac { 1 } { 6 } f ( \xi _ { p + 3 } ) \right] N _ { p } ^ { 3 } \left( x \right) , } \\ { a \leqslant x \leqslant b . } \end{array}
$$

Because equations (20.38) and (20.41) are valid when $f$ is any cubic polynomial, the conditions

$$
f ( \xi _ { i } ) = s ( \xi _ { i } ) , \qquad i = 0 , 1 , \ldots , n , \qquad f \in \mathcal { P } _ { 3 } ,
$$

are obtained. Further,equations (19.18)and (20.42） imply that, for $i = 0 , 1 , \ldots , n$ ,the derivative $s ^ { \prime } ( \xi _ { i } )$ has the value

$$
s ^ { \prime } ( \xi _ { i } ) = \frac { 1 } { 1 2 h } \big [ f ( \xi _ { i - 2 } ) - 8 f ( \xi _ { i - 1 } ) + 8 f ( \xi _ { i + 1 } ) - f ( \xi _ { i + 2 } ) \big ] ,
$$

which is equal to $f ^ { \prime } ( \pmb { \xi } _ { i } )$ when $f$ is in $\mathcal { P } _ { 3 }$ . Hence the spline approximation (20.42) is equal to $f ,$ when $f$ is any cubic polynomial.

Therefore, if $f$ is in $\mathcal { C } ^ { ( 4 ) } [ a , b ] ,$ . we may apply the method of proof of Theorem 20.4 to obtain a bound on $d ^ { * } ( \mathcal { S } , f )$ in terms of $\| f ^ { ( 4 ) } \| _ { \infty }$ . To begin this analysis the definition of $f$ is extended to the interval $[ a - 2 h , b + 2 h ]$ in a way that does not increase $\| f ^ { ( 4 ) } \| _ { \infty }$ ，and an operator $L _ { i }$ ，from $\mathscr { C } [ a - 2 h , b + 2 h ]$ to ${ \mathcal { S } } ,$ is defined by the equation

$$
\begin{array} { r l } { { } } & { { \displaystyle { L f } = \sum _ { p = - 3 } ^ { n - 1 } \big [ - \frac { 1 } { 6 } f ( \xi _ { p + 1 } ) + \frac { 4 } { 3 } f ( \xi _ { p + 2 } ) . - \frac { 1 } { 6 } f ( \xi _ { p + 3 } ) \big ] N _ { p } ^ { 3 } } } \\ { { } } & { { = \displaystyle { \sum _ { p = - 3 } ^ { n - 1 } \lambda _ { p } ( f ) N _ { p } ^ { 3 } } , } } \end{array}
$$

say. We let $j = 4$ in expression (20.27),and we note that equation (20.28) is satisfied. Therefore we require an upper bound on $\left| ( L \{ \phi - f \} ) ( \zeta ) \right|$ that is independent of $\zeta .$

Equation (20.45), the properties of $\pmb { B }$ -splines and Theorem 20.1 imply the condition

$$
\begin{array} { r l } { | ( L \{ \phi - f \} ) ( \zeta ) | = \biggr | \displaystyle \sum _ { p = - 3 } ^ { n - 1 } \lambda _ { p } ( \phi - f ) N _ { p } ^ { 3 } ( \zeta ) \biggr | } & { } \\ { = \biggr | \displaystyle \sum _ { p = - q - 3 } ^ { q } \lambda _ { p } ( \phi - f ) N _ { p } ^ { 3 } ( \zeta ) \biggr | } & { } \\ { \leqslant \displaystyle \operatorname* { m a x } _ { q = 3 \in p \in q } \left| \lambda _ { p } ( \phi - f ) \right| \displaystyle \sum _ { p = - q - 3 } ^ { q } \left| N _ { p } ^ { 3 } ( \zeta ) \right| } \\ { = \displaystyle \operatorname* { m a x } _ { q = 3 \in p \in q } \left| \lambda _ { p } ( \phi - f ) \right| , } \end{array}
$$

where $\pmb q$ is still an integer such that $\zeta$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$ . There is no need to introduce a function that corresponds to the function $\psi _ { \zeta }$ in the proof of Theorem 20.4, because expressions (20.45) and (20.30) give the bound

$$
\begin{array} { c l } { { \displaystyle \left| \lambda _ { p } ( \phi - f ) \right| \leqslant \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { p + 1 } ) \big | + \frac { 4 } { 3 } \big | ( f - \phi ) ( \xi _ { p + 2 } ) \big | + \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { p + 3 } ) \big | } } \\ { { \displaystyle \leqslant \frac { \| f ^ { ( 4 ) } \| _ { \infty } } { 1 4 4 } [ \big | \xi _ { p + 1 } - \zeta \big | ^ { 4 } + 8 \big | \xi _ { p + 2 } - \zeta \big | ^ { 4 } + \big | \xi _ { p + 3 } - \zeta \big | ^ { 4 } ] . } } \end{array}
$$

When $p$ is in the interval $[ q - 3 , q ] ,$ ，then $\zeta$ is in the interval $[ \xi _ { p } , \xi _ { p + 4 } ]$ In

this case the greatest possible value of expression (20.47) occurs when $\left| \xi _ { p + 2 } - \zeta \right| = 2 h .$ It follows from equation (20.28)and condition (20.46) that the inequality

$$
| f ( \zeta ) - s ( \zeta ) | \leqslant \frac { 3 5 } { 2 4 } h ^ { 4 } \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant \zeta \leqslant b ,
$$

is satisfied, which is a slight improvement on the one that is obtained by setting $k = 3$ and $j = 4$ in Theorem 20.3.

The factor $\frac { 3 5 } { 2 4 }$ in condition (20.48) is much larger than necessary. Most of the loss of precision comes from the third line of expression (20.46), but some of the loss can be avoided by a different choice of $\phi$ For example, we let $\phi$ be the cubic polynomial that interpolates the function values $f ( \xi _ { q - 1 } ) , f ( \xi _ { q } ) , f ( \xi _ { q + 1 } )$ and $f ( \xi _ { q + 2 } )$ . In this case Theorem 4.2 gives the inequality

$$
\begin{array} { r } { \vert f ( x ) - \phi \left( x \right) \vert \leqslant \frac { 1 } { 2 4 } \bigg \vert \underset { j = q - 1 } { \overset { q + 2 } { \prod } } \left( x - \xi _ { j } \right) \bigg \vert \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b , } \end{array}
$$

instead of expression (20.30). It follows that, instead of equation (20.28), the bound

$$
\begin{array} { r } { \left| f ( \zeta ) - s ( \zeta ) \right| \leqslant \left| \phi ( \zeta ) - ( L f ) ( \zeta ) \right| + \left| f ( \zeta ) - \phi ( \zeta ) \right| } \\ { \leqslant \left| ( L \{ \phi - f \} ) ( \zeta ) \right| + \frac { 3 } { 1 2 8 } h ^ { 4 } \left\| f ^ { ( 4 ) } \right\| _ { \infty } } \end{array}
$$

is satisfied, where the last line depends on the fact that $\pmb { \zeta }$ is in $[ \xi _ { q } , \xi _ { q + 1 } ]$ The relation (2O.46) is still valid, but there are substantial changes to expression (20.47) because the terms $\{ ( f - \phi ) ( \xi _ { j } ) ; q - 1 \leqslant j \leqslant q + 2 \}$ are all zero.Hence,when $p = q - 3$ , the definition of $\lambda _ { p }$ and inequality (20.49) imply the bound

$$
\begin{array} { r l } & { \left| \lambda _ { p } ( \phi - f ) \right| = \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { q - 2 } ) \big | } \\ & { \qquad \leqslant \frac { 1 } { 6 } h ^ { 4 } \left\| f ^ { ( 4 ) } \right\| _ { \infty } . } \end{array}
$$

This bound also holds when $\pmb { p } = \pmb { q }$ Similarly, if $p$ is equal to $q - 2$ or $q - 1$ ， then $\lambda _ { p } ( \phi - f )$ is zero.It follows from expressions (20.46) and (20.50) that the inequality

$$
\begin{array} { r } { \big | f ( \zeta ) - s ( \zeta ) \big | \leqslant \frac { 7 3 } { 3 8 4 } h ^ { 4 } \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant \zeta \leqslant b , } \end{array}
$$

is obtained, which is sharper than condition (20.48).

By being more ingenious in the choice of $\phi$ ，or by giving detailed attention to the third line of expression (20.46), it is possible to make a further reduction in the constant of inequality (20.52). However,by using a different procedure, the least possible value of this constant is found in Section 22.4.

# 20 Exercises

20.1 Let $k = 2$ ，let $f$ be a quadratic polynomial, and let $\pmb { s }$ be the quadratic spline (20.11),where $\{ \xi _ { j } = j h ; j = - 2 , - 1 , \ldots , n + 2 \}$ and $\{ x _ { p } = \frac { 1 } { 2 } ( \xi _ { p } + \xi _ { p + 3 } ) ; \ p = - 2 , \ - 1 , \ldots , n - 1 \}$ . Show that for every point $\pmb { x }$ in the interval $[ \xi _ { 0 } , \xi _ { n } ] ,$ ，the error $[ f ( { \pmb x } ) - { \pmb s } ( { \pmb x } ) ]$ is equal to the constant $- { \textstyle \frac { 1 } { 8 } } h ^ { 2 } f ^ { \prime \prime } ( x )$

20.2 Let $k$ be a fixed positive integer,and let $\beta$ be a constant such that the inequality

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant \omega \left( \beta h \right)
$$

holds for all functions $f$ in ${ \mathcal { C } } [ a , b ]$ and for all spaces of splines of degree $k$ whose knots satisfy the conditions (20.2),where $\pmb { \omega }$ is the modulus continuity of $f ,$ and where $^ { h }$ has the value (20.3). Prove that $\beta$ is not less than one.Hence Theorem 2O.2 gives the optimal value of $\beta$ when $k = 1$

20.3Prove that, if the bound

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant c h ^ { j } \| f ^ { ( j ) } \| _ { \infty } , \quad f \in { \mathcal { C } } ^ { ( j ) } [ a , b ] ,
$$

is satisfied for all spaces $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ whose knots satisfy the condition

$$
\xi _ { i } - \xi _ { i - 1 } \geqslant \mu h , \qquad i = 1 , 2 , \ldots n ,
$$

where $\pmb { \mu }$ is a positive constant that is less than one, and where $h$ is the maximum knot spacing (20.3), then the inequality

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c \left( h / [ 1 - \mu ] \right) ^ { j } \| f ^ { ( j ) } \| _ { \infty }
$$

holds when there are no restrictions on the positions of the knots of $\mathcal { S }$

20.4 Let $f$ be a quartic polynomial, and let $\pmb { s }$ be the cubic spline in the space $\mathcal { S } ( 3 , 0 , 1 , 2 , 3 , 4 , 5 )$ that satisfies the interpolation conditions $\{ s ( { x } _ { i } ) = f ( { x } _ { i } )$ ； $i = 1 , 2 , 3 , \ldots , 8 \}$ ， where the interpolation points have the values $\begin{array} { r } { \{ x _ { i } = ( i - 1 ) / 3 , i = 1 , 2 , 3 , 4 ; x _ { i } = ( i + 7 ) / 3 , } \end{array}$ ， $i = 5 , 6 , 7 , 8 \}$ . Show that the error $[ f ( 2 \frac { 1 } { 2 } ) - s ( 2 \frac { 1 } { 2 } ) ]$ is equal to ${ \frac { 1 7 9 } { 1 0 3 6 8 } } f ^ { ( 4 ) } ( x )$ ndattdeii $\pmb { s }$ have the values ${ \textstyle \frac { 2 8 } { 2 7 } } f ^ { ( 4 ) } ( x ) , { \textstyle \frac { 2 6 } { 2 7 } } f ^ { ( 4 ) } ( x ) , { \textstyle \frac { 2 6 } { 2 7 } } f ^ { ( 4 ) } ( x )$ and ${ \textstyle \frac { 2 8 } { 2 7 } } f ^ { ( 4 ) } ( x )$

20.5 Obtain a bound on $\| f - s \| _ { \infty }$ that is stronger than condition (20.52) by substituting the conditions on $\begin{array} { r } { \{ \vert \lambda _ { p } ( \phi - f ) \vert ; q - 3 \leqslant p \leqslant q \} , } \end{array}$ that are given immediately before inequality (20.52), into the second line of expression (20.46).

20.6 Let the knots $\{ \xi _ { j } \}$ have the values (20.34),and let ${ \pmb S } _ { \pmb { \alpha } }$ be the cubic spline approximation

$$
s _ { \alpha } ( x ) = \sum _ { p = - 3 } ^ { n - 1 } \left[ f ( \xi _ { p + 2 } ) + \alpha f ^ { \prime \prime } ( \xi _ { p + 2 } ) \right] N _ { p } ^ { 3 } \left( x \right) , \qquad a \leqslant x \leqslant b ,
$$

to a function $f$ in $\mathcal { C } ^ { ( 4 ) } [ a - h , b + h ]$ .Calculate the value of $\pmb { \alpha }$ such that ${ \pmb S } _ { { \pmb \alpha } }$ is equal to $f$ when $f$ is a cubic polynomial. Hence find a bound on the error $\{ | f ( x ) - s ( x ) | ; a \leqslant x \leqslant b \}$ of the form (20.48).

).7 Investigate whether the inequality of Exercise 20.2 is valid when $k = 2$ and $\beta = 1$

Improve the bound of Theorem 20.4 by replacing the function (20.27) by a polynomial of degree $( j - 1 )$ that interpolates $f$ at suitable points of the interval (20.29).

20.9 Prove that the Chebyshev polynomial $T _ { k }$ maximizes the derivative $\{ \| p ^ { \prime } \| _ { \infty } ; p \in \mathcal { P } _ { k } \}$ subject to the condition $\| p \| _ { \infty } \leqslant 1$ , where the $\infty$ -norm applies to the interval [-1,1]. Hence deduce that the bound

$$
\operatorname* { m a x } _ { \xi _ { i - 1 } \le x \le \xi _ { i } } \big | p ( x ) \big | \geqslant \frac { ( \xi _ { i } - \xi _ { i - 1 } ) } { 2 k ^ { 2 } } \operatorname* { m a x } _ { \xi _ { i - 1 } \le x \le \xi _ { i } } \big | p ^ { \prime } ( x ) \big | , \qquad p \in \mathcal { P } _ { k } ,
$$

is satisfied. This condition is required for the next exercise.

20.10 Let $f$ be a function in $\mathcal { C } ^ { ( j ) } [ a , b ]$ ，and let $\pmb { s }$ be a spline in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the condition

$$
\| \boldsymbol { f } - \boldsymbol { s } \| _ { \infty } \leqslant c h ^ { j } \| \boldsymbol { f } ^ { ( j ) } \| _ { \infty } ,
$$

where $k \geqslant j - 1 \geqslant 1$ ，where $^ c$ is a constant, and where $h$ is the maximum interval between knots. Prove that $ \| f ^ { \prime } - s ^ { \prime } \| _ { \infty }$ is bounded above by a constant multiple of the expression $h ^ { j } \parallel f ^ { ( j ) } \parallel _ { \infty } / \eta ,$ where $\pmb { \eta }$ is the smallest of the numbers $\{ \xi _ { i } - \xi _ { i - 1 } ; i = 1 , 2 , \ldots , n \}$ Note that it is helpful to use Exercise 20.9 to bound the difference $\left| f ^ { \prime } ( \zeta ) - s ^ { \prime } ( \zeta ) \right| = \left| \phi ^ { \prime } ( \zeta ) - s ^ { \prime } ( \zeta ) \right| ,$ where $\pmb { \zeta }$ is any point of the interval $[ \xi _ { i - 1 } , \xi _ { i } ] ,$ ,and where $\phi$ is the Taylor series approximation to $f$ at $\pmb { \zeta }$ of degree $( j - 1 )$

# Knot positions and the calculation of spline approximations

# 21.1 The distribution of knots at a singularity

A strong advantage of letting the knots of a spline approximation have the equally spaced values

$$
\xi _ { j } = \xi _ { 0 } + \left( j / n \right) ( \xi _ { n } - \xi _ { 0 } ) , \qquad j = 0 , 1 , \ldots , n ,
$$

is that,for any $x$ in $[ a , b ] ,$ ,one can find by one division and one integer part operation an index $j$ such that the condition $\xi _ { j } \leqslant x \leqslant \xi _ { j + 1 }$ is satisfied. It is often possible, however, to reduce greatly the total number of knots by giving up the condition that the spacing between knots is constant. In order to demonstrate this point, we consider the approximation of the function $\{ f ( x ) = x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ by the piecewise linear function $\pmb { s }$ from the space $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ (where ${ \xi _ { 0 } } = 0$ and $\xi _ { n } = 1$ ） that is defined by the interpolation conditions

$$
s ( \xi _ { i } ) = f ( \xi _ { i } ) , \qquad i = 0 , 1 , . . . , n .
$$

We consider the number of knots that are needed to provide the accuracy

$$
\| f - s \| _ { \infty } \leqslant \varepsilon ,
$$

where $\varepsilon$ is a small positive constant.

In each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$ , the error function satisfies the equation

$$
f ( x ) - s \left( x \right) = x ^ { \frac { 1 } { 2 } } - \frac { \xi _ { j } ^ { \frac { 1 } { 2 } } \left( \xi _ { j + 1 } - x \right) + \xi _ { j + 1 } ^ { \frac { 1 } { 2 } } \left( x - \xi _ { j } \right) } { \xi _ { j + 1 } - \xi _ { j } } , \qquad \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } .
$$

Therefore the maximum error on $[ \xi _ { j } , \xi _ { j + 1 } ]$ occurs at the point $x =$ $\begin{array} { r } { \frac { 1 } { 4 } ( \xi _ { j } ^ { \frac { 1 } { 2 } } + \xi _ { j + 1 } ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \end{array}$ . Here the modulus of the error function has the value

$$
\begin{array} { r } { \frac { 1 } { 4 } \big ( \xi _ { j + 1 } ^ { \frac { 1 } { 3 } } - \xi _ { j } ^ { \frac { 1 } { 2 } } \big ) ^ { 2 } / ( \xi _ { j } ^ { \frac { 1 } { 2 } } + \xi _ { j + 1 } ^ { \frac { 1 } { 3 } } ) . } \end{array}
$$

If the knots are equally spaced, then this expression is greatest when $j = 0$

Hence $\| f - s \| _ { \infty }$ is equal to ${ \frac { 1 } { 4 } } n ^ { - { \frac { 1 } { 2 } } }$ . It follows that, in order to achieve the bound (21.3), the integer $_ n$ must not be less than $1 / { ( 4 \varepsilon ) } ^ { 2 }$

If there are no restrictions on the positions of the knots, however, then the values

$$
\xi _ { j } = ( j / n ) ^ { 4 } , \qquad j = 0 , 1 , \ldots , n ,
$$

are particularly suitable. In this case expression (21.5) gives the identity

$$
\operatorname* { m a x } _ { \xi _ { i } \le x \le \xi _ { i + 1 } } \big | f ( x ) - s ( x ) \big | = \frac { 1 } { 4 n ^ { 2 } } \frac { 4 j ^ { 2 } + 4 j + 1 } { 2 j ^ { 2 } + 2 j + 1 } .
$$

Because the right-hand side is bounded above by $1 / 2 { n } ^ { 2 }$ , the accuracy (21.3) is achieved if $_ n$ is not less than $( 2 \varepsilon ) ^ { - \frac { 1 } { 2 } }$ , which is a large improvement on the previous bound. For example, if $\varepsilon = 1 0 ^ { - 4 }$ ，then $n \geq 2 5 \times { 1 0 } ^ { 6 }$ when the knots are equally spaced,but the distribution (21.6) allows $n = 7 1$ . The reduction in the number of knots that can be made by adapting the knot positions to the form of $f$ is usually even greater when $\pmb { s }$ is a quadratic or a cubic spline.

It is interesting to compare the number of knots that are needed to approximate the functions $\{ f ( x ) = x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ and $\{ f ( x ) = 2 x ^ { 2 }$ ； $0 \leqslant x \leqslant$ 1} to accuracy $\pmb \varepsilon$ by a linear spline.When $f$ is a quadratic polynomial it is best to use a constant knot spacing.Hence in both cases the fewest number of knots that is necessary to achieve the required accuracy is about $( 2 \varepsilon ) ^ { - { \frac { 1 } { 2 } } }$ , even though one function has a singularity and the other one is very smooth. It happens often that singularities in $f$ do not increase greatly the total number of knots, provided that careful attention is given to the knot positions.

One kind of singularity that can be fitted easily is a derivative discontinuity. We consider the case when $f ^ { ( q ) }$ is discontinuous at $\bar { x }$ where $q$ is an integer in the interval $[ 1 , k ]$ ,and where $\bar { x }$ is an interior point of the range $[ a , b ]$ .When $q = k .$ , then placing one of the knots $\left\{ \xi _ { i } ; i = 1 , 2 , \ldots , \right.$ $n - 1 \}$ at $\bar { x }$ allows the discontinuity to be fitted exactly， because the function

$$
\sigma ( x ) = ( x - \bar { x } ) _ { + } ^ { q } , \qquad a \leqslant x \leqslant b ,
$$

is in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . When $q$ is less than $k$ ,then it is suitable to let $( k + 1 - q )$ of the knots $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ be close to $\bar { x } ,$ ,because the following theorem shows that in this way the function (21.8) can be approximated arbitrarily closely by an element of ${ \mathcal { S } } .$

# Theorem 21.1

Let $q$ be an integer in $[ 1 , k - 1 ]$ ,and let $\sigma$ be the function (21.8), where $\bar { x }$ is any fixed point in $( a , b )$ .For any $\varepsilon > 0$ , there exists a spline $\pmb { s }$ in

$\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the inequality

$$
\| { \pmb \sigma } - { \pmb s } \| _ { \infty } \leqslant { \pmb \varepsilon } ,
$$

provided that the condition

$$
\left| { \bar { x } } - \xi _ { j } \right| \leqslant \varepsilon / [ q \ ( b - a ) ^ { q - 1 } ]
$$

holds for at least $( k + 1 - q )$ of the knots $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$

Proof. We let the knots $\{ \xi _ { i } ; j = p , p + 1 , \ldots , p + k - q \}$ satisfy condition (21.10),and we let $\pmb { s }$ be the function

$$
s ( x ) = \frac { ( - 1 ) ^ { k - q } ( k - q ) ! q ! } { k ! } \sum _ { { j = p \atop i = p } } ^ { p + k - q } \frac { ( x - \xi _ { j } ) _ { + } ^ { k } } { \underset { i = p } { \prod _ { j = k + 1 } ^ { p + k - q } } ( \xi _ { j } - \xi _ { i } ) } , \qquad a \leqslant x \leqslant b ,
$$

which is in $\mathcal { S } .$ Equation (5.2) shows that,for any fixed $x , s ( x )$ is the divided difference $g [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { p + k - q } ] _ { : }$ where $\pmb { g }$ is the function

$$
g ( \theta ) = ( - 1 ) ^ { k - q } [ ( k - q ) ! q ! / k ! ] ( x - \theta ) _ { + } ^ { k } , \qquad a \leqslant \theta \leqslant b .
$$

It follows from Theorem 5.1 that $s ( x )$ has the value

$$
\begin{array} { c } { { s ( x ) = \left[ 1 / ( k - q ) ! \right] g ^ { ( k - q ) } ( \xi ) } } \\ { { = ( x - \xi ) _ { + } ^ { q } , } } \end{array}
$$

where $\xi$ is in the interval $[ \xi _ { p } , \xi _ { p + k - q } ]$ and depends on $x$ .The remainder of the proof depends only on equations (21.8) and (21.13),and the fact that $\xi$ satisfies the condition

$$
{ \left| { \bar { x } - \xi } \right| } \leqslant \varepsilon / [ q \left( { b - a } \right) ^ { q - 1 } ] .
$$

If $q = 1$ ,then equations (21.8) and (21.13) imply the inequality

$$
\left| \sigma ( x ) - s ( x ) \right| \leqslant \left| { \bar { x } } - \xi \right| .
$$

When $q > 1$ ，the mean value theorem is applied to the function $\{ ( x - \theta ) _ { + } ^ { q }$ ； $a \leqslant \theta \leqslant b \}$ to deduce the equation

$$
\left| \sigma ( x ) - s ( x ) \right| = \left| { \bar { x } } - \xi \right| q ( x - \zeta ) _ { + } ^ { q - 1 } ,
$$

where $\pmb { \zeta }$ is between $\bar { x }$ and $\xi .$ The term $( x - \zeta ) _ { + } ^ { q - 1 }$ is bounded above by $( b - a ) ^ { q - 1 }$ . It follows from expressions (21.14), (21.15) and (21.16) that $\left| \sigma ( { \pmb x } ) - s ( { \pmb x } ) \right|$ does not exceed $\pmb { \varepsilon }$ .Because this statement holds for all $x$ in $[ a , b ] .$ ,the theorem is proved.□

In practice,instead of choosing the knots $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ in such a way that the function (21.8) can be approximated to high accuracy by an element of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ , it is more convenient to let the function (21.8) be in the set of.approximating functions. Therefore we extend the definition of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ in order to allow repeats in the set $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ . If the conditions

$$
a = \xi _ { 0 } \leqslant \xi _ { 1 } \leqslant \xi _ { 2 } \leqslant . ~ . ~ \leqslant \xi _ { n } = b
$$

hold,and if at least one of the inequalities is satisfied as an equation, then the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ is defined as follows. It is the space that is spanned by the functions $\{ x ^ { i } , a \leqslant x \leqslant b$ ； $i = 0 , 1 , \ldots , k \}$ and $\{ ( { \pmb x } - { \pmb \xi } _ { j } ) _ { + } ^ { i } .$ ， $a \leqslant x \leqslant b ; k + 1 - q ( j ) \leqslant i \leqslant k ; j = 1 , 2 , \ldots , n - 1 \}$ ,where $q ( j )$ is the minimum of $k$ and the number of times that the number $\xi _ { j }$ Occurs in the set $\{ \xi _ { p } ; p = 1 , 2 , \ldots , n - 1 \}$ .Most of the theory that is given in Chapters 19 and 20 applies to the extended definition of $\mathcal { S }$

# 21.2 Interpolation for general knots

In order that the results of the previous section are useful, there is a need for an algorithm that calculates an approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ]$ ,without unnecessary loss of accuracy when the distribution of knots is highly irregular. Interpolation methods are often suitable,provided that the interpolation points $\{ x _ { i }$ ； $i = 1 , 2 , \ldots , n + k \}$ are selected carefully. The conditions of Theorem 19.4 must be satisfied,and then the equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k ,
$$

define a unique element of $\mathcal { S }$ for each $f$ in $\mathcal { C } [ a , b ]$ . Thus the interpolation algorithm is a linear projection operator from ${ \mathcal { C } } [ a , b ]$ to ${ \mathcal { S } } .$ It follows from Theorem 3.1 that, if the norm of the interpolation operator is small, then the error of the calculated approximation is never much larger than necessary. Therefore we seek interpolation points that make the norm small.

If the splines are piecewise linear functions, then the norm of the interpolation procedure is one if the interpolation points are the knots. For $k \geqslant 2$ , it is usually suitable to include the values

$$
x _ { i } = \left( \xi _ { i - k } + \xi _ { i - k + 1 } + . . . + \xi _ { i - 1 } \right) / k , \qquad i = k , k + 1 , \ldots , n + 1 .
$$

The following theorem makes this statement definite in the case when $k = 2$ . We find later, however, that, if the interpolation points are specified before the knots are chosen, then it may not be possible to achieve a small norm.

# Theorem 21.2

For any $f$ in ${ \mathcal { C } } [ a , b ]$ ,let $s = L f$ be the quadratic spline in the space $\mathcal { S } ( 2 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions

(21.18), where the knots are in ascending order

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b ,
$$

and where the interpolation points have the values

$$
\left. { \begin{array} { l } { x _ { 1 } = \xi _ { 0 } } \\ { x _ { i } = { \frac { 1 } { 2 } } ( \xi _ { i - 2 } + \xi _ { i - 1 } ) , \qquad i = 2 , 3 , \ldots , n + 1 } \\ { x _ { n + 2 } = \xi _ { n } } \end{array} } \right\} .
$$

Then the norm of the interpolation operator satisfies the bound

$$
\| L \| _ { \infty } \leqslant 2 .
$$

Proof. Let $s _ { j }$ be the quadratic function that is equal to $\pmb { s }$ on the interval $[ \xi _ { j } , \xi _ { j + 1 } ]$ .Because $x _ { j + 2 }$ is the mid-point of this interval, the quadratic can be expressed in terms of the function values $s ( \xi _ { j } ) , f ( x _ { j + 2 } )$ and $\pmb { s } ( \pmb { \xi } _ { j + 1 } )$ Hence the equations

$$
\begin{array} { r l } & { ( \xi _ { j + 1 } - \xi _ { j } ) s _ { j } ^ { \prime } ( \xi _ { j } ) = - 3 s ( \xi _ { j } ) + 4 f ( x _ { j + 2 } ) - s ( \xi _ { j + 1 } ) } \\ & { ( \xi _ { j + 1 } - \xi _ { j } ) s _ { j } ^ { \prime } ( \xi _ { j + 1 } ) = s ( \xi _ { j } ) - 4 f ( x _ { j + 2 } ) + 3 s ( \xi _ { j + 1 } ) } \end{array} \bigg \}
$$

are satisfied. Therefore the first derivative continuity conditions $\{ s _ { j } ^ { \prime } ( \xi _ { j + 1 } ) = s _ { j + 1 } ^ { \prime } ( \xi _ { j + 1 } ) ; j = 0 , 1 , \ldots , n - 2 \}$ give the recurrence relations

$$
\begin{array} { r l } & { s ( \xi _ { j } ) h _ { j + 1 } + 3 s ( \xi _ { j + 1 } ) [ h _ { j } + h _ { j + 1 } ] + s ( \xi _ { j + 2 } ) h _ { j } } \\ & { \quad = 4 f ( x _ { j + 2 } ) h _ { j + 1 } + 4 f ( x _ { j + 3 } ) h _ { j } , \qquad j = 0 , 1 , \ldots , n - 2 , } \end{array}
$$

where $h _ { j }$ is the length of the interval $[ \xi _ { j } , \xi _ { j + 1 } ]$ Let $M = \left| s ( \xi _ { q } ) \right|$ be the largest of the numbers $\{ | s ( \xi _ { j } ) | ; j = 0 , 1 , \ldots , n \}$ If $1 \leqslant q \leqslant n - 1$ ，then expression (21.24) implies the bound

$$
3 M ( h _ { q - 1 } + h _ { q } ) \leqslant ( 4 \| f \| _ { \infty } + M ) ( h _ { q - 1 } + h _ { q } ) ,
$$

which shows that $M$ is not greater than $2 \| f \| _ { \infty }$ . Alternatively, if $q$ is 0 or $_ n$ ， then the equation $s ( \xi _ { q } ) = f ( \xi _ { q } )$ holds. It follows that the inequalities

$$
| s ( \xi _ { j } ) | \leqslant 2 \| f \| _ { \infty } , \qquad j = 0 , 1 , \ldots , n ,
$$

are obtained. Moreover,equations (21.18) and (21.21) give the conditions

$$
\begin{array} { r } { \big | s \big ( \frac 1 2 [ \xi _ { j } + \xi _ { j + 1 } ] \big ) \big | \leqslant \| f \| _ { \infty } , \qquad j = 0 , 1 , \ldots , n - 1 . } \end{array}
$$

The required bound on $\| L \| _ { \infty }$ will be derived from the last two inequalities and the fact that $\pmb { s }$ is a quadratic function on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$

In order to simplify notation, we suppose that $\xi _ { j } = 0$ and $\xi _ { j + 1 } = 1$ . Then the Lagrange interpolation formula and expressions (21.26) and (21.27)

imply that, if $\textstyle 0 \leqslant x \leqslant { \frac { 1 } { 2 } }$ , the condition

$$
{ \begin{array} { r l r } & { | s ( x ) | = \left| 2 ( x - { \frac { 1 } { 2 } } ) ( x - 1 ) s ( 0 ) + 4 ( x - x ^ { 2 } ) s ( { \frac { 1 } { 2 } } ) + 2 ( x ^ { 2 } - { \frac { 1 } { 2 } } x ) s ( 1 ) \right| } \\ & { \qquad \leqslant 4 \| f \| _ { \infty } [ ( x - { \frac { 1 } { 2 } } ) ( x - 1 ) + ( x - x ^ { 2 } ) + ( { \frac { 1 } { 2 } } x - x ^ { 2 } ) ] } \\ & { \qquad } & { = 4 \| f \| _ { \infty } [ { \frac { 1 } { 2 } } - x ^ { 2 } ] \leqslant 2 \| f \| _ { \infty } \qquad ( 2 } \end{array} }
$$

is satisfed. Similarly this condition holds when $\textstyle { \frac { 1 } { 2 } } \leqslant x \leqslant 1$ . The same technique may be used to bound $\left| s ( x ) \right|$ on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$ .Hence $\| s \| _ { \infty }$ is not greater than $2 \| f \| _ { \infty }$ , which is the required result.□

Unfortunately there is no constant bound on $\| L \| _ { \infty }$ when $\pmb { s }$ is a quadratic spline,and when, instead of placing the interpolation points midway between the knots,the procedure of Section 18.4 is followed, which places the knots midway between the interpolation points. There is not even a constant upper bound on the norm of the interpolation operator if the knot positions are chosen to minimize the norm. This result is easy to prove if there are only three interpolation points,because then $\pmb { s }$ is just a quadratic polynomial. It is more interesting, however, to consider a case when the maximum distance between adjacent interpolation points can be made arbitrarily small. We find that it is still possible for the distribution of interpolation points to prevent a bounded norm.The demonstration depends on an elementary property of quadratic splines,which is proved in the following theorem, in order to separate it from the main argument.

# Theorem 21.3

Let $\pmb { s }$ be any quadratic spline,and let $( \alpha , \beta )$ be any interval of the real line that contains at most two knots. Then the inequality

$$
\operatorname* { m a x } _ { \alpha \leqslant x \leqslant \beta } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 2 0 } ( \beta - \alpha ) \left| s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) \right|
$$

is satisfied.

Proof.If $\pmb { S }$ is a quadratic polynomial on the interval $[ u , v ]$ , then straightforward algebra shows that the bound

$$
\operatorname* { m a x } _ { u \leqslant x \leqslant v } \left| s ( x ) \right| \geqslant \frac { 1 } { 8 } ( v - u ) \operatorname* { m a x } \left[ \left| s ^ { \prime } ( u ) \right| , \left| s ^ { \prime } ( v ) \right| \right]
$$

holds in general, and that the bound

$$
\operatorname* { m a x } _ { u \leqslant x \leqslant v } \left| s ( x ) \right| \geqslant \frac { 1 } { 2 } ( v - u ) \operatorname* { m i n } \left[ \left| s ^ { \prime } ( u ) \right| , \left| s ^ { \prime } ( v ) \right| \right]
$$

is obtained in the particular case when the signs of the derivatives $\pmb { s } ^ { \prime } ( u )$ and $\pmb { s } ^ { \prime } ( \pmb { v } )$ are the same. If there is no knot in the interval $( \alpha , \frac { 1 } { 2 } [ \alpha + \beta ] )$ ,then expression (21.30) implies that inequality (21.29) is satisfied,with the factor $\scriptstyle { \frac { 1 } { 2 0 } }$ replaced by $\scriptstyle { \frac { 1 } { 1 6 } }$ .Similarly this inequality holds when there is no knot in the interval $( \frac { 1 } { 2 } [ \alpha + \beta ] , \beta )$ . Therefore it remains to consider the case when there are two knots in $( \alpha , \beta ) , \ \xi _ { j }$ and $\xi _ { j + 1 }$ say，such that $\xi _ { j } < \frac { 1 } { 2 } ( \alpha + \beta ) < \xi _ { j + 1 }$ .Because the derivative $\{ s ^ { \prime } ( x ) ; \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } \}$ is a linear function, we may assume without loss of generality that $\pmb { s } ^ { \prime } ( \pmb { \xi } _ { j + 1 } ) \geq$ $s ^ { \prime } ( { \scriptstyle { \frac { 1 } { 2 } } } [ \alpha + \beta ] )$ ,and that $s ^ { \prime } ( { \scriptstyle { \frac { 1 } { 2 } } } [ \alpha + \beta ] )$ is non-negative. It follows from expressions (21.30) and (21.31) that the bounds

$$
\begin{array} { r l } & { \underset { \xi _ { i + 1 } \leqslant x \leqslant \beta } { \operatorname* { m a x } } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 8 } ( \beta - \xi _ { i + 1 } ) s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) } \\ & { \underset { \frac { 1 } { 2 } ( \alpha + \beta ) \leqslant x \leqslant \xi _ { j + 1 } } { \operatorname* { m a x } } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 2 } ( \xi _ { j + 1 } - \frac { 1 } { 2 } [ \alpha + \beta ] ) s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) \Bigg ] } \end{array}
$$

are obtained. Because the greater right-hand side is least when $\xi _ { j + 1 } =$ $0 . 4 \alpha + 0 . 6 \beta$ , the inequality

$$
\operatorname* { m a x } _ { { \scriptstyle \frac { 1 } { 2 } } ( \alpha + \beta ) \leqslant x \leqslant \beta } \left| s ( x ) \right| \geqslant \frac { 1 } { 2 0 } ( \beta - \alpha ) \ s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] )
$$

holds,which completes the proof of the theorem.

In order to show that, if $\pmb { s } = \pmb { L } ( f )$ is the spline in $\mathcal { S } ( 2 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions (21.18), then $\| \pmb { L } \| _ { \infty }$ may be large, even if the knot positions are chosen carefully, we consider the case when the spacings between the interpolation points are the distances

$$
\begin{array} { r } { x _ { i + 1 } - x _ { i } = \left\{ \begin{array} { c c } { h , } & { i \mathrm { ~ o d d } , } \\ { \delta h , } & { i \mathrm { ~ e v e n } , } \end{array} \right. \quad \quad i = 1 , 2 , \ldots , n + 1 , } \end{array}
$$

where $h$ and $\delta$ are positive constants, and where $\pmb \delta$ is much smaller than one. It is sufficient to show that $\| \pmb { s } \| _ { \infty }$ is large when the data have the values $\{ f ( x _ { i } ) = ( - 1 ) ^ { i + 1 }$ ； $i = 1 , 2 , \ldots , n + 2 \}$ If $q$ is any even integer in the range $[ 2 , n ] ,$ , then the mean value theorem implies that there is a point $\pmb { \eta _ { q } }$ in the interval $\left( x _ { q } , x _ { q + 1 } \right)$ that satisfies the equation

$$
\begin{array} { c } { { s ^ { \prime } ( \eta _ { q } ) = [ s ( x _ { q + 1 } ) - s ( x _ { q } ) ] / ( x _ { q + 1 } - x _ { q } ) } } \\ { { { } } } \\ { { = 2 / ( \delta h ) . } } \end{array}
$$

Because the intervals $\{ ( \eta _ { q } - { \textstyle \frac { 1 } { 2 } } h , \eta _ { q } + { \textstyle \frac { 1 } { 2 } } h ) ; q = 2 , 4 , 6 , . . . \}$ are disjoint, and because the number of internal knots of the spline is only $( n - 1 )$ ，it follows that, when $_ n$ is large, there are fewer than three knots in several of the intervals $\{ ( \eta _ { q } - \frac { 1 } { 2 } h , \eta _ { q } + \frac { 1 } { 2 } h )$ ； $q = 2 , 4 , 6 , \ldots \}$ .We apply Theorem 21.3 to any one of them,where $( \alpha , \beta ) = ( \eta _ { q } - \textstyle \frac 1 2 h , \eta _ { q } + \textstyle \frac 1 2 h )$ . Hence equation (21.35) gives the bound

$$
\| s \| _ { \infty } \geqslant 1 / ( 1 0 \delta ) .
$$

This inequality holds for all choices of knots, and $\pmb { \delta }$ can be arbitrarily small. Therefore some distributions of interpolation points make it inevitable that the norm of the interpolation operator is large.Hence it is important sometimes to choose the positions of the knots before the positions of the interpolation points,and then Theorem 21.2 gives a convenient way of achieving a small norm.

# 21.3 The approximation of functions to prescribed accuracy

This section considers the problem of calculating automatically a cubic spline function $\pmb { s }$ that satisfies the condition

$$
\| f - s \| _ { \infty } \leqslant \varepsilon ,
$$

where $f$ is a given function in $\mathcal { C } [ a , b ]$ ,and where $\pmb \varepsilon$ is a given constant tolerance.One reason for this study is that, if a computer program requires the value $f ( x )$ for many thousand different values of $x$ ,and if each evaluation takes several seconds of computer time, then it is necessary to replace $f$ by an approximation that can be calculated easily. We let $\pmb { s }$ be a cubic spline approximation, because cubic splines give a good balance between smoothness and flexibility.

First we consider a spline whose knots are equally spaced

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = 0 , 1 , \ldots , n ,
$$

and that satisfies the interpolation conditions

$$
s ( \xi _ { j } ) = f ( \xi _ { j } ) , \qquad j = 0 , 1 , . . . , n .
$$

We suppose that the technique that fixes the two end conditions, discussed in Section 18.3,is such that,if $f$ is a quartic polynomial, then $s ^ { \prime } ( a )$ and $s ^ { \prime } ( b )$ are equal to $f ^ { \prime } ( a )$ and $f ^ { \prime } ( b )$ respectively.For example,Exercise 18.3 shows that it is sufficient to satisfy the equations $d _ { 1 } = d _ { 2 }$ and $d _ { n - 2 } = d _ { n - 1 }$ ,where $d _ { j }$ is the third derivative discontinuity

$$
d _ { j } = s ^ { \prime \prime \prime } ( \xi _ { j } + ) - s ^ { \prime \prime \prime } ( \xi _ { j } - ) , \qquad j = 1 , 2 , \ldots , n - 1 .
$$

If the number of knots of $\pmb { s }$ is to be chosen automatically, then it is necessary to predict whether the accuracy (21.37) is obtained.

In order to derive an error estimate, we follow an approach that is often successful. It is to analyse the error of the spline approximation when $f$ is a polynomial of the lowest degree that gives a non-zero error. Therefore we assume that $f$ is in ${ \mathcal { P } } _ { 4 }$ ,and we note that Exercise 18.3 implies the values

$$
\begin{array} { c c } { { s ( \xi _ { j } ) = f ( \xi _ { j } ) } } \\ { { s ^ { \prime } ( \xi _ { j } ) = f ^ { \prime } ( \xi _ { j } ) } } \end{array} \bigg \} , ~ j = 0 , 1 , . . . , n ,
$$

and

$$
d _ { j } = h f ^ { ( 4 ) } ( \xi ) , \qquad j = 1 , 2 , \dots , n - 1 ,
$$

where $\pmb { \xi }$ is any point of $[ a , b ]$ .Because the function $\{ f ( x ) - s ( x ) ; \xi _ { q } \leqslant x \leqslant$

$\xi _ { q + 1 } \big \}$ is a quartic polynomial, where $q$ is any integer in $[ 0 , n - 1 ]$ ,it follows from expressions (21.41) and (21.42) that the equation

$$
\begin{array} { r l } { f ( x ) - s ( x ) = \frac { 1 } { 2 4 } ( x - \xi _ { q } ) ^ { 2 } ( x - \xi _ { q + 1 } ) ^ { 2 } f ^ { ( 4 ) } ( \xi ) \ d t } \\ { = \displaystyle \frac { 1 } { 2 4 h } ( x - \xi _ { q } ) ^ { 2 } ( x - \xi _ { q + 1 } ) ^ { 2 } d _ { j } , \qquad \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } , } \end{array}
$$

is satisfied. Because the greatest error occurs at the point $\begin{array} { r } { { \pmb x } = \frac { 1 } { 2 } ( { \pmb \xi } _ { q } + { \pmb \xi } _ { q + 1 } ) } \end{array}$ it has the value

$$
\operatorname* { m a x } _ { \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } } | f ( x ) - s ( x ) | = \frac { h ^ { 3 } } { 3 8 4 } | d _ { j } | ,
$$

where $d _ { j }$ is any one of the third derivative discontinuities of $s$ , and where $f$ is a fourth degree polynomial.

The next stage of the derivation of the error estimate is to let $f$ be an infinitely differentiable function, and to consider the error of the spline approximation to the Taylor series expansion

$$
f ( x ) = \sum _ { i = 0 } ^ { \infty } { \frac { ( x - \xi ) ^ { i } } { i ! } } f ^ { ( i ) } ( \xi ) , \qquad a \leqslant x \leqslant b ,
$$

where $\xi$ is any fixed point of $[ a , b ]$ . Because the interpolation method for calculating the spline approximation is a linear operator, the error $( f - s )$ is the sum of the errors that occur when the separate terms of the Taylor series are approximated by splines. It is important to note that, because the cardinal function of Figure 18.2 decays exponentially, the error $\{ f ( \xi ) - s ( \xi )$ ； $a \leqslant \xi \leqslant b \}$ is dominated by the form of $\{ f ( x ) ; a \leqslant x \leqslant b \}$ in a neighbourhood of $\xi .$ Therefore,for sufficiently small $h _ { \ast }$ ,the error at $\xi$ is mostly due to the fourth derivative term of expression (21.45). A similar argument shows that, if $h$ is sufficiently small, and if $\xi _ { j }$ is close to $\xi ,$ ，then the main contribution to the third derivative discontinuity (21.40) also comes from the fourth derivative term of the Taylor series. By combining these remarks with equation (21.44),we obtain the error estimate

$$
\operatorname* { m a x } _ { \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } } { \big | } f ( x ) - s ( x ) { \big | } \approx { \frac { h ^ { 3 } } { 3 8 4 } } \operatorname* { m a x } { [ \big | } d _ { q } { \big | } , \big | d _ { q + 1 } { \big | } ] .
$$

It may be used for $q = 1 , 2 , \ldots , n - 2 .$ When $q = 0$ the term $\left| d _ { q } \right|$ is deleted from the right-hand side,and when $q = n - 1$ the term $| d _ { q + 1 } |$ is deleted, because $s$ does not have third derivative discontinuities at $\xi _ { 0 }$ and $\xi _ { n }$

The approximation (21.46) is usually adequate in practice,even when $f$ has some mild singularities. It is easy to calculate the right-hand side of the approximation from the parameters of $\pmb { S } ,$ . Because there are separate error estimates for each of the intervals $\{ [ \xi _ { q } , \xi _ { q + 1 } ] ; q = 0 , 1 , \ldots , n - 1 \}$ a computer program can find automatically when it is advantageous to give up the condition that the spacing between knots is constant.

The example of Section 21.1 shows that changes in knot spacing can give large gains in efficiency，but one loses the advantage that is mentioned in the opening sentence of this chapter, error control is more difficult when there are frequent changes of knot spacing,and also, if a sequence of trial approximations to $f$ is calculated, then it is more difficult to control the positions of interpolation points so that full use is made of all calculated values of $f ( x )$ . A successful compromise is to keep each knot spacing for several consecutive intervals,and to allow only halving and doubling where the knot spacing changes.Therefore we consider the case when the knots have the values

$$
\begin{array} { l } { { \xi _ { j } = \xi _ { r } + ( j - r ) h , \qquad j = 0 , 1 , \ldots , r } } \\ { { \qquad \xi _ { j } = \xi _ { r } + 2 ( j - r ) h , \qquad j = r , r + 1 , \ldots , n } } \end{array} \biggr \} ,
$$

where $\xi _ { r }$ is remote from the ends of the range $[ a , b ]$ . In particular, we ask whether the error estimate (21.46) is suitable if $q$ is close to $\boldsymbol { r }$

Because of the importance of the fourth order term of the Taylor series (21.45), we again let $f$ be a quartic polynomial, and we let $e = f - s$ be the error function of the spline approximation that is defined by interpolation at the knots (21.47).In order to analyse this error function, we compare it with $e _ { h }$ and $e _ { 2 h }$ ,which are the error functions that would be obtained if the spacing between knots were the constants $h$ and $^ { 2 h }$ respectively.The solid line of Figure 21.1 is the function $^ e$ ,and the dotted line is composed of the functions $\{ e _ { h } ( x ) ; \xi _ { r - 4 } \leqslant x \leqslant \xi _ { r } \}$ and $\{ e _ { 2 h } ( x ) ; \xi _ { r } \leqslant x \leqslant \xi _ { r + 3 } \}$ The differences $\{ e ( x ) - e _ { h } ( x ) ; x \leqslant \xi _ { r } \}$ and $\{ e ( x ) - e _ { 2 h } ( x ) ; x \ge \xi _ { r } \}$ are similar to the tails of the cardinal function of Figure 18.2.

![](images/7fbda3a09f149a594656ab153164f92a6fba11718b20318935ebec7f3102747c.jpg)  
Figure 21.1. The effect on the error of a change in step-length.

Therefore,assuming that the effects from the ends of the range $[ a , b ]$ can be neglected, there exist parameters $\pmb { \lambda }$ and $\pmb { \mu }$ such that the equation

$$
e ( x ) = \left\{ \begin{array} { l l } { e _ { h } ( x ) + \lambda \ \sigma ( [ \xi _ { r } - x ] / h ) , \quad } & { x \leqslant \xi _ { r } } \\ { e _ { 2 h } ( x ) + \mu \ \sigma ( [ x - \xi _ { r } ] / 2 h ) , \quad } & { x \geqslant \xi _ { r } , } \end{array} \right.
$$

holds, where $\pmb { \sigma }$ is the function

$$
\sigma ( x ) = x - \sqrt { 3 { x } ^ { 2 } + ( \sqrt { 3 } - 1 ) { x } ^ { 3 } + 2 \sqrt { 3 } \sum _ { j = 1 , 2 , . . . } ( \sqrt { 3 } - 2 ) ^ { j } ( x - j ) _ { + } ^ { 3 } } ,
$$

that is studied in Section 19.1. Because $e ^ { \prime }$ and $e ^ { \prime \prime }$ are continuous at $\boldsymbol { x } = \boldsymbol { \xi } _ { r } ,$ the conditions $\mu = - 2 \lambda$ and

$$
{ \textstyle \frac { 1 } { 1 2 } } h ^ { 2 } f ^ { ( 4 ) } ( \xi ) - 2 \sqrt { 3 \lambda / h ^ { 2 } } = { \textstyle \frac { 1 } { 3 } } h ^ { 2 } f ^ { ( 4 ) } ( \xi ) - { \textstyle \frac { 1 } { 2 } } \sqrt { 3 \mu / h ^ { 2 } }
$$

are satisfied, where $f ^ { ( 4 ) } ( \xi )$ is the constant fourth derivative of $f .$ It follows that the parameters have the values

$$
\left. \begin{array} { l } { \displaystyle \lambda = - \frac { h ^ { 4 } } { 1 2 \sqrt { 3 } } f ^ { ( 4 ) } ( \xi ) } \\ { \displaystyle \mu = \frac { h ^ { 4 } } { 6 \sqrt { 3 } } f ^ { ( 4 ) } ( \xi ) } \end{array} \right\} .
$$

It is now straightforward to obtain from expression (21.48) the third derivative discontinuities of $\pmb { s }$ , and the maximum value of $| f - s |$ on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = r - 4 , r - 3 , \ldots , r + 2 \}$ .These numbers are given in Table 21.1.

The table shows that the expression

$$
\operatorname* { m a x } _ { \xi _ { q } \le x \le \xi _ { q + 1 } } | f ( x ) - s ( x ) | \approx \frac { ( \xi _ { q + 1 } - \xi _ { q } ) ^ { 3 } } { 3 8 4 } \operatorname* { m a x } \left[ | d _ { q } | , \left| d _ { q + 1 } \right| \right]
$$

Table 21.1. Errors and derivative discontinuities at a change in knot spacing   

<table><tr><td>j di max |f(x)-s(x)l j≤x≤5j+1</td></tr><tr><td>1.0052hf(() 0.0028h4f（4）（） r-4</td></tr><tr><td>0.9808hf（4（） 0.0021h4f(） r-3</td></tr><tr><td>1.0718hf() 0.0047h4f4（) r-2</td></tr><tr><td>0.7321hf（（） 0.0060hf（（） r-1</td></tr><tr><td>1.6585hf(（) 0.0571h4f（）（） r</td></tr><tr><td>2.0670hf（） 0.0376h4f（） r+1</td></tr><tr><td>r+2 1.9821hf(） 0.0428h4f（4）() r+3 2.0048hf（(）</td></tr><tr><td></td></tr></table>

overestimates the error when $q = r - 3$ and $r + 1$ , and it underestimates the error when $q = r - 4 , r - 2 , r - 1$ ， $r$ and $r + 2$ ,by $7 \%$ ， $4 1 \%$ ， $2 8 \%$ ， $2 5 \%$ and 22% respectively. The discrepancies for q<r do not matter very much because they occur in errors that are much smaller then the errors when $q \geqslant r .$ The $2 \%$ discrepancy can usually be ignored,but a modification is needed when $q = r .$ The table suggests that the approximation

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { k \to s \in \xi _ { r + 1 } } \big | f ( x ) - s ( x ) \big | } } \\ & { } & { \approx \frac { ( \xi _ { r + 1 } - \xi _ { r } ) ^ { 3 } } { 3 8 4 } \operatorname* { m a x } [ 1 . 6 5 | d _ { r } | , | d _ { r + 1 } | ] } \end{array}
$$

is suitable.Moreover,in order to avoid the possibility that the error estimate predicts incorrectly that the interval $[ \xi _ { r - 1 } , \xi _ { r } ]$ is too long, it is advisable to delete the term $| d _ { q + 1 } |$ from expression (21.52) when $q = r - 1$ .

These ideas give an automatic method of estimating the local error of an interpolating cubic spline approximation to a function $f ,$ provided that, where the knot spacing changes, it only halves or doubles,and provided that each new knot spacing is used for several consecutive intervals.The error estimate is usually adequate when $f$ is a general function,even though the analysis is based on the assumption that $f$ is a quartic polynomial. If it is applied to a trial cubic spline approximation, then the estimate indicates the parts of the range $[ a , b ]$ where the accuracy is insufficient. By reducing the knot spacing only in these parts of the range, the spacing between knots can be adapted automatically to the form of $f .$ Hence a general algorithm has been developed for solving the problem that is stated at the beginning of this section. The algorithm begins by calculating an interpolating cubic spline that has a few equally spaced knots in $[ a , b ]$ .This spline is the first of a sequence of trial approximations.If it is predicted that a trial approximation is not sufficiently accurate, then the knot spacing is halved where the error is too large,and a new trial spline is calculated. The procedure finishes when the error estimate indicates that the required accuracy is achieved. Two features that are worth including in the algorithm are to insert extra knots only in the parts of the range $[ a , b ]$ where it is predicted that the error of the current trial approximation is within one-sixteenth of its maximum value, and to allow for an effect that is shown in Figure 21.1, namely that in the interval $[ \xi _ { r } , \xi _ { r + 1 } ]$ the error given by the solid line is about 1.4 times larger than the error shown by the dashed line. This increase in error is due to the change in interval length at $\xi _ { r }$ . Many trial approximations can be saved sometimes by anticipating this effect when the algorithm chooses the intervals in which to place new knots.

# 21 Exercises

21.1 If a linear spline approximation $\pmb { s }$ to a function $f$ in $\mathcal { C } ^ { ( 2 ) } [ a , b ]$ satisfies the condition $\| f - s \| _ { \infty } \leqslant \varepsilon$ and if $\pmb { s }$ interpolates $f$ at the knots,then Theorem 4.2 shows that, in a neighbourhood of a point $x$ of $[ a , b ] _ { \mathrm { : } }$ ,the knot spacing $^ { h }$ is at most about $\left| 8 \varepsilon / f ^ { \prime \prime } ( x ) \right| ^ { \frac { 1 } { 2 } }$ . This remark suggests the density of knots that is needed to approximate a given function to prescribed accuracy. Hence estimate the minimum number of knots that are necessary to achieve the condition $\| f - s \| _ { \infty } \leqslant \varepsilon$ when $f$ is the function $\{ f ( x ) =$ $x ^ { \mu } ; 0 \leqslant x \leqslant 1 \}$ where the constant $\pmb { \mu }$ is greater than two. Show that, if the knot spacing has to be constant, then the number of knots increases by a factor of about ${ \scriptstyle { \frac { 1 } { 2 } } } \mu$

21.2 Apply the interpolation method of Theorem 21.2 to calculate a spline approximation from the space $\mathcal { S } ( 2 , 0 , \frac { 1 } { 6 4 } , \frac { 8 } { 6 4 } , \frac { 2 7 } { 6 4 } , 1 )$ to the function $\dot { \{ f ( x ) = x ^ { \frac { 3 } { 2 } } } $ ； $0 \leqslant x \leqslant 1 \}$ . You should find that the maximum error at a knot is equal to O.000 254.

21.3 Let $\mathcal { S } _ { \epsilon }$ be the space of cubic splines on the infinite range $( - \infty , \infty )$ that have knots at the points $\{ \xi _ { 3 j } = j h$ ， $\xi _ { 3 j - 1 } = j h - \varepsilon$ ， $\xi _ { 3 j + 1 } =$ $j h + \varepsilon ; j = 0 , \pm 1 , \pm 2 , . . . \} ,$ ，where $h$ is a positive constant, and where $\varepsilon$ is a positive parameter that is less than $^ { \frac { 1 } { 2 } h }$ For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { S } _ { \epsilon }$ be the bounded spline in $\mathcal { S } _ { \epsilon }$ that interpolates $f$ at the points $\begin{array} { r } { \{ x _ { i } = \frac { 1 } { 3 } ( \xi _ { i - 1 } + \xi _ { i } + \xi _ { i + 1 } ) } \end{array}$ ； $i = 0 , \pm 1 , \pm 2 , \ldots \}$ Prove that, as $\varepsilon$ tends to zero, $\pmb { S } _ { \pmb { \epsilon } }$ tends to the function $s ^ { * }$ that, on each of the intervals $\{ [ j h , j h + h ] ; j = 0 , \pm 1 , \pm 2 , . . . \}$ ，is the cubic polynomial that is defined by the interpolation conditions $\{ s ^ { * } ( j h + { \textstyle \frac { 1 } { 3 } } l h ) = f ( j h + { \textstyle \frac { 1 } { 3 } } l h ) ; l = 0 , 1 , 2 , 3 \} .$

21.4 Let $\pmb { \mathscr { s } }$ be the cubic spline that interpolates the function $\{ f ( { \pmb x } ) =$ $| x | ; - \infty < x < \infty \}$ at the knots $\{ \xi _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , \ldots \}$ Show that the error estimate (21.46) underestimates the error in the interval $[ \xi _ { 0 } , \xi _ { 1 } ]$ by a factor of about 7.4.

21.5 Let the knots of a cubic spline $\pmb { s }$ on $( - \infty , \infty )$ have the values $\{ \xi _ { j } = j h ; j \ge 0 \}$ and $\{ \xi _ { j } = j \eta h ; j \leqslant 0 \}$ ，where $\eta$ is a small positive constant. Prove that, if $\pmb { s }$ is the bounded spline that satisfies the cardinality conditions $\{ s ( \xi _ { j } ) = \delta _ { j 0 } ; j = 0 , \pm 1 , \pm 2 , . . . \} ,$ ， then there is no upper bound on $\| \pmb { s } \| _ { \infty }$ that is independent of $\pmb { \eta }$

21.6 Let $f$ be a function in $\mathcal { C } ^ { ( 2 ) } [ a , b ]$ such that the derivative $\{ f ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ has no zeros. For any small positive number $\varepsilon$ let $\pmb { s }$ be a linear spline with fewest knots that gives the accuracy $\| f - s \| _ { \infty } \leqslant \varepsilon$ ， subject to the condition that $\pmb { s }$ interpolates $f$ at its knots. Investigate the positions of the knots of s $\{ \xi _ { j } [ \varepsilon ] ; j =$ $0 , 1 , \dots , n [ \varepsilon ] \}$ say,in the limit as $\pmb \varepsilon$ tends to zero. You should find that asymptotically $\xi _ { j } [ \varepsilon ]$ has the value $\phi ( j / n [ \varepsilon ] )$ ，where $\left\{ \phi ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ is the monotonically increasing differentiable function that satisfies the equations $\phi ( 0 ) = a$ ， $\phi ( 1 ) = b$ ,and

$$
[ \phi ^ { \prime } ( \theta ) ] ^ { 2 } f ^ { \prime \prime } [ \phi \left( \theta \right) ] = \mathrm { c o n s t a n t } , \qquad 0 \leqslant \theta \leqslant 1 .
$$

21.7 Use Exercise 21.6 to explain why the knots (21.6) are particularly suitable for the approximation of the function $\{ f ( { \pmb x } ) =$ $x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ by a linear spline. Similarly，find good knot positions for the approximation of the function $\{ f ( x ) = x ^ { \mu }$ ； $0 \leqslant x \leqslant 1 \}$ ,where $\pmb { \mu }$ is a constant in (O,1),and bound the number of knots that are needed to achieve a given accuracy.

21.8 Apply the method that gives the error estimate (21.46) to deduce that, if $\pmb { s }$ is a quadratic spline with equally spaced knots $\{ \xi _ { j } = j h \}$ ， that interpolates a function $f$ at the points that are midway between the knots, then the error estimate

$$
\operatorname* { m a x } _ { \xi _ { q } \le x \le \xi _ { q + 1 } } \big | f ( x ) - s ( x ) \big | \approx \frac { h ^ { 2 } } { 7 2 \sqrt { 3 } } \operatorname* { m a x } \left[ \big | d _ { q } \big | , \big | d _ { q + 1 } \big | \right]
$$

is appropriate, where $d _ { q }$ is the second derivative discontinuity of $\pmb { s }$ at $\xi _ { q }$

21.9 Let $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ be the space that is defned in the last paragraph of Section 21.1, where inequality (21.17) holds.Let $\pmb { s }$ be any fixed function in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ,and let $\pmb \varepsilon$ be any pos-itive constant.Prove thatthereexists apositive number $\pmb { \delta }$ suchthat, if $\{ \eta _ { j } ; j = 0 , 1 , \dotsc , n \}$ is any set of numbers that satisfies the conditions $\{ \vert \eta _ { j } - \xi _ { j } \vert \leqslant \delta$ ； $j = 0 , 1 , \ldots , n \}$ and $a = \eta _ { 0 } < \eta _ { 1 } < \eta _ { 2 } < . ~ . ~ .$ $< \eta _ { n } = b$ ，then there is a function, $\pmb { \sigma }$ say，in the space $\mathcal { S } ( k , \eta _ { 0 } , \eta _ { 1 } , \dots , \eta _ { n } )$ such that $\| s - \sigma \| _ { \infty }$ is less than $\pmb \varepsilon$

21.10 Extend the definition of $\pmb { B }$ -splines and the four theorems of Chapter 19 to the case when $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ is the extended space of splines that is defined in the last paragraph of Section 21.1.

#

# The Peano kernel theorem

# 22.1 The error of a formula for the solution of differential equations

The Peano kernel theorem gives a general and highly useful technique for expressing the errors of approximations in terms of derivatives of the underlying function of the approximation. For example, let the coefficients $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ and the points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ be such that the quadrature rule

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x \approx \sum _ { t = 1 } ^ { m } w _ { t } f ( x _ { t } )
$$

is exact when $f$ is in $\mathcal { P } _ { k }$ ，where the points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ are all in $[ a , b ]$ .The theorem defines a function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ , that is independent of $f ,$ such that the equation

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x - \sum _ { t = 1 } ^ { m } w _ { t } f ( x _ { t } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

holds for all functions $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ . One useful consequence of this equation is that the error of the approximation (22.1) is bounded above by $c \| f ^ { ( k + 1 ) } \| _ { \infty }$ ,where $c$ is the number

$$
c = \int _ { a } ^ { b } \left| K ( \theta ) \right| \mathrm { d } \theta .
$$

Because $c$ is independent of $f ,$ it provides a convenient measure of the accuracy of formula (22.1), that may be useful to a comparison of integration methods.

In order to introduce the theorem，we consider the problem of expressing the error of the formula

$$
f ( x _ { t } + 2 h ) \approx f ( x _ { t } + h ) + h \big [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) \big ]
$$

in terms of the third derivative of $f .$ This formula is a standard technique for the step-by-step solution of ordinary differential equations. We solve the problem by making use of the Taylor series. In Section 22.2 the method of solution is generalized, which gives the Peano kernel theorem. The remainder of the chapter describes some applications of the theorem.

The simplest way of estimating the error

$$
L ( f ) = f ( x _ { t } + 2 h ) - f ( x _ { t } + h ) - h [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) ] ,
$$

when $f$ is suficiently differentiable, is to make the Taylor series approximations

$$
\left. { \begin{array} { l } { f ( x _ { t } + 2 h ) = f ( x _ { t } ) + 2 h f ^ { \prime } ( x _ { t } ) + 2 h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) + { \frac { 4 } { 3 } } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \\ { f ( x _ { t } + h ) = f ( x _ { t } ) + h f ^ { \prime } ( x _ { t } ) + { \frac { 1 } { 2 } } h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) + { \frac { 1 } { 6 } } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \\ { f ^ { \prime } ( x _ { t } + h ) = f ^ { \prime } ( x _ { t } ) + h f ^ { \prime \prime } ( x _ { t } ) + { \frac { 1 } { 2 } } h ^ { 2 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \end{array} } \right\} ,
$$

ignoring the higher order terms that are represented by‘...'.By substituting expression (22.6) in equation (22.5) we obtain the estimate

$$
\begin{array} { r } { L ( f ) \approx \frac { 5 } { 1 2 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) . } \end{array}
$$

It is better, however, to use the Taylor series with explicit remainder, because then the exact value of $L ( f )$ is found. We express $f ( x _ { t } + h )$ ,for example,in the form

$$
\begin{array} { l } { f ( x _ { t } + h ) = f ( x _ { t } ) + h f ^ { \prime } ( x _ { t } ) + \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) } \\ { \qquad + \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) ^ { 2 } f ^ { \prime \prime \prime } ( \theta ) \ : \mathrm { d } \theta . } \end{array}
$$

Hence equation (22.5) implies the identity

$$
\begin{array} { r l } & { L ( f ) = \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + 2 h } \left( x _ { t } + 2 h - \theta \right) ^ { 2 } f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad - \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) ^ { 2 } f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad - \frac { 3 } { 2 } h \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad = \displaystyle \int _ { x _ { t } } ^ { x _ { t } + 2 h } K ( \theta ) f ^ { \prime \prime \prime } ( \theta ) \mathrm { d } \theta , } \end{array}
$$

where $\pmb { K } ( \pmb \theta )$ has the value

$$
\begin{array} { r } { K ( \theta ) = \Big \{ \frac { 1 } { 2 } h \big ( \theta - x _ { t } \big ) , \qquad x _ { t } \leqslant \theta \leqslant x _ { t } + h } \\ { \frac 1 2 \big ( x _ { t } + 2 h - \theta \big ) ^ { 2 } , \qquad x _ { t } + h \leqslant \theta \leqslant x _ { t } + 2 h . } \end{array}
$$