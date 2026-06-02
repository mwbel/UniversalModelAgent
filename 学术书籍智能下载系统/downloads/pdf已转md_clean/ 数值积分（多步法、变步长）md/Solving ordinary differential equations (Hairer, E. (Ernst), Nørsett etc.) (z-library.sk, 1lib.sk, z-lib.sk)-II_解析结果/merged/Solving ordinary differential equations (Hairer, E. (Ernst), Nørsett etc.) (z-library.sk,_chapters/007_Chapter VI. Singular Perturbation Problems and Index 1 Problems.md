# Chapter VI. Singular Perturbation Problems and Index 1 Problems

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/8e848ab1b8930cb68894ad5f233dbb7f620663acd0b804aee4bbe5464e4e9256.jpg)  
(Drawing by G.Di Marzo)

Singular perturbation problems (SPP) form a special class of problems containing a parameter ε.When this parameter is small, the corresponding differential equation is stiff; when $\varepsilon$ tends to zero, the differential equation becomes differential algebraic. This chapter investigates the numerical solution of such singular perturbation problems. This allows us to understand many phenomena observed for very stiff problems. Much insight is obtained by studying the limit case $\varepsilon = 0$ ("the reduced system” or“problem of index 1") which is usually much easier to analyze.

We start by considering the limit case $\varepsilon = 0$ . Two numerical approaches - the $\varepsilon$ -embedding method and the state space form method - are investigated in Sect. VI.1. We then analyze multistep methods in Sect.VI.2, Runge-Kutta methods in Sect. VI.3, Rosenbrock methods in Sect. VI.4 and extrapolation methods in Sect. VI.5. Convergence is studied for singular perturbation problems and for semiexplicit differential-algebraic systems of "index 1".

# VI.1 Solving Index 1 Problems

Singular perturbation problems (SPP) have several origins in applied mathematics. One comes from fluid dynamics and results in linear boundary value problems containing a small parameter $\varepsilon$ (the coefficient of viscosity） such that for $\varepsilon \to 0$ the differential equation loses the highest derivative (see Exercise 1 below). Others originate in the study of nonlinear oscillations with large parameters (van der Pol 1926,Dorodnicyn 1947） or in the study of chemical kinetics with slow and fast reactions (see e.g., Example (IV.1.4)).

# Asymptotic Solution of van der Pol's Equation

The classical paper of Dorodnicyn (1947) studied the van der Pol Equation (IV.1.5) with large $\mu$ ,i.e., with small $\varepsilon$ . The investigation becomes a little easier if we use Lienard's coordinates (see Exercise I.16.8). In Eq.(IV.1.5'), writen here as

$$
\varepsilon z ^ { \prime \prime } + ( z ^ { 2 } - 1 ) z ^ { \prime } + z = 0 ,
$$

we insert the identity

$$
\varepsilon z ^ { \prime \prime } + ( z ^ { 2 } - 1 ) z ^ { \prime } = { \frac { d } { d x } } \underbrace { \left( \varepsilon z ^ { \prime } + ( { \frac { z ^ { 3 } } { 3 } } - z ) \right) } _ { : = y }
$$

so that (1.1) becomes

$$
\begin{array} { l l } { { y ^ { \prime } = - z } } & { { = : f ( y , z ) } } \\ { { \varepsilon z ^ { \prime } = y - \displaystyle \left( { \frac { z ^ { 3 } } { 3 } } - z \right) } } & { { = : g ( y , z ) . } } \end{array}
$$

Fig.1.1 shows solutions of Eq.(1.2) with $\varepsilon = 0 . 0 3$ in the $( y , z )$ -plane. One ob-serves rapid movements towards the manifold $M$ defined by $y = z ^ { 3 } / 3 - z$ ,close to which the solution becomes smooth. In order to approximate the solution for very small $\varepsilon$ , we set $\varepsilon = 0$ in (1.2) and obtain the so-called reduced system

$$
\begin{array} { l l } { { y ^ { \prime } = - z } } & { { = f ( y , z ) } } \\ { { \displaystyle 0 = y - \left( { \frac { z ^ { 3 } } { 3 } } - z \right) } } & { { = g ( y , z ) . } } \end{array}
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $\mathit { I I }$ ， Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_25, $©$ Springer-Verlag Berlin Heidelberg 2010

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/362a30f8f35a30aa0c9e99a9931d53c0a3de239e36f150d9c9bbf5a1ab036b7f.jpg)  
Fig.1.1. Solutions of SPP (1.2)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/1f0803de82e5539ff368c723176eae1a8e44eb42b143b6747a52fb28dfa607f7.jpg)  
Fig.1.2. Reduced problem (1.2')

While(1.2) has no analytic solution, (1.2') can easily be solved to give

$$
y ^ { \prime } = - z = ( z ^ { 2 } - 1 ) z ^ { \prime } \quad \mathrm { o r } \quad \ln | z | - { \frac { z ^ { 2 } } { 2 } } = x + C .
$$

Equation (1.2') is called a differential algebraic equation (DAE), since it combines a differential equation (first line) with an algebraic equation (second line). Such a problem only makes sense if the initial values are consistent, i.e., lie on the manifold $M$ . The points of $M$ with coordinates $y = \pm 2 / 3$ ， $z = \mp 1$ are of special interest (Fig. 1.2): at these points the partial derivative $g _ { z } = \partial g / \partial z$ vanishes and the defining manifold is no longer “transversal’ to the direction of the fast movement. Here the solutions of (1.2'） cease to exist, while the solutions of the full problem(1.2) for $\varepsilon \to 0$ jump with “infinite” speed to the opposite manifold. For $- 1 < z < 1$ the manifold $M$ is unstable for the solution of (1.2) (here $g _ { z } > 0$ ）， otherwise $M$ is stable $( g _ { z } < 0 )$

We demonstrate the power of the reduced equation by answering the question:

what is the period $T$ of the limit cycle solution of van der Pol's equation for $\varepsilon \to 0 \ ?$ Fig.1.2 shows that the asymptotic value of $T$ is just twice the time which $z ( x )$ of (1.3) needs to advance from $z = - 2$ to $z = - 1$ ,i.e.,

$$
T = 3 - 2 \ln 2 .
$$

This is the first term of Dorodnicyn's asymptotic formula. We also see that $z ( x )$ reaches its largest values (i.e.， crosses the Poincaré cut $z ^ { \prime } = 0$ ， see Fig.I.16.2) at $z = \pm 2$ . We thus have the curious result that the limit cycle of van der Pol's equation (1.1) has the same asymptotic initial value $z \approx 2$ and $z ^ { \prime } = 0$ for $\varepsilon  0$ and for $\varepsilon \to \infty$ (see Eq. (I.16.10)).

# The $\varepsilon$ -Embedding Method for Problems of Index 1

We now want to study the behaviour of the numerical solution for $\varepsilon  0$ .This will give us insight into many phenomena encountered for very stiff equations and also suggest advantageous numerical procedures for stiff and differential-algebraic equations. Let an arbitrary singular perturbation problem be given,

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { \varepsilon z ^ { \prime } = g ( y , z ) , } \end{array}
$$

where $y$ and $z$ are vectors； suppose that $f$ and $g$ are sufficiently often differentiable vector functions of the same dimensions as $y$ and $z$ ，respectively. The corresponding reduced equation is the DAE

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) , } \end{array}
$$

whose initial values are consistent if $0 = g ( y _ { 0 } , z _ { 0 } )$ ． A general assumption of the present chapter will be that the Jacobian

$$
g _ { z } ( y , z ) \mathrm { i s \ i n v e r t i b l e }
$$

in a neighbourhood of the solution of (1.6). Equation (1.6b) then possesses a locally unique solution $z = G ( y )$ ("Implicit Function Theorem") which inserted into (1.6a) gives

$$
y ^ { \prime } = f { \bigl ( } y , G ( y ) { \bigr ) } ,
$$

the so-called “state space form”,an ordinary differential system. Under the as-sumption (1.7),Eq.(1.6) is said to be a differential-algebraic equation of index $l$

An interesting approach for solving (1.6) is to apply some numerical method to the SPP (1.5) and to put $\varepsilon = 0$ in the resulting formulas. Let us illustrate this approach for Runge-Kutta methods. Applied to the system (1.5) we obtain

$$
Y _ { n \imath } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { \imath j } \ f ( Y _ { n j } , Z _ { n \jmath } )
$$

$$
\begin{array} { r c l } { { } } & { { } } & { { \varepsilon Z _ { n \scriptscriptstyle 1 } = \varepsilon z _ { n } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } g \left( Y _ { n \jmath } , Z _ { n \jmath } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { y _ { n + 1 } = y _ { n } + h \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } f \left( Y _ { n \imath } , Z _ { n \imath } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \varepsilon z _ { n + 1 } = \varepsilon z _ { n } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \imath } g \left( Y _ { n \imath } , Z _ { n \jmath } \right) . } } \end{array}
$$

We now suppose that the RK matrix $\left( { { a _ { \iota } } _ { \ j } } \right)$ is invertible and obtain from (1.9b)

$$
h g ( Y _ { n \imath } , Z _ { n \imath } ) = \varepsilon \sum _ { \jmath = 1 } ^ { s } \omega _ { \imath \jmath } ( Z _ { n \jmath } - z _ { n } ) ,
$$

where the $\omega _ { \imath \jmath }$ are the elements of the inverse of $\left( { { a _ { \iota } } _ { \jmath } } \right)$ .Inserting this into (1.9d) makes the definition of $z _ { n + 1 }$ independent of $\varepsilon$ . We thus put without more ado $\varepsilon = 0$ and obtain

$$
\begin{array} { c } { { { \cal Y } _ { n \displaystyle i } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i _ { j } } ~ f \left( Y _ { n _ { 2 } } , Z _ { n _ { 2 } } \right) } } \\ { { 0 = g ( Y _ { n i } , Z _ { n _ { 1 } } ) } } \\ { { y _ { n \displaystyle + 1 } = y _ { n } + h \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ f } } ~ f \left( Y _ { n \mathrm { } } , Z _ { n \mathrm { } } \right) } } \\ { { { } } } \\ { { z _ { n \displaystyle + 1 } = \left( 1 - \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ r } } \omega _ { \mathrm { n } j } \right) z _ { n } + \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ w } _ { \mathrm { i } j } } ~ Z _ { n _ { 2 } } . } } \end{array}
$$

Here

$$
1 - \sum _ { i , \ j = 1 } ^ { s } b _ { i } \omega _ { \ i \ j } = R ( \infty )
$$

(see Eq.(IV.3.15), where $R ( z )$ is the stability function of the method.

# State Space Form Method

The numerical solution $( y _ { n + 1 } , z _ { n + 1 } )$ of the above approach will usually not lie on the manifold $g ( y , z ) = 0$ . However,this can easily be repaired by replacing (1.11d) by the condition

$$
0 = g ( y _ { n + 1 } , z _ { n + 1 } ) .
$$

Then, we do not only have $Z _ { n } \mathrm {                                          } _ { } = G ( Y _ { n } \mathrm { \ } _ { \mathrm { } n } )$ (see (1.11b), but also $z _ { n + 1 } = G ( y _ { n + 1 } )$ In this case the method (1.11a-c),(1.12) is identical to the solution of the state space form (1.8) with the same Runge-Kutta method. This will be called the state space form method. The whole situation is summarized in the following diagram:

SPP (1.5) m↑0 DAE (1.6) z=G(y） → ODE (1.8)   
RK RK √   
Sol. (1.9) →0 $\varepsilon$ -embedding method state space form method Sol. (1.12)

Of special importance here are stifly accurate methods,i.e., methods which satisfy

$$
a _ { s \imath } = b _ { \imath } \qquad \mathrm { f o r } \quad i = 1 , \ldots , s .
$$

This means that $y _ { n + 1 } = Y _ { n s } , z _ { n + 1 } = Z _ { n s }$ and(12)isicefor stiffly accurate methods the $\varepsilon$ -embedding method and the state space form method are identical. For this reason, Griepentrog & März（1986) denote such methods IRK(DAE).

Both approaches have their own merits. Theoretical results for the $\varepsilon$ -embedding method yield insight into the method when applied to singular perturbation problems. Moreover, this approach can easily be extended to more general situa-tions,where the algebraic relation is not explicitly separated from the differential equation (see below). The state space form method, on the other hand, has the advantage that it is not restricted to implicit methods. Applying an explicit Runge-Kutta method or a multistep method to Eq.(1.8) is certainly a method of choice for semi-explicit index 1 equations. No new theory is necessary in this case.

# A Transistor Amplifier

...auf eine merkwirdige Tatsache aufmerksam machen, das ist die auBerordentlich grosse Zahl berihmter Mathematiker, die aus Konigsberg stammen ...: Kant 1724, Richelot 1808, Hesse 1811, Kirchhoff 1824, Carl Neumann 1832, Clebsch 1833,Hilbert 1862. (F. Klein, Entw. der Math., p.159)

Very often, differential-algebraic problems arising in practice are not at once in the semi-explicit form(1.6),but rather in the form $M u ^ { \prime } = \varphi ( u )$ where $M$ is a constant singular matrix.

As an example we compute the amplifier of Fig.1.3, where $U _ { e } ( t )$ is the entry voltage, $U _ { b } = 6$ the operating voltage, $U _ { i } ( t ) ~ ( i = 1 , 2 , 3 , 4 , 5 )$ the voltages at the nodes 1,2,3,4,5,and $U _ { 5 } ( t )$ the output voltage. The current through a resistor satisfies $I = U / R$ $( \mathrm { O h m ~ } 1 8 2 7 )$ , the current through a capacitor $I = C \cdot d U / d t$ ， where $R$ and $C$ are constants and $U$ the voltage. The transistor acts as amplifier in that the current from node 4 to node 3 is 99 times larger than that from node 2 to node 3 and depends on the voltage difference $U _ { 3 } - U _ { 2 }$ in a nonlinear way. Kirchhoff's law (a Konigsberg discovery) says that the sum of currents entering a node vanishes. This law applied to the 5 nodes of Fig.1.3 leads to the following equations:

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/0bbfd3ba238d96433ac51fa1ba5b5594c36fb5a272aff7ac94a0ca8f406b1220.jpg)  
Fig.1.3. A transistor amplifier

$$
\begin{array} { r l } { \textnormal { e l . } } & { \frac { U _ { k } } { R _ { 0 } } - \frac { U _ { 1 } } { R _ { 0 } } + C _ { 1 } ( U _ { 2 } ^ { \prime } - U _ { 1 } ^ { \prime } ) = 0 } \\ { \textnormal { e 2 . } } & { \frac { U _ { k } } { R _ { 2 } } - U _ { 2 } \left( \frac { 1 } { R _ { 1 } } + \frac { 1 } { R _ { 2 } } \right) + C _ { 1 } ( U _ { 1 } ^ { \prime } - U _ { 2 } ^ { \prime } ) - 0 . 0 1 f ( U _ { 2 } - U _ { 3 } ) = 0 } \\ { \textnormal { e 3 . } } & { f ( U _ { 2 } - U _ { 3 } ) - \frac { U _ { 3 } } { R _ { 3 } } - C _ { 2 } U _ { 3 } ^ { \prime } = 0 } \\ { \textnormal { e 4 . } } & { \frac { U _ { k } } { R _ { 4 } } - \frac { U _ { 4 } } { R _ { 4 } } + C _ { 3 } ( U _ { 5 } ^ { \prime } - U _ { 4 } ^ { \prime } ) - 0 . 9 9 f ( U _ { 2 } - U _ { 3 } ) = 0 } \\ { \textnormal { e 5 . } } & { - \frac { U _ { 5 } } { R _ { 5 } } + C _ { 3 } ( U _ { 4 } ^ { \prime } - U _ { 5 } ^ { \prime } ) = 0 . } \end{array}
$$

As constants we adopt the values reported (for a similar problem) by Rentrop, Roche & Steinebach(1989)

$$
\begin{array} { r l } & { f ( U ) = 1 0 ^ { - 6 } \left( \exp \left( \frac { U } { 0 . 0 2 6 } \right) - 1 \right) } \\ & { R _ { 0 } = 1 0 0 0 , \quad R _ { 1 } = \ldots = R _ { 5 } = 9 0 0 0 } \\ & { C _ { k } = k \cdot 1 0 ^ { - 6 } , \quad k = 1 , 2 , 3 , } \end{array}
$$

and the initial signal is chosen as

$$
U _ { e } ( t ) = 0 . 4 \cdot \sin ( 2 0 0 \pi t ) .
$$

Equations (1.14) are of the form $M \mathfrak { u } ^ { \prime } = \varphi ( \mathfrak { u } )$ where

$$
{ \cal M } = \left( \begin{array} { c c c c c } { { - C _ { 1 } } } & { { C _ { 1 } } } & { { } } & { { } } & { { } } \\ { { C _ { 1 } } } & { { - C _ { 1 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - C _ { 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { - C _ { 3 } } } & { { C _ { 3 } } } \\ { { } } & { { } } & { { } } & { { C _ { 3 } } } & { { - C _ { 3 } } } \end{array} \right)
$$

is obviously a singular matrix of rank 3. The sum of the first two and of the last two equations leads directly to two algebraic equations. Introducing e.g.,

$$
U _ { 1 } - U _ { 2 } = y _ { 1 } , \quad U _ { 3 } = y _ { 2 } , \quad U _ { 4 } - U _ { 5 } = y _ { 3 } , \quad U _ { 1 } = z _ { 1 } , \quad U _ { 4 } = z _ { 2 } ,
$$

transforms equations (1.14) to the form (1.6). Consistent initial values must thus satisfy $\varphi _ { 1 } ( u ) + \varphi _ { 2 } ( u ) = 0$ and $\varphi _ { 4 } ( u ) + \varphi _ { 5 } ( u ) = 0$ . If we put $U _ { 2 } ( 0 ) = U _ { 3 } ( 0 )$ ，we have $f ( U _ { 2 } ( 0 ) - U _ { 3 } ( 0 ) ) = 0$ . Since $U _ { e } ( 0 ) = 0$ , we then easily find consistent initial values, e.g., as

$$
U _ { 1 } ( 0 ) = 0 , \quad U _ { 2 } ( 0 ) = U _ { 3 } ( 0 ) = \frac { U _ { b } R _ { 1 } } { R _ { 1 } + R _ { 2 } } , \quad U _ { 4 } ( 0 ) = U _ { b } , \quad U _ { 5 } ( 0 ) = 0 .
$$

# Problems of the Form $M \boldsymbol { u } ^ { \prime } = \varphi ( \boldsymbol { u } )$

Numerical methods for problems of the form

$$
M u ^ { \prime } = \varphi ( u ) ,
$$

where $M$ is a constant matrix,can be derived as follows: we assume that $M$ is regular, apply an ODE method to $u ^ { \prime } = M ^ { - 1 } \varphi ( u )$ and multiply the resulting formulas by $M$ . For Runge-Kutta methods we obtain in this way

$$
M ( U _ { n \imath } - u _ { n } ) = h \sum _ { j = 1 } ^ { s } a _ { \imath j } \varphi ( U _ { n j } )
$$

$$
u _ { n + 1 } = \bigg ( 1 - \sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } \bigg ) u _ { n } + \sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } U _ { n j } ,
$$

where again $( \omega _ { i j } )$ is the inverse of $\left( a _ { \imath \jmath } \right)$ . The second formula was obtained from

$$
M ( u _ { n + 1 } - u _ { n } ) = h \sum _ { i = 1 } ^ { s } b _ { i } \varphi ( U _ { n \ i } )
$$

in exactly the same way as above (see (1.10)).

Formulas (1.18) also make sense formally when $M$ is a singular matrix. In this case,problem (1.17) is mathematically equivalent to a semi-explicit system (1.6) and method (1.18) corresponds to method (1.11). This can be seen as follows: we decompose the matrix $M$ (e.g., by Gaussian elimination with total pivoting) as

$$
M = S \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) T ,
$$

where $S$ and $T$ are invertible matrices and the dimension of $I$ represents the rank of $M$ . Inserting this into (1.17), multiplying by $S ^ { - 1 }$ , and using the transformed variables

$$
T u = { \left( \begin{array} { l } { y } \\ { z } \end{array} \right) } 
$$

gives

$$
{ \binom { y ^ { \prime } } { 0 } } = S ^ { - 1 } \varphi \Bigl ( T ^ { - 1 } { \binom { y } { z } } \Bigr ) = : \left( { \begin{array} { l } { f ( y , z ) } \\ { g ( y , z ) } \end{array} } \right) ,
$$

a problem of type (1.6). An initial value $u _ { 0 }$ is consistent if $\varphi ( u _ { 0 } )$ lies in the range of the matrix $M$

Similarly,if (1.19) is inserted into (1.18),and the variables

$$
T U _ { n j } = \left( \begin{array} { l } { { Y _ { n j } } } \\ { { Z _ { n j } } } \end{array} \right) , \qquad T u _ { n } = \left( \begin{array} { l } { { y _ { n } } } \\ { { z _ { n } } } \end{array} \right)
$$

are introduced, Eq.(1.18b) (for $Z _ { n + 1 } )$ and Eq.(1.18c) (for $Y _ { n + 1 } )$ lead precisely to equations (1.11). This means that the diagram

$$
\{ u _ { n } \}
$$

commutes. An important consequence of this commutativity is that all results for semi-explicit systems (1.6) and the $\varepsilon$ -embedding method (1.11) (existence of a numerical solution, convergence,asymptotic expansions,.. .） also apply to implicit problems (1.17) with singular $M$ and method (1.18).

All codes,such as RADAU5,which have an option for implicit differential equations (1.17) can thus be applied directly. This has been done for problem (1.14) with initial values (1.16),integration interval $0 \le x \le 0 . 2$ , and $T o l = 1 0 ^ { - 4 }$ · The code computed the solution $U _ { 5 } ( t )$ displayed in Fig.1.4 in 556 (accepted) steps. The comparison with the entry voltage $U _ { e } ( t )$ shows that our amplifier is working. See also Hairer,Lubich & Roche (1989),p.108-111 for a more elaborate example.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/a9cdc848062e5b556107f12d2c92277b92f6394ac0b773d8bb6eaecb06a85d8c.jpg)  
Fig.1.4. Computed solution of amplifier problem (1.14)

# Convergence of Runge-Kutta Methods

If the method is stiffly accurate, the numerical solutions (1.11） are equivalent to those of the ordinary equation (1.8). Therefore the convergence of the solutions is described by Theorems II.3.4 and II.3.6 as

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) ,
$$

where $p$ is the classical order of the method (the second formula follows from a Lipschitz condition for $G$ ). For general methods,the estimate (1.24) remains valid for $y _ { n }$ ,because (1.11a,b,c) are independent of $z _ { n }$ and do not change if (1.11d) is replaced by (1.12). Thus we only have to prove a convergence result for $z _ { n }$ .An essential ingredient of the following theorem is the stage order $q$ of the method, i.e., condition $C ( q )$ of Sect. II.7 or IV.5.

Theorem 1.1. Suppose that the system (1.6) satisfies(1.7) in a neighbourhood of the exact solution $( y ( x ) , z ( x ) )$ and assume the initial values are consistent. Consider a Runge-Kutta method of order $p$ ， stage order $q$ and with invertible matrix $A$ . Then the numerical solution of(1.1la-d) has global error

$$
z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { r } ) \quad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t ,
$$

where

$a$ ） $r = p$ for stiffly accurate methods,   
$b _ { . }$ ） $r = \operatorname* { m i n } ( p , q + 1 )$ if the stability function satisfes $- 1 \leq R ( \infty ) < 1$ $c _ { , }$ ） $r = \operatorname* { m i n } ( p - 1 , q )$ f $R ( \infty ) = + 1$ .   
d）1f $\dot { | } R ( \infty ) | > 1$ , the numerical solution diverges.

Proof. Part (a) has already been discussed. For the remaining cases we proceed as follows: we first observe that Condition $C ( q )$ and order $p$ imply

$$
z ( x _ { n } + c _ { \imath } h ) = z ( x _ { n } ) + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } z ^ { \prime } ( x _ { n } + c _ { \jmath } h ) + { \mathcal O } ( h ^ { q + 1 } )
$$

$$
z ( x _ { n + 1 } ) = z ( x _ { n } ) + h \sum _ { i = 1 } ^ { s } b _ { \imath } z ^ { \prime } ( x _ { n } + c _ { \imath } h ) + \mathcal { O } ( h ^ { p + 1 } ) .
$$

Since $A$ is invertible we can compute $z ^ { \prime } ( x _ { n } + c _ { \jmath } h )$ from(1.26a) and insert it into (1.26b). This gives

$$
z ( x _ { n + 1 } ) = \varrho z ( x _ { n } ) + b ^ { T } A ^ { - 1 } \widehat Z _ { n } + \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { q + 1 } )
$$

where $\varrho = 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } = R ( \infty )$ and $\widehat { Z } _ { n } = ( z ( x _ { n } + c _ { 1 } h ) , \ldots , z ( x _ { n } + c _ { s } h ) ) ^ { T }$ .We then denote the global error by $\Delta z _ { n } = z _ { n } - z ( x _ { n } )$ ， and $\Delta Z _ { n } = Z _ { n } - \widehat { Z } _ { n }$ . Subtracting (1.27) from (1.11d) yields

$$
\begin{array} { r } { \Delta z _ { n + 1 } = \varrho \Delta z _ { n } + b ^ { T } A ^ { - 1 } \Delta Z _ { n } + \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { q + 1 } ) . } \end{array}
$$

Our next aim is to estimate $\Delta Z _ { n }$ . For this we have to consider the $y$ -component of the system. Due to (1.11a-c) the values $y _ { n } , Y _ { n \imath }$ are those of the Runge-Kutta method applied to (1.8). It thus follows from Theorem II.8.1 that $y _ { n } - y ( x _ { n } ) =$ $e _ { p } ( x _ { n } ) h ^ { p } + { \mathcal { O } } ( h ^ { p + 1 } )$ . Since Eq.(1.26a) also holds with $z ( x )$ replaced by $y ( x )$ ， we can subtract this formula from (1.11a) and so obtain

$$
\begin{array} { r l } {  { Y _ { n \imath } - y ( x _ { n } + c _ { \imath } h ) = y _ { n } - y ( x _ { n } ) } } \\ & { \quad + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \Big ( f \big ( Y _ { n \jmath } , G ( Y _ { n \jmath } ) \big ) - f \big ( y ( x _ { n } + c _ { \jmath } h ) , G ( y ( x _ { n } + c _ { \jmath } h ) ) \Big ) + \mathcal O ( h ^ { q + 1 } ) . } \end{array}
$$

This implies that

$$
Y _ { n \imath } - y ( x _ { n } + c _ { \imath } h ) = { \mathcal O } ( h ^ { \nu } ) \qquad { \mathrm { w i t h } } \quad \nu = \operatorname* { m i n } ( p , q + 1 ) .
$$

Because of (1.11b) we get

$$
Z _ { n \ i } - z ( x _ { n } + c _ { \ i } h ) = G ( Y _ { n \ i } ) - G \big ( y ( x _ { n } + c _ { \ i } h ) \big ) = \mathcal { O } ( h ^ { \nu } )
$$

and Eq.(1.28) becomes

$$
\Delta z _ { n + 1 } = \varrho \Delta z _ { n } + \delta _ { n + 1 } , \qquad \mathrm { w h e r e } \quad \delta _ { n + 1 } = \mathcal { O } \big ( h ^ { \nu } \big ) .
$$

Repeated insertion of this formula gives

$$
\Delta z _ { n } = \sum _ { \imath = 1 } ^ { n } \varrho ^ { n - \imath } \delta _ { \imath } ,
$$

because $\Delta z _ { 0 } = 0$ . This proves the statement for $\varrho \neq - 1$ . For the case $\varrho = - 1$ the error $\Delta z _ { n }$ is a sum of differences $\delta _ { \jmath + 1 } - \delta _ { j }$ . Since $\delta _ { n + 1 }$ is actually of the form $\delta _ { n + 1 } = d ( x _ { n } ) h ^ { \nu } + \mathcal { O } ( h ^ { \nu + 1 } )$ we have $\begin{array} { r } { \dot { \delta } _ { \jmath + 1 } - \dot { \delta } _ { \jmath } = \mathcal { O } ( h ^ { \nu + 1 } ) } \end{array}$ and the statement also follows in this situation. □

The order reduction in the $z$ -component (for non stiffly accurate methods) was first studied by Petzold (1986) in a more general context.

# Exercises

1. Compute the solutions of the boundary value problems

$$
\begin{array} { c c c } { { \varepsilon y ^ { \prime \prime } + y ^ { \prime } + y = 1 } } & { { \mathrm { r e s p e c t i v e l y } } } & { { \varepsilon y ^ { \prime \prime } - y ^ { \prime } + y = 1 } } \\ { { } } & { { } } & { { y ( 0 ) = y ( 1 ) = 0 , \quad \mathrm { f o r } \quad \varepsilon > 0 . } } \end{array}
$$

Observe that the solutions possess, for $\varepsilon \to 0$ ,a"boundary layer”on one of the two sides of [O,1] and that the limit solutions for $\varepsilon = 0$ satisfy

$$
y ^ { \prime } + y = 1 \qquad { \mathrm { r e s p e c t i v e l y } } \qquad - y ^ { \prime } + y = 1
$$

with one of the two boundary conditions being lost.

# VI.2 Multistep Methods

The aim of this section is to study convergence of multistep methods when applied to singular perturbation problems (Runge-Kutta methods will be treated in Sect. VI.3). We are interested in estimates that hold uniformly for $\varepsilon \to 0$ . The re-sults of the previous chapters cannot be applied. Since the Lipschitz constant of the singular perturbation problem (1.5) is of size $\mathcal { O } ( \varepsilon ^ { - 1 } )$ ， the estimates of Sect. III.4 are useless. Also the one-sided Lipschitz constant is in general $\mathcal { O } ( \varepsilon ^ { - 1 } )$ , so that the convergence results of Sect. V.8 can neither be applied. Let us start by considering the reduced problem.

# Methods for Index 1 Problems

A multistep method applied to the system $y ^ { \prime } = f ( y , z )$ ， $\varepsilon z ^ { \prime } = g ( y , z )$ gives

$$
\begin{array} { c } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f ( y _ { n + \imath } , z _ { n + \imath } ) } } \\ { { \displaystyle \varepsilon \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } z _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } g ( y _ { n + \imath } , z _ { n + \imath } ) . } } \end{array}
$$

By putting $\varepsilon \approx 0$ we obtain ( $\varepsilon$ -embedding method)

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { n + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } f ( y _ { n + \ i } , z _ { n + \ i } )
$$

$$
0 = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } g ( y _ { n + \imath } , z _ { n + \imath } )
$$

which allows us to apply a multistep method to the differential-algebraic system (1.6). This approach was first proposed (for the BDF methods) by Gear (1971).

Theorem 2.1. Suppose that the system (1.6) satisfies (1.7). Consider a multistep method of order $p$ which is stable at the origin and at infinity(O and $\infty$ are in the stability region) and suppose that the error of the starting values $y _ { \jmath } , z _ { \jmath }$ for $j = 0 , \ldots , k - 1$ is $\mathcal { O } ( h ^ { p } )$ . Then the global error of(2.2) satisfies

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } )
$$

for $x _ { n } - x _ { 0 } = n h \leq C o n s t .$

Proof.Formula (2.2b) is a stable recursion for $\delta _ { n } = g ( y _ { n } , z _ { n } )$ , because $\infty$ lies in the stability region of the method. This together with the assumption on the starting values implies that $\delta _ { n } = \mathcal { O } ( h ^ { p } )$ for all $n \geq 0$ . By the Implicit Function Theorem $g ( y _ { n } , z _ { n } ) = \delta _ { n }$ can be solved for $z _ { n }$ and yields

$$
z _ { n } = G ( y _ { n } ) + \mathcal { O } ( h ^ { p } )
$$

with $G ( y )$ as in (1.8). Inserting (2.3) into (2.2a) gives the multistep formula for the differential equation (1.8) with an $\mathcal { O } ( h ^ { p + 1 } )$ perturbation. The statement then follows from the convergence proof of Sect. III.4. □

For the implicit index l problem (1.17) the multistep method becomes

$$
M \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } u _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \varphi ( u _ { n + \imath } )
$$

and convergence without any order reduction for methods satisfying the hypotheses of Theorem 2.1 follows from the transformation (1.20) and the diagram (1.23).

The state space from approach is also possible for multistep methods. We just have to replace (2.2b) by

$$
g ( y _ { n + k } , z _ { n + k } ) = 0 .
$$

Method $( 2 . 2 \mathsf { a } , \mathsf { c } )$ is equivalent to the solution of(1.8) by the above multistep method. Hence,we have convergence as for nonstiff ordinary differential equations. The assumption $^ { 6 6 } \infty \in S ^ { \prime \prime }$ is no longer necessary and even explicit methods can be applied.

# Convergence for Singular Perturbation Problems

The error propagation has been studied by Soderlind & Dahlquist (1981) using $G$ stability estimates. Convergence results were first obtained by Lotstedt (1985) for BDF methods. The following convergence result by Lubich (1991), based on the smoothness of the exact solution and thus uniform in $\varepsilon$ as long as we stay away from transient phases,gives optimal error bounds for arbitrary multistep methods.

The Jacobian of the system (1.5) is of the form

$$
\left( \begin{array} { c c } { { f _ { y } } } & { { f _ { z } } } \\ { { \varepsilon ^ { - 1 } g _ { y } } } & { { \varepsilon ^ { - 1 } g _ { z } } } \end{array} \right)
$$

and its dominant eigenvalues are seen to be close to ${ \varepsilon } ^ { - 1 } \lambda$ where $\lambda$ represents the eigenvalues of $g _ { z }$ . For reasons of stability we assume throughout this subsection that the eigenvalues of $g _ { z }$ have negative real part. More precisely, we assume that

for $( y , z )$ in a neighbourhood of the considered solution. We then have the following result for method (2.1a,b):

Theorem 2.2 (Lubich 1991). Suppose that the multistep method is of order $p$ ， $A ( \alpha )$ -stable and strictly stable at infinity. If the problem (1.5) satisfies (2.5), then the error is bounded for $h \geq \varepsilon$ and $n h \le \overline { { x } } - x _ { 0 }$ by

$$
\begin{array} { r l } {  { \| y _ { n } - y ( x _ { n } ) \| + \| z _ { n } - z ( x _ { n } ) \| } } \\ & { \leq C \Big ( \underset { 0 \leq \jmath < k } { \operatorname* { m a x } } \ \| y _ { \jmath } - y ( x _ { \jmath } ) \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { n } } \| y ^ { ( p + 1 ) } ( x ) \| d x } \\ & { \qquad + ( h + \varrho ^ { n } ) \underset { 0 \leq \jmath < k } { \operatorname* { m a x } } \ \| z _ { \jmath } - z ( x _ { \jmath } ) \| + \varepsilon h ^ { p } \underset { x _ { 0 } \leq x \leq x _ { n } } { \operatorname* { m a x } } \| z ^ { ( p + 1 ) } ( x ) \| \Big ) } \end{array}
$$

with $0 < \varrho < 1$ . This estimate holds for $h \leq h _ { 0 }$ （ $h _ { 0 }$ sufficiently small, but independent of $\varepsilon$ ), and provided that the starting values are in $a$ sufficiently small, $h$ - and $\varepsilon$ -independent neighbourhood of the exact solution. The constants $C$ and $\varrho$ are independent of $\varepsilon$ and $h$

