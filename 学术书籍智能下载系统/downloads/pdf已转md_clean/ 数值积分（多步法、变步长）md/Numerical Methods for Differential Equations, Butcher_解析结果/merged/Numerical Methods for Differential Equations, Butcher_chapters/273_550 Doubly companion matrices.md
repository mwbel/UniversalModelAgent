# 550 Doubly companion matrices

As a preliminary to a discussion of inherent RK stability, we recall the properties of the matrices introduced by Butcher and Chartier (1997). The original application was in the analysis of singly implicit methods with a specific effective order, but they also have a central role in the construction of the methods to be considered in Subsection 551. A review of doubly companion matrices is given in Butcher and Wright (2006).

Let $\alpha ( z ) = 1 + \alpha _ { 1 } z + \cdot \cdot \cdot + \alpha _ { n } z ^ { n }$ and $\beta ( z ) = 1 + \beta _ { 1 } z + \cdot \cdot \cdot + \beta _ { n } z ^ { n }$ denote given polynomials, and consider the $n \times n$ matrix

$$
X = \left[ { \begin{array} { c c c c c c c c } { - \alpha _ { 1 } } & { - \alpha _ { 2 } } & { - \alpha _ { 3 } } & { \cdots } & { - \alpha _ { n - 1 } } & { - \alpha _ { n } - \beta _ { n } } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - \beta _ { n - 1 } } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { - \beta _ { n - 2 } } \\ { \vdots } & { \vdots } & { \vdots } & & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - \beta _ { 1 } } \end{array} } \right] .
$$

Theorem 550A The coefficients in the characteristic polynomial of $X$ , $\operatorname* { d e t } ( w I - X ) = w ^ { n } + \gamma _ { 1 } w ^ { n - 1 } + \gamma _ { 2 } w ^ { n - 2 } + \cdot \cdot \cdot + \gamma _ { n }$ , are given by

$$
1 + \gamma _ { 1 } z + \gamma _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \gamma _ { n } z ^ { n } = \operatorname * { d e t } ( I - z X ) = \alpha ( z ) \beta ( z ) + O ( z ^ { n + 1 } ) .
$$

Proof. We assume that the eigenvalues of $X$ are distinct and non-zero. There is no loss of generality in this assumption because, for given values of the $\alpha$ coefficients, the coefficients in the characteristic polynomial are continuous functions of the $\beta$ coefficients; furthermore, choices of the $\beta$ coefficients which lead to distinct non-zero eigenvalues form a dense set.

Let $\lambda$ denote an eigenvalue of $X$ , and let

$$
\begin{array} { r } { v _ { k } = \lambda ^ { k } + \beta _ { 1 } \lambda ^ { k - 1 } + \beta _ { 2 } \lambda ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } , \qquad k = 0 , 1 , 2 , \dots , n . } \end{array}
$$

By comparing components numbered $n$ , $n - 1 , \ldots , 2$ of $X v$ and $\lambda v$ , where

$$
V = [ v _ { n - 1 } \quad v _ { n - 2 } \quad \cdot \cdot \cdot \quad 1 ] ^ { \top } ,
$$

we see that $v$ is the eigenvector corresponding to $\lambda$ . Now compare the first components of $\lambda v$ and $X v$ and it is found that

$$
\lambda v _ { n } + \alpha _ { 1 } v _ { n - 1 } + \cdot \cdot \cdot + \alpha _ { n } = 0
$$

and contains all the terms with non-negative exponents in the product

$$
v _ { n } ( 1 + \alpha _ { 1 } \lambda ^ { - 1 } + \cdots + \alpha _ { n } \lambda ^ { - n } ) .
$$

Replace $\lambda$ by $z ^ { - 1 }$ and the result follows.

Write $\phi ( z )$ for the vector (550b) with $\lambda$ replaced by $z$ . We now note that

