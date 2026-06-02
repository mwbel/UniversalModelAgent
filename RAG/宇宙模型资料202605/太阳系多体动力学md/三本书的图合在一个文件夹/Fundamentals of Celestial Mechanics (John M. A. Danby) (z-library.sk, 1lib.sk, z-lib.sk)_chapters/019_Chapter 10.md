# Chapter 10

# Numerical Procedures

# 10.1 Differences and Sums

In this chapter we shall describe the notation and procedures involved in some of the numerical work that occurs in celestial mechanics. No attempt hasbeen made to make this account complete; various formulas are quoted, but:no proofs are offered since the chapter is intended partly for reference. Foran account of the theory the reader should consult a work on numerical analysis. Difference notation is not universal; here we shall use that given in Interpolation and Allied Tables,published by H.M.Nautical Almanac Office (Ref.47). This is a small but invaluable volume containing details of many numerical procedures and hints on using them,as well as suitable tables.

Suppose some function, $f ( { \boldsymbol { \mathbf { \mathit { z } } } } )$ , to be tabulated at equal intervals, $h$ ,of the independent variable $\pmb { \mathcal { X } }$ If $\mathtt { r o }$ is some suitable tabular point, then we have a table of values $\hat { \beta } \{ x _ { 0 } + p \hat { \mu } \}$ for integral values of ${ \mathcal { P } } ;$ this may be written $f ( x _ { \mathfrak { p } } )$ ,or simply $f _ { \mathfrak { P } }$ The argument is $\{ x _ { \Updownarrow } + \Im h \}$ ,but this can be written without ambiguity asp.

If we subtract $f _ { \mathfrak { p } }$ from $f _ { { \mathfrak { p } } + 1 }$ , we shall haveformed the first iffrence, $\delta _ { \mathfrak { p } + \frac { \mathfrak { j } } { 2 } }$ It is written to the right of the column of values of $f _ { \vec { \rho } }$ and between the value of fpand $\hat { f } _ { \mathcal { P } \div \updownarrow }$ (see Table 10.1). If we form a column of first differences in this wayand difference this column,we form the second differences. Thus

$$
\delta _ { \mathfrak { p } \div \frac { 1 } { 2 } } - \delta _ { \mathfrak { p } - \frac { 3 } { 2 } } = \delta _ { \mathfrak { p } } ^ { 2 } .
$$

Here the superscript denotes the number of the difference, and the subscript shows the position with respect to the argument. This differencing can be carried out indefinitely, in principle. A formal scheme is shown in Table 10.1.

Table 10.1 can be modified by inserting arithmetical means of the entries tanding immediately above and below a space. These half-differences will ways be preceded by $^ { 6 4 } \mu$ ”Thus

$$
\mu \delta \hat { f } _ { \mathcal { P } } = \frac { 1 } { 2 } ( \delta _ { \mathcal { P } + \frac { 1 } { 2 } } + \delta _ { \mathcal { P } - \frac { 1 } { 2 } } ) .
$$

This is shown in Table 10.2.

Table 10.1   

<table><tr><td colspan="3"></td><td colspan="4">Differences</td></tr><tr><td>Argument Function1st 2nd 3rd</td><td></td><td></td><td></td><td></td><td>4th</td><td></td></tr><tr><td>-2</td><td>f-2</td><td>8信</td><td>82</td><td>8</td><td>82</td><td></td></tr><tr><td>-1</td><td>f-1</td><td></td><td>8</td><td></td><td>s</td><td></td></tr><tr><td>0</td><td>f</td><td>b~</td><td>8</td><td>8</td><td>8</td><td></td></tr><tr><td>+1</td><td>f</td><td></td><td>8</td><td></td><td>8</td><td></td></tr><tr><td>+2</td><td>f</td><td>S</td><td>8</td><td>福</td><td>8</td><td></td></tr></table>

This table is assumed to be part ofa more extensive one. If we start with only the five values tabulated,then only one fourth difference, $\delta _ { \mathfrak { d } } ^ { \sharp }$ can be found,and the difference table ends there.

Table 10.2   

