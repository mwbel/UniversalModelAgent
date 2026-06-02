# 461 Representation of data

After a number of steps, with constant size $h$ , have been carried out using an order $p$ method, for example by a PECE combination of Adams–Bashforth and Adams–Moulton methods, approximations are available to $y ( x _ { n } ) , h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ , $\cdot \cdot \cdot$ , $h y ^ { \prime } ( x _ { n - p + 1 } )$ . If the stepsize is to be altered by a factor $r$ to a new value $r h$ , then there seem to be two distinct approaches to proceeding further.

The first approach is to use a modified form of the Adams formulae which enables $y ( x _ { n } + r h )$ to be written in terms of $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ , . . . , $h y ^ { \prime } ( x _ { n - p + 1 } )$ . Of course this only works for a single step. For the step after that, the data on which to base the approximation would be $y ( x _ { n } + h r )$ , $h y ^ { \prime } ( x _ { n } + h r )$ , $h y ^ { \prime } ( x _ { n } )$ , . . . , $h y ^ { \prime } ( x _ { n - p + 2 } )$ and the results computed would be approximations to $y ( x _ { n } + h r + h r \hat { r } )$ , where $\widehat { r }$ is the stepsize ratio for this new step. Rather than explore the form of the modified Adams formula in this rather ad hoc manner, write the exact quantities that the incoming data is supposed to approximate as the sequence consisting of

$$
y ( x _ { n } - h \theta _ { 1 } ) , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { 1 } ) , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { 2 } ) , \quad \ldots , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { k } ) .
$$

The Adams–Bashforth method would then generalize to an approximation of the form

$$
y ( x _ { n } ) \approx y ( x _ { n } - h \theta _ { 1 } ) + \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } h y ^ { \prime } ( x _ { n } - h \theta _ { i } ) ,
$$

and the Adams–Moulton to an approximation of the form

$$
y ( x _ { n } ) \approx \beta _ { 0 } h y ^ { \prime } ( x _ { n } ) + y ( x _ { n } - h \theta _ { 1 } ) + \sum _ { i = 1 } ^ { k } \beta _ { i } h y ^ { \prime } ( x _ { n } - h \theta _ { i } ) .
$$

To obtain order $p = k$ for (461a), the coefficients $\beta _ { i } ^ { * }$ , $i = 1 , 2 , \ldots , k$ , have to be chosen so that

$$
1 = \exp ( - \theta _ { 1 } z ) + z \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } \exp ( - \theta _ { i } z ) + { \cal O } ( z ^ { p + 1 } ) ,
$$

and to obtain order $p = k + 1$ for (461b), $\beta _ { i }$ , $i = 1 , 2 , \ldots , k$ , are chosen so that

$$
1 = \exp ( - \theta _ { 1 } z ) + z \beta _ { 0 } + z \sum _ { i = 1 } ^ { k } \beta _ { i } \exp ( - \theta _ { i } z ) + O ( z ^ { p + 1 } ) .
$$

To use this approach in practice, the coefficients $\beta _ { 1 } ^ { * }$ , $\beta _ { 2 } ^ { * }$ , $\cdot \cdot \cdot$ and $\beta _ { 0 }$ , $\beta _ { 1 }$ , . . . have to be evaluated afresh every step, before any differential equation solutions are approximated. For many problems this is justified, and many codes use some sort of approach based on this technique.

The second main approach to stepsize adjustment was proposed by Nordsieck (1962) and further developed by Gear (1967, 1971). For a Nordsieck method of order $p$ , the data imported into step $n$ consists of approximations to

$$
y ( x _ { n - 1 } ) , \quad h y ^ { \prime } ( x _ { n - 1 } ) , \quad { \frac { 1 } { 2 ! } } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) , \quad { \frac { 1 } { p ! } } h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) ,
$$

and the quantities exported from this step are approximations to

$$
y ( x _ { n } ) , \quad h y ^ { \prime } ( x _ { n } ) , \quad \frac { 1 } { 2 ! } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) , \quad \frac { 1 } { p ! } h ^ { p } y ^ { ( p ) } ( x _ { n } ) .
$$