$$
z \phi ( z ) - X \phi ( z ) = \prod _ { i = 1 } ^ { n } ( z - \lambda _ { i } ) e _ { 1 } ,
$$

because the expression vanishes identically except for the first component which is a monic polynomial of degree $n$ which vanishes when $z$ is an eigenvalue.

We are especially interested in choices of $\alpha$ and $\beta$ such that $X$ has a single $n$ -fold eigenvalue, so that

$$
\alpha ( z ) \beta ( z ) = ( 1 - \lambda z ) ^ { n } + O ( z ^ { n + 1 } )
$$

and so that the right-hand side of (550c) becomes $( z - \lambda ) ^ { n } e _ { 1 }$ . In this case it is possible to write down the similarity that transforms $X$ to Jordan canonical form.

Theorem 550B Let the doubly companion matrix $X$ be chosen so that (550d) holds. Also let $\phi ( z )$ denote the vector given by (550b) with $\lambda$ replaced by $z$ , and let $S$ the matrix given by

$$
\begin{array} { r } { \Psi = \big [ \frac { 1 } { ( n - 1 ) ! } \phi ^ { ( n - 1 ) } ( \lambda ) \quad \frac { 1 } { ( n - 2 ) ! } \phi ^ { ( n - 2 ) } ( \lambda ) \quad \cdots \quad \frac { 1 } { 1 ! } \phi ^ { \prime } ( \lambda ) \quad \phi ( \lambda ) \big ] . } \end{array}
$$

Then

$$
\Psi ^ { - 1 } X \Psi = \left[ \begin{array} { l l l l l l } { \lambda } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { \lambda } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { \lambda } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { \lambda } \end{array} \right] .
$$

Proof. From the special case of (550c), we have

$$
X \phi ( z ) = z \phi ( z ) - ( z - \lambda ) ^ { n } e _ { 1 } .
$$

Differentiate $k$ times, divide by $k$ ! and set $z = \lambda$ , for $k = 1 , 2 , \ldots , n - 1$ . The result is

$$
X \frac { 1 } { k ! } \phi ^ { ( k ) } ( \lambda ) = \lambda I \frac { 1 } { k ! } \phi ^ { ( k ) } ( \lambda ) + \frac { 1 } { ( k - 1 ) ! } \phi ^ { ( k - 1 ) } ( \lambda ) , \qquad k = 1 , 2 , \ldots , n - 1 .
$$

Hence the vectors $\phi ( \lambda )$ , $\phi ^ { \prime } ( \lambda ) , \textstyle { \frac { 1 } { 2 ! } } \phi ^ { \prime \prime } ( \lambda ) , \dots , \textstyle { \frac { 1 } { ( n - 1 ) ! } } \phi ^ { ( n - 1 ) } ( \lambda )$ form a sequence of eigenvector and generalized eigenvectors, and the result follows. 

The inverse of $\Psi$ is easy to evaluate by interchanging the roles of rows and columns of $X$ . We present the following result without further proof.

# Corollary 550C If

$$
\begin{array} { r } { \chi ( \lambda ) = [ 1 \quad \lambda + \alpha _ { 1 } \quad \lambda ^ { 2 } + \alpha _ { 1 } \lambda + \alpha _ { 2 } \quad \cdots \quad \lambda ^ { n - 1 } + \alpha _ { 1 } \lambda ^ { n - 2 } + \cdots + \alpha _ { n - 1 } ] , } \end{array}
$$

then

$$
\Psi ^ { - 1 } = [ \chi ( \lambda ) \quad { \textstyle { \frac { 1 } { 1 ! } } } \chi ^ { \prime } ( \lambda ) \quad \cdots \quad { \textstyle { \frac { 1 } { ( n - 2 ) ! } } } \chi ^ { ( n - 2 ) } ( \lambda ) \quad { \textstyle { \frac { 1 } { ( n - 1 ) ! } } } \chi ^ { ( n - 1 ) } ( \lambda ) ] ^ { \top } .
$$
