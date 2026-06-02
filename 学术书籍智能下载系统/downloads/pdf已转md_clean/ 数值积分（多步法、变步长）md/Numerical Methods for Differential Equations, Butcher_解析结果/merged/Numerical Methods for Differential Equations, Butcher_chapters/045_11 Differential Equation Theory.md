# 11 Differential Equation Theory

110 Existence and uniqueness of solutions

A fundamental question that arises in scientific modelling is whether a given differential equation, together with initial conditions, can be reliably used to predict the behaviour of the trajectory at later times. We loosely use the expression ‘well-posed’ to describe a problem that is acceptable from this point of view. The three attributes of an initial value problem that have to be taken into account are whether there actually exists a solution, whether the solution, if it exists, is unique, and how sensitive the solution is to small perturbations to the initial information. Even though there are many alternative criteria for answering these questions in a satisfactory manner, we focus here on the existence of a Lipschitz condition. This is especially convenient because the same type of condition can be used to study the behaviour of numerical approximations.

Definition 110A The function $f ~ : ~ [ a , b ] \times \mathbb { R } ^ { N } ~ \longrightarrow ~ \mathbb { R } ^ { N }$ is said to satisfy a ‘Lipschitz condition in its second variable’ if there exists a constant $L$ , known as a ‘Lipschitz constant’, such that for any $x \in [ a , b ]$ and $Y , Z \in \mathbb { R } ^ { N }$ , $\| f ( x , Y ) - f ( x , Z ) \| \leq L \| Y - Z \|$ .

We need a basic lemma on metric spaces known as the ‘contraction mapping principle’. We present this without proof.

Lemma 110B Let $M$ denote a complete metric space with metric $\rho$ and let $\phi : { \cal M }  { \cal M }$ denote a mapping which is a contraction, in the sense that there exists a number $k$ , satisfying $0 \leq k < 1$ , such that, for any $\eta , \zeta \in M$ , $\rho ( \phi ( \eta ) , \phi ( \zeta ) ) \leq k \rho ( \eta , \zeta )$ . Then there exists a unique $\xi \in M$ such that $\phi ( \xi ) = \xi$ .

We can now state our main result.

Theorem 110C Consider an initial value problem

$$
\begin{array} { c } { { y ^ { \prime } ( x ) = f ( x , y ( x ) ) , } } \\ { { y ( a ) = y _ { 0 } , } } \end{array}
$$

where $f : [ a , b ] \times \mathbb { R } ^ { N }  \mathbb { R } ^ { N }$ is continuous in its first variable and satisfies a Lipschitz condition in its second variable. Then there exists a unique solution to this problem.

Proof. Let $M$ denote the complete metric space of continuous functions $y : [ a , b ] \to \mathbb { R } ^ { N }$ , such that $y ( a ) = y _ { 0 }$ . The metric is defined by

$$
\rho ( y , z ) = \operatorname* { s u p } _ { x \in [ a , b ] } \exp ( - K ( x - a ) ) \| y ( x ) - z ( x ) \| ,
$$

where $K > L$ . For given $y \in M$ , define $\phi ( y )$ as the solution $Y$ on $[ a , b ]$ to the initial value problem

$$
\begin{array} { l c r } { { Y ^ { \prime } ( x ) = f ( x , Y ( x ) ) , } } \\ { { Y ( a ) = y _ { 0 } . } } \end{array}
$$

This problem is solvable by integration as

$$
\phi ( y ) ( x ) = y _ { 0 } + \int _ { a } ^ { x } f ( s , y ( s ) ) d s .
$$

This is a contraction because for any two $y , z \in M$ , we have

$$
\begin{array} { r l } { \rho ( \phi ( y ) , \phi ( z ) ) \leq } & { \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \left\| \int _ { a } ^ { x } \big ( f ( s , y ( s ) ) - f ( s , z ( s ) ) \big ) d s \right\| } \\ & { \leq \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \| f ( s , y ( s ) ) - f ( s , z ( s ) ) \| d s } \\ & { \leq L \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \| y ( s ) - z ( s ) \| d s } \\ & { \leq L \rho ( y , z ) \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \exp ( K ( s - a ) ) d s } \\ & { \leq L \rho ( y , z ) \underset { x \in [ a , b ] } { \operatorname* { s u p } } \exp ( - K ( x - a ) ) \int _ { a } ^ { x } \exp ( K ( s - a ) ) d s } \\ & { \leq \frac { L } { K } \rho ( y , z ) . } \end{array}
$$

The unique function $y$ that therefore exists satisfying $\phi ( y ) = y$ , is evidently the unique solution to the initial value problem given by (110a), (110b). 

The third requirement for being well-posed, that the solution is not overly sensitive to the initial condition, can be readily assessed for problems satisfying

a Lipschitz condition. If $y$ and $z$ each satisfy (110a) with $y ( a ) \ = \ y _ { 0 }$ and $z ( a ) = z _ { 0 }$ , then

$$
\frac { d } { d x } \| y ( x ) - z ( x ) \| \leq L \| y ( x ) - z ( x ) \| .
$$

Multiply both sides by $\exp ( - L x )$ and deduce that

$$
{ \frac { d } { d x } } { \big ( } \exp ( - L x ) \| y ( x ) - z ( x ) \| { \big ) } \leq 0 ,
$$

implying that

$$
\begin{array} { r } { \| y ( x ) - z ( x ) \| \leq \| y _ { 0 } - z _ { 0 } \| \exp \big ( L ( x - a ) \big ) . } \end{array}
$$

This bound on the growth of initial perturbations may be too pessimistic in particular circumstances. Sometimes it can be improved upon by the use of ‘one-sided Lipschitz conditions’. This will be discussed in Subsection 112.
