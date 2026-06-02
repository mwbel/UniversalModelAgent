# 521 Methods with maximal stability order

Although a full discussion of the order of general linear methods will be postponed until Section 53, we look here at the relationship between stability and methods with a property closely related to order.

Definition 521A A method with stability function $\Phi ( w , z )$ has ‘stability order’ $\widetilde { p }$ if

$$
\Phi ( \exp ( z ) , z ) = O ( z ^ { \widetilde { p } + 1 } ) .
$$

Suppose the stability function is given by

$$
\Phi ( w , z ) = \sum _ { j = 0 } ^ { k } w ^ { k - j } \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { j } ,
$$

where $k$ is the $w$ -degree of $\Phi$ and $\nu _ { j }$ is the $z$ -degree of the coefficient of $w ^ { k - j }$ . We can regard the sequence of integers

$$
\nu = [ \nu _ { 0 } , \nu _ { 1 } , \ldots , \nu _ { k } ] ,
$$

as representing the complexity of the stability function $\Phi$ . To include all sensible cases without serious redundancies, we always assume that $\nu _ { j } \geq - 1$ for $j = 0 , 1 , 2 , \ldots , k$ with strict inequality in the cases $j = 0$ and $j = k$ .

It is interesting to ask the question: ‘For a given sequence $\nu$ , what is the highest possible stability order?’. The question can be looked at in two parts. First, there is the question of determining for what $\widetilde { p }$ it is possible to find a function $\Phi$ with a given complexity and with stability order $\hat { p }$ . Secondly, there is the question of finding a general linear method corresponding to a given $\Phi$ , with order $p$ as close as possible to $\widetilde { p }$ . The first half of the question can be firmly answered and is interesting since it gives rise to speculations about possible generalizations of the Ehle results on rational approximations to the exponential function. The definitive result that we have referred to is as follows:

Theorem 521B For given $\nu$ , the maximum possible stability order is given by

$$
\widetilde { p } = \sum _ { j = 0 } ^ { k } ( \nu _ { j } + 1 ) - 2 .
$$

Proof. If order higher than $\hat { p }$ given by (521a) is possible, then

$$
\sum _ { j = 0 } ^ { k } \exp ( ( k - j ) z ) \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { l } = C _ { \widetilde { p } + 2 } z ^ { \widetilde { p } + 2 } + C _ { \widetilde { p } + 3 } z ^ { \widetilde { p } + 3 } + \cdots ,
$$

where the right-hand side is convergent for any $z$ . Differentiate $\nu _ { k } + 1$ times and multiply the result by $\exp ( - z )$ . We now have a stability function with complexity $[ \nu _ { 0 } , \nu _ { 1 } , \dots , \nu _ { k - 1 } ]$ , where the $w$ -degree can be reduced even further if $\nu _ { k - 1 } = - 1$ . Furthermore, the new approximation also has a stability order contrary to the bound we are trying to prove. Thus, by an induction argument


<!-- chunk 0007: pages 421-484 -->
we reduce to the case $k = 0$ , and it remains to prove that there does not exist a non-zero polynomial $P$ of degree $\nu _ { 0 }$ such that

$$
P ( z ) = O ( z ^ { \nu _ { 0 } + 1 } ) .
$$

To show that an approximation with stability order $\hat { p }$ given by (521a) exists, it is possible to reverse the non-existence argument and to construct the required stability function recursively, but we use a different approach.

Consider the rational function

$$
\phi ( t ) = \prod _ { j = 0 } ^ { k } ( t + j ) ^ { - \nu _ { j } - 1 } ,
$$

with partial fraction expansion which can be written in the form

$$
\phi ( t ) = \sum _ { j = 0 } ^ { k } \sum _ { l = 0 } ^ { \nu _ { j } } \frac { l ! \alpha _ { j l } } { ( j + t ) ^ { l + 1 } } .
$$

Calculate the integral

$$
\frac { 1 } { 2 \pi i } \oint _ { C } \phi ( t ) \exp _ { \widetilde { p } } ( t z ) d t ,
$$

where

$$
\exp _ { \widetilde { p } } ( z ) = \sum _ { j = 0 } ^ { \widetilde { p } } \frac { z ^ { j } } { j ! }
$$

is the polynomial of degree $\hat { p }$ approximating the exponential function to within $O ( z ^ { \overleftarrow { p } + 1 } )$ and $C$ is a circular counter-clockwise contour, centred at 0 and with radius $R > k$ . Using the partial fraction form of $\phi$ , (521c) is found to be

$$
\sum _ { j = 0 } ^ { k } \sum _ { l = 0 } ^ { \nu _ { j } } \alpha _ { j l } z ^ { l } \exp _ { \widetilde { p } - l } ( - z j ) ,
$$

but using (521b), the integral can be bounded in terms of $R ^ { - 1 }$ for large $R$ , and is therefore zero. Use the fact that $z ^ { l } \exp _ { \widetilde { p } - l } ( - z j ) = z ^ { l } \exp ( - z j ) + { \cal O } ( z ^ { \widetilde { p } + 1 } )$ and the result follows. $\sqcup$

