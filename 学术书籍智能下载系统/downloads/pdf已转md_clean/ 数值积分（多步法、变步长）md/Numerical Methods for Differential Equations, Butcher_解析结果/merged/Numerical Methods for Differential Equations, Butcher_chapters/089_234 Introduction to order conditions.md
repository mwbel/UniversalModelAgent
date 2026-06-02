# 234 Introduction to order conditions

As the order being sought increases, the algebraic conditions on the coefficients of the method become increasingly complicated. The pattern behind these conditions is known and, in this brief introduction to the order conditions, we state the results without any justification and show, by examples, how they are used.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/87985150b311a58e0ff0506897b42884a8b4cbf36973f1d4d4839ba2baed0f24.jpg)  
Some illustrative rooted trees

Let $T$ denote the set of all ‘rooted trees’. These are simple combinatorial graphs, which have the properties of being connected, having no cycles, and having a specific vertex designated as the root. The ‘order’ of a tree is the number of vertices in this tree. If the order is greater than 1, then the ‘leaves’ of a tree are the vertices from which there are no outward-growing arcs; in other words, a leaf is a vertex, other than the root, which has exactly one other vertex joined to it.

An assortment of trees of various orders, with leaves and the root indicated in each case, is shown in Figure $2 3 4 ( \mathrm { i } ) .$ In pictorial representations of particular rooted trees, as in this figure, we use the convention of placing the root at the lowest point in the picture.

For each tree $t$ , a corresponding polynomial in the coefficients of the method can be written down. Denote this by $\Phi ( t )$ . Also associated with each tree $t$ is an integer $\gamma ( t )$ . We now explain how $\Phi ( t )$ and $\gamma ( t )$ are constructed.

In the case of $\Phi ( t )$ , associate with each vertex of the tree, except the leaves, a label $i$ , $j , \ldots ,$ and assume that $i$ is the label attached to the root. Write down a sequence of factors of which the first is $b _ { i }$ . For each arc of the tree, other than an arc that terminates in a leaf, write down a factor, say $a _ { j k }$ , where $j$ and $k$ are the beginning and end of the arc (assuming that all directions are in the sense of movement away from the root). Finally, for each arc terminating at a leaf, write down a factor, say $c _ { j }$ , where $j$ is the label attached to the beginning of this arc. Having written down this sequence of factors, sum their product for all possible choices of each of the labels, in the set $\{ 1 , 2 , \ldots , s \}$ .

To find the value of $\gamma ( t )$ , associate a factor with each vertex of the tree. For the leaves this factor is 1, and for all other vertices it is equal to the sum of the factors attached to all outward-growing neighbours, plus 1. The product of the factors, for all vertices of the tree, is the value of $\gamma ( t )$ .

The rooted trees up to order 4   

<table><tr><td>Tree</td><td>·</td><td>：</td><td>?</td><td>：</td></tr><tr><td>Order</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>重</td><td>∑ibi</td><td>∑ibiCi</td><td>∑ibic</td><td>∑ijbiaijCj</td></tr><tr><td>Y</td><td>1</td><td>2</td><td>3</td><td>6</td></tr></table>

<table><tr><td>Tree</td><td>? ?</td><td>丫</td><td>：</td></tr><tr><td>Order</td><td>4 4</td><td>4</td><td>4</td></tr><tr><td>重</td><td>∑ibic</td><td></td><td>∑ijbiciaijCj ∑ijbiaijc² ∑ijkbiaijajkCk</td></tr><tr><td>Y</td><td>4 8</td><td>12</td><td>24</td></tr></table>

The values of these quantities are shown in Table 234(I), for each of the eight trees with orders up to 4. A further illustrative example is given by the tree

$$
t = \alpha ^ { Y }
$$

for which $\begin{array} { r } { \Phi ( t ) = \sum _ { i j } b _ { i } c _ { i } ^ { 2 } a _ { i j } c _ { j } ^ { 2 } } \end{array}$ and $\gamma ( t ) ~ = ~ 1 8$ . Details of the calculation of these quantities are presented in Figure 234(ii). On the left-hand diagram labels $i$ and $j$ are attached to the non-terminal vertices, as used in the formula for $\Phi ( t )$ , using the factors shown in the middle diagram. On the right-hand diagram, the factors are shown whose product gives the value of $\gamma ( t )$ .

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/f186d3236766e589fa70ce8741ddc83be0bb3dc7bf22dad33fa708803aebd53c.jpg)  
Calculation details for $\Phi ( t )$ and $\gamma ( t )$ , where $t = \Phi$