<table><tr><td rowspan="2">Argument Function</td><td rowspan="2"></td><td colspan="4">Differences</td></tr><tr><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1</td><td>f-1</td><td>[u8_1]</td><td>82</td><td>[821]</td><td>8</td><td></td></tr><tr><td rowspan="4">0</td><td>uf-y]</td><td>8 M</td><td>[82</td><td>8 1</td><td>8 </td><td></td></tr><tr><td>fo</td><td>[o]</td><td>8</td><td>[u8]</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>] f</td><td>B [</td><td>8</td><td>8 []</td><td>[o 8</td><td></td></tr></table>

We can regard the tabulated values, $f _ { \mathcal { P } }$ as being the first differences of another function,which we shall call the first sum of $f _ { p }$ The first sums can be regarded in their turn as the differences of the second sums, and so on. We then have the scheme shown in Table 10.3.

In forming a sum there is uncertainty to the extent of an additive constant. There is an analogy here between summing and integrating,and also between differencing and differentiating. In fact the $\delta ^ { \cdot }$ s can be regarded as operators

iat obey the ordinary laws of algebra.

Table 10.3   

<table><tr><td rowspan="2">Argument</td><td colspan="2">Sums</td><td rowspan="2"></td><td colspan="5">Differences</td></tr><tr><td>2nd</td><td></td><td>1stFunction</td><td>1st</td><td>2md</td><td>3rd</td><td>4th</td></tr><tr><td>-2</td><td>8</td><td></td><td>f-2</td><td></td><td>82</td><td></td><td></td><td>82</td></tr><tr><td>-1</td><td>8</td><td>8-1 2</td><td>f-1</td><td>8</td><td>82</td><td>8信</td><td>8</td><td></td></tr><tr><td>0</td><td>62</td><td>-1 1</td><td>f</td><td>8 </td><td>8</td><td>8 </td><td>8</td><td></td></tr><tr><td>+1</td><td>s2</td><td></td><td>f</td><td>b</td><td>8</td><td>8</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>b</td><td></td><td>8 </td><td></td><td></td></tr><tr><td>+2</td><td>2</td><td></td><td>f</td><td></td><td>8</td><td></td><td>8</td><td></td></tr></table>

The notation just used is that of central differences. Another notation, to beused later in this chapter,is that of backward differences.The numbers and theirlocation are precisely the same as they would be in Table 10.3, but the symbols are changed as follows:

Table 10.4   

<table><tr><td rowspan="2">Argument</td><td colspan="2">Sums</td><td rowspan="2"></td><td colspan="5">Differences</td></tr><tr><td>2nd</td><td></td><td>1stFunction1st2nd 3rd 4th</td><td></td><td></td><td></td><td></td></tr><tr><td>-2</td><td></td><td></td><td>f-2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1</td><td>V</td><td>V</td><td>f-1</td><td>-1</td><td>V1</td><td>V</td><td>V</td><td></td></tr><tr><td>0</td><td>A</td><td>V</td><td></td><td>V0</td><td>A</td><td>V</td><td>V</td><td></td></tr><tr><td></td><td>V</td><td>V1</td><td>f</td><td>V1</td><td>V</td><td>V</td><td>V</td><td></td></tr><tr><td>+1</td><td>V²</td><td></td><td>f</td><td></td><td>V</td><td></td><td>V</td><td></td></tr><tr><td></td><td></td><td>V11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>V</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td>D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>+2</td><td></td><td></td><td>f</td><td></td><td>V</td><td></td><td>V</td><td></td></tr></table>

# 10.2 Interpolation

The tables of the preceding section refer to values of $f ( x _ { \mathbb { G } } \div p _ { \ell } )$ for integral values of $\mathfrak { p }$ ；but once an adequate table has been constructed, it can be used for finding the value of $\pmb { \hat { \xi } }$ for any value of $\mathfrak { P }$ that is included comfortably within the range of the table. This is known as interpolation. In the following work we shall assume $0 \leq p < 1$

We notice that if the second differences are negligible or zero (and there need be no distinction in numerical work),then

$$
f _ { p } = f _ { \perp } + p \delta _ { \frac { 1 } { 2 } } .
$$

In most books of tables the interval of tabulation, ${ \vec { n } } ,$ is chosen to be so small that second differences are usually negligible;but this cannot normally be done in a practical calculation. We might suspect that $\hat { \pmb { j } } _ { \pmb { \mathcal { P } } }$ would in general be given bya formula involving successive differences in a way that depends on $\mathfrak { P }$ This is the case; two such relations,out of many,will be described here. The frst is Bessel'sformula:

$$
f _ { \mathcal { P } } = f _ { \hat { 0 } } + { p \delta _ { \frac { 1 } { 2 } } } + { B _ { 2 } } ( \delta _ { \hat { 0 } } ^ { 2 } + \delta _ { \frac { 1 } { 2 } } ^ { 2 } ) + { B _ { 3 } } \delta _ { \frac { 1 } { 2 } } ^ { 3 } + { B _ { 4 } } ( \delta _ { 0 } ^ { 4 } + \delta _ { \frac { 1 } { 2 } } ^ { 4 } ) + \cdot \cdot \cdot
$$

where the $B ^ { \prime } { \mathbf s } .$ or Bessel interpolation coefficients, are functions of $\mathfrak { P }$ For instance

$$
\begin{array} { r } { B _ { 2 } = \frac 1 4 p ( p - 1 ) , \quad B _ { 3 } = \frac 1 { 1 2 } p ( p - 1 ) ( 2 p - 1 ) , \quad B _ { 4 } = \frac 1 { 4 8 } p ( p ^ { 2 } - 1 ) ( p - 2 ) , \dots . } \end{array}
$$

These functions are tabulated in standard references.

The second relation is Everett's formula:

$$
f _ { p } = ( 1 - p ) f _ { 0 } + p f _ { 1 } + E _ { 2 } \delta _ { 0 } ^ { 2 } + F _ { 2 } \delta _ { 1 } ^ { 2 } + E _ { 4 } \delta _ { 0 } ^ { 4 } + F _ { 4 } \delta _ { 1 } ^ { 4 } + \cdot \cdot \cdot
$$

The Everett coefficients are related to the Bessel coefficients by

$$
\vec { \mathcal { E } } \cdot \vec { \mathcal { E } } + \vec { \mathcal { F } } = 2 \mathcal { B } ,
$$

and we also have $E ( \mathfrak { p } ) = E ( 1 - \mathfrak { p } )$ and $\mathcal { E } \{ 1 - p \} = \mathcal { F } \{ p \}$

We shall illustrate the use of these formulas by taking a table of sin $\pmb { \mathscr { x } }$ to six places of decimals where $h = 5 ^ { \circ }$ . This is given in Table 10.4, with differences up to the sixth. When differencing a table, the differences should be taken up to the stage where they become small and irregular; this is the case for the fifth and sixth differences. Since the interpolation coefficients become very small anyway for these differences, they will not contribute anything in the interpolation.

Table 10.5   

<table><tr><td>2</td><td>sinx</td><td>8</td><td>82</td><td>8</td><td>84</td><td>85</td><td>86</td></tr><tr><td>0</td><td>0.000000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>+0.087156</td><td>+87156</td><td>-664</td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>173648</td><td>86 492</td><td>1321</td><td>-657</td><td>+8</td><td></td><td></td></tr><tr><td>15</td><td>258819</td><td>85 171</td><td>1970</td><td>649</td><td>16</td><td>+8</td><td>14</td></tr><tr><td>20</td><td>342 020</td><td>83201</td><td>2603</td><td>633</td><td></td><td>4</td><td>11</td></tr><tr><td>25</td><td>422618</td><td>80598</td><td></td><td>613</td><td>20</td><td>3</td><td></td></tr><tr><td></td><td>500000</td><td>77382</td><td>3216</td><td>590</td><td>23</td><td>+9</td><td>+6</td></tr><tr><td>30</td><td></td><td>73572</td><td>3806</td><td>558</td><td></td><td>-3</td><td>-12</td></tr><tr><td>35</td><td>573576</td><td>69 212</td><td>4364</td><td>529</td><td>29</td><td>+11</td><td>+14</td></tr><tr><td>40</td><td>642 788</td><td>64319</td><td>4893</td><td>489</td><td>40</td><td>+2</td><td>19</td></tr><tr><td>45</td><td>707107</td><td>58937</td><td>5382</td><td></td><td>42</td><td></td><td>-3</td></tr><tr><td>50</td><td>766044</td><td></td><td>5829</td><td>447</td><td>41</td><td>-1</td><td>+11</td></tr><tr><td>55</td><td>819152</td><td>53108</td><td>6235</td><td>406</td><td>51</td><td>+10</td><td>-14</td></tr><tr><td>60</td><td>866025</td><td>46873</td><td>6590</td><td>355</td><td>47</td><td>14</td><td>+11</td></tr><tr><td>65</td><td>906308</td><td>40283</td><td>6898</td><td>308</td><td></td><td>+7</td><td>-6</td></tr><tr><td>70</td><td>939 693</td><td>33 385</td><td></td><td>254</td><td>54</td><td>+1</td><td></td></tr><tr><td></td><td></td><td>26 233</td><td>7152</td><td></td><td>55</td><td></td><td>-1</td></tr><tr><td>75</td><td>965926</td><td></td><td>7351</td><td>199</td><td>55</td><td>0</td><td>+2</td></tr><tr><td></td><td></td><td>18882</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80</td><td></td><td></td><td></td><td>144</td><td></td><td>+2</td><td></td></tr><tr><td></td><td>984808</td><td></td><td>7495</td><td></td><td>+57</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>11387</td><td></td><td>-87</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>85</td><td>996195</td><td></td><td>-7582</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>+3805</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90</td><td>+1.000000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Decimal points can be omitted without ambiguity in this case, with the understanding that quantities are in units of the sixth place.

Let us use this table to find the value of sin $4 1 ^ { \circ }$ ；then $x _ { \Updownarrow } ~ = ~ \frac { 4 } { 2 } 0 ^ { \circ }$ and 0.20oooo.First we shall use the Everett formula. From tables we find

$$
\begin{array} { r l r } { E _ { 2 } = - 0 . 0 4 8 , } & { { } } & { \vec { F } _ { 2 } = - 0 . 0 3 2 , } \\ { \vec { E } _ { 4 } = + 0 . 0 0 8 , } & { { } } & { \vec { F } _ { 4 } = + 0 . 0 0 6 ; } \end{array}
$$

further coefficients are not needed. We then find

$$
\begin{array} { r l r } { \cdot \mathcal { P } ) f _ { 0 } = + 0 . 5 \frac { 1 4 } { 4 } 2 3 3 } & { } & \\ { \cdot \mathcal { P } f _ { 1 } = + } & { 1 . 4 1 4 2 1 } & \\ { E _ { 2 } \delta _ { 0 } ^ { 2 } = + } & { 2 3 5 } & \\ { F _ { 2 } \delta _ { 1 } ^ { 2 } = + } & { 1 7 2 } & \\ { E _ { 4 } \delta _ { 0 } ^ { 4 } = } & { 0 } & \\ { F _ { 4 } \delta _ { 1 } ^ { 4 } = } & { 0 } & \\ { f _ { p } = + 0 . 6 5 6 0 5 8 . } & \end{array}
$$

The appropriate Bessel coefficients are

$$
B _ { 2 } = - 0 . 0 4 0 , \quad B _ { 3 } = + 0 . 0 0 8 , \quad B _ { 4 } = + 0 . 0 0 7 .
$$

We find

$$
\begin{array} { r l r } & { } & { f _ { 0 } = + 0 . 6 4 2 7 8 8 } \\ & { } & { p \delta _ { \frac { 1 } { 2 } } = + \quad 1 2 8 6 4 } \\ & { } & { B _ { 2 } ( \delta _ { 0 } ^ { 2 } + \delta _ { 1 } ^ { 2 } ) = + \quad \quad 4 1 1 } \\ & { } & { B _ { 3 } \delta _ { \frac { 3 } { 2 } } ^ { 3 } = - \quad \quad 4 } \\ & { } & { B _ { 4 } ( \delta _ { 0 } ^ { 4 } + \delta _ { 1 } ^ { 4 } ) = \pm \quad \quad 1 } \\ & { } & { f _ { p } = + 0 . 6 5 6 0 6 0 . } \end{array}
$$

The actual answer, correct to six places, is $\pm 0 . 6 5 6 0 5 9$ ，so that the agreement is good, considering the number of calculations performed.

If the fourth differences are small (less than 10oo),the term in ${ \mathcal { B } } _ { 4 }$ may be neglected if the second differences are modified so that

$$
\delta _ { m o d } ^ { 2 } = \delta ^ { 2 } - 0 . 1 8 4 \delta ^ { 4 } .
$$

The fourth differences are said to have been thrown back. A similar device can beused in Everett's formula. There are more complicated throwbacks involving higher differences: the reader will find these described in the standard references.

If in our example we had required the value of sin $8 6 ^ { \circ }$ ,on the basis of Table 10.5 alone, it would have been necessary to guess some of the differences. This can be done with reasonable confidence,since the run of differences is smooth; we can reasonably assume that the fourth differences will remain at about $\div 5 7$ and so build up the lower differences.If our guess of the fourth differences was wrong by 10,the error in the product $\mathcal { B } _ { \sharp } \delta ^ { 4 }$ would be less than one,and so would not affect the accuracy of the answer.

If we build up extra differences in this way,it is possible to add extra values to the table. Let us assume that the next fourth difference is $\div 5 7 .$ Then,extra third,second,and first differences of-30,-7612,and -3807, respectively，can be added to the table of differences, so that we can deduce that sin95°=+0.996193, giving an error of two only. This process is known asextrapolation.

We can also use Table 10.5 to find the argument for a given value of sin x. This is known as inverse interpolation. It requires successive approximations, unfortunately, there is no direct formula that can be used.

Backward differences also provide convenient notation for interpolation. Suppose that a function is tabulated as in Table 10.6, where f-:= f(to-ih). The important differences are those in the final diagonal. They can easily be computed from the initial table (see below)；also,ifwe know only fo and the lowest diagonal of differences,the values of the function,and all other differences can be recovered. It is the terms in the lowest diagonal that are used in the formula.

# Table 10.6

Let $t = \ t _ { 0 } - \pounds _ { \ell }$ lie in the range of the table, so that $\mathfrak { P }$ is not restricted to interval $\{ \mathfrak { G } , \mathfrak { T } \}$ The formula for interpolating $f ( t _ { 0 } - p h )$ is

$$
\begin{array} { c } { { f ( t _ { 0 } - p h ) \simeq f ( t _ { 0 } ) + \displaystyle \sum _ { n = 1 } ^ { m } c _ { n } ( p ) \nabla _ { 0 } ^ { n } , } } \\ { { { } } } \\ { { { } } } \\ { { { \displaystyle c _ { n } ( p ) = ( - 1 ) ^ { n } { \binom { p } { n } } = ( - 1 ) ^ { n } \frac { p ( p - 1 ) \cdot \cdot \cdot ( p - n + 1 ) } { 1 \cdot 2 \cdot \cdot \cdot \cdot n } } . } } \end{array}
$$

ecoefficients $c _ { \mathfrak { n } }$ can be found recursively from

$$
\begin{array} { l } { { c _ { 0 } ( p ) = 1 , } } \\ { { c _ { n } ( p ) = \displaystyle \frac { n - p - 1 } { n } c _ { n - 1 } ( p ) , \quad n = 1 , 2 , \ldots , m . } } \end{array}
$$

Consider a program for carrying this out. Suppose that we have a table of values of a function and that F(I) stands for f-;. Then if D(I) stands for Vi, they can be found from

$$
\begin{array} { l } { { \mathrm {  ~ \psi ~ } _ { 1 } ^ { \mathrm { { q } } } \odot 0 \mathrm {  ~ \psi ~ } _ { 2 } ^ { \mathrm { { E } } } \Omega \ \stackrel { \mathrm { ~ { ~ \textstyle ~ \frac { 1 } ~ { 2 } ~ } } } { = } \ \frac { \mathrm {  ~ \psi ~ } _ { 1 } ^ { \mathrm { { q } } } } { \Sigma } \ \stackrel { \mathrm {  ~ { ~ \scriptstyle ~ \frac { 1 } ~ { 2 } ~ } } } { = } \ \frac { \mathrm {  ~ \psi ~ } _ { 2 } ^ { \mathrm { { E } } } } { \Sigma } \left( \Sigma \right) } }  \\ { { \mathrm {  ~ \psi ~ } _ { 4 } ^ { \mathrm { { q } } } \odot \ \mathrm {  ~ \psi ~ } _ { 3 } ^ { \mathrm { { E } } } \left( \Sigma \right) \ = \ \frac { \mathrm {  ~ \psi ~ } _ { 1 } ^ { \mathrm { { q } } } } { \Sigma } \ - \ \mathrm {  ~ \psi ~ } _ { 4 } ^ { \mathrm { { F } } } \left( \Sigma \right) } } \\ { { \mathrm {  ~ \psi ~ } _ { 2 } ^ { \mathrm { { q } } } \odot \ \mathrm {  ~ \psi ~ } _ { 3 } ^ { \mathrm { { E } } } \Sigma \ \stackrel { \mathrm { ~ { ~ \textstyle ~ 1 } ~ } } { = } \ 2 \mathrm {  ~ \psi ~ } _ { 3 } ^ { \mathrm { { E } } } \ } } \\ { { \mathrm {  ~ \psi ~ } _ { 4 } ^ { \mathrm { { q } } } \odot \ \mathrm {  ~ \psi ~ } _ { 5 } ^ { \mathrm { { E } } } \Omega \ \stackrel { \mathrm { ~ { ~ \textstyle ~ J ~ } ~ } } { = } \ \frac { \mathrm {  ~ \psi ~ } _ { 3 } ^ { \mathrm { { q } } } } { \Sigma } \ \stackrel { \mathrm {  ~ { ~ \scriptstyle ~ \frac { 1 } ~ { 2 } ~ } } } { = } \ \Sigma \ { \mathbb { 0 } } \ \stackrel { \mathrm {  ~ \psi ~ } _ { 4 } ^ { \mathrm { { q } } } } { = } \ \Sigma \ { \mathbb { 1 } } } } \\  { \mathrm {  ~ \psi ~ } _ { 3 } ^ { \mathrm { { q } } } \Sigma \ \stackrel { \mathrm { ~ \scriptstyle ~ \frac { 1 } { 2 } ~ } } { = } \ \Sigma \ { \left( \Sigma + \Sigma - \frac { \mathrm { ~ \textstyle ~ 1 } } { \Sigma } \right) } \ = \ \mathrm {  ~ \ u ~ } _ { 4 } \ } \\   \mathrm  q \end{array}
$$

If we want to approximate the value of $f ( t )$ by interpolation, then

200P=（TO-T）/H   
210 FINT =F   
220C=1   
230FORN=1 TO   
240 C=C\*（N-P-1）/N   
250 FINT = FINT + C\*D（N）   
260 NEXT N

Writea program for carrying out these computations (preferably in double precision) using a function that can be accurately computed, so that the error of the interpolation will be printed out. Experiment with various h and $\vec { i } \vec { q }$ ,playing with some ridiculous extremes. Also notice how the error mounts steeply if the value of t wanders outside the interval covered by the table.

A Lagrangian formula is one in which the tabular values of $f$ appear,but no differences. For instance,

$$
f ( t _ { 0 } - x ) \simeq \sum _ { n = 0 } ^ { m } p _ { n } ( x ) f ( t _ { 0 } - n h ) ,
$$

where the $p _ { \mathfrak { P } } \{ { \mathfrak { x } } \}$ are polynomials in $\pmb { \mathcal { X } }$ Such formulas will be applied to the solution of differential equations in section 10.7, but are not recommended here for interpolation.

One other useful technique for interpolation involves divided differences. An account of this,with programs,can be found in Refs.49 and 52. Anadvantage of the method is that the values of $f$ do not have to be tabulated at regular intervals,nor,indeed,in any special order.

# 10.3Differentiation

If all the second differences in $\mathtt { a }$ table were zero, the function would be an arithmetical series,and its differential coefficient would be given exactly by

$$
\hbar \frac { d \hat { \vec { y } } } { d \hat { x } } = \hbar \hat { \vec { z } } ^ { \prime } = \frac { \vec { u } \hat { \vec { y } } } { \vec { d } \hat { y } } = \delta _ { \frac { 3 } { 2 } } .
$$

This corresponds to the case (10.2.1） considered in the preceding section,and so we would expect in general to find $f ^ { f }$ given by $\mathtt { a }$ series involving higher. differences. The reader should note the appearance of $\tilde { \mathbf { \Sigma } } _ { \tilde { \mathbf { \Lambda } } }$ on the left-hand side of(10.3.1)；it must never be forgotten.

If the Bessel interpolation coefficients are expressed in terms of $\mathfrak { P }$ then (10.2.2) can be differentiated any number of times to give appropriate formulas successive differential coefficients. We have, for instance,

$$
h \dot { f } _ { p } ^ { t } = \delta _ { \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 4 } } ( 2 p - 1 ) ( \delta _ { 0 } ^ { 2 } + \delta _ { 1 } ^ { 2 } ) + B _ { 3 } ^ { \prime } \delta _ { \frac { 1 } { 2 } } ^ { 3 } + B _ { 4 } ^ { \prime } ( \delta _ { 0 } ^ { 4 } + \delta _ { 1 } ^ { 4 } ) + \cdot \cdot \cdot
$$

he Bn are tabulated in the standard references. As in the case of interpolation, hereare alternative formulas.

Often only the derivatives at tabular or half-tabular points are required. he.coefcients can then be given definite mumerical values. For tabular points rehave

$$
\begin{array} { r } { \hbar \dot { f } _ { 0 } ^ { \prime } = \mu \delta _ { 0 } - \frac { 1 } { 6 } \mu \delta _ { 0 } ^ { 3 } + \frac { 1 } { 3 0 } \mu \delta _ { 0 } ^ { 5 } - \frac { 1 } { 1 4 0 } \mu \delta _ { 0 } ^ { 7 } \div \cdot \cdot \cdot } \end{array}
$$

$$
\begin{array} { r } { \hbar ^ { 2 } \hat { J } _ { 0 } ^ { \prime \prime } = \delta _ { 0 } ^ { 2 } - \frac { 1 } { 1 2 } \delta _ { 0 } ^ { 4 } \div \frac { 1 } { 9 0 } \delta _ { 0 } ^ { 6 } \div \cdot \cdot \cdot } \end{array}
$$

Asan illustration let us find the differential coefficient of sin 40°from Table 0.4.Expressed in radians, $\hslash$ is 0.0872665.We find

$$
\mu \delta _ { 0 } = \div 6 6 7 6 6 ,
$$

$$
\begin{array} { r } { \frac { 1 } { 6 } \mu \delta _ { 0 } ^ { 3 } = \div 8 5 , } \end{array}
$$

from which we find

$$
\begin{array} { l } { { \sin ^ { \prime } { 4 \Omega ^ { \circ } } = + 0 . 0 6 6 6 8 1 \ \mathrm { \ d i v i d e d ~ b y ~ 0 . 0 8 7 ~ 2 6 6 } } } \\ { { \qquad = + 0 . 7 6 6 0 6 . } } \end{array}
$$

s compares with the correct figure, 0.766 04.

The formulas for the derivatives at half-tabular points are

$$
\begin{array} { r } { \hbar \hat { f } _ { \frac { 1 } { 2 } } ^ { \prime } = \delta _ { \frac { 1 } { 2 } } - \frac { 1 } { 2 4 } \delta _ { \frac { 1 } { 2 } } ^ { 3 } + \frac { 3 } { 6 4 0 } \delta _ { \frac { 1 } { 2 } } ^ { 5 } - \cdots } \end{array}
$$

$$
\begin{array} { r } { \hbar ^ { 2 } \dot { \hat { J } } _ { \frac { 1 } { 2 } } ^ { \prime \prime } = \mu \delta _ { \frac { 1 } { 2 } } ^ { 2 } - \frac { 5 } { 2 4 } \mu \delta _ { \frac { 1 } { 2 } } ^ { 4 } + \frac { 2 5 9 } { 5 7 6 0 } \mu \delta _ { \frac { 1 } { 2 } } ^ { 6 } - \cdot \cdot \cdot } \end{array}
$$

# 10.4 Integration

The analogy between sums and integrals (or the direct integration of Bessel's nterpolation formula) leads us to expect a formula of the type

$$
\int ^ { p } \ f _ { p } \dot { d p } = \delta _ { \frac { 1 } { 2 } } ^ { - 1 } + A _ { 0 } ^ { \frac { 1 } { 2 } } \big ( f _ { 0 } + f _ { 1 } \big ) + A _ { 1 } ^ { \frac { 1 } { 2 } } \delta _ { \frac { 1 } { 2 } } + A _ { 2 } ^ { \frac { 1 } { 2 } } \big ( \delta _ { 0 } ^ { 2 } + \delta _ { 1 } ^ { 2 } \big ) + \cdot \cdot \cdot
$$

forthe integral of $\hat { \xi } _ { p }$ This is the case,and the $A$ 'sare tabulated in standard references.Asimilar formula holds for double integrals; these involve the second

sums. We note that

$$
\int f ( x ) d x = h \int f _ { \mathcal { P } } d \vec { \mathcal { P } } .
$$

For our purposes we shall need only to evaluate integrals at tabular points, for which $z = 0$ Then we have

$$
\begin{array} { c } { { \displaystyle h ^ { - 1 } \int ^ { 0 } f ( x ) d x = \int ^ { 0 } f _ { p } d p } } \\ { { = \mu \delta _ { 0 } ^ { - 1 } - \frac { 1 } { 1 2 } \mu \delta _ { 0 } + \frac { 1 1 } { 7 2 0 } \mu \delta _ { 0 } ^ { 3 } - \frac { 1 9 1 } { 6 0 4 8 0 } \mu \delta _ { 0 } ^ { 5 } + \cdot \cdot \cdot } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle { \hbar } ^ { - 2 } \int \int ^ { 0 } f ( x ) d x ^ { 2 } = \int \int _ { } ^ { 0 } f _ { p } d p ^ { 2 } } } \\ { { \displaystyle \qquad = \mu \delta _ { 0 } ^ { - 2 } + \frac { 1 } { 1 2 } f _ { 0 } - \frac { 1 } { 2 4 0 } \delta _ { 0 } ^ { 2 } + \frac { 3 1 } { 6 9 4 8 9 } \mu \delta _ { 0 } ^ { 4 } - \cdots } } \end{array}
$$

These expressions will be needed later when we consider the numerical solution of differential equations.

The notation $f ^ { \cdot \mathbf { p } }$ is confusing because an integral must have two limits for it to have a definite value. Specifying only the upper limit results in uncertainty to the extent of an added constant; but this is related in (10.4.1) to the uncertainty in forming the frst sums. We can express a definite integral as

$$
\int _ { q } ^ { \vec { p } } f d \vec { p } = \int _ { C } ^ { \vec { p } } f d \vec { p } - \int _ { C } ^ { q } f d \vec { p } ,
$$

where $C$ is arbitrary. Then let us omit the $C$ altogether and apply (10.4.1） to each integral. The final answer for the definite integral will not be influenced by the choice of arbitrary constant when forming the first sums,as this will disappear in the subtraction.

When solving a differential equation, the sums must be known definitely; in this case they are found by using the initial conditions. Suppose we are required to calculate $y$ from

$$
\frac { d \hat { y } } { d z } = \sin x ,
$$

subject to the initial condition that when $\mathfrak { L } = 4 5 ^ { \circ }$ $y = - 0 . 7 0 7 1 0 7$ Using Table 10.4, let $z _ { \mathrm { 0 } } = 4 5 ^ { \circ }$ ； then from (10.4.2) we find

$$
- 0 . 7 0 7 1 0 7 = h ( \mu \delta _ { 0 } ^ { - 1 } - 0 . 0 0 5 1 4 3 ) ,
$$

from which

$$
\mu \delta _ { 0 } ^ { - 1 } = - 8 . 0 9 7 7 0 7 ,
$$

where the final digit is unreliable. Then since

$$
\delta _ { \frac { 1 } { 2 } } ^ { - 1 } - \delta _ { - { \frac { 1 } { 2 } } } ^ { - 1 } = + 0 . 7 0 7 1 0 7 , \quad
$$

we find

$$
\delta _ { \frac { \ddagger } { 2 } } ^ { - 1 } = - 7 . 7 4 4 1 5 4 .
$$

Using this value, the complete column of first sums can be entered into Table 10.4,and the application of (10.4.2） will yield values of -cosx. The reader should verify that this is,in fact,the case.

Definite integrals are often evaluated mumerically by using values of the function to be integrated at tabular points,instead of its sums and differences. There are many suitable formulas; here we shall quote only one, known as the repeated Simpson rule. Let the function y = f(x) be integrated from xo = α ton= b,and suppose $\mathfrak { Y }$ to be tabulated for all the $\mathcal { Z } _ { i }$ such that $y _ { i } = f _ { i } ( x _ { i } )$ ， =1,2,3,..,n.We assume that n is even.Then

$$
y d x = { \frac { b - a } { 3 n } } ( y _ { 0 } + 4 y _ { 1 } + 2 y _ { 2 } + 4 y _ { 3 } + 2 y _ { 4 } + \cdots + 2 y _ { n - 2 } + 4 y _ { n - 1 } + y _ { n } ) .
$$

The:error of this formula is proportional to the fourth power of $h$ ，theinterval ftabulation,making the approximation adequate for many purposes,as well as being simple to use.

If you must evaluate a lot of integrals numerically， then you should acquire etechnique of Gaussian integration.

# 10.5Errors

In.a world in which the stored precision of a number must be limited, and we are to use finite numerical procedures to approximate the results of calculus, umerical errors are unavoidable and natural. In this section we shall look atsome aspects of their nature and control.“Error” in this context should bedistinguished from “blunder".Blunders can happen because a program is not completely debugged, or because the INPUT quantities have errors in them,or because the operator does not understand the natural limitations ofa program, or the OUTPUT quantities are misinterpreted. Remember that the hardest part of debugging starts after the program has run all the way forthe first time.This is why it is important,whenever possible, to apply aprogram first to problems for which the solution is known. Also debugging should be comprehensive; for instance, if an angle is to be computed from inverse trigonometric functions, then the program should be run for enough cases to ensure the correctness of the quadrant. Before starting a calculation,you should have some idea as to what the DUTPUT should look like, so that you can spot absurdities. This requires experience. There may be internal checks that can be used. For instance, a system of differential equations may have an integral, i.e., a function of the variables that is constant along any solution. (Conservation of energy,for instance, or Jacobi's integral in the restricted problem.) Monitoring this function at each state of the integration can make possible an early warning if something is going wrong.

The respectable errors to be discussed arise from two causes. Round-off error is due to finite word length. Truncation error is due basically to the fact that while a mathematical result may depend on a limiting process (the convergence of a series, for instance),we are limited to a finite number of steps.

In the past,a potent reason for the seriousness of round-off error was the fact that in most calculations every digit was precious. This need not be the case today. In simple calculations, round-off errors will be mostly (but not invariably) confined to the final two or three decimal places; so if we require, ten-figure accuracy, and use double precision, the round-off errors may be safely out of sight. They should never be out of mind; ultimately，if a program is large enough,or runs for long enough,round-off errors can kill it. Certain bad programming practices can expedite the process; subtracting nearly equal quantities, for instance, or using units unwisely so that quantities in the same formula (position and velocity，say) can have very different orders of magnitude. When debugging a program, using a model with known results, be satisfied only with agreement consistent with the precision that you are using.

A good way to get some experience with truncation error is to experiment with the program of section 10.2, varying M.A mathematical formula of interpolation using differences would involve an infinite series;in theory, it might seem that the more differences we use, the better will be the results. This is only true up toa point. We try to illustrate this using Table 10.7. If the entries in a table are rounded off to $\Bbbk$ decimal places, then the neglected parts will lie between $\pm \frac { 1 } { 2 }$ ; these errors will affect the differences, and the maximum possible effcts are shown by assuming that the errors are alternatively $+ \frac { 1 } { 2 }$ and $- \textstyle { \frac { 1 } { 2 } }$ ,in units of the final decimal used. Suppose, for example, that we are dealing with a tabulated function where (were there no round-off error) the sixth differences would be near zero; it is easy to see that any numbers that actually appear in the sixth differences (and they could be as great as 32) are garbage, and that any calculation involving them is contributing nonsense. The higher the differences that are involved, the greater is the danger.

Table 10.7

$$
\begin{array} { r l } & { \quad + \frac { 1 } { 2 } \frac { \delta } { \mathrm { ~  ~ \gamma ~ } } - \frac { \delta ^ { 2 } } { \mathrm { ~  ~ \gamma ~ } } \frac { \delta ^ { 3 } } { \mathrm { ~  ~ \gamma ~ } } \frac { \delta ^ { 4 } } { \mathrm { ~  ~ \gamma ~ } } \frac { \delta ^ { 5 } } { \mathrm { ~  ~ \gamma ~ } } \qquad \frac { \delta ^ { 6 } } { \mathrm { ~  ~ \gamma ~ } } } \\ & { \quad - \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } + 2 \mathrm { ~  ~ \gamma ~ } - 8 \mathrm { ~  ~ \gamma ~ } - 1 6 \mathrm { ~  ~ \gamma ~ } - 3 2 } \\ & { \quad - \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } + 1 \mathrm { ~  ~ \gamma ~ } \mathrm { ~  ~ \gamma ~ } - 4 \mathrm { ~  ~ \gamma ~ } } \\ & { \quad + \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } - 2 \mathrm { ~  ~ \gamma ~ } + 4 \mathrm { ~  ~ \beta ~ } } \\ & { \quad - \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } - 1 \mathrm { ~  ~ \gamma ~ } + 2 \mathrm { ~  ~ \gamma ~ } - 8 \mathrm { ~  ~ \gamma ~ } - 1 6 \mathrm { ~  ~ \gamma ~ } . } \\ & { \quad + \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } + 1 \mathrm { ~  ~ \gamma ~ } - 2 \mathrm { ~  ~ \gamma ~ } - 4 } \\ & { \quad - \frac { 1 } { 2 } \mathrm { ~  ~ \gamma ~ } - 1 } \end{array}
$$

