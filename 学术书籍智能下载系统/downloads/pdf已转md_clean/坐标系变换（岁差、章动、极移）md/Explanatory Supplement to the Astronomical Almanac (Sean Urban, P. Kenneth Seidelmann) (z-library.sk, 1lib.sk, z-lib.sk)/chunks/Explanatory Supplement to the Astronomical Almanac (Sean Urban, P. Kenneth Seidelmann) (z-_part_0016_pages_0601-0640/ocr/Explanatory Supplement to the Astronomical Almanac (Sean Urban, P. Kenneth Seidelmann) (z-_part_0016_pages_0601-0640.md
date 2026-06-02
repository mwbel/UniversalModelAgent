Table14.5 Formulae for plane and spherical triangles (The anglesof the triangleare denoted by $A$ , $B$ , $C$ ；theopposite sides,by $a , b , c$ Other formulae may be obtainedby cyclic changesof $A$ ， $B$ , $C$ and $a , b , c . )$   

<table><tr><td>PlaneTriangle</td><td>Spherical Triangle</td></tr><tr><td>a sinB=bsin A</td><td>sina sinB= sinbsinA</td></tr><tr><td>acosB=c-bcosA</td><td>sinacosB= cosb sinc-sinbcosccosA</td></tr><tr><td>a²=b²+c²-2bccosA</td><td>cosa= cosb cosc+sinb sinccos A</td></tr><tr><td>acosC=b-ccosA</td><td>sin a cosC= sin bcosc-cosb sinccos A</td></tr><tr><td>a sinC=csinA</td><td>sina sinC = sin c sin A</td></tr><tr><td>sin(B+C）=cos¹A</td><td>cos¹asin(B+C)=cosAcos(b-c)</td></tr><tr><td>cos²(B+C）=sinA</td><td>cos¹acos↓(B+C)=sin↓Acos↓(b+c)</td></tr><tr><td>a sin¹(B-C)=(b-c)cos¹A</td><td>sin¹asin↓(B-C)=cos↓Asin¹(b-c)</td></tr><tr><td>acos↓(B-C)=(b+c)sin¹A</td><td>sin¹acos↓(B-C)=sin↓Asin↓(b+c)</td></tr><tr><td>s=(a+b+c)</td><td>s=（a+b+c）</td></tr><tr><td>r²=(s-a)(-b)(s-c)/s</td><td>m²=sin(s-a)sin(s-b)sin(s-c) sin s</td></tr><tr><td>Area=sr=bc sin A</td><td>Area=A+B+C-180°</td></tr><tr><td>bcsin²¹A=(s-b)(s-c)</td><td>sinb sinc sin²1A= sin(s-b) sin(s-c)</td></tr><tr><td>bccos²A=s(s-a)</td><td>sinb sinccos²¹A= sins sin(s-a)4</td></tr><tr><td>tan¹A=r/(s-a)</td><td>tan¹A=m/sin(s-a)</td></tr></table>

<table><tr><td>Additional Formulae</td><td>Right-angled Triangle A=90°</td></tr><tr><td>sinA sinb= sinB sina</td><td>sina sin B = sin b</td></tr><tr><td></td><td>sina cosB= cosb sin c</td></tr><tr><td></td><td>cos a = cos b cos c</td></tr><tr><td></td><td>sina cosC = sin bcosc</td></tr><tr><td>sinA sin c = sin Csin a</td><td>sina sinC = sinc</td></tr><tr><td>cos a cosB = sina cotc-sinBcot C</td><td>sinB cos a = cosb cosC</td></tr><tr><td>cos a cosC = sin a cot b-sin C cot B</td><td>cos B = cos b sin C</td></tr><tr><td>cosb cosA = sinbcot c-sinAcotC</td><td>sin B cosc = cosC</td></tr><tr><td>cos c cosA = sinccotb-sin AcotB</td><td>sinB sinc = sinb sin C</td></tr><tr><td>S=(A+B+C)</td><td>tana= tan b sec C</td></tr><tr><td>M²=-cos(S-A) cos(S-B)cos(S-C)/cos S</td><td>tana= tanc sec B</td></tr><tr><td>sin B sinCsin²a =-cosScos(S-A)</td><td>cosa= cot Bcot C</td></tr><tr><td>sin B sin c cos²</td><td>tanb= sinc tan B</td></tr><tr><td>tana=cos(S-A)/M</td><td>tanc= sinbtanC</td></tr></table>

Table14.5 (continued)   

<table><tr><td colspan="3">Quadrantal Triangle: a =90°</td></tr><tr><td>sin A sinb= sin B</td><td>sinb sin A = sin B</td><td>tanA=-tanBsec c</td></tr><tr><td>sin A cosb = cosB sinC</td><td>sin bcosA= -cosBcosc</td><td>tanA=-tanCsec b</td></tr><tr><td>cosA=-cosBcosC</td><td>cos b= cosB sinc</td><td>cosA=-cot bcot c</td></tr><tr><td>sin A cosc = sinB cosC</td><td>sin b cosC = cos c</td><td>tanB= sinC tanb</td></tr><tr><td>sin A sinc = sin C</td><td>sinb sinC = sinB sinc</td><td>tanc= sinB tanc</td></tr></table>

<table><tr><td>Spherical TriangleinWhichbis Small</td></tr><tr><td>a-c=-b cos A+↓b²cot c sin²A+..</td></tr><tr><td></td></tr><tr><td>BsinC=+bA+b²cotc sin2A+... 180°-C-A=+bcotcsinA+b²(1+2cot²c)sin2A+...</td></tr></table>

![](images/54affab813d5c61a3685ffbcd414043b53dc2e73e48182b18fd30d4be2338663.jpg)  
Figure14.3 Arc of circle

# 14.4 Matrix and Vector Techniques

# 14.4.1 Matrix Multiplication

Two matrices $\mathbf { A }$ and $\mathbf { B }$ form the product AB,where the superscript indicates the row and the subscript indicates the column,

$$
 \begin{array} { r l } { \mathbf { A } = { [ \begin{array} { l l l } { a _ { 1 } ^ { 1 } } & { a _ { 2 } ^ { 1 } } & { a _ { 3 } ^ { 1 } } \\ { a _ { 1 } ^ { 2 } } & { a _ { 2 } ^ { 2 } } & { a _ { 3 } ^ { 2 } } \\ { a _ { 1 } ^ { 3 } } & { a _ { 2 } ^ { 3 } } & { a _ { 3 } ^ { 3 } } \end{array} ] } , \quad } & { \mathbf { B } = { [ \begin{array} { l l l } { b _ { 1 } ^ { 1 } } & { b _ { 2 } ^ { 1 } } & { b _ { 3 } ^ { 1 } } \\ { b _ { 1 } ^ { 2 } } & { b _ { 2 } ^ { 2 } } & { b _ { 3 } ^ { 2 } } \\ { b _ { 1 } ^ { 3 } } & { b _ { 2 } ^ { 3 } } & { b _ { 3 } ^ { 3 } } \end{array} ] } } \\  \mathbf { A } \mathbf { B } =  [ \begin{array} { l l l } { a _ { 1 } ^ { 1 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 1 } ^ { 3 } } & { a _ { 1 } ^ { 1 } b _ { 2 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 2 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 2 } ^ { 3 } } & { a _ { 1 } ^ { 1 } b _ { 3 } ^ { 1 } + a _ { 2 } ^ { 1 } b _ { 3 } ^ { 2 } + a _ { 3 } ^ { 1 } b _ { 3 } ^ { 3 } } \\ { a _ { 1 } ^ { 2 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 1 } ^ { 3 } } & { a _ { 1 } ^ { 2 } b _ { 2 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 2 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 2 } ^ { 3 } } & { a _ { 1 } ^ { 2 } b _ { 3 } ^ { 1 } + a _ { 2 } ^ { 2 } b _ { 3 } ^ { 2 } + a _ { 3 } ^ { 2 } b _ { 3 } ^ { 3 } } \\ { a _ { 1 } ^ { 3 } b _ { 1 } ^ { 1 } + a _ { 2 } ^ { 3 } b _ { 1 } ^ { 2 } + a _ { 3 } ^ { 3 } b _ { 1 } ^ { 3 } } \end{array} \end{array}
$$

# 14.4.2 Rotation of Axes Using Matrices

In practical computations it is often necessary to change the orientation of reference frames.   
This is frequently done by performing three rotations,one each about the $x$ , $y$ ,and $z$ axes.

In TheAstronomical Almanac,these matricesare designated $\mathbf { R } _ { 1 }$ , $\mathbf { R } _ { 2 }$ ,and $\mathbf { R } _ { 3 }$ respectively. Givena right-handed system of rectangular coordinates $x$ , $y$ ，z,and rotating the system positively through the angle $\phi _ { 1 }$ about the $x$ -axis (i.e.,counterclockwiseas viewed from the $+ x$ direction),the new coordinates $x ^ { \prime }$ , $y ^ { \prime }$ , $z ^ { \prime }$ are related to the original coordinates by

$$
\begin{array} { l } { x ^ { \prime } = x } \\ { y ^ { \prime } = y \cos \phi _ { 1 } + z \sin \phi _ { 1 } } \\ { z ^ { \prime } = - y \sin \phi _ { 1 } + z \cos \phi _ { 1 } . } \end{array}
$$

In matrix notation,this becomes

$$
\left[ \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] = \mathbf { R } _ { 1 } ( \phi _ { 1 } ) \left[ \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right] , \quad \mathrm { w h e r e } \ \mathbf { R } _ { 1 } ( \phi _ { 1 } ) = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \phi _ { 1 } } & { \sin \phi _ { 1 } } \\ { 0 } & { - \sin \phi _ { 1 } } & { \cos \phi _ { 1 } } \end{array} \right] .
$$

Similarly,forapositiverotation $\phi _ { 2 }$ about the $y$ -axis,

$$
\left[ \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] = \mathbf { R } _ { 2 } ( \phi _ { 2 } ) \left[ \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right] , \quad \mathrm { w h e r e ~ } \mathbf { R } _ { 2 } ( \phi _ { 2 } ) = \left[ \begin{array} { c c c } { \cos \phi _ { 2 } } & { 0 } & { - \sin \phi _ { 2 } } \\ { 0 } & { 1 } & { 0 } \\ { \sin \phi _ { 2 } } & { 0 } & { \cos \phi _ { 2 } } \end{array} \right] .
$$

Again,forapositive rotation $\phi _ { 3 }$ about the $z$ -axis,

$$
\left[ \begin{array} { c } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] = \mathbf { R } _ { 3 } ( \phi _ { 3 } ) \left[ \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right] , \quad \mathrm { w h e r e ~ } \mathbf { R } _ { 3 } ( \phi _ { 3 } ) = \left[ \begin{array} { c c c } { \cos \phi _ { 3 } } & { \sin \phi _ { 3 } } & { 0 } \\ { - \sin \phi _ { 3 } } & { \cos \phi _ { 3 } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] .
$$

The equation for two positive rotations may be written as

$$
\left[ \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ { z ^ { \prime } } \end{array} \right] = \mathbf { R } _ { 1 } ( \phi _ { 1 } ) \mathbf { R } _ { 2 } ( \phi _ { 2 } ) \left[ \begin{array} { c c c c c c c c c c c c } { x } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { y } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { z ^ { \prime } } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \end{array} \right]
$$

where the matrix product $\mathbf { R } _ { 1 } ( \phi _ { 1 } ) \mathbf { R } _ { 2 } ( \phi _ { 2 } )$ is

$$
\left[ \begin{array} { c c c } { \cos \phi _ { 2 } } & { 0 } & { - \sin \phi _ { 2 } } \\ { \sin \phi _ { 1 } \sin \phi _ { 2 } } & { \cos \phi _ { 1 } } & { \sin \phi _ { 1 } \cos \phi _ { 2 } } \\ { \cos \phi _ { 1 } \sin \phi _ { 2 } } & { - \sin \phi _ { 1 } } & { \cos \phi _ { 1 } \cos \phi _ { 2 } } \end{array} \right] .
$$

For three successive positive rotations $( \phi _ { 1 } ) , ( \phi _ { 2 } ) , ( \phi _ { 3 } )$ about the $x \mathrm { - , ~ y - }$ ,and $Z$ -axes,respectively

$$
{ \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] } = \mathbf { R } _ { 1 } ( \phi _ { 1 } ) \mathbf { R } _ { 2 } ( \phi _ { 2 } ) \mathbf { R } _ { 3 } ( \phi _ { 3 } ) { \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] }
$$

where the matrix product of $\mathbf { R } _ { 1 } ( \phi _ { 1 } ) \mathbf { R } _ { 2 } ( \phi _ { 2 } ) \mathbf { R } _ { 3 } ( \phi _ { 3 } )$ is

$$
\left[ \begin{array} { c c c } { \cos \phi _ { 2 } \cos \phi _ { 3 } } & { \cos \phi _ { 2 } \sin \phi _ { 3 } } & { - \sin \phi _ { 2 } } \\ { \sin \phi _ { 1 } \sin \phi _ { 2 } \cos \phi _ { 3 } - \cos \phi _ { 1 } \sin \phi _ { 3 } } & { \sin \phi _ { 1 } \sin \phi _ { 2 } \sin \phi _ { 3 } + \cos \phi _ { 1 } \cos \phi _ { 3 } } & { \sin \phi _ { 1 } \cos \phi _ { 2 } } \\ { \cos \phi _ { 1 } \sin \phi _ { 2 } \cos \phi _ { 3 } + \sin \phi _ { 1 } \sin \phi _ { 3 } } & { \cos \phi _ { 1 } \sin \phi _ { 2 } \sin \phi _ { 3 } - \sin \phi _ { 1 } \cos \phi _ { 3 } } & { \cos \phi _ { 1 } \cos \phi _ { 2 } } \end{array} \right] .
$$

This case comprises a rotation $( \phi _ { 1 } )$ about the $x$ -axis,arotation $( \phi _ { 2 } )$ around the new position of the $y$ -axis,andarotation $( \phi _ { 3 } )$ around the final position of the $z$ -axis.

The matrix denoting any number of rotations can be derived by multiplication following the precepts below.

# 14.4.3Spherical Coordinates Using Vectors

Considera triangle $A B C$ (Fig.14.1) scribed on the surface of a sphere of unit radiuswhose center is denoted by $o$ .Each side abc is a portion of a great circle defined by $B O C = a$ , $A O C = b$ ,and $A O B = c$ .

$A$ is the angle between the planes $B O A$ and $C O A$ , $B$ is the angle between the planes $A O B$ and $C O B$ ,and $C$ is the angle between planes $A O C$ and $B O C$ .

Take 1, $\mathbf { m } , \mathbf { n }$ ,as nonorthogonal unit vectors along $O A$ , $O B$ ,and $o c$ respectively. The cross productl $\times \textbf { m }$ is a vector of magnitude sin $c$ directed orthogonally to the plane $A O B$ . In the same manner,the cross product $\mathbf { l } \times \mathbf { n }$ is a vector of magnitude sin $^ b$ orthogonal to $A O C$ $A$ is the angle between these two vectors.

The dot product of these two vectors is

$$
\begin{array} { r l } & { ( \mathbf { l } \times \mathbf { m } ) \cdot ( \mathbf { l } \times \mathbf { n } ) = \sin c \sin b \cos A } \\ & { \qquad = \mathbf { l } \cdot [ \mathbf { m } \times ( \mathbf { l } \times \mathbf { n } ) ] } \\ & { \qquad = \mathbf { l } \cdot [ \mathbf { l } ( \mathbf { m } \cdot \mathbf { n } ) - \mathbf { n } ( \mathbf { l } \cdot \mathbf { m } ) ] } \\ & { \qquad = \left( \mathbf { m } \cdot \mathbf { n } \right) - \left( \mathbf { l } \cdot \mathbf { n } \right) ( \mathbf { l } \cdot \mathbf { m } ) } \\ & { \qquad = \cos a - \cos b \cos c } \end{array}
$$

which gives

$$
\cos a = \cos b \cos c + \sin b \sin c \cos A .
$$

Similar equations for cos $^ b$ and cos $c$ are easily obtained.

From the definition of the vector product,we find

$$
{ \begin{array} { r l } & { \sin A = { \frac { | ( \mathbf { 1 } \times \mathbf { m } ) \times ( \mathbf { 1 } \times \mathbf { n } ) | } { | \mathbf { 1 } \times \mathbf { m } | \mathbf { \phi } | \mathbf { 1 } \times \mathbf { n } | } } } \\ & { \qquad = { \frac { | \mathbf { - } \mathbf { l } [ \mathbf { m } , \mathbf { l } , \mathbf { n } ] + \mathbf { m } [ \mathbf { l } , \mathbf { l } , \mathbf { n } ] | } { \sin b \sin c } } } \\ & { \qquad = { \frac { [ \mathbf { l } , \mathbf { m } , \mathbf { n } ] } { \sin b \sin c } } . } \end{array} }
$$

Thus,

$$
{ \frac { \sin A } { \sin a } } = { \frac { \sin B } { \sin b } } = { \frac { \sin C } { \sin c } } .
$$

![](images/83ea888f290ee812f46affae27ed3b17bd8a2631c1e610f5a79e0b38cde44316.jpg)  
Figure14.4 Triangle on unit sphere

Other formulae of spherical trigonometry (see Table 14.5）may be obtained from Eqs.14.38 and 14.39.

An example of the application of vectors to the solution of a problem in spherical trigonometry concerns transforming the coordinates of a star from right ascension $( \alpha )$ and declination (δ) to ecliptic longitude $( \lambda )$ and latitude $( \beta )$ .

Given the triangle $E Q S$ (Fig.14.4) on a sphere of unit radius with center at $o$ , $\boldsymbol { Q }$ isthe pole of the celestial equator, $E$ is the pole of the ecliptic,and $s$ is the star.

The side $E Q$ is the obliquity of the ecliptic $( \epsilon )$ ,theside $\boldsymbol { Q } \boldsymbol { S }$ is $9 0 ^ { \circ } - \delta$ ,and the side $E S$ is $9 0 ^ { \circ } - \beta$ .Two great circles passing through $E$ and $\boldsymbol { Q }$ ，each being orthogonal to side $E S$ ,intersect the equator and ecliptic planes at the vernal equinox.Then the angle $E Q S = 9 0 ^ { \circ } + \alpha$ ,andtheangle $S E Q = 9 0 ^ { \circ } - \lambda$

Using these quantities the problem is easily solved by the equations previously derived:

$$
\begin{array} { c } { \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \alpha \sin \epsilon } \\ { \cos \beta \cos \lambda = \cos \delta \cos \alpha } \\ { \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \sin \alpha \cos \epsilon . } \end{array}
$$

The problem can also be solved by the use of vectors.Assume axes l, $\mathbf { m }$ ,n(forming the conventional right-handed triad) withl pointing to the vernal equinox and $\mathbf { n }$ directed toward the north pole of the equator $( \varrho )$ .Alsoassume the right-handed triad $\mathbf { u }$ , $\mathbf { v }$ ,wwithudirected to the vernal equinox and $\mathbf { w }$ toward the pole of the ecliptic $( E )$ .

Then

$$
\begin{array} { l } { \mathbf { u } = \mathbf { l } } \\ { \mathbf { v } = \mathbf { m } \cos \epsilon - \mathbf { n } \sin \epsilon } \\ { \mathbf { w } = \mathbf { m } \sin \epsilon + \mathbf { n } \cos \epsilon . } \end{array}
$$

The components of $o s$ projected onto the equatorial and ecliptic axes are

$$
\begin{array} { r l r } { \cos \delta \cos \alpha , } & { \cos \delta \sin \alpha , } & { \sin \delta , } \\ { \cos \beta \cos \lambda , } & { \cos \beta \sin \lambda , } & { \sin \beta , } \end{array}
$$

leading to the original trigonometric equations.

# 14.4.4 Specific Coordinate Transformations

# 14.4.4.1 GeocentricCoordinate Transformations

For geocentric spherical coordinates there are the four practical reference systems of:

1.Azimuth/Altitude System:Azimuth (A) ismeasured from the north through east in the plane of the horizon,and altitude (a) measured perpendicular to the horizon. In astronomy,the zenith distance( $z = 9 0 ^ { \circ } - a )$ ismore generallyused,but the altitude is retained in the formulae for reasons of symmetry.   
2.Hour Angle/Declination System:Hour angle $( h )$ is measured westward in the plane ofthe equator from the meridian,and declination (δ)ismeasured perpendicular to the equator,positive to the north.   
3.Right Ascension/Declination System:Right ascension $( a )$ is measured from the equinox or CIO eastward in the plane of the equator,and declination (δ) is measured perpendicular to the equator, positive to the north.   
4.Longitude/Latitude System: Longitude (λ) is measured from the equinox eastward in the plane of the ecliptic,and latitude $( \beta )$ is measured perpendicular to the ecliptic, positive to the north.

Formulae for transforming equatorial right ascensionand declination toecliptic longitude andlatitude may be written using direction cosines (unit vectors) and (rotation matrices) as follows:

$$
\left[ \begin{array} { c c c } { \cos \beta \cos \lambda } \\ { \cos \beta \sin \lambda } \\ { \sin \beta } \end{array} \right] = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \epsilon } & { \sin \epsilon } \\ { 0 } & { - \sin \epsilon } & { \cos \epsilon } \end{array} \right] \left[ \begin{array} { c c c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right] .
$$

The inverse transformation,using $[ R _ { \epsilon } ]$ to denote the rotation matrix,is

$$
\left[ \begin{array} { c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right] = [ R _ { \epsilon } ] ^ { - 1 } \left[ \begin{array} { c } { \cos \beta \cos \lambda } \\ { \cos \beta \sin \lambda } \\ { \sin \beta } \end{array} \right] .
$$

The transformations correspond to simple rotations about the $x$ -axisthrough $\epsilon$ ,which is the obliquity of the ecliptic corresponding to the particular equator and ecliptic used.

Transformation from right ascension/declination to local hour angle/declination may be carried out by substitution of

$$
h = \mathrm { l o c a l s i d e r e a l t i m e } - \alpha .
$$

The two systems are identical apart from the origin and direction angular measurement. The transformation may also be considered as a rotation about the axis perpendicular to the equatorial plane and positive in the direction of the North Pole.Thus,

$$
\left[ \begin{array} { c c c } { \cos \delta \cos h } \\ { \cos \delta \sin h } \\ { \sin \delta } \end{array} \right] = \left[ \begin{array} { c c c } { \cos t _ { s } } & { \sin t _ { s } } & { 0 } \\ { - \sin t _ { s } } & { \cos t _ { s } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right]
$$

where $t _ { s }$ is the local sidereal time.

Transformation of local hour angle/declination to azimuth/altitude involvesarotation of thereference frame through an angle $9 0 ^ { \circ } - \phi$ in the plane of the meridian,where $\phi$ isthe geocentric latitude,followed by a rotation about the new vertical by $1 8 0 ^ { \circ }$ .Thus,

$$
{ \left[ \begin{array} { l } { \cos a \cos A } \\ { \cos a \sin A } \\ { \sin a } \end{array} \right] } = { \left[ \begin{array} { l l l } { - 1 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { \sin \phi } & { 0 } & { - \cos \phi } \\ { 0 } & { 1 } & { 0 } \\ { \cos \phi } & { 0 } & { \sin \phi } \end{array} \right] } { \left[ \begin{array} { l } { \cos \delta \cos h } \\ { \cos \delta \sin h } \\ { \sin \delta } \end{array} \right] }
$$

In this transformation the diagonal matrix is its own inverse and,if $[ R _ { \phi } ]$ denotes the rotation in the meridian plane with inverse, then

$$
[ R _ { \phi } ] ^ { - 1 } = \left[ \begin{array} { c c c } { { \sin \phi } } & { { 0 } } & { { \cos \phi } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \cos \phi } } & { { 0 } } & { { \sin \phi } } \end{array} \right]
$$

and

$$
\left[ \begin{array} { l } { \cos \delta \cos h } \\ { \cos \delta \sin h } \\ { \sin \delta } \end{array} \right] = [ R _ { \phi } ] ^ { - 1 } \left[ \begin{array} { c c c } { - 1 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { \cos a \cos A } \\ { \cos a \sin A } \\ { \sin a } \end{array} \right] .
$$

The corresponding equatorial rectangular coordinates and distance are denoted by $X$ , $Y$ , $Z$ ,and $R$ for the Sun and by $\xi , \eta , \zeta$ ,and $\Delta$ forthe planets;they are derived from the spherical coordinates by the formulae:

$$
\begin{array} { l } { \displaystyle \frac { X } { R } ~ \mathrm { o r } ~ \frac { \xi } { \Delta } = \cos \delta \cos \alpha } \\ { \displaystyle \frac { Y } { R } ~ \mathrm { o r } ~ \frac { \eta } { \Delta } = \cos \delta \sin \alpha } \\ { \displaystyle \frac { Z } { R } ~ \mathrm { o r } ~ \frac { \zeta } { \Delta } = \sin \delta . } \end{array}
$$

Geocentric ecliptic rectangular coordinates are rarely (if ever) used.

# 14.4.4.2 Heliocentric Coordinate Transformations

For heliocentric coordinates there are only the two practical reference systems-the equatorial and the ecliptic.In the equatorial system onlyrectangular coordinates are used.The relationships between the ecliptic rectangular coordinates $( x _ { c } , y _ { c } , z _ { c } )$ ,the ecliptic longitude, latitude,and distance $( l , b , r )$ ,and the equatorial rectangular coordinates $( x , y , z )$ are

$$
\left[ \begin{array} { c c c } { x _ { c } } & { = } & { r \cos b \cos l } \\ { y _ { c } } & { = } & { r \cos b \sin l } \\ { z _ { c } } & { = } & { r \sin b } \end{array} \right] = [ R _ { \epsilon } ] \left[ \begin{array} { c c c } { x } \\ { y } \\ { z } \end{array} \right]
$$

$$
\left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] = [ R _ { \epsilon } ] ^ { - 1 } \left[ \begin{array} { l } { x _ { c } } \\ { y _ { c } } \\ { z _ { c } } \end{array} \right] .
$$

The conversion from heliocentric to geocentric coordinates is performed in terms of equatorial rectangular coordinates using

$$
\begin{array} { c } { { \xi = x + X } } \\ { { \eta = y + Y } } \\ { { \zeta = z + Z } } \end{array}
$$

where $X$ ,Y, $Z$ are the geocentric coordinates of the Sun.

The calculation of the spherical coordinates from the rectangular coordinates,or from the known direction cosines,typified by

$$
\begin{array} { r } { \Delta \cos \delta \cos \alpha = \xi } \\ { \Delta \cos \delta \sin \alpha = \eta } \\ { \Delta \sin \delta = \zeta } \end{array}
$$

is performed by

$$
\begin{array} { c } { \Delta = \sqrt { \xi ^ { 2 } + \eta ^ { 2 } + \zeta ^ { 2 } } } \\ { \cot \alpha = \xi / \eta } \\ { \sin \delta = \zeta / \Delta . } \end{array}
$$

The quadrant of $\alpha$ is determined by the signs of $\xi$ and $\eta$ ,and that of $\delta$ by the sign of $\zeta . \Delta$ and $\Delta \cos \delta$ arealwayspositive.The formulae for $\alpha$ and $\delta$ may be written as

$$
\begin{array} { r l } { \alpha = \tan ^ { - 1 } \eta / \xi , ~ } & { \mathrm { o r ~ } \arctan \eta / \xi , } \\ { \quad } & { \mathrm { o c o t } ^ { - 1 } \xi / \eta , ~ \mathrm { o r ~ } \operatorname { a r c c o t } \xi / \eta , } \\ { \quad } & { \delta = \sin ^ { - 1 } \zeta / \Delta , ~ \mathrm { o r ~ } \arcsin \zeta / \Delta , } \end{array}
$$

provided that the appropriate values,and not necessarily the principal values,of the multivalued functionsare taken.

Many of the conversions above correspond to a simple rotation of the frame of reference about one of its axes.These are special cases of the general conversion from a set of axes designated by $x , y , z$ to a set designated by $x ^ { \prime }$ , $y ^ { \prime } , z ^ { \prime }$ .The two systems are connected by the formulae

$$
\begin{array} { l l } { x = l _ { 1 } x ^ { \prime } + l _ { 2 } y ^ { \prime } + l _ { 3 } z ^ { \prime } } & { x ^ { \prime } = l _ { 1 } x + m _ { 1 } y + n _ { 1 } z } \\ { y = m _ { 1 } x ^ { \prime } + m _ { 2 } y ^ { \prime } + m _ { 3 } z ^ { \prime } } & { y ^ { \prime } = l _ { 2 } x + m _ { 2 } y + n _ { 2 } z } \\ { z = n _ { 1 } x ^ { \prime } + n _ { 2 } y ^ { \prime } + n _ { 3 } z ^ { \prime } } & { z ^ { \prime } = l _ { 3 } x + m _ { 3 } y + n _ { 3 } z } \end{array}
$$

where $l _ { 1 } , m _ { 1 } , n _ { 1 } ; l _ { 2 } , m _ { 2 } , n _ { 2 }$ and $l _ { 3 } , m _ { 3 } , n _ { 3 }$ are the direction cosines of $x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ referred to the system $x , y , z$ .The direction cosines satisfy the relations typified by

$$
\begin{array} { r } { l _ { 1 } ^ { 2 } + m _ { 1 } ^ { 2 } + n _ { 1 } ^ { 2 } = 1 } \\ { \quad l _ { 2 } l _ { 3 } + m _ { 2 } m _ { 3 } + n _ { 2 } n _ { 3 } = 0 } \\ { \quad l _ { 1 } ^ { 2 } + l _ { 2 } ^ { 2 } + l _ { 3 } ^ { 2 } = 1 } \\ { m _ { 1 } n _ { 1 } + m _ { 2 } n _ { 2 } + m _ { 3 } n _ { 3 } = 0 . } \end{array}
$$

These nine quantities can be expressed interms of the Eulerian angles $\theta , \phi , \psi$ as

$$
\begin{array} { r l } & { l _ { 1 } = + \cos \phi \cos \theta \cos \psi - \sin \phi \sin \psi } \\ & { l _ { 2 } = - \cos \phi \cos \theta \sin \psi - \sin \phi \cos \psi } \\ & { l _ { 3 } = + \cos \phi \sin \theta } \\ & { m _ { 1 } = + \sin \phi \cos \theta \cos \psi + \cos \phi \sin \psi } \\ & { m _ { 2 } = - \sin \phi \cos \theta \sin \psi + \cos \phi \cos \psi } \\ & { m _ { 3 } = + \sin \phi \sin \theta } \\ & { n _ { 1 } = - \sin \theta \cos \psi } \\ & { n _ { 2 } = + \sin \theta \sin \psi } \\ & { n _ { 3 } = + \cos \theta . } \end{array}
$$

In this case the conversion corresponds to a rotation $\phi$ about the $Z$ -axis, $\theta$ about the new position of the $y$ -axis,and $\psi$ about the new (and final) position of the $Z$ -axis.The transformation is equivalent toa single rotationabout some line not in general coincident with one of the axes; but such single rotations are not frequently encountered in astronomical practice.

# 14.5 Numerical Calculus

# 14.5.1Numerical Differentiation

Successive derivatives of afunctionare closely related to the successive orders of differences. Thusto obtain the exact expression for the derivatives in terms of differences it is necessary merely to differentiate any of the interpolation formulae (see $\ S \ 1 4 . 2$ ）asmanytimesas required.

Differentiation of Bessel's interpolation formula leads to

$$
h f _ { p } ^ { \prime } = \delta _ { 1 / 2 } + \frac { 1 } { 2 } \left( p - \frac { 1 } { 2 } \right) ( \delta _ { 0 } ^ { 2 } + \delta _ { 1 } ^ { 2 } ) + \frac { 1 } { 1 2 } ( 1 - 6 p + 6 p ^ { 2 } ) \delta _ { 1 / 2 } ^ { 3 } + \cdot \cdot \cdot
$$

where $f _ { p } ^ { \prime }$ denotes the value of $d f / d t$ at the point $t = t _ { 0 } + p h$

This formula is intended for usein the range $0 \leq p \leq 1$ ；the maximum value of the third-difference coefficient is $1 / 1 2$ and occurs at $p = 0$ and 1.At $p = 1 / 2$ the formula reduces to

$$
h f _ { 1 / 2 } ^ { \prime } = \delta _ { 1 / 2 } - \frac { 1 } { 2 4 } \delta _ { 1 / 2 } ^ { 3 } + \frac { 3 } { 6 4 0 } \delta _ { 1 / 2 } ^ { 5 } - \cdot \cdot \cdot .
$$

Differentiation of Stirling's interpolation formula leads to

$$
h f _ { p } ^ { \prime } = \mu \delta _ { 0 } + p \delta _ { 0 } ^ { 2 } - \frac { 1 } { 6 } ( 1 - 3 p ^ { 2 } ) \mu \delta _ { 0 } ^ { 3 } + \cdot \cdot \cdot
$$

were, for eample, $\mu \delta _ { 0 } ^ { 3 } = \textstyle { \frac { 1 } { 2 } } ( \delta _ { - 1 / 2 } ^ { 3 } + \delta _ { 1 / 2 } ^ { 3 } )$ i $- 1 / 2 \le p \le 1 / 2$ ；the maximum value of the coefficient of the mean third differenceis $1 / 6$ and occurs at $p = 0$ .At $p = 0$ the formula reduces to

$$
h f _ { 0 } ^ { \prime } = \mu \delta _ { 0 } - \frac { 1 } { 6 } \mu \delta _ { 0 } ^ { 3 } + \frac { 1 } { 3 0 } \mu \delta _ { 0 } ^ { 5 } - \cdot \cdot \cdot .
$$

The condition for amaximum or minimum is that $f _ { p } ^ { \prime } = 0$ For Stirling's formulathis condition may be expressed as:

$$
p = \frac { - \mu \delta _ { 0 } + \frac { 1 } { 6 } ( 1 - 3 p ^ { 2 } ) \mu \delta _ { 0 } ^ { 3 } - \cdot \cdot \cdot } { \delta _ { 0 } ^ { 2 } } .
$$

This equation must normally be solved by successive approximations.The maximum contribution from the third difference is $1 / 6 \mu \delta _ { 0 } ^ { 3 } / \delta _ { 0 } ^ { 2 }$ ,and,ifthisisgligible, $\boldsymbol { p }$ may be evaluated directly from

$$
p = - \mu \delta _ { 0 } / \delta _ { 0 } ^ { 2 } = - \frac { 1 } { 2 } - \delta _ { - 1 / 2 } / \delta _ { 0 } ^ { 2 } .
$$

Inastronomical usage,the terms variation and motion are synonymous with“derivative with respect to time,”whenqualified by anadjective defining the unit of time,andare usually evaluated for the tabularpoints.The term secularvariation usuallyimpliesasecondderivative with respect to time.

The second derivative $f _ { p } ^ { \prime \prime }$ is obtained bydifferentiating the formulae for $f _ { p } ^ { \prime }$ for Stirling's formula thisleadsto

$$
h ^ { 2 } f _ { p } ^ { \prime } = \delta _ { 0 } ^ { 2 } + p \mu \delta _ { 0 } ^ { 3 } + \cdot \cdot \cdot
$$

and, when $p = 0$ ,to

$$
h ^ { 2 } f _ { p } ^ { \prime \prime } = \delta _ { 0 } ^ { 2 } - \frac { 1 } { 1 2 } \delta _ { 0 } ^ { 4 } + \frac { 1 } { 9 0 } \delta _ { 0 } ^ { 6 } - \cdot \cdot \cdot .
$$

In terms of central differences,the derivatives to order1O at the tabular point and at the half-way pointare listed in Table14.6.Primes areused to denote differentiation with respect to $x$ .For example,

$$
h ^ { 2 } f _ { p } ^ { \prime \prime } = h ^ { 2 } \frac { d ^ { 2 } } { d x ^ { 2 } } f ( x _ { 0 } + p h ) = \frac { d ^ { 2 } } { d p ^ { 2 } } f _ { p } .
$$

For higher derivatives the primes are replaced by italicized roman numerals.In general formulae, $f _ { p } ^ { ( n ) }$ isusedtodenotethenthderivativeof $f$ with respect to $x$ at the point $x _ { 0 } + p h$

The formulae in Table 14.6 may also be written by substituting for the differences theirvalues in terms of the function.Additional expressions for derivatives in terms of the functional values are as follows:

$$
\begin{array} { r l } { \rho _ { 1 } } & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( \begin{array} { c c } { \rho _ { 1 } } \\ { \rho _ { 2 } } \\ { \rho _ { 3 } } \end{array} \right) , } \\ { = \frac { 1 } { \rho _ { 1 } } \cdot \left( - \epsilon _ { 1 } + \alpha _ { 1 } - \gamma _ { 1 } - \alpha _ { 2 } \rho _ { 3 } + \frac { 1 } { \alpha _ { 1 } } \frac { \partial ^ { 2 } \rho _ { 3 } } { \partial \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \alpha _ { 3 } ^ { 2 } \rho _ { 3 } - \epsilon _ { 1 } \right) , } \\ & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 1 } + \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 1 } + \alpha _ { 2 } ^ { 2 } \cdot \gamma _ { 2 } \right) , } \\ { \rho _ { 1 } \cdot \left( - \epsilon _ { 2 } ^ { 2 } \cdot \gamma _ { 2 } - \alpha _ { 3 } \rho _ { 4 } + \alpha _ { 1 } - \frac { 1 } { 2 } \frac { \partial ^ { 2 } \rho _ { 3 } } { \partial \alpha _ { 2 } } + \alpha _ { 2 } ^ { 2 } \cdot \gamma _ { 2 } \right) , } \\ & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( 1 6 \rho _ { 1 } \cdot \gamma _ { 1 } + \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 2 } \right) , } \\ & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 1 } + 2 \gamma _ { 1 } \cdot \alpha _ { 2 } ^ { 2 } \cdot \gamma _ { 2 } + \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 2 } \right) , } \\ & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 1 } + 2 \gamma _ { 1 } \cdot \alpha _ { 2 } ^ { 2 } \cdot \gamma _ { 2 } + \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 2 } \right) , } \\ & { = \frac { 1 } { \rho _ { 1 } } \cdot \left( \alpha _ { 1 } ^ { 2 } \cdot \gamma _ { 1 } ^ { 2 } - \alpha _ { 2 } ^ { 2 } \cdot \gamma _ { 3 } ^ { 2 } \right) , } \\ &  = \frac { 1 }  \rho _ { 1 } \end{array}
$$

