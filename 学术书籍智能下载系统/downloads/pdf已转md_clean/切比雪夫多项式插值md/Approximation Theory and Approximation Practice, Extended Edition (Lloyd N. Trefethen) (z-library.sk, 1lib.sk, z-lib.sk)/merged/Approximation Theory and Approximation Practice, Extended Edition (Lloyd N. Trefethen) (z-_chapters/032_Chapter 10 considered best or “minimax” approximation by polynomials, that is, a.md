Chapter 10 considered best or “minimax” approximation by polynomials, that is, approximation in the $\infty$ -norm, where optimality is characterized by an equioscillating error curve. This chapter presents analogous results for approximation by rational functions. Much remains the same, but a crucial new feature is the appearance in the equioscillation condition of a number known as the defect, which leads to the phenomenon of square blocks of degenerate entries in the “Walsh table” of best approximations. This complication adds a fascinating new dimension to the theory, but it is a complication with destructive consequences in terms of the fragility of rational approximations and the difficulty of computing them numerically. An antidote to some such difficulties may be the use of algorithms based on linearized least-squares and the singular value decomposition, a theme we shall take up in Chapters 26 and 27.

Another new feature in rational approximation is that we must now be careful to distinguish real and complex situations, because of a curious phenomenon: best rational approximations to real functions are in general complex. This effect is intriguing, but it has little relevance to practical problems, so for the most part we shall restrict our attention to approximations in the space $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ consisting of functions in $\mathcal { R } _ { m n }$ with real coefficients.

We will first state the main theorem, then give some examples, and then present a proof. To begin the discussion, we must define the defect. Suppose $r \in \mathcal { R } _ { m n }$ , that is, $r$ is a rational function of type $( m , n )$ . As discussed in the last chapter, this means that $r$ can be written as a fraction $p / q$ in lowest terms with $p$ and $q$ having exact degrees $\mu \leq m$ and $\nu \leq n$ . The defect $d$ of $r$ in $\mathcal { R } _ { m n }$ is the number between $0$ and $n$ defined by

$$
d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0 .
$$

Note that $d$ is a measure of how far both the numerator and the denominator degrees fall short of their maximum allowed values. Thus $( 1 - x ^ { 2 } ) / ( 1 + x ^ { 2 } )$ , for example, has defect $0$ in $\mathcal { R } _ { 2 2 }$ or $\mathcal { R } _ { 2 3 }$ and defect 1 in $\mathcal { R } _ { 3 3 }$ .

A special case to be noted is the situation in which $r = 0$ , that is, $r$ is identically zero. Recall that in this case we defined $\mu = - \infty$ and $\nu = 0$ , so that $r$ is said to have exact type $( - \infty , 0 )$ . The definition (24.1) remains in force in this case, so if $r = 0$ , we say that $T$ has defect $d = n$ in $\mathcal { R } _ { m n }$ , regardless of $m$ .

The reason why defects matter has to do with the counting of zeros. Suppose $r = p / q \in \mathcal { R } _ { m n }$ has exact type $( \mu , \nu )$ and $\tilde { r } = \tilde { p } / \tilde { q }$ is another function in $\mathcal { R } _ { m n }$ . Then we have

$$
r - \tilde { r } = \frac { p } { q } - \frac { \tilde { p } } { \tilde { q } } = \frac { p \tilde { q } - \tilde { p } q } { q \tilde { q } } ,
$$

a rational function of type $( \operatorname* { m a x } \{ \mu + n , m + \nu \} , n + \nu )$ . By (24.1), this implies that $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus $r - \bar { r }$ can have at most $m + n - d$ zeros, and this zero count is a key to equioscillation and uniqueness results.

Here is our main theorem. The study of rational best approximations goes back to Chebyshev [1859], including the idea of equioscillation, though without a precise statement of what form an alternant must take. Existence was first proved by de la Vall´ee Poussin [1911] and Walsh [1931], and equioscillation is due to Achieser [1930].

Theorem 24.1. Equioscillation characterization of best approximants. $A$ real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and a function $r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ is equal to $r ^ { * }$ if and only if $f - r$ equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

“Equioscillation” here is defined just as in Chapter 10. For $f - r$ to equioscillate between $k$ extreme points means that there exists a set of numbers $- 1 \leq x _ { 1 } < \cdot \cdot \cdot <$ $x _ { k } \le 1$ such that

$$
f ( x _ { j } ) - r ( x _ { j } ) = ( - 1 ) ^ { j + i } \| f - r \| , \qquad 1 \leq j \leq k ,
$$

with $i = 0$ or 1. Here and throughout this chapter, $\| \cdot \|$ is the supremum norm.

We now give some examples. To begin with, here is a function with a spike at $x = 0$ :

Polynomial approximations of this function converge rather slowly. For example, it takes $n = 2 0$ to achieve 1 digit of accuracy:

[p,err] $=$ minimax(f,10); subplot(1,2,1), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,err] $=$ minimax(f,20); subplot(1,2,2), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/71364f9cd98091156bcd840d63950feea6cbb1351b11bd535434152b78f2c657.jpg)