Proof. The proof is divided into several parts: in part (a) we shall derive recursive estimates for the global error, these will be solved in part (b); part (c) proves an inequality which is needed in (a).

a) First we insert the exact solution of(1.5) into the method (2.1) and so obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { i } y ( x _ { n + \imath } ) = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f \bigl ( y ( x _ { n + \imath } ) , z ( x _ { n + \imath } ) \bigr ) + d _ { n + k } } } \\ { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } z ( x _ { n + \imath } ) = \frac { h } { \varepsilon } \sum _ { \imath = 0 } ^ { k } \beta _ { i } g \bigl ( y ( x _ { n + i } ) , z ( x _ { n + \imath } ) \bigr ) + e _ { n + k } , } } \end{array}
$$

where the perturbations $d _ { n + k } , e _ { n + k }$ can be estimated (for $n \geq 0$ as

$$
\begin{array} { l } { \| d _ { n + k } \| \leq C _ { 1 } h ^ { p } \displaystyle \int _ { x _ { n } } ^ { x _ { n + k } } \| y ^ { ( p + 1 ) } ( x ) \| d x } \\ { \| e _ { n + k } \| \leq C _ { 2 } h ^ { p + 1 } \displaystyle \operatorname* { m a x } _ { x _ { n } \leq x \leq x _ { n + k } } \| z ^ { ( p + 1 ) } ( x ) \| . } \end{array}
$$

We then denote the global errors by $\Delta y _ { n } = y _ { n } - y ( x _ { n } )$ ， $\Delta z _ { n } = z _ { n } - z ( x _ { n } )$ and introduce the differences

$$
\Delta f _ { n + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Bigl ( f ( y _ { n + \imath } , z _ { n + \imath } ) - f \bigl ( y ( x _ { n + \imath } ) , z ( x _ { n + \imath } ) \bigr ) \Bigr ) , \qquad n \geq 0 ,
$$

$\Delta f _ { \jmath } = 0$ for $j < k$ . Subtraction of (2.6a) from (2.1a) yields for $n \geq 0$

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } \Delta y _ { n + \imath } = h \Delta f _ { n + k } - d _ { n + k } .
$$

Guided by previous experience (see (V.7.41)), we define $d _ { 0 } , \ldots , d _ { k - 1 }$ so that (2.8)

also holds for negative $n$ . Solving for $\Delta y _ { n }$ gives

$$
\Delta y _ { n } = h \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } ( 0 ) \Delta f _ { \jmath } - \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } ( 0 ) d _ { \jmath }
$$

where $r _ { \jmath } ( 0 )$ is defined in (V.7.44). These numbers are the coefficients of $r ( \zeta , 0 ) =$ $\zeta ^ { - k } / \varrho \big ( \breve { \zeta } ^ { - 1 } \big )$ . By zero-stability of the method, the sequence $\{ r _ { \jmath } ( 0 ) \}$ is bounded, so that a Lipschitz condition for $f ( y , z )$ implies the estimate

$$
\| \Delta y _ { n } \| \leq h \sum _ { \jmath = 0 } ^ { n } \bigl ( M \| \Delta y _ { \jmath } \| + N \| \Delta z _ { \jmath } \| \bigr ) + C _ { 3 } \sum _ { \jmath = 0 } ^ { n } \| d _ { \jmath } \| .
$$

A more refined estimate is necessary for the $z$ -component. We take the difference of (2.1b) and (2.6b) and then subtract from both sides the quantity

$$
\frac { h } { \varepsilon } \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } J \Delta z _ { n + \iota } \qquad \mathrm { w h e r e } \quad J = g _ { \iota } ( y _ { 0 } , z _ { 0 } ) .
$$

This yields

$$
\sum _ { \ i = 0 } ^ { k } \bigl ( \alpha _ { \ i } I - \beta _ { \ i } { \frac { h } { \varepsilon } } J \bigr ) \Delta z _ { n + \ i } = { \frac { h } { \varepsilon } } \Delta g _ { n + k } - e _ { n + k }
$$

where

$$
\Delta g _ { n + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Big ( g \big ( y _ { n + \imath } , z _ { n + \imath } \big ) - g \big ( y \big ( x _ { n + \imath } \big ) , z \big ( x _ { n + \imath } \big ) \big ) - J \Delta z _ { n + \imath } \Big ) ,
$$

and $\Delta g _ { \jmath } = 0$ for $\jmath < k$ . We again define $e _ { 0 } , \ldots , e _ { k - 1 }$ such that (2.11) holds for negative $\mathscr { n }$ ,and we then solve (2.11) for $\Delta z _ { n }$ . This gives

$$
\Delta z _ { n } = \frac { h } { \varepsilon } \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } \left( \frac { h } { \varepsilon } J \right) \Delta g _ { \jmath } - \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } \left( \frac { h } { \varepsilon } J \right) e _ { \jmath }
$$

where the matrices $\begin{array} { r } { r _ { \jmath } \left( \frac { h } { \varepsilon } \boldsymbol { J } \right) } \end{array}$ are defined by (see Formula (V.7.50))

$$
{ \frac { h } { \varepsilon } } \sum _ { \jmath \geq 0 } r _ { \jmath } \left( { \frac { h } { \varepsilon } } \ J \right) \zeta ^ { \jmath } = \left( { \frac { \varepsilon } { h } } \delta ( \zeta ) I - J \right) ^ { - 1 } { \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } }
$$

with $\delta ( \zeta )$ given in (V.7.45). In part (c) below we shall prove that

$$
\frac { h } { \varepsilon } \left\| r _ { \ j } \left( \frac { h } { \varepsilon } \ j \right) \right\| \leq C \kappa ^ { \ j } \qquad \mathrm { w i t h } \quad 0 < \kappa < 1 .
$$

Inserted into (2.13) we thus get

$$
\| \Delta z _ { n } \| \leq \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \big ( L \| \Delta y _ { \jmath } \| + \ell \| \Delta z _ { \jmath } \| \big ) + C _ { 4 } \frac { \varepsilon } { h } \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \| e _ { \jmath } \| .
$$

It is important to remark that the Lipschitz constant $\ell$ can be made arbitrarily small by shrinking the considered interval.

b) In ordertosolvetheinequalities (2.9)and (2.16)we definesequences $\{ u _ { n } \}$ and $\{ v _ { n } \}$ by

$$
\begin{array} { l } { \displaystyle { u _ { n } = h \sum _ { \jmath = 0 } ^ { n } ( M u _ { \jmath } + N v _ { \jmath } ) + C _ { 3 } \sum _ { \jmath = 0 } ^ { n } \| d _ { \jmath } \| , } } \\ { \displaystyle { v _ { n } = \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } ( L u _ { \jmath } + \ell v _ { \jmath } ) + C _ { 4 } \frac { \varepsilon } { h } \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \| e _ { \jmath } \| . } } \end{array}
$$

An induction argument shows that

$$
\| \Delta y _ { n } \| \leq u _ { n } , \qquad \| \Delta z _ { n } \| \leq v _ { n }
$$

provided $\ell < 1$ and $h \leq h _ { 0 }$ . We then rewrite (2.17) as

$$
\begin{array} { l l } { { u _ { n } = u _ { n - 1 } + h M u _ { n } + h N v _ { n } + C _ { 3 } \| d _ { n } \| , \qquad u _ { - 1 } = 0 , } } \\ { { \displaystyle v _ { n } = \kappa v _ { n - 1 } + L u _ { n } + \ell v _ { n } + C _ { 4 } \frac { \varepsilon } { h } \| e _ { n } \| , \qquad v _ { - 1 } = 0 . } } \end{array}
$$

Solving for $u _ { n } , v _ { n }$ we get (with $\varrho = \kappa / ( 1 - \ell ) )$

$$
\left( \begin{array} { c } { { u _ { n } } } \\ { { v _ { n } } } \end{array} \right) = A ( h ) \left( \begin{array} { c } { { u _ { n - 1 } } } \\ { { v _ { n - 1 } } } \end{array} \right) + \left( \begin{array} { c } { { \widehat { d } _ { n } } } \\ { { \widehat { e } _ { n } } } \end{array} \right) , \qquad A ( h ) = \left( \begin{array} { c c } { { 1 + { \mathcal O } ( h ) } } & { { { \mathcal O } ( h ) } } \\ { { { \mathcal O } ( 1 ) } } & { { \varrho + { \mathcal O } ( h ) } } \end{array} \right)
$$

where

$$
| \widehat { d } _ { n } | \leq C _ { 5 } \big ( \| d _ { n } \| + \varepsilon \| e _ { n } \| \big ) , \qquad | \widehat { e } _ { n } | \leq C _ { 6 } \big ( \| d _ { n } \| + \frac \varepsilon h \| e _ { n } \| \big ) .
$$

Inserting (2.18) repeatedly we obtain

$$
\left( \begin{array} { l } { u _ { n } } \\ { v _ { n } } \end{array} \right) = \sum _ { j = 0 } ^ { n } A ( h ) ^ { n - j } \left( \begin{array} { l } { \widehat { d } _ { j } } \\ { \widehat { e } _ { j } } \end{array} \right) .
$$

If $\ell$ is small enough so that $\varrho = \kappa / ( 1 - \ell ) < 1$ and if $h \leq h _ { 0 }$ , then the eigenvalues of $A ( h )$ are distinct and $A ( h )$ can be diagonalized as

$$
A ( h ) = T ^ { - 1 } ( h ) \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { 0 } \\ { 0 } & { \varrho + \mathcal { O } ( h ) } \end{array} \right) T ( h ) , \quad T ( h ) = \left( \begin{array} { c c } { 1 } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { 1 } \end{array} \right) .
$$

Inserted into (2.20) this yields

$$
u _ { n } + v _ { n } \leq C o n s t . \left( \sum _ { \jmath = 1 } ^ { n } \widehat { d } _ { \jmath } + \sum _ { \jmath = 1 } ^ { n } ( h + \varrho ^ { n - \jmath } ) \widehat { e } _ { \jmath } \right) .
$$

Since $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the values $\Delta y _ { 0 } , \ldots , \Delta y _ { k - 1 }$ ，and $e _ { 0 } , \ldots , e _ { k - 1 }$ are linear combinations of the $\Delta z _ { \jmath }$ and $\begin{array} { r } { \frac { h } { \varepsilon } \Delta z _ { \jmath } } \end{array}$ , the statement of the theorem follows from (2.19） and (2.7). Because of our assumption on $\ell$ (that $\varrho = \kappa / ( 1 - \ell ) < 1 )$ ）we have proved the theorem for sufficiently small (but $\varepsilon \cdot$ independent） intervals. Compact intervals $\left\{ x _ { 0 } , { \overline { { x } } } \right\}$ can be covered by repeated application of the above estimates.

c) It still remains to prove (2.15). More generally, we shall show that

$$
\frac { h } { \varepsilon } \left\| r _ { \ j } \left( \frac { h } { \varepsilon } g _ { z } ( y , z ) \right) \right\| \leq C \kappa ^ { \ j } \qquad \mathrm { w i t h } \quad 0 < \kappa < 1
$$

holds uniformly in a compact neighbourhood of the solution. This is necessary, if the above estimates are applied to several subintervals.In order to prove (2.21) we remember that $\begin{array} { r } { r _ { \mathcal { I } } \left( \frac { h } { \varepsilon } J \right) } \end{array}$ is defined by (2.14). If we are able to show that

$$
\bigg \vert \bigg \vert \bigg ( \frac { \varepsilon } { h } \delta ( \zeta ) I - g _ { z } ( y , z ) \bigg ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - k } ) } \bigg \vert \bigg \vert \leq C \qquad \mathrm { f o r } \ \quad \vert \zeta \vert \leq 1 / \kappa
$$

then the estimate (2.21) follows immediately from Cauchy's integral formula

$$
\frac { h } { \varepsilon } r _ { j } \Big ( \frac { h } { \varepsilon } J \Big ) = \frac { 1 } { 2 \pi i } \int _ { | \zeta | = 1 / \kappa } \Big ( \frac { \varepsilon } { h } \delta ( \zeta ) I - J \Big ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } \cdot \zeta ^ { - j - 1 } d \zeta .
$$

By definition of the stability region $S$ of a multistep method, the value $\delta ( \zeta )$ lies outside of $S$ whenever $| \zeta | < 1$ . Recall that the method is $A ( \alpha )$ -stable and strictly stable at infinity,and the differential equation satisfies (2.5). Therefore the set of eigenvalues of $g _ { z } ( y , z )$ (with $( y , z )$ varying in a compact neighbourhood of the solution) is well separated from $\{ \gamma \delta ( \zeta ) : \gamma \leq 1 , | \zeta | \leq 1 \}$ . It is even separated from $\{ \gamma \delta ( \zeta ) ; \gamma \leq 1 , | \zeta | \leq 1 / \kappa \}$ with some $\kappa < 1$ . Together with Exercise 2 of Sect.V.7 this proves (2.22). □

# Exercises

1. (Lubich 1991). Prove that for the BDF-schemes the estimate of Theorem 2.2 (for $n \geq k )$ is valid with $\left( h + \varrho ^ { \pi } \right)$ replaced by $\varepsilon ( 1 + \varrho ^ { n } / \hbar )$ in the factor multiplying the $z$ -component of the errors in the starting values. Hint. Give a direct proof for $n \in \{ k , \ldots , 2 k - 1 \}$ ; then apply Theorem 2.2 to shifted starting values.

# VI.3Epsilon Expansions for Exact and RK Solutions

In the preceding section we have proved convergence of multistep methods for singular perturbation problems. The same techniques do not yield optimal estimates for Runge-Kutta methods. We therefore investigate more thoroughly the structure of the solutions of singular perturbation problems. A first systematic study of the qualitative aspects of such problems is due to Tikhonov (1952). Asymptotic expansions were then analyzed by Vasil'eva (1963). Classical books on this subject are Wasow (1965), O'Malley (1974),and Tikhonov, Vasil'eva & Sveshnikov(1985).

# Expansion of the Smooth Solution

Tihonov's theorem is only the first step ... The actual approximate solution of such problems in series form is still a difficult question. It has been analyzed in a series of papers by Vasil'eva (W. Wasow 1965)

We consider the singular perturbation problem

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { \varepsilon z ^ { \prime } = g ( y , z ) , \qquad 0 < \varepsilon \ll 1 } } \end{array}
$$

where $f$ and $g$ are sufficiently differentiable. The functions $f , g$ and the initial values $y ( 0 )$ ， $z ( 0 )$ may depend smoothly on $\varepsilon$ . For simplicity of notation we suppress this dependence. The corresponding equation for $\varepsilon \approx 0$ ，

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) , } \end{array}
$$

is the reduced problem. In order to guarantee the solvability of (3.2),we assume that $g _ { z } ( y , z )$ is invertible (in a neighbourhood of the solution of (3.2).

We are mainly interested in smooth solutions of (3.1), which are of the form

$$
\begin{array} { l } { { y ( x ) = y _ { 0 } ( x ) + \varepsilon y _ { 1 } ( x ) + \varepsilon ^ { 2 } y _ { 2 } ( x ) + \dots . } } \\ { { z ( x ) = z _ { 0 } ( x ) + \varepsilon z _ { 1 } ( x ) + \varepsilon ^ { 2 } z _ { 2 } ( x ) + \dots . } } \end{array}
$$

Inserting (3.3) into (3.1) and collecting equal powers of $\varepsilon$ yields

$$
\left. \begin{array} { r l } { \varepsilon ^ { 0 } : } & { { } \quad y _ { 0 } ^ { \prime } = f \big ( y _ { 0 } , z _ { 0 } \big ) } \\ { 0 = g \big ( y _ { 0 } , z _ { 0 } \big ) } \end{array} \right\}
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_27, $©$ Springer-Verlag Berlin Heidelberg 2010

$$
\begin{array} { r l r } {  { \varepsilon ^ { 1 } : \quad } } & { y _ { 1 } ^ { \prime } = f _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { 1 } + f _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { 1 } \quad } & { \mathrm { ( } } \\ & { } & { z _ { 0 } ^ { \prime } = g _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { 1 } + g _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { 1 } \quad \} } \\ & { } & { \quad \cdot \cdot \cdot } \\ & { \quad } & { y _ { \nu } ^ { \prime } = f _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { \nu } + f _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { \nu } + \varphi _ { \nu } \big ( y _ { 0 } , z _ { 0 } , \ldots , y _ { \nu - 1 } , z _ { \nu - 1 } \big ) \quad } \\ & { } & { z _ { \nu - 1 } ^ { \prime } = g _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { \nu } + g _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { \nu } + \psi _ { \nu } \big ( y _ { 0 } , z _ { 0 } , \ldots , y _ { \nu - 1 } , z _ { \nu - 1 } \big ) \quad } \end{array}
$$

As expected, we see from (3.4a) that $y _ { 0 } ( x ) , \ z _ { 0 } ( x )$ is a solution of the reduced system. Since $g _ { z }$ is invertible, the second equation of (3.4b) can be solved for $z _ { 1 }$ .By inserting $z _ { 1 }$ into the upper relation of(3.4b) we obtain a linear differential equation for $y _ { 1 } ( x )$ . Hence, $y _ { 1 } ( x )$ and $z _ { 1 } ( x )$ are determined. Similarly, we get $y _ { 2 } ( x ) , z _ { 2 } ( x )$ from (3.4c), etc.

This construction of the coefficients of (3.3） shows that we can choose the initial values $y _ { \jmath } ( 0 )$ arbitrarily,but that there is no freedom in the choice of $z _ { \jmath } ( 0 )$ · Consequently, not every solution of (3.1) can be written in the form (3.3).

# Expansions with Boundary Layer Terms

To construct a uniform asymptotic expansion we must combine the Maclaurin expansion with another expansion of special form. The terms in this expansion are exponential functions that are appreciable inside the boundary layer,but negligibly small outside it. (A.B. Vasil'eva 1963)

Example 3.1. We consider the problem (IV.1.1), written in the form

$$
\varepsilon z ^ { \prime } = - z + \cos x .
$$

Its analytic solution

$$
\begin{array} { c } { { z ( x ) = ( 1 + \varepsilon ^ { 2 } ) ^ { - 1 } ( \cos x + \varepsilon \sin x ) + C e ^ { - x / \varepsilon } } } \\ { { { } } } \\ { { = \cos x + \varepsilon \sin x - \varepsilon ^ { 2 } \cos x - \varepsilon ^ { 3 } \sin x + \ldots + C e ^ { - x / \varepsilon } } } \end{array}
$$

is a superposition of a smooth solution of the form (3.3) and of a rapidly decaying function. This additional term (transient phase, boundary layer) compensates the missing freedom in the choice of the initial values $z _ { \jmath } \left( 0 \right)$

Motivated by this example, we seek solutions of the general problem (3.1) which are of the form

$$
\begin{array} { l } { { \displaystyle y ( x ) = \sum _ { j \ge 0 } \varepsilon ^ { j } y _ { j } ( x ) + \varepsilon \sum _ { j \ge 0 } \varepsilon ^ { j } \eta _ { j } ( x / \varepsilon ) } } \\ { { \displaystyle z ( x ) = \sum _ { j \ge 0 } \varepsilon ^ { j } z _ { j } ( x ) + \sum _ { j \ge 0 } \varepsilon ^ { j } \zeta _ { j } ( x / \varepsilon ) , } } \end{array}
$$

where $y _ { \jmath } ( x ) , z _ { \jmath } ( x )$ are determined by (3.4) and the $\varepsilon$ -independent functions $\eta _ { \jmath }$ $\zeta _ { j }$ are assumed to satisfy

$$
\| \eta _ { \ j } ( \xi ) \| \le e ^ { - \kappa \xi } , \qquad \| \zeta _ { \ j } ( \xi ) \| \le e ^ { - \kappa \xi }
$$

with some $\kappa > 0$ . Inserting (3.6) into (3.1) and using (3.4) we obtain formally

$$
\begin{array} { l } { { \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } ^ { \prime } \left( \frac { x } { \varepsilon } \right) = f \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) + \varepsilon \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } \left( \frac { x } { \varepsilon } \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) + \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } \left( \frac { x } { \varepsilon } \right) \right) } } \\ { { \displaystyle \qquad - f \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) \right) } } \\ { { \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } ^ { \prime } \left( \frac { x } { \varepsilon } \right) = g \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) + \varepsilon \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } \left( \frac { x } { \varepsilon } \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) + \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } \left( \frac { x } { \varepsilon } \right) \right) } } \\ { { \displaystyle \qquad - g \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) \right) } . } \end{array}
$$

We then replace $x$ by the stretched variable

$$
\xi = x / \varepsilon
$$

and compare like powers of $\varepsilon$ in (3.8). This gives for $\varepsilon ^ { 0 }$

$$
\begin{array} { r l } & { \eta _ { 0 } ^ { \prime } ( \xi ) = f { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) { \big ) } - f { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) { \big ) } } \\ & { \zeta _ { 0 } ^ { \prime } ( \xi ) = g { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) { \big ) } - g { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) { \big ) } . } \end{array}
$$

At this point it is necessary to introduce some stability assumption for (3.1) in order to obtain (3.7). We shall require that the logarithmic norm of $g _ { z }$ satisfy

$$
\mu \big ( g _ { z } ( y , z ) \big ) \leq - 1
$$

in an $\varepsilon$ -independent neighbourhood of the solution of (3.2) (any negative bound other than $- 1$ can be normalized by re-scaling $\varepsilon$ ).By Theorem I.10.6 Eqs. (3.10b) and (3.11) imply

$$
\begin{array} { r } { \| \zeta _ { 0 } ( \xi ) \| \le \| \zeta _ { 0 } ( 0 ) \| e ^ { - \xi } . } \end{array}
$$

Since $f ( y , z )$ satisfies locally a Lipschitz condition, the right-hand side of (3.10a), denoted by $\varphi ( \xi )$ , is bounded by $\| \varphi ( \xi ) \| \le L \| \zeta _ { 0 } ( 0 ) \| e ^ { - \xi }$ . Consequently, there is only one solution of (3.10a) which satisfies (3.7), namely

$$
\eta _ { 0 } ( \xi ) = \int _ { 0 } ^ { \xi } \varphi ( s ) d s - \int _ { 0 } ^ { \infty } \varphi ( s ) d s .
$$

A comparison of the powers of $\varepsilon ^ { 1 }$ in (3.8) yields

$$
\begin{array} { r l } & { \eta _ { 1 } ^ { \prime } ( \xi ) = f _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) + \eta _ { 0 } ( \xi ) \big ) } \\ & { \qquad + f _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) + \zeta _ { 1 } ( \xi ) \big ) } \\ & { \qquad - f _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) \big ) } \\ & { \qquad - f _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) \big ) } \\ & { \zeta _ { 1 } ^ { \prime } ( \xi ) = g _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) + \eta _ { 0 } ( \xi ) \big ) } \\ & { \qquad + g _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) + \zeta _ { 1 } ( \xi ) \big ) } \end{array}
$$

$$
\begin{array} { r l } & { - g _ { y } \left( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \right) \left( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) \right) } \\ & { - g _ { z } \left( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \right) \left( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) \right) . } \end{array}
$$

Eq.(3.13b) is a linear differential equation for $\zeta _ { 1 } ( \xi )$ . Its defect, for $\zeta _ { 1 }$ replaced by 0, is bounded by $C e ^ { - \xi }$ . Therefore,an application of Theorem I.10.6 yields

$$
\begin{array} { r } { \| \zeta _ { 1 } ( \xi ) \| \le e ^ { - \xi } \big ( \| \zeta _ { 1 } ( 0 ) \| + C \xi \big ) , } \end{array}
$$

which implies (3.7) for any $\kappa < 1$ . The right-hand side of (3.13a) is then bounded by $C _ { 1 } e ^ { - \kappa \xi }$ ． As in (3.12) we obtain a unique solution to (3.13a),which satisfies (3.7). This procedure can be continued to construct all further $\eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ . At each step, the value of $\kappa$ in (3.7) may become smaller. This is no serious difficulty, because we are only interested in a finite part of the series (3.6).

We point out that for the construction of $\eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ we can choose $\zeta _ { \mathcal { I } } ( 0 )$ arbitrarily, but that there is no freedom in the choice of $\mathfrak { \eta } _ { \jmath } ( 0 )$ ·

As a consequence,for an arbitrary initial value for (3.1) with expansion

$$
\begin{array} { l } { { y ( 0 ) = y _ { 0 } ^ { 0 } + \varepsilon y _ { 1 } ^ { 0 } + \varepsilon ^ { 2 } y _ { 2 } ^ { 0 } + \dots . } } \\ { { z ( 0 ) = z _ { 0 } ^ { 0 } + \varepsilon z _ { 1 } ^ { 0 } + \varepsilon ^ { 2 } z _ { 2 } ^ { 0 } + \dots . } } \end{array}
$$

the coeficients of the series (3.6) can be constructed as follows: put $x = 0$ in (3.6) to obtain the necessary relations

$$
y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 } , \qquad y _ { \ j } ( 0 ) + \eta _ { \ j - 1 } ( 0 ) = y _ { \ j } ^ { 0 } , \qquad z _ { \ j } ( 0 ) + \zeta _ { \ j } ( 0 ) = z _ { \ j } ^ { 0 } .
$$

This initial value $y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 }$ determines $z _ { 0 } ( 0 )$ by (3.4a), $\zeta _ { 0 } ( 0 )$ is then given by (3.15), $\eta _ { 0 } ( 0 )$ by (3.12), $y _ { 1 } ( 0 )$ by (3.15), $z _ { 1 } ( 0 )$ by (3.4b), $\zeta _ { 1 } ( 0 )$ by (3.15), $\eta _ { 1 } ( 0 )$ by (3.13a) and (3.7), $y _ { 2 } ( 0 )$ by (3.15), etc.

# Estimation of the Remainder

The following result gives a rigorous estimate of the remainder in (3.6), when only a truncated series is considered.

Theorem 3.2. Consider the initial value problem (3.1), (3.14), and suppose that (3.11) holds in an $\varepsilon$ -independent neighbourhood of the solution $y _ { 0 } ( x )$ ， $z _ { 0 } ( x )$ $[ 0 \leq$ $x \leq \overline { { x } } )$ of the reduced problem $( y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 } )$ .If $( y _ { 0 } ^ { 0 } , z _ { 0 } ^ { 0 } )$ lies in this neighbourhood, then the problem (3.1),(3.14) has $a$ unique solution for $\varepsilon$ sufficiently small and for $0 \leq x \leq \overline { { x } }$ ， which is of the form

$$
\begin{array} { l } { { \displaystyle y ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } y _ { j } ( x ) + \varepsilon \sum _ { j = 0 } ^ { N - 1 } \varepsilon ^ { j } \eta _ { j } ( x / \varepsilon ) + \mathcal { O } ( \varepsilon ^ { N + 1 } ) } } \\ { { \displaystyle z ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } z _ { j } ( x ) + \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } \zeta _ { j } ( x / \varepsilon ) + \mathcal { O } ( \varepsilon ^ { N + 1 } ) . } } \end{array}
$$

The coefficients $y _ { 3 } ( x ) , z _ { 3 } ( x ) , \eta _ { 3 } ( \xi ) , \zeta _ { 3 } ( \xi )$ are given by (3.4), (3.10), (3.13), and satisfy (3.7).

Proof. We denote the truncated series by

$$
\begin{array} { l } { { \displaystyle { \widehat { y } } ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { \jmath } y _ { \jmath } ( x ) + \varepsilon \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } \eta _ { j } ( x / \varepsilon ) } } \\ { { \displaystyle { \widehat { z } } ( x ) = \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } z _ { \jmath } ( x ) + \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } \zeta _ { \jmath } ( x / \varepsilon ) } . } \end{array}
$$

By our construction of $y _ { j } ( x ) , z _ { \jmath } ( x ) , \eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ we have

$$
\begin{array} { c } { { \widehat { y } ^ { \prime } ( x ) = f \big ( \widehat { y } ( x ) , \widehat { z } ( x ) \big ) + { \mathcal O } ( { \varepsilon } ^ { N + 1 } ) } } \\ { { \varepsilon \widehat { z } ^ { \prime } ( x ) = g \big ( \widehat { y } ( x ) , \widehat { z } ( x ) \big ) + { \mathcal O } ( { \varepsilon } ^ { N + 1 } ) . } } \end{array}
$$

Subtracting (3.1) from (3.18) and exploiting Lipschitz conditions for $f$ and $g$ we obtain

$$
\begin{array} { r l } & { \quad D _ { + } \| \widehat { y } ( x ) - y ( x ) \| \leq L _ { 1 } \| \widehat { y } ( x ) - y ( x ) \| + L _ { 2 } \| \widehat { z } ( x ) - z ( x ) \| + C _ { 1 } \varepsilon ^ { N + 1 } } \\ & { \quad \varepsilon D _ { + } \| \widehat { z } ( x ) - z ( x ) \| \leq L _ { 3 } \| \widehat { y } ( x ) - y ( x ) \| - \| \widehat { z } ( x ) - z ( x ) \| + C _ { 2 } \varepsilon ^ { N + 1 } . } \end{array}
$$

Here, $D _ { + }$ denotes the Dini derivate introduced in Section I.1O. We have used $D _ { + } \| w ( x ) \| \leq \| w ^ { \prime } ( x ) \|$ (see Eq.(I.10.4)) and, for the second inequality of (3.19), Formula (I.10.17) together with (3.11).

In order to solve inequality (3.19) we replace $\leq { \mathfrak { b y } } =$ and so obtain

$$
\begin{array} { r l } { u ^ { \prime } = L _ { 1 } u + L _ { 2 } v + C _ { 1 } \varepsilon ^ { N + 1 } , \quad } & { u _ { 0 } = \| \widehat { y } ( 0 ) - y ( 0 ) \| = \mathcal { O } ( \varepsilon ^ { N + 1 } ) } \\ { \varepsilon v ^ { \prime } = L _ { 3 } u - v + C _ { 2 } \varepsilon ^ { N + 1 } , \quad } & { v _ { 0 } = \| \widehat { z } ( 0 ) - z ( 0 ) \| = \mathcal { O } ( \varepsilon ^ { N + 1 } ) . } \end{array}
$$

This system is quasimonotone,it thus follows from Exercise 7 (Sect.I.10) that

$$
\| { \widehat { y } } ( x ) - y ( x ) \| \leq u ( x ) , \qquad \| { \widehat { z } } ( x ) - z ( x ) \| \leq v ( x ) .
$$

Transforming (3.20) to diagonal form one easily finds its analytic solution and verifies that $u ( x ) = \mathcal { O } ( \varepsilon ^ { N + 1 } )$ ， $v ( x ) = \mathcal { O } ( \varepsilon ^ { N + 1 } )$ on compact intervals. Inserted into (3.21) this proves the statement. □

# Expansion of the Runge-Kutta Solution

After having understood the structure of the analytic solution of (3.1),we turn our attention to its numerical counterpart. We consider the Runge-Kutta method

$$
\left( { \begin{array} { l } { y _ { n + 1 } } \\ { z _ { n + 1 } } \end{array} } \right) = \left( { \begin{array} { l } { y _ { n } } \\ { z _ { n } } \end{array} } \right) + h \sum _ { \iota = 1 } ^ { \ s } b _ { \iota } \left( { \begin{array} { l } { k _ { n \iota } } \\ { \ell _ { n \iota } } \end{array} } \right)
$$

where

$$
\binom { k _ { n \imath } } { \varepsilon \ell _ { n \imath } } = \binom { f ( Y _ { n \imath } , Z _ { n \imath } ) } { g ( Y _ { n \imath } , Z _ { n \imath } ) }
$$

and the internal stages are given by

$$
{ \binom { Y _ { n \imath } } { Z _ { n \imath } } } = { \binom { y _ { n } } { z _ { n } } } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \left( { k _ { n \jmath } \atop \ell _ { n \jmath } } \right) .
$$

For arbitrary initial values,the solution possesses a transient phase (as described by Theorem 3.2),and the numerical method has anyway to take small step sizes of magnitude $\mathcal O ( \varepsilon )$ . We shall therefore focus on the situation where the transient phase is over and the method has reached the smooth solution within the given tolerance.We thus suppose that the initial values lie on the smooth solution (ie., that an expansion of the form (3.3) holds) and that the step size $h$ is large compared to $\varepsilon$ ．Our first goal is an $\varepsilon$ -expansion of the numerical solution. To this end, we formally expand all occuring quantities into powers of $\varepsilon$ with $\varepsilon$ -independent coefficients (see Hairer,Lubich & Roche 1988)

$$
\begin{array} { c } { { y _ { n } = y _ { n } ^ { 0 } + \varepsilon y _ { n } ^ { 1 } + \varepsilon ^ { 2 } y _ { n } ^ { 2 } + . . . } } \\ { { \nonumber Y _ { n \imath } = Y _ { n \imath } ^ { 0 } + \varepsilon Y _ { n \imath } ^ { 1 } + \varepsilon ^ { 2 } Y _ { n \imath } ^ { 2 } + . . . } } \\ { { \nonumber k _ { n i } = k _ { n \imath } ^ { 0 } + \varepsilon k _ { n i } ^ { 1 } + \varepsilon ^ { 2 } k _ { n \imath } ^ { 2 } + . . . } } \end{array}
$$

and similarly for $z _ { n } , Z _ { n } , \ell _ { n i }$ . Because of the linearity of the relations (3.22) and (3.24) we have

$$
\left( { y _ { n + 1 } ^ { \nu } \atop z _ { n + 1 } ^ { \nu } } \right) = \left( { y _ { n } ^ { \nu } \atop z _ { n } ^ { \nu } } \right) + h \sum _ { i = 1 } ^ { s } b _ { \imath } \left( { k _ { n \atop \ell _ { n } ^ { \nu } } ^ { \nu } } \right)
$$

and

$$
\binom { Y _ { n \iota } ^ { \nu } } { Z _ { n \iota } ^ { \nu } } = \binom { y _ { n } ^ { \nu } } { z _ { n } ^ { \nu } } + h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \binom { k _ { n j } ^ { \nu } } { \ell _ { n \jmath } ^ { \nu } } .
$$

Inserting (3.25b, c) into (3.23) and comparing equal powers of $\varepsilon$ we obtain

$$
\begin{array} { r l r } { \varepsilon ^ { 0 } : } & { k _ { n \tau } ^ { 0 } = f ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) \ \biggr \} } & { ( 3 . 2 8 \mathfrak { a } ) } \\ & { 0 = g ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) \ \biggr \} } & { ( 3 . 2 8 \mathfrak { a } ) } \\ & { k _ { n \tau } ^ { 1 } = f _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { 1 } + f _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n i } ^ { 1 } \ \biggr \} } & { ( 3 . 2 8 \mathfrak { b } ) } \\ { \varepsilon ^ { 1 } : } & { \ell _ { n \tau } ^ { 0 } = g _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n i } ^ { 1 } + g _ { z } ( Y _ { n i } ^ { 0 } , Z _ { n i } ^ { 0 } ) Z _ { n \tau } ^ { 1 } \ \biggr \} } \\ & { \cdot \cdot \cdot } & { \cdot \cdot } \\ & { k _ { n \tau } ^ { \nu } = f _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { \nu } + f _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n \tau } ^ { \nu } + \varphi _ { \nu } ( Y _ { n \tau } ^ { 0 } , Z _ { n i } ^ { 0 } , . . . , Y _ { n \tau } ^ { \nu - 1 } , Z _ { n \tau } ^ { \nu - 1 } ) \ \biggr \} } \\ { \varepsilon ^ { \nu } : } & { \ell _ { n \tau } ^ { \nu - 1 } = g _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { \nu } + g _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n \tau } ^ { \nu } + \psi _ { \nu } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } , . . . , Y _ { n \tau } ^ { \nu - 1 } , Z _ { n \tau } ^ { \nu - 1 } ) \ \biggr \} } \end{array}
$$

