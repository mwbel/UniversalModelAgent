# 555 Some non-stiff methods

The following method, for which $\begin{array} { r } { c = [ \frac { 1 } { 3 } , \frac { 2 } { 3 } , 1 ] ^ { \intercal } } \end{array}$ , has order 2:

$$
{ [ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] } =  [ \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } &   | \begin{array} { l l l } { 1 } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 1 8 } } } \\ { { \frac { 3 } { 1 0 } } } & { 0 } & { 0 } & { { | \begin{array} { l l l } { 1 } & { { \frac { 1 1 } { 3 0 } } } & { { \frac { 1 1 } { 9 0 } } } \\ { { \frac { 1 } { 5 } } } & { { \frac { 5 } { 1 2 } } } & { 0 } & { { | \begin{array} { l l l } { 1 } & { { \frac { 2 3 } { 6 0 } } } & { { \frac { 7 } { 4 5 } } } \\ { { \frac { 5 } { 3 } } } & { - { \frac { 2 9 } { 1 2 } } } & { { \frac { 4 } { 3 } } } & { { | \begin{array} { l l l } { 1 } & { { \frac { 5 } { 1 2 } } } & { { \frac { 2 } { 9 } } } \\ { - 2 } & { 4 } & { - 1 } & { 0 } & { 0 } \\ { 3 } & { - 9 } & { 6 } & { 0 } & { 0 } \end{array} | } } \end{array} ] } } } \end{array} ] } . \end{array} \end{array}
$$

This method was constructed by choosing $\beta _ { 1 } = - \textstyle { \frac { 1 } { 6 } }$ , $\beta _ { 2 } = \textstyle { \frac { 2 } { 9 } }$ , $\epsilon _ { 0 } = 0$ and requiring $\dot { V }$ to be strictly upper triangular. It could be interpreted as having an enhanced order of 3, but of course the stage order is only 2.

The next method, with $\begin{array} { r } { c = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } , \frac { 3 } { 4 } , 1 ] ^ { 1 } } \end{array}$ , has order 3:

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1 1 4</td><td></td><td>1 32</td><td>1 384 67</td></tr><tr><td>224 403 1851</td><td>0</td><td>0</td><td>0</td><td>1</td><td>45 806</td><td>45 3224</td><td>19344</td></tr><tr><td>2170</td><td>93 280</td><td>0</td><td>0</td><td>1</td><td>3777 8680 473</td><td>681 6944</td><td>297 138880</td></tr><tr><td>305 364</td><td>5 28</td><td>5 12</td><td>0</td><td>1</td><td>1092</td><td>81 728</td><td>17 17472</td></tr><tr><td>305 364</td><td>5 28</td><td>5 12</td><td>0</td><td>1</td><td>473 1092</td><td>81 728</td><td>17</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>17472 0</td></tr><tr><td>156</td><td>188</td><td>-20</td><td>8</td><td>0</td><td>52</td><td></td><td>1</td></tr><tr><td>7</td><td>7</td><td></td><td></td><td></td><td>7</td><td>1</td><td>28</td></tr><tr><td>512 7</td><td>584 7</td><td>160 3</td><td>16</td><td>0</td><td>568 21</td><td>4</td><td>1</td></tr></table>

For this method, possessing property F, $\beta _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ , $\beta _ { 2 } = \textstyle { \frac { 1 } { 1 6 } }$ , $\epsilon _ { 0 } = 0$ . The $3 \times 3$ matrix $\dot { V }$ is chosen so that $\delta ( P ^ { - 1 } \dot { V } P ) = 0$ , where

$$
P = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } \\ { 4 } & { 1 } & { 0 } \end{array} \right] } ~ .
$$
