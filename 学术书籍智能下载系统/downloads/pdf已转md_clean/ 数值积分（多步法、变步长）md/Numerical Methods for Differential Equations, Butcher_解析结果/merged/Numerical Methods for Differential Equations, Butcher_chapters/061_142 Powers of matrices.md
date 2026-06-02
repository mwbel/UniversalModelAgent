# 142 Powers of matrices

We are interested in powers of a matrix $A$ in terms of two questions: when is the sequence of powers bounded, and when does the sequence converge to the zero matrix? There are various equivalent formulations of the criteria for these properties of $A$ , and we state the most widely accessible of these.

Definition 142A A square matrix $A$ is ‘stable’ if there exists a constant $C$ such that for all $n = 0 , 1 , 2 , \ldots$ , $\| A ^ { n } \| \leq C$ .

This property is often referred to as ‘power-boundedness’.

Definition 142B A square matrix A is ‘convergent’ if $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \| A ^ { n } \| = 0 } \end{array}$ .

Theorem 142C Let A denote an $m \times m$ matrix. The following statements are equivalent:

(i) A is stable.   
(ii) The minimal polynomial of A has all its zeros in the closed unit disc and all its multiple zeros in the open unit disc.   
(iii) The Jordan canonical form of $A$ has all its eigenvalues in the closed unit disc with all eigenvalues of magnitude 1 lying in $1 \times 1$ blocks.   
(iv) There exists a non-singular matrix $S$ such that $\| S ^ { - 1 } A S \| _ { \infty } \leq 1$ .

Proof. We prove that $( i ) \Rightarrow ( i i ) \Rightarrow ( i i i ) \Rightarrow ( i v ) \Rightarrow ( i )$ . If $A$ is stable but $( i i )$ is not true, then either there exist $\lambda$ and $v \neq 0$ such that $| \lambda | > 1$ and $A v = \lambda v$ , or there exist $\lambda$ , $u \ne 0$ and $\boldsymbol { v }$ such that $| \lambda | = 1$ and $A v = \lambda v + u$ , with $A u \ = \ \lambda u$ . In the first case, $A ^ { n } v \ = \lambda ^ { n } v$ and therefore $\| A ^ { n } \| ~ \geq ~ | \lambda | ^ { n }$ which is not bounded. In the second case, $A ^ { n } v = \lambda ^ { n } v + n \lambda ^ { n - 1 } u$ and therefore $\| A ^ { n } \| \geq n \| u \| / \| v \| - 1$ , which also is not bounded. Given $( i i )$ , it is not possible that the conditions of $( i i i )$ are not satisfied, because the minimal polynomial of any of the Jordan blocks, and therefore of $A$ itself, would have factors that contradict $( i i )$ . If $( i i i )$ is true, then $S$ can be chosen to form $J$ , the Jordan canonical form of $A$ , with the off-diagonal elements chosen sufficiently small so that $\| J \| _ { \infty } \leq 1$ . Finally, if $( i v )$ is true then $A ^ { n } = S ( S ^ { - 1 } A S ) ^ { n } S ^ { - 1 }$ so that $\| A ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } A S \| ^ { n } \cdot \| S ^ { - 1 } \| \leq \| S \| \cdot \| S ^ { - 1 } \|$ . 

Theorem 142D Let A denote an $m \times m$ matrix. The following statements are equivalent

(i) A is convergent.   
(ii) The minimal polynomial of $A$ has all its zeros in the open unit disc.   
(iii) The Jordan canonical form of $A$ has all its diagonal elements in the open unit disc.   
(iv) There exists a non-singular matrix $S$ such that $\| S ^ { - 1 } A S \| _ { \infty } < 1$ .

Proof. We again prove that $( i ) \Rightarrow ( i i ) \Rightarrow ( i i i ) \Rightarrow ( i v ) \Rightarrow ( i )$ . If $A$ is convergent but $( i i )$ is not true, then there exist $\lambda$ and $u \neq 0$ such that $\lambda \geq 1$ and $A u = \lambda u$ . Hence, $A ^ { n } u = \lambda ^ { n } u$ and therefore $\| A ^ { n } \| \ge | \lambda | ^ { n }$ , which does not converge to zero. Given $( i i )$ , it is not possible that the conditions of $( i i i )$ are not satisfied, because the minimal polynomial of any of the Jordan blocks, and therefore of $A$ itself, would have factors that contradict $( i i ) .$ If $( i i i )$ is true, then $S$ can be chosen to form $J$ , the Jordan canonical form of $A$ , with the off-diagonal elements chosen sufficiently small so that $\| J \| _ { \infty } < 1$ . Finally, if $( i v )$ is true then $A ^ { n } = S ( S ^ { - 1 } A S ) ^ { n } S ^ { - 1 }$ so that $\| A ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot \| S ^ { - 1 } A S \| ^ { n } \to 0$ . $\boxed { \begin{array} { r l } \end{array} }$

