![](images/efc0b0bfc56f45dd313c29bbb2ad5f6c1e180cdc27e34c0701d952c582bdb26b.jpg)

# Celestial Mechanics Volume 2, Part 2 Perturbation Theory

Volume2, Pal Volume2,Part

The launching of space vehicles has givenrise toabroadenedinterest in the problems of celestial mechanics, and the availability of computers has made practical the solution of some of the more numerically unwieldy of these problems. These circumstances only furtherenhance the importanceof the appearance of Celestial Mechanics, which isbeing published infive volumes. This treatise isby far the most extensive of its kind,and it rigorously develops the fullmathematical theory.Itsauthoris Professor of Astronomy at the University of Tokyo.

Thefirstvolume,DynamicalPrinciples and Transformation Theory,appeared in1970.Volume ll,which consists of two separately bound parts,takesup the process of iteration of successive approximations,knownasperturbation theory.Together,the two parts describe the classical methods of computing perturbations inaccordancewithplanetary, satellite,andlunartheories,with their modern modifications.Inparticular，the motionsofartificial satellitesandinterplanetaryvehiclesarestudied inthe lightofthesetheories.

In addition to explaining the various perturbation methods, the work describes the outcomes of their application to existing celestial bodies,such as the discovery of new planets, the determination of their masses, the explanation of the gaps in.the distribution of asteroids, and the capture.and ejection hypotheses of satellitesandcometsand their genesis.

Part1 consists of three chaptersand Part 2 of two. The chapters (italicized) and their subcontents are as follows: Part1-Disturbing Function:Laplace coefficients; inclined circular orbits; Newcomb's operators; convergence criteria;recurrence relations;approximation to higher coefficients.Lagrange's Method: variation of the elements; Poisson's theorem; Laplace-Lagrange theory of secular perturbation; Secular variation of asteroidal orbits; Gauss's method; discussion of the law of gravitation. Delaunay's Theory:Delaunay'smethod; theory of libration,motion of satellites; Brown's transformation; Poincare's theory;Von Zeipel's theory.Part 2— Absolute Perturbation:coordinate perturbation; Hansen's theory;Newcomb's theory; Gylden's theory; Brown's theory; Andoyer's theory; cometary perturbation; Bohlin's theory;solution by Lambert's

# CELESTIAL MECHANICS Volume II, Part 2 Perturbation Theory

# CELESTIAL MECHANICS

Yusuke Hagihara

# Perturbation Theory

# The MIT Press

Copyright@ 1972 by the Massachusets Institute of Technology Designed by Dwight E.Agner. Set in Monotype Baskeruille. Printed by HallidayLithograph Corp.,and bound byThe Colonial Press,Inc. in the United States of America.

All rights reserved.No partof this book may bereproduced in any formor by any means,electronic ormechanical,including photocopying,recording,orby any information storage and retrieval system,without permissionin writing fromthe publisher.

ISBN0 262 08053 2

Library of Congress catalog card number:74-95280

# Preface

Volume II, Part 1 and its companion, Volume II, Part 2, describe the clasical methods of computing perturbations in accordance with planetary,satelite,and lunar theories,with their modern modifications； in particular, the motions of artificial satellites and interplanetary vehicles are studied in the light of these theories.The description is not restricted merely to the explanation of various methods but includes the outcomes of their application to existing celestial bodies from an astronomical point of view, such as the discovery of new planets, the determination of their masses, the explanation of the gaps in the asteroidal distribution, and the capture and ejection hypotheses of satellites and comets and their genesis.The treatment in each chapter is chosen so as to proceed from the elementary part to the advanced.

As has been stated in Volume I, the methods in celestial mechanics must at present rely on some transcendental process.This is the process of iteration of successive approximations, called perturbation theory.A primitive procedure for computing the perturbation is to take the Keplerian ellipse as a first approximation.Deviation from the ellipse is due to the presence of other disturbing bodies whose masses are small compared with the sun in the case of a planetary system, or whose mean distances are large in the case of a satellite system.The perturbation is small,of the order of the disturbing masses or the small meandistance ratios,and is computed by the Laplace-Lagrange method of variation of elements.The perturbation is expanded in powers of eccentricities and inclinations, since these are small for the main existing natural celestial bodies in the solar system.

However, the difficulty of small divisors came in with the nearcommensurability of mean motions,and various other methods of successive approximations have been proposed. In general, an orbit incorporated with secular variations has been adopted as the intermediary orbit in a first approximation.However,Gylden's theory of a moving ellpse as intermediary orbit cannot be recommended, despite the vast amount of literature concerning the theory. Hansen's ingenious method is still in great use and has now been modifed in order to proceed to higher orders of approximation.Newcomb's theory is a modified form of a theory originally considered by Laplace.The Tables for the motion of planets in current use for almanac computation were compiled in accordance with Hill's theory of Jupiter and Saturn founded on Hansen's method,and in accordance with Newcomb's theory for the other major planets except Pluto; Clemence has now built up a modified Hansen theory for Mars. The motion of the moon is fully represented by the theory of Hill and Brown一a monument to last century's celestial mechanics.At present this theory is being checked by means of modern electronic computers.Hill's intermediary orbit is a periodic orbit with a part of the solar perturbation taken into account.

The motion of satellites is rather complicated.The mean motions of the Galilean satellites of Jupiter have double commensurability. Some of Saturn's satellites have commensurable mean motions. Satellites remote from their parent planets are exposed to strong solar perturbation. To overcome the difficulties of computation for such satellites,special methods have been and should be devised.

It will remain an open question whether a comet in the solar system was captured by Jupiter,until a detailed numerical computation by means of computers is carried out for each individual comet. Another open question is whether the asteroids are broken pieces from a larger mother mass. The gaps in the asteroidal distribution are still a riddle.

The launching of artificial vehicles to the moon and planets 一even the motion of an artificial earth satellite-sets new problems in celestial mechanics hitherto untouched upon.We must consider orbits with high eccentricities and inclinations,without expanding the perturbation in powers of eccentricity and inclination,as we do for the natural celestial bodies of the solar system. Motion in interplanetary space, where the perturbations due to two or more than two masses are comparable in magnitude,is a problem of pressing importance at present. Thus we are now confronted face to face with various new problems in celestial mechanics for which the solutions are urgently needed.

Methods for treating these problems are here described without any mathematical discussion as to their convergence and the legitimacy of the processes. In any of these methods the process of successive approximations is not uniformly convergent,as will be proved in Volume III.At present we cannot estimate the errors of truncating at a finite number of iterations to represent the rigorous solution,whose existence will be proved in Volume V but which is not yet known. The processes described in this volume are semiconvergent in the sense used by Poincaré. Can we approach nearer the solution by further iterations of such successive approximations? This is not true of Stirling's series, for example; the deviation becomes larger if we take higher-order terms in the expansion beyond a certain term.It is to be kept in mind that the formal series expansions are not our final goal, even though the results may represent the observations to a currently realizable degree of accuracy.

In each method, deviation from the intermediary orbit is represented by formal series. Such formal series are arranged in the form of trigonometric series with linear functions of time as arguments. If these series were uniformly convergent, then they would represent quasi-periodic functions,and the'solutions would be quasi-periodic; they will be really quasi-periodic if certain conditions are satisfied,as Arnold and Moser have recently shown.We shall discuss this in Volume IV.

Chapter 7 of the present volume begins with the expansion techniques of the disturbing function in powers of the ratio of the semimajor axes, the eccentricities,and the inclinations. Convergence criteria for the expansions are discussed.The recurrence relations among the coefficients of the expansions are derived in accordance with Poincaré. The asymptotic evaluation of the coeffcients of higher-degree terms is made on the basis of the theory of Darboux,and the proof begun in Volume I, Chapter 6,of Poincaré's theorem on the nonexistence of uniform integrals is completed.

Chapter 8 is dedicated to the first classical method of perturbation, that of Lagrange - variation of elements - with its application to the motion of the major planets (Le Verrier), to motion in resisting media in the light of cosmogonical hypotheses,and to the discussion of various proposed laws of gravitation designed to resolve the discrepancies in the secular variations of the orbits of the major planets. The motion of artificial earth satellites is touched upon as another application of Lagrange's method.Poisson's theorem on the invariability of the major axes and the Laplace-Lagrange theory of secular perturbations of eccentricities and inclinations are fully discussed in connection with the stability of the solar system in a certain sense.The secular variations of asteroidal orbits,in particular,are discussed with the genesis of astroids in mind, such as the asteroidal families. Gauss's method of computing secular variations is described in detail, with the modern modification that allows programming for computers.

Chapter 9 describes a purely analytical and literal expansion method, due to Delaunay, elegant in its formulation but lacking the rapidity of formal convergence. Delaunay's lunar theory is treated together with various attempts to explain the secular acceleration of the moon.The theory is applied to the discussion of libration among planetary and satellite motions. The commensurability case is fully worked out for the motions of asteroids and satelites.Brown's and von Zeipel's transformations for reducing the degree of freedom are described.Poincaré distinguished the analytical and numerical small divisors in Delaunay's lunar theory.Von Zeipel's method is applied to the motion of artificial earth satellites (in accordance with Brouwer) and a moon satellite. The diffculty of applying the method at critical inclination is discussed. The motion in an orbit of high eccentricity and inclination is analyzed by von Zeipel's method.Motion in the field of geopotential expanded in tesseral harmonics is treated.

Chapter l0 (Volume II, Part 2) deals with absolute perturbations of coordinates, beginning with the methods of special perturbations.The perturbation theories of Hansen, Newcomb, Gylden, Brendel, Andoyer, and others are described,with application to actual celestial bodies. Brown's theory of the eighth satellite of Jupiter is explained.The sphere of activity,the capture hypotheses,and the Poincaré-Schwarzschild theorem are discussed with a view to learning the origin of comets and their disintegration.A new approach by a method ofmatching conics for interplanetary trajectories is touched upon.A particular theory of Bohlin is described.Finally, the solution by series proceeding in positive integral powers of time - the so-called Lambert's series-is discussed, in accordance with Charlier and Steffensen.The modern concepts of the Lie transforms and the polynomial expansions are dealt with.

Chapter 11 is devoted to Hill's lunar theory - which has beena new dawn in celestial mechanics - with its ingenious device of adopting a periodic orbit as the intermediary orbit for the motion of the moon. Special attention is paid to the convergence of the expansions for the intermediary orbit.The classical method of treating the effects of the earth's figure and planetary action on the motion of the moon is described.Adams's theorem is discussed.Finally Hill's theory is applied to the motion of Jupiter's satellites.

Volume III will take up the discussion of Hill's infinite determinant and the solution of linear differential equations with periodic coeffcients. Another topic will be the modern tendency to apply the Krylov-Bogoliubov averaging method (originally devised for electric circuits) and Diliberto's periodic surface theory to the motion of artificial celestial bodies,with estimation of errors.The main topic, however,will be the form of the integrals in the planetary theory and the convergence. Liapounov stability will also be discussed.

Volume IV will deal with periodic, quasi-periodic,and asymptotic solutions in general, and Volume V with topological theories.

# Contents

# VOLUME II, PART 1

Chapter 7 Disturbing Function 1   
LAPLACE COEFFICIENTS 1   
7.1 Definition 1   
7.2 Integral Representation 4   
7.3 Recurrence Formulas 8   
7.4 Derivatives 10   
7.5 Numerical Tables 16   
INCLINED CIRCULAR ORBITS 23   
7.6 Jacobi's Expansion 23   
7.7 Tisserand'sPolynomials 28   
7.8 Hansen-Tisserand Polynomials 32   
7.9 Double Hypergeometric Series 36   
NEWCOMB'S OPERATORS 40   
7.10 Newcomb's Expansion 40   
7.11 Newcomb's Operators 43   
7.12 Poincaré's Recurrence Formulas 47   
7.13 Hill's Expansion 51   
7.14 Gylden's Expansion 53   
7.15 Brown's Expansion 55   
CONVERGENCE CRITERIA 58   
7.16 Sundman's Criterion 58   
7.17 Sundman's Proof 60   
7.18 A Generalization 67   
7.19 Part's iire'srtion 7

