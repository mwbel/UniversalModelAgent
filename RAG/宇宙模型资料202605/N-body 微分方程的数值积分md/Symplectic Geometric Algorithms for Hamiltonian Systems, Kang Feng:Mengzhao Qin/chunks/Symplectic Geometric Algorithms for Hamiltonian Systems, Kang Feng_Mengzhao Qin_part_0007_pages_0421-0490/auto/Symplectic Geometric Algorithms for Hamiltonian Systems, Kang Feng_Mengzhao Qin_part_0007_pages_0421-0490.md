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

![](images/fc8757327f0857590fa6f098fc4ea8254ddb5b42b162bdae993a2b185437a7e3.jpg)  
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

# Chapter 9. Formal Power Series and B-Series

We study vector fields, their associated dynamical systems and phase flows together with their algorithmic approximations in $\mathbf { R } ^ { N }$ from the formal power series approach [Fen93a,Fen92] .

# 9.1 Notation

Our considerations will be local in both space and time, all related objects are $\mathbf { C } ^ { \infty }$ smooth. We use coordinate description and matrix notation, the coordinate vectors in $\mathbf { R } ^ { N }$ and vector functions $a : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ are denoted by column matrices. The identity vector function $1 _ { N }$ is given by $1 _ { N } ( x ) \ = \ x$ . For vector function $a = ( a _ { 1 } , \cdots , a _ { N } ) ^ { \mathrm { T } } : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ ,

$$
a \mathrm { * } : = \left( { \frac { \partial a _ { i } } { \partial x _ { j } } } \right) = \mathrm { J a c o b i a n \ m a t r i x } \ a ,
$$

the association $a \to a ^ { * }$ is linear, $a ^ { * }$ operates on scalar functions $\phi : \mathbf { R } ^ { N } \to \mathbf { R }$

$$
a ^ { * } \phi = \sum a _ { i } \frac { \partial \phi } { \partial x _ { i } } ,
$$

and on vector functions $b : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ as

$$
a ^ { * } b = a ^ { * } ( b _ { 1 } , \cdot \cdot \cdot , b _ { N } ) ^ { \mathrm { T } } = ( a ^ { * } b _ { 1 } , \cdot \cdot \cdot , a ^ { * } b _ { N } ) ^ { \mathrm { T } } = b _ { * } a , \quad a ^ { * } 1 _ { N } = a .
$$

Multiple applications of linear differential operators are naturally defined, such as $a ^ { * } b ^ { * }$ , $( a ^ { * } b ^ { * } ) c ^ { * }$ , $a ^ { * } ( b ^ { * } c ^ { * } )$ , etc. The operations are multilinear, associative but noncommutative; thus, powers can be defined as

$$
a ^ { * k } = a ^ { * } a ^ { * } \cdot \cdot \cdot a ^ { * } ( k { \mathrm { t i m e } } ) , \quad a ^ { k } : = a ^ { * k } 1 _ { N } ,
$$

the identity operator $I$ operates on scalar and vector functions $\phi$ and $b$ as $I \phi = \phi$ , $I b = b$ .

We identify all vector functions $a : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ as vector fields. All vector fields in $\mathbf { R } ^ { N }$ form a ( $\infty$ -dimensional) real Lie bracket under Lie bracket

$$
[ a , b ] : = a _ { * } b - b _ { * } a = b ^ { * } a - a ^ { * } b = ( b ^ { * } a ^ { * } - a ^ { * } b ^ { * } ) 1 _ { N } .
$$

The Lie algebra ${ \bf V } ^ { N }$ is associated with the ( $\infty$ -dimensional) local Lie group $\mathbf { D } ^ { N }$ of near-identity diffeomorphisms—or simply near-1 maps—of $\mathbf { R } ^ { N }$ .

Consider the dynamical system in $\mathbf { R } ^ { N }$

$$
\frac { \mathrm { d } \boldsymbol { x } } { \mathrm { d } t } = \boldsymbol { a } ( \boldsymbol { x } ) ,
$$

defined by a vector field $a$ . It possesses a phase flow $e _ { a } ^ { t } = e ^ { t }$ , which is a one-parameter (in $t$ ) group of near-1 maps of $\mathbf { R } ^ { N }$ ,

$$
e ^ { 0 } = 1 _ { N } , \quad e ^ { t + s } = e ^ { t } \circ e ^ { s } ,
$$

and generates the solution by $x ( 0 )  e _ { a } ^ { t } x ( 0 ) = x ( t )$ . The phase flow is expressible as a convergent power series in $t$ :

$$
\begin{array} { l } { { \displaystyle e _ { a } ^ { t } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } t ^ { k } e _ { k } , } } \\ { { \displaystyle e _ { 0 } = 1 _ { N } , \quad e _ { k } = \frac { 1 } { k } a ^ { * } e _ { k - 1 } = \frac { 1 } { k ! } ( a ^ { * } ) ^ { k } 1 _ { N } = \frac { 1 } { k ! } a ^ { k } . } } \end{array}
$$

We define

$$
\displaystyle \mathtt { E x p } t a ^ { * } : = I + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } ( t a ) ^ { * k } , \quad I \mathrm { \ i s \ t h e \ i d e n t i t y \ o p e r a t o r { . } }
$$

This is an operator power series operating on scalar and vector functions, and defined by

$$
\exp t a : = ( \mathrm { E x p } t a ^ { * } ) 1 _ { N } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } ( t a ^ { * } ) ^ { k } 1 _ { N } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } \frac { t ^ { k } } { k ! } a ^ { k } ,
$$

then

$$
e _ { a } ^ { t } = (  { \mathrm { E x p } } t a ^ { * } ) 1 _ { N } = \exp t a ,
$$

for scalar function

$$
\phi \circ e _ { a } ^ { t } = \phi \circ \exp { t a } = ( \exp { t a ^ { * } } ) \phi ,
$$

for vector function

$$
b \circ e _ { a } ^ { t } = b \circ \exp { t a } = ( \mathrm { E x p } t a ^ { * } ) b = ( \mathrm { E x p } t a ^ { * } ) b ^ { * } 1 _ { N } .
$$

Each numerical algorithm solving the system (1.1) possesses the step transition map $f _ { a } ^ { s }$ which is one-parameter (in step-size $s$ ) family (in general not a one-parameter group in $s$ ) of near-1 maps on $\mathbf { R } ^ { N }$ , expressible as a convergent power series in $s$

$$
f _ { a } ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } ,
$$

the coefficients can be determined recursively form the defining difference equation. The transition generates the numerical solution $x ( 0 ) ~ \longrightarrow ~ ( f _ { a } ^ { s } ) ^ { N } x ( 0 ) \approx x ( N s )$ by iterations with step-size $s$ chosen fixed in general.

The main problem is to construct and analyze the algorithmic approximations $\left. f _ { a } ^ { s } \approx e _ { a } ^ { t } \right| _ { t = s } = e _ { a } ^ { s }$ in a proper way. For this purpose, we propose a unified framework based on the apparatus of formal power series, Lie algebra of vector fields, and the corresponding Lie group of diffeomorphisms [Lie88,Olv93] .

# 9.2 Near-0 and Near-1 Formal Power Series

Among the formal power series $\sum _ { 0 } ^ { \infty } s ^ { k } a _ { k } , a _ { k } : \mathbf { R } ^ { N }  \mathbf { R } ^ { N }$ , we pick out two special classes. The first class consists of those with $a _ { 0 } ~ = ~ 0$ , called near-0 formal vector fields and the second class consists of those with $a _ { 0 } = 1 _ { N }$ , called near-1 formal maps (diffeomorphisms).

All near-0 formal vector fields $a ^ { s } = \sum _ { 1 } ^ { \infty } s ^ { k } a _ { k }$ form a ( $\infty$ -dim.) real Lie algebra $\mathbf { F V } ^ { N }$ under the Lie bracket

$$
[ a ^ { s } , b ^ { s } ] = \left[ \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } , \sum _ { k = 1 } ^ { \infty } s ^ { k } b _ { k } \right] : = \sum _ { k = 2 } ^ { \infty } s ^ { k } \sum _ { i + j = k } [ a _ { i } , b _ { j } ] .
$$

The associated near-0 formal differential operators and their products are

$$
\begin{array} { l } { ( a ^ { s } ) _ { * } : = \displaystyle \left( \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \right) _ { * } : = \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k * } , } \\ { \displaystyle a ^ { s * } : = \left( \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \right) ^ { * } : = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } ^ { * } , } \\ { \displaystyle a ^ { s * } b ^ { s * } : = \sum _ { k = 2 } ^ { \infty } s ^ { k } \sum _ { i + j = k } ^ { \infty } a _ { i } ^ { * } b _ { j } ^ { * } , \quad ( a ^ { s * } ) ^ { 2 } : = a ^ { s * } a ^ { s * } , \mathrm { e t c . } } \end{array}
$$

For any vector function $a = ( a _ { 1 } , \cdots , a _ { N } ) ^ { \mathrm { T } } : \mathbf { R } ^ { N } \to \mathbf { R } ^ { N }$ and any near-1 formal map $g ^ { s } = 1 + \sum _ { k = 1 } ^ { \infty } s ^ { k } g _ { k }$ , we define the composition,

$$
\begin{array} { l } { { ( a \circ g ^ { s } ) ( x ) = a ( g ^ { s } ( x ) ) = a ( x ) + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } ( a \circ g ) _ { k } ( x ) , } } \\ { { ( a \circ g ) _ { k } = \displaystyle \sum _ { m = 1 } ^ { k } \displaystyle \sum _ { k _ { 1 } + \cdots + k _ { m } = k } \frac { 1 } { m ! } ( D ^ { m } a ) ( g _ { k _ { 1 } } , \cdot \cdot \cdot , g _ { k _ { m } } ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle D ^ { m } a = ( D ^ { m } a _ { 1 } , \cdots , D ^ { m } a _ { N } ) ^ { \mathrm { T } } , } } \\ { { \displaystyle D ^ { m } a _ { i } ( v _ { 1 } , \cdots , v _ { m } ) = \sum _ { j _ { 1 } , \cdots , j _ { m } = 1 } ^ { N } \frac { \partial ^ { m } a _ { i } } { \partial x _ { j _ { 1 } } \cdots \partial x _ { j _ { m } } } v _ { 1 j _ { 1 } } \cdots v _ { m j _ { m } } , } } \end{array}
$$

is the usual $m$ -th differential multi-linear form for $m$ tangent vectors $v _ { i } = ( v _ { i _ { 1 } } , \cdots ,$ $v _ { i _ { N } } ) ^ { \mathrm { T } } ( i \ = \ 1 , \cdot \cdot \cdot , m )$ at point $\boldsymbol { x } \in \mathbf { R } ^ { N }$ , which is invariant under permutation of Nvectors. Using the identities,

$$
\begin{array} { l } { { ( D ^ { 1 } a ) ( b ) = b ^ { * } a , } } \\ { { ( D ^ { 2 } a ) ( b , c ) = ( c ^ { * } b ^ { * } - ( c ^ { * } b ) ^ { * } ) a , } } \\ { { ( D ^ { 3 } a ) ( b , b , b ) = ( b ^ { * 3 } + 2 b ^ { 3 * } - 3 b ^ { * } b ^ { 2 * } ) a . } } \end{array}
$$

We get in particular

$$
\begin{array} { l } { ( a \circ g ) _ { 1 } = g _ { 1 } ^ { \ast } a , } \\ { ( a \circ g ) _ { 2 } = g _ { 2 } ^ { \ast } a + \cfrac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) a , } \\ { ( a \circ g ) _ { 3 } = g _ { 3 } ^ { \ast } a + ( ( g _ { 2 } ^ { \ast } g _ { 1 } ^ { \ast } - ( g _ { 2 } ^ { \ast } g _ { 1 } ) ^ { \ast } ) a + \cfrac 1 { 3 ! } ( g _ { 1 } ^ { \ast 3 } + 2 g _ { 1 } ^ { 3 \ast } - 3 g _ { 1 } ^ { \ast } g _ { 1 } ^ { 2 \ast } ) a . } \end{array}
$$

For any two near-1 formal maps

$$
f ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } , \quad g ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } g _ { k } ,
$$

the composition $f ^ { s } \circ g ^ { s }$ is defined in a term by term way:

$$
\begin{array} { l } { \displaystyle \big ( f ^ { s } \circ g ^ { s } \big ) ( x ) = f ^ { s } ( g ^ { s } ( x ) ) = 1 _ { N } ( g ^ { s } ( x ) ) + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } ( g ^ { s } ( x ) ) } \\ { \displaystyle = : 1 _ { N } ( x ) + \sum _ { k = 1 } ^ { \infty } s ^ { k } ( f \circ g ) _ { k } ( x ) , } \\ { \displaystyle ( f \circ g ) _ { 1 } = f _ { 1 } + g _ { 1 } , } \\ { \displaystyle ( f \circ g ) _ { k } = f _ { k } + g _ { k } + \delta ( f _ { 1 } , \cdots , f _ { k - 1 } ; g _ { 1 } , \cdots , g _ { k - 1 } ) , \quad k \geq 2 , } \\ { \displaystyle \delta ( f _ { 1 } , \cdots , f _ { k - 1 } ; g _ { 1 } , \cdots , g _ { k - 1 } ) = \displaystyle \sum _ { i = 1 } ^ { k - 1 } \sum _ { m = 1 } ^ { i } \sum _ { i _ { 1 } + \cdots + i _ { m = i } } \frac { 1 } { m ! } ( D ^ { m } f _ { k - i } ) ( g _ { i _ { 1 } } , \cdots , g _ { i _ { m } } ) . } \end{array}
$$

In particular we get,

$$
\begin{array} { l } { { ( f \circ g ) _ { 2 } = f _ { 2 } + g _ { 2 } + g _ { 1 } ^ { \ast } f _ { 1 } , } } \\ { { \ } } \\ { { ( f \circ g ) _ { 3 } = f _ { 3 } + g _ { 3 } + g _ { 1 } ^ { \ast } f _ { 2 } + g _ { 2 } ^ { \ast } f _ { 1 } + \displaystyle \frac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) f _ { 1 } , } } \\ { { \ } } \\ { { ( f \circ g ) _ { 4 } = f _ { 4 } + g _ { 4 } + g _ { 1 } ^ { \ast } f _ { 3 } + g _ { 2 } ^ { \ast } f _ { 2 } + g _ { 3 } ^ { \ast } f _ { 1 } + \displaystyle \frac 1 2 ( g _ { 1 } ^ { \ast 2 } - g _ { 1 } ^ { 2 \ast } ) f _ { 2 } \ ~ } } \\ { { \ } } \\ { { \ \qquad + ( g _ { 2 } ^ { \ast } g _ { 1 } ^ { \ast } - ( g _ { 2 } ^ { \ast } g _ { 1 } ) ^ { \ast } ) f _ { 1 } + \displaystyle \frac 1 { 3 ! } ( g _ { 1 } ^ { \ast 3 } + 2 g _ { 1 } ^ { 3 \ast } - 3 g _ { 1 } ^ { \ast } g _ { 1 } ^ { 2 \ast } ) f _ { 1 } . } } \end{array}
$$

Under this composition rule, all near-1 formal maps

$$
f ^ { s } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k }
$$

form a $\scriptstyle ( \infty \mathrm { - d i m } )$ ) formal Lie group $\mathbf { F } \mathbf { D } ^ { N }$ . In group $\mathbf { F } \mathbf { D } ^ { N }$ , inverse elements, square roots, rational powers, etc., always exist, and their coefficients can always be determined recursively by the defining composition relations. For example, the inverse $( f ^ { s } ) ^ { - 1 } : = 1 + \sum _ { k = 1 } ^ { \infty } { s ^ { k } h _ { k } } = h ^ { s }$ is defined by $( f ^ { s } \circ h ^ { s } ) = 1 _ { N }$ , hence

$$
f _ { 1 } + h _ { 1 } = 0 , \quad f _ { k } + h _ { k } + \delta ( f _ { 1 } , \cdot \cdot , f _ { k - 1 } ; h _ { 1 } , \cdot \cdot , h _ { k - 1 } ) = 0 , \quad k \geq 2 .
$$

In particular,

$$
\begin{array} { l } { { h _ { 1 } = - f _ { 1 } , \quad h _ { 2 } = - f _ { 2 } + f _ { 1 } ^ { 2 } , } } \\ { { { } } } \\ { { h _ { 3 } = - f _ { 3 } + f _ { 1 } ^ { * } f _ { 2 } + \big ( f _ { 2 } ^ { * } - f _ { 1 } ^ { 2 * } \big ) f _ { 1 } - { \textstyle \frac 1 2 } f _ { 1 } ^ { 3 } + { \textstyle \frac 1 2 } f _ { 1 } ^ { 2 * } f _ { 1 } . } } \end{array}
$$

There is an obvious one-one correspondence between the Lie algebra $\mathbf { F V } ^ { N }$ and the Lie group $\mathbf { F } \mathbf { D } ^ { N }$ , established simply by $+ 1 _ { N }$ and $- 1 _ { N }$ . However, the more significant one-one correspondence between them is given by exp and its inverse log.

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \exp : { \bf { F } } { \bf { V } } ^ { N }  { \bf { F } } { \bf { D } } ^ { N } , } } \\ { { } } & { { } } & { { \displaystyle a ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k } \Longrightarrow ~ \exp a ^ { s } ~ = : 1 _ { N } + \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ! } ( a ^ { s * } ) ^ { m } 1 _ { N } } } \\ { { } } & { { } } & { { \displaystyle = : 1 _ { N } + \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } = f ^ { s } . } } \end{array}
$$

Note that

$$
( a ^ { s * } ) ^ { m } = \left( \sum _ { k _ { 1 } = 1 } ^ { \infty } { s ^ { k _ { 1 } } a _ { k _ { 1 } } ^ { * } } \right) \cdot \cdot \cdot \left( \sum _ { k _ { m } = 1 } ^ { \infty } { s ^ { k _ { m } } a _ { k _ { m } } ^ { * } } \right) = \sum _ { k _ { 1 } , \cdots , k _ { m } = 1 } ^ { \infty } { s ^ { k _ { 1 } + \cdots + k _ { m } } a _ { k _ { 1 } } ^ { * } } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } ,
$$

so we get easily

$$
\begin{array} { l l } { f _ { k } = \displaystyle \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } , } & { k \geq 1 , f _ { 1 } = a _ { 1 } , } \\ { f _ { k } = a _ { k } + \displaystyle \sum _ { m = 2 } ^ { k } \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } , k \geq 2 , f _ { 2 } = a _ { 2 } + \displaystyle \frac { 1 } { 2 } a _ { 1 } ^ { 2 } . } \end{array}
$$

Note that (2.2) provides a 2-way recursion formula from $a _ { 1 } , \cdots , a _ { k }$ to $f _ { 1 } , \cdots , f _ { k }$ and vice versa. Therefore, exp maps $\mathbf { F V } ^ { N }$ one-one onto $\mathbf { F } \mathbf { D } ^ { N }$ and its inverse, i.e., log is defined by the same (2.2):

$$
\begin{array} { r l } & { \log = ( \exp ) ^ { - 1 } : { \mathbf { F } } { \mathbf { D } } ^ { N } \longrightarrow { \mathbf { F } } { \mathbf { V } } ^ { N } , } \\ & { \log \exp \ a ^ { s } = a ^ { s } , \quad \exp \log \ f ^ { s } = f ^ { s } . } \end{array}
$$

In particular,

$$
\begin{array} { l } { { a _ { 1 } = f _ { 1 } , \quad a _ { 2 } = f _ { 2 } - \displaystyle \frac { 1 } { 2 } a _ { 1 } ^ { 2 } , \quad a _ { 3 } = f _ { 3 } - \displaystyle \frac { 1 } { 2 } ( a _ { 1 } ^ { * } a _ { 2 } + a _ { 2 } ^ { * } a _ { 1 } ) - \displaystyle \frac { 1 } { 3 ! } a _ { 1 } ^ { 3 } , } } \\ { { \displaystyle a _ { 4 } = f _ { 4 } - \displaystyle \frac { 1 } { 2 } \big ( a _ { 1 } ^ { * } a _ { 3 } + a _ { 2 } ^ { 2 } + a _ { 3 } ^ { * } a _ { 1 } \big ) - \displaystyle \frac { 1 } { 3 ! } \big ( a _ { 1 } ^ { * } a _ { 1 } ^ { * } a _ { 2 } + a _ { 1 } ^ { * } a _ { 2 } ^ { * } a _ { 1 } + a _ { 2 } ^ { * } a _ { 1 } ^ { * } a _ { 1 } \big ) - \displaystyle \frac { 1 } { 4 ! } a _ { 1 } ^ { 4 } , } } \\ { { \displaystyle a _ { k } = f _ { k } - \displaystyle \sum _ { m = 2 } ^ { k - 1 } \displaystyle \frac { 1 } { m ! } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } a _ { k _ { 1 } } ^ { * } \cdot \cdot \cdot a _ { k _ { m } } ^ { * } \mathbf { 1 } _ { N } - \displaystyle \frac { 1 } { k ! } a _ { 1 } ^ { k } , \quad k \ge 3 . } } \end{array}
$$

An equivalent construction of $\log f ^ { s } = a ^ { s }$ is

$$
\log f ^ { s } = \sum _ { m = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { m - 1 } } { m } } h _ { m } ^ { s } ,
$$

where

$$
\begin{array} { r } { h _ { 1 } ^ { s } = f ^ { s } - 1 _ { N } , \quad h _ { m } ^ { s } = h _ { m - 1 } ^ { s } \circ f ^ { s } - h _ { m - 1 } ^ { s } . } \end{array}
$$

It is easy to compute

$$
\begin{array} { l } { { \displaystyle h _ { 1 } ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } = \sum _ { k _ { 1 } = 1 } ^ { \infty } s ^ { k _ { 1 } } ( 1 _ { N } \circ f ) _ { k _ { 1 } } } , } \\ { { } } \\ { { \displaystyle h _ { 2 } ^ { s } = \sum _ { k _ { 1 } , k _ { 2 } = 1 } ^ { \infty } s ^ { k _ { 1 } + k _ { 2 } } ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } , } } \\ { { } } \\ { { \displaystyle h _ { 3 } ^ { s } = \sum _ { k _ { 1 } , k _ { 2 } , k _ { 3 } = 1 } ^ { \infty } s ^ { k _ { 1 } + k _ { 2 } + k _ { 3 } } ( ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } \circ f ) _ { k _ { 3 } } , } } \\ { { } } \\ { { \displaystyle . . . . } } \end{array}
$$

