$$
\begin{array} { r l } & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) W _ { k - 1 } W _ { k - 1 } ^ { T } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { ~ + \Gamma ( t _ { k } , t _ { k - 1 } ) V _ { k } V _ { k } ^ { T } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { ~ = \overline { { W } } _ { k } \overline { { W } } _ { k } ^ { T } } \end{array}
$$

where

$$
Q _ { k } = V _ { k } V _ { k } ^ { T } .
$$

A Givens algorithm to compute an upper (or lower) triangular matrix, $\overline { { W } } _ { k }$ , is given in Section 5.8, Eqs. (5.8.6) through (5.8.13). If there is no process noise, set $V _ { k } = 0$ in this algorithm. Methods for maintaining the measurement update in triangular form are discussed next.

# Triangular Square Root Measurement Update

The algorithm for performing the measurement update on the state error covariance matrix square root, $\overline { W }$ , can be expressed as

$$
W = { \overline { { W } } } \widetilde { A } .
$$

If $\overline { W }$ is lower triangular and if $\widetilde { A }$ is lower triangular, then $W$ will be lower triangular, and the computational process expressed in Eq. (5.7.19) will be conducted in a more efficient manner. Choose $\widetilde { A }$ as the solution to

$$
\widetilde { A } \widetilde { A } ^ { T } = [ I - \alpha \widetilde { F } \widetilde { F } ^ { T } ] ,
$$

and require that $\widetilde { A }$ be lower triangular. $\widetilde { A }$ will contain $( n ^ { 2 } + n ) / 2$ unknowns. Since the right-hand side is symmetric, Eq. (5.7.20) contains $( n ^ { 2 } + n ) / 2$ unique equations for the $( n ^ { 2 } + n ) / 2$ unknowns. By analytically expanding the results we can determine the expressions for $\tilde { a } _ { i j }$ , the elements of $\widetilde { A }$ . The procedure used is as follows.

If $\overline { W }$ is lower triangular, the equation

$$
\widetilde { \boldsymbol { F } } = \overline { { \boldsymbol { W } } } ^ { T } \boldsymbol { H } ^ { T }
$$

can be expressed as

$$
\left[ \begin{array} { c } { \widetilde F _ { 1 } } \\ { \vdots } \\ { \widetilde F _ { n } } \end{array} \right] = \left[ \begin{array} { c c c c } { \overline { { W } } _ { 1 1 } } & { \cdots \cdots \cdots \bullet } & { \overline { { W } } _ { n 1 } } \\ { \overline { { W } } _ { 2 2 } \cdots \cdots \cdots \bullet } & { \overline { { W } } _ { n 2 } } \\ { \ddots } & { \vdots } \\ { \cal O } & { \overbrace { W } _ { n n } } \end{array} \right] \left[ \begin{array} { c } { H _ { 1 } } \\ { \vdots } \\ { H _ { n } } \end{array} \right]
$$

$$
= \left[ \begin{array} { l } { \displaystyle { \sum _ { j = 1 } ^ { n } \overline { { W } } _ { j 1 } H _ { j } } } \\ { \quad } \\ { \quad } \\ { \overline { { W } } _ { n n } H _ { n } } \end{array} \right]
$$

or, for the general $i ^ { \mathrm { t h } }$ element,

$$
\widetilde { F } _ { i } = \sum _ { j = i } ^ { n } \overline { { { W } } } _ { j i } H _ { j } , \quad i = 1 , \ldots , n .
$$

From Eq. (5.7.20), the matrix $B$ can be defined as

$$
B = \widetilde { A } \widetilde { A } ^ { T } = I - \alpha \widetilde { F } \widetilde { F } ^ { T } .
$$

The general $i j$ element of the product matrix in Eq. (5.7.23) can be expressed as

$$
B _ { i j } = \sum _ { k = 1 } ^ { j } a _ { i k } a _ { j k } = \delta _ { i j } - \alpha \widetilde { F } _ { i } \widetilde { F } _ { j } , i = 1 , \dots , n ; j = 1 , \dots , i .
$$

From Eq. (5.7.24), it follows that

$$
\begin{array} { r l } & { B _ { 1 1 } = a _ { 1 1 } ^ { 2 } = 1 - ( \tilde { F } _ { 1 } ^ { 2 } \alpha ) } \\ & { B _ { 2 1 } = a _ { 2 1 } a _ { 1 1 } = - ( \tilde { F } _ { 2 } \tilde { F } _ { 1 } \alpha ) } \\ & { B _ { 2 2 } = a _ { 2 1 } ^ { 2 } + a _ { 2 2 } ^ { 2 } = 1 - ( \tilde { F } _ { 2 } ^ { 2 } \alpha ) } \\ & { B _ { 3 1 } = a _ { 3 1 } a _ { 1 1 } = - ( \tilde { F } _ { 3 } \tilde { F } _ { 1 } \alpha ) } \\ & { B _ { 3 2 } = a _ { 3 1 } a _ { 2 1 } + a _ { 3 2 } a _ { 2 2 } = - ( \tilde { F } _ { 3 } \tilde { F } _ { 2 } \alpha ) } \\ & { B _ { 3 3 } = a _ { 3 1 } ^ { 2 } + a _ { 3 2 } ^ { 2 } + a _ { 3 3 } ^ { 2 } = 1 - ( \tilde { F } _ { 3 } ^ { 2 } \alpha ) } \\ & { B _ { 4 1 } = a _ { 4 1 } a _ { 1 1 } = - ( F _ { 4 } F _ { 1 } \alpha ) . } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

If the definit ion

$$
\beta _ { i } = \frac { 1 } { \alpha } - \sum _ { j = 1 } ^ { i - 1 } \widetilde { F } _ { j } ^ { 2 } = R + \sum _ { j = i } ^ { n } \widetilde { F } _ { j } ^ { 2 } ,
$$

where

$$
\frac { 1 } { \alpha } = R + \sum _ { j = 1 } ^ { n } \widetilde { F } _ { j } ^ { 2 }
$$

is used, then

$$
\beta _ { i - 1 } = \beta _ { i } + \widetilde { F } _ { i - 1 } ^ { 2 } i = n + 1 , \ldots , 2
$$

where $\beta _ { i }$ satisfies the conditions

$$
\begin{array} { r } { \beta _ { n + 1 } = R , \beta _ { 1 } = \frac { 1 } { \alpha } . } \end{array}
$$

If Eq. (5.7.25) are solved recursively, starting with $a _ { 1 1 }$ , the solution can be expressed as

$$
a _ { i i } = \sqrt { \beta _ { i + 1 } / \beta _ { i } }
$$

$$
a _ { i j } = - \widetilde { F } _ { i } \widetilde { F } _ { j } / \sqrt { \beta _ { j + 1 } \beta _ { j } } \qquad \begin{array} { l l } { i = 1 , \dots , n } \\ { j = 1 , \dots , i - 1 . } \end{array}
$$

Once the elements of $\widetilde { A }$ have been computed, the elements of Eq. (5.7.19) can be expressed as follows:

$$
W _ { i j } = \sum _ { k = j } ^ { i } \overline { { { W } } } _ { i k } a _ { k j } \begin{array} { l } { i = 1 , \ldots , n } \\ { j = 1 , \ldots , i . } \end{array}
$$

The algorithm for the state estimate with a lower triangular square root covariance update is:

Given: $\overline { { W } } , H , R , \overline { { \mathbf { x } } }$ , and $y$ , where $\overline { W }$ is lower triangular Compute:

$$
\begin{array} { l } { { \displaystyle { 1 . \widetilde { F } _ { i } = \sum _ { j = 1 } ^ { n } \overline { { { W } } } _ { j i } H _ { j } } \qquad i = 1 , \ldots , n } } \\ { { \mathrm { } } } \\ { { \displaystyle { 2 . \beta _ { n + 1 } = R } } } \\ { { \beta _ { j } = \beta _ { j + 1 } + \widetilde { F } _ { j } ^ { 2 } \qquad j = n , \ldots , 1 } } \\ { { \beta _ { 1 } = 1 / \tilde { \alpha } } } \end{array}
$$

$$
\begin{array} { c c } { { 3 . d _ { i } = 1 / \sqrt { \beta _ { i + 1 } \beta _ { i } } \qquad } } & { { i = 1 , \ldots , n } } \\ { { a _ { i i } = \beta _ { i + 1 } d _ { i } \qquad } } & { { } } \\ { { a _ { i j } = - \widetilde { F } _ { i } \widetilde { F } _ { j } d _ { j } \qquad } } & { { j = 1 , \ldots , i - 1 } } \end{array}
$$

$$
4 . W _ { i j } = \sum _ { k = j } ^ { i } { \overline { { W } } } _ { i k } a _ { k j } \qquad i = 1 , \dots , n
$$

$$
5 . K _ { i } = \alpha ( \sum _ { j = 1 } ^ { i } \overline { { { W } } } _ { i j } \widetilde { F } _ { j } ) i = 1 , \ldots , n
$$

$$
6 . { \hat { \mathbf { x } } } _ { i } = { \overline { { \mathbf { x } } } } + K ( y - H { \overline { { \mathbf { x } } } } ) .
$$

If $\mathbf { y }$ is a vector of observations, this procedure must be repeated for each element of $\mathbf { y }$ .

The previous algorithm yields a lower triangular square root factorization of the measurement update error covariance matrix. An upper triangularization also can be used. The algorithm for this was developed by Carlson (1973). The version presented here is due to Bierman (1977) and is a slightly modified version of Carlson’s algorithm to enhance accuracy.

Given: $\overline { W }$ , $H , R , { \overline { { \mathbf { x } } } }$ , and $y$ , where $\overline { W }$ is upper triangular

Compute:

$$
\begin{array} { r l } & { 1 . \widetilde { F } = \overline { { W } } ^ { T } H ^ { T } } \\ & { \beta _ { o } = R , K _ { 2 } ^ { T } = \left[ \overline { { W } } _ { 1 1 } \widetilde { F } _ { 1 } , \overbrace { 0 , 0 , . . . 0 } ^ { n - 1 } \right] } \end{array}
$$

$$
\begin{array} { r l } & { 2 . \beta _ { j } = \beta _ { j - 1 } + \widetilde { F } _ { j } ^ { 2 } } \\ & { 3 . d _ { j } = ( \beta _ { j - 1 } / \beta _ { j } ) ^ { 1 / 2 } } \\ & { 4 . \gamma _ { j } = \widetilde { F } _ { j } / ( \beta _ { j } d _ { j } ) } \\ & { 5 . W _ { j j } = \overline { { W } } _ { j j } d _ { j } } \\ & { 6 . W _ { i j } = \overline { { W } } _ { i j } d _ { j } - \gamma _ { j } K _ { j } ( i ) } \\ & { 7 . K _ { j + 1 } ( i ) = K _ { j } ( i ) + \widetilde { F } _ { j } \widetilde { W } _ { i j } } \\ & { 8 . K = K _ { n + 1 } / \beta _ { n } } \\ & { 9 . \tilde { \kappa } = \overline { { \mathbf { X } } } + K ( y - H \mathbf { X } ) . } \end{array}
$$

$$
\begin{array} { l } { i = 1 , \dots j - 1 } \\ { \qquad } \\ { i = 1 , \dots j } \end{array}
$$

Although at first glance it does not seem to matter whether one uses an upper or lower triangular form for $W$ , Carlson (1973) points out that the time update for the upper triangular form is computationally more efficient. This can be seen by partitioning the state vector such that

$$
\begin{array} { r } { \mathbf { x } = \left[ \begin{array} { l } { \mathbf { x } _ { 1 } } \\ { \mathbf { x } _ { 2 } } \end{array} \right] , } \end{array}
$$

where $\mathbf { x } _ { 1 }$ contains the dynamical parameters such as position and velocity and $\mathbf { x } _ { 2 }$ contains constants such as gravity coefficients or time-varying quantities such as gas leaks that affect the elements of $\mathbf { x } _ { 1 }$ but are not affected by $\mathbf { x } _ { 1 }$ . Hence, the state transition matrix for $\mathbf { x }$ can be partitioned as

$$
\Phi = \left[ { \Phi _ { 1 1 } } \Phi _ { 1 2 } \right] ,
$$

where $\Phi _ { 1 1 }$ is a dense matrix, $\Phi _ { 1 2 }$ may contain some zeros, and $\Phi _ { 2 2 }$ is typically diagonal. When performing the time update, if $W$ is upper triangular, only the upper left partition of the product $\overline { { W } } = \Phi W$ becomes nontriangular and requires retriangularization.

Recall that these algorithms are designed to process the observations (acutally observation deviations) as scalars. Hence, if $\mathbf { y }$ is a vector the elements of $\mathbf { y }$ must be processed one at a time. We assume that the observations are uncorrelated so that $R$ is a diagonal matrix.

If $R$ is not a diagonal matrix, that is, the observation errors are correlated, we can perform a whitening and decorrelation transformation given by Bierman (1977), and described next.

Given a set of observations

$$
\mathbf { y } - H \mathbf { x } = { \boldsymbol { \epsilon } } ,
$$

where

$$
\begin{array} { r } { E [ \epsilon ] = 0 } \\ { E [ \epsilon \epsilon ^ { T } ] = R } \end{array}
$$

and $R$ is not diagonal but is positive definit e. Compute the triangular square root of $R$

$$
R = V V ^ { T } .
$$

The Cholesky algorithm may be used to ensure that $V$ is triangular. Next multiply Eq. (5.7.34) by $V ^ { - 1 }$

$$
V ^ { - 1 } \mathbf { y } = V ^ { - 1 } H \mathbf { x } + V ^ { - 1 } \boldsymbol \epsilon
$$

let

$$
\tilde { \mathbf { y } } = V ^ { - 1 } \mathbf { y } , \tilde { H } = V ^ { - 1 } H , \tilde { \epsilon } = V ^ { - 1 } \epsilon
$$

then

$$
\tilde { \mathbf { y } } = \widetilde { H } x + \tilde { \mathbf { \epsilon } }
$$

It is easily shown that $\widetilde { \epsilon }$ has zero mean and unit variance,

$$
\begin{array} { r } { \boldsymbol { E } [ \tilde { \epsilon } ] = V ^ { - 1 } \boldsymbol { E } [ \epsilon ] = 0 \qquad } \\ { E [ \tilde { \epsilon } \tilde { \epsilon } ^ { T } ] = V ^ { - 1 } \boldsymbol { E } [ \epsilon \epsilon ^ { T } ] V ^ { - T } = V ^ { - 1 } R V ^ { - T } = I } \end{array}
$$

Hence, we would process the observations, $\tilde { \mathbf { y } }$ , instead of $\mathbf { y }$ .

# 5.7.2 SQUARE ROOT FREE MEASUREMENT UPDATE ALGORITHMS

The square root operations in the Potter and Triangular algorithms shown earlier lead to increased computational load. Square root free equivalents of these algorithms can be used to obtain enhanced computational performance. A comprehensive discussion of these square root free algorithms is given by Thornton (1976) and Bierman (1977).

A square root free algorithm, known as the $U \mathcal { D }$ covariance factorization, developed by Bierman and Thornton is described next. Let

$$
{ \cal P } = U { \cal D } U ^ { T }
$$

where $U$ is unit upper triangular and $D$ is diagonal. Substituting Eq. (5.7.39) into the expression for the covariance matrix update

$$
P = [ I - K H ] \overline { { P } }
$$

and restricting attention to the scalar observation case leads to the following expression:

$$
U D U ^ { T } = \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } ~ - \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } H ^ { T } \alpha H \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T }
$$

where

$$
\alpha = ( H \overline { { { P } } } H ^ { T } + R ) ^ { - 1 } = \big ( H \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } H ^ { T } + R \big ) ^ { - 1 } .
$$

Now, by factoring, Eq. (5.7.41) can be expressed as follows:

$$
\boldsymbol { U } \boldsymbol { D } \boldsymbol { U } ^ { T } = \overline { { \boldsymbol { U } } } \left[ \overline { { \boldsymbol { D } } } - \overline { { \boldsymbol { D } } } \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } \alpha \boldsymbol { H } \overline { { \boldsymbol { U } } } \overline { { \boldsymbol { D } } } \right] \overline { { \boldsymbol { U } } } ^ { T } .
$$

Let

$$
\boldsymbol { F } = \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } , \boldsymbol { V } = \overline { { \boldsymbol { D } } } \boldsymbol { F } ,
$$

then Eq. (5.7.43) can be expressed as

$$
P = U D U ^ { T } = \overline { { U } } \left[ \overline { { D } } - V \alpha V ^ { T } \right] \overline { { U } } ^ { T } ,
$$

where

$$
\overline { { { U } } } = \left[ \begin{array} { c c c c c c } { { 1 \overline { { { U } } } _ { 1 2 } \cdots } } & { { \overline { { { U } } } _ { 1 n } } } \\ { { } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ddots } } \\ { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } \end{array} \right] ; \overline { { { D } } } = \left[ \begin{array} { c c c c c c c } { { \overline { { { d } } } _ { 1 } } } & { { 0 } } & { { } } \\ { { \overline { { { d } } } _ { 2 } } } & { { } } \\ { { } } & { { \ddots } } \\ { { } } & { { } } & { { \overline { { { d } } } _ { n } } } \end{array} \right] .
$$

$$
\boldsymbol { F } = \left[ \begin{array} { l } { \overline { { d } } _ { 1 } F _ { 1 } } \\ { \vdots } \\ { F _ { n } } \end{array} \right] = \overline { { \boldsymbol { U } } } ^ { T } \boldsymbol { H } ^ { T } ; \boldsymbol { V } = \overline { { D } } \boldsymbol { F } = \left[ \begin{array} { l } { \overline { { d } } _ { 1 } F _ { 1 } } \\ { \overline { { d } } _ { 2 } F _ { 2 } } \\ { \vdots } \\ { \overline { { d } } _ { n } F _ { n } } \end{array} \right] .
$$

Now let $\widetilde { U }$ and $\widetilde { D }$ be the factors of $[ \overline { { D } } - V \alpha V ^ { T } ]$ . Then Eq. (5.7.45) can be written as

$$
U D U ^ { T } = \overline { { { U } } } \widetilde { U } \widetilde { D } \widetilde { U } ^ { T } \overline { { { U } } } ^ { T } .
$$

Since $\overline { U }$ and $\widetilde { U }$ are upper triangular, their product will be upper triangular, and can be expressed as

$$
\begin{array} { l } { { U = \overline { { U } } \widetilde { U } } } \\ { { D = \widetilde { D } . } } \end{array}
$$

Hence, the problem of factoring the covariance measurement update for $P$ has been reduced to factoring the symmetric matrix $[ \overline { { \cal D } } - V \alpha V ^ { T } ]$ into $\widetilde { U }$ and $\widetilde { D }$ . This can be done using the square root free Cholesky decomposition or using the more computationally efficient algorithm presented in Thornton (1976) or Bierman (1977). This algorithm together with an example also appears in Maybeck (1979).

The computational algorithm for the measurement update of $P$ can be summarized then as follows:

Given: $\overline { { U } } , \overline { { D } } , H , R , \overline { { \mathbf { x } } }$ , and $y$

Compute:

1. $F = \overline { { U } } ^ { T } H ^ { T }$   
2. $V _ { i } = \overline { { d } } _ { i } F _ { i }$ , $i = 1 , \ldots , n$   
3. $\alpha _ { 1 } = \left( R + V _ { 1 } F _ { 1 } \right)$ d = d1R b1 = V1   
4. $\alpha _ { j } = \alpha _ { j - 1 } + F _ { j } V _ { j }$ $\left\{ { \begin{array} { l } { \qquad } \\ { j = 2 , \ldots , n } \\ { \qquad } \\ { \qquad \left. \right.} \\ { \qquad j = 2 , \ldots , n } \\ { \qquad } \\ { i = 1 , \ldots , j - } \end{array} }  \right.$ dj = dj αj−1 / αj bj = Vj pj = −Fj / αj−1   
5. $U _ { i j } = \overline { { U } } _ { i j } + b _ { i } p _ { j }$ bi = bi + U ij Vj 1   
6. K = b / αn   
$7 . { \hat { \mathbf { x } } } = { \overline { { \mathbf { x } } } } + K ( y - H { \overline { { \mathbf { x } } } } ) .$

Note that $\mathbf { b }$ is an $n$ vector, $[ b _ { 1 } , b _ { 2 } \dots b _ { n } ] ^ { T }$ . If the estimation error covariance matrix is needed, it may be calculated by using Eq. (5.7.39).

Thus far, with the exception of the Potter Algorithm, we have not addressed the time update of the estimation error covariance matrix. This will be addressed in Sections 5.8 and 5.9.

# 5.8 TIME UPDATE OF THE ESTIMATION ERROR COVARIANCE MATRIX

Section 5.7 deals primarily with the measurement update of the estimation error covariance matrix, $P$ . Various discrete algorithms have been developed for the time update. The most obvious approach for the time update would be to map $W W ^ { T }$ or $U D U ^ { T }$ using the conventional measurement update equation given in Chapter 4, for $W _ { k }$ and $V _ { k }$ ,

$$
\begin{array} { r l } & { \overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad = \Phi ( t _ { k + 1 } , t _ { k } ) W _ { k } W _ { k } ^ { T } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) V _ { k } V _ { k } ^ { T } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \end{array}
$$

where

$$
Q _ { k } = V _ { k } V _ { k } ^ { T } .
$$

$\overline { { P } } _ { k + 1 }$ may then be triangularized using a Cholesky transformation. After this, the measurement update is applied to process the next vector of observations.

Although this approach is computationally efficient, it is not as accurate as an orthogonal transformation approach that does not require the formation of the covariance matrix with the attendant numerical problems. A more accurate approach would be to find a propagation equation for the square root of $\overline { { P } }$ . This can be accomplished by noting that the right-hand side of Eq. (5.8.1) may be written as

$$
\overline { { P } } _ { k + 1 } = B _ { k + 1 } B _ { k + 1 } ^ { T }
$$

where

$$
B _ { k + 1 } = \left[ \Phi ( t _ { k + 1 } , t _ { k } ) W _ { k } \colon \Gamma ( t _ { k + 1 } , t _ { k } ) V _ { k } \right] .
$$

Note, however, that $B _ { k + 1 }$ would not be a square matrix but would be of dimension $n \times ( n { + } m )$ , where $n$ is the dimension of the state vector and $m$ is the dimension of the process noise vector. Various methods for converting Eq. (5.8.3) into an $n \times n$ triangular matrix are described by Bierman (1977), Thornton (1976), Maybeck (1979), Dyer and McReynolds (1969), and Kaminski (1971). The key to the triangularization of Eq. (5.8.3) is to note that an $( n + m ) \times ( n + m )$ orthogonal transformation, $T$ , can be applied to Eq. (5.8.2) so that (recall that $T T ^ { T } = I$ )

$$
B _ { k + 1 } T T ^ { T } B _ { k + 1 } ^ { T } = \tilde { W } _ { k + 1 } \tilde { W } _ { k + 1 } ^ { T }
$$

where

$$
\tilde { W } _ { k + 1 } = B _ { k + 1 } T = \left[ \phi : \overline { { W } } _ { k + 1 } \right]
$$

and where $\overline { { W } } _ { k + 1 }$ is now an $n \times n$ upper triangular matrix and $\phi$ is an $n \times m$ null matrix. Various methods that may be used to accomplish the triangularization are the Gram-Schmidt orthogonalization (Bierman, 1977), the Householder transformation, or the Givens transformation (Thornton, 1976).

The following Givens square root factorization algorithm is taken from Thornton (1976), and yields an $n \times n$ upper triangularization for $\overline { W }$ and an $n \times m$ null matrix, $\phi$ .

Let $B$ be a full rank $n \times ( n { + } m )$ matrix with column vectors $B _ { i }$ , $i = 1 \ldots , n +$ $m$ . The following algorithm yields an $n \times n$ upper triangular factor $\overline { W }$ such that $\overline { { W } } \ : \overline { { W } } ^ { T } = B B ^ { T }$ . For $j = n , \ldots , 1$ , cycle through Eqs. (5.8.6) through (5.8.12).

$$
k = m + j .
$$

For $i = k - 1 , \ldots 1$ evaluate recursively Eqs. (5.8.7) through (5.8.12).

$$
\begin{array} { c } { { B _ { k } ^ { \prime } ( j ) = \sqrt { ( B _ { i } ( j ) ) ^ { 2 } + ( B _ { k } ( j ) ) ^ { 2 } } } } \\ { { { } } } \\ { { C = B _ { k } ( j ) / B _ { k } ^ { \prime } ( j ) } } \\ { { S = B _ { i } ( j ) / B _ { k } ^ { \prime } ( j ) } } \\ { { { } } } \\ { { { \cal V } = B _ { i } } } \\ { { B _ { i } = C B _ { i } - S B _ { k } } } \\ { { B _ { k } = S V + C B _ { k } . } } \end{array}
$$

When completed this algorithm yields

$$
\begin{array} { c } { { \stackrel { m } { \longleftrightarrow } } } \\ { { B = \ \left[ \phi \ \stackrel { : } { : } \ \stackrel { n } { W } \ \right] \ \} n } } \end{array}
$$

where $\overline { W }$ is upper triangular.

As pointed out by Thornton (1976), a lower triangular factor $\overline { W }$ may be obtained from Eqs (5.8.6) through (5.8.12) if the indicies $i$ and $j$ are reordered so that $j = 1 , \dotsc , n$ and $i = j + 1 , \ldots , k$ . At the conclusion of this algorithm $B$ has the form

$$
\begin{array} { c } { { \stackrel { n } { \longleftrightarrow } } } \\ { { B = \ \left[ \overline { { { W } } } \ \stackrel { . } { : } \ \stackrel { m } { \phi } \ \right] \ \} n } } \end{array}
$$

where $\overline { W }$ is lower triangular.

The previous algorithms yield $\overline { W }$ as either upper or lower triangular. For the $U - D$ factorization we need $\overline { U }$ and $\overline { { D } }$ in order to perform the time update for $P$ ,

$$
\overline { { P } } = \overline { { U } } \overline { { D } } \overline { { U } } ^ { T }
$$

The following algorithm employs a generalized Gram-Schmidt orthogonalization to preserve numerical accuracy and was developed by Thornton and Bierman (1975), and it also appears in Maybeck (1979). The measurement update for $P$ at the $k ^ { \mathrm { t h } }$ stage is given by

$$
P _ { k } = U _ { k } D _ { k } U _ { k } ^ { T } .
$$

Let

$$
\begin{array} { l } { { Y _ { k + 1 } = [ \Phi ( t _ { k + 1 } , t _ { k } ) U _ { k } : \Gamma ( t _ { k + 1 } , t _ { k } ) ] } } \\ { { \widetilde D _ { k + 1 } = \left[ \begin{array} { l l } { { D _ { k } } } & { { 0 } } \\ { { 0 } } & { { Q _ { k } } } \end{array} \right] . } } \end{array}
$$

Then it can be seen that $Y _ { k + 1 } \widetilde { D } _ { k + 1 } Y _ { k + 1 } ^ { T }$ satisfies Eq. (5.8.1). We may now apply the following algorithm to obtain $\overline { U }$ and $\overline { { D } }$ , the time updated values of $U$ and $D$ . Let

