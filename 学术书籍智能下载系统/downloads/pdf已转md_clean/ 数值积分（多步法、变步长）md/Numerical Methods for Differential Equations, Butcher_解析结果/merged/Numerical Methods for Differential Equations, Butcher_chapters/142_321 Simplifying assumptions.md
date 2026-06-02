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

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/fb84986ce75b33490495146aad335c44a6458ed7536f47415bf8920a02f3dc08.jpg)  
The $C ( k )$ condition relating $\textstyle \sum _ { j } a _ { i j } c _ { j } ^ { k - 1 }$ (left-hand tree) to $c _ { i } ^ { k }$ (right-hand tree). The underlying tree is a pohutukawa (Metrosideros excelsa), also known as the ‘New Zealand Christmas tree’ because its bright red flowers bloom at Christmas-time.

In addition to (321a), we can consider the possibility that conditions like

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \quad i = 1 , 2 , \ldots , s ,
$$

hold for $k = 1 , 2 , \ldots .$ Assuming that these hold for $1 \leq k \leq \xi$ , we denote this collection of conditions by $C ( \xi )$ . The consequences of $C ( \xi )$ are that, for any pair of trees $t _ { 1 }$ and $t _ { 2 }$ for which $\Phi ( t _ { 1 } )$ contains a factor $a _ { i j } c _ { j } ^ { k - 1 }$ , $\Phi ( t _ { 2 } )$ contains a factor $\scriptstyle { \frac { 1 } { k } } c _ { i } ^ { k }$ and the remaining factors are identical in the two expressions, then $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ implies $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ . We illustrate this in Figure 321(i).

The $D ( k )$ conditions interrelate three trees $t _ { 1 }$ , $t _ { 2 }$ and $t _ { 3 }$ for which the corresponding elementary weights differ only in that $\Phi ( t _ { 1 } )$ has a factor $b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ , $\Phi ( t _ { 2 } )$ has a factor $b _ { j }$ and $\Phi ( t _ { 3 } )$ has a factor $b _ { j } c _ { j } ^ { k }$ . This means that these trees have forms like those shown in Figure 321(ii).

We illustrate this further, for the case $k = 1$ , in Table 321(II). Note that if $D ( 1 )$ holds, then the truth of $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ follows from $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ and $\Phi ( t _ { 3 } ) = 1 / \gamma ( t _ { 3 } )$ . For explicit methods, $D ( 2 )$ cannot hold, for similar reasons to the impossibility of $C ( 2 )$ . For implicit methods $D ( s )$ is possible, as we shall see in Section 342.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/ff9c9de1b79338b1593c984ed36a7e9e8e2f72cce9e35ce52ef10fe65ea4fc75.jpg)  
Figure 321(ii) The $D ( k )$ condition relating $\sum _ { i } b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ (left-hand tree) to $b _ { j }$ (middle tree) and $b _ { j } c _ { j } ^ { k }$ (right-hand tree). The underlying tree is a kauri (Agathis australis). Although the immature tree shown is only a few metres tall, the most famous kauri tree, Tane Mahuta (Lord of the Forest), has a height of $4 0 \textrm { m }$ and a diameter, 1.5 m above ground level, of 5.21 m.

Sets of three related trees illustrating $D ( 1 )$   

<table><tr><td rowspan="3">t1</td><td rowspan="3">(t1)=</td><td>1</td><td rowspan="3">t2</td><td rowspan="3">Φ(t2) =</td><td>1</td><td rowspan="3">t3</td><td rowspan="3">（(t3)=</td><td>1</td></tr><tr><td>(t1)</td><td>(t2）</td><td>（t3)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijcj=</td><td></td><td></td><td>∑bcj=</td><td></td><td>Y</td><td>∑bj²=</td><td></td></tr><tr><td></td><td></td><td></td><td>：</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>？</td><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td>∑biaijc²=12</td><td></td><td></td><td>∑b=</td><td></td><td></td><td>∑bjc=1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijajkck =</td><td></td><td></td><td></td><td></td><td>∑bjCjajkCk=</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>∑bjajkck=</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Finally, the condition $E ( \eta , \zeta )$ states that

$$
\sum b _ { i } c _ { i } ^ { k - 1 } a _ { i j } c _ { j } ^ { l - 1 } = \frac { 1 } { l ( k + l ) } , \qquad k = 1 , 2 , \ldots , \eta , \quad l = 1 , 2 , \ldots , \zeta .
$$

This simply expresses the fact that the order condition $\Phi ( t ) = 1 / \gamma ( t )$ is satisfied for trees $t = [ \tau ^ { k - 1 } [ \tau ^ { l - 1 } ] ]$ for $k \leq \eta$ and $l \leq \zeta$ . This is a necessary condition for orders at least $\eta + \zeta$ .