Substituting in (2.3) and equating with $\sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k }$ , we get

$$
a _ { k } = \sum _ { m = 1 } ^ { k } { \frac { ( - 1 ) ^ { m - 1 } } { m } } \sum _ { k _ { 1 } + \cdots + k _ { m } = k } ( \cdots ( ( 1 _ { N } \circ f ) _ { k _ { 1 } } \circ f ) _ { k _ { 2 } } \cdots \circ f ) _ { k _ { m } } .
$$

It is easy to verify $\log \exp a ^ { s } = a ^ { s }$ for this log, so this is precisely the inverse of exp, thus agreeing with the previous one.

We use the above construction (2.4) to establish the formal Baker–Campbell– Hausdorff formula[Bak05,Hau06] . For arbitrary near-1 formal maps $f ^ { s } , g ^ { s }$ ,

$$
\log { \big ( } f ^ { s } \circ g ^ { s } { \big ) } = \log ~ f ^ { s } + \log ~ g ^ { s } + \sum _ { k = 1 } ^ { \infty } d _ { k } ( \log ~ f ^ { s } , \log ~ g ^ { s } ) ,
$$

where log $f ^ { s } = a ^ { s }$ , log $g ^ { s } = b ^ { s }$ , then[Dyn46]

$$
d _ { k } ( a ^ { s } , b ^ { s } ) = \frac { 1 } { k } \sum _ { m = 1 } ^ { k } \frac { ( - 1 ) ^ { m - 1 } } { m } \sum _ { { \bf \Phi } _ { p _ { 1 } + q _ { 1 } + \ldots + p _ { m } + q _ { m } = k } \atop { \bf \Phi } _ { p _ { i } + q _ { i } \geq 1 , p _ { i } \geq 0 , q _ { i } \geq 0 } } \frac { [ ( a ^ { s } ) ^ { p _ { 1 } } ( b ^ { s } ) ^ { q _ { 1 } } \cdot \cdot \cdot ( a ^ { s } ) ^ { p _ { m } } ( b ^ { s } ) ^ { q _ { m } } ] } { p _ { 1 } ! q _ { 1 } ! \cdot \cdot \cdot p _ { m } ! q _ { m } ! } ,
$$

where

$$
( x ) ^ { p } = x x \cdot \cdot \cdot x ( p { \mathrm { ~ t i m e s } } ) , \quad [ x _ { 1 } x _ { 2 } x _ { 3 } \cdot \cdot \cdot x _ { n } ] = [ [ \cdot \cdot [ [ x _ { 1 } , x _ { 2 } ] , x _ { 3 } ] , \cdot \cdot \cdot ] , x _ { n } ] .
$$

In particular,

$$
d _ { 1 } = { \frac { 1 } { 2 } } [ a ^ { s } , b ^ { s } ] , \quad d _ { 2 } = { \frac { 1 } { 1 2 } } { \big ( } [ a ^ { s } b ^ { s } b ^ { s } ] + [ b ^ { s } a ^ { s } a ^ { s } ] { \big ) } , \quad d _ { 3 } = - { \frac { 1 } { 2 4 } } [ a ^ { s } b ^ { s } b ^ { s } a ^ { s } ] .
$$

Let $\log { ( f ^ { s } \circ g ^ { s } ) } = c ^ { s } = \sum _ { k = 1 } ^ { \infty } { s ^ { k } c _ { k } }$ , then

$$
\begin{array} { l } { { c _ { 1 } = a _ { 1 } + b _ { 1 } , \quad c _ { 2 } = a _ { 2 } + b _ { 2 } + \displaystyle \frac { 1 } { 2 } [ a _ { 1 } b _ { 1 } ] , } } \\ { { \ } } \\ { { c _ { 3 } = a _ { 3 } + b _ { 3 } + \displaystyle \frac { 1 } { 2 } ( [ a _ { 1 } b _ { 2 } ] + [ a _ { 2 } b _ { 1 } ] ) + \displaystyle \frac { 1 } { 1 2 } ( [ a _ { 1 } b _ { 1 } b _ { 1 } ] + [ b _ { 1 } a _ { 1 } a _ { 1 } ] ) , } } \\ { { \ } } \\ { { c _ { 4 } = a _ { 4 } + b _ { 4 } + \displaystyle \frac { 1 } { 1 2 } ( [ a _ { 1 } b _ { 3 } ] + [ a _ { 2 } b _ { 2 } ] + [ a _ { 3 } b _ { 1 } ] ) } } \\ { { \ } } \\ { { \displaystyle \qquad + \displaystyle \frac { 1 } { 1 2 } \big ( [ a _ { 1 } b _ { 1 } b _ { 2 } ] + [ a _ { 1 } b _ { 2 } b _ { 1 } ] + [ a _ { 2 } b _ { 1 } b _ { 1 } ] + [ b _ { 1 } a _ { 1 } a _ { 2 } ] + [ b _ { 1 } a _ { 2 } a _ { 1 } ] + [ b _ { 2 } a _ { 1 } a _ { 1 } ] \big ) } } \\ { { \ } } \\ { { \displaystyle - \displaystyle \frac { 1 } { 2 4 } [ a _ { 1 } b _ { 1 } b _ { 1 } a _ { 1 } ] , \quad \mathrm { e t c . } } } \end{array}
$$

Note that the classical BCH formula is restricted to the composition of two oneparameter groups, where log $f ^ { s } = s a _ { 1 }$ and $\log { g ^ { s } } = s b _ { 1 }$ .

The log transform reduces matters at the Lie group level to those at the easier level of Lie algebra. All properties of near-1 formal maps have their logarithmic interpretations.

Proposition 2.1. [Fen93a,Fen92,Fen93b] We list some of them, let $\log f ^ { s } = a ^ { s } = \sum _ { k = 1 } ^ { \infty } s ^ { k } a _ { k }$ :

$1 ^ { \circ }$ $f ^ { s }$ is a phase flow, i.e., $f ^ { s + t } = f ^ { s } \circ f ^ { t } \Leftrightarrow \log f ^ { s } = s a _ { 1 }$ .   
$2 ^ { \circ }$ $f ^ { s }$ is revertible, i.e., $f ^ { s } \circ f ^ { - s } = 1 _ { N } \Leftrightarrow \log f ^ { s }$ is odd in $s$ .   
$3 ^ { \circ }$ $f ^ { s }$ raised to real $\mu$ -th power $( f ^ { s } ) ^ { \mu } \Leftrightarrow \log ( f ^ { s } ) ^ { \mu } = \mu \log f ^ { s } $ . In particular, $\log { ( f ^ { s } ) ^ { - 1 } } = - \log { f ^ { s } } , \log { \sqrt { f ^ { s } } } = { \frac { 1 } { 2 } } \log { f ^ { s } } .$ .   
$4 ^ { \circ }$ $f ^ { s }$ scaled to $f ^ { \alpha s } \Leftrightarrow \log { ( f ^ { \alpha s } ) } = ( \bar { \log { f } } ) ^ { \alpha s } .$ . In particular,   
$\log { ( f ^ { - s } ) } = ( \log { f } ) ^ { - s }$ .   
$5 ^ { \circ }$ $f ^ { s } - g ^ { s } = O ( s ^ { p + 1 } ) \Leftrightarrow \log f ^ { s } - \log g ^ { s } = O ( s ^ { p + 1 } ) .$ .   
$6 ^ { \circ }$ $\begin{array} { r l r } & { \stackrel { \scriptscriptstyle \mathcal { I } } { f ^ { s } } \circ g ^ { s } = g ^ { s } \circ f ^ { s } \Leftrightarrow \left[ \log f ^ { s } , \log g ^ { s } \right] = 0 \Leftrightarrow \log f ^ { s } \circ g ^ { s } ) = \log f ^ { s } + \log g ^ { s } + \log g ^ { s } . } & \\ & { ( f ^ { s } \circ g ^ { s } ) = h ^ { s } \Leftrightarrow \log h ^ { s } = \log ( f ^ { s } \circ g ^ { s } ) = \log f ^ { s } + \log g ^ { s } + \displaystyle \sum _ { k = 1 } ^ { \infty } d _ { k } ( \log f ^ { s } , \log g ^ { s } ) . } & \end{array}$ $7 ^ { \circ }$   
$8 ^ { \circ }$ $f ^ { s }$ symplectic $\Leftrightarrow$ all $a _ { k }$ are Hamiltonian fields (see Chapter 5).   
$9 ^ { \circ }$ $f ^ { s }$ contact $\Leftrightarrow$ all $a _ { k }$ are contact fields (see Chapter 11).   
$1 0 ^ { \circ }$ $f ^ { s }$ volume-preserving $\Leftrightarrow$ all $a _ { k }$ are source-free fields (see Chapter 10).

The log transform has important bearing on dynamical systems with Lie algebra structure. The structure-preserving property of maps $f ^ { s }$ at the Lie group $( \mathbf { G } \subset \mathbf { D } _ { m } )$ ) level can be characterized through their logarithms at the associated Lie algebra $\mathbf { L } \subset$ $\mathbf { V } _ { m }$ ) level.

# 9.3 Algorithmic Approximations to Phase Flows

# 9.3.1 Approximations of Phase Flows and Numerical Method

We return to the main problem of approximation to the phase flow for dynamical system ${ \frac { \operatorname { d } { \boldsymbol { x } } } { \operatorname { d } t } } = a ( { \boldsymbol { x } } )$ .

$$
\begin{array} { l } { { f _ { a } ^ { s } = f ^ { s } = 1 _ { N } + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } f _ { k } \approx e _ { a } ^ { s } = 1 _ { N } + \displaystyle \sum _ { k = 1 } ^ { \infty } s ^ { k } e _ { k } , } } \\ { { e _ { k } = \displaystyle \frac { a ^ { k } } { k ! } . } } \end{array}
$$

If $f _ { k } = e _ { k }$ $( 1 \leq k \leq p )$ ), we say $f _ { a } ^ { s }$ is accurate to order $\geq p$ , if moreover, $f _ { p + 1 } \neq e _ { p + 1 }$ we say it is accurate to order $p$ .

Let $\log f ^ { s } = a ^ { s } = \sum s ^ { k } a _ { k } .$ . Note that the first $p { + 1 }$ equations in (2.2) completely determine $a _ { 1 } , a _ { 2 } , \cdots , a _ { p + 1 }$ and $f _ { 1 } , f _ { 2 } , \cdots , f _ { p + 1 }$ each other. It is then easy to establish

$$
\begin{array} { r l } & { f _ { k } = e _ { k } , \quad 1 \leq k \leq p ; \quad f _ { p + 1 } \neq e _ { p + 1 } \Longleftrightarrow } \\ & { a = a _ { 1 } = e _ { 1 } ; \quad a _ { k } = 0 , \quad 1 < k \leq p ; \quad a _ { p + 1 } = f _ { p + 1 } - e _ { p + 1 } \neq 0 . } \end{array}
$$

So, the orders of approximation for $f _ { a } ^ { s } \approx e _ { a } ^ { s }$ and for $\log f _ { a } ^ { s } - s a$ are the same.

Moreover, note that we have a formal field

$$
s ^ { - 1 } \log f ^ { s } = s ^ { - 1 } a ^ { s } = a + \sum _ { k = 1 } ^ { \infty } s ^ { k + 1 } a _ { k + 1 } = a + O ( s ^ { p } ) ,
$$

which is the original field $a$ up to a near-0 perturbation and defines a formal dynamical system

$$
{ \frac { \mathrm { d } x } { \mathrm { d } t } } = ( s ^ { - 1 } \log f ^ { s } ) ( x ) = a ( x ) + \sum _ { k = 1 } ^ { \infty } { s ^ { k + 1 } a _ { k + 1 } ( x ) }
$$

whose diagoible algorithm formal of order $t$ $s$ is exactly ed solution $t$ $e _ { s ^ { - 1 } a ^ { s } } ^ { t } ~ = ~ \exp { t s ^ { - 1 } } a ^ { s }$ $e _ { s ^ { - 1 } a ^ { s } } ^ { t } | _ { t = s }$ $f ^ { s }$ $f _ { a } ^ { s }$ $p$   
equation with field $a$ ; however, it gives the right solution of a perturbed equation with field $s ^ { - 1 } \log f _ { a } ^ { s } = a + O ( s ^ { p } )$ . There could be many methods with the same formal order of accuracy but with quite different qualitative behavior. The problem is to choose among them those leading to allowable perturbations in the equation. For systems with geometric structure, the $8 ^ { \circ } , 9 ^ { \circ } , 1 0$ $1 0 ^ { \circ }$ of Proposition 2.1 provide guidelines for a proper choice. The structure-preservation requirement for the algorithms precludes all unallowable perturbations alien to the pertinent type of dynamics. Take, for example, Hamiltonian systems. A transition map $f _ { a } ^ { s }$ for Hamiltonian field $a$ is symplectic if and only if all fields $a _ { k }$ are Hamiltonian, i.e., the induced perturbations in the equation are Hamiltonian. So symplectic algorithms are clean, inherently free from all kinds of perturbations alien to Hamiltonian dynamics (such as artificial dissipation inherent in the vast majority of conventional methods), this accounts for their superior performance. The situations are the same for contact and volume-preserving algorithms . The Proposition 2.1 profound impact on later developed called “Backward error series” work, “Modified equation” and “Modified integrator”[Hai94,CHV05,CHV07] .

# 9.3.2 Typical Algorithm and Step Transition Map

Finally we give, as an illustration, four simplest methods together with step transition maps and their logarithms.

$$
e _ { a } ^ { s } = 1 _ { N } + s a + \frac { 1 } { 2 } s ^ { 2 } a ^ { 2 } + \frac { 1 } { 3 ! } s ^ { 3 } a ^ { 3 } + O ( s ^ { 4 } ) .
$$