Note that the factors $( i ! ) ^ { - 1 }$ are inserted for convenience. When a stepsize change from $h$ to $r h$ is required, the simple adjustment of scaling the quantities in (461c) by powers of the scale factor $r$ is used. This means that they become approximations to

$$
y ( x _ { n } ) , \quad r h y ^ { \prime } ( x _ { n } ) , \quad \frac { 1 } { 2 ! } ( r h ) ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) , \quad \frac { 1 } { p ! } ( r h ) ^ { p } y ^ { ( p ) } ( x _ { n } ) .
$$

Denote the vector of Nordsieck approximations imported into step $n$ by

$$
\begin{array} { l } { \eta _ { 0 } ^ { [ n - 1 ] } \approx y ( x _ { n - 1 } ) , } \\ { \eta _ { 1 } ^ { [ n - 1 ] } \approx h y ^ { \prime } ( x _ { n - 1 } ) , } \\ { \eta _ { 2 } ^ { [ n - 1 ] } \approx \displaystyle \frac { 1 } { 2 ! } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) , } \\ { \quad \quad \vdots \quad \quad \vdots } \end{array}
$$

$$
\eta _ { p } ^ { [ n - 1 ] } \approx \frac { 1 } { p ! } h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) ,
$$

Coefficients, $\gamma _ { 0 }$ $_ { 0 } , \gamma _ { 1 } , \ldots$ , $\gamma _ { p }$ , for Nordsieck methods   

<table><tr><td></td><td></td><td>p=2 p=3 p=4 p=5 p=6</td><td></td><td></td><td></td><td>p=7</td><td>p=8</td></tr><tr><td>70</td><td></td><td></td><td>3</td><td>251</td><td>95</td><td>19087</td><td>5257</td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td>720 1</td><td>288 1</td><td>60480 1</td><td>17280 1</td></tr><tr><td>71</td><td>1</td><td></td><td>11</td><td></td><td>137</td><td>49</td><td>363</td></tr><tr><td>22</td><td></td><td>A</td><td>前</td><td>中</td><td>120</td><td>40 203</td><td>280 469</td></tr><tr><td>73</td><td></td><td></td><td></td><td></td><td></td><td>270 49</td><td>540 967</td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td>192 7</td><td>2880 7</td></tr><tr><td>5</td><td></td><td></td><td></td><td>120</td><td>新</td><td>144 7</td><td>9 23</td></tr><tr><td>76</td><td></td><td></td><td></td><td></td><td></td><td>1440 1</td><td>2160 1</td></tr><tr><td>77 78</td><td></td><td></td><td></td><td></td><td></td><td>5040</td><td>1260 1 40320</td></tr></table>

so that the result computed by the Adams–Bashforth predictor will be

$$
y _ { n } ^ { * } = \eta _ { 0 } ^ { [ n - 1 ] } + \eta _ { 1 } ^ { [ n - 1 ] } + \cdots + \eta _ { p } ^ { [ n - 1 ] } .
$$

If an approximation is also required for the scaled derivative at $x _ { n }$ , this can be found from the formula, also based on a Taylor expansion,

$$
h y ^ { \prime } ( x _ { n } ) \approx \eta _ { 1 } ^ { [ n - 1 ] } + 2 \eta _ { 2 } ^ { [ n - 1 ] } + \cdot \cdot \cdot + p \eta _ { p } ^ { [ n - 1 ] } .
$$

To find the Nordsieck equivalent to the Adams–Moulton corrector formula, it is necessary to add $\beta _ { 0 }$ multiplied by the difference between the corrected value of the scaled derivative and the extrapolated value computed by (461d). That is, the corrected value of $\eta _ { 0 } ^ { \lfloor n \rfloor }$ becomes

$$
\eta _ { 0 } ^ { [ n ] } = \beta _ { 0 } \Delta _ { n } + \eta _ { 0 } ^ { [ n - 1 ] } + \eta _ { 1 } ^ { [ n - 1 ] } + \cdot \cdot \cdot + \eta _ { p } ^ { [ n - 1 ] } ,
$$

where

$$
\Delta _ { n } = h f ( x _ { n } , y _ { n } ^ { * } ) - \sum _ { i = 1 } ^ { s } i \eta _ { i } ^ { [ n - 1 ] } .
$$

