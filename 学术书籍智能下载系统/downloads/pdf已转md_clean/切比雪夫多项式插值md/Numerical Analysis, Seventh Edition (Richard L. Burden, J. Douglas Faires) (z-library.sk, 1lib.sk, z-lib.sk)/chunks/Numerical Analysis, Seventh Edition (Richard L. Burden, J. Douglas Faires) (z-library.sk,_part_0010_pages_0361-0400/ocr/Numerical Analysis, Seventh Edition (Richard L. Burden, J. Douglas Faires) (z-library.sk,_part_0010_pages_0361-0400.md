# Gaussian Elimination with Backward Substitution

To solve the $n \times n$ linear system

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = a _ { 1 , n + 1 } } \\ { E _ { 2 } : } & { { } a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = a _ { 2 , n + 1 } } \\ { \vdots } & { { } \vdots } & { \vdots } & { \vdots } \\ { E _ { n } : } & { { } a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = a _ { n , n + 1 } } \end{array}
$$

INPUT number of unknowns and equations $\pmb { n }$ ; augmented matrix $A = ( a _ { i j } )$ ， where $1 \leq$ $i \leq n$ and $1 \leq j \leq n + 1$

OUTPUT solution $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ or message that the linear system has no unique solution.

Step 1 For $i = 1 , \ldots , n - 1$ do Steps 2-4. (Elimination process.)

Step 2 Let $p$ be the smallest integer with $i \leq p \leq n$ and $a _ { p i } \neq 0$ · If no integer $p$ can be found then OUTPUT(‘no unique solution exists'); STOP.

Step 3If $p \neq i$ then perform $( E _ { p } )  ( E _ { i } )$

Step 4 For $j = i + 1 , \ldots , n$ do Steps 5 and 6.

Step 5Set $m _ { j i } = a _ { j i } / a _ { i i }$ $S t e p \ 6 \mathrm { P e r f o r m } \ ( E _ { j } - m _ { j i } E _ { i } )  ( E _ { j } )$

Step 7 If $a _ { n n } = 0$ then OUTPUT(‘no unique solution exists'); STOP.

Step 8 Set $x _ { n } = a _ { n , n + 1 } / a _ { n n }$ . (Start backward substitution.)

$$
\begin{array} { r } { { S t e p } g \quad \mathrm { F o r } i = n - 1 , \ldots , 1 \mathrm { ~ s e t } x _ { i } = \Bigl [ a _ { i , n + 1 } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } \Bigr ] \Bigg / a _ { i i } . } \end{array}
$$

![](images/b7bbbb01671c3336259434ebf214a7f60313b10123b5a7498de92138a3bdd300.jpg)

Step 10 OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ；  (Procedure completed successfully.) STOP.

All CAS have matrix routines. To define matrices and perform Gaussian elimination using Maple, you must first access the linear algebra library using the command >with(linalg); To define the matrix $\tilde { A } ^ { ( 1 ) }$ of Example 2, which we will call AA,use the command $> \mathtt { A A } : = \mathtt { m a t r i x } ( 4 , 5 , [ 1 , - 1 , 2 , - 1 , - 8 , 2 , - 2 , 3 , - 3 , - 2 0 , 1 , 1 , 1 , 0 , - 2 , 1 , - 1 , 4 , 3 , - 3 , - 4 , 1 , 1 , 1 , 0 , 1 , - 1 , - 1 , 1 , 4 , 3 , - 3 , 1 , - 1 , 0 , 1 , - 1 , 0 , 1 , - 1 , 1 , - 1 , 4 , 3 , 1 , - 1 , 0 , 1 , - 1 , 0 , 1 , - 1 , 1 , - 1 , 1 , 0 , 1 , 0 , 1 , - 1 , - 1 , 1 , - 1 , 1 , - 1 , 4 , 3 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , - 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , - 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,$ 4]）； The first two parameters, 4 and 5, give the number of rows and columns, respectively, and the last parameter is a list of the entries of $\tilde { A } ^ { ( 1 ) } \equiv A A$ . The function addrow(AA,i,j,m)

performs the operation $( E _ { j } + m E _ { i } )  ( E _ { j } )$ and the function swaprow(AA,i,j） prforms the operation $( E _ { i } )  ( E _ { j } )$ . So, the sequence of operations

>AA: $=$ addrow(AA,1,2,-2);   
>AA : $\asymp$ addrow(AA,1,3,-1);   
>AA : addrow(AA,1,4,-1);   
>AA: $\Bumpeq$ swaprow(AA,2,3);   
>AA : addrow(AA,3,4,2);

gives the reduction to $\tilde { A } ^ { ( 4 ) }$ , which is again called AA. Alternatively, the single command AA : gausselim(AA); returns the reduced matrix. In either case, the final operation

>x:=backsub(AA); produces the solution $x : = [ - 7 , 3 , 2 , 2 ]$

# EXAMPlE 4

The purpose of this example is to show what can happen if Algorithm 6.1 fails. The computations wil be done simultaneously on two linear systems:

$$
\begin{array} { r l r } { x _ { 1 } + \ x _ { 2 } + \ x _ { 3 } = 4 , } & { } & { x _ { 1 } + \ x _ { 2 } + \ x _ { 3 } = 4 , } \\ { 2 x _ { 1 } + 2 x _ { 2 } + \ x _ { 3 } = 6 , } & { \mathrm { a n d } } & { 2 x _ { 1 } + 2 x _ { 2 } + \ x _ { 3 } = 4 , } \\ { x _ { 1 } + \ x _ { 2 } + 2 x _ { 3 } = 6 , } & { } & { x _ { 1 } + \ x _ { 2 } + 2 x _ { 3 } = 6 . } \end{array}
$$

These systems produce matrices

$$
\tilde { A } = \left[ \begin{array} { l l l l l } { 1 } & { 1 } & { 1 } & { \vdots } & { 4 } \\ { 2 } & { 2 } & { 1 } & { \vdots } & { 6 } \\ { 1 } & { 1 } & { 2 } & { \vdots } & { 6 } \end{array} \right] \quad \mathrm { a n d } \quad \tilde { A } = \left[ \begin{array} { l l l l l } { 1 } & { 1 } & { 1 } & { \vdots } & { 4 } \\ { 2 } & { 2 } & { 1 } & { \vdots } & { 4 } \\ { 1 } & { 1 } & { 2 } & { \vdots } & { 6 } \end{array} \right] .
$$

Since $a _ { 1 1 } = 1$ , we perform $( E _ { 2 } - 2 E _ { 1 } )  ( E _ { 2 } )$ and $( E _ { 3 } - E _ { 1 } )  ( E _ { 3 } )$ to produce

$$
\tilde { A } = \left[ \begin{array} { c c c c } { 1 } & { 1 } & { 1 } & { \vdots } \\ { 0 } & { 0 } & { - 1 } & { \vdots } \\ { 0 } & { 0 } & { 1 } & { \vdots } \end{array} \right] \quad \mathrm { a n d } \quad \tilde { A } = \left[ \begin{array} { c c c c } { 1 } & { 1 } & { 1 } & { \vdots } \\ { 0 } & { 0 } & { - 1 } & { \vdots } \\ { 0 } & { 0 } & { 1 } & { \vdots } \end{array} \right] .
$$

At this point, ${ a _ { 2 2 } } = { a _ { 3 2 } } = 0$ . The algorithm requires that the procedure be halted, and no solution to either system is obtained. Writing the equations for each system gives

$$
\begin{array} { r l r } { x _ { 1 } + x _ { 2 } + } & { { } x _ { 3 } = } & { 4 , ~ x _ { 1 } + x _ { 2 } + ~ x _ { 3 } = ~ 4 , } \\ { - x _ { 3 } = - 2 , } & { { } \mathrm { a n d } ~ } & { - x _ { 3 } = - 4 , } \\ { x _ { 3 } = } & { { } 2 , ~ x _ { 3 } = } & { 2 . } \end{array}
$$

The first linear system has an infinite number of solutions; $x _ { 3 } = 2 , x _ { 2 } = 2 - x _ { 1 }$ ,and $x _ { 1 }$ arbitrary. The second system leads to the contradiction $x _ { 3 } = 2$ and $x _ { 3 } = 4$ , so no solution exists. In each case, however, there is no unique solution, as we conclude from Algorithm 6.1.

Although Algorithm 6.1 can be viewed as the construction of the augmented matrices $\tilde { A } ^ { ( 1 ) }$ $\check { A } ^ { ( n ) }$ ,thecomputatioscanbeperforedinacomputerusingonlyone $n \times ( n + 1 )$ array for storage. At each step we simply replace the previous value of $a _ { i j }$ by the new one.

In addition,we can store the multipliers $m _ { j i }$ in the locations of $a _ { j i }$ since $a _ { j i }$ has the value O for each $i = 1 , 2 , \ldots , n - 1$ and $j = i + 1 , i + 2 , \dots , n$ .Thus, $A$ can be overwritten by the multipliers below the main diagonal and by the nonzero entries of $\tilde { A } ^ { ( n ) }$ on and above the main diagonal. These values can be used to solve other linear systems involving the original matrix $A$ ,as we will see in Section 6.5.

Both the amount of time required to complete the calculations and the subsequent roundoff error depend on the number of floating-point arithmetic operations needed to solve a routine problem. In general, the amount of time required to perform a multiplication or division on a computer is approximately the same and is considerably greater than that required to perform an addition or subtraction. The actual differences in execution time,however, depend on the particular computing system. To demonstrate the counting operations for a given method, we will count the operations required to solve a typical linear system of n equations in n unknowns using Algorithm 6.1. We will keep the count of the additions/subtractions separate from the count of the multiplications/divisions because of the time differential.

No arithmetic operations are performed until Steps 5 and 6 in the algorithm. Step 5 requires that $( n - i )$ divisions be performed. The replacement of the equation $E _ { j }$ by $( E _ { j } - m _ { j i } E _ { i } )$ in Step 6 requires that $m _ { j i }$ be multiplied by each term in $E _ { i }$ , resulting in a total of $( n - i ) ( n - i + 1 )$ multiplications. After this is completed, each term of the resulting equation is subtracted from the corresponding term in $E _ { j }$ . This requires $( n - i ) ( n - i + 1 )$ subtractions.For each $i = 1 , 2 , \ldots , n - 1$ ,the operations required in Steps 5 and 6 are as follows.

# Multiplications/divisions

$$
( n - i ) + ( n - i ) ( n - i + 1 ) = ( n - i ) ( n - i + 2 ) .
$$

# Additions/subtractions

$$
( n - i ) ( n - i + 1 ) .
$$

The total number of operations required by these steps is obtained by summing the operation counts for each i. Recalling from calculus that

$$
\sum _ { j = 1 } ^ { m } 1 = m , \quad \sum _ { j = 1 } ^ { m } j = \frac { m ( m + 1 ) } { 2 } , \quad \mathrm { a n d } \quad \sum _ { j = 1 } ^ { m } j ^ { 2 } = \frac { m ( m + 1 ) ( 2 m + 1 ) } { 6 } ,
$$

we have the following operation counts.

# Multiplications/divisions

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { n - 1 } ( n - i ) ( n - i + 2 ) = \sum _ { i = 1 } ^ { n - 1 } ( n ^ { 2 } - 2 n i + i ^ { 2 } + 2 n - 2 i ) } \\ { = ( n ^ { 2 } + 2 n ) \sum _ { i = 1 } ^ { n - 1 } 1 - 2 ( n + 1 ) \sum _ { i = 1 } ^ { n - 1 } i + \sum _ { i = 1 } ^ { n - 1 } i ^ { 2 } = \frac { 2 n ^ { 3 } + 3 n ^ { 2 } - 3 n - 4 } { 6 } } \end{array}
$$

# Additions/subtractions

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n - 1 } ( n - i ) ( n - i + 1 ) = \sum _ { i = 1 } ^ { n - 1 } ( n ^ { 2 } - 2 n i + i ^ { 2 } + n - i ) } } \\ { { = ( n ^ { 2 } + n ) \sum _ { i = 1 } ^ { n - 1 } 1 - ( 2 n + 1 ) \sum _ { i = 1 } ^ { n - 1 } i + \sum _ { i = 1 } ^ { n - 1 } i ^ { 2 } = \frac { n ^ { 3 } - n } { 3 } . } } \end{array}
$$

The only other steps in Algorithm 6.1 that involve arithmetic operations are those required for backward substitution, Steps 8 and 9. Step 8 requires one division. Step 9 requires (n -i） multiplications and (n -i - 1) additions for each summation term and then one subtraction and one division. The total number of operations in Steps 8 and 9 is as follows.

# Multiplications/divisions

$$
1 + \sum _ { i = 1 } ^ { n - 1 } ( ( n - i ) + 1 ) = { \frac { n ^ { 2 } + n } { 2 } } .
$$

# Additions/subtractions

$$
\sum _ { i = 1 } ^ { n - 1 } ( ( n - i - 1 ) + 1 ) = { \frac { n ^ { 2 } - n } { 2 } } .
$$

The total number of arithmetic operations in Algorithm 6.1 is, therefore:

# Multiplications/divisions

$$
{ \frac { 2 n ^ { 3 } + 3 n ^ { 2 } - 5 n } { 6 } } + { \frac { n ^ { 2 } + n } { 2 } } = { \frac { n ^ { 3 } } { 3 } } + n ^ { 2 } - { \frac { n } { 3 } } .
$$

# Additions/subtractions

$$
{ \frac { n ^ { 3 } - n } { 3 } } + { \frac { n ^ { 2 } - n } { 2 } } = { \frac { n ^ { 3 } } { 3 } } + { \frac { n ^ { 2 } } { 2 } } - { \frac { 5 n } { 6 } } .
$$

# Table 6.1

For large $\pmb { n }$ , the total number of multiplications and divisions is approximately $n ^ { 3 } / 3$ ， as is the total number of additions and subtractions. Thus,the amount of computation and the time required increases with $n$ in proportion to $n ^ { 3 }$ , as shown in Table 6.1.

<table><tr><td>n</td><td>Multiplications/Divisions</td><td>Additions/Subtractions</td></tr><tr><td>3</td><td>17</td><td>11</td></tr><tr><td>10</td><td>430</td><td>375</td></tr><tr><td>50</td><td>44,150</td><td>42,875</td></tr><tr><td>100</td><td>343,300</td><td>338,250</td></tr></table>

# Exercise set 6.1

1.For each of the following linear systems,obtain a solution by graphical methods, if possible. Explain the results from a geometrical standpoint.

a. $\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } = 3 , } \\ { x _ { 1 } - \ x _ { 2 } = 0 . } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \ } & { { } x _ { 1 } + 2 x _ { 2 } = 0 , } \\ { \mathbf { \qquad } } & { { } x _ { 1 } - \ x _ { 2 } = 0 . } \end{array}$   
c. $\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } = 3 , } \\ { 2 x _ { 1 } + 4 x _ { 2 } = 6 . } \end{array}$ $\begin{array} { r l r } { \mathbf { d } . } & { } & { x _ { 1 } + 2 x _ { 2 } = 3 , } \\ & { } & { - 2 x _ { 1 } - 4 x _ { 2 } = 6 . } \end{array}$   
e. $\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } = 0 , } \\ { 2 x _ { 1 } + 4 x _ { 2 } = 0 . } \end{array}$ f $\begin{array} { r c l } { { 2 x _ { 1 } + } } & { { x _ { 2 } = - 1 , } } \\ { { } } & { { } } & { { x _ { 1 } + } } \\ { { } } & { { } } & { { x _ { 1 } - 3 x _ { 2 } = 5 . } } \end{array}$   
g $\begin{array} { c } { { 2 x _ { 1 } + \ x _ { 2 } = - 1 , } } \\ { { \ } } \\ { { 4 x _ { 1 } + 2 x _ { 2 } = - 2 , } } \\ { { \ x _ { 1 } - 3 x _ { 2 } = 5 . } } \end{array}$ h $\begin{array} { l } { { 2 x _ { 1 } + x _ { 2 } + x _ { 3 } = 1 , } } \\ { { 2 x _ { 1 } + 4 x _ { 2 } - x _ { 3 } = - 1 . } } \end{array}$

2. Use Gaussian elimination with backward substitution and two-digit rounding arithmetic to solve the following linear systems. Do not reorder the equations. (The exact solution to each system is $x _ { 1 } = 1 , x _ { 2 } = - 1 , x _ { 3 } = 3 , y$

$$
\begin{array} { r l } { { 4 } x _ { 1 } - \ x _ { 2 } + \ x _ { 3 } = 8 , } & { \qquad \mathbf { b } _ { \ast } \quad 4 x _ { 1 } + \ x _ { 2 } + 2 x _ { 3 } = 9 , } \\ { 2 x _ { 1 } + 5 x _ { 2 } + 2 x _ { 3 } = 3 , } & { \qquad \quad 2 x _ { 1 } + 4 x _ { 2 } - \ x _ { 3 } = - 5 , } \\ { \ x _ { 1 } + 2 x _ { 2 } + 4 x _ { 3 } = 1 1 . } & { \qquad \ x _ { 1 } + \ x _ { 2 } - 3 x _ { 3 } = - 9 . } \end{array}
$$

3.Use the Gaussian Elimination Algorithm to solve the following linear systems,if possible,and determine whether row interchanges are necessary:

a. $\begin{array} { c } { { x _ { 1 } - \ x _ { 2 } + 3 x _ { 3 } = 2 , } } \\ { { 3 x _ { 1 } - 3 x _ { 2 } + \ x _ { 3 } = - 1 , } } \\ { { x _ { 1 } + \ x _ { 2 } } } \end{array}$ $\begin{array} { r l r } { \mathbf { b } . } & { } & { 2 x _ { 1 } - 1 . 5 x _ { 2 } + 3 x _ { 3 } = 1 , } \\ & { } & { - x _ { 1 } \qquad + 2 x _ { 3 } = 3 , } \\ & { } & { 4 x _ { 1 } - 4 . 5 x _ { 2 } + 5 x _ { 3 } = 1 . } \end{array}$   
c. $\begin{array} { r l r } { 2 x _ { 1 } } & { } & { = 3 , } \\ { x _ { 1 } + 1 . 5 x _ { 2 } } & { = 4 . 5 , } \\ { - } & { 3 x _ { 2 } + 0 . 5 x _ { 3 } } & { = - 6 . 6 , } \\ { 2 x _ { 1 } - } & { 2 x _ { 2 } + } & { x _ { 3 } + x _ { 4 } = 0 . 8 . } \end{array}$ d. $\begin{array} { r l r } & { } & { x _ { 1 } - \frac { 1 } { 2 } x _ { 2 } + x _ { 3 } \qquad = 4 , } \\ & { } & { 2 x _ { 1 } - \ x _ { 2 } - x _ { 3 } + x _ { 4 } = 5 , } \\ & { } & { x _ { 1 } + \ x _ { 2 } \qquad = 2 , } \\ & { } & { x _ { 1 } - \frac { 1 } { 2 } x _ { 2 } + x _ { 3 } + x _ { 4 } = 5 . } \end{array}$   
e. $\begin{array} { r } { \begin{array} { c c } { { \scriptstyle x _ { 1 } + x _ { 2 } \quad \quad + \ x _ { 4 } = 2 , } } \\ { { \scriptstyle 2 x _ { 1 } + x _ { 2 } - \ x _ { 3 } + \ x _ { 4 } = 1 , } } \\ { { \scriptstyle 4 x _ { 1 } - x _ { 2 } - 2 x _ { 3 } + 2 x _ { 4 } = 0 , } } \\ { { \scriptstyle 3 x _ { 1 } - x _ { 2 } - \ x _ { 3 } + 2 x _ { 4 } = - 3 . } } \end{array} \quad \begin{array} { r l } { { \scriptstyle \mathrm { . } } } & { { \scriptstyle x _ { 1 } \quad + \ x _ { 2 } \quad \quad + \ x _ { 4 } = 2 , } } \\ { { \scriptstyle 2 x _ { 1 } \quad + \ x _ { 2 } - \ x _ { 3 } + \ x _ { 4 } = 1 , } } \\ { { \scriptstyle \quad - x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } - \ x _ { 4 } = 4 , } } \\ { { \quad 3 x _ { 1 } - \ x _ { 2 } - \ x _ { 3 } + 2 x _ { 4 } = - 3 . } } \end{array} } \end{array}$