Notice that the extreme points of these error curves are distributed all across $[ - 1 , 1 ]$ , even though the challenging part of the function would appear to be in the middle. As discussed in Chapter 16, this is typical of polynomial best approximations.

If we switch to rational approximations, which can also be computed by the Chebfun minimax command [Filip et al. 2018, Pach´on 2010], the accuracy improves. Here we see error curves for approximations of types $( 2 , 2 )$ and $( 4 , 4 )$ , with much smaller errors despite the degrees being low. Note that most of the extreme points are now localized in the middle.

[p,q,rh,err] $=$ minimax(f,2,2); subplot(1,2,1), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,q,rh,err] $=$ minimax(f,4,4); subplot(1,2,2), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/5a158a7a1c8b82ee4e508ef486ec2dd932c1de7544806d4b9e8c107d16725881.jpg)

The error curves just plotted provide good examples of the role of the defect in the characterization of best approximants. The function $f$ is even, and so are its best approximations (Exercise 24.1). Thus we expect that the type $( 2 , 2 )$ , $( 3 , 2 )$ , $( 2 , 3 )$ , and $( 3 , 3 )$ best approximations will all be the same function, a rational function of exact type $( 2 , 2 )$ whose error curve has 7 points of equioscillation. For $( m , n ) =$ $( 2 , 2 )$ , the defect is $0$ and there is one more equioscillation point than the minimum $m + n + 2 - d = 6$ . For $( m , n ) = ( 3 , 2 )$ or $( 2 , 3 )$ , the defect is $0$ and the number of equioscillation points is exactly the minimum $m + n + 2 - d$ . For $( m , n ) = ( 3 , 3 )$ , the defect is $1$ and the number of equioscillation points is again exactly the minimum $m + n + 2 - d$ .

Similarly, the error curve in the plot on the right, with 11 extrema, indicates that this rational function is a best approximation not only of type $( 4 , 4 )$ but also of types $( 5 , 4 )$ , $( 4 , 5 )$ , and $( 5 , 5 )$ .

Here is another example, an odd function:

f = x.\*exp(-5\*abs(abs(x)-.3)); plot(f)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/dae37f7f8c0bd16c20f22e13a193c5feb32662b17dbeaebd0596fb863e222e99.jpg)

If we look for a best approximation of type $( 4 , 5 )$ , we find that the numerator has exact degree 3,

[p,q,rh,err] $=$ minimax(f,4,5); chebcoeffs(p)'

ans $=$

0.0000 0.0154 0.0000 0.0045 and the denominator has exact degree 4,

chebcoeffs(q)'

ans =

0.1468 0.0000 0.1987 0.0000 0.0574

The defect is 1, so there must be at least $4 + 5 + 2 - 1 = 1 0$ extreme points in the error curve. In fact, there are exactly 10:

plot(f-p/q), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/a4eb78e96c299be0b8944715e676a297b9a8a6e5ca0d38788e5458b962e9bf4c.jpg)

