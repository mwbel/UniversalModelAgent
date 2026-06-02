# Appendix B

As a supplement to this book, additional resources are provided on Springer’s Extra Materials Server http://extra.springer.com/. Owners of the printed book can download a zip archive SatOrbEM.zip after entering the ISBN number. .Downloading this content should require a code given in the printed book

# B.1 Internet Resources

A wealth of data as well as software that could not be provided within this book is available via the Internet and the World Wide Web. We have, therefore, compiled a set of useful URL resources with a focus on data that require frequent updates. All addresses may conveniently be accessed via the hyperlink file SAT.html available in the SatOrbEM.zip archive. Links are ordered by topics and accompanied by brief textual descriptions (cf. Fig. B.1). It is emphasized, however, that the given list is in no way comprehensive and that server names and files are subject to changes without further notice.

![](../chunks/其他影响-Satellite Orbits Models, Methods and Applications (Oliver Montenbruck • Eberhard Gill_part_0005_pages_0281-0350/auto/images/a8485a6c91ac1ffe406d69724622b04f8ff11d202b0fc2888bacceda77cb36f5.jpg)  
Fig. B.1. Useful internet links provided in SAT.html

# B.2 Source Codes on Springer’s Extra Materials Server

# B.2.1 Contents

The SatOrbEM.zip archive on the Extra Materials server provides a comprehensive library of $\mathrm { C } { + + }$ modules as well as programs to solve the exercises given at the end of each chapter. After downloading the archive and unapcking it to a working directory (here C:\Sat) the following directories and files are obtained.

Directory Description   
C:\Sat\Source\ Source codes of library modules (header and implementatio files) SAT_Const.h, SAT_DE.h, SAT_DE.cpp, SAT_Filter.h, SAT_Filter.cpp, SAT_Force.h, SAT_Force.cpp, SAT_Kepler.h, SAT_Kepler.cpp, SAT_RefSys.h, SAT_RefSys.cpp, SAT_Time.h, SAT_Time.cpp, SAT_VecMat.h, SAT_VecMat.cpp Source codes for solutions to exercises Exercise_2_1.cpp, …, Exercise_2_6.cpp, Exercise_3_1.cpp, …, Exercise_3_4.cpp, Exercise_4_1.cpp, …, Exercise_4_3.cpp, Exercise_5_1.cpp, …, Exercise_5_3.cpp, Exercise_6_1.cpp, …, Exercise_6_4.cpp, Exercise_7_1.cpp, Exercise_8_1.cpp, …, Exercise_8_3.cpp Application programs GEODA.cpp, RTOD.cpp, TDRSOD.cpp \InOut\ Output of exercise programs Exercise_2_1.out, …, Exercise_8_3.out Input data for application programs GEODA_A1.inp, …, GEODA_C2.inp, RTOD_A.inp, …, RTOD_C.inp, RTOD.dat, TDRSOD.inp, TDRSOD.dat Output of application programs GEODA_A1.out, …, GEODA_C2.out, RTOD_A.out, …, RTOD_C.out TDRSOD.out \Win32\ Executable programs (Windows 32-bit Version) GEODA.exe, RTOD.exe, TDRSOD.exe \Linux\ Executable programs (Linux Version) GEODA, RTOD, TDRSOD Unix archives of input/output files, executable programs (Linu only) and source code (incl. makefile) satio.tar, satexe.tar, satsrc.tar

The SAT_Lib library comprises elementary operators, functions, and classes, which are common to the various exercises but may also be applied by the reader to develop his/her own applications. In total the library comprises nine modules, each covering a specific and well defined scope:

SAT_Const.h Mathematical and astronomical constants   
SAT_DE.h Numerical integration of differential equations   
SAT_Filter.h Kalman filtering and least-squares estimation   
SAT_Force.h Satellite force model   
SAT_Kepler.h Keplerian orbit computation   
SAT_RefSys.h Reference system transformations   
SAT_Time.h Calendrical computations   
SAT_VecMat.h Vector and matrix arithmetics

Making use of the header files $\mathrm { S A T _ { - } } * .$ h, the required modules can be included into the application programs in an easy way. The associated implementations are provided in the corresponding files SAT_ $^ *$ .cpp , which can be compiled separately and linked in the form of object or library files. Excluded from this is the SAT_Const module, which requires no implementation part and consists of a header file only.

# B.2.2 System Requirements

For a painless application of the programs we recommend the installation on a personal computer with the following minimum characteristics:

• Intel processor 1 GHz or equivalent,   
• 256 MB memory, $1 0 0 \mathrm { M B }$ free hard disk space, CD drive,   
Windows XP/7 or OpenSuSE Linux 10.3 operating system,   
Microsoft Visual Studio 2005 (Windows) or GNU $\mathrm { C } { + } { + } 4 . 2$ (Linux).

# B.2.3 Executing the Programs

The SatOrbEM.zip archive on the Extra Materials server contains pre-compiled versions of the application programs described in Chap. 9. To run these programs on a PC with the Windows operating system unpack the archive as discussed above and copy the files in the C:\Sat\Win32 folder to an appropriate working directory (e.g., C:\Sat\Exe) on the hard disk. The input data files from the folder Sat\InOut folder should then be copied to the same folder. After the command interpreter has been started (by running cmd.exe) and switching to the chosen program folder, the individual programs may be run as in the following example:

Iteration 1

<table><tr><td>Date</td><td>UTC</td><td>Sta TDRS</td><td></td><td>obs</td><td>[m]</td><td>comp [m]</td><td>o-c[m]</td></tr><tr><td></td><td>1999/09/01 00:22:01.000</td><td>162</td><td>5</td><td></td><td></td><td>79010.2586 79010.2408</td><td>17.78</td></tr></table>

For all programs the input files may be specified in the command line (see Table B.1). Using the redirection operator $( > )$ , the default screen output may, furthermore, be written to an arbitrary output file.

Table B.1. Executing the application programs with optional command-line arguments   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Arguments</td><td rowspan=1 colspan=1>Default setup</td><td rowspan=1 colspan=1>Default data</td></tr><tr><td rowspan=1 colspan=1>GEODARTODTDRSOD</td><td rowspan=1 colspan=1>[setup-file] [&gt;output-file][setup-file[data-file]] [&gt;output-file][setup-file[data-file]] [&gt;output-file]</td><td rowspan=1 colspan=1>GEODA.inpRTOD.inpTDRSOD.inp</td><td rowspan=1 colspan=1>RTOD.datTDRSOD.dat</td></tr></table>

The advice just given applies in a similar manner to running the programs under Linux. After creating a suitable directory and copying the files from the unpacked archive, the programs may be started by entering the corresponding program names, provided the working directory is contained in the path. As under Windows, input and output files may be specified in the command line under Linux.

If the names of the input data files are not correctly reproduced under Linux upon reading the CD, there is a Unix tar archive available. This may be unpacked with the commands

tar -xvf /cdrom/Sat/Linux/satio.tar and copied into the current working directory.

# B.2.4 Compilation and Linking

In the sequel, the basic steps for generating executable programs under the Windows and Linux operating systems are described.

For use under the Windows operating system, we assume that all source files are available in a subdirectory C:\Sat\Source\ after unpacking the archive from the Extra Materials Server. Within with Microsoft Visual Studio 2005, the various programs (for exercises and applications) as well as a common library are treated as individual “projects”. These projects are combined in a common workspace or “solution”. After starting Visual Studio, a first project is created through the Project.New Project menu to build the library from the generic modules. This library can later be linked to the individual programs. Within the New Project dialog, an Empty Project is selected from the available templates. Furthermore, the project’s Name (SAT_Lib) as well the desired Location (C:\Sat) and Solution Name (Prj) need to be specified. The latter items define the root directory (C:\Sat\Prj)

for all files maintained by Visual Studio within the current set of projects. Confirm by $O K$ to complete the allocation of this project and the overall workspace. Subsequently the source and header files of the library modules are added to the SAT_Lib project by calling the menu Project.Add Existing Item ... and selecting all files within the C:\Sat\Source\ folder, which adhere to the naming scheme $\mathrm { S A T \_ } * . *$ . By default, Visual Studio will try to build an exectuable program from these source files. Therefore, it is necessary to change the Configuration type in the Configuration Properties.General.Project Defaults field of the Project.Properties menu of the SAT_Lib project from Application (\*.exe) to Static Library (.lib). Now, the library can be completed by selecting the Build.Build SAT_Lib menu. Visual Studio compiles all source files and then links the resulting object files into a static library SAT_Lib.lib.

The Exercises Exercise_2_1 to Exercise_8_3 and the application programs (GEODA, RTOD, TDRSOD) are treated as independent projects within the Sat\Prj workspace. In the sequel this is illustrated for the RTOD program. Start the New Project dialog from the File.Add.New Project menu. Then select an Empty Project, specify its Name (RTOD) and Location (C:\Sat\Prj). Select the new project in the “Solution Explorer”, then add the source file RTOD from the source directory via the Project.Add Existing Item ... dialog. Finally, select the Project.Project dependencies ... menu and check the SAT_Lib check box in the resulting dialog. This makes the respective header files known to the compiler and informs the builder that this library is required for linking the RTOD program. The executable module RTOD.exe is finally created by selecting Build.Build RTOD and can subsequently be found in the C:\Sat\Prj\debug folder. For further hints we refer to the comprehensive documentation of the Microsoft $\mathrm { C } { + } { + }$ compiler and the Visual Studio environment.

Under the Linux operating system the individual programs can directly by built from a console using the GNU $\mathrm { C } { + + }$ compiler. Again, it is advisable to combine all modules $\mathtt { S A T \_ * }$ in a library libSAT.a using the shell commands:

$> \mathrm { g + + \Delta \mathcal { - } c } \ \mathrm { S A T * . c }$ pp # Compilation of library modules $>$ ar rc libSAT.a $\mathtt { S A T * }$ .o # Generation of library from object files

Assuming that all relevant files are contained in the same directory, the main programs can subsequently be built by the commands

$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ Exercise_2_1.cpp -o Exercise_2_1 -lSAT -L.   
$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ Exercise_2_2.cpp -o Exercise_2_2 -lSAT -L.   
$>$ ...   
$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ TDRSOD.cpp -o TDRSOD -lSAT -L.

For ease of use, a make file is provided as part of the satsrc.tar archive, which performs all steps in a single run.

# B.2.5 Index of Library Functions

The following compilation summarizes all identifiers of public types, constants, functions, and classes provided by the individual modules.

$< <$ Output operator for dates, vectors, and matrices   
() Access to vector and matrix components   
$=$ Assignment of vectors and matrices   
$^ +$ Addition of vectors and matrices   
$+ =$ Vector addition   
- Subtraction of vectors and matrices   
- Unary minus (vector, matrix)   
-= Vector subtraction   
$^ *$ Multiplication (scalar, vector, matrix)   
/ Division by a scalar   
abserr Public element of DE class specifying the absolute accuracy requirement   
AccelDrag Acceleration due to atmospheric drag   
AccelHarmonic Acceleration due to harmonic gravity field of central body   
AccelMain Total acceleration of an Earth-orbiting satellite   
AccelPointMass Acceleration due to point-mass perturbation   
AccelSolrad Acceleration due to solar radiation pressure   
Accumulate Method of class LSQ for accumulation of data equations   
Arcs Arcseconds per radian   
AU Astronomical unit [m]   
AzEl Azimuth, elevation and, optionally, partials from local tangential coordinates [m]   
CalDat Calendar date and time   
c_light Velocity of light [m/s]   
Col Column vector of a matrix   
Cov Method of class EKF returning the current covariance   
Cov Method of class LSQ for covariance computation   
Cross Cross product of 3-dimensional vectors   
Date Auxiliary class for output of dates   
Data Method of class LSQ returning the transformed right-hand side of the data equations   
DE Class for numerical solution of differential equations   
DE_BADACC Enumerator of type DE_STATE (Flag for too stringent accuracy requirements)   
DE_DONE Enumerator of type DE_STATE (Flag for successful integration step)   
Define Method of DE class defining the differential equation   
DEfunct Function prototype for differential equations   
Deg $1 8 0 ^ { \circ } / \pi$   
DE_INIT Enumerator of type DE_STATE (Integrator restart)   
DE_INVPARAM Enumerator of type DE_STATE (invalid input parameters)   
Density_HP Atmospheric density based on Harris–Priester model   
DE_NUMSTEPS Enumerator of type DE_STATE (Permitted number of steps exceeded)   
DE_STATE Enumeration type for status codes of class DE inegrator   
DE_STIFF Enumerator of type DE_STATE (Suspect of stiff problem)   
Diag Diagonal matrix from vector of diagonal elements   
Diag Method of Matrix class returning the vector of diagonal elements   
Dot Dot product of two vectors   
Dyadic Dyadic vector product   
EccAnom Eccentric anomaly for elliptic orbits   
EclMatrix Transformation matrix from equator to ecliptic   
EKF Extended Kalman filter class   
Elements Orbital elements from position and velocity   
Elements Orbital elements from two positions   
EqnEquinox Equation of the equinoxes [rad]   
f_Earth Flattening of the Earth   
FindEta Sector–triangle ratio   
GAST Greenwich Apparent Sidereal Time   
Geodetic Class for handling geodetic coordinates   
GHAMatrix Earth rotation matrix   
GM_Earth Product of gravitational constant $\times$ mass of Earth $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GM_Moon Product of gravitational constant $\times$ lunar mass $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GM_Sun Product of gravitational constant $\times$ solar mass $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GMST Greenwich Mean Sidereal Time   
GPS_TAI Method of IERS returning GPS–TAI time difference [s]   
GPS_UTC Method of IERS returning GPS–UTC time difference [s]   
Grav Earth gravity model   
GravModel Data structure for gravity model parameters   
Id Identity matrix   
IERS Class for handling of Earth rotation parameters   
Illumination Fractional illumination of a spacecraft near the Earth   
Init Method of DE class for initialization of a new initial value problem   
Init Method of class EKF for initialization of a Kalman filter   
Init Method of class LSQ for initialization of a least-squares problem (with or without a priori information)   
Integ Method of class DE for performing an integration step   
Intrp Method of class DE for interpolation of solution   
Inv Inversion of general square matrix   
InvUpper Inversion of upper triangular matrix   
LSQ Least-squares estimation class   
LTCMatrix   
LTC_Matrix   
Matrix   
MeanObliquity   
MeasUpdate   
Mjd   
MJD_J2000   
Moon   
Norm   
NutMatrix   
omega_Earth   
PermitTOUT   
pi   
pi2   
PoleMatrix   
Position   
PrecMatrix   
P_Sol   
R_Earth   
R_Moon   
R_Sun   
R_x   
R_y   
R_z   
Rad   
relerr   
RK4   
RK4funct   
Row   
Set   
SetCol   
SetRow   
size   
size1   
Transformation from Greenwich coordinates to local tangential   
coordinates   
Method of class geodetic returning the transformation to local   
tangential coordinates   
Matrix class   
Mean obliquity of the ecliptic   
Method of class EKF performing the measurement update of   
Kalman filter parameters   
Modified Julian Date   
Modified Julian Date at epoch J2000   
Low-precision lunar coordinates   
Euclidean norm of a vector   
Nutation matrix   
Earth rotation rate [rad/s]   
Public element of DE class controlling integration past the spec  
ified output point   
$\pi$   
$2 \pi$   
Polar motion matrix   
Method of class Geodetic computing Cartesian from geodetic   
coordinates   
Precession matrix   
Solar radiation pressure at 1 AU $[ \mathrm { N } / \mathrm { m } ^ { 2 } ]$ 1   
Earth radius [m]   
Lunar radius [m]   
Solar radius [m]   
Matrix describing elementary $x$ -axis rotation   
Matrix describing elementary $y$ -axis rotation   
Matrix describing elementary $z$ -axis rotation   
$\pi / 1 8 0 ^ { \circ }$   
Public element of DE class specifying the relative accuracy re  
quirement   
Class for 4th-order Runge–Kutta integration   
Function prototype for differential equations   
Row vector of a matrix   
Method of class IERS for initialization of Earth orientation pa  
rameters   
Method of Matrix class for assignment of a column vector   
Method of Matrix class for assignment of a row vector   
Method of Vector class returning the number of vector ele  
ments   
Method of Matrix class returning the first dimension (number   
of rows)   
size2 Method of Matrix class returning the second dimension (number of columns)   
slice Method of Vector class for extraction of a sub-vector   
slice Method of Matrix class for extraction of a sub-matrix   
Solve Method of class LSQ for solution of a least-squares problem by backsubstitution   
Sqrt Method of Vector class returning the square-roots of all vector elements   
SRIM Method of class LSQ returning the square-root information matrix   
State Method of class EKF returning the current state vector   
State Position and velocity from Keplerian elements   
State Public element of DE class specifying the current integrator status   
StatePartials Partial derivatives of state vector w.r.t. Keplerian elements   
StdDev Method of class EKF returning the current standard deviation   
StdDev Method of class LSQ for computing the standard deviation of the solution   
Step Method of RK4 class performing a single integration step   
Sun Low-precision solar coordinates   
Time Method of class EKF returning the current time   
TimeUpdate Method of class EKF performing the time update of Kalman filter parameters   
T_J2000 Epoch J2000 (in Julian centuries since J2000)   
Transp Matrix transposition   
TT_TAI Method of IERS class returning TT–TAI time difference [s]   
TT_UTC Method of IERS class returning TT–UTC time difference [s]   
TwoBody State vector propagation and transition matrix for Keplerian orbits   
UTC_TAI Method of IERS returning UTC–TAI time difference [s]   
UT1_UTC Method of IERS returning UT1–UTC time difference [s]   
VecPolar Three-dimensional vector from polar coordinates   
Vector Vector class   
x_pole Matrix of class IERS returning the $x$ -coordinate of the Earth’s pole [rad]   
y_pole Matrix of class IERS returning the $y$ -coordinate of the Earth’s pole [rad]   
A Runge–Lenz vector   
A Cross-section (surface area)   
A Avogadro number   
A Moment of inertia with respect to the $x { - } / y$ -axes   
$A$ Azimuth   
$C$ Moment of inertia with respect to the $z$ -axis   
CD Drag coefficient   
CR Radiation pressure coefficient   
Cnm Potential coefficient   
$\pmb { D }$ Torque vector   
$\pmb { D }$ Diagonal matrix   
D Solar torque vector Mean solar torque vector   
$D$ Mean elongation of the Moon from the Sun   
$E$ Earth-fixed to local-tangent transformation matrix   
E Expectation value   
$E$ Eccentric anomaly   
$E$ Elevation   
$E$ Energy   
ET Ephemeris Time   
$F$ Force vector   
$F$ Mean distance of the Moon from the ascending node of its orbit   
F10.7 Index measuring solar UV radiation at $1 0 . 7 \mathrm { c m }$   
$\textbf { \textit { G } }$ Jacobian matrix (partial derivatives of measurement vector with respect to the state vector)   
$G$ Gravitational constant   
GMST Greenwich Mean Sidereal Time   
$\pmb { H }$ Jacobian matrix (partial derivatives of measurement vector with respect to the epoch state)   
$H _ { 0 }$ Atmospheric density scale height   
$H$ Sun-satellite hour angle   
$H$ Macro step size   
$I$ Moment of inertia   
$J$ Loss function   
$J _ { n }$ Zonal potential coefficient of degree n   
$\mathrm { J D }$ Julian Date   
$\pmb { K }$ Kalman gain   
$K$ Knudsen number   
$K _ { p }$ Three-hourly planetary geomagnetic index   
L0 Mean longitude of the Moon   
$M$ Mean anomaly   
$M$ Mass   
$M _ { 0 }$ Mean anomaly at reference epoch   
MJD Modified Julian Date   
$N$ Nutation matrix   
$N$ Particles per unit volume   
$N$ Auxiliary quantity for transformation of geodetic coordinate   
$N$ Accumulated Doppler counts   
$N$ Integer cycle ambiguity   
$P$ Gaussian vector (in direction of perigee)   
$P$ Precession matrix   
$P$ Covariance matrix   
$P$ Period   
$P _ { n }$ Legendre polynomial of degree n   
Pnm Associated Legendre polynomial of degree $n$ and order $m$   
$P _ { \odot }$ Solar radiation pressure at 1 AU   
$\varrho$ Gaussian vector (perpendicular to perigee)   
$\varrho$ Orthonormal matrix   
$\varrho$ Process-noise covariance matrix   
$\pmb { R }$ Upper triangular matrix   
$\pmb { R }$ Station position vector   
$R _ { x } , R _ { y }$ , $\pmb { R } _ { z }$ Matrices describing rotations around the $x$ , y, z-axes   
$\mathcal { R }$ Universal gas constant   
$R$ Radius of a celestial body   
$R$ Upper triangular matrix   
$R _ { \oplus }$ Equatorial radius of the Earth   
$s$ Sensitivity matrix   
$s$ Square root of the weighting matrix   
$s _ { A }$ Square root of the information matrix   
S Area of sector bounded by two position vectors   
$S _ { n m }$ Potential coefficient   
$T$ Time in Julian centuries since J2000   
$T$ Absolute temperature   
T1,2 Satellite transponder turn-around ratio   
Teqx Epoch of reference equinox in Julian centuries since J2000   
$T _ { n }$ Chebyshev polynomial of order $n$   
$T _ { \infty }$ Exospheric temperature   
TAI International Atomic Time   
TCB Barycentric Coordinate Time   
TCG Geocentric Coordinate Time   
TDB Barycentric Dynamic Time   
TDT Terrestrial Dynamic Time   
TT Terrestrial Time   
$U$ Transformation matrix (inertial to Earth-fixed)   
$U$ Orthonormal matrix   
$U _ { i }$ Elementary Householder transformation matrix   
$U _ { i k }$ Elementary Givens rotation matrix   
$U$ Potential   
$U _ { 2 }$ Potential due to tides   
$U _ { T }$ Potential of tide-induced gravity   
UT Universal Time   
UTC Coordinated Universal Time   
$V$ Orthonormal matrix   
$V _ { n m }$ Potential function   
W Gaussian vector perpendicular to the orbital plane   
W Weighting matrix   
$W _ { n m }$ Potential function   
$X _ { \mathrm { E W } } , Y _ { \mathrm { E W } }$ X/Y-angles using antenna with East/West mount   
$X _ { \mathrm { N S } } , Y _ { \mathrm { N S } }$ X/Y-angles using antenna with North/South mount   
$Z$ Height   
$Z _ { x }$ Height of inflection point   
a Acceleration vector   
$a$ Semi-major axis   
$a$ Ambiguity   
$a$ Albedo of the Earth   
$a _ { i }$ Coefficient of Chebyshev expansion   
aij Runge–Kutta(–Nystrøm) coefficients   
$a _ { p }$ Three-hourly planetary amplitude index   
$a _ { i } ^ { \prime }$ Chebyshev coefficient for derivative of a function   
$^ b$ Ecliptic latitude   
$b _ { i }$ Runge–Kutta(–Nystrøm) coefficients   
$c$ Aerial velocity or specific angular momentum vector   
$c$ Velocity of light ( $c = 2 9 9 7 9 2 4 5 8 { \mathrm { m } } / { \mathrm { s } }$ )   
$c$ Element of Givens rotation matrix   
$c _ { i }$ Runge–Kutta coefficients   
$d _ { i }$ Singular value   
$e$ Unit vector   
$e$ Orbital eccentricity   
$e$ Local truncation error   
$e$ Eccentricity of reference ellipsoid   
$f$ Vector function


<!-- chunk 0006: pages 351-378 -->
$f$ Orbital-plane unit vector   
$f$ Flattening of the Earth $f \approx 1 / 2 9 8 . 2 5 7 )$   
$f$ Frequency   
$\pmb { g }$ Modeled measurement vector   
$\pmb { g }$ Orbital-plane unit vector   
g Gravitational acceleration   
$g _ { j } ( i )$ Coefficient of variable stepsize multistep method   
h Aerial velocity (specific angular momentum) vector   
$\pmb { h }$ Modeled measurement vector   
$h$ Equinoctial element (eccentricity vector component)   
$h$ Altitude (height above reference ellipsoid)   
$h$ Step size   
$i$ Orbital inclination   
$k _ { i }$ Function values for use in Runge–Kutta methods   
$k$ Equinoctial element (eccentricity vector component)   
$\imath$ Angular momentum vector   
$l$ Mean longitude   
$l$ Typical satellite dimension   
$l$ Mean anomaly of the Moon   
$l$ Ecliptic longitude   
$l ^ { \prime }$ Mean anomaly of the Sun   
m Satellite mass   
$\pmb { n }$ Surface normal unit vector   
$n$ Mean motion   
$n$ Particle number density   
$n _ { i j }$ Elements of nutation matrix   
$\pmb { p }$ Polynomial approximation of vector-valued function   
$\pmb { p }$ Force model parameter vector   
$p$ Semi-latus rectum   
$p$ Equinoctial element (inclination vector component)   
$p$ Order of numerical integration method   
$p$ Precession in longitude   
pij Elements of precession matrix   
$p _ { \nu }$ Impulse of a photon   
q Measurement model parameter vector   
$q$ Equinoctial element (inclination vector component)   
$q _ { 0 }$ Fraction by volume of atmospheric constituents   
$r$ Geocentric satellite position vector   
$\dot { \boldsymbol { r } }$ Geocentric satellite velocity vector   
$\ddot { r }$ Geocentric satellite acceleration vector   
$r _ { \odot }$ Geocentric position vector of the Sun   
$r$ Geocentric satellite distance   
s Position vector   
s Satellite position in local tangent coordinates   
s Tide constituent   
$t$ Time   
$t _ { 0 }$ Reference epoch   
$\pmb { u }$ Process noise   
$\pmb { u } _ { i }$ Mid-point rule approximation in extrapolation method   
$u$ Argument of latitude   
$\pmb { v }$ Geocentric satellite velocity vector   
$v$ Geocentric satellite velocity   
$\pmb { w }$ Householder transformation vector   
$x , y , z$ Geocentric satellite coordinates   
${ \ddot { x } } , { \ddot { y } } , { \ddot { z } }$ Geocentric satellite acceleration   
$\hat { x } , \hat { y }$ Satellite coordinates with respect to the orbital plane   
$x _ { \mathrm { p } }$ , yp Pole coordinates   
$x _ { 0 }$ Reference epoch state   
$\pmb { x } _ { 0 } ^ { \mathrm { l s q } }$ Least-squares estimate of reference epoch state   
$\textbf {  { y } }$ State vector   
$\scriptstyle { y _ { 0 } }$ State vector (initial value)   
z Measurement vector   
z Auxiliary angle in description of precession   
z Height in km   
z Measurement   
$z _ { x }$ Height of inflection point in km   
$\varDelta$ Area of triangle formed by two position vectors   
$\varDelta E$ Transfered photon energy   
$\varDelta T$ Ephemeris Time Universal Time difference   
$\varDelta T _ { \infty }$ Exospheric temperature correction   
$\varDelta m$ Mass element   
$\varDelta p$ Transfered photon impulse   
$\varDelta t$ Time interval   
$\varDelta \ v { x } _ { 0 }$ Reference state correction   
$\varDelta z$ Measurement residuals relative to reference orbit   
$\varDelta \varepsilon$ Nutation in ecliptic latitude   
$\varDelta \psi$ Nutation in ecliptic longitude   
$\mathbf { \sigma } _ { \Theta }$ Earth rotation matrix   
$\Theta$ Greenwich sidereal time   
Λ Information matrix   
$\varLambda$ Auxiliary angle in description of precession   
$\pi$ Polar motion transformation matrix   
$\boldsymbol { \Pi }$ Auxiliary angle for description of precession   
$\phi$ GPS code phase   
$\Phi$ Increment function   
$\Phi$ State transition matrix   
$\phi$ Solar radiation flux