4. Use the Gaussian Elimination Algorithm and single-precision arithmetic on a computer to solve the following linear systems.

a. ${ \begin{array} { r l } & { { \frac { 1 } { 4 } } x _ { 1 } + { \frac { 1 } { 5 } } x _ { 2 } + { \frac { 1 } { 6 } } x _ { 3 } = 9 , } \\ & { { \frac { 1 } { 3 } } x _ { 1 } + { \frac { 1 } { 4 } } x _ { 2 } + { \frac { 1 } { 5 } } x _ { 3 } = 8 , } \\ & { { \frac { 1 } { 2 } } x _ { 1 } + x _ { 2 } + 2 x _ { 3 } = 8 . } \end{array} }$ b. $3 . 3 3 3 x _ { 1 } + \ 1 5 9 2 0 x _ { 2 } - 1 0 . 3 3 3 x _ { 3 } = 1 5 9 1 3$ ，$2 . 2 2 2 x _ { 1 } + ~ 1 6 . 7 1 x _ { 2 } + ~ 9 . 6 1 2 x _ { 3 } = 2 8 . 5 4 4 ,$ $1 . 5 6 1 1 x _ { 1 } + 5 . 1 7 9 1 x _ { 2 } + 1 . 6 8 5 2 x _ { 3 } = 8 . 4 2 5 4$

$$
{ \begin{array} { r } { x _ { 1 } + { \frac { 1 } { 2 } } x _ { 2 } + { \frac { 1 } { 3 } } x _ { 3 } + { \frac { 1 } { 4 } } x _ { 4 } { = { \frac { 1 } { 6 } } } , } \\ { { \frac { 1 } { 2 } } x _ { 1 } + { \frac { 1 } { 3 } } x _ { 2 } + { \frac { 1 } { 4 } } x _ { 3 } + { \frac { 1 } { 5 } } x _ { 4 } { = { \frac { 1 } { 7 } } } , } \\ { { \frac { 1 } { 3 } } x _ { 1 } + { \frac { 1 } { 4 } } x _ { 2 } + { \frac { 1 } { 5 } } x _ { 3 } + { \frac { 1 } { 6 } } x _ { 4 } { = { \frac { 1 } { 8 } } } , } \\ { { \frac { 1 } { 4 } } x _ { 1 } + { \frac { 1 } { 5 } } x _ { 2 } + { \frac { 1 } { 6 } } x _ { 3 } + { \frac { 1 } { 7 } } x _ { 4 } { = { \frac { 1 } { 9 } } } . } \end{array} }
$$

$$
\begin{array} { r l } & { 2 x _ { 1 } + \ x _ { 2 } - \ x _ { 3 } + x _ { 4 } - 3 x _ { 5 } = 7 , } \\ & { \ x _ { 1 } \quad \quad \quad + 2 x _ { 3 } - x _ { 4 } + \ x _ { 5 } = 2 , } \\ & { \quad \quad \quad - 2 x _ { 2 } - \ x _ { 3 } + x _ { 4 } - \ x _ { 5 } = - 5 , } \\ & { 3 x _ { 1 } + \ x _ { 2 } - 4 x _ { 3 } \quad \quad \quad + 5 x _ { 5 } = 6 , } \\ & { \ x _ { 1 } - \ x _ { 2 } - \ x _ { 3 } - x _ { 4 } + \ x _ { 5 } = 3 . } \end{array}
$$

5. Given the linear system

$$
\begin{array} { r } { 2 x _ { 1 } - 6 \alpha x _ { 2 } = 3 , \ } \\ { 3 \alpha x _ { 1 } - \ \qquad x _ { 2 } = \frac { 3 } { 2 } . } \end{array}
$$

a. Find value(s) of $\pmb { \alpha }$ for which the system has no solutions.   
b. Find value(s) of $\pmb { \alpha }$ for which the system has an infinite number of solutions.   
c. Assuming a unique solution exists for a given $\pmb { \alpha }$ , find the solution.

6. Given the linear system

$$
\begin{array} { r } { x _ { 1 } - x _ { 2 } + \alpha x _ { 3 } = - 2 , } \\ { - x _ { 1 } + 2 x _ { 2 } - \alpha x _ { 3 } = 3 , \ } \\ { \alpha x _ { 1 } + \ x _ { 2 } + \ x _ { 3 } = 2 . \qquad } \end{array}
$$

a. Find value(s) of $\pmb { \alpha }$ for which the system has no solutions.   
${ \bf \delta h } .$ Find value(s) of $\pmb { \alpha }$ for which the system has an infinite number of solutions.   
c. Assuming a unique solution exists for a given $\pmb { \alpha }$ , find the solution.

7．Show that the operations

a. $( \lambda E _ { i } ) \to ( E _ { i } )$ $\begin{array} { r } { \mathbf { b } _ { \bullet } \quad ( E _ { i } + \lambda E _ { j } ) \right. ( E _ { i } ) \qquad \mathbf { c . } \quad ( E _ { i } ) \left. ( E _ { j } ) } \end{array}$

do not change the solution set of a linear system.

8. Gauss-Jordan Method: This method is described as follows. Use the ith equation to eliminate not only $x _ { i }$ from the equations $E _ { i + 1 }$ ， $E _ { i + 2 } , \ldots , E _ { n }$ , as was done in the Gaussian elimination method, but also from $E _ { 1 } , E _ { 2 } , \dots , E _ { i - 1 }$ . Upon reducing $[ A , { \bf b } ]$ to:

$$
\left[ \begin{array} { c c c c c c } { a _ { 1 1 } ^ { \left( 1 \right) } } & { 0 } & { \cdots } & { 0 } & { \vdots } & { a _ { 1 , n + 1 } ^ { \left( 1 \right) } } \\ { 0 } & { a _ { 2 2 } ^ { \left( 2 \right) } } & { \ddots } & { \vdots } & { \vdots } & { a _ { 2 , n - 1 } ^ { \left( 2 \right) } } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } & { \vdots } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { a _ { n n } ^ { \left( n \right) } } & { \vdots } & { a _ { n , n + 1 } ^ { \left( n \right) } } \end{array} \right] ,
$$

the solution is obtained by setting

$$
x _ { i } = \frac { a _ { i , n + 1 } ^ { ( i ) } } { a _ { i i } ^ { ( i ) } } ,
$$

for each $i = 1 , 2 , \dots , n$ . This procedure circumvents the backward substitution in the Gaus-sian elimination. Construct an algorithm for the Gauss-Jordan procedure patterned after that of Algorithm 6.1.

9.Use the Gauss-Jordan method and two-digit rounding arithmetic to solve the systems in Exercise 2.

10.Repeat Exercise 4 using the Gauss-Jordan method.

11.a.Show that the Gauss-Jordan method requires

$$
{ \frac { n ^ { 3 } } { 2 } } + n ^ { 2 } - { \frac { n } { 2 } } \quad { \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s } }
$$

and

$$
{ \frac { n ^ { 3 } } { 2 } } - { \frac { n } { 2 } } \quad { \mathrm { a d d i t i o n s / s u b t r a c t i o n s } } .
$$

b. Make a table comparing the required operations for the Gauss-Jordan and Gaussian elimination methods for $n = 3$ , 10, 50,10o.Which method requires less computation ?

12. Consider the following Gaussian-elimination-Gauss-Jordan hybrid method for solving the system (6.4).First, apply the Gaussian-elimination technique to reduce the system to triangular form.Then use the $n$ th equation to eliminate the coefficients of $x _ { n }$ in each of the first $n - 1$ rows.After this is completed use the $( n - 1 ) { \mathsf { s t } }$ equation to eliminate the coefficients of $x _ { n - 1 }$ in the first $n - 2$ rows,etc. The system will eventually appear as the reduced system in Exercise 8.

a. Show that this method requires

$$
{ \frac { n ^ { 3 } } { 3 } } + { \frac { 3 } { 2 } } n ^ { 2 } - { \frac { 5 } { 6 } } n \quad { \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s } }
$$

and

$$
{ \frac { n ^ { 3 } } { 3 } } + { \frac { n ^ { 2 } } { 2 } } - { \frac { 5 } { 6 } } n \quad \mathrm { a d d i t i o n s / s u b t r a c t i o n s } .
$$

b. Make a table comparing the required operations for the Gaussian elimination, Gauss-Jordan,and hybrid methods,for $n = 3$ ,10, 50,100.

13. Use the hybrid method described in Exercise 12 and two-digit rounding arithmetic to solve the systems in Exercise 2.

14.Repeat Exercise 4 using the method described in Exercise 12.

15. Suppose that in a biological system there are $\pmb { n }$ species of animals and m sources of food. Let $x _ { j }$ represent the population of the $j$ th species,for each $j = 1 , \dots , n ; b _ { i }$ represent the available daily supply of the $i$ th food; and $a _ { i j }$ represent the amount of the $i$ th food consumed on the average by a member of the $j$ th species. The linear system

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } \\ { a _ { m 1 } x _ { 1 } + a _ { m 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { m n } x _ { n } = b _ { m } } \end{array}
$$

represents an equilibrium where there is a daily supply of food to precisely meet the average daily consumption of each species.

a. Let

$$
A = ( a _ { i j } ) = \left[ { \begin{array} { r r r r } { 1 } & { 2 } & { 0 } & { 3 } \\ { 1 } & { 0 } & { 2 } & { 2 } \\ { 0 } & { 0 } & { 1 } & { 1 } \end{array} } \right] ,
$$

$\mathbf { x } = ( x _ { j } ) = [ 1 0 0 0 , 5 0 0 , 3 5 0 , 4 0 0 ]$ ,and $\mathbf { b } = ( b _ { i } ) = [ 3 5 0 0 , 2 7 0 0 , 9 0 0 ]$ .Is there sufficient food to satisfy the average daily consumption?

b. What is the maximum number of animals of each species that could be individually added to the system with the supply of food still meeting the consumption?   
c. If species 1 became extinct, how much of an individual increase of each of the remaining species could be supported?   
d. If species 2 became extinct, how much of an individual increase of each of the remaining species could be supported?

16.A Fredholm integral equation of the second kind is an equation of the form

$$
u ( x ) = f ( x ) + \int _ { a } ^ { b } K ( x , t ) u ( t ) d t ,
$$

where $a$ and $b$ and the functions $f$ and $K$ are given. To approximate the function $\boldsymbol { u }$ on the interval $[ a , b ]$ ,a partition $x _ { 0 } = a < x _ { 1 } < \cdot \cdot \cdot < x _ { m - 1 } < x _ { m } = b$ is selected and the equations

$$
u ( x _ { i } ) = f ( x _ { i } ) + \int _ { a } ^ { b } K ( x _ { i } , t ) u ( t ) d t , \quad { \mathrm { f o r } } \operatorname { e a c h } i = 0 , \dots , m ,
$$

are solved for $u ( x _ { 0 } ) , u ( x _ { 1 } ) , \dots , u ( x _ { m } )$ . The integrals are approximated using quadrature formulas based on the nodes $x _ { 0 } , \ldots , x _ { m }$ . In our problem, $a ~ = ~ 0 , ~ b ~ = ~ 1$ ， $f ( x ) ~ = ~ x ^ { 2 }$ ，and $K ( x , t ) = e ^ { | x - t | }$

a. Show that the linear system

$$
\begin{array} { l } { { \displaystyle { u ( 0 ) = f ( 0 ) + \frac { 1 } { 2 } [ K ( 0 , 0 ) u ( 0 ) + K ( 0 , 1 ) u ( 1 ) ] , } } } \\ { { \displaystyle { u ( 1 ) = f ( 1 ) + \frac { 1 } { 2 } [ K ( 1 , 0 ) u ( 0 ) + K ( 1 , 1 ) u ( 1 ) ] } } } \end{array}
$$

must be solved when the Trapezoidal rule is used.

b. Set up and solve the linear system that results when the Composite Trapezoidal rule is used with $n = 4$   
c. Repeat part (b) using the Composite Simpson's rule.

# 6.2 Pivoting Strategies

In deriving Algorithm 6.1,we found that a row interchange is needed when one of the pivot elements $\breve { a } _ { \boldsymbol { k } \boldsymbol { k } } ^ { ( \boldsymbol { k } ) }$ is O. This row interchange has the form $( E _ { k } )  ( E _ { p } )$ , where $p$ is the smallet integergreae han $k$ with $a _ { p k } ^ { ( k ) } \neq 0$ Toue to perform row interchanges even when the pivot elements are not zero.

Ifak ismll i magitudeompore t $a _ { j k } ^ { ( k ) }$ ,the magnitue of themulilier

$$
m _ { j k } = \frac { a _ { j k } ^ { ( k ) } } { a _ { k k } ^ { ( k ) } }
$$

$a _ { k l } ^ { ( k ) }$ $m _ { j k }$ a+)，whichoponstheial

$$
x _ { k } = \frac { a _ { k , n + 1 } ^ { ( k ) } - \sum _ { j = k + 1 } ^ { n } a _ { k j } ^ { ( k ) } } { a _ { k k } ^ { ( k ) } } ,
$$

with a small value f $a _ { k k } ^ { ( k ) }$ , anerror intnumeratocabedamtiallyineasdbcuse of the division by $a _ { k k } ^ { ( k ) }$ . An illustration of this difficulty is given in the following example.

The linear system

$$
\begin{array} { r l r } { E _ { 1 } : } & { 0 . 0 0 3 0 0 0 x _ { 1 } + 5 9 . 1 4 x _ { 2 } = 5 9 . 1 7 } & \\ { E _ { 2 } : } & { 5 . 2 9 1 x _ { 1 } - 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 , } & \end{array}
$$

has the exact solution $x _ { 1 } = 1 0 . 0 0$ and $x _ { 2 } = 1 . 0 0 0$ . Suppose Gaussian elimination is performed on this system using four-digit arithmetic with rounding.

The first pivot element, $a _ { 1 1 } ^ { ( 1 ) } = \bar { 0 } . 0 0 3 0 0 0$ ,is sall,asoa

$$
m _ { 2 1 } = \frac { 5 . 2 9 1 } { 0 . 0 0 3 0 0 0 } = 1 7 6 3 . 6 \overline { { { 6 } } } ,
$$

rounds to the large number 1764. Performing $( E _ { 2 } - m _ { 2 1 } E _ { 1 } )  ( E _ { 2 } )$ and the appropriate rounding gives

$$
\begin{array} { c } { { 0 . 0 0 3 0 0 0 x _ { 1 } + 5 9 . 1 4 x _ { 2 } \approx 5 9 . 1 7 } } \\ { { - 1 0 4 3 0 0 x _ { 2 } \approx - 1 0 4 4 0 0 , } } \end{array}
$$

instead of the precise values,

$$
\begin{array} { c } { 0 . 0 0 3 0 0 0 x _ { 1 } + 5 9 . 1 4 x _ { 2 } = 5 9 . 1 7 } \\ { - 1 0 4 3 0 9 . 3 7 \overline { { 6 } } x _ { 2 } = - 1 0 4 3 0 9 . 3 7 \overline { { 6 } } . } \end{array}
$$

The disparity in the magnitudes of $m _ { 2 1 } a _ { 1 3 }$ and $a _ { 2 3 }$ has introduced roundoff error, but the roundoff error has not yet been propagated. Backward substitution yields

$$
x _ { 2 } \approx 1 . 0 0 1 ,
$$

which is a close approximation to the actual value, $x _ { 2 } = 1 . 0 0 0$ . However, because of the small pivot $a _ { 1 1 } = 0 . 0 0 3 0 0 0 .$ ，

$$
x _ { 1 } \approx \frac { 5 9 . 1 7 - ( 5 9 . 1 4 ) ( 1 . 0 0 1 ) } { 0 . 0 0 3 0 0 0 } = - 1 0 . 0 0
$$

contains the small rror of 0.001 multiplied by

$$
{ \frac { 5 9 . 1 4 } { 0 . 0 0 3 0 0 0 } } \approx 2 0 0 0 0 .
$$

This ruins the approximation to the actual value $x _ { 1 } = 1 0 . 0 0$ . (See Figure 6.1.)

![](images/a6f04916b4ba767c2eaf9d3236cfcd1c59ce9c487a529d7a555f7cbb78066a55.jpg)  
Figure 6.1

Example 1 shows how difficulties arise when the pivot element ak is small relative to the entries $a _ { i j } ^ { ( k ) }$ ,for k ≤i ≤ n and k ≤ j ≤n. To avoid this problem,pivoting is performed by selecting a larger element $a _ { p q } ^ { ( k ) }$ for the pivot and interchanging the $k$ th and $p$ th rows, followed by the interchange of the kth and qth columns,if necessary. The simplest strategy is to select an element in the same column that is below the diagonal and has the largest absolute value; specifically, we determine the smallest $p \geq k$ such that

