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