$$
Y _ { k + 1 } ^ { T } = [ \mathbf { \_ { a } } _ { 1 } : \mathbf { a } _ { 2 } : \dots : \mathbf { a } _ { n } ]
$$

Where each vector ${ \bf a } _ { i }$ is of dimension $n + m$ . Again $n$ is the dimension of the state vector and $m$ is the dimension of the process noise vector.

$$
\begin{array} { l } { { \mathrm { F o r } \ell = n , n - 1 , \ldots , 1 : } } \\ { { \ } } \\ { { { \bf C } _ { \ell } = \widetilde D { \bf a } _ { \ell } \quad \mathrm { ( i . e . , } C _ { \ell j } = \widetilde D _ { j j } a _ { \ell j } , j = 1 , 2 , \ldots , n + m ) } } \\ { { \ } } \\ { { \overline { { { D } } } _ { \ell \ell } = { \bf a } _ { \ell } ^ { T } { \bf C } _ { \ell } \quad \quad \quad } } \\ { { \ } } \\ { { { \bf \overline { { U } } } _ { j \ell } = { \bf a } _ { j } / D _ { \ell \ell } \quad \quad \quad } } \\ { { \ } } \\ { { { \bf a } _ { j }  { \bf a } _ { j } - { \bf \overline { { U } } } _ { j \ell } { \bf a } _ { \ell } \quad \quad \quad } } \end{array}
$$

where $\longleftarrow$ denotes replacement; that is, write over the old variable to reduce storage requirements. For the final iteration, $\ell = 1$ and only $\mathbf { C } _ { 1 }$ and $D _ { 1 1 }$ are computed.

# 5.9 CONTINUOUS STATE ERROR COVARIANCE PROPAGATION

In this section a method that allows the integration of the continuous state error covariance differential equations in square root form is described. The derivation follows the approach used in Tapley and Choe (1976) and Tapley and Peters (1980), but the results are based on the $P \equiv U D U ^ { T }$ decomposition. This algorithm can be combined with a triangular measurement update algorithm to obtain a complete square root estimation algorithm for which square root operations are avoided. In addition, the effects of state process noise are included without approximation.

The differential equation for propagation of the state error covariance matrix can be expressed as

$$
{ \dot { \overline { { P } } } } ( t ) = A ( t ) { \overline { { P } } } ( t ) + { \overline { { P } } } ( t ) A ^ { T } ( t ) + Q ( t ) ,
$$

where $\overline { { P } } ( t )$ is the $a$ priori state error covariance matrix, $A ( t )$ is the $n \times n$ linearized dynamics matrix, and $Q ( t )$ is the process noise covariance matrix. Each of the matrices in Eq. (5.9.1) is time dependent in the general case. However, for simplicity, the time dependence will not be noted specifically in the following discussion.

If the following definitions are used,

$$
\overline { { { P } } } \equiv \overline { { { U } } } \overline { { { D } } } \overline { { { U } } } ^ { T } , \overline { { { Q } } } \equiv Q / 2 \ ,
$$

and if the first part of Eq. (5.9.2) is differentiated with respect to time and substituted into Eq. (5.9.1), the results can be rearranged to form

$$
\begin{array} { r l } & { ( \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 - \overline { { Q } } \overline { { U } } ^ { - T } - A \overline { { U } } \overline { { D } } ) \overline { { U } } ^ { T } } \\ & { + \overline { { U } } ( \overline { { D } } \dot { \overline { { U } } } ^ { T } + \dot { \overline { { D } } } \overline { { U } } ^ { T } / 2 - \overline { { U } } ^ { - 1 } \overline { { Q } } ^ { T } - \overline { { D } } \overline { { U } } ^ { T } A ^ { T } ) = 0 . } \end{array}
$$

Noting that the first term of Eq. (5.9.3) is the transpose of the second term, and making the following definition

$$
{ \cal C } ( t ) \equiv ( \dot { \overline { { U } } } \overline { { { D } } } + \overline { { { U } } } \dot { \overline { { { D } } } } / 2 - \overline { { { Q } } } \overline { { { U } } } ^ { - T } - A \overline { { { U } } } \overline { { { D } } } ) \overline { { { U } } } ^ { T }
$$

one obtains

$$
C ( t ) + C ^ { T } ( t ) = 0 .
$$

Relation (5.9.5) requires that $C ( t )$ be either the null matrix or, more generally, skew symmetric.

Equation (5.9.4) can be simplified by selectively carrying out the multiplication of the $- Q \overline { { U } } ^ { - T }$ term by $\overline { { U } } ^ { \bar { T } }$ to yield, after terms are arranged

$$
( \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 - A \overline { { U } } \overline { { D } } ) \overline { { U } } ^ { T } = \overline { { Q } } + C ( t ) \equiv \tilde { C } ( t ) .
$$

Equation (5.9.6) defines the differential equations for $\overline { U }$ and $\overline { { D } }$ to the degree of uncertainty in $C ( t )$ . Since the unknown matrix $C ( t )$ is skew symmetric, there exist $n ( n { - } 1 ) / 2$ unknown scalar quantities in Eq. (5.9.6). The problem considered here is one of specifying the elements of $C ( t )$ so that $\overline { U }$ is maintained in triangular form during the integration of Eq. (5.9.6). (The derivation pursued here assumes that $\overline { U }$ is lower triangular and $\overline { { D } }$ is diagonal, although an algorithm for an upper triangular $\overline { U }$ can be obtained as easily.) The following definiti ons are made to facilitate the solution to the problem posed:

$$
T \equiv A \overline { { { U } } } \overline { { { D } } } \quad M \equiv \dot { \overline { { { U } } } } \overline { { { D } } } + \overline { { { U } } } \dot { \overline { { { D } } } } / 2 - T .
$$

With these definitions, Eq. (5.9.6) is expressed as

$$
\boldsymbol { M } \boldsymbol { \overline { { U } } } ^ { T } = \boldsymbol { \widetilde { C } } ( t ) = \boldsymbol { \overline { { Q } } } + \boldsymbol { C } ( t ) \mathrm { ~ . ~ }
$$

Since $\overline { U }$ and $\dot { \overline { { U } } }$ in Eq. (5.9.6) are lower triangular, and since from Eq. (5.9.5) $C ( t )$ is skew symmetric, several observations can be made regarding Eq. (5.9.8). There are $n ( n - 1 ) / 2$ unknown elements in $\tilde { C }$ . The products $\dot { \overline { { U } } } \overline { { D } }$ and $\overline { { U } } \dot { \overline { { D } } }$ are lower triangular, creating $n ( n + 1 ) / 2$ unknowns. Therefore, the $n \times n$ system of equations in Eq. (5.9.8) has $\left[ n ( n - 1 ) / 2 + n ( n + 1 ) / 2 \right] = n \times n$ unknowns that can be determined uniquely.

An expansion of Eq. (5.9.8) into matrix elements indicates the method of solution

$$
\begin{array} { r l r } & { } & { \left[ { \cal M } _ { 1 1 } - { \cal T } _ { 1 2 } \cdot \cdot \cdot - { \cal T } _ { 1 n } \right] \left[ \begin{array} { l } { 1 \overline { { { \cal U } } } _ { 2 1 } \cdot \cdot \cdot \cdot \overline { { { \cal U } } } _ { n 1 } } \\ { M _ { 2 1 } \ M _ { 2 2 } \ \cdot \cdot \cdot \cdot - { \cal T } _ { 2 n } } \\ { \vdots \ \cdot \ 1 \ \cdot \ \cdot \cdot \overline { { { \cal U } } } _ { n 2 } } \\ { \vdots \ \vdots \ \cdot \ \ddots \ \vdots } \\ { M _ { n 1 } \ M _ { n 2 } \cdot \cdot \cdot \cdot \ M _ { n n } } \end{array} \right] \left[ \begin{array} { l } { 1 \overline { { { \cal U } } } _ { 2 1 } \cdot \cdot \cdot \cdot \overline { { { \cal U } } } _ { n 1 } } \\ { \vdots \ } \\ { \vdots \ } \\ { \vdots \ \vdots \ \cdot \ \ddots \ \vdots } \\ { 0 \ \vdots \ \ \vdots \ \ \ddots \ 1 } \end{array} \right] } \end{array}
$$

$$
= \left[ \begin{array} { c c c c } { \overline { { q } } _ { 1 1 } - C _ { 2 1 } \cdot \cdot \cdot - C _ { n 1 } } \\ { C _ { 2 1 } } & { \overline { { q } } _ { 2 2 } } & { \cdot \cdot \cdot - C _ { n 2 } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { C _ { n 1 } } & { C _ { n 2 } } & { \cdot \cdot \cdot } & { \overline { { q } } _ { m n } } \end{array} \right] .
$$

In Eq. (5.9.9), $\overline { { Q } }$ is assumed to be a diagonal matrix with elements $\overline { { q } } _ { i i } = q _ { i i } / 2$ $( i = 1 , \ldots , n )$ . (This assumption can be generalized to allow other nonzero terms in the $\overline { { Q } }$ matrix with only a slight increase in algebraic complexity.) Each row of the upper triangular portion of the $\widetilde { C }$ matrix in Eq. (5.9.9) is determined as the product of the corresponding row of the $M$ matrix with the appropriate column of the $\overline { { U } } ^ { T }$ matrix. After an upper triangular row of $\widetilde { C }$ is determined, the condition from Eq. (5.9.5) that $\begin{array} { r } { \ddot { C } _ { i j } = - \ddot { C } _ { j i } ( i = 1 , \dotsc , n ; j = 1 , \dotsc , i - 1 ) } \end{array}$ is invoked to evaluate the corresponding lower triangular column of $\widetilde { C }$ . Then, a column of the lower triangular elements of $M$ can be evaluated. Once the elements of the $M$ matrix are determined, the new row of the upper triangular $\widetilde { C }$ elements can be computed along with a column of the $\dot { \overline { { U } } }$ and $\dot { \overline { { D } } }$ elements. This process is repeated until all $\dot { \overline { { U } } }$ and $\dot { \overline { { D } } }$ values are determined. The implementation of this approach proceeds as follows. From Eqs. (5.9.6) and (5.9.7) one can write

$$
M + T = \dot { \overline { { U } } } \overline { { D } } + \overline { { U } } \dot { \overline { { D } } } / 2 .
$$

The expansion of Eq. (5.9.10) in summation notation gives

$$
M _ { i j } + T _ { i j } = \sum _ { k = 1 } ^ { n } { \dot { \overline { { U } } } } _ { i k } { \overline { { d } } } _ { k j } + \sum _ { k = 1 } ^ { n } { \overline { { U } } } _ { i k } { \dot { \overline { { d } } } } _ { k j }
$$

$$
\left( i = 1 , \ldots , n ; j = 1 , \ldots , i \right) .
$$

But, since $\overline { { D } }$ is diagonal, Eq. (5.9.11) becomes

$$
\begin{array} { c } { { M _ { i j } + T _ { i j } = \dot { \overline { { U } } } _ { i j } \overline { { d } } _ { j j } + \overline { { U } } _ { i j } \dot { \overline { { d } } } _ { j j } / 2 } } \\ { { \nonumber } } \\ { { ( i = 1 , \ldots , n ; j = 1 , \ldots , i ) } } \end{array}
$$

for $i = j , \overline { { U } } _ { i j } \equiv 1$ , and $\dot { \overline { { U } } } _ { i j } \equiv 0$ . Therefore, Eq. (5.9.12) becomes

$$
\dot { \overline { d } } _ { i i } = 2 \left( M _ { i i } + T _ { i i } \right) ( i = 1 , \ldots , n ) .
$$

For $i > j$ , Eq. (5.9.12) is rearranged to obtain the differential equation

$$
\begin{array} { r l r } & { } & { \dot { \overline { { U } } } _ { i j } = ( M _ { i j } + T _ { i j } - \overline { { U } } _ { i j } \dot { \overline { { d } } } _ { j j } / 2 ) / \overline { { d } } _ { j j } } \\ & { } & \\ & { } & { ( i = 2 , . . . , n ; ~ j = 1 , . . . , ~ i - 1 ) . } \end{array}
$$

Equations (5.9.13) and (5.9.14) are the forms of the differential equations to be employed in the derivative routine of a numerical integrator. The elements of $T _ { i j }$ and $M _ { i j }$ are computed as define d in Eq. (5.9.7). The pertinent equations can be combined to obtain the following algorithm.

# 5.9.1 TRIANGULAR SQUARE ROOT ALGORITHM

# Measurement Update

If the Extended Sequential Filter algorithm (for which the reference trajectory is updated at each observation point) is adopted, the measurement update algorithm for the $U D U ^ { T }$ factorization has the following form. Using the observation $Y _ { k + 1 } = G ( \mathbf { X } _ { k + 1 } , t _ { k + 1 } )$ , calculate

$$
H _ { k + 1 } = \left[ \partial G \left( \overline { { \mathbf { X } } } _ { k + 1 } , t _ { k + 1 } \right) / \partial \overline { { \mathbf { X } } } _ { k + 1 } \right] .
$$

For $i = 1 , \ldots , n$

$$
\overline { { F } } _ { i } = H _ { i } + \sum _ { k = i + 1 } ^ { n } H _ { k } \overline { { U } } _ { k i }
$$

$$
V _ { i } = \overline { { { d } } } _ { i } \overline { { { F } } } _ { i } .
$$

Set $\beta _ { n + 1 } = R _ { k + 1 }$ (where $R _ { k + 1 }$ is the variance of the measurement noise at the $k + 1 ^ { \mathrm { s t } }$ observation epoch) and calculate

$$
\beta _ { i } = \beta _ { i + 1 } + V _ { i } \overline { { F } } _ { i } \quad ( i = n , . . . , 1 ) .
$$

Calculate diagonal covariance elements

$$
\begin{array} { c } { { d _ { i } = \overline { { { d } } } _ { i } \beta _ { i + 1 } / \beta _ { i } ( i = 1 , \ldots , n ) } } \\ { { { } } } \\ { { \alpha = \beta _ { 1 } . } } \end{array}
$$

For $i = 2 , \ldots , n$ and $j = 1 , \dots , i - 1$ , calculate

$$
P _ { j } = \overline { { F } } _ { j } / \beta _ { j + 1 }
$$

$$
B _ { i j } = V _ { i } + \sum _ { k = j + 1 } ^ { i - 1 } { \overline { { U } } } _ { i k } V _ { k }
$$

$$
U _ { i j } = \overline { { { U } } } _ { i j } - B _ { i j } P _ { j } \quad ( i = 2 , \ldots n ; \quad j = 1 , \ldots , i - 1 ) .
$$

Compute the observation residual

$$
y _ { k + 1 } = Y _ { k + 1 } - G \left( \overline { { \mathbf { X } } } _ { k + 1 } , t _ { k + 1 } \right) .
$$

Calculate gain, and update the state using

$$
\begin{array} { l } { { \displaystyle { \overline { { K } } } _ { i } = V _ { i } + \sum _ { j = 1 } ^ { i - 1 } \overline { { U } } _ { i j } V _ { j } \quad ( i = 1 , \dots , n ) } } \\ { { \displaystyle \hat { \bf X } _ { i } = \overline { { \bf X } } _ { i } + \overline { { K } } _ { i } y _ { k + 1 } / \alpha \quad ( i = 1 , \dots , n ) . } } \end{array}
$$

# Propagation

Given the elements of the square root state error covariance in lower triangular $\overline { { U } } \overline { { D } } \overline { { U } } ^ { T }$ form, $\overline { { Q } } \equiv Q / 2$ and $A ( t )$ , the differential equations $\dot { \overline { { U } } } _ { i j }$ and $\dot { \overline { { d } } } _ { i i }$ can be computed as follows:

$$
\begin{array} { r l r } & { } & { \mathcal { T } _ { 3 \zeta } - \displaystyle \sum _ { j = 0 } ^ { \infty } \mathcal { A } _ { j , j } \mathbb { E } _ { j , j } \mathcal { A } _ { j , j } \left\{ \ell - 1 , \dots , n _ { k } \right\} } \\ & { } & { \mathcal { D } _ { j , 1 \ell } } \\ & { } & { \mathcal { E } _ { i \ell } = \displaystyle \sum _ { k = 1 } ^ { \ell } \lambda _ { i \ell } \widetilde { U } _ { j , k } - \displaystyle \sum _ { k = 1 + 1 } ^ { \ell } \mathcal { D } _ { k \ell } \widetilde { U } _ { \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { j \ell } - \displaystyle \sum _ { k = 1 } ^ { \ell } \lambda _ { \ell } \widetilde { U } _ { \ell } \left( \ell + 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \widetilde { \mathcal { D } } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { D } _ { k \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { M } _ { i , j } = \widetilde { U } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { M } _ { j , \ell } \mathcal { D } _ { \ell } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { H } _ { i , j } = \widetilde { U } _ { i , j } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \widetilde { \mathcal { D } } _ { i , j } \frac { \ell - 1 } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \left( \lambda _ { i \ell } \right) _ { i \ell } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 2 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } & { \mathcal { D } _ { i , j } = \left( \lambda _ { i \ell } \right) _ { i \ell } \frac { \ell } { \lambda _ { \ell } } \mathcal { D } _ { j , 1 } \left( \ell - 1 , \dots , n _ { k } \right) } \\ & { } &  \end{array}
$$

The algorithm summarized in Eqs. (5.9.15) through (5.9.32) defines a complete sequential estimation algorithm in which the covariance matrices $P$ and $\bar { \overline { { P } } }$ are replaced by the factors $( U , D )$ and $( \overline { { U } } , \overline { { D } } )$ , respectively. The algorithm given here assumes that only a single scalar observation is processed at each observation epoch; however, the algorithm is applicable to the case of multiple observations at a given epoch if the observation errors are uncorrelated. To obtain

$$
A ( t ) = \frac { F ( { \bf X } , t ) } { \partial { \bf X } } ,
$$

the additional integration of the system of nonlinear differential equations, ${ \dot { \bf X } } = { }$ $F ( \mathbf { X } , t )$ , is required. At the initial point, the starting conditions $\dot { \overline { { \mathbf { X } } } } _ { k } = \hat { \mathbf { X } } _ { k }$ are used.

# 5.10 THE SQUARE ROOT INFORMATION FILTER

In Sections 5.7, 5.8, and 5.9, attention has been directed to the problem of developing estimation algorithms based on the square root of the covariance matrix. Both measurement incorporation and time propagation algorithms were considered. In this section, we consider algorithms derived from the information equations, referred to as the normal equations in Chapter 4. Specificall y, we consider algorithms that deal with factoring the information matrix. In general such an algorithm is referred to as a square root information fil ter or SRIF.

We will first consider the case where the state vector, $\mathbf { x }$ , is independent of time; that is, a constant. Assume that $a$ priori information $[ \overline { { \mathbf { x } } } , \overline { { \Lambda } } ]$ is given, where x is the a priori value of x and Λ is the a priori information matrix, Λ = P −1 . The $a$ priori information can be written in the form of a data equation by noting that

$$
\begin{array} { r } { \overline { { \mathbf { x } } } = \mathbf { x } + \boldsymbol { \eta } , } \end{array}
$$

where $\eta$ is the error in $\overline { { \mathbf { x } } }$ and is assumed to have the following characteristics

$$
E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } } = \overline { { \Lambda } } ^ { - 1 } .
$$

Factoring the information matrix yields

$$
\overline { { { \Lambda } } } = \overline { { { R } } } ^ { T } \overline { { { R } } } .
$$

Multiplying Eq. (5.10.1) by $\overline { { R } }$ yields

$$
\overline { { R } } \overline { { \mathbf { x } } } = \overline { { R } } \mathbf { x } + \overline { { R } } \boldsymbol { \eta } .
$$

Define

$$
\begin{array} { r } { \overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } } \quad \mathrm { a n d } \quad \overline { { \eta } } = \overline { { R } } \eta . } \end{array}
$$

Then Eq. (5.10.4) assumes the standard form of the data equation

$$
\overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } } .
$$

Note that the error $\overline { { \eta } }$ still has zero mean but now has unit variance,

$$
\begin{array} { r l } & { E [ \overline { { \eta } } ] = \overline { { R } } E [ \pmb { \eta } ] = 0 } \\ & { E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { R } } E [ \pmb { \eta } \pmb { \eta } ^ { T } ] \overline { { R } } ^ { T } = \overline { { R } } \overline { { P } } \overline { { R } } ^ { T } = I . } \end{array}
$$

We now seek to determine the “best” estimate of $\mathbf { x }$ given the a priori information in the form of Eq. (5.10.6), and additional observation data

$$
\mathbf { y } = H \mathbf { x } + \epsilon ,
$$

where $\epsilon \sim ( O , I )$ ; the observations have been prewhitened as described in Section 5.7.1. This value of $\mathbf { x }$ will be defined as that which minimizes the least squares performance index,

$$
\begin{array} { r l } & { J ( \mathbf { x } ) = \| \boldsymbol { \epsilon } \| ^ { 2 } + \| \overline { { \eta } } \| ^ { 2 } } \\ & { \qquad = \| H \mathbf { x } - \mathbf { y } \| ^ { 2 } + \| \overline { { R } } \mathbf { x } - \overline { { \mathbf { b } } } \| ^ { 2 } } \\ & { \qquad = \left\| \left[ \begin{array} { l } { \overline { { R } } } \\ { H } \end{array} \right] \mathbf { x } - \left[ \overline { { \mathbf { b } } } \right] \right\| ^ { 2 } . } \end{array}
$$

Following the procedure of Section 5.4, we apply a series of orthogonal transformations to Eq. (5.10.9) such that

$$
T \left[ { \frac { { \overline { { R } } } { \bar { \mathbf { b } } } } { H { \mathbf { y } } } } \right] = { \left[ { R \mathbf { b } } \right] }
$$

and the performance index becomes

$$
{ \begin{array} { r } { J ( \mathbf { x } ) = \left\| \left[ { \boldsymbol { R } } \right] \mathbf { x } - \left[ \mathbf { b } \right] \right\| ^ { 2 } } \\ { = \| { \boldsymbol { R } } \mathbf { x } - \mathbf { b } \| ^ { 2 } + \| \mathbf { e } \| ^ { 2 } . } \end{array} }
$$

The value of the $\mathbf { x }$ that minimizes the performance index is

$$
\hat { \mathbf { x } } = R ^ { - 1 } \mathbf { b } .
$$

Equation (5.10.12) is most easily solved by a backward substitution given by Eq. (5.2.8),

$$
\hat { x } _ { i } = \left( b _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } \hat { x } _ { j } \right) / R _ { i i } , i = n \ldots 1 .
$$

The data processing algorithm based on the orthogonal transformation can be summarized as follows. Assume we are given the $a$ priori information $\overline { { \cal R } } , \overline { { \bf b } }$ and the measurements $y _ { j } = H _ { j } { \bf x } + \epsilon _ { j } , j = 1 , \ldots , \ell$ , where each $y _ { j }$ is a scalar and where $\epsilon _ { j } \sim ( O , 1 )$ . Then the least squares estimate can be generated recursively as follows:

(a) Compute

$$
T _ { j } \left[ { \begin{array} { l } { { \overline { { R } } } { \bar { \mathbf { \Delta b } } } } \\ { { H _ { j } y _ { j } } } \end{array} } \right] = \left[ { R _ { j } \mathbf { \Delta b } _ { j } } \right] .
$$

(b) $R _ { j } { \hat { \mathbf { x } } } _ { j } = \mathbf { b } _ { j } .$

Solve for $\hat { \mathbf { x } } _ { j }$ by a backward substitution as given by Eq. (5.10.13) at each stage $j$ . If the estimation error covariance matrix is desired at any stage, it is computed from

$$
P _ { j } = R _ { j } ^ { - 1 } R _ { j } ^ { - T } .
$$

(c) $R _ { j }$ and $\mathbf { b } _ { j }$ become the a priori for the next stage.

(d) Repeat this process for $j = 1 , \dots , \ell$ .

Note that the residual sum of squares of the $a$ priori errors plus observation errors based on $\ell$ measurements is

$$
J ( \widehat { \mathbf { x } } _ { \ell } ) = \sum _ { i = 1 } ^ { \ell } \left( y _ { i } - H _ { i } \widehat { \mathbf { x } } _ { \ell } \right) ^ { 2 } + ( \widehat { \mathbf { x } } _ { \ell } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { R } } ^ { T } \overline { { R } } ( \widehat { \mathbf { x } } _ { \ell } - \overline { { \mathbf { x } } } ) = \sum _ { i = 1 } ^ { \ell } e _ { i } ^ { 2 } .
$$

# 5.10.1 THE SQUARE ROOT INFORMATION FILTER WITH TIME-DEPENDENT EFFECTS

Consider the dynamic model of Eq. (4.9.46),

$$
\mathbf { x } _ { k } = \boldsymbol \Phi ( t _ { k } , t _ { j } ) \mathbf { x } _ { j } + \Gamma ( t _ { k } , t _ { j } ) \mathbf { u } _ { j }
$$

where

$$
E [ \mathbf { u } _ { j } ] = \overline { { \mathbf { u } } } , ~ E [ ( \mathbf { u } _ { j } - \overline { { \mathbf { u } } } ) ( \mathbf { u } _ { k } - \overline { { \mathbf { u } } } ) ^ { T } ] = Q \delta _ { j k } .
$$

Generally we assume that $\mathbf { \overline { { u } } = 0 }$ , but for this discussion we will assume that the random sequence $\mathbf { u } _ { j }$ has a known mean, u. $Q$ is assumed to be positive definite, and may vary with time, but we will assume that both $Q$ and $\mathbf { \overline { { u } } }$ are constant here.

Assume that a sequence of scalar observation, $y _ { i }$ , is given such that

$$
y _ { i } = H _ { i } \mathbf { x } _ { i } + \epsilon _ { i } , \quad i = 1 , \ldots , \ell
$$

and the observations have been prewhitened so that

$$
E [ \epsilon _ { i } ] = 0 , ~ E ( \epsilon _ { i } ^ { 2 } ) = 1 .
$$

Assume that at the initial time, say $t _ { 0 }$ , there is $a$ priori information given in the form of the information array $[ \overline { { R } } _ { 0 } , \overline { { \mathbf { b } } } _ { 0 } ]$ from which $\overline { { \mathbf { x } } } _ { 0 }$ and $\overline { { P } } _ { 0 }$ are determined as (the a priori information may be $\overline { { \mathbf { x } } } _ { \mathrm { 0 } }$ and $\overline { { P } } _ { 0 }$ from which $[ \overline { { R } } _ { 0 } , \overline { { \mathbf { b } } } _ { 0 } ]$ are computed)

$$
{ \bf { \overline { { x } } } } _ { 0 } = { \overline { { R } } } _ { 0 } ^ { - 1 } { \bf { \overline { { b } } } } _ { 0 } \quad { \bf { \overline { { P } } } } _ { 0 } = { \overline { { R } } } _ { 0 } ^ { - 1 } { \overline { { R } } } _ { 0 } ^ { - T } .
$$