Forfurther formulaeseethe Interpolationand Allied Tables(H.M.Nautical Almanac Office 1956)and the Handbook of Mathematical Functions(Abramowitz and Stegun 1973).

# 14.5.2Numerical Integration

When studying motions within the solar system it is necessary to use the solution of ordinary differential equations of the second order.This normally involves the simultaneous integration of three second-order differential equations to produce an ephemeris in rectangular coordinates of a planet,comet,or satelite with time as the independent argument.

In numerical differentiation,the derivatives of a functionare expressed in terms of the differences.In numerical integration,the opposite method is used.Derivatives of some function are computed and checked bydifferencing,to forma table of $f , \delta , \delta ^ { 2 } , \delta ^ { 3 } , \delta ^ { 4 }$ ,and so on.In the simplest case,where the values of the function to be integrated can be calculated in advance,it is possible to compute a starting value of the first summation $f ^ { \prime }$ and to extend the table in either direction by applying successive values of $f$ .Fora double integration,a starting value for $f ^ { \prime \prime }$ must be evaluated and successive values of $f ^ { \prime }$ applied.Expressions to evaluate the firstand second integralsarederivedby integratinganinterpolation formula,for example,

Table14.6 Derivatives to an order of 10   

<table><tr><td>Derivativesata Tabular Point</td><td>Derivatives ataHalfway Point</td></tr><tr><td>hf=μ8o-μ8³+30μ8</td><td>hf/12=812-82+82</td></tr><tr><td>h²f=8-8+8</td><td>h²fi=μ8-u8+u8</td></tr><tr><td>h³f=μ8²-μ8+20μ8-.</td><td>h³f1=8-18+108</td></tr><tr><td>h4fi=8-8+2408-...</td><td>h4fi=18-2u8+u812</td></tr><tr><td>hf=μ8-μ8+μ8-.</td><td>h5f1=812-8+13282</td></tr><tr><td>hfi=-8+28.</td><td>hf=u8-u8+1</td></tr><tr><td>hfoii=μ8-u8+u8-.</td><td>hf=8-28+181</td></tr><tr><td>h8fi=88-80+82</td><td>h8f =μ8-μ81+781</td></tr><tr><td>hfix=μ8-μ8+...</td><td>hf2=8-81+.</td></tr><tr><td>h1of=80-28²+.</td><td>h1ofi/=μ8-2μ8+.</td></tr></table>

