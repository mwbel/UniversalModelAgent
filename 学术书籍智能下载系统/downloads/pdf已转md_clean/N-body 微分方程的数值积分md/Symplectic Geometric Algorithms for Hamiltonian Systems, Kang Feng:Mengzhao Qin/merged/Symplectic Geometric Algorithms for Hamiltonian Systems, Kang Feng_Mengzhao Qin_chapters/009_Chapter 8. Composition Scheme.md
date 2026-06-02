# Chapter 8. Composition Scheme

In this chapter, we consider a class of reversible schemes also called symmetrical schemes. In algebraic language, it is not other, just like self-adjoint schemes . Here, we only deal with one-step reversible schemes. We will introduce the concept of adjoint methods and some of their properties. We will show that there is a self-adjoint scheme of even order in every method. Using the self-adjoint schemes with lower order, we can construct higher order schemes by “composing” a method, and this constructing process can be continued to obtain arbitrary even order schemes. The composing method presented here can be used to in both non-symplectic and symplectic schemes.

$\mathrm { I n } \stackrel { \lbrack \mathrm { Y \bar { o s } 9 0 } \rbrack } { }$ , H.Yoshida proposed a new method to get multistage higher order explicit symplectic schemes for separable Hamiltonian systems by composing lower order ones. However, in $\left[ \mathrm { Q Z 9 2 , W r u \bar { 9 } 6 , S u z 9 2 } \right]$ , we found that this method can also be applied to non-symplectic schemes for both Hamiltonian and non-Hamiltonian systems.

# 8.1 Construction of Fourth Order with 3-Stage Scheme

In this section, we construct a 3-stage difference scheme of fourth order by the method of composing 2nd order schemes symmetrically.

# 8.1.1 For Single Equation

We know that trapezoid scheme

$$
Z _ { k + 1 } = Z _ { k } + { \frac { h } { 2 } } { \big ( } f ( Z _ { k } ) + f ( Z _ { k + 1 } ) { \big ) }
$$

with $h$ the step length, is order 2 for ODEs,

$$
{ \dot { Z } } = f ( Z ) .
$$

We expect that the 3-stage method of the form

$$
\begin{array} { r } { Z _ { 1 } = Z _ { 0 } + c _ { 1 } h \big ( f ( Z _ { 0 } ) + f ( Z _ { 1 } ) \big ) , } \\ { Z _ { 2 } = Z _ { 1 } + c _ { 2 } h \big ( f ( Z _ { 1 } ) + f ( Z _ { 2 } ) \big ) , } \\ { Z _ { 3 } = Z _ { 2 } + c _ { 3 } h \big ( f ( Z _ { 2 } ) + f ( Z _ { 3 } ) \big ) } \end{array}
$$

would be of order 4 (i.e., $Z _ { 3 } - Z ( t + h ) = O ( h ^ { 5 } ) )$ , where $Z _ { 0 } = Z ( t ) . Z ( t + h )$ is the exact solution at $t + h$ and $Z _ { 3 }$ the numerical one when the parameters $c _ { 1 } , c _ { 2 }$ , and $c _ { 3 }$ are chosen properly.

We will use the method of Taylor expansion to deal with the simple case when there is only one ordinary differential equation (ODE). When we deal with the case of systems of ODEs, the Taylor expansions become very complex, although they surely can be applied and the same conclusion as in the former case can be derived. We introduce another method[HNW93] , known as “trees and elementary differentials” to deal with the latter case. In fact, the essence of the two methods is the same; they are just two different ways of expression.

In this section, without specific statements, the values of all functions and their derivatives are calculated at $Z _ { 0 }$ , and we consider only the terms up to $o ( h ^ { 4 } )$ in the following calculations, while the higher order terms of $h$ are omitted,

$$
f = f ( Z _ { 0 } ) , \quad f ^ { \prime } = f ^ { \prime } ( Z _ { 0 } ) , \ldots , { \mathrm { ~ e t c . } }
$$

First, we calculate the Taylor expansion of the exact solution. Since

$$
\left\{ \begin{array} { l l } { \dot { Z } = f , } \\ { \ddot { Z } = f ^ { \prime } \cdot \dot { Z } = f ^ { \prime } f , } \\ { Z ^ { ( 3 ) } = f ^ { \prime \prime } f ^ { 2 } + { f ^ { \prime } } ^ { 2 } f , } \\ { Z ^ { ( 4 ) } = f ^ { \prime \prime \prime } f ^ { 3 } + 4 { f ^ { \prime } } ^ { \prime } f ^ { \prime } f ^ { 2 } + { f ^ { \prime } } ^ { 3 } f , } \end{array} \right.
$$

we have, with $Z _ { 0 } = Z ( t )$ ,

$$
Z ( t + h ) = Z _ { 0 } + h f + { \frac { h ^ { 2 } } { 2 ! } } f ^ { \prime } f + { \frac { h ^ { 3 } } { 3 ! } } ( f ^ { \prime \prime } f ^ { 2 } + f ^ { \prime } { } ^ { 2 } f ) + { \frac { h ^ { 4 } } { 4 ! } } ( f ^ { \prime \prime \prime } f ^ { 3 } + 4 f ^ { \prime \prime } f ^ { \prime } f ^ { 2 } + f ^ { \prime } { } ^ { 3 } f ) + O ( h ^ { 5 } ) + Z _ { 0 } + O ( 1 ) ,
$$

Now, we turn to the Taylor expansion of the numerical solution. We can rewrite (1.3) as

$$
\begin{array} { r c l } { { Z _ { 3 } } } & { { = } } & { { Z _ { 0 } + c _ { 1 } h ( f ( Z _ { 0 } ) + f ( Z _ { 1 } ) ) + c _ { 2 } h ( f ( Z _ { 1 } ) } } \\ { { } } & { { } } & { { + f ( Z _ { 2 } ) ) + c _ { 3 } h ( f ( Z _ { 2 } ) + f ( Z _ { 3 } ) ) } } \\ { { } } & { { = } } & { { Z _ { 0 } + h ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) } } \\ { { } } & { { } } & { { + ( c _ { 2 } + c _ { 3 } ) f ( Z _ { 2 } ) + c _ { 3 } f ( Z _ { 3 } ) ) . } } \end{array}
$$

We use the same technique to expand the Taylor expansions of $f ( Z _ { 2 } ) , f ( Z _ { 3 } )$ . Since

$$
\begin{array} { l } { { Z _ { 2 } - Z _ { 0 } \ = \ c _ { 1 } h ( f ( Z _ { 1 } ) + f ( Z _ { 0 } ) ) + c _ { 2 } h ( f ( Z _ { 2 } ) + f ( Z _ { 1 } ) ) } } \\ { { \ } } \\ { { \ = \ c _ { 1 } h f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) h f ( Z _ { 1 } ) - c _ { 2 } h f ( Z _ { 2 } ) . } } \end{array}
$$

We need to calculate $f ( Z _ { 1 } ) , f ( Z _ { 2 } ) , f ( Z _ { 3 } )$ Taylor expansion up to the terms of order 3 of $h$

$$
f ( Z _ { i } ) = f ( Z _ { 0 } ) + f ^ { \prime } ( Z _ { i } - Z _ { 0 } ) + \frac { f ^ { \prime \prime } } { 2 ! } ( Z _ { i } - Z _ { 0 } ) ^ { 2 } + \frac { f ^ { \prime \prime \prime } } { 3 ! } ( Z _ { i } - Z _ { 0 } ) ^ { 3 } + O ( h ^ { 4 } ) .
$$

Since $Z _ { 1 } = Z _ { 0 } + c _ { 1 } h ( f ( Z _ { 1 } ) + f ( Z _ { 0 } ) )$ by (1.8), we have

$$
\begin{array} { r c l } { { f ( Z _ { 1 } ) } } & { { = } } & { { f ( Z _ { 0 } ) + f ^ { \prime } \Bigl ( c _ { 1 } h f ( Z _ { 0 } ) + c _ { 1 } h f ( Z _ { 1 } ) \Bigr ) } } \\ { { } } & { { } } & { { + \frac { f ^ { \prime \prime } } { 2 ! } \Bigl ( c _ { 1 } h f ( Z _ { 0 } ) + c _ { 1 } h f ( Z _ { 1 } ) \Bigr ) ^ { 2 } } } \\ { { } } & { { } } & { { + \frac { f ^ { \prime \prime \prime } } { 3 ! } \Bigl ( c _ { 1 } h f ( Z _ { 0 } ) + c _ { 1 } h f ( Z _ { 1 } ) \Bigr ) ^ { 3 } + { \cal O } ( h ^ { 4 } ) . } } \end{array}
$$

Inserting the Taylor expansion of $f ( Z _ { 1 } )$ into right side of (1.9), we get

$$
\begin{array} { r l } { f ( Z _ { 1 } ) } & { = \ f ( Z _ { 0 } ) + c \kappa h f ^ { * } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 0 } ) + c h f ^ { * } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 1 } ) \Big ) } \\ & { \quad + \frac { f ^ { * } } { 2 ! } ( c _ { 1 } \Lambda ) ^ { 2 } \Big ( f ( Z _ { 0 } ) + f ( Z ( \tau _ { 1 } ) ) \Big ) ^ { 2 } \Big ) + \frac { f ^ { * } } { 2 ! } ( c _ { 1 } \Lambda ) ^ { 2 } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 0 } ) } \\ & { \quad + c _ { 1 } h f ^ { * } \Big ( f ( Z _ { 0 } ) + f ( Z ( \tau _ { 1 } ) ) \Big ) ^ { 2 } + \frac { f ^ { * } } { 3 ! } ( c _ { 1 } \Lambda ) ^ { 3 } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 0 } ) \Big ) ^ { 3 } + O ( h ^ { 4 } ) } \\ & { = \ f ( Z _ { 0 } ) + c h f ^ { * } \Big ( 2 f ( Z _ { 0 } ) + c h f ^ { * } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 0 } ) + c _ { 1 } 2 h f ^ { * } f ( Z _ { 0 } ) \Big ) } \\ & { \quad + ( c _ { 1 } h ) ^ { 2 } \frac { f ^ { * } } { 2 ! } \Big ( f ( Z _ { 0 } ) + f ( Z _ { 0 } ) \Big ) ^ { 2 } \Big ) + ( c _ { 1 } h ) ^ { 2 } \frac { f ^ { * } } { 2 ! } \Big ( 2 f ( Z _ { 0 } ) + c _ { 1 } h f ^ { * } \Big ( f ( Z _ { 0 } ) \Big ) } \\ & { \quad + f ( Z _ { 0 } ) \Big ) ^ { 2 } + ( c _ { 1 } h ) ^ { 3 } \frac { f ^ { * } } { 3 ! } \Big ( 2 f ( Z _ { 0 } ) \Big ) ^ { 3 } + O ( h ^ { 4 } ) } \\ & { = \ f ( Z _ { 0 } ) + c \kappa h \Big ( 2 f ^ { * } ( Z _ { 0 } ) \Big ) + ( c _ { 1 } h ) ^ { 2 } \Big ( 2 f ^ { * } f ( Z _ { 0 } ) + 2 f ^ { * } f ^ { * } f ^ { 2 } ( Z _ { 0 } ) \Big ) } \\ &  \quad + ( c _ { 1 } h ) ^ { 3 } \Big ( 2 f ^ { * } f ( Z _ { 0 } ) \Big ) + \delta ( f ^ { * } f ^ { * } f  \end{array}
$$

Similarly, developing $f ( Z _ { 2 } )$ and $f ( Z _ { 3 } )$ , since

$$
\begin{array} { r c l } { { Z _ { 2 } - Z _ { 0 } } } & { { = } } & { { c _ { 1 } h \Big ( f ( Z _ { 1 } ) + f ( Z _ { 0 } ) \Big ) + c _ { 2 } h \Big ( f ( Z _ { 2 } ) + f ( Z _ { 1 } ) \Big ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { c _ { 1 } h f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) h f ( Z _ { 1 } ) + c _ { 2 } h f ( Z _ { 2 } ) , } } \end{array}
$$

therefore

$$
\begin{array} { r l } { f ( Z _ { 2 } ) = } & { f ( Z _ { 0 } ) + h f ^ { ' } ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } f ( Z _ { 2 } ) ) + \frac { f ^ { \prime \prime } } { 2 ! } b ^ { 2 } ( c _ { 1 } f ( Z _ { 0 } )  } \\ & {  + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } f ( Z _ { 2 } ) ) ^ { 2 } + \frac { f ^ { \prime \prime } } { 3 ! } b ^ { 3 } ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } )  } \\ & {  + c _ { 2 } f ( Z _ { 2 } ) ) ^ { 3 } + O ( h ^ { 4 } ) } \\ & { = f ( Z _ { 0 } ) + h f ^ { ' } ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + e _ { 2 } ( f ( Z _ { 0 } ) + h f ^ { ' } ( c _ { 1 } f ( Z _ { 0 } )    } \\ & {   + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } \Big ( f ( Z _ { 0 } ) + h f ^ { ' } ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } f ( Z _ { 0 } ) ) )  } \\ & {   + \frac { f ^ { \prime \prime } } { 2 ! } b ^ { 2 } ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } f ( Z _ { 0 } ) ) ) ) \frac { f ^ { \prime \prime } } { 2 ! } b ^ { 2 } ( c _ { 1 } f ( Z _ { 0 } )   } \\ &    + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } ( f ( Z _ { 0 } ) + h f ^  '  \end{array}
$$

Similarly, inserting Taylor expansion of $f ( Z _ { 1 } )$ into (1.11), we get

$$
\begin{array} { r l } { J ( \gamma \otimes 2 ) } & { = \int \langle \nabla \cdot \boldsymbol { u } \rangle - J ( \pi f \otimes 2 ) ( \sin \theta + \cos { 2 \theta } ) ( J ( \mathcal { A } \otimes 2 ) + \cos { 2 \theta } ) \mathcal { L } ( J ( \mathcal { A } \otimes 3 ) + \cos { 2 \theta } ) } \\ & { - \sin { \theta } \gamma ( 2 ^ { 2 } \mathcal { A } ^ { 2 } ( \mathcal { B } 2 ) - 2 \theta ^ { 2 } \mathcal { A } ^ { 2 } ( 2 \otimes 2 ) ) - \cos { 2 \theta } ( J ( 2 \otimes 2 ) ) } \\ & { - \sin { \theta } ( \theta ^ { 2 } ( \Gamma ^ { 2 } \otimes 4 ) + \sin { \theta } ) ( J ( \mathcal { A } \otimes 4 ) + \sin { \theta } ) ( J ( \mathcal { A } \otimes 4 ) + \sin { 2 \theta } ) \mathcal { L } ( J ( \mathcal { A } \otimes 3 ) ) } \\ & { - h ( \theta ( 1 + \omega _ { 2 } ) \hat { J } ^ { 2 } ( \mathcal { A } \otimes 2 ) ) ) \quad , } \\ & { - h ( \theta ( 1 + \omega _ { 2 } ) \hat { J } ^ { 2 } ( \mathcal { A } \otimes 2 ) ) \quad , \quad | \theta \rangle ^ { 2 } h ^ { 2 } ( \mathcal { A } \otimes 1 + \omega _ { 2 } ^ { 2 } \hat { J } ^ { 2 } ( \mathcal { A } \otimes 2 ) ) ) } \\ & { - \frac { 1 } { 2 } h ^ { 2 } ( \alpha h ( 2 h ( \theta ) ) + \sin { 2 \theta } ) ( J ( \mathcal { A } \otimes 4 ) + \cos { \theta } ) \mathcal { L } f ( \mathcal { A } \otimes 3 ) + \cos { 2 \theta } ( J ( \mathcal { A } \otimes 4 )  } \\ & {  - h \hat { J } ^ { 2 } ( \mathcal { A } \otimes 2 ) ( ( J \otimes 4 ) + J ( \mathcal { A } \otimes 2 ) ) ) ^ { 2 } + \frac { 1 } { 2 } h ^ { 2 } h ^ { 2 } ( \mathcal { A } \otimes 1 + \cos { 2 \theta } ) h ^ { 2 } ( \mathcal { A } \otimes 4 ) } \\ & { - J ( \mathcal { A } \otimes 1 ) } \\ & { - \frac { 2 } { 2 } \theta ( \theta ) } \\ &  - \frac { 2 } { 3 } \theta ( 1 + \omega _ { 2 } ) \hat { J } ^ { 2 } ( \mathcal { A } \otimes \hat { J } ^ { 2 } ( \end{array}
$$

Using the above identical method, we have

$$
\begin{array} { r l } { \eta ^ { 2 } ( 2 s ) = } & { \int | U _ { \mu } | ^ { 2 } ( s ) + | U ^ { \prime } | ^ { 2 } ( s ) | ^ { 2 } ( s ) + \langle u + \phi _ { s } ^ { 2 } \rangle | \mathcal { G } ^ { \prime } ( s ) + \langle u + \phi _ { s } ^ { 2 } \rangle | \mathcal { G } ^ { \prime } ( s ) + \langle u + \phi _ { s } ^ { 2 } \rangle | \mathcal { G } ^ { \prime } ( s ) + \langle u ^ { 2 } \rangle | \mathcal { G } ^ { \prime } ( s ) \rangle } \\ & { \quad + \frac { 2 } { 3 } \int _ { 0 } ^ { \infty } \left( \mathcal { G } ^ { 2 } ( 2 s ) \right) \big ( \sin \big ( | \Omega | \phi | ^ { 2 } \rangle \big ) \big ( \sin | \Omega | \phi | ^ { 2 } \big ) + \big | \cos | \Omega | \mathcal { G } ^ { \prime } ( 2 s ) \big | \right) \left( \sin | \Omega | \phi ^ { 2 } \big ) } \\ & { \quad + \frac { 2 } { 3 } \int _ { 0 } ^ { \infty } \Big ( \mathcal { G } ^ { 2 } ( 2 s ) \big ) \big ( \sin | \phi | ^ { 2 } \big ) \big ( \sin | \phi | ^ { 2 } \big ) \big ( 2 s ) + \langle u + \phi _ { s } ^ { 2 } \rangle \big ) \big ( 2 \sin | \phi ^ { 2 } \big ) \left( \sin | \phi | ^ { 2 } \right) } \\ & { \quad + \mathcal { O } \big ( \sin ^ { 3 } \phi \big ) } \\ & { = } & { \int | U _ { \mu } | ^ { 2 } \Big ( s \big ) d s \int _ { 0 } ^ { \infty } \mathcal { G } ^ { \prime } ( 2 s ) + \big ( u + \phi _ { s } ^ { 2 } \big ) \big ( \sqrt { 2 } \big ) \big ( \sin | \phi | ^ { 2 } \big ) + \big ( u ^ { 2 } + \phi _ { s } ^ { 2 } \big ) \big ) \big ( \sin | \phi ^ { 2 } \big ) + \sin \big ( \phi ^ { 2 } \big ) } \\ & { \quad + \frac { 2 } { 3 } \int _ { 0 } ^ { \infty } \int | \mathrm { d } s \int ( 2 \sin | \phi ^ { 2 } \big ) + \big ( u ^ { 2 } \ ) \big ( \sin | \phi ^ { 2 } \big ) + \sin | \phi ^ { 2 } \big ) \Big ( \sin | \phi ^ { 2 } \big ) - \sin | \phi ^ { 2 } \big ) } \\ &  \quad + d s \int _ { 0 } ^   \end{array}
$$

Inserting the Taylor expansion of $f ( Z _ { 1 } )$ and $f ( Z _ { 2 } )$ into (1.13)

