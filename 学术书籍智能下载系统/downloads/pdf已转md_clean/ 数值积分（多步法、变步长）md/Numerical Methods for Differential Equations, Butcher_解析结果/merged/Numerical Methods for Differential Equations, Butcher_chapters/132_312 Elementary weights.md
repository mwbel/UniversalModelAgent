# 312 Elementary weights

Having found the Taylor expansion of the exact solution to an initial value problem, we now find the corresponding expansion for the approximation computed by a Runge–Kutta method. A term-by-term comparison of these will provide criteria for the error generated in a single step to be zero, except for terms that can be estimated in terms of high powers of the stepsize $h$ .

As a prelude, we consider a three-stage explicit Runge–Kutta method. We find the Taylor expansion in this simple case up to terms in $h ^ { 3 }$ . As the standard problem that we use for studying Runge–Kutta methods, we consider the autonomous initial value system

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { N } \to \mathbb { R } ^ { N }$ . The method has the tableau

$$
\left. \begin{array} { c } { { 0 } } \\ { { c _ { 2 } } } \\ { { c _ { 3 } } } \\ { { b _ { 1 } } } \end{array} \right| _ { { c _ { 3 } } } - a _ { 3 2 } \quad a _ { 3 2 } \qquad \mathrm { ~ . ~ }
$$

Denote by $Y _ { 1 }$ , $Y _ { 2 }$ and $Y _ { 3 }$ the results computed at the stages and $y _ { 1 }$ for the result computed at the end of the step.

We can in turn find truncated Taylor expansions for the stages and the output result. We also use Theorem 306A to evaluate the Taylor expansions of $h F _ { i } = h f ( Y _ { i } )$ , for $i = 1 , 2 , 3 .$ . Note that the stage values need only terms up to $h ^ { 2 }$ , because the extra $h$ in $h F _ { i }$ takes away the need to find $h ^ { 3 }$ terms except for the $h F _ { i }$ terms and the final result:

$$
\begin{array} { r l } & { Y _ { 1 } = y _ { 0 } , } \\ & { h F _ { 1 } = h _ { 0 } / ( y _ { 0 } ) , } \\ & { Y _ { 2 } = y _ { 0 } + c _ { 2 } h / ( y _ { 0 } ) , } \\ & { h F _ { 2 } = h _ { 0 } + c _ { 2 } h / ( y _ { 0 } ) , } \\ & { Y _ { 3 } = h _ { 0 } + ( c _ { 3 } - a _ { 5 } ) h / ( y _ { 0 } ) + a _ { 5 } 2 c _ { 2 } ^ { 3 } h / ^ { \prime \prime } ( y _ { 0 } ) ( f ( y _ { 0 } ) , f ( y _ { 0 } ) ) + O ( h ^ { 3 } ) , } \\ & { \qquad \quad \gamma _ { 3 } = y _ { 0 } + ( c _ { 3 } - a _ { 5 } ) h f ( y _ { 0 } ) + a _ { 5 } 2 ( h f ( y _ { 0 } ) + c _ { 2 } h ^ { 2 } / ( y _ { 0 } ) f ( y _ { 0 } ) ) + O ( h ^ { 3 } ) , } \\ & { \qquad \quad = y _ { 0 } + c _ { 3 } h f ( y _ { 0 } ) + a _ { 3 } 2 c _ { 2 } ^ { 3 } h ^ { \prime } f ( y _ { 0 } ) f ( y _ { 0 } ) + O ( h ^ { 3 } ) , } \\ & { h F _ { 3 } = h f ( y _ { 0 } ) + c _ { 3 } h ^ { 2 } f ^ { \prime } ( y _ { 0 } ) f ( y _ { 0 } ) + a _ { 5 } 2 c _ { 2 } h ^ { 2 } f ^ { \prime } ( y _ { 0 } ) f ( y _ { 0 } ) f ( y _ { 0 } ) } \\ & { \qquad \quad + \frac { 1 } { 2 } c _ { 2 } ^ { 3 } h ^ { 3 } f ^ { \prime \prime } ( y _ { 0 } ) ( f ( y _ { 0 } ) , f ( y _ { 0 } ) ) + O ( h ^ { 4 } ) , } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \qquad \quad \quad \quad \end{array}
$$