$$
\int ^ { 1 / 2 } f ( x ) d x = \omega \left[ f _ { 1 / 2 } ^ { \prime } + { \frac { 1 } { 2 4 } } \delta _ { 1 / 2 } - { \frac { 1 7 } { 5 7 6 0 } } \delta _ { 1 / 2 } ^ { 3 } + { \frac { 3 6 7 } { 9 6 7 6 8 0 } } \delta _ { 1 / 2 } ^ { 5 } - \cdots \right]
$$

$$
\iint ^ { 0 } f ( x ) d x ^ { 2 } = \omega ^ { 2 } \left[ f _ { 0 } ^ { \prime \prime } + { \frac { 1 } { 1 2 } } f _ { 0 } - { \frac { 1 } { 2 4 0 } } \delta _ { 0 } ^ { 2 } + { \frac { 3 1 } { 6 0 4 8 0 } } \delta _ { 0 } ^ { 4 } - \cdot \cdot \cdot \right] .
$$

Additional formulae are given in H.M.Nautical Almanac Ofice (1956) and in Abramowitz and Stegun (1973).

In the integration of orbits the problemis more complicated because the function that isto be integrated isundetermined until the integral becomes known.Thus itis necessary to proceed stepwise using extrapolation and approximation at each step.Because of the availability of computers,as wellas the rectangular coordinates of the principal planets,two methods forthe numerical integration of the orbits have proved useful,Cowell'sand Encke's.

When one is utilizing Cowell's approach,the equations of motion are integrated to give directly the positions ofthe perturbed body in rectangular coordinates.For a planet or comet, the origin usually is the Sun and at each step the atractions of the perturbing bodies would be added to that of the Sun.

With Cowell'smethod,however,the origin maybe any perturbing body,or evena double star,since no use is made of a conic section as the first approximation.The single condition is that the motions of all perturbing bodies relative to the selected origin should be known.A disadvantage of Cowell's method is that the integrals comprise numerous significant figures that vary extensively with time.Thus,the integration tables are prone to converge rather slowly,which may require the use of a short step interval.The basic equations in the Cowell approach are

$$
\ddot { x } = - k ^ { 2 } ( 1 + m ) \frac { x } { r ^ { 3 } } + \sum _ { j } k ^ { 2 } m _ { j } \left( \frac { x _ { j } - x } { \rho _ { j } ^ { 3 } } - \frac { x _ { j } } { r _ { j } ^ { 3 } } \right)
$$

with similar equations in $y$ and $Z$ .The masses are expressed in terms of the mass of the Sun, $k$ equals the Gaussian constant, $m$ is the mass of the perturbed body,and $m _ { j }$ the masses of theperturbing bodies.The first term is the attraction of the Sun on $m$ ,and the first term in parentheses is the attraction of m；on $m$ .The last term in parentheses is the action of the perturbing bodies on the Sun.

In Encke's method the unperturbed orbit of the mass $m$ about the Sun is assumed known. Hence only the difference between the unperturbed position and the perturbed position needs to be determined. The equations may be written

$$
\ddot { x } - \ddot { x } _ { 0 } = \ddot { \xi } = k ^ { 2 } ( 1 + m ) \left( \frac { x _ { 0 } } { r _ { 0 } ^ { 3 } } - \frac { x } { r ^ { 3 } } \right) + \sum _ { j } k ^ { 2 } m _ { j } \left( \frac { x _ { j } - x } { \rho _ { j } ^ { 3 } } - \frac { x _ { j } } { r _ { j } ^ { 3 } } \right)
$$

with similar equations for $\ddot { \eta }$ and $\dddot { \zeta }$ .These equations could be integrated directly,but since $\xi$ is small,many figures would have to becarried in the term $( x _ { 0 } / r _ { 0 } ^ { 3 } - x / r ^ { 3 } )$ to retain significance in the difference. On the assumption that $\xi$ , $\eta$ and $\zeta$ are so small compared to $x , y , z$ thattheir squarescanbe neglected,the equationcan be transformed by the use ofauxiliary quantities $q$ and $f$ where

$$
\begin{array} { l } { q = \frac { x _ { 0 } \xi + y _ { 0 } \eta + z _ { 0 } \zeta } { r _ { 0 } ^ { 2 } } } \\ { f = \frac { 1 - ( 1 + 2 q ) ^ { - 3 / 2 } } { q } . } \end{array}
$$

The final Encke equations become

$$
\omega ^ { 2 } \ddot { \xi } = \omega ^ { 2 } k ^ { 2 } ( 1 + m ) \frac { 1 } { r _ { 0 } ^ { 3 } } ( f q x - \xi ) + \sum _ { j } \omega ^ { 2 } k ^ { 2 } m _ { j } \left( \frac { x _ { j } - x } { \rho _ { j } ^ { 3 } } - \frac { x _ { j } } { r _ { j } ^ { 3 } } \right) .
$$

Where $\omega$ represents the interval of integration. Similar equations hold for $\ddot { \eta }$ and $\ddot { \zeta }$

Encke's procedure normally allows a larger step size than Cowell's but when close approaches happen,the Encke perturbations tend to growrapidly in size,requiringa smaller step interval.

Other approaches to the numerical solution of differential equations are provided by Runge-Kutta methods. These are single-step methods with each step being independent of those preceding.

Given:

$$
{ \frac { d x } { d t } } = f ( t , x ) ; \quad x ( t _ { 0 } ) = x _ { 0 } .
$$

A widely used Runge-Kutta method (to the fourth order) involves the following operations for one step.Here $h$ is the step interval.

$$
{ \begin{array} { l } { f _ { 0 } = f ( t _ { 0 } , x ) } \\ { f _ { 1 } = f \left( t _ { 0 } + { \frac { 1 } { 2 } } h , x _ { 0 } + { \frac { 1 } { 2 } } h f _ { 0 } \right) } \\ { f _ { 2 } = f \left( t _ { 0 } + { \frac { 1 } { 2 } } h , x _ { 0 } + { \frac { 1 } { 2 } } h f _ { 1 } \right) } \end{array} }
$$

$$
\begin{array} { r } { f _ { 3 } = f \left( t _ { 0 } + h , x _ { 0 } + h f _ { 2 } \right) } \\ { . . . } \end{array}
$$

Then

$$
x \left( t _ { 0 } + h \right) \approx x _ { 1 } = x _ { 0 } + \frac { 1 } { 6 } ( f _ { 0 } + 2 f _ { 1 } + 2 f _ { 2 } + f _ { 3 } ) .
$$

Similar equations exist in $y$ and $Z$ .

Equations to the fourth order are not suficiently accurately for most orbital calculations but this serves as an example of the method.For modifications of the method refer to Danby (1988).

In all the step-by-step methods for numerical solution of differential equations some precautions apply:

1.The interval of tabulation must be monitored in cases of close approach,since the approximations used in the iterative process may prove to be of insuficient accuracy. Automatic methods to vary the step size are now in use with some methods.   
2.The accumulation of round-off errors must be monitored. The probable error after $n$ steps can be estimated.   
3.If the method of solution adopted makes use of truncated formulae either corrections mustbe applied subsequently or the number offigures in the solution must be reduced accordingly.

Examples of numerical integrations may be found in Brouwer and Clemence (1961) and in Danby (1988).

Anexample of a multistep scheme is the Adams-Bashforth method.The order of this method is limited by the number of terms the user is wiling to compute.The formulae for this method are

$$
x _ { n + 1 } = x _ { n } + h \sum _ { k = 0 } ^ { N } \alpha _ { k } \nabla ^ { k } f _ { n }
$$

where