$$
\begin{array} { r c l } { f ( Z _ { 3 } ) } & { = } & { f ( Z _ { 0 } ) + h \big ( 2 ( c _ { 1 } + c _ { 2 } + c _ { 3 } ) f ^ { \prime } f ( Z _ { 0 } ) \big ) + h ^ { 2 } \big ( ( c _ { 1 } + c _ { 2 } + c _ { 3 } ) ^ { 2 } 2 f ^ { \prime } { } ^ { 2 } f ( Z _ { 0 } ) } \end{array}
$$

$$
\begin{array} { l } { { + ( c _ { 1 } + c _ { 2 } + c _ { 3 } ) ^ { 2 } 2 f ^ { \prime \prime } f ^ { 2 } ( Z _ { 0 } ) ) + h ^ { 3 } \bigl ( \bigl ( \bigl ( c _ { 1 } + c _ { 2 } \bigr ) c _ { 1 } ^ { 2 } + \bigl ( c _ { 2 } + c _ { 3 } \bigr ) ( c _ { 1 } + c _ { 2 } ) ^ { 2 } } } \\ { { + c _ { 3 } \bigl ( c _ { 1 } + c _ { 2 } + c _ { 3 } \bigr ) ^ { 2 } \bigr ) 2 f ^ { \prime 3 } f ( Z _ { 0 } ) + \bigl ( \bigl ( c _ { 1 } + c _ { 2 } \bigr ) c _ { 1 } ^ { 2 } + \bigl ( c _ { 2 } + c _ { 3 } \bigr ) ( c _ { 1 } + c _ { 2 } ) ^ { 2 } } } \\ { { + c _ { 3 } \bigl ( c _ { 1 } + c _ { 2 } + c _ { 3 } \bigr ) ^ { 2 } + 2 \bigl ( c _ { 1 } + c _ { 2 } + c _ { 3 } \bigr ) ^ { 3 } \bigr ) 2 f ^ { \prime \prime } f ^ { \prime } f ^ { 2 } f ( Z _ { 0 } ) } } \\ { { + \displaystyle \frac { 4 } { 3 } \bigl ( c _ { 2 } + c _ { 2 } + c _ { 3 } \bigr ) ^ { 3 } \bigr ) f ^ { \prime \prime \prime } f ^ { 3 } ( Z _ { 0 } ) + O ( h ^ { 4 } ) . \qquad ( 1 . 1 4 ) } } \end{array}
$$

Let $c _ { 1 } = c _ { 3 } = \frac { w _ { 1 } } { 2 }$ , $c _ { 2 } = \frac { w _ { 0 } } { 2 }$ , take into account (1.5) and (1.6), and compare the Taylor expansion of the exact solution (1.5) with the above one. In order to get fourth order accuracy schemes (1.3), we need to solve the following equations for coefficients $c _ { 1 } , c _ { 2 } , c _ { 3 }$ :

$$
\begin{array} { r l r } & { } & { \mu _ { 2 } ^ { \mathrm { { g r } } } : \ ( \varepsilon _ { 2 } - \varepsilon _ { 3 } + \varepsilon _ { 2 } ) ^ { 2 } \gamma + \varepsilon _ { 3 } + \varepsilon _ { 4 } + \varepsilon _ { 3 } ) + \varepsilon _ { 3 } = 2 \mu _ { 1 } + \sigma _ { 2 } - 1 . 0 1 , } \\ & { } & { \mu _ { 2 } ^ { \mathrm { { g r } } } \mathcal { F } : \ ( \varepsilon _ { 3 } - 2 \varepsilon _ { 3 } ) ^ { 2 } \gamma + \ ( \varepsilon _ { 2 } + \varepsilon _ { 1 } ) ^ { 2 } \gamma - \varepsilon _ { 2 } ^ { 2 } + \gamma \varepsilon _ { 3 } + 2 \varepsilon _ { 4 } + \varepsilon _ { 2 } + \varepsilon _ { 3 } ; } \\ & { } & { = \frac { 1 } { 2 } , } \\ & { } & { = \frac { 1 } { 2 } , } \\ & { \varepsilon _ { 2 } ^ { \mathrm { p } } \sigma _ { f } ^ { \mathrm { { g r } } } \beta _ { f } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 3 } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 3 } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 4 } + \varepsilon _ { 2 } ) \big ) ^ { 2 } \big ) \cdot \ ( \varepsilon _ { 2 } + \varepsilon _ { 1 } ) ^ { 2 } \big ( \varepsilon _ { 3 } + \varepsilon _ { 2 } ) ^ { 2 } - \varepsilon _ { 2 } ^ { 2 } / ( \varepsilon _ { 3 } + \varepsilon _ { 2 } + \varepsilon _ { 3 } ) ^ { 2 } } \\ & { } & { - \frac { 1 } { 8 } , } \\ & { \varepsilon _ { 3 } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 3 } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 3 } ^ { \mathrm { { g r } } } \big ( \varepsilon _ { 3 } ^ { \mathrm { { g r } } } + \varepsilon _ { 3 } \big ) ^ { 2 } \big ) \big ) \cdot \ ( \varepsilon _ { 2 } + \varepsilon _ { 3 } ) ^ { 4 } \big ( \varepsilon _ { 3 } + \varepsilon _ { 3 } ) ^ { 3 } + \varepsilon _ { 3 } ^ { 4 } / ( \varepsilon _ { 3 } + \varepsilon _ { 3 } ) ^ { 2 } } \\ & { } & { ( 1 ) ^ { 2 } } \\ & { } & { = \frac { 1 } { 2 } , } \\ & { } &  \beta _ { 2 } ^ { \mathrm { { g r } } } \beta _ { 1 } ^ { \mathrm { { g r } } } \big ( \ \end{array}
$$

When $2 w _ { 1 } + w _ { 0 } = 1$ holds, the Equation (1.16) becomes ${ \frac { 1 } { 2 } } = { \frac { 1 } { 2 } }$ , i.e., identity, and the Equations (1.17) – (1.20) become the same, i.e.,

$$
6 w _ { 1 } ^ { 3 } - 1 2 w _ { 1 } ^ { 2 } + 6 w _ { 1 } - 1 = 0 .
$$

Thus, we get the conditions for the difference scheme (1.3) to be of order 4:

$$
\left\{ \begin{array} { l l } { 2 w _ { 1 } + w _ { 0 } = 1 , } \\ { 6 w _ { 1 } ^ { 3 } - 1 2 w _ { 1 } ^ { 2 } + 6 w _ { 1 } - 1 = 0 . } \end{array} \right.
$$

Thus we get,

$$
w _ { 0 } = \frac { - 2 ^ { \frac { 1 } { 3 } } } { 2 - 2 ^ { \frac { 1 } { 3 } } } , \quad w _ { 1 } = \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } .
$$

Now, scheme (1.3) becomes

$$
\left\{ \begin{array} { l l } { Z _ { 1 } = Z _ { 0 } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { \frac 1 3 } ) } h \big ( f ( Z _ { 0 } ) + f ( Z _ { 1 } ) \big ) , } \\ { Z _ { 2 } = Z _ { 1 } + \displaystyle \frac { - 2 ^ { \frac 1 3 } } { 2 ( 2 - 2 ^ { \frac 1 3 } ) } h \big ( f ( Z _ { 1 } ) + f ( Z _ { 2 } ) \big ) , } \\ { Z _ { 3 } = Z _ { 2 } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { \frac 1 3 } ) } h \big ( f ( Z _ { 2 } ) + f ( Z _ { 3 } ) \big ) . } \end{array} \right.
$$

# 8.1.2 For System of Equations

We use the “method of tree and elementary differentials” [HNW93] given in Chapter 7. We first rewrite the scheme (1.3) in the $\mathbf { R - K }$ methods:

$$
\left\{ \begin{array} { l l } { Z _ { 1 } = Z _ { 0 } + h \big ( c _ { 1 } f ( Z _ { 0 } ) + c _ { 1 } f ( Z _ { 1 } ) \big ) , } \\ { Z _ { 2 } = Z _ { 0 } + h \big ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + c _ { 2 } f ( Z _ { 2 } ) \big ) , } \\ { Z _ { 3 } = Z _ { 0 } + h \big ( c _ { 1 } f ( Z _ { 0 } ) + ( c _ { 1 } + c _ { 2 } ) f ( Z _ { 1 } ) + ( c _ { 2 } + c _ { 3 } ) f ( Z _ { 2 } ) + c _ { 3 } f ( Z _ { 3 } ) \big ) . } \end{array} \right.
$$

Obviously, the above equation is equivalent to following

$$
\left\{ \begin{array} { l l } { g _ { 1 } = Z _ { 0 } , } \\ { g _ { 2 } = Z _ { 0 } + c _ { 1 } h f ( g _ { 1 } ) + c _ { 1 } h f ( g _ { 2 } ) , } \\ { g _ { 3 } = Z _ { 0 } + c _ { 1 } h f ( g _ { 1 } ) + ( c _ { 1 } + c _ { 2 } ) h f ( g _ { 2 } ) + c _ { 2 } h f ( g _ { 3 } ) , } \\ { g _ { 4 } = Z _ { 0 } + c _ { 1 } h f ( g _ { 1 } ) + ( c _ { 1 } + c _ { 2 } ) h f ( g _ { 2 } ) + ( c _ { 2 } + c _ { 3 } ) h f ( g _ { 3 } ) + c _ { 3 } h f ( g _ { 4 } ) , } \\ { Z = Z _ { 0 } + h \big ( c _ { 1 } f ( g _ { 1 } ) + ( c _ { 1 } + c _ { 2 } ) f ( g _ { 2 } ) + ( c _ { 2 } + c _ { 3 } ) f ( g _ { 3 } ) + c _ { 3 } f ( g _ { 4 } ) \big ) , } \end{array} \right.
$$

where $g _ { 2 } = Z _ { 1 } , g _ { 3 } = Z _ { 2 } , g _ { 4 } = Z _ { 3 }$ , and $Z = Z _ { 3 }$ . Thus, the Butcher tableau

$$
\frac { \mathbf { \phi } _ { C } } { \mathbf { \phi } _ { b ^ { \mathrm { { T } } } } } \_ \frac { \mathbf { \phi } _ { A } } { \mathbf { \phi } _ { b ^ { \mathrm { { T } } } } }
$$

takes the following form:

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2c1</td><td>C1</td><td>C1</td><td>0</td><td>0</td></tr><tr><td>2(c1+c2)</td><td>C1</td><td>C1+C2</td><td>C2</td><td>0</td></tr><tr><td>2(c1 + C2 + C3)</td><td>C1</td><td>C1+C2</td><td>C2+C3</td><td>C3</td></tr><tr><td></td><td>C1</td><td>C1+C2</td><td>C2+C3</td><td>C3</td></tr></table>

From the previous chapter, we have the order condition for $\mathbf { R - K }$ method as follows:

# Theorem 1.1. R–K method

$$
\begin{array} { l } { { g _ { i } ^ { J } = Z _ { 0 } ^ { J } + \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } f ^ { J } ( g _ { j } ^ { 1 } , \cdot \cdot \cdot , g _ { j } ^ { h } ) , } } \\ { { { } } } \\ { { Z _ { 1 } ^ { J } = Z _ { 0 } ^ { J } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } h f ^ { J } ( g _ { j } ^ { 1 } , \cdot \cdot \cdot , g _ { j } ^ { h } ) } } \end{array}
$$

is order of $p$ , iff

$$
\sum _ { j = 1 } ^ { s } b _ { j } \phi _ { j } ( \rho t ) = \frac { 1 } { \gamma ( \rho t ) }
$$

for all rooted tree ρt, have $r ( \rho t ) \leq p _ { \mathrm { : } }$ , where $Z _ { 0 } = ( Z _ { 0 } ^ { 1 } , \cdot \cdot \cdot , Z _ { 0 } ^ { n } ) ^ { \mathrm { T } } , f ^ { J } = ( f ^ { 1 } , f ^ { 2 } , \cdot \cdot \cdot , f ^ { n } ) ^ { \mathrm { T } } .$

Since rooted tree $\rho t$ of Theorem 1.1 is defined in Chapter 7, definitions of $\phi _ { j } ( \rho t )$ are as follows:

$$
\phi _ { j } ( \rho t ) = \sum _ { k , l , \cdots } a _ { j k } a \cdot \cdot \cdot ,
$$

where $\rho t$ is a labelled tree with root $j$ , the sum over the $r ( \rho t ) - 1$ remaining indices $k , l , \cdot \cdot \cdot$ . The summand is a product of $r ( \rho t ) - 1 \ a$ ’s, where all fathers stand two by two with their sons as indices.

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } = 1 , } & { \qquad \displaystyle \sum _ { j = 1 } ^ { \lambda } b _ { j } \sum _ { k = 1 } ^ { 4 } a _ { j k } = \frac { 1 } { 2 } , } \\ { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l = 1 } ^ { 4 } a _ { j k } a _ { j l } = \frac { 1 } { 3 } , } & { \qquad \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l = 1 } ^ { 4 } a _ { j k } a _ { k l } = \frac { 1 } { 6 } , } \\ { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l , m = 1 } ^ { 4 } a _ { j k } a _ { j l } a _ { j m } = \frac { 1 } { 4 } , } & { \qquad \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l , m = 1 } ^ { 4 } a _ { j k } a _ { k l } a _ { j m } = \frac { 1 } { 8 } , } \\ { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l , m = 1 } ^ { 4 } a _ { j k } a _ { k l } a _ { k m } = \frac { 1 } { 1 2 } , } & { \qquad \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { j } \displaystyle \sum _ { k , l , m = 1 } ^ { 4 } a _ { j k } a _ { k l } a _ { l m } = \frac { 1 } { 2 4 } . } \end{array} \right.
$$

From the previous chapter on simplifying condition of symplectic R–K, we know that the system of Equation (1.25) only exists in 3 independent conditions (equation). In the above equation, last 4 conditions have only one independent condition. By symmetrically choosing $c _ { 1 } = c _ { 3 }$ , this condition is satisfied automatically. Taking ${ \overset { \cdot } { c _ { 1 } } } = { \overset { \cdot } { c _ { 3 } } } = { \frac { w _ { 1 } } { 2 } }$ $\dot { c } _ { 2 } = \frac { w _ { 0 } } { 2 }$ , by the first two conditions of Equation (1.25), we obtain the same equation

$$
2 w _ { 1 } + w _ { 0 } = 1 .
$$

Substituting the relation (1.26) in the order of conditions (1.25), we get

$$
2 w _ { 1 } ^ { 3 } + w _ { 0 } ^ { 3 } = 0 .
$$

These Equations (1.26) and (1.27) are just the same as in Subsection 8.1.1 for single equation.

From the literature[Fen85] , we know that the centered Euler scheme is symplectic, but trapezoidal scheme (1.1) is right non-symplectic as a result of nonlinear transformation [Dah75,QZZ95,Fen92] , the scheme (1.1) can transform the Euler center point form, therefore the trapezoidal form is nonstandard symplectic, just as discussed in Section 4.3 of Chapter 4. It is the same with the trapezoidal form, the centered Euler scheme may also be used to construct the higher order scheme. Because

$$
\left\{ \begin{array} { l } { { Z _ { 1 } = Z _ { 0 } + d _ { 1 } h f \Big ( \frac { Z _ { 0 } + Z _ { 1 } } { 2 } \Big ) , } } \\ { { Z _ { 2 } = Z _ { 1 } + d _ { 2 } h f \Big ( \frac { Z _ { 1 } + Z _ { 2 } } { 2 } \Big ) , } } \\ { { Z _ { 3 } = Z _ { 2 } + d _ { 3 } h f \Big ( \frac { Z _ { 2 } + Z _ { 3 } } { 2 } \Big ) , } } \end{array} \right.
$$

it is equally the same in $\mathbf { R - K }$ method with in the following Butcher tableau:

<table><tr><td>d</td><td>小</td><td>0</td><td>0</td></tr><tr><td>d+</td><td>d</td><td>小</td><td>0</td></tr><tr><td>d d1+d+</td><td>d</td><td>d2</td><td>d</td></tr><tr><td></td><td>d</td><td>d2</td><td>d</td></tr></table>

Using the same method, we can prove that , when $d _ { 1 } = d _ { 3 } = { \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } }$ $d _ { 2 } =$ $\frac { - 2 ^ { \frac { 1 } { 3 } } } { 2 - 2 ^ { \frac { 1 } { 3 } } }$ , the above scheme is fourth order, and the coefficient is entirely the same as in trapezoidal method.

# 8.2 Adjoint Method and Self-Adjoint Method

Here, we will introduce the concept of adjoint scheme and self-adjoint scheme. These two kinds of schemes are the foundation that construct higher order scheme in the future. First, we see several higher order schemes as the example, and seek common character which may supply method for constructing higher order scheme; In the Section 4.4 of Chapter 4, we discussed an explicit scheme for separable Hamiltonian system. We know