(1) Explicit Euler method $( E )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = s a ( x _ { 0 } ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = s a , } } \\ { { \displaystyle f _ { E } ^ { s } = 1 _ { N } + s a , } } \\ { { \displaystyle \log f _ { E } ^ { s } = s a - \frac { s ^ { 2 } } { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \end{array}
$$

non-revertible, order $= 1$ .

(2) Implicit Euler method $( I )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = s a ( x _ { 1 } ) , } } \\ { { f ^ { s } - 1 _ { N } = s a \circ f ^ { s } , } } \\ { { f _ { I } ^ { s } = ( 1 _ { N } - s a ) ^ { - 1 } = ( f _ { E } ^ { - s } ) ^ { - 1 } = 1 + s a + s ^ { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \\ { { \log f _ { I } ^ { s } = s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + O ( s ^ { 3 } ) , } } \end{array}
$$

non-revertible, order $= 1$

(3) Trapezoidal method $( T )$ :

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = \displaystyle \frac { s } { 2 } ( a ( x _ { 1 } ) + a ( x _ { 0 } ) ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = \displaystyle \frac { s } { 2 } ( a \circ f ^ { s } + a ) , } } \\ { { \displaystyle f _ { T } ^ { s } = \left( 1 _ { N } - \frac { s } { 2 } a \right) ^ { - 1 } \circ \left( 1 _ { N } + \frac { s } { 2 } a \right) = f _ { I } ^ { \frac { s } { 2 } } \circ f _ { E } ^ { \frac { s } { 2 } } } } \\ { { \displaystyle ~ = ( f _ { E } ^ { \frac { s } { 2 } } ) ^ { - 1 } \circ f _ { C } ^ { s } \circ f _ { E } ^ { \frac { s } { 2 } } = 1 _ { N } + s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + \frac { s ^ { 3 } } { 4 } a ^ { 3 } + O ( s ^ { 4 } ) , } } \\ { { \log f _ { T } ^ { s } = s a + \frac { s ^ { 3 } } { 1 2 } a ^ { 3 } + O ( s ^ { 5 } ) , } } \end{array}
$$

revertible, order ${ \it \Delta \phi } = 2 { \it \Delta \Psi }$ , symplectic for linear Hamiltonian but non-symplectic for nonlinear Hamiltonian systems, where $f _ { C } ^ { s }$ denoting following centered Euler scheme.

(4) Centered Euler method $( C )$ :

$$
\begin{array} { l } { { \displaystyle x _ { 1 } - x _ { 0 } = s a \Big ( \frac 1 2 \big ( x _ { 1 } + x _ { 0 } \big ) \Big ) , } } \\ { { \displaystyle f ^ { s } - 1 _ { N } = s a \circ \Big ( \frac 1 2 \big ( f ^ { s } + 1 _ { N } \big ) \Big ) , } } \end{array}
$$

2-stage version recommended for implementation:

$$
\begin{array} { r l } & { \bar { x } = x + \frac { s } { 2 } a ( \bar { x } ) , \quad x _ { 1 } = 2 \bar { x } - x _ { 0 } , } \\ & { \bar { x } = f _ { \bar { I } } ^ { \ \frac { s } { 2 } } ( x _ { 0 } ) , \qquad x _ { 1 } = 2 f _ { \bar { I } } ^ { \ \frac { s } { 2 } } ( x _ { 0 } ) - 1 _ { N } ( x _ { 0 } ) , } \\ & { f _ { C } ^ { \  s } = 2 f _ { \bar { I } } ^ { \ \frac { s } { 2 } } - 1 _ { N } = \left( 1 _ { N } + \frac { s } { 2 } a \right) \circ \left( 1 _ { N } - \frac { s } { 2 } a \right) ^ { - 1 } = f _ { E } ^ { \ \frac { s } { 2 } } \circ f _ { \bar { I } } ^ { \frac { s } { 2 } } } \\ & { \qquad = 1 _ { N } + s a + \frac { s ^ { 2 } } { 2 } a ^ { 2 } + \frac { s ^ { 3 } } { 8 } ( a _ { \ast } a ^ { 2 } + a ^ { 3 } ) + { \cal O } ( s ^ { 4 } ) , } \\ & { \log f _ { C } ^ { \ } = s a + s ^ { 3 } \left( \frac { 1 } { 8 } a _ { \ast } a ^ { 2 } - \frac { 1 } { 2 4 } a ^ { 3 } \right) + { \cal O } ( s ^ { 5 } ) , } \end{array}
$$

revertible, order $= 2$ , unconditionally symplectic with preservation of all quadratic invariants for Hamiltonian systems.

Note the similarities and delicate differences between $C$ and $T$ : Both can be composed by a $\frac { s } { 2 }$ implicit and a $\frac { s } { 2 }$ explicit stages but in opposite orderings. Moreover, they

are conjugate to each other. $C$ is far less known than $T$ , it becomes prominent only after the recent development of symplectic algorithms [Fen85] . In crucial aspects, $C$ is superior.

Remark 3.1. The above $\log f _ { C } ^ { s }$ is not others but just formal vector fields for centered Euler scheme or present called backward error analysis

$$
\bar { f } = f + \frac { s ^ { 2 } } { 1 2 } ( f ^ { \prime } f ^ { \prime } f - \frac { 1 } { 2 } f ^ { \prime \prime } ( f , f ) ) .
$$

# 9.4 Related B-Series Works

Consider the numerical solution of ODEs

$$
\dot { z } = f ( z ) , \quad z \in \mathbf { R } ^ { n } .
$$

B-series methods: B-series were introduced by Harier and Wanner $\mathrm { [ H W 7 4 ] }$ . The Taylor series of exact solution of (4.1) with initial value $z ( 0 ) = z$ can be written as

$$
z ( h ) = z + h f ( z ) + { \frac { h ^ { 2 } } { 2 ! } } f ^ { \prime } ( z ) f ( z ) + { \frac { h ^ { 3 } } { 3 ! } } { \big ( } f ^ { \prime \prime } ( f ( z ) , f ( z ) ) + f ^ { \prime } ( z ) f ^ { \prime } ( z ) f ( z ) { \big ) } + \cdots .
$$

B-series methods are numerical integrators $z _ { n + 1 } = \Phi _ { h } ( z _ { n } )$ whose Taylor series have the same structure with real coefficients $a ( \tau )$ :

$$
\begin{array} { r c l } { { \Phi _ { h } ( z ) } } & { { = } } & { { z + h a ( \bullet ) f ( z ) + h ^ { 2 } a ( \underline { { { \ O } } } ) f ^ { \prime } ( z ) f ( z ) + h ^ { 3 } \bigl ( \frac { a ( \underline { { { \ O } } } ) } { 2 ! } f ^ { \prime \prime } ( f ( z ) , f ( z ) ) } } \\ { { } } & { { } } & { { + a ( \bigl \{ \begin{array} { l } { { \ O } } \\ { { \ O } } \end{array}  + \ O } ( z ) f ^ { \prime } ( z ) f ^ { \prime } ( z ) \bigr ) + \cdot \cdot \cdot , }  \end{array}
$$

where coefficients $a ( \tau )$ are defined for all rooted trees and characterize the integrator.

Every numerical integrator (including $\mathbf { R - K }$ method) can be expanded into a Bseries as introduced and studied in[HW74] .

Definition 4.1 (rooted tree and forest). The set of rooted tree $T$ and forest $\mathcal { F }$ are defined recursively by

$1 ^ { \circ }$ The tree , only one vertex belong to $T$ ;   
$2 ^ { \circ }$ If $\tau _ { 1 } , \cdots , \tau _ { n }$ are $n$ tree of $\tau$ , the forest $u = \tau _ { 1 } , \cdots , \tau _ { n }$ is the commutative product of $\tau _ { 1 } , \cdots , \tau _ { n }$ ;   
$3 ^ { \circ }$ If $u$ is a forest of $\mathcal { F }$ , then $u = | \tau |$ is a tree of $T$ .

Let $T = \{ \cdot , \cdot , \cdot \} , \nabla , \cdot \cdot \cdot \}$ be the set of rooted trees and let $\varnothing$ be the empty tree. For $\tau _ { 1 } , \cdot \cdot \cdot , \tau _ { n } \in T$ , we denote by $\tau = [ \tau _ { 1 } , \cdots , \tau _ { n } ]$ the tree obtained by grafting the roots of $\tau _ { 1 } , \cdots , \tau _ { n }$ to a new vertex which becomes the root of $\tau$ . Elementary differentials $F _ { f } ( \tau )$ are defined by induction as

$$
F _ { f } ( \bullet ) ( z ) = f ( z ) , \quad F _ { f } ( \tau ) ( z ) = f ^ { ( m ) } ( z ) \big ( F _ { f } ( \tau _ { 1 } ) , \cdot \cdot \cdot , F _ { f } ( \tau _ { m } ) ( z ) \big ) .
$$

For real coefficients $a ( \emptyset )$ and $a ( \tau ) , \tau \in T$ a B-series is a series of the form

$$
B ( f , a , z ) ~ = ~ a ( \emptyset ) I d + \sum _ { \tau \in T } { \frac { h ^ { | \tau | } } { \sigma ( \tau ) } } ~ a ( \tau ) ~ F _ { f } ( \tau ) ( z ) ~
$$

where $I d$ stands for the identity; $I d ( z ) = z$ and the scalars $a ( \tau )$ are the known normalization coefficients[BSS96] . Now, we give following examples:

Example 4.2. The Taylor series of the exact solution of (4.1) can be written as a Bseries $z ( h ) = B ( f , e ) ( z _ { 0 } )$ with coefficients $a ( \tau ) = e ( \tau ) = \frac { 1 } { \gamma ( \tau ) } , \forall \tau \in T .$ .

Example 4.3. The coefficient B-series for explicit Euler scheme $a ( \tau ) = 0 , \forall \tau \in T$ except $a ( \cdot ) = 1$ .

Example 4.4. The coefficient B-series for implicit Euler scheme $a ( \tau ) = 1 , \forall \tau \in T$ .

Example 4.5. The coefficient B-series for centered Euler scheme $\boldsymbol { a } ( \tau ) = \left( \frac { 1 } { 2 } \right) ^ { | \tau | - 1 }$ , $\forall \tau \in T$ .

Example 4.6. The coefficient B-series for trapezoidal scheme $a ( \bullet ) = 1 , a ( \pmb { \zeta } ) =$

$$
{ \frac { 1 } { 2 } } , a ( \pmb { \gamma } ) = { \frac { 1 } { 2 } } , a ( \pmb { \gamma } ) = { \frac { 1 } { 4 } } , \cdots .
$$

Example 4.7. The coefficient B-series for R–K method $( A , b , c ) , a ( \tau ) = b ^ { \mathrm { T } } \phi ( \tau ) , \forall \tau$ $\forall \tau \in$ $T$ .

Partitions and skeletons: A partition $p ^ { \tau }$ of a tree $\tau$ is obtained by cutting some of the edges $\mathrm { [ C H V 0 7 ] }$ . The resulting list of trees is denoted by $P ( p ^ { \tau } )$ . Eventually, the set of all partitions $p ^ { \tau }$ of $\tau$ is denoted by $P ( p ^ { \tau } )$ . Now, given a partition $p ^ { \tau }$ , the corresponding skeleton $\chi ( p ^ { \tau } )$ , as introduced in $[ \mathrm { C H V 0 7 } ]$ , is the tree obtained by contracting each tree of $P ( p ^ { \tau } )$ to a single vertex and by re-establishing the cut edges (see Tables 4.1 – 4.25). We observe that a tree $\tau \in T$ has exactly $2 ^ { | \tau | - \bar { 1 } }$ partitions $p ^ { \tau }$ and that different partitions may lead to the same $P ( p ^ { \tau } )$ . An admissible partition is a partition with at most one cut along any part from the root to any terminal vertex. We denote ${ \mathcal { A } } { \mathcal { P } } ^ { \tau }$ as the set of admissible partition of $\tau$ and by convention, we suppose that $\varnothing \in { \mathcal { A } } { \mathcal { P } } ^ { \tau }$ . We denote $\# ( p ^ { \tau } )$ as number of subtrees. We denote this distinguished tree by $R ( p ^ { \tau } ) ( \operatorname { o r } r _ { p } )$ . We denote $P ^ { * } ( p ^ { \tau } ) = P ( p ^ { \tau } ) \setminus R ( p ^ { \tau } )$ as the list of forest that do not contain the root of $\tau$ . We distinguish $r _ { p }$ as the tree $v _ { p }$ (or $P ( p ^ { \tau } ) )$ whose root coincides with the root of $\tau$ . This tree is usually referred to as a subtree of $\tau$ and we denoted by $v _ { p } ^ { * } \left( \operatorname { o r } P ^ { * } ( p ^ { \tau } ) \right)$ the forest obtained by removing $r _ { p }$ from $v _ { p }$ . The above definition can be seen in Tables 4.1 – 4.25.

# 9.4.1 The Composition Laws

The following theorem result on the composition of B-series was obtained by[HW74] . Now we formulate this theorem in the form [CHV07] :

Theorem 4.8. Let $a , b : T \cup \{ \varnothing \} \to \mathbf { R }$ be two mappings, with $a ( \emptyset ) = 1$ . Then $B$ -series $B ( f , a ) ( z )$ inserted into $B ( f , b ) ( \cdot )$ is still a $B$ -series

$$
B ( f , b ) \big ( B ( f , a ) ( z ) \big ) = B ( f , a \cdot b ) ( z ) ,
$$

and $a \cdot b : T \cup \{ \varnothing \} \to \mathbf { R }$ is defined by

$$
( a \cdot b ) = b ( \emptyset ) = b ( \emptyset ) , \quad \forall \tau \in T , \quad ( a \cdot b ) = \sum _ { p \in A \mathcal { P } ( \tau ) } b ( r _ { p } ) a ( v _ { p } ^ { * } ) ,
$$

where a is extended to $\mathcal { F }$ , as follows:

$$
\forall u = \tau _ { 1 } \cdot \cdot \cdot \tau _ { n } \in \mathcal { F } , \quad a ( u ) = \prod _ { i = 1 } ^ { n } a ( \tau _ { i } ) .
$$

Table 4.1. The partitions of a tree of order 2 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>：</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1>{5</td><td rowspan=1 colspan=1>{5</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0}{}</td><td rowspan=1 colspan=1>{0}{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.2. The partitions of a tree of order 3 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{...)</td></tr><tr><td rowspan=1 colspan=1>R(pT）</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.3. The partitions of a tree of order 3 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>()</td></tr><tr><td rowspan=1 colspan=1>R(（p）</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.4. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1>{0}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.5. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>&gt;</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>丫</td></tr><tr><td rowspan=1 colspan=1>P(p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{M}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>p EAP</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.6. The partitions of a tree of order 4 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>.</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.7. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>()</td><td rowspan=1 colspan=1>()</td></tr><tr><td rowspan=1 colspan=1>R(p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{…})</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.8. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(pT）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(pT)</td><td rowspan=1 colspan=1>{0}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.9. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1>\</td><td rowspan=1 colspan=1>\</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pEAPT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.10. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R（p）</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p+)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>p ∈AP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.11. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>&gt;</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>）.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{..}</td><td rowspan=1 colspan=1>{·)}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>p ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.12. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(pT）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.13. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>中</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{0)</td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{..)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.14. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>入</td></tr><tr><td rowspan=1 colspan=1>P*(p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.15. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.16. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.17. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（pT)</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{…}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.}</td></tr><tr><td rowspan=1 colspan=1>#（pT）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.18. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td></tr><tr><td rowspan=1 colspan=1>R（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p）</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.19. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>心</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>心</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{..)</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pT ∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.20. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>v</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{0</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1>{0</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#(p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pT∈APT</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td></tr></table>

Table 4.21. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>力</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{..)</td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{..}</td></tr><tr><td rowspan=1 colspan=1>#(pT)</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAP</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.22. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td></tr><tr><td rowspan=1 colspan=1>P(pT)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>{v</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{M</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.23. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.)</td></tr><tr><td rowspan=1 colspan=1>#（p）</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pTEAPT</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.24. The partitions of a tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>vv</td><td rowspan=1 colspan=1>vv</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>#（p)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr></table>

Table 4.25. Continuous partitions of the above tree of order 5 with associated skeleton and forest   

<table><tr><td rowspan=1 colspan=1>pT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>x(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P(p）</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{.:)</td><td rowspan=1 colspan=1>{.:)</td><td rowspan=1 colspan=1>{.)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>R(p)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>P*（p)</td><td rowspan=1 colspan=1>{W}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td><td rowspan=1 colspan=1>{</td><td rowspan=1 colspan=1>{}</td><td rowspan=1 colspan=1>{.}</td></tr><tr><td rowspan=1 colspan=1>#（p</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>pEAP</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

# 9.4.2 Substitution Law

$\mathrm { I n } ^ { \mathrm { [ C H V 0 7 , C H V 0 5 ] } }$ ,they introduce a new composition law on B-series, denoted by $^ *$ and called law of substitution, obtained as a result of the substitution of vector field $g ( z ) =$ $\frac { 1 } { h } B ( f , b ) ( z )$ with $b ( \emptyset ) = 0$ , into another B-series $B ( g , a ) ( z )$ . Chartier, Hairer, and Vilmart give the following theorem:

Theorem 4.9. For $b ( \emptyset ) = 0$ , the vector field $h ^ { - 1 } B ( f , b )$ gives a $B$ -series

$$
B ( h ^ { - 1 } B ( f , b ) , a ) = B ( f , b \ast a ) .
$$

We have $( b * a ) ( \emptyset ) = a ( \emptyset )$ and for all $\tau \in T$ ,

$$
( b \ast a ) ( \tau ) = \sum _ { p \in \mathcal { P } ( \tau ) } a ( \chi _ { p } ) b ( v _ { p } ) ,
$$

where $b$ is extended to $\mathcal { F }$ as follows:

$$
\forall u = \tau _ { 1 } \cdot \cdot \cdot \tau _ { n } \in \mathcal { F } , \quad a ( u ) = \prod _ { i = 1 } ^ { n } a \left( \tau _ { i } \right) .
$$

Remark 4.10. The composition law for the trees of order $\leq 5$ is listed in Example 4.22.

Remark 4.11. The Substitution law for the (backward error) trees of order $\leq 5$ is listed in Example 4.24.

Remark 4.12. The Substitution law for the trees of order $\leq 5$ is listed in Example 4.23.

Modified integrators (called generating function method or preprocessed vector field integrators): Let $\Psi _ { f , h }$ is the exact h-flow for Equation (4.1) which is a B-series with coefficient $e ( \tau ) = \frac { 1 } { \gamma ( \tau ) }$ Consequently, the coefficient $\breve { b } ( \tau )$ of the modified differential equation for $\Phi _ { f , h } = B ( f , a )$ is obtained from

$$
( \breve { b } * a ) ( \tau ) = e ( \tau ) , \quad \forall \tau \in T .
$$

Backward error analysis (called formal vector field, modified equation or postprocessed vector field): The modified differential equation of a method $\Psi _ { f , h } = B ( f , e )$ is obtained by putting $\Phi _ { f , h }$ equal to the exact flow. Its coefficient $\widehat { b } ( \tau )$ is therefore obtained from

$$
( \widehat { b } * e ) ( \tau ) = a ( \tau ) , \quad \forall \tau \in T .
$$

Remark 4.13. Substituting the expression $\frac { 1 } { \gamma }$ given in (4.13) into (4.14) gives $\stackrel { \smile } { b } { * } \widehat { b } { * } a =$ $a$ . Therefore, $\breve { b }$ and $\widehat { b } ( \tau )$ are inverse elements for substitution law $^ *$

$$
\Breve { \boldsymbol { b } } ( \tau ) * \widehat { \boldsymbol { b } } ( \tau ) = \widehat { \boldsymbol { b } } ( \tau ) * \Breve { \boldsymbol { b } } ( \tau ) = \delta _ { \bullet } ( \tau ) .
$$

Proposition 4.14. Using formulae (4.13) and (4.11) in Example 4.23, we easily obtain modified centered Euler scheme of sixth order first find $\ d _ { i n } \mathrm { [ C H V 0 7 ] }$ :

$$
\begin{array} { r c l } { { \dot { z } } } & { { = } } & { { f ( z ) + \displaystyle \frac { h ^ { 2 } } { 2 4 } \big [ f ^ { ( 2 ) } ( f , f ) - 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + \displaystyle \frac { h ^ { 4 } } { 1 2 0 } \big [ \frac { 3 } { 4 8 } f ^ { ( 4 ) } ( f , f , f , f ) } } \\ { { } } & { { } } & { { - \displaystyle \frac { 1 } { 4 } f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ) + \frac { 1 } { 4 } f ^ { ( 2 ) } ( f , f ^ { ( 2 ) } ( f , f ) ) - f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { + \displaystyle \frac { 2 } { 4 } f ^ { ( 2 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) - \frac { 3 } { 1 2 } f ^ { ( 1 ) } f ^ { ( 3 ) } ( f , f , f ) + \displaystyle \frac { 1 } { 2 } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { - \displaystyle \frac { 1 } { 4 } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) + f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + O ( h ^ { 6 } ) . } } \end{array}
$$

Proof. First, we must point out $\breve { b } ( \tau ) = 0 , \forall | \tau | = e v e n$ . We calculate coefficient $\breve { b } (  { \uparrow } )$ as follows

$$
\begin{array} { r l r } & { } & { \check { b } ( \begin{array} { c } { \check { \pmb { \zeta } } } \\ { \check { \pmb { \updownarrow } } } \end{array} ) + 2 a ( \dot { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \pmb { \zeta } ) + a ( \pmb { \gamma } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \dot { \pmb { \zeta } } ) } \\ & { } & { \qquad \vdots } \\ & { } & { + a ( \dot { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 2 } \check { b } ( \pmb { \zeta } ) + a ( \check { \pmb { \zeta } } ) \check { b } ( \bullet ) ^ { 5 } = e ( \check { \pmb { \zeta } } ) . } \end{array}
$$

Note the formula in Example 4.23, coefficient $a ( \tau )$ in Example 4.5, and $\gamma ( \tau )$ in Table

4.26, we have $\begin{array} { r } { \check { b } ( \displaystyle \sum _ { i = 0 } ^ { j } + \frac { 1 } { 2 4 } - \frac { 1 } { 1 6 } = \frac { 1 } { 2 4 0 } . } \end{array}$

The proof of others is left to the reader.

Proposition 4.15. In 2001, the author first obtained modified equation for centered Euler scheme given in Example 4.6 of Chapter 7. Using formulas (4.14) and (4.23) in Example 4.24, we can obtain this formula again.

Proof. First, we must point out ${ \widehat b } ( \tau ) = 0 , \forall | \tau | = e v e n$ . We calculate coefficient $\widehat { b } ( \curlyeq \Psi )$ as follows

$$
\widehat { b } ( { \mathbb { V } } ) + 6 e ( { \mathbb { V } } ) \widehat { b } ( \bullet ) ^ { 2 } \widehat { b } ( { \mathbb { V } } ) + \frac { 1 } { \gamma } ( { \mathbb { V } } ) = a ( { \mathbb { V } } ) .
$$

Note the formula in Example 4.22, coefficient $a ( \tau )$ in Example 4.5, and $\gamma ( \tau )$ in Table 4.26, we have $\widehat { b } ( \Psi ) = \frac { 1 } { 1 6 } + \frac { 1 } { 6 } - \frac { 1 } { 5 } = \frac { 7 } { 2 4 0 }$ The proof of others is left to the reader.

Remark 4.16. After calculating the coefficients $\breve { b } ( \tau )$ and $\widehat { b } ( \tau )$ , we list following in Table 4.26.

Remark 4.17. Can directly test following equation

$$
\Breve { b } ( \tau ) * \widehat { b } ( \tau ) = \delta _ { \bullet } ( \tau ) ,
$$

via $^ *$ operation formula (4.11).

Remark 4.18. Relating the previous laws to two Hopf algebra introduced, respectively, by Connes and Kremer[CK98] and by Calaque, Ebrahimi-Fard, and Manchon[CEFM08] , we can see these papers[Bro00],[CHV08]].

Table 4.26. Coefficients $\sigma ( \tau ) , \gamma ( \tau ) , \breve { b } ( \tau )$ , and $\widehat { b } ( \tau )$ for trees of order $\leqslant 5$   

<table><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>！</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1>丫</td><td rowspan=1 colspan=1>！</td></tr><tr><td rowspan=1 colspan=1>g(T)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Y(T)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>6(1)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1/12</td><td rowspan=1 colspan=1>−1/12</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>6()</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>−1/12</td><td rowspan=1 colspan=1>1/12</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>&lt;</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VY</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>?</td></tr><tr><td rowspan=1 colspan=1>g(T)</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>7(T)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>(T)</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>1/120</td><td rowspan=1 colspan=1>-1/80</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>-1/120</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>1/120</td><td rowspan=1 colspan=1>1/240</td></tr><tr><td rowspan=1 colspan=1>6(T)</td><td rowspan=1 colspan=1>7/240</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>-7/240</td><td rowspan=1 colspan=1>-1/240</td><td rowspan=1 colspan=1>-1/80</td><td rowspan=1 colspan=1>1/240</td><td rowspan=1 colspan=1>1/80</td><td rowspan=1 colspan=1>−1/240</td></tr></table>

# 9.4.3 The Logarithmic Map

The coefficient $\omega ( \tau )$ can be interpreted as the coefficient of the modified field obtained by backward error analysis, for the explicit Euler method $z _ { 1 } = z _ { 0 } + h f ( z _ { 0 } )$ , corresponding to $a = \delta _ { \emptyset } + \delta _ { \bullet }$ . They can be computed by formula (4.11) or (4.22). Murua $\mathrm { i n } ^ { [ \mathrm { M u r 0 6 } ] }$ ∅ •gives the following formula

$$
\begin{array} { r } { \log { ( a ) } = ( a - b _ { \emptyset } ) * \omega . } \end{array}
$$

Properties of logarithmic map has been discussed in Proposition 2.1. Using formula of Example 4.24, determined $\omega ( \tau ) ( = \widehat { b } ( \tau ) )$ recursively , because $a ( \tau ) = 0 \forall \tau \in T$ except $a ( \cdot ) = 1$ .

For example: from 14 formula of Example 4.24, we have

$$
\begin{array} { r l } & { b ( \sqrt [ ] { \textstyle \mathstrut } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 1 2 } ) + ( \frac { 1 } { 2 } ) ( - \frac { 1 } { 2 } ) ( \frac { 1 } { 6 } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 2 } ) ( \frac { 1 } { 3 } ) + \frac { 1 } { 2 } ( - \frac { 1 } { 4 } ) + \frac { 1 } { 6 } ( \frac { 1 } { 6 } ) + 2 ( \frac { 1 } { 6 } ) ( \frac { 1 } { 4 } ) } \\ & { + ( \frac { 1 } { 3 } ) ( \frac { 1 } { 4 } ) + 2 ( \frac { 1 } { 3 } ) ( \frac { 1 } { 3 } ) + ( \frac { 1 } { 2 4 } ) ( - \frac { 1 } { 2 } ) + 3 ( \frac { 1 } { 8 } ) ( - \frac { 1 } { 2 } ) + \frac { 1 } { 3 0 } = 0 , } \end{array}
$$

then we get

$$
\omega ( { \dot { \bigtriangledown } } ) = b ( { \dot { \bigtriangledown } } ) = { \frac { 1 } { 2 0 } } .
$$

The test of others $\omega ( \tau )$ is left the reader.

We give following Table 4.27(compare with [Mur06],[CHV05][CHV08],[CEFM08] ).

Table 4.27. Coefficient $\omega ( \tau )$ for trees of order $\leqslant 5$   

<table><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>w(t)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1/2</td><td rowspan=1 colspan=1>1/6</td><td rowspan=1 colspan=1>1/3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1/12</td><td rowspan=1 colspan=1>-1/6</td><td rowspan=1 colspan=1>-1/4</td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>ω(t）-1/30</td><td rowspan=1 colspan=1>ω(t）-1/30</td><td rowspan=1 colspan=1>-1/60</td><td rowspan=1 colspan=1>1/30</td><td rowspan=1 colspan=1>1/30</td><td rowspan=1 colspan=1>1/10</td><td rowspan=1 colspan=1>1/20</td><td rowspan=1 colspan=1>3/20</td><td rowspan=1 colspan=1>1/5</td><td rowspan=1 colspan=1>1/60</td></tr></table>

Definition 4.19. (Lie derivative of B-series) Let $b ( \tau )$ with $b ( \emptyset ) = 0$ and $a ( \tau )$ be the coefficient of two B-series and let $z ( t )$ be a formal solution of the differential equation $h \dot { z } ( t ) = B ( b , z ( t ) )$ . The Lie derivatives of the function $B ( a , z ( t ) )$ with respect to the vector field $B ( b , z ( t ) )$ is again B-series

$$
h \frac { \mathrm { d } } { \mathrm { d } t } B ( a , z ( t ) ) = B ( \partial _ { b } a , z ( t ) ) .
$$

Its coefficients are given by $\partial _ { b } a ( \emptyset ) = 0$ and for $| \tau | \geq 1$ by

$$
\partial _ { b } a ( \tau ) = \sum _ { \theta \in S P ( \tau ) } a ( \theta ) b ( \tau \setminus \theta ) , \quad \partial _ { b } a ( \tau ) = \sum _ { p ^ { \tau } \in \mathcal { P } ( \tau ) } a ( \chi _ { p } ) b ( v _ { p } ) .
$$

Exercise 4.20. [HLW02] Prove that the coefficient of modified differential equation are recursively defined by $b ( \emptyset ) = 0 , b ( \cdot ) = 1$ and

$$
b ( \tau ) = a ( \tau ) - \sum _ { j = 2 } ^ { | \tau | } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) ,
$$

where $\partial _ { b } ^ { j - 1 } b ( \tau )$ is the $( j - 1 )$ -th iterative of the Lie-derivative $\partial _ { b }$ .

Proposition 4.21. The above-mentioned formula (4.20) is just formula $b * \frac { 1 } { \gamma ( \tau ) } =$ $a ( \tau )$ namely

$$
\sum _ { j = 1 } ^ { | \tau | } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) = b ( \tau ) * \frac { 1 } { \gamma ( \tau ) } .
$$

Proof. Note that formula (4.23) in Example 4.24 and Tables 4.1 – 4.25, can obtain this results directly. -

For Example: from 4th formula of Example 4.24, we have

$$
\begin{array}{c} \begin{array} { c }  { e ( \bullet ) b ( \displaystyle \sum _ { \begin{array} { l } { b } \\ { { } \end{array} } + 2 e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \underline { { { \uparrow } } } ) + e ( \displaystyle \sum _ { } ^ { \bullet } ) b ( \bullet ) ^ { 3 } = a ( \displaystyle \sum _ { } ^ { } ) , } } \\ { { b ( \displaystyle \sum _ { \begin{array} { l } { b } \\ { { } \end{array} } + b ( \bullet ) b ( \underline { { { \uparrow } } } ) + \frac { 1 } { 6 } b ( \bullet ) ^ { 3 } = a ( \displaystyle \sum _ { } ^ { } ) , } } \\ { { b ( \displaystyle \sum _ { } ^ { } ) = a ( \displaystyle \sum _ { } ^ { \bullet } ) - b ( \bullet ) b ( \underline { { { \uparrow } } } ) - \frac { 1 } { 6 } b ( \bullet ) ^ { 3 } . } } \end{array} } \end{array}
$$

Example 4.22. The composition laws for the trees of order $\leq 5$ are

$$
\begin{array} { r l } { \alpha _ { 1 } \zeta _ { 2 } } & { = \beta _ { 2 } \zeta _ { 1 } + \frac { 1 } { 2 } - \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 1 } + \frac { 1 } { 8 } \beta _ { 4 } \zeta _ { 2 } } \\ { \gamma _ { 3 } \zeta _ { 2 } } & { = \left. \zeta _ { 2 } \zeta _ { 3 } \right. - \frac { 1 } { 8 } \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \alpha _ { 3 } \zeta _ { 2 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \alpha _ { 3 } \zeta _ { 3 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + 4 \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. - 6 \left. \zeta _ { 2 } \zeta _ { 3 } \right. + \frac { 1 } { 8 } \zeta _ { 3 } } \\ { \zeta _ { 4 } } & { = \beta _ { 3 } \zeta _ { 2 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. - \frac { 1 } { 8 } \zeta _ { 3 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. } \\ { \beta _ { 4 } \zeta _ { 2 } } & { = \beta _ { 3 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } \right. + 8 \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. - \beta _ { 4 } \zeta _ { 3 } + \frac { 1 } { 8 } \left. \zeta _ { 2 } \zeta _ { 3 } + \zeta _ { 3 } \right. + \beta _ { 4 } \zeta _ { 3 } } \\ { \zeta _ { 3 } \zeta _ { 4 } } &  = \beta _ { 3 } \zeta _ { 2 } + \frac   \end{array}
$$$$
\begin{array} { r l } & { \quad \alpha : \forall \mathcal { F } _ { j } = \alpha \mathcal { F } _ { j } \left( \mathcal { F } _ { j } + \mathcal { E } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } , \mathcal { H } _ { j } \right) } \\ & { \quad = \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } + \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } - \alpha \left( \mathcal { F } _ { j } \right) ^ { T } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array} { r l } { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \{ \vec { y } \} + b ( \langle \cdot \rangle \cdot a ( \mathbb { Y } ) + b ( \bullet ) \cdot a ( \bigstar ) ) + b ( \bigstar ) \cdot a ( \bullet ) ^ { 2 } } \\ & { \qquad \int } \\ & { \quad + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) } \\ { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \{ \vec { y } \} ) + b ( \bigstar ) \cdot a ( \langle \cdot \rangle + b ( \bullet ) \cdot a ( \bigstar ) + b ( \underline { { Y } } ) \cdot a ( \bigstar ) } \\ & { \qquad \int } \\ & { \qquad + b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) } \\ { \underset { a \cdot b ( \bigstar ) } { \big \downarrow } } & { = b ( \emptyset ) \cdot a ( \bigstar ) + b ( \bigstar ) \cdot a ( \bullet ) + b ( \bullet ) \cdot a ( \bullet ) \cdot a ( \mathbb { Y } ) + b ( \bigstar ) \cdot a ( \bullet ) ^ { 2 } } \\ & { \quad + b ( \bigstar ) \cdot a ( \bullet ) + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \cdot ) \cdot a ( \bullet ) \cdot a ( \mathbb { Y } ) + b ( \bigstar ) ^ { 2 } } \\ & { \quad + b ( \bigstar ) \cdot a ( \bullet ) + 2 b ( \bigstar ) \cdot a ( \bullet ) + b ( \bigstar ) \cdot a ( \mathbb { Y } ) \cdot a ( \mathbb { Y } ) } \end{array}
$$

Example 4.23. The substitution law $^ *$ defined in for the trees of order $\leq 5$ .

$$
 \begin{array} { r l } &   \begin{array} { r l } & { { \lambda } \operatorname { i n } ( t ^ { 2 } ) } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 3 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 4 } ] } \\ & { \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 5 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 6 } ] } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 6 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 5 } ] } \\ & { - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 6 } ] ) } \\ & { - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ) } \\ & { + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] + \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 7 } ] ) } \\ &  - \operatorname* { m a x } _ { i \in \mathbf { X } } [ t ^ { 1 } ] + \operatorname* { m a x } [ t ^ { 1 0 } ] ( \operatorname* { s u p } _ { i \in \mathbf { X } } [ t ^ { 1 } ] + \operatorname* { m a x } [ \end{array} \end{array}
$$

$$
\begin{array} { r l } { \Delta x ^ { 2 } \Delta y ( x , y , z ) } & { = \delta ^ { 2 } \Delta y ( x , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z ) ( 2 ) } \\ { \Delta z ( x , y , z ) } & { = \delta ^ { 2 } \Delta z ( x , y , z ) } \\ { \Delta x ^ { 2 } \Delta y ( x , y , z ) } & { = \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z ) - \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z ) - \Delta z ( x , y , z ) \Delta z ( x , y , z ) - \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , y ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ { \Delta z ( x , y , z , z ) } & { = \delta ^ { 2 } \Delta y ( x , y , z , y ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad = - \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ & { \quad \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , z ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \Delta y ( x , y , z , y , z ) } \\ & { \quad = \delta ^ { 2 } \Delta y ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) + \delta ^ { 2 } \Delta z ( x , y , z , y , z ) } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array} { r l } { \varepsilon _ { \perp } } & { = } \\ { \varepsilon _ { \perp } - \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\ { + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ( \varepsilon _ { \perp } ^ { \perp } \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } \\ & { + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } } \\ & { + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) ( \varepsilon _ { \perp } ^ { \perp } \Phi _ { 3 } ^ { \perp } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) ^ { 2 } + \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) \varepsilon _ { \perp } ^ { \perp } } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 2 } ^ { \parallel } ) } & { = } \\ { \varepsilon _ { \perp } ( \Phi _ { 3 } ^ { \parallel } ) } & { = } \\  \varepsilon _ { \perp } ( \Phi _ { 4 } ^ { \parallel } ) + \varepsilon _ { \perp } ( \Phi _  2 \end{array}
$$$$
\begin{array} { r l } { ( \lambda \circ u ) _ { i } ^ { \lambda } } & { = \alpha ( \lambda ^ { 1 } , \theta , \partial \lambda ^ { 2 } ) = \alpha ( \beta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + 2 \alpha ( \beta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } & { = \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } & { = \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) \qquad \quad \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ & { + \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ { ( \lambda \circ u ^ { 2 } , \theta \otimes u ^ { 2 } ) } \\ &  + 2 \alpha ( \lambda ^ { 1 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \otimes u ^ { 2 } , \theta \ \end{array}
$$

Example 4.24. The substitution law $^ *$ defined in for the trees of order $\leq 5$

$$
\begin{array} { r l } & { \delta \neq ( e ^ { - \frac { 1 } { 2 } } - e ^ { - \frac { 1 } { 2 } } ) \delta \neq ( 2 , 1 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } + \frac { 1 } { 2 } ( 2 ) \delta + 1 \right) ^ { 2 } \delta \neq ( 2 ) \delta \neq ( 1 + e ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 1 + e ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ & { \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \left( - e ^ { \frac { 1 } { 2 } } \delta ^ { 2 } \right) \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) \delta \neq ( 2 ) } \\ &  \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( 2 ) \delta \neq ( e ^ { \frac { 1 } { 2 } } ) \delta \neq ( e ^  \ \end{array}
$$

$$
\begin{array} { r l } { \psi _ { * } \gets ( \boldsymbol { * } ) b ( \dot { \mathcal { V } } ) = } & { e ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { H } } ( \cdot ) b ( \dot { \mathcal { V } } ) ) + ( e ( \cdot ) b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) + ) ^ { 2 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + 4 e ( \cdot \mathbb { V } ) b ( \dot { \mathcal { V } } ) ( b ( \cdot ) ^ { 3 } b ( \dot { \mathcal { V } } ) + e ( \cdot \mathbb { V } ) b ( \dot { \mathcal { V } } ) b ( \cdot ) ^ { 5 } ) } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) = } & { e ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + c ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + 2 c ( \cdot ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) } \\ & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathbb { V } } ) + 2 e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathcal { V } } ) + e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ^ { 2 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + 2 e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) ^ { 2 } + 2 e ( \mathbb { V } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) + 2 e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 3 } b ( \dot { \mathcal { V } } ) } \\ & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ( \dot { \mathcal { V } } ) } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) } & { \quad + e ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) ^ { 5 } } \\ { b { \scriptsize * e } ( \dot { \mathcal { V } } ) } &  = e ( \cdot ) b ( \dot { \mathcal { V } } ) + 2 e ( \cdot ) b ( \dot { \mathcal { V } } ) b ( \dot { \mathcal { V } } ) + 2 c ( \dot { \mathcal { V } } ) b ( \ \end{array}
$$

$$
\begin{array} { r c l } { { b \ast e \big ( \textstyle { \mathsf { Y } } \big ) } } & { { = } } & { { e ( \bullet ) b ( \textstyle { \mathsf { Y } } ) + e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \textstyle { \mathsf { Y } } ) + 3 e ( \underline { { { \uparrow } } } ) b ( \bullet ) b ( \textstyle { \mathsf { Y } } ) } } \\ { { } } & { { } } & { { + 3 e ( \textstyle { \mathsf { Y } } ) b ( \bullet ) ^ { 2 } b ( \pmb { \mathsf { Y } } ) + 3 e ( \pmb { \mathsf { Y } } ) b ( \bullet ) ^ { 2 } b ( \textstyle { \mathsf { Y } } ) + e ( \pmb { \mathsf { Y } } ) b ( \bullet ) ^ { 3 } b ( \pmb { \updownarrow } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 3 e ( \textstyle { \mathsf { Y } } ) b ( \bullet ) ^ { 3 } b ( \pmb { \updownarrow } ) + e ( \pmb { \mathsf { Y } } ) _ { b ( \bullet ) ^ { 5 } } } } \end{array}
$$

$$
\begin{array} { r l } { \alpha  \sqrt { \frac { \beta } { \hbar } } } & { = \epsilon + \beta \frac { \hbar } { 8 } ( \frac { 1 } { \hbar } + \epsilon / \hbar ) \epsilon \frac { \hbar } { 2 } \hbar ( 3 + \epsilon / \hbar ) \epsilon ^ { \frac { \beta } { \hbar } } \gamma _ { 1 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\ & { + \epsilon ( \hbar / 8 / 2 3 \epsilon / \hbar ) \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\ & { + \epsilon \frac { \hbar } { 8 } ( \frac { 1 6 } { 1 6 } + \epsilon / \hbar \epsilon ^ { \frac { \beta } { \hbar } } { 1 6 } \epsilon \frac { 1 6 } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } \epsilon \frac { \hbar } { 1 6 } } \\  \alpha  \frac { \hbar } \end{array}
$$

$$
\begin{array} { r l } & { \quad + 4 2 7 5 \times 1 9 7 2 + 4 7 8 7 3 + 1 4 7 9 7 1 + 2 1 7 5 8 7 3 + 1 0 7 1 2 5 } \\ & { \quad + 1 4 7 8 1 4 8 5 8 7 1 + 2 1 2 1 5 1 9 8 1 8 7 8 2 8 1 } \\ & { \quad + 1 4 8 9 1 4 8 5 1 4 7 1 + 2 1 2 1 5 1 9 1 8 7 8 2 8 1 } \\ & { \quad - 1 3 4 0 6 9 9 7 1 1 + 1 4 7 1 9 1 2 + 1 4 1 9 1 1 4 5 1 1 2 1 + 2 1 1 1 4 1 6 1 7 8 4 1 } \\ & { \quad + 1 4 0 6 9 7 1 1 1 4 1 + 2 1 1 4 1 4 1 1 9 1 1 + 3 1 1 1 1 1 4 1 1 1 9 1 1 + 2 1 1 1 1 4 1 0 1 8 1 9 1 } \\ & { \quad + 1 6 8 8 4 1 1 4 1 9 1 1 4 1 + 2 1 1 1 4 1 0 1 4 1 1 + 3 1 1 1 1 4 1 1 4 1 1 1 9 1 1 + 3 1 1 1 1 1 8 1 1 1 } \\ & { \quad + 1 9 7 1 1 1 1 4 1 1 4 1 1 9 1 1 + 3 1 1 1 1 4 1 1 1 1 1 + 3 1 1 1 1 1 4 1 1 1 1 1 + 3 1 1 1 1 1 1 1 1 1 1 1 + 3 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 9 7 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 1 4 1 1 1 1 1 1 1 1 1 1 1 3 1 3 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 } \\ & { \quad - 1 3 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 } \\ & { \quad + 1 4 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 } \\ &  \quad + 1 1 1 1 1 1 1 1 + 1 1 1 1 1 1 1 1 1 +  \end{array}
$$

# Bibliography

[Bak05] H. F. Baker: Alternants and continuous groups. Proc. London Math. Soc., 3:24–47, (1905).   
[Bro00] Ch. Brouder: Runge–Kutta methods and renormalization. Euro. Phys. J. C, 12:521– 534, (2000).   
[BSS96] J. C. Butcher and J. M. Sanz-Serna: The number of conditions for a Runge–Kutta method to have effective order p. Appl. Numer. Math., 22:103–111, (1996).   
[CEFM08] D. Calaque, K. Ebrahimi-Fard, and D. Manchon: Two Hopf algebra of trees interacting. arXiv: 0806.2238 v 2, (2008).   
[CHV05] P. Chartier, E. Hairer, and G. Vilmart: A substitution law for B-series vector fields. Technical Report 5498, INRIA, (2005).   
[CHV07] P. Chartier, E. Hairer, and G. Vilmart: Numerical integration based on modified differential equations. Math. Comp., 76(260):1941–1953, (2007).   
[CHV08] P. Chartier, E. Hairer, and G Vilmart: Composing and substituting S-series and Bseries of integrators and vector fields. Preprint, www.irisa.fr/ipso/fichiers/algebraic.pdf, (2008).   
[CK98] A. Connes and D. Kreimer: Hopf algebra, renormazation and noncommutative geometry. Communications in Mathematical Physics, 199:203–242, (1998).   
[Dyn46] E. B. Dynkin: Normed Lie algebra and analytic groups, volume 1. Amer. Math. Soc. (translation), (1946).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen92] K. Feng: Formal power series and numerical methods for differential equations. In T. Chan and Z. C. Shi, editors, International conf. on scientific computation, pages 28–35. World Scientific, Singapore, (1992).   
[Fen93a] K. Feng: Formal dynamical systems and numerical algorithms. In K. Feng and Z. C. Shi, editors, International conf. on computation of differential equations and dynamical systems, pages 1–10. World Scientific, Singapore, (1993).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C. Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equations and dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[Hai94] E. Hairer: Backward analysis of numerical integrators and symplectic methods. Annals of Numer. Math., 1:107–132, (1994).   
[Hau06] F. Hausdorff: Die symbolische exponentialformel in der gruppentheorie. Berichte der Sachsischen Akad. der Wissensch., 58:19–48, (1906).   
[HLW02] E. Hairer, Ch. Lubich, and G. Wanner: Geometric Numerical Integration. Number 31 in Springer Series in Computational Mathematics. Springer-Verlag, Berlin, (2002).   
[HW74] E. Hairer and G. Wanner: On the Butcher group and general multivalue methods. Computing, 13:1–15, (1974).   
[Lie88] S. Lie; Zur theorie der transformationsgruppen. Christiania, Gesammelte Abh., Christ. Forh. Aar., 13, (1988).   
[Mur06] A. Murua: The Hopf algebra of rooted trees, free Lie algebra, and Lie series. Foundations of Computational Mathematics, 6(4):387–426, (2006).   
[Olv93] P. J. Olver: Applications of Lie Groups to Differential Equations. GTM 107. Springer-Verlag, Berlin, Second edition, (1993).   
[Ote91] J. A. Oteo: The Baker–Campbell–Hausdorff formula and nested commutator identities. J. of Math. Phys., 32(2):419–424, (1991).   
[OW00] B. Owren and B. Welfert: The Newton iteration on Lie groups. BIT, 40(1):121–145, (2000).   
[Owr06] B. Owren: Order conditions for commutator-free Lie group methods. J. Phys. A: Math. Gen., 39:5585–5599, (2006).   
[Rei99] S. Reich: Backward error analysis for numerical integrators. SIAM J. Numer. Anal., 36:475–491, (1999).   
[SS96] J. M. Sanz-Serna: Backward Error Analysis for Symplectic Integrators. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 193–206. American Mathematical Society, New York, (1996).   
[SS97] J. M. Sanz-Serna: Geometric integration. In The State of the Art in Numerical Analysis (York, 1996), volume 63 of Inst. Math. Appl. Conf. Ser. New Ser., pages 121–143, Oxford Univ. Press, New York, (1997).

# Chapter 10. Volume-Preserving Methods for Source-Free Systems

Source-free dynamical systems is an important system in recent mechanics and physics. It has a abroad application. Therefore, designing a proper numerical method for this system is significant. It is well known that phase flow of source-free system is a volume-preserving transformation. Therefore, the transient operator of the numerical method that we design should be volume-preserving. We call this algorithm the volume-preserving algorithm.

# 10.1 Liouville’s Theorem

Let $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { N } ) ^ { \mathrm { T } }$ , and $f ( x ) = ( f _ { 1 } ( x ) , f _ { 2 } ( x ) , \cdot \cdot \cdot , f _ { N } ( x ) ) ^ { \mathrm { T } } : \mathbf { R } ^ { N }  \mathbf { R } ^ { N } ,$ then the dynamical system

$$
{ \frac { \operatorname { d } { \boldsymbol { x } } } { \operatorname { d } t } } = f ( { \boldsymbol { x } } )
$$

is source-free (i.e., divergence-free), when $\sum _ { i = 1 } ^ { N } { \frac { \partial f _ { i } } { \partial x _ { i } } } = 0$ (i.e., div $f ( x ) = 0 ,$ ). The flow of a source-free system is volume-preserving, i.e.,

$$
\operatorname* { d e t } { ( e _ { f } ^ { t } ( x ) ) _ { * } } = 1 , \quad \forall x , t ,
$$

here $e _ { f } ^ { t }$ denotes the flow of system (1.1) and $( e _ { f } ^ { t } ( x ) ) _ { * }$ the Jacobian of $e _ { f } ^ { t }$ at $x$ . Thus, volume-preserving schemes are required for computing the numerical solution of (1.1). If det $\biggl ( \frac { \partial x _ { n + 1 } } { \partial x _ { n . } } \biggr ) = 1$ , we call this scheme volume-preserving, where $x _ { n }$ denotes the numerical solution at step $n$ .

We know that the phase flow of Hamiltonian system preserves phase volume invariable. The source-free system is more general than the Hamiltonian system, we must prove that the phase flow preserving phase volume is invariable, considering the dynamic system (1.1), its phase flow is

$$
g ^ { t } ( x ) = x + f ( x ) t + o ( t ^ { 2 } ) .
$$

Let $D ( 0 )$ be a region in $x$ space and $V ( 0 )$ is its volume, then

$$
V ( t ) = \mathrm { v o l u m e ~ o f } D ( t ) , \quad D ( t ) = g ^ { t } D ( 0 ) .
$$

Theorem 1.1 (Liouville’s Theorem). If div $f = 0$ , then $g ^ { t }$ preserving the volume is invariable, $V ( t ) = V ( 0 )$ .

Proof. First proof

$$
\left. { \frac { \operatorname { d } V ( t ) } { \operatorname { d } t } } \right| _ { t = 0 } = \int _ { D ( 0 ) } \operatorname { d i v } f \operatorname { d } x ,
$$

for any $t$ , using the formula for changing variables in a multiple integral gives

$$
V ( t ) = \int _ { D ( 0 ) } \mathrm { d e t } \frac { \partial g ^ { t } x } { \partial x } \mathrm { d } x .
$$

Calculating $\frac { \partial g ^ { t } x } { \partial x }$ by formula (1.2), we find

$$
{ \frac { \partial g ^ { t } x } { \partial x } } = E + { \frac { \partial f } { \partial x } } t + O ( t ^ { 2 } ) , \quad { \mathrm { a s ~ } } t \to 0 .
$$

but

$$
\operatorname* { d e t } \left( E + A t \right) = 1 + t \operatorname { t r } A + O ( t ^ { 2 } ) , \quad t \to 0 ,
$$

where t $\cdot A = \sum _ { i = 1 } ^ { n } a _ { i i }$ . Therefore

$$
\begin{array} { l } { { \displaystyle { V ( t ) = \int _ { D ( 0 ) } [ 1 + t \mathrm { d i v } f + O ( t ^ { 2 } ) ] \mathrm { d } x } , } } \\ { { \displaystyle { \left. \frac { \mathrm { d } V ( t ) } { \mathrm { d } t } \right| _ { t = 0 } = \int _ { D ( 0 ) } \mathrm { d i v } f \mathrm { d } x . } } } \end{array}
$$

Then Equation (1.3) is proved. Now we take $t = t _ { 0 }$ is no worse than $t = 0$ , therefore

$$
\frac { \mathrm { d } V ( t ) } { \mathrm { d } t } \Big | _ { t = t _ { 0 } } = \int _ { D ( t _ { 0 } ) } \mathrm { d i v } f \mathrm { d } x ,
$$

and if div $f = 0 , \frac { \mathrm { d } V ( t ) } { \mathrm { d } t } = 0 .$ , d V (t) = 0. This completes the proof.

In particular, for Hamiltonian equation

$$
\operatorname { d i v } f = { \frac { \partial } { \partial p } } { \Big ( } - { \frac { \partial H } { \partial q } } { \Big ) } + { \frac { \partial } { \partial q } } { \Big ( } { \frac { \partial H } { \partial p } } { \Big ) } = 0 ,
$$

Liouville’s theorem is proved specially.

# 10.2 Volume-Preserving Schemes

# 10.2.1 Conditions for Centered Euler Method to be Volume Preserving

Let us consider centered Euler scheme

$$
x _ { n + 1 } = x _ { n } + \tau f \left( { \frac { x _ { n + 1 } + x _ { n } } { 2 } } \right) ,
$$

where $\tau$ is the step size in $t$ . We then have

$$
\begin{array} { l } { \displaystyle \frac { \partial x _ { n + 1 } } { \partial x _ { n } } = I _ { N } + \tau \mathbf { D } f \left( \frac { x _ { n + 1 } + x _ { n } } { 2 } \right) \left( \frac { 1 } { 2 } \frac { \partial x _ { n + 1 } } { \partial x _ { n } } + \frac { 1 } { 2 } I _ { N } \right) , } \\ { \displaystyle \frac { \partial x _ { n + 1 } } { \partial x _ { n } } = \frac { I _ { N } + \frac { \tau } { 2 } \mathbf { D } f ( x ^ { * } ) } { I _ { N } - \frac { \tau } { 2 } \mathbf { D } f ( x ^ { * } ) } . } \end{array}
$$

Here $\begin{array} { r l } & { \mathrm { , ~ } { \mathrm { D } } f = f _ { x } = \frac { \partial f } { \partial x } \equiv B = ( b _ { i j } ) , x ^ { \ast } = \frac { x _ { n + 1 } + x _ { n } } { 2 } . \mathrm { T h e ~ c o n d i t i o n ~ d e t } \left( \frac { \partial x _ { n + 1 } } { \partial x _ { n } } \right) = } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ w ~ r e q u i r e s ~ } \frac { | I _ { N } + \frac { T } { 2 } { \mathrm { D } } f ( x ^ { \ast } ) | } { | I _ { N } - \frac { T } { 2 } { \mathrm { D } } f ( x ^ { \ast } ) | } = 1 . \mathrm { L e t } \ : P ( \lambda ) = \left| { \mathrm { D } } f ( x ^ { \ast } ) - \lambda I _ { n } \right| \mathrm { b e ~ t h e ~ c h a r a c t e r - } } \\ & { \mathrm { ~ } \quad \cdots \quad \cdots } \end{array}$   
1, n   
istic matrix of $ { \mathrm { D } } f ( x ^ { * } )$ . Since