$$
\begin{array} { c l } { { } } & { { N = \mathrm { t h e ~ n u m b e r ~ o f ~ t e r m s } } } \\ { { } } & { { \alpha = 1 , \displaystyle \frac { 1 } { 2 } , \displaystyle \frac { 5 } { 1 2 } , \frac { 3 } { 8 } , \displaystyle \frac { 2 5 1 } { 7 2 0 } , \displaystyle \frac { 9 5 } { 2 8 8 } , \ldots } } \\ { { } } & { { } } \\ { { \nabla ^ { k } f _ { n } = \nabla ^ { k - 1 } f _ { n } - \nabla ^ { k - 1 } f _ { n - 1 } } } \\ { { } } & { { \nabla ^ { 0 } f _ { n } = f _ { n } } } \\ { { } } & { { f _ { n } = f ( x _ { n } , t _ { n } ) . } } \end{array}
$$

This method can be started using a single step method such as the Runge-Kutta.

Todifferentiallycorrect the initial conditions of the motion,one integrates seven orbits simultaneously.The first orbit uses unaltered initial conditions.Each of the rest of the orbits uses initial conditions for which one coordinate or velocity has been incremented by a small amount.Earth-based observations are right ascensions and declinations of the satellite.The residuals for these observations can be expressed as

$$
\begin{array} { r l } & { \Delta \alpha _ { i } = \cfrac { \partial \alpha _ { i } } { \partial X _ { 0 } } \Delta X _ { 0 } + \cfrac { \partial \alpha _ { i } } { \partial Y _ { 0 } } \Delta Y _ { 0 } + \cfrac { \partial \alpha _ { i } } { \partial Z _ { 0 } } \Delta Z _ { 0 } + \cfrac { \partial \alpha _ { i } } { \partial \dot { X } _ { 0 } } \Delta \dot { X } _ { 0 } + \cfrac { \partial \alpha _ { i } } { \partial \dot { Y } _ { 0 } } \Delta \dot { Y } _ { 0 } + \cfrac { \partial \alpha _ { i } } { \partial \dot { Z } _ { 0 } } \Delta \dot { Z } _ { 0 } } \\ & { \Delta \delta i = \cfrac { \partial \delta _ { i } } { \partial X _ { 0 } } \Delta X _ { 0 } + \cfrac { \partial \delta _ { i } } { \partial Y _ { 0 } } \Delta Y _ { 0 } + \cfrac { \partial \delta _ { i } } { \partial Z _ { 0 } } \Delta Z _ { 0 } + \cfrac { \partial \delta _ { i } } { \partial \dot { X } _ { 0 } } \Delta \dot { X } _ { 0 } + \cfrac { \partial \delta _ { i } } { \partial \dot { Y } _ { 0 } } \Delta \dot { Y } _ { 0 } + \cfrac { \partial \delta _ { i } } { \partial \dot { Z } _ { 0 } } \Delta \dot { Z } _ { 0 } } \end{array}
$$

where $\alpha$ and $\delta$ are the right ascension and declination respectively; $X _ { 0 } , \ Y _ { 0 } , \ Z _ { 0 } , \ \dot { X } _ { 0 } , \ \dot { Y } _ { 0 }$ and $\dot { Z } _ { 0 }$ are the initial coordinates and velocities;the subscript $i$ refers to the number of the observation.The partial derivativesare evaluated numerically,and canbe written in the form

$$
\frac { \partial \alpha _ { i } } { \partial X _ { 0 } } = \frac { \alpha _ { i } ( X _ { 0 } + \Delta X _ { 0 } , Y _ { 0 } , Z _ { 0 } , \dot { X } _ { 0 } , \dot { Y } _ { 0 } , \dot { Z } _ { 0 } ) - \alpha _ { i } ( X _ { 0 } , Y _ { 0 } , Z _ { 0 } , \dot { X } _ { 0 } , \dot { Y } _ { 0 } , \dot { Z } _ { 0 } ) } { \Delta X _ { 0 } } .
$$

The differential corrections can be written as

$$
\Delta \mathbf { R } = ( \mathbf { A } ^ { T } \mathbf { A } ) ^ { - 1 } \mathbf { A } ^ { T } \Delta \mathbf { r } .
$$

where $\Delta \mathbf { R }$ is the matrix of corrections to the initial conditions, $\mathbf { A }$ is the matrix of the partial derivatives,and $\Delta \mathbf { r }$ isthe matrixof residuals.

# 14.6 Statistics

# 14.6.1 Accumulation of Error

The formulae listed in Table 14.7 indicate the way in which errors accumulate in simple arithmetical operations.The distribution of accumulated error is usually nearly normal, whatever the distributions of the original errors,so the standard deviation of the error, calculated from theformulae,isof value in theexaminationof the differences of tabulated functions.The notation used and assumptions made in the table are:

$a _ { i }$ is the absolute error of $A _ { i }$ ,in the sense of given value minus true value.These errors are assumed to be unbiased and independent.   
$\alpha _ { i }$ isthe variance,or mean square value,of the error of $A _ { i }$ .The standard deviation of the error is the square root of variance.   
$i , m$ ,and $n$ are integers. $k$ is a known constant. $r$ isequally likely to takeany value between $- 1 / 2$ and $+ 1 / 2$ . $p$ is equally likely to take any value between O and1.   
$k , r$ ,and $p$ are considered to be free from error,that is,they are exact or are known to moresignificantfiguresthan thequantities $A _ { i }$   
$e$ is the error arising from the rounding of the final result; it is assumed that a guarding figure is kept in intermediate results. $e$ isequally likely to takeany value between $\pm 1 / 2$ so that its variance is $1 / 1 2$ ,equal to the integral of $e ^ { 2 }$ between $\pm 1 / 2$ ,inunits

Table 14.7 Accumulation of error in arithmetical operations   