The rest of this chapter is concerned with the numerical solution of a system of differential equations. Before looking at some specific methods, we need to makea few general points. Any method proceeds in steps; the independent variable is increased by a quantity $\hslash$ called the stepsize. Associated with a step there will be local truncation error that will depend on the method used and on thestepsize. This error can usually be approximated by an expression of the form Ah.Mathematically,we could say that the limit,as $\hslash$ approaches zero, of(local truncation error) $r _ { k } z ^ { k }$ exists,and is equal to A. The number $( k - 1 )$ is called the order of the method. The step will also suffer from round-off error. Soeven if conditions were perfect at the start of a step,there will be error at the end.We have consequently been set onto a different solution path of the differential equations. The error will propagate into future steps, giving accumulated error, which depends not only on the numerical method used, but also on the nature of the differential equations. This can be serious. Consider

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = x ; \qquad x ( 0 ) = 1 , \quad \dot { x } ( 0 ) = - 1 .
$$

The general solution is $x = c _ { 1 } e ^ { \frac { t } { 2 } } + c _ { 2 } e ^ { - { \frac { t } { 2 } } }$ ；applying the initial conditions, and assuming perfect precision,we find $c _ { 1 } = 0$ and $c _ { 2 } = \frac { \pi } { 2 }$ ,so the solution decays exponentially.But at the end of the first step of a numerical integration we shall be ona different solution path-one for which $\mathcal { C } _ { \mathfrak { I } }$ is not zero;however small this false $c _ { 1 }$ may be,we shall now be on a solution path that has exponential growth.