Because $E [ \mathbf { u } ( t _ { 0 } ) ] = \overline { { \mathbf { u } } }$ , the a priori quantities are mapped to $t _ { 1 }$ by

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { \mathbf { x } } } _ { 0 } + \Gamma ( t _ { 1 } , t _ { 0 } ) \overline { { \mathbf { u } } } } \\ & { \mathbf { x } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) \mathbf { x } _ { 0 } + \Gamma ( t _ { 1 } , t _ { 0 } ) \mathbf { u } _ { 0 } } \\ & { \overline { { P } } _ { 1 } = E [ ( \overline { { \mathbf { x } } } _ { 1 } - \mathbf { x } _ { 1 } ) ( \overline { { \mathbf { x } } } _ { 1 } - \mathbf { x } _ { 1 } ) ^ { T } ] } \\ & { \quad \mathbf { \Phi } = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { P } } _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) + \Gamma ( t _ { 1 } , t _ { 0 } ) Q \Gamma ^ { T } ( t _ { 1 } , t _ { 0 } ) . } \end{array}
$$

For the case where there is no process noise, $Q$ is assumed to be zero, as is $\mathbf { u } _ { j }$ , and the following solution is applicable.

# Process Noise Absent

In this case both $Q$ and $\mathbf { \overline { { u } } }$ are assumed to be zero and

$$
\overline { { { P } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) .
$$

In terms of square root notation

$$
\overline { { { P } } } _ { k } = \overline { { { R } } } _ { k } ^ { - 1 } \overline { { { R } } } _ { k } ^ { - T } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 } R _ { j } ^ { - T } \Phi ^ { T } ( t _ { k } , t _ { j } ) .
$$

Hence,

$$
\overline { { R } } _ { k } ^ { - 1 } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 }
$$

and

$$
\overline { { { R } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) .
$$

It follows then that the mapping relations are

$$
\begin{array} { l } { { { \overline { { \bf x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) { \hat { \bf x } } _ { j } } } \\ { { { \overline { { R } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) . } } \end{array}
$$

Note also that the compressed observation can be obtained as

$$
\begin{array} { r l } & { \mathbf { \overline { { b } } } _ { k } = \overline { { R } } _ { k } \mathbf { \overline { { x } } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \quad \mathbf { \overline { { \Lambda } } } = R _ { j } \hat { \mathbf { x } } _ { j } = \mathbf { b } _ { j } . } \end{array}
$$

With these mapping equations we can set up the equations for the SRIF algorithm. Assume that at time, $t _ { j }$ , we have a priori information

$$
\overline { { \mathbf { b } } } _ { j } = \overline { { R } } _ { j } \overline { { \mathbf { x } } } _ { j }
$$

where

$$
\overline { { \mathbf { x } } } _ { j } = \mathbf { x } _ { j } + \boldsymbol { \eta } _ { j }
$$

and

$$
\begin{array} { r } { E [ \pmb { \eta } _ { j } ] = 0 \qquad } \\ { E [ \pmb { \eta } _ { j } \pmb { \eta } _ { j } ^ { T } ] = \overline { { P } } _ { j } = \overline { { R } } _ { j } ^ { - 1 } \ \overline { { R } } _ { j } ^ { - T } . } \end{array}
$$

By multiplying Eq. (5.10.27) by $\overline { { R } } _ { j }$ , we obtain

$$
\overline { { \mathbf { b } } } _ { j } = \overline { { R } } _ { j } \mathbf { x } _ { j } + \overline { { \pmb { \eta } } } _ { j }
$$

where $\overline { { \pmb { \eta } } } _ { j } = \overline { { \pmb { R } } } _ { j } \pmb { \eta } _ { j }$ . Further, $\overline { { \pmb { \eta } } } _ { j }$ satisfies the condition $E ( \overline { { \eta } } _ { j } ) = 0$ and it is easily demonstrated that $E ( \overline { { \eta } } _ { j } \overline { { \eta } } _ { j } ^ { T } ) = I$ . Now assume that we have the new observation, $y _ { j }$ , where

$$
y _ { j } = H _ { j } \mathbf { x } _ { j } + \epsilon _ { j }
$$

and $\epsilon _ { j }$ satisfies the conditions given in Eq. (5.10.18). To obtain a best estimate of $\mathbf { x } _ { j }$ , the least squares performance index to be minimized is

$$
J ( \mathbf { x } _ { j } ) = \| \overline { { \pmb { \eta } } } _ { j } \| ^ { 2 } + \epsilon _ { j } ^ { 2 } ,
$$

or

$$
J ( \mathbf { x } _ { j } ) = \| \overline { { R } } _ { j } \mathbf { x } _ { j } - \overline { { \mathbf { b } } } _ { j } \| ^ { 2 } + \left( H _ { j } \mathbf { x } _ { j } - y _ { j } \right) ^ { 2 } .
$$

Following the procedure discussed in the previous section, $J ( \mathbf { x } _ { j } )$ can be written as

$$
J ( \mathbf { x } _ { j } ) = \left\| \left[ \overline { { R } } _ { j } \right] \mathbf { x } _ { j } - \left[ \overline { { \mathbf { b } } } _ { j } \right] \right\| ^ { 2 } .
$$

Multiplying by an orthogonal transformation, $T$ , yields

$$
J ( \mathbf { x } _ { j } ) = [ \begin{array} { l } { [ \overline { { R } } _ { j } ] } \\ { H _ { j } } \end{array} ] \mathbf { x } _ { j } - [ \overline { { \mathbf { b } } } _ { j } ] ] ^ { T } T ^ { T } T [ \begin{array} { l } { [ \overline { { R } } _ { j } ] } \\ { H _ { j } } \end{array} ] \mathbf { x } _ { j } - [ \overline { { \mathbf { b } } } _ { j } ] ] .
$$

We select $T$ so that

$$
T \left[ { \overline { { R } } } _ { j } \right] = { \bigg [ } R _ { j } { \bigg ] } , T \left[ { \overline { { \mathbf { b } } } } _ { j } \right] = { \bigg [ } { \mathbf { b } } _ { j } { \bigg ] }
$$

where $R _ { j }$ is upper triangular. Eq. (5.10.30) can be expressed then as

$$
J ( \mathbf { x } _ { j } ) = \left\| \left[ \binom { R _ { j } } { 0 } \mathbf { x } _ { j } - \left[ \mathbf { b } _ { j } \right] \right] ^ { 2 } \right\| ^ { 2 }
$$

or

$$
J ( \mathbf { x } _ { j } ) = ( e _ { j } ) ^ { 2 } + \| R _ { j } \mathbf { x } _ { j } - \mathbf { b } _ { j } \| ^ { 2 } .
$$

It follows that to minimize $J ( \mathbf { x } _ { j } )$ ,

$$
\hat { \mathbf { x } } _ { j } = R _ { j } ^ { - 1 } \mathbf { b } _ { j } , P _ { j } = R _ { j } ^ { - 1 } R _ { j } ^ { - T } , J ( \hat { \mathbf { x } } _ { j } ) \ : = \ : e _ { j } ^ { 2 } .
$$

where the elements of the vector $\hat { \mathbf { x } } _ { j }$ are obtained by evaluating Eq. (5.10.13). The previous steps are equivalent to the measurement update for the Kalman filter. The time update is obtained by mapping $\hat { \mathbf { x } } _ { j }$ and $R _ { j }$ forward to time $t _ { k }$ as follows

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \overline { { R } } _ { k } = R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) } \\ & { \overline { { \mathbf { b } } } _ { k } = \overline { { R } } _ { k } \overline { { \mathbf { x } } } _ { k } = \mathbf { b } _ { j } } \end{array}
$$

and the measurement update process is repeated to obtain $\hat { \mathbf { x } } _ { k }$ . Note that the sum of squares of the estimation errors would be stored as (assuming we have processed $k$ scalar observations)1

$$
J ( \mathbf { x } _ { k } ) = \sum _ { i = 1 } ^ { k } e _ { i } ^ { 2 } .
$$

An alternate equation to Eq. (5.10.23) can be obtained by noting that for any $t$ ,

and

$$
\begin{array} { r } { \overline { { R } } ( t ) = R _ { j } \Phi ^ { - 1 } ( t , t _ { j } ) } \\ { \qquad } \\ { \dot { \overline { { R } } } ( t ) = R _ { j } \dot { \Phi } ^ { - 1 } ( t , t _ { j } ) . } \end{array}
$$

Substituting for $\dot { \Phi } ^ { - 1 } ( t , t _ { j } )$ leads to

$$
\dot { \overline { { { R } } } } ( t ) = - R _ { j } \Phi ^ { - 1 } ( t , t _ { j } ) A ( t ) = - \overline { { { R } } } ( t ) A ( t ) .
$$

Hence, as an alternate to Eq. (5.10.23) one can integrate the equation

$$
{ \dot { \overline { { R } } } } ( t ) = - { \overline { { R } } } A ( t ) .
$$

with initial conditions

$$
\begin{array} { r } { \overline { { R } } ( t _ { j } ) = R _ { j } . } \end{array}
$$

The propagation can be accomplished either by using Eq. (5.10.37) or by integrating Eq. (5.10.38) while propagating the state by integrating

$$
\dot { \overline { { \mathbf { x } } } } = A ( t ) \overline { { \mathbf { x } } } ,
$$

with the initial conditions $\overline { { \mathbf { x } } } _ { j } = \hat { \mathbf { x } } _ { j }$ . However, because $\overline { { \mathbf { b } } } _ { k } = \mathbf { b } _ { j }$ there is no need to map $\overline { { \mathbf { x } } } _ { j }$ . The $a$ priori covariance $\overline { { P } } _ { k }$ at $t _ { k }$ is obtained, in either case, as

$$
\overline { { P } } _ { k } = \overline { { R } } _ { k } ^ { - 1 } \overline { { R } } _ { k } ^ { - T } .
$$

If needed, a differential equation for $\overline { { R } } ^ { - 1 }$ is easily developed. From Eq. (5.10.37)

$$
\overline { { R } } _ { k } ^ { - 1 } = \Phi ( t _ { k } , t _ { j } ) R _ { j } ^ { - 1 }
$$

and

$$
\begin{array} { r l } & { \dot { \overline { { R } } } ^ { - 1 } ( t ) = \dot { \Phi } ( t , t _ { j } ) R _ { j } ^ { - 1 } } \\ & { \qquad = A ( t ) \Phi ( t , t _ { j } ) R _ { j } ^ { - 1 } } \\ & { \dot { \overline { { R } } } ^ { - 1 } ( t ) = A ( t ) \overline { { R } } ^ { - 1 } ( t ) , \mathrm { w i t h ~ I . c . ~ } \overline { { R } } ^ { - 1 } ( t _ { j } ) = R _ { j } ^ { - 1 } . } \end{array}
$$

Finally, note that even though $R _ { j }$ is upper triangular, the propagated information matrix $\overline { { R } } _ { k }$ will not be. An upper triangular time update for $\overline { { R } } _ { k }$ can be developed by noting that

$$
\overline { { { \Lambda } } } _ { k } = \overline { { { P } } } _ { k } ^ { - 1 } = \overline { { { R } } } _ { k } ^ { T } \overline { { { R } } } _ { k } .
$$

From Eq. (5.10.37)

$$
\overline { { \Lambda } } _ { k } = \Phi ^ { - T } ( t _ { k } , t _ { j } ) R _ { j } ^ { T } R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } )
$$

multiplying by an orthogonal transformation yields

$$
\overline { { \Lambda } } _ { k } = \Phi ^ { - T } ( t _ { k } , t _ { j } ) R _ { j } ^ { T } T ^ { T } T R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } ) = \overline { { R } } _ { k } ^ { T } \overline { { R } } _ { k }
$$

where $T$ is chosen so that

$$
\overline { { R } } _ { k } = T R _ { j } \Phi ^ { - 1 } ( t _ { k } , t _ { j } )
$$

is upper triangular. A Householder or Givens transformation may be used to accomplish this.

# 5.10.2 THE DYNAMIC CASE WITH PROCESS NOISE

The technique for including process noise in both the Potter and SRIF algorithms was developed by Dyer and McReynolds (1969). The state propagation equation for the case with process noise is given by Eq. (5.10.16),

$$
\mathbf { x } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \mathbf { x } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \mathbf { u } _ { k - 1 } .
$$

The SRIF for this case can be formulated as follows. Assume that at $t _ { k - 1 }$ a priori information in the form of an information array $[ \overline { { R } } _ { k - 1 } \overline { { \mathbf { b } } } _ { k - 1 } ]$ or equivalently $[ \overline { { P } } _ { k - 1 } \overline { { \mathbf { x } } } _ { k - 1 } ]$ is available,

$$
\overline { { \mathbf { b } } } _ { k - 1 } = \overline { { R } } _ { k - 1 } \overline { { \mathbf { x } } } _ { k - 1 }
$$

but

$$
\overline { { \mathbf { x } } } _ { k - 1 } = \mathbf { x } _ { k - 1 } + \boldsymbol { \eta } _ { k - 1 }
$$

where $\mathbf x _ { k - 1 }$ is the true value. Also,

$$
E [ \pmb { \eta } _ { k - 1 } ] = 0 , E [ \pmb { \eta } _ { k - 1 } \pmb { \eta } _ { k - 1 } ^ { T } ] = \overline { { P } } _ { k - 1 } = \overline { { R } } _ { k - 1 } ^ { - 1 } \overline { { R } } _ { k - 1 } ^ { - T } .
$$

Substituting Eq. (5.10.47) into (5.10.46) yields the data equation for the $a$ priori information

$$
\overline { { \mathbf { b } } } _ { k - 1 } = \overline { { R } } _ { k - 1 } \mathbf { x } _ { k - 1 } + \overline { { \pmb { \eta } } } _ { k - 1 }
$$

where

$$
\begin{array} { c } { { E [ \overline { { { \pmb { \eta } } } } _ { k - 1 } ] = \overline { { { \cal R } } } _ { k - 1 } E [ \pmb { \eta } _ { k - 1 } ] = 0 } } \\ { { E [ \overline { { { \pmb { \eta } } } } _ { k - 1 } \overline { { { \pmb { \eta } } } } _ { k - 1 } ^ { T } ] = \overline { { { \cal R } } } _ { k - 1 } \overline { { { \cal P } } } _ { k - 1 } \overline { { { \cal R } } } _ { k - 1 } ^ { T } = I . } } \end{array}
$$

A scalar observation is given at $t _ { k - 1 }$

$$
y _ { k - 1 } = H _ { k - 1 } \mathbf { x } _ { k - 1 } + \epsilon _ { k - 1 }
$$

where we assume that the observations have been prewhitened so that $\epsilon _ { k - 1 } \sim$ [0, 1].

A priori information on $\mathbf { u } _ { k - 1 }$ is given by covariance $Q$ and by $\overline { { \mathbf { u } } } _ { k - 1 }$ , the mean value of $\mathbf { u }$ . Generally it is assumed that $\mathbf { u }$ is a zero mean process so that the $a$ priori value $\overline { { \mathbf { u } } } = 0$ at each stage. This information also may be written in the form of a data equation by noting that

$$
\begin{array} { c } { { \overline { { \mathbf { u } } } = \overline { { \mathbf { u } } } _ { k - 1 } } } \\ { { \mathbf { \Pi } } } \\ { { \mathbf { \Pi } = \mathbf { u } _ { k - 1 } + \alpha _ { k - 1 } } } \end{array}
$$

where $\overline { { \mathbf { u } } } _ { k - 1 }$ is the a priori value and $\mathbf { u } _ { k - 1 }$ is the true value. The error, $\pmb { \alpha } _ { k - 1 }$ , has the properties

$$
\begin{array} { r } { E [ \pmb { \alpha } _ { k - 1 } ] = 0 , } \\ { E [ \pmb { \alpha } _ { k - 1 } \pmb { \alpha } _ { k - 1 } ^ { T } ] = Q . } \end{array}
$$

We will assume that the process noise is uncorrelated in time; that is, $E [ \pmb { \alpha } _ { i } \pmb { \alpha } _ { j } ^ { T } ] =$ 0 for $i \neq j$ . Although it is not necessary, we will assume that both $\mathbf { u }$ and $Q$ are constant in time. Factor $Q$ such that

$$
\begin{array} { r } { R _ { u } ^ { - 1 } R _ { u } ^ { - T } = Q . } \end{array}
$$

After multiplying Eq. (5.10.53) by $R _ { u }$ , we may write the data equation for $\overline { { \mathbf { u } } } _ { k - 1 }$ as

$$
\begin{array} { r l } {  { R _ { u } \overline { { \mathbf { u } } } _ { k - 1 } \equiv \overline { { \mathbf { b } } } _ { u _ { k - 1 } } } } \\ & { = R _ { u } \mathbf { u } _ { k - 1 } + \overline { { \mathbf { \alpha } } } \overline { { \mathbf { \alpha } } } _ { k - 1 } } \end{array}
$$

where

$$
\begin{array} { r } { \overline { { \alpha } } _ { k - 1 } \sim [ O , I ] . } \end{array}
$$

Now define a performance index for the measurement update at $t _ { k - 1 }$ . We choose as our least squares performance index the sum of the squared errors given by Eqs (5.10.49), (5.10.52), and (5.10.56),

$$
\hat { J } _ { k - 1 } = \| \overline { { \eta } } _ { k - 1 } \| ^ { 2 } + ( \epsilon _ { k - 1 } ) ^ { 2 } + \| \overline { { \alpha } } _ { k - 1 } \| ^ { 2 } .
$$

Note that including $\| \overline { { \alpha } } \| ^ { 2 }$ in the performance index allows us to estimate $\mathbf { u }$ at each stage. The values of $\mathbf x _ { k - 1 }$ that minimizes $\hat { J } _ { k - 1 }$ is the filter value, $\hat { \mathbf { x } } _ { k - 1 }$ . At this point the value of $\mathbf { u } _ { k - 1 }$ that minimizes $\hat { J } _ { k - 1 }$ is just the $a$ priori value, $\overline { { \mathbf { u } } } _ { k - 1 }$ . After we perform a time and measurement update at $t _ { k }$ we will have the necessary information to compute $\hat { \mathbf { u } } _ { k - 1 }$ . Use the defining equations for the errors to write $\hat { J } _ { k - 1 }$ as

$$
\begin{array} { r l } & { \hat { J } _ { k - 1 } = \Vert \overline { { R } } _ { k - 1 } \mathbf { x } _ { k - 1 } - \overline { { \mathbf { b } } } _ { k - 1 } \Vert ^ { 2 } + ( H _ { k - 1 } \mathbf { x } _ { k - 1 } - y _ { k - 1 } ) ^ { 2 } } \\ & { \qquad + \Vert R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \Vert ^ { 2 } . } \end{array}
$$

Because $\mathbf x _ { k - 1 }$ is independent of $\mathbf { u } _ { k - 1 }$ it is convenient to write this as

$$
\hat { J } _ { k - 1 } = \left\| \left[ \begin{array} { l } { \overline { { R } } _ { k - 1 } } \\ { H _ { k - 1 } } \end{array} \right] \mathbf { x } _ { k - 1 } - \left[ \overline { { \mathbf { b } } } _ { k - 1 } \right] \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \| ^ { 2 } .
$$

Applying a series of orthogonal transformations to the first term of Eq. (5.10.59) results in

$$
\hat { J } _ { k - 1 } = \left\| \begin{array} { l } { \left[ \begin{array} { l } { \hat { R } _ { k - 1 } } \\ { 0 } \end{array} \right] \mathbf { x } _ { k - 1 } - \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { k - 1 } } \\ { e _ { k - 1 } } \end{array} \right] } \end{array} \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k - 1 } - \overline { { \mathbf { b } } } _ { u _ { k - 1 } } \| ^ { 2 }
$$

or

$$
\hat { J } _ { k - 1 } = ( e _ { k - 1 } ) ^ { 2 } + \| \hat { R } _ { k - 1 } { \bf x } _ { k - 1 } - \hat { \bf b } _ { k - 1 } \| ^ { 2 } + \| R _ { u } { \bf u } _ { k - 1 } - \overline { { { \bf b } } } _ { u _ { k - 1 } } \| ^ { 2 } .
$$

The minimum value of $\hat { J } _ { k - 1 }$ is found by setting

$$
\begin{array} { r } { \hat { R } _ { k - 1 } \hat { \mathbf { x } } _ { k - 1 } = \hat { \mathbf { b } } _ { k - 1 } } \\ { R _ { u } \overline { { \mathbf { u } } } _ { k - 1 } = \overline { { \mathbf { b } } } _ { u _ { k - 1 } } . } \end{array}
$$

As stated earlier, Eq. (5.10.63) returns the $a$ priori value, $\overline { { \mathbf { u } } } _ { k - 1 }$ . The minimum value of $\hat { J } _ { k - 1 }$ is given by

$$
\begin{array} { r } { \hat { J } _ { k - 1 } = \left( e _ { k - 1 } \right) ^ { 2 } . } \end{array}
$$

Also,

$$
P _ { k - 1 } = \hat { R } _ { k - 1 } ^ { - 1 } \hat { R } _ { k - 1 } ^ { - T } .
$$

Having completed the measurement update at $t _ { k - 1 }$ , we are ready to do the time update to $t _ { k }$ . In order to time update the performance index $\hat { J } _ { k - 1 } ^ { - }$ , we need to write Eq. (5.10.61) in terms of $\mathbf { x } _ { k }$ . Because $\mathbf { u } _ { k - 1 }$ is not time dependent, the update of $\mathbf { u }$ to $t _ { k }$ will be handled in the measurement update. From Eq. (5.10.45) we may write $\mathbf x _ { k - 1 }$ in terms of $\mathbf { x } _ { k }$ ,

$$
{ \bf x } _ { k - 1 } = \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) ( { \bf x } _ { k } - \Gamma ( t _ { k } , t _ { k - 1 } ) { \bf u } _ { k - 1 } ) .
$$

Substituting Eq. (5.10.66) into Eq. (5.10.61) yields the time update

