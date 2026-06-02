# 302 Some combinatorial questions

We consider the question of labelling a tree $t$ with $r ( t )$ vertices, using the symbols $\{ 1 , 2 , \ldots , r ( t ) \}$ , under the following conditions:

(i) Each vertex receives one and only one label.   
(ii) Labellings that are equivalent under the symmetry group are counted only once.   
(iii) If $( i , j )$ is a labelled edge then $i < j$ .

The number of distinct ways of labelling the given tree $t$ will be denoted by $\alpha ( t )$ . A similar question, in which conditions (i) and (ii) apply, but (iii) does not, leads to a function $\beta ( t )$ . We have:

Theorem 302A

$$
\begin{array} { l } { \displaystyle \alpha ( t ) = \frac { r ( t ) ! } { \sigma ( t ) \gamma ( t ) } , } \\ { \displaystyle \beta ( t ) = \frac { r ( t ) ! } { \sigma ( t ) } . } \end{array}
$$

Proof. The value of $\beta ( t )$ is found by labelling the vertices of $t$ with all permutations and then dividing by $\sigma ( t )$ so as to count, only once, sets of labellings which are equivalent under symmetry. In the case of $\alpha ( t )$ , we are restricted by the requirement that, of the labels assigned to any vertex $\boldsymbol { v }$ and to its descendants, only the lowest may be assigned to $v$ . The product of the factors that must be divided out to satisfy this constraint is $\gamma ( t )$ . $\boxed { \begin{array} { r l } \end{array} }$

We now look at the enumeration question of the number of rooted trees of various orders.

Theorem 302B Let $\theta _ { k }$ , $k = 1 , 2 , 3 , \dots$ . denote the number of rooted trees with exactly $k$ vertices. Then,

$$
\theta _ { 1 } + \theta _ { 2 } x + \theta _ { 3 } x ^ { 2 } + \cdot \cdot \cdot = ( 1 - x ) ^ { - \theta _ { 1 } } ( 1 - x ^ { 2 } ) ^ { - \theta _ { 2 } } ( 1 - x ^ { 3 } ) ^ { - \theta _ { 3 } } \cdot \cdot \cdot \cdot .
$$

Before proving this result, we consider how (302c) is to be interpreted. The right-hand side can be formally expanded as a power series, and it can be seen that the coefficient of $x ^ { k }$ depends only on $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots , \theta _ { k }$ (and is independent of any of $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ if $k = 0$ ). Equate this to the coefficient of $x ^ { k }$ on the left-hand side and the result is a formula for $\theta _ { k + 1 }$ in terms of previous members of the $\theta$ sequence. In particular, $k = 0$ gives $\theta _ { 1 } = 1$ . We now turn to the justification of the result.

Proof. Let $\Theta _ { k } ( U )$ denote the number of trees of order $k$ that can be formed using the operation $( t _ { 1 } , t _ { 2 } , \ldots , t _ { n } ) \mapsto [ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } ]$ , where $t _ { 1 }$ , $t _ { 2 }$ , $\cdot \cdot \cdot$ , $t _ { n }$ are all members of $U$ which is assumed to be a subset of $T$ . In particular, $\Theta _ { k } ( T )$ is identical to $\theta _ { k }$ . Let $V$ denote the set $U \cup \{ \hat { t } \}$ , where ${ \hat { t } } \notin U$ . Every tree of the form $[ \hat { t } ^ { m } , \dots ]$ , with order $k$ , is included in a set with $\Theta _ { k } ( V ) - \Theta _ { k } ( U )$ members. However, there are the same number of members of this set as there are trees of order $k - r ( \hat { t } )$ of the form $[ \hat { t } ^ { m - 1 } , \dots ]$ . Thus, $\Theta _ { k } ( V ) - \Theta _ { k } ( U ) = \Theta _ { k - r ( \hat { t } ) } ( V )$ , which is equivalent to

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = ( 1 - x ^ { r ( \hat { t } ) } ) ( \Theta _ { 1 } ( V ) + \Theta _ { 2 } ( V ) x + \cdots ) .
$$

Since

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdot \cdot \cdot = 1 ,
$$

when $U$ is the empty set, we can successively compute the value of this expression when $U = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } \}$ using (302d) as

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = \prod _ { k = 1 } ^ { n } ( 1 - x ^ { r ( t _ { k } ) } ) ^ { - 1 } .
$$

Now assume that $t _ { 1 }$ , $t _ { 2 } , \ldots$ consist of all trees of orders up to some integer $p$ , and we can write (302e) as

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = \prod _ { k = 1 } ^ { p } ( 1 - x ^ { k } ) ^ { - \theta _ { k } } .
$$