Inorbital work the principal effect of errors can be seen by considering Keplerian motion.A small error in position and velocity will lead to small errors in the elements,so that the size,shape and orientation of the orbit will bechanged, but only by a correspondingly small amount. But since the mean motion will be changed, the mean anomaly will have an error that increases steadily with the time.So the principal error in most orbital integrations is in the position along the orbital path,rather than in the path itself. Physically, this corresponds to fragments of a comet spreading out along the orbit of the comet.

Numerical methods for the solution of differential equations can be classified under single-step and multistep methods. In the first, every step taken is like aninitial value problem; no account is taken of the past history of the solution. Such methods include the application of power series and Runge-Kutta methods.Power series can be powerful and are especially useful if a set of equations isto be solved many times; but each problem must be programmed individually. They will not (with regret) be discussed here; an introduction to their use, with applications, can be found in Ref. 52. In a single-step method the stepsize canbe changed at each step; if a solution is uneventful, h can be increased, but itmust be decreased as the action becomes more exciting. In Section 10.6 we describe a Runge-Kutta method that has automatic stepsize control.

Runge-Kutta methods are usually of low order and are slow because for   
each step the right-hand sides of the equations must be calculated many times.   
Multistep methods use results from preceding steps; they are faster in operation   
and can easily be designed to higher order. But variation of the stepsize is   
cumsy.Usually it is either halved or doubled. Doubling requires storage of a   
lot of previous calculations; halving requires interpolation. The operations are ：

not difficult, and involve only programming considerations. More troublesome is the logic for deciding whether or not the stepsize should be changed; here opinions may difer. For reasons of space, stepsize control for multistep methods will not be included in the programs to be described.

Multistep methods can be set out to use tabular values (Lagrangian formulas) or differences. Tabular values are more commonly used today, although I prefer differences. In section 10.7 a method is given for first-order equations using Lagrangian formulas. In section 10.8 you will find the traditional method of celestial mechanics for second-order equations.

# 10.6 The Numerical Integration of Differential Equations-Runge-Kutta Methods

The subject of the numerical solution of differential equations is vast and wonderful; here I offer only the briefest introduction,with the outlines of some basic methods,and, I hope, some useful ideas for programs. On no account should you allow your knowledge to be restricted by what is contained in this book.There is an element of art to the subject.A lot of judgment is needed; so experience,gained through experiment,is important.

Methods will be described here in the first place for single equations,but the programs will apply to systems. Runge-Kutta methods are single-step methods, which means that each step is like starting an initial value problem, being independent of whatever went before. Consider

$$
\frac { \dot { d } x } { \dot { d } \dot { \tau } } = \dot { f } ( \dot { t } , x ) ; x ( \dot { \varepsilon } _ { 0 } ) = x _ { 0 } .
$$

The best known Runge-Kutta method has for a step, with stepsize $\Bbbk$ the following operations:

$$
\begin{array} { r l } & { f _ { 0 } = f ( t _ { 0 } , x _ { 0 } ) , } \\ & { f _ { 1 } = f ( t _ { 0 } + \frac { 1 } { 2 } h , x _ { 0 } + \frac { 1 } { 2 } h f _ { 0 } ) , } \\ & { f _ { 2 } = f ( t _ { 0 } + \frac { 1 } { 2 } \tilde { h } , x _ { 0 } + \frac { 1 } { 2 } \tilde { h } f _ { 1 } ) , } \\ & { f _ { 3 } = f ( t _ { 0 } + h , x _ { 0 } + h f _ { 2 } ) , } \\ & { x ( t _ { 0 } + \tilde { h } ) \simeq x _ { 1 } = x _ { 0 } + \frac { 1 } { 6 } \big ( f _ { 0 } + 2 f _ { 1 } + 2 f _ { 2 } + f _ { 3 } \big ) . } \end{array}
$$

This method is of the fourth order. This means that for small enough $\tilde { \hbar }$ the error of the approximation can itself be approximated by $\mathbb { A } \mathbb { \tilde { \hbar } } ^ { 5 }$ ,for $\hat { A }$ independent of $\ z _ { 2 }$ ;or

$$
x ( t _ { 0 } \div h ) - x _ { \perp } \simeq A h ^ { 5 } .
$$

A great advantage of this algorithm is that it is quick and easy to program; but for most orbital calculations it is neither accurate nor fast enough to run. It will be used.in the following section to set up a table of values of (to+nh）， ${ \mathfrak { R } } = { \widehat { \mathbb { 0 } } } , { \widehat { \mathbb { i } } } , \dots$ so that a more powerful method of solution can then estarted.

But one modification of the Runge-Kutta method will be described here in detail. It allows for full automatic control of the stepsize from one step to the next,in conformity with an error bound that can be set by the operator. It is one of a class of methods due to Fehlberg,E.(Ref.51).He has published algorithms for many different orders; the one chosen here can give fifth-order accuracy. In essence, the method runs,in tandem, two algorithms; at the end ofa step there are two separate approximations for $\pmb { \mathscr { x } }$ ： $\mathfrak { X } _ { 1 }$ has fourth-order,and has fifth-order accuracy.So

$$
x ( t _ { 0 } + h ) \simeq x _ { 1 } + A \dot { h } ^ { 5 } , ~ x ( t _ { 0 } + h ) \simeq \hat { x } _ { 1 } + B \dot { h } ^ { 6 } .
$$

Thedifference $\{ \hat { x } _ { \tt i } - z _ { \tt i } \}$ is therefore an approximation to the local truncation error of the approximation ${ \mathfrak { X } } _ { 1 }$ .The stepsize is calculated,or adjusted, so that this difference will always be less than some prescribed quantity. If the error of xis less than this quantity, so,a fortiori,will be the error of $\hat { \boldsymbol { z } } _ { \mathfrak { I } } ; \hat { \boldsymbol { z } } _ { \mathfrak { I } }$ is used as the starting value for the next step.

Let

$$
\mathcal { T } \mathcal { \vec { E } } = | \hat { \boldsymbol { \mathfrak { x } } } _ { \mathrm { \scriptsize 1 } } - \boldsymbol { \mathfrak { x } } _ { \mathrm { \scriptsize 1 } } | .
$$

ippose that we have just calculated a step in the integration. $\pmb { \mathcal { Z } } \pmb { \mathcal { E } }$ is calculated; it is too large,or, say， if

$$
\mathbb { Z } \mathbb { Z } > \mathbb { Z } \mathbb { Z } ,
$$

where TL is the greatest tolerable local truncation error, then the step cannot beused, and must be repeated with a smaller stepsize. But if $\mathbb { Z } < \mathbb { Z } \mathbb { Z } .$ then the step was good, and we need to find a stepsize for the next step. Either way, whena step has been calculated, a new value of $\ z _ { k }$ must be found.

Now, approximately,

$$
\mathcal { F } \mathcal { E } \simeq A \hbar ^ { 5 } , \quad \mathrm { s o } \quad A \simeq \frac { \mathcal { T } \mathcal { Z } } { \hbar ^ { 5 } } .
$$

the local truncation error resulting from a new stepsize $j _ { z _ { j } }$ were to equal $\mathbb { Z } ,$ en

$$
\begin{array} { r } { A \hbar _ { \perp } ^ { 5 } \simeq \mathcal { T } \tilde { L } , } \end{array}
$$

so from (10.6.7),

$$
R _ { 1 } \simeq \left( \frac { T L } { A } \right) ^ { 1 / 5 } \simeq h \left( \frac { T L } { T E } \right) ^ { 1 / 5 } .
$$

t would be dangerous to replace $\mathbf { \tilde { s e } } _ { \simeq } \mathbf { \tilde { s } } ^  $ by $^ { 6 4 } = ^ { 5 9 }$ to give a formula for $\check { h } _ { \ I }$ ,because fall the approximations made. Accordingly， set

$$
\hbar _ { \perp } = C E \cdot \hbar \left( \frac { \mathcal { T } \mathcal { L } } { \mathcal { T } \mathcal { E } } \right) ^ { 1 / 5 } ,
$$

where CH,the “chicken factor”,is a number less than one. I have found that $\sigma H = . 9$ is usually satisfactory， ensuring that TE will actually be less than TL. Its value can change in different circumstances, depending on the system to be solved,and the courage of the operator.

The basic formulas follow. The notation has been changed from that origi-naly used by Fehlberg in order to eliminate zero subscripts, making programing in FORTRAN easier.

For

$$
\frac { d \boldsymbol { x } } { d t } = \boldsymbol { \mathscr { f } } ( t , \boldsymbol { x } ) ; \quad \boldsymbol { x } ( t _ { 0 } ) = \boldsymbol { x } _ { 0 } ,
$$

let

$$
\begin{array} { r l } & { f _ { 1 } = f ( \bar { t } _ { 0 } , x _ { 0 } ) , } \\ & { f _ { 2 } = f [ \bar { t } _ { 0 } + a _ { 2 } h , x _ { 0 } + h ( b _ { 2 1 } f _ { 1 } ) ] , } \\ & { f _ { 3 } = f [ \bar { t } _ { 0 } + a _ { 3 } h , x _ { 0 } + h ( b _ { 3 1 } f _ { 1 } + b _ { 3 2 } f _ { 2 } ) ] , } \\ & { f _ { 4 } = f [ \bar { t } _ { 0 } + a _ { 4 } h , x _ { 0 } + h ( b _ { 4 1 } f _ { 1 } + b _ { 4 2 } f _ { 2 } + b _ { 4 3 } \hat { f } _ { 3 } ) ] , } \\ & { f _ { 5 } = f [ \bar { t } _ { 0 } + a _ { 5 } h , x _ { 0 } + h ( b _ { 5 1 } f _ { 1 } + b _ { 5 2 } f _ { 2 } + b _ { 5 3 } f _ { 3 } + b _ { 5 4 } \hat { f } _ { 4 } ) ] , } \\ & { f _ { 6 } = f [ \bar { t } _ { 0 } + a _ { 6 } h , x _ { 0 } + h ( b _ { 6 4 } f _ { 1 } + b _ { 6 2 } \hat { f } _ { 2 } + b _ { 6 3 } \hat { f } _ { 3 } + b _ { 6 4 } f _ { 4 } + b _ { 6 5 } f _ { 5 } ) ] , } \\ & { x _ { 1 } = x _ { 0 } + h ( c _ { 1 } f _ { 1 } + c _ { 2 } f _ { 2 } + c _ { 3 } f _ { 3 } + c _ { 4 } f _ { 4 } + c _ { 5 } f _ { 5 } ) , } \\ & { \hat { x } _ { 1 } = x _ { 0 } + h ( \hat { c } _ { 1 } f _ { 1 } + \hat { c } _ { 2 } f _ { 2 } + \hat { c } _ { 3 } f _ { 3 } + \hat { c } _ { 4 } f _ { 4 } + \hat { c } _ { 6 } f _ { 6 } ) . } \end{array}
$$

The values of the constants are given in Table 10.8.

Table 10.8   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>aKA(K)</td><td rowspan=1 colspan=5>bKL=B(K,L）</td><td rowspan=2 colspan=1>CKC(K）</td><td rowspan=2 colspan=1>CKCH(K）</td></tr><tr><td rowspan=1 colspan=1>L=1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>K=123456ww</td><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>11281716432</td><td rowspan=1 colspan=1>A243128274品</td><td rowspan=1 colspan=1>135642751</td><td rowspan=1 colspan=1>154</td><td rowspan=1 colspan=1>5144</td><td rowspan=1 colspan=1>0西</td><td rowspan=1 colspan=1>474500</td></tr></table>

From this it follows that

$$
{ \begin{array} { r l } & { { \mathcal { I } } ^ { E } E ^ { 2 } = { \hat { x } } _ { 1 } - x _ { 1 } } \\ & { \qquad = h \left( - { \frac { 1 } { 1 5 5 } } f _ { 1 } + { \frac { 3 } { 1 0 0 } } f _ { 3 } - { \frac { 1 6 } { 7 5 } } f _ { 4 } - { \frac { 1 } { 2 0 } } f _ { 5 } + { \frac { 6 } { 2 5 } } f _ { 6 } \right) . } \end{array} }
$$

In the program $\pmb { \mathcal { Z } } \pmb { \mathcal { B } }$ and $\hat { \boldsymbol { { \mathbf { z } } } } _ { 1 }$ are calculated, but not $\mathfrak { X } _ { \mathfrak { X } }$ ;the coefficients in (10.6.10) are stored as CT(I).

To be useful, these formulas must be generalized to apply to a system of firsttder equations. This generalization can be considered in terms of programing. We shall consider a system of $N Q$ equations: 1

$$
\frac { d X ( I ) } { d T } = F _ { I } [ T , X ( 1 ) , X ( 2 ) , \ldots , X ( N Q ) ] , \quad I = 1 , 2 , \ldots , N Q .
$$

The f's computed in (10.6.9) must be taken for each equation,so that a double array, $\ f _ { i j }$ or F(I,J),will be generated,with $\dot { \mathfrak { z } }$ (I）going from1 to $6$ and j（J）going from 1 to NQ.Then,generalizing (10.6.10）,there will be $I _ { 1 } ^ { 3 } = 2$ separate values of $\mathcal { T B } ,$ hence the appearance of the array TE(I).The greatest of these, in absolute value, is what Fehlberg calls TEMAX; it is TM in the program. TEMAX is used in the calculation of the next stepsize.To calculate the right-hand sides of the equations (10.6.11)it is necessary to write a subroutine which,when given values for $\mathfrak { t } , \mathfrak { x } _ { 1 } , \mathfrak { x } _ { 2 } , \ldots , \mathfrak { x } _ { N Q }$ will have as output $Z _ { i } = f _ { i } ( \underline { { { t } } } , x _ { 1 } , x _ { 2 } , \dots , x _ { N Q } )$ (or the equivalent,with changed notation). This starts at line 1oo0 in the program. But what do we do if we do not start with a system of the form (10.6.11)? Suppose that we want to integrate numerically the system:

$$
\begin{array} { l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = F X ( t , x , y , z , \dot { x } , \dot { y } , \dot { z } ) , } \\ { \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } = F Y ( t , x , y , z , \dot { x } , \dot { y } , \dot { z } ) , } \\ { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } = F Z ( t , x , y , z , \dot { x } , \dot { y } , \dot { z } ) . } \end{array}
$$

$$
X _ { 1 } = x , \quad X _ { 2 } = y , \quad X _ { 3 } = z , \quad X _ { 4 } = \dot { x } , \quad X _ { 5 } = \dot { y } , \quad X _ { 6 } = \dot { z } .
$$

Then the original system can be written in the form:

$$
\begin{array} { r l } & { \frac { d X _ { 1 } } { d t } = X _ { 4 } , } \\ & { \frac { d X _ { 2 } } { d t } = X _ { 5 } , } \\ & { \frac { d X _ { 3 } } { d t } = X _ { 6 } , } \\ & { \frac { d X _ { 4 } } { d t } = F X ( t , X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 5 } , X _ { 6 } ) , } \\ & { \frac { d X _ { 5 } } { d t } = F \bar { Y } ( t , X _ { 3 } , X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 5 } , X _ { 6 } ) , } \\ & { \frac { d X _ { 6 } } { d t } = F \bar { Z } ( t , X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 5 } , X _ { 6 } ) . } \end{array}
$$