$$
\begin{array} { r l r } & { } & { \overline { { J } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \Vert \hat { R } _ { k - 1 } \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) ( { \bf x } _ { k } - \Gamma ( t _ { k } , t _ { k - 1 } ) { \bf u } _ { k - 1 } ) - \hat { { \bf b } } _ { k - 1 } \Vert ^ { 2 } } \\ & { } & { + \Vert { R } _ { u } { \bf u } _ { k - 1 } - \overline { { { \bf b } } } _ { u _ { k - 1 } } \Vert ^ { 2 } , \qquad ( { \boldsymbol 5 } . 1 0 . } \end{array}
$$

which may be written as

$$
\begin{array} { r l } & { \overline { { \boldsymbol J } } _ { k } = ( \boldsymbol e _ { k - 1 } ) ^ { 2 } + } \\ & { \left\| \left[ \begin{array} { l } { \boldsymbol R _ { u } } \\ { - \tilde { \boldsymbol R } _ { k } \boldsymbol \Gamma ( t _ { k } , t _ { k - 1 } ) ~ \tilde { \boldsymbol R } _ { k } } \end{array} \right] \left[ \begin{array} { l } { \mathbf u _ { k - 1 } } \\ { \mathbf x _ { k } } \end{array} \right] - \left[ \overline { { \mathbf b } } _ { u _ { k - 1 } } \right] \right\| ^ { 2 } } \end{array}
$$

where

$$
\tilde { R } _ { k } \equiv \hat { R } _ { k - 1 } \Phi ^ { - 1 } ( t _ { k } , t _ { k - 1 } ) .
$$

We now apply a series of $q$ orthogonal transformations to the second term of Eq. (5.10.68), where $q$ is the dimension of $\mathbf { u } _ { k - 1 }$ . This will partly upper triangularize Eq. (5.10.68) (for $q < n$ ) and will eliminate the explicit dependence of $\mathbf { x } _ { k }$ on $\mathbf { u } _ { k - 1 }$ , i.e.

$$
\begin{array} { r } { \overline { { T } } _ { k } \left[ \begin{array} { c c } { R _ { u } } & { 0 } & { \overline { { \mathbf { b } } } _ { u _ { k - 1 } } } \\ { - \tilde { R } _ { k } \Gamma ( t _ { k } , t _ { k - 1 } ) } & { \tilde { R } _ { k } } & { \hat { \mathbf { b } } _ { k - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { \overline { { R } } _ { u _ { k } } } & { \overline { { R } } _ { u x _ { k } } } & { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { 0 } & { \overline { { R } } _ { k } } & { \overline { { \mathbf { b } } } _ { k } } \end{array} \right] . } \end{array}
$$

Then,

$$
\begin{array} { r } { \overline { { \boldsymbol { J } } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \left\| \left[ \begin{array} { l l } { \overline { { R } } _ { u _ { k } } } & { \overline { { R } } _ { u x _ { k } } } \\ { 0 } & { \overline { { R } } _ { k } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { u } _ { k - 1 } } \\ { \mathbf { x } _ { k } } \end{array} \right] - \left[ \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \overline { { \mathbf { b } } } _ { k } } \end{array} \right] \right\| ^ { 2 } . } \end{array}
$$

The minimum value of $J$ is obtained by setting

$$
\begin{array} { r } { \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } = \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \overline { { R } } _ { k } \mathbf { x } _ { k } = \overline { { \mathbf { b } } } _ { k } . } \end{array}
$$

Therefore,

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \overline { { R } } _ { k } ^ { - 1 } \overline { { \mathbf { b } } } _ { k } . } \end{array}
$$

Because $\overline { { R } } _ { u k }$ is nonsingular we can find a value of $\mathbf { u } _ { k - 1 }$ to satisfy Eq. (5.10.72) for any value of $\mathbf { x } _ { k }$ . We know that the value of $\overline { { \mathbf { x } } } _ { k }$ that results from Eq. (5.10.74) is given by

$$
\overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \overline { { \mathbf { u } } } _ { k - 1 }
$$

where $\overline { { \mathbf { u } } } _ { k - 1 }$ is the mean or $a$ priori value. Using this value of $\overline { { \mathbf { x } } } _ { k }$ in Eq. (5.10.72) will yield $\overline { { \mathbf { u } } } _ { k - 1 }$ . This is to be expected since we get no information on $\overline { { \mathbf { u } } } _ { k - 1 }$ until we process an observation at $t _ { k }$ .

Recall that the error covariance associated with $\bar { \bf x } _ { k }$ is

$$
\begin{array} { r l } & { \overline { { P } } _ { k } = E [ ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ^ { T } ] = \overline { { R } } _ { k } ^ { - 1 } \overline { { R } } _ { k } ^ { - T } } \\ & { \quad = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { \quad + \Gamma ( t _ { k } , t _ { k - 1 } ) Q \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) . } \end{array}
$$

Equation (5.10.71) may be written as

$$
\begin{array} { r l } & { \overline { { J } } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \widetilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ & { \quad ~ + \| \overline { { R } } _ { k } \mathbf { x } _ { k } - \overline { { \mathbf { b } } } _ { k } \| ^ { 2 } . } \end{array}
$$

We may now do the measurement update at $t _ { k }$ . The least squares performance index for the measurement update is

$$
\begin{array} { r l } & { \hat { J } _ { k } = \overline { { J } } _ { k } + ( \epsilon _ { k } ) ^ { 2 } + \| \overline { { \alpha } } _ { k } \| ^ { 2 } } \\ & { \quad = \overline { { J } } _ { k } + ( H _ { k } \mathbf { x } _ { k } - y _ { k } ) ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

This may be written as

$$
\begin{array} { r } { \hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \widetilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ { + \left\| \left[ \overline { { R } } _ { k } \right] \mathbf { x } _ { k } - \left[ \overline { { \mathbf { b } } } _ { k } \right] \right\| ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

Applying orthogonal transformations to the third term yields

$$
\begin{array} { r l } & { \hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + \| \overline { { R } } _ { u _ { k } } \mathbf { u } _ { k - 1 } + \overline { { R } } _ { u x _ { k } } \mathbf { x } _ { k } - \tilde { \mathbf { b } } _ { u _ { k } } \| ^ { 2 } } \\ & { \quad + \| \hat { R } _ { k } \mathbf { x } _ { k } - \hat { \mathbf { b } } _ { k } \| ^ { 2 } + ( e _ { k } ) ^ { 2 } + \| R _ { u } \mathbf { u } _ { k } - \overline { { \mathbf { b } } } _ { u _ { k } } \| ^ { 2 } . } \end{array}
$$

Once again $\mathbf { u } _ { k - 1 }$ , $\mathbf { u } _ { k }$ , and $\mathbf { x } _ { k }$ may be chosen to null all but the $( e ) ^ { 2 }$ terms. Hence, the minimum value of $\hat { J } _ { k }$ is

$$
\hat { J } _ { k } = ( e _ { k - 1 } ) ^ { 2 } + ( e _ { k } ) ^ { 2 } .
$$

The time update to obtain $\overline { { J } } _ { k + 1 }$ may now be obtained by substituting

$$
\mathbf { x } _ { k } = \Phi ^ { - 1 } \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \bigl ( \mathbf { x } _ { k + 1 } - \Gamma \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \mathbf { u } _ { k } \bigr )
$$

for $\mathbf { x } _ { k }$ in the term $\| \hat { R } _ { k } \mathbf { x } _ { k } - \hat { \mathbf { b } } _ { k } \| ^ { 2 }$ . Hence, the general expression for the time update at $t _ { m }$ after processing $m - 1$ observations is

$$
\begin{array} { r l r } {  { \overline { { J } } _ { m } = \sum _ { i = 1 } ^ { m - 1 } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m - 1 } \| \overline { { R } } _ { u _ { i } } \mathbf { u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } \mathbf { x } _ { i } - \widetilde { \mathbf { b } } _ { u _ { i } } \| ^ { 2 } } } \\ & { } & { + \| [ \begin{array} { l } { R _ { u } } \\ { - \widetilde { R } _ { m } \Gamma ( t _ { m } , t _ { m - 1 } ) \widetilde { R } _ { m } } \end{array} ] [ \begin{array} { l } { \mathbf { u } _ { m - 1 } } \\ { \mathbf { x } _ { m } } \end{array} ] - [ \overline { { \mathbf { b } } } _ { u _ { m - 1 } } ] \| ^ { 2 } } \end{array}
$$

and the corresponding measurement update for processing $m$ observations is obtained by upper triangularizing the third term of Eq. (5.10.82) and adding the data equations for the $m ^ { t h }$ observation,

$$
\begin{array} { r l r } {  { \hat { J } _ { m } = \overline { { J } } _ { m } + ( \epsilon _ { m } ) ^ { 2 } + \| \overline { { \boldsymbol { \alpha } } } _ { m } \| ^ { 2 } } } \\ & { } & { = \displaystyle \sum _ { i = 1 } ^ { m - 1 } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m } \| \overline { { R } } _ { u _ { i } } \mathbf { u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } \mathbf { x } _ { i } - \widetilde { \mathbf { b } } _ { u _ { i } } \| ^ { 2 } + \| R _ { u } \mathbf { u } _ { m } - \overline { { \mathbf { b } } } _ { u _ { m } } \| ^ { 2 } } \\ & { } & { + \| [ \overline { { R } } _ { m } ] \mathbf { x } _ { m } - [ \overline { { \mathbf { b } } } _ { m } ] \| ^ { 2 } . \quad \quad \quad \quad ( 5 . 1 0 . } \end{array}
$$

An orthogonal transformation is then applied to the last term of Eq. (5.10.83).

Finally, continuing the time and measurement update through stage $m$ yields

$$
\begin{array} { l } { { \displaystyle \hat { J } _ { m } = \sum _ { i = 1 } ^ { m } ( e _ { i } ) ^ { 2 } + \sum _ { i = 1 } ^ { m } \| \overline { { R } } _ { u _ { i } } { \bf u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } { \bf x } _ { i } - \widetilde { { \bf b } } _ { u _ { i } } \| ^ { 2 } } } \\ { { \displaystyle ~ + \| R _ { u } { \bf u } _ { m } - \overline { { { \bf b } } } _ { u _ { m } } \| ^ { 2 } + \| \hat { R } _ { m } { \bf x } _ { m } - \hat { { \bf b } } _ { m } \| ^ { 2 } } , } \end{array}
$$

so that for the filtering problem ${ \hat { J } } _ { m } $ is minimized by choosing

$$
\hat { \mathbf { x } } _ { m } = \hat { R } _ { m } ^ { - 1 } \hat { \mathbf { b } } _ { m }
$$

and

$$
\overline { { { R } } } _ { u _ { i } } \hat { \mathbf { u } } _ { i - 1 } = \widetilde { \mathbf { b } } _ { u _ { i } } - \overline { { { R } } } _ { u x _ { i } } \hat { \mathbf { x } } _ { i } ; i = m , m - 1 \ldots 1 .
$$

Notice that the third term in Eq. (5.10.84) is simply the addition of a priori information on $\mathbf { u } _ { m }$ and does not affect the performance index until we perform a time and measurement update at $t _ { m + 1 }$ . Then it yields the estimate for $\hat { \mathbf { u } } _ { m }$ given by Eq. (5.10.86) with $i = m + 1$ .

If we were performing only a filtering operation and had a need for a filtered value of $\hat { \bf { u } }$ , we would calculate it at each stage and not save the quantities $\overline { { R } } _ { u }$ , $\overline { { { \bf b } } } _ { u }$ , and $\overline { { R } } _ { u x }$ needed to compute it. However, if we wish to perform smoothing, these quantities should be saved as described in Section 5.10.4.

# 5.10.3 SRIF COMPUTATIONAL ALGORITHM

The SRIF computational algorithm is summarized as follows. Assuming we have processed the observations at the $k - 1 ^ { s t }$ stage, the time update for $t _ { k }$ is obtained by applying a series of orthogonal transformations, $\overline { { T } } _ { k }$ , to

$$
\begin{array} { r l } { \overrightarrow { T } _ { k } } &  \left[ \overbrace { \frac { R _ { u } } { - \tilde { R } _ { k } \Gamma ( t _ { k } , t _ { k - 1 } ) \left| \ \tilde { R } _ { k } \right| \ \hat { \mathbf { b } } _ { k - 1 } } } ^ { q } \right] \mathbf { \} \mathbf { \Sigma } _ { \left. n \right. } } \\ &  = \left[ \begin{array} { c c c c } { \overbrace { \tilde { R } _ { u _ { k } } } ^ { \mathrm { ~ ~ \it ~ n ~ } } } & { \overbrace { \tilde { R } _ { u _ { k } u _ { k } } } ^ { \mathrm { ~ \it ~ n ~ } } } & { \overbrace { \tilde { \mathbf { b } } _ { u _ { k } } } ^ { \mathrm { ~ \it ~ 1 ~ } } } & { } \\ { 0 } & { \overbrace { \tilde { R } _ { k } \mathrm { ~ \it ~ \hat { \textbf { b } } } _ { k } } ^ { \mathrm { ~ \it ~ 1 ~ } } } & { \right] \mathbf { \Sigma } _ { \left. n \right. } } \end{array} \end{array}
$$

where $\tilde { R } _ { k }$ is defined by Eq. (5.10.69) and $q$ and $n$ are the dimensions of the process noise and state vector, respectively. From Eqs. (5.10.70) and (5.10.71) we can write

$$
\left[ \begin{array} { c } { { \overline { { { R } } } _ { u _ { k } } \overline { { { R } } } _ { u x _ { k } } } } \\ { 0 \overline { { { R } } } _ { k } } \end{array} \right] \left[ \begin{array} { c } { { \widetilde { \mathbf { u } } _ { k - 1 } } } \\ { { \overline { { \mathbf { x } } } _ { k } } } \end{array} \right] = \left[ \begin{array} { c } { { \widetilde { \mathbf { b } } _ { u _ { k } } } } \\ { { \overline { { \mathbf { b } } } _ { k } } } \end{array} \right]
$$

from which $\tilde { \mathbf { u } } _ { k - 1 }$ , $\overline { { \mathbf { x } } } _ { k }$ and $\overline { { P } } _ { k }$ may be computed if desired. It is not necessary to compute these quantities. However, the quantities in the first row of Eq. (5.10.87) should be stored if smoothing is to take place.

The measurement update at $t _ { k }$ is obtained by applying a series of orthogonal transformations, $\hat { T } _ { k }$ , to

$$
\hat { T } _ { k } \stackrel { n } { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { \widehat { R } _ { k } } & { \widehat { \mathbf { b } } _ { k } } \\ { H _ { k } } & { y _ { k } } \end{array} \right] } \} n = \left[ \hat { R } _ { k } \hat { \mathbf { b } } _ { k } \right]
$$

and

$$
\begin{array} { r } { \hat { R } _ { k } \hat { \mathbf x } _ { k } = \hat { \mathbf b } _ { k } \quad } \\ { P _ { k } = \hat { R } _ { k } ^ { - 1 } \ \hat { R } _ { k } ^ { - T } } \\ { e = e + e _ { k } ^ { 2 } \ \quad } \end{array}
$$

where $e$ is the sum of squares of the observation residuals.

We can compute the filter value, $\hat { \mathbf { u } } _ { k - 1 }$ , by substituting $\hat { \mathbf { x } } _ { k }$ into Eq. (5.10.86),

$$
\hat { \mathbf { u } } _ { k - 1 } = \overline { { R } } _ { u _ { k } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k } } - \overline { { R } } _ { u x _ { k } } \hat { \mathbf { x } } _ { k } \big ) .
$$

The time update at $t _ { k + 1 }$ may now be computed from Eq. (5.10.87) and the measurement update from Eq. (5.10.89) after changing the index from $k$ to $k + 1$ . The procedure is continued until all observations have been processed.

# 5.10.4 SMOOTHING WITH THE SRIF

There are two approaches that may be taken to perform smoothing with the SRIF (Kaminski, 1971). The first of these uses the performance index given by Eq. (5.10.84). This performance index must be satisfied by the smooth states as well as the filter states. Hence, the equations needed for smoothing are Eqs. (5.10.85), (5.10.86), and (5.10.66). These are repeated using smoothing notation:

$$
\begin{array} { r } { \hat { R } _ { m } \hat { \mathbf { x } } _ { m } ^ { m } = \hat { \mathbf { b } } _ { m } } \\ { \overline { { R } } _ { u _ { i } } \hat { \mathbf { u } } _ { i - 1 } ^ { m } = \widetilde { \mathbf { b } } _ { u _ { i } } - \overline { { R } } _ { u x _ { i } } \hat { \mathbf { x } } _ { i } ^ { m } \quad i = m , m - 1 , \ldots , 1 . } \\ { \hat { \mathbf { x } } _ { i - 1 } ^ { m } = \Phi ^ { - 1 } ( t _ { i } , t _ { i - 1 } ) ( \hat { \mathbf { x } } _ { i } ^ { m } - \Gamma ( t _ { i } , t _ { i - 1 } ) \hat { \mathbf { u } } _ { i - 1 } ^ { m } ) } \end{array}
$$

where the notation $( ) _ { i } ^ { m }$ means the smoothed value of the quantity at $t _ { i }$ based on $m$ observations. Note that this is the same notation used for the conventional smoother in Section 4.15.

Starting with $\hat { \mathbf { x } } _ { m } ^ { m }$ from Eq. (5.10.94), then $\hat { \mathbf { u } } _ { m - 1 } ^ { m }$ is computed from Eq. (5.10.95) and $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ is determined from Eq. (5.10.96). With this value of $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ , compute $\hat {  { \mathbf { u } } } _ { m - 2 } ^ { m }$ from Eq. (5.10.95) and $\hat { \mathbf { x } } _ { m - 2 } ^ { m }$ from Eq. (5.10.96), and so on.

This backward sweep strategy may be shown to be equivalent to the smoother described in Section 4.15, and hence it is also equivalent to the Rauch, Tung, and Striebel smoother (1995).

This equivalence may be used to derive an expression for the smoothed covariance for $\hat { \mathbf { x } } _ { k } ^ { m }$ using the filt er time update equation

$$
\overline { { \mathbf { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { \mathbf { u } } } _ { k } .
$$

The smoothed solution must also satisfy this equation; hence

$$
\hat { \mathbf { x } } _ { k + 1 } ^ { m } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { m } + \Gamma ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { u } } _ { k } ^ { m } .
$$

Using Eqs. (5.10.97) and (5.10.98) we may write

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { m } - \hat { \mathbf { x } } _ { k } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } \right] } \\ & { \qquad + \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \Gamma ( t _ { k + 1 } , t _ { k } ) \left[ \overline { { \mathbf { u } } } _ { k } - \hat { \mathbf { u } } _ { k } ^ { m } \right] . } \end{array}
$$

From Eq. (5.10.95)

$$
\hat { \mathbf { u } } _ { k } ^ { m } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k + 1 } } - \overline { { R } } _ { u x _ { k + 1 } } \hat { \mathbf { x } } _ { k + 1 } ^ { m } \big ) .
$$

This equation also yields the fil ter value of $\overline { { \mathbf { u } } } _ { k }$

$$
\overline { { \mathbf { u } } } _ { k } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \big ( \widetilde { \mathbf { b } } _ { u _ { k + 1 } } - \overline { { R } } _ { u x _ { k + 1 } } \overline { { \mathbf { x } } } _ { k + 1 } \big ) .
$$

From Eq. (5.10.100) and (5.10.101) we may write

$$
\overline { { \mathbf { u } } } _ { k } - \hat { \mathbf { u } } _ { k } ^ { m } = \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } ( \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } ) .
$$

Substituting Eq. (5.10.102) into (5.10.99) results in

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } ^ { m } = \hat { \mathbf { x } } _ { k } + \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ I + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } \right] } \\ { \times \left[ \hat { \mathbf { x } } _ { k + 1 } ^ { m } - \overline { { \mathbf { x } } } _ { k + 1 } \right] . \qquad } \end{array}
$$

Comparing Eq. (5.10.103) with Eqs. (4.15.9) and (4.15.10) yields the identity

$$
\begin{array} { r l } & { S _ { k } = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) \left( P _ { k + 1 } ^ { k } \right) ^ { - 1 } } \\ & { \quad = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) \left[ I + \Gamma ( t _ { k + 1 } , t _ { k } ) \overline { { R } } _ { u _ { k + 1 } } ^ { - 1 } \overline { { R } } _ { u x _ { k + 1 } } \right] . } \end{array}
$$

Recall that $\mathbf { \overline { { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k }$ in Eq. (4.15.9) since $\overline { { \mathbf { u } } } _ { k } = 0$ by assumption. Hence, the smoothed covariance for the estimation error in $\hat { \mathbf { x } } _ { k } ^ { m }$ may be obtained

from Eq. (4.15.24),

$$
P _ { k } ^ { m } = P _ { k } ^ { k } + S _ { k } ( P _ { k + 1 } ^ { m } - P _ { k + 1 } ^ { k } ) S _ { k } ^ { T }
$$

where $P _ { k } ^ { k }$ is the measurement update of the filter covariance at $t _ { k }$ and $P _ { k + 1 } ^ { k }$ is the time-updated value of $P _ { k } ^ { k }$ at $t _ { k + 1 }$ .

Note that this approach requires storage of the time and measurement update of the filter covariance. The time update is given by Eq. (5.10.75), where ${ \overline { { \overline { { P } } } } } \equiv$ $P _ { k + 1 } ^ { k }$ . The measurement update is given by Eq. (5.10.91), where $P _ { k } \equiv P _ { k } ^ { k }$ .

The smoothing operation also may be carried out, as described by Kaminski (1971), using an approach that yields the smoothed covariance directly and does not require storage of the filter covariance. Use Eq. (5.10.66) in Eq. (5.10.84) to eliminate $\mathbf { x } _ { m }$ . Then the performance index in terms of $\mathbf { x } _ { m - 1 } ^ { m }$ and $\mathbf { u } _ { m - 1 } ^ { m }$ becomes

$$
\begin{array} { r l r } {  { \hat { J } _ { m - 1 } ^ { m } = e _ { m } + \sum _ { m - 1 } + \Vert \overline { { R } } _ { u _ { m } } ^ { m } \mathbf { u } _ { m - 1 } ^ { m } + \overline { { R } } _ { u x _ { m } } [ \Phi ( t _ { m } , t _ { m - 1 } ) \mathbf { x } _ { m - 1 } ^ { m }  } } \\ & { } & { +  \Gamma ( t _ { m } , t _ { m - 1 } ) \mathbf { u } _ { m - 1 } ^ { m } ] - \widetilde { \mathbf { b } } _ { u _ { m } }  ^ { 2 } + \Vert \hat { R } _ { m } [ \Phi ( t _ { m } , t _ { m - 1 } ) \mathbf { x } _ { m - 1 } ^ { m }   } \\ & { } & {   + \Gamma ( t _ { m } , t _ { m - 1 } ) \mathbf { u } _ { m - 1 } ^ { m } ] - \hat { \mathbf { b } } _ { m } \Vert ^ { 2 } . } \end{array}
$$

The term $\| R _ { u } \mathbf { u } _ { m } - \overline { { \mathbf { b } } } _ { u _ { m } } \| ^ { 2 }$ has been dropped since its value is zero by definition; hence, it does not effect the value of $\hat { J } _ { m - 1 } ^ { m }$ . Also,

$$
\begin{array} { l } { { \displaystyle e _ { m } \equiv \sum _ { i = 1 } ^ { m } ( e _ { i } ) ^ { 2 } } \ ~ } \\ { { \displaystyle \sum _ { m - 1 } \equiv \sum _ { i = 1 } ^ { m - 1 } \left\| \overline { { R } } _ { u _ { i } } { \bf u } _ { i - 1 } + \overline { { R } } _ { u x _ { i } } { \bf x } _ { i } - \widetilde { { \bf b } } _ { u _ { i } } \right\| ^ { 2 } } \ . } \end{array}
$$

Equation (5.10.106) may be written as

$$
\begin{array} { r } { \hat { J } _ { m - 1 } ^ { m } =  [ \begin{array} { l } { [ \begin{array} { l } { \overline { { R } } _ { u _ { m } } + \overline { { R } } _ { u x _ { m } } \Gamma ( t _ { m } , t _ { m - 1 } ) } \end{array} ] \begin{array} { l } { \overline { { R } } _ { u x _ { m } } \Phi ( t _ { m } , t _ { m - 1 } ) } \\ { \hat { R } _ { m } \hat { \Phi } ( t _ { m } , t _ { m - 1 } ) } \end{array} ] } \\ { [ \begin{array} { l } { \mathbf { u } _ { m - 1 } ^ { m } } \\ { \mathbf { x } _ { m - 1 } ^ { m } } \end{array} ] - [ \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { m } } } \\ { \hat { \mathbf { b } } _ { m } } \end{array} ]  ^ { 2 } + e _ { m } + \boldsymbol { \Sigma } _ { m - 1 } . } \end{array}  ~ ( 5 . 1 } \end{array}
$$

A series of orthogonal transformation is used to upper triangularize the first term of Eq. (5.10.109),

$$
\begin{array} { r l } { T _ { m - 1 } ^ { * } } &  { } \left[ \frac { \phantom { \frac { 1 } { 2 } } \overline { { R } } _ { u _ { m } } + \overline { { R } } _ { u x _ { m } } \Gamma ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \phantom { \frac { 1 } { 2 } } \left| \begin{array} { c } { \overline { { R } } _ { u x _ { m } } \Phi ( t _ { m } , t _ { m - 1 } ) } \end{array} \right. \right] } \\ { \phantom { \frac { 1 } { 2 } } \left. \qquad \hat { R } _ { m } \Gamma ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \qquad \hat { R } _ { m } \Phi ( t _ { m } , t _ { m - 1 } ) \phantom { \frac { 1 } { 2 } } \phantom { \frac { 1 } { 2 } } \right] } \end{array}
$$

$$
\mathbf { \Phi } = \left[ \begin{array} { c } { R _ { u _ { m - 1 } } ^ { * } } \\ { 0 } \end{array} \right] \begin{array} { c } { R _ { u x _ { m - 1 } } ^ { * } } \\ { R _ { m - 1 } ^ { * } } \end{array} \left[ \begin{array} { c } { \mathbf { b } _ { u _ { m - 1 } } ^ { * } } \\ { \ \mathbf { b } _ { m - 1 } ^ { * } } \end{array} \right] .
$$

Hence,

$$
\begin{array} { r } { \hat { J } _ { m - 1 } ^ { m } = \left\| \boldsymbol { R } _ { u _ { m - 1 } } ^ { * } \mathbf { u } _ { m - 1 } ^ { m } + { \cal R } _ { u x _ { m - 1 } } ^ { * } \mathbf { x } _ { m - 1 } ^ { m } - \mathbf { b } _ { u _ { m - 1 } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| { \cal R } _ { m - 1 } ^ { * } \mathbf { x } _ { m - 1 } ^ { m } - \mathbf { b } _ { m - 1 } ^ { * } \right\| ^ { 2 } + e _ { m } + \Sigma _ { m - 1 } . } \end{array}
$$

To minimize $\hat { J } _ { m - 1 } ^ { m }$ , choose

$$
\begin{array} { r l } & { R _ { u _ { m - 1 } } ^ { * } \hat { \mathbf { u } } _ { m - 1 } ^ { m } = \mathbf { b } _ { u _ { m - 1 } } ^ { * } - R _ { u x _ { m - 1 } } ^ { * } \hat { \mathbf { x } } _ { m - 1 } ^ { m } } \\ & { \quad R _ { m - 1 } ^ { * } \hat { \mathbf { x } } _ { m - 1 } ^ { m } = \mathbf { b } _ { m - 1 } ^ { * } . } \end{array}
$$

The elements of $\Sigma _ { m - 1 }$ can be nulled by the proper selection of $\mathbf { u } _ { m - 2 } . . . . \mathbf { u } _ { 0 }$ . Therefore, we do not need to consider this term. The covariance for the estimation error in $\hat { \mathbf { u } } _ { m - 1 } ^ { m }$ and $\hat { \mathbf { x } } _ { m - 1 } ^ { m }$ is given by

$$
\begin{array} { r l } & { P _ { m - 1 } ^ { m } \equiv \left[ \begin{array} { c } { P _ { u } \ P _ { u x } } \\ { P _ { x u } \ P _ { x } } \end{array} \right] _ { m - 1 } ^ { m } } \\ & { \qquad = \left[ \begin{array} { c } { R _ { u _ { m - 1 } } ^ { * } \ R _ { u x _ { m - 1 } } ^ { * } } \\ { 0 \ R _ { m - 1 } ^ { * } } \end{array} \right] ^ { - 1 } \left[ R _ { u _ { m - 1 } } ^ { * } R _ { u x _ { m - 1 } } ^ { * } \right] ^ { - T } . } \end{array}
$$

Solving the equation

$$
\left[ \begin{array} { c c } { R _ { u _ { m - 1 } } ^ { * } } & { R _ { u x _ { m - 1 } } ^ { * } } \\ { 0 } & { R _ { m - 1 } ^ { * } } \end{array} \right] \left[ \begin{array} { c c } { A } & { B } \\ { 0 } & { C } \end{array} \right] = \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { I } \end{array} \right]
$$

for the matrices $A , B$ , and $C$ yields the inverse necessary to solve for $P _ { m - 1 } ^ { m }$ Substituting the result into Eq. (5.10.114) results in

$$
\begin{array} { r l } & { P _ { u _ { m - 1 } } ^ { m } = R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u _ { m - 1 } } ^ { * - T } } \\ & { \qquad + R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u x _ { m - 1 } } ^ { * } R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } R _ { u x _ { m - 1 } } ^ { * T } R _ { u _ { m - 1 } } ^ { * - T } } \\ & { P _ { u x _ { m - 1 } } ^ { m } = - R _ { u _ { m - 1 } } ^ { * - 1 } R _ { u x _ { m - 1 } } ^ { * } R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } } \\ & { \qquad P _ { x _ { m - 1 } } ^ { m } = R _ { m - 1 } ^ { * - 1 } R _ { m - 1 } ^ { * - T } . } \end{array}
$$

We are now ready to write $J _ { m - 1 } ^ { m }$ in terms of $ { \mathbf { x } } _ { m - 2 } ^ { m }$ and $ { \mathbf { u } } _ { m - 2 } ^ { m }$ . Because $\mathbf { u } _ { m - 1 } ^ { m }$ is independent of either of these quantities and we have already chosen its value

to null the fir st term in Eq. (5.10.111), we may drop this term when writing $J _ { m - 2 } ^ { m }$ hence,

$$
\begin{array} { r l } & { \hat { J } _ { m - 2 } ^ { m } = \hphantom { \eta } \| R _ { m - 1 } ^ { * } \mathbf x _ { m - 1 } - \mathbf b _ { m - 1 } ^ { * } \| ^ { 2 } + \| \overline { { R } } _ { u _ { m - 1 } } \mathbf u _ { m - 2 } } \\ & { \qquad + \overline { { R } } _ { u x _ { m - 1 } } \mathbf x _ { m - 1 } - \widetilde { \mathbf b } _ { u _ { m - 1 } } \| ^ { 2 } + e _ { m } + \Sigma _ { m - 2 } . } \end{array}
$$

Now use Eq. (5.10.45) to write $\mathbf x _ { m - 1 }$ in Eq. (5.10.118) in terms of $\mathbf { x } _ { m - 2 }$ ,

$$
\begin{array}{c} \begin{array} { r l r } {  { \hat { f } _ { m - 2 } ^ { m } = \| R _ { m - 1 } ^ { * } [ \Phi ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { x } _ { m - 2 } + \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { u } _ { m - 2 } ] - \mathbf { b } _ { m - 1 } ^ { * } \| ^ { 2 } } } \\ & { } & { + \| \overline { { R } } _ { u _ { m - 1 } } \mathbf { u } _ { m - 2 } + \overline { { R } } _ { u x _ { m - 1 } } [ \Phi ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { x } _ { m - 2 }   } \\ & { } & {   + \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) \mathbf { u } _ { m - 2 } ] - \widetilde { \mathbf { b } } _ { u _ { m - 1 } } \| ^ { 2 } + e _ { m } + \sum _ { m - 2 } } \\ & { } & { = \| [ \begin{array} { l l } { \overline { { R } } _ { u _ { m - 1 } } + \overline { { R } } _ { u x _ { m - 1 } } \Gamma ( t _ { m - 2 } , t _ { m - 1 } ) } & { | \overline { { R } } _ { u x _ { m - 1 } } \Phi ( t _ { m - 2 } , t _ { m - 1 } )  } \\ {   R _ { m - 1 } ^ { * } \Gamma ( t _ { m - 2 } , t _ { m - 1 } )   } & {   R _ { m - 1 } ^ { * } \Phi ( t _ { m - 2 } , t _ { m - 1 } ) ] } \end{array} ] } \\ & { } & { [ \begin{array} { l } { \mathbf { u } _ { m - 2 } } \\ { \mathbf { x } _ { m - 2 } } \end{array} ] - [ \widetilde { \mathbf { b } } _ { u _ { m - 1 } } } \\ { \mathbf { b } _ { m - 1 } ^ { * } } \end{array} ] \| ^ { 2 } + e _ { m } + \Sigma _ { m - 2 } .  \end{array}
$$