$$
\{ a _ { p k } ^ { ( k ) } \} = \operatorname* { m a x } _ { k \le i \le n } | a _ { i k } ^ { ( k ) } |
$$

and perform $( E _ { k } )  ( E _ { p } )$ . In this case no interchange of columns is used.

# EXAMPle 2

Reconsider the system

$$
\begin{array} { r l r } { . E _ { 1 } : } & { { } } & { 0 . 0 0 3 0 0 0 x _ { 1 } + 5 9 . 1 4 x _ { 2 } = 5 9 . 1 7 , } \\ { E _ { 2 } : } & { { } } & { 5 . 2 9 1 x _ { 1 } - 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 . } \end{array}
$$

The pivoting procedure just described results in first finding

$$
\operatorname* { m a x } \left\{ | a _ { 1 1 } ^ { ( 1 ) } | , | a _ { 2 1 } ^ { ( 1 ) } | \right\} = \operatorname* { m a x } \left\{ | 0 . 0 0 3 0 0 0 | , | 5 . 2 9 1 | \right\} = | 5 . 2 9 1 | = | a _ { 2 1 } ^ { ( 1 ) } | .
$$

The operation $( E _ { 2 } )  ( E _ { 1 } )$ is then performed to give the system

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } } & { 5 . 2 9 1 x _ { 1 } - 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 , } \\ { E _ { 2 } : } & { { } } & { 0 . 0 0 3 0 0 0 x _ { 1 } + 5 9 . 1 4 x _ { 2 } = 5 9 . 1 7 . } \end{array}
$$

The multiplier for this system is

$$
m _ { 2 1 } = \frac { a _ { 2 1 } ^ { ( 1 ) } } { a _ { 1 1 } ^ { ( 1 ) } } = 0 . 0 0 0 5 6 7 0 ,
$$

and the operation $( E _ { 2 } - m _ { 2 1 } E _ { 1 } )  ( E _ { 2 } )$ reduces the system to

$$
\begin{array} { r l r } & { } & { 5 . 2 9 1 x _ { 1 } - 6 . 1 3 0 x _ { 2 } \approx 4 6 . 7 8 , } \\ & { } & { 5 9 . 1 4 x _ { 2 } \approx 5 9 . 1 4 . } \end{array}
$$

The four-digit answers resulting from the backward substitution are the correct values $x _ { 1 } = 1 0 . 0 0$ and $x _ { 2 } = 1 . 0 0 0$

The technique just described is called partial pivoting, or maximal column pivoting, and is detailed in Algorithm 6.2.The actual row interchanging is simulated in the algorithm by interchanging the values of NROW in Step 5.

# Gaussian Elimination with Partial Pivoting

To solve the $n \times n$ linear system

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = a _ { 1 , n + 1 } } \\ { E _ { 2 } : } & { { } a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = a _ { 2 , n + 1 } } \\ { } & { { } } & { \vdots } \\ { E _ { n } : } & { { } a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = a _ { n , n + 1 } } \end{array}
$$

INPUT number of unknowns and equations $\pmb { n }$ ; augmented matrix $A = ( a _ { i j } )$ where $1 \leq$ $i \leq n$ and $1 \leq j \leq n + 1$

OUTPUTsolution $x _ { 1 } , \ldots , x _ { n }$ or message that the linear system has no unique solution.

Step 1For $i = 1 , \ldots , n$ set $N R O W ( i ) = i$ .(Initialize row pointer.)

Step 2 For $i = 1 , \ldots , n - 1$ do Steps 3-6. (Elimination process.)