RECURRENCE RELATIONS 7.21 Recurrence Formulas 7.22 Application to the Disturbing Function 7.23 Case of Two Circular Orbits

# APPROXIMATION TO HIGHER COEFFICIENTS

v   
7.24 Method of Darboux 90   
7.25 Principle of Darboux's Method 93   
7.26 Motion on a Plane 98   
7.27 Case of One Circular Orbit 101   
7.28 Application of Darboux's Method 108   
7.29 Two Elliptic Orbits 112   
7.30 Nonexistence of Uniform Integrals 116

# Chapter 8 Lagrange's Method 128

VARIATION OF THE ELEMENTS 128   
8.1 Principle of the Method 128   
8.2 Form of the Solution 133   
8.3 Perturbation of Heliocentric Coordinates 137   
8.4 Discovery of Neptune and Pluto 142   
8.5 Motion under Resistance 145   
8.6 Motion of an Earth Satellite 149   
POISSON'S THEOREM 164   
8.7 Equations of Motion 164   
8.8 First-Order Perturbation 167   
8.9 Second-Order Perturbation 167   
8.10 Third-and Higher-Order Perturbation 169   
LAPLACE-LAGRANGE THEORY OF SECULAR   
PERTURBATION 174   
8.11 Classical Theory 174   
8.12 Secular Determinant 178   
8.13 Laplace-Lagrange Solution 180   
8.14 Computations of Stockwell and Brouwer 185

SECULAR VARIATION OF ASTEROIDAL ORBITS 187

8.15 Formal Solution 187   
8.16 Family of Asteroids 190   
8.17 Critical Asteroid 193   
8.18 Commensurability of Higher Orders 198

GAUSS's METHOD 199

3.19 Gauss's Method 199

8.22 Halphen-Musen Method 216

# DISCUSSION OF THE LAW OF GRAVITATION

8.23 Historical Note   
8.24 Discussion of Various Laws   
8.25 Relativistic Theory

# Chapter 9 Delaunay's Theory

DELAUNAY'S METHOD 9.1 Delaunay's Operations 9.2 Delaunay's Lunar Theory 9.3 Secular Acceleration

THEORY OF LIBRATION 9.4 Commensurability of Mean Motions 9.5 Poincare's Theory 9.6 Commensurability of the First Rank 9.7 Critical Argument 9.8 Brown's Theory 9.9 Distribution of Asteroids MOTION OF SATELLITES   
9.10 Souillart's Theory of Jupiter's Satellites   
9.11 Saturn's Satellites   
9.12 Woltjer's Theory of Hyperion   
9.13 Consideration of Satellite Orbits BROWN'S TRANSFORMATION   
9.14 Brown's Transformation   
9.15 Application of Brown's Transformation to a Stellar Case   
9.16 Apse-Node Terms POINCARE'S THEORY   
9.17 Poincaré's Formulation   
9.18 Small Divisors VON ZEIPEL'S THEORY   
9.19 Von Zeipel's Transformation   
9.20 Brouwer's Theory of an Artificial Satellite   
9.21 Garfinkel's Improved Theory   
9.22 Critical Inclination   
9.23 Effect of Air Drag   
9.24 Brouwer's Discussion of the Asteroidal Gaps   
9.25 Orbit with High Inclination and Eccentricity   
9.26 Twenty-Four-Hour Earth Satellites   
9.27 Lunar Orbiter   
9.28 Von Zeipel's Theory applied to Jupiter's Satellites

# 9.29General Perturbation with Unspecifed Canonical

Variables 479   
VOLUME II, PART 2   
Chapter 10 Absolute Perturbation 505   
COORDINATE PERTURBATION 505   
10.1 Perturbation in Rectangular Coordinates 505   
10.2 Hill's Method 512   
10.3 Brouwer's Method 517   
10.4 Stromgren'sMethod 525   
10.5 The Hansen-Tietjen Method 547   
HANSEN'S THEORY 552   
10.6 Ideal Coordinates 552   
10.7 Hansen's Method of Integration 555   
10.8 Motion of the Orbital Plane 560   
10.9 Disturbing Function 565   
10.10 Musen's Modification of Hansen's Theory 568   
10.11 Group Perturbations 591   
10.12 Hansen's Method Applied to Comets 594   
10.13 Oppolzer's Lunar Theory 599   
NEWCOMB'S THEORY 604   
10.14 Laplace's Theory 604   
10.15 Newcomb's Equations of Motion 607   
10.16 Perturbation in Longitude 612   
10.17 Motion of the Orbital Plane 613   
GYLDEN'S THEORY 617   
10.18 Gyldén's Intermediary Orbit 617   
10.19 Heuristic Method 618   
10.20 Characteristic Terms 624   
10.21 Brendel's Modification 631   
10.22 Brendel's Lunar Theory 639   
BROWN'S THEORY 644   
10.23 Equations of Motion for a Trojan Asteroid 644   
10.24 Brown's Intermediary Orbit 648   
10.25 Equation for Variation 651   
10.26 Planetary Perturbation 655   
10.27 Brown's Revised Theory 658   
10.28 Brown's Theory of Jupiter's Eighth Satellite 661   
10.29 Kovalevsky's Numerical Method 668   
ANDOYER'S THEORY 678   
10.30 Andoyer's Lunar Theory 678   
10.31Paloque's Theory of a Trojan Asteroid 683   
10.32 Trousset's Theory of J VIII 687   
10.33 Roure's Theory of Planets 689   
COMETARY PERTURBATION 695   
10.34 Sphere of Activity 695   
10.35 Capture of a Comet by Jupiter 703   
10.36 The Poincaré-Schwarzschild Theorem 707   
10.37 Interplanetary Trajectories 713   
10.38 Disintegration of a Comet 734   
BOHLIN'S THEORY 739   
10.39 Bohlin's Quintic Equation 739   
10.40 Auxiliary Functions 743   
10.41 Analytical Expansion 748   
SOLUTION BY LAMBERT'S SERIES 755   
10.42 Charlier's Theory 755   
10.43 Steffensen's Theory 760   
10.44 The Lie Transform 769   
10.45 Expansions in Polynomial Series 773   
Chapter 11 Hill's Lunar Theory 805   
HILL'S INTERMEDIARY ORBIT 805   
11.1 Hill's Equations of Motion 805   
11.2 Intermediary Orbit 810   
11.3 Variational Curve 816   
11.4 Convergence for a Variational Curve 821   
THE MOTION OF PERIGEE AND NODE 849   
11.5 Equations for Variations 849   
11.6 Terms Depending on m and $\pmb { e }$ 865   
11.7 Other Inequalities 870   
11.8 Convergence of Hil's Series 877   
THE PLANETARY ACTIONS 880   
11.9 Action due to Planets 880   
11.10 Inequality due to the Earth's Figure 886   
11.11 Adams's Theorem 88g   
APPLICATION TO JUPITER'S SATELLITES 905   
11.12 Ferraz Mello's Theory 905   
Retrospect of Volume II 921   
Index to Volume II, Part 1 and Volume I1,   
Part 2. following pp. 504, 921

# Absolute Perturbation

# COORDINATE PERTURBATION

# I0.IPERTURBATION IN RECTANGULAR COORDINATES

The perturbation theory treated in the foregoing chapters deals with the variation of elements due to perturbation. The method of computing the effects of the perturbation directly on the coordinates themselves is called the absolute perturbation method,or sometimes the direct method,in contrast to the indirect method of computation through the intermediary of the elements.The method of the variation of elements fails for an orbit with large eccentricity,such as a periodic comet of long period.In 1760 Clairaut tried a numerical method for computing the motion of Halley's comet.Damoiseaux, Pontécoulant,and Rosenberger each presented to the Paris Academy of Sciences as a prize essay a method for predicting the return in 1835 of this comet.At the time of the next return in 1910, Cowell and Crommelin devised a method for computing the disturbed coordinates numerically by solving the equations of motion. Several methods were proposed for computing the rectangular coordinates, such as Encke's and Bond's, and for computing the polar coordinates, such as Hansen's,Brunnow's,Tietzen's,and Oppolzer's.Encke's method is more convenient for a short-period comet.For an asteroid with small eccentricity and small inclination,the method of the variation of elements is often employed by integrating numerically the differential equations (175) of Section 5.18,or (1) of Section 8.1,or (la) of Section 8.5. These methods are called the special perturbation method, in contrast to the general perturbation method, which deals with the purely literal analytical solution of the differential equations such as Lagrange's or Delaunay's. The method of special perturbation for the variation of elements was simplified by Stracke (1924,1929,1929a,1930) and others, because of its frequent application to a great number of asteroids. We now consider the coordinate perturbation method.

Let ${ \pmb x } = { \pmb x } _ { 0 } + { \pmb \xi }$ stand in general for one of the disturbed rectangular coordinates, where $\pmb { \xi }$ denotes the perturbation in that coordinate.The differential equation of motion for the coordinate, taking one coordinate as representative, is

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } + \frac { d ^ { 2 } \xi } { d t ^ { 2 } } ,
$$

where

$$
\frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } = - k ^ { 2 } ( 1 + m ) \frac { x _ { 0 } } { r _ { 0 } ^ { 3 } } , \qquad r _ { 0 } ^ { 2 } = x _ { 0 } ^ { 2 } + y _ { 0 } ^ { 2 } + z _ { 0 } ^ { 2 } .
$$

From these we obtain

$$
\frac { d ^ { 2 } \xi } { d t ^ { 2 } } = \sum k ^ { 2 } m _ { 1 } \bigg [ \frac { x _ { 1 } - x } { \rho ^ { 3 } } - \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } \bigg ] + k ^ { 2 } ( 1 + m ) \bigg [ \frac { x _ { 0 } } { r _ { 0 } ^ { 3 } } - \frac { x } { r ^ { 3 } } \bigg ] ,
$$

where $m _ { 1 } , x _ { 1 } , y _ { 1 } , z _ { 1 } , r _ { 1 }$ are the mass, the three rectangular coordinates, and the heliocentric distance,respectively,ofone ofthe disturbing bodies, and $\pmb { \rho }$ is the mutual distance between the disturbed and the disturbing bodies. Then

$$
\begin{array} { r } { r ^ { 2 } = r _ { 0 } ^ { 2 } + ( 2 x _ { 0 } + \xi ) \xi + ( 2 y _ { 0 } + \eta ) \eta + ( 2 z _ { 0 } + \zeta ) \zeta + \cdot \cdot \cdot . } \end{array}
$$

Cowel's method is to integrate these equations numerically as they stand.

In accordance with Encke, let

$$
\frac { r ^ { 2 } } { r _ { 0 } ^ { 2 } } = 1 + 2 q ;
$$

then,

$$
\begin{array} { c } { { \displaystyle { \frac { x _ { 0 } } { r _ { 0 } ^ { 3 } } - \frac { x } { r ^ { 3 } } = \frac { 1 } { r _ { 0 } ^ { 3 } } ( f q x - \xi ) , } } } \\ { { \displaystyle { f = 3 \biggl [ 1 - \frac { 5 } { 2 } q + \frac { 5 \cdot 7 } { 2 \cdot 3 } q ^ { 2 } - \frac { 5 \cdot 7 \cdot 9 } { 2 \cdot 3 \cdot 4 } q ^ { 3 } + \cdot \cdot \cdot \biggr ] . } } } \end{array}
$$

Hence the differential equation for the disturbed coordinate is

