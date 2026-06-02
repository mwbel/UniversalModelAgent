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