Since (3.23) has the same form as the differential equation (3.1),it is obvious that the formulas of (3.28) are exactly the same as those of (3.4). An interesting interpretation of this fact is the following:thecoeficients $y _ { n } ^ { 0 } , z _ { n } ^ { 0 } , y _ { n } ^ { 1 } , z _ { n } ^ { 1 } , . .$ repre-sent the numerical solution of the Runge-Kutta method applied to the differentialalgebraic system (3.4) ( $\varepsilon$ -embedding method of Sect. VI.1). This can be expressed by the commutativity of the following diagram:

Subtracting (3.25a) from(3.3) we get formally

$$
\begin{array} { l } { { \displaystyle y _ { n } - y ( x _ { n } ) = \sum _ { \nu \geq 0 } \varepsilon ^ { \nu } \left( y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) \right) } } \\ { { \displaystyle z _ { n } - z ( x _ { n } ) = \sum _ { \nu \geq 0 } \varepsilon ^ { \nu } \left( z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) \right) } . } \end{array}
$$

In order to study this error we first investigate the differences $y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) , z _ { n } ^ { \nu } -$ $z _ { \nu } ( x _ { n } )$ (next subsection). A rigorous estimate of the remainder in (3.29) will then follow. The presentation follows that of Hairer,Lubich & Roche (1988).

# Convergence of RK-Methods for Diferential-Algebraic Systems

The first differences $y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } )$ ， $z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } )$ in the expansions of (3.29) are just the global errors of the Runge-Kutta method applied to the reduced system (3.4a). By assumption (3.11) this system is of index 1. Therefore,the following result is an immediate consequence of Theorem 1.1.

Theorem 3.3. Consider a Runge-Kutta method of (classical) order $p$ , with invertible coefficient matrix $( { a } _ { \iota _ { \mathcal { I } } } )$ . Suppose that Problem $( 3 . 4 a )$ satisfies (3.11) and that the initial values are consistent.

$a$ ) If the method is stiffly accurate (i.e.,， $a _ { s _ { 2 } } = b _ { \tau }$ for $\iota = 1 , \ldots , s )$ then the global error satisfies

$$
y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) .
$$

$^ { b ) }$ If the stability function satisfes $| R ( \infty ) | < 1$ ， and the stage order is $q$ $1 ( q < p )$ ， then

$$
y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \qquad z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) = { \mathcal { O } } ( h ^ { q + 1 } ) .
$$

In both cases the estimates hold uniformly for $n h \le C o n s t$

Estimating the second differences $y _ { n } ^ { 1 } - y _ { 1 } ( x _ { n } )$ ， $z _ { n } ^ { 1 } - z _ { 1 } ( x _ { n } )$ is not as simple, because the enlarged system (3.4a,b) with differential variables $y _ { 0 } , z _ { 0 } , y _ { 1 }$ and algebraic variable $z _ { 1 }$ ,is no longer of index 1. It is actually of index 2, as will become clear in Sect. VII.1 below (Exercise 5). In principle it is possible to consult the re-sults of Sect. VI.4 (Theorems VII.4.5 and VII.4.6). For the special system $_ { ( 3 . 4 a , b ) }$ ， however, a simpler proof is possible. It also extends more easily to the higher-index problems (3.4a-c).

Theorem 3.4 (Hairer, Lubich & Roche 1988). Consider a Runge-Kuta method of order $ { p }$ ， stage order $q$ $( q < p )$ ， such that $\left( { a _ { \iota } } _ { \jmath } \right)$ is invertible and the stability function satisfies $| R ( \infty ) | < 1$ .If $\left( 3 . l I \right)$ holds and if the initial values of the differentialalgebraic system $\left( 3 . 4 a \cdot c \right)$ are consistent, then the global error of method (3.26)- (3.28) satisfies for $1 \leq \iota / \leq \ q + 1$

$$
y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) = \mathcal { O } ( h ^ { q + 2 - \nu } ) , \qquad z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) = \mathcal { O } ( h ^ { q + 1 - \nu } ) .
$$

Proof. We denote the differences to the exact solution values by

$$
\begin{array} { r l r } & { \Delta y _ { n } ^ { \nu } = y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) , } & { \Delta z _ { n } ^ { \nu } = z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) , } \\ & { \Delta Y _ { n \imath } ^ { \nu } = Y _ { n \imath } ^ { \nu } - y _ { \nu } ( x _ { n } + c _ { \imath } h ) , } & { \Delta Z _ { n \imath } ^ { \nu } = Z _ { n \imath } ^ { \nu } - z _ { \nu } ( x _ { n } + c _ { \imath } h ) , } \\ & { \Delta k _ { n \imath } ^ { \nu } = k _ { n \imath } ^ { \nu } - y _ { \nu } ^ { \prime } ( x _ { n } + c _ { \imath } h ) , } & { \Delta \ell _ { n \imath } ^ { \nu } = \ell _ { n \imath } ^ { \nu } - z _ { \nu } ^ { \prime } ( x _ { n } + c _ { \imath } h ) . } \end{array}
$$

Since the quadrature formula with nodes $c _ { \imath }$ and weights $b _ { \imath }$ is of order $ { p }$ , we have from (3.26)

$$
\left( \begin{array} { c } { \Delta y _ { n + 1 } ^ { \nu } } \\ { \Delta z _ { n + 1 } ^ { \nu } } \end{array} \right) = \left( \begin{array} { c } { \Delta y _ { n } ^ { \nu } } \\ { \Delta z _ { n } ^ { \nu } } \end{array} \right) + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \left( \begin{array} { c } { \Delta k _ { n i } ^ { \nu } } \\ { \Delta \ell _ { n i } ^ { \nu } } \end{array} \right) + \mathcal { O } ( h ^ { p + 1 } ) .
$$

Similarly, the definition of the stage order implies

$$
\left( \begin{array} { c } { \Delta Y _ { n } ^ { \nu } } \\ { \Delta Z _ { n \imath } ^ { \nu } } \end{array} \right) = \left( \begin{array} { c } { \Delta y _ { n } ^ { \nu } } \\ { \Delta z _ { n \imath } ^ { \nu } } \end{array} \right) + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \left( \begin{array} { c } { \Delta k _ { n \jmath } ^ { \nu } } \\ { \Delta \ell _ { n \jmath } ^ { \nu } } \end{array} \right) + \mathcal { O } ( h ^ { q + 1 } ) .
$$

It follows from Theorem 3.3 (see also the proof of Theorem 1.1) that

$$
\begin{array} { r l r l r l } & { \Delta y _ { n } ^ { 0 } = \mathcal { O } ( h ^ { p } ) , } & & { \Delta Y _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta k _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) } \\ & { \Delta z _ { n } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta Z _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta \ell _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q } ) . } \end{array}
$$

a) We frst consider the case $\imath / = 1$ Replacing n (3.28b) $Y _ { n i } ^ { ( 0 ) }$ ， $Z _ { n \uparrow } ^ { ( \ l ) }$ by $y _ { 0 } ( x _ { n } +$ $c _ { i } h ) + \Delta Y _ { n i } ^ { 0 }$ ， $z _ { 0 } ( x _ { n } + c _ { \imath } h ) + \Delta Z _ { n \imath } ^ { 0 }$ andsubtractingEquation (3.4b)ateposition $x = x _ { n } + c _ { \imath } \hbar$ ,we obtain with the help of (3.35)

$$
\begin{array} { r l } & { \Delta k _ { n \imath } ^ { 1 } = f _ { y } ( x _ { n } + c _ { i } h ) \Delta Y _ { n \imath } ^ { 1 } + f _ { z } ( x _ { n } + c _ { \imath } h ) \Delta Z _ { n \imath } ^ { 1 } } \\ & { \qquad \quad + \mathcal { O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta Y _ { n \imath } ^ { 1 } \| + h ^ { q + 1 } \| \Delta Z _ { n \imath } ^ { 1 } \| ) } \\ & { \Delta \ell _ { n \imath } ^ { 0 } = g _ { y } ( x _ { n } + c _ { \imath } h ) \Delta Y _ { n \imath } ^ { 1 } + g _ { z } ( x _ { n } + c _ { \imath } h ) \Delta Z _ { n \imath } ^ { 1 } } \\ & { \qquad \quad + \mathcal { O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta Y _ { n \imath } ^ { 1 } \| + h ^ { q + 1 } \| \Delta Z _ { n \imath } ^ { 1 } \| ) . } \end{array}
$$

Here we have used the abbreviations $f _ { y } ( x ) = f _ { y } ( y _ { 0 } ( x ) , z _ { 0 } ( x ) )$ ， etc. Computing $\Delta Z _ { n i } ^ { 1 }$ from the second relation of (3.36) and inserting it into the first one yields

$$
\begin{array} { r l } & { \Delta k _ { n \ i } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + c _ { i } h ) \Delta \ell _ { n \ i } ^ { 0 } } \\ & { \qquad = ( f _ { y } - f _ { z } g _ { z } ^ { - 1 } g _ { y } ) ( x _ { n } + c _ { i } h ) \Delta \boldsymbol { \Upsilon } _ { n \ i } ^ { - 1 } + { \mathcal O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta \boldsymbol { \Upsilon } _ { n \ i } ^ { \prime 1 } \| ) . } \end{array}
$$

Using (3.34) we can eliminate $\Delta Y _ { n \imath } ^ { 1 }$ and obtain (with (3.35))

$$
\Delta k _ { n \ i } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + c _ { \ i } h ) \Delta \ell _ { n \ i } ^ { 0 } = \mathcal { O } ( \| \Delta y _ { n } ^ { 1 } \| ) + \mathcal { O } ( h ^ { q + 1 } ) .
$$

Since $\Delta \ell _ { n \imath } ^ { 0 }$ is of size $\mathcal { O } ( h ^ { q } )$ ， we only have $\Delta k _ { n \imath } ^ { 1 } = \mathcal { O } ( \vert \vert \Delta y _ { n } ^ { 1 } \vert \vert ) + \mathcal { O } ( h ^ { q } )$ ，and a direct estimation of $\Delta y _ { n } ^ { 1 }$ in (3.33） would lead to $\Delta y _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ ,which is not optimal. We therefore introduce the new variable

$$
\Delta u _ { n } ^ { 1 } = \Delta y _ { n } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \Delta z _ { n } ^ { 0 } .
$$

From (3.33) we get

$$
\begin{array} { l } { \displaystyle \Delta u _ { n + 1 } ^ { 1 } = \Delta u _ { n } ^ { 1 } + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } \big ( \Delta k _ { n } ^ { 1 } - \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } ) \Delta \ell _ { n a } ^ { 0 } \big ) } \\ { \displaystyle - \left( \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } + h ) - \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } ) \right) \Delta z _ { n + 1 } ^ { 0 } + \mathcal { O } \big ( h ^ { p + 1 } \big ) . } \end{array}
$$

The estimates (3.35), (3.37)and the fact that $\Delta y _ { n } ^ { 1 } = \Delta u _ { n } ^ { 1 } + \mathcal { O } ( h ^ { q + 1 } )$ imply that

$$
\begin{array} { r } { \| \Delta u _ { n + 1 } ^ { 1 } \| \leq ( 1 + C h ) \| \Delta u _ { n } ^ { 1 } \| + \mathcal { O } ( h ^ { q + 2 } ) . } \end{array}
$$

Standard techniques now show that $\Delta u _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q + 1 } )$ for $n h \le C o n s t$ (observe that the initial values are assumed to be consistent, i.e., $\Delta u _ { 0 } ^ { 1 } = 0 .$ ),so that by (3.38) and (3.35) also $\Delta y _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q + 1 } )$ . This implies $\Delta k _ { n \ i } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ by (3.37) and $\Delta Y _ { n \ i } ^ { 1 } =$ $\mathcal { O } ( h ^ { q + 1 } )$ by (3.34). The second relation of (3.36) then proves that $\Delta Z _ { n \imath } ^ { 1 } = \mathcal { O } ( \bar { h ^ { q } } )$ . In order to estimate $\Delta z _ { n } ^ { 1 }$ ，we compute $\Delta \ell _ { n \imath } ^ { 1 }$ from (3.34) and insert it into (3.33). Using $\Delta Z _ { n \imath } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ this gives

$$
\Delta z _ { n + 1 } ^ { 1 } = ( 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } ) \Delta z _ { n } ^ { 1 } + { \cal O } ( h ^ { q } ) ,
$$

and it follows from $\vert 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } \vert = \vert R ( \infty ) \vert < 1$ that $\Delta z _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ . We have thus proved the case $\nu \simeq 1$

b) The proof for general $\nu$ is by induction.We shall show that

$$
\begin{array} { r l } { \Delta y _ { n } ^ { \nu } = \mathcal { O } ( h ^ { q + 2 - \nu } ) , \quad } & { \Delta Y _ { n \ i } ^ { \nu } = \mathcal { O } \big ( h ^ { q + 2 - \nu } \big ) } \\ { \Delta z _ { n \ i } ^ { \nu } = \mathcal { O } ( h ^ { q + 1 - \nu } ) , \quad } & { \Delta Z _ { n \ i } ^ { \nu } = \mathcal { O } \big ( h ^ { q + 1 - \nu } \big ) } \end{array}
$$

holds for $\nu = 1 , \ldots , q + 1$ . The main difference to the case $\nu = 1$ consists in the additional inhomogeneities $\varphi _ { \nu }$ and $\psi _ { \nu }$ in (3.4c). Using their Lipschitz continuity one obtains an aditional term of size $\mathcal { O } ( h ^ { q + 2 - \nu } )$ in (3.36). Otherwise the proof is identical to that for $\nu = 1$ □

We next study the existence and local uniqueness of the solution of the Runge-Kutta method (3.22)-(3.24). Further, we investigate the influence of perturbations in (3.24) to the numerical solution. This will be important for the estimation of the remainder in the expansion (3.29).

# Existence and Uniqueness of the Runge-Kutta Solution

For $h$ small compared to $\varepsilon$ , the existence of a unique numerical solution of (3.23), (3.24) follows from standard fixed point iteration (e.g., Theorem II.7.2). For the (more interesting) case where the step size $h$ is large compared to $\varepsilon$ ,we suppose that $( y _ { n } , z _ { n } )$ are known,denote it by $( \eta , \zeta )$ ，and prove the cxistence of $\left( y _ { n + 1 } , z _ { n + 1 } \right)$ as follows:

Theorem 3.5 (Hairer,Lubich & Roche 1988)． Assume that $y ( \eta , \zeta ) = \mathcal { O } ( h )$ ， $\mu ( g _ { z } ( \eta , \zeta ) ) \leq - 1$ and that the eigenvalues of the Runge-Kuta matrix $\left( \boldsymbol { a } _ { i j } \right)$ have positive real part. Then, the nonlinear system

$$
\left( { \begin{array} { l } { \displaystyle Y _ { \imath } - \eta } \\ { \varepsilon ( Z _ { \imath } - \zeta ) } \end{array} } \right) = h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \left( { \begin{array} { l } { f ( Y _ { \jmath } , Z _ { \jmath } ) } \\ { g ( Y _ { \jmath } , Z _ { \jmath } ) } \end{array} } \right)
$$

possesses a locally unique solution for $h \leq h _ { 0 }$ ，where $h _ { 0 }$ is sufficiently small but independent of $\xi$ . This solution satisfies

$$
Y _ { \imath } - \eta = \mathcal { O } ( h ) , \qquad Z _ { \imath } - \zeta = \mathcal { O } ( h ) .
$$

Proof. We apply Newton's method to the nonlinear system (3.43), whose second equation is divided by $l _ { l }$ . The existence and uniqueness statement can then be deduced from the theorem of Newton-Kantorovich (Kantorovich & Akilov 1959, Ortega &Rheinboldt 1970)asfollows:forthestarting valuesY( =n， $Z _ { 1 } ^ { ( 0 ) } = 5$ the Jacobian of the system is of the form

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { ( \varepsilon / h ) I - A \otimes g _ { z } ( \eta , \zeta ) } \end{array} \right) .
$$

Since $\mu ( g _ { z } ( \eta , \zeta ) ) \leq - 1$ it follows from the matrix-valued theorem of von Neumann (Theorem V.7.8) that

$$
\big \| \big ( \kappa I - A \otimes g _ { z } ( \eta , \zeta ) \big ) ^ { - 1 } \big \| \leq \operatorname* { m a x } _ { \mathrm { R e } \mu \leq - 1 } \| ( \kappa I - \mu A ) ^ { - 1 } \| .
$$

The right-hand side of (3.46) is bounded by a constant independent of $r _ { i } \geq 0$ ,bccause the eigenvalues of $A$ are assumed to have positive real part. Consequently, also the inverse of (3.45) is uniformly bounded for $\varepsilon > 0$ and $l _ { l } \le h _ { 0 }$ . This together with $g \left( \uparrow \jmath , \zeta \right) = \mathcal { O } \left( h \right)$ implies that the first increment (of Newton's method) is of size $\mathcal { O } ( h )$ .Hence, for sufficiently small $h$ , the Ncwton-Kantorovich assumptions are fulfilled. □

# Influence of Perturbations

For the perturbed Runge-Kutta method

$$
\binom { \widehat { Y } _ { \scriptscriptstyle 2 } - \widehat { \eta } } { \varepsilon ( \widehat { Z } _ { \scriptscriptstyle 1 } - \widehat { \zeta } ) } = h \sum _ { \scriptscriptstyle 2 = 1 } ^ { s } a _ { \scriptscriptstyle 1 \jmath } \left( { f ( \widehat { Y } _ { \scriptscriptstyle \jmath } , \widehat { Z } _ { \scriptscriptstyle \jmath } ) } \right) + h \left( { \delta _ { \scriptscriptstyle \imath } } \right)
$$

we have the following result.

Theorem 3.6 (Hairer, Lubich & Roche 1988). Let $Y _ { \imath } , Z _ { \imath }$ be given by (3.43) and consider perturbed values ${ \widehat { Y } } _ { \imath } , { \widehat { Z } } _ { \imath }$ satisfying (3.47). In addition to the assumptions of Theorem 3.5 suppose that $\widehat { \eta } - \eta = \mathcal { O } ( h )$ ， $\widehat { \zeta } - \zeta = \mathcal { O } ( h )$ ， $\delta _ { \mathfrak { \imath } } = \mathcal { O } ( { \mathfrak { 1 } } )$ ,and $\theta _ { \imath } =$ $\mathcal O ( h )$ . Then we have for $h \leq h _ { 0 }$

$$
\begin{array} { r l } & { \| \widehat { Y } _ { \iota } - Y _ { \iota } \| \leq C ( \| \widehat { \eta } - \eta \| + \varepsilon \| \widehat { \zeta } - \zeta \| ) + h C ( \| \delta \| + \| \theta \| ) } \\ & { \| \widehat { Z } _ { \iota } - Z _ { \iota } \| \leq C ( \| \widehat { \eta } - \eta \| + \frac { \varepsilon } { h } \| \widehat { \zeta } - \zeta \| ) + C ( h \| \delta \| + \| \theta \| ) . } \end{array}
$$

Here $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { s } ) ^ { T }$ and $\boldsymbol { \theta } = ( \theta _ { 1 } , \ldots , \theta _ { s } ) ^ { T }$ ·

Proof. The essential idea is to consider the homotopy

$$
\left( { { Y } _ { \iota } } - \eta \atop \varepsilon ( { \boldsymbol { Z } _ { i } } - \zeta ) \right) - h \sum _ { \jmath = 1 } ^ { s } { { a } _ { \iota _ { \boldsymbol { \jmath } } } } \left( { { f } ( { \boldsymbol { Y } } _ { \boldsymbol { \jmath } } , { \boldsymbol { Z } } _ { \boldsymbol { \jmath } } ) } \right) = \tau \left( \begin{array} { c } { \widehat { \eta } - \eta + h { \delta } _ { \iota } } \\ { \varepsilon ( \widehat { \zeta } - \zeta ) + h { \theta } _ { \iota } } \end{array} \right)
$$

which relates the system (3.43) for $\tau = 0$ to the perturbed system (3.47) for $\tau \approx 1$ . The solutions $Y _ { \imath }$ and $Z _ { \imath }$ of (3.49) are functions of $\tau$ . If we differentiate (3.49) with respect to $\tau$ and divide its second formula by $h$ ，we obtain the differential equation

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { M ( \varepsilon / h , Y , Z ) } \end{array} \right) \left( \begin{array} { c } { \dot { Y } } \\ { \dot { Z } } \end{array} \right) = \left( \begin{array} { c } { \mathbb { 1 } \cdot ( \widehat { \eta } - \eta ) + h \delta } \\ { ( \varepsilon / h ) \mathbb { 1 } \cdot ( \widehat { \zeta } - \zeta ) + \theta } \end{array} \right)
$$

where $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T } , Y = ( Y _ { 1 } , \ldots , Y _ { s } ) ^ { T } , Z = ( Z _ { 1 } , \ldots , Z _ { s } ) ^ { T }$ and

$$
M ( \kappa , Y , Z ) = \kappa I - A \otimes I \cdot \left( \begin{array} { c c c } { { g _ { z } ( Y _ { 1 } , Z _ { 1 } ) } } & { { } } & { { 0 } } \\ { { } } & { { \ddots } } & { { } } \\ { { 0 } } & { { } } & { { g _ { z } ( Y _ { s } , Z _ { s } ) } } \end{array} \right) .
$$

Whenever $\| Y _ { \imath } - \eta \| \leq d$ and $\| Z _ { \iota } - \zeta \| \leq d$ for all $i$ , we have

$$
M ( \kappa , Y , Z ) = \kappa I - A \otimes g _ { z } ( \eta , \zeta ) + { \mathcal O } ( d )
$$

and it follows from (3.46) that $M ^ { - 1 } ( \kappa , Y , Z )$ is uniformly bounded for $\kappa \geq 0$ ,if $d$ is sufficiently small. Hence,the inverse of the matrix in (3.50) satisfies

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { M ( \varepsilon / h , Y , Z ) } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { \mathcal { O } ( 1 ) } \end{array} \right)
$$

and the statement (3.48) follows from the fact that

$$
{ \widehat { Y } } - Y = \int _ { 0 } ^ { 1 } { \dot { Y } } ( \tau ) d \tau , \qquad { \widehat { Z } } - Z = \int _ { 0 } ^ { 1 } { \dot { Z } } ( \tau ) d \tau .
$$

Remark 3.7. If the Runge-Kutta matrix $A$ is only assumed to be invertible, the results of Theorems 3.5 and 3.6 still hold for $\varepsilon \leq \bar { K } \bar { h }$ ，where $\bar { \Lambda } ^ { \gamma }$ is any constant smaller than the modulus of the smallest eigenvalue of $A$ (i.e., $K ^ { \prime } < | \lambda _ { \operatorname* { m i n } } | )$ .In this situation, the right-hand side of (3.48) is also bounded,and the same conclusions hold.

# Estimation of the Remainder in the Numerical Solution

We are now in the position to estimate the remainder in (3.29). The result is the following.

Theorem 3.8 (Hairer, Lubich & Roche 1988). Consider the stiff problem (3.1), (3.11) with initial values $y ( 0 )$ ， $\approx ( 0 )$ admitting $a$ smooth solution. Apply the Runge-Kutta method (3.22)-(3.24) of classical order $p$ and stage order $q$ $( 1 \leq q < p )$ Assume that the method is $A$ -stable, that the stability function satisfies $| R ( \infty ) | < 1$ ， and that the eigenvalues of the coefficient matrix $A$ have positive real part. Then for any fixed constant $c > 0$ the global error satisfies for $\varepsilon \leq c h$ and $\nu \leq q + 1$

$$
\begin{array} { r l } & { y _ { n } - y ( x _ { n } ) = \Delta y _ { n } ^ { 0 } + \varepsilon \Delta y _ { n } ^ { 1 } + . . . + \varepsilon ^ { \nu } \Delta y _ { n } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { z _ { n } - z ( x _ { n } ) = \Delta z _ { n } ^ { 0 } + \varepsilon \Delta z _ { n } ^ { 1 } + . . . + \varepsilon ^ { \nu } \Delta z _ { n } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) . } \end{array}
$$

Here $\Delta y _ { n } ^ { 0 } = y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) , \ \Delta z _ { n } ^ { 0 } = z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) , . . .$ (see Formulu (3.32)) are the global errors of the method applied to the system (3.4). The estimates (3.53) hold uniformly for ${ \boldsymbol { h } } \leq h _ { 0 }$ and $r \ i h \le C o n s t$

Proof. By Theorem 3.4 it suffices to prove the result for $\nu = q + 1$ . We denote thc truncated series of (3.25) by

$$
\begin{array} { c } { { \widehat { y } _ { n } = y _ { n } ^ { 0 } + \varepsilon y _ { n } ^ { 1 } + \ldots + \varepsilon ^ { \nu } y _ { n } ^ { \prime \prime } } } \\ { { { } } } \\ { { { \widehat { Y } } _ { n \imath } = Y _ { n \imath } ^ { 0 } + \varepsilon Y _ { n \imath } ^ { - 1 } + \ldots + \varepsilon ^ { \nu } Y _ { n \imath } ^ { \nu } } } \\ { { { } } } \\ { { { \widehat { k } } _ { n \imath } = k _ { n \imath } ^ { 0 } + \varepsilon k _ { n \imath } ^ { 1 } + \ldots + \varepsilon ^ { \nu } k _ { n \imath } ^ { \nu } } } \end{array}
$$

and similarly ${ \widehat { z } } _ { n } , { \widehat { Z } } _ { n \imath } , { \widehat { \ell } } _ { n \imath }$ . Further we denote

$$
\Delta y _ { n } = { \widehat { y } } _ { n } - y _ { n } , \qquad \Delta Y _ { n \ i } = { \widehat { Y } } _ { n \ i } - Y _ { n \ i } , \qquad \Delta k _ { n \ i } = { \widehat { k } } _ { n \ i } - k _ { n i } , \dots
$$

Using (3.3) and Theorem 3.4 the statement (3.53) is then equivalent to

$$
\Delta y _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) , \qquad \Delta z _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

a) We first estimate the differences $\Delta Y _ { n i } , \Delta Z _ { n \imath }$ of the internal stages. For this we investigate the defect when (3.54) is inserted into (3.23). By our construction (3.28) it follows from (3.42) and $\nu = q + 1$ that

$$
\begin{array} { r l } & { \widehat { k } _ { n \iota } = f ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { \varepsilon \widehat { \ell } _ { n \iota } = g ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) + \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

From (3.42) and (3.27) we know that $\ell _ { n \ i } ^ { \nu } = \mathcal { O } ( h ^ { - 1 } )$ .Together with (3.27) this implies

$$
\left( \begin{array} { c } { \widehat { Y } _ { n \ i } - \widehat { y } _ { n } } \\ { \varepsilon ( \widehat { Z } _ { n \ i } - \widehat { z } _ { n } ) } \end{array} \right) = h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \left( \begin{array} { c } { f ( \widehat { Y } _ { n j } , \widehat { Z } _ { n \jmath } ) } \\ { g ( \widehat { Y } _ { n \jmath } , \widehat { Z } _ { n \jmath } ) } \end{array} \right) + \left( \begin{array} { c } { \mathcal { O } ( h \varepsilon ^ { \nu + 1 } ) } \\ { \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \end{array} \right) ,
$$

which is of the form (3.47). Application of Theorem 3.6 yields

$$
\begin{array} { r l } & { \| \Delta Y _ { n \imath } \| \leq C ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { \| \Delta Z _ { n \imath } \| \leq C ( \| \Delta y _ { n } \| + \displaystyle \frac { \varepsilon } { h } \| \Delta z _ { n } \| ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) } \end{array}
$$

provided that $\Delta y _ { n }$ and $\Delta z _ { n }$ are of size ${ \mathcal { O } } ( h )$ . This will be justifed in part (c).

b) Our next aim is to prove the recursion

$$
\begin{array} { r } { \left( \left. \Delta y _ { n + 1 } \right. \right) \leq \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( \varepsilon ) } \\ { \mathcal { O } ( 1 ) } & { \alpha + \mathcal { O } ( \varepsilon ) } \end{array} \right) \left( \left. \Delta y _ { n } \right. \right) + \left( \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) \right) } \end{array}
$$

where we assume again that $\Delta y _ { n }$ and $\Delta z _ { n }$ are of size $\mathcal O ( h )$ . The value $\alpha < 1$ will be given in Formula (3.63) below. The upper relation of (3.60) follows from

$$
\Delta y _ { n + 1 } = \Delta y _ { n } + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \Big ( f ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) - f ( Y _ { n \iota } , Z _ { n \iota } ) \Big ) + \mathscr { O } ( h \varepsilon ^ { \nu + 1 } )
$$

by the use of (3.59) and a Lipschitz condition for $f$ ·

For the verification of the second relation in (3.60) we subtract (3.57) from (3.23),and use (3.59) and (3.42) to obtain

$$
\varepsilon \Delta \ell _ { n \iota } = g _ { z } ( x _ { n } ) \Delta Z _ { n \iota } + { \mathcal O } ( \| \Delta Y _ { n \iota } \| + h \| \Delta Z _ { n \iota } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

Here we use the notation $g _ { z } ( x ) = g _ { z } ( y _ { 0 } ( x ) , z _ { 0 } ( x ) )$ Inserting $\Delta Z _ { n \imath } = \Delta z _ { n \imath } +$ $\boldsymbol { h } \sum \boldsymbol { a } _ { \iota \jmath } \Delta \ell _ { n \jmath }$ into this relation and using (3.59) again we obtain

$$
\varepsilon \Delta \ell _ { n \ i } - h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } g _ { \boldsymbol z } ( { \boldsymbol x } _ { n } ) \Delta \ell _ { n \jmath } = g _ { \boldsymbol z } ( { \boldsymbol x } _ { n } ) \Delta z _ { n } + { \mathcal O } ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

We now solve for $h \Delta \ell _ { n \imath }$ and insert it into $\begin{array} { r } { \Delta z _ { n + 1 } = \Delta z _ { n } + h \sum b _ { \imath } \Delta \ell _ { n \imath } } \end{array}$ . Since the matrix $( \varepsilon / h ) I - A \otimes g _ { z } ( x _ { n } )$ has a bounded inverse by (3.46), this gives

$$
\Delta z _ { n + 1 } = R \Big ( \frac { h } { \varepsilon } g _ { z } ( x _ { n } ) \Big ) \Delta z _ { n } + { \mathcal O } ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) ,
$$

where $R ( \mu )$ is the stability function of the method. Because of (3.11) we can apply von Neumann $\mathbf { \dot { s } }$ theorem (Corollary IV.11.4) to estimate

$$
\left\| R { \Big ( } { \frac { h } { \varepsilon } } g _ { z } ( x _ { n } ) { \Big ) } \right\| \leq \operatorname* { s u p } \{ | R ( \mu ) | ; \operatorname { R e } \mu \leq - h / \varepsilon \} \leq \alpha < 1 .
$$

The bound $\alpha$ is strictly smaller than 1,because $| R ( \infty ) | < 1$ and $- h / \varepsilon \le - 1 / c < 0$ The triangle inequality applied to (3.62) completes the proof of Formula (3.60).

c) Applying Lemma 3.9 below to the difference inequality (3.60) gives

$$
\Delta y _ { n } = { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) , \qquad \Delta z _ { n } = { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h )
$$

for $n h \leq C o n s t$ . We are now in a position to justify the assumption $\Delta y _ { n } = \mathcal { O } ( h )$ and $\Delta z _ { n } = \mathcal { O } ( h )$ of the beginning of the proof. Indeed, this follows by induction on $n$ $( \Delta y _ { 0 } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$ ， $\Delta z _ { 0 } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) )$ and from (3.64), because $\nu = q + 1 \ge 2$

d) Formula (3.64) proves the desired result (3.56) for the $z$ -component. However, the estimate (3.64) is not yet optimal for the $y$ -component. The proof for the correct estimate is similar to that of Theorem 3.4. We have to treat more carefully the expression which gives rise to the ${ \mathcal O } ( \varepsilon ^ { \nu + 1 } / h )$ term in (3.61). Using (3.59) and (3.64) the same calculations which gave (3.61), now yield

$$
\begin{array} { c } { \Delta k _ { n \ i } = f _ { y } ( x _ { n } ) \Delta Y _ { n \ i } + f _ { z } ( x _ { n } ) \Delta Z _ { n \ i } + \mathcal O ( \varepsilon ^ { \nu + 1 } ) } \\ { \varepsilon \Delta \ell _ { n \ i } = g _ { y } ( x _ { n } ) \Delta Y _ { n \ i } + g _ { z } ( x _ { n } ) \Delta Z _ { n \ i } + \varepsilon ^ { \nu + 1 } \ell _ { n \ i } ^ { \nu } + \mathcal O ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

We compute $\Delta Z _ { n \imath }$ from (3.65b) and insert it into (3.65a). This gives

$$
\begin{array} { r l } & { \qquad \Delta k _ { n \iota } - \bigl ( f _ { z } g _ { z } ^ { - 1 } \bigr ) ( x _ { n } ) \bigl ( \varepsilon \Delta \ell _ { n \iota } - \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } \bigr ) } \\ & { \qquad = \bigl ( f _ { y } - f _ { z } g _ { z } ^ { - 1 } g _ { y } \bigr ) ( x _ { n } ) \Delta Y _ { n \iota } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

Guided by this formula we put

$$
\Delta u _ { n } = \Delta y _ { n } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \big ( \varepsilon \Delta z _ { n } - \varepsilon ^ { \nu + 1 } z _ { n } ^ { \nu } \big ) .
$$

Since

$$
\begin{array} { r l r } {  { \Delta u _ { n + 1 } = \Delta u _ { n } + h \sum _ { \iota = 1 } ^ { s } \underline { b } _ { \iota } \Big ( \Delta k _ { n \iota } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \big ( \varepsilon \Delta \ell _ { n \iota } - \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } \big ) \Big ) } } \\ & { } & { \qquad - ( ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + h ) - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) ) ( \varepsilon \Delta z _ { n + 1 } - \varepsilon ^ { \nu + 1 } z _ { n + 1 } ^ { \nu } ) } \end{array}
$$

it follows from (3.66),(3.64),and (3.42) that

$$
\begin{array} { r } { \| \Delta u _ { n + 1 } \| \leq ( 1 + c h ) \| \Delta u _ { n } \| + \mathcal { O } ( h \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

As in the proof of Theorem 3.4 we deduce $\Delta u _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$ and $\Delta y _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$

In the above proof we used the following result.

Lemma 3.9. Let $\{ u _ { n } \}$ ， $\{ v _ { n } \}$ be two sequences of non-negative numbers satisfying (componentwise)

$$
\begin{array} { r } { \left( \begin{array} { c } { u _ { n + 1 } } \\ { v _ { n + 1 } } \end{array} \right) \leq \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( \varepsilon ) } \\ { \mathcal { O } ( 1 ) } & { \alpha + \mathcal { O } ( \varepsilon ) } \end{array} \right) \left( \begin{array} { c } { u _ { n } } \\ { v _ { n } } \end{array} \right) + M \left( \begin{array} { c } { h } \\ { 1 } \end{array} \right) } \end{array}
$$