$$
{ \frac { d ^ { 2 } \xi } { d t ^ { 2 } } } = k ^ { 2 } \sum m _ { 1 } \bigg ( { \frac { x _ { 1 } - x } { \rho ^ { 3 } } } - { \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } } \bigg ) + { \frac { k ^ { 2 } } { r _ { 0 } ^ { 3 } } } ( f q x - \xi ) ;
$$

or, writing

$$
{ \frac { k ^ { 2 } } { \ell ^ { 2 } } } = h , \qquad \sum k ^ { 2 } m _ { 1 } \biggl ( { \frac { x _ { 1 } - x } { \rho ^ { 3 } } } - { \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } } \biggr ) = \sum ( X ) ,
$$

we obtain

$$
\frac { d ^ { 2 } \xi } { d t ^ { 2 } } + h \xi = \sum \left( X \right) + h f q x .
$$

For a first approximation we put $f = 3$ and integrate the equation (1) numerically. Let ${ \pmb w }$ be the interval of the argument in the numerical integration, and, with the second sum $^ { \mathrm { t r } } f$ and the second difference $f ^ { \mathrm { { I I } } }$ ， write, after Bauschinger (1928),

$$
S _ { ( x ) } = \mathbb { \pi } f _ { ( x ) } ( a + i w ) + \frac { 1 } { 1 2 } \sum \big ( X \big ) - \frac { 1 } { 2 4 0 } f _ { ( x ) } ^ { \mathrm { { \scriptsize { T } } } } ( a + i w ) ,
$$

where

$$
f ( a + i w ) = \frac { d ^ { 2 } } { d t ^ { 2 } } \ : \xi ( a + i w ) \qquad ( i = 0 , 1 , 2 , . . . ) ;
$$

then the double integral $\xi$ is written in the form

$$
\begin{array} { r } { \xi = S _ { ( x ) } + \frac { 1 } { 1 2 } h f g x - \frac { 1 } { 1 2 } h \xi . } \end{array}
$$

Put

$$
a = \frac { x _ { 0 } + \frac { 1 } { 2 } \xi } { r _ { 0 } ^ { 2 } ( 1 + \frac { 1 } { 1 2 } h ) } , \qquad b = \frac { y _ { 0 } + \frac { 1 } { 2 } \eta } { r _ { 0 } ^ { 2 } ( 1 + \frac { 1 } { 1 2 } h ) } , \qquad c = \frac { z _ { 0 } + \frac { 1 } { 2 } \zeta } { r _ { 0 } ^ { 2 } ( 1 + \frac { 1 } { 1 2 } h ) } ;
$$

then

$$
q = \frac { a S _ { ( x ) } + b S _ { ( y ) } + c S _ { ( z ) } } { 1 - \frac { 1 } { 1 2 } h f ( a x + b y + c z ) } \cdot
$$

By inserting the first approximate values of $x , y , z$ in the right-hand member we obtain $\pmb q$ Then,

$$
\frac { d ^ { 2 } \xi } { d t ^ { 2 } } = \sum \left( X \right) + h ^ { \prime } [ f q x - S _ { ( x ) } ] , h ^ { \prime } = \frac { h } { 1 + \frac { 1 } { 1 2 } h } .
$$

This is Encke's method (1854).The osculating elements can be computed from these disturbed coordinates. Some simplifications are made by neglecting the squares and products of the coordinate perturbations $\xi _ { : }$ $\pmb { \eta }$ and $\boldsymbol { \zeta }$ (Oppolzer, 1880; Watson, 1900; Bauschinger, 1928； Stracke, 1929;Herget, 1948; Dubiago,1961). Brünnow (1865) modified Encke's method and applied it to the motion of the asteroids Iris and Flora.

Wilkens (1932) improved the method for computing the perturbation of a Trojan-group asteroid.Rasmusen (l951） published a table for Encke's function fq. Hall, Gawlowicz,and Wallman (l96l） employed Encke's method for the motion of an earth satellite affected by oblateness and drag (Section 8.6).Kyner and Bennett (1966) and Born (1970) modified the classical Encke method for integrating the equations of motion of a near-earth satellite so that the intermediary,which they call nominal, and the instantaneous orbits are forced to remain close to each other for many revolutions,by making the nominal ellipse rotate slowly in a plane which is in turn rotating slowly in space.

Herget (1947) improved the computation of $( f q x - \xi ) r _ { 0 } ^ { - 3 }$ in Encke's technique, because the difference of two large numbers causes inconvenience for numerical work. Herget put, in the place of $_ x$ ${ \ : , } x _ { 0 } , \xi$ of Encke,

$$
\begin{array} { c } { { \left[ x \right] = \left( x \right) + x , \qquad \left[ y \right] = \left( y \right) + y , \qquad \left[ z \right] = \left( z \right) + z , } } \\ { { ( r ) ^ { 2 } = \left( x \right) ^ { 2 } + ( y ) ^ { 2 } + ( z ) ^ { 2 } , } } \end{array}
$$

and

$$
\begin{array} { l } { { q = \frac { \frac { 1 } { 2 } r ^ { 2 } + ( x ) x + ( y ) y + ( z ) z } { ( r ) ^ { 2 } } , } } \\ { { \ } } \\ { { h = m _ { 1 } \frac { ( w k ) ^ { 2 } } { r ^ { 3 } } , \ ~ ( h ) = m _ { 1 } \frac { ( w k ) ^ { 2 } } { ( r ) ^ { 3 } } , } } \end{array}
$$

and obtained

$$
\begin{array} { c } { { f _ { x } = - m _ { 1 } \displaystyle \frac { ( w k ) ^ { 2 } } { r ^ { 3 } } x - ( w k ) ^ { 2 } \biggl \{ \frac { [ x ] } { [ r ] ^ { 3 } } - \frac { ( x ) } { ( r ) ^ { 3 } } \biggr \} } } \\ { { = \{ ( h ) f q - ( h ) - h \} x + ( h ) f q ( x ) . } } \end{array}
$$

In general, from the interpolation formula we have

$$
f ( a + w ) = f ( a ) + f ^ { \tt T } ( a - \textstyle { \frac { 1 } { 2 } } w ) + f ^ { \tt I I } ( a ) + \cdot \cdot \cdot ,
$$

and, from Taylor's theorem,

$$
f ( a + i w ) = f ( a ) + i { \frac { d f ( a ) } { d t } } + { \frac { i ^ { 2 } } { 1 \cdot 2 } } { \frac { d ^ { 2 } f ( a ) } { d t ^ { 2 } } } + \cdot \cdot \cdot .
$$

Hence the second difference is

$$
\begin{array} { l } { { f ^ { \mathrm { { I I } } } ( a ) = w ^ { 2 } { \displaystyle \frac { d ^ { 2 } f ( a ) } { d t ^ { 2 } } } + \rho , } } \\ { { \displaystyle \rho = \frac { 2 } { 4 ! } w ^ { 4 } { \displaystyle \frac { d ^ { 4 } f ( 0 ) } { d t ^ { 4 } } } + \frac { 2 } { 6 ! } w ^ { 6 } { \displaystyle \frac { d ^ { 6 } f ( 0 ) } { d t ^ { 6 } } } + \cdot \cdot \cdot . } }  \end{array}
$$

From Newton's backward interpolation formula we have

$$
\begin{array} { l } { { f ( a + i w ) = f ( a ) + i f ^ { \mathrm { r } } \Big ( a - \frac { 1 } { 2 } w \Big ) + \frac { i ( i + 1 ) } { 1 \cdot 2 } f ^ { \mathrm { r t } } ( a - w ) } } \\ { { + \frac { i ( i + 1 ) ( i + 2 ) } { 3 ! } f ^ { \mathrm { r t } } \Big ( a - \frac { 3 } { 2 } w \Big ) \ . } } \end{array}
$$

Diferentiate this formula and substitute it in the expression for $\rho$ ; then,

$$
\begin{array} { r c l } { { f ^ { \mathrm { I I } } ( a ) = w ^ { 2 } { \frac { d ^ { 2 } f ( 0 ) } { d t ^ { 2 } } } + { \frac { 1 } { 1 2 } } f ^ { \mathrm { I V } } ( a - 2 w ) + { \frac { 1 } { 6 } } f ^ { \mathrm { v } } \Bigl ( a - { \frac { 5 } { 2 } } w \Bigr ) } } \\ { { } } & { { } } \\ { { } } & { { } } & { { + { \frac { 4 3 } { 1 8 0 } } f ^ { \mathrm { v I } } ( a - 3 w ) ~ . } } \end{array}
$$

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = F ( x , t )
$$

is the given differential equation to be integrated numerically, then

$$
\rho = \frac { 2 } { 4 ! } w ^ { 2 } \frac { d ^ { 2 } F } { d t ^ { 2 } } + \frac { 2 } { 6 ! } w ^ { 4 } \frac { d ^ { 4 } F } { d t ^ { 4 } } + \frac { 2 } { 8 ! } w ^ { 6 } \frac { d ^ { 6 } F } { d t ^ { 6 } } + \cdot \cdot \cdot ,
$$

or

$$
\begin{array} { c } { { { \pi } ( a ) = F ( a ) + { \frac { 1 } { 1 2 } } F ^ { \pi } ( a - w ) + { \frac { 1 } { 1 2 } } F ^ { \pi } ( a - { \frac { 3 } { 2 } } w ) } } \\ { { + { \frac { 1 9 } { 2 4 0 } } F ^ { \pi } ( a - 2 w ) + { \frac { 3 } { 4 0 } } F ^ { \nu } ( a - { \frac { 5 } { 2 } } w ) + } } \end{array}
$$

This is Stormer's method, by which the trajectories of a charged particle in the earth's magnetic field have been calculated. The accuracy of Stormer's method was estimated by Miachin (1964).

We have Stirling's interpolation formula

$$
\begin{array} { c } { { ( a + i w ) = f ( a ) + i f ^ { \mathrm { \tiny { I } } } ( a ) + \displaystyle \frac { i ^ { 2 } } { 1 \cdot 2 } f ^ { \mathrm { \tiny { I I } } } ( a ) + \displaystyle \frac { i ( i ^ { 2 } - 1 ^ { 2 } ) } { 1 \cdot 2 \cdot 3 } f ^ { \mathrm { \tiny { I I I } } } ( a ) } } \\ { { + \displaystyle \frac { i ^ { 2 } ( i ^ { 2 } - 1 ^ { 2 } ) } { 4 ! } f ^ { \mathrm { \tiny { I V } } } ( a ) + } } \end{array}
$$

By a similar procedure we obtain

$$
f ^ { \mathrm { I I } } ( a ) = w ^ { 2 } \frac { d ^ { 2 } f ( a ) } { d t ^ { 2 } } + \frac { 1 } { 1 2 } f ^ { \mathrm { I V } } ( a ) - \frac { 1 } { 9 0 } f ^ { \mathrm { V I } } ( a ) + \frac { 1 } { 5 6 0 } f ^ { \mathrm { V I I } } ( a ) + \cdot \cdot \cdot ,
$$

or

$$
\begin{array} { r } { f ^ { \mathrm { \tt T } } ( a ) = F _ { 0 } + \frac { 1 } { 1 2 } F ^ { \mathrm { \tt I I } } ( a ) - \frac { 1 } { 2 4 0 } F ^ { \mathrm { \tt I V } } ( a ) + \frac { 3 1 } { 6 0 4 8 0 } F ^ { \mathrm { \tt V I } } ( a ) + \cdot \cdot \cdot . } \end{array}
$$

This is Cowelland Crommelin's method by which the orbit of Halley's comet for the returns in 1759,1835,and 1910 was computed (Cowell and Crommelin,1907,1908,1908a,1910). The same method was applied to the motion of the eighth satelite of Jupiter (Cowell and Crommelin, 1908b). The special perturbation by Cowell's integration method was adapted to a Hellerith computing machine by Eckert (1935).

Define $\pmb { \bar { x } }$ by

$$
\widetilde { x } = x - \frac { 1 } { 1 2 } w ^ { 2 } \frac { d ^ { 2 } x } { d t ^ { 2 } } = x - \frac { 1 } { 1 2 } w ^ { 2 } { \cal F } ( x , t ) ;
$$

then the diference is writen,for the new variable $\pmb { \bar { x } }$

$$
\begin{array} { l } { { \displaystyle { \overline { { f ^ { \mathrm { I I } } } } } ( a ) = w ^ { 2 } \frac { d ^ { 2 } } { d t ^ { 2 } } f ( a ) + \bar { \rho } } } \\ { { \displaystyle \bar { \rho } = - \sum _ { k = 6 , 8 , 1 0 } A _ { k } w ^ { k } \frac { d ^ { k } } { d t ^ { k } } f ( a ) } , \ ~ } \\ { { \displaystyle A _ { k } = \frac { 2 } { k ! } \left[ \frac { k ( k - 1 ) } { 1 2 } - 1 \right] } , \ ~ } \end{array}
$$

or

$$
\begin{array} { c } { \displaystyle { \tilde { \rho } = \sum _ { k = 6 , 8 , 1 0 } B _ { k } w ^ { k } \frac { d ^ { k } } { d t ^ { k } } f ( a ) , } } \\ { \displaystyle { B _ { k } = A _ { k } + \frac { A _ { k - 2 } } { 1 2 } + \frac { A _ { k - 4 } } { 1 2 ^ { 2 } } + \cdots + \frac { A _ { 6 } } { 1 2 ^ { ( k - 6 ) / 2 } } } . } \end{array}
$$

If we start with Newton's backward interpolation formula, then $\bar { \pmb \rho }$ becomes

$$
\begin{array} { r } { = - \frac { 1 } { 2 4 0 } \overline { { f ^ { \mathrm { V I } } ( a - 3 w ) } } - \frac { 1 } { 8 0 } \overline { { f ^ { \mathrm { V I I } } ( a - \frac { 7 } { 2 } w ) } } - \frac { 2 9 6 2 } { 1 2 0 9 6 0 } \overline { { f ^ { \mathrm { V I I } } ( a - 4 w ) } } , } \end{array}
$$

where the bar over a functionfindicates that thecorresponding difference is to be taken in the argument of the modified variable $\pmb { \bar { x } } .$ If we start with Stirling's formula, then

$$
\begin{array} { r } { \bar { \rho } = - \frac { 1 } { 2 4 0 } \overline { { f ^ { \nabla \mathrm { I } } ( a ) } } + \frac { 3 1 } { 6 0 4 8 0 } \overline { { f ^ { \nabla \mathrm { I I I } } ( a ) } } + \cdot \cdot \cdot . } \end{array}
$$

Evidently these series converge rapidly. This is Numerov's method, which embodies both his own methods of orbit determination and special perturbation (Numerov,1923,1924, 1926,1927, 1928). Commendantov (1931） applied the method to the motion of asteroids.

Let the equations of motion be

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } = - \frac { k ^ { 2 } x } { r ^ { 3 } } + \frac { 1 } { w ^ { 2 } } R , } } \\ { { R = k ^ { 2 } w ^ { 2 } \displaystyle \sum m _ { i } \biggl ( \frac { x _ { i } - x } { \rho _ { i } ^ { 3 } } - \frac { x _ { i } } { r _ { i } ^ { 3 } } \biggr ) . } } \end{array}
$$

