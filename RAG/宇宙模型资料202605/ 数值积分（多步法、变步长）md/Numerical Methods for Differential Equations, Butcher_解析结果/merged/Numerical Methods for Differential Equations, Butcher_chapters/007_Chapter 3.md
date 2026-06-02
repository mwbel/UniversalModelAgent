# Chapter 3

# Runge–Kutta Methods

# 30 Preliminaries

# 300 Rooted trees

We saw in Section 23 that the graphs known as ‘rooted trees’ play a central role in the analysis of the accuracy of Runge–Kutta methods. We regard a rooted tree as a pair $( V , E )$ , where $V$ is a finite set of ‘vertices’ and $E$ a set of ‘edges’. The edges consist of ordered pairs of members of $V$ , subject to certain conditions. The first condition is that every member of $V$ , except one element known as the ‘root’, occurs exactly once amongst the second member in each pair in $E$ . The special root vertex does not occur as the second member of any pair. For the final condition, for $( V , E )$ to be a rooted tree, there are two alternatives, which are known to be equivalent: the first is that the graph defined by $( V , E )$ is connected; and the second is that $( V , E )$ defines a partial ordering.

It will be convenient, throughout this discussion, to refer to members of $V$ which do not occur as the first member of any pair in $V$ . For a given edge $[ x , y ] \in E$ , $x$ will be referred to as the ‘parent’ of $y$ and $y$ will be referred to as a ‘child’ of $x$ . Thus, a vertex may have one or more children but, if it has none, it is a leaf. Similarly every vertex, except the root, has exactly one parent, whereas the root has no parent.

We do not pursue the formal properties of graphs, and of rooted trees in particular, because they are formulated in specialist books on this subject and are easily appreciated through examples and diagrams. In diagrammatic depictions of a directed graph, the vertices are represented as points and the edges by arrowed line segments joining pairs of points, with the arrow pointing from the first to second member of the pair. We illustrate these ideas in Figure 300(i), where a number of rooted trees are shown. In contrast, Figure 300(ii) shows some graphs which are not rooted trees. In these figures, the members of $V$ are chosen to be positive integers. Wherever possible, the diagrams are arranged so that the root, if it exists, is at the bottom of the picture and so that all arrows are pointing in a direction with an upwards component.

Even though we are representing rooted trees using points, labelled by members of a vertex set, we are interested in the abstract structure behind this definition. That is, if $( V , E )$ and $( V ^ { \prime } , E ^ { \prime } )$ are rooted trees and there exists a bijection $\varphi : V \to V ^ { \prime }$ such that $[ x , y ] \in E$ if and only if $[ \varphi ( x ) , \varphi ( y ) ] \in E ^ { \prime }$ , then the two rooted trees are identical, when represented as diagrams, except for the labels attached to the points. We can thus regard an ‘abstract rooted tree’ as an equivalence class under this type of isomorphism. We use each interpretation from time to time, according to our convenience; where it is not clear from the context which is intended, we add some words of clarification. For a labelled tree $\mathbf { t }$ , the corresponding abstract tree will be denoted by |t|.

![](images/cd9df731d918dc43d7de8d1f6ec505a63837bff0e398c0f965c9b70531d816fe.jpg)  
Some directed graphs which are rooted trees

![](images/56ef01b02ac5a1b850d36907458b3785c59fdf9682f70c488c287e3e8e7979fc.jpg)  
Some directed graphs which are not rooted trees

To conclude this introduction to rooted trees, we present two alternative notations for trees. In each notation, we denote the single tree, with only one vertex, by the symbol $\tau$ . In the first notation, we consider a tree $t$ such that, when the root is removed, there remain a number of disconnected trees, say $t _ { 1 }$ , $t _ { 2 } , \ldots , t _ { m }$ , where $m$ is the number of ‘children’ of the root of $t$ . We then write $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ . This gives a recursion for constructing a symbolic denotation for any particular tree. When some of $t _ { 1 }$ , $t _ { 2 }$ , $\cdot \cdot \cdot$ , $t _ { m }$ are equal to each other, it will be convenient to represent these repetitions using a power notation. For example, $\left[ t _ { 1 } t _ { 1 } t _ { 2 } t _ { 2 } t _ { 2 } t _ { 3 } \right]$ will also be written as $[ t _ { 1 } ^ { 2 } t _ { 2 } ^ { 3 } t _ { 3 } ]$ .

The second notation builds up a symbolic representation of all trees by using a non-associative product of rooted trees, such that $t _ { 1 } t _ { 2 }$ is formed by joining them at the roots, with an additional edge from the root $v _ { 1 }$ of $t _ { 1 }$ to the root $v _ { 2 }$ of $t _ { 2 }$ . Thus if $t _ { 1 } = | ( V _ { 1 } , E _ { 1 } ) |$ and $t _ { 2 } = | ( V _ { 2 } , E _ { 2 } ) |$ , and $V _ { 1 }$ and $V _ { 2 }$ are disjoint sets, then $t _ { 1 } t _ { 2 }$ is the tree $| ( V _ { 1 } \cup V _ { 2 } , E _ { 1 } \cup E _ { 2 } \cup | v _ { 1 } , v _ { 2 } | ) |$ . Because the product is not associative, we need to distinguish between $( t _ { 1 } t _ { 2 } ) t _ { 3 }$ and $t _ { 1 } ( t _ { 2 } t _ { 3 } )$ without introducing more parentheses than necessary. Hence, we sometimes write $( t _ { 1 } t _ { 2 } ) t _ { 3 } = t _ { 1 } t _ { 2 } . t _ { 3 }$ and $t _ { 1 } ( t _ { 2 } t _ { 3 } ) = t _ { 1 } . t _ { 2 } t _ { 3 }$ .

Trees, notations for trees and various functions on trees   

<table><tr><td>r(t)</td><td>t</td><td></td><td></td><td>σ(t）γ(t)</td><td></td></tr><tr><td>1</td><td>·</td><td>T</td><td>T</td><td>1</td><td>1</td></tr><tr><td>2</td><td>：</td><td>[7]</td><td>TT</td><td>1</td><td>2</td></tr><tr><td>3</td><td>?</td><td>[r2]</td><td>TT.T</td><td>2</td><td>3</td></tr><tr><td>3</td><td></td><td>[]]</td><td>T.TT</td><td>1</td><td>6</td></tr><tr><td>4</td><td>：</td><td>[73]</td><td>(TT.T)T</td><td>6</td><td>4</td></tr><tr><td>4</td><td>山</td><td>[[]]</td><td>TT.TT = (T.TT)T</td><td>1</td><td>8</td></tr><tr><td>4</td><td></td><td>[r2]]</td><td>T(TT.T)</td><td>2</td><td>12</td></tr><tr><td>4</td><td>：</td><td>[[]]</td><td>T(T.TT)</td><td>1</td><td>24</td></tr><tr><td>5</td><td>V</td><td>[r4]</td><td>(TT.T)T.T</td><td>24</td><td>5</td></tr><tr><td>5</td><td>2</td><td>[r2[7]]</td><td>(T.TT)T.T = (TT.TT)T = (TT.T).TT</td><td>2</td><td>10</td></tr><tr><td>5</td><td></td><td>[[r2]]</td><td>TT.(TT.T) = T(TT.T).T</td><td>2</td><td>15</td></tr><tr><td>5</td><td></td><td>[7[[]]</td><td>T(T.TT).T = TT.(T.TT)</td><td>1</td><td>30</td></tr><tr><td>5</td><td></td><td>[[r]2]</td><td>(T.TT).TT</td><td>2</td><td>20</td></tr><tr><td>5</td><td></td><td>[[73]]</td><td>T.(TT.T)T</td><td>6</td><td>20</td></tr><tr><td>5</td><td></td><td>[7[7]]</td><td>T(TT.TT) = T.(T.TT)T</td><td>1</td><td>40</td></tr><tr><td>5</td><td></td><td>[[t2]]</td><td>T.T(TT.T)</td><td>2</td><td>60</td></tr><tr><td>5</td><td></td><td>[[7]]]</td><td>T.T(T.TT)</td><td>1</td><td>120</td></tr></table>

We illustrate these notations in Table $3 0 0 ( \mathrm { I } )$ , where all trees with up to five vertices are shown. Also shown are the functions $r ( t )$ , $\sigma ( t )$ and $\gamma ( t )$ to be introduced in the next subsection.

# 301 Functions on trees

For a rooted tree $t$ , define $r ( t )$ , the ‘order’ of $t$ , as the number of vertices in $t$ . That is, if $t$ is labelled as $( V , E )$ , then $r ( t ) = \# V$ , the cardinality of the set $V$ . Let $A ( t )$ denote the group of automorphisms on a particular labelling of $t$ . That is, $A ( t )$ is the set of mappings $\varphi : V \to V$ such that $[ x , y ] \in E$ if and only if $[ \varphi ( x ) , \varphi ( y ) ] \in E$ . The group $A ( t )$ will be known as the ‘symmetry group’ of $t$ ; its order will be known as the ‘symmetry’, and denoted by $\sigma ( t )$ . The ‘density’ of $t$ , $\gamma ( t )$ , is defined as the product over all vertices of the order of the subtree rooted at that vertex. We illustrate these definitions using a specific tree $( V , E )$ with nine vertices given by

$$
\begin{array} { l } { V = \{ a , b , c , d , e , f , g , h , i \} , } \\ { E = \{ [ a , b ] , [ a , c ] , [ b , d ] , [ b , e ] , [ b , f ] , [ c , g ] , [ c , h ] , [ c , i ] \} . } \end{array}
$$

The diagram representing this tree, with the vertex labels attached, is

![](images/aaf9e43c403d3660ad34a43fc74b050dd3c840c16d0ef3da920dffb45c36fb80.jpg)

The value of $r ( t )$ is, of course, 9. The symmetry group is the set of permutations generated by all members of the symmetric group on $\{ d , e , f \}$ , by all members of the symmetric group on $\{ g , h , i \}$ , and the group $S _ { 2 }$ generated by the single permutation, in which $b$ and $c$ are interchanged, $d$ and $g$ are interchanged, $e$ and $h$ are interchanged, and $f$ and $i$ are interchanged. Thus the order of the symmetry group is $\sigma ( t ) = 3 ! 3 ! 2 ! = 7 2$ . To calculate $\gamma ( t )$ , attach integers to the vertices as follows:

![](images/448ab88329382b747dfbf9dfbf70889cd0decda08d950502a305747f8eee3640.jpg)

leading to $\gamma ( t ) = 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 4 \cdot 4 \cdot 9 \ = 1 4 4$

We complete this subsection with a formal statement of recursions for the computation of $r ( t )$ , $\sigma ( t )$ and $\gamma ( t )$ .

Theorem 301A Let $t = [ t _ { 1 } ^ { \prime \prime \imath 1 } t _ { 2 } ^ { \prime \prime \imath 2 } \cdot \cdot \cdot t _ { k } ^ { \prime \prime \imath k } ]$ , where $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { k }$ are distinct trees. Then

$$
\begin{array} { l } { \displaystyle r ( t ) = 1 + \sum _ { i = 1 } ^ { k } m _ { i } r ( t _ { i } ) , } \\ { \displaystyle \sigma ( t ) = \prod _ { i = 1 } ^ { k } m _ { i } ! \sigma ( t _ { i } ) ^ { m _ { i } } , } \\ { \displaystyle \gamma ( t ) = r ( t ) \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) ^ { m _ { i } } . } \end{array}
$$

Furthermore,

$$
r ( \tau ) = \sigma ( \tau ) = \gamma ( \tau ) = 1 .
$$

Proof. To verify (301d), calculate $r$ , $\sigma$ and $\gamma$ for the single tree with one vertex. To prove (301a), add the numbers of vertices in the $m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { k }$ trees attached to the new root, and add one extra for the new root. In the calculation of $\gamma ( t )$ , the integers attached to the vertices in the $m _ { 1 } + m _ { 2 } +$ $\cdots + m _ { k }$ trees joined to the new root are the same as in the constituent trees themselves. The product of these integers, and the integer $r ( t )$ , gives the result (301c). Finally, (301b) follows by noting that the permutations which leave the vertex pairs, making up the list of edges, are just as in the individual attached trees, together with the additional permutations of the label sets amongst identical subtrees. 

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

# 303 The use of labelled trees

We have seen that $\alpha ( t )$ , introduced in Subsection 302, is the number of distinct ways of labelling the vertices of $t$ with the integers $\{ 1 , 2 , \ldots , r ( t ) \}$ , on condition that for each edge $( i , j )$ , $i < j .$ It is convenient to generalize this by writing $S$ for an finite ordered set such that the cardinality is $\# S = r ( t )$ , and counting trees labelled with members of $S$ such that $i < j$ for each edge $( i , j )$ . Let $T _ { S } ^ { * }$ denote the set of trees labelled in this way and let $| \mathbf t |$ denote the member of $T$ corresponding to $\mathbf { t } \in T _ { S } ^ { * }$ , but with the vertex labels removed. This means that $\alpha ( t )$ can be interpreted as the number of members of $T _ { S } ^ { * }$ such that $| \cdot |$ maps them to $t \in T$ . Similarly, we write $T _ { S }$ for the set of trees labelled by a set with cardinality $r ( t )$ , where no assumption is made about order. In this case $\beta ( t )$ is the number of $\mathbf { t } \in T _ { S }$ , such that $| \mathbf { t } | = t$ .

# 304 Enumerating non-rooted trees

Recall the generating function for the numbers of rooted trees of various orders

$$
\theta ( x ) = \theta _ { 1 } + \theta _ { 2 } x + \theta _ { 3 } x ^ { 2 } + \cdot \cdot \cdot ,
$$

![](images/00dff3eda7dd4af2044d9dda13be2eec775a97d03ed67464fab4d9661e03a211.jpg)  
Trees with up to six vertices

where $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ are given in (302c). Also write

$$
\begin{array} { l } { { \phi ( x ) = \phi _ { 1 } + \phi _ { 2 } x + \phi _ { 3 } x ^ { 2 } + \cdots , } } \\ { { \psi ( x ) = \psi _ { 1 } + \psi _ { 2 } x + \psi _ { 3 } x ^ { 2 } + \cdots , } } \end{array}
$$

as the generating functions for the numbers of trees $\phi _ { i }$ of orders $i = 1 , 2 , \dots$ and the numbers of non-superfluous trees $\psi _ { i }$ . The meaning of ‘superfluous tree’ will become clear from the discussion which follows.

Given a tree, we can form a family of rooted trees by designating one of its vertices to be the root. We will refer to two such rooted trees as adjacent if the two roots are at the ends of the same edge in the underlying tree. For any particular vertex $\boldsymbol { v }$ , let $t = \left\lfloor t _ { 1 } , t _ { 2 } , \ldots , t _ { m } \right\rfloor$ and write $\phi ( v ) = \mathrm { m a x } _ { i = 1 } ^ { m } r ( t _ { i } )$ . There will be at most one vertex adjacent to $\boldsymbol { v }$ for which the value of $\phi$ is lower. However, for some trees with even order there will be two adjacent vertices for which the values of $\phi$ are each equal to $r ( t ) / 2$ . The 14 trees with up to six vertices are shown in Figure $\mathrm { 3 0 4 ( i ) }$ . The value of $\phi$ is attached to each vertex, with arrows showing the direction of decreasing $\phi$ . In the cases of two adjacent vertices $\boldsymbol { v }$ and $w$ with $\phi ( v ) = \phi ( w )$ , two arrows are shown meeting midway through the edge.

For a rooted tree formed from a tree by selecting a vertex as the root, we can move along an arrow to obtain a vertex with a lower value of $\phi$ . Thus we should subtract from the total number of rooted trees of a given order $n$ , the number of pairs or trees with unequal orders. This means subtracting the number of rooted trees of the form $t u$ , where $r ( t ) < r ( u )$ . In the case of trees where $n = 2 m$ is even, and for two adjacent vertices, the rooted trees $t u$ and ut occur, where $r ( t ) = r ( u )$ , we need to subtract half the number of such trees unless $t = u$ , in which case no subtraction is performed.

For a tree of order $\textit { n } = \ 2 m + 1$ , the number of trees will thus be $\begin{array} { r } { \theta _ { n } - \sum _ { i = 1 } ^ { m } \theta _ { i } \theta _ { n - i } } \end{array}$ , which is the coefficient of $x ^ { n - 1 }$ in

$$
\theta ( x ) - \frac { x } { 2 } \Bigl ( \theta ( x ) ^ { 2 } \mp \theta ( x ^ { 2 } ) \Bigr ) ,
$$

where the term involving $\theta ( x ^ { 2 } )$ does not actually contribute to this case of odd $n$ . In the case of even $n = 2 m$ , the number of trees will be

$$
\theta _ { n } - \sum _ { i = 1 } ^ { m - 1 } \theta _ { i } \theta _ { n - i } - \frac 1 2 \theta _ { m } ( \theta _ { m } \mp 1 ) ,
$$

where $\mp$ is interpreted as $^ -$ , and this is again equal to the coefficient of $x ^ { n - 1 }$ in (304a).

Counting non-superfluous trees is the same except that we need to subtract from the totals the number of trees of the form $t t$ , and this gives the same result as (304a) but with $\mp$ replaced by $^ +$ . Putting these results together we formally state:

Theorem 304A The generating functions for trees and non-superfluous trees are

$$
\begin{array} { c } { { \phi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } - \theta ( x ^ { 2 } ) \Big ) , } } \\ { { \psi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } + \theta ( x ^ { 2 } ) \Big ) . } } \end{array}
$$

# 305 Differentiation

We need to develop fairly intricate formulae involving derivatives of vectorvalued functions of vector arguments. Hence, in this subsection and the next, we review basic calculus ideas in a vector setting. We start with the elementary notions of the derivative of a real-valued function of a single real variable, and the partial derivatives of a real-valued function of several real variables. A real-valued function $f$ , whose domain contains an open interval around the real number $a$ , is differentiable at $a$ if there exists a number $f ^ { \prime } ( a )$ , referred to as the derivative of $f$ at $a$ , such that $| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta | / | \delta | \to 0$ a s $| \delta | \to 0$ . This definition is extended in two ways. First, $f$ can take values in $\mathbb { R } ^ { N }$ , in which case $f$ is differentiable if each of its components is differentiable. Furthermore, $f ^ { \prime } ( a ) \in \mathbb { R } ^ { N }$ is equal to the vector made up from the derivatives of the components of $f$ . Another way of writing this is

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { | \delta | } } \to 0 \quad { \mathrm { a s ~ } } | \delta | \to 0 .
$$

When the domain of $f$ is generalized to $X \subset \mathbb { R } ^ { M }$ , such that $a \in O \subset X$ , where $O$ is an open set, such as a product of open intervals, then $f ^ { \prime } ( a )$ , if it

exists, is a linear operator, $f ^ { \prime } ( a ) : \mathbb { R } ^ { M } \longrightarrow \mathbb { R } ^ { N }$ , such that

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { \| \delta \| } } \to 0 \quad { \mathrm { a s ~ } } \| \delta \| \to 0 .
$$

If the components of $a$ and $f$ are written as

$$
a = \left[ \begin{array} { c } { { a ^ { 1 } } } \\ { { a ^ { 2 } } } \\ { { \vdots } } \\ { { a ^ { M } } } \end{array} \right] , \qquad f = \left[ \begin{array} { c } { { f ^ { 1 } } } \\ { { f ^ { 2 } } } \\ { { \vdots } } \\ { { f ^ { N } } } \end{array} \right] ,
$$

then the linear operator $f ^ { \prime } ( a )$ is represented by the matrix of partial derivatives

$$
{ \bf \\xi } ^ { \prime } ( a ) = \left[ { \begin{array} { c c c c } { f _ { 1 } ^ { 1 } ( a ) } & { f _ { 2 } ^ { 1 } ( a ) } & { \cdots } & { f _ { M } ^ { 1 } ( a ) } \\ { f _ { 1 } ^ { 2 } ( a ) } & { f _ { 2 } ^ { 2 } ( a ) } & { \cdots } & { f _ { M } ^ { 2 } ( a ) } \\ { \vdots } & { \vdots } & & { \vdots } \\ { f _ { 1 } ^ { N } ( a ) } & { f _ { 2 } ^ { N } ( a ) } & { \cdots } & { f _ { M } ^ { N } ( a ) } \end{array} } \right] = \left[ { \begin{array} { c c c c } { { \frac { \partial f ^ { 1 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { M } } } } \\ { { \frac { \partial f ^ { 2 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { M } } } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { { \frac { \partial f ^ { N } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { N } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { N } } { \partial a ^ { M } } } } \end{array} } \right] .
$$

Second and higher derivatives are bilinear and multilinear operators. In the tensor representation

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } ( a ) = { \frac { \partial ^ { k } f ^ { i } } { \partial a _ { j _ { 1 } } \partial a _ { j _ { 2 } } \cdot \cdot \cdot \partial a _ { j _ { k } } } } ,
$$

the argument ( $a$ ) is omitted, for convenience, if its value is understood.

Finally, inoperating wicollection of this subsech the order arguments $k$ $f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i }$ at eva, as a gives $k$ uation of the result of-linear operator, on thehe expression $k$ $v _ { 1 } , v _ { 2 } , \ldots , v _ { k } \in \mathbb { R } ^ { M }$

$$
\sum _ { j _ { 1 } = 1 } ^ { M } \sum _ { j _ { 2 } = 1 } ^ { M } \cdot \cdot \cdot \sum _ { j _ { k } = 1 } ^ { M } f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

The complicated appearance of (305a) can be alleviated by omitting all the summation symbols and regarding them as implied. This is the wellknown ‘summation convention’, and we use this notational simplification freely throughout this book. Thus we write, instead of (305a),

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

Members of $\mathcal { I } _ { 2 }$ and their symmetries

$$
\sigma ( I ) | \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { I } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } &  { } \end{array}
$$

# 306 Taylor’s theorem

We start from the identity,

$$
\begin{array} { r } { f ( a + \delta ) = f ( a ) + f ^ { \prime } ( a ) ( \delta ) + \frac { 1 } { 2 ! } f ^ { \prime \prime } ( a ) ( \delta , \delta ) \qquad } \\ { + \dots + \displaystyle \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } , } \end{array}
$$

where the ‘remainder’ $R _ { n }$ is given by

$$
R _ { n } = \frac { 1 } { n ! } \int _ { 0 } ^ { 1 } f ^ { ( n + 1 ) } ( a + \xi \delta ) ( \delta , \delta , \ldots , \delta ) ( 1 - \xi ) ^ { n } d \xi .
$$

This is proved by induction, with the key step being

$$
R _ { n - 1 } = \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } ,
$$

which is verified by integration by parts. With Taylor’s theorem written in the form (306a), the result is quite versatile and applies if $f : X \subset \mathbb { R } ^ { M } \to \mathbb { R } ^ { N }$ , where $a + \xi \delta \in O \subset X$ , for all $\xi \in [ 0 , 1 ]$ . Assuming that $\| f ^ { ( n + 1 ) } ( x ) \|$ exists and is bounded for $x \in O$ , then

$$
\| R _ { n } \| = O ( \| \delta \| ^ { n + 1 } ) .
$$

We consider a slight variation of the theorem, in which $\delta$ is replaced by the sum of a finite number of vectors, $\delta _ { i }$ , $i = 1 , 2 , \dots , m$ . We assume that $f$ is analytic in a neighbourhood of $a$ and that each of the $\delta _ { i }$ is small. The formal result we present can be interpreted as a finite series, together with remainder, with the details dependent on the relative magnitudes of the $\delta _ { i }$ . Let $I$ denote a sequence of integers from the set $\{ 1 , 2 , \ldots , m \}$ and $\mathcal { L } _ { m }$ the set of all such sequences. Two sequences $I$ and $I ^ { \prime }$ will be regarded as identical if the members of $I ^ { \prime }$ are a permutation of the members of $I$ . The ‘symmetry’ of $I$ is the order of the group of permutations of the elements of $\{ 1 , 2 , \ldots , \# I \}$ , which maps the ordered members of $I$ to themselves. That is, if $I$ contains $k _ { i }$ occurrences of $i$ , for each $i = 1 , 2 , \dots , m$ , then

$$
\sigma ( I ) = k _ { 1 } ! k _ { 2 } ! \cdot \cdot \cdot k _ { m } ! .
$$

For $m = 2$ , the first few $I \in \mathcal { I } _ { m }$ , together with the corresponding symmetries, are given in Table 306(I).

For $I = ( i _ { 1 } , i _ { 2 } , \ldots , i _ { k } ) \in { \mathcal { T } } _ { m }$ , we denote by $\delta _ { I }$ the quantity

$$
( \delta _ { i _ { 1 } } , \delta _ { i _ { 2 } } , \ldots , \delta _ { i _ { m } } ) \in ( \mathbb { R } ^ { N } ) ^ { m } .
$$

These will be used as operands for multilinear operators, such as $f ^ { ( m ) } ( a )$ , and, in the case $I = ( )$ , we interpret $f ( a ) ( )$ as being simply $f ( a )$ . We are now in a position to state the form of the Taylor expansion (306a), when $\delta$ is replaced by $\textstyle \sum _ { i = 1 } ^ { \cdot { m } } \delta _ { i }$ .

Theorem 306A

$$
f \biggl ( a + \sum _ { i = 1 } ^ { m } \delta _ { i } \biggr ) = \sum _ { I \in \mathcal { T } _ { m } } \frac { 1 } { \sigma ( I ) } f ^ { ( \# I ) } ( a ) \delta _ { I } .
$$

Proof. Continue to write $k _ { i }$ for the number of occurrences of $i$ in $I$ , so that $\sigma ( I )$ is given by (306b). The coefficient of $f ^ { ( \# I ) } ( a ) \delta _ { I }$ is equal to the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in $\textstyle \exp \left( \sum _ { i = 1 } ^ { m } x _ { i } \right)$ . This equals the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in

$$
\begin{array} { r } { \left( 1 + x _ { 1 } + \frac { 1 } { 2 ! } x _ { 1 } ^ { 2 } + \cdot \cdot \cdot \right) \left( 1 + x _ { 2 } + \frac { 1 } { 2 ! } x _ { 2 } ^ { 2 } + \cdot \cdot \cdot \right) \cdot \cdot \left( 1 + x _ { m } + \frac { 1 } { 2 ! } x _ { m } ^ { 2 } + \cdot \cdot \cdot \right) } \end{array}
$$

and is equal to $1 / \sigma ( I )$ .

We illustrate this result by applying (306A) to the case $m = 2$ , using Table 306(I):

$$
\begin{array} { r l } & { f ( a + \delta _ { 1 } + \delta _ { 2 } ) = f ( a ) + f ^ { \prime } ( a ) \delta _ { 1 } + f ^ { \prime } ( a ) \delta _ { 2 } + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } , \delta _ { 2 } ) + \cdots \ . } \end{array}
$$

# Exercises 30

30.1 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = | \mathbf { t } |$ , where $| \mathbf { t } | = ( V , E )$ , with

$$
V = \{ a , b , c , d , e , f , g \} \mathrm { ~ a n d ~ } E = \{ ( a , b ) , ( b , c ) , ( b , d ) , ( a , e ) , ( e , f ) , ( e , g ) \} .
$$

30.2 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = [ [ \tau ] ^ { 2 } \tau ^ { 3 } ]$ .

30.3 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = \tau \tau \cdot ( \tau \tau \cdot \tau ) \tau$ .

30.4 Define $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ by

$$
f ( y ^ { 1 } , y ^ { 2 } , y ^ { 3 } ) = \left[ \begin{array} { c } { { y ^ { 1 } + y ^ { 2 } y ^ { 3 } } } \\ { { ( y ^ { 1 } ) ^ { 2 } + 2 y ^ { 1 } y ^ { 2 } } } \\ { { 1 + ( y ^ { 2 } + y ^ { 3 } ) ^ { 2 } } } \end{array} \right] .
$$

Find formulae for $f _ { j } ^ { i }$ , $f _ { j k } ^ { i }$ and $f _ { j k l } ^ { \imath }$ , for $i , j , k , l = 1 , 2 , 3$ .

30.5 Expand $f ( a + \delta _ { 1 } \xi + \delta _ { 2 } \xi ^ { 2 } + \delta _ { 3 } \xi ^ { 3 } )$ up to terms in $\xi ^ { 3 }$ using Theorem 306A.

# 31 Order Conditions

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

# 311 The Taylor expansion of the exact solution

We approach the question of the Taylor series of the exact solution from two points of view. In the first, we evaluate the Taylor coefficients by repeated differentiation, as we have illustrated in Subsection 310. In the second, we successively find Taylor series for the Picard iterates.

The central result in the first approach is an expression for the derivatives written in terms of labelled trees. Throughout the discussion it will be assumed, without further comment, that $y$ is a solution to $y ^ { \prime } ( x ) = f ( y ( x ) )$ and that $y$ is differentiable arbitrarily often. First, we need a formula for the derivative of a single elementary differential.

Lemma 311A Let $S = S _ { 0 } \cup \{ s \}$ be an ordered set, where every member of $S _ { 0 }$ is less than $s$ . Let $\mathbf { t }$ be a member of $T _ { S _ { 0 } } ^ { * }$ . Then

$$
{ \frac { d } { d x } } F ( | \mathbf { t } | ) ( y ( x ) )
$$

is the sum of $F ( | \mathbf { u } | ) ( y ( x ) )$ over all $\mathbf { u } \in T _ { S } ^ { * }$ such that the subtree formed by removing $s$ from the set of vertices is $\mathbf { t }$ .

Proof. If $S = \{ s _ { 0 } , s \}$ , then the result is equivalent to

$$
{ \frac { d } { d x } } f ( y ( x ) ) = f ^ { \prime } ( y ( x ) ) f ( y ( x ) ) .
$$

We now complete the proof by induction in the case $S = \{ s _ { 0 } \} \cup S _ { 1 } \cup S _ { 2 } \cup \cdot \cdot \cdot \cup$ $S _ { k } \cup \{ s \}$ , where $\left\{ s _ { 0 } \right\}$ , $S _ { 1 }$ , $S _ { 2 }$ , . . . , $S _ { k }$ , $\{ s \}$ are disjoint subsets of the ordered set $S$ . By the induction hypothesis, assume that the result of the lemma is true, when $S$ is replaced by $S _ { i }$ , $i = 1 , 2 , \ldots , k$ . If $\mathbf { t } \in T _ { S _ { 0 } } ^ { * }$ , then

$$
| \mathbf { t } | = [ \left| \mathbf { t } _ { 1 } \right| \left| \mathbf { t } _ { 2 } \right| \cdot \cdot \cdot \left| \mathbf { t } _ { k } \right| ] ,
$$

where $\mathbf { t } _ { i } \in T _ { S _ { i } } ^ { * }$ , $i = 1 , 2 , \ldots , k$ . Differentiate

$$
\begin{array} { r l } & { F ( | \mathbf { t } | ) ( y ( x ) ) } \\ & { \qquad = f ^ { ( k ) } ( y ( x ) ) \bigl ( F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \dots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) \bigr ) , } \end{array}
$$

to obtain

$$
Q _ { 0 } + Q _ { 1 } + Q _ { 2 } + \cdot \cdot \cdot + Q _ { k } ,
$$

where

$$
Q _ { 0 } = f ^ { ( k + 1 ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) , f ( y ( x ) ) { \big ) }
$$

and, for $i = 1 , 2 , \ldots , k$ ,

$$
Q _ { i } = f ^ { ( k ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , \ldots , { \frac { d } { d x } } F ( | \mathbf { t } _ { i } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) { \big ) } .
$$

The value of $Q _ { 0 }$ is

$$
F ( \left[ \left. \mathbf { t } _ { 1 } \right. \left. \mathbf { t } _ { 2 } \right. \cdot \cdot \cdot \left. \mathbf { t } _ { k } \right. \left. \mathbf { t } _ { 0 } \right. \right] ) ( y ( x ) ) ,
$$

where $| \mathbf { t } _ { 0 } |$ is $\tau$ labelled with the single label $s$ . For $i = 1 , 2 , \ldots , k$ , the value of $Q _ { i }$ is the sum of all terms of the form (311a), with $F ( | \mathbf { t } _ { i } | ) ( y ( x ) )$ replaced by terms of the form $F ( | \mathbf { u } _ { i } | ) ( y ( x ) )$ , where $\mathbf { u } _ { i }$ is formed from $\mathbf { t } _ { i }$ by adding an additional leaf labelled by $s$ . The result of the lemma follows by combining all terms contributing to the derivative of (311a).

Theorem 311B Let $S$ denote a finite ordered set. Then

$$
y ^ { ( \# S ) } ( y _ { 0 } ) = \sum _ { \mathbf { t } \in T _ { S } } F ( | \mathbf { t } | ) ( y _ { 0 } ) .
$$

Proof. In the case $| \mathbf { t } | = \tau$ , the result is obvious. For the case $\# S > 1$ , apply Lemma 311A repeatedly by adding additional (and increasing) members to $S$ . 

We rewrite this result in terms of unlabelled trees, by noting that the number of times that a tree $t$ with order $\# S$ occurs as the unlabelled counterpart of a member of $T _ { S } ^ { * }$ , is exactly $\alpha ( t )$ .

# Theorem 311C

$$
y ^ { ( n ) } ( y ( x ) ) = \sum _ { t \in T _ { n } } \alpha ( t ) F ( t ) ( y ( x ) ) .
$$

The alternative approach to finding the Taylor coefficients is based on the Picard integral equation

$$
y ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y ( x _ { 0 } + h \xi ) ) d \xi ,
$$

which, written in terms of Picard iterations, becomes

$$
y _ { n } ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y _ { n - 1 } ( x _ { 0 } + h \xi ) ) d \xi ,
$$

where the initial iterate is given by

$$
y _ { 0 } ( x + h \xi ) = y ( x _ { 0 } ) .
$$

For $n = 1 , 2 , \ldots$ , we expand $y _ { n } ( x _ { 0 } + h \xi )$ for $\xi \in [ 0 , 1 ]$ , omitting terms that are $O ( h ^ { n + 1 } )$ .

Theorem 311D The Taylor expansion of $y _ { n }$ given by (311b) and (311c) is equal to

$$
y _ { n } = y ( x _ { 0 } ) + \sum _ { i = 1 } ^ { n } h ^ { i } \xi ^ { i } \sum _ { t \in T _ { i } } \frac { 1 } { \sigma ( t ) \gamma ( t ) } F ( t ) ( y ( x _ { 0 } ) ) + O ( h ^ { n + 1 } ) .
$$

Proof. The case $n = 0$ is obvious. We now use induction and suppose that (311d) is true with $n$ replaced by $n - 1$ . By Lemma 310B, with

$$
\theta ( t ) = \frac { 1 } { \gamma ( t ) } ,
$$

we have as the coefficient of $F ( t ) ( y ( x _ { 0 } ) ) h ^ { r ( t ) }$ , the expression

$$
\int _ { 0 } ^ { \xi } \frac { 1 } { \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) - 1 } { d \xi } = \frac { 1 } { r ( t ) \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) } = \frac { 1 } { \gamma ( t ) } \xi ^ { r ( t ) } ,
$$

where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ .

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

# 313 The Taylor expansion of the approximate solution

We show that the result output by a Runge–Kutta methods is exactly the same as (311d), except that the factor $\gamma ( t ) ^ { - 1 }$ is replaced by $\Phi ( t )$ . We first establish a preliminary result.

Lemma 313A Let $k = 1 , 2 , \ldots ,$ . If

$$
Y _ { i } = y _ { 0 } + \sum _ { r ( t ) \leq k - 1 } { \frac { 1 } { \sigma ( t ) } } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k } ) ,
$$

then

$$
h f ( Y _ { i } ) = \sum _ { r ( t ) \leq k } \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k + 1 } ) .
$$

Proof. Use Lemma 310B. The coefficient of $\sigma ( t ) ^ { - 1 } F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in $h f ( Y _ { i } )$ is $\textstyle \prod _ { j = 1 } ^ { n } \Phi _ { i } ( t _ { j } )$ , where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ . $\boxed { \begin{array} { r l } \end{array} }$

We are now in a position to derive the formal Taylor expansion for the computed solution. The proof we give for this result is for a general Runge– Kutta method that may be implicit. In the case of an explicit method, the iterations used in the proof can be replaced by a sequence of expansions for $Y _ { 1 }$ , for $h f ( Y _ { 1 } )$ , for $Y _ { 2 }$ , for $h f ( Y _ { 2 } )$ , and so on until we reach $Y _ { s }$ , $h f ( Y _ { s } )$ and finally $y _ { 1 }$ .

Theorem 313B The Taylor expansions for the stages, stage derivatives and output result for a Runge–Kutta method are

$$
\begin{array} { c } { { Y _ { i } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle h f ( Y _ { i } ) = \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) . } } \end{array}
$$

Proof. In a preliminary part of the proof, we consider the sequence of approximations to $Y _ { i }$ given by

$$
\begin{array} { l l } { { { \displaystyle Y _ { i } ^ { [ 0 ] } = y _ { 0 } } , } } & { { i = 1 , 2 , \ldots , s , } } \\ { { { \displaystyle Y _ { i } ^ { [ k ] } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f \left( Y _ { j } ^ { [ k - 1 ] } \right) , \ } } } & { { i = 1 , 2 , \ldots , s . } } \end{array}
$$

We prove by induction that Y [n]i agrees with the expression given for $Y _ { i }$ to within $O ( h ^ { n + 1 } ) .$ For $n = 0$ this is clear. For $n > 0$ , suppose it has been proved for $n$ replaced by $n - 1$ . From Lemma 313A with $k = n - 1$ and $Y _ { i }$ replaced by $Y _ { i } ^ { \lfloor n - 1 \rfloor }$ , we see that

$$
k f ( Y _ { i } ^ { [ n - 1 ] } ) = \sum _ { r ( t ) \leq n } { \frac { 1 } { \sigma ( t ) } } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { n + 1 } ) , \quad i = 1 , 2 , \ldots , s .
$$

Calculate Y [n]i using (313c) and the preliminary result follows. Assume $h$ tly to mall to guarantee convergence of the sequenceand (313c) follows. Finally, (313d) follows from $( Y _ { i } ^ { [ 0 ] } , Y _ { i } ^ { [ 1 ] } , Y _ { i } ^ { [ 2 ] } , \dots )$ $Y _ { i }$ Lemma 313A and (313e) from (312d). 

# 314 Independence of the elementary differentials

Our aim of comparing the Taylor expansions of the exact and computed solutions to an initial value problem will give an inconclusive answer unless the terms involving the various elementary differentials can be regarded as independent. We introduce a special type of differential equation for which any finite number of elementary differentials evaluate to independent vectors.

Let $U$ denote any finite subset of $T$ , such that if

$$
t _ { i } = [ t _ { 1 } ^ { m _ { 1 } } , t _ { 2 } ^ { m _ { 2 } } , \ldots , t _ { k } ^ { m _ { k } } ] \in U ,
$$

Trees to order 4 with corresponding differential equations   

<table><tr><td>i</td><td colspan="2">ti</td><td>yi</td><td>=fi</td></tr><tr><td>1</td><td>.</td><td></td><td>[]</td><td>y=1,</td></tr><tr><td>2</td><td></td><td>：</td><td>[t1]</td><td>y= y1,</td></tr><tr><td>3</td><td>?</td><td></td><td>[t]</td><td>y=y²，</td></tr><tr><td>4</td><td></td><td></td><td>[t2]</td><td>y4=y2,</td></tr><tr><td>5</td><td>?</td><td></td><td>[t]</td><td>y5=y，</td></tr><tr><td>6</td><td></td><td></td><td>[t1t2]</td><td>y = y1y2,</td></tr><tr><td>7</td><td>丫</td><td>：</td><td>[t3]</td><td>y= y3,</td></tr><tr><td>8</td><td></td><td></td><td>[t4]</td><td>y&#x27;s= y4.</td></tr></table>

then each of $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { k }$ is also a member of $U$ . For example, $U$ might consist of all trees with orders up to some specified integer. Assume that when we write a tree in this way, the $t _ { i }$ , $i = 1 , 2 , \ldots , k$ , are all distinct. Suppose that $N$ is the number of members of $U$ , and consider the $m$ -dimensional differential equation system in which

$$
y _ { i } ^ { \prime } = \prod _ { j = 1 } ^ { k } \frac { y _ { j } ^ { m _ { j } } } { m _ { j } ! } ,
$$

corresponding to tree number $i$ defined in (314a). The initial values are supposed to be $y _ { i } ( 0 ) ~ = ~ y _ { i } ( x _ { 0 } ) ~ = ~ 0$ , for $i = 1 , 2 , \ldots , N$ . The interesting property of this initial value problem is encapsulated in the following result:

Theorem 314A The values of the elementary differentials for the differential equation (314b), evaluated at the initial value, are given by

$$
F ( t _ { i } ) ( y ( x _ { 0 } ) ) = e _ { i } , \qquad i = 1 , 2 , \ldots , N .
$$

Because the natural basis vectors $e _ { 1 } , e _ { 2 } , \ldots , e _ { N }$ are independent, there cannot be any linear relation between the elementary differentials for an arbitrary differential equation system.

We illustrate this theorem in the case where $U$ consists of the eight trees with up to four vertices. Table 314(I) shows the trees numbered from $i = 1$ to $i = 8$ , together with their recursive definitions in the form (314a) and the corresponding differential equations. Note that the construction given here is given as an exercise in Hairer, Nørsett and Wanner (1993) .

# 315 Conditions for order

Now that we have expressions for the Taylor expansions of the exact solution, and also of the computed solution, we have all we need to find conditions for order. If the exact solution has Taylor series given by (311d) and the approximate solution has Taylor series given by (313e), then we need only compare these term by term to arrive at the principal result on the order of Runge–Kutta methods.

Theorem 315A A Runge–Kutta method with elementary weights

$$
\Phi : T  \mathbb { R } ,
$$

has order $p$ if and only if

$$
\Phi ( t ) = { \frac { 1 } { \gamma ( t ) } } , { \mathrm { ~ } } f o r { \mathrm { ~ } } a l l \ t \in T { \mathrm { ~ } } s u c h { \mathrm { ~ } } t h a t r ( t ) \leq p .
$$

Proof. The coefficient of $F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in (313e) is $\begin{array} { r } { \frac { 1 } { \sigma ( t ) } \Phi ( t ) } \end{array}$ , compared with the coefficient in (311d), which is $\frac { 1 } { \sigma ( t ) \gamma ( t ) }$ . Equate these coefficients and we obtain (315a). $\boxed { \begin{array} { r l } \end{array} }$

# 316 Order conditions for scalar problems

Early studies of Runge–Kutta methods were built around the single scalar equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) .
$$

Even though it was always intended that methods derived for (316a) should be interpreted, where appropriate, in a vector setting, a subtle difficulty arises for orders greater than 4.

We adopt the notation $f _ { x }$ , $f _ { y }$ for partial derivatives of $f$ with respect to the first and second arguments, with similar notations for higher derivatives. Also, for simplicity, we omit the arguments in expressions like $f _ { x } ( x , y )$ . By straightforward differentiation of (316a), we have

$$
y ^ { \prime \prime } = f _ { x } + f _ { y } y ^ { \prime } = f _ { x } + f _ { y } f ,
$$

where the two terms together correspond to the elementary differential associated with $t = \mathbb { I }$ Similarly, for the third derivative we have

$$
y ^ { \prime \prime \prime } = { \left( { { f _ { x x } } + 2 { f _ { x y } } f + { f _ { y y } } { f ^ { 2 } } } \right) + \left( { { f _ { y } } ( { f _ { x } } + { f _ { y } } { f } ) } \right) } ,
$$

where the grouped terms correspond to $t = \mathsf { Y }$ and $t = { \mathfrak { f } }$ respectively.

The expressions that arise here, and for the fourth derivative, are more complicated, because of the presence of derivatives with respect to $x$ . However, the terms can be grouped together according to the elementary differentials to which they correspond. Furthermore, the order conditions are identical to those found in the general vector case. When similar expressions are worked out for the 17 elementary differentials of order 5, we find a confusion between the results for two particular trees. In fact for each of $t _ { 1 } = { \sqrt [ { \object Object] { \operatorname { \rho } } } } \mathrm { a n d } t _ { 2 } = { \sqrt [ { \math { \rho } } } , F$ $F ( t )$ reduces to

$$
F ( t ) = f _ { y } ( f _ { y y } f + f _ { x y } ) ( f _ { y } f + f _ { x } ) ,
$$

and instead of two order conditions

$$
\Phi ( t _ { 1 } ) = \sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } = { \frac { 1 } { \gamma ( t _ { 1 } ) } } = { \frac { 1 } { 3 0 } }
$$

and

$$
\Phi ( t _ { 2 } ) = \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac 1 { \gamma ( t _ { 2 } ) } = \frac 1 { 4 0 } ,
$$

we have the single condition

$$
\sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } + \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac { 7 } { 1 2 0 } .
$$

We discuss in Subsection 325 the construction of fifth order methods. These usually satisfy the so-called $D ( 1 )$ condition, which we introduce in Subsection 321. This simplifying assumption has, as one of its consequences, the dependence of (316b) on other conditions, for which there is no confusion. Hence, for methods satisfying $D ( 1 )$ , scalar and vector order 5 conditions are equivalent.

For orders 6 and higher, the confusion between the order conditions for the scalar case becomes more pronounced. The first published methods of this order(Huˇta, 1956, 1957) were derived for scalar problems but, nevertheless, have order 6 for the general vector case (Butcher, 1963a).

# 317 Independence of elementary weights

We show in Subsection 324 that, given a positive integer $p$ , there exists an integer $s$ such that there is a Runge–Kutta method with $s$ stages with order $p$ . We now present a more general result on the independence of the elementary weights but without a specific value of $s$ given.

Theorem 317A Given a finite subset $T _ { 0 }$ , of $T$ and a mapping $\phi : T _ { 0 }  \mathbb { R }$ , there exists a Runge–Kutta method such that the elementary weights satisfy

$$
\Phi ( t ) = \phi ( t ) , \qquad f o r \ a l l \ t \in T _ { 0 } .
$$

Proof. Let $\# T _ { 0 } = n$ . The set of possible values that can be taken by the vector of $\Phi ( t )$ values, for all $t \in T _ { 0 }$ , is a vector space. To see why this is the case, consider Runge–Kutta methods given by the tableaux

$$
{ \frac { c \left| \ A \right. } { \left| \ b ^ { \mathsf { T } } \right. } } \qquad { \mathrm { a n d } } \qquad { \frac { \overline { { c } } } { \overline { { b } } ^ { \mathsf { T } } } } \qquad { \frac { \overline { { A } } } { \overline { { b } } ^ { \mathsf { T } } } }
$$

with $s$ and $\overline { { s } }$ stages, respectively. If the elementary weight functions for these two Runge–Kutta methods are $\Phi$ and $\overline { { \Phi } }$ , then the method given by the tableau

$$
\frac { c } { c } \left| \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { \overline { { { A } } } } } \\ { { \theta b ^ { \intercal } } } & { { \overline { { { \theta } } } \overline { { { b } } } ^ { \intercal } } } \end{array} \right.
$$

has elementary weight function $\theta \Phi + { \overline { { \theta \Phi } } }$ . Let $V \subset \mathbb { R } ^ { n }$ denote this vector space. We complete the proof by showing that $V = \mathbb { R } ^ { n } .$ If this were not the case, there would exist a non-zero function $\psi : T _ { 0 } \to \mathbb { R }$ such that $\begin{array} { r } { \sum _ { t \in T _ { 0 } } \psi ( t ) \Phi ( t ) = 0 } \end{array}$ , for all Runge–Kutta methods. Because every coefficient in a Runge–Kutta tableau can be multiplied by an arbitrary scalar $\theta$ to give a new method for which $\Phi ( t )$ is replaced by $\theta ^ { r ( t ) } \Phi ( t )$ , we may assume that every non-zero value of $\psi$ corresponds to trees with the same order $k$ . This is impossible for $k = 1$ , because in this case there is only a single tree $\tau$ . Suppose the impossibility of this has been proved for all orders less than $k$ , but that there exist trees Kutta methods with $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { m }$ , each of order $\psi ( t _ { i } ) \neq 0$ $k$ , such that , for $i = 1 , 2 , \dots , m$ $\textstyle \sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \Phi ( t _ { i } ) = 0$ . Write $t _ { i } = [ t _ { i 1 } ^ { l _ { i 1 } } t _ { i 2 } ^ { l _ { i 2 } } \cdot \cdot \cdot ]$ , for all Runge– , for $i = 1 , 2 , \dots , m$ . Let $\hat { t }$ denote a tree appearing amongst the $t _ { i j }$ which does not occur with the same exponent in each of the $t _ { i }$ . Construct an $s$ -stage Runge–Kutta method

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

for which each of $\Phi ( t _ { i j } ) = 1$ , except for $\Phi ( \hat { t } ) = \theta$ . Define second Runge–Kutta tableau with $s + 1$ stages of the form

$$
{ \frac { c \ \boxed { A } \ 0 } { 1 \ \boxed { b ^ { \intercal } } \ 0 } } \ .
$$

If $q _ { i }$ is the exponent of $\hat { t }$ in $t _ { i }$ , then it follows that

$$
\sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \theta ^ { q _ { i } } = 0 .
$$

Since $\theta$ can take any value and since $q _ { i }$ is not constant, it is not possible that $\psi$ is never zero. 

# 318 Local truncation error

The conditions for order give guarantees that the Taylor expansions of the exact and computed solutions agree up to terms in $h ^ { p }$ . Obtaining an understanding of the respective terms in $h ^ { p + 1 }$ is regarded as a key to deriving methods that not only have a specific order, but also have a small truncation error. Because the number of terms of this order rises rapidly as $p$ increases, it is extremely difficult to know how this sort of optimality should be arrived at. Picking out just the terms of order $p + 1$ , we can write the local truncation error in a single step as

$$
h ^ { p + 1 } \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left( \frac { 1 } { \gamma ( t ) } - \Phi ( t ) \right) F ( t ) ( y _ { 0 } ) + O ( h ^ { p + 2 } ) .
$$

Since we are interested in asymptotic behaviour, that is, limiting behaviour for $h$ small, we do not devote much attention to the term $O ( h ^ { p + 2 } )$ . The coefficient of $h ^ { p + 1 }$ in (318a) is bounded in magnitude by

$$
\sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| ,
$$

and this should somehow be made small. There is simply no general rule interrelating the magnitudes of the various elementary differentials, and some assumptions need to be made.

expression fo The first approach that can be considered is to compare, term by term, the r 1(p+1)! y(p+1)(x0), which is proportional to the local truncation error coefficient for linear multistep methods or for implicit Runge–Kutta methods of collocation type. The coefficient in this expression, corresponding to $t$ , is

$$
{ \frac { 1 } { \sigma ( t ) \gamma ( t ) } } ,
$$

so that the corresponding multiplier to yield the corresponding term in (318b) is

$$
| \gamma ( t ) \Phi ( t ) - 1 | .
$$

Hence, we can bound (318b) by

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 | \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) \gamma ( t ) } \cdot \| F ( t ) ( y _ { 0 } ) \|
$$

and hence, it might be desirable to minimize

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 |
$$

in seeking an efficient method.

Another approach would be to assume a bound $M$ on $\| f \|$ , a bound $L$ on the linear operator $\| f ^ { \prime } \|$ , and further bounds to make up the sequence

$$
\begin{array} { r l } & { \| f \| \leq M , } \\ & { \| f ^ { \prime \prime } \| \leq L , } \\ & { \| f ^ { \prime \prime } \| \leq \frac { L ^ { 2 } } { M } , } \\ & { \| f ^ { \prime \prime \prime } \| \leq \frac { L ^ { 3 } } { M ^ { 2 } } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad  \end{array}
$$

This will mean that for any tree of order $p + 1$ , $\| F ( t ) ( y _ { 0 } ) \| \le L ^ { p } M$ and that

$$
\sum _ { \substack { \cdot ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| \leq \sum _ { \substack { r ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot L ^ { p } M .
$$

In studying the behaviour of a particular method of order $p$ when used to solve a particular initial value problem, we wish to assume that the local truncation error is bounded asymptotically by some constant multiplied by $h ^ { p + 1 }$ . This assumption will hinge on smoothness of the solution and the differentiability, sufficiently many times, of $f$ .

# 319 Global truncation error

We consider the cumulative effect of errors in many steps leading to an error in a final output point. Suppose that $n$ steps are performed to carry the solution from an initial point $x _ { 0 }$ to a final point $\scriptstyle { \overline { { x } } }$ . If a constant stepsize is used, this would need to be equal to $( { \overline { { x } } } - x _ { 0 } ) / n$ to exactly reach the final point. Denote the approximations computed by a Runge–Kutta method by $y _ { 1 }$ , $y _ { 2 }$ , $\cdot \cdot \cdot$ , $y _ { n }$ , with $y _ { 0 } = y ( x _ { 0 } )$ . If the error committed in each of the $n$ steps is bounded by $C h ^ { p + 1 }$ then the total contribution to the error would seem to be

$$
n C h ^ { p + 1 } = C ( \overline { { x } } - x _ { 0 } ) h ^ { p } .
$$

We attempt to make this argument more precise by noting that an error in the initial value input to a step will lead to an error in the output value consisting of two terms. The first of these is the perturbation to the output due to the error in the input, and the second is the truncation error due to the method itself.

In the statement of a preliminary lemma that we need, $| A |$ and $\left| b ^ { \dagger } \right|$ will denote the matrix $A$ and the vector $b ^ { \intercal }$ , respectively, with every term replaced by its magnitude.

![](images/7069dad99fe8cba6df92d3df7742e7e316a06d11c2a6f005b98913010ef5fb82.jpg)  
Growth of global errors from local errors referred to the computed solution

Lemma 319A Let $f$ denote a function $\mathbb { R } ^ { m } \to \mathbb { R } ^ { m }$ , assumed to satisfy a Lipschitz condition with constant $L$ . Let $y _ { 0 } \in \mathbb { R } ^ { m }$ and $z _ { 0 } \in \mathbb { R } ^ { m }$ be two input values to a step with the Runge–Kutta method $( A , b ^ { \intercal } , c )$ , using stepsize $h \leq h _ { 0 }$ , where $h _ { 0 } L \rho ( | A | ) < 1$ , and let $y _ { 1 }$ and $z _ { 1 }$ be the corresponding output values. Then

$$
\begin{array} { r } { \| y _ { 1 } - z _ { 1 } \| \leq ( 1 + h L ^ { \star } ) \| y _ { 0 } - z _ { 0 } \| , } \end{array}
$$

where

$$
L ^ { \star } = { L } | b ^ { \mathsf { T } } | ( I - h _ { 0 } L | A | ) ^ { - 1 } \mathbf { 1 } .
$$

Proof. Denote the stage values by $Y _ { i }$ and $Z _ { i }$ , $i = 1 , 2 , \dots , s$ , respectively. From the equation $\begin{array} { r } { Y _ { i } - Z _ { i } = ( y _ { 0 } - z _ { 0 } ) + h \sum _ { j = 1 } ^ { s } a _ { i j } ( f ( Y _ { j } ) - f ( Z _ { j } ) ) } \end{array}$ , we deduce that

$$
\| Y _ { i } - Z _ { i } \| \leq \| y _ { 0 } - z _ { 0 } \| + h _ { 0 } L \sum _ { j = 1 } ^ { s } | a _ { i j } | \| Y _ { j } - Z _ { j } \| ,
$$

so that, substituting into

$$
\| y _ { 1 } - z _ { 1 } \| \leq \| y _ { 0 } - z _ { 0 } \| + h L \sum _ { j = 1 } ^ { s } | b _ { j } | \| Y _ { j } - Z _ { j } \| ,
$$

we obtain the result.

![](images/26e12816636dcf5118b0aa79a0107d61337f85fe29f11b6c2cebf01bc1842577.jpg)  
Growth of global errors from local errors referred to the exact solution

To see how to use this result, consider Figures 319(i) and 319(ii). Each of these shows the development of global errors generated by local truncation errors in individual steps. In Figure 319(i), the local truncation errors are referred to the computed solution. That is, in this figure, $\delta _ { k }$ is the difference between the exact solution defined by an initial value at the start of step $k$ and the numerical solution computed in this step. Furthermore, $\Delta _ { k }$ is the contribution to the global error resulting from the error $\delta _ { k }$ in step $k$ . An alternative view of the growth of errors is seen from Figure 319(ii), where $\delta _ { k }$ is now the difference between the exact solution at $x _ { k }$ and the computed solution found by using an input value $y _ { k - 1 }$ at the start of this step exactly equal to $y ( x _ { k - 1 } )$ . As in the previous figure, $\Delta _ { k }$ is the contribution to the global error resulting from the local error $\delta _ { k }$ . To obtain a bound on the global truncation error we first need an estimate on $\delta _ { 1 }$ , $\delta _ { 2 } , \ldots , \delta _ { n }$ using these bounds. We then estimate by how much $\delta _ { k }$ can grow to $\Delta _ { k }$ , $k = 1 , 2 , \ldots , n$ . The global error is then bounded in norm by $\scriptstyle \sum _ { k = 1 } ^ { \pi } \Delta _ { k }$ . We have a bound already from (110c) on how much a perturbation in the exact solution can grow. If we were basing our global error bound on Figure $3 1 9 ( \mathrm { i } )$ then this would be exactly what we need. However, we use Figure 319(ii), and in this case we obtain the same growth factor but with $L$ replaced by $L ^ { \star }$ . The advantage of using an argument based on this figure, rather than on Figure 319(i), is that we can then use local truncation error defined in the standard way, by comparing the exact solution at step value $x _ { n }$ with the numerically computed result over a single step with initial value $y ( x _ { n - 1 } )$ .

Theorem 319B Let $h _ { 0 }$ and $L ^ { \star }$ be such that the local truncation error at step $k = 1 , 2 , \ldots , n$ is bounded by

$$
\delta _ { k } \leq C h ^ { p + 1 } , \qquad h \leq h _ { 0 } .
$$

Then the global truncation error is bounded by

$$
\| y ( x _ { n } ) - y _ { n } \| \leq \left\{ \begin{array} { l l } { \frac { \exp ( L ^ { \star } ( \overline { { x } } - x _ { 0 } ) ) - 1 } { L ^ { \star } } C h ^ { p } , } & { L ^ { \star } > 0 , } \\ { ( \overline { { x } } - x _ { 0 } ) C h ^ { p } , } & { L ^ { \star } = 0 . } \end{array} \right.
$$

Proof. Use Figure 319(ii) and obtain the estimate

$$
\| y ( x _ { n } ) - y _ { n } \| \leq C h ^ { p + 1 } \sum _ { k = 1 } ^ { n } ( 1 + h L ^ { \star } ) ^ { k } .
$$

The case $L ^ { \star } = 0$ is obvious. For the case $L ^ { \star } > 0$ , calculate the sum and use the bound

$$
( 1 + h L ^ { \star } ) ^ { n } \leq \exp ( L ^ { \star } h n ) = \exp ( L ^ { \star } ( \overline { { x } } - x _ { 0 } ) ) .
$$

# Exercises 31

31.1 Define $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ by

$$
f ( y ^ { 1 } , y ^ { 2 } , y ^ { 3 } ) = \left[ \begin{array} { c } { { y ^ { 1 } + y ^ { 2 } y ^ { 3 } } } \\ { { ( y ^ { 1 } ) ^ { 2 } + 2 y ^ { 1 } y ^ { 2 } } } \\ { { 1 + ( y ^ { 2 } + y ^ { 3 } ) ^ { 2 } } } \end{array} \right] .
$$

Find formulae for the elementary differentials $F ( t )$ , for $t = [ \tau ]$ , $\left[ \tau ^ { 2 } \right]$ and $[ \tau [ \tau ] ]$ .

31.2 For the Runge–Kutta method

$$
\frac { 1 } { 3 } \neq \frac { \frac { 5 } { 1 2 } } { 4 } \frac { \frac { 1 } { 4 } } { 4 }
$$

find the elementary weights for the eight trees up to order 4. What is the order of this method?

31.3 For an arbitrary Runge–Kutta method, find the order condition corresponding to the tree

# 32 Low Order Explicit Methods

# 320 Methods of orders less than 4

It will be shown in Subsection 324 that, for an explicit method to have order $p$ , at least $s = p$ stages are necessary. We derive methods up to $p = 3$ , with exactly $p$ stages, and then discuss briefly the advantages of using $s = p + 1$ .

For $s = p = 1$ there is no choice beyond the Euler method with tableau

![](images/9618c77e2502a58024623115b20e87f83cfa797f034b711167351b780177be93.jpg)

For $s = p = 2$ , we have a one-parameter family of methods of the form

$$
\frac { 0 } { \frac { c _ { 2 } } { 1 - \frac { 1 } { 2 c _ { 2 } } ~ \frac { 1 } { 2 c _ { 2 } } } }
$$

which satisfies the conditions $b _ { 1 } + b _ { 2 } = 1$ and $\begin{array} { r } { b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , corresponding to the trees and .

For $s = p = 3$ , we must satisfy four conditions, which are shown together with the corresponding trees as follows:

$$
\begin{array} { c c c } { \cdot } & { b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 , } \\ { \vdots } & { } & { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \displaystyle { \frac { 1 } { 2 } } , } \\ { \big \nvee } & { } & { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \displaystyle { \frac { 1 } { 3 } } , } \\ { \vdots } & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } = \displaystyle { \frac { 1 } { 6 } } . } \end{array}
$$

To solve these equations in the most straightforward manner, it is convenient to treat $c _ { 2 }$ and $c _ { 3 }$ as free parameters and to carry out three steps. First, solve for $b _ { 2 }$ and $b _ { 3 }$ from the linear system given by (320b) and (320c). Secondly, evaluate $b _ { 1 }$ from (320a). Finally, solve for $a _ { 3 2 }$ from (320d). This plan will run into difficulties if the matrix of coefficients in (320b) and (320c) is singular; that is, if $c _ { 2 } c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = 0$ . Assuming this does not occur, we have a further difficulty if the solution to (320b) and (320c) results in $b _ { 3 } = 0$ . This anomaly, which occurs if $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , makes it impossible to solve (320d). A more careful analysis is necessary to resolve these difficulties, and it is possible to identify three cases where a solution can be found. These are

$$
\begin{array} { l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \neq 0 \neq c _ { 3 } \neq c _ { 2 } \neq \frac { 2 } { 3 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { c _ { 2 } = c _ { 3 } = \frac { 2 } { 3 } , b _ { 3 } \neq 0 , } } \\ { { \mathrm { ~ I I I ~ } } } & { { c _ { 2 } = \frac { 2 } { 3 } , c _ { 3 } = 0 , b _ { 3 } \neq 0 . } } \end{array}
$$

The coefficient tableaux for the three cases are summarized as follows, with the general form of the tableau given in each case: for case I we have

for case II,

$$
{ \frac { \displaystyle { \frac { 2 } { 3 } } } { \displaystyle { \frac { 2 } { 3 } } - { \frac { 1 } { 4 b _ { 3 } } } } } { \frac { \frac { 2 } { 3 } } { \frac { 2 } { 4 } } } { \frac { \frac { 2 } { 3 } } { \frac { 1 } { 4 } - b _ { 3 } } } { \frac { \frac { 1 } { 6 } } { b _ { 3 } } }  ; 
$$

and for case III,

# 321 Simplifying assumptions

As the order being sought increases, the number of conditions rises rapidly and soon becomes unmanageable. For this reason, it is necessary to examine the relationships between the conditions corresponding to various trees. At the same time, we identify certain collections of order conditions which have some sort of central role. Since these special conditions will be of varying complexity, depending on the orders to which we apply them, they will be parameterized by one or more positive integers. For example, $E ( \eta , \zeta )$ is a set of assumptions about a method that hold for all positive integers $k \leq \eta$ and $l \leq \zeta$ .

that the cond The first of these conditions will be denoted by ions $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = k ^ { - 1 }$ old for $k = 1 , 2 , \ldots , \eta$ $B ( \eta )$ , and simply states . For a method $p$ $B ( p )$   
restates the order condition for the trees

Order conditions corresponding to some pairs of related trees   

<table><tr><td>t1</td><td>1 Φ(t1)= (t1）</td><td>t2</td><td>（t2）=27（t2)</td><td>1</td></tr><tr><td>：</td><td></td><td>?</td><td></td><td></td></tr><tr><td></td><td>∑baijC=</td><td></td><td>∑bic²=</td><td></td></tr><tr><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1∑bic=</td><td></td></tr><tr><td></td><td>∑biciaijCj=</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑bxakiaijCj =24</td><td></td><td>1∑bkakic²=4</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>丫</td><td></td><td></td></tr><tr><td>:iv:iI!</td><td></td><td></td><td></td><td></td></tr></table>

To motivate condition $C ( \eta )$ , consider pairs of trees $t _ { 1 }$ and $t _ { 2 }$ , with the same order, that differ in only one small respect. Suppose they are labelled with identical vertex sets and that the edge sets, say $E _ { 1 }$ and $E _ { 2 }$ , respectively, differ only in that $E _ { 1 }$ contains the edges $[ i , j ]$ and $[ j , k ]$ , and that $j$ and $k$ do not occur in any of the other ordered pairs in $E _ { 1 }$ , whereas $E _ { 2 }$ contains the edge $[ i , k ]$ instead of $[ j , k ]$ . This will mean that the elementary weight corresponding to $t _ { 1 }$ will have a factor $a _ { i j } c _ { j }$ , whereas $t _ { 2 }$ will have a corresponding factor $c _ { i } ^ { 2 }$ . Furthermore, the densities are also closely related in that $\gamma ( t _ { 1 } ) ~ = ~ 2 \gamma ( t _ { 2 } )$ . Hence, the equations

$$
\Phi ( t _ { 1 } ) = { \frac { 1 } { \gamma ( t _ { 1 } ) } } \qquad { \mathrm { a n d } } \qquad \Phi ( t _ { 2 } ) = { \frac { 1 } { \gamma ( t _ { 2 } ) } }
$$

will be equivalent if

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } = { \frac { 1 } { 2 } } c _ { i } ^ { 2 } , { \mathrm { ~ f o r ~ a l l ~ } } i = 1 , 2 , \ldots , s .
$$

We illustrate this by looking at some pairs of trees and noting the form of the equations

$$
\Phi ( t _ { 1 } ) = { \frac { 1 } { \gamma ( t _ { 1 } ) } } \mathrm { a n d } \frac { 1 } { 2 } \Phi ( t _ { 2 } ) = { \frac { 1 } { 2 \gamma ( t _ { 2 } ) } } .
$$

These are displayed in Table 321(I).

It is clear that, if it were possible for (321a) to hold for all $i \in \{ 1 , 2 , \ldots , s \}$ , then we could simply remove the order equations associated with the $t _ { 1 }$ trees from consideration, because they will automatically be satisfied if the conditions $\Phi ( t ) = 1 / \gamma ( t )$ are satisfied for the $t _ { 2 }$ trees. However, it is not possible in the case $i \ = \ 2$ because this gives the equation $\textstyle { \frac { 1 } { 2 } } c _ { 2 } ^ { 2 } \ = \ 0$ which implies $c _ { 2 } = 0$ . It will then follow in turn that $c _ { 3 } = 0$ , $c _ { 4 } = 0$ , . . . and all $c$ components equal to zero will not be consistent even with the order condition $\textstyle \sum b _ { i } c _ { i } \ = \ { \frac { 1 } { 2 } }$ . While we cannot make use of the simplification of assuming (321a) in the case of explicit methods, we make extensive use of this and closely related conditions in the case of implicit methods. Furthermore, we can still use this sort of simplification applied to just some of the stages.

![](images/fb84986ce75b33490495146aad335c44a6458ed7536f47415bf8920a02f3dc08.jpg)  
The $C ( k )$ condition relating $\textstyle \sum _ { j } a _ { i j } c _ { j } ^ { k - 1 }$ (left-hand tree) to $c _ { i } ^ { k }$ (right-hand tree). The underlying tree is a pohutukawa (Metrosideros excelsa), also known as the ‘New Zealand Christmas tree’ because its bright red flowers bloom at Christmas-time.

In addition to (321a), we can consider the possibility that conditions like

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \quad i = 1 , 2 , \ldots , s ,
$$

hold for $k = 1 , 2 , \ldots .$ Assuming that these hold for $1 \leq k \leq \xi$ , we denote this collection of conditions by $C ( \xi )$ . The consequences of $C ( \xi )$ are that, for any pair of trees $t _ { 1 }$ and $t _ { 2 }$ for which $\Phi ( t _ { 1 } )$ contains a factor $a _ { i j } c _ { j } ^ { k - 1 }$ , $\Phi ( t _ { 2 } )$ contains a factor $\scriptstyle { \frac { 1 } { k } } c _ { i } ^ { k }$ and the remaining factors are identical in the two expressions, then $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ implies $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ . We illustrate this in Figure 321(i).

The $D ( k )$ conditions interrelate three trees $t _ { 1 }$ , $t _ { 2 }$ and $t _ { 3 }$ for which the corresponding elementary weights differ only in that $\Phi ( t _ { 1 } )$ has a factor $b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ , $\Phi ( t _ { 2 } )$ has a factor $b _ { j }$ and $\Phi ( t _ { 3 } )$ has a factor $b _ { j } c _ { j } ^ { k }$ . This means that these trees have forms like those shown in Figure 321(ii).

We illustrate this further, for the case $k = 1$ , in Table 321(II). Note that if $D ( 1 )$ holds, then the truth of $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ follows from $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ and $\Phi ( t _ { 3 } ) = 1 / \gamma ( t _ { 3 } )$ . For explicit methods, $D ( 2 )$ cannot hold, for similar reasons to the impossibility of $C ( 2 )$ . For implicit methods $D ( s )$ is possible, as we shall see in Section 342.

![](images/ff9c9de1b79338b1593c984ed36a7e9e8e2f72cce9e35ce52ef10fe65ea4fc75.jpg)  
Figure 321(ii) The $D ( k )$ condition relating $\sum _ { i } b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ (left-hand tree) to $b _ { j }$ (middle tree) and $b _ { j } c _ { j } ^ { k }$ (right-hand tree). The underlying tree is a kauri (Agathis australis). Although the immature tree shown is only a few metres tall, the most famous kauri tree, Tane Mahuta (Lord of the Forest), has a height of $4 0 \textrm { m }$ and a diameter, 1.5 m above ground level, of 5.21 m.

Sets of three related trees illustrating $D ( 1 )$   

<table><tr><td rowspan="3">t1</td><td rowspan="3">(t1)=</td><td>1</td><td rowspan="3">t2</td><td rowspan="3">Φ(t2) =</td><td>1</td><td rowspan="3">t3</td><td rowspan="3">（(t3)=</td><td>1</td></tr><tr><td>(t1)</td><td>(t2）</td><td>（t3)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijcj=</td><td></td><td></td><td>∑bcj=</td><td></td><td>Y</td><td>∑bj²=</td><td></td></tr><tr><td></td><td></td><td></td><td>：</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>？</td><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td>∑biaijc²=12</td><td></td><td></td><td>∑b=</td><td></td><td></td><td>∑bjc=1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijajkck =</td><td></td><td></td><td></td><td></td><td>∑bjCjajkCk=</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>∑bjajkck=</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Finally, the condition $E ( \eta , \zeta )$ states that

$$
\sum b _ { i } c _ { i } ^ { k - 1 } a _ { i j } c _ { j } ^ { l - 1 } = \frac { 1 } { l ( k + l ) } , \qquad k = 1 , 2 , \ldots , \eta , \quad l = 1 , 2 , \ldots , \zeta .
$$

This simply expresses the fact that the order condition $\Phi ( t ) = 1 / \gamma ( t )$ is satisfied for trees $t = [ \tau ^ { k - 1 } [ \tau ^ { l - 1 } ] ]$ for $k \leq \eta$ and $l \leq \zeta$ . This is a necessary condition for orders at least $\eta + \zeta$ .

# 322 Methods of order 4

It is an interesting consequence of the fourth order conditions for a method with $s \ = \ 4$ stages, that $c _ { 4 } ~ = ~ 1$ and that $D ( 1 )$ holds. This fact reduces significantly the number of conditions that remain to be solved; furthermore, it is possible to segment the derivation into two phases: the solution of the remaining order conditions and the evaluation of the elements in the final row of $A$ to ensure that $D ( 1 )$ is actually satisfied. Assuming that the method

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { c _ { 4 } } \\ { b _ { 1 } } \end{array} \right| a _ { 2 1 } \qquad \eqno { 3 } 2 } \end{array}
$$

satisfies the fourth order conditions, then we can compute the values of

$$
\begin{array} { r l } & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 2 } ) c _ { i } = \frac { 1 } { 4 } - \frac { c _ { 2 } + c _ { 4 } } { 3 } + \frac { c _ { 2 } c _ { 4 } } { 2 } , } \\ & { b _ { 4 } a _ { 4 3 } ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } a _ { i j } ( c _ { j } - c _ { 2 } ) c _ { j } \qquad = \frac { 1 } { 1 2 } - \frac { c _ { 2 } } { 6 } , } \\ & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) a _ { i j } c _ { j } \qquad = \frac { 1 } { 8 } - \frac { c _ { 4 } } { 6 } , } \\ & { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } a _ { i j } a _ { j k } c _ { k } \qquad = \frac { 1 } { 2 4 } . } \end{array}
$$

In each of these calculations, the first column is the only non-zero term in the middle column, while the final column is found by expanding the middle column into a linear combination of elementary weights and equating each of these to the right-hand sides of the corresponding order conditions. For example, (322a) is evaluated from the trees $\blacktriangledown$ , $\blacktriangledown$ and $\natural$ and uses the combination of order conditions

$$
\Phi ( { \pmb { \Psi } } ) - ( c _ { 2 } + c _ { 4 } ) \Phi ( { \pmb { \Psi } } ) + c _ { 2 } c _ { 4 } \Phi ( { \pmb { \updownarrow } } ) = \frac { 1 } { \gamma ( { \pmb { \Psi } } ) } - \frac { c _ { 2 } + c _ { 4 } } { \gamma ( { \pmb { \ Y } } ) } + \frac { c _ { 2 } c _ { 4 } } { \gamma ( { \pmb { \updownarrow } } ) } .
$$

From the first columns of (322a)–(322d), we observe that $\mathrm { { ( 3 2 2 a ) } } \times \mathrm { { ( 3 2 2 d ) } } =$ (322b) $\times$ (322c) so that, from the last columns, we find

$$
\left( { \frac { 1 } { 4 } } - { \frac { c _ { 2 } + c _ { 4 } } { 3 } } + { \frac { c _ { 2 } c _ { 4 } } { 2 } } \right) \left( { \frac { 1 } { 2 4 } } \right) - \left( { \frac { 1 } { 1 2 } } - { \frac { c _ { 2 } } { 6 } } \right) \left( { \frac { 1 } { 8 } } - { \frac { c _ { 4 } } { 6 } } \right) = 0 .
$$

This relation simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$ which, because $c _ { 2 } = 0$ is incompatible with (322d), implies $c _ { 4 } = 1$ .

An alternative proof of this result, is found by using the following:

Lemma 322A If $P$ and $Q$ are each $3 \times 3$ matrices such that their product has the form

$$
P Q = \left[ \begin{array} { c c c } { r _ { 1 1 } } & { r _ { 1 2 } } & { 0 } \\ { r _ { 2 1 } } & { r _ { 2 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

where

$$
\operatorname* { d e t } \left( { \left[ \begin{array} { l l } { r _ { 1 1 } } & { r _ { 1 2 } } \\ { r _ { 2 1 } } & { r _ { 2 2 } } \end{array} \right] } \right) \neq 0 ,
$$

then either the last row of $P$ is zero or the last column of $Q$ is zero.

Proof. Because $P Q$ is singular, either $P$ is singular or $Q$ is singular. In the first case, let $u ^ { \prime } \ne 0$ be such that $u ^ { \prime } P = 0$ , and therefore $u ^ { \intercal } P Q = 0$ ; in the second case, let $v \neq 0$ be such that $Q v = 0$ , and therefore $P Q v = 0$ . Because of the form of $P Q$ , this implies that the first two components of $u ^ { \intercal }$ (or, respectively, the first two components of $v$ ) are zero. $\boxed { \begin{array} { r l } \end{array} }$

To obtain the result that $D ( 1 )$ necessarily holds if $s = p = 4$ , we apply Lemma 322A with

$$
\begin{array}{c} \mathbf { \Phi } ^ { \mathcal { P } } = \left[ \begin{array} { c c c } { b _ { 2 } } & { b _ { 3 } } & { b _ { 4 } } \\ { b _ { 2 } c _ { 2 } } & { b _ { 3 } c _ { 3 } } & { b _ { 4 } c _ { 4 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { i = 1 } & { i } & { i = 1 } \end{array} \right] \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 3 } - b _ { 3 } ( 1 - c _ { 3 } ) \quad \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } )  \end{array}
$$

and

$$
\begin{array} { r } { Q = \left[ \begin{array} { c c c c c } { c _ { 2 } } & { c _ { 2 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } } \\ { c _ { 3 } } & { c _ { 3 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 3 j } c _ { j } - \frac { 1 } { 2 } c _ { 3 } ^ { 2 } } \\ { c _ { 4 } } & { c _ { 4 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 4 j } c _ { j } - \frac { 1 } { 2 } c _ { 4 } ^ { 2 } } \end{array} \right] . } \end{array}
$$

The value of the matrix $P Q$ can be calculated from the order conditions. For example, the $( 2 , 2 )$ element is equal to

$$
\left[ b _ { 2 } c _ { 2 } b _ { 3 } c _ { 3 } b _ { 4 } c _ { 4 } \right] \left[ c _ { 2 } ^ { 2 } c _ { 3 } ^ { 2 } c _ { 4 } ^ { 2 } \right] ^ { \intercal } = \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 3 } = { \frac { 1 } { 4 } } .
$$

The elements in the last row and last column are a little more complicated to evaluate because they depend on linear combinations of elementary weights, but the relation of these elements in the product to the $C ( 2 )$ and $D ( 1 )$ conditions simplifies each of these elements to a zero value. In summary, the product of $P$ and $Q$ is

$$
P Q = \left[ \begin{array} { l l l } { \frac 1 2 } & { \frac 1 3 } & { 0 } \\ { \frac 1 3 } & { \frac 1 4 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

so that the conditions of Lemma 322A are satisfied. The conclusion is that the last roeither $P$ of  or $Q$ r, this means that. These simplify to $\begin{array} { r } { \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } ) = 0 } \end{array}$ $\begin{array} { r } { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ $b _ { 4 } ( 1 - c _ { 4 } ) = 0$ or to $\begin{array} { r } { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ , respectively. It is impossible that $c _ { 2 } = 0$ or that $b _ { 4 } = 1$ , and hence $c _ { 4 } = 1$ and the $D ( 1 )$ condition holds.

Since $D ( 1 )$ holds, the set of additional equations we need to satisfy reduce to those associated with the trees , , $\curlyvee$ and $\blacktriangledown$ as well as with the $\operatorname { t r e e } \sqrt { \frac { \pi } { 2 } }$ . The order condition associated with the last of these is $\begin{array} { r } { \sum b _ { i } c _ { i } a _ { i j } c _ { j } = \frac { 1 } { 8 } } \end{array}$ . It turns out to be more convenient to use, instead of this condition, the difference between this and with the condition associated with $\nmid$ , that is, $\begin{array} { r } { \sum b _ { i } a _ { i j } c _ { j } = \frac { 1 } { 6 } } \end{array}$ , which is a consequence of other assumptions and of the $D ( 1 )$ condition. Hence we assume $\begin{array} { r } { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } = \frac { 1 } { 2 4 } } \end{array}$ .

The steps we need to carry out to derive one of these methods are as follows:

(a) Choose $c _ { 2 }$ and $c _ { 3 }$ , noting that $c _ { 1 } = 0$ and $c _ { 4 } = 1$ . (b) Choose $b _ { 1 }$ , $b _ { 2 }$ , $b _ { 3 }$ , $b _ { 4 }$ to satisfy $\sum b _ { i } c _ { i } ^ { k - 1 } = 1 / k$ for $k = 1 , 2 , 3 , 4$ . (c) Choose $a _ { 3 2 }$ so that $\begin{array} { r } { b _ { 3 } ( 1 - c _ { 3 } ) a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } } \end{array}$ . (d) Choose $a _ { 4 1 }$ , $a _ { 4 2 }$ , $a _ { 4 3 }$ , so that $\begin{array} { r } { \sum _ { i } b _ { i } a _ { i j } = b _ { j } \bigl ( 1 - c _ { j } \bigr ) } \end{array}$ for $j = 1 , 2 , 3$

Carrying out this programme might present some difficulties. For example, if in step (a) the $c _ { i }$ are not distinct, then there might not exist a solution in step (b). It might also happen that the value of $b _ { 4 }$ , found in step (b), is zero, and this will make it impossible to carry out either step (c) or step (d). Even if a solution exists for the sub-problem that arises in each step, the solution might not be unique, and there could turn out to be a family of solutions. The general solution, which is valid except in these exceptional cases, is given by the following coefficients:

$$
\begin{array} { r l } & { a _ { 2 1 } = c _ { 2 1 } , } \\ & { a _ { 3 1 } = \frac { c _ { 3 } \left( c _ { 3 } + 4 c _ { 2 } ^ { 2 } - 3 c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 3 2 } = - \frac { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 4 1 } = \frac { - 1 2 c _ { 3 } c _ { 2 } ^ { 2 } + 1 2 c _ { 3 } ^ { 2 } c _ { 2 } ^ { 2 } + 4 c _ { 2 } ^ { 2 } - 6 c _ { 2 } + 1 5 c _ { 2 } c _ { 3 } - 1 2 c _ { 3 } ^ { 2 } c _ { 2 } + 2 + 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } } { 2 c _ { 2 } c _ { 3 } \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 2 } = \frac { \left( c _ { 2 } - 1 \right) \left( 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } + 2 - c _ { 2 } \right) } { 2 c _ { 2 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 3 } = - \frac { \left( 2 c _ { 2 } - 1 \right) \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - 1 \right) \left( c _ { 3 } - 1 \right) } { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \end{array}
$$

$$
\begin{array} { l } { b _ { 1 } = \cfrac { 6 c _ { 3 } c _ { 2 } - 2 c _ { 3 } - 2 c _ { 2 } + 1 } { 1 2 c _ { 3 } c _ { 2 } } , } \\ { b _ { 2 } = - \cfrac { \left( 2 c _ { 3 } - 1 \right) } { 1 2 c _ { 2 } \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - c _ { 2 } \right) } , } \\ { b _ { 3 } = \cfrac { \left( 2 c _ { 2 } - 1 \right) } { 1 2 c _ { 3 } \left( c _ { 2 } - c _ { 3 } c _ { 2 } + c _ { 3 } ^ { 2 } - c _ { 3 } \right) } , } \\ { b _ { 4 } = \cfrac { - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } } { 1 2 \left( c _ { 3 } - 1 \right) \left( c _ { 2 } - 1 \right) } . } \end{array}
$$

Kutta identified five special cases where a solution is certain to exist:

$$
\begin{array} { l l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \notin \{ 0 , \frac { 1 } { 2 } , \frac { 1 } { 2 } \pm \frac { \sqrt { 3 } } { 6 } , 1 \} , } } & { { c _ { 3 } = 1 - c _ { 2 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { b _ { 2 } = 0 , } } & { { c _ { 2 } \neq 0 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ I I I ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = \frac { 1 } { 2 } , \quad c _ { 3 } = 0 , } } \\ { { \mathrm { ~ I V ~ } } } & { { b _ { 4 } \neq 0 , } } & { { c _ { 2 } = 1 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ V ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = c _ { 3 } = \frac { 1 } { 2 } . } } \end{array}
$$

The coefficient tableaux are for case I,

<table><tr><td>0</td><td colspan="3"></td></tr><tr><td>1-C3</td><td colspan="3">1-C3</td></tr><tr><td>C3</td><td>C3(1-2c3)</td><td>C3 2(1-c3）</td><td></td></tr><tr><td rowspan="2">1</td><td colspan="3">2(1-c3）</td></tr><tr><td>12c-24c+17c3-4</td><td>C3(1-2c3)</td><td>1-C3</td></tr><tr><td colspan="3"></td><td></td></tr><tr><td rowspan="2"></td><td>2(1-c3)(6c3-1-6c) 6c3-1-6c</td><td>2(1-c3）(6c3-1-6c2）</td><td>6cg-1-6c2</td></tr><tr><td>1 12c3(1-c3) 12c3(1-c3)</td><td>1 12c3(1-c3)</td><td>6cg-1-6c 12c3(1-c3)</td></tr></table>

for case II,

$$
{ \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { { \frac { 1 } { 2 } } } \\ { 1 } \\ { { \frac { 1 } { 2 c _ { 2 } } } - 1 \quad - { \frac { 1 } { 2 c _ { 2 } } } \quad { \mathrm { ~ 2 ~ } } } \\ { { \frac { 1 } { 6 } } } \end{array} } ;
$$

for case III,

for case IV,

$$
\begin{array} { r }   \begin{array} { c } { 0 } \\ { 1 } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} | _ { \begin{array} { c c c c c c } { \frac { 3 } { 8 } } & { \frac { 1 } { 8 } } & { } & { } & { } \\ { 1 - \frac { 1 } { 4 b _ { 4 } } } & { - \frac { 1 } { 1 2 b _ { 4 } } } & { \frac { 1 } { 3 b _ { 4 } } } & { } & { } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 6 } - b _ { 4 } } & { \frac { 2 } { 3 } } & { b _ { 4 } } \end{array} \} } \end{array}
$$

and for case V,

$$
\begin{array} { r l } & { \left. \begin{array} { c } { 0 } \\ { \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} \right| \frac { 1 } { 2 } - \frac { 1 } { 6 b _ { 3 } } \qquad \frac { 1 } { 6 b _ { 3 } } } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad 1 - 3 b _ { 3 } \quad 3 b _ { 3 } \quad \right. } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad \frac { 2 } { 3 } - b _ { 3 } \quad b _ { 3 } \quad \frac { 1 } { 6 } \qquad \right. } \end{array} .
$$

Some interesting special choices within these cases are $\begin{array} { r } { c _ { 3 } = \frac { 2 } { 3 } } \end{array}$

and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ in case II,

$$
\begin{array} { r } { { \frac { 1 } { 4 } } { \left| \begin{array} { l l l l } { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { { \frac { 1 } { 2 } } } \end{array} \right| } ~ 0 \quad { { \frac { 1 } { 2 } } } } \\ { { \frac { 1 } { 6 } } { \frac { 1 } { 6 } } { \frac { - 2 } { 0 } } { \frac { 2 } { 3 } } { \begin{array} { l } { { \frac { 1 } { 6 } } } \end{array} } . } \end{array}
$$

A further, and somewhat eccentric, special choice in case II, is $c _ { 2 } = - \frac { 1 } { 2 }$

<table><tr><td>0 中</td><td></td></tr><tr><td></td><td>1 1</td><td>2</td><td></td></tr><tr><td></td><td>#</td><td>2</td><td></td></tr><tr><td></td><td>1</td><td></td><td>1</td></tr></table>

The interest in this method, as for a similar method with $c _ { 2 } = - 1$ , is that it is possible to eliminate one stage of computation, by replacing $F _ { 2 }$ by a quantity found in the previous step. The method contrived in this way is no longer a Runge–Kutta method, and has poorer stability, but it is more efficient in terms of order achieved per stages computed.

We also present the choices $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 1 2 } } \end{array}$ in case III,

$$
\begin{array} { r } { { \left. \begin{array} { c } { { 0 } } \\ { { \frac { 1 } { 2 } } } \\ { { 0 } } \\ { { 1 } } \end{array} \right| } \quad \frac { 1 } { 2 } \quad { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { 1 } } \end{array} \right. } } \\ { { \left. \begin{array} { l l l l l l } { { \frac { 1 } { 1 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 1 2 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 1 2 } } } & { { \frac { 1 } { 6 } } } \end{array} \right. } } \end{array} \right. , } } \end{array}
$$

and $\begin{array} { r } { b _ { 4 } = \frac { 1 } { 6 } } \end{array}$ in case IV,

Amongst the methods in case V, the ‘classical Runge–Kutta method’ is especially notable. The tableau is

$$
\begin{array} { r } { \frac { 0 } { 2 } \left| \begin{array} { l l l l l } { ~ } & { ~ } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ 0 } & { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 0 } } & { 0 } & { 1 } & { ~ } & { ~ } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 6 } } & { . ~ } \end{array} \right. } \end{array}
$$

Also in case V is a special method derived by Gill (1951), for the special purpose of reducing memory requirements for large problems. Gill found that by using a value $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 3 } + \frac { \sqrt { 2 } } { 6 } } \end{array}$ , or the conjugate of this which was rejected as having larger errors, it was possible to solve an $N$ -dimensional system using only $3 N$ stored numbers. For a general method with $s = p = 4$ , the corresponding memory needs are $4 N$ . The tableau for Gill’s method is

$$
{ \begin{array} { c } { { \mathrm { ~ 0 ~ } } } \\ { { \frac { 1 } { 2 } } } \\ { { \mathrm { ~ 1 ~ } } } \\ { { \mathrm { ~ 1 ~ } } } \end{array} } { \frac { 1 } { 2 } } { \left| \begin{array} { l l l l l } { { \underline { { { \mathrm { ~ 1 ~ } } } } } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { \mathrm { ~ 2 ~ } } { 2 } } } & { { \underline { { { 2 \mathrm { - } } } } } { \sqrt { \underline { { { 2 } } } } } } & { { } } & { { } } \\ { { 0 } } & { { - { \frac { { \sqrt { 2 } } } { 2 } } } } & { { { \underline { { { 2 \mathrm { + } { \sqrt { 2 } } } } } } } } & { { } } \\ { { { \frac { 1 } { 6 } } } } & { { { \frac { { 2 \mathrm { - } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { { 2 \mathrm { + } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { 1 } { 6 } } } } \end{array} \right. }
$$

and is characterized by the condition

$$
\operatorname * { d e t } \left( { \left[ \begin{array} { l l l } { 1 } & { a _ { 3 1 } } & { a _ { 3 2 } } \\ { 1 } & { a _ { 4 1 } } & { a _ { 4 2 } } \\ { 1 } & { b _ { 1 } } & { b _ { 2 } } \end{array} \right] } \right) = 0
$$

which, for a method in case V, imposes the constraint

$$
1 8 b _ { 3 } ^ { 2 } - 1 2 b _ { 3 } + 1 = 0 ,
$$

with solutions

$$
b _ { 3 } = { \frac { 2 \pm { \sqrt { 2 } } } { 6 } } .
$$

# 323 New methods from old

As we seek explicit Runge–Kutta methods of higher and higher order, we observe relationships between methods of two adjacent orders. For example, fourth order methods are connected in a special way with certain methods with only three stages, but with a modified type of third order condition. Denote the fourth order method by

$$
\begin{array} { r } { \frac { c } { \left| \begin{array} { l } { A } \\ { A } \\ { b ^ { \intercal } } \end{array} \right| } = \begin{array} { l } { c _ { 2 } } \\ { c _ { 3 } } \\ { 1 } \end{array} \left| \begin{array} { l l l l } { a _ { 2 1 } } & & & \\ { a _ { 3 1 } } & { a _ { 3 2 } } & & \\ { a _ { 4 1 } } & { a _ { 4 2 } } & { a _ { 4 3 } } & \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { b _ { 4 } } \end{array} \right| } \end{array}
$$

and consider the three-stage tableau

$$
\frac  \stackrel { \displaystyle \widetilde { c } } { \longrightarrow } \bigg | \stackrel { \widetilde { A } } { \widetilde { b } ^ { \top } } = \begin{array} { l } { 0 } \\ { c _ { 2 } } \\ { \frac { c _ { 3 } } { b _ { 1 } } \bigg | \stackrel { a _ { 2 1 } } { b _ { 2 } } \big ( 1 - c _ { 2 } \big ) \quad b _ { 3 } \big ( 1 - c _ { 3 } \big ) } \end{array} .
$$

If we denote the elementary weights for the new method (323b) by $\widetilde { \Phi }$ , we find for the trees with order up to 3,

$$
\begin{array} { l } { \displaystyle \widetilde { \Phi } ( \bullet ) = \frac 1 2 = \frac 1 { \left( r ( \bullet ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } ( \bullet ) = \frac 1 6 = \frac 1 { \left( r ( \bullet ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } ( \bullet \bullet ) = \frac 1 { 1 2 } = \frac 1 { \left( r ( \bullet \vee ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } \left( \ddag \right) = \frac 1 { 2 4 } = \frac 1 { \left( r \left( \bullet \right) + 1 \right) \gamma \left( \bullet \right) } . } \end{array}
$$

The conclusion that $\widetilde { \Phi } ( t ) = 1 / \big ( ( r ( t ) + 1 ) \gamma ( t ) \big )$ is not in the least remarkable. In fact, such a conclusion will always hold if $ { \tilde { b } } ^ { \intercal } = b ^ { \intercal } A$ , with obvious working in the opposi adjustments made to $c$ and   direction, from order 3 to order 4. If to form and $\widetilde { A }$ , but our interest here is in $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } = 1$ is satisfied for the four-stage method (323a), then the remainder of the order conditions are satisfied as a consequence of (323c)–(323f) and of the $D ( 1 )$ assumption. We check these as follows, where the relevant trees are also shown:

$$
\begin{array} { r l } & { \cdot \frac { \sum \hat { b } _ { i } } { 2 } b _ { i } = 1 , } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } = \frac { 3 } { \sqrt { 2 } } b _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) e _ { i } ^ { 4 } = \frac { 1 } { 2 } - \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } } \\ { 1 } & { \qquad \quad \le - \frac { 1 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 1 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) e _ { i } ^ { 2 } = \frac { 1 } { 5 } - \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 1 } { 4 } , } \\ { 1 } &  \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } e _ { i } ^ { 2 }  \end{array}
$$

It is not possible to extend the principle illustrated in this result to higher orders without making some additional assumptions. We introduce the idea we need as follows:

Definition 323A Consider a Runge–Kutta method given by the tableau

$$
\frac { c \dag A } { \ d b ^ { \intercal } } _ { \mathbf { \Pi } . }
$$

For a tree t and stage $i$ , let $\Phi _ { i } ( t )$ denote the elementary weight associated with t for the tableau

$$
\frac { c \left| \begin{array} { l } { \boldsymbol { A } } \\ { e _ { i } ^ { \top } \boldsymbol { A } } \end{array} \right| } { \left| \begin{array} { l } { e _ { i } ^ { \top } \boldsymbol { A } } \end{array} \right| } .
$$

Stage i has ‘internal order $q$ ’, if for all trees such that $r ( t ) \leq q$

$$
\Phi _ { i } ( t ) = \frac { c _ { i } ^ { r ( t ) } } { \gamma ( t ) } .
$$

The significance of this definition is that if stage $i$ has internal order $q$ , then, in any step with initial value $y _ { n - 1 } = y ( x _ { n - 1 } )$ , the value computed in stage $i$ satisfies $Y _ { i } = y ( x _ { n - 1 } + h c _ { i } ) + O ( h ^ { q + 1 } )$ . Note that the $C ( q )$ condition is

necessary and sufficient for every stage to have internal order $q$ , and this is possible only for implicit methods.

We are now in a position to generalize the remarks we have made about third and fourth order methods.

Theorem 323B Let

$$
\frac { \boldsymbol { \widetilde { c } } \mathbin { \vrule h \vrule h \vrule h \vrule h 0 . 6 1 \widetilde { \boldsymbol { A } } } } { \textup { \vrule h } ^ { \boldsymbol { \widetilde { b } } \intercal } }
$$

denote a Runge–Kutta method with $s - 1$ stages and generalized order $p - 1$ , satisfying $\widetilde { c } _ { s - 1 } \neq 1$ . Let $q$ be an integer such that $2 q + 2 \geq p$ and suppose that for any $i \in S \subset \{ 1 , 2 , \dotsc , s - 1 \}$ , the method has internal order $q$ . If there exists $b \in \mathbb { R } ^ { s }$ , with $b _ { s } \neq 0$ such that

$$
\sum _ { i = 1 } ^ { s } b _ { i } = 1 ,
$$

and such that $b _ { i } \neq 0$ implies $i \in S$ , $c _ { i } \neq 1$ and $b _ { i } ( 1 - c _ { i } ) = \widetilde { b } _ { i }$ , then the s-stage method

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

has order $p$ , where $\boldsymbol { c } ^ { \intercal } = \left[ \begin{array} { l l } { \widetilde { \boldsymbol { c } } ^ { \intercal } } & { 1 } \end{array} \right]$ and the $s \times s$ matrix $A$ is formed from $\widetilde { A }$ by adding an additional row with component $j \in \{ 1 , 2 , \ldots , s - 1 \}$ equal to $\begin{array} { r } { \left( \tilde { b } _ { j } - \sum _ { i = 1 } ^ { s - 1 } b _ { i } a _ { i j } \right) / { b _ { s } } } \end{array}$ and then adding an additional column of s zeros.

Proof. The case $p = 1$ follows from (323g), so we consider instead the case $p \geq 2$ . Also, without loss of generality we assume that $1 \leq q \leq p - 1$ , because internal order $^ { 1 }$ is equivalent to $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } } \end{array}$ and because $q \geq p$ implies internal order $p - 1$ . We first prove that

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \qquad k = 1 , 2 , \ldots , p .
$$

For $k = 1$ the result is equivalent to (323g). If the result has been proved for $k - 1 < p$ , we verify it for $k$ , thus completing an induction argument. We have

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } - \sum _ { i = 1 } ^ { s } \widetilde { b } _ { i } c _ { i } ^ { k - 2 } = \frac { 1 } { k - 1 } - \frac { 1 } { k ( k - 1 ) } = \frac { 1 } { k } .
$$

The next step is to extend the internal order property to stage $s$ . Write the

value of $\Phi _ { i } ( t )$ as $\textstyle \sum _ { j = 1 } ^ { s } a _ { i j } \chi _ { j }$ . We then have

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { \gamma ( t ) ( r ( t ) + 1 ) } = \sum _ { j = 1 } ^ { s } \tilde { b } _ { j } \chi _ { j } } & { } \\ { = \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { j } \chi _ { j } } & { } \\ { = b _ { s } \left( \displaystyle \sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } - \frac { 1 } { \gamma ( t ) } \right) + \sum _ { i = 1 } ^ { s } b _ { i } \frac { c _ { i } ^ { r ( t ) } } { \gamma ( t ) } } & { } \\ { = b _ { s } \left( \displaystyle \sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } - \frac { 1 } { \gamma ( t ) } \right) + \frac { 1 } { \gamma ( t ) ( r ( l ) + 1 ) } , } & { } \end{array}
$$

implying that

$$
\sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } = \frac { 1 } { \gamma ( t ) } .
$$

Next we prove the order condition for a tree of the form $[ \tau ^ { k - 1 } t _ { 1 } ]$ where $k + r ( t _ { 1 } ) \leq p$ . We write $\begin{array} { r } { \Phi ( t _ { 1 } ) = \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } } \end{array}$ . For $k = 1$ we have

$$
\Phi ( t ) = \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { i j } \chi _ { j } = \sum _ { j = 1 } ^ { s } \widetilde { b } _ { j } \chi _ { j } = \frac { 1 } { \gamma ( t _ { 1 } ) ( r ( t _ { 1 } ) + 1 ) } = \frac { 1 } { \gamma ( t ) } .
$$

Now assume that $k > 1$ and that the result has been proved when $k$ is replaced by $k - 1$ . For the rest of this proof, we write $\begin{array} { r } { \Phi ( [ t _ { 1 } ] ) = \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } } \end{array}$ . We have $b _ { i } c _ { i } ^ { k - 1 } = b _ { i } c _ { i } ^ { k - 2 } - \widetilde { b } _ { i } c _ { i } ^ { k - 2 }$ and hence

$$
\begin{array} { l } { \Phi ( t ) = \Phi ( [ \pi ^ { k - 1 } l _ { 1 } ] ) } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } \chi _ { i } } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } \chi _ { i } - \displaystyle \sum _ { i = 1 } ^ { s } \tilde { b } _ { i } c _ { i } ^ { k - 2 } \chi _ { i } } \\ { = \displaystyle \frac { 1 } { \gamma ( l _ { 1 } ) ( r ( t ) - 1 ) } - \frac { 1 } { \gamma ( l _ { 1 } ) r ( t ) ( r ( t ) - 1 ) } } \\ { = \displaystyle \frac { 1 } { \gamma ( l _ { 1 } ) r ( t ) } } \\ { = \displaystyle \frac { 1 } { \gamma ( l ) } . } \end{array}
$$

Finally, we consider a tree of the form $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ , where $r ( t _ { 1 } ) \geq r ( t _ { 2 } ) \geq$ $\cdots \geq r ( t _ { m } )$ . Because $2 q + 2 \geq p$ , $r ( t _ { k } ) \leq q$ for $k = 2 , 3 , \ldots , m$ . We now have

$$
\begin{array} { r l } { \Phi ( t ) } & { = \Phi ( [ i _ { 1 } L _ { 2 } , \cdot . . . , i _ { m } ] ) } \\ & { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } ^ { \prime } \prod _ { k = 2 } ^ { t ( t _ { k } ) } c _ { i } ^ { \prime } ( t _ { k } ) } \\ & { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \chi c _ { i } ^ { \prime } c _ { i } ^ { \prime } ( s ) - \overline { { 1 } } \prod _ { k = 2 } ^ { s } \gamma ( t _ { k } ) } \\ & { = \displaystyle \frac { 1 } { \prod _ { k = 2 } ^ { m } \gamma ( t _ { k } ) } \Phi ( [ r ^ { \prime ( t ) - r ( t _ { k } ) - 1 } t _ { 1 } ] ) } \\ & { = \displaystyle \frac { 1 } { r ( t ) \gamma ( t _ { k } ) \prod _ { k = 2 } ^ { m } \gamma ( t _ { k } ) } } \\ & { = \displaystyle \frac { 1 } { \gamma ( t ) } . } \end{array}
$$

Before we consider how to extend the benefits of Theorem 323B beyond the gain of a single order, we look again at the generalized order conditions

$$
\widetilde { \Phi } ( t ) = \frac { 1 } { ( r ( t ) + 1 ) \gamma ( t ) } .
$$

Because the series

$$
y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { \xi ^ { r ( t ) } h ^ { r ( t ) } } { \gamma ( t ) \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) )
$$

represents the solution of

$$
y ^ { \prime } ( x ) = f ( y ( x ) )
$$

at $x = x _ { 0 } + \xi h$ , we find by integrating term by term, from $\xi = 0$ to $\xi = 1$ , that h−1  x0+h y $\begin{array} { r } { h ^ { - 1 } \int _ { x _ { 0 } } ^ { x _ { 0 } + h } y ( x ) d x } \end{array}$ has Taylor expansion

$$
y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { h ^ { r ( t ) } } { ( r ( t ) + 1 ) \gamma ( t ) \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) ) .
$$

Hence a method satisfying (323h) for $r ( t ) \leq p$ agrees with (323i) to within $O ( h ^ { p + 1 } )$ .

We can generalize the meaning of order further by replacing the single integral by the double integral

$$
\int _ { 0 } ^ { 1 } \int _ { 0 } ^ { \overline { { \xi } } } y ( x _ { 0 } + \xi h ) d \xi d \overline { { \xi } } ,
$$

and we now find

$$
h ^ { - 2 } \int _ { x _ { 0 } } ^ { x _ { 0 } + h } \int _ { x _ { 0 } } ^ { \overline { { x } } } y ( x ) d x d \overline { { x } } = \frac { 1 } { 2 } y ( x _ { 0 } ) + \sum _ { t \in T } \frac { h ^ { r ( t ) } } { ( r ( t ) + 1 ) ( r ( t ) + 2 ) \gamma ( t ) \sigma ( t ) } F ( t ) ( y ( x _ { 0 } ) + y _ { 0 } ) ,
$$

For a method with generalized order conditions, it might seem possible to carry out the process of reducing to one less stage and the second generalization of the order conditions, but this is of little value. When we have recovered the method with the first generalization, the last abscissa will have value 1, and it will not be possible to go further to recover a method satisfying the standard order conditions.

However, this difficulty can be overcome, to some extent, by setting the last component of the abscissa vector of the first generalized method to 0 rather than to 1, with appropriate modifications made to the method of recovery. To see how this works, consider the method with first level of generalized order equal to 3 whose tableau is

$$
\begin{array} { r } { \frac { 1 } { 4 } \left| \begin{array} { l l l l } { \frac { 1 } { 4 } } & { } & { } & { } \\ { \frac { 1 } { 2 } } & { 0 } & { } & { } \\ { 0 } & { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } & { } \\ { 0 } & { \frac { 1 } { 2 } } & { - \frac { 1 } { 6 } } & { \frac { 1 } { 6 } } \end{array} \right. . } \end{array}
$$

Note that this method was constructed to satisfy not only the four generalized order conditions

$$
b ^ { \mathsf { T } } \mathbf { 1 } = { \frac { 1 } { 2 } } , \quad b ^ { \mathsf { T } } c = { \frac { 1 } { 6 } } , \quad b ^ { \mathsf { T } } c ^ { 2 } = { \frac { 1 } { 1 2 } } , \quad b ^ { \mathsf { T } } A c = { \frac { 1 } { 2 4 } } ,
$$

but also the condition

$$
\sum _ { i = 1 } ^ { 4 } { \frac { b _ { i } } { 1 - c _ { i } } } = 1 ,
$$

which is imposed in anticipation of our intention to construct a fourth order method by adding an additional stage. The new method is

$$
{ \begin{array} { r l } & { 0 } \\ & { { \frac { 1 } { 4 } } } \\ & { { \frac { 1 } { 2 } } } \\ & { { \frac { 3 } { 4 } } } \\ & { 0 } \\ & { 0 } \end{array} } { \left\{ \begin{array} { r r r r r r } { 1 } & { } & { } & { } & { } & { } \\ { } & { { \frac { 1 } { 4 } } } & { } & { } & { } & { } \\ { } & { { \frac { 1 } { 2 } } } & { 0 } & { } & { } & { } \\ { } & { 0 } & { { \frac { 1 } { 2 } } } & { } & { { \frac { 1 } { 4 } } } & { } \\ { } & { } & { } & { } & { } & { { \frac { 1 } { 4 } } } \end{array} \right. }  \\ &  { \begin{array} { r r r r r r r } { \left[ { \begin{array} { r r r r r r r } { 1 } & { } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } \\ { } & { } & { { \frac { 1 } { 6 \beta } } } & { - { \frac { 1 } { 3 \beta } } } & { { \frac { 1 } { 6 \beta } } } & { } \\ { } & { - \beta } & { { \frac { 2 } { 3 } } } & { - { \frac { 1 } { 3 } } } & { { \frac { 2 } { 3 } } } & { { \beta } } \end{array} } \right] } \end{array} }
$$

and it is an easy matter to check that all the fourth order conditions are satisfied for any choice of the non-zero parameter $\beta$ .

# 324 Order barriers

It is possible, as we have seen, to derive explicit methods with $s ~ = ~ p$ for $p = 1 , 2 , 3 , 4$ . These methods are optimal in the sense that $s ~ < ~ p$ is never possible and $p = 4$ is as high as it is possible to go with $s ~ = ~ p$ . We now formalize these remarks.

Theorem 324A If an explicit $s$ -stage Runge–Kutta method has order $p$ , then $s \geq p$ .

Proof. Let $t = [ [ \cdots [ t ] \cdot \cdot \cdot ] ]$ such that $r ( t ) = p > s$ . The order condition associated with this tree is $\Phi ( t ) = 1 / \gamma ( t )$ , where $\gamma ( t ) = p !$ and $\Phi ( t ) = b ^ { \mathsf { T } } A ^ { p - 1 } \mathbf { 1 }$ . Because $A$ is strictly lower triangular, $A ^ { p } = 0$ . Hence, the order condition becomes $0 = 1 / p !$ , which has no solution. 

Theorem 324B If an explicit $s$ -stage Runge–Kutta method has order $p \geq 5$ , then $s > p$ .

Proof. Assume $s = p$ . Evaluate the values of the following four expressions:

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) ( C - c _ { 2 } I ) c = \displaystyle { \frac { 6 } { p ! } } - \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) A c = \displaystyle { \frac { 3 } { p ! } } - \frac { c _ { 4 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ( C - c _ { 2 } I ) c = \displaystyle { \frac { 2 } { p ! } } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ^ { 2 } c = \displaystyle { \frac { 1 } { p ! } } . } } \end{array}
$$

From the left-hand sides of these expressions we observe that (324a) $\times$ (324d) = (324b) $\times$ (324c). Evaluate the right-hand sides, and we find that

$$
\left( { \frac { 6 } { p ! } } - { \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 3 } { p ! } } - { \frac { c _ { 4 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

which simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$

Now consider the four expressions

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ( C - c _ { 2 } I ) c = \displaystyle \frac { 8 } { p ! } - \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ^ { 2 } c = \displaystyle \frac { 4 } { p ! } - \frac { c _ { 5 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 2 } ( C - c _ { 2 } I ) c = \displaystyle \frac { 2 } { p ! } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 3 } c = \displaystyle \frac { 1 } { p ! } . } } \end{array}
$$

Again we see that (324e) $\times$ (324h) = (324f) $\times$ (324g), so that evaluating the right-hand sides, we find

$$
\left( { \frac { 8 } { p ! } } - { \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 4 } { p ! } } - { \frac { c _ { 5 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

leading to $c _ { 2 } ( c _ { 5 } - 1 ) = 0$ . Since we cannot have $c _ { 2 } = 0$ , it follows that $c _ { 4 } =$ $c _ { 5 } = 1$ . Now evaluate $b ^ { 1 } A ^ { p - 5 } ( C - e ) A ^ { 2 } c$ . This equals $( 4 - p ) / p !$ by the order conditions but, in contradiction to this, it equals zero because component number $i$ of $b ^ { 1 } A ^ { p - 5 }$ vanishes unless $i ~ \leq ~ 5$ . However, these components of $( C - e ) A ^ { 2 } c$ vanish. $\boxed { \begin{array} { r l } \end{array} }$

The bound $s - p \ge 1$ , which applies for $p \geq 5$ , is superseded for $p \geq 7$ by $s \mathrm { ~ - ~ } p \mathrm { ~ \geq ~ 2 ~ }$ . This is proved in Butcher (1965a). For $p \geq 8$ we have the stronger bound $s - p \ge 3$ (Butcher, 1985). It seems likely that the minimum value of $s - p$ rises steadily as $p$ increases further, but there are no published results dealing with higher orders. On the other hand, it is known, because of the construction of a specific method (Hairer, 1978), that $p = 1 0$ , $s = 1 7$ is possible.

That a sufficiently high $s$ can be found to achieve order $p$ follows immediately from Theorem 317A. We now derive an upper bound on the minimum value of such an $s$ . This is done by constructing methods with odd orders, or methods satisfying the generalization of odd orders introduced in Subsection 323. In the latter case, we then use the results of that subsection to extend the result to the next even order higher.

Theorem 324C For any positive integer $p$ , an explicit Runge–Kutta method exists with order $p$ and $s$ stages, where

$$
s = \left\{ \begin{array} { l l } { \frac { 3 p ^ { 2 } - 1 0 p + 2 4 } { 8 } , \qquad } & { p \ e v e n , } \\ { \frac { 3 p ^ { 2 } - 4 p + 9 } { 8 } , \qquad } & { p \ o d d . } \end{array} \right.
$$

Proof. We consider the case of $p$ odd, but allow for generalized order conditions. If $p = 1 + 2 m$ , we construct first an implicit Runge–Kutta method with $1 + m$ stages, using (case I) standard order conditions and (case II) generalized order conditions. For case I, the order condition associated with the tree $t$ is, as usual,

$$
\Phi ( t ) = \frac { 1 } { \gamma ( t ) } .
$$

In case II, this condition is replaced by

$$
\Phi ( t ) = \frac { 1 } { ( r ( t ) + 1 ) \gamma ( t ) } .
$$

For the implicit method, the abscissae are at the zeros of the polynomial

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m } , \mathrm { i n c a s e I , } } } \\ { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m + 1 } , \mathrm { i n c a s e I I , } } } \end{array}
$$

with the zero $x = 1$ omitted in case II. It is clear that $x = 0$ is a zero in both cases and that the remaining zeros are distinct and lie in the interval $\lfloor 0 , 1 \rfloor$ . Denote the positive zeros by $\xi _ { i }$ , $i = 1 , 2 , \dots , m$ . We now construct methods with abscissae chosen from the successive rows of the following table:

$$
\begin{array} { l l l l l l } { \mathrm { r o w ~ 0 } } & { 0 } & { 0 } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 1 } } & { } & { \xi _ { 1 } } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 2 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { } & { } & { } \\ { \mathrm { r o w ~ 3 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { } & { } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } & { } \\ { \mathrm { r o w ~ m ~ } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ { \mathrm { r o w ~ m + 1 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { } \\ { \mathrm { r o w ~ 2 } m } & { } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } \end{array}
$$

where there are exactly $m + 1$ repetitions of the rows with $m$ members. The total number of stages will then be

$$
s = 1 + { \big ( } 1 + 2 + \cdot \cdot \cdot + ( m - 1 ) { \big ) } + ( m + 1 ) m = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) .
$$

Having chosen $c = \left( \begin{array} { l l l l l l } { 0 } & { \xi _ { 1 } } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \dots } & { \xi _ { m } } \end{array} \right) ^ { 1 }$ , we construct $b ^ { \scriptscriptstyle 1 }$ with all components zero except the first component and the final $m$ components. The non-zero components are chosen so that

$$
\begin{array} { l } { { b _ { 1 } + \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } = \left\{ \begin{array} { l l } { { 1 , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { 2 } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right. } } \\ { { \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } \xi _ { i } ^ { k - 1 } = \left\{ \begin{array} { l l } { { \frac { 1 } { k } , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { k ( k + 1 ) } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right\} , \quad k = 1 , 2 , \ldots , 2 m + 1 . } } \end{array}
$$

The possibility that the non-zero $b$ components can be found to satisfy these conditions follows from the theory of Gaussian quadrature. The final step in the construction of the method is choosing the elements of the matrix $A$ . For $i$ corresponding to a member of row $k$ for $k = 1 , 2 , \ldots , m$ , the only non-zero


<!-- chunk 0004: pages 211-280 -->
$a _ { i j }$ are for $j = 1$ and for $j$ corresponding to a member of row $k - 1$ . Thus, the quadrature formula associated with this row has the form

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { k - 1 } w _ { j } \phi ( \xi _ { j } )
$$

and the coefficients are chosen to make this exact for $\phi$ a polynomial of degree $k - 1$ . For $i$ a member of row $k = m + 1 , m + 2 , \ldots , 2 m$ , the non-zero $a _ { i j }$ are found in a similar way based on the quadrature formula

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { m } w _ { j } \phi ( \xi _ { j } ) .
$$

The method constructed in this way has order, or generalized order, respectively, equal to $p = 2 m + 1$ . To see this, let ${ \widetilde { Y } } _ { i }$ denote the approximation to $y ( x _ { n - 1 } + h \xi _ { i } )$ in stage $1 + i$ of the order $2 m + 1$ Radau I method (in case I) or the order $2 m + 2$ Lobatto method (in case II). It is easy to see that the stages corresponding to row $k$ approximate the $\widetilde { Y }$ quantities to within $O ( h ^ { k + 1 } )$ . Thus the full method has order $2 m + 1$ in case I and generalized order $2 m + 1$ in case II. Add one more stage to the case II methods, as in Theorem 323B, and we obtain order $p = 2 m + 2$ with $s = { \textstyle { \frac { 1 } { 2 } } } ( 3 m ^ { 2 } + m + 4 )$ stages compared with $p = 2 m + 1$ and $\begin{array} { r } { s = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) } \end{array}$ stages in case I. This gives the result of the theorem. 

# 325 Methods of order 5

We saw in Theorem 324B that for orders greater than 4, $s = p$ is impossible. Hence, we assume that $s = 6$ . We assume the $D ( 1 )$ condition and the $C ( 2 )$ condition applied to all stages except the second. We also need to assume the subsidiary conditions $\begin{array} { r } { b _ { 2 } = \sum _ { i = 3 } ^ { 5 } b _ { i } ( 1 - c _ { i } ) a _ { i 2 } = 0 } \end{array}$ . These conditions dispose of all conditions except those associated with the trees

$$
\bar { \cdot } , \bar { \bf \Xi } _ { \ast } , \bar { \bf \Xi } _ { \ast } , \bar { \bf \Xi } _ { \ast } \Psi , \bar { \bf \Xi } _ { \ast } \Psi .
$$

The second and third of these turn out to be consequences of the $D ( 1 )$ and $C ( 2 )$ conditions, and we find that some of the elements in the final row can be evaluated in two different but consistent ways. The condition associated with $\gamma$ can be replaced by the difference of this condition and the automatically satisfied condition associated with ; see (325h) below. This last modification of the order conditions we actually solve has the advantage that it removes the last row of the $A$ matrix from the calculation until, at the end, we compute this row using the $D ( 1 )$ condition.

Collecting these comments together, we summarize the defining equations for a fifth order method. Where we write ‘choose’ one of the coefficients, we mean that it can be set to an arbitrary value, excluding only a finite set of possibilities. We do not state in detail what constitute the exceptional cases, but these can be identified with little difficulty:

$$
\begin{array} { c } { { c _ { 6 } = 1 , } } \\ { { \mathrm { C h o o s e ~ } c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 6 } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , ~ k = 1 , 2 , . . . , 5 , } } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 2 } ^ { i - 1 } a _ { i j } c _ { j } = \frac { 1 } { 2 } c _ { i } ^ { 2 } , ~ i = 3 , 4 , 5 , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } = c _ { i } , ~ i = 2 , 3 , 4 , 5 , } } \\ { { \displaystyle \sum _ { i = 3 } ^ { 5 } b _ { i } ( 1 - c _ { i } ) a _ { i 2 } = 0 , } } \\ { { \displaystyle b _ { 3 } ( 1 - c _ { 5 } ) a _ { 5 4 } c _ { 1 } ( c _ { 4 } - c _ { 5 } ) = \frac { 1 } { 6 0 } - \frac { c _ { 3 } } { 2 4 } , } } \\ { { \displaystyle \sum _ { i = j + 1 } ^ { 5 } b _ { i } a _ { i j } = b _ { j } ( 1 - c _ { i } ) , ~ j = 1 , 2 , 3 , 4 , 5 . } } \end{array}
$$

The following schema shows which of these various defining equations are used in the choice of particular coefficients of the method:

<table><tr><td>0 (325b) (325b) (325b) (325b)</td><td>(325f) (325f) (325f) (325f)</td><td>(325e) (325d) (325g) (325i)</td><td>(325e) (325e) (325i)</td><td>(325h) (325i)</td><td>(325i)</td></tr><tr><td>(325a)</td><td>(325i) (325c)</td><td>0</td><td>(325c)</td><td>(325c) (325c)</td><td>(325c)</td></tr></table>

We give a single example of a method derived in this manner:

<table><tr><td></td><td colspan="5"></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>云</td><td>1</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>3</td><td></td><td>GR</td><td></td></tr><tr><td></td><td>16</td><td>GR</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td></td><td>7 90</td><td>0</td><td>1</td><td>1</td><td>1 7 90</td></tr></table>

The first methods of this order, derived by Kutta (1901), have a different structure. One of these, as corrected by Nystr¨om (1925), is

<table><tr><td>0 </td><td rowspan="16"></td><td rowspan="4"></td><td rowspan="4">2</td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td><td></td><td>3</td><td>影</td><td></td></tr><tr><td></td><td>中</td><td></td><td></td><td>0</td></tr><tr><td rowspan="2"></td><td></td><td rowspan="2"></td><td rowspan="2">15452万</td><td></td></tr><tr><td>0</td><td>27</td></tr><tr><td rowspan="2"></td><td>23 192</td><td rowspan="2"></td><td rowspan="2">125 192</td><td>64</td><td>125 192</td></tr><tr><td></td><td>0</td><td></td></tr></table>

As we have pointed out in Subsection 316, the order conditions for a scalar first order differential equation are less restrictive than for the general vector case, if orders of 5 or more are under consideration. This suggests the existence of methods whose orders, when applied to a single first order differential equation, may be 5, whereas it is only 4 when applied to a higher-dimensional system. An example of such a method is given in Butcher (1995).

# 326 Methods of order 6

The first methods of order 6 were derived by Huˇta (1956, 1957). Although his methods used $s = 8$ stages, it is possible to find methods of this order with $s = 7$ . Just as for order 5, we assume the modified $C ( 2 )$ condition and the $D ( 1 )$ condition. We also assume the quadrature conditions so that the only order conditions that remain are $\Phi ( t ) = 1 / \gamma ( t )$ for the trees

$$
t = \{ \begin{array} { c c c c c c } { \ddot { \bigtriangledown } , } & { \ddot { \bigtriangledown } , } & { \ddot { \bigtriangledown } ^ { \prime } } & { \mathrm { ~  ~ \nabla ~ } _ { \mathrm { a n d } } } & { \ddot { \bigtriangledown } ^ { \prime } . } \end{array} \}
$$

Linear combinations of these with other order conditions whose truth is automatic appear in (326h)–(326k) below, where we have listed all the conditions we need to specify a method:

$$
\begin{array} { c } { { b _ { 2 } = 0 , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 3 } ) ( c _ { i } - c _ { 4 } ) c _ { i } = } } \\ { { \displaystyle \frac { 1 } { 3 0 } - \frac { c _ { 3 } + c _ { 4 } + c _ { 6 } } { 2 0 } + \frac { c _ { 3 } c _ { 4 } + c _ { 3 } c _ { 6 } + c _ { 4 } c _ { 6 } } { 1 2 } - \frac { c _ { 3 } c _ { 4 } c _ { 6 } } { 6 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 4 } ) c _ { i } = \frac { 1 } { 2 0 } - \frac { c _ { 4 } + c _ { 6 } } { 1 2 } + \frac { c _ { 4 } c _ { 6 } } { 6 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) c _ { i } = \frac { 1 } { 1 2 } - \frac { c _ { 6 } } { 6 } , } } \end{array}
$$

$$
\begin{array} { c c } { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) c _ { i } ( \varepsilon - \omega _ { i } ^ { \prime } ) } } \\ { { \le } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\  { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) } \\ { { \le } } \\   \displaystyle \sum _ { i = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^  \prime  \end{array}
$$

$$
\begin{array} { r l } { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( n _ { k } ( \xi ) - c _ { k } ) ( \xi - c _ { k } ) ( \xi - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta - c _ { k } } { 1 2 } + \frac { c _ { k } \Delta c _ { k } } { 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( 1 - c _ { k } ) ( \xi ) , \quad \quad k = - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad + \frac { c _ { k } \Delta c _ { k } } { 2 ( \xi - \xi ) } + \frac { \Delta } { 1 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad + \frac { c _ { k } \Delta c _ { k } } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad ) } & { \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } ) , \quad \quad } \\  \sum _  k = 1 \end{array}
$$

This rather formidable set of equations can be solved in a systematic and straightforward manner except for one detail: there are three equations, (326i), (326j) and (326k), each involving $a _ { 5 4 }$ and $a _ { 6 5 }$ and no other elements of $A$ . Hence, we need to ensure, by restricting the choice of $c$ , that these equations are consistent. To find the consistency condition, note that the left-hand sides of these equations are related by (3 $2 6 \mathrm { i } ) \times ( 3 2 6 \mathrm { j } ) = ( 3 2 6 \mathrm { b } ) \times ( 3 2 6 \mathrm { k } )$ . The consistency condition, found from the right-hand sides, simplifies to

$$
\begin{array} { r } { ( c _ { 6 } - 1 ) \left( c _ { 4 } ( 2 - 1 0 c _ { 3 } + 1 5 c _ { 3 } ^ { 2 } ) - c _ { 3 } \right) = 0 . } \end{array}
$$

We can eliminate the factor $c _ { 6 } - 1$ because, if it were zero, then it would follow that $\begin{array} { r } { c _ { 3 } = \frac { 1 } { 3 } } \end{array}$ and that $c _ { 4 } = 1$ , which are consistent with the vanishing of the second factor, which leads to

$$
c _ { 4 } = \frac { c _ { 3 } } { 2 - 1 0 c _ { 3 } + 1 5 c _ { 3 } ^ { 2 } } .
$$

Having chosen $c _ { 3 }$ , and therefore $c _ { 4 }$ , together with arbitrary $c _ { 2 }$ , $c _ { 5 }$ and $c _ { 6 }$ and the known value $c _ { 7 } = 1$ , excluding some impossible cases, we can solve for the components of $b ^ { \intercal }$ from (326a)–(326g). We can then solve for $a _ { 5 4 }$ , $a _ { 6 4 }$ and $a _ { 6 5 }$ from the consistent equations (326h)–(326k). We then solve for $a _ { 3 2 }$ from (326l) and then for $a _ { 4 2 }$ , $a _ { 4 3 }$ , $a _ { 5 2 }$ , $a _ { 5 3 }$ , $a _ { 6 2 }$ and $a _ { 6 3 }$ from (326l) with $i = 4 , 5 , 6$ and from (326o), (326p) and (326q). It remains to compute the first column of $A$ from (326m) and the last row from (326n).

The following example is of a method derived from these equations:

<table><tr><td>0 D</td><td>1 0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>中</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>24</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>33</td><td>43</td><td></td><td>118</td><td>花 195</td><td>80</td><td></td></tr><tr><td></td><td>260</td><td>13</td><td>156</td><td></td><td>39</td><td></td><td>39</td><td></td></tr><tr><td></td><td>13 200</td><td>0</td><td>11 40</td><td></td><td>11 40</td><td>A</td><td>A</td><td>13 200</td></tr></table>

It is possible to derive sixth order methods in other ways. For example, Huˇta used the $C ( 3 )$ with subsidiary conditions for stages 2 and 3. However, he used $s = 8$ , and this gave him more freedom in the choice of $c$ .

The alternative example of a method of this order that we give uses $C ( 2 )$ and $D ( 2 )$ with subsidiary conditions to repair the gaps in the order conditions caused by $C ( 2 )$ not applying to stage 2 and $D ( 2 )$ not holding for stage 6. It is necessary to choose $b _ { 2 } = 0$ , and to require that $c _ { 3 }$ , $c _ { 4 }$ and $c _ { 5 }$ are related so that the right-hand side vanishes in the equations

$$
\begin{array} { c } { { \displaystyle \sum _ { i , j = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 5 } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \frac { 1 } { 9 0 } - \frac { c _ { 3 } } { 4 0 } - \frac { c _ { 5 } } { 6 0 } + \frac { c _ { 3 } c _ { 5 } } { 2 4 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 3 } ) ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 5 } ) c _ { i } = } } \\ { { \displaystyle \frac { 1 } { 3 0 } - \frac { c _ { 3 } + c _ { 4 } + c _ { 5 } } { 2 0 } + \frac { c _ { 3 } c _ { 4 } + c _ { 3 } c _ { 5 } + c _ { 4 } c _ { 5 } } { 1 2 } - \frac { c _ { 3 } c _ { 4 } c _ { 5 } } { 6 } , } } \end{array}
$$

because the left-hand sides are identically zero. A method derived along these lines is as follows:

<table><tr><td>0 #</td><td rowspan="11"></td><td rowspan="4">2 4</td><td rowspan="4"></td><td rowspan="4">65</td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4">19</td></tr><tr><td>0 110</td></tr><tr><td>169</td></tr><tr><td>1458 44</td></tr><tr><td></td><td>729 88</td><td>1458 76</td><td>336</td><td></td></tr><tr><td>15</td><td>675</td><td>135 351</td><td>325</td><td></td></tr><tr><td>0</td><td>21</td><td>0 105</td><td>324</td><td>45</td></tr><tr><td></td><td>106</td><td>689</td><td>689</td><td>106</td></tr><tr><td>1</td><td>2517</td><td>55</td><td>10615 567</td><td>7245</td></tr><tr><td></td><td>4864</td><td>38</td><td>31616</td><td>7904</td><td>4864</td><td>2597 2432</td></tr><tr><td></td><td>0</td><td>0</td><td>1375 4992</td><td>6561 20384</td><td>3375 12544</td><td>53 768 294</td></tr></table>

# 327 Methods of orders greater than 6

Methods with order 7 must have at least nine stages. It is possible to construct such a method using the principles of Subsection 323, extending the approach used in Subsection 326. The abscissa vector is chosen as

$$
\begin{array} { r } { c = [ 0 \quad \frac { 1 } { 3 } c _ { 4 } \quad \frac { 2 } { 3 } c _ { 4 } \quad c _ { 4 } \quad c _ { 5 } \quad c _ { 6 } \quad c _ { 7 } \quad 0 \quad 1 ] ^ { \intercal } , } \end{array}
$$

and the orders of stages numbered $4 , 5 , \dots , 9$ are forced to be 3. To achieve consistency of the conditions

$$
\begin{array} { c } { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } a _ { j k } c _ { k } ( c _ { k } - c _ { 4 } ) ( c _ { k } - c _ { 5 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 4 \cdot 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } } { 3 \cdot 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 3 \cdot 4 \cdot 5 } , } } \\ { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) ( c _ { j } - c _ { 6 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } + c _ { 6 } } { 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } + c _ { 4 } c _ { 6 } + c _ { 5 } c _ { 6 } } { 3 \cdot 4 \cdot 5 } - \frac { c _ { 4 } c _ { 5 } c _ { 6 } } { 2 \cdot 3 \cdot 4 } , } } \\ { { { } } } \\ { { \displaystyle \sum b _ { i } ( 1 - c _ { i } ) c _ { i } a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) = \frac { 1 } { 4 \cdot 6 \cdot 7 } - \frac { c _ { 4 } } { 3 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 4 \cdot 5 } } } \end{array}
$$

it is found that

$$
c _ { 6 } = \frac { u - 1 2 v + 7 u v } { 3 - 1 2 u + 2 4 v + 1 4 u ^ { 2 } - 7 0 u v + 1 0 5 v ^ { 2 } } ,
$$

where $u = c _ { 4 } + c _ { 5 }$ and $v = c _ { 4 } c _ { 5 }$ . The value of $c _ { 7 }$ is selected to ensure that

$$
\int _ { 0 } ^ { 1 } x ( 1 - x ) ( x - c _ { 4 } ) ( x - c _ { 5 } ) ( x - c _ { 6 } ) ( x - c _ { 7 } ) d x = 0 .
$$

The tableau for a possible method derived along these lines is

<table><tr><td>0 G</td><td rowspan="16"></td><td colspan="2"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td></tr><tr><td>1 0</td><td>1</td><td></td></tr><tr><td>1</td><td>0 3</td><td></td></tr><tr><td></td><td>0 150</td><td></td></tr><tr><td></td><td>148 0</td><td>1331</td><td>56</td><td></td><td></td></tr><tr><td></td><td>1331 404</td><td>170</td><td>1331</td><td></td><td></td></tr><tr><td></td><td>243</td><td>27</td><td>4024 1701</td><td>10648</td><td></td></tr><tr><td></td><td>2466</td><td>1242</td><td>19176</td><td>1701 51909</td><td>1053</td></tr><tr><td></td><td>2401</td><td>0 343</td><td>16807</td><td></td><td></td></tr><tr><td>0</td><td>5</td><td>0</td><td></td><td>96</td><td>16807 1815</td><td>2401 405</td><td>49</td></tr><tr><td></td><td>154</td><td></td><td>0</td><td>539</td><td>20384</td><td>2464</td><td>1144</td></tr><tr><td>1</td><td>113</td><td>0</td><td>195</td><td>32</td><td>29403</td><td>729</td><td>1029 21</td></tr><tr><td></td><td>32</td><td></td><td>22</td><td></td><td></td><td>512</td><td>1408</td></tr><tr><td></td><td></td><td></td><td></td><td>7</td><td>3584</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>32</td><td>1771561</td><td>243</td><td>16</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td>16807 77</td></tr><tr><td></td><td></td><td></td><td></td><td>105</td><td>6289920</td><td>2560</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>74880</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1440</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Order 8 requires 11 stages, and methods of this order were derived by Curtis (1970)and Cooper and Verner (1972). In each case the abscissae were based on the Lobatto quadrature formula with three internal points. We quote the method of Cooper and Verner in Table 327(I).

Although order 9 has not attracted much interest, and it is unknown how many stages are required to achieve this order, order 10 has posed a challenge. In Curtis (1975) a method of order 10 was presented with 18 stages. However, using an ingenious combination of various simplifying assumptions, Hairer (1978) accomplished this feat in 17 stages. It is still not known if fewer stages are possible.

# Exercises 32

32.1 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 2 } } } , 1 ]$ .

32.2 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 3 } } } , 1 ]$ .

32.3 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $\textstyle c _ { 2 } = { \frac { 1 } { 5 } }$ .

32.4 Find a method with $s = p = 4$ such that $b _ { 2 } = 0$ and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ .

32.5 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $c _ { 3 } = 0$ .

32.6 Show that Lemma 322A can be used to prove that $c _ { 4 } = 1$ , if $s = p \geq 4$ .

32.7 Show that Lemma 322A can be used to prove that $c _ { 5 } = 1$ , if $s = p \geq 5$ leading to an alternative proof of Theorem 324B.

<table><tr><td>% 08I I 6</td><td>贵</td><td>08 6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>81 12-65</td><td>亚 227281</td><td>Z</td><td>2 2223125533173153111</td><td>业 18781</td><td>81 2+2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>I</td></tr><tr><td></td><td>2</td><td>99</td><td>509</td><td>2555</td><td></td><td></td><td></td><td></td><td>红</td><td>V</td></tr><tr><td></td><td></td><td>2173121111111-1113171112111311111-1111</td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>T</td><td>1+2</td></tr><tr><td></td><td></td><td>82 35533211</td><td>1111 12712188</td><td>兴</td><td>99 110-16</td><td>0</td><td>0</td><td>0</td><td>2 T</td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td>I</td></tr><tr><td></td><td></td><td></td><td></td><td>1213531</td><td>1241</td><td>0</td><td>0</td><td>0</td><td>T</td><td>1A-2</td></tr><tr><td></td><td></td><td></td><td></td><td>0</td><td>0 1271111451</td><td>06</td><td>118 227222231</td><td>0</td><td>W</td><td>V</td></tr><tr><td></td><td></td><td></td><td></td><td>32731351</td><td></td><td>3575555315</td><td></td><td></td><td>-01</td><td>1-2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>08 122-99</td><td>098 22245223111</td><td>9 1+6</td><td>0</td><td>8</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+9</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>222</td><td>9 1+81</td><td>0</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>-2</td><td>6</td><td>86</td><td>+</td><td>+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+1</td><td>120-2-</td><td>1</td><td>1+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 33 Runge–Kutta Methods with Error Estimates

# 330 Introduction

Practical computations with Runge–Kutta methods usually require a means of local error estimation. This is because stepsizes are easy to adjust so as to follow the behaviour of the solution, but the optimal sequence of stepsizes depends on the local truncation error. Of course, the exact truncation error cannot realistically be found, but asymptotically correct approximations to it can be computed as the integration proceeds. One way of looking at this is that two separate approximations to the solution at a step value $x _ { n }$ are found. Assuming that the solution value at the previous point is regarded as exact, because it is the local error that is being approximated, denote the two solutions found at the current point by $y _ { n }$ and ${ \hat { y } } _ { n }$ . Suppose the two approximations have orders $p$ and $q$ , respectively, so that

$$
y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } ) , \qquad { \widehat { y } } _ { n } = y ( x _ { n } ) + O ( h ^ { q + 1 } ) .
$$

Then, if $q > p$

$$
{ \widehat { y } } _ { n } - y _ { n } = y ( x _ { n } ) - y _ { n } + O ( h ^ { p + 2 } ) ,
$$

which can be used as an approximation to the error committed in the step. Furthermore, the approximation becomes increasingly accurate as $h$ becomes small. Thus ${ \widehat { y } } _ { n } - y _ { n }$ is used as the error estimator.

Even though we emphasize the construction of method pairs for which $q = p + 1$ , and for which it is $y _ { n }$ (rather than the asymptotically more accurate approximation ${ \widehat { y } } _ { n }$ ) that is propagated as the numerical approximation at $x _ { n }$ , customary practice is to use the higher order as the propagated value. This is sometimes interpreted as ‘local extrapolation’, in the sense that the error estimate is added to the approximate solution as a correction. While the estimator is still used as a stepsize controller, it is now no longer related asymptotically to the local truncation error.

We review the ‘deferred approach to the limit’ of Richardson (1927) and then consider specially constructed Runge–Kutta tableaux, which combine two methods, with orders one apart, built into one. The classical method of this type is due to Merson (1957), but we also consider built-in estimators due to Fehlberg (1968, 1969), Verner (1978) and Dormand and Prince (1980). Some of the methods derived for the author’s previous book (Butcher, 1987) will also be recalled.

# 331 Richardson error estimates

Richardson extrapolation consists of calculating a result in a manner that depends on a small parameter, and for which the error in the calculation varies systematically as the parameter varies. By using a sequence of values of the parameter, much of the effect of the errors can be eliminated so that improved accuracy results. In numerical quadrature, for example, the method of Romberg (1955) is based on calculating an integral $\begin{array} { r } { I = \int _ { a } ^ { b } \phi ( x ) d x } \end{array}$ using the trapezoidal rule with a stepsize $h$ equal to an integer divisor of $b - a$ . For a single choice of $h$ , the result computed can be expanded by an asymptotic formula of the form

$$
T ( h ) = I + C _ { 1 } h ^ { 2 } + C _ { 2 } h ^ { 4 } + \cdot \cdot \cdot ,
$$

so that, using a sequence $\begin{array} { l l l } { { h } } & { { = } } & { { H , 2 ^ { - 1 } H , 2 ^ { - 2 } H , . . . . } } \end{array}$ , we arrive at the approximations $T _ { 0 } = T ( H )$ , $T _ { 1 } = T ( \textstyle { \frac { 1 } { 2 } } H )$ , $T _ { 2 } = T ( \textstyle { \frac { 1 } { 4 } } H ) _ { ; }$ . . . with expansions

$$
\begin{array} { c } { { T _ { 0 } = I + C _ { 1 } H ^ { 2 } + C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 1 } = I + \frac { 1 } { 4 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 1 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 2 } = I + \frac { 1 } { 1 6 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 2 5 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { \vdots } } \\ { { { } } } \end{array}
$$

By forming

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 } = \frac { 4 } { 3 } T _ { 1 } - \frac { 1 } { 3 } T _ { 0 } } , } \\ { ~ } \\ { { \displaystyle T _ { 1 2 } = \frac { 4 } { 3 } T _ { 2 } - \frac { 1 } { 3 } T _ { 1 } } , } \\ { ~ } \\ { { \displaystyle \quad \vdots \qquad } } \end{array}
$$

we obtain an ‘improved’ sequence in which the $C _ { 1 } H ^ { 2 }$ terms are eliminated from the asymptotic expansions so that convergence towards the exact result $I$ is more rapid as terms in the sequence are calculated. Similarly, a second sequence of improved approximations can be found from

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 2 } = \frac { 1 6 } { 1 5 } T _ { 1 2 } - \frac { 1 } { 1 5 } T _ { 0 1 } } , } \\ { { \displaystyle T _ { 1 2 3 } = \frac { 1 6 } { 1 5 } T _ { 2 3 } - \frac { 1 } { 1 5 } T _ { 1 2 } } , } \\ { { \displaystyle \quad \quad \quad \quad \quad \vdots } } \end{array}
$$

This idea has an application to Runge–Kutta methods for ordinary differential equations on the small scale of a single step, repeated with two steps and half the original value of $h$ . Let $y _ { n - 1 }$ denote an incoming approximation for $y ( x _ { n - 1 } )$ and $y _ { n }$ the solution computed as an approximation to $y ( x _ { n } ) = y ( x _ { n - 1 } + h )$ using a Runge–Kutta method with tableau

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} \right| \overset { \phantom { = } } \longrightarrow \left| \begin{array} { c c c c c } { 0 } \\ { a _ { 2 1 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \ddots } & { a _ { s , s - 1 } } \\ { b _ { 1 } } & { b _ { 2 } } & { \ddots } & { b _ { s - 1 } } & { b _ { s } } \end{array} \right. . } \end{array}
$$

Repeating the calculation with $h$ replaced by ${ \frac { 1 } { 2 } } h$ but carrying out two steps, rather than only one, is equivalent to taking a single step with the original $h$ , but using the tableau

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & \end{array}
$$

Denote the result computed by this $2 s$ -stage method by ${ \hat { y } } _ { n }$ , and note that if the local truncation error in $y _ { n }$ is $C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ , so that

$$
y _ { n } = y ( x _ { n } ) - C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

then

$$
\widehat { y } _ { n } = y ( x _ { n } ) - 2 ^ { - p } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

because the error in computing ${ \hat { y } } _ { n }$ is $2 ^ { - p - 1 } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ contributed from each of two steps.

From the difference of (331a) and (331b) we find

$$
\widehat { y } _ { n } - y _ { n } = ( 1 - 2 ^ { - p } ) C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

so that the local truncation error in $y _ { n }$ can be approximated by

$$
( 1 - 2 ^ { - p } ) ^ { - 1 } ( { \widehat { y } } _ { n } - y _ { n } ) .
$$

This seems like an expensive way of computing the error in the result computed using an $s$ -stage method, because the additional computations required for the estimation take twice as long as the result itself. However, the additional cost becomes more reasonable when we realize that it is not $y _ { n }$ but ${ \widehat { y } } _ { n }$ that should be propagated. The additional cost on this basis is something like $5 0 \%$ . Actually, it is slightly less than this because the calculation of the derivative of $y _ { n - 1 }$ is shared by each of the two methods, and needs to be carried out only once.

# 332 Methods with built-in estimates

Instead of using the Richardson technique it is possible to combine two methods into one by constructing a tableau with common stages but two alternative output coefficient vectors. The following method, due to Merson (1957), seems to have been the first attempt at constructing this type of stepsize control mechanism:

<table><tr><td>1</td><td>R 1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>0 0</td><td>GR 0</td><td>2 2</td><td>1</td></tr><tr><td></td><td>1</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

The interpretation of this tableau, which contains two $b ^ { \scriptscriptstyle 1 }$ vectors, is that it combines two methods given by

<table><tr><td rowspan=1 colspan=1>0 1-3:1-3:1-2 1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1  0    0    2  1</td></tr></table>

and by

<table><tr><td>0 N</td><td></td><td>1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>BU</td><td>0</td><td>G</td><td>2</td><td></td></tr><tr><td></td><td>1 10</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

![](images/a11978509f5592fc936d87d83461fb155c52032813e0ec83d846e80c2154f654.jpg)  
Two alternative stepsize control mechanisms based on Richardson (dashed line) and built-in (solid line) error estimates

In Merson’s derivation of this method, (332a) was shown to be of order 4. Although (332b) has order only 3, it becomes effectively of order 5 if used to solve linear problems with constant coefficients. The difference between the results computed by the two methods can, it is suggested, be used as a local error estimator. To show how well the method works in practice, an experiment using this technique has been carried out and the results summarized in Figure 332(i). The three problems attempted are the Kepler orbit problem with eccentricities $e = 0 . 1$ , $e = 0 . 5$ and $e = 0 . 9$ , respectively.

# 333 A class of error-estimating methods

In the search for efficient step-control mechanisms, we consider $( s + 1 )$ -stage methods of the form

with order $p + 1$ , with the coefficients chosen so that the embedded method

has order $p$

Even though this method formally has $s ~ + ~ 1$ stages, in terms of computational cost it can be regarded as having only $s$ , because the derivative calculation needed for stage $s + 1$ is identical to the first derivative calculation in the succeeding step. It is convenient to write order conditions for the embedded method pair in terms of the number $\boldsymbol { B } = \boldsymbol { b } _ { s + 1 }$ and the artificial tableau

$$
\begin{array}{c} { \begin{array} { r l } & { { \begin{array} { l } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} } } \\ & { { \begin{array} { r l } { c _ { 3 } } \\ { c _ { 3 } } \\ { \vdots } \end{array} } } \\ & { { \begin{array} { r l } { c _ { s } } \\ { b _ { 1 } } & { a _ { s 2 } } \end{array} } } & { \cdots \quad a _ { s , s - 1 } } \\ & { { \begin{array} { r l } { b _ { 2 } } & { \ddots \quad } \\ { b _ { 1 } } & { b _ { 2 } } & { \ddots \quad } \end{array} } } \end{array} } .  \end{array} 
$$

An elementary weight, computed using this tableau, differs from that of the full method by a single term. This additional term is formed by multiplying $B$ by the derivative of the order result found by the method represented by $p$   
(333b). This enables us to form modified order conditions for (333c), which will ensure that both (333a) and (333b) satisfy the correct conditions. We denote the elementary weights for (333c) by $\Phi ( t )$ .

Theorem 333A If (333b) has order $p$ and (333a) has order $p + 1$ and $\boldsymbol { B } = \boldsymbol { b } _ { s + 1 }$ , then

$$
\Phi ( t ) = \frac { 1 - B r ( t ) } { \gamma ( t ) } , \qquad r ( t ) \leq p + 1 .
$$

Conversely, if (333d) holds with $c _ { s } \neq 1$ and $B \neq 0$ and, in addition,

$$
\begin{array} { l } { { b _ { s + 1 } = B , } } \\ { { a _ { s + 1 , s } = B ^ { - 1 } b _ { s } ( 1 - c _ { s } ) , } } \\ { { a _ { s + 1 , j } = B ^ { - 1 } \left( b _ { j } ( 1 - c _ { j } ) - \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } a _ { i j } \right) , \qquad j = 1 , 2 , \ldots , s - 1 , } } \end{array}
$$

then (333b) has order $p$ and (333a) has order $p + 1$ .

Proof. For a given tree $t$ , let $\widehat { \Phi } ( t )$ denote the elementary weight for (333a) and $\overline { { \Phi } } ( t )$ the elementary weight for (333b). Because the latter method has order $p$ , it follows that for a tree $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ , with order not exceeding $p + 1$ , we have $\overline { { \Phi } } ( t _ { i } ) = 1 / \gamma ( t _ { i } )$ , for $i = 1 , 2 , \dots , m$ . Hence, for a method identical with (333a) except for $b ^ { \top }$ replaced by the basis vector $e _ { s + 1 } ^ { \prime }$ , the elementary weight corresponding to $t$ will be

$$
\prod _ { i = 1 } ^ { m } { \frac { 1 } { \gamma ( t _ { i } ) } } = { \frac { r ( t ) } { \gamma ( t ) } } .
$$

Adding $B$ multiplied by this quantity to $\Phi ( t )$ gives the result

$$
\Phi ( t ) + B \frac { r ( t ) } { \gamma ( t ) } = \widehat { \Phi } ( t ) = \frac { 1 } { \gamma ( t ) } ,
$$

which is equivalent to (333d).

To prove the converse, we first note that, because $B \neq 0$ , the previous argument can be reversed. That is, if (333b) has order $p$ then (333d) implies that (333a) has order $p + 1$ . Hence, it is only necessary to prove that (333b) has order $p$ . We calculate $\overline { { \Phi } } ( t )$ , for $r ( t ) \leq p$ as follows, where we have written $\chi _ { i } ( t )$ for the coefficient of $b _ { i }$ in $\Phi ( t )$

$$
\begin{array} { l } { \displaystyle \overline { { \Phi } } ( t ) = B ^ { - 1 } \sum _ { j = 1 } ^ { s } b _ { j } ( 1 - c _ { j } ) \chi _ { j } ( t ) - B ^ { - 1 } \sum _ { i = 1 } ^ { s } \sum _ { j = 1 } ^ { s - 1 } b _ { i } a _ { i j } \chi _ { j } ( t ) } \\ { \displaystyle \quad = B ^ { - 1 } ( \Phi ( t ) - \Phi ( t \tau ) - \Phi ( \tau t ) ) } \\ { \displaystyle \quad = B ^ { - 1 } \left( \frac { 1 - B r ( t ) } { \gamma ( t ) } - \frac { r ( t ) ( 1 - B ( 1 + r ( t ) ) ) } { ( 1 + r ( t ) ) \gamma ( t ) } - \frac { 1 - B ( 1 + r ( t ) ) } { ( 1 + r ( t ) ) \gamma ( t ) } \right) } \\ { \displaystyle \qquad = \frac { 1 } { \gamma ( t ) } . } \end{array}
$$

Although the derivation is carried out from a modified version of the order conditions, it is convenient to display a particular method in the format

$$
\begin{array} { r l } & { \left| \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { \frac { - - 1 - \frac { \lambda } { a _ { s - } } - \dots - \dots - \dots - } { a _ { s , s - 1 } } } \\ { \frac { c _ { s } } { c _ { s } } \left| \frac { b _ { 1 } } { d _ { 3 } } - \frac { 1 - \lambda } { d _ { 2 } } - \dots - \frac { b _ { s - 1 } } { d _ { s - 1 } } - \frac { b _ { s } } { d _ { s } } \right. } \end{array} \right| } \end{array}
$$

where

$$
\left[ d _ { 1 } \quad d _ { 2 } \quad \cdots \quad d _ { s - 1 } \quad d _ { s } \right] = \left[ b _ { 1 } - a _ { s 1 } \quad b _ { 2 } - a _ { s 2 } \quad \cdots \quad b _ { s - 1 } - a _ { s , s - 1 } \quad b _ { s } \right]
$$

is the vector of coefficients in the proposed error estimator. That is, $\textstyle h \sum _ { i = 1 } ^ { s } d _ { i } f ( Y _ { i } )$ is used to evaluate the difference between the order $p$ approximation $\begin{array} { r } { y _ { n - 1 } + h \sum _ { i = 1 } ^ { s } a _ { s + 1 , i } f ( Y _ { i } ) } \end{array}$ and the supposedly more accurate −approximation of order $p + 1$ given by $\begin{array} { r } { y _ { n - 1 } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } ) } \end{array}$ . The dashed line above row number $s$ of the tableau is intended to indicate that the row below it is the approximation to be propagated and, of course, the dashed line below the $b ^ { \intercal }$ vector separates the order $p { + 1 }$ approximation from the error estimator.

Now let us look at some example of these embedded methods. Methods of orders $^ { 1 }$ and 2 are easy to derive and examples of each of these are as follows:

$$
\frac { - \llangle 1 } { \vert - \frac { 1 } { 2 } - \frac { 1 } { 2 } \vert }
$$

and

$$
\begin{array} { r }  \frac { 0 } { \frac { 1 } { 2 } } | \begin{array} { l } { 1 } \\ { \frac { 1 } { 2 } } \\ { - \frac { 1 } { 1 } - 0 - \frac { 1 } { 0 } -- 0 } \\ { \frac { 1 } { | \frac { 1 } { 6 } - \frac { 1 } { 3 } - \frac { 1 } { 3 } - \frac { 1 } { 3 } - \frac { 1 } { 6 } } \\ { - \frac { 1 } { 6 } - \frac { 1 } { 3 } - \frac { 2 } { 3 } - \frac { 1 } { 6 } } \end{array}  } \end{array} .
$$

Observe that for the second order method, the third order method in which it is embedded is actually the classical fourth order method.

Order 3 embedded in order 4 requires $s = 4$ stages. From the modified order conditions we find that

$$
\begin{array} { c } { { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = \displaystyle { \left( \frac { 1 } { 4 } - B \right) - ( c _ { 2 } + c _ { 4 } ) \left( \frac { 1 } { 3 } - B \right) + c _ { 2 } c _ { 4 } \left( \frac { 1 } { 2 } - B \right) } , } } \\ { { b _ { 4 } a _ { 4 3 } c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = \displaystyle { \left( \frac { 1 } { 1 2 } - \frac { B } { 3 } \right) - c _ { 2 } \left( \frac { 1 } { 6 } - \frac { B } { 2 } \right) } , } } \\ { { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) a _ { 3 2 } c _ { 2 } = \displaystyle { \left( \frac { 1 } { 8 } - \frac { B } { 2 } \right) - c _ { 4 } \left( \frac { 1 } { 6 } - \frac { B } { 2 } \right) } , } } \\ { { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \displaystyle { \left( \frac { 1 } { 2 4 } - \frac { B } { 6 } \right) } , } } \end{array}
$$

so that, equating the products (333h) $\times$ (333k) and (333i) $\times$ (333j) and simplifying, we find the consistency condition

$$
c _ { 4 } = \frac { 1 - 7 B + 1 2 B ^ { 2 } } { 1 - 6 B + 1 2 B ^ { 2 } } .
$$

For example, choosing $B = \textstyle { \frac { 1 } { 1 2 } }$ to give $c _ { 4 } = \textstyle { \frac { 6 } { 7 } }$ , together with $c _ { 2 } = { \frac { 2 } { 7 } }$ and $\textstyle c _ { 3 } = { \frac { 4 } { 7 } }$ , yields the tableau

<table><tr><td></td><td colspan="5"></td></tr><tr><td>G5</td><td>中</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>G</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>35</td><td></td><td>立</td></tr><tr><td></td><td></td><td></td><td>96</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>5</td><td></td><td></td></tr><tr><td></td><td>品</td><td></td><td>96</td><td></td><td></td></tr></table>

Order 4 embedded in order 5 requires $s = 6$ . That is, there are seven stages overall, but the last stage derivative is identical to the first stage derivative for the following step. To derive a method of this type, make the simplifying assumption

$$
\sum _ { j = 1 } ^ { 6 } a _ { i j } c _ { j } = { \frac { 1 } { 2 } } c _ { i } ^ { 2 } , \qquad i \neq 2 ,
$$

together with the subsidiary conditions

$$
b _ { 2 } = \sum _ { i = 3 } ^ { 6 } b _ { i } a _ { i 2 } = \sum _ { i = 3 } ^ { 6 } b _ { i } c _ { i } a _ { i 2 } = \sum _ { i = 4 } ^ { 6 } \sum _ { j = 3 } ^ { i - 1 } b _ { i } a _ { i j } a _ { j 2 } = 0 .
$$

Also, impose order conditions for the trees but instead of the corresponding conditions for the trees $\gamma _ { \textit { v } } \gamma _ { \textit { i } } \gamma _ { \textit { i } } ^ { \textit { v } } \}$ , use linear combinations as follows:

$$
\begin{array} { c } { { \displaystyle \sum _ { 6 \geq i > j \geq 4 } b _ { i } a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \left( \frac 1 { 1 2 } - \frac 1 3 B \right) - c _ { 3 } \left( \frac 1 6 - \frac 1 2 B \right) , } } \\ { { \displaystyle \sum _ { 5 \geq i \geq 5 } b _ { i } c _ { i } ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 3 } ) = \left( \frac 1 5 - B \right) - \left( c _ { 6 } + c _ { 4 } + c _ { 3 } \right) \left( \frac 1 4 - B \right) } } \\ { { + ( c _ { 6 } c _ { 4 } + c _ { 6 } c _ { 3 } + c _ { 4 } c _ { 3 } ) \left( \frac 1 3 - B \right) } } \\ { { - c _ { 6 } c _ { 4 } c _ { 3 } \left( \frac 1 2 - B \right) , } } \end{array}
$$

$$
\begin{array} { r l r } { \sum _ { } } & { } & { b _ { i } ( c _ { i } - c _ { 6 } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \left( \frac { 1 } { 1 5 } - \frac { 1 } { 3 } B \right) - c _ { 6 } \left( \frac { 1 } { 1 2 } - \frac { 1 } { 3 } B \right) } \\ { \frac { } { 5 \geq i > j \geq 4 } } & { } & { - c _ { 3 } \left( \frac { 1 } { 8 } - \frac { 1 } { 2 } B \right) + c _ { 6 } c _ { 3 } \left( \frac { 1 } { 6 } - \frac { 1 } { 2 } B \right) , } \end{array}
$$

$$
\begin{array} { r l r } {  { \sum _ { 6 \geq i > j \geq 5 } b _ { i } a _ { i j } c _ { j } ( c _ { i } - c _ { 4 } ) ( c _ { j } - c _ { 3 } ) = ( \frac { 1 } { 2 0 } - \frac { 1 } { 4 } B ) - ( c _ { 4 } + c _ { 3 } ) ( \frac { 1 } { 1 2 } - \frac { 1 } { 3 } B ) } } \\ & { } & { + c _ { 4 } c _ { 3 } ( \frac { 1 } { 6 } - \frac { 1 } { 2 } B ) , } \end{array}
$$

$$
\sum _ { 6 \geq i > j > k \geq 4 } b _ { i } a _ { i j } a _ { j k } c _ { k } ( c _ { k } - c _ { 3 } ) = \left( \textstyle { \frac { 1 } { 6 0 } } - \frac { 1 } { 1 2 } { \cal B } \right) - c _ { 3 } \left( \textstyle { \frac { 1 } { 2 4 } } - \frac { 1 } { 6 } { \cal B } \right) .
$$

The left-hand sides of (333m)–(333p) consist of only a single term and we see that the product of (333m) and (333p) is equal to the product of (333n) and (333o). Thus we obtain consistency conditions for the values of $a _ { 6 5 }$ and $a _ { 5 4 }$ by comparing the products of the corresponding right-hand sides. After considerable manipulation and simplification, we find that this consistency condition reduces to

$$
c _ { 6 } = 1 - \frac { q _ { 0 } B } { q _ { 0 } - q _ { 1 } B + q _ { 2 } B ^ { 2 } } ,
$$

with

$$
\begin{array} { r l } & { q _ { 0 } = 1 0 c _ { 3 } ^ { 2 } c _ { 4 } + 2 c _ { 4 } - 8 c _ { 3 } c _ { 4 } - c _ { 3 } , } \\ & { q _ { 1 } = 6 0 c _ { 3 } ^ { 2 } c _ { 4 } - 5 6 c _ { 3 } c _ { 4 } + 1 6 c _ { 4 } - 8 c _ { 3 } , } \\ & { q _ { 2 } = 1 2 0 c _ { 3 } ^ { 2 } c _ { 4 } - 1 2 0 c _ { 3 } c _ { 4 } + 4 0 c _ { 4 } - 2 0 c _ { 3 } . } \end{array}
$$

Construction of the method consists of selecting $c _ { 2 }$ , $c _ { 3 }$ , $c _ { 4 }$ , $c _ { 5 }$ and $B$ ; choosing $c _ { 6 }$ in accordance with (333q); evaluating $a _ { 6 5 }$ and $a _ { 5 4 }$ from the consistent equations (333n), (333o) and (333p); and then evaluating $a _ { 6 4 }$ from (333l). The remaining coefficients are then evaluated using the remaining conditions that have been stated.

An example of a method in this family is

$$
 \begin{array} { r l } & { { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \frac { 1 } { 4 } } \end{array} \right] } \qquad { \begin{array} { r l } { 1 } & { } \\ { \frac { 1 } { 4 } } \end{array} } } \\ & { { \left[ \begin{array} { l l l l l l } { 1 } & { } & { } & { } & { } & { } & { } \\ { 0 } & { } { } & { } & { } & { } & { } & { } \\ { { \frac { 1 } { 4 } } } \end{array} \right] } \qquad { \begin{array} { r l } { 1 } & { } & { } & { } & { } & { } \\ { { \frac { 1 } { 8 } } } & { } & { } & { } & { } & { } & { } \\ { 0 } & { } { } & { } { - { \frac { 1 } { 2 } } } \end{array} } } \\ & { } &   \begin{array} { r l } { { \frac { 1 3 } } } & { } { 1 3 } & { } & { } & { } & { } & { } \\ { { \frac { 1 0 3 } { 2 0 } } } & { } { } & { - { \frac { 2 9 9 9 } { 1 0 0 0 } } } & { } & { { \frac { 7 8 } { 1 2 5 } } } & { } { \qquad { \frac { 1 3 } { 8 0 } } } & { } \\ { - { \frac { 6 } { 1 5 4 } } - { \frac { 7 4 1 5 } { 3 7 5 } } - { \frac { 6 8 5 } { 2 5 } } - { \frac { 5 7 2 5 } { 6 } } - { \frac { 5 7 2 } { 6 } } - { \frac { 5 7 5 } { 6 } } - { \frac { 5 7 5 } { 6 } } - - { \frac { 5 7 5 } { 6 } } } \\ { - { \frac { 5 7 3 } { 3 1 2 } } - } & { } & { } & { } & { } & { } \\ { { \frac { 1 0 1 } { 3 4 2 } } } & { } & { 0 } & { { \frac { 1 6 } { 3 8 } } } & { - { \frac { 1 6 0 } { 1 5 0 0 } } - { \frac { 5 7 5 } { 1 5 0 0 } } - { \frac { 1 3 } { 1 5 0 0 } } - { \frac { 1 3 } { 1 5 0 } } - { \frac { 7 5 7 } { 5 7 5 } } - \cdots } \\  - { \frac { 7 5 } { 3 1 0 } } - { \frac { 7 5 } { 6 } } - { \frac { 1 } { 1 5 0 } } - { \frac { 1 5 } { 1 3 5 } } -  \end{array} \end{array}
$$

For $p = 5$ , that is, a fifth order method embedded within a sixth order method, $s = 8$ seems to be necessary. We present a single example of a method satisfying these requirements. For all stages except the second, the stage order is at least 2, and for stages after the third, the stage order is at least 3. Under these assumptions, together with subsidiary conditions, it is found that for consistency, a relation between $c _ { 4 }$ , $c _ { 5 }$ , $c _ { 6 }$ , $c _ { 8 }$ and $B$ must hold. Given that these are satisfied, the derivation is straightforward but lengthy and will not be presented here. The example of a method pair constructed in this way is shown in the following tableau:

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 1-</td><td></td><td>1 18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td>0</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>2</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>15</td><td>0</td><td>63</td><td></td><td>7</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>8</td><td></td><td>8</td><td></td><td></td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>93</td><td>0</td><td>24921</td><td></td><td>10059</td><td>735</td><td>735</td><td></td><td></td><td></td></tr><tr><td>4</td><td>22</td><td></td><td>1408</td><td></td><td>704</td><td>1408</td><td>704</td><td></td><td></td><td></td></tr><tr><td>17</td><td>86547313055</td><td>0</td><td></td><td>96707067 15526951598 27949088</td><td></td><td></td><td></td><td>452648800 270189568 467982711</td><td></td><td></td></tr><tr><td>19</td><td>10295610642</td><td></td><td>2867062</td><td></td><td>571978869</td><td>81711267</td><td>245133801</td><td></td><td>390963</td><td></td></tr><tr><td></td><td>98 765</td><td>0</td><td>0</td><td></td><td>9 83</td><td>071 1600</td><td>75</td><td>64 225</td><td>2257600</td><td></td></tr><tr><td></td><td>188</td><td></td><td></td><td></td><td>1593</td><td>2943</td><td>197</td><td>576</td><td>2476099</td><td>2</td></tr><tr><td></td><td>3315</td><td></td><td>0</td><td></td><td>7553</td><td>20800</td><td>975</td><td>2275</td><td>29348800</td><td>39</td></tr><tr><td></td><td>142</td><td></td><td></td><td></td><td>2412</td><td>549</td><td>68</td><td>128</td><td>130321</td><td>2</td></tr><tr><td></td><td></td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>39</td></tr><tr><td></td><td>1989</td><td></td><td></td><td></td><td>7553</td><td>1040</td><td>195</td><td>4095</td><td>1467440</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 334 The methods of Fehlberg

Early attempts to incorporate error estimators into Runge–Kutta methods are exemplified by the work of Fehlberg (1968, 1969). In writing the coefficients of methods from this paper, a tabular form is used as follows:

$$
\begin{array} { r } { \frac { c } { \vert \vert \mathbf { \epsilon } \vert } . } \\ { \frac { \vert \widehat { b } ^ { \intercal } } { \vert \widehat { b } ^ { \intercal } } . } \end{array}
$$

The significance of this augmented tableau is that

$$
\frac { c \mid A } { b ^ { \top } }
$$

is a Runge–Kutta method of order $p$ , while

$$
\frac { c \dag A } { \ d b ^ { \dagger } }
$$

is a Runge–Kutta method of order $p + 1$ . The additional vector $\boldsymbol { d } ^ { \intercal } = \widehat { \boldsymbol { b } } ^ { \intercal } - \boldsymbol { b } ^ { \intercal }$ is used for error estimation. The fifth order method, with additional sixth order output for error estimation, recommended by Fehlberg, is

<table><tr><td>0 D</td><td rowspan="16"></td><td rowspan="4"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>提</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>中</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>144</td><td>-4</td><td>花</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>361</td><td>25 18</td><td>407</td><td></td><td>55</td><td></td><td></td><td></td></tr><tr><td>1</td><td>320</td><td>5</td><td>128</td><td></td><td>128</td><td></td><td></td><td></td></tr><tr><td>0</td><td>11</td><td></td><td>11</td><td>11</td><td>11</td><td>0</td><td></td><td></td></tr><tr><td></td><td>640</td><td>0</td><td>256</td><td>160</td><td>256</td><td></td><td></td><td></td></tr><tr><td>1</td><td>93</td><td>18</td><td>803</td><td>11</td><td>99</td><td>0</td><td>1</td><td></td></tr><tr><td rowspan="4"></td><td>640</td><td>5</td><td>256</td><td>160</td><td>256</td><td></td><td></td><td></td></tr><tr><td>31</td><td>0</td><td>1125</td><td></td><td>125</td><td>5</td><td>0</td><td>0</td></tr><tr><td>384 7</td><td></td><td>2816</td><td>品</td><td>768 125</td><td>66</td><td>5</td><td>5</td></tr><tr><td></td><td>0</td><td>1125 2816</td><td></td><td>品</td><td>768</td><td>0</td><td>66</td><td>66</td></tr><tr><td rowspan="2"></td><td>1408</td><td></td><td></td><td></td><td></td><td></td><td>5</td><td>5</td><td>5</td></tr><tr><td>5 66</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>66</td><td>66</td><td>66</td></tr></table>

We also present a similar method with $p ~ = ~ 7$ . This also comes from Fehlberg’s paper, subject to the correction of some minor misprints. The augmented tableau is

<table><tr><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0 0</td><td>靠</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td>0</td><td></td><td>2</td><td>云</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>25</td><td>0</td><td>0</td><td></td><td>125</td><td></td><td>125</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td></td><td>108</td><td></td><td>54</td><td>13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>31 300</td><td>0</td><td>0</td><td>0</td><td></td><td>61 225</td><td>2</td><td>900</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td></td><td>53</td><td></td><td>704</td><td>107</td><td>67</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td></td><td>0</td><td>6</td><td></td><td>45</td><td>9</td><td>90</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>91</td><td>0</td><td>0</td><td>23</td><td></td><td>976</td><td>311</td><td>19</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td>108</td><td></td><td>135</td><td>54</td><td>60</td><td>北</td><td></td><td>45</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2383</td><td>0</td><td>0</td><td>341</td><td></td><td>4496</td><td>301</td><td>2133</td><td>82</td><td>164</td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td>4100 3</td><td>0</td><td></td><td>164</td><td></td><td>1025</td><td>82 6</td><td>4100 3</td><td>3</td><td>3</td><td></td><td></td><td>0</td><td></td><td></td></tr><tr><td>0</td><td>205</td><td></td><td>0</td><td>0</td><td></td><td>0</td><td>41</td><td>205</td><td>41</td><td>41</td><td>A</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1777</td><td>0</td><td>0</td><td>341</td><td></td><td>4496</td><td>289</td><td>2193</td><td>51</td><td>33</td><td>12</td><td></td><td>0</td><td>1</td><td></td></tr><tr><td></td><td>4100 41</td><td>0</td><td></td><td>164</td><td></td><td>1025</td><td>82 34</td><td>4100 9</td><td>82 9</td><td>164 9</td><td>41 9</td><td></td><td>41</td><td>0</td><td>0</td></tr><tr><td></td><td>840</td><td></td><td>0</td><td>0</td><td></td><td>0</td><td>105 34</td><td>35 9</td><td>35 9</td><td>280 9</td><td>280 9</td><td>840</td><td></td><td>41</td><td>41</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td>0</td><td>105</td><td>35</td><td>35</td><td>280</td><td>280</td><td>0</td><td></td><td>840</td><td>840</td></tr><tr><td></td><td>41</td><td>0</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>41</td><td>41</td><td>41 840</td></tr><tr><td></td><td>840</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>840</td><td>840</td><td></td></tr></table>

The two methods presented here, along with some of the other Runge– Kutta pairs derived by Fehlberg, have been criticized for a reason associated with computational robustness. This is that the two quadrature formulae characterized by the vectors $b ^ { \intercal }$ and $\hat { b } ^ { \top }$ are identical. Hence, if the differential equation being solved is approximately equal to a pure quadrature problem, then error estimates will be too optimistic.

Although the methods were intended by Fehlberg to be used as order $p$ schemes together with asymptotically correct error estimators, such methods are commonly implemented in a slightly different way. Many numerical analysts argue that it is wasteful to propagate a low order approximation when a higher order approximation is available. This means that the method $( A , \widehat { b } ^ { \intercal } , c )$ , rather than $( A , b ^ { \prime } , c )$ , would be used to produce output values. The order $p + 1$ method will have a different stability region than that of the order $p$ method, and this needs to be taken into account. Also there is no longer an asymptotically correct error estimator available. Many practical codes have no trouble using the difference of the order $p$ and order $p + 1$ approximations to control stepsize, even though it is the higher order result that is propagated.

# 335 The methods of Verner

The methods of Verner overcome the fault inherent in many of the Fehlberg methods, that the two embedded methods both have the same underlying quadrature formula. The following method from Verner (1978) consists of a fifth order method which uses just the first six stages together with a sixth order method based on all of the eight stages. Denote the two output coefficient vectors by $b ^ { \scriptscriptstyle 1 }$ and $\widehat { b } ^ { \intercal }$ , respectively. As usual we give the difference $\widehat { b ^ { \intercal } } - b ^ { \intercal }$ which is used for error estimation purposes:

<table><tr><td rowspan="9">0 1 18 GR 1</td><td>369</td></tr><tr><td>中</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>8</td></tr><tr><td></td><td>81</td></tr><tr><td>五</td><td>56 54</td></tr><tr><td></td><td>11</td></tr><tr><td>11 7 5380 219</td><td>12285 2695</td></tr><tr><td>73 656</td><td>584 1752 52</td></tr><tr><td>8716 891 297 9</td><td>39520 416</td></tr><tr><td>8 1 3015</td><td>27 891 11 4219 5985</td></tr><tr><td>256</td><td>539 0 128 384</td></tr><tr><td>3 80</td><td>78 4 243 77 73 700</td></tr><tr><td></td><td>0</td></tr><tr><td></td><td>25 1120</td></tr><tr><td>57 640</td><td>160 16 1377 121</td></tr><tr><td></td><td>0 891</td></tr><tr><td>0 33 0 640</td><td>2240 320 8320</td></tr></table>

As for the Fehlberg methods, we have a choice as to whether we use the fifth or sixth order approximation as output for propagation purposes. Even though the sixth order choice leaves us without an asymptotically correct local error estimator, the use of this more accurate approximation has definite advantages. In Figure 335(i) the stability regions for the two approximations are plotted. It is clear that stability considerations favour the higher order method.

![](images/15da8a01811fb95f49f1d23ac0f93efbbdcc497a4af4adbf5de2e0e5b57e4f14.jpg)  
Stability regions of embedded Verner method with orders 5 and 6

# 336 The methods of Dormand and Prince

If it is accepted that in using a Runge–Kutta pair, comprising methods of orders $p$ and $p + 1$ , it is the higher order member of the pair that is going to be propagated, then it is logical to take some care over the properties of this order $p { + 1 }$ method. In the methods introduced in Dormand and Prince (1980), this point of view is adopted. The first of these method pairs, referred to by the authors as ‘RK5(4)7M’, is designed to have a low value of the 2-norm of the vector of sixth order error coefficients. This method has the tableau

<table><tr><td>0</td><td>嘉</td><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>中</td><td>44 45</td><td>40 56 15 25360</td><td>32 9 64448</td><td></td><td>212</td><td></td><td></td><td></td></tr><tr><td></td><td>19372 6561</td><td>2187</td><td>6561</td><td></td><td>729</td><td></td><td></td><td></td></tr><tr><td></td><td>9017</td><td>355</td><td>46732</td><td></td><td>49</td><td>5103</td><td></td><td></td></tr><tr><td></td><td>3168</td><td>33</td><td>5247</td><td></td><td>176</td><td>18656</td><td></td><td></td></tr><tr><td>1</td><td>35</td><td>0</td><td>500</td><td></td><td>125</td><td>2187</td><td>11</td><td></td></tr><tr><td></td><td>384</td><td></td><td>1113</td><td>192</td><td></td><td>6784</td><td>84</td><td></td></tr><tr><td></td><td>35</td><td>0</td><td>500</td><td>125</td><td></td><td>2187</td><td>11</td><td>0</td></tr><tr><td></td><td>384</td><td></td><td>1113</td><td></td><td>192</td><td>6784</td><td>84</td><td></td></tr><tr><td></td><td>5179</td><td>0</td><td>7571</td><td></td><td>393</td><td>92097</td><td>187</td><td>1</td></tr><tr><td></td><td>57600</td><td></td><td>16695</td><td></td><td>640</td><td>339200</td><td>2100</td><td>40</td></tr><tr><td></td><td>71</td><td>0</td><td>71</td><td></td><td>71</td><td>17253</td><td>22</td><td>1</td></tr><tr><td></td><td>57600</td><td></td><td></td><td></td><td>1920</td><td>339200</td><td>525</td><td>40</td></tr><tr><td></td><td></td><td></td><td>16695</td><td></td><td></td><td></td><td></td><td></td></tr></table>

It is emphasized that the first of the output approximations has order $p { + } 1 = 5$ and is the result propagated. This method, like those derived in Subsection 333, have the so-called FSAL (‘first same as last’) property in which the vector $b ^ { \scriptscriptstyle 1 }$ , corresponding to the output approximation, has its last component zero and is in fact identical to the last row of $A$ . This means that, while this particular method has seven stages, it operates as though it only had six because the evaluation of the seventh and last stage derivative can be retained to serve as the first stage derivative for the subsequent step.

An alternative choice of free parameters leads to the following method:

<table><tr><td>G 1</td><td rowspan="11"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>G</td><td></td><td>美</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>55 324</td><td></td><td>品</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td>9</td><td></td><td></td><td></td></tr><tr><td>83 330</td><td>13</td><td></td><td></td><td>110</td><td></td><td></td><td></td></tr><tr><td>19</td><td>22</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td>4</td><td></td><td>1</td><td>27</td><td>22</td><td></td><td></td></tr><tr><td>1</td><td>19</td><td>0</td><td>3</td><td>243</td><td>33</td><td>7</td><td></td></tr><tr><td rowspan="4"></td><td>200</td><td></td><td></td><td>400</td><td>40</td><td>80</td><td></td></tr><tr><td>19</td><td>0</td><td></td><td>243</td><td>33</td><td>7</td><td>0</td></tr><tr><td>200 431</td><td></td><td>333</td><td>400 7857</td><td>40 957</td><td>80 193</td><td>1</td></tr><tr><td>5000</td><td>0</td><td>500</td><td>10000</td><td>1000</td><td>2000</td><td>50</td></tr><tr><td rowspan="2"></td><td>11</td><td></td><td>33</td><td>891</td><td>33</td><td>9</td><td>1</td></tr><tr><td>1250</td><td>0</td><td>500</td><td>5000</td><td>250</td><td>1000</td><td>50</td></tr></table>

Although this has larger error constants overall (as measured by the 2-norm of the sixth order error vector), it has the advantage of a longer stability interval than that of (336a).

For comparison, a method pair with exactly six stages (but of course without the FSAL property) was also presented in the Dormand and Prince paper. This method, given by

<table><tr><td>0</td><td rowspan="16"></td><td colspan="6"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>中</td><td>广 9</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>40</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>9</td><td>6</td><td></td><td></td><td></td></tr><tr><td></td><td>10</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>226</td><td>25</td><td>880</td><td>55</td><td></td><td></td></tr><tr><td></td><td>729</td><td>27</td><td>729</td><td>729</td><td></td><td></td></tr><tr><td></td><td>181</td><td>5</td><td>266</td><td>91</td><td>189</td><td></td></tr><tr><td></td><td>270</td><td></td><td>297</td><td>27</td><td>55</td><td></td></tr><tr><td></td><td>19</td><td>0</td><td>1000</td><td>125</td><td>81</td><td>5</td></tr><tr><td></td><td>216</td><td></td><td>2079</td><td>216</td><td>88</td><td>56</td></tr><tr><td></td><td>31</td><td>0</td><td>190</td><td>145</td><td>351</td><td>1</td></tr><tr><td></td><td>540</td><td></td><td>297</td><td>108</td><td>220</td><td>20</td></tr><tr><td></td><td>11</td><td>0</td><td>10</td><td>55</td><td>27</td><td>11</td></tr><tr><td></td><td>360</td><td></td><td>63</td><td>72</td><td>40</td><td>280</td></tr></table>

seems to be less efficient than the FSAL method.

In the derivation of these method pairs, some attention is devoted to the properties of the approximation which is not propagated. In particular, care is taken to ensure that this approximation has an acceptable stability region. In any implementation of these methods, $\widehat { b } ^ { \intercal }$ does not play a direct role because stepsize is controlled using the vector of coefficients $\boldsymbol { d } ^ { \intercal } = \widetilde { \boldsymbol { b } } ^ { \intercal } - \boldsymbol { b } ^ { \intercal }$ . Rescaling this vector by a non-zero factor is then equivalent to rescaling the userimposed tolerance. From this point of view, the restriction of methods to those for which the non-propagated approximation has good stability properties is unnecessary.

# Exercises 33

33.1 To overcome the perceived disadvantage of using Richardson extrapolation as in Subsection 331, is it feasible to modify the method so that a proportion of the estimated error (331c) is subtracted from the result ${ \hat { y } } _ { n }$ ?   
33.2 Find a problem for which the Merson method gives reasonable error estimating performance.   
33.3 Find a problem which exposes the error estimating deficiencies of the Merson method.   
33.4 Find a method of order 3 embedded in order 4, based on equations (333h)–(333k) with $\begin{array} { r } { B = \frac { 1 } { 6 } } \end{array}$ , $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 3 } = \frac { 1 } { 3 } } \end{array}$ .   
33.5 Find an example of a differential equation system for which the methods given in Subsection 334 are likely to have misleading error estimates.

# 34 Implicit Runge–Kutta Methods

# 340 Introduction

The possibility that the coefficient matrix $A$ in a Runge–Kutta method might not be strictly lower triangular has very important consequences. These more general methods, known as ‘implicit Runge–Kutta methods’, are difficult to actually use, because the explicit stage-by-stage implementation scheme enjoyed by explicit methods is no longer available and needs to be replaced by an iterative computation. However, there are several very good reasons, both theoretical and practical, for moving these methods into the centre of our attention. Perhaps the most important theoretical reason for regarding implicit methods as the standard examples of Runge–Kutta methods is the fact that implicit methods have a group structure. We explore this in detail in Section 38. In the explicit case, methods do not have explicit methods as inverses, and thus explicit methods possess only a semi-group structure. Stiff problems cannot be solved efficiently using explicit methods: this fact is the most important practical reason for paying special attention to implicit methods. However, there are other problem classes, such as differentialalgebraic equations, for which implicit Runge–Kutta methods also have a vital role.

# 341 Solvability of implicit equations

As we have remarked, explicit evaluation of the stages is not, in general, possible for an implicit Runge–Kutta method. However, under mild assumptions on the smoothness of the function $f$ it is easy to see that, for sufficiently small $h$ , the values of $Y _ { 1 }$ , $Y _ { 2 }$ , $\cdot \cdot \cdot$ , $Y _ { s }$ , and hence the output from a step, exist and are unique. Suppose that $f$ satisfies a Lipschitz condition

$$
\| f ( \eta ) - f ( \overline { { \eta } } ) \| \leq L \| \eta - \overline { { \eta } } \|
$$

and consider the stages in a step with size $h$ from initial value $y _ { 0 }$ . We can identify the values of $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , as comprising the components of a vector in $\mathbb { R } ^ { s N }$ which is a fixed point of the mapping

$$
Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] \mapsto \phi ( Y ) = \left[ \begin{array} { c } { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 1 i } f ( Y _ { i } ) } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 2 i } f ( Y _ { i } ) } \\ { \vdots } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { s i } f ( Y _ { i } ) } \end{array} \right] .
$$

Define a metric on $\mathbb { R } ^ { s N }$ by the formula

$$
\rho ( Y , \overline { { Y } } ) = \operatorname* { m a x } _ { i = 1 } ^ { s } \| Y _ { i } - \overline { { Y } } _ { i } \| ,
$$

and estimate $\rho ( \phi ( Y ) , \phi ( { \overline { { Y } } } ) )$ as follows:

$$
\begin{array} { r l } { \displaystyle \rho ( \phi ( Y ) , \phi ( \overline { { Y } } ) ) = \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \parallel \underset { j = 1 } { \overset { s } { \sum } } h a _ { i j } \parallel f ( Y _ { j } ) - \overline { { f } } ( Y _ { j } ) \parallel } & { } \\ { \displaystyle \leq | h | \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \sum _ { j = 1 } ^ { s } | a _ { i j } | L \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \underset { j = 1 } { \overset { s } { \operatorname* { m a x } } } \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \rho ( Y , \overline { { Y } } ) , } \end{array}
$$

so that the conditions for the contraction mapping principle are satisfied as long as

$$
| h | \leq ( L \| A \| _ { \infty } ) ^ { - 1 } .
$$

In practice, this result is of little value, because implicit Runge–Kutta methods are usually used only for stiff problems for which $L$ is typically unreasonably large. In this case it is usually more efficient to use some variant of the Newton method. We discuss this question further in Subsection 360.

# 342 Methods based on Gaussian quadrature

We recall the Legendre polynomials on the interval $[ 0 , 1 ]$

$$
\begin{array} { l } { { P _ { 0 } ^ { * } ( x ) = 1 , } } \\ { { P _ { 1 } ^ { * } ( x ) = 2 x - 1 , } } \\ { { P _ { 2 } ^ { * } ( x ) = 6 x ^ { 2 } - 6 x + 1 , } } \\ { { P _ { 3 } ^ { * } ( x ) = 2 0 x ^ { 3 } - 3 0 x ^ { 2 } + 1 2 x - 1 , } } \\ { { \ } } \\ { { \vdots \ } } \end{array}
$$

where we use the notation $P _ { n } ^ { * }$ for the member of the sequence with degree $n$ . Note that $P _ { n } ^ { * }$ is related to $P _ { n }$ , the Legendre polynomials on the standard symmetric interval $[ - 1 , 1 ]$ , by $P _ { n } ^ { * } ( x ) = P _ { n } ( 2 x - 1 )$ . Amongst the rich collection of properties of this polynomial sequence, we state:

Lemma 342A There exist polynomials $P _ { n } ^ { * } : | 0 , 1 | \to \mathbb { R }$ , of degrees $n$ , for $n = 0 , 1 , 2 , \ldots$ with the properties that

$$
\begin{array} { c } { { \displaystyle { \int _ { 0 } ^ { 1 } P _ { m } ^ { * } ( x ) P _ { n } ^ { * } ( x ) d x = 0 , \qquad m \neq n , } } } \\ { { \displaystyle { P _ { n } ^ { * } ( 1 ) = 1 , \qquad n = 0 , 1 , 2 , \ldots . } } } \end{array}
$$

Furthermore, the polynomials defined by (342a) and (342b) have the following additional properties:

$$
\begin{array} { l } { { P _ { n } ^ { * } ( 1 - x ) = ( - 1 ) ^ { n } P _ { n } ^ { * } ( x ) , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } P _ { n } ^ { * } ( x ) ^ { 2 } d x = \frac { 1 } { 2 n + 1 } , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle P _ { n } ^ { * } ( x ) = \frac { 1 } { n ! } \left( \frac { d } { d x } \right) ^ { n } ( x ^ { 2 } - x ) ^ { n } , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle n P _ { n } ^ { * } ( x ) = ( 2 x - 1 ) ( 2 n - 1 ) P _ { n - 1 } ^ { * } ( x ) - ( n - 1 ) P _ { n - 2 } ^ { * } ( x ) , ~ n = 2 , 3 , 4 , \dots , } } \end{array}
$$

$P _ { n } ^ { * }$ has n distinct real zeros in the interval $( 0 , 1 ) , \quad n { = } 0 , 1 , 2 , \ldots .$

Proof. We give only outline proofs of these well-known results. The orthogonality property (342a), of the polynomials defined by (342e), follows by repeated integration by parts. The value at $x = 1$ follows by substituting $x = 1 + \xi$ in (342e) and evaluating the coefficient of the lowest degree term. The fact that $P _ { n } ^ { * }$ is an even or odd polynomial in $2 x - 1$ , as stated in (342c), follows from (342e). The highest degree coefficients in $P _ { n } ^ { * }$ and $P _ { n - 1 } ^ { * }$ can be compared so that $n P _ { n } ^ { * } ( x ) - ( 2 x - 1 ) ( 2 n - 1 ) P _ { n - 1 } ^ { * } ( x )$ is a polynomial, $Q$ say, of degree less than $n$ . Because $Q$ has the same parity as $n$ , it is of degree less than $n - 1$ . A simple calculation shows that $Q$ is orthogonal to $P _ { k } ^ { * }$ for $k < n - 2$ . Hence, (342f) follows except for the value of the $P _ { n - 2 } ^ { * }$ coefficient, which is resolved by substituting $x = 1$ . The final result (342g) is proved by supposing, on the contrary, that $P _ { n } ^ { * } ( x ) = Q ( x ) R ( x )$ , where the polynomial factors $Q$ and $R$ have degrees $m < n$ and $n - m$ , respectively, and where $R$ has no zeros in $( 0 , 1 )$ . We now find that $\begin{array} { r } { \int _ { 0 } ^ { 1 } P _ { n } ^ { * } ( x ) Q ( x ) d x = 0 } \end{array}$ , even though the integrand is not zero and has a constant sign. 

In preparation for constructing a Runge–Kutta method based on the zeros $c _ { i }$ , $i = 1 , 2 , \dots , s$ of $P _ { s } ^ { * }$ , we look at the associated quadrature formula.

Lemma 342B Let $c _ { 1 }$ , $c _ { 2 } , . . .$ denote the zeros of $P _ { s } ^ { * }$ . Then there exist positive numbers $b _ { 1 }$ , $b _ { 2 }$ , . . . , $b _ { s }$ such that

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) ,
$$

for any polynomial of degree less than $2 s$ . The $b _ { i }$ are unique.

Proof. Choose $b _ { i }$ , $i = 1 , 2 , \dots , s$ , so that (342h) holds for any $\phi$ of degree less than $s$ . Because the $c _ { i }$ are distinct the choice of the $b _ { i }$ is unique. To prove that (342h) holds for degree up to $2 s - 1$ , write

$$
\phi ( x ) = P _ { s } ^ { * } ( x ) Q ( x ) + R ( x ) ,
$$

where the quotient $Q$ and the remainder $R$ have degrees not exceeding $s - 1$ . We now have

$$
\begin{array} { l } { \displaystyle ^ { \int ^ { 1 } } \phi ( x ) d x = \int _ { 0 } ^ { 1 } P _ { s } ^ { * } ( x ) Q ( x ) d x + \int _ { 0 } ^ { 1 } R ( x ) d x = 0 + \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } R ( c _ { i } ) = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) . } \end{array}
$$

To prove the $b _ { i }$ are positive, let $\phi ( x )$ denote the square of the polynomial formed by dividing $P _ { s } ^ { * } ( x )$ by $x - c _ { i }$ . Substitute into (342h), and the result follows. 

We note that the choice of the $c _ { i }$ as the zeros of $P _ { s } ^ { * }$ is the only one possible for (342h) to hold for $\phi$ of degree as high as $2 s - 1$ . If this were not the case, let

$$
S ( x ) = \prod _ { i = 1 } ^ { s } ( x - c _ { i } )
$$

and substitute $\phi ( x ) = S ( x ) Q ( x )$ for any polynomial $Q$ of degree less than $s$ . It is found that $S$ is orthogonal to all polynomials of lower degree and hence, apart from a scale factor, is identical to $P _ { s } ^ { * }$ .

We now consider the possibility of constructing an $s$ -stage implicit Runge– Kutta method with order $2 s$ . If such a method exists, then the values of the

vectors $c$ and $b ^ { \prime }$ are known. In the case $s = 2$ we can explore the possibility of choosing the only free parameters that remain, to satisfy four additional order conditions. Surprisingly, this can be done. Write the tableau in the form

$$
{ \frac { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } } { \frac { 1 } { 2 } + { \frac { \sqrt { 3 } } { 6 } } } } \left| { \begin{array} { c c } { a _ { 1 1 } } & { { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } - a _ { 1 1 } } } \\ { { { \frac { 1 } { 2 } } + { \frac { \sqrt { 3 } } { 6 } } - a _ { 2 2 } } } & { a _ { 2 2 } } \\ { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 2 } } } } \end{array} } \right.  .
$$

For the trees $\bullet , \mathtt { l } , \mathtt { V } , \Psi$ , the order conditions are satisfied. These are just the $B ( 4 )$ conditions introduced in Subsection 321. The remaining trees and the conditions that result from substituting the values from (342i) and simplifying are:

$$
\begin{array} { r l r } { \updownarrow } & { } & { a _ { 1 1 } = a _ { 2 2 } , } \\ { \Updownarrow } & { } & { ( 1 - \sqrt { 3 } ) a _ { 1 1 } + ( 1 + \sqrt { 3 } ) a _ { 2 2 } = \frac { 1 } { 2 } , } \\ { \updownarrow } & { } & { a _ { 1 1 } = a _ { 2 2 } , } \\ { \updownarrow } & { } & { ( 1 + \sqrt { 3 } ) a _ { 1 1 } + ( 1 - \sqrt { 3 } ) a _ { 2 2 } + 2 \sqrt { 3 } ( a _ { 1 1 } ^ { 2 } - a _ { 2 2 } ^ { 2 } ) = \frac { 1 } { 2 } . } \end{array}
$$

These are all satisfied by $\begin{array} { r } { a _ { 1 1 } = a _ { 2 2 } = \frac { 1 } { 4 } } \end{array}$

We also notice that $C ( 2 )$ and $D ( 2 )$ are satisfied by these values, and it is natural to ask if it is possible, in general, to satisfy both $C ( s )$ and $D ( s )$ assuming that the $b ^ { \intercal }$ and $c$ vectors have been chosen to satisfy the quadrature conditions. A crucial link in the chain connecting these conditions is $E ( s , s )$ , given by (321c), and we present a result which expresses the essential connections between them. It will be convenient to write $G ( \eta )$ to represent the fact that a given Runge–Kutta method has order $\eta$ .

# Theorem 342C

$$
\begin{array} { r l r } & { } & { G ( 2 s ) \Rightarrow B ( 2 s ) , } \\ & { } & { G ( 2 s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge C ( s ) \wedge D ( s ) \Rightarrow G ( 2 s ) , } \\ & { } & { B ( 2 s ) \wedge C ( s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge E ( s , s ) \Rightarrow C ( s ) , } \\ & { } & { B ( 2 s ) \wedge D ( s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge E ( s , s ) \Rightarrow D ( s ) . } \end{array}
$$

Proof. The first two results (342j), (342k) are consequences of the order conditions. Given that $C ( s )$ is true, all order conditions based on trees containing the structure $\cdots \left[ \tau ^ { k - 1 } \right] \cdot \cdot \cdot$ , with $k \leq s$ , can be removed, as we saw in Subsection 321. Similarly, the condition $D ( s )$ enables us to remove from consideration all trees of the form $[ \tau ^ { k - 1 } [ \cdot \cdot \cdot ] ]$ . Hence, if both $C ( s )$ and $D ( s )$ are true, the only trees remaining are those associated with the trees covered by $B ( 2 s )$ . Hence, (342l) follows. Multiply the matrix of quantities that must be zero according to the $C ( s )$ condition

![](images/71923baf9d87d0db6b0f710dce5d05a07efdb04f42f6b951c4912ea7d5042abd.jpg)  
Schema representing Theorem 342C

$$
{ \left[ \begin{array} { l l l l } { \sum _ { j } a _ { 1 j } - c _ { 1 } } & { \sum _ { j } a _ { 1 j } c _ { j } - { \frac { 1 } { 2 } } c _ { 1 } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { 1 j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { 1 } ^ { s } } \\ { \sum _ { j } a _ { 2 j } - c _ { 2 } } & { \sum _ { j } a _ { 2 j } c _ { j } - { \frac { 1 } { 2 } } c _ { 2 } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { 2 j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { 2 } ^ { s } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \sum _ { j } a _ { s j } - c _ { s } } & { \sum _ { j } a _ { s j } c _ { j } - { \frac { 1 } { 2 } } c _ { s } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { s j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { s } ^ { s } } \end{array} \right] }
$$

by the non-singular matrix

$$
\left[ \begin{array} { c c c c } { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \\ { b _ { 1 } c _ { 1 } } & { b _ { 2 } c _ { 2 } } & { \cdots } & { b _ { s } c _ { s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { b _ { 1 } c _ { 1 } ^ { s - 1 } } & { b _ { 2 } c _ { 2 } ^ { s - 1 } } & { \cdots } & { b _ { s } c _ { s } ^ { s - 1 } } \end{array} \right]
$$

and the result is the matrix of $E ( s , s )$ conditions. Hence, (342m) follows and, because the matrix multiplier is non-singular, (342n) also follows. The final results (342o) and (342p) are proved in similar way. 

A schema summarizing Theorem 342C is shown in Figure 342(i). To turn this result into a recipe for constructing methods of order $2 s$ we have:

Corollary 342D A Runge–Kutta method has order $2 s$ if and only if its coefficients are chosen as follows:

(i) Choose $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ as the zeros of $P _ { s } ^ { * }$ .   
(ii) Choose $b _ { 1 }$ , $b _ { 2 }$ , . . . , $b _ { s }$ to satisfy the $B ( s )$ condition.   
(iii) Choose $a _ { i j }$ , $i , j = 1 , 2 , \dots , s$ , to satisfy the $C ( s )$ condition.

Proof. If the method has order $2 s$ then $B ( 2 s )$ is satisfied. This implies (i) and (ii). Because the order is $2 s$ , $E ( s , s )$ is satisfied and this, together with $B ( 2 s )$ , implies (iii). Conversely, if (i) and (ii) are satisfied, then $B ( 2 s )$ holds and this in turn implies $E ( s , s )$ . This fact, together with $B ( 2 s )$ , implies $D ( s )$ . Finally, use (342l) to complete the proof. 

We conclude this introduction to the Gauss methods by listing the tableaux for $s = 1 , 2 , 3$ and orders $2 , 4 , 6$ , respectively:

$$
s = 1 , \quad p = 2 ,
$$

$$
{ \frac { { \frac { 1 } { 2 } } \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { 1 } } \end{array} \right. } ; }
$$

$$
s = 2 , \quad p = 4 , 
$$

$s = 3 , \quad p = 6 ,$

# 343 Reflected methods

Given a Runge–Kutta method,

$$
{ \begin{array} { r } { c _ { 1 } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { \rule { 0 ex } { 1. 5 ex } } \\ { b _ { 1 } } \end{array} } { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| }
$$

we construct a method which exactly undoes the work of the given method. If the signs of the coefficients are then all reversed, the resulting method is known as the ‘reflection’ (Scherer, 1977, 1978) of the original method. Because the exact solution is its own reflection, it is natural to consider whether Runge–Kutta methods that have this property have any advantage over other methods. In particular, the Gauss methods are their own reflections, as we will see. Reflected methods are now commonly known as ‘adjoint methods’; for references to modern applications and research, see Hairer, Lubich and Wanner (2006).

For method (343a), the stages and the final output at the end of step $n$ are given by

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ) , \quad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } b _ { j } f ( Y _ { j } ) . } } \end{array}
$$

Subtract (343c) from (343b) so that the stage values are written in terms of the result found at the end of the step. Also rearrange (343c) so that it gives $y _ { n - 1 }$ in terms of $y _ { n }$ . Thus, the result that works in the reverse direction is given by the equations

$$
\begin{array} { c } { { Y _ { i } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) f ( Y _ { j } ) , \quad i = 1 , 2 , \ldots , s , } } \\ { { } } \\ { { y _ { n - 1 } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } ( - b _ { j } ) f ( Y _ { j } ) . } } \end{array}
$$

This reversed method has tableau

$$
\begin{array} { c } { { c _ { 1 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { c _ { 2 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { c _ { s } - \sum _ { j = 1 } ^ { s } b _ { j } \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { 1 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 1 s } - b _ { s } } } \\ { { a _ { 2 1 } - b _ { 1 } } } & { { a _ { 2 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 2 s } - b _ { s } } } \end{array} \right| } } \\ { { - b _ { 1 } \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad } } \\ { { \frac { c _ { s } - \sum _ { j = 1 } ^ { s } b _ { j } } { - b _ { 1 } } \left| \begin{array} { c c c c c } { { a _ { s 1 } - b _ { 1 } } } & { { a _ { s 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { s s } - b _ { s } } } \\ { { - b _ { 1 } } } & { { - b _ { 2 } } } & { { \cdots } } & { { - b _ { s } } } \end{array} \right| } . } \end{array}
$$

Reverse the signs and we have the tableau for the reflection of (343a)

$$
\begin{array} { r } { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { 1 } } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { 2 } } \\ { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { s } } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { s } } \end{array}
$$

It is easy to verify the following result, which we present without proof.

Theorem 343A The reflection of the reflection of a Runge–Kutta method is the original method.

If a method satisfies some of the simplifying assumptions introduced in Subsection 321, then we consider the possibility that the reflection of the method satisfies corresponding conditions. To enable us to express these connections conveniently, we write $\widetilde { B } ( \eta )$ , $\bar { C } ( \eta )$ , $\widetilde { D } ( \eta )$ and $\widetilde { E } ( \eta , \zeta )$ to represent $B ( \eta )$ , $C ( \eta )$ , $D ( \eta )$ and $E ( \eta , \zeta )$ , respectively, but with reference to the reflected method. We then have:

Theorem 343B If $\eta$ and $\zeta$ are positive integers, then

$$
\begin{array} { r l r } & { } & { B ( \eta ) \Rightarrow \widetilde { B } ( \eta ) , } \\ & { } & { B ( \eta ) \wedge C ( \eta ) \Rightarrow \widetilde { C } ( \eta ) , } \\ & { } & { B ( \eta ) \wedge D ( \eta ) \Rightarrow \widetilde { D } ( \eta ) , } \\ & { } & { B ( \eta + \zeta ) \wedge E ( \eta , \zeta ) \Rightarrow \widetilde { E } ( \eta , \zeta ) . } \end{array}
$$

Proof. Let $P$ and $Q$ be arbitrary polynomials of degrees less than and $\eta$ less than $\zeta$ , respectively. By using the standard polynomial basis, we see that $B ( \eta ) , C ( \eta ) , D ( \eta )$ and $E ( \eta , \zeta )$ are equivalent respectively to the statements

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } P ( c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) d x , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } P ( c _ { j } ) = \int _ { 0 } ^ { c _ { i } } P ( x ) d x , \quad \quad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P ( c _ { i } ) a _ { i j } = b _ { j } \int _ { c _ { j } } ^ { 1 } P ( x ) d x , \quad \quad j = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } P ( c _ { i } ) a _ { i j } Q ( c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { 0 } ^ { x } Q ( x ) d x \right) d x . } } \end{array}
$$

In each part of the result $B ( \eta )$ holds with $\eta \geq 1$ , and hence we can assume that $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } = 1$ . Hence the reflected tableau can be assumed to be

$$
\begin{array} { r } { { 1 } - c _ { 1 } \left| \begin{array} { c c c c } { b _ { 1 } - a _ { 1 1 } } & { b _ { 2 } - a _ { 1 2 } } & { \cdots } & { b _ { s } - a _ { 1 s } } \\ { 1 - c _ { 2 } } \end{array} \right| } \\ { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad } & { \vdots \qquad } \\ { { 1 } - c _ { s } \left| \begin{array} { c c c c } { b _ { 1 } - a _ { 1 1 } } & { b _ { 2 } - a _ { 1 2 } } & { \cdots } & { b _ { s } - a _ { s s } } \\ { b _ { 1 } - a _ { 2 1 } } & { b _ { 2 } - a _ { 2 2 } } & { \cdots } & { b _ { s } - a _ { 2 s } } \end{array} \right| } \\ { \qquad \quad \textmd { b } _ { 1 } \qquad \textmd { b } _ { 2 } \qquad \textcsc \qquad \textmu _ { s } } \end{array} .
$$

To prove (343d) we have, using (343h),

$$
\sum _ { j = 1 } ^ { s } b _ { j } P ( 1 - c _ { j } ) = \int _ { 0 } ^ { 1 } P ( 1 - x ) d x = \int _ { 0 } ^ { 1 } P ( x ) d x .
$$

To prove (343e) we use (343i) to obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } ( b _ { j } - a _ { i j } ) P ( 1 - c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 0 } ^ { c _ { i } } P ( 1 - x ) d x } } \\ { ~ } \\ { { \displaystyle ~ = \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 1 - c _ { i } } ^ { 1 } P ( x ) d x } } \\ { { \displaystyle ~ = \int _ { 0 } ^ { 1 - c _ { i } } P ( x ) d x . } } \end{array}
$$

Similarly, we prove (343f) using (343j):

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P ( 1 - c _ { i } ) ( b _ { j } - a _ { i j } ) = b _ { j } \int _ { 0 } ^ { 1 } P ( x ) d x - b _ { j } \int _ { c _ { j } } ^ { 1 } P ( 1 - x ) d x } } \\ { { \displaystyle \qquad = b _ { j } \left( \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 0 } ^ { 1 - c _ { j } } P ( x ) d x \right) } } \\ { { \displaystyle \qquad = b _ { j } \int _ { 1 - c _ { j } } ^ { 1 } P ( x ) d x . } } \end{array}
$$

Finally, use (343k) to prove (343g):

$$
\begin{array} { l } { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } P ( 1 - c _ { i } ) ( b _ { j } - a _ { i j } ) Q ( 1 - c _ { j } ) } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( 1 - x ) \left( \int _ { 0 } ^ { x } Q ( 1 - x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( 1 - x ) \left( \int _ { 1 - x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { x } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { 0 } ^ { x } Q ( x ) d x \right) d x . } \end{array}
$$

# 344 Methods based on Radau and Lobatto quadrature

It will be shown in Subsection 353 that the Gauss methods have stability regions equal to exactly the left half-plane, and they are therefore A-stable.

For many stiff problems, it is desirable to sacrifice order to gain L-stability, so that the stability function satisfies the property $\begin{array} { r } { \operatorname* { l i m } _ { | z | \to \infty } | R ( z ) | = 0 } \end{array}$ . We explore methods based on quadrature formulae of orders $2 s - 1$ or $2 s \textrm { -- } 2$ . Instead of choosing $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ to obtain as high a degree as possible for polynomials $\phi$ such that

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) ,
$$

we choose either (i) $c _ { 1 } = 0$ , (ii) ${ c _ { s } = 1 }$ or (iii) $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ . The remaining unspecified $c _ { i }$ are then chosen to make (344a) true for a polynomial of degree as high as is still possible.

A ‘Radau I quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ ; a ‘Radau II quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and a ‘Lobatto quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ . Note that ‘Lobatto’ is sometimes referred to as ‘Lobatto III’, to bring the naming of these formulae into a consistent pattern. These three quadrature formulae are the ones sought. We have:

Theorem 344A Let $c _ { 1 } < c _ { 2 } < \cdots < c _ { s }$ be chosen as abscissae of the Radau   
I, the Radau II or the Lobatto quadrature formula, respectively. Then: I For the Radau $I$ formula, $c _ { 1 } = 0$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
II For the Radau II formula, ${ c _ { s } = 1 }$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
III For the Lobatto formula, $c _ { 1 } ~ = ~ 0 , c _ { s } ~ = ~ 1$ . This formula is exact for polynomials of degree up to $2 s - 3$ .   
Furthermore, for each of the three quadrature formulae, $c _ { i } ~ \in ~ [ 0 , 1 ]$ , for   
$i = 1 , 2 , \dots , s$ , and $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ .

Proof. The fact that $x = 1$ is a zero of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b). The fact that $x = 0$ is a zero of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b) and (342c), with $x = 1$ . Let $\phi$ denote an arbitrary polynomial of degree not exceeding $2 s - 2$ in the Radau cases or $2 s - 3$ in the Lobatto case. Divide this by the polynomial satisfied by the abscissae and write $Q$ for the quotient and $R$ for the remainder. We have in the three cases,

$$
\begin{array} { r l r l } & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { L o b a t t o ~ c a s e } . } \end{array}
$$

Methods in the Radau and Lobatto families   

<table><tr><td>Name</td><td>Choice of b&#x27;and c</td><td>Choice of A</td></tr><tr><td>Radau I</td><td>Radau I quadrature</td><td>C(s)</td></tr><tr><td>Radau IA</td><td>Radau I quadrature</td><td>Thereflections of Radau II</td></tr><tr><td>Radau II</td><td>Radau II quadrature</td><td>D(s)</td></tr><tr><td>Radau IA</td><td>Radau II quadrature</td><td>The reflections of Radau I</td></tr><tr><td>Lobatto III</td><td>Lobatto quadrature</td><td>C(s-1)，a1s = a2s=..=αss =0</td></tr><tr><td>Lobatto IIIA</td><td>Lobatto quadrature</td><td>C(s)</td></tr><tr><td>Lobatto IIIB</td><td>Lobatto quadrature</td><td>D(s)</td></tr><tr><td>Lobatto IIIC</td><td>Lobatto quadrature</td><td>Thereflections ofLobatto III</td></tr></table>

Evaluate the approximate integral of $\phi$ written in this form, and the terms involving $Q$ are zero because of orthogonality, and the terms involving $R$ are exact because of the interpolational nature of the quadrature.

In the Radau cases, to prove that the abscissae are always in $\lfloor 0 , 1 \rfloor$ and that the weights are positive, use a homotopy $t \mapsto P _ { s } ^ { * } \pm t P _ { s - 1 } ^ { * }$ , where the upper sign is used for Radau I and the lower sign for Radau II. If any of the weights becomes zero, then for this value of $t$ , the quadrature formula has a greater order than is possible. Furthermore, no abscissae can move outside $[ 0 , 1 ]$ , until $t$ reaches a value $t = 1$ . The proof is slightly more complicated in the Lobatto case, where we use the homotopy $t \mapsto P _ { s } ^ { * } - t P _ { s - 2 } ^ { * }$ . Because of the symmetry of the quadrature formula for all $t$ , $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ both occur at the same time and this is when $t = 1$ . If a weight passes through zero, then we again obtain a contradiction to the optimality of Gaussian quadrature because two weights vanish simultaneously. The one case not covered by this argument is when $s$ is odd and the weight corresponding to $\begin{array} { r } { c _ { ( s + 1 ) / 2 } = \frac { 1 } { 2 } } \end{array}$ vanishes. However, it is impossible that as $t$ moves from 0 to $1$ , it passes through a point for which this happens because in this case the remaining abscissae would have to be the zeros of $P _ { s - 1 } ^ { * }$ . By (342f), this occurs only for $t = - ( n - 1 ) / n$ , and this has the wrong sign. 

Given the choice of $c$ and $b ^ { \top }$ in accordance with the requirements of Radau I, Radau II or Lobatto quadrature, the choice of $A$ to yield a Runge–Kutta of the same order as for the underlying quadrature formula remains. The most obvious choice, of making the methods as close to explicit as possible, is inappropriate for stiff problems, but makes the method more efficient for nonstiff problems. Other choices can be made in terms of the $C$ and $D$ conditions, and in terms of specific choices of specific elements of $A$ . To distinguish these from the simple (closest to explicit) choices, a letter A, B or C is added to the designation for the method. A summary of many of the methods in the Radau and Lobatto families is given in Table 344(I).

Selected examples of these methods are as follows, where we note that Lobatto IIIB with $s = 2$ does not exist:

$$
\mathrm { R a d a u } \mathrm { ~ I ~ } \qquad ( s = 2 , p = 3 ) ,
$$

![](images/f203af32647fc4e925753f71395de816b9168e09faaa76f5c879fb36d1348986.jpg)

Radau IA ( $s = 2 , p = 3$ ),

Radau II ( $s = 2 , p = 3$ ),

$$
\begin{array} { r } { { \frac { 1 } { 3 } } ~ { \left| \begin{array} { l l } { { \frac { 1 } { 3 } } } & { 0 } \\ { 1 } & { 0 } \end{array} \right| } } \\ { { \frac { 1 } { 4 } } ~ { \frac { 1 } { 4 } } } \end{array}
$$

Radau IIA ( $s = 2 , p = 3$ ),

![](images/d49b79b2c9447690cb0534a32535b4ff31a050cc9cac856b6b52e17a882190ca.jpg)

Radau I ( $s = 3 , p = 5$ ),

Radau IA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">0 6-√6 10</td><td rowspan="2">1 G</td><td rowspan="2">-1-√6 18 88+7√6 360</td><td>-1+√6 18</td></tr><tr><td>88-43√6 360</td></tr><tr><td>6+√6 10</td><td></td><td>88+43√6 360</td><td>88-7√6</td></tr><tr><td></td><td></td><td>16+√6</td><td>360</td></tr><tr><td></td><td>1</td><td>36</td><td>16-√6 36</td></tr></table>

$$
\mathrm { R a d a u \ I I } \qquad ( s = 3 , p = 5 ) ,
$$

<table><tr><td>4-√6 10 4+V6</td><td>24-√6 120 24+11√6</td><td>24-11√6 120 24+√6</td><td>0</td></tr><tr><td>10 1</td><td>120 6-√6</td><td>120 6+√6</td><td>0 0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td></td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td></td></tr></table>

Radau IIA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">4-√6 10 4+√6 10</td><td rowspan="2">88-7√6 360 296+169√6 1800 16-√6</td><td>296-169√6 1800</td><td>-2+3√6 225</td></tr><tr><td>88+7√6 360</td><td>-2-3√6 225</td></tr><tr><td rowspan="2">1</td><td>36</td><td>16+√6 36</td><td>1</td></tr><tr><td>16-√6 36</td><td>16+√6 36</td><td>1</td></tr></table>

Lobatto III ( $s = 2 , p = 2$ ),

<table><tr><td>0 1</td><td>0 0 1 0</td></tr><tr><td></td><td>1 1</td></tr></table>

Lobatto IIIA ( $s = 2 , p = 2$ ),

![](images/786cc1641957243644dabdad9f5e83e2ec1595e38cc7239060923684af77638e.jpg)

Lobatto IIIC ( $s = 2 , p = 2$ ),

![](images/345a7d6c870c6a20ef53fef71a5c1d598e76aefe70ff84b3724613edd711806c.jpg)

$$
\mathrm { L o b a t t o ~ I I I } \qquad ( s = 3 , p = 4 ) ,
$$

<table><tr><td></td><td>0 0</td><td>0</td></tr><tr><td>0</td><td>4 4 0 1</td><td>0 0</td></tr><tr><td></td><td>1 2</td><td>1</td></tr></table>

Lobatto IIIA ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>0 </td></tr><tr><td></td><td>D</td></tr><tr><td></td><td></td></tr><tr><td></td><td>1</td></tr></table>

Lobatto IIIB ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>G</td><td>N 0 0</td></tr><tr><td></td><td>1</td><td>0 1</td></tr></table>

Lobatto IIIC ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>GU</td><td>美</td><td>广</td></tr><tr><td rowspan="3"></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

Lobatto III ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td>0 5+√5 60</td><td>0 </td><td>0 15-7√5 60</td><td>0 0</td></tr><tr><td rowspan="3">5+√5 10 1</td><td>5-5 60</td><td>15+7√5 60</td><td>1</td><td>0</td></tr><tr><td>1</td><td>5-5</td><td>5+√5</td><td>0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td rowspan="3"></td><td>1</td><td>品</td><td>品</td><td>1 12</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

Lobatto IIIA ( $s = 4 , p = 6$ ),

<table><tr><td rowspan="2">0 5-√5 10</td><td rowspan="2">0 11+√5 120</td><td>0</td><td>0</td><td>0</td></tr><tr><td>25-√5 120</td><td>25-13√5 120</td><td>-1+√5 120</td></tr><tr><td>5+√5 10</td><td>11-√5 120</td><td>25+13√5 120</td><td>25+√5 120</td><td>-1-√5 120</td></tr><tr><td rowspan="2">1</td><td>1 12</td><td>5 12</td><td>5 12</td><td>1</td></tr><tr><td>12</td><td>5 12</td><td>品</td><td>12 1 12</td></tr></table>

Lobatto IIIB ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td></td><td>-1-√5 24 25+√5 120</td><td>-1+√5 24 25-13√5 120</td><td>0 0</td></tr><tr><td>5+√5 10</td><td></td><td>25+13√5 120 11-√5</td><td>25-√5 120 11+√5</td><td>0</td></tr><tr><td>1</td><td></td><td>120</td><td>120</td><td>0</td></tr><tr><td></td><td>1</td><td>5</td><td>5 12</td><td>1 12</td></tr><tr><td></td><td>12</td><td>12</td><td></td><td></td></tr></table>

Lobatto IIIC ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10 5+√5 10 1</td><td>中</td><td>长 12 4 10+7√5 60 5 12 5</td><td>60 1 12 5</td><td></td></tr></table>

Lobatto III

<table><tr><td>(s=5,p=8), 0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7-√21</td><td>立前</td><td></td><td>13-3√21</td><td>14-3√21</td><td></td></tr><tr><td>14</td><td></td><td>1</td><td>63</td><td>126</td><td>0</td></tr><tr><td>1</td><td></td><td>91+21√21</td><td>美</td><td>91-21V21</td><td>0</td></tr><tr><td></td><td></td><td>576</td><td>13+3V21</td><td>576</td><td></td></tr><tr><td>7+√21</td><td>1 14</td><td>14+3√21</td><td>63</td><td></td><td>0</td></tr><tr><td>14</td><td></td><td>126 7</td><td></td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>18</td><td>2</td><td>18</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td>49</td><td>16</td><td>49</td><td>1</td></tr><tr><td>20</td><td>180</td><td>45</td><td>180</td><td>20</td></tr></table>

Lobatto IIIA ( $s = 5 , p = 8$ ),

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td colspan="2">0</td></tr><tr><td>7-√21 14</td><td>119+3√21</td><td>343-9√21</td><td>392-96√21</td><td>343-69√21</td><td colspan="2">-21+3√21</td></tr><tr><td>1</td><td>1960</td><td>2520 392+105√21</td><td>2205</td><td>2520 392-105√21</td><td colspan="2">1960</td></tr><tr><td>2</td><td>13 320</td><td></td><td>8</td><td></td><td colspan="2">3</td></tr><tr><td>7+√21</td><td>119-3√21</td><td>2880 343+69√21</td><td>45 392+96√21</td><td>2880</td><td colspan="2">320</td></tr><tr><td>14</td><td></td><td></td><td></td><td>343+9√21</td><td colspan="2">-21-3√21</td></tr><tr><td></td><td>1960 1</td><td>2520</td><td>2205</td><td>2520</td><td colspan="2">1960</td></tr><tr><td>1</td><td></td><td>49</td><td>16</td><td>49</td><td colspan="2">1</td></tr><tr><td rowspan="2"></td><td>20</td><td>180</td><td>45</td><td>180</td><td colspan="2">20</td></tr><tr><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td colspan="2">1 20</td></tr><tr><td colspan="4">LobattoIIIB (s=5, P1-2015151-201 =8)，</td><td rowspan="2">-7+√21</td><td rowspan="2">0</td></tr><tr><td>0 7-√21</td><td></td><td>27-√21 120</td><td>15</td></tr><tr><td rowspan="12"></td><td></td><td>343+9√21</td><td>56-15√21</td><td>120 343-69√21</td><td rowspan="2">0</td></tr><tr><td></td><td>2520</td><td>315</td><td>2520</td></tr><tr><td>14</td><td></td><td>49+12√12</td><td>49-12√12</td><td>0</td></tr><tr><td>1</td><td>360</td><td>8 45</td><td>360</td><td></td></tr><tr><td>7+√21</td><td>343+69√21</td><td>56+15√21</td><td>343-9√21</td><td>0</td></tr><tr><td>14</td><td>2520</td><td>315</td><td>2520</td><td></td></tr><tr><td>1</td><td>119-3√21</td><td>13</td><td>119+3√21</td><td>0</td></tr><tr><td></td><td></td><td>360</td><td>45</td><td>360</td><td></td></tr><tr><td></td><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td>1 20</td></tr></table>

Lobatto IIIC ( $s = 5 , p = 8$ ),

<table><tr><td>0 7-√21 14 1 7+√21</td><td>中</td><td>7 60 29 180 329+105√21 2880 203+30√21</td><td>2 15 47-15√21 315 73 360 47+15√21 315</td><td>7 60 203-30√21 1260 329-105√21 2880</td><td>六 140 3 160</td></tr></table>

# Exercises 34

34.1 Show that there is a unique Runge–Kutta method of order 4 with $s = 3$ for which $A$ is lower triangular with $a _ { 1 1 } = a _ { 3 3 } = 0$ . Find the tableau for this method.

34.2 Show that the implicit Runge–Kutta given by the tableau

<table><tr><td>0 A</td><td>0 0</td></tr><tr><td>1</td><td>云 0 0</td></tr><tr><td></td><td></td></tr><tr><td>0</td><td>0</td></tr><tr><td>1 32 14 81</td><td>药 0 250 5</td></tr></table>

has order 5.

34.3 Find the tableau for the Gauss method with $s = 4$ and $p = 8$ .

34.4 Show that Gauss methods are invariant under reflection.

# 35 Stability of Implicit Runge–Kutta Methods

350 $A$ -stability, $A ( \alpha )$ -stability and L-stability

We recall that the stability function for a Runge–Kutta method (238b) is the rational function

$$
R ( z ) = 1 + z b ^ { \top } ( I - z A ) ^ { - 1 } \mathbf { 1 } ,
$$

and that a method is A-stable if

$$
| R ( z ) | \leq 1 , \quad { \mathrm { w h e n e v e r ~ } } \mathrm { R e } ( z ) \leq 0 .
$$

For the solution of stiff problems, A-stability is a desirable property, and there is sometimes a preference for methods to be L-stable; this means that the method is A-stable and that, in addition,

$$
R ( \infty ) = 0 .
$$

Where A-stability is impossible or difficult to achieve, a weaker property is acceptable for the solution of many problems.

Definition 350A Let $\alpha$ denote an angle satisfying $\alpha \in ( 0 , \pi )$ and let $S ( \alpha )$ denote the set of points $x + i y$ in the complex plane such that $x \ \leq \ 0$ and $- \tan ( \alpha ) | x | \leq y \leq \tan ( \alpha ) | x |$ . A Runge–Kutta method with stability function $R ( z )$ is $A ( \alpha )$ -stable if $| R ( z ) | \leq 1$ for all $z \in S ( \alpha )$ .

The region $S ( \alpha )$ is illustrated in Figure 350(i) in the case of the Runge–Kutta method

<table><tr><td rowspan="4">入 1+ 2 1</td><td>入</td><td>0</td><td>0</td></tr><tr><td>1-</td><td>入</td><td>0</td></tr><tr><td>2 (1-λ)(1-9λ+6)²)</td><td>2(1-λ)(1-6λ+6λ²)</td><td></td></tr><tr><td>1-3入+6λ2</td><td>1-3入+6λ2</td><td>入</td></tr><tr><td rowspan="3"></td><td></td><td>2(1-3&gt;)</td><td></td></tr><tr><td>1+3&gt; 6(1-)2</td><td>3(1-&gt;)2</td><td>1-3入+6λ² 6(1-λ)2</td></tr><tr><td></td><td></td><td></td></tr></table>

where $\lambda \approx 0 . 1 5 8 9 8 4$ is a zero of $6 \lambda ^ { 3 } - 1 8 \lambda ^ { 2 } + 9 \lambda - 1$ . This value of $\lambda$ was chosen to ensure that (350b) holds, even though the method is not A-stable. It is, in fact, $\mathrm { A } ( \alpha )$ -stable with $\alpha \approx 1 . 3 1 9 4 6 \approx 7 5 . 5 9 9 6 ^ { \circ }$ .

# 351 Criteria for $A$ -stability

We first find an alternative expression for the rational function (350a).

Lemma 351A Let $( A , b , c )$ denote a Runge–Kutta method. Then its stability function is given by

$$
R ( z ) = \frac { \operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) } { \operatorname* { d e t } ( I - z A ) } .
$$

![](images/690e3faa45b81170a17aa11fe62c25aaa19bbb6d6d05478e2f1d8e6565fb4688.jpg)  
Figure 350(i) $\mathrm { A } ( \alpha )$ stability region for the method (350c)

Proof. Because a rank 1 $s \times s$ matrix $u v ^ { \top }$ has characteristic polynomial $\operatorname* { d e t } ( I w - u v ^ { \intercal } ) = w ^ { s - 1 } ( w - v ^ { \intercal } u )$ , a matrix of the form $I + u v ^ { \prime }$ has characteristic polynomial $( w - 1 ) ^ { s - 1 } ( w - 1 - v ^ { \mathsf { I } } u )$ and determinant of the form $1 + v ^ { \intercal } u .$ Hence,

$$
\operatorname* { d e t } \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) = 1 + z b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \mathbf { 1 } = R ( z ) .
$$

We now note that

$$
I + z ( \mathbf { 1 } b ^ { \mathsf { T } } - A ) = \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) ( I - z A ) ,
$$

so that

$$
\operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) = R ( z ) \operatorname* { d e t } ( I - z A ) .
$$

Now write the stability function of a Runge–Kutta method as the ratio of two polynomials

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

and define the E-polynomial by

$$
E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) .
$$

Theorem 351B A Runge–Kutta method with stability function $\begin{array} { r l } { R ( z ) } & { { } = } \end{array}$ $N ( z ) / D ( z )$ is A-stable if and only if (a) all poles of $R$ (that is, all zeros of $D$ ) are in the right half-plane and (b) $E ( y ) \ge 0$ , for all real $y$ .

Proof. The necessity of (a) follows from the fact that if $z ^ { * }$ is a pole then $\begin{array} { r } { \operatorname* { l i m } _ { z \to z ^ { * } } | R ( z ) | = \infty } \end{array}$ , and hence $| R ( z ) | > 1$ , for $z$ close enough to $z ^ { * }$ . The necessity of (b) follows from the fact that $E ( y ) < 0$ implies that $| R ( i y ) | > 1$ , so that $| R ( z ) | > 1$ for some $z = - \epsilon + i y$ in the left half-plane. Sufficiency of these conditions follows from the fact that (a) implies that $R$ is analytic in the left half-plane so that, by the maximum modulus principle, $| R ( z ) | > 1$ in this region implies $| R ( z ) | > 1$ on the imaginary axis, which contradicts (b). $\boxed { \begin{array} { r l } \end{array} }$

# 352 Pad´e approximations to the exponential function

Given a function $f$ , assumed to be analytic at zero, with $f ( 0 ) \neq 0$ , and given non-negative integers $\it l$ and $m$ , it is sometimes possible to approximate $f$ by a rational function

$$
f ( z ) \approx { \frac { N ( z ) } { D ( z ) } } ,
$$

with $N$ of degree $\it l$ and $D$ of degree $m$ and with the error in the approximation equal to $O ( z ^ { l + m + 1 } )$ . In the special case $m = 0$ , this is exactly the Taylor expansion of $f$ about $z ~ = ~ 0$ , and when $\mathit { l } \mathit { \Theta } = \mathit { \Theta } 0$ , $D ( z ) / N ( z )$ is the Taylor expansion of $1 / f ( z )$ .

For some specially contrived functions and particular choices of the degrees $\it l$ and $m$ , the approximation will not exist. An example of this is

$$
f ( z ) = 1 + \sin ( z ) \approx 1 + z - { \frac { 1 } { 6 } } z ^ { 3 } + \cdots ,
$$

with $l = 2$ , $m = 1$ because it is impossible to choose $a$ to make the coefficient of $z ^ { 3 }$ equal to zero in the Taylor expansion of $( 1 + a z ) f ( z )$ .

When an approximation

$$
f ( z ) = \frac { N _ { l m } ( z ) } { D _ { l m } ( z ) } + O ( z ^ { l + m + 1 } )
$$

exists, it is known as the ‘ $( l , m )$ Pad´e approximation’ to $f$ . The array of Pad´e approximations for $l , m = 0 , 1 , 2 , \ldots$ is referred to as ‘the Pad´e table’ for the function $f$ .

Pad´e approximations to the exponential function are especially interesting to us, because some of them are equal to the rational functions of some important Gauss, Radau and Lobatto methods. We show that the full Pad´e table exists for this function and, at the same time, we find explicit values for the coefficients in $N$ and $D$ and for the next two terms in the Taylor series for $N ( z ) - \exp ( z ) D ( z )$ . Because it is possible to rescale both $N$ and $D$ by an arbitrary factor, we specifically choose a normalization for which $N ( 0 ) = D ( 0 ) = 1$ .

Theorem 352A Let $l , m \geq 0$ be integers and define polynomials $N _ { l m }$ and $D _ { l m }$ by

$$
\begin{array} { l } { { \displaystyle N _ { l m } ( z ) = \frac { l ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { l } \frac { ( l + m - i ) ! } { i ! ( l - i ) ! } z ^ { i } , } } \\ { { \displaystyle D _ { l m } ( z ) = \frac { m ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { m } \frac { ( l + m - i ) ! } { i ! ( m - i ) ! } ( - z ) ^ { i } . } } \end{array}
$$

Also define

$$
C _ { l m } = ( - 1 ) ^ { m } \frac { l ! m ! } { ( l + m ) ! ( l + m + 1 ) ! } .
$$

Then

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + \frac { m + 1 } { l + m + 2 } C _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) .
$$

Proof. In the case $m = 0$ , the result is equivalent to the Taylor series for $\exp ( z )$ ; by multiplying both sides of (352d) by $\exp ( - z )$ we find that the result is also equivalent to the Taylor series for $\exp ( - z )$ in the case ${ \mathit { l } } = 0$ . We now suppose that $l \geq 1$ and $m \geq 1$ , and that (352d) has been proved if $\it l$ is replaced by ${ \mathit { l } } - 1$ or $m$ replaced is by $m - 1$ . We deduce the result for the given values of $\it l$ and $m$ so that the theorem follows by induction.

Because the result holds with $\it l$ replaced by ${ \mathit { l } } - 1$ or with $m$ replaced by $m - 1$ , we have

$$
\begin{array} { r l r } & { } & { N _ { l - 1 , m } ( z ) - \exp ( z ) D _ { l - 1 , m } ( z ) + \left( 1 + \frac { m + 1 } { l + m + 1 } z \right) C _ { l - 1 , m } z ^ { l + m } = O ( z ^ { l + m + 2 } ) , } \\ & { } & { ( 3 5 2 } \\ & { } & { N _ { l , m - 1 } ( z ) - \exp ( z ) D _ { l , m - 1 } ( z ) + \left( 1 + \frac { m } { l + m + 1 } z \right) C _ { l , m - 1 } z ^ { l + m } = O ( z ^ { l + m + 2 } ) . } \end{array}
$$

Multiply (352e) by $l / ( l + m )$ and (352f) by $m / ( l + m )$ , and we find that the coefficient of $z ^ { l + m }$ has the value

$$
\frac { l } { l + m } C _ { l - 1 , m } + \frac { m } { l + m } C _ { l , m - 1 } = 0 .
$$

The coefficient of $z ^ { l + m + 1 }$ is found to be equal to $C _ { l m }$ . Next we verify that

$$
\frac { l } { l + m } N _ { l - 1 , m } ( z ) + \frac { m } { l + m } N _ { l , m - 1 } ( z ) - N _ { l m } ( z ) = 0
$$

and that

$$
\frac { l } { l + m } D _ { l - 1 , m } ( z ) + \frac { m } { l + m } D _ { l , m - 1 } ( z ) - D _ { l m } ( z ) = 0 .
$$

Pad´e approximations $N _ { l m } / D _ { l m }$ for $l , m = 0 , 1 , 2 , 3$   

<table><tr><td>m</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>1</td><td>1+z</td><td>1+z+ 1 22 2</td><td>1+z+ 1 + 6 1 2 心 23</td></tr><tr><td>1</td><td>1 1-x</td><td>1+ 1 之</td><td>1+ 2 z+ 1 6</td><td>1+ 3 2 + 1 之 2 + 1 4 4 24 </td></tr><tr><td>2</td><td>1</td><td>1- 1+ </td><td>1 2 1+ z+ 1 2</td><td>1 4 z 1+ 3 z+ 3 2 2 + 1</td></tr><tr><td></td><td>1-z+ 1 22</td><td>1- 2 z+ T 22</td><td>12 1- 1 z+ 1 22 12</td><td>20 60 2 z+ 20 1 22</td></tr><tr><td>3</td><td>1</td><td></td><td>1+ 2 z+ 1 20 2</td><td>1+ 1 z+ 1 × 1 2 2</td></tr><tr><td></td><td></td><td></td><td></td><td>10 120</td></tr><tr><td></td><td>1 1-z+ 2 22 2</td><td>1- 4 22 1 23 24</td><td>3 z+ 3 22 23 20 60</td><td>1- 1 z+ 10 22 120 23</td></tr></table>

The coefficient of $z ^ { i }$ in (352g) is

$$
\frac { ( l - 1 ) ! ( l + m - i - 1 ) ! } { ( l + m ) ! i ! ( l - i ) ! } \big ( l ( l - i ) + m l - l ( l + m - i ) \big ) = 0 ,
$$

so that (352g) follows. The verification of (352h) is similar and will be omitted. It now follows that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + { \frac { m + 1 } { l + m + 2 } } \widetilde { C } _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) ,
$$

and we finally need to prove that $\widetilde { C } _ { l m } = C _ { l m }$ . Operate on both sides of (352i) with the operator $( d / d z ) ^ { l + 1 }$ and multiply the result by $\exp ( - z )$ . This gives

$$
\begin{array} { r } { P ( z ) + \left( \frac { m + 1 } { l + m + 2 } \frac { ( l + m + 2 ) ! } { ( m + 1 ) ! } \widetilde { C } _ { l m } - \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } \right) z ^ { m + 1 } = O ( z ^ { m + 2 } ) , } \end{array}
$$

where $P$ is the polynomial of degree $m$ given by

$$
P ( z ) = \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } z ^ { m } - \left( 1 + \frac { d } { d z } \right) ^ { l + 1 } D _ { l m } ( z ) .
$$

It follows from (352j) that $\widetilde { C } _ { l m } = C _ { l m }$ .

The formula we have found for a possible $( l , m )$ Pad´e approximation to $\exp ( z )$ is unique. This is not the case for an arbitrary function $f$ , as the example of the function given by (352a) shows; the $( 2 , 1 )$ approximation is not unique. The case of the exponential function is covered by the following result:

Theorem 352B The function $N _ { l m } / D _ { l m }$ , where the numerator and denominator are given by (352b) and (352c), is the unique $( l , m )$ Pad´e approximation to the exponential function.

Proof. If $\hat { N } _ { l m } / \hat { D } _ { l m }$ is a second such approximation then, because these functions differ by $O ( z ^ { l + m + 1 } )$ ,

$$
N _ { l m } \widehat { D } _ { l m } - \widehat { N } _ { l m } D _ { l m } = 0 ,
$$

Diagonal members of the Pad´e table $N _ { m m } / D _ { m m }$ for $m = 0 , 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td></td><td></td><td></td><td>Nmm Dmm</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td>1+</td><td>1 1</td></tr><tr><td>1</td><td></td><td>1 1 × 2</td><td>1 2 z 2 12</td><td></td></tr><tr><td>2</td><td></td><td>1 + 1</td><td>1 2 12 1 2 2 1 北</td><td>心</td></tr><tr><td>3</td><td></td><td>1 1 z 1 22 10</td><td>10</td><td>120 2 1 120 2</td></tr><tr><td>4</td><td></td><td>1 X 1 z + 28 1 3 2 2 比</td><td>3 + 比 28 心</td><td>1 + 1 84 2 1680 24</td></tr><tr><td>5</td><td>1</td><td>X 1 2 1 1 + 北 72</td><td>1 30240 6 25</td><td>84 2</td><td>1680 1 1008</td></tr><tr><td></td><td>1</td><td>125 1 2 + 一</td><td>22</td><td>1 + 72 20 1</td><td>1 1 1008 2 30240 1</td></tr><tr><td>6</td><td>1 + Z 1 2 1 2</td><td>1 44 北 66 5 1</td><td>66 23 </td><td>× 792 1 792 24 </td><td>× 15840 1 + 15840 25 1 1 × 25</td></tr></table>

because the expression on the left-hand side is $O ( z ^ { l + m + 1 } )$ , and is at the same time a polynomial of degree not exceeding $\boldsymbol { l } + \boldsymbol { m }$ . Hence, the only way that two distinct approximations can exist is when they can be cancelled to a rational function of lower degrees. This means that for some $( l , m )$ pair, there exists a Pad´e approximation for which the error coefficient is zero. However, since $\exp ( z )$ is not equal to a rational function, there is some higher exponent $k$ and a non-zero constant $C$ such that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) = C z ^ { k } + O ( z ^ { k + 1 } ) ,
$$

with $k \geq l + m + 2$ . Differentiate (352k) $k - m - 1$ times, multiply the result by $\exp ( - z )$ and then differentiate a further $m + 1$ times. This leads to the contradictory conclusion that $C = 0$ . 

Expressions for the $( l , m )$ Pad´e approximations are given in Table 352(I) for $l , m = 0 , 1 , 2 , 3$ . To extend the information further, Table 352(II) is presented to give the values for $l = m = 0 , 1 , 2 , . . . , 7$ . Similar tables are also given for the first and second sub-diagonals in Tables 352(III) and 352(IV), respectively, and error constants corresponding to entries in each of these three tables are presented in Table 352(V).

First sub-diagonal members of the Pad´e table $N _ { m - 1 , m } / D _ { m - 1 , m }$ for $m = 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-1,m Dm-1,m</td><td colspan="4"></td></tr><tr><td>1</td><td colspan="3"></td><td colspan="2">1 1-z</td><td colspan="4"></td></tr><tr><td>2</td><td colspan="3"></td><td>1+</td><td colspan="2"></td><td colspan="3" rowspan="4"></td></tr><tr><td></td><td></td><td></td><td>2-325</td><td>z 1 2 2 1 北</td><td></td></tr><tr><td>3 4</td><td></td><td>35 2 3 十 20 3 1 + 1 2 + 14</td><td>十 比</td><td>2 比 60 1</td><td>20 </td></tr><tr><td>5</td><td></td><td>2 1 4 2 十</td><td>比 5 5 心 23</td><td>22 1 126</td><td>210 2 105 23 840 24 1 1 3024</td></tr></table>

For convenience, we write $V _ { m n } ( z )$ for the two-dimensional vector whose first component is $N _ { l m } ( z )$ and whose second component is $D _ { l m } ( z )$ . From the proof of Theorem 352A, it can be seen that the three such vectors $V _ { l - 1 , m } ( z )$ , $V _ { l , m - 1 } ( z )$ and $V _ { l , m } ( z )$ are related by

$$
l V _ { l - 1 , m } ( z ) + m V _ { l , m - 1 } ( z ) = ( l + m ) V _ { l , m } ( z ) .
$$

Many similar relations between neighbouring members of a Pad´e table exist, and we present three of them. In each case the relation is between three Pad´e vectors of successive denominator degrees.

Theorem 352C If $l , m \geq 2$ then

$$
\begin{array} { l } { { \displaystyle V _ { l m } ( z ) = \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad + \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

Second sub-diagonal members of the Pad´e table

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-2,m Dm-2,m</td></tr><tr><td>2</td><td></td><td>1 1-x+ 12 22</td></tr><tr><td>3</td><td>4 1 2 4</td><td>1+ 4 z 28</td></tr><tr><td>4</td><td>1 + z 十 1 30 1 2 2 1 一 十 + 心 30 28 1+ 3 3 2 1 </td></tr><tr><td>5</td><td>56 336 1 5 品 5 2 × 22 168 23 336 24 1+ 2 z X 1 1 + 1 15 180 1 1</td></tr><tr><td>6 7</td><td>1 3 Z 1 一 + 1 22 36 2 336 5040 151200 1+ 5 5 2 2 4 1 12 66 2 132 2376 2 95040 7 2 × 7 7 × 7 7 1 12 44 比 264 23 2376 24 31680 25 95040 26</td></tr></table>

Proof. Let

$$
\begin{array} { l } { { \displaystyle V ( z ) = V _ { l m } ( z ) - \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad - \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

It is easy to verify that the coefficients of $z ^ { 0 }$ , $z ^ { 1 }$ and $z ^ { 2 }$ vanish in both components of $V ( z )$ . We also find that

$$
\begin{array} { r l } { [ 1 } & { { } - \exp ( z ) ] V ( z ) = O ( z ^ { l + m - 1 } ) . } \end{array}
$$

If $V ( z )$ is not the zero vector, we find that

$$
z ^ { - 2 } \big [ 1 \  - \exp ( z ) \big ] V ( z ) = O ( z ^ { l + m - 3 } ) ,
$$

contradicting the uniqueness of Pad´e approximations of degrees $( l - 2 , m - 2 )$

Theorems 352D and $3 5 2 \mathrm { E }$ which follow are proved in the same way as Theorem 352C and the details are omitted.

Error constants for diagonal and first two sub-diagonals   

<table><tr><td>m</td><td>Cm-2,m</td><td>m-1,m</td><td>mm</td></tr><tr><td>0</td><td></td><td></td><td>1</td></tr><tr><td>1</td><td></td><td></td><td>1 12</td></tr><tr><td>2</td><td>1</td><td></td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>720 1</td></tr><tr><td>4</td><td>480 1</td><td>7200 1</td><td>100800 1</td></tr><tr><td>5</td><td>75600 1</td><td>1411200 1</td><td>25401600 1</td></tr><tr><td>6</td><td>20321280 1</td><td>457228800 1</td><td>10059033600 1</td></tr><tr><td>7</td><td>8382528000 1 4931800473600</td><td>221298739200 1</td><td>5753767219200 1 4487938430976000</td></tr></table>

Theorem 352D If $l \geq 1$ and $m \geq 2$ then

$$
\begin{array} { l } { \displaystyle { V _ { l m } ( z ) = \left( 1 - \frac { l } { ( l + m ) ( l + m - 1 ) } z \right) V _ { l , m - 1 } ( z ) } } \\ { \displaystyle { \qquad + \frac { l ( m - 1 ) } { ( l + m ) ( l + m - 1 ) ^ { 2 } ( l + m - 2 ) } z ^ { 2 } V _ { l - 1 , m - 2 } ( z ) . } } \end{array}
$$

Theorem 352E If $l \geq 0$ and $m \geq 2$ then

$$
V _ { l m } ( z ) = \Bigl ( 1 - \frac { 1 } { l + m } z \Bigr ) V _ { l + 1 , m - 1 } ( z ) + \frac { m - 1 } { ( l + m ) ^ { 2 } ( l + m - 1 ) } z ^ { 2 } V _ { l , m - 2 } ( z ) .
$$

# 353 A-stability of Gauss and related methods

We consider the possible A-stability of methods whose stability functions correspond to members on the diagonal and first two sub-diagonals of the Pad´e table for the exponential function. These include the Gauss methods and the Radau IA and IIA methods as well as the Lobatto IIIC methods. A corollary is that the Radau IA and IIA methods and the Lobatto IIIC methods are L-stable.

Theorem 353A Let s be a positive integer and let

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

denote the $( s - d , s )$ member of the Pad´e table for the exponential function, where $d = 0$ , $1$ or 2. Then

$$
| R ( z ) | \leq 1 ,
$$

for all complex $\mathcal { L }$ satisfying $\mathrm { R e } z \le 0$ .

Proof. We use the E-polynomial. Because $N ( z ) = \exp ( z ) D ( z ) + O ( z ^ { 2 s - d + 1 } )$ , we have

$$
\begin{array} { l } { { E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) \nonumber } } \\ { { \nonumber } } \\ { { = D ( i y ) D ( - i y ) - \exp ( i y ) D ( i y ) \exp ( - i y ) D ( - i y ) + { \cal O } ( y ^ { 2 s - d + 1 } ) } } \\ { { \nonumber } } \\ { { = { \cal O } ( y ^ { 2 s - d + 1 } ) . } } \end{array}
$$

Because $E ( y )$ has degree not exceeding $2 s$ and is an even function, either $E ( y ) = 0$ , in the case $d = 0$ , or $E ( y ) = C y ^ { 2 s }$ with $C > 0$ , in the cases $d = 1$ and $d = 2$ . In all cases, $E ( y ) \ge 0$ for all real $y$ .

To complete the proof, we must show that the denominator of $R$ has no zeros in the left half-plane. Without loss of generality, we assume that $\mathrm { R e } z < 0$ and we prove that $D ( z ) \neq 0$ . Write $D _ { 0 }$ , $D _ { 1 }$ , $\cdot \cdot \cdot$ , $D _ { s }$ for the denominators of the sequence of Pad´e approximations given by

$$
V _ { 0 0 } , V _ { 1 1 } , \ldots , V _ { s - 1 , s - 1 } , V _ { s - d , s } ,
$$

so that $D ( z ) = D _ { s } ( z )$ . From Theorems 352C, 352D and 352E, we have

$$
D _ { k } ( z ) = D _ { k - 1 } ( z ) + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } D _ { k - 2 } , \quad k = 2 , 3 , \ldots , s - 1 ,
$$

and

$$
D _ { s } ( z ) = ( 1 - \alpha z ) D _ { s - 1 } + \beta z ^ { 2 } D _ { s - 2 } ,
$$

where the constants $\alpha$ and $\beta$ will depend on the value of $d$ and $s$ . However, $\alpha = 0$ if $d = 0$ and $\alpha > 0$ for $d = 1$ and $d = 2$ . In all cases, $\beta > 0$ .

Consider the sequence of complex numbers, $\zeta _ { k }$ , for $k = 1 , 2 , \dots , s$ , defined by

$$
\begin{array} { l } { \displaystyle \zeta _ { 1 } = 1 - \frac 1 2 z , } \\ { \displaystyle \zeta _ { k } = 1 + \frac 1 { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } \zeta _ { k - 1 } ^ { - 1 } , \qquad k = 2 , 3 , \ldots , s - 1 , } \\ { \displaystyle \zeta _ { s } = ( 1 - \alpha z ) + \beta z ^ { 2 } \zeta _ { s - 1 } ^ { - 1 } . } \end{array}
$$

This means that $\zeta _ { 1 } / z = - 1 / 2 + 1 / z$ has negative real part. We prove by induction that $\zeta _ { k } / z$ also has negative real part for $k = 2 , 3 , \ldots , s$ . We see this by noting that

$$
\begin{array} { l } { \displaystyle \frac { \zeta _ { k } } { z } = \frac { 1 } { z } + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } \left( \frac { \zeta _ { k - 1 } } { z } \right) ^ { - 1 } , \qquad k = 2 , 3 , \dots , s - 1 , } \\ { \displaystyle \frac { \zeta _ { s } } { z } = \frac { 1 } { z } - \alpha + \beta \left( \frac { \zeta _ { s - 1 } } { z } \right) ^ { - 1 } . } \end{array}
$$

The fact that $D _ { s } ( z )$ cannot vanish now follows by observing that

$$
\begin{array} { r } { D _ { s } ( z ) = \zeta _ { 1 } \zeta _ { 2 } \zeta _ { 3 } \cdot \cdot \cdot \zeta _ { s } . } \end{array}
$$

Hence, $D = D _ { s }$ does not have a zero in the left half-plane.

Alternative proofs of this and related results have been given byAxelsson (1969, 1972), Butcher (1977), Ehle (1973), Ehle and Picel (1975), Watts and Shampine (1972) and Wright (1970).

# 354 Order stars

We have identified some members of the Pad´e table for the exponential function for which the corresponding numerical methods are A-stable. We now ask: are there other members of the table with this property? It will be seen that everything hinges on the value of $m - l$ , the degree of the denominator minus the degree of the numerator. It is clear that if $m - l < 0$ , A-stability is impossible, because in this case

$$
| R ( z ) | \to \infty ,
$$

as $z  \infty$ , and hence, for some $z$ satisfying $\mathrm { R e } z < 0$ , $| R ( z ) |$ is greater than $^ { 1 }$ . For $m - l \in \{ 0 , 1 , 2 \}$ , A-stability follows from Theorem 353A. Special cases with $m - l > 2$ suggest that these members of the Pad´e table are not A-stable. For the third sub-diagonal, this was proved by Ehle (1969), and for the fourth and fifth sub-diagonals by Nørsett (1974). Based on these observations, Ehle (1973) conjectured that no case with $m - l > 2$ can be A-stable. This result was eventually proved by Wanner, Hairer and Nørsett (1978), and we devote this subsection to introducing the approximations considered in that paper and to proving the Ehle conjecture.

In Subsection 216, we touched on the idea of an order star. Associated with the stability function $R ( z )$ for a Runge–Kutta method, we consider the set of points in the complex plane such that

$$
| \exp ( - z ) R ( z ) | > 1 .
$$

This is known as the ‘order star’ of the method, and the set of points such that

$$
| \exp ( - z ) R ( z ) | < 1
$$

is the ‘dual order star’. The common boundary of these two sets traces out an interesting path, as we see illustrated in Figure 354(i), for the case of the $( 1 , 3 )$ Pad´e approximation given by

$$
R ( z ) = { \frac { 1 + { \frac { 1 } { 4 } } z } { 1 - { \frac { 3 } { 4 } } z + { \frac { 1 } { 4 } } z ^ { 2 } - { \frac { 1 } { 2 4 } } z ^ { 3 } } } .
$$

![](images/245bb3fc37091066fe93197cfed019393d414bf7d740ed1ff3e9f33fd1156ad7.jpg)  
Order star for the $( 1 , 3 )$ Pad´e approximation to exp

In this diagram, the dual order star, which can also be described as the ‘relative stability region’, is the interior of the unshaded region. The order star is the interior of the shaded region.

In Butcher (1987) an attempt was made to present an informal survey of order stars leading to a proof of the Ehle result. In the present volume, the discussion of order stars will be even more brief, but will serve as an introduction to an alternative approach to achieve similar results. In addition to Wanner, Hairer and Nørsett (1978), the reader is referred to Iserles and Nørsett (1991) for fuller information and applications of order stars.

The ‘order star’, for a particular rational approximation to the exponential function, disconnects into ‘fingers’ emanating from the origin, which may be bounded or not, and similar remarks apply to ‘dual fingers’ which are the connected components of the dual star. The following statements summarize the key properties of order stars for applications of the type we are considering. Because we are including only hints of the proofs, we refer to them as remarks rather than as lemmas or theorems. Note that $S$ denotes the order star for a specific ‘method’ and $I$ denotes the imaginary axis.

Remark 354A A method is $A$ -stable if and only if $S$ has no poles in the negative half-plane and $S \cup I = \emptyset$ , because the inclusion of the exponential factor does not alter the set of poles and does not change the magnitude of the stability function on $I$ .

Remark 354B There exists $\rho _ { 0 } ~ > ~ 0$ such that, for all $\rho ~ \geq ~ \rho _ { 0 }$ , functions $\theta _ { 1 } ( \rho )$ and $\theta _ { 2 } ( \rho )$ exist such that the intersection of $S$ with the circle $| z | = \rho$ is the set $\{ \rho \exp ( i \theta ) : \theta _ { 1 } < \theta < \theta _ { 2 } \}$ and where $\begin{array} { l } { \operatorname* { l i m } _ { \rho \to \infty } \theta _ { 1 } ( \rho ) ~ = ~ \pi / 2 } \end{array}$ and $\operatorname* { l i m } _ { \rho \to \infty } \theta _ { 2 } ( \rho ) = 3 \pi / 2$ , because at a great distance from the origin, the behaviour of the exponential function multiplied by the rational function on which the order star is based is dominated by the exponential factor.

![](images/478ddae7b9c90a9cb8002184e20f54a267f735bc8144ad38f973845d858b99b8.jpg)  
Relation between order arrows and order stars

Remark 354C For a method of order $p$ , the arcs $\{ r \exp ( i ( j + \frac { 1 } { 2 } ) \pi / ( p + 1 ) ) :$ $0 \leq r \}$ , where $j = 0 , 1 , \ldots , 2 p + 1$ , are tangential to the boundary of $S$ at 0, because $\exp ( - z ) R ( z ) = 1 + C z ^ { p + 1 } + O \big ( | z | ^ { p + 2 } \big )$ , so that $| \exp ( - z ) R ( z ) | =$ $1 + \mathrm { R e } ( C z ^ { p + 1 } ) + O ( | z | ^ { p + 2 } )$ .

It is possible that $m$ bounded fingers can join together to make up a finger of multiplicity $m$ . Similarly, $m$ dual fingers in $\overline { S }$ can combine to form a dual finger with multiplicity $m$ .

Remark 354D Each bounded finger of $S$ , with multiplicity $_ { m }$ , contains at least m poles, counted with their multiplicities, because, by the Cauchy– Riemann conditions, the argument of $\exp ( - z ) R ( z )$ increases monotonically as the boundary of the order star is traced out in a counter-clockwise direction.

In the following subsection, we introduce a slightly different tool for studying stability questions. The basic idea is to use, rather than the fingers and dual fingers as in order star theory, the lines of steepest ascent and descent from the origin. Since these lines correspond to values for which $R ( z ) \exp ( - z )$ is real and positive, we are, in reality, looking at the set of points in the complex plane where this is the case.

We illustrate this by presenting, in Figure 354(ii), a modified version of Figure 354(i), in which the boundary of the order star is shown as a dashed line and the ‘order arrows’, as we call them, are shown with arrow heads showing the direction of ascent.

# 355 Order arrows and the Ehle barrier

For a stability function $R ( z )$ of order $p$ , define two types of ‘order arrows’ as follows:

Definition 355A The locus of points in the complex plane for which $\phi ( z ) =$ $R ( z ) \exp ( - z )$ is real and positive is said to be the ‘order web’ for the rational function $R$ . The part of the order web connected to 0 is the ‘principal order web’. The rays emanating from 0 with increasing value of $\phi$ are ‘up arrows’ and those emanating from 0 with decreasing $\phi$ are ‘down arrows’.

The up and down arrows leave the origin in a systematic pattern:

Theorem 355B Let $R$ be a rational approximation to exp of exact order $p$ so that

$$
R ( z ) = \exp ( z ) - C z ^ { p + 1 } + O ( z ^ { p + 2 } ) ,
$$

where the error constant $C$ is non-zero. If $C ~ < ~ 0$ ( $C ~ > ~ 0$ ) there are up (down) arrows tangential at $0$ to the rays with arguments $k 2 \pi i / ( p + 1 )$ , $k ~ = ~ 0 , 1 , \ldots , p$ , and down (up) arrows tangential at $0$ to the rays with arguments $( 2 k + 1 ) \pi i / ( p + 1 )$ , $k = 0 , 1 , \dotsc , p$ .

Proof. If, for example, $C ~ < ~ 0$ , consider the set $\{ r \exp ( i \theta ) : r > 0 , \theta \in$ $[ k 2 \pi i / ( p + 1 ) - \epsilon , k 2 \pi i / ( p + 1 ) + \epsilon \}$ , where $\epsilon$ and $r$ are both small and $k \in \{ 0 , 1 , 2 , \ldots , p \}$ . We have

$$
R ( z ) \exp ( - z ) = 1 + ( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) + O ( r ^ { p + 2 } ) .
$$

For $r$ sufficiently small, the last term is negligible and, for $\epsilon$ sufficiently small, the real part of $( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) )$ is positive. The imaginary part changes sign so that an up arrow lies in this wedge. The cases of the down arrows and for $C > 0$ are proved in a similar manner. $\boxed { \begin{array} { r l } \end{array} }$

Where the arrows leaving the origin terminate is of crucial importance.

Theorem 355C The up arrows terminate either at poles of $R$ or at $- \infty$ .   
The down arrows terminate either at zeros of $R$ or at $+ \infty$ .

Proof. Consider a point on an up arrow for which $| z |$ is sufficiently large to ensure that it is not possible that $z$ is a pole or that $z$ is real with $( d / d z ) ( R ( z ) \exp ( - z ) ) ~ = ~ 0$ . In this case we can assume without loss of generality that $\operatorname { I m } ( z ) \geq 0$ . Write $R ( z ) = K z ^ { n } + O ( \vert z \vert ^ { n - 1 } )$ and assume that $K > 0$ (if $K < 0$ , a slight change is required in the details which follow). If $z = x + i y = r \exp ( i \theta )$ , then

$$
\begin{array} { l } { w ( z ) = R ( z ) \exp ( - z ) } \\ { \quad = K r ^ { n } \exp ( - x ) \big ( 1 + O ( r ^ { - 1 } ) \big ) \exp \big ( i ( n \theta - y + O ( r ^ { - 1 } ) ) \big ) . } \end{array}
$$

Because $\theta$ cannot leave the interval $[ 0 , \pi ]$ , then for $w$ to remain real, $y$ is bounded as $z \longrightarrow \infty$ . Furthermore, $w \to \infty$ implies that $x \to - \infty$ .

The result for the down arrows is proved in a similar way.

We can obtain more details about the fate of the arrows from the following result.

Theorem 355D Let $R$ be a rational approximation to exp of order $p$ with numerator degree $n$ and denominator degree $d$ . Let $\widehat { n }$ denote the number of down arrows terminating at zeros and $\hat { d }$ the number of up arrows terminating at poles of R. Then

$$
\widehat { n } + \widehat { d } \geq p .
$$

Proof. There are $p + 1 - \widehat { n }$ down arrows and $p + 1 - { \acute { d } }$ up arrows terminating at $+ \infty$ and $- \infty$ , respectively. Let $\theta$ and $\phi$ be the minimum angles with the properties that all the down arrows which terminate at $+ \infty$ lie within $\theta$ on either side of the positive real axis and all the up arrows which terminate at $- \infty$ lie within an angle $\phi$ on either side of the negative real axis. Hence

$$
2 \theta \geq \frac { ( p - \widehat { n } ) 2 \pi } { p + 1 } , 2 \phi \geq \frac { ( p - \widehat { d } ) 2 \pi } { p + 1 } .
$$

Because up arrows and down arrows cannot cross and, because there is a wedge with angle equal to at least $\pi / ( p + 1 )$ between the last down arrow and the first up arrow, it follows that $2 \theta + 2 \phi + 2 \pi / ( p + 1 ) \le 2 \pi$ . Hence we obtain the inequality

$$
\frac { 2 p + 1 - \widehat { n } - \widehat { d } } { p + 1 } 2 \pi \leq 2 \pi ,
$$

and the result follows.

For Pad´e approximations we can obtain precise values of $\widehat { n }$ and $\hat { d }$ .

Theorem 355E Let $R ( z )$ denote a Pad´e approximation to $\exp ( z )$ , with degrees n (numerator) and d (denominator). Then n of the down arrows terminate at zeros and $d$ of the up arrows terminate at poles.

Proof. Because $p = n + d$ , $n \geq \widetilde n$ and $d \geq \widehat { d }$ , it follows from Theorem 355D that

$$
p = n + d \geq \widetilde { n } + \widetilde { d } \geq p
$$

and hence that $( n - \widetilde { n } ) + ( d - \overset { . } { d } ) = 0$ . Since both terms are non-negative they must be zero and the result follows. 

Before proving the ‘Ehle barrier’, we establish a criterion for A-stability based on the up arrows that terminate at poles.

Theorem 355F A Runge–Kutta method is A-stable only if all poles of the stability function $R ( z )$ lie in the right half-plane and no up arrow of the order web intersects with or is tangential to the imaginary axis.

Proof. The requirement on the poles is obvious. If an up arrow intersects or is tangential to the imaginary axis then there exists $y$ such that

$$
| R ( i y ) \exp ( - i y ) | > 1 .
$$

Because $| \exp ( - i y ) | = 1$ , it follows that $| R ( i y ) | > 1$ and the method is not A-stable. $\sqcup$

We are now in a position to prove the result formerly known as the Ehle conjecture (Ehle, 1973),but which we will also refer to as the ‘Ehle barrier’.

Theorem 355G Let $R ( z )$ denote the stability function of a Runge–Kutta method. If $R ( z )$ is an $( n , d )$ Pad´e approximation to $\exp ( z )$ then the Runge– Kutta is not $A$ -stable unless $d \leq n + 2$ .

Proof. If $d \geq n + 3$ and $p = n + d$ , it follows that $d \geq \frac { 1 } { 2 } ( p + 3 )$ . By Theorem 355E, at least $d$ up arrows terminate at poles. Suppose these leave zero in directions between $- \theta$ and $+ \theta$ from the positive real axis. Then

$$
2 \theta \geq \frac { 2 \pi ( d - 1 ) } { p + 1 } \geq \pi ,
$$

and at least one up arrow, which terminates at a pole, is tangential to the imaginary axis or passes into the left half-plane. If the pole is in the left halfplane, then the stability function is unbounded in this half-plane. On the other hand, if the pole is in the right half-plane, then the up arrow must cross the imaginary axis. In either case, the method cannot be A-stable, by Theorem 355F. 

# 356 AN-stability

Linear stability analysis is based on the linear test problem

$$
y ^ { \prime } ( x ) = q y ( x ) ,
$$

so that

$$
y _ { n } = R ( z ) y _ { n - 1 } ,
$$

where $z = h q$ . Even though this analysis provides useful information about the behaviour of a numerical method when applied to a stiff problem, even more is learned from generalizing this analysis in two possible ways. The first

of these generalizations allows the linear factor $q$ to be time-dependent so that the test problem becomes

$$
y ^ { \prime } ( x ) = q ( x ) y ( x ) .
$$

A second generalization, which we explore in Subsection 357, allows the differential equation to be non-linear.

When (356a) is numerically solved using an implicit Runge–Kutta method $( A , b ^ { \prime } , c )$ , the stage values satisfy the equations

$$
Y _ { i } = y _ { n - 1 } + \sum _ { j = 1 } ^ { s } a _ { i j } h q ( x _ { n - 1 } + h c _ { j } ) Y _ { j } , \qquad i = 1 , 2 , \dots , s ,
$$

and the output result is

$$
y _ { n } = y _ { n - 1 } + \sum _ { i = 1 } ^ { s } b _ { i } h q ( x _ { n - 1 } + h c _ { i } ) Y _ { i } .
$$

Let $Z$ denote the diagonal matrix given by

$$
{ \cal Z } = \left[ \begin{array} { c c c c c } { { h q ( x _ { n - 1 } + h c _ { 1 } ) } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { h q ( x _ { n - 1 } + h c _ { 2 } ) } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { h q ( x _ { n - 1 } + h c _ { s } ) } } \end{array} \right] ~ ,
$$

This makes it possible to write the vector of stage values in the form

$$
Y = y _ { n - 1 } { \bf 1 } + A Z Y ,
$$

so that

$$
Y = ( I - A Z ) ^ { - 1 } \mathbf { 1 } y _ { n - 1 } .
$$

The output value is given by

$$
y _ { n } = y _ { n - 1 } + b ^ { \mathsf { T } } Z Y = \left( 1 + b ^ { \mathsf { T } } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } \right) y _ { n - 1 } = R ( Z ) y _ { n - 1 } .
$$

The function $R ( Z )$ introduced here is the non-autonomous generalization of the linear stability function.

We are mainly concerned with situations in which the stage abscissae are distinct and where they do not interfere with the stages of adjoining steps. This means that we can regard the diagonal elements of $Z$ as different from each other and independent of the values in the steps that come before or after the current step. With this in mind, we define a non-autonomous counterpart of A-stability that will guarantee that we obtain stable behaviour as long as the real part of $q ( x )$ is never positive. This is appropriate because the exact solution to (356a) is never increasing under this assumption, and we want to guarantee that this property carries over to the computed solution.

Definition 356A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘AN-stable’ if the function

$$
R ( Z ) = 1 + b ^ { \intercal } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } ,
$$

where $Z = \operatorname { d i a g } \left( \left[ z _ { 1 } \quad z _ { 2 } \quad \cdots \quad z _ { s } \right] \right)$ is bounded in magnitude by 1 whenever $z _ { 1 }$ , $z _ { 2 }$ , . . . , $z _ { s }$ are in the left half-plane.

It is interesting that a simple necessary and sufficient condition exists for AN-stability. In Theorem 356C we state this criterion and prove it only in terms of necessity. Matters become complicated if the method can be reduced to a method with fewer stages that gives exactly the same computed result. This can happen, for example, if there exists $j ~ \in ~ \{ 1 , 2 , \ldots , s \}$ such that $b _ { j } = 0$ , and furthermore, $a _ { i j } = 0$ for all $i = 1 , 2 , \dots , s$ , except perhaps for $i = j$ . Deleting stage $j$ has no effect on the numerical result computed in a step. We make a detailed study of reducibility in Subsection 381, but in the meantime we identify ‘irreducibility in the sense of Dahlquist and Jeltsch’, or ‘DJ-irreducibility’, (Dahlquist and Jeltsch, 1979) as the property that a tableau cannot be reduced in the sense of Definition 356B.

Definition 356B A Runge–Kutta method is ‘DJ-reducible’ if there exists a partition of the stages

$$
\{ 1 , 2 , \ldots , s \} = S \cup S _ { 0 } ,
$$

with $S _ { 0 }$ non-empty, such that if $i \in S$ and $j \in S _ { 0 }$ ,

$$
b _ { j } = 0 \ a n d \ a _ { i j } = 0 .
$$

The ‘reduced method’ is the method formed by deleting all stages numbered by members of the set $S _ { 0 }$ .

The necessary condition to be given in Theorem 356C will be strengthened under DJ-irreducibility in Corollary 356D.

Theorem 356C Let $( A , b ^ { \prime } , c )$ be an implicit Runge–Kutta method. Then the method is AN-stable only if

$$
b _ { j } \geq 0 , \qquad j = 1 , 2 , \ldots , s ,
$$

and the matrix

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is positive semi-definite.

Proof. If $b _ { j } < 0$ then choose $Z = - t \mathrm { d i a g } ( e _ { j } )$ , for $t$ positive. The value of $R ( Z )$ becomes

$$
R ( Z ) = 1 - t b _ { j } + O ( t ^ { 2 } ) ,
$$

which is greater than $^ { 1 }$ for $t$ sufficiently small. Now consider $Z$ chosen with purely imaginary components

$$
Z = i \mathrm { d i a g } ( v t ) ,
$$

where $v$ has real components and $t$ is a small positive real. We have

$$
\begin{array} { c } { { R ( Z ) = 1 + i t b ^ { \top } \mathrm { d i a g } ( v ) { \bf 1 } - t ^ { 2 } b ^ { \top } \mathrm { d i a g } ( v ) A \mathrm { d i a g } ( v ) { \bf 1 } + O ( t ^ { 3 } ) } } \\ { { { } } } \\ { { = 1 + i t b ^ { \top } v - t ^ { 2 } v ^ { \top } \mathrm { d i a g } ( b ) A v + O ( t ^ { 3 } ) , } } \end{array}
$$

so that

$$
| R ( Z ) | ^ { 2 } = 1 - t ^ { 2 } v ^ { \top } M v + O ( t ^ { 3 } ) .
$$

Since this cannot exceed $^ { 1 }$ for $t$ small and any choice of $v$ , $M$ is positive semi-definite. 

Since there is no practical interest in reducible methods, we might look at the consequences of assuming a method is irreducible. This result was published in Dahlquist and Jeltsch (1979):

Corollary 356D Under the same conditions of Theorem 356C, with the additional assumption that the method is DJ-irreducible,

$$
b _ { j } > 0 , \qquad j = 1 , 2 , \ldots , s .
$$

Proof. Suppose that for $i \leq \overline { { s } }$ , $b _ { i } > 0$ , but that for $i > { \overline { { s } } }$ , $b _ { i } = 0$ . In this case, $M$ can be written in partitioned form as

$$
\begin{array} { r } { M = \left[ \begin{array} { c c } { \overline { { M } } } & { N } \\ { N ^ { \top } } & { 0 } \end{array} \right] } \end{array}
$$

and this cannot be positive semi-definite unless $N = 0$ . This implies that

$$
a _ { i j } = 0 , \quad { \mathrm { w h e n e v e r ~ } } i \leq { \overline { { s } } } < j ,
$$

implying that the method is reducible to a method with only $\overline { { s } }$ stages.

# 357 Non-linear stability

The second generalization of A-stability we consider is the assumption that, even though the function $f$ is non-linear, it satisfies the condition that

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

where $\langle \cdot \rangle$ denotes a semi-inner product, with corresponding semi-norm defined by

$$
| \boldsymbol { u } | = \langle \boldsymbol { u } , \boldsymbol { u } \rangle ^ { 1 / 2 } .
$$

The reason for our interest in the assumption (357a) is that if there are two solutions $y$ and $z$ to the same differential equations, but with possibly different initial values, then the norm difference of $y$ and $z$ satisfies the bound

$$
| y ( x ) - z ( x ) | \leq | y ( x _ { 0 } ) - z ( x _ { 0 } ) | ,
$$

because

$$
{ \frac { d } { d x } } | y ( x ) - z ( x ) | ^ { 2 } = 2 \langle f ( y ( x ) ) - f ( z ( x ) ) , y ( x ) - z ( x ) \rangle \leq 0 .
$$

The corresponding property for a Runge–Kutta method would be that the sequences of computed solutions satisfy

$$
| y _ { n } - z _ { n } | \leq | y _ { n - 1 } - z _ { n - 1 } | .
$$

It would equally be possible to use a simpler type of test problem, such as $Y ^ { \prime } ( x ) = F ( Y ( x ) )$ , where

$$
\begin{array} { r } { \langle \langle g ( U ) , U \rangle \rangle \leq 0 , } \end{array}
$$

because (357a) can be expressed using (357c). If $\langle \cdot \rangle$ is the semi-inner product on $\mathbb { R } ^ { N }$ used in (357a), with $| \cdot |$ the corresponding semi-norm, then we can define a quasi-inner product $\langle \langle \cdot \rangle \rangle$ on $\mathbb { R } ^ { 2 N }$ , with corresponding norm $\| \cdot \|$ , by the formula

$$
\left. \left. \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] , \left[ \begin{array} { l } { \widetilde { u } } \\ { \widetilde { v } } \end{array} \right] \right. \right. = \langle u , \widetilde { u } \rangle - \langle u , \widetilde { v } \rangle - \langle v , \widetilde { u } \rangle + \langle v , \widetilde { v } \rangle .
$$

The semi-norms defined from these quasi-inner products are related by

$$
\left\| \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] \right\| = \langle \langle u - v , u - v \rangle \rangle = | u - v | ^ { 2 } ,
$$

and we can write the condition (357a) in the form

$$
\left. \left. G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right]}  \right) , { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right. \right. \leq 0 ,
$$

where $G$ is defined by

$$
G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right) = { \left[ \begin{array} { l } { f ( u ) } \\ { f ( v ) } \end{array} \right] } .
$$

Furthermore, the requirement on a numerical method (357b) can be written in the form

$$
\| Y _ { n } \| \leq \| Y _ { n - 1 } \| .
$$

Hence we lose no generality in using a test problem which satisfies (357c) rather than the formally more complicated condition (357a). We therefore adopt this requirement, but revert to the more conventional notation of using $\langle \cdot \rangle$ for a standard semi-inner product with $\| \cdot \|$ the corresponding norm.

Even though we have simplified the notation in one way, it is appropriate to generalize it in another. We really need to avoid the use of autonomous problems because of the intimate relationship that will be found between ANstability and the type of non-linear stability we are discussing here. When Definition 357A was first introduced, it was referred to as ‘B-stability’, because it is one step more stringent than A-stability. In the non-autonomous form in which it seems to be a more useful concept, a more natural name is BNstability.

Definition 357A A Runge–Kutta $( A , b ^ { \intercal } , c )$ is ‘BN-stable’ if for any initial value problem

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

satisfying the condition

$$
\langle f ( x , u ) , u \rangle \leq 0 ,
$$

the sequence of computed solutions satisfies

$$
\left\| y _ { n } \right\| \leq \left\| y _ { n - 1 } \right\| .
$$

The crucial result is that for an irreducible non-confluent method, ANstability and BN-stability are equivalent. Because of the fundamental importance of the necessary and sufficient conditions for a Runge–Kutta method to have either, and therefore both, of these properties, we formalize these conditions:

Definition 357B A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘algebraically stable’ if $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ , and if the matrix $M$ , given by

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top } ,
$$

is positive semi-definite.

We now show the sufficiency of this property.

Theorem 357C If a Runge–Kutta method is algebraically stable then it is BN-stable.

Proof. Let $F _ { i } = f ( x _ { n - 1 } + h c _ { i } , Y _ { i } )$ . We note that if $M$ given by (357d) is positive semi-definite, then there exist vectors $v _ { l } \in \mathbb { R } ^ { s }$ , $l = 1 , 2 , \ldots , \overline { { s } } \leq s$ , such that

$$
M = \sum _ { l = 1 } ^ { \overline { { s } } } \mu _ { l } \mu _ { l } ^ { \intercal } .
$$

This means that a quadratic form can be written as the sum of squares as follows:

$$
\xi ^ { \mathsf { T } } M \xi = \sum _ { l = 1 } ^ { \overline { { s } } } ( \mu _ { l } ^ { \mathsf { T } } \xi ) ^ { 2 } .
$$

Furthermore, a quadratic form of inner products

$$
\sum _ { i , j = 1 } ^ { s } m _ { i j } \langle U _ { i } , U _ { j } \rangle
$$

is equal to

$$
\sum _ { l = 1 } ^ { \overline { { s } } } \Big \| \sum _ { i = 1 } ^ { s } \mu _ { l i } U _ { i } \Big \| ^ { 2 } ,
$$

and cannot be negative. We show that

$$
\| y _ { n } \| - \| y _ { n - 1 } \| ^ { 2 } = 2 h \sum _ { i = 1 } ^ { s } b _ { i } \langle Y _ { i } , F _ { i } \rangle - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } \langle F _ { i } , F _ { j } \rangle ,
$$

so that the result will follow. To prove (357e), we use the equations

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } } , } \\ { { \displaystyle Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) F _ { j } } , } \end{array}
$$

which hold for $i = 1 , 2 , \dots , s$ . In each case, form the quasi-inner product with $F _ { i }$ , and we find

$$
\begin{array} { l } { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n - 1 } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \langle F _ { i } , F _ { j } \rangle , } } \\ { { } } \\ { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) \langle F _ { i } , F _ { j } \rangle . } } \end{array}
$$

Hence,

$$
\begin{array} { c } { { 2 h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \big \langle Y _ { i } , F _ { i } \big \rangle = \Big \langle y _ { n } + y _ { n - 1 } , h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } \Big \rangle } } \\ { { = h ^ { 2 } \displaystyle \sum _ { i , j = 1 } ^ { s } ( 2 b _ { i } a _ { i j } - b _ { i } b _ { j } ) \big \langle F _ { i } , F _ { j } \big \rangle . } } \end{array}
$$

Substitute $y _ { n }$ and $y _ { n - 1 }$ from (357f) and (357g) and rearrange to deduce (357e).

Our final aim in this discussion of non-autonomous and non-linear stability is to show that BN-stability implies AN-stability. This will give the satisfactory conclusion that algebraic stability is equivalent to each of these concepts.

Because we have formulated BN-stability in terms of a quasi-inner product over the real numbers, we first need to see how (356a) can be expressed in a suitable form. Write the real and imaginary parts of $q ( x )$ as $\alpha ( x )$ and $\beta ( x )$ , respectively. Also write $y ( x ) = \xi ( x ) + i \eta ( x )$ and write $\zeta ( x )$ for the function with values in $\mathbb { R } ^ { 2 }$ whose components are $\xi ( x )$ and $\eta ( x )$ , respectively.

Thus, because

$$
\begin{array} { c } { { y ^ { \prime } ( x ) = ( \alpha ( x ) + i \beta ( x ) ) ( \xi ( x ) + i \eta ( x ) ) } } \\ { { { } } } \\ { { { } = ( \alpha ( x ) \xi ( x ) - \beta ( x ) \eta ( x ) ) + i ( \beta ( x ) \xi ( x ) + \alpha ( x ) \eta ( x ) ) , } } \end{array}
$$

we can write

$$
\zeta ^ { \prime } ( x ) = Q \zeta ,
$$

where

$$
Q = \left[ \begin{array} { c c } { { \alpha ( x ) } } & { { - \beta ( x ) } } \\ { { \beta ( x ) } } & { { \alpha ( x ) } } \end{array} \right] .
$$

Using the usual inner product we now have the dissipativity property

$$
\begin{array} { r } { \langle Q v , v \rangle = \alpha \| v \| ^ { 2 } \leq 0 , } \end{array}
$$

if $\alpha \leq 0$

What we have found is that the test problem for AN-stability is an instance of the test problem for BN-stability. This means that we can complete the chain of equivalences interconnecting AN-stability, BN-stability and algebraic stability. The formal statement of the final step is as follows:

Theorem 357D If an irreducible non-confluent Runge–Kutta method is BNstable, then it is AN-stable.

# 358 BN-stability of collocation methods

In the case of methods satisfying the collocation conditions

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad \quad \quad i , k = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \quad \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \qquad \quad \quad k = 1 , 2 , \ldots , s , } } \end{array}
$$

a congruence transformation of $M$ , using the Vandermonde matrix

$$
V = { \left[ \begin{array} { l l l l l } { \mathbf { 1 } } & { c } & { c ^ { 2 } } & { \cdots } & { c ^ { s - 1 } } \end{array} \right] } ,
$$

where powers of $c$ are interpreted in a componentwise manner, leads to considerable simplification. Denote

$$
\epsilon _ { k } = \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } - \frac { 1 } { k } , \qquad k = 1 , 2 , \ldots , 2 s ,
$$

so that $\epsilon _ { 1 } = \epsilon _ { 2 } = \cdot \cdot \cdot = \epsilon _ { s } = 0$ . Calculate the $( k , l )$ element of $V ^ { \prime } M V$ . This has the value

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 1 } ^ { s } c _ { i } ^ { k - 1 } \sum _ { j = 1 } ^ { s } c _ { j } ^ { l - 1 } \big ( b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } \big ) } & { } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } \frac { 1 } { l } b _ { i } c _ { i } ^ { k + l - 1 } + \sum _ { j = 1 } ^ { s } \frac { 1 } { k } b _ { j } c _ { j } ^ { k + l - 1 } - \frac { 1 } { k l } } & { } \\ { } & { = \displaystyle \frac { 1 } { l ( k + l ) } + \frac { 1 } { l } \epsilon _ { k + l } + \frac { 1 } { k ( k + l ) } + \frac { 1 } { k } \epsilon _ { k + l } - \frac { 1 } { k l } } \\ { } & { = \displaystyle \frac { k + l } { k l } \epsilon _ { k + l } . } \end{array}
$$

Thus,

$$
{ \boldsymbol { r } } ^ { \mathsf { T } } M V = { \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } \\ & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ & & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { \cdots } & { { \frac { 2 s - 2 } { ( s - 1 ) ^ { 2 } } } \epsilon _ { 2 s - 2 } } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } \\ & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } & { \cdots } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } & { { \frac { 2 s } { s ^ { 2 } } } \epsilon _ { 2 s } } \end{array} \right] } .
$$

A symmetric positive semi-definite matrix cannot have a zero diagonal element unless all the elements on the same row and column are also zero. Hence, we deduce that $\epsilon _ { i } = 0$ for $i = s + 1 , s + 2 , \ldots , 2 s - 1$ . Thus, the only way for $M$ to be positive semi-definite is that

$$
V ^ { \top } M V = \frac { 2 s } { s ^ { 2 } } \epsilon _ { 2 s } e _ { s } e _ { s } ^ { \top }
$$

and that

$$
\epsilon _ { 2 s } \geq 0 .
$$

Combining these remarks with a criterion for (358a), we state:

Theorem 358A A collocation Runge–Kutta method is algebraically stable if and only if the abscissae are zeros of a polynomial of the form

$$
\begin{array} { r } { P _ { s } ^ { * } - \theta P _ { s - 1 } ^ { * } , } \end{array}
$$

where $\theta \geq 0$ .

Proof. Because $\epsilon _ { i } = 0$ for $i = 1 , 2 , \ldots , 2 s - 1$ , it follows that

$$
\int _ { 0 } ^ { 1 } P ( x ) \phi ( x ) d x = 0 ,
$$

where $\phi ( x )$ is a polynomial of degree $s$ , with positive leading coefficient and zeros $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ and $P$ is any polynomial of degree not exceeding $s - 2$ . Furthermore, if $P$ is a polynomial of degree $s - 1$ and positive leading coefficient, the integral in (358c) has the same sign as $- \epsilon _ { 2 s }$ . Because of the orthogonality of $\phi$ and polynomials of degree less than $s - 1$ , $\phi$ is a positive constant multiple of (358b). Apart from a positive factor, we can now evaluate the integral in (358c), with $P ( x ) = P _ { s - 1 } ^ { * } ( x )$ ,

$$
\int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ( P _ { s } ^ { * } ( x ) - \theta P _ { s - 1 } ^ { * } ( x ) ) d x = - \theta \int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ^ { 2 } d x ,
$$

which has the opposite sign to $\theta$ .

A consequence of this result is that both Gauss and Radau IIA methods are algebraically stable. Many other methods used for the solution of stiff problems have stage order lower than $s$ and are therefore not collocation methods. A general characterization of algebraic stable methods is found by using a transformation based not on the Vandermonde matrix $V$ , but on a generalized Vandermonde matrix based on the polynomials that are essentially the same as $P _ { i } ^ { * }$ , for $i = 0 , 1 , 2 , \ldots , s - 1$ .

# 359 The $V$ and $W$ transformations

We refer to the transformation of $M$ using the Vandermonde matrix $V$ to form $V ^ { \prime } M V$ , as the $V$ transformation’. We now introduce the more sophisticated $W$ transformation.

We recall Corollary 356D, which enables us to confine our attention to irreducible methods in which $b ^ { \intercal }$ has only positive elements. Construct a sequence of polynomials $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ with degrees 0, 1, . . . , $s \mathrm { ~ - ~ } 1$ , respectively, which are orthonormal in the sense that

$$
\sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } , \qquad k , l = 1 , 2 , \ldots , s .
$$

We can assume that the leading coefficients are all positive. Define $W$ as the generalized Vandermonde matrix

$$
\begin{array} { r l } { W = [ P _ { 0 } ( c ) \quad P _ { 1 } ( c ) \quad \cdots \quad P _ { s - 1 } ( c ) ] } \\ & { \qquad = \left[ \begin{array} { c c c c } { P _ { 0 } ( c _ { 1 } ) } & { P _ { 1 } ( c _ { 1 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 1 } ) } \\ { P _ { 0 } ( c _ { 2 } ) } & { P _ { 1 } ( c _ { 2 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 2 } ) } \\ { \vdots } & { \vdots } & { \vdots } \\ { P _ { 0 } ( c _ { s } ) } & { P _ { 1 } ( c _ { s } ) } & { \cdots } & { P _ { s - 1 } ( c _ { s } ) } \end{array} \right] . } \end{array}
$$

This matrix can be constructed using the Gram–Schmidt process, or what is algebraically equivalent, from a QR factorization

$$
B ^ { 1 / 2 } V = ( B ^ { 1 / 2 } W ) R ,
$$

where $B ^ { 1 / 2 } = \mathrm { d i a g } ( \sqrt { b _ { 1 } } , \sqrt { b _ { 2 } } , \cdot \cdot \cdot , \sqrt { b _ { s } } )$ and $R$ is upper triangular with positive elements on the diagonal. Note that the coefficients in $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ can be read off from the columns of $R$ .

If $b ^ { \prime }$ and $c$ are weight and abscissa vectors for a Runge–Kutta method of order $p$ , then as long as $k + l \le p + 1$ , (359a) implies that

$$
\int _ { 0 } ^ { 1 } P _ { k - 1 } ( x ) P _ { l - 1 } ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } ,
$$

implying that $P _ { 0 }$ , $P _ { 1 }$ , . . . , $P _ { \left[ \left( p - 1 \right) / 2 \right] }$ are orthonormal with respect to integration on $[ 0 , 1 ]$ . This means that they are necessarily the normalized Legendre polynomials on this interval, given by

$$
P _ { k } ( z ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k - i } { \binom { k } { i } } { \binom { k + i } { i } } z ^ { i } .
$$

In particular, $P _ { 0 } ( x ) \ = \ 1$ and the first column of $W$ is $\mathbf { 1 }$ . Because of orthonormality, it follows that $\mathbf { 1 } ^ { \prime } B W = e _ { 1 } ^ { \mathsf { T } }$ .

We now focus our attention on the matrix $X = W ^ { \prime } B A W$ . This is significant because

$$
\begin{array} { r } { W ^ { \mathsf { T } } M W = X + X ^ { \mathsf { T } } - ( W ^ { \mathsf { T } } B \mathbf { 1 } ) ( \mathbf { 1 } ^ { \mathsf { T } } B W ) = ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) + ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) ^ { \mathsf { T } } . } \end{array}
$$

Because $M$ , and therefore $W ^ { \prime } M W$ , is the zero matrix for the Gauss method, it follows that $\begin{array} { r } { X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top } } \end{array}$ is skew-symmetric. Denote $X$ by $X _ { \mathrm { G } }$ in this special case. We now evaluate $X _ { \mathrm { G } }$ in full.

# Lemma 359A Let

$$
\begin{array} { r } { X _ { G } = W ^ { \top } B A W , } \end{array}
$$

where $A$ and $B = \mathrm { d i a g } ( b )$ are as for the Gauss method of order 2s. Also let

$$
\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } , \qquad k = 1 , 2 , \ldots , s - 1 .
$$

Then

$$
\begin{array} { r } { { \cal X } _ { G } = \left[ \begin{array} { c c c c c c c c } { \frac 1 2 } & { - \xi _ { 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { \xi _ { 2 } } & { 0 } & { - \xi _ { 3 } } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - \xi _ { s - 1 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { \xi _ { s - 1 } } & { 0 } \end{array} \right] . } \end{array}
$$

Proof. From linear combinations of identities included in the condition $E ( s , s )$ , given by (321c), we have

$$
\sum _ { i = 1 } ^ { s } \sum _ { j = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) a _ { i j } \psi ( c _ { j } ) = \int _ { 0 } ^ { 1 } \phi ( u ) \int _ { 0 } ^ { u } \psi ( v ) d v d u ,
$$

for polynomials $\phi$ and $\psi$ each with degree less than $s$ . Use the polynomials $\phi = P _ { k - 1 }$ , $\psi = P _ { l - 1 }$ and we have a formula for the $( k , l )$ element of $X _ { \mathrm { G } }$ . Add to this the result for $k$ and $\it l$ interchanged and use integration by parts. We have

$$
( X _ { \mathrm { G } } ) _ { k l } + ( X _ { \mathrm { G } } ) _ { l k } = \int _ { 0 } ^ { 1 } P _ { k - 1 } ( u ) d u \int _ { 0 } ^ { 1 } P _ { l - 1 } ( v ) d v = \delta _ { k 1 } \delta _ { l 1 } .
$$

This result determines the diagonal elements of $X _ { \mathrm { G } }$ , and also implies the skew-symmetric form of $X _ { \mathrm { G } } ~ - ~ \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top }$ . We now determine the form of the lower triangular elements. If $k > l + 1$ , the integral $\int _ { 0 } ^ { u } P _ { l - 1 } ( v ) d v$ has lower degree than $P _ { k - 1 }$ and is therefore orthogonal to it. Thus, in this case, $( X _ { \mathrm { G } } ) _ { k l } = 0$ . It remains to evaluate $( X _ { \mathrm { G } } ) _ { k , k - 1 }$ for $k = 1 , 2 , \ldots , s - 1$ . The integral $\int _ { 0 } ^ { u } P _ { k - 1 } ( v ) d v$ is a polynomial in $u$ of degree $k$ and can be written in the form $\theta P _ { k } ( u )$ added to a polynomial of degree less than $k$ . The integral of $P _ { k } ( u )$ multiplied by the polynomial of degree less than $k$ is zero, by orthogonality, and the integral reduces to

$$
\int _ { 0 } ^ { 1 } \theta P _ { k } ( u ) ^ { 2 } d u = \theta .
$$

is The value of $\sqrt { 2 k - 1 } \binom { 2 k - 2 } { k - 1 }$ $\theta$ can be found by noting that the coefficient of , with a similar formula for the leading coefficient of in $P _ { k - 1 } ( v )$ $P _ { k } ( u )$

Hence,

$$
( X _ { \mathrm { G } } ) _ { k , k - 1 } = \theta = { \frac { { \frac { 1 } { k } } { \sqrt { 2 k - 1 } } { \binom { 2 k - 2 } { k - 1 } } } { { \sqrt { 2 k + 1 } } { \binom { 2 k } { k } } } } = { \frac { 1 } { 2 { \sqrt { 4 k ^ { 2 } - 1 } } } } .
$$

The computation of elements of $X ~ = ~ W ^ { \top } B A W$ for any Runge–Kutta method, for which $W$ makes sense, will lead to the same $( k , l )$ elements as in $X _ { \mathrm { G } }$ as long as $k + l \le p + 1$ . We state this formally.

Corollary 359B Let $( A , b , c )$ denote a Runge–Kutta method for which $B =$ $\mathrm { d i a g } ( b )$ is positive definite and for which the abscissae are distinct. Define $W$ by (359b) and $X$ by $X = W ^ { \prime } B A W$ . Then $X _ { k l } ~ = ~ ( X _ { G } ) _ { k l }$ , as long as $k + l \le p + 1$ .

The $W$ transformation is related in an interesting way to the $C ( m )$ and $D ( m )$ conditions, which can be written in the equivalent forms

$$
\begin{array} { c c } { { C ( m ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } P _ { k - 1 } ( c _ { j } ) = \int _ { 0 } ^ { c _ { i } } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ i = 1 , 2 , \ldots , s , } } \\ { { D ( m ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) a _ { i j } = b _ { j } \int _ { c _ { j } } ^ { 1 } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ j = 1 , 2 , \ldots , s . } } \end{array}
$$

It follows from these observations that, if $B ( m )$ and $C ( m )$ are true, then the first $m$ columns of $X$ will be the same as for $X _ { \mathrm { G } }$ . Similarly, if $B ( m )$ and $D ( m )$ , then the first $m$ rows of $X$ and $X _ { \mathrm { G } }$ will agree.

Amongst the methods known to be algebraically stable, we have already encountered the Gauss and Radau IIA methods. We can extend this list to include further methods.

Theorem 359C The Gauss, Radau IA, Radau IIA and Lobatto IIIC methods are algebraically stable.

Proof. We have already settled the Gauss and Radau IIA cases, using the $V$ transformation, making use of the $C ( s )$ and $B ( p )$ conditions, as in Theorem 358A.

To prove the result for Radau IA methods, use the $D ( s )$ and $B ( 2 s - 1 )$ conditions:

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } & { } \\ { = \displaystyle \frac { 1 } { k } \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \displaystyle \frac { 1 } { l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ^ { l } ) c _ { i } ^ { k - 1 } - \displaystyle \frac { 1 } { k l } } & { } \\ { \displaystyle } & { = \displaystyle \frac { 1 } { k l } - \frac { k + l } { k l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } . } \end{array}
$$

The value of this expression is zero if $k + l \le 2 s - 1$ . Although it can be verified directly that the value is positive in the remaining case $k = l = s$ , it is enough to show that the $( 1 , 1 )$ element of $M$ is positive, because this will have the same sign as the only non-zero eigenvalue of the rank 1 matrix $V ^ { \prime } M V$ . We note that all values in the first column of $A$ are equal to $b _ { 1 }$ because these give the unique solution to the $D ( s )$ condition applied to the first column. Hence, we calculate the $( 1 , 1 )$ element of $M$ to be

$$
2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = b _ { 1 } ^ { 2 } > 0 .
$$

In the case of the Lobatto IIIC methods, we can use a combination of the $C ( s - 1 )$ and $D ( s - 1 )$ conditions to evaluate the $( k , l )$ and $( l , k )$ elements of $M$ , where $k \le s - 1$ and $l \leq s$ . The value of these elements is

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \frac { 1 } { k } \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = 0 . } } \end{array}
$$

The final step of the proof is the same as for the Radau IA case, because again $a _ { i 1 } = b _ { 1 }$ , for $i = 1 , 2 , \dots , s$ . 

The $V$ transformation was used to simplify questions concerning algebraic stability in Butcher (1975) and Burrage (1978). The $W$ transformation was introduced in Hairer and Wanner (1981, 1982). Recent results on the $W$ transformation, and especially application to symplectic methods, were presented in Hairer and Leone (2000) .

# Exercises 35

35.1 Show that a Runge–Kutta method with $R ( z ) ~ = ~ N ( z ) / D ( z )$ , where $N$ and $D$ have no common factors, cannot be A-stable unless the coefficients in $D ( z )$ alternate in sign.

35.2 Show that the error constant for the $( s - d , s )$ Pad´e approximation to the exponential function has sign $( - 1 ) ^ { s }$ . Deduce that, if $d > 0$ and $d = 3$ (mod 4) or $d = 0$ (mod 4), then $| R ( i y ) | > 0$ , for sufficiently small real $y$ .

35.3 Show that the implicit Runge–Kutta method with tableau

<table><tr><td>#云</td><td>A 2</td></tr><tr><td>1</td><td></td></tr><tr><td>1</td><td></td></tr><tr><td></td><td>1</td></tr></table>

is A-stable but not AN-stable.

35.4 For the $( 0 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 5$ .

35.5 For the $( 1 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 7$ .

# 36 Implementable Implicit Runge–Kutta Methods

360 Implementation of implicit Runge–Kutta methods

Because of the implicit nature of these methods, every step requires the solution of an algebraic system. For an $s$ -stage method with an $N$ -dimensional problem, there are $s N$ unknowns to evaluate and these satisfy $s N$ equations. If $f$ is nonlinear, then the large system of equations to be solved is also nonlinear. However, there are linear parts of it, and it may be possible to exploit this in their numerical solution. Let $A$ denote the coefficient matrix; then the stage values need to be computed as solutions to the system of equations

$$
\begin{array} { l } { { \displaystyle Y _ { 1 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 1 j } f ( Y _ { j } ) } . } \\ { ~ } \\ { { \displaystyle Y _ { 2 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 2 j } f ( Y _ { j } ) } . } \\ { { \displaystyle \quad \vdots \qquad } } \\ { { \displaystyle Y _ { s } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { s j } f ( Y _ { j } ) } . } \end{array}
$$

For an $N$ -dimensional differential equation system, this amounts to a system of $s N$ non-linear equations.

We consider how to solve these equations using a full Newton method. This requires going through the following steps:


<!-- chunk 0005: pages 281-350 -->
1. Compute approximations to $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ using information available at the start of the step. Denote these ‘predicted’ values by $Y _ { i } ^ { [ 0 ] }$ , $i = 1 , 2 , \dots , s$ .

2. Carry out a sequence of iterations leading to approximations $Y _ { i } ^ { \left[ k \right] }$ , for $k = 1 , 2 , \dots$ , $i = 1 , 2 , \dots , s$ . These are given by the formulae

$$
Y _ { i } ^ { [ k ] } = Y _ { i } ^ { [ k - 1 ] } - \Delta _ { i } ,
$$

where

$$
\sum _ { j = 1 } ^ { s } m _ { i j } \Delta _ { j } = \phi _ { i } , \qquad i = 1 , 2 , \ldots , s ,
$$

with

$$
\phi _ { i } = Y _ { i } ^ { [ k - 1 ] } - y _ { n - 1 } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ^ { [ k - 1 ] } )
$$

and

$$
m _ { i j } = \delta _ { i j } I - h a _ { i j } f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } ) .
$$

3. Test for convergence and terminate when each of $\lVert \Delta _ { 1 } \rVert$ , $| | \Delta _ { 2 } | |$ , . . . , $\| \Delta _ { s } \|$ are sufficiently small. Suppose that this happens in the computation of iteration $k$ .

4. Assign $Y _ { i } ^ { \left[ k \right] }$ to $Y _ { i }$ , for each $i = 1 , 2 , \dots , s$

In a practical calculation, it is usual to simplify this computation in various ways. Most importantly, the solution of (360a), preceded by the evaluation of the elements of $m _ { i j }$ which depend on $f ^ { \prime }$ evaluated at each stage and in each iteration, requires a large number of algebraic operations; these are to be avoided whenever possible.

A typical simplification is to replace the value of $f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } )$ by a constant approximation to this Jacobian matrix. This approximation is maintained at a fixed value over every iteration and over each stage, and possibly over many steps. This means that the $s N \times s N$ matrix with elements built up from the submatrices $m _ { i j }$ can be replaced by a matrix of the form

$$
I _ { s } \otimes I _ { N } - h A \otimes J ,
$$

where $J$ is the Jacobian approximation. The cost, measured solely in terms of linear algebra costs, divides into two components. First, the factorization of the matrix (360b), carried out from time to time during the computation, costs a small multiple of $s ^ { 3 } N ^ { 3 }$ floating point operations. Secondly, the solution of (360a) costs a small multiple of $s ^ { 2 } N ^ { 2 }$ arithmetic operations per iteration.

It is the aim of the study of implementable methods to lower the factors $s ^ { 3 }$ in the occasional part of the cost and to lower the factor $s ^ { 2 }$ in the ‘per iteration’ part of the cost.

# 361 Diagonally implicit Runge–Kutta methods

Because of the excessive cost in evaluating the stages in a fully implicit Runge– Kutta method, we consider the so-called ‘diagonally implicit Runge–Kutta’ or DIRK methods (Alexander, 1977). For these methods, the coefficient matrix $A$ has a lower triangular structure with equal elements on the diagonal. Note that sometimes these methods are referred to as ‘singly diagonally implicit’ or SDIRK, with DIRK methods not necessarily having equal diagonals. Earlier names for methods in this general class are semi-implicit Runge–Kutta methods (Butcher, 1965)and semi-explicit (Nørsett, 1974).

The advantage of these methods is that the stages can be evaluated sequentially rather than as one great implicit system. We consider here the derivation of some low order members of this class with a brief analysis of their stability regions.

To obtain order 2 with two stages, consider the tableau

$$
\frac { \lambda } { \left| \begin{array} { c c c } { \lambda } & { 0 } & { } \\ { c _ { 2 } - \lambda } & { \lambda } & { } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right. } .
$$

The order conditions are

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } = 1 , } \\ { b _ { 1 } \lambda + b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } , } \end{array}
$$

with solution $\begin{array} { r } { b _ { 1 } = \frac { 2 c _ { 2 } - 1 } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ , $\begin{array} { r } { b _ { 2 } = \frac { 1 - 2 \lambda } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ . The method is A-stable if $\lambda \geq \frac { 1 } { 4 }$ and L-stable if $\lambda = 1 \pm \textstyle { \frac { 1 } { 2 } } { \sqrt { 2 } }$ . A particularly attractive choice is $c _ { 2 } = 1 , \lambda = 1 - { \textstyle \frac { 1 } { 2 } } \sqrt { 2 }$ , for which the tableau is

$$
\frac { 1 - \frac 1 2 \sqrt 2 } { 1 } \left| \begin{array} { c c } { 1 - \frac 1 2 \sqrt { 2 } } & { 0 } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \end{array} \right. .
$$

For $s = p = 3$ , the stability function is given by

$$
R ( z ) = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } + ( \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ) z ^ { 3 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial is found to be

$$
\mathrm {  ~ \psi ~ } ( y ) = \biggl ( \frac { 1 } { 1 2 } - \lambda + 3 \lambda ^ { 2 } - 2 \lambda ^ { 3 } \biggr ) y ^ { 4 } + \biggl ( - \frac { 1 } { 3 6 } + \frac { \lambda } { 2 } - \frac { 1 3 \lambda ^ { 2 } } { 4 } + \frac { 2 8 \lambda ^ { 3 } } { 3 } - 1 2 \lambda ^ { 4 } + 6 \lambda ^ { 5 } \biggr ) y ^ { 6 } .
$$

For $E ( y ) \ge 0$ , for all $y > 0$ , it is necessary and sufficient for A-stability that $\lambda \in [ \textstyle { \frac { 1 } { 3 } } , \widetilde { \lambda } ]$ , where $\tilde { \lambda } \approx 1 . 0 6 8 5 7 9 0 2 1 3$ is a zero of the coefficient of $y ^ { 4 }$ in $E ( y )$ . For

L-stability there is only one possible choice in this interval: $\lambda \approx 0 . 4 3 5 8 6 6 5 2 1 5$ , a zero of the coefficient of $z ^ { 3 }$ in the numerator of $R ( z )$ . Assuming $\lambda$ is chosen as this value, a possible choice for the remaining coefficients is given by the tableau

<table><tr><td rowspan=1 colspan=1>入(1+λ)1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4（-6)²+16λ-1）(6λ²-20λ+5）λ</td></tr></table>

# 362 The importance of high stage order

The asymptotic error behaviour of a numerical method underlines the importance of the order $p$ in ensuring high accuracy at minimal computing cost, as long as sufficient accuracy is required. If, for two methods, the asymptotic local truncation errors are, respectively, $C _ { 1 } h ^ { p _ { 1 } + 1 }$ and $C _ { 2 } h ^ { p _ { 2 } + 1 }$ , where $p _ { 2 } > p _ { 1 }$ , then the second method will always be more efficient as long as $h$ is taken to be sufficiently small. This argument ignores the fact that the methods might have differing costs per step, and therefore the stepsizes that make the work done by the methods comparable might be vastly different. It also ignores the fact that $C _ { 1 }$ and $C _ { 2 }$ can have such values that, for moderate stepsizes, the first method may be more efficient. This argument also ignores the fact that it is not just local errors that matter, but rather the accumulated global error after many steps; from the global error point of view it is also true that high orders will always eventually win over low orders. This ignores the case of special problems where there might be a cancellation of errors, so that in effect the order is greater than it would be for a general problem.

If the stage order is significantly lower than the order, then the final result computed will have depended for its value on much less accurate answers evaluated along the way. For non-stiff problems this is not a serious difficulty, because the order conditions take into account the need for the effect of these internal errors to cancel each other out. Asymptotically this also happens for stiff problems, but the magnitude of the stepsize required to enjoy the benefits of this asymptotic behaviour may depend drastically on the nature of the problem and on some quantitative measure of its stiffness.

To investigate this question, Prothero and Robinson (1974) considered a special family of problems of the form

$$
y ^ { \prime } ( x ) = L { \bigl ( } y ( x ) - g ( x ) { \bigr ) } + g ^ { \prime } ( x ) , \qquad y ( x _ { 0 } ) = g ( x _ { 0 } ) ,
$$

where $L$ is a negative constant and $g$ is a smooth function that varies at a moderate rate. We first look at the extreme ‘non-stiff’ case $L = 0$ . In this case the Prothero and Robinson problem becomes

$$
y ^ { \prime } ( x ) = g ^ { \prime } ( x ) ,
$$

and the defining equations for the solution computed by the Runge–Kutta method are

$$
\begin{array} { l } { { Y = y _ { n - 1 } \mathbf { 1 } + h A G ^ { \prime } , } } \\ { { y _ { n } = y _ { 0 } + h b ^ { \top } G ^ { \prime } , } } \end{array}
$$

where $G ^ { \prime }$ is the subvector made up from the values of $g ^ { \prime } ( x )$ evaluated at the stage values. We also write $G$ for the corresponding vector of $G ( x )$ values. Thus

$$
G = \left[ \begin{array} { c } { g ( x _ { n - 1 } + h c _ { 1 } ) } \\ { g ( x _ { n - 1 } + h c _ { 2 } ) } \\ { \vdots } \\ { g ( x _ { n - 1 } + h c _ { s } ) } \end{array} \right] , \qquad G ^ { \prime } = \left[ \begin{array} { c } { g ^ { \prime } ( x _ { n - 1 } + h c _ { 1 } ) } \\ { g ^ { \prime } ( x _ { n - 1 } + h c _ { 2 } ) } \\ { \vdots } \\ { g ^ { \prime } ( x _ { n - 1 } + h c _ { s } ) } \end{array} \right] .
$$

We see that the accuracy of the computation of $y _ { n }$ , as an approximation to $y ( x _ { n } )$ , is independent of the $A$ matrix and is determined by the accuracy of the quadrature formula

$$
\sum _ { i = 1 } ^ { s } b _ { i } \phi ^ { \prime } ( c _ { i } ) \approx \int _ { 0 } ^ { 1 } \phi ^ { \prime } ( \xi ) d \xi ,
$$

which we assume to be of order $p$ . This means that (362c) is exact for $\phi$ a polynomial of degree up to $p$ , and the error will be approximately

$$
{ \frac { 1 } { p ! } } \left( { \frac { 1 } { p + 1 } } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { p } \right) \phi ^ { ( p + 1 ) } ( 0 )
$$

and the error in the Runge–Kutta method for this problem will be

$$
\frac { h ^ { p + 1 } } { p ! } \left( \frac { 1 } { p + 1 } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { p } \right) g ^ { ( p + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) .
$$

Now return to the full Prothero and Robinson problem

$$
y ^ { \prime } ( x ) = L \Bigl ( y ( x ) - g ( x ) \Bigr ) + g ^ { \prime } ( x ) ,
$$

for which the computed results satisfy

$$
\begin{array} { r } { \begin{array} { r l } & { Y = y _ { n - 1 } \mathbf { 1 } + h A \left( L ( Y - G ) + G ^ { \prime } \right) , } \\ & { y _ { n } = y _ { n - 1 } + h b ^ { \top } \left( L ( Y - G ) + G ^ { \prime } \right) . } \end{array} } \end{array}
$$

Eliminate $Y$ , and we find

$$
y _ { n } = \Big ( 1 + h L b ^ { \top } ( I - h L A ) ^ { - 1 } { \bf 1 } \Big ) y _ { n - 1 } + h b ^ { \top } ( I - h L A ) ^ { - 1 } ( G ^ { \prime } - L G ) ,
$$

where the coefficient of $y _ { n - 1 }$ is seen to be the stability function value

$$
R ( h L ) = 1 + h L b ^ { \top } ( I - h L A ) ^ { - 1 } \mathbf { 1 } .
$$

By rearranging this expression we see that

$$
\begin{array} { r l } & { y _ { n } = R ( h L ) \Big ( y _ { n - 1 } - g ( x _ { n - 1 } ) \Big ) + g ( x _ { n - 1 } ) + h b ^ { \top } G ^ { \prime } } \\ & { \qquad + h L b ^ { \top } ( I - h L A ) ^ { - 1 } \Big ( h A G ^ { \prime } - ( G - g ( x _ { n - 1 } ) ) \Big ) } \\ & { \qquad = R ( h L ) \Big ( y _ { n - 1 } - g ( x _ { n - 1 } ) \Big ) + g ( x _ { n } ) - \epsilon _ { 0 } - h L b ^ { \top } ( I - h L A ) ^ { - 1 } \epsilon , } \end{array}
$$

where

$$
\epsilon _ { 0 } = h \int _ { 0 } ^ { 1 } g ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi - h \sum _ { i = 1 } ^ { s } b _ { i } g ^ { \prime } ( x _ { n - 1 } + h c _ { i } )
$$

is the non-stiff error term given approximately by (362d) and $\epsilon$ is the vector of errors in the individual stages with component $i$ given by

$$
h \int _ { 0 } ^ { c _ { i } } g ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi - h \sum _ { j = 1 } ^ { s } a _ { i j } g ^ { \prime } ( x _ { n - 1 } + h c _ { j } ) .
$$

If $L$ has a moderate size, then $h L b ^ { \mathsf { T } } ( I - h L A ) ^ { - 1 } \epsilon$ can be expanded in the form

$$
h L b ^ { \mathsf { T } } ( I + h L A + h ^ { 2 } L ^ { 2 } A ^ { 2 } + \cdot \cdot \cdot ) \epsilon
$$

and error behaviour of order $p$ can be verified term by term.

On the other hand, if $h L$ is large, a more realistic idea of the error is found using the expansion

$$
( I - h L A ) ^ { - 1 } = - \frac { 1 } { h L } A ^ { - 1 } - \frac { 1 } { h ^ { 2 } L ^ { 2 } } A ^ { - 2 } - \cdot \cdot \cdot ,
$$

and we obtain an approximation to the error, $g ( x _ { n } ) - y _ { n }$ , given by

$$
\begin{array} { c } { { g ( x _ { n } ) - y _ { n } = R ( h L ) \Big ( g ( x _ { n - 1 } ) - y _ { n - 1 } \Big ) + \epsilon _ { 0 } } } \\ { { - b ^ { \top } A ^ { - 1 } \epsilon - h ^ { - 1 } L ^ { - 1 } b ^ { \top } A ^ { - 2 } \epsilon - h ^ { - 2 } L ^ { - 2 } b ^ { \top } A ^ { - 3 } \epsilon - \cdot \cdot \cdot . . ~ . } } \end{array}
$$

Even though the stage order may be low, the final stage may have order $p$ . This will happen, for example, if the final row of $A$ is identical to the vector $b ^ { \prime }$ . In this special case, the term $b ^ { \scriptscriptstyle 1 } A ^ { - 1 } \epsilon$ will cancel $\epsilon _ { 0 }$ .

In other cases, the contributions from $b ^ { \intercal } A ^ { - 1 } \epsilon$ might dominate $\epsilon _ { 0 }$ , if the stage order is less than the order.

Define

$$
\eta _ { n } = \epsilon _ { 0 } + h L b ^ { \dag } ( I - h L A ) ^ { - 1 } \epsilon , \qquad n > 0 ,
$$

with $\eta _ { 0 }$ defined as the initial error $g ( x _ { 0 } ) - y _ { 0 }$ . The accumulated truncation error after $n$ steps is equal to

$$
\sum _ { i = 0 } ^ { n } R ( h L ) ^ { n - i } \eta _ { i } \approx \sum _ { i = 0 } ^ { n } R ( \infty ) ^ { n - i } \eta _ { i } .
$$

There are three important cases which arise in a number of widely use methods. If $R ( \infty ) = 0$ , as in the Radau IA, Radau IIA and Lobatto IIIC methods, or for that matter in any L-stable method, then we can regard the global truncation error as being just the error in the final step. Thus, if the local error is $O ( h ^ { q + 1 } )$ then the global error would also be $O ( h ^ { q + 1 } )$ . On the other hand, for the Gauss method with $s$ stages, $R ( \infty ) = ( - 1 ) ^ { s }$ . For the methods for which $R ( \infty ) = 1$ , then we can further approximate the global error as the integral of the local truncation error multiplied by $h ^ { - 1 }$ . Hence, a local error $O ( h ^ { q + 1 } )$ would imply a global error of $O ( h ^ { q } )$ . In the cases for which $R ( \infty ) = - 1$ we would expect the global error to be $O ( h ^ { q + 1 } )$ , because of cancellation of $\eta _ { i }$ over alternate steps.

We explore a number of example methods to see what can be expected for both local and global error behaviour.

For the Gauss methods, for which $p = 2 s$ , we can approximate $\epsilon _ { \mathrm { 0 } }$ by

$$
\frac { h ^ { 2 s + 1 } } { ( 2 s ) ! } \left( \frac { 1 } { 2 s + 1 } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 s } \right) g ^ { ( 2 s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 2 } ) ,
$$

which equals

$$
\frac { h ^ { 2 s + 1 } s ! ^ { 4 } } { ( 2 s ) ! ^ { 3 } ( 2 s + 1 ) } g ^ { ( 2 s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 2 } ) .
$$

Now consider the term $- b ^ { \intercal } A ^ { - 1 } \epsilon$ . This is found to equal

$$
\frac { h ^ { s + 1 } s ! } { ( 2 s ) ! ( s + 1 ) } g ^ { ( s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { s + 2 } ) ,
$$

which, if $| h L |$ is large, dominates (362e).

We also consider the important case of the Radau IIA methods. In this case $\epsilon _ { 0 }$ is approximately

$$
\begin{array} { r l r } {  { \frac { h ^ { 2 s } } { ( 2 s - 1 ) ! } ( \frac { 1 } { 2 s } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 s - 1 } ) g ^ { ( 2 s ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 1 } ) } } \\ & { } & \\ & { } & { = - \frac { h ^ { 2 s } s ! ( s - 1 ) ! ^ { 3 } } { 2 ( 2 s - 1 ) ! ^ { 3 } } g ^ { ( 2 s ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 1 } ) . } \end{array}
$$

As we have remarked, for $| h L |$ large, this term is cancelled by $- b ^ { \intercal } A ^ { - 1 } \epsilon$ . Hence, the local truncation error can be approximated in this case by $- ( h L ) ^ { - 1 } b ^ { \mathsf { T } } A ^ { - 2 } \epsilon .$ . The value of this is

$$
\frac { s ! } { ( s + 1 ) ( 2 s - 1 ) ! } \frac { 1 } { h L } g ^ { ( s ) } ( x _ { n - 1 } ) h ^ { s } + O ( L ^ { - 1 } h ^ { s } ) .
$$

To summarize: for very stiff problems and moderate stepsizes, a combination modelled for the Prothero–Robinson problem by a high value of $h L$ , the stage order, rather than the classical order, plays a crucial role in determining the error behaviour. For this reason, we consider criteria other than superconvergence as important criteria in the identification of suitable methods for the solution of stiff problems. In particular, we look for methods that are capable of cheap implementation.

# 363 Singly implicit methods

We consider methods for which the stage order $q$ and the order are related by $p = q = s$ . To make the methods cheaply implementable, we also assume that

$$
\sigma ( A ) = \{ \lambda \} .
$$

The detailed study of methods for which $A$ has a one-point spectrum and for which $q \geq p - 1$ began with Burrage (1978). The special case $q = p$ was further developed in Butcher (1979), and this led to the implementation of STRIDE described in Burrage, Butcher and Chipman (1980).

Given $q = p$ and (363a), there will be a constraint on the abscissae of the method. To explore this, write down the $C ( s )$ conditions

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad i , k = 1 , 2 , \ldots , s ,
$$

or, more compactly,

$$
A c ^ { k - 1 } = \frac { 1 } { k } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

where $c ^ { k }$ denotes the component-by-component power.

We can now evaluate $A ^ { k - 1 } \mathbf { 1 }$ by induction. In fact,

$$
A ^ { k } \mathbf { 1 } = { \frac { 1 } { k ! } } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

because the case $k = 1$ is just (363b), also with $k = 1$ ; and the case $k > 1$ follows from (363c) with $k$ replaced by $k - 1$ and from (363b).

Because of (363a) and the Cayley–Hamilton theorem, we have

$$
( A - \lambda I ) ^ { s } = 0 .
$$

Laguerre polynomials $L _ { s }$ for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S L(S）</td></tr><tr><td>1 1 -</td></tr><tr><td>2 1 1 + s</td></tr><tr><td>北 3 3 1 1 + 1-6 2-35-3 5</td></tr><tr><td>4 1 + 4</td></tr><tr><td>124524 5 1 1 + 1 m5 120 S</td></tr><tr><td>6 6 1 1 十 1 1 6 20 720</td></tr><tr><td>中 10336° 583524 7 s² 7 5 7 6 1 57 7 1 十 m 4 40 十 720 5040 1</td></tr><tr><td>2 8 14g2 五 1 8 + + 7 × 7 1 1 s 7 + 15 180 630</td></tr></table>

Post-multiply by $\mathbf { 1 }$ and expand using the binomial theorem, and we find

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } A ^ { i } \mathbf { 1 } = \boldsymbol { 0 } .
$$

Using (363c), we find that

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } \frac { 1 } { i ! } c ^ { i } = 0 .
$$

This must hold for each component separately so that, for $i = 1 , 2 , \dots , s$ , $c _ { i } / \lambda$ is a zero of

$$
\sum _ { i = 0 } ^ { s } { \binom { s } { i } } ( - 1 ) ^ { i } \frac { ( - \xi ) ^ { i } } { i ! } .
$$

However, this is just the Laguerre polynomial of degree $s$ , usually denoted by $L _ { s } ( \xi )$ , and it is known that all its zeros are real and positive. For convenience, expressions for these polynomials, up to degree 8, are listed in Table 363(I) and approximations to the zeros are listed in Table 363(II). We saw in Subsection 361 that for $\lambda = \xi ^ { - 1 }$ for the case of three doubly underlined zeros of orders 2 and 3, L-stability is achieved. Double underlining to show similar choices for other orders is continued in the table and these are the only possibilities that exist (Wanner, Hairer and Nørsett, 1978). This means that there are no L-stable methods $^ -$ and in fact there is not even an A-stable method $-$ with $s = p = 7$ or with $s = p > 8$ . Even though fully L-stable methods are confined to the eight cases indicated in this table, there are other choices of $\lambda = \xi ^ { - 1 }$ that give stability which is acceptable for many problems. In each of the values of $\xi$ for which there is a single underline, the method is $\mathrm { A } ( \alpha )$ -stable with $\alpha \geq 1 . 5 5 \approx 8 9 ^ { \circ }$ .

Zeros of Laguerre polynomials for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S</td><td>$1,...,Ss</td><td></td><td></td><td></td></tr><tr><td>1</td><td>1.0000000000</td><td></td><td></td><td></td></tr><tr><td>2</td><td>0.5857864376</td><td>3.4142135624</td><td></td><td></td></tr><tr><td>3</td><td>0.4157745568</td><td>2.2942803603</td><td>6.2899450829</td><td></td></tr><tr><td>4</td><td>0.3225476896</td><td>1.7457611012</td><td>4.5366202969</td><td>9.3950709123</td></tr><tr><td>5</td><td>0.2635603197</td><td>1.4134030591</td><td>3.5964257710</td><td>7.0858100059</td></tr><tr><td>6</td><td>12.6408008443</td><td></td><td></td><td></td></tr><tr><td></td><td>0.2228466042</td><td>1.1889321017</td><td>2.9927363261</td><td>5.7751435691</td></tr><tr><td></td><td>9.8374674184</td><td>15.9828739806</td><td></td><td></td></tr><tr><td>7</td><td>0.1930436766</td><td>1.0266648953</td><td>2.5678767450</td><td>4.9003530845</td></tr><tr><td></td><td>8.1821534446</td><td>12.7341802918</td><td>19.3957278623</td><td></td></tr><tr><td>8</td><td>0.1702796323</td><td>0.9037017768</td><td>2.2510866299</td><td>4.2667001703</td></tr><tr><td></td><td>7.0459054024</td><td>10.7585160102</td><td>15.7406786413</td><td>22.8631317369</td></tr></table>

The key to the efficient implementation of singly implicit methods is the similarity transformation matrix that transforms the coefficient matrix to lower triangular form. Let $T$ denote the matrix with $( i , j )$ element

$$
t _ { i j } = L _ { j - 1 } ( \xi _ { i } ) , \qquad i , j = 1 , 2 , \ldots , s .
$$

The principal properties of $T$ and its relationship to $A$ are as follows:

Theorem 363A The $( i , j )$ element of $T ^ { - 1 }$ is equal to

$$
\frac { \xi _ { j } } { s ^ { 2 } L _ { s - 1 } ( \xi _ { j } ) ^ { 2 } } L _ { i - 1 } ( \xi _ { j } ) .
$$

Let $\widetilde { A }$ denote $T ^ { - 1 } A T$ ; then

$$
\widetilde { A } = \lambda \left[ \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 1 } & { 1 } \end{array} \right] .
$$

Proof. To prove (363d), use the Christoffel–Darboux formula for Laguerre polynomials in the form

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( x ) L _ { k } ( y ) = \frac s { x - y } \big ( L _ { s } ( y ) L _ { s - 1 } ( x ) - L _ { s } ( x ) L _ { s - 1 } ( y ) \big ) .
$$

For $i \neq j$ , substitute $x = \xi _ { i } , y = \xi _ { j }$ to find that rows $i$ and $j$ of $T$ are orthogonal. To evaluate the inner product of row $i$ with itself, substitute $y = \xi _ { i }$ and take the limit as $x \to \xi _ { i }$ . It is found that

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( \xi _ { k } ) ^ { 2 } = - s L _ { s } ^ { \prime } ( \xi _ { i } ) L _ { s - 1 } ( \xi _ { i } ) = \frac { s ^ { 2 } L _ { s - 1 } ( \xi _ { i } ) ^ { 2 } } { \xi _ { i } } .
$$

The value of $T T ^ { \rvert }$ as a diagonal matrix with $( i , i )$ element given by (363f) is equivalent to (363d).

The formula for $\widetilde { A }$ is verified by evaluating

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( \xi _ { j } ) = \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( c _ { j } / \lambda ) } \\ { = \displaystyle \int _ { 0 } ^ { \lambda \xi _ { i } } L _ { k - 1 } ( c _ { j } / \lambda ) d t } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } L _ { k - 1 } ( t ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d t } \\ { = \lambda ( L _ { k - 1 } ( \xi _ { i } ) - L _ { k } ( \xi _ { i } ) ) d t , } \end{array}
$$

where we have used known properties of Laguerre polynomials. The value of this sum is equivalent to (363e). 

For convenience we sometimes write

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right] ,
$$

so that (363e) can be written

$$
{ \widetilde { A } } = \lambda ( I - J ) .
$$

We now consider the possible A-stability or L-stability of singly implicit methods. This hinges on the behaviour of the rational functions

$$
R ( z ) = { \frac { N ( z ) } { ( 1 - \lambda z ) ^ { s } } } ,
$$

where the degree of the polynomial $N ( z )$ is no more than $s$ , and where

$$
N ( z ) = \exp ( z ) ( 1 - \lambda z ) ^ { s } + O ( z ^ { s + 1 } ) .
$$

We can obtain a formula for $N ( z )$ as follows:

$$
N ( z ) = \sum _ { i = 0 } ^ { s - i } ( - \lambda ) ^ { i } L _ { s } ^ { ( s - i ) } \left( \frac { 1 } { \lambda } \right) z ^ { i } ,
$$

where $L _ { n } ^ { ( m ) }$ denotes the $m$ -fold derivative of $L _ { n }$ , rather than a generalized Laguerre polynomial. To verify the L-stability of particular choices of $s$ and $\lambda$ , we note that all poles of $N ( z ) / ( 1 - \lambda z ) ^ { s }$ are in the right half-plane. Hence, it is necessary only to test that $| D ( z ) | ^ { 2 } - | ( 1 - \lambda z ) ^ { s } | ^ { 2 } \ge 0$ , whenever $z$ is on the imaginary axis. Write $z = i y$ and we find the ‘E-polynomial’ defined in this case as

$$
E ( y ) = ( 1 + \lambda ^ { 2 } y ^ { 2 } ) ^ { s } - N ( i y ) N ( - i y ) ,
$$

with $E ( y ) \ge 0$ for all real $y$ as the condition for A-stability. Although Astability for $s = p$ is confined to the cases indicated in Table 363(II), it will be seen in the next subsection that higher values of $s$ can lead to additional possibilities.

We conclude this subsection by constructing the two-stage L-stable singly implicit method of order 2. From the formulae for the first few Laguerre polynomials,

$$
L _ { 0 } ( x ) = 1 , \quad L _ { 1 } ( x ) = 1 - x , \quad L _ { 2 } ( x ) = 1 - 2 x + \frac { 1 } { 2 } x ^ { 2 } ,
$$

we find the values of $\xi _ { 1 }$ and $\xi _ { 2 }$ , and evaluate the matrices $T$ and $T ^ { - 1 }$ . We have

$$
\xi _ { 1 } = 2 - \sqrt { 2 } , \qquad \xi _ { 2 } = 2 + \sqrt { 2 }
$$

and

$$
\begin{array} { r } { \mathrm { ~  ~ { ~ \sigma ~ } ~ } ^ { \prime } = \left[ \begin{array} { l l } { L _ { 0 } ( \xi _ { 1 } ) } & { L _ { 1 } ( \xi _ { 1 } ) } \\ { L _ { 0 } ( \xi _ { 2 } ) } & { L _ { 1 } ( \xi _ { 2 } ) } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { - 1 + \sqrt { 2 } } \\ { 1 } & { - 1 - \sqrt { 2 } } \end{array} \right] , \quad T ^ { - 1 } = \left[ \begin{array} { l l } { \frac { 1 } { 2 } + \frac { \sqrt { 2 } } { 4 } } & { \frac { 1 } { 2 } - \frac { \sqrt { 2 } } { 4 } } \\ { \frac { \sqrt { 2 } } { 4 } } & { - \frac { \sqrt { 2 } } { 4 } } \end{array} \right] . } \end{array}
$$

For L-stability, choose $\begin{array} { r } { \lambda = \xi _ { 2 } ^ { - 1 } = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ , and we evaluate $A = \lambda T ( I - J ) T ^ { - 1 }$ to give the tableau

$$
{ \frac { 3 - 2 { \sqrt { 2 } } } { 1 } } { \frac { \frac { 5 } { 4 } - { \frac { 3 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } + { \frac { 1 } { 4 } } { \sqrt { 2 } } } } { \frac { \frac { 7 } { 4 } - { \frac { 5 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } - { \frac { 1 } { 4 } } { \sqrt { 2 } } } }  .
$$

In the implementation of this, or any other, singly implicit method, the actual entries in this tableau are not explicitly used. To emphasize this point, we look in detail at a single Newton iteration for this method. Let $M = I - h \lambda f ^ { \prime } ( y _ { n - 1 } )$ . Here the Jacobian matrix $f ^ { \prime }$ is supposed to have been evaluated at the start of the current step. In practice, a Jacobian evaluated at an earlier time value might give satisfactory performance, but we do not dwell on this point here. If the method were to be implemented with no special use made of its singly implicit structure, then we would need, instead of the $N \times N$ matrix $M$ , a $2 N \times 2 N$ matrix $\widetilde { M }$ given by

$$
\widetilde { \cal M } = \left[ \begin{array} { c c } { { I - h a _ { 1 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { - h a _ { 1 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \\ { { - h a _ { 2 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { I - h a _ { 2 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \end{array} \right] .
$$

In this ‘fully implicit’ situation, a single iteration would start with the input approximation $y _ { n - 1 }$ and existing approximations to the stage values and stage derivatives $Y _ { 1 }$ , $Y _ { 2 }$ , $h F _ { 1 }$ and $h F _ { 2 }$ . It will be assumed that these are consistent with the requirements that

$$
Y _ { 1 } = y _ { n - 1 } + a _ { 1 1 } h F _ { 1 } + a _ { 1 2 } h F _ { 2 } , \quad Y _ { 2 } = y _ { n - 1 } + a _ { 2 1 } h F _ { 1 } + a _ { 2 2 } h F _ { 2 } ,
$$

and the iteration process will always leave these conditions intact.

# 364 Generalizations of singly implicit methods

In an attempt to improve the performance of existing singly implicit methods, Butcher and Cash (1990) considered the possibility of adding additional diagonally implicit stages. For example, if $s ~ = ~ p + 1$ is chosen, then the coefficient matrix has the form

$$
\begin{array} { r } { A = \left[ \begin{array} { c c } { \lambda \widehat { A } } & { 0 } \\ { b ^ { \top } } & { \lambda } \end{array} \right] , } \end{array}
$$

where $\widehat { A }$ is the matrix

$$
{ \widehat { A } } = T ( I - J ) T ^ { - 1 } .
$$

An appropriate choice of $\lambda$ is made by balancing various considerations. The first of these is good stability, and the second is a low error constant. Minor considerations would be convenience, the avoidance of coefficients with abnormally large magnitudes or with negative signs, where possible, and a preference for methods in which the $c _ { i }$ lie in $[ 0 , 1 ]$ . We illustrate these ideas for the case $p = 2$ and $s = 3$ , for which the general form for a method would be

<table><tr><td>入(2-√2) 入(2+√2)</td><td colspan="3">入(1-√2) 入(1+√②)</td><td>&gt;(1-√2) 入(1+1√②)</td><td>0 0</td></tr><tr><td rowspan="3">1</td><td>2+3√2_ λ(1+√2) 4</td><td>2 2 8</td><td>2-3√2_(1-√2) 4</td><td>3 2</td><td rowspan="3">入 入</td></tr><tr><td>2+3√2</td><td>入(1+√2)</td><td>2-3√2</td><td></td></tr><tr><td>4</td><td>2 2 8</td><td>4</td><td>入(1-√2) 点 + 2</td></tr></table>

![](images/c0b1581105a7e8352a8baf7e761a8469c17426adeb496aeaacbfbe83a5eded4e.jpg)  
Error constant $C ( \lambda )$ for $\lambda \in [ 0 . 1 , 0 . 5 ]$

The only choice available is the value of $\lambda$ , and we consider the consequence of making various choices for this number. The first criterion is that the method should be A-stable, and we analyse this by calculating the stability function

$$
R ( z ) = \frac { N ( z ) } { D ( z ) } = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial

$$
\begin{array} { r } { E ( y ) = | D ( i y ) | ^ { 2 } - | N ( i y ) | ^ { 2 } = \Big ( 3 \lambda ^ { 4 } - \big ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } \big ) ^ { 2 } \Big ) y ^ { 4 } + \lambda ^ { 6 } y ^ { 6 } . } \end{array}
$$

For A-stability, the coefficient of $y ^ { 4 }$ must be non-negative. The condition for this is that

$$
\frac { 3 - { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } \leq \lambda \leq \frac { 3 + { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } ,
$$

or that $\lambda$ lies in the interval [0.180425, 2.185600]. The error constant $C ( \lambda )$ , defined by $\exp ( z ) - R ( z ) = C ( \lambda ) z ^ { 3 } + O ( z ^ { 4 } )$ , is found to be

$$
C ( \lambda ) = \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ,
$$

and takes on values for $\lambda \in [ 0 . 1 , 0 . 5 ]$ , as shown in Figure 364(i).

The value of $b _ { 1 }$ is positive for $\lambda > 0 . 1 2 5 4 4 1$ . Furthermore $b _ { 2 }$ is positive for $\lambda < 0 . 3 6 4 3 3 5$ . Since $b _ { 1 } + b _ { 2 } + \lambda = 1$ , we obtain moderately sized values of all components of $b ^ { \top }$ if $\lambda \in [ 0 . 1 2 5 4 4 1 , 0 . 3 6 4 3 3 5$ ]. The requirement that $c _ { 1 }$ and $c _ { 2 }$ lie in $( 0 , 1 )$ is satisfied if $\lambda < ( 2 - \sqrt { 2 } ) ^ { - 1 } \approx 0 . 2 9 2 8 9 3$ . Leaving aside the question of convenience, we should perhaps choose $\lambda \approx 0 . 1 8 0 4 2 5$ so that the error constant is small, the method is A-stable, and the other minor considerations are all satisfied. Convenience might suggest an alternative value $\textstyle \lambda = { \frac { 1 } { 5 } }$ .

# 365 Effective order and DESIRE methods

An alternative way of forcing singly implicit methods to be more appropriate for practical computation is to generalize the order conditions. This has to be done without lowering achievable accuracy, and the use of effective order is indicated. Effective order is discussed in a general setting in Subsection 389 but, for methods with high stage order, a simpler analysis is possible.

Suppose that the quantities passed from one step to the next are not necessarily intended to be highly accurate approximations to the exact solution, but rather to modified quantities related to the exact result by weighted Taylor series. For example, the input to step $_ { n }$ might be an approximation to

$$
y ( x _ { n - 1 } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n - 1 } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n - 1 } ) .
$$

We could regard a numerical method, which produces an output equal to

$$
y _ { n } = y ( x _ { n } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n } ) + O ( h ^ { p + 1 } ) ,
$$

as a satisfactory alternative to a method of classical order $p$ .

We explore this idea through the example of the effective order generalization of the L-stable order 2 singly implicit method with the tableau (363g). For this method, the abscissae are necessarily equal to $3 - 2 { \sqrt { 2 } }$ and $^ { 1 }$ , which are quite satisfactory for computation. However, we consider other choices, because in the more complicated cases with $s = p > 2$ , at least one of the abscissae is outside the interval $[ 0 , 1 ]$ , for A-stability.

If the method is required to have only effective order 2, then we can assume that the incoming and outgoing approximations are equal to

$$
\begin{array} { c } { { y _ { n - 1 } = y ( x _ { n - 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { p + 1 } ) , } } \\ { { y _ { n } = y ( x _ { n } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n } ) + O ( h ^ { p + 1 } ) , } } \end{array}
$$

respectively. Suppose that the stage values are required to satisfy

$$
Y _ { 1 } = y ( x _ { n - 1 } + h c _ { 1 } ) + O ( h ^ { 3 } ) , \qquad Y _ { 2 } = y ( x _ { n - 1 } + h c _ { 2 } ) + O ( h ^ { 3 } ) ,
$$

with corresponding approximations for the stage derivatives. In deriving the order conditions, it can be assumed, without loss of generality, that $n = 1$ . The order conditions for the two stages and for the output approximation $y _ { n } = y _ { 1 }$ are

$$
\begin{array} { r l } & { y ( x _ { 0 } + h c _ { 1 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h \alpha _ { 1 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h \alpha _ { 1 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 0 } + h c _ { 2 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h a _ { 2 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h a _ { 2 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 1 } ) } \\ & { \qquad = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h b _ { 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h b _ { 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) . } \end{array}
$$

These can be converted into algebraic relations on the various free parameters by expanding by Taylor series about $x _ { 0 }$ and equating coefficients of $h y ^ { \prime } ( x _ { 0 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } )$ . This gives the conditions

$$
\begin{array} { c } { { c _ { 1 } = \alpha _ { 1 } + a _ { 1 1 } + a _ { 1 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 1 } ^ { 2 } = \alpha _ { 2 } + a _ { 1 1 } c _ { 1 } + a _ { 1 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { c _ { 2 } = \alpha _ { 1 } + a _ { 2 1 } + a _ { 2 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = \alpha _ { 2 } + a _ { 2 1 } c _ { 1 } + a _ { 2 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { { 1 + \alpha _ { 1 } = \alpha _ { 1 } + b _ { 1 } + b _ { 2 } , } } } \\ { { { { \frac { 1 } { 2 } + \alpha _ { 1 } + \alpha _ { 2 } = \alpha _ { 2 } + b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } . } } } } \end{array}
$$

Because of the single-implicitness condition $\sigma ( A ) = \{ \lambda \}$ , we also have

$$
\begin{array} { r } { a _ { 1 1 } + a _ { 2 2 } = 2 \lambda , } \\ { a _ { 1 1 } a _ { 2 2 } - a _ { 2 1 } a _ { 1 2 } = \lambda ^ { 2 } . } \end{array}
$$

Assuming that $c _ { 1 }$ and $c _ { 2 }$ are distinct, a solution to these equations always exists, and it leads to the values

$$
\begin{array} { r } { \alpha _ { 1 } = \frac 1 2 ( c _ { 1 } + c _ { 2 } ) - 2 \lambda , \quad \alpha _ { 2 } = \frac 1 2 c _ { 1 } c _ { 2 } - \lambda ( c _ { 1 } + c _ { 2 } ) + \lambda ^ { 2 } , } \end{array}
$$

together with the tableau

$$
\frac { c _ { 1 } \ { \boxed { \begin{array} { r l r l } { { c _ { 2 } } } & { { - \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda + \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } & & { \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } \end{array} } } } { \frac { \lambda } { c _ { 2 } } } } & { \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } { \frac { \lambda } { c _ { 2 } } + \frac { 2 \lambda - \frac { 1 } { 2 } } { c _ { 2 } - c _ { 1 } } }  &  .
$$

In the special case $c ^ { \mathsf { T } } = [ 0 , 1 ]$ , with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ for L-stability, we find $\begin{array} { r } { \alpha _ { 1 } = \sqrt { 2 } - \frac { 3 } { 2 } } \end{array}$ and $\alpha _ { 2 } = \textstyle { \frac { 1 } { 2 } } ( 1 - { \sqrt { 2 } } )$ and the tableau

$$
{ \frac { 1 \left| { \begin{array} { l l } { { \frac { 1 } { 2 } } } ( 4 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } ( { \sqrt { 2 } } - 1 ) } \\ { { \frac { 1 } { 2 } } ( 5 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } { \sqrt { 2 } } } \end{array} \right.}  } { 2 - { \sqrt { 2 } } }  ~ .
$$

Combine the effective order idea with the diagonal extensions introduced in Subsection 364, and we obtain ‘DESIRE’ methods (diagonally extended by the example with implicit Runge–Kutta methods using effective order). These are exemplified $p = 2$ , $s = 3$ and $\textstyle \lambda = { \frac { 1 } { 5 } }$ . For this method, $\alpha _ { 1 } = - \frac { 3 } { 2 0 }$ $\begin{array} { r } { \alpha _ { 2 } = \frac { 1 } { 4 0 0 } } \end{array}$ and the coefficient tableau is

<table><tr><td>0</td><td>31 200</td><td>1 200</td><td>0</td></tr><tr><td rowspan="4"></td><td>81</td><td>49</td><td>0</td></tr><tr><td>200</td><td>200</td><td></td></tr><tr><td>71</td><td>119</td><td></td></tr><tr><td>200</td><td>200</td><td>1</td></tr><tr><td rowspan="2"></td><td>103</td><td>119</td><td>14</td></tr><tr><td>250</td><td>250</td><td>125</td></tr></table>

# Exercises 36

36.1 Derive the tableau for the two-stage order 2 diagonally implicit method satisfying (361a), (361b) with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ and $c _ { 2 } = 3 \lambda$ .

36.2 Rewrite the method in Exercise 36.1 so that the value of $Y _ { 1 }$ in step $n$ is the input and the value of $Y _ { 1 }$ in step $n + 1$ is the output.

36.3 Show that the method derived in Exercise 36.2 has stage order 2.

36.4 Derive a diagonally implicit method with $s = p = 3$ and with $\lambda = c _ { 2 } =$ $\textstyle { \frac { 1 } { 3 } }$ , $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , $c _ { 3 } = 1$ .

36.5 Derive a diagonally implicit method with $s = p = 3$ , $\lambda = 1$ , $c _ { 2 } = { \textstyle { \frac { 1 } { 3 } } }$ , $c _ { 3 } = 1$ , $b _ { 1 } = 0$ .

36.6 Show that for an L-stable method of the type described in Subsection 364 with $p = 3$ , $s = 4$ , the minimum possible value of $\lambda$ is approximately 0.2278955169, a zero of the polynomial

$1 8 5 9 7 6 \lambda ^ { 1 2 } - 1 4 9 0 4 0 0 \lambda ^ { 1 1 } + 4 6 0 1 4 4 8 \lambda ^ { 1 0 } - 7 2 5 7 1 6 8 \lambda ^ { 9 } + 6 8 4 2 8 5 3 \lambda ^ { 8 }$ $- 4 1 8 1 7 6 0 \lambda ^ { 7 } + 1 7 2 4 2 5 6 \lambda ^ { 6 } - 4 8 7 2 9 6 \lambda ^ { 5 } + 9 4 1 7 6 \lambda ^ { 4 } - 1 2 1 9 2 \lambda ^ { 3 } + 1 0 0 8 \lambda ^ { 2 } - 4 8 \lambda + 1 . 0 0 0 9 4 1 6 \lambda ^ { 5 }$ .

# 37 Symplectic Runge–Kutta Methods

# 370 Maintaining quadratic invariants

We recall Definition 357B in which the matrix $M$ plays a role, where the elements of $M$ are

$$
\begin{array} { r } { m _ { i j } = b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } . } \end{array}
$$

Now consider a problem for which

$$
y ^ { \mathsf { T } } Q f ( y ) = 0 ,
$$

for all $y$ . It is assumed that $Q$ is a symmetric matrix so that (370b) is equivalent to the statement that $y ( x ) ^ { 1 } Q y ( x )$ is invariant.

We want to characterize Runge–Kutta methods with the property that $y _ { n } ^ { \mathsf { T } } Q y _ { n }$ is invariant with $n$ so that the the numerical solution preserves the conservation law possessed by the problem. If the input to step $1$ is $y _ { 0 }$ , then the output will be

$$
y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } , 
$$

where the stage derivatives are $F _ { i } = f ( Y _ { i } )$ , with

$$
Y _ { i } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } .
$$

From (370b) it follows that

$$
\boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q y _ { 0 } } = - h \sum _ { j = 1 } ^ { s } a _ { i j } \boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q F } _ { j } .
$$

Use (370c) to calculate $y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 }$ and substitute from (370d) to obtain the result

$$
y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 } = y _ { 0 } ^ { \mathsf { T } } Q y _ { 0 } - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } F _ { i } ^ { \mathsf { T } } Q F _ { j } ,
$$

with $m _ { i j }$ given by (370a).

Thus $M ~ = ~ 0$ implies that quadratic invariants are preserved and, in particular, that symplectic behaviour is maintained. Accordingly, we have the following definition:

Definition 370A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is symplectic if

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is the zero matrix.

The property expressed by Definition 370A was first found by Cooper (1987) and, as a characteristic of symplectic methods, by Lasagni (1988), Sanz-Serna (1988) and Suris (1988).

# 371 Examples of symplectic methods

A method with a single stage is symplectic only if $2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = 0$ . For consistency, that is order at least $^ { 1 }$ , $b _ { 1 } = 1$ and hence $\begin{array} { r } { c _ { 1 } = a _ { 1 1 } = \frac { 1 } { 2 } } \end{array}$ ; this is just the implicit mid-point rule. We can extend this in two ways: by either looking at methods where $A$ is lower triangular or looking at the methods with stage order $s$ .

For lower triangular methods we will assume that none of the $b _ { i }$ is zero. The diagonals can be found from $2 b _ { i } a _ { i i } = b _ { i } ^ { 2 }$ to be $\begin{array} { r } { a _ { i i } = \frac { 1 } { 2 } b _ { i } } \end{array}$ . For the elements of $A$ below the diagonal we have $b _ { i } a _ { i j } = b _ { i } b _ { j }$ so that $a _ { i j } = b _ { j }$ . This gives a tableau

$$
 \begin{array} { r l } { { \frac { 1 } { 2 } } b _ { 1 } } & { { | \begin{array} { l } { { \frac { 1 } { 2 } } b _ { 1 } } \\ { b _ { 1 } + { \frac { 1 } { 2 } } b _ { 2 } } \end{array}  } } &  { | \begin{array} { l l l l l } { { \frac { 1 } { 2 } } b _ { 1 } } & { } & { } & { } & { } \\ { b _ { 1 } } & { { \frac { 1 } { 2 } } b _ { 2 } } & { } & { } & { } \\ { b _ { 1 } } & { b _ { 2 } } & { { \frac { 1 } { 2 } } b _ { 3 } } & { } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } \\ { b _ { 1 } + \cdot \cdot + b _ { s - 1 } + { \frac { 1 } { 2 } } b _ { s } } & { { | \begin{array} { l l l l l l } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { { \frac { 1 } { 2 } } b _ { s } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { b _ { s } } \end{array}  } } \end{array} } \end{array}
$$

This method is identical with $s$ steps of the mid-point rule with stepsizes $b _ { 1 } h$ , $b _ { 2 } h$ , $\cdot \cdot \cdot$ , $b _ { s } h$ .

For methods with order and stage order equal to $s$ , we have, in the notation of Subsection 358, $\epsilon _ { i } = 0$ for $i = s + 1$ , $s + 2$ , $\cdot \cdot \cdot$ , $2 s$ . This follows from the observation that $V ^ { \ I } M V = 0$ . Thus, in addition to $B ( s )$ , $B ( 2 s )$ holds. Hence, the abscissae of the method are the zeros of $P _ { s } ^ { * }$ and the method is the $s$ -stage Gauss method.

# 372 Order conditions

Given rooted trees $t$ , $u$ and a symplectic Runge–Kutta method, we consider the relationship between the elementary weights $\phi ( t u ) , \phi ( u t ) , \phi ( t ) , \phi ( u )$ . Write

$$
\Phi ( t ) = \sum _ { i = 1 } b _ { i } \phi _ { i } , \quad \Phi ( u ) = \sum _ { i = 1 } b _ { i } \psi _ { i } .
$$

Then we find

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) = \sum _ { i , j = 1 } ^ { s } b _ { i } \phi _ { i } a _ { i j } \psi _ { j } , } \\ { \displaystyle \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } b _ { j } \psi _ { j } a _ { j i } \phi _ { i } , } \end{array}
$$

so that

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) + \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } ( b _ { i } a _ { i j } + b _ { j } a _ { j i } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \sum _ { i , j = 1 } ^ { s } ( b _ { i } b _ { j } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \Phi ( t ) \Phi ( u ) . } \end{array}
$$

Assuming the order conditions $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ are satisfied, then

$$
\Phi ( t u ) - \frac { 1 } { \gamma ( t u ) } + \Phi ( u t ) - \frac { 1 } { \gamma ( u t ) } = 0 .
$$

Using this fact, we can prove the following theorem:

Theorem 372A Let $( A , b ^ { \prime } , c )$ be a symplectic Runge–Kutta method. The method has order $p$ if and only if for each non-superfluous tree and any vertex in this tree as root, $\Phi ( t ) = 1 / \gamma ( t )$ , where $t$ is the rooted tree with this vertex.

Proof. We need only to prove the sufficiency of this criterion. If two rooted trees belong to the same tree but have vertices $v _ { 0 }$ , $\widehat { v }$ say, then there is a sequence of vertices $v _ { 0 }$ , $v _ { 1 }$ , $\cdot \cdot \cdot$ , $v _ { m } = \widehat { v }$ , such that $v _ { i - 1 }$ and $v _ { i }$ are adjacent for $i = 1 , 2 , \dots , m$ . This mean that rooted trees $t , u$ exist such that $t u$ is the rooted tree with root $v _ { i - 1 }$ and $u t$ is the rooted tree with root $v _ { i }$ . We are implicitly using induction on the order of trees and hence we can assume that $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ . Hence, if one of the order conditions for the trees $t u$ and $u t$ is satisfied, then the other is. By working along the chain of possible roots $v _ { 0 } , v _ { 1 } , \ldots , v _ { m }$ , we see that the order condition associated with the root $v _ { 0 }$ is equivalent to the condition for $\widehat { v }$ . In the case of superfluous trees, one choice of adjacent vertices would imply that $t = u$ . Hence, (372a) is equivalent to $2 \Phi ( t t ) = 2 / \gamma ( t t )$ so that the order condition associated with $t t$ is satisfied and all rooted trees belonging to the same tree are also satisfied.

The first experiment uses the simple pendulum based on the Hamiltonian $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ and initial value $\left( p , q \right) = \left( 1 , 0 \right)$ . The amplitude is found to be $\pi / 3 \approx 1 . 0 4 7 1 9 8$ and the period to be approximately 6.743001. Numerical solutions, displayed in Figure 373(i), were found using the Euler, implicit Euler and the implicit mid-point rule methods. Only the last of these is symplectic and its behaviour reflects this. That is, like the exact solution which is also shown, the area of the initial set remains unchanged, even though its shape is distorted.

The second experiment is based on problem (122c), which evolves on the unit sphere $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ . The value of $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ is calculated by the Euler method, the implicit Euler method and the implicit mid-point rule method. Only the last of these is symplectic. The computed results are shown in Figure 373(ii). In each case a stepsize $h = 0 . 1$ was used. Although results are shown for only 500 time steps, the actual experiment was extended much further. There is no perceptible deviation from $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ for the first million steps.

![](images/83a6e1ff135a200883a79c61d1e2a5fd54639e36ae4148227af8a545daa4bdd1.jpg)  
Solutions of the Hamiltonian problem $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ . Left: Euler method (grey) and implicit Euler method (white). Right: exact solution (grey) and implicit mid-point method (white). The underlying image depicts the takahe Porphyrio hochstetteri, rediscovered in 1948 after many years of presumed extinction.

![](images/49ea0f5ff0444cf6688a2b9cb532cb3bfd5aa23c33b768de46a5533e41ed7d97.jpg)  
Experiments for problem (122c). The computed value of $\| y _ { n } \| ^ { 2 }$ is shown after $n = 1 , 2 , \ldots$ , steps.

# Exercises 37

37.1 Do two-stage symplectic Runge–Kutta methods exist which have order 3 but not order 4?

37.2 Do three-stage order 3 symplectic Runge–Kutta methods exist for which $A$ is lower triangular?

# 38 Algebraic Properties of Runge–Kutta Methods

# 380 Motivation

For any specific $N$ -dimensional initial value problem, Runge–Kutta methods can be viewed as mappings from $\mathbb { R } ^ { N }$ to $\mathbb { R } ^ { N }$ . However, the semi-group generated by such mappings has a significance independent of the particular initial value problem, or indeed of the vector space in which solution values lie. If a method with $s _ { 1 }$ stages is composed with a second method with $s _ { 2 }$ stages, then the combined method with $s _ { 1 } + s _ { 2 }$ stages can be thought of as the product of the original methods. It turns out that this is not quite the best way of formulating this product, and we need to work with equivalence classes of Runge–Kutta methods. This will also enable us to construct a group, rather than a mere semi-group.

It will be shown that the composition group of Runge–Kutta equivalent classes is homomorphic to a group on mappings from trees to real numbers. In fact the mapping that corresponds to a specific Runge–Kutta method is just the function that takes each tree to the associated elementary weight.

There are several reasons for introducing and studying these groups. For Runge–Kutta methods themselves, it is possible to gain a better understanding of the order conditions by looking at them in this way. Furthermore, methods satisfying certain simplifying assumptions, notably the $C$ and $D$ conditions, reappear as normal subgroups of the main group. An early application of this theory is the introduction of the concept of ‘effective order’. This is a natural generalization from this point of view, but makes very little sense from a purely computational point of view. While effective order was not widely accepted at the time of its discovery, it has been rediscovered (L´opez-Marcos, Sanz-Serna and Skeel, 1996) and has now been seen to have further ramifications.

The final claim that is made for this theory is that it has applications to the analysis of the order of general linear methods. In this guise a richer structure, incorporating an additive as well as a multiplicative operation, needs to be used; the present section also examines this more elaborate algebra.

The primary source for this theory is Butcher (1972), but it is also widely known through the work of Hairer and Wanner (1974). Recently the algebraic structures described here have been rediscovered through applications in theoretical physics. For a review of these developments, see Brouder (2000).

Before proceeding with this programme, we remark that the mappings from trees to real numbers, which appear as members of the algebraic systems introduced in this section, are associated with formal Taylor series of the form

$$
a ( \emptyset ) y ( x ) + \sum _ { t \in T } { \frac { a ( t ) } { \sigma ( t ) } } h ^ { r ( t ) } F ( t ) ( y ( x ) ) .
$$

Such expressions as this were given the name B-series by Hairer and Wanner

(1974) and written

$$
B ( a , y ( x ) ) ,
$$

where $a : T ^ { \# } \to \mathbb { R }$ , with $T ^ { \# }$ denoting the set of rooted trees $T$ together with an additional empty tree $\varnothing$ . Because of the central role of the exact solution series, in which $a ( \emptyset ) = 1$ and $a ( t ) = 1 / \gamma ( t )$ , Hairer and Wanner scale the terms in the series slightly differently, and write

$$
\begin{array} { l l l } { { \displaystyle { \cal B } ( a , y ( x ) ) = a ( \emptyset ) y ( x ) + \sum _ { t \in T } \frac { \alpha ( t ) a ( t ) } { r ( t ) ! } h ^ { r ( t ) } F ( t ) ( y ( x ) ) } } \\ { { \displaystyle ~ = a ( \emptyset ) y ( x ) + \sum _ { t \in T } \frac { a ( t ) } { \gamma ( t ) \sigma ( t ) ! } h ^ { r ( t ) } F ( t ) ( y ( x ) ) , } } \end{array}
$$

where $\alpha ( t )$ is the function introduced in Subsection 302. This means that the B-series representing a Runge–Kutta method with order $p$ will have $a ( t ) = 1$ whenever $r ( t ) \leq p$ . In this book we concentrate on the coefficients themselves, rather than on the series, but it will be the interpretation as coefficients in (380a), and not as coefficients in (380b), that will always be intended.

# 381 Equivalence classes of Runge–Kutta methods

We consider three apparently distinct ways in which two Runge–Kutta methods may be considered equivalent. Our aim will be to define these three equivalence relations and then show that they are actually equivalent equivalence relations. By this we mean that if two methods are equivalent in one of the three senses then they are equivalent also in each of the other senses. We temporarily refer to these three equivalence relations as ‘equivalence’, ‘ $\Phi$ - equivalence’ and $P$ -equivalence’, respectively.

Definition 381A Two Runge–Kutta methods are ‘equivalent’ if, for any initial value problem defined by an autonomous function $f$ satisfying a Lipschitz condition, and an initial value $y _ { 0 }$ , there exists $h _ { 0 } ~ > ~ 0$ such that the result computed by the first method is identical with the result computed by the second method, if $h \leq h _ { 0 }$ .

Definition 381B Two Runge–Kutta methods are $\cdot _ { \Phi }$ -equivalent’ if, for any $t \in T$ , the elementary weight $\Phi ( t )$ corresponding to the first method is equal to $\Phi ( t )$ corresponding to the second method.

In introducing $P$ -equivalence, we need to make use of the concept of reducibility of a method. By this we mean that the method can be replaced by a method with fewer stages formed by eliminating stages that do not contribute in any way to the final result, and combining stages that are essentially the same into a single stage. We now formalize these two types of reducibility.

Definition 381C A Runge–Kutta method $( A , b ^ { \prime } , c )$ is $^ { \small 4 }$ -reducible’ if the stage index set can be partitioned into two subsets $\{ 1 , 2 , \ldots , s \} = P _ { 0 } \cup P _ { 1 }$ such that $b _ { i } = 0$ for all $i \in P _ { 0 }$ and such that $a _ { i j } = 0$ if $i \in P _ { 1 }$ and $j \in \mathcal { P } _ { 0 }$ . The method formed by deleting all stages indexed by members of $P _ { 0 }$ is known as the $^ { \small 4 }$ -reduced method’.

Definition 381D A Runge–Kutta method $( A , b ^ { \prime } , c )$ is $^ { \cdot } P$ -reducible’ if the stage index set can be partitioned into $\{ 1 , 2 , \ldots , s \} = P _ { 1 } \cup P _ { 2 } \cup \ldots \cup P _ { \overline { { s } } }$ and if, for all $I , J = 1 , 2 , \ldots , { \overline { { s } } }$ , $\textstyle \sum _ { j \in P _ { J } } a _ { i j }$ is constant for all $i \in P _ { I }$ . The method $( \overline { { A } } , \overline { { b } } ^ { \intercal } , \overline { { c } } )$ , with $\overline { { s } }$ stages with $\begin{array} { r } { \overline { { a } } _ { I J } = \sum _ { j \in P _ { J } } a _ { i j } } \end{array}$ , for $i \in P _ { I }$ , $\textstyle { \overline { { b } } } _ { I } = \sum _ { i \in P _ { I } } b _ { i }$ and $\overline { { c } } _ { I } = c _ { i }$ , for $i \in P _ { I }$ , is known as the $P$ -reduced method.

Definition 381E A Runge–Kutta method is ‘irreducible’ if it is neither 0-reducible nor $P$ -reducible. The method formed from a method by first carrying out a $P$ -reduction and then carrying out a 0-reduction is said to be the ‘reduced method’.

Definition 381F Two Runge–Kutta methods are $^ { \circ }$ -equivalent’ if each of them reduces to the same reduced method.

Theorem 381G Let $( A , b ^ { \intercal } , c )$ be an irreducible $s$ -stage Runge–Kutta method. Then, for any two stage indices $i , j \in \{ 1 , 2 , \dots , s \}$ , there exists a Lipschitzcontinuous differential equation system such that $Y _ { i } \neq Y _ { j }$ . Furthermore, there exists $t \in T$ , such that $\Phi _ { i } ( t ) \neq \Phi _ { j } ( t )$ .

Proof. If $i , j$ exist such that

$$
\Phi _ { i } ( t ) = \Phi _ { j } ( t ) \quad { \mathrm { f o r ~ a l l ~ } } t \in T ,
$$

then define a partition $P = \{ P _ { 1 } , P _ { 2 } , . . . , P _ { \overline { { s } } } \}$ of $\{ 1 , 2 , \ldots , s \}$ such that $i$ and $j$ are in the same component of the partition if and only if (381a) holds. Let $\mathcal { A }$ denote the algebra of vectors in $\mathbb { R } ^ { s }$ such that, if $i$ and $j$ are in the same component of $P$ , then the $i$ and $j$ components of $v \in { \mathcal { A } }$ are identical. The algebra is closed under vector space operations and under component-bycomponent multiplication. Note that the vector with every component equal to $^ { 1 }$ is also in $\mathcal { A }$ . Let $\hat { \cal A }$ denote the subalgebra generated by the vectors made up from the values of the elementary weights for the stages for all trees. That is, if $t \in T$ , then $v \in \mathbb { R } ^ { s }$ defined by $v _ { i } = \Phi _ { i } ( t )$ , $i = 1 , 2 , \dots , s$ , is in $\hat { \cal A }$ , as are the component-by-component products of the vectors corresponding to any finite set of trees. In particular, by using the empty set, we can regard the vector defined by $v _ { i } = 1$ as also being a member of $\hat { \cal A }$ . Because of the way in which elementary weights are constructed, $v \in \widehat { A }$ implies $A v \in { \widehat { A } }$ . We now show that $\widehat { A } = A$ . Let $I$ and $J$ be two distinct members of $P$ . Then because $t \in T$ exists so that $\Phi _ { i } ( t ) \neq \Phi _ { j } ( t )$ for $i \in I$ and $j \in J$ , we can find $v \in { \mathcal { A } }$ so that $v _ { i } \neq v _ { j }$ . Hence, if $w = ( v _ { i } - v _ { j } ) ^ { - 1 } ( v - v _ { j } 1 )$ , where $1$ in this context represents the vector in $\mathbb { R } ^ { s }$ with every component equal to 1, then $w _ { i } = 1$ and $w _ { j } = 0$ . Form the product of all such members of the algebra for $J \ne I$ and we deduce that the characteristic function of $I$ is a member of $\mathcal { A }$ . Since the $S$ such vectors constitute a basis for this algebra, it follows that $\widehat { A } = A$ . Multiply the characteristic function of $J$ by $A$ and note that, for all $i \in I \in P$ , the corresponding component in the product is the same. This contradicts the assumption that the method is irreducible. Suppose it were possible that two stages, $Y _ { i }$ and $Y _ { j }$ , say, give identical results for any Lipschitz continuous differential equation, provided $h > 0$ is sufficiently small. We now prove the contradictory result that $\Phi _ { i } ( t ) = \Phi _ { j } ( t )$ for all $t \in T$ . If there were a $t \in T$ for which this does not hold, then write $U$ for a finite subset of $T$ containing $t$ as in Subsection 314. Construct the corresponding differential equation as in that subsection and consider a numerical solution using the Runge–Kutta method $( A , b ^ { \prime } , c )$ and suppose that $t$ corresponds to component $k$ of the differential equation. The value of component $k$ of $Y _ { i }$ is $\Phi _ { i } ( t )$ and the value of component $k$ of $Y _ { j }$ is $\Phi _ { j } ( t )$ . 

Now the key result interrelating the three equivalence concepts.

Theorem 381H Two Runge–Kutta methods are equivalent if and only if they are $P$ -equivalent and if and only if they are $\Phi$ -equivalent.

# Proof.

$P$ -equivalence $\Rightarrow$ equivalence. It will enough to prove that if $i , j ~ \in ~ P _ { I }$ , in any $P$ -reducible Runge–Kutta method, where we have used the notation of Definition 381D, then for any initial value problem, as in Definition 381A, $Y _ { i } = Y _ { j }$ , for $h < h _ { 0 }$ . Calculate the stages by iteration starting with $Y _ { i } ^ { \left[ 0 \right] } = \eta$ , for every $i \in \{ 1 , 2 , \ldots , s \}$ . The value of $Y _ { i } ^ { \left[ k \right] }$ in iteration $k$ will be identical for all $i$ in the same partitioned component.

$P$ -equivalence ⇒ Φ-equivalence. Let the stages be partitioned according to $\{ 1 , 2 , \ldots , s \} = P _ { 1 } \cup P _ { 2 } \cup \ldots \cup P _ { \overline { { s } } }$ and assume that a Runge–Kutta method is reducible with respect to this partition. It will be enough to prove that, for all $t \in T$ , $\Phi _ { i } ( t ) = \Phi _ { j } ( t )$ if $i$ and $j$ belong to the same component. This follows by induction on the order of $t$ . It is true for $t = \tau$ because $\Phi _ { i } ( t ) = c _ { i }$ is constant for all $i$ in the same component. For $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ ,

$$
\Phi _ { i } ( [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) = \sum _ { j = 1 } ^ { s } a _ { i j } \prod _ { k = 1 } ^ { m } \Phi _ { j } ( t _ { k } )
$$

and this also is constant for all $i$ in the same component.

$\Phi$ -equivalence  P -equivalence. Suppose two methods are $\Phi$ -equivalent but not $P$ -equivalent. Combine the $s$ stages of method 1 and the $\widehat { s }$ stages of method 2, together with the output approximations, into a single method and replace this by a reduced method. Because the original methods are not $P$ - equivalent, the output approximations in the combined method are not in the same partition. Hence, by Theorem 381G, there exists $t \in T$ such that $\Phi _ { i } ( t )$ takes on different values for these two approximations.

$E q u i v a l e n c e \Rightarrow P$ -equivalence. Suppose two methods are equivalent but not $P$ -equivalent. Carry out the same construction as in the immediately previous part of the proof. By Theorem 381G, there is an initial value problem satisfying the requirements of Definition 381A such that $Y _ { i }$ takes on different values for the two output approximations. This contradicts the assumption that the original methods are equivalent. $\sqcup$

# 382 The group of Runge–Kutta methods

Consider two equivalence classes of Runge–Kutta methods and choose a representative member of each of these classes. Because of the results of the previous subsection, equivalence is the same as $\Phi$ -equivalence and the same as $P$ -equivalence. To see how to construct the composition product for the classes, form a tableau

$$
{ \begin{array} { c c c c c c c c c c } { c _ { 1 } } & & & & & & & & & & & & & & \\ { c _ { 2 } } & & { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ & { c _ { 2 } } & & & & & & & & & & \\ { \vdots } & & { \vdots } & & & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ & & & & & & & & & & { c _ { s } } & & { 0 } & { \cdots } & { 0 } \\ & & & & & & & & & & & { \ddots } & { \vdots } \\ & & & & & & & & & & & & { \vdots } \\ { c _ { 3 } } b _ { j } + { \hat { c } } _ { 1 } \ } & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 1 1 } } & { { \hat { a } } _ { 1 2 } } & { \cdots } & { { \hat { a } } _ { 1 s } } \\ { \sum _ { i = 1 } ^ { s } b _ { j } + { \hat { c } } _ { 2 } } & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 2 1 } } & { { \hat { a } } _ { 2 2 } } & { \cdots } & { { \hat { a } } _ { 2 s } } \\ & & & & & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ & & & & & & & { \sum _ { i = 1 } ^ { s } b _ { i } + { \hat { c } } _ { s } \ }  & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 3 1 } } & { { \hat { a } } _ { 3 2 } } \\ & & & & & & & & { \hat { b } } & { { \hat { b } } _ { 4 3 } } & { \cdots } & { { \hat { b } } _ { 4 3 } } \end{array} 
$$

from the elements of the tableaux for the two methods $( A , b ^ { \iota } , c )$ and $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ , respectively. We have written $s$ and $\widehat { s }$ for the numbers of stages in the first and second method, respectively.

By writing $y _ { 0 }$ for the initial value for the first method and $y _ { 1 }$ for the value computed in a step and then writing $y _ { 2 }$ for the result computed by the second method using $y _ { 1 }$ for its initial value, we see that $y _ { 2 }$ is the result computed by the product method defined by (382a). To see why this is the case, denote the stage values by $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , for the first method and by $\widehat { Y } _ { i }$ , $i = 1 , 2 , \dots , \widehat { s }$ , for the second method. The variables $F _ { i }$ and $\widehat { F } _ { i }$ will denote the values of $f ( Y _ { i } )$ and $f ( \widehat { Y } _ { i } )$ .

The values of the stages and of the final results computed within the first and second steps are

$$
\begin{array} { l } { { Y _ { i } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } , \qquad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle } } \\ { { y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } F _ { j } , } } \\ { { \displaystyle } } \\ { { \widehat { Y } _ { i } = y _ { 1 } + h \displaystyle \sum _ { j = 1 } ^ { \widehat { s } } \widehat { a } _ { i j } \widehat { F } _ { j } , \qquad i = 1 , 2 , \ldots , \widehat { s } , } } \\ { { \displaystyle } } \\ { { y _ { 2 } = y _ { 1 } + h \displaystyle \sum _ { j = 1 } ^ { \widehat { s } } \widehat { b } _ { j } \widehat { F } _ { j } . } } \end{array}
$$

Substitute $y _ { 1 }$ from (382c) into (382d) and (382e), and we see that the coefficients for the stages in the second step and for the final output value $y _ { 2 }$ are given as in the tableau (382a).

If $m _ { 1 }$ and $m _ { 2 }$ denote the methods $( A , b ^ { \prime } , c )$ and $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ , respectively, write $m _ { 1 } \cdot m _ { 2 }$ for the method defined by (382a). Also, for a given method $m$ , we write $[ m ]$ for the equivalence class containing $m$ . The notation $m \equiv { \overline { { m } } }$ will signify that $m$ and $\overline { { m } }$ are equivalent methods.

We are interested in multiplication of equivalent classes, rather than of particular methods within these classes. Hence, we attempt to use the method given by (382a) as defining a new class of equivalent methods, which we can use as the product of the original two classes. The only possible difficulty could be that the result might depend on the particular choice of representative member for the two original classes. That no such difficulty arises follows from the following theorem:

Theorem 382A Let $m _ { 1 }$ , $_ { I I l 2 }$ , $\overline { { m } } _ { 1 }$ , $\overline { { m } } _ { 2 }$ denote Runge–Kutta methods, such that

$$
m _ { 1 } \equiv \overline { { { m } } } _ { 1 } a n d m _ { 2 } \equiv \overline { { { m } } } _ { 2 } .
$$

Then

$$
[ m _ { 1 } \cdot m _ { 2 } ] = [ { \overline { { m } } } _ { 1 } \cdot { \overline { { m } } } _ { 2 } ] .
$$

Proof. We note that an equivalent statement is

$$
m _ { 1 } \cdot m _ { 2 } \equiv \overline { { { m } } } _ { 1 } \cdot \overline { { { m } } } _ { 2 } .
$$

Let $y _ { 1 }$ and $y _ { 2 }$ denote the output values over the two steps for the sequence of steps constituting $m _ { 1 } \cdot m _ { 2 }$ , and $\overline { { y } } _ { 1 }$ and $\overline { { y } } _ { 2 }$ denote the corresponding output values for ${ \overline { { m } } } _ { 1 } \cdot { \overline { { m } } } _ { 2 }$ . If $f$ satisfies a Lipschitz condition and if $h$ is sufficiently small, then $y _ { 1 } = \overline { { y } } _ { 1 }$ because $m _ { 1 } \equiv \overline { { m } } _ { 1 }$ , and $y _ { 2 } = \overline { { y } } _ { 2 }$ because $m _ { 2 } \equiv \overline { { m } } _ { 2 }$ . Hence, (382g) and therefore (382f) follows. 

Having constructed a multiplicative operation, we now construct an identity element and an inverse for equivalence classes of Runge–Kutta methods. For the identity element we consider the class containing any method $m _ { 0 }$ that maps an initial value to an equal value, for a problem defined by a Lipschitz continuous function, provided that $h$ is sufficiently small. It is clear that $[ { \boldsymbol { m } } _ { 0 } { \boldsymbol { \cdot } } { \boldsymbol { m } } ] = [ { \boldsymbol { m } } { \boldsymbol { \cdot } } { \boldsymbol { m } } _ { 0 } ] = [ { \boldsymbol { m } } ]$ for any Runge–Kutta method $m$ . It will be convenient to denote the identity equivalence class by the symbol 1, where it will be clear from the context that this meaning is intended.

To define the inverse of an equivalence class, start with a particular representative $m = ( A , b ^ { \intercal } , c )$ , with $s$ stages, and consider the tableau

$$
\begin{array} { c } { { c _ { 1 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { c _ { 2 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \hdots \sum _ { j = 1 } ^ { s } b _ { j } \ \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { 1 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 1 s } - b _ { s } } } \\ { { a _ { 2 1 } - b _ { 1 } } } & { { a _ { 2 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 2 s } - b _ { s } } } \end{array} \right| } } \\ { { - b _ { 1 } \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \hdots \qquad \sum _ { j = 1 } ^ { s } b _ { j } \ \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { s 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { s s } - b _ { s } } } \\ { { - b _ { 1 } \qquad - b _ { 2 } } } & { { \cdots } } & { { - b _ { s } } } \end{array} \right| } } \end{array} .
$$

As we saw in Subsection 343, this method exactly undoes the work of $m$ Denote this new method by $m ^ { - 1 }$ , and we prove the following result:

Theorem 382B Let $m$ denote a Runge–Kutta method. Then

$$
[ m \cdot m ^ { - 1 } ] = [ m ^ { - 1 } \cdot m ] = 1 .
$$

Proof. The tableaux for the two composite methods $m \cdot m ^ { - 1 }$ and ${ m ^ { - 1 } } \cdot { m }$ are, respectively,

$$
\begin{array} { r l } & { c _ { 1 } \left| \begin{array} { l l l l l l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right| } \\ & { c _ { s } \left| \begin{array} { l l l l l l l l l } { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } & { \vdots } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { b _ { s } } & { a _ { 1 1 } - b _ { 1 } } & { a _ { 1 2 } - b _ { 2 } } & { \cdots } & { a _ { 1 s } - b _ { s } } \end{array} \right| } \\ & { c _ { 2 } \left| \begin{array} { l l l l l l l l l } { b _ { 1 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { a _ { 2 1 } - b _ { 1 } } & { a _ { 2 2 } - b _ { 2 } } & { \cdots } & { a _ { 2 s } } & { - b _ { s } } \end{array} \right| } \\ & { c _ { 2 } \left| \begin{array} { l l l l l l l l l l } { b _ { 1 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { \vdots } & { 0 } & { \vdots } & { \cdots } & { \vdots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right| } \\ & { c _ { s } \left| \begin{array} { l l l l l l l l l } { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { a _ { s 1 } - b _ { 1 } } & { a _ { s 2 } - b _ { 2 } } & { \cdots } & { a _ { s s } - b _ { s } } & { \cdots } & { b _ { s } } \end{array} \right| } \\ & { b _ { 1 1 } } & { b _ { 2 } \cdots } & { b _ { s } } &  - b _ { 1 } \end{array}
$$

and

$$
 \begin{array} { l }  { \begin{array} { l } { c c c c c c c c c c c c c c } { { } } \\ { { } } \\ { } \\ { { } } \\ { { } } \\ { { } ^ { c _ { 2 } } - \sum _ { j = 1 } ^ { s } b _ { j } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } \sum _ { j = 1 } ^ { s } } \\ { { } } \end{array} } { \left| \begin{array} { l l l l l l l l l l } { a _ { 1 1 } - b _ { 1 } } & { a _ { 1 1 } } & { a _ { 1 2 } - b _ { 2 } } & { \cdots } & { a _ { 1 s } - b _ { s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } \vdots } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { a _ { s 1 } - b _ { j } } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } - b _ { 1 } } \end{array} \right| } { \begin{array} { l l l l l l l l l } { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \end{array} }  \begin{array} { l l l l l l l } { { } } & { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\  { } \end{array} \end{array}
$$

Each of these methods is $P$ -reducible to the methods $m$ and $m ^ { - 1 }$ , respectively, but in each case with $b ^ { \top }$ replaced by the zero vector, so that each lies in the equivalence class 1. 

# 383 The Runge–Kutta group

While the group of equivalent classes of Runge–Kutta methods is conceptually very simple, it is difficult to use for detailed manipulations. We turn to a second group that is closely related to it, but which has a more convenient representation.

Let $G _ { 1 }$ denote the set of functions on $T$ , the rooted trees, to the real numbers. We define a binary relation on $G _ { 1 }$ that makes it a group. It is convenient to widen the scope of our discussion by making use of forests. By a ‘forest’, we mean a set of vertices $V$ and a set of edges $E$ such that each edge is an ordered pair of members of $V$ under the restrictions that each vertex appears as the second member of at most one edge. If $[ v _ { 1 } , v _ { 2 } ]$ , $[ v _ { 2 } , v _ { 3 } ]$ , $\cdot \cdot ,$ $[ v _ { n - 1 } , v _ { n } ]$ are edges, we write $v _ { 1 } < v _ { n }$ . We will require this relation to be a partial ordering.

Suppose that $V$ and $E$ can be partitioned as $V ~ = ~ V _ { 1 } \cup V _ { 2 } \cup \dots \cup V _ { k }$ , $E = E _ { 1 } \cup E _ { 2 } \cup \cdot \cdot \cdot \cup E _ { k }$ , where each of $( V _ { i } , E _ { i } )$ , $i = 1 , 2 , \ldots , k$ , is connected and is therefore a rooted tree. A function $\alpha : T  \mathbb { R }$ can be extended multiplicatively to a function on the set of all forests by defining

$$
\alpha { \big ( } ( V , E ) { \big ) } = \prod _ { i = 1 } ^ { k } \alpha { \big ( } ( V _ { i } , E _ { i } ) { \big ) } .
$$

If $( V , E )$ is a forest and $\hat { V }$ is a subset of $V$ , then the sub-forest induced by $\hat { V }$ is the forest $( \widehat { V } , \widehat { E } )$ , where $\widehat { E }$ is the intersection of $\hat { V } \times \hat { V }$ and $E$ . A special

case is when a sub-forest $( \widehat { V } , \widehat { E } )$ satisfies the requirement that for any two vertices $u , v$ of $E$ such that $u < v$ and $v \in \widehat { E }$ , $u$ is also a member of $\widehat { E }$ . In this case we write

$$
( { \widehat { V } } , { \widehat { E } } ) \triangleleft ( V , E ) .
$$

From now on we write forests by single letters $Q$ , $R$ , $S$ , and interpret $R \triangleleft S$ accordingly. If $R \triangleleft S$ then $S \backslash R$ will denote the forest induced by the difference of the vertex sets of $S$ and $R$ , respectively.

We can now define a product of two multiplicative mappings of forests to real numbers. If $\alpha$ and $\beta$ are two such mappings, then we write

$$
( \alpha \beta ) ( S ) = \sum _ { R \diamond S } \alpha ( S \setminus R ) \beta ( R ) .
$$

We need to verify that $\alpha \beta$ is multiplicative if the same is true for $\alpha$ and $\beta$ .

Lemma 383A Let $\alpha$ and $\beta$ be multiplicative mappings from the forests to the real numbers. Then $\alpha \beta$ is multiplicative.

Proof. It will be sufficient to consider the value of $( \alpha \beta ) ( S )$ , where $S = S _ { 1 } \cup S _ { 2 }$ . Each $R \triangleleft S$ can be written as $R = R _ { 1 } \cup R _ { 2 }$ , where $R _ { 1 } \triangleleft S _ { 1 }$ and $R _ { 2 } \triangleleft S _ { 2 }$ . We now have

$$
\begin{array} { l } { { ( \alpha \beta ) ( S ) = \displaystyle \sum _ { R \ll S } \alpha ( S \setminus R ) \beta ( R ) } } \\ { { \ = \displaystyle \sum _ { R _ { 1 } \leqslant S _ { 1 } } \alpha ( S _ { 1 } \setminus R _ { 1 } ) \beta ( R _ { 1 } ) \sum _ { R _ { 2 } \leqslant S _ { 2 } } \alpha ( S _ { 2 } \setminus R _ { 2 } ) \beta ( R _ { 2 } ) } } \\ { { \ = ( \alpha \beta ) ( S _ { 1 } ) ( \alpha \beta ) ( S _ { 2 } ) . } } \end{array}
$$

We next show that the product we have defined is associative.

Lemma 383B Let $\alpha$ , $\beta$ and $\gamma$ be multiplicative mappings from forests to reals. Then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Proof. If $Q \triangleleft R \triangleleft S$ then $( R \setminus Q ) \triangleleft ( S \setminus Q )$ . Hence, we find

$$
\begin{array} { r l } { ( ( \alpha \beta ) \gamma ) ( S ) = \displaystyle \sum _ { Q + \delta } ( \alpha \beta ) ( S \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + S } \sum _ { ( R \backslash Q ) \leqslant ( S \backslash Q ) } \alpha ( ( S \setminus Q ) \setminus ( R \setminus Q ) ) \beta ( R \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + R R \cap Q \leqslant ( S \setminus R ) \beta ( R \setminus Q ) \gamma ( Q ) } } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = ( \alpha ( \beta \gamma ) ) ( S ) . } \end{array}
$$

We can now restrict multiplication to trees, and we note that associativity still remains. The semi-group that has been constructed on the set $G _ { 1 }$ is actually a group because we can construct both left and right inverses, α−1left and $\alpha _ { \mathrm { r i g h t } } ^ { - 1 }$ say, for any $\alpha \in G _ { 1 }$ , which must be equal because

$$
\alpha _ { \mathrm { l e f t } } ^ { - 1 } = \alpha _ { \mathrm { l e f t } } ^ { - 1 } \left( \alpha \alpha _ { \mathrm { r i g h t } } ^ { - 1 } \right) = \left( \alpha _ { \mathrm { l e f t } } ^ { - 1 } \alpha \right) \alpha _ { \mathrm { r i g h t } } ^ { - 1 } = \alpha _ { \mathrm { r i g h t } } ^ { - 1 } .
$$

Lemma 383C Given $\alpha \in G _ { 1 }$ , there exist a left inverse and a right inverse.

Proof. We show, by induction on the order of $t$ , that it is possible to construct $\beta$ such that $( \alpha \beta ) ( t ) = 0$ or $( \beta \alpha ) ( t ) = 0$ , for all $t \in T$ . Because $( \alpha \beta ) ( \tau ) = ( \beta \alpha ) ( \tau ) = \alpha ( \tau ) + \beta ( \tau )$ , the result is clear for order 1. Suppose the result has been proved for all trees of order less than that of $t \neq \tau$ ; then we note that

$$
( \alpha \beta ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \alpha , \beta )
$$

and

$$
( \beta \alpha ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \beta , \alpha ) ,
$$

where $\phi ( t , \alpha , \beta )$ involves the values of $\alpha$ and $\beta$ only for trees with orders less than $r ( t )$ . Hence, it is possible to assign a value to $\beta ( t )$ so that $( \alpha \beta ) ( t ) = 0$ or that $( \beta \alpha ) ( t ) = 0$ , respectively. Thus it is possible to construct $\beta$ as a left inverse or right inverse of $\alpha$ . 

Having established the existence of an inverse for any $\alpha \in G _ { 1 }$ , we find a convenient formula for $\alpha ^ { - 1 }$ . We write $S$ for a tree $t$ , written in the form $( V , E )$ , and ${ \mathcal { P } } ( S )$ for the set of all partitions of $S$ . This means that if $P \in { \mathcal { P } } ( S )$ , then $P$ is a forest formed by possibly removing some of the edges from $E$ . Another way of expressing this is that the components of $P$ are trees $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , where $V$ is the union of $V _ { 1 }$ , $V _ { 2 }$ , $\cdot \cdot \cdot$ , $V _ { n }$ and each $E _ { i }$ is a subset of $E$ . The integer $n$ , denoting the number of components of $P$ , will be written as $\# P$ . We write $t _ { i }$ as the tree represented by $( V _ { i } , E _ { i } )$ .

Lemma 383D Given $\alpha \in G _ { 1 }$ and $t \in T$ , written in the form $( V , E )$ , then

$$
\alpha ^ { - 1 } ( t ) = \sum _ { P \in \mathcal { P } ( S ) } \prod _ { i = 1 } ^ { \# P } ( - \alpha ( t _ { i } ) ) .
$$

Proof. Construct a mapping $\beta \in G _ { 1 }$ equal to the right-hand side of (383b). We show that for any $t \in T$ , $( \alpha \beta ) ( t ) = 0$ so that $\alpha \beta = 1$ . Let $t = ( V , E )$ . For any partition $P$ with components $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , we consider the set of possible combinations of $\{ 1 , 2 , \ldots , n \}$ , with the restriction that if $C$ is such a combination, then no edge $( v _ { 1 } , v _ { 2 } ) \in E$ exists with $v _ { 1 } \in V _ { i }$ and $v _ { 2 } \in V _ { j }$ , with $i$ and $j$ distinct members of $C$ . Let $\mathcal C ( P )$ denote the set of all such combinations of $P \in \mathcal { P } ( t )$ . Given $C \in P$ , denote by $\overline { { C } }$ the complement of $C$ in $P$ .

The value of $( \alpha \beta ) ( t )$ can be written in the form

$$
\sum _ { P \in \mathcal { P } ( t ) } \sum _ { C \in \mathcal { C } ( P ) } \prod _ { i \in C } \alpha ( t _ { i } ) ( - 1 ) ^ { \# \overline { { C } } } \prod _ { j \in \overline { { C } } } \alpha ( t _ { j } ) .
$$

For any particular partition $P$ , the total contribution is

$$
\sum _ { C \in \mathcal { C } ( P ) } ( - 1 ) ^ { n - \# C } \prod _ { i = 1 } ^ { \# P } \alpha ( t _ { i } ) .
$$

This is zero because $\begin{array} { r } { \sum _ { C \in { \mathcal { C } } ( P ) } ( - 1 ) ^ { n - \# C } = 0 } \end{array}$

# 384 A homomorphism between two groups

We show that the groups introduced in Subsections 382 and 383 are related in such a way that the former is isomorphic to a subgroup of the latter. The mapping between elements of the group that provides this homomorphism maps an equivalence class of Runge–Kutta methods to the function on $T$ to $\mathbb { R }$ defined by the elementary weights associated with a representative member of the class. We need to establish that products in the first group are preserved in the second. This means that if $m$ and $\widehat { m }$ are Runge–Kutta methods and $\Phi : T  \mathbb { R }$ and $\widehat \Phi : T  \mathbb { R }$ are the elementary weight functions for $m$ and $\widehat { m }$ , respectively, then $\Phi \widehat \Phi$ is the elementary weight function associated with $m \widehat { m }$ .

Theorem 384A Let $\Phi : T  \mathbb { R }$ be the elementary weight function associated with $( A , b ^ { \prime } , c )$ and $\widehat \Phi : T \to \mathbb { R }$ the elementary weight function associated with $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ . Let $\widetilde { \Phi } : T  \mathbb { R }$ denote the elementary weight function for the product method as represented by (382a). Then

$$
{ \widetilde { \Phi } } = \Phi { \widehat { \Phi } } .
$$

Proof. Denote the $( s + { \widehat { s } } )$ -stage composite coefficient matrices by $( \widetilde { A } , \widetilde { b } ^ { \intercal } , \widetilde { c } )$ with the elements of $\ddot { A }$ and $\widetilde { b } ^ { \intercal }$ given by

$$
\begin{array} { r l } & { \widetilde { a } _ { i j } = \left\{ \begin{array} { l l } { a _ { i j } , } & { i \leq s , j \leq s , } \\ { 0 , } & { i \leq s , j > s , } \\ { b _ { j } , } & { i > s , j \leq s , } \\ { \widehat { a } _ { i - s , j - s } , } & { i > s , j > s . } \end{array} \right. } \\ & { \widetilde { b } _ { i } = \left\{ \begin{array} { l l } { b _ { i } , } & { i \leq s , } \\ { \widehat { b } _ { i - s } , } & { i > s . } \end{array} \right. } \end{array}
$$

For a tree $t$ , such that $r ( t ) = n$ , represented by the vertex–edge pair $( V , E )$ , with root $\rho \in V$ , write the elementary weight $ { \widetilde { \Phi } } ( t )$ in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { i \in I } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

In this expression, $I$ is the set of all mappings from $V$ to the set $\{ 1 , 2 , \ldots , { \widetilde { s } } \}$ and, for $i \in I$ and $v \in V$ , $i ( v )$ denotes the value to which the vertex $v$ maps.

If $v \ < \ w$ and $i ( v ) \leq s < i ( w )$ then the corresponding term in (384a) is zero. Hence, we sum only over $I ^ { \prime }$ defined as the subset of $I$ from which such $i$ are omitted. For any $i \in I ^ { \prime }$ , define $R \triangleleft S = ( V , E )$ such that all the vertices associated with $R$ map into $\{ s + 1 , s + 2 , \ldots , s + \widehat { s } \}$ . Collect together all $i \in I ^ { \prime }$ which share a common $R$ so that (384a) can be written in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { R \leqslant S } \sum _ { i \in I _ { R } } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

For each $R$ , the terms in the sum have total value $\Phi ( S \setminus R ) { \widehat { \Phi } } ( R )$ , and the result follows. $\sqcup$

# 385 A generalization of $G _ { 1 }$

It will be convenient to build an algebraic system similar to $G _ { 1 }$ , but possessing, in addition to the group structure, a vector space structure. We cannot exactly achieve all of this, but we can achieve almost all of it. The way we go about this is to add to $T$ an additional member, known as the ‘empty tree’ and denoted by $\emptyset$ . The augmented set of trees will be denoted by $T ^ { \# }$ . We write $G$ for the set of mappings $T ^ { \# }  \mathbb { R }$ and $G _ { 1 }$ for the set of those members of $G$ for which $\varnothing$ maps to 1. We define the operation $G _ { 1 } \times G \to G$ just as for the group operation except that the coefficient of $\alpha ( t )$ in the formula for $( \alpha \beta ) ( t )$ is $\beta ( \emptyset )$ . With this understanding we retain the associativity property, in cases where it makes sense. That is, if $\alpha , \beta \in G _ { 1 }$ and $\gamma \in G$ , then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Furthermore, left-multiplication by an element of $G _ { 1 }$ is linear in the sense that

$$
\alpha ( \beta + \gamma ) = \alpha \beta + \alpha \gamma ,
$$

whenever $\alpha \in G _ { 1 }$ and $\beta , \gamma \in G$ . Furthermore,

$$
\alpha ( c \beta ) = c \alpha \beta ,
$$

where, for a scalar $c$ , $c \beta$ is the mapping that takes $t$ to $c \beta ( t )$ for all $t \in T ^ { \# }$ .

The generalization we have introduced has a simple significance in terms of Runge–Kutta tableaux and methods. Instead of computing the output value from a step of computation by the formula

$$
y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } ,
$$

where $y _ { 0 }$ is the input value and $F _ { 1 }$ , $F _ { 2 }$ , . . . , $F _ { s }$ are stage derivatives, we can replace (385a) by

$$
b _ { 0 } y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } { \cal F } _ { i } .
$$

To express this in a tableau, we place the coefficient $b _ { 0 }$ in the spare space at the left of the last line. Thus, the tableau would have the form

$$
\begin{array}{c} { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { b _ { 0 } } \end{array} \right| } { a _ { 2 1 } }  & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { { \left| \begin{array} { l l l l l } { \vdots } & { } & { \vdots } & { } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| } } \end{array} 
$$

As a Runge–Kutta method, to be used in the conventional manner as a onestep method for advancing the solution of a differential equation, this makes no sense at all, if $b _ { 0 } \neq 1$ . Indeed, the method would not even be covariant with respect to shifts of origin. However, the process of computing with a single step of this contrived method may play an important role as part of a more sophisticated computation. An important example of a generalized Runge–Kutta method is given by the one-stage tableau

$$
{ \frac { 0 \left| 0 } { 0 \right| 1 } } \ .
$$

This method does nothing other than computing $h$ multiplied by the derivative of the input value. Combined with linear operations, all Runge–Kutta methods can be built up from this basic method. The elementary weights associated with this method are given by

$$
\Phi ( t ) = { \left\{ \begin{array} { l l } { 1 , } & { t = \tau , } \\ { 0 , } & { t \neq \tau . } \end{array} \right. }
$$

# 386 Recursive formula for the product

We consider a formalism for the product on $G _ { 1 } \times G \to G$ , based on the second of the recursive constructions of trees defined in Subsection 300. That is, for

two trees $t$ , $u$ , we define $t u$ as the tree formed by joining the roots of $t$ and $u$ with the root of $t$ regarded as the root of the product. Corresponding to $t \in T ^ { \# }$ , we define $\widehat { t } : G _ { 1 } \to \mathbb { R }$ by the formula

$$
{ \widehat { t } } ( \alpha ) = \alpha ( t ) , \qquad \alpha \in G _ { 1 } .
$$

The set of all $\hat { \boldsymbol { t } }$ , for $t \in T$ , will be denoted by $\widehat { T }$ . We extend the dot-product notation from $T \times T  T$ to ${ \widehat { T } } \times { \widehat { T } }  { \widehat { T } }$ by the formula

$$
\widehat { t } \cdot \widehat { u } = \widehat { t } \widehat { u } .
$$

Since $\widehat { T } ^ { \# }$ denotes a set of linear functionals on $G$ , it is natural to consider also the vector space spanned by such functionals and extend the dot-product notation to make the product of two functionals bilinear. We denote this set of functionals by $G ^ { * }$ .

We can now define a special function, $\lambda : G _ { 1 } \times T \to G ^ { * }$ , by the recursion

$$
\begin{array} { c } { { \lambda ( \alpha , \tau ) = \widehat { \tau } , } } \\ { { \lambda ( \alpha , t u ) = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) . } } \end{array}
$$

This enables us to generate expressions for $\alpha \beta$ for all trees.

Theorem 386A For $\alpha \in G _ { 1 }$ and $\beta \in G$ ,

$$
\begin{array} { l } { { ( \alpha \beta ) ( \emptyset ) = \beta ( \emptyset ) , } } \\ { { ( \alpha \beta ) ( t ) = \lambda ( \alpha , t ) ( \beta ) + \alpha ( t ) \beta ( \emptyset ) . } } \end{array}
$$

Proof. In this proof only, we introduce the notation $R { \dot { < } } S$ to denote $R \triangleleft S$ , with $R \neq \emptyset$ . If a tree $t$ is represented by the set $S$ of vertices, with an implied set of edges, then the notation $t _ { R }$ , where $R \triangleleft S$ , will denote the tree formed from the elements of $R$ , with the induced set of edges. With this terminology, we can write (383a) in the form

$$
( \alpha \beta ) ( t ) = \sum _ { R \doteq S } \alpha ( S \setminus R ) \beta ( R ) + \alpha ( t ) \beta ( \emptyset ) .
$$

Hence, we need to show that

$$
\lambda ( \alpha , t ) = \sum _ { R \mathbin { \dot { \times } } \colon S } \alpha ( S \setminus R ) \widehat { t } _ { R } .
$$

This is obvious in the case $t = \tau$ . We now consider a tree $t u$ with $t$ represented by $S$ and $u$ represented by $Q$ . This means that $t u$ can be represented by the graph $( V , E )$ , where $V$ is the union of the vertex sets associated with $S$ and

The function $\lambda$ for trees of orders 1 to 5   

<table><tr><td>t</td><td></td><td>r(t) λ(α,t)</td><td></td></tr><tr><td>·</td><td>T</td><td>1</td><td></td></tr><tr><td>：</td><td>TT</td><td>2</td><td>T+a（T）</td></tr><tr><td>?</td><td>TT·T</td><td>3</td><td>+2a(T)+a(T)²</td></tr><tr><td>：</td><td>T·TT</td><td>3</td><td>.竹+a(T)T+a(TT)T</td></tr><tr><td>Y</td><td>(TT·T)T</td><td>4</td><td>(T.T)T+3a(T).↑+3a(T)²T+a(T)↑</td></tr><tr><td></td><td>· TT·TT</td><td>4</td><td>T+a(T)T.+a(T).TT+ (a(T)²+a(TT))TT+a(T)a(TT)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT·T)4 T(T.T)+2a(T)T.T+α(T)²TT+α(TT·T)T</td></tr><tr><td></td><td></td><td></td><td>T(T:TT)4 T(T.TT)+α(T)T.T+α(TT)TT+α(T·TT)T</td></tr><tr><td>W</td><td></td><td></td><td>(TT:T)T·T 5 (TT.T)T.T+4a(T)(TT.T)T+6a(T)².T+ 4a(t)+a(T)T</td></tr><tr><td></td><td></td><td></td><td>(TT·T)·TT 5 (TT.T).TT+2α(T)TT.TT+a(T)(TT.T)T+ 2a(T)².↑+(a(T)²+a(TT)).T+</td></tr><tr><td>?</td><td></td><td></td><td>(a(τ)³+2a(T)a(τT))TT+α(τ)²a(TT)T TT·(TT·T) 5 TT.(TT.T)+2a(T)TT.TT+α(T)T(TT.T)+ a(T)².↑+2a(T)².T+</td></tr><tr><td></td><td></td><td></td><td>(a(T)³+α(TT·T))TT+α(T)a(TT·T)T TT·(T.TT） 5 T.(T.TT)+a(T)TT.T+a(T)(T.TT)+ a(TT)TT.↑+a(T)².T+</td></tr><tr><td>V</td><td></td><td></td><td>(a(T)a(TT)+α(T:TT))TT+a(T)a(T·TT)T (T:TT).TT 5 (T.TT).TT+2a(T)TT.T+a(T)².T+ 2a(TT)T.TT+2a(T)a(TT)+α(TT)²↑</td></tr><tr><td></td><td></td><td></td><td>YT·(TT·T)T 5 T.(TT.T)T+3a(T)T(T.T)+3a(T)²TT+ a(T)³TT+a((TT.T)T)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT:TT)5 T(TT.T)+a(T)T(TT.T)+α(T)T(T.TT)+</td></tr><tr><td></td><td></td><td></td><td>(a(T)²+α(TT))T.TT+a(T)a(TT)TT+α(TT·TT)T T·T(TT.T） 5 T.T(.T)+2a(T)T(T.TT)+α(T)²T.TT+</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>α(TT·T)TT+α(T(TT·T))T</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T·T(T·TT) 5 T.T(T.TT)+a(T)T(T.TT)+α(TT)T.TT+</td></tr></table>

$Q$ , and $E$ is the union of the corresponding edge sets together with additional edge connecting the two roots. Temporarily we write $( V , E ) = S Q$ . If $R { \dot { < } } S$ and $P \mathcal { \hat { A } } Q$ then the set of subgraphs related to $S Q$ by the relation $X { \dot { \triangle } } S Q$ are of the form $X = R P$ or of the form $X = R$ . Hence,

Formulae for $( \alpha \beta ) ( t _ { i } )$ up to trees of order 5   

<table><tr><td>ti(αβ)(ti)</td><td>ir(ti)</td><td></td><td></td></tr><tr><td>0</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td>β+α1β0</td></tr><tr><td>2</td><td>2</td><td></td><td>β+α1β1+a2βo</td></tr><tr><td>3</td><td>3</td><td>?</td><td>β+2a1β2+α²β1+α3βo</td></tr><tr><td>4</td><td>3</td><td>…</td><td>β4+α1β+α2β1+a4βo</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>β5 + 3α1β+3a²β+a³β1+α5β0</td></tr><tr><td>6</td><td>4</td><td></td><td>β6+α1β4+α1β+(a²+a2)β+a1a2β1 +a6βo</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>β7 +2α1β4+a²β2+α3β1+α7β0</td></tr><tr><td>8</td><td>4</td><td>：</td><td>β8+a1β4 +a2β2+α4β1 +a8β0</td></tr><tr><td>9</td><td>5</td><td>E</td><td>βg+4a1β5+6a²β+4a³β+a𝑖β1+agβo</td></tr><tr><td>10</td><td>5</td><td></td><td>β10+2α1β6+α1β5 +a²β4+(2a² +α2)β3+ (2α1α2+α²)β+α²α2β1+α10β0</td></tr><tr><td></td><td>115</td><td></td><td>β11 +α1β7+2α1β6+2a²β4+α²β+(a²+α3)β²+</td></tr><tr><td></td><td>125</td><td></td><td>α1α3βi+α11β</td></tr><tr><td></td><td></td><td></td><td>α1α4β1+α12β0</td></tr><tr><td></td><td>135V</td><td></td><td>β13 +2α1β6+2a2β4+α²β+2α1α2β2+α²β1+α13β0</td></tr><tr><td></td><td>145</td><td></td><td>Yβ14+3α1β7+3a²β4+α³β+α5β1+α14/0</td></tr><tr><td>15</td><td>5</td><td></td><td>β15 +α1β8+α1β7+(a²+α2)β4+α1α2β+α6β1+α15β</td></tr><tr><td>165</td><td></td><td></td><td></td></tr><tr><td>17</td><td>5</td><td></td><td>β17 +α1β8+a2β4+α4β2+α8β1+α17β0</td></tr></table>

$$
\begin{array} { r l } { \displaystyle \sum _ { X \mathbin { \vrule d S Q } } \alpha ( S Q \setminus X ) \widehat { t } _ { X } = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P d \setminus P } } \alpha ( S Q \setminus P R ) \widehat { t } _ { P R } + \displaystyle \sum _ { R \mathbin { \vrule d S \widehat { X } } } \alpha ( S Q \setminus R ) \widehat { t } _ { R } } & { } \\ { = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P \widehat { t } _ { P } } } \alpha ( Q \setminus P ) \widehat { t } _ { P } \displaystyle \sum _ { R \mathbin { \vrule d S } } \alpha ( S \setminus R ) \widehat { t } _ { R } + \alpha ( ( S \setminus R ) Q ) \displaystyle \sum _ { R \mathbin { \vrule h } } \widehat { t } _ { R } } & { } \\ { = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) } & { } \\ { = \lambda ( \alpha , t u ) . } \end{array}
$$

<table><tr><td>ir(ti）</td><td></td><td></td><td>ti(a-1)(ti)</td></tr><tr><td>1</td><td>1</td><td>.</td><td>-α1</td></tr><tr><td>2</td><td>2</td><td></td><td>a²-a2 ：</td></tr><tr><td>3</td><td>3</td><td>Y</td><td>2α1α2 -α² -a3</td></tr><tr><td>4</td><td>3</td><td></td><td>三 2α1α2 -α² -α4</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>3α1α3 -3α2a² +α4 -α5</td></tr><tr><td>6</td><td>4</td><td></td><td>√ a1a3 +α1a4+a²- 3a2a² +a4 -a6</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>2α1α4 +α1α3 -3a²α2 +α𝑖 -α7</td></tr><tr><td>8</td><td>4</td><td></td><td>2α1α4+a²-3a²a2+a4-α8</td></tr><tr><td>9</td><td></td><td>√</td><td>4α1α5 -6a²α3 + 4a²α2 -α𝑖 -α9</td></tr><tr><td>10</td><td>5</td><td></td><td> 2α1a6 +α1a5 +α2a3 -a²α4 - 3a²α3 + 4α1α2 -α− - α10</td></tr><tr><td></td><td></td><td>115</td><td>α1α7 + 2α1α6 +α2α3-2a1α² -α²α3 - 2α²α4+ 4a³α2 -α -α11</td></tr><tr><td></td><td>125</td><td></td><td>4α²α2 -ai -α12</td></tr><tr><td></td><td></td><td>135</td><td>2α1a6+2α2α4-a²ag-2a²α4-3α1α²+4α³α2-a -α13</td></tr><tr><td></td><td>145</td><td></td><td>Y 3α1a7 +α1a5 - 3a²α4 -3a²αg +4a³α2 -α− - α14</td></tr><tr><td></td><td></td><td></td><td>α1a8 +α1α7 +α1a6 +α2α4 - 2α1a² -α²α3 -3a²α4+ 4α²α2 -α -α15</td></tr><tr><td></td><td>165</td><td></td><td>4α²α2 -α -α16</td></tr><tr><td>175</td><td></td><td></td><td>2α1α8 +2a2α4-3a1α² + 4α²α2 -α -α17</td></tr></table>

As examples of the use of the algorithm for evaluating $\lambda$ , and thence values of the product on $G _ { 1 } \times G$ , we find

$$
\begin{array} { r l } & { \quad \quad \lambda ( \alpha , \tau ) = \hat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \tau ) = \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } , } \\ & { \lambda ( \alpha , \tau \tau \cdot \tau ) = ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) \cdot \widehat { \tau } + \alpha ( t ) ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) } \\ & { \quad \quad \quad \quad = \widehat { \tau \tau } \cdot \widehat { \tau } + 2 \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau ) ^ { 2 } \widehat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \cdot \tau \tau ) = \widehat { \tau } \cdot ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) + \alpha ( \tau \tau ) \widehat { \tau } } \\ & { \quad \quad \quad = \widehat { \tau } \cdot \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau \tau ) \widehat { \tau } . } \end{array}
$$

The values of $\lambda ( \alpha , t )$ are continued in Table 386(I) up to trees of order 5. For convenience, each tree is given in product form as well as in pictorial form.

From (386a)–(386d), we find

$$
\begin{array} { r l } & { \quad ( \alpha \beta ) ( \tau ) = \beta ( \tau ) + \alpha ( \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau ) = \beta ( \tau \tau ) + \alpha ( \tau ) \beta ( \tau ) + \alpha ( \tau \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau \cdot \tau ) = \beta ( \tau \tau \cdot \tau ) + 2 \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau ) ^ { 2 } \beta ( \tau ) + \alpha ( \tau \tau \cdot \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \cdot \tau \tau ) = \beta ( \tau \cdot \tau \tau ) + \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau \tau ) \beta ( \tau ) + \alpha ( \tau \cdot \tau \tau ) \beta ( \emptyset ) . } \end{array}
$$

It will be convenient to extend these formulae up to trees of order 5, and we present this in Table 386(II). For convenience, we denote the empty tree by $t _ { 0 }$ and the trees of order 1 to 5 by $t _ { i }$ , $i = 1 , 2 , \dots , 1 7 .$ . We also write $\alpha _ { i }$ and $\beta _ { i }$ for $\alpha ( t _ { i } )$ and $\beta ( t _ { i } )$ , respectively. Note that $\alpha _ { 0 }$ does not appear in this table because it always has the value $\alpha ( \varnothing ) = 1$ .

Because Table 386(II) has reference value, we supplement the information it contains with Table 386(III), which gives the formulae for $( \alpha ^ { - 1 } ) ( t )$ where $r ( t ) \leq 5$ and $\alpha \in G _ { 1 }$ .

# 387 Some special elements of $G$

As we have remarked, $D \in G$ represents the differentiation operation, scaled by the unit stepsize $h$ . If $\xi$ denotes the element in $G _ { 1 }$ corresponding to a generalized Runge–Kutta tableau

$$
{ \frac { c \mid A } { 1 \mid b ^ { \mathsf { T } } } } = { \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \\ { c } \\ { \vdots } \\ { c _ { s } } \\ { 1 } \end{array} } { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| }
$$

then $\xi D$ will correspond to the $s$ -stage tableau

$$
{ \begin{array} { r } { c _ { 1 } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { \sum _ { i = 1 } ^ { s } b _ { i } \ { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { 0 } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right| } } \end{array} }
$$

The result computed by (387b) is just $h f ( \widehat { y } )$ , where $\widehat { y }$ is the result computed by (387a). With this understanding, we have an alternative means of defining the group element corresponding to each of the stages, as well as the final

result, of a Runge–Kutta method. Denote the members of $G _ { 1 }$ corresponding to the stages $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , of (387a) by $\eta _ { i }$ and the output result by $\xi$ ; then

$$
\begin{array} { l } { { \displaystyle \eta _ { i } = 1 + \sum _ { j = 1 } ^ { s } a _ { i j } \eta _ { j } D , } } \\ { { \displaystyle \xi = 1 + \sum _ { i = 1 } ^ { s } b _ { i } \eta _ { i } D . } } \end{array}
$$

In the case of a generalized method, where $b _ { 0 }$ is the coefficient of $y _ { n - 1 }$ in the formula for $y _ { n }$ , (387c) is replaced by

$$
\xi = b _ { 0 } 1 + \sum _ { i = 1 } ^ { s } b _ { i } \eta _ { i } D ,
$$

where, in this context, $^ { 1 }$ is the group-theoretic identity in $G$ .

In addition to $D$ , it is convenient to introduce an element $E \in G$ , defined by

$$
\begin{array} { l } { \displaystyle E ( \emptyset ) = 1 , } \\ { \displaystyle E ( t ) = \frac { 1 } { \gamma ( t ) } , \qquad t \in T . } \end{array}
$$

This means that $E$ corresponds to the exact solution of the differential equation as represented by the Picard iteration scheme introduced in Section 311. The conditions for order $p$ for the Runge–Kutta method (387a) can now be written in the form

$$
\xi ( t ) = E ( t ) , \qquad r ( t ) \leq p .
$$

Finally, we define a sequence of members of $G$ which correspond to the computation of the Taylor coefficients at the initial point, scaled in terms of powers of $h$ . If $T _ { k }$ corresponds to the method which, on input $y _ { 0 } = y ( x _ { 0 } )$ , computes $h ^ { k } y ^ { ( k ) } ( x _ { 0 } )$ , then we require that

$$
\begin{array} { l } { { T _ { k } ( \emptyset ) = 0 , } } \\ { { T _ { k } ( t ) = \left\{ \begin{array} { l l } { { \alpha ( t ) , } } & { { \quad r ( t ) = k , } } \\ { { 0 , } } & { { \quad r ( t ) \neq k . } } \end{array} \right. } } \end{array}
$$

Obviously, $T _ { 1 } = D$ , but $D ^ { n }$ is not defined for $n \geq 2$ .

We can relate $T _ { 1 }$ , $u _ { 2 } , \ldots .$ with $E$ by writing

$$
E = 1 + \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k ! } } T _ { k } ,
$$

where the result is interpreted as meaning that

$$
E ( t ) = 1 ( t ) + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } T _ { k } ( t ) ,
$$

for any $t \in T$

Since $E$ takes the exact solution to a differential equation through one unit step $h$ , it is natural to ask how we would represent the solution at a general point $\theta h$ advanced from the initial point. We write this as $E ^ { ( \theta ) }$ , and we note that

$$
E ^ { ( \theta ) } ( t ) = \theta ^ { r ( t ) } E ( t ) ,
$$

for all $t \in T$ . We can generalize (387d) in the form

$$
E ^ { ( \theta ) } = 1 + \sum _ { k = 1 } ^ { \infty } \frac { \theta ^ { k } } { k ! } T _ { k } ,
$$

and note that, for $\theta$ an integer $n$ , we have

$$
E ^ { ( n ) } = E ^ { n } .
$$

This property is, to some extent, characteristic of $E$ , and we have:

Theorem 387A If $\alpha \in G _ { 1 }$ such that $\alpha ( \tau ) = 1$ , and $m$ is an integer with $m \not \in \{ 0 , 1 , - 1 \}$ , then $\alpha ^ { ( m ) } = \alpha ^ { m }$ implies that $\alpha = E$ .

Proof. For any tree $t \neq \tau$ , we have $\alpha ^ { ( m ) } ( t ) = r ( t ) ^ { m } \alpha ( t ) + Q _ { 1 }$ and $\alpha ^ { m } ( t ) =$ $m \alpha ( t ) + Q _ { 2 }$ , where $Q _ { 1 }$ and $Q _ { 2 }$ are expressions involving $\alpha ( u )$ for $r ( u ) < r ( t )$ . Suppose that $\alpha ( u )$ has been proved equal to $E ( u )$ for all such trees. Then

$$
\begin{array} { c } { { \alpha ^ { ( m ) } ( t ) = r ( t ) ^ { m } \alpha ( t ) + Q _ { 1 } , } } \\ { { \alpha ^ { m } ( t ) = m \alpha ( t ) + Q _ { 2 } , } } \\ { { E ^ { ( m ) } ( t ) = r ( t ) ^ { m } E ( t ) + Q _ { 1 } , } } \\ { { E ^ { m } ( t ) = m E ( t ) + Q _ { 2 } , } } \end{array}
$$

so that $\alpha ^ { ( m ) } ( t ) = \alpha ^ { m } ( t )$ implies that

$$
( r ( t ) ^ { m } - m ) ( \alpha ( t ) - E ( t ) ) = 0 ,
$$

implying that $\alpha ( t ) ~ = ~ E ( t )$ , because $r ( t ) ^ { m } \neq m$ whenever $r ( t ) ~ > ~ 1$ and $m \not \in \{ 0 , 1 , - 1 \}$ . $\sqcup$

Of the three excluded values of $m$ in Theorem 387A, only $\begin{array} { l } { m ~ = ~ - 1 } \end{array}$ is interesting. Methods for which $\alpha ^ { ( - 1 ) } = \alpha ^ { - 1 }$ have a special property which makes them of potential value as the source of efficient extrapolation

procedures. Consider the solution of an initial value problem over an interval $[ x _ { 0 } , { \overline { { x } } } ]$ using $n$ steps of a Runge–Kutta method with stepsize $h = ( \overline { { x } } - x _ { 0 } ) / n$ . Suppose the computed solution can be expanded in an asymptotic series in $h$ ,

$$
y ( \overline { { x } } ) + \sum _ { i = 1 } ^ { \infty } C _ { i } h ^ { i } .
$$

If the elementary weight function for the method is $\alpha$ , then the method corresponding to $( \alpha ^ { ( - 1 ) } ) ^ { - 1 }$ exactly undoes the work of the method but with $h$ reversed. This means that the asymptotic error expansion for this reversed method would correspond to changing the sign of $h$ in (387e). If $\alpha = ( \alpha ^ { ( - 1 ) } ) ^ { - 1 }$ , this would give exactly the same expansion, so that (387e) is an even function. It then becomes possible to extend the applicability of the method by extrapolation in even powers only.

# 388 Some subgroups and quotient groups

Let $H _ { p }$ denote the linear subspace of $G$ defined by

$$
H _ { p } = \{ \alpha \in G : \alpha ( t ) = 0 , { \mathrm { ~ w h e n e v e r ~ } } r ( t ) \leq p \} .
$$

If $\alpha , \beta \in G$ then $\alpha = \beta + H _ { p }$ will mean that $\alpha - \beta$ is a member of $H _ { p }$ . The subspace is an ideal of $G$ in the sense of the following result:

Theorem 388A Let $\alpha ~ \in ~ G _ { 1 }$ , $\beta \in G _ { 1 }$ , $\gamma \in G$ and $\delta \in G$ be such that $\alpha = \beta + H _ { p }$ and $\gamma = \delta + H _ { p }$ . Then $\alpha \gamma = \beta \delta + H _ { p }$ .

Proof. Two members of $G$ differ by a member of $H _ { p }$ if and only if they take identical values for any $t$ such that $r ( t ) \leq p$ . For any such $t$ , the formula for $( \alpha \gamma ) ( t )$ involves only values of $\alpha ( u )$ and $\gamma ( u )$ for $r ( u ) ~ < ~ r ( t )$ . Hence, $( \alpha \gamma ) ( t ) = ( \beta \delta ) ( t )$ . 

An alternative interpretation of $H _ { p }$ is to use instead $1 + H _ { p } \in G _ { 1 }$ as a subgroup of $G _ { 1 }$ . We have:

Theorem 388B Let $\alpha , \beta \in G _ { 1 }$ ; then

$$
\alpha = \beta + H _ { p }
$$

if and only if

$$
\alpha = \beta ( 1 + H _ { p } ) .
$$

Proof. Both (388a) and (388b) are equivalent to the statement $\alpha ( t ) = \beta ( t )$ for all $t$ such that $r ( t ) \leq p$ . $\sqcup$

Furthermore, we have:

Theorem 388C The subgroup $1 + H _ { p }$ is a normal subgroup of $G _ { 1 }$ .

Proof. Theorem 388B is equally true if (388b) is replaced by $\alpha = ( 1 + H _ { p } ) \beta$ Hence, for any $\beta \in G _ { 1 }$ , $( 1 + H _ { p } ) \beta = \beta ( 1 + H _ { p } )$ . $\boxed { \begin{array} { r l } \end{array} }$

Quotient groups of the form $G _ { 1 } / ( 1 + H _ { p } )$ can be formed, and we consider their significance in the description of numerical methods. Suppose that $m$ and $\overline { { m } }$ are Runge–Kutta methods with corresponding elementary weight functions $\alpha$ and $\overline { \alpha }$ . If $m$ and $\overline { { m } }$ are related by the requirement that for any smooth problem the results computed by these methods in a single step differ by $O ( h ^ { p + 1 } )$ , then this means that $\alpha ( t ) = \overline { { \alpha } } ( t )$ , whenever $r ( t ) \leq p$ . However, this is identical to the statement that

$$
\overline { { \alpha } } \in ( 1 + H _ { p } ) \alpha ,
$$

which means that $\alpha$ and $\overline { \alpha }$ map canonically into the same member of the quotient group $G _ { 1 } / ( 1 + H _ { p } )$ .

Because we also have the ideal $H _ { p }$ at our disposal, this interpretation of equivalent computations modulo $O ( h ^ { p + 1 } )$ can be extended to approximations represented by members of $G$ , and not just of $G _ { 1 }$ .

The $C ( \xi )$ and $D ( \xi )$ conditions can also be represented using subgroups.

Definition 388D $A$ member $\alpha$ of $G _ { 1 }$ is in $C ( \xi )$ if, for any tree $t$ such that $r ( t ) \leq \xi$ , $\alpha ( t ) = \gamma ( t ) ^ { - 1 } \alpha ( \tau ) ^ { r ( t ) }$ and also

$$
\alpha ( [ t t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) = \frac { 1 } { \gamma ( t ) } \alpha ( [ \tau ^ { r ( t ) } t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) ,
$$

for any $t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } \in T$ .

Theorem 388E The set $C ( \xi )$ is a normal subgroup of $G _ { 1 }$

A proof of this result, and of Theorem 388G below, is given in Butcher (1972).

The $D ( \xi )$ condition is also represented by a subset of $G _ { 1 }$ , which is also known to generate a normal subgroup.

Definition 388F A member $\alpha$ of $G _ { 1 }$ is a member of $D ( \xi )$ if

$$
\alpha ( t u ) + \alpha ( u t ) = \alpha ( t ) \alpha ( u ) ,
$$

whenever $t , u \in T$ and $r ( t ) \leq \xi$ .

Theorem 388G The set $D ( \xi )$ is a normal subgroup of $G _ { 1 }$

The importance of these semi-groups is that $E$ is a member of each of them and methods can be constructed which also lie in them. We first prove the following result:

Theorem 388H For any real $\theta$ and positive integer $\xi$ , $E ^ { ( \theta ) } \in C ( \xi )$ and $E ^ { ( \theta ) } \in D ( \xi )$ .

Proof. To show that $E ^ { ( \theta ) } \in C ( \xi )$ , we note that $E ^ { ( \theta ) } ( t ) = \gamma ( t ) ^ { - 1 } \theta ^ { r ( t ) }$ and that if $E ^ { ( \theta ) }$ is substituted for $\alpha$ in (388c), then both sides are equal to

$$
\frac { \theta ^ { r ( t ) + r ( t _ { 1 } ) + \cdots + r ( t _ { m } ) + 1 } } { ( r ( t ) + r ( t _ { 1 } ) + \cdots + r ( t _ { m } ) + 1 ) \gamma ( t ) \gamma ( t _ { 1 } ) \cdots \gamma ( t _ { m } ) } .
$$

To prove that $E ^ { ( \theta ) } \in D ( \xi )$ , substitute $E$ into (388d). We find

$$
\frac { r ( t ) } { ( r ( t ) + r ( u ) ) \gamma ( t ) \gamma ( u ) } + \frac { r ( u ) } { ( r ( t ) + r ( u ) ) \gamma ( t ) \gamma ( u ) } = \frac { 1 } { \gamma ( t ) } \cdot \frac { 1 } { \gamma ( u ) } .
$$

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

# 39 Implementation Issues

# 390 Introduction

In this section we consider several issues arising in the design and construction of practical algorithms for the solution of initial value problems based on Runge–Kutta methods.

An automatic code needs to be able to choose an initial stepsize and then adjust the stepsize from step to step as the integration progresses. Along with the need to choose appropriate stepsizes to obtain an acceptable accuracy in a given step, there is a corresponding need to reject some steps, because they will evidently contribute too large an error to the overall inaccuracy of the final result. The user of the software needs to have some way of indicating a preference between cheap, but low accuracy, results on the one hand and expensive, but accurate, results on the other. This is usually done by supplying a ‘tolerance’ as a parameter. We show that this tolerance can be interpreted as a Lagrange multiplier $T$ . If $E$ is a measure of the total error to plan for, and $W$ is a measure of the work that is to be allocated to achieve this accuracy, then we might try as best we can to minimize $E + T W$ . This will mean that a high value of $T$ will correspond to an emphasis on reducing computing costs, and a low value of $T$ will correspond to an emphasis on accuracy. It is possible to achieve something like an optimal value of this weighted objective function by requiring the local truncation error to be maintained as constant from step to step. However, there are other views as to how the allocation of resources should be appropriately allocated, and we discuss these in Subsection 393.

If the local truncation error committed in a step is to be the main determining criterion for the choice of stepsize, then we need a means of estimating the local error. This will lead to a control system for the stepsize, and we need to look at the dynamics of this system to ensure that good behaviour is achieved.

It is very difficult to find suitable criteria for adjusting order amongst a range of alternative Runge–Kutta methods. Generally, software designers are happy to construct fixed order codes. However, it is possible to obtain useful variable order algorithms if the stage order is sufficiently high. This applies especially to implicit methods, intended for stiff problems, and we devote at least some attention to this question.

For stiff problems, the solution of the algebraic equations inherent to the implementation of implicit methods is a major issue. The efficiency of a stiff solver will often depend on the management of the linear algebra, associated with a Newton type of solution, more than on any other aspect of the calculation.

# 391 Optimal sequences

Consider an integration over an interval $[ a , b ]$ . We can interpret $a$ as the point $x _ { 0 }$ at which initial information $y ( x _ { 0 } ) = y _ { 0 }$ is given and $b$ as a final point, which we have generally written as $\overline { { x } }$ where we are attempting to approximate $y ( { \overline { { x } } } )$ . As steps of a Runge–Kutta method are carried out we need to choose $h$ for a new step starting at a point $x \in [ a , b ]$ , assuming previous steps have taken the solution forward to this point. From information gleaned from details of the computation, it will be possible to obtain some sort of guide as to what the truncation error is likely to do in a step from $x$ to $x + h$ and, assuming that the method has order $p$ , the norm of this truncation error will be approximately like $C ( \boldsymbol { x } ) h ^ { p + 1 }$ , where $C$ is some positively valued function. Write the choice of $h$ for this step as $H ( x )$ . Assuming that all stepsizes are sufficiently small, we can write the overall error approximately as an integral

$$
E ( H ) = \int _ { a } ^ { b } C ( x ) H ( x ) ^ { p } d x .
$$

The total work carried out will be taken to be the simply the number of steps. For classical Runge–Kutta methods the cost of carrying out each step will be approximately the same from step to step. However, the number of steps is approximately equal to the integral

$$
W ( H ) = \int _ { a } ^ { b } H ( x ) ^ { - 1 } d x .
$$

To obtain an optimal rule for defining values of $H ( x )$ , as $x$ varies, we have to ensure that it is not possible, by altering $H$ , to obtain, at the same time, lower values of both $E ( H )$ and $W ( H )$ . This means that the optimal choice is the same as would be obtained by minimizing $E ( H )$ , for a specified upper bound on $W ( H )$ , or, dually, minimizing $W ( H )$ , subject to an upper bound on $E ( H )$ . Thus we need to optimize the value of $E ( H ) + T W ( H )$ for some positive value of the Lagrange multiplier $T$ .

From calculus of variation arguments, the optimal is achieved by setting to zero the expression $( d / d H ) ( E ( H ) + T W ( H ) )$ . Assuming that $W ( H )$ has the constant value $p$ , chosen for convenience, this means that

$$
p C ( x ) H ( x ) ^ { p - 1 } = p T H ( x ) ^ { - 2 } ,
$$

for all $x$ . Hence, $C ( x ) H ( x ) ^ { p + 1 }$ should be kept equal to the constant value $T$ . In other words, optimality is achieved by keeping the magnitude of the local truncation error close to constant from step to step. In practice, the truncation error associated with a step about to be carried out is not known. However, an estimation of the error in the last completed step is usually available, using techniques such as those described in Section 33, and this can be taken as a usable guide. On the other hand, if a previous attempt to carry out this step has been rejected, because the truncation error was regarded as excessive, then this gives information about the correct value of $h$ to use in a second attempt.

For robustness, a stepsize controller has to respond as smoothly as possible to (real or apparent) abrupt changes in behaviour. This means that the stepsize should not decrease or increase from one step to the next by an excessive ratio. Also, if the user-specified tolerance, given as a bound on the norm of the local truncation error estimate, is ever exceeded, recomputation and loss of performance will result. Hence, to guard against this as much as possible, a ‘safety factor’ is usually introduced into the computation. If $h$ is the estimated stepsize to give a predicted truncation error equal to the tolerance, then some smaller value, such as $0 . 9 h$ , is typically used instead. Combining all these ideas, we can give a formula for arriving at a factor $r$ , to give a new stepsize $r h$ , following a step for which the error estimate is est. The tolerance is written as tol, and it is assumed that this previous step has been accepted. The ratio $r$ is given by

$$
r = \operatorname* { m a x } { \left( 0 . 5 , \operatorname* { m i n } { \left( 2 . 0 , 0 . 9 { \left( \frac { \mathrm { t o l } } { \mathrm { e s t } } \right) } ^ { 1 / ( p + 1 ) } \right) } \right) } .
$$

The three constants, given here with values 0.5, 2.0 and 0.9, are all somewhat arbitrary and have to be regarded as design parameters.

# 392 Acceptance and rejection of steps

It is customary to test the error estimate in a step against $T$ and to accept the step only when the estimated error is smaller. To reduce the danger of rejecting too many steps, the safety factor in (391a) is inserted. Thus there would have to be a very large increase in the rate of error production for a step to be rejected. We now consider a different way of looking at the question of acceptance and rejection of steps. This is based on removing the safety factor but allowing for the possible acceptance of a step as long as the ratio of the error to the tolerance is not too great. We need to decide what ‘too great’ should mean.

The criterion will be based on attempting to minimize the rate of error production plus $T$ times the rate of doing work. Because we are considering the rejection of a completed step with size $h$ , we need to add the work already carried out to the computational costs in some way. Suppose that the error estimated for the step is $r ^ { - ( p + 1 ) } T$ , and that we are proposing to change the stepsize to $r h$ . This will mean that, until some other change is made, the rate of growth of error $+ \textit { T } \times$ work will be $T ( 1 + p ) / r h$ . By the time the original interval of size $h$ has been traversed, the total expenditure will be $T ( 1 + p ) / r h$ . Add the contribution from the work in the rejected step and the total expenditure will be $T ( ( p + 1 ) / r + p )$ .

If, instead, the step had been accepted, the expenditure (linear combination of error and work) would be $T ( r ^ { - ( p + 1 ) } + p )$ . Comparing the two results, we conclude that the step should be accepted if $r ^ { - ( p + 1 ) } \leq ( p + 1 ) / r$ , that is, when

Minimal value of stepsize ratio and maximal value of error/ $T$ for step acceptance   

<table><tr><td>p (p+1)-1/p</td><td>(p +1)(𝑝+1)/p</td></tr><tr><td>1</td><td>0.500 4.00</td></tr><tr><td>2 0.577</td><td>5.20</td></tr><tr><td>3</td><td>0.630 6.35</td></tr><tr><td>4 0.669</td><td>7.48</td></tr><tr><td>5 0.700</td><td>8.59</td></tr><tr><td>6 0.723</td><td>9.68</td></tr><tr><td>7 0.743</td><td>10.77</td></tr><tr><td>8 0.760</td><td>11.84</td></tr><tr><td>9 0.774</td><td>12.92</td></tr><tr><td>10 0.787</td><td>13.98</td></tr></table>

$$
r \geq ( p + 1 ) ^ { - 1 / p } ,
$$

and rejected otherwise. Looked at another way, the step should be accepted if the error estimated in a step, divided by the tolerance, does not exceed $( p + 1 ) ^ { ( p + 1 ) / p }$ . Values of $( p + 1 ) ^ { - 1 / p }$ and $( p + 1 ) ^ { ( p + 1 ) / p }$ are given in Table 392(I).

# 393 Error per step versus error per unit step

The criterion we have described for stepsize selection is based on the principle of ‘error per step’. That is, a code designed on this basis attempts to maintain the error committed in each step as close to constant as possible. An alternative point of view is to use ‘error per unit step’, in which error divided by stepsize is maintained approximately constant. This idea is attractive from many points of view. In particular, it keeps the rate of error production under control and is very natural to use. In an application, the user has to choose a tolerance which indicates how rapidly he or she is happy to accept errors to grow as the solution approximation evolves with time.

Furthermore, there is a reasonable expectation that, if a problem is attempted with a range of tolerances, the total truncation error will vary in more or less the same ratio as the tolerances. This state of affairs is known as ‘proportionality’, and is widely regarded as being desirable. On the other hand, if the error per step criterion is used we should hope only for the global errors to vary in proportion to $\mathrm { t o l } ^ { p / ( p + 1 ) }$ . The present author does not regard this as being in any way inferior to simple proportionality. The fact that error per step is close to producing optimal stepsize sequences, in the sense we have described, seems to be a reason for considering, and even preferring, this choice in practical codes.

From the user point of view, the interpretation of the tolerance as a Lagrange multiplier is not such a difficult idea, especially if tol is viewed not so much as ‘error per step’ as ‘rate of error production per unit of work’. This interpretation also carries over for algorithms for which $p$ is still constant, but the work might vary, for some reason, from one step to the next.

# 394 Control-theoretic considerations

Controlling the stepsize, using a ratio of $h$ in one step to $h$ in the previous step, based on (391a), can often lead to undesirable behaviour. This can come about because of over-corrections. An error estimate in one step may be accidentally low and this can lead to a greater increase in stepsize than is justified by the estimate found in the following step. The consequent rejection of this second step, and its re-evaluation with a reduced stepsize, can be the start of a series of similarly disruptive and wasteful increases and decreases.

In an attempt to understand this phenomenon and to guard against its damaging effects, an analysis of stepsize management using the principles of control theory was instituted by Gustafsson, Lundh and S¨oderlind (1988). The basic idea that has come out of these analyses is that PI control should be used in preference to I control. Although these concepts are related to continuous control models, they have a discrete interpretation. Under the discrete analogue, I control corresponds to basing each new stepsize on the most recently available error estimate, whereas PI control would make use of the estimates found in the two most recently completed steps.

If we were to base a new stepsize on a simplified alternative to (391a), using the ratio $r = ( \mathrm { e s t / t o l } ) ^ { 1 / ( p + 1 ) }$ , this would correspond to what is known in control theory as ‘dead-beat’ control. On the other hand, using the ratio $r = ( \mathrm { t o l } / \mathrm { e s t } ) ^ { \alpha / ( p + 1 ) }$ , where $0 < \alpha < 1$ , would correspond to a damped version of this control system. This controller would not respond as rapidly to varying accuracy requirements, but would be less likely to change too quickly for future behaviour to deal with. Going further, and adopting PI control, would give a stepsize ratio equal to

$$
r _ { n } = \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 1 } } } \right) ^ { \alpha / ( p + 1 ) } \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 2 } } } \right) ^ { \beta / ( p + 1 ) } .
$$

In this equation, $r _ { n }$ is the stepsize ratio for determining the stepsize $h _ { n }$ to be used in step $n$ . That is, if $h _ { n - 1 }$ is the stepsize in step $n - 1$ , then $h _ { n } = r _ { n } h _ { n - 1 }$ . The quantities $\mathrm { e s t } _ { n - 1 }$ and $\mathrm { e s t } _ { n - 2 }$ , denote the error estimates found in steps $n - 1$ and $n - 2$ , respectively.

For convenience, we work additively, rather than multiplicatively, by dealing with $\log ( h _ { n } )$ and $\log ( r _ { n } )$ rather than with $h _ { n }$ and $r _ { n }$ themselves. Let $\xi _ { n - 1 }$ denote the logarithm of the stepsize that would be adopted in step $n$ , if deadbeat control were to be used. That is,

$$
\xi _ { n - 1 } = \log ( h _ { n - 1 } ) + \frac { 1 } { p + 1 } ( \log ( \mathrm { t o l } ) - \log ( \mathrm { e s t } _ { n - 1 } ) ) .
$$

Now let $\eta _ { n }$ denote the logarithm of the stepsize actually adopted in step $n$ . Thus we can write dead-beat control as

$$
\eta _ { n } = \xi _ { n - 1 }
$$

and the modification with damping factor $\alpha$ as

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } + \alpha \xi _ { n - 1 } .
$$

For the PI controller (394a), we have

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } - \beta \eta _ { n - 2 } + \alpha \xi _ { n - 1 } + \beta \xi _ { n - 2 } .
$$

Appropriate choices for the parameters $\alpha$ and $\beta$ have been discussed by the original authors. Crucial considerations are the stable behaviour of the homogeneous part of the difference equation (394b) and the ability of the control system to respond sympathetically, but not too sensitively, to changing circumstances. For example, $\alpha = 0 . 7$ and $\beta = - 0 . 4$ , as proposed by Gustafsson (1991), works well. Recently, further work has been done on control-theoretic approaches to stepsize control by S¨oderlind (2002).

# 395 Solving the implicit equations

For stiff problems, the methods of choice are implicit. We discuss some aspects of the technical problem of evaluating the stages of an implicit Runge–Kutta method. For a one-stage method, the evaluation technique is also similar for backward difference methods and for Runge–Kutta and general linear methods that have a lower triangular coefficient matrix.

For these simple methods, the algebraic question takes the form

$$
Y - h \gamma f ( X , Y ) = U ,
$$

where $X$ and $U$ are known. Let $J ( X , Y )$ denote the Jacobian matrix with elements given by

$$
J ( X , Y ) _ { i j } = \frac { \partial f _ { i } } { \partial y _ { j } } ( X , Y ) , \qquad i , j , = 1 , 2 , \ldots , N .
$$

A full Newton scheme would start with the use of a predictor to obtain a first approximation to $Y$ . Denote this by $Y ^ { \left[ 0 \right] }$ and update it with a sequence of approximations $Y ^ { \left\lfloor i \right\rfloor }$ , $i = 1 , 2 , \dots$ , given by

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \Delta ,
$$

where

$$
( I - h \gamma J ( X , Y ^ { [ i - 1 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U .
$$

Although the full scheme has the advantage of quadratic convergence, it is usually not adopted in practice. The reason is the excessive cost of evaluating the Jacobian $J$ and of carrying out the LU factorization of the matrix $I - h \gamma J$ . The Newton scheme can be modified in various ways to reduce this cost. First, the re-evaluation of $J$ after each iteration can be dispensed with. Instead the scheme (395b) can be replaced by

$$
( I - h \gamma J ( X , Y ^ { [ 0 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U ,
$$

and for many problems this is almost as effective as the full Newton method. Even if more iterations are required, the additional cost is often less than the saving in $J$ evaluations and LU factorizations.

Secondly, in the case of diagonally implicit methods, it is usually possible to evaluate $J$ only once per step, for example at the start of the first stage. Assuming the Jacobian is sufficiently slowly varying, this can be almost as effective as evaluating the Jacobian once for each stage.

The third, and most extreme, of the Jacobian update schemes is the use of the same approximation over not just one step but over many steps. A typical algorithm signals the need to re-evaluate $J$ only when the rate of convergence is sufficiently slow as to justify this expenditure of resources to achieve an overall improvement. When $J$ is maintained at a constant value over many steps, we have to ask the further question about when $I \mathrm { ~ - ~ } h \gamma J$ should be refactorized. Assuming that $\gamma$ is unchanged, any change in $h$ will affect the convergence by using a factorization of this matrix which is based not only on an incorrect value of $J$ , but on what may be a vastly different value of $h$ .

It may be possible to delay the refactorization process by introducing a ‘relaxation factor’ into the iteration scheme. That is, when $\Delta$ has been computed in a generalized form of (395b), the update takes the form

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \theta \Delta ,
$$

where $\theta$ is a suitably chosen scalar factor. To analyse how this works, suppose for simplicity that $J$ is constant but that $h$ has changed from $\overline { { h } }$ at the time the factorization took place to $r { \bar { h } }$ at the time a generalized Newton step is being carried out. As a further simplification, assume that $f ( x , y ) = J y + V$ and that we are exploring the behaviour in a direction along along an eigenvector corresponding to an eigenvalue $\lambda$ . Write $z = \overline { { h } } \gamma \lambda$ . Under these assumptions the iteration scheme effectively seeks a solution to an equation of the form

$$
\eta - r z \eta = a ,
$$

with solution $\eta = \eta ^ { * } = a / ( 1 - r )$ , using an iteration scheme which replaces $\eta ^ { * } + \epsilon$ by $\eta ^ { * } + \phi ( z ) \epsilon$ , where

$$
\phi ( z ) = 1 - \theta \frac { 1 - r z } { 1 - z } .
$$

Convergence will depend on the magnitude of $\phi ( z )$ for all $z$ that are likely to arise. Values of $z$ near zero correspond to non-stiff components of the problem, and values of $z$ with large magnitude in the left half-plane correspond to stiff components. Hence, it seems desirable to choose $\theta$ to minimize $| \phi ( z ) |$ for $z$ in the left half-plane. The value that achieves this is

$$
\theta = { \frac { 2 } { 1 + r } } .
$$

For fully implicit Runge–Kutta methods, the problem of evaluating the stages becomes much more complicated and potentially more costly. For a method with coefficient matrix $A$ , we need to consider all stages at the same time. Let $Y$ denote the $s N$ -dimensional vector made up from $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ . Furthermore the approximation sequence will be written as $Y ^ { \left[ j \right] }$ , $j = 0 , 1 , \ldots$ , each also made up from $s$ subvectors, and $\Delta$ will denote a vector in $\mathbb { R } ^ { s N }$ made up from the subtrahends in each of the $s$ components in iteration $i$ . Thus

$$
\begin{array} { r } { Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad Y ^ { [ i ] } = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i ] } } \end{array} \right] , \quad \Delta = \left[ \begin{array} { c } { \Delta _ { 1 } } \\ { \Delta _ { 2 } } \\ { \vdots } \\ { \Delta _ { s } } \end{array} \right] = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i - 1 ] } - Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i - 1 ] } - Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i - 1 ] } - Y _ { s } ^ { [ i ] } } \end{array} \right] . } \end{array}
$$

In place of (395a), the algebraic equations to solve in a step take the form

$$
Y - h A \otimes f ( X , Y ) = U \in \mathbb { R } ^ { s N } .
$$

Note that $f ( X , Y )$ denotes a vector in $\mathbb { R } ^ { s N }$ made up from subvectors of the form $f ( X _ { j } , Y _ { j } )$ , $j = 1 , 2 , \dots , s$ . The iteration scheme consists of solving the equations

$$
\Delta _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } J \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) \Delta _ { k } = Y _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } f \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) - U _ { i } ,
$$

and then carrying out the update $Y _ { j } ^ { [ i ] } = Y _ { j } ^ { [ i - 1 ] } - \Delta _ { j }$ , $j = 1 , 2 , \dots , s$ . If it is assumed that Jacobians are evaluated only once per step, or even less frequently, then we can write (395c) in the simplified form

$$
( I _ { s } \otimes I _ { N } - h A \otimes J ) \Delta = Y ^ { [ i - 1 ] } - h A \otimes F ^ { [ i - 1 ] } - U ,
$$

where $F ^ { [ i - 1 ] }$ is the vector with $k$ th subvector equal to $f \big ( X _ { k } , Y _ { k } ^ { \lfloor i - 1 \rfloor } \big )$ . Here $J$ is a single approximation to the $n \times n$ Jacobian matrix. One of the advantages of using a single $J$ approximation is the fact that it is possible to operate, for example, with similarity transformations, on the coefficient matrix $A$ and $J$ independently.

If no such transformation is carried out, the computational costs can become very severe. The LU factorization of the matrix on the left-hand side of (395d) requires a number of operations proportional to $s ^ { 3 } N ^ { 3 }$ , compared with just $N ^ { 3 }$ if $s = 1$ . However, if $A = T ^ { - 1 } \widehat { A } T$ , where $\widehat { A }$ has a structure close to diagonal, then the cost reduces to something like $s N ^ { 3 }$ .

# Exercises 39

39.1 An implicit Runge–Kutta method is to be implemented for the solution of non-stiff problems using functional iteration to solve the nonlinear equations. How should the stepsize be selected?

39.2 A Runge–Kutta method of order $p$ is used over an interval of length $X$ . Suppose that for a subinterval of length $( 1 - \theta ) X$ the error in a step of length $h$ is $C h ^ { p + 1 }$ , and for the remaining distance $\theta X$ the error is $\alpha C h ^ { 5 }$ . Assume that a large number $N$ of steps are performed, of which $( 1 - \phi ) N$ are in the first subinterval and $\phi N$ are in the second subinterval. Determine the value of $\phi$ which will minimize the total error committed in the integration.

39.3 Compare the result found in Exercise 39.2 with the result that would be obtained from an ‘error per unit step’ argument.