$$
\begin{array} { r } { \displaystyle \frac { \left| I _ { N } + \frac { \tau } { 2 } \mathbf { D } f ( x ^ { * } ) \right| } { \left| I _ { N } - \frac { \tau } { 2 } \mathbf { D } f ( x ^ { * } ) \right| } = \frac { \displaystyle \left| \frac { \tau } { 2 } \left( \mathbf { D } f ( x ^ { * } ) + \frac { 2 } { \tau } I _ { N } \right) \right| } { \displaystyle \left| - \frac { \tau } { 2 } \left( \mathbf { D } f ( x ^ { * } ) - \frac { 2 } { \tau } I _ { N } \right) \right| } = ( - 1 ) ^ { N } \frac { P \left( \frac { 2 } { \tau } \right) } { P \left( - \frac { 2 } { \tau } \right) } , } \end{array}
$$

we then get the condition for scheme (2.1) to be volume-preserving[QZ93] , i.e.,

$$
P ( \lambda ) = ( - 1 ) ^ { N } P ( - \lambda ) .
$$

Let us consider some particular cases of $N$ to show that scheme (2.1) is not always volume preserving.

Case 2.1. In this case, we have

$$
P ( \lambda ) = \lambda ^ { 2 } + ( b _ { 1 1 } + b _ { 2 2 } ) \lambda + b _ { 1 1 } b _ { 2 2 } - b _ { 1 2 } b _ { 2 1 } .
$$

