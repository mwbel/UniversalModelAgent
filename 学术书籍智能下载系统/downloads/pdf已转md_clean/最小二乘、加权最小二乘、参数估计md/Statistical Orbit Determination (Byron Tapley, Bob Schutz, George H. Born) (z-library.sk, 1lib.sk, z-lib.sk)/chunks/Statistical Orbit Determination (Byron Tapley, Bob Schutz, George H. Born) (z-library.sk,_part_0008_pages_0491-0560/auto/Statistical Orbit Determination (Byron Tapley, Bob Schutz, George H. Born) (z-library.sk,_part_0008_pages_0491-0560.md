# B.2 RANK

• The rank of a matrix is the dimension of its largest square nonsingular submatrix; that is, one whose determinant is nonzero.

• The rank of the product AB of the two matrices $\mathbf { A }$ and $\mathbf { B }$ is less than or equal to the rank of $\mathbf { A }$ and is less than or equal to the rank of $\mathbf { B }$ .

• The rank of the sum of $\textbf { A + B }$ is less than or equal to the rank of $\mathbf { A }$ plus the rank of $\mathbf { B }$ .

• If A is an $n \times n$ matrix and if $| \mathbf { A } | = 0$ , then the rank of $\mathbf { A }$ is less than $n$ .

• If the rank of $\mathbf { A }$ is less than $n$ , then all the rows of $\mathbf { A }$ are not independent; likewise, all the columns of $\mathbf { A }$ are not independent ( $\mathbf { A }$ is $n \times n$ ).

• If the rank of $\mathbf { A }$ is $m \leq n$ , then the number of linearly independent rows is $m$ ; also, the number of linearly independent columns is $m$ ( $\mathbf { A }$ is $n \times n$ ).

• If $\mathbf { A } ^ { T } \mathbf { A } \ = \ 0$ , then $\textbf { A } = \textbf { 0 }$ .

• The rank of a matrix is unaltered by multiplication by a nonsingular matrix; that is, if A, $\mathbf { B }$ , and $\mathbf { C }$ are matrices such that AB and BC exist and if A and $\mathbf { C }$ are nonsingular, then $\rho \left( \mathbf { A } \mathbf { B } \right) \ = \ \rho \left( \mathbf { B } \mathbf { C } \right) \ = \ \rho \left( \mathbf { B } \right) . \rho \left( \mathbf { B } \right) \ = \mathbf { r }$ ank of $\mathbf { B }$ .

• If the product AB of two square matrices is 0, then $\mathbf { A } = 0 , \mathbf { B } = 0$ , or A and $\mathbf { B }$ are both singular.

• If A and $\mathbf { B }$ are $n \times n$ matrices of rank $r$ and $s$ , respectively, then the rank of AB is greater than or equal to $r \ + \ s \ - \ n$ .

• The rank of $\mathbf { A A } ^ { T }$ equals the rank of ${ \bf A } ^ { T } { \bf A }$ , equals the rank of A, equals the rank of ${ \mathbf A } ^ { T }$ .

# B.3 QUADRATIC FORMS

• The rank of the quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is defined as the rank of the matrix A where $\mathbf { Y }$ is a vector and $\textbf { Y } \neq 0$ .

• The quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive definit $e$ if and only if $\mathbf { Y } ^ { T } \mathbf { A Y } > 0$ for all vectors $\mathbf { Y }$ where $\textbf { Y } \neq 0$ .

• A quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive semidefinite if and only if $\mathbf { Y } ^ { T } \mathbf { A Y } \geq 0$ for all $\mathbf { Y }$ , and $\mathbf { Y } ^ { T } \mathbf { A Y } = \mathbf { \zeta } 0$ for some vector $\textbf { Y } \neq 0$ .

• A quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ that may be either positive definite or positive semidefini te is called nonnegative definite .

• The matrix A of a quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive definite (semidefinite) when the quadratic form is positive defini te (semidefinite ).

• If $\mathbf { P }$ is a nonsingular matrix and if $\mathbf { A }$ is positive definite (semidefinite), then $\mathbf { P } ^ { T } \mathbf { A P }$ is positive definite (semidefinit e).

• A necessary and sufficie nt condition for the symmetric matrix A to be positive definite is that there exist a nonsingular matrix $\mathbf { P }$ such that $\mathbf { A } = \bar { \mathbf { P } } \mathbf { P } ^ { T }$ .

• A necessary and sufficient condition that the matrix A be positive definite, where

$$
\textbf { A } = \begin{array} { l } { \left[ \begin{array} { l } { a _ { 1 1 } \ a _ { 1 2 } \dots a _ { 1 n } } \\ { a _ { 2 1 } \ a _ { 2 2 } \dots a _ { 2 n } } \\ { \vdots \quad \vdots \quad \ddots \quad \vdots } \\ { a _ { n 1 } a _ { n 2 } \dots a _ { n n } } \end{array} \right] } \end{array}
$$

is that the following inequalities hold:

$$
\begin{array} { r } { a _ { 1 1 } > 0 , \left| \begin{array} { l } { a _ { 1 1 } a _ { 1 2 } } \\ { a _ { 2 1 } a _ { 2 2 } } \\ { a _ { 2 1 } a _ { 2 2 } } \end{array} \right| > 0 , \ldots \left| \begin{array} { l } { a _ { 1 1 } a _ { 1 2 } \ldots a _ { 1 n } } \\ { a _ { 2 1 } a _ { 2 2 } \ldots a _ { 2 n } } \\ { \vdots \quad \vdots \quad \vdots \quad \ldots \quad \vdots } \\ { a _ { n 1 } a _ { n 2 } \ldots a _ { n n } } \end{array} \right| > 0 . } \end{array}
$$

• If $\mathbf { A }$ is an $m \times n$ matrix of rank $n < m$ , then ${ \bf A } ^ { T } { \bf A }$ is positive definite and $\mathbf { A A } ^ { T }$ is positive semidefinite.

• If $\mathbf { A }$ is an $m \times n$ matrix of rank $k < n$ and $k < m$ , then ${ \bf A } ^ { T } { \bf A }$ and $\mathbf { A A } ^ { T }$ are each positive semidefinite.

• A matrix that may be either positive definite or positive semidefinite is said to be nonnegative defini te.

• If $\mathbf { A }$ and $\mathbf { B }$ are symmetric conformable matrices, A is said to be greater than $\mathbf { B }$ if $\mathbf { A } - \mathbf { B }$ is nonnegative definite.

# B.4 DETERMINANTS

• For each square matrix A, there is a uniquely defined scalar called the determinant of $\mathbf { A }$ and denoted by $| \mathbf { A } |$ .

• The determinant of a diagonal matrix is equal to the product of the diagonal elements.

• If A and $\mathbf { B }$ are $n \times n$ matrices, then $\mathbf { \left| A B \right| } = \mathbf { \left| B A \right| } = \mathbf { \left| A \right| } \mathbf { \left| B \right| }$ .

• If A is singular if and only if $| \mathbf { A } | = 0$ .

• If $\mathbf { C }$ is an $n \ \times \ n$ matrix such that ${ \bf C } ^ { T } { \bf C } \ = \ { \bf I }$ , then $\mathbf { C }$ is said to be an orthogonal matrix, and ${ \bf C } ^ { T } = { \bf C } ^ { - 1 }$ .

• If $\mathbf { C }$ is an orthogonal matrix, then $| { \bf C } | = + 1$ or $| { \bf C } | = - 1$

• If $\mathbf { C }$ is an orthogonal matrix, then $| \mathbf { C } ^ { T } \mathbf { A C } | = | \mathbf { A } |$ .

• The determinant of a positive definit e matrix is positive.

• The determinant of a triangular matrix is equal to the product of the diagonal elements.

• The determinant of a matrix is equal to the product of its eigenvalues.

• $| \mathbf { A } | = | \mathbf { A } ^ { T } |$

• $| \mathbf { A } ^ { - 1 } | = 1 / \left| \mathbf { A } \right|$ , if $| \mathbf { A } | \neq 0$ .

• If $\mathbf { A }$ is a square matrix such that

$$
\mathbf { A } = { \left[ \begin{array} { l } { \mathbf { A } _ { 1 1 } \mathbf { A } _ { 1 2 } } \\ { \mathbf { A } _ { 2 1 } \mathbf { A } _ { 2 2 } } \end{array} \right] }
$$

where $\mathbf { A } _ { 1 1 }$ and $\mathbf { A } _ { 2 2 }$ are square matrices, and if $\mathbf { A } _ { 1 2 } { \mathbf { \Omega } } = { \mathbf { \Omega } } 0$ or $\mathbf { A } _ { 2 1 } ~ = ~ 0$ , then $| \mathbf { A } | = | \mathbf { A } _ { 1 1 } | | \mathbf { A } _ { 2 2 } |$ .

• If ${ \bf A } _ { 1 }$ and ${ \bf A } _ { 2 }$ are symmetric and ${ \bf A } _ { 2 }$ is positive defini te and if ${ \bf A } _ { 1 } ~ - ~ { \bf A } _ { 2 }$ is positive semidefinite (or positive definite), then $| \mathbf { A } _ { 1 } | \geq | \mathbf { A } _ { 2 } |$ .

# B.5 MATRIX TRACE

• The trace of a matrix A, which will be written $\operatorname { t r } \left( \mathbf { A } \right)$ , is equal to the sum of the diagonal elements of $\mathbf { A }$ ; that is,

$$
t r \left( \mathbf { A } \right) = \sum _ { i = 1 } ^ { n } a _ { i i } .
$$

• $\operatorname { t r } ( \mathbf { A } \mathbf { B } ) = \operatorname { t r } ( \mathbf { B } \mathbf { A } )$

• $\operatorname { t r } ( \mathrm { A B C } ) = \operatorname { t r } ( \mathbf { C A B } ) = \operatorname { t r } ( \mathbf { B C A } )$ ; that is, the trace of the product of matrices is invariant under any cyclic permutation of the matrices.

• Note that the trace is defined only for a square matrix.

• If $\mathbf { C }$ is an orthogonal matrix, $\operatorname { t r } \left( \mathbf { C } ^ { T } \mathbf { A C } \right) = \operatorname { t r } \left( \mathbf { A } \right)$ .

# B.6 EIGENVALUES AND EIGENVECTORS

• A characteristic root (eigenvalue) of a $p \ \times \ p$ matrix $\mathbf { A }$ is a scalar $\lambda$ such that $\mathbf { A X } = \lambda \mathbf { X }$ for some vector $\mathbf { X } \neq 0$ .

• The vector $\mathbf { X }$ is called the characteristic vector (eigenvector) of the matrix A.

• The characteristic root of a matrix A can be defined as a scalar $\lambda$ such that $| \mathbf { A } \ - \ \lambda \mathbf { I } | \ = \ 0$ .

• $| \mathbf { A } \ - \ \lambda \mathbf { I } |$ is a pth degree polynomial in $\lambda$ .

• This polynomial is called the characteristic polynomial, and its roots are the characteristic roots of the matrix A.

• The number of nonzero characteristic roots of a matrix A is equal to the rank of A.

• The characteristic roots of $\mathbf { A }$ are identical with the characteristic roots of $\mathbf { C A C } ^ { - 1 }$ . If C is an orthogonal matrix, it follows that A and $\mathbf { C A C } ^ { T }$ have identical characteristic roots; that is, ${ \bf C } ^ { T } = { \bf C } ^ { - 1 }$ .

• The characteristic roots of a symmetric matrix are real; that is, if $\mathbf { A } = \mathbf { A } ^ { T }$ , the characteristic polynomial of $| \mathbf { A } = \lambda \mathbf { I } | = 0$ has all real roots.

• The characteristic roots of a positive definit e matrix A are positive; the characteristic roots of a positive semidefinite matrix are nonnegative.

# B.7 THE DERIVATIVES OF MATRICES AND VECTORS

• Let $\mathbf { X }$ be an $n \times 1$ vector and let $Z$ be a scalar that is a function of $\mathbf { X }$ . The derivative of $Z$ with respect to the vector $\mathbf { X }$ , which will be written $\partial Z / \partial \mathbf { X }$ , will mean the $1 \times n$ row vector∗

$$
\begin{array} { r } { \mathbf { C } \equiv \left[ \frac { \partial Z } { \partial x _ { 1 } } \frac { \partial Z } { \partial x _ { 2 } } \dots \frac { \partial Z } { \partial x _ { n } } \right] . } \end{array}
$$

• If X, C, and $Z$ are as defined previously, then

$$
\partial Z / \partial \mathbf { X } = \mathbf { C } .
$$

• If A and $\mathbf { B }$ are $m \times 1$ vectors, which are a function of the $n \times 1$ vector $\mathbf { X }$ , and we define

$$
\frac { \partial ( \mathbf { A } ^ { T } \mathbf { B } ) } { \partial \mathbf { X } }
$$

to be a row vector as in Eq. (B.7.1), then

$$
\partial ( \mathbf { A } ^ { T } \mathbf { B } ) / \partial \mathbf { X } = \mathbf { B } ^ { T } \frac { \partial \mathbf { A } } { \partial \mathbf { X } } + \mathbf { A } ^ { T } \frac { \partial \mathbf { B } } { \partial \mathbf { X } }
$$

where

$$
\frac { \partial \mathbf { A } } { \partial \mathbf { X } }
$$

is an $m \times n$ matrix whose $i j$ element is

$$
\frac { \partial A _ { i } } { \partial X _ { j } }
$$

and

$$
\frac { \partial ( \mathbf { A } ^ { T } \mathbf { B } ) } { \partial \mathbf { X } }
$$

is a $1 \times n$ row vector.†

• If $\mathbf { A }$ is an $m \times 1$ vector that is a function of the $n \times 1$ vector $\mathbf { X }$ , and $W$ is an $m \times m$ symmetric matrix such that

$$
Z = \mathbf { A } ^ { T } W \mathbf { A } = \mathbf { A } ^ { T } W ^ { 1 / 2 } W ^ { 1 / 2 } \mathbf { A } .
$$

Let ${ \bf B } \equiv W ^ { 1 / 2 } { \bf A }$ , then

$$
Z = \mathbf { B } ^ { T } \mathbf { B } .
$$

From Eq. (B.7.3)

$$
\frac { \partial Z } { \partial \mathbf { X } } = 2 \mathbf { B } ^ { T } \frac { \partial \mathbf { B } } { \partial \mathbf { X } }
$$

where

$$
\frac { \partial { \bf B } } { \partial { \bf X } } = W ^ { 1 / 2 } \frac { \partial { \bf A } } { \partial { \bf X } } .
$$

• Let A be a $p \times 1$ vector, $\mathbf { B }$ be a $q \times 1$ vector, and $C$ be a $p \ \times \ q$ matrix whose $i j ^ { \mathrm { t h } }$ element equals $c _ { i j }$ . Let

$$
Z = \mathbf { A } ^ { T } C \mathbf { B } \ = \ \sum _ { m = 1 } ^ { q } \sum _ { n = 1 } ^ { p } a _ { n } c _ { n m } b _ { m } .
$$

Then $\partial Z / \partial C = \mathbf { A B } ^ { T }$ .

Proof: $\partial Z / \partial C$ will be a $p \ \times \ q$ matrix whose $i j ^ { \mathrm { t h } }$ element is $\partial Z / \partial c _ { i j }$

Assuming that $C$ is not symmetric and that the elements of $C$ are independent,

$$
\frac { \partial Z } { \partial c _ { i j } } \ : = \ : \frac { \partial \ : \left( \displaystyle \sum _ { m = 1 } ^ { q } \ : \sum _ { n = 1 } ^ { p } a _ { n } c _ { n m } b _ { m } \right) } { \partial c _ { i j } } \ : = \ : a _ { i } \ : b _ { j } .
$$

Thus the $i j ^ { \mathrm { t h } }$ element of $\partial Z / \partial C$ is $a _ { i } b _ { j }$ . Therefore, it follows that

$$
\frac { \partial Z } { \partial C } = \mathbf { A B } ^ { T } .
$$

• The derivative of a matrix product with respect to a scalar is given by

$$
{ \frac { d } { d t } } \left\{ \mathbf { A } ( t ) \mathbf { B } ( t ) \right\} = { \frac { d \mathbf { A } ( t ) } { d t } } \mathbf { B } ( t ) + \mathbf { A } ( t ) { \frac { d \mathbf { B } ( t ) } { d t } } .
$$

See Graybill (1961) for additional discussion of the derivatives of matrices and vectors.

# B.8 MAXIMA AND MINIMA

• If $\begin{array} { r c l } { y } & { = } & { f \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right) } \end{array}$ is a function of $n$ variables and if all partial derivatives $\partial y / \partial x _ { i }$ are continuous, then $y$ attains its maxima and minima only at the points where

$$
{ \frac { \partial y } { \partial x _ { 1 } } } = { \frac { \partial y } { \partial x _ { 2 } } } = \ldots = { \frac { \partial y } { \partial x _ { n } } } = 0 .
$$

• If $f \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right)$ is such that all the firs t and second partial derivatives are continuous, then at the point where