Next a series of orthogonal tranformations is applied to Eq. (5.10.119). This yields the solution for $\hat { \mathbf { x } } _ { m - 2 } ^ { m }$ and $\hat {  { \mathbf { u } } } _ { m - 2 } ^ { m }$ and the associated covariance matrices. This procedure is repeated until the initial stage is reached.

Hence, the procedure is continued recursively by applying orthogonal transformations so that

$$
\begin{array} { r l r } { T _ { k - 1 } ^ { * } } &  \left[ \begin{array} { l } { \overline { { R } } _ { u _ { k } } \overline { { R } } _ { u x _ { k } } \Gamma ( t _ { k } , t _ { k - 1 } ) } \\ { \overline { { R _ { k } ^ { * } \Gamma ( t _ { k } , t _ { k - 1 } ) } } \quad \left| \begin{array} { l } { \overline { { R } } _ { u x _ { k } } \Phi ( t _ { k } , t _ { k - 1 } ) } \\ { \boldsymbol { R } _ { k } ^ { * } \Phi ( t _ { k } , t _ { k - 1 } ) } \end{array} \right| \begin{array} { l } { \widetilde { \mathbf { b } } _ { u _ { k } } } \\ { \mathbf { b } _ { k } ^ { * } } \end{array} \right] } & \\ & { = \left[ \begin{array} { l l } { R _ { u _ { k - 1 } } ^ { * } R _ { u x _ { k - 1 } } ^ { * } \mathbf { b } _ { u _ { k - 1 } } ^ { * } } \\ { 0 \qquad R _ { k - 1 } ^ { * } \mathbf { b } _ { k - 1 } ^ { * } } \end{array} \right] } & { ( 5 . } \end{array} \end{array}
$$

where R∗uk−1 and $R _ { k - 1 } ^ { * }$ are upper triangular. The smoothed solution is given by

$$
\begin{array} { r l } & { \quad R _ { k - 1 } ^ { * } \hat { \mathbf { x } } _ { k - 1 } ^ { m } = \mathbf { b } _ { k - 1 } ^ { * } } \\ & { \quad R _ { u _ { k - 1 } } ^ { * } \hat { \mathbf { u } } _ { k - 1 } ^ { m } = \mathbf { b } _ { u _ { k - 1 } } ^ { * } - R _ { u x _ { k - 1 } } ^ { * } \hat { \mathbf { x } } _ { k - 1 } ^ { m } . } \end{array}
$$

The smoothed covariance is given by

$$
\begin{array} { r l } & { P _ { x _ { k - 1 } } ^ { m } = R _ { k - 1 } ^ { * } - 1 \ R _ { k - 1 } ^ { * - T } } \\ & { P _ { u _ { k - 1 } } ^ { m } = R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u _ { k - 1 } } ^ { * - T } } \\ & { \quad \quad \quad + R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u x _ { k - 1 } } ^ { * } R _ { k - 1 } ^ { * - 1 } R _ { k - 1 } ^ { * - T } R _ { u x _ { k - 1 } } ^ { * T } R _ { u _ { k - 1 } } ^ { * - T } } \end{array}
$$

$$
P _ { u x _ { k - 1 } } ^ { m } = - R _ { u _ { k - 1 } } ^ { * - 1 } R _ { u x _ { k - 1 } } ^ { * } R _ { k - 1 } ^ { * - 1 } R _ { k - 1 } ^ { * - T } .
$$

The first row of the left-hand side of Eq. (5.10.120) is saved from the filtering solution and the second row is computed as part of the smoothing procedure.

# 5.11 PROCESS NOISE PARAMETER FILTERING/ SMOOTHING USING A SRIF

Along with the dynamic state parameters, it is often advantageous to include some other types of parameters in filtering satellite data to improve the solution. In this section we expand the results of the previous section to include in the state vector, bias parameters, and exponentially correlated process noise parameters. These additional parameters will be defined as

c : Bias parameters (constant acceleration parameters, ephemeris corrections, station coordinates, etc.)   
p : Correlated process noise parameters; many random or unmodeled phenomena can be approximated quite well with fir st order exponentially correlated process noise, also referred to as a Gauss-Markov Process and sometimes as colored noise. Variables that commonly are modeled as a Gauss-Markov Process include

Solar radiation pressure Mismodeled drag effects Leaky attitude control systems Moving station positions Polar motion parameters Clock errors Atmospheric path delays Earth rotation parameters

The recursive equation for mapping a discrete first order exponentially correlated process is (Tapley and Ingram, 1973; Bierman, 1977)

$$
\mathbf { p } _ { k + 1 } = M _ { k + 1 } \mathbf { p } _ { k } + \mathbf { w } _ { k } .
$$

$M$ is the process noise parameter transition matrix and is assumed diagonal, with diagonals, $m$ , given by

$$
m = e ^ { - ( t _ { k + 1 } - t _ { k } ) / \tau }
$$

where $\tau$ is the time constant of the process and represents how correlated a process noise parameter is from one time step to the next. The extremes for $\tau$ are related to $m$ as follows:

$$
{ \begin{array} { r l r l r l } { \tau  0 } & { ~  ~ } & { m  0 } & & { ~ { \mathrm { ~ W h i t e ~ n o i s e } } } \\ & { } & & { } & & { ( { \mathrm { n o t ~ c o r r e l a t e d ~ a t ~ a l l ~ i n ~ t i m e } } ) } \\ { \tau  \infty } & { ~  ~ } & { m  1 } & & { ~ { \mathrm { R a n d o m ~ w a l k ~ ( n o ~ s t e a d y ~ s t a t e , ~ } } } \end{array} }
$$

w is called the process noise (not the same as $\mathbf { p }$ ) with

$$
E \left[ \mathbf { w } _ { j } \right] = \overline { { \mathbf { w } } } _ { j } .
$$

In almost all applications, the $a$ priori estimate of $\overline { { \mathbf { w } } } _ { j }$ is zero, but this is not a necessary assumption for this development.

Next

$$
E [ ( \mathbf { w } _ { j } - \overline { { \mathbf { w } } } _ { j } ) ( \mathbf { w } _ { k } - \overline { { \mathbf { w } } } _ { k } ) ^ { T } ] = Q \delta _ { j k }
$$

and

$$
Q = R _ { w } ^ { - 1 } R _ { w } ^ { - T }
$$

where $Q$ is the process noise covariance and is diagonal with elements

$$
q _ { i } = ( 1 - m _ { i } ^ { 2 } ) \sigma _ { i } ^ { 2 } .
$$

The variance corresponding to the particular process noise parameter $p _ { i }$ is $\sigma _ { i } ^ { 2 }$ . The SRIF formulation of Section 5.10 can be adapted to handle bias parameters and first order exponentially correlated noise (Bierman, 1977). The state propogation equations are represented by

$$
\begin{array}{c} \begin{array} { r } { \mathbf { \tilde { \rho } } { \bf \Xi } } \\ { \mathbf { x } } \\ { \mathbf { c } { \bf \Xi } } \\ { { \bf \Xi } { \bf { c } } { \bf \Xi } } \end{array} = \left[ \begin{array} { l l l } { M } & { 0 } & { 0 } \\ { \Phi _ { p } \Phi _ { x } \Phi _ { c } } \\ { 0 } & { 0 } & { I } \end{array} \right] _ { k + 1 } \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] _ { k } + \left[ \begin{array} { l } { \mathbf { w } _ { k } } \\ { 0 } \\ { 0 } \end{array} \right]  \end{array}
$$

where $\Phi _ { p } , \Phi _ { x }$ , and $\Phi _ { c }$ are state transition matrices that map perturbations in $\mathbf { p } , \mathbf { x }$ , and $\mathbf { c }$ at $t _ { k }$ into perturbations in $\mathbf { x }$ at $t _ { k + 1 }$ . If we define

$$
\mathbf { X } _ { k + 1 } \equiv { \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] } _ { k + 1 }
$$

$$
\Phi ( t _ { k + 1 } , t _ { k } ) \equiv \left[ { \begin{array} { c c c } { M \ 0 } & { 0 } \\ { \Phi _ { p } \ \Phi _ { x } \ \Phi _ { c } } \\ { 0 } & { 0 } & { I } \end{array} } \right] _ { k + 1 }
$$

$$
\Gamma ( t _ { k + 1 } , t _ { k } ) \equiv { \Bigg [ } { \begin{array} { l } { I } \\ { 0 } \\ { 0 } \end{array} } { \Bigg ] } ~ ,
$$

Eq. (5.11.7) may be written as

$$
{ \bf X } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) { \bf X } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) { \bf w } _ { k }
$$

which is identical to Eq. (5.10.45). Hence the algorithms of Section 5.10.2 may be applied directly to this problem. In actual practice, however, it is customary to reduce computations by taking advantage of the fact that some parameters are constant and the process noise parameters are modeled as a Gauss-Markov Process (Bierman, 1977).

# 5.11.1 EXPONENTIALLY CORRELATED PROCESS NOISE SRIF

Recall that for a SRIF, $R$ (the square root of the information matrix, $\Lambda$ ) is operated on for the measurement and time update rather than the covariance matrix, $P$ , where

$$
P = \Lambda ^ { - 1 } = R ^ { - 1 } R ^ { - T } .
$$

By keeping $R$ upper triangular through orthogonal transformations, the state deviation estimate, $\hat { \bf x }$ , in a standard SRIF is found by simple back substitution and is given by

$$
\hat { \mathbf { x } } = R ^ { - 1 } \mathbf { b } .
$$

We will derive the filter/s moother equations for the SRIF with bias parameters and process noise parameters shown explicitly. This will be accomplished by deriving and minimizing a least squares performance index.

As shown by Eq. (5.11.1), the recursive equation for a first-order exponentially correlated process is

$$
\mathbf { p } _ { k } = M _ { k } \mathbf { p } _ { k - 1 } + \mathbf { w } _ { k - 1 } .
$$

Assume that $a$ priori information for $\mathbf { w } _ { k - 1 }$ is given by $\overline { { \mathbf { w } } } _ { k - 1 }$ . Generally it is assumed that $\overline { { \bf w } } = 0$ at each stage. Assume that the error in $\overline { { \mathbf { w } } } _ { k - 1 }$ has zero mean (i.e., $\overline { { \mathbf { w } } } _ { k - 1 }$ is the mean value of $\mathbf { w } _ { k - 1 }$ ) and covariance $Q$ . Thus,

$$
\overline { { \mathbf { w } } } _ { k - 1 } = \mathbf { w } _ { k - 1 } + \boldsymbol { \gamma } _ { k - 1 }
$$

where $\mathbf { w } _ { k - 1 }$ is the true value and $\gamma _ { k - 1 }$ is the error in $\overline { { \mathbf { w } } } _ { k - 1 }$ . Hence,

$$
E [ \gamma _ { k - 1 } ] = 0 , E [ \gamma _ { k - 1 } \gamma _ { k - 1 } ^ { T } ] = Q .
$$

We will assume that $\gamma$ is uncorrelated in time so that

$$
E [ \gamma _ { k } \gamma _ { j } ^ { T } ] = Q \delta _ { k j } .
$$

As stated in Eq. (5.11.5), define the square root of $Q$ as

$$
\begin{array} { r } { R _ { w } ^ { - 1 } R _ { w } ^ { - T } = Q . } \end{array}
$$

Substituting $\mathbf { w } _ { k - 1 }$ from Eq. (5.11.13) into Eq. (5.11.14) and multiplying by $R _ { w }$ yields a data equation for $\mathbf { w } _ { k - 1 }$ ,

$$
R _ { w } \overline { { \mathbf { w } } } _ { k - 1 } \equiv \overline { { \mathbf { b } } } _ { w _ { k - 1 } } = R _ { w } \big ( \mathbf { p } _ { k } - M _ { k } \mathbf { p } _ { k - 1 } \big ) + R _ { w } \gamma _ { k - 1 }
$$

or

$$
\overline { { { \bf b } } } _ { w _ { k - 1 } } = R _ { w } ( { \bf p } _ { k } - M _ { k } { \bf p } _ { k - 1 } ) + \overline { { \gamma } } _ { k - 1 }
$$

where

$$
E \left[ \overline { { \gamma } } _ { k - 1 } \right] = R _ { w } E \left[ \gamma _ { k - 1 } \right] = 0 \mathrm { a n d } E \left[ \overline { { \gamma } } _ { k - 1 } \overline { { \gamma } } _ { k - 1 } ^ { T } \right] = I .
$$

Assume further that at $t _ { k - 1 }$ we have a priori information arrays $[ \overline { { R } } _ { p } \ \overline { { \mathbf { b } } } _ { p } ] _ { k - 1 }$ , $[ \overline { { { R } } } _ { x } \ \overline { { { \bf b } } } _ { x } ] _ { k - 1 }$ , and $[ \overline { { R } } _ { c } \ \overline { { \mathbf { b } } } _ { c } ] _ { k - 1 }$ for $\mathbf { p } , \mathbf { x }$ , and $\mathbf { c }$ , respectively. Assume that an observation is available at $t _ { k - 1 }$ given by

$$
y _ { k - 1 } = [ H _ { p } H _ { x } H _ { c } ] _ { k - 1 } \left[ \mathbf { x } \right] _ { k - 1 } + \epsilon _ { k - 1 }
$$

where the observations have been prewhitened so that $\epsilon$ has zero means and unit variance.

Recall that the a priori information on $\mathbf { p } , \mathbf { x }$ , and c may be written in the form of a data equation. For example, the $a$ priori value, $\overline { { \mathbf { p } } } _ { k - 1 }$ , may be written in terms of the true value, $\mathbf { p } _ { k - 1 }$ , and the error, $\eta _ { p _ { k - 1 } }$ , as

$$
\overline { { \mathbf { p } } } _ { k - 1 } = \mathbf { p } _ { k - 1 } + \boldsymbol { \eta } _ { p _ { k - 1 } }
$$

where

$$
E \left[ \pmb { \eta } _ { p _ { k - 1 } } \right] = 0 \mathrm { a n d } E \left[ \pmb { \eta } _ { p } \pmb { \eta } _ { p } ^ { T } \right] _ { k - 1 } = \overline { { P } } _ { p _ { k - 1 } }
$$

and

$$
\overline { { { P } } } _ { p _ { k - 1 } } = ( \overline { { { R } } } _ { p } ^ { - 1 } \overline { { { R } } } _ { p } ^ { - T } ) _ { k - 1 } .
$$

Then the desired data equation is given by multiplying Eq. (5.11.21) by $\overline { { R } } _ { p _ { k - 1 } }$

$$
\left( \overline { { { R } } } _ { p } \ \overline { { { \bf p } } } \right) _ { k - 1 } \equiv \overline { { { \bf b } } } _ { p _ { k - 1 } } = \left( \overline { { { R } } } _ { p } \ { \bf p } \right) _ { k - 1 } + \overline { { { \eta } } } _ { p _ { k - 1 } }
$$

where $\overline { { \eta } } _ { p _ { k - 1 } }$ has zero mean and unit covariance. Similar data equations can be written to represent the a priori information for $\mathbf { x }$ and $\mathbf { c }$ at $t _ { k - 1 }$ .

Given the a priori information and the observation at $t _ { k - 1 }$ we wish to determine the corresponding filter values of $\mathbf { p } , \mathbf { x }$ , and c. The desired algorithm can be developed by minimizing the least squares performance index given by

$$
\hat { J } _ { k - 1 } \equiv \left\| \overline { { \eta } } _ { p _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \eta } } _ { x _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \eta } } _ { c _ { k - 1 } } \right\| ^ { 2 } + \left\| \overline { { \gamma } } _ { k - 1 } \right\| ^ { 2 } + \left( \epsilon _ { k - 1 } \right) ^ { 2 } .
$$

Equation (5.11.25), which corresponds to the measurement update at $t _ { k - 1 }$ , may be written as (see Eqs. (5.11.18), (5.11.20), (5.11.24))

