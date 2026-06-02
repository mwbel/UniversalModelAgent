# 212 Global truncation error

After many steps of the Euler method, the errors generated in these steps will accumulate and reinforce each other in a complicated manner. It is important to understand how this happens. We assume a uniform bound $h ^ { 2 } m$ on the norm of the local truncation error committed in any step of length $h$ . We aim to find a global error bound using a difference inequality. We make the standard assumption that a Lipschitz condition holds, and we write $L$ as the Lipschitz constant.

Recall that $\widetilde y ( x )$ denotes the computed solution on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ . That is, at step values $x _ { 0 }$ , $x _ { 1 }$ , . . . , $x _ { n } ~ = ~ { \overline { { x } } }$ , $\widetilde { y }$ is computed using the equation $\widetilde { y } ( x _ { k } ) = y _ { k } = y _ { k - 1 } + ( x _ { k } - x _ { k - 1 } ) f ( x _ { k - 1 } , y _ { k - 1 } )$ . For ‘off-step’ points, $\widetilde y ( x )$ is defined by linear interpolation; or, what is equivalent, $\widetilde y ( x )$ is evaluated using a partial step from the most recently computed step value. That is, if $x \in ( x _ { k - 1 } , x _ { k } )$ , then

$$
\widetilde { y } ( x ) = y _ { k - 1 } + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , y _ { k - 1 } ) .
$$

Let $\alpha ( x )$ and $\beta ( x )$ denote the errors in $\widetilde y ( x )$ , as an approximation to $y ( x )$ , and in $f ( x , \widetilde { y } ( x ) )$ , as an approximation to $y ^ { \prime } ( x )$ , respectively. That is,

$$
\begin{array} { l } { \alpha ( x ) = y ( x ) - \widetilde { y } ( x ) , } \\ { \beta ( x ) = f ( x , y ( x ) ) - f ( x , \widetilde { y } ( x ) ) , } \end{array}
$$

so that, by the Lipschitz condition,

$$
\| \beta ( x ) \| \leq L \| \alpha ( x ) \| .
$$

Define $E ( x )$ so that the exact solution satisfies

$$
\begin{array} { r l r } & { } & { y ( x ) = y ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , y ( x _ { k - 1 } ) ) + ( x - x _ { k - 1 } ) ^ { 2 } { E } ( x ) , \quad } \\ & { } & { x \in ( x _ { k - 1 } , x _ { k } ] , } \end{array}
$$

and we assume that $\| E ( x ) \| \leq m$

Subtract (212a) from (212e), and use (212b) and (212c), so that

$$
\alpha ( x ) = \alpha ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) \beta ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) ^ { 2 } E ( x ) .
$$

Hence,

$$
\begin{array} { r l } & { \| \alpha ( x ) \| \leq \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) \| \beta ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) L \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq ( 1 + ( x - x _ { k - 1 } ) L ) \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq ( 1 + ( x - x _ { k - 1 } ) L ) \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) H m , } \end{array}
$$

where we have used (212d) and assumed that no step has a length greater than $H$ . We distinguish two cases. If $L = 0$ , then it follows that

$$
\| \alpha ( \boldsymbol { x } ) \| \le \| \alpha ( \boldsymbol { x } _ { 0 } ) \| + H m ( \boldsymbol { x } - \boldsymbol { x } _ { 0 } ) ;
$$

and if $L > 0$ , it follows that

$$
\begin{array} { r } { \displaystyle \left( \| \alpha ( x ) \| + \frac { H m } { L } \right) \leq ( 1 + ( x - x _ { k - 1 } ) L ) \left( \| \alpha ( x _ { k - 1 } ) \| + \frac { H m } { L } \right) } \\ { \leq \exp ( ( x - x _ { k - 1 } ) L ) \left( \| \alpha ( x _ { k - 1 } ) \| + \frac { H m } { L } \right) . } \end{array}
$$

Let $\phi ( x ) = \exp ( - ( x - x _ { 0 } ) L ) ( \| \alpha ( x ) \| + H m / L )$ , so that $\phi ( x )$ never increases. Hence,

$$
\| \alpha ( x ) \| \leq \exp ( ( x - x _ { 0 } ) L ) \| \alpha ( x _ { 0 } ) \| + \frac { \exp ( ( x - x _ { 0 } ) L ) - 1 } { L } H m .
$$

Combining the estimates found in the two cases and stating them formally, we have:

Theorem 212A Assuming that $f$ satisfies a Lipschitz condition, with constant $L$ , the global error satisfies the bound

$$
\| y ( x ) - \widetilde { y } ( x ) \| \leq \left\{ \begin{array} { l l } { \| y ( x _ { 0 } ) - \widetilde { y } ( x _ { 0 } ) \| + H m ( x - x _ { 0 } ) , \qquad L = 0 , } \\ { \exp ( ( x - x _ { 0 } ) L ) \| y ( x _ { 0 } ) - \widetilde { y } ( x _ { 0 } ) \| + ( \exp ( ( x - x _ { 0 } ) L ) - 1 ) \frac { H m } { L } , } \\ { \qquad L > 0 . } \end{array} \right.
$$