$$
\left\{ \begin{array} { l l } { p ^ { n + 1 } = p ^ { n } - \tau V _ { q } ( q ^ { n } ) , } \\ { q ^ { n + 1 } = q ^ { n } + \tau U _ { p } ( p ^ { n + 1 } ) } \end{array} \right.
$$

(where $\tau$ is step size, $p ^ { n } , q ^ { n }$ are numerical solution in step $n$ ) is of order 1. We shall compose this scheme (2.1) to a 2nd order scheme choosing a suitable coefficient of $\tau$ ,

$$
\left\{ \begin{array} { l l } { p ^ { n + \frac { 1 } { 2 } } = p ^ { n } - \frac { \tau } { 2 } V _ { q } ( q ^ { n } ) , } \\ { q ^ { n + \frac { 1 } { 2 } } = q ^ { n } + \tau U _ { p } ( p ^ { n + \frac { 1 } { 2 } } ) , } \\ { p ^ { n + 1 } = p ^ { n + \frac { 1 } { 2 } } - \frac { \tau } { 2 } V _ { q } ( q ^ { n + \frac { 1 } { 2 } } ) , } \\ { q ^ { n + 1 } = q ^ { n + \frac { 1 } { 2 } } . } \end{array} \right.
$$

This scheme is equal to the following:

$$
\left\{ \begin{array} { l } { { p ^ { n + \frac { 1 } { 2 } } = p ^ { n } - \frac { \tau } { 2 } V _ { q } ( q ^ { n } ) , } } \\ { { q ^ { n + \frac { 1 } { 2 } } = q ^ { n } + \frac { \tau } { 2 } U _ { p } ( p ^ { n + \frac { 1 } { 2 } } ) , } } \\ { { q ^ { n + 1 } = q ^ { n + \frac { 1 } { 2 } } + \frac { \tau } { 2 } U _ { p } ( p ^ { n + \frac { 1 } { 2 } } ) , } } \\ { { p ^ { n + 1 } = p ^ { n + \frac { 1 } { 2 } } - \frac { \tau } { 2 } V _ { q } ( q ^ { n + 1 } ) . } } \end{array} \right.
$$

This 2nd order scheme can also be defined as a self-adjoint scheme, see also $\left[ \mathrm { Y o s 9 0 } \right]$ .

$\mathrm { R u t h } ^ { \left[ \mathrm { R u t } 8 3 \right] }$ , using scheme (2.1), constructed a 3rd order scheme via composition method,

$$
\left\{ \begin{array} { l l } { p _ { 1 } = p ^ { k } - c _ { 1 } \tau V _ { q } ( q ^ { k } ) , \qquad } & { q _ { 1 } = q ^ { k } + d _ { 1 } \tau U _ { p } ( p _ { 1 } ) , } \\ { p _ { 2 } = p _ { 1 } - c _ { 2 } \tau V _ { q } ( q _ { 1 } ) , \qquad } & { q _ { 2 } = q _ { 1 } + d _ { 2 } \tau U _ { p } ( p _ { 2 } ) , } \\ { p ^ { k + 1 } = p _ { 2 } - c _ { 3 } \tau V _ { q } ( q _ { 2 } ) , \qquad } & { q ^ { k + 1 } = q _ { 2 } + d _ { 3 } \tau U _ { p } ( p ^ { k + 1 } ) . } \end{array} \right.
$$

When c1 = $c _ { 1 } = \frac { 7 } { 2 4 }$ , $c _ { 2 } = \frac { 4 } { 3 }$ , $c _ { 3 } = - { \frac { 1 } { 2 4 } }$ , $d _ { 1 } = \frac { 2 } { 3 }$ , $d _ { 2 } = - \frac { 2 } { 3 }$ , $d _ { 3 } = 1$ , this scheme is 3rd order. We may construct multistage schemes, in order to achieve the higher order precision. In literature $\mathrm { [ Q Z 9 2 , F e n 8 6 , F e n 9 1 , \bar { F } R 9 0 , R u t 8 3 ] }$ , we may see the following 4th order form:

$$
\left\{ \begin{array} { l l } { p _ { 1 } = p ^ { k } - c _ { 1 } \tau V _ { q } ( q ^ { k } ) , \qquad } & { q _ { 1 } = q ^ { k } + d _ { 1 } \tau U _ { p } ( p _ { 1 } ) , } \\ { p _ { 2 } = p _ { 1 } - c _ { 2 } \tau V _ { q } ( q _ { 1 } ) , \qquad } & { q _ { 2 } = q _ { 1 } + d _ { 2 } \tau U _ { p } ( p _ { 2 } ) , } \\ { p _ { 3 } = p _ { 2 } - c _ { 3 } \tau V _ { q } ( q _ { 2 } ) , \qquad } & { q _ { 3 } = q _ { 2 } + d _ { 3 } \tau U _ { p } ( p _ { 3 } ) , } \\ { p ^ { k + 1 } = p _ { 3 } - c _ { 4 } \tau V _ { q } ( q _ { 3 } ) , \qquad } & { q ^ { k + 1 } = q _ { 3 } + d _ { 4 } \tau U _ { p } ( p ^ { k + 1 } ) , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { l l } { { c _ { 1 } = 0 , } } & { { c _ { 2 } = c _ { 4 } = - { \displaystyle \frac { 1 } { 3 } } ( 2 + \alpha ) , } } & { { c _ { 3 } = { \displaystyle \frac { 1 } { 3 } } ( 1 + 2 \alpha ) , } } \\ { { d _ { 1 } = d _ { 4 } = { \displaystyle \frac { 1 } { 6 } } ( 2 + \alpha ) , } } & { { } } \\ { { d _ { 2 } = d _ { 3 } = { \displaystyle \frac { 1 } { 6 } } ( 1 - \alpha ) , } } & { { \alpha = \sqrt [ 3 ] { 2 } + \sqrt [ 3 ] { \displaystyle \frac { 1 } { 2 } } , } } \end{array} \right.
$$

or

$$
\left\{ \begin{array} { l l } { \displaystyle c _ { 1 } = c _ { 4 } = \frac { 1 } { 6 } ( 2 + \alpha ) , \quad c _ { 2 } = c _ { 3 } = \frac { 1 } { 6 } ( 1 - \alpha ) , } \\ { \displaystyle d _ { 1 } = d _ { 3 } = \frac { 1 } { 3 } ( 1 + 2 \alpha ) , } \\ { \displaystyle d _ { 2 } = - \frac { 1 } { 3 } ( 1 + 2 \alpha ) , \quad d _ { 4 } = 0 , \quad \alpha = \sqrt [ 3 ] { 2 } + \sqrt [ 3 ] { \frac { 1 } { 2 } } . } \end{array} \right.
$$

The above examples in the 3-stage fourth-order scheme give us an understanding. We can construct the higher order scheme through the low-order scheme, and this method is not limited the symplictic type. Because the usual structure uses the Taylor expansion, the comparison of coefficient of structure in the higher order form will be cumbersome, therefore in this section and next, we will use the Lie series method. This method is already used widely , for example Stanly. Stenberg, Alex, J. Dragt and F. Neri used the Lie series to study the differential equation, see also the literature [Ste84,DF76,DF83,Ner87] . Using the Lie series to study our question is convenient as there is no need to extract the Lie series item truly to which form it corresponds, but must use its form only. We will see this later.

We know that each scheme is always formal and is expressed as follows:

$$
y _ { n + 1 } = S ( \tau ) y _ { n } ,
$$

where $\tau$ is the step size. $S ( \tau )$ is called the integrator, but $y _ { n + 1 }$ and $y _ { n }$ are numerical solutions of equation in steps $n + 1$ and $n$ .

Definition 2.1. An integrator $S ^ { * } ( \tau )$ is called the adjoint integrator $S ( \tau )$ , if

$$
\begin{array} { r } { S ^ { * } ( - \tau ) S ( \tau ) = I , } \\ { S ( \tau ) S ^ { * } ( - \tau ) = I . } \end{array}
$$

That means $y _ { n + 1 } ~ = ~ S ( \tau ) y _ { n }$ , $y _ { n } ~ = ~ S ^ { * } ( - \tau ) y _ { n + 1 }$ , or $y _ { n + 1 } ~ = ~ S ^ { * } ( - \tau ) y _ { n }$ , $y _ { n } =$ $S ( \tau ) y _ { n + 1 }$ . In fact, $( 2 . 6 ) - ( 2 . 7 )$ equations are equivalent to

$$
\begin{array} { c } { { S ( - \tau ) S ^ { * } ( \tau ) = I , } } \\ { { S ^ { * } ( \tau ) S ( - \tau ) = I . } } \end{array}
$$

In order to prove this, set $\tau = - \tau ^ { ' }$ , then (2.6) – (2.7) becomes

$$
\left\{ \begin{array} { l l } { S ^ { * } ( \tau ^ { \prime } ) S ( - \tau ^ { \prime } ) = I , } \\ { S ( - \tau ^ { \prime } ) S ^ { * } ( \tau ^ { \prime } ) = I . } \end{array} \right.
$$

$\tau$ expresses the length of arbitrary step; therefore, the above equations are formula of (2.8), (2.9). Further, we would like to point out that the two conditions (2.6) and (2.7) are the same. Since form $S ^ { * } ( - \tau ) S ( \tau ) = I$ , we get

$$
S ^ { * } ( - \tau ) = S ^ { - 1 } ( \tau ) ,
$$

where $S ^ { - 1 } ( \tau )$ is the inverse of the integrator $S ( \tau )$ . Here, we always assume $S ( \tau )$ is invertible. So, we have

$$
S ( \tau ) S ^ { * } ( - \tau ) = S ( \tau ) S ^ { - 1 } ( \tau ) = I .
$$

The formula may result in (2.7) by (2.6), and vice versa.

But note the difference between $S ^ { * } ( \tau )$ and $S ^ { - 1 } ( \tau )$ , that is, $S ^ { * } ( - \tau ) = S ^ { - 1 } ( \tau )$ . Here, $S ^ { * } ( \tau )$ and $S ( \tau )$ is the same push-forward mapping, but $S ^ { - 1 } ( \tau )$ is the pull-back mapping.

For a convenient deduction in Section 8.3, we give another definition of a selfadjoint method[HNW93] here, and show that it is equivalent to definition adjoint (2.1). We rewrite (2.5) as follows:

$$
y _ { n + 1 } = y _ { n } + \tau \phi ( x , y _ { n } , \tau ) .
$$

$y _ { n } , y _ { n + 1 }$ is numerical solution for the equation $y ^ { \prime } = f ( x )$ in the $n$ and $n + 1$ step, and $\phi$ is increment function which the form (2.5) corresponds.

Definition 2.2. Scheme $y _ { n + 1 } = y _ { n } + \tau \phi ^ { * } ( x , y _ { n } , \tau )$ is an adjoint scheme (2.10), if it satisfies:

$$
\begin{array} { l } { { B = A - \tau \phi ( x + \tau , A , - \tau ) , } } \\ { { A = B + \tau \phi ^ { * } ( x , B , \tau ) . } } \end{array}
$$

Theorem 2.3. Definition 2.1 and Definition 2.2 are equivalent.

Proof. Since (2.8) – (2.9) and (2.6) – (2.7) are equivalent, (2.6) and (2.9) are also equivalent. It is enough to prove that (2.9) is equivalent to $( 2 . 1 1 ) - ( 2 . 1 2 ) .$ . Let

$$
\left\{ \begin{array} { l l } { { S ^ { * } ( \tau ) y _ { n } = y _ { n } + \tau \phi ^ { * } ( x , y _ { n } , \tau ) , } } \\ { { S ( \tau ) y _ { n } = y _ { n } + \tau \phi ( x , y _ { n } , \tau ) , } } \end{array} \right.
$$

first prove that $( 2 . 9 )  ( 2 . 1 1 ) - ( 2 . 1 2 )$ . Let

$$
\left\{ \begin{array} { l } { { A = y _ { n + 1 } , } } \\ { { B = A - \tau \phi ( x + \tau , A , - \tau ) , } } \end{array} \right.
$$

prove that (2.12), due to

$$
\begin{array} { l } { { S ^ { \ast } ( \tau ) S ( - \tau ) y _ { n + 1 } ~ = ~ S ^ { \ast } ( \tau ) \big ( y _ { n + 1 } - \tau \phi ( x + \tau , y _ { n + 1 } , - \tau ) \big ) } } \\ { { ~ = ~ y _ { n + 1 } - \tau \phi ( x + \tau , y _ { n + 1 } , - \tau ) } } \\ { { ~ } } \\ { { ~ + \tau \phi ^ { \ast } \big ( x , y _ { n + 1 } - \tau \phi ( x + \tau , y _ { n + 1 } , - \tau ) , \tau \big ) } } \\ { { ~ = ~ y _ { n + 1 } - \tau \phi ( x + \tau , y _ { n + 1 } , - \tau ) + \tau \phi ^ { \ast } ( x , B , \tau ) } } \\ { { ~ = ~ B + \tau \phi ^ { \ast } ( x , B , \tau ) } } \\ { { ~ = ~ I A . } } \end{array}
$$

By the last equality, also because $S ^ { * } ( \tau ) S ( - \tau ) = I$ , we have

$$
B + \tau \phi ^ { * } ( x , B , \tau ) = A ,
$$

this is the formula (2.12).

Now, we will prove : $( 2 . 1 1 ) - ( 2 . 1 2 ) \Rightarrow \ ( 2 . 9 )$ . Let

$$
\left\{ \begin{array} { l l } { { A = y _ { n + 1 } , } } \\ { { B = A - \tau \phi ( x + \tau , A , - \tau ) . } } \end{array} \right.
$$

Since

$$
\begin{array} { l } { { S ^ { * } ( \tau ) S ( - \tau ) y _ { n + 1 } ~ = ~ S ^ { * } ( \tau ) \bigl ( y _ { n + 1 } - \tau \phi ( x + \tau , y _ { n + 1 } , - \tau ) \bigr ) } } \\ { { { } } } \\ { { { } = ~ A - \tau \phi ( x + \tau , A , - \tau ) + \tau \phi ^ { * } ( x , B , \tau ) , } } \end{array}
$$

from (2.12), we have

$$
S ^ { * } ( \tau ) S ( - \tau ) A = B + \tau \phi ^ { * } ( x , B , \tau ) = A = I A ,
$$

i.e., $S ^ { * } ( \tau ) S ( - \tau ) = I$ .

Definition 2.4. An integrator $S ( \tau )$ is self-adjoint, if

$$
S ^ { * } ( \tau ) = S ( \tau ) , \quad \mathrm { i . e . , } \quad S ( - \tau ) S ( \tau ) = I .
$$

$\mathrm { I n } ^ { \mathrm { [ Y o s 9 0 ] } }$ , the integrator with the property $S ( - \tau ) S ( \tau ) = I . \mathrm { ~ H } .$ . Yoshida called this operator as reversible. We see that time reversibility and self-adjointness are the same. The time reversible (i.e., self-adjoint) integrator plays an important role in this chapter due to its special property.

Theorem 2.5. For every integrator $S ( \tau )$ , $S ^ { * } \left( { \frac { \tau } { 2 } } \right) S \left( { \frac { \tau } { 2 } } \right) \left( o r S \left( { \frac { \tau } { 2 } } \right) S ^ { * } \left( { \frac { \tau } { 2 } } \right) \right)$ is selfadjoint integrator[QZ92,Str68] .

Proof. We must prove that $S ^ { * } \Big ( \frac { \tau } { 2 } \Big ) = S \Big ( \frac { \tau } { 2 } \Big )$ is self-adjoint, i.e.,

$$
\left( S ^ { * } ( \tau ) S ( \tau ) \right) ^ { * } = S ^ { * } ( \tau ) S ( \tau ) .
$$

By Definition 2.1,we have $S ^ { * } ( \tau ) S ( - \tau ) = I$ , then

$$
\begin{array} { l l l } { { \left( S ^ { * } ( \tau ) S ( \tau ) \right) ^ { * } ~ = ~ \left( S ^ { * } ( - \tau ) S ( - \tau ) \right) ^ { - 1 } } } \\ { { } } & { { } } \\ { { } } & { { = ~ S ^ { - 1 } ( - \tau ) \bigl ( S ^ { * } ( - \tau ) \bigr ) ^ { - 1 } } } \\ { { } } & { { } } \\ { { } } & { { = ~ S ^ { * } ( \tau ) \bigl ( S ^ { * } ( - \tau ) \bigr ) ^ { - 1 } . } } \end{array}
$$

Because we also have

$$
S ^ { * } ( - \tau ) S ( \tau ) = I ,
$$

i.e.,

$$
\left( S ^ { \ast } ( - \tau ) \right) ^ { - 1 } = S ( \tau ) ,
$$

therefore

$$
\left( S ^ { * } ( \tau ) S ( \tau ) \right) ^ { * } = S ^ { * } ( \tau ) S ( \tau ) .
$$

Therefore, the theorem is completed.

Theorem 2.6. If $S _ { 1 } ( \tau )$ and $S _ { 2 } ( \tau )$ are self-adjoint integrators, then symmetrical composition S1(τ )S2(τ )S1(τ ) is self-adjoint[QZ92] .

Proof. Consider $S _ { 1 } ( \tau )$ and $S _ { 2 } ( \tau )$ are self-adjoint integrators, then

$$
\begin{array} { l l l } { { \left( S _ { 1 } ( \tau ) S _ { 2 } ( \tau ) S _ { 1 } ( \tau ) \right) ^ { * } ~ = ~ \left( S _ { 1 } ( - \tau ) S _ { 2 } ( - \tau ) S _ { 1 } ( - \tau ) \right) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ S _ { 1 } ( - \tau ) ^ { - 1 } S _ { 2 } ( - \tau ) ^ { - 1 } S _ { 1 } ( - \tau ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ S _ { 1 } ^ { * } ( \tau ) S _ { 2 } ^ { * } ( \tau ) S _ { 1 } ^ { * } ( \tau ) = S _ { 1 } ( \tau ) S _ { 2 } ( \tau ) S _ { 1 } ( \tau ) . } } \end{array}
$$

The theorem is proved.

We pointed out that generally, a combination of self-adjoint operators is not necessarily from the self-adjoint. One simple example is

$$
\left( S _ { 1 } ( \tau ) S _ { 2 } ( \tau ) \right) ^ { * } = S _ { 2 } ( \tau ) S _ { 1 } ( \tau ) \neq S _ { 1 } ( \tau ) S _ { 2 } ( \tau ) ,
$$

where $S _ { 1 } ( \tau )$ and $S _ { 2 } ( \tau )$ are self-adjoint operators, but they not commutative. We will construct a higher order form in the below section.

# 8.3 Construction of Higher Order Schemes

We will first give constructed method for the higher difference scheme, and will further prove that the Gauss–Legendre method is a self-adjoint method. We have given some example for structured higher order schemes.

In this section, we will introduce first-order differential operators, Lie series and some of their properties, all these are the basis of further deduction.

Denote:

$$
\begin{array} { l } { f = ( f _ { 1 } , f _ { 2 } , \cdots , f _ { n } ) ^ { \mathrm { T } } } \\ { g = ( g _ { 1 } , g _ { 2 } , \cdots , g _ { n } ) ^ { \mathrm { T } } } \\ { D = \left( \frac { \mathrm { d } } { \mathrm { d } y _ { 1 } } , \cdots , \frac { \mathrm { d } } { \mathrm { d } y _ { n } } \right) ^ { \mathrm { T } } , } \end{array}
$$

where $f _ { 1 } , f _ { 2 } , \cdots , f _ { n }$ and $g _ { 1 } , g _ { 2 } , \cdots , g _ { n }$ are scalar function. Let

$$
L _ { f } = f ^ { \mathrm { T } } D = \sum _ { i = 1 } ^ { n } f _ { i } { \frac { \partial } { \partial y _ { i } } }
$$

be a first-order differential operator. The action of $L _ { f }$ on a scalar function $\varphi$ is,

$$
L _ { f } \varphi = \left( \sum _ { i = 1 } ^ { n } f _ { i } { \frac { \partial } { \partial y _ { i } } } \right) \varphi = f ^ { \operatorname { T } } D \varphi ( y ) .
$$

It is linear and satisfies the Leibniz formula, i.e., for two scalar functions $\varphi _ { 1 }$ and $\varphi _ { 2 }$ ,

$$
\begin{array} { r l } & { L _ { f } ( \lambda _ { 1 } \varphi _ { 1 } + \lambda _ { 2 } \varphi _ { 2 } ) = \lambda _ { 1 } L _ { f } \varphi _ { 1 } + \lambda _ { 2 } L _ { f } \varphi _ { 2 } , \quad \forall \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } . } \\ & { L _ { f } ( \varphi _ { 1 } \varphi _ { 2 } ) = \varphi _ { 1 } L _ { f } \varphi _ { 2 } + \varphi _ { 2 } L _ { f } \varphi _ { 1 } . } \end{array}
$$

Definition 3.1. The commutator of two first-order differential operators $L _ { f }$ and $L _ { g }$ is defined by

$$
\left[ L _ { f } , L _ { g } \right] = L _ { f } L _ { g } - L _ { g } L _ { f } .
$$

The commutator of the two first-order differential operators is still a first differential operator, since

$$
 \begin{array} { r l } { L _ { f } L _ { g } \varphi } &  = f ^ { \mathrm { T } } D g ^ { \mathrm { T } } D \varphi = \displaystyle \sum _ { j = 1 } ^ { n } f _ { j } { \frac { \partial } { \partial y _ { j } } } \displaystyle \sum _ { i = 1 } ^ { n } g _ { i } { \frac { \partial } { \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } f _ { j } { \frac { \partial g _ { i } } { \partial y _ { j } } } { \frac { \partial } { \partial y _ { i } } } \varphi + \displaystyle \sum _ { i , j = 1 } ^ { n } f _ { j } g _ { i } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } f _ { j } g _ { i } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { j } \partial y _ { i } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j } { \frac { \partial ^ { 2 } \varphi } { \partial y _ { i } \partial y _ { j } } } \varphi = \displaystyle \sum _ { i , j = 1 } ^ { n } g _ { i } g _ { j }  \ \end{array}
$$

therefore,

$$
( L _ { f } L _ { g } - L _ { g } L _ { f } ) \varphi = \sum _ { i , j = 1 } ^ { n } \left( f _ { j } { \frac { \partial g _ { i } } { \partial y _ { j } } } - g _ { j } { \frac { \partial f _ { i } } { \partial y _ { j } } } \right) { \frac { \partial } { \partial y _ { i } } } \varphi ,
$$

this means

$$
[ L _ { f } , L _ { g } ] = L _ { c } , \quad c = [ c _ { 1 } , c _ { 2 } , \cdots , c _ { n } ] , \quad c _ { i } = \sum _ { j = 1 } ^ { n } \left( f _ { j } { \frac { \partial g _ { i } } { \partial y _ { j } } } - g _ { j } { \frac { \partial f _ { i } } { \partial y _ { j } } } \right) ,
$$

and $L _ { c }$ will still be the first-order differential operator. It is very easy to prove the following properties of bracket

$$
\begin{array} { c } { { [ L _ { f } , L _ { f } ] = 0 , } } \\ { { { } } } \\ { { { } [ \lambda _ { 1 } L _ { f _ { 1 } } + \lambda _ { 2 } L _ { f _ { 2 } } , L _ { g } ] = \lambda _ { 1 } [ L _ { f _ { 1 } } , L _ { g } ] + \lambda _ { 2 } [ L _ { f _ { 2 } } , L _ { g } ] , \quad \forall \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } . } } \end{array}
$$

The commutator also satisfies the Jacobi identity, i.e., if $L _ { f } , L _ { g } , L _ { h }$ are three firstorder differential operators, then

$$
\begin{array} { r } { \left[ [ L _ { f } , L _ { g } ] , L _ { h } \right] + \left[ [ L _ { g } , L _ { h } ] , L _ { f } \right] + \left[ [ L _ { h } , L _ { f } ] , L _ { g } \right] = 0 . } \end{array}
$$

(3.7) is very easy to prove, the detailed proof process is seen $\left[ \mathrm { A r n } 8 9 \right]$ . From the above, we know that first-order differential operator forms a Lie algebra.

Definition 3.2. A Lie series is an exponential of a first-order linear differential operator

$$
\mathrm { e } ^ { t L _ { f } } = \sum _ { n = 0 } ^ { \infty } \frac { t ^ { n } L _ { f } ^ { n } } { n ! } .
$$

The action of a Lie series a scalar function $\varphi ( y )$ is given by:

$$
\begin{array} { l } { { { \displaystyle { \mathrm { e } } ^ { t L _ { f } } } \varphi ~ = ~ \sum _ { k = 0 } ^ { \infty } { \displaystyle { \frac { t ^ { k } L _ { f } ^ { k } } { k ! } } } \varphi ( y ) = \sum _ { k = 0 } ^ { \infty } { \displaystyle { \frac { t ^ { k } } { k ! } } } { \left( f ^ { \mathrm { T } } ( y ) D \right) } ^ { k } \varphi ( y ) } } \\ { { ~ = ~ \varphi ( y ) + t f ^ { \mathrm { T } } ( y ) ( D ( y ) ) + { \displaystyle { \frac { t ^ { 2 } } { 2 } } } f ^ { \mathrm { T } } ( y ) D \big ( f ^ { \mathrm { T } } ( y ) D \varphi ( y ) \big ) + \cdots } . }  \end{array}
$$

Taylor expansion gives us an one elementary example of a Lie series

$$
\begin{array} { r l } { \displaystyle \mathtt { e } ^ { t [ 1 , 1 , \cdots , 1 ] D } \varphi ( y ) } & { = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { t ^ { k } } { k ! } \left( \displaystyle \sum _ { i = 1 } ^ { n } \frac { \mathrm { d } } { \mathrm { d } y _ { i } } \right) ^ { k } \varphi ( y ) } \\ & { = \varphi \big ( y + t ( 1 , 1 , \cdots , 1 ) ^ { \mathrm { T } } \big ) . } \end{array}
$$

We have seen several properties of Lie series, which are similar to those of $[ { \mathrm { S t e 8 4 } } ]$ . Let,

$$
\begin{array} { r } { f = ( f _ { 1 } ( y ) , f _ { 2 } ( y ) , \cdot \cdot \cdot , f _ { n } ( y ) ) ^ { \mathrm { T } } , } \\ { g = ( g _ { 1 } ( y ) , g _ { 2 } ( y ) , \cdot \cdot \cdot , g _ { n } ( y ) ) ^ { \mathrm { T } } , } \end{array}
$$

and

$$
\begin{array} { r } { \mathtt { e } ^ { t f ^ { \mathrm { T } } D } g = \big ( \mathtt { e } ^ { t f ^ { \mathrm { T } } D } g _ { 1 } , \mathtt { e } ^ { t f ^ { \mathrm { T } } D } g _ { 2 } , \cdot \cdot \cdot , \mathtt { e } ^ { t f ^ { \mathrm { T } } D } g _ { n } \big ) ^ { \mathrm { T } } , } \end{array}
$$

then, we have the following:

Property 3.3. The Lie series has the compositionality

$$
\mathrm { e } ^ { t L _ { f } } g ( y ) = g ( \mathrm { e } ^ { t L _ { f } } y ) .
$$

Proof. It is enough to prove

$$
\mathrm { e } ^ { t L _ { f } } g _ { m } ( y ) = g _ { m } ( \mathrm { e } ^ { t L _ { f } } y ) .
$$

Since

$$
\mathrm { e } ^ { t L _ { f } } y = \sum _ { k = 0 } ^ { \infty } { \frac { t ^ { k } L _ { f } ^ { k } } { k ! } } y = \sum _ { k = 0 } ^ { \infty } { \frac { t ^ { k } } { k ! } } \left( \sum _ { i = 1 } ^ { n } f _ { i } { \frac { \partial } { \partial y _ { i } } } \right) ^ { k } y ,
$$

considering $j$ component $( 1 \leq j \leq n )$ , in $ { \mathbf { e } } ^ { t L _ { f } } y$ , we have

$$
\mathrm { e } ^ { t L _ { f } } y _ { j } = \sum _ { k = 0 } ^ { \infty } \Big ( \sum _ { i = 1 } ^ { n } f _ { i } \frac { \partial } { \partial y _ { i } } \Big ) ^ { k } y _ { j } = y _ { j } + \sum _ { k = 1 } ^ { \infty } \frac { t ^ { k } } { k ! } L _ { f } ^ { k - 1 } f _ { j } ,
$$

then

$$
\begin{array} { r c l } { { g _ { m } ( { \bf e } ^ { t L _ { f } } y ) } } & { { = } } & { { g _ { m } \displaystyle \left( y _ { 1 } + \sum _ { k = 1 } ^ { \infty } \frac { t ^ { k } } { k ! } L _ { f } ^ { k - 1 } f _ { 1 } ( y ) , \cdots , y _ { n } + \sum _ { k = 1 } ^ { \infty } \frac { t ^ { k } } { k ! } L _ { f } ^ { k - 1 } f _ { n } ( y ) \right) } } \\ { { } } & { { } } & { { = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { t ^ { k } } { k ! } \left( \sum _ { i = 1 } ^ { n } f _ { i } ( y ) \frac { \partial } { \partial y _ { i } } \right) ^ { k } g _ { m } ( y ) = e ^ { t L _ { f } } g _ { m } ( y ) . } } \end{array}
$$

The proof can be obtained.

Property 3.4. Product preservation property

$$
\mathrm { e } ^ { t L _ { f } } ( p q ) = ( \mathrm { e } ^ { t L _ { f } } p ) ( \mathrm { e } ^ { t L _ { f } } q ) ,
$$

where $p ( y ) , q ( y )$ are scalar functions.

Proof. By (3.2) – (3.3) and (3.8), (3.12) can be obtained by direct computation.

Property 3.5. Baker-Campbell-Hausdroff formula (simply called BCH formula): All first differential operators constituted a Lie algebra. Therefore, we have the following BCH formula:

$$
{ \mathrm { e } } ^ { t L _ { f } } { \mathrm { e } } ^ { t L _ { g } } = { \mathrm { e } } ^ { t ( L _ { f } + L _ { g } ) + t ^ { 2 } w _ { 2 } + t ^ { 3 } w _ { 3 } + t ^ { 4 } w _ { 4 } + \cdots } ,
$$

where

$$
\begin{array} { l } { { w _ { 2 } = \displaystyle \frac { 1 } { 2 } [ L _ { f } , L _ { g } ] , } } \\ { { } } \\ { { w _ { 3 } = \displaystyle \frac { 1 } { 1 2 } \big [ [ L _ { f } , L _ { g } ] , L _ { f } \big ] + \displaystyle \frac { 1 } { 1 2 } \big [ [ L _ { f } , L _ { g } ] , L _ { g } \big ] , } } \\ { { } } \\ { { w _ { 4 } = \displaystyle \frac { 1 } { 2 4 } \big [ L _ { f } , \big [ L _ { g } \big [ L _ { g } , L _ { f } \big ] \big ] \big ] , } } \\ { { } } \\ { { \therefore . . . } } \end{array}
$$

Property 3.6. If the differential equation property is,

$$
\begin{array} { r } { { \boldsymbol y } ( t ) = { \mathrm e } ^ { t f ^ { \mathrm { T } } D } { \boldsymbol y } , \quad { \boldsymbol y } = { \boldsymbol y } ( 0 ) , } \end{array}
$$

then

$$
{ \dot { y } } ( t ) = f ( y ( t ) ) .
$$

Proof. Since $y _ { i } ( t ) = \mathbf { e } ^ { t f ^ { \mathrm { T } } ( y ) D } y _ { i } ( 0 )$ , then

$$
\frac { \mathrm { d } } { \mathrm { d } t } y _ { i } ( t ) = \mathrm { e } ^ { t f ^ { \mathrm { T } } ( y ) D } f ^ { \mathrm { T } } ( y ) D y _ { i } ( 0 ) = \mathrm { e } ^ { t f ^ { \mathrm { T } } D } f _ { i } ( y ) .
$$

From Property 3.3, we have

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } y _ { i } ( t ) = f _ { i } ( \mathbf { e } ^ { t { f ^ { \mathrm { T } } } D } y ) = f _ { i } { \big ( } y _ { 1 } ( t ) , y _ { 2 } ( t ) , \cdot \cdot \cdot , y _ { n } ( t ) { \big ) } = f _ { i } ( y ( t ) ) .
$$

The proof can be obtained.

From Property 3.6, we know that equation $\dot { y } = f ( y )$ can express the solution $y ( t ) =$ $ { \mathrm { e } } ^ { t L _ { f } } y ( 0 )$ , Section 8.2 has discussed that the integral $S ( \tau )$ can also be represented in this form. If $S ( \tau )$ has the group property about $\tau$ , it will be the phase flow of autonomous ODE ${ \frac { \operatorname { d } y } { \operatorname { d } \tau } } = f ( y )$ . However, in our problem, there is just one parameter family $S ( \tau )$ without group property. So, there just exists a formal vector field $f ^ { \tau } ( y )$ , which defines only the formal autonomous system

$$
\begin{array} { r } { \frac { \mathrm { d } y } { \mathrm { d } t } = f ^ { \tau } ( y ) . } \end{array}
$$

Its formal phase flow concerning two parameters $\tau , t$ , can be expressed by $\mathrm { e } ^ { t L _ { f } \tau }$ . Take the diagonal phase flow

$$
\mathbf { e } ^ { t L _ { f ^ { \tau } } } | _ { t = \tau } = \mathbf { e } ^ { \tau L _ { f ^ { \tau } } } .
$$

This is just $S ( \tau )$ Lie series expression. See the next chapter to know more about the formal vector field and the formal phase flow. Since $f ^ { \tau } ( y )$ is a formal vector field, it is a formal power series in $\tau$ . Thus, the exponential representation of $S ( \tau )$ will the following form:

$$
S ( \tau ) = \exp { ( \tau A + \tau ^ { 2 } B + \tau ^ { 3 } C + \tau ^ { 4 } D + \tau ^ { 5 } E + \cdot \cdot \cdot ) } ,
$$

and series

$$
\tau A + \tau ^ { 2 } B + \tau ^ { 3 } C + \tau ^ { 4 } D + \tau ^ { 5 } E + \cdot \cdot \cdot
$$

may not be convergence, where $A , B , C , D , E , \cdots$ are first-order differential operators. Therefore, we have:

Theorem 3.7. Every integrator $S ( \tau )$ has a formal Lie expression $[ \mathrm { Q } Z ^ { 9 2 } ]$

We use Theorem 3.7 to derive an important conclusion.

Theorem 3.8. Every self-adjoint integrator has an even order of accuracy[QZ92] .

Proof. Let $S ( \tau )$ be a self-adjoint integrator. Expand $S ( \tau )$ in the exponential form

$$
S ( \tau ) = \exp { ( \tau w _ { 1 } + \tau ^ { 2 } w _ { 2 } + \tau ^ { 3 } w _ { 3 } + \cdot \cdot \cdot ) } .
$$

Suppose $S ( \tau )$ is of order $n$ , then

$$
S ( \tau ) y ( 0 ) = { \mathrm e } ^ { \tau L _ { f } } y ( 0 ) + O ( \tau ^ { n + 1 } ) ,
$$

when the ODE to be solved is ${ \dot { y } } = f ( y )$ . Since

$$
\mathbf { e } ^ { \tau L _ { f } } + o \left( \tau ^ { n + 1 } \right) = \mathbf { e } ^ { \tau L _ { f } + O ( \tau ^ { n + 1 } ) } ,
$$

then

$$
S ( \tau ) =  { \mathbf { e } } ^ { \tau L _ { f } + O ( \tau ^ { n + 1 } ) } .
$$

We must show that $n$ is an even number. This means that we have to prove

$$
w _ { 2 } = w _ { 4 } = w _ { 6 } = w _ { 8 } = \cdot \cdot \cdot = 0 .
$$

Since

$$
S ( - \tau ) = \exp { ( - \tau w _ { 1 } + \tau ^ { 2 } w _ { 2 } - \tau ^ { 3 } w _ { 3 } + \cdot \cdot \cdot ) } ,
$$

and using the BCH formula, we get

$$
S ( \tau ) S ( - \tau ) = \exp { ( 2 \tau ^ { 2 } w _ { 2 } + O ( \tau ^ { 3 } ) ) } .
$$

Since $S ( \tau )$ is self-adjoint, i.e., $S ( \tau ) S ( - \tau ) = I$ , So (3.14) means $w _ { 2 } = 0$ , and (3.14) becomes

$$
S ( \tau ) S ( - \tau ) = \exp \big ( 2 \tau ^ { 4 } w _ { 4 } + O ( \tau ^ { 5 } ) \big ) .
$$

This leads to $w _ { 4 } = 0$ . Continuing this process, we have

$$
w _ { 2 } = w _ { 4 } = w _ { 6 } = \cdot \cdot \cdot = w _ { 2 k } = \cdot \cdot \cdot = 0 .
$$

Thus $S ( \tau )$ becomes

$$
S ( \tau ) = \exp { ( \tau w _ { 1 } + \tau ^ { 3 } w _ { 3 } + \tau ^ { 5 } w _ { 5 } + \cdot \cdot \cdot ) } .
$$

Therefore, if $S ( \tau )$ is of order $n$ , then $n$ must be an even number. Since $S ( \tau )$ is at least of order 1, and if $n \geqslant 2$ , we have $w _ { 1 } = L _ { f }$ , because $S ( \tau )$ Lie series expression is unique. -

Now, we will provide a corollary on the construction of higher order schemes.

Corollary 3.9. Let $S ( \tau )$ be a self-adjoint integrator with order $2 n$ , if $c _ { 1 } , c _ { 2 }$ satisfies

$$
2 c _ { 1 } ^ { 2 n + 1 } + c _ { 2 } ^ { 2 n + 1 } = 0 , \quad 2 c _ { 1 } + c _ { 2 } = 1 ,
$$

then composition integrator $S ( c _ { 1 } \tau ) ~ S ( c _ { 2 } \tau ) ~ S ( c _ { 1 } \tau )$ is of order $2 n + 2$ , solving the above equations, we get $[ \mathrm { Q } Z ^ { 9 2 } ]$ :

$$
c _ { 1 } = { \frac { 1 } { 2 - { \sqrt [ { 2 n + 1 } ] { 2 } } } } , ~ c _ { 2 } = { \frac { \sqrt [ { 2 n + 1 } ] { 2 } } { 2 - { \sqrt [ { 2 n + 1 } ] { 2 } } } } .
$$

Proof. From Theorem 2.6, we know $S ( c _ { 1 } \tau ) S ( c _ { 2 } \tau ) S ( c _ { 1 } \tau )$ is a self-adjoint operator and Theorem 3.8 shows it to be even order. Since $S ( \tau )$ is of order $2 n$ , the expansions in exponential form of $S ( c _ { 1 } \tau ) , S ( c _ { 2 } \tau )$ are

$$
\begin{array} { r l } & { S ( c _ { 1 } \tau ) = \exp \big ( c _ { 1 } \tau w _ { 1 } + \tau ^ { 2 n + 1 } c _ { 1 } ^ { 2 n + 1 } w _ { 2 n + 1 } + O ( \tau ^ { 2 n + 3 } ) \big ) , } \\ & { S ( c _ { 2 } \tau ) = \exp \big ( c _ { 2 } \tau w _ { 1 } + \tau ^ { 2 n + 1 } c _ { 2 } ^ { 2 n + 1 } w _ { 2 n + 1 } + O ( \tau ^ { 2 n + 3 } ) \big ) . } \end{array}
$$

Again, by BCH formula, we get

$$
\begin{array} { r l } & { S ( c _ { 1 } \tau ) S ( c _ { 2 } \tau ) S ( c _ { 1 } \tau ) } \\ & { = \exp \big ( ( 2 c _ { 1 } + c _ { 2 } ) \tau w _ { 1 } + ( 2 c _ { 1 } ^ { 2 n + 1 } + c _ { 2 } ^ { 2 n + 1 } ) \tau ^ { 2 n + 1 } w _ { 2 n + 1 } + O ( \tau ^ { 2 n + 3 } ) \big ) } \\ & { = \exp \big ( \tau w _ { 1 } + O ( \tau ^ { 2 n + 3 } ) \big ) . } \end{array}
$$

The proof can be obtained.

H. Yoshida in $\left[ \mathrm { Y o s 9 0 } \right]$ obtained the same result for symplectic explicit integrator used to solve separable systems. The result can be applied to non-Hamiltonian systems and non-symplectic integrators.

In this chapter, we will extend these results to solve general autonomous system’s form. Some examples of adjoint scheme and its construction are given below. A concrete method to construct an adjoint for any given scheme is also given. This method can be referred in literature [HNW93] . If the numerical solution is $y _ { \tau }$ , then any given scheme may be expressed as:

$$
y _ { \tau } ( x + \tau ) = y _ { \tau } ( x ) + \tau \phi ( x , y _ { \tau } ( x ) , \tau ) ,
$$

where $\phi$ is increment function corresponding to the scheme and $\tau$ is step size. By substituting $- \tau$ instead of $\tau$ in (3.15), we get

$$
y _ { - \tau } ( x - \tau ) = y _ { - \tau } ( x ) - \tau \phi \big ( x , y _ { - \tau } ( x ) , - \tau \big ) ,
$$

and $x + \tau$ instead of $x$ , we get

$$
y _ { - \tau } ( x ) = y _ { - \tau } ( x + \tau ) - \tau \phi ( x + \tau , y _ { - \tau } ( x + \tau ) , - \tau ) .
$$

For sufficiently $\tau$ , Equation (3.16), for $y _ { - \tau } ( x + \tau )$ possesses a unique solution (by the implicit function theorem) and expresses in the following form:

$$
y _ { - \tau } ( x + \tau ) = y _ { - \tau } ( x ) + \tau \phi ^ { * } \bigl ( x , y _ { - \tau } ( x ) , \tau \bigr ) ,
$$

and (3.17) is just the adjoint scheme for (3.15). $y _ { - \tau }$ is the adjoint scheme of numerical solution. $\phi ^ { * }$ is the increment function corresponding to the adjoint scheme (the above process equals to: first solve $S ( - \tau )$ , then solve $S ^ { - 1 } ( - \tau ) )$ . In fact; let $y _ { - \tau } ( x + \tau ) =$ $A$ , $y _ { - \tau } ( x ) = B$ , from (3.16) and (3.17), we have

$$
\left\{ \begin{array} { l } { { B = A - \tau \phi ( x + \tau , A , - \tau ) , } } \\ { { A = B + \tau \phi ^ { * } ( x , B , \tau ) , } } \end{array} \right.
$$

as in Equations (2.11) and (2.12) in Definition 2.2. Next, we would like to consider self adjoint conditions for $\mathbf { R - K }$ method. Since most one-step multistage methods can be written in $\mathbf { R - K }$ form, we now turn to the $\mathbf { R - K }$ methods to get some results which may be useful. The general $s$ -stage $\mathbf { R - K }$ method is in the form $\mathbf { R - K }$ .

$$
\left\{ \begin{array} { l l } { \displaystyle k _ { i } = f \bigg ( \boldsymbol { x } _ { 0 } + c _ { i } \tau , \boldsymbol { y } _ { 0 } + \tau \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \bigg ) , } \\ { \displaystyle y _ { 1 } = y _ { 0 } + \tau \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } , } \end{array} \right.
$$

where $y _ { 0 }$ is numerical solution in $x _ { 0 } , y _ { 1 }$ is numerical value in $x _ { 0 } + \tau$ , then

$$
c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j }
$$

may be expressed in Butcher tableau:

$$
{ \begin{array} { r l } & { c _ { 1 } } \\ & { c _ { 2 } } \\ & { \vdots } \\ & { c _ { s } } \end{array} } \left| { \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & \\ & { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ & & { \vdots } & { \vdots } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} } \right.
$$

The proof for the following Lemma $3 . 1 0 \sec ^ { [ \mathrm { H N W 9 3 } ] }$ . It can be proved by Definition 2.2 directly. Since we have proved the equivalence between Definition 2.1 and 2.2.

Lemma 3.10. Every R–K method has an adjoint method, whose coefficients $a _ { i j } ^ { * }$ , $b _ { j } ^ { * }$ , $c _ { j } ^ { * }$ $( i , j = 1 , \cdots , s )$ can be written as follows:

$$
\left\{ \begin{array} { l l } { c _ { i } ^ { * } = 1 - c _ { s + 1 - i } ^ { * } , } \\ { a _ { i j } ^ { * } = b _ { s + 1 - j } - a _ { s + 1 - i , s + 1 - j } , } \\ { b _ { j } ^ { * } = b _ { s + 1 - j } . } \end{array} \right.
$$

Lemma 3.11. If $a _ { s - i + 1 , s - j + 1 } + a _ { i j } = b _ { s - j + 1 } = b _ { j }$ , then the corresponding $R – K$ method (3.18) is self-adjoint.

Concentrating on semi-explicit symplectic $\mathbf { R - K }$ method, we have:

Theorem 3.12. The semi-explicit symplectic $R – K$ method for autonomous systems is self-adjoint if its Butcher tableau is of the form $\{ Q Z ^ { g _ { 2 } } \}$ .

Proof. We know that the Butcher tableau of semi-explicit symplectic R–K method must be of the form

Tab. 3.1is obvious from Lemma 3.11.

By Lemma 3.11, we know that possesses such form of Table 3.1 is evident. For non self-adjoint symplectic integrator $S ( \tau )$ , $S ^ { * } ( \tau ) S ( \tau )$ is self-adjoint, and is symplectic. In order to prove that it is symplectic, it is enough to prove $S ^ { \ast } ( \tau )$ is symplectic. If $S ^ { * } ( \tau ) S ( - \tau ) = I$ , then $S ^ { * } ( \tau ) = S ^ { - 1 } ( - \tau )$ . As $S ( \tau )$ is symplectic, $S ( - \tau )$

and $S ^ { - 1 } ( - \tau )$ are symplectic integrators, and therefore $S ^ { \ast } ( \tau )$ is also symplectic. The two Lemmas given below can be seen in paper[HNW93] . Lemma 3.13 is derived from Theorem 1.24 of Chapter 7 and Theorem 1.1 of Chapter 8. -

Lemma 3.13. If in an implicit $s$ -stage $R – K$ method, all $c _ { i }$ $( i = 1 , \cdots , s )$ are different and at least of order $s$ , then it is a collocation method iff it is satisfies:

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { q - 1 } = \frac { c _ { i } ^ { q } } { q } , \quad i = 1 , \cdots , s , \quad q = 1 , \cdots , s .
$$

Lemma 3.14. Based on the symmetrical distribution, collocation algorithm is selfadjoint.

As the Legendre polynomial is the orthogonal, coefficient of Gauss–Legendre method $c _ { i }$ $( i = 1 , \cdots , s )$ takes the root of Legendre polynomial $P _ { s } ( 2 c - 1 )$ in which the root is not mutually same. Moreover, the coefficient of Gauss–Legendre method $a _ { i j }$ $( i , j = 1 , \cdots , s )$ satisfies formula (3.21) , and the Gauss–Legendre method is of the order $2 s$ ; therefore, it is the collocation method. For details, $\mathrm { s e e } ^ { \mathrm { [ H N W 9 3 ] } }$ . We have:

Theorem 3.15. Gauss–Legendre methods are self-adjoint.

Proof. Since Gauss–Legendre method is collocation method, we only need to prove $c _ { i } = 1 - c _ { s + 1 - i }$ , and $c _ { i }$ are symmetrical distributions, where $c _ { 1 } , c _ { 2 } , \cdots , c _ { s }$ are the root of Legendre polynomial $P _ { s } ( 2 c - 1 )$ (lower index denotes order of polynomial). If the root of $P _ { s } ( w )$ are $w _ { 1 } , w _ { 2 } , \cdots , w _ { s }$ , then

$$
c _ { i } = { \frac { 1 } { 2 } } - { \frac { w _ { i } } { 2 } } , \quad i = 1 , \cdots , s ,
$$

i.e., $c _ { i } = 1 - c _ { s + 1 - i }$ and $w _ { i } + w _ { s + 1 - i } = 0$ are equivalent.

Legendre polynomial can be constructed by

$$
\left\{ \begin{array} { l l } { q _ { 0 } ( w ) = 1 , \quad q _ { - 1 } ( w ) = 0 , } \\ { \qquad } \\ { q _ { i + 1 } ( w ) = ( w - \delta _ { i + 1 } ) q _ { i } ( w ) - \gamma _ { i + 1 } ^ { 2 } q _ { i - 1 } ( w ) , \quad i = 0 , 1 , \cdots , } \end{array} \right.
$$

where

$$
\delta _ { i + 1 } = { \frac { ( w q _ { i } , q _ { i } ) } { ( q _ { i } , q _ { i } ) } } , \quad i \geq 0 ,
$$

$$
\gamma _ { i + 1 } ^ { 2 } = \left\{ \begin{array} { l l l } { { 0 , } } & { { \mathrm { f o r } } } & { { i = 0 , } } \\ { { \frac { \left( q _ { i } , q _ { i } \right) } { \left( q _ { i - 1 } , q _ { i - 1 } \right) } , } } & { { \mathrm { f o r } } } & { { i \geq 1 , } } \end{array} \right.
$$

and

$$
( q _ { i } , q _ { j } ) = \int _ { - 1 } ^ { 1 } q _ { i } ( w ) q _ { j } ( w ) { \bf d } w .
$$

We obtain $q _ { 1 } = w$ , $q _ { 2 } = w ^ { 2 } - \frac { 1 } { 3 }$ , assuming $q _ { 2 n } ( w )$ is an even function and $q _ { 2 n - 1 } \ ( w )$ is an odd function. We proceed by induction on $n$ , for $n = 1$ , this has established.

Suppose $q _ { 2 n }$ is an even function, and $q _ { 2 n - 1 }$ is an odd function. Prove that $n + 1$ is also true.

Since

$$
\delta _ { 2 n + 1 } = { \frac { ( w q _ { 2 n } , q _ { 2 n } ) } { ( q _ { 2 n } , q _ { 2 n } ) } } = { \frac { \int _ { - 1 } ^ { 1 } \mathrm { o d d d } \mathrm { d } w } { ( q _ { 2 n } , q _ { 2 n } ) } } = { \frac { \mathrm { e v e n } | _ { - 1 } ^ { 1 } } { ( q _ { 2 n } , q _ { 2 n } ) } } = 0 ,
$$

then $q _ { 2 n + 1 } = w q _ { 2 n } - \gamma _ { 2 n + 1 } ^ { 2 } q _ { 2 n - 1 } ( w ) = \mathfrak { c }$ odd function−odd function $=$ odd function.

$$
\delta _ { 2 n + 2 } = { \frac { ( w q _ { 2 n + 1 } , q _ { 2 n + 1 } ) } { ( q _ { 2 n + 1 } , q _ { 2 n + 1 } ) } } = { \frac { \int _ { - 1 } ^ { 1 } \mathrm { o d d } \mathrm { d } w } { \left( q _ { 2 n + 1 } , q _ { 2 n + 1 } \right) } } = 0 ,
$$

then $q _ { 2 n + 2 } = w q _ { 2 n + 1 } - \gamma _ { 2 n + 2 } ^ { 2 } q _ { 2 n } ( w ) = \mathrm { i s }$ an even function. We have proved this conclusion for $n + 1$ . From this, the $P _ { 2 n } ( w )$ root may be written in the following sequence:

$$
- w _ { 1 } , - w _ { 2 } , \cdot \cdot \cdot , - w _ { n } , w _ { n } , \cdot \cdot \cdot , w _ { 2 } , w _ { 1 } .
$$

But the root of $p _ { 2 n + 1 } ( w )$ has the following form:

$$
- w _ { 1 } , - w _ { 2 } , \cdot \cdot \cdot , - w _ { n } , 0 , w _ { n } , \cdot \cdot \cdot , w _ { 2 } , w _ { 1 } ,
$$

where $w _ { i } > 0 , w _ { i } > w _ { i + 1 } ( i = 1 , \cdots , n )$ , therefore $w _ { i } + w _ { n + 1 - i } = 0$ . Even though we have the direct proof of Theorem 3.15, the computation is tedious. As a result of Gauss–Legendre method coefficient $a _ { i j } , b _ { j }$ satisfies the following equation:

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { q - 1 } = \frac { c _ { i } ^ { q } } { q } , \quad i = 1 , \cdots , s , \quad q = 1 , \cdots , s , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { q - 1 } = \frac { 1 } { q } , \quad q = 1 , \cdots , s . } } \end{array}
$$

Using the linear algebra knowledge, we have

$$
\begin{array} { l } { \displaystyle a _ { i j } = \sum _ { k = 1 } ^ { s } \frac { ( - 1 ) ^ { n + k } \frac { c _ { i } ^ { k } } { k } } { \ s { \prod _ { j \ne l } ^ { ( c _ { j } - c _ { l } ) } \varphi _ { k j } } } , \quad \displaystyle n = \frac { s } { 2 } , } \\ { \displaystyle b _ { j } = \sum _ { k = 1 } ^ { s } \frac { ( - 1 ) ^ { n + k } \frac { 1 } { k } } { \ s { \prod _ { j \ne l } ^ { ( c _ { j } - c _ { l } ) } \varphi _ { k j } } } , \qquad i , j , l = 1 , \cdots , s , } \end{array}
$$

where

$$
\left\{ \begin{array} { l l } { \varphi _ { k j } = \displaystyle \sum _ { \{ t _ { 1 } , t _ { 2 } , \cdots , t _ { s - k } \} \subset \{ 1 , 2 , \cdots , j - 1 , j + 1 , \cdots , s \} } c _ { t _ { 1 } } c _ { t _ { 2 } } \cdot \cdot \cdot c _ { t _ { s - k } } , \quad k < s , } \\ { \varphi _ { s j } = 1 . } \end{array} \right.
$$

The direct calculation may result in

$$
\begin{array} { l } { { \displaystyle \sum _ { k = 1 } ^ { s } \displaystyle \frac { ( - 1 ) ^ { n + k } \frac { c _ { i } ^ { k } } { k } \varphi _ { k j } = \int _ { 0 } ^ { c _ { i } } l _ { j } ( t ) \mathrm { d } t } , \quad j = 1 , \cdots , s , } } \\ { { \displaystyle \sum _ { k = 1 } ^ { s } \displaystyle \frac { ( - 1 ) ^ { n + k } \frac { 1 } { k } } { \prod _ { j \neq l } ( c _ { j } - c _ { l } ) } \varphi _ { k j } = \int _ { 0 } ^ { 1 } l _ { j } ( t ) \mathrm { d } t } , \quad j = 1 , \cdots , s , }  \end{array}
$$

$\prod \left( t - c _ { k } \right)$ where $l _ { j } = { \frac { \underset { k \neq j } { \mathbf { 1 } } } { \underset { k \neq j } { \prod } } } ( c _ { j } - c _ { k } )$ , when $c _ { i } = 1 - c _ { s + 1 - i }$ , we have $l _ { i } ( t ) = l _ { s + 1 - i ( 1 - t ) }$ , then

$$
a _ { s + 1 - i , s + 1 - j } + a _ { i j } = b _ { s + 1 - j } = b _ { j } ,
$$

from (3.24) and (3.25), it is easy to prove.

Below given is an example to construct a self-adjoint scheme using a given scheme [QZ92] .

Example 3.16. It is well know that scheme (2.1) is of the first order. From the above method, the adjoint scheme will be

$$
\left\{ \begin{array} { l } { { q ^ { n + 1 } = q ^ { n } + \tau U _ { p } ( p ^ { n } ) , } } \\ { { p ^ { n + 1 } = p ^ { n } - \tau V _ { q } ( q ^ { n + 1 } ) . } } \end{array} \right.
$$

Composition scheme (2.2) from (2.1) and (3.26) is of order 2. In order to maintain the transient step size, original $\tau$ will shrink and will become $\frac { \tau } { 2 }$ , because the present scheme is $S ^ { * } \left( \frac { \tau } { 2 } \right) S \left( \frac { \tau } { 2 } \right)$ . If it is self-adjoint, the transient length of step size is maintained as $\tau$ .

Example 3.17. It is easy to prove that scheme

$$
y _ { 1 } = y _ { 0 } + \frac \tau 2 \big [ f ( y _ { 1 } ) + f ( y _ { 0 } ) \big ]
$$

is self-adjoint, and will be of order 2. Symmetrical composition scheme (1.22) is 3- stage of 4th order and also self-adjoint.

Example 3.18. The explicit 4th order symplectic scheme (2.4) can be composed by $S _ { 2 } ( x _ { 1 } \tau ) ~ S _ { 2 } ( x _ { 2 } \tau ) ~ S _ { 2 } ( x _ { 1 } \tau )$ and developed as follows:

$$
S _ { V } \underbrace { ( c _ { 1 } \tau ) S _ { U } ( d _ { 1 } \tau ) S _ { V } } _ { S _ { 2 } ( x _ { 1 } \tau ) } ( c _ { 2 } \underbrace { \tau ) S _ { U } ( d _ { 2 } \tau ) S _ { V } } _ { S _ { 2 } ( x _ { 2 } \tau ) } \underbrace { ( c _ { 3 } \tau ) S _ { U } ( d _ { 3 } \tau ) S _ { V } ( c _ { 4 } \tau ) S _ { U } ( d _ { 4 } \tau ) } _ { S _ { 2 } ( x _ { 1 } \tau ) } .
$$

noting Corollary 3.9, we get:

$$
{ \begin{array} { r l } & { c _ { 1 } = c _ { 4 } = { \frac { x _ { 1 } } { 2 } } = { \frac { 1 } { 2 \ - { \sqrt [ { 3 } ] { 3 } } } } = 0 . 6 7 5 6 0 3 5 , } \\ & { d _ { 1 } = d _ { 3 } = x _ { 1 } = { \frac { 1 } { 2 \left( 2 \ - { \sqrt [ { 3 } ] { 2 } } \right) } } = 1 . 3 5 1 2 0 7 1 9 , } \\ & { d _ { 2 } = { \frac { - { \sqrt [ { 3 } ] { 2 } } } { 2 \ - { \sqrt [ { 3 } ] { 2 } } } } = x _ { 2 } = - 1 . 7 0 2 4 1 4 2 , \quad d _ { 4 } = 0 , } \\ & { c _ { 2 } = c _ { 3 } = { \frac { x _ { 1 } + x _ { 2 } } { 2 } } = { \frac { 1 \ - { \sqrt [ { 3 } ] { 2 } } } { 2 ( 2 \ - { \sqrt [ { 3 } ] { 2 } } ) } } = - 0 . 1 7 5 6 0 3 6 . } \end{array} }
$$

Example 3.19. By literature $\left[ \mathrm { F Q 9 1 } \right]$ , we know that one class of symplectic scheme for equation $\frac { \mathrm { d } \boldsymbol { y } } { \mathrm { d } t } = \boldsymbol { J \nabla } H$

$$
y ^ { k + 1 } = y ^ { k } + \tau J ( \nabla H ) \left( { \frac { 1 } { 2 } } ( I + J B ) y ^ { k + 1 } + { \frac { 1 } { 2 } } ( I - J B ) y ^ { k } \right) , \quad B ^ { \mathrm { T } } = B ,
$$

$$
J = \left[ \begin{array} { c c } { { O } } & { { - I _ { n } } } \\ { { I _ { n } } } & { { O } } \end{array} \right] , \quad I = \left[ \begin{array} { c c } { { I _ { n } } } & { { O } } \\ { { O } } & { { I _ { n } } } \end{array} \right] ,
$$

this scheme is of order 1, if $B \neq O$ ; if $B = O$ , then the scheme will be of order 2.

In scheme (3.27), if $B = O$ , we can prove it is self-adjoint.

When $B \neq O$ , if integrator of scheme (3.27) is $S ( \tau , H , B )$ , then adjoint integrator of scheme (3.27) will be

$$
S ( \tau , H , - B ) = S ^ { * } ( \tau , H , B ) .
$$

Composition integrator from $S { \Big ( } { \frac { \tau } { 2 } } { \Big ) }$ and $S ^ { * } \Big ( \frac { \tau } { 2 } \Big )$ is self-adjoint with second order, concrete scheme is

$$
\left\{ \begin{array} { l l } { y _ { 1 } = y ^ { k } + \frac { \tau } { 2 } J ( \nabla H ) \Big ( \frac { 1 } { 2 } ( I - J B ) y _ { 1 } + \frac { 1 } { 2 } ( I + J B ) y ^ { k } \Big ) , } \\ { y ^ { k + 1 } = y _ { 1 } + \frac { \tau } { 2 } J ( \nabla H ) \Big ( \frac { 1 } { 2 } ( I + J B ) y ^ { k + 1 } + \frac { 1 } { 2 } ( I - J B ) y _ { 1 } \Big ) . } \end{array} \right.
$$

# 8.4 Stability Analysis for Composition Scheme

In this paragraph, will discuss the stability of the three-stage $[ \mathrm { Q } Z ^ { 9 3 } ]$ , fourth order scheme which was constructed in Section 8.1

$$
\begin{array} { l } { { y _ { n + \frac { 1 } { 3 } } = y _ { n } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { \frac { 1 } { 3 } } ) } \tau f \big ( f ( y _ { n } ) + f ( y _ { n + \frac { 1 } { 3 } } ) \big ) , } } \\ { { \ } } \\ { { y _ { n + \frac { 2 } { 3 } } = y _ { n + \frac { 1 } { 3 } } + \displaystyle \frac { - 2 ^ { \frac { 1 } { 3 } } } { 2 ( 2 - 2 ^ { \frac { 1 } { 3 } } ) } \tau \big ( f ( y _ { n + \frac { 1 } { 3 } } ) + f ( y _ { n + \frac { 2 } { 3 } } ) \big ) , } } \\ { { \ } } \\ { { y _ { n + 1 } = y _ { n + \frac { 2 } { 3 } } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { \frac { 1 } { 3 } } ) } \tau \big ( f ( y _ { n + \frac { 2 } { 3 } } ) + f ( y _ { n + 1 } ) \big ) . } } \end{array}
$$

We will prove that although the trapezoid method is $A$ -stable, scheme (4.1) is not $A$ -stable. Fortunately , the unstable region is very small, as Fig. 4.2 (enlaged figure is Fig.4.1) shows, and scheme (4.1) is still useful for solving stiff systems. Judging from the size and location of the unstable region of scheme (4.1), we know it is safe for systems which have eigenvalues not very adjacent to the real axis, while some other methods which have unstable regions near the imaginary axis, such as Gear’s are safe for systems which have eigenvalues not very adjacent to the imaginary axis.

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0006_pages_0351-0420/auto/images/ca1496cc93ae0ed1f5382e18d8e4bf49c4dc49f6d58594835a20a73a988ee467.jpg)  
Fig. 4.1. Closed curve $S$ which contains all zero point of scheme (4.1)

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0006_pages_0351-0420/auto/images/6d280c00cc44f4183ee57ead4d042baf4099e85a7153f6480e2b2b306712c696.jpg)  
Fig. 4.2. Stability region size and position of (4.1)

Just the same as in scheme (4.1), the Euler midpoint rule can also be used to construct a scheme:

$$
\left\{ \begin{array} { l } { \displaystyle y _ { n + \frac { 1 } { 3 } } = y _ { n } + \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } \tau f \left( \frac { y _ { n } + y _ { n + \frac { 1 } { 3 } } } { 2 } \right) , } \\ { \displaystyle y _ { n + \frac { 2 } { 3 } } = y _ { n + \frac { 1 } { 3 } } + \frac { - 2 ^ { \frac { 1 } { 3 } } } { 2 - 2 ^ { \frac { 1 } { 3 } } } \tau f \left( \frac { y _ { n + \frac { 1 } { 3 } } + y _ { n + \frac { 2 } { 3 } } } { 2 } \right) , } \\ { \displaystyle y _ { n + 1 } = y _ { n + \frac { 2 } { 3 } } + \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } \tau f \left( \frac { y _ { n + \frac { 2 } { 3 } } + y _ { n + 1 } } { 2 } \right) . } \end{array} \right.
$$

Scheme (4.2) is symplectic, but scheme (4.1) is non-symplectic. We now study the stability of scheme (4.1). Note that scheme (4.1) is not $A \cdot$ - stable, whereas the trapezoid method is. To show this, we apply scheme (4.1) to test equation

$$
\dot { y } = \lambda y , \quad y ( 0 ) = y _ { 0 } , \quad \lambda \in { \bf C } , \quad { \mathrm R e } \lambda < 0 ,
$$

which yields

$$
\left\{ \begin{array} { l l } { { \displaystyle y _ { n + \frac { 1 } { 3 } } = y _ { n } + c _ { 1 } \frac { \tau } { 2 } \bigl ( \lambda y _ { n } + \lambda y _ { n + \frac { 1 } { 3 } } \bigr ) } , } \\ { { \displaystyle y _ { n + \frac { 2 } { 3 } } = y _ { n + \frac { 1 } { 3 } } + c _ { 2 } \frac { \tau } { 2 } \bigl ( \lambda y _ { n + \frac { 1 } { 3 } } + \lambda y _ { n + \frac { 2 } { 3 } } \bigr ) } , } \\ { { \displaystyle y _ { n + 1 } = y _ { n + \frac { 2 } { 3 } } + c _ { 1 } \frac { \tau } { 2 } \bigl ( \lambda y _ { n + \frac { 2 } { 3 } } + \lambda y _ { n + 1 } \bigr ) , } } \end{array} \right.
$$

i.e.,

$$
\left\{ \begin{array} { l } { \displaystyle y _ { n + \frac { 1 } { 3 } } = \frac { 1 + \frac { c _ { 1 } \lambda \tau } { 2 } } { 1 - \frac { c _ { 1 } \lambda \tau } { 2 } } y _ { n } , } \\ { \displaystyle y _ { n + \frac { 2 } { 3 } } = \frac { 1 + \frac { c _ { 2 } \lambda \tau } { 2 } } { 1 - \frac { c _ { 2 } \lambda \tau } { 2 } } y _ { n + \frac { 1 } { 3 } } , } \\ { \displaystyle y _ { n + 1 } = \frac { 1 + \frac { c _ { 1 } \lambda \tau } { 2 } } { 1 - \frac { c _ { 1 } \lambda \tau } { 2 } } y _ { n + \frac { 2 } { 3 } } , } \end{array} \right.
$$

where $c _ { 1 } = { \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } }$ , $c _ { 2 } = { \frac { - 2 ^ { \frac { 1 } { 3 } } } { 2 - 2 ^ { \frac { 1 } { 3 } } } }$ . Let $\frac { \lambda \tau } { 2 } = z , z \in { \bf C }$ , we have

$$
y _ { n + 1 } = { \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 1 } z ) } } y _ { n } .
$$

Definition 4.1. The stable region $R$ of scheme (4.1) is:

$$
R = \{ \lambda \tau \in { \bf C } | | \frac { ( 1 + \frac { c _ { 1 } \lambda \tau } { 2 } ) ( 1 + \frac { c _ { 2 } \lambda \tau } { 2 } ) ( 1 + \frac { c _ { 1 } \lambda \tau } { 2 } ) } { ( 1 - \frac { c _ { 1 } \lambda \tau } { 2 } ) ( 1 - \frac { c _ { 2 } \lambda \tau } { 2 } ) ( 1 - \frac { c _ { 1 } \lambda \tau } { 2 } ) } | < 1 , \mathrm { R e } ( \lambda \tau ) < 0 \} ,
$$

i.e.,

$$
R = \left\{ z \in \mathbf { C } \left| \left| \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 1 } z ) } \right| < 1 , \mathrm { R e } z < 0 \right. \right\} .
$$

Obviously, when $z  \frac { 1 } { c _ { 2 } } ( < 0 )$ , we have

$$
\left| \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 1 } z ) } \right| \longrightarrow \infty .
$$