Step 3 Let $p$ be the smallest integer with $i \le p \le n$ and $\begin{array} { r l } & { \{ a ( N R O W ( p ) , i ) | = \operatorname* { m a x } _ { i \leq j \leq n } | a ( N R O W ( j ) , i ) | . } \\ & { ( N o t a t i o n ; \ a ( N R O W ( i ) , j ) \equiv a _ { N R O W _ { i } , j } . ) } \end{array}$

Step 4 If $a ( N R O W ( p ) , i ) = 0$ then OUTPUT ( $\bullet _ { \mathbf { n 0 } }$ unique solution exists'); STOP.

Step 5If $\cdot N R O W ( i ) \neq N R O W ( p )$ then set $N C O P Y = N R O W ( i )$ ； $N R O W ( i ) = N R O W ( p )$ ； $N R O W ( p ) = N C O P Y .$ (Simulated row interchange.)

Step 6 For $j = i + 1 , \ldots , n$ do Steps 7 and 8.

$$
\mathfrak { t } m ( N R O W ( j ) , i ) = a ( N R O W ( j ) , i ) / a ( N R O W ( i ) , i ) .
$$

$$
\mathrm { e r f o r m } ~ ( E _ { N R O W ( j ) } - m ( N R O W ( j ) , i ) \cdot E _ { N R O W ( i ) } )  ( E _ { N R O W ( j ) } ) .
$$

Step 9If $a ( N R O W ( n ) , n ) = 0$ then OUTPUT( $\mathbf { \widetilde { n o } }$ unique solution exists'); STOP.

Step 10 Set $x _ { n } = a ( N R O W ( n ) , n + 1 ) / a ( N R O W ( n ) , n ) .$ (Start backward substitution.)

Step11 $\boldsymbol { \Xi } _ { \mathrm { O T } } \ i = n - 1 , \ . \ . \ , \ 1$

$$
\mathsf { s e t } \ x _ { i } = \frac { a ( N R O W ( i ) , n + 1 ) - \sum _ { j = i + 1 } ^ { n } a ( N R O W ( i ) , j ) \cdot x _ { j } } { a ( N R O W ( i ) , i ) } .
$$

Step 12OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ； (Procedure completed successfully.) STOP.

Each multiplier $m _ { j i }$ in the partial pivoting algorithm has magnitude less than or equal to 1.Although this strategy is sufficient for most linear systems, situations do arise when it is inadequate.

# EXAMPLE 3

The linear system

$$
\begin{array} { r l } { E _ { 1 } : } & { 3 0 . 0 0 x _ { 1 } + 5 9 1 4 0 0 x _ { 2 } = 5 9 1 7 0 0 , } \\ { E _ { 2 } : } & { 5 . 2 9 1 x _ { 1 } - \phantom { 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 , } 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 , } \end{array}
$$

is the same as that in Examples 1 and 2 except that all the entries in the first equation have been multiplied by $1 0 ^ { 4 }$ . The procedure described in Algorithm 6.2 with four-digit arithmetic leads to the same results as obtained in Example 1. The maximal value in the first column is 30.0O, and the multiplier

$$
m _ { 2 1 } = \frac { 5 . 2 9 1 } { 3 0 . 0 0 } = 0 . 1 7 6 4
$$

leads to the system

$$
\begin{array} { r l r } & { } & { 3 0 . 0 0 x _ { 1 } + 5 9 1 4 0 0 x _ { 2 } \approx 5 9 1 7 0 0 , } \\ & { } & { - 1 0 4 3 0 0 x _ { 2 } \approx 1 0 4 4 0 0 , } \end{array}
$$

which has the same inaccurate solutions as in Example 1: $x _ { 2 } \approx 1 . 0 0 1$ and $x _ { 1 } \approx - 1 0 . 0 0$

Scaled partial pivoting,also called scaled-column pivoting, is appropriate for the system in Example 3. It places the element in the pivot position that is largest relative to the entries in its row. The first step in this procedure is to define a scale factor $\pmb { S _ { i } }$ for each row as

$$
s _ { i } = \operatorname* { m a x } _ { 1 \leq j \leq n } | a _ { i j } | .
$$

If, for some $i$ ， we have $s _ { i } = 0$ ,then the system has no unique solution since all entries in the ith row are O. Assuming that this is not the case,the appropriate row interchange to

place zeros in the first column is determined by choosing the least integer $p$ with

$$
{ \frac { | a _ { p 1 } | } { s _ { p } } } = \operatorname* { m a x } _ { 1 \leq k \leq n } { \frac { | a _ { k 1 } | } { s _ { k } } }
$$

and performing $( E _ { 1 } )  ( E _ { p } )$ . The effect of scaling is to ensure that the largest element in each row has a relative magnitude of 1 before the comparison for row interchange is performed.

In a similar manner, before eliminating the variable $x _ { i }$ using the operations

$$
E _ { k } - m _ { k i } E _ { i } , \quad { \mathrm { f o r ~ } } k = i + 1 , \dots , n ,
$$

we select the smallest integer $p \geq i$ with

$$
{ \frac { | a _ { p i } | } { s _ { p } } } = \operatorname* { m a x } _ { i \leq k \leq n } { \frac { | a _ { k i } | } { s _ { k } } }
$$

and perform the row interchange $E _ { i }  E _ { p }$ if $i \neq p$ . The scale factors $s _ { 1 } , \ldots , s _ { n }$ are computed only once,at the start of the procedure,and must also be interchanged when row interchanges are performed.

Applying scaled partial pivoting to Example 3 gives

$$
s _ { 1 } = \operatorname* { m a x } \{ | 3 0 . 0 0 | , | 5 9 1 4 0 0 | \} = 5 9 1 4 0 0
$$

and

$$
s _ { 2 } = \operatorname* { m a x } \{ | 5 . 2 9 1 | , | - 6 . 1 3 0 | \} = 6 . 1 3 0 .
$$

Consequently,

$$
\frac { | a _ { 1 1 } | } { s _ { 1 } } = \frac { 3 0 . 0 0 } { 5 9 1 4 0 0 } = 0 . 5 0 7 3 \times 1 0 ^ { - 4 } , \qquad \frac { | a _ { 2 1 } | } { s _ { 2 } } = \frac { 5 . 2 9 1 } { 6 . 1 3 0 } = 0 . 8 6 3 1 ,
$$

and the interchange $( E _ { 1 } )  ( E _ { 2 } )$ is made.

Applying Gaussian elimination to the new system

$$
\begin{array} { c } { 5 . 2 9 1 x _ { 1 } - 6 . 1 3 0 x _ { 2 } = 4 6 . 7 8 } \\ { 3 0 . 0 0 x _ { 1 } + 5 9 1 4 0 0 x _ { 2 } = 5 9 1 7 0 0 } \end{array}
$$

produces the correct results: $x _ { 1 } = 1 0 . 0 0$ and $x _ { 2 } = 1 . 0 0 0$

Algorithm 6.3 implements scaled partial pivoting.

# Gaussian Elimination with Scaled Partial Pivoting

The only steps in this algorithm that differ from those of Algorithm 6.2 are:

Step 1 For $\begin{array} { r } { \dot { \mathbf { \eta } } ^ { } \dot { \mathbf { \eta } } ^ { i } = 1 , \dots , n \det s { \mathbf { e } } { \mathbf { \eta } } s _ { i } = \operatorname* { m a x } _ { 1 \leq j \leq n } | a _ { i j } | ; } \end{array}$ if $s _ { i } = 0$ then OUTPUT ( $\mathbf { \dot { n } 0 }$ unique solution exists'); STOP. $\mathsf { s e t } N R O W ( i ) = i$

Step 2 For $i = 1 , \ldots , n - 1$ do Steps 3-6. (Elimination process.)

Step 3 Let $p$ be the smallest integer with $i \le p \le n$ and

$$
\frac { | a ( N R O W ( p ) , i ) | } { s ( N R O W ( p ) ) } = \operatorname* { m a x } _ { i \leq j \leq n } \frac { | a ( N R O W ( j ) , i ) | } { s ( N R O W ( j ) ) } .
$$

The next example ilustrates scaled partial pivoting using Maple with finite-digit rounding arithmetic.

# EXAMPLE 4

Solve the linear system using three-digit rounding arithmetic.

$$
\begin{array} { r l r } & { 2 . 1 1 x _ { 1 } - } & { 4 . 2 1 x _ { 2 } + 0 . 9 2 1 x _ { 3 } = ~ 2 . 0 1 , } \\ & { 4 . 0 1 x _ { 1 } + } & { 1 0 . 2 x _ { 2 } - ~ 1 . 1 2 x _ { 3 } = - 3 . 0 9 , } \\ & { 1 . 0 9 x _ { 1 } + 0 . 9 8 7 x _ { 2 } + 0 . 8 3 2 x _ { 3 } = ~ 4 . 2 1 . } \end{array}
$$

To obtain three-digit rounding arithmetic, enter

>Digits: $= 3$ ；

We have $s _ { 1 } = 4 . 2 1$ ， $s _ { 2 } = 1 0 . 2$ ,and $s _ { 3 } = 1 . 0 9$

So

$$
\frac { | a _ { 1 1 } | } { s _ { 1 } } = \frac { 2 . 1 1 } { 4 . 2 1 } = 0 . 5 0 1 , \quad \frac { | a _ { 2 1 } | } { s _ { 1 } } = \frac { 4 . 0 1 } { 1 0 . 2 } = 0 . 3 9 3 , \quad \mathrm { a n d } \quad \frac { | a _ { 3 1 } | } { s _ { 3 } } = \frac { 1 . 0 9 } { 1 . 0 9 } = 1 .
$$

The augmented matrix AA is defined by

>AA:=matrix(3,4,[2.11,-4.21,0.921,2.01,4.01,10.2,-1.12,-3.09,1.09, 0.987,0.832,4.21]);

which gives

$$
A A : = \left[ { \begin{array} { c c c c } { 2 . 1 1 } & { - 4 . 2 1 } & { . 9 2 1 } & { 2 . 0 1 } \\ { 4 . 0 1 } & { 1 0 . 2 } & { - 1 . 1 2 } & { - 3 . 0 9 } \\ { 1 . 0 9 } & { . 9 8 7 } & { . 8 3 2 } & { 4 . 2 1 } \end{array} } \right] .
$$

Since $\lvert a _ { 3 1 } \rvert / s _ { 3 }$ is largest, we perform $( E _ { 1 } )  ( E _ { 3 } )$ using

>AA : swaprow(AA,1,3);

to obtain

$$
A A : = \left[ { \begin{array} { r r r r } { 1 . 0 9 } & { . 9 8 7 } & { . 8 3 2 } & { 4 . 2 1 } \\ { 4 . 0 1 } & { 1 0 . 2 } & { - 1 . 1 2 } & { - 3 . 0 9 } \\ { 2 . 1 1 } & { - 4 . 2 1 } & { . 9 2 1 } & { 2 . 0 1 } \end{array} } \right] .
$$

Computing multipliers gives

>m21: $\pm 4$ .01/1.09;

$$
m 2 1 : = 3 . 6 8
$$

>m31 : $\approx 2$ .11/1.09;

$$
m 3 1 : = 1 . 9 4
$$

We perform the frst two eliminations using

>AA: $\simeq$ addrow(AA,1,2,-m21);

and

>AA : $=$ addrow(AA,1,3,-m31) ;

to obtain

$$
A A : = \left[ \begin{array} { l r r r r } { 1 . 0 9 } & { { 9 8 7 } } & { . 8 3 2 } & { 4 . 2 1 } \\ { 0 } & { { 6 . 5 7 } } & { { - 4 . 1 8 } } & { { - 1 8 . 6 } } \\ { 0 } & { { - 6 . 1 2 } } & { { - . 6 8 9 } } & { { - 6 . 1 6 } } \end{array} \right] .
$$

Since

$$
\frac { | a _ { 2 2 } | } { s _ { 2 } } = \frac { 6 . 5 7 } { 1 0 . 2 } = 0 . 6 4 4 < \frac { | a _ { 3 2 } | } { s _ { 3 } } = \frac { 6 . 1 2 } { 4 . 2 1 } = 1 . 4 5 ,
$$

we perform

>AA : $\fallingdotseq$ swaprow(AA,2,3);

giving

$$
A A : = \left[ \begin{array} { l l l l } { 1 . 0 9 } & { \quad . 9 8 7 } & { \quad . 8 3 2 } & { \quad 4 . 2 1 } \\ { 0 } & { - 6 . 1 2 } & { \quad - . 6 8 9 } & { \quad - 6 . 1 6 } \\ { 0 } & { \quad 6 . 5 7 } & { - 4 . 1 8 } & { - 1 8 . 6 } \end{array} \right] .
$$

The multiplier $m _ { 3 2 }$ is computed by

$> \mathrm { m } 3 2 : = 6 . 5 7 / \left( - 6 . 1 2 \right) ;$

$$
m _ { 3 2 } : = - 1 . 0 7 .
$$

The elimination step

>AA : $\ncong$ addrow(AA,2,3,-m32);

gives

$$
A A : = \left[ \begin{array} { l l l l l } { 1 . 0 9 } & { { . 9 8 7 } } & { { . 8 3 2 } } & { { 4 . 2 1 } } \\ { 0 } & { { - 6 . 1 2 } } & { { - . 6 8 9 } } & { { - 6 . 1 6 } } \\ { 0 } & { { . 0 2 } } & { { - 4 . 9 2 } } & { { - 2 5 . 2 } } \end{array} \right] .
$$

We cannot use backsub because of the entry .02 in the (3,2) position. This entry is nonzero due to rounding, but we can remedy this minor problem using the command

$> \tt A A [ 3 , 2 ] : = 0 ;$

which replaces the entry .02 with a 0. To see this enter

>evalm(AA);

which displays the matrix AA. Finally,

>x:=backsub(AA);

gives the solution

$$
x : = \left[ { \begin{array} { r r r } { - . 4 3 1 } & { . 4 3 0 } & { 5 . 1 2 } \end{array} } \right] .
$$

The first additional computations required for scaled partial pivoting result from the determination of the scale factors; there are $( n - 1 )$ comparisons for each of the $\pmb { n }$ rows, for a total of

To determine the correct first interchange, $\pmb { n }$ divisions are performed,followed by $n - 1$ comparisons. So the first interchange determination adds

Since the scaling factors are computed only once, the second step requires

We proceed in a similar manner until there are zeros below the main diagonal in all but the $\pmb { n }$ th row. The final step requires that we perform

As a consequence, scaled partial pivoting adds a total of

$$
n ( n - 1 ) + \sum _ { k = 1 } ^ { n - 1 } k = n ( n - 1 ) + { \frac { ( n - 1 ) n } { 2 } } = { \frac { 3 } { 2 } } n ( n - 1 ) \quad { \mathrm { c o m p a r i s o r } }
$$

and

$$
\sum _ { k = 2 } ^ { n } k = \sum _ { k = 1 } ^ { n } k - 1 = { \frac { n ( n + 1 ) } { 2 } } - 1 \quad { \mathrm { d i v i s i o n s } }
$$

to the Gaussan elimination procedure.The time required to perform a comparison is about the same as an addition/subtraction. Since the total time to perform the basic Gaussian elimination procedure is $O ( n ^ { 3 } / 3 )$ multiplications/divisions and $O ( n ^ { 3 } / 3 )$ additions/subtractions, scaled partial pivoting does not add significantly to the computational time required to solve a system for large values of $\pmb { n }$ ·

To emphasize the importance of choosing the scale factors only once, consider the amount of additional computation that would be required if the procedure were modified so that new scale factors were determined each time a row interchange decision was to be made. In this case,the term $n ( n - 1 )$ in Eq. (6.7) would be replaced by

$$
\sum _ { k = 2 } ^ { n } k ( k - 1 ) = { \frac { 1 } { 3 } } n ( n ^ { 2 } - 1 ) .
$$

As a consequence, this pivoting technique would add $O ( n ^ { 3 } / 3 )$ comparisons,in addition to the $\left\{ n ( n + 1 ) / 2 \right\} - 1$ divisions. If a system warrants this type of pivoting, complete (or maximal) pivoting should instead be used. Complete pivoting at the $k$ th step searches all the entries $a _ { i j }$ ,for $i = k , k + 1 , \ldots , n$ and $j = k , k + 1 , \ldots , n$ ,to find the entry with the largest magnitude. Both row and column interchanges are performed to bring this entry to the pivot position. The first step of total pivoting requires that $n ^ { 2 } - 1$ comparisons be performed, the second step requires $( n - 1 ) ^ { 2 } - 1$ comparisons,and so on. Hence the total additional time required to incorporate complete pivoting into Gaussian elimination is

$$
\sum _ { k = 2 } ^ { n } ( k ^ { 2 } - 1 ) = { \frac { n ( n - 1 ) ( 2 n + 5 ) } { 6 } }
$$

comparisons. This figure is comparable to the number required for the modified scaledcolumn pivoting technique, but no divisions are required. Complete pivoting is,consequently,the strategy recommended for systems where accuracy is essential and the amount of execution time needed for this method can be justified.

1.Find the row interchanges that are required to solve the folowing linear systems using Algorithm 6.1.

$$
\begin{array} { r l r } { \mathbf { a } . \quad } & { x _ { 1 } - 5 x _ { 2 } + } & { x _ { 3 } = 7 , } \\ & { } & { \mathrm { ~ } \mathrm { ~ } 1 0 x _ { 1 } \qquad + 2 0 x _ { 3 } = 6 , } & { x _ { 1 } + x _ { 2 } + 4 x _ { 3 } = 2 , } \\ & { } & { 5 x _ { 1 } \qquad - \quad x _ { 3 } = 4 . } \\ & { } & { \mathrm { ~ } 2 x _ { 1 } - x _ { 2 } + 2 x _ { 3 } = 3 . } \\ & { \mathbf { c } . \quad } & { 2 x _ { 1 } - 3 x _ { 2 } + 2 x _ { 3 } = 5 , } & { \mathbf { d } . } \\ & { } & { - 4 x _ { 1 } + 2 x _ { 2 } - 6 x _ { 3 } = 1 4 , } & { x _ { 1 } - 2 x _ { 2 } - x _ { 3 } = 4 , } \\ & { } & { 2 x _ { 1 } + 2 x _ { 2 } + 4 x _ { 3 } = 8 . } \end{array}
$$

2. Repeat Exercise 1 using Algorithm 6.2.

3. Repeat Exercise 1 using Algorithm 6.3.

4. Repeat Exercise 1 using complete pivoting.

5. Use Gaussian eliminiation and three-digit chopping arithmetic to solve the following linear systems, and compare the approximations to the actual solution.

a. $0 . 0 3 x _ { 1 } + 5 8 . 9 x _ { 2 } = 5 9 . 2 ,$ $5 . 3 1 x _ { 1 } - 6 . 1 0 x _ { 2 } = 4 7 . 0 $ Actual solution $( 1 0 , 1 ) ^ { t }$

$\begin{array} { r } { \ b _ { \bullet } \qquad 5 8 . 9 x _ { 1 } + 0 . 0 3 x _ { 2 } = 5 9 . 2 , } \end{array}$ $- 6 . 1 0 x _ { 1 } + 5 . 3 1 x _ { 2 } = 4 7 . 0 .$ Actual solution (1, 10)'.

c. $3 . 0 3 x _ { 1 } - 1 2 . 1 x _ { 2 } + 1 4 x _ { 3 } = - 1 1 9 ,$ $- 3 . 0 3 x _ { 1 } + 1 2 . 1 x _ { 2 } - 7 x _ { 3 } = 1 2 0 ,$ $6 . 1 1 x _ { 1 } - 1 4 . 2 x _ { 2 } + 2 1 x _ { 3 } = - 1 3 9 .$ Actual solution $( 0 , 1 0 , \frac { 1 } { 7 } ) ^ { t }$ ·

d. $3 . 3 3 3 0 x _ { 1 } + 1 5 9 2 0 x _ { 2 } + 1 0 . 3 3 3 x _ { 3 } = 7 9 5 3 ,$ $2 . 2 2 2 0 x _ { 1 } + 1 6 . 7 1 0 x _ { 2 } + 9 . 6 1 2 0 x _ { 3 } = 0 . 9 6 5$ ， $- 1 . 5 6 1 1 x _ { 1 } + 5 . 1 7 9 2 x _ { 2 } - 1 . 6 8 5 5 x _ { 3 } = 2 . 7 1 4$ Actual solution $( 1 , 0 . 5 , - 1 ) ^ { t }$

e. $1 . 1 9 x _ { 1 } + ~ 2 . 1 1 x _ { 2 } - ~ 1 0 0 x _ { 3 } + x _ { 4 } = 1 . 1 2 ,$ $1 4 . 2 x _ { 1 } - 0 . 1 2 2 x _ { 2 } + 1 2 . 2 x _ { 3 } - x _ { 4 } = 3 . 4 4 ,$ $1 0 0 x _ { 2 } - 9 9 . 9 x _ { 3 } + x _ { 4 } = 2 . 1 5$ ， $1 5 . 3 x _ { 1 } + 0 . 1 1 0 x _ { 2 } - 1 3 . 1 x _ { 3 } - x _ { 4 } = 4 . 1 6 .$ Actual solution (0.17682530,0.01269269,-0.02065405,-1.18260870)t .

f. $\begin{array} { r l } & { ~ \pi x _ { 1 } - ~ e x _ { 2 } + \sqrt { 2 } x _ { 3 } - \sqrt { 3 } x _ { 4 } = \sqrt { 1 1 } , } \\ & { ~ \pi ^ { 2 } x _ { 1 } + ~ e x _ { 2 } - ~ e ^ { 2 } x _ { 3 } + ~ \frac { 3 } { 7 } x _ { 4 } = 0 , } \\ & { \sqrt { 5 } x _ { 1 } - \sqrt { 6 } x _ { 2 } + ~ x _ { 3 } - \sqrt { 2 } x _ { 4 } = \pi , } \\ & { ~ \pi ^ { 3 } x _ { 1 } + ~ e ^ { 2 } x _ { 2 } - \sqrt { 7 } x _ { 3 } + ~ \frac { 1 } { 9 } x _ { 4 } = \sqrt { 2 } . } \end{array}$   
Actual solution (0.78839378,-3.12541367, 0.16759660,4.55700252).

6. Repeat Exercise 5 using three-digit rounding arithmetic.   
7. Repeat Exercise 5 using Gaussian elimination with partial pivoting.   
8. Repeat Exercise 6 using Gaussian elimination with partial pivoting.   
9. Repeat Exercise 5 using Gaussian elimination with scaled partial pivoting.   
10. Repeat Exercise 6 using Gaussian elimination with scaled partial pivoting.   
11. Repeat Exercise 5 using Algorithm 6.1 with single-precision computer arithmetic.   
12. Repeat Exercise 5 using Algorithm 6.2 with single-precision computer arithmetic.   
13. Repeat Exercise 5 using Algorithm 6.3 with single-precision computer arithmetic.   
14. Construct an algorithm for the complete pivoting procedure discussed in the text.   
15. Use the complete pivoting algorithm developed in Exercise 14 to obtain solutions to

a.Exercise 5 b.Exercise 6 c.Exercise 11

16.Suppose that

$$
\begin{array} { r l r } & { } & { 2 x _ { 1 } + x _ { 2 } + 3 x _ { 3 } = 1 , } \\ & { } & \\ & { } & { 6 x _ { 1 } + 6 x _ { 2 } + 8 x _ { 3 } = 5 , } \\ & { } & \\ & { } & { 6 x _ { 1 } + \alpha x _ { 2 } + 1 0 x _ { 3 } = 5 , } \end{array}
$$

with $| { \pmb { \alpha } } | < 1 0$ . For which of the following values of $\pmb { \alpha }$ will there be no row interchange required when solving this system using scaled partial pivoting?

a. $\alpha = 6$ $\begin{array} { c c c c } { \mathbf { b } , } & { \alpha = 9 } & { } & { } & { \mathbf { c } . } & { \alpha = - 3 } \end{array}$

# 6.3 Linear Algebra and Matrix Inversion

Matrices were introduced in Section 6.1 as a convenient method for expresing and manipulating linear systems. In this section we consider some algebra associated with matrices and show how it can be used to solve problems involving linear systems.

# Definition 6.2

Two matrices $A$ and $B$ are equal if they have the same number of rows and columns,say $n \times m$ , and if $a _ { i j } = b _ { i j }$ , for each $i = 1 , 2 , \dots , n$ and $j = 1 , 2 , \dots , m$

This definition means, for example, that

$$
\left[ { \begin{array} { r r } { 2 } & { - 1 } \\ { 3 } & { 1 } & { 0 } \end{array} } \right] \neq \left[ { \begin{array} { r r } { 2 } & { 3 } \\ { - 1 } & { 1 } \\ { 7 } & { 0 } \end{array} } \right] ,
$$

since they differ in dimension.

Two important operations performed on matrices are the sum of two matrices and the multiplication of a matrix by a real number.

# Definition 6.3

If $A$ and $B$ are both $n \times m$ matrices, then the sum of $A$ and $B$ , denoted $A + B$ , is the $n \times m$ matrix whose entries are $a _ { i j } + b _ { i j }$ , for each $i = 1 , 2 , \dots , n$ and $j = 1 , 2 , \dots , m .$

Definition 6.4

$\pmb { A }$ is an $n \times m$ matrix and $\lambda$ is a real number, then the scalar multiplication of $\lambda$ and $\pmb { A }$ , denoted $\lambda A$ ,is the $n \times m$ matrix whose entries are $\lambda a _ { i j }$ , for each $i = 1 , 2 , \dots , n$ and $j = 1 , 2 , \dots , m$

EXAMPLE 1 Let

$$
A = { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 7 } \\ { 3 } & { 1 } & { 0 } \end{array} \right] } , \quad B = { \left[ \begin{array} { l l l } { 4 } & { 2 } & { - 8 } \\ { 0 } & { 1 } & { 6 } \end{array} \right] }
$$

and $\lambda = - 2$ . Then

$$
A + B = { \left[ \begin{array} { l l l } { 2 + 4 } & { - 1 + 2 } & { 7 - 8 } \\ { 3 + 0 } & { 1 + 1 } & { 0 + 6 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 6 } & { 1 } & { - 1 } \\ { 3 } & { 2 } & { 6 } \end{array} \right] } ,
$$

and

$$
\lambda A = { \left[ \begin{array} { l l l } { - 2 ( 2 ) } & { - 2 ( - 1 ) } & { - 2 ( 7 ) } \\ { - 2 ( 3 ) } & { - 2 ( 1 ) } & { - 2 ( 0 ) } \end{array} \right] } = { \left[ \begin{array} { l l l } { - 4 } & { 2 } & { - 1 4 } \\ { - 6 } & { - 2 } & { 0 } \end{array} \right] } .
$$

Let $o$ denote a matrix all of whose entries are O and $- \pmb { A }$ be the matrix whose entries are $- a _ { i j }$ . We have the following general properties for matrix addition and scalar multiplication. These properties are sufficient to classify the set of all $n \times m$ matrices with real entries as a vector space over the field of real numbers. (See [ND, pp. 1O7-109].)

# Theorem 6.5

Let $A , B$ , and $C$ be $n \times m$ matrices and $\lambda$ and $\mu$ be real numbers. The following properties of addition and scalar multiplication hold:

$$
\begin{array} { r l r l } & { A + B = B + A , } & { \qquad } & { \mathbf { b } _ { * } } & { ( A + B ) + C = A + ( B + C ) , } \\ & { A + O = O + A ^ { \prime } = A , } & { \qquad } & { \mathbf { d } , } & { A + ( - A ) = - A + A = 0 , } \\ & { \lambda ( A + B ) = \lambda A + \lambda B , } & { \qquad } & { \mathbf { f } , } & { ( \lambda + \mu ) A = \lambda A + \mu A , } \\ & { \lambda ( \mu A ) = ( \lambda \mu ) A , } & { \qquad } & { \mathbf { h } _ { * } } & { 1 A = A . } \end{array}
$$

All these properties follow from similar results concerning the real numbers.

# Definition 6.6

Let $A$ be an $n \times m$ matrix and $B$ an $m \times p$ matrix. The matrix product of $A$ and $B$ ,denoted $A B$ , is an $n \times p$ matrix $C$ whose entries $c _ { i j }$ are

$$
c _ { i j } = \sum _ { k = 1 } ^ { m } a _ { i k } b _ { k j } = a _ { i 1 } b _ { 1 j } + a _ { i 2 } b _ { 2 j } + \cdot \cdot \cdot + a _ { i m } b _ { m j } ,
$$

for each $i = 1 , 2 , \ldots n$ ,and $j = 1 , 2 , . . . , p$

The computation of $c _ { i j }$ can be viewed as the multiplicationof the entries of the ith row of $A$ with corresponding entries in the $j$ th column of $B$ ,followed by asummation;that is,

$$
{ \{ a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i m } \} } \left[ \begin{array} { c } { { b _ { 1 j } } } \\ { { b _ { 2 j } } } \\ { { \vdots } } \\ { { b _ { m j } } } \end{array} \right] = c _ { i j } ,
$$

where

$$
c _ { i j } = a _ { i 1 } b _ { 1 j } + a _ { i 2 } b _ { 2 j } + \cdot \cdot \cdot + a _ { i m } b _ { m j } = \sum _ { k = 1 } ^ { m } a _ { i k } b _ { k j } .
$$

This explains why the number of columns of $\pmb { A }$ must equal the number of rows of $B$ for the product $A B$ to be defined.

The following example should serve to further clarify the matrix multiplication process.

EXAMPLE 2 Let

$$
A = \left[ { \begin{array} { r r r } { 2 } & { 1 } & { - 1 } \\ { 3 } & { 1 } & { 2 } \\ { 0 } & { - 2 } & { - 3 } \end{array} } \right] , \quad B = \left[ { \begin{array} { r r } { 3 } & { 2 } \\ { - 1 } & { 1 } \\ { 6 } & { 4 } \end{array} } \right] ,
$$

$$
C = \left[ { \begin{array} { r r r } { 2 } & { 1 } & { 0 } \\ { - 1 } & { 3 } & { 2 } \end{array} } \right] , \quad { \mathrm { a n d } } \quad D = \left[ { \begin{array} { r r r } { 1 } & { - 1 } & { 1 } \\ { 2 } & { - 1 } & { 2 } \\ { 3 } & { 0 } & { 3 } \end{array} } \right] .
$$

Then,

$$
A D = \left[ { \begin{array} { r r r } { 1 } & { - 3 } & { 1 } \\ { 1 1 } & { - 4 } & { 1 1 } \\ { - 1 3 } & { 2 } & { - 1 3 } \end{array} } \right] \neq \left[ { \begin{array} { r r r } { - 1 } & { - 2 } & { - 6 } \\ { 1 } & { - 3 } & { - 1 0 } \\ { 6 } & { - 3 } & { - 1 2 } \end{array} } \right] = D A .
$$

Further,

$$
B C = { \left[ \begin{array} { l l l } { 4 } & { 9 } & { 4 } \\ { - 3 } & { 2 } & { 2 } \\ { 8 } & { 1 8 } & { 8 } \end{array} \right] } \quad { \mathrm { a n d } } \quad C B = { \left[ \begin{array} { l l } { 5 } & { 5 } \\ { 6 } & { 9 } \end{array} \right] }
$$

are not even the same size.

Finally,

$$
A B = \left[ { \begin{array} { r r } { - 1 } & { 1 } \\ { 2 0 } & { 1 5 } \\ { - 1 6 } & { - 1 4 } \end{array} } \right] ,
$$

but $B A$ cannot be computed.

# Definition 6.7

A square matrix has the same number of rows as columns. A diagonal matrix is a square matrix $D = ( d _ { i j } )$ with $d _ { i j } = 0$ whenever $i \neq j$ . The identity matrix of order $\pmb { n }$ $, I _ { n } = ( \delta _ { i j } )$ ， is a diagonal matrix with entries

$$
\delta _ { i j } = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } i = j , } \\ { 0 , } & { { \mathrm { i f ~ } } i \neq j . } \end{array} \right. }
$$

When the size of $I _ { n }$ is clear, this matrix is generally written simply as $I$

For example, the identity matrix of order three is

$$
I = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right] .
$$

# Definition 6.8

An upper-triangular $n \times n$ matrix $U = ( u _ { i j } )$ has, for each $j = 1 , 2 , \dots , n$ ,the entries

$$
u _ { i j } = 0 , \quad \mathrm { f o r e a c h } i = j + 1 , j + 2 , \ldots , n ;
$$

and a lower-triangular matrix $L = ( l _ { i j } )$ has,for each $j = 1 , 2 , \dots , n$ , the entries

$$
l _ { i j } = 0 , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , j - 1 .
$$

# EXAMPLE 3

Consider the identity matrix of order three,

$$
I _ { 3 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } ~ .
$$

If $A$ is any $3 \times 3$ matrix,then

$$
A I _ { 3 } = { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } = A .
$$

The identity matrix $I _ { n }$ commutes with any $n \times n$ matrix $A$ ; that is,the order of multiplication does not matter, $I _ { n } A = A = A I _ { n }$ . In Example 2 it was seen that the property $A B = B A$ is not generally true for matrix multiplication. Some of the properties involving matrix multiplication that do hold are presented in the next theorem.

# Theorem 6.9

Let $A$ be an $n \times m$ matrix, $B$ be an $m \times k$ matrix, $C$ be a $k \times p$ matrix, $D$ be an $m \times k$ matrix, and $\lambda$ be a real number. The following properties hold:

a. $A ( B C ) = ( A B ) C ;$ $\begin{array} { r l } { \mathbf { b } . \ } & { { } A ( B + D ) = A B + A D ; } \\ { \mathbf { d } . \ } & { { } \lambda ( A B ) = ( \lambda A ) B = A ( \lambda B ) . } \end{array}$   
c. $I _ { m } B = B$ and $B I _ { k } = B$ ；

Proof The verification of the property in part (a) is presented to show the method involved.The other parts can be shown in a similar manner.

To show that $A ( B C ) = ( A B ) C$ , compute the i, $j$ -entry of each side of the equation. $B C$ is an $m \times p$ matrix with $i$ ， $j$ -entry

$$
( B C ) _ { i j } = \sum _ { l = 1 } ^ { k } b _ { i l } c _ { l j } .
$$

Thus, $A ( B C )$ is an $n \times p$ matrix with entries

$$
[ A ( B C ) ] _ { i j } = \sum _ { s = 1 } ^ { m } a _ { i s } ( B C ) _ { s j } = \sum _ { s = 1 } ^ { m } a _ { i s } \left( \sum _ { l = 1 } ^ { k } b _ { s l } c _ { l j } \right) = \sum _ { s = 1 } ^ { m } \sum _ { l = 1 } ^ { k } a _ { i s } b _ { s l } c _ { l j } .
$$

Similarly, $A B$ is an $n \times k$ matrix with entries

$$
( A B ) _ { i j } = \sum _ { s = 1 } ^ { m } a _ { i s } b _ { s j } ,
$$

so $( A B ) C$ is an $n \times p$ matrix with entries

$$
\{ ( A B ) C \} _ { i j } = \sum _ { l = 1 } ^ { k } ( A B ) _ { i l } c _ { l j } = \sum _ { l = 1 } ^ { k } \left( \sum _ { s = 1 } ^ { m } a _ { i s } b _ { s l } \right) c _ { l j } = \sum _ { l = 1 } ^ { k } \sum _ { s = 1 } ^ { m } a _ { i s } b _ { s l } c _ { l j } .
$$

Interchanging the order of summation on the right side gives

$$
[ ( A B ) C ] _ { i j } = \sum _ { s = 1 } ^ { m } \sum _ { l = 1 } ^ { k } a _ { i s } b _ { s l } c _ { l j } = [ A ( B C ) ] _ { i j } ,
$$

for each $i = 1 , 2 , \dots , n$ and $j = 1 , 2 , \dots , p$ .So $A ( B C ) = ( A B ) C$

The linear system

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ { \vdots \qquad \vdots } \\ { a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = b _ { n } , } \end{array}
$$

can be viewed as the matrix equation

$$
A \mathbf { x } = \mathbf { b } ,
$$

where

$$
A = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right] } , \quad \mathbf { x } = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] } , \quad { \mathrm { a n d } } \quad \mathbf { b } = { \left[ \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right] } .
$$

Related to the linear systems is the inverse of a matrix.

# Definition 6.10

An n X n matrix A is said to be nonsingular (or invertible) if an n × n matrix A-l exists with AA-1 = A-1A = I. The matrix A-1 is called the inverse of A. A matrix without an inverse is called singular (or noninvertible).

The following properties regarding matrix inverses follow from Definition 6.10. The proofs of these results are considered in Exercise 5.

# Theorem 6.11

For any nonsingular $n \times n$ matrix A:

a. $A ^ { - 1 }$ is unique. b. $A ^ { - 1 }$ is nonsingular and $( A ^ { - 1 } ) ^ { - 1 } = A$ ： c. If $B$ is also a nonsingular $n \times n$ matrix, then

$$
( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 } .
$$

# EXAMPLE 4 Let

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} } \right] \quad { \mathrm { a n d } } \quad B = \left[ { \begin{array} { r r r } { - { \frac { 2 } { 9 } } } & { { \frac { 5 } { 9 } } } & { - { \frac { 1 } { 9 } } } \\ { { \frac { 4 } { 9 } } } & { - { \frac { 1 } { 9 } } } & { { \frac { 2 } { 9 } } } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } \right] .
$$

Then

$$
A B = { \left[ \begin{array} { r r r } { 1 } & { { \dot { 2 } } } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} \right] } \cdot { \left[ \begin{array} { r r r } { - { \frac { 2 } { 9 } } } & { { \frac { 5 } { 9 } } } & { - { \frac { 1 } { 9 } } } \\ { { \frac { 4 } { 9 } } } & { - { \frac { 1 } { 9 } } } & { { \frac { 2 } { 9 } } } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} \right] } = { \left[ \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } = I _ { 3 } .
$$

In a similar manner, BA = I3,so A and B are nonsingular with B = A-1 and A = B-1.

If we have the inverse of $A$ , we can easily solve a linear system of the form $\pmb { A } \mathbf { x } = \mathbf { b }$ Suppose, for example, we want to solve

$$
\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } - \ x _ { 3 } = 2 , } \\ { 2 x _ { 1 } + \ x _ { 2 } \qquad = 3 , } \\ { - x _ { 1 } + \ x _ { 2 } + 2 x _ { 3 } = 4 . } \end{array}
$$

First, convert the system to the matrix equation

$$
\left[ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} } \right] \left[ { \begin{array} { r } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } \right] = \left[ { \begin{array} { r } { 2 } \\ { 3 } \\ { 4 } \end{array} } \right] ,
$$

and then multiply both sides by the inverse:

$$
{ \begin{array} { r l } { - { \frac { 2 } { 9 } } } & { \quad { \frac { 5 } { 9 } } } & { \quad - { \frac { 1 } { 9 } } } \\ { \quad { \frac { 4 } { 9 } } } & { \quad - { \frac { 1 } { 9 } } } & { \quad { \frac { 2 } { 9 } } } \\ { - { \frac { 1 } { 3 } } } & { \quad { \frac { 1 } { 3 } } } & { \quad { \frac { 1 } { 3 } } } \end{array} } \left( { \left[ \begin{array} { l l l } { \quad 1 } & { \quad 2 } & { \quad - 1 } \\ { \quad 2 } & { \quad 1 } & { \quad 0 } \\ { \quad - 1 } & { \quad 1 } & { \quad 2 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } \right) = { \left[ \begin{array} { l l l } { - { \frac { 2 } { 9 } } } & { \quad { \frac { 5 } { 9 } } } & { \quad - { \frac { 1 } { 9 } } } \\ { \quad { \frac { 4 } { 9 } } } & { \quad - { \frac { 1 } { 9 } } } & { \quad { \frac { 2 } { 9 } } } \\ { \quad - { \frac { 1 } { 3 } } } & { \quad { \frac { 1 } { 3 } } } & { \quad { \frac { 1 } { 3 } } } \end{array} \right] } { \left[ \begin{array} { l } { 2 } \\ { 3 } \\ { 4 } \end{array} \right] } = { \left[ \begin{array} { l } { \quad { \frac { 7 } { 9 } } } \\ { \quad { \frac { 5 } { 9 } } } \\ { \quad { \frac { 5 } { 3 } } } \end{array} \right] } { \left[ \begin{array} { l } { \quad 1 } \\ { 0 } \\ { \quad - 1 } \end{array} \right] }
$$

so

$$
\begin{array} { r l r } & { } & { \left[ \begin{array} { c } { \frac { 7 } { 9 } } \\ { \frac { 1 3 } { 9 } } \\ { \frac { 5 } { 3 } } \end{array} \right] = \left( \left[ \begin{array} { c c c } { - \frac { 2 } { 9 } } & { \frac { 5 } { 9 } } & { - \frac { 1 } { 9 } } \\ { \frac { 4 } { 9 } } & { - \frac { 1 } { 9 } } & { \frac { 2 } { 9 } } \\ { - \frac { 3 } { 9 } } & { \frac { 3 } { 9 } } & { \frac { 3 } { 9 } } \end{array} \right] \left[ \begin{array} { c c c } { 1 } & { 2 } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} \right] \right) \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] = I _ { 3 } \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] . } \end{array}
$$

This gives the solution $x _ { 1 } = 7 / 9$ ， $x _ { 2 } = 1 3 / 9$ ,and $x _ { 3 } = 5 / 3$

Although it is easy to solve a linear system of the form $\pmb { A } \mathbf { x } = \mathbf { b }$ if $A ^ { - 1 }$ is known, it is not computationally efficient to determine $A ^ { - 1 }$ in order to solve the system. (See Exercise 8.) Even so, it is useful from a conceptual standpoint to describe a method for determining the inverse of a matrix.

To find a method of computing $A ^ { - 1 }$ assuming its existence, let us look again at matrix multiplication. Let $B _ { j }$ be the $j$ th column of the $n \times n$ matrix $B$ ，

$$
B _ { j } = \left[ \begin{array} { c } { b _ { 1 j } } \\ { b _ { 2 j } } \\ { \vdots } \\ { b _ { n j } } \end{array} \right] .
$$

If $A B = C$ , then the $j$ th column of $C$ is given by the product

$$
{ \left[ \begin{array} { l } { c _ { 1 j } } \\ { c _ { 2 j } } \\ { \vdots } \\ { c _ { n j } } \end{array} \right] } = C _ { j } = A B _ { j } = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n n } } \end{array} \right] } { \left[ \begin{array} { l } { b _ { 1 j } } \\ { b _ { 2 j } } \\ { \vdots } \\ { b _ { n j } } \end{array} \right] } = { \left[ \begin{array} { l } { \sum _ { k = 1 } ^ { n } a _ { 1 k } b _ { k j } } \\ { \sum _ { k = 1 } ^ { n } a _ { 2 k } b _ { k j } } \\ { \vdots } \\ { \sum _ { k = 1 } ^ { n } a _ { n k } b _ { k j } } \end{array} \right] } .
$$

Suppose that $A ^ { - 1 }$ exists and that $A ^ { - 1 } = B = ( b _ { i j } )$ . Then $A B = 1$ and

$$
A B _ { j } = \left[ \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] ,
$$

To find $B$ we must solve $\pmb { n }$ linear systems in which the $j$ th column of the inverse is the solution of the linear system with right-hand side the $j$ th column of $I$ . The next example demonstrates this method.

To determine the inverse of the matrix

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} } \right] ,
$$

let us first consider the product $A B$ ,where $\pmb { B }$ is an arbitrary $3 \times 3$ matrix.

$$
{ \begin{array} { r l } & { A B = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } \end{array} \right] } { \left[ \begin{array} { l l l } { b _ { 1 1 } } & { b _ { 1 2 } } & { b _ { 1 3 } } \\ { b _ { 2 1 } } & { b _ { 2 2 } } & { b _ { 2 3 } } \\ { b _ { 3 1 } } & { b _ { 3 2 } } & { b _ { 3 3 } } \end{array} \right] } } \\ & { \qquad = { \left[ \begin{array} { l l l } { b _ { 1 1 } + 2 b _ { 2 1 } - b _ { 3 1 } } & { b _ { 1 2 } + 2 b _ { 2 2 } - b _ { 3 2 } } & { b _ { 1 3 } + 2 b _ { 2 3 } - b _ { 3 3 } } \\ { 2 b _ { 1 1 } + b _ { 2 1 } } & { 2 b _ { 1 2 } + b _ { 2 2 } } & { 2 b _ { 1 3 } + b _ { 2 3 } } \\ { - b _ { 1 1 } + b _ { 2 1 } + 2 b _ { 3 1 } } & { - b _ { 1 2 } + b _ { 2 2 } + 2 b _ { 3 2 } } & { - b _ { 1 3 } + b _ { 2 3 } + 2 b _ { 3 3 } } \end{array} \right] } . } \end{array} }
$$

If $B = A ^ { - 1 }$ ,then $A B = I$ , so we must have

$$
\begin{array} { r l r } { b _ { 1 1 } + 2 b _ { 2 1 } - } & { { } b _ { 3 1 } = 1 , } & { b _ { 1 2 } + 2 b _ { 2 2 } - } & { b _ { 3 2 } = 0 , } & { b _ { 1 3 } + 2 b _ { 2 3 } - } \\ { 2 b _ { 1 1 } + } & { { } b _ { 2 1 } } & { = 0 , } & { 2 b _ { 1 2 } + } & { b _ { 2 2 } = 1 , } & { 2 b _ { 1 3 } + } & { b _ { 2 3 } = 0 , } \\ { - b _ { 1 1 } + } & { { } b _ { 2 1 } + 2 b _ { 3 1 } = 0 , } & { - b _ { 1 2 } + } & { b _ { 2 2 } + 2 b _ { 3 2 } = 0 , } & { - b _ { 1 3 } + } & { b _ { 2 3 } + 2 b _ { 3 3 } = 1 . } \end{array}
$$

Notice that the coefficients in each of the systems of equations are the same,the only change in the systems occurs on the right side of the equations. As a consequence, Gaussian elimination can be performed on a larger augmented matrix formed by combining the matrices for each of the systems:

$$
\left[ { \begin{array} { r r r r r r } { 1 } & { 2 } & { - 1 } & { \vdots } & { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { \vdots } & { 0 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { 2 } & { \vdots } & { 0 } & { 0 } & { 1 } \end{array} } \right] .
$$

First, performing $( E _ { 2 } - 2 E _ { 1 } )  ( E _ { 2 } )$ and $( E _ { 3 } + E _ { 1 } )  ( E _ { 3 } )$ , followed by $( E _ { 3 } + E _ { 2 } ) $ $( E _ { 3 } )$ produces

$$
\left[ { \begin{array} { c c c c c c } { 1 } & { 2 } & { - 1 } & { \vdots } & { 1 } & { 0 } & { 0 } \\ { 0 } & { - 3 } & { 2 } & { \vdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 3 } & { 1 } & { \vdots } & { 1 } & { 0 } & { 1 } \end{array} } \right] \quad { \mathrm { a n d } } \quad \left[ { \begin{array} { c c c c c c } { 1 } & { 2 } & { - 1 } & { \vdots } & { 1 } & { 0 } & { 0 } \\ { 0 } & { - 3 } & { 2 } & { \vdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { \vdots } & { - 1 } & { 1 } & { 1 } \end{array} } \right] .
$$

Backward substitution is performed on each of the three augmented matrices,

$$
\left[ { \begin{array} { r r r r r } { 1 } & { 2 } & { - 1 } & { \vdots } & { 1 } \\ { 0 } & { - 3 } & { 2 } & { \vdots } & { - 2 } \\ { 0 } & { 0 } & { 3 } & { \vdots } & { - 1 } \end{array} } \right] , \left[ { \begin{array} { r r r r r } { 1 } & { 2 } & { - 1 } & { \vdots } & { 0 } \\ { 0 } & { - 3 } & { 2 } & { \vdots } & { 1 } \\ { 0 } & { 0 } & { 3 } & { \vdots } & { 1 } \end{array} } \right] , \left[ { \begin{array} { r r r r } { 1 } & { 2 } & { - 1 } & { \vdots } & { 0 } \\ { 0 } & { - 3 } & { 2 } & { \vdots } & { 0 } \\ { 0 } & { 0 } & { 3 } & { \vdots } & { 1 } \end{array} } \right] ,
$$

to eventually give

$$
\begin{array} { l l l } { { b _ { 1 1 } = - \frac { 2 } { 9 } , ~ } } & { { b _ { 1 2 } = \frac { 5 } { 9 } , ~ } } & { { b _ { 1 3 } = - \frac { 1 } { 9 } , } } \\ { { b _ { 2 1 } = \frac { 4 } { 9 } , ~ } } & { { b _ { 2 2 } = - \frac { 1 } { 9 } , ~ } } & { { ~ \mathrm { a n d } ~ b _ { 2 3 } = \frac { 2 } { 9 } , } } \\ { { b _ { 3 1 } = - \frac { 1 } { 3 } , ~ } } & { { b _ { 3 2 } = \frac { 1 } { 3 } , ~ } } & { { b _ { 3 2 } = \frac { 1 } { 3 } . } } \end{array}
$$

As shown in Example 4, these are the entries of $A ^ { - 1 }$ ：

$$
A ^ { - 1 } = \left[ { \begin{array} { r r r } { - { \frac { 2 } { 9 } } } & { { \frac { 5 } { 9 } } } & { - { \frac { 1 } { 9 } } } \\ { { \frac { 4 } { 9 } } } & { - { \frac { 1 } { 9 } } } & { { \frac { 2 } { 9 } } } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } \right]
$$

In the last example we ilustrated the computation of $A ^ { - 1 }$ . As we saw in that example, it is convenient to set up a larger augmented matrix,

$$
\left[ \begin{array} { l l l } { A } & { \vdots } & { I } \end{array} \right] .
$$

Upon performing the elimination in accordance with Algorithm 6.1, we obtain an augmented matrix of the form

$$
\begin{array} { r } { \left\{ \begin{array} { r l r l } { U } & { { } : } & { Y } \end{array} \right\} , } \end{array}
$$

where $U$ is an upper-triangular matrix and $\pmb { Y }$ is the matrix obtained by performing the same operations on the identity $I$ that were performed to take $A$ into $U$

Gaussian elimination with backward substitution requires $4 n ^ { 3 } / 3 - n / 3$ multiplications/divisions and $4 n ^ { 3 } / 3 - 3 n ^ { 2 } / 2 + n / 6$ additions/subtractions to solve the $\pmb { n }$ linear systems (see Exercise 8(a)). Special care can be taken in the implementation to note the operations that need not be performed,as, for example, a multiplication when one of the multipliers is known to be unity or a subtraction when the subtrahend is known to be O. The number of multiplications/divisions required can then be reduced to $n ^ { 3 }$ and the number of additions/subtractions reduced to $n ^ { \bar { 3 } } - 2 n ^ { 2 } + n$ (see Exercise 8(d)).

Another important matrix associated with a given matrix $A$ is its transpose, denoted $A ^ { t }$ .

The transpose of an $n \times m$ matrix $A = ( a _ { i j } )$ is the $m \times n$ matrix $A ^ { t }$ ,where for each $i$ ,the ith column of $A ^ { t }$ is the same as the ith row of $A$ ,that is, $A ^ { \prime } = \{ a _ { j i } )$ . A square matrix $A$ is called symmetric if $A = A ^ { t }$ ·

For example, the matrices

$$
A = { \left[ \begin{array} { l l l } { 7 } & { 2 } & { 0 } \\ { 3 } & { 5 } & { - 1 } \\ { 0 } & { 5 } & { - 6 } \end{array} \right] } , \quad B = { \left[ \begin{array} { l l l } { 2 } & { 4 } & { 7 } \\ { 3 } & { - 5 } & { - 1 } \end{array} \right] } , \quad C = { \left[ \begin{array} { l l l } { 6 } & { 4 } & { - 3 } \\ { 4 } & { - 2 } & { 0 } \\ { - 3 } & { 0 } & { 1 } \end{array} \right] }
$$

have transposes

$$
A ^ { t } = { \left[ \begin{array} { l l r } { 7 } & { 3 } & { 0 } \\ { 2 } & { 5 } & { 5 } \\ { 0 } & { - 1 } & { - 6 } \end{array} \right] } , \quad B ^ { t } = { \left[ \begin{array} { l l } { 2 } & { 3 } \\ { 4 } & { - 5 } \\ { 7 } & { - 1 } \end{array} \right] } , \quad C ^ { t } = { \left[ \begin{array} { l l r } { 6 } & { 4 } & { - 3 } \\ { 4 } & { - 2 } & { 0 } \\ { - 3 } & { 0 } & { 1 } \end{array} \right] } .
$$

The matrix $C$ is symmetric since $C ^ { t } = C$ , but the matrices $\pmb { A }$ and $B$ are not.

The proof of the next result follows directly from the definition of the transpose.

# Theorem 6.13

The following operations involving the transpose of a matrix hold whenever the operation is possible:

a. $( A ^ { t } ) ^ { t } = A ,$ ${ \bf b } . \quad ( A + B ) ^ { t } = A ^ { t } + B ^ { t } .$ ， c. $( A B ) ^ { t } = B ^ { t } A ^ { t } ;$ ， d.if $A ^ { - 1 }$ exists, then $( A ^ { - 1 } ) ^ { t } = ( A ^ { t } ) ^ { - 1 }$ ·

Any CAS can be used to perform matrix operations. For example,matrix addition is done in Maple with matadd(A,B) or evalm $( A + B )$ . Scalar multiplication is defined by scalarmul(A,c) or evalm $( c * A )$

Matrix multiplication is done using multiply(A,B) or evalm $( A B C * B )$ . Matrix transposition is achieved with transpose(A) and matrix inversion, with inverse (A).

# ExErcise Set 6.3

1.Determine which of the following matrices are nonsingular,and compute the inverse of these matrices:

$\begin{array} { r l } { \mathbf { a } } & { { } \left[ \begin{array} { c c c } { 4 } & { 2 } & { 6 7 } \\ { 3 } & { 0 } & { 7 } \\ { - 2 } & { - 1 } & { - 3 } \end{array} \right] } \\ { \mathbf { c } . } & { { } \left[ \begin{array} { c c c } { 4 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} \right] } \end{array}$ $\begin{array} { r l } { \mathbf { h . } } & { { } \left[ \begin{array} { l l l } { 1 } & { 2 } & { 0 } \\ { 2 } & { 1 } & { - 1 } \\ { 3 } & { 1 } & { 1 } \end{array} \right] } \\ { \mathbf { d . } } & { { } \left[ \begin{array} { l l l l l } { 1 } & { 1 } & { - 1 } & { 1 } \\ { 1 } & { 2 } & { - 4 } & { - 2 } \\ { 2 } & { 1 } & { 1 } & { 5 } \\ { - 1 } & { 0 } & { - 2 } & { - 4 } \end{array} \right] } \\ { \mathbf { f . } } & { { } \left[ \begin{array} { l l l l l } { 2 } & { 0 } & { 1 } & { 2 } \\ { 1 } & { 1 } & { 0 } & { 2 } \\ { 2 } & { - 1 } & { 3 } & { 1 } \\ { 3 } & { - 1 } & { 4 } & { 3 } \end{array} \right] } \end{array}$ e. $\left[ \begin{array} { l l l l } { 4 } & { 0 } & { 0 } & { 0 } \\ { 6 } & { 7 } & { 0 } & { 0 } \\ { 9 } & { 1 1 } & { 1 } & { 0 } \\ { 5 } & { 4 } & { 1 } & { 1 } \end{array} \right]$

2.Consider the four $3 \times 3$ linear systems having the same coefficient matrix:

$$
\begin{array} { r l } { { 2 x _ { 1 } - 3 x _ { 2 } + \ x _ { 3 } = 2 , } } & { { \qquad 2 x _ { 1 } - 3 x _ { 2 } + \ x _ { 3 } = 6 , } } \\ { { x _ { 1 } + \ x _ { 2 } - \ x _ { 3 } = - 1 , } } & { { \qquad x _ { 1 } + \ x _ { 2 } - \ x _ { 3 } = 4 , } } \\ { { - x _ { 1 } + \ x _ { 2 } - 3 x _ { 3 } = 0 ; } } & { { \qquad - x _ { 1 } + \ x _ { 2 } - 3 x _ { 3 } = 5 ; } } \end{array}
$$

$$
\begin{array} { r l } { { 2 x _ { 1 } - 3 x _ { 2 } + } } & { { x _ { 3 } = 0 , } } \\ { { x _ { 1 } + \ x _ { 2 } - } } & { { x _ { 3 } = 1 , } } \\ { { - x _ { 1 } + \ x _ { 2 } - 3 x _ { 3 } = - 3 ; } } & { { \qquad - x _ { 1 } + \ x _ { 2 } - 3 x _ { 3 } = 0 . } } \end{array}
$$

a.Solve the linear systems by applying Gaussian elimination to the augmented matrix

$$
\left[ { \begin{array} { r r r r r r r r r } { 2 } & { - 3 } & { 1 } & { \vdots } & { 2 } & { 6 } & { 0 } & { - 1 } \\ { 1 } & { 1 } & { - 1 } & { \vdots } & { - 1 } & { 4 } & { 1 } & { 0 } \\ { - 1 } & { 1 } & { - 3 } & { \vdots } & { 0 } & { 5 } & { - 3 } & { 0 } \end{array} } \right] .
$$

b.Solve the linear systems by finding and multiplying by the inverse of

$$
A = \left[ { \begin{array} { r r r } { 2 } & { - 3 } & { 1 } \\ { 1 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { - 3 } \end{array} } \right] { \mathrm { . } }
$$

c. Which method requires more operations?

3.Repeat Exercise 2 using the linear systems

$$
\begin{array} { r l } { x _ { 1 } - x _ { 2 } + 2 x _ { 3 } - } & { x _ { 4 } = 6 , } \\ { x _ { 1 } \qquad - \ x _ { 3 } + \ x _ { 4 } = 4 , } & { \qquad x _ { 1 } \qquad - \ x _ { 3 } + \ x _ { 4 } = 1 , } \\ { 2 x _ { 1 } + x _ { 2 } + 3 x _ { 3 } - 4 x _ { 4 } = - 2 , } & { \qquad 2 x _ { 1 } + x _ { 2 } + 3 x _ { 3 } - 4 x _ { 4 } = 2 , } \\ { - x _ { 2 } + \ x _ { 3 } - } & { x _ { 4 } = 5 ; } \end{array}
$$

4.Prove the following statements or provide counterexamples to show they are not true.

a. The product of two symmetric matrices is symmetric.   
b. The inverse of a nonsingular symmetric matrix is a nonsingular symmetric matrix.   
c. If $\pmb { A }$ and $B$ are $n \times n$ matrices, then $( A B ) ^ { t } = A ^ { t } B ^ { t }$ .

5.The following statements are needed to prove Theorem 6.11.

a. Show that if $A ^ { - 1 }$ exists, it is unique.   
b. Show that if $\pmb { A }$ is nonsingular, then $( A ^ { - 1 } ) ^ { - 1 } = A$   
c. Show that if $A$ and $B$ are nonsingular $n \times n$ matricies, then $( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 }$

6.Prove Theorem 6.5.

7．a.Show that the product of two $n \times n$ lower triangular matrices is lower triangular. $\mathbf { b } .$ Show that the product of two $n \times n$ upper triangular matrices is upper triangular. $\pmb { \mathrm { c } } _ { \bullet }$ Show that the inverse of a nonsingular $n \times n$ lower triangular matrix is lower triangular.

8.Suppose $^ { m }$ linear systems

$$
A \mathbf { x } ^ { ( p ) } = \mathbf { b } ^ { ( p ) } , \quad p = 1 , 2 , \ldots , m ,
$$

are to be solved, each with the $n \times n$ coefficient matrix $A$ ：

a. Show that Gaussian elimination with backward substitution applied to the augmented matrix

$$
\left[ A : ~ \mathbf { b } ^ { ( 1 ) } \mathbf { b } ^ { ( 2 ) } \cdots \mathbf { b } ^ { ( m ) } \right]
$$

requires

$$
{ \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 3 } } n \quad { \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s } }
$$

and

$$
{ \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n ^ { 2 } - m n + { \frac { 1 } { 6 } } n \quad { \mathrm { a d d i t i o n s / s u b t r a c t i o n s } } .
$$

b. Show that the Gaus-Jordan method (see Exercise 8, Section 6.1） applied to the augmented matrix

$$
\left[ A : ~ { \bf b } ^ { ( 1 ) } { \bf b } ^ { ( 2 ) } \cdot \cdot \cdot { \bf b } ^ { ( m ) } \right]
$$

requires

$$
{ \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n \quad { \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s } }
$$

and

$$
{ \frac { 1 } { 2 } } n ^ { 3 } + ( m - 1 ) n ^ { 2 } + \left( { \frac { 1 } { 2 } } - m \right) n \quad { \mathrm { a d d i t i o n s / s u b t r a c t i o n s } } .
$$

c.For the special case

$$
\begin{array} { r } { \mathbf { b } ^ { ( p ) } = [ \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \\ { \vdots } \\ { 0 } \end{array} ]  p \mathrm { t h } \mathrm { r o w } , } \end{array}
$$

for each $p = 1 , \ldots , m$ ，with $m = n$ , the solution $\mathbf { x } ^ { ( p ) }$ is the $p$ th column of $A ^ { - 1 }$ . Show that Gaussian elimination with backward substitution requires

$$
{ \frac { 4 } { 3 } } n ^ { 3 } - { \frac { 1 } { 3 } } n \quad { \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s } }
$$

and

$$
{ \frac { 4 } { 3 } } n ^ { 3 } - { \frac { 3 } { 2 } } n ^ { 2 } + { \frac { 1 } { 6 } } n \quad { \mathrm { a d d i t i o n s / s u b t r a c t i o n s } }
$$

for this application,and that the Gauss-Jordan method requires

$$
{ \frac { 3 } { 2 } } n ^ { 3 } - { \frac { 1 } { 2 } } n \quad \mathrm { m u l t i p l i c a t i o n s / d i v i s i o n s }
$$

and

$$
{ \frac { 3 } { 2 } } n ^ { 3 } - 2 n ^ { 2 } + { \frac { 1 } { 2 } } n \quad { \mathrm { a d d i t i o n s / s u b t r a c t i o n s } } .
$$

d. Construct an algorithm using Gaussian elimination to find $A ^ { - 1 }$ , but do not perform multiplications when one of the multipliers is known to be 1,and do not perform additions/subtractions when one of the elements involved is known to be O. Show that the required computations are reduced to $n ^ { 3 }$ multiplications/divisions and $n ^ { 3 } - 2 n ^ { 2 } + n$ additions/subtractions.

e. Show that solving the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ ,when $A ^ { - 1 }$ is known, still requires $n ^ { 2 }$ multiplications/divisions and $n ^ { 2 } - n$ additions/subtractions.

f. Show that solving $m$ linear systems $A \mathbf { x } ^ { ( p ) } = \mathbf { b } ^ { ( p ) }$ ,for $p = 1 , 2 , \ldots , m$ , by the method $\mathbf { x } ^ { ( p ) } = A ^ { - 1 } \mathbf { b } ^ { ( p ) }$ requires $m n ^ { 2 }$ multiplications and $m ( n ^ { 2 } - n )$ additions, if $A ^ { - 1 }$ is known.

g. Let $\pmb { A }$ be an $n \times n$ matrix. Compare the number of operations required to solve $n$ linear systems involving $\pmb { A }$ by Gaussian elimination with backward substitution and by first inverting $A$ and then multiplying $A \mathbf { x } = \mathbf { b }$ by $A ^ { - 1 }$ ，for $n \ = \ 3$ ,10,50,100. Is it ever advantageous to compute $A ^ { - 1 }$ for the purpose of solving linear systems ?

9.Use the algorithm developed in Exercise 8(d) to find the inverses of the nonsingular matrices in Exercise 1.

10.It is often useful to partition matrices into a collection of submatrices. For example, the matrices

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 3 } & { - 4 } & { - 3 } \\ { 6 } & { 5 } & { 0 } \end{array} \right] } \quad { \mathrm { a n d } } \quad B = { \left[ \begin{array} { l l l l } { 2 } & { - 1 } & { 7 } & { 0 } \\ { 3 } & { 0 } & { 4 } & { 5 } \\ { - 2 } & { 1 } & { - 3 } & { 1 } \end{array} \right] }
$$

can be partitioned into

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { \vdots } \\ { 3 } & { - 4 } & { \vdots } \\ { \vdots } & { \cdot \cdot \cdot \vdots } & { \vdots } \\ { 6 } & { 5 } & { \vdots } \end{array} \right] } = { \left[ \begin{array} { l } { A _ { 1 1 } } \\ { \dots \dots \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { A _ { 2 1 } } \end{array} \right] }
$$

and

$$
{ \left[ \begin{array} { l l l l l } { 2 } & { - 1 } & { 7 } & { \vdots } & { 0 } \\ { 3 } & { 0 } & { 4 } & { \vdots } & { 5 } \\ { \cdots { \bar { 2 } } } & { 1 } & { - 3 } & { \vdots } & { \ddots } \\ { - 2 } & { 1 } & { - 3 } & { \vdots } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l l } { B _ { 1 1 } } & { \cdot } & { B _ { 1 2 } } \\ { \cdot \dots \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { B _ { 2 1 } } & { \cdot \cdot \cdot } & { B _ { 2 2 } } \end{array} \right] }
$$

a. Show that the product of $A$ and $B$ in this case is

$$
A B = { \left[ \begin{array} { l l l } { A _ { 1 1 } B _ { 1 1 } + A _ { 1 2 } B _ { 2 1 } } & { \colon } & { A _ { 1 1 } B _ { 1 2 } + A _ { 1 2 } B _ { 2 2 } } \\ { \therefore \therefore \therefore \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { A _ { 2 1 } B _ { 1 1 } + A _ { 2 2 } B _ { 2 1 } } & { \colon } & { A _ { 2 1 } B _ { 1 2 } + A _ { 2 2 } B _ { 2 2 } } \end{array} \right] }
$$

b.If $B$ were instead partitioned into

$$
B = \left[ { \begin{array} { c c c c c } { 2 } & { - 1 } & { 7 } & { \vdots } & { 0 } \\ { 3 } & { 0 } & { 4 } & { \vdots } & { 5 } \\ { - 2 } & { 1 } & { - 3 } & { \vdots } & { 1 } \end{array} } \right] = \left[ { \begin{array} { c c c c c } { B _ { 1 1 } } & { \cdot } & { B _ { 1 2 } } \\ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } & { \cdot \cdot \cdot } \\ { B _ { 2 1 } } & { \cdot \cdot \cdot \cdot \cdot } & { B _ { 2 2 } } \end{array} } \right] ,
$$

would the result in part (a) hold?

c. Make a conjecture concerning the conditions necessary for the result in part (a) to hold in the general case.

11. In a paper entitled “Population Waves," Bernadelli [Ber] (see also [Se]) hypothesizes a type of simplified beetle that has a natural life span of 3 years.The female of this species has a survival rate of $\frac { 1 } { 2 }$ in the first year of life,has a survival rate of $\frac { 1 } { 3 }$ from the second to third years, and gives birth to an average of six new females before expiring at the end of the third year. A matrix can be used to show the contribution an individual female beetle makes,in a probabilistic sense,to the female population of the species by letting $a _ { i j }$ in the matrix $A = \left( a _ { i j } \right)$ denote the contribution that a single female beetle of age $j$ will make to the next year's female population of age $i$ ; that is,

$$
A = \left[ \begin{array} { l l l } { 0 } & { 0 } & { 6 } \\ { \frac { 1 } { 2 } } & { 0 } & { 0 } \\ { 0 } & { \frac { 1 } { 3 } } & { 0 } \end{array} \right] .
$$

a. The contribution that a female beetle makes to the population 2 years hence is determined from the entries of $A ^ { 2 }$ , of 3 years hence from $A ^ { 3 }$ ,and so on. Construct $A ^ { 2 }$ and $A ^ { 3 }$ ,and try to make a general statement about the contribution of a female beetle to the population in $\pmb { n }$ years’ time for any positive integral value of $\pmb { n }$   
b. Use your conclusions from part (a) to describe what wil occur in future years to a population of these beetles that initially consists of 6oOO female beetles in each of the three age groups.   
c. Construct $A ^ { - 1 }$ , and describe its significance regarding the population of this species.

12. The study of food chains is an important topic in the determination of the spread and accumulation of environmental pollutants in living matter. Suppose that a food chain has three links. The first link consists of vegetation of types $v _ { 1 } , v _ { 2 } , \ldots , v _ { n }$ ， which provide all the food requirements for herbivores of species $h _ { 1 } , h _ { 2 } , \ldots , h _ { m }$ in the second link. The third link consists of carmivorous animals $c _ { 1 } , c _ { 2 } , \ldots , c _ { k }$ ， which depend entirely on the herbivores in the second link for their food supply. The coordinate $a _ { i j }$ of the matrix

$$
A = \left[ \begin{array} { c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 m } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 m } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n m } } \end{array} \right]
$$

represents the total number of plants of type $\upsilon _ { i }$ eaten by the herbivores in the species $h _ { j }$ ， whereas $b _ { i j }$ in