We recognize elementary differentials, evaluated at $y _ { 0 }$ , appearing in these expansions and we rewrite $y _ { 1 }$ as

$$
\begin{array} { r l } & { y _ { 1 } = y _ { 0 } + h \Phi ( \bullet ) F ( \bullet ) ( y _ { 0 } ) + h ^ { 2 } \Phi ( \mathfrak { T } ) F ( \mathfrak { T } ) ( y _ { 0 } ) } \\ & { \qquad + \frac { 1 } { 2 } h ^ { 3 } \Phi ( \pmb { \mathbb { Y } } ) F ( \pmb { \mathbb { Y } } ) ( y _ { 0 } ) + h ^ { 3 } \Phi \left( \mathfrak { T } \right) F \left( \mathfrak { T } \right) ( y _ { 0 } ) + O ( h ^ { 4 } ) , } \end{array}
$$

where the coefficients associated with the four trees of orders up to 3 are given by

$$
\begin{array} { r l } & { \Phi ( \bullet ) = b _ { 1 } + b _ { 2 } + b _ { 3 } , } \\ & { \Phi ( \mathbf { \widehat { t } } ) = b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } , } \\ & { \Phi ( \mathbf { \widehat { V } } ) = b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } , } \\ & { \Phi \left( \mathbf { \widehat { f } } \right) = b _ { 3 } a _ { 3 2 } c _ { 2 } . } \end{array}
$$

It is obvious that these expressions, which we have already introduced in Section 234, are of vital importance in understanding the accuracy of Runge– Kutta methods. We name them ‘elementary weights’ and define them formally, along with similar expressions associated with the individual stages, in the next definition. At the same time we define ‘derivative weights’ associated with the stages.

Relation between elementary weights and rooted trees   

<table><tr><td>labelled tree t</td><td>Elementary weight Φ(t) S</td></tr><tr><td>·i</td><td>M bi i=1</td></tr><tr><td>1</td><td>S S M biaij= &gt; biCi i,j=1 i=1</td></tr><tr><td>k I</td><td>S S bic² £ biaijaik = ? i,j,k=1 i=1 s S M M</td></tr></table>

Definition 312A Let

$$
\frac { c \mid A } { b ^ { \textsf { T } } }
$$

denote the tableau for an $s$ -stage Runge–Kutta method. Then the ‘elementary weights’ $\Phi ( t )$ , the ‘internal weights’ $\Phi _ { i } ( t )$ and the ‘derivative weights $\mathbf { \nabla } ^ { \prime } ( \Phi _ { i } D ) ( t )$ for $t \in T$ and $i = 1 , 2 , \dots , s$ are defined by

$$
\begin{array} { c } { { ( \Phi _ { i } D ) ( \tau ) = 1 , } } \\ { { \displaystyle \Phi _ { i } ( t ) = \sum _ { j = 1 } ^ { s } a _ { i j } ( \Phi _ { j } D ) ( t ) , } } \\ { { \displaystyle ( \Phi _ { i } D ) ( [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot { t _ { k } } ] ) = \prod _ { j = 1 } ^ { k } \Phi _ { i } ( t _ { j } ) , } } \\ { { \displaystyle \Phi ( t ) = \sum _ { i = 1 } ^ { s } b _ { i } ( \Phi _ { i } D ) ( t ) . } } \end{array}
$$

This definition is used recursively. First $\Phi _ { i } D$ is found for $t = \tau$ , using (312a), then $\Phi _ { i }$ is evaluated for this single vertex tree, using (312b). This enables $( \Phi _ { i } D ) ( [ \tau ] )$ , using (312c), and then $\Phi _ { i } ( [ \tau ] )$ to be found for each stage. The order is built up in this way until $( \Phi _ { i } D ) ( t )$ is known for any required tree. Finally, (312d) is used to evaluate $\Phi ( t )$ .