While the two results we have presented here are related to the convergence of difference equation solutions, the next is introduced only because of its application in later chapters.

Theorem 142E If $A$ is a stable $m \times m$ matrix and $B$ an arbitrary $m \times m$ matrix, then there exists a real $C$ such that

$$
\left\| \left( A + { \frac { 1 } { n } } B \right) ^ { n } \right\| \leq C ,
$$

for $n = 1 , 2 , \ldots .$

Proof. Without loss of generality, assume that $\| \cdot \|$ denotes the norm $\| \cdot \| _ { \infty }$ . Because $S$ exists so that $\| S ^ { - 1 } A S \| \leq 1$ , we have

$$
\begin{array} { r l } {  { \| ( A + \frac { 1 } { n } B ) ^ { n } \| \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot \| ( S ^ { - 1 } A S + \frac { 1 } { n } S ^ { - 1 } B S ) ^ { n } \| } } \\ & { \leq \| S \| \cdot \| S ^ { - 1 } \| \cdot ( 1 + \frac { 1 } { n } \| S ^ { - 1 } B S \| ) ^ { n } } \\ & { \leq \| S \| \cdot \| S ^ { - 1 } \| \exp ( \| S ^ { - 1 } B S \| ) . } \end{array}
$$

In applying this result to sequences of vectors, the term represented by the matrix $B$ can be replaced by a non-linear function which satisfies suitable conditions. To widen the applicability of the result a non-homogeneous term is included.

Theorem 142F Let $A$ be a stable $m \times m$ matrix and $\phi ~ : ~ \mathbb { R } ^ { m } \ \to \ \mathbb { R } ^ { m }$ be such that $\| \phi ( x ) \| ~ \leq ~ L \| x \|$ , for $L$ a positive constant and $\boldsymbol { x } ~ \in ~ \mathbb { R } ^ { m }$ . If $w = ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } )$ and $v = ( v _ { 0 } , v _ { 1 } , \ldots , v _ { n } )$ are sequences related by

$$
v _ { i } = A v _ { i - 1 } + { \frac { 1 } { n } } \phi ( v _ { i - 1 } ) + w _ { i } , \quad i = 1 , 2 , \ldots , n ,
$$

then

$$
\left\| v _ { n } \right\| \leq C \left( \left\| v _ { 0 } \right\| + \sum _ { i = 1 } ^ { n } \left\| w _ { i } \right\| \right) ,
$$

where $C$ is independent of $n$ .

Proof. Let $S$ be the matrix introduced in the proof of Theorem 142C. From (142a), it follows that

$$
( S ^ { - 1 } v _ { i } ) = ( S ^ { - 1 } A S ) ( S ^ { - 1 } v _ { i - 1 } ) + \frac { 1 } { n } ( S ^ { - 1 } \phi ( v _ { i - 1 } ) ) + ( S ^ { - 1 } w _ { i } )
$$

and hence

$$
\| S ^ { - 1 } v _ { i } \| \leq \| S ^ { - 1 } A S \| \cdot \| S ^ { - 1 } v _ { i - 1 } \| + \frac { 1 } { n } \| S ^ { - 1 } \phi ( v _ { i - 1 } ) \| + \| S ^ { - 1 } w _ { i } \| ,
$$

leading to the bound

$$
\left\| v _ { n } \right\| \leq \left\| S \right\| \cdot \left\| S ^ { - 1 } \right\| \exp \left( L \| S \| \cdot \| S ^ { - 1 } \| \right) \left( \left\| v _ { 0 } \right\| + \sum _ { i = 1 } ^ { n } \| w _ { i } \| \right) .
$$

# Exercises 14

14.1 Find a constant $C$ such that $\| A ^ { n } \| _ { \infty } \leq C$ , for all $n = 0 , 1 , \ldots$ , where

$$
A = \left[ { \begin{array} { r r } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 4 } { 3 } } } \end{array} } \right] .
$$

14.2 For what values of the complex number $\theta$ is the matrix $A$ stable, where

$$
A = { \left[ \begin{array} { l l } { \theta } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } .
$$


<!-- chunk 0002: pages 71-140 -->