We conclude that $r$ is the best approximation of types $( 4 , 4 ) , ( 4 , 5 ) , ( 3 , 4 )$ , and $( 3 , 5 )$ . Let us now turn to the proof of Theorem 24.1. For polynomial approximations, our analogous theorem was Theorem 10.1, whose proof proceeded in four steps:

1. Existence proof via compactness,   
2. Equioscillation $\Rightarrow$ optimality,

3. Optimality equioscillation,

4. Uniqueness proof via equioscillation.

For rational functions, we shall follow the same sequence. The main novelty is in step 1, where compactness must be applied in a subtler way. We shall see an echo of this argument one more time in Chapter 27, in the proof of Theorem 27.1 for Pad´e approximants.

Part 1 of proof: Existence via compactness. For polynomial approximation, in Chapter 10, we noted that $\| f - p \|$ is a continuous function on $\mathcal { P } _ { n }$ , and since one candidate approximation was the zero polynomial, it was enough to look in the bounded subset $\{ p \in { \mathcal { P } } _ { n } : \| f - p \| \leq \| f \| \}$ . Since this set was compact, the minimum was attained.

For rational functions, $\| f - r \|$ is again a continuous function on $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and again it is enough to look in the bounded subset $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| f - r \| \leq \| f \| \}$ or, more simply, the larger bounded set $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| r \| \leq 2 \| f \| \}$ . The difficulty is that bounded sets of rational functions are not, in general, compact. To illustrate this fact, consider the family of functions

$$
r _ { \varepsilon } ( x ) = { \frac { x ^ { 3 } + \varepsilon } { x ^ { 2 } + \varepsilon } } ,
$$

where $\varepsilon > 0$ is a parameter. For each $\varepsilon$ , $r _ { \varepsilon } ( x )$ is a continuous function on $[ - 1 , 1 ]$ with $\| r _ { \varepsilon } \| = 1$ . As $\varepsilon  0$ , however, $r _ { \varepsilon }$ behaves discontinuously:

$$
\operatorname* { l i m } _ { \varepsilon \to 0 } r _ { \varepsilon } ( x ) = { \left\{ \begin{array} { l l } { 1 , } & { x = 0 , } \\ { x , } & { x \neq 0 . } \end{array} \right. }
$$

So we cannot find a limit function $r _ { 0 }$ by taking a limit as $\varepsilon \  \ 0$ . What saves us, however, is that the spaces of numerators and denominators are both compact, so we can argue that the numerators and denominators separately approach limits and , which in this example would be $x ^ { 3 }$ and $x ^ { 2 }$ . We then define a limiting $p _ { 0 }$ $q _ { 0 }$   
rational function by $r _ { 0 } = p _ { 0 } / q _ { 0 }$ and argue by continuity that it has the necessary properties. This kind of reasoning is spelled out in greater generality in [Walsh 1931].

Suppose then that $\{ r _ { k } \}$ is a sequence of functions in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with $\| r _ { k } \| \le 2 \| f \|$ and

$$
\operatorname* { l i m } _ { k \to \infty } \left\| f - r _ { k } \right\| = E = \operatorname* { i n f } _ { r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } } \left\| f - r \right\| .
$$

Write each $r _ { k }$ in the form $p _ { k } / q _ { k }$ with $p _ { k } \in \mathcal { P } _ { m }$ , $q _ { k } \in \mathcal { P } _ { n }$ , $q _ { k } ( x ) \neq 0$ for all $x \in [ - 1 , 1 ]$ , and $\| q _ { k } \| = 1$ ; hence $\| p _ { k } \| \leq \| q _ { k } \| \| r _ { k } \| \leq 2 \| f \|$ . Since $\left\{ p _ { k } \right\}$ and $\left\{ q _ { k } \right\}$ lie in compact sets, we may assume by passing to a subsequence if necessary that $p _ { k } \to p ^ { * }$ and $q _ { k } \to q ^ { * }$ for some $p ^ { * } \in \mathcal { P } _ { m }$ and $q ^ { * } \in \mathcal { P } _ { n }$ . Since $\| q _ { k } \| = 1$ for each $k$ , $\| q ^ { * } \| = 1$ too, and thus $q ^ { * }$ is not identically zero but has at most a finite set of zeros on $[ - 1 , 1 ]$ . Now define $r ^ { * } = p ^ { * } / q ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . For all $x \in [ - 1 , 1 ]$ except perhaps the zeros of $q ^ { * }$ , $| f ( x ) - r ^ { * } ( x ) | = \operatorname* { l i m } _ { k \to \infty } | f ( x ) - r _ { k } ( x ) | \leq E$ . By continuity, the same must hold for all $x \in [ - 1 , 1 ]$ , with $p ^ { * }$ having zeros in $[ - 1 , 1 ]$ wherever $q ^ { * }$ does. Thus $r ^ { * }$ is a best approximation to $f$ .