Any system of higher-order equations can be reduced to a system of first-order equations bya device of this kind.

In the following listing the functions subroutine is shown for pure Keplerian motion,and the initial conditions are the same as those used in section 6.8. The program should,anyway，be debugged using a problem for which a check is available. In starting up the program, there must be an initial suggestion for the stepsize； if it is too large, the program will automatically reduce it; if it is too small,the program will use it for one (good） step,and then increase it. In the program the greatest tolerable local truncation error was $\mathfrak { T } ^ { \underline { { \tau } } } = \mathfrak { i } \mathfrak { V } ^ { - \overline { { \tau } } }$ It was arranged that the program would finish with the value ${ \vec { \tau } } = 1$ (MT).This is accomplished by working until MT is exceeded, and then taking a (negative) step to land precisely on MT; in this way the very last step is guaranteed to be good.

The program took steps giving tabulated values at the times: .1, .2191.., .3387..,.4593..,.5817...7069.,.8337...9583..,1.0816..,and1.The final values (with those from section 6.8 in brackets for comparison) were:

$\overrightarrow { \mathbfit { L } } = \overrightarrow { \mathbfit { L } }$ ${ \mathfrak { X } } =$ .4660807619349315 （ .466 0807846539234), $y =$ .9006112133419389 （ .9006112349077236), z= .1140459793096798 （ .114 0459806673234), x=-.876 5944425796892 (-.876 594436 852 5084), y=.4731565936190367 (.4731566049794786), z=.1931594909873066( .1931594924439623).

The results conform with the accuracy requirement. But remember that after many steps the accumulated truncation error will increase without bound.

Program the method in the way that you think is best. Debug it carefully. Run some cases using ellptic orbits with high eccentricity in order to appreciate the luxury of the stepsize control.

A more detailed account of this method, together with fowcharts and exercises for debugging, can be found in the author's “Computing Applications to Differential Equations”, Ref. 52. This reference also includes listings in FOR-TRAN and PASCAL. I recommend that you read Fehlberg's papers, if only to appreciate the genius that was responsible for this very elegant algorithm.

