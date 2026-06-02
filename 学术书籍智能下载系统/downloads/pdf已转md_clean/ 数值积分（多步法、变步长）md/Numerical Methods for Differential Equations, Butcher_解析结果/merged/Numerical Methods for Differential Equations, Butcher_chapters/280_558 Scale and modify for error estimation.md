# 558 Scale and modify for error estimation

Consider first the constant stepsize case and assume that, after many steps, there is an accumulated error in each of the input components to step $n$ . If $y ( x )$ is the particular trajectory defined by $y ( x _ { n - 1 } ) = y _ { 1 } ^ { [ n - 1 ] }$ , then write the remaining input values as

$$
\begin{array}{c} y _ { i } ^ { [ n - 1 ] } = h ^ { i - 1 } y ^ { ( i - 1 ) } ( x _ { n - 1 } ) - \epsilon _ { i - 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) , ~  \\ { i = 2 , 3 , \ldots , p + 1 . ~ } \end{array}
$$

After a single step, the principal output will have acquired a truncation error so that its value becomes $y ( x _ { n } ) - \epsilon _ { 0 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } )$ , where

$$
\epsilon _ { 0 } = \frac { 1 } { ( p { + } 1 ) ! } - \frac { 1 } { p ! } \sum _ { j = 1 } ^ { s } b _ { 1 j } c _ { j } ^ { p } + \sum _ { j = 2 } ^ { r } v _ { 1 j } \epsilon _ { j - 1 } .
$$

Write $\epsilon$ as the vector with components $\epsilon _ { 1 }$ , $\epsilon _ { 2 }$ , $\cdot \cdot \cdot$ , $\epsilon _ { p }$ . The value of $\epsilon$ is determined by the fact that (558a) evolves after a single step to

$$
\begin{array}{c} y _ { i } ^ { [ n ] } = h ^ { i - 1 } y ^ { ( i - 1 ) } ( x _ { n } ) - \epsilon _ { i - 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) ,  \\ { i = 2 , 3 , \ldots , p + 1 . } \end{array}
$$

However,

$$
y _ { i } ^ { [ n ] } = h \sum _ { j = 1 } ^ { s } b _ { i j } y ^ { \prime } ( x _ { n - 1 } + h c _ { j } ) + \sum _ { j = 2 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } + O ( h ^ { p + 1 } ) , \quad i = 2 , 3 , \ldots , p + 1 ,
$$

so that substitution of (558a) and (558c) into (558d), followed by Taylor expansion about $x _ { n - 1 }$ , gives the result

$$
\begin{array} { r } { \boldsymbol { \epsilon } = \left[ \begin{array} { c } { \frac { 1 } { p ! } } \\ { \frac { 1 } { ( p - 1 ) ! } } \\ { \vdots } \\ { \frac { 1 } { 1 ! } } \end{array} \right] - \frac { 1 } { p ! } \dot { \boldsymbol { B } } + \dot { \boldsymbol { V } } \boldsymbol { \epsilon } , } \end{array}
$$

where $\dot { B }$ is the matrix $B$ with its first row deleted. It was shown in Wright (2003) that

$$
\epsilon _ { i } = \beta _ { p + 1 - i } , \quad i = 1 , 2 , \ldots , p .
$$

Without a modification to the simple scaling process, the constancy of $\epsilon$ from step to step will be destroyed, and we consider how to correct for this. There are several reasons for wanting this correction. First, the reliability of (558b), as providing an estimate of the local error in a step, depends on values of $\epsilon$ in the input to the current step. Secondly, asymptotically correct approximations to $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )$ are needed for stepsize control purposes and, if these approximations are based on values of both $h F$ and $y ^ { \lfloor n - 1 \rfloor }$ , then these will also depend on $\epsilon$ in the input to the step. Finally, reliable estimates of $h ^ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } )$ are needed as a basis for dynamically deciding when an order increase is appropriate. It was shown in Butcher and Podhaisky (2006) that, at least for methods possessing property F, estimation of both $h ^ { p + 1 } y ^ { ( p + 1 ) }$ and $h ^ { p + 2 } y ^ { ( p + 2 ) }$ is possible, as long as constant $\epsilon$ values are maintained.

In Subsection 557 we considered the method (555b) from the point of view of variable stepsize stability. To further adjust to maintain the integrity of $\epsilon$ in a variable $h$ regime, it is only necessary to add to the scaled and modified outputs $y _ { 3 } ^ { \lfloor n \rfloor }$ and $y _ { 4 } ^ { [ n ] }$ , appropriate multiples of $- h F _ { 1 } + 3 h F _ { 2 } - 3 h F _ { 3 } + h F _ { 4 }$ .

# Exercises 55