with $0 \leq \alpha < 1$ and $M \geq 0$ . Then the following estimates hold for $\varepsilon \leq c h , h \leq h _ { 0 }$ and $n h \le C o n s t$

$$
\begin{array} { r l } & { u _ { n } \leq C ( u _ { 0 } + \varepsilon v _ { 0 } + M ) } \\ & { v _ { n } \leq C ( u _ { 0 } + ( \varepsilon + \alpha ^ { n } ) v _ { 0 } + M ) . } \end{array}
$$

Proof. We transform the matrix in (3.69) to diagonal form and so obtain

$$
\left( \begin{array} { c } { u _ { n } } \\ { v _ { n } } \end{array} \right) \leq T ^ { - 1 } \left( \begin{array} { c c } { \lambda _ { 1 } ^ { n } } & { 0 } \\ { 0 } & { \lambda _ { 2 } ^ { n } } \end{array} \right) T \left( \begin{array} { c } { u _ { 0 } } \\ { v _ { 0 } } \end{array} \right) + M \sum _ { \jmath = 1 } ^ { n } T ^ { - 1 } \left( \begin{array} { c c } { \lambda _ { 1 } ^ { n - \jmath } } & { 0 } \\ { 0 } & { \lambda _ { 2 } ^ { n - \jmath } } \end{array} \right) T \left( \begin{array} { c } { h } \\ { 1 } \end{array} \right)
$$

where $\lambda _ { 1 } = 1 + \mathcal { O } ( h ) , \lambda _ { 2 } = \alpha + \mathcal { O } ( \varepsilon )$ are the eigenvalues and the transformation matrix $T$ (composed of eigenvectors) satisfies

$$
T = \left( \begin{array} { c c } { { 1 } } & { { \mathcal { O } ( \varepsilon ) } } \\ { { \mathcal { O } ( 1 ) } } & { { 1 } } \end{array} \right) .
$$

The statement now follows from the fact that $( \alpha + \mathcal { O } ( \varepsilon ) ) ^ { n } = \mathcal { O } ( \alpha ^ { n } ) + \mathcal { O } ( \varepsilon )$ for $\varepsilon \leq c h$ and $n h \le C o n s t$ □

By combining Theorems 3.3,3.4 and 3.8 we get the following result.

Corollary 3.10 (Hairer, Lubich & Roche 1988). Under the assumptions of Theorem 3.8 the global error of a Runge-Kutta method satisfies

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon h ^ { q + 1 } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { q + 1 } ) .
$$

If in addition $a _ { s _ { 1 } } = b _ { \ i }$ for all $i$ , we have

$$
z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon h ^ { q } ) .
$$

Remarks. a) If the $A$ -stability assumption is dropped and the coefficient matrix $A$ is only assumed to be invertible, then the estimates of Corollary 3.10 still hold for $\varepsilon \leq \bar { k } \tilde { h }$ where $\bar { k } ^ { \ast }$ is a method-dependent constant (see Remark 3.7).

b) $A$ -stability and the invertibility of the matrix $A$ imply in general that the eigenvalues of $A$ have positive real part. Otherwise the stability function would have to be reducible.

c) For several Runge-Kutta methods satisfying $a _ { s _ { 1 } } = b _ { \ i }$ the estimate (3.71) for the $y$ -component can be improved. E.g., for Radau IIA and for Lobatto IIC one has $y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon ^ { 2 } h ^ { q } )$ . This follows from Table VII.4.1 below.

d) A completely different proof of the estimates (3.71) is given by Nipp & Stoffer (1995). They show that the Runge-Kutta method, considered as a discrete

dynamical system, admits an attractive invariant manifold $M _ { h , \varepsilon }$ ， which is close to the invariant manifold $M _ { \varepsilon }$ of the problem (3.1). Studying the closeness of the two manifolds, they obtain the error estimates (3.71) without considering $\varepsilon$ -expansions.

e) The analogues of Theorem 3.8 and Corollary 3.10 for Rosenbrock methods are given in Hairer,Lubich & Roche (1989).

f) Estimates for $p = q$ are given in Exercise 3 below.

# Numerical Confirmation

The estimates of Corollary 3.10 can be observed numerically. As an example of (3.1) we choose the van der Pol equation

$$
\begin{array} { c } { { y ^ { \prime } = z } } \\ { { \varepsilon z ^ { \prime } = ( 1 - y ^ { 2 } ) z - y } } \end{array}
$$

with $\varepsilon = 1 0 ^ { - 5 }$ and initial values

$$
y ( 0 ) = 2 , \qquad z ( 0 ) = - 0 . 6 6 6 6 5 4 3 2 1 1 2 1 1 7 2
$$

on the smooth solution (Exercise 2).

Table 3.1 shows the methods of our experiment together with the theoretical error bounds. In Fig.3.1 we have plotted the relative global error at $x _ { e n d } = 0 . 5$ as a function of the step size $h$ ，which was taken constant over the considered interval. The use of logarithmic scales in both directions makes the curves appear as straight lines of slope $\mathscr { r }$ ， whenever the leading term of the global error behaves like $C o n s t \cdot h ^ { r }$ . The figures show complete agreement with our theoretical results.

Table 3.1. Global errors predicted by Corollary 3.10   

<table><tr><td>Method</td><td>ag=b</td><td>y -comp.</td><td>z -comp.</td></tr><tr><td>Radau IA</td><td>no</td><td>h2s-1+eh8</td><td>h</td></tr><tr><td>Radau IIA</td><td>yes</td><td>h2g-1+e²h8</td><td>h2s-1+eh</td></tr><tr><td>Lobatto IIIC</td><td>yes</td><td>h2s-2+e²h8-1</td><td>h²s-2+eh8-1</td></tr><tr><td>SDIRK (IV.6.16)</td><td>yes</td><td>h4+h²</td><td>h4+εh</td></tr><tr><td>SDIRK (IV.6.18)</td><td>no</td><td>h4+h²</td><td>h2</td></tr></table>


<!-- chunk 0007: pages 421-490 -->
![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/786029a6dcb5d648daf5ca5bdd696139bb039e6fa2a0a36444966a1b12465ecb.jpg)  
Fig.3.1. Global error versus the step size

# Perturbed Initial Values

When integrating a singular perturbation problem, the numerical solution approximates the smooth solution only within the given tolerance $T o l$ . It is therefore interesting to investigate the influence of perturbations in the initial values on the global and local errors of the method. Let us begin with a numerical experiment. We perturb the $z ( 0 )$ value of (3.74) by an amount of $1 0 ^ { - 6 }$ and apply the Radau IIA methods to the problem (3.73). For the global error at ${ x _ { e n d } } \mathrm { = } 0 . 5$ we obtain ex-actly the same results as in Fig.3.1. This shows that the perturbation is completely damped out during integration. The results for the local error show a different behaviour and are displayed in Fig.3.2. We observe the presence of a“hump",exactly as in Fig.IV.7.4 and in Fig.IV.8.2.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/f250347c703cb18d954b7b01d6efd6b0625694e7fa872f340d9a2e9d6893b533.jpg)  
Fig.3.2. Local error of Radau IA (perturbed initial value)

In order to explain this phenomenon we denote by $( y _ { 0 } , z _ { 0 } )$ the considered initial value, and by $( y _ { 1 } , z _ { 1 } )$ the numerical solution after one step with step size $h$ . The exact solution $y ( x ) , z ( x )$ passing through $( y _ { 0 } , z _ { 0 } )$ will have a boundary layer, and (under suitable assumptions, see Theorem 3.2) can be written as

$$
y ( x ) = \widetilde { y } ( x ) + \mathcal { O } ( \varepsilon e ^ { - x / \varepsilon } ) , \qquad z ( x ) = \widetilde { z } ( x ) + \mathcal { O } ( e ^ { - x / \varepsilon } ) .
$$

Here $\widetilde { y } ( \boldsymbol { x } ) , \widetilde { z } ( \boldsymbol { x } )$ represents a smooth solution of (3.1). We denote by $\widetilde { y } _ { 0 } = \widetilde { y } ( 0 )$ ， $\widetilde { z } _ { 0 } = \widetilde { z } ( 0 )$ the initial values on this smooth solution, and by $( \widetilde { y } _ { 1 } , \widetilde { z } _ { 1 } )$ the numerical approximation obtained by the same method with step size $h$ and initial values $( \widetilde { y } _ { 0 } , \widetilde { z } _ { 0 } )$ . The local error can now be written as

$$
z _ { 1 } - z ( h ) = ( z _ { 1 } - \widetilde { z } _ { 1 } ) + ( \widetilde { z } _ { 1 } - \widetilde { z } ( h ) ) + ( \widetilde { z } ( h ) - z ( h ) )
$$

and similarly for the $y$ -component. The last term in (3.76)，which is of size $\mathcal { O } ( T o l \cdot e ^ { - h / \varepsilon } )$ , can be neglected if the step size $h$ is significantly larger than $\varepsilon$ The term $\widetilde { z } _ { 1 } - \widetilde { z } ( h )$ represents the local error in the “smooth” situation and is bounded by at least $\mathcal { O } ( h ^ { q + 1 } )$ (apply Corollary 3.10 with $n = 1$ ). It can be observed in Fig.3.2 whenever $h$ or the error is large. The difference $z _ { 1 } - \widetilde { z } _ { 1 }$ is the term which causes the irregularity in Fig.3.2. Using Theorem 3.6 (with $\delta = 0$ ， $\theta = 0$ ， $\widehat { \eta } - \eta = \mathcal { O } ( \varepsilon \cdot T o l )$ ， $\begin{array} { r } { \widehat { \zeta } - \zeta = \mathcal { O } ( T o l ) , } \end{array}$ and the ideas of the proof of Theorem 3.8 (in particular Eq.(3.62)) we obtain

$$
\begin{array} { r l } & { z _ { 1 } - \widetilde { z } _ { 1 } = R \Big ( \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ( z _ { 0 } - \widetilde { z } _ { 0 } ) + \mathcal { O } ( \varepsilon \cdot T o l ) } \\ & { y _ { 1 } - \widetilde { y } _ { 1 } = \mathcal { O } ( \varepsilon \cdot T o l ) . } \end{array}
$$

For $\varepsilon < h$ we develop

$$
R \Bigl ( { \frac { h } { \varepsilon } } g _ { z } ( 0 ) \Bigr ) = R ( \infty ) + C { \frac { \varepsilon } { h } } g _ { z } ^ { - 1 } ( 0 ) + { \mathcal { O } } \Bigl ( \Bigl ( { \frac { \varepsilon } { h } } \Bigr ) ^ { 2 } \Bigr ) .
$$

This shows that an $h$ -independent expression $R ( \infty ) ( z _ { 0 } - \widetilde { z } _ { 0 } ) = \mathcal { O } ( T o l )$ will be observed in the local error, if $R ( \infty ) \neq 0$ . For methods with $R ( \infty ) = 0$ (such as Radau IA) the dominant part in $z _ { 1 } - \widetilde { z } _ { 1 }$ is $C ( \varepsilon / h ) g _ { z } ^ { - 1 } ( 0 ) ( z _ { 0 } - \widetilde { z _ { 0 } } ) = \mathcal { O } ( T o l \cdot \varepsilon / h )$ This term can be observed in Fig.3.2 as a straight line of slope $- 1$ . Thus in this region the local error increases like $h ^ { - 1 }$ when $h$ decreases. A similar perturbation, multiplied however by $\varepsilon$ , is observed for the $y$ -component.

This is not a serious drawback for a numerical implementation, because the phenomenon appears only for step sizes where the local error is smaller than $T o l$

# Exercises

1. Prove that the statement of Theorem 3.2 remains valid,if the assumption (3.11) is replaced by

for all $y , z$ in a neighbourhood of the solution $y _ { 0 } ( x ) , ~ z _ { 0 } ( x )$ of the reduced system.

Hint. Split the interval into a finite number of small subintervals and construct for each of them an inner product norm such that, after a rescaling of $\varepsilon$ ,(3.11) holds (see Nevanlinna 1976).

2. Let $y ( 0 ) = 2$ ; find the corresponding $z ( 0 )$ for the van der Pol equation (3.73), such that its solution is smooth.

Result.

$$
z ( 0 ) = - { \frac { 2 } { 3 } } + { \frac { 1 0 } { 8 1 } } \varepsilon - { \frac { 2 9 2 } { 2 1 8 7 } } \varepsilon ^ { 2 } - { \frac { 1 8 1 4 } { 1 9 6 8 3 } } \varepsilon ^ { 3 } + { \mathcal { O } } ( \varepsilon ^ { 4 } ) .
$$

3. If the assumption $q < p$ $p$ classical order, $q$ stage order) is dropped in Corollary 3.10, we still have

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) .
$$

Prove this statement. The implicit Euler method and the SIRK methods of Lemma IV.8.1 are typical examples with $p \approx q$

Hint. Apply Corollary 3.10 with $q$ reduced by 1.

This section is devoted to the extension of Rosenbrock methods (see Sect.IV.7) to differential-algebraic equations in semi-explicit form

$$
\begin{array} { r } { { \boldsymbol { y } } ^ { \prime } = f ( { \boldsymbol { y } } , z ) , \qquad { \boldsymbol { y } } ( { \boldsymbol { x } } _ { 0 } ) = { \boldsymbol { y } } _ { 0 } } \\ { 0 = g ( { \boldsymbol { y } } , z ) , \qquad z ( { \boldsymbol { x } } _ { 0 } ) = z _ { 0 } . } \end{array}
$$

We suppose that $g _ { z }$ is invertible (see (1.7))，so that the problem is of index 1. We shall obtain new methods for the numerical solution of such problems,and at the same time get more insight into the behaviour of Rosenbrock methods for stiff differential equations. In particular, the phenomenon of Fig.IV.7.4 will be explained.

# Definition of the Method

The main advantage of Rosenbrock methods over implicit Runge-Kutta methods is that nonlinear systems are completely avoided. The state space form method (transforming (4.1) to $y ^ { \prime } = f ( y , G ( y ) )$ ） would destroy this advantage. This is one more reason for considering the $\varepsilon$ -embedding method. For the problem (1.5）a Rosenbrock method reads

$$
\binom { k _ { z } } { \ell _ { \ast } } = h \left( { \begin{array} { c } { f ( v _ { \ast } , w _ { \iota } ) } \\ { \varepsilon ^ { - 1 } g ( v _ { \ast } , w _ { \iota } ) } \end{array} } \right) + h \left( { \begin{array} { c c } { f _ { y } } & { f _ { z } } \\ { \varepsilon ^ { - 1 } g _ { y } } & { \varepsilon ^ { - 1 } g _ { z } } \end{array} } \right) ( y _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \imath _ { \jmath } } \binom { k _ { \jmath } } { \ell _ { \jmath } }
$$

$$
\left( \begin{array} { l } { { v _ { \mathfrak { _ { \lambda } } } } } \\ { { w _ { \mathfrak { _ { \lambda } } } } } \end{array} \right) = \left( \begin{array} { l } { { y _ { 0 } } } \\ { { z _ { 0 } } } \end{array} \right) + \sum _ { \substack { \jmath = 1 } } ^ { \imath - 1 } \alpha _ { \mathfrak { _ { \imath } } \jmath } \left( \begin{array} { l } { { k _ { \jmath } } } \\ { { \ell _ { \jmath } } } \end{array} \right) , \qquad \left( \begin{array} { l } { { y _ { 1 } } } \\ { { z _ { 1 } } } \end{array} \right) = \left( \begin{array} { l } { { y _ { 0 } } } \\ { { z _ { 0 } } } \end{array} \right) + \sum _ { \substack { \imath = 1 } } ^ { s } b _ { \imath } \left( \begin{array} { l } { { k _ { \jmath } } } \\ { { \ell _ { \imath } } } \end{array} \right) .
$$

If we multiply the second line of (4.2) by $\varepsilon$ and then put $\varepsilon = 0$ we obtain

$$
\left( \begin{array} { l } { k _ { \ i } } \\ { 0 } \end{array} \right) = h \left( \begin{array} { l } { f ( v _ { \ i } , w _ { \iota } ) } \\ { g ( v _ { \iota } , w _ { \iota } ) } \end{array} \right) + h \left( \begin{array} { l l } { f _ { y } } & { f _ { z } } \\ { g _ { y } } & { g _ { z } } \end{array} \right) ( y _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \iota _ { \jmath } } \left( \begin{array} { l } { k _ { \jmath } } \\ { \ell _ { \jmath } } \end{array} \right) .
$$

Formulas (4.3a) and (4.3b) together constitute the extension of a Rosenbrock method to the problem (4.1). This type of method was first considered by Michelsen (1976) (quoted by Feng, Holland & Gallun (1984)). Further studies are due to Roche

(1988). We remark that the computation of $( k _ { \imath } , \ell _ { i } )$ from (4.3b) requires the solu-tion of a linear system with matrix

$$
\left( \begin{array} { c c } { I - \gamma h f _ { y } } & { - \gamma h f _ { z } } \\ { - \gamma h g _ { y } } & { - \gamma h g _ { z } } \end{array} \right)
$$

where all derivatives are evaluated at $( y _ { 0 } , z _ { 0 } )$ . For nonsingular $g _ { z }$ , nonzero $\gamma$ ,and small enough $h > 0$ ,this matrix is invertible. This can be seen by dividing the lower blocks by $\gamma h$ and then putting $h = 0$

Non-autonomous equations. If the functions $f$ and $g$ in (4.1) also depend on $\boldsymbol { \mathscr { x } }$ ， we replace (4.3b) by

$$
\left( { \begin{array} { c } { k _ { _ { 1 } } } \\ { 0 } \end{array} } \right) = h \left( { \begin{array} { c } { f ( x _ { _ { 0 } } + \alpha _ { _ { 1 } } h , v _ { _ { 1 } } , w _ { _ { 1 } } ) } \\ { g ( x _ { _ { 0 } } + \alpha _ { _ { 1 } } h , v _ { _ { 1 } } , w _ { _ { 1 } } ) } \end{array} } \right) + h \left( { \begin{array} { c c } { f _ { _ { y } } } & { f _ { z } } \\ { g _ { _ { y } } } & { g _ { z } } \end{array} } \right) \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { _ { 1 } \jmath } \left( { k _ { \jmath } \atop \ell _ { \jmath } } \right) + h ^ { 2 } \gamma _ { _ { 1 } } \left( { f _ { _ { x } } } \right)
$$

(compare with (IV.7.4a) and recall the definition of $\alpha _ { \iota }$ and $\gamma _ { \imath }$ in (IV.7.5)). All derivatives are evaluated at the initial value $\left( x _ { 0 } , y _ { 0 } , z _ { 0 } \right)$

Problems of the form $M u ^ { \prime } = \varphi ( u )$ . Rosenbrock formulas for these problems have been developed in Sect.IV.7 (Formula (IV.7.4b)) in the case of regular $M$ . This formula is also applicable for singular $M$ ，and can be justified as follows: It is theoretically possible to apply the transformation（1.2O) so that $M$ becomes the block-diagonal matrix with entries $I$ and O. The method (IV.7.4b) is then identical to method (4.3). Therefore, the theory to be developed in this section will also be valid for Rosenbrock method (IV.7.4b) applied to index 1 problems of the form $M u ^ { \prime } = \varphi ( u )$

Having introduced a new class of methods,we must study their order conditions. As usual, this is done by Taylor expansion of both the exact and the numerical solution (similar to Section I.2). A nice correspondence between the order condi-tions and certain rooted trees with two different kinds of vertices will be obtained (Roche 1988).

# Derivatives of the Exact Solution

In contrast to Sect.II.2, where we used “hordes of indices" (see Dieudonné's preface to his “Foundations of Modern Analysis"） to show us the way through the “woud met bomen” (Hundsdorfer), we here write higher derivatives as multilinear mappings. For example, the expression

$$
\sum _ { \ j , k } \frac { \partial ^ { 2 } g _ { i } } { \partial y _ { \ j } \partial z _ { k } } \cdot u _ { \ j } v _ { k } \quad \mathrm { \ i s { w r i t t e n } { a s } } \quad g _ { y z } ( u , \upsilon ) ,
$$

which simplifies the subsequent formulas.

We differentiate (4.1b) to obtain $0 = g _ { y } \cdot y ^ { \prime } + g _ { z } \cdot z ^ { \prime }$ and, equivalently,

$$
z ^ { \prime } = ( - g _ { z } ^ { - 1 } ) g _ { y } f .
$$

We now differentiate successively (4.1a) and (4.6) with respect to $\boldsymbol { \mathscr { x } }$ . We use the formula

$$
( - g _ { z } ^ { - 1 } ) ^ { \prime } u = \left( - g _ { z } ^ { - 1 } \right) \left( g _ { z y } { \left( \bigl ( - g _ { z } ^ { - 1 } \bigr ) u , f \right) } + g _ { z z } { \left( \bigl ( - g _ { z } ^ { - 1 } \bigr ) u , \bigl ( - g _ { z } ^ { - 1 } \bigr ) g _ { y } f \right) } \right)
$$

which is a consequence of $( A ^ { - 1 } ( x ) ) ^ { \prime } { = } { - } A ^ { - 1 } ( x ) A ^ { \prime } ( x ) A ^ { - 1 } ( x )$ and the chain rule. This gives

$$
y ^ { \prime \prime } = f _ { y } \cdot y ^ { \prime } + f _ { z } \cdot z ^ { \prime } = f _ { y } f + f _ { z } ( - g _ { z } ^ { - 1 } ) g _ { y } f
$$

$$
z ^ { \prime \prime } = ( - g _ { z } ^ { - 1 } ) { \Big ( } g _ { z y } ( ( - g _ { z } ^ { - 1 } ) g _ { y } f , f ) + g _ { z z } ( ( - g _ { z } ^ { - 1 } ) g _ { y } f , ( - g _ { z } ^ { - 1 } ) g _ { y } f ) { \Big ) }
$$

$$
+ ( - g _ { z } ^ { - 1 } ) \Big ( g _ { y y } ( f , f ) + g _ { y z } ( f , ( - g _ { z } ^ { - 1 } ) g _ { y } f \Big )
$$

$$
+ ( - g _ { z } ^ { - 1 } ) g _ { y } \Big ( f _ { y } f + f _ { z } ( - g _ { z } ^ { - 1 } ) g _ { y } f \Big ) .
$$

Clearly, these expressions soon become very complicated and a graphical representation of the terms in (4.8) and (4.9) is desirable.

# Trees and Elementary Differentials

We shall identify each occuring $f$ with a meagre vertex, and each of its deriva-tives with an upward leaving branch. The expression $( - g _ { z } ^ { - 1 } ) g$ is identified with a fat vertex. The derivatives of $g$ therein are again indicated by upwards leaving branches. For example,the second expression of (4.8) and the first one of (4.9) correspond to the trees in Fig. 4.1.

The above formulas for $y ^ { \prime } , z ^ { \prime } , y ^ { \prime \prime } , z ^ { \prime \prime }$ thus become

$$
\left. \begin{array} { l } { { y ^ { \prime } = \bullet } } \\ { { \ z ^ { \prime \prime } = \bigwedge \quad \ z ^ { \prime \prime } = \not { C } \Im \big \langle \displaystyle \hat { \big \langle } \ y \vee \Big \rangle \ \geq \ \not { C } \big \rangle } } \end{array} \right\}
$$

The first and fourth expressions in(4.9) are identical, because $g _ { z y } ( u , v ) { = } g _ { y z } ( v , u )$ This is in nice accordance with the fact that the corresponding"trees are topologically equivalent. The lowest vertex of a tree will be called its root.

We see that derivatives of $y$ are characterized by trees with a meagre root. These trees will be denoted by $t$ or $t _ { \imath }$ , the tree consisting only of the root (for $y ^ { \prime }$ ） being $\tau _ { y }$ . Derivatives of $z$ have trees with a fat root. These will be written as $u$ or $u _ { i }$ , the tree for $z ^ { \prime }$ being $\tau _ { z }$

$$
\int \limits _ { f _ { z } } ^ { f } \biggl \langle d z ^ { - 1 } \biggr \rangle g _ { y } \qquad ( - g _ { z } ^ { - 1 } ) g _ { y } \biggl \langle \overset { f } { \underbrace { et { } { ' } \mathstrut } } \biggr \rangle f _ { ( - g _ { z } ^ { - 1 } ) g _ { z y } } ^ { f }
$$

Fig. 4.1. Graphical representation of elementary differentials

Definition 4.1. Let $D A T = D A T _ { y } \cup D A T _ { z }$ denote the set of (differential algebraic rooted) trees defined recursively by

a) $\tau _ { y } \in D A T _ { y } , \tau _ { z } \in D A T _ { z } ;$   
b） $[ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots u _ { n } ] _ { y } \in D A T _ { y }$ if $t _ { 1 } , \ldots , t _ { m } \in D A T _ { y }$ and $u _ { 1 } , \ldots u _ { n } \in D A T _ { z }$   
c） $[ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { z } \in D A T _ { z }$ if $t _ { 1 } , \ldots , t _ { m } \in D A T _ { y }$ ， $u _ { 1 } , \ldots , u _ { n } \in D A T _ { z }$ , and $( m , n ) \neq ( 0 , 1 )$

Here $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ and $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z }$ represent unordered $( m + n )$ -tuples.

The graphical representation of these trees is as follows: if we connect the roots of $t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n }$ by $m + n$ branches to a new meagre vertex (the new root） we obtain $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ ; if we connect them to a new fat vertex we obtain $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z }$ . For example, the two trees of Fig.4.1 can be written as $\left\{ \tau _ { z } \right\} _ { y }$ and $[ \tau _ { z } , \tau _ { y } ] _ { z }$

Definition 4.2. The order of a tree $t \in D A T _ { y }$ or $u \in D A T _ { z }$ ， denoted by $\varrho ( t )$ or $\varrho ( u )$ , is the number of its meagre vertices.

We see in (4.1O) that this definition of order coincides with the derivative order of $y ^ { ( \imath ) }$ or $z ^ { ( \imath ) }$ as far as they are computed there.

We next give a recursive definition of the one-to-one correspondence between the trees in (4.10) and the expressions in (4.8) and (4.9).

Definition 4.3. The elementary differentials $F ( t )$ （or $F ( u )$ ) corresponding to trees in $D A T$ are defined as follows:

$$
\begin{array} { l } { { F ( \tau _ { y } ) = f , F ( \tau _ { z } ) = ( - g _ { z } ^ { - 1 } ) g _ { y } f , } } \\ { { F ( t ) = \displaystyle \frac { \partial ^ { m + n } f } { \partial y ^ { m } \partial z ^ { n } } \left( F ( t _ { 1 } ) , \ldots , F ( t _ { m } ) , F ( u _ { 1 } ) , \ldots , F ( u _ { n } ) \right) } } \\ { { \mathrm { ~ i f ~ } t = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y } \in D A T _ { y } , } } \\ { { F ( u ) = ( - g _ { z } ) ^ { - 1 } \displaystyle \frac { \partial ^ { m + n } g } { \partial y ^ { m } \partial z ^ { n } } \left( F ( t _ { 1 } ) , \ldots , F ( t _ { m } ) , F ( u _ { 1 } ) , \ldots , F ( u _ { n } ) \right) } } \\ { { \mathrm { ~ i f ~ } u = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z } \in D A T _ { z } . } } \end{array}
$$

Because of the symmetry of partial derivatives,this definition is unaffected by a permutation of $t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n }$ and therefore the functions $F ( t )$ and $F ( u )$ are well defined.

# Taylor Expansion of the Exact Solution

In order to get more insight into the process of (4.8) and (4.9) we study the differentiation of an elementary differential with respect to $x$ . By Leibniz' rule the differentiation of $F ( t )$ (or $F ( u ) )$ gives a sum of new elementary differentials which are obtained by the following four rules:

i) attach to each vertex a branch with $\tau _ { y }$ (derivative of $f$ or $g$ with respect to $y$ and addition of the factor $y ^ { \prime } = f$ ；   
ii） attach to each vertex a branch with $\tau _ { z }$ (derivative of $f$ or $g$ with respect to $z$ and addition of the factor $z ^ { \prime } = ( - g _ { z } ^ { - 1 } ) g _ { y } f )$ ；   
iii） split each fat vertex into two new fat vertices (linked by a new branch) and attach tothe lowerofthesefatverticesabranch with $\tau _ { y }$   
iv) as in (ii) split each fat vertex into two new fat vertices,but attach this time to the lower of the new fat vertices a branch with $\tau _ { z }$

The rules (iii) and (iv) correspond to the differentiation of $( - g _ { z } ^ { - 1 } )$ and follow at once from (4.7). We observe that the differentiation of a tree of order $q$ (or, more precisely,of its corresponding elementary differential） generates trees of order $q + 1$

As was the case in Sect.I.2, some of these trees appear several times in the derivative (as the first and fourth tree for $z ^ { \prime \prime }$ in (4.1O)). In order to distinguish all these trees, we indicate the order of generation of the meagre vertices by labels. This is demonstrated, for the first derivatives of $y$ , in Fig. 4.2. Since in the above differentiation process the new meagre vertex is always an end-vertex of the tree, the labelling thus obtained is necessarily increasing from the root upwards along each branch.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/c0f9376f2b717e6f0682d9e48efc43629e736e590a5a463eb5ac21050ae9d486.jpg)  
Fig. 4.2. Monotonically labelled trees $( L D A T _ { y }$

Definition 4.4. A tree $t \in D A T _ { y }$ (or $u \in D A T _ { z }$ )together with a monotonic labelling of its meagre vertices is called a monotonically labelled tree. The sets of all such monotonically labelled trees are denoted by $L D A T _ { y } , L D A T _ { z }$ and LDAT.

Definition 4.2 (order of a tree) and Definition 4.3 (elementary differential) are extended in a natural way to monotonically labelled trees. We can therefore write the derivatives of the exact solution as follows:

Theorem 4.5 (Roche 1988). For the exact solution of(4.1) we have:

$$
\begin{array} { l } { { y ^ { ( q ) } ( x _ { 0 } ) = \displaystyle \sum _ { \substack { t \in L D A T _ { y } , \varrho ( t ) = q } } F ( t ) ( y _ { 0 } , z _ { 0 } ) = \displaystyle \sum _ { \substack { t \in D A T _ { y } , \varrho ( t ) = q } } \alpha ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) \hfill } } \\ { { z ^ { ( q ) } ( x _ { 0 } ) = \displaystyle \sum _ { \substack { u \in L D A T _ { z } , \varrho ( u ) = q } } F ( u ) ( y _ { 0 } , z _ { 0 } ) = \displaystyle \sum _ { \substack { u \in D A T _ { z } , \varrho ( u ) = q } } \alpha ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) \hfill } } \end{array}
$$

The integer coefficients $\alpha ( t )$ and $\alpha ( u )$ indicate the number of possible monotonic labellings of a tree.

Proof. For $q = 1$ and $q = 2$ this is just (4.1a), (4.6), (4.8) and (4.9). For general $q$ the above differentiation process of trees generates all elements of $L D A T$ ,each element exactly once. If the sum is taken over $D A T _ { y }$ and $D A T _ { z }$ ，the factors $\alpha ( t )$ and $\alpha ( u )$ must be added. □

# Taylor Expansion of the Numerical Solution

Our next aim is to prove an analogue of Theorem 4.5 for the numerical solution of a Rosenbrock method. We consider $y _ { 1 } , z _ { 1 }$ as functions of the step size $h$ and compute their derivatives.From (4.3a) it follows that

$$
y _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } ^ { ( q ) } ( 0 ) , \qquad z _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { \iota = 1 } ^ { s } b _ { i } \ell _ { \iota } ^ { ( q ) } ( 0 ) .
$$

Consequently we have to compute the derivatives of $k _ { \imath }$ and $\ell _ { \ i }$ . This is done as for Runge-Kutta methods (Sect.II.2) or for Rosenbrock methods applied to ordinary differential equations (Sect.IV.7).

We differentiate the first line of (4.3b) with respect to $h$ . Using Leibniz’ rule (II.2.4) this yields for $h \approx 0$

$$
k _ { i } ^ { ( q ) } = q \big ( f ( v _ { i } , w _ { i } ) \big ) ^ { ( q - 1 ) } + ( f _ { y } ) _ { 0 } q \sum _ { j = 1 } ^ { \iota } \gamma _ { i j } k _ { j } ^ { ( q - 1 ) } + ( f _ { z } ) _ { 0 } q \sum _ { j = 1 } ^ { \iota } \gamma _ { i j } \ell _ { j } ^ { ( q - 1 ) } .
$$

The index O in $( f _ { y } ) _ { 0 }$ and $( f _ { z } ) _ { 0 }$ indicates that the derivatives are evaluated at $( y _ { 0 } , z _ { 0 } )$ .The second line of (4.3b) is divided by $h$ before differentiation. This gives (again for $h = 0$ ）

$$
0 = \left( g ( v _ { \imath } , w _ { i } ) \right) ^ { ( q ) } + ( g _ { y } ) _ { 0 } \sum _ { j = 1 } ^ { i } \gamma _ { \imath j } k _ { j } ^ { ( q ) } + ( g _ { z } ) _ { 0 } \sum _ { j = 1 } ^ { \imath } \gamma _ { \imath j } \ell _ { j } ^ { ( q ) } .
$$

The derivatives of $f$ and $g$ can be computed by Faa di Bruno's formula (Lemma II.2.8). This yields

$$
\left( f ( v _ { i } , w _ { i } ) \right) ^ { ( q - 1 ) } = \sum \frac { \partial ^ { m + n } f ( v _ { \ i } , w _ { \ i } ) } { \partial y ^ { m } \partial z ^ { n } } \left( v _ { i } ^ { ( \mu _ { 1 } ) } , \ldots , v _ { \ i } ^ { ( \mu _ { m } ) } , w _ { \ i } ^ { ( \nu _ { 1 } ) } , \ldots , w _ { i } ^ { ( \nu _ { n } ) } \right)
$$

where the sum is over all“special $L D A T _ { y } ^ { \mathrm { ~ } \bullet \mathrm { ~ } }$ of order $q$ . These are monotonically labelled trees $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ where $t _ { j }$ and $u _ { \ j }$ do not have any ramifica-tion and alltheir vertices are meagre with the exception of the roots of $u _ { 1 } , \ldots , u _ { n } .$ The integers $\mu _ { j }$ and $\nu _ { j }$ are the orders of $t _ { j }$ and $u _ { j }$ ， respectively. They satisfy $\mu _ { 1 } + . . . + \mu _ { m } + \nu _ { 1 } + . . . + \nu _ { n } = q - 1$ . Similarly we apply Faa di Bruno's formula to $g$ and obtain

$$
\begin{array} { c } { \displaystyle \left( g ( v _ { i } , w _ { \imath } ) \right) ^ { ( q ) } = \sum \displaystyle \frac { \partial ^ { m + n } g ( v _ { \imath } , w _ { i } ) } { \partial y ^ { m } \partial z ^ { n } } \left( v _ { i } ^ { ( \mu _ { 1 } ) } , \ldots , v _ { \imath } ^ { ( \mu _ { m } ) } , w _ { i } ^ { ( \nu _ { 1 } ) } , \ldots , w _ { i } ^ { ( \nu _ { n } ) } \right) } \\ { \displaystyle + g _ { z } ( v _ { \imath } , w _ { i } ) w _ { i } ^ { ( q ) } . } \end{array}
$$

Here the sum is over all“special $L D A T _ { z } ^ { \mathrm { ~ } \bullet \prime }$ of order $q$ . They are defined as above but have a fat vertex. The integers $\mu _ { \ j } , \nu _ { j }$ satisfy $\mu _ { 1 } + \ldots + \mu _ { m } + \nu _ { 1 } + \ldots + \nu _ { n } = q$ The term with $g _ { z }$ is written separately,because (by the definition of $L D A T _ { z }$ ） $\left\{ u _ { 1 } \right\} _ { z }$ is not an admissible tree.

We are now in a position to compute the derivatives of $k _ { i }$ and $\ell _ { i }$ . For this it is convenient to introduce the notation

$$
\beta _ { i j } = \alpha _ { \iota j } + \gamma _ { i j }
$$

(with $\alpha _ { i i } = 0$ ) as in (IV.7.12). We also need the inverse of the matrix $( \beta _ { \imath j } )$ ,whose coefcients we denote by $\omega _ { i j }$ ：

$$
( \omega _ { i j } ) = ( \beta _ { \ i j } ) ^ { - 1 } .
$$

Theorem 4.6. The derivatives of $k _ { i }$ and $\ell _ { i }$ satisfy

$$
\begin{array} { l } { { k _ { i } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle { t \in L D A T _ { y } , \varrho ( t ) = q } } \gamma ( t ) \Phi _ { i } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \ell _ { i } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle u \in L D A T _ { z } , \varrho ( u ) = q } \gamma ( u ) \Phi _ { i } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) , } } \end{array}
$$