This means schemes (4.1) cannot be stable in the adjacent region ${ \frac { 1 } { c _ { 2 } } } .$ . Thus, we obtain the following theorem:

Theorem 4.2. Scheme (4.1) is not $A$ -stable.

Since scheme (4.1) is not $A$ -stable, we will figure out the stable region of it. To do this, we will first study the roots of the following equation:

$$
\left| \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 1 } z ) } \right| = 1 .
$$

Once the roots of (4.8) are known, it is not difficult to get the stable region of (4.1). Note Equation (4.8) is equivalent to

$$
{ \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 1 } z ) } } = \mathbf { e } ^ { \mathbf { i } \theta } , \quad 0 \leq \theta < 2 \pi .
$$

From (4.9), we get the following polynomial:

$$
\begin{array} { r l } & { c _ { 1 } ^ { 2 } c _ { 2 } ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 3 } + ( 2 c _ { 1 } c _ { 2 } + c _ { 1 } ^ { 2 } ) ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 2 } } \\ & { \quad + ( 2 c _ { 1 } + c _ { 2 } ) ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z + ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) = 0 , \quad 0 \leq \theta < 2 \pi . } \end{array}
$$

Since $2 c _ { 1 } + c _ { 2 } = 1$ , and $a = c _ { 1 } ^ { 2 } c _ { 2 } , b = 2 c _ { 1 } c _ { 2 } + c _ { 1 } ^ { 2 }$ , then (4.10) becomes:

$$
a ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 3 } + b ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 2 } + ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z + ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) = 0 , \quad 0 \leq \theta < 2 \pi .
$$

Consider the roots of (4.11) in two cases.

Case 4.3. $1 + \mathrm { e } ^ { \mathrm { i } \theta } \neq 0$ (i.e., $0 \leq \theta < 2 \pi , \theta \neq \pi ) .$

By computing the roots of polynomial (4.11), we get

$$
z _ { 1 } = x + y \mathbf { i } , \quad z _ { 2 } = - x + y \mathbf { i } , \quad z _ { 3 } = w \mathbf { i } , \quad x , y , w \in \mathbf { C }
$$

when $\theta$ is chosen as a definite value. $z _ { 1 } , z _ { 2 } , z _ { 3 }$ should satisfy

$$
\begin{array} { r c l } { ( z - z _ { 1 } ) ( z - z _ { 2 } ) ( z - z _ { 3 } ) } & { = } & { a ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 3 } + b ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) z ^ { 2 } + ( 1 + \mathrm { e } ^ { \mathrm { i } \theta } ) z } \\ & & { + ( 1 - \mathrm { e } ^ { \mathrm { i } \theta } ) = 0 } \\ & & { \iff \left\{ \begin{array} { l l } { z _ { 1 } + z _ { 2 } + z _ { 3 } = - \displaystyle \frac { b } { a } \Big ( \displaystyle \frac { 1 - \mathrm { e } ^ { \mathrm { i } \theta } } { 1 + \mathrm { e } ^ { \mathrm { i } \theta } } \Big ) , } \\ { z _ { 1 } z _ { 2 } + z _ { 1 } z _ { 3 } + z _ { 2 } z _ { 3 } = \displaystyle \frac { 1 } { a } , } \\ { z _ { 1 } z _ { 2 } z _ { 3 } = - \displaystyle \frac { 1 } { a } \Big ( \displaystyle \frac { 1 - \mathrm { e } ^ { \mathrm { i } \theta } } { 1 + \mathrm { e } ^ { \mathrm { i } \theta } } \Big ) . } \end{array} \right. } \end{array}
$$

Since

$$
\frac { 1 - \mathrm { e } ^ { \mathrm { i } \theta } } { 1 + \mathrm { e } ^ { \mathrm { i } \theta } } = \frac { ( 1 - \cos \theta ) - \mathrm { i } \sin \theta } { ( 1 + \cos \theta ) + \mathrm { i } \sin \theta } = - \frac { \sin \theta } { 1 + \cos \theta } \mathrm { i } ,
$$

then

$$
\left\{ \begin{array} { l l } { \displaystyle z _ { 1 } + z _ { 2 } + z _ { 3 } = \frac { b } { a } \frac { \sin \theta } { 1 + \cos \theta } \mathrm { i } = \mathrm { i } p _ { 1 } , } \\ { \displaystyle z _ { 1 } z _ { 2 } + z _ { 1 } z _ { 3 } + z _ { 2 } z _ { 3 } = \frac { 1 } { a } = p _ { 2 } , } \\ { \displaystyle z _ { 1 } z _ { 2 } z _ { 3 } = \frac { 1 } { a } \frac { \sin \theta } { 1 + \cos \theta } \mathrm { i } = \mathrm { i } p _ { 3 } , } \end{array} \right.
$$

where $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are real numbers. From (4.12) and (4.14), we have equations of $x , y , w$ as the following:

$$
\begin{array} { l } { 2 y + w = p _ { 1 } , } \\ { x ^ { 2 } + y ^ { 2 } + 2 y w = - p _ { 2 } , } \\ { x ^ { 2 } w + y ^ { 2 } w = - p _ { 3 } . } \end{array}
$$

Now, we will prove that Equations system (4.15)–(4.17) exists as a set of real solution. In fact, from (4.16) and (4.17), we get:

$$
p _ { 2 } w + 2 y w ^ { 2 } = p _ { 3 } .
$$

From (4.15) and (4.18), we have

$$
w ^ { 3 } - p _ { 1 } w ^ { 2 } - p _ { 2 } w + p _ { 3 } = 0 .
$$

Since $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are all real, (4.19) is a polynomial with real coefficient and has one real root and two conjugate complex roots. Using the real root $w$ from (4.19), we can get a real value of $y$ from (4.15) , and from (4.16) and (4.17), we have $x ^ { 2 } = { }$ real, then $x$ is real or pure imaginary. If $x$ is pure imaginary, then from (4.12), $z _ { 1 } , z _ { 2 } , z _ { 3 }$ are all pure imaginaries, so all the the roots of (4.11) are on the imaginary axis. This means that if we assume

$$
V ( z ) = \left| \frac { ( 1 + c _ { 1 } z ) ( 1 + c _ { 2 } z ) ( 1 + c _ { 1 } z ) } { ( 1 - c _ { 1 } z ) ( 1 - c _ { 2 } z ) ( 1 - c _ { 2 } z ) } \right| ,
$$

then, $V ( z ) > 1$ or $V ( z ) < 1$ for $\begin{array} { r } { \operatorname { R e } \left( z \right) < 0 } \end{array}$ . For the same reason that scheme (4.1) cannot be $A$ -stable, $V ( z ) > 1$ for Re $( z ) < 0$ is possible, but we have $V ( - 0 . 5 ) < 1$ , and $V ( z )$ is continuous except at $\frac { 1 } { c _ { 2 } }$ . Thus, $x$ is impossible to be pure imaginary, so it must be real. Since polynomial (4.11) only has three roots, we will get the same results of $z _ { 1 } , z _ { 2 } , z _ { 3 }$ if we use other value of $w$ , real or complex.

Case 4.4. $1 + \mathrm { e } ^ { \mathrm { i } \theta } = 0$ (i.e., $\theta = \pi ,$ ).

When $\theta = \pi$ , (4.11) becomes $z ^ { 2 } = - \frac { 1 } { b } > 0$ , then it has two real roots $\pm \sqrt { - \frac { 1 } { b } }$

Eventually, we get the following:

Theorem 4.5. The three roots of polynomial (4.11) are in the form :

$$
z _ { 1 } = - x + y \mathbf { i } , \quad z _ { 2 } = x + y \mathbf { i } , \quad z _ { 3 } = w \mathbf { i } ,
$$

where $x , y , w$ are all real.

Theorem 4.5 tells us that there is a root of (4.10) on the imaginary, and that the two other roots are located symmetrically with respect to the imaginary axis. Thus, there is only one root on the left open semi-plane. Computation shows that these roots form a closed curve $S$ (when $\theta$ changes from 0 to $2 \pi$ ), as in Fig. 4.1.

From (4.15) – (4.17), we get the equation for $S$ :

$$
\left\{ \begin{array} { l l } { x ^ { 2 } - 3 y ^ { 2 } + 2 p _ { 1 } y + p _ { 2 } = 0 , } & { \quad 0 \leq \theta < 2 \pi , \quad \theta \neq \pi . } \\ { 2 y x ^ { 2 } + 2 y ^ { 3 } - p _ { 1 } x ^ { 2 } - p _ { 1 } y ^ { 2 } - p _ { 3 } = 0 , } & { \quad 0 \leq \theta < 2 \pi , \quad \theta \neq \pi . } \end{array} \right.
$$

and

$$
x = \pm \sqrt { - { \frac { 1 } { b } } } , \quad y = 0 , \quad \mathrm { f o r } \theta = \pi ,
$$

where $z = - x + \mathrm { i } y$ $, p _ { 1 } = \frac { b \sin \theta } { a ( 1 + \cos \theta ) } , p _ { 2 } = \frac { 1 } { a } , p _ { 3 } = \frac { \sin \theta } { a ( 1 + \cos \theta ) } .$

Since in $S$ $S , V ( z ) > 1$ , and when $z  \infty$ , $V ( Z ) \to 1$ , we can conclude the stability of scheme (4.1).

Theorem 4.6. The stable region $R$ of scheme (4.1) $i s ^ { [ Q Z 9 3 ] }$ :

$$
R = \{ z \in { \bf C } \ | \ z o u t s i d e \ S \ a n d \ \mathrm { R e } z < 0 \} , \quad i . e . ,
$$

$R = \{ \lambda \tau \in \mathbf { C } \mid \lambda \tau$ outside $S ^ { * }$ and $\mathrm { R e } \left( \lambda \tau \right) < 0 \}$ , where $S ^ { * } = \left\{ z \in \mathbf { C } \mid \frac { z } { 2 } \in S \right\}$

Scheme (4.1) is not $A$ -stable, the outside region of it is infinite, and the unstable region is very small. The unstable region is blackened in Fig. 4.2, it is a little “disk” about $- 1 . 1 8$ on the real axis. For every definite $\lambda$ , we can choose some special step length $\tau$ , such that $\lambda \tau$ will not be in $S ^ { * }$ , while the step-length $\tau$ need not be very small for $\lambda$ which has a big modulus. Because of linear cases, scheme (4.2) is equivalent to (4.1). So, scheme (4.2) has exactly the same stable region as (4.1). Thus, we conclude that scheme (4.1) and (4.2) are still useful for solving stiff problems, which we wanted to show in example.

Following are some numerical tests for stability of scheme (4.1).

Example 4.7. Numerical test for orders of schemes (4.1) and (4.2).

To test the order scheme (4.1) and (4.2), we apply them to the following Hamiltonian system:

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } p } { \mathrm { d } t } = - \frac { \partial H } { \partial q } = - w ^ { 2 } q - q ^ { 3 } , } \\ { \frac { \mathrm { d } q } { \mathrm { d } t } = \frac { \partial H } { \partial p } = p , } \end{array} \right.
$$