Sin ce $\sum _ { i = 1 } ^ { N } { \frac { \partial f _ { i } } { \partial x _ { i } } } = 0$ = 0, i.e., tr B = 0, then P (λ) = λ2 + b11b22 − b12b21, and

$$
P ( - \lambda ) = P ( \lambda ) .
$$

Thus, the scheme (2.1) is always volume-preserving for source-free systems of dim.2.

# Case 2.2. Here

$$
P ( \lambda ) = - \lambda ^ { 3 } + ( b _ { 1 1 } + b _ { 2 2 } + b _ { 3 3 } ) \lambda ^ { 2 } - c \lambda + | { \cal B } | = - \lambda ^ { 3 } - c \lambda + | { \cal B } | ,
$$

where

$$
c = \left| \begin{array} { l l } { { b _ { 1 1 } } } & { { b _ { 1 2 } } } \\ { { b _ { 2 1 } } } & { { b _ { 2 2 } } } \end{array} \right| + \left| \begin{array} { l l } { { b _ { 2 2 } } } & { { b _ { 2 3 } } } \\ { { b _ { 3 2 } } } & { { b _ { 3 3 } } } \end{array} \right| + \left| \begin{array} { l l } { { b _ { 1 1 } } } & { { b _ { 1 3 } } } \\ { { b _ { 3 1 } } } & { { b _ { 3 3 } } } \end{array} \right| .
$$

The volume-preserving condition for Euler method is now $| B | = 0$ . For example, (ABC flow) when system (1.1) takes the form

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } x } { \mathrm { d } t } = c y - b z , } \\ { \displaystyle \frac { \mathrm { d } y } { \mathrm { d } t } = a z - c x , \quad a , b , c \in { \bf R } , } \\ { \displaystyle \frac { \mathrm { d } z } { \mathrm { d } t } = b x - a y , } \end{array}
$$

we have $| B | = 0$ . For this dynamical system, centered Euler method is volumepreserving.

Lemma 2.3. Let $P ( \lambda )$ be the characteristic polynomial of matrix $A _ { N \times N }$ , then

$$
P ( \lambda ) = | A - \lambda I _ { N } | = ( - 1 ) ^ { N } \bigl ( \lambda ^ { N } - P _ { 1 } \lambda ^ { N - 1 } + P _ { 2 } \lambda ^ { N - 2 } + \cdots + ( - 1 ) ^ { N } P _ { N } \bigr ) ,
$$

where

$$
\begin{array} { l } { { P _ { 1 } = \displaystyle \sum _ { i } ^ { N } a _ { i i } = \mathrm { t r } A , } } \\ { { P _ { 2 } = \displaystyle \sum _ { i < j } ^ { N } \left| \begin{array} { l l } { { a _ { i i } } } & { { a _ { i j } } } \\ { { a _ { j i } } } & { { a _ { j j } } } \end{array} \right| , } } \end{array}
$$

$$
\begin{array} { l } { { P _ { 3 } = \displaystyle \sum _ { i < j < k } ^ { N } \left| \begin{array} { l l l } { { a _ { i i } } } & { { a _ { i j } } } & { { a _ { i k } } } \\ { { a _ { j i } } } & { { a _ { j j } } } & { { a _ { j k } } } \\ { { a _ { k i } } } & { { a _ { k j } } } & { { a _ { k k } } } \end{array} \right| , } } \\ { { \displaystyle \quad \dots . . } } \\ { { P _ { N } = | { \cal A } | . } } \end{array}
$$

Using Lemma 2.3, we can discuss the case $N = 4$ .

Case 2.4. At this time,

$$
P ( \lambda ) = \lambda ^ { 4 } - P _ { 1 } \lambda ^ { 3 } + P _ { 2 } \lambda ^ { 2 } - P _ { 3 } \lambda + | B | .
$$

Since $P _ { 1 } = \operatorname { t r } \left( B \right) = 0$ , then $P ( - \lambda ) = ( - 1 ) ^ { 4 } P ( \lambda )$ requires $P _ { 3 } = 0$ .

It must be pointed out that, when $N$ increases, more increasing number of conditions is required for system (2.1) to be volume-preserving, and it seems impossible to satisfy all these condition. But fortunately, for the special case when system (1.1) is Hamiltonian, i.e.,

$$
f = J \nabla H , \quad J = \left[ \begin{array} { c c } { O } & { - I _ { k } } \\ { I _ { k } } & { O } \end{array} \right] , \quad N = 2 k .
$$

Scheme (2.1) is volume-preserving. This is because the Hamiltonian system is sourcefree and $ Ḋ \mathrm Ḋ f Ḍ Ḍ$ is an infinitesimal symplectic matrix, we have the following Lemma.

# Lemma 2.5. Let $M$ be an infinitesimal symplectic matrix, if $\lambda$ is an eigenvalue of $M$ , so are $- \lambda , { \bar { \lambda } } , - { \bar { \lambda } }$ .

From Lemma 2.5, we know that $P ( - \lambda ) = ( - \lambda ) ^ { 2 k } P ( \lambda )$ is valid when system (1.1) is Hamiltonian, so Euler method is volume-preserving for Hamiltonian systems. In fact, the method is even symplectic for Hamiltonian systems, that is to say it also preserve the symplectic structure of Hamiltonian systems which is a much stronger property than volume-preserving.

# 10.2.2 Separable Systems and Volume-Preserving Explicit Methods

In this section, we consider a special kind of source-free systems called separable systems. System (1.1) is separable if

$$
\frac { \mathrm { d } x _ { i } } { \mathrm { d } t } = f _ { i } ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { i - 1 } , x _ { i + 1 } , \cdot \cdot \cdot , x _ { N } ) , \quad i = 1 , 2 , \cdot \cdot \cdot , N .
$$

We can divide the above system into $N$ source-free systems:

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } x _ { 1 } } { \mathrm { d } t } = f _ { 1 } ( x _ { 2 } , \cdots , x _ { N } ) , } \\ { \frac { \mathrm { d } x _ { 2 } } { \mathrm { d } t } = 0 , } \\ { ~ \vdots } \\ { \frac { \mathrm { d } x _ { N } } { \mathrm { d } t } = 0 . } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \mathrm { d } x _ { 1 } } { \mathrm { d } t } = 0 , } \\ { \displaystyle \frac { \mathrm { d } x _ { 2 } } { \mathrm { d } t } = f _ { 2 } ( x _ { 1 } , x _ { 3 } , \cdots , x _ { N } ) , } \\ { ~ \vdots } \\ { \displaystyle \frac { \mathrm { d } x _ { N } } { \mathrm { d } t } = 0 . } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } x _ { 1 } } { \mathrm { d } t } = 0 , } \\ { \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \frac { \mathrm { d } x _ { N - 1 } } { \mathrm { d } t } = 0 , } \\ { \quad \quad \quad \quad \frac { \mathrm { d } x _ { N } } { \mathrm { d } t } = f _ { N } ( x _ { 1 } , \cdot \cdot \cdot , x _ { N - 1 } ) . } \end{array} \right.
$$

The first order explicit Euler method can be applied to them to get the exact solutions of them, i.e., the phase flows of them. Using the composition method[QZ92] , we can construct first order explicit Euler volume-preserving scheme for system (2.6). The adjoint of this scheme is obtained from the implicit Euler method and is also explicit. Composing these two schemes, we get a reversible explicit. This process can be expressed by formal power series as shown below.

From Chapter 9, we know the flow of (1.1) can be represented by power of series.

$$
e _ { f } ^ { \tau } = 1 _ { N } + \sum _ { k = 1 } ^ { \infty } \tau ^ { k } e _ { k , f } , \quad e _ { k , f } : \mathbf { R } ^ { N } \longrightarrow \mathbf { R } ^ { N } , \quad e _ { k , f } = \frac { 1 } { k ! } { f ^ { * } } ^ { k } 1 _ { N } ,
$$

where $f ^ { * }$ denotes the first order differential operator , $f ^ { * } = \sum _ { i = 1 } ^ { N } f _ { i } { \frac { \partial } { \partial x _ { i } } }$ $f ^ { * 2 } = f ^ { * } \times$ $f ^ { * } , f ^ { * 3 } = f ^ { * } \times f ^ { * } \times f ^ { * } , \cdot \cdot \cdot , 1$ $1 _ { N }$ is the identity vector function, $1 _ { N } ( x ) = x$ . For simplicity, we just write out

$$
e _ { A } ^ { \tau } \cdot e _ { B } ^ { \tau } = e _ { c ^ { \tau } } ^ { \tau } ,
$$

the first several terms are

$$
c ^ { \tau } = A + B + \frac { \tau } { 2 } [ A , B ] + o ( \tau ^ { 2 } ) ,
$$

where $[ A , B ] = A _ { * } B - B _ { * } A$ is the Lie bracket of $A$ and $B , A _ { * } , B _ { * }$ denotes the Jacobian matrix of $A$ and $B$ .

We now rewrite system of Equations (2.7) – (2.9) in compact form as

$$
\frac { \mathrm { d } \boldsymbol { x } } { \mathrm { d } t } = \boldsymbol { a } _ { i } ( \boldsymbol { x } ) , \quad \boldsymbol { a } _ { i } = ( 0 , \cdots , 0 , f _ { i } , 0 , \cdots , 0 ) ^ { \mathrm { T } } , \quad i = 1 , 2 , \cdots , N .
$$

These integrable systems have flow

$$
e _ { a _ { i } } ^ { \tau } = 1 _ { N } + \sum _ { k = 1 } ^ { \operatorname* { i n f } } \tau ^ { k } e _ { k , a _ { i } } , \quad i = 1 , 2 , \cdots , N .
$$

Since we have $a _ { i } ^ { * N } 1 _ { N } ( x ) = a _ { i } ^ { * k } x = 0$ , when $k \geq 2$ , then

$$
e _ { a _ { i } } ^ { \tau } ( x ) = x + \sum _ { k = 1 } ^ { \operatorname* { i n f } } \tau ^ { k } e _ { k , a _ { i } } ( x ) = x + \sum _ { k = 1 } ^ { \operatorname* { i n f } } \frac { \tau ^ { k } } { k ! } a _ { i } ^ { * k } 1 _ { N } ( x ) = x + \tau a _ { i } ( x ) .
$$

Using the formula (2.10), we find