where the coefficients $\Phi _ { i } ( t )$ and $\Phi _ { i } ( u )$ are given by $\Phi _ { \imath } ( \tau _ { y } ) = 1$ ， $\Phi _ { i } ( \tau _ { z } ) = 1$ and

$$
\Phi _ { i } ( t ) = \left\{ \begin{array} { l l } { { \displaystyle \sum _ { \mu _ { 1 } , \dots , \mu _ { m } , \nu _ { 1 } , \dots , \nu _ { n } } \alpha _ { \iota _ { \mu _ { 1 } } } \cdot \cdot \cdot \alpha _ { i \mu _ { m } } \alpha _ { \iota \nu _ { 1 } } \cdot \cdot \cdot \alpha _ { i \nu _ { n } } } } _ { \iota _ { \mu _ { 1 } } }  & { { \mathrm { ~ } } } \\ { { \quad \cdot \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } ) \Phi _ { \nu _ { 1 } } ( u _ { 1 } ) \cdot \cdot \cdot \Phi _ { \nu _ { n } } ( u _ { n } ) } } & { { \mathrm { ~ } } } \\ { { \quad \quad } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( t _ { 1 } ) } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( u _ { 1 } ) } } & { { \mathrm { ~ } } } \\ { { \displaystyle \sum _ { j } \beta _ { i j } \Phi _ { j } ( u _ { 1 } ) } } & { { \mathrm { ~ } } } \end{array} \right.
$$

$$
\Phi _ { \imath } ( u ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { \jmath , \mu _ { 1 } , \ldots , \mu _ { m } , \nu _ { 1 } , \ldots , \nu _ { n } } \omega _ { i j } \alpha _ { j \mu _ { 1 } } \cdot \cdot \cdot \alpha _ { j \mu _ { m } } \alpha _ { \jmath \nu _ { 1 } } \cdot \cdot \cdot \alpha _ { j \nu _ { n } } } & \\ { \quad \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } ) \Phi _ { \nu _ { 1 } } ( u _ { 1 } ) \cdot \cdot \cdot \Phi _ { \nu _ { n } } ( u _ { n } ) } & \\ { \quad \quad \quad \quad i f u = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { z } a n d m + n \geq 2 } \\ { \Phi _ { i } ( t _ { 1 } ) } & { \quad \quad \quad i f u = [ t _ { 1 } ] _ { z } } \end{array} \right.
$$

and the integer coefficients $\gamma ( t )$ and $\gamma ( u )$ are defined by $\gamma ( \tau _ { y } ) = 1 , \ \gamma ( \tau _ { z } ) = 1$ and

$$
\begin{array} { r l } & { \gamma ( t ) = \varrho ( t ) \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) \gamma ( u _ { 1 } ) \dots \gamma ( u _ { n } ) \quad i f t = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { y } } \\ & { \gamma ( u ) = \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) \gamma ( u _ { 1 } ) \dots \gamma ( u _ { n } ) \qquad i f u = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { z } . } \end{array}
$$

Proof. By (4.3a) we have

$$
v _ { \imath } ^ { ( \mu ) } = \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { \imath \jmath } k _ { \jmath } ^ { ( \mu ) } , \qquad w _ { \imath } ^ { ( \nu ) } = \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } \ell _ { \jmath } ^ { ( \nu ) } .
$$

We now insert (4.19) into (4.14) and the resulting formula for $( f ( v _ { \iota } , w _ { i } ) ) ^ { ( q - 1 ) }$ into (4.12). This yields (all expressions have to be evaluated at $h \approx 0$ ）

$$
\begin{array} { c } { { k _ { \imath } ^ { ( q ) } = q \displaystyle \sum _ { m + n \geq 2 } \displaystyle \frac { \partial ^ { m + n } f ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \displaystyle \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { \imath j } k _ { \jmath } ^ { ( \mu _ { 1 } ) } , \ldots , \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { i _ { j } } \ell _ { j } ^ { ( \nu _ { 1 } ) } , \ldots \right) } } \\ { { + q ( f _ { y } ) _ { 0 } \displaystyle \sum _ { \jmath = 1 } ^ { i } \beta _ { \imath j } k _ { \jmath } ^ { ( q - 1 ) } + q ( f _ { z } ) _ { 0 } \displaystyle \sum _ { j = 1 } ^ { \imath } \beta _ { \imath j } \ell _ { j } ^ { ( q - 1 ) } . } } \end{array}
$$

The same analysis for the second component leads to

$$
\begin{array} { l } { { \displaystyle 0 = \sum _ { m + n \geq 2 } \frac { \partial ^ { m + n } g ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } k _ { j } ^ { ( \mu _ { 1 } ) } , \dots , \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } \ell _ { j } ^ { ( \nu _ { 1 } ) } , \dots \right) } } \\ { { \displaystyle \qquad + ( g _ { y } ) _ { 0 } \sum _ { j = 1 } ^ { i } \beta _ { i j } k _ { j } ^ { ( q ) } + ( g _ { z } ) _ { 0 } \sum _ { j = 1 } ^ { i } \beta _ { i j } \ell _ { j } ^ { ( q ) } . } } \end{array}
$$

The sums in (4.20) and (4.21) are over elements of $L D A T$ exactly as in (4.14) and (4.15). Equation (4.21) allows us to extract $\ell _ { i } ^ { ( q ) }$ if we use the inverse of (βij). This gives

$$
\begin{array} { l } { { \displaystyle { \bf \zeta } _ { i } ^ { ( q ) } = \left( - g _ { z } \right) _ { 0 } ^ { - 1 } \sum _ { j = 1 } ^ { i } \omega _ { i j } \sum _ { m + n \geq 2 } \frac { \partial ^ { m + n } g ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { \kappa = 1 } ^ { j - 1 } \alpha _ { j \kappa } k _ { \kappa } ^ { ( \mu _ { 1 } ) } , \dots , \sum _ { \kappa = 1 } ^ { j - 1 } \alpha _ { j \kappa } \ell _ { \kappa } ^ { ( \nu _ { 1 } ) } , \dots , \sum _ { \kappa = 1 } ^ { i - 1 } \alpha _ { j \kappa } k _ { \kappa } ^ { ( \mu _ { 1 } ) } \right) } } \\ { { \displaystyle \qquad + \left( ( - g _ { z } ^ { - 1 } ) g _ { y } \right) _ { 0 } k _ { i } ^ { ( q ) } . \qquad \quad { \scriptstyle ( 4 . 2 2 \kappa ) } } } \end{array}
$$

The proof of Formula (4.18) is now by induction on $q$ . The case $q = 1$ follows immediately from (4.12) and (4.13). For general $q$ , we insert the induction hypothesis into (4.20) and (4.22),exploit the multilinearity of the derivatives,and arrange the summations as in the proof of Theorem II.2.11. □

Finally, Eq.(4.11) yields the derivatives of the numerical solution.

Theorem 4.7 (Roche 1988). The numerical solution of(4.3) satisfies:

$$
\begin{array} { l } { { \displaystyle y _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { t \in L D A T _ { y } , \varrho ( t ) = q } \gamma ( t ) \sum _ { \iota = 1 } ^ { s } b _ { \iota } \Phi _ { \iota } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \displaystyle z _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { \iota \in L D A T _ { z } , \varrho ( u ) = q } \gamma ( u ) \sum _ { i = 1 } ^ { s } b _ { \iota } \Phi _ { i } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) } } \end{array}
$$

where the coefficients $\gamma$ and $\Phi _ { \imath }$ are given in Theorem 4.6.

# Order Conditions

Comparing Theorem 4.5 and 4.7 we obtain

Theorem 4.8. For the Rosenbrock method (4.3) we have:

$$
\begin{array} { r l } { y ( x _ { 0 } + h ) - y _ { 1 } = \mathcal { O } ( h ^ { p + 1 } ) } & { i f f } \\ { \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } \Phi _ { i } ( t ) = \frac { 1 } { \gamma ( t ) } \quad } & { f o r t \in D A T _ { y } , \varrho ( t ) \le p ; } \end{array}
$$

$$
\begin{array} { r l } { z ( x _ { 0 } + h ) - z _ { 1 } = \displaystyle { \mathcal { O } ( h ^ { q + 1 } ) } i f f \quad } & { } \\ { \displaystyle { \sum _ { \imath = 1 } ^ { s } b _ { \imath } \Phi _ { \imath } ( u ) } = \frac { 1 } { \gamma ( u ) } \quad } & { \ f o r u \in D A T _ { z } , \varrho ( u ) \leq q , } \end{array}
$$

where the coeffcients $\Phi _ { i }$ and $\gamma$ are those of Theorem 4.6.

Repeated application of the recursive definition of $\Phi _ { \imath }$ in Theorem 4.6 yields the following algorithm:

Forming the Order Condition for a Given Tree: atach to each meagre vertex one summation index,and to each fat vertex two indices (one above the other). Then the left hand side of the order condition is a sum over all indices of a product with factors

$b _ { i }$ if $^ { \mathfrak { s } } { } _ { i } \mathbf { \vec { \mu } } ^ { \mathfrak { s } }$ is the index of the root (the lower index if the root is fat); $\alpha _ { \imath j }$ if $^ { 6 6 } j ^ { 3 }$ lies directly above $^ { \mathfrak { s } \mathfrak { e } ^ { \mathfrak { s } } \mathfrak { z } }$ and $^ { 6 6 } i ^ { , 9 }$ is multiply branched; βi if $^ { 6 6 } \vec { \mathcal { I } } ^ { \ ' }$ lies directly above $^ { 6 6 } i ^ { 7 3 }$ and $^ { \mathfrak { s } \mathfrak { e } ^ { \mathfrak { s } } \mathfrak { z } }$ is singly branched; $\omega _ { i j }$ if $^ { \mathbf { \omega } _ { ^ { 6 6 } i , j } ^ { \mathbf { \omega } } }$ are the two indices of a fat vertex $( ^ { 6 6 } i ^ { 3 3 } \mathrm { b e l o w } ^ { 6 6 } j ^ { 3 3 } )$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/5d5ddc51cfdc4133ee2ec71e572850fcd0157e54685fa6bbc898cc4401986950.jpg)  
Fig. 4.3. Trees with labelling

As an example, we present the order conditions for the first two trees of Fig.4.3.

$$
\begin{array} { c } { { \displaystyle { \sum _ { i , j , k , \ell , m } b _ { i } \alpha _ { i j } \alpha _ { i k } \omega _ { k \ell } \beta _ { \ell m } = \frac { 1 } { 3 } } } } \\ { { { \displaystyle { \sum _ { i , j , k , \ell , m , n , p } b _ { \iota } \omega _ { i j } \alpha _ { j k } \alpha _ { j \ell } \omega _ { \ell m } \alpha _ { m n } \alpha _ { m p } = 1 } } . } } \end{array}
$$

The condition (4.23)can be further simplified if we use the fact that $\left( \omega _ { \imath j } \right)$ is the inverse of the matrix $( \beta _ { i j } )$ . Indeed, (4.23) is equivalent to

$$
\sum _ { i , j , k } b _ { i } \alpha _ { i j } \alpha _ { i k } = \frac { 1 } { 3 }
$$

which is the order condition for the third tree inFig.4.3. Exploiting this reduction systematically we arrive at the following result.

Lemma 4.9. For a Rosenbrock method (4.3) the order conditions corresponding to one of the following situations are redundant:

a) a fat vertex is singly branched.   
b) a singly branched vertex is followed by a fat vertex.

The subset of $D A T _ { y }$ which consists of trees with only meagre vertices, is simply $T$ (the set of trees of Sect.II.2). The corresponding order conditions are those given in Sect.IV.7. Consequently, a $p$ -th order Rosenbrock method has to satisfy all “classical” order conditions and, in addition, several “algebraic” conditions. The first of these new order conditions are given in Table 4.1. We have included the polynomial $p _ { t } ( \gamma )$ in its last column,which is the right-hand side of the order condition, when written in the form (IV.7.11').

# Convergence

Before we proceed to the actual construction of a new Rosenbrock method, we still have to study its convergence property. The following result will also involve

$$
R ( \infty ) = 1 - b ^ { T } B ^ { - 1 } \mathbb { 1 } = 1 - \sum _ { \iota , j } b _ { i } \omega _ { \iota j }
$$

where $R ( z )$ is the stability function (IV.7.14).

Table 4.1. Trees and elementary differentials   

<table><tr><td>g(t）</td><td>t</td><td>graph</td><td>r(t）</td><td>(t）</td><td>Pt(y)</td></tr><tr><td>4</td><td>t45</td><td></td><td>4</td><td>∑ajkaJewlmamnamp</td><td>1/4</td></tr><tr><td>2</td><td>u21</td><td></td><td>1</td><td>Mwkakeakm</td><td>1</td></tr><tr><td>3 3</td><td>u31</td><td></td><td>1 2</td><td>MwJkakeakmakn ∑wJkaklakmβmn</td><td>1 1/2-Y</td></tr><tr><td>3</td><td>u32</td><td></td><td>1</td><td>∑wjkakeαkmwmnanpanq</td><td>1</td></tr><tr><td></td><td>u33</td><td></td><td></td><td></td><td></td></tr></table>

We denote the local error of the Rosenbrock method (4.3) by

$$
\delta y _ { h } ( x ) = y _ { 1 } - y ( x + h ) , \qquad \delta z _ { h } ( x ) = z _ { 1 } - z ( x + h ) .
$$

Here $y _ { 1 } , z _ { 1 }$ is the numerical solution obtained with the exact initial values $y _ { 0 } =$ $y ( x )$ ， $z _ { 0 } = z ( x )$ ·

Theorem 4.10. Suppose that $g _ { z }$ is regular in $a$ neighbourhood of the solution $( y ( x ) , z ( x ) )$ of(4.1) and that the initial values $( y _ { 0 } , z _ { 0 } )$ are consistent. If the stability function is such that $| R ( \infty ) | < 1$ , and the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad \delta z _ { h } ( x ) = \mathcal { O } ( h ^ { p } ) ,
$$

then the Rosenbrock method (4.3) is convergent of order $p ; i . e . ,$

$$
y _ { n } - y ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \quad z _ { n } - z ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) \quad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t .
$$

Proof. Since $g _ { z }$ is regular we have

$$
\| g _ { z } ^ { - 1 } ( y , z ) g ( y , z ) \| \leq \delta
$$

for $( y , z )$ in acompact neighbourhood $\mathcal { U }$ of the solution. The $h$ -independent value of $\delta$ can be made arbitrarily small by shrinking $\mathcal { U }$ . We also suppose for the moment that the numerical solution and all its internal stages remain in this neighbourhood. The propagation of local errors will be studied in part (a),and their accumulation over the whole interval in part (b).

a) We consider two pairs of initial values, $( y _ { 0 } , z _ { 0 } )$ and $( \widehat { y } _ { 0 } , \widehat { z } _ { 0 } )$ , and apply the method to each (these values may be inconsistent, but they are assumed to lie in $\boldsymbol { \mathcal { U } } )$ . We shall prove that

$$
\begin{array} { r l } & { \| y _ { 1 } - \widehat { y } _ { 1 } \| \leq ( 1 + h L ) \| y _ { 0 } - \widehat { y } _ { 0 } \| + h M \| z _ { 0 } - \widehat { z } _ { 0 } \| } \\ & { \| z _ { 1 } - \widehat { z } _ { 1 } \| \leq N \| y _ { 0 } - \widehat { y } _ { 0 } \| + \kappa \| z _ { 0 } - \widehat { z } _ { 0 } \| } \end{array}
$$

where $\kappa < 1$ . For this we fix a sufficiently small step size $h$ , and consider $y _ { 1 } , z _ { 1 }$

$k _ { \imath } , \ell _ { \imath }$ as functions of $( y _ { 0 } , z _ { 0 } )$ . We shall show that

$$
\begin{array} { r l r l } & { \displaystyle \frac { \partial y _ { 1 } } { \partial y _ { 0 } } = I + \mathcal { O } ( h ) , } & & { \displaystyle \frac { \partial y _ { 1 } } { \partial z _ { 0 } } = \mathcal { O } ( h ) , } \\ & { \displaystyle \frac { \partial z _ { 1 } } { \partial y _ { 0 } } = \mathcal { O } ( 1 ) , } & & { \displaystyle \frac { \partial z _ { 1 } } { \partial z _ { 0 } } = R ( \infty ) I + \mathcal { O } ( h + \delta ) . } \end{array}
$$

The mean value theorem then implies (4.29).

We first estimate $k _ { \imath }$ and $\ell _ { \ i }$ , defined in (4.3b). Using (4.28) we compute $\ell _ { \ i }$ from the second line and insert it into the first one. This yields successively $k _ { \imath } =$ ${ \mathcal { O } } ( h )$ and $\ell _ { \ i } = \mathcal { O } ( h + \delta )$ for all internal stages. We then differentiate (4.3b) once with respect to $y _ { 0 }$ and once with respect to $z _ { 0 }$ . An analysis similar to that for $k _ { \imath }$ and $\ell _ { \ i }$ yields

$$
\begin{array} { r l r l } & { \displaystyle \frac { \partial k _ { \iota } } { \partial y _ { 0 } } = \mathcal { O } ( h ) , } & & { \displaystyle \frac { \partial k _ { i } } { \partial z _ { 0 } } = \mathcal { O } ( h ) } \\ & { \displaystyle \frac { \partial \ell _ { \iota } } { \partial y _ { 0 } } = \mathcal { O } ( 1 ) , } & & { \displaystyle \frac { \partial \ell _ { i } } { \partial z _ { 0 } } = - \sum _ { \jmath } \omega _ { \iota \jmath } I + \mathcal { O } ( h + \delta ) } \end{array}
$$

and the estimates (4.30) follow from (4.3a) and (4.25).

b) As a consequence of Lemma 3.9 (see Exercise 8), the propagation of the local errors $\delta y _ { h } ( x _ { \jmath - 1 } ) , \delta z _ { h } ( x _ { \jmath - 1 } )$ to the solution at $x _ { n }$ can be bounded by

$$
C \big ( \| \delta y _ { h } ( x _ { j - 1 } ) \| + ( h + \kappa ^ { n - \jmath } ) \| \delta z _ { h } ( x _ { \jmath - 1 } ) \| \big ) .
$$

Summing up these terms from $j = 1$ to $j = n$ and using (4.27) gives the stated bounds forthe global error, because $\textstyle \sum _ { j = 1 } ^ { n } \left( h + \kappa ^ { n - \jmath } \right) \leq C o n s t .$

Our assumption that the numerical solution and the internal stages lie in $\mathcal { U }$ can now easily be justified by induction on the step number. The numerical solution remains $\mathcal { O } ( h ^ { p } )$ -close to the exact solution and thus remains in $\mathcal { U }$ for sufficiently small $h$ ．This implies $g ( y _ { \jmath } , z _ { \jmath } ) = \mathcal { O } ( h ^ { p } )$ for all $j$ and hence also $\ell _ { \ i } = \mathcal { O } ( h )$ Consequently $( v _ { \imath } , w _ { \imath } )$ are also as close to the exact solution as we want. □

# Stiffly Accurate Rosenbrock Methods

We have already had several occasions to admire the beneficial effect of stiffly accurate Runge-Kutta methods (methods with $a _ { s i } = b _ { \imath }$ for all $i$ ; see Theorem 1.1 and Corollary 3.1O). What is the corresponding condition for Rosenbrock methods?

Definition 4.11. A Rosenbrock method is called stiffly accurate, if

$$
\alpha _ { s \ i } + \gamma _ { s \ i } = b _ { \ i } \quad ( i = 1 , \ldots , s ) \quad \mathrm { { a n d } } \quad \alpha _ { s } = 1 .
$$

Recall that $\textstyle \alpha _ { \iota } = \sum _ { \boldsymbol { \jmath } } \alpha _ { \iota \boldsymbol { \jmath } }$ . It has already been remarked at the end of Sect.IV.15 that methods satisfying (4.33) yield asymptotically exact results for the problem $y ^ { \prime } = \lambda ( y - \varphi ( x ) ) + \varphi ^ { \prime } ( x )$ . A further interesting interpretation of this condition has been given by C. Schneider (1991). He argues that DAE's are combinations of differential equations and algebraic equations; hence methods should be equally valuable for both extreme cases, either a purely differential equation, or a purely algebraic equation

$$
x ^ { \prime } = 1 , \qquad 0 = g ( x , z ) , \qquad g _ { z } { \mathrm { ~ i n v e r t i b l e ~ . } }
$$

Proposition 4.12. A stiffly accurate Rosenbrock method, applied to (4.34), yields

$$
z _ { 1 } = w _ { s } - g _ { z } ^ { - 1 } ( x _ { 0 } , z _ { 0 } ) \cdot g ( x _ { 0 } + h , w _ { s } ) .
$$

The numerical solution $z _ { 1 }$ is thus the result of one simplified Newton iteration for $0 = g ( x _ { 0 } + h , z )$ (with starting value $w _ { s }$ ）

Proof. Condition (4.33)together with $\sum _ { i } b _ { i } = 1$ implies that $\begin{array} { r } { \gamma _ { s } = \sum _ { j } \gamma _ { s j } = 0 } \end{array}$ Therefore, the second line of (4.5） gives (observe that $k _ { \ i } = h$ for the problem (4.34))

$$
0 = g ( x _ { 0 } + h . w _ { s } ) + g _ { z } ( x _ { 0 } , z _ { 0 } ) \sum _ { \jmath = 1 } ^ { \imath } { \gamma } _ { \imath \jmath } \ell _ { \jmath } .
$$

Inserting the expression thus obtained for $\sum _ { \jmath } \gamma _ { \imath \jmath } \ell _ { \jmath }$ into

$$
z _ { 1 } = z _ { 0 } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \ell _ { \jmath } = w _ { s } + \sum _ { \jmath = 1 } ^ { s } \gamma _ { \mathfrak { s } \jmath } \ell _ { \jmath }
$$

proves the statement.

The values $( v _ { s } , w _ { s } )$ of the last stage are often used as an embedded solution for step size control. If this is the case for a stiffly accurate method, then many of the algebraic order condition are automatically satisfied. This is a consequence of the following result.

Proposition 4.13. Consider a stifly accurate Rosenbrock method. For suffciently regular problems (4.1) we have

$$
z _ { 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { q + 1 } )
$$

if and only if

$$
v _ { s } - y \big ( x _ { 0 } + h \big ) = \mathcal { O } \big ( h ^ { q } \big ) \qquad \quad a n d \qquad w _ { s } - z \big ( x _ { 0 } + h \big ) = \mathcal { O } ( h ^ { q } ) .
$$

Proof.Weusethe characterizationof Theorem 4.8and thefact that (with $\omega _ { i j }$ defined in (4.17))

$$
\sum _ { \ i } b _ { \ i } \omega _ { \ i \jmath } = \left\{ \begin{array} { l l } { 1 } & { \mathrm { ~ i f ~ } \ \jmath = s } \\ { 0 } & { \mathrm { ~ e l s e ~ . ~ } } \end{array} \right.
$$

Suppose first that (4.35) holds.For a tree $\boldsymbol { u } = \left[ \tau _ { y } , t _ { 2 } \right] _ { z }$ with arbitrary $t _ { 2 } \in D A T _ { y }$ we have, by definition of $\Phi _ { j } ( u )$ and $\gamma ( u )$ ，

$$
\sum _ { i } b _ { \imath } \Phi _ { \imath } ( u ) = \sum _ { \imath , j , k } b _ { \imath } \omega _ { i j } \alpha _ { j } \alpha _ { j k } \Phi _ { k } ( t _ { 2 } ) = \sum _ { k } \alpha _ { s k } \Phi _ { k } ( t _ { 2 } )
$$

and $\gamma ( u ) = \gamma ( t _ { 2 } )$ . Consequently, the order condition is satisfied for $u$ iff it is satisfied for $t _ { 2 }$ . Since $\varrho \big ( t _ { 2 } \big ) = \varrho \big ( u \big ) - 1$ , we see that $v _ { s } - y ( x _ { 0 } + h ) = \mathcal { O } \left( h ^ { q } \right)$ is a consequence of (4.35). By considering $\boldsymbol { u } = [ \tau _ { y } , u _ { 1 } ] _ { z }$ with $u _ { 1 } \in D A T _ { z }$ we deduce the second relation of (4.36). The “if" part is proved in a similar way. □

Finally we remark that because of (4.25) and (4.37) the stability function of a stiffly accurate Rosenbrock method always satisfies $R ( \infty ) = 0$ . This is a desirable property when solving stiff or differential algebraic equations.

# Construction of RODAS, a Stiffly Accurate Embedded Method

We want to construct an embedded Rosenbrock method (where $\widehat { y } _ { 1 } = v _ { s } , \widehat { z } _ { 1 } = w _ { s } )$ ， such that both methods are stiffly accurate. This gives the following conditions

$$
\begin{array} { l l } { { b _ { \imath } = \beta _ { s \imath } ~ ( i = 1 , \ldots , s ) , ~ \qquad \alpha _ { s } = 1 } } \\ { { \widehat { b } _ { i } = \alpha _ { s i } = \beta _ { s - 1 , i } ~ ( i = 1 , \ldots , s - 1 ) , ~ \qquad \alpha _ { s - 1 } = 1 } } \end{array}
$$

(as usual $\beta _ { i j } = \alpha _ { \iota j } + \gamma _ { i j } )$ . It follows from Proposition 4.12 that the last two stages represent simplified Newton iterations. Further,both methods have a stability function which vanishes at infinity. The construction of such a method of order 4(3) seems to be impossible with $s = 5$ . We therefore put $s = 6$

Here is the list of order conditions which have to be solved. We use the abbreviations $\alpha _ { \imath } , \beta _ { \imath } ^ { \prime }$ defined in (IV.7.16),and the coefficients $\omega _ { \imath \jmath }$ from (4.17).We shall require that

$$
y _ { 1 } - y ( x _ { 0 } + h ) = { \mathcal { O } } ( h ^ { 5 } ) , \qquad { \widehat { y } } _ { 1 } - y ( x _ { 0 } + h ) = { \mathcal { O } } ( h ^ { 4 } ) .
$$

Since we have sufficiently many parameters we also require

$$
v _ { s - 1 } - y ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { 3 } ) , \qquad w _ { s - 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { 3 } ) .
$$

By Proposition 4.13 this implies

$$
\widehat { z } _ { 1 } - z \big ( x _ { 0 } + h \big ) = { \mathcal O } \big ( h ^ { 4 } \big ) , \qquad z _ { 1 } - z \big ( x _ { 0 } + h \big ) = { \mathcal O } \big ( h ^ { 5 } \big ) ,
$$

which is more than sufficient to ensure convergence of order 4 (see Theorem 4 The conditions for (4.40) and (4.41) are (see Table IV.7.1 and Table 4.1)

$$
\begin{array} { r l } & { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } + ( b _ { 5 } + b _ { 6 } ) = 1 } \\ & { b _ { 2 } \beta _ { 2 } ^ { \prime } + b _ { 3 } \beta _ { 3 } ^ { \prime } + b _ { 4 } \beta _ { 4 } ^ { \prime } + ( b _ { 5 } + b _ { 6 } ) ( 1 - \gamma ) = \frac { 1 } { 2 } - \gamma } \\ & { b _ { 2 } \alpha _ { 2 } ^ { 2 } + b _ { 3 } \alpha _ { 3 } ^ { 2 } + b _ { 4 } \alpha _ { 4 } ^ { 2 } + ( b _ { 5 } + b _ { 6 } ) = \frac { 1 } { 3 } } \end{array}
$$

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { i } \partial _ { x } \beta _ { 1 2 } \partial _ { y } ^ { 2 } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 1 1 } ^ { 2 } \neq \frac { 1 } { 2 } \partial _ { y } \beta _ { 2 1 } ^ { 1 } \neq \frac { 1 } { 2 } \partial _ { z } \beta _ { 1 1 } ^ { 2 } \neq \frac { 1 } { 2 } \partial _ { y } \beta _ { 1 2 } ^ { 1 } = \frac { 1 } { 2 } \partial _ { z } \gamma _ { 1 1 } ^ { 2 } \ \gamma ^ { 2 } \ } \\ & { \partial _ { x } \beta _ { 1 2 } ^ { 3 } \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 3 } ^ { 2 } \ \ + \frac { 1 } { 2 } \partial _ { x } \partial _ { z } \beta _ { 1 2 } ^ { 3 } \ \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \neq \frac { 1 } { 2 } \ } \\ & { \partial _ { y } \partial _ { 3 } \alpha _ { 3 } \partial _ { y } ^ { 2 } \partial _ { 1 } ^ { 2 } \ + \Delta _ { z } \partial _ { z } \gamma \sum _ { \alpha _ { 1 3 } } ^ { \alpha } \partial _ { y } ^ { 3 } \ \ + \frac { 1 } { 2 } \partial _ { x } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \ \ \ \ \mathrm { ( } \partial _ { y } \partial _ { 1 2 } ^ { 3 } \ \ \ \mathrm { - } \ \gamma _ { 1 } ^ { 2 } \ \gamma } \\ & { \partial _ { x } \partial _ { x } \gamma _ { 2 1 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { z } \partial _ { x } \gamma ^ { 2 } \ \partial _ { 1 2 } ^ { 3 } \ \ \mathrm { ~ } } \\ & { \partial _ { y } \partial _ { 3 } \gamma _ { 3 2 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { z } \gamma \ \partial _ { 4 2 } ^ { 3 } \ \ \mathrm { ~ } } \\ & { \partial _ { z } \partial _ { 3 } \gamma _ { 3 2 } ^ { \alpha } \neq \frac { 1 } { 2 } \partial _ { y } \partial _ { 4 2 } ^ { 3 } \ \gamma \ } \\ &  \partial _ { x } \partial _ { x } \partial _ { y } \partial _ { z } \gamma \end{array} \end{array}
$$

In order to solve the system (4.39), (4.43a-n) we can take $\gamma , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } , \beta _ { 2 } ^ { \prime } =$ $\beta _ { 2 1 } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ as free parameters. The remaining coeficients can then be computed as follows:

Step $l$ . We have $b _ { 6 } = \gamma$ by (4.39). The remaining $b _ { i }$ can be chosen such that (4.43a,b,c,e) are satisfied. We have one degree of freedom which can be exploited to fulfill the additional order condition $\textstyle \sum _ { i } b _ { i } \alpha _ { i } ^ { 4 } = 1 / 5$ . This step also yields $\beta _ { 6 i } \simeq$ $b _ { i }$ for $i = 1 , \ldots , 6$

Step 2. Compute the two expressions $b _ { 3 } \beta _ { 3 2 } + b _ { 4 } \beta _ { 4 2 }$ and $b _ { 4 } \beta _ { 4 3 }$ from (4.43d,g), and then $\beta _ { 3 2 }$ from(4.43b). Because f $\begin{array} { r } { \beta _ { i } ^ { \prime } = \sum _ { j = 1 } ^ { i - 1 } \beta _ { i j } } \end{array}$ tis etemines all $\beta _ { i j }$ with $i \leq 4$ . Observe that $\beta _ { i i } = \gamma$ for all

Step 3. Solve the linear system $( 4 . 4 3 \mathrm { j } , \mathrm { k } , \mathrm { l } )$ for $\alpha _ { 6 2 } , \alpha _ { 6 3 } , \alpha _ { 6 4 }$ . We have $\alpha _ { 6 5 } = \gamma$ by (4.39) and compute $\alpha _ { 6 1 }$ from $\begin{array} { r } { \alpha _ { 6 } = \sum _ { i } \alpha _ { 6 i } = 1 } \end{array}$ .This also yields $\beta _ { 5 i } \simeq \alpha _ { 6 i }$ by (4.39). Hence all $\beta _ { \imath j }$ and $\omega _ { i j }$ ,and also $\widehat { \boldsymbol { b } } _ { \iota } = \beta _ { 5 \iota }$ $( i = 1 , \ldots , 5 )$ are determined at this stage.

Step 4. The conditions $( 4 . 4 3 \mathrm { m } , \mathrm { n } )$ and $\alpha _ { 5 } = 1$ constitute 3 linear equations in the four unknown parameters $\alpha _ { 5 1 } , \alpha _ { 5 2 } , \alpha _ { 5 3 } , \alpha _ { 5 4 }$ . We have one degree of freedom in this step.

Step 5.The remaining two conditions (4.43f,i) are linear equations in $\alpha _ { 3 2 } ,$ $\alpha _ { 4 2 } , \alpha _ { 4 3 }$ . We have one more degree of freedom which can be exploited to fulfill the order condition for the tree $\left\{ \tau _ { y } , \tau _ { y } , \left[ \tau _ { y } \right] _ { y } \right\} _ { y }$ . The values of $\alpha _ { \imath 1 }$ are then determined by $\begin{array} { r } { \alpha _ { \iota } = \sum _ { \jmath = 1 } ^ { i - 1 } \alpha _ { i \jmath } } \end{array}$ , and those of $\gamma _ { \imath j }$ are given by $\gamma _ { \imath j } = \beta _ { \imath j } - \alpha _ { \imath j }$

The coeficients for the code RODAS of the appendix were computed with the above procedure. In step 4 we have added the condition

$$
\sum _ { \imath , j } \alpha _ { 5 i } \omega _ { i j } = 1
$$

which will be explained in Exercise 3 below. The free parameters were chosen in

order to get an $A$ -stable method with small error constants. The result is

$$
\begin{array} { l l l } { { \gamma = 0 . 2 5 } } & { { } } & { { } } \\ { { \alpha _ { 2 } = 0 . 3 8 6 } } & { { } } & { { \alpha _ { 3 } = 0 . 2 1 } } & { { \alpha _ { 4 } = 0 . 6 3 } } \\ { { \beta _ { 2 } ^ { \prime } = 0 . 0 3 1 7 } } & { { } } & { { \beta _ { 3 } ^ { \prime } = 0 . 0 6 3 5 } } & { { \beta _ { 4 } ^ { \prime } = 0 . 3 4 3 8 } } \end{array}
$$

We do not claim that these values are optimal. Nevertheless, the numerical results of Sect.IV.10 (Fig.IV.10.8,IV.10.9 and IV.10.12) are encouraging. Although the new method needs 6 function evaluations per step, it is in general superior to the classical methods of Table IV.7.2 which need only 3 evaluations per step.

A different set of coeficients,based on the same construction, has been proposed by Steinebach (1995). The free parameters are chosen in order to satisfy the Scholz conditions $C _ { 2 } ( z ) \equiv 0$ and $C _ { 3 } ( z ) \equiv 0$ (see Eq.(15.41) of Sect.IV.15).

Dense Output. A natural way to define a continuous numerical solution for $y ( x _ { 0 } +$ $\theta h )$ ， $z { \big ( } x _ { 0 } + \theta h { \big ) }$ is

$$
y _ { 1 } ( \theta ) = y _ { 0 } + \sum _ { i = 1 } ^ { s } b _ { i } ( \theta ) k _ { i } , \qquad z _ { 1 } ( \theta ) = z _ { 0 } + \sum _ { \ i = 1 } ^ { s } b _ { i } ( \theta ) \ell _ { i } ,
$$

where the $b _ { \imath } ( \theta )$ are polynomials which satisfy $b _ { i } ( 0 ) = 0$ ， $b _ { \ i } ( 1 ) = b _ { \ i }$ . In complete analogy to Theorem 4.8 we have

$$
\begin{array} { l l } { { y ( x _ { 0 } + \theta h ) - y _ { 1 } ( \theta ) = \displaystyle { \mathcal O } ( h ^ { p + 1 } ) } } & { { \mathrm { i f f } \quad \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( \theta ) \Phi _ { \imath } ( t ) = \displaystyle { \frac { \theta ^ { e ( t ) } } { \gamma ( t ) } } } } \\ { { } } & { { \mathrm { f o r } t \in D A T _ { y } , \varrho ( t ) \leq p , } } \\ { { \displaystyle z ( x _ { 0 } + \theta h ) - z _ { 1 } ( \theta ) = \displaystyle { \mathcal O } ( h ^ { q + 1 } ) } } & { { \mathrm { i f f } \quad \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( \theta ) \Phi _ { \imath } ( u ) = \displaystyle { \frac { \theta ^ { e ( u ) } } { \gamma ( u ) } } } } \end{array}
$$

In our situation ( $( s = 6$ ) it is easy to fulfill these conditions with $p = 3$ and $q = 2$ · The additional condition $b _ { s } ( \theta ) = \gamma \theta$ makes the solution unique.

Methods of Order 5. C. Schneider (1991b) first constructed stiffly accurate Rosenbrock methods of order 5 with $s \simeq 8$ stages. Di Marzo （1992) then determined carefully the free parameters to obtain $A$ -stability and small error constants. The resulting method, implemented in the code RODAS5, gives excellent results (see Sect. IV.10).

# Inconsistent Initial Values

Even if we start the computation with consistent initial values, the numerical solution $( y _ { n } , z _ { n } )$ of a Rosenbrock method does not, in general, satisfy $g ( y _ { n } , z _ { n } ) = 0$ It is therefore of interest to investigate the local error also for inconsistent initial

values $\left( { y _ { 0 } , z _ { 0 } } \right)$ . But what is the local error? To which solution of (4.1) should we compare the numerical values? If

$$
\| ( g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) \| \leq \delta
$$

with sufficiently small $\delta$ , we can find (because of (1.7)) a locally unique $\widehat { z } _ { 0 }$ which satisfies $g ( y _ { 0 } , \widehat { z } _ { 0 } ) = 0$ . It is natural to compare the numerical solution $( y _ { 1 } , z _ { 1 } )$ t0 that solution of (4.1) which passes through $( y _ { 0 } , \widehat { z } _ { 0 } )$

Our first aim is to write this solution in terms of elementary differentials evaluated at $( y _ { 0 } , z _ { 0 } )$ . Using

$$
\begin{array} { r } { \widehat { z } _ { 0 } - z _ { 0 } = ( - g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( \delta ^ { 2 } ) , } \end{array}
$$

which is a consequence of $0 = g ( y _ { 0 } , z _ { 0 } ) + g _ { z } ( y _ { 0 } , z _ { 0 } ) ( \widehat { z } _ { 0 } - z _ { 0 } ) + . . . , \mathrm { w e ~ g e t }$

$$
\begin{array} { r l } & { y ( x _ { 0 } + h ) = y _ { 0 } + h f ( y _ { 0 } , \hat { z } _ { 0 } ) + \mathcal { O } ( h ^ { 2 } ) } \\ & { \qquad = y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) + h ( f _ { z } ( - g _ { z } ^ { - 1 } ) g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( h ^ { 2 } + h \delta ^ { 2 } ) } \\ & { z ( x _ { 0 } + h ) = \hat { z } _ { 0 } + h ( - g _ { z } ^ { - 1 } g _ { y } f ) ( y _ { 0 } , \hat { z } _ { 0 } ) + \mathcal { O } ( h ^ { 2 } ) } \\ & { \qquad = z _ { 0 } + ( - g _ { z } ^ { - 1 } g ) \big ( y _ { 0 } , z _ { 0 } ) + h ( - g _ { z } ^ { - 1 } g _ { y } f ) ( y _ { 0 } , z _ { 0 } ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { z z } \big ( - g _ { z } ^ { - 1 } g , - g _ { z } ^ { - 1 } g _ { y } f \big ) \big ) ( y _ { 0 } , z _ { 0 } ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { y z } \big ( f , - g _ { z } ^ { - 1 } g \big ) \big ) \big ( y _ { 0 } , z _ { 0 } \big ) } \\ & { \qquad + h \big ( - g _ { z } ^ { - 1 } g _ { y } f _ { z } \big ( - g _ { z } ^ { - 1 } \big ) g \big ) \big ( y _ { 0 } , z _ { 0 } \big ) + \mathcal { O } ( h ^ { 2 } + \hat { \delta } ^ { 2 } ) } \end{array}
$$

The expressions so obtained allow a nice interpretation using trees. We only have to add in the recursive Definition 4.1 a tree of order O, which consists of a fat root. We denote this tree by $\varnothing _ { z }$ ，and extend Definition 4.3 by seting $F ( \varnothing _ { z } ) ( y , z ) =$ $( - g _ { z } ^ { - 1 } g ) ( y , z )$ . Then, the exprcssions of (4.49) and (4.50) correspond to the trees of Fig. 4.4.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/68886b7ca0226b8f0357b7465c20aa372be2fede485e6940f61bffb82526eb12.jpg)  
Fig. 4.4. Trees,to be considered for inconsistent initial values

The numerical solution also possesses an expansion of the form (4.49), (4.50) with additional method-dependent coefficients. The first few terms are as follows:

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + \displaystyle \left( \sum _ { \iota } b _ { \iota } \right) h f ( y _ { 0 } , z _ { 0 } ) + \displaystyle \left( \sum _ { \iota , y , k } b _ { \iota } \beta _ { \iota j } \omega _ { \jmath k } \right) h ( f _ { z } ( - g _ { \iota } ^ { - 1 } ) g ) ( y _ { 0 } , z _ { 0 } ) } } \\ { { \qquad \quad + \mathcal { O } ( h ^ { 2 } + h \delta ^ { 2 } ) } } \\ { { z _ { 1 } = z _ { 0 } + \displaystyle \left( \sum _ { \iota , y } b _ { \iota } \omega _ { \iota j } \right) ( - g _ { z } ^ { - 1 } g ) ( y _ { 0 } , z _ { 0 } ) + \mathcal { O } ( h + \delta ^ { 2 } ) . } } \end{array}
$$