where the Hamiltonian $H = \frac { 1 } { 2 } \big ( p ^ { 2 } + w ^ { 2 } q ^ { 2 } + \frac { 1 } { 2 } q ^ { 4 } \big )$ , and compare the numerical solutions with trapezoid method and centered Euler scheme.

For convenience, the numerical solution of $p$ and $q$ can be denoted as

$1 ^ { \circ }$ (4.1) by $T 4 p , T 4 q$ .   
$2 ^ { \circ }$ (4.2) by $E 4 p$ , $E 4 q$ .   
$3 ^ { \circ }$ trapezoid scheme by $T 2 p , T 2 q$ .

$4 ^ { \circ }$ centered Euler scheme by $E 2 p , E 2 q$ . Respectively, we use double precision in all computations. We can see the following explicit scheme:

$$
\left\{ \begin{array} { l l } { p _ { n + \frac { 1 } { 2 } } = p _ { n } - \frac { \tau } { 2 } V _ { q } ( q _ { n } ) , } \\ { q _ { n + \frac { 1 } { 2 } } = q _ { n } + \frac { \tau } { 2 } U _ { p } ( p _ { n + \frac { 1 } { 2 } } ) , } \\ { q _ { n + 1 } = q _ { n + \frac { 1 } { 2 } } + \frac { \tau } { 2 } U _ { p } ( p _ { n + \frac { 1 } { 2 } } ) , } \\ { p _ { n + 1 } = p _ { n + \frac { 1 } { 2 } } - \frac { \tau } { 2 } V _ { q } ( q _ { n + 1 } ) , } \end{array} \right.
$$

$$
{ \begin{array} { r l } & { c _ { 1 } = c _ { 4 } = { \frac { x _ { 1 } } { 2 } } = { \frac { 1 } { 2 \ - { \sqrt [ { 3 } ] { 3 } } } } = 0 . 6 7 5 6 0 3 5 , } \\ & { d _ { 1 } = d _ { 3 } = x _ { 1 } = { \frac { 1 } { 2 ( 2 \ - { \sqrt [ { 3 } ] { 2 } } ) } } = 1 . 3 5 1 2 0 7 1 9 , } \\ & { d _ { 2 } = { \frac { - { \sqrt [ { 3 } ] { 2 } } } { 2 \ - { \sqrt [ { 3 } ] { 2 } } } } = x _ { 2 } = - 1 . 7 0 2 4 1 4 2 , \quad d _ { 4 } = 0 , } \\ & { c _ { 2 } = c _ { 3 } = { \frac { x _ { 1 } + x _ { 2 } } { 2 } } = { \frac { 1 \ - { \sqrt [ { 3 } ] { 2 } } } { 2 ( 2 \ - { \sqrt [ { 3 } ] { 2 } } ) } } = - 0 . 1 7 5 6 0 3 6 . } \end{array} }
$$

A separable system with $H = V ( q ) + U ( p )$ is self-adjoint, so it can be used to construct fourth-order scheme to get (4.1) and (4.2). From Sections 8.2 and 8.3, the simplified fourth-order scheme can be written taking $c _ { 1 } = { \frac { 1 } { 2 - 2 ^ { \frac { 1 } { 3 } } } } = c _ { 3 }$ , $c _ { 2 } =$ 2 13 1 , x1 = x3 = 1.35120719, $x _ { 2 } = - 1 . 7 0 2 4 1 4 2$ . For details see Example 3.18. 2 2 3

$$
\left\{ \begin{array} { l l } { p _ { n + \frac { 1 } { 4 } } = p _ { n } - x _ { 1 } \frac { T } { 2 } V _ { q } ( q _ { n } ) , } \\ { q _ { n + \frac { 1 } { 3 } } = q _ { n } + x _ { 1 } \tau U _ { p } ( p _ { n + \frac { 1 } { 4 } } ) , } \\ { p _ { n + \frac { 1 } { 2 } } = p _ { n + \frac { 1 } { 4 } } - \frac { x _ { 1 } + x _ { 2 } } { 2 } \tau V _ { q } ( q _ { n + \frac { 1 } { 3 } } ) , } \\ { q _ { n + \frac { 2 } { 3 } } = q _ { n + \frac { 1 } { 3 } } + x _ { 2 } \tau U _ { p } ( p _ { n + \frac { 1 } { 2 } } ) , } \\ { p _ { n + \frac { 3 } { 4 } } = p _ { n + \frac { 1 } { 2 } } - \frac { x _ { 2 } + x _ { 3 } } { 2 } \tau V _ { q } ( q _ { n + \frac { 2 } { 3 } } ) , } \\ { q _ { n + 1 } = q _ { n + \frac { 3 } { 2 } } + x _ { 3 } \tau U _ { p } ( p _ { n + \frac { 3 } { 4 } } ) , } \\ { p _ { n + 1 } = p _ { n + \frac { 3 } { 4 } } - x _ { 3 } \frac { \tau } { 2 } V _ { q } ( q _ { n + 1 } ) , } \end{array} \right.
$$

where $p _ { n + \frac { 1 } { 4 } } , p _ { n + \frac { 1 } { 2 } } , p _ { n + \frac { 3 } { 4 } }$ and $q _ { n + \frac { 1 } { 3 } } , \ q _ { n + \frac { 2 } { 3 } }$ denote the numerical solution of different stages at every step. Scheme (4.24) has been proved by $_ \mathrm { H }$ . Yoshida to be a fourthorder scheme in $\left[ \mathrm { Y o s 9 0 } \right]$ . We can apply scheme (4.24) to Equation (4.22) and compare the results with that of schemes we mentioned above. We denote $E X p$ and $E X q$ as the exact solution of $p$ and $q$ for system (4.22), and present our results when taking $w = 2$ , $\tau = 0 . 1$ , $p _ { 0 } = 0 . 5$ , $q _ { 0 } = 0 . 5$ in Table 4.1. From Table 4.1, we can see that $T 4 p , T 4 q$ and $E 4 p , E 4 q$ are more approximate to $E X p , E X q$ than $T 2 p , T 2 q$ and $E 2 p , E 2 q$ . Thus, we conclude that scheme (4.1) and (4.2) have a higher order than trapezoid method and centered Euler scheme. Table 4.1 also shows that although the trapezoid scheme (4.1) is non-symplectic, it can be used to solve a Hamiltonian system to get satisfactory results than the centered Euler scheme, by nonlinear transformation; the latter can be obtained from the former, see Section 8.1.

Table 4.1. Numerical comparison between several schemes   

<table><tr><td>StepN</td><td colspan="2">Numerical solution and exact solution</td></tr><tr><td rowspan="3">N=10</td><td>EXp= -1.131156 917 000000 T4p- EXp = 0.000 014 55000</td><td>EXq= -0.021 512 660 000000 T4q- EXq = -0.000 003 728</td></tr><tr><td>E4p- EXp = 0.000 068 24300</td><td>E4q- EXq= -0.000 029 687</td></tr><tr><td>T2p- EXp= 0.000 641 21600 E2p- EXp= 0.000 025 85700</td><td>T2q- EXq= 0.003 917 96400</td></tr><tr><td rowspan="4">N=20</td><td>EXp= -0.578 997 162 000000</td><td>EXq= -0.479 477 967 00000</td></tr><tr><td>T4p-EXp= 0.000 00411500</td><td>T4q- EXq= -0.000002 660</td></tr><tr><td>E4p - EXp= -0.000 116 088</td><td>E4q- EXq= -0.000 029 838</td></tr><tr><td>T2p-EXp= -0.014 158 525 E2p 1 EXp 二 -0.015 197 562</td><td>T2q- EXq= -0.003977 057 E2q EXq 1= -0.004255 307</td></tr><tr><td rowspan="5">N=100</td><td>EXp= -1.083 692 040 00000 T4p- EXp= -0.000 104 873</td><td>EXq= 0.163 258 193 0000000 T4q-EXq= -0.000 195 865</td></tr><tr><td>E4p- EXp= 0.000 145 7860</td><td></td></tr><tr><td></td><td>E4q-EXq = 0.000 131 2730</td></tr><tr><td>T2p-EXp= 0.024 490 7400</td><td>T2q- EXq= 0.036 283 1300</td></tr><tr><td>E2p- EXp= 0.027 254 9000</td><td>E2q- EXq= 0.039 2231760</td></tr><tr><td rowspan="4">N=500</td><td>EXp= -1.089 537 517 000000 T4p- EXp= 0.000 560 51300</td><td>EXq= -0.153 288 801000000 T4q-EXq= -0.001139 354</td></tr><tr><td></td><td></td></tr><tr><td>E4p- EXp= -0.000 250 063</td><td>E4q- EXq= 0.000 559 4940</td></tr><tr><td>T2p-EXp = -0.040 591714 E2p- EXp= -0.037 488 191</td><td>T2q- EXq= 0.188 655 9980</td></tr><tr><td rowspan="4">N= 1000</td><td>EXp= -0.966 531326 000000</td><td>EXq= -0.293 028 275 000000</td></tr><tr><td>T4p- EXp= 0.002 470 90100</td><td>T4q- EXq= 0.002 014 58300</td></tr><tr><td>E4p- EXp= -0.001 281 080</td><td>E4q- EXq = -0.000 988 873</td></tr><tr><td>T2p- EXp= -0.603 588 331 E2p-EXp= ：-0.668 484708</td><td>T2q- EXq= -0.233 974665</td></tr></table>

Example 4.8. Numerical test for stability of schemes (4.1) and (4.2). To consider the unstable case, we take $\lambda = - 1 1 . 8$ , $\tau = 0 . 1$ , and initial value $y _ { 0 } = 1 . 0$ in the test equation, so $\lambda \tau$ falls into the unstable region. While the exact solution decreases quickly, the numerical solution obtained by scheme (4.1) grows to infinity as shown in Table 4.2.

Example 4.9. For the stable case, we consider a linear stiff system

$$
\left\{ \begin{array} { l l } { \dot { y } _ { 1 } = - 5 0 1 y _ { 1 } + 5 0 0 y _ { 2 } , } \\ { \dot { y } _ { 2 } = 5 0 0 y _ { 1 } - 5 0 1 y _ { 2 } , } \end{array} \right.
$$

which has eigenvalues $\lambda _ { 1 } = - 1 0 0 1$ , $\lambda _ { 2 } = - 1$ . The exact solution is


<!-- chunk 0007: pages 421-490 -->
Table 4.2. Stability test   

<table><tr><td>Step number</td><td colspan="2">Numerical and exact solution</td></tr><tr><td>Step1</td><td>0.576776990×101</td><td>0.307278738</td></tr><tr><td>Step10</td><td>0.407404568×108</td><td>0.000007504</td></tr><tr><td>Step50</td><td>0.112235299×1039</td><td>0.000000000</td></tr><tr><td>Step100</td><td>0.816583328×1075</td><td>0.000000000</td></tr></table>

Table 4.3. Test for stiff system   

<table><tr><td>Step N</td><td colspan="2">Numerical solution and exact solution</td></tr><tr><td rowspan="2">N=10</td><td>EXY1= 0.998364638 T4Y1= 0.998453117</td><td>EXY2= 0.991660285 T4Y2= 0.991571619</td></tr><tr><td>T4Y1- EXY1= 0.000088478</td><td>T4Y2- EXY2= -0.000088666</td></tr><tr><td rowspan="2">N=30</td><td>EXY1= 0.985112102 T4Y1= 0.985111988</td><td>EXY2= 0.985111801 T4Y2= 0.985111662</td></tr><tr><td>T4Y1- EXY1= -0.000000114</td><td>T4Y2- EXY2= -0.000000138</td></tr><tr><td rowspan="3">N= 50</td><td>EXY1= 0.975309908</td><td>EXY2= 0.975309908</td></tr><tr><td>T4Y1= 0.975309788</td><td>T4Y2= 0.975309788</td></tr><tr><td>T4Y1- EXY1= -0.000000120</td><td>T4Y2- EXY2= -0.000000120</td></tr><tr><td rowspan="3">N=100</td><td>EXY1= 0.006571583</td><td>EXY2= 0.006571583</td></tr><tr><td>T4Y1= 0.006571770</td><td>T4Y2= 0.006571771</td></tr><tr><td>T4Y1- EXY1= -0.000000186</td><td>T4Y2- EXY2= -0.000000188</td></tr><tr><td rowspan="3">N=200</td><td>EXY1= 0.000000298</td><td>EXY2= 0.000000298</td></tr><tr><td>T4Y1= 0.000000298</td><td>T4Y2= 0.000000298</td></tr><tr><td>T4Y1- EXY1= -0.000000000</td><td>T4Y2- EXY2= -0.000000000</td></tr></table>

$$
\left\{ \begin{array} { l l } { y _ { 1 } ( t ) = f _ { 1 } ( y _ { 1 } , y _ { 2 } ) = 0 . 5 \big ( y _ { 1 } ( 0 ) - y _ { 2 } ( 0 ) \big ) \mathrm { e } ^ { - 1 0 0 1 t } + 0 . 5 \big ( y _ { 1 } ( 0 ) + y _ { 2 } ( 0 ) \big ) \mathrm { e } ^ { - t } , } \\ { y _ { 2 } ( t ) = f _ { 2 } ( y _ { 1 } , y _ { 2 } ) = - 0 . 5 \big ( y _ { 1 } ( 0 ) - y _ { 2 } ( 0 ) \big ) \mathrm { e } ^ { - 1 0 0 1 t } + 0 . 5 \big ( y _ { 1 } ( 0 ) + y _ { 2 } ( 0 ) \big ) \mathrm { e } ^ { - t } . } \end{array} \right.
$$

where $y _ { 1 } ( 0 ) , ~ y _ { 2 } ( 0 )$ denote the initial value. Since system (4.25) is linear, schemes (4.1) and (4.2) are equivalent in this case. We present a numerical solution using scheme (4.1) here. In Table 4.3, we denote the numerical solution of $y _ { 1 }$ and $y _ { 2 }$ using (4.1) by $T 4 Y 1 , T 4 Y 2$ , and the exact solution of $y _ { 1 }$ and $y _ { 2 }$ by $E X Y 1$ and $E X Y 2$ . We also assume $\tau = 0 . 1$ , $y _ { 1 } ( 0 ) = 1 . 5$ , $y _ { 2 } ( 0 ) = 0 . 5$ , in the Table 4.3, while $\tau = 0 . 0 0 0 5$ in the first 50 steps, and $\tau = 0 . 1$ in the remaining steps.

# 8.5 Application of Composition Schemes to PDE

When solving partial differential equations (PDEs), there are several methods such as spectral methods and finite difference methods which can be used to achieve highorder accuracy in the space direction, while it is difficult to obtain high-order accuracy in time direction. So it is obvious that the overall accuracy is often influenced strongly by the relatively unsatisfactory approximation in the time direction. Though the self-adjoint schemes (also called symmetrical schemes or reversible schemes) are well known, such as the composed Strang scheme [Str68] which is of order 2, the advantage of these schemes which can be used to construct higher order schemes is long neglected. In this section, we use scheme (4.1) to solve two kinds of PDEs in order to show that the technique introduced in previous section can be used to overcome the deficiency in the time direction, since theoretically, we can construct arbitrary even order schemes in the time direction[ZQ93b] .

Let us first consider the following one-dimensional first-order wave equation

$$
\left\{ \begin{array} { l l } { u _ { t } + u _ { x } = 0 , } \\ { \ u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq 2 \pi , } \end{array} \right.
$$

with periodic boundary conditions

$$
u ( 0 , t ) = u ( 2 \pi , t ) .
$$

Since collocation, Galerkin, and tau methods are identical in the absence of essential boundary conditions, we will analyze the Fourier collocation or pseudospectral method. Let us introduce the collocation points $x _ { n } = 2 \pi n / 2 N \left( n = 0 , \cdots , 2 N - 1 \right)$ , and let $u = \left( u _ { 0 } , \cdot \cdot \cdot , u _ { 2 N - 1 } \right)$ , where $u _ { n } = u ( x _ { n } , t )$ . The collocation equation that approximates (5.1) is as follows:

$$
\frac { \partial \boldsymbol { u } } { \partial t } = \boldsymbol { C } ^ { - 1 } \boldsymbol { D } \boldsymbol { C } \boldsymbol { u } ,
$$

where $C$ and $D$ are $2 N \times 2 N$ matrices whose entries are

$$
\begin{array} { l } { { c _ { k l } ~ = ~ \displaystyle \frac { 1 } { \sqrt { 2 N } } \exp \big [ ( k - N ) x _ { l } \big ] , } } \\ { { d _ { k l } ~ = ~ - k ^ { * } \delta _ { k l } , } } \end{array}
$$

where $k ^ { * } = k - N$ $1 \leq k \leq 2 N - 1 \rangle$ ), and $k ^ { * } = 0$ , if $k = 0$ . For the process of the discretization, see also literature [GO77] , we leave out the proof in this, but directly quote. To solve this, let us consider Equation (5.1) with initial value $f ( x ) = \sin { x }$ , and compare the numerical solution with the exact solution $\boldsymbol { u } ( \boldsymbol { x } , t ) = \sin { ( \boldsymbol { x } - t ) }$ , we use scheme (4.1) and trapezoid scheme (crank-Nicolson) to solve Equation (5.2) ( $N = 5$ ).

All $u$ values are calculated in the collocation points taking the time step size $\tau = 0 . 1$ and 0.01, and respectively calculating 100 steps with the double precision. $O R D . 4$ and ORD.2, represent results that use (4.1) and the trapezoidal form obtained numerical solution respectively. $E R R . 4$ and $E R R . 2$ represent error between numerical solution $O R D . 4$ and $O R D . 2$ and the exact solution, where the collocation point is $n$ . We list $u ( x , t )$ in each step with values 0, 5, 9 as collocation points. The exact solution is denoted by $E X$ . From Table 5.1 and Table 5.2 we can see that the solution of the 4th order scheme is more precise than the solution of the 2nd order scheme, when $\tau = 0 . 1$ precise 2, when $\tau = 0 . 0 1$ precise 4.

Table 5.1. Comparison between numerical and exact solution when $\tau = 0 . 1$   

<table><tr><td>StepN</td><td>n</td><td>EX</td><td>ORD.4</td><td>ORD.2</td><td>ERR.4</td><td>ERR.2</td></tr><tr><td rowspan="3">N=1</td><td>0</td><td>-0.099833416647</td><td>-0.099832763924</td><td>-0.099750623437</td><td>0.000000652723</td><td>0.000082793209</td></tr><tr><td>5</td><td>0.099833416647</td><td>0.099832763924</td><td>0.099750623438</td><td>-0.000000652723</td><td>-0.000082793209</td></tr><tr><td>9</td><td>-0.665615704994</td><td>-0.66561545443</td><td>-0.665553604585</td><td>0.000000489551</td><td>0.000062100409</td></tr><tr><td rowspan="3">N=10</td><td>0</td><td>-0.841470984808</td><td>-0.841467440655</td><td>-0.841021115481</td><td>0.000003544153</td><td>0.000449869327</td></tr><tr><td>5</td><td>0.841470984808</td><td>0.841467440655</td><td>0.841021115481</td><td>-0.000003544153</td><td>-0.000449869327</td></tr><tr><td>9</td><td>-0.998346054152</td><td>-0.998346431587</td><td>-0.998393545150</td><td>-0.000000377435</td><td>-0.000047490998</td></tr><tr><td rowspan="3">N=100</td><td>0</td><td>0.544021110889</td><td>0.543966068061</td><td>0.537020563223</td><td>-0.000055042829</td><td>-0.007000547666</td></tr><tr><td>5</td><td>-0.544021110889</td><td>-0.543966068061</td><td>-0.537020563223</td><td>0.000055042829</td><td>0.007000547666</td></tr><tr><td>9</td><td>0.933316194418</td><td>0.933292641025</td><td>0.930296266090</td><td>-0.000023553213</td><td>-0.003019928328</td></tr></table>

Table 5.2. Comparison between numerical and exact solution when $\tau = 0 . 0 1$   

<table><tr><td>Step N</td><td>n</td><td>EX</td><td>ORD.4</td><td>ORD.2</td><td>ERR.4</td><td>ERR.2</td></tr><tr><td rowspan="3">N=1</td><td>0</td><td>0.009999833340</td><td>-0.099998333280</td><td>-0.009999750000</td><td>0.000000000007</td><td>0.000000083334</td></tr><tr><td>5</td><td>0.009999833340</td><td>0.009999833280</td><td>0.009999750000</td><td>-0.000000000007</td><td>-0.000000083334</td></tr><tr><td>9</td><td>-0.595845898383</td><td>-0.595845898378</td><td>-0.595845831454</td><td>0.000000000005</td><td>0.000000066929</td></tr><tr><td rowspan="3">N=10</td><td>0</td><td>-0.099833416647</td><td>-0.099833416582</td><td>-0.099832587427</td><td>0.000000000065</td><td>0.000000829220</td></tr><tr><td>5</td><td>0.099833416647</td><td>0.099833416582</td><td>0.099832587427</td><td>0.000000000042</td><td>-0.000000829220</td></tr><tr><td>9</td><td>-0.665615704994</td><td>-0.665615704952</td><td>-0.665615083044</td><td>0.000000000003</td><td>0.000000621950</td></tr><tr><td rowspan="3">N=100</td><td>0</td><td>-0.841470984808</td><td>-0.841470984547</td><td>-0.841466481987</td><td>0.000000000261</td><td>-0.000004502821</td></tr><tr><td>5</td><td>0.841470984808</td><td>0.841470984547</td><td>0.841466481987</td><td>-0.000000000267</td><td>-0.000004502871</td></tr><tr><td>9</td><td>-0.998346054152</td><td>-0.998346054304</td><td>-0.998346533230</td><td>-0.000000000152</td><td>-0.000000479078</td></tr></table>

Similarly, in 2nd order PDE, the result of the 4th order scheme is more precise when compared to the result of the 2nd order scheme in 2 - 4 precision.

Let us take the second order heat conductivity equation

$$
\left\{ \begin{array} { r l l } { \frac { \partial u ( x , t ) } { \partial t } \ = \ \frac { \partial ^ { 2 } u ( x , t ) } { \partial x ^ { 2 } } , } & { 0 < x < \pi , \quad t \geq 0 , } \\ { u ( 0 , t ) \ = \ u ( \pi , t ) = 0 , } & { t > 0 , } \\ { u ( x , 0 ) \ = \ f ( x ) , } & { 0 \leq x \leq \pi . } \end{array} \right.
$$

By applying Fourier sine approach in Equation (5.5), we get

$$
u _ { N } ( x , t ) = \sum _ { n = 1 } ^ { N } a _ { n } ( t ) \sin n x ,
$$

and

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \mathrm { d } a _ { n } } { \mathrm { d } t } = - n ^ { 2 } a _ { n } , } \\ { a _ { n } ( 0 ) = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } f ( x ) \sin { n x } \mathrm { d } x . } \end{array} \right.
$$

Table 5.3. Comparison between numerical and exact solution when $\tau = 0 . 1$   

<table><tr><td>StepN</td><td>n</td><td>EX</td><td>ORD.4</td><td>ORD.2</td><td>ERR.4</td><td>ERR.2</td></tr><tr><td rowspan="3">N=1</td><td>1</td><td>0.531850090044</td><td>0.5318500444815</td><td>0.531805704455</td><td>0.0000003547710</td><td>-0.000044385589</td></tr><tr><td>2</td><td>0.860551522611</td><td>0.8605520966420</td><td>0.860479705219</td><td>0.0000005740310</td><td>-0.000071817391</td></tr><tr><td>3</td><td>0.860551522611</td><td>0.8605520966420</td><td>0.860479705219</td><td>0.0000005740310</td><td>-0.000071817391</td></tr><tr><td rowspan="4">N=10</td><td>4 1</td><td>0.531850090044 0.216234110142</td><td>0.5318504448150 0.2162355525360</td><td>0.531805704455 0.216053719560</td><td>0.0000003547710 0.0000001442394</td><td>-0.000443855890 -0.000180390582</td></tr><tr><td>2</td><td>0.349814139737</td><td>0.3498764735800</td><td>0.349582261644</td><td>0.0000023338430</td><td>-0.000291878093</td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>0.349814139737 0.216234110142</td><td>0.3498764735800 0.2162355522536</td><td>0.349582269644 0.216053719560</td><td>0.0000123338430 0.0000014423940</td><td>-0.000291878093 -0.000180390582</td></tr><tr><td rowspan="4">N=50</td><td>1 2</td><td>0.003960465877</td><td>0.0039605979700</td><td>0.003943973573</td><td>0.0000001320940</td><td>-0.000164923040</td></tr><tr><td></td><td>0.006408168400</td><td>0.0064083821320</td><td>0.006381483292</td><td>0.0000002137320</td><td>-0.000026685108</td></tr><tr><td>3</td><td>0.006408168400</td><td>0.0064083821320</td><td>0.006381483292</td><td>0.0000002137320</td><td>-0.000026685108</td></tr><tr><td>4</td><td>0.003960465877</td><td>0.0039605979700</td><td>0.003943973573</td><td>0.0000001320940</td><td>-0.000164923040</td></tr></table>

The initial value of $a _ { n }$ can be represented in another form. Let $x _ { j } = \frac { \pi j } { N + 1 } \ : \left( j = \right.$ $1 , \cdots , N )$ be collocation points, from collocation equation

$$
\sum _ { n = 1 } ^ { N } a _ { n } \sin \frac { \pi j n } { N + 1 } = u ( x _ { j } ) , \quad j = 1 , \cdots , N ,
$$

we get explicit solution

$$
a _ { n } = \frac { 2 } { N + 1 } \sum _ { j = 1 } ^ { N } u ( x _ { j } ) \sin \frac { \pi j n } { N + 1 } , \quad n = 1 , \cdots , N .
$$

Since $u ( x , 0 ) = f ( x )$ , we get:

$$
a _ { n } ( 0 ) = \frac { 2 } { N + 1 } \sum _ { j = 1 } ^ { N } f ( x _ { j } ) \sin \frac { \pi j n } { N + 1 } , \quad n = 1 , \cdots , N .
$$

The exact solution for Equation (5.5) with boundary condition $f ( x ) \ = \ \sin \ x$ is $\mathrm { e } ^ { - t } \sin { x }$ . In Table 5.3 and Table 5.4, all symbols carry the same significance. We take $N = 4$ for computation.

To solve the semi-discrete spectral approximations

$$
u _ { t } = L _ { N } u ,
$$

of the differential equation

$$
u _ { t } = L u ,
$$

where $L$ denotes the spacial operator, we often use the Crank–Nicolson scheme, backward Euler scheme, and leap-frog scheme. However, we know the backward and forward Euler schemes are not self-adjoint, nor the leap-frog scheme. But the first two schemes are adjoint to each other and the composition is the Crank–Nicolson scheme

Table 5.4. Comparison between numerical and exact solution when $\tau = 0 . 0 1$   

<table><tr><td>Step N</td><td>n</td><td>EX</td><td>ORD.4</td><td>ORD.2</td><td>ERR.4</td><td>ERR.2</td></tr><tr><td rowspan="4">N=1</td><td>1</td><td>0.581936691312</td><td>0.581936691316</td><td>0.581936642817</td><td>-0.000000000004</td><td>-0.000000048495</td></tr><tr><td>2</td><td>0.941593345844</td><td>0.941593345850</td><td>0.941593267377</td><td>0.000000000006</td><td>-0.000000078467</td></tr><tr><td>3</td><td>0.941593345844</td><td>0.941593345850</td><td>0.941593267377</td><td>0.000000000006</td><td>-0.000000078467</td></tr><tr><td>4</td><td>0.581936693120</td><td>0.581936691316</td><td>0.581936642817</td><td>-0.000000000004</td><td>-0.000000048495</td></tr><tr><td rowspan="4">N=100</td><td>1</td><td>0.216234110142</td><td>0.216234110285</td><td>0.216232308172</td><td>0.0000000001430</td><td>-0.000001801970</td></tr><tr><td>2</td><td>0.349874139137</td><td>0.349874139969</td><td>0.349811224088</td><td>0.0000000002310</td><td>-0.000002915049</td></tr><tr><td>3</td><td>0.349874139137</td><td>0.349874139969</td><td>0.349811224088</td><td>0.0000000000231</td><td>-0.000002915049</td></tr><tr><td>4</td><td>0.276234110142</td><td>0.216234110285</td><td>0.216232308172</td><td>0.0000000001430</td><td>-0.000001801970</td></tr></table>

$$
u ^ { n + 1 } - u ^ { n } = \Delta t \frac { 1 } { 2 } \big ( L _ { N } u ^ { n + 1 } + L _ { N } u ^ { n } \big ) .
$$

which is self-adjoint and of order 2. We can construct a fourth-order scheme by composition

$$
\begin{array} { r c l } { { } } & { { } } & { { u ^ { n + 1 / 3 } ~ = ~ u ^ { n } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { 1 / 3 } ) } \Delta t \big ( L _ { N } u ^ { n } + L _ { N } u ^ { n + 1 / 3 } \big ) , } } \\ { { } } & { { } } & { { u ^ { n + 2 / 3 } ~ = ~ u ^ { n + 1 / 3 } - \displaystyle \frac { 2 ^ { 1 / 3 } } { 2 ( 2 - 2 ^ { 1 / 3 } ) } \Delta t \big ( L _ { N } u ^ { n + 1 / 3 } + L _ { N } u ^ { n + 2 / 3 } \big ) , } } \\ { { } } & { { } } & { { u ^ { n + 1 } ~ = ~ u ^ { n + 2 / 3 } + \displaystyle \frac { 1 } { 2 ( 2 - 2 ^ { 1 / 3 } ) } \Delta t \big ( L _ { N } u ^ { n + 2 / 3 } + L _ { N } u ^ { n + 1 } \big ) . } } \end{array}
$$