Write

$$
\bar { x } = x - \frac { 1 } { 1 2 } w ^ { 2 } \frac { d ^ { 2 } x } { d t ^ { 2 } } + \frac { R } { 1 2 } ;
$$

then,

$$
\begin{array} { r l r } & { } & { \bar { x } = x \Big ( 1 + \frac { k ^ { 2 } w ^ { 2 } } { 1 2 r ^ { 3 } } \Big ) , } \\ & { } & \\ & { } & { \overline { { f ^ { \mathrm { I I } } ( a ) } } = w ^ { 2 } \frac { d ^ { 2 } f ( a ) } { d t ^ { 2 } } + \rho _ { 0 } + \frac { 1 } { 1 2 } \Delta ^ { \mathrm { I I } } ( R ) . } \end{array}
$$

From the equations of motion and the expression for $\bar { x }$ we obtain

$$
\begin{array} { r l r } {  { \overline { { f ^ { \mathrm { I I } } ( a ) } } = - \sigma _ { 0 } \bar { x } + \delta _ { 0 } , } } \\ & { } & { \delta _ { 0 } = R _ { 0 } + \rho _ { 0 } + \frac { 1 } { 1 2 } \Delta _ { 0 } ^ { \mathrm { I I } } ( R ) , } \\ & { } & { \sigma _ { 0 } = \frac { k ^ { 2 } w ^ { 2 } } { r _ { 0 } ^ { 3 } } \Big / \Big ( 1 + \frac { k ^ { 2 } w ^ { 2 } } { 1 2 r _ { 0 } ^ { 3 } } \Big ) , ~ } \\ & { } & { \rho _ { 0 } = - \frac { 1 } { 2 4 0 } w ^ { 6 } f ^ { \mathrm { V I } } ( a ) - \frac { 1 1 } { 6 0 4 8 0 } w ^ { 8 } f ^ { \mathrm { V I I I } } ( a ) + \cdot \cdot \cdot , } \end{array}
$$

where $\sigma$ is given as a function of $\pmb { r }$ in the form

$$
\bar { r } = r \biggl ( 1 + \frac { k ^ { 2 } w ^ { 2 } } { 1 2 r ^ { 3 } } \biggr ) .
$$

Thus,

$$
\sigma \Big ( 1 - \frac { \sigma } { 1 2 } \Big ) ^ { 2 } = \lambda = \frac { k ^ { 2 } w ^ { 2 } } { \bar { r } ^ { 3 } } ,
$$

or

$$
\sigma = \lambda + { \textstyle \frac { 1 } { 6 } } \lambda ^ { 2 } + { \textstyle \frac { 7 } { 1 4 4 } } \lambda ^ { 3 } + { \textstyle \frac { 5 } { 2 8 8 } } \lambda ^ { 4 } + { \textstyle \frac { 1 4 3 } { 2 0 7 3 6 } } \lambda ^ { 5 } + \cdot \cdot \cdot .
$$

Hence the fundamental formula for extrapolation is

$$
{ \overline { { f ( a + w ) } } } = ( 2 - \sigma _ { 0 } ) { \overline { { f ( a ) } } } - { \overline { { f ( a - w ) } } } + \delta _ { 0 } ,
$$

where $\delta _ { \rho }$ consists of the value $R _ { 0 }$ of $R$ at $t = a$ ,the insignificant effects of the derivatives and the differences of higher orders, and $\scriptstyle { \frac { 1 } { 1 2 } }$ of the insignificant second difference of $R$ .This method converges satisfactorily rapidly. The practical comparison of various methods - variation of elements,and Cowell's, Encke's,and Numerov's methods - has been discussed by Herget (1947,l952),Kline and Herget (l94l),Kahrstedt (1951),Kühne (l95l),Hintze (l952),Porter (1958),and Baker et al. (1960) for an earth satellite.

For solving a differential equation numerically, Runge-Kutt's method is usually referred to (Runge and K5nig, l924; Collatz, l95l). There is a problem in changing the integration steps in the numerical integration of differential equations (Miachin,196l,1964).Subbotin (1965) studied the accuracy of the computation of the ephemerides of the inner planets, and Foursenko (l965) discussed the moon's ephemerides on the basis of Brown's expansions (discussed in Chapter 11) and estimated the accuracy of the moon's coordinates. Filippi (l966) discussed the accuracy of the method of Runge-Kutta-Fehlberg in the solution of the $\pmb { n }$ -body problem.

# 10.2HILL'S METHOD

Hill(1874) proposed a new method of computingdisturbed rectangular coordinates.Put

$$
\begin{array} { r } { x = x _ { 0 } + \xi , ~ y = y _ { 0 } + \eta , ~ z = z _ { 0 } + \zeta , ~ } \\ { r = r _ { 0 } + \rho , ~ r _ { 0 } ^ { 2 } = x _ { 0 } ^ { 2 } + y _ { 0 } ^ { 2 } + z _ { 0 } ^ { 2 } ; ~ } \end{array}
$$

then the equations of the disturbed motion are

$$
\begin{array} { r l r } & { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } + \frac { \mu x } { r ^ { 3 } } = \frac { \partial R } { \partial x } , } & { \quad \displaystyle \frac { d ^ { 2 } y } { d t ^ { 2 } } + \frac { \mu y } { r ^ { 3 } } = \frac { \partial R } { \partial y } , } \\ & { \displaystyle \frac { d ^ { 2 } z } { d t ^ { 2 } } + \frac { \mu z } { r ^ { 3 } } = \frac { \partial R } { \partial z } , } & { \quad \displaystyle \mu = k ^ { 2 } ( m _ { 0 } + m ) , } \end{array}
$$

and those of the undisturbed motion are

$$
\frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } + \frac { \mu x _ { 0 } } { r _ { 0 } ^ { 3 } } = 0 , ~ \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } + \frac { \mu y _ { 0 } } { r _ { 0 } ^ { 3 } } = 0 , ~ \frac { d ^ { 2 } z _ { 0 } } { d t ^ { 2 } } + \frac { \mu z _ { 0 } } { r _ { 0 } ^ { 3 } } = 0 .
$$

Combining these, we obtain

$$
\begin{array} { l } { { \displaystyle \frac { d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } } { d t ^ { 2 } } - \frac { 2 \mu } { r } + \frac { \mu } { a } = 2 \int d R , } } \\ { { \displaystyle \frac { d x _ { 0 } ^ { 2 } + d y _ { 0 } ^ { 2 } + d z _ { 0 } ^ { 2 } } { d t ^ { 2 } } - \frac { 2 \mu } { r _ { 0 } } + \frac { \mu } { a } = 0 . } } \end{array}
$$

From (2), (3),and (3a) we have

$$
{ \frac { 1 } { 2 } } { \frac { d ^ { 2 } r ^ { 2 } } { d t ^ { 2 } } } - { \frac { \mu } { r } } + { \frac { \mu } { a } } = 2 \int d R + r { \frac { \partial R } { \partial r } } ,
$$

and

$$
{ \frac { d ^ { 2 } ( r _ { 0 } \rho ) } { d t ^ { 2 } } } + { \frac { \mu } { r _ { 0 } ^ { 3 } } } r _ { 0 } \rho = 2 \int d R + r { \frac { \partial R } { \partial r } } - { \frac { 1 } { 2 } } { \frac { d ^ { 2 } \rho ^ { 2 } } { d t ^ { 2 } } } + { \frac { \mu \rho ^ { 2 } } { r _ { 0 } ^ { 2 } r } } .
$$

The equations (2) are transformed to