Because of the maximal order properties of these approximations, they will be known as ‘generalized Pad´e approximations’. Some examples are given in Table 521(I). In each case, $\Phi ( w , z )$ is scaled so that the coefficient of $w ^ { k } z ^ { 0 }$ is $^ { 1 }$ . Some of these functions correspond to A-stable methods, and this is indicated in the table. The entry for $\nu = [ 1 , 0 , 1 ]$ is reducible, in the sense that $\Phi ( w , z )$ factorizes into the approximation for [1, 1] multiplied by $w - 1$ ; the order 3 suggested for this method is, of course, an illusion.

Some generalized Pad´e approximations   

<table><tr><td></td><td>p</td><td>重(w,2)</td><td>Remarks</td></tr><tr><td>[1,0,0]2</td><td></td><td>(1-²z)w²-w+</td><td>A-stable</td></tr><tr><td>[1,0,1]3</td><td></td><td>(1-z)w²-2w+1+½z</td><td>A-stable</td></tr><tr><td>[1,1,0]3</td><td></td><td>(1-z)w²-（g+z)-½</td><td></td></tr><tr><td>[2,0,0]3</td><td></td><td>(1-/z+²z²）w²-w+↓</td><td>A-stable</td></tr><tr><td>[2,0,1]</td><td></td><td>(1-+）w²-++</td><td>A-stable</td></tr><tr><td>[2,1,0]</td><td>4</td><td>(1-1+z²）w²-（1+)-17</td><td>A-stable</td></tr><tr><td>[2,0,2]5</td><td></td><td>(1-+z²）w²-2ω+1++²</td><td>see text</td></tr><tr><td></td><td></td><td>7 2 1 15 15</td><td>比</td></tr><tr><td></td><td></td><td>[3,0,0]4（1-1+2²- 16 w+ 15 15</td><td>A-stable</td></tr><tr><td></td><td>[4,0,0] 5(1-x+</td><td>4 23 2 z4）w² 32 w+ 31 93 31</td><td></td></tr></table>

The approximation based on $\nu = \left\lfloor 2 , 0 , 2 \right\rfloor$ is especially interesting. According to the result formerly known as the Daniel–Moore conjecture (Daniel and Moore, 1970), it cannot correspond to an A-stable method and also have order $p = 5$ , because it does not satisfy the necessary condition $p \leq 2 s$ . However, the solutions to the equation $\Phi ( w , z ) = 0$ for $z = i y$ satisfy

$$
| w | ^ { 2 } = \left| { \frac { 8 \pm i y { \sqrt { 9 + y ^ { 2 } } } } { 8 - y ^ { 2 } - 5 i y } } \right| ^ { 2 } = 1 .
$$

By the maximum modulus principle, the bound $| w | \leq 1$ holds in the left halfplane and the only point in the closed left half-plane where the two $w$ roots have equal values on the unit circle is when $z = 0$ . For Obreshkov methods we have to regard this as representing instability in the sense of Dahlquist. On the other hand, general linear methods with this stability function exist with $V = I$ and therefore convergent methods are definitely possible. A possible method satisfying this requirement is

$$
\left[ \begin{array} { r } { { \frac { 5 } { 1 6 } } \qquad { \frac { 1 0 7 } { 4 8 } } } \\ { { - { \frac { 2 1 } { 1 7 1 2 } } \qquad { \frac { 5 } { 1 6 } } } \qquad 0 \quad 1 } \\ { { \frac { 7 7 5 } { 8 5 6 } } \qquad { - { \frac { 9 9 } { 8 } } } \qquad 1 \quad 0 } \\ { { - { \frac { 4 5 9 } { 9 1 5 9 2 } } \qquad { \frac { 2 9 5 } { 8 5 6 } } \qquad 0 \quad 1 } } \end{array} \right] .
$$

Although $\Phi ( \exp ( z ) , z ) = { \cal O } ( z ^ { 6 } )$ , the order is only 4 because the solution to $\Phi ( w , z ) = 0$ which is ‘principal’ in the sense that it is a good approximation to $\exp ( z )$ , is

$$
w = \frac { 1 + \frac 3 8 z \sqrt { 1 - \frac 1 9 z ^ { 2 } } } { 1 - \frac 5 8 z + \frac 1 8 z ^ { 2 } } = \exp ( z ) - \frac 1 { 2 7 0 } z ^ { 5 } + { \cal O } ( z ^ { 6 } ) .
$$

In Butcher and Chipman (1992), the search for possible $\nu$ corresponding to A-stable methods was focused on the cases $2 \nu _ { 0 } - \widetilde { p } \in \{ 0 , 1 , 2 \}$ . For $k = 1$ (the one-step case), this is necessary and sufficient for A-stability. It seems to be the case that, even for $k > 1$ , those methods for which $2 \nu _ { 0 } - \widetilde { p } > 2$ cannot be A-stable. This proposition has become known as the ‘Butcher–Chipman conjecture’. A partial proof was given in Butcher (2002), restricted to the cases $2 \nu _ { 0 } - \widetilde { p } = 3 , 4 , 7 , 8 , 1 1 , 1 2 , . . .$ , and a complete proof is given in Butcher (2008). An outline of the argument will be given in Subsection 522.