Part 2 of proof: Equioscillation $\Rightarrow$ optimality. Suppose $f { - } r$ takes equal extreme values with alternating signs at $m + n + 2 - d$ points $x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { m + n + 1 - d }$ , and suppose $\| f - \tilde { r } \| < \| f - r \|$ for some $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then $r - \bar { r }$ must take nonzero values with alternating signs at the equioscillation points, implying that it must take the value zero in at least $m + n + 1 - d$ points in between. However, as observed above, $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus it cannot have $m + n + 1 - d$ zeros unless it is identically zero, a contradiction.

Part 3 of proof: Optimality equioscillation. Suppose $f - r$ equioscillates at fewer than $m + n + 2 - d$ points, and set $E = \| f - r \|$ . Without loss of generality suppose the leftmost extremum is one where $f - r$ takes the value $- E$ . Then by a compactness argument, for all sufficiently small $\varepsilon > 0$ , there are numbers $- 1 < x _ { 1 } < \dots < x _ { k } < 1$ with $k \leq m + n - d$ such that $( f - r ) ( x ) < E - \varepsilon$ for x $ [ - 1 , x _ { 1 } + \varepsilon ] \cup [ x _ { 2 } - \varepsilon , x _ { 3 } + \varepsilon ] \cup [ x _ { 4 } - \varepsilon , x _ { 5 } + \varepsilon ] \cup$ · · · and $( f - r ) ( x ) > - E + \varepsilon$ for $x \in | x _ { 1 } - \varepsilon , x _ { 2 } + \varepsilon | \cup | x _ { 3 } - \varepsilon , x _ { 4 } + \varepsilon | \cup \cdot \cdot \cdot$ . Let $r$ be written in the form $p / q$ , where $p$ has degree $\mu \leq m - d$ and $q$ has degree $\nu \leq n - d$ , with $p$ and $q$ having no roots in common. The proof now consists of showing that $r$ can be perturbed to a function $\tilde { r } = ( p + \delta p ) / ( q + \delta q ) \in \mathcal { R } _ { m n }$ with the properties that $\| \tilde { r } - r \| < \varepsilon$ and $\bar { r } - r$ is strictly negative for $x \in [ - 1 , x _ { 1 } - \varepsilon ] \cup [ x _ { 2 } + \varepsilon , x _ { 3 } - \varepsilon ] \cup [ x _ { 4 } + \varepsilon , x _ { 5 } - \varepsilon ] \cup \cdot \cdot \cdot$ and strictly positive for $x \in | x _ { 1 } + \varepsilon , x _ { 2 } - \varepsilon | \cup | x _ { 3 } + \varepsilon , x _ { 4 } - \varepsilon | \cup \cdot \cdot \cdot$ . Such a function $\tilde { r }$ will have error less than $E$ throughout the whole interval $\lfloor - 1 , 1 \rfloor$ . We calculate

$$
\tilde { r } = \frac { p + \delta p } { q + \delta q } = \frac { ( p + \delta p ) ( q - \delta q ) } { q ^ { 2 } } + O ( \lVert \delta q \rVert ^ { 2 } )
$$

and therefore

$$
\tilde { r } - r = \frac { q \delta p - p \delta q } { q ^ { 2 } } + O ( \| \delta p \| \| \delta q \| + \| \delta q \| ^ { 2 } ) .
$$