$$
\begin{array} { r } { \frac { d ^ { 2 } \xi } { d t ^ { 2 } } + \frac { \mu \xi } { r _ { 0 } ^ { 3 } } = \frac { \partial R } { \partial x } + \bigl ( \frac { 1 } { r _ { 0 } ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \bigr ) \mu x , } \\ { \frac { d ^ { 2 } \eta } { d t ^ { 2 } } + \frac { \mu \eta } { r _ { 0 } ^ { 3 } } = \frac { \partial R } { \partial y } + \bigl ( \frac { 1 } { r _ { 0 } ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \bigr ) \mu y , } \\ { \frac { d ^ { 2 } \zeta } { d t ^ { 2 } } + \frac { \mu \zeta } { r _ { 0 } ^ { 3 } } = \frac { \partial R } { \partial z } + \bigl ( \frac { 1 } { r _ { 0 } ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \bigr ) \mu z . } \end{array}
$$

Put

$$
Q _ { r } = 2 \int d R + r \frac { \partial R } { \partial r } - \frac { 1 } { 2 } \frac { d ^ { 2 } \rho ^ { 2 } } { d t ^ { 2 } } + \frac { \mu \rho ^ { 2 } } { r _ { 0 } ^ { 2 } r } ,
$$

$$
Q _ { x } = { \frac { \partial R } { \partial x } } + { \biggl ( } { \frac { 1 } { r _ { 0 } ^ { 3 } } } - { \frac { 1 } { r ^ { 3 } } } { \biggr ) } \mu x , \qquad Q _ { y } = { \frac { \partial R } { \partial y } } + { \biggl ( } { \frac { 1 } { r _ { 0 } ^ { 3 } } } - { \frac { 1 } { r ^ { 3 } } } { \biggr ) } \mu y ;
$$

$$
Q _ { z } = { \frac { \partial R } { \partial z } } + \Big ( { \frac { 1 } { r _ { 0 } ^ { 3 } } } - { \frac { 1 } { r ^ { 3 } } } \Big ) \mu z ;
$$

then the equations of motion become

$$
\begin{array} { r } { \frac { d ^ { 2 } \left( r _ { 0 } \rho \right) } { d t ^ { 2 } } + \frac { \mu } { r _ { 0 } ^ { 3 } } r _ { 0 } \rho = Q _ { r } , } \end{array}
$$

$$
\begin{array} { c } { { d t ^ { 2 } { } ^ { - } \mathrm {  ~ \tau ~ } \overline { { { r _ { 0 } ^ { 3 } } } } ^ { \prime } \circ p = \check { \bf q } \tau , } } \\ { { \displaystyle \frac { d ^ { 2 } \xi } { d t ^ { 2 } } + \frac { \mu \xi } { r _ { 0 } ^ { 3 } } = Q _ { x } , ~ \frac { d ^ { 2 } \eta } { d t ^ { 2 } } + \frac { \mu \eta } { r _ { 0 } ^ { 3 } } = Q _ { y } , } } \\ { { \displaystyle \frac { d ^ { 2 } \zeta } { d t ^ { 2 } } + \frac { \mu \zeta } { r _ { 0 } ^ { 3 } } = Q _ { z } . } } \end{array}
$$

We know $\mu / r _ { 0 } ^ { 3 }$ as a function of $t$ from the properties of an elliptic motion.Denote the fundamental set of independent solutions of

$$
\frac { d ^ { 2 } q } { d t ^ { 2 } } + \frac { \mu q } { r _ { 0 } ^ { 3 } } = 0
$$

by $\pmb q _ { 1 }$ and $q _ { 2 }$ . Then the general solution is $q = k _ { 1 } q _ { 1 } + k _ { 2 } q _ { 2 }$ with arbitrary constants $k _ { 1 }$ and $k _ { 2 }$ .We have the integral

$$
\frac { q _ { 1 } d q _ { 2 } - q _ { 2 } d q _ { 1 } } { d t } = \mathrm { c o n s t a n t } .
$$

Then the solution of the nonhomogeneous equations (5) is

$$
\begin{array} { r l r } & { } & { \tau _ { 0 } \rho = q _ { 2 } \int q _ { 1 } Q _ { r } d t - \ q _ { 1 } \int q _ { 2 } Q _ { r } d t , } \\ & { } & \\ & { } & { \xi = q _ { 2 } \int q _ { 1 } Q _ { x } d t - \ q _ { 1 } \int q _ { 2 } Q _ { x } d t , } \\ & { } & \\ & { } & { \eta = q _ { 2 } \int q _ { 1 } Q _ { y } d t - \ q _ { 1 } \int q _ { 2 } Q _ { y } d t , } \\ & { } & \\ & { } & { \zeta = q _ { 2 } \int q _ { 1 } Q _ { z } d t - \ q _ { 1 } \int q _ { 2 } Q _ { z } d t . } \end{array}
$$

We have the check equation

$$
\begin{array} { r } { \begin{array} { r } { r _ { 0 } \rho = x _ { 0 } \xi + y _ { 0 } \eta + z _ { 0 } \zeta + \frac { 1 } { 2 } ( \xi ^ { 2 } + \eta ^ { 2 } + \zeta ^ { 2 } - \rho ^ { 2 } ) . } \end{array} } \end{array}
$$

The equations (8) contain nine arbitrary constants， including the additive constant to be put in $\int d R .$ But this last constant is.connected with the other eight by the relation

$$
\begin{array} { c } { \displaystyle \frac { d x _ { 0 } } { d t } \frac { d \xi } { d t } + \frac { d y _ { 0 } } { d t } \frac { d \eta } { d t } + \frac { d z _ { 0 } } { d t } \frac { d \zeta } { d t } + \frac { \mu } { r _ { 0 } ^ { 2 } r } r _ { 0 } \rho } \\ { \displaystyle { = \int d R - \frac { 1 } { 2 } \left[ \left( \frac { d \xi } { d t } \right) ^ { 2 } + \left( \frac { d \eta } { d t } \right) ^ { 2 } + \left( \frac { d \zeta } { d t } \right) ^ { 2 } \right] } , } \end{array}
$$

obtained from (9).

As shown by Hansen (see Sections l0.6-l0.9), the right-hand sides of (8) can be simplified. Denote the variable $\pmb { t }$ outside the integral signs by $\tau _ { : }$ ，and indicate with a bar the function in which this change has been made.We integrate with respect to $t$ under the supposition that $\pmb { \tau }$ con-tained in such a function is constant. After the integration we put $\tau = t$ Then an arbitrary function of $\pmb { \tau }$ should be added by this integration with respect to $\pmb { t } .$ ，This arbitrary function is determined so that the functions

$$
\begin{array} { r } { r _ { 0 } \rho = \displaystyle \int N Q _ { r } d \tau , \xi = \displaystyle \int N Q _ { x } d \tau , \eta = \displaystyle \int N Q _ { y } d \tau , } \end{array}
$$

$$
\zeta = \int N Q _ { z } d \tau , N = \bar { q } _ { 2 } q _ { 1 } - \bar { q } _ { 1 } q _ { 2 } ,
$$

should coincide with those of (8).

Now we have for an eliptic motion,

$$
q _ { 1 } = k ( \cos u - e ) , \qquad k _ { 2 } = k \sin u .
$$

In fact, by writing

$$
n = \sqrt { \mu / a ^ { 3 } } , ~ n t + \epsilon - \varpi = M = u - \epsilon \sin u ,
$$

we have

$$
{ \frac { r _ { 0 } } { a } } = 1 - \thinspace e \cos { u } , \qquad d M = { \frac { r _ { 0 } } { a } } d u .
$$

Then (6) becomes

$$
\frac { d ^ { 2 } q } { d M ^ { 2 } } + \frac { a ^ { 3 } } { r _ { 0 } ^ { 3 } } q = 0 ,
$$

or, if we take $\pmb { u }$ as the independent variable,

$$
( 1 - e \cos u ) \frac { d ^ { 2 } q } { d u ^ { 2 } } - e \sin u \frac { d q } { d u } + q = 0 ,
$$

or

$$
\frac { d ^ { 3 } q } { d u ^ { 3 } } + \frac { d q } { d u } = 0 .
$$

The solution of this equation is

$$
q = k _ { 1 } \cos u + k _ { 2 } \sin u + k _ { 3 } ,
$$

or

$$
q = K _ { 1 } ( \cos u - e ) + K _ { 2 } \sin u ,
$$

where $k _ { 3 }$ is so chosen that (1O) is satisfied, that is, $k _ { 3 } = - k _ { 1 } e$

Put $k ^ { 2 } = 1 / n$ ; then,

$$
\begin{array} { l } { { q _ { 1 } = \displaystyle \sqrt { \frac { a ^ { 3 } n } { \mu } } \left( \cos u - \epsilon \right) = \displaystyle \sqrt { \frac { a n } { \mu } } r _ { 0 } \cos v , } } \\ { { q _ { 2 } = \displaystyle \sqrt { \frac { a ^ { 3 } n } { \mu } } \sin u = \sqrt { \frac { a n } { \mu ( 1 - \epsilon ^ { 2 } ) } } r _ { 0 } \sin v , } } \\ { { N = \displaystyle \frac { a n } { \mu \sqrt { 1 - \epsilon ^ { 2 } } } \bar { r } _ { 0 } r _ { 0 } \sin \left( \bar { v } - v \right) . } } \end{array}
$$

Referring to the formula of an elliptic motion

$$
d t = { \frac { r ^ { 2 } d v } { a ^ { 2 } n { \sqrt { 1 - e ^ { 2 } } } } } ,
$$

we obtain the perturbation

$$
\begin{array} { l } { \displaystyle { \rho = \frac { 1 } { \mu a ( 1 - \varepsilon ^ { 2 } ) } \int Q _ { \varepsilon ^ { T _ { 0 } ^ { 3 } } } \sin { ( \bar { \upsilon } - \upsilon ) } d \upsilon , } } \\ { \displaystyle { \xi = \frac { r _ { 0 } } { \mu a ( 1 - \varepsilon ^ { 2 } ) } \int Q _ { \varepsilon ^ { T _ { 0 } ^ { 3 } } } \sin { ( \bar { \upsilon } - \upsilon ) } d \upsilon , } } \\ { \displaystyle { \eta = \frac { r _ { 0 } } { \mu a ( 1 - \varepsilon ^ { 2 } ) } \int Q _ { \varepsilon ^ { T _ { 0 } ^ { 3 } } } \sin { ( \bar { \upsilon } - \upsilon ) } d \upsilon , } } \\ { \displaystyle { \zeta = \frac { r _ { 0 } } { \mu a ( 1 - \varepsilon ^ { 2 } ) } \int Q _ { \varepsilon ^ { T _ { 0 } ^ { 3 } } } \sin { ( \bar { \upsilon } - \upsilon ) } d \upsilon . } } \end{array}
$$

Let the longitude measured on the $( x , y )$ -plane be $\lambda$ , so that tan $\lambda = y / x ,$ and put

$$
\begin{array} { r l r } {  { \frac { x _ { 0 } d y _ { 0 } - y _ { 0 } d x _ { 0 } } { d t } = h , } } \\ & { } & { \frac { x d y - y d x } { d t } = h + \int ( x \frac { \partial R } { \partial y } - y \frac { \partial R } { \partial x } ) d t ; } \end{array}
$$

then,

$$
( r ^ { 2 } - z ^ { 2 } ) { \frac { d \lambda } { d t } } = h + \int Q _ { \lambda } d t ,
$$

where

$$
h = \sqrt { \mu a ( 1 - e ^ { 2 } ) } \cdot \cos I , \qquad Q _ { \lambda } = x \frac { \partial R } { \partial y } - y \frac { \partial R } { \partial x } = \frac { \partial R } { \partial \lambda } .
$$

Let $\lambda = \lambda _ { 0 } + \delta \lambda _ { : }$ tan $\lambda _ { 0 } = y _ { 0 } / x _ { 0 }$ ; then,

$$
\begin{array} { l } { { \displaystyle { \bar { 3 } \lambda = \int \left[ \int \frac { a n } { \mu } Q _ { \lambda } d t - \sqrt { 1 - e ^ { 2 } } { \cdot } { \cos { \cal I } } . \frac { ( r + r _ { 0 } ) \rho - ( z - z _ { 0 } ) \zeta } { r _ { 0 } ^ { 2 } - z _ { 0 } ^ { 2 } } \right] \frac { a ^ { 2 } n \sigma } { r ^ { 2 } - } } } } \\ { { \displaystyle { \quad = \int \left[ \int \frac { r _ { 0 } ^ { 2 } } { \mu \dot { p } } Q _ { \lambda } d v - \frac { ( r + r _ { 0 } ) \rho - \zeta ^ { 2 } } { r _ { 0 } ^ { 2 } } \right] \frac { r _ { 0 } ^ { 2 } d v } { r ^ { 2 } - \zeta ^ { 2 } } } . } } \end{array}
$$

For computing the first-order perturbation we write

$$
\begin{array} { l } { { T = \displaystyle \frac { r ^ { 3 } } { \mu \beta } Q _ { r } = \displaystyle \frac { r ^ { 3 } } { \mu \beta } \left[ 2 \int d R + r \frac { \partial R } { \partial r } \right] , \hfill } } \\ { { \quad \displaystyle X = \frac { r ^ { 4 } } { \mu \beta } \frac { \partial R } { \partial r } , \qquad Y = \frac { r ^ { 2 } } { \mu \beta } Q _ { \lambda } , \qquad Z = \frac { r ^ { 3 } } { \mu \beta } \frac { \partial R } { \partial z } } , } \end{array}
$$

and define

$$
\sin \beta = \frac { z } { r } , \qquad \sin \beta _ { 0 } = \frac { z _ { 0 } } { r _ { 0 } } , \qquad \beta = \beta _ { 0 } + \delta \beta ;
$$

then,

$$
\delta r = \int T \sin ( \bar { v } - v ) d v , \qquad \delta \beta = \int Z \sin ( \bar { v } - v ) d v ,
$$

$$
\delta \lambda = \int \left[ \int \boldsymbol { Y } d v - 2 \frac { \delta \boldsymbol { r } } { r } \right] d v ,
$$

or

$$
\begin{array} { l } { { \displaystyle \delta r = \int \left[ X + 2 r ^ { 3 } \int r ^ { - 2 } \biggl ( \frac { e \sin v } { \dot { P } } X + Y \biggr ) d v \right] \sin ( \bar { v } - v ) \ d v , } } \\ { { \displaystyle \delta \lambda = \int \left[ \int Y d v - 2 \frac { \delta r } { r } \right] d v , } } \\ { { \displaystyle \delta \beta = \int \left[ Z \sin \left( \bar { v } - v \right) \right] d v . } } \end{array}
$$

For the second-order perturbation， put $r = r _ { 0 } + \delta r + \delta ^ { 2 } r$ and proceed successively.Hill (l896) applied this method to the computation of the first-order perturbation of Ceres.Grebenikov (l960) applied it to an earth satellite.

# 10.3BROUWER'S METHOD

Brouwer (1944,1955)- following Brunnow (1865), Hill (1874),and Dziobek (1888)-modified Encke's method by avoiding the inconvenient

use of the fourth quantity $\delta r$ in the perturbation.Take the undisturbed orbital plane as the $( x , y )$ -plane. The equations of motion are

$$
\begin{array} { r } { \displaystyle { \frac { d ^ { 2 } \xi } { d t ^ { 2 } } + \frac { r } { r ^ { 3 } } \left( x _ { 0 } + \xi \right) - \frac { \mu x _ { 0 } } { r _ { 0 } ^ { 3 } } = \frac { \partial R } { \partial x } } , } \\ { \displaystyle { \frac { d ^ { 2 } \eta } { d t ^ { 2 } } + \frac { \mu } { r ^ { 3 } } \left( y _ { 0 } + \eta \right) - \frac { \mu y _ { 0 } } { r _ { 0 } ^ { 3 } } = \frac { \partial R } { \partial y } } , } \\ { \displaystyle { \frac { d ^ { 2 } z } { d t ^ { 2 } } + \frac { \mu z } { r ^ { 3 } } = \frac { \partial R } { \partial z } } . } \end{array}
$$

Expanding the second terms on the left-hand sides in powers of $\xi , \eta , \zeta ,$ we can transform the equations to the form

$$
\begin{array} { r l } & { \displaystyle \frac { d ^ { 2 } \xi } { d t ^ { 2 } } + \frac { \mu \xi } { r _ { 0 } ^ { 3 } } - \frac { 3 \mu x _ { 0 } } { r _ { 0 } ^ { 5 } } \left( x _ { 0 } \xi + y _ { 0 } \eta \right) = X = \frac { \partial R } { \partial x } + \Delta X , } \\ & { \displaystyle \frac { d ^ { 2 } \eta } { d t ^ { 2 } } + \frac { \mu \eta } { r _ { 0 } ^ { 3 } } - \frac { 3 \mu y _ { 0 } } { r _ { 0 } ^ { 5 } } \left( x _ { 0 } \xi + y _ { 0 } \eta \right) = Y = \frac { \partial R } { \partial y } + \Delta Y . } \end{array}
$$

The corresponding equations without the right-hand members are satisfied by

$$
\xi _ { j } = \frac { \partial x _ { 0 } } { \partial c _ { j } } , \qquad \eta _ { j } = \frac { \partial y _ { 0 } } { \partial c _ { j } } \qquad ( j = 1 , 2 , 3 , 4 ) ,
$$

where $c _ { j }$ are the four constants defining the motion on the undisturbed orbital plane. Hence the general solution is

$$
\xi = \sum _ { j = 1 } ^ { 4 } C _ { j } { \frac { \partial x _ { 0 } } { \partial c _ { j } } } , \qquad \eta = \sum _ { j = 1 } ^ { 4 } C _ { j } { \frac { \partial y _ { 0 } } { \partial c _ { j } } } ,
$$

with four arbitrary constants $C _ { j }$ 、By the method of the variation of arbitrary constants for solving differential equations we have for the disturbed motion

$$
\sum _ { j = 1 } ^ { 4 } \frac { \partial x _ { 0 } } { \partial c _ { j } } \frac { d C _ { j } } { d t } = 0 , \qquad \sum _ { j = 1 } ^ { 4 } \frac { \partial y _ { 0 } } { \partial c _ { j } } \frac { d C _ { j } } { d t } = 0 ,
$$

$$
\sum _ { j = 1 } ^ { 4 } \frac { \partial \dot { x } _ { 0 } } { \partial c _ { j } } \frac { d C _ { j } } { d t } = X , \qquad \sum _ { j = 1 } ^ { 4 } \frac { \partial \dot { y } _ { 0 } } { \partial c _ { j } } \frac { d C _ { j } } { d t } = Y .
$$

Denote the Jacobian by

$$
J = \frac { \partial ( x _ { 0 } , y _ { 0 } , \dot { x } _ { 0 } , \dot { y } _ { 0 } ) } { \partial ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } ) } ,
$$

and its minor determinants by enclosing in a square bracket.The result of solving these four equations is

$$
\frac { d C _ { j } } { d t } = \frac { X } { J } \left[ \frac { \partial \dot { x } _ { 0 } } { \partial c _ { j } } \right] + \frac { Y } { J } \left[ \frac { \partial \dot { y } _ { 0 } } { \partial c _ { j } } \right] ~ ( j = 1 , 2 , 3 , 4 ) .
$$

Hence,

$$
\begin{array} { l } { \displaystyle \xi = \sum _ { j = 1 } ^ { 4 } \frac { \partial x _ { 0 } } { \partial c _ { j } } \int \left\{ \frac { X } { \mathcal { T } } \left[ \frac { \partial \dot { x } _ { 0 } } { \partial c _ { j } } \right] + \frac { Y } { \mathcal { J } } \left[ \frac { \partial \dot { y } _ { 0 } } { \partial c _ { j } } \right] \right\} d t , } \\ { \displaystyle \eta = - \sum _ { j = 1 } ^ { 4 } \frac { \partial y _ { 0 } } { \partial c _ { j } } \int \left\{ \frac { X } { \mathcal { J } } \left[ \frac { \partial \dot { x } _ { 0 } } { \partial c _ { j } } \right] + \frac { Y } { \mathcal { J } } \left[ \frac { \partial \dot { y } _ { 0 } } { \partial c _ { j } } \right] \right\} d t . } \end{array}
$$

This integration is hopelessly laborious. The following artifice was first introduced by Hansen and used by Hill (Section lO.2):we move the factors $\partial { x _ { 0 } } / \partial { c _ { j } }$ and $\partial y _ { 0 } / \partial c _ { j }$ under the integral signs and combine the various factors of $X$ and $\pmb { Y }$ into single factors.We then replace by $\pmb { \tau }$ the independent variable $t$ in the factors outside the integral signs,and integrate with respect to $\pmb { t }$ by keeping $\pmb { \tau }$ constant after the multiplication of the two factors under the integral signs. After integration we change $\pmb { \tau }$ into t. Indicate with a bar a function of $\pmb { \tau }$ in which $\boldsymbol { \tau }$ is substituted for $\pmb { t } ,$ Then the final expression for the perturbation is

$$
\begin{array} { l } { { \displaystyle \xi = \frac { \partial x _ { 0 } } { \partial l } \delta ^ { \prime } l + \int \left( A _ { x } X + A _ { y } Y \right) d t } , } \\ { ~ } \\ { { \displaystyle \eta = \frac { \partial y _ { 0 } } { \partial l } \delta ^ { \prime \prime } l + \int \left( B _ { x } X + B _ { y } Y \right) d t } , } \end{array}
$$

in which

$$
\begin{array} { l } { { \displaystyle \delta ^ { \prime } l = - \frac { 3 n ^ { 2 } a } { \mu } \int \int \left( \frac { \partial x _ { 0 } } { \partial l } X + \frac { \partial y _ { 0 } } { \partial l } Y \right) d t ^ { 2 } } } \\ { { \displaystyle ~ = - \frac { 3 n ^ { 2 } a } { \mu } \int \int \left[ \left( \frac { \partial R } { \partial l } \right) _ { 0 } + \frac { \partial x _ { 0 } } { \partial l } \Delta X + \frac { \partial y _ { 0 } } { \partial l } \Delta Y \right] d t ^ { 2 } } , } \end{array}
$$

where $A _ { x } = \left( x _ { 0 } , \bar { x } _ { 0 } \right)$ ， $A _ { y } = ( y _ { 0 } , \bar { x } _ { 0 } )$ ， $\boldsymbol { B _ { x } } = \left( x _ { 0 } , \bar { y } _ { 0 } \right)$ ， $\begin{array} { r } { B _ { y } = ( y _ { 0 } , \bar { y } _ { 0 } ) } \end{array}$ are similar to the Poisson brackets.

The equation for the $_ z$ -coordinate

$$
\frac { d ^ { 2 } \zeta } { d t ^ { 2 } } + \frac { \mu \zeta } { r ^ { 3 } } = \frac { \partial R } { \partial z }
$$

can be solved similarly to Hil'smethod by

$$
\zeta = \frac { n a } { \mu \sqrt { 1 - e ^ { 2 } } } \left[ \int r \bar { r } \sin \left( \bar { v } - v \right) \frac { \partial R } { \partial z } d t \right] _ { \tau = t } .
$$

This method can easily be extended to the computation of higher-order perturbations.

Brouwer and Clemence (l946) later simplified the development of the powers of the reciprocal of the mutual distance between two planets. Duncombe and Davis (l950,l95l） applied the method and saw that Brouwer's method needs very little labor in the computation. Further Davis (l95l） applied the method to the motion of the asteroid 185 Eunike and then Clemence (l947) applied it to the perturbation of Mars due to Venus. Davis (1958) rewrote Brouwer's formulas in terms of the standard elliptic elements instead of canonical elements as in Brouwer's theory. They reported that the computation of the motion of the five outer major planets by Brouwer's method was in progress (Clemence 1953,1954,1960).

Recently Danby (1962) applied the matrix method for the approximate solution of differential equations to the development of general perturbations in rectangular coordinates,and then in polar coordinates (1965). He obtained the solution directly in the form of the complementary function and the particular integral. According to Danby, the matrix method was used first by Miachin in l959 for discussing the observational accuracy,and was adopted for perturbation computation by Gontkovskaya in 1958 and Deberdeev in l960 (see Sections 12.24-12.33).

Brouwer's theory of the general perturbations in rectangular coordinates refers to the variation of elements in canonical form. If perturbations are expanded in trigonometric series with purely numerical coefficients, then the use of canonical elements is not of any advantage, as recognized by Davis (l95l).Davis rewrote Brouwer's formula in terms of the Keplerian elements, but his formula contains two terms of order $- 1$ in the eccentricity which causes numerical inconvenience in the case of nearly circular orbits. Musen (1966) suggested the use of the Eckert-Brouwer formula (l937) for the orbit correction as a foundation of a planetary theory. This leads directly to a vectorial expression for perturbation, free from the small divisor,in terms of the Gibbs rotation vectors, which will be defined by equation (29).Musen gave the method of iteration for computing higher-order perturbations,which is necessary for cislunar orbits far away from the earth一resembling in their motions planets or comets rather than satellites.

The central idea of Brouwer's method is one form of the variation of elements. This form requires the computation ofLagrange's and Poisson's brackets not for the osculating elements but for the constant elements, and hence removes from the differential equations the effect of the variability of the elements on the coefficients of the disturbing force components and shifts this effect to the modified disturbing force.Musen (1966a）expresses this modified disturbing force in terms of Faa de Bruno's differential operators (Musen, l963, l965).The perturbation effects of higher orders are transferred from the elements to these operators. The application of these operators leads to the decomposition of the disturbing force in terms of multipoles (see the latter part of Section l0.4） with the momenta equal to the perturbations in the position vectors of the planets.

Denote by $\nabla$ the del operator with respect to $\pmb { x }$ and by $\nabla ^ { \prime }$ that with respect to $\mathbf { r } ^ { \prime }$ ,and let $\mathfrak { p } = \mathbf { r } ^ { \prime } - \mathbf { r } , \mu ^ { 2 } = k ^ { 2 } ( 1 + m )$ .Then the differential equations in vector notation

$$
{ \frac { d ^ { 2 } ( \mathbf { r } + \mathbf { \delta } \delta \mathbf { r } ) } { d t ^ { 2 } } } = \mu ^ { 2 } \nabla { \frac { 1 } { | \mathbf { r } + \mathbf { \delta } \delta \mathbf { r } | } } + k ^ { 2 } m ^ { \prime } \nabla ^ { \prime } \left( { \frac { 1 } { | \mathbf { r } ^ { \prime } + \mathbf { \delta } \delta \mathbf { r } ^ { \prime } | } } - { \frac { 1 } { | \mathbf { \delta } \mathbf { \cdot } \delta \mathbf { \delta } | } } \right)
$$

can be transformed to

$$
\frac { d ^ { 2 } \ : \delta \mathbf { r } } { d t ^ { 2 } } = \mu ^ { 2 } ( D - \nabla ) \ : \frac { 1 } { r } + \ : k ^ { 2 } m ^ { \prime } \Big ( D ^ { \prime } \ : \frac { 1 } { r } - \ : D ^ { \prime \prime } \ : \frac { 1 } { \rho } \Big ) ,
$$

where

$$
\begin{array} { r l r l r } { \mathrm {  ~ \lambda ~ } } & { { } \lambda = \nabla \exp \delta { \bf x } \cdot \nabla , } & { } & { D ^ { \prime } = \nabla ^ { \prime } \exp \delta { \bf x } ^ { \prime } \cdot \nabla ^ { \prime } , } & { } & { D ^ { \prime } = \nabla ^ { \prime } \exp \delta { \bf \circ } \cdot \nabla ^ { \prime } ; } \end{array}
$$

or, by the identity

$$
\delta \mathbf { r } \cdot \nabla \nabla { \frac { 1 } { r } } = \mathbf { \nabla } - { \frac { 1 } { r ^ { 3 } } } \left( I - { \frac { 3 \mathbf { r } \mathbf { r } } { r ^ { 2 } } } \right) \cdot \delta \mathbf { r } ,
$$

to

$$
\begin{array} { c } { \displaystyle \frac { d ^ { 2 } ~ \delta \mathbf { r } } { d t ^ { 2 } } + \frac { \mu ^ { 2 } } { r ^ { 3 } } \left( I - \frac { 3 \mathbf { r } \mathbf { r } } { r ^ { 2 } } \right) \cdot \delta \mathbf { r } = \mathbf { F } , } \\ { \displaystyle \mathbf { F } = \mu ^ { 2 } ( D - \nabla - \delta \mathbf { r } \cdot \nabla \nabla ) \frac { 1 } { r } + k ^ { 2 } m ^ { \prime } \Big ( D ^ { \prime } \frac { 1 } { r ^ { \prime } } - D ^ { \prime \prime } \frac { 1 } { \rho } \Big ) . } \end{array}
$$

Let the solution of

$$
{ \frac { d ^ { 2 } \mathbf { r } } { d t ^ { 2 } } } = \mu ^ { 2 } \nabla { \frac { 1 } { r } }
$$

be $\mathbf { r } = \mathbf { r } ( t ; c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , c _ { 6 } )$ ； then,according to the method of the variation of constants, the solution with $\mathbf { F } = 0$ is

$$
\delta \mathbf { r } = \sum _ { j = 1 } ^ { 6 } \delta c _ { j } { \frac { \partial \mathbf { r } } { \partial c _ { j } } } .
$$

We have

$$
\delta \mathbf { v } = \sum _ { j = 1 } ^ { 6 } \delta c _ { j } { \frac { \partial \mathbf { v } } { \partial c _ { j } } } , \qquad \sum _ { j = 1 } ^ { 6 } { \frac { d \delta c _ { j } } { d t } } { \frac { \partial \mathbf { r } } { \partial c _ { j } } } = 0 ,
$$

$$
\sum _ { j = 1 } ^ { 6 } \frac { d \delta c _ { j } } { d t } \frac { \partial \mathbf { v } } { \partial c _ { j } } = \mathbf { F } .
$$

Hence

$$
\sum _ { j = 1 } ^ { 6 } \left[ c _ { i } , c _ { j } \right] { \frac { d \delta c _ { j } } { d t } } = { \frac { \partial \mathbf { r } } { \partial c _ { j } } } { \boldsymbol { \cdot } } \mathbf { F } ,
$$

$$
[ c _ { i } , c _ { j } ] = \frac { \partial \mathbf { r } } { \partial c _ { i } } \frac { \partial \mathbf { v } } { \partial c _ { j } } - \frac { \partial \mathbf { r } } { \partial c _ { j } } \frac { \partial \mathbf { v } } { \partial c _ { i } } ,
$$

or

$$
\frac { d \delta c _ { i } } { d t } = \sum _ { j = 1 } ^ { 6 } \left( c _ { i } , c _ { j } \right) \frac { \partial \mathbf { r } } { \partial c _ { j } } { \boldsymbol { \cdot } } \mathbf { F } ,
$$

where $[ c _ { i } , c _ { j } ]$ and $( c _ { i } , c _ { j } )$ should be formed with constant elements, but not with the osculating elements. The sums $c _ { i } + \delta c _ { i }$ are not the osculating elements, either.This means that the effect of the perturbation is transferred from the elements to the operators $D , D ^ { \prime } , D ^ { \prime \prime }$ .From (20) we obtain

$$
\delta \mathbf { r } = \sum _ { i = 1 } ^ { 6 } { \frac { \partial \mathbf { r } } { \partial c _ { i } } } \left( { \delta c _ { i } } \right) + \sum _ { i = 1 } ^ { 6 } \sum _ { j = 1 } ^ { 6 } { \frac { \partial \mathbf { r } } { \partial c _ { i } } } \int \left( c _ { i } , c _ { j } \right) { \frac { \partial \mathbf { r } } { \partial c _ { j } } } \cdot \mathbf { F } d t
$$

with the integration constants $( \delta c _ { i } )$ . In accordance with Hansen's device we distinguish between the time $\pmb { t }$ under this integral and the time contained in the undisturbed vector $\mathbf { r } ( t )$ and its derivatives outside the integrals.Denote the latter time by $\tau _ { ; }$ and $\mathbf { r } ( \tau )$ by r. The mean anomaly $n \tau + l _ { 0 }$ associated with r is denoted by $\bar { \iota } .$ We consider $\pmb { \tau }$ and r as constants until the integration is performed; and after the integration we replace $\pmb { \tau }$ by t. Thus,

and

$$
\delta \mathbf { r } = \sum _ { i = 1 } ^ { 6 } { \frac { \partial \mathbf { r } } { \partial c _ { i } } } \left( \delta c _ { i } \right) + \int \Gamma ( t , \tau ) \cdot \mathbf { F } d t ,
$$

$$
\Gamma ( t , \tau ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { 6 } \sum _ { j = 1 } ^ { 6 } \left( c _ { i } , c _ { j } \right) \left( \frac { \partial \overline { { \mathbf { r } } } } { \partial c _ { i } } \frac { \partial \mathbf { r } } { \partial c _ { j } } - \frac { \partial \overline { { \mathbf { r } } } } { \partial c _ { j } } \frac { \partial \mathbf { r } } { \partial c _ { i } } \right) ,
$$

$$
\delta \mathbf { v } = \sum _ { i = 1 } ^ { 6 } \frac { \partial \mathbf { v } } { \partial c _ { i } } \left( \delta c _ { i } \right) + \int \frac { \partial \Gamma ( t , \tau ) } { \partial \tau } \cdot \mathbf { F } \ d t .
$$

Using (20) we can transfer a differential equation for perturbation of an osculating element into the equation in the present theory by replacing $\partial \Omega / \partial c _ { i }$ by $\partial \mathbf { r } / \partial c _ { i } { \cdot } \mathbf { F }$ If the element is a vector $\pmb { \mathrm { c } }$ ，then $\nabla _ { \mathbf { c } } \Omega$ should be replaced by $\nabla _ { \mathbf { c } } \mathbf { r } \cdot \mathbf { F }$ .Thus,

$$
\begin{array} { r l } & { \frac { d \delta \mathbf { P } } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { n a ^ { 2 } e } \mathbf { Q } \frac { \partial \mathbf { r } } { \partial e } \mathbf { \cdot F } - \frac { 1 } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } s _ { 1 } \mathbf { R } \mathbf { R } \mathbf { \cdot F } , } \\ & { \frac { d \delta \mathbf { Q } } { d t } = - \frac { \sqrt { 1 - e ^ { 2 } } } { n a ^ { 2 } e } \mathbf { P } \frac { \partial \mathbf { r } } { \partial e } \mathbf { \cdot F } + \frac { 1 } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } c _ { 1 } \mathbf { R } \mathbf { R } \mathbf { \cdot F } , } \\ & { \frac { d \delta e } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { n a ^ { 2 } e } \left( \mathbf { r } \times \mathbf { R } + \sqrt { 1 - e ^ { 2 } } \frac { \partial \mathbf { r } } { \partial l } \right) \mathbf { \cdot F } , } \end{array}
$$

where $\mathbf { p } , \mathbf { Q } , \mathbf { R }$ are the Gibbs vector such that

$$
\begin{array} { c } { { { \bf r } = \xi { \bf P } + \eta { \bf Q } , \qquad \xi = c _ { 1 } = a ( \cos u - e ) , } } \\ { { \eta = s _ { 1 } = a \sqrt { 1 - e ^ { 2 } } \sin u . } } \end{array}
$$

We have

$$
\begin{array} { r l } & { \frac { \sqrt { 1 - \epsilon ^ { 2 } } } { n a ^ { 2 } \epsilon } \left[ \frac { \partial \bar { \bf x } } { \partial \epsilon } \left( { \bf r } \times { \bf R } + \sqrt { 1 - \epsilon ^ { 2 } } \frac { \partial { \bf r } } { \partial \tilde { l } } \right) \right. } \\ & { \qquad \quad \left. - \left( \bar { \bf r } \times { \bf R } + \sqrt { 1 - \epsilon ^ { 2 } } \frac { \partial \bar { \bf x } } { \partial \tilde { l } } \right) \frac { \partial { \bf r } } { \partial e } \right] } \\ & { \mathrm { ~  ~ \cdot ~ } \frac { 2 } { n a ^ { 2 } } \left[ \left( a \frac { \partial \bar { \bf x } } { \partial \tilde { a } } \right) \frac { \partial { \bf r } } { \partial \tilde { l } } - \frac { \partial \bar { \bf r } } { \partial \tilde { l } } \left( a \frac { \partial { \bf r } } { \partial \tilde { a } } \right) \right] + \frac { 1 } { n a ^ { 2 } \sqrt { 1 - \epsilon ^ { 2 } } } ( { \bf r } \times \bar { \bf r } ) \cdot { \bf R } . } \end{array}
$$

It can be shown that $\epsilon = 0$ is not a singularity,so that the method can be used even for nearly circular orbits.The function $\mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma }$ can be expressed as a double Fourier series with arguments $\iota$ and $\bar { \iota } .$

Next we expand $\delta \mathbf { r } , \delta \mathbf { r } ^ { \prime }$ ， $\delta \pmb { \rho }$ in powers of $_ m$ and $m ^ { \prime }$ ，so that

$$
\begin{array} { c } { { \delta { \bf r } = \delta _ { 1 } { \bf r } + \delta _ { 2 } { \bf r } + \cdot \cdot \cdot , \qquad \delta { \bf r } ^ { \prime } = \delta _ { 1 } { \bf r } ^ { \prime } + \delta _ { 2 } { \bf r } ^ { \prime } + \cdot \cdot \cdot , } } \\ { { \delta { \mathsf e } = \delta _ { 1 } { \mathsf e } + \delta _ { 2 } { \mathsf e } + \cdot \cdot \cdot ; } } \end{array}
$$

then,

$$
\begin{array} { c } { { \exp \left( \delta \mathbf { r } { \cdot } \nabla \right) = T _ { 0 } + T _ { 1 } + T _ { 2 } + \cdots , } } \\ { { \exp \left( \delta \mathbf { r } ^ { \prime } { \cdot } \nabla ^ { \prime } \right) = T _ { 0 } ^ { \prime } + T _ { 1 } ^ { \prime } + T _ { 2 } ^ { \prime } + \cdots , } } \\ { { \exp \left( \delta \mathbf { \rho } { \cdot } \nabla ^ { \prime } \right) = T _ { 0 } ^ { \prime \prime } + T _ { 1 } ^ { \prime \prime } + T _ { 2 } ^ { \prime \prime } + \cdots , } } \end{array}
$$

where $T _ { k } , \ T _ { k } ^ { \prime } , \ T _ { k } ^ { \prime \prime } \ ( k = 0 , 1 , 2 , . . . )$ ，are Faa de Bruno's differential operators. Let the kth order term in $\pmb { m }$ and $m ^ { \prime }$ be $\delta _ { \kappa }$ ; then,

$$
\delta _ { k } = \delta _ { k } \mathbf { r } \cdot \nabla , \qquad \delta _ { k } ^ { \prime } = \delta _ { k } \mathbf { r } ^ { \prime } \cdot \nabla ^ { \prime } , \qquad \delta _ { k } ^ { \prime \prime } = \delta _ { k } \mathsf { p } \cdot \nabla ^ { \prime } .
$$

The operators are

$$
T _ { 0 } = 1 , T _ { 1 } = \delta _ { 1 } , T _ { 2 } = \delta _ { 2 } + { \textstyle { \frac { 1 } { 2 } } } \delta _ { 1 } ^ { 2 } , . . . .
$$

The expansions of the operators $T _ { k } , \ T _ { k } ^ { \prime } , \ T _ { k } ^ { \prime \prime } , D , D ^ { \prime } , D ^ { \prime \prime }$ can be obtained by the formulas for multipole potentials.

For working by iteration we use the formulas

$$
{ \begin{array} { r l } & { \mathbf { F } = \left. 4 \mathbf { x } + B \mathbf { \Delta } \mathbf { \hat { x } } \right. + k ^ { 2 } m ^ { \prime } [ ( A ^ { \dagger } \mathbf { r } ^ { \prime } + B ^ { \prime } \mathbf { \Delta } \mathbf { \hat { x } } \mathbf { r } ) + \left( A ^ { \dagger } \mathbf { \hat { e } } + B ^ { \prime } \mathbf { \Delta } \mathbf { \hat { e } } \right) ] , } \\ & { A = - { \frac { 1 5 } { 2 \sqrt { \pi } } } \mathbf { e } ^ { 2 } + { \frac { 5 } { 2 \sqrt { \pi } } } \beta ^ { 2 } + { \frac { 3 5 } { 2 \sqrt { \pi } } } \alpha ^ { 2 } - { \frac { 1 5 } { 2 \sqrt { \pi } } } \alpha ^ { 2 } + \cdots , } \\ & { B = { \frac { 3 } { \sqrt { \pi } } } \alpha - { \frac { 1 5 } { 2 \sqrt { \pi } } } \alpha ^ { 2 } + \cdots , } \\ & { A ^ { \prime } = - { \frac { 1 } { \sqrt { \pi } ^ { 3 } } } + { \frac { 3 } { \sqrt { \pi } ^ { 3 } } } \alpha ^ { \prime } - { \frac { 1 5 } { 2 { \sqrt { \pi } } ^ { 7 } } } \alpha ^ { 2 } + { \frac { 3 } { 2 { \sqrt { \pi } } ^ { 5 } } } \beta ^ { 2 } + { \frac { 3 5 } { 2 { \sqrt { \pi } } ^ { 9 } } } \alpha ^ { \prime 3 } - { \frac { 1 5 } { 2 { \sqrt { \pi } } ^ { 7 } } } \alpha \beta ^ { 2 } + \cdots } \\ & { B ^ { \prime } = - { \frac { 1 } { \sqrt { \pi } ^ { 3 } } } + { \frac { 3 } { \sqrt { \pi } ^ { 3 } } } \alpha ^ { \prime } - { \frac { 1 5 } { 2 { \sqrt { \pi } } ^ { 7 } } } \alpha ^ { 2 } + \cdots , } \\ & { A ^ { \prime } = - { \frac { 1 } { \sqrt { \pi } ^ { 3 } } } + { \frac { 3 } { \sqrt { \pi } ^ { 9 } } } \alpha ^ { \prime } - { \frac { 1 5 } { 2 { \sqrt { \pi } } ^ { 7 } } } \alpha ^ { \prime 3 } + { \frac { 3 } { 2 { \sqrt { \pi } } ^ { 9 } } } \beta ^ { 2 } + \cdots , } \end{array} }
$$

$$
\begin{array} { r l } { \alpha = \mathbf { r } { \cdot } \delta \mathbf { r } , \quad } & { \beta ^ { 2 } = \delta \mathbf { r } ^ { 2 } , \quad \quad \alpha ^ { \prime } = \mathbf { r } ^ { \prime } { \cdot } \delta \mathbf { r } ^ { \prime } , \quad \quad \beta ^ { \prime 2 } = \delta \mathbf { r } ^ { \prime 2 } , } \\ & { \alpha ^ { \prime \prime } = \mathsf { p } { \cdot } \delta \mathsf { e } , \quad \quad \beta ^ { \prime \prime 2 } = \delta \mathsf { p } ^ { 2 } . } \end{array}
$$

The expansions in double series in $\pmb { \alpha }$ and $\beta ^ { 2 }$ converge rapidly. By harmonic analysis the negative powers of $r , r ^ { \prime }$ ,and $\pmb { \rho }$ can be expanded in double Fourier series with arguments $\iota$ and $\mathbf { \xi } _ { l ^ { \prime } }$ ·

Bower (1932), like Brouwer and Eckert,approached the solution by computing at first the variations of the eliptic elements with respect to the initial conditions and then the variations of the coordinates with respect to the elliptic elements.Danby (1962,1965） computed the elements of his matrizant in the reference frame in which the $\pmb { x } \cdot$ -axis is directed toward the perihelion.Miachin (l959） carried out similar computations together with the estimation of errors by numerical integration after the fashion of Brouwer (l938).Brumberg (1961) operated in the reference frame in which the $\pmb { x }$ -axis is directed to the radius vector,by taking into account the probability distribution of the initial conditions. Charnyi (l963） came to the consideration of the fundamental set of solutions of the adjoint variational equation. Deprit (1967),referring to Jacobi's dual theorem of the last multiplier, computed the matrizant by the intermediary of the adjoint variational equations (Section 18.24).

# 10.4STROMGREN'S METHOD

Denote by $\mathbf { F }$ the vector of the disturbing force acting on an asteroid. At any instant the osculating elements are determined by the radius vector $\mathbf { r } ( x , y , z )$ and the velocity vector ${ \bf v } ( \dot { x } , \dot { y } , \dot { z } )$ .In a time dt these vectors change by the amounts $\begin{array} { r } { d \mathbf { r } = \frac { 1 } { 2 } \mathbf { F } _ { 0 } \ : d t ^ { 2 } } \end{array}$ and $d \mathbf { v } = \mathbf { F } _ { 0 } d t ;$ ,respectively, plus higher-order terms.In the limit $d t  0$ we can set $d \mathbf { v } = \mathbf { F } d t ,$ $d \mathbf { r } = 0$ .We consider only the first-order perturbations.Let the $_ x$ -axis be directed toward the perihelion at $t _ { 0 }$ and the $z$ -axis perpendicular to the orbital plane at $t _ { 0 }$ . Denote by $I _ { x }$ and $I _ { y }$ the components of the moment of momentum of the asteroid, and the angle ${ \pmb { \pi } } = { \pmb { \omega } } + { \pmb { \Omega } } _ { \mathrm { { \pmb { \Lambda } } } }$ ，referred to this coordinate system.At the epoch of osculation, $I _ { x } = I _ { y } = 0$ ， $\pi = 0 _ { : }$ ， $a = a ^ { ( 0 ) }$ ， $\epsilon = \epsilon ^ { ( 0 ) }$ ,and $M = M _ { 0 } ^ { ( 0 ) }$ , the mean anomaly. From $\mathbf { I } = \mathbf { r } \times \mathbf { v } ,$ $d \mathbf { r } = 0$ and $d \mathbf { v } = \mathbf { F } d t _ { : }$ ,in vector notation,we see that $d \mathbf { I } = \left[ \mathbf { r } \times \mathbf { v } \right] d t ,$ where $| \mathbf { I } | = k { \sqrt { \pmb { \rho } } }$ ，Let the positive normal to the orbital plane be $\mathbf { N }$ $( N _ { x } , N _ { y } , N _ { z } )$ ; then

$$
d N _ { x } = d \alpha _ { 1 } = \frac { 1 } { k \sqrt { \dot { \gamma } } } y F _ { z } , d N _ { y } = d \alpha _ { 2 } = - \frac { 1 } { k \sqrt { \dot { \gamma } } } x F _ { z } , d N _ { z } = 0
$$

From the equation

$$
| \mathbf { v } | ^ { 2 } = k ^ { 2 } \big ( \frac { 2 } { r } - \frac { 1 } { a } \big ) ,
$$

we obtain

$$
d a = { \frac { 2 a ^ { 2 } } { k ^ { 2 } } } \mathbf { v } { \boldsymbol { \cdot } } \mathbf { F } d t = { \frac { 2 a ^ { 2 } } { k ^ { 2 } } } ( { \dot { x } } F _ { x } + { \dot { y } } F _ { y } ) ,
$$