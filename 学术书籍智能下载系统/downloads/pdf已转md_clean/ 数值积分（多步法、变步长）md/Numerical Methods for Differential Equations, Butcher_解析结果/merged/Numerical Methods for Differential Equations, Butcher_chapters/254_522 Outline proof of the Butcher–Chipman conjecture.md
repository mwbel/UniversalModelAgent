# 522 Outline proof of the Butcher–Chipman conjecture

The essential elements of the proof are just as in the proof of Theorem 355G. That is, the result hinges on the fact that if $2 \nu _ { 0 } - \widetilde { p } > 2$ , then an up arrow from zero must be tangential to the imaginary axis, or protrude into the left half-plane, and terminate at a pole. This will mean that this pole will be in the left half-plane or else the arrow will have to cross the imaginary axis to reach this pole.

The missing detail, which we will now focus on, is the fact that each pole is at the termination of an up arrow from zero. We cannot prove this in a simple way based on non-crossing of up and down arrows, because the relation $\Phi ( w \exp ( z ) , z ) = 0$ now defines a Riemann surface, rather that $w$ as a function of $z$ . The way we will proceed is (i) to modify the order arrow diagram slightly to avoid the need to deal in a special way with special points which arise in the diagram and (ii) to look at changes in the structure of the diagram as the approximation is changed smoothly from one approximation to another.

The modification to arrow diagrams is illustrated in the case of the [4, 2] Pad´e approximation. Consider Figure $5 2 2 ( \mathrm { i } )$ , where two versions of the arrow system are presented. On the left is the standard diagram and on the right is its modified form. The modifications are of two types. First, all arrows are moved an infinitesimal distance to the right to avoid an ambiguity caused by ‘stagnation points’, such as at $z = 0 .$ The ambiguity is that an up arrow arriving at a stagnation point is equally related to arrows leaving this point on the left and on the right. Under the modification, this arrow can be regarded as being continued as an up arrow to the right. For example, in the approximation shown in Figure $5 2 2 ( \mathrm { i } )$ , arrows arrive in directions $0 , 2 \pi / 7 , 4 \pi / 7 , \ldots , 1 2 \pi / 7 .$ In the diagram on the right these are continued unambiguously as outgoing up arrows in the directions $0 \pi / 7 , 3 \pi / 7 , 5 \pi / 7 , \dots , 1 3 \pi / 7$ , respectively. The second modification is to replace poles and zeros as termination points for up and down arrows respectively, by additional sheets in the Riemann surface. The way this done, in the case of poles, is to introduce the approximation defined by

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0007_pages_0421-0484/auto/images/555f0c6005b246c4acae5cc5aaa114db6092a5b008b706cab7f7449be19dae54.jpg)  
Unmodified (left) and modified (right) order arrows for the approximation [4, 2]

$$
( 1 - t ) \Phi ( w , z ) + t \widetilde { \Phi } ( w , z ) ,
$$

where $\widetilde { \Phi }$ is defined from $\left[ 0 \quad \nu _ { 0 } \quad \nu _ { 1 } \quad \cdot \cdot \cdot \quad \nu _ { k } \right]$ , normalized so that $\widetilde P _ { 1 } ( 0 ) = 1$ . If we take the limit as $t  0$ , the Riemann surface limit does not exist but the projection of the new sheet onto the $\mathcal { L }$ plane does exist. This new plane has the same projection as the order arrow system for

$$
\pm \exp ( z ) + P _ { 1 } ( z ) ,
$$

where the sign is chosen to agree with the coefficient of $w ^ { r + 1 }$ in $\widetilde { \Phi } ( w , z )$ . A similar construction is used for a new bottom sheet defined from the zeros of $P _ { k }$ . This means that the artificial bottom sheet is found as the limit as $t \longrightarrow 0$ of the arrow system for $w \Phi ( w , z ) \pm t$ . There is no reason why this should not be replaced by $w ^ { n } \Phi ( w , z ) \pm t$ where $n$ is any positive integer and we would obtain similar behaviour.

Given an order $p$ approximation $[ \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { k } ]$ , denoted by $\Phi$ , we can construct, for any $t \in [ 0 , 1 ]$ , the approximation $\Phi _ { t } = t \Phi + ( 1 - t ) \Phi _ { 0 }$ , where $\Phi _ { 0 }$ is the $\lfloor \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { r } - 1 \rfloor$ approximation of order $p - 1$ . Because of the uniqueness of generalized Pad´e approximations, $\Phi _ { t }$ will have order only $p - 1$ if $t < 1$ . The parameter $t$ now takes the role of homotopy variable and we will consider the structure of the arrow system as $t$ moves from 0 to 1. We illustrate in Figure 522(ii) what happens in a series of diagrams in the case $p = 4 , \nu _ { 0 } = 2$ , for $t = 0$ , $t = 0 +$ (a small positive value), $t = 1 -$ (a value less than but close to 1) and $t = 1$ . Note that these are stylized diagrams and apply to a generic situation. That is, they could apply to any of the approximations, [2, 2], $[ 2 , 1 , 0 ]$ , $\lfloor 2 , 0 , 1 \rfloor$ , $[ 2 , 0 , 0 ]$ etc. Furthermore, the diagrams are distorted to

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0007_pages_0421-0484/auto/images/cc9dd24fcdc27d1bf8180c4360f66618de51c41d77b1eaa1bb2d8a9adefbd43d.jpg)  
Homotopy from an order 3 to an order 4 approximation

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0007_pages_0421-0484/auto/images/5f11880b6c0744f803a6222f454856be888e597bf4b0b7071b21a2d25aff76bd.jpg)  
Illustrating the impossibility of A-stable methods with

$$
2 \nu _ { 0 } - p > 2
$$

avoid overlapping lines. For $t > 0$ , a new arrow is introduced; this is shown as a prominent line. As $t$ approaches 1, it moves into position as an additional up arrow to 0 and an additional up arrow away from 0.

In such a homotopic sequence as this, it is not possible that an up arrow associated with a pole is detached from 0 because either this would mean a loss of order or else the new arrow would have to pass through 0 to compensate for this. However, at the instant when this happens, the order would have been raised to $p$ , which is impossible because of the uniqueness of the $[ \nu _ { 0 } , \nu _ { 1 } , \ldots , \nu _ { k } ]$ approximation.

To complete this outline proof, we recall the identical final step in the proof of Theorem 355G which is illustrated in Figure 522(iii). If $2 \nu _ { 0 } > p + 2$ , then the up arrows which terminate at poles subtend an angle $( \nu _ { 0 } - 1 ) 2 \pi / ( p + 1 ) \geq \pi$ . If this angle is $\pi$ , as in (a) in this figure, then there will be an up arrow leaving $0$ in a direction tangential to the imaginary axis. Thus there will be points on the imaginary axis where $| w | > 1$ . In the case of (b), an up arrow terminates at a pole in the left half-plane, again making A-stability impossible. Finally, in (c), where an up arrow leaves 0 and passes into the left half-plane, but returns to the right half-plane to terminate at a pole, it must have crossed the imaginary axis. Hence, as in (a), there are points on the imaginary axis where $| w | > 1$ and A-stability is not possible.