$$
e _ { a _ { N } } ^ { \tau } \times e _ { a _ { N - 1 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { 2 } } ^ { \tau } \times e _ { a _ { 1 } } ^ { \tau } = e _ { f + o ( \tau ) } ^ { \tau } .
$$

This means the concatenation eτa $e _ { a _ { N } } ^ { \tau } \times e _ { a _ { N - 1 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { 1 } } ^ { \tau }$ approximates the flow $e _ { f } ^ { \tau }$ to the first order of $\tau$ .

Because the equations in the system (2.11) are all source-free, their flows are all volume-preserving and the concatenation of them remains volume-preserving, so

$$
\begin{array} { r l } & { \operatorname* { d e t } \bigl ( ( e _ { a _ { N } } ^ { \tau } \times e _ { a _ { N - 1 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { 1 } } ^ { \tau } ) ( x ) \bigr ) _ { * } } \\ & { = \operatorname* { d e t } \big ( e _ { a _ { N } } ^ { \tau } ( x ^ { N - 1 } ) \big ) _ { * } \times \operatorname* { d e t } \big ( e _ { a _ { N - 1 } } ^ { \tau } ( x ^ { N - 2 } ) \big ) _ { * } \times \cdot \cdot \cdot \times \operatorname* { d e t } \big ( e _ { a _ { 1 } } ^ { \tau } ( x ^ { 0 } ) \big ) _ { * } = 1 , } \end{array}
$$

where $x ^ { 0 } = x , x ^ { 1 } = e _ { a _ { 1 } } ^ { \tau } ( x ^ { 0 } ) , \cdot \cdot \cdot , x ^ { N - 1 } = e _ { a _ { N - 1 } } ^ { \tau } ( x ^ { N - 2 } ) , x ^ { N } = e _ { a _ { N } } ^ { \tau } ( x ^ { N - 1 } ) .$

N− NThus, from system (2.6) we get volume-preserving scheme of first order. This is an explicit scheme since $e _ { a _ { i } } ^ { \tau } ( i = 1 , \cdots , N )$ are flows of integrable systems which can be i written as (2.13). From [QZ92] , we know the concatenation $e _ { a _ { N } } ^ { \tau } \times e _ { a _ { N - 1 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { 1 } } ^ { \tau }$ with its adjoint $e _ { a _ { 1 } } ^ { \tau } \times e _ { a _ { 2 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { N } } ^ { \tau }$ Nproduces a reversible scheme

$$
e _ { a _ { N } } ^ { \frac { \tau } { 2 } } \times e _ { a _ { N - 1 } } ^ { \frac { \tau } { 2 } } \times \cdot \cdot \cdot \times e _ { a _ { 1 } } ^ { \tau } \times \cdot \cdot \cdot \times e _ { a _ { N - 1 } } ^ { \frac { \tau } { 2 } } \times e _ { a _ { N } } ^ { \frac { \tau } { 2 } }
$$

of second order, but is still explicit. We can use theory of composition $[ \mathbf { Q } \mathbf { Z } ^ { 9 2 } ]$ to construct symplectic scheme of arbitrary order.

# 10.3 Source-Free System

Source-free dynamical systems on the Euclidean space $\mathbf { R } ^ { n }$ are defined by source-free (or divergence-free) vector fields $a : \mathbf { R } ^ { n } \to \mathbf { R } ^ { n }$ ,

$$
\operatorname { d i v } a ( x ) = \sum _ { i = 1 } ^ { n } { \frac { \partial a _ { i } ( x ) } { \partial x _ { i } } } = 0 , \quad \forall x \in \mathbf { R } ^ { n } ,
$$

through equations

$$
\frac { \mathrm { d } x } { \mathrm { d } t } = \dot { x } = a ( x ) ,
$$

here and hereafter, we use the coordinate description and matrix notation

$$
\begin{array} { r } { x = ( x _ { 1 } , \cdots , x _ { n } ) ^ { \mathrm { T } } , \quad a ( x ) = ( a _ { 1 } ( x ) , \cdots , a _ { n } ( x ) ) ^ { \mathrm { T } } , } \end{array}
$$

where $\mathrm { T }$ denotes the transpose of a matrix.

In this subsection, we mainly analyze and construct numerical algorithms proper for source-free systems. Such systems constitute one of the most important classical cases of dynamical systems preserving certain geometric structure and arise in many physical problems such as particle tracking in incompressible fluids and toroidal magnetic surface-generation in stellarators. Because of the difficulty and even impossibility of solving equations by quadrature, the numerical methods certainly play an important role in understanding the dynamic behavior of a system and in solving physical and engineering problems. On the other hand, the problem of whether a numerical algorithm is proper for a system is closely related to the problem of whether the algorithmic approximation to the corresponding phase flow approximates perfectly in some sense and even strictly preserve the structure of the system itself if the system has such structure. It has been evidenced with some typical examples in the Hamiltonian case that “nonproper” algorithms will result in essentially wrong approximations to the solutions of systems and “proper” algorithms may generate remarkably right ones.

But how does one evaluate a numerical algorithm to be proper for source-free systems? It is well known that intrinsic to all source-free systems there is a volume form of the phase space $\mathbf { R } ^ { n }$ , say

$$
\alpha = \mathrm { d } x _ { 1 } \wedge \mathrm { d } x _ { 2 } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x _ { n }
$$

such that the evolution of dynamics preserves this form. In other words, the phase flow $e _ { a } ^ { t }$ , of source-free system (3.2), satisfies the volume-preserving condition

$$
( e _ { a } ^ { t } ) ^ { * } \alpha = \alpha ,
$$

or equivalently,

$$
{ \operatorname* { d e t } } \frac { \partial e _ { a } ^ { t } ( x ) } { \partial x } = 1 , \quad \forall x \in { \mathbf { R } } ^ { n } , t \in { \mathbf { R } } .
$$

In addition to this, $e _ { a } ^ { t }$ satisfies the group property in $t$ ,

$$
e _ { a } ^ { 0 } = \mathrm { i d e n t i t y } , \quad e _ { a } ^ { t + s } = e _ { a } ^ { t } \circ e _ { a } ^ { s } .
$$

In fact, (3.5) and (3.7) completely describe the properties of the most general source-free dynamical systems. This fact suggests that a proper algorithmic approximation $g _ { a } ^ { s }$ to phase flow $e _ { a } ^ { s }$ for source-free vector field $a : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ should satisfy these two requirements. However, the group property (3.7) is too stringent in general for algorithmic approximations because only the phase flows satisfy it. Instead of it, a weaker requirement, i.e.,

$$
g _ { a } ^ { 0 } = \mathrm { i d e n t i t y } , \quad g _ { a } ^ { s } \circ g _ { a } ^ { - s } = \mathrm { i d e n t i t y } ,
$$

is reasonable and practicable for all vector fields $a : \mathbf { R } ^ { n } \to \mathbf { R } ^ { n }$ . We call such algorithmic revertible approximations, that means $g _ { a } ^ { s }$ always generate coincident forward and backward orbits.

As for the volume-preserving property (3.5), it characterizes the geometric structure —volume-preserving structure—of source-free systems. Our aim here is just to construct difference schemes preserving this structure, which we call volumepreserving schemes, in sense that the algorithmic approximations to the phase flows satisfy (3.5) for the most general source-free systems.

# 10.4 Obstruction to Analytic Methods

We note that for $n = 2$ , source-free vector fields $=$ Hamiltonian fields, and areapreserving maps $=$ symplectic maps, so the problem for area-preserving algorithms has been solved in principle.

But for $n \geq 3$ , the problem is new, since all the conventional methods plus even the symplectic methods are generally not volume-preserving, even for linear source-free systems. As an illustration, see example and Lemma of Feng and Shang[FS95] .

Example 4.1. Solve on $\mathbf { R } ^ { 3 }$

$$
{ \frac { \mathrm { d } x } { \mathrm { d } t } } = a ( x ) = A x , \quad \operatorname { t r } A = 0 ,
$$

by the Euler centered method, we get algorithmic approximation $G ^ { s }$ to $e _ { a } ^ { s } = \exp \left( s A \right)$ with

$$
G ^ { s } = \left( I - \frac { s } { 2 } A \right) ^ { - 1 } \left( I + \frac { s } { 2 } A \right) .
$$

Simple calculations show that in 3-dimensions, if $\operatorname { t r } A = 0$ , then $\operatorname* { d e t } G ^ { s } = 1 \Leftrightarrow$ det $; A = 0$ , which is exceptional. A more general conclusion in linear case is

Lemma 4.2. Let $s l ( n )$ denote the set of all $n \times n$ real matrices with trace equal to zero and $S L ( n )$ the set of all $n \times n$ real matrices with determinant equal to one. Then for any real analytic function $\phi ( z )$ defined in a neighborhood of $z = 0$ in $\mathbf { C }$ satisfying the conditions:

$1 ^ { \circ }$ $\phi ( 0 ) = 1$ ; $2 ^ { \circ }$ $\dot { \phi } ( 0 ) = 1$ . We know that $\phi ( s l ( n ) ) \subset S L ( n )$ for some $n \geq 3$ if and only if $\phi ( z ) = \exp \left( z \right)$ .

Proof. “If part” is a known conclusion, for the “only if part” it suffices to show it for $n = 3$ . For this, we consider matrices of the diagonal form

$$
D ( s , t ) = { \left[ \begin{array} { l l l } { s } & { 0 } & { 0 } \\ { 0 } & { t } & { 0 } \\ { 0 } & { 0 } & { - ( s + t ) } \end{array} \right] } \in s l ( 3 ) , \quad s , t \in \mathbf { R } .
$$

Since $\phi$ is analytic in a neighborhood of the origin in $\mathbf { C }$ , we have

$$
\phi ( D ( s , t ) ) = \left[ \begin{array} { c c c c } { { \phi ( s ) } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \phi ( t ) } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \phi ( - ( s + t ) ) } } \end{array} \right] , \quad s , t \backsim 0 .
$$

By assumption, det $\phi ( D ( s , t ) ) = 1$ , for $s , t \sim 0$ . So

$$
\phi ( s ) \phi ( t ) \phi ( - ( s + t ) ) = 1 , \quad s , t \textgreater 0 ,
$$

together with the condition $\phi ( 0 ) = 1$ , we have

$$
\phi ( s ) \phi ( - s ) = 1 , \quad s \sim 0 .
$$

Multiplying the both sides of Equation (4.5) by $\phi ( s + t )$ and using (4.6), we get

$$
\phi ( s ) \phi ( t ) = \phi ( s + t ) , \quad s , t \sim 0 .
$$

This, together with the conditions $1 ^ { \circ }$ and $2 ^ { \circ }$ of the lemma, implies

$$
\phi ( z ) = \exp { ( z ) } ,
$$

which completes the proof.

Lemma 4.2 says that there are no consistent analytic approximations to the exponential function sending $s l ( n )$ into $S L ( n )$ at the same time other than the exponential itself. This shows that it is impossible to construct volume-preserving algorithms analytically depending on source-free vector fields. Thus we have:

Theorem 4.3 (Feng-Shang). All the conventional methods including the well-known Runge–Kutta methods, linear multistep methods and Euler methods (explicit, implicit and centered) are non-volume-preserving.

The above lemma tell us we cannot construct volume-preserving scheme for all source-free system. But we can split class $s l ( n )$ to subclass and perhaps in subclass, there exists volume-preserving scheme.

In Subsection 10.2.1, we get some condition for centered Euler scheme to be volume-preserving scheme. It is the best elucidation.

Consequently, to construct volume-preserving algorithms for source-free systems, we must break through the conventional model and explore new ways.

# 10.5 Decompositions of Source-Free Vector Fields

In $\mathbf { R } ^ { 2 }$ , every source-free field $\mathbf { \Lambda } \boldsymbol { a } ~ = ~ ( a _ { 1 } , a _ { 2 } ) ^ { \mathrm { T } }$ corresponds to a stream function or 2-dimensional Hamiltonian $\psi$ , unique up to a constant:

$$
a _ { 1 } = - \frac { \partial \psi } { \partial x _ { 2 } } , \quad a _ { 2 } = \frac { \partial \psi } { \partial x _ { 1 } } .
$$

In $\mathbf { R } ^ { 3 }$ , every source-free field $a = ( a _ { 1 } , a _ { 2 } , a _ { 3 } ) ^ { \mathrm { T } }$ corresponds to a vector potential $\boldsymbol { b } = ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) ^ { \mathrm { T } }$ , unique up to a gradient:

$$
\begin{array} { l l } { { a = \operatorname { c u r l } b , } } & { { a _ { 1 } = { \frac { \displaystyle \partial b _ { 3 } } { \displaystyle \partial x _ { 2 } } } - { \frac { \displaystyle \partial b _ { 2 } } { \displaystyle \partial x _ { 3 } } } , } } \\ { { a _ { 2 } = { \frac { \displaystyle \partial b _ { 1 } } { \displaystyle \partial x _ { 3 } } } - { \frac { \displaystyle \partial b _ { 3 } } { \displaystyle \partial x _ { 1 } } } , } } & { { a _ { 3 } = { \frac { \displaystyle \partial b _ { 2 } } { \displaystyle \partial x _ { 1 } } } - { \frac { \displaystyle \partial b _ { 1 } } { \displaystyle \partial x _ { 2 } } } , } } \end{array}
$$

then we get source-free decomposition

$$
a = \left[ \begin{array} { c } { a _ { 1 } } \\ { a _ { 2 } } \\ { a _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { \frac { \partial b _ { 1 } } { \partial x _ { 3 } } } \\ { - \frac { \partial b _ { 1 } } { \partial x _ { 2 } } } \end{array} \right] + \left[ \begin{array} { c } { - \frac { \partial b _ { 2 } } { \partial x _ { 3 } } } \\ { 0 } \\ { \frac { \partial b _ { 2 } } { \partial x _ { 1 } } } \end{array} \right] + \left[ \begin{array} { c } { \frac { \partial b _ { 3 } } { \partial x _ { 2 } } } \\ { - \frac { \partial b _ { 3 } } { \partial x _ { 1 } } } \\ { 0 } \end{array} \right] = a ^ { ( 1 ) } + a ^ { ( 2 ) } + a ^ { ( 3 ) } .
$$

As a generalization of cases $n = 2 , 3$ , on $\mathbf { R } ^ { n }$ , we have[FS95] :

Lemma 5.1. To every source-free field $a = ( a _ { 1 } , a _ { 2 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ , there corresponds $a$ skew symmetric tensor field of order 2, $b = ( b _ { i k } ) _ { 1 \leq i , k \leq n }$ , $b _ { i k } = - b _ { k i }$ , so that

$$
a _ { i } = \sum _ { k = 1 } ^ { n } { \frac { \partial b _ { i k } } { \partial x _ { k } } } , \quad i = 1 , 2 , \cdots , n .
$$

Proof. With the given $\boldsymbol { a } = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ , we define the 1-form on $\mathbf { R } ^ { n }$

$$
\alpha = \sum _ { i = 1 } ^ { n } a _ { i } ( x ) \mathrm { { d } } x _ { i } .
$$

Since $a$ is source-free, we have

$$
\delta \alpha = - \sum _ { i = 1 } ^ { n } { \frac { \partial a _ { i } } { \partial x _ { i } } } = - \mathbf { d i v } a = 0 ,
$$

where $\delta$ is codifferential operator. The above equation means that $\alpha$ is $\delta$ -closed. By Poincare’s lemma, there exists a 2-form, say ´ $\beta$ , so that

$$
\alpha = \delta \beta .
$$

But for the 2-form $\beta$ , there exists a skew symmetric tensor of order 2, $b = ( b _ { i k } ) _ { 1 \leq i . k \leq n }$ , $b _ { i k } = - b _ { k i }$ , so that

$$
\beta = \sum _ { i , k = 1 } ^ { n } b _ { i k } \mathbf { d } x _ { i } \wedge \mathbf { d } x _ { k } .
$$

Take (5.7) codifferential,

$$
\delta \beta = \sum _ { i = 1 } ^ { n } \left( \sum _ { k = 1 } ^ { n } { \frac { \partial b _ { i k } } { \partial x _ { k } } } \right) \operatorname { d } x _ { i } ,
$$

and from Equations (5.5) and (5.6), we get (5.4). The proof is completed.

By (5.4), we can decompose

$$
a = \sum _ { 1 \leq i < k \leq n } a ^ { ( i k ) } , \quad a ^ { ( i k ) } = \left( 0 , \cdots , 0 , \frac { \partial b _ { i k } } { \partial x _ { k } } , 0 , \cdots , - \frac { \partial b _ { i k } } { \partial x _ { i } } , 0 , \cdots , 0 \right) ^ { \mathrm { T } } , \quad i < k .
$$

Every vector field $a ^ { ( i k ) }$ in (5.9) is a 2-dimensional Hamiltonian on the $x _ { i } – x _ { k }$ plane and zero in other dimensions. We call such decompositions essentially Hamiltonian decompositions.

We note that the tensor potential $b = ( b _ { i k } ) _ { 1 \leq i , k \leq n }$ is far from uniquely determined for a given source-free field $\boldsymbol { a } = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ from Equation (5.4). For uniqueness, one may impose normalizing conditions in many different ways. One way is to impose, as done by H. Weyl $\mathrm { i n } ^ { [ \mathrm { W e y 4 0 } ] }$ in 3-dimensional case:

$$
N _ { 0 } : b _ { i k } = 0 , \quad | i - k | \geq 2 ,
$$

this condition is ineffective for $n = 2$ . The non zero components are

$$
\begin{array} { r l } & { b _ { 1 2 } = - b _ { 2 1 } , \quad b _ { 2 3 } = - b _ { 3 2 } , \cdot \cdot \cdot , b _ { n - 1 , n } = - b _ { n , n - 1 } . } \\ & { N _ { k } : b _ { k , k + 1 } | _ { x _ { k + 1 } = 0 } = 0 , \quad 1 < k \le n - 2 } \end{array}
$$

this condition is ineffective for $n = 2$ ,

$$
\begin{array} { r } { N _ { n - 1 } : b _ { n - 1 , n } | _ { x _ { n - 1 } = x _ { n } = 0 } = 0 . } \end{array}
$$

Then, simple calculations show that all $b _ { k , k + 1 }$ are uniquely determined by quadrature

$$
\begin{array} { r l r } {  { b _ { 1 2 } = \int _ { 0 } ^ { x _ { 2 } } a _ { 1 } \mathrm { d } x _ { 2 } , } } \\ {  { b _ { k , k + 1 } = \int _ { 0 } ^ { x _ { k + 1 } } \Big ( a _ { k } + \frac { \partial b _ { k - 1 , k } } { \partial x _ { k - 1 } } \Big ) \mathrm { d } x _ { k + 1 } , } } & { 2 \le k \le n - 2 , } \\ & { } & { b _ { n - 1 , n } = \int _ { 0 } ^ { x _ { n } } \bigg ( a _ { n - 1 } + \frac { \partial b _ { n - 2 , n - 1 } } { \partial x _ { n - 2 } } \bigg ) \mathrm { d } x _ { n } - \int _ { 0 } ^ { x _ { n - 1 } } a _ { n } \big | _ { x _ { n } = 0 } \mathrm { d } x _ { n - 1 } . } \end{array}
$$

So, one gets an essentially Hamiltonian decomposition for $a$ as

$$
a = \sum _ { k = 1 } ^ { n - 1 } a ^ { ( k ) } , \quad a ^ { ( k ) } = \left( 0 , \cdots , 0 , { \frac { \partial b _ { k , k + 1 } } { \partial x _ { k + 1 } } } , - { \frac { \partial b _ { k , k + 1 } } { \partial x _ { k } } } , 0 , \cdots , 0 \right) ^ { \mathrm { T } } ,
$$

or in components,

$$
\left\{ \begin{array} { l l } { \displaystyle a _ { 1 } = \frac { \partial b _ { 1 2 } } { \partial x _ { 2 } } , } \\ { \displaystyle a _ { 2 } = - \frac { \partial b _ { 1 2 } } { \partial x _ { 1 } } + \frac { \partial b _ { 2 3 } } { \partial x _ { 3 } } , } \\ { ~ \vdots } \\ { \displaystyle a _ { n - 1 } = - \frac { \partial b _ { n - 2 , n - 1 } } { \partial x _ { n - 2 } } + \frac { \partial b _ { n - 1 , n } } { \partial x _ { n } } , } \\ { \displaystyle a _ { n } = - \frac { \partial b _ { n - 1 , n } } { \partial x _ { n - 1 } } . } \end{array} \right.
$$

# 10.6 Construction of Volume-Preserving Schemes

In this section, we give a general way to construct volume-preserving difference schemes for source-free systems by means of essentially the Hamiltonian decompositions of source-free vector fields and the symplectic difference schemes for 2- dimensional Hamiltonian systems. With this aim, we first prove:

Lemma 6.1. Let a be a smooth vector field on $\mathbf { R } ^ { n }$ and have decomposition

$$
a = \sum _ { i = 1 } ^ { m } a ^ { ( i ) } ,
$$

with smooth fields $a ^ { ( i ) } \mathbf { : R } ^ { n } \ \to \ \mathbf { R } ^ { n } \ ( i \ = \ 1 , \cdots , m )$ . Suppose that, for each $i \ =$ $1 , \cdots , m , G _ { i } ^ { \tau }$ is an approximation of order $p$ to $e _ { a ( i ) } ^ { \tau }$ , the phase flow of the system

associated to the field $a ^ { ( i ) }$ , in the sense that $\operatorname * { l i m } _ { \tau  0 } \frac { 1 } { \tau ^ { p } } ( G _ { i } ^ { \tau } ( x ) - e _ { a ^ { ( i ) } } ^ { \tau } ( x ) ) = 0$ for all $\boldsymbol { x } \in \mathbf { R } ^ { n }$ with some $p \geq 1$ . Then, we have:

$1 ^ { \circ }$ For any permutation $( i _ { 1 } i _ { 2 } \cdot \cdot \cdot i _ { m } ) o f ( 1 2 \cdot \cdot \cdot m ) _ { }$ , the compositions

$$
\begin{array} { r } { { _ 1 G _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } } : = G _ { i _ { m } } ^ { \tau } \circ \cdot \cdot \cdot \circ G _ { i _ { 2 } } ^ { \tau } \circ G _ { i _ { 1 } } ^ { \tau } , \quad { _ 1 } \widehat { G } _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } : = \left( { _ 1 G _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { - \tau } } \right) ^ { - 1 } } \end{array}
$$

are approximations, of order one, to $e _ { a } ^ { \tau }$ ; and the compositions

$$
\begin{array} { r } { { _ 2 g _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } } : = { _ 1 } \widehat { G } _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \frac \tau 2 } \circ { _ 1 G _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \frac \tau 2 } } , \quad \widehat { g } _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } : = { _ 1 G _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \frac \tau 2 } } \circ { _ 1 } \widehat { G } _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { - \frac \tau 2 } } \end{array}
$$

are revertible approximations, of order 2, to $e _ { a } ^ { \tau }$ ;

$2 ^ { \circ }$ If, for each $i = 1 , 2 , \cdots , m , ($ $G _ { i } ^ { \tau }$ is an approximation, of order 2, to $e _ { a } ^ { \tau }$ , then

$$
{ } _ { 2 } G _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } : = G _ { i _ { m } } ^ { \frac { \tau } { 2 } } \circ \cdot \cdot \cdot \circ G _ { i _ { 2 } } ^ { \frac { \tau } { 2 } } \circ G _ { i _ { 1 } } ^ { \frac { \tau } { 2 } } \circ G _ { i _ { 1 } } ^ { \frac { \tau } { 2 } } \circ G _ { i _ { 2 } } ^ { \frac { \tau } { 2 } } \circ \cdot \cdot \cdot \circ G _ { i _ { m } } ^ { \frac { \tau } { 2 } }
$$

is an approximation, of order 2, to $e _ { a } ^ { \tau }$ ; and it is revertible if each $G _ { i } ^ { \tau }$ is revertible;

$3 ^ { \circ }$ If ${ } _ { 2 } G ^ { \tau }$ is a revertible approximation, of order 2, to $e _ { a } ^ { \tau }$ , then the symmetric composition[QZ92]

$$
_ 4 G ^ { \tau } = { } _ { 2 } G ^ { \alpha _ { 1 } \tau } \circ _ { 2 } G ^ { \beta _ { 1 } \tau } \circ _ { 2 } G ^ { \alpha _ { 1 } \tau }
$$

with

$$
\alpha _ { 1 } = ( 2 - 2 ^ { \frac { 1 } { 3 } } ) ^ { - 1 } , \quad \beta _ { 1 } = 1 - 2 \alpha _ { 1 } < 0 ,
$$

is a revertible approximation, of order 4, to $e _ { a } ^ { \tau }$ ; and generally, the symmetric composition, recursively is defined as follows,

$$
{ } _ { 2 ( l + 1 ) } G ^ { \tau } = { } _ { 2 l } G ^ { \alpha _ { l } \tau } \circ { } _ { 2 l } G ^ { \beta _ { l } \tau } \circ { } _ { 2 l } G ^ { \alpha _ { l } \tau } ,
$$

with

$$
\alpha _ { l } = ( 2 - 2 ^ { \frac { 1 } { ( 2 l + 1 ) } } ) ^ { - 1 } , \quad \beta _ { l } = 1 - 2 \alpha _ { l } < 0 ,
$$

as a revertible approximation, of order $2 ( l + 1 )$ , to $e _ { a } ^ { \tau }$

Proof. It is only needed to prove for $( i _ { 1 } i _ { 2 } \cdot \cdot \cdot i _ { m } ) = ( 1 2 \cdot \cdot \cdot m )$ .

$1 ^ { \circ }$ It is easy to prove that the phase flow $e _ { a } ^ { t }$ has the series expansion

where

$$
e _ { a } ^ { t } ( x ) = x + \sum _ { k = 1 } ^ { \infty } { \frac { t ^ { k } } { k ! } } a ^ { k } ( x ) , \quad x \in \mathbf { R } ^ { n } , \quad t \backsim 0 ,
$$

$$
\begin{array} { l } { { a ^ { 1 } ( x ) = a ( x ) , \quad a ^ { 2 } ( x ) = \displaystyle \frac { \partial a ^ { 1 } ( x ) } { \partial x } a ( x ) , } } \\ { { a ^ { k } ( x ) = \displaystyle \frac { \partial a ^ { k - 1 } ( x ) } { \partial x } a ( x ) , \quad k = 1 , 2 , \cdots . } } \end{array}
$$

The assumption that for $i = 1 , 2 , \cdots , m , G _ { i } ^ { \tau }$ are approximations of order $p \geq 1$ , to $e _ { a ( i ) } ^ { \tau }$ implies that for all $\boldsymbol { x } \in \mathbf { R } ^ { n }$ ,

$$
G _ { i } ^ { \tau } ( x ) = x + \tau a ^ { ( i ) } ( x ) + { \cal O } ( \tau ^ { 2 } ) , \tau \backsim 0 , i = 1 , 2 , \cdots , m .
$$

So, from Taylor expansion, we have that for $\boldsymbol { x } \in \mathbf { R } ^ { n }$ ,

$$
\bigl ( G _ { 2 } ^ { \tau } \circ G _ { 1 } ^ { \tau } \bigr ) ( x ) = G _ { 2 } ^ { \tau } \bigl ( G _ { 1 } ^ { \tau } ( x ) \bigr ) = x + \tau \bigl ( a ^ { ( 1 ) } ( x ) + a ^ { ( 2 ) } ( x ) \bigr ) + O ( \tau ^ { 2 } ) , \quad \tau \sim 0 .
$$

By induction for $m$ , we get

$$
\begin{array} { l } { { _ 1 G _ { ( 1 2 \cdots m ) } ^ { \tau } ( x ) = ( G _ { m } ^ { \tau } \circ \cdots \circ G _ { 2 } ^ { \tau } \circ G _ { 1 } ^ { \tau } ) ( x ) } } \\ { { \ = x + \tau ( a ^ { ( 1 ) } ( x ) + a ^ { ( 2 ) } ( x ) + \cdots + a ^ { ( m ) } ( x ) ) + O ( \tau ^ { 2 } ) } } \\ { { \ = x + \tau a ( x ) + O ( \tau ^ { 2 } ) , \quad \tau \smile 0 . } } \end{array}
$$

This implies that $1 ^ { G ^ { \tau } } { } _ { ( 1 2 \cdots m ) }$ is an approximation, of order one, to $e _ { a } ^ { \tau }$ , which provides the proof needed.

$\mathrm { I n } ^ { \left[ \mathrm { Q Z 9 2 } \right] }$ that ${ _ { 2 } g _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau } }$ and ${ } _ { 2 } \widehat { g } _ { i _ { 1 } i _ { 2 } \cdots i _ { m } } ^ { \tau }$ , defined by Equation (6.2), are revertible m approximations, of order 2, to $e _ { a } ^ { \tau }$  m, the conclusion of the Lemma 6.1 is proved.

$2 ^ { \circ }$ By assumption, we have that for $\boldsymbol { x } \in \mathbf { R } ^ { n }$ and $\tau \sim 0$

$$
G _ { i } ^ { \tau } ( x ) = x + \tau a ^ { ( i ) } ( x ) + \frac { 1 } { 2 } \tau ^ { 2 } \bigl ( a ^ { ( i ) } \bigr ) ^ { 2 } ( x ) + { \cal O } ( \tau ^ { 3 } ) , \quad i = 1 , 2 , \cdot \cdot \cdot , m .
$$