We are done if we can show that $\delta p$ and $\delta \boldsymbol { q }$ can be chosen so that $q \delta p - p \delta q$ is a nonzero polynomial of degree exactly $k$ with roots $x _ { 1 } , \ldots , x _ { k }$ ; by scaling this $\delta p$ and $\delta \boldsymbol { q }$ sufficiently small, the quadratic terms above can be made arbitrarily small relative to the others, so that the required $\varepsilon$ conditions are satisfied. This can be shown by the Fredholm alternative of linear algebra. The map from the $( m + n + 2 )$ - dimensional set of choices of $\delta p$ and $\delta \boldsymbol { q }$ to the $( m + n + 1 - d )$ -dimensional space of polynomials $q \delta p - p \delta q$ is linear. To show the map is surjective, it is enough to show that its kernel has dimension $d + 1$ but no more. Suppose then that $q \delta p - p \delta q$ is zero, that is, $q \delta p = p \delta q$ . Then since $p$ and $q$ have no roots in common, all the roots of $p$ must be roots of $\delta p$ and all the roots of $q$ must be roots of $\delta \boldsymbol { q }$ . In other words we must have $\delta p = g p$ and $\delta q = g q$ for some polynomial $g$ . Since $\delta p$ has degree no greater than $m$ and $\delta \boldsymbol { q }$ has degree no greater than $n$ , $g$ can have degree no greater than $d$ . The set of polynomials of degree $d$ has dimension $d + 1$ , so we are done.

Part 4 of proof: Uniqueness via equioscillation. Finally, to prove uniqueness, suppose $r$ is a best approximation whose error curve equioscillates between extreme points at $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then (without loss of generality) $x _ { 0 } < x _ { 1 } < \dots < x _ { m + n + 1 - d }$ , and suppose $( r - \tilde { r } ) ( x )$ must be $\| f - \tilde { r } \| \leq \| f - r \|$ $\leq 0$ at $x _ { 0 } , x _ { 2 } , x _ { 4 } , \ldots$ for some and $\geq 0$ at $x _ { 1 } , x _ { 3 } , x _ { 5 } , \ldots$ . This implies that $r - \tilde { r }$ has roots in each of the $m + n +$ $1 - d$ closed intervals $[ x _ { 0 } , x _ { 1 } ] , \dotsc , [ x _ { m + n - d } , x _ { m + n + 1 - d } ]$ , and since $r - \tilde { r }$ is a rational function of type $( m + n - d , 2 n - d )$ , the same must hold for its numerator polynomial. We wish to conclude that its numerator polynomial has at least $m + n + 1 - d$ roots in total, counted with multiplicity, implying that $r = \tilde { r }$ . The argument for this is the same as given in the proof of Theorem 10.1.

We have now finished the substantial mathematics. It is time to look at some of the consequences.

One of the recurring themes in the subject of rational approximation is the phenomenon of square blocks in the Walsh table. Suppose that a real function $f \in$ $C ( [ - 1 , 1 ] )$ is given, and consider the set of all of its real rational best approximations of type $( m , n )$ for various $m , n \geq 0$ . We can imagine these laid out in an array, with $m$ along the horizontal and $n$ along the vertical. This array is called the Walsh table for $f$ [Walsh 1934].

Generically, all the entries in the Walsh table for a given $f$ will be distinct, and in this case we say that $f$ is normal. Sometimes, however, certain entries in the table may be repeated, and in fact this is a frequent occurrence because it happens whenever $f$ is even or odd. If $f$ is even, then for any nonnegative integers $j$ and $k$ , all of its rational approximations of types $( 2 j , 2 k )$ , $( 2 j + 1 , 2 k )$ , $( 2 j , 2 k + 1 )$ , and $( 2 j + 1 , 2 k + 1 )$ must be the same. Similarly, if $f$ is odd, then all of its approximations of types $( 2 j + 1 , 2 k )$ , $( 2 j + 2 , 2 k )$ , $( 2 j + 1 , 2 k + 1 )$ , and $( 2 j + 2 , 2 k + 1 )$ must be the same. We have already seen a number of examples.