Finally, we can point out that scheme (5.13) is unstable for some special step size of $t$ . Since the diameter of the unstable region is very small, we can always avoid taking those step-size $\Delta t$ which make $\lambda \Delta t$ ( $\lambda$ denotes the eigenvalue of the system to be solved) fall into the unstable region. Fig. 5.1 shows the solution of the heat equation when we use scheme (5.13) to solve the (5.11) We take $\Delta t = 0 . 0 0 9 7$ and $N = 2 4$ . We can conclude that while the Crank–Nicolson remains stable, the scheme (5.13) does not, and solution tends to overflow. For a Detailed numerical test about this problem, see[ZQ93b] .

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0007_pages_0421-0490/auto/images/fc8757327f0857590fa6f098fc4ea8254ddb5b42b162bdae993a2b185437a7e3.jpg)  
Fig. 5.1. Stability comparison between schemes of Crank–Nicolson (L), (5.13) (M) and exact solution (R) of the heat equation

# 8.6 H-Stability of Hamiltonian System

We know that Hamiltonian system always appears in space of even dimension. A more important fact is that there is no asymptotically stable linear Hamiltonian system. They are either Liapunov stable or unstable, so are the linear symplectic algorithms. Therefore, the usual stability concepts in numerical methods for ODEs are not suitable to symplectic algorithms for Hamiltonian systems, for example, A-stability and $\mathbf { A } ( \alpha )$ stability, $\alpha \leq \frac { \pi } { 2 }$ . Hence, usual $\mathbf { A } ( \alpha )$ stability is useless for $\alpha \leq \frac { \pi } { 2 }$ and A-stability needs to be modified. Here, we introduce a new test system and a new concept-Hstability (Hamiltonian stability) for symplectic algorithms and discuss the H-stability of symplectic invariant algorithms and the H-stability intervals of explicit symplectic algorithms.

