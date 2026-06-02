# 310 Elementary differentials

To investigate the error in carrying out a single step of a Runge–Kutta method, we need to compare successive terms in the Taylor expansions of the exact and the computed solutions. These involve expressions whose structures are related to rooted trees. In the case of the exact solution, it is possible to evaluate the Taylor coefficients by repeated differentiation. We start with a differential equation, assumed for convenience to be autonomous,

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) .
$$

We also write (310a) in component-by-component form, with arguments omitted for brevity, as

$$
( y ^ { i } ) ^ { \prime } = f ^ { i } .
$$

To obtain the second derivative, use the chain rule

$$
y ^ { \prime \prime } ( x ) = { \frac { d } { d x } } f ( y ( x ) ) = f ^ { \prime } ( y ( x ) ) y ^ { \prime } ( x ) = f ^ { \prime } ( y ( x ) ) f ( y ( x ) )
$$

or, using (310b) as the starting point,

$$
{ \frac { d } { d x } } ( y ^ { i } ) ^ { \prime } = { \frac { d } { d x } } f ^ { i } = f _ { j } ^ { i } f ^ { j } .
$$

Note that in (310d) we have used the summation convention. We continue to use this convention without further comment. The third derivative can be found in a similar manner, but is complicated by the fact that $y ( x )$ is present in both factors in $f ^ { \prime } ( y ( x ) ) f ( y ( x ) )$ . Even though we are omitting arguments, $y ( x )$ is also implicitly present in the tensor form $f _ { j } ^ { i } f ^ { j }$ . The two forms of the third derivative are

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 3 } } { d x ^ { 3 } } y ( x ) = f ^ { \prime \prime } ( y ( x ) ) \big ( f ( y ( x ) ) , f ( y ( x ) ) \big ) + f ^ { \prime } ( y ( x ) ) ( f ^ { \prime } ( y ( x ) ) f ( y ( x ) ) ) , } } \\ { { \displaystyle \quad \frac { d ^ { 3 } } { d x ^ { 3 } } y ^ { i } = f _ { j k } ^ { i } f ^ { j } f ^ { k } + f _ { j } ^ { i } f _ { k } ^ { j } f ^ { k } . } } \end{array}
$$

We can find a pattern in the terms occurring in the first, second and third derivatives, using rooted trees. In the total derivative form, (310a), (310c), (310e), we relate $f ( \boldsymbol { y } ( \boldsymbol { x } ) )$ to a leaf in a tree, we relate $f ^ { \prime } ( y ( x ) )$ to a vertex with a single outwardly directed edge, and we relate $f ^ { \prime \prime } ( y ( x ) )$ to a vertex with two outward edges. In the case of $f ^ { \prime }$ and $f ^ { \prime \prime }$ , the outward edges are joined to subtrees, as representatives of the operands of these linear and bilinear operators, respectively.

For the tensor representations of the terms in the first three derivatives of $y ^ { i }$ , we treat the superscripts in $f ^ { i }$ , $f ^ { j }$ , $f ^ { k }$ as members of the vertex set $V$ , and we define the edge set $E$ in terms of the pairs, such as $( i , j )$ that occur in $f _ { j } ^ { i }$ , $f _ { j k } ^ { i }$ .

Relation between terms in $_ y$ derivatives and rooted trees   

<table><tr><td>Tree</td><td>Operator diagram</td><td>Term</td><td>Labelled tree</td><td>Tensor term</td></tr><tr><td>. ！</td><td>·f</td><td>f(y(x))</td><td>·i</td><td>fi</td></tr><tr><td></td><td>1</td><td>f&#x27;(y(x))f(y(x))</td><td>I</td><td>ffj</td></tr><tr><td>V</td><td>V f</td><td>f&quot;(y(x))(f(y(x)),f(y(x)))</td><td>V</td><td>fikfi fk</td></tr><tr><td>！</td><td>I</td><td>f&#x27;(y(x))(f&#x27;(y(x)f(y(x)))</td><td>[L</td><td>ffk</td></tr></table>

Thus, we can identify four trees as representatives of the terms that occur in the first, second and third derivatives of $y$ . In Table 310(I) we illustrate this correspondence using both formulations. Note that we write f, $\mathbf { f ^ { \prime } }$ and $\mathbf { f } ^ { \prime \prime }$ as abbreviations for $f ( \boldsymbol { y } ( \boldsymbol { x } ) )$ , $f ^ { \prime } ( y ( x ) )$ and $f ^ { \prime \prime } ( y ( x ) )$ , respectively.

We can expect this pattern to continue, because the operation of differentiating adds an additional vertex to an existing tree, in a number of different ways, and each of these corresponds to a further tree.

Definition 310A Given a tree $t$ and a function $f : \mathbb { R } ^ { N } \to \mathbb { R } ^ { N }$ , analytic in a neighbourhood of $y$ , the ‘elementary differential’ $F ( t ) ( y )$ is defined by

$$
\begin{array} { c } { F ( \tau ) ( y ) = f ( y ) , } \\ { F ( [ t _ { 1 } , t _ { 2 } , \dotsc , t _ { m } ] ) = f ^ { ( m ) } ( y ) ( F ( t _ { 1 } ) ( y ) , F ( t _ { 2 } ) ( y ) , \dotsc , F ( t _ { m } ) ( y ) ) . } \end{array}
$$