$$
B = \left[ \begin{array} { c c c c } { b _ { 1 1 } } & { b _ { 1 2 } } & { \cdot \cdot \cdot } & { b _ { 1 k } } \\ { b _ { 2 1 } } & { b _ { 2 2 } } & { \cdot \cdot \cdot } & { b _ { 2 k } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { b _ { m 1 } } & { b _ { m 2 } } & { \cdot \cdot \cdot } & { b _ { m k } } \end{array} \right]
$$

describes the number of herbivores in species $h _ { i }$ that are devoured by the animals of type $c _ { j }$

a. Show that the number of plants of type $v _ { i }$ that eventually end up in the animals of species $c _ { j }$ is given by the entry in the ith row and $j$ th column of the matrix $A B$ ·   
b. What physical significance is associated with the matrices $A ^ { - 1 } , B ^ { - 1 }$ ，and $( A B ) ^ { - 1 } =$ $B ^ { - 1 } A ^ { - 1 } \ b { \zeta }$

13. In Section 3.5 we found that the parametric form $( x ( t ) , y ( t ) )$ of the cubic Hermite polynomials through $( x ( 0 ) , y ( 0 ) ) = ( x _ { 0 } , y _ { 0 } )$ and $( x ( 1 ) , y ( 1 ) ) = ( x _ { 1 } , y _ { 1 } )$ with guide points $( x _ { 0 } + \alpha _ { 0 } , y _ { 0 } +$ $\beta _ { 0 } )$ and $( x _ { 1 } - \alpha _ { 1 } , y _ { 1 } - \beta _ { 1 } )$ , respectively, are given by

$$
x ( t ) = [ 2 ( x _ { 0 } - x _ { 1 } ) + ( \alpha _ { 0 } + \alpha _ { 1 } ) ] t ^ { 3 } + [ 3 ( x _ { 1 } - x _ { 0 } ) - \alpha _ { 1 } - 2 \alpha _ { 0 } ] t ^ { 2 } + \alpha _ { 0 } t + x _ { 0 }
$$

and

$$
y ( t ) = [ 2 ( y _ { 0 } - y _ { 1 } ) + ( \beta _ { 0 } + \beta _ { 1 } ) ] t ^ { 3 } + [ 3 ( y _ { 1 } - y _ { 0 } ) - \ \beta _ { 1 } - 2 \beta _ { 0 } ] t ^ { 2 } + \beta _ { 0 } t + y _ { 0 } .
$$

The Bézier cubic polynomials have the form

$$
\hat { x } ( t ) = [ 2 ( x _ { 0 } - x _ { 1 } ) + 3 ( \alpha _ { 0 } + \alpha _ { 1 } ) ] t ^ { 3 } + [ 3 ( x _ { 1 } - x _ { 0 } ) - 3 ( \alpha _ { 1 } + 2 \alpha _ { 0 } ) ] t ^ { 2 } + 3 \alpha _ { 0 } t + x _ { 0 }
$$

and

$$
\hat { y } ( t ) = [ 2 ( y _ { 0 } - y _ { 1 } ) + 3 ( \beta _ { 0 } + \beta _ { 1 } ) ] t ^ { 3 } + [ 3 ( y _ { 1 } - y _ { 0 } ) - 3 ( \beta _ { 1 } + 2 \beta _ { 0 } ) ] t ^ { 2 } + 3 \beta _ { 0 } t + y _ { 0 } .
$$

a. Show that the matrix

$$
A = \left[ { \begin{array} { r r r r } { 7 } & { 4 } & { 4 } & { 0 } \\ { - 6 } & { - 3 } & { - 6 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right]
$$

transforms the Hermite polynomial coeficients into the Bézier polynomial coefficients.

b. Determine a matrix $B$ that transforms the Bezier polynomial coeffcients into the Hermite polynomial coefficients.

14. Consider the $2 \times 2$ linear system $( A + i B ) ( { \bf x } + i { \bf y } ) = { \bf c } + i { \bf d }$ with complex entries in component form:

$$
\begin{array} { r } { ( a _ { 1 1 } + i b _ { 1 1 } ) ( x _ { 1 } + i y _ { 1 } ) + ( a _ { 1 2 } + i b _ { 1 2 } ) ( x _ { 2 } + i y _ { 2 } ) = c _ { 1 } + i d _ { 1 } , } \\ { ( a _ { 2 1 } + i b _ { 2 1 } ) ( x _ { 1 } + i y _ { 1 } ) + ( a _ { 2 2 } + i b _ { 2 2 } ) ( x _ { 2 } + i y _ { 2 } ) = c _ { 2 } + i d _ { 2 } . } \end{array}
$$

a. Use the properties of complex numbers to convert this system to the equivalent $4 \times 4$ real linear system

$$
\begin{array} { r } { A \mathbf { x } - B \mathbf { y } = \mathbf { c } , } \\ { B \mathbf { x } + A \mathbf { y } = \mathbf { d } . } \end{array}
$$

b.Solve the linear system

$$
\begin{array} { c } { { ( 1 - 2 i ) ( x _ { 1 } + i y _ { 1 } ) + ( 3 + 2 i ) ( x _ { 2 } + i y _ { 2 } ) = 5 + 2 i , } } \\ { { ( 2 + i ) ( x _ { 1 } + i y _ { 1 } ) + ( 4 + 3 i ) ( x _ { 2 } + i y _ { 2 } ) = 4 - i . } } \end{array}
$$

# 6.4 The Determinant of a Matrix

The determinant of a matrix provides existence and uniqueness results for linear systems having the same number of equations and unknowns.We will denote the determinant of a square matrix $A$ by det $A$ , but it is also common to use the notation $\vert A \vert$

# Definition 6.14

a.If $A = [ a ]$ is a $1 \times 1$ matrix, then det $A = a$

b.If $A$ is an $n \times n$ matrix, the minor $M _ { i j }$ is the determinant of the $( n - 1 ) \times ( n - 1 )$ submatrix of $A$ obtained by deleting the ith row and $j$ th column of the matrix $A$

c. The cofactor $A _ { i j }$ associated with $M _ { i j }$ is defined by $A _ { i j } = ( - 1 ) ^ { i + j } M _ { i j }$

d. The determinant of the $n \times n$ matrix $A$ ,when $n > 1$ , is given either by

$$
\operatorname* { d e t } A = \sum _ { j = 1 } ^ { n } a _ { i j } A _ { i j } = \sum _ { j = 1 } ^ { n } ( - 1 ) ^ { i + j } a _ { i j } M _ { i j } , \quad { \mathrm { f o r ~ a n y ~ } } i = 1 , 2 , \dots , n ,
$$

or by

$$
\operatorname* { d e t } A = \sum _ { i = 1 } ^ { n } a _ { i j } A _ { i j } = \sum _ { i = 1 } ^ { n } ( - 1 ) ^ { i + j } a _ { i j } M _ { i j } , \quad { \mathrm { f o r ~ a n y ~ } } j = 1 , 2 , \ldots , n .
$$

It can be shown (see Exercise 9) that to calculate the determinant of a general $n \times n$ matrix by this definition requires $O ( n ! )$ multiplications/divisions and additions/subtractions. Even for relatively small values of $\pmb { n }$ ,the number of calculations becomes unwieldy.

Although it appears that there are $2 n$ different definitions of det $A$ ,depending on which row or column is chosen,all definitions give the same numerical result. The flexibility in the definition is used in the following example. It is most convenient to compute det $A$ across the row or down the column with the most zeros.

Let

$$
A = \left[ { \begin{array} { r r r r } { 2 } & { - 1 } & { 3 } & { 0 } \\ { 4 } & { - 2 } & { 7 } & { 0 } \\ { - 3 } & { - 4 } & { 1 } & { 5 } \\ { 6 } & { - 6 } & { 8 } & { 0 } \end{array} } \right] .
$$

To compute det $\pmb { A }$ ,it is easiest to expand about the fourth column:

$$
\begin{array} { r } { A = a _ { 1 4 } A _ { 1 4 } + a _ { 2 4 } A _ { 2 4 } + a _ { 3 4 } A _ { 3 4 } + a _ { 4 4 } A _ { 4 4 } = 5 A _ { 3 4 } = - 5 M _ { 3 4 } . } \end{array}
$$

Eliminating the third row and the fourth column gives

$$
{ \begin{array} { r l } & { \operatorname* { d e t } A = - 5 \operatorname* { d e t } { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 3 } \\ { 4 } & { - 2 } & { 7 } \\ { 6 } & { - 6 } & { 8 } \end{array} \right] } } \\ & { \qquad = - 5 \left\{ 2 \operatorname* { d e t } { \left[ \begin{array} { l l } { - 2 } & { 7 } \\ { - 6 } & { 8 } \end{array} \right] } - ( - 1 ) \operatorname* { d e t } { \left[ \begin{array} { l l } { 4 } & { 7 } \\ { 6 } & { 8 } \end{array} \right] } + 3 \operatorname* { d e t } { \left[ \begin{array} { l l } { 4 } & { - 2 } \\ { 6 } & { - 6 } \end{array} \right] } \right\} = - 3 0 . } \end{array} }
$$

The determinant of a matrix can also be computed in Maple by the command det（A）;.

The following properties are useful in relating linear systems and Gaussian elimination to determinants. These are proved in any standard linear algebra text. (See, for example, [ND, pp. 200-201].)

Theorem 6.15 Suppose $A$ is an $n \times n$ matrix:

a. If any row or column of $\pmb { A }$ has only zero entries, then det $A = 0$   
$\mathbf { b _ { \delta } }$ If $A$ has two rows or two columns the same, then det $A = 0$   
$\pmb { \mathbb { c } } _ { \pmb { \cdot } }$ If $\tilde { A }$ is obtained from $\pmb { A }$ by the operation $( E _ { i } )  ( E _ { j } )$ ，with $i \neq j$ , then det $\tilde { A } =$ - det $A$ .   
d. If $\tilde { A }$ is obtained from $\pmb { A }$ by the operation $( \lambda E _ { i } ) \to ( E _ { i } )$ , then det $\tilde { A } = \lambda$ det $A$   
e. If $\tilde { A }$ is obtained from $\pmb { A }$ by the operation $( E _ { i } + \lambda E _ { j } )  ( E _ { i } )$ with $i \neq j$ , then det ${ \tilde { A } } = \operatorname* { d e t } A$   
f. If $\pmb { B }$ is also an $n \times n$ matrix, then det $A B = \operatorname* { d e t } A$ det $\pmb { B }$   
$\mathbf { g } .$ det $A ^ { t } = \operatorname* { d e t } A$   
h. When $A ^ { - 1 }$ exists,det $A ^ { - 1 } = ( \det A ) ^ { - 1 }$   
i. If $A$ is an upper triangular, lower triangular, or diagonal matrix,then det $A \ =$ $\textstyle \prod _ { i = 1 } ^ { n } a _ { i i }$

A matrix in triangular form has an easily calculated determinant, so computing the determinant of any matrix can be simplified by first reducing the matrix to triangular form, and then using part (i) of the theorem to find the determinant of the triangular matrix.

# EXAMPLE 2

Compute the determinant of the matrix

$$
A = \left[ { \begin{array} { r r r r } { 2 } & { 1 } & { - 1 } & { 1 } \\ { 1 } & { 1 } & { 0 } & { 3 } \\ { - 1 } & { 2 } & { 3 } & { - 1 } \\ { 3 } & { - 1 } & { - 1 } & { 2 } \end{array} } \right]
$$

using parts (b), $( \mathbf { d } )$ , and (e) of Theorem 6.15, doing the computations in Maple. Matrix A is defined by

$$
\mathtt { A } : = \operatorname* { m a t } \mathbf { r } \mathrm { i } \mathbf { x } ( 4 , 4 , [ 2 , 1 , - 1 , 1 , 1 , 1 , 0 , 3 , - 1 , 2 , 3 , - 1 , 3 , - 1 , - 1 , - 1 , 2 ] ) \ ;
$$

The sequence of operations in Table 6.2 produces the matrix

$$
A 8 = { \left[ \begin{array} { l l l l } { 1 } & { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { 0 } & { 1 } & { 1 } & { 5 } \\ { 0 } & { 0 } & { 3 } & { 1 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 3 } \end{array} \right] } .
$$

By part (i), det $A 8 = - 3 9$ ,so det $A = 3 9$

Table 6.2

<table><tr><td>Operation</td><td>Maple</td><td>Effect</td></tr><tr><td>E→E1</td><td>A1:= mulrow(A,1,0.5)</td><td>det A1 =  det A</td></tr><tr><td>E-E→E2</td><td>A2:= addrow(A1,1,2,-1)</td><td>det A2 = det A1 = ↓ det A</td></tr><tr><td>E+E→E</td><td>A3:= addrow(A2,1,3,1)</td><td>det A3 = det A2 =  det A</td></tr><tr><td>E4-3E→E4</td><td>A4:= addrow(A3,1,4,-3)</td><td>det A4 = det A3=  det A</td></tr><tr><td>2E→E2</td><td>A5:= mulrow(A,2,2)</td><td>det A5 = 2 det A4 = det A</td></tr><tr><td>E-E→E</td><td>A6:= addrow(A,2,3,-2.5)</td><td>det A6= det A5 = det A</td></tr><tr><td>E4+E→E4</td><td>A7:= addrow(A,2,4,2.5)</td><td>det A7 = det A6= det A</td></tr><tr><td>E←E4</td><td>A8:= swaprow(A,3,4)</td><td>det A8= - det A7= -det A</td></tr></table>

The key result relating nonsingularity, Gaussian elimination, linear systems, and determinants is that the following statements are equivalent.

# Theorem 6.16

The following statements are equivalent for any $n \times n$ matrix $A$ ：

a. The equation $\pmb { A } \mathbf { x } = \mathbf { 0 }$ has the unique solution $\mathbf { x } = \mathbf { 0 }$   
$\mathbf { b } .$ The system $\pmb { A } \mathbf { x } = \mathbf { b }$ has a unique solution for any $\pmb { n }$ -dimensional column vector b. c. The matrix $\pmb { A }$ is nonsingular; that is, $A ^ { - 1 }$ exists.   
d.det $A \neq 0$   
e. Gaussian elimination with row interchanges can be performed on the system $A \mathbf { x } = \mathbf { b }$ for any $_ n$ -dimensional column vector b.

# ExErcIsE SEt 6.4

1.Use Definition 6.14 to compute the determinants of the following matrices:

$\mathbf { a } . \quad \left[ { \begin{array} { r r r } { 1 } & { 2 } & { 0 } \\ { 2 } & { 1 } & { - 1 } \\ { 3 } & { 1 } & { 1 } \end{array} } \right]$ b.   
$\mathrm { ~ c ~ } \left[ \begin{array} { r r r r } { { 1 } } & { { 1 } } & { { - 1 } } & { { 1 } } \\ { { 1 } } & { { 2 } } & { { - 4 } } & { { - 2 } } \\ { { 2 } } & { { 1 } } & { { 1 } } & { { 5 } } \\ { { - 1 } } & { { 0 } } & { { - 2 } } & { { - 4 } } \end{array} \right]$ d.

2.Repeat Exercise 1 using the method of Example 2.

3.Compute det $A$ ,det $B$ ,det $A B$ , and det $B A$ for

$$
A = \left[ \begin{array} { c c c c } { 4 } & { 6 } & { 1 } & { - 1 } \\ { 2 } & { 1 } & { 0 } & { \frac { 1 } { 2 } } \\ { 3 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { - 1 } & { 1 } & { 1 } \end{array} \right] \quad \mathrm { a n d } \quad B = \left[ \begin{array} { c c c c } { 1 } & { 2 } & { 3 } & { 4 } \\ { 0 } & { 2 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 3 } & { 2 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} \right] .
$$

4.Let $A$ be a $3 \times 3$ matrix. Show that if $\tilde { A }$ is the matrix obtained from $A$ using any of the operations

$$
( E _ { 1 } )  ( E _ { 2 } ) , \quad ( E _ { 1 } )  ( E _ { 3 } ) , \quad { \mathrm { o r } } \quad ( E _ { 2 } )  ( E _ { 3 } ) ,
$$

then det $\tilde { A } = - \operatorname* { d e t } A$

5.Find all values of $\pmb { \alpha }$ that make the following matrix singular.

$$
A = \left[ { \begin{array} { r r r } { 1 } & { - 1 } & { \alpha } \\ { 2 } & { 2 } & { 1 } \\ { 0 } & { \alpha } & { - { \frac { 3 } { 2 } } } \end{array} } \right] .
$$

6.Find all values of $\pmb { \alpha }$ that make the following matrix singular.

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 1 } & { \alpha } & { 1 } \\ { 2 } & { \alpha } & { - 1 } \end{array} } \right] .
$$

7.Find all values of $\pmb { \alpha }$ so that the following linear system has no solutions.

$$
\begin{array} { r } { 2 x _ { 1 } - x _ { 2 } + 3 x _ { 3 } = 5 , } \\ { 4 x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 6 , } \\ { - 2 x _ { 1 } + \alpha x _ { 2 } + 3 x _ { 3 } = 4 . } \end{array}
$$

8.Find all values of $\pmb { \alpha }$ so that the following linear system has an infinite number of solutions.

$$
\begin{array} { r } { 2 x _ { 1 } - x _ { 2 } + 3 x _ { 3 } = 5 , } \\ { 4 x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 6 , } \\ { - 2 x _ { 1 } + \alpha x _ { 2 } + 3 x _ { 3 } = 1 . } \end{array}
$$

9.Use mathematical induction to show that when $n > 1$ , the evaluation of the determinant of a $n \times n$ miin $n ! \sum _ { k = 1 } ^ { n - 1 } \frac { 1 } { k ! }$ multiplicationsrdivisiosad $n ! - 1$ additions/subtractions.

10.Prove that $A B$ is nonsingular if and only if both $A$ and $B$ are nonsingular.

11.The solution by Cramer's rule to the linear system

$$
\begin{array} { r l } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + a _ { 1 3 } x _ { 3 } = b _ { 1 } , } \\ & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + a _ { 2 3 } x _ { 3 } = b _ { 2 } , } \\ & { a _ { 3 1 } x _ { 1 } + a _ { 3 2 } x _ { 2 } + a _ { 3 3 } x _ { 3 } = b _ { 3 } , } \end{array}
$$

has