Taylor expansion of the right hand side of Equation (6.4) with $\left( i _ { 1 } i _ { 2 } \cdot \cdot \cdot i _ { m } \right) \ =$ $\left( 1 2 \cdots m \right)$ yields

$$
{ } _ { 2 } G _ { ( 1 2 \cdots m ) } ^ { \tau } ( x ) = x + \tau \sum _ { i = 1 } ^ { m } a ^ { ( i ) } ( x ) + \frac { 1 } { 2 } \tau ^ { 2 } \left( \sum _ { i , j = 1 } ^ { m } a ^ { ( i ) } a ^ { ( j ) } \right) ( x ) + { \cal O } ( \tau ^ { 3 } ) , \quad \tau \sim 0 .
$$

Here, we have used the convention

$$
( a b ) ( x ) = ( a _ { * } b ) ( x ) = a _ { * } ( x ) b ( x ) , \quad a _ { * } ( x ) = \frac { \partial a ( x ) } { \partial x } ,
$$

for $a , b : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ . However, we have

$$
a ^ { 2 } = a _ { * } a = \left( \sum _ { i = 1 } ^ { m } a ^ { ( i ) } \right) _ { * } \left( \sum _ { j = 1 } ^ { m } a ^ { ( j ) } \right) = \sum _ { i , j = 1 } ^ { m } ( a ^ { ( i ) } ) _ { * } a ^ { ( j ) } = \sum _ { i , j = 1 } ^ { m } a ^ { ( i ) } a ^ { ( j ) } .
$$

So

$$
e _ { a } ^ { \tau } ( x ) = x + \tau a ( x ) + \frac { 1 } { 2 } \tau ^ { 2 } a ^ { 2 } ( x ) + { \cal O } ( \tau ^ { 3 } ) = { } _ { 2 } G _ { ( 1 2 \cdots m ) } ^ { \tau } ( x ) + { \cal O } ( \tau ^ { 3 } ) , \quad \tau \sim 0 .
$$

This shows that 2Gτ(12 m) i s an approximation, of order 2, to $e _ { a } ^ { \tau }$ . By direct verification, this is revertible if each component $G _ { i } ^ { \tau }$ is revertible.

The conclusion $3 ^ { \circ }$ directly follows from Qin-Zhu’s paper[QZ93] .

Lemma 6.2. Given system

$$
\begin{array} { r } { \dot { x } = a ^ { ( k ) } ( x ) , \quad a ^ { ( k ) } ( x ) = \Big ( 0 , \cdots , 0 , \frac { \partial b _ { k , k + 1 } } { \partial x _ { k + 1 } } ( x ) , - \frac { \partial b _ { k , k + 1 } } { \partial x _ { k } } ( x ) , 0 , \cdots , 0 \Big ) ^ { \mathrm { T } } , } \end{array}
$$

with $x = ( x _ { 1 } , \cdot \cdot \cdot , x _ { k } , x _ { k + 1 } , \cdot \cdot \cdot , x _ { n } ) ^ { \mathrm { T } }$ and smooth function $b _ { k , k + 1 } : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ . Then any symplectic difference scheme, of order $p \geq 1$ , of the Hamiltonian system on the $x _ { k } – x _ { k + 1 }$ plane

$$
\dot { x } _ { k } = \frac { \partial b _ { k , k + 1 } } { \partial x _ { k + 1 } } , \quad \dot { x } _ { k + 1 } = - \frac { \partial b _ { k , k + 1 } } { \partial x _ { k } } ,
$$

with $x _ { j } , j ~ \neq ~ k , k + 1$ as parameters naturally gives a volume-preserving difference scheme, of order $p$ , of the source-free system (6.18) on the $n$ -dimensional $( x _ { 1 } , \cdots , x _ { n } ) ^ { \mathrm { T } }$ -space by simply freezing the coordinates $x _ { j } , j \neq k , k + 1$ and transforming $x _ { k }$ and $x _ { k + 1 }$ according to the symplectic difference scheme for (6.19) in which $x _ { j } , j \neq k , k + 1$ are considered as frozen parameters.

Proof. It is obvious that the so-constructed difference scheme is of order $p$ . As to the volume-preserving property, we easily prove that it is true by direct calculation of the determinant of the Jacobian of the step-transition map of the scheme, with the notice of the fact that the determinant of the Jacobian of a symplectic map is equal to one.

Now, we construct volume-preserving difference schemes for source-free systems. Let $a = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ be a source-free field. As was proved in Section 10.5, we have essentially Hamiltonian decomposition (5.17) for $a$ with the functions $b _ { k , k + 1 }$ given from $a$ by (5.14) – (5.16). We denote by $S _ { k } ^ { \tau }$ the step transition map of a volume-preserving difference scheme with step size $\tau$ , as constructed in Lemma 6.2, associated to the vector field $a ^ { ( k ) } = { \bigg ( } 0 , \cdots , 0 , { \frac { \partial b _ { k , k + 1 } } { \partial x _ { k + 1 } } } , - { \frac { \partial b _ { k , k + 1 } } { \partial x _ { k } } } , 0 , \cdots , 0 { \bigg ) } ^ { \mathrm { T } }$ T for $k = 1 , 2 , \cdots$ . -

Then by Lemma 6.1, we have:

Theorem 6.3. [FW94] $1 ^ { \circ }$ A simple composition of the $n - 1$ components $S _ { 1 } ^ { \tau } , S _ { 2 } ^ { \tau } , \cdots$ , $S _ { n - 1 } ^ { \tau }$ , say

$$
{ } _ { 1 } G ^ { \tau } : = S _ { n - 1 } ^ { \tau } \circ \cdot \cdot \cdot \circ S _ { 2 } ^ { \tau } \circ S _ { 1 } ^ { \tau }
$$

is a volume-preserving algorithmic approximation, of order one, to $e _ { a } ^ { \tau }$ ; and

$$
{ } _ { 2 } g ^ { \tau } : = { } _ { 1 } \widehat G ^ { \frac { \tau } { 2 } } \circ { } _ { 1 } G ^ { \frac { \tau } { 2 } } , \quad { } _ { 2 } \widehat g ^ { \tau } = { } _ { 1 } G ^ { \frac { \tau } { 2 } } \circ { } _ { 1 } \widehat G ^ { \frac { \tau } { 2 } }
$$

are revertible volume-preserving algorithmic approximations, of order 2.

$2 ^ { \circ }$ If each $S _ { k } ^ { \tau }$ is an approximation, of order 2, to $e _ { a ^ { ( k ) } } ^ { \tau }$ , then the symmetric composition

$$
{ } _ { 2 } G ^ { \tau } = S _ { n - 1 } ^ { \frac { \tau } { 2 } } \circ \dots \circ S _ { 2 } ^ { \frac { \tau } { 2 } } \circ S _ { 1 } ^ { \frac { \tau } { 2 } } \circ S _ { 1 } ^ { \frac { \tau } { 2 } } \circ S _ { 2 } ^ { \frac { \tau } { 2 } } \circ \dots \circ S _ { n - 1 } ^ { \frac { \tau } { 2 } }
$$

is a volume-preserving approximation, of order 2, to $e _ { a } ^ { \tau }$ .

$3 ^ { \circ }$ If each $S _ { k } ^ { \tau }$ is revertible, then the so-constructed ${ } _ { 2 } G ^ { \tau }$ is revertible too.

$4 ^ { \circ }$ From the above constructed revertible algorithmic approximation $2 \boldsymbol { g } ^ { \tau }$ or ${ } _ { 2 } G ^ { \tau }$ , we can further recursively construct revertible approximations, of all even orders, to $e _ { a } ^ { \tau }$ according to the process of Lemma 6.1.

Remark 6.4. If $a$ has essentially Hamiltonian decompositions other than (5.17) and (5.14) – (5.16), then one can construct volume-preserving difference schemes corresponding to these decompositions in a similar way to the above.

# 10.7 Some Special Discussions for Separable Source-Free Systems

For a source-free field $\boldsymbol { a } = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ with essentially Hamiltonian decomposition (5.17), we take $S _ { k } ^ { \tau } : x = ( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) ^ { \mathrm { T } }  { \widehat { x } } = ( { \widehat { x } } _ { 1 } , \cdot \cdot \cdot , { \widehat { x } } _ { n } ) ^ { \mathrm { T } }$ as determined from the following:

$$
\left\{ \begin{array} { l l } { \widehat x _ { j } = x _ { j } , \quad j \neq k , k + 1 , } \\ { } \\ { \widehat x _ { k } = x _ { k } + \tau \frac { \partial b _ { k , k + 1 } } { \partial x _ { k + 1 } } ( x _ { 1 } , \cdots , x _ { k - 1 } , \widehat x _ { k } , x _ { k + 1 } , \cdots , x _ { n } ) , } \\ { } \\ { } \\ { \widehat x _ { k + 1 } = x _ { k + 1 } - \tau \frac { \partial b _ { k , k + 1 } } { \partial x _ { k } } ( x _ { 1 } , \cdots , x _ { k - 1 } , \widehat x _ { k } , x _ { k + 1 } , \cdots , x _ { n } ) . } \end{array} \right.
$$

Then, simple calculations show that ${ } _ { 1 } G ^ { \tau } = S _ { n - 1 } ^ { \tau } \circ \cdot \cdot \cdot \circ S _ { 2 } ^ { \tau } \circ S _ { 1 } ^ { \tau }$ from

$$
\left\{ \begin{array} { l l } { \displaystyle \hat { x } _ { 1 } = x _ { 1 } + \tau a _ { 1 } \big ( \hat { x } _ { 1 } , x _ { 2 } , \cdot \cdot , x _ { n } \big ) , } \\ { \displaystyle \hat { x } _ { j } = x _ { j } + \tau a _ { j } \big ( \hat { x } _ { 1 } , \cdot \cdot , \hat { x } _ { j } , x _ { j + 1 } , \cdot \cdot , x _ { n } \big ) } \\ { \displaystyle \qquad + \tau \int _ { x _ { j } } ^ { \hat { x } _ { j } } \sum _ { l = 1 } ^ { j - 1 } \frac { \partial a _ { l } } { \partial x _ { l } } \big ( \hat { x } _ { 1 } , \cdot \cdot , \hat { x } _ { j - 1 } , t , x _ { j + 1 } , \cdot \cdot , x _ { n } \big ) \mathrm { d } t , \quad j = 2 , \cdot \cdot \cdot , n - 1 , } \\ { \displaystyle \qquad \hat { x } _ { n } = x _ { n } + \tau a _ { n } \big ( \hat { x } _ { 1 } , \cdot \cdot \cdot , \hat { x } _ { n - 1 } , x _ { n } \big ) , } \end{array} \right.
$$

and $_ 1 \widehat { G } ^ { \tau } = \left( _ { 1 } G ^ { - \tau } \right) ^ { - 1 }$ is given from

$$
\left\{ \begin{array} { l l } { \widehat x _ { n } = x _ { n } + \tau a _ { n } \big ( x _ { 1 } , \cdot \cdot \cdot , x _ { n - 1 } , \widehat x _ { n } \big ) , } \\ { \widehat x _ { j } = x _ { j } + \tau a _ { j } \big ( x _ { 1 } , \cdot \cdot \cdot , x _ { j } , \widehat x _ { j + 1 } , \cdot \cdot \cdot , \widehat x _ { n } \big ) } \\ { \qquad - \tau \displaystyle \int _ { x _ { j } } ^ { \widehat x _ { j } } \displaystyle \sum _ { l = 1 } ^ { j - 1 } \frac { \partial a _ { l } } { \partial x _ { l } } \big ( x _ { 1 } , \cdot \cdot \cdot , x _ { j - 1 } , t , \widehat x _ { j + 1 } , \cdot \cdot \cdot , \widehat x _ { n } \big ) \mathrm { d } t , \quad j = 2 , \cdot \cdot \cdot , n - 1 , } \\ { \widehat x _ { 1 } = x _ { 1 } + \tau a _ { 1 } \big ( x _ { 1 } , \widehat x _ { 2 } , \cdot \cdot \cdot , \widehat x _ { n } \big ) . } \end{array} \right.
$$

(7.2) and (7.3) are both volume-preserving difference scheme, of order 1, of the source-free system associated to the field $a$ , with the step-transition maps $_ 1 G ^ { \tau }$ and ${ } _ { 1 } \widehat { G } ^ { \tau }$ . They can be composed into revertible volume-preserving schemes of order 2, say, 2-stage scheme with step transition map ${ } _ { 2 } \widehat g ^ { \tau } = { } _ { 1 } \hat { G } ^ { \frac { \tau } { 2 } } \circ _ { 1 } \widehat G ^ { \frac { \tau } { 2 } } : \ d x = ( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) ^ { \mathrm T } $ $\widehat { \boldsymbol { x } } = ( \widehat { x } _ { 1 } , \cdots , \widehat { x } _ { n } ) ^ { \mathrm { T } }$ as follows,

$$
\{ \begin{array} { l l } { \frac { \hat { x } _ { 1 } ^ { \prime } } { x _ { 2 } ^ { \prime } } = x _ { 1 } + \frac { \hat { y } _ { 2 } } { 2 } \varepsilon _ { \mathrm { a f f } } ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 3 } , x _ { 4 } ^ { \prime } ) , } \\ { \frac { \hat { x } _ { 2 } ^ { \prime } } { x _ { 3 } ^ { \prime } } = x _ { 1 } + \frac { \hat { y } _ { 2 } } { 2 } \varepsilon _ { \mathrm { a f f } } ( x _ { 1 } , \dots , x _ { 3 } , x _ { 4 } ^ { \prime } , x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } ) , } \\ { ~ \frac { \hat { x } _ { 3 } ^ { \prime } } { x _ { 4 } ^ { \prime } } = x _ { 2 } + \frac { \hat { y } _ { 3 } } { 2 } \varepsilon _ { \mathrm { a f f } } ( x _ { 1 } , \dots , x _ { 3 } , x _ { 4 } ^ { \prime } , x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } ) , } \\ { ~ - \frac { \hat { y } _ { 4 } } { x _ { 3 } ^ { \prime } } \int _ { x _ { 2 } } ^ { x _ { 3 } } \frac { \hat { y } _ { 4 } } { \hat { y } _ { 3 } ^ { \prime } } ( x _ { 1 } , \dots , x _ { 3 } , x _ { 4 } ^ { \prime } , x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } ) , } \\ { ~ \frac { \hat { x } _ { 4 } ^ { \prime } } { x _ { 5 } ^ { \prime } } = x _ { 1 } + \frac { \hat { y } _ { 2 } } { x _ { 2 } ^ { \prime } } \varepsilon _ { \mathrm { a f f } } ( x _ { 1 } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } , x _ { 4 } ^ { \prime } ) , } \\ { \frac { \hat { x } _ { 5 } } { x _ { 1 } } = x _ { 3 } + \frac { \hat { y } _ { 2 } } { x _ { 2 } ^ { \prime } } \varepsilon _ { \mathrm { a f f } } ( x _ { 1 } , x _ { 3 } ^ { \prime } , x _ { 3 } ^ { \prime } , x _ { 4 } ^ { \prime } ) , } \\  \frac { \hat { x } _ { 5 } } { x _ { 2 } ^ { \prime } } + \frac  \end{array}
$$

Either (7.2) or (7.3) contains $n - 1$ implicit equations generally. But for fields $a$ with some specific properties, it will turn into explicit. For example,

$$
{ \frac { \partial a _ { i } } { \partial x _ { i } } } = 0 , \quad i = 1 , \cdots , n
$$

(i.e., $a _ { i }$ does not depend on $x _ { i }$ ), then (7.2) turns into explicit[QZ93]

$$
\left\{ \begin{array} { l l } { \widehat x _ { 1 } = x _ { 1 } + \tau a _ { 1 } ( x _ { 2 } , \cdots , x _ { n } ) , } \\ { \widehat x _ { j } = x _ { j } + \tau a _ { j } ( \widehat x _ { 1 } , \cdots , \widehat x _ { j - 1 } , x _ { j + 1 } , \cdots , x _ { n } ) , \quad j = 2 , \cdots , n - 1 , } \\ { \widehat x _ { n } = x _ { n } + \tau a _ { n } ( \widehat x _ { 1 } , \cdots , \widehat x _ { n - 1 } , x _ { n } ) . } \end{array} \right.
$$

For details, see the Section 10.2.

We note that, for $\boldsymbol { a } = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ ,

$$
a = \sum _ { k = 1 } ^ { n } a ^ { \{ k \} } , \quad a ^ { \{ k \} } = ( 0 , \cdots , 0 , a _ { k } , 0 , \cdots , 0 ) ^ { \mathrm { T } } , \quad k = 1 , 2 , \cdots , n .
$$

It is easy to verify that if $a = ( a _ { 1 } , \cdots , a _ { n } ) ^ { \mathrm { T } }$ satisfies the condition (7.5), then the scheme (7.6) is just the result of composing the Euler explicit schemes of the systems associated to the fields $a ^ { \{ k \} } ( k = 1 , \bar { \cdot } \cdot , n )$ , i.e., we have

$$
{ } _ { 1 } G ^ { \tau } = E _ { a ^ { \{ n \} } } ^ { \tau } \circ \cdot \cdot \cdot \circ E _ { a ^ { \{ 2 \} } } ^ { \tau } \circ E _ { a ^ { \{ 1 \} } } ^ { \tau } ,
$$

where

$$
E _ { a \{ k \} } ^ { \tau } = I + \tau a ^ { \{ k \} } , \quad k = 1 , 2 , \cdots , n , \quad I = \mathrm { i d e n t i t y } .
$$

In fact, $E _ { a ^ { \{ k \} } } ^ { \tau }$ are the phase flows $e _ { a \{ k \} } ^ { \tau }$ , since a{k} ∗ a{k} = 0 for k = 1, 2, · · · , n, k kwhich is implied by the condition (7.5). According to Theorem 6.3, we then get a 2nd order explicit revertible volume-preserving scheme, with step transition map

$$
\begin{array} { l } { { _ 2 G ^ { \tau } = E _ { a ^ { \{ \tau \} } } ^ { \frac { \tau } { 2 } } \circ \cdot \cdot \cdot \circ E _ { a ^ { \{ 2 \} } } ^ { \frac { \tau } { 2 } } \circ E _ { a ^ { \{ 1 \} } } ^ { \frac { \tau } { 2 } } \circ \widehat { E } _ { a ^ { \{ 1 \} } } ^ { \frac { \tau } { 2 } } \circ \widehat { E } _ { a ^ { \{ 2 \} } } ^ { \frac { \tau } { 2 } } \circ \cdot \cdot \cdot \circ \widehat { E } _ { a ^ { \{ n \} } } ^ { \frac { \tau } { 2 } } } } \\ { { = \ _ { 1 } G ^ { \frac { \tau } { 2 } } \circ _ { 1 } \widehat { G } ^ { \frac { \tau } { 2 } } = _ { 2 } \widehat { g } ^ { \tau } . } } \end{array}
$$

# 10.8 Construction of Volume-Preserving Scheme via Generating Function

Not only symplectic scheme can be constructed via generating function, but volume-Preserving scheme is also constructed via generating function. A. Thyagaraja and F.A. Haas[TH85,Sco91] give an important type generating function for volume-preserving mapping in 3-dimensions. It is however, not complete both in generality and in systematization. The complete results are given by Z.J. Shang $[ \mathrm { S h a 9 4 a } , \mathrm { S h a 9 4 b } ]$ .

# 10.8.1 Fundamental Theorem

Theorem 8.1. Let $\alpha = { \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } \in G L ( 2 n ) , \ \alpha ^ { - 1 } = { \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] } .$ Cα Dα . Assume that $g : \mathbf { R } ^ { n }  \mathbf { R } ^ { n } , { \widehat { z } } = g ( z )$ is a differentiable mapping given, in some point $z _ { 0 } \in$ $\mathbf { R } ^ { n }$ , satisfying transversality condition

$$
\left| C _ { \alpha } \frac { \partial g ( z ) } { \partial z } + D _ { \alpha } \right| \neq 0 .
$$

Then, in $\mathbf { R } ^ { n }$ neighborhood W of point $w _ { 0 } = C _ { \alpha } g ( z _ { 0 } ) + D _ { \alpha } z _ { 0 }$ exists a unique differentiable mapping $f ( w ) = f _ { \alpha , g } = ( f _ { 1 } ( w ) , f _ { 2 } ( w ) , \cdot \cdot \cdot , f _ { n } ( w ) )$ : $\mathbf { W } ^ { n } \to \mathbf { R } ^ { n }$ such that ${ \widehat { z } } = g ( z )$ satisfying condition

$$
\left| \frac { \partial f ( w ) } { \partial w } C _ { \alpha } - A _ { \alpha } \right| = \left| B _ { \alpha } - \frac { \partial f ( w ) } { \partial w } D _ { \alpha } \right| \neq 0 ,
$$

such that, mapping ${ \widehat { z } } = g ( z )$ can reconstruct in a neighborhood $V$ of the point $z = z _ { 0 }$ from $\widehat { w } = f ( w )$ by the relation

$$
A _ { \alpha } \widehat { z } + B _ { \alpha } z = f ( C _ { \alpha } \widehat { z } + D _ { \alpha } z ) .
$$

Conversely, for any differential mapping $f ( w ) = ( f _ { 1 } ( w ) , \cdot \cdot \cdot , f _ { n } ( w ) ) : \mathbf { R } ^ { n } $ $\mathbf { R } ^ { n }$ , satisfying condition (8.2) at the point $w _ { 0 } \in \mathbf { R } ^ { n }$ , we give a unique differential mapping in some neighborhood $V$ of the point $z _ { 0 } = C ^ { \alpha } f ( w ) { + } D ^ { \alpha } w _ { 0 }$ (8.3). Moreover, the transversality condition (8.1) is satisfied for the mapping $g$ at the point $z _ { 0 } =$ $C ^ { \alpha } f ( w ) + D ^ { \alpha } w _ { 0 }$ .

Remark 8.2. Generally speaking, a volume-preserving mapping $f$ is uniquely determined by the matrix $\alpha \in G L ( 2 n )$ and mapping $g$ as above by relation (8.3) determined by mapping $f = f _ { \alpha , g }$ . We called $f = f _ { \alpha , g }$ as generating mapping dependent on $\alpha , g$ .