Note that the tensor interpretation of (310h) is written as

$$
F ^ { i } ( [ t _ { 1 } , t _ { 2 } , \ldots , t _ { m } ] ) = f _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { m } } ^ { i } F ^ { j _ { 1 } } ( t _ { 1 } ) F ^ { j _ { 2 } } ( t _ { 2 } ) \cdot \cdot \cdot F ^ { j _ { m } } ( t _ { m } ) .
$$

The elementary differentials up to order 5 are shown in Table 310(II). Note that we use the same abbreviation as in Table 310(I), in which f, $\mathbf { f ^ { \prime } } , \ldots$ denote $f ( y ( x ) ) , f ( y ( x ) ) ^ { \prime } , \ldots .$ The values of $\alpha ( t )$ are also shown; their significance will be explained in the next subsection.

As part of the equipment we need to manipulate expressions involving elementary differentials we consider the value of

$$
h f \Big ( y _ { 0 } + \sum _ { t \in T } \theta ( t ) \frac { h ^ { r ( t ) } } { \sigma ( t ) } F ( t ) ( y _ { 0 } ) \Big ) .
$$

Elementary differentials for orders 1 to 5   

<table><tr><td>r(t）</td><td>t</td><td>a（t）</td><td>F(t）(y)</td><td>F(t)(y）)</td></tr><tr><td>1</td><td>·</td><td>1</td><td>f</td><td>fr</td></tr><tr><td>2</td><td>：</td><td>1</td><td>ff</td><td>ffj</td></tr><tr><td>3</td><td>?</td><td>1</td><td>f&quot;(f,f)</td><td>fikfj fk</td></tr><tr><td>3</td><td>·</td><td>1</td><td>fff</td><td>ffk</td></tr><tr><td>4</td><td>Y</td><td>1</td><td>f&quot;(f,f,f)</td><td>fikfi fk fl</td></tr><tr><td>4</td><td></td><td>3</td><td>f&quot;(f,ff)</td><td>fkfiffl</td></tr><tr><td>4</td><td>小</td><td>1</td><td>f&#x27;f&quot;(f,f)</td><td>fffkfl</td></tr><tr><td>4</td><td>：</td><td>1</td><td>ffff</td><td>ffffl</td></tr><tr><td>5</td><td>￥ 4</td><td>1</td><td>f(4)(f,f,f,f)</td><td>fjklmfj fk fl fm</td></tr><tr><td>5</td><td></td><td>6</td><td>f(3)(f,f,ff)</td><td>fikifjfkfmfm</td></tr><tr><td>5</td><td></td><td>4</td><td>f&quot;(f,f&quot;(f,f))</td><td>fkfjfimflfm</td></tr><tr><td>5</td><td></td><td>4</td><td>f&quot;(f,fff)</td><td>fikfifrfmfm</td></tr><tr><td>5</td><td></td><td>3</td><td>f&quot;(f&#x27;f,ff)</td><td>fikfiflffm</td></tr><tr><td>5</td><td>Y</td><td>1</td><td>ff&quot;(f,f,f)</td><td>ffklmfk flfm</td></tr><tr><td>5</td><td>广</td><td>3</td><td>f&#x27;f&quot;(f,ff)</td><td>fffkfmfm</td></tr><tr><td>5</td><td></td><td>1</td><td>f&#x27;ff&quot;(f,f)</td><td>ff fimfl fm</td></tr><tr><td>5</td><td>！</td><td>1</td><td>f&#x27;fff&#x27;f</td><td>ffffm</td></tr></table>

As a formal series, this can be evaluated using the following result:

Lemma 310B The value of (310i) is

$$
\sum _ { t \in T } \widetilde { \theta } ( t ) \frac { h ^ { r ( t ) } } { \sigma ( t ) } F ( t ) ( y _ { 0 } ) ,
$$

where $ { \widetilde { \theta } }$ is defined by

$$
\widetilde { \theta } ( t ) = \left\{ \begin{array} { l l } { 1 , } & { t = \tau , } \\ { \displaystyle \prod _ { i = 1 } ^ { k } \theta ( t _ { i } ) , } & { t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } ] . } \end{array} \right.
$$

Proof. Use Theorem 306A. The case $t = \tau$ is obvious. For $t = [ t _ { 1 } ^ { m _ { 1 } } t _ { 2 } ^ { m _ { 2 } } \cdot \cdot \cdot t _ { j } ^ { m _ { j } } ]$ $t _ { 1 }$ $t _ { 2 }$ $t _ { j }$ are distinct, the factor

$$
\Big ( \sigma ( I ) \prod _ { i = 1 } ^ { j } \sigma ( t _ { j } ) ^ { m _ { j } } \Big ) ^ { - 1 } ,
$$

where $I$ is the index set consisting of $m _ { 1 }$ copies of $^ { 1 }$ , $m _ { 2 }$ copies of 2, $\cdot \cdot \cdot$ and copies of $j$ , is equal to $\sigma ( t ) ^ { - 1 }$ . $\sqcup$ $m _ { j }$