More generally, repeated entries or “degeneracies” in the Walsh table may take complicated forms. Nevertheless the equioscillation condition imposes quite a bit of structure on the chaos. Degeneracies always appear precisely in a pattern of square blocks. The following statement of this result is taken from [Trefethen 1984], where a discussion of various aspects of this and related problems can be found. We shall return to the subject of square blocks in Chapter 27, on Pad´e approximation.

Theorem 24.2. Square blocks in the Walsh table. The Walsh table of best real rational approximants to a real function $f \in C ( [ - 1 , 1 ] )$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. Given a nonrational function $f$ , let $r \neq 0$ be a best approximation in $\mathcal { R } _ { \mu \nu } ^ { \mathrm { r e a . } }$ l of exact type $( \mu , \nu )$ . (The cases of rational $f$ or $r = 0$ can be handled separately.) By Theorem 24.1, the number of equioscillation points of $f - r$ is $\mu + \nu + 2 + k$ for some integer $k \geq 0$ . We note that $r$ is an approximation to $f$ in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ for any $m \geq \mu$ and $n \geq \nu$ , and the defect is $\operatorname* { m i n } \{ m - \mu , n - \nu \}$ . Thus by Theorem 24.1, $r$ is the best approximation to $f$ precisely for those values of $( m , n )$ satisfying $m \geq \mu$ , $n \geq \nu$ , and $\mu + \nu + 2 + k \geq m + n + 2 - \operatorname* { m i n } \{ m - \mu , n - \nu \}$ . The latter condition simplifies to $n \leq \nu + k$ and $m \leq \mu + k$ , showing that $r$ is the best approximation to $f$ precisely in the square block $\mu \leq m \leq \mu + k$ , $\nu \leq n \leq \nu + k$ .

Within a square block in the Walsh table, the defect $d$ is equal to zero precisely in the first column and the first row. An approximation with $d = 0$ is sometimes said to be nondegenerate. It can have more points of equioscillation than the generic number $m + n + 2$ , but never fewer.

As mentioned above, the theory of equioscillation and degeneracies is very appealing mathematically. As an example we note a result due to Werner [1964], in completion of earlier work of Maehly and Witzgall [1960]: the type $( m , n )$ best approximation operator, which maps functions $f$ to their best approximations $r _ { m n } ^ { * }$ , is continuous at $f$ with respect to the supremum norm if and only if $f \in \mathcal { R } _ { m n }$ or the corresponding function $r _ { m n } ^ { * }$ is nondegenerate. The essential reason for this effect is that if a function $r ^ { * }$ is the best approximation to $f$ in a nontrivial square block, then a small perturbation $f  { \ddot { f } }$ might fracture that block into smaller pieces [Trefethen 1984]. If $( m , n )$ corresponds to a degenerate position in the block, with $d > 0$ , then the best approximation $\tilde { r } ^ { * }$ for such an $\ddot { f }$ might need to have a higher equioscillation number than that of $r ^ { * }$ for $f$ , requiring $\tilde { r } ^ { * }$ to be far from $r ^ { * }$ if $\| f - r ^ { * } \|$ is positive.

These complications hint at some of the practical difficulties of rational approximation. For example, the Remez algorithm is based on explicit manipulation of alternant sets. If the number of extremal points is not known a priori, it is plausible that one may expect numerical difficulties in certain circumstances. Indeed, this is the case, and so far as I am aware, no implementation of the Remez algorithm for rational approximation, including that of Chebfun, can be called fully robust. Other kinds of algorithms may have better prospects.

We finish by returning to the matter of best complex approximations to real functions. Nonuniqueness of certain complex rational approximations was pointed out by Walsh in the 1930s. Later Lungu [1971] noticed, following a suggestion of Gonchar, that the nonuniqueness arises even for approximation of a real function $f$ on $[ - 1 , 1 ]$ , with examples as simple as type $( 1 , 1 )$ approximation of $| x |$ . (Exercise 24.3 gives another proof that there must exist such examples.) These observations were rediscovered independently by Saff and Varga [1978a]. Ruttan [1981] showed that complex best approximations are always better than real ones in the strict lower-right triangle of a square block, that is, when a type $( m , n )$ best approximation equioscillates in no more than $m + n + 1$ points. Trefethen and Gutknecht [1983a] showed that for every $( m , n )$ with $n \geq m + 3$ , examples exist where the ratio of the optimal complex and real errors is arbitrarily small. Levin, Ruttan, and Varga showed that the minimal ratio is exactly $1 / 3$ for $n = m + 2$ and exactly $1 / 2$ for $1 \leq n \leq m + 1$ [Ruttan & Varga 1989]. None of this has much to do with practical approximation, but it is fascinating.

