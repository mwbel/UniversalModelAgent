with $\omega _ { s } d \ll c$ ，On the other hand,the energy-momentum tensor is non-vanishing only inside the source,so the integral in eq.(3.26) is restricted to $| { \bf x } ^ { \prime } | \leqslant d$ Thenthedominantcontributionto $h _ { i j } ^ { \mathrm { T T } }$ comes from frequencies $\omega$ that satisfy

$$
\frac { \omega } { c } { \bf x } ^ { \prime } | \cdot \hat { { \bf n } } \lesssim \frac { \omega _ { s } d } { c } \ll 1 ,
$$

and therefore we can expand the exponentialin eq. (3.27),

$$
\begin{array} { l } { { \displaystyle e ^ { - i \omega ( t - r / c + { \bf x } ^ { \prime } \cdot \hat { \bf n } / c ) } = e ^ { - i \omega ( t - \eta / c ) } \qquad \quad ( 3 . 2 } } \\ { { \displaystyle \qquad \times \left[ 1 - i \frac { \omega } { c } { x ^ { \prime } } ^ { i } n ^ { i } + \frac { 1 } { 2 } \left( - i \frac { \omega } { c } \right) ^ { 2 } x ^ { \prime } { x ^ { \prime } } ^ { j } n ^ { i } n ^ { j } + . . . \right] . } } \end{array}
$$

This is equivalent to expanding

$$
\begin{array} { l } { { \displaystyle T _ { k l } \left( t - \frac { r } { c } + \frac { { \bf x } ^ { \prime } \cdot \hat { \bf n } } { c } , { \bf x } ^ { \prime } \right) \simeq T _ { k l } ( t - \frac { r } { c } , { \bf x } ^ { \prime } ) } \ ~ ( 3 . 3 0 ) } \ ~  \\ { { \displaystyle ~ + \frac { { \bf x } ^ { \prime } { } ^ { i } n ^ { i } } { c } \partial _ { 0 } T _ { k l } + \frac { 1 } { 2 c ^ { 2 } } x ^ { \prime } { } ^ { i } x ^ { \prime } { } ^ { j } n ^ { i } n ^ { j } \partial _ { 0 } ^ { 2 } T _ { k l } + \dots { } . } } \end{array}
$$

10One could have directly writen the expansion (3.30)，as a formal Taylor expansion in the parameter $\mathbf { x } ^ { \prime } \cdot \hat { \mathbf { n } } / c$ However,the above derivation emphasizes that the assumption behind this expansion is the condition $\omega _ { s } d \ll c _ { \mathrm { ~ ~ } }$ with $\omega _ { s }$ the typical source frequency.

where all derivatives are evaluated at the point $( t - r / c , \mathbf { x } ^ { \prime } )$ .10 We now define the momenta of the stress tensor $T ^ { i j }$ ，

$$
\begin{array} { c } { { S ^ { i j } ( t ) = \displaystyle \int d ^ { 3 } x T ^ { i j } ( t , { \bf x } ) , } } \\ { { S ^ { i j , k } ( t ) = \displaystyle \int d ^ { 3 } x T ^ { i j } ( t , { \bf x } ) x ^ { k } , } } \\ { { S ^ { i j , k l } ( t ) = \displaystyle \int d ^ { 3 } x T ^ { i j } ( t , { \bf x } ) x ^ { k } x ^ { l } , } } \end{array}
$$

11Observe that,contrary to most of the literature on general relativity,we never use commas to denote derivatives (nor semicolons to denote covariant derivatives).

and similarly for all higher order momenta. In this notation,a comma separates the spatial indices which originates from $T ^ { i j }$ from the indices coming from $\boldsymbol { x } ^ { i _ { 1 } } \ldots \boldsymbol { x } ^ { i _ { N } }$ .11 The energy-momentum tensor of matter that appears in eq.(3.3)is the one pbtained from the variation of the matter action with respect to the metric,so it is in its symmetric form, $T ^ { i j } =$ $T ^ { j i }$ Then,its momenta are symmetric separately in the first type of indices and in the second,e.g. $S ^ { i j , k } = S ^ { j i , k }$ or $S ^ { i j , k l } = S ^ { i j , l k }$ but not necessarily under the exchange of two indices of different type,e.g. in general $S ^ { i j , k } \ne S ^ { i k , j }$

Inserting the expansion (3.30)into eq. (3.26) we get where the subscript “ret”means that the quantities $S ^ { k l } , \dot { S } ^ { k l , m } , \ddot { S } ^ { k l , m p }$ , etc.are evaluated at retarded time $t - r / c$ .This equation is the basis for the multipole expansion. From the definitions (3.31)-(3.32) we see that, with respect to $S ^ { k l }$ ， $S ^ { k l , m }$ has an additional factor $x ^ { m } \sim O ( d )$ , while each time derivative brings a factor $O ( \omega _ { s } )$ .So, with respect to $S ^ { k l }$ ,the tensor $\dot { S } ^ { k l , m }$ has an aditional factor $O ( \omega _ { s } d )$ ,i.e. $O ( v )$ ，where $v$ is a typical velocity inside the source. Then the term $( 1 / c ) n _ { m } \dot { S } ^ { k l , m }$ is a correction $O ( v / c )$ to the term $S ^ { k l }$ ,and similarly the term $( 1 / c ^ { 2 } ) n _ { m } n _ { p } \ddot { S } ^ { k l , m p }$ isa correction $O ( v ^ { 2 } / c ^ { 2 } )$ ,etc.

<table><tr><td>14G hTT T(t,x)= Aij,1(n） r C shl 1 × + 二 + C</td><td>1 2c2 ， Jret</td></tr></table>

The physical meaning of the various terms in this expansion becomes more clear if we eliminate the momenta of $T ^ { i j }$ in favor of the momenta of the energy density $T ^ { 0 0 }$ ,and of the momenta of the linear momentum, $T ^ { 0 i } / c$ We define the momenta of $T ^ { 0 0 } / c ^ { 2 }$ by12

$$
\begin{array} { c } { { { \displaystyle M = \frac { 1 } { c ^ { 2 } } \int d ^ { 3 } x ~ { \cal T } ^ { 0 0 } \big ( t , { \bf x } \big ) , } } } \\ { { { } } } \\ { { { \displaystyle M ^ { i } = \frac { 1 } { c ^ { 2 } } \int d ^ { 3 } x ~ { \cal T } ^ { 0 0 } \big ( t , { \bf x } \big ) x ^ { i } , } } } \\ { { { } } } \\ { { { \displaystyle M ^ { i j } = \frac { 1 } { c ^ { 2 } } \int d ^ { 3 } x ~ { \cal T } ^ { 0 0 } \big ( t , { \bf x } \big ) x ^ { i } x ^ { j } , } } } \\ { { { } } } \\ { { { \displaystyle M ^ { i j k } = \frac { 1 } { c ^ { 2 } } \int d ^ { 3 } x ~ { \cal T } ^ { 0 0 } \big ( t , { \bf x } \big ) x ^ { i } x ^ { j } x ^ { k } , } } } \end{array}
$$

ind so on,while the momenta of the momentum density $( 1 / c ) T ^ { 0 i }$ are denoted by

$$
\begin{array} { c } { { P ^ { i } = \displaystyle \frac { 1 } { c } \int d ^ { 3 } x ~ { \cal T } ^ { 0 i } ( t , { \bf x } ) , } } \\ { { { } } } \\ { { P ^ { i , j } = \displaystyle \frac { 1 } { c } \int d ^ { 3 } x ~ { \cal T } ^ { 0 i } ( t , { \bf x } ) ~ x ^ { j } ~ , } } \\ { { { } } } \\ { { P ^ { i , j k } = \displaystyle \frac { 1 } { c } \int d ^ { 3 } x ~ { \cal T } ^ { 0 i } ( t , { \bf x } ) ~ x ^ { j } x ^ { k } ~ , } } \end{array}
$$

And similarly for the higher momenta.|The time derivatives of these quantities and of the momenta of $T ^ { i j }$ satisfy relations which follow from mergy-momentum conservation.Recall that we are working within linrarized theory,which means that the energy-momentum tensor of matter $T ^ { \mu \nu }$ satisfies the flat-space equation $\partial _ { \mu } T ^ { \mu \nu } = 0$ ,as we have seen in 4. (1.25)，while non-linearities such as those written schematically in q (2.113) are neglected. This means that we are also neglecting the back-action of the GWs on the source.13

To obtain these identities,we take a box of volume $V$ larger than the source,and we denote its boundary by $\partial V$ (so $T _ { \mu \nu }$ vanishes on $\partial V$ ). Using $\partial _ { \mu } T ^ { \mu , 0 } = 0$ ,that is

$$
\partial _ { 0 } T ^ { 0 0 } = - \partial _ { i } T ^ { 0 i } ,
$$

nd recalling that $\dot { M } \equiv \partial M / \partial t = c \partial _ { 0 } M ,$ we have

$$
\begin{array} { c } { { \displaystyle { c \dot { M } = \int _ { V } d ^ { 3 } x \partial _ { 0 } T ^ { 0 0 } } } } \\ { { \displaystyle { \phantom { \bigg [ } } } } \\ { { \displaystyle { \phantom { \bigg [ } } = - \int _ { V } d ^ { 3 } x \partial _ { i } T ^ { 0 i } } } \end{array}
$$

12 Dimensionally $T ^ { 0 0 } / c ^ { 2 }$ is a mass density but of course,besides the contribution due to the rest mass of the source，it contains also all contributionsto $T ^ { 0 0 }$ coming from the kinetic energy of the particles which make up the source,contributions from the potential energy,etc.For sources that generate a strong gravitational field,such as neutron stars,the gravitational binding energy will also be important.Only for weak-field sources and in the nonrelativistic limit, $T ^ { 0 0 } / c ^ { 2 }$ becomes the mass density. However,since the multipole expansion of the linearized theory assumes weak fields and is a nonrelativistic expansion,to lowest order in $v / c$ we can actually replace $T ^ { 0 0 } / c ^ { 2 }$ with the mass density.

$^ { 1 3 } \mathrm { T h e }$ inclusionofthesenon-liearities will be discussed in Chapter 5.

The last equality follows from thefact that $T ^ { 0 i }$ vanishes on the boundary $\partial V$ , since we have taken the volume $V$ larger than the volume of the source.Of course,a physical system that radiates GWs loses mass. The conservation of the mass $M$ of the radiating body，expressed by eq.(3.43),is due to the fact that in the linearized approximation the back action of the source dynamics duetothe energycarried away by the GWs is neglected.Similarly,we obtain the identity

$$
\begin{array} { l } { { { \scriptstyle c \dot { M } ^ { i } = \displaystyle \int _ { V } d ^ { 3 } x x ^ { i } \partial _ { 0 } T ^ { 0 0 } } } } \\ { { { \scriptstyle = - \displaystyle \int _ { V } d ^ { 3 } x x ^ { i } \partial _ { j } T ^ { 0 j } } } } \\ { { { \scriptstyle = \displaystyle \int _ { V } d ^ { 3 } x ( \partial _ { j } x ^ { i } ) T ^ { 0 j } } } } \\ { { { \scriptstyle = \displaystyle \int _ { V } d ^ { 3 } x \delta _ { j } ^ { i } T ^ { 0 j } } } } \\ { { { \scriptstyle = \displaystyle \int _ { 0 } e ^ { i } } } } \end{array}
$$

In the same way one derives similar identities for the higher momenta of $T ^ { 0 0 }$ and of $T ^ { 0 i }$ .For the first few lowest-order momenta of $T ^ { 0 0 }$ we get

$$
\begin{array} { r c l } { { } } & { { } } & { { \dot { M } = 0 \sp [ \nonumber ) } } \\ { { } } & { { } } & { { \dot { M } \sp { i } = P \sp { i } ~ , } } \\ { { } } & { { } } & { { \dot { M } \sp { i j } = P \sp { i , j } + P \sp { j , i } ~ , } } \\ { { } } & { { } } & { { \dot { M } \sp { i j k } = P \sp { i , j k } + P \sp { j , k i } + P \sp { k , i j } ~ , } } \end{array}
$$

while the lowest-order momenta of $T ^ { 0 i }$ satisfy

$$
\begin{array} { r c l } { { } } & { { } } & { { \left. \dot { P } ^ { i } \right| = 0 , } } \\ { { } } & { { } } & { { \left. \dot { P } ^ { i , j } \right| = S ^ { i j } , } } \\ { { } } & { { } } & { { \left. \dot { P } ^ { i , j k } \right| = S ^ { i j , k } + S ^ { i k , j } . } } \end{array}
$$

$^ { 1 4 } \mathrm { { I n } }$ particular， the momenta of $T ^ { i j }$ ， i.e. $\{ S ^ { i j } , S ^ { i j , k } , \ldots \}$ depend on the distribution of the stresses inside the body, which might be difficult to determine, while the total mass of a body,its mass quadrupole,etc.can be measured more easily.

The equations $\dot { M } = 0$ and $\dot { P } ^ { i } \equiv 0$ are the conservation of the mass and of the total momentum of the source.Another interesting identity is ${ \dot { P } } ^ { i , j } - { \dot { P } } ^ { j , i } = S ^ { i j } - S ^ { j i } = 0$ ,which follows from eq.(3.50)using the fact that $S ^ { i j }$ is a symmetric tensor,and is the conservation of the angular momentum of the source.

We can now combine these identities to express the momenta $S ^ { i j }$ , $\Dot { S } ^ { i j , k }$ ,etc., thatappear in the multipoleexpansion,in terms of the two sets of momenta $\{ M , M ^ { i } , M ^ { i j } , . . . \}$ and $\{ P ^ { i } , P ^ { i , j } , \ldots \}$ ，which have a more immediate physical interpretation.14 Taking the time derivative of eq. (3.47) and using eq. (3.5O),as well as the fact that $S ^ { i j } = S ^ { j i }$ ,we obtain the identity

<table><tr><td>gij</td><td>1 MU</td></tr><tr><td></td><td></td></tr></table>

If we combine eq. (3.48) with eq. (3.51) instead, we get

$$
\ddot { \boldsymbol { M } } ^ { i j k } = 2 ( \dot { S } ^ { i j , k } + \dot { S } ^ { i k , j } + \dot { S } ^ { j k , i } ) .
$$

From eq. (3.51) it also follows that $\ddot { P } ^ { i , j k } = \dot { S } ^ { i j , k } + \dot { S } ^ { i k , j }$ Using this relation and eq. (3.53) we can verify that

$$
\overbrace  { \dot { S } } ^ { i j , k } = { \frac { 1 } { 6 } } { \ddot { M } } ^ { i j k } + { \frac { 1 } { 3 } } \left( { \ddot { P } } ^ { i , j k } + { \ddot { P } } ^ { j , i k } - 2 { \ddot { P } } ^ { k , i j } \right) .
$$

Equations (3.52) and (3.54) relate $S ^ { i j }$ and $\Dot { S } ^ { i j , k }$ ，which are the two lowest-order momenta appearing in the multipole expansion (3.34)，to the momenta of $T ^ { 0 0 }$ and of $T ^ { 0 i }$ .One can proceed similarly with the higher-order terms. In the next two sections,we examine the leading and the next-to-leading terms,while in Section 3.5 we discuss systematically the expansion to all orders.

# 3.3 Mass quadrupole radiation

# 3.3.1Amplitude and angular|distribution

Using eq. (3.52),the leading term of the expansion (3.34) is

$$
\left[ h _ { i j } ^ { \mathrm { T T } } ( t , \mathbf { x } ) \right] _ { \mathrm { q u a d } } = \frac { 1 } { r } \frac { 2 G } { c ^ { 4 } } \Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) \ddot { M } ^ { k l } ( t - r / c ) .
$$

From the point of view of the rotation group the tensor $M _ { k l }$ ，asany symmetric tensor with two indices,decomposes into irreducible representations as

$$
M ^ { k l } = \biggl ( M ^ { k l } - \frac 1 3 \delta ^ { k l } M _ { i i } \biggr ) + \frac 1 3 \delta ^ { k l } M _ { i i } ,
$$

where $M _ { i i }$ is the trace of $M _ { i j }$ . The first tetm is traceless by construction, and is a pure spin-2 operator,while the trace part is a scalar. Since the Lambda tensor $\Lambda _ { i j , k l }$ gives zero when contracted with $\delta _ { k l }$ ,only the traceless term contributes. We use the notation

$$
\rho = { \frac { 1 } { c ^ { 2 } } } T ^ { 0 0 } .
$$

To lowest order in $v / c , \rho$ becomes the mass density,see Note 12.We also introduce the quadrupole moment

$$
\begin{array} { l } { { \displaystyle Q ^ { i j } \equiv M ^ { i j } - \frac { 1 } { 3 } \delta ^ { i j } M _ { k k } } } \\ { { \displaystyle ~ = \int d ^ { 3 } x \rho ( t , { \bf x } ) ( x ^ { i } x ^ { j } - \frac { 1 } { 3 } r ^ { 2 } \delta ^ { i j } ) , } } \end{array}
$$

nd eq.(3.55） becomes

$$
\begin{array} { l } { \displaystyle \left[ h _ { i j } ^ { \mathrm { T T } } ( t , \mathbf { x } ) \right] _ { \mathrm { q u a d } } = \frac { 1 } { r } \frac { 2 G } { c ^ { 4 } } \Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) \ddot { Q } _ { k l } ( t - r / c ) } \\ { \displaystyle \equiv \frac { 1 } { r } \frac { 2 G } { c ^ { 4 } } \ddot { Q } _ { i j } ^ { \mathrm { T T } } ( t - r / c ) . } \end{array}
$$

Angular distribution of quadrupole radiation

In order to obtain the waveform emitted into an arbitrary direction n we could in principle plug the explicit expression (1.39) of the Lambda tensor into eq.(3.59),and perform the contraction with $\ddot { Q } _ { k l }$ . It is however more instructive to proceed as follows.First we observe that,when the direction of propagation $\hat { \bf n }$ of the GW is equal to $\hat { \mathbf { z } }$ ， $P _ { i j }$ is the diagonal matrix diag $( 1 , 1 , 0 )$ ，i.e. $P _ { i j }$ is a projector on the $( x , y )$ plane. Writing $\Lambda _ { i j , k l }$ in terms of $P _ { i j }$ using eq. (1.36) we have, for an arbitrary $3 \times 3$ matrix $A _ { k l }$ ，

$$
\begin{array} { r l } {  { \Lambda _ { i j , k l } A _ { k l } = \bigg [ P _ { i k } P _ { j l } - \frac { 1 } { 2 } P _ { i j } P _ { k l } \bigg ] A _ { k l } } } \\ & { = ( P A P ) _ { i j } - \frac { 1 } { 2 } P _ { i j } \mathrm { T r } ( P A ) . } \end{array}
$$

When $P$ has the form

$$
P = \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

we get

$$
P A P = \left( \begin{array} { c c c } { { A _ { 1 1 } } } & { { A _ { 1 2 } } } & { { 0 } } \\ { { A _ { 2 1 } } } & { { A _ { 2 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ~ ,
$$

while $\mathrm { T r } \left( P A \right) = A _ { 1 1 } + A _ { 2 2 }$ Therefore

$$
\begin{array} { c } { { \Lambda _ { i j , k l } A _ { k l } = \left( \begin{array} { c c c } { { A _ { 1 1 } } } & { { A _ { 1 2 } } } \\ { { A _ { 2 1 } } } & { { A _ { 2 2 } } } \\ { { 0 } } & { { 0 } } \end{array} \right) _ { i j } - \frac { A _ { 1 1 } + A _ { 2 2 } } 2 \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { i j } } } \\ { { = \left( \begin{array} { c c c } { { ( A _ { 1 1 } - A _ { 2 2 } ) / 2 } } & { { A _ { 1 2 } } } & { { 0 } } \\ { { A _ { 2 1 } } } & { { - ( A _ { 1 1 } - A _ { 2 2 } ) / 2 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { i j } . \qquad ( \sharp ) } } \end{array}
$$

$^ { 1 5 } \mathrm { W e }$ write the result in terms of the second mass moment $M _ { i j }$ ,rather than in terms of the quadrupole moment $Q _ { i j }$ Since $\Lambda _ { i j , k l } Q _ { k l } = \Lambda _ { i j , k l } M _ { k l }$ (because $\Lambda _ { i j , k l } \delta _ { k l } = 0$ ,see eq.(1.38))，in the equations below we could use $M _ { i j }$ or $Q _ { i j }$ equivalently.Typically，it is slightly more practical to use $M _ { i j }$ when one makes explicit computations.

Thus,when $\hat { \bf n } = \hat { \bf z }$ 15

$$
\Lambda _ { i j , k l } \ddot { M } _ { k l } = \left( \begin{array} { c c c } { { ( \ddot { M } _ { 1 1 } - \ddot { M } _ { 2 2 } ) / 2 } } & { { \ddot { M } _ { 1 2 } } } & { { 0 } } \\ { { \ddot { M } _ { 2 1 } } } & { { - ( \ddot { M } _ { 1 1 } - \ddot { M } _ { 2 2 } ) / 2 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { i j } .
$$

From this we directly read the two polarization amplitudes,for a GW propagating in the $z$ direction,

$$
\begin{array} { l } { { \displaystyle h _ { + } = \frac { 1 } { r } \frac { G } { c ^ { 4 } } \left( \ddot { M } _ { 1 1 } - \ddot { M } _ { 2 2 } \right) , } } \\ { { \displaystyle h _ { \times } = \frac { 2 } { r } \frac { G } { c ^ { 4 } } \ddot { M } _ { 1 2 } , } } \end{array}
$$

where it is understood that the right-hand side is computed at the re tarded time $t - r / c$ .To compute the amplitudes for a wave that,in a frame with axes $( x , y , z )$ ，propagates in a generic direction $\hat { \bf n }$ ,weintroduce two unit vectors $\hat { \bf u }$ and $\hat { \mathbf { v } }$ ，orthogonal to $\hat { \bf n }$ and to each other, chosen so that $\hat { \mathbf { u } } \times \hat { \mathbf { v } } = \hat { \mathbf { n } }$ (so,when $\hat { \textbf { n } } = \hat { \textbf { z } }$ ，we can take $\hat { \textbf { u } } = \hat { \textbf { x } }$ and $\hat { \mathbf { v } } = \hat { \mathbf { y } }$ ),see Fig.3.2.Then in the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame,whose axes are in the directions $( \hat { \mathbf { u } } , \hat { \mathbf { v } } , \hat { \mathbf { n } } )$ ,the wave propagates along the $z ^ { \prime }$ axis and we can use the previous result to read $h _ { + }$ and $h _ { \times }$ ，

$$
\begin{array} { l } { { \displaystyle h _ { + } ( t , { \hat { \mathbf { n } } } ) = \frac { 1 } { r } \frac { G } { c ^ { 4 } } ( { \ddot { M } } _ { 1 1 } ^ { \prime } - { \ddot { M } } _ { 2 2 } ^ { \prime } ) , } } \\ { { \displaystyle h _ { \times } ( t , { \hat { \mathbf { n } } } ) = \frac { 2 } { r } \frac { G } { c ^ { 4 } } { \ddot { M } } _ { 1 2 } ^ { \prime } } , } \end{array}
$$

where $M _ { i j } ^ { \prime }$ ,are the components of the second mass moment in the frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ 16 Thesecan be related tothe components $M _ { i j }$ in the $( x , y , z )$ frame observing that in the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame the vector $\hat { \bf n }$ has coordinates $n _ { i } ^ { \prime } = \left( 0 , 0 , 1 \right)$ ，while in the $( x , y , z )$ frame it has coordinates

$$
n _ { i } = \left( \sin \theta \sin \phi , \sin \theta \cos \phi , \cos \theta \right) ,
$$

Then the components $n _ { i }$ and $n _ { i } ^ { \prime }$ are related by a rotation matrix $\mathcal { R }$ such that $n _ { i } = \mathcal { R } _ { i j } n _ { j } ^ { \prime }$ ,whose explicit expression is

$$
\mathcal { R } = \left( \begin{array} { c c c } { { \cos \phi } } & { { \sin \phi } } & { { 0 } } \\ { { - \sin \phi } } & { { \cos \phi } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \cos \theta } } & { { \sin \theta } } \\ { { 0 } } & { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) .
$$

Similarly,a tensor $\mathbf { M }$ with two indice\$ has components $M _ { i j }$ in the $( z , y , z )$ frame and $M _ { i j } ^ { \prime }$ in the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame,related by

$$
M _ { i j } = \mathcal { R } _ { i k } \mathcal { R } _ { j l } M _ { k l } ^ { \prime } ,
$$

or, solving for $M ^ { \prime }$ ， $M _ { i j } ^ { \prime } = ( \mathcal { R } ^ { T } M \mathcal { R } ) _ { i j }$ ,where $\mathcal { R } ^ { T }$ is the transpose matrix. Inserting $\mathcal { R }$ from eq. (3.7O),and plugging the resulting values of $M _ { i j } ^ { \prime }$ into qs. (3.67) and (3.68), we get

$$
\begin{array} { r l } { h _ { + } ( t ; \theta , \phi ) = \frac { 1 } { \tau } \frac { G } { c } \left[ } & { \hat { M } _ { 1 1 } ( \cos ^ { 2 } \phi _ { - } \sin ^ { 2 } \phi \cos ^ { 2 } \theta ) \right. } \\ & { \left. + \hat { M } _ { 2 2 } ( \sin ^ { 2 } \phi - \cos ^ { 2 } \phi \cos ^ { 2 } \theta ) \right. } \\ & { \left. - \hat { M } _ { 3 3 } \sin ^ { 2 } \theta \right] } \\ & { - \hat { M } _ { 1 2 } \sin 2 \phi ( 1 + \cos ^ { 2 } \theta ) } \\ & { + \hat { M } _ { 1 3 } \sin \phi \sin 2 \theta } \\ & { \left. + \hat { M } _ { 2 3 } \cos \phi \sin 2 \theta \right] , } \\ { h _ { \times } ( t ; \theta , \phi ) = \frac { 1 } { \tau } \frac { G } { c } \left[ ( \hat { M } _ { 1 1 } - \hat { M } _ { 2 2 } ) \sin 2 \phi \cos \theta \right. } \\ & { \left. + 2 \hat { M } _ { 1 2 } \cos 2 \phi \cos \theta \right. } \\ & { - 2 \hat { M } _ { 1 3 } \cos \phi \sin \theta } \\ & { \left. + 2 \hat { M } _ { 2 3 } \sin \theta \right] \sin \theta . } \end{array}
$$

Ihis equation allows us to compute the angular distribution of the Hadrupole radiation, once $M _ { i j }$ is given.

16Recall that h+ and hx are defied in terms of the components of $h _ { i j }$ in the plane transverse to the propagation direction. Therefore these are“the”polarization amplitudes,and are denoted by $h _ { + }$ and $h _ { \times }$ ,rather than $h _ { + } ^ { \prime }$ and $h _ { \times } ^ { \prime }$

![](images/2c4aece31837b4d0ca160734c71c8238d52ba0d069d3380071c1c044cc966e21.jpg)  
Fig.3.2 The relation between the $( \hat { \mathbf { x } } , \hat { \mathbf { y } } , \hat { \mathbf { z } } )$ frame and the $( \hat { \mathbf { u } } , \hat { \mathbf { v } } , \hat { \mathbf { n } } )$ frame. The vector $\hat { \bf u }$ is in the $\left( \hat { \mathbf { x } } , \hat { \mathbf { y } } \right)$ plane,while $\hat { \mathbf { v } }$ points downward, with respect to the $\left( \hat { \mathbf { x } } , \hat { \mathbf { y } } \right)$ plane.

We see from eq.(3.59) that the leading term of the multipole expansion is the mass quadrupole. There is neither monopole nor dipole radiation for GWs.This can be understood in two different ways. First of all observe that a monopole term would depend on $M$ and a dipole term on $P ^ { i }$ (the mass dipole moment $M ^ { i }$ can be set to zero with a shift of the originof thecoodinatesystem).Furtrmore $h _ { i j } ^ { \mathrm { T T } }$ depends on derivatives of the multipole moments, since a static source does not radiate. However, $M$ and $P ^ { i }$ are conserved quantities,so any contribution from $M$ or $P ^ { i }$ must vanish.

Actually, $M$ and $P ^ { i }$ are conserved only at the level oflinearized theory: a radiating system loses mass and, in general,also linear momentum (see page 130). However, the absence of monopole and dipole radiation holds more generally,and is not restricted to linearized theory. One can verify this observing that,even when we include all non-linear terms. as in eq. (2.113),the right-hand side of the wave equation must still be conserved,to be consistent with the Lorentz gauge condition. We will see explicitly in Section 5.2 how to write the equations in such a form. Using that expresson,see in particular eqs. (5.69)，(5.71) and (5.72),one can verify that the derivation of the absence of monopole and dipole radiation goes through even in the full non-linear theory. The difference with linearized theory is that the lowest-order multipole that contributes,rather than being the quadrupole moment of the energy density of matter, $T ^ { 0 0 }$ , is the quadrupole moment of a more general quantity $\tau ^ { 0 0 }$ that includes also the contribution of the gravitational field

However, there is no need tb enter into the details of the non-linear theory:the absence of monopole and dipole radiation is simply the expression of the fact that the graviton is a massless particle with helicity $\pm 2$ We already showed in Problem 1.2 that it is impossible to put a graviton in a state with total angular momentum $j = 0$ or $j = 1$ This emerged as a consequence of the fact that the graviton is a massless particle with helicities $\pm 2$ ,and it therefore obeys gauge conditions that eliminate the spurious degrees of freedom. Indeed,these conditions al-lowed us to reduce the five degrees of a traceless syinmetric tensor $h _ { i j }$ which would be appropriate for describing a massive spin-2 particle to the two degrees of freedom ofa massless particle,as we discussed in Section 2.2.2.

Since it is impossible to put a graviton in a state with total angular momentum $j = 0$ or $j = 1$ ，we can have neither monopole nor dipole radiation,since they correspond to a collection of quanta with $j = 0$ and $j = 1$ ,respectively. The situation is completely analogous to electrodynamics,where the photon is massless and has helicity $\pm 1$ ，soit is impossible to put it in a state with total angular momentum $j = 0$ (see Problem 1.2,or Landau and Lifshitz,Vol.IV (1982),Section 6),and therefore monopole radiationis forbidden. In electromagnetism,the leading term of the multipole expansion is therefore dipole radiation.

# 3.3.2 Radiated energy

Inserting eq.(3.59) in eq.(1.153)and using the property (1.37) of the Lambda tensor,we find the power radiated per unit solid angle,in the quadrupole approximation,

$$
\begin{array} { r } { \left( \displaystyle \frac { d P } { d \Omega } \right) _ { \mathrm { q u a d } } = \frac { r ^ { 2 } c ^ { 3 } } { 3 2 \pi G } \langle \dot { h } _ { i j } ^ { \mathrm { T T } } \dot { h } _ { i j } ^ { \mathrm { T T } } \rangle } \\ { = \displaystyle \frac { G } { 8 \pi c ^ { 5 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) \langle \ddot { Q } _ { i j } \ddot { Q } _ { k l } \rangle , } \end{array}
$$

where,as usual, the average is a temporal average over several characteristic periods of the GW,and it is understood that $\ddot { Q _ { i j } }$ must be evaluated at the retarded time $t - r / c ,$ The angular integral can be performed observing that the dependence on $\hat { \mathbf { n } }$ is only in $\Lambda _ { i j , k l }$ .Using eqs.(3.21) and (3.22) we find

$$
\int d \Omega \Lambda _ { i j , k l } = \frac { 2 \pi } { 1 5 } \left( 1 1 \delta _ { i k } \delta _ { j l } - 4 \delta _ { i j } \delta _ { k l } + \delta _ { i l } \delta _ { j k } \right) .
$$

Then,the total radiated power (or,in|notation used in astrophysics, the total gravitational luminosity $\mathcal { L }$ of the source) is,in the quadrupole approximation,

$$
\overline { { { P _ { \mathtt { q u a d } } = \frac { G } { 5 c ^ { 5 } } \langle \overset { . . . } { Q } _ { i j } \overset { . . . } { Q } _ { i j } ^ { . } \rangle } } } ,
$$

where,again, $\ddot { Q _ { i j } }$ must be evaluated at the retarded time $t - r / c$ This is the famous quadrupole formula,first derived by Einstein.17 Sometimes, mexplicit computations,it is more practical to use $M _ { i j }$ rather than $Q _ { i j }$ Substituting $Q _ { i j } = M _ { i j } - ( 1 / 3 ) \delta _ { i j } M _ { k k }$ in eq. (3.75) we have

$$
P _ { \mathrm { q u a d } } = { \frac { G } { 5 c ^ { 5 } } } \langle { \ddot { M } } _ { i j } { \ddot { M } } _ { i j } - { \frac { 1 } { 3 } } ( { \ddot { M } } _ { k k } ) ^ { 2 } \rangle .
$$

The same result could be obtained by observing that eq.(3.73) is still valid if we replace $\Lambda _ { i j , k l } \overleftrightarrow { Q } _ { i j } \overleftrightarrow { Q } _ { k l }$ by $\dot { \Lambda } _ { i j , k l } \ddot { M } _ { i j } \ddot { M } _ { k l }$ ， since the contraction of $\Lambda _ { i j , k l }$ with $\delta _ { i j }$ (orwith $\delta _ { k l }$ ）gives zero. However，when we use $\Lambda _ { i j , k l } \ddot { M } _ { i j } \ddot { M } _ { k l }$ , after integrating in $d \Omega$ ,onthe right-hand side of eq. (3.74) the term $- 4 \delta _ { i j } \delta _ { k l }$ (which gave zero when contracted with $\ddot { Q } _ { i j } \ddot { Q } _ { k l } )$ now contributes, since $M _ { i j }$ is not traceless,and we find eq. (3.76) again.

The energy radiated per unit solid ahgle is obtained by integrating the power,eq. (3.73)，with respect to tlime.We write the quadrupole moment in terms of its Fourier transform,

$$
Q _ { i j } ( t ) = \int _ { - \infty } ^ { \infty } \frac { d \omega } { 2 \pi } \tilde { Q } _ { i j } ( \omega ) e ^ { - i \omega t } ,
$$

ndintegrating eq.(3.73) withrespectto time, we get

<table><tr><td>G 8π25A,（(n）</td><td></td></tr><tr><td></td><td></td></tr></table>

17Observe that some authors,e.g. Landau and Lifshitz,Vol.II (1979),define the quadrupole moment with a different normalization,

$$
( Q _ { i j } ) ^ { \mathrm { L L } } = \int d ^ { 3 } x \rho ( t , { \bf x } ) ( 3 x ^ { i } x ^ { j } - r ^ { 2 } \delta ^ { i j } ) ,
$$

where the superscript“LL”stands for Landau and Lifshitz.This is larger by a factor of 3 than our definition, eq.(3.58).In term of this quantity,the quadrupole formula therefore reads

$$
P _ { \mathrm { q u a d } } = \frac { G } { 4 5 c ^ { 5 } } \langle ( \ddot { Q _ { i j } } \ddot { Q _ { i j } } ) ^ { \mathrm { L L } } \rangle ,
$$

and all other equations involving $Q _ { i j }$ must be rescaled similarly.

where the integral in $d \omega$ from $- \infty$ to $+ \infty$ has been written as twice an integral from zero to $\infty$ using $\tilde { Q } _ { i j } ( - \omega ) = \tilde { Q } _ { i j } ^ { * } ( \omega )$ . Integrating over the solid angle we find the total radiated energy,

$$
E _ { \mathrm { q u a d } } = \frac { G } { 5 \pi c ^ { 5 } } \int _ { 0 } ^ { \infty } d \omega \omega ^ { 6 } \tilde { Q } _ { i j } ( \omega ) \tilde { Q } _ { i j } ^ { * } ( \omega ) ,
$$

18To compare this equation with the results in the literature,beside checking the factor of 3 in the normalization of $Q _ { i j }$ ,one must also check whether or not the Fourier transform is defined using $d \omega / ( 2 \pi )$ ，as we do,or simply $d \omega$ ，as, for instance,in Weinberg (1972） or in Straumann (2004).

and therefore the energy spectrum,integrated over the solid angle,is18

$$
\overline { { \Big ( \frac { d E } { d \omega } \Big ) _ { \mathrm { \tiny ~ q u a d } } } } = \frac { \widetilde { \mathrm { \tiny ~ G } } } { 5 \pi c ^ { 5 } } \omega ^ { 6 } \widetilde { Q } _ { i j } ( \omega ) \widetilde { Q } _ { i j } ^ { * } ( \omega ) .
$$

For a monochromatic source,radiating at a frequency $\omega _ { 0 } > 0$ , we proceed as in Section 3.1: we write,for positive $\omega$ ，

$$
\tilde { Q } _ { i j } ( \omega ) \ne q _ { i j } 2 \pi \delta ( \omega - \omega _ { 0 } ) ,
$$

insert this into eq. (3.78),and again use $2 \pi \delta ( \omega = 0 ) = T$ ，where $T$ is the total (infinite) time interval. The instantaneous power generated by the monochromatic source is obtained by dividing by $T$ ,so

$$
\left( \frac { d P } { d \Omega d \omega } \right) _ { \mathrm { q u a d } } = \frac { G \omega _ { 0 } ^ { 6 } } { 4 \pi c ^ { 5 } } \left( \Lambda _ { i j , k l } q _ { i j } q _ { k l } ^ { * } \right) \delta ( \omega - \omega _ { 0 } ) .
$$

As for the linear momentum,inserting eq. (3.59) into eq. (1.164) we get

$$
{ \frac { d P ^ { i } } { d t } } = - { \frac { G } { 8 \pi \epsilon ^ { 5 } } } \int d \Omega \ddot { Q } _ { a b } ^ { \mathrm { T T } } \partial ^ { i } \ddot { Q } _ { a b } ^ { \mathrm { T T } } .
$$

Under reflection, ${ \bf x } \ \to \ - { \bf x }$ ，the quadrupole moment is invariant while $\partial ^ { i }  - \partial ^ { i }$ .Therefore the integrand is odd,and the angular integral vanishes. There is no loss of linear momentum in the quadrupole approximation.A non-vanishing result can be obtained by going beyond the quadrupole approximation,from the interference between multipoles of different parity,as we will see in Section 3.4.

# 3.3.3 Radiated angular momentum

The angular momentum carried away per unit time by GWs can be obtainedbypluggingtheexpresionfor $h _ { i j } ^ { \mathrm { T T } }$ in the quadrupole approx imation,eq.(3.59)，into the general formula for the rate of angular momentum loss,eq. (2.61). Recalling that the first term in eq.(2.61) is the contribution form the orbital angular momentum $L ^ { i }$ of the GWs while the second comes from the spin $S ^ { i }$ of the field configuration,we write

$$
\frac { d J ^ { i } } { d t } = \frac { d L ^ { i } } { d t } + \frac { d S ^ { i } } { d t } .
$$

For the orbital part we have

$$
\left( \frac { d L ^ { i } } { d t } \right) _ { \mathrm { q u a d } } = - \frac { c ^ { 3 } } { 3 2 \pi G } \epsilon ^ { i k l } \int d \Omega r ^ { 2 } \langle \dot { h } _ { a b } ^ { \mathrm { T T } } x ^ { k } \partial ^ { l } h _ { a b } ^ { \mathrm { T T } } \rangle .
$$

We then substitute $h _ { a b } ^ { \mathrm { T T } } ( t , \mathbf { x } ) = ( 2 G / r c _ { | } ^ { 4 } ) \Lambda _ { a b , c d } ( \hat { \mathbf { n } } ) \ddot { Q } _ { c d } ( t - r / c )$ and we perform the angular integral. The explicit computation is slightly involved,but we find it useful to perform it in detail. The uninterested reader can jump to the result,eq. (3.93).

When we compute $\partial ^ { l } h _ { a b } ^ { \mathrm { T T } }$ ，the derivative $\partial ^ { \underline { { \iota } } }$ acts on $\Lambda _ { a b , c d } ( { \hat { \mathbf { n } } } )$ (since $n ^ { i } = $ $x ^ { i } / r )$ as well as on $\ddot { Q } _ { c d } ( t - r / c )$ However,

$$
\begin{array} { l } { \displaystyle \frac { \partial } { \partial x ^ { l } } \ddot { \mathcal { Q } } _ { c d } ( t - r / c ) = \left( \frac { \partial r } { \partial x ^ { l } } \right) \frac { d } { d r } \ddot { \mathcal { Q } } _ { c d } ( t - r / c ) } \\ { = - \displaystyle \frac { x ^ { l } } { r } \frac { 1 } { c } \ddot { \mathcal { Q } } _ { c d } ( t - r / c ) . } \end{array}
$$

In eq.(3.85) this therefore gives a contribution proportional to $\epsilon ^ { i k l } x ^ { k } x ^ { l } = 0$ The only non-vanishing term is obtained when $\partial ^ { \iota }$ acts on $\Lambda _ { a b , c d } ( { \hat { \mathbf { n } } } )$ ,and

$$
\left( \frac { d L ^ { i } } { d t } \right) _ { \mathrm { q u a d } } = - \frac { G } { 2 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { c d } \ddot { Q } _ { f g } \rangle \int \frac { d \Omega } { 4 \pi } \Lambda _ { a b , c d } x ^ { k } \partial ^ { l } \Lambda _ { a b , f g } ,
$$

where it is understood that the derivatives of the quadrupole moment are evaluated at theretarded time $t - r / c$ .Weobserve that

$$
{ \begin{array} { c } { { \cfrac { \partial n ^ { m } } { \partial x ^ { l } } } = { \cfrac { \partial } { \partial x ^ { l } } } \left( { \cfrac { \dot { x } ^ { m } } { r } } \right) } \\ { = { \cfrac { \delta ^ { l m } } { r } } - { \cfrac { x ^ { l } x ^ { m } } { r ^ { 3 } } } } \\ { = { \cfrac { 1 } { r } } P ^ { l m } , } \end{array} }
$$

where $P ^ { l m } = \delta ^ { l m } - n ^ { l } n ^ { m }$ is the projector first introduced ineq. (1.35).19 Then

$$
\begin{array} { c } { { \displaystyle \partial ^ { l } \Lambda _ { a b , f g } = \frac { \partial n ^ { m } } { \partial x ^ { l } } \frac { \partial } { \partial \eta ^ { m } } \Lambda _ { a b , f g } } } \\ { { = \displaystyle \frac { 1 } { r } { \cal P } ^ { l m } \frac { \partial } { \partial \ h ^ { m } } \Lambda _ { a b , f g } . } } \end{array}
$$

Using $\Lambda _ { a b , f g }$ in the form (1.36) together with

$$
\frac { \partial P ^ { i j } } { \partial n ^ { m } } = - \langle \delta ^ { i m } n ^ { j } + \delta ^ { j m } n ^ { i } \rangle ,
$$

lich follows from thedefinitionof $P ^ { i j }$ , we find the identity

$$
P ^ { l m } \frac { \partial } { \partial n ^ { m } } \Lambda _ { a b , f g } = - \big ( n _ { f } \Lambda _ { a b , l g } + n _ { g } \Lambda _ { a b , l f } + n _ { a } \Lambda _ { l b , f g } + n _ { b } \Lambda _ { l a , f g } \big ) .
$$

Ielast two terms give zero when contracted with the factor $\Lambda _ { a b , c d }$ in eq. (3.87), ice the Lambda tensor is transverse on all indices, $n _ { a } \Lambda _ { a b , c d } = n _ { b } \Lambda _ { a b , c d } = 0$ Then

$$
\begin{array} { c } { { \displaystyle \left( \frac { d L ^ { i } } { d t } \right) _ { \mathrm { q u a d } } = \displaystyle \frac { G } { 2 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { c d } \ddot { Q } _ { f g } \rangle \displaystyle \int \displaystyle \frac { d \Omega } { 4 \pi } \bigwedge _ { a b , c d } n _ { k } ( n _ { f } \Lambda _ { a b , l g } + n _ { g } \Lambda _ { a b , l f } ) } } \\ { { = \displaystyle \frac { G } { 2 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { c d } \ddot { Q } _ { f g } \rangle \displaystyle \int \displaystyle \frac { d \Omega } { 4 \pi } n _ { k } ( n _ { f } \Lambda _ { c d , l g } + n _ { g } \Lambda _ { c d , l f } ) . \qquad ( 3 ) } } \end{array}
$$

19 As always, we do not need to be careful about raising and lowering spatial indices,since the spatial metric is $\delta _ { i j }$ Otherwise,we should write $\partial n ^ { m } / \partial x ^ { l } =$ $( 1 / r ) P _ { l } ^ { m }$

The angular integral can now be computed by inserting the explicit form of the $\Lambda$ tensor (1.39) and using the identities (3.21) and (3.22) (the term with six factors n is proportional tonn' and vanishes when contracted with e so we only need the integrals with two and with four factors n).

The result is

$$
\left( \frac { d L ^ { i } } { d t } \right) _ { \mathrm { \scriptsize { q u a d } } } = \frac { 2 G } { 1 5 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { k a } \ddot { Q } _ { l a } \rangle .
$$

The calculation of the spin part gives

$$
\begin{array} { r } { \left( \displaystyle \frac { d { \cal S } ^ { i } } { d t } \right) _ { \mathrm { q u a d } } = \displaystyle \frac { c ^ { 3 } } { 1 6 \pi G } \epsilon ^ { i k l } \int r ^ { 2 } d \Omega \langle \dot { h } _ { a l } ^ { \mathrm { T T } } h _ { a k } ^ { \mathrm { T T } } \rangle \qquad } \\ { = \displaystyle \frac { G } { c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { m n } \ddot { Q } _ { c d } \rangle \int \frac { d \Omega } { 4 \pi } \Lambda _ { a l , m n } \Lambda _ { a k , c d } . } \end{array}
$$

Using eq. (1.36) we can provethe identity

$$
\Lambda _ { a l , m n } \Lambda _ { a k , c d } = P _ { l n } \Lambda _ { m k , c d } - \frac { 1 } { 2 } P _ { m n } \Lambda _ { k l , c d } .
$$

The second factor gives zero contracted with $\epsilon ^ { i k l }$ and, again using the identities eqs.(3.21） and (3.22),the remaining angular integration is straightforward,

$$
\begin{array} { r l } { ~ } & { \left( \displaystyle \frac { d S ^ { i } } { d t } \right) _ { \mathrm { q u a d } } = \displaystyle \frac { G } { c ^ { 5 } } \epsilon ^ { i k l } \ddot { Q } _ { m n } \ddot { Q } _ { c d } \int \frac { d \Omega } { 4 \pi } P _ { l n } \Lambda _ { m k , c d } } \\ & { ~ = \displaystyle \frac { 4 G } { 1 5 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { k a } \ddot { Q } _ { l a } \rangle . } \end{array}
$$

Summing the spin and orbital contribution,we finally get the angular momentum carried away,per unit time,by the GWs,

$$
\overline { { \left( \frac { d J ^ { i } } { d t } \right) _ { \mathrm { { q u a d } } } } } = \frac { 2 G } { 5 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { k a } \ddot { Q } _ { l a } \rangle ,
$$

where we recall again that thelderivatives of the quadrupole moment are evaluated at the retarded time $t - r / c$

# 3.3.4 Radiation reaction on non-relativistic sources

We have seen that gravitational radiation carries away energy and angular momentum.Ultimately,this energy and angular momentum must come from the source.We therefore expect that the energy and angular momentum carried by the GWs,at a large distance $r$ from the source and at time $t$ ，were drained at retarded time $t - r / c$ from the energy and the angular momentum of the source.In the full non-linear theory of gravity (so,in particular,when dealing with self-gravitating sources) one must however take into account non-linear efects in the GW propagation from the source to infnity (such as back-scattering of gravitons on the background space-time,graviton-graviton scattering,etc.).We will see in Section 5.3.4 that,as a result at higher orders in the post-Newtonian expansion part of the gravitational radiation is delayed,and tle total GW consists of a wavefront,which travels at the speed of light, and a“tail”,which arrives later.Thus,it is not at all obvious that there is an exact equality,to all orders in the post-Newtonian expansion,between the instantaneous power radiated at large distances at a given time $t$ ,and the rate of energy loss of the source at the corresponding retarded time. We will discuss the issuein Section 5.3.5. However,as long as we are in linearized theory,the background space-time is flat,the wave propagates at the speed of light,and this energy balance argument is inescapable.

For $v / c \ll 1$ , the leading term is given by quadrupole radiation,so the instantaneous rate of decreases of energy and orbital20 angular momentum of the source must be given by eqs. (3.75) and (3.97),i.e.

$$
\begin{array} { l } { \displaystyle \frac { d E _ { \mathrm { s o u r c e } } } { d t } = - \frac { G } { 5 c ^ { 5 } } \langle \ddot { Q } _ { i j } \ddot { Q } _ { i j } \rangle , } \\ { \displaystyle \frac { d L _ { \mathrm { s o u r c e } } ^ { i } } { d t } = - \frac { 2 G } { 5 c ^ { 5 } } \epsilon ^ { i k l } \langle \ddot { Q } _ { k a } \ddot { Q } _ { l a } \rangle . } \end{array}
$$

We have required that $d E _ { \mathrm { s o u r c e } } / d t$ ,computed at retarded time $t - r / c ,$ be the negative of the power radiated at a large distance $r$ in GWs,at time $t$ Since the latter is expressed in terms of $\langle \ddot { Q } _ { i j } \ddot { Q } _ { i j } \rangle$ evaluated at retarded time,as in eq. (3.75),we have obtained an equality between $\mathbb { d } \mathbb { E } _ { s 0 \ u r c e } / d t$ and $- ( G / 5 c ^ { 5 } ) \langle \ddot { Q } _ { i j } \ddot { Q } _ { i j } \rangle$ ,both evaluated at the same value of retarded time or,equivalently,at the same value of time (and similarly for the angular momentum).

The multipole expansion assumes that the sources are non-relativistic so,at least to lowest order,the dynamics of the source is governed by Newtonian mechanics,and it should be possible to describe the backreaction of the GWs on the source in terms of a force $\mathbf { F }$ .Then，we xpect that it should be possible to write eq.(3.98) in the form

$$
\frac { d E _ { \mathrm { s o u r c e } } } { d t } = \langle F _ { i } v _ { i } \rangle ,
$$

more precisely, for an extended body,

$$
\frac { d E _ { \mathsf { s o u r c e } } } { d t } = \langle \int d ^ { 3 } x \frac { d F _ { i } } { d V } \dot { x } _ { i } \rangle ,
$$

where $d F _ { i } / d V$ is the force per unit volume. Similarly,we expect that (3.99) can be written as

$$
\frac { d L _ { \sf s o u r c e } ^ { i } } { d t } = \langle T ^ { i } \rangle ,
$$

mhere $T ^ { i }$ is the torque associated to the force per unit volume $d F _ { i } / d V$ The average $\left. \ldots \right.$ takes into account the fact that the energy and angu-momentum of GWs are notions well defined only if we average over

20Gravitational waves，asanyfeld, carry awaya total angular momentum $J ^ { i }$ that,as we saw in Section 2.1.2, is made of a spin contribution and of an orbital angular momentum contribution.This total angular momentum is drained from the total angular momentum of the source which,for a macroscopic source,is a purely orbital angular momentum.

several periods. The expression for lthis force, in the quadrupole approximation, can be found as follows. Since inside $\langle \ldots \rangle$ we can integrate by parts (compare with Note 23 on page 35),we rewrite eq. (3.98) as

$$
\frac { d E _ { \mathrm { s o u r c e } } } { d t } = - \frac { \dot { \mathcal { G } } } { 5 \epsilon ^ { 5 } } \langle \frac { d Q _ { i j } } { d t } \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } \rangle .
$$

From eq.(3.58) we have

$$
\frac { d Q _ { i j } } { d t } = \int d ^ { 3 } x ^ { \prime } \partial _ { t } \rho ( t , { \bf x } ^ { \prime } ) \bigg ( x _ { i } ^ { \prime } x _ { j } ^ { \prime } - \frac { 1 } { 3 } { r ^ { \prime } } ^ { 2 } \delta _ { i j } \bigg ) ~ .
$$

The term proportional to $\delta _ { i j }$ gives zero when contracted with $d ^ { 5 } Q _ { i j } / d t ^ { 5 }$ For a Newtonian source with $T ^ { 0 0 } / \vert c ^ { 2 } = \rho$ and $T ^ { 0 i } / c = \rho v ^ { i }$ ， the conservation of the energy-momentum tensor gives the continuity equation

$$
\partial _ { t } \rho + \partial _ { k } \langle \rho v _ { k } \rangle = 0 .
$$

We then replace $\partial _ { t } \rho$ by $- \partial _ { k } ( \rho v _ { k } ) |$ in eq. (3.104) and we integrate by parts.The boundary term at infinity vanishes,because the body has a finite extent,so $\rho = 0$ beyond some value $r > a$ . Therefore

$$
\int d ^ { 3 } x ^ { \prime } \partial _ { t } \rho ( t , { \bf x } ^ { \prime } ) x _ { i } ^ { \prime } x _ { j } ^ { \prime } = \int d ^ { 3 } x ^ { \prime } \rho ( t , { \bf x } ^ { \prime } ) \dot { x } _ { k } ^ { \prime } ( \delta _ { i k } x _ { j } ^ { \prime } + \delta _ { j k } x _ { i } ^ { \prime } ) ,
$$

and

$$
\frac { d E _ { \mathrm { s o u r c e } } } { d t } = - \frac { 2 G } { 5 c ^ { 5 } } \langle \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } \int d ^ { 3 } x ^ { \prime } \rho ( t , { \bf x } ^ { \prime } ) \dot { x } _ { i } ^ { \prime } x _ { j } ^ { \prime } \rangle .
$$

Of course, $d ^ { 5 } Q _ { i j } / d t ^ { 5 }$ is a function only of time,and does not depend on the dummy integration variable $x ^ { \prime }$ .Then it can be carried inside the integral,and eq.(3.107) can be written as

$$
\frac { d E _ { \mathrm { s o u r c e } } } { d t } = \langle \int d ^ { 3 } x ^ { \prime } \frac { d F _ { i } } { d V ^ { \prime } } \dot { x } _ { i } ^ { \prime } \rangle ,
$$

with a force per unit volume

$$
\frac { d F _ { i } } { d V ^ { \prime } } = - \frac { 2 G } { 5 c ^ { 5 } } \rho ( t , { \bf x } ^ { \prime } ) x _ { j } ^ { \prime } \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } ( t ) .
$$

Therefore the total force is

$$
F _ { i } = - \frac { 2 G } { 5 c ^ { 5 } } \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } \int d ^ { 3 } x ^ { \prime } \rho ( t , { \bf x } ^ { \prime } ) x _ { j } ^ { \prime } .
$$

Defining the center-of-mass coordinates by

we find

$$
\begin{array} { c } { { \displaystyle x _ { j } ( t ) \equiv \frac { 1 } { m } \int d ^ { 3 } x ^ { \prime } \rho ( t , { \bf x } ^ { \prime } ) x _ { j } ^ { \prime } , } } \\ { { \displaystyle F _ { i } = - \frac { 2 G } { 5 c ^ { 5 } } m x _ { j } \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } . } } \end{array}
$$

We have deduced this gravitational force on the source considering the GWsat infinity and imposing the energy balance.However,the motion ofa particle under the effect of gravitational forces is completely determined by the value of the metric and its derivatives at the particle location．Thus,it should be possible to deduce the back-reaction force (3.1l2)also looking directly at the metric in the near-source region,without invoking the energy balance.In other words,if one solves for the gravitational field everywhere in space,in correspondence to a GW solution in the far region,there must be terms in the metric in the near region which,acting directly on the source motion through the geodesic equation,produce exactly the effect that we have inferred from the energy balance argument,i.e. provide the force (3.112).This correspondence between the GWs in the far region and the metric in the near region will be discussed in Chapter 5 in the appropriate context,which is the post-Newtonian formalism.The result is that,indeed,in the near region,among other terms that describe post-Newtonian corrections to the static potential, there is also a correction to the metric coefficient $h _ { 0 0 }$ of the form

$$
\Delta h _ { 0 0 } = - \frac { 2 \Phi } { \epsilon ^ { 2 } } ,
$$

with

$$
\Phi ( t , \mathbf { x } ) = \frac { G } { 5 c ^ { 5 } } x _ { i } x _ { j } \frac { d ^ { 5 } Q _ { i j } } { d t ^ { 5 } } ( t ) .
$$

This is known as the Burke-Thorne pqtential,21 and generates a Newtonian force

$$
F _ { i } = - m \partial _ { i } \Phi ,
$$

in agreement with eq. (3.112).22 As we will discuss in detail in Chapter 5, this termis singled out,and associatedto radiation reaction, thanks to the fact that it is odd under time reversal. Terms associated with conservative forces are invariant under time reversal.In contrast,the emission of radiation breaks time-reversal invariance through the boundary conditions,since we impose that there is no incoming radiation (technically, at minus null infinity,see Note 1 on page 1O2),while at plus nullinfinity we can have outgoing radiation.

We now check that the force (3.112) also correctly accounts for the ngular momentum loss. The torque on a unit volume located at the position $x _ { i }$ is

$$
\begin{array} { l } { { \displaystyle { \frac { d { \cal T } _ { i } } { d V } } = \epsilon _ { i j k } x _ { j } \frac { d F _ { k } } { d V } } } \\ { { \displaystyle ~ = - \frac { 2 G } { 5 c ^ { 5 } } ~ \epsilon _ { i j k } \rho ( t , { \bf x } ) x _ { j } x _ { l } \frac { d ^ { 5 } Q _ { k l } } { d t ^ { 5 } } } , }  \end{array}
$$

where we used eq. (3.109). Then

$$
T _ { i } = - \frac { 2 G } { 5 c ^ { 5 } } \ \epsilon _ { i j k } \frac { d ^ { 5 } Q _ { k l } } { d t ^ { 5 } } \int d ^ { 3 } x \rho ( t , { \bf x } ) x _ { j } x _ { l } .
$$

21igherreiosack reaction force are given in eqs.(5.190) and (5.191)．When comparing these results with eq. (3.1l4),observe that eqs.(5.190) and (5.91) are written in terms of the variable $\mathsf { h } _ { \mu \nu }$ defined in eq.(5.69) (which in the linearized limit reduces to $- \bar { h } _ { \mu \nu }$ ),rather than in terms of $h _ { \mu \nu }$

22Observe that there is here an abuse of notation．In eq.(3.114), $x ^ { i }$ is the generic spatial variable.After taking the derivative with respect tox in eq.(3.115)，we evaluate the force on the actual location of the particle, i.e．on the position $x ^ { i } ( t )$ defined by eq.(3.1ll),and this gives eq. (3.112). For instance,for a point-like mass $\mu$ the quadrupole moment is $Q _ { i j } ( t ) ~ =$ $\mu [ x _ { i } ( t ) x _ { j } ( t ) \ - \ ( 1 / 3 ) \delta _ { i j } | { \bf x } ( t ) | ^ { 2 } ]$ ，where $x _ { i } ( t )$ is the actual trajectory of the particle,rather then the generic spatial variable $x _ { i }$ So $Q _ { i j }$ is a given function of time only,and $\partial _ { i }$ in eq. (3.115) does not act on it.

In the last integral we can replace $x _ { j } x _ { l }$ by $x _ { j } x _ { l } - ( 1 / 3 ) \delta _ { i j } r ^ { 2 }$ ,since the term $\sim \delta _ { j l }$ gives zero contracted with $\epsilon _ { i j k } d ^ { 5 } Q _ { k l } / d t ^ { 5 }$ ,s0

$$
T _ { i } = - \frac { 2 G } { 5 c ^ { 5 } } \epsilon _ { i j k } Q _ { j l } \frac { d ^ { 5 } Q _ { k l } } { d t ^ { 5 } } .
$$

In eq. (3.102)actually enters $\left. T _ { i } \right.$ . Inside the average, we can integrate by parts twice,and we get

$$
\langle T _ { i } \rangle = \mathcal { - } \frac { 2 G } { 5 c ^ { 5 } } \epsilon _ { i k l } \langle \ddot { Q } _ { k a } \ddot { Q } _ { l a } \rangle .
$$

Comparison with eq. (3.99) shows that we have indeed correctly reproduced the expression for the angular momentum loss of the source.

It should be observed that|this is also by far the quickest way to derive eq. (3.97),without going through the formalism of Noether's the orem and the more complicated algebra of Section 3.3.3.However,the derivation from the Noether theorem is more general, since it holds independently of the multipole expansion,and of whether or not the back-reaction of GWs on the source can be described by Newtonian mechanics.It is also conceptually more satisfying，since it stresses that the angular momentum carried by GWs is an intrinsic property of the gravitational field,independent of the description of the source,that can be computed by applying the standard methods of classical field theory, as is usually done in all other feld theories.

Finally，,we expect that the change in linear momentum should be given by $d P ^ { i } / d t = \langle F ^ { i } \rangle$ .This is proportional to $\langle x _ { j } ( t ) d ^ { 5 } Q _ { i j } / d t ^ { 5 } ( t ) \rangle$ Since the quadrupole moment is even under parity while $x _ { j }$ is odd,the integrand is odd and,for a periodic motion,its average ovcr one orbital period vanishes and therefore $  F _ { i }  = 0$ .This is in agreement with the fact that,in the quadrupole approximation, linear momentum is conserved,see the discussion below eq. (3.83).

# Gravitational radiation and the equivalence principle

The above results also allow us to clarify an apparent paradox related to the equivalence principle. Consider,for simplifying the setting,a mass $\mu$ orbiting a mass $M$ ,in the limit $M / \mu \to \infty$ ，Thus,the light mass $\mu$ is accelerated by the gravitational field of the heavy mass $M$ and, according to our computations,it radiates GWs (while $M$ is static and does not radiate.） An observer at large distance from the source, wel into the far region,would then in principle be able to detect the waves emitted,and would conclude that the mass $\mu$ indeed emits gravitational radiation.

Examine now the same situation from the point of view of an observer freely falling together with the mass $\mu$ .According to the equivalence principle,for this observer,in a sufficiently small region around the mass $\mu$ ,the gravitational field vanishes.We have indeed seen explicitly in Section 1.3.2 how to construct such a freely falling frame all along a geodesic. In this frame the mass $\mu$ is not accelerated,and the corresponding observer should then conclude that the mass $\mu$ does not radiate,contrary to the findings of the observer at infinity.

This apparent paradox can be understood recalling that the equivalence principle holds only locally,i.e.in a region around the mass $\mu$ much smaller than the typical scales of spatial variation of the gravitational field. One such scale is the length $\uparrow ,$ overwhich retardation effects become important (and which determines the wavelength of the GWs detected by the observer at infinity.） Then，conclusions based on the equivalence principle can be valid only up to a distance $r$ from the mass $\mu$ much smaller than .23 This means that the equivalence principle at most gives us informations on what happens in the near zone $r \ll \lambda$ ； GWs rather appear in the far zone $r \gg \nmid$ ,so there is no paradox in the fact that,using arguments valid only for $r \ll \lambda$ ,one does not see them. The presence of gravitational radiation at infinity is reflected, in the near zone,in the existence of the force given by eqs.(3.114) and (3.115). However,in the near region retardation effects are negligible,so this term just gives a correction to the static|gravitational force,which furthermore is hidden behind other,much larger,corrections.We will see in fact in Chapter 5 that,in an expansion in $\upsilon / c$ ,the radiation-reaction force is of order $( \upsilon / c ) ^ { 5 }$ (as it is alreadyclear from the factor $1 / c ^ { 5 }$ in eq.(3.1l4))，while the Newtonian gravitational field receives generalrelativistic corrections,corresponding to conservative forces,already at orders $( \upsilon / c ) ^ { 2 }$ and $( \upsilon / c ) ^ { 4 }$ .All these tidal-like terms,however,in the far region decrease much faster than 1/r,leaving us with the radiation field only.

# 3.3.5 Radiation from a closed system of point masses

For a point-like particle moving on a given trajectory $x _ { 0 } ( t )$ ,in flat spacetime, the energy-momentum tensor is24

$$
T ^ { \mu \nu } ( t , { \bf x } ) = \frac { p ^ { \mu } p ^ { \nu } } { \gamma m } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { 0 } ( t ) ) ,
$$

where $\gamma = ( 1 - v ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ ，and $p ^ { \mu } = \gamma m ( d x _ { 0 } ^ { \mu } / d t ) = ( E / c , \mathbf { p } )$ is the four-momentum. If we have a set of point particles labeled by an index $\mathbb { A }$ movingunder their mutual influence on trajectories $x _ { A } ^ { \mu } ( t )$ ,the total energy-momentum tensor of the systemis therefore

$$
\begin{array} { l } { { \displaystyle T _ { \mathrm { t o t } } ^ { \mu \nu } ( t , { \bf x } ) = \sum _ { A } \frac { p _ { A } ^ { \mu } p _ { A } ^ { \nu } } { \gamma _ { A } m _ { A } } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { A } ( t ) ) } \ ~ } \\ { { \displaystyle ~ = \sum _ { A } \gamma _ { A } m _ { A } \frac { d x _ { A } ^ { \mu } } { d t } \frac { d x _ { A } ^ { \nu } } { d t } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { A } ( t ) ) , } } \end{array}
$$

nd in particular

$^ { 2 3 } \mathrm { { I n } }$ fact, $\gamma$ must also be much smaller than the scale of spatial variation of the quasi-static tidal gravitational fields near the mass $\mu$ ,which in turn ismuch smaller than $\star$

$$
T _ { \mathrm { t o t } } ^ { 0 0 } ( t , { \bf x } ) = \sum _ { A } \gamma _ { A } m _ { A } c ^ { 2 } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { A } ( t ) ) .
$$

$^ { 2 4 } \mathrm { S e e } .$ e.g. LandauandLifshitzVol.II (1979),eq.(33.5),or Weinberg (1972), Section 2.8. In curved space-time the expression for $T ^ { \mu \nu }$ must be further multiplied by $1 / { \sqrt { - g } }$ ,see,e.g.Straumann (2003),eq.(5.83).

If the system is closed,i.e.no external forces are acting on it,the total energy-momentum tensor of the system is conserved,and we can consistently use eq.(3.121) on the right-hand side of the wave equation (3.3).It is important however to realize that,if we consider a single particle moving on a pre-assigned trajectory $x _ { 0 } ( t )$ ，we cannot compute the gravitational radiation that it generates by simply plugging $x _ { 0 } ( t )$ into eq. (3.120) and then using eq. (3.9). Such an energy-momentum tensor is in fact not conserved,as a consequence of the fact that, if the particle moves on a path that is not a geodesic of fat space-time. there must be external forces acting on it.To have a conserved energymomentum tensor,we must also include in our description all objects that generate a force on the particle.

Since the conservation of the energy-momentum tensor in fat space time is a consequence of the invariance under space-time translations, an equivalent way to pose the problem is to ask what happens to the multipole moments if we perform a shift of the origin of the coordinate system. To understand this point it is sufficient to restrict ourselves to the non-relativistic limit,i.e. to the quadrupole approximation,and to ask what happens to the quadrupole moment if we change the origin of our coordinate system.For a Set of non-relativistic particles,labeled by an index $A$ ,we see from eq. (3.122) that the second mass moment $\mathrm { i s ^ { 2 5 } }$

$$
\begin{array} { l } { { \displaystyle M ^ { i j } ( t ) = \sum _ { A } m _ { A } \int d ^ { 3 } x x ^ { i } x ^ { i } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { A } ( t ) ) } } \\ { { \displaystyle ~ = \sum _ { A } m _ { A } x _ { A } ^ { i } ( t ) x _ { A } ^ { j } ( t ) . } } \end{array}
$$

Under a constant translation, $x ^ { i }  x ^ { i } + a ^ { i }$ ， $M ^ { i j }$ acquires an additive contribution

$$
M ^ { i j } ( t )  M ^ { i j } ( t ) + a ^ { i } \sum _ { A } m _ { A } x _ { A } ^ { j } ( t ) + a ^ { j } \sum _ { A } m _ { A } x _ { A } ^ { i } ( t ) + a ^ { i } a ^ { j } \sum _ { A } m _ { A } ,
$$

so its value depends on the choice of the origin. However

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \dot { M } ^ { i j }  \dot { M } ^ { i j } + a ^ { i } \sum _ { A } m _ { A } \dot { x } _ { A } ^ { j } + a ^ { j } \sum _ { A } m _ { A } \dot { x } _ { A } ^ { i } } } \\ { { } } & { { } } & { { \displaystyle = \dot { M } ^ { i j } + a ^ { i } P _ { \mathrm { t o t } } ^ { j } + a ^ { j } P _ { \mathrm { t o t } } ^ { i } , } } \end{array}
$$

where $\begin{array} { r } { P _ { \mathrm { t o t } } ^ { i } = \sum _ { A } m _ { A } \dot { x } _ { A } ^ { i } } \end{array}$ is thetotal momentum ofthe (non-relativistic) system. For a closed system, $ { \lvert { P _ { \mathrm { t o t } } ^ { i } } \rvert } _ { }$ is constant and therefore $\ddot { M } ^ { i j }$ is invariant.Since $h _ { i j } ^ { \mathrm { T T } }$ dependsonthesecondtimedervativeof $M _ { i j }$ ,the gravitational radiation is not affected by a shift of the origin,as it should be, since $h _ { i j } ^ { \mathrm { T T } }$ (asnytherfeldinaneldtheoryissarer translations.It is important,however,that we have a closed system where all particles have been included,and no external force is present. In the presence of external forces,the energy-momentum tensor of matter is not conserved,or equivalently the multipole moments and all their time derivatives depend on the|choice of the origin of the coordinate system,and the whole formalism that we have developed is not consistent.

However, the procedure of taking a given trajectory ${ \bf x } _ { 0 } ( t )$ ，plugging it into eq.(3.12O),and computing the corresponding GW production, becomes correct when $\mathbf { x } _ { 0 }$ isthe relative coordinate of an isolated twobody system in the center-of-mass frame,and ${ \bf x } _ { 0 } ( t )$ is the actual time evolution of $\mathbf { x } _ { 0 }$ ,as determined by the mutual interaction between the two bodies.To understand this point,we defne as usual the center-of-mass coordinate by

$$
\mathbf { x } _ { \mathrm { C M } } = { \frac { m _ { 1 } \mathbf { x } _ { 1 } + m _ { 2 } \mathbf { x } _ { 2 } } { m _ { 1 } + m _ { 2 } } } ,
$$

and the relative coordinate ${ \bf x } _ { 0 } = { \bf x } _ { 1 } - { \bf x } _ { 2 }$ ,and we denote by $m = m _ { 1 } + m _ { 2 }$ the total mass and by $\mu = m _ { 1 } m _ { 2 } / m$ the reduced mass.Then,for a nonrelativistic system, the second mass moment can be written as

$$
\begin{array} { r l } & { M ^ { i j } = m _ { 1 } x _ { 1 } ^ { i } x _ { 1 } ^ { j } + m _ { 2 } x _ { 2 } ^ { i } x _ { 2 } ^ { j } } \\ & { \qquad = m x _ { \mathrm { { C M } } } ^ { i } x _ { \mathrm { { C M } } } ^ { j } + \mu ( x _ { \mathrm { { C M } } } ^ { i } x _ { 0 } ^ { j } + x _ { \mathrm { { C M } } } ^ { j } x _ { 0 } ^ { i } ) + \mu x _ { 0 } ^ { i } x _ { 0 } ^ { j } . } \end{array}
$$

Therefore,if (and only if) we choose the prigin of the coordinate system at $\mathbf { x } _ { \mathrm { C M } } = 0$ ，the quadrupole moment becomes the same as that of a particle of mass $\mu$ described by the coordinate $x _ { 0 } ( t )$ .If we rather opt for an origin with non-vanishing $\mathbf { x } _ { \mathrm { C M } }$ ,then the first term in eq.(3.127) isa constant and does not contribute to the production of gravitational radiation,but the second is non-vanishing and time-dependent,since $\boldsymbol { z } = \boldsymbol { x } _ { 0 } ( t )$ ,and therefore contributes.

Thus,if we describe the system using $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ ,we can fix the origin f the reference frame at will,since $P _ { \mathrm { { t o t } } } ^ { i }$ is conserved,and therefore the quadrupole moment is invariant under $\mathtt { a }$ shift $x ^ { i }  x ^ { i } + a ^ { i }$ .Alternatively,we canadopt the CM point of view,and we are left witha single effective particle of mass $\mu$ and coordinate $x _ { 0 } ^ { i } ( t )$ .This is formally identical to working with $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ ,so it isa consistent and correct way of computing GW production.However, in this case we no longer have the freedom to shift the origin of the reference frame,since this description bs only valid in the CM frame,where $\mathbf { x } _ { \mathbb { C } \mathrm { M } } = 0$ .In the CM frame,the mass density is then

$$
\rho ( t , \mathbf { x } ) = \mu \delta ^ { ( 3 ) } \left( \mathbf { x } - \mathbf { x } _ { 0 } ( t ) \right) ,
$$

he second mass moment is

$$
M ^ { i j } ( t ) = \mu x _ { 0 } ^ { i } ( t ) x _ { 0 } ^ { j } ( t ) ,
$$

Ind the mass quadrupole is

$$
Q ^ { i j } ( t ) = \mu \left( x _ { 0 } ^ { i } ( t ) x _ { 0 } ^ { j } ( t ) - { \frac { 1 } { 3 } } r _ { 0 } ^ { 2 } ( t ) \delta ^ { i j } \right) .
$$

llaving understood this point,it makes sense to ask about the radiation mitted by a two-body system whose relative coordinate performs a iven periodic motion,say simple harmonic oscillations.Suppose that the relative coordinate ${ \bf x } _ { 0 } ( t )$ performs $\mathrm { \AA }$ simple periodic motion with quency Ws,say along thez direction,6

$^ { 2 6 } \mathrm { { I n } }$ a one-dimensional motionthisexample would be quite unrealistic,since the two bodies would go through each other whenever $\cos { \omega _ { s } t } ~ = ~ 0$ However,this is just an example to illustrate what happens to a typical oscillatory mode of a system.For instance, one can consider an elliptic motion on a plane,which is the combination of two simple oscillations along the two axes.

Then

$$
\begin{array} { c } { { } } \\ { { z _ { 0 } ( t ) = a _ { 1 } \cos \omega _ { s } t . } } \\ { { } } \\ { { { \cal M } ^ { i j } ( t ) = \delta ^ { i 3 } \delta ^ { j 3 } \mu z _ { 0 } ^ { 2 } ( t ) } } \\ { { = \displaystyle \delta ^ { i 3 } \delta ^ { j 3 } \frac { \mu a _ { 1 } ^ { 2 } } { 2 } \left( 1 + \cos 2 \omega _ { s } t \right) . } } \end{array}
$$

Since the GW amplitude depends on the second derivative of $M ^ { i j }$ ,the $h _ { i j } ^ { \mathrm { r I I } }$ comes from the term proportional to $\cos 2 \omega _ { s } t$ .From eq.(3.55)，we see that the corresponding waveform $h _ { i j } ^ { \mathrm { T T } }$ oscillates as $\cos { 2 \omega _ { s } t }$ This shows that a non-relativistic source performing simple harmonic oscilations with a frequency $\omega _ { s }$ emits monochromatic quadrupole radiation at $\omega =$ $2 \omega _ { s }$

However,the fact that the quadrupole radiation is at twice the source frequency is only true if the source performs a simple harmonic motion. For instance,if the motion of the source is a superposition of a periodic motion and of its higher harmbnics,e.g.if

$$
\begin{array} { r } { z _ { 0 } ( t ) = a _ { 1 } \cos { \omega _ { s } t } + a _ { 2 } \cos { 2 \omega _ { s } t } + \dots , } \end{array}
$$

then $z _ { 0 } ^ { 2 } ( t )$ contains the term

$$
a _ { 1 } ^ { 2 } \cos ^ { 2 } \omega _ { s } t = a _ { 1 } ^ { 2 } \frac { 1 + \cos 2 \omega _ { s } t } { 2 } ,
$$

considered above,plus a term

$$
a _ { 2 } ^ { 2 } \cos ^ { 2 } 2 \omega _ { s } t = a _ { 2 } ^ { 2 } \frac { 1 + \cos 4 \omega _ { s } t } { 2 } ,
$$

which gives radiation at $\omega _ { \mathrm { g w } } = 4 \omega _ { s }$ ,etc., but also mixed terms such as

$$
2 a _ { 1 } a _ { 2 } \cos ( \omega _ { s } t ) \cos ( 2 \omega _ { s } t ) = a _ { 1 } a _ { 2 } ( \cos \omega _ { s } t + \cos 3 \omega _ { s } t ) .
$$

Therefore in this case quadrupole radiation is emitted at all frequencies $n \omega _ { s }$ for all integers $n$ ,both even and odd,including $n = 1$ Wewill see an example of this type in Section 4.1.2,when we study the radiation emitted from a mass in a Keplerian elliptic orbit.

An even simpler example is given by a system of two masses connected bya spring with rest length $L$ (see Problem 3.1).In this case the relative coordinate satisfies

$$
z _ { 0 } ( t ) = L + a \cos { \omega _ { s } t } ,
$$

and in $z _ { 0 } ^ { 2 } ( t )$ ,besides a constant and a term $( a ^ { 2 } / 2 ) \cos 2 \omega _ { s } t$ ,we also have a term $2 L a \cos \omega _ { s } t$ ，so the spectrum of gravitational radiation has two lines,one at $\omega = \omega _ { s }$ ,and one at $\omega = 2 \omega _ { s }$ .As we have discussed above, the whole procedure of computing GWs from a source on a preassigned trajectory $z _ { 0 } ( t )$ is consistent only if $z _ { 0 } ( t )$ is a relative coordinate in the center-of-mass frame.Therefore we do not have the freedom to shift the origin of the coordinate system,which otherwise would allow us to eliminate $L$

# 3.4Mass octupole and current quadrupole

We now examine the next-to-leading term of the expansion (3.34),

$$
\left( h _ { i j } ^ { \mathrm { T T } } \right) _ { \mathrm { n e x t - t o - l e a d i n g } } = \frac { 1 } { r } \frac { 4 G } { c ^ { 5 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) n _ { m } \dot { S } ^ { k l , m } ( t - r / c ) .
$$

By definition $\dot { S } ^ { k l , m }$ is symmetric in $k l$ ,and it has no special symmetry with respect to the exchange of $k$ with $m$ .We have seen in eq. (3.54) that

$$
\dot { S } ^ { k l , m } = \frac 1 6 \dddot { M } ^ { k l m } + \frac 1 3 \left( \ddot { P } ^ { k , l m } + \ddot { P } ^ { l , k m } - 2 \ddot { P } ^ { m , k l } \right) .
$$

Therefore $\dot { S } ^ { k l , m }$ separates into a totally symmetric tensor $\ddot { M } ^ { k l m }$ plus a tensor with mixed symmetry. The meaning of this separation from the point of view of group theory is explained in Problem3.4,in the Solved Problems section. The totally symmetric term generates mass octupole radiation，while the term with mixed symmetry is called the current quadrupole.

# Mass octupole

We consider frst te massoctupole radjation. The mass octupole Oklm is defined removing all traces from $M ^ { i j k }$ ，

$$
\mathcal { O } ^ { k l m } = M ^ { k l m } - \frac { 1 } { 5 } \left( \delta ^ { k l } M ^ { k ^ { \prime } k ^ { \prime } m } + \delta ^ { k m } M ^ { k ^ { \prime } l k ^ { \prime } } + \delta ^ { l m } M ^ { k k ^ { \prime } k ^ { \prime } } \right) .
$$

Using the fact that $\Lambda _ { i j , k l } ( \hat { \mathbf { n } } )$ is transverse and traceless,we see that the contraction of the trace part with $\Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) n _ { m }$ gives zero,and we can use $M ^ { k l m }$ or $\mathcal { O } ^ { k l m }$ interchangeablyinteexpesionfor $h _ { i j } ^ { \mathrm { T T } }$ Therefore the mas ctupoleontribution to $h _ { i j } ^ { \mathrm { T T } }$ can be written as

$$
\left( h _ { i j } ^ { \mathrm { T T } } \right) _ { \mathrm { o c t } } = \frac 1 r \frac { 2 G } { 3 c ^ { 5 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) n _ { m } \ddot { \mathcal { O } } ^ { k l m } .
$$

Similarly to the case of quadrupole radiation,the use of $\mathcal { O } ^ { k l m }$ is nicer from a group-theoretical point of view,since it is a pure spin-3 tensor, see Problem 3.4,while theuse of $M ^ { i j k }$ is simpler in actual computations. We will use $\ddot { M } ^ { k l m }$ and $\ddot { \mathcal { O } } ^ { k l m }$ interchangeably in eq. (3.141).

Observe that， when we consider quantities quadratic in $h _ { i j } ^ { \mathrm { T T } }$ ,as for instance the radiated energy,there is ${ \mathrm { n } o } \mathrm { , }$ interference between the mass quadrupoleand the mass octupole terms because they have different parity.Underaparity operation, ${ \bf x }  - { \bf x } .$ the mass density is a true scalar, and therefore the quadrupole is invariant while the octupole changes ign (for the same reason,in electrodynamics there is no interference between dipole and quadrupole radiation.）More generally,wewill see n Section 3.5 how to systematicaily organize the multipole expansion $3 0$ that there are no interference terms to all orders.

Comparing the mass quadrupole and the mass octupole we see that, while the contribution to the GW amplitude from the mass quadrupole is proportional to the second time derivative of $M ^ { i j }$ ，the contribution from the mass octupole is proportional to $( 1 / c )$ times the third time derivative of $M ^ { i j k }$ .If $d$ is the typical dimension of the source,the tensor $M ^ { i j k }$ differ from $M ^ { i j }$ by a factor $O ( d )$ .Each time derivative carries a factor $O ( \omega _ { s } )$ ，where $\omega _ { s }$ is the typical frequency of the movement of matter inside the source,so $( 1 / c ) \ddot { \vec { M } } ^ { i j k } = O ( \omega _ { s } d / c ) \ddot { \vec { M } } ^ { i j }$ Since $\omega _ { s } d \sim v$ isthetypicalvelcityinsidethesourcetheoctupolecontributioto $h _ { i j } ^ { \mathrm { T T } }$ is smaller than the quadrupole contribution by a factor $O ( v / c )$ ,and the contribution of the mass octupole to the radiated power is smaller than the contribution of the mass qyadrupole by a factor $O ( v ^ { 2 } / c ^ { 2 } )$

Consider now a two-body noh-relativistic system whose relative coordinate in the center-of-mass frame is described by a function $x _ { 0 } ^ { i } ( t )$ ,and has a reduced mass $\mu$ .Then,similarly to eq.(3.129),to lowest order in $v / c$ (e.g. replacing $T ^ { 0 0 } / c ^ { 2 }$ with the mass density),we have

$$
M ^ { i j k } ( t ) = \mu x _ { 0 } ^ { i } ( t ) x _ { 0 } ^ { j } ( t ) x _ { 0 } ^ { k } ( t ) .
$$

Suppose now that $x _ { 0 } ( t )$ performs simple harmonic oscillations with frequency $\omega _ { s }$ .Then,each factor $x _ { 0 } ^ { i } ( t )$ is the superposition of a term oscillating as $e ^ { i \omega _ { s } t }$ and of a term oscillating as $e ^ { - i \omega _ { s } t }$ ，s0 $M ^ { i j k }$ is the sum of terms oscillating as $e ^ { \pm i \omega _ { s } t }$ and of terms oscillating as $e ^ { \pm 3 i \omega _ { s } t }$ There fore a source performing simple harmonic oscillations at a frequency $\omega _ { s }$ emits octupole radiation at $\omega = \omega _ { s }$ and at $\omega = 3 \omega _ { s }$

If a non-relativistic source performs simple harmonic oscillations,then its energy spectrum is made of a stronger line due to quadrupole radiation at $\omega = 2 \omega _ { s }$ ，plus two smaller“lateral bands”due to the octupole at w= ωg and at ω= 3ws,as we will see in more detail in Problem 3.3. Recall however from Section $\$ 3.5$ that periodic trajectories that are not simple harmonic motions produce a more complicated spectrum,in whichtheadletelle all integer $n$

The power emitted per unit solid angle by the octupole moment is computed inserting $\dot { h } _ { i j } ^ { \mathrm { T T } }$ ,obtained fromeq. (3.141),into the epson for the power given in eq.(1.153). This gives

$$
\begin{array} { l } { { \displaystyle P _ { \mathrm { o c t } } = \frac { c ^ { 3 } r ^ { 2 } } { 3 2 \pi G } \int d \Omega \langle ( \dot { h } _ { i j } ^ { \mathrm { T T } } ) _ { \mathrm { o c t } } ( \dot { h } _ { i j } ^ { \mathrm { T T } } ) _ { \mathrm { o c t } } \rangle } } \\ { { \displaystyle \quad = \frac { c ^ { 3 } } { 3 2 \pi G } \frac { 4 G ^ { 2 } } { 9 c ^ { 1 0 } } \langle \frac { d ^ { 4 } O ^ { k l m } } { d t ^ { 4 } } \frac { d ^ { 4 } \mathcal { O } ^ { k ^ { \prime } l ^ { \prime } m ^ { \prime } } } { d t ^ { 4 } } \rangle \int d \Omega \Lambda _ { i j , k l } \Lambda _ { i j , k ^ { \prime } l ^ { \prime } } n _ { m } n _ { m ^ { \prime } } . } } \end{array}
$$

Using the property (1.37) of the Lambda tensor,together with $\Lambda _ { i j , k l } =$ $\Lambda _ { k l , i j }$ ,we have $\dot { \Lambda _ { i j , k l } } \dot { \Lambda _ { i j , k ^ { \prime } l ^ { \prime } } } = \dot { \Lambda } _ { k l , k ^ { \prime } l ^ { \prime } }$ . Then,renaming the indices,we get

$$
P _ { \mathrm { o c t } } = \frac { G } { 7 2 \pi c ^ { 7 } } \langle \frac { d ^ { 4 } \mathcal { O } ^ { i j m } } { d t ^ { 4 } } \frac { d ^ { 4 } \mathcal { O } ^ { k l p } } { d t ^ { 4 } } \rangle \int d \Omega \Lambda _ { i j , k l } \bigl ( \hat { \mathbf { n } } \bigr ) n _ { m } n _ { p } .
$$

To integrate over the solid angle we need the identities (3.21)and (3.22), together with eq.(3.23) with $l = 3$ ，

$$
\int \frac { d \Omega } { 4 \pi } n _ { i } n _ { j } n _ { k } n _ { l } n _ { m } n _ { p } = \frac { 1 } { 1 0 5 } ( \delta _ { i j } \delta _ { k l } \delta _ { m p } + \ldots ) ,
$$

where the dots denote the other 14 possible pairings of indices.Using the fact that $\mathcal { O } ^ { i j k }$ is totally symmetric and traceless,the contractions are straightforward,and we get

$$
P _ { \mathrm { o c t } } = \frac { G } { 1 8 9 c ^ { 7 } } \langle \frac { d ^ { 4 } \mathcal { O } ^ { i j k } } { d t ^ { 4 } } \frac { d ^ { 4 } \mathcal { O } ^ { i j k } } { d t ^ { 4 } } \rangle .
$$

# Current quadrupole

The current quadrupole is given by the second term in eq. (3.139).Its physical meaning can be understood observing that,from the definition (3.41),

$$
\begin{array} { l } { { \displaystyle P ^ { k , l m } + P ^ { l , k m } - 2 P ^ { m , k l } } } \\ { { \displaystyle = \frac 1 c \int d ^ { 3 } x \left[ T ^ { 0 k } x ^ { l } x ^ { m } + T ^ { 0 l } x ^ { k } x ^ { m } \right] - 2 T ^ { 0 m } x ^ { k } x ^ { l } \big ] } } \\ { { \displaystyle = \frac 1 c \int d ^ { 3 } x \left[ x ^ { l } ( x ^ { m } T ^ { 0 k } - x ^ { k } T ^ { 0 m } ) + x ^ { k } ( x ^ { m } T ^ { 0 l } - x ^ { l } T ^ { 0 m } ) \right] } } \\ { { \displaystyle = \int d ^ { 3 } x \left[ x ^ { l } j ^ { m k } + x ^ { k } j ^ { m l } \right] , } } \end{array}
$$

where

$$
j ^ { j k } = \frac 1 c \left( x ^ { j } T ^ { 0 k } - x ^ { k } T ^ { 0 j } \right) .
$$

This is the angular momentum density associated to the $( j , k )$ plane. We write $~ j ^ { j k } = \epsilon ^ { j k l } j ^ { l }$ ，where $j ^ { l }$ is the $\textit { i }$ -th component of the angular momentum density vector,and we define

$$
J ^ { i , j } = \int d ^ { 3 } x j ^ { i } x ^ { j } ,
$$

S0 $J ^ { i , j }$ is the first moment of the angular momentum density (i.e. the lipole moment of the angular momentum distribution). Then we get

$$
\begin{array} { r } { P ^ { k , l m } + P ^ { l , k m } - 2 P ^ { m , k l } = \epsilon ^ { m k p } J ^ { p , l } + \epsilon ^ { m l p } J ^ { p , k } . } \end{array}
$$

Therefore the current quadrupole is the first moment of the angular momentum density of the source,symmetrized over the indices $k , l$ Its contribution to the GW amplitude can be written as

$$
\left( h _ { i j } ^ { \mathrm { T T } } \right) _ { \mathrm { c u r r \ q u a d } } = \frac 1 r \frac { 4 G } { 3 c ^ { 5 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) n _ { m } \left( \epsilon ^ { \eta a k p } J ^ { p , l } + \epsilon ^ { m l p } J ^ { p , k } \right) .
$$

We willideed see in the next section that the full multipole expansion can be organized systematically so that it is determined by two types ofobjects:the momenta of the energy density of the source (which,to leading order in $v / c$ ,are the same as the momenta of the mass density), ike the mass quadrupole $Q ^ { i j }$ ，the mas\$ octupole $\mathcal { O } ^ { i j k }$ ,etc.，and the momenta of the angular momentum dersity of the source,such as the mrent quadrupole.

The power associated to the|current quadrupole is computed just as we have done for the mass quadrupole and mass octupole: we write

$$
\begin{array} { l } { \displaystyle P _ { \mathrm { c u r r ~ q u a d } } = \frac { c ^ { 3 } r ^ { 2 } } { 3 2 \pi G } \int d \Omega \langle ( \dot { h } _ { i j } ^ { \mathrm { T T } } ) _ { \mathrm { c u r r ~ q u a d } } ( \dot { h } _ { i j } ^ { \mathrm { T T } } ) _ { \mathrm { c u r r ~ q u a d } } \rangle } \\ { \displaystyle = \frac { c ^ { 3 } } { 3 2 \pi G } \frac { 1 6 G ^ { 2 } } { 9 c ^ { 1 0 } } \int d \Omega \Lambda _ { k l , k ^ { \prime } l ^ { \prime } } n _ { m } n _ { m ^ { \prime } } } \\ { \displaystyle \qquad \times \langle \left( \epsilon ^ { m k p } J ^ { p , l } + \epsilon ^ { m l p } J ^ { p , k } \right) \left( \epsilon ^ { m ^ { \prime } k ^ { \prime } p ^ { \prime } } J ^ { p ^ { \prime } , l ^ { \prime } } + \epsilon ^ { m ^ { \prime } l ^ { \prime } p ^ { \prime } } J ^ { p ^ { \prime } , k ^ { \prime } } \right) \rangle , } \end{array}
$$

where we used again $\Lambda _ { i j , k l } \Lambda _ { i j , k ^ { \prime } l ^ { \prime } } = \Lambda _ { k l , k ^ { \prime } l ^ { \prime } }$ . The angular integration is performed using the identities (3.21） and (3.22). Observe also that the term in the Lambda tensor with four factors of $_ n$ ，i.e. $n _ { k } n _ { l } n _ { k ^ { \prime } } n _ { l ^ { \prime } }$ (see eq.(1.39)) does not contribute since,together with the factors $n _ { m } n _ { m ^ { \prime } }$ in eq. (3.152),it gives a totally symmetric tensor $n _ { k } n _ { l } n _ { m } n _ { k ^ { \prime } } n _ { l ^ { \prime } } n _ { m ^ { \prime } }$ ,which vanishes upon contraction with $\epsilon ^ { m k p }$ or $\epsilon ^ { m l p }$

When performing contractions,we also make use of the fact that $\mathbf { \mathcal { J } } ^ { i , j }$ is traceless,since

$$
\begin{array} { l } { { \displaystyle { J ^ { i , i } = \int d ^ { 3 } x x ^ { i } j ^ { i } } } } \\ { { \displaystyle ~ = \frac { 1 } { c } \int d ^ { 3 } x x ^ { i } \epsilon ^ { i j k } x ^ { j } T ^ { 0 k } = 0 } } \end{array}
$$

(the sum over $_ i$ is understood)|Then, we get

$$
P _ { \mathrm { c u r r ~ q u a d } } = \frac { 1 6 G } { 4 5 c ^ { 7 } } \langle \ddot { \mathcal { I } } ^ { i j } \ddot { \mathcal { T } } ^ { i j } \rangle ,
$$

where we introduced the traceless symmetric matrix

$$
{ \mathcal { I } } ^ { i j } \equiv { \frac { J ^ { i , j } + J ^ { j , i } } { 2 } } ,
$$

that is, the symmetrization of the dipole moment of the angular momentum density. Putting together the power radiated by the mass quadru-pole,current quadrupole and mass octupole,we therefore get

$$
\begin{array} { l } { \displaystyle P = \frac { G } { c ^ { 5 } } \left[ \frac { 1 } { 5 } \langle \dddot { Q } _ { i j } \dddot { Q } _ { i j } \rangle + \frac { | 1 } { c ^ { 2 } } \frac { 1 6 } { 4 5 } \langle \dddot { \mathcal T } _ { i j } \dddot { \mathcal T } _ { i j } \rangle \right. } \\ { \displaystyle \left. + \frac { 1 } { c ^ { 2 } } \frac { 1 } { 1 8 9 } \langle \frac { d ^ { 4 } { \mathcal O } _ { i j k } } { d t ^ { 4 } } \frac { d ^ { 4 } { \mathcal O } _ { i j k } } { d t ^ { 4 } } \rangle + O \left( \frac { v ^ { 4 } } { c ^ { 4 } } \right) \right] , } \end{array}
$$

where $O ( v ^ { 4 } / c ^ { 4 } )$ denotes the cortributions from higher orders in the multipole expansion. In this formula,one must be careful to include in $Q _ { i j }$ also its first corrections $O ( v ^ { 2 } / c ^ { 2 } )$ ，since it gives a contribution to the power of the same order as that due to the mass octupole and current quadrupole. This means that $\phi _ { i j }$ here is not simply the quadrupole of the mass distribution.Rather,we must go back to its original definition in terms of $T ^ { 0 0 }$ ,see eq. (3.37) and include in $T ^ { 0 0 }$ not only the terms of order $\rho c ^ { 2 }$ ,where $\rho$ is the mass density,but also the terms of order $\rho v ^ { 2 }$ Furthermore, the time-dependence of the leading term must be computed using the relativistic equations of motion, including corrections upto $O ( v ^ { 2 } / c ^ { 2 } )$

It is quite diffcult to imagine a realistic physical system for which the time derivative of the mass quadrupole vanishes,but still the mass octupole is time-varying.For this reason,the mass octupole isalways a correction to the leading term.However, there are interesting physical situations where both the mass quadrupole and the mass octupole are constant in time and therefore do not contribute to GW production, while the current quadrupole still contributes,so it becomes the leading term. To have $M ^ { i j }$ and $M ^ { i j k }$ constant,infct,itsufes thattheeergy density $T ^ { 0 0 }$ be constant. Then all the mass momenta are constant,see cg.eqs.(3.35)-(3.38). Still，, the angular momentum density and its momenta,such as its dipole $J ^ { i , j }$ ,are not necessarily constant.Consider for example a ring in the $( x , y )$ plane with a uniform mass density $\rho$ ， rotating around the $z$ axis.Even if any single volume element of the ring rotates, this rotation does not induce any temporal variation in the density $\rho$ since the ring is spatially uniform,so all mass moments are constant.27 However, this ring has non-vanishing angular momentum along z.To obtain a system with a dipole moment of angular momentum $5 ^ { i , j }$ , we can simply take two rings, both rotating around the $z$ axis,but one counterclockwise and one clockwise,as in Fig. 3.3. The upper ring has a positive $J ^ { z }$ while the lower one has a negative $J ^ { z }$ ,so it is clear at the whole system has a non-vanishing dipole moment Jz,z.28

If the rotational velocities of the rings are not constant, this dipole moment of the angular momentum is time-dependent.A physical example of a system of this type is provided by the torsional oscillations maneutron star.It is possible that,either because of some external perturbation,or because of a“corequake”,the upper hemisphere of a NS nflers a clockwise torsion while the lower hemisphere receives a counterlockwise torsion (with the equator which,by symmetry reasons,stays fixed).Then the two hemispheres will start oscillating back and forth in oposite directions,so that when one rotates clockwise the other rotates counterclockwise,and vice versa.This system will then emit current quadrupole radiation,but not mass quadrupole nor mass octupole radiation.Another important example of this type is the $r$ -mode of neutron tars.which will be discussed in Vol. 2.

It is therefore worthwhile to study the current quadrupole radiation in more detail,and derive its angular distribution. First,we compute the mplitude of the GWs radiated in the $\ngeq$ direction. This is quite simple, ce we just have to substitute $n = ( 0 , 0 , 1 )$ into eq. (3.151).Using the xplicit expression for the Lambda tensor,eq. (1.39),and recalling that, a wave traveling along $z$ ， $h _ { 1 1 } = h _ { + }$ and $h _ { 1 2 } = h _ { \times }$ ，we obtain

27One might wonder howit isposible that there is no quadrupole radiation from the whole ring，given that every single mass element is inrotation and therefore radiates GWs.From this “microscopic”point of view,the answer is that the total amplitude is the sum over the contribution of all the mass elements,and these contributions interfere destructively,so that the total GW amplitude $h _ { i j }$ vanishes.

$^ { 2 8 } \mathrm { { I t } }$ also has a non-zero $J ^ { x , x }$ and $J \mathcal { Y } , \mathcal { Y }$ (consistent with the condition $\begin{array} { r l } { J ^ { i , i } = } & { { } } \end{array}$ 0).This can be seen by drawing the direction of the angular momentum vector ${ \delta { \bf { J } } } ~ = ~ ( \delta m ) { \bf { r } } \times { \bf { v } }$ of various mass elements，where $\mathbf { r }$ is measured from the origin of the coordinate system,see Fig.3.3.We see for instance that both the infinitesimal mass elements labeled $a$ and $c$ have $J ^ { y } < 0$ and are at a coordinate $y > 0$ ,therefore their contribution to $J ^ { y , y }$ is negative.Similarly,for the mass elements $b$ and $d$ we have $J ^ { y } > 0$ ， but they have a coordinate $y < 0$ so their contribution to $J ^ { y , y }$ is again negative.

$$
\begin{array} { l } { \displaystyle h _ { + } = \frac { 1 } { r } \frac { 4 G } { 3 c ^ { 5 } } \left( \ddot { J } _ { 1 , 2 } + \ddot { J } _ { 2 , 1 } \right) , } \\ { \displaystyle h _ { \times } = \frac { 1 } { r } \frac { 4 G } { 3 c ^ { 5 } } \left( \ddot { J } _ { 2 , 2 } - \ddot { J } _ { 1 , 1 } \right) . } \end{array}
$$

To obtain the amplitudes $h _ { + }$ ahd $h _ { \times }$ for a GW propagating into an arbi trary direction,we proceed as we did for the mass quadrupole,betweel eqs.(3.67) and (3.72).We first write

$$
\begin{array} { l } { \displaystyle h _ { + } = \frac { 1 } { r } \frac { 4 G } { 3 c ^ { 5 } } \left( \ddot { J } _ { 1 , 2 } ^ { \prime } + \ddot { J } _ { 2 , 1 } ^ { \prime } \right) , } \\ { \displaystyle h _ { \times } = \frac { 1 } { r } \frac { 4 G } { 3 c ^ { 5 } } \left( \ddot { J } _ { 2 , 2 } ^ { \prime } - \ddot { J } _ { 1 , 1 } ^ { \prime } \right) , } \end{array}
$$

![](images/6c0f87faf59cf32774b82d79bafb836dbe5f7fb978310616b86f24b6386bf941.jpg)  
Fig.3.3 Two rings,both with uniform mass density，one rotating counterclockwise and one clockwise. The arrows show the direction of the angular momentum $\delta \mathbf { J } = ( \delta m ) \mathbf { r } \times \mathbf { v }$ (with r measured from the origin of the coordinate system,rather than from the center of each disk) of four infinitesimal mass elements,labeled $a , b , c , d$

where $J _ { i , j } ^ { \prime }$ are the components of the angular momentum dipole in the $( \hat { \mathbf { u } } , \hat { \mathbf { v } } , \hat { \mathbf { n } } )$ frame defined in Fig3.2.Since $J _ { i , j }$ is a spatial tensor with two indices,it transforms under rotation just as we found for $M _ { i j }$ in eq. (3.71), i.e. $J _ { i , j } ^ { \prime } = \mathcal { R } _ { k i } \mathcal { R } _ { l j } J _ { k , l }$ ，with $\mathcal { R }$ given by eq. (3.70).Performing the matrix multiplication, we get

$$
\begin{array} { l } { { { \displaystyle { \bar { h } } _ { + } ( \{ { \dot { \gamma } } , \dot { \theta } } , \dot { \theta } ) \Bigr \} _ { \mathrm { o u r \ \ \ q a i n } } = \frac { 1 } { \tau } \frac { 4 G } { 3 \mathcal { E } _ { \sigma } ^ { 2 } } \Big \{ \ ( { \bar { J } } _ { 1 1 } , - { \bar { J } } _ { 2 2 } ) \sin { 2 \phi } \cos { \theta } } } \\ { ~ + ( { \bar { J } } _ { 1 2 } , + { \bar { J } } _ { 2 1 } ) \cos { 2 \phi } \cos { \theta } } \\ { ~ - ( { \bar { J } } _ { 1 3 } , + { \bar { J } } _ { 3 1 } ) \cos { \phi } \sin { \theta } ~ } \\ { ~ + ( { \bar { J } } _ { 2 3 } , + { \bar { J } } _ { 3 2 } ) \sin { \theta } \sin { \theta } ~ } \\ { { \displaystyle { \bar { h } } _ { \times } ( \{ \dot { \gamma } } , \dot { \theta } ) \Bigr \} _ { \mathrm { l o r \ \ \ q a i n } } = \frac { 1 } { \tau } \frac { 4 G } { 3 \mathcal { E } _ { \sigma } ^ { 3 } } \Big \{ - { \bar { J } } _ { 1 4 } ( \cos ^ { 2 } { \phi } - \sin ^ { 2 } { \phi } \cos ^ { 2 } { \theta } ) }  \\ { ~ - { \bar { J } } _ { 2 2 } ( \sin ^ { 2 } { \phi } - \cos ^ { 2 } { \phi } \cos ^ { 2 } { \theta } ) } \\ { ~ + { \bar { J } } _ { 3 3 } \sin ^ { 2 } { \theta } } \\ { ~ + ( { \bar { J } } _ { 1 4 } , + { \bar { J } } _ { 2 1 } ) \sin { \phi } \cos { \theta } ( 1 + \cos ^ { 2 } { \theta } ) } \\ { ~ - ( { \bar { J } } _ { 3 3 } + { \bar { J } } _ { 3 1 } ) \sin { \phi } \cos { \theta } ~ } \\ { ~ - ( { \bar { J } } _ { 3 4 } , + { \bar { J } } _ { 3 2 } ) \cos { \phi } \cos { \theta } ~ ( 3 . 1 ) } \end{array}
$$

29Comparing with eq. (3.72) we see that the angular dependence is the same as for the mass quadrupole, if we replace $M _ { i j }$ by $J _ { i , j }$ ,and we exchange the roles of $h _ { + }$ and $h _ { \times }$ (with an additional minus sign for (hx)curr quad· This wasalready clear from a comparison of eqs.(3.157)and(3.158)with eqs.(3.65)and (3.66),and from the fact that both $M _ { i j }$ and $J _ { i , j }$ transform as rank-2 tensors under rotations.

This gives the angular distribution of the current quadrupole radiation,29 for $J ^ { i , j }$ arbitrary (but satisfying the zero-trace condition $J _ { 1 , 1 } + J _ { 2 , 2 } +$ ${ { J } _ { 3 , 3 } } = 0$ ).To check these equations we can plug them into the expression (1.154) for the angular distribution of the power in terms of $h _ { + }$ and $h _ { \times }$

$$
{ \frac { d P } { d \Omega } } = { \frac { | c ^ { 3 } r ^ { 2 } } { 1 6 \pi G } } \langle \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \rangle .
$$

Performing explicitly the integral over $d \Omega = d \phi d \theta | \sin \theta |$ , we verify that we get eq.(3.154) back.

# Linear momentum losses

Finally,it is interesting to observe that the leading term contributing to the loss of linear momentum comes from the interference between the quadrupole term and the next-to-leading term (i.e. the octupole plus current quadrupole). In fact, recall from eq.(1.164) that $d P ^ { k } / d t$ is proportional to

$$
\int d \Omega \dot { h } _ { i j } ^ { \mathrm { T T } } \partial _ { k } h _ { i j } ^ { \mathrm { T T } } .
$$

Using eqs. (3.59) and (3.138) we write

$$
\begin{array} { l } { { \displaystyle h _ { i j } ^ { \mathrm { T T } } = [ h _ { i j } ^ { \mathrm { T T } } ] _ { \mathfrak { q u a d } } + [ h _ { i j } ^ { \mathrm { T T } } ] _ { \mathfrak { n e x t - t o - l e a d i n g } } } } \\ { { \displaystyle ~ = \frac { 1 } { r } \frac { 2 G } { c ^ { 4 } } \left[ \ddot { Q } _ { i j } ^ { \mathrm { T T } } + \frac { 2 } { c } n _ { m } \dot { S } _ { i j , m } ^ { \mathrm { T T } } \right] } , } \end{array}
$$

where $\dot { S } _ { i j , m } ^ { \mathrm { T T } } = \Lambda _ { i j , k l } \dot { S } _ { k l , m }$ In the produet $\dot { h } _ { i j } ^ { \mathrm { T T } } \partial _ { k } h _ { i j } ^ { \mathrm { T T } }$ we have diagonal terms and interference terms between the quadrupole and the next-toleading term.The diagonal terms are proportional to

$$
\int d \Omega \ddot { Q } _ { i j } ^ { \mathrm { T T } } \partial _ { k } \ddot { Q } _ { i j } ^ { \mathrm { T T } } ,
$$

for the quadrupole,and to

$$
\int d \Omega \left( n _ { l } \ddot { S } _ { i j , l } ^ { \mathrm { T T } } \right) \partial _ { k } \left( n _ { m } \dot { S } _ { i j , m } ^ { \mathrm { T T } } \right) ,
$$

for the next-to-leading term. Because|of parity, these angular integrals vanish if the integrand is the product of an odd number of factors $n _ { i }$ Therefore,we need to count the number of $\hat { \bf n }$ in these expressions. The TT projection is performed with the Lambda tensor,which has an even number of factors $\hat { \bf n }$ ．As for the derivative $\partial _ { k }$ which appears in eqs.(3.166) and (3.167),recall that，on a function of $r$ $\partial _ { k } f ( r ) =$ $( \partial _ { k } r ) d f / d r \ = \ n ^ { k } d f / d r$ ，while $\partial _ { k } n ^ { i } = | \partial _ { k } ( x ^ { i } / r ) = ( 1 / r ) ( \delta ^ { i k } - n ^ { i } n ^ { k } )$ Therefore the effect of $\partial _ { k }$ is always to lower or to raise by one the number of factors $n ^ { i }$ ,i.e.to transform a term with an even number of $\hat { \bf n }$ in a terin with an odd number,and vice versa.

Then,we see that the diagonal terms in eqs. (3.166) and (3.167) have al od number of factors $\hat { \bf n }$ ，so their angular integral vanish.In the imterference terms,such as

$$
\int d \Omega \ddot { Q } _ { i j } ^ { \mathrm { T T } } \partial _ { k } \left( n _ { m } \dot { S } _ { i j , m } ^ { \mathrm { T T } } \right) ,
$$

the integrand is even in $\hat { \bf n }$ and in general is non-vanishing. So,while the mdiated energy only gets contributions from the diagonal terms (as we will verify to all orders in the multipole expansion in the next section), the radiated momentum only gets contributions from the interference between multipoles of different parity,in order to compensate for the minus sign acquired by the derivative $\partial _ { k }$ under $\hat { \bf n }  - \hat { \bf n }$

# 3.5 Systematic multipole expansion

ln eq. (3.34) the multipole expansion has been organized in terms of tensors such as $S ^ { k l }$ ， $\dot { S } ^ { k l , m }$ ， $\ddot { S } ^ { k l , m _ { 1 } m _ { 2 } }$ ,etcwhichhave two setsof indices separated by a comma),the first always made by two indices $k , l$ and the Econd made by a generic number of indices, $\displaystyle m _ { 1 } , \ldots , m _ { N }$ .These tensors are symmetric under the exchange of $k$ and $l$ ,and are also symmetric mder the exchange of indices in the $m _ { 1 } , \ldots , m _ { N }$ set.However,they have no special symmetry property under the exchange of indices betweenth two sets (and they are in general not traceless under contraction of pain of indices)．At next-to-leading order,we separated by hand the term $\dot { S } ^ { k l , m }$ into two contributions,one corresponding to massoctupole and one to current quadrupole. The reason underlying this separation i group-theoretical． As we discuss in Problem 3.4,this corresponds t a decomposition into irreducible representations of the rotation group To generalize such a construction to arbitrary orders in the multipole expansion,we must introduce a complete set of representations of the rotation group,for all multipoles. There are two particularly convenien ways of doing that. One is to consider tensors which are symmetri and trace-free (STF) with respect to all pairs of indices.This formalism will be introduced in Section 3.5.1,and we will use it extensively i particular in Chapter 5.A second possibility is to introduce the spherica components of tensors and the|tensor spherical harmonics,which is the approach that we discuss in Section 3.5.2

To illustrate these two diferent approaches,it can be useful to begin our discussion by recalling how the multipole expansion works in the simpler case of a static situation,governed by a Poisson equation of the form

$$
\nabla ^ { 2 } \phi = - 4 \pi \rho ,
$$

which would be the case,e.g.in electrostatics or in Newtonian gravity. We consider a stationary source with density $\rho ( \mathbf { x } )$ localized in space,so $\rho ( \mathbf { x } ) = 0$ if $r > d$ where $d$ is the source size. The most general solution in the external region $r > d$ can be written as

$$
\phi ( \mathbf { x } ) = 4 \pi \sum _ { l = 0 } ^ { \infty } \sum _ { m = - l } ^ { l } \frac { Q _ { l m } } { 2 l + 1 } \frac { Y _ { l m } ( \theta , \phi ) } { r ^ { l + 1 } } .
$$

In fact, for $r > 0$

$$
\nabla ^ { 2 } \left[ \frac { Y _ { l m } ( \theta , \phi ) } { r ^ { l + 1 } } \right] = 0 ,
$$

as can be seen immediately from the expression of the Laplacian in spherical coordinates,

$$
\nabla ^ { 2 } \psi ( \mathbf { x } ) = \frac { 1 } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial \psi } { \partial r } \right) - \frac { \mathrm { L } ^ { 2 } } { r ^ { 2 } } \psi ,
$$

together with the property $\mathbf { L } ^ { 2 } Y _ { l m } = l ( l + 1 ) Y _ { l m }$ of the spherical harmonics.Then,in the external region $r > d$ ,all terms in the sum in eq. (3.170) are separately solution of the vacuum equation $\nabla ^ { 2 } \phi = 0$ The fact that eq.(3.17O） is the most general vacuum solution follows from the fact that the spherical harmonics provide a complete set of representations of the rotation group. On the other hand,the solution of eq.(3.169) (subject to the boundary condition that $\phi$ approaches zero as $r \to \infty$ can be written in terms of the Green's function of the Laplacian, as

$$
\phi ( { \bf x } ) = \int d ^ { 3 } y \frac { 1 } { | { \bf x } - { \bf y } | } \rho ( { \bf y } ) ,
$$

which is valid both for x inside and outside the source.Outside the source we have $| \mathbf { x } | > | \mathbf { y } |$ ，and we can use the addition theorem for spherical harmonics30 in the form

$$
\frac { 1 } { | { \bf x } - { \bf y } | } = 4 \pi \sum _ { l = 0 } ^ { \infty } \sum _ { m = - l } ^ { l } \frac { 1 } { 2 l + 1 } { \frac { { r ^ { \prime } } ^ { l } } { r ^ { l + 1 } } } Y _ { l m } ^ { * } ( \theta ^ { \prime } , \phi ^ { \prime } ) Y _ { l m } ( \theta , \phi ) ,
$$

where we used the notation $| { \bf x } | = r$ and $| \mathbf { y } | = r ^ { \prime }$ ； $( \theta , \phi )$ are the polar angles of $\hat { \mathbf { x } }$ and $( \theta ^ { \prime } , \phi ^ { \prime } )$ of $\hat { \mathbf { y } }$ .Inserting this identity in eq. (3.173) and comparing with eq.(3.17O) we find the expression for the multipole coefficients $Q _ { l m }$ in terms of the source density $\rho ( \mathbf { x } )$ ，

$$
Q _ { l m } = \int d ^ { 3 } y Y _ { l m } ^ { * } ( \theta ^ { \prime } , \phi ^ { \prime } ) r ^ { \prime l } \rho ( { \bf y } ) .
$$

$\mathfrak { S } _ { 0 }$ eq. (3.170) gives the most general solution of the vacuum equation, and eq.(3.175) fixes thc coefficients $Q _ { l m }$ in terms of the density of the source.

An alternative way of performing the multipole expansion is to write

$$
\begin{array} { l } { { \displaystyle { \frac { 1 } { | \mathbf { x } - \mathbf { y } | } } = { \frac { 1 } { | \mathbf { x } | } } - y ^ { i } \partial _ { i } { \frac { 1 } { | \mathbf { x } | } } + { \frac { 1 } { 2 } } y ^ { i } y ^ { j } \partial _ { i } \partial _ { j } { \frac { 1 } { | \mathbf { x } | } } + \ldots } } \\ { { \displaystyle ~ = \sum _ { l = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { l } } { l ! } } y ^ { i _ { 1 } } \ldots y ^ { i _ { l } } \partial _ { i _ { 1 } } \ldots \partial _ { i _ { l } } { \frac { 1 } { | \mathbf { x } | } } . } } \end{array}
$$

We then make use of the fact that, for $r \not > 0$ ,and therefore in particular outside the source,we have $\nabla ^ { 2 } ( 1 / | \mathbf { x } | ) = 0$ ,as can be checked again from cq.(3.172).31 Then, in eq. (3.176) we can replace $y ^ { i } y ^ { j }$ with the traceless combination $y ^ { i } y ^ { j } - ( 1 / 3 ) \delta ^ { i j } | \mathbf { y } | ^ { 2 }$ ,and similarly we can remove all traces from the tensors $y ^ { i _ { 1 } } \ldots y ^ { i _ { l } }$ .Then,inserting eq.(3.176) into eq.(3.173), we get

$$
\phi ( { \bf x } ) = \sum _ { l = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { l } } { l ! } } Q _ { i _ { 1 } . . . i _ { l } } \partial _ { i _ { 1 } } \dots \partial _ { i _ { l } } { \frac { 1 } { | { \bf x } | } } ,
$$

where

$$
Q _ { i _ { 1 } . . . i _ { l } } = \int d ^ { 3 } y y ^ { \langle i _ { 1 } } . . . y ^ { i _ { l } \rangle } \rho ( { \bf y } ) ,
$$

ind the brackets in $y ^ { \langle i _ { 1 } } \dots y ^ { i _ { l } \rangle }$ means that we must take the symmetrictrace-free (STF) part of the tensor $y ^ { i _ { 1 } } \cdot , \cdot y ^ { i _ { l } }$ .We therefore have two equivalent formalisms for the multipole expansion of a scalar field that satisfies the Poisson equation (3.169),either in terms of spherical harmonics,or in terms of STF tensors.

For applications to electrodynamics or to gravitational waves,we need t generalize the above results in two ways.First，we do not have a scalar field but rather a vector field $A _ { \mu }$ or a tensor field $\bar { h } _ { \mu \nu }$ .Second, we do not have static fields governed by $\dot { \mathrm { ~  ~ } }$ Poisson equation,but rather time-dependent fields whose wave equatidn involve a d'Alembertian operator,such as $\sqcup A _ { \mu } = - ( 4 \pi / c ) J _ { \mu }$ in electromagnetism,and eq.(3.3) Ior GWs. For dealing with non-stationary fields,a possible route is to

30eJo7.

31 More generally,

$$
\nabla ^ { 2 } \frac { 1 } { | { \bf x } | } = - 4 \pi \delta ^ { ( 3 ) } ( { \bf x } ) ,
$$

i.e. $G ( { \bf x - y } ) = - 1 / ( 4 \pi | { \bf x - y } | )$ is the Green's function of the Laplacian.

perform a Fourier transform in time (but not in space),thus reducing the d'Alembertian operator $\boldsymbol { \bigsqcup } \boldsymbol { \phi } ( t , { \mathbf x } )$ to $( \nabla ^ { 2 } + k ^ { 2 } ) { \tilde { \phi } } _ { k } ( \mathbf { x } )$ , so that outside the source the field satisfies a Helmholtz equation $( \dot { \nabla } ^ { 2 } + k ^ { 2 } ) \tilde { \phi } _ { k } ( { \bf x } ) = 0$ , Foryector or tensor fields this can be combined with the use of vector and tensor spherical harmonics,respectively. In electrodynamics,this is the approach discussed in Chapter 16 of Jackson (1975).However,this approach does not make explicit the time integration linking the multipole moments to the actual levolution of the source,and furthermore yields somewhat complicated final expressions. Thus, in Section 3.5.1 we rather followan elegant approach,based on STF tensors,which gives a simple and unified treatment of scalar,vector and tensor fields.This formalism will be used extensively in Chapter 5,in the study of post-Newtonian sources.

The generalization of the approach based on spherical harmonics to the vector and tensor case leads to a more complicated formalism, which nevertheless can be useful in various instances (e.g. for classifying the extra polarization states of GWs in alternative theories of gravity),and we study it in Section 3.5.2.

# 3.5.1 Symmetric-trace-free (STF） form

We begin by introducing a useful multi-index notation,due to Blanchet and Damour,where a tensor with $l$ indices $i _ { 1 } i _ { 2 } \dots i _ { l }$ is labeled simply using a capital letter $L$ ，

$$
{ \cal F } _ { L } \equiv F _ { i _ { 1 } i _ { 2 } \dots i _ { l } } .
$$

Similarly, $G _ { i \mathcal { L } }$ denotes a tensor with $l + 1$ indices, $G _ { i L } \equiv G _ { i i _ { 1 } i _ { 2 } \dots i _ { l } }$ while, e.g.FiL-1 is a notation for Fiiz.i-1. Furthermore,OL is a notation for $\partial _ { i _ { 1 } } \ldots \partial _ { i _ { l } }$ ,and we will also use the notation $x _ { L } \equiv x _ { i _ { 1 } } x _ { i _ { 2 } } \cdot \cdot \cdot x _ { i _ { l } }$ and nL = nniz··nit，where ni= xi/r is the unit vector in the radial direction.In expressions such as $F _ { L } G _ { L }$ ，with repeated $L$ indices,the summation over all indices $i _ { 1 } , i _ { 2 } , \dots , i _ { l }$ is understood,so

$^ { 3 2 } \mathrm { { I n } }$ general,itcasowttthe irreducible tensor representations of a group are those that give zero when contracted with the invariant tensors (i.e.with the tensors whose form is unchanged by a group transformation). For $S O ( 3 )$ the invariant tensors are $\delta _ { i j }$ and $\epsilon _ { i j k }$ In fact，if $\mathcal { R } _ { i j }$ isrotation matrix, $\delta _ { i j }$ transforms as $\delta _ { i j } \ \to$ $\begin{array} { r } { \mathcal { R } _ { i k } \mathcal { R } _ { j l } \delta _ { k l } , } \end{array}$ asfor any tensor with two indices.However, $\mathcal { R } _ { i k } \mathcal { R } _ { j l } \delta _ { k l } \ =$ $\mathcal { R } _ { i k } \mathcal { R } _ { j k } = \delta _ { i j }$ because $\mathcal { R }$ is an orthogonal matrix. Similarly $\epsilon _ { i j k }$ is invariant because the determinant of $\mathcal { R }$ is equal to one.The condition that the contraction of any two indices ofa tensor with an epsilon tensor gives zero singlesout totally symmetric tensor,and thecondition that the contraction with $\delta _ { i j }$ gives zero gives the condition of zero trace,for anypair of indices.

$$
F _ { L } G _ { L } = \sum _ { i _ { 1 } . . . i _ { l } } F _ { i _ { 1 } . . . i _ { l } } G _ { i _ { 1 } . . . i _ { l } } .
$$

We use round brackets around indices to denote the symmetrization,e.g. @(ij)= (1/2)(aij +αji),and we denote by a hat the symmetric-trace-free (STF）projection．That is,the notation $\hat { K } _ { L }$ means that,starting from the tensor with $l$ indices $\dot { K } _ { i _ { 1 } \dots i _ { l } }$ ，we symmetrize it over all indices,and remove all the traces.The operation of taking the STF projection can also be denote by brackets around the indices,so $\hat { K } _ { L }$ can be equivalently written as $K _ { \langle L \rangle }$ .The latter notation allows us to write compactly the STF operation between indices belonging to different tensors,e.g. Cij(k AL-1)i means that we perform the STF operation among the index $k$ of $\epsilon _ { i j k }$ and the first ${ \mathit { l } } - 1$ indices of $A _ { i _ { 1 } \dots i _ { l - 1 } i _ { l } }$

A STF tensor with $l$ indices (i.e.of rank $l$ ） $A _ { i _ { 1 } . . . i _ { l } }$ has $2 l + 1$ independent components and is therefore a representation of dimension 2l+1 of the rotation group $S O ( 3 )$ .The crucial point is that these representations are irreducible.32 On the other hand,we know from the theory of representation of the rotation group that the irreducible representations of SO(3) are labeled by an integer value $l = 0 , 1 , , . . . ,$ and have dimension 2l+1,so we see that the set of all STF tensor,for all possible ranks l.gives a complete set of representations of $S O ( 3 )$

A generic tensor does not provide an ireducible representation of the rotation group,and can be decomposed in irreducible representation,i.e. expressed in terms of STF tensors and factors δij and Eijk. The simplest example is the decomposition of a generic tensor with two indices Tj. Writing

$$
\begin{array} { c } { { T _ { i j } = \displaystyle \frac { 1 } { 2 } ( T _ { i j } + T _ { j i } ) + \displaystyle \frac { 1 } { 2 } ( T _ { i j } - T _ { j i } ) } } \\ { { \equiv S _ { i j } + A _ { i j } ~ , } } \end{array}
$$

we lave decomposed Tij into its symmetric part Sij and its antisymmetric part Aij. Defining Ak = EijkAgj,we have Aij = (1/2)∈ijkAk. Furthermore,defining Sas the trace of Sij,i.e. S= Si,we can rewrite eq. (3.182) as

$$
T _ { i j } = \frac { 1 } { 3 } S \delta _ { i j } + \frac { 1 } { 2 } \epsilon _ { i j k } A _ { k } + ( S _ { i j } - \frac { 1 } { 3 } S \delta _ { i j } ) ,
$$

which shows explicitly the decomposition of a generic rank-2 tensor $T _ { i j }$ tocalarSveckdratesS

We now examine separately the application of the STF formalism to the multipole expansion of relativistic scalar,vector and tensor fields.

Scalar fields

Consider a scalar field $\phi$ satisfying the relativistic wave equation

$$
\begin{array} { r } { \phantom { \frac { 1 } { 2 } } \boxed { 1 } = - 4 \pi \rho , } \end{array}
$$

where the source p(t,x) is in general time-dependent,but is localized in space,so it vanishes if |xl >d.In the region outside the source,the most general solution can be written as

$$
\phi ( t , { \bf x } ) = \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { F _ { L } ( t - r / c ) } { r } \right] ,
$$

where we have used the multi-index notation explained above. This result follows from the fact that,forr >O and FL an arbitrary function of retarded time $u = t - r / c$

$$
\bigcirc \Bigg \lbrack \frac { F _ { L } ( t - r / c ) } { r } \Bigg \rbrack = 0 ,
$$

as can be checked immediately with the help of eq. (3.172).Therefore each term of the sum in eq.(3.185) is separately a solution of the vacuum equationΦ= O. The fact that this is the most general solution follows from the fact that the set of tensors FL,with allpossible ranks l,provides

33Observe that scalar and vectors are trivially STF tensors of rank zero and one,respectively.

a complete set of representations of the rotation group. So,eq. (3.185)is the generalization of eq.(3.178) to fields governed by a relativistic wave equation,with a non-stationary source.On the other hand,eq. (3.184) can be solved exactly using tHe retarded Green's function (3.6),which is the appropriate Green's function for a radiation problem, so

$$
\phi ( t , \mathbf { x } ) = \int d ^ { 3 } x ^ { \prime } { \frac { 1 } { | \mathbf { x } - | \mathbf { x } ^ { \prime } | } } \rho \left( t - { \frac { | \mathbf { x } - \mathbf { x } ^ { \prime } | } { c } } , \mathbf { x } ^ { \prime } \right) .
$$

34The computation is performed in detail in Appendix B of Blanchet and Damour (1989).

Comparing this expression, which holds everywhere and therefore in par ticular outside the source,with eq.(3.185),we can obtain the relativistic multipoles $F _ { L }$ in terms of the source density $\rho$ .The result $\mathrm { i s ^ { 3 4 } }$

$$
{ \cal F } _ { L } ( u ) = \int d ^ { 3 } y { \hat { y } } _ { L } \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) \rho ( u + z | { \bf y } | / c , { \bf y } ) ,
$$

where,according to the multi-index notation discussed above, $\hat { y } _ { L }$ is the STF projection of $y _ { L }$ .The function $\delta _ { l } ( z )$ is defined as

$$
\delta _ { l } ( z ) = \frac { \left. 2 l + 1 \right. ! ! } { 2 ^ { l + 1 } l ! } \left( 1 - z ^ { 2 } \right) ^ { l } ,
$$

and satisfies the identities

35Observe that the argument u+zlyl/c in eq.(3.188)can be changed to $u \ : -$ $z | \mathbf { y } | / c$ since $\delta _ { l } ( z ) = \delta _ { l } ( - z )$

$$
\begin{array} { l } { { \displaystyle \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) = 1 \mathrm { , } } } \\ { { \displaystyle \operatorname* { l i m } _ { l  \infty } \delta _ { l } ( z ) = \delta ( z ) \mathrm { , } } } \end{array}
$$

and

where $\delta ( z )$ is the usual Dirac delta.Physically,the integration over $d z$ in eq.(3.188) performs a weighted time average,diferent for each multipole moment $l$ ，and originates in the different time delay of the radiation emitted from different points inside the source. Equation (3.191) implies that,for sufficiently large $l$ ,this time delay becomes negligible.35

# Vector field

We next consider the electromagnetic field $A ^ { \mu }$ which,in the Lorentz gauge $\partial _ { \mu } A ^ { \mu } = 0$ (and unrationalized units for the electric charge),satisfies the wave equation

$$
\sqcap A ^ { \mu } = - \frac { 4 \pi } { c } J ^ { \mu } ,
$$

and again we consider a soure $J ^ { \mu } = \left( c \rho , { \bf J } \right)$ which is time-dependent but localized,so it vanishes if $| { \mathbf x } | > d$ Each component of $A ^ { \mu }$ can be treated just like the scalar field of the previous subsection,and therefore in the external source region we find

$$
\begin{array} { l } { { \displaystyle { \cal A } ^ { 0 } ( t , { \bf x } ) = \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { { \cal F } _ { L } ( u ) } { r } \right] \ : , } } \\ { { \displaystyle { \cal A } ^ { i } ( t , { \bf x } ) = \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { { \cal G } _ { i L } ( u ) } { r } \right] \ : , } } \end{array}
$$

where $u = t - r / c$ ．The explicit expression of $F _ { L } ( u )$ in terms of the source density is given again by eq. (3.188),while

$$
G _ { i L } ( u ) = \int d ^ { 3 } y \hat { y } _ { L } \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) J _ { i } ( u + z | { \bf y } | / c , { \bf y } ) .
$$

This is not yet the most convenient final form of the result,because the tensor $G _ { i L }$ is symmetric and traceless with respect to the indices i.i, since it depends on yL,but not under exchange of the index i with one of the indices $i _ { 1 } , \dots , i _ { l }$ ，so it is not irreducible.It can however be decomposed in irreducible STF tensors as follows,

$$
G _ { i L } = U _ { i L } + { \frac { l } { l + 1 } } \epsilon _ { a i \langle i _ { l } } C _ { L - 1 \rangle a } + { \frac { 2 l - 1 } { 2 l + 1 } } \delta _ { i \langle i _ { l } } D _ { L - 1 \rangle } ,
$$

where $U _ { L + 1 } \equiv G _ { \left. L + 1 \right. }$ ， $C _ { L } \equiv { \cal G } _ { a b ( L - 1 } \epsilon _ { i _ { l } } ) _ { a } b$ and $D _ { L - 1 } \equiv G _ { a a L - 1 }$ Then, $\mathbb { A } ^ { i } ( t , \mathbf { x } )$ is given by the sum of three STF terms.It is convenient to perform a gauge transformation Aμ→Aμ-δμθ (with \~= O in order not to spoil the Lorentz gauge) which removes the last term in eq.(3.196) from A,at the price of adding a new contribution to A°. The final result 1336

$$
\begin{array} { l } { { \displaystyle { \cal A } ^ { 0 } ( t , { \bf x } ) = \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { Q _ { L } ( u ) } { r } \right] \ : , \ } } \\ { { \displaystyle { \cal A } ^ { i } ( t , { \bf x } ) = - \frac { 1 } { c } \sum _ { l = 1 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 1 } \left[ \frac { Q _ { i L - 1 } ^ { ( 1 ) } ( u ) } { r } + \frac { l } { l + 1 } \epsilon _ { i a b } \partial _ { a } \left( \frac { M _ { b L - 1 } ( u ) } { r } \right) \right] \ : , } } \end{array}
$$

wtere $Q _ { i L - 1 } ^ { ( 1 ) }$ denotesthefirst derivative f $Q _ { i L - 1 }$ with respeto re tarded time.37 The explicit expression of the moments terms of the source is

$$
\begin{array} { l } { { \displaystyle Q _ { L } ( u ) = \int d ^ { 3 } y \int _ { - 1 } ^ { 1 } d z \left[ \delta _ { l } ( z ) \hat { y } _ { L } \rho ( u + z | { \bf y } | / c , { \bf y } ) \right. } } \\ { { \displaystyle \left. - \frac { 1 } { c ^ { 2 } } \frac { 2 l + 1 } { ( l + 1 ) ( 2 l + 3 ) } \delta _ { l + 1 } ( z ) \hat { y } _ { i L } J _ { i } ^ { ( 1 ) } ( u + z | { \bf y } | / c , { \bf y } ) \right] , } } \end{array}
$$

where $l \geqslant 0$ and

$$
M _ { L } ( u ) = \int d ^ { 3 } y \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) \hat { y } _ { \langle L - 1 } m _ { i _ { l } \rangle } ( u + z | { \bf y } | / c , { \bf y } ) ,
$$

where $l \geqslant 1$ and $m _ { i } = \epsilon _ { i j k } y _ { j } J _ { k }$ is the“magnetization density”.These results show that the electromagnetic field outside the source can be expressed in terms of two families of $\$ 12$ time-dependent multipole moments,the“electric moments” $Q _ { L } ( u )$ and the“magnetic moments" $\mathrm { M } _ { L } ( u )$ ,

# Gravitational field

We now consider the linearized gravitational field $\bar { h } _ { \mu \nu }$ that,in the Lorentz auge (1.18),satisfies eq. (1.24). Again, we assume that the source $T _ { \mu \nu }$

36The computation is performed in detail in Damour and Iyer (1991a).

$^ { 3 7 } \mathrm { F o r }$ a function $f ( u )$ of retarded time, we will use the notation

$$
f ^ { ( n ) } ( u ) \equiv \frac { d ^ { n } f } { d u ^ { n } } .
$$

has compact support. Then,in the exterior source region the same argument used above for scalar and electromagnetic fields allows us to write the most general solution of the vacuum equations,as

$$
\begin{array} { l } { { \displaystyle \bar { h } ^ { 0 0 } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { F _ { L } ( u ) } { r } \right] \ : , } } \\ { { \displaystyle \bar { h } ^ { 0 i } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { G _ { i L } ( u ) } { r } \right] \ : , } } \\ { { \displaystyle \bar { h } ^ { i j } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { H _ { i j L } ( u ) } { r } \right] \ : . } } \end{array}
$$

38See Damour and Iyer (199la), where it is performed in all detail.

The computation proceeds similarly to the electromagnetic case,but is technically more involved.38 We first decompose $G _ { i L }$ in STF tensors, just as we have done in eq. (3.196). Similarly, we decompose $H _ { i j L }$ in STF tensors. After performing a suitable gauge transformation (that preserves the gauge condition $| \partial _ { \mu } \bar { h } ^ { \mu \nu } = 0 \bigr array$ ),the result can be written as

$$
\begin{array} { l } { { \displaystyle \bar { h } ^ { 0 0 } = + \frac { 4 G } { c ^ { 2 } } \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { M _ { L } \left. u \right. } { r } \right] \ : , \ } } \\ { { \displaystyle \bar { h } ^ { 0 i } = - \frac { 4 G } { c ^ { 3 } } \sum _ { l = 1 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 1 } \left[ \frac { M _ { i L - 1 } ^ { ( 1 ) } \left( u \right) } { r } + \frac { l } { l + 1 } \epsilon _ { i a b } \partial _ { a } \left( \frac { S _ { b L - 1 } \left( u \right) } { r } \right) \right] \ : , \ : \ : } } \\ { { \displaystyle \bar { h } ^ { i j } = + \frac { 4 G } { c ^ { 4 } } \sum _ { l = 2 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 2 } \left[ \frac { 1 } { r } M _ { i j L - 2 } ^ { ( 2 ) } ( u ) + \frac { 2 l } { l + 1 } \partial _ { a } \left( \frac { 1 } { r } \epsilon _ { a b \left( i } S _ { j \right) b L - 2 } ^ { ( 1 ) } ( u ) \right) \right] } . }  \end{array}
$$

The result therefore depends again on two families of STF tensors, $M _ { L }$ and $S _ { L }$ .Their explicit expression in terms of the energy-momentum tensor of the source can be written introducing the “active gravitationalmass density" $\sigma$ ，

$$
{ \boldsymbol { \sigma } } \equiv { \frac { 1 } { \ c { c } ^ { 2 } } } ~ \left[ { \cal T } ^ { 0 0 } + { \cal T } ^ { i i } \right] .
$$

and the “active mass-current density”,

$$
\sigma _ { i } \equiv { \frac { 1 } { c } } T ^ { 0 i } ,
$$

as well as $\sigma _ { i j } = T ^ { i j }$ .Then

$$
\begin{array} { l } { { \displaystyle M _ { L } ( u ) = \int d ^ { 3 } x \int _ { - 1 } ^ { 1 } d z \left\{ \delta _ { l } ( z ) \hat { x } _ { L } \sigma - \frac { 4 ( 2 l + 1 ) \hat { \delta } _ { l + 1 } ( z ) } { c ^ { 2 } ( l + 1 ) ( 2 l + 3 ) } \hat { x } _ { i L } \sigma _ { i } ^ { ( 1 ) } \right. } } \\ { { \displaystyle ~ \left. + \frac { 2 ( 2 l + 1 ) \delta _ { l + 2 } ( z ) } { c ^ { 4 } ( l + 1 ) ( l + 2 ) ( 2 l + 5 ) } \hat { x } _ { i j L } \sigma _ { i j } ^ { ( 2 ) } \right\} ( u + z | { \bf x } | / c , { \bf x } ) , \beta _ { l } ~ } } \\ { { \displaystyle S _ { L } ( u ) = \int d ^ { 3 } x \int _ { - 1 } ^ { 1 } d z \left. \varepsilon _ { \alpha b \hat { \nu } ( \hat { x } _ { i } } \left\{ \delta _ { l } ( z ) \hat { x } _ { L - 1 ) a } \sigma _ { b } \right. \right.}  }  \\ { { \displaystyle ~ \left. - \frac { ( 2 l + 1 ) \delta _ { l + 1 } ( z ) } { c ^ { 2 } ( l + 2 ) ( 2 l + 3 ) } \hat { x } _ { L - 1 ) a c } \sigma _ { b c } ^ { ( 1 ) } \right\} ( u + z | { \bf x } | / c , { \bf x } ) . } } \end{array}
$$

This result holds at the level of linearizedl theory.In Chapter 5 we will study the full non-linear theory and we will discover that,remarkably, the exact solution of the full general-relativistic problem is constructed using a quantity $\mathsf { h } _ { 1 } ^ { \mu \nu }$ that is obtained fromieqs.(3.204)-(3.208) by means of a very simple modification,that is,withithe replacement of the energy momentum tensor of matter $T _ { \mu \nu }$ by an effective energy-momentum tensor Tμv that includes also the non-linearities of the gravitational field,39 see eqs.(5.135) and (5.136)． Thus,eqs(3.207) and (3.208) already contain the blueprint of the solution to the full non-linear problem.

The integration over $z$ can be computed,in an expansion in powers of $1 / c .$ using the formula

$$
\int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) f ( u + z | { \bf x } | / c , { \bf x } ) = \sum _ { k = 0 } ^ { + \infty } \frac { ( 2 l + 1 ) ! ! } { 2 ^ { k } k ! ( 2 l + 2 k + 1 ) ! ! } \left( \frac { | { \bf x } | } { c } \frac { \partial } { \partial u } \right) ^ { 2 k } f ( u , { \bf x } ) .
$$

From this we see that，in eqs. (3.207) and (3.208)(as well as in the analogous formulas for the scalar and vector fields),the integration over z allows us to take into account, in a compact way,an infinite series of derivatives.

39Together withaprescriptionforren dering finite the integral,since the source $\tau _ { \mu \nu }$ no longer has compact support.

Finally, we can use these multipolar expressions for $\bar { h } _ { \mu \nu }$ to compute the $O ( 1 / r )$ $h _ { i j } ^ { \mathrm { T T } }$ (14)yegt integration.40 The result is

$$
\begin{array} { r } { \frac { d E } { d t } = \displaystyle \sum _ { l = 2 } ^ { + \infty } \frac { G } { c ^ { 2 l + 1 } } \left\{ \frac { ( l + 1 ) ( l + 2 ) } { ( l - 1 ) l l ! ( 2 l + 1 ) ! ! } \langle M _ { L } ^ { ( l + 1 ) } ( u ) M _ { L } ^ { ( l + 1 ) } ( u ) \rangle \right. } \\ { \left. + \frac { 4 l ( l + 2 ) } { c ^ { 2 } ( l - 1 ) ( l + 1 ) ! ( 2 l + 1 ) ! ! } \langle S _ { L } ^ { ( l + 1 ) } ( u ) S _ { L } ^ { ( l + 1 ) } ( u ) \rangle \right\} . } \end{array}
$$

Similarly,for the linear momentum losses one finds

$$
\begin{array} { r l } { \displaystyle \frac { d P _ { i } } { d t } = \sum _ { l = 2 } ^ { + \infty } \frac { G } { c ^ { 2 l + 2 } } \Bigg \{ \frac { 2 ( l + 2 ) ( l + 3 ) } { l ( l + 1 ) ! ( 2 l + 3 ) ! ! } \big \langle M _ { i L } ^ { ( l + 2 ) } ( u ) M _ { L } ^ { ( l + 1 ) } ( u ) \big \rangle } & { { } } \\ { + \frac { 8 ( l + 3 ) } { c ^ { 2 } ( l + 1 ) ! ( 2 l + 3 ) ! ! } \big \langle S _ { i L } ^ { ( l + 2 ) } ( u ) S _ { L } ^ { ( l + 1 ) } ( u ) \big \rangle } & { { } \mathrm { ( \xi } } \\ { \displaystyle } & { { } + \frac { 8 ( l + 2 ) } { c ^ { 2 } ( l - 1 ) ( l + 1 ) ! ( 2 l + 1 ) ! ! } \big \langle \epsilon _ { i j k } S _ { j L - 1 } ^ { ( l + 1 ) } ( u ) S _ { k L - 1 } ^ { ( l + 1 ) } ( u ) \big \rangle \Bigg \} . } \end{array}
$$

Observe that the linear momentum losses come from the interference between multipoles of different rank,such as the mass quadrupole/mass octupole mixed term,as we already saw on pages 130-131.41

# 3.5.2 Spherical tensor form

In this section we discuss an alternative|formalism for performing the multipole expansion to all orders,which is based on the generalization of the notion of spherical harmonics to a spin-2 field.

$^ { 4 0 } \mathrm { T h e }$ power is quadratic in $\dot { h } _ { i j } ^ { \mathrm { T T } }$ and therefore in the multipole moments. However,mixed terms of the form $M _ { L } S _ { L ^ { \prime } }$ give vanishing contribution,after the angular integration,because of parity,while terms $M _ { L } M _ { L ^ { \prime } }$ or $S _ { L } S _ { L ^ { \prime } }$ contribute only if $L \ = \ L ^ { \prime }$ In fact, if ${ \mathit { l } } \ > \ { \mathit { l } } ^ { \prime }$ ，the indices in $M _ { i _ { 1 } \dots i _ { l } }$ cannot be all contracted with the indices of $M _ { i _ { 1 } \dots i _ { l ^ { \prime } } }$ ，and the remaining indices of the $i _ { 1 } \ldots , i _ { l }$ group are necessarily contracted among them,via the Kronecker deltas that come of from the angular integration,see eq.(3.23).

41See Thorne (1980), eq. $\left( 4 . 2 3 ^ { \prime } \right)$ for the corresponding expression for the angular momentum losses.

This section is quite technical,and can be omitted at a first reading.

# Spherical components of tensors

To introduce spherical tensors we first consider the quadrupole momem or,more generally，any traceless symmetric tensor with two indices whose Cartesian components we denote by $Q _ { i j }$ . As a first step we in troduce a basis in the space bf traceless symmetric tensors with two indices，which is chosen so to have a simple relation with the $l = 2$ spherical harmonics.

42Here,according to the standard definition of spherical harmonics,the angle $\phi$ is measured from the $\boldsymbol { \mathscr { x } }$ axis,so for instance the unit vector in the radial direction  has components nx = $\sin \theta \cos \phi , n _ { y } ~ = ~ \sin \theta \sin \phi$ and $\begin{array} { r l } { n _ { z } } & { { } = } \end{array}$ $\cos \theta$ Observe that this definition differs from that used,e.g.in Fig.3.2 and in equations such as eq.(3.72),where $\phi$ is measured from the $y$ axis.

We recallthat the sphericalharmonics $Y ^ { l m } ( \theta , \phi )$ with $l = 2$ are42

$$
\begin{array} { l } { { { \displaystyle Y ^ { 2 2 } ( \theta , \phi ) = \left( \frac { 1 5 } { 3 2 \pi } \right) ^ { 1 / 2 } ( e ^ { i \phi } \sin \theta ) ^ { 2 } , } } } \\ { { { \displaystyle Y ^ { 2 1 } ( \theta , \phi ) = - \left( \frac { 1 5 } { 8 \pi } \right) ^ { 1 / 2 } e ^ { i \phi } \sin \theta \cos \theta , } } } \\ { { { \displaystyle Y ^ { 2 0 } ( \theta , \phi ) = \left( \frac { 5 } { 1 6 \pi } \right) ^ { 1 / 2 } ( 3 \cos ^ { 2 } \theta - 1 ) , } } } \end{array}
$$

while the expressions for negative values of $m$ are obtained using

$$
Y ^ { l , - m } = ( - 1 ) ^ { m } Y ^ { l m ^ { * } } .
$$

Consider now the unit radial vector $\hat { \bf n }$ .In polar coordinates we have $n _ { x } = \sin \theta \cos \phi$ $n _ { y } = \sin \theta \sin \phi$ , $n _ { z } = \cos \theta$ ,and therefore

$$
e ^ { i \phi } \sin \theta = n _ { x } + i n _ { y } , \cos \theta = n _ { z } .
$$

Plugging this into the explicit expressions for the spherical harmonics $Y ^ { 2 m }$ ,and using the fact that $n _ { i } n _ { i } = 1$ , we see that we can write

$$
\overline { { Y ^ { 2 m } ( \theta , \phi ) = y _ { i j } ^ { 2 m } n _ { i } n _ { j } } } ,
$$

where $y _ { i j } ^ { 2 m }$ is independent of $\theta , \phi$ , and the sum over $i , j$ on the right-hand ided $\mathcal { V } _ { i j } ^ { 2 m }$ whichis symmetricin andwecopetetheefnitiono $\mathcal { V } _ { i j } ^ { 2 m }$ requiring he the antisymmetric part vanishes.The explicit form of the tensors $\mathcal { V } _ { i j } ^ { 2 m }$ is then

$$
\begin{array} { r l } & { y _ { i j } ^ { 2 2 } = \sqrt { \frac { 1 5 } { 3 2 \pi } } \left( \begin{array} { r r r } { 1 } & { i } & { 0 } \\ { i } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) _ { i j } , } \\ & { y _ { i j } ^ { 2 1 } = - \sqrt { \frac { 1 5 } { 3 2 \pi } } \left( \begin{array} { r r r } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { i } \\ { 1 } & { i } & { 0 } \end{array} \right) _ { i j } , } \\ & { y _ { i j } ^ { 2 0 } = \sqrt { \frac { 5 } { 1 6 \pi } } \left( \begin{array} { r r r } { - 1 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right) _ { i j } , } \end{array}
$$

together with $\mathcal { V } _ { i j } ^ { 2 , - m } = ( - 1 ) ^ { m } ( \mathcal { V } _ { i j } ^ { 2 m } ) ^ { * }$ .We seefrom theexplicit expres sions that thefive matrices $y _ { i j } ^ { 2 , \dag n }$ are traceless in the $( i , j )$ indices.This could have also been understood by integrating eq.(3.217) over the solid angle and using $\int d \Omega Y ^ { 2 m } = 0$ and $\int d { \bar { \Omega } } | n _ { i } n _ { j } \sim \delta _ { i j }$ ．From the explicit exresioseetf $\mathcal { V } _ { i j } ^ { 2 m }$ are an orthogonal basis,in the sense that

$$
\sum _ { i j } ^ { } y _ { i j } ^ { 2 m } ( y _ { i j } ^ { 2 m ^ { \prime } } ) ^ { * } = { \frac { 1 5 } { 8 \pi } } \delta ^ { m m ^ { \prime } } .
$$

It is sometimes useful to invert eq. (3.217).The result is

$$
n _ { i } n _ { j } - \frac { 1 } { 3 } \delta _ { i j } = \sum _ { m = - 2 } ^ { 2 } c _ { i j } ^ { m } Y ^ { 2 m } ( \theta , \phi ) ,
$$

where

$$
c _ { i j } ^ { m } = \frac { 8 \pi } { 1 5 } ( y _ { i j } ^ { 2 m } ) ^ { * } .
$$

This can be proved multiplying both sides of eq. (3.220) by $\mathcal { V } _ { i j } ^ { 2 m }$ ,summing over i,j and using eqs. (3.221） and (3.219)，which gives back eq. (3.217). Since $y _ { i j } ^ { 2 m }$ is traceless,the coefficient of the term proportional to δij on the left-hand side of eq.(3.22O) is not yet fixed in this way,but we can fix it by observing that the right-hand side of eq.(3.220) is traceless,so also the left-hand side must be traceless.

The five symmetric and traceless matrices $\mathcal { V } _ { i j } ^ { 2 m }$ ，with $m = - 2 , \ldots , 2$ are linearly independent and therefore area basis for the five-dimensional space of traceless symmetric tensors $Q _ { i j }$ .This means that we can expand an arbitrary traceless symmetric tensors $Q _ { i j }$ as

$$
Q _ { i j } = \sum _ { m = - 2 } ^ { 2 } Q _ { m } y _ { i j } ^ { 2 m } .
$$

The quantities $Q _ { m }$ are called the spherical components of $Q _ { i j }$ .Multiplving by $n _ { i } n _ { j }$ and using eq.(3.217) we obtain

$$
Q _ { i j } n _ { i } n _ { j } = \sum _ { m = - 2 } ^ { 2 } Q _ { m } Y ^ { 2 m } ( \theta , \phi ) .
$$

(As always,the summation over the repeated $i , j$ indices is understood; instead,we write explicitly the sum over $m$ .）This equation could also have been obtained directly by observing that $Q _ { i j } n _ { i } n _ { j }$ is a function of $\theta , \phi$ (with the dependence hidden in $n _ { i } ( \theta , \phi )$ ，while $Q _ { i j }$ isa constant tensor) and therefore can be expanded in spherical harmonicsas $\begin{array} { r } { \sum _ { l , m } Q _ { l m } Y ^ { l m } ( \theta , \phi ) } \end{array}$ .However, $Q _ { i j }$ is symmetric and traceless, so it is a spin-2 operator and therefore in the expansion in spherical harmonics, only $l = 2$ contributes.

The five independent components of the symmetric traceless tensor Qjare therefore expressed in terms of the five independent quantities $Q _ { m }$ ,with $m = - 2 , \ldots , 2$ If $Q _ { i j }$ is real,asin the case of the mass quadrupole,thefivecomplexquntities $Q _ { m }$ satisfy $Q _ { m } ^ { * } = ( - 1 ) ^ { m } Q _ { - m }$ because of eq. (3.215). Using eq. (3.219) we can invert eq.(3.222),

$$
Q _ { m } = \frac { 8 \pi } { 1 5 } Q _ { i j } ( y _ { i j } ^ { 2 m } ) ^ { * } ,
$$

or, explicitly,

$$
\begin{array} { c } { { Q _ { \pm 2 } = \left( \displaystyle \frac { 2 \pi } { 1 5 } \right) ^ { 1 / 2 } \left( Q _ { 1 1 } - Q _ { 2 2 } \mp 2 i Q _ { 1 2 } \right) , } } \\ { { { } } } \\ { { Q _ { \pm 1 } = \mp \left( \displaystyle \frac { 8 \pi } { 1 5 } \right) ^ { 1 / 2 } \left( Q _ { 1 3 } \mp i Q _ { 2 3 } \right) , } } \\ { { { } } } \\ { { Q _ { 0 } = - \left( \displaystyle \frac { 4 \pi } { 5 } \right) ^ { 1 / 2 } \left( Q _ { 1 1 } + Q _ { 2 2 } \right) . } } \end{array}
$$

We can now write the power emitted by the quadrupole radiation, given in eq.(3.75),in terms of the spherical components $Q _ { m }$ Using eq. (3.223) we write

$$
\overleftrightarrow { Q } _ { i j } n _ { i } n _ { j } = \Biggl | \sum _ { m = - 2 } ^ { 2 } \overleftrightarrow { Q } _ { m } Y ^ { 2 m } ( \theta , \phi ) \Biggr . ,
$$

and we take the squared modulus,

$$
\overleftrightarrow { Q } _ { i j } \overleftrightarrow { Q } _ { k l } n _ { i } n _ { j } n _ { k } n _ { l } = \sum _ { m , m ^ { \prime } } \overleftrightarrow { Q } _ { m } ^ { * } \overleftrightarrow { Q } _ { m ^ { \prime } } Y ^ { 2 m ^ { * } } ( \theta , \phi ) Y ^ { 2 m ^ { \prime } } ( \theta , \phi ) .
$$

Integrating over $d \Omega$ with the help of eq. (3.22) and using the orthogo nality of the spherical harmonics,

$$
\int d \Omega Y ^ { l m ^ { * } } ( \theta , \phi ) Y ^ { l ^ { \prime } m ^ { \prime } } ( \theta , \phi ) = \delta ^ { l l ^ { \prime } } \delta ^ { m m ^ { \prime } } ,
$$

we get

$$
\frac { 8 \pi } { 1 5 } \dddot { Q _ { i j } } \ddot { Q _ { i j } } = \sum _ { m = - 2 } ^ { 2 } | \dddot { Q _ { m } } | ^ { 2 } .
$$

Therefore,eq.(3.75) becomes

$$
\overline { { { \cal P } _ { \mathrm { q u a d } } } } = \frac { 3 G } { 8 \pi c ^ { \sharp } } \sum _ { m = - 2 } ^ { 2 } \langle | \overleftrightarrow { Q } _ { m } | ^ { 2 } \rangle .
$$

43In this section we prefer to write explicitly the indices $i _ { 1 } \ldots i _ { l }$ ,rather than using the multi-index notation defined on page 134.

We can now generalize the above construction to traceless symmetric tensors with an arbitrary number of indices.We consider a (real) STF tensor with $l$ indices, $T _ { i _ { 1 } \dots i _ { l } }$ 43A basis in this tensor spacecan be ob tained by observing that the spherical harmonics $Y ^ { l m } ( \theta , \phi )$ with $m \geqslant 0$ are given explicitly by

$$
\begin{array} { l } { { \displaystyle Y ^ { l m } ( \theta , \phi ) = C ^ { l m } e ^ { i m \phi } P ^ { l m } ( \cos \theta ) } } \\ { { \displaystyle \quad = C ^ { l m } ( e ^ { i \phi } \sin \theta ) ^ { m } \sum _ { k = 0 } ^ { | ( l - m ) / 2 | } a _ { k } ^ { l m } ( \cos \theta ) ^ { l - m - 2 k } , } } \end{array}
$$

and $Y ^ { l m } = ( - 1 ) ^ { m } ( Y ^ { l , - m } ) ^ { * }$ for $m < 0$ .The notation $[ ( l - m ) / 2 ]$ denotes the largest integer smaller or equal to $( l - m ) / 2$ ,and the coefficients are givenby

$$
\begin{array} { c } { { C ^ { l m } = ( - 1 ) ^ { m } \left( \displaystyle \frac { 2 l + 1 } { 4 \pi } \displaystyle \frac { ( l - m ) ! } { ( l + m ) ! } \right) ^ { 1 / 2 } , } } \\ { { a _ { k } ^ { l m } = \displaystyle \frac { ( - 1 ) ^ { k } } { 2 ^ { l } k ! ( l - k ) ! } \displaystyle \frac { ( 2 l - 2 k ) ! } { ( l - m - 2 k ) ! } . } } \end{array}
$$

Comparing with eq. (3.216) we see that $Y _ { \parallel } ^ { l m }$ is the sum of a term containing $l$ factors $n _ { i }$ ,a term containing $l - 2$ factors $n _ { i }$ ,a term containing $l - 4$ factors $n _ { i }$ ,etc.Using $n _ { i } n _ { i } = 1$ ,a term with $l - 2$ factors $n _ { i _ { 1 } } \ldots n _ { i _ { l - 2 } }$ can be rewritten trivially as a term with $\it l$ factors $n _ { i }$ ，as $\delta _ { i j } n _ { i _ { 1 } } \dots n _ { i _ { l - 2 } } n _ { i } n _ { j } .$ and similarly for all terms with $l - 2 k$ factors.Then we can write

$$
Y ^ { l m } ( \theta , \phi ) = \mathcal { Y } _ { i _ { 1 } \dots i _ { l } } ^ { l m } n _ { i _ { 1 } } \cdot \cdot \cdot n _ { i _ { l } } ,
$$

where the tensors $\mathcal { V } _ { i _ { 1 } \dots i _ { l } } ^ { l m }$ are independent of $\theta , \phi$ ,and the sum over the lindices $i _ { 1 } \ldots i _ { l }$ is understood. We will not need the explicit form of $y _ { i _ { 1 } , . . , i _ { l } } ^ { i m }$ $l = 2$ $y _ { i _ { 1 } \dots i _ { l } } ^ { l m }$ are a basis in the space of traceless symmetric tensors with indices. This means that we can expand

$$
T _ { i _ { 1 } \dots i _ { l } } = \sum _ { m = - l } ^ { l } T _ { l m } \mathcal { V } _ { i _ { 1 } \dots i _ { l } } ^ { l m } ,
$$

and this defines the spherical components $T _ { l m }$ of the tensor $T _ { i _ { 1 } \dots i _ { l } }$ Multiplyingby $n _ { i _ { 1 } } \cdots n _ { i _ { l } }$ we have the identity

$$
T _ { i _ { 1 } . . . i _ { l } } n _ { i _ { 1 } } \cdot \cdot \cdot n _ { i _ { l } } = \sum _ { m = - l } ^ { l } T _ { l m } Y ^ { l m } ( \theta , \phi ) ,
$$

which expresses the fact that in the expansion in spherical harmonics of the left-hand side contribute only the spherical harmonics whose angular momentum $l$ is equal to the number of indices of $T _ { i _ { 1 } \dots i _ { l } }$ This is a consequence of the fact that both a STF tensor with $\it l$ indices,and the spherical harmonics $Y ^ { l m }$ ，provide an irreducible representation of dimension $2 l + 1$ of the rotation group.

Using the orthogonality of spherical harmonics we can invert eq. (3.236) and we obtain the spherical components $T _ { l m }$ in terms of the Cartesian components $T _ { i _ { 1 } \dots i _ { l } }$ ，

$$
\begin{array} { l } { { \displaystyle { \mathcal T } _ { l m } = T _ { i _ { 1 } \dots i _ { l } } \int d \Omega ( Y ^ { l m } ) ^ { * } n _ { i _ { 1 } } \Big \vert \cdot \cdot n _ { i _ { l } } } } \\ { { \displaystyle \ } } \\ { { \displaystyle \quad = T _ { i _ { 1 } \dots i _ { l } } ( { \mathcal V } _ { j _ { 1 } , \dots j _ { l } } ^ { l m } ) ^ { * } \int d \Omega n _ { i _ { 1 } } \cdot \cdot \cdot n _ { i _ { l } } n _ { j _ { 1 } } \cdot \cdot \cdot n _ { j _ { l } } \ , } } \end{array}
$$

vhere in the second line we used eq. (3.234). The integral can be perumedusing cq (3.23). Since $\mathcal { Y } _ { j _ { 1 } , \dots j _ { l } } ^ { l m }$ and $T _ { i _ { 1 } \dots i _ { l } }$ are rceless in he

44For this reasons,the spherical components find a typical application in quantum mechanics,for writing selection rules in atomic transitions.

sum over permutations in eq.(3.23) the terms with Kronecker deltas of the type $\delta _ { i _ { k } i _ { k ^ { \prime } } }$ or $\delta _ { j _ { k } j _ { k ^ { \prime } } }$ give zero,and the only contributions come from the term $\delta _ { i _ { 1 } j _ { 1 } } \dots \delta _ { i _ { l } j _ { l } }$ and from its permutations. Since $y _ { j _ { 1 } , . . . j _ { l } } ^ { l m }$ is totally symmetric,these $l !$ permutations all give the same result, so

$$
\overline { { { T _ { l m } = 4 \pi \frac { l ! } { ( 2 l + 1 ) ! ! } } T _ { i _ { 1 } \dots i _ { l } } ( y _ { i _ { 1 } \dots i _ { l } } ^ { l m } ) ^ { * } } } .
$$

For $l = 2$ ,we recover the result|obtained in eq. (3.224).Finally,a useful identity which generalizes eq.(3.229) is obtained taking the modulus squared of eq.(3.236)and integrating over $d \Omega$ with the help of eq. (3.23). This gives

$$
4 \pi { \frac { l ! } { ( 2 l + 1 ) ! ! } } T _ { i _ { 1 } \dots i _ { l } } T ^ { i _ { 1 } \dots i _ { l } } = \sum _ { m = - l } ^ { l } | T _ { l m } | ^ { 2 } .
$$

The transformation properties under rotations of the spherical compo nents of tensors are fixed by the transformation properties of the spher ical harmonics.For instance,consider a rotation by an angle $\varphi$ around the $z$ -axis, $\phi  \phi + \varphi$ .The left-hand side of eq.(3.236) is a scalar $^ { \mathrm { ~ S 0 ~ } }$ it is invariant,while on the right-hand side $Y _ { l m }  e ^ { i m \varphi } Y _ { l m }$ .Therefore $T _ { i m }$ transforms into itself, $\mathrm { a s ^ { 4 4 } }$ |

$$
T _ { l m }  e ^ { - i m \varphi } T _ { l m } .
$$

More generally, under arbitrary rotations the $2 l + 1$ components of $T _ { l m }$ with $m = - l , \ldots , l$ and $l$ given,transform among themselves in the same way as $Y _ { l m } ^ { * } ( \theta , \phi )$

# Vector and tensor spherical harmonics

The spherical components of tensors,introduced above,are one of the tools useful for the construction of a systematic multipole expansion. Here we introduce another necessary ingredient of this formalism,the tensor spherical harmonics.In the same way as the usual (scalar) spherical harmonics are useful to describe the angular dependence of a scalar field,tensor spherical harmonics are useful for describing the angular dependence of a field with spin.

We denote by L the orbital angular momentum operator,by S the spin operator and by ${ \mathbf { J } } = { \mathbf { L } } + { \mathbf { S } }$ the total angular momentum. All these quantities are measured in units of $\hbar$ ,so for instance,as operator acting on functions, $\mathbf { L } = \mathbf { r } \times \left( - i \nabla \right)$ . Since the operators $\mathbf { J } ^ { 2 } , J _ { z } ^ { 2 } , \mathbf { L } ^ { 2 }$ and $\mathbf { S } ^ { 2 }$ commute,we can diagonalize them simultaneously. The eigenfunctions are the tensor spherical harmonics and are denoted by $Y _ { j j _ { z } } ^ { l s } ( \theta , \phi )$ .Therefore. by definition,the functions $Y _ { j j _ { \ast } } ^ { l s } ( \theta , \phi )$ are the solutions of

$$
\begin{array} { r l } & { \mathbf { J } ^ { 2 } Y _ { j j _ { z } } ^ { l s } = j ( j + 1 ) Y _ { j j _ { z } } ^ { l s } , } \\ & { J _ { z } Y _ { j j _ { z } } ^ { l s } = j _ { z } Y _ { j j _ { z } } ^ { l s } , } \\ & { \mathbf { L } ^ { 2 } Y _ { j j _ { z } } ^ { l s } = l ( l + 1 ) Y _ { j j _ { z } } ^ { l s } , } \\ & { \mathbf { S } ^ { 2 } Y _ { j j _ { z } } ^ { l s } = s ( s + 1 ) Y _ { j j _ { z } } ^ { l s } . } \end{array}
$$

Their explicit form can be obtained coupling the (scalar) spherical harmonics $Y _ { l m }$ to the spin function $\chi _ { s s _ { z } }$ ，with the appropriate Clebsch-Gordan coefficients which gives a state with total angular momentum $| j , j _ { z } \rangle$ ，

$$
Y _ { j j _ { z } } ^ { l s } ( \theta , \phi ) = \sum _ { l _ { z } = - l } ^ { l } \sum _ { s _ { z } = - s } ^ { s } \langle s l s _ { z } l _ { z } | j j _ { z } \rangle Y _ { l l _ { z } } ( \theta , \phi ) \chi _ { s s _ { z } } .
$$

It is easy to check that this expressionlindeed satisfies eqs. (3.241)- (3.244).For instance,the operators $L _ { i }$ act only on the variables $\theta , \phi$ of $Y _ { l l _ { z } } ( \theta , \phi )$ ，and then eq.(3.243） follows from ${ \bf L } ^ { 2 } Y _ { l l _ { z } } = l ( l + 1 ) Y _ { l l _ { z } }$ Similarly,eq.(3.244) follows from the fact that the spin operator acts only on the spin wavefunction $\chi$ ，with ${ \bf S } ^ { 2 } \chi _ { s s _ { z } } = s ( s + 1 ) \chi _ { s s _ { z } }$ .Finally, the Clebsch-Gordan coefficients $\langle s l s _ { z } l _ { z } | j _ { J _ { z } } \rangle$ couple a state with orbital angular momentum $| l l _ { z } \rangle$ to a state with \$pin $\left| s s _ { z } \right.$ to give a state with total angular momentum $| j j _ { z } \rangle$ ,so that eqs.(3.241) and (3.242) follow.

Depending on the value of $s$ ，one has spinor spherical harmonics $( s = 1 / 2$ ),vector spherical harmonics $\mathbf { \Phi } _ { \left. s \right. } ^ { \prime } = 1 \mathbf { \dot { \Phi } } _ { \left. \mathbf { \Phi } \right. } ^ { \prime }$ )，spin-2 tensor spherical harmonics, etc.45

Tensor spherical harmonics describe the angular distribution and polarization of particles of spin $s$ ,ina state with definite values of the total angular momentum $j$ ,of $j _ { z }$ ,and of the orbital angular momentum .For gravitational waves,we are interested in spin-2 tensor spherical harmonics. Observe that,beside the indices $l , s , j , j _ { z }$ written explicitly, $Y _ { j j _ { z } } ^ { l s }$ carries also an index which depends on the nature of the spin wavefunction $\chi$ ；e.g.a spinor index for $s = 1 / 2$ ,a vector index for $s = 1$ ， a pair of spatial indices $( i , i ^ { \prime } )$ for $s = 2$ (with $( Y _ { j j _ { z } } ^ { l 2 } ) _ { i i ^ { \prime } }$ symmetric and traceless in $i , i ^ { \prime }$ ，etc.

45One should not be misled by this nomenclature.Of course,the properties of $Y _ { j j _ { z } } ^ { l s }$ under rotations depend on the value of the total angular momentum $j$ ,not on the spin s,so for instance a vector spherical harmonics $Y _ { j j _ { z } } ^ { l 1 }$ with $j ~ = ~ 2$ (and therefore $\ l \ = \ 1 , 2$ or3) has the transformation properties of a spin-2 operator,not of a vector，just as the usual scalar spherical harmonics $Y _ { l m }$ transform of course as a spin-l operator,not as a scalar.

Vector spherical harmonics

Let us first examine the vector spherical harmonics. The spin wave funetion $\chi$ in this case is a vector,and we denote it by $\xi$ The wavefunctions with a definite value of $s _ { z } = \mathrm { 0 , \pm 1 }$ can be constructed from the unit vectors $\mathbf { e } _ { x } , \mathbf { e } _ { y }$ and $\mathbf { e } _ { z }$ as

$$
{ \pmb \xi } ^ { ( \pm 1 ) } = \mp \frac { 1 } { \sqrt { 2 } } \left( { \bf e } _ { x } \pm i { \bf e } _ { y } \right) , \quad { \pmb \xi } ^ { ( 0 ) } = { \bf e } _ { z } .
$$

Then the vector spherical harmonics are

$$
\mathbf { Y } _ { j j _ { z } } ^ { l } ( \theta , \phi ) = \sum _ { l _ { z } = - l } ^ { l } \sum _ { s _ { z } = 0 , \pm 1 } \langle 1 l s _ { z } l _ { z } | j j _ { z } \rangle Y _ { l l _ { z } } ( \theta , \phi ) \pmb { \xi } ^ { ( s _ { z } ) } .
$$

Observe that in $\pmb { \xi } ^ { ( s _ { z } ) }$ the index $s _ { z } ~ = ~ \pm 1 , 0$ tells us which vector we must consider,according to eq. (3.246);the spatial components of the retor are instead denoted by $\xi _ { i } ^ { ( \dot { s } _ { z } ) }$ Correspondingly, $\mathbf { Y } _ { j j _ { z } } ^ { l }$ is a vector with components $( Y _ { j j _ { z } } ^ { l } ) _ { i }$ .Note also that we have written $\check { \mathbf { Y } } _ { j j _ { z } } ^ { \tilde { l } 1 }$ simply as $Y _ { j j _ { z } } ^ { l }$ since the fact that $s = 1$ is already implicit in the vector notation V