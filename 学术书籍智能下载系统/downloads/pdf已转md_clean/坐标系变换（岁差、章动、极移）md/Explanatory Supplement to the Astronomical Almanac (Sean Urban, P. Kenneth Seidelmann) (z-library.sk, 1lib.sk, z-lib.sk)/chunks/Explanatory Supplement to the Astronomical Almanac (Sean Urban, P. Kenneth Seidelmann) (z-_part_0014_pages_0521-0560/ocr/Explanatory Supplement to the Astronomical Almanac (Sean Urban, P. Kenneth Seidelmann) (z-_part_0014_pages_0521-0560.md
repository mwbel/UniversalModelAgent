![](images/0751fe21fdbd10758257ce0cd0439c64d7b4a5e339992f748509280cd0f7defc.jpg)  
Figure11.14 Definition of auxiliary quantity $\psi$ . $L$ isradius of the shadow in the plane of the observer, $\Delta$ isdistance of observer from the axis, $n$ isspeed of separation, $s$ issemiduration.

From maximum eclipse,semiduration of the partial phase may be estimated as follows. Define $\psi$ in Fig.11.14,where $s$ is the semiduration and $n$ is the speed of the shadow. The respective units are hours and equatorial radii per hour. Then

$$
s = ( L _ { i } \cos \psi ) / n ,
$$

where

$$
\begin{array} { l } { { n ^ { 2 } = ( \dot { x } - \dot { \xi } ) ^ { 2 } + ( \dot { y } - \dot { \eta } ) ^ { 2 } } } \\ { { \dot { \xi } = \dot { \mu } \cos \psi \cos \theta } } \\ { { \dot { \eta } = \dot { \mu } \xi \sin d . } } \end{array}
$$

The exact durationis found from the difference in times offirst andlast contacts,as described in $\ S 1 1 . 3 . 6 . 2$ .

The magnitude of the eclipse is found from

$$
{ \frac { L _ { 1 } - \Delta } { L _ { 1 } + L _ { 2 } } } .
$$

If $L _ { 2 }$ is not available,the approximation $L _ { 2 } = L _ { 1 } - 0 . 5 4 5 9$ is used.(Subscript 1forpenumbra, 2 for umbra.)

Curves of equal semiduration or equal magnitude must be found by inverse interpolation on curves of maximum eclipse.(See $\ S \ 1 1 . 3 . 6$ on local circumstances for further discussion of magnitude.)

# 11.3.5.6 General Circumstances

A collection of event points known as the general circumstances are the important extrema of the curves of the eclipse.They define the bounds of the eclipse on the spheroidal surface andin time.Theyalso join together the variouscurvesand areessentialin preparing the eclipse map.General circumstances are computed from the Besselian elements through a set of discriminants.For each discriminant,atable of values is calculated fora sequence of times, and used as described in the subtopicswithin this(§11.3.5.6) section.In practice,general circumstances are calculated before the complete curves are generated.If circumstancesare required for high altitudes,the calculations are repeated fora larger spheroid.

The first and last contacts of the penumbra occur for every solar eclipse.They are the points where the shadow cone of the Moon first and last encounters the spheroidal surface. These points are shown on the eclipse maps as First Contact and Last Contact,and always lie onthe rising and seting curve.The times at which they occur define the date(s)of the eclipse.

If the eclipse is central,then there are first and last contacts of the umbra.These are the extreme end points ofthe central line,and fall on the curve of maximum eclipse in the horizon.

Fora central eclipse,there are also extreme points of the northern and southern limits of the central track.It is a rare occurrence when only one limit exists.These points also fall on the curve of maximum eclipse in the horizon.

The extreme points of the northern and southern limits of the penumbra fall on both the rising and setting curve and the curve of maximum eclipse in the horizon and,thus,mark the joining points.The extremes need not be known accurately; they are the points at which an observer theoreticallycould“see”the limb of theMoon brush the limb of the Sun for an instant.If the eclipse curves have been calculated taking flattening of the spheroid into account,the samemust be done for thesepointsor thecurveswill notlink.

The point of central eclipse at local apparent noon or midnight is self-explanatory, ie., maximum occurs on the meridian.Meridian passage at midnight may occur in the polar regions.

The pointof greatesteclipse is calculated only for partial eclipses and shown on the eclipse map.It is the point on the spheroidal surface that comes closest to the axis of the shadow, and it lies on the curve of maximum eclipse in the horizon.

First and last contacts of the penumbra.First and last contacts of the penumbra occur when the shadow cone is tangential to the spheroid.Thus at two instants,

$$
x ^ { 2 } + y ^ { 2 } = ( l _ { 1 } + \rho ) ^ { 2 } .
$$

Taking the flattening of the Earth into account, let

$$
\begin{array} { c } { { m ^ { 2 } = x ^ { 2 } + y ^ { 2 } } } \\ { { } } \\ { { m _ { 1 } ^ { 2 } = x ^ { 2 } + y _ { 1 } ^ { 2 } } } \\ { { } } \\ { { y _ { 1 } = y / \rho _ { 1 } } } \\ { { } } \\ { { \rho = m / m _ { 1 } . } } \end{array}
$$

Then $x ^ { 2 } + y _ { 1 } ^ { 2 } = ( l _ { 1 } + m / m _ { 1 } ) ^ { 2 }$ is the condition;the discriminant is

$$
D _ { 1 } \equiv x ^ { 2 } + y _ { 1 } ^ { 2 } - ( l _ { 1 } + m / m _ { 1 } ) ^ { 2 } .
$$

In the table of discriminants,the times of the contacts are calculated by inverse interpolation when $D _ { 1 } = 0$ .These timesare used to obtain $x$ , $y$ ,and $\rho _ { 1 }$ .At the times of contact,

$$
\begin{array} { c } { \xi = x / m _ { 1 } } \\ { \eta _ { 1 } = y _ { 1 } / m _ { 1 } = y / \rho _ { 1 } m _ { 1 } } \\ { \zeta _ { 1 } = 0 } \end{array}
$$

gives the data to compute latitude and longitude by successive approximation.

Beginning and end of central eclipse.Central eclipse begins and ends when the shadow axis is tangential to the Earth's surface—i.e.,

$$
\begin{array} { r } { x ^ { 2 } + y _ { 1 } ^ { 2 } = 1 } \\ { \xi = x } \\ { \eta _ { 1 } = y _ { 1 } } \\ { \zeta _ { 1 } = 0 . } \end{array}
$$

Thediscriminantis

$$
D _ { 2 } \equiv x ^ { 2 } + y _ { 1 } ^ { 2 } - 1
$$

and the procedure is the same as for the penumbra.

Extreme points of umbral and penumbral limits.The extreme points of the limits of umbra and penumbra are found by setting $\zeta _ { 1 } = 0$ and then calculating tan $\boldsymbol { Q }$ from Eq. 11.79.

$$
\begin{array} { c } { \cos Q = \pm { ( 1 + \tan ^ { 2 } Q ) ^ { - 1 / 2 } } } \\ { \sin Q = \cos Q \tan Q } \\ { \xi = x - l _ { i } \sin Q , \quad i = 1 , 2 , } \\ { \eta _ { 1 } = ( y \mp l _ { i } \cos Q ) / \rho _ { 1 } , \quad i = 1 , 2 , } \\ { \xi ^ { 2 } + \eta _ { 1 } ^ { 2 } = 1 . } \end{array}
$$

Note that the sign of cos $\boldsymbol { Q }$ determineswhether the point is on the northern or southern limit. Note also that there are two cones and,therefore,four discriminants of the form

$$
D _ { i } \equiv ( x - l \sin Q ) ^ { 2 } + \left( \frac { y - l \cos Q } { \rho _ { 1 } } \right) ^ { 2 } - 1 , \quad i = 3 , \ldots , 6 .
$$

Again,the times are found by inverse interpolation,and the coordinates,with fattening taken into account,by the usual procedure.

Central eclipse on the meridian. Central eclipse on the meridian—noon or midnight— is the point on the central line at conjunction of the Sun and the Moon in right ascension. The discriminant is $x$ ,and the condition is $x = 0$ .Test the signs carefully in polar regions,to distinguish noon from midnight.

Greatest eclipse.In partial eclipses,the maximum magnitude,or greatest eclipse,occurs at the point on the surface of the spheroid that comes closest to the axis of the shadow. The magnitude changes very slowly,so high precision is not required.The eclipse will occur in the horizonat thispoint,and it issufficientto find the time when the shadow axis isclosest to the center of the Earth or when the rate of change of separation goes to zero.Hence,the discriminant is

$$
D _ { 7 } \equiv x \dot { x } + y \dot { y } .
$$

When the time is known,position is found as before.The distance of the observer from the axisis

$$
\Delta = m - \rho .
$$

The magnitude of the greatest eclipse for this case is

$$
{ \frac { l _ { 1 } - \Delta } { l _ { 1 } + l _ { 2 } } } .
$$

# 11.3.6 Local Circumstances

Before proceeding,the readershould review $\ S 1 1 . 3 . 4$ on conditional and variational equations. Local circumstances provide a description of eclipse phenomena relative to a fixed reference position,which is equivalent to fixing $\rho$ asconstant.

# 11.3.6.1 Eclipse Maps

The eclipse maps currently given in The Astronomical Almanac show the region over which various phases of each solar eclipse may be seen and the times at which phases occur. Each map isa plot of the curves described in $\ S \ 1 1 . 3 . 5 . 5$ ,except that outline curves are limited to those of the penumbra every hour.

The outline curves are divided into leading edge (in short dash)and trailing edge (in long dash).Except for certain extreme cases,the shadow outline moves generally from west to east.For a given location,first contact (the beginning of partial eclipse)occurs when the leading edgeof the shadowarrives;similarly,last contact (the end of partial eclipse) occurs when the trailing edgearrives.Firstor last contact may be estimated fromthe map to within a few minutes.

# 11.3.6.2 Precise Calculations

There are many refinements to be considered in performing precise calculations:choosing aconsistent ephemeris,corrections forEarth'srateofrotation,and,forthe Moon,offsetof centerof figure fromcenter of mass;correcting forirregularities ofthe lunar limb;and effects of the Earth's atmosphere (refraction in solar eclipses and the effect on the shadow in lunar eclipses).

Some elements (e.g.,the radius of the shadow cone) used to describe an eclipse remain nearlyconstantfor the duration.Elementsthat changedosoverynearly linearly.Ineffect, an observer sees an eclipse as two disks of fixed size,one crossing the other in a straight line at constant speed.

In conventional notation,define $u$ ， $v$ such that:

$$
\mathbf { r } - { \boldsymbol { \rho } } = { \left[ \begin{array} { l } { x - \xi } \\ { y - \eta } \\ { 0 } \end{array} \right] } \equiv { \left[ \begin{array} { l } { u } \\ { v } \\ { 0 } \end{array} \right] } = \mathbf { m } .
$$

The distance from the observer to the nearest point of the shadow axis is $| \mathbf { m } | \equiv m$ .Let the relative velocity be $\mathbf { n } = \dot { \mathbf { m } }$ ，and then the relative speed is $| \mathbf { n } | \equiv n$ .The rate of separation is $\mathbf { m } \cdot \mathbf { n }$ ,andmaximum eclipse occurswhen the shadow axisisclosest to the observer,or $\mathbf { m } \cdot \mathbf { n } = 0$ .

Contact times and duration．At the beginning or end of penumbral,or partial, phase, the condition is $m = L _ { 1 }$ .Similarly,ifthe chosenpointis inthe central path,thenatthebeginning or end of umbral phase $m = L _ { 2 }$ .

There are methods for finding the times ofthese phenomena by successive iteration, using approximationsand auxiliary angles.However,it is simpler to tabulate $u$ , $\boldsymbol { \upsilon }$ , $\scriptstyle L$ (where $L$ iseither radius) as a function of time,and also the discriminant $u ^ { 2 } + v ^ { 2 } - L ^ { 2 }$ .When the discriminant goes to zero,inverse interpolation gives the time of the local contact.Duration is the difference between the two contact times for the umbra.

Position angles.The projected shadow is areflection of what the observer sees in the sky, so the position angle of contact, $\boldsymbol { Q }$ ,may be found from

$$
\begin{array} { r } { \mathbf { m } = \left[ \begin{array} { c } { L \sin Q } \\ { L \cos Q } \\ { 0 } \end{array} \right] . } \end{array}
$$

Theangle $\mathcal { Q }$ is measured eastward from the north,on the solar limb as the observer sees it,or theprojected shadow circle on the imaginary plane of reference.From the observer's point of view,however,the vertex (up) is not usually north.The parallactic angle $c$ ,definedby tan $C = \xi / \eta$ ,is the measure of the difference.The position angle $V$ of the contact point from thevertexis

$$
V = Q - C .
$$

Magnitude and obscuration.Magnitude is commonly confused with obscuration.Magnitude is defined as the fraction of the solar diameter covered by the Moon at the time of greatest phase and is expressed in units of the solar diameter.Obscuration is the fraction of the surface of the solar disk obscured by the Moon.

Inthecase of a total eclipse,the magnitude can be greater than 1.O.To derive the expression,however, consider the annular case shown inFig.11.15.An observer at point $B$ in the penumbra sees part $S ^ { \prime } B ^ { \prime }$ ofthe solar diameterblocked off,whereasanobserverat point $E$ intheumbra sees the Moon's entire disk projected in $D D ^ { \prime }$ on the Sun, $S S ^ { \prime }$ .

The known quantities are

At B,n

$$
\begin{array} { r l } & { \begin{array} { r l } { P ^ { \prime } O = P O = L _ { 1 } } \\ { f A ^ { \prime } O = A O = L _ { 2 } } \end{array} } \\ & { \begin{array} { r l } {  } & {  } \\ & { \Delta O = m . } \end{array} } \\ & { \begin{array} { r l } { \Delta O = m . } \\ & { \Delta ^ { \prime } } \\ & { \mathrm { ~ i s g ~ h i n t i a l ~ } M _ { 1 } = S ^ { \prime } \mathrm { S i g } } \\ & { = P A ^ { \prime } P A ^ { \prime } \mathrm { b y s ~ i m p l e ~ p r o p o r t ~ l e m ~ } } \\ & { = ( P O - B ) / ( P O + O A ) } \end{array} } \\ & { \begin{array} { r l } & { \quad = ( L _ { 1 } - m ) / ( L _ { 1 } + L _ { 2 } ) . } \\ & { \quad } \\ & { \mathrm { ~ i s g n i s t ~ } L _ { 2 } = D ^ { \prime } / S ^ { \prime } } \\ & { = ( S D - S D ^ { \prime } ) / S ^ { \prime } S } \\ & { = P E / P A ^ { \prime } - A L / P A ^ { \prime } } \\ & { = P A / P A ^ { \prime } } \\ & { = ( L _ { 1 } - L _ { 2 } ) / ( L _ { 1 } + L _ { 2 } ) . } \end{array} } \end{array}
$$

For a total eclipse,in which the plane is on the other side of the vertex, $A$ and $A ^ { \prime }$ are reversed, so that $O A = - L _ { 2 }$ ,and the expressionis identical.Note also that this is the diameter of the lunardisk in units of the diameter of the solar disk.

The degree of obscuration is now calculated using $L _ { 1 }$ , $L _ { 2 }$ ,and $m$ .In Fig.11.16, $A$ isthe center of the lunardisk, $B$ is the centerof the solar disk.The disks overlap,with intersections at $C , C ^ { \prime }$ The line $A B$ joins the centers andintersects the circumferences and thechord $C C ^ { \prime }$ at

At $\mathrm { E }$ ,n

![](images/9f78f60523b1799a9f819d9946026cb4399111be15e2d0789f657a96a6e472e6.jpg)  
Figure11.15 Magnitude is the fraction of the linear diameter of the Suncovered by the Moon.In this schematic of anannular eclipse,in the observer’s plane, $A ^ { \prime } A$ is the zone of annularity.To an observer within that zone at point $E$ ,theMoon'scross-section $M M ^ { \prime }$ projects onto $S S ^ { \prime }$ as $D D ^ { \prime }$ Hence the magnitude is $D ^ { \prime } D / S ^ { \prime } S$ Toan observer at point $B$ in the zone of partial eclipse, $S ^ { \prime } B ^ { \prime }$ is obscured,hence the magnitude is $S ^ { \prime } B ^ { \prime } / S ^ { \prime } S$ .

![](images/3aa96afa213190a7dbb0752d94b7d809871d7213f3d357a1b2e1dee9d61664ba.jpg)  
Figure11.16 Obscuration is the fraction of the area of the solardisk obscured by theMoon.Hereitis theratioof the area of segment $C D C ^ { \prime } F$ to the area of the solar disk.

the indicated points.Let the lunar radius be $s = A C$ .The solar radius is takenas unity; hence $B C = 1$ and $A C = M _ { 2 } \equiv s$ .By definition also,and in units of solar radius, $M _ { 1 } = D F / 2$ ,or $D F = 2 M _ { 1 }$ Finally,

$$
A B = 1 + s - D F .
$$

In terms of known quantities, then

$$
\begin{array} { l } { \displaystyle B C = 1 } \\ { \displaystyle A C = M _ { 2 } = \frac { L _ { 1 } - L _ { 2 } } { L _ { 1 } + L _ { 2 } } \equiv s } \\ { \displaystyle D F = 2 \frac { L _ { 1 } - m } { L _ { 1 } + L _ { 2 } } } \\ { \displaystyle A B = 1 + \frac { L _ { 1 } - L _ { 2 } } { L _ { 1 } + L _ { 2 } } - \frac { 2 ( L _ { 1 } - m ) } { L _ { 1 } + L _ { 2 } } = \frac { 2 m } { L _ { 1 } + L _ { 2 } } . } \end{array}
$$

The areaof the solardisk covered bythe Moonis given by

$$
S = { \mathrm { s e g m e n t } } C F C ^ { \prime } + { \mathrm { s e g m e n t } } C D C ^ { \prime } ,
$$

Using angles in radians:

$$
\begin{array} { c } { { \mathrm { A r e a ~ o f ~ s e c t o r ~ } A C F = s A } } \\ { { \mathrm { A r e a ~ o f ~ s e c t o r ~ } B C D = B } } \\ { { C E = s ~ \sin { A } = \sin { B } } } \\ { { A E = s \cos { A } } } \\ { { E B = \cos { B } . } } \end{array}
$$

Substituting into Eqs.11.128 and then Eq.11.127:

$$
{ \begin{array} { r l } & { \operatorname { s e g m e n t } C F C ^ { \prime } = 2 \left( { \frac { 1 } { 2 } } s ^ { 2 } A - { \frac { 1 } { 2 } } s ^ { 2 } \sin A \cos A \right) } \\ & { \operatorname { s e g m e n t } C D C ^ { \prime } = 2 \left( { \frac { 1 } { 2 } } B - { \frac { 1 } { 2 } } \sin B \cos B \right) } \\ & { \qquad S = ( s ^ { 2 } A + B ) - ( s ^ { 2 } \sin A \cos A + \sin B \cos B ) } \\ & { \qquad = ( s ^ { 2 } A + B ) - s \sin C . } \end{array} }
$$

The area of the solar disk is $\pi$ ;hence the obscuration asa fraction of the disk is $S ^ { \prime } { = } S / \pi$ .

The angles $A$ ， $B$ ,and $C$ may be evaluated from fundamental rules of trigonometry.The workingrelationsare:

$$
\begin{array} { r l r } {  { \cos C = ( L _ { 1 } ^ { 2 } + L _ { 2 } ^ { 2 } - 2 m ^ { 2 } ) / ( L _ { 1 } ^ { 2 } - L _ { 2 } ^ { 2 } ) , } } & { 0 \le C \le \pi } \\ & { \cos B = ( L _ { 1 } L _ { 2 } + m ^ { 2 } ) / m ( L _ { 1 } + L _ { 2 } ) , } & { 0 \le B \le \pi } \\ & { } & { A = \pi - ( B + C ) . } \end{array}
$$

If an observer wishes to construct a diagram showing the exact relationships of the disks during the course of an eclipse,it is useful to have calculated these quantities at a convenient tabular interval.Note that during central phase,all intersections cease to exist and the quantities are undefined.During that phase,for anannular eclipse $S ^ { \prime } = s ^ { 2 }$ ; for a total eclipse, $S ^ { \prime } = 1$

# 11.3.6.3Differential Corrections in Space and Time

Differential corrections were in times past used to adjust precisely calculated local circumstances to nearby locations.However, computing equipment has reached such a stage of advancement that differentials have fallen into disuse in favor of repeating the whole calculation for the new site.

Calculations are normally providedin provisional Universal Time(UT)or,more precisely, UT1 (see $\ S \ 3 . 2 . 2$ usingapredicted value of $\Delta T$ .For record purposes this is not necessarily the best practice,but for the convenience of users it was deemed significant enough to be necessary.If alater value of $\Delta T$ is adopted—such that the offset becomes $\Delta T + \delta T$ ——then tabular quantities may be corrected quite easily by applying

$$
\delta \lambda = - 1 . 0 0 2 7 3 8 \delta T \quad ( \mathrm { l o n g i t u d e m e a s u r e d e a s t w a r d } )
$$

toall longitudes in the tabulated phenomena,and subtracting $\delta T$ algebraically from all tabulated times expressed in UT.Finally,interpolate the table back to the original arguments.

For calculation of circumstances at elevations above the spheroid,the assumed radius of theEarthisincreased accordinglyand thecalculationsrepeated.

# 11.4 Lunar Eclipses

# 11.4.1 Introduction

The calculation of lunar eclipses follows the same principles as that of solar eclipses.The fundamental plane isperpendicular to the axis of the shadow,and the origin of coordinates

is the shadow'saxis.The $z$ -coordinateis notused.Since the observeris on the body that is casting the shadow,the circumstances are the same for allparts of the Earth from which the Moon is visible.

The criteria for the occurrence ofalunar eclipse,and the definitions of the types that may occur,are given in $\ S \ 1 1 . 2 . 3$ .

# 11.4.2 Computations

Equations 11.13and11.14 define specific values of the separation of centers at which contacts occur (see Fig.11.4).By conventional notation deriving from solar eclipses,the angular distance between the centers of the Moon and the shadowisdesignated $L$ and at times of contact hasvaluesas follows:

$$
\begin{array} { r l r } & { \mathrm { a t ~ b e g i n n i n g ~ a n d ~ e n d ~ o f ~ t h e ~ p e n u m b r a l ~ e c l i p s e } , \quad L _ { 1 } = f _ { 1 } + s _ { \mathrm { m } } ; } \\ & { \mathrm { a t ~ b e g i n n i n g ~ a n d ~ e n d ~ o f ~ t h e ~ u m b r a l ~ e c l i p s e } , \quad } & { L _ { 2 } = f _ { 2 } + s _ { \mathrm { m } } ; } \\ & { \mathrm { a t ~ b e g i n n i n g ~ a n d ~ e n d ~ o f ~ t h e ~ t o t a l ~ e c l i p s e } , \quad } & { L _ { 3 } = f _ { 2 } - s _ { \mathrm { m } } . } \end{array}
$$

Asis the case for solar eclipses,for dates when a lunar eclipse is to be calculated,apparent ephemerides of the Sunand theMoon are generatedata suitable interval, bysubtabulation if necessary.The usual interval is 1O minutes.The ephemeris is corrected for the offset of the center of figure from the center of mass,as appropriate for the chosen ephemeris,and the argument ischangedtoUTbyapplying $\Delta T$ .

# 11.4.2.1 Besselian Elements

Asin $\ S 1 1 . 3 . 2 . 2$ andEq.11.24,the geocentricunitvector totheSun,inanequatorial system,is

$$
\begin{array} { r } { \mathbf { r } _ { \mathrm { s G } } = \left[ \begin{array} { c } { \cos \alpha _ { \mathrm { s } } \cos \delta _ { \mathrm { s } } } \\ { \sin \alpha _ { \mathrm { s } } \cos \delta _ { \mathrm { s } } } \\ { \sin \delta _ { \mathrm { s } } } \end{array} \right] . } \end{array}
$$

It follows that the vector of theantisolar point,along the axis,is $\mathbf { r } _ { \mathrm { { a G } } } = - \mathbf { r } _ { \mathrm { { s G } } }$ Thisvector corresponds to $\mathbf { g }$ in Eq.11.25,with $a = \alpha _ { \mathrm { s } } + 1 2 ^ { \mathrm { h } }$ ， $d = - \delta _ { \mathrm { s } }$ ,for a geocentric system and eliminates the step of solving for $( a , d )$ .To transform the Moon'sposition to a geocentric systemin which the $z$ -axisis parallel to the axis of the shadow,apply the same rotations as givenin Eq.11.26,but for unitsuse seconds ofarc.This calculation gives Eqs.11.29,without the unit conversion factor,and from which only $( x , y )$ in the fundamental plane are used.

To summarize:

$$
\mathbf { r } _ { \mathrm { a G } } = \left[ \begin{array} { c } { \cos a \cos d } \\ { \sin a \cos d } \\ { \sin d } \end{array} \right] = - \mathbf { r } _ { \mathrm { s G } } = \left[ \begin{array} { c } { - \cos \alpha _ { \mathrm { s } } \cos \delta _ { \mathrm { s } } } \\ { \sin \alpha _ { \mathrm { s } } \cos \delta _ { \mathrm { s } } } \\ { - \sin \delta _ { \mathrm { s } } } \end{array} \right] .
$$

$$
\mathbf { r } _ { \mathrm { m F } } = \mathbf { R } _ { 1 } \left( { \frac { \pi } { 2 } } - d \right) \mathbf { R } _ { 3 } \left( a + { \frac { \pi } { 2 } } \right) \mathbf { r } _ { \mathrm { m G } } = { \left[ \begin{array} { l l l } { \displaystyle \cos \delta _ { \mathrm { m } } \sin ( \alpha _ { \mathrm { m } } - a ) } & { \displaystyle \cos \delta _ { \mathrm { m } } \sin ( \alpha _ { \mathrm { m } } - a ) } \\ { \displaystyle \sin \delta _ { \mathrm { m } } \cos d - \cos \delta _ { \mathrm { m } } \sin d \cos ( \alpha _ { \mathrm { m } } - a ) } \\ { \displaystyle \sin \delta _ { \mathrm { m } } \sin d + \cos \delta _ { \mathrm { m } } \cos d \cos ( \alpha _ { \mathrm { m } } - a ) } \end{array} \right] } \mathbf { r } _ { \mathrm { m G } } = \mathbf { 0 } ,
$$

where

$$
\begin{array} { l } { { d = - \delta _ { \mathrm { s } } } } \\ { { \phantom { d } } } \\ { { a = \alpha _ { \mathrm { s } } + \pi . } } \end{array}
$$

In the fundamental plane-i.e.,where $z = 0$ —the separation is

$$
m = ( x ^ { 2 } + y ^ { 2 } ) ^ { \frac { 1 } { 2 } } .
$$

Call the vector form m.The hourly variation, $\dot { \mathbf { m } }$ ,is found by numerical differentiation or,if a polynomial representation isused,by differentiating the polynomial.

The Besselian elements fora lunar eclipse are $x , y , { \dot { x } } , { \dot { y } } , m , L _ { 1 } , L _ { 2 } , L _ { 3 } , f _ { 1 } , f _ { 2 } .$ Thereis no widelyacceptedconvention,however,andthe elementsarenot published inTheAstronomical Almanac.

# 11.4.2.2 Contact Times

The contact times can now be found by either of two methods.

One method is to choose a time $T _ { 0 }$ near opposition, with corresponding ${ \bf m } _ { 0 }$ , $\dot { \mathbf { m } } _ { 0 }$ .Fora contact at time $T = T _ { 0 } + t ,$ inwhich $t$ is positive or negative and $L$ is chosen from Eq.11.133,

$$
( \mathbf { m } _ { 0 } + { \dot { \mathbf { m } } } _ { 0 } t ) \cdot ( \mathbf { m } _ { 0 } + { \dot { \mathbf { m } } } _ { 0 } t ) = \mathbf { L } \cdot \mathbf { L } .
$$

Equation11.138 may be solved as a quadratic equation in $t$ ；use the two roots to estimate the two contacts.The two times may then be used to start asecond iteration,and convergence is very rapid.

Alternatively,the following discriminants may be tabulated as a function of time:

$$
\begin{array} { c } { L _ { 1 } - m } \\ { L _ { 2 } - m } \\ { L _ { 3 } - m } \end{array}
$$

fora timespan starting before opposition such that initially $m \approx 1 . 5 L _ { 1 }$ ,and continuing until the first discriminant has passed through zero twice.

No approximations or manipulations are necessary.At each time step,the discriminants areexamined for a change of sign from the preceding step;when a change occurs,find the time of the zero by inverse interpolation.The cases that may occur appear in Table11.2,and must occurin the sequence indicated.

In special cases where examination indicates that one phase might have begun and ended withinasingletabularinterval,subtabulation orthealternative method of polynomialiteration may be necessary.

# 11.4.2.3 Time of Greatest Obscuration

The time of greatest obscuration occurs when the axis of the shadow is closest to the center of theMoon,orwhen $\mathbf { m }$ isaminimum:

$$
{ \frac { d } { d t } } \left( \mathbf { m } \cdot \mathbf { m } \right) = 0 \quad { \mathrm { o r } } \quad \mathbf { m } \cdot { \dot { \mathbf { m } } } = 0 .
$$

The quantity

$$
\mathbf { m } \cdot \dot { \mathbf { m } } = x \dot { x } + y \dot { y }
$$

may also be tabulated as a discriminant and the zero found by inverse interpolation.

Table11.2 Sequences and conditions for contact times   

<table><tr><td>Starta</td><td>Condition</td><td>End</td></tr><tr><td>No eclipse</td><td>L1-m&lt;0</td><td>No eclipse</td></tr><tr><td>Penumbral eclipse begins</td><td>L-m=0</td><td>Penumbral eclipse ends</td></tr><tr><td>Penumbral eclipse</td><td>L1-m&gt;0andL2-m&lt;0</td><td>Penumbral eclipse</td></tr><tr><td>Partial eclipse begins</td><td>L2-m=0andL3-m&lt;0</td><td>Partial eclipse ends</td></tr><tr><td>Partial eclipse</td><td>L-m&lt;0</td><td>Partial eclipse</td></tr><tr><td>Total eclipse begins</td><td>L-m=0</td><td>Total eclipse ends</td></tr><tr><td>Total eclipse</td><td>L-m&gt;0</td><td>Total eclipse</td></tr></table>

äNote:The events in the leftmost column ofthe table occur in sequence from the top down,and in the rightmost columnof the table,from the bottomup.

# 11.4.2.4Magnitude

The magnitudeis the fraction of theMoon'sdiameter covered by shadow,inunitsof the lunar diameter.As published,magnitude corresponds only to the maximum obscuration,but foruse in special calculations,it may be calculated as a function of time for both umbra and penumbra.

The expression is

$$
{ \frac { L _ { i } - m } { 2 s _ { \mathrm { m } } } } , \quad i = 1 , 2
$$

in which $L _ { 1 }$ is used for penumbral magnitude and $L _ { 2 }$ for umbral magnitude.Magnitude may be greater than unity,but not negative.

# 11.4.2.5 Position Angles

The position angle of contact $P$ on the limb of the Moon is the position angle $M$ of $\mathbf { m }$ at the instant of contact,measured eastward (clockwise) from the north;i.e.,

$$
\begin{array} { r l } { \tan { M } = x / y } \\ { P = M } & { \mathrm { f o r ~ i n t e r i o r ~ c o n t a c t s } } \\ { = M + 1 8 0 ^ { \circ } } & { \mathrm { f o r ~ e x t e r i o r ~ c o n t a c t s } . } \end{array}
$$

# 11.4.2.6 Sub-lunar Points

The latitudes $( \phi )$ and longitudes $( \lambda )$ of places that have the Moon in the zenithat given times are given by

$$
\begin{array} { l } { \phi = \delta _ { \mathrm { m } } } \\ { \lambda = \mathrm { G r e e n w i c h \ A p p a r e n t \ S i d e r e a l \ T i m e } - \alpha _ { \mathrm { m } } . } \end{array}
$$

For a given position $( \phi _ { 0 } , \lambda _ { 0 } )$ found from this,the horizon circle is the locus of points on a great circle that satisfy the condition:

$$
\tan \phi = - \cot \phi _ { 0 } \cos ( \lambda _ { 0 } - \lambda ) .
$$

Values of $\lambda$ maybe assumed and coordinate pairs calculated.The hemisphere defined bythis central point and horizon circle is where the Moon is above the horizon at the instant.

# 11.5 Eclipses Online

Eclipses Online,found at URL[2],is a canon of solar and lunar eclipse information for phenomena in the period A.D.1501 to A.D. 21oo. Currently,it provides information on a total of 2881 eclipses composed of 1421 solar eclipses and 1460 lunar eclipses.

It was originally designed to provide both local and general circumstances for solar eclipses and general circumstances for lunar eclipses.These web pages can be seen as a partial replacement for the eclipse information formerly provided in the circulars produced bythe U.S.Naval Observatory(see $: \ S \ 1 1 . 1 . 1 . 3 $ .Havingselectedaparticular year,the eclipses occurring during that yearare listed.This in turn provides the necessary links to the individual eclipse pages themselves.The software underpinning the general information on the site is that used in The AstronomicalAlmanac.Consequently,predictions make useof the fractional radius of the Moon, $k$ ,adoptedby the IAUalthough values ofquantitiessuch as $\Delta T$ may be different than those used in The Astronomical Almanac for the appropriate year.

# 11.5.1 Solar Eclipses

Typical solar eclipse information starts with a global view of the eclipse showing an orthographic projection of the eclipse“footprint”and,where appropriate,the areas of the globe from which partial,annular or total eclipses can be seen denoted by different types of shading.Light shading indicates which parts of the eclipse footprint take place at sunrise and sunset and medium shading denotes the parts of the footprint where the whole eclipse can beviewed.The darkest shading indicates thepath of totality,annularity ora combination of both for total,annular and hybrid eclipses,respectively.

A number ofcurves are plotted on the diagram indicating the northern and southern limits of the penumbral shadow where appropriate,the start and end of the eclipse at both sunrise and sunset and maximum eclipse at sunrise and sunset.Where appropriate,the northern and southern limits of totality or annularity are also given.Forall eclipses,the point at which the shadow first contacts the Earth's surfaceis denoted by $\left( \oplus \right)$ and similarlywhere the shadow leaves the Earth's surface by $( \odot )$ .In the case of a partial eclipse,the point of greatest eclipse isdenoted by $( \otimes )$ .

The title of the diagram includes the type of eclipse,its place in the sequence of eclipses of the year and the Greenwich calendar date of the eclipse.At the foot of the diagram,the adopted $\Delta T$ value is given as well as the point on the Earth's surface at which the projection iscentered.

Asummaryof thegeneral circumstancesisgiven belowtheplot.This includes the time andlocation ofthe firstand lastcontact of the shadow with the Earth's surface,greatest eclipse inthecase of apartialeclipse including the maximum magnitude of the eclipse,the beginning andend of the northern and southern penumbral limits where appropriate,the beginning and end of the northern and southern umbral limits and the central line limits where appropriate in the case of annular, total and hybrid eclipses,and also central eclipse atlocal noon. The symbols described above arerepeated with this information.An example of a solar eclipse diagram for the 2017 August 21 total eclipse of the Sun can be found in Fig.11.17.

Ananimation of theeclipse is provided using software developed byDr.Andrew Sinclair, aformer head of HMNautical Almanac Office.This combines the umbral and penumbral shadows of the eclipse and the motion of the day/night terminator depicted at five-minute intervals.Italso shows theGreenwich date of the start of the eclipse,the current UTtime and the duration of annularity or totality appropriate to the eclipse being displayed.

![](images/6b522bd183790e948ff6693b64ed9f9fd236a688ad9fae975d89f93d0ac7546e.jpg)  
Figure11.17 Example of solar eclipse diagrams found on Eclipses Online site.

Local circumstances are provided based on a gazetteer of some 15oo locations around the world made up of major population centers,capitals of countries and a number of placesproviding a good distribution of locationsaround theworld.Thoselocations falling inthe footprint of the eclipse are listed.The exceptions are those locations within the region delimited by the“maximum eclipse at sunrise"curve and“eclipse ends at sunrise"curve,and its counterpart,the region delimited by the“maximum eclipse at sunset”curve and “eclipse begins at sunset”curve.These exceptionswill be removed ina future revision of the site.

The table of locations lying within the footprint meeting the condition mentioned previously provides access to both a local circumstances diagram and an animation of the eclipse asseen from thatlocation.Those locations inthe path ofannularity or totality are highlighted. Each location also provides a link to the eclipse history of that location between A.D.1501 and A.D.2100.

The local circumstances plot shows the orientation of the Sun and Moon (denoted by a dashed circular outline)at first and last contact with either(1) in the outline to denote first contact or (4) to denote last contact.The Sun is shown as it appears at maximum eclipse. Thismay beayellow,partially-obscured Sundenoting themaximumpartial eclipse,ablack disk surrounded by a white serrated edge denoting a total eclipse or a black circle with a yellowring around it denoting an annular eclipse.The titleof the plot includes thelocation and country forwhich thediagram has beenconstructed,thelatitude and longitudeof the location,the Greenwich date and the maximum obscuration of the eclipse expressed asa percentage.The times of the principal phases of the eclipse from the selected location are given below theplot in UT.

The animation itself is an animated Graphics Interchange Format (GIF) file showing the progress of the eclipse.TheMoon is displayed asa dashed circular outline and the Sun as ayellow disk.The relative orientation of the Sun andMoon is displayed at one-minute intervals during the partial phase of the eclipse dropping to ten-second intervals for totality or annularity as appropriate.The eclipsed part of the Sun is shown asa black area.Totality is denoted in the same manner as the local circumstance plot.The title of the animation includes the chosen location and country and the current Greenwich date.The lower part of the animation shows the current azimuth,altitude and obscuration of the Sun,the UT time and the status of the eclipse.The horizon is also depicted as a brown region when the eclipse occurs at around sunrise or sunset.

Atthe foot of the page is the eclipse listing for the year and,ina handful of cases, additional information connected with the eclipse is give such as historical information or some significant event connected with the eclipse.

# 11.5.2 Lunar Eclipses

In the case of lunar eclipses,the eclipse information is provided in the same wayas it is in The Astronomical Almanac since the 2oo5 edition.A fulldescription of the plot canbe found belowandanexampleofalunareclipse diagramfor2O14April15canbefoundinFig.11.18.

Information on lunar eclipses is presented in the form of a diagram consisting of two parts. The upper panel shows the path of the Moon relative to the penumbral and umbral shadows of the Earth.The lower panel shows the visibility of the eclipse from the surface of the Earth. The title of the upper panelincludes the type of eclipse,its place in the sequence ofeclipses of the yearand the Greenwich calendar date of the eclipse.The innerdarker circle is the umbral shadow ofthe Earthandthe outerlighter circle is that of the penumbra.The axis ofthe shadow oftheEarthisdenoted by $( + )$ withthe eclipse shown for reference purposes.A3O-arcminute scale bar is provided on the right-hand side of the diagram and the orientation is given by thecardinal points displayed on the small graphic on the left-hand side of the diagram.The position angle (PA),printed for the first and fourth umbral contacts,is measured from the North point of the lunar disk through East along the limb of the Moon to the point of contact. For convenience,the general direction of this measurement is shown on the graphic by the use of an arc extending anti-clockwise (eastwards) from North terminated with an arrow head.

![](images/0a3dcebe18b8125cf8f489b8fb50287ebc288d2cba76f3eca444ff92f2b88e8e.jpg)  
Figure11.18 Example of lunar eclipse diagrams found on Eclipses Online site.

Moonsymbols are plotted at the principal phases ofthe eclipse to show its position relative to the umbral and penumbral shadows.The UT times of the different phases of the eclipse to the nearest tenth of aminute are printed above or below the Moonsymbolsas appropriate. Pl and P4are the first and last external contacts of the penumbra,respectively,and denote the beginningand end of the penumbral eclipse,respectively.U1 and U4 are the first and last external contacts of the umbra denoting the beginning and end of the partial eclipse, respectively.U2andU3are the first and last internal contactsof theumbraand denote the beginning and end of the total phase,respectively.MID is the middle of the eclipse.The positionangleisgiven forP1andP4 forpenumbral eclipsesandU1andU4 forpartial and total eclipses.The UT time of the geocentric opposition in right ascension of the Sun andMoon and the magnitude of the eclipseare given above or below the Moon symbolsas appropriate.

The lower panel isacylindrical equidistant map projection showing the Earth centered on the longitude at which the Moon is in the zenith at the middle of the eclipse.The visibility of the eclipse is displayed byploting the Moon rise/setterminator for the principal phases of the eclipse for which timing information is provided in the upper panel of the diagram.The terminator for the middle of the eclipse is not plotted for the sake of clarity.

Theunshaded area indicates the region of the Earth from which all of the eclipse is visible,whereas the darkest shading indicates thearea from which the eclipse is invisible. The different shades of gray indicate regions where the Moonis either rising or seting during the principal phases of the eclipse.TheMoon is rising on the left hand side of the diagram after the eclipse has started,and is setting on the right-hand side of the diagram before the eclipseends.Labelsare provided to thiseffect.

Symbols are plotted showing the locations for which theMoon isin the zenithat the principal phases of the eclipse.The points at which the Moon is in the zenith atP1 and P4 are denoted by $( + )$ ,atU1andU4 by $( \odot )$ ,andatU2andU3by $( \oplus )$ .These symbols are also plotted on the upper panel where appropriate.The value of $\Delta T$ used for the calculation of theeclipse circumstances is given below the diagram.Country boundaries are also provided to assist the user in determining the visibility of the eclipse at a particular location.

# 11.6 Transits

General information about transits of Mercury and Venuscan be found in Meeus (1989). Information concerning specific transits of Mercury and Venus is tabulated in The Astronomical Almanac.This information consists of the geocentric phases of the transit,a world map (Mercator projection) which indicates the beginning and ending curves of the transit from whichausercan determine the regions of visibility,and atable of local circumstances for locations worldwide.All circumstancesare provided in Universal Time (UT) withaprovisional value of $\Delta T$ .If,closerto the time of the transit,abettervalue of $\Delta T$ is obtained, the data may be corrected using the new value.

Table11.3Transits of Mercury for112 years   

<table><tr><td>TransitMonth</td><td>33-year cycle</td><td>13-year cycle</td></tr><tr><td>November</td><td>1907-1940-1973-2006</td><td>1914-1927-1940-1953</td></tr><tr><td></td><td>1927-1960-1993</td><td>1960-1973-1986-1999</td></tr><tr><td></td><td>1953-1986-2019</td><td>1993-2006-2019</td></tr><tr><td>May</td><td>1924-1957</td><td>1924-1937</td></tr><tr><td></td><td>1937-1970-2003</td><td>1957-1970</td></tr><tr><td></td><td></td><td>2003-2016</td></tr></table>

Before computation of the general circumstances of the transit is performed,the exact time of conjunction in right ascension between the Sun and the transiting planet is determined.An approximate time for the middle of the transit,determined beforehand,servesas the center point for a ten-hour span of time over which the apparent places of the Sun and the transiting planet are determined (see $\ S 7 . 4 . 1$ ).Using the DE405/LE405 ephemeris (see Chapter 8) and theNOVAS software (URL[4]),differences in apparent right ascension between the transiting planet and the Sun are determined at consecutive 15-minute intervals.Once a minimum is reached,a precise time of conjunction is found usinga Lagrangian inverse interpolation scheme during the 15-minute interval in which the conjunction occurs.

After the time of conjunction has been determined,the geocentric phases are computed. Starting at the beginning of the ten-hour ephemeris span,a search is made at one minute intervals for four contact points: ingress,exterior contact;ingress,interior contact;egress, interior contact；and egress,exterior contact.The four contact points are illustrated in Fig.11.19.The transit ends at the time of thelast contact.

At the times of first and fourth contact points,the apparent separation between the center of the Sun and the center of the transiting planet is equal to the sum of their semidiameters; that is,when

$$
\sigma = s _ { s } + s _ { p }
$$

where $s _ { p }$ is the apparent semidiameter of the transiting planet, $s _ { s }$ is the apparent semidiameter of the Sun,and $\sigma$ is the apparent angular separation between the centers of the two.At the times of second and third contact points,the apparent separation between the center of the two bodies is equal to the difference of their semidiameters;thatis,when

$$
\boldsymbol { \sigma } = \boldsymbol { s } _ { s } - \boldsymbol { s } _ { p } .
$$

For each one-minute interval the apparent places,semidiameters,apparent separation between centers,and the time rate of change of the separation for the Sun and the planet are computed.The apparent separation between the two bodies and the sum of the semidiameters arecomputed,and thenevaluated against the criterionofEq.11.146.When the testindicates that the first contact point has been reached,aLagrangian interpolation scheme is employed to determine the first contact time precisely.From this point on,the computation of apparent places,semidiameters,apparent separation between centers,and the time rate of change of theseparation for the two bodiescontinues,but now thecriterionofEq.11.147isused.When the test indicates that the second contact point has been reached,the Lagrangian interpolation scheme is again employed to determine the second contact time precisely. Contact points three and four are found in a similar manner.Associated with each contact point is a position angle $( P )$ ,measured from the apparent north pole of the Sun towards the east to the contact point;see Fig.11.19.

![](images/f2e6be71bb2e56748e0a63e8eb55d31bbe4c61b01d80b924001c16833a16323c.jpg)  
Figure11.19 Example showing the four contact pointsand least angular distance foratransit across theSun's disk.Contact point1is ingress,exteriorcontact; contact point2is ingress,interiorcontact;contact point 3is egress,interior contact;and contact point 4 is egress,exterior contact. The position angle for contact point 2 is alsoillustrated.

The time of least angular distance lies between the second and third contact times.After the second contact time has been determined,the apparent distance between the center of the Sun and the center of the transiting planet is tested to determine the minimum value. The checks continue until the minimum value is reached.At that point,the same Lagrangian interpolation scheme employed to determine the contact times is used to determine the time of the least angular distance; the value of the least angular distance is also computed.

The transit diagram printed in The Astronomical Almanac is a Mercator projection map of the Earth with two curvesplotted.The curve labeled“Transit beginsat Sunrise/Sunset” is the great circle having for its pole the sub-planet point for the transiting planet at the time of exterior ingress.(The sub-planet point being the point on Earth where the planet is at the zenith).Similarly,thecurve labeled“Transit endsat Sunrise/Sunset”is the great circlewith its pole at the sub-planet point at the time of exterior egress.These two sub-planet points are determined via the technique shown in Eq.11.144,but substituting the $\alpha$ ， $\delta$ of the planet instead of the Moon.Pointson the great circle are found using Eq.11.145 and plotted. Other labelson the diagramindicatewhere the entire transit is visibleaswellaswhere the transit is in progress at sunrise or sunset.

The table of local (topocentric) circumstances for locations across the Earth is assembled byusing an extensive list of geographic locations.

Foreach location,the process of finding the four contact points and computing the associated data is performed as described above,except that instead of apparent (geocentric) places of the Sun and planet, topocentric places are used (see $\ S \ 7 . 4 . 3$ ).Thetablepublished in TheAstronomical Almanac presents selected locationswhere at least two of the five phases (i.e.,four contact pointsand the least angular distance) are above the horizon.Due tospaceconsiderations,onlya limited numberof locationscan bepresented in thebook. Beginning with the 2O12 transit of Venus,The Astronomical Almanac Online will present a more complete table of locations.

# Acknowledgements

Acknowledgements are due to Mark Stollberg (U.S.Naval Observatory),who wrote $\ S \ 1 1 . 6$ Transits.

# REFERENCES

1.The Astronomical Almanac Online: http://asa.usno.navy.mil or http://asa.hmnao.com.   
2.Eclipses Online: http://astro.ukho.gov.uk/eclipse/.   
3.NASA EclipseWebsite: http://eclipse.gsfc.nasa.gov/.   
4.Naval Observatory Vector Astrometry Software(NOVAS): http://a.usno.navy.mil/software/novas/novas_info.php.   
Chauvenet,W.(1891,Reprint1960).AManualofsphericalandpractical astronomy-Vol.1:Spherical astronomy (revisedandcorr.,5thed.).NewYork:DoverPublication.   
Herald,D.(1983).Correcting Predictions of Solar EclipseContact Timesfor the Effects ofLunarLimb Iregularities.JournaloftheBritishAstronomicalAssociation93,241-246.   
Meeus,J.(1989).Transits.Richmond,Va.:Willmann-Bell.   
Mikhailov,A.(1931). Uber die Berechnung der Breite der Totalitatszone bei Sonnenfinsternissen. AstronomischesNachrichten243,51.   
Nautical Almanac OfficesofUKand USA(1961).Explanatory Supplement toThe Astronomical EphemerisandTheAmerican Ephemeris and Nautical Almanac.London:HerMajesty'sStationery Office.Reprinted 1974.

# FURTHER READING

Green,R.(1985).Spherical Astronomy.Cambridge:Cambridge University Press.   
Link,F.(1969).EclipsePhenomenainAstronomy.New York:Springer-Verlag.   
Liu,B.-L.(1983).Canon ofLunar Eclipses from 1000 B.C.toA.D.3000.Publicationsof thePurple Mountain Observatory 2,1.   
Meeus,J.,C.Grosjean,and W.Vanderleen(1966).Canonof Solar Eclipses.Oxford: Pergamon Press.   
Meeus,J.andH.Mucke(1983).Canon of Lunar Eclipses,-2002 to2526(2nd ed.).Vienna: Astronomical Office.   
Mitchell,S.A.(1951).Eclipsesof theSun (5thed.).New York:Columbia UniversityPress.   
Mucke,H.andJ.Meeus(1983).CanonofSolarEclipses-2003to $+ 2 5 2 6$ .Vienna:Astronomical Office.   
Murray,C.A.(1985).Vectorial Astrometry(5th ed.).Bristol: Hilger.   
Newcomb,S.(1882).Discussionand results of observations on transits of Mercury,from 1677 to 1881.InAstronomicalPapersoftheAmericanEphemerisandNautical Almanac,VolumeI,part VI.Washington,DC:U.S.Government Printing Office.   
Oppolzer,T.R.v.(1887).CanonderFinsternisse.ViennaandNew York: ImperialAcademy ofScience and Dover Publications.Reprinted 1962 w/English translation.   
Smart,W.M.(1977).Text-book inSpherical Astronomy (6thed.).Cambridge:Cambridge University Press.   
Willams,W.J.(1971).Prediction and analysis of solar eclipse circumstances.Technical ReportNTIS No.AD726626,National Technical Information Service,Springfield,Virginia.

# Astronomical Phenomena

B.D.YALLOP,C.Y.HOHENKERK,& S.A.BELL

# 12.1 General Aspects of the Night Sky

The configurationsand phenomena of the Sun,Moon,and planetsas seen from the Earth arise from their apparent movement in the sky.Most of the phenomena published in the“Diary of Phenomena”for example,are geocentric; the remainder are heliocentric.

The Earth rotates about its polar axis once a day and produces an apparent motion of the night sky about thecelestial poles.In theNorthern Hemisphere the north celestial pole is elevated above the horizon.Facing away from the elevated celestial pole,an observer sees the Sun,Moon,planets,and stars risein the east and set in the west.They reach their highest altitudeas theycross the local meridian.When the observer turns to face the elevated celestial pole,stars nearest the pole neither rise nor set.They become circumpolar and cross the meridian each day once above the pole at their highest altitude and once below the pole at their lowest altitude.In the Northern Hemisphere,circumpolar stars appear to rotate about the north celestial pole anticlockwise.In the Southern Hemisphere the effect is reversed and theyappear torotate clockwise.

Superimposed on the diurnal rotation is an annual rotation caused by the Earth's orbiting the Sun.Since the stars are seen by the naked eye after sunset,the constellations appear to move from east to west,and to return to the same position after a year.Relative to the Sun, the stars riseand set roughly four minutes earliereach day.Inthe course ofamonth,the night sky appears to move two hours in right ascension to the west.Also because of this orbital motion of the Earth,the circumpolar stars in the Northern Hemisphere appear to rotate once a yearinan anticlockwise direction around the north celestial pole and inaclockwise direction about the south celestial pole.

TheMoon moves in an orbit inclined to the ecliptic by $5 \% 1 6$ ；theMoon makesone revolution about the sky from west to east in about a month.During this period the phases of the Moon complete acycle from new to full and back to new.The orbit of the Moon is moving around the ecliptic,so that other aspects of the Moon’s position in the sky,such as itsmaximum and minimum declination,change from one month to the next.

It is important to know when the planets are in the most favourable position for observation.The outer planets,for example,are best seen around opposition.They are in their most unfavourable position around conjunction.The inner planetsare different—they are in their most favourable position near greatest elongation,even though they are not at full phase.At superior conjunction the phase isaround full,but the planets are difficult to see because they are furthest from the Earth and usually too close to the Sun.At inferior conjunction the inner planetsare nearest to the Earth,butagain they are difficult to see because their phase is small, and they are too close to the Sun as viewed from Earth.

Often the times of phenomena need not have any great precision; sometimes the nearest hour or even the nearest day are sufficient for observational purposes.The dates and times, however,usually depend on the coordinate system.For historical reasons the conjunctions and oppositions of planets have been calculated in geocentric ecliptic coordinates,e.g.,time of conjunction is when the ecliptic longitudes are equal.On the other hand,the conjunctions of planets with other planets,bright stars,or the Moon have always been calculated using equatorial coordinates;the phenomena are then observed more easilywith an equatorially mounted telescope.In some cases the times of phenomena have been defined as the maxima or minima of the distances from the Sun or the Earth or the elongation from anotherbody.In such cases,the phenomena are independent of the coordinate system.

# 12.2 Configurations of the Sun, Moon,and Planets

The Universal Times (UT) of the principal astronomical phenomena involving configurations ofthe Sun,Moon,and planetsare givenin TheAstronomical Almanac pp.A1-A11 under the heading“Phenomena".These data are also available for planning purposes in Astronomical Phenomena,published upto two years inadvance of TheAstronomical Almanac.In most cases the times are given to the nearest hour,but for certain heliocentric phenomena of the planets,only the date appears.The times of the phenomena of greatest general interest—the beginning of the seasonsand the phasesof the Moon—are to the nearest minute,although the accuracy is of no significance.

Times may be calculated usinga daily tabular ephemeris.For quantities that vary slowly with time,such as planetary apsides,a tabular interval of five days gives better results.On theother hand,quantities suchas the phases of the Moon vary rapidly,and a shorter interval ofahalf or quarterday is more appropriate.Ifthe ephemeris is in Terrestrial Time(TT),then, to convert to UT,subtract the correction $\Delta T = \mathrm { T T } - \mathrm { U T }$ to the time obtained at the end of the calculation.

The time $t$ of the phenomenon derives from a functional expression involving the parametersassociated with the phenomenon.The time of the phenomenon is calculated from the equation $f ( t ) = 0$ or $f ^ { \prime } ( t ) = 0$ ,where $f ^ { \prime } ( t ) = d f ( t ) / d t$ .

# 12.2.1 Interesting Phenomena of the Sun,Earth,and Moon

# 12.2.1.1 Equinoxes and Solstices

The times of the equinoxesand solstices are defined to be when the Sun's apparent ecliptic longitude $\lambda _ { S }$ is a multiple of $9 0 ^ { \circ }$ ；i.e.,it iscalculatedfrom $f ( t ) = 0$ ,where $f ( t ) = \lambda _ { S } - 0 ^ { \circ }$ , $9 0 ^ { \circ }$ , $1 8 0 ^ { \circ }$ ,or $2 7 0 ^ { \circ }$ .Thus in the northern hemisphere,for the spring equinox $f ( t ) = \lambda _ { S }$ ,for the summer solstice $f ( t ) = \lambda _ { S } - 9 0 ^ { \circ }$ ,for the autumn equinox $f ( t ) = \lambda _ { S } - 1 8 0 ^ { \circ }$ and for the winter solstice $f ( t ) = \lambda _ { S } - 2 7 0 ^ { \circ }$ .Atthe equinoxes the Sun crosses the equator.At that time thelengths of the day and night are approximately equal everywhere,however the length of the day exceeds the length of the night slightlydue to refraction,semidiameter,and parallax of the Sun.

Table 12.1 Time of commencement of the seasons during the 21st century. Note:The total range in timesisabout54 hours ineach case.   

<table><tr><td></td><td></td><td>Spring</td><td>Summer</td><td>Autumn</td><td>Winter</td></tr><tr><td></td><td></td><td>d h</td><td>dh</td><td>d h</td><td>d h</td></tr><tr><td>Latest</td><td>2003</td><td>March 2101</td><td>June 21 19</td><td>Sept.2311</td><td>Dec.22 07</td></tr><tr><td>Earliest</td><td>2096</td><td>1914</td><td>2007</td><td>2123</td><td>2021</td></tr></table>

The time of the commencement of the seasons changes progressively during the leapyear cycle.Because the period of revolution of the Earth about the Sun is not commensurate with the Gregorian calendar year,it is only after acomplete cycle offour centuries that the seasons again commence at approximately the same times.In the present century the latest dates for the seasons occurred in 20o3,and the earliest willbe in 2096 (see Table 12.1).

# 12.2.1.2 Perihelion and Aphelion of the Earth

In the “Diary of Phenomena,”the times when the Earth is at perihelion (the Sun isat perigee) are defined to be those for which the Sun's geometric distance $R$ is a minimum. Likewise, the times when the Earth is at aphelion (the Sun isat apogee) are defined to be when $R$ is amaximum.Thus,if $t$ is the time of perihelion,itis calculated from the equation $f ^ { \prime } ( t ) = 0$ where $f ( t ) = R$ .The times do not always agree with those calculated from the times when the Sunisat perigee or apogee in its mean elliptical orbit (i.e.,the time $t$ when the mean longitude of perigee $\Gamma = 0$ ,orapogee $\Gamma - 1 8 0 ^ { \circ } = 0$ )because of perturbations by the planets.

Itis worth noting that the times of Earth at perihelion and aphelion vary in date more than other annually-occuring phenomena such as the start of the seasons.Thisis due to the presence of the Moon.Because perihelion and aphelion are defined by the distance between the center of the Sun and the center of the Earth,the Earth's position in its monthly motion around theEarth-Moon barycenter greatly affects the time of perihelionand aphelion.Due to the fact that the position of the Moon doesn't repeat from year to year on the same date,neither does the position of the Earth with respect to the Earth-Moon barycenter.This produces what appears to be a quasi-random variation in the dates of perihelion and aphelion.In the 21st century,time of the earliest perihelion is January2at $1 ^ { \mathrm { h } }$ (2005）and the latest is January 5at $2 2 ^ { \mathrm { h } }$ (2096).Earliest and latest aphelion are July 3at $1 6 ^ { \mathrm { h } }$ (2044)and July 7 at $1 5 ^ { \mathrm { h } }$ (2083).Timesare TT,butat thisprecision the difference between TT and UT is negligible.

# 12.2.1.3 Phases of the Moon

Thetimes of thephases of the Moonare tabulated to the nearest minute of UT in The Astronomical Almanac pp.Aland D1 and are given to the nearest hourof UT in the“Diary” on pp.A9-A11.They are the times when the excess of the Moon's apparent geocentric ecliptic longitude $\lambda _ { M }$ over the Sun'sapparent geocentric ecliptic longitude is $0 ^ { \circ }$ , $9 0 ^ { \circ }$ , $1 8 0 ^ { \circ }$ ,or $2 7 0 ^ { \circ }$ i.e.,the times when $f ( t ) = 0$ where $f ( t ) = \lambda _ { M } - \lambda _ { S }$ for new Moon, $f ( t ) = \lambda _ { M } - \lambda _ { S } - 9 0 ^ { \circ }$ for first quarter, $f ( t ) = \lambda _ { M } - \lambda _ { S } - 1 8 0 ^ { \circ }$ for full Moon and $f ( t ) = \lambda _ { M } - \lambda _ { S } - 2 7 0 ^ { \circ }$ forlast quarter. Because the times are determined from geocentric coordinates,they are independent oflocation on theEarth.

Owing to the rapid variations in the distance and velocity of the Moon,the intervals between successive phases are not constant,and it is not possible to check these times bydifferencing.Moreover,there is no simple prediction formula with which to make a comparison.Examination of the higher differences of the successive times of the same phenomenon providesa check.

The phases of the Moon do not recur on exactly the same dates in any regular cycle,but theapproximate dates of the phases in any year can be found from the dates on which the phase occurred19 yearspreviously.Thus in the Metonic cycle,inwhich19 tropical years are nearly equal to 235 synodic months (new moon to new moon),the phases recur on dates that are the same or differ by one or occasionally two days,depending on the number of intervening leap years and on the perturbations of the Moon.For example,during 2O0o the dates are the same as in 198l on thirty occasions,and differ by one day for the remaining nineteen.

Another relevant cycleis the Saros,which consists of 233 synodic monthsand equals nearly19 passages of the Sun through the node of the Moon’s orbit;not only will the moon phases recur but eclipses as well.Moreover in this cycle the Moon’s apse makes 239 revolutions and returns to nearly the same position,so the durations of solar eclipses are similar aswell.

# 12.2.2 Geocentric Phenomena

The times of geocentric phenomena are calculated from the expressions for $f ( t )$ listed below. Table12.2contains the phenomena for which the time is obtained from the equation $f ( t ) = 0$ Table 12.3contains phenomena for which the time is obtained from the equation $f ^ { \prime } ( t ) = 0 .$ In thistable,except for the stationary points in right ascension,the phenomenaare independent of the coordinate system.

The notation $\lambda$ , $\alpha$ ,δ refers to the apparent geocentric ecliptic longitude,right ascension, and declination;and the subscripts $s$ , $M$ , $p , b$ refer to the Sun,Moon,planet,or bright star, respectively.The distances $r$ , $R$ , $\Delta$ ,and $\rho$ refer to the geometric distances of the Sun-planet, Earth-Sun,Earth-planet,and Earth-Moon,respectively; $\pi$ is the horizontal parallax of the Moon and $s$ is the semidiameterof the planetat1au.The five bright stars used in the“Diary” areAldebaran,Pollux,Regulus,Spica,andAntares.Itshouldbe notedthat,atcurrent epochs, planetary and lunar occultations of Pollux are not possible.

The following formulae are useful for calculating elongation and longitude:

$$
\begin{array} { l } { \cos E = \sin \delta _ { p } \sin \delta _ { s } + \cos \delta _ { p } \cos \delta _ { s } \cos ( \alpha _ { p } - \alpha _ { s } ) } \\ { \tan \lambda = \displaystyle { \frac { \sin \epsilon \sin \delta + \cos \epsilon \cos \delta \sin \alpha } { \cos \delta \cos \alpha } } } \end{array}
$$

where $\epsilon$ is the true obliquity of the ecliptic.

# 12.2.2.1Visibility of Planets

Table12.4 shows thecriteria adopted for the“Diary”for the minimum elongations from the Sun at which Mercury,the bodies used in navigation,and the minor planets can be seen with the naked eye.

Table 12.2 Geocentric phenomena for which $f ( t ) = 0$   

<table><tr><td>Phenomenon</td><td>f(t)</td><td>Remarks</td></tr><tr><td colspan="3">Seasons:</td></tr><tr><td>Vernal Equinox</td><td>λs</td><td>March equinox,FirstPoint ofAries</td></tr><tr><td>Summer Solstice</td><td>s-90°</td><td>June solstice</td></tr><tr><td>Autumnal Equinox</td><td>λs-180°</td><td>September equinox</td></tr><tr><td>Winter Solstice</td><td>s-270°</td><td>December solstice</td></tr><tr><td colspan="3">Conjunctions of the planets with the Sun:</td></tr><tr><td colspan="3">Inferior planets:</td></tr><tr><td>inferior conjunction</td><td>λp-λs</td><td>λp-λs changes from plus to minus</td></tr><tr><td>superiorconjunction</td><td>λp-λs</td><td>λp-λs changes from minus to plus</td></tr><tr><td colspan="3">Superior planets:</td></tr><tr><td>conjunction</td><td>λp-λs</td><td></td></tr><tr><td>opposition</td><td>λp-λs-180°</td><td></td></tr><tr><td colspan="3">Phases of the Moon:</td></tr><tr><td>New Moon</td><td>λM-λs</td><td></td></tr><tr><td>First Quarter</td><td>λM-λs-90°</td><td></td></tr><tr><td>FullMoon</td><td>λM-λs-180°</td><td></td></tr><tr><td>Last Quarter</td><td>λM-λs-270°</td><td></td></tr><tr><td colspan="3">Conjunctions of other bodies:</td></tr><tr><td>planet with planet</td><td>ap-ap2</td><td>separation=δp-δp2</td></tr><tr><td>planetwith brightstar</td><td>ap-αb</td><td>separation=δp-δb</td></tr><tr><td>Moon with planet</td><td>αM-αp</td><td>separation=δM-δp</td></tr><tr><td>Moonwith bright star</td><td>αM-αb</td><td>separation=δM-δb</td></tr></table>

# 12.2.2.2 Synodic Periods

Once the date and time of a geocentric phenomenon are known,the approximate time of the next similar phenomenon may be estimated by adding the synodic period $T$ of the body concerned.The eccentricities of the orbits of the Earth and the body,and the perturbations byother bodies,will introduce errors in this estimate.Table12.5 gives synodic periods of theplanets,Pluto,Ceresand the three brightest minorplanets.The periodsmay beused for a systematic search for geocentric phenomena.

The synodic period $T$ is calculated from the mean motion of the planet, $n _ { \mathrm { p } }$ ,and the mean motion of the Earth, $n _ { \mathrm { e } }$ Thus,

$$
T = \frac { 3 6 0 ^ { \circ } } { n _ { p } - n _ { e } } \mathrm { ~ f o r ~ i n n e r ~ p l a n e t s , } \quad \mathrm { a n d } \quad T = \frac { 3 6 0 ^ { \circ } } { n _ { e } - n _ { p } } \mathrm { ~ f o r ~ o u t e r ~ p l a n e t s . }
$$

For the slowly moving objects,the error in using these values is small,but for Mercury, Venus,and Mars,the mean synodic period is less useful.Much more accurate estimates of

Table 12.3 Geocentric phenomena for which $f ^ { \prime } ( t ) = 0$   

<table><tr><td>Body</td><td>Phenomenon</td><td>f(t)</td><td>Remarks</td></tr><tr><td>Mercury</td><td>Greatest elongation</td><td>E</td><td>-28≤E≤+28°</td></tr><tr><td>Venus</td><td></td><td>(r+△+R)(r+△-R)</td><td>-47°≤E≤+47°</td></tr><tr><td>Venus</td><td>Greatest brilliancy</td><td>(r△)</td><td>0.39au&lt;△&lt;0.47au</td></tr><tr><td>Venus</td><td>Greatest illuminated extent</td><td>πs²(r+△+R)(r+△-R) 4r△3</td><td>whereπ=3.14159...</td></tr><tr><td>Earth</td><td>Apsides</td><td>r=R</td><td>Atperihelionrisaminimum</td></tr><tr><td>Moon</td><td>Apsides</td><td>p=1/sinπ</td><td>Ataphelionrisamaximum Atperigeeρisaminimum</td></tr><tr><td></td><td></td><td>π</td><td>Atapogeeρisamaximum Atperigeeπisamaximum</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Atapogeeπisaminimum</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Mars</td><td>Closest approach</td><td>△</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Planet</td><td>Stationary in</td><td></td><td></td></tr><tr><td></td><td>right ascension</td><td>αp</td><td></td></tr></table>

Table12.4 Visibility criteria for geocentric phenomena   

<table><tr><td>Body</td><td>Minimum Elongation</td></tr><tr><td>Moon,Mars,Saturn</td><td>15°</td></tr><tr><td>Minor planets</td><td>15°</td></tr><tr><td>Venus, Jupiter</td><td>10°</td></tr><tr><td>Mercury</td><td>10°+visual magnitude of Mercury</td></tr></table>

Table 12.5 Synodic periods of selected solar system objects   

<table><tr><td>Object</td><td>Days</td><td>Object</td><td>Days</td><td>Object</td><td>Days</td></tr><tr><td>Mercury</td><td>116</td><td>Saturn</td><td>378</td><td>Ceres</td><td>467</td></tr><tr><td>Venus</td><td>584</td><td>Uranus</td><td>370</td><td>Pallas</td><td>466</td></tr><tr><td>Mars</td><td>780</td><td>Neptune</td><td>367</td><td>Juno</td><td>474</td></tr><tr><td>Jupiter</td><td>399</td><td>Pluto</td><td>367</td><td>Vesta</td><td>504</td></tr></table>

when these planets may be seen again in the same part of the sky may be made by using longperiodcycles that contain,with varying degrees of accuracy,integral numbers ofrevolutions of the Earth and the planet.(See Table 12.6.)

Any particular phenomenon of a planet repeats itself after each cycle at the same time of year and in the same part of the sky.However,repetition does not occur aftera single synodic period.For Venus auseful and accurate form of the relation is

$$
5 \ { \mathrm { m e a n ~ s y n o d i c ~ p e r i o d s } } = 8 \ { \mathrm { c a l e n d a r ~ y e a r s } } - 2 . 4
$$

unless the interval includes acentury year that is nota leap year.

Table 12.6 Long-period cycles of Mercury,Venus,and Mars   

<table><tr><td>ForMercury</td><td>54 sidereal periods= 13years+ 2days 137 sidereal periods= 33 years- 1day</td></tr><tr><td>ForVenus</td><td>13 sidereal periods=8years- 1day</td></tr><tr><td></td><td>359 sidereal periods=243 years- day</td></tr><tr><td>ForMars</td><td>8 sidereal periods= 15 years+17days</td></tr><tr><td></td><td>17 sidereal periods= 32 years- 9 days</td></tr><tr><td></td><td>25 sidereal periods= 47 years+ 8days</td></tr><tr><td></td><td>42 sidereal periods= 79 years- 1day</td></tr></table>

Table 12.7 Heliocentric phenomena   

<table><tr><td>Phenomenon</td><td>f(t)</td><td>Type</td><td>Remarks</td></tr><tr><td>Nodes</td><td>b</td><td>f(t)=0</td><td>At the descending node,b is decreasing. At theascending node,b is increasing.</td></tr><tr><td>Apsides</td><td>r</td><td>f&#x27;(t)=0</td><td>At aphelion,risamaximum.</td></tr><tr><td></td><td></td><td></td><td>Atperihelion,risaminimum.</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Greatest latitudes</td><td>b</td><td>f&#x27;(t)=0</td><td>At greatestlatitudeNorth,bispositive.</td></tr><tr><td></td><td></td><td></td><td>At greatest latitude South,b is negative.</td></tr></table>

# 12.2.3 Heliocentric Phenomena

Certain heliocentric phenomena of the planets are given in TheAstronomical Almanac,p.A3. The dates of perihelion and aphelion are those on which the geometric distance of the planet from the Sunis a minimum and maximum respectively;the dates are thus the times when the first derivative of the distance is zero-i.e., $f ^ { \prime } ( t ) = d r / d t = 0$ .Owing to the presence ofperturbations in the planetary motion,these dates may differ from those obtained from theangular elements of the mean orbits.The actual disturbed motionof theplanetsis also used to determine the dates when they pass through the nodes on the ecliptic,and when they reach greatest latitudes north or south.At the nodes,the heliocentric latitude is zero; i.e., $\textstyle f ( t ) = b = 0$ .Thevalue of $f ( t )$ changes from negative to positive at the ascending node, and from positive to negative at the descending node.These dates are given each year for Mercury,Venus,andMars,but they occur less frequentlyfor theotherplanets,and in these cases are givenas additional notes when necessary.The dates on which aplanethas its greatest latitudenorthor south is determinedas the timesat which the first derivativeofthe latitude is zero—i.e., $f ^ { \prime } ( t ) = d b / d t = 0$ Table12.7 shows $f ( t )$ for the various phenomena.

# 12.3Risings,Settings,andTwilight

The astronomer is concerned with the phenomena of rising,seting,and twilight primarily in regard to the planning of observations.Precision of better than a minute of time is not required for this purpose,and extensive tables of these phenomena are in The Astronomical Almanac,pp.A14-A77.

The tabulated times of the phenomena referto sealevel withaclear horizon and anadopted correction for refraction under normal meteorological conditions.The actual times of rising and setting may differ considerably,especially near extreme conditions when the altitude is changing slowly.This difference can reach half a minute of time at mid-latitudes and more at high latitudes.The illuminationat the beginning or end of twilight also varies greatly with meteorological conditions.Precise times have little real significance, except in special circumstances,such as navigation at sea.

No data are given for the times of rising and seting of planets.Data may be obtained fairly simply from navigationtables such as the Rapid Sight Reduction TablesforNavigation. Within their range of declination $( 0 ^ { \circ } - 2 9 ^ { \circ } )$ ),these tables may also be used to find the times of rising and setting of stars.

Section 12.3.3 givesalgorithms that may easily be programmed into a computer to calculate the times of the phenomena.

# 12.3.1Sunrise,Sunset,and Twilight

The data givenin The Astronomical Almanac enable the times of sunrise,sunset,and the beginning and endof civil,nautical,andastronomical twilight to be found forany position between latitudes $6 6 ^ { \circ }$ north and $5 5 ^ { \circ }$ south.The times,tabulated for every fourth day,are the local mean times of the phenomena on the meridianof Greenwich andinthe specified latitude; interpolationis necessary to obtain the local mean times for intermediate latitudes,for intermediate days,and for longitude.To an accuracy of about five minutes this interpolation can generally be done by sight; near limiting conditions,when interpolation becomes difficult, large changes of time correspond toonly smallchanges in depression and accurate times have little real meaning.

Interpolation for latitude is nonlinear. Interpolation for longitude,which israrely justified,can be combined with the interpolation for date by increasing for west longitudes,or decreasing for east longitudes,the Greenwich date by the appropriate fraction (longitude in degrees/36O); for sunrise and sunset,the error due to neglecting the variation with longitude amounts to a maximum of two minutesinlatitudesup to $6 0 ^ { \circ }$ .The timesso obtainedare local mean times,which can be converted to universal time by applying longitude in time—adding if west and subtracting if east.Standard times are obtained by adding (subtracting)to the local time four minutes for every degree of longitude west (east) of the standard meridian.

At the tabulated times of sunrise and sunset,the geocentric zenith distance of the center of the Sun is $9 0 ^ { \circ } 5 0 ^ { \prime }$ ;i.e.,a geocentric altitude of $- 5 0 ^ { \prime }$ ,ofwhich $3 4 ^ { \prime }$ is allowed forhorizontal refraction and $1 6 ^ { \prime }$ forsemidiameter;the Sun'sapparent upper limb is thus on the horizon. Correctionsare necessary if some other value of thealtitudeisrequired,(such as for the conventional meteorological value of $- 3 4 ^ { \prime } )$ orto allow for the height of the observerand the elevation of the actual horizon.In such casesuse Eq.12.5.

Atthe times given for civil,nautical,andastronomical twilight,thealtitude of the center of the Sun is $- 6 ^ { \circ }$ , $- 1 2 ^ { \circ }$ and $- 1 8 ^ { \circ }$ respectively.These tabulations willproduce times for any desiredaltitudebetween $- 5 0 ^ { \prime }$ and $- 1 8 ^ { \circ }$ .

TheNauticalAlmanac,TheUSAirAlmanacandTheUKAirAlmanac tabulate the times of sunrise,sunset,and the beginning and end of civil twilight (altitude $- 6 ^ { \circ }$ )every threedays for latitudes between $7 2 ^ { \circ }$ north and $6 0 ^ { \circ }$ south;times of the beginning and end of nautical twilight (altitude $- 1 2 ^ { \circ } )$ ）arealsoinTheNauticalAlmanac.TheUSAirAlmanacandThe UKAir Almanac provide graphs that enable corrections to the time of sunrise or sunset. These corrections give the times at which the Sun has altitudes between $0 ^ { \circ }$ and $- 1 2 ^ { \circ }$ (that is,depressions to $1 2 ^ { \circ }$ ).

Sunrise or sunset ata height $H$ meters above the level of the horizon occurs when the Sun'saltitude is approximately

$$
\begin{array} { r l } { - 5 0 ^ { \prime } - 2 { : } 1 2 \sqrt { H } } & { { } ( 1 { : } 1 7 \mathrm { f o r } H \mathrm { i n f e e t } ) } \end{array}
$$

so that the same table can beused to give corrections for height to the times of sunrise and sunset.InTheUSAirAlmanacandTheUKAirAlmanacthecorrectionscanbeobtained from graphs.The constant 2.12 is really a slowly decreasing function of $H$ ,butbelowaheight of about $5 0 0 0 \mathrm { m }$ it is constant; it decreases to a value of 2.00 at $1 0 0 0 0 0 \mathrm { m }$ .

Times of rising and seting and associated phenomena change rapidly from day to day in polar regions or may not occurforlong periods,the Sun being continuously above or below the horizon;accurate times are therefore diffcult to tabulate.Diagrams are given in The US AirAlmanacand The UKAir Almanac that enable approximate times that are sufficiently accurate for all practical purposes to be obtained.

# 12.3.1.1 A Low Precision Ephemeris forthe Sun

The followingalgorithm gives the equation of time $( E )$ ,the Greenwich Hour Angle (GHA), declination (δ),and semidiameter $( S D )$ of the Sun,in degrees,to a precision of better than $1 { } ; 0$ ,which can be used with the algorithm for rising and setting (see $\ S \ 1 2 . 3 . 3$ ).Theequation of time is also useful for erecting sundials and determining the transit time of the Sun.

1.Using theJulian date,JD,and the universal time,UT,in hours,calculate $T$ ,the number of centuries from J2000.0:

$$
T = ( { \mathrm { J D } } + { \mathrm { U T } } / 2 4 - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 .
$$

2.Calculate the solar arguments;the mean longitude corrected for aberration, $L$ ;the mean anomaly, $G$ ;the ecliptic longitude, $\lambda$ ;and theobliquity of the ecliptic, $\epsilon$ ：

$$
\begin{array} { l } { L = 2 8 0 \% 4 6 0 + 3 6 0 0 0 \% 7 7 0 T \quad \mathrm { ( r e m o v e ~ m u l t i p l e s ~ o f ~ } 3 6 0 \% ) } \\ { G = 3 5 7 \% 5 2 8 + 3 5 9 9 9 \% 5 0 T } \\ { \lambda = L + 1 \% 1 5 \sin G + 0 \% 0 2 0 \sin 2 G } \\ { \epsilon = 2 3 \% 4 3 9 3 - 0 \% 0 1 3 0 0 T . } \end{array}
$$

3.The equation of time $E$ ,the GHA, $\delta$ ,and $s D$ are given by

$$
\begin{array} { r l } & { E = - 1 ^ { \circ } 9 1 5 \sin G - 0 ^ { \circ } 0 2 0 \sin 2 G + 2 ^ { \circ } 4 6 6 \sin 2 \lambda - 0 ^ { \circ } 0 5 3 \sin 4 \lambda } \\ & { \mathrm { G H A } = 1 5 \mathrm { U T } - 1 8 0 ^ { \circ } + E } \\ & { \qquad \delta = \sin ^ { - 1 } ( \sin \epsilon \sin \lambda ) } \\ & { \qquad S D = 0 ^ { \circ } 2 6 7 / ( 1 - 0 . 0 1 7 \cos G ) . } \end{array}
$$

Plotting the positionof the apparent Sun relative to the mean Sun (which moves uniformly along the equator) produces the analemmic curve,see Fig.12.1. The displacement of the apparent Sun in longitude is given by the equation of time $( E )$ and the displacement in latitudeis given by the declination (δ).The progress of the apparent Sun throughout the yearis indicated at the beginning of each month on the closed curve.The analemmic curve playsan important role in certain types of sundial.

![](images/41407d6e4b562be18aa19903efe6877effee093aef9b1bd893f4a53ef155b2a5.jpg)  
Figure12.1 Theanalemmic curve

# 12.3.2Moonrise and Moonset

The tables in The Astronomical Almanac give,for every day and fora range of latitudes from $6 6 ^ { \circ }$ north to $5 5 ^ { \circ }$ south,thelocal mean times of moonrise and moonset for the meridian ofGreenwich.Interpolation for latitude and longitude is necessary to obtain local times for other places.In practice,timesare rarely required more accurately than to within about five minutes,and interpolation can be done mentally.Formal interpolation,using tables such asthosegivenin TheNautical AlmanacandTheUSAirAlmanac,yieldstimesaccurate to about two minutes.The times so obtained may be converted to universal time or standard time byapplyinglongitudeintime—adding ifwestand subtractingifeast.Times forlatitudes between $7 2 ^ { \circ }$ north and $6 0 ^ { \circ }$ southare givenin TheNautical Almanacand TheUSAirAlmanac. InTheUSAirAlmanacand TheUKAirAlmanactimesappear in graphical formabove $7 2 ^ { \circ }$ north,right up to the North Pole.

In calculating the times of moonrise and moonset,the true altitude $h$ of the center of the Moon is

$$
h = - 3 4 ^ { \prime } - \mathrm { s e m i d i a m e t e r + h o r i z o n t a l p a r a l l a x }
$$

where $3 4 ^ { \prime }$ isallowed for horizontal refraction; depending upon the distance of the Moon, $h$ lies in the range $5 ^ { \prime }$ to $1 1 ^ { \prime }$ .At these times,the upper limb of theMoon is on the horizon;no allowanceismade forphase.Ata heightof $H$ metersabove the horizon,the altitude of the Moon when its upper limb is on the horizon is decreased by $2 . 1 2 { \sqrt { H } }$ (see $\ S 1 2 . 3 . 3 . 1 $ ).

The Moon revolves around the Earth and makes one complete revolution relative to the Sunina synodic month of mean length 29.53 days;in that time the Moon,therefore,appears to lose one transit acrossany meridian and,in general,one rising and one setting.During each month there is,therefore,no moonrise on one local day (near last quarter) and no moonset on one local day (near first quarter).In high latitudes the times of the phenomena change rapidly from day to day and may not occur for longperiods,the Moon being continuously above or below the horizon;in these extreme conditions the times of moonrise and moonset sometimes decrease fromday to day,instead of the usual increase in lowerlatitudes,and it is possible to have two moonrises or two moonsets during the same local day.

# 12.3.3Formulae Associated with Rising and Setting

Consider first an algorithm for calculating the times of rising or setting of a body at true altitude $h$ .

The GHA and declination (δ) of the body are required to about one minute of arc as a function of UT.For the Moon,the horizontal parallax $\pi$ is also required. To speed up the calculation,which is iterative,itis convenient toexpress GHA, $\delta$ ,and $\pi$ as daily polynomials. For the Moon second-order polynomialsare required for GHA and $\delta$ ,and first order for $\pi$ . Forother bodies like the Sunand the inner planets,first-order polynomials are sufficient.For stars and outer planets,a constant daily value for declination may be adopted.Alternatively low-precision formulae forthe ephemeris of the Sun(§12.3.1.1) may be used.For the Moon, thelow-precision formulae on p.D22of The Astronomical Almanacmay be used.

At sunrise and sunset the apparent altitude of the upper limb on the horizon is zero and hencethe adopted true altitude indegrees is $h = - 5 0 / 6 0 - 0 . 0 3 5 3 { \sqrt { H } }$ where $H$ is the height, in meters,of the observer above the horizon.

Similarlyat moonrise and moonset the apparent altitude of the upper limb on the horizon is zero and the adopted true altitude $h = - 3 4 / 6 0 + 0 . 7 2 7 5 \pi - 0 . 0 3 5 3 \sqrt { H }$ At rise and set of a star ora planet,the apparent altitude of the body is zero; hence, $h = - 3 4 / 6 0 - 0 . 0 3 5 3 \sqrt { H }$ .

Other important cases to consider are twilights: civil twilight $h = - 6 ^ { \circ }$ ,nautical twilight $h = - 1 2 ^ { \circ }$ ,and astronomical twilight $h = - 1 8 ^ { \circ }$ .

Thetime of rise orset,UT,inhours,is foundbysolving iterativelythe equation

$$
\mathrm { U T } = \mathrm { U T } _ { 0 } - ( \mathrm { G H A } + \lambda \pm t ) / 1 5
$$

where the plus sign is used for rise and the minus sign for set,and $t$ is the hour angle of the body at $\mathrm { U T _ { 0 } }$ ,which is given by

$$
\cos t = { \frac { \sin h - \sin \phi \ \sin \delta } { \cos \phi \ \cos \delta } }
$$

and $\phi$ is the latitude and $\lambda$ the longitude (positive to the east).

$$
\begin{array} { l } { { \mathrm { I f ~ c o s \ : } t > + 1 , \mathrm { s e t \ : } t = 0 ^ { \circ } ; } } \\ { { \mathrm { I f ~ c o s \ : } t < - 1 , \mathrm { s e t \ : } t = 1 8 0 ^ { \circ } . } } \end{array}
$$

As an initial guess,set $\mathrm { U T _ { 0 } } = 1 2 ^ { \mathrm { h } }$ ,although any valuein the range $0 ^ { \mathrm { h } }$ to $2 4 ^ { \mathrm { h } }$ will do. After each iteration,add multiples of $2 4 ^ { \mathrm { h } }$ to set UT in the range $0 ^ { \mathrm { h } }$ to $2 4 ^ { \mathrm { h } }$ .Replace $\mathrm { U T _ { 0 } }$ by UT until the difference between them is less than $0 ^ { \mathrm { h } } . 0 0 8 .$ If for several iterations cos $t > 1$ ,itislikely that there is no phenomenonand the body remains below the true altitude $h$ all day. On the other hand, if cos $t < - 1$ ,the body remains above the true altitude all day.In each lunation, around firstquarter,there is alwaysaday when the Moon does not set,and another,around last quarter,when the Moon does not rise.

At latitudes above $6 0 ^ { \circ }$ the algorithmmay fail,and it is necessary to use a more systematic approach. If $h _ { 0 }$ is the adopted true altitude,the times when $h = h _ { 0 }$ where

$$
\sin h = \sin \phi \ \sin \delta + \cos \phi \ \cos \delta \ \cos ( \mathrm { G H A } + \lambda )
$$

are the times of rising or seting.

These roots,if they exist,will liebetween the truealtitude at $0 ^ { \mathrm { h } }$ and $2 4 ^ { \mathrm { h } }$ and the maximum and minimum altitudes during theday.The maximum and minimum altitudes occur ator very nearupper andlower transit.These times are found by setting $t = 0 ^ { \circ }$ and $t = 1 8 0 ^ { \circ }$ in Eq.12.10 and iterating.

Only for theMoonat high latitudes is it necessary to calculate the maximumand minimum altitudes more precisely.This calculation is done by fiting a second-order polynomial to the true altitude at points around upper or lower transit and differentiating with respect to time to find the turning point.

# 12.3.3.1 Effects of Dipand Refraction

Dip is required for reducing sights made with a marine sextant and for calculating the true altitude of a body at rise and set.Dip is the apparent angle between the geometric horizon (at rightangles to the vertical) and the visible horizon.For an observer at height $H$ above the surface of the Earth,dip $D ( H ) = 1 . 7 5 { \sqrt { H } }$ ,where $H$ is in meters ${ \bf ( 0 . 9 7 } \sqrt { H }$ if $H$ is in feet) (seeWoolard and Clemence 1966,p.215).

A navigator using a marine sextant sets on the apparent horizon and wants to know how much the horizon appears to be below the horizontal and therefore only needs to know the dip.On the other hand,when computing the times of rise or setof a body,we need to know the true altitude when the body appears to be on the horizon,which involves dip and the refraction between the horizon and the observer $R ( H )$ ,where $R ( H ) = 0 . 3 7 \sqrt { H }$ and $H$ isin meters (or $0 . 7 2 0 \sqrt { H }$ if $H$ is in feet).

In Fig.12.2, $o$ is the observer at height $H$ above the surface of the Earth, $s$ isthe body at rise or set,and $A$ is the observer's horizon.The true altitude of $S$ from the vantage point $A$ is $- 3 4 ^ { \prime }$ due to refraction. The true altitude of $s$ from $o$ is the true altitude at $A - D ( H ) - R ( H ) = - 3 4 ^ { \prime } - 1 / 7 5 \sqrt { H } - 0 ; 3 7 \sqrt { H } = - 3 4 ^ { \prime } - 2 ; 1 2 \sqrt { H }$

Refraction,the bending of light as it passes through the atmosphere,is illustrated in Fig.12.2 for the rising or seting of acelestial object.The following approximate formulae (Bennett 1982) are valid for all altitudes and standard meteorological conditions.A more precise algorithm is given in $\ S 7 . 2 . 7 .$ The amount of refraction, $R$ ,is given by

$$
R ( h _ { a } ) = { \frac { 0 . 0 1 6 7 } { \tan { ( h _ { a } + 7 . 3 1 / ( h _ { a } + 4 . 4 ) ) } } }
$$

where $h _ { a }$ is the apparent altitude.Alternatively,if $h$ is the true altitude,then

$$
R ( h ) = \frac { 0 . 0 1 6 7 } { \tan { ( h + 8 . 6 / ( h + 4 . 4 ) ) } } .
$$

![](images/c915b3a57eef8174abf782ad67d35168bbe4d9b1654b8504978d8f701ecbc517.jpg)  
Figure12.2Thehorizonatrising or setting

# 12.3.3.2 Time fora Specified ShadowLength

The lengths of shadows depend upon the apparent altitude of the Sun, $h _ { a }$ .The true altitude $h$ of the Sun is needed to find the required time where

$$
h = h _ { a } - R ( h _ { a } )
$$

and $R$ is the refractionat apparent altitude $h _ { a }$ which may be calculated approximately using Eq.12.14.Altematively, if $h$ is known and $h _ { a }$ is required useEq.12.15 for calculating the refractionattruealtitude $h$ and set

$$
h _ { a } = h + R ( h ) .
$$

# 12.3.3.3 Rates of Change

The rate of change of hour angle with altitude may be obtainedby differentiating the altitude as shown in Eq.12.13.Assuming that $\lambda , \phi$ ,and $\delta$ do not change with time,then the change in time, $( \Delta t )$ ,inhours,foragivenchange inaltitude $( \Delta h )$ ,indegrees,can be calculated from the simple expression

$$
\Delta t = { \frac { 1 } { \Delta { \mathrm { L H A ~ } } \cos \phi \ \sin Z } } \Delta h
$$

where△LHA is the rate of change of hour angle per hour and $Z$ is the azimuth.For the Sun, $\Delta \mathrm { L H A } = 1 5 ^ { \circ }$ per hour and for the Moon, $\Delta \mathrm { L H A } = 1 4 . 4 9 3$ per hour.

Near rise and set when $h \approx 0 ^ { \circ }$ ,this expression can be further simplified to

$$
\begin{array} { r } { \Delta t = A \Delta h \phantom { x } } \\ { \mathrm { { w h e r e } } A = 6 0 / \left( \Delta \mathrm { { L H A } } \sqrt { \cos ^ { 2 } \phi - \sin ^ { 2 } \delta } \right) } \end{array}
$$

and $\Delta t$ is now in minutes of time.This correction is accurate to within afew minutes provided $A$ does not exceed 20 and $\Delta h$ does not exceed a few degrees.

# 12.3.3.4 Timefora Specified Azimuth

Another interesting problem is to calculate the time when the azimuth $Z$ of abody takes a particular value.The time UT is calculated iteratively from

$$
\mathrm { U T } = \mathrm { U T } _ { 0 } - ( \mathrm { G H A } + \lambda \pm t ) / 1 5
$$

where the plus sign is used if $Z < 1 8 0 ^ { \circ }$ and the minus sign is used otherwise. $t$ iscalculated from

$$
\cos t = { \frac { - a b \pm { \sqrt { 1 + a ^ { 2 } - b ^ { 2 } } } } { 1 + a ^ { 2 } } }
$$

where $a = \tan Z \sin \phi , b = - \cos \phi$ tan $\delta$ tan $Z$ ,and the plus sign is used if $9 0 ^ { \circ } < Z < 2 7 0 ^ { \circ }$ ; otherwise use the minus sign.In the special cases $Z = 9 0 ^ { \circ }$ and $Z = 2 7 0 ^ { \circ }$ orif $1 + a ^ { 2 } - b ^ { 2 } < 0$ ， then

$$
\begin{array} { r } { \cos t = - b / a = \tan \delta / \tan \phi ; } \\ { \mathrm { I f } \cos t > + 1 , \mathrm { s e t } \cos t = + 1 ; } \\ { \mathrm { I f } \cos t < - 1 , \mathrm { s e t } \cos t = - 1 . } \end{array}
$$

IterateEq.12.20 until UT differs from $\mathrm { U T _ { 0 } }$ by less than $0 ^ { \mathrm { h } } . 0 0 8$

# 12.3.3.5 Times of Transit

Times of transit are required to low precision for planning observations,and for setting instruments.The times foraparticular place may be calculated forany body by iterating Eq.12.10 and setting $t = 0 ^ { \circ }$ .Forthe Sun,the transit time may be determined from $1 2 ^ { \mathrm { h } } - E / 1 5$ ,where $E$ is the equation of time given in $\ S \ 1 2 . 3 . 1 . 1$ .

# 12.3.4 Illumination

The ground illumination (i.e.,the illuminance on a horizontal surface) from natural sources varies considerably during the day.The variation of the illumination on a horizontal surface, inclearconditions,on the surface of the Earth isshown diagrammatically inFig.12.3 asa functionofaltitude.

This section contains a simple method of calculating ground illuminance from sunlight, twilight,and moonlight based on data publishedby the Radio Corporation of America (RCA 1974).A more precise method is available in Janiczek and DeYoung (1987).This method is based on the extensive Natural Illumination Charts produced by Brown.

Data from the handbook have been represented by sets of cubic polynomials for the Sun and the fullMoonat mean distance,for various ranges of altitudes,in Table 12.8.The illuminance is measured in lux or lumens per square meter;however,the logarithm of the illuminance has been used because large ranges are involved,and also the sensitivity of the human eye varies in proportion to the logarithm of intensity.Thus the illuminance $I$ in lux is given by

$$
\log _ { 1 0 } I = l _ { 0 } + l _ { 1 } x + l _ { 2 } x ^ { 2 } + l _ { 3 } x ^ { 3 }
$$

![](images/f8c9d81c57926136a63dfbdfdf81999c92979de82c508c1cfc4eb2b6fa4f46ba.jpg)  
Figure 12.3 Ground illumination from various sources. $\mathrm { { f } = 0 ^ { \circ } }$ corresponds to approximately the full moon, $\mathrm { f } = 9 0 ^ { \circ }$ to the first or third quarter,etc.

Table12.8 Coeffcients for calculating ground illumination   

<table><tr><td rowspan="2">Altitude range</td><td rowspan="2"></td><td colspan="4">From the Sun</td><td rowspan="2">Maximum error</td></tr><tr><td>10</td><td>1</td><td>h</td><td>1</td></tr><tr><td>20°</td><td>90°</td><td>3.74</td><td>3.97</td><td>-4.07</td><td>1.47</td><td>0.02</td></tr><tr><td>5</td><td>20</td><td>3.05</td><td>13.28</td><td>-45.98</td><td>64.33</td><td>0.02</td></tr><tr><td>-0.8</td><td>5</td><td>2.88</td><td>22.26</td><td>-207.64</td><td>1034.30</td><td>0.02</td></tr><tr><td>-5</td><td>-0.8</td><td>2.88</td><td>21.81</td><td>-258.11</td><td>-858.36</td><td>0.02</td></tr><tr><td>-12</td><td>-5</td><td>2.70</td><td>12.17</td><td>-431.69</td><td>-1899.83</td><td>0.01</td></tr><tr><td>-18</td><td>-12</td><td>13.84</td><td>262.72</td><td>1447.42</td><td>2797.93</td><td>0.01</td></tr><tr><td></td><td colspan="6">From the Full Moon atMean Distance</td></tr><tr><td>20°</td><td>90°</td><td>-1.95</td><td>4.06</td><td>-4.24</td><td>1.56</td><td>0.02</td></tr><tr><td>5</td><td>20</td><td>-2.58</td><td>12.58</td><td>-42.58</td><td>59.06</td><td>0.03</td></tr><tr><td>-0.8</td><td>5</td><td>-2.79</td><td>24.27</td><td>-252.95</td><td>1321.29</td><td>0.03</td></tr></table>

where $x = h / 9 0 , h$ is the altitude,and $l _ { 0 } , l _ { 1 } , l _ { 2 } , l _ { 3 }$ are the appropriate set of coefficients given in Table12.8 for variousranges of altitude.To obtain the total ground illumination from the Moon,corrections for phase and parallax must also be added (see $\ S 1 2 . 3 . 4 . 2 $

The values for the Sun in daylight give the illuminance from direct and indirect sunlight ina cloudless sky.The values for indirect sunlight are about a factor of 1O smaller.If the sky is overcast,the values for indirect sunlight should be reduced by about a factorof 1O,and if the skyisvery dark byabouta factorof1oo.Acorrection of $2 \log _ { 1 0 } ( S / S _ { 0 } )$ ,where $s$ isthe semidiameter of the Sun and $S _ { 0 }$ is the semidiameter at mean distance,should be added to the daylightilluminance to allow for the variable distance of the Sun from the Earth.

When the Sun is below the horizon,the sky is illuminated from the sources discussed in the following sections.

# 12.3.4.1 Twilight

Thisis caused by the scattering of sunlight from the upper layers of the Earth'satmosphere. Itbeginsat sunset (ends at sunrise) and is conventionally taken to end (or begin)when the center of the Sun reaches an altitude of $- 1 8 ^ { \circ }$ ;thisisalsoreferred toasastronomicaltwilight. Atan altitude of $- 1 8 ^ { \circ }$ ,theindirectillumination from the Sun on a horizontal surface is about $6 \times 1 0 ^ { - 4 }$ lux,rather less than the contribution from starlight and airglow.The actual brightness of the sky depends onwhere the observer looksand where the illuminationis coming from,as well as on meteorological conditions.

In navigational practice and for certain civil purposes,two intermediate steps in the twilight period are recognized and tabulated:civil twilight ends (or begins) when the Sun reachesan altitude of $- 6 ^ { \circ }$ and nautical twilight ends(or begins)when the Sun reaches an altitude of $- 1 2 ^ { \circ }$ .Before morningand aftereveningcivil twilight,outdooractivities that depend on natural lighting requireartificial illumination.The degree of ilumination at the beginning and end of civil twilight (in good conditions and in the absence of other illumination) is usually described for navigational purposesas illumination such that the brightest starsarevisibleand thesea horizonisclearlydefined;for thebeginningand end of nautical twilight,the corresponding statement is that the sea horizon is in general notvisible and it is too dark for the observation of altitudes with reference to the horizon.

# 12.3.4.2 Moonlight

Theilluminationreceived from the Moon varies according to phase,altitude,and atmospheric extinction.From fullMoonin the zenith,the intensity of illumination ona horizontal surface is approximately $0 . 2 7 \ \mathrm { l u x }$ ,equivalentto that fromthe Sunatanaltitudeofabout $- 8 ^ { \circ }$ . Theamount of ground illumination at night from moonlight— $\mathbf { \cdot l o g } _ { 1 0 } M$ ，where $M$ isthe illuminance in lux—may be calculated from $L _ { 1 } ,$ ,the ground illumination fromaFull Moon at altitude $h$ ,atamean distance thathasbeencorrected forphase $( L _ { 2 } )$ and parallax $( L _ { 3 } )$ as follows:

$$
\log _ { 1 0 } M = L _ { 1 } + L _ { 2 } + L _ { 3 } .
$$

Extracting the appropriate set of $l ^ { \prime }$ 's from the table and setting $x = h / 9 0$ ,where $h$ is the altitude of the Moon, then

$$
\begin{array} { r l } & { L _ { 1 } = l _ { 0 } + l _ { 1 } x + l _ { 2 } x ^ { 2 } + l _ { 3 } x ^ { 3 } } \\ & { L _ { 2 } = - 8 . 6 8 \times 1 0 ^ { - 3 } f - 2 . 2 \times 1 0 ^ { - 9 } f ^ { 4 } } \\ & { L _ { 3 } = 2 \log _ { 1 0 } ( \pi / 0 . 9 5 1 ) ; } \end{array}
$$

Figure 12.3 also shows the ground illumination on a horizontal surface from the standard phases of the Moon at mean distance and at various altitudes.The half Moon gives only oneninth as much light as the full Moon.For astronomical observations,the position of the Moon inthesky,ratherthan the general illumination,isthemost important factor.

12.3.4.3Starlight,Airglow,Aurora,ZodiacalLight,andGegenschein

The total illumination from the stars contributes about $2 . 2 \times 1 0 ^ { - 4 }$ lux,rather less than the Sunat the beginning and end of astronomical twilight.The illumination from the stars together with airglow contributes about $2 \times 1 0 ^ { - 3 }$ lux.The illumination from the aurora (which depends upon solar activity) may in rare cases be comparable with moonlight.The other sources are very faint and never give an illumination greatly exceeding that from starlight.As with moonlight,the position of the source is the most important factor for astronomical observations.

# 12.4 Occultations

Only dates and general areas of visibility for the occultations of planets and bright stars by the Moon are published in The Astronomical Almanac.Asthe International Lunar Occultation Centre ceased operations in March 2Oo9,coordination of occultation observations by the Moon is now handled by The International Occultation Timing Association (IOTA） at URL[2].

# 12.4.1 Occultations of Stars

Whenever a star is within an angular distance from the Moon that is less than the sum of the Moon's horizontal parallax and semidiameter,it will be occulted from some point on the Earth.The large number of occultations makes it impossible to publish maps of each occultation in The Astronomical Almanac.However,global visibility mapsare availableon TheAstronomical Almanac Online website(URL[1]).Itis possible,however,tocalculateand display these maps on a personal computer. The calculations require the Besselian elements, which are defined ina similarway to those for eclipses (see $\ S \ 1 1 . 3 . 2 \}$ .In occultations,the fundamental plane passes through the centerof the Earth and isperpendicular to the line joining the starand thecenterof the Moon—i.e.,to the axisof shadow.The origin of the coordinates is the center of the Earth; the $x$ -axisisthe intersection of the Earth's equator with thefundamental plane and is takenas positive toward the east; the $y$ -axis isperpendicular to that of $x$ andis taken as positive toward the north in the fundamental plane.The great distance of the star implies that the fundamental plane isperpendicular to the line joining the center of theEarth to the star,and that the Moon’s shadow is essentiallyacylinderwhose intersection with the fundamental plane is acircle of invariable size,its diameter being equal to that of theMoon.The coordinates of the center of this circle—i.e.,the axis of shadow-are denoted by $x$ and $y$ .The adopted unit of linearmeasurement is theEarth's equatorial radius.

The Besselian elements are given for one instant only—namely,the time of conjunction of the star and Moon in right ascension, when $x$ is zero. They are:

$$
\begin{array} { r l } & { T _ { 0 } = \mathrm { t h e ~ U T ~ o f ~ c o n j u n c t i o n ~ i n ~ r i g h t ~ a s c e n s i o n } ; } \\ & { H = \mathrm { t h e ~ G r e e n w i c h ~ H o u r ~ A n g l e ~ o f ~ t h e ~ s t a r ~ a t ~ } T _ { 0 } ; } \\ & { Y = y ~ \mathrm { a t } ~ T _ { 0 } ; } \\ & { x ^ { \prime } , y ^ { \prime } = \mathrm { t h e ~ h o u r l y ~ r a t e s ~ o f ~ c h a n g e ~ i n ~ } x ~ \mathrm { a n d } ~ y ; } \\ & { \alpha _ { s } , ~ \delta _ { s } = \mathrm { t h e ~ r i g h t ~ a s c e n s i o n ~ a n d ~ d e c l i n a t i o n ~ o f ~ t h e ~ s t a } } \end{array}
$$

The formulaefor $x$ and $y$ ,thecoordinatesof thecenterof the shadowin the fundamental plane,are

$$
\begin{array} { l } { { x \sin \pi = \cos \delta \sin ( \alpha - \alpha _ { s } ) } } \\ { { y \sin \pi = \sin \delta \cos \delta _ { s } - \cos \delta \sin \delta _ { s } \cos ( \alpha - \alpha _ { s } ) } } \end{array}
$$

where $\alpha$ and $\delta$ are the right ascension and declination of the Moon at a particular Universal Time and $\pi$ is the parallax.

For prediction purposes these reduce to

$$
x = \frac { \alpha - \alpha _ { s } } { \pi } \ \cos { \delta } ; \qquad y = \frac { \delta - \delta _ { s } } { \pi } + 0 . 0 0 8 7 \ x ( \alpha - \alpha _ { s } ) \ \sin { \delta _ { s } }
$$

where $\alpha$ , $\delta$ ,and $\pi$ are in degrees.

At conjunction

$$
\begin{array} { r l r } { x = 0 ; } & { { } } & { y = Y = \displaystyle \frac { \delta - \delta _ { s } } { \pi } } \\ { x ^ { \prime } = \displaystyle \frac { \alpha ^ { \prime } \cos \delta } { \pi } ; } & { { } } & { y ^ { \prime } = \displaystyle \frac { \delta ^ { \prime } } { \pi } - Y \displaystyle \frac { \pi ^ { \prime } } { \pi } . } \end{array}
$$

Here the primed quantities are hourly variations that arise fromdifferentiating the Moon's daily polynomial coefficients for $\alpha$ , $\delta$ ,and $\pi$

Therectangular coordinates of the center of the shadow on the surface of the Earth at Universal Time $\tau$ from conjunction are given by

$$
\scriptstyle { \begin{array} { l } { x = x ^ { \prime } t } \\ { y = y ^ { \prime } t + Y } \\ { z = { \sqrt { ( 1 - x ^ { 2 } - y ^ { 2 } ) } } } \end{array} }
$$

where $z$ ismeasured along the shadow axis from the fundamental plane toward the Moon. The longitude and latitude $( \lambda , \phi )$ of this point on the surface of the Earth are calculated from

$$
\begin{array} { l } { \phi = \sin ^ { - 1 } ( y \cos \delta + z \sin \delta ) } \\ { \displaystyle h = \tan ^ { - 1 } \frac { x } { - y \sin \delta + z \cos \delta } } \\ { \lambda = h - ( H + 1 5 \times 1 . 0 0 2 7 3 8 t ) . } \end{array}
$$

Therectangular coordinates of the edge of the shadow on the surface of the Earth,a $( \xi , \eta , \zeta )$ ,are given by

$$
\begin{array} { l } { { \xi = x - k \ \sin Q } } \\ { { \eta = y - k \ \cos Q } } \\ { { \zeta = \sqrt { ( 1 - \xi ^ { 2 } - \eta ^ { 2 } ) } } } \end{array}
$$

where $k = 0 . 2 7 2 5$ is the radius of the Moon in Earth radii and $\boldsymbol { Q }$ cycles through the range $0 ^ { \circ }$ to $3 6 0 ^ { \circ }$ .The longitude and latitude $( \lambda , \phi )$ ofa point on the edge of the shadow is obtained from Eq.12.30 byreplacing $( x , y , z )$ ,with $( \xi , \eta , \zeta )$

The remainder of this section describes how to plot a map of the area of visibility of an occultation.Project the longitudes and latitudes of the continents,islands,and places of interestonto theplane that passes through the center of the Earth and isperpendicular to the direction defined bya vector from the center of the Earth to the place $\lambda _ { c }$ , $\phi _ { c }$ .Here( $\lambda _ { c } ,$ $\phi _ { c }$ )is the longitude and latitude of the center of the shadow at the time of conjunction.This plane rotates with the Earth and coincides with the fundamental plane at conjunction. The rectangular coordinates of a place at longitude and latitude $( \lambda , \phi )$ are given by

$$
\begin{array} { r l } & { u = \cos \phi \ \sin ( \lambda - \lambda _ { c } ) } \\ & { v = \sin \phi \ \cos \phi _ { c } - \cos \phi \ \sin \phi _ { c } \cos ( \lambda - \lambda _ { c } ) } \\ & { w = \sin \phi \ \sin \phi _ { c } + \cos \phi \ \cos \phi _ { c } \cos ( \lambda - \lambda _ { c } ) } \end{array}
$$

where $u$ and $v$ are in the plane (with the origin at the center of the Earth), $u$ is to the east, $\boldsymbol { v }$ is to the north,and $w$ isthe height of the place above the plane; $w \ge 0$ for all places to be plotted.

To plot the edge of the shadow at any time during the occultation,calculate the rectangular coordinates of the center of the shadow $x _ { 0 }$ , $y _ { 0 }$ ,fromEq.12.29.Then calculate the coordinates $\xi$ ， $\eta$ ， $\zeta$ ofthe edge of the shadow from Eq.12.31 and obtain the corresponding $( \lambda , \phi )$ fromEq.12.30.Finallyproject the $( \lambda , \phi )$ of the shadow outline onto the same plane as the continents,etc.,using the coordinates $( u , v )$ in Eq. 12.32.

When $\zeta ^ { 2 } + \eta ^ { 2 } > 1$ ,the shadow isonly partiallyon the Earth.To find the values $Q _ { 1 }$ and $Q _ { 2 }$ where the edge of the shadow cuts the surface of the Earth,see Fig.12.4,where $o$ is the center of the Earth and $S$ is the center of the shadow.

The great circle arc $A B$ between the polar angle $\theta _ { 1 }$ and $\theta _ { 2 }$ is then plotted by setting $x = \cos \theta$ , $y = \sin \theta$ ,and $z = 0$ ,and usingEqs.12.30and12.32.The polaranglesare found as follows: Calculate $\boldsymbol { Q } _ { 1 }$ and $Q _ { 2 }$ from

$$
\sin ( Q _ { 1 } + S ) = { \frac { k ^ { 2 } + D ^ { 2 } - 1 } { 2 k D } } \quad { \mathrm { a n d } } \quad Q _ { 2 } = 1 8 0 ^ { \circ } - Q _ { 1 } - 2 S
$$

Then for $i = 1$ and 2

$$
\begin{array} { r l } & { \xi _ { i } = x _ { 0 } - k \sin Q _ { i } } \\ & { \eta _ { i } = y _ { 0 } - k \cos Q _ { i } } \\ { \mathrm { a n d } } & { \theta _ { i } = \tan ^ { - 1 } { ( \eta _ { i } / \xi _ { i } ) } , 0 ^ { \circ } \leq \theta _ { i } \leq 3 6 0 ^ { \circ } . } \end{array}
$$