Since $\textstyle \prod _ { k = 1 } ^ { \infty }$ . $\Theta _ { i } ( U ) = \theta _ { i }$ if $i \le p + 1$ , we obtain the result by replacing $\textstyle \prod _ { k = 1 } ^ { p }$ by $\boxed { \begin{array} { r l } \end{array} }$

The values of $\theta _ { k }$ , computed using Theorem 302B, are shown in Table $3 0 2 ( \mathrm { I } )$ up to order 10. Also shown are the total numbers of trees up to a given order, and two further functions equal to the totals of the $\alpha ( t )$ and $\beta ( t )$ values for each order.

Various enumerations of rooted trees up to order 10   

<table><tr><td>n</td><td>0n</td><td>∑i=10i ∑r(t)=n a(t) ∑r(t)=n β(t)</td></tr><tr><td>1 1</td><td></td><td>1 1</td></tr><tr><td>2</td><td>1 2</td><td>1</td></tr><tr><td>3</td><td>2 4</td><td>2 9</td></tr><tr><td>4</td><td>4 8</td><td>6</td></tr><tr><td>5</td><td>9 17</td><td>24 625</td></tr><tr><td>6</td><td>20 37</td><td>120 7776</td></tr><tr><td>7</td><td>48 85</td><td>720 117649</td></tr><tr><td>8</td><td>115 200</td><td>5040 2097152</td></tr><tr><td>9 286</td><td>486</td><td>40320 43046721</td></tr><tr><td>10 719</td><td>1205</td><td>362880 1000000000</td></tr></table>

The entries in last two columns of Table 302(I) are important in classical combinatorics, although their roles in our work is only incidental. The sum of the $\beta ( t )$ for $r ( t ) = n$ is the number of fully labelled rooted trees with $n$ vertices, whereas the corresponding sum for $\alpha ( t )$ is the number of monotonically labelled rooted trees. It is easy to guess a formula for each of these totals, and we now verify these.

Theorem 302C Let $\begin{array} { r } { A _ { n } = \sum _ { r ( t ) = n } \alpha ( t ) , B _ { n } = \sum _ { r ( t ) = n } \beta ( t ) } \end{array}$ . Then

$$
A _ { n } = ( n - 1 ) ! , \quad B _ { n } = n ^ { n - 1 } .
$$

Proof. Let $X _ { n }$ denote the set of vectors of the form $[ x _ { 1 } , x _ { 2 } , \dotsc , x _ { n - 1 } ]$ and $Y _ { n }$ the set of vectors of the form $\left[ y _ { 1 } , y _ { 2 } , \dotsc , y _ { n - 1 } \right]$ , where $x _ { i } \in \{ 1 , 2 , \ldots , i \}$ and $y _ { i } \in \{ 1 , 2 , . . . , n \}$ , for $i = 1 , 2 , \ldots , n$ . It is easy to see that the cardinalities of these sets are $\# X _ { n } = ( n - 1 ) !$ , $\# Y _ { n } = n ^ { n - 1 }$ . We conclude the proof by showing how to define bijections between the monotonically labelled rooted trees of order $n$ and $X _ { n }$ and between the fully labelled rooted trees of order $n$ and $Y _ { n } .$ In each case, given a labelled rooted tree, let $v$ denote the leaf with greatest label and assign, as the value of $x _ { n - 1 }$ or $y _ { n - 1 }$ , respectively, the label attached to the parent of $v$ . Delete the leaf $v$ and continue the process until only the root remains. That is, in step $i = 1 , 2 , \ldots , n - 1$ , we work with a tree with $n + 1 - i$ vertices. We assign to $x _ { n - i }$ (or to $y _ { n - i }$ , respectively) the label attached to the parent of the leaf with the highest remaining label, and then delete this leaf to yield a tree with $n - i$ vertices. 

Although we have not included details of the bijections involved in this summarized proof, we illustrate these in the cases $n = 4$ , for monotonically labelled trees in Table 302(II), and $n = 3$ , for fully labelled trees in Table 302(III).

The bijection relating a monotonically labelled fourth order tree $t$ and $x \in X _ { 4 }$   

<table><tr><td>x</td><td>t</td><td>x t</td><td>x t</td></tr><tr><td>[1,1,1] 2</td><td>[1,1,2] 3</td><td>4 [1,1,3]</td><td>.4 3</td></tr><tr><td>[1,2,1] 4</td><td>3 [1,2,2]</td><td></td><td>E [1,2,3]</td></tr></table>

The bijection relating a fully labelled third order tree $t$ and $y \in Y _ { 3 }$

<table><tr><td>y t</td><td>y</td><td>t y</td><td>t</td></tr><tr><td>[1,1] 2 3</td><td>F [1,2]</td><td>[1,3]</td><td>5</td></tr><tr><td>[2,1] 1</td><td>[2,2]1</td><td>[2,3]</td><td>E</td></tr><tr><td>L [3,1]</td><td>E [3,2]</td><td></td><td></td></tr></table>