Geocentric angle between satellite and apex of density bulge

$\varOmega$ Right ascension (or longitude) of the ascending node   
$\pmb { \alpha }$ Orbital elements vector   
$\alpha$ Right ascension   
$\alpha _ { i }$ Thermal diffusion coefficient   
$\alpha _ { \odot }$ Right ascension of the Sun   
$\beta$ Ecliptic latitude   
$\beta _ { m j }$ Adams–Bashforth coefficient   
$\beta _ { m j } ^ { * }$ Adams–Moulton coefficient   
$\gamma$ Angle   
$\gamma _ { j }$ Adams–Bashforth coefficient   
$\gamma _ { j } ^ { * }$ Adams–Moulton coefficient   
δ Declination   
δ Dirac delta function   
$\delta _ { j }$ Coefficient of Stoermer method   
${ \delta } _ { j } ^ { * }$ Coefficient of Cowell method   
δnm Kronecker symbol $( \delta _ { n m } = \{ { 1 \atop 0 } \}$ for $\left\{ { \begin{array} { l } { n { = } m } \\ { n { \neq } m } \end{array} } \right\} \qquad $   
E Measurement noise vector   
$\epsilon$ Emissivity of the Earth   
$\varepsilon$ Reflectivity   
$\varepsilon$ Mean obliquity of the ecliptic   
$\varepsilon$ Coefficient of reflectivity   
$\varepsilon ^ { \prime }$ True obliquity of the ecliptic   
$\varepsilon _ { j }$ Error coefficient of mid-point rule approximation   
$\zeta$ Auxiliary angle in description of precession   
$\pmb { \eta }$ Numerical approximation of initial value problem   
$\eta$ Ratio of sector to triangle   
$\theta$ Angle between incoming radiation and surface normal   
$\theta _ { s }$ Angle of the weighted sum of Doodson variables   
$\vartheta$ Auxiliary angle in description of precession   
$\kappa$ Love number   
$\kappa _ { n } ^ { \prime }$ Ocean-load deformation coefficient   
$\lambda$ Geocentric longitude (positive towards the East)   
$\lambda$ Mean free path length   
$\lambda$ Error constant of Runge–Kutta–Nystrøm method   
$\lambda$ Wavelength   
$\lambda$ Ecliptic longitude   
μ∗ Ratio of the Earth’s and the Moon’s mass $( \mu ^ { * } \approx 8 1 . 3 )$   
$\nu$ True anomaly   
$\nu$ Shadow function   
$\pi$ 3.1415926…   
$\pi$ Angle between ecliptic of epoch and fixed reference ecl   
$\pmb { \rho }$ Residual vector   
$\rho$ Density   
$\rho$ Range (topocentric distance)   
$\rho _ { \varPhi }$ GPS code pseudorange   
$\rho _ { \phi }$ GPS carrier pseudorange   
$\dot { \rho }$ Range rate (topocentric velocity)   
$\bar { \dot { \rho } }$ Average range rate   
$\sigma$ Fraction of integration step size   
$\sigma _ { i }$ Measurement weight   
$\sigma _ { \varphi }$ Phase noise   
$\sigma _ { \dot { \rho } }$ Range rate noise   
$\tau$ Time within unit interval   
$\tau$ Signal travel time   
$\phi$ Rotation angle   
$\phi$ Geocentric latitude   
$\phi$ GPS carrier phase   
$\phi _ { j } ( i )$ Backward difference of variable stepsize multistep method   
$\varphi$ Geodetic/geographic latitude   
$\varphi ^ { \prime }$ Geocentric latitude   
$\psi$ Lunisolar precession   
$\omega _ { \oplus }$ Angular velocity vector of the Earth   
$\omega$ Argument of perigee (or perihelion)   
$\omega$ Angular velocity   
$\omega$ Inclination of mean equator with respect to reference ecliptic   
$\nabla ^ { n }$ Backwards difference of order $n$   
${ \bf 0 } _ { n \times m }$ Null matrix of dimension $n \times m$   
1n n $n$ -dimensional identity matrix   
$\oplus$ Earth   
$\odot$ Sun   
◦ Degree   
${ \pmb a } \cdot { \pmb b }$ Dot product of two vectors   
$\mathbf { \pmb { a } } ^ { T } \mathbf { \pmb { b } }$ Dot product of two vectors   
AT Transposed matrix   
A−1 Inverse matrix   
A−T Inverse of transposed matrix

The elementary rotation matrices are defined as

$$
\begin{array} { r } { R _ { x } ( \phi ) = \left( \begin{array} { c c } { 1 } & { 0 } & { 0 } \\ { 0 + \cos \phi + \sin \phi } \\ { 0 - \sin \phi + \cos \phi } \end{array} \right) \quad R _ { y } ( \phi ) = \left( \begin{array} { c c } { + \cos \phi 0 - \sin \phi } \\ { 0 } & { 1 } & { 0 } \\ { + \sin \phi 0 + \cos \phi } \end{array} \right) \quad R _ { z } ( \phi ) = \left( \begin{array} { c c } { + \cos \phi + \sin \phi } & { 0 } \\ { - \sin \phi + \cos \phi 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \quad . } \end{array}
$$

# References

Abramowitz M., Stegun I. A.; Handbook of Mathematical Functions; Dover, New York (1965).   
Allgower E. L., Georg K.; Numerical Continuation Methods; SCM13; Springer Verlag, New York (1990).   
Andrews A.; A Square Root Formulation of the Kalman Covariance Equations; AIAA Journal 6, No. 6, 1165–1166 (1968).   
Aoki S., Guinot B., Kaplan G. H., Kinoshita H., McCarthy D. D., Seidelman P. K.; The New Definition of Universal Time; Astronomy and Astrophysics 105, 359–361 (1982).   
Arias E. F., Charlot P., Feissel M., Lestrade J.-F.; The extragalactic reference system of the International Earth Rotation Service, ICRS; Astronomy and Astrophysics 303, 604–608 (1995).   
Ballani L.; Partielle Ableitungen und Variationsgleichungen zur Modellierung von Satellitenbahnen und Parameterbestimmung; Vermessungstechnik, 36. Jg., Heft 6, 192–194 (1988a).   
Ballani L.; Numerische Untersuchungen zur Bestimmung von Parametern des Erdkörpers und von Satellitenbahnen; Vermessungstechnik, 36. Jg., Heft 7, 220–223 (1988b).   
Barlier F., Berger C., Falin J. L., Kockarts G., Thuillier G.; A thermospheric model based on satellite drag data; Ann. Geophys., 34, 9–24 (1978).   
Bate R. R., Mueller D. D., White J. E.; Fundamentals of Astrodynamics; Dover Publications, Inc., New York (1971).   
Battin R. H.; An Introduction to the Mathematics and Methods of Astrodynamics; AIAA Education Series; American Institute of Aeronautics and Astronautics, New York (1987).   
Battin R. H., Levine G. M.; Application of Kalman Filtering Techniques to the Apollo Program; Chap. 14 in Leondes C. T. (ed.); Theory and applications of Kalman filtering; NATO Advisory Group for Aerospace Res. Develop., AGARDograph 139 (1970).   
Bedrich S., Flechtner F., Förste Ch., Reigber Ch., Teubel A.; PRARE System Performance; Proc. 3rd ERS Scientific Symposium (ESA SP-414), Florence, Italy (1997).   
Berger C., Barlier F., Ill M.; Diurnal Variations of the Response of the Equatorial Thermosphere to Geomagnetic Activity; Physica Scripta, 37, 427–431 (1988).   
Bertiger W. I., Bar-Sever Y. E., Christensen E. J., Davis E. S., Guinn J. R., Haines B. J., Ibanez-Meier R. W., Jee J. R., Lichten S. M., Melbourne W. G., Muellerschoen R. J., Munson T. N., Vigue Y., Wu S. C., Yunck T. P., Schutz B. E., Abusali P. A. M., Rim H. J., Watkins M. M., Willis P.; GPS Precise Tracking of TOPEX/POSEIDON: Results and Implications; J. Geophys. Res., TOPEX/POSEIDON Special Issue, 99, No. C12, 24449,–24465 (1994).   
Bertotti B., Farinella P.; Physics of the Earth and the Solar System; Kluwer Academic Publishers, Dordrecht (1990).   
Bhat R. S., Frauenholz R. B., Canelli P. E.; TOPEX/Poseidon Orbit Maintenance Maneuver Design; AAS 89-408, 645–670 (1989).   
Bhat R. S., Frauenholz R. B., Canelli P. E.; TOPEX/Poseidon Orbit Maintenance for the First Five Years; AAS 98-379, 953 (1998).   
Bierman G. J.; Factorization Methods for Discrete Sequential Estimation; Academic Press; New York (1977).   
Bierman G. J.; Bierman K. H.; Estimation Subroutine Library User Guide; FEA Report No. 81584, Factorized Estimation Applications Inc., Sherman Oaks, California (1984).   
Bilitza D., Rawer K., Bossy L., Gulyaeva T.; International Reference Ionosphere – past, present, and future: I. electron density; Adv. Space. Res. 13/3, 3 (1993).   
Bilitza D., Koblinsky C., Beckley B., Zia S., Williamson R.; Using IRI for the Computation of Ionospheric Corrections for Altimeter Data Analysis; Adv. Space. Res. 15/2, 113–119 (1995).   
Black H. D.; An Easily Implemented Algorithm for the Tropospheric Range Correction; Journal of Geophysical Research, 83 No. B4, 1825–1828 (1978).   
Böhnhardt H., Ruder H., Schneider M.; Modelle des Strahlungsdrucks für die Theorie der Satellitenbahnen; Deutsche Geodätische Kommission bei der Bayerischen Akademie der Wissenschaften, Reihe A, Heft 93; München (1981).   
Bohrmann A.; Bahnen künstlicher Satelliten; Bibliographicshes Institut, Mannheim (1963).   
Bomford G.; Geodesy; Clarendon Press, Oxford; 4th ed. (1980).   
Borkowski K. M.; Accurate Algorithms to Transform Geocentric to Geodetic Coordinates; Bulletin Geodetique 63, 50–56 (1989).   
Bowring B. R.; The accuracy of geodetic latitude and height equations; Survey Review 28, 202–206 (1985).   
Brankin R. W., Dormand J. R., Gladwell I., Prince P. J., Seward W. L.; A Runge–Kutta–Nyström Code; Num. Anal. Rep. 136, University of Manchester (1987).   
Brankin R. W., Gladwell I., Dormand J. R., Prince P. J., Seward W. L.; Algorithm 670 – A Runge– Kutta–Nyström Code; ACM Transactions on Mathematical Software, 15/1, 31–40 (1989).   
Branyon S. A., Knowles H. B., Hess G. K. jr.; Kalman Filters in Generic ADA Packages; 6th National Conference on Ada Technology - Washington 1988, U.S. Dept. Commerce, Springfield VA, 365–376 (1988).   
Broucke R. A.; On the Matrizant of the Two-Body Problem; Astronomy and Astrophysics 6, 173–182 (1970).   
Broucke R. A., Cefola P. J.; On the equinoctial orbit elements; Celestial Mechanics 5, 303–310 (1972).   
Brown R. G., Hwang P. Y. C.; Introduction to Random Signals and Applied Kalman Filtering with Matlab Exercises and Solutions; John Wiley & Sons, 3rd ed. (1997).   
Bucerius H.; Bahnbestimmung als Randwertproblem; Astronomische Nachrichten 278, 193–216 (1950).   
Bucy R. S., Joseph P. D.; Filtering for Stochastic Processes with Applications to Guidance; Wiley, New York (1968).   
Bulirsch R., Stoer J.; Numerical treatment of ordinary differential equations by extrapolation methods; Num. Math. 8, 1–13 (1966).   
Butcher J. C.; On Runge–Kutta processes of high order; J. Austral. Math. Soc., IV/2, 179–194 (1964).   
Butcher J. C.; On the attainable order of Runge–Kutta methods; Math. of Comp., 19, 408–417 (1965).   
Butcher J. C.; The non-existence of ten stage eighth order explicit Runge–Kutta methods; BIT, 25, 521–540 (1985).   
Campbell J. K., Synnott S. P., Bierman G. J.; Voyager Orbit Determination at Jupiter; IEEE Transactions on Automatic Control, AC-28, 256–268 (1983).   
Capitaine N., Williams J. G., Seidelmann P. K.; Clarifications concerning the definition and determination of the celestial ephemeris pole; Astronomy and Astrophysics 146, 381–383 (1985).   
Capitaine N., Gontier A.-M.; Accurate procedure for deriving UT1 at a submilliarcsecond accuracy from Greenwich Sidereal Time or from the stellar angle; Astronomy and Astrophysics 275, 645– 650 (1993).   
Carter S. S., Cefola P. J., Proulx R. J.; The Determination of Precision Mean Element Sets from GPS Receiver on-Board Navigation Solutions; AAS 95-371; Advances in the Astronautical Sciences 90, Astrodynamics, pp. 1203 (1995).   
CCSDS; Radio Frequency and Modulation Systems - Part 1 - Earth Stations and Spacecraft; CCSDS 401.0-B Blue Book (1998).   
Cefola P. J.; Equinoctial Orbit Elements - Application to Artificial Satellite Orbits; AIAA/AAS Astrodynamics Conference, Palo Alto, California, Sep. 11–12, 1972; AIAA 72-937, (1972).   
Cicci D. A., Tapley B. D.; Optimal Solution of Unobservable Orbit Determination Problems; Celestial Mechanics 44, 339–363 (1988).   
CIRA; COSPAR International Reference Atmosphere 1972; Compiled by COSPAR Working Group IV, Akademie-Verlag, Berlin (1972).   
CIRA; COSPAR International Reference Atmosphere: 1986 Part I: Thermosphere Models; Advances in Space Research, 8 (1986).   
Chao B. F.; Predictability of the Earth’s Polar Motion; Bull. Géod. 59, 81–93 (1985).   
Clarke A. C.; Extra-Terrestrial Relays; Wireless World, October 1945, pp. 305–308 (1945).   
Clohessy W. H., Wiltshire R. S.; Terminal Guidance system for Satellite Rendezvous; Journal of Aerospace Science 270, 653 (1960).   
Cohen E. R., Taylor B. N.; The 1986 CODATA Recommended Values Of the Fundamental Physical Constants; Journal of Research of the National Bureau of Standards 92, No. 2, 85–95 (1987).   
Colombo O. L.; The Dynamics of Global Positioning System Orbits and the Determination of Precise Ephemerides; Journal of Geophysical Research 94, No. B7, 9167–9182 (1989).   
Cox C., Oza D.; Tracking and Data Relay Satellite (TDRS) Orbit Determination: Operations Concepts for Using Global Positioning System (GPS) Tracking and Alternative Approaches; 553-FDD-94/036/R0UD0, Goddard Space Flight Center, Mission Operations and Data Systems Directorate (1994).   
Cunningham L. E.; On the Computation of the Spherical Harmonic Terms needed during the Numerical Integration of the Orbital Motion of an Artificial Satellite; Celestial Mechanics 2, 207–216 (1970).   
Cunningham J., Curtis V.; WGS84 Coordinate Validation and Improvement for the NIMA and Air Force GPS Tracking Stations; NSWCDD/TR-96/201; Naval Surface Warfare Center, Dahlgren Division; Dahlgren, Virginia (1996).   
Curkendall D. W., Leondes C. T.; Sequential Filter Design for Precision Orbit Determination and Physical Constant Determination; Celestial Mechanics 8, 481–494 (1974).   
Curtis L. E.; High order explicit Runge–Kutta formulae, their uses, and limitations; J. Inst. Maths Applics 16, 35-55 (1975).   
Danby J. M. A., Burkardt T. M.; The Solution of Kepler’s Equation I; Celestial Mechanics, 31, 95-107 (1983).   
Daniell R. E., Brown L. D., Anderson D. N., Fox M. W., Doherty P. H., Decker D. T., Sojka J. J., Schunk R. W.; Parametrized Ionospheric Model: A global ionospheric Parametrization based on First Principles Models Radio Science 30, 1499–1510 (1995).   
Davis E., Dunn C. E., Stanton R. H., Thomas J. B.; The GRACE Mission: Meeting the Technical Challenge; $5 0 ^ { \mathrm { t h } }$ International Astronautical Congress, 4–8 Oct. 1999, Amsterdam; (1999).   
Degnan J. J., Pavlis E. C.; Laser Ranging to GPS Satellites with Centimeter Accuracy; GPS World September 1994, 62–70 (1994).   
DeMets C., Gordon R. G., Argus D. F., Stein S.; Effect of recent revisions to the geomagnetic reversal time scale on estimates of current plate motions; Geophys. Res. Let. 21, 2191–2194 (1994).   
Dershowitz N., Reingold E. M.; Calendrical Calculations; Cambridge University Press, New York (1997).   
Deuflhard P.; On Algorithms for the Summation of Certain Special Functions; Computing 17, 37–48 (1976).   
Deuflhard P.; Order and Stepsize Control in Extrapolation Methods; Numerische Mathematik 41, 399–422 (1983).   
Deuflhard P.; Recent progress in extrapolation methods for ordinary differential equations; SIAM Review 27, 505–535 (1985).   
van Dierendonck A. J., Russell S. S., Kopitzke E. R., Birnbaum M.; The GPS Navigation Message; Navigation 25, No. 2, p. 147–165 (1978).   
Dormand J. R., Prince P. J.; New Runge–Kutta algorithms for numerical simulation in dynamical   
astronomy; Cel. Mech. 18, 223–232 (1978).   
Dormand J. R., Prince P. J.; A family of embedded Runge–Kutta formulae; J. Comp. Appl. Math. 6, No.1, 19–26 (1980).   
Dormand J. R., Prince P. J.; Runge–Kutta–Nyström triples; Comput. Math. Appl., 13, 937–949 (1987).   
Dormand J. R., Prince P. J.; Practical Runge–Kutta Processes; SIAM J. Sci. Stat. Comput., 5, 977–989 (1989).   
Dormand J. R., El-Mikkawy M. E. A., Prince P. J.; High Order Embedded Runge–Kutta–Nyström Formulae; IMA J. Numer. Anal. 7, 423–430 (1987).   
Dow J. M.; Non-singular Partial Derivatives for Synchronous Orbits; ESOC OAD Working Paper No. 22; European Space Operations Centre, Orbit and Attitude Division; Darmstadt (1975).   
Eanes R. J., Schutz B., Tapley B.; Earth and Ocean Tide Effects on Lageos and Starlette; in Proceedings of the Ninth International Symposium on Earth Tides, Kuo J. T. (ed), E. Sckweizerbart’sche Verlagsbuchhandlung, Stuttgart (1983).   
Edenhofer P., Glesner D., Stein V.; Ausbreitungsfehler elektromagnetischer Wellen bei der Bahnvermessung von Erdsatelliten; DFVLR Forschungsbericht 73-56; Oberpfaffenhofen (1973).   
Enright W. H., Jackson K. R., Nørsett S. P., Thomsen P. G.; Interpolants for Runge–Kutta Formulas; ACM Transactions on Mathematical Software, 12, No. 3, 193–218 (1986).   
Enright W. H., Higham D. J., Owren B., Sharp P. W.; A Survey of the Explicit Runge–Kutta Method; Technical Report 291/94, Dept. Computer Science, University of Toronto; revised version; April (1995).   
Escobal P. R.; Methods of Orbit Determination; John Wiley & Sons, Inc., New York (1965). Reprint: Krieger Publishing Company, Malabar, Florida (1976).   
EUMETSAT; The Meteosat System; EUM TD 05 Rev. 3, May 1999 (1999).   
Evans M. J., Maclay T. D.; Mission Design of the ORBCOMM Constellation; in: van der Ha J. C. (ed.), Mission Design & Implementation of Satellite Constellations, 103–112; Kluwer Academic Publishers (1998).   
Fallon L. III; Recursive Least-Squares Estimators and Kalman Filters; Chap. 13.5 in Wertz J. R. (ed.); Spacecraft Attitude Determination and Control; D. Reidel Publishing Company (1978).   
Fehlberg E.; Classical fifth-, sixth-, seventh-, and eighth-order Runge–Kutta formulas with stepsize control; Technical Report NASA TR R-287 (1968).   
Fehlberg E.; Klassische Runge–Kutta–Nyström-Formeln mit Schrittweiten-Kontrolle für Differentialgleichungen $\ddot { { \boldsymbol x } } = f ( t , { \boldsymbol x } , \dot { { \boldsymbol x } } )$ ; Computing 14, 371–387 (1975).   
Feltens J., Dow J. M., Martín-Mur T. J., García Martínez C., Martínez-Fadrique F., Piriz R.; Using GPS for Ionospheric Corrections of ESA Tracking Data; $1 2 ^ { \mathrm { t h } }$ International Symposium on Space Flight Dynamics, SFD 97/17 ESA SP-403, 121–125, Darmstadt (1997).   
Feissel M., Mignard F.; The adoption of ICRS on 1 January 1998: meaning and consequences; Astronomy and Astrophysics 331, L33–L36 (1998).   
Filippi S., Gräf J.; New Runge–Kutta–Nyström formula-pairs of order 8(7), 9(8), 10(9) and 11(10)   
for differential equations of the form $y ^ { \prime \prime } = f ( x , y )$ ; Journal of Computational and Applied Mathematics, 14, 361–370 (1986).   
van Flandern T. C., Pulkkinen K.F.; Low precision formulae for planetary positions; Astrophysical Journal Supplement Series 41, 391 (1979).   
Folkner W. M., Charlot P., Finger M. H., Williams J. G., Sovers O. J., Newhall X. X., Standish E. M. jr.; Determination of the extragalactic-planetary frame tie from joint analysis of radio interferometric and lunar ranging measurements; Astronomy and Astrophysics 287, 279–289 (1994).   
Forman P.; Atomichron: The Atomic Clock from Concept to Commercial Product; Proc. IEEE, Vol. 73, No. 7, 1181 (1985).   
Fox K; Numerical Integration of the Equations of Motion of Celestial Mechanics; Celestial Mechanics 33, 127–142 (1984).   
Frauenholz R. B., Shapiro B. E.; The role of predicted solar activity in TOPEX/POSEIDON orbit maintenance maneuver design; AAS/AIAA Astrodynamics Specialist Conference, AAS 91-515, Durango, Colorado (1991).   
Fricke W., Schwan H., Lederle T., Bastian U., Bien R., Burkhardt G., du Mont B., Hering, R., Jährling R., Jahreiß H., Röser S., Schwerdtfeger H.-M., Walter H. G. Fifth fundamental catalogue (FK5). Part 1. The Basic Fundamental Stars; Veröffentlichungen Astronomisches Rechen-Institut Heidelberg Nr. 32; Verlag G. Braun, Karlsruhe (1988).   
Gaposchkin E. M., Coster A. J.; Evaluation of Thermospheric Models and the Precipitation Index for Satellite Drag; Adv. Space Res., 10, 3303–3309 (1990).   
Gaudenzi De R., Lijphart E. E., Vassallo E.; The New ESA Multi-Purpose Tracking System; ESA Journal 14, 23–40 (1990).   
Gelb A. (ed.); Applied Optimal Estimation; The MIT Press; Massachusetts Institute of Technology; Cambridge, Massachusetts (1974).   
Gendt G., Sorokin N. A.; Probleme bei der numerischen Integration von Satellitenbahnen mit hoher Genauigkeit; Vermessungstechnik, 26. Jg., Heft 9, 291–295 (1978).   
Gerstl M.; Vergleich von Algorithmen zur Summation von Kugelflächenfunktionen; in M. Schneider, Die Arbeiten des SFB 78 Satellitengeodäsie der TU München 1977, 81-88 (1978).   
Gibson R.; A Derivation of Relativistic Effects in Satellite Tracking; TR 83-55, Naval Surface Weapons Center, Dahlgren Virginia (1983).   
Gill E.; Smooth Bi-Polynomial Interpolation of Jacchia 1971 Atmospheric Densities For Efficient Satellite Drag Computation; DLR-GSOC IB 96-1; German Aerospace Center (DLR) (1996).   
Gill E.; Orbit Determination of the MIR Space Station from GPS Navigation Data; $1 2 ^ { \mathrm { t h } }$ International Symposium on Space Flight Dynamics, SFD 97/17 ESA SP-403, 79–84, Darmstadt (1997).   
Gill P. E., Murray W., Wright M. H.; Numerical Linear Algebra and Optimization; Addison-Wesley Publ. Co., California (1990).   
Givens J. W.; Computation of plane unitary rotations transforming a general matrix to triangular   
form; SIAM J. Appl. Math. 6, 26–50 (1958).   
Gladwell I., Shampine L. F., Brankin R.W.; Automatic selection of the initial step size for an ODE solver; Journal of Computational and Applied Mathematics, 18, 175-192 (1987).   
Goad C.C., Goodman L.; A Modified Hopfield Tropospheric Refraction Correction Model; Fall Annual Meeting, Americal Geophysical Union, San Fransisco, CA, Dec. 12–17, (1974).   
Goldstein H.; Classical Mechanics; Addison-Wesley, Reading Mass., 2nd ed. (1980).   
Golub G. H., Reinsch C.; Singular Value Decomposition and Least Squares Solution; Handbook Series Linear Algebra; Numer. Math., 14, 403–420 (1970).   
Golub G. H., van Loan Ch.; Matrix Computations; 2nd edition; The Johns Hopkins University Press, Baltimore (1989).   
Goodman D. T., Bell R. J. (eds.); The International System of Units (SI); U. S. Department of Commerce (1986).   
Goodyear W. H.; Completely general closed-form solution for coordinates and partial derivatives of the two-body problem; Astronomical Journal 70, 189–192 (1965). Erratum: AJ 70, 446 (1965).   
Gragg W. B.; On extrapolation algorithms for ordinary initial value problems; SIAM J. Num. Anal., ser. B, 2, 384–403 (1965).   
van Graas F., Braasch M. S.; Selective Availability; in: Global Positioning System: Theory and Applications; Eds.: Parkinson B. W., Spilker J. J., American Institute of Aeronautics and Astronautics, Washington (1994).   
Green R. M.; Spherical Astronomy; Cambridge University Press; Cambridge (1985).   
Grigorieff R. D.; Numerik gewöhnlicher Differentialgleichungen 2; Teubner Verlag, Stuttgart (1977).   
Großkopf J.; Wellenausbreitung $I { + } U$ ; Hochschultaschenbuch BI 141/141a; Bibliographisches Institut, Mannheim (1970).   
Groten E.; The motion of the Earth; in Landolt-Börnstein, Numerical Data and Functional Relationships in Science and Technology, New Series, Group V, 2a, Springer Verlag, Berlin (1984).   
Guinot B.; Atomic Time; in Kovalevsky J., Mueller I. I., Kolaczek B. (eds.); Reference Frames in Astronomy and Geophysics; Astronomy and Space Science Library Vol. 154, 379–415; Kluwer Academic Publishers (1989).   
Gupta G. K., Sacks-Davis R., Tischer P. E.; A Review of Recent Developments in Solving ODEs; Computing Surveys 17, 5 (1985). Space Structures; The Journal of the Astronautical Sciences, XXV, No.4, 283–306 (1977).   
Hairer E.; A Runge–Kutta Method of Order 10; J. Inst. Maths Applics, 21, 47–59 (1978).   
Hairer E., Nørsett S. P., Wanner G.; Solving Ordinary Differential Equations I; Springer-Verlag, Berlin-Heidelberg-New York (1987).   
Hairer E., Ostermann A.; Dense output for extrapolation methods; Numer. Math. 58, 419–439 (1990).   
Hajj G. A., Kursinski E. R., Bertiger W., Leroy, Romans L., Schofield J. T.; Sensing the atmosphere   
from a low-earth orbiter tracking GPS: early results and lessons from the GPS/MET experiment; Proceedings of the ION GPS-95, Institute of Navigation, Palm Springs, Calif, U.S.A., 12-15,   
Sept., pp. 1167–1174 (1995).   
Hajj G. A., Romans L. J.; Ionospheric Electron Density Profiles obtained from the Global Positioning System: Results from the GPS/MET experiment; Radio Science 33, 175–190 (1998).   
Halain J. P., Welter T., Francken P., Krier G., Wauthier P., Rochus P.; Performance of Least Squares   
and Kalman Filter Algorithms for Orbit Determination using Single- and Multi-Station Tracking of Geostationary Satellites; AAS 98-368; Advances in the Astronautical Sciences 100, Spaceflight Dynamics, pp. 835 (1998).   
Harris I., Priester W.; Time-Dependent Structure of the Upper Atmosphere; NASA TN D-1443; Goddard Space Flight Center, Maryland (1962).   
Hartl Ph.; Fernwirktechnik der Raumfahrt; Springer Verlag, Berlin, Heidelberg, New York (1977).   
Hartl Ph.; The Precise Range and Range Rate Equipment (PRARE) and its Possible Support to the Radar Altimeter Measurements For ERS-1; Proceedings of a Workshop on ERS-1 Radar Altimeter Data Products, Frascati, Italy, ESA SP-221 (1984).   
Hedin A. E.; A Revised Thermospheric Model based on Mass Spectrometer and Incoherent Scatter Data - MSIS-83; Journal of Geophysical Research, 88 10 170–10 188 (1983).   
Hedin A. E.; MSIS-86 Thermospheric Model; Journal of Geophysical Research, 92 4649–4662 (1987).   
Hedin A. E., Salah J. E., Evans J. V., Reber C. A., Newton G. P., Spencer N. W., Kayser D. C., Alcayde D., Bauer P., Cogger L., McLure J. P.; A Global Thermospheric Model based on Mass Spectrometer and Incoherent Scatter Data, MSIS 1, N2 Density and Temperature; Journal of Geophysical Research, 82 2139–2147 (1977).   
Hedin A. E., Spencer N. W., Killeen T. L.; Empirical Global Model of Upper Thermosphere Winds   
Based on Atmosphere and Dynamics Explorer Satellite Data; Journal of Geophysical Research, 93 No. A9, 9959–9978 (1988).   
Hellings R. W.; Relativistic Effects in Astronomical Timing Measurements; Astronomical Journal 91, No. 3, 650–659 (1986); Erratum in Astronomical Journal 92, No. 6, 1446 (1986).   
Henize K. G.; The Baker–Nunn Satellite Tracking Camera; Sky and Telescope 16, 108–111 (1957).   
Henrici P.; Discrete Variable Methods in Ordinary Differential Equations; Wiley, New York (1962).   
Herrick S.; Astrodynamics I & II; Van Nostrand Reinhold, London (1971, 1972).   
Higham D. J.; Defect estimation in Adams PECE Codes; SIAM J. Sci. Stat. Comput. 10, 964–976 (1989).   
Hofmann-Wellenhof B., Lichtenegger H., Collins J.; Global Positioning System – Theory and Practice; Springer-Verlag Wien New York 4th ed. (1997).   
Hopfield H. S.; Two-Quartic Tropospheric Refraction Profile for Correcting Satellite Data; Journal of Geopysical Research 74, 4487–4499 (1969).   
Horn M. K.; Scaled Runge–Kutta Algorithms for Handling Dense Output; DFVLR-FB 81-13;   
Deutsche Forschungs- und Versuchsanstalt für Luft- und Raumfahrt, Oberpfaffenhofen (1981).   
Horn M. K.; Fourth- and fifth-order, scaled Runge–Kutta algorithms for treating dense output; SIAM J. Numer. Anal., 20/3, 558–568 (1983).   
Householder A. S.; Unitary triangularization of a nonsymmetric matrix; J. Assoc. Comp. Mach. 5, 339–342 (1958).   
Hull T. E., Enright W. H., Fellen B. M., Sedgwick A. E.; Comparing numerical methods for ordinary differential equations; SIAM J. Numer. Anal. 9, 603–637 (1972).   
Hussels H.-G.; Schrittweitensteuerung bei der Integration gewöhnlicher Differentialgleichungen mit Extrapolationsverfahren; Diplomarbeit, Köln (1973).   
Husson V.; Global SLR Performance Evaluation; AlliedSignal Technical Services Corporation, NASA SLR Program, Lanham Maryland (1997).   
ICD-GLONASS; Global Navigation Satellite System GLONASS Interface Control Document; Coordination Scientific Information Center; Moscow (1998).   
ICD-GPS-200; Navstar GPS Space Segment / Navigation User Interfaces; Revison C; 25 Sept. 1997; Arinc Research Corp., El Segundo (1997).   
IERS; Explanatory Supplement to IERS Bulletins A and B; International Earth Rotation Service; Paris (1998).   
Ivanov N., Salischev V.; The GLONASS System – An Overview; The Journal of Navigation 45, No. 2, 175–182 (1992).   
Jacchia L. G.; Static Diffusion Models of the Upper Atmosphere with Empirical Temperature Profiles; Smithsonian Contr. Astrophys. 8, No. 9, 215–257 (1965).   
Jacchia L. G.; New Static Models of the Thermosphere and Exosphere with Empirical Temperature Profiles; SAO Special Report 313, Cambridge (1970).   
Jacchia L. G.; Revised Static Models of the Thermosphere and Exosphere with Empirical Temperature Profiles; SAO Special Report 332, Cambridge (1971).   
Jacchia L. G.; Thermospheric Temperature, Density, and Composition: New Models; SAO Special Report 375, Cambridge (1977).   
Jacchia L. G., Slowey J. W.; Analysis of Data for the Development of Density and Composition Models of the Upper Atmosphere; Air Force Geophsyics Laboratory, AFGL-TR-81-0230, Ma. (1981).   
Jackson J.; Monthly Notices of the Royal Astronomical Society 84, 602 (1924).   
Jazwinski A. H.; Stochastic Processes and Filtering Theory; Academic Press, New York (1970).   
Jeske H.; Chap. 7.2/7.3; in Landolt-Börnstein, Numerical Data and Functional Relationships in Science and Technology, New Series, Group V, 4b; Springer Verlag, Berlin (1988).   
Kallemeyn P., Vaughan R.; Observing Doppler to Verify Attitude Behaviour; JPL Interoffice Memorandum IOM 312.3-96-028 (1996).   
Kalman R. E.; A New Approach to Linear Filtering and Prediction Problems; J. Basic Eng. 82, 35–45 (1960).   
Kalman R. E., Bucy R. S.; New Results in Linear Filtering and Prediction Theory; J. Basic Eng. 83D, 95–108 (1961).   
Kaminski P. G., Bryson A. E., Schmidt S. F.; Discrete square root filtering: a survey of current techniques; IEEE Trans. Automatic Control AC-16, No. 6, 727-736 (1971).   
Kaula W. M.; Theory of Satellite Geodesy; Blaisdell Publishing Company, Waltham, Massachusetts (1966).   
Knocke P.C., Ries J.C., Tapley B.D.; Earth Radiation Pressure Effects on Satellites; Proceedings of the AIAA/AAS Astrodynamics Conference, 88-4292-CP, pp. 577–587 (1988).   
King-Hele D.; Satellite orbits in an atmosphere; Blackie and Son Ltd.; London (1987).   
Kinoshita H.; Theory of the Rotation of the Rigid Earth; Celestial Mechanics 15, 277 (1977).   
Kinoshita H., Aoki S.; The Definition of the Ecliptic; Celestial Mechanics 31, 329–338 (1983).   
Kinoshita H., Nakai H.; Numerical Integration Methods in Dynamical Astronomy; Celestial Mechanics 45, 231–244 (1989).   
Kirschner S. M., Beri A. C., Broaddus S. R., Doll C. E.; Spacecraft preliminary orbit determination using tracking measurements obtained from the tracking and data relay satellite system (TDRSS) and the ground spaceflight tracking data network (GSTDN); Space Dynamics Conference, CNES Toulouse, Nov. 89 (1990).   
Kramer H. J.; Observation of the Earth and Its Environment – Survey of Missions and Sensors; Springer Verlag, 3rd ed. (1996).   
Krogh F. T.; VODQ/SVDQ/DVDQ - Variable Order Integrators for the Numerical Solution of Ordinary Differential Equations; JPL Technical Utilization Document CP-2308, NPO-11643 (1969).   
Krogh F. T.; Changing Stepsize in the Integration of Differential Equations Using Modified Differences; in Lecture Notes in Mathematics 362, 22–71, Springer Verlag, New York (1974).   
Kumar M.; World Geodetic System 1984: A Reference Frame for Global Mapping, Charting and Geodetic Applications; Surveying and Land Information Systems 53/1, 53–56 (1993).   
Lafontaine de J., Hughes P.; An Analytic Version of Jacchia’s 1977 Model Atmosphere; Celestial Mechanics, 29, 3–26 (1983).   
Lambert J. D.; Computational Methods in Ordinary Differential Equations; John Wiley and Sons, London (1973).   
Lanyi G.; Tropospheric Propagation Delay Effects in Radio Interferometric Measurements; EOS Transactions, American Geophys. Union 64, pp. 210 (1983).   
Laudet P., Deleuze M., Guitart A., Piuzzi A., Valorge C.; Precise Orbit Determination with DORIS; Carrou J. P. (ed.), Spaceflight Dynamics; Cépaduès-Éditions (1995).   
Lawson C. L.; Applications of Singular Value Analysis; in Rice J. R., Mathematical Software; Academic Press (1971).   
Lawson C. L., Hanson R. J.; Solving Least Squares Problems; Prentice Hall, Englewood Cliffs, New Jersey (1974).   
Lemoine F. G., Kenyon S. C., Factor J. K., Trimmer R. G., Pavlis N. K., Chinn D. S., Cox C. M., Klosko S. M., Luthcke S. B., Torrence M. H., Wang Y. M., Williamson R. G., Pavlis E. C., Rapp R. H., Olson T. R.; The Development of the Joint NASA GSFC and NIMA Geopotential Model EGM96; NASA/GSFC, NASA/TP-1998-206891 (1998).   
Leondes C. T. (ed.); Theory and applications of Kalman filtering; NATO Advisory Group for   
Aerospace Res. Develop., AGARDograph 139 (1970).   
Lerch F. J., Putney B. H., Wagner C. A., Klosko S. M.; Goddard Earth Models for Oceanographic   
Applications (GEM 10B and 10C); Marine Geodesy 5, No. 2, 145–187 (1981).   
Lerch F. J., Nerem R. S., Putney B. H., Felsentreger T. L., Sanchez B. V., Klosko S. M.,Patel G. B., Williamson R. G., Chinn D. S., Chan J. C., Rachlin K. E., Chandler N. L., McCarthy J. J., Marshall J. A., Lutchke S. B., Pavlis D. W., Robbins J. W., Kapoor S., Pavlis E. C.; Geopotential Models from Satellite Tracking, Altimeter, and Surface Gravity Data: GEM-T3 and GEM-T3S; Journal of Geophysical Research 99, 2815–2839 (1994).   
Llewellyn S. K.; Documentation and Description of the Bent Ionospheric Model; Atlantic Science Corporation AD-772 733 (1973).   
Llewellyn S. K., Nesterczuk G., Bent R. B.; Evaluation of the Faraday Rotation Technique for Use in Real Time Ionospheric Modeling; Atlantic Science Corporation NAS5-22353 (1976).   
Lieske J. H.; Precession Matrix based on IAU (1976) System of Astronomical Constants; Astronomy and Astrophysics 73, 282 (1979).   
Lieske J. H., Lederle T., Fricke W., Morando B.; Expressions for the Precession Quantities Based upon the IAU (1976) System of Astronomical Constants; Astronomy and Astrophysics 58, 1 (1977).   
Long A. C., Cappellari J. O., Velez C. E., Fuchs A. J.; Mathematical Theory of the Goddard Trajectory Determination System; Goddard Space Flight Center; FDD/552-89/001; Greenbelt, Maryland (1989).   
Lundberg J. B.; Computational errors and their control in the determination of satellite orbits; Center for Space Research, Univ. of Texas at Austin, CSR-85-3 (1985).   
Lundberg J. B.; Mitigation of Satellite Orbit Errors Resulting from the Numerical Integration Across Shadow Boundaries; Proceedings of the AAS/AIAA Astrodynamics Conference 1996, Halifax, AAS 96-408, pp. 1701–1719 (1996).   
Malys S., Slater J.; Maintenance and Enhancement of the World Geodetic System 1984; Proc. ION GPS-94, Sept. 1994, Salt Lake City, Utah; The Institute of Navigation (1994).   
Malys S., Slater J., Smith R., Kunz L., Kenyon S.; Status of the World Geodetic System 1984; Proc. ION GPS-97; Sept. 1997, Kansas City, Missouri; The Institute of Navigation (1997).   
Manabe S. T., Sato T., Sakai S., Yokoyama K.; Atmospheric Loading Effects on VLBI Observations; in: Proceedings of the AGU Chapman Conference on Geodetic VLBI: Monitoring Global Change, NOAA Tech. Rep. NOS 137 NGS 49, 111–122 (1991). ng techniques; AAS 89-419 (1989).   
Marini J. W.; The Effect of Satellite Spin on Two-Way Doppler Range-Rate Measurements; IEEE Trans. Aerospace and Electronic Systems 7, 316–320 (1970).   
Marini J. W.; Correction of satellite tracking data for an arbitrary tropospheric profile; Radio Science 7, 223-231 (1972).   
Markowitz W., Hall R. G., Essen L., Perry J. V. L.; Frequency of Cesium in Terms of Ephemeris Time; Physical Review Letters 1, 105 (1958).   
Marsh J. G., Lerch F. J., Putney B. H., Christodoulidis D. C., Smith D. E., Felsentreger T. L., Sanchez B. V., Klosko S. M., Pavlis E. C., Martin T. V., Robbins J. W., Williamson R. G., Colombo O. L., Rowlands D. D., Eddy W. F., Chandler N. L., Rachlin K. E., Patel G. B., Bhati S., Chinn D. S.; A New Gravitational Model for the Earth from Satellite Tracking Data: GEM-T1; Journal of Geophysical Research 93, 6169–6215 (1988).   
Marsh J. G. et al.; The GEM-T2 Gravitational Model; Journal of Geophysical Research 95, 22043– 22070 (1990), Correction: Journal of Geophysical Research 96, 16651 (1991).   
Marshall J. A., Antreasian P. G., Rosborough G. W., Putney B. H.; Modeling Radiation Forces Acting on Satellites for Precision Orbit Determination; AAS/AIAA Astrodynamics Specialist Conference, Durango Co., AAS 91-357 (1991).   
Marshall J. A., Klosko S. M., Reis J. C.; Dynamics of SLR Tracked Satellites; Rev. Geophys. 33 Suppl. (1995).   
Marshall J. A., Lerch F. J., Luthcke S.B., Williamson R.G., Chan J.C.; An Assessment of TDRSS for Precision Orbit Determination; The Journal of the Astronautical Sciences, 44, No.1, 115-127 (1996).   
Mass J., Vassy E.; Doppler Effect of Artificial Satellites; Advances in Space Science and Technology 4, 1–38 (1962)   
Matossian M. G.; A TELEDESIC Space Infrastructure Overview; in: van der Ha J. C. (ed.), Mission Design & Implementation of Satellite Constellations, 153–156; Kluwer Academic Publishers (1998).   
May J. A.; A Study of the Effects of State Transition Matrix Approximations; Proceedings of a Symposium held at Greenbelt, MD, Oct. 17–18, 1979; NASA CP 21123, NASA/GSFC, (1980).   
Mayaud P. N.; Derivation, Meaning, and Use of Geomagnetic Indices; American Geophysical Union, Geophysical Monograph 22, Washington D.C. (1980).   
McCarthy D. D.; IERS Standards (1992); IERS Technical Note 13; Central Bureau of IERS - Observatoire de Paris; Paris (1992).   
McCarthy D. D.; IERS Conventions (1996); IERS Technical Note 21; Central Bureau of IERS - Observatoire de Paris; Paris (1996).   
McCarthy J. J., Rowton S., Moore D., Pavlis D., Luthcke S. B., Tsaoussi L.; GEODYN II Systems Description; NASA Goddard Space Flight Center, Greenbelt Maryland (1993).   
McCoubrey A. O.; History of Atomic Frequency Standards: A Trip Through 20th Century Physics; Proceedings of the 1996 IEEE International Frequency Symposium, pp. 1225-1241 (1996).   
McNish A. G., Lincoln J. V.; Prediction of Sunspot Numbers; Trans. Am. Geophys. Union 30, 673–685 (1949).   
Merson R. H.; RAE Technical Report 74184, Royal Airforce Establishment (1974).   
Meeus J.; Astronomical Formulae for Calculators; Volksterrenwacht Urania, Belgium (1978).   
Meeus J.; Astronomical Algorithms; Willmann-Bell, Inc.; Richmond, Virginia (1991).   
Milani A., Nobili A. M., Farinella P.; Non-gravitational perturbations and satellite geodesy; Adam Hilger, Bristol (1987).   
Misra P. N., Abbot R. I., Gaposchkin E. M.; Transformation Between WGS-84 and PZ-90; Proc. ION GPS-96, 307–314; 17–20 Sept. 1996, Kansas City, Missouri; The Institute of Navigation (1996).   
Mitrikas V., Revnivykh S., Bykhanov E., WGS84/PZ90 Transformation Parameters Determination Based on Laser and Ephemeris Long-Term GLONASS Orbital Data Processing; ION GPS-98, September 15–18, 1998, Nashville; pp. 1625 (1998).   
Montenbruck O.; Practical Ephemeris Calculations; Springer Verlag, Heidelberg (1989).   
Montenbruck O., Pfleger T.; Astronomy on the Personal Computer; Springer Verlag, Heidelberg; 4th edition (2000).   
Moore H.; Comparison of Numerical Integration Techniques for Orbital Applications; in Bettis D. G., Proceedings of the Conference on the Numerical Solution of Ordinary Differential Equations, 19/20 Oct. 1972, Texas; Lecture Notes in Mathematics 362, p.149, Springer Verlag (1974).   
Moritz H.; Geodetic Reference System 1980; Bulletin Geodesique 54/3, 395–405 (1980).   
Moyer T. D.; Mathematical Formulation of the Double Precision Orbit Determination program (DPODP); JPL Technical Report 32-1527 (1971);   
Moyer G.; The Origin of the Julian Day System; Sky and Telescope 61, 311–313 (1981).   
Mueller A. C.; Jacchia–Lineberry Upper Atmosphere Density Model; Johnson Space Center Internal Note No. 82-FM-52, JSC-18507 (1981).   
Mueller I. I.; Spherical and Practical Astronomy as Applied to Geodesy; F. Ungar Publ. Co., New York (1969).   
Mueller I. I.; Transformations between Celestial and Terrestrial Reference Frames; in Kovalevsky J. et al. (ed.), Reference Frames in Astronomy and Geophysics, 287-294; Kluwer Academic Publishers, Dordrecht (1989).   
Mugellesi R., Kerridge D. J.; Prediction of Solar and Geomagnetic Activity for Low-Flying Spacecraft; ESA Journal 15, 123-134 (1991).   
Nagel E., Reigber Ch.; Verwendung der Atmosphärenmodelle CIRA65 und CIRA72 in der Bahnbestimmung geodätischer Satelliten; Forschungsbericht BMFT-FB W 73-11; Inst. Astron. Physik. Geodäsie TU München, Bundesministerium für Forschung und Technologie (1973).   
Nerem R. S., Lerch F. J., Marshall J. A., Pavlis E. C., Putney B. H., Tapley B. D., Eanes R. J., Ries J. C., Schutz B. E., Shum C. K., Watkins M. M., Klosko S. M., Chan J. C., Luthcke S. B., Patel G. B., Pavlis N. K., Williamson R. G., Rapp R. H., Biancle R., Nouel F.; Gravity Model Development for TOPEX/POSEIDON: Joint Gravity Models 1 and 2; Journal of Geophysical Research 99, 24421–24447 (1994).   
Nerem R. S., Jekeli C., Kaula W. M.; Gravity Field Determination and Characteristics: Retrospective and Prospective; Journal of Geophysical Research 100, 15053–15074 (1995).   
Newcomb S.; Tables of the motion of the Earth on its Axis and around the Sun; Astronomical Papers of the American Ephemeris Vol. VI/1, 1–170, Washington (1898).   
Newhall X. X.; Numerical representation of planetary ephemerides; Celestial Mechanics 45, 305- 310 (1989).   
Newhall X. X., Standish E. M., Williams J. G.; DE102: a Numerically Integrated Ephemeris of the Moon and Planets Spanning Fourty-four Centuries; Astron. Astroph. 125, 150–167 (1983).   
NIMA; Department of Defense World Geodetic System 1984 – Its Definition and Relationships with Local Geodetic Systems; NIMA TR 8350.2, 3rd ed., 4 July 1997; National Imagery and Mapping Agency; Bethesda, Maryland (1997).   
NIMA; Earth Orientation Parameter Prediction Description; http://164.214.2.59/GandG/sathtml/eoppdoc.html; Revision May 1999; (1999).   
Nisbet J. S.; On the Construction and Use of a Simple Ionospheric Model; Radio Science 6, 437–464 (1974).   
Noordung H.; Das Problem der Befahrung des Weltraums - Der Raketenmotor; Richard Carl Schmidt & Co., Berlin W62 (1929).   
Nostrand P. M.; Forecast Verification of the 10.7 Centimeter Solar Flux and the $A _ { p }$ Daily Geomagnetic Activity Indices; Report No. AD-A152959, Department of the Air Force, Air Force Institute of Technology, Ohio (1984).   
NRC; The Global Positioning System: A Shared National Asset; National Academy Press, Washington, D.C. (1995).   
Oza D. H., Jones T. L., Hodjatzadeh M., Samii M. V., Doll C. E., Hart R. C., Mistretta G. D.; Evaluation of TDRSS-User Orbit Determination Accuracy Using Batch Least-Squares and Sequential Methods; 3rd International Symposium on Spacecraft Flight Dynamics, Darmstadt Sep/Oct. 1991; (1992).   
Parkinson B. W.; GPS Error Analysis; in: Global Positioning System: Theory and Applications; Eds.: Parkinson B. W., Spilker J. J., American Institute of Aeronautics and Astronautics, Washington (1994).   
Pensa A. F., Sridharan R.; Monitoring Objects in Space with the U.S. Space Surveillance Network; International Workshop on Mission Design and Implementation of Satellite Constellations; Astrodynamics Committee of the International Astronautical Federation; Toulouse, November 17–19 (1997).   
Pizzicaroli J. C.; Launching and Building the IRIDIUM Constellation; in: van der Ha J. C. (ed.), Mission Design & Implementation of Satellite Constellations, 113–121; Kluwer Academic Publishers (1998).   
Press W. H., Flannery B. P., Teukolsky S. A., Vetterling W. T.; Numerical Recipes in $C$ - The Art of   
Scientific Computing; Cambridge University Press; Cambridge; 2nd ed. (1992).   
Prince P. J., Dormand J. R.; High order embedded Runge–Kutta formulae; J. Comp. Appl. Math. 7, 67–75 (1981).   
Radomski M. S., Doll C. E.; Differenced Range Versus Integrated Doppler (DRVID) Ionospheric Analysis of Metric Tracking in the Tracking and Data Relay Satellite System (TDRSS); NASA Conference Publication 3299, Flight Mechanics/Estimation Theory Symposium, Greenbelt (1995).   
Raol J. R., Sinha N. K.; On the Orbit Determination Problem; IEEE Transactions on Aerospace and Electronic Systems AES-21 No. 3, 274-290 (1985).   
Rapp R. H.; Combination of Satellite, Altimetric and Terrestrial Gravity Data; in Sanso F., Rummel R.; Theory of Satellite Geodesy and Gravity Field Determination; Springer Lecture Notes in Earth Sciences 25; Springer Verlag, Berlin (1989).   
Reigber Ch.; Überblick über Stand und Entwicklung von Erdschweremodellen zur präzisen Bahnbestimmung bei geodynamischen Anwendungen; in Schneider M., Satellitengeodäsie – Ergebnisse aus dem gleichnamigen Sonderforschungsbereich der Technischen Universität München; VCH Verlagsgesellschaft, Weinheim (1990).   
Rice D. R.; An Investigation into the Effects of Using Simplified Force Models in the Computation of State Transistion Matrices; AIAA Paper 67-123; AIAA 5th Aerospace Sciences Meeting, New York, Jan. 23-26 (1967).   
Ries J. C., Eanes R. J., Huang C., Schutz B. E., Shum C. K., Tapley B. D., Watkins M. M., Yuan D. N.; Determination of the Gravitational Coefficient of the Earth from Near-Earth satellites; Geophysical Research Letters 16, No. 4, 271–274 (1989).   
Roberts C. E.; Densities Based Upon Jacchia’s 1970 Models; Celestial Mechanics 4, 368–377 (1971).   
Rowlands D. D., Luthcke S. B., Marshall J. A., Cox C. M., Williamson R. G., Rowton S. C.; Space Shuttle Precision Orbit Determination in Support of SLA-1 Using TDRSS and GPS Tracking Data; The Journal of the Astronautical Sciences 45 (1997).   
Rubincam D. P.; On the Secular Decrease in the Semimajor Axis of LAGEOS’s Orbit; Celestial Mechanics, 361 (1981).   
Sanchez B. V.; Rotational Dynamics of Mathematical Models of the Nonrigid Earth; AMRL 1066; Department of Aerospace Engineering and Engineering Mechanics, The University of Texas at Austin (1974).   
Schamberg R.; A new analytic representation of surface interaction for hyperthermal free molecule flow; Rep. RM-2313, Rand Corp., Santa Monica (1959).   
Schastok J., Gleixner H., Soffel M., Ruder H., Schneider M.; The Ephemeris Program GLE2000 Comp. Phys. Commun. 54, 167–170 (1989).   
Schatten K. H., Scherrer P. H., Svalgaard L., Wilcox J. M.; Using Dynamo Theory to predict the Sunspot Number during Solar Cycle 21; Geophysical Research Letters 5, 411–414 (1978).   
Schatten K. H., Pesnell W. D.; An Early Solar Dynamo Prediction: Cycle23 - Cycle 22; Geophysical Research Letters 20, 2275–2278 (1993).   
Schatten K. H.; Predicted Solar Data as of January 1, 1999; http://envnet.gsfc.nasa.gov/Models/Schatten_Predicitions_01-99.html; (1999).   
Schmid P. E., Lynn J. J.; Satellite Doppler-Data Processing using a Microcomputer; IEEE Transactions on Geoscience Electronics, GE-16, No. 4, 340–349 (1978).   
Schoenmaekers J.; Cluster: Fuel-optimum Spacecraft Formation Control; 3rd International Symposium on Spacecraft Flight Dynamics, 30 Sep. – 4 Oct. 1991, Darmstadt; ESA SP-326 (1991).   
Schubart J., Stumpff P.; On an n-body program of high accuracy for the computation of ephemerides of minor planets and comets; Veröffentlichungen des Astronomischen Rechen-Instituts Heidelberg Nr. 18 (1966).   
Schutz B. E., Tapley B. D.; UTOPIA: University of Texas Orbit Processor; Department of Aerospace Engineering and Engineering Mechanics, University of Texas at Austin, TR 80-1 (1980).   
Schwarz H. R.; Numerische Mathematik; B. G. Teubner, Stuttgart (1988).   
Schwiderski E.; Atlas of Ocean Tidal Charts and Maps, Part I: The Semidiurnal Principal Lunar Tide M2; Marine Geodesy 6, 219–256 (1983).   
Sconzo P.; Explicit Expressions for the 36 Terms of a Jacobian Matrix used in Orbit Computations; Mem. della Soc. Astr. Ital.; (1963).   
Sedgwick A. E.; An effective variable order variable step Adams method; Ph. D. Thesis, Tech. Rep. No. 53, Departement of Computer Science, University of Toronto (1973).   
Seeber G.; Satellitengeodäsie; Walter de Gruyter, Berlin (1989).   
Segura R.; Analysis of Rosetta RSI Ground Station Requirements; TOS/ONN/981103/RS; ESA, ESOC, Darmstadt (1998).   
Seidelmann P. K.; 1980 IAU Theory of Nutation: The Final Report of the IAU Working Group on Nutation; Celestial Mechanics 27, 79–106 (1982).   
Seidelmann P. K. (ed.); Explanatory Supplement to the Astronomical Almanac; University Science Books, Mill Valley, California (1992).   
Seidelmann P. K.; The International Celestial Reference System; AAS/AIAA Spaceflight Mechanics Meeting, 9–11 Feb. 1998, Monterey CA; (1998).   
Seidelmann P. K., Fukushima T.; Why new time scales?; Astronomy and Astrophysics 265, 833–838 (1992).   
Sehnal L.; Thermospheric Total Density Model TD; Bull. Astron. Inst. Czechosl. 39, 120–127 (1988).   
Sehnal L.; Comparison of the Thermosphere Total Density Model TD 88 with CIRA 86; Adv. Space Res. 10 No. 6, pp.(6)27–(6)31 (1990).   
Sehnal L., Pospí˘silová L.; Thermospheric Model TD88; Astronomical Institute, Czechoslovak Academy of Sciences, Observatory Ond˘rejov, Prepr. No. 67 (1988).   
Shampine L. F.; Interpolation for Runge–Kutta methods; SIAM J. Numer. Anal., 22, 1014–1027 (1985).   
Shampine L. F., Gordon M. K.; Computer Solution of Ordinary Differential Equations; Freeman and Comp., San Francisco (1975).   
Shampine L. F., Watts, H. A.; DEPAC - Design of a user oriented package of ODE solvers; SAND79- 2374, Sandia Laboratories (1979).   
Shampine L. F., Baca L. S., Bauer H.-J.; Output in Extrapolation Codes; Tech. Rep. 196 SFB 123, Univ. Heidelberg (1982).   
Sharp P. W., Verner J. H.; Generation of high-order interpolants for explicit Runge–Kutta pairs; ACM Transactions on Mathematical Software 24, No. 1, 13–29 (1998).   
Shepperd S. W.; Universal Keplerian State Transition Matrix; Celestial Mechanics 35, 129–144 (1985).   
Smith G. R.; A Simple Efficient Starting Value for the Iterative Solution of Kepler’s Equation; Celestial Mechanics 19, 163 (1979).   
Smith D. E., Dunn P.; Long term evolution of the LAGEOS orbit; Geophysical Research Letters 7, 437–440 (1980).   
SN; Space Network Users’ Guide; 530-SNUG, NASA Goddard Space Flight Center, Rev. 7 (1995). berg (1989).   
Soffel M. H., Brumberg V. A.; Relativistic Reference Frames Including Time Scales; Celestial Mechanics and Dynamical Astronomy 52, 355–373 (1991).   
Soop E. M.; Introduction to geostationary orbits; ESA SP-1053 (1983).   
Soop E. M.; Handbook of Geostationary Orbits; Kluwer Academic Publishers Dordrecht, Boston, London (1994).   
Spilker J. J.; GPS Signal Structure and Performance Characteristics; Navigation 25 121–146 (1978).   
Spilker J. J.; GPS Navigation Data; in: Global Positioning System: Theory and Applications; Eds.: Parkinson B. W., Spilker J. J., American Institute of Aeronautics and Astronautics, Washington (1994).   
Springer T. A., Beutler G., Rothacher M.; Improving the orbit estimates of GPS satellites; Journal of Geodesy 73, 147–157 (1999).   
Standish E. M.; Orientation of the JPL Ephemerides, DE 200/LE 200, to the Dynamical Equinox of J2000; Astronomy and Astrophysics 114, 297–302 (1982).   
Standish E. M.; User’s Guide to the JPL Lunar and Planetary Ephemeris Export Package; Jet Propulsion Laboratory (1985).   
Standish E. M.; The Observational Basis for JPL’s DE200, the Planetary Ephemeris of the Astronomical Almanac; Astron. Astroph. 233, 252–271 (1990).   
Standish E. M.; JPL Planetary and Lunar Ephemerides, DE405/LE405; JPL Interoffice Memorandum IOM 312.F–98–048, Aug. 26 (1998).   
Standish E. M., Newhall X. X., Williams J. G., Folkner W. F.; JPL Planetary and Lunar Ephemerides, DE403/LE403; JPL IOM 314.10-127 (1995)   
STDN; STDN Operations Concept; 451-OCD-STDN, NASA Goddard Space Flight Center, Rev. 5 (1998).   
Stein V.; Modelle der ionosphärischen Elektronendichteverteilung zur Korrektur von Ausbreitungsfehlern elektromagnetischer Wellen; DFVLR-Mitt. 82-03, Oberpfaffenhofen (1982).   
Stoer J., Bulirsch R.; Introduction to Numerical Analysis; Springer Verlag; 2nd ed. (1983).   
Swerling P.; A Proposed Stagewise Differential Correction Procedure for Satellite Tracking and Prediction; The Journal of the Astronautical Sciences 6, (1959).   
Taff L. G.; Celestial Mechanics: A Computational Guide for the Practitioner; John Wiley & Sons; (1985).   
Taff L. G., Brennan T. A.; On Solving Kepler’s Equation; Celestial Mechanics and Dynamical Astronomy 46, 163-176 (1989).   
Tapley B. D.; Statistical Orbit Determination Theory; in Tapley B. D., Szebehely V. (eds.), Recent Advances in Dynamical Astronomy; D. Reidel Publ. Co., Dordrecht-Holland (1973).   
Tapley B. D.; Fundamentals of Orbit Determination; in Sanso F., Rummel R.; Theory of Satellite Geodesy and Gravity Field Determination; Springer Lecture Notes in Earth Sciences 25, 235-260; Springer Verlag, Berlin (1989).   
Tapley B. D., Ries J. C., Davis G. W., Eanes R. J., Schutz B. E., Shum C. K., Watkins M. M.; Precision Orbit Determination for TOPEX/POSEIDON; J. Geophys. Res., TOPEX/POSEIDON Special Issue, 99, No. C12, 24 383-24 404 (1994).   
Tapley B. D., Watkins M. M., Ries J. C., Davis G. W., Eanes R. J., Poole S. R., Rim H. J., Schutz B. E., Shum C. K., Nerem R. S., Lerch F. J., Marshall J. A., Klosko S. M., Pavlis N. K., Williamson R. G.; The Joint Gravity Model 3; Journal of Geophysical Research 101, 28029-28049 (1996).   
Tapley B. D., Bettadpur S., Watkins M., Reigber C., The gravity recovery and climate experiment: Mission overview and early results; Geophys. Res. Lett. 31/9, L09607 (2004a).   
Tapley B. D., Schutz B. E., Born George H.; Statistical Orbit Determination; Elsevier Academic Press, Amsterdam (2004b).   
Torge W.; Geodesy; W. de Gruyter, Berlin, New York, 2nd ed. (1991).   
Tsiolkovsky K. E.; Outside the Earth (1918); engl. transl. in: The Call of the Cosmos, Moscow (1960).   
Vallado D. A.; Fundamentals of Astrodynamics and Applications; McGraw-Hill; New York (1997).   
Vessot R. F. C.; Lectures on frequency stability and clocks; in Bertotti B., ed.; Experimental Gravitation, 111–162; Academic Press, New York (1974).   
Wahr J. M.; The Forced Nutations of an Elliptical, Rotating, Elastic, and Oceanless Earth; Geophys. J. R. Astr. Soc. 64, 705 (1981).   
Watts H. A.; Starting step size for an ODE solver; Journal of Computational and Applied Mathematics, 9, 177–191 (1983).   
Watts H. A., Shampine L. F.; Smoother interpolants for Adams codes; SIAM J. Sci. Stat. Comput. 7, 334-345 (1986).   
Weinberg S.; Gravitation and Cosmology; Wiley, New York (1972).   
Wintner A.; The Analytical Foundations of Celestial Mechanics; Princeton University Press (1941).   
Wolf P., Petit G.; Relativistic clock theory for clock syntonization and the realization of geocentric coordinate times; Astronomy and Astrophysics 304, 653–661 (1995).   
Woolard E. W.; Theory of the Rotation of the Earth Around its Center of Mass; Astronomical Papers for the American Ephemeris XV/1; Washington (1953).   
Wright J. R.; Sequential Orbit Determination with Auto-Correlated Gravity Modeling Errors; Journal of Guidance and Control 4, 304 (1981).   
Zarrouati O.; Trajectoires Spatiales; CNES, Cepadues Editions (1987).   
Zhu S. Y., Reigber C., Kang Z.; Apropos laser tracking to GPS satellites; Journal of Geodesy 71 423–431 (1997).

# Index

A priori   
– covariance 268,280   
– information 266,277   
– information matrix 270   
– standard deviation 307,314   
– state 279,287,306   
– weight 268   
Aberration 210,234   
Absorption 77   
– line 161   
Acceleration 15   
– due to drag 84   
– due to Earth radiation 108   
– due to gravity 68   
– due to Moon 69   
– due to point mass 69   
– due to solar radiation pressure 79   
– due to Sun 69   
– due to thrust 105   
– empirical 112   
– partials 244   
– post-Newtonian formulation 111   
Accuracy   
– of angle measurements 196   
– of range measurements 197–199   
– of range rate data 198,199   
Adams–Bashforth method 133   
Adams–Moulton method 136   
Aerodynamic drag 83,243   
– partials 248   
Albedo 107   
Allen variance 202   
Almanac 208,324,325   
Altimeter 62   
Ambiguity 197,215   
– resolution 207,215   
Ammonium 161   
Amplitude modulation 194   
Angle measurement 193,194,196,20   
Angular momentum 16,54   
– of orbit 53   
– of the Earth 172   
– relativistic effects 110   
Anomaly   
– eccentric 22,29   
– mean 23,43   
– true 18,29,43   
Antapex 90   
Antenna   
– aperture 194   
– beamwidth 196   
– feed 194   
– mount 212   
Anti-Spoofing 205   
Aperture 194   
Apex 90   
Apogee 18,47   
Apollo 258   
Area-to-mass ratio 85   
Areal velocity 17,28   
Argument   
– of latitude 27,29,43   
– of perigee 26,29   
– secular change 35   
Ariane 34,48   
Ascending node 26,28,42   
– secular change 35,50   
Atmosphere 87   
– drag 83   
– hypersonic flow 84   
– wind model 85   
Atmospheric drag 243   
Atomic clock 161   
Atomic Time 158,161   
Attitude models 106   
Autotrack mode 194   
Azimuth 37,194,212   
– partials 251   
Back-substitution 270   
Backward differences 134,142   
Baker–Nunn camera 61   
Barycenter   
– Earth-Moon system 76,160   
– solar system 76,164   
Barycentric Coordinate Time 164   
Barycentric Dynamical Time 164   
Batch estimation 276   
Beamwidth of the antenna 196   
Bias 298   
– estimation 196   
BIH 162,183   
– system 171   
BIPM 162   
Broadcast ephemeris 208,326   
BRTS 199   
Bulirsch sequence 149   
Bureau International   
– de l’Heure 162,183   
– des Poids et Mesures 162   
Butcher barriers 120   
C/A code 205   
Calendar 319   
– date from Modified Julian Date 322   
– Gregorian 321   
– Julian 319   
Carrier phase 206   
Celestial Ephemeris Pole 181   
Center for Space Research 63   
Centre National d’Études Spatiales 63   
CEP 181   
Cesium 161   
CGRO 198   
Chandler period 183   
Chebyshev   
– approximation of lunisolar position 75   
– Clenshaw algorithm 74   
– polynomial approximation 73   
Cholesky factorization 261,270   
CIO 171,183   
Clock   
– dither 207   
– error 206   
Clohessy–Wiltshire equations 295   
CNES 63,202   
Coarse Acquisition 205   
Code-ranging system 197   
Coefficients   
– of Adams–Bashforth method 134,136   
– of Adams–Moulton method 137   
– of geopotential 172,233,246   
Conic section 18   
Conical scan 194   
Consider   
– covariance 266   
– covariance analysis 297   
– parameters 265   
Conventional International Origin 171,18   
Convergence 48,242   
Coordinate system   
– equatorial 25   
– local tangent 36   
– orbital plane 27   
Coordinate time 163   
Coordinated Universal Time 158   
Coordinates   
– Cartesian 25   
– geodetic 186   
– polar 25   
– spherical 25   
Coriolis forces 294   
Corrector step 138,140   
Correlation 264   
Covariance 263   
– a priori 268   
– consider 266   
– matrix 264   
Cross-section area 77,83   
Cunningham algorithm 66,68   
Cycle slip 207   
Day   
– sidereal 157   
– solar 157   
DE 75   
Declination 25   
Degeneracy 296   
Dense output 127,131,151,153   
Density   
– atmospheric 54   
– comparison of models 98   
– exponential interpolation 89   
– Harris–Priester model 89,303   
– Helium polynomial coefficients 99   
– Jacchia models 91   
– Jacchia polynomial coefficients 96,97   
– scale height 86   
Development Ephemerides 75   
Dielectric constant 220   
Difference quotient 253   
Differential equation 117,129,141,240   
– of sensitivity matrix 241   
– of state transition matrix 240   
– second order 123,143,151,241   
Diffuse reflection 85   
Distance 45   
– Earth-Sun 79   
– geocentric 25   
– measurement 196   
– zenith 220   
Dither of GPS clocks 207

Divergence 287   
Divided differences 142   
Doodson variables 110   
Doppler   
– count 200,215   
– effect 199   
– measurement 200,215 – bias 217 – destructive 201 – one-way 202,216 – two-way 215   
– tracking 63,199   
DORIS tracking system 61,63,202   
Drag 83,243   
– atmospheric 54   
– coefficient 84,315   
– partials 248   
DRVID 227

– partials 251   
Ellipse 19,295   
Ellipsoid, oblate rotational 59   
EME2000 170,315   
Empirical accelerations 112   
Encryption 205   
Energy law 20   
ENVISAT 202   
Ephemeris   
– GPS satellite 324,326   
– planetary and lunar 158   
Ephemeris Time 158,160   
Equation   
– Clohessy-Wiltshire 295   
– Euler’s 182   
– Hill’s 295   
– Kepler’s 23,326   
– of light time 210,213   
– of motion 53,117,153,257   
– regularization 153   
– of relativistic motion 111   
– variational 241   
Equator 25,169   
Equatorial   
– coordinates 72   
– plane 25   
Equinoctial elements 30   
Equinox 25,27,170   
– true 181   
ERBS 198   
ERS 50,197,202   
ET 158,160   
Euler   
– equations 182   
– step 118   
EUVE 198   
Exospheric temperature 92   
Expected value 263   
Extrapolation methods 147   
– Bulirsch sequence 149   
– comparison 150   
– stepsize control 149   
Earth   
– asphericity 53   
– atmospheric drag 54   
– axis 25   
– center 25   
– density structure 53   
– emissivity 108   
– equator 25   
– flattening 189   
– gravity potential 56,57,163   
– main axes of inertia 61   
– mass 15   
– oblateness 35   
– plasma 219   
– plate motion 209   
– polar motion 183   
– radiation pressure 107   
– rotation 33,53,158   
– rotation rate 294   
– spin period 165   
– tides 108,209   
Earth Orientation Parameters 171   
Eccentric anomaly 22,29   
Eccentricity 18,29,42   
– of Earth orbit 157   
Echo-1 34   
Eclipse 80   
Ecliptic 169   
– coordinates 72   
– obliquity 71,176   
Eigenvalue 275   
Elastic reflection 85   
Electron density 227   
Elevation 38,194,212   
Faraday rotation 227   
Feed 194   
Fixed-point iteration 48,313   
FK5 catalog 170   
Flattening 60,189   
– dynamical 183   
Force   
– binormal 83   
– lift 83   
– radially symmetric 53   
– velocity-dependent 54   
Four-way ranging 215   
Free molecular flow 84   
Fundamental plane 80   
GAST 181   
Gauss C. F. 43,258   
Gauss–Jackson method 145,154   
Gaussian orbit determination 39   
Gaussian vectors 27,31   
General relativity 110,162   
Geocentric Coordinate Time 163   
GEODA 299,332   
Geodetic   
– coordinates 186,192   
– datums 185   
GEODYN 154,258   
Geoid 62   
Geomagnetic   
– activity 92   
– index 88   
– index prediction 102   
– storms 88   
Geopotential 56   
– coefficients 58,68,172,233,246   
– partials 244   
GEOS 62,63   
Geosat 63   
Geostationary   
– orbit 21   
– radius 294   
– satellite 29,154,294   
GFZ 202   
Givens rotations 272,289   
GLONASS 186   
GMST 165   
GMT 157   
Goddard Space Flight Center 63,199   
GPS 171,203,204,303,324   
–  process 207   
– almanac 324,325   
– broadcast ephemeris 324,326   
– clock dither 207   
– empirical forces 112   
– multipath 208,218   
– navigation data 205,303   
– position fix 207   
– signal frequencies 204   
– tracking of satellites 61   
– week 324   
GPS Time 158,162,324   
GPS/MET 303   
Gravimetry 61   
Gravitational constant 15   
Gravity   
– coefficients 57   
– gradient 243,244   
– JGM-3 coefficients 64   
– models 61   
– normalized coefficients 58   
– potential 56   
– recurrence relation 66   
Great circle 32   
Greenwich   
– Apparent Sidereal Time 181   
– Hour Angle 33,158,165   
– Mean Sidereal Time 158,165   
– Mean Time 157   
– meridian 33,186   
GRGS 202   
Ground track 32   
– shift 51   
GSFC 63   
GTDS 154,258   
Gyroscope 53,172,182   
Harmonic oscillation 295   
Helmert transformation 186   
Heterosphere 87   
Hill’s equations 295   
Hohmann transfer 47   
Homosphere 87   
Homotopy continuation method 257   
Horizontal plane 37   
Hour angle 33   
Householder transformation 270   
Humidity 222   
Hydrogen 161   
Hyperbola 19   
Hypersonic continuum flow 84   
IAU 163   
ICRS 170   
IEEE 154,155   
IERS 167   
– Bulletin A 184   
– Bulletin B 166,184   
– Bulletin C 168   
– Reference Pole 171,183   
IGN 202   
ILS 183   
Impulse, specific 105   
Inclination 25,28,42   
– of mean equator 174   
Increment function 118,133   
Information matrix 267,268,270   
International   
– Astronomical Union 163   
– Atomic Time 158,162   
– Celestial Reference System 170   
– Earth Rotation Service 167   
– Latitude Service 183   
– Terrestrial Reference System 171   
Internet 329   
Interpolant 129   
Interpolation   
– in multistep methods 140   
– Newton’s formula 134,142   
– polynomial 132,140   
Inverse   
– of covariance matrix 267   
– of symplectic matrix 239,243   
Ionosphere 225   
– path delay 198   
– refraction 226   
ITRS 171   
J2000 163   
Jacobian 260   
Jason 202   
JPL Ephemerides 75   
Julian Date 319   
Jupiter 54   
Kalman filter 258,276,303   
– continuous discrete 286   
– extended 282   
– factorization 283   
– linearized 281   
– process noise 284   
Kalman gain 278   
Kaula rule 58   
Kepler J. 15   
Kepler’s equation 23,32,48,326   
– iterative solution 23   
Kepler’s laws   
– first 18   
– second 17   
– third 23,174   
Kepler’s problem 16,130   
Knudsen number 84   
L1/2 frequency 204   
LAGEOS 54,63,202   
Landsat 198   
Laplace vector 17   
Laplacian orbit determination 39   
Laser 202   
– ranging 61,202   
Latitude   
– geocentric 186   
– geodetic 186   
– geograpical 32   
Law   
– energy 20   
– Kepler’s first 18   
– Kepler’s second 17   
– Kepler’s third 23,174   
– of areas 17   
– of gravity 15   
– vis-viva 20,47   
Leap seconds 169   
Least-squares estimation 258   
Legendre polynomials 56,66   
– addition theorem 57   
– associated polynomials 57,58   
Light time 208,234,313   
– equation 210,213,215   
Line of nodes 26,30   
Linearization 233,260   
Linux 332   
LLR 171   
Local tangential system 211   
Local truncation error 119,135,146   
Longitude   
– geocentric 186   
– geodetic 186   
– geograpical 33   
– mean 30   
Loss function 259   
– with a priori information 267   
Love number 109   
Lunar laser ranging 76,171   
Major tone 196   
Maneuver 47,104,105   
Mass   
– flow rate 105   
– point-like 53   
– relativistic effects 110   
Matrix   
– consider covariance 266   
– covariance 264   
– Earth rotation 181   
– elementary rotation 27   
– information 267,268   
– Jacobian 260   
– normal equations 261   
– nutation 180   
– orthonormal 269   
– polar motion 185   
– precession 176   
– sensitivity 233   
– state transition 233   
– symplectic 239   
– upper triangular 269   
– weighting 262   
Mean anomaly 23,43   
Mean longitude 30   
Mean motion 23,28   
Mean Sun 157   
Mean value 263   
Measurement   
– accuracy 196–199,201,202   
– model 257   
– update 282   
– vector 259   
Mercury 76   
Mesosphere 87   
Meteorological data 202   
Meteosat 215   
Metric 162   
Micro-step 148   
MicroLab-1 303   
Microwave signal 161   
Mid-point rule 147   
Mode coupler 194   
Modified Julian Date 33,319   
– from calendar date 321   
Molniya 35   
Moment of inertia 172,183   
Monopulse 194   
Moon   
– libration 76   
– low precision coordinates 70   
– mean torque 174   
– orbit perturbations due to the 53   
Multipath effects 208,218   
Multistep methods 132   
– comparison 146   
– Gauss–Jackson method 145   
– interpolation 140   
– second sum method 145   
– Stoermer–Cowell 143   
– variable order and stepsize 141   
NAG 131,143   
NASA 63   
National Bureau of Standards 161   
Navigation solution 207   
Newcomb S. 157,160   
Newton I. 16   
Newton’s law 15   
Newton’s method 24,48   
NIMA 63   
Non-singular elements 30   
Normal distribution 265   
Normal equations 260   
Normal points 203   
North pole 25,170   
Numerical integration 74,83,107,117,209,   
241,253,305   
– comparison of methods 151   
Nutation 76,170,171,178   
– angles 178   
– IAU 1980 theory 179   
– in longitude 181   
Oblateness 35   
Obliquity of the ecliptic 71   
Occulation 80   
Ocean tide 209   
One-way measurements 193,199   
Orbit   
– form 17   
– geostationary 21   
– geostationary transfer 34,48   
– Molniya 34   
– near-circular 29,154   
– near-equatorial 29   
– sun-synchronous 50   
Orbit determination   
– batch estimation 258   
– from three sets of angles 43   
– from two position vectors 40   
– preliminary 39,51,257   
– real-time 283,303   
– sequential estimation 258   
Orbital elements 28   
– classical 29   
– from position & velocity 28   
– from two positions 42   
– non-singular 30   
– osculating 49   
– transition matrix 235   
Orbital period 20,23   
Orbital plane 17,25,32   
Osculating elements 49   
P code 205   
Parabola 19   
Partial derivatives 30,233,260   
– difference quotient 253   
– of acceleration 244   
– of Keplerian elements 236   
– of measurements 250,252   
– w.r.t. Keplerian elements 238   
PECE method 138   
Penumbra 81   
PEPSOC 154,258   
Perigee 18,47   
– argument of 26   
Photon, impulse of 77   
Plane   
– ecliptic 169   
– equatorial 25,169   
– horizontal 37   
– orbital 17,25,32   
Plasma frequency 226   
Plate motion 209   
PN code 197,198   
Point-mass   
– acceleration 69   
– partials 247   
Poisson parentheses 238   
Polar motion 183,209   
Polarization of signal 217,219   
Pole   
– BIH 183   
– celestial 181   
– CIO 183   
– IERS reference 183   
– of the ecliptic 174   
– true celestial 178   
Polynomial interpolation 132   
Position fix 207   
Post-Newtonian approximation 163   
PPS 204   
PRARE tracking system 61,197   
Precession 71,170–172   
– free Eulerian 182   
– in longitude 176   
– lunisolar 174   
– planetary 176   
Precise GPS Code 205   
Precise Positioning Service 204   
Predictor–Corrector method 138   
Probability distribution 264   
Process noise 284,305   
Proper time 163   
Pseudorange 206,217   
PZ-90 186   
QR factorization 269,298   
Quadrant 25,28,29   
Quasar 171   
Radius vector 17   
Random variable 263   
Range measurement 193,196   
– 4-way 313   
– calibration 214   
Range rate measurement 193,201,216   
Recurrence relation   
– Adams–Bashforth coefficients 135   
– Adams–Moulton coefficients 137   
– divided differences 142   
– geopotential 246   
Recursive estimation 277   
Reflection 77   
– diffuse 85   
– elastic 85   
– specular 85   
Reflectivity 77,78   
Refraction 220   
Regular elements 30   
Regularization 153   
Relativity 162   
– effects of Sun 111   
– planetary motion 75   
– satellite motion 110   
Remote sensing 29,47,50   
Residuals 259,318   
Resonance 161   
Retro-reflector 43   
Retrograde 25   
Richardson extrapolation 147   
Right ascension 25   
– of ascending node 26,28,42   
– Sun 157   
RK4 method 119,154   
Rotation matrix 27   
RTOD 306,332   
Rubidium 161   
Runge–Kutta methods 118   
– continuous 127   
– embedded 121   
– explicit 120   
– performance 129   
– RK4 119,283,305   
– stepsize control 121   
Runge–Kutta–Nyström methods 123   
Runge–Lenz vector 17,30   
SA 207   
Satellite   
– area-to-mass ratio 85   
– attitude 106   
– box-wing shape 79   
– geodetic 54,154   
– geostationary 29,154,198,294   
– GPS 191   
– mass 77,84,105   
– propulsion systems 105   
– remote sensing 29,47,50   
– signal travel time 208   
– surface area 77   
– telecommunications 21   
– tracking 61,193   
– transponder 196,200,214   
Satellite laser ranging 10,61,171,202   
Satellite-satellite tracking 61,312   
Scale height 86   
Scaliger J. J. 319   
Schwarzschild radius 111   
Seasat 62,63   
Secant 118   
Second   
– Ephemeris 160   
– SI 158,162   
Second sum method 145   
Sector–triangle ratio 40   
Sectorial gravity coefficients 58   
Selective Availability 207,303   
Semi-latus rectum 18,28,42   
Semi-major axis 18,28   
– variance 299   
Sensitivity matrix 233   
– differential equation 241   
Sequential estimation 280   
Shadow   
– cone angle 81   
– conical model 80   
– transits 83   
– vertex 81   
Shuttle 198   
SI second 158,162   
Sidereal Time 33,165,171   
– apparent 181   
Signal travel time 208   
Singular value decomposition 274   
Singularity 29,276   
SLR 10,61,171,202   
Solar   
– cycle 103   
– flux 77,103   
– flux prediction 102   
– radiation pressure 54,77   
– radiation pressure coefficient 78,31   
Solid Earth tide 209   
Space shuttle 198   
Space-Time 162   
Specific impulse 105   
Specular reflection 85   
Speed of light 165   
Spherical harmonics 56   
Spheroid 53   
SPOT 63,202   
SPS 204   
Sputnik 62,98   
SST 61   
Stability 287   
– of atomic clocks 162   
– of Earth rotation 162   
– of multistep methods 139   
Standard deviation 263   
Standard Positioning Service 204   
State transition matrix 233   
– differential equation 240   
– for orbital elements 235   
– inverse 239,243   
– linearized orbit model 295   
– two-body problem 239   
State vector 118,233,240   
Statistics 263   
Stella 63   
Stepsize control 121,131,149,155   
Stern–Gerlach magnet 161   
Stoermer–Cowell methods 143   
Stratosphere 87   
Sun   
– dynamo model 104   
– fraction of light 83   
– low precision coordinates 70   
– mean 157   
– orbit perturbations due to 53   
– radio flux 88   
– relativistic effects 111   
– rotation period 88   
– spot cycle 88   
– torque 174   
Sunspot numbers 103   
Symplectic matrix 239,243   
Système International 158   
TAI 158,162   
Taylor expansion 118   
TCB 164   
TCG 163,171   
TDB 164   
TDRSOD 313,332   
TDRSS 63,198,312   
TDT 163   
TEC 198   
Telecommand 197   
Temperature, exospheric 54,92   
Terrestrial Dynamical Time 163   
Terrestrial Time 158,163   
Tesseral gravity coefficients 58   
Third-body forces 108   
Three-way Doppler 200   
Thrust 105   
– force 104   
– partials 249   
– performance 105   
Thruster activity 104   
Tidal   
– force 70   
– friction 167   
– station displacement 209   
Tide 209   
Time 157   
– coordinate 163   
– ΔT 167   
– proper 163   
Time update 281   
Tone-ranging system 196   
TOPEX/POSEIDON 61,107,112,198,199,202   
Topocentric 37   
Total electron content 226   
Tracking unit 194   
Transfer ellipse 47   
TRANSIT 186   
Transponder 43,196,200,214,234,312   
Tropical year 160   
Troposphere 87,221   
– refraction 222   
True anomaly 18,29,43   
TT 158,163   
Two-body problem 16,129   
– state transition matrix 239   
Two-way measurements 193   
USNO 162   
UT 157   
UT1 167   
UTC 158,168   
UTOPIA 154,258   
Vanguard 62   
Variance 263   
Variational equations 241   
Velocity   
– areal 17,28   
– at apogee 47   
– at perigee 47   
– transformation 191   
– two-body problem 24   
Velocity increment 105   
Venus 54,76   
Vernal equinox 25,170   
Very Long Baseline Interferometry 171   
Vis-viva law 20,47   
VLBI 171   
Water vapor pressure 221   
Weighting 262   
WGS84 185,304,324   
White Sands 199   
Wind model 85   
Windows 331   
World Geodetic System 185   
UARS 315   
Ultrastable oscillator 202   
Umbra 81   
United States Naval Observatory 162   
Universal Time 157   
– UT1 158,167   
– UT1R 167   
– UTC 158,168   
X-angle 213   
– partials 252   
Y code 205   
Y-angle 213   
– partials 252   
Zenith distance 220   
Zonal gravity coefficients 58   
Zone of exclusion 198

# Astrodynamical Constants

<table><tr><td> Quantity</td><td> Value</td><td>References and Remarks</td></tr><tr><td>Time</td><td></td><td></td></tr><tr><td>MJD(J2000)</td><td> 51 544.5</td><td>IAU 1976 (Seidelmann 1992)</td></tr><tr><td> TT-TAI</td><td>32.184 s</td><td> IAU 1991 (Seidelmann 1992)</td></tr><tr><td> GPS-TAI</td><td> -19 s</td><td>Hofmann-Wellenhof et al.(1997)</td></tr><tr><td>Universal c G</td><td>299 792 458 m/s 6.673:10-20 km³ /(kg s2)</td><td>IAU 1976 (Seidelmann 1992) Cohen &amp; Taylor 1987</td></tr><tr><td>Earth GM h R④ f</td><td>398 600.4415 km3/s2 0.00108263 6378.137 km 1/298.257223563</td><td>JGM-3 JGM-3 WGS-84 (NIMA 1997) WGS-84 (NIMA 1997)</td></tr><tr><td>田 Sun GM④</td><td>0.7292115:10-4 rad/s 1.32712440018:1011 km3/s2 149 597 870.691 km</td><td>Moritz 1980 DE405 (Standish 1998)</td></tr><tr><td>AU Ro P</td><td>6.96.105 km 4.560·10-6 N/m2</td><td>DE405 (Standish 1998) Seidelmann 1992 IERS 1996 (McCarthy 1996)</td></tr><tr><td>Moon</td><td></td><td></td></tr><tr><td> GMm</td><td> 4 902.801 km/s2</td><td>DE405 (Standish 1998)</td></tr><tr><td></td><td> 384 400 km</td><td> Seidelmann 1992</td></tr><tr><td>am</td><td></td><td></td></tr><tr><td></td><td>1738 km</td><td></td></tr><tr><td>RM</td><td></td><td> Seidelmann 1992</td></tr><tr><td></td><td></td><td></td></tr><tr><td> Satellites</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td> 42 164 km</td><td> 23h56m04s orbital period</td></tr><tr><td>rGEo</td><td></td><td></td></tr><tr><td>VGEO</td><td> 3.075 km/s</td><td></td></tr><tr><td></td><td>26 561 km</td><td>11h58m02s orbital period</td></tr><tr><td>rgpS</td><td></td><td></td></tr><tr><td></td><td> 3.874 km/s</td><td></td></tr><tr><td>VGPS</td><td></td><td></td></tr><tr><td></td><td> 6678 ...7878 km</td><td> 300 ... 1500 km altitude</td></tr><tr><td> rLEo</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>VLEO</td><td>7.726 ... 7.113 km/s</td><td></td></tr></table>

Underlined numbers indicate a rounding of the original value to the given number of digits.   
DE405 constants refer to the TDB time system.