$$
\begin{array} { r l r } & { } & { \hat { J } _ { k - 1 } = \left\| \overline { { R } } _ { p } \mathbf { p } - \overline { { \mathbf { b } } } _ { p } \right\| _ { k - 1 } ^ { 2 } + \left\| \overline { { R } } _ { x } \mathbf { x } - \overline { { \mathbf { b } } } _ { x } \right\| _ { k - 1 } ^ { 2 } + \left\| \overline { { R } } _ { c } \mathbf { c } - \overline { { \mathbf { b } } } _ { c } \right\| _ { k - 1 } ^ { 2 } } \\ & { } & { + \left\| { R } _ { w } ( \mathbf { p } _ { k } - M _ { k } \mathbf { p } _ { k - 1 } ) - \overline { { \mathbf { b } } } _ { w _ { k - 1 } } \right\| ^ { 2 } } \\ & { } & { + \left( \left[ H _ { p } \ H _ { x } \ H _ { x } \right] \left[ \mathbf { p } \right] _ { k } - y \right) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Because we may choose $\mathbf { p } _ { k }$ to zero the next-to-last term in Eq. (5.11.26), we do not have to deal with it until we do the time update to $t _ { k }$ . We may write $\hat { J } _ { k - 1 }$ as

$$
\begin{array} { r } { \hat { J } _ { k - 1 } = \left. \left[ \begin{array} { l l l } { \overline { { R } } _ { p } } & { 0 } & { 0 } \\ { 0 } & { \overline { { R } } _ { x } } & { 0 } \\ { 0 } & { 0 } & { \overline { { R } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] - \left[ \begin{array} { l } { \mathbf { \overline { { b } } } _ { p } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \\ { y } \end{array} \right] \right. _ { k - 1 } ^ { 2 } } \\ { + \left. R _ { w } ( \mathbf { p } _ { k } - M _ { k } \mathbf { \textbf { p } } _ { k - 1 } ) - \mathbf { \overline { { b } } } _ { w _ { k - 1 } } \right. ^ { 2 } . } \end{array}
$$

Applying a series of orthogonal transformations to the first term of Eq. (5.11.27) yields

$$
T _ { k - 1 } \left[ \begin{array} { c c c c } { \overline { { { R } } } _ { p } } & { 0 } & { 0 } & { \overline { { { \mathbf b } } } _ { p } } \\ { 0 } & { \overline { { { R } } } _ { x } } & { 0 } & { \overline { { { \mathbf b } } } _ { x } } \\ { 0 } & { 0 } & { \overline { { { R } } } _ { c } } & { \overline { { { \mathbf b } } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } & { y } \end{array} \right] _ { k - 1 } = \left[ \begin{array} { c c c c } { \hat { R } _ { p } } & { \hat { R } _ { p x } } & { \hat { R } _ { p c } } & { \hat { \mathbf b } _ { p } } \\ { 0 } & { \hat { R } _ { x } } & { \hat { R } _ { x c } } & { \hat { \mathbf b } _ { x } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } & { \hat { \mathbf b } _ { c } } \\ { 0 } & { 0 } & { 0 } & { e } \end{array} \right] _ { k - 1 }
$$

and Eq. (5.11.27) becomes

$$
\begin{array} { r l } & { \hat { J } _ { k - 1 } = \left\| \left[ \begin{array} { l l l } { \hat { R } _ { p } } & { \hat { R } _ { p x } } & { \hat { R } _ { p c } } \\ { 0 } & { \hat { R } _ { x } } & { \hat { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] - \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} \right] \right\| _ { k - 1 } ^ { 2 } } \\ & { + \left\| R _ { w } \big ( \mathbf { p } _ { k } - M _ { k } \mathbf { \ p } _ { k - 1 } \big ) - \overline { { \mathbf { b } } } _ { w _ { k - 1 } } \right\| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

From Eq. (5.11.29) we could solve for $\hat { \mathbf { c } } , \hat { \mathbf { x } }$ , and $\hat { \bf p }$ at the $k - 1 ^ { \mathrm { t h } }$ stage.

We now perform the time update of $\hat { J } _ { k - 1 }$ in order to obtain $\overline { { J } } _ { k }$ . To accomplish this we need to replace $\mathbf { x } _ { k - 1 }$ with $\mathbf { x } _ { k }$ . Notice that our performance index already contains $\mathbf { p } _ { k }$ and we will leave $\mathbf { p } _ { k - 1 }$ in the performance index. This will conveniently yield the smoothed value of $\mathbf { p } _ { k - 1 }$ .

From Eq. (5.11.7)

$$
\mathbf { x } _ { k } = \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } + \Phi _ { x } ( k ) \mathbf { x } _ { k - 1 } + \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 }
$$

or

$$
\mathbf { x } _ { k - 1 } = \Phi _ { x } ^ { - 1 } ( k ) \left[ \mathbf { x } _ { k } - \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } - \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 } \right]
$$

where

$$
\Phi ( k ) \equiv \Phi ( t _ { k } , t _ { k - 1 } ) .
$$

Also, ${ \bf c } _ { k - 1 } ~ = ~ { \bf c } _ { k }$ , since $\mathbf { c }$ is a constant. Substituting Eq. (5.11.31) into Eq. (5.11.29) yields the following equations

$$
\hat { R } _ { p } \mathbf { p } _ { k - 1 } + \overline { { R } } _ { p x } \left[ { \bf x } _ { k } - \Phi _ { p } ( k ) \mathbf { p } _ { k - 1 } - \Phi _ { c } ( k ) \mathbf { c } _ { k - 1 } \right] + \hat { R } _ { p c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { p _ { k - 1 } }
$$

$$
\overline { { { R } } } _ { x } \left[ \mathbf { x } _ { k } - \boldsymbol { \Phi } _ { p } ( k ) \mathbf { p } _ { k - 1 } - \boldsymbol { \Phi } _ { c } ( k ) \mathbf { c } _ { k - 1 } \right] + \hat { R } _ { x c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { x _ { k - 1 } }
$$

$$
\hat { R } _ { c } \mathbf { c } _ { k - 1 } = \hat { \mathbf { b } } _ { c _ { k - 1 } } .
$$

Also,

$$
R _ { w } ( { \bf p } _ { k } - M _ { k } \mathrm { \bf ~ p } _ { k - 1 } ) = \overline { { { \bf b } } } _ { w _ { k - 1 } }
$$

where

$$
\begin{array} { r } { \overline { { R } } _ { p x } \equiv \hat { R } _ { p x } \Phi _ { x } ^ { - 1 } ( k ) } \\ { \overline { { R } } _ { x } \equiv \hat { R } _ { x } \Phi _ { x } ^ { - 1 } ( k ) . } \end{array}
$$

By regrouping and writing in matrix form (while noting that $\mathbf { c } _ { k - 1 } = \mathbf { c } _ { k }$ ), we may write Eq. (5.11.29) as

$$
\hat { J } _ { k - 1 } = \| [ \begin{array} { c c c c c } { - R _ { w } M _ { k } } & { R _ { w } } & { 0 } & { 0 } \\ { ( \hat { R } _ { p } - \overline { { R } } _ { p x } \Phi _ { p } ( k ) ) } & { 0 } & { \overline { { R } } _ { p x } } & { ( \hat { R } _ { p c } - \overline { { R } } _ { p x } \Phi _ { c } ( k ) ) } \\ { - \overline { { R } } _ { x } \Phi _ { p } ( k ) } & { 0 } & { \overline { { R } } _ { x } } & { ( \hat { R } _ { x c } - \overline { { R } } _ { x } \Phi _ { c } ( k ) ) } \\ { 0 } & { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} ] _ { k - 1 }
$$

$$
\begin{array} { r l } & { [ \mathbf { p } _ { k - 1 } ] } \\ & { [ \begin{array} { l } { \mathbf { p } _ { k } } \\ { \mathbf { x } _ { k } } \\ { \mathbf { c } _ { k } } \end{array} ] - [ \begin{array} { l } { \overline { { \mathbf { b } } } _ { w } } \\ { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} ] _ { k - 1 }  ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Applying a series of orthogonal transformations to upper triangularize the first term in Eq. (5.11.33) yields the time update

$$
\begin{array} { r l } & { \overline { { J } } _ { k } = \left. \left[ \begin{array} { c c c c } { R _ { p } ^ { * } } & { R _ { p p } ^ { * } } & { R _ { p x } ^ { * } } & { R _ { p c } ^ { * } } \\ { 0 } & { \overline { { R } } _ { p p } ^ { * } } & { \overline { { R } } _ { p x } } & { \overline { { R } } _ { p c } ^ { * } } \\ { 0 } & { 0 } & { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { 0 } & { 0 } & { \overline { { R } } _ { c } } \end{array} \right] _ { k } \left[ \begin{array} { c } { \mathbf { p } _ { k - 1 } } \\ { \mathbf { p } _ { k } } \\ { \mathbf { x } _ { k } } \\ { \mathbf { c } _ { k } } \end{array} \right] } \\ & { \qquad - \left[ \begin{array} { c } { \mathbf { b } _ { p } ^ { * } } \\ { \mathbf { \overline { { b } } } _ { p } ^ { * } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \end{array} \right] _ { k } \right. ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

The $( ) ^ { * }$ quantities are not used for filtering but are necessary if smoothing is to be done following the filter ing. Hence, these quantities must be saved at each stage in the forward (filtering) sweep. Also, because c is a constant, it is unaffected by the mapping from $t _ { k - 1 }$ to $t _ { k }$ and need not be included in the time update procedure,

$$
\left[ \hat { R } _ { c } \hat { \mathbf { b } } _ { c } \right] _ { k - 1 } = \left[ \overline { { R } } _ { c } \overline { { \mathbf { b } } } _ { c } \right] _ { k } .
$$

We may now perform the measurement update on $\overline { { J } } _ { k }$ to obtain $\hat { J } _ { k }$ . This is accomplished by adding $\| \overline { \gamma } _ { k } \| ^ { 2 }$ (see Eq. (5.11.18)) and $( \epsilon _ { k } ) ^ { 2 }$ to $\overline { { J } } _ { k }$ given by Eq.

(5.11.34). Hence,

$$
\begin{array} { r } { \hat { J } _ { k } = \left\| \left[ \begin{array} { l l l } { \overline { { R } } _ { p } } & { \overline { { R } } _ { p x } } & { \overline { { R } } _ { p c } } \\ { 0 } & { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { 0 } & { \overline { { R } } _ { c } } \\ { H _ { p } } & { H _ { x } } & { H _ { c } } \end{array} \right] _ { k } \left[ \begin{array} { l } { \mathbf { p } } \\ { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] _ { k } - \left[ \begin{array} { l } { \mathbf { \overline { { b } } } _ { p } } \\ { \mathbf { \overline { { b } } } _ { x } } \\ { \mathbf { \overline { { b } } } _ { c } } \\ { y } \end{array} \right] _ { k } \right\| ^ { 2 } } \\ { + \left\| \boldsymbol { R } _ { p _ { k } } ^ { * } \mathbf { p } _ { k - 1 } + \boldsymbol { R } _ { p p _ { k } } ^ { * } \mathbf { p } _ { k } + \boldsymbol { R } _ { p x _ { k } } ^ { * } \mathbf { x } _ { k } + \boldsymbol { R } _ { p c _ { k } } ^ { * } \mathbf { c } _ { k } - \mathbf { b } _ { p _ { k } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| \boldsymbol { R } _ { w } ( \mathbf { p } _ { k + 1 } - \boldsymbol { M } _ { k + 1 } \mathbf { p } _ { k } ) - \mathbf { \overline { { b } } } _ { w _ { k } } \right\| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } . } \end{array}
$$

Once again we can null the third term, $\| \overline { \gamma } _ { k } \|$ , by proper choice of $\mathbf { p } _ { k + 1 }$ ; hence, we do not have to deal with this term until we perform the time update to $t _ { k + 1 }$ . Notice that we can choose $\mathbf { p } _ { k - 1 }$ to null the second term. Later we will see that this is the smoothed value of $\mathbf { p } _ { k - 1 }$ .

A series of orthogonal transformations is now applied to Eq. (5.11.36) to yield

$$
\begin{array} { r l } & { { \hat { J } } _ { k } = \| [ \begin{array} { l l } { { \hat { R } } _ { p } \ { \hat { R } } _ { p x } \ { \hat { R } } _ { p c } } \\ { 0 \ } & { { \hat { R } } _ { x } \ { \hat { R } } _ { x c } } \\ { 0 \ } & { 0 \ } & { { \hat { R } } _ { c } } \end{array} ] [ \mathbf { c } ] - [ \begin{array} { l } { \mathbf { \hat { b } } _ { p } } \\ { \mathbf { \hat { b } } _ { x } } \\ { \mathbf { \hat { b } } _ { c } } \end{array} ] \| _ { k } ^ { 2 } } \\ & { \quad \quad \quad + \| R _ { p _ { k } } ^ { * } \mathbf { p } _ { k - 1 } + R _ { p p _ { k } } ^ { * } \mathbf { p } _ { k } + R _ { p x _ { k } } ^ { * } \mathbf { x } _ { k } + R _ { p c _ { k } } ^ { * } \mathbf { c } _ { k } - \mathbf { b } _ { p _ { k } } ^ { * } \| ^ { 2 } } \\ & { \quad \quad + \| R _ { w } ( \mathbf { p } _ { k + 1 } - M _ { k + 1 } \mathbf { p } _ { k } ) - \mathbf { \bar { b } } _ { w _ { k } } \| ^ { 2 } + ( e ) _ { k - 1 } ^ { 2 } + ( e ) _ { k } ^ { 2 } . } \end{array}
$$

This procedure of time and measurement updates is carried out until the desired number of observations has been processed.

After the $N ^ { \mathrm { t h } }$ measurement update the performance index is given by

$$
\begin{array}{c} \begin{array} { l } { { \hat { J } } _ { N } = \Sigma _ { N - 1 } + \left\| { \boldsymbol { R } } _ { p _ { N } } ^ { * } { \bf { p } } _ { N - 1 } + { \boldsymbol { R } } _ { p p _ { N } } ^ { * } { \bf { p } } _ { N } + { \boldsymbol { R } } _ { p x _ { N } } ^ { * } { \bf { x } } _ { N } + { \boldsymbol { R } } _ { p c _ { N } } ^ { * } { \bf { c } } _ { N } - { \bf { b } } _ { p _ { N } } ^ { * } \right\| ^ { 2 } } \\ { + \left\| \left[ \begin{array} { l } { { \hat { \boldsymbol { R } } } _ { p } \hat { \boldsymbol { R } } _ { p x } \hat { \boldsymbol { R } } _ { p c } } \\ { 0 \hat { \boldsymbol { R } } _ { x } \hat { \boldsymbol { R } } _ { x c } } \\ { 0 \ } & { \hat { \boldsymbol { R } } _ { c } } \end{array} \right] _ { N } \left[ { \bf { s } } _ { N } \right] - \left[ \hat { \bf { b } } _ { x }  \right\right\} \\ { { \bf { \hat { b } } } _ { c } } \end{array}] _ { N } | ^ { 2 }  \\ { + \displaystyle \sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 } } \end{array}
$$

where

$$
\Sigma _ { N - 1 } \equiv \sum _ { i = 1 } ^ { N - 1 } \| R _ { p _ { i } } ^ { * } \mathbf { p } _ { i - 1 } + R _ { p p _ { i } } ^ { * } \mathbf { p } _ { i } + R _ { p x _ { i } } ^ { * } \mathbf { x } _ { i } + R _ { p c _ { i } } ^ { * } \mathbf { c } _ { i } - \mathbf { b } _ { p _ { i } } ^ { * } \| ^ { 2 } .
$$

The best estimate of the state at $t _ { N }$ is obtained from

$$
\hat { \mathbf { X } } _ { N } = \hat { R } _ { N } ^ { - 1 } \hat { \mathbf { b } } _ { N }
$$

where

$$
\begin{array} { r l } & { \hat { \mathbf { X } } _ { N } \equiv \left[ \hat { \mathbf { p } } \right] } \\ & { ~ \hat { \mathbf { X } } _ { N } \equiv \left[ \begin{array} { l } { \hat { \mathbf { p } } } \\ { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right] _ { N } , ~ \hat { R } _ { N } \equiv \left[ \begin{array} { l l } { \hat { R } _ { p } \hat { R } _ { p x } \hat { R } _ { p c } } \\ { 0 } & { \hat { R } _ { x } \hat { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right] _ { N } } \\ & { ~ \hat { \mathbf { b } } _ { N } \equiv \left[ \begin{array} { l } { \hat { \mathbf { b } } _ { p } } \\ { \hat { \mathbf { b } } _ { x } } \\ { \hat { \mathbf { b } } _ { c } } \end{array} \right] _ { N } . } \end{array}
$$

The filter covariance is given by

$$
\begin{array} { r } { P _ { N } = R _ { N } ^ { - 1 } \ R _ { N } ^ { - T } . } \end{array}
$$

Since $\hat { R } _ { N }$ is upper triangular, $\hat { \mathbf { X } } _ { N }$ is obtained directly from a back substitution described by Eq. (5.2.8). If $\hat { P } _ { N } , \hat { \mathbf { x } } _ { N }$ , and $\hat { \mathbf { c } } _ { N }$ are used in the second term of Eq. (5.11.38), the smoothed value of $P _ { N - 1 }$ may be obtained. Note that it is not necessary to retain the first two terms of ${ \hat { J } } _ { N } $ if smoothing is not used.

# 5.11.2 SMOOTHING WITH A SRIF

Smoothing can now be done using Eq. (5.11.38) and the values of $\hat { \mathbf { X } } _ { N }$ given by Eq. (5.11.40). From the second term of Eq. (5.11.38) we have the smoothed value of $\mathbf { p } _ { N - 1 }$ based on $N$ measurements

$$
\hat { \mathbf { p } } _ { N - 1 } ^ { N } = { R _ { p } ^ { * } } _ { N } ^ { - 1 } \left[ \mathbf { b } _ { p } ^ { * } - { R _ { p } ^ { * } } _ { p } \hat { \mathbf { p } } _ { N } - { R _ { p x } ^ { * } } _ { N } - { R _ { p c } ^ { * } } _ { c _ { N } } \hat { \mathbf { c } } _ { N } \right] _ { N } .
$$

The smoothed value of $\mathbf { x } _ { N - 1 }$ is obtained from Eq. (5.11.31)

$$
\hat { \mathbf { x } } _ { N - 1 } ^ { N } = \Phi _ { x } ^ { - 1 } ( N ) \left[ \hat { \mathbf { x } } _ { N } - \Phi _ { p } ( N ) \hat { \mathbf { p } } _ { N - 1 } ^ { N } - \Phi _ { c } ( N ) \hat { \mathbf { c } } _ { N - 1 } ^ { N } \right]
$$

and c smooths as a constant,

$$
\hat { \mathbf { c } } _ { N } = \hat { \mathbf { c } } _ { N - 1 } ^ { N } = \hat { \mathbf { c } } _ { i } ^ { N } i = 1 , \ldots , N .
$$

Hence, the general expression for smoothing is given by

$$
\begin{array} { c } { \hat { \mathbf { p } } _ { i } ^ { N } = R _ { p i + 1 } ^ { * } \left[ \mathbf { b } _ { p } ^ { * } - R _ { p p } ^ { * } \hat { \mathbf { p } } _ { i + 1 } ^ { N } - R _ { p x } ^ { * } \hat { \mathbf { x } } _ { i + 1 } ^ { N } - R _ { p c } ^ { * } \hat { \mathbf { c } } _ { N } \right] _ { i + 1 } } \\ { { \phantom { \frac { 1 } { 2 } } } i = N - 1 , \dots , 1 \qquad } \end{array}
$$

where the $( \quad ) ^ { * }$ quantities have been saved at each value of $t _ { i }$ during the fil tering process. Also,

$$
\begin{array} { c } { { \hat { \mathbf { x } } _ { i } ^ { N } = \Phi _ { x } ^ { - 1 } ( i + 1 ) \left[ \hat { \mathbf { x } } _ { i + 1 } ^ { N } - \Phi _ { p } ( i + 1 ) \hat { \mathbf { p } } _ { i } ^ { N } - \Phi _ { c } ( i + 1 ) \hat { \mathbf { c } } _ { N } \right] } } \\ { { { } } } \\ { { i = N - 1 , \ldots , 1 . } } \end{array}
$$

The state transition matrices also are saved during filtering.

Although the procedure just outlined yields the smoothed solutions, it does not yield a smoothed covariance. To obtain the covariance we use the procedure for the filter time update and substitute for $\mathbf { x } _ { N }$ in terms of parameters at the $N - 1 ^ { \mathrm { s t } }$ stage; from Eq. (5.11.30),

$$
\begin{array} { r } { { \bf x } _ { N } = \Phi _ { x } ( N ) { \bf x } _ { N - 1 } + \Phi _ { p } ( N ) { \bf p } _ { N - 1 } + \Phi _ { c } ( N ) { \bf c } _ { N - 1 } . } \end{array}
$$

There is no need to substitute for $\mathbf { p } _ { N }$ because we already have $\mathbf { p } _ { N - 1 }$ available in Eq. (5.11.38) through the use of the data equation for the process noise parameters in the filt er sweep.

Substituting Eq. (5.11.48) into Eq. (5.11.38) yields

$$
\begin{array} { r l } { \hat { J } _ { N _ { 1 } } ^ { N } = } & { \displaystyle { \sum _ { i = 1 } ^ { N } ( e _ { i } ^ { \hbar } ) ^ { \prime } + \sum _ { k = 1 } ^ { N } } } \\ & { + [ [ \begin{array} { l l l } { \displaystyle { R _ { \mathrm { p } } ^ { k } } } & { \displaystyle { R _ { \mathrm { p } } ^ { k } + R _ { \mathrm { p } , i } ^ { \prime } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { R _ { \mathrm { p } , i } ^ { \prime } \Phi _ { \mathrm { x } } ( N ) } } & { \displaystyle { R _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { c } } ( N ) + R _ { \mathrm { i s c } } ^ { \ast } } } \\ { \displaystyle { \hat { R } _ { \mathrm { p } } ^ { k } } } & { \displaystyle { \hat { R } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { p } , i } \Phi _ { \mathrm { x p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { x p } } ( N ) + \hat { T } _ { \mathrm { p } , i } } } \\ { \displaystyle { 0 } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { p } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } } ^ { k } \Phi _ { \mathrm { x } } ( N ) } } & { \displaystyle { \hat { T } _ { \mathrm { s p } , i } \Phi _ { \mathrm { x c } } ( N ) + \hat { T } _ { \mathrm { s c } } } } \\ { \displaystyle { 0 } } & { 0 } & { \displaystyle { 0 } } & { \hat { R } _ { \mathrm { c } } } \end{array} ] } \\ &  \displaystyle  [ \begin{array} { l } { \displaystyle { \mathbb { P } _ { N } } } \\ { \displaystyle { \mathbb { P } _ { N - 1 } ^ { N } } } \\ { \displaystyle { \mathbb { R } _ { N - 1 } ^ { N } } } \\ { \displaystyle { \mathbb { C } _ { N - 1 } ^ { N } } } \end{array} ] - [ \begin{array} { l } { \displaystyle { \mathbb { P } _ { N _ { 1 } } ^ { k } } } \\ { \displaystyle { \mathbb { S } _ { P _ { 1 } } ^ { N } } } \\ { \displaystyle { \mathbb { S } _ { P _ { 1 } } ^ { N } } } \\  \displaystyle  \mathbb  S \end{array} \end{array}
$$

Because the smoothed value of c maps as a constant, we may drop the last row in the preceding matrix and use $\hat { R } _ { c }$ and $\hat { \mathbf { c } } _ { N }$ when needed. Applying a series of orthogonal transformations to the third term yields

$$
\begin{array} { c } { { \displaystyle \hat { J } _ { N - 1 } ^ { N } = \sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 } + \Sigma _ { N - 1 } } } & { { \mathrm { ( S ~ ) } } } \\ { { \displaystyle ~ + \left\| \left[ \begin{array} { l l l } { { \displaystyle { R _ { p p } ^ { \prime } R _ { p } ^ { \prime } R _ { p x } ^ { \prime } R _ { p x } ^ { \prime } R _ { p c } ^ { \prime } } } } & { { \displaystyle { R _ { N - 1 } ^ { \prime } } } } \\ { { \displaystyle { R _ { p } \tilde { R } _ { p x } \tilde { R } _ { p x } \tilde { R } _ { p c } } } } & { { \displaystyle { R _ { N - 1 } \left[ \begin{array} { l } { { \hat { \bf x } _ { N } ^ { N } } } \\ { { \hat { \bf x } _ { N } } } \end{array} \right] } } } & { { \displaystyle { \left[ \begin{array} { l } { { \hat { \bf b } ^ { * \prime } } } \\ { { \bf { b } _ { p } ^ { \prime } } } \\ { { \hat { \bf b } _ { p } } } \\ { { \hat { \bf x } _ { N - 1 } ^ { N } } } \end{array} \right] } } } \end{array} \right] \right\| _ { { \displaystyle \hat { \cal T } _ { N - 1 } } } ^ { 2 } } }  \end{array}
$$

Solving for the state vector that minimizes $\hat { J } _ { N - 1 } ^ { N }$ yields the smoothes solution for the state. We may ignore the $( ) ^ { \prime }$ quantities because we already know the value of $\hat { \mathbf { p } } _ { N } ^ { N } = \hat { \mathbf { p } } _ { N }$ . The desired solution is

$$
\tilde { R } _ { N - 1 } \hat { \mathbf { X } } _ { N - 1 } ^ { N } = \widetilde { \mathbf { b } } _ { N - 1 }
$$

where

$$
\tilde { R } _ { N - 1 } = \left[ \begin{array} { l l l } { \tilde { R } _ { p } \tilde { R } _ { p x } \tilde { R } _ { p c } } \\ { 0 } & { \tilde { R } _ { x } } & { \tilde { R } _ { x c } } \\ { 0 } & { 0 } & { \hat { R } _ { c } } \end{array} \right]
$$

$$
\begin{array} { r } { \hat { \mathbf { X } } _ { N - 1 } ^ { N } = \left[ \hat { \mathbf { p } } _ { N - 1 } ^ { N } \right] , \qquad \hat { \mathbf { b } } _ { N - 1 } = \left[ \overset { \mathbf { \sim } } { \mathbf { b } } _ { p } ^ { \prime } \right] . } \\ { \hat { \mathbf { x } } _ { N - 1 } ^ { N } = \left[ \hat { \mathbf { x } } _ { N - 1 } ^ { N } \right] , \qquad \hat { \mathbf { b } } _ { N - 1 } = \left[ \overset { \mathbf { \sim } } { \mathbf { b } } _ { p } ^ { \prime } \right] . } \end{array}
$$

The smoothed covariance at $t _ { N - 1 }$ is given by

$$
P _ { N - 1 } ^ { N } = \tilde { R } _ { N - 1 } ^ { - 1 } \tilde { R } _ { N - 1 } ^ { - T } .
$$

Recall that the smoothed value of c never changes and is always the final filter value. Because the smoothed value of the state must also satisfy Eq. (5.11.48), we may substitute this into Eq. (5.11.50) in order to determine the smoothed state at $t _ { N - 2 }$ . Keep in mind that while we drop the $( ) ^ { \prime }$ terms, we must now deal with the $N - 1 ^ { \mathrm { s t } }$ term in $\Sigma _ { N - 1 }$ because it depends on the state at $t _ { N - 1 }$ and contains $\mathbf { p } _ { N - 2 }$ . Hence, the performance index $\hat { J } _ { N - 2 } ^ { N }$ becomes

$$
\begin{array} { r l } & { \hat { J } _ { N - 2 } ^ { N } = \Sigma _ { N - 2 } + \left\| \left[ \begin{array} { l l l } { R _ { p } ^ { * } R _ { p p } ^ { * } R _ { p x } ^ { * } R _ { p e } ^ { * } } \\ { 0 } & { \tilde { R } _ { p } } & { \tilde { R } _ { p x } \tilde { R } _ { p e } } \\ { 0 } & { 0 } & { \hat { R } _ { x } } \end{array} \right] _ { N - 1 } \right\| \mathbf { y } _ { N - 1 } } \\ & { \qquad - \left\| \mathbf { b } _ { p } ^ { * } \right\| _ { N } } \\ & { \qquad - \left\| \hat { \mathbf { b } } _ { p } \right\| _ { N - 1 } } \\ & { \qquad \left\| \mathbf { \tilde { b } } _ { x } \right\| _ { N - 1 } } \end{array}
$$

Substituting

$$
{ \bf x } _ { N - 1 } = \Phi _ { x } ( N - 1 ) { \bf x } _ { N - 2 } + \Phi _ { p } ( N - 1 ) { \bf p } _ { N - 2 } + \Phi _ { c } ( N - 1 ) { \bf c } _ { N }
$$

into Eq. (5.11.54) we obtain the $N - 2 ^ { \mathrm { n d } }$ stage of Eq. (5.11.49). Next we apply a series of orthogonal transformations to this equation to obtain the $N - 2 ^ { \mathrm { n d } }$ stage of Eq. (5.11.50). From this we obtain $\hat { \mathbf { X } } _ { N - 2 } ^ { N }$ and the associated covariance matrix. This procedure is repeated until the initial stage is reached. Notice that we have dropped the term

$$
\sum _ { i = 1 } ^ { N } ( e _ { i } ) ^ { 2 }
$$

in Eq. (5.11.54). This is the sum of squares of residuals from the filter sweep and is not affected by smoothing. We do not obtain a smoothed sum of squares of residuals during the backward sweep.

# 5.12 REFERENCES

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

Carlson, N. A., “F ast triangular formulation of the square root filter”, AIAA J., Vol. 11, No. 9, pp. 1239–1265, September 1973.

Dyer, P., and S. McReynolds, “Extension of square-root fil tering to include process noise”, J. Optim. Theory Appl., Vol. 3, No. 6, pp. 444–458, 1969.

Gentleman, W. M., “Least squares computations by Givens transformations without square roots”, J. Inst. Math. Applic., Vol. 12, pp. 329–336, 1973.

Givens, W., “Computation of plane unitary rotations transforming a general matrix to triangular form,” J. Appl. Math., Vol. 6, pp. 26–50, 1958.

Golub, G. H., and C. F. Van Loan, Matrix Computations, Johns Hopkins University Press, 1996.

Graybill, F. A., An Introduction to Linear Statistical Models , Volume I, McGraw-Hill Series in Probability and Statistics, McGraw-Hill, New York, 1961.

Householder, A. S., “Unitary triangularization of a nonsymmetric matrix,” J. Assoc. Comput. Mach., Vol. 5, No. 4, pp. 339–342, October 1958.

Kaminski, P. G., A. E. Bryson, and S. F. Schmidt, “Discrete square root fil tering: A survey of current techniques”, Trans. Auto. Cont., Vol. AC-16, No. 6, pp. 727–735, 1971.

Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

Tapley, B. D., and C. Y. Choe, “An algorithm for propagating the square root covariance matrix in triangular form,” Trans. Auto. Cont., Vol. AC-21, pp. 122–123, 1976.

Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations,” Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369–373, August, 1973.

Tapley, B. D., and J. G. Peters, “A sequential estimation algorithm using a continuous $U D U ^ { T }$ covariance factorization,” J. Guid. Cont., Vol. 3, No. 4, pp. 326–331, July–August 1980.

Thornton, Thornton, C. L., Triangular covariance factorizations for Kalman filtering, Technical Memorandum, 33–798, Jet Propulsion Laboratory, Pasadena, CA, October 15, 1976.

# 5.13 EXERCISES

1. In Section 5.2 the algorithm for $\hat { x }$ is derived assuming the factorization

$$
M = R ^ { T } R
$$

(a) Rederive the algorithm assuming the factorization

$$
M = R R ^ { T }
$$

where $R$ is $n \times n$ upper triangular and

$$
\begin{array} { c } { M \hat { x } = N } \\ { R R ^ { T } \hat { x } = N } \\ { z \equiv R ^ { T } \hat { x } } \\ { R z = N . } \end{array}
$$

Answer:

$$
\begin{array} { r l } & { z _ { i } = \frac { \displaystyle ( N _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } z _ { j } } { R _ { i i } } \quad i = n , n - 1 . . . 1 } \\ & { \displaystyle \hat { x } _ { i } = \frac { \displaystyle ( z _ { i } - \sum _ { j = 1 } ^ { i - 1 } R _ { j i } \hat { x } _ { j } ) } { R _ { i i } } \quad } \\ & { \hat { x } _ { i } = \frac { R _ { i i } } { R _ { i i } } \quad i = 1 , 2 . . . n . } \end{array}
$$

2. Verify that the algorithm for $R$ in Exercise 1 is given by

$$
\begin{array} { l } { { \displaystyle R _ { j j } = \left( M _ { j j } - \sum _ { k = j + 1 } ^ { n } R _ { j k } ^ { 2 } \right) ^ { 1 / 2 } ~ j = n , n - 1 , \ldots 1 } } \\ { { \displaystyle R _ { i j } = \frac { \left( M _ { i j } - \sum _ { k = j + 1 } ^ { n } R _ { i k } R _ { j k } \right) } { R _ { j j } } ~ i = j - 1 , \ldots 1 } } \end{array}
$$

3. Using Eq. (5.2.6), find $R$ for

(a) The matrix $M$ given by

$$
M = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { 3 } \\ { 2 } & { 8 } & { 2 } \\ { 3 } & { 2 } & { 1 4 } \end{array} } \right] .
$$

(b) Compute $R$ using the algorithm derived in Exercise 2. Note that these will be different matrices, thus illustrating the nonuniqueness of the matrix square root.

Answers:

Part (a)

$$
R = { \left[ 0 2 - 2 \right] }
$$

Part (b)

$$
R = \left[ \begin{array} { c c c } { { \displaystyle \frac { 1 } { 3 \sqrt { 3 } } \frac { 1 1 } { 3 \sqrt { 4 2 } } \frac { 3 } { \sqrt { 1 4 } } } } \\ { { 0 } } & { { 3 \sqrt { \frac { 6 } { 7 } } \frac { 2 } { \sqrt { 1 4 } } } } \\ { { 0 } } & { { 0 } } & { { \sqrt { 1 4 } } } \end{array} \right]
$$

4. Use the square root free Cholesky algorithm (Eqs. (5.2.11) and (5.2.12)) to determine the $U$ and $D$ factors of $M$ for problem 3,

$$
M = U D U ^ { T } .
$$

Answer:

$$
U = { \left[ \begin{array} { l l } { 1 { \frac { 1 1 } { 5 4 } } { \frac { 3 } { 1 4 } } } \\ { 0 \ 1 } & { { \frac { 1 } { 7 } } } \\ { 0 \ 0 } & { 1 } \end{array} \right] }
$$

$$
D = { \left[ \begin{array} { l l l } { { \frac { 1 } { 2 7 } } } & { 0 } & { 0 } \\ { 0 } & { { \frac { 5 4 } { 7 } } } & { 0 } \\ { 0 } & { 0 } & { 1 4 } \end{array} \right] }
$$

5. Given the function

$$
f ( t ) = \sum _ { i = 0 } ^ { 4 } a _ { i } t ^ { i } + \sum _ { i = 1 } ^ { 4 } A _ { i } \cos ( \omega _ { i } t ) + B _ { i } \sin ( \omega _ { i } t )
$$

where

$$
\begin{array} { r } { \omega _ { 1 } = \frac { 2 \pi } { 7 0 9 } , \quad \omega _ { 2 } = \frac { 2 \pi } { 3 8 3 } , \quad \omega _ { 3 } = \frac { 2 \pi } { 1 0 7 } , \quad \omega _ { 4 } = \frac { 2 \pi } { 1 3 } } \end{array}
$$

and given measurements of $f$ for $t = 0 , 1 , 2 , \ldots , 1 0 0 0$ , do the following:

(a) Estimate the constants $a _ { 0 }$ , and $a _ { i } , A _ { i } , B _ { i }$ for $i = { 1 , 2 , 3 , 4 }$ (b) Compare execution times and accuracy of the following four algorithms.

i. Cholesky decomposition ii. Givens transformation iii. Givens square root free transformation iv. Householder transformation

Generate your own perfect observations using the coefficients given:

Exact Coefficients:

$$
{ \begin{array} { l l l } { a _ { 0 } = - 5 0 } & & { a _ { 1 } = - 5 0 } \\ { a _ { 1 } = 0 . 2 5 } & & { A _ { 1 } = - 5 0 } & { B _ { 1 } = 1 0 1 } \\ { a _ { 2 } = - 0 . 6 2 5 \times 1 0 ^ { - 3 } } & & { A _ { 2 } = 1 } & { B _ { 2 } = - 0 . 5 } \\ { a _ { 3 } = - 0 . 4 \times 1 0 ^ { - 6 } } & & { A _ { 3 } = - 2 7 } & { B _ { 3 } = - 2 7 } \\ { a _ { 4 } = 0 . 9 \times 1 0 ^ { - 9 } } & & { A _ { 4 } = 4 } & { B _ { 4 } = - 3 } \end{array} }
$$

(c) Redo (a) after adding Gaussian random noise with mean zero and variance $= 2$ to the data.

6. From Eq. (5.10.120), derive Eqs. (5.10.123), (5.10.124), and (5.10.125), which define the covariance for the smoothed solution including process noise. (Hint: see Eqs. (5.10.114) through Eq. (5.10.117)).

7. Generate one cycle of a sine wave with an amplitude of unity. Add white noise, $N ( 0 , 0 . 0 5 )$ . Generate observation data by sampling the noisy sine wave 1000 times at equal intervals.

Using one process noise parameter, recover the sine wave using a SRIF both as a filter and a smoother. Try various combinations of $\tau$ and $\sigma$ in Eqs. (5.11.2) and (5.11.6). For example try a large $\tau$ and small $\sigma$ and estimate the amplitude as a constant (case 1). Try $\tau = 0$ and a very large $\sigma$ to simulate the sine wave as a white noise process (case 2). Try a random walk process to describe the process noise parameter (i.e., $m = 1$ , choose $q$ (case 3)). Finally find a value of $\tau$ and $\sigma$ that does a good job of replicating the sine wave (e.g., one for which the RMS of fit is near to the RMS of the noise on the data (case 4)). Assume a priori information, $\bar { p } = 0$ and $\overline { { P } } _ { 0 } = \infty$ and that the process noise, $\overline { { w } } = 0$ , at each stage. Use the algorithms described in Sections 5.11.1 and 5.11.2 for filtering and smoothing, respectively.

Generate the following figures for these four cases:

(a) Plot the observations and the filter solutions. Compute the RMS difference.   
(b) Plot the observations and the smoothed solutions. Compute the RMS difference.   
(c) Compute the RMS differences between the true sine wave (without noise) and the filter and smoothed solutions.   
(d) Plot the observations minus the smoothed solution.   
(e) Plot $w$ , the process noise.

For the optimal $\tau$ and $\sigma$ , the plots in (d) and (e) should look similar. The optimal $\tau$ and $\sigma$ result in the correlated signal in the observations being absorbed by $p$ and the random noise by $w$ .

\* Solution hints for Exercise 7.

The measurement update at the $i ^ { \mathrm { t h } }$ stage is given by performing an orthogonal transformation (Householder or Givens),

$$
T _ { i } \left[ \begin{array} { l } { \overline { { { R } } } _ { p _ { i } } \bar { b } _ { p _ { i } } } \\ { H \quad y _ { i } } \\ { 2 \times 2 } \end{array} \right] _ { 2 \times 2 } = \left[ \begin{array} { l } { \hat { R } _ { p _ { i } } \hat { b } _ { p _ { i } } } \\ { 0 \quad e _ { i } } \end{array} \right] _ { 2 \times 2 }
$$

where the equation number refers to the corresponding equation in the text.   
At the epoch time $\overline { { R } } _ { p _ { 0 } } = 0$ and $\bar { b } _ { p _ { 0 } } = 0$ are given.

Next, a time update to the $i + 1 ^ { \mathrm { s t } }$ stage results from a series of orthogonal transformations on

$$
T _ { i + 1 } \left[ \begin{array} { c c c } { - R _ { w } m } & { R _ { w } } & { \bar { b } _ { w _ { i } } } \\ { \hat { R } _ { p _ { i } } } & { 0 } & { \hat { b } _ { p _ { i } } } \end{array} \right] _ { 2 \times 3 } = \left[ \begin{array} { c c c } { R _ { p _ { i } } ^ { * } } & { R _ { p _ { i + 1 } } ^ { * } } & { b _ { p _ { i } } ^ { * } } \\ { 0 } & { \overline { { R } } _ { p _ { i + 1 } } } & { \bar { b } _ { p _ { i + 1 } } } \end{array} \right] _ { 2 \times 3 . }
$$

The $( \quad ) ^ { * }$ values must be saved for smoothing. Also,

$$
\begin{array} { l } { { \displaystyle R _ { w } = \frac { 1 } { \sqrt { q } } } } \\ { { \displaystyle m = e ^ { - ( t _ { i + 1 } - t _ { i } ) / \tau } } } \\ { { \displaystyle q = ( 1 - m ^ { 2 } ) \sigma ^ { 2 } } } \\ { { \displaystyle H = 1 ~ \mathrm { ( t h e ~ o b s e r v a t i o n ~ i s ~ } p ) } } \\ { { \displaystyle \overline { { P } } _ { 0 } = \infty } ; } \end{array}
$$

hence, $\overline { { R } } _ { p _ { 0 } } = 0$ and $\bar { b } _ { p _ { 0 } } = \overline { { R } } _ { p _ { 0 } } \bar { p } _ { 0 } = 0 .$ . The filter value of $p$ at each stage is

computed from

$$
\hat { p } _ { i } = \frac { \hat { b } _ { p _ { i } } } { \hat { R } _ { p _ { i } } } .
$$

After the final data point has been processed we may begin smoothing. The first smoothed value of $p$ is given by (assuming $N$ data points)

$$
p _ { N - 1 } ^ { N } = \frac { b _ { p _ { N } } ^ { * } - R _ { p _ { N } } ^ { * } \hat { p } _ { N } } { R _ { p _ { N - 1 } } ^ { * } } .
$$

The smoothed value of $p$ at the $i ^ { \mathrm { t h } }$ stage is given by

$$
p _ { i } ^ { N } = \frac { b _ { p _ { i + 1 } } ^ { * } - R _ { p _ { i + 1 } } ^ { * } \hat { P } _ { i + 1 } ^ { N } } { R _ { p _ { i } } ^ { * } }
$$

A value of $\hat { w } _ { i } ^ { N }$ may be determined from Eq. (5.11.13) by using the smoothed values of $p$ ,

$$
\hat { w } _ { i } ^ { N } = p _ { i + 1 } ^ { N } - m p _ { i } ^ { N } i = N - 1 , N - 2 , \ldots 0 .
$$

8. Work Example 4.8.2, the spring mass problem, using the square root free Givens method to solve for $\hat { \mathbf { x } } _ { 0 }$ and the associated estimation error covariance matrix. You should get results almost identical to those given in Example 4.8.2.

# Chapter 6

# Consider Covariance Analysis

# 6.1 INTRODUCTION

The design and subsequent performance of the statistical estimation algorithms used for orbit determination, parameter identification, and navigation applications are dependent on the accuracy with which the dynamic system and the measurements used to observe the motion can be modeled. In particular, the design of orbit determination algorithms usually begins with the defini tion of the important error sources and a statistical description of these error sources. The effect of erroneous assumptions regarding (1) the mathematical description of the force model or the measurement model, (2) the statistical properties of the random errors, and (3) the accuracy of the numerical values assigned to the unestimated measurement and force model parameters, as well as the round-off and truncation characteristics that occur in the computation process, can lead to reduced estimation accuracy and, on occasion, to fil ter divergence. The general topic of covariance analysis treats the sensitivity of the estimation accuracy to these error sources. The first topic to be treated here is the effects of errors in the constant, but nonestimated, dynamic, and measurement model parameters. Errors of this nature lead to biased estimates. A second topic to be considered is the effect of errors in statistics such as the data noise covariance and the a priori state covariance.

On occasion it may be advantageous to ignore (i.e., not estimate) certain unknown or poorly known model parameters. Consider covariance analysis is a technique to assess the impact of neglecting to estimate these parameters on the accuracy of the state estimate.

The reasons for neglecting to estimate certain parameters are:

1. It is cost effective in computer cost, memory requirements, and execution time to use as small a parameter array as possible. 2. Large dimension parameter arrays may not be “totally” observable from an observation set collected over a short time interval.

Consider covariance analysis is a “des ign tool” that can be used for sensitivity analysis to determine the optimal parameter array for a given estimation problem or to structure an estimation algorithm to achieve a more robust performance in the presence of erroneous force and/or measurement model parameters.

Covariance analysis is an outgrowth of the study of the effects of errors on an estimate of the state of a dynamical system. These errors manifest themselves as:

1. Large residuals in results obtained with a given estimation algorithm.   
2. Divergence in the sequential estimation algorithms.   
3. Incorrect navigation decisions based on an optimistic state error covariance.

As discussed in Chapter 4, the operational “fix” for the Kalman or sequential filter divergence problem caused by optimistic state error covariance estimates is the addition of process noise. In an application, the process noise model will cause the filter to place a higher weight on the most recent data. For the batch estimate, a short-arc solution, which reduces the time interval for collecting the batch of observations, can be used to achieve a similar result. Neither approach is very useful as a design tool.

The comments in the previous paragraphs can be summarized as follows. Consider covariance analysis, in the general case, attempts to quantify the effects of:

a. Nonestimated parameters, C, whose uncertainty is neglected in the estimation procedure. b. Incorrect a priori covariance for the a priori estimate of $\mathbf { X }$ . c. Incorrect a priori covariance for the measurement noise.

A consider filter will use actual data along with a priori information on certain consider parameters to improve the filter divergence characteristics due to errors in the dynamic and measurement models. The effects of bias in the unestimated model parameters is the most important of these effects and will be given primary emphasis in the following discussion.

# 6.2 BIAS IN LINEAR ESTIMATION PROBLEMS

Errors in the constant parameters that appear in the dynamic and/or measurement models may have a random distribution a priori. However, during any estimation procedure the values will be constant but unknown and, hence, must be treated as a bias. Bias errors in the estimation process are handled in one of three ways:

1. Neglected. The estimate of the state is determined, neglecting any errors in the nonestimated force model and measurement model parameters. 2. Estimated. The state vector is expanded to include dynamic and measurement model parameters that may be in error. 3. Considered. The state vector is estimated but the uncertainty in the nonestimated parameters is included in the estimation error covariance matrix. This assumes that the nonestimated parameters are constant and that their $a$ priori estimate and associated covariance matrix is known.

In sequential filteri ng analysis, an alternate approach is to compensate for the effects of model errors through the addition of a process noise model, as discussed in Section 4.9 of Chapter 4.

# 6.3 FORMULATION OF THE CONSIDER COVARIANCE MATRIX

Consider the following partitioning of the generalized state vector $\mathbf { z }$ , and observation-state mapping matrix $H$ ,

$$
\mathbf { z } = \left[ \mathbf { x } \right] , H = [ H _ { x } ; H _ { c } ]
$$

where $\mathbf { x }$ is an $n \times 1$ vector of state variables whose values are to be estimated and $\mathbf { c }$ is a $q \times 1$ vector of measurement and force model variables whose values are uncertain but whose values will not be estimated. Note that we are considering a linearized system so that c represents a vector of deviations between the true and nominal values of the consider parameters, $\mathbf { C }$ ,

$$
\mathbf { c } = \mathbf { C } - \mathbf { C } ^ { * } .
$$

The measurement model for the $i ^ { \mathrm { t h } }$ observation,

$$
\mathbf { y } _ { i } = H _ { i } \mathbf { z } _ { i } + \epsilon _ { i } , i = 1 , \ldots , l
$$

can be expressed as

$$
{ \bf y } _ { i } = H _ { x _ { i } } { \bf x } + H _ { c _ { i } } { \bf c } + \epsilon _ { i } , i = 1 , \ldots , l .
$$

Assume that an $a$ priori estimate of $\mathbf { x }$ and associated covariance (e.g., $( \overline { { \mathbf { x } } } , \overline { { P } } _ { x } ) $ ) is given along with c, an a priori estimate of $\mathbf { c }$ . The filt er equations can be derived by following the procedures used in Chapter 4. The relevant equations are

$$
{ \bf y } = H _ { x } { \bf x } + H _ { c } { \bf c } + \epsilon
$$

where

$$
\mathbf { y } = \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \mathbf { y } _ { 2 } } \\ { \vdots } \\ { \mathbf { y } _ { l } } \end{array} \right] , H _ { x } = \left[ \begin{array} { c } { H _ { x _ { 1 } } } \\ { H _ { x _ { 2 } } } \\ { \vdots } \\ { H _ { x _ { l } } } \end{array} \right] ,
$$

$$
H _ { c } = \left[ \begin{array} { c } { H _ { c _ { 1 } } } \\ { H _ { c _ { 2 } } } \\ { \vdots } \\ { H _ { c _ { l } } } \end{array} \right] , \epsilon = \left[ \begin{array} { c } { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \\ { \vdots } \\ { \epsilon _ { l } } \end{array} \right]
$$

and

$$
\begin{array} { r l } { \mathbf { y } _ { i } ~ } & { { } = ~ } & { p \times 1 \mathrm { ~ v e c t o r ~ o f ~ } \mathrm { { f o s e r s a i o n s } } } \\ { \mathbf { y } ~ } & { { } = ~ } & { l p \times 1 \mathrm { ~ v e c t o r ~ o f ~ } \mathrm { { o b s e r s a t i o n s } } } \\ { H _ { x _ { i } } ~ } & { { } = ~ } & { p \times n \mathrm { ~ m a t r i x } } \\ { H _ { x _ { i } } ~ } & { { } = ~ } & { l p \times n \mathrm { ~ a t r i x } } \\ { H _ { c _ { i } } ~ } & { { } = ~ } & { p \times q \mathrm { ~ m a t r i x } } \\ { H _ { c _ { i } } ~ } & { { } = ~ } & { p \times q \mathrm { ~ m a t r i x } } \\ { H _ { c } ~ } & { { } = ~ } & { l p \times q \mathrm { ~ m a t r i x } } \\ { \mathbf { x } ~ } & { { } = ~ } & { n \times 1 \mathrm { ~ s t a t e ~ v e c t o r ~ o r a t e r ~ p a r a m e t e r s } } \\ { \mathbf { c } ~ } & { { } = ~ } & { q \times 1 \mathrm { ~ v e c t o r ~ o f ~ c o n s i d e r ~ p a r a m e t o r s } } \\ { \boldsymbol { \epsilon } ~ } & { { } = ~ } & { l p \times 1 \mathrm { ~ v e c t o r ~ o f ~ o b s e r s a t i o n ~ e r m o r s } } \\ { \boldsymbol { \epsilon } _ { i } ~ } & { { } = ~ } & { p \times 1 \mathrm { ~ w e c t o r ~ o f ~ n o s e r s a t i o n ~ e r m o r s } . } \end{array}
$$

Recall that unless the observation-state relationship and the state propagation equations are linear, $\mathbf { y } , \mathbf { x }$ , and c represent observation, state, and consider parameter deviation vectors, respectively. Also,

$$
E [ \epsilon _ { i } ] = 0 , \qquad E [ \epsilon _ { i } \epsilon _ { j } ^ { T } ] = R _ { i } \delta _ { i j } ,
$$

$$
E [ \epsilon \epsilon ^ { T } ] = R = \left[ \begin{array} { c c c c } { { R _ { 1 } } } & { { } } & { { } } & { { } } \\ { { } } & { { R _ { 2 } } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { R _ { l } } } \end{array} \right] _ { l p \times l p }
$$

where $\delta _ { i j }$ is the Kronecker delta.

A priori estimates for $\mathbf { x }$ and c are given by $\overline { { \mathbf { x } } }$ and $\overline { { \mathbf { c } } }$ , where

$$
\begin{array} { r } { \overline { { \mathbf { x } } } = \mathbf { x } + \pmb { \eta } , \overline { { \mathbf { c } } } = \mathbf { c } + \pmb { \beta } . } \end{array}
$$

The errors, $\eta$ and $\beta$ , have the following statistical properties:

$$
\begin{array} { r l } & { \quad E [ \eta ] = E [ \beta ] = 0 } \\ & { E [ \eta \eta ^ { T } ] = \overline { { P } } _ { x } } \\ & { E [ \beta \beta ^ { T } ] = \overline { { P } } _ { c c } } \\ & { E [ \eta \epsilon ^ { T } ] = E [ \beta \epsilon ^ { T } ] = 0 } \\ & { E [ \eta \beta ^ { T } ] = \overline { { P } } _ { x c } . } \end{array}
$$

It is convenient to express this information in a more compact form, such as that of a data equation. From Eqs. (6.3.4) and (6.3.7)

$$
\begin{array} { r l } & { \mathbf { y } = H _ { x } \mathbf { x } + H _ { c } \mathbf { c } + \epsilon ; \epsilon \sim ( 0 , R ) } \\ & { \overline { { \mathbf { x } } } = \mathbf { x } + \eta ; \qquad \eta \sim ( 0 , \overline { { P } } _ { x } ) } \\ & { \overline { { \mathbf { c } } } = \mathbf { c } + \boldsymbol { \beta } ; } \end{array}
$$

Let

$$
\mathbf { z } = \left[ \begin{array} { l } { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] ; \tilde { \mathbf { y } } = \left[ \begin{array} { l } { \mathbf { y } } \\ { \overline { { \mathbf { x } } } } \\ { \overline { { \mathbf { c } } } } \end{array} \right] ;
$$

$$
H _ { z } = \left[ \begin{array} { l l } { H _ { x } } & { H _ { c } } \\ { I } & { 0 } \\ { 0 } & { I } \end{array} \right] ; \tilde { \epsilon } = \left[ \begin{array} { l } { \epsilon } \\ { \eta } \\ { \beta } \end{array} \right] .
$$

It follows that the observation equations can be expressed as

$$
\tilde { \mathbf { y } } = H _ { z } \mathbf { z } + \tilde { \epsilon } ; \tilde { \mathbf { \epsilon } } \sim ( 0 , \tilde { R } )
$$

where

$$
\tilde { R } = \left[ \begin{array} { l l l } { R } & { 0 } & { 0 } \\ { 0 } & { \overline { { P } } _ { x } } & { \overline { { P } } _ { x c } } \\ { 0 } & { \overline { { P } } _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right] .
$$

We wish to determine the weighted least squares estimate of $\mathbf { z }$ , obtained by choosing the value of $\mathbf { z }$ , which minimizes the performance index

$$
J = 1 / 2 \tilde { \epsilon } \tilde { R } ^ { - 1 } \tilde { \epsilon } ^ { T } .
$$

Note that the weight has been specified as the $a$ priori data noise covariance matrix. As illustrated in Section 4.3.3, the best estimate of $\mathbf { z }$ is given by

$$
\hat { \mathbf { z } } = \left( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \right) ^ { - 1 } H _ { z } ^ { T } \tilde { R } ^ { - 1 } \tilde { \mathbf { y } }
$$

with the associated estimation error covariance matrix

$$
\begin{array} { r } { P _ { z } = E \Big [ ( \hat { \mathbf { z } } - \mathbf { z } ) ( \hat { \mathbf { z } } - \mathbf { z } ) ^ { T } \Big ] = \Big ( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \Big ) ^ { - 1 } . } \end{array}
$$

Equations (6.3.18) and (6.3.19) may be written in partitioned form in order to isolate the quantities of interest. First define

$$
\tilde { R } ^ { - 1 } = \left[ \begin{array} { l l l } { R ^ { - 1 } } & { 0 } & { 0 } \\ { 0 } & { \overline { { M } } _ { x x } } & { \overline { { M } } _ { x c } } \\ { 0 } & { \overline { { M } } _ { c x } } & { \overline { { M } } _ { c c } } \end{array} \right] .
$$

From

$$
\tilde { R } \tilde { R } ^ { - 1 } = I ,
$$

it can be shown that

$$
\begin{array} { r c l } { \overline { { M } } _ { x x } } & { = } & { \overline { { P } } _ { x } ^ { - 1 } + \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } \overline { { M } } _ { c c } \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } } \\ & { = } & { ( \overline { { P } } _ { x } - \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } \overline { { P } } _ { c x } ) ^ { - 1 } } \\ { \overline { { M } } _ { x c } } & { = } & { - ( \overline { { P } } _ { x } - \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } \overline { { P } } _ { c x } ) ^ { - 1 } \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } } \\ & { = } & { - \overline { { M } } _ { x x } \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } } \\ { \overline { { M } } _ { c x } } & { = } & { - ( \overline { { P } } _ { c c } - \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } ) ^ { - 1 } \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } = \overline { { M } } _ { x c } ^ { T } } \\ { \overline { { M } } _ { c c } } & { = } & { ( \overline { { P } } _ { c c } - \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } ) ^ { - 1 } . } \end{array}
$$