$$
{ \frac { \partial f } { \partial { x } _ { 1 } } } = { \frac { \partial f } { \partial { x } _ { 2 } } } = \ldots = { \frac { \partial f } { \partial { x } _ { n } } } = 0
$$

the function has

– a minimum, if the matrix $\mathbf { K }$ , where the $i j$ th element of $\mathbf { K }$ is $\partial ^ { 2 } f / \partial x _ { i } \partial x _ { j }$ , is positive definite.   
– a maximum, if the matrix $- \mathbf { K }$ is positive definit e.

In these two theorems on maxima and minima, remember that the $x _ { i }$ are independent variables.

• If the $x _ { i }$ are not independent, that is, there are constraints relating them, we use the method of Lagrange multipliers. Suppose that we have a function $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ we wish to maximize (or minimize) subject to the constraint that $h ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0$ . The equation $h = 0$ describes a surface in space and the problem is one of maximizing $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ as $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ vary on the curve of intersection of the two surfaces. At a maximum point the derivative of $f$ must be zero along the intersection curve; that is, the directional derivative along the tangent must be zero. The directional derivative is the component of the vector $\nabla f$ along the tangent. Hence, $\nabla f$ must lie in a plane normal to the intersection curve at this point. This plane must also contain $\nabla h$ ; that is, $\nabla f$ and $\nabla h$ are coplanar at this point. Hence, there must exist a scalar $\lambda$ such that

$$
\nabla f + \lambda \nabla h = 0
$$

at the maximum point. If we define

$$
F \equiv f + \lambda h
$$

then Eq. (B.8.3) is equivalent to $\nabla F = 0$ . Hence,

$$
{ \frac { \partial F } { \partial x _ { 1 } } } = { \frac { \partial F } { \partial x _ { 2 } } } = \cdots = { \frac { \partial F } { \partial x _ { n } } } = 0 .
$$

These $n$ equations together with $h = 0$ provide us with $n + 1$ equations and $n + 1$ unknowns $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , \lambda )$ . We have assumed that all first partial derivatives are continuous and that $\partial h / \partial x _ { i } \neq 0$ for all $i$ at the point.

• If there are additional constraints we introduce additional Lagrange multipliers in Eq. (B.8.3); for example,

$$
\nabla f + \lambda _ { 1 } \nabla h _ { 1 } + \lambda _ { 2 } \nabla h _ { 2 } + \cdot \cdot \cdot \lambda _ { k } \nabla h _ { k } = 0 .
$$

# B.9 USEFUL MATRIX INVERSION THEOREMS

Theorem 1: Let $\mathbf { A }$ and $\mathbf { B }$ be $n \ \times \ n$ positive definite (PD) matrices. If $\mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 }$ is PD, then $\mathbf { A } + \mathbf { B }$ is PD and

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } ^ { - 1 }
$$

$$
\mathbf { \Sigma } = \mathbf { A } ^ { - 1 } \left( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \right) ^ { - 1 } \mathbf { B } ^ { - 1 } .
$$

Proof: From the identity

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } \ : = \ : [ \mathbf { A } \left( \mathbf { A } ^ { - 1 } \ : + \ : \mathbf { B } ^ { - 1 } \right) \mathbf { B } ] ^ { - 1 } \ : = \ : \mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } \ : + \ : \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } ^ { - 1 }
$$

or

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = [ \mathbf { B } ( \mathbf { B } ^ { - 1 } + \mathbf { A } ^ { - 1 } ) \mathbf { A } ] ^ { - 1 } = \mathbf { A } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { B } ^ { - 1 } .
$$

Theorem 2: Let $\mathbf { A }$ and $\mathbf { B }$ be $n \times n$ PD matrices. If $\mathbf { A } + \mathbf { B }$ is PD, then $\mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 }$ and $\mathbf { I } + \mathbf { B } \mathbf { A } ^ { - 1 }$ are PD and

$$
\begin{array} { r } { ( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } } \\ { = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } ( \mathbf { I } + \mathbf { B } \mathbf { A } ^ { - 1 } ) ^ { - 1 } \mathbf { B } \mathbf { A } ^ { - 1 } . } \end{array}
$$

Proof: From the identity

$$
\mathbf { A } ^ { - 1 } = ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) - \mathbf { B } ^ { - 1 }
$$

premultiply by $\mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 }$ and use Theorem 1

$$
\begin{array} { r l } & { \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { A } ^ { - 1 } = \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) } \\ & { \qquad - \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { B } ^ { - 1 } } \\ & { \qquad = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } \big [ \mathbf { A } ^ { - 1 } \big ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } \big ) \big ] ^ { - 1 } \mathbf { B } ^ { - 1 } } \\ & { \qquad = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } \big ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } . } \end{array}
$$

The left-hand side of this equation is $( \mathbf { A } + \mathbf { B } ) ^ { - 1 }$ (from Theorem 1). Hence,

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } .
$$

Theorem 3: If $\mathbf { A }$ and $\mathbf { B }$ are PD matrices of order $n$ and $m$ , respectively, and if $\mathbf { C }$ is of order $n \times m$ , then

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } = \mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ^ { - 1 }
$$

provided the inverse exists.

Proof: From the identity

$$
\mathbf { C } ^ { T } ( \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } + \mathbf { I } ) ( \mathbf { I } + \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } ) ^ { - 1 } \equiv \mathbf { C } ^ { T }
$$

we have

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } + \mathbf { C } ^ { T } ) ( \mathbf { A } ^ { - 1 } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ) ^ { - 1 } = \mathbf { C } ^ { T }
$$

or

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) \mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B } \mathbf { C } ^ { T } ) ^ { - 1 } \mathbf { A } = \mathbf { C } ^ { T } .
$$

Now premultiply by $( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 }$ and postmultiply by $\mathbf { A } ^ { - 1 }$ , which yields

$$
\mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ^ { - 1 } = ( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } .
$$

Theorem 4: The Schur Identity or insideout rule. If $\mathbf { A }$ is a PD matrix of order $n$ , and if $\mathbf { B }$ and $\mathbf { C }$ are any conformable matrices such that BC is order $n$ , then

