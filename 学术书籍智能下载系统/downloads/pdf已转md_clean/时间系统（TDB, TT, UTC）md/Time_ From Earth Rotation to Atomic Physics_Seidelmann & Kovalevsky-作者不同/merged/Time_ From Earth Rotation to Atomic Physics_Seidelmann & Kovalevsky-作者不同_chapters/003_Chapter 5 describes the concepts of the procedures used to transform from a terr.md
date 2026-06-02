Chapter 5 describes the concepts of the procedures used to transform from a terrestrial reference system (TRS) to the celestial reference system (CRS) at any epoch $t$ . There we saw that:

$$
[ \mathrm { C R S } ( t ) ] = \mathbf { Q } ( t ) \ \mathbf { R } ( t ) \ \mathbf { W } ( t ) \ [ \mathrm { T R S } ( t ) ] ,
$$

where ${ \bf Q } ( t ) , { \bf R } ( t )$ , and $\mathbf { W } ( t )$ are the transformation matrices describing precession/ nutation, the rotation of the Earth, and polar motion, respectively (Petit & Luzum, 2010), and $t$ is defined by:

$$
t = [ T T - 2 0 0 0 \ \mathrm { J a n u a r y } \ 1 , 1 2 h \ T T \ \mathrm { i n \ d a y s } ] / 3 6 5 2 5 .
$$

Note that 2000 January $1 . 5 \ : \mathrm { T T = }$ Julian Date 2451545.0 TT.

The precession/nutation rotation is given by:

$$
\mathbf { Q } ( t ) = \left[ \begin{array} { c c c } { 1 - a X ^ { 2 } } & { - a X Y } & { X } \\ { - a X Y } & { 1 - a Y ^ { 2 } } & { Y } \\ { - X } & { - Y } & { 1 - a \left( X ^ { 2 } + Y ^ { 2 } \right) } \end{array} \right] \bullet \left[ \begin{array} { c c c } { \cos s } & { \sin s } & { 0 } \\ { - \sin s } & { \cos s } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] ,
$$

$$
a = { ^ 1 } / { _ { 2 } } + { ^ 1 } / { _ { 8 } } ( X ^ { 2 } + Y ^ { 2 } ) ,
$$

where $X$ and $Y$ are the angular “coordinates” of the Conventional Intermediate Pole (CIP) in the CRS, provided in part by the conventional mathematical models, and $s$ is given by Equations (5.3–5.5). For the highest precision, it is necessary to account for the differences between the observed value and the theoretical model. Mathematically:

$$
\begin{array} { r } { X = X _ { \mathrm { M O D E L } } + \delta X } \\ { Y = Y _ { \mathrm { M O D E L } } + \delta Y , } \end{array}
$$

where $X _ { \mathrm { M O D E L } }$ and $Y _ { \mathrm { M O D E L } }$ are the values provided by the models and $\delta X$ and $\delta Y$ are the celestial pole along the meridian of $9 0 ^ { \circ }$ east observations.

The Earth’s rotation angle is handled by the matrix:

$$
\mathbf { R } ( t ) = \left[ \begin{array} { c c c } { \cos \theta } & { - \sin \theta } & { 0 } \\ { \sin \theta } & { \cos \theta } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] ,
$$

$\theta$ being the Earth Rotation Angle given by:

$$
\theta ( T _ { u } ) = 2 \pi { \left( \begin{array} { l l } { { \mathrm { U T 1 ~ J u l i a n ~ D a y s ~ e l a p s e d ~ s i n c e ~ } } 2 4 5 1 5 4 5 . 0 + 0 . 7 7 9 0 5 7 2 7 3 2 6 4 0 } \\ { { + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 4 8 \ T _ { u } } } \end{array} \right) }
$$

where $T _ { u } =$ (Julian UT1 date − 2451545.0), and $U T I = U T C + ( U T I - U T C )$ .

Finally the polar motion rotation is given by:

$$
\mathbf { W } ( t ) = \left[ \begin{array} { c c c } { \cos s ^ { \prime } } & { - \sin s ^ { \prime } } & { 0 } \\ { \sin s ^ { \prime } } & { \cos s ^ { \prime } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \bullet \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos y } & { \sin y } \\ { 0 } & { - \sin y } & { \cos y } \end{array} \right] \bullet \left[ \begin{array} { c c c } { \cos x } & { 0 } & { - \sin x } \\ { 0 } & { 1 } & { 0 } \\ { \sin x } & { 0 } & { \cos x } \end{array} \right] .
$$

where $x$ and $y$ are the angular “coordinates” of the Conventional Intermediate Pole in the TRS and $\mathbf { s } ^ { \prime }$ in microarcseconds $( \mu \mathrm { a s } )$ can be approximated for the 21st century by:

$$
s ^ { \prime } = - 4 7 ~ \mu \mathrm { a s } ~ t .
$$

where $t$ is given in Equation (18.2) and the angles $X , ~ Y ,$ UT1−UTC, $x$ , and $y$ collectively are known as the Earth orientation parameters, which must be determined by observation.

# 18.2 Determination of Earth Orientation Parameters