From Eq. (6.3.18) it follows that

$$
\big ( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \big ) \hat { \mathbf { z } } = H _ { z } ^ { T } \tilde { R } ^ { - 1 } \tilde { \mathbf { y } }
$$

or

$$
\left[ \begin{array} { c c } { \left( H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { M } } _ { x x } \right) } & { \left( H _ { x } ^ { T } R ^ { - 1 } H _ { c } + \overline { { M } } _ { x c } \right) } \\ { \left( H _ { c } ^ { T } R ^ { - 1 } H _ { x } + \overline { { M } } _ { c x } \right) } & { \left( H _ { c } ^ { T } R ^ { - 1 } H _ { c } + \overline { { M } } _ { c c } \right) } \end{array} \right] \left[ \begin{array} { c c } { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right]
$$

$$
\mathbf { \Psi } = \left[ \begin{array} { l } { H _ { x } ^ { T } R ^ { - 1 } y + \overline { { M } } _ { x x } \overline { { x } } + \overline { { M } } _ { x c } \overline { { c } } } \\ { H _ { c } ^ { T } R ^ { - 1 } y + \overline { { M } } _ { c x } \overline { { x } } + \overline { { M } } _ { c c } \overline { { c } } } \end{array} \right] .
$$

Rewriting Eq. (6.3.27) as

$$
\left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] \left[ \begin{array} { l } { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right] = \left[ \begin{array} { l } { \mathbf { N } _ { x } } \\ { \mathbf { N } _ { c } } \end{array} \right]
$$

leads to the simultaneous equations

$$
\begin{array} { r l r } { M _ { x x } \hat { \bf x } + M _ { x c } \hat { \bf c } } & { { } = } & { { \bf N } _ { x } } \\ { M _ { c x } \hat { \bf x } + M _ { c c } \hat { \bf c } } & { { } = } & { { \bf N } _ { c } } \end{array}
$$

where

$$
\begin{array} { l c l } { { M _ { x x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } } } \\ { { M _ { x c } } } & { { = } } & { { H _ { x } ^ { T } \ R ^ { - 1 } H _ { c } + \overline { { { M } } } _ { x c } } } \\ { { M _ { c x } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } \ H _ { x } + \overline { { { M } } } _ { c x } = M _ { x c } ^ { T } } } \\ { { M _ { c c } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } H _ { c } + \overline { { { M } } } _ { c c } } } \\ { { { \bf N } _ { x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } { \bf y } + \overline { { { M } } } _ { x x } \overline { { { \bf x } } } + \overline { { { M } } } _ { x c } \overline { { { \bf z } } } } } \\ { { { \bf N } _ { c } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } { \bf y } + \overline { { { M } } } _ { c x } \overline { { { \bf x } } } + \overline { { { M } } } _ { c c } \overline { { { \bf z } } } . } } \end{array}
$$

From Eq. (6.3.29) it follows that

$$
{ \hat { \mathbf { x } } } = M _ { x x } ^ { - 1 } \mathbf { N } _ { x } \ - \ M _ { x x } ^ { - 1 } M _ { x c } { \hat { \mathbf { c } } } .
$$

If Eq. (6.3.32) is substituted into Eq. (6.3.30), the following result is obtained:

$$
M _ { c x } ( M _ { x x } ^ { - 1 } { \mathbf { N } } _ { x } - M _ { x x } ^ { - 1 } M _ { x c } \hat { \mathbf { c } } ) + M _ { c c } \hat { \mathbf { c } } = \mathbf { N } _ { c }
$$

or

$$
( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) \hat { \mathbf { c } } = \mathbf { N } _ { c } - M _ { c x } M _ { x x } ^ { - 1 } \mathbf { N } _ { x }
$$

and

$$
\hat { \mathbf { c } } = ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) ^ { - 1 } ( \mathbf { N } _ { c } - M _ { c x } M _ { x x } ^ { - 1 } \mathbf { N } _ { x } ) .
$$

The value for cˆ determined by Eq. (6.3.33) can be substituted into Eq. (6.3.32) to obtain $\hat { \bf x }$ .

The covariance matrix for the errors in $\hat { \bf x }$ and cˆ given by Eq. (6.3.19) can be

written in partitioned form as

$$
\left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { P _ { c c } } \end{array} \right] = \left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] ^ { - 1 }
$$

where $M _ { x x } , M _ { c x } , M _ { x c }$ , and $M _ { c c }$ are defined by Eq. (6.3.31). From the equation

$$
\left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] \left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { P _ { c c } } \end{array} \right] = \left[ \begin{array} { l l } { I } & { 0 } \\ { 0 } & { I } \end{array} \right] .
$$

It can be shown that

$$
\begin{array} { l c l } { { P _ { c x } } } & { { = } } & { { - M _ { c c } ^ { - 1 } M _ { c x } P _ { x x } } } \\ { { P _ { x c } } } & { { = } } & { { - M _ { x x } ^ { - 1 } M _ { x c } P _ { c c } } } \\ { { P _ { x x } } } & { { = } } & { { ( M _ { x x } - M _ { x c } M _ { c c } ^ { - 1 } M _ { c x } ) ^ { - 1 } } } \\ { { P _ { c c } } } & { { = } } & { { ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) ^ { - 1 } . } } \end{array}
$$

Note that

$$
P _ { x c } = P _ { c x } ^ { T } .
$$

The expression for $P _ { x x }$ can be written in an alternate form. Using the Schur identity (Theorem 4 of Appendix B) and letting

$$
\begin{array} { r c l } { { A } } & { { = } } & { { M _ { x x } } } \\ { { B } } & { { = } } & { { - M _ { x c } M _ { c c } ^ { - 1 } } } \\ { { C } } & { { = } } & { { M _ { c x } , } } \end{array}
$$

it can be shown that

$$
P _ { x x } = M _ { x x } ^ { - 1 } + M _ { x x } ^ { - 1 } M _ { x c } \big ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } \big ) ^ { - 1 } M _ { c x } M _ { x x } ^ { - 1 } .
$$

If we use the definition

$$
P _ { x } = M _ { x x } ^ { - 1 } = ( H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } ) ^ { - 1 } ,
$$

and define $S _ { x c }$ as (in Section 6.4 we will show Eq. (6.3.43) to be the sensitivity matrix)

$$
S _ { x c } \equiv - M _ { x x } ^ { - 1 } M _ { x c }
$$

and using Eq. (6.3.39) to define $P _ { c c }$ , we can write Eq. (6.3.41) as

$$
\begin{array} { r } { P _ { x x } = P _ { x } + S _ { x c } P _ { c c } S _ { x c } ^ { T } . } \end{array}
$$

Also, from Eqs. (6.3.37) and (6.3.44) we have

$$
P _ { x c } = S _ { x c } P _ { c c } = P _ { c x } ^ { T } .
$$

Using Eqs. (6.3.39), (6.3.42), and (6.3.44) we may write Eqs. (6.3.32) and (6.3.33) as

$$
\begin{array} { r c l } { \hat { \mathbf { x } } } & { = } & { P _ { x } \mathbf { N } _ { x } + S _ { x c } \hat { \mathbf { c } } } \\ { \hat { \mathbf { c } } } & { = } & { P _ { c c } ( \mathbf { N } _ { c } + S _ { x c } ^ { T } \mathbf { N } _ { x } ) . } \end{array}
$$

The consider estimate is obtained by choosing not to compute $\hat { \mathbf { c } }$ and $P _ { c c }$ but to fix them at their a priori values $\overline { { \mathbf { c } } }$ and $\overline { { P } } _ { c c }$ , respectively. In this case, the equations that require modification are