<table><tr><td>Operation</td><td>AbsoluteError</td><td>Variance of Error (unit1/12)</td></tr><tr><td>£A</td><td>∑=ai</td><td>∑=α</td></tr><tr><td>mA∑_1miA；</td><td>ma∑1miAi</td><td>m²a∑_1mia</td></tr><tr><td>∑=1iAi (n large)</td><td>∑=iai</td><td>n³a ifα;=α for alli</td></tr><tr><td>kA∑=1kiA;</td><td>ka+e∑=1kiai+e</td><td>k²a+1∑i=1k²α;+1</td></tr><tr><td>krA</td><td>kra+e</td><td>1k²α+1</td></tr><tr><td>g(p)A</td><td>g(p)a+e</td><td>S{g(p)}²dp.a+1</td></tr><tr><td>∑=1p𝑖A;(for αi=α)</td><td>∑=1piai+e</td><td>(1+++·.·+2n+1）+1</td></tr><tr><td>AA</td><td>Aa1+Aa+e</td><td>A²α+A²α+1</td></tr><tr><td>A</td><td>nAn-la+e</td><td>n²A2n-2α+1</td></tr><tr><td>1</td><td>(-）a+e</td><td>(1/A4)α+1</td></tr><tr><td>A1/2</td><td>(A1/2）a+e</td><td>(A)α+1</td></tr><tr><td>茶</td><td>(）a1-（）a+e</td><td>)+1</td></tr><tr><td>nth difference of A(x)</td><td>∑=1(-1)(i&quot;)ai</td><td>α(2n!) if α is constant</td></tr><tr><td>f(A,A,...)</td><td>af af a+a+..+e</td><td>n2 （）² （） 2 α+ α+··+1</td></tr><tr><td>f(A)by direct interpolation</td><td>af&#x27;(A)+er+ei+e</td><td>{f&#x27;(A)}²α+vr+v+1</td></tr><tr><td>f(A) by inverse interpolation</td><td>(a-er-et)f&#x27;(A)+e</td><td>{f&#x27;(A)}²(α+vr+vt）+1</td></tr></table>

of the last place retained.For convenience all variances are expressed in this unit of 1/12.

In addition, $e _ { r }$ is the erordue to therounding-off errors in the tabular values,including their effects onthe differences; $e _ { t }$ is the truncation error,and $v _ { r }$ , $v _ { t }$ are the variances of $e _ { r }$ and $e _ { t }$ .If all values of the interpolatingfactor $p$ are equally likely, $v _ { r }$ variesfromO.67for linear interpolation to O.81 forinterpolation with fifth differences.If $f ( A )$ isdetermined from a critical table,its error is that of asimple rounding-off errorunless the number of figures in the argument is small or unless the interval in the respondent is greater than unity.

# 14.6.2 The Method of Least-Squares

# 14.6.2.1 Introduction

When one is measuring the physical universe,certain constants must be determined from observation,such as theorbital elements ofa satelite about itsprimary or the rotational elementsabout its axis.Methods for ab initio determination of orbital elements from three or more observations are well-documented in the literature (Herget 1948).The more typical case assumes that approximate values of the constants are available on which a provisional theory can be based.This theory is then used to construct positions against which the observations can be compared.Thus,each observation minus the computed place forms a difference, referred to as an $O - C$ .The errors in these differences can arise from three sources:errors in the observations;errors in the constants on which the computed positionsare based;and errors in the theory itself.Only the first two error sourceswill be treated in the following discussion,which concerns the analysis of $O - C$ 's to improve the initial approximation to the constants.

# 14.6.2.2Errors of Observation:Frequency Distribution

Errorsof observation may arise from many sources.The size of these errors vary and,in general,follow the normal distribution curve or probability distribution curve wherein small errors occur more frequently than large errors,and positive errors occur with the same frequency as negative errors.In most problems,the frequency distribution of the errors is not known in advance.However,if each observation is assumed to be affected by the sum of several simultaneous,independent errors,we may assume the distribution of the errors to be accidental rather than systematic,the latter being the case where all the errors have a common origin.As there is no satisfactory mathematical theory of systematic errors,we must proceed initially on the assumption that the errors are accidental.In this case ifa set of random variables $x$ areindependent of each other,the theory of probability postulates that the frequency distribution of the sum of such variables,each with its own frequency distribution, will slowly approach the function

$$
Y = { \frac { h } { \sqrt { \pi } } } \exp ( - h ^ { 2 } x ^ { 2 } )
$$

where $h$ is defined as the index of precision.This is related to the standard deviation $\sigma$ ,or the root-mean-square error by $h ^ { 2 } = 1 / 2 \sigma ^ { 2 }$ .

The best fit to a series of $n$ observations,according to the principle of least-squares,is the one that reduces the sum of the squares of the errors to a minimum.Assuming that the index of precision is constant in this set of observations and letting the errors associated with each observation, $O _ { i }$ ,be $x _ { i }$ ,theprobability, $P _ { i }$ ,of occurrence of error $x _ { i }$ becomes

$$
P _ { i } = { \frac { h } { \sqrt { \pi } } } \exp ( - h ^ { 2 } x _ { i } ^ { 2 } ) d x _ { i } .
$$

Assuming that $P$ is independent,the probability that each error will occur in turn is

$$
P = \left( \frac { h } { \sqrt { \pi } } \right) ^ { n } \exp \left( - h ^ { 2 } \sum _ { i = 0 } ^ { n } x _ { i } ^ { 2 } \right) d x _ { 1 } d x _ { 2 } \cdot \cdot \cdot d x _ { n } .
$$

Thus,it can be stated that the set of errors that maximize $P$ in Eq.14.82 will produce the best fitotheseratiosecaeaatot $\scriptstyle \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 }$ is a minimum.

If the index of precision varies with each observation,the introduction of the factor $h _ { i }$ requires knowing the correspondence between the $h _ { i }$ and the arbitrary weight of an observation,based on unit weight. If the precision index corresponding to weight 1 is $h$ , and the precision index corresponding to weight $w _ { 1 }$ is $h _ { 1 }$ ,the probability that an error of size

$x$ will occur in an observation of weight 1 is

$$
P = { \frac { h } { \sqrt { \pi } } } \exp ( - h ^ { 2 } x ^ { 2 } ) d x .
$$

Also the probability of an error of size $x$ occurring in an observation of weight $w _ { 1 }$ is

$$
P = \frac { h _ { i } } { \sqrt { \pi } } \exp ( - h _ { i } ^ { 2 } x ^ { 2 } ) d x .
$$

Assuming that $P = P _ { 1 }$ ,that is that an error of size $x$ has an equal probability of occurring in bothEqs.14.83 and14.84,leads to

$$
\begin{array} { r } { w _ { 1 } = ( h _ { 1 } / h ) ^ { 2 } } \\ { w _ { i } = ( h _ { i } / h ) ^ { 2 } } \end{array}
$$

which shows that the weights are proportional to the precision indices.In terms of the precision index $h$ and the weights $w _ { i }$ ，

$$
P = \left( \frac { w _ { 1 } \cdot w _ { 2 } \cdot \cdot \cdot w _ { n } } { \pi } \right) ^ { n / 2 } h ^ { n } \exp \left[ - h \sum _ { i = 1 } ^ { n } w _ { i } x _ { i } ^ { 2 } \right] d x _ { 1 } d x _ { 2 } \dots d x _ { n } .
$$

showing that for $P$ to be a maximum, the $\scriptstyle \sum _ { i = 1 } ^ { n } w _ { i } x _ { i } ^ { 2 }$ must be a minimum.

Assume $o _ { i }$ (where $i = 1$ ,2,3,...,n)to be observations of aquantity for which $\tau$ is the true value. The error $x _ { i }$ of each observation is $x _ { i } = O _ { i } - \tau$ Using the standard deviation $o$ instead of the precision index $h$ ,the best estimate $\gamma$ of the true value $\tau$ is that which reduces

$$
1 / 2 \sigma ^ { 2 } \sum ( O _ { 1 } - \gamma ) ^ { 2 }
$$

to a minimum. To do this requires that ə $\sum / \partial \gamma = 0$ ；i.e., $: \sum ( O _ { i } - \gamma ) = 0$ ,from which $\gamma = 1 / n \sum O _ { i }$ ,or the best estimate is the arithmetic mean.

Given $n$ observations $O _ { i }$ ,having normally distributed errors $x _ { i }$ ,the error of the arithmetic meanis

$$
x = \frac { 1 } { n } \sum x _ { i }
$$

which isalinearcombination of $n$ randomvariables.If themean error of one observationis $\sigma$ ,thenit can be shown that the mean error of the arithmetic meanis the $\sigma$ of one observation divided by the $\sqrt { n }$

Once the estimate $\gamma$ of the true value $\tau$ of the measured quantity is obtained,a residual $r$ can be formed by $O _ { i } - \gamma = r _ { i }$ .Also $O _ { i } - \tau = x _ { i }$ ,where the $x _ { i }$ are the true errors of the observations.Then

$$
\begin{array} { r } { \sum x _ { i } = \displaystyle \sum O _ { i } - n \tau = n \gamma - n \tau } \\ { \gamma = \tau + \displaystyle \sum x _ { i } / n } \\ { r _ { i } = x _ { i } - \displaystyle \sum x _ { i } / n . } \end{array}
$$

Let $\sigma _ { r }$ be the mean error of the residuals and $\sigma _ { x }$ be the mean error of the errors $x _ { i }$ ,then

$$
\sigma _ { r } ^ { 2 } = ( ( n - 1 ) / n ) ^ { 2 } \sigma _ { x } ^ { 2 } + ( n - 1 / n ^ { 2 } ) \sigma _ { x } ^ { 2 } = ( n - 1 / n ) \sigma _ { x } ^ { 2 } .
$$

Since $\sigma _ { r } ^ { 2 } = \sum r ^ { 2 } / n$ , then $\scriptstyle \sigma _ { x } ^ { 2 } = \sum r ^ { 2 } / n - 1$ andthe mean-square errorof the arithmetic mean in terms of the residuals is

$$
\Gamma = \sqrt { \sum r ^ { 2 } / n ( n - 1 ) } .
$$

# 14.6.2.3 The Method of Least-Squares

In many problems the quantity measured is not the one that we wish to correct.A simple case involves one unknown, $\eta$ ,to be determined from measurements $\zeta _ { i }$ ,where $i = 1$ ,2，3，...,n. Thus $\zeta = f ( \eta )$ .Let $\eta _ { c }$ be the provisionally known value of $\eta$ ,and $\eta _ { 0 }$ be the value to be determined from the measurements,then the difference $\eta _ { 0 } - \eta _ { c } = \Delta \eta$ .Calculating from $\eta _ { c }$ for each measurement $i$ ,gives $\Delta _ { i } \zeta = \zeta _ { i } - \zeta _ { c }$ Usinga Taylor’s series expansion, $\Delta \zeta$ maybe written asa function of $\Delta \eta$ ,

$$
\Delta \zeta = \frac { \partial f } { \partial \eta } \Delta \eta + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f } { \partial \eta ^ { 2 } } ( \Delta \eta ) ^ { 2 } + \frac { 1 } { 6 } \frac { \partial ^ { 3 } f } { \partial \eta ^ { 3 } } ( \Delta \eta ) ^ { 3 } + \cdot \cdot \cdot .
$$

Assuming $\Delta \eta$ is small enough that its square and higher powers canbe ignored,then

$$
\left( \frac { \partial f } { \partial \eta } \right) _ { i } \Delta \eta = \Delta \zeta _ { i }
$$

and we have $n$ equations where in each case the $( \partial f / \partial \eta )$ is a known numerical coefficient. Denoting the coefficients by $A$ ,the equations of condition can be written $A \Delta \eta = \Delta \zeta .$ The preferred value of theunknown is that forwhich

$$
\frac { \partial } { \partial \Delta \eta } = \sum ( A _ { i } \Delta \eta - \Delta _ { i } \zeta ) ^ { 2 } = 0 .
$$

Diferentiating gives $\begin{array} { r } { \sum A ^ { 2 } \Delta \eta = \sum A \Delta \zeta } \end{array}$ , thus $\textstyle \Delta \eta = \sum A \Delta \zeta { \big / } \sum A ^ { 2 }$ and $\Delta \eta + \eta _ { c } = \eta _ { 0 }$

In a more general problemit may be necessary to determine more unknowns than one from a series of measurements.The constants of a planetary orbit $C _ { i }$ (where $i = 1$ ,2,3,...， $n$ ） may already be approximately known and can be used to compute the $\eta _ { c }$ corresponding to each observation $\eta _ { 0 }$ ,then $\eta _ { 0 } - \eta _ { c } = \Delta \eta$ .Let the corrections to the approximate values of the orbital constants be $E _ { i }$ ,so that the corrected constants are $C _ { i } + E _ { i }$ .The equations of condition can then be written

$$
{ \frac { \partial \eta } { \partial C _ { 1 } } } E _ { i } + { \frac { \partial \eta } { \partial C _ { 2 } } } E _ { 2 } + \cdot \cdot \cdot + { \frac { \partial \eta } { \partial C _ { n } } } E _ { n } = \Delta \eta .
$$

Setting $\partial \eta / \partial C _ { 1 } = A , \partial \eta / \partial C _ { 2 } = B , \partial \eta / \partial C _ { 3 } = C$ ,and so on,the conditional equation can be written

$$
A E _ { 1 } + B E _ { 2 } + C E _ { 3 } + \cdot \cdot \cdot + N E _ { n } = \Delta \eta .
$$

Supposing there are no errors in the $\Delta \eta$ ,i.e.,that the theoryused isadequate,and that the observations contain no errors,then the only source of error in the solution comes from the approximate values of the constants.The theory of linear equations states that $n$ independent equations of condition are necessary and sufficient to determine the $E _ { i }$ .With the above restrictions as to the source of errors,the solution will yield values of $E$ thatwill exactly satisfy the $n$ equations.Normally,however,accidental errors in the values of $\Delta \eta$ prevent the derivation of theexactvaluesof $E _ { i }$ .Increasing thenumber $m$ of observations and thus the number of conditional equationswill decrease the effect of the accidental errors.In some problems in dynamical astronomy it is not unusual to have $m$ exceed $n$ by a factor of10oo.Since values of $E _ { i }$ are derived that do not exactly satisfy the conditional equations,the procedureis to evaluate the left-hand side of the equations and subtract from the corresponding $\Delta \eta$ to produce residuals $r$ .The best values of the $E _ { i }$ are those that reduce the sum of the squares of the residuals $( r )$ to a minimum as discussed earlier.

In the instance where there are $m$ equations of condition,with $m > n$ ,the procedure is to form $n$ normal equations for solution.The normals are formed as follows.Given the conditional equations,

$$
\begin{array} { r l } & { A _ { 1 } E _ { 1 } + B _ { 1 } E _ { 2 } + C _ { 1 } E _ { 3 } + \cdot \cdot \cdot + N _ { 1 } E _ { n } = \Delta \eta _ { 1 } } \\ & { A _ { 2 } E _ { 1 } + B _ { 2 } E _ { 2 } + C _ { 2 } E _ { 3 } + \cdot \cdot \cdot + N _ { 2 } E _ { n } = \Delta \eta _ { 2 } } \\ & { A _ { 3 } E _ { 1 } + B _ { 3 } E _ { 2 } + C _ { 3 } E _ { 3 } + \cdot \cdot \cdot + N _ { 3 } E _ { n } = \Delta \eta _ { 3 } \mathrm { e t c . , } } \end{array}
$$

multiply through each conditional equation by the coefficient $A _ { i }$ and sum to form the first normal equation in the arrayinEq.14.97,where the bracketsrepresent summation.Then multiply through each conditional equation by $B _ { i }$ and sum to form the second line of the array. Repeat with $C _ { i }$ to form the third line of the array.The procedure isrepeated through the coefficient of $E _ { n }$ and the symmetry of the resulting array of $n$ equations in $n$ unknowns reduces the complexity of the solution.

$$
\begin{array} { r l } & { [ A _ { i } ^ { 2 } ] E _ { 1 } + [ A _ { i } B _ { i } ] E _ { 2 } + [ A _ { i } C _ { i } ] E _ { 3 } + \cdot \cdot \cdot + [ A _ { i } N _ { i } ] E _ { n } = [ A _ { i } \Delta \eta _ { i } ] } \\ & { [ B _ { i } A _ { i } ] E _ { 1 } + [ B _ { i } ^ { 2 } ] E _ { 2 } + [ B _ { i } C _ { i } ] E _ { 3 } + \cdot \cdot \cdot + [ B _ { i } N _ { i } ] E _ { n } = [ B _ { i } \Delta \eta _ { i } ] } \\ & { [ C _ { i } A _ { i } ] E _ { 1 } + [ C _ { i } B _ { i } ] E _ { 2 } + [ C _ { i } ^ { 2 } ] E _ { 3 } + \cdot \cdot \cdot + [ C _ { i } N _ { i } ] E _ { n } = [ C _ { i } \Delta \eta _ { i } ] . } \end{array}
$$

When the $m$ equations of condition are not all of equal weight,each equation may be multiplied through by the square root of its weight before forming the normals.

Methods of solution of the normal equations are numerous and are detailed in the references given at the end of this chapter.

# REFERENCES

1.TheAstronomical Almanac Online: http://asa.usno.navy.mil or http://sa.hmnao.com.   
Abramowitz,M.andI. Stegun (1973).Handbook of Mathematical Functions (9th ed.).New York: Dover Press.   
Brouwer,D.and G.Clemence (1961).MethodsofCelestial Mechanics.New York and London: Academic Press.   
Carpenter,L.(196,June).Solutions to planetary perturbation motion equations by Chebyshev series. TechinicalNoteD-3168,NASA.   
Danby,J.(1988).FundamentalsofelestialMechanics(2nded.).ichmond,VA:Willmann-Bell,Inc.   
Fox,L.andI.Parker(1972).ChebyshevPolynomials inNumerical Analysis.Oxford,England:Oxford University Press.   
Herget,P. (1948).ComputationofOrbits.Willmann-Bell,Inc.,Richmond,VA:Published privatelyby the author.   
Hildebrand,F.(1987).Introductionto Numerical Analysis.New York:DoverPress.   
H.M.Nautical Almanac Office (1956). Interpolation and Allied Tables.London: H.M.Stationery Office.   
H.M.Nautical Almanac Offce (1958).Subtabulation:A Companion Bookletto Interpolation and AlliedTables.London:H.M.StationeryOffice.   
Lanczos,C.(1956).Applied Analysis.Englewood Cliff,NJ:Prentice-Hall.   
Pres,W.,B.Flannery,S.Teukolsky,andW.Veterling(1986).NumericalRecipes,TheArtofScientific Computing.Cambridge,England:CambridgeUniversity Press.

# Calendars

E.G.RICHARDS

# 15.1 Introduction

# 15.1.1 Overview

A calendar is a system for assigning aunique name,itsdate,to every day so that the order of the dates isapparent and the interval in days between two datescanbe readily calculated.A dateisgenerally specifiedby three numbers:adayof the month,D,amonth,Mandayear, Y;inmost calendars,the monthsalso have names.

Most calendars are based on astronomical cycles so that the days of the month cycle in approximate synchrony with the lunations (the cycle of the phases of the Moon) and the months cycle in approximate synchronywith the seasons of the year.

Since the number of lunations ina year and the numberof days inalunation are not integral (and also slowly change with time),extra intercalary days or months may be inserted into occasional years to maintain a long-term average synchrony with the astronomical cycles. Years in which aday or month isintercalated are sometime called leapyears.The Romans called yearswith an extra day bissextile years.

Solarcalendars,such as the current Gregorian calendar,maintain accurate synchrony with the astronomical year while abandoning any attempt to keep the months in synchrony withthe lunations of theMoon.Lunar calendars,such as the Islamic calendar,maintain synchrony of the monthsand abandon synchrony with the Sun.Luni-solar calendars,such as the Jewish, Chinese and Christian Ecclesiastic calendars,attempt to maintain synchrony with both.

According to a recent estimate (Fraser1987),there are about forty calendars in use in the world today and more that have beenabandoned.This chapter isconcerned with onlyafew of these.Wediscuss here nine.The first of these is the Gregorian calendar,which isnow used throughout the world for secular purposes.It is the official calendarof the United Kingdom (since1752),but not of the United States(which has no official calendar).We discussa furthersix(theJulian,Jewish,Islamic,Indian,ChineseandBaha’icalendars),whicharein current use to determine the proper dates of religious or cultural activities.We discuss two more(The Ancient Egyptianand the French Republican calendars),which areof historical interest.Brief historical summariesand the details of the operation are given for each of these nine calendars,but we do not discuss their usage.Algorithms are given for arithmetic calendars(s $\mathrm { \ ; e e } \ \ S \ 1 5 . 1 . 4 )$ forconvertingdatesin one to those in others.

Despite a vast literature on calendars,truly authoritative references,particularly in English,are diffcultto find.One suchis ReingoldandDershowitz(1997,20o1).Richards (1998)

surveysabroad varietyofcalendarsand Aveni (199O) stresses theircultural contextsrather than their operational details.Fotheringham(1935),Doggett(1992) and the Encyclopaedia ofReligionand Ethics(Hastings191O),in itssectionon“Calendars,offer basic information on historical calendars.Blackburn and Holford-Stevens (1999) give detailed information about customs appertaining toeach day ofthe year and onavariety of calendars.The sections on“Calendars”and“Chronology”inall editions of the Encyclopaedia Britannicaprovide useful historical surveys.Ginzel (19o6,1911) remainsanauthoritative,if dated,standard of calendrical scholarship.References on individual calendars are given in the relevant sections. See also URL[1],URL[2],URL[3],URL[4],andURL[5].

# 15.1.2 Uses of Calendars

Calendars have been used from the earliest times to regulate hunting,agricultural practices and other economic activities.Later they were important in regulating religious rituals,fasts and feasts.Most major religions use a special calendar and most calendars are associated with a religion.From the beginnings of civilization calendars have been used to date receipts, contracts and other documents and to order social life and to define holidays.

Details of their uses in religious practices are discussed in the Encyclopaedia of Religion and Ethics (Hastings 191o)and in Blackburn and Holford-Stevens (1999).

# 15.1.3Astronomical Bases of Calendars

The principal astronomical cycles are the year (based on the revolution of the Earth around the Sun),the month (based on the revolution of the Moon around the Earth) and the day (based on the rotation of the Earth on its axis).The complexity of calendars arises because the month and the year do not comprise an integral number of days,and because they are neither constant nor perfectly commensurable with each other (see Dogget1992).

The tropical year is today defined as the time needed for the Sun's mean longitude to increase by $3 6 0 ^ { \circ }$ (Danjon 1959;Meeus and Savoie 1992).This varies from year to year by several minutes,but it may be averaged over several years to give the mean tropical year.It maybenoted that this definition differs from the traditional definition,which isthe mean period between two vernal equinoxes.

The intervals between any particular pair of equinoxes or solstices are not equal to one another or to the tropical year;theyare also subject to variations from yearto year but may be averaged over anumber of years.Thearithmetic meanof the four average intervals based on the two equinoxes and the two solstices is equivalent to the value of the mean tropical year. These matters are discussed by Steel (2000).

It is sometimes assumed that the tropical year represents the period of the cycle of the seasons.It may be noted,however,that the Gregoriancalendar is tied to the vernal equinox year and the Chinese calendar to the winter solstice.

The following approximate expression,based on the orbital elements ofLaskar(1986), maybe used to calculate the length of the mean tropical yearin the distant past.Note,however, that The Astronomical Almanac has not used these equations,nor does it use the orbital elements fromLaskar,but starting from the 2OO4 edition,it uses the orbital elementsof Simon et al. (1994):

$$
3 6 5 ^ { \mathrm { d } } 2 4 2 \ 1 8 9 \ 6 6 9 8 - 0 . 0 0 0 \ 0 0 6 \ 1 5 3 \ 5 9 \ T - 7 . 2 9 \times 1 0 ^ { - 1 0 } \ T ^ { 2 } + 2 . 6 4 \times 1 0 ^ { - 1 0 } \ T ^ { 3 } .
$$

Table 15.1 Approximate lengths of the astronomical cycles   

<table><tr><td>Yeara</td><td>Days in Yearb 1 day= 86400 seconds (SI)</td><td>Days in lunationc</td><td>Length of day</td><td>Daysd/year</td><td>Dayse/lunation</td></tr><tr><td>2000</td><td>365.24219</td><td>29.53059</td><td>86400.003</td><td>365.24217</td><td>29.53059</td></tr><tr><td>1500</td><td>365.24222</td><td>29.53059</td><td>86399.995</td><td>365.24224</td><td>29.53059</td></tr><tr><td>1000</td><td>365.24225</td><td>29.53059</td><td>86399.886</td><td>365.24231</td><td>29.53059</td></tr><tr><td>500</td><td>365.24228</td><td>29.53059</td><td>86399.878</td><td>365.24237</td><td>29.53059</td></tr><tr><td>0</td><td>365.24231</td><td>29.53058</td><td>86399.969</td><td>365.24244</td><td>29.53059</td></tr><tr><td>-500</td><td>365.24234</td><td>29.53058</td><td>86399.961</td><td>365.24250</td><td>29.53060</td></tr><tr><td colspan="6">rate of change f</td></tr><tr><td>(ppb)</td><td>-17</td><td>73</td><td>20</td><td>-37</td><td>53</td></tr></table>

Astronomical year;i.e.,theyearYB.C.isdesignated astronomical year1-Y. b The mean tropical year as given by Eq.15.1. cMean Synodic period as given by Eq.15.2 dDays of alength in seconds (SI) as given in column 4 eDays of alength in seconds(SI) as given in column 4 $f$ Theratesof change of these periods themselves changeoverthecenturies,butthe proportionalrates of increase,expressed as parts per billion $( 1 0 ^ { 9 } )$ per century,are given for the year 2000

The synodic month,or lunation,the mean interval between conjunctions of the Moon andSun,corresponds to the cycle of lunar phases.The following expression for the synodic month is based on the lunar theory of Chapront-Touzé and Chapront (1988):

$$
2 9 . 5 3 0 5 8 8 8 5 3 1 + 0 . 0 0 0 0 0 2 1 6 2 1 T - 3 . 6 4 \times 1 0 ^ { - 1 0 } T ^ { 2 }
$$

butany particular cycle may vary from the mean by up to seven hours.

In these expressions, $T$ is the number of Julian centuries (of 36525 days) measured from 2000January1in Terrestrial Time(TT).Itisgivenby $T = ( J - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5$ where $J$ is theJulian date (see $\ S \ 1 5 . 1 . 1 0 $ .

Thelengths of the tropical yearand synodic monthare given bythese formulae in days of 86400 seconds(SI) of International Atomic Time(TAI).See Chapter 3 for furtherinformation on timescales.

Historians (Stephenson 1997) have also found that the length of the mean solar day expressed in TAI isnot constant.It appears to be increasingby about O.Oo17 seconds per century because of tidal and other effects.It also suffers from both periodicand small random changes.

The lengths of the cycles change slowly with time and expressons 15.1 and 15.2 only represent approximations and are included in this chapter only for illustrative reasons.The lengths of these cycles calculated from them forrepresentative yearsare shown in.Table 15.1.

# 15.1.4Astronomical, Observational and Arithmetic Calendars

Some calendars,termed observational calendars,rely on actual sightings of a new moon, solstice,equinox;or some other natural phenomenon to determine the start of the months and the years or when to intercalate a day or a month.The times of the sightings are subject to error on account of the weather and such calendars cannot be constructed in advance. Examplesare the ancient Jewish calendar and the Islamic calendar as it is generally used to determine important religious dates (such as the start of Ramadan);both of these depend on sightings of the crescent of the new moon.The heliacal rising of Sopdet (Sirius) may,at one time,have signalled thestartof theancientEgyptianyear.Itis likelythatmanycalendars now lost were observational.Note that the local time at which an observation is made may fall in different days according to the locality of the observer.

Astronomical calendars depend onamodel to predict the times of such events.These models have changed over the centuries as astronomical knowledge improved.Examples ofastronomical calendars include the Chinese and Indian luni-solar calendars,the original form of the French Republican calendarand one form of the Baha'i calendar.Astronomical calendarsusually specify that the events be observed or calculated fora particular meridian. ThuseventsusedintheChinesecalendarareobservedatameridianat $1 2 0 ^ { \circ }$ East (but before 1929 at the meridian of Beijing).The French Republican calendar specified the meridian of Paris.

Arithmetic calendars abandon any explicit references to astronomical events and are regulated by fixedrules,though theymay have been designed inanattempt to keep their years ormonths instep with the astronomical periods.Examples include the current Gregorian calendar and its predecessor,the Julian calendar,as wellas the ancient Egyptian calendar, the modern Jewish calendarand the civilIslamic calendar(used by historians of Islamic culture).

# 15.1.5Visibility of the Crescent Moon

Several observational calendars rely on the first sighting of new moons.Under optimal conditions,the crescent Moon has been sighted about 15.4 hoursafter the astronomical new moon (i.e.,the conjunction) (Schaefer1988).Usually,however,it is not seen until it is more than twenty-four hours old.Babylonian astronomers were the first to develop methods forcalculating first visibility,though no surviving tables are explicitly concerned with this (Neugebauer1975,pp.533-540).The earliest knownvisibility tablesarebyal-Khwarizmi, aninth-century astronomer of Baghdad (King1987).These tables,and many subsequent tables,were based on the Indian criterion that the Moon will be visible if the local hour angle of the Moon at sunset is equal to orless than $7 8 ^ { \circ }$ .With the development of Islamic astronomy more complexcriteria were developed.

Modern models for predicting first visibility incorporate celestial mechanics,spherical astronomy,selenology,atmospheric physics,and ophthalmology.Bruin (1977) was the first to prepare such a model.Ilyas (1984),recognising that the Islamic calendar is used around theworld,introduced theconceptofanInternational LunarDateline,west ofwhich the Moon should be visible under good observing conditions.Schaefer(1988) has further investigated the theory of this.Extensive observing programswere once organised by Doggett, Seidelmann,and Schaefer(1988) and Doggett and Schaefer (1989); see also URL[7].

# 15.1.6Non-astronomical Cycles and theWeek

The calendars of many societies have incorporated cycles with no astronomical basis.Cycles of days include the eight-daycycle (Nundinae)oftheRomans,the13and 20day cycles of Central America and the market weeks,of various lengths,of Africa.The Ancient Egyptian calendar and theFrench Republicancalendaruseda1O-daycycle,and the Bolsheviks in Russia experimented with afour-day“week."Most of the world today recognises the sevenday week which has religious significance for Christians,Jews and Muslims.

The seven-day week probablyoriginated in Babylonas auseful,if inexact,divisionof the lunar month and was probablyadopted by the Jewish peopleat the time of the Babylonian exileinthe sixth century B.c.. Itis likely thatit has run continuously and without interruption since these times to the present day (but see Zerubavel E.(1989).The seven-day cycle was widely used in the Roman Empire from the first century B.C..According to Cassius Deo each ofthe seven“wandering stars,”the Sun,the Moon and the five naked-eye planets known to the ancients,was assigned cyclically to each of the 24 hours of each day in the order of their apparent speed in the heavens.The star assigned to the first hour was the regent of the day.The names of the regents gave each day its name and the order of the days in this astrological week.These names,or their equivalents inother languagesand pantheons,are still used today.Saturn'sdaycoincided with theJewish Sabbath,though the Jews neverused the Roman names.

Colson (1926)and Zerubavel(1989)are standard references on the week.Richards(1998) gives a comprehensive list of the names of the days of the week. Zerubavel (1989) also considers other week-like numerical cyclesused bypast and present cultures.

Cycles of years have also had significance for various cultures.The Romans used a15- year cycle of indiction for taxation purposes.The Chinese have acycle of 6O years comprised of two simultaneous cycles of 10 and12 years (60 is the lowest common multiple of10and 12).The years in both of these Chinese cycles carried names.Thecultures ofCentral America and of India used several cycles of years; some are exceedingly long.

# 15.1.7 Historical Eras and Chronology

Astronomical cycleswith aperiod greater thana year have rarely been used incalendars. Instead,years have generallybeennumberedfrom someimportant event,secularorreligious. Thus,regnal dates count the years from the accession of a ruler and the numbering starts afresh with each new ruler. Other calendars count years from an important event,maybe in theremote past,which initiates anera.Thus,the Islamic calendar counts the years from the dateof the flight of theProphet fromMecca toMedinaand the Christianscount from the presumed birth ofChrist.Inother calendars,Chinese,Indian,Mayan,yearswere sometimes counted in cycles of various lengths;the cycles themselves may also be counted.

The first day of the first month of the year numbered 1 is sometimes called the epoch of the calendar.Table 15.2 shows the starting yearof a few of the eras of historical importance.

# 15.1.8 The Christian Era

The epoch of the Christiancalendarisusually,but wrongly,taken to be the birthofChrist.This epoch was established by the sixth-century scholar Dionysius Exiguus who was compiling a table of dates of Easter.An existing table covered the nineteen-year period denoted 228-247, where years were counted from the beginning of the reign of the Roman emperor Diocletian. Dionysius continued the table for a nineteen-year period,which he designated Anno Domini Nostri Jesu Christi 532-550.Thus,Dionysius’Anno Domini 532 is equivalent to Anno Diocletiani 248.In this way a correspondence was established between the new Christian eraand an existing system associated with historical records.However,Dionysius did not useanaccurate date for the birth of Christ and scholars generally believe that Christ was born some years before A.D.1,but the historical evidence is not adequate toallow a definitive dating.

Table 15.2 Some eras   

<table><tr><td>Name of era</td><td>Year of epoch</td><td>Used by</td><td>Eventcommemorated</td></tr><tr><td>Byzantine Eraa</td><td>-5508</td><td>Byzantium</td><td>Creation of theworld</td></tr><tr><td>Anno Mundi (A.M.) a</td><td>-3760</td><td>Judaism</td><td>Creation of theworld</td></tr><tr><td>Kali-yuga b</td><td>-3101</td><td>India</td><td>Mean conjunction of planets</td></tr><tr><td></td><td>-2636</td><td>Chinese</td><td>Traditional start of 60 year cycles</td></tr><tr><td>Ab Urbe Condita (A.U.C.)ä</td><td>-752</td><td>Roman Empire</td><td>Legendary foundation ofRome</td></tr><tr><td>The Era of Nabonassara</td><td>-746</td><td>Alexandria, Early astronomers</td><td>Accession of Babylonian KingNabonassar</td></tr><tr><td>Jimmu Tennoa</td><td>-659</td><td>Japan</td><td>Accessionof Emperor Jimmu Tenno;adoption of Chinese</td></tr><tr><td>Seleucid Eraa</td><td>-312</td><td>Selucid Empire</td><td>calendar Foundation of Empireby Seleucis</td></tr><tr><td>Anno Domini(A.D.or C.E)</td><td>1</td><td>Christianity</td><td>Approximatedateof Birth of Christ</td></tr><tr><td>SakaEra“</td><td>78</td><td>India</td><td>Uncertain;possibleaccession ofKing Salivahana</td></tr><tr><td>Era ofDiocletian“</td><td>283</td><td>Coptic&amp;Ethiopian churches; Roman Empire</td><td>Accession of Roman EmperorDiocletian</td></tr><tr><td>Era of the Hegira (A.H.)a</td><td>622</td><td>Islam</td><td>Prophet&#x27;sflightfromMecca</td></tr><tr><td>Republican Era(E.R.)</td><td>1792</td><td>France</td><td>Foundation of theRepublic</td></tr><tr><td>Badi Era (B.E.)</td><td>1844</td><td>Baha&#x27;i</td><td>Declarationof theBab</td></tr></table>

“Thedates of the startof the year in these eras arecurrently given inThe Astronomical Almanac. bTheChinese used noeraassuch butcounted years incyclesof 60.Thecycles weresometimes counted with the first starting in $- 2 6 3 6$

Yearsafter the epoch of the Christian calendar are traditionally labeled:A.D.(Anno Domini） but the label c.E.(Common Era) ispreferredbysome.Likewise the traditional label of years before A.D.1 has been B.C.(Before Christ) but some prefer B.C.E.(Before Common Era).

Itis often possible to assign a date in a calendar to days preceding the epoch or the date on which it was firstused.Such datesare termed prolepticdates.Bede,theeighthcentury English historian,began the practice of counting years backward from A.D.1 (see

Colgrave andMynors1969).Inthis system,theyear A.D.1isprecededby the year1 B.c., with nointervening yearO.Becauseof this numerical discontinuity,this“historical”systemis cumbersome forcomparing ancient and modern dates.Ihave used $+ 1$ (etc.) to designate A.D.1 (etc.).The year $+ 1$ isnaturallyprecededbyyearO,whichisprecededbyyear $^ { - 1 }$ Since the use of negative numbers developed slowly in Europe,this system of dating was delayed until the eighteenth century,when it was introducedby the astronomer Jacques Cassni(Cassni 1740).

# 15.1.9 Dates

The date ofany day is specifiedby giving the year and the month inwhich it falls and its day of the month and maybe the day of the week.There are many conventions concerning the order in which these are presented.We shall specify here dates by giving the day of the week,the year number,the name of the month and the day of the month in that order.

Note that in nearly all calendars,the first day ofa month is day1—rather than day O; likewise,the first month of ayear is month1—ratherthan month O.This is incontradistinction to other systems for specifying time;thus the first hour ofaday is hourO—rather than hour1.

We shall use,following the practice of historians,the Julian calendar(see $\ S \ 1 5 . 3 . 4 $ for dates before 1582and the Gregorian for dates after,but it is usualto specify the calendar used for dates between 1582 and 18oo.We shall not always label the years with either A.D./B.C. or C.E./B.C.E.Instead a positive year number should be read to imply a year in the Common Era(A.D.),whilstanegative year impliesayear before that (B.c.).Thus,ayear2OOO means A.D.2000 whilst $- 1 0 0 0$ implies1Oo1 B.c.. In general negativeyear, $- \mathrm { Y }$ isequivalent to $1 - \mathrm { Y }$ B.C..We will,however, use the terms A.D.orB.C.when referring to centuries.

The time of dayof the start of aday varies in different Calendars.Thus,the Gregorian day runs from midnight to midnight,but the Islamic and Jewish days start some six hours earlierand run fromdusk (ata nominal $6 \ \mathrm { p . m } ,$ ）to dusk.This raises the point as to which, for example,Gregorian day or date corresponds to a given Islamic or Jewish date.The usual convention,which wefollowhereandinTheAstronomicalAlmanac,isthatdatesindifferent calendars correspond when they contain the same noon.Thus the Islamic and Jewish days start some six hours before the correspondingGregorian day.In some Indian calendars the daystartsat dawn,some six hourslater.

# 15.1.10 Julian Day Numbers and Julian Dates

Dating systems in medieval Europe caused considerable confusion.Some states used regnal dating(with a plethora of local rulers)；others used the Anno Domini system.Moreover different states used different days to starttheir years.Although the Romans had used January 1to start their years,Christendom often used March 25th,though other days were sometimes used.

Inthe sixteenth century,Joseph Justus Scaliger(1540O-16O9) tried to resolve the patchwork of historical erasby dating every event according to a single system (Scaliger 1583). Instead of introducing negative year counts,he sought an initial epoch before any historical record. Hisapproach utilised three calendrical cycles:the 28-year solar cycle (the period after which weekdays and calendar dates repeat in the Julian calendar),the nineteen-year cycle of golden numbers (the period after which the Moon’s phases approximately repeat on the same calendar dates),and the fifteen-year indictioncycle (the Roman tax cycle).

Scaliger could,therefore,characterise ayearbya triplet of numbers(S,G,I);S,the numberof the year in the solar cycle,runs from1to 28;G,the golden number of the year, runs from1to19;I,the numberof the year in the Indiction cycle runs from1 to15.He noted that a given combination would recur after 7980 $( = 2 8 \times 1 9 \times 1 5$ years.Thishecalleda JulianPeriod,because itwas basedontheJulian calendaryear.Forhis initial epoch,Scaliger chose the year in which S, $\mathbf { G }$ andI were all equal to1.He knew that the year1(A.D.1) had ${ \bf S } = 1 0$ , $\mathbf { G } = 2$ and $\mathbf { I } = 4$ and worked out that the combination(1,1,1) occurred in the year -4712(4713 B.c.)whichwasyear1of Scaliger'sJulian period.

Although Scaliger's original idea was to introduce a count of years,nineteenth-century astronomers adapted this system to create a count of days elapsed since the beginning of the Julian period.John Herschel(1849) gave a thorough explanation of the system and provided atableof‘Intervals inDays betweenthe Commencement of the Julian Period,and that of some other remarkable chronological and astronomical Eras.”

Astronomers have extended this idea by appending to the day number,the time of day expressed asadecimal fractionofaday.The resulting numbers called Julian dates define any instant of time.Thus 2451545.0 corresponds to noon on 20o0 January1as observed at a meridian of $0 ^ { \circ }$ (Greenwich) in the Gregorian calendar.At a meridian of $0 ^ { \circ }$ ,theday 2000 January1began12hoursearlierat2451544.5.Further east,theday begins earlierand further west,later.

Itisimportant to note theseJulian datesspecifyan instant in Universal Time(UT),not local time.Adayin the Gregorian calendar beginsat midnight,the world over,atan instant that varies with longitude,and henceis specifiedbydifferent Julian dates.This isinconvenient when considering calendars.It is,therefore,useful to define a Julian Day Number,J,(to be distinguished froma Juliandate)which isa whole number,and which may beused to label each of the days.The JulianDayNumberof Saturday 2Ooo January1is then2451545 and of Tuesday $- 4 7 1 2$ January1it is1.URL[7] provides a useful program for interconverting dates and Julian dates.

# 15.1.11 Luni-solar Calendars

It may be noted that 19 astronomical years and 235 lunations both contain about 6939 days. This was realised in Babylon in about the 5th century B.C.,and gave rise toa calendarusually ascribedtoMetonofAthens (5th centuryB.C.).In this,each yearofa19-year cyclecontains 12monthsof alternately 29and3O days,but7of the19 yearscontaina13th intercalated month of 30 days.Thus the19 years contain 235 months or 6936 days.The average number of daysperyear isabout 365.05 $( = 6 9 3 6 / 1 9$ ）and theaveragenumberof dayspermonth isabout 29.51.In the short term,such a calendar keeps,onaverage,in rough synchrony with both the Sun and the Moon.The accuracy of this Metonic calendar can be improved by judicious intercalations of extra days,anda variant of it isused in both the Jewish and the Christian Ecclesiastical calendars.

The luni-solar calendars of China and India similarly interpolate leap months,but use astronomical considerations to decide when to intercalate and when to begin a year or a month.The months themselves may begin on the day of a conjunction of the Moon (new moon)and are thus synchronised with thelunations,but these calendars also make use of solar months.These are defined by dividing the ecliptic into twelve sections,analogous to the sign of the Zodiac,and separated by $3 0 ^ { \circ }$ of solarlongitude.The temporal lengths of both thelunar months andofthe solar months vary throughoutthe year.Thus,although the starting dates of the solar and lunar months generally alternate,so that each lunar month contains the start of just one solar month,there are years in which a lunar month contains the start of two solar months (i.e.,the solar month is entirely contained in a lunar month) or of no solar month (i.e.,the lunar month is entirely contained in a solar month).The points at which extra monthsareintercalatedare determinedby such months.Thisresultsintheintercalationof about7extra monthsin19 yearsand achieves aresult similarto thatof the Metoniccalendar.

# 15.1.12 Accuracy of Calendars

The question of accuracy for observational calendars does not arise.The accuracy of an astronomical calendar depends on the adequacy of the underlying astronomical theory and the precision of the celestial observations on which itis based.Although arithmeticcalendars do not explicitly refer to astronomical cycles,they are usually founded on an attempt to maintain their years in synchrony with the tropical year or their months in synchrony with thelunar cycle.These attempts can never be wholly accurate if only because the astronomical periodschange with time,albeit slowly.To assess their accuracy,thesynodic period may be compared to the average length of the calendar month and the mean tropical year(or the vernal equinox or winter solstices year) may be compared to the average length of the calendar year. Auseful parameter is the number of years required for a calendar cycle to become one day out of phase with the corresponding astronomical cycle in some particular year.Bear in mind that the lengths of these astronomical cycles are themselves slowly changing (see Table 15.1).

High precision in the average lengths of the months was achieved quite early on account of the ease with which the mean synodic period can be measured.The precise measurement ofthe length of the year(solstice to solstice orequinox to equinox) seems to have presented a greater challenge.The most accurate solar calendar in general use is the Gregorian calendar inwhich there are146 O97daysin400 yearsor365.2425days/year.Today,inA.D.2000, the Gregorian calendar yearis slightlylonger than the mean vernal equinox year(365.24237 days)and,neglecting its change with time,would be oneday out relative to the vernal equinox yearafter about another 8ooo years.Variousproposals have been made (Delambre1821; Herschel 1849) to improve this accuracy but none take count of the slowly changing length of the year and day.

At the other extreme,theancient Egyptian civil calendar contained 365 days.This lagged afurtherday behind the tropical yearevery four years orby 365 days inabout15OO years.

# 15.2The Ancient Egyptian Calendar

# 15.2.1Historyof the Egyptian Calendars

Ancient Egyptian civilisation,from the start of the Old Kingdom to the annexation of Egypt byAugustus,lasted some 25oo years.It employed several calendars for religiousand for civil purposes,but it is not known when these were first instituted.The year of the civil calendarcontaineda constant 365 days divided into 12 months of30 days each,followed by

Table15.3 Months in the ancient Egyptian calendar   

<table><tr><td>Month</td><td>Month</td></tr><tr><td>1. Thoth</td><td>7.Phanemoth</td></tr><tr><td>2. Paophi</td><td>8.Pharmouti</td></tr><tr><td>3. Athyr</td><td>9.Pachons</td></tr><tr><td>4. Cohiac</td><td>10.Payni</td></tr><tr><td>5. Tybi</td><td>11. Epiphi</td></tr><tr><td>6.Mesir</td><td>12.Mesori</td></tr><tr><td colspan="2">The five epagomenal days followed Mesori.</td></tr></table>

5epagomenal days belonging tono month.The names of the months are shown in Table 15.3. The year began on Thoth 1.Since 365 is a poor approximation to the number of days in the year,the start of the yearcycled slowly through the seasonswith a period of about 1500 years.There was no Egyptian Era,instead the years were counted from theaccesson of each Pharaoh in regnal fashion,but Ptolemyused the era of Nabonassar (E.N.) (see $\ S \ 1 5 . 1 . 7$ ).

The Roman writer Censorinus noted that the Julian calendar date 139 July 2O(Julian Day Number1772 028)) was Thoth1in the Egyptian calendar. This day started year 887E.N.

The Egyptian calendar was reformed by the Roman Emperor Augustus in 23 B.c..He decreed that a sixth epagomenal day should be inserted once every four years to keep it insynchronywith the Julian calendar.Thismodified calendaris sometimes called the Alexandriancalendar.

ThisAlexandrian calendar is not extinct even today.Calendars closely similar to it are used by the Coptic Church inmodern Egypt and in Ethiopia.It was also used bya variety of cultures and religions including The Zoroastrian Parsees,the Armenian Church and the French Republicansafter their revolution.

# 15.2.2Rules of the Egyptian Calendar

The Egyptian calendar has 12 months of 3O days in each;the five epagomenal days may be considered to forma thirteenth month of five days.Thus,each yearhas exactly 365 days.The day Thoth1,1E.N.wasWednesday,February 26, $- 7 4 6$ in the proleptic Julian Calendar and hadaJulianDayNumber1448 638.

The Alexandrian version has an extra leap day,a sixth epagomenal day,intercalated at the end of the thirteenth month once every four years.

# 15.3 The Roman and Julian Calendars

# 15.3.1 Introduction

TheRoman calendarwas probably originally lunarand relied on intercalations,which were applied haphazardly.It underwent several alterations in which the names and lengths of the monthswere changed,although some of the details are lost.By $- 4 5$ ,therewere12months mostly with names similar to those in the current Gregorian calendar,though the numbers of daysin several were different. The year started on Januarius1.

At one time the years were indicated by aregnal system that mentioned the names of the current Consuls.Later,in the first century B.c.,the years were numbered from the presumed date of the foundation of Rome, $- 7 5 2$ ;theseare termed ab urbe condita (A.U.C).Laterstill theEmperorDiocletian instituted an erawhich started with his accession in 283.

# 15.3.2Divisions of the Roman Months

The Roman months were divided into three unequal sections,which may,when the Roman calendar was lunar,have marked the phases ofthe Moon.The last days ofeach section,which wemaycall the division points,were called theKalends (Kalendae),theNones (Nonae)and theIdes (Idus).The Kalendswasthe first day of the month;the Ides,the thirteenth of the month,exceptinMarch,May,July,andOctober,whenitwas thefifteenthday.TheNones wasalwayseight daysbefore the Ides (see Table15.4).The dayspreceding the division pointswere termed Prid.Kal. (pridie $=$ daybefore),Prid.Non.andPrid.Id.respectively.The remaining days were numbered backwards from the division days as indicated in Table15.4 and labelled with the month inwhich the division point fell.For example,January 4 was termed Prid.Non.Jan.and January 11 was IIIId.Jan.Confusingly,but logically,the days preceding the Kalendswhich fell in the previous month were labelled by the month in which the division point fell,rather than the month to which theybelonged; thus December 3O was called IIIKal.Jan.This Roman system is occasionally used,even to this day.

# 15.3.3 Caesar'sReform

By $- 4 6$ ，the Roman calendar had gone badly awry；the months no longer followed the lunations and the yearhad lost step with the cycle of seasons (see Michels 1978;Bickerman 1980).This state of affairs was reformed by Julius Caesar(1O7-44 B.c.),who took the advice of the Alexandrian astronomer,Sosigenes.

Caesar first inserted 9O days into the year $- 4 5$ to bring the months of the Roman calendar back to their traditional placeswith respect to the seasons.Thisyear has beencalled“the lastyear of confusion.”He next changed the length of some of the old months.Finally he made provision foran intercalary dayto be inserted every four years.This intercalary day (see $\ S \ 1 5 . 3 . 5 $ wasinsertedbeforeVIKal.Mar.and termedBisVIKal.Mar.; itfellbetween VIIKal.Mar.(February 23)andVIKal.Mar.(February 25th).Years in which thiswas done were termed bissextileyears.

This new Roman calendar,the Julian calendar,was thus a solar calendar. The average length of the calendar year was 365.25 days so that the vernal equinox fell back from March 21by one day inabout13O years.Neverthelessitservedasastandard forEuropean civilisation until the Gregorian Reform of 1582.

Following Caesar's death,the Roman calendrical authorities misapplied the leap-year rule,with theresultthatthe intercalaryday was inserted every third,ratherthan every fourth, year.Thiserrorwas rectified byAugustusin $^ { - 8 , }$ Thedetails of thiscorrectionare uncertain but it is likely that he decreed that there should be no intercalationin the years $^ { - 7 }$ to $+ 6$ and that there should be intercalary days (leap days) inserted every fourth yearfrom then on(i.e., in years 8,12,16...).

Table15.4 Roman dating in the Julian calendar   

<table><tr><td></td><td>Januarius Augustus December</td><td>Februarius</td><td>Martius Maius Julius October</td><td>Aprilis Junius September November</td></tr><tr><td>1</td><td>Kalendae</td><td>Kalendae</td><td>Kalendae</td><td>Kalendae</td></tr><tr><td>2</td><td>IV Non.</td><td>IV Non.</td><td>VI Non.</td><td>IV Non.</td></tr><tr><td>3</td><td>III Non.</td><td>III Non.</td><td>VNon.</td><td>III Non.</td></tr><tr><td>4</td><td>Prid. Non.</td><td>Prid. Non.</td><td>IV Id.</td><td>Prid. Non.</td></tr><tr><td>5</td><td>Nonae</td><td>Nonae</td><td>III Non.</td><td>Nonae</td></tr><tr><td>6</td><td>VIII Id.</td><td>VIII Id.</td><td>Prid. Non.</td><td>VIII Id.</td></tr><tr><td>7</td><td>VII Id.</td><td>VII Id.</td><td>Nonae</td><td>VII Id.</td></tr><tr><td>8</td><td>VI Id.</td><td>VI Id.</td><td>VIII Id.</td><td>VI Id.</td></tr><tr><td>9</td><td>V Id.</td><td>V Id.</td><td>VII Id.</td><td>V Id.</td></tr><tr><td>10</td><td>IV Id.</td><td>IV Id.</td><td>VI Id.</td><td>IV Id.</td></tr><tr><td>11</td><td>III Id.</td><td>III Id.</td><td>V Id.</td><td>III Id.</td></tr><tr><td>12</td><td>Prid. Id.</td><td>Prid. Id.</td><td>IV Id.</td><td>Prid. Id.</td></tr><tr><td>13</td><td>Idus</td><td>Idus</td><td>III Id.</td><td>Idus</td></tr><tr><td>14</td><td>XIX Kal.</td><td>XVI Kal.</td><td>Prid. Ides</td><td>XVIII Kal.</td></tr><tr><td>15</td><td>XVIII Kal.</td><td>XV Kal.</td><td>Ides</td><td>XVII Kal.</td></tr><tr><td>16</td><td>XVII Kal.</td><td>XIV Kal.</td><td>XVII Kal.</td><td>XVI Kal.</td></tr><tr><td>17</td><td>XVI Kal.</td><td>XIII Kal.</td><td>XVI Kal.</td><td>XV Kal.</td></tr><tr><td>18</td><td>XV Kal.</td><td>XII Kal.</td><td>XV Kal.</td><td>XIV Kal.</td></tr><tr><td>19</td><td>XIV Kal.</td><td>XI Kal.</td><td>XIV Kal.</td><td>XIII Kal.</td></tr><tr><td>20</td><td>XIII Kal.</td><td>X Kal.</td><td>XIII Kal.</td><td>XII Kal.</td></tr><tr><td>21</td><td>XII Kal.</td><td>IX Kal.</td><td>XII Kal.</td><td>XI Kal.</td></tr><tr><td>22</td><td>XI Kal.</td><td>VIII Kal.</td><td>XI Kal.</td><td>X Kal.</td></tr><tr><td>23</td><td>X Kal.</td><td>VII Kal.</td><td>X Kal.</td><td>IX Kal.</td></tr><tr><td>24</td><td>IX Kal.</td><td>VI Kal.</td><td>IX Kal.</td><td>VIII Kal.</td></tr><tr><td>25</td><td>VIII Kal.</td><td>VKal.</td><td>VIII Kal.</td><td>VII Kal.</td></tr><tr><td>26</td><td>VII Kal.</td><td>IV Kal.</td><td>VII Kal.</td><td>VI Kal.</td></tr><tr><td>27</td><td>VI Kal.</td><td>III Kal.</td><td>VI Kal.</td><td>VKal.</td></tr><tr><td>28</td><td>VKal.</td><td>Prid. Kal.</td><td>VKal.</td><td>IV Kal.</td></tr><tr><td>29</td><td>IVKal.</td><td></td><td>IV Kal.</td><td>III Kal.</td></tr><tr><td>30</td><td>III Kal.</td><td></td><td>III Kal.</td><td>Prid. Kal.</td></tr><tr><td>31</td><td>Prid. Kal.</td><td></td><td>Prid. Kal</td><td></td></tr></table>

# 15.3.4The Julian Calendarin Medieval Europe

Through the Middle Ages the use of theJulian calendar evolved and acquired local peculiarities that continue to snare the unwary historian.There were variations in the initial epoch forcountingyears,the datefor beginningtheyear,and themethodof specifying theday of the month.Not only did these vary with time and place,but also with purpose.Different conventions were sometimes used for dating ecclesiastical records,fiscal transactions,and personal correspondence.

Caesar designated January1as the beginning of the year.However,other conventions flourished at different times and places.The most popular alternativeswere March1,March 25,and December 25.This continues to cause problems for historians,since,for example, 998February 28 as recorded ina city that began its year on March1,would be the same day as999February 28of acity thatbegan theyear onJanuary1.

Bythe eleventh century,consecutive counting of days from the beginning of the month came into use,displacing the Roman system of divisions.Local variations continued,however,including counts of days from dates that commemorate local saints.Auniform standard forrecording dateswasinstituted only after the inaugurationand spread of the Gregorian calendar.TheleapdaybecameFebruary29 insteadofthedayafterFebruary23.

Cappelli (1930),Grotefend and Grotefend (1941),and Cheney (1981) offer guidance through the maze of medieval dating.

Today the Julian calendar continues to be used by chronologists.The Julian proleptic calendaris formedbyapplying therules oftheJuliancalendar to times beforeCaesar’s reform. This provides a simple chronological system for correlating other calendars and serves as the basis for the Julian Day Numbers (see $\ S \ 1 5 . 1 . 1 0 \rangle$ .

# 15.3.5Rules for theJulian Calendar

The month names and the number of days in each are listed in Table 15.5 for the Julian calendar.The monthsin the Gregoriancalendarare identical.

Table 15.5 Months and days therein of the Julian and Gregorian calendars   

<table><tr><td colspan="3">Month</td><td colspan="3">Montha</td></tr><tr><td>1.</td><td>January(Januarius)</td><td>31</td><td>7.</td><td>July (Julius)</td><td>31</td></tr><tr><td>2.</td><td>February (Februarius)</td><td>28</td><td>8.</td><td>August (Augustus d)</td><td>31</td></tr><tr><td>3.</td><td>March (Martius)</td><td>31</td><td>9.</td><td>September (September)</td><td>30</td></tr><tr><td>4.</td><td>April (Aprilis)</td><td>30</td><td>10.</td><td>October (October)</td><td>31</td></tr><tr><td>5.</td><td>May (Maius)</td><td>31</td><td>11.</td><td>November(November)</td><td>30</td></tr><tr><td>6.</td><td>June (Junius)</td><td>30</td><td>12.</td><td>December (December)</td><td>31</td></tr></table>

ä These months were at one time the 5th,6th 7th,8th,9thand 1Oth aptly named months of the Roman year. b Originally called Quintilis but renamed inhonourofJulius Caesar. C Inaleapyear,February has 29 days dOriginally called Sextilis but renamed in honourofthe emperor Augustus.

AJulian calendar year thus contains 365days or366 ina leap year.Yearsare,today, counted from the initial epoch defined by Dionysius Exiguus (see $\ S \ 1 5 . 1 . 8 $ Aleap day, February29,is intercalated afterFebruary28in leap years.Leap yearsare divisibleby4, e.g., $+ 2 0 0 0$ wasaleap yearbut $+ 2 0 0 1$ was not.For this purpose,yearO(or1 B.C.,see $\ S 1 5 . 1 . 9$ ） is considered to be divisible by 4.

The epoch of the calendar (Saturday,1 January1) had a Julian Day Number 1721 424

# 15.4 The Gregorian Calendar

# 15.4.1History of the Gregorian Reform

The early Christians church adoptedtheJulian calendar and used it as the basis for calculating the date of Easter following the recommendation of the Council of Nicea held in 325.March 21was assumed to be the date of the equinox and the Metonic cyclewas used as the basis for calculating the lunar phases.

Bythe thirteenth century it was realised that the true vernal equinox had regressed from March 21 to an earlier day in March.Over the next four centuries,scholars debated the “correct”time for celebrating Easter and the need forareform of the calendar.The Church madeintermittentattemptsto remedy thematter,without takingaction.

Bythe sixteenth century the equinox had shifted to March 11,and astronomical new moons were occurring four days before the dates assumed in the calculation of the date of Easter.At the behestofthe Councilof Trent,Pope PiusVintroduced anew Breviary in1568 and Missal in157o,both of which included adjustments to the lunar tables and the leap-year system.Pope Gregory XIII,who succeeded PopePius in 1572,convened a commission to consider reform of the calendar,since he considered his predecessor's measures inadequate.

Thiscommission adopted a proposal suggested by Aloysius Lilius (1510-1576) and issued a report writen by Christopher Clavius (1537-1612)which resulted in a papal bull, “inter Gravissimas”signed by Gregory XII on 1582 February 24.

Ten dayswere deleted from the calendar,so that 1582 October 4 was followed by1582 October 15,thereby causing the vermal equinox of 1583 and subsequent years to returm to aboutMarch 21.Therules for intercalatinga leap daywere changed,and anew method of calculating the dates of Easter was introduced.The new method of intercalation meant that a period of 400 years contained146 O97 days.Since 146 097is divisible by7,the Gregorian civil calendar exactly repeats after 4OO years.The average number of days ina year is 365.2425.(see Table15.1).Itwould be one day out of synchrony with the vernal equinox year after about another 3OOO years (if the year were to remain unchanged in length).

This Gregorian calendar today serves as an international standard for civil use.In addition, it regulates the ecclesiastical calendar of the Catholicand Protestantchurches but was rejected bythe Orthodox churches.It was first promulgated and adopted throughout the Roman Catholicworld;the Protestant states initiallyrejected it,but one by one theyaccepted it over the coming centuries.England (and her then American colonies) finally accepted the change in 1752 when11 dayswere lost;contrary to popular belief there is no evidence for riots in protest at this (Poole 1998).The Eastern Orthodox churches continue to use the Julian calendar with the traditional lunar tables for calculatingEaster.Because thepurpose of the Gregorian calendar was to regulate the cycle of Christian holidays,its acceptance in the non-Christian world was initially not at issue.

Detailed information about the Gregorian reform may be found in the collection of papers resulting froma conference sponsored by the Vatican to commemorate its four-hundredth anniversary (Coyne,Hoskin and Pedersen 1983).

# 15.4.2Rules for the Civil Use of the Gregorian Calendar

The Gregorian calendar uses the same months with the numbers of days as it predecessor, theJuliancalendar(see Table15.5).Daysare counted from the first day of each month.

Yearsare counted from the initial epoch defined by Dionysius Exiguus (see $\ S \ 1 5 . 1 . 8$ ）， and each begins on January1.Acommon year has 365days but a leap year has 366,with anintercalaryday,designatedFebruary29,precedingMarch1.Leapyearsare determined according to the following rule:

Everyyear thatis exactlydivisible by4isaleap year,except foryears that are exactly divisible by10o,but these centurial years are leap years if they are exactly divisible by 400.

As a result, the year 20oO was a leap year, whereas 19o0 and 210O are not.

The epoch of the Gregorian calendar,(1 January1) wasMonday,1January 3 in the Julian calendar or Julian DayNumber1721426.

# 15.4.3Rules forthe Ecclesiastical Calendar

The ecclesiastical calendars of Christian churches are based on cycles of movable and immovable feasts.Christmas is the principal immovable feast,with its date set at December 25. Easteris the principal movable feast,and dates of most other movable feasts are determined with respect to Easter. However,the movable feasts of the Advent and Epiphany seasons are Sundays reckoned from Christmas and the Feastof the Epiphany,respectively.

In both the Julian and Gregorian calendars,the date of Easter is defined to occur on the Sunday following the ecclesiastical fullmoon that falls on or next afterMarch 21.This should not be confused with the popular notion that Easter is the first Sunday after the first full moon following the vernal equinox.In the first place,the vernal equinox does not necessarily occur onMarch 21.Secondly, the ecclesiastical full moon is not the astronomical full moon.It is based on tables that do not take into account the fullcomplexity of lunar motion.As a result, the date of an ecclesiastical full moon may difer from that of the true full moon.However, the Gregorian system of leap yearsand lunar tables prevents any progressive departure of the tabulated date from the astronomical phenomena.

The ecclesiastical full moonis defined as day14 of a lunation,where the day of the ecclesiastical new moon is counted as day 1.The tablesare based on the Metonic cycle, in which 235 mean synodic months contain 6939.688 days.Since nineteen Gregorian years contain 6939.6O75days,the dates ofMoon'sphases ina givenyearwill recur on nearly the same dates nineteen years later.To prevent the 0.O8-day difference between the cycles from accumulating,the tables incorporate adjustments to synchronise the system overlonger periods of time.Additional complications arise because the ecclesiastical lunations are of 29or 30 integral days.The entire calendar involvesa cycle 57oo ooO years containing 2081 882 250 days,which are equated to 70 499175 lunations.After this period,the dates of Easter repeat themselves.

The date of Easterascalculated in the Gregorian calendar isused by theCatholic and most Protestant churches.However,the Eastern Orthodox churches still calculate the date of Easter in the Juliancalendar,though some such churches have,in this century,modified the original method of calculation.

# 15.4.4 Calculation ofthe Date of Easter Sunday

The date of Easter was calculated using three parameters.

Thefirstof these is the Dominical (or Sunday)Letter.This defines the positions ina year of the Sundays.It is obtained by labelling the days of the year consecutively with the seven lettersA to G.And for the next7,againA-Gand so on.TheDominicalLetter is the letter so assigned to the first Sunday (and every other).It changes from year to year.

Equating A with $^ { 1 , \mathrm { B } }$ with 2etc.,theDominicalLetterforyear $Y$ is given by the equivalent to the number, $N$ ,in:

$$
N = 7 - { \bmod { ( Y + Y / 4 + 4 , 7 ) } } \quad { \mathrm { i n ~ t h e ~ J u l i a n ~ c a l e n d a r } }
$$

or

$$
N = 7 - { \bmod { ( Y + Y / 4 - Y / 1 0 0 + Y / 4 0 0 - 1 , 7 ) } } \quad { \mathrm { i n t h e ~ G r e g o r i a n ~ c a l e n d a r } } .
$$

The second,the Golden number,is the position(1 to19) of a year in the 19 yearMetonic cycle. If $Y$ isthe year in either the Julianor Gregorian calendar,the golden number, $^ { G }$ ,is given by:

$$
G = 1 + { \bmod { ( Y , ~ 1 9 ) } } .
$$

The third is theEpact of a year.It is the age in days (O to 29) of the ecclesiastical moon on the first day of the year (January 1).

For the Dionysian canon(tiedto the Julian calendar),the epact, $E$ ,ofayearwithaGolden number $\mathbf { G }$ is given by:

$$
E = \mathrm { m o d } ( 1 1 * G - 3 , 3 0 ) .
$$

In the Gregorian canon,the calculation of the epact is more complicated.First the basic formula for the epact is changed to:

$$
E = \mathrm { m o d } ( 1 1 * G - 1 0 , 3 0 ) .
$$

But this must be modified by the addition of the so called solar (SOL)and lunar (LUN) equations.

The solar equation firstly makes an adjustment needed to return the date of the vernal equinox to its traditional date close to March 21.Secondly it makes an adjustment of the decreased length of the Gregorian year.It is given by:

$$
\mathrm { S O L } = H - H / 4 - 1 2 .
$$

The lunar equation likewise gives an adjustment to correct the average length of a lunation to value more close to that of the real Moon.It is given by:

$$
\mathrm { L U N } = ( H - 1 5 - ( H - 1 7 ) / 2 5 ) / 3 .
$$

In both these expressions, $H = Y / 1 0 0$ where $Y$ is the year.

Afurther adjustment of 1day is required of the Golden number if $E = 2 5$ and $G \ge 1 2$ or $E = 2 4$ .This is to maintain a traditional requirement that no two new moons fell on the same dayof theyear inaMetonic cycle of19 years.Itmaybe calculated as $V$ in

$$
V = E / 2 4 - E 2 5 + ( G / 1 2 ) * ( E / 2 5 - E - 2 6 )
$$

so that the adjusted Epact is

$$
E = { \bmod { ( } } 1 1 * G - 1 0 , 3 0 ) - { \bmod { ( } } { \mathrm { S O L } } - { \mathrm { L U N } } , 3 0 ) + V .
$$

The day of Easter Sunday is then given asaDay of March, $s$ ,(i.e.,counting from March 1 as day 1)in terms of this modified epact $E$ by:

$$
S = R + { \bmod { ( 7 + N - C , 7 ) } }
$$

where

$$
C = 1 + { \bmod { ( R + 2 , 7 ) } }
$$

and

$$
\begin{array} { r } { R = 4 5 - E \quad \mathrm { i f } \ E < 2 4 } \\ { \mathrm { o r } \ R = 7 5 - E \quad \mathrm { i f } \ E \geq 2 4 } \end{array}
$$

See $\ S 1 5 . 1 1 . 1$ fora full explanation of the mathematical notationused here.Details of the calculation are discussed at length by Butcher(1877), Oudin (1940)and Richards (1998).

# 15.5 The Jewish Calendar

# 15.5.1History of theJewish Calendar

The codified Jewish calendar as we know it today is generally considered to date from about 359,though the exact dateis uncertain.

Jewish calendrical practices before that are uncertain.The earliest evidence indicates acalendar based on observations of thephases of the new moonat Jerusalem.Since the Bible mentions seasonal festivals,there were probably intercalations.There was probably an evolution of conflicting calendrical practices.

TheBabylonian exile,in the first half of the sixth century B.C.,greatly influenced the Jewish calendar.The names of the months are very similarto those in the Babylonian calendar and the practice of intercalating months may have been learnt from the Babylonians.

During the period of the Sanhedrin the calendar was observational; months began with sightings of the crescent of the newmoon.Acommittee of the Sanhedrin met to evaluate reports of sightings.If sightings were not possible,the new month was begun 3O days after the beginning of the previous month.Decisions on intercalation were influenced,if not determined entirely,by the state of vegetationand animal life.Although eight-year,nineteenyear,and longer-period intercalation cycles may have been instituted at various times prior to Hillel I,there is lite evidence that they were employed consistently over long periods. The Sanhedrin was entrusted to run the calendar and only its members knew how to do it.

After the Diaspora,this arrangement became unworkable;by the time news of sightings atJerusalem reach outlying Jewish communities,the start of the months Was well past.The patriarch Hillel II is credited with reforming this state of affairsby disseminatingcodified rules,whichanybody,anywhere,could follow.

Theexact detailsofHillel'scalendar havenot survived,but itis generallyconsidered to include rules for intercalation over nineteen-year cycles.Up to the tenth century A.D., however,there was disagreement about the proper years forintercalation and the initial epoch for reckoning years.

The modern Jewish calendaris the officialcalendarof Israel and is the liturgical calendar of the Jewish faith.

# 15.5.2Rules for the ModernJewish Calendar

The day of theJewish calendar is divided into 24 hours and each hour into1O8o halakim (hk). Thus,there are 1O secondsin3 halakim.The day begins at $1 8 . 0 0 \mathrm { P . M }$ ,thatis six hours in advance of our current calendrical day and this is counted as $0 \mathrm { { h r } 0 \mathrm { { h k } } }$ in Jewish timekeeping. The days of the week are numbered from Sunday (1) to Saturday,the Sabbath (7).

Asitexists today,theJewishcalendarisaluni-solar calendar thatisbasedoncalculation rather than observation and is based on the Metonic calendar.Its regulation depends on three levels of abstraction.First,there is the real astronomical moon;secondly,a highly regular but fictitious moon whose behaviouris close to the average behaviourofthe real Moon and which defines the astronomical calendar.Each month and year of the later starts at the instant of conjunctionofthe fictitious moon;thisis termeda Molad.Thirdly,thereis thecivil calendar; the monthsand years of this start on,or up to two daysafter,the molad.Thus,the start of acivil year may be postponed from the date of its molad by the application of four rules (dehiyyot).

The epoch of the calendar is taken to occur in the same year, $- 3 7 6 0$ ,as the Creation as described in Genesis.Thisyear was calculated inabout the 1Oth century byMaimonedes from data in the Bible,which gives the generation times of the Patriarchs from Adam,and important historical dates culminatingin the sack of Jerusalemby the Romans which can be dated historically.The results of such calculations are controversial but Maimonedes’value isaccepted by the Jewish religion.

Years counted from this epoch define the Mundane Era (Anno Mundi,A.M.)and it may benoted that theJewish year,Y,currently beginsin the autumn of the Gregorian or Julian year: $Y - 3 7 6 1$ .Theepochof thecalendar,the first dayofTishri is1A.M.isonMonday, -3760 October7in the proleptic Julian calendar with aJulian Day Number of 347 998.This epoch is not the date of the creation itself; this is taken to have occurredinthe next September.

The yearsare counted incycles of19 years,and in this period thereare 12common years of 12 months apiece and 7leap years each containing13 months;thus there are 235 months in the19-year cycle.The leap years are now fixedas the 3rd,6th,8th,11th,14th,17thand 19th year of each cycle

The total period ofthis 19-year cycle is 6939 days,16 hours,595 halakim (=6939.689 590 days)so thatthe average number of days ina yearis 365.24682.Thus,the average start of the Jewish year is currently falling behind the mean tropical year by about1 day in 2OO years.

Eachcivil yearisdeemed tostartwith thefirstdayof the first month,Tishri.Thefirst (fictitious)molad,which initiates year1,and which is the first year of a19 yearcycle,is deemed to have taken place on the Monday,October7, $- 3 7 6 0$ at $1 1 { : } 2 0 \ \mathrm { P } . \mathrm { M }$ .orTishri 1, A.M. 1 at $5 \mathrm { h r }$ $2 0 4 \mathrm { h k }$ ；it is asimple matterto calculate the molad of Tishri ofany succeeding yearby addinganappropriate multiple ofthe interval between successive moladot to the time of this first molad.

Table15.6 Numberof days in the six categories of the Jewish year   

<table><tr><td></td><td>Common year</td><td>Leap year</td></tr><tr><td>Deficient</td><td>353</td><td>383</td></tr><tr><td>Regular</td><td>354</td><td>384</td></tr><tr><td>Abundant</td><td>355</td><td>385</td></tr></table>

Table15.7 Months and days therein of the Jewish calendar   

<table><tr><td colspan="3">Month</td><td colspan="3">Month</td></tr><tr><td>1.</td><td>Tishri</td><td>30</td><td>7.</td><td>Nisan</td><td>30</td></tr><tr><td>2.</td><td>Heshvan</td><td>29a</td><td>8.</td><td>Iyar</td><td>29</td></tr><tr><td>3.</td><td>Kislev</td><td>30b</td><td>9.</td><td>Sivan</td><td>30</td></tr><tr><td>4.</td><td>Tebet</td><td>29</td><td>10.</td><td>Tammuz</td><td>29</td></tr><tr><td>5.</td><td>Shebat</td><td>30</td><td>11.</td><td>Ab</td><td>30</td></tr><tr><td>6.</td><td>Addar</td><td>29</td><td>12.</td><td>Elul</td><td>29</td></tr></table>

" In an abundant year,Heshvan has 30 days. bInadeficientyearKislevhas29days. cInaleap year,Addarhas 3O days;itis followed by AddarII with 29 days.

Successive moladot occurat fixed intervals of 29 days $1 2 \mathrm { h r }$ and $7 9 3 ~ \mathrm { h k }$ $( = 2 9 . 5 3 0 5 9 4 $ days).Theydo not coincide with the phases of the real astronomical Moon,but they should remain in average synchrony fora very long time.Calendrical dates are worked out,independent of longitude using local times.

The rules of postponement and the insertion of leap month imply that the number of days inayear varies.There are six types of calendar year,according to the number of daysin them.Firstly,a year may be common or leap;common years contain 12 months and leap years contain13.Furthermoreany year may be deficient,regular or abundant.The numbers of days in the six types of year are shownin Table 15.6.The namesof the months and the numberof days therein are shown in Table15.7 Generally the number of daysin the month alternate between 30 and29.

# 15.5.3Rules for Postponement (Dehiyot)

Below are the four rules that determine whether Tishri 1 should be postponed until after itsmolad.The first three are sometimes termed astronomical ruleswhile the fourth is termed a political rule.We also give below the reason underlying each rule.Only one of the astronomical postponements should be applied.Rule (4)is applied last but its application may be required after the application of one of the other three to give a second postponement.