$$
( \mathbf { A } + \mathbf { B C } ) ^ { - 1 } = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } \mathbf { B } ( \mathbf { I } + \mathbf { C A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C A } ^ { - 1 } .
$$

Proof: Define

$$
\mathbf { X } = ( \mathbf { A } + \mathbf { B } \mathbf { C } ) ^ { - 1 } .
$$

Then

$$
\begin{array} { r } { \left( \mathbf { A } + \mathbf { B C } \right) \mathbf { X } = \mathbf { I } } \\ { \mathbf { A X } + \mathbf { B C X } = \mathbf { I } . } \end{array}
$$

Solve Eq. (B.9.5) for CX. First multiply by ${ { \bf A } ^ { - 1 } }$ to yield

$$
\mathbf { X } + \mathbf { A } ^ { - 1 } \mathbf { B } \mathbf { C } \mathbf { X } = \mathbf { A } ^ { - 1 } .
$$

Premultiply Eq. (B.9.6) by $\mathbf { C }$

$$
\mathbf { C } \mathbf { X } + \mathbf { C } \mathbf { A } ^ { - 1 } \mathbf { B } \mathbf { C } \mathbf { X } = \mathbf { C } \mathbf { A } ^ { - 1 } .
$$

Then

$$
\mathbf { C } \mathbf { X } = ( \mathbf { I } + \mathbf { C } \mathbf { A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C } \mathbf { A } ^ { - 1 } .
$$

Substitute Eq. (B.9.7) into Eq. (B.9.6) to yield

$$
\mathbf { X } = ( \mathbf { A } + \mathbf { B C } ) ^ { - 1 } = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } \mathbf { B } ( \mathbf { I } + \mathbf { C A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C A } ^ { - 1 } .
$$

# B.10 REFERENCE

Graybill, F. A., An Introduction to Linear Statistical Models, McGraw-Hill, New York, 1961.

# Appendix C

# Equations of Motion

# C.1 LAGRANGE PLANETARY EQUATIONS

If the perturbing force $\mathbf { f }$ is conservative, it follows that f is derivable from a disturbing function, $D$ , such that $\mathbf { f } = \nabla D$ . The force f will produce temporal changes in the orbit elements that can be expressed by Lagrange’s Planetary Equations (e.g., Kaula, 1966):

$$
\begin{array} { r l } & { \frac { d a } { d t } = \frac { 2 } { n a } \frac { \partial D } { \partial M } } \\ & { \frac { d e } { d t } = \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { n a ^ { 2 } e } \left( ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \frac { \partial D } { \partial M } - \frac { \partial D } { \partial \omega } \right) } \\ & { \frac { d i } { d t } = \frac { 1 } { h \sin i n } \left( \cos i \frac { \partial D } { \partial \omega } - \frac { \partial D } { \partial \Omega } \right) } \\ & { \frac { d \Omega } { d l } = \frac { 1 } { h \sin i n } \frac { \partial D } { \partial i } } \\ & { \frac { d \omega } { d t } = - \frac { \cos i } { h \sin i n } \frac { \partial D } { \partial i } + \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { n a ^ { 2 } e } \frac { \partial D } { \partial e } } \\ & { \frac { d M } { d t } = n - \frac { 1 - e ^ { 2 } } { n a ^ { 2 } e } \frac { \partial D } { \partial e } - \frac { 2 } { n a } \frac { \partial D } { \partial i } . } \end{array}
$$

Note that $h = n a ^ { 2 } [ 1 - e ^ { 2 } ] ^ { 1 / 2 }$ .

# C.2 GAUSSIAN FORM

If the perturbing force f is expressed as

$$
\mathbf { f } = \hat { R } \overline { { u } } _ { r } + \hat { T } \overline { { u } } _ { T } + \hat { N } \overline { { u } } _ { n }
$$

where the unit vectors are defined by the $R T N$ directions (radial, along-track, and cross-track) and $\hat { R } , \hat { T } , \hat { N }$ represent force components, the temporal changes in orbit elements can be expressed in the Gaussian form of Lagrange’s Planetary Equations (e.g., Pollard, 1966) as:

$$
\begin{array} { r l } & { \frac { d \delta } { d t } = \frac { 2 e ^ { 2 \pi \epsilon } } { h } \sin \hat { t } + \frac { 2 e ^ { 2 \pi \epsilon } h } { \mu \nu ^ { 2 } } } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { h } \Big [ i \sin \hat { t } h + \hat { T } \big ( e + 2 \cos \hat { t } + c \cos ^ { 2 } \hat { t } / \mathcal { A } ( 1 + c \cos \hat { t } ) \big ) } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { - \frac { d \delta } { d t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { \frac { d \delta } { d t } - \frac { 1 } { h } \sin \hat { t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { \mu \nu } \cos \hat { t } / \mathcal { A } - \sin ( \omega + f ) / \mathcal { A } } \\ & { \quad \quad + \frac { ( d \delta ) } { d t } + \eta \theta \sin \hat { t } / \mathcal { A } } \\ & { \frac { d \mathcal { A } } { d t } = - \frac { 1 } { \mu \nu } \Big ( \frac { 2 } { \pi } - \frac { 1 - e ^ { 2 \pi \epsilon } } { e } \operatorname* { s u p } \Big ( \hat { T } / \mathcal { A } ( 1 + c \cos \hat { t } ) \Big ) \hat { \mathcal { A } } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

The Gaussian form applies to either conservative or nonconservative forces.

# C.3 REFERENCES

Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, MA, 1966 (republished by Dover Publications, New York, 2000).

Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1966.

# Appendix D

# Constants

# D.1 PHYSICAL CONSTANTS∗

The speed of light is an important fundamental constant since it effectively defines the length scale in a range measurement. As described in Chapter 3, the range measurement actually is based on a measurement of the time required for a signal to travel from the transmitter to the receiver. This time interval measurement is converted into a distance measurement (range) using the speed of light, $c$ . The value of $c$ was adopted by the International Astronomical Union (IAU) in 1976, to be a defining constant with the value

$$
c = 2 9 9 , 7 9 2 , 4 5 8 \mathrm { ~ m } \mathrm { s } ^ { - 1 } .
$$

The constant of gravitation, $G$ , is experimentally determined. A recent value is (Mohr and Taylor, 2003)

$$
G = 6 . 6 7 3 \times 1 0 ^ { - 1 1 } \pm 1 . 0 \times 1 0 ^ { - 1 3 } \mathrm { m ^ { 3 } \ k g ^ { - 1 } \ s ^ { - 2 } } .
$$

The IAU (1976) System of Astronomical Constants can be found in The Astronomical Almanac for the Year 2000 on pages K6 and K7. Updated constants are given by Seidelmann (1992) and McCarthy (1996).

# D.2 EARTH CONSTANTS

For an Earth-orbiting satellite, the normalized gravity coefficients $\hat { C } _ { l m }$ and $\bar { S } _ { l m }$ ), $G M$ , and $a _ { e }$ are required. Recent determinations include the WGS-84 (DMA, 1987), JGM-3 field (Tapley et al., 1996), EGM-96 (Lemoine et al., 1998),

and the GRIMS-C1 (Gruber et al., 2000). The degree and order eight subset of JGM-3 is given in the Table D.1 with standard deviations. Conversion of normalized coefficients to conventional coefficients can be accomplished by:

$$
\begin{array} { l } { { C _ { l m } = N _ { l m } \bar { C } _ { l m } } } \\ { { S _ { l m } = N _ { l m } \bar { S } _ { l m } } } \\ { { N _ { l m } = \sqrt { \displaystyle \frac { ( l - m ) ! ( 2 l + 1 ) ( 2 - \delta _ { 0 m } ) } { ( l + m ) ! } } } } \end{array}
$$

where $\delta _ { 0 m }$ is the Kronecker delta function, which is zero when $m$ is not zero, otherwise it is one. Furthermore, for zonal harmonics, the commonly used $J _ { \ell }$ correspond to $m = 0$ , and

$$
J _ { l } = - C _ { l 0 } .
$$

The ellipsoidal model of the Earth was described in Chapter 2. Current ellipsoid parameters adopted by the IERS (McCarthy, 1996) are:

$$
a _ { e } = 6 3 7 8 1 3 6 . 4 9 \pm 0 . 1 \mathrm { m }
$$

$$
1 / f = 2 9 8 . 2 5 6 4 5 \pm 0 . 0 0 0 0 1 .
$$

# D.3 LUNAR, SOLAR, AND PLANETARY MASSES

Additional parameters required for the description of satellite motion include the gravitational parameters for the Sun, Moon, and planets. The values that are used with the planetary ephemerides, such as DE-405 (Standish, et al., 1997), are given in Table D.2. Additional information can be found in McCarthy (1996), Seidelmann (1992), and Standish et al. (1997). All mass parameters have been determined from observations; consult the references for uncertainties.

Table D.1 JGM-3 Earth Gravity Model   

<table><tr><td>lm</td><td>T</td><td>S</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>啦</td><td>i</td></tr><tr><td>20</td><td>-0.48416954845647E-03</td><td>0.00000000000000E+00</td><td>0.4660E-10</td><td>0.0000E+00</td></tr><tr><td>30</td><td>0.95717059088800E-06</td><td>0.00000000000000E+00</td><td>0.3599E-10</td><td>0.0000E+00</td></tr><tr><td>40</td><td>0.53977706835730E-06</td><td>0.00000000000000E+00</td><td>0.1339E-09</td><td>0.0000E+00</td></tr><tr><td>50</td><td>0.68658987986543E-07</td><td>0.00000000000000E+00</td><td>0.8579E-10</td><td>0.0000E+00</td></tr><tr><td>60</td><td>-0.14967156178604E-06</td><td>0.00000000000000E+00</td><td>0.2428E-09</td><td>0.0000E+00</td></tr><tr><td>70</td><td>0.90722941643232E-07</td><td>0.00000000000000E+00</td><td>0.2604E-09</td><td>0.0000E+00</td></tr><tr><td>80</td><td>0.49118003174734E-07</td><td>0.00000000000000E+00</td><td>0.3996E-09</td><td>0.0000E+00</td></tr><tr><td>2 1</td><td>-0.18698764000000E-09</td><td>0.11952801000000E-08</td><td>0.0000E+00</td><td>0.0000E+00</td></tr><tr><td>31</td><td>0.20301372055530E-05</td><td>0.24813079825561E-06</td><td>0.1153E-09</td><td>0.1152E-09</td></tr><tr><td>41</td><td>-0.53624355429851E-06</td><td>-0.47377237061597E-06</td><td>0.8693E-10</td><td>0.8734E-10</td></tr><tr><td></td><td>-0.62727369697705E-07</td><td>-0.94194632134383E-07</td><td>0.2466E-09</td><td>0.2465E-09</td></tr><tr><td>6</td><td>-0.76103580407274E-07</td><td>0.26899818932629E-07</td><td>0.2702E-09</td><td>0.2752E-09</td></tr><tr><td></td><td>0.28028652203689E-06</td><td>0.94777317813313E-07</td><td>0.4361E-09</td><td>0.4344E-09</td></tr><tr><td></td><td>0.23333751687204E-07</td><td>0.58499274939368E- -07</td><td>0.5070E-09</td><td>0.5137E-09</td></tr><tr><td>2</td><td>0.24392607486563E-05</td><td>-0.14002663975880E- -05</td><td>0.3655E-10</td><td>0.3709E-10</td></tr><tr><td>2</td><td>0.90470634127291E-06</td><td>-0.61892284647849E-06</td><td>0.9378E-10</td><td>0.9375E-10</td></tr><tr><td>42</td><td>0.35067015645938E-06</td><td>0.66257134594268E-06</td><td>0.1559E-09</td><td>0.1560E-09</td></tr><tr><td></td><td>0.65245910276353E-06</td><td>-0.32333435244435E-06</td><td>0.2392E-09</td><td>0.2398E-09</td></tr><tr><td>62</td><td>0.48327472124892E-07</td><td>-0.37381591944355E-06</td><td>0.3145E-09</td><td>0.3160E-09</td></tr><tr><td>72</td><td>0.32976022742410E-06</td><td>0.93193696831045E-07</td><td>0.4635E-09</td><td>0.4587E-09</td></tr><tr><td>82</td><td>0.80070663931587E-07</td><td>0.65518559097464E-07</td><td>0.5185E-09</td><td>0.5323E-09</td></tr><tr><td>33</td><td>0.72114493982309E-06</td><td>0.14142039847354E-05</td><td>0.5755E-10</td><td>0.5720E-10</td></tr><tr><td>43</td><td>0.99086890577441E-06</td><td>-0.20098735484731E-06</td><td>0.7940E-10</td><td>0.7942E-10</td></tr><tr><td>53</td><td>-0.45183704808780E-06</td><td>-0.21495419346421E-06</td><td>0.1599E-09</td><td>0.1616E-09</td></tr><tr><td>63</td><td>0.57020965757974E-07</td><td>0.88894738008251E-08</td><td>0.2598E-09</td><td>0.2574E-09</td></tr><tr><td>73</td><td>0.25050152675038E-06</td><td>-0.21732010845254E-06</td><td>0.3656E-09</td><td>0.3736E-09</td></tr><tr><td>83</td><td>-0.19251764331400E-07</td><td>-0.86285836534248E-07</td><td>0.4947E-09</td><td>0.4918E-09</td></tr><tr><td>44</td><td>-0.18848136742527E-06</td><td>0.30884803690355E-06</td><td>0.7217E-10</td><td>0.7228E-10</td></tr><tr><td>54</td><td>-0.29512339302196E-06</td><td>0.49741427230934E-07</td><td>0.9264E-10</td><td>0.9288E-10</td></tr><tr><td>64</td><td>-0.86228032619800E-07</td><td>-0.47140511232148E-06</td><td>0.1656E-09</td><td>0.1663E-09</td></tr><tr><td>74</td><td>-0.27554096307403E-06</td><td>-0.12414151248516E-06</td><td>0.2665E-09</td><td>0.2656E-09</td></tr><tr><td>84</td><td>-0.24435806439297E-06</td><td>0.69857074850431E-07</td><td>0.4033E-09</td><td>0.4063E-09</td></tr><tr><td>55</td><td>0.17483157769990E-06</td><td>-0.66939293724911E-06</td><td>0.8139E-10</td><td>0.8131E-10</td></tr><tr><td>65</td><td>-0.26711227171966E-06</td><td>-0.53641016466390E-06</td><td>0.8465E-10</td><td>0.8510E-10</td></tr><tr><td>75</td><td>0.16440038146411E-08</td><td>0.18075335233506E-07</td><td>0.1832E-09</td><td>0.1835E-09</td></tr><tr><td>85</td><td>-0.25498410010257E-07</td><td>0.89090297494640E-07</td><td>0.2586E-09</td><td>0.2571E-09</td></tr><tr><td>66</td><td>0.95016518338557E-08</td><td>-0.23726147889522E-06</td><td>0.8021E-10</td><td>0.8081E-10</td></tr><tr><td>76</td><td>-0.35884263307918E-06</td><td>0.15177808443426E-06</td><td>0.5899E-10</td><td>0.5913E-10</td></tr><tr><td>86</td><td>-0.65859353864388E-07</td><td>0.30892064157956E-06</td><td>0.1566E-09</td><td>0.1569E-09</td></tr><tr><td>77</td><td>0.13795170564076E-08</td><td>0.24128594080773E-07</td><td>0.9709E-10</td><td>0.9747E-10</td></tr><tr><td>87</td><td>0.67262701848734E-07</td><td>0.74813196768710E-07</td><td>0.9308E-10</td><td>0.9378E-10</td></tr><tr><td>88</td><td>-0.12397061395498E-06</td><td>0.12044100668766E-06</td><td>0.1379E-09</td><td>0.1384E-09</td></tr></table>

$G M _ { \mathrm { E a r t h } } = 3 . 9 8 6 0 0 4 4 1 5 \times 1 0 ^ { 1 4 } \pm 8 \times 1 0 ^ { 5 } \mathrm { m } ^ { 3 } \mathrm { s } ^ { - 2 }$ $a _ { e } = 6 3 7 8 1 3 6 . 3 \ : \mathrm { m }$

Table D.2   
Lunar, Solar and Planetary Masses   

<table><tr><td>Planet</td><td>GM (m³ s-2)</td></tr><tr><td>Mercury</td><td>2.203208 × 1013</td></tr><tr><td>Venus</td><td>3.248586 × 1014</td></tr><tr><td>Mars</td><td>4.282831 × 1013</td></tr><tr><td>Jupiter</td><td>1.267128 × 1017</td></tr><tr><td>Saturn</td><td>3.794063× 1016</td></tr><tr><td>Uranus</td><td>5.794549 ×1015</td></tr><tr><td>Neptune</td><td>6.836534 × 1015</td></tr><tr><td>Pluto</td><td>9.816009 × 1011</td></tr><tr><td>Moon</td><td>4.902801 × 1012</td></tr><tr><td>Sun</td><td>1.327124 × 1020</td></tr></table>

The Earth-Moon mass ratio is 81.30056 and 1 Astronomical Uni $= 1 4 9$ , 597, 870, 691 m, as provided with DE-405.

Note that using the Earth-Moon mass ratio in Table D.2 yields $G M _ { \mathrm { M o o n } } =$ $4 . 9 0 2 8 0 4 \times 1 0 ^ { 1 2 } m ^ { 3 } s ^ { - 2 }$ based on the $G M _ { \mathrm { E a r t h } }$ =from JGM-3. The difference with $G M _ { \mathrm { M o o n } }$ 10in Table D.2 is caused by the $G M _ { \mathrm { E a r t h } }$ adopted in DE-405.

# D.4 REFERENCES

Defense Mapping Agency, Department of Defense World Geodetic System 1984, DMA Technical Report 8350.2, Washington, DC, September, 1987.

Gruber, T., A. Bode, C. Reigber, P. Schwintzer, G. Balmino, R. Biancale, J. Lemoine, “GRIM5-C1: Combination solution of the global gravity field to degree and order 120,” Geophys. Res. Ltrs., Vol. 27, No. 24, pp. 4005–4008, December 2000.

Lemoine, F., S. Kenyon, J. Factor, R. Trimmer, N. Pavlis, D. Chinn, C. Cox, S. Klosko, S. Luthcke, M. Torrence, Y. Wang, R. Williamson, E. Pavlis, R. Rapp, and T. Olson, The development of the Joint NASA GSFC and the National Imagery and Mapping Agency (NIMA) Geopotential Model EGM96, NASA/TP–1998–206861, Greenbelt, MD, July 1998.

Le Systeme International d’Unites (SI), Bureau International des Poids et Mesures, Sevres, France, 1991.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Mohr, P. J., and B. Taylor, “The fundamental physical constants,” Physics Today, Vol. 56, No. 8, Supplement, pp. BG6–BG13, August 2003.

Seidelmann, P. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA 1997.

Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3,” J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

# Appendix E

# Analytical Theory for Near-Circular Orbits

# E.1 DESCRIPTION

An analytical theory for the variation of the orbit elements under the influence of the zonal harmonics $J _ { 2 }$ through $J _ { 5 }$ has been developed by Brouwer (1959). This appendix presents a simplificat ion of his equations for the time variation of the orbit elements for a near-circular orbit under the influence of $J _ { 2 }$ . The classical elements $e$ and $\omega$ used by Brouwer have been replaced by $h = e \sin \omega$ and $k = e \cos \omega$ since the argument of perigee is not well defined for a nearcircular orbit. The analytical solutions are given by (Born et al., 2001):

$$
\begin{array} { r l } & { a ( t ) = \hat { a } + k _ { 1 } \cos { 2 \hat { b } } } \\ & { h ( t ) = \hat { k } ( t ) + k _ { 2 } \sin { \hat { \beta } } + k _ { 3 } \sin { 3 \hat { \beta } } } \\ & { k ( \hat { t } ) = \hat { k } ( t ) + k _ { 4 } \cos { \hat { \beta } } + k _ { 3 } \cos { 3 \hat { \beta } } } \\ & { \hat { \iota } ( t ) = \hat { \iota } ( t ) + k _ { 5 } \cos { 2 \hat { \beta } } } \\ & { \Omega ( t ) = \hat { \Omega } + k _ { 6 } \sin { 2 \hat { \beta } } } \\ & { \beta ( \hat { t } ) = \hat { \beta } + k _ { 7 } \sin { 2 \hat { \beta } } + k _ { 8 } ( t - t _ { 0 } ) ^ { 2 } } \\ & { \hat { h } ( t ) = \hat { e } \sin { \hat { \alpha } } } \\ & { \hat { \Omega } - \hat { \Omega } ( t _ { 0 } ) + k _ { 9 } ( t - t _ { 0 } ) } \\ & { \hat { \omega } = \hat { w } ( t _ { 0 } ) + k _ { 1 0 } ( t - t _ { 0 } ) } \\ & { \hat { \beta } = \hat { \beta } ( t _ { 0 } ) + k _ { 1 1 } ( t - t _ { 0 } ) } \end{array}
$$

where $\beta = \omega + M$ and $( ^ { - } )$ represents the mean value of the element. Mean values are given by

$$
\begin{array} { r l } & { \quad \bar { a } = a ( t _ { 0 } ) - K _ { 1 } \cos 2 \beta ( t _ { 0 } ) } \\ & { \quad \bar { h } ( t _ { 0 } ) = \bar { e } \sin \bar { \omega } ( t _ { 0 } ) = h ( t _ { 0 } ) - K _ { 2 } \sin \beta ( t _ { 0 } ) - K _ { 3 } \sin 3 \beta ( t _ { 0 } ) } \\ & { \quad \bar { k } ( t _ { 0 } ) = \bar { e } \cos \bar { \omega } ( t _ { 0 } ) = k ( t _ { 0 } ) - K _ { 4 } \cos \beta ( t _ { 0 } ) - K _ { 3 } \cos 3 \beta ( t _ { 0 } ) } \\ & { \quad \bar { e } = \sqrt { \bar { h } ^ { 2 } ( t _ { 0 } ) + \bar { k } ^ { 2 } ( t _ { 0 } ) } } \\ & { \quad \quad \bar { \omega } ( t _ { 0 } ) = \mathrm { a t a n 2 ~ } \left( \bar { h } ( t _ { 0 } ) , \bar { k } ( t _ { 0 } ) \right) } \\ & { \quad \quad \bar { \tau } = i ( t _ { 0 } ) - K _ { 5 } \cos 2 \beta ( t _ { 0 } ) } \\ & { \quad \quad \sum _ { \bar { \omega } ( t _ { 0 } ) } = \Omega ( t _ { 0 } ) - K _ { 6 } \sin 2 \beta ( t _ { 0 } ) } \\ & { \quad \quad \bar { \beta } ( t _ { 0 } ) = \beta ( t _ { 0 } ) - K _ { 7 } \sin 2 \beta ( t _ { 0 } ) . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { E _ { 1 } = 3 \cdots \gamma _ { 2 } e ^ { 2 \theta } } \\ & { K _ { 3 } = \gamma _ { 2 } ^ { \prime } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 3 } = \frac { 3 } { 2 } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 3 } = \frac { \gamma _ { 1 } } { 2 } e ^ { 2 \theta } } \\ & { K _ { 4 } = \frac { 3 } { 2 } ( 1 6 - \frac { 1 5 } { 2 } \delta ^ { 2 } ) } \\ & { K _ { 4 } = \frac { 3 } { 2 } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 5 } = \frac { 3 } { 2 } \gamma _ { 2 } e ^ { 3 \theta } } \\ & { K _ { 6 } = \frac { 3 } { 2 } \gamma _ { 5 } \theta ^ { 3 } } \\ & { K _ { 7 } = \frac { 3 } { 2 } \gamma _ { 1 } ( 1 - 8 6 \pi ^ { 2 } ) } \\ & { K _ { 8 } = \frac { 3 } { 2 } \theta \gamma _ { 2 } ^ { \prime } ( \gamma _ { 2 } \theta _ { 3 } ^ { 2 } \frac { \theta } { 2 } ) } \\ & { K _ { 8 } = - \frac { 3 } { 8 } \theta \gamma _ { 2 } \theta \gamma _ { 3 } ^ { \prime } } \\ & { K _ { 8 } = - \frac { 3 } { 2 } \theta \gamma _ { 4 } ( 1 - \delta \pi ^ { 2 } ) } \\ & { K _ { 8 } = \frac { 3 } { 2 } \gamma _ { 2 } \theta ( 1 + \delta \pi ^ { 2 } ) } \\ & { K _ { 1 1 } = \pi ^ { 2 } \delta ( 1 + \delta \pi ^ { 2 } ) . } \end{array}
$$

and

$$
\begin{array} { c } { { \displaystyle \gamma _ { 2 } = \frac { J _ { 2 } } { 2 } \left( \frac { R } { \bar { a } } \right) ^ { 2 } } } \\ { { \displaystyle \theta = \cos \bar { \imath } } } \\ { { \displaystyle \delta = \sin \bar { \imath } } } \end{array}
$$

![](images/9038d09aa29a0906ec65d2b9c87fb811e5e0968af63183bd53d6595dc2a9f5d6.jpg)  
Figure E.1.1: Analytical solution results for the QUIKSCAT orbit using Eq. (E.1.1).

$$
\begin{array} { r l } & { \bar { n } { = } \displaystyle \frac { \mu ^ { 1 / 2 } } { \bar { a } ^ { 3 / 2 } } , \qquad \mu { = } G M } \\ & { \rho { = } \mathrm { a v e r a g e ~ a t m o s p h e r i c ~ d e n s i t y ~ a t ~ s a t e l l i t e ~ a l t i t u d e } } \\ & { v _ { \mathrm { r e l } } { = } \mathrm { a v e r a g e ~ v e l o c i t y ~ o f ~ t h e ~ s a t e l l i t e ~ r e l a t i v e ~ t o ~ t h e ~ a t m o s p h e r e } } \end{array}
$$

This representation is based on the solution developed by Brouwer (1959), except for the last term in the $\beta ( t )$ expression, $k _ { 8 } ( t - t _ { 0 } ) ^ { 2 }$ . This quadratic term is introduced to compensate for drag.

Note that it is not necessary to iterate to determine mean values because this is a first-order theory in $J _ { 2 }$ . It is necessary to use $\bar { a }$ to compute $\bar { n }$ in order to avoid an error of $O ( J _ { 2 } )$ in computing $K _ { 1 1 }$ .

Other useful equations are

$$
\begin{array} { l } { \displaystyle { r ( t ) = \frac { a ( t ) \left[ 1 - \left( h ( t ) ^ { 2 } + k ^ { 2 } ( t ) \right) \right] } { 1 + k ( t ) \cos \beta ( t ) + h ( t ) \sin \beta ( t ) } } } \\ { \displaystyle { e ( t ) = \sqrt { h ^ { 2 } ( t ) + k ^ { 2 } ( t ) } } } \end{array}
$$

![](images/0c01e80c6c1dbd32dcbec5f18acbe3368b21b4bf975523f9117f449a55f246af.jpg)  
Figure E.1.2: Difference between QUIKSCAT analytical solutions and numerical integration.

$$
\begin{array} { c } { { \omega ( t ) = \mathrm { a t a n 2 } \left( h ( t ) , k ( t ) \right) } } \\ { { M ( t ) = \beta ( t ) - \omega ( t ) . } } \end{array}
$$

The equation for $r ( t )$ also can be written in terms of the mean elements as follows

$$
\begin{array} { l } { { \displaystyle r ( t ) = \bar { a } [ 1 - \bar { e } \cos \overline { { { M } } } ( t ) ] + \frac { 3 } { 4 } \frac { R ^ { 2 } } { \bar { a } } J _ { 2 } ( 3 \sin ^ { 2 } \bar { \imath } - 2 ) } } \\ { { \displaystyle ~ + \frac { 1 } { 4 } \frac { R ^ { 2 } } { a } J _ { 2 } \sin ^ { 2 } \bar { \imath } \cos 2 \bar { \beta } } } \end{array}
$$

where

$$
\overline { { { { \cal M } } } } ( t ) = \bar { \beta } ( t ) - \bar { \omega } ( t ) .
$$

# E.2 EXAMPLE

Figure E.2.1 presents the classical orbit elements and radius time history for the QUIKSCAT satellite over one day computed by using Eq. (E.1.1). Initial conditions are given on the figure. Fig. E.2.2 presents the differences between the analytical solutions and numerical integration.

We have ignored terms of $O ( e J _ { 2 } )$ and $O ( J _ { 2 } ^ { 2 } )$ in developing this theory. Here the values of $e$ and $J _ { 2 }$ are the same order of magnitude. However, errors of $O ( e J _ { 2 } )$ are dominant since reducing the initial eccentricity to $1 0 ^ { - 4 }$ reduces the periodic errors in the analytical solutions by a factor of two. Secular errors of $O ( J _ { 2 } ^ { 2 } )$ are apparent in $\Omega$ . Including secular rates of $O ( J _ { 2 } ^ { 2 } )$ , given by Brouwer (1959), reduces the RMS error in $\Omega$ by an order of magnitude.

# E.3 REFERENCES

Born, G. H., D. B. Goldstein and B. Thompson, An Analytical Theory for Orbit Determination, J. Astronaut. Sci., Vol. 49, No. 2, pp. 345–361, April–June 2001.

Brouwer, D., “Solutions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

# Appendix F

# Example of State Noise and Dynamic Model Compensation

# F.1 INTRODUCTION

Consider a target particle that moves in one dimension along the $x$ axis in the positive direction.∗ Nominally, the particle’s velocity is a constant $1 0 \mathrm { m / s e c }$ . This constant velocity is perturbed by a sinusoidal acceleration in the $x$ direction, which is unknown and is described by:

$$
\eta ( t ) = \frac { 2 \pi } { 1 0 } \cos \left( \frac { 2 \pi } { 1 0 } t \right) \mathrm { m / s e c } .
$$

The perturbing acceleration, perturbed velocity, and position perturbation (perturbed position—nominal position) are shown in Fig. F.1.1.

A measurement sensor is located at the known position $x = - 1 0 \textrm { m }$ . This sensor takes simultaneous range and range-rate measurements at a frequency of $1 0 ~ \mathrm { H z }$ . The range measurements are corrupted by uncorrelated Gaussian noise having a mean of zero and a standard deviation of $1 \textrm { m }$ . Likewise, the range-rate measurements are corrupted by uncorrelated Gaussian noise having a mean of zero and a standard deviation of $0 . 1 \mathrm { m } / \mathrm { s e c }$ . We want to estimate the state of the particle, with primary emphasis on position accuracy, using these observations given the condition that the sinusoidal perturbing acceleration is unknown. The following estimation results were generated using the extended sequential algorithm discussed in Section 4.7.3.

A simple estimator for this problem incorporates a two-parameter state vector

![](images/de860162f7bdb77f3ed2359709e333db3cc3901164942493f6597dc588634ebd.jpg)  
Figure F.1.1: Perturbed particle motion.

consisting of position and velocity:

$$
{ \bf X } ( t ) = \left[ \begin{array} { l } { x ( t ) } \\ { \dot { x } ( t ) } \end{array} \right] = \left[ \begin{array} { l } { x ( t _ { 0 } ) + \dot { x } ( t _ { 0 } ) ( t - t _ { 0 } ) } \\ { \dot { x } ( t _ { 0 } ) } \end{array} \right] .
$$

The dynamic model assumes constant velocity for the particle motion and does

not incorporate process noise. The state transition matrix for this estimator is:

$$
\Phi ( t , t _ { 0 } ) = { \left[ \begin{array} { l l } { 1 t - t _ { 0 } } \\ { 0 \quad 1 } \end{array} \right] }
$$

and the observation/state mapping matrix is a two-by-two identity matrix:

$$
\widetilde { H } = \left[ \begin{array} { l } { 1 0 } \\ { 0 1 } \end{array} \right] .
$$

Since the sinusoidal acceleration is not included in the dynamic model and the filter has no means of compensation for the dynamic model defici ency, the filter quickly saturates and its estimation performance is poor. Fig. F.1.2 shows the actual position errors along with the one-sigma position standard deviation bounds estimated by the filter . The position error RMS is $0 . 9 6 5 3 \mathrm { ~ m ~ }$ , and only 18.60 percent of the actual position errors are within the estimated one-sigma standard deviation bounds. Fig. F.1.3 shows the corresponding velocity errors and onesigma velocity standard deviation bounds. As with position, the velocity errors are generally well outside the standard deviation bounds.

# F.2 STATE NOISE COMPENSATION

The State Noise Compensation (SNC) algorithm (see Section 4.9) provides a means to improve estimation performance through partial compensation for the unknown sinusoidal acceleration. SNC allows for the possibility that the state dynamics are influenced by a random acceleration. A simple SNC model uses a two-state filter but assumes that particle dynamics are perturbed by an acceleration that is characterized as simple white noise:

$$
\ddot { x } ( t ) = \eta ( t ) = u ( t )
$$

where $u ( t )$ is a stationary Gaussian process with a mean of zero and a variance of $\sigma _ { u } ^ { 2 } \delta ( t - \tau )$ , and $\delta ( t - \tau )$ is the Dirac delta function. The Dirac delta function is not an ordinary function, and to be mathematically rigorous, white noise is a fictiti ous process. However, in linear stochastic models, it can be treated formally as an integrable function. Application of Eq. (4.9.1) to this case results in

$$
{ \Big [ } { \dot { x } } ( t ) { \Big ] } = { \Big [ } 0 1 { \Big ] } { \Big [ } x ( t ) { \Big ] } + { \Big [ } 0 { \Big ] } u ( t )
$$

![](images/f99ba31501d1ce030fed68eff6216639eb24ce835028d6b421d7ca96eaca4d9a.jpg)  
Figure F.1.2: Position errors and estimated standard deviation bounds from the two-state filter without process noise.

where the state propagation matrix A is identified as:

$$
A = { \binom { 0 1 } { 0 0 } }
$$

and the process noise mapping matrix is:

$$
\begin{array} { r } { B = \bigg [ \begin{array} { c } { 0 } \\ { 1 } \end{array} \bigg ] . } \end{array}
$$

The state transition matrix is the same:

$$
\Phi ( t , t _ { 0 } ) = { \Bigg [ } { 1 t - t _ { 0 } } { \Bigg ] } ~ .
$$

![](images/57dffb58609f5d82cd9312900618b40d2ec94c1ada7a07c141232a7af3544e90.jpg)  
Figure F.1.3: Velocity errors and estimated standard deviation bounds from the two-state filter without process noise.

The process noise covariance integral (see Eq. (4.9.44)) needed for the time update of the estimation error covariance matrix at time $t$ is expressed as:

$$
Q _ { \eta } ( t ) = \sigma _ { u } ^ { 2 } \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) B B ^ { T } \Phi ^ { T } ( t , \tau ) d \tau
$$

where

$$
\Phi ( t , \tau ) = \left[ { 1 \left( { t - \tau } \right) } \right] .
$$

Substituting for $B$ and $\Phi ( t , \tau )$ and evaluating results in the process noise covariance matrix:

$$
Q _ { 7 } ( t ) = \sigma _ { u } ^ { 2 } \left[ \frac { 1 } { 3 } ( t - t _ { 0 } ) ^ { 3 } \frac { 1 } { 2 } ( t - t _ { 0 } ) ^ { 2 } \right]
$$

where $t - t _ { 0 }$ is the measurement update interval; that is, $t _ { k } - t _ { k - 1 } = 0 . 1$ sec. The implication of this is that the original deterministic constant velocity model of particle motion is modified to include a random component that is a constantdiffusion Brownian motion process, $\sigma _ { u } ^ { 2 }$ being known as the diffusion coefficient (Maybeck, 1979).

![](images/1ec57391824d6cb269c308f97eae488e5bd07c6541c12de0738d29a35d6019fd.jpg)  
Figure F.2.1: Position errors and estimated standard deviation bounds from the two-state SNC filter .

The magnitude of the process noise covariance matrix and its effect on estimation performance are functions of this diffusion coefficient, hence $\sigma _ { u }$ is a tuning parameter whose value can be adjusted to optimize performance. Figures F.2.1 and F.2.2 show the result of the tuning process. The optimal value of $\sigma _ { u }$ is $0 . 4 2 ~ \mathrm { m / s e c ^ { 3 / 2 } }$ at which the position error RMS is $0 . 1 3 7 8 \mathrm { m }$ and 56.81 percent of the actual position errors fall within the estimated one-sigma standard deviation bounds. The large sinusoidal error signature in both position and velocity displayed by the uncompensated filter is eliminated by SNC.

Note that there is no noticable change in the position standard deviations; however, the velocity standard deviations show a significant increase when process noise is included. This increase in the velocity variances prevents the components of the Kalman gain matrix from going to zero with the attendant saturation of the filte r.

![](images/a8940fa2726c56d42f646b700821056be1280406ede6b579c97190353ccbec65.jpg)  
Figure F.2.2: Velocity errors and estimated standard deviation bounds from the two-state filter with SNC process noise.

# F.3 DYNAMIC MODEL COMPENSATION

A more sophisticated process noise model is provided by the Dynamic Model Compensation (DMC) formulation. DMC assumes that the unknown acceleration can be characterized as a first-order linear stochastic differential equation, commonly known as a Langevin equation:

$$
\dot { \eta } ( t ) + \beta \eta ( t ) = u ( t ) ,
$$

where $u ( t )$ is a white zero-mean Gaussian process as described earlier and $\beta$ is the inverse of the correlation time:

$$
\beta = \frac { 1 } { \tau } .
$$

The solution to this Langevin equation is

$$
\eta ( t ) = \eta _ { 0 } e ^ { - \beta ( t - t _ { 0 } ) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta ( t - \tau ) } u ( \tau ) d \tau .
$$

This is the Gauss-Markov process (more precisely known as an Ornstein-Uhlenbeck process) described in Section 4.9. Note that, unlike SNC, the DMC process noise model yields a deterministic acceleration term as well as a purely random term. The deterministic acceleration can be added to the state vector and estimated along with the velocity and position; the augmented state vector becomes a threestate filter with

$$
\mathbf { X } ( t ) = \left[ \begin{array} { l } { x ( t ) } \\ { \dot { x } ( t ) } \\ { \eta _ { D } ( t ) } \end{array} \right]
$$

where $\eta _ { D } ( t )$ is the deterministic part of $\eta ( t )$ ; that is, $\eta _ { 0 } e ^ { - \beta \left( t - t _ { 0 } \right) }$ . Since the acceleration integrates into velocity and position increments, the dynamic model of the particle’s motion becomes

$$
\mathbf { X } ( t ) = \left[ \begin{array} { c } { x _ { 0 } + \dot { x } _ { 0 } ( t - t _ { 0 } ) + \frac { \eta _ { 0 } } { \beta } ( t - t _ { 0 } ) + \frac { \eta _ { 0 } } { \beta ^ { 2 } } \left( e ^ { - \beta ( t - t _ { 0 } ) } - 1 \right) } \\ { \dot { x } _ { 0 } + \frac { \eta _ { 0 } } { \beta } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) } \\ { \eta _ { 0 } e ^ { - \beta ( t - t _ { 0 } ) } } \end{array} \right] .
$$

The correlation time, $\tau$ , can also be added to the estimated state, resulting in a four-parameter state vector. However, a tuning strategy that works well for many DMC estimation problems is to set $\tau$ to a near-optimal value and hold it constant, or nearly constant, during the estimation span. For simplicity, $\tau$ is held constant in this case, allowing the use of the three-parameter state vector just noted. The observation/state mapping matrix is a simple extension of the two-state case:

$$
\widetilde H = \left[ { 1 0 0 } \right] .
$$

Using the methods described in Example 4.2.3, the state transition matrix is found to be

$$
\Phi ( t , t _ { 0 } ) = \frac { \partial X ( t ) } { \partial X ( t _ { 0 } ) } = \left[ \begin{array} { l l l } { 1 t - t _ { 0 } \frac { 1 } { \beta } ( t - t _ { 0 } ) + \frac { 1 } { \beta ^ { 2 } } \left( e ^ { - \beta ( t - t _ { 0 } ) } - 1 \right) } & { } \\ { 0 } & { 1 } & { \frac { 1 } { \beta } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) } \\ { 0 } & { 0 } & { e ^ { - \beta ( t - t _ { 0 } ) } } \end{array} \right] .
$$

The state propagation matrix for this case is

$$
A = { \left[ \begin{array} { l l } { 0 1 } & { 0 } \\ { 0 0 } & { 1 } \\ { 0 0 } & { - \beta } \end{array} \right] }
$$

and the process noise mapping matrix is

$$
B = { \binom { 0 } { 0 } } \cdot
$$

With these, the process noise covariance integral becomes (in terms of the components of $\Phi ( t , \tau )$ )

$$
\begin{array} { r l } & { Q _ { \eta } ( t ) = \sigma _ { u } ^ { 2 } \times } \\ & { \int _ { t _ { 0 } } ^ { t } \left[ \begin{array} { c c } { \Phi _ { 1 , 3 } ^ { 2 } ( t , \tau ) } & { \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) } \\ { \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) } & { \Phi _ { 2 , 3 } ^ { 2 } ( t , \tau ) } & { \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) } \\ { \Phi _ { 3 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) \Phi _ { 2 , 3 } ( t , \tau ) } & { \Phi _ { 3 , 3 } ^ { 2 } ( t , \tau ) } \end{array} \right] d \tau . } \end{array}
$$