In order to understand the form of these new coefficients we have to cxtend the proof of Theorem 4.6. It turns out that the elementary differentials are multiplicd by $\begin{array} { r } { \gamma ( t ) \sum _ { \iota } b _ { \iota } \Phi _ { \iota } ( t ) } \end{array}$ or $\gamma ( \mathfrak { u } ) \sum , b _ { \iota } \Phi _ { \iota } ( \mathfrak { u } )$ ,where $\gamma$ and $\Phi _ { \iota }$ are defined by $\gamma ( \emptyset _ { z } ) =$

1, $\begin{array} { r } { \Phi _ { i } ( \emptyset _ { z } ) = \sum _ { j } \omega _ { \iota j } } \end{array}$ and the recursion of Theorem 4.6. Equating the coeficients of the exact and numerical solutions yields new order conditions for the case of inconsistent initial values. The first of these (to be added to those of Table IV.7.1 and Table 4.1) are presented in Table 4.2.

Table 4.2. Order conditions for inconsistent initial values   

<table><tr><td>tree</td><td>order condition</td><td>size of error term</td></tr><tr><td>Y</td><td>∑baazywk=1/2</td><td>O(h²8）</td></tr><tr><td>。</td><td>∑bw=1</td><td>0(8）</td></tr><tr><td>10</td><td>∑bwaαjkwkl=1</td><td>O(hs)</td></tr></table>

Remarks. a) The first condition of Table 4.2 is exactly the same as that found by van Veldhuizen (1984) in a different context. It implies that the local error of the $y$ -component is of size $\mathcal { O } ( h ^ { p + 1 } + h ^ { 3 } \delta + h \delta ^ { 2 } )$

b) Condition $\sum _ { \iota _ { 1 } } b _ { \iota _ { 2 } } \omega _ { \iota _ { 2 } } = 1$ means that the stability function satisfies $R ( \infty ) =$ O.Unless this condition is satisfied, the local error of the $z$ -component contains an $h$ -independent term of size $\delta$ (which usually is near to $T o l$ ). This was observed numerically in Fig.IV.7.4 and explains the phenomenon of Fig.IV.7.3.

c) For Rosenbrock methods which satisfy (4.39), the second and third conditions of Table 4.2 are automatically fulfilled. For such methods the local error of the $z$ -component is of size $\mathcal { O } ( h ^ { q + \mathrm { i } } + h ^ { 2 } \delta + \delta ^ { 2 } )$

# Exercises

1. (Roche 1989). Consider the implicit Runge-Kutta method (1.11) applied to (1.6).

a) Prove that $z _ { 1 } - z ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { q + 1 } )$ iff

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } \Phi _ { \ i } ( u ) = \frac 1 { \gamma ( u ) } \qquad \mathrm { ~ f o r ~ } \quad u \in D A T _ { \ o z } , \ \varrho ( u ) \le q ,
$$

where $\gamma ( u )$ and $\Phi _ { \imath } ( u )$ arede $\alpha _ { \imath \jmath }$ and $\beta _ { \imath \jmath }$ are replaced bytheRunge-Kutcoefficients $a _ { \imath \jmath }$

b) Show that those trees in $D A T _ { z }$ which have more than one fat vertex,are redundant.

2. The simplifying assumptions (4.39) imply that many of the (algebraic) order conditions are automatically satisfied. Characterize the corresponding trees.

3.State the order condition for the tree $\left[ \tau _ { y } , \left[ \tau _ { y } , \emptyset _ { z } \right] _ { z } \right] _ { z }$

a) Show that the corresponding error term is of size $\mathcal { O } ( h ^ { 2 } \delta )$ with $\delta$ given in (4.48). b)For methods satisfying (4.39),this condition is equivalent to (4.44).

4.(Ostermann 1990). Suppose that the Rosenbrock method (4.3) satisfies (4.27). Define polynomials $b _ { \imath } ( \theta )$ of degree $q = [ ( p + 1 ) / 2 ]$ by $b _ { \imath } ( 0 ) = 0$ ， $b _ { \ i } ( 1 ) = b _ { \ i }$ ， and

$$
\int _ { 0 } ^ { 1 } b _ { \iota } ( \theta ) \theta ^ { \ell - 1 } \ d \theta = \left\{ \begin{array} { l l } { \sum _ { \ j } b _ { \ j } \big ( \alpha _ { \ j \iota } + \gamma _ { \ j \iota } \big ) } & { \quad \mathrm { i f ~ } \ \ell = 1 } \\ { \sum _ { \ j } b _ { \ j } \alpha _ { \ j } ^ { \ell - 1 } \alpha _ { \ j \iota } } & { \quad \mathrm { i f ~ } \ \ell = 2 , \dots , q - 1 . } \end{array} \right.
$$

Prove that the error of the dense output formulas (4.46) is $\mathcal { O } ( h ^ { q + 1 } )$

Hint. Extend the ideas of Exercise II.17.5 to Rosenbrock methods.

5. Suppose that a Rosenbrock method is implemented in the form (IV.7.25). If it satisfies (4.39), then its last two stages allow a very simple implementation

Hint. Prove that

$$
m _ { \ i } = \left\{ \begin{array} { l l } { { a _ { s \ i } ~ } } & { { \ i = 1 , \ldots , s - 1 } } \\ { { 1 ~ } } & { { \ i = s ~ , } } \end{array} \right. \qquad a _ { s \ i } = \left\{ \begin{array} { l l } { { a _ { s - 1 , s } ~ } } & { { \ i = 1 , \ldots , s - 2 } } \\ { { 1 ~ } } & { { \ i = s - 1 ~ . } } \end{array} \right.
$$

6.Partitioned Rosenbrock methods (Rentrop,Roche & Steinebach 1989). Consider the method (4.3） with $f _ { y }$ and $f _ { z }$ replaced by 0. Derive necessary and sufficient conditions that it be of order $p$

Remark. Case (a) of Lemma 4.9 remains valid in this new situation. However, the trees of Lemma 4.9b give rise to new conditions.

7. What is the“algebraic order”of the classical 4th order Rosenbrock methods of Section IV.7?

8. Let $\left\{ u _ { n } \right\} , \left\{ v _ { n } \right\}$ be two sequences of non-negative numbers satisfying (componentwise)

$$
\binom { u _ { n + 1 } } { v _ { n + 1 } } \leq \binom { 1 + h L } { N } \quad k M \bigg ) \binom { u _ { n } } { v _ { n } }
$$

with $0 \leq \kappa < 1$ and positive constants $L , M , N$ . Prove that for $h \leq h _ { 0 }$ and $n h \le C o n s t$

$$
u _ { n } \leq C ( u _ { 0 } + h v _ { 0 } ) , \qquad \quad v _ { n } \leq C ( u _ { 0 } + ( h + \kappa ^ { n } ) v _ { 0 } ) .
$$

Hint. Apply Lemma 3.9 with $\varepsilon = h$ and $M = 0$ .

The numerical computations of Sect.IV.1O have revealed the extrapolation code SEULEX as one of the best method for very stringent tolerances. The aim of the present section is to justify theoretically the underlying numerical method, the extrapolated linearly implicit Euler method, for singular perturbation problems as a representative of stiff equations.

# Linearly Implicit Euler Discretization

The linearly implicit Euler method (IV.9.25) applied to the singular perturbation problem (1.5) reads

$$
\left( \begin{array} { r r } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { \varepsilon I - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { l } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { l } { f ( y _ { \iota } , z _ { \iota } ) } \\ { g ( y _ { \iota } , z _ { \iota } ) } \end{array} \right) .
$$

Here we have used abbreviations such as $f _ { y } ( 0 ) = f _ { y } ( y _ { 0 } , z _ { 0 } )$ for the partial derivatives. We recall that the numerical approximations at $x _ { 0 } + H$ $\left( H = n h \right)$ are extrapolated according to (IV.9.26).

For the differential algebraic problem (1.6) we just put $\varepsilon = 0$ in (5.1). This yields

$$
\left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { c } { f ( y _ { \iota } , z _ { \iota } ) } \\ { g ( y _ { \iota } , z _ { \iota } ) } \end{array} \right) .
$$

Possible extensions to non-autonomous problems have been presented in Sect.IV.9. For problems $M u ^ { \prime } = \varphi ( u )$ we use the formulation (IV.9.34) also for singular $M$ Due to the invariance of the method with respect to the transformation (1.23),all results of this section are equally valid for $M u ^ { \prime } = \varphi ( u )$ of index 1.

The performance of extrapolation methods relies heavily on the existence of an asymptotic expansion of the global error. Such expansions are well understood, if the differential equation is nonstiff (see Sections II.8 and IV.9). But what happens if the problem is stiff or differential-algebraic?

Continued study of special problems is still a commendable way towards greater insight ... (E.Hopf 1950)

Example 5.1. Consider the test problem

$$
y ^ { \prime } = 1 , \qquad \varepsilon z ^ { \prime } = - z + g ( y ) .
$$

Method (5.1) yields the exact result $y _ { \imath } = x _ { \imath } = x _ { 0 } + i h$ for the $y$ -component, and the recursion

$$
( \varepsilon + h ) z _ { \iota + 1 } = \varepsilon z _ { \iota } + h g ( x _ { \iota } ) + h ^ { 2 } g ^ { \prime } ( x _ { 0 } )
$$

for the $z$ -component. In order to compute the coeficients of the asymptotic expansion (Theorem II.8.1), we insert

$$
z _ { \iota } = z ( x _ { \iota } ) + h b _ { 1 } ( x _ { \iota } ) + h ^ { 2 } b _ { 2 } ( x _ { \iota } ) + h ^ { 3 } b _ { 3 } ( x _ { \iota } ) + \ldots
$$

into (5.4),expand into a Taylor series and compare the coefficients of $h ^ { \jmath }$ .This yields the differential equation

$$
\varepsilon b _ { \bf 1 } ^ { \prime } ( x ) + b _ { \bf 1 } ( x ) = - \frac { \varepsilon } { 2 } z ^ { \prime \prime } ( x ) - z ^ { \prime } ( x ) + g ^ { \prime } ( x _ { 0 } )
$$

for $b _ { 1 } ( x )$ ， and similar ones for $b _ { 2 } ( x ) , b _ { 3 } ( x )$ , etc. Putting $\iota \ : = 0$ in (5.5） we get the initial values $b _ { \imath } ( x _ { 0 } ) = 0$ (all $\wr$ ). In general, the computation of the functions $b _ { 1 } ( x ) , \ b _ { 2 } ( x ) , \ldots$ is rather tedious. We therefore continue this example for the special case $x _ { 0 } = 0$ ， $g ( x ) = x ^ { 2 } + 2 \varepsilon x$ .and $z _ { 0 } = 0$ ,so that the exact solution of (5.3) is $z ( x ) = x ^ { 2 }$ . In this situation we get

$$
\begin{array} { l } { { b _ { 1 } ( x ) = - 3 \varepsilon e ^ { - r / \varepsilon } + 3 \varepsilon - 2 x } } \\ { { b _ { 2 } ( x ) = - \displaystyle \left( 1 + \frac { 3 x } { 2 \varepsilon } \right) e ^ { - x / \varepsilon } + 1 } } \\ { { b _ { 3 } ( x ) = \displaystyle \left( \frac { x } { 2 \varepsilon ^ { 2 } } - \frac { 3 x ^ { 2 } } { 8 \varepsilon ^ { 3 } } \right) e ^ { - x / \varepsilon } } } \end{array}
$$

etc. We observe that for $\varepsilon  0$ ,the function $b _ { 2 } ( x )$ becomes discontinuous at $x = 0$ ， and $b _ { 3 } \mathopen { } \mathclose \bgroup \left( x ^ { \ast } \aftergroup \egroup \right)$ is even not uniformly bounded. Hence, the expansion (5.5) is not useful for the study of extrapolation, if $\varepsilon$ is small compared to the step size $H$

The idea is now to omit in (5.6) the terms containing the factor $e ^ { - x / \varepsilon }$ by requiring that the functions $\boldsymbol { b } _ { \imath } ( \boldsymbol { x } )$ be smooth uniformly in $\boldsymbol { \mathcal { E } }$ and, instead, to add a discrete perturbation $\beta _ { \imath }$ to (5.5). For our example, this then becomes

$$
z _ { i } = x _ { \imath } ^ { 2 } + h ( 3 \varepsilon - 2 x _ { \imath } ) + h ^ { 2 } + \beta _ { \imath } .
$$

Inserting (5.7a) into (5.4) gives the relation $( \varepsilon + h ) { \beta _ { \iota + 1 } } = \varepsilon { \beta _ { \iota } }$ . The value of $\beta _ { 0 }$ is obtained from (5.7a) with $i \approx 0$ . We thus get

$$
\beta _ { \imath } = - \Big ( 1 + \frac { h } { \varepsilon } \Big ) ^ { - \imath } \big ( 3 \varepsilon h + h ^ { 2 } \big ) .
$$

If the numerical solution is extrapolated, the smooth terms in (5.7) are eliminated one after the other. It remains to study the effect of extrapolation on the perturbation terms $\beta _ { \ i }$ .If the differential equation is very stiff $\left( \varepsilon \ll h \right)$ ，these terms are very small and may be neglected over a wide range of $j _ { l }$ (observe that $i \geq n _ { 1 } )$ ，

Example 5.2.For the differential-algebraic problem

$$
y ^ { \prime } = 1 , \qquad 0 = - z + g ( y )
$$

with initial values $y _ { 0 } = x _ { 0 } , z _ { 0 } = g ( x _ { 0 } )$ the numerical solution, given by (5.2), is

$$
z _ { \ i } = \left\{ \begin{array} { l l } { { g ( x _ { 0 } ) } } & { { \mathrm { ~ f o r ~ } i = 0 \nonumber } } \\ { { g ( x _ { \ i - 1 } ) + h g ^ { \prime } ( x _ { 0 } ) } } & { { \mathrm { ~ f o r ~ } i \geq 1 \nonumber . } } \end{array} \right.
$$

Developing its second formula (for $i \geq 1$ yields

$$
z _ { \imath } = g ( x _ { \imath } ) + h \big ( g ^ { \prime } ( x _ { 0 } ) - g ^ { \prime } ( x _ { \imath } ) \big ) + \frac { h ^ { 2 } } { 2 } g ^ { \prime \prime } ( x _ { \imath } ) - \frac { h ^ { 3 } } { 6 } g ^ { \prime \prime \prime } ( x _ { \imath } ) + \mathcal { O } ( h ^ { 4 } ) .
$$

If we add the perturbation

$$
\beta _ { \imath } = h \beta _ { i } ^ { 1 } + h ^ { 2 } \beta _ { \imath } ^ { 2 } + h ^ { 3 } \beta _ { i } ^ { 3 } + \ldots
$$

(which is different from zero only for $i \approx 0$ ) we get for all $i$

$$
z _ { \imath } - g ( x _ { \imath } ) = \sum _ { \jmath = 1 } ^ { 3 } h ^ { j } ( b _ { j } ( x _ { i } ) + \beta _ { i } ^ { j } ) + \mathcal { O } ( h ^ { 4 } )
$$

where

$$
b _ { 1 } ( x ) = g ^ { \prime } ( x _ { 0 } ) - g ^ { \prime } ( x ) , \quad b _ { 2 } ( x ) = \frac { 1 } { 2 } g ^ { \prime \prime } ( x ) , \quad b _ { 3 } ( x ) = - \frac { 1 } { 6 } g ^ { \prime \prime \prime } ( x )
$$

are smooth functions and the perturbations are given by

$$
\beta _ { 0 } ^ { 1 } = 0 , \quad \beta _ { 0 } ^ { 2 } = - { \frac { 1 } { 2 } } g ^ { \prime \prime } ( x _ { 0 } ) , \quad \beta _ { 0 } ^ { 3 } = { \frac { 1 } { 6 } } g ^ { \prime \prime \prime } ( x _ { 0 } ) .
$$

If we add a further algebraic equation to (5.8), e.g., $0 = u - k ( z )$ ， and again apply Method (5.2)，we get three different formulas for $u _ { \iota }$ ，one for $\iota \approx 0$ ，one for $i = 1$ ，and a different one for $i \geq 2$ . In an expansion of the type (5.10) for $u _ { \iota } - k \big ( g \big ( x _ { \iota } \big ) \big )$ , perturbation terms will be present for $i \approx 0$ and for $i \approx 1$

# Perturbed Asymptotic Expansion

For general differential algebraic problems we have the following result.

Theorem 5.3 (Deuflhard, Hairer & Zugck 1987). Consider the problem (1.6) with consistent initial values $( y _ { 0 } , z _ { 0 } )$ , and suppose that (1.7) is satisfied. The global error of the linearly implicit Euler method (5.2) then has an asymptotic $h$ -expansion of the form

$$
\begin{array} { l } { { \displaystyle y _ { \imath } - y \big ( x _ { \imath } \big ) = \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( a _ { \jmath } \big ( x _ { i } \big ) + \alpha _ { \imath } ^ { \jmath } \big ) + \mathcal { O } \big ( h ^ { M + 1 } \big ) } } \\ { { \displaystyle z _ { \imath } - z \big ( x _ { \imath } \big ) = \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } \big ( x _ { i } \big ) + \beta _ { \imath } ^ { \jmath } \big ) + \mathcal { O } \big ( h ^ { M + 1 } \big ) } } \end{array}
$$

where $a _ { \ j } ( \ j ) , \ j _ { \ j } ( \ j )$ are smooth functions and the perturbations satisfy (see Table 5.1 and 5.2)

$$
\begin{array} { r l } { \alpha _ { \iota } ^ { 1 } = 0 , \quad \alpha _ { \iota } ^ { 2 } = 0 , } & { \alpha _ { \iota } ^ { 3 } = 0 , \quad \beta _ { \iota } ^ { 1 } = 0 \quad \quad f o r \ \iota \geq 0 } \\ { \beta _ { \iota } ^ { 2 } = 0 \quad } & { f o r \ \iota \geq 1 } \\ { \alpha _ { \iota } ^ { \jmath } = 0 \quad } & { f o r \ \iota \geq j - 4 \ a n d \ \jmath \geq 4 } \\ { \beta _ { \iota } ^ { \jmath } = 0 \quad } & { f o r \ \iota \geq j - 2 \ a n d \ j \geq 3 . } \end{array}
$$

The error terms in (5.11) are uniformly bounded for $x _ { \ i } = i h \le H$ ， $i f ~ H$ is sufficiently small.

Table 5.1.Non-zero $\alpha$ 's

Table 5.2.Non-zero $\beta$ 's

$$
\begin{array} { c c } { \small { ( \begin{array} { c c c c c c c c c c c c c c c c } { \small { b } } & { \small { h } } & { h ^ { 2 } } & { h ^ { 3 } } & { h ^ { 4 } } & { h ^ { 5 } } & { h ^ { 6 } } & { h ^ { 7 } } & { \small { ( \begin{array} { c c c c c c c c c c c c } { \boxed { h } } & { h ^ { 2 } } & { h ^ { 3 } } & { h ^ { 3 } } & { h ^ { 4 } } & { h ^ { 5 } } & { h ^ { 6 } } & { h ^ { 7 } } & { h ^ { 7 } } & { h ^ { 7 } } & { h ^ { 8 } } & { h ^ { 7 } } & { h ^ { 7 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 2 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 3 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } & { \ast } \\ { y _ { 4 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \ast } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \ast } & { \ast } & { \ast } \\ { y _ { 5 } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } & { \omega } \end{array} ) } } \end{array} ) } } \end{array} \quad \begin{array} { c c c c c c c c c c c c }  \small  ( \begin{array} { c c c c c c c c c } { \box { h } } & { h ^ { 2 } } &  h  \end{array} \end{array}
$$

Proof. In part (a) we shall recursively construct truncated expansions

$$
\begin{array} { l } { \widehat { y } _ { \iota } = y ( x _ { \iota } ) + \displaystyle \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( a _ { \jmath } ( x _ { \iota } ) + \alpha _ { \iota } ^ { \jmath } \big ) + h ^ { M + 1 } \alpha _ { \iota } ^ { M + 1 } } \\ { \widehat { z } _ { \iota } = z ( x _ { \iota } ) + \displaystyle \sum _ { \jmath = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } ( x _ { \iota } ) + \beta _ { \iota } ^ { \jmath } \big ) } \end{array}
$$

such that the defect of $\widehat { \boldsymbol { y } } _ { \iota } , \widehat { \boldsymbol { z } } _ { \iota }$ inserted into the method is small; more precisely, we require that

$$
\begin{array} { r } { \left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c c } { \widehat { y } _ { \iota + 1 } - \widehat { y } _ { \iota } } \\ { \widehat { z } _ { i + 1 } - \widehat { z } _ { \iota } } \end{array} \right) = h \left( \begin{array} { c c } { f ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \\ { g ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \end{array} \right) + { \mathcal O } ( h ^ { M + 2 } ) . } \end{array}
$$

For the initial values we rquire $\widehat { y } _ { 0 } = y _ { 0 } , \widehat { z } _ { 0 } = z _ { 0 }$ , or equivalently

$$
a _ { \ i } ( 0 ) + \alpha _ { 0 } ^ { \ i } = 0 , \qquad b _ { \ i } ( 0 ) + \beta _ { 0 } ^ { \ j } = 0 ,
$$

and the perturbation terms are assumed to satisfy

$$
\alpha _ { \ i } ^ { \ j }  0 , \qquad \beta _ { \ i } ^ { \ j }  0 \qquad \mathrm { f o r } \quad \ i  \infty ,
$$

otherwise, these limits could be added to the smooth parts. The result will then follow from a stability estimate derived in part (b).

a) For the construction of $a _ { \ j } ( \boldsymbol { x } ) , b _ { \ j } ( \boldsymbol { x } ) , \alpha _ { \iota } ^ { \ j } , \beta _ { \iota } ^ { \ j }$ we insert (5.13) into (5.14), and develop

$$
\begin{array} { c } { { f ( \widehat { y } _ { \imath } , \widehat { z } _ { \imath } ) = f \bigl ( y ( x _ { \imath } ) , z ( x _ { \imath } ) \bigr ) + f _ { y } ( x _ { \imath } ) \bigl ( h a _ { 1 } ( x _ { \imath } ) + h \alpha _ { \imath } ^ { 1 } + \ldots \bigr ) } } \\ { { + f _ { z } ( x _ { \imath } ) \bigl ( h b _ { 1 } ( x _ { \imath } ) + h \beta _ { \imath } ^ { 1 } + \ldots \bigr ) } } \\ { { + f _ { y y } ( x _ { \imath } ) \bigl ( h a _ { 1 } ( x _ { \imath } ) + h \alpha _ { \imath } ^ { 1 } + \ldots \bigr ) ^ { 2 } + \ldots , } } \\ { { { \widehat { y } } _ { \imath + 1 } - \widehat { y } _ { \imath } = y ( x _ { \imath + 1 } ) - y ( x _ { \imath } ) + h \bigl ( a _ { 1 } ( x _ { \imath + 1 } ) - a _ { 1 } ( x _ { \imath } ) + \alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 } \bigr ) + \ldots } } \\ { { = h y ^ { \prime } ( x _ { \imath } ) + \displaystyle \frac { h ^ { 2 } } { 2 } y ^ { \prime \prime } ( x _ { \imath } ) + \ldots + h ^ { 2 } a _ { 1 } ^ { \prime } ( x _ { \imath } ) + h ( \alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 } ) + \ldots , } } \end{array}
$$

where $f _ { y } ( x ) = f _ { y } ( y ( x ) , z ( x ) )$ , etc. Similarly, we develop $g ( \widehat { y } _ { \imath } , \widehat { z } _ { \imath } )$ and $\widehat { z } _ { \iota + 1 } - \widehat { z } _ { \iota }$ ， and compare coefficients of $h ^ { j + 1 }$ (for $j = 0 , \ldots , M )$ . Each power of $h$ will lead to two conditions - one containing the smooth functions and the other containing the perturbation terms.

First step. Equating the coefficients of $h ^ { 1 }$ yields the equations (1.6) for the smooth part (due to consistency of the method), and $\alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { i } ^ { 1 } = 0$ for $i \geq 0$ Because of (5.16) we get $\alpha _ { \ i } ^ { \ i } = 0$ for all $i \geq 0$ (compare (5.12a)).

Second step. The coeficents of $h ^ { 2 }$ give

$$
\begin{array} { c l l } { { a _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { 1 } { 2 } y ^ { \prime \prime } ( x ) - f _ { y } ( 0 ) y ^ { \prime } ( x ) - f _ { z } ( 0 ) z ^ { \prime } ( x ) = f _ { y } ( x ) a _ { 1 } ( x ) + f _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { - g _ { y } ( 0 ) y ^ { \prime } ( x ) - g _ { z } ( 0 ) z ^ { \prime } ( x ) = g _ { y } ( x ) a _ { 1 } ( x ) + g _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { \alpha _ { \imath + 1 } ^ { 2 } - \alpha _ { \imath } ^ { 2 } - f _ { z } ( 0 ) ( \beta _ { \imath + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 } ) = f _ { z } ( 0 ) \beta _ { \imath } ^ { 1 } } } \\ { { - g _ { z } ( 0 ) ( \beta _ { \imath + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 } ) = g _ { z } ( 0 ) \beta _ { \imath } ^ { 1 } . } } \end{array}
$$

Observe that the coefficients $\alpha _ { \ i } ^ { \ell } , \beta _ { \ i } ^ { \ell }$ have to be independent of $h , s 0$ that $f _ { z } ( 0 )$ ， $g _ { z } ( 0 )$ cannot be replaced by $f _ { z } ( x _ { \imath } ) , g _ { z } ( x _ { \imath } )$ in the right-hand sides of (5.17c, d). The system (5.17) can be solved as follows. Compute $b _ { 1 } ( x )$ from (5.17b） and insert it into (5.17a). This gives a linear differential equation for $a _ { 1 } ( x )$ .Because of (5.15) and $\alpha _ { 0 } ^ { 1 } = 0$ the initial value is $a _ { 1 } ( 0 ) = 0$ . Therefore $a _ { 1 } ( x )$ and $b _ { 1 } ( x )$ are uniquely determined by (5.17a, b).Differentiating $g ( y ( x ) , z ( x ) ) = 0$ and putting $x \approx 0$ implies that the left-hand side of (5.17b) vanishes at $x \approx 0$ . Consequently, we have $b _ { 1 } ( 0 ) = 0$ and by (5.15),also $\beta _ { 0 } ^ { 1 } = 0$ . Condition (5.17d) then implies $\beta _ { \imath } ^ { 1 } = 0$ (all $i$ ), and (5.17c) together with (5.16) give $\alpha _ { \ i } ^ { 2 } = 0 \ ( \mathrm { a l l } \ i )$

Third step. As in the second step we get (for $j = 2$ ）

$$
\begin{array} { r } { a _ { \jmath } ^ { \prime } ( x ) = f _ { y } ( x ) a _ { \jmath } ( x ) + f _ { z } ( x ) b _ { \jmath } ( x ) + r ( x ) } \\ { 0 = g _ { y } ( x ) a _ { \jmath } ( x ) + g _ { z } ( x ) b _ { \jmath } ( x ) + s ( x ) , } \end{array}
$$

where $r ( x ) , s ( x )$ are known functions depending on derivatives of $y ( x ) , z ( x )$ ， and on $a _ { \ell } ( x ) , b _ { \ell } ( x )$ with $\ell \leq j - 1$ . We further get

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 3 } - \alpha _ { \iota } ^ { 3 } = f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } } \\ { 0 = g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } . } \end{array}
$$

We compute $a _ { 2 } ( x ) , b _ { 2 } ( x )$ as in step 2. However, $b _ { 2 } ( 0 ) \neq 0$ in general,and for the first time, we are forced to introduce a perturbation term $\beta _ { 0 } ^ { 2 } \neq 0$ . From (5.18c,d) we then get $\beta _ { \imath } ^ { 2 } = 0$ (for $i \geq 1 $ and $\alpha _ { \ i } ^ { 3 } = 0$ (for all $\textit { \textbf { l } }$ ）

Fourth step. Comparing the coefficients of $h ^ { 4 }$ we just get (5.18a,b) with $j = 3$ and (5.18c,d) with the upper index raised by 1. As above we conclude ${ \beta } _ { \ i } ^ { 3 } = 0$ (for $i \geq 1$ and $\alpha _ { \ i } ^ { 4 } = 0$ (for all $i$ ).

General step. The conditions for the smooth functions are (5.18a,b). For the perturbation terms we get

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { \jmath + 1 } - \alpha _ { \iota } ^ { \jmath + 1 } = f _ { \boldsymbol { z } } ( 0 ) \beta _ { \iota + 1 } ^ { \jmath } + \varrho _ { \iota } ^ { \jmath } } \\ { 0 = g _ { \boldsymbol { z } } ( 0 ) \beta _ { \iota + 1 } ^ { \jmath } + \sigma _ { \iota } ^ { \jmath } , } \end{array}
$$

where $\boldsymbol { \underline { { \varrho } } } _ { \iota } ^ { \jmath } , \boldsymbol { \sigma } _ { \iota } ^ { \jmath }$ are linear combinations of expressions which contain as factors $\alpha _ { \imath + 1 } ^ { \ell } , \ \alpha _ { \imath } ^ { \ell - 1 }$ β-1 with $\ell \leq j$ . For example, we have $\varrho _ { \imath } ^ { 4 } = f _ { z z } ( 0 ) ( \beta _ { \imath } ^ { 2 } ) ^ { 2 }$ and $\sigma _ { \imath } ^ { 4 } = g _ { z z } ( 0 ) ( \beta _ { \imath } ^ { 2 } ) ^ { 2 }$ ．The proof of (5.12) is now by induction on $j$ By the induction hypothesis we have ${ \varrho _ { \mathrm { \ell } _ { \mathrm { : } } } ^ { \mathrm { \mathcal { I } } } } = 0$ ， $\sigma _ { \ i } ^ { \ j } = 0$ for $\iota \geq j - 3$ . Formula (5.19d) hence implies $\beta _ { \iota + 1 } ^ { J } = 0$ (for $i \geq j - 3 )$ and (5.19c) together with (5.16) gives $\alpha _ { \iota } ^ { \jmath + 1 } = 0$ (for $i \geq \jmath - 3 )$ . But this is simply the statement $( 5 . 1 2 \mathrm { c } , \mathrm { d } )$

b) We still have to estimate the remainder term,i.e., differences $\Delta y _ { \imath } = y _ { \imath } - \widehat { y } _ { \imath }$ ， $\Delta z _ { \imath } = z _ { \imath } - \widehat { z } _ { \imath }$ . Subtracting (5.14) from (5.2) and eliminating $\Delta y _ { i + 1 } , \Delta z _ { i + 1 }$ yields

$$
\begin{array} { r l } & { \left( \begin{array} { l } { \Delta y _ { \iota + 1 } } \\ { \Delta z _ { \iota + 1 } } \end{array} \right) = \left( \begin{array} { l } { \Delta y _ { \iota } } \\ { \Delta z _ { \iota } } \end{array} \right) } \\ & { \qquad + \left( \begin{array} { l l } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { - g _ { z } ^ { - 1 } ( 0 ) } \end{array} \right) \left( \begin{array} { l } { h \big ( f ( y _ { \iota } , z _ { \iota } ) - f ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) \big ) } \\ { g ( y _ { \iota } , z _ { \iota } ) - g ( \widehat { y } _ { \iota } , \widehat { z } _ { \iota } ) } \end{array} \right) + \left( \begin{array} { l } { \mathcal { O } ( h ^ { M + 2 } ) } \\ { \mathcal { O } ( h ^ { M + 1 } ) } \end{array} \right) . } \end{array}
$$

The application of a Lipschitz condition for $f ( y , z )$ and $g \{ y , z \}$ then gives

$$
\begin{array} { r } { \left( \begin{array} { l } { \left\| \Delta y _ { \imath + 1 } \right\| } \\ { \left\| \Delta z _ { \imath + 1 } \right\| } \end{array} \right) \leq \left( \begin{array} { l l } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { \varrho } \end{array} \right) \left( \left\| \Delta y _ { \imath } \right\| \right) + \left( \mathcal { O } ( h ^ { M + 2 } ) \right) , } \end{array}
$$

where $| \varrho \} < 1$ if $H$ is sufficiently small. Applying Lemma 3.9 we deduce ${ \| \Delta y _ { \imath } \| + }$ $\| \Delta z _ { \imath } \| = \mathcal { O } \big ( h ^ { M + 1 } \big )$ □

# Order Tableau

We consider (5.2) as our basic method for extrapolation, i.e., we takc some step number sequence $n _ { 1 } < n _ { 2 } < \ldots .$ ，put ${ \hslash } _ { \mathit { 1 } } = H / n _ { \mathit { 1 } }$ , and define

$$
Y _ { \ j 1 } = y _ { h _ { \ j } } ( x _ { 0 } + H ) , \qquad Z _ { \ j 1 } = z _ { h _ { \ j } } ( x _ { 0 } + H ) ,
$$

the numerical solution of (1.6) after $n _ { \jmath }$ steps with step size ${ \boldsymbol { \jmath } } _ { \boldsymbol { \imath } , \boldsymbol { \imath } }$ . We then extrapolate these values according to (IV.9.26) and obtain $Y _ { \jmath k } , Z _ { \jmath k }$ . What is the order of the approximations thus obtained?

Theorem 5.4 (Deuflhard, Hairer & Zugck 1987). If we consider the harmonic sequence $\{ 1 , 2 , 3 , 4 , \ldots \}$ , then the extrapolated values $Y _ { j k } , ~ Z _ { j k }$ satisfy

$$
Y _ { \jmath k } - y ( x _ { 0 } + h ) = { \mathcal O } ( H ^ { r _ { \jmath k } + 1 } ) , \qquad Z _ { \jmath k } - z ( x _ { 0 } + H ) = { \mathcal O } ( H ^ { s _ { \jmath k } } )
$$

where the differential-algebraic orders $\boldsymbol { r } _ { \jmath k } , s _ { \jmath k }$ are given in Tables 5.3 and 5.5.

# Table 5.3.orders $r _ { j k }$

Table 5.4. orders S jk · $\begin{array} { l } { { \begin{array} { l l l l l l l l l } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 5 } } & { { } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 5 } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } \\ { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } \end{array} } } \end{array}$ 5 5

