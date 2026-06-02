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