For the linear Hamiltonian system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = L z , \quad L = J A \in s p ( 2 n ) , \quad H = ( z , A z ) , A ^ { \mathrm { T } } = A ,
$$

a linear symplectic algorithm

$$
z ^ { k + 1 } = g _ { H } ^ { t } ( z ^ { k } ) = G ( s , A ) z ^ { k } , \quad k \geqslant 0
$$

is stable, if $\exists C > 0$ , such that

$$
\| z ^ { k } \| = \| G ^ { k } ( s , A ) z ^ { 0 } \| \leqslant C \| z ^ { 0 } \| , \quad \forall k > 0 ,
$$

where $\| \bullet \|$ is a well-defined norm, such as Euclidean norm. Evidently, it is equivalent to $\| G ^ { k } ( s ) \|$ bounded, or the eigenvalues of $G ( s )$ are in the unit disk and its elementary divisors corresponding to the eigenvalues on the unit circle are linear. Since $G ( s )$ is symplectic, then

$$
G ^ { - 1 } ( s ) = J ^ { - 1 } G ( s ) ^ { \mathrm { T } } J .
$$

Hence, if $\lambda$ is an eigenvalue of $G ( s )$ , so is $\lambda ^ { - 1 }$ , and they have the same elementary divisors. Therefore, the eigenvalue with the module less than 1 is always accompanied with the eigenvalue with the module great than 1. This implies that the linear symplectic method (6.1) cannot be asymptotically stable. We have:

Theorem 6.1. Linear symplectic method (6.1) is stable iff the eigenvalues of $G ( s )$ are unimodular and their elementary divisors are linear $[ \mathrm { W a n 9 4 } ]$ .

Here, we introduce the test Hamiltonian system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = \alpha J z , \quad \alpha \in \mathbf { R } ,
$$

with

$$
H ( z ) = H ( p , q ) = \frac { \alpha } { 2 } z ^ { \tt T } z = \frac { \alpha } { 2 } ( p ^ { 2 } + q ^ { 2 } ) , \quad A = \alpha I .
$$

Definition 6.2. A symplectic difference method is $_ \mathrm { H }$ -stable at $\mu = \alpha s$ , if it is stable for the test Hamiltonian system (6.2) with the given $\mu$ , such $\mu$ is called a stable point. The maximum interval in which every point is stable and which contains the original point is called the H-stability interval of the method. A symplectic difference method is H-stable if its H-stability interval is the whole real axis. In this case, its numerical solutions are bounded for (6.2) with $\alpha \in \mathbf { R }$ .

Remark 6.3. It is reasonable to choose (6.5) as the model equation because any linear Hamiltonian system may turn into the standard form

$$
H ( p , q ) = { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \alpha _ { i } ( p _ { i } ^ { 2 } + q _ { i } ^ { 2 } ) .
$$

Test Equations (6.2) and (6.1) become

$$
z ^ { k + 1 } = G ( \mu ) z ^ { k } ,
$$

where $G ( \mu )$ is $2 \times 2$ symplectic matrix. If

$$
G ( \mu ) = \left[ \begin{array} { c c } { { a _ { 1 } } } & { { a _ { 2 } } } \\ { { } } & { { } } \\ { { a _ { 3 } } } & { { a _ { 4 } } } \end{array} \right] ,
$$

then det $G ( \mu ) = a _ { 1 } a _ { 4 } - a _ { 2 } a _ { 3 } = 1 .$ . Its characteristic polynomial is

$$
\left| G ( \mu ) - \lambda I \right| = \left| \begin{array} { c c } { { a _ { 1 } - \lambda } } & { { a _ { 2 } } } \\ { { } } & { { } } \\ { { a _ { 3 } } } & { { a _ { 4 } - \lambda } } \end{array} \right| = \lambda ^ { 2 } - ( a _ { 1 } + a _ { 4 } ) \lambda + 1 .
$$

So, its eigenvalues are

$$
\lambda _ { \pm } = \frac { a _ { 1 } + a _ { 4 } } { 2 } \pm \sqrt { { \left( \frac { a _ { 1 } + a _ { 4 } } { 2 } \right) } ^ { 2 } - 1 } .
$$

Lemma 6.4. Scheme (6.6) is stable at $\mu \neq 0 ,$ , iff

$$
\Bigl ( \frac { a _ { 1 } + a _ { 4 } } { 2 } \Bigr ) ^ { 2 } < 1 , \quad i . e . , - 1 < \frac { a _ { 1 } + a _ { 4 } } { 2 } < 1 .
$$

Example 6.5. Applying the centered Euler scheme to the test system (6.5), it becomes

$$
\begin{array} { l } { { \displaystyle \widehat { z } = z + \frac { 1 } { 2 } \mu J ( \widehat { z } + z ) , \quad \mu = \alpha s , } } \\ { { \displaystyle \widehat { z } = \left( I + \frac { 1 } { 2 } \mu J \right) ^ { - 1 } \left( I - \frac { 1 } { 2 } \mu J \right) z , } } \end{array}
$$

where

$$
G ( \mu ) = \frac { 1 } { 1 + \frac { 1 } { 4 } \mu ^ { 2 } } \left[ \begin{array} { c c } { { 1 - \frac { 1 } { 4 } \mu ^ { 2 } } } & { { - \mu } } \\ { { \mu } } & { { 1 - \frac { 1 } { 4 } \mu ^ { 2 } } } \end{array} \right] ,
$$

therefore

$$
\left( { \frac { a _ { 1 } + a _ { 4 } } { 2 } } \right) ^ { 2 } = \left( { \frac { 1 - { \frac { 1 } { 4 } } \mu ^ { 2 } } { 1 + { \frac { 1 } { 4 } } \mu ^ { 2 } } } \right) < 1 , \forall \mu \neq 0 .
$$

By Lemma 6.4, we know that the centered Euler scheme to all $\mu \neq 0$ is stable, certainly it is also stable for $\mu = 0$ , therefore, the centered Euler scheme is $_ \mathrm { H }$ -stable.

For the stability region of certain explicit scheme, see the literature $[ \mathrm { W a n 9 4 } , \mathrm { Q Z 9 0 } ]$ .

In Section 8.2, we have constructed schemes of difference from 1st order to 4th order. We will now discusses its stability by applying these schemes to the model Equation (6.5), we get

$$
z ^ { k + 1 } = G _ { i } ( \mu ) z ^ { k } , \mu = \alpha s , i = 1 , 2 , 3 , 4
$$

$G _ { i }$ is the step transition equation.

$$
\begin{array} { r l } & { G _ { \cdot } ( \theta ) = \left( \begin{array} { l l } { 1 } & { - \rho } \\ { \mu } & { 1 - \mu ^ { 2 } } \end{array} \right) , } \\ & { G _ { \cdot } ( \theta ) = \left( \begin{array} { l l } { 1 - \frac { 1 } { 2 } \mu ^ { \prime \prime } } & { - \beta } \\ { \mu \left( 1 - \frac { 1 } { 3 } \mu ^ { 2 } \right) } & { 1 - \frac { 1 } { 2 } \mu ^ { \prime \prime } } \end{array} \right) , } \\ & { G _ { \cdot } ( \theta ) = \left( \begin{array} { l l } { 1 - \frac { 1 } { 2 } \mu ^ { 2 } } & { 1 - \frac { 1 } { 3 } \mu ^ { 2 } } \\ { \mu \left( 1 - \frac { 1 } { 3 } \mu ^ { 2 } + \frac { 1 } { 2 } \mu ^ { 3 } \right) } & { - \mu \left( 1 - \frac { 1 } { 3 } \mu ^ { 2 } + \frac { 1 } { 1 2 8 } \mu ^ { 4 } \right) } \\ { \mu \left( 1 - \frac { 1 } { 6 } \mu ^ { 2 } + \frac { 1 } { 2 } \mu ^ { 4 } \right) } & { 1 - \frac { 1 } { 2 } \mu ^ { 2 } + \frac { 5 } { 2 } \mu ^ { 4 } - \frac { 7 } { 1 2 8 } \mu ^ { 4 } } \end{array} \right) , } \\ & { G _ { \cdot } ( \theta ) = \left( \begin{array} { l l } { \alpha _ { 1 } } & { \alpha _ { 2 } } \\ { \alpha _ { 3 } } & { \alpha _ { 3 } } \end{array} \right) , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$$$
\begin{array} { r l } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \ \end{array}
$$

Theorem 6.6. From the explicit scheme above, the H-stability intervals are $( - 2 , 2 )$ , $( - 2 , 2 )$ , (−2.507, 2.507) and (−1.573, 1.573).

Proof. Proof of this theorem can be found in paper of Daoliu $\mathrm { W a n g ^ { [ W a n 9 4 ] } }$ and paper of Mengzhao Qin and Meiqing Zhang[QZ90] . -

# Bibliography

[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin, Second edition, (1989).   
[Dah75] G. Dahlquist: Error analysis for a class of methods for stiff nonlinear initial value problems. In G.A. Watson, editor, Lecture Notes in Mathematics, Vol. 506, Numerical Analysis, Dundee, pages 60–74. Springer, Berlin, (1975).   
[DF76] A. J. Dragt and J. M. Finn: Lie series and invariant functions for analytic symplectic maps. J. of Math. Phys., 17:2215–2227, (1976).   
[DF83] A.J. Dragt and E. Forest: Computation of nonlinear behavior of Hamiltonian systems using Lie algebraic methods. J. of Math. Phys., 24(12):2734–2744, (1983).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen86] K. Feng: Difference schemes for Hamiltonian formalism and symplectic geometry. J. Comput. Math., 4:279–289, (1986).   
[Fen91] K. Feng: The Hamiltonian Way for Computing Hamiltonian Dynamics. In R. Spigler, editor, Applied and industrial Mathmatics, pages 17–35. Kluwer, The Netherlands, (1991).   
[Fen92] K. Feng: Formal power series and numerical methods for differential equations. In T. Chan and Z.C. Shi, editors, International conf. on scientific computation, pages 28–35. World Scientific, Singapore, (1992).   
[For92] E. Forest: Sixth-order Lie group integrators. J. of Comp. Phys., 99:209–213, 1992.   
[For06] E. Forest. Geometric integration for particle accelerators. J. Phys. A: Math. Gen., 39:5321–5377, (2006).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FR90] E. Forest and R. D. Ruth: Fourth-order symplectic integration. Physica D, 43:105–117, (1990).   
[GO77] D. Gottlib and A. Orsag: Numerical Analysis of Spectral Methods, Theory and Application. SIAM, Philadelphia, (1977).   
[HNW93] E. Hairer, S. P. Nørsett, and G. Wanner: Solving Ordinary Differential Equations I, Nonstiff Problems. Springer-Verlag, Berlin, Second revised edition, (1993).   
[McL95a] R. I. McLachlan: Comment on “ Poisson schemes for Hamiltonian systems on Poisson manifolds”. Computers Math. Applic., 29:1, (1995).   
[McL95b] R. I. McLachlan: Composition methods in the presence of small parameters. BIT, 35:258–268, (1995).   
[McL95c] R. I. McLachlan: On the numerical integration of ODE’s by symmetric composition methods. SIAM J. Numer. Anal., 16:151–168, (1995).   
[McL95d] R. I. McLachlan: On the numerical integration of ordinary differential equations by symmetric composition methods. SIAM J. Sci. Comput., 16:151–168, (1995).   
[MSS99] A. Murua and J. M. Sanz-Serna: Order conditions for numerical integrators obtained by composing simpler integrators. Phil. Trans. Royal Soc. A, 357:1079–1100, (1999).   
[MSSS97] A. Murua, J. M. Sanz-Serna, and R. D. Skeel: Order conditions for numerical integrators obtained by composing simpler methods. Technical Report 1997/7, Departemento de Matematica Aplicada y Computati ´ on, Universidad de Valladolid, Spain, (1997). ´   
[Mur97] A. Murua: On order conditions for partitioned symplectic methods. SIAM J. Numer. Anal., 34:2204–2211, (1997).   
[Mur99] A. Murua: Formal series and numerical integrators, part I: Systems of ODEs and symplectic integrators. Appl. Numer. Math., 29:221–251, (1999).   
[Mur06] A. Murua: The Hopf algebra of rooted trees, free Lie argebra,and Lie series. Foundations of Computational Mathematics, 6(4):387–426, (2006).   
[Ner87] F. Neri: Lie algebras and canonical integration. University of Maryland Tech. report, (1987).   
[QWZ91] M. Z. Qin, D. L. Wang, and M. Q. Zhang: Explicit symplectic difference schemes for separable Hamiltonian systems. J. Comput. Math., 9(3):211–221, (1991).   
[QZ90] M. Z. Qin and M. Q. Zhang: Multi-stage symplectic schemes of two kinds of Hamiltonian systems for wave equations. Computers Math. Applic., 19:51–62, (1990).   
[QZ90a] M. Z. Qin and M. Q. Zhang: Explicit Runge–Kutta–like schemes to solve certain quantum operator equations of motion. J. Stat. Phys., 60(5/6):839–843, (1990).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[QZ93] M. Z. Qin and W. J. Zhu: A note on stability of three stage difference schemes for ODEs. Computers Math. Applic., 25:35–44, (1993).   
[QZZ95] M. Z. Qin, W. J. Zhu, and M. Q. Zhang: Construction of symplectic of a three stage difference scheme for ODEs. J. Comput. Math., 13:206–210, (1995).   
[Rut83] R. Ruth: A canonical integration technique. IEEE Trans. Nucl. Sci., 30:26–69, (1983).   
[Ste84] S. Steinberg: Lie series and nonlinear ordinary equations. J. of Math. Anal. and Appl., 101:39–63, (1984).   
[Str68] G. Strang: On the construction and comparison of difference schemes. SIAM J. Numer. Anal., 5:506–517, (1968).   
[Suz77] M. Suzuki: On the convergence of exponential operators the zassenhuas formula, BCH formula and systematic approximants. Communications in Mathematical Physics, 57:193–200, (1977).   
[Suz90] M. Suzuki: Fractal decomposition of exponential operators with applications to manybody theories and Monte Carlo simulations. Physics Letters A, 146:319–323, (1990).   
[Suz92] M. Suzuki: General theory of higher-order decomposition of exponential operators and symplectic integrators. Physics Letters A, 165:387–395, (1992).   
[Wan94] D. L. Wang: Some acpects of Hamiltonian systems and symplectic defference methods. Physica D, 73:1–16, (1994).   
[Wru96] O. Wrubel: Qin-Kompositionen mit Lie-Reihen. Diplomarbeit Uni Karlsruhe (TH), (1996).   
[Yos90] H. Yoshida: Construction of higher order symplectic integrators. Physics Letters A, 150:262–268, (1990).   
[ZQ93] W. Zhu and M. Qin: Applicatin of higer order self-adjoint schemes of PDEs. Computers Math. Applic., 26(3):15–26, 1993.