4 7 48 4 4

Proof. We use the expansion (5.11). It follows from $\alpha _ { \ i } ^ { 1 } = \beta _ { \ i } ^ { 1 } = 0$ (for all $i \geq 0$ ） and from (5.15) that $a _ { 1 } ( x _ { 0 } ) = b _ { 1 } ( x _ { 0 } ) = 0$ . Since $a _ { \ j } ( \ j x )$ and $\boldsymbol { b } _ { \ u { \jmath } } ( \boldsymbol { x } )$ are smooth functions we obtain $a _ { 1 } ( x _ { 0 } + H ) = \mathcal { O } ( H )$ ， $b _ { 1 } ( x _ { 0 } + H ) = \mathcal { O } ( H )$ and the errors of $Y _ { j 1 } , Z _ { j 1 }$ $\mathcal { O } ( H ^ { 2 } )$   
$a _ { 2 } ( x _ { 0 } + H ) = { \mathcal { O } } ( H )$ However, since $\beta _ { 0 } ^ { 2 } \neq 0$ in general, we have $b _ { 2 } ( x _ { 0 } ) \neq 0$ by (5.15) and the term $b _ { 2 } ( x _ { 0 } + H )$ is only of size $\mathcal { O } ( 1 )$ . One extrapolation of the numerical solution eliminates the terms with $j = 1$ in (5.11). The error is thus of size $\mathcal { O } ( H ^ { 3 } )$ for $Y _ { _ { \jmath 2 } }$ but only $\mathcal { O } ( H ^ { 2 } )$ for $Z _ { j 2 }$ , verifying the second columns of Tables 5.3 and 5.4. If we continue the extrapolation process, the smooth parts of the error expansion (5.11) are eliminated one after the other. The perturbation terms, however, are not eliminated.

For the $y$ -component the first non-vanishing perturbation for $i \geq n _ { 1 } = 1$ is $\alpha _ { 1 } ^ { 6 }$ Therefore, the diagonal elements of the extrapolation tableau for the $y$ -component (Table 5.3) contain an error term of size $\mathcal { O } ( H ^ { 6 } )$ (observe that $\alpha _ { 1 } ^ { 6 }$ is multiplied by $h ^ { 6 }$ in (5.11). The elements $Y _ { j , \ j - 1 }$ of tefirstsubdiagonaldependonlyon $Y _ { \ell 1 } = y _ { n _ { \ell } }$ for $\ell \geq 2$ . Since $n _ { 2 } \geq 2$ , only the perturbations $\alpha _ { i } ^ { j }$ with $i \geq 2$ can have an influence. We see from (5.12) that the first non-vanishing perturbation for $i \geq 2$ is $\alpha _ { 2 } ^ { \overline { { \ell } } }$ . This explains the $\mathcal { O } ( H ^ { 7 } )$ error term in the first subdiagonal of Table 5.3.

For the $z$ -component, $\beta _ { 1 } ^ { 4 }$ is the first perturbation term for $i \geq 1$ . Hence the diagonal entries of the extrapolation tableau for the $z$ -component contain an error of size $\mathcal { O } ( H ^ { 4 } )$ . All other entries of Tables 5.3 and 5.4 can be verified analogously.

If we consider a step number sequence $\{ n _ { j } \}$ which is different from the harmonic sequence,we obtain the corresponding order tableaux as follows: the $j$ th diagonal of the new tableau is the $n _ { j }$ th diagonal of Table 5.3 and 5.4, respectively.

Theorem 5.4 then remains valid with $r _ { j k } , s _ { j k }$ given by these new tableaux. This implies that a larger $n _ { 1 }$ ，say ${ { \ n } _ { 1 } } = 2$ increases, the order of the extrapolated values. Numerical computations have shown that the sequence

$$
\{ 2 , 3 , 4 , 5 , 6 , \ldots \}
$$

is superior to the harmonic sequence. It is therefore recommended for SEULEX.

It is interesting to study the influence of the perturbation terms on the extra-polated values. Suppose that $\alpha _ { n _ { 1 } } ^ { j }$ (or $\beta _ { n _ { 1 } } ^ { j } )$ is the leading perturbation term in $Y _ { 1 1 }$ (or $Z _ { 1 1 }$ ). Because of the recursion (IV.9.26) all $Y _ { k k }$ then contain an error term of the form $C _ { k } H ^ { \jmath } \alpha _ { n _ { 1 } } ^ { \jmath }$ , whereas the $Y _ { \jmath k }$ (for $j > k$ ) do not depend on $\alpha _ { n _ { 1 } } ^ { \prime }$ . The error constants $C _ { k }$ are given recursively by

$$
C _ { 1 } = \frac { 1 } { n _ { 1 } ^ { J } } , \qquad C _ { k } = - \frac { n _ { 1 } } { n _ { k } - n _ { 1 } } C _ { k - 1 }
$$

and tend to zero exponentially, if $k$ increases.

# Error Expansion for Singular Perturbation Problems

Our aim is to extend the analysis of Example 5.1 to general singular perturbation problems

$$
\begin{array} { r l } { y ^ { \prime } = f ( y , z ) , \quad } & { { } y ( 0 ) = y _ { 0 } } \\ { \varepsilon z ^ { \prime } = g ( y , z ) , \quad } & { { } z ( 0 ) = z _ { 0 } , \quad 0 < \varepsilon \ll 1 , } \end{array}
$$

where the solution $y ( x ) , z ( x )$ is assumed to be sufficiently smooth (i.e., its deriva-tives up to a certain order are bounded independently of $\varepsilon$ ). An important observa-tion in Example 5.1 was the existence of smooth solutions of the (linear) differential equations for the coefficients $\boldsymbol { b } _ { \boldsymbol { \imath } } ( \boldsymbol { x } )$ . In the general situation we shall be concerned with equations of the form

$$
\begin{array} { r } { a ^ { \prime } = f _ { y } ( x ) a + f _ { z } ( x ) b + c ( x , \varepsilon ) } \\ { \varepsilon b ^ { \prime } = g _ { y } ( x ) a + g _ { z } ( x ) b + d ( x , \varepsilon ) } \end{array}
$$

(the coefficients $f _ { y } ( x ) = f _ { y } ( y ( x ) , z ( x ) )$ , etc. depend smoothly on $\varepsilon$ because the solution of (5.25) itself depends on $\varepsilon$ , even if $f$ and $g$ are $\varepsilon$ -independent).

Lemma 5.5. Suppose that the logarithmic norm of $g _ { z } ( x )$ satisfies

$$
\mu ( g _ { z } ( x ) ) \leq - 1 \qquad f o r \quad 0 \leq x \leq \overleftrightarrow { x } .
$$

For $a$ given value

$$
a ( 0 ) = a _ { 0 } ^ { 0 } + \varepsilon a _ { 0 } ^ { \perp } + \dots + \varepsilon ^ { N } a _ { 0 } ^ { N } + \mathcal { O } ( \varepsilon ^ { N + 1 } )
$$

there exists a unique $( u p t o \mathcal { O } ( \varepsilon ^ { N + 1 } ) )$

$$
b ( 0 ) = b _ { 0 } ^ { 0 } + \varepsilon b _ { 0 } ^ { 1 } + \dots + \varepsilon ^ { N } b _ { 0 } ^ { N } + \mathcal { O } ( \varepsilon ^ { N + 1 } )
$$

such that the solutions $a ( x )$ ， $b ( x )$ of (5.26) and their first $N$ derivatives are bounded independently of $\varepsilon$ ，

Proof. We insert the finite expansions

$$
\widehat { a } ( x ) = \sum _ { i = 0 } ^ { N } \varepsilon ^ { \prime } a _ { \ i } ( x ) , \quad \widehat { b } ( x ) = \sum _ { i = 0 } ^ { N } \varepsilon ^ { \prime } b _ { \ i } ( x )
$$

with $\varepsilon$ -independent coeficients $a _ { _ 2 } ( x ) b _ { i } ( x )$ into (5.26) and compare powers of $\varepsilon$ (see Section VI.2). This leads to the differential-algebraic system (2.4). Consequently, $a _ { 0 } ^ { 0 }$ determines $b _ { 0 } ^ { 0 }$ ; these two together with $a _ { 0 } ^ { 1 }$ determine $b _ { 0 } ^ { 1 }$ ,etc. The remainders $a ( x ) - { \widehat { a } } ( x ) , \ b ( x ) - { \widehat { b } } ( x )$ are then estimated as in the proof of Theorem 2.1. □

The next result exhibits the dominant perturbation terms in an asymptotic ex-pansion of the error of the linearly implicit Euler method, when it is applied to a singular perturbation problem.

Theorem 5.6 (Hairer&Lubich 1988). Assume that the solution of(5.25) is smooth. Under the condition

$$
\lVert ( I - \gamma g _ { z } ( 0 ) ) ^ { - 1 } \rVert \leq \frac { 1 } { 1 + \gamma } \qquad f o r a l l \quad \gamma \geq 1
$$

(which is a consequence of(5.27) and Theorem IV.11.2), the numerical solution of (5.1) possesses for $\varepsilon \leq h$ a perturbed asymptotic expansion of the form

$$
\begin{array} { l } { { y _ { i } = y ( x _ { i } ) + h a _ { 1 } ( x _ { i } ) + h ^ { 2 } a _ { 2 } ( x _ { i } ) + { \mathcal O } ( h ^ { 3 } ) } } \\ { { \displaystyle - \varepsilon f _ { z } ( 0 ) { g _ { z } ^ { - 1 } } ( 0 ) \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - \prime } \big ( h b _ { 1 } ( 0 ) + h ^ { 2 } b _ { 2 } ( 0 ) \big ) } } \\ { { z _ { \imath } = z ( x _ { \imath } ) + h b _ { 1 } ( x _ { \imath } ) + h ^ { 2 } b _ { 2 } ( x _ { \imath } ) + { \mathcal O } ( h ^ { 3 } ) } } \\ { { \displaystyle ~ - \left( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \right) ^ { - \displaystyle i } \big ( h b _ { 1 } ( 0 ) + h ^ { 2 } b _ { 2 } ( 0 ) \big ) } } \end{array}
$$

where $x _ { i } = i h \le H$ with $H$ sufficiently small (but independent of $\varepsilon$ ). The smooth functions $a _ { \ j } ( x ) , b _ { j } ( x )$ satisfy

$$
a _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ^ { 2 } ) , \quad a _ { 2 } ( 0 ) = \mathcal { O } ( \varepsilon ) , \quad b _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ) , \quad b _ { 2 } ( 0 ) = \mathcal { O } ( 1 ) .
$$

Proof. This proof is organized like that of Theorem 5.3. In part (a) we recursively construct truncated expansions (for $M \leq 2$ ）

$$
\begin{array} { l } { { \displaystyle { \widehat { y } } _ { i } = y \big ( x _ { i } \big ) + \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( a _ { j } \big ( x _ { i } \big ) + \alpha _ { i } ^ { \jmath } \big ) } } \\ { { \displaystyle { \widehat { z } } _ { \imath } = z \big ( x _ { i } \big ) + \sum _ { j = 1 } ^ { M } h ^ { \jmath } \big ( b _ { \jmath } \big ( x _ { i } \big ) + \beta _ { i } ^ { j } \big ) } } \end{array}
$$

such that

$$
\left( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { \varepsilon I - h g _ { z } ( 0 ) } \end{array} \right) \left( \begin{array} { c c } { \widehat { y } _ { i + 1 } - \widehat { y } _ { i } } \\ { \widehat { z } _ { i + 1 } - \widehat { z } _ { i } } \end{array} \right) = h \left( \begin{array} { c c } { f ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \\ { g ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \end{array} \right) + \mathcal { O } ( h ^ { M + 2 } ) .
$$

The smooth functions $a _ { _ { 3 } } ( x ) , b _ { j } ( x )$ clearly depend on $\boldsymbol { \varepsilon }$ , but are independent of $h$ . The perturbation terms $\alpha _ { \ i } ^ { j } , \beta _ { \ i } ^ { j }$ (for $i \geq 1$ ),however,willdepend smoothly on $\varepsilon$ and on $\varepsilon / h$ . As in the case $\varepsilon = 0$ , we shall require that (5.15) and (5.16) hold. The differences $y _ { \imath } - \widehat { y } _ { \imath }$ and $z _ { \imath } - \widehat { z } _ { \imath }$ will then be estimated in part b).

a) The case $M = 0$ is obvious. Indeed, the values $\widehat { \boldsymbol { y } } _ { \boldsymbol { \imath } } = \boldsymbol { y } ( \boldsymbol { x } _ { \boldsymbol { \imath } } )$ ， $\widehat { z } _ { \iota } = z ( x _ { \iota } )$ satisfy (5.32) with $M = 0$ . The construction of the coefficients in (5.31) is done in two steps.

First step $( M = 1 )$ .We insert (5.31) into (5.32) and compare the smooth coefficients of $h ^ { 2 }$ . This gives

$$
\begin{array} { c } { { a _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { 1 } { 2 } y ^ { \prime \prime } ( x ) - f _ { y } ( 0 ) y ^ { \prime } ( x ) - f _ { z } ( 0 ) z ^ { \prime } ( x ) = f _ { y } ( x ) a _ { 1 } ( x ) + f _ { z } ( x ) b _ { 1 } ( x ) } } \\ { { \varepsilon b _ { 1 } ^ { \prime } ( x ) + \displaystyle \frac { \varepsilon } { 2 } z ^ { \prime \prime } ( x ) - g _ { y } ( 0 ) y ^ { \prime } ( x ) - g _ { z } ( 0 ) z ^ { \prime } ( x ) = g _ { y } ( x ) a _ { 1 } ( x ) + g _ { z } ( x ) b _ { 1 } ( x ) } } \end{array}
$$

ByLemma 5.5 the initial value $b _ { \mathrm { 1 } } ( 0 )$ is uniquely determined by $a _ { \mathrm { \scriptsize ~ j } } ( 0 )$ . Differentiation of $\varepsilon z ^ { \prime } = g ( y , z )$ with respect to $\mathscr { x }$ gives $\varepsilon z ^ { \prime \prime } ( x ) = g _ { y } ( x ) y ^ { \prime } ( x ) + g _ { z } ( x ) z ^ { \prime } ( x )$ Inserted into (5.33b) this yields the relation

$$
g _ { y } ( 0 ) a _ { 1 } ( 0 ) + g _ { z } ( 0 ) b _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon )
$$

with known right-hand side.

As to the perturbation terms, we obtain by collecting everything up to $\mathcal { O } ( h ^ { 2 } )$

$$
\begin{array} { r l } { \alpha _ { i + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } - h f _ { y } ( 0 ) ( \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } ) - h f _ { z } ( 0 ) ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) } & { { } } \\ { = h f _ { y } ( x _ { \iota } ) \alpha _ { \iota } ^ { 1 } + h f _ { z } ( x _ { \iota } ) \beta _ { \iota } ^ { 1 } } & { { } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) - h g _ { y } ( 0 ) ( \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } ) - h g _ { z } ( 0 ) ( \beta _ { i + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) } & { { } } \\ { = h g _ { y } ( x _ { \iota } ) \alpha _ { \iota } ^ { 1 } + h g _ { z } ( x _ { \iota } ) \beta _ { \iota } ^ { 1 } } & { { } } \end{array}
$$

and try to determine the most important parts of this. We firstly replace $h f _ { y } ( x _ { \imath } ) \alpha _ { \imath } ^ { 1 }$ by $h f _ { y } ( 0 ) \alpha _ { \iota } ^ { 1 }$ and similarly for three other terms. This is motivated by the fact that we search for exponentially decaying $\alpha _ { \pmb { \imath } }$ . Therefore with $x _ { \imath } = i h$ ，

$$
\begin{array} { r } { \left( f _ { y } ( x _ { \imath } ) - f _ { y } ( 0 ) \right) \alpha _ { \imath } ^ { \rfloor } = \mathcal { O } ( h ) . } \end{array}
$$

Then many terms cancel in (5.35). We next observe that $\beta _ { i + 1 } ^ { 1 } - \beta _ { \imath } ^ { 1 }$ is multiplied by $\varepsilon$ ,but not $\alpha _ { \imath + 1 } ^ { 1 } - \alpha _ { \imath } ^ { 1 }$ . This suggests that the $\beta _ { \imath + \jmath } ^ { 1 }$ are an order of magnitude larger than $\boldsymbol \alpha _ { \imath + 1 } ^ { \mathrm { 1 } }$ . Neglecting therefore $\boldsymbol \alpha _ { \imath + 1 } ^ { 1 }$ where it competes with $\boldsymbol { \beta } _ { \iota + 1 } ^ { 1 }$ ,we are led to define

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 1 } - \alpha _ { \iota } ^ { 1 } = h f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 1 } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 1 } - \beta _ { \iota } ^ { 1 } ) = h g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 1 } . } \end{array}
$$

It remains to verify a posteriori, that there exist solutions of $( 5 . 3 3 \mathrm { a } , \mathrm { b } , \mathrm { c } , \mathrm { d } )$ which produce an error term $\mathcal O ( h ^ { 3 } )$ in (5.32): from (5.33d) we obtain

$$
\beta _ { \iota } ^ { 1 } = \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - \iota } \beta _ { 0 } ^ { 1 } .
$$

Since we require $\alpha _ { \imath } ^ { 1 }  0$ for $i \to \infty$ ,the solution of (5.33c) is given by

$$
\alpha _ { \iota } ^ { 1 } = \varepsilon f _ { z } ( 0 ) { g } _ { z } ^ { - 1 } ( 0 ) \Big ( I - \frac { h } { \varepsilon } { g } _ { z } ( 0 ) \Big ) ^ { - \iota } \beta _ { 0 } ^ { 1 } .
$$

For $i \approx 0$ this implies the relation

$$
\alpha _ { 0 } ^ { 1 } = \varepsilon f _ { z } ( 0 ) g _ { z } ^ { - 1 } ( 0 ) \beta _ { 0 } ^ { 1 } .
$$

The assumption (5.15) together with (5.34) and (5.37) uniquely determine the coefficients $a _ { 1 } ( 0 ) , b _ { 1 } ( 0 ) , \alpha _ { 0 } ^ { 1 } , \beta _ { 0 } ^ { 1 }$ . We remark that $b _ { \mathbf { 1 } } ( 0 ) = { \mathcal { O } } ( \varepsilon )$ and $a _ { 1 } ( 0 ) = \mathcal { O } ( \varepsilon ^ { 2 } )$ Using the fact that $\alpha _ { \ i } ^ { 1 } = \mathcal { O } ( \varepsilon ^ { 2 } )$ and $\varepsilon \leq h$ , one easily verifies that the quantities (5.31) with $M = 1$ satisfy (5.32).

Second step $M = 2 )$ . Comparing the smooth coefficients of $h ^ { 3 }$ in (5.32) gives two differential equations for $a _ { 2 } ( x ) , b _ { 2 } ( x )$ which are of the form (5.26). It follows from Lemma 5.5 that the initial values have to satisfy a relation

$$
g _ { y } ( 0 ) a _ { 2 } ( 0 ) + g _ { z } ( 0 ) b _ { 2 } ( 0 ) = \mathcal { O } ( 1 )
$$

with known right-hand side. As in the first step we require for the perturbations

$$
\begin{array} { r } { \alpha _ { \iota + 1 } ^ { 2 } - \alpha _ { \iota } ^ { 2 } = h f _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } } \\ { \varepsilon ( \beta _ { \iota + 1 } ^ { 2 } - \beta _ { \iota } ^ { 2 } ) = h g _ { z } ( 0 ) \beta _ { \iota + 1 } ^ { 2 } . } \end{array}
$$

and obtain the formulas (5.36) and (5.37) with $\alpha _ { \imath } ^ { 1 } , \beta _ { \imath } ^ { 1 }$ replaced by $\alpha _ { \ i } ^ { 2 } , \beta _ { \ i } ^ { 2 }$ . Again the values $a _ { 2 } ( 0 ) , b _ { 2 } ( 0 ) , \alpha _ { 0 } ^ { 2 } , \beta _ { 0 } ^ { 2 }$ are uniquely determined by (5.15), (5.38), and (5.37). Due to the $\mathcal { O } ( 1 )$ term in (5.38) we only have $b _ { 2 } ( 0 ) = \mathcal { O } ( 1 )$ and $a _ { 2 } ( 0 ) =$ ${ \mathcal { O } } ( \varepsilon )$

We still have to verify (5.32) with $M = 2$ . In the left-hand side we have ne-glected terms of the form $h f _ { y } ( 0 ) ( h \alpha _ { \iota } ^ { 1 } + h ^ { 2 } \alpha _ { i } ^ { 2 } )$ .This is justified,because $\alpha _ { \ i } ^ { 1 } =$ $\mathcal { O } ( \varepsilon ^ { 2 } )$ ， $\alpha _ { \ i } ^ { 2 } = \mathcal { O } ( \varepsilon )$ and $\varepsilon \leq h$ . The most dangerous term, neglected in the righthand side of (5.32) is

$$
h \big ( f _ { z } ( x _ { \imath } ) - f _ { z } ( 0 ) \big ) ( h \beta _ { \imath } ^ { 1 } + h ^ { 2 } \beta _ { \imath } ^ { 2 } ) .
$$

However, $f _ { z } ( x _ { \imath } ) - f _ { z } ( 0 ) = \mathcal { O } ( \imath h )$ ,and $\beta _ { \imath } ^ { 1 } = \mathcal { O } ( \varepsilon 2 ^ { - \imath } )$ ， $\beta _ { \imath } ^ { 2 } = \mathcal { O } ( 2 ^ { - \imath } )$ by (5.28) and $\varepsilon \leq h$ . This shows that the term (5.40) is also of size $\mathcal { O } ( h ^ { 4 } )$ ， so that (5.32) holds with $M = 2$

b) In order to estimate the remainder term,i.e., the differences $\Delta y _ { \imath } = y _ { \imath } - \widehat { y } _ { \imath }$ ， $\Delta z _ { \imath } = z _ { \imath } - \widehat { z } _ { \imath }$ we subtract (5.32) from (5.1) and eliminate $\Delta y _ { i + 1 }$ and $\Delta z _ { \imath + 1 }$ . This

gives

$$
\begin{array} { r l } & { \biggl ( \Delta y _ { i + 1 } \atop \Delta z _ { i + 1 } \biggr ) = \biggl ( \frac { \Delta y _ { i } } { \Delta z _ { i } } \biggr ) } \\ & { + \biggl ( \begin{array} { l l } { I + O ( h ) } & { \mathcal { O } ( h ) } \\ { O ( 1 ) } & { \left( \frac { \varepsilon } { h } I - g _ { z } ( 0 ) \right) ^ { - 1 } } \end{array} \biggr ) \biggl ( \begin{array} { l } { h \bigl ( f ( y _ { i } , z _ { i } ) - f ( \widehat { y } _ { i } , \widehat { z } _ { i } ) \bigr ) } \\ { g ( y _ { i } , z _ { i } ) - g ( \widehat { y } _ { i } , \widehat { z } _ { i } ) } \end{array} \biggr ) + \biggl ( \mathcal { O } ( h ^ { M + 2 } ) \biggr ) . } \end{array}
$$

Due to (5.28) and $\varepsilon \leq h$ we have

$$
\Big \| I + \Big ( \frac { \varepsilon } { h } I - g _ { z } ( 0 ) \Big ) ^ { - 1 } g _ { z } ( 0 ) \Big \| = \Big \| \Big ( I - \frac { h } { \varepsilon } g _ { z } ( 0 ) \Big ) ^ { - 1 } \Big \| \leq \frac { \varepsilon } { \varepsilon + h } \leq \frac { 1 } { 2 } .
$$

We therefore again obtain (5.20) with some $| \varrho | < 1$ ,if $H$ is sufficiently small. We then deduce the result as in the proof of Theorem 5.3. □

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/0246742a20f1c7b322a3908bbdacc4b0f10356066f183ef642ddf26ec1fd2dfc.jpg)  
Fig. 5.1. Step size/error diagram

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/bdd6da939c45401d2d7d2ca58e0054a00b6edd52591b5d3c8f166c6f1f603777.jpg)  
Fig. 5.2. $T _ { j j }$ as functions of $H / \varepsilon$

Of course,it is possible to add a third step to the above proof. However, the recursions for $\alpha _ { i } ^ { 3 } , \beta _ { i } ^ { 3 }$ are no longer as simple as in (5.33) or (5.39). Moreover, the perturbations of (5.29) and (5.30) already describe very well the situation encountered in practice. We shallillustrate this with the following numerical example (see also Hairer &Lubich 1988).

Consider van der Pol's equation (2.73) with $\varepsilon = 1 0 ^ { - 5 }$ and with initial values (2.74) on the smooth solution. We take the step number sequence (5.23) and apply Method (5.1) $n _ { j }$ times with step size $h = H / n _ { j }$ The numerical result $Y _ { j 1 } , Z _ { j 1 }$ is then extrapolated according to (IV.9.26). In Fig.5.1 we show in logarithmic scale the errors $| Z _ { \ j j } - z ( H ) |$ for $j = 1 , 2 , \dots , 6$ as functions of $H$ . We observe that whenever the error is larger than $\varepsilon ^ { 2 } = 1 0 ^ { - 1 0 }$ ， the curves appear as straight lines with slopes $2 , 2 , 3 , 4 , 5$ , and 6,respectively. If its slope is $q$ , we have $\mathrm { l o g } ( e r r o r ) \approx$ $q \log { H } + C o n s t$ ,or equivalently $e r r o r \approx C H ^ { q }$ . This corresponds (with exception of the last one) to the orders predicted by the subdiagonal entries of Table 5.4 for the case $\varepsilon = 0$

In order to understand the irregular behaviour of the curves when the error becomes smaller than $\varepsilon ^ { 2 } = 1 0 ^ { - 1 0 }$ ， we study the influence of extrapolation on the perturbation terms in (5.30). Since $b _ { 1 } ( 0 )$ contains a factor $\varepsilon$ , the dominant part of the perturbation in $Z _ { j 1 }$ is $( I - ( h / \varepsilon ) g _ { z } ( 0 ) ) ^ { - n _ { j } } h ^ { 2 } b _ { 2 } ( 0 )$ ，where $b _ { 2 } ( 0 )$ is some constant and $\begin{array} { r } { h = H / n _ { g } } \\ { . } \end{array}$ : We assume the matrix $g _ { z } ( 0 )$ to be diagonalized and put $g _ { z } ( 0 ) = - 1$ . The dominant perturbation in $Z _ { \ j 1 }$ is therefore $\varepsilon ^ { 2 } T _ { j 1 } b _ { 2 } ( 0 )$ ，where

$$
T _ { j 1 } = \Big ( \frac { H } { \varepsilon n _ { j } } \Big ) ^ { 2 } \Big ( 1 + \frac { H } { \varepsilon n _ { j } } \Big ) ^ { - n _ { j } } .
$$

Due to the linearity of extrapolation, the dominant perturbation in $Z _ { \ j }$ will be $\varepsilon ^ { 2 } T _ { j j } b _ { 2 } ( 0 )$ ，where $T _ { j \jmath }$ is obtained from (5.42) and (IV.9.26). For the step number sequence (5.23) the values of $T _ { j j }$ are plotted as functions of $H / \varepsilon$ in Fig.5.2.For large values of $H / \varepsilon$ the curves appear as horizontal lines. This is a consequence of our choice $n _ { 1 } = 2$ and of the fact that

$$
T _ { j j } = C _ { j } \cdot \Big ( \frac { H } { \varepsilon } \Big ) ^ { 2 - n _ { 1 } } + \mathcal { O } \Big ( \Big ( \frac { H } { \varepsilon } \Big ) \Big ) ^ { 1 - n _ { 1 } } \qquad \mathrm { f o r } \quad \frac { H } { \varepsilon } \to \infty ,
$$

where $C _ { 1 } = 1$ and the other $C _ { \jmath }$ are given by the recursion (5.24).

The errors of Fig. 5.1 are now seen to be a superposition of the errors, predicted from the case $\varepsilon = 0$ (Theorem 5.4),and of the perturbations of Fig.5.2 scaled by a factor $\mathcal { O } ( \varepsilon ^ { 2 } )$ ·

Remark. As mentioned in Sect.VI.1, the implicit Euler discretization possesses a classical asymptotic expansion for differential-algebraic problems (1.6) of index 1 (case $\varepsilon = 0$ ). However, for singular perturbation problems,perturbations of the same type as in (5.29) and (5.3O) are present. The only difference is that all $b _ { i } ( 0 )$ contain a factor $\varepsilon$ for the implicit Euler method. For details and numerical experiments we refer to Hairer & Lubich (1988). A related analysis for a slightly different class of singular perturbation problems is presented in Auzinger, Frank & Macsek (1990).

# Dense Output