$$
\begin{array} { r c l } { P _ { c c } } & { = } & { \overline { { P } } _ { c c } } \\ { P _ { x x } } & { = } & { P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } } \\ { P _ { x c } } & { = } & { S _ { x c } \overline { { P } } _ { c c } } \\ { \hat { \mathbf { x } } } & { = } & { P _ { x } \mathbf { N } _ { x } + S _ { x c } \overline { { \mathbf { c } } } . } \end{array}
$$

The a priori covariance of the state and consider parameters, $\overline { { P } } _ { x c }$ , generally is unknown and assumed to be the null matrix. For the case where $\overline { { P } } _ { x c } = 0$ , Eq. (6.3.31) reduces to

$$
\begin{array} { r c l } { { M _ { x x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { P } } } _ { x } ^ { - 1 } \equiv P _ { x } ^ { - 1 } } } \\ { { M _ { x c } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { c } . } } \end{array}
$$

Hence,

$$
S _ { x c } = - M _ { x x } ^ { - 1 } M _ { x c }
$$

reduces to

$$
S _ { x c } = - P H _ { x } ^ { T } R ^ { - 1 } H _ { c } .
$$

The computational algorithm for the batch consider filte r is

$$
G i \nu e n \colon \overline { { \mathbf { x } } } , \overline { { \mathbf { c } } } , \overline { { P } } _ { x } , \overline { { P } } _ { x c } , \overline { { P } } _ { c c } , R _ { i } , H _ { x _ { i } } , H _ { c _ { i } } \mathrm { a n d } \mathbf { y } _ { i } , i = 1 \cdots l
$$

$\overline { { M } } _ { x x } , \overline { { M } } _ { x c }$ , and $\overline { { M } } _ { c c }$ are given by Eqs. (6.3.22), (6.3.23), and (6.3.25), respectively.

Compute:

$$
\begin{array} { l c l } { { M _ { x x } } } & { { = } } & { { \displaystyle { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } } } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { i = 1 } ^ { l } H _ { x _ { i } } ^ { T } R _ { i } ^ { - 1 } H _ { x _ { i } } + \overline { { { M } } } _ { x x } = P _ { x } ^ { - 1 } } } \end{array}
$$

$$
\begin{array} { r l } { M _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e } } N ^ { - 1 } M _ { \mathrm { e } } + \overline { { M } } _ { \mathrm { e x } } } \\ & { = \phantom { - } \frac { 1 } { \mathrm { e } ^ { - \mathrm { i } \epsilon _ { \mathrm { x } } } } B _ { \mathrm { e } } ^ { 2 } \mu _ { \mathrm { x } } ^ { - 1 } H _ { \mathrm { e } } + \overline { { M } } _ { \mathrm { e x } } } \\ { M _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { + 1 } } \\ { M _ { \mathrm { e x } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } R _ { \mathrm { e } } ^ { 2 } R _ { \mathrm { e } } ^ { - 1 } R _ { \mathrm { e } } } { \rho _ { \mathrm { x } } ^ { - 1 } } + \overline { { M } } _ { \mathrm { e x } } } \\ { \overline { { P } } _ { \mathrm { x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { + 1 } } \\ { \overline { { S } } _ { \mathrm { e x } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } M _ { \mathrm { e x } } ^ { + 1 } } { \rho _ { \mathrm { x } } ^ { - 1 } } } \\ { \mathbf { N } _ { \mathrm { s } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } R _ { \mathrm { e x } } ^ { 2 } } { \rho _ { \mathrm { x } } ^ { - 1 } } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } M _ { \mathrm { e x } } ^ { - 1 } \mathbf { \tilde { S } } _ { \mathrm { e x } } + \overline { { P } } _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \rho _ { \mathrm { e x } } } &  = \mathbf { \tilde { S } } _  \mathrm  e x  \end{array}
$$

Equation (6.3.66) may also be written as

$$
P _ { x x } = P _ { x } + P _ { x c } \overline { { P } } _ { c c } ^ { - 1 } P _ { x c } ^ { T } .
$$

The complete consider covariance matrix may be written as

$$
\mathbf { P _ { c } } = E \left\{ \left[ \begin{array} { l } { \hat { \mathbf { x } } _ { c } - \mathbf { x } } \\ { \overline { { \mathbf { c } } } - \mathbf { c } } \end{array} \right] \left[ ( \hat { \mathbf { x } } _ { c } - \mathbf { x } ) ^ { T } \mathbf { \Psi } ( \overline { { \mathbf { c } } } - \mathbf { c } ) ^ { T } \right] \right\} = \left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right]
$$

where $P _ { x x }$ is the consider covariance associated with the state vector of estimated parameters, $\mathbf { x }$ .

Note also that the expression for $\hat { \mathbf { x } } _ { c }$ can be written

$$
\begin{array} { r c l } { \hat { \mathbf { x } } _ { c } } & { = } & { P _ { x } \mathbf { N } _ { x } - P _ { x } M _ { x c } \mathbf { \overline { { c } } } } \\ { \hat { \mathbf { x } } _ { c } } & { = } & { \hat { \mathbf { x } } - P _ { x } M _ { x c } \mathbf { \overline { { c } } } } \end{array}
$$

or, from Eq. (6.3.53)

$$
\hat { \mathbf { x } } _ { c } = \hat { \mathbf { x } } - P _ { x } H _ { x } ^ { T } R ^ { - 1 } H _ { c } \overline { { \mathbf { c } } }
$$

where $\hat { \bf x }$ and $P _ { x }$ are the values of those parameters obtained from a batch processor, which assumes there are no errors in the consider parameters (i.e., $\mathbf { C ^ { * } } = \mathbf { C }$ and $P _ { x c }$ , $\overline { { P } } _ { c c }$ , $\mathbf { c }$ , and c are all zero).

# 6.4 THE SENSITIVITY AND PERTURBATION MATRICES

Several other matrices are often associated with the concept of consider analysis. The sensitivity matrix is defined to be

$$
S _ { x c } = \frac { \partial \hat { \mathbf { x } } _ { c } } { \partial \hat { \mathbf { c } } }
$$

which from Eq. (6.3.32) is

$$
S _ { x c } = - M _ { x x } ^ { - 1 } M _ { x c } .
$$

From Eq. (6.3.52)

$$
S _ { x c } = - P M _ { x c } ,
$$

and using Eq. (6.3.53) $S _ { x c }$ becomes

$$
S _ { x c } = - P H _ { x } ^ { T } R ^ { - 1 } H _ { c } .
$$

Hence, Eq. (6.3.71) may be written as

$$
\hat { \mathbf { x } } _ { c } = \hat { \mathbf { x } } + S _ { x c } \overline { { \mathbf { c } } } .
$$

Recall from Eq. (6.3.66) that the consider covariance can be written in terms of the sensitivity matrix as

$$
P _ { x x } = P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } .
$$

Also, using Eq. (6.3.67) the covariance, $P _ { x c }$ , can be written as

$$
P _ { x c } = S _ { x c } \overline { { P } } _ { c c } .
$$

The sensitivity matrix describes how $\hat { \mathbf { x } } _ { c }$ varies with respect to the consider parameters, c. Another commonly used matrix is the perturbation matrix defined by

$$
\Gamma = S _ { x c } \cdot \left[ \mathrm { d i a g o n a l } \left( \sigma _ { c } \right) \right]
$$

where the elements of the diagonal matrix are the standard deviations of the consider parameters. Each element, $\Gamma _ { i j }$ , gives the error in the estimate of $\mathbf { x } _ { i }$ due to a one-sigma error in the consider parameter $c _ { j }$ .

Additional discussion of consider covariance analysis can be found in Bierman (1977).

# 6.4.1 EXAMPLE APPLICATION OF A SENSITIVITY AND PERTURBATION MATRIX

Assume we have a state vector comprised of coordinates $x$ and $y$ and a parameter $\alpha$ , and consider parameters $\gamma$ and $\delta$ ,

$$
\mathbf { X } = { \left[ \begin{array} { l } { x } \\ { y } \\ { \alpha } \end{array} \right] } , \quad \mathbf { c } = { \left[ \begin{array} { l } { \gamma } \\ { \delta } \end{array} \right] } .
$$

The perturbation matrix is defined by

$$
\Gamma \equiv S _ { x c } \cdot [ \mathrm { d i a g } \sigma _ { c } ] = \left[ \begin{array} { l l } { \frac { \partial \hat { x } } { \partial \gamma } } & { \frac { \partial \hat { x } } { \partial \delta } } \\ { \frac { \partial \hat { y } } { \partial \gamma } } & { \frac { \partial \hat { y } } { \partial \delta } } \\ { \frac { \partial \hat { \alpha } } { \partial \gamma } } & { \frac { \partial \hat { \alpha } } { \partial \delta } } \end{array} \right] \left[ \begin{array} { l l } { \sigma _ { \gamma } } & { 0 } \\ { 0 } & { \sigma _ { \delta } } \end{array} \right]
$$

or

$$
\Gamma = \left[ \begin{array} { l l } { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } } \\ { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } } \\ { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } } \end{array} \right] .
$$

Hence, the errors in the state estimate due to one-sigma errors in the consider parameters are given by

$$
\begin{array} { r c l } { { \Delta \hat { x } } } & { { = } } & { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } } } \\ { { \Delta \hat { y } } } & { { = } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } } } \\ { { \Delta \hat { \alpha } } } & { { = } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } . } } \end{array}
$$

Note that the information in $\Gamma$ is meaningful only if $\overline { { P } } _ { c c }$ (the covariance matrix of the errors in the consider parameters) is diagonal.

We may now form the consider covariance matrix. For simplicity, assume that

$\overline { { P } } _ { c c }$ is diagonal. Using Eq. (6.4.6) we may write $P _ { x x }$ in terms of $\Gamma$

$$
P _ { x x } = P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } = P _ { x } + \Gamma \Gamma ^ { T } .
$$

The contribution of the consider parameters is given by

$$
\begin{array} { r c l } { { S _ { x c } \overline { { { P } } } _ { c c } \ S _ { x c } ^ { T } } } & { { = } } & { { P _ { x c } S _ { x c } ^ { T } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \left[ \begin{array} { l l } { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \\ { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \\ { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \end{array} \right] \left[ \begin{array} { l l l } { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } } } \\ { { \displaystyle \frac { \partial \hat { x } } { \partial \delta } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \delta } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } } } \end{array} \right] . } } \end{array}
$$

The diagonal terms of this matrix are

$$
= \left[ \begin{array} { c } { \left( \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { x } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \\ { \left( \frac { \partial \hat { y } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { y } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \\ { \left( \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { \alpha } } { \partial \delta } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { \alpha } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \end{array} \right]
$$

or in simplified notation, the upper triangular portion of this symmetric matrix is given by

$$
S _ { x c } \overline { { { P } } } _ { c c } S _ { x c } ^ { T } = \left[ \begin{array} { c c c } { { \sigma _ { \hat { x } } ^ { 2 } } } & { { \sigma _ { \hat { x } } \sigma _ { \hat { y } } \rho _ { x y } } } & { { \sigma _ { \hat { x } } \sigma _ { \hat { \alpha } } \rho _ { x \alpha } } } \\ { { } } & { { \sigma _ { \hat { y } } ^ { 2 } } } & { { \sigma _ { \hat { y } } \sigma _ { \hat { \alpha } } \rho _ { y \alpha } } } \\ { { } } & { { } } & { { \sigma _ { \hat { \alpha } } ^ { 2 } } } \end{array} \right] _ { \mathrm { c o n s i d e r } } .
$$

For example, the total consider variance for the state variable, $x$ , is given by

$$
\begin{array} { r c l } { { \sigma _ { \hat { x } } ^ { 2 } } } & { { = } } & { { [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { d a t a  n o i s e } } + \left( \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \displaystyle \frac { \partial \hat { x } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } } \\ { { } } & { { = } } & { { [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { d a t a n n o i s e } } + [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { c o n s i d e r } } . } } \end{array}
$$

Comments:

1. If $\overline { { P } } _ { c c }$ is diagonal, then the diagonal elements of $P _ { x x }$ consist of the variance due to data noise plus the sum of the squares of the perturbations due to each consider parameter.

2. Off diagonal terms of the consider portion of $P _ { x x }$ contain correlations between errors in the estimated parameters caused by the consider parameters.

3. If di $\overline { { P } } _ { c c }$ is a full matrix, nal terms become $S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T }$ becomes much more complex, and thef the covariances (correlations) between consider parameters.

For example, consider the case where $\overline { { P } } _ { c c }$ is a full matrix and $\mathbf { X } = [ x y ] ^ { T }$ and ${ \bf c } = [ c _ { 1 } c _ { 2 } ] ^ { T }$ are $2 \times 1$ vectors. Then

$$
\begin{array} { r } { S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } = \left[ \begin{array} { c c } { \displaystyle \frac { \partial \hat { x } } { \partial c _ { 1 } } } & { \displaystyle \frac { \partial \hat { x } } { \partial c _ { 2 } } } \\ { \displaystyle \frac { \partial \hat { y } } { \partial c _ { 1 } } } & { \displaystyle \frac { \partial \hat { y } } { \partial c _ { 2 } } } \end{array} \right] \left[ \begin{array} { c c } { \boldsymbol { \sigma } _ { c _ { 1 } } ^ { 2 } } & { \displaystyle \mu _ { 1 2 } } \\ { \displaystyle \mu _ { 1 2 } } & { \boldsymbol { \sigma } _ { c _ { 2 } } ^ { 2 } } \end{array} \right] S _ { x c } ^ { T } . } \end{array}
$$

If this is expanded, the 1,1 element becomes

$$
( P _ { c } ) _ { 1 1 } = \left( \frac { \partial \hat { x } } { \partial c _ { 1 } } \right) ^ { 2 } \sigma _ { c _ { 1 } } ^ { 2 } + 2 \frac { \partial \hat { x } } { \partial c _ { 1 } } \frac { \partial \hat { x } } { \partial c _ { 2 } } \mu _ { 1 2 } + \left( \frac { \partial \hat { x } } { \partial c _ { 2 } } \right) ^ { 2 } \sigma _ { c _ { 2 } } ^ { 2 } .
$$

Depending on the sign of the components of the second term on the right-hand side, the consider uncertainty of $x$ could be greater or less than that for the case where $\overline { { P } } _ { c c }$ is diagonal. In general, inclusion of the correlations between the consider parameters (e.g., $\mu _ { 1 2 }$ ) results in a reduction in the consider variances.

# 6.5 INCLUSION OF TIME-DEPENDENT EFFECTS

In this section we will discuss consider covariance analysis under the assumption that the state vector is time dependent. However, in this chapter we will only “consider” the effect on the state vector of errors in constant measurement or model parameters.

The dynamical equations associated with the consider covariance model can be derived as follows. The differential equations for state propagation are given by (see Chapter 4):

$$
\dot { \mathbf { X } } = F ( { \mathbf { X } } , { \mathbf { C } } , t ) .
$$

Expanding Eq. (6.5.1) in a Taylor series to first order about a nominal trajectory yields

$$
{ \dot { \bf X } } = F ( { \bf X } ^ { * } , { \bf C } ^ { * } , t ) + \left[ \frac { \partial F } { \partial { \bf X } } \right] ^ { * } ( { \bf X } - { \bf X } ^ { * } ) + \left[ \frac { \partial F } { \partial { \bf C } } \right] ^ { * } ( { \bf C } - { \bf C } ^ { * } ) + . . .
$$

Define

$$
{ \dot { \mathbf { x } } } \equiv { \dot { \mathbf { X } } } - F ( \mathbf { X } ^ { * } , \mathbf { C } ^ { * } , t ) = \left[ { \frac { \partial F } { \partial \mathbf { X } } } \right] ^ { * } \left( \mathbf { X } - \mathbf { X } ^ { * } \right) + \left[ { \frac { \partial F } { \partial \mathbf { C } } } \right] ^ { * } \left( \mathbf { C } - \mathbf { C } ^ { * } \right) .
$$

This may be written as

$$
{ \dot { \mathbf { x } } } = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { c }
$$

where

$$
\begin{array} { r c l } { \mathbf { x } ( t ) } & { = } & { \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) } \\ { \mathbf { c } } & { = } & { \mathbf { C } - \mathbf { C } ^ { * } } \\ { A ( t ) } & { = } & { \left[ \cfrac { \partial F } { \partial \mathbf { X } } \right] ^ { * } } \\ { B ( t ) } & { = } & { \left[ \cfrac { \partial F } { \partial \mathbf { C } } \right] ^ { * } . } \end{array}
$$

For the conventional filter model $\mathbf { c } = 0$ , and the solution for Eq. (6.5.4) is

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { k } ) \mathbf { x } ( t _ { k } ) .
$$

The general solution of Eq. (6.5.4) can be obtained by the method of variation of parameters to yield

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { k } ) \mathbf { x } _ { k } + \theta ( t , t _ { k } ) \mathbf { c } .
$$

In Eq. (6.5.8), the $n \times n$ mapping matrix, $\Phi ( t , t _ { k } )$ , and the $n \times q$ mapping matrix, $\theta ( t , t _ { k } )$ , are defined as

$$
\begin{array} { l } { { \displaystyle \Phi ( t , t _ { k } ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf X } ( t _ { k } ) } } } \\ { { \displaystyle \theta ( t , t _ { k } ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf C } ( t _ { k } ) } . } } \end{array}
$$

The corresponding differential equations for $\Phi ( t , t _ { k } )$ and $\theta ( t , t _ { k } )$ are obtained by differentiating Eq. (6.5.1) and recognizing that differentiation with respect to time and $\mathbf { X } ( t _ { k } )$ and $\mathbf { C }$ are interchangeable for functions whose derivatives are continuous. From Eq. (6.5.1)

$$
\frac { \partial \dot { \mathbf X } } { \partial \mathbf X ( t _ { k } ) } = \frac { \partial F } { \partial \mathbf X ( t _ { k } ) } ,
$$

which may be written as

$$
\frac { d } { d t } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } ( t _ { k } ) } = \left[ \frac { \partial F } { \partial \mathbf { X } ( t ) } \right] ^ { * } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } ( t _ { k } ) }
$$

or

$$
{ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )
$$

with initial conditions $\Phi ( t _ { 0 } , t _ { 0 } ) = I$ . Likewise,

$$
\frac { d } { d t } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { C } ( t _ { k } ) } = \left[ \frac { \partial F } { \partial \mathbf { X } ( t ) } \right] ^ { * } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { C } ( t _ { k } ) } + \left[ \frac { \partial F } { \partial \mathbf { C } } \right] ^ { * }
$$

becomes

$$
\dot { \theta } ( t , t _ { k } ) = A ( t ) \theta ( t , t _ { k } ) + B ( t )
$$

with initial conditions $\theta ( t _ { 0 } , t _ { 0 } ) = 0$ . Note that if $C$ is partitioned as

$$
\mathbf { C } ^ { T } = [ \mathbf { C } _ { d } ^ { T } : \mathbf { C } _ { m } ^ { T } ]
$$

where $\mathbf { C } _ { d }$ are dynamic model parameters and $\mathbf { C } _ { m }$ are measurement model parameters, then $\theta$ can be written as

$$
\theta = [ \theta _ { d } \colon \theta _ { m } ]
$$

where the solution for $\theta _ { m }$ will be $\theta _ { m } ( t , t _ { k } ) = 0$ , the null matrix. This follows since measurement model parameters do not appear in the dynamic equations.

The estimation errors for the conventional filter model (Eq. 6.5.7) and the consider model (Eq. 6.5.8), labeled here as Filter and Consider, are mapped according to

Filter:

$$
\tilde { \mathbf { x } } ( t ) = \hat { \mathbf { x } } ( t ) - \mathbf { x } ( t ) = \boldsymbol { \Phi } ( t , t _ { k } ) \tilde { \mathbf { x } } _ { k }
$$

where $\tilde { \mathbf { x } } _ { k } = \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k }$ and all quantities are computed assuming there are no consider parameters.

Consider:

$$
\begin{array} { r c l } { \tilde { \mathbf { x } } _ { c } ( t ) } & { = } & { \hat { \mathbf { x } } _ { c } ( t ) - \mathbf { x } ( t ) } \\ & { = } & { [ \boldsymbol { \Phi } ( t , t _ { k } ) \hat { \mathbf { x } } _ { c _ { k } } + \boldsymbol { \theta } ( t , t _ { k } ) \bar { \mathbf { c } } ] - [ \boldsymbol { \Phi } ( t , t _ { k } ) \mathbf { x } _ { k } + \boldsymbol { \theta } ( t , t _ { k } ) \mathbf { c } ] } \\ & { = } & { \boldsymbol { \Phi } ( t , t _ { k } ) ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) + \boldsymbol { \theta } ( t , t _ { k } ) ( \bar { \mathbf { c } } - \mathbf { c } ) ( 6 . 5 . 1 } \\ & { = } & { \boldsymbol { \Phi } ( t , t _ { k } ) \tilde { \mathbf { x } } _ { c _ { k } } + \boldsymbol { \theta } ( t , t _ { k } ) \boldsymbol { \beta } } \end{array}
$$

where $\tilde { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k }$ and $\beta = \bar { \mathbf { c } } - \mathbf { c }$

We have included the conventional filter results in this section to illustrate differences with the consider fil ter. Remember that the conventional filter results assume that there are no errors in the consider parameters $\mathbf { C ^ { * } } = \mathbf { C }$ ). Hence, the true value, $\mathbf { x } _ { k }$ , for the fil ter results is different from the true value for the consider results.

The respective observation models are

Filter:

$$
\mathbf { y } _ { j } = \tilde { H } _ { x _ { j } } \mathbf { x } _ { j } + \boldsymbol { \epsilon } _ { j } \quad j = 1 , \ldots , l .
$$

Consider:

$$
\begin{array} { r } { { \bf y } _ { j } = \tilde { H } _ { x _ { j } } { \bf x } _ { j } + \tilde { H } _ { c _ { j } } { \bf c } + \epsilon _ { j } \quad j = 1 , \ldots , l . } \end{array}
$$

The state vector, $\mathbf { x } _ { j }$ , is replaced by its value at the estimation epoch $t _ { k }$ , by using Eq. (6.5.7),

Filter:

$$
{ \bf y } _ { j } = \tilde { H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) { \bf x } _ { k } + \epsilon _ { j } .
$$

The consider expression for $\mathbf { y } _ { j }$ is obtained by recognizing that

$$
{ \bf y } _ { j } = \tilde { H } _ { x _ { j } } \Big [ \Phi ( t _ { j } , t _ { k } ) { \bf x } _ { k } + \theta ( t _ { j } , t _ { k } ) { \bf c } \Big ] + \tilde { H } _ { c _ { j } } { \bf c } + \epsilon _ { j } .
$$

This equation may be written as

$$
\begin{array} { r } { \mathbf { y } _ { j } = \left[ \tilde { H } _ { x _ { j } } \tilde { H } _ { c _ { j } } \right] \left[ \begin{array} { c c } { \Phi ( t _ { j } , t _ { k } ) } & { \theta ( t _ { j } , t _ { k } ) } \\ { 0 } & { I } \end{array} \right] \left[ \begin{array} { c } { \mathbf { x } _ { k } } \\ { \mathbf { c } } \end{array} \right] + \epsilon _ { j } } \end{array}
$$

or

$$
\begin{array} { r } { \mathbf { y } _ { j } = \left[ \tilde { H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) \colon \tilde { H } _ { x _ { j } } \theta ( t _ { j } , t _ { k } ) + \tilde { H } _ { c _ { j } } \right] \left[ \begin{array} { l } { \mathbf { x } _ { k } } \\ { \mathbf { c } } \end{array} \right] + \epsilon _ { j } . } \end{array}
$$

By using the definitions

$$
{ \cal H } _ { x _ { j } } \equiv \tilde { \cal H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) \quad j = 1 , \ldots , l
$$

$$
{ \cal H } _ { c _ { j } } \equiv \tilde { H } _ { x _ { j } } \theta ( t _ { j } , t _ { k } ) + \tilde { H } _ { c _ { j } } \quad j = 1 , \ldots , l
$$

and

$$
\mathbf { y } \equiv \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \vdots } \\ { \mathbf { y } _ { l } } \\ { \mathbf { y } _ { l } } \end{array} \right] , \qquad H _ { x } \equiv \left[ \begin{array} { c } { H _ { x _ { 1 } } } \\ { \vdots } \\ { H _ { x _ { l } } } \end{array} \right] ,
$$

$$
H _ { c } \equiv \left[ \begin{array} { c } { { H _ { c _ { 1 } } } } \\ { { \vdots } } \\ { { } } \\ { { H _ { c _ { l } } } } \end{array} \right] , \quad \epsilon \equiv \left[ \begin{array} { c } { { \epsilon _ { 1 } } } \\ { { \vdots } } \\ { { } } \\ { { \epsilon _ { l } } } \end{array} \right]
$$

the two cumulative observation models used in Section 6.3 can then be obtained,

Filter:

$$
\mathbf { y } = H _ { x } \mathbf { x } _ { k } + \epsilon
$$

Consider:

$$
{ \bf y } = H _ { x } { \bf x } _ { k } + H _ { c } { \bf c } + \epsilon
$$

where $E [ \epsilon ] = 0$ and $E [ \epsilon \epsilon ^ { T } ] = R$ . The associated error covariance matrix for the filter model at the epoch, $t _ { k }$ , is

$$
\begin{array} { r } { P _ { x k } = E \big [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ^ { T } \big ] = \big [ H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { P } } _ { k } ^ { - 1 } \big ] ^ { - 1 } . } \end{array}
$$

To simplify, notation $P _ { x x }$ is being replaced by $P _ { c }$ , $S _ { x c }$ is being replaced by $S$ , and $P _ { x }$ is being replaced by $P$ for the remainder of this chapter.

The consider covariance is given by

$$
P _ { x x _ { k } } \equiv P _ { c _ { k } } = E \bigl [ ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ^ { T } \bigr ] .
$$

From Eq. (6.4.5)

$$
\hat { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { k } + S _ { k } \overline { { \mathbf { c } } } .
$$

However, the true value of $\mathbf { x } _ { k }$ for the consider covariance analysis is given by

$$
\mathbf { x } _ { k } = \mathbf { x } _ { k } ^ { * } + S _ { k } \mathbf { c }
$$

where $\mathbf { x } _ { k } ^ { * }$ is the true value of $\mathbf { x } _ { k }$ for the conventional fil ter $\mathbf { C ^ { * } } = \mathbf { C }$ ) and there are no errors in the consider parameters. $S _ { k } \mathbf { c }$ is the contribution due to the true value of $\mathbf { c }$ , the error in the consider parameters. Hence, $\Delta \hat { \mathbf x } _ { c _ { k } }$ , the error in the consider estimate, $\hat { \mathbf { x } } _ { c _ { k } }$ , is given by

$$
\Delta \hat { \bf x } _ { c _ { k } } \equiv \hat { \bf x } _ { c _ { k } } - { \bf x } _ { k } = \hat { \bf x } _ { k } - { \bf x } _ { k } ^ { * } + S _ { k } ( \overline { { \bf c } } - { \bf c } ) .
$$