$$
x _ { 1 } = { \frac { 1 } { D } } \operatorname* { d e t } { \left[ \begin{array} { l l l } { b _ { 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { b _ { 2 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { b _ { 3 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } \equiv { \frac { D _ { 1 } } { D } } ,
$$

$$
x _ { 2 } = \frac { 1 } { D } { \sf d e t } \left[ \begin{array} { l l l } { a _ { 1 1 } } & { b _ { 1 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { b _ { 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { b _ { 3 } } & { a _ { 3 3 } } \end{array} \right] \equiv \frac { D _ { 2 } } { D } ,
$$

and

$$
x _ { 3 } = \frac { 1 } { D } \det \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { b _ { 1 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { b _ { 2 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { b _ { 3 } } \end{array} \right] \equiv \frac { D _ { 3 } } { D } ,
$$

where

$$
D = \operatorname* { d e t } { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } ~ .
$$

a. Find the solution to the linear system

$$
\begin{array} { r c l } { { 2 x _ { 1 } + } } & { { 3 x _ { 2 } - } } & { { x _ { 3 } = 4 , } } \\ { { } } & { { } } & { { x _ { 1 } - } } & { { 2 x _ { 2 } + } } & { { x _ { 3 } = 6 , } } \\ { { } } & { { } } & { { x _ { 1 } - 1 2 x _ { 2 } + 5 x _ { 3 } = 1 0 , } } \end{array}
$$

by Cramer's rule.

b. Show that the linear system

$$
\begin{array} { r l } { { 2 } x _ { 1 } + } & { 3 x _ { 2 } - } \\ { \quad x _ { 1 } - } & { 2 x _ { 2 } + } \\ { \quad - x _ { 1 } - } & { 1 2 x _ { 2 } + 5 x _ { 3 } = 9 } \end{array}
$$

does not have a solution. Compute $D _ { 1 } , D _ { 2 }$ ,and $D _ { 3 }$ ·

c. Show that the linear system

$$
\begin{array} { r } { 2 x _ { 1 } + ~ 3 x _ { 2 } - ~ x _ { 3 } = 4 , } \\ { x _ { 1 } - ~ 2 x _ { 2 } + ~ x _ { 3 } = 6 , } \\ { - x _ { 1 } - 1 2 x _ { 2 } + 5 x _ { 3 } = 1 0 } \end{array}
$$

has an infinite number of solutions. Compute $D _ { 1 } , D _ { 2 }$ ,and $D _ { 3 }$ ·

d.Prove that if a $3 \times 3$ linear system with $D = 0$ has solutions, then $D _ { 1 } = D _ { 2 } = D _ { 3 } = 0$

e. Determine the number of multiplications/divisions and additions/subtractions required for Cramer's rule on a $3 \times 3$ system.

12.a.Generalize Cramer's rule to an $n \times n$ linear system. b. Use the result in Exercise 9 to determine the number of multiplications/divisions and additions/subtractions required for Cramer's rule on an $n \times n$ system.

# 6.5 Matrix Factorization

Gaussian elimination is the principal tool in the direct solution of linear systems of equations,so it should be no surprise that it appears in other guises.In this section we will see that the steps used to solve a system of the form $\pmb { A } \mathbf { x } = \mathbf { b }$ can be used to factor a matrix. The factorization is particularly useful when it has the form $A = L U$ ,where $L$ is lower triangular and $U$ is upper triangular. Although not all matrices have this type of representation, many do that occur frequently in the study of numerical techniques.

In Section 6.1 we found that Gaussian elimination applied to an arbitrary linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ requires $O ( n ^ { 3 } / 3 )$ arithmetic operations to determine x. If A has been factored into the triangular form $A = L U$ , then we can solve for $\mathbf { x }$ more easily by using a two-step process. First we let $\mathbf { y } = U \mathbf { x }$ and solve the system $L \mathbf { y } = \mathbf { b }$ for $\mathbf { y }$ . Since $L$ is triangular, determining $\mathbf { y }$ from this equation requires only $O ( n ^ { 2 } )$ operations. Once $\mathbf { y }$ is known, the upper triangular system $U \mathbf { X } = \mathbf { y }$ requires only an additional $O ( n ^ { 2 } )$ operations to determine the solution $\mathbf { x }$ . This fact means that the number of operations needed to solve the system $A \mathbf { x } = \mathbf { b }$ is reduced from $O ( n ^ { 3 } / 3 )$ to $O ( 2 n ^ { 2 } )$ . In systems greater than 100 by 100, this can reduce the amount of calculation by more than $9 7 \%$ . Not surprisingly, the reductions resulting from matrix factorization do not come free; determining the specific matrices $L$ and $U$ requires $O ( n ^ { 3 } / 3 )$ operations.But once the factorization is determined,a system involving the matrix $A$ and any vector b can be solved in this simplified manner.

To examine which matrices have an $L U$ factorization and to find how it is determined, first suppose that Gaussian elimination can be performed on the system $A \mathbf { x } = \mathbf { b }$ without row interchanges. With the notation in Section 6.1, this is equivalent to having nonzero pivot elements $\dot { a } _ { i i } ^ { ( i ) }$ ,for each $i = 1 , 2 , \dots , n$

The first step in the Gaussian elimination process consists of performing,for each $j = 2 , 3 , \dots , n$ , the operations

$$
( E _ { j } - m _ { j , 1 } E _ { 1 } )  ( E _ { j } ) , \quad \mathrm { w h e r e } \quad m _ { j , 1 } = \frac { a _ { j 1 } ^ { ( 1 ) } } { a _ { 1 1 } ^ { ( 1 ) } } .
$$

These operations transform the system into one in which all the entries in the first column below the diagonal are zero.

The system of operations in (6.8) can be viewed in another way. It is simultaneously accomplished by multiplying the original matrix $A$ on the left by the matrix

$$
M ^ { ( 1 ) } = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 . \dots \dots \dots \dots } } & { { 0 } } \\ { { - m _ { 2 1 } } } & { { 1 . } } & { { . } } & { { \vdots } } \\ { { \vdots } } & { { 0 . } } & { { . } } & { { . } } \\ { { \vdots } } & { { \vdots } } & { { . } } & { { . } } \\ { { - \dot { m _ { n 1 } } } } & { { \dot { 0 } . } } & { { . . . . \vdots } } & { { 0 } } \end{array} \right] .
$$

This is called the first Gaussian transformation matrix. We denote the product of this matrix with $\boldsymbol { A } ^ { ( 1 ) } \equiv \boldsymbol { A }$ by $A ^ { ( 2 ) }$ and with b by $\mathbf { b } ^ { ( 2 ) }$ ，so

$$
{ \cal A } ^ { ( 2 ) } { \bf x } = { \cal M } ^ { ( 1 ) } { \cal A } { \bf x } = { \cal M } ^ { ( 1 ) } { \bf b } = { \bf b } ^ { ( 2 ) } .
$$

In a similar manner we construct $M ^ { ( 2 ) }$ ,the dentity matrix with the entries below the diagonal in the second column replaced by the negatives of the multipliers

$$
m _ { j , 2 } = \frac { a _ { j 2 } ^ { ( 2 ) } } { a _ { 2 2 } ^ { ( 2 ) } } .
$$

The product of this matrix with $A ^ { ( 2 ) }$ has zeros below the diagonal in the first two columns, and we let

$$
A ^ { ( 3 ) } \mathbf { x } = M ^ { ( 2 ) } A ^ { ( 2 ) } \mathbf { x } = M ^ { ( 2 ) } M ^ { ( 1 ) } A \mathbf { x } = M ^ { ( 2 ) } M ^ { ( 1 ) } \mathbf { b } = \mathbf { b } ^ { ( 3 ) } .
$$

In general, with ${ \pmb A } ^ { ( k ) } { \bf x } = { \bf b } ^ { ( k ) }$ already formed, multiply by the kth Gaussian transformation matrix

$$
M ^ { ( k ) } = \left[ \begin{array} { l l l l l l } { 1 _ { { - } , } } & { 0 _ { { + } , } } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 _ { { - } , } } & { \dots } & { } & { } & { } & { } & { } \\ { 0 _ { { - } , } } & { \dots } & { \dots } & { } & { } & { } & { } \\ { \vdots } & { \ddots } & { \dots } & { } & { } & { } & { } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { } & { } & { } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { } & { } & { } \\ { \vdots } & { \vdots } & { { - } } & { \ddots } & { \ddots } & { } & { } \\ { \vdots } & { \vdots } & { { - } } & { { - } } & { \dots } & { \ddots } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \dots } & { \ddots } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \dots } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \ddots } \end{array} \right] ,
$$

to obtain

$$
\begin{array} { r } { \boldsymbol { A } ^ { ( k + 1 ) } \mathbf { x } = \boldsymbol { M } ^ { ( k ) } \boldsymbol { A } ^ { ( k ) } \mathbf { x } = \boldsymbol { M } ^ { ( k ) } \cdot \cdot \cdot \boldsymbol { \cdot } \boldsymbol { M } ^ { ( 1 ) } \boldsymbol { A } \mathbf { x } = \boldsymbol { M } ^ { ( k ) } \mathbf { b } ^ { ( k ) } = \mathbf { b } ^ { ( k + 1 ) } = \boldsymbol { M } ^ { ( k ) } \cdot \cdot \cdot \boldsymbol { \cdot } \boldsymbol { M } ^ { ( 1 ) } \mathbf { b } . } \end{array}
$$

The process ends with the formation of $A ^ { ( n ) } \mathbf { x } = \mathbf { b } ^ { ( n ) }$ ， where $A ^ { ( n ) }$ is the upper triangular matrix

$$
A ^ { ( n ) } = \left[ \begin{array} { c c c c c c } { a _ { 1 1 } ^ { ( 1 ) } } & { a _ { 1 2 } ^ { ( 1 ) } . . . . . . . . . a _ { 1 n } ^ { ( 1 ) } } \\ { \vdots } & { a _ { 2 2 } ^ { ( 2 ) } } & { . . . } & { . } \\ { . . . } & { . . } & { . } & { . } \\ { . } & { . . . } & { . . } & { a _ { n - 1 , n } ^ { ( n - 1 ) } } \\ { 0 . . . . . . . . . } & { . } & { a _ { n n } ^ { ( n ) } } \end{array} \right] ,
$$

given by

$$
\boldsymbol { A } ^ { ( n ) } = \boldsymbol { M } ^ { ( n - 1 ) } \boldsymbol { M } ^ { ( n - 2 ) } \cdot \cdot \cdot \boldsymbol { M } ^ { ( 1 ) } \boldsymbol { A } .
$$

This process forms the $U = A ^ { ( n ) }$ portion of the matrix factorization $A \ = \ L U$ .To determine the complementary lower triangular matrix $L$ ,first recall the multiplication of ${ \cal A } ^ { ( k ) } { \bf X } = { \bf b } ^ { ( k ) }$ by the Gaussian transformation of $M ^ { ( k ) }$ used to obtain (6.9):

$$
A ^ { ( k + 1 ) } \mathbf { x } = M ^ { ( k ) } A ^ { ( k ) } \mathbf { x } = M ^ { ( k ) } \mathbf { b } ^ { ( k ) } = \mathbf { b } ^ { ( k + 1 ) } ,
$$

where $M ^ { ( k ) }$ generates the row operations

$$
( E _ { j } - m _ { j , k } E _ { k } ) \to ( E _ { j } ) , \quad { \mathrm { f o r ~ } } j = k + 1 , \ldots , n .
$$

To reverse the effects of this transformation and return to $A ^ { ( k ) }$ requires that the operations $( E _ { j } + m _ { j , k } E _ { k } )  ( E _ { j } )$ be performed for each $j = k + 1 , \dots , n$ . This is equivalent to multiplying by the inverse of the matrix $M ^ { ( k ) }$ , the matrix

$$
L ^ { ( k ) } = [ M ^ { ( k ) } ] ^ { - 1 } = \left[ \begin{array} { l l l l l l l l } { 1 . } & { 0 . \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 } & { \dots } & { \dots } & { } & { } & { } & { } \\ { 0 } & { \dots } & { \dots } & { } & { } & { } & { } \\ { \vdots } & { \ddots } & { \dots } & { \dots } & { } & { } & { } & { } \\ { \vdots } & { \ddots } & { \ddots } & { \dots } & { } & { } & { } & { } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \dots } & { } & { } & { } \\ { \vdots } & { } & { \vdots } & { \ddots } & { \ddots } & { \dots } & { } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { \ddots } & { \ddots } & { \dots } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { } { \ddots } & { \dots } & { \ddots } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { } { \vdots } & { \ddots } & { \dots } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { } { \vdots } & { \ddots } & { \dots } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { } { \vdots } & { \ddots } & { \dots } & { } \\ { \vdots } & { } { \vdots } & { } { \vdots } & { } { \vdots } & { \ddots } & { \dots } & { } \\ { 0 } & { \dots } & { \dots } & { \ddots } & { \vdots } & { } \end{array} \right] .
$$

The lower-triangular matrix $L$ in the factorization of $A$ is the product of the matrices $L ^ { ( k ) }$ ：

$$
L = L ^ { ( 1 ) } L ^ { ( 2 ) } \cdots L ^ { ( n - 1 ) } = \left[ \begin{array} { c c c } { { 1 } } & { { 0      ; \cdots \cdots \cdots } } & { { 0 } } \\ { { m _ { 2 1 } } } & { { 1 \cdots \cdots \cdots } } & { { \vdots } } \\ { { \cdots \cdots \cdot } } & { { \cdot \ddots \underbrace { \quad \cdot } } } & { { 0 } } \\ { { \dot { m _ { n 1 } } \cdot \cdots \cdots \cdot } } & { { m _ { n , n - 1 } \cdot } } & { { 1 } } \end{array} \right] ,
$$

since the product of $L$ with the upper-triangular matrix $U = M ^ { ( n - 1 ) } \cdot \cdot \cdot M ^ { ( 2 ) } M ^ { ( 1 ) } A$ gives

$$
\begin{array} { r l } { { } } & { { L U = L ^ { ( 1 ) } L ^ { ( 2 ) } \cdot \cdot \cdot L ^ { ( n - 3 ) } L ^ { ( n - 2 ) } L ^ { ( n - 1 ) } \cdot M ^ { ( n - 1 ) } M ^ { ( n - 2 ) } M ^ { ( n - 3 ) } \cdot \cdot \cdot M ^ { ( 2 ) } M ^ { ( 1 ) } A } } \\ { { } } & { { } } \\ { { \ } } & { { = [ M ^ { ( 1 ) } ] ^ { - 1 } [ M ^ { ( 2 ) } ] ^ { - 1 } \cdot \cdot \cdot [ M ^ { ( n - 2 ) } ] ^ { - 1 } [ M ^ { ( n - 1 ) } ] ^ { - 1 } \cdot M ^ { ( n - 1 ) } M ^ { ( n - 2 ) } \cdot \cdot \cdot M ^ { ( 2 ) } M ^ { ( 1 ) } A = } } \end{array}
$$

Theorem 6.17 follows from these observations.

# Theorem 6.17

If Gaussian elimination can be performed on the linear system $A \mathbf { x } = \mathbf { b }$ without row interchanges,then the matrix $A$ can be factored into the product of a lower-triangular matrix $L$ and an upper-triangular matrix $U$ ，

$$
A = L U ,
$$

where $m _ { j i } = a _ { j i } ^ { ( i ) } / a _ { i i } ^ { ( i ) }$

$$
U = \left[ \begin{array} { c c c c c } { a _ { 1 1 } ^ { ( 1 ) } } & { a _ { 1 2 } ^ { ( 1 ) } . . . . . . . . . a _ { 1 n } ^ { ( 1 ) } } \\ { 0 } & { a _ { 2 2 } ^ { ( 2 ) } . . . . } & { . . } \\ { \vdots } & { . . . } & { . . } \\ { \vdots } & { . . . . } & { . . } & { a _ { n - 1 , n } ^ { ( n - 1 ) } } \\ { 0 } & { . . . . . . . . . \cdot 0 } & { a _ { n n } ^ { ( n ) } } \end{array} \right] , \quad \mathrm { a n d } \quad L = \left[ \begin{array} { c c c c c } { 1 } & { 0 _ { ! } . . . } & { . . . . } & { . . . } \\ { m _ { 2 1 } } & { 1 . . . } & { . . . } & { . . } \\ { . . . } & { . . . } & { . . . } & { . } \\ { m _ { n 1 } ^ { ( 1 ) } . . . . } & { . . . } & { . . } & { 1 } \end{array} \right] .
$$

# EXAMPLE 1 The linear system

$$
\begin{array} { r l } { x _ { 1 } + { \ x } _ { 2 } } & { { } + 3 x _ { 4 } = { \ } 4 , } \\ { 2 x _ { 1 } + { \ x } _ { 2 } - { \ x } _ { 3 } + { \ x } _ { 4 } = { \ } 1 , } \\ { 3 x _ { 1 } - { \ x } _ { 2 } - { \ x } _ { 3 } + 2 x _ { 4 } = - 3 , } \\ { - x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } - { \ x } _ { 4 } = { \ } 4 } \end{array}
$$

was considered in Section 6.1. The sequence of operations $( E _ { 2 } - 2 E _ { \mathrm { { i } } } )  ( E _ { 2 } )$ ， $( E _ { 3 } \mathrm { ~ - ~ }$ $3 E _ { 1 } )  ( E _ { 3 } ) , ( E _ { 4 } - ( - 1 ) E _ { 1 } )  ( E _ { 4 } ) , ( E _ { 3 } - 4 E _ { 2 } )  ( E _ { 3 }$ ， $( E _ { 4 } - ( - 3 ) E _ { 2 } )  ( E _ { 4 } )$ converts the system to the triangular system

$$
\begin{array} { r l r } { x _ { 1 } + x _ { 2 } } & { } & { + \ 3 x _ { 4 } = \quad 4 , } \\ { - x _ { 2 } - \ x _ { 3 } - \ 5 x _ { 4 } = \ - 7 , } & { } & \\ { 3 x _ { 3 } + 1 3 x _ { 4 } = \quad 1 3 , } & { } & \\ { - \ 1 3 x _ { 4 } = - 1 3 . } & { } & \end{array}
$$

The multipliers $m _ { i j }$ and the upper triangular matrix produce the factorization

$$
= { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { 0 } & { 3 } \\ { 2 } & { 1 } & { - 1 } & { 1 } \\ { 3 } & { - 1 } & { - 1 } & { 2 } \\ { - 1 } & { 2 } & { 3 } & { - 1 } \end{array} \right] } = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 3 } & { 4 } & { 1 } & { 0 } \\ { - 1 } & { - 3 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { - 1 } & { - 1 } & { - 5 } \\ { 0 } & { 0 } & { 3 } & { 1 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 3 } \end{array} \right] } = L U .
$$

This factorization permits us to easily solve any system involving the matrix A.For example, to solve

$$
\mathbf { A } \mathbf { x } = L U \mathbf { x } = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 3 } & { 4 } & { 1 } & { 0 } \\ { - 1 } & { - 3 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { - 1 } & { - 1 } & { - 5 } \\ { 0 } & { 0 } & { 3 } & { 1 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 3 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right] } = { \left[ \begin{array} { l } { 8 } \\ { 7 } \\ { 1 4 } \\ { - 7 } \end{array} \right] } ,
$$

we first introduce the substitution $\mathbf { y } = U \mathbf { x }$ Then $\pmb { L } \pmb { y } = \pmb { \ b }$ ; that is,