In this formulation we have assumed a PECE mode but, if further iterations are carried out, the only essential change will be that the second argument of $h f ( x _ { n } , y _ { n } ^ { * } )$ will be modified.

For constant stepsize, the method should be equivalent to the Adams predictor–corrector pair and this means that all the output values will be modified in one way or another from the result that would have been formed by simple extrapolation from the incoming Nordsieck components. Thus we can write the result computed in a step as

$$
\left[ \begin{array} { c } { \boldsymbol { \eta } _ { 0 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { 1 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { \boldsymbol { \eta } _ { p - 1 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { p } ^ { [ n ] } } \end{array} \right] = \left[ \begin{array} { c } { \gamma _ { 0 } } \\ { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \vdots } \\ { \gamma _ { p - 1 } } \\ { \gamma _ { p } } \end{array} \right] \boldsymbol { \Delta } _ { n } + \left[ \begin{array} { c c c c c c } { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { \cdots } & { p - 1 } & { p } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \binom { p - 1 } { 2 } } & { \binom { p } { 2 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { p } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { \boldsymbol { \eta } _ { 0 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { 1 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { \boldsymbol { \eta } _ { p - 1 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { p } ^ { [ n - 1 ] } } \end{array} \right] .
$$

The quantities $\gamma _ { i }$ , $i = 0 , 1 , 2 , \dotsc , p$ , have values determined by the equivalence with the standard fixed stepsize method and we know at least that

$$
\gamma _ { 0 } = \beta _ { 0 } , \qquad \gamma _ { 1 } = 1 .
$$

The value selected for $\gamma _ { 1 }$ ensures that $\eta _ { 1 } ^ { \lfloor n \rfloor }$ is precisely the result evaluated from η[ ]0 using the differential equation. We can arrive at the correct values of $\gamma _ { 2 }$ , . . . , $\gamma _ { p }$ , by the requirement that the matrix

$$
\left[ \begin{array} { c c c c c } { 1 } & { 3 } & { \cdots } & { \binom { p - 1 } { 2 } } & { \binom { p } { 2 } } \\ { 0 } & { 1 } & { \cdots } & { \binom { p - 1 } { 3 } } & { \binom { p } { 3 } } \\ { \vdots } & & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 1 } & { p } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] - \left[ \begin{array} { c } { \gamma _ { 2 } } \\ { \gamma _ { 3 } } \\ { \vdots } \\ { \gamma _ { p - 1 } } \\ { \gamma _ { p } } \end{array} \right] [ 2 \quad 3 \quad \cdots \quad p - 1 \quad p ]
$$

has zero spectral radius.

Values of the coefficients $\gamma _ { i }$ , $i = 0 , 1 , \dotsc , p$ , are given in Table $4 6 1 ( \mathrm { I } )$ for $p = 2 , 3 , \ldots , 8$ .

Adjustment of stepsize is carried out by multiplying the vector of output approximations formed in (461e) at the completion of step $n$ , by the diagonal matrix $D ( r )$ before the results are accepted as input to step $n + 1$ , where

$$
D ( r ) = \operatorname { d i a g } ( 1 , r , r ^ { 2 } , . . . , r ^ { p } ) .
$$

It was discovered experimentally by Gear that numerical instabilities can result from using this formulation. This can be seen in the example $p = 3$ , where we find the values $\begin{array} { r } { \gamma _ { 2 } = \frac { 3 } { 4 } } \end{array}$ , $\textstyle \gamma _ { 3 } = { \frac { 1 } { 6 } }$ Stability is determined by products of matrices of the form

$$
\left[ \begin{array} { l l } { - { \frac { 1 } { 2 } } r ^ { 2 } } & { { \frac { 3 } { 4 } } r ^ { 2 } } \\ { - { \frac { 1 } { 3 } } r ^ { 3 } } & { { \frac { 1 } { 2 } } r ^ { 3 } } \end{array} \right] ,
$$

and for $r \geq 1 . 6 9 5 6 2$ , this matrix is no longer power-bounded.

Gear’s pragmatic solution was to prohibit changes for several further steps after a stepsize change had occurred. An alternative to this remedy will be considered in the next subsection.