Extrapolation methods typically take very large (basic） step sizes during integra-tion. This makes it important that the method possess a continuous numerical solution. The first attempt to get a dense output for extrapolation methods is due to Lindberg (1972). His approach, however, imposes severe restrictions on the step number sequence. We present here the dense output of Hairer & Ostermann (1990), which exists for any step number sequence.

The main idea (due to Ch.Lubich) is the following: when computing the $j$ - th entry of the extrapolation tableau, we consider not only $Y _ { j 1 } = y _ { n _ { j } }$ ， but also compute the difference $( y _ { n _ { j } } - y _ { n _ { j } - 1 } ) / h _ { j }$ . Since these expressions possess an $h$ - expansion, their extrapolation gives an accurate approximation to $y ^ { \prime } ( x _ { 0 } + H )$ . By considering higher differences,we get also approximations to higher derivatives of $y ( x )$ at $x _ { 0 } + H$ . They are then used for Hermite interpolation. The reason for computing the derivatives only at the right end of the basic interval, is the presence of perturbation terms as described in Theorems 5.3 and 5.6. These perturbations are large at the beginning (near the initial value),but decrease exponentially for increasing $i$ . For the same reason, one must not use differences of a too high an order. We thus choose an integer $\lambda$ (usually O or 1) and avoid the values $y _ { 0 } , \ldots , y _ { n _ { 1 } + \lambda - 2 }$ for the computation of the finite differences. We remark that a similar idea was used by Deuflhard & Nowak (1987) to construct consistent initial values for differentialalgebraic problems.

An algorithmic description of the dense output for the linearly implicit Euler method is as follows (we suppose that the value $Y _ { \kappa \kappa }$ has been accepted as a numerical approximation to $y ( x _ { 0 } + H ) )$ .

Step $I$ For each $j \in \{ 1 , \ldots , \kappa \}$ we compute

$$
r _ { \jmath } ^ { ( k ) } = \frac { \nabla ^ { k } y _ { n _ { j } } ^ { ( \jmath ) } } { h _ { \jmath } ^ { k } } \qquad \mathrm { f o r } \quad k = 1 , \dots , j - \lambda .
$$

Here $y _ { \imath } ^ { ( { \jmath } ) }$ isthe approximation of $y ( x _ { i } )$ , Obaineding theuationf $Y _ { j 1 }$ and $\nabla y _ { \imath } = y _ { \imath } - y _ { \imath - 1 }$ is the backward difference operator.

Step 2. We exrapoate $r _ { \jmath } ^ { ( k ) }$ ， $\left( \kappa - k - \lambda \right)$ tiesis s t mation $\gamma ^ { ( k ) }$ t0 $y ^ { ( k ) } ( x _ { 0 } + H )$

Step 3. We define the polynomial $P ( \theta )$ of degree $\kappa$ by

$$
\begin{array} { l l } { { P ( 0 ) = y _ { 0 } , } } & { { P ( 1 ) = Y _ { \kappa \kappa } } } \\ { { P ^ { ( k ) } ( 1 ) = H ^ { k } r ^ { ( k ) } \quad } } & { { \mathrm { f o r } k = 1 , \ldots , \kappa - 1 . } } \end{array}
$$

The following theorem shows to which order these polynomials approximate the exact solution.

Theorem 5.7 (Hairer & Ostermann 1990). Consider a nonstiff differential equation and let $\lambda \in \{ 0 , 1 \}$ . Then, the error of the interpolation polynomial $P ( \theta )$ satisfies

$$
P ( \theta ) - y ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) \qquad f o r \quad H \to 0 .
$$

Proof. Since $P ( \theta )$ is a polynomial of degree $\kappa$ , the error due to interpolation is of size ${ \mathcal { O } } ( H ^ { \kappa + 1 } )$ . We know that $Y _ { \kappa \kappa } - y ( x _ { 0 } + H ) = \mathcal { O } ( H ^ { \kappa + 1 } )$ . Therefore it suffices to prove that

$$
r ^ { ( k ) } = y ^ { ( k ) } ( x _ { 0 } + H ) + \mathcal { O } ( H ^ { \kappa - k - \lambda + 1 } ) \qquad \mathrm { ~ f o r ~ } \quad k = 1 , \dots , \kappa - 1 .
$$

Due to the asymptotic expansion of the global error $y _ { \imath } - y ( x _ { \imath } )$ , the approximations $r _ { j } ^ { ( k ) }$ also have an expansion of the form

$$
r _ { j } ^ { ( k ) } = y ^ { ( k ) } ( x _ { 0 } + H ) + h _ { j } a _ { 1 } ^ { ( k ) } + h _ { j } ^ { 2 } a _ { 2 } ^ { ( k ) } + \dots .
$$

The statement (5.45) now follows from the fact that each extrapolation eliminates one power of $h$ in (5.46). □

It is now natural to investigate the error of the dense output $P ( \theta )$ also for stiff differential equations, such as singular perturbation problems. We shall treat here the limit case $\varepsilon = 0$ which is easier to analyse and, nevertheless, gives much insight into the structure of the error for very stiff problems.

For the differential-algebraic system (1.6) one defines the dense output in ex-actly the same way as for ordinary differential equations. As the system (1.6) is partitioned into $y -$ and $z$ -components, it is convenient to denote the corresponding interpolation polynomials by $P ( \theta )$ and $Q ( \theta )$ , respectively.

Theorem 5.8 (Hairer & Ostermann 1990). Let $y ( x ) , z ( x )$ be the solution of (1.6). Suppose that the step number sequence satisfies $n _ { 1 } + \lambda \ge 2$ with $\lambda \in \{ 0 , 1 \}$ . We then have

$$
\begin{array} { r l } & { P ( \theta ) - y ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) + \mathcal { O } ( H ^ { r + 1 } ) , } \\ & { Q ( \theta ) - z ( x _ { 0 } + \theta H ) = \mathcal { O } ( H ^ { \kappa + 1 - \lambda } ) + \mathcal { O } ( H ^ { s } ) , } \end{array}
$$

where $\mathscr { r }$ and $s$ are the $( \kappa + n _ { 1 } + \lambda - 2 , \kappa )$ -entries of Table 5.3 and Table 5.4, respectively.

Proof. We use the perturbed asymptotic error expansions of Theorem 5.3. Their smooth terms are treated exactly as in the proof of Theorem 5.7 and yield the ${ \mathcal { O } } ( H ^ { \kappa + 1 - \lambda } )$ error term in (5.47). The second error terms in (5.47) are due to $y _ { i }$ cpe $z _ { \imath }$ $i \ge n _ { \jmath } - j + \lambda$ $n _ { \jmath } - j \geq n _ { 1 } - 1$ $r _ { \jmath } ^ { ( k ) }$ $y _ { 0 } , \ldots , y _ { n _ { 1 } + \lambda - 2 }$ do not enter into the formulas for $r _ { j } ^ { ( k ) }$ ， so that the dominant perturbation comes from $y _ { n _ { 1 } + \lambda - 1 }$ (01 $z _ { n _ { 1 } + \lambda - 1 } )$ □

It is interesting to note that for $\lambda = 1$ , the second error term in (5.47) is of the same size as that in the numerical solution $Y _ { \kappa \kappa } , Z _ { \kappa \kappa }$ (see Theorem 5.4). However, one power of $H$ is lost in the first term of (5.47). On the other hand, one $H$ may be lost in the second error term,if $\lambda \approx 0$ . Both choices lead to a cheap (no additional function evaluations) and accurate dense output. Its order for $\theta \in ( 0 , 1 )$ is at most one lower than the order obtained for $\theta \simeq 1$ .

# Exercises

1. The linearly implicit mid-point rule, applied to the differential-algebraic system (1.6),reads

$$
\begin{array} { r l r } {  { ( \begin{array} { c c } { I - h f _ { y } ( 0 ) } & { - h f _ { z } ( 0 ) } \\ { - h g _ { y } ( 0 ) } & { - h g _ { z } ( 0 ) } \end{array} ) ( \begin{array} { c } { y _ { { z + 1 } } - y _ { i } } \\ { z _ { i + 1 } - z _ { i } } \end{array} ) } } \\ & { } & { = - ( \begin{array} { c c } { I + h f _ { y } ( 0 ) } & { h f _ { z } ( 0 ) } \\ { h g _ { z } ( 0 ) } & { h g _ { z } ( 0 ) } \end{array} ) ( \begin{array} { c } { y _ { { z } } - y _ { { z - 1 } } } \\ { z _ { i } - z _ { i - 1 } } \end{array} ) + 2 h ( \begin{array} { c } { f ( y _ { { z } } , z _ { i } ) } \\ { g ( y _ { { z } } , z _ { i } ) } \end{array} ) . } \end{array}
$$

If we compute $y _ { 1 } , z _ { 1 }$ from (5.2),and if we define the numerical solution at $x _ { 0 } + H \enspace ( H = 2 m h )$ by

$$
\begin{array} { r l r } { y _ { h } ( x _ { 0 } + H ) = \frac { 1 } { 2 } ( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) , } & { { } } & { z _ { h } ( x _ { 0 } + H ) = \frac { 1 } { 2 } ( z _ { 2 m + 1 } + z _ { 2 m - 1 } ) , } \end{array}
$$

this algorithm constitutes an extension of (IV.9.16) to differential-algebraic problems.

a) Show that this method integrates the problem (5.8) exactly.

b) Apply the algorithm to

$$
y ^ { \prime } = 1 , \quad 0 = u - y ^ { 2 } , \quad 0 = v - y u , \quad 0 = w - y v , \quad 0 = z - y w
$$

with zero initial values and verify the formula

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \left( z _ { 2 m + 1 } + z _ { 2 m - 1 } \right) - z ( x _ { 2 m } ) = - 1 0 x _ { 2 m } ^ { 3 } h ^ { 2 } + 9 x _ { 2 m } h ^ { 4 } } \\ & { \phantom { \frac { 1 } { 2 } } - ( - 1 ) ^ { m } \bigl ( \frac { 1 } { 8 } x _ { 2 m } ^ { 5 } + x _ { 2 m } ^ { 3 } h ^ { 2 } + 9 x _ { 2 m } h ^ { 4 } \bigr ) . } \end{array}
$$

Remark. The error of the $z$ -component thus contains an $h$ -independent term of size $\mathcal { O } ( H ^ { 5 } )$ , which is not affected by extrapolation.

2. Consider the method of Exercise 1 as the basis of an $h ^ { 2 }$ -extrapolation me-thod. Prove that for the step number sequence (IV.9.22) the extrapolated values satisfy

$$
Y _ { j k } - y ( x _ { 0 } + H ) = { \mathcal { O } } ( H ^ { r _ { j k } + 1 } ) , \qquad Z _ { \ j k } - z ( x _ { 0 } + H ) = { \mathcal { O } } ( H ^ { s _ { \ j k } } )
$$

with $\boldsymbol { r } _ { j k } , \boldsymbol { s } _ { j k }$ given in Tables 5.5 and 5.6.

Hint. Interpret $Y _ { \ j 1 } , Z _ { \ j 1 }$ as numerical solution of a Rosenbrock method (Exercise 3 of Sect.IV.9) and verify the order condition derived in Sect. VI.3 (see also Hairer & Lubich (1988b) and C. Schneider (1993)).

Table 5.5. orders rjk ·

Table 5.6. orders S jk ·

$\begin{array} { l } { { 1 } } \\ { { 1 \quad 3 } } \\ { { 1 \quad 3 \quad 5 } } \\ { { 1 \quad 3 \quad 5 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 \quad 7 } } \\ { { 1 \quad 3 \quad 5 \quad 7 \quad 7 \quad 7 \quad 7 } } \end{array}$

5 5 5

Quasilinear differential equations are usually understood to be equations in which the highest derivative appears linearly. In the case of first order ODE systems, they are of the form

$$
C ( y ) \cdot y ^ { \prime } = f ( y ) ,
$$

where $C ( y )$ is a $n \times n$ -matrix. In the regions where $C ( y )$ is invertible,Eq. (6.1) can be written as

$$
y ^ { \prime } = C ( y ) ^ { - 1 } \cdot f ( y )
$$

and every ODE-code can be applied by solving at every function call a linear system. But this would destroy, for example, a banded structure of the Jacobian and it is therefore often preferable to treat Eq.(6.1) directly. If the matrix $C$ is everywhere of rank m $( m < n )$ ,Eq. (6.1) represents a quasilinear differential-algebraic system.

# Example: Moving Finite Elements

As an example, we present the classical idea of "moving finite elements", described in K. Miller & R.N. Miller (1981): the solution $u ( x , t )$ of a nonlinear partial differential equation

$$
\frac { \partial u } { \partial t } = L \big ( u ( x , t ) \big ) , \quad u ( 0 , t ) = u ( 1 , t ) = 0 ,
$$

where $L ( u )$ is an unbounded nonlinear differential operator, is approximated by finite element polygons $v ( x , a _ { 1 } , s _ { 1 } , \ldots , a _ { n } , s _ { n } )$ which satisfy $v ( s _ { j } , \ldots ) = a _ { j }$ (see Fig. 6.1). These polygons form a $2 n$ -dimensional manifold in the Hilbert space $L ^ { 2 } ( 0 , 1 )$ parametrized by $a _ { 1 } , s _ { 1 } , \ldots , a _ { n } , s _ { n }$ . The idea is now to move simultaneously $a ( t )$ and $s ( t )$ in oder to adapt at any time the finite element solution as best as possible to Eq.(6.2).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/9d533172dfb7c7e8f72c7345eedb907d7dff46ce744b32570798b1234156f4e2.jpg)  
Fig. 6.1. Moving finite elements

We thus require that the defect $\dot { v } - L ( v )$ remains always orthogonal to the tangent space. The conditions

$$
\int _ { 0 } ^ { 1 } { \bigl ( } { \dot { v } } - L ( v ) { \bigr ) } \cdot { \frac { \partial v } { \partial a _ { j } } } d x = 0 \qquad \int _ { 0 } ^ { 1 } { \bigl ( } { \dot { v } } - L ( v ) { \bigr ) } \cdot { \frac { \partial v } { \partial s _ { j } } } d x = 0
$$

lead to a system of type (6.1) with

$$
\begin{array} { r l r l } & { c _ { 2 j - 1 , 2 k - 1 } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial a _ { j } } \cdot \frac { \partial v } { \partial a _ { k } } d x , } & & { c _ { 2 j - 1 , 2 k } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial a _ { j } } \cdot \frac { \partial v } { \partial s _ { k } } d x , } \\ & { c _ { 2 j , 2 k - 1 } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial s _ { j } } \cdot \frac { \partial v } { \partial a _ { k } } d x , } & & { c _ { 2 j , 2 k } = \int _ { 0 } ^ { 1 } \frac { \partial v } { \partial s _ { j } } \cdot \frac { \partial v } { \partial s _ { k } } d x , } \\ & { f _ { 2 j - 1 } = \int _ { 0 } ^ { 1 } L ( v ) \cdot \frac { \partial v } { \partial a _ { j } } d x , } & & { f _ { 2 j } = \int _ { 0 } ^ { 1 } L ( v ) \cdot \frac { \partial v } { \partial s _ { j } } d x . } \end{array}
$$

For the partial derivatives of $v$ , sketched in Fig.6.1, the non-zero of these scalar products become

$$
\begin{array} { l l } { { c _ { 2 j - 1 , 2 j - 1 } = \frac { 1 } { 3 } ( \triangle _ { j } + \triangle _ { j + 1 } ) } } & { { c _ { 2 j - 1 , 2 j } = - \frac { 1 } { 3 } ( m _ { j } \triangle _ { j } + m _ { j + 1 } \triangle _ { j + 1 } ) } } \\ { { c _ { 2 j , 2 j - 1 } = - \frac { 1 } { 3 } ( m _ { j } \triangle _ { j } + m _ { j + 1 } \triangle _ { j + 1 } ) } } & { { c _ { 2 j , 2 j } = \frac { 1 } { 3 } ( m _ { j } ^ { 2 } \triangle _ { j } + m _ { j + 1 } ^ { 2 } \triangle _ { j + 1 } ) + \displaystyle \frac { 2 \varepsilon ^ { 2 } } { \angle \varepsilon } . } } \end{array}
$$

$$
\begin{array} { r l } { c _ { 2 j - 1 , 2 j + 1 } = c _ { 2 j + 1 , 2 j - 1 } = \frac { 1 } { 6 } \Delta _ { j + 1 } } & { { } c _ { 2 j - 1 , 2 j + 2 } = c _ { 2 j + 2 , 2 j - 1 } = - \frac { 1 } { 6 } m _ { j + 1 } \Delta _ { j + 1 } } \\ { c _ { 2 j , 2 j + 1 } = c _ { 2 j + 1 , 2 j } = - \frac { 1 } { 6 } m _ { j + 1 } \Delta _ { j + 1 } } & { { } c _ { 2 j , 2 j + 2 } = c _ { 2 j + 2 , 2 j } = \frac { 1 } { 6 } m _ { j + 1 } ^ { 2 } \Delta _ { j + 1 } - \varepsilon ^ { 2 } } \end{array}
$$

where

$$
\Delta _ { \ j } = s _ { j } - s _ { j - 1 } , \quad m _ { j } = ( a _ { j } - a _ { j - 1 } ) / \Delta _ { \ j } , \qquad j = 1 , \ldots , n + 1 .
$$

The matrix $C ( y )$ is banded with bandwidth $3 + 1 + 3$ . The $\varepsilon ^ { 2 }$ -terms in (6.5) come from an “internodal viscosity” penalty term, explained in Miller & Miller (1981), which aims to regularize the relative movement of the nodes $s _ { j }$ whenever their position is ill-conditioned,which happens to appear in the vicinity of inflection points (see Fig.6.2).

It is then hoped that the nodes move automatically into the critical regions of the solutions, move with shocks which may appear, and that $a ( t )$ and $s ( t )$ become smooth functions.

Application to Burgers’Equation. Burgers’Equation is given by

$$
u _ { t } = - u u _ { x } + \mu u _ { x x } \qquad \mathrm { o r } \qquad u _ { t } = - \Big ( \frac { u ^ { 2 } } { 2 } \Big ) _ { x } + \mu u _ { x x }
$$

where $\mu = 1 / R$ and $R$ is called te Reynolds number. This is one of the equations originally designed by Burgers (1948） as $^ { 6 6 } \mathbf { 2 }$ mathematical model illustrating the theory of turbulence". However, soon afterwards,E. Hopf (195O) presented an analytical solution (see Exercise 1 below) and concluded that “we doubt that Burgers’equation fully illustrates the statistics of free turbulence.(...） Equation (1） is too simple a model to display chance fluctuations ...". Nowadays it remains interesting as a nonlinear equation resembling the Navier-Stokes' equations in fluid dynamics which possesses, for $R$ large,shock waves and, for $R \to \infty$ ， discontinuous solutions. Here,the integrals in (6.4) become

$$
f _ { 2 j - 1 } = A _ { j } + \mu B _ { j } , \quad f _ { 2 j } = C _ { j } + \mu D _ { \jmath } , \qquad j = 1 , \ldots n .
$$

where

$$
\begin{array} { r l } & { A _ { j } = \big ( a _ { j - 1 } - a _ { j } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j - 1 } \big ) + \big ( a _ { j } - a _ { j + 1 } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j + 1 } \big ) , } \\ & { B _ { j } = \big ( m _ { j + 1 } - m _ { j } \big ) , } \\ & { C _ { j } = - m _ { j } \big ( a _ { j - 1 } - a _ { j } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j - 1 } \big ) - m _ { j + 1 } \big ( a _ { j } - a _ { j + 1 } \big ) \big ( \frac { 1 } { 3 } a _ { j } + \frac { 1 } { 6 } a _ { j + 1 } \big ) , } \\ & { D _ { j } = \big ( m _ { j + 1 } - m _ { j } \big ) \big ( \frac { 1 } { 2 } m _ { j + 1 } + \frac { 1 } { 2 } m _ { j } \big ) , } \end{array}
$$

(in the case of $D _ { \ j }$ appears the product of a Dirac $\delta$ function with a discontinuous function; these must be suitably “mollified"). We choose as initial function

$$
u ( x , 0 ) = ( \sin ( 3 \pi x ) ) ^ { 2 } \cdot ( 1 - x ) ^ { 3 / 2 } \ , \qquad \mu = 0 . 0 0 0 3
$$

and as initial positions

$$
s _ { j } = j / ( n + 1 ) , \quad a _ { j } = u ( s _ { j } , 0 ) , \qquad j = 1 , \ldots , n , \quad n = 1 0 0 ,
$$

and solve the problem with smoothing parameter $\varepsilon = 1 0 ^ { - 2 }$ for $0 \leq t \leq 1 . 9$ . Two shock waves arise which later fuse into one (see Fig. 6.2).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/f229978c2f7bfcd0247816cb24e24a34384387e1d403dc1c5072fd063046ff93.jpg)  
Fig. 6.2.Moving finite element solution of Burgers’ equation

# Problems of Index One

For invertible $C ( y )$ ，Eq.(6.1） is an ordinary differential equation and standard theory (for existence and uniqueness results) can be applied. If the matrix is illconditioned or even singular, new investigations are necessary. In order to exclude equations with singularities, such as $x y ^ { \prime } = ( q + b x ) y$ (see Sect.I.5), we assume that

$$
C ( y ) { \mathrm { ~ h a s ~ c o n s t a n t ~ r a n k ~ } } m ( m < n )
$$

in a neighbourhood of the solution. Then the columns of $C ( y )$ span an $m$ -dimensional subspace $\mathcal { I } m \ : C ( y )$ which moves with $y$ . Clearly, in order that (6.1） can make sense, we need consistent initial values,i.e., we need

$$
f ( y _ { 0 } ) \in { \underline { { \tau } } } m C ( y _ { 0 } ) .
$$

We shall now show, how, under a certain condition, this property can be satisfied for all $_ x$ and determines uniquely the solution: choose a nonsingular matrix

$$
T ( y ) = { \binom { T _ { 1 } ( y ) } { T _ { 2 } ( y ) } } \qquad { \mathrm { s u c h ~ t h a t } } \qquad T ( y ) C ( y ) = { \binom { B _ { 1 } ( y ) } { 0 } } ;
$$

this means that the rows of $T _ { 2 } ( y )$ must span the $( n - m )$ -dimensional orthogonal complement of $\mathcal { T } m C ( y )$ . Then we multiply Eq. (6.1) by $T ( y )$ and obtain

$$
\left( { \begin{array} { c } { B _ { 1 } ( y ) } \\ { 0 } \end{array} } \right) y ^ { \prime } = \left( { \begin{array} { c } { T _ { 1 } ( y ) f ( y ) } \\ { T _ { 2 } ( y ) f ( y ) } \end{array} } \right) ,
$$

so that the condition corresponding to (6.9) becomes visible in the form $\begin{array} { r } { T _ { 2 } ( y ) f ( y ) = } \end{array}$ O. Differentiating this relation and inserting the derivative into the second part of (6.11), we obtain

$$
\left( { \cal B } _ { 1 } ( y ) \atop ( T _ { 2 } f ) ^ { \prime } ( y ) \right) y ^ { \prime } = \left( { \displaystyle ( T _ { 1 } f ) ( y ) \atop 0 } \right) ,
$$

which is a regular quasilinear equation if the matrix

$$
\begin{array} { r } { \left( \begin{array} { c } { B _ { 1 } ( y ) } \\ { ( T _ { 2 } f ) ^ { \prime } ( y ) } \end{array} \right) \qquad \mathrm { i s ~ i n v e r t i b l e . } } \end{array}
$$

Lemma 6.1. Let the matrix $C ( y )$ satisfy (6.8) and (6.13),and let the initial values $y _ { 0 }$ fulfill (6.9). Then, the quasilinear problem $C ( y ) y ^ { \prime } = f ( y )$ $y ( x _ { 0 } ) = y _ { 0 }$ possesses a locally unique solution.

Proof. Condition (6.9) means that $T _ { 2 } ( y _ { 0 } ) f ( y _ { 0 } ) = 0$ and the second part of (6.12) assures that $( T _ { 2 } ( y ( x ) ) f ( y ( x ) ) ) ^ { \prime } = 0$ . Therefore we have $( T _ { 2 } f ) ( y ( x ) ) = 0$ for all $_ x$ , and the solution of (6.12) solves also (6.11) and (6.1). □

The following result gives a consequence of condition (6.13) which shall be essential in the later discussions of feasibility of numerical procedures.

Lemma 6.2. Assume that $C ( y )$ satisfies (6.8) and (6.13). If $f ( y _ { 0 } ) = C ( y _ { 0 } ) y _ { 0 } ^ { \prime }$ ， then the matrix

$$
C ( y ) + \lambda \bigl ( f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) \bigr )
$$

is invertible for sufficiently small $\lambda \neq 0$ and for $y$ sufficiently close to $y _ { 0 }$ .Here,

$$
\Gamma ( y , y ^ { \prime } ) = { \frac { \partial } { \partial y } } { \big ( } C ( y ) y ^ { \prime } { \big ) } .
$$

Proof. Condition (6.13) implies that

$$
T ( y ) C ( y ) + \lambda ( T f ) ^ { \prime } ( y _ { 0 } ) \qquad \mathrm { i s ~ i n v e r t i b l e }
$$

for small $\lambda \neq 0$ and $y$ close to $y _ { 0 }$ . Using $T ^ { \prime } C + T C ^ { \prime } = B ^ { \prime }$ we have

$$
( T ^ { \prime } f ) ( y _ { 0 } ) = T ^ { \prime } ( y _ { 0 } ) C ( y _ { 0 } ) y _ { 0 } ^ { \prime } = - T ( y _ { 0 } ) \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) + B ^ { \prime } ( y _ { 0 } ) y _ { 0 } ^ { \prime } .
$$

Since $B ^ { \prime } ( y _ { 0 } ) y _ { 0 } ^ { \prime }$ does not contribute to the lower block of the matrix (6.14), it can be neglected after insertion of $( T f ) ^ { \prime } = T f ^ { \prime } + T ^ { \prime } f$ and (6.15) into (6.14). This implies that

$$
T ( y ) C ( y ) + \lambda T ( y _ { 0 } ) { \big ( } f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) { \big ) } \qquad { \mathrm { i s ~ i n v e r t i b l e . } }
$$

The statement of the Lemma now follows from a continuity argument.

# Numerical Treatment of $C ( \boldsymbol { y } ) \boldsymbol { y } ^ { \prime } = f ( \boldsymbol { y } )$

As has been said above, in the case of invertible matrices $C ( y )$ , one can eventually apply an explicit numerical method to (6.1').However,if Eq.(6.1') is stiff,implicit methods have to be applied. In this case it may be advantageous to have methods that avoid the computation of the Jacobian of $C ( y ) ^ { - 1 } f ( y )$

Transformation to Semi-Explicit Form. In the case where (6.1') is stiff or where $C ( y )$ is singular and satisfies (6.8) and (6.13) we introduce $z = y ^ { \prime }$ as new variable, such that system (6.1) becomes of the semi-explicit form

$$
\begin{array} { c } { { y ^ { \prime } = z } } \\ { { 0 = C ( y ) z - f ( y ) } } \end{array}
$$

Here,all methods of the preceding sections can be applied (at least formally). The study of convergence, however, needs further investigation, because Condition (1.7) is no longer satisfied here.

Implicit Runge-Kutta and Multistep Methods. With the $\varepsilon$ -embedding approach (see (1.11) for Runge-Kutta methods and (2.2) for multistep methods) we are led to

nonlinear equations, which, when solved by Newton iterations, require the solution of linear systems of the form

$$
\left( \begin{array} { c c } { - \alpha I } & { I } \\ { \Gamma ( y _ { 0 } , z _ { 0 } ) - f ^ { \prime } ( y _ { 0 } ) } & { C ( y _ { 0 } ) } \end{array} \right) .
$$

Here $\alpha = ( \gamma h ) ^ { - 1 }$ ，and $\gamma$ is an eigenvalue of the Runge-Kutta matrix. By Lemma 6.2 this matrix is invertible for small enough $h > 0$ . Convergence follows from the results of Sections VI.3 and VII.4 (see Exercise 2).

Rosenbrock Methods. Method (4.3) applied to system (6.16) leads to

$$
\left( { v _ { \mathfrak { r } } } _ { \mathfrak { a } } \right) = \left( { y _ { 0 } } \atop { z _ { 0 } } \right) + \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } \left( { k _ { \jmath } } \atop { \ell _ { \jmath } } \right) , \qquad \left( { y _ { 1 } } \atop { z _ { 1 } } \right) = \left( { y _ { 0 } } \atop { z _ { 0 } } \right) + \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } \left( { k _ { \imath } } \atop { \ell _ { i } } \right) .
$$

$$
\binom { k _ { i } } { 0 } = h \left( { C ( v _ { i } ) w _ { i } } + h \left( { \begin{array} { c c } { 0 } & { I } \\ { \Gamma _ { 0 } - f _ { 0 } ^ { \prime } } & { C ( y _ { 0 } ) } \end{array} } \right) \sum _ { j = 1 } ^ { i } \gamma _ { \upsilon _ { j } } \binom { k _ { j } } { \ell _ { j } } . \right)
$$

Again, it can be seen that (6.18b) represents a linear system whose regularity is assured by Lemma 6.2. However, since Condition (1.7) is not satisfied, a new theory for the order conditions of the local error as well as for convergence of the global error is necessary. This theory reveals, for example, that new order conditions for the coefficients are necessary and explains why, say, the code RODAS, directly applied to (6.16), does not give precise results. For full details we refer the reader to the original publication Lubich & Roche (1990).

# Extrapolation Methods

The first problem is to find suitable linearly implicit Euler discretizations for (6.1), to serve as basic method for the extrapolation algorithm (see Sect.IV.9).

Method of Deuflhard & Nowak. Applying the linearly implicit Euler method (IV.9.15) to the differential equation (6.1') we obtain

$$
( I - h A ) ( y _ { i + 1 } - y _ { \imath } ) = h C ( y _ { i } ) ^ { - 1 } f ( y _ { \imath } )
$$

where

$$
A \approx ( C ^ { - 1 } f ) ^ { \prime } ( y _ { 0 } ) = C ( y _ { 0 } ) ^ { - 1 } \left( f ^ { \prime } ( y _ { 0 } ) - \Gamma ( y _ { 0 } , y _ { 0 } ^ { \prime } ) \right)
$$

with $\Gamma ( y , y ^ { \prime } )$ as in Lemma 6.2. Multiplication of (6.19) with $C ( y _ { \imath } )$ yield:

$$
\left( C ( y _ { \iota } ) - h C ( y _ { \iota } ) C ( y _ { 0 } ) ^ { - 1 } J \right) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( y _ { \iota } )
$$

with $J = f \prime ( y _ { 0 } ) - \Gamma \big ( y _ { 0 } , y _ { 0 } ^ { \prime } \big )$ ．Deuflhard & Nowak（1987） suggest to replace $C ( y _ { \imath } ) C ( y _ { 0 } ) ^ { - 1 }$ by the identity matrix,which “may be interpreted as just introduc-ing an approximation error into the Jacobian matrix". This leads to the discretization

$$
\left( C ( y _ { \imath } ) - h J \right) ( y _ { \imath + 1 } - y _ { \imath } ) = h f ( y _ { \imath } )
$$

which represents the basic step for the code LIMEX described in Deuflhard & Nowak (1987). The regularity of the matrix of this linear system is again assured by Lemma 6.2.

The computation of $J$ requires an approximation to $z _ { 0 } = y _ { 0 } ^ { \prime }$ . Such consistent initial values must be computed explicitely for the first basic steps,and are obtained by extrapolation of

$$
z _ { n } = ( y _ { n } - y _ { n - 1 } ) / h
$$

in the subsequent steps.

Linearly-Implicit Euler to Semi-Explicit Model. Another possibility is to apply the linearly-implicit Euler discretization (5.2) to the differential-algebraic system (6.16). This gives

$$
\left( \begin{array} { c c } { I } & { - h I } \\ { - h J } & { h C ( y _ { 0 } ) } \end{array} \right) \left( \begin{array} { c } { y _ { \iota + 1 } - y _ { \iota } } \\ { z _ { \iota + 1 } - z _ { \iota } } \end{array} \right) = h \left( \begin{array} { c } { z _ { \iota } } \\ { f ( y _ { \iota } ) - C ( y _ { \iota } ) z _ { \iota } } \end{array} \right)
$$

with $z _ { 0 } = y _ { 0 } ^ { \prime } = y ^ { \prime } ( x _ { 0 } )$ . The first line yields $z _ { \imath + 1 } = ( y _ { \imath + 1 } - y _ { \imath } ) / h$ and the second line becomes

$$
\left( C ( y _ { 0 } ) - h J \right) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( y _ { \iota } ) - \left( C ( y _ { \iota } ) - C ( y _ { 0 } ) \right) ( y _ { \iota } - y _ { \iota - 1 } ) .
$$

The right-most term vanishes for $i = 0$ ,so that $y _ { - 1 }$ does not enter the algorithm.

Asymptotic Expansions. The theoretical justification of the use of either (6.20) or (6.23)as basic step for an extrapolation process requires the investigation of the asymptotic expansion of their global errors.

In the situation where $C ( y )$ is invertible, the discretization (6.2O) is a consistent one-step discretization of (6.1'） and possesses therefore,by standard theory (Theorem II.8.1),an asymptotic expansion, the terms of which, however, depend on the stiffness. Since the system (6.16) is of the form (1.6) with assumption (1.7) satisfied, we can conclude from Theorem 5.3 the existence of a perturbed asymptotic expansion for the second discretization (6.23).

In the situation where $C ( y )$ is singular,Lubich (1989) reveiled the existence of a perturbed asymptotic expansion for both discretizations (6.20) and (6.23). We refer to this original publication for further details, in particular to the study of the influence of these perturbations to the extrapolated numerical approximation.

# Exercises

1. Reconstruct E. Hopf's analytic solution of Burgers' equation (6.6). Hint. Introduce the new dependent variable

$$
\varphi ( x , t ) = \exp \left\{ - \frac { 1 } { 2 \mu } \int _ { 0 } ^ { x } u ( \xi , t ) d \xi - \int _ { 0 } ^ { t } c ( \tau ) d \tau \right\} .
$$

Show that for a suitably chosen $c ( t )$ the function $\varphi ( x , t )$ satisfies the one dimensional heat equation. The solution $u ( x , t )$ of (6.6) can then be recovered from $\varphi ( x , t )$ by

$$
u = - 2 \mu ( \log \varphi ) _ { x } = - 2 \mu ( \varphi _ { x } / \varphi ) .
$$

2.Assume that (6.8) and (6.13) hold. By eliminating from $0 = C ( y ) z - f ( y )$ as many components of $z$ as possible, transform the system (6.16) into an equivalent one of the form

$$
y ^ { \prime } = F ( y , u ) , \qquad 0 = G ( y ) ,
$$

where $u$ collects the remaining components of $z$ ·

a) Prove that Runge-Kutta methods and multistep methods are invariant with respect to this transformation.

b) Show that $G _ { y } ( y ) F _ { u } ( y , u )$ is invertible, so that the convergence results of Sections VII.3 and VII.4 can be applied.

3. (Quasilinear problems with gradient-type mass-matrix, see HLR89, page 111). Consider the electrical circuit (1.14), but suppose this time that the capacities depend on the voltages, e.g. as

$$
C _ { k } = { C _ { k 0 } } / { \left( 1 - ( U _ { i } - U _ { j } ) / U _ { b } \right) ^ { 1 / 2 } }
$$

so that the expressions $C _ { k } ( U _ { i } ^ { \prime } - U _ { j } ^ { \prime } )$ in (1.14) must be replaced by $( C _ { k } ( U _ { \imath } -$ $U _ { \jmath } ) /$ . Show that then the corresponding equations are of the form (6.1) with

$$
C ( y ) = A q ^ { \prime } ( y )
$$

where $A$ is a constant matrix and $q ( y )$ a known function of $y$ . Show that such problems can be efficiently solved by introducing $q ( y ) = z$ as a new variable such that the problem becomes semi-explicit as

$$
A z ^ { \prime } = f ( y ) , \qquad 0 = z - q ( y ) .
$$