REH RUNGE-KUTTA-FEHLBERG 4（5）.REM THE PROGRAN SOLVES A SYSTEN OF NQ FIRST-ORDERREH DIFFERENTIAL EQUATIONS.IT GIVES RESULTS OFREN FIFTH ORDER ACCURACY.SEE NASA TR R315 （1969）.DEFDBL A-H,O-Z:DEFINT I-NDIH A(6）,B(6,7),CH（6）,x(6）,Z(6）,XT(6）,TE(6）,F(6,6）RENSUITABLE FOR SIX SIHULTANEOUS FIRST-ORDER EQUATIONS8 =2#/9（3)=1#/3:（4）=3/4 =1:A（6）=5#/6100 110 18 : = 112140B（63） =13#/16:B（6,4）=4#/27#:B（6,5)=5/144150 CH（）= 47#/450:CH（2）=0:CH（3）=12#/25#190 REM THIS COAPLETES THE.LISTING OF THE COEFFICIENTS.200 NQ= 6 :REK NUHBER OF EQUATIONS IN.THE SYSTEN.

220 REN GREATEST TOLERABLE LOCAL TRUNCATION ERROR.  
230H= 1 :REN SUGGESTED STEPSIZE FOR THE FIRST STEP.  
240T=0:x（1）=1:x（2）=.1:x（3）=-.1  
250x（4）=-1:x（5）=1:x（6）=.2#  
260 REK INITIAL CONDITIONS.HERE X(1）,X(2) AND X(3)ARE  
270 REN CONPONENTS OF POSITION；X(4）,X(S) AND X(6) ARE  
280 REHCONPONENTS OF VELOCITY  
290TF =1 :REH FINAL TINE FOR THE INTEGRATION.  
300 REN THE PROGRAH IS SET UP SO THAT THE INTEGRATION  
310 REN ENDS PRECISELY AT TINE TF.  
320 REN  
400 REN NOV AN INTEGRATION STEP IS STARTED.  
410TT=T:REM SAVE THE TINE FOR THE START OF THE STEP.  
420GOSUB1000  
430FOR=1TO NQ  
440 F（1,N）=Z(N）  
450 T（N）=x（N）  
460NEXTH  
470REN RETURN HERE WITH A SHALLER STEPSIZE IF NECESSARY.  
480FORK=2T06  
490T=TT+A（K）\*H  
500FOR=1TONQ  
510 X（N）=T（N）:K1=K-1  
520 FORL=1T0K1  
530 x（N）= x（N） + H\*B(K,L）\*F(L,N）  
550 NEXT  
560 GOSUB1000  
570 FOR =1TO NQ、  
580 F（RN）=Z(N）  
590 NEXTN  
600 NEXT K  
880 FOR=1TONQ  
TE(N）=0:X（N）=IT(N）  
630 FORK=1T06  
640 X（N）=X（N）H\*CH（K）\*F（K,N）  
650 TE（N）=TE（N)+H\*CT（K）\*F(K,N）  
660 NEXTK  
670TE（N）=ABS（TE(N)）  
680 NEXTN  
690 TH=0#  
700 FOR N=1 TO NQ  
710 IFTHTENTHEN 730  
720T=TE(N）  
730 NEXTN  
740REN TH IS THE TEMAX OF THE TEXT.  
750HT=H  
760H= .9\*H\*（TL/TH）.2\* :REN NEV STEPSIZE.  
770 IF TH>TL THEN470  
780 REK THE STEP HUST BE REPEATED VITH THE NEV,REDUCED，H.  
790T=TT÷HT  
800 REN A SUCCESSFUL STEP HAS BEEN CONPLETED.  
810 PRINT TIE  
3383  
4O THEN 8OREN THE PIAL STEP HASBEEN TAKEN  
850IFT<TF THE410  
860H=TF-T:GOT0 410  
870 REM READY FOR THE FINAL STEP.H WILL BE NEGATIVE.  
880END  
1000 REN THIS SUBROUTINE CALCULATES THE RIGHT-HAND SIDES  
1010 REH OF THE DIFFERENTIAL EQUATIONS AND PUTS THEH  
100 ）））  
1040=SR（x（x（）+x(）x(2x（）\*x（））:R3=\*\*R  
1050Z（）(:(52(2）/2(6(3）/3 1060RETURN


<!-- chunk 0005: pages 161-200 -->
# 10.7 The Numerical Integration of Differential Equations-A Multistep Method for First-Order Systems

We start once more with the differential equation

$$
\begin{array} { r l } { \frac { d \mathcal { Z } } { d t } = f ( t , x ) ; } & { { } x ( t _ { 0 } ) = x _ { 0 } . } \end{array}
$$

The solution (and we assume, of course, existence and uniquenessin any domain in which we are working) can be formally written as

$$
{ \mathfrak { x } } = { \mathfrak { x } } \{ t \} ,
$$

and for any time $\hat { \bf \ddagger } _ { j }$ ,we have the formal relation

$$
x ( t _ { i } ) - x ( t _ { 0 } ) = \int _ { t _ { 0 } } ^ { t _ { i } } f [ t , x ( t ) ] d t .
$$

This will be applied by replacing the integrand by a polynomial that interpolates a set of values of $f$ In order to do this, we must know some of the past history of $f _ { i }$ so the method cannot start until $\clubsuit$ set of values is available:

$$
t _ { i } = t _ { 0 } + i h , x _ { i } , f _ { i } = f ( t _ { i } , x _ { i } ) , i = 1 , 2 , \ldots , k .
$$

$\hslash$ is the stepsize to be used, and $k$ is related to the order of the method: the more values used, the higher the degree of the interpolating polynomial,and, up to $\ f$ point, the greater the accuracy of the method. In the program that follows, these initial values are found through the use of the Runge-Kutta algorithm (10.6.2): slow, but safe, provided that the stepsize for the Runge-Kutta start is small enough compared with the stepsize for the regular integration. Fehlberg's method could also be used. In any event， care should be taken over these starting values. We mention also that $\pmb { k }$ is an INPUT parameter in the program that follows.

A regular step in the program has two components, prediction and correction. Let us start with a set of values for $f _ { 1 } , f _ { 2 } , \ldots , f _ { k }$ These can be fitted to an interpolating polynomial of degree $( \Bbbk - I )$ Call this $P _ { p } ( \vec { \tau } )$ ,where

$$
P _ { p } ( t ) = p _ { 1 } ( t ) f _ { 1 } + p _ { 2 } ( t ) f _ { 2 } + \cdots + p _ { k } ( t ) f _ { k } .
$$

The value of $\pmb { \mathcal { X } } _ { k }$ at time $\ddagger _ { \bar { \star } }$ is, of course, known: we need to approximate $\boldsymbol { \mathfrak { X } } _ { k + 1 }$ at time $t _ { k + 1 } = t _ { k } + h$ This is done by using (10.7.3) in the form

$$
\begin{array} { l } { { \displaystyle x _ { k + 1 } ^ { a } = x _ { k } + \int _ { t _ { k } } ^ { t _ { k + 1 } } P _ { p } ( t ) d t } } \\ { ~ = x _ { k } + \int _ { t _ { k } } ^ { t _ { k } + h } [ p _ { 1 } ( t ) f _ { 1 } + \dots + p _ { k } ( t ) f _ { k } ] d t } \\ { ~ = x _ { k } + h [ b _ { k } f _ { 1 } + b _ { k - 1 } f _ { 2 } + \dots \pmb { \cdot } b _ { 1 } f _ { k } ] . } \end{array}
$$

This completes the prediction.

After $x _ { k + 1 } ^ { a }$ is found, $\begin{array} { l c l } { { { \hat { f } } _ { k \pm 1 } ^ { \alpha } } } & { { = } } & { { f ( t _ { k \pm 1 } , x _ { k \pm 1 } ^ { \alpha } ) } } \end{array}$ is computed, and the et:f,f，,fk,f+1is the basis for an interpolating polynomial Pe(t).A orrected value,xk+1, is then found from

$$
x _ { k + \frac { 1 } { 4 } } ^ { c } = x _ { k } + \int _ { t _ { k } } ^ { t _ { k + 1 } } \bar { P } _ { c } ( t ) d t .
$$

This leads to a corrected value for fk+1,and a corrected interpolating polynomial,and (10.7.5) can be used again. Thus correction can be viewed as a recursive operation; if all goes well, the recursion will lead to an acceptable value for $\pmb { \mathcal { X } } \pmb { \mathcal { k } } \pm \mathbf { 1 }$ ,and the step is complete.

The preceding paragraph describes the principle of the correction. To deseribe the detail that will be used in the program, the notation will be changed. After prediction,the subscripts are shifted,with the old fi abandoned,and i+1.So

$$
\begin{array} { r l } & { f _ { 1 } \gets f _ { 2 } , \quad f _ { 2 } \gets f _ { 3 } , \quad . . . , f _ { k - \bar { 1 } } \gets f _ { k } , \quad f _ { k } \gets f _ { k + 1 } ^ { a } , } \\ & { \qquad t _ { k - 1 } \gets t _ { k } , \quad t _ { k } \gets t _ { k + 1 } . } \end{array}
$$

nthe program,the final f-switch is delayed.） Then (10.7.5) is modifed to

$$
\begin{array} { l } { { \displaystyle x _ { k } ^ { c } = x _ { k - 1 } + \int _ { t _ { k - 1 } } ^ { t _ { k } } P _ { c } ( t ) d t } } \\ { { \displaystyle \quad = x _ { k - 1 } + h [ [ \bar { b } _ { k } ^ { * } f _ { 1 } + \bar { b } _ { k - 1 } ^ { * } f _ { 2 } + \cdot \cdot \cdot + b _ { 2 } ^ { * } f _ { k - 1 } + b _ { 1 } ^ { * } f _ { k } ] } . } \end{array}
$$

The coefficients bi and b are computed in the program; they depend on k as well asi,but are, of course,independent of h. When (10.7.7) is used recursively, only the final term changes from one iteration to the next, simplifying the programing.

The prediction and correction procedures are respectively known as the Adams-Bashforth and Adams-Moulton methods. Technical details can be found inreferences such as 50. The formulas for the coefficients may be summarized as follows.Introduce $g _ { \dot { \mathfrak { z } } }$ and $g _ { \hat { \pm } } ^ { \ast }$ ， $i = \vec { \bf \tilde { \tau } } _ { 3 } , 2 , \dots , \vec { \kappa }$ ,where $g _ { 1 } = g _ { 1 } ^ { * } = 1$ and

$$
\begin{array} { l l } { { g _ { i } + \displaystyle \frac { 1 } { 2 } g _ { i - 1 } + \displaystyle \frac { 1 } { 3 } g _ { i - 2 } + \cdots + \displaystyle \frac { 1 } { i + 1 } g _ { 1 } = \mathbb { i } , \Bigg ] } } & { { } } \\ { { g _ { i } ^ { * } + \displaystyle \frac { 1 } { 2 } g _ { i - 1 } ^ { * } + \displaystyle \frac { 1 } { 3 } g _ { i - 2 } ^ { * } + \cdots + \displaystyle \frac { 1 } { i + 1 } g _ { \mathbb { i } } ^ { * } = 0 . } } \end{array}  ~ i = 2 , 3 , \ldots , k .
$$

These would be actual coefficients if backward differences were to be used.)

Then

$$
b _ { m } = \sum _ { j = m } ^ { k } p _ { m j } g _ { j } \quad { \mathrm { a n d } } \quad { \bar { b } } _ { m } ^ { * } \sum _ { j = m } ^ { k } { p _ { m j } g _ { j } ^ { * } } , \qquad { \Bigg \} }
$$

where

$$
\left. \begin{array} { l } { { p _ { m j } = ( - 1 ) ^ { \dot { m } - 1 } { \binom { j - 1 } { m - 1 } } } } \\ { { = ( - 1 ) ^ { m - 1 } { \frac { ( j - 1 ) ( j - 2 ) \cdots ( j - m + 1 ) } { 1 \cdot 2 \cdot \cdots \cdot ( m - 1 ) } } . } } \end{array} \right\}
$$

The stepsize in the Runge-Kutta starting procedure should be smaller than the regular stepsize; if this is $\mathbf { \Sigma } _ { H } ^ { \mp }$ ,then a rule of thumb for that of the Runge-Kutta section is

$$
\begin{array} { r } { \bar { z } \bar { z } ^ { \bar { z } } \bar { \kappa } = \frac { \bar { \cal H } ^ { \bar { z } } } { 2 ^ { ( \bar { \kappa } - 4 ) } } . } \end{array}
$$

You should experiment with this. The ratio of the two stepsizes,RK,is an INPUT parameter of the program. In the program the corrector is iterated for up to three times. As it stands, the quantity used in line 2320 to test whether another iteration should be made is too small for the stepsize used. Here again, you should run experiments. When experimenting,be generous with your printout.

The program was tested with the same orbit that was used in the preceding section. Results for time $\hat { \ell } = \vec { \lambda }$ were:

$$
\begin{array} { r l } { x = } & { { } . \frac { 4 6 6 0 8 0 7 8 4 6 3 5 7 9 2 5 } { 6 } , } \\ { y = } & { { } . \frac { 9 0 0 6 1 1 2 4 0 9 0 0 4 8 1 7 } { 6 } , } \\ { z = } & { { } . \frac { 1 1 4 0 4 5 9 8 1 7 9 6 8 2 8 2 } { 6 } , } \\ { x = } & { { } . 8 7 6 5 9 4 4 8 2 2 9 2 0 0 6 , } \\ { y = } & { { } . \frac { 4 7 3 1 5 6 6 1 0 9 8 1 8 8 7 4 } { 6 } , } \\ { z = } & { { } . \frac { 1 9 3 1 5 9 4 9 4 9 2 4 8 1 4 5 } { 6 } . } \end{array}
$$

The good figures are underlined. The accuracy is not spectacular; you may find it worth the programing effort to rewrite the method using backward diferences. Here is the program that generated these figures:

REM PREDICTOR-CORRECTOR HETHOD WITH RUNGE-KUTTA START. DEFDBL A-H,O-Z :DEFINT I-N   
DIM X(6),2(6）,F(6,10）,xT(6),R1(6),R2(6),3(6),SUH(6) $\chi \ : = \ : \ : \forall$   
REN K IS THE PARANETER FOR THE ORDER OF THE HETHOD. $7 7 = 8$   
REM RK IS THE NUNBER OF RUNGE-KUTTA STEPS PER REGULAR REM STEPSIZE TO BE USED IN THE STARTING PROCEDURE. 90 H=..1\*:REM STEPSIZE.   
100 TMAX = 1\* : REH FINAL TIME FOR THE INTEGRATION.   
110 NQ=6 :REM NUMBER OF EQUATIONS IN THE SYSTEN.   
120T=0:x（1）=1:x（2)=1:x（3）=-.1   
130 X（4）=-1:x（5）=1:x（6）=.2   
140 REM_INITIAL CONDITIONS.   
150 PRINT TIET   
160FORN=1TO NQ   
170 PRINTX（"；N；"）="；X(N）   
180 NEXT N:PRINT   
190 GOSUB 5OO :REH FIND COEFFICIENTS.   
200 GOSUB 15OO :REH RUNGE-KUTTA START.

220 PRINTPRINT TIHE；T  
230FORN=1TO NQ  
240 PRINT²X（；N;）="；X(N）  
250NEXTN  
260IF T >= THAX THEN 280  
270GOTO210  
280END  
500 REN CALCULATE COEFFICIENTS FOR THE INTEGRATION.  
510FORJ=1TOK  
520 B（J）=0  
530 BS（J）=0  
540 P(i,J）=1#  
550 NEXTJ  
560FORI=2TOK  
570 PORT0 K  
590   
600 P(I,J）=- P(I - 1,J)\*（FJ-FI ÷1#)/(FI - 1#)  
610 NEXT  
620 NEXTI  
630G（i）=1#:GG（1）=1#  
640FORI=2TOK  
650 G（I）=1GG（I）=0#  
660 FORJ=2T0I  
670 FJ=J  
680 （）=G（I）-G(I-J+1）/FJ  
690 GG（I）=GG（I）-GG(I-J+1）/FJ  
700 NEXTJ  
710 NEXTI  
720 FOR=1 TO K  
730 FORJ=HTOK  
740 B（N）=B（H）+P(H,J）\*G（J）  
750 BS（H）=BS（H）+P（H,J）\*GG（J）  
760 NEXT J  
770NEXTH  
780RETURN  
1000 REH RIGHT-HAND SIDES OF THE EQUATIONS  
10102（1）=x（4）:z（2）=x（5）:z（3）=x（6）  
1020R=SqR（x（1）\*X（1）+X(2）\*X（2）+X(3）\*X(3））:R3=R\*R\*R  
1030z（4）=-x（1）/R3:z（5）=-x(2）/R3:2（6）=-X（3）/R3  
1040RETURN  
1500 REH RUNGE-KUTTA START  
1510HRK $=$ H/RK:REN REDUCED STEPSIZE FOR THIS SUBROUTINE.  
1520GOSUB1000  
1530FOR=1TO NQ  
1540 F(N,1）=z(N）  
1550NEXT  
1560FORL=2 TO K  
1570 FORH=1TORK  
1580 FORN=1TONQ  
1590 XT（N）=X（N）  
1600 R1（N)=HRK\*Z（N）  
1610 X（N）=XT（N）R1（N）/2  
1620 NEXT_N  
1630 T=T+HRK/2#:GOSUB1000  
1640 FORN=1T0NQ  
1650 R2（N）=HHKZ（N）  
1660 X（N）=XT（N）+R2（N）/2#  
1670 NEXTN  
1680 GOSUB 1000  
1690 FORN=1TONQ  
1700 R3（N）=HRK\*Z（N）  
1710 X（N）=XT（N）R3（N）  
1720 NEXTN  
17 1730 22）0）  
HRK\*Z（N））/6  
1760 NEXTN  
1770 GOSUB1000  
1780 NEXTH  
1790 FORN=1TO_NQ  
1800 F(N,L)=Z(N）  
1810 NEXTN  
1820 PRINT :PRINT "TIHE  ；T  
1830 FORN=1 TO NQ  
1840 PRINTX（"；N；"）="；X（N）  
1850 NEXT N  
1860 NEXTL  
1870 RETURN  
2000 REN PREDICTOR-CORRECTOR.  
2010 REN PREDICTION.  
2020FOR $\begin{array} { l } { \displaystyle \overrightarrow { \lambda } ~ \equiv ~ \frac { \ell } { \lambda } } \end{array}$ TO NQ  
2030 $z = 0$   
2040 FORJ=1TO K.  
2050 Z=Z+B（J）\*F（N,K-J÷1）  
2060 NEXT J  
2070 XT（N）=X（N）  
2080 X（N）=XT（N）+H\*Z  
2090NEXTN  
2100 REH SHIFT.  
2110FORN=1TO NQ  
2120 FORJ=1T0K-1  
2130 F（N,J）=F（N,J+1）  
2140 NEXT  
2150 NEXT N  
2160 REN CORRECTION.  
2170T=T+H  
2180FORN=1TO NQ  
2190 SUH（N）=O#  
2200 FORJ=2TOK  
2210 SUH(N）=SUH（N)+BS（J）\*F(N,K-J÷1)  
2220 NEXT  
2230 SUN(N)=XT(N）+H\*SUN（N）  
2240 NEXTH  
2250FORNC=1TO3  
2260 P=O#:GOSUB 1000  
2270 FORN=1TONQ  
2280 CORR=SUH（N）+H\*BS（1）\*Z（N）  
2290 P=P÷ABS（X(N）-CORR）  
2300 X（N）=CORR  
2310 NEXT  
2320 IFP< 1E-11 THEN2350  
2330 NEXT NC  
2340 PRINT CONVERGENCE PROBLEN. $\oint \mathbf { \Sigma } = \mathbf { \Sigma } ^ { 1 1 }$ ；P  
2350 FOR $\tilde { \lambda } ~ \equiv ~ \mathfrak { f }$ TONQ  
2360 $\mathtt { F } ( \mathbb { F } , \mathbb { X } ) \ = \ \mathtt { Z } \{ \hat { \mathtt { M } } \}$   
2370 NEXT  
2380 RETURN

# 10.8 The Numerical Integration of Differential Equations-Systems of Second-Order Equations

This section is based on the method traditionally used in celestial mechanics. It is credited to Gauss,although often referred to as the “Gauss-Jackson" method. For much orbital work it is arguably without rival. As an introduction, consider the single equation

$$
\frac { \vec { a } ^ { 2 } \boldsymbol { x } } { \vec { d t } ^ { 2 } } = F ( \boldsymbol { x } , \frac { \vec { a } \boldsymbol { x } } { \vec { d t } } , \frac { \boldsymbol { t } } { \boldsymbol { \tau } } ) ,
$$

or $\ddot { \boldsymbol { x } } = \boldsymbol { \Xi } ^ { \prime } \{ \boldsymbol { x } , \dot { \boldsymbol { x } } , \dot { \boldsymbol { t } } \}$ At some time, $\ddagger _ { i }$ ,there will be values $\boldsymbol { \mathfrak { Z } } _ { \widehat { \mathfrak { t } } } , \boldsymbol { \dot { \mathfrak { L } } } _ { \widehat { \mathfrak { t } } }$ ,and

$$
\vec { \varepsilon } _ { i } = \hbar ^ { 2 } \vec { \varepsilon } ^ { \prime } ( x _ { i } , \dot { x } _ { i } , \dot { \varepsilon } _ { i } ) ,
$$

here $\gamma$ is the stepsize. So $\dot { \varepsilon } _ { i } = \dot { \varepsilon } _ { 0 } + \dot { \varepsilon } \dot { \mu }$ $\ddagger _ { 0 }$ being the starting time.

In terms of central differences, the basic formulas are

$$
\begin{array} { r } { x _ { i } = \delta ^ { - 2 } F _ { i } + \frac { 1 } { 1 2 } F _ { i } - \frac { 1 } { 2 4 0 } \delta ^ { 2 } F _ { i } + \frac { 3 1 } { 6 0 4 8 0 } \delta ^ { 4 } F _ { i } - \frac { 2 8 9 } { 3 6 2 8 8 0 0 } \delta ^ { 6 } F _ { i } + \cdot \cdot \cdot } \end{array}
$$

$$
\begin{array} { r } { h \dot { x } _ { i } = \delta ^ { - 1 } F _ { i + \frac { 1 } { 2 } } - \frac { 1 } { 2 } F _ { i } - \frac { 1 } { 1 2 } \mu \delta F _ { i } + \frac { 1 1 } { 7 2 0 } \mu \delta ^ { 3 } F _ { i } - \frac { 1 9 1 } { 6 0 4 8 0 } \mu \delta ^ { 5 } F _ { i } + \cdot \cdot \cdot } \end{array}
$$

For the sake of the program, these formulas will be rewritten to use backward differences.We start by considering a typical “step” once the method is established. As usual, we have prediction followed by correction. Assume that astep has just been satisfactorily completed, giving “good” values for the time The most up-to-date information will be stored in the differences and sums:

# Table 10.9

This could be taken further (and the program will be capable of using more terms) but this table will be good enough for discussion.x；and x；are known for time $\dot { \pmb { \tau } } _ { i }$ We predict

$$
\begin{array} { r } { x _ { i + 1 } ^ { a } = \nabla ^ { - 2 } \mathcal { F } _ { i } + \frac { 1 } { 1 2 } \mathcal { F } _ { i } + \frac { 1 } { 1 2 } \nabla \mathcal { F } _ { i } + \frac { 1 9 } { 2 4 0 } \nabla ^ { 2 } \mathcal { F } _ { i } + \frac { 1 8 } { 2 4 0 } \nabla ^ { 3 } \mathcal { F } _ { i } } \\ { + \frac { 8 6 3 } { 1 2 0 9 6 } \nabla ^ { 4 } \mathcal { F } _ { i } + \frac { 8 2 5 } { 1 2 0 9 6 } \nabla ^ { 5 } \mathcal { F } _ { i } + \frac { 2 3 7 6 7 1 } { 3 6 2 8 8 0 0 } \nabla ^ { 6 } \mathcal { F } _ { i } , \quad } \end{array}
$$

$$
\begin{array} { r l } & { \hbar \dot { x } _ { i + 1 } ^ { a } = \nabla ^ { - 1 } F _ { i } + \frac { 1 } { 2 } F _ { i } + \frac { 5 } { 1 2 } \nabla F _ { i } + \frac { 3 } { 8 } \nabla ^ { 2 } F _ { i } + \frac { 2 5 1 } { 7 2 0 } \nabla ^ { 3 } \vec { F } _ { i } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \dot { \tau } + \frac { 9 5 } { 2 8 8 } \nabla ^ { 4 } F _ { i } + \frac { 1 9 0 8 7 } { 6 0 4 8 0 } \nabla ^ { 5 } + \frac { 3 6 7 9 9 } { 1 2 0 9 6 0 } \nabla ^ { 6 } \vec { F } _ { i } . } \end{array}
$$

1these,we can calculate

$$
F _ { i + 1 } ^ { a } = h ^ { 2 } F ( x _ { i + 1 } ^ { a } , \dot { x } _ { i + 1 } ^ { a } , \dot { t } _ { i + 1 } \}
$$

move down the table, finding the next diagonal of differences and sums:

# Table 10.10

Next we find corrected values, $x _ { i + 1 } ^ { \dot { \mathfrak { b } } }$ and $\dot { \bar { x } } _ { i + \bar { 1 } } ^ { \bar { 3 } }$ ,from

$$
\begin{array} { r l } & { x _ { i + 1 } ^ { \flat } = \nabla ^ { - 2 } \overline { { F } } _ { i } + \frac { 1 } { 1 2 } F _ { i + 1 } ^ { a } - \frac { 1 } { 2 4 \bar { 0 } } \nabla ^ { 2 } \overline { { F } } _ { i + 1 } ^ { a } - \frac { 1 } { 2 4 0 } \nabla ^ { 3 } \overline { { F } } _ { i + 1 } ^ { a } } \\ & { \qquad - \frac { 2 2 1 } { 6 0 4 8 0 } \nabla ^ { 4 } \overline { { F } } _ { i + 1 } ^ { a } - \frac { 1 9 0 } { 6 0 4 8 0 } \nabla ^ { 5 } \check { F } _ { i + \bar { 1 } } ^ { a } - \frac { 9 8 2 9 } { 3 6 2 8 8 0 0 } \nabla ^ { 6 } \bar { F } _ { i + \bar { 1 } } ^ { a } , } \end{array}
$$

and

$$
\begin{array} { r l } & { { \hslash } \dot { x } _ { i + 1 } ^ { \flat } = \nabla ^ { - 1 } \mathcal { F } _ { i + 1 } ^ { \alpha } - \frac { 1 } { 2 } \mathcal { F } _ { i + 1 } ^ { \alpha } - \frac { 1 } { 1 2 } \nabla F _ { i + 1 } ^ { \alpha } - \frac { 1 } { 2 4 } \nabla ^ { 2 } F _ { i + 1 } ^ { \alpha } - \frac { 1 9 } { 7 2 0 } \nabla ^ { 3 } \mathcal { F } _ { i + 1 } ^ { \alpha } } \\ & { \qquad - \frac { 3 } { 1 6 0 } \nabla ^ { 4 } \mathcal { F } _ { i + 1 } ^ { \alpha } - \frac { 8 6 3 } { 6 9 4 8 0 } \nabla ^ { 5 } \mathcal { F } _ { i + 1 } ^ { \alpha } - \frac { 1 3 7 5 } { 1 2 0 9 6 0 } \nabla ^ { 6 } \mathcal { F } _ { i + 1 } ^ { \alpha } . } \end{array}
$$

A new $\pmb { \xi }$ can now be computed, using an obvious modification of (10.8.7), and the differences adjusted. Traditionally, the stepsize has been chosen so that correction was not needed; but provided that more decimal places are carried in the computation than are needed in the solution, the difference $\left\{ x ^ { \hat { b } } - x ^ { a } \right\}$ will be informative. For now,provided that the difference is smaller than some preset tolerance,the step will have been completed.

We now change the notation in order to generate a program. Table 10.9 becomes:

Table 10.11

S1

The predicted values for $\pmb { x }$ and $\dot { \mathfrak { x } }$ are found from

$$
\begin{array} { r } { \displaystyle \chi A = S 2 + A ( 0 , 2 ) * F + \sum _ { N = 1 } ^ { M } A ( 0 , N + 2 ) * D ( N ) , \Bigg ] } \\ { \displaystyle H * \bar { X } V A = S 1 + B ( 0 , 1 ) * F + \sum _ { N = 1 } ^ { M } B ( 0 , N + 1 ) * D ( N ) . \Bigg ] } \end{array}
$$

The time is increased, so that

$$
\mathcal { T } = \mathcal { T } + \mathcal { T } ,
$$

and then

$$
\mathcal { F } A = H ^ { 2 } \ast \mathcal { F } ( X A , X V A , \mathcal { T } )
$$

and the new differences, and a new first sum are found. We then have the situation of Table 10.9,which,in the new notation,is

# Table 10.12

The corrections follow:

$$
\begin{array} { r l r } & { } & { X B = S 2 + A ( 1 , 2 ) * F A + \displaystyle \sum _ { N = 1 } ^ { M } A ( 1 , N + 2 ) * D ( N ) , } \\ & { } & { \displaystyle H * X V B = S 1 + B ( 1 , 1 ) * F A + \displaystyle \sum _ { N = 1 } ^ { M } B ( 1 , N + 1 ) * D ( N ) . } \end{array}
$$

Ifthe difference $\{ \pmb { X } \pmb { B } - \pmb { X } \pmb { A } \}$ is small enough, then we find

$$
\begin{array} { r } { \mathcal { F B } = H ^ { 2 } * \mathcal { F } ( X \mathcal { B } , X Y B , T ) . } \end{array}
$$

Increase each of S1,D(1),...,D(M) by the amount (FB-FA),and find the new. second sum from $S 2 = S 2 \pm S 1$ Set $\Sigma = \Sigma \mathcal { B }$ and the step is complete.

if $X B$ is not satisfactory, further adjustments, $\Im X$ and $D X Y$ can be made, here

$$
\begin{array}{c} \begin{array} { r l } & { \frac { 3 2 \pi } { 2 } , } \\ & { \frac { 3 2 \pi } { 2 } , } \\ & { \frac { 3 2 \pi } { 2 } , } \\ & { \frac { 3 2 \pi } { 2 } , } \end{array} \quad D X = ( F B - F A ) * [ A ( 1 , 2 ) + A ( 1 , 3 ) + \cdots + A ( 1 , M + 2 ) ] , \ : \ : ]  \\ & { \frac { 3 2 \pi } { 2 } , } \\ & { \frac { 3 2 \pi } { 2 }  \qquad H * D X V = ( F B - F A ) * [ B ( 1 , 0 ) + B ( 1 , 1 ) + \cdots + B ( 1 , M + 1 ) ] . \ : ] } \end{array}
$$

Socontinued correction is no great burden.

There are several schools of thought about the best way to set up the initial table,before the first prediction can be made. The most obvious way is to use asingle-step method,as in the preceding section. Alternatives involve iteration procedures. We shall look at just one. We assume that the equations to be solved can bewritten as

$$
\ddot { \bar { \mathbf { r } } } = \overline { { \mathbf { g } } } _ { \mathbb { Q } } + \overline { { \mathbf { g } } } _ { \mathbb { 1 } } ,
$$

where $\overrightarrow { \mathbf { r } } = \overrightarrow { \mathbf { g } } _ { 0 } = - \mathbf { \nabla } \mu \mathbf { r } / r ^ { 3 }$ would yield $\hat { \pmb { \alpha } }$ Keplerian orbit and $| \overline { { \mathbf { x } } } _ { 1 } | \ll | \overline { { \mathbf { x } } } _ { 0 } |$ In orbital work thisis, of course,usually the case. In setting out the formulas,Ishall continue to use the notation for just one equation, (10.8.1)； the generalization to three should be obvious.

The initial table is set out using the approximate known solution, correponding to the given initial conditions, $X \mathbb { 0 }$ and $\pmb { \chi } _ { \pmb { \jmath } }$ at time $\mathfrak { Z 0 }$ Let

$$
\left. \begin{array} { l } { { F ( 0 ) = H ^ { 2 } * F ( X 0 , X V 0 , T 0 ) . } } \\ { { \mathrm { ~ F o r ~ e a c h ~ t i m e ~ } T N = T 0 - N * H , \mathrm { ~ c a l - } } } \\ { { \mathrm { ~ c a l a t e ~ } X N , X V N \pounds \mathrm { m ~ t h e ~ a p p r o x i m a t e ~ } } } \\ { { \mathrm { ~ s o l u t i o n ~ a n d ~ i e t ~ } } } \\ { { F ( N ) = H ^ { 2 } * F ( X N , X V N , T N ) , \quad N = 1 , 2 , \ldots , M . } } \end{array} \right]
$$

Next, find the backward differences, $\mathfrak { D } ( 1 ) , \bar { D } ( 2 ) , \dots , \bar { D } ( \tilde { M } )$ and use the formulas(10.8.12） to find the sums:

$$
 \begin{array} { l }   \displaystyle [ \begin{array} { l l l l } { { \displaystyle 0 } } & { { \displaystyle 0 \le N \le 0 \le \frac { \partial \delta ( N ) } { \partial \delta } } } & { { \displaystyle \le \delta ( N - N ) } } & { { \displaystyle \le \delta ( N ) - \frac { M } { \delta } } } \\ { { \displaystyle - \frac { N } { \delta } } } & { { \displaystyle \le \delta ( N - N ) } } & { { \displaystyle \le \delta ( N - N ) } } \end{array} ] \le [ \begin{array} { l } { { \displaystyle M } } \\ { { \displaystyle N } } \end{array} ] \le N \le N \le 1 \le N \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le N \le 1 \le 1 \le N \le 1 \le 1 \le N \le 1 \le 1 \le N \le 1 \le 1 \le 1 \le N \le 1 \le 1 \le 1 \le 1 \le N \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \le 1 \end{array}
$$

This table is now used to calculate new values for X, XV for each time, and these generate corrected values for F(N). Specifically, for N= 1,2,..,M, find $T N = \overline { { { \Omega } } } 0 - N * \bar { M } ,$

$$
\begin{array} { c } { { \displaystyle X N = S 2 + A ( N + 1 , 1 ) * S 1 + A ( N + I , 2 ) * F ( 0 ) } } \\ { { \displaystyle ~ + \sum _ { I = 1 } ^ { M } A ( N + 1 , I + 2 ) * D ( N ) } , } \\ { { \displaystyle H * X V N = S 1 + B ( N + 1 , 1 ) * F ( 0 ) } } \\ { { \displaystyle M * \sum _ { I = 1 } ^ { M } B ( N + 1 , I + 1 ) * D ( N ) , } } \\ { { \displaystyle F ( N ) = H ^ { 2 } * F ( X N , X V N , T N ) . } } \end{array}
$$

As each F(N) is found the difference between it and its predecessor should be calculated, and the sum of the absolute values of all the differences computed. With the completion of a new set of F(N), fresh differences and sums are found,and another iteration can be made. This continues until the changes in the $F ( N )$ become acceptably small.

The coefficients are found from the following formulas:

$$
\begin{array} { r l } & { \begin{array} { r l } & { A ( \mathcal { I } , \mathfrak { G } ) = 1 , } \\ & { A ( \mathcal { I } , N ) = ( - 1 ) ^ { N } \left( \begin{array} { l } { J - 1 } \\ { N } \end{array} \right) - \frac { 2 } { 3 } ( 1 + \frac { 1 } { 2 } ) A ( J , N - 1 ) } \\ & { \qquad - \frac { 2 } { 4 } ( 1 + \frac { 1 } { 2 } + \frac { 1 } { 3 } ) A ( J , N - 2 ) - \cdots } \\ & { \qquad \cdots - \frac { 2 } { N + 2 } ( 1 + \frac { 1 } { 2 } + \cdots + \frac { 1 } { N + 1 } ) A ( J , 0 ) , } \end{array} } \\ & { \begin{array} { r } { B ( J , 0 ) = 1 , } \\ & { B ( J , N ) = \{ - 1 \} ^ { N } \left( \begin{array} { l } { J - 1 } \\ { N } \end{array} \right) - \frac { 1 } { 2 } B ( J , N - 1 ) - \frac { 1 } { 3 } B ( J , N - 2 ) - \cdots } \\ & { \qquad \cdots - \frac { 1 } { N + 1 } B ( J , 0 ) . } \end{array} } \end{array}
$$

Aderivation of these can be found in the NASA Technical Memorandum 33-451, which contains also a wealth of other useful information.

The starting procedure can be improved, with a little more programing effort,if the initial time is in the middle of the starting values. Suppose, for instance, that M = 6； then F(3) would correspond to H² \* F(xo,Xv0,T0), and the initial sums found would be V-1F and V-2F, using implicitly or explicitly the central difference formulas (10.8.3) and (10.8.4).

Another starting procedure begins with F= H² \* F(X0,XVo,TO),and all   
of the differences equal to zero. S1 and S2 are found using the initial conditions,   
and M steps are taken. There will then be a non-zero value for D(M). The   
preceding Mth differences are all put equal to this value, and the differences .

extrapolated back to the initial diagonal. The process starts again with the numbers in this diagonal and F being the starting value as before. S1 and S2 are calculated again, and M steps taken. This continues until the magnitudes ofthe values of X all change by amounts less than some given tolerance between two iterations.

The listing that follows is not general, but was designed to test the basic formulas using the known results for Keplerian motion.The complete program included a subroutine (starting on line 25oo) that solves the initial value problem of Keplerian motion using universal variables;this is similar to programs listed earlier,and is not included here. The starting values were “exact”so no iteration was required. Consequently, A(J,N),B(J,N) are only needed when J=0,1. F(O) corresponds to the starting time, to；as remarked above, the accuracy is increased if the F for the starting time is set in the middle of the table.Velocities are not calculated at each step since the right-hand sides of the equations depend on position only.

Program the method in your own way； but I recommend that you delay experiments with starting procedures until you are sure of the regular steps. Experiment with the order of the method, and the stepsize; also decide whether ornot vou think it is worthwhile to include the correction cycle.

REH PREDICTOR-CORRECTOR METHOD FOR A SYSTEH  
REM OF SECOND-ORDER EQUATIONS.FOR THIS  
REH LISTING THE DIFFERENTIAL EQUATIONS ARE  
REH FOR KEPLERIAN HOTION,AND THE STARTING  
RENVALUES ARE FOUND BY THE FORHULASOF  
REM KEPLERIAN HOTION.THESE ARE NOT LISTED.  
REH  
DEFDBL A-H,O-Z :DEFINT I-N  
DIHA(12,12）,B（12,12）,D（10）,FX（10）,FY（10）  
DIHFZ（i0）,DX(10),DY（1O）,DZ（10）  
GU=1#  
REH HU" FOR THE EQUATIONS OF MOTION.SEE LINE 1510.  
170 REH INITIAL CONDITIONS.  
180 REM INITIALIZE THE INTEGRATION TABLE. SINCE THIS190 REM ISA TEST RUN VITH PURE KEPLERIAN HOTION,THE200 REH INITIAL VALUES ARE FOUND FRON EXACT FORMULAS.210 REN THE FORNULAS ARE CONTAINED IN A SUBROUTINE220 REH STARTING AT LINE 25OO，AND ARE NOT LISTED.230 X=XO :Y=Y0:2=Z0  
XV=XVO :YV=YVO:ZV=ZVO:GOSUB1500  
REMFIND TABULAR VALUES.  
FX(0） $=$ H\*H\*XF  
2 FY（O）=E\*H\*YF FZ（O）=H\*H\*ZF FORI=1TOH:FI=I  
T= TO-FI\*H  
GOSUB 2500 ：G0SUB 1500  
PRINT :PRINT T:PRINT X,Y,Z  
FX（I）=H\*H\*XF  
Y（=H\*Y  
F2（1）=H\*H\*ZF  
NEXTI  
REN FIND DIFFERENCES.  
FORT0-1） = FX（H  
DY（H+   
DZ（H+1- = F2（- -z（ + 1  
NEXTI

440 FOR_IJTOM   
450 DX(x+J-I） = DX(-1÷J-I）-DX(KJ-]   
460   
470   
480 NEXTI   
490NEXTJ   
500 GOSUB 2OOO :REH CALCULATE COEFFICIENTS.   
510 EN FIND SUHS.   
520 Fx =FX(O）:PY=rY(O） :PZ= FZ（0）   
530S1x=H\*XVo-B（1,1）\*FX   
540 S1Y=YV-（i\*Y   
550 s12=H\*Zv0-B（i\*   
560 S2X =0-（12\*x   
570 S2Y=Y0-(1\*   
580 S2z=z0-(\*   
590FORN=1TO   
600 S1x=S1x-B（1,N+1）\*DX(N）   
610 S1Y=SiY-B(i,N+\*DY(N）   
620 SiZ=S12-B(1N+1）\*DZ(N）   
630 S2X=S2X-A（1+2)\*DX(N）   
640 S2Y=S2Y-A(1N2\*DY(N）   
650 S22=S22-（1÷2）\*D2（N）   
660 NEXT   
670 S2x=S1x +S2X   
680 S2Y= S1Y+S2Y   
690 S22= S1z +S2z   
700T=TO   
710 REN PREDICTION.   
720T=T+H   
730 A=S2x+A（0,2）\*FX   
740 YA = S2Y +0\*Y   
750 ZA= S22+（0,2）\*F2   
760FORN=1TO   
770 XA=A+A（O,N+2）\*DX（N）   
780 YA=YA+A（O+2）\*DY(N）   
790 ZA=2A+A（ON+2）\*DZ(N）   
800 NEXTN   
820PRICOORDINATESYAZA 810 PRINT:PRINT PREDICTION.TIHE；T   
830 REH FIND NEV DIFFERENCES   
840 x=XAY=YA $z = z _ { \mathrm { ~ \normalfont ~  ~ } }$ ：GOSUB 1500   
850 FXA $\equiv$ H\*H\*XF   
860 FYA $=$ H\*H\*YF   
870FZA $\lneq$ H\*H\*2F   
880 S = S+PXA   
890S1Y $\simeq$ S1YA   
900 S1z = S12+FZ   
910 D（oA   
920 DY（OA   
930 D(O）=FZA-Pz   
950 ： -DX（）   
960 -DY   
970 -Dz（）   
980 NEXTI   
990F10   
1000 1020 BEB   
1030 NEXTI   
1040 REM CORRECTION.   
1050 XB =S2X+A（1,2\*FXA   
1060 YB = S2Y +A(12\*YA   
1070 ZB= S2Z +2\*F2A   
1080FORN=1T   
1090 XB=XB÷A（1,N+2）\*DX（N）   
1100 YB=YB+A（1+2\*DY(N）   
1110 2B=ZB（1+2）\*D（N）   
1120 NEXTN   
1130 X=XB :Y= YB :Z= ZB :GOSUB 1500   
1140 FX =H\*H\*XF   
1150FY=H\*H\*YF   
1160FZ=H\*H\*ZF   
1170 DFX =X-FXA   
1180 DFY=-A

FZADFXDF2s1xS1YS121 T0+DFXDY（I）=DY）DFYDZ（I）=DZ（I）+DPZ  
NEXTIREN CORRECTION CONPLETED.  
PRINT :PRINT "CORRECTION.TIME " ；T  
PRINT "COORDINATES" ；X,Y,Z  
IFT<1#THEN710  
END  
REH RIGHT-HAND SIDES OF THE EQUATIONS.  
A（J,0）=1:B（J,0）=1:SN=1#FOR=1T0H+2FLN = NSI=1SN = - SN\*(FJ- FLN）/FLNA(J,N）=SNB（J,N）=SNFORK=1TONFK=KZ=1/（FK+1）SI = SI + ZB（J,N）=B（J,N）-Z\*B（JN-K）A（J）=（J,N）-SI\*A（J,N-K）\*2B/（FK÷2）NEXTKNEXT N  
NEXT J  
RETURNE SRIOGOOENS OF POSITION

The coordinates for $\acute { \bf z } = \acute { \bar { \bf z } }$ for this listing were ${ \mathfrak { x } } =$ .4660807848129564, ${ \mathfrak { z } } =$ .900611234846 4384, $z =$ .114045 980636 8995.
