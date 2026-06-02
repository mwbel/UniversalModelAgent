# 556 Some stiff methods

The first example, with $\textstyle \lambda = { \frac { 1 } { 4 } }$ and $\begin{array} { r } { c = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } , \frac { 3 } { 4 } , 1 ] ^ { \intercal } } \end{array}$ , has order 3:

This method was constructed with $\beta _ { 1 } = - \frac { 1 } { 4 }$ , $\beta _ { 2 } = \beta _ { 3 } = \textstyle { \frac { 1 } { 4 } }$ , $\begin{array} { r } { \epsilon _ { 0 } = \frac { 1 } { 2 5 6 } } \end{array}$ and $\delta ( \dot { V } ) = 0$ . The choice of $\epsilon _ { \mathrm { 0 } }$ was determined by requiring the stability function to be

$$
R ( z ) = \frac { 1 - \frac { 1 } { 8 } z ^ { 2 } - \frac { 1 } { 4 8 } z ^ { 3 } } { ( 1 - \frac { 1 } { 4 } z ) ^ { 4 } } ,
$$

which makes the method L-stable.

The second example has order 4 and an abscissa vector $\left[ \begin{array} { l l l l l } { 1 } & { \ \frac { 3 } { 4 } } & { \ \frac { 1 } { 4 } } & { \ \frac { 1 } { 2 } } & { \ 1 } \end{array} \right]$

$$
A = \left[ \begin{array} { r r r r r r } { \frac { 1 } { 4 } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - \frac { 5 1 3 } { 5 4 2 7 2 } } & { \frac { 1 } { 4 } } & { 0 } & { 0 } & { 0 } \\ { \frac { 3 7 0 6 1 1 9 } { 6 9 0 8 2 5 6 } } & { - \frac { 4 8 8 } { 3 8 1 9 } } & { \frac { 1 } { 4 } } & { 0 } & { 0 } \\ { \frac { 3 2 1 6 1 0 6 1 } { 1 9 7 5 4 9 2 3 2 } } & { - \frac { 1 1 1 8 1 4 } { 2 3 2 9 5 9 } } & { \frac { 1 3 4 } { 1 8 3 } } & { \frac { 1 } { 4 } } & { 0 } \\ { - \frac { 1 3 5 4 2 5 } { 2 9 4 8 4 9 6 } } & { - \frac { 6 4 1 } { 1 0 4 3 1 } } & { \frac { 7 3 } { 1 8 3 } } & { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } \end{array} \right] ,
$$

$$
V = \left[ \begin{array} { r r r r r r } { { 1 } } & { { - \frac { 3 6 7 3 1 3 } { 8 8 4 5 4 8 8 } } } & { { - \frac { 2 2 7 2 7 } { 2 9 4 8 4 9 6 } } } & { { \frac { 4 0 9 7 9 } { 5 8 9 6 9 9 2 } } } & { { \frac { 3 2 3 } { 6 2 0 7 3 6 } } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - \frac { 2 8 7 4 5 } { 1 0 4 3 1 } } } & { { - \frac { 1 9 3 7 } { 1 3 9 0 8 } } } & { { \frac { 1 1 7 } { 1 8 5 4 4 } } } & { { \frac { 6 5 } { 1 1 7 1 2 } } } \\ { { 0 } } & { { - \frac { 1 4 1 2 6 8 } { 1 0 4 3 1 } } } & { { - \frac { 2 0 5 0 } { 3 4 7 7 } } } & { { - \frac { 1 8 7 } { 2 3 1 8 } } } & { { \frac { 1 1 3 } { 1 4 6 4 } } } \\ { { 0 } } & { { - \frac { 2 1 6 4 1 6 } { 1 0 4 3 1 } } } & { { - \frac { 4 5 2 } { 3 4 7 7 } } } & { { - \frac { 4 9 1 } { 1 1 5 9 } } } & { { \frac { 1 6 1 } { 7 3 2 } } } \end{array} \right] .
$$

This property F method was constructed with $\beta _ { 1 } = \textstyle { \frac { 3 } { 4 } }$ , $\begin{array} { r } { \beta _ { 2 } = \frac { 3 } { 1 6 } } \end{array}$ , $\beta _ { 3 } = \textstyle { \frac { 1 } { 6 4 } }$ , $\begin{array} { r } { \epsilon _ { 0 } = \frac { 1 3 } { 1 5 3 6 0 } } \end{array}$ and $\delta ( P ^ { - 1 } \dot { V } P ) = 0$ , where

$$
P = \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 8 } & { 1 } & { 0 } & { 0 } \\ { 1 6 } & { 4 } & { 1 } & { 0 } \end{array} \right] .
$$

The method is L-stable with

$$
R ( z ) = { \frac { 1 - { \frac { 1 } { 4 } } z - { \frac { 1 } { 8 } } z ^ { 2 } + { \frac { 1 } { 9 6 } } z ^ { 3 } + { \frac { 7 } { 7 6 8 } } z ^ { 4 } } { ( 1 - { \frac { 1 } { 4 } } z ) ^ { 5 } } } .
$$