The notation $\Phi _ { i } D$ is part of a more general scheme, which we introduce in Subsection 387. In the meantime, $D$ should be thought of as an operator to be applied to $\Phi _ { i }$ , which replaces the sequence of Taylor coefficient weights in a stage value by the set of coefficient weights for the stage derivatives.

Elementary weights for orders 1 to 5   

<table><tr><td>r(t)</td><td>t</td><td>（t）</td><td></td></tr><tr><td>1</td><td></td><td></td><td>∑i-1bi</td></tr><tr><td>2</td><td></td><td>：</td><td>∑i=1bici</td></tr><tr><td></td><td>?</td><td></td><td>∑i=1bic²</td></tr><tr><td>3</td><td></td><td>·</td><td></td></tr><tr><td>3</td><td></td><td></td><td>∑ij=1biaijj</td></tr><tr><td>4</td><td>Y</td><td></td><td>∑i=1bic</td></tr><tr><td>4</td><td>丫</td><td></td><td>∑ij=1biqaigGj</td></tr><tr><td>4</td><td></td><td></td><td>ij=1bai</td></tr><tr><td>4</td><td></td><td>！</td><td>∑ij=1iaijajC</td></tr><tr><td>5</td><td>Y</td><td></td><td>∑i-1bic</td></tr><tr><td>5</td><td></td><td>Y</td><td>∑ij=1bic2aijC</td></tr><tr><td>5</td><td>?</td><td></td><td>∑ij=1biciaije²</td></tr><tr><td>5</td><td></td><td>?</td><td>∑ij=1ijjk</td></tr><tr><td>5</td><td>Y</td><td></td><td>∑i-1bi(∑j=1aijc)）²</td></tr><tr><td>5</td><td></td><td>Y</td><td>Eij=1baig</td></tr><tr><td>5</td><td>丫</td><td></td><td>∑ijk=1biaijjajkCk</td></tr><tr><td></td><td></td><td>丫</td><td></td></tr><tr><td></td><td></td><td></td><td>ij=1biaijaj</td></tr><tr><td></td><td></td><td></td><td>ij=1biaigajac</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

An alternative formula for $\Phi ( t )$ , which uses the vertex and edge characterization of each tree $t$ , is given in the following lemma, which we state without proof.

Lemma 312B Denote the vertex set $V$ of the tree $t$ by the set of index symbols $V = \{ j , k , l , \dots \}$ , where $j$ is the root of $t$ . Let the corresponding edge set be $E$ . Form the expression

$$
b _ { j } \prod _ { ( k , l ) \in E } a _ { k l }
$$

and sum this over each member of $V$ ranging over the index set $\{ 1 , 2 , \ldots , s \}$ .

The resulting sum is the value of $\Phi ( t )$ . A similar formula for $\Phi _ { i } ( t )$ , where $i$ is not a member of $V$ , is found by replacing (312e) by

$$
a _ { i j } \prod _ { ( k , l ) \in E } a _ { k l }
$$

and summing this as for $\Phi ( t )$

Note that, although $c$ does explicitly appear in Definition 312A or Lemma 312B, it is usually convenient to carry out the summations $\textstyle \sum _ { l = 1 } ^ { s } a _ { k l }$ to yield a result $c _ { k }$ if $\it l$ denotes a leaf (terminal vertex) of $V$ . This is possible because $\it l$ occurs only once in (312e) and (312f).

We illustrate the relationship between the trees and the corresponding elementary weights in Table 312(I). For each of the four trees, we write $\Phi ( t )$ in the form given directly by Lemma 312B, and also with the summation over leaves explicitly carried out. Finally, we present in Table 312(II) the elementary weights up to order 5.