Remark 8.3. We only consider some typical types generating mapping

$$
\alpha _ { ( s , s ) } = \left[ \begin{array} { c c c } { I _ { n } - E _ { s s } } & { } & { E _ { s s } } \\ { E _ { s s } } & { } & { I _ { n } - E _ { s s } } \end{array} \right] , \quad 1 \leq s \leq n ,
$$

where $E _ { s s }$ denotes the $n \times n$ matrix, of which only the entry at the $s$ -th row and the $s$ -th column is equal to 1, and all other entries are 0. In this case, (8.2) and (8.3) have much more simple forms. For example, for $\alpha = \alpha _ { ( 1 , 1 ) }$ , (8.2) turns into

$$
\frac { \partial f _ { 1 } } { \partial w _ { 1 } } = \left| \frac { \partial ( f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) } { \partial ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) } \right| \neq 0 ,
$$

and (8.3) turns into

$$
\begin{array} { c } { z _ { 1 } = f _ { 1 } ( \widehat { z _ { 1 } } , z _ { 2 } , \cdots , z _ { n } ) , } \\ { \ } \\ { \widehat { z _ { 2 } } = f _ { 2 } ( \widehat { z _ { 1 } } , z _ { 2 } , \cdots , z _ { n } ) , } \\ { \ } \\ { \ \cdots \ } \\ { \widehat { z _ { n } } = f _ { n } ( \widehat { z _ { 1 } } , z _ { 2 } , \cdots , z _ { n } ) . } \end{array}
$$

The same situation also applies for $\alpha _ { ( s , s ) }$

Remark 8.4. For such a matrix $\alpha _ { ( 1 , 1 ) }$ , generating mapping $f ( w )$ of type $\alpha _ { ( 1 , 1 ) }$ , there are $n$ component $f ( w ) = ( f _ { 1 } ( w ) , f _ { 2 } ( w ) , \cdot \cdot \cdot , f _ { n } ( w ) )$ , in which $n - 1$ component $f _ { 2 } ( w ) , \cdot \cdot \cdot , f _ { n } ( w )$ is linear independent, satisfying condition

$$
\left| \frac { \partial ( f _ { 2 } , \cdots , f _ { n } ) } { \partial ( w _ { 2 } , \cdots , w _ { n } ) } \right| \neq 0 ,
$$

then we can express the first component $f _ { 1 }$ of $f$ by other $n - 1$ component

$$
f _ { 1 } ( w _ { 1 } , w _ { 2 } , \cdots , w _ { n } ) = C ( w _ { 2 } , \cdots , w _ { n } ) + \int _ { w _ { 1 , 0 } } ^ { w _ { 1 } } \left| \frac { \partial ( f _ { 2 } , \cdots , f _ { n } ) } { \partial ( w _ { 2 } , \cdots , w _ { n } ) } \right| ( \xi , w _ { 2 } , \cdots , w _ { n } ) \mathrm { d } \xi ,
$$

where $C$ is scalar function dependent $n - 1$ variable.

Theo $\alpha = \Bigl [ \begin{array} { l l } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \Bigr ] \in G L ( 2 n ) a n d \alpha ^ { - 1 } = \Bigl [ \begin{array} { l l } { { A ^ { \alpha } } } & { { B ^ { \alpha } } } \\ { { C ^ { \alpha } } } & { { D ^ { \alpha } } } \end{array} \Bigr ] .$ . Sup $| C _ { \alpha } + D _ { \alpha } | \neq 0$ $M _ { 0 } \in G L ( 2 n )$ $t$ $\alpha$ of the diffeomorphism $g _ { \alpha } ^ { t } ( M _ { 0 } z )$ generating mapping, $f ( w , t ) = f _ { \alpha , a } ( w , t )$ , its phase flow $g _ { \alpha } ^ { t }$ satisfying

$$
\dot { z } = \boldsymbol { a } ( z ) , \quad \boldsymbol { a } ( z ) = ( a _ { 1 } ( z ) , \cdot \cdot \cdot , a _ { n } ( z ) ) ^ { \mathrm { T } } , \quad z = ( z _ { 1 } , \cdot \cdot \cdot , z _ { n } ) ^ { \mathrm { T } } ,
$$

such that

$$
\frac { \partial f } { \partial t } = \left( A _ { \alpha } - \frac { \partial f } { \partial \omega } C _ { \alpha } \right) { a } ( A ^ { \alpha } f + B ^ { \alpha } \omega ) ,
$$

$$
f ( w , 0 ) = ( A _ { \alpha } + B _ { \alpha } ) ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } \omega .
$$

We call (8.9) a Hamilton–Jacobi equation. The proofs of Theorems 8.1 and 8.2 can found in [Sha94b] .

Remark 8.6. If $\alpha = \alpha _ { ( 1 , 1 ) }$ , then relations (8.9) and (8.10) turn into

$$
\begin{array} { l } { \displaystyle \frac { \partial f _ { 1 } } { \partial t } = - a _ { 1 } ( w _ { 1 } , f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) \frac { \partial f _ { 1 } } { \partial w _ { 1 } } , } \\ { \displaystyle \frac { \partial f _ { k } } { \partial t } = a _ { k } ( w _ { 1 } , f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) - a _ { 1 } ( w _ { 1 } , f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) \frac { \partial f _ { k } } { \partial w _ { 1 } } , \quad k = 2 , \cdot \cdot \cdot , n , } \\ { f _ { k } ( w _ { 1 } , \cdot \cdot \cdot , w _ { n } , 0 ) = w _ { k } , \quad k = 1 , 2 , \cdot \cdot \cdot , n . } \end{array}
$$

When $a$ is source-free system, i.e.,

$$
\operatorname { d i v } a ( z ) = \sum _ { k = 1 } ^ { n } { \frac { \partial a _ { k } } { \partial z _ { k } } } ( z ) = 0 , \quad z \in \mathbf { R } ^ { n } ,
$$

then $g _ { \alpha } ^ { t }$ is volume-preserving, we get

$$
\frac { \partial f _ { 1 } } { \partial w _ { 1 } } ( w , t ) = \left| \frac { \partial ( f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) } { \partial ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) } \right| ( w , t ) .
$$

From (8.11), (8.13), and (8.15), we get

$$
f _ { 1 } ( w , t ) = w _ { 1 } - \int _ { 0 } ^ { t } a _ { 1 } ( w _ { 1 } , f _ { 2 } ( w , \tau ) , \cdot \cdot \cdot , f _ { n } ( w , \tau _ { 1 } ) ) \left| \frac { \partial ( f _ { 2 } , \cdot \cdot \cdot , f _ { n } ) } { \partial ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) } \right| ( w , \tau ) \mathrm { d } \tau .
$$

$f _ { 2 } , \cdots , f _ { n }$ is independently determined by (8.12) and (8.13) (for $k = 2 , \cdots , n )$ we call these as generating function type $\alpha _ { ( 1 , 1 ) }$ for source-free system (8.8).

Theorem 8.7. Suppose vector field a is analytical function of $z$ , then $f ( w , t ) ~ =$ $f _ { \alpha , a } ( w , t )$ , is solution of Cauchy problem (8.9) and (8.10), it is expressible as a convergent power series in $t$ for sufficiently small $| t |$ , with the recursively determined coefficients

$$
\begin{array} { l } { \displaystyle f ( w , t ) = \sum _ { k = 0 } ^ { \infty } f ^ { ( k ) } ( w ) t ^ { k } , } \\ { \displaystyle f ^ { 0 } ( w ) = N _ { 0 } w , \quad N _ { 0 } = ( A _ { \alpha } + B _ { \alpha } ) ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } , } \\ { \displaystyle f ^ { 1 } ( w ) = L _ { 0 } a ( E _ { 0 } w ) , \quad E _ { 0 } = ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } , \quad L _ { 0 } = A _ { \alpha } - N _ { 0 } C _ { \alpha } , } \end{array}
$$

for $k \geq 1$ , we have

$$
\begin{array} { r l } { f ^ { ( k + 1 ) } ( w ) } & { = - \displaystyle \frac { 1 } { k + 1 } \frac { \partial f ^ { ( k ) } ( w ) } { \partial w } C _ { \alpha } \boldsymbol { a } ( E _ { 0 } w ) - \frac { 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \sum _ { j = 1 } ^ { m } \sum _ { \boldsymbol { i } _ { 1 } + \cdots + \boldsymbol { i } _ { j } = m } ^ { i _ { p } \ge 1 } \frac { 1 } { j ! } } \\ & { \cdot \frac { \partial f ^ { ( k - m ) } ( w ) } { \partial w } C _ { \alpha } D _ { \alpha , E _ { 0 } w } ^ { j } ( A ^ { \alpha } f ^ { ( i _ { 1 } ) } ( \omega ) , \cdots , A ^ { \alpha } f ^ { ( i _ { j } ) } ( w ) ) } \\ & { + \frac { 1 } { k + 1 } \sum _ { \operatorname* { m } = 1 } ^ { k } \displaystyle \sum _ { i _ { 1 } + \cdots + i _ { m } = k } \frac { 1 } { m ! } A _ { \alpha } D _ { \alpha , E _ { 0 } w } ^ { m } ( A ^ { \alpha } f ^ { ( i _ { 1 } ) } ( \omega ) , \cdots , A ^ { \alpha } f ^ { ( i _ { m } ) } ( w ) ) , } \end{array}
$$

where for $\xi ^ { ( k ) } = ( \xi _ { 1 } ^ { ( k ) } , \cdot \cdot \cdot , \xi _ { n } ^ { ( k ) } ) ^ { \mathrm { T } } \in \mathbf { R } ^ { n }$ = (ξ (k)1 , · , ξ(k) n )T ∈ Rn (k = 1, 2, · · · , m), we get

$$
D _ { \alpha , w } ^ { m } ( \xi ^ { ( 1 ) } , \cdot \cdot , \xi ^ { ( m ) } ) = \left[ \begin{array} { c } { \displaystyle \sum _ { \alpha _ { 1 } , \cdots , \alpha _ { m } = 1 } ^ { n } \frac { \partial ^ { m } a _ { 1 } ( w ) } { \partial z _ { \alpha _ { 1 } } \cdot \cdot \cdot \partial z _ { \alpha _ { m } } } \xi _ { \alpha _ { 1 } } ^ { 1 } \cdot \cdot \cdot \xi _ { \alpha _ { m } } ^ { m } } \\ { \vdots } \\ { \displaystyle \sum _ { \alpha _ { 1 } , \cdots , \alpha _ { m } = 1 } ^ { n } \frac { \partial ^ { m } a _ { n } ( w ) } { \partial z _ { \alpha _ { 1 } } \cdot \cdot \cdot \partial z _ { \alpha _ { m } } } \xi _ { \alpha _ { 1 } } ^ { 1 } \cdot \cdot \cdot \xi _ { \alpha _ { m } } ^ { m } } \\ { \displaystyle \alpha _ { 1 } , \cdots , \alpha _ { m } = 1 } \end{array} \right] .
$$

Proof. Under the above proposition, if generating function $f ( w , t ) = f _ { \alpha , a } ( w , t )$ is dependent analytically on $w$ and $t$ in some neighborhood $\mathbf { R } ^ { n }$ for sufficient small $t$ then it can be expressed as a power series

$$
f ( w , t ) = \sum _ { k = 0 } ^ { \infty } f ^ { ( k ) } ( w ) t ^ { k } .
$$

Differentiating it with respect to $w$ and $t$ , we get

$$
\begin{array} { r l } & { \frac { \partial f } { \partial w } ( w , t ) = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { \partial f ^ { ( k ) } ( w ) } { \partial w } t ^ { k } , } \\ & { \frac { \partial f } { \partial t } ( w , t ) = \displaystyle \sum _ { k = 0 } ^ { \infty } ( k + 1 ) f ^ { ( k + 1 ) } ( w ) t ^ { k } . } \end{array}
$$

By (8.10),

$$
f ^ { ( 0 ) } ( w ) = f ( w , 0 ) = N _ { 0 } w .
$$

This is (8.19). Denote $E _ { 0 } = A ^ { \alpha } N _ { 0 } + B ^ { \alpha } = ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 }$ , then

$$
A ^ { \alpha } f ( w , t ) + B ^ { \alpha } w = E _ { 0 } w + \sum _ { k = 1 } ^ { \infty } A ^ { \alpha } f ^ { ( k ) } ( w ) t ^ { k } .
$$

Expanding $a ( z )$ at $z = E _ { 0 } w$ , we get

$$
\begin{array} { l } { \displaystyle \alpha ( A ^ { \alpha } f ( w , t ) + B ^ { \alpha } w ) = a \left( E _ { 0 } w + \sum _ { k = 1 } ^ { \infty } A ^ { \alpha } f ^ { ( k ) } ( w ) t ^ { k } \right) } \\ { = a ( E _ { 0 } w ) + \displaystyle \sum _ { k = 1 } ^ { \infty } t ^ { k } \sum _ { \substack { m = 1 } } ^ { k } \displaystyle \sum _ { i _ { 1 } + \dots + i _ { m } = k } \frac { 1 } { m ! } D _ { a , E _ { 0 } w } ^ { m } ( A ^ { \alpha } f ^ { ( i _ { 1 } ) } ( w ) , \cdots , A ^ { \alpha } f ^ { ( i _ { m } ) } ( w ) ) . } \end{array}
$$

Here, $D _ { a , E _ { 0 } }$ is multilinear operator defined by (8.21).

Substituting (8.22) and (8.24) in the right hand side of Equation (8.9), substituting (8.23) in the left hand side of (8.9), and then comparing the coefficients of $t ^ { k }$ on both sides, we get the recursions $( 8 . 1 8 ) - ( 8 . 2 0 )$ . The proof is completed. -

Remark 8.8. Let $\alpha = \alpha _ { ( 1 , 1 ) }$ , then (8.18) – (8.20) turn into

$$
\begin{array} { l l } { { f ^ { ( 0 ) } ( w ) = w , } } & { { } } \\ { { f ^ { ( 1 ) } ( w ) = \widetilde { a } ( w ) , } } & { { \widetilde { a } ( w ) = ( - a _ { 1 } ( w ) , a _ { 2 } ( w ) , \cdots , a _ { n } ( w ) ) ^ { \mathrm { T } } , } } \end{array}
$$

for $k \geq 1$

$$
\begin{array} { r c l } { f _ { i } ^ { ( k + 1 ) } ( w ) } & { = } & { \frac { 1 } { k + 1 } \widetilde { a _ { 1 } } ( w ) \frac { \partial f _ { i } ^ { ( k ) } ( w ) } { \partial w _ { 1 } } + \frac { 1 } { k + 1 } \displaystyle \sum _ { m = 1 } ^ { k - 1 } \sum _ { j = 1 } ^ { m } \sum _ { i _ { 1 } + \cdots + i _ { j } = m } \sum _ { 1 , \cdots , \alpha _ { j } = 2 } ^ { n } \frac { 1 } { j ! } } \\ & & { \cdot \frac { \partial f _ { i } ^ { ( k - m ) } ( w ) } { \partial w _ { 1 } } \frac { \partial ^ { j } \widetilde { a _ { 1 } } ( w ) } { \partial w _ { \alpha _ { 1 } } \cdots \partial w _ { \alpha _ { j } } } f _ { \alpha _ { 1 } } ^ { ( i _ { 1 } ) } ( w ) \cdot \cdot f _ { \alpha _ { j } } ^ { ( i _ { j } ) } ( w ) } \\ & & { + \displaystyle \frac { 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \sum _ { i _ { 1 } + \cdots + i _ { m } = k \alpha _ { 1 } , \cdots , \alpha _ { m } = 2 } ^ { n } \frac { 1 } { m ! } \frac { \partial ^ { m } \widetilde { a _ { i } } ( w ) } { \partial w _ { \alpha _ { 1 } } \cdot \cdot \cdot \partial w _ { \alpha _ { m } } } f _ { \alpha _ { 1 } } ^ { ( i _ { 1 } ) } ( w ) \cdot \cdot f _ { \alpha _ { m } } ^ { ( i _ { m } ) } ( w ) , } \\ & & { i = 1 , 2 , \cdots , n . } \end{array}
$$

# 10.8.2 Construction of Volume-Preserving Schemes

In this subsection, we consider the construction of volume-preserving schemes[Sha94a] for the source-free system (8.8). By Remark 8.3 of Theorem 8.1, for given timedependent scalar functions $\phi _ { 2 } ( w , t ) , \cdot \cdot \cdot , \phi _ { n } ( w , t ) : \mathbf { R } ^ { n } \times \mathbf { R }  \mathbf { R }$ and $C ( \widetilde { w } , t ) :$ $\mathbf { R } ^ { n - 1 } \times \mathbf { R } \to \mathbf { R }$ , we can get a time-dependent volume-preserving mapping $\widetilde { g } ( z , t )$ . If $\phi _ { 2 } ( w , t ) , \cdot \cdot \cdot , \phi _ { n } ( w , t )$ approximates the generating functions $f _ { 2 } ( w , t ) , \cdot \cdot \cdot , f _ { n } ( w , t )$ of the type $\alpha _ { ( 1 , 1 ) }$ of the source-free system (8.8), then suitable choice $C ( \tilde { w } , t ) , \tilde { g } ( w , t )$ approximates the phase flow $g _ { \alpha } ^ { t } ( z ) = g ( z , t )$ . Fixing $t$ " "as a time step, we can get a difference scheme (volume-preserving schemes) whose transition from one time step to the next is volume-preserving. By Remark 8.8 of Theorem 8.7, generating functions $f _ { 2 } ( w , t ) , \cdot \cdot \cdot , f _ { n } ( w , t )$ can be expressed as power series. So, a natural way to approximate $f _ { 2 } ( w , t ) , \cdot \cdot \cdot , f _ { n } ( w , t )$ is take the truncation of the series. However, we have to choose a suitable $C ( \widetilde w , t )$ in (8.7) to guarantee the accuracy of the scheme.

Assume that

$$
\phi _ { i } ^ { m } ( w , t ) = \sum _ { k = 0 } ^ { m } f _ { i } ^ { ( k ) } ( w ) t ^ { k } , \quad i = 2 , \cdots , n
$$

and

$$
\psi _ { 1 } ^ { m } ( w , t ) = \sum _ { k = 0 } ^ { m } f _ { 1 } ^ { ( k ) } ( w ) t ^ { k } .
$$

Let for some fixed value $w _ { 1 , 0 }$

$$
C ^ { m } ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } , t ) = \psi _ { 1 } ^ { ( m ) } ( w _ { 1 , 0 } , w _ { 2 } , \cdot \cdot \cdot , w _ { n } , t )
$$

and

$$
\phi _ { 1 } ^ { ( m ) } ( w , t ) = C ^ { ( m ) } ( w _ { 2 } , \cdots , w _ { n } , t ) + \int _ { w _ { 1 , 0 } } ^ { w _ { 1 } } \left| \frac { \partial \left( \phi _ { 2 } ^ { ( m ) } , \cdots , \phi _ { n } ^ { ( m ) } \right) } { \partial \left( w _ { 2 } , \cdots , w _ { n } \right) } \right| ( \xi , w _ { 2 } , \cdots , w _ { n } , t ) \mathrm { d } \xi .
$$

then we have,

Theorem 8.9. Using Theorem 8.5 and Theorem 8.7 for sufficiently small $\tau \geq 0$ as the time step, defining mapping $\phi ^ { ( m ) } ( w , \tau ) ~ = ~ ( \phi _ { 1 } ^ { ( m ) } ( w , \tau ) , \phi _ { 2 } ^ { ( m ) } ( w , \tau ) , \cdots ,$ $\phi _ { n } ^ { ( m ) } ( w , \tau ) ) ^ { \mathrm { T } }$ with the components $\phi _ { i } ^ { ( m ) } ( w , \tau ) ( i = 1 , 2 , \cdot \cdot \cdot , n )$ given as above for $m = 1 , 2 , \cdots$ , then the mapping

$$
w \longrightarrow \widehat { w } = \phi ^ { ( m ) } ( w , \tau ) ,
$$

defines a volume-preserving scheme $z = z ^ { k } \to z ^ { k + 1 } = { \widehat { z } }$

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k } = \phi _ { 1 } ^ { ( m ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \\ { \widehat { z } _ { i } ^ { k + 1 } = \phi _ { i } ^ { ( m ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \end{array} \right. \quad i = 2 , \cdot \cdot \cdot , n ,
$$

of $m$ -th order of accuracy of the source-free system (8.8).

Proof. Since $\phi _ { i } ^ { ( m ) } ( w , 0 ) = f _ { i } ^ { 0 } ( w , 0 ) = w _ { i } ( i = 2 , \cdot \cdot \cdot , n ) ,$

$$
\left| \frac { \partial ( \phi _ { 2 } ^ { ( m ) } , \cdots , \phi _ { n } ^ { ( m ) } ) } { \partial ( w _ { 2 } , \cdots , w _ { n } ) } \right| ( w , 0 ) = 1 .
$$

Therefore, for sufficiently small $\tau$ and in some neigbourhood of $\mathbf { R } ^ { n }$

$$
\left| \frac { \partial ( \phi _ { 2 } ^ { ( m ) } , \cdots , \phi _ { n } ^ { ( m ) } ) } { \partial ( w _ { 2 } , \cdots , w _ { n } ) } \right| ( w , \tau ) \neq 0 .
$$

By Theorem 8.1, Remark 8.3, Remark 8.4, and Equation (8.31), the relation (8.33) defines a time-dependent volume-preserving $z = z ^ { k } \to z ^ { k + 1 } = { \widehat { z } } = { \widetilde { g } } ( z , \tau )$ . That is, (8.33) is a volume-preserving scheme.

Noting that

$$
\begin{array} { r l } & { \phi _ { i } ^ { ( m ) } ( w , \tau ) = f _ { i } ( w , \tau ) + O ( \tau ^ { m + 1 } ) , \quad i = 2 , \cdot \cdot \cdot , n , } \\ & { } \\ & { \psi _ { 1 } ^ { ( m ) } ( w , \tau ) = f _ { 1 } ( w _ { 1 } , \tau ) + O ( \tau ^ { m + 1 } ) , } \end{array}
$$