Summary of Chapter 24. Any real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { \ast } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with respect to the $\infty$ -norm, and $r ^ { * }$ is characterized by having an error curve that equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . In the Walsh table of all best approximations to $f$ indexed by $m$ and $n$ , repeated entries, if any, lie in exactly square blocks.

Exercise 24.1. Approximating even functions. Prove that if a real function $f \in$ $C ( [ - 1 , 1 ] )$ is even, then its real best approximations of all types $( m , n )$ are even.

Exercise 24.2. Approximating the Gaussian. The first figures of this chapter considered lower degree polynomial and rational approximations of $\exp ( - 1 0 0 x ^ { 2 } )$ on $[ - 1 , 1 ]$ . Make a plot of the errors in approximations of types $( n , 0 )$ and $( n , n )$ , now taking $n$ as high as you can. (You may find that the cf command takes you farther than minimax.) How do the polynomial and rational approximations compare?

Exercise 24.3. Complex approximations and nonuniqueness. (a) Suppose a real function $f \in C ( [ - 1 , 1 ] )$ takes both the values 1 and $^ { - 1 }$ . Prove that no real rational function $r \in \mathcal { R } _ { 0 n } ^ { \mathrm { r e a l } }$ , for any $n$ , can have $\| f - r \| < 1$ . (b) On the other hand, show that for any $\varepsilon > 0$ , there is a complex rational function $r \in \mathcal { R } _ { 0 n }$ for some $n$ with $\| f - r \| < \varepsilon$ . (Hint: Perturb $f$ by an imaginary constant and consider its reciprocal.) (c) Conclude that type $( 0 , n )$ complex rational best approximations in $C ( [ - 1 , 1 ] )$ are nonunique in general for large enough $_ n$ .

Exercise 24.4. A function with a spike. Plot chebfuns of the function (24.2) for $\varepsilon = 1 , 0 . 1 , \dots , 1 0 ^ { - 6 }$ and determine the polynomial degree $n ( \varepsilon )$ of the chebfun in each case. What is the observed asymptotic behavior of $n ( \varepsilon )$ as $\varepsilon  0$ ? How accurately can you explain this observation based on the theory of Chapter 8?

Exercise 24.5. de la Vall´ee Poussin lower bound. Suppose an approximation $r \in$ $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } < s _ { 1 } < \cdot \cdot \cdot < s _ { m + n + 1 - d } \leq 1$ at which $f - r$ alternates in sign with $| f ( s _ { j } ) - r ( s _ { j } ) | \geq$ $\varepsilon$ for some $\varepsilon > 0$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . Show that the best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ satisfies $\| \boldsymbol { f } - \boldsymbol { r } ^ { * } \| \ge \varepsilon$ . (Compare Exercise 10.3.)

Exercise 24.6. A rational lethargy theorem. Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Adapt the proof of Exercise 10.7 to show that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - r _ { n n } ^ { * } \| \geq \varepsilon { n }$ for all $_ n$ .

Exercise 24.7. Approximation of $e ^ { z }$ . Equation (10.2) gave an asymptotic formula for the accuracy of polynomial best approximations to $e ^ { z }$ on $[ - 1 , 1 ]$ . The generalization to rational best approximations is

$$
E _ { m n } \sim \frac { m ! n ! } { 2 ^ { m + n } ( m + n ) ! ( m + n + 1 ) ! } , \quad m + n \to \infty
$$

(conjectured by Meinardus [1967], proved by Braess [1984]). Produce a table of numerically computed best approximation errors for $0 \leq m + n \leq 1 2$ . How well do these numbers match the asymptotic formula?