55.1 Show that the method given by (555a) has order 2, and that the stages are also accurate to this order.   
55.2 Find the stability matrix of the method (555a), and show that it has two zero eigenvalues.   
55.3 Show that the method given by (556a) has order 3, and that the stages are also accurate to this order.   
55.4 Find the stability matrix of the method (556a), and show that it has two zero eigenvalues.   
55.5 Show that (556a) is L-stable.   
55.6 Show that the $( i , j )$ element of $\Psi ^ { - 1 }$ is equal to the coefficient of $w ^ { i - 1 } z ^ { j - 1 }$ in the power series expansion about $z = 0$ of $\alpha ( z ) / ( 1 - ( \lambda + w ) z )$ .

# References

Alexander R. (1977) Diagonally implicit Runge–Kutta methods for stiff ODEs. SIAM J. Numer. Anal., 14, 1006–1021.   
Axelsson O. (1969) A class of A-stable methods. BIT, 9, 185–199.   
Axelsson O. (1972) A note on class of strongly A-stable methods. BIT, 12, 1–4.   
Barton D., Willers I. M. and Zahar R. V. M. (1971) The automatic solution of systems of ordinary differential equations by the method of Taylor series. Comput. J., 14, 243–248.   
Bashforth F. and Adams J. C. (1883) An Attempt to Test the Theories of Capillary Action by Comparing the Theoretical and Measured Forms of Drops of Fluid, with an Explanation of the Method of Integration Employed in Constructing the Tables which Give the Theoretical Forms of Such Drops. Cambridge University Press, Cambridge.   
Brenan K. E., Campbell S. L. and Petzold L. R. (1989) Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations. North-Holland, New York.   
Brouder C. (2000) Runge–Kutta methods and renormalization. Eur. Phys. J. C., 12, 521–534.   
Burrage K. (1978) A special family of Runge–Kutta methods for solving stiff differential equations. BIT, 18, 22–41.   
Burrage K. and Butcher J. C. (1980) Non-linear stability of a general class of differential equation methods. BIT, 20, 185–203.   
Burrage K., Butcher J. C. and Chipman F. H. (1980) An implementation of singlyimplicit Runge–Kutta methods. BIT, 20, 326–340.   
Butcher J. C. (1963) Coefficients for the study of Runge–Kutta integration processes. J. Austral. Math. Soc., 3, 185–201.   
Butcher J. C. (1963a) On the integration processes of A. Huˇta. J. Austral. Math. Soc., 3, 202–206.   
Butcher J. C. (1965) A modified multistep method for the numerical integration of ordinary differential equations. J. Assoc. Comput. Mach., 12, 124–135.   
Butcher J. C. (1965a) On the attainable order of Runge–Kutta methods. Math. Comp., 19, 408–417.   
Butcher J. C. (1966) On the convergence of numerical solutions to ordinary differential equations. Math. Comp., 20, 1–10.   
Butcher J. C. (1972) An algebraic theory of integration methods. Math. Comp., 26, 79–106.   
Butcher J. C. (1975) A stability property of implicit Runge–Kutta methods. BIT, 15, 358–361.   
Butcher J. C. (1977) On A-stable implicit Runge–Kutta methods. BIT, 17, 375–378. Comput. Mach., 26, 731–738.   
Butcher J. C. (1985) The nonexistence of ten-stage eighth order explicit Runge– Kutta methods. BIT, 25, 521–540.   
Butcher J. C. (1987) The Numerical Analysis of Ordinary Differential Equations, Runge–Kutta and General Linear Methods. John Wiley & Sons Ltd, Chichester.   
Butcher J. C. (1987a) The equivalence of algebraic stability and AN-stability. BIT, 27, 510–533.   
Butcher J. C. (1995) On fifth order Runge–Kutta methods. BIT, 35, 202–209.   
Butcher J. C. (1995a) An introduction to DIMSIMs. Comput. Appl. Math., 14, 59– 72.   
Butcher J. C. (1997) An introduction to ‘Almost Runge–Kutta’ methods. Appl. Numer. Math., 24, 331–342.   
Butcher J. C. (1998) ARK methods up to order five. Numer. Algorithms, 17, 193– 221.   
Butcher J. C. (2001) General linear methods for stiff differential equations. BIT, 41, 240–264.   
Butcher J. C. (2002) The A-stability of methods with Pad´e and generalized Pad´e stability functions. Numer. Algorithms, 31, 47–58.   
Butcher J. C. (2006) General linear methods. Acta Numerica, 15, 157–256.   
Butcher J. C. (2008) Order and stability of generalized Pad´e approximations. Appl. Numer. Math. (to appear).   
Butcher J. C. and Cash J. R. (1990) Towards efficient Runge–Kutta methods for stiff systems. SIAM J. Numer. Anal., 27, 753–761.   
Butcher J. C. and Chartier P. (1997) A generalization of singly-implicit Runge– Kutta methods. Appl. Numer. Math., 24, 343–350.   
Butcher J. C. and Chipman F. H. (1992) Generalized Pad´e approximations to the exponential function. BIT, 32, 118–130.   
Butcher J. C. and Hill A. T. (2006) Linear multistep methods as irreducible general linear methods. BIT, 46, 5–19.   
Butcher J. C. and Jackiewicz Z. (1996) Construction of diagonally implicit general linear methods of type 1 and 2 for ordinary differential equations. Appl. Numer. Math., 21, 385–415.   
Butcher J. C. and Jackiewicz Z. (1998) Construction of high order diagonally implicit multistage integration methods for ordinary differential equations. Appl. Numer. Math., 27, 1–12.   
Butcher J. C. and Jackiewicz Z. (2003) A new approach to error estimation for general linear methods. Numer. Math., 95, 487–502.   
Butcher J. C. and Moir N. (2003) Experiments with a new fifth order method. Numer. Algorithms, 33, 137–151 .   
Butcher J. C. and Podhaisky H. (2006) On error estimation in general linear methods for stiff ODEs. Appl. Numer. Math., 56, 345–357.   
Butcher J. C. and Rattenbury N. (2005) ARK methods for stiff problems. Appl. Numer. Math., 53, 165–181 .   
Butcher J. C. and Wright W. M. (2003) A transformation relating explicit and diagonally-implicit general linear methods. Appl. Numer. Math., 44, 313–327.   
Butcher J. C. and Wright W. M. (2003a) The construction of practical general linear methods. BIT, 43, 695–721.   
Butcher J. C. and Wright W. M. (2006) Applications of doubly companion matrices. Appl. Numer. Math., 56, 358–373. points. J. Assoc. Comput. Mach., 13, 114–123.   
Cooper G. J. (1987) Stability of Runge-Kutta methods for trajectory problems. IMA J. Numer. Anal., 7, 1–13.   
Cooper G. J. and Verner J. H. (1972) Some explicit Runge–Kutta methods of high order. SIAM J. Numer. Anal., 9, 389–405.   
Curtis A. R. (1970) An eighth order Runge–Kutta process with eleven function evaluations per step. Numer. Math., 16, 268–277.   
Curtis A. R. (1975) High-order explicit Runge–Kutta formulae, their uses and limitations. J. Inst. Math. Appl., 16, 35–55.   
Curtiss C. F. and Hirschfelder J. O. (1952) Integration of stiff equations. Proc. Nat. Acad. Sci. U.S.A., 38, 235–243.   
Dahlquist G. (1956) Convergence and stability in the numerical integration of ordinary differential equations. Math. Scand., 4, 33–53.   
Dahlquist G. (1963) A special stability problem for linear multistep methods. BIT, 3, 27–43.   
Dahlquist G. (1976) Error analysis for a class of methods for stiff non–linear initial value problems. In G. A. Watson (ed.) Numerical Analysis, Lecture Notes in Math. 506, Springer, Berlin, 60–72.   
Dahlquist G. (1978) G-stability is equivalent to A-stability. BIT, 18, 384–401.   
Dahlquist G. (1983) On one-leg multistep methods. SIAM J. Numer. Anal., 20, 1130–1138.   
Dahlquist G. and Jeltsch R. (1979) Generalized disks of contractivity for explicit and implicit Runge–Kutta methods, Technical Report TRITA NA–7906, Dept. of Numer. Anal. and Computing Sci., Roy. Inst. Tech.   
Daniel J. W. and Moore R. E. (1970) Computation and Theory in Ordinary Differential Equations. W. H. Freeman, San Francisco.   
Davis P. J. and Rabinowitz P. (1984) Methods of Numerical Integration. Academic Press, New York.   
Donelson J. and Hansen E. (1971) Cyclic composite multistep predictor–corrector methods. SIAM J. Numer. Anal., 8, 137–157.   
Dormand J. R. and Prince P. J. (1980) A family of embedded Runge–Kutta formulae. J. Comput Appl, Math., 6, 19–26.   
Ehle B. L. (1969) On Pad´e approximations to the exponential function and $A$ -stable methods for the numerical solution of initial value problems, Research Rep. CSRR 2010, Dept. of AACS, University of Waterloo, Ontario, Canada.   
Ehle B. L. (1973) A-stable methods and Pad´e approximations to the exponential. SIAM J. Math. Anal., 4, 671–680.   
Ehle B. L. and Picel Z. (1975) Two parameter, arbitrary order, exponential approximations for stiff equations. Math. Comp., 29, 501–511.   
Euler L. (1913) De integratione aequationum differentialium per approximationem. In Opera Omnia, 1st series, Vol. 11, Institutiones Calculi Integralis, Teubner, Leipzig and Berlin, 424–434.   
Fehlberg E. (1968) Classical fifth, sixth, seventh and eighth order Runge–Kutta formulas with stepsize control, NASA TR R-287.   
Fehlberg E. (1969) Klassische Runge–Kutta-Formeln f¨unfter und siebenter Ordnung mit Schrittweiten-Kontrolle. Computing, 4, 93–106.   
Gear C. W. (1965) Hybrid methods for initial value problems in ordinary differential equations. SIAM J. Numer. Anal., 2, 69–86. Math. Comp., 21, 146–156.   
Gear C. W. (1971) Numerical Initial Value Problems in Ordinary Differential Equations. Prentice Hall, Englewood Cliffs, NJ.   
Gear C. W. (1971a) Algorithm 407, DIFSUB for solution of ordinary differential equations. Comm. ACM, 14, 185–190.   
Gear C. W. (1980) Runge–Kutta starters for multistep methods. ACM Trans. Math. Software, 6, 263–279.   
Gibbons A. (1960) A program for the automatic integration of differential equations using the method of Taylor series. Comput. J., 3, 108–111.   
Gill S. (1951) A process for the step-by-step integration of differential equations in an automatic computing machine. Proc. Cambridge Philos. Soc., 47, 96–108.   
Gragg W. B. and Stetter H. J. (1964) Generalized multistep predictor–corrector methods. J. Assoc. Comput. Mach., 11, 188–209.   
Gustafsson K. (1991) Control theoretic techniques for stepsize selection in explicit Runge–Kutta methods. ACM Trans. Math. Software, 17, 533–544.   
Gustafsson K., Lundh M. and S¨oderlind G. (1988) A PI stepsize control for the numerical solution of ordinary differential equations. BIT, 28, 270–287.   
Hairer E. (1978) A Runge–Kutta method of order 10. J. Inst. Math. Appl., 21, 47–59.   
Hairer E. and Leone P. (2000) Some properties of symplectic Runge–Kutta methods. NZ J. Math., 29, 169–175.   
Hairer E., Lubich C. and Roche M. (1989) The Numerical Solution of Differential-Algebraic Systems by Runge–Kutta Methods, Lecture Notes in Math. 1409. Springer, Berlin.   
Hairer E., Lubich C. and Wanner G. (2006) Geometric Numerical Integration: Structure-preserving Algorithms for Ordinary Differential Equations. Springer, Berlin.   
Hairer E., Nørsett S. P. and Wanner G. (1993) Solving Ordinary Differential Equations I: Nonstiff Problems. Springer, Berlin.   
Hairer E. and Wanner G. (1974) On the Butcher group and general multi-value methods. Computing, 13, 1–15.   
Hairer E. and Wanner G. (1981) Algebraically stable and implementable Runge– Kutta methods of high order. SIAM J. Numer. Anal., 18, 1098–1108.   
Hairer E. and Wanner G. (1982) Characterization of non-linearly stable implicit Runge–Kutta methods. In J. Hinze (ed.) Numerical Integration of Differential Equations and Large Linear Systems, Lecture Notes in Math. 968, Springer, Berlin, 207–219.   
Hairer E. and Wanner G. (1996) Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems. Springer, Berlin.   
Henrici P. (1962) Discrete Variable Methods in Ordinary Differential Equations. John Wiley & Sons Inc, New York.   
Henrici P. (1963) Error Propagation for Difference Methods. John Wiley & Sons Inc, New York.   
Heun K. (1900) Neue Methoden zur approximativen Integration der Differentialgleichungen einer unabh¨angigen Ver¨anderlichen. Z. Math. Phys., 45, 23–38.   
Higham N. J. (1993) The accuracy of floating point summation. SIAM J. Sci. Comput., 14, 783–799.   
Hundsdorfer W. H. and Steininger B. I. (1991) Convergence of linear multistep and one-leg methods for stiff nonlinear initial value problems. BIT, 31, 124–143. la r´esolut on num´erique des ´equations diff ielles du premier cta Fac. Nat. Univ. Comenian. Math., 1, 201–224.   
Huˇta A. (1957) Contribution \`a la formule de sixi\`eme ordre dans la m´ethode de Runge–Kutta–Nystr¨om. Acta Fac. Nat. Univ. Comenian. Math., 2, 21–24.   
Iserles A., Munthe-Kaas H. Z., Nørsett S. P. and Zanna A. (2000) Lie-group methods. Acta Numer., 9, 215–365.   
Iserles A. and Nørsett S. P. (1991) Order Stars. Chapman & Hall, London.   
Kahan W. (1965) Further remarks on reducing truncation errors. Comm. ACM, 8, 40.   
Kirchgraber U. (1986) Multistep methods are essentially one-step methods. Numer. Math., 48, 85–90.   
Kutta W. (1901) Beitrag zur n¨aherungsweisen Integration totaler Differentialgleichungen. Z. Math. Phys., 46, 435–453.   
Lambert J. D. (1991) Numerical Methods for Ordinary Differential Systems: the Initial Value Problem. John Wiley & Sons Ltd, Chichester.   
Lasagni F. M. (1988) Canonical Runge–Kutta methods. Z. Angew. Math. Phys., 39, 952–953.   
L´opez-Marcos M. A., Sanz-Serna J. M. and Skeel R. D. (1996) Cheap enhancement of symplectic integrators. In D. F. Griffiths and G. A. Watson (eds.) Numerical Analysis, Pitman Res. Notes Math. Ser., 344, Longman, Harlow, 107–122.   
Lotka A. J. (1925) Elements of Physical Biology. Williams and Wilkins, Baltimore, Md.   
Merson R. H. (1957) An operational method for the study of integration processes. In Proc. Symp. Data Processing, Weapons Research Establishment, Salisbury, S. Australia.   
Milne W. E. (1926) Numerical integration of ordinary differential equations. Amer. Math. Monthly, 33, 455–460.   
Milne W. E. (1953) Numerical Solution of Differential Equations. John Wiley & Sons Inc, New York.   
Møller O. (1965) Quasi double-precision in floating point addition. BIT, 5, 37–50.   
Møller O. (1965a) Note on quasi double-precision. BIT, 5, 251–255.   
Moore R. E. (1964) The automatic analysis and control of error in digital computation based on the use of interval numbers. In L. B. Rall (ed.) Error in Digital Computation, vol. 1. John Wiley & Sons Inc, New York, 61–130.   
Moulton F. R. (1926) New Methods in Exterior Ballistics. University of Chicago Press.   
Nordsieck A. (1962) On numerical integration of ordinary differential equations. Math. Comp., 16, 22–49.   
Nørsett S. P. (1974) Semi-explicit Runge–Kutta methods, Report No. 6/74, Dept. of Math., Univ. of Trondheim.   
Nystr¨om E. J. (1925) Uber die numerische Integration von Differentialgleichungen. ¨ Acta Soc. Sci. Fennicae, 50 (13), 55pp.   
Obreshkov N. (1940) Neue Quadraturformeln. Abh. der Preuß. Akad. der Wiss., Math.-naturwiss. Klasse, 4, .   
Prothero A. and Robinson A. (1974) On the stability and accuracy of one-step methods for solving stiff systems of ordinary differential equations. Math. Comp., 28, 145–162.   
Rattenbury N. (2005) Almost Runge–Kutta methods for stiff and non-stiff problems, PhD thesis, The University of Auckland.   
Richardson L. F. (1927) The deferred approach to the limit. Philos. Trans. Roy. Soc. London Ser. A., 226, 299–361.   
Robertson H. H. (1966) The solution of a set of reaction rate equations. In J. Walsh (ed.) Numerical Analysis: An Introduction, Academic Press, London, 178–182.   
Romberg W. (1955) Vereinfachte numerische Integration. Norske Vid. Selsk. Forh., Trondheim, 28, 30–36.   
Rosenbrock H. H. (1963) Some general implicit processes for the numerical solution of differential equations. Comput. J., 5, 329–330.   
Runge C. (1895) Uber die numerische Aufl¨ ¨ osung von Differentialgleichungen. Math. Ann., 46, 167–178.   
Sanz-Serna J. M. (1988) Runge–Kutta schemes for Hamiltonian systems. BIT, 39, 877–883.   
Sanz-Serna J. M. and Calvo M. P. (1994) Numerical Hamiltonian Problems. Chapman & Hall, London.   
Scherer R. (1977) A note on Radau and Lobatto formulae for ODEs. BIT, 17, 235– 238.   
Scherer R. (1978) Spiegelung von Stabilit¨atsbereichen. In R. Bulirsch, R. D. Grigorieff and J. Schr¨oder (eds.) Numerical Treatment of Differential Equations, Lecture Notes in Math. 631, Springer, Berlin, 147–152.   
Singh A. D. (1999) Parallel diagonally implicit multistage integration methods for stiff ordinary differential equations, PhD thesis, The University of Auckland.   
S¨oderlind G. (2002) Automatic control and adaptive time-stepping. Numer. Algorithms, 31, 281–310.   
Stoffer D. (1993) General linear methods: connection to one step methods and invariant curves. Numer. Math., 64, 395–408.   
Suris Yu. B. (1988) Preservation of symplectic structure in the numerical solution of Hamiltonian systems (in Russian). Akad. Nauk SSSR, Inst. Prikl. Mat., Moscow,, 232, 148–160, 238–239.   
Van der Pol B. (1926) On relaxation-oscillations. Philos. Mag. Ser. 7, 2, 978–992.   
Verner J. H. (1978) Explicit Runge–Kutta methods with estimates of the local truncation error. SIAM J. Numer. Anal., 15, 772–790.   
Vitasek E. (1969) The numerical stability in solution of differential equations. In J.L. Morris (ed.) Conf. on Numerical Solution of Differential Equations, Lecture Notes in Math. 109, Springer, Berlin, 87–111.   
Volterra V. (1926) Variazioni e fluttuazioni del numero d’individui in specie animali conviventi. Memorie della R. Accad. Naz. dei Lincei, (Ser. VI), 2, 31–131.   
Wanner G., Hairer E. and Nørsett S. P. (1978) Order stars and stability theorems. BIT, 18, 475–489.   
Wantanabe D. S. and Sheikh Q. M. (1984) One-leg formulas for stiff ordinary differential equations. SIAM J. Sci. Statist. Comput., 2, 489–496.   
Watts H. A. and Shampine L. F. (1972) A-stable block implicit one-step methods. BIT, 12, 252–266.   
Wright K. (1970) Some relationships between implicit Runge–Kutta, collocation and Lanczos $\tau$ methods, and their stability properties. BIT, 10, 217–227.   
Wright W. M. (2002) Explicit general linear methods with inherent Runge–Kutta stability. Numer. Algorithms, 31, 381–399.   
Wright W. M. (2003) General linear methods with inherent Runge–Kutta stability, PhD thesis, The University of Auckland.

# Index

A-stability, 76, 230, 238, 261, 270, 272,   
343, 353, 356, 365, 398, 421   
$\mathrm { A } ( \alpha )$ -stability, 230   
Adams, xiv, 105, 375   
adjoint methods, 220   
Alexander, 261   
algebraic analysis of order, 413   
algebraic stability, 250, 252   
AN-stability, 245, 252   
angular momentum, 5   
annihilation conditions, 129, 427, 431   
arithmetic-geometric mean, 43   
asymptotic error formula, 72   
Axelsson, 240

B-series, 280   
B-stability, 250   
Barton, 115   
Bashforth, xiv, 105, 375   
BN-stability, 250, 252   
boundary locus, 344, 346   
Brenan, xv   
Brouder, 280   
Burrage, 124, 258, 266, 373   
Butcher, 93, 122, 124, 163, 188, 192, 198, 240, 241, 258, 261, 266, 271, 280, 301, 358, 373, 380, 382, 402, 419, 420, 426, 433, 434, 436, 438, 445   
Butcher–Chipman conjecture, 402   
Byrne, 122, 380   
Calvo, xv   
Campbell, xv   
Cash, 271   
Cauchy–Schwarz inequality, 58   
Chartier, 436   
Chipman, 266, 402   
Christoffel–Darboux formula, 269   
coefficient tableau, 94

companion matrix, 25   
compensated addition, 82   
compensated summation, 83   
conjugacy, 302   
consistency, 107, 109, 317, 320–322, 324,   
326, 385, 389, 390, 396   
contraction mapping principle, 22   
convergence, 69, 107, 109, 317, 319, 322,   
324, 326, 385, 387, 388, 390, 396   
Cooper, 196   
covariance, 108, 386   
Curtis, 196   
Curtiss, 105

Dahlquist, 105, 247, 248, 320, 353, 358, 360, 361, 364, 365, 379   
Dahlquist barrier, 353, 355, 380   
Dahlquist second barrier, 358   
Daniel, 401   
Daniel–Moore barrier, 401   
DASSL, xv   
Davis, 20   
delay differential equation, 31 neutral, 32   
density of tree, 140   
derivative weight, 156   
difference equation, 38 Fibonacci, 40 linear, 38, 44   
differential equation autonomous, 2, 150 chemical kinetics, 14 dissipative, 8 Euler (rigid body), 20 Hamiltonian, xv, 34 harmonic oscillator, 16 initial value problem, 2 Kepler, 4, 87, 127 linear, 24 Lotka–Volterra, 18

G-stability, 343, 360, 361, 365   
Gaussian quadrature, 189, 215   
Gear, xiv, 122, 318, 368, 370, 380   
generalized order conditions, 186   
generalized Pad´e approximation, 400   
Gibbons, 115   
Gill, 82, 93, 180   
Gill–Møller algorithm, 82, 83   
global truncation error, 395, 412   
Gragg, 122, 380   
graph, 137   
Gustafsson, 130, 312, 313

many-body, 28 method of lines, 7 mildly stiff, 60 Prothero and Robinson, 262 restricted three–body, 28 Robertson, 15 simple pendulum, 10 stiff, 26, 64, 74, 214, 245, 308, 313, 343, 353 Van der Pol, 16 differential index, 13 differential-algebraic equation, xiv, 10, 36 differentiation, 146 DIFSUB, xiv Dirichlet conditions, 7 DJ-reducibility, 247 Donelson, 380 Dormand, 198, 211 doubly companion matrix, 436, 442

Hairer, xiv, xv, 77, 161, 188, 196, 220,   
240, 241, 258, 267, 280, 281, 356,   
358   
Hamiltonian, 5   
Hansen, 380   
Henrici, 81, 105   
Heun, 93   
hidden constraint, 37   
Higham, 82   
Hirschfelder, 105   
homomorphism, 290   
Hundsdorfer, 361   
Huˇta, 93, 163, 192, 194   
E-polynomial, 231, 270   
eccentricity, 6   
effective order, 273, 302, 365, 436   
efficient extrapolation, 299   
Ehle, 240, 245   
Ehle barrier, 243, 244   
Ehle conjecture, 240   
elementary differential, 150, 151, 156   
elementary differentials   
independence of, 160   
elementary weight, 155, 156   
independence, 163   
elliptic integral, 43   
equivalence, 281   
error constant, 335   
error estimation, 79   
error estimator, 198   
error growth, 335   
error per step, 311   
error per unit step, 311   
Euler, 51   
existence and uniqueness, 22   
ideal, 300   
implementation, 128, 259   
index reduction, 13   
inherent Runge–Kutta stability, 438   
internal order, 182   
internal weights, 157   
interpolation, 131   
invariant, 35   
Iserles, 241

Jackiewicz, 419, 426   
Jacobian, xiv   
Jacobian matrix, 27, 260, 271, 313   
Jeltsch, 247, 248

Kahan, 82   
Kirchgraber, 338   
Kronecker product, 374   
Kutta, 93, 178, 192   
Fehlberg, 198, 208   
Feng, xv   
finger, 78, 241   
forest, 287   
product, 288   
FSAL property, 211, 376   
L-stability, 238, 261, 262, 270, 398   
labelled trees, 144   
Laguerre polynomial, 267   
Laguerre polynomials, 269   
Lambert, J. D., 320   
Lambert, R. J., 122, 380   
Lasagni, 276   
Legendre polynomials, 215   
Leone, 258   
limit cycles, 16   
linear stability, 397   
linear stability function, 246   
Lipschitz condition, 22, 65   
Lobatto IIIA, 376   
Lobatto quadrature, 196, 222   
local extrapolation, 198   
local truncation error, 324, 393, 412   
L´opez-Marcos, 280   
Lotka, 18   
Lubich, xv, 220   
Lundh, 130, 312

matrix convergent, 46 Jordan, 47 power-bounded, 46 stable, 46   
Merson, 93, 198, 201   
method Adams, 105 Adams–Bashforth, xiv, 105, 109, 111, 318, 331, 346, 378 Adams–Moulton, xiv, 91, 105, 109, 111, 330, 378 Almost Runge–Kutta (ARK), 128, 383, 426 stiff, 434 backward difference, 105, 330, 332 collocation, 252 cyclic composite, 380 DESIRE, 273, 275 diagonally implicit, 261 DIMSIM, xiv, 383, 420, 421 types, 421 DIRK, 261, 421 Dormand and Prince, 198, 211 Euler, xiii, 51, 65, 78 convergence, 68 order, 69 Fehlberg, 198, 208 Gauss, 257, 265 general linear, 90, 124 order, 280   
generalized linear multistep, 124   
Gill, 180   
higher derivative, 88, 119   
Huˇta, 163, 192   
hybrid, 122, 380   
implicit, 91   
implicit Euler, 63, 64   
implicit Runge–Kutta, 102   
IRK stable, 442   
Kutta, 192   
leapfrog, 339   
linear multistep, xiv, 87, 105, 107, 377 implementation, 366 order of, 329   
Lobatto, 257   
Lobatto IIIA, 91   
Lobatto IIIC, 265   
Merson, 198, 201   
mid-point rule, 94   
modified multistep, 122   
multiderivative, 90   
multistage, 88, 373   
multistep, 88   
multivalue, 88, 373   
Nordsieck, 368, 371   
Nystr¨om, 105   
Obreshkov, 90, 401   
one-leg, 360, 361, 364, 379   
PEC, 111   
PECE, 111, 378   
PECEC, 111   
PECECE, 111   
predictor–corrector, 105   
predictor-corrector, xiv, 92, 109, 349, 378   
pseudo Runge–Kutta, 122, 123, 380, 382   
Radau IA, 257, 265   
Radau IIA, 257, 265   
reflected, 219   
Rosenbrock, 90, 120   
Runge–Kutta, xiii, xiv, 87, 93, 112, 319, 376 algebraic property, 280 effective order, 303 embedded, 202 equivalence class, 281, 285 Gauss, 238, 252 generalized, 292, 416 group, 284

identity, 286 implementation, 308 implicit, 99, 213, 259 inverse, 286 irreducible, 282 Lobatto IIIC, 238 order, 162 Radau IA, 238 Radau IIA, 238, 252 symplectic, 275 Runge–Kutta (explicit), 170 high order, 195 order 4, 175 order 5, 190 order 6, 192 SDIRK, 261, 421 singly implicit, 266, 268, 270 starting, 112, 318 Taylor series, 89, 114 underlying one-step, 337, 338, 417 Verner, 198, 210 weakly stable, 339 Milne, 105, 112, 339 Milne device, 111 Moir, 433 Moore, 115, 401 Moulton, xiv, 105 Munthe-Kaas, xv Møller, 82

order of tree, 139   
order star, 77, 240, 241   
order stars, 356   
order web, 243   
P-equivalence, 281   
Pad´e approximation, 232, 244   
Pad´e approximation, 120   
periodic orbit, 17   
perturbing method, 302   
Petzold, xv   
$\Phi$ -equivalence, 281   
PI control, 312   
Picard iteration, 154   
Picel, 240   
powers of matrix, 46   
preconsistency, 108, 320, 385   
Prince, 198, 211   
principal moments of inertia, 21   
problem   
discontinuous, 133   
Prothero, 262

quotient group, 301

Neumann conditions, 7   
Newton, 214   
Newton iteration, 214, 308, 313   
Newton method, 42, 91   
non-linear stability, 248   
Nordsieck, 368, 375   
Nordsieck vector, 440   
normal subgroup, 301   
Nørsett, xv, 77, 161, 240, 241, 261, 267,   
356, 358   
Nystr¨om, 93, 105, 192   
Rabinowitz, 20   
Radau code, xiv   
Radau quadrature, 222   
Rattenbury, 433, 434   
reduced method, 247   
relaxation factor, 314   
Richardson, 198   
Riemann surfaces, 356   
RK stability, 420, 423, 424, 432   
Robertson, 15   
Robinson, 262   
Roche, xv   
Romberg, 199   
rooted tree, 96, 137   
Rosenbrock, 90, 120   
round-off error, 80   
rounding error, 80   
Runge, 93   
Runge–Kutta, xiv   
Runge–Kutta group, 287   
Obreshkov, 90   
one-sided Lipschitz condition, 24, 26   
optimal stepsize sequences, 198, 308   
order, 329, 410   
order arrows, 79, 242, 243, 358   
order barrier, 187, 352   
order conditions, 95, 162   
scalar problems, 162   
S-stability, 230   
safety factor, 310   
Sanz-Serna, xv, 276, 280   
Scherer, 220   
Schur criterion, 345, 349   
Shampine, 240   
Sheikh, 361   
similarity transformation, 316   
simplifying assumption, 171   
Singh, 426   
Skeel, 280   
S¨oderlind, 130, 312, 313   
stability, 107, 109, 317, 320, 322, 324,   
326, 342, 385, 386, 388, 390, 396   
stability function, 76, 100, 398, 424   
stability matrix, 397, 424, 432   
stability order, 398, 399   
stability region, 74, 75, 100, 344, 398   
explicit Runge–Kutta, 101   
implicit Runge–Kutta, 102   
stage order, 262   
starting method   
degenerate, 411   
non-degenerate, 411   
Steiniger, 361   
stepsize control, 58, 112   
stepsize controller, 310   
Stetter, 122, 380   
Stoffer, 338, 418   
subgroup, 300   
super-convergence, 19   
superposition principle, 24   
Suris, 276   
symmetry, 148   
symmetry of tree, 140   
symplectic behaviour, 7

Taylor expansion, 153, 159   
Taylor’s theorem, 148   
tolerance, 308   
transformation of methods, 375   
tree, 137   
truncation error, 333 estimation, 390, 419 global, 66, 166, 168, 265, 390 local, 60, 66, 72, 73, 79, 112, 165, 168, 198, 309, 336, 428 built-in estimate, 201 estimate, 91

$V$ transformation, 254, 258   
Van der Pol, 16   
variable order, 308, 318   
variable stepsize, 130, 340, 368, 371, 419   
Verner, 196, 198, 210   
Vitasek, 82   
Volterra, 18   
W transformation, 254   
Wanner, xiv, xv, 77, 161, 220, 240, 241,   
258, 267, 280, 281, 356, 358   
Watanabe, 361   
Watts, 240   
weak stability, 339   
Willers, 115   
Wright, K., 240   
Wright, W. M., 436, 438, 440, 445, 450   
Wronskian, 35

Zahar, 115   
Zanna, xv   
zero spectral radius, 440   
zero-stability, 320