Note that here $\tau$ designates the integration variable, not the correlation time. The expanded, integrated process noise covariance matrix terms follow: position variance:

$$
\begin{array} { l } { { \displaystyle Q _ { \eta 1 , 1 } ( t ) = \sigma _ { u } ^ { 2 } \biggl ( \frac { 1 } { 3 \beta ^ { 2 } } ( t - t _ { 0 } ) ^ { 3 } - \frac { 1 } { \beta ^ { 3 } } ( t - t _ { 0 } ) ^ { 2 } } } \\ { { \displaystyle \qquad + \frac { 1 } { \beta ^ { 4 } } ( t - t _ { 0 } ) ( 1 - 2 e ^ { - \beta ( t - t _ { 0 } ) } ) + \frac { 1 } { 2 \beta ^ { 5 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) \biggr ) } } \end{array}
$$

position/velocity covariance:

$$
\begin{array} { r } { Q _ { \eta 1 , 2 } ( t ) = \sigma _ { u } ^ { 2 } \bigg ( \frac { 1 } { 2 \beta ^ { 2 } } ( t - t _ { 0 } ) ^ { 2 } - \frac { 1 } { \beta ^ { 3 } } ( t - t _ { 0 } ) ( 1 - e ^ { - \beta ( t - t _ { 0 } ) } ) } \\ { + \frac { 1 } { \beta ^ { 4 } } ( 1 - e ^ { - \beta ( t - t _ { 0 } ) } ) - \frac { 1 } { 2 \beta ^ { 4 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) \bigg ) } \end{array}
$$

position/acceleration covariance:

$$
Q _ { \eta 1 , 3 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { 2 \beta ^ { 3 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) - \frac { 1 } { \beta ^ { 2 } } ( t - t _ { 0 } ) e ^ { - \beta ( t - t _ { 0 } ) } \right)
$$

velocity variance:

$$
Q _ { \eta 2 , 2 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { \beta ^ { 2 } } ( t - t _ { 0 } ) - \frac { 2 } { \beta ^ { 3 } } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) + \frac { 1 } { 2 \beta ^ { 3 } } \left( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) \right)
$$

velocity/acceleration covariance:

$$
Q _ { \eta 2 , 3 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { 2 \beta ^ { 2 } } \left( 1 + e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) - \frac { 1 } { \beta ^ { 2 } } e ^ { - \beta ( t - t _ { 0 } ) } \right)
$$

![](images/b1b7e4b7cb843cd05ef9da9dce3721d0d289e042724c6cf6d4b34621a0452f02.jpg)  
Figure F.3.1: Position errors and estimated standard deviation bounds from the three-state DMC filter .

acceleration variance:

$$
Q _ { \eta 3 , 3 } ( t ) = \frac { \sigma _ { u } ^ { 2 } } { 2 \beta } \left( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) .
$$

With $\tau$ fix ed at 200.0 sec (or $\beta = 0 . 0 0 5 \ \sec ^ { - 1 } ,$ ), the optimal value of $\sigma _ { u }$ is 0.26 $\mathrm { { m } / \mathrm { { s e c } ^ { 5 / 2 } } }$ . This combination produces the position error results shown in Fig. F.3.1. The position error RMS is $0 . 1 3 7 6 \mathrm { ~ m ~ }$ and 56.81 percent of the actual position errors are within the estimated one-sigma standard deviation bounds. Although not shown here, the plot of velocity errors exhibits a behavior similar to the velocity errors for the SNC filt er.

Figure F.3.2 is a plot of the RMS of the position error as a function of $\sigma _ { u }$ for both the two-state SNC filter and the three-state DMC filte r. Although the optimally tuned SNC fil ter approaches the position error RMS performance of the DMC filt er, it is much more sensitive to tuning. DMC achieves very good performance over a much broader, suboptimal range of $\sigma _ { u }$ values than does SNC.

![](images/2a4347a4a9fd5f4445d0d42e86046bc6b9137c3adc5bfae7f14b2fc759a32db7.jpg)  
Figure F.3.2: RMS Position error as a function of $\sigma _ { u }$ for the two-state SNC and three-state DMC filters.

This is a significant advantage for DMC applications where the true state values are not available to guide the tuning effort, as they are in a simulation study, and the precisely optimal tuning parameter values are not known.

Aside from this, the DMC filter also provides a direct estimate of the unknown, unmodeled acceleration. This information could, in turn, be useful in improving the filter dynamic model. Figure F.3.3 is a plot of the estimated and true sinusoidal accelerations. This plot shows excellent agreement between the estimated and true accelerations; their correlation coefficient is 0.9306.

# F.4 REFERENCE

Maybeck, P. S., Stochastic Models, Estimation and Control, Vol. 1, Academic Press, 1979.

![](images/7bfae3b384cb1cd49da689312e9faa6718957e69fb58f21211d785763e5e0b76.jpg)  
Figure F.3.3: Estimated and true sinusoidal accelerations.

Appendix G

# Solution of the Linearized Equations of Motion

# G.1 INTRODUCTION

The equations of motion for a satellite are given by:

$$
\begin{array} { r } { \dot { \mathbf { X } } = F ( \mathbf { X } , t ) , } \end{array}
$$

where

$$
\mathbf { X } = [ X Y Z \dot { X } \dot { Y } \dot { Z } \beta ] ^ { T } .
$$

$\mathbf { X }$ is the state vector containing six position and velocity elements and $\beta$ , an $m$ vector, represents all constant parameters such as gravity and drag coeffic ients that are to be solved for. Hence, $\mathbf { X }$ is a vector of dimension $n = m + 6$ .

Equation (G.1.1) can be linearized by expanding about a reference state vector denoted by $\mathbf { X } ^ { * }$ ,

$$
\dot { \mathbf { X } } ( t ) = \dot { \mathbf { X } } ^ { * } ( t ) + \left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \left( \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right) + \mathrm { h . o . t . }
$$

The $^ *$ indicates that the quantity is evaluated on the reference state. By ignoring higher-order terms (h.o.t.) and defining

$$
\mathbf { x } ( t ) \equiv \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) ,
$$

we can write Eq. (G.1.2) as

$$
\dot { \mathbf { x } } ( t ) = \left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \mathbf { x } ( t ) .
$$

Define

$$
A ( t ) \equiv \left[ \frac { \partial \dot { \bf X } ( t ) } { \partial { \bf X } ( t ) } \right] ^ { * } ,
$$

then

$$
\dot { \mathbf { x } } ( t ) = \boldsymbol { A } ( t ) \mathbf { x } ( t ) .
$$

Equation (G.1.5) is a linear system of first -order differential equations with $A ( t )$ being an $n \times n$ time varying matrix evaluated on the known reference state $\mathbf { X } ^ { * } ( t )$ . Note that $\dot { \boldsymbol { { \beta } } } = 0$ , so that

$$
\frac { \partial \dot { \boldsymbol { \beta } } } { \partial \mathbf { X } ( t ) } = 0 .
$$

Because Eq. (G.1.4) is linear† and of the form

$$
\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t ) ,
$$

the solution can be written as

$$
{ \bf x } ( t ) = \frac { \partial { \bf x } ( t ) } { \partial { \bf x } _ { 0 } } { \bf x } _ { 0 } .
$$

It is also true that

$$
\mathbf { x } ( t ) = \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } \mathbf { x } _ { 0 } .
$$

This follows from the fact that the reference state does not vary in this operation,

$$
\begin{array} { c } { \displaystyle \frac { \partial \mathbf { x } ( t ) } { \partial \mathbf { x } _ { 0 } } = \frac { \partial \left( \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right) } { \partial ( \mathbf { X } _ { 0 } - \mathbf { X } _ { 0 } ^ { * } ) } } \\ { \displaystyle = \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } . } \end{array}
$$

The conditions under which Eq. (G.1.6) satisfies Eq. (G.1.4) are demonstrated as follows. First define

$$
\Phi ( t , t _ { 0 } ) \equiv \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } .
$$

Then Eq. (G.1.6) can be written as

$$
\begin{array} { r } { { \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf x } _ { 0 } . } \end{array}
$$

Differentiating Eq. (G.1.8) yields

$$
\dot { { \bf x } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) { \bf x } _ { 0 } .
$$

Equating Eq. (G.1.4) and Eq. (G.1.9) yields

$$
\frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \mathbf { x } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) \mathbf { x } _ { 0 } .
$$

Substituting Eq. (G.1.8) for ${ \bf x } ( t )$ into Eq. (G.1.10) results in

$$
\left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \Phi ( t , t _ { 0 } ) \mathbf { x } _ { 0 } = \dot { \Phi } ( t , t _ { 0 } ) \mathbf { x } _ { 0 } .
$$

Equating the coefficie nts of $\mathbf { x } _ { \mathrm { 0 } }$ in this equation yields the differential equation for $\dot { \Phi } ( t , t _ { 0 } )$ ,

$$
\dot { \Phi } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) ,
$$

with initial conditions

$$
\Phi ( t _ { 0 } , t _ { 0 } ) = I .
$$

The matrix $\Phi ( t , t _ { 0 } )$ is referred to as the State Transition Matrix. Whenever Eqs. (G.1.11) and (G.1.12) are satisfied, the solution to $\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t )$ is given by Eq. (G.1.8).

# G.2 THE STATE TRANSITION MATRIX

Insight into the $n \times n$ state transition matrix can be obtained as follows. Let

$$
\Phi ( t , t _ { 0 } ) \equiv \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } \equiv \left[ \begin{array} { l } { \phi _ { 1 } ( t , t _ { 0 } ) } \\ { \phi _ { 2 } ( t , t _ { 0 } ) } \\ { \phi _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { l } { \frac { \partial { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } } \\ { \frac { \partial { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } } \\ { \frac { \partial \beta ( t ) } { \partial { \bf X } _ { 0 } } } \end{array} \right] .
$$

Note that $\phi _ { 3 } ( t , t _ { 0 } )$ is an $m \times n$ matrix of constants partitioned into an $m \times 6$ matrix of zeros on the left and an $m \times m$ identity matrix on the right, where $m$ is the dimension of $\beta$ and $\mathbf { X }$ is of dimension $n$ . Because of this, it is only necessary to solve the upper $6 \times n$ portion of Eq. (G.1.11).

Equation (G.1.11) also can be written in terms of a second-order differential equation. This can be shown by differentiating Eq. (G.2.1):

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) = { \frac { { \partial } { \dot { \mathbf { X } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } = \left[ { \dot { \phi } } _ { 1 } ( t , t _ { 0 } ) \right] = \left[ \begin{array} { c } { \frac { { \partial } { \dot { \mathbf { r } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } \\ { \frac { { \partial } { \dot { \mathbf { r } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } \\ { { \dot { \phi } } _ { 3 } ( t , t _ { 0 } ) \end{array} } \right]
$$

$$
\mathbf { \Gamma } = \left[ \begin{array} { c } { \frac { \partial \dot { \mathbf { r } } ( t ) } { \partial \mathbf { X } ( t ) } } \\ { \frac { \partial \ddot { \mathbf { r } } ( t ) } { \partial \mathbf { X } ( t ) } } \\ { 0 } \end{array} \right] _ { n \times n } \left[ \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } \right] _ { n \times n } .
$$

In these equations, 0 represents an $m \times n$ null matrix. Notice from the first of Eq. (G.2.2) that

$$
\ddot { \phi } _ { 1 } = \frac { \partial \ddot { \bf r } } { \partial { \bf X } _ { 0 } } = \dot { \phi } _ { 2 } .
$$

Hence, we could solve this second-order system of differential equations to obtain $\Phi ( t , t _ { 0 } )$ ,

$$
\begin{array} { l } { \displaystyle { \ddot { \phi } } _ { 1 } ( t , t _ { 0 } ) = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf X } ( t ) } \ \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } \qquad } \\ { \displaystyle = \left[ \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf r } ( t ) } \frac { \partial \ddot { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \frac { \partial \ddot { \bf r } ( t ) } { \partial \beta } \right] _ { 3 \times n } \left[ \frac { \partial \dot { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } \right] _ { n \times n } } \end{array}
$$

or

$$
\ddot { \phi } _ { 1 } ( t , t _ { 0 } ) = \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } { \bf r } ( t ) } \phi _ { 1 } ( t , t _ { 0 } ) + \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } \dot { \bf r } ( t ) } \dot { \phi } _ { 1 } ( t , t _ { 0 } ) + \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } \beta } \phi _ { 3 } ( t , t _ { 0 } ) .
$$

With initial conditions

$$
\begin{array} { r l } & { \phi _ { 1 } ( t _ { 0 } , t _ { 0 } ) = \left[ [ I ] _ { 3 \times 3 } [ 0 ] _ { 3 \times ( n - 3 ) } \right] } \\ & { \dot { \phi } _ { 1 } ( t _ { 0 } , t _ { 0 } ) = \phi _ { 2 } ( t _ { 0 } , t _ { 0 } ) = [ [ 0 ] _ { 3 \times 3 } [ I ] _ { 3 \times 3 } [ 0 ] _ { 3 \times m } ] \ . } \end{array}
$$

We could solve Eq. (G.2.5), a $3 \times n$ system of second-order differential equations, instead of the $6 \times n$ first-orde r system given by Eq. (G.2.2). Recall that the partial derivatives are evaluated on the reference state and that the solution of the $m \times n$ system represented by $\dot { \phi } _ { 3 } ( t , t _ { 0 } ) = 0$ is trivial,

$$
\phi _ { 3 } ( t , t _ { 0 } ) = [ [ 0 ] _ { m \times 6 } [ I ] _ { m \times m } ] .
$$

In solving Eq. (G.2.5) we could write it as a system of $n \times n$ first-order equations,

$$
\begin{array} { r l } & { \dot { \phi } _ { 1 } ( t , t _ { 0 } ) = \phi _ { 2 } ( t , t _ { 0 } ) } \\ & { \dot { \phi } _ { 2 } ( t , t _ { 0 } ) = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf r } ( t ) } \phi _ { 1 } ( t , t _ { 0 } ) + \frac { \partial \ddot { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \phi _ { 2 } ( t , t _ { 0 } ) + \frac { \partial \ddot { \bf r } ( t ) } { \partial \beta } \phi _ { 3 } ( t , t _ { 0 } ) } \\ & { \dot { \phi } _ { 3 } ( t , t _ { 0 } ) = 0 . } \end{array}
$$

It is easily shown that Eq. (G.2.6) is identical to Eq. (G.1.11),

$$
\left[ \begin{array} { c } { \dot { \phi } _ { 1 } ( t , t _ { 0 } ) } \\ { \dot { \phi } _ { 2 } ( t , t _ { 0 } ) } \\ { \dot { \phi } _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] _ { n \times n } = \left[ \begin{array} { c c } { [ 0 ] _ { 3 \times 3 } } & { [ I ] _ { 3 \times 3 } } & { [ 0 ] _ { 3 \times m } } \\ { \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial { \bf r } ( t ) } \right] _ { 3 \times 3 } \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \right] _ { 3 \times 3 } \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial \beta } \right] _ { 3 \times m } } \\ { [ 0 ] _ { m \times 3 } } & { [ 0 ] _ { m \times 3 } } & { [ 0 ] _ { m \times m } } \end{array} \right] _ { n \times n } ^ { * } \left[ \begin{array} { c } { \phi _ { 1 } ( t , t _ { 0 } ) } \\ { \phi _ { 2 } ( t , t _ { 0 } ) } \\ { \phi _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] _ { n \times n }
$$

or

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) .
$$

Appendix H

# Transformation between ECI and ECF Coordinates

# H.1 INTRODUCTION

The transformation between ECI and ECF coordinates is defined by Eq. (2.

$$
T _ { X Y Z } ^ { x y z } = T _ { \mathrm { E C I } } ^ { \mathrm { E C F } } = W S ^ { \prime } N P .
$$

The transformation matrices W, $S ^ { \prime }$ , N, and $\mathrm { \bf P }$ account for the following effects:

$W =$ the offset of the Earth’s angular velocity vector with respect to the $z$ axis of the ECF (see Section 2.4.2)   
$S ^ { \prime } =$ the rotation of the ECF about the angular velocity vector (see Sections 2.3.3 and 2.4.2)   
$N =$ the nutation of the ECF with respect to the ECI (see Section 2.4.1)   
$P =$ the precession of the ECF with respect to the ECI (see Section 2.4.1).

The ECI and ECF systems have fundamental characteristics described in Chapter 2. The realization of these reference systems in modern space applications is usually through the International Celestial Reference Frame (ICRF) for the ECI and the International Terrestrial Reference Frame (ITRF) for the ECF. These realizations infer certain characteristics for highest accuracy and consistency. For example, the ICRF is defined using the coordinates of extragalactic radio sources, known as quasars, where the coordinates are derived from observations obtained on the surface of the Earth with a set of large antennas known as the Very Long Baseline Interferometry (VLBI) network. The coordinates of the quasars are then linked with visible sources to an optical star catalog and the coordinates of the celestial bodies in the solar system. In a similar manner, the ITRF is realized with ground networks of SLR, LLR, GPS, and DORIS (see Chapter 3), which establish the center of mass origin of the ITRF, as well as the reference meridian.

The following sections summarize the content of the matrices required for the transformation from an ECI system to an ECF system. This discussion follows the classical formulation and it will be assumed that the ECI is realized through J2000, which is not precisely the same as the actual ICRF adopted by the International Astronomical Union. If observed values of polar motion $( x _ { p } , y _ { p } )$ and $\Delta ( \mathrm { U T 1 } )$ are used, the transformation matrix has an accuracy of better than one arc-sec. The satellite motion is especially sensitive to polar motion and the rate of change in UT1, which is related to length of day. This sensitivity enables the estimation of these parameters from satellite observations.

The International Earth Rotation Service (IERS) distributes Earth Orientation Parameters (EOP) derived from VLBI and satellite observations. The main EOP are $( x _ { p } , y _ { p } )$ , $\Delta ( \mathrm { U T } 1 )$ and corrections to the precession and nutation parameters. These parameters are empirical corrections derived from satellite and VLBI observations which account for changes resulting from tides and atmospheric effects, for example. The EOP are regularly distributed by the IERS as Bulletin B. Consult the IERS publications and web page for additional information. As the models adopted by the IERS are improved, they are documented in new releases of the IERS Standards (or “Con ventions”).

For the most part, the following discussion follows Seidelmann (1992) and McCarthy (1996). A comprehensive summary is given by Seeber (1993). A comparison of different implementations of the matrices, including a detailed review of the transformations, has been prepared by Webb (2002).

# H.2 MATRIX $P$

For this discussion, P represents the transformation from J2000 to a mean-ofdate system. If is a function of the precession of the equinoxes (see Section 2.4.1). The transformation matrix is dependent on three angles and is given by (where C represents cosine and S denotes sine):

P =

and the precession angles are given by

$$
\begin{array} { l } { \zeta _ { A } = 2 3 0 6 \prime \prime 2 1 8 1 t + 0 \prime \prime 3 0 1 8 8 t ^ { 2 } + 0 \prime \prime 0 1 7 9 9 8 t ^ { 3 } } \\ { \theta _ { A } = 2 0 0 4 \prime 3 1 0 9 t - 0 \prime \prime 4 2 6 6 5 t ^ { 2 } - 0 \prime \prime 0 4 1 8 3 3 t ^ { 3 } } \\ { z _ { A } = 2 3 0 6 \prime \prime 2 1 8 1 t + 1 \prime 0 9 4 6 8 t ^ { 2 } + 0 \prime \prime 0 1 8 2 0 3 t ^ { 3 } } \end{array}
$$

with $t$ defined as

$$
t = { \frac { [ T T - J 2 0 0 0 . 0 ] ( \mathrm { { d a y s } } ) } { 3 6 5 2 5 } } .
$$

In Eq. H.2.3, J2000.0 is January 1, 2000, 12:00 in TT, or JD 2451545.0. These equations are based on the work of Lieske, et al. (1977). Terrestrial Time (TT) is defined in Section 2.4.2.

# H.3 MATRIX $N$

The transformation from a mean-of-date system to a true-of-date system is dependent on the nutations (see Section 2.4.1). Four angles are used: the mean obliquity of the ecliptic $( \epsilon _ { m } )$ , the true obliquity of the ecliptic $\left( \epsilon _ { t } \right)$ , the nutation in longitude $( \Delta \psi )$ , and the nutation in obliquity $( \Delta \epsilon )$ . The matrix $_ \mathrm { N }$ is given by

$$
\left[ \begin{array} { l l l } { \mathbf { C } \Delta \boldsymbol { \psi } } & { - \mathbf { C } \epsilon _ { m } \mathbf { S } \Delta \boldsymbol { \psi } } & { - \boldsymbol { \mathrm { S } } \epsilon _ { m } \boldsymbol { \mathrm { S } } \Delta \boldsymbol { \psi } } \\ { \mathbf { C } \epsilon _ { t } \mathbf { S } \Delta \boldsymbol { \psi } } & { \mathbf { C } \epsilon _ { m } \mathbf { C } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } + \mathbf { S } \epsilon _ { m } \mathbf { S } \epsilon _ { t } } & { \quad \mathrm { S } \epsilon _ { m } \mathbf { C } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } - \mathbf { C } \epsilon _ { m } \mathbf { S } \epsilon _ { t } } \\ { \mathbf { S } \epsilon _ { t } \mathbf { S } \Delta \boldsymbol { \psi } } & { \mathbf { C } \epsilon _ { m } \mathbf { S } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } - \mathbf { S } \epsilon _ { m } \mathbf { C } \epsilon _ { t } } & { \quad \mathrm { S } \epsilon _ { m } \mathbf { S } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } + \mathbf { C } \epsilon _ { m } \mathbf { C } \epsilon _ { t } } \end{array} \right] ,
$$

where the mean obliquity is

$$
\epsilon _ { m } = 8 4 3 8 1 ^ { \prime \prime } 4 4 8 - 4 6 ^ { \prime \prime } 8 1 5 0 t - 0 ^ { \prime \prime } 0 0 0 5 9 t ^ { 2 } + 0 ^ { \prime \prime } 0 0 1 8 1 3 t ^ { 3 }
$$

and the true obliquity is

$$
\epsilon _ { t } = \epsilon _ { m } + \Delta \epsilon .
$$

The expression for the nutation in longitude and in obliquity is given by Mc-Carthy (1996), for example. The IAU 1980 theory of nutation is readily available in a convenient Chebychev polynomial approximation with the planetary ephemerides (Standish, et al., 1997). Corrections to the adopted series, based on observations, are provided by the IERS in Bulletin B.

# H.4 MATRIX $S ^ { \prime }$

The true-of-date rotation to a pseudo-body-fix ed system accounts for the ‘spin’ of the Earth. This diurnal rotation depends on a single angle $\alpha _ { G }$ , which is referred

to as the Greenwich Mean Sidereal Time (GMST). The matrix $S ^ { \prime }$ is identical to Eq. 2.3.20; namely,

$$
\begin{array} { r } { S ^ { \prime } = \left[ \begin{array} { c c c } { \mathrm { C } \alpha _ { G } } & { \mathrm { S } \alpha _ { G } } & { 0 } \\ { - \mathrm { S } \alpha _ { G } } & { \mathrm { C } \alpha _ { G } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

In some cases, especially when a satellite velocity vector with respect to the rotating ECF is required, the time derivative of the time-dependent elements of each of the transformation matrices will be needed. However, the time derivative of $S ^ { \prime }$ is particularly significant since the angle $\alpha _ { G }$ is the fastest changing variable in the matrices P, N, $S ^ { \prime }$ and W. The time derivative of $S ^ { \prime }$ is

$$
\dot { S } ^ { \prime } = \dot { \alpha } _ { G } \left[ \begin{array} { c c c } { - \mathrm { S } \alpha _ { G } } & { \mathrm { C } \alpha _ { G } } & { 0 } \\ { - \mathrm { C } \alpha _ { G } } & { - \mathrm { S } \alpha _ { G } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

where $\dot { \alpha } _ { G }$ is the rotation rate of the Earth. For some applications, this rate can be taken to be constant, but for high-accuracy applications the variability in this rate must be accounted for. According to the IERS, the average rate is $\mathrm { 7 . 2 9 2 1 1 5 1 4 6 7 0 6 4 \times 1 0 ^ { - 5 } r a d / s }$ , but this value should be adjusted using IERS Bulletin B to account for variations. The GMST for a given UT1 $( \mathrm { U T C } + \Delta ( \mathrm { U T 1 } ) )$ can be found from Kaplan, et al. (1981), modified to provide the result in radians:

$$
\begin{array} { r l } { \mathrm { G M S T ( U T 1 ) } = 4 . 8 9 4 9 6 1 2 1 2 8 2 3 0 5 8 7 5 1 3 7 5 7 0 4 4 3 0 } & { { } { \mathrm { ( H } } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad + \Delta T \Bigl \{ 6 . 3 0 0 3 8 8 0 9 8 9 8 4 8 9 3 5 5 2 2 7 6 5 1 3 7 2 0 } & { } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad + \Delta T \Bigl ( 5 . 0 7 5 2 0 9 9 9 4 1 1 3 5 9 1 4 7 8 0 5 3 8 0 5 5 2 3 \times 1 0 ^ { - 1 5 } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - 9 . 2 5 3 0 9 7 5 6 8 1 9 4 3 3 5 6 4 0 0 6 7 1 9 0 6 8 8 \times 1 0 ^ { - 2 4 } \Delta T \Bigr ) \Bigr \} } \end{array}
$$

where $\Delta T = \mathrm { U T 1 } - \mathrm { J 2 0 0 0 . 0 }$ , and where $\Delta T$ is in days, including the fractional part of a day.

An additional correction known as the equation of the equinoxes must be applied. For highest accuracy, additional terms amounting to a few milli-arc-sec amplitude should be applied (see McCarthy, 1996; or Simon, et al., 1994) . With the equation of the equinoxes, the angle $\alpha _ { G }$ becomes

$$
\alpha _ { G } = \mathrm { G M S T } ( \mathrm { U T 1 } ) + \Delta \psi \cos \epsilon _ { m } .
$$

# H.5 MATRIX W

The pseudo-body-fix ed system is aligned with the instantaneous pole, equator and reference meridian of the Earth. As noted in Section 2.4.2, the Earth’s spin axis is not fix ed in the Earth and two angles $( x _ { p } , y _ { p } )$ are used to describe the spin axis location with respect to an adopted ECF, such as an ITRF. Because of the small magnitude of the polar motion angles, the transformation matrix W can be represented by

$$
T _ { \mathrm { P B F } } ^ { \mathrm { B F } } = W = \left[ \begin{array} { c c c } { 1 } & { 0 } & { x _ { p } } \\ { 0 } & { 1 } & { - y _ { p } } \\ { - x _ { p } } & { y _ { p } } & { 1 } \end{array} \right] ,
$$

where the polar motion angles are expressed in radians. The angles are available in IERS Bulletin B, for example.

# H.6 REFERENCES

Aoki, S., and H. Kinoshita, “Note on the relation between the equinox and Guinot’s non-rotating origin,” Celest. Mech., Vol. 29, No. 4, pp. 335–360, 1983.

Kaplan, G. H. (ed.), The IAU Resolutions on astronomical constants, time scales, and the fundamental reference frame, USNO Circular No. 163, U.S. Naval Observatory, 1981.

Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

Lieske, J. H., T. Lederle, W. Fricke, and B. Morando, “Expressions for the precession quantities based upon the IAU (1976) System of Astronomical Constants,” Astronomy and Astrophysics, Vol. 58, pp. 1–16, 1977.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Seeber, G., Satellite Geodesy: Foundations, Methods & Applications, Walter deGruyter, New York, 1993.

Seidelmann, P. K., “1980 IAU Nutation: The Final Report of the IAU Working Group on Nutation,” Celest. Mech., Vol. 27, No. 1, pp. 79–106, 1982.

Seidelmann, P. K., Explanatory Supplement to the Astronautical Almanac, University Science Books, Mill Valley, CA, 1992.

Simon, J. L., P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. ´ Laskar, “Numerical expressions for precession formulae and mean elements for the Moon and planets,” Astronomy and Astrophysics, Vol. 282, pp. 663–683, 1994.   
Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc. Richmond, 1997.   
Webb, C.,The ICRF-ITRF Transformation: A Comparison of Fundamental Earth Orientation Models found in MSODP and CALC, The University of Texas at Austin, Center for Space Research Report CSR-02-01, Austin, TX, 2002.

# Bibliography Abbreviations

Adv. Space Res.   
AIAA   
AIAA J.   
ASME   
Astron. J.   
Celest. Mech.   
Geophys. J. Royal Astronom. Soc. Geophys. Res. Ltrs.   
IEEE J. Appl. Math.   
J. Assoc. Comput. Mach.   
J. Astronaut. Sci.   
J. Basic Engr.   
J. Geophys. Res.   
J. Guid. Cont.   
J. Guid. Cont. Dyn.   
J. Inst. Math. Applic.   
Advances in Space Research   
American Institute of Aeronautics and Astronautic   
AIAA Journal   
American Society of Mechanical Engineers   
Astronomical Journal   
Celestial Mechanics and Dynamical Astronomy   
Geophysical Journal of the Royal Astronomical Society   
Geophysical Research Letters   
Institute for Electrical and Electronics Engineers   
Journal of Applied Mathematics   
Journal of the Association of Computing Machiner   
Journal of the Astronautical Sciences   
ASME Journal of Basic Engineering   
Journal of Geophysical Research   
Journal of Guidance and Control   
Journal of Guidance, Control, and Dynamics   
Journal of the Institute of Mathematics and Its Applications   
Journal of the Insitute of Navigation   
Journal of Optimization Theory and Applications   
Journal of Spacecraft and Rockets   
Society for Industrial and Applied Mathematics   
International Society for Optical Engineering   
IEEE Transactions on Automatic Control J. ION   
J. Optim. Theory Appl. J. Spacecr. Rockets   
SIAM   
SPIE   
Trans. Auto. Cont.

# Bibliography

[1] Aoki, S., and H. Kinoshita, “Note on the relation between the equinox and Guinot’s non-rotating origin,” Celest. Mech., Vol. 29, No. 4, pp. 335–360, 1983.

[2] Ashby, N., “Relati vity and the Global Positioning System,” Physics Today, Vol. 55, No. 5, pp. 41–47, May 2002.

[3] Barlier, F., C. Berger, J. Falin, G. Kockarts, and G. Thuiller, “A thermospheric model based on satellite drag data,” Annales de Geophysique ´ , Vol. 34, No. 1, pp. 9–24, 1978.

[4] Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

[5] Bertiger, W., Y. Bar-Sever, E. Christensen, E. Davis, J. Guinn, B. Haines, R. Ibanez-Meier, J. Jee, S. Lichten, W. Melbourne, R. Muellerschoen, T. Munson, Y. Vigue, S. Wu, T. Yunck, B. Schutz, P. Abusali, H. Rim, W. Watkins, and P. Willis , “GPS precise tracking of TOPEX/Poseidon: Results and implications,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,449– 24,462, December 15, 1995.

[6] Beutler, G., E. Brockmann, W. Gurtner, U. Hugentobler, L. Mervart, M. Rothacher, and A. Verdun, “Extended orbit modeling techniques at the CODE Processing Center of the International GPS Service for Geodynamics (IGS): theory and initial results,” Manuscripta Geodaetica, Vol. 19, No. 6, pp. 367–385, April 1994.

[7] Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

[8] Bjorck, A., ¨ Numerical Methods for Least Squares Problems, SIAM, Philadelphia, PA, 1996.

[9] Bond, V., and M. Allman, Modern Astrodynamics, Princeton University Press, Princeton, NJ, 1996.

[10] Born, G. H., D. B. Goldstein, and B. Thompson, “An Analytical Theory for Orbit Determination”, J. Astronaut. Sci., Vol. 49, No. 2, pp. 345–361, April–June 2001.

[11] Born, G., J. Mitchell, and G. Hegler, “GEOSAT ERM – mission design,” J. Astronaut. Sci., Vol. 35, No. 2, pp. 119–134, April–June 1987.

[12] Born, G. H., B. D. Tapley, and M. L. Santee, “Orbit determination using dual crossing arc altimetry,” Acta Astronautica, Vol. 13, No. 4, pp. 157– 163, 1986.

[13] Boucher, C., Z. Altamini, and P. Sillard, The International Terrestrial Reference Frame (ITRF97), IERS Technical Note 27, International Earth Rotation Service, Observatoire de Paris, May 1999.

[14] Brouwer, D., “Sol utions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

[15] Brouwer, D., and G. Clemence, Methods of Celestial Mechanics, Academic Press, New York, 1961.

[16] Bryson, A. E., and Y. C. Ho, Applied Optimal Control, Hemisphere Publishing Corp., Washington, DC, 1975.

[17] Bucy, R., and P. Joseph, Filtering for Stochastic Processes, John Wiley & Sons, Inc., New York, 1968.

[18] Cajori, F., A History of Mathematics, MacMillan Co., New York, 1919.

[19] Carlson, N. A., “F ast triangular formulation of the square root fil ter”, AIAA J., Vol. 11, No. 9, pp. 1239-1265, September 1973.

[20] Chobotov, V. (ed.), Orbital Mechanics, American Institute of Aeronautics and Astronautics, Inc., Reston, VA, 1996.

[21] Christensen, E., B. Haines, K. C. McColl, and R. S. Nerem, “Observ ations of geographically correlated orbit errors for TOPEX/Poseidon using the Global Positioning System,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2175–2178, September 15, 1994.

[22] Cook, G. E., “Perturbati ons of near-circular orbits by the Earth’s gravitational potential,” Planetary and Space Science, Vol. 14, No. 5, pp. 433– 444, May 1966.

[36] El´Yasberg, P. E., Introduction to the Theory of Flight of Artifici al Earth Satellites, translated from Russian, Israel Program for Scientific Translations, 1967.

[37] Fisher, R. A., “On an absolute criteria for fitti ng frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

[38] Fliegel, H., T. Gallini, and E. Swift, “Global Positioning System radiation force models for geodetic applications”, J. Geophys. Res., Vol. 97, No. B1, pp. 559–568, January 10, 1992.

[39] Freeman, H., Introduction to Statistical Inference, Addison-Wesley, 1963.

[40] Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

[41] Gelb, A. (ed.), Applied Optimal Estimation, Massachusetts Institute of Technology Press, Cambridge, MA, 1974.

[42] Gentleman, W. M., “Lea st squares computations by Givens transformations without square roots,” J. Inst. Math. Applic., Vol. 12, pp. 329–336, 1973.

[43] Givens, W., “Computa tion of plane unitary rotations transforming a general matrix to triangular form,” J. Appl. Math., Vol. 6, pp. 26–50, 1958.

[44] Goldstein, D. B., G. H. Born, and P. Axelrad, “Real-time, autonomous, precise orbit determination using GPS,” J. ION, Vol. 48, No. 3, pp. 169– 179, Fall 2001.

[45] Golub, G. H., and C. F. Van Loan, Matrix Computations, Johns Hopkins University Press, 1996.

[46] Goodyear, W. H., “Complet ely general closed form solution for coordinates and partial derivatives of the two-body problem,” Astron. J., Vol. 70, No. 3, pp. 189–192, April 1965.

[47] Graybill, F. A., An Introduction to Linear Statistical Models, McGraw-Hill, New York, 1961.

[48] Grewal, M. S., and A. P. Andrews, Kalman Filtering: Theory and Practice, Prentice Hall, 1993.

[49] Gruber, T., A. Bode, C. Reigber, P. Schwintzer, G. Balmino, R. Biancale, J. Lemoine, “GRIM5- C1: Combination solution of the global gravity field to degree and order 120,” Geophys. Res. Ltrs., Vol. 27, No. 24, pp. 4005– 4008, December 2000.

[50] Heffes, H., “The effects of erroneous models on the Kalman filt er response”, Trans. Auto. Cont., Vol. AC-11, pp. 541–543, July 1966.

[51] Heiskanen, W., and H. Moritz, Physical Geodesy, W. H. Freeman and Co., San Francisco, 1967.

[52] Helmert, F. R., “Zur Bestimmung kleiner Flachenst ¨ ucke des Geoids aus ¨ Lothabweichungen mit Rucksicht auf Lothkr ¨ ummung”, Sitzungsberichte ¨ Preuss. Akad. Wiss., Berlin, Germany, 1900.

[53] Helstrom, C. W., Probability and Stochastic Processes for Engineers, MacMillan, 1984.

[54] Herring, T., “Model ing atmospheric delays in the analysis of space geodetic data,” in Refraction of Transatmospheric Signals in Geodesy, eds. J. C. DeMunck and T. A. Th. Spoelstra, Netherlands Geodetic Commission Publications in Geodesy, 36, pp. 157-164, 1992.

[55] Herring, T., B. Buffett, P. Mathews, and I. Shapiro, “Free nutations of the Earth: influence of inner core dynamics,” J. Geophys. Res., Vol. 96, No. B5, pp. 8259–8273, May 10, 1991.

[56] Hofmann-Wellenhof, B., H. Lichtenegger, and J. Collins, Global Positioning System: Theory and Practice, Springer-Verlag, Wien-New York, 1997.

[57] Householder, A. S., “Unita ry triangularization of a nonsymmetric matrix,” J. Assoc. Comput. Mach., Vol. 5, No. 4, pp. 339–342, October 1958.

[58] Huang, C., J. C. Ries, B. Tapley, and M. Watkins, “Rela tivistic effects for near-Earth satellite orbit determination,” Celest. Mech., Vol. 48, No. 2, 167-185, 1990.

[59] Ingram, D. S., Orbit determination in the presence of unmodeled accelerations, Ph.D. Dissertation, The University of Texas at Austin, 1970.

[60] Ingram, D. S., and B. D. Tapley, “Lunar orbit determination in the presence of unmodeled accelerations,” Celest. Mech., Vol. 9, No. 2, pp. 191–211, 1974.

[61] Jacchia, L., Thermospheric temperature, density and composition: new models, Special Report 375, Smithsonian Astrophysical Observatory, Cambridge, MA, 1977.

[62] Jazwinski, A. H., Stochastic Process and Filtering Theory, Academic Press, New York, 1970.

[63] Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March, 1960.

[64] Kalman, R. E. and R. S. Bucy, “Ne w Results in Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 83, Series D, No. 1, pp. 95–108, March, 1961.

[65] Kaminski, P. G., A. E. Bryson, and S. F. Schmidt, “Discret e square root filteri ng: A survey of current techniques,” Trans. Auto. Cont., Vol. AC-16, No. 6, pp. 727–736, December 1971.

[66] Kaplan, G. H. (ed.), The IAU Resolutions on astronomical constants, time scales, and the fundamental reference frame, USNO Circular No. 163, U.S. Naval Observatory, 1981.

[67] Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, 1966 (republished by Dover, New York, 2000).

[68] Kolmogorov, A. N., “Interpolation and Extrapolation of Stationary Random Sequences,” Bulletin of the Academy of Sciences of the USSR Math. Series, Vol. 5, pp. 3–14, 1941.

[69] Kovalevsky, J., I. Mueller, and B. Kolaczek (eds.), Reference Frames in Astronomy and Geophysics, Kluwer Academic Publishers, Dordrecht, 1989.

[70] Kreyszig, E., Advanced Engineering Mathematics, John Wiley & Sons, Inc., New York, 1993.

[71] Lambeck, K., The Earth’s Variable Rotation, Cambridge University Press, Cambridge, 1980.

[72] Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

[73] Laplace, P. S., Theorie Analytique de Probabilit ´ es´ , Paris, 1812 (The 1814 edition included an introduction, Essai Philosophique sur les Probabilites´ , which has been translated into English: Dale, A. I., Philosophical Essay on Probabilities, Springer-Verlag, New York, 1995).

[74] Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

[75] Le Systeme International d’Unites (SI), Bureau International des Poids et Mesures, Sevres, France, 1991.

[76] Legendre, A. M., Nouvelles methodes pour la d ´ etermination des orbites ´ des cometes \` , Paris, 1806.

[77] Leick, A., GPS Satellite Surveying, J. Wiley & Sons, Inc., New York, 2003.

[78] Lemoine, F., S. Kenyon, J. Factor, R. Trimmer, N. Pavlis, D. Chinn, C. Cox, S. Klosko, S. Luthcke, M. Torrence, Y. Wang, R. Williamson, E. Pavlis, R. Rapp, and T. Olson, The development of the Joint NASA GSFC and the National Imagery and Mapping Agency (NIMA) Geopotential Model EGM96, NASA/TP–1998–206861, Greenbelt, MD, July 1998.

[79] Lemoine, F., D. Rowlands, S. Luthcke, N. Zelensky, D. Chinn, D. Pavlis, and G. Marr, “P recise orbit determination of GEOSAT follow-on using satellite laser ranging and intermission altimeter crossovers,” NASA/CP-2001-209986, Flight Mechanics Symposium, John Lynch (ed.), NASA Goddard Space Flight Center, Greenbelt, MD, pp. 377–392, June 2001.

[80] Lichten, S. M., “Es timation and fil tering for high precision GPS positioning applications,” Manuscripta Geodaetica, Vol. 15, pp. 159–176, 1990.

[81] Liebelt, P. B., An Introduction to Optimal Estimation, Addison-Wesley, Reading, MA, 1967.

[82] Lieske, J. H., T. Lederle, W. Fricke, and B. Morando, “Expre ssions for the precession quantities based upon the IAU (1976) System of Astronomical Constants,” Astronomy and Astrophysics, Vol. 58, pp. 1–16, 1977.

[83] Lundberg, J., and B. Schutz, “Recursion formulas of Legendre functions for use with nonsingular geopotential models,” J. Guid. Cont. Dyn., Vol. 11, No. 1, pp. 31–38, January–Fe bruary 1988.

[84] Lutchke, S. B., N. P. Zelenski, D. D. Rowlands, F. G. Lemoine, and T. A. Williams, “The 1-centimeter orbit: Jason-1 precision orbit determination using GPS, SLR, DORIS and altimeter data,” Marine Geodesy, Vol. 26, No. 3-4, pp. 399–421, 2003.

[85] Marini, J. W., and C. W. Murray, “Correction of laser range tracking data for atmospheric refraction at elevations above 10 degrees,” NASA GSFC X591-73-351, Greenbelt, MD, 1973.

[86] Markov, A. A., “The law of large numbers and the method of Least Squares,” (1898), Izbr. Trudi., Izd. Akod. Nauk, USSR, pp. 233-251, 1951.

[87] Marshall, J. A., F. J. Lerch, S. B. Luthcke, R. G. Williamson, and C. Chan, “An Assessment of TDRSS for Precision Orbit Determination,” J. Astonaut. Sci, Vol. 44, No. 1, pp. 115–127, January–March, 1996.

[102] Plummer, H. C., An Introductory Treatise on Dynamical Astronomy, Cambridge University Press, 1918 (republished by Dover Publications, New York, 1966).   
[103] Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1966.   
[104] Press, W., B. Flannery, S. Teukolsky, and W. Vetterling, Numerical Recipes, Cambridge University Press, Cambridge, 1986.   
[105] Prussing, J., and B. Conway, Orbit Mechanics, Oxford University Press, New York, 1993.   
[106] Rausch, H. E., F. Tung, and C. T. Striebel, “Maximum likelihood estimates of linear dynamic systems,” AIAA J., Vol. 3, No. 7, pp. 1445–1450, August 1965.   
[107] Reddy, J. N., and M. L. Rasmussen, Advanced Engineering Analysis, Robert E. Krieger Publishing Co., Malabar, FL 1990.   
[108] Ries, J. C., C. Huang, M. M. Watkins, and B. D. Tapley, “Orbit determination in the relativistic geocentric reference frame,” J. Astronaut. Sci., Vol. 39, No. 2, pp. 173–181, April–J une 1991.   
[109] Ries, J. C., C. K. Shum, and B. Tapley, “Surf ace force modeling for precision orbit determination,” Geophysical Monograph Series, Vol. 73, A. Jones (ed.), American Geophysical Union, Washington, DC, 1993.   
[110] Rowlands, D. D., S. B. Luthcke, J. A. Marshall, C. M. Cox, R. G. Williamson, and S. C. Rowton, “Space Shuttle precision orbit determination in support of SLA-1 using TDRSS and GPS tracking data,” J. Astronaut. Sci., Vol. 45, No. 1, pp. 113–129, January–March 1997.   
[111] Roy, A. E., Orbital Motion, John Wiley & Sons Inc., New York, 1988.   
[112] Saastamoinen, J., “Atmospheric correction for the troposphere and stratosphere in radio ranging of satellites,” Geophysical Monograph Series, Vol. 15, S. Henriksen, A. Mancini, and B. Chovitz (eds.), American Geophysical Union, Washington, DC, pp. 247–251, 1972.   
[113] Schaub, H., and J. Junkins, Analytical Mechanics of Space Systems, American Institute of Aeronautics and Astronautics, Reston, VA, 2003.   
[114] Schlee, F. H., C. J. Standish, and N. F. Toda, “Di vergence in the Kalman filter ,” AIAA J., Vol. 5, No. 6, pp. 1114–1120, June 1967.

[115] Schutz, B., B. D. Tapley, P. Abusali, H. Rim, “Dynamic orbit determination using GPS measurements from TOPEX/Poseidon,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2179–2182, 1994.

[116] Seeber, G., Satellite Geodesy: Foundations, Methods & Applications, Walter de Gruyter, New York, 1993.

[118] Seidelmann, P. K. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

[119] Shampine, L., and M. Gordon, Computer Solution of Ordinary Differential Equations, The Initial Value Problem, W. H. Freeman and Co., San Francisco, 1975.

[120] Shum, C. K., B. Zhang, B. Schutz, and B. Tapley, “Altimeter crossover methods for precise orbit determination and the mapping of geophysical parameters,” J. Astronaut. Sci., Vol. 38, No. 3, pp. 355–368, July– September 1990.

[121] Simon, J. L., P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, ´ J. Laskar, “Numerical expressions for precession formulae and mean elements for the Moon and planets,” Astronomy and Astrophysics, Vol. 282, pp. 663–683, 1994.

[122] Skolnik, M.I. (ed.), Radar Handbook, McGraw-Hill, New York, 1990.

[123] Smart, W. M., Celestial Mechanics, John Wiley & Sons Inc., New York, 1961.

[124] Sorenson, H. W., “Least squares estimation: from Gauss to Kalman,” IEEE Spectrum, Vol. 7, No. 7, pp. 63–68, July, 1970.

[125] Sorenson, H. W. (ed.), Kalman Filtering: Theory and Applications, IEEE Press, 1985.

[126] Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA 1997.

[127] Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

[128] Szebehely, V., Theory of Orbits, Academic Press, New York, 1967.

[129] Szebehely, V., and H. Mark, Adventures in Celestial Mechanics, John Wiley & Sons, Inc., New York, 1998.

[130] Tapley, B. D., “Stat istical orbit determination theory,” in Recent Advances in Dynamical Astronomy, B. D. Tapley and V. Szebehely (eds.), D. Reidel, pp. 396–425, 1973.

[131] Tapley, B. D.,“ Fundamentals of orbit determination”, in Theory of Satellite Geodesy and Gravity Field Determination, Vol. 25, pp. 235-260, Springer-Verlag, 1989.

[132] Tapley, B. D., and C. Y. Choe, “An algorithm for propagating the square root covariance matrix in triangular form,” Trans. Auto. Cont., Vol. AC-21, pp. 122–123, 1976.

[133] Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations,” Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369– 373, August 1973.

[134] Tapley, B. D., and J. G. Peters, “A sequential estimation algorithm using a continuous $U D U ^ { T }$ covariance factorization,” J. Guid. Cont., Vol. 3, No. 4, pp. 326–331, July–August 1980.

[135] Tapley, B. D., J. Ries, G. Davis, R. Eanes, B. Schutz, C. Shum, M. Watkins, J. Marshall, R. Nerem, B. Putney, S. Klosko, S. Luthcke, D. Pavlis, R. Williamson, and N. P. Zelensky, “Pre cision orbit determination for TOPEX/Poseidon,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,383– 24,404, December 15, 1994.

[136] Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3,” J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

[137] Thompson, B., M. Meek, K. Gold, P. Axelrad, G. Born, and D. Kubitschek, “Orbit determination for the QUIKSCAT spacecraft,” J. Spacecr. Rockets, Vol. 39, No. 6, pp. 852–858, November–Decem ber 2002.

[138] Thornton, C. L., Triangular covariance factorizations for Kalman filtering , Technical Memorandum, 33–798, Jet Propulsion Laboratory, Pasadena, CA, October 15, 1976.

[139] Torge, W., Geodesy, Walter de Gruyter, Berlin, 1980 (translated to English: Jekeli, C.).

[140] Vallado, D., Fundamentals of Astrodynamics and Applications, Space Technology Library, Microcosm Press, El Segundo, CA, 2001.

[141] Vigue, Y., B. Schutz, and P. Abusali, “Thermal force modeling for the Global Positioning System satellites using the finite element method,” $J .$ Spacecr. Rockets, Vol. 31, No. 5, pp. 866–859, 1994.

[142] Visser, P., and B. Ambrosius, “O rbit determination of TOPEX/Poseidon and TDRSS satellites using TDRSS and BRTS tracking,” Adv. Space Res., Vol. 19, pp. 1641–1644, 1997.

[143] Wahr, J. M., “The forced nutations of an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. of Royal Astronom. Soc., 64, pp. 705–727, 1981.

[144] Walpole, R. E., R. H. Myers, S. L. Myers, and Y. Keying, Probability and Statistics for Engineers and Scientists, Prentice Hall, Englewood Cliffs, NJ, 2002.

[145] Webb, C.,The ICRF-ITRF Transformation: A Comparison of Fundamental Earth Orientation Models found in MSODP and CALC, The University of Texas at Austin, Center for Space Research Report CSR-02-01, Austin, TX, 2002.

[146] Wells, D., Guide GPS Positioning, Canadian GPS Associates, Fredericton, 1987.

[147] Westfall, R., Never at Rest: A Biography of Isaac Newton, Cambridge University Press, Cambridge, 1980.

[148] Wiener, N., The Extrapolation, Interpolation and Smoothing of Stationary Time Series, John Wiley & Sons, Inc., New York, 1949.

[149] Wiesel, W. E., Spaceflight Dynamics, McGraw-Hill, 1997.

[150] Woolard, E., Theory of the rotation of the Earth around its center of mass, Astronomical Papers—American Ephemeris and Nautical Almanac, Vol. XV, Part I, U.S. Naval Observatory, Washington, DC, 1953.

# Author Index

Abusali, P., 69, 159   
Allman, M., 19, 56   
Altamini, Z., 78   
Ambrosius, B., 132   
Andrews, A. P., 199   
Axelrad, P., 116, 148, 233   
Balmino, G., 488   
Bar-Sever, Y., 125, 159   
Barlier, F., 67   
Battin, R. H., 19, 165, 167, 333   
Berger, C., 67   
Bertiger, W., 125, 159   
Bettadpur, S., 125   
Beutler, G., 68   
Biancale, R., 488   
Bierman, G. J., 199, 205, 206, 316,   
338–340, 342–345, 369–   
371, 397, 434   
Bjorck, A., 173, 180 ¨   
Bode, A., 488   
Bond, V., 19, 56   
Born, G. H., 60, 147, 148, 233, 493   
Boucher, C. Z., 78   
Brahe, T., 17   
Bretagnon, P., 520   
Brockmann, E., 68   
Brouwer, D., 28, 59, 70, 493, 495,   
497   
Bryson, A. E., 251, 331   
Bucy, R., 13, 205   
Buffett, B., 73, 113   
Cajori, F., 13   
Carlson, N. A., 338, 339   
Chapront, J., 520   
Chapront-Touze, M., 520 ´   
Chinn, D., 147, 488   
Chobotov, V., 19   
Choe, C. Y., 346   
Christensen, E., 146, 159   
Clemence, G., 28   
Collins, J., 116, 120, 123, 124, 148   
Conway, B., 19   
Cook, G. E., 60   
Cox, C. M., 132, 488   
Cruickshank, D. R., 229, 233, 499   
Curkendall, D. W., 434   
Dahlquist, G., 180   
Danby, J. M. A., 19, 24, 51, 67   
Davis, E., 159   
Davis, G., 159, 243, 244, 487   
Davis, J. C., 465   
Degnan, J., 126, 127   
Desai, S. D., 125, 160   
Deutsch, R., 185   
Dorroh, W. E., 251   
Dunn, C., 125   
Dyer, P., 343, 358   
Eanes, R., 159, 243, 244, 487   
Einstein, A., 18, 65   
El´Yasberg, P. E., 44   
Enge, P., 116   
Factor, J., 488   
Falin, J., 67   
Fisher, R. A., 13, 190   
Flannery, B., 45   
Fliegel, H., 68   
Folkner, W., 64, 74, 488, 519   
Francou, G., 520   
Franklin, G., 125   
Freeman, H., 440, 451, 465   
Fricke, W., 519   
Gallini, T., 68   
Gauss, K. F., 12, 13, 173   
Gelb, A., 199   
Gentleman, W. M., 302, 307   
Gill, E., 94, 199   
Givens, W., 292, 324, 330   
Gold, K., 148   
Goldstein, D. B., 233, 493   
Golub, G. H., 288   
Goodyear, W. H., 40, 41, 182   
Gordon, M., 45, 46   
Graybill, F. A., 331, 463, 464, 473,   
480   
Grewal, M. S., 199   
Gruber, T., 488   
Guinn, J., 159   
Gurtner, W., 68   
Haines, B. J., 125, 146, 159, 160   
Hanson, R. J., 173, 332   
Harris, I., 125   
Heffes, H., 427   
Hegler, G., 60   
Heiskanen, W., 52, 53   
Helmert, F. R., 13   
Helstrom, C. W., 440   
Herring, T., 73, 113   
Ho, Y. C., 251   
Hofmann-Wellenhof, B., 116, 120,   
124, 148   
Householder, A. S., 310   
Huang, C., 65, 116   
Hugentobler, U., 68   
Ibanez-Meier, R., 159   
Ingram, D. S., 229, 233, 369   
Jacchia, L., 67   
Jazwinski, A. H., 246, 248, 434   
Jee, J., 159   
Joseph, P. D., 205   
Junkins, J., 19   
Kalman, R. E., 13, 14, 199, 206, 208,   
334, 388   
Kaminski, P. G., 331, 343, 364, 366   
Kaula, W. M., 58, 59, 485   
Kenyon, S., 488   
Kepler, J., 17, 27   
Keying, Y., 465   
Kim, J., 125   
Klosko, S., 159, 243, 244, 487, 488   
Kockarts, G., 67   
Kolaczek, B., 18   
Kolmogorov, A. N., 13   
Kovalevsky, J., 18   
Kreyszig, E., 251   
Kruizinga, G., 125   
Kuang, D., 125   
Kubitschek, D., 148   
Lambeck, K., 64, 71   
Laplace, P. S., 13, 171   
Laskar, J., 520   
Lawson, C. L., 173, 332   
Lederle, T., 519   
Legendre, A. M., 13, 52   
Leick, A., 116   
Lemoine, F., 147, 487   
Lemoine, J., 488   
Lerch, F. J., 132, 243, 487   
Lichten, S. M., 159, 229, 233   
Lichtenegger, H., 116, 120, 123, 124,   
148   
Liebelt, P. B., 199   
Lieske, J. H., 519   
Lundberg, J., 53   
Lutchke, S. B., 132, 147, 159, 160,   
244, 488   
Marini, J. W., 112, 113   
Mark, H., 19   
Markov, A. A., 13, 230   
Marr, G., 147   
Marshall, J. A., 132, 159, 243, 244,   
487   
Mathews, P., 73, 113   
Maybeck, P. S., 199, 230, 233, 342,   
343, 345, 503   
McCarthy, D., 64, 77, 78, 487, 488,   
518–520   
McColl, K. C., 146   
McGarry, J., 126, 127   
McReynolds, S., 343, 358   
Meehan, T., 125   
Meek, M., 148   
Melbourne, W., 159   
Mervart, L., 68   
Mikhail, E. M., 251   
Mitchell, J., 60   
Mohr, P. J., 487   
Moler, C., 172   
Montenbruck, O., 94, 199   
Morando, B., 519   
Moritz, H., 52, 53, 71   
Motte, A., 17   
Moulton, F. R., 45   
Mueller, I., 18, 71   
Muellerschoen, R., 159   
Munson, T., 159   
Murray, C. W., 112, 113   
Myers, K. A., 190, 191, 231   
Myers, R. H., 465   
Myers, S. L., 465

Nandi, S., 125

Nerem, R. S., 146, 159, 243, 244,   
487   
Newhall, X., 64, 74, 488, 519   
Newton, I., 16–20, 44, 71, 162, 244   
Nguyen, D., 125

Olson, T., 488

Papoulis, A., 467   
Parkinson, B., 116   
Pavlis, D., 147, 159, 244   
Pavlis, E., 488   
Pavlis, N., 243, 487, 488   
Peters, J. G., 346   
Pines, S., 54   
Plummer, H.C., 17   
Pollard, H., 486   
Poole, S., 243, 487   
Press, W., 45   
Prussing, J., 19   
Putney, B., 159, 244   
Rapp, R., 488   
Rasmussen, M. L., 254   
Rausch, H. E., 248, 250, 365   
Reddy, J. N., 254   
Reigber, C., 488   
Ries, J. C., 65, 69, 116, 159, 243,   
244, 487   
Rim, H., 159, 243, 487   
Rogstad, T., 125   
Romans, L., 125   
Rothacher, M., 68   
Rowlands, D. D., 132, 147   
Rowton, S. C., 132   
Roy, A. E., 19   
Saastamoinen, J., 112   
Santee, M. L., 147   
Schaub, H., 19   
Schlee, F. H., 220   
Schmidt, S. F., 331   
Schutz, B. E., 53, 147, 159, 243, 244,   
487   
Schwintzer, P., 488   
Seeber, G., 94, 518   
Seidelmann, P. K., 74, 77, 487, 488,   
518   
Shampine, L., 45, 46   
Shapiro, I., 73, 113   
Shum, C. K., 69, 147, 159, 243, 244,   
487   
Sillard, P., 78   
Simon, J. L., 520   
Smart, W. M., 28   
Sorenson, H. W., 14, 199   
Spilker, J., 116   
Standish, C. J., 220   
Standish, E. M., 64, 74, 488, 519   
Striebel, C. T., 248, 250, 365   
Swerling, P., 13, 199   
Swift, E., 68   
Szebehely, V., 19, 46   
Tapley, B. D., 65, 116, 147, 159, 160,   
199, 233, 243, 244, 346,   
369, 487   
Taylor, B. N., 487   
Teukolsky, S., 45   
Thomas, J., 125   
Thompson, B., 148, 493   
Thornton, C. L., 340, 342–345, 434   
Thornton, T. H., 251   
Thuiller, G., 67   
Tien, J., 125   
Toda, N. F., 220   
Torge, W., 79   
Torrence, M., 488   
Trimmer, R., 488   
Tung, F., 248, 250, 365   
Vallado, D., 19, 26   
Van Loan, C., 172   
Verdun, A., 68   
Vetterling, W., 45   
Vigue, Y., 69, 159   
Visser, P., 132   
Wahr, J. M., 73   
Walpole, R. E., 190, 191, 465   
Wang, Y., 488   
Watkins, M. M., 65, 116, 125, 159,   
243, 244, 487   
Webb, C., 518   
Westfall, R., 17   
Wiener, N., 13   
Wiesel, W. E., 257   
Williams, J., 64, 74, 488, 519   
Williamson, R. G., 132, 159, 243,   
244, 487, 488   
Willis, P., 159   
Woolard, E., 73   
Wu, S. C., 125, 159   
Yunck, T., 159   
Zelensky, N. P., 147, 159, 244   
Zhang, B., 147

# Index

along-track direction, 42   
ambiguity, 135   
ambiguity resolution, 135   
AMOS (Air Force Maui Optical and Supercomputing), 149   
AN (ascending node), 28, 31   
angular momentum, 20–22, 28, 30, 32, 74, 90, 238, 254, 257   
apfocus, 25   
apogee, 25   
area-to-mass ratio, 67   
argument of perigee, 24, 36, 62, 63, 65, 493   
ARP (antenna reference point), 122   
AS (anti-spoofing), 120   
ascending node, 28–31, 47, 58, 60, 62 longitude of, 29, 40, 238 right ascension of, 29, 36   
autocorrelation, 230, 231, 469   
autocovariance, 469   
autumnal equinox, 31   
azimuth, 81

ballistic coefficient, 36, 66, 67   
batch processor, 190, 194, 197, 237   
Bayes theorem, 465, 466   
Bayesian estimation, 190   
biased range, 102   
bivariate normal density function, 460   
bivariate normal distribution, 460, 461   
broadcast ephemerides, 124

carrier frequencies, 116   
CCD (charge coupled device), 148   
central force, 1, 162   
central limit theorem, 465   
characteristic polynomial, 478   
characteristic root, 478   
characteristic vector, 478   
choke-ring antenna, 121   
Cholesky decomposition, 14, 198, 286, 287, 290, 295, 318, 324, 325, 330, 332, 334, 342, 384   
clock time, 102   
clock-steering, 134   
CNES (Centre National d’Etudes Spatiales), 132   
combining estimates, 258   
computed observation, 93, 179   
computed range, 97   
conditional density function, 191–193, 246, 249, 454, 461, 464, 466   
conditional probability, 247, 443, 454   
conditioning number, 332   
consider covariance, 435, 436, 438   
consider covariance analysis, 14, 245, 387, 388, 397, 400, 407, 410   
consider covariance matrix, 389, 396, 398   
consider error, 425   
consider fil ter, 388, 395, 416

consider parameters, 388–390   
constant of nutation, 73   
continuous system, 227   
coordinate system, 18   
correlation coefficient, 277, 457–459,   
463, 509   
covariance matrix coordinate trans  
formation, 257   
covariance matrix mapping, 190   
critical inclination, 59   
cross-link ranging, 125   
cross-track direction, 43   
crossover measurements, 146   
cycle slip, 134

derivative matrix, 161   
descending node, 31   
determinant, 462, 473, 475–477   
Dirac delta function, 220, 224, 227, 501   
direct effect, 63   
distribution function, 444, 452, 453, 468   
disturbing function, 49, 57, 485   
dithered, 122   
DMC (Dynamic Model Compensation), 220, 230, 233, 499, 505, 506, 508, 509   
DN (descending node), 29, 31   
Doppler effect, 109   
DORIS (Doppler Orbitography and Radio positioning Integrated by Satellite), 115, 132, 138   
downlink path, 99   
DOY (day of year), 75   
drag, 66 drag coefficie nt, 66   
dry component, 111   
dual-one-way-ranging, 125   
eccentric anomaly, 25–27, 33, 35, 37, 44   
eccentricity, 24, 28, 33, 36, 44, 57– 59, 67, 79, 82, 88, 497   
eccentricity vector, 33   
ECEF (Earth-centered, Earth-fix ed) or ECF (Earth-centered, fix ed) 32, 39, 56, 79, 82, 90, 91, 105, 135, 136, 151, 257, 517   
ECI (Earth-centered inertial), 32, 34, 43, 56, 82, 91, 105, 106, 257, 258, 517   
ecliptic, 30, 31, 46, 47, 49, 50, 63, 72, 73   
eigenvalue, 332, 478   
eigenvector, 478   
EKF (Extended Kalman Filter), 209   
elevation, 81   
elevation mask, 96   
empirical forces, 69   
empty focus, 25   
energy per unit mass, 21   
EOP (Earth Orientation Parameters), 518   
ephemeris, 37   
ephemeris parameters, 124   
ERS (European Earth Resources Satellites), 128   
escape trajectories, 25   
estimation error covariance matrix, 185   
Euler angles, 254, 255   
expected value, 222, 248, 405, 408, 445, 447, 455, 469   
extended sequential filter , 202, 209, 349   
frozen orbits, 60, 61   
gain matrix, 200, 429   
GALILEO, 118   
Gauss-Markov Process, 220, 229–232, 281, 369, 371, 506   
Gaussian distribution, 277   
general perturbations, 45, 59   
geocenter, 54   
geocentric latitude, 39, 52, 65, 78, 79, 81   
geodetic latitude, 78, 79, 113   
geometric range, 94   
Givens algorithm, 208, 298, 300, 307– 309, 327, 330, 335 rotation, 292, 298, 300, 303, 327 square root factorization algorithm, 344 square root free algorithm, 330 square root free computational algorithm, 305 square root free transformation, 301, 302, 307, 325, 326, 384 transformation, 291, 318, 320, 324, 344, 357, 384   
GLAS (Geoscience Laser Altimeter System), 130   
GLONASS (Global Navigation Satellite System), 118   
GMST (Greenwich Mean Sidereal Time), 31, 520   
GPS (Global Positioning System), 69, 70, 74, 77, 78, 87–89, 93, 115, 116, 118, 120, 122, 123, 132, 134, 140, 146, 151   
GPS-T (GPS-Time), 76, 77, 134   
GPS-week, 77   
GRACE (Gravity Recovery And Climate Experiment), 125   
Gram-Schmidt orthogonalization, 344, 345   
gravitational pertubations, 50   
ground track, 38, 40, 90, 95, 97, 100   
height above the ellipsoid, 78   
high-high, 125   
high-low, 125   
Hipparcos astrometry satellite, 148   
Householder algorithm, 208, 316, 325, 330 equations, 314 transformation, 310–312, 315, 316, 318, 322, 329, 330, 344, 357, 384   
hydrostatic component, 111   
ICESat, 128, 130, 154   
ICRF (International Celestial Reference Frame), 517, 518   
IERS (International Earth Rotation Service), 74, 78, 488, 518– 521   
IGS (International GPS Service), 124, 136   
ILRS (International Laser Ranging Service), 127   
inclination, 28   
index of refraction, 111   
indirect oblateness, 63   
inertial reference frame, 18   
information filter , 233, 235, 236, 284, 351   
information matrix, 190   
innovation, 210   
instantaneous range, 94   
ITRF (International Terrestrial Reference Frame), 78, 82, 135, 517, 518   
J2000 system, 31   
Jacobi Constant, 56   
Jacobi integral, 56, 91   
Jason-1 satellite, 159   
JD (Julian Date), 75   
Joseph covariance formulation, 205, 207, 208   
Julian day number, 75   
Kalman filter (see also sequential filter), 14, 199, 202, 207, 356, 427 gain, 200, 211   
Kepler’s Equation, 26–28, 35, 44   
kinematic solution, 148   
Kronicker delta, 199   
Lageos, 115   
Langevin equation, 230, 505   
leap seconds, 77   
least squares, 9, 14, 173, 174, 176, 177, 187, 352   
Legendre functions, 53 polynomial, 52, 53   
Legendre’s Associated Functions, 52, 53   
LEO (Low Earth Orbiter), 124, 125, 147, 148   
likelihood function, 191, 193, 194, 259, 277   
line of nodes, 22, 28–30, 47, 58   
linear approximations, 42   
linearization, 9, 160, 161, 202, 209   
LOD (length of day), 74, 91   
long-period perturbations, 48   
longitude, 78   
longitude angle, 52   
low-low, 125

M50 system, 31   
marginal distribution, 461, 463, 469   
mass distribution, 50   
matrix trace, 477   
matrizant, 40   
Maximum Likelihood Estimation, 190–   
193, 276, 277, 290   
MC (Master Clock), 77   
mean, 445   
mean anomaly, 27, 36   
mean elements, 58

mean equator and equinox of 1950.0, 32 of 2000.0, 31   
mean motion, 27   
measurement noise, 144   
measurement precision, 144   
measurement update, 202   
median, 194, 466, 467   
minimum norm, 174, 175, 273   
minimum variance, 183–186, 188, 194, 259, 290   
minimum variance estimation, 14   
Minitrack, 93   
MJD (modified Julian date), 75   
mode, 191, 194, 466, 467   
MOLA (Mars Orbiter Laser Altimeter), 130   
moment generating function, 448, 450   
multipath, 121   
multivariate normal density function, 462   
multivariate normal distribution, 462– 464   
multiway, 131   
n-body effects, 61   
navigation message, 124   
navigation solution, 148   
Newton-Raphson method, 7, 27, 180, 182   
NIMA (National Imagery and Mapping Agency), 124   
NIST (National Institute of Standards and Time), 76   
nodal period, 60, 61   
nondispersive medium, 111   
nonnegative definite , 476   
nonspherical, 54   
normal matrix, 174, 177, 187, 190, 229, 237, 238, 413   
normalized, 53   
nutation, 71–73, 82, 91, 243