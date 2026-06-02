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


<!-- chunk 0008: pages 491-560 -->
for sufficiently small $\tau$ and

$$
f _ { 1 } ( w , \tau ) = f _ { 1 } ( w _ { 1 , 0 } , w _ { 2 } , \cdot \cdot \cdot , w _ { n } , \tau ) + \int _ { w _ { 1 , 0 } } ^ { w _ { 1 } } \left| \frac { \partial \left( f _ { 2 } , \cdot \cdot \cdot , f _ { n } \right) } { \partial \left( w _ { 2 } , \cdot \cdot \cdot , w _ { n } \right) } \right| ( \xi , w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) \mathrm { d } \xi ,
$$

we have from (8.31)

$$
\phi _ { 1 } ^ { ( m ) } ( w , \tau ) = f _ { 1 } ( w , \tau ) + { \cal O } ( \tau ^ { m + 1 } ) .
$$

So, $\phi ^ { ( m ) } ( w , \tau ) ~ = ~ ( \phi _ { 1 } ^ { ( m ) } ( w , \tau ) , \cdot \cdot \cdot , \phi _ { n } ^ { ( m ) } ( w , \tau ) )$ is an $m$ -th order approximant to $f ( w , \tau ) = ( f _ { 1 } ( w , \tau ) , \cdot \cdot \cdot , f _ { n } ( w , \tau ) )$ , the generating function of the type $\alpha _ { 1 , 1 }$ of $g _ { \alpha } ^ { t }$ and hence the volume-preserving scheme (8.33) is of $m$ -th order of accuracy. The proof is completed.

Remark 8.10. We note that the volume-preserving scheme $z = z ^ { k } \to z ^ { k + 1 }$ given by (8.33) is implicit for only one new variable $z _ { 1 } ^ { k + 1 }$ and explicit for all other new variables $z _ { i } ^ { k + 1 } ( i = 2 , \cdots , n )$ in terms of the old variables $z _ { i } ^ { k } ( i = 2 , \cdots , n )$ .

Remark 8.11. We can get volume-preserving scheme similar to the above one if we consider the types $\alpha = \alpha _ { ( s , s ) }$ $2 \leq s \leq n$ ), instead of $\alpha = \alpha _ { ( 1 , 1 ) }$ .

Example 8.12. First order scheme:

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k } = \phi _ { 1 } ^ { ( 1 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \\ { z _ { i } ^ { k } = \phi _ { i } ^ { ( 1 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \end{array} \right. \quad i = 2 , \cdot \cdot \cdot , n ,
$$

where

$$
\begin{array} { r c l } { { \phi _ { 1 } ^ { ( 1 ) } ( w , \tau ) } } & { { = } } & { { - \tau a _ { 1 } ( 0 , w _ { 2 } , \cdots , w _ { n } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { + } } & { { \displaystyle \int _ { 0 } ^ { w _ { 1 } } \left[ \begin{array} { c c c c c } { { 1 + \tau \frac { \partial a _ { 2 } } { \partial w _ { 2 } } } } & { { \tau \frac { \partial a _ { 2 } } { \partial w _ { 3 } } } } & { { \cdots } } & { { \tau \frac { \partial a _ { 3 } } { \partial w _ { n } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \tau \frac { \partial a _ { 3 } } { \partial w _ { 2 } } } } & { { 1 + \tau \frac { \partial a _ { 3 } } { \partial w _ { 3 } } } } & { { \cdots } } & { { \tau \frac { \partial a _ { 3 } } { \partial w _ { n } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { } } & { { \vdots } } \\ { { \tau \frac { \partial a _ { n } } { \partial w _ { 2 } } } } & { { \tau \frac { \partial a _ { n } } { \partial w _ { 3 } } } } & { { \cdots } } & { { 1 + \tau \frac { \partial a _ { n } } { \partial w _ { n } } } } \end{array} \right] ( \xi , w _ { 2 } , \cdots , w _ { n } ) \mathrm { d } \xi } } \\ { { } } & { { } } & { { } } \\ { { \phi _ { i } ^ { ( 1 ) } ( w , \tau ) } } & { { = } } & { { w _ { i } + \tau a _ { i } ( w ) . } } \end{array}
$$

Second order scheme:

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k } = \phi _ { 1 } ^ { ( 2 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdots , z _ { n } ^ { k } , \tau ) , } \\ { z _ { i } ^ { k + 1 } = \phi _ { i } ^ { ( 2 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdots , z _ { n } ^ { k } , \tau ) , } & { i = 2 , \cdots , n , } \end{array} \right.
$$

where

$$
\begin{array} { l } { { \phi _ { 1 } ^ { ( 2 ) } ( w , \tau ) = \psi _ { 1 } ^ { ( 2 ) } ( 0 , w _ { 2 } , \cdot \cdot \cdot , w _ { n } , \tau ) + \displaystyle \int _ { 0 } ^ { w _ { 1 } } \left| \frac { \partial ( \psi _ { 2 } ^ { ( 2 ) } , \cdot \cdot \cdot , \psi _ { n } ^ { ( 2 ) } ) } { \partial ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) } \right| ( \xi , w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) \mathrm { d } \xi . } } \\ { { \phi _ { i } ^ { ( 2 ) } ( w , \tau ) = \psi _ { i } ^ { ( 2 ) } ( w , \tau ) , \quad i = 2 , \cdot \cdot \cdot , n , } } \end{array}
$$

and

$$
\begin{array} { l } { { \psi ^ { ( 2 ) } ( w , \tau ) = \bigl ( \psi _ { 1 } ^ { ( 2 ) } ( w , \tau ) , \cdots , \psi _ { n } ^ { ( 2 ) } ( w , \tau ) \bigr ) ^ { \mathrm { T } } = w + \tau \widetilde { a } ( w ) + \frac 1 2 \tau ^ { 2 } \frac { \partial \widetilde { a } ( w ) } { \partial w _ { 1 } } \widetilde { a } ( w ) } } \\ { { \mathrm { } } } \\ { { \widetilde { a } ( w ) = \bigl ( - a _ { 1 } ( w ) , a _ { 2 } ( w ) , \cdots , a _ { n } ( w ) \bigr ) ^ { \mathrm { T } } . } } \end{array}
$$

# 10.9 Some Volume-Preserving Algorithms

In this section, we analyze and study under conditions a source-free system that has volume-preserving R–K schemes.

# 10.9.1 Volume-Preserving R–K Methods

Consider the system

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { a } ( \boldsymbol { z } ) ,
$$

where

$$
\begin{array} { r l } & { z = \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] , \quad x \in \mathbf { R } ^ { p } , \quad y \in \mathbf { R } ^ { q } , } \\ & { \quad a ( z ) = \left[ \begin{array} { l } { g ( y ) } \\ { f ( x ) } \end{array} \right] . } \end{array}
$$

Obviously, this is a source-free system. Its phase flow in $\mathbf { R } ^ { p + q }$ preserves the phase volume of $( p + q )$ form

$$
\operatorname { d } x _ { 1 } \wedge \operatorname { d } x _ { 2 } \wedge \cdots \wedge \operatorname { d } x _ { p } \wedge \operatorname { d } y _ { 1 } \wedge \operatorname { d } y _ { 2 } \wedge \cdots \wedge \operatorname { d } y _ { q } .
$$

Only R–K and P–R–K are to be discussed. We wish, some of the phase volume is preserved.

The formula of a general $m$ -th stage P–R–K method with time step $h$ applied to system (9.1) is read as

$$
\begin{array} { l } { \displaystyle \xi _ { i } = x _ { n } + h \sum _ { j = 1 } ^ { m } d _ { i j } g ( \eta _ { j } ) , \eta _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { m } c _ { i j } f ( \xi _ { j } ) , \quad 1 \le i \le m , } \\ { \displaystyle x _ { n + 1 } = x _ { n } + h \sum _ { j = 1 } ^ { m } \delta _ { j } g ( \eta _ { j } ) , } \\ { \displaystyle y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { m } \gamma _ { j } f ( \xi _ { j } ) , } \end{array}
$$

here $\xi _ { i } \in \mathbf { R } ^ { p } , \eta _ { i } \in \mathbf { R } ^ { q }$ ( $1 \leq i \leq m$ ) are auxiliary vectors used to compute updates $( x _ { n + 1 } , y _ { n + 1 } )$ .

Suppose (9.2) is irreducible, that is, if $i \neq j$ , then $\xi _ { i } \neq \xi _ { j }$ or $\eta _ { i } \neq \eta _ { j } ^ { \mathrm { [ D V 8 4 ] } }$ . We have following Lemma of Y.B. Suris[Sur96] .

Lemma 9.1. Let $\delta = [ \delta _ { 1 } , \delta _ { 2 } , \cdots , \delta _ { m } ] ^ { \mathrm { T } }$ , $D = \left( d _ { i j } \right)$ , $C = \left( c _ { i j } \right)$ , $e = [ 1 , 1 , \cdots , 1 ] ^ { \mathrm { T } }$ be a $m$ -dimensional vector $D ^ { - } = e \delta ^ { \mathrm { T } } - D$ , $C ^ { - } = e \delta ^ { \mathrm { T } } - C$ . The P–R–K method preserves phase volume for system (9.1) in arbitrary dimensions, iff

$$
\begin{array} { r l } & { d _ { k _ { 1 } l _ { 1 } } c _ { l , k _ { 2 } } \cdot \cdot \cdot d _ { k _ { r - 1 } l _ { r - 1 } } c _ { l _ { r - 1 } k _ { r } } d _ { k _ { r } l _ { r } } c _ { l _ { r } k _ { 1 } } } \\ & { = d _ { k _ { 1 } l _ { 1 } } ^ { - } c _ { l _ { 1 } k _ { 2 } } ^ { - } \cdot \cdot \cdot d _ { k _ { r - 1 } l _ { r - 1 } } ^ { - } c _ { l _ { r - 1 } k _ { r } } ^ { - } d _ { k _ { r } l _ { r } } ^ { - } c _ { l _ { r } k _ { 1 } } ^ { - } . } \end{array}
$$

For arbitrary $1 \leq r \leq m$ and two arbitrary ordered sets $\left( k _ { 1 } , \cdots , k _ { r } \right)$ and $( l _ { 1 } , \cdots , l _ { r } )$ of different natural numbers from $( 1 , m )$ , $d _ { i j }$ and $c _ { i j }$ are elements $( i , j )$ with respect to matrix $D ^ { - }$ and $C ^ { - }$ .

Next, for system (9.1), we construct some volume-preserving method by P–R–K method, using the above criteria.

First we consider volume-preserving by $\mathbf { R - K }$ method for linear system.

Linear system of ODE is read as

$$
{ \dot { y } } = M y ,
$$

where $M$ is $n \times n$ matrix with trace $M = 0$ . If $\operatorname* { d e t } M = 0$ , the system (9.3) can degrade to a lower stage, so we assume $\operatorname* { d e t } M \neq 0$ . Now, we assume that $M$ is a constant matrix. As in R–K method, $( A . b . c )$ applied to system (9.3) takes the form

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } M Y _ { j } } , } \\ { { \displaystyle y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { s } b _ { j } M Y _ { j } } , } \end{array}
$$

where $A = ( a _ { i j } ) _ { s \times s } , b = [ b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { s } ] ^ { \mathrm { T } }$ .

Here, we just talk about R–K method and according to Lemma 4.2, we cannot find a general volume-preserving $\mathbf { R - K }$ method. So, our hope is to distinguish $M$ into

different classes and find out whether there are volume-preserving R–K method in any class.

Now, we need the following notations:

$$
\begin{array} { l l } { { \overline { { { A } } } = A \otimes E _ { n } , } } & { { \overline { { { M } } } = \mathrm { d i a g } \left( M , M , \cdots , M \right) = E _ { s } \otimes M , } } \\ { { \overline { { { b } } } = b ^ { \mathrm { T } } \otimes E _ { n } , } } & { { Y = [ Y _ { 1 } , Y _ { 2 } , \cdots , Y _ { s } ] ^ { \mathrm { T } } } } \\ { { \overline { { { y } } } _ { n } = [ y _ { n } , y _ { n } , \cdots , y _ { n } ] ^ { \mathrm { T } } , } } & { { \overline { { { e } } } = e \otimes e _ { s } , } } \end{array}
$$

where $E _ { n }$ is an $n$ -stage identical matrix and $e = [ 1 , 1 , \cdots , 1 ] ^ { \mathrm { T } }$ is a $n$ -dimensional   
vector. For $\mathbf { R - K }$ method to be volume-preserving, we have equivalent condition:   
de t ∂ yn+1 ≡ 1. So, we need to calculate the matrix ∂ yn+1 1. In matrix notations, ∂ yn   
$\mathbf { R - K }$ method (9.4) reads

$$
\begin{array} { l } { { y _ { n + 1 } = y _ { n } + h M \overline { { { b } } } Y , } } \\ { { Y = ( 1 - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { y } } } _ { n } . } } \end{array}
$$

So,

$$
\begin{array} { r c l } { { y _ { n + 1 } } } & { { = } } & { { ( E _ { n } + ( h M \overline { { { b } } } ( I - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { e } } } ) y _ { n } } } \\ { { } } & { { \Longrightarrow } } & { { \displaystyle { \frac { \partial y _ { n + 1 } } { \partial y _ { n } } = E _ { n } + h M \overline { { { b } } } ( I - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { e } } } . } } } \end{array}
$$

Lemma 9.2. Let $A , D$ be non-degenerate $m \times m$ and $n \times n$ matrices respectively and $B$ an $m \times n$ and $C$ an $n \times m$ matrix, then

$$
\operatorname* { d e t } A \operatorname* { d e t } \left( D + C A ^ { - 1 } B \right) = \operatorname* { d e t } D \operatorname* { d e t } \left( A + B D ^ { - 1 } C \right) .
$$

The proof can be found in any textbook of linear algebra.

By Lemma 9.2, it is easy to get from (9.7)

$$
\operatorname* { d e t } \left( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \right) = \frac { \operatorname* { d e t } \left( I - h \overline { { M } } \overline { { A } } - \overline { { e } } M \overline { { b } } \right) } { \operatorname* { d e t } \left( I - h \overline { { M } } \overline { { A } } \right) } .
$$

Additionally, we define the notations

$$
\begin{array} { l l } { { A ^ { - } = ( a _ { i j } ^ { - } ) , ~ } } & { { a _ { i j } ^ { - } = a _ { i j } - b _ { j } , } } \\ { { { } } } & { { { } } } \\ { { N = A \otimes M , ~ N ^ { - } = A ^ { - } \otimes M . } } \end{array}
$$

In these notations, (9.7) reads as

$$
\operatorname* { d e t } \left( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \right) = \frac { \operatorname* { d e t } \left( I - h N ^ { - } \right) } { \operatorname* { d e t } \left( I - h N \right) } .
$$

Now, if (9.10) is identical to 1, we arrive at the criterion for $\mathbf { R - K }$ method (9.4) to be volume-preserving scheme as

$$
\operatorname* { d e t } \left( \lambda I - N ^ { - } \right) = \operatorname* { d e t } { \big ( } \lambda I - N { \big ) } , \quad \forall \lambda \in \mathbf { R } .
$$

Theorem 9.3. If dimension of $M$ is odd, then all the R–K methods based on high order quadrature formula such as Gauss–Legendre, Radau, and Lobatto are not volumepreserving.

Proof. Note that $N \ = \ A \otimes$ M and $N ^ { - } ~ = ~ A ^ { - } ~ \otimes ~ M$ . If the method is volumepreserving, then

$$
{ \begin{array} { r l } { \operatorname* { d e t } N = \operatorname* { d e t } ( N ^ { - } ) \iff \operatorname* { d e t } ( A \otimes M ) = \operatorname* { d e t } ( A ^ { - } \otimes M ) } \\ & { \iff ( \operatorname* { d e t } A ) ^ { n } ( \operatorname* { d e t } ( M ) ) ^ { s } = ( \operatorname* { d e t } ( A ^ { - } ) ) ^ { n } ( \operatorname* { d e t } M ) ^ { s } } \\ & { \iff ( \operatorname* { d e t } A ) ^ { n } = ( \operatorname* { d e t } ( A ^ { - } ) ) ^ { n } } \\ & { \iff \operatorname* { d e t } A = \operatorname* { d e t } ( A ^ { - } ) . } \end{array} }
$$

Now, we need the $W$ -transformation proposed by Hairer and Wanner $\mathrm { [ H W 8 1 ] }$ . They introduced a generalized square matrix $W$ defined by

$$
W = ( p _ { 0 } ( c ) , p _ { 1 } ( c ) , \cdot \cdot \cdot , p _ { n - 1 } ( c ) ) ,
$$

where the normalized shifted Legendre polynomials are defined by

$$
p _ { k } ( x ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k + i } \Big ( \begin{array} { c } { { k } } \\ { { i } } \end{array} \Big ) \Big ( \begin{array} { c } { { k + i } } \\ { { i } } \end{array} \Big ) x ^ { i } , \quad k = 0 , 1 , \cdots , s - 1 .
$$

For Gauss–Legendre, let $X = W ^ { - 1 } A W$ , then

$$
\begin{array} { r } { X = \left[ \begin{array} { c c c c c c } { \frac 1 2 } & { - \xi _ { 1 } } & & & & \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & & & \\ & { \xi _ { 2 } } & & & & \\ & & { \ddots } & { \ddots } & { - \xi _ { s - 1 } } \\ & & & & { \xi _ { s - 1 } } & { 0 } \end{array} \right] , } \end{array}
$$

where $\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } \left( k = 0 , 1 , \cdots , s - 1 \right)$ .

However, $X ^ { - } = W ^ { - 1 } A ^ { - } W$ , then

$$
X ^ { - } = \left[ \begin{array} { c c c c c c } { { - \frac { 1 } { 2 } } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { - \xi _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \xi _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { - \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { 0 } } \end{array} \right] .
$$

It is easy to verify that d $\operatorname { e t } X \neq \operatorname* { d e t } ( X ^ { - } ) \Rightarrow \operatorname* { d e t } A \neq \operatorname* { d e t } ( A ^ { - } ) .$ So, Gauss–Legendre method is not volume-preserving.

Using the Table 2.1 of Chapter 7, the remaining part of the proof is similar, where $\sigma \in \mathbf { R }$ and $u \sigma \neq 0$ .

Theorem 9.4. [QL00] If the dimension of $M$ is even, then the R–K methods based on high order quadrature formulas such as Gauss–Legendre, Lobatto III A, Lobatto III $B$ , Lobatto III $s$ , Radau $I B$ , and Radau IIB are volume-preserving, iff

$$
\lambda ( M ) = ( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , \cdot \cdot \cdot , - \lambda _ { \frac { n } { 2 } } ) .
$$

Proof. Assume $A , B$ are $n \times n$ and $m \times m$ matrices respectively, and their eigenvalue are respectively $\{ \lambda _ { 1 } , \lambda _ { 2 } , \dotsb , \lambda _ { n } \}$ and $\{ \mu _ { 1 } , \mu _ { 2 } , \cdots , \mu _ { m } \}$ . Then according to the property of Kronecker product, we have $\lambda ( A \otimes B ) = \{ \lambda _ { i } \mu _ { j } , i = 1 , \cdot \cdot \cdot , n ; j = 1 , \cdot \cdot \cdot , m \}$ . For $\mathbf { R - K }$ methods to be volume-preserving schemes, according to (9.11), $N$ and $N ^ { - }$ must have same eigenvalue, that is to say, $A \otimes M$ and $A ^ { - } \otimes M$ must have the same eigenvalues. For example, for Gauss–Legendre method, $\lambda ( A ) ~ = ~ \lambda ( X )$ and $\lambda ( A ^ { - } ) = \lambda ( X ^ { - } )$ , however, it is obvious that $\lambda ( X ) = - \lambda ( X ^ { - } )$ , so according to the properties of Kronecker product, we can easily verify that $A \otimes M$ and $A ^ { - } \otimes M$ have the same eigenvalues. -

tem, that is to say, invertible matrix, th $M \ : = \ : J ^ { - 1 } S$ , where $J = \left[ \begin{array} { c c } { 0 } & { I _ { n } } \\ { - I _ { n } } & { 0 } \end{array} \right]$ $S ^ { \prime } = S$ $n \times n$

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } \right) .
$$

So, the $\mathbf { R - K }$ method based on high order quadrature formula (Gauss–Legendre, Lobatto IIIA, Lobatto IIIB, Lobatto IIIS, Radau IB, and Radau IIB) are volumepreserving. The Theorem 9.4 says that for the methods to preserve volume, the system, in some sense, must be similar to a Hamiltonian system. If the matrix $M$ similar to an infinitesimally symplectic matrix, i.e., there is an invertible matrix $P$ , subjected to $P ^ { - 1 } M P = J S$ , $S ^ { \mathrm { T } } = S$ , then we can transform the system to a Hamiltonian system by a coordinate transformation. In this situation, the volume-preserving $\mathbf { R - K }$ methods and the symplectic $\mathbf { R - K }$ methods almost have no difference, that is, if $P$ is a symplectic matrix, then volume-preserving R–K methods are equivalent to symplectic $\mathbf { R - K }$ methods; and in this case, they can be transformed to one another by a linear transformation.

# 10.9.2 Volume-Preserving 2-Stage P–R–K Methods

In the case $r = 1$ , if the necessary and sufficient condition of Lemma 9.5 are satisfied, then a 2-stage P–R–K method is volume-preserving. This condition is the same condition of symplecity on the class of separable Hamiltonian system. Thus for system (9.3), all 2-stage P–R–K methods proposed $\mathrm { i n } ^ { [ \mathrm { S u n 9 5 } ] }$ are volume-preserving algorithms[QL00] .

Example 9.6. 3th order Radau IA-IA method

Example 9.7. 3th order Radau IIA-IIA method   

<table><tr><td>0</td><td>14</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>1</td><td>5</td><td></td><td></td><td></td></tr><tr><td>2</td><td>4</td><td>12</td><td>2</td><td>1</td><td>1</td></tr><tr><td></td><td>1</td><td>3-4</td><td></td><td>1</td><td>3-4</td></tr></table>

Example 9.8. 2nd order Lobatto IIIC-IIIC method   

<table><tr><td>1</td><td>5</td><td>1 12</td><td>1 1</td><td></td><td>0</td></tr><tr><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>1</td><td>4 4</td><td>4 1</td><td></td><td>1 4</td><td>0 1-4</td></tr></table>

Example 9.9. 4th order Gauss IA-IA method   

<table><tr><td>0</td><td>1</td><td>1-2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td></td><td>1</td><td>1</td><td></td><td>1</td><td>1</td></tr></table>

<table><tr><td>1 V3 6</td><td>1+2g 4</td><td>1-2σ 4</td><td>V3 6</td></tr><tr><td>1 V3 + 6</td><td>1-2σ V 十 6</td><td>1+2g</td><td></td></tr><tr><td></td><td>4 1</td><td>4 1</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>1-2 V3 6</td><td>1-2σ</td><td>1+2σ</td><td>V3</td></tr><tr><td></td><td>4</td><td>4</td><td>6</td></tr><tr><td>V</td><td>1+2σ V</td><td></td><td></td></tr><tr><td>1 + 6</td><td>+ 6</td><td>1-2σ</td><td></td></tr><tr><td></td><td>4</td><td>4</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td></td></tr><tr><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td></tr></table>

# 10.9.3 Some Generalizations

Method $\mathrm { i n } ^ { [ \mathrm { S u r 9 6 } ] }$ can be applied to the extension of following system:

$$
{ \dot { x } } = g ( y ) , \quad { \dot { y } } = h ( z ) , \quad { \dot { z } } = f ( x ) , \quad x , y , z \in \mathbf { R } ^ { P } .
$$

For this system, we consider multi-stage P–R–K method

$$
\xi _ { i } = x _ { n } + h \sum _ { j = 1 } ^ { m } d _ { i j } g ( \eta _ { j } ) , \ \eta _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { m } c _ { i j } h ( w _ { j } ) , \ w _ { j } = z _ { n } + h \sum _ { j = 1 } ^ { m } e _ { i j } f ( \xi _ { j } ) ,
$$

$$
x _ { n + 1 } = x _ { n } + h \sum _ { j = 1 } ^ { m } \alpha _ { j } g ( \eta _ { j } ) , y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { m } \beta _ { j } h ( w _ { j } ) , z _ { n + 1 } = z _ { n } + h \sum _ { j = 1 } ^ { m } \gamma _ { j } ( \xi _ { j } ) .
$$

Theorem 9.10. A multi-stage P–R–K method is volume-preserving for a system type (9.17), iff

$$
\begin{array} { r l } & { d _ { k _ { 1 } l _ { 1 } } c _ { l _ { 1 } m _ { 1 } } e _ { m _ { 1 } k _ { 2 } } d _ { k _ { 2 } l _ { 2 } } c _ { l _ { 2 } m _ { 2 } } e _ { m _ { 2 } k _ { 3 } } \cdot \cdot \cdot d _ { k _ { r } l _ { r } } c _ { l _ { r } m _ { r } } e _ { m _ { r } k _ { r } } } \\ & { = d _ { k _ { 1 } l _ { 1 } } ^ { - } c _ { l _ { 1 } m _ { 1 } } ^ { - } e _ { m _ { 1 } k _ { 2 } } ^ { - } d _ { k _ { 2 } l _ { 2 } } ^ { - } c _ { l _ { 2 } m _ { 2 } } ^ { - } e _ { m _ { 2 } k _ { 3 } } ^ { - } \cdot \cdot \cdot d _ { k _ { r } l _ { r } } ^ { - } c _ { l _ { r } m _ { r } } ^ { - } e _ { m _ { r } k _ { r } } ^ { - } } \end{array}
$$

for arbitrary $1 \leq r \leq m$ and three arbitrary ordered sets $\left( k _ { 1 } , \cdots , k _ { r } \right)$ , $\left( l _ { 1 } , \cdots , l _ { r } \right)$ , and $( m _ { 1 } , \cdots , m _ { r } )$ of different natural number form $[ 1 , \cdots , m ]$ , here $d _ { i j } , c _ { i j } , e _ { i j } , d _ { i j } ^ { - }$ , c−ij, e−ij are defined by Lemma 9.5.

Example 9.11. A multi-stage P–R–K method   

<table><tr><td>0</td><td>1</td><td>1 0</td><td>0</td><td>0</td><td>a</td><td>a 0</td></tr><tr><td>1</td><td>1</td><td>1 2</td><td>1</td><td>0</td><td>b+c</td><td>b C</td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>b 2c</td></tr></table>

Suitably choose $a , b , c ,$ , as method can get global truncation error with order $O ( h ^ { 2 } )$

Remark 9.12. Dimension of $x , y , z$ may be different.

Remark 9.13. Theorem 9.10 can be extended with no difficulty to the following system:

$$
{ \dot { x } } _ { 1 } = f _ { 2 } ( x _ { 2 } ) \quad { \dot { x } } _ { 2 } = f _ { 3 } ( x _ { 4 } ) , \quad \cdots , \quad { \dot { x } } _ { n } = f _ { 1 } ( x _ { 1 } ) .
$$

# 10.9.4 Some Explanations

We usually state that symplectic method is volume-preserving scheme. But this parlance is somewhat irrelevancy because symplectic scheme (satisfying symplectic condition), true only in this case, that it applied to Hamiltonian system. For P–R–K method $( d _ { i j } , \delta _ { i } , c _ { i j } , \gamma _ { j } )$ , if it satisfies

$$
\gamma _ { i } d _ { i j } + \delta _ { i } c _ { j i } - \gamma _ { i } \delta _ { j } = 0 ,
$$

we can say this integrator is symplectic. If system is not Hamiltonian, we cannot say that this $\mathrm { P - R - K }$ method is symplectic. The main problem is that we say a scheme is symplectic because it preserves symplectic structure for a given system. Therefore, only Hamiltonian system possesses symplectic structure. Consequently, we cannot say “volume-preserving P–R–K methods form a subset of symplectic ones”.

Until now, we gave some criteria for volume-preserving by $\mathbf { R - K }$ and P–R–K methods. In fact, it is almost impossible based on these criteria to construct volumepreserving algorithm with high order accuracy. Indeed, we even cannot predict that there exists schemes which satisfied those criteria. We are too far to resolve these problems.

It should be noted that in the above discussion, we always suppose system is not reducible. In other words, det $M \neq 0$ . But in practice, some systems are reducible, for example

$$
\begin{array} { r l } & { \dot { \boldsymbol { x } } = c \boldsymbol { y } - b \boldsymbol { z } , } \\ & { \dot { \boldsymbol { y } } = a \boldsymbol { z } - c \boldsymbol { x } , \quad a , b , c \in { \bf R } . } \\ & { \dot { \boldsymbol { z } } = b \boldsymbol { x } - a \boldsymbol { y } , } \end{array}
$$

In fact, for this system, centered Euler scheme is volume-preserving. Furthermore, LobattoIIIA, LobattoIIIB, LobattoIIIS, RadauIB, RadauIIB etc. are also volumepreserving. With detailed analysis of the process in Subsection 10.9.2, it is easy to get the following[QL00] .

Theorem 9.14. If the dimension of $M$ is odd, then the R–K methods based on high order quadrature formulae, such as LobattoIIIA, LobattoIIIB, LobattoIIIS, RadauI, RadauIIB etc., are volume-preserving, iff

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { \frac { n } { 2 } } , 0 , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdots , - \lambda _ { \frac { n } { 2 } } \right) .
$$

We also find that in Theorem 9.4, det $M \neq 0$ is not necessary.

As for nonlinear systems, we cannot give some satisfactory results. A nonlinear system

$$
\dot { y } = f ( y ) , \quad t \in \mathbf { R } , \ y \in \mathbf { R } ^ { n } ,
$$

is said to be source-free if $\mathrm { d i v } f = \sum _ { i = 1 } ^ { n } { \frac { \partial f _ { i } ( y ) } { \partial y _ { i } } } = 0 .$ . Such system preserves the phase volume on the phase $R ^ { n }$ . For these systems, we only point out the centered Euler

schemes is volume-preserving iff the Jacobian ∂ fi = M is, in some sense, similar to an infinitesimally symplectic matrix. That is, the eigenvalues of $M$ can be specified as

or

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdot \cdot \cdot , - \lambda _ { \frac { n } { 2 } } \right) ,
$$

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { \frac { n } { 2 } } , 0 , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdots , - \lambda _ { \frac { n } { 2 } } \right) .
$$

# Bibliography

[DV84] K. Dekker and J.G. Verwer: Stability of Runge–Kutta Methods for Stiff Initial Value Problems. Elesevier Science Pub. B. V., North-Holland, Amsterdam, (1984).   
[FS95] K. Feng and Z. J. Shang: Volume-preserving algorithms for source-free dynamical systems. Numer. Math., 71:451–463, (1995).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS, Vol. 163, pages 1–32. AMS, (1994).   
[HW81] E. Hairer and G. Wanner: Algebraically stable and implementable Runge–Kutta methods of high order. SIAM J. Numer. Anal., 18:1098–1108, (1981).   
[MQ04] R.I. McLachlan and G.R.W. Quispel: Explicit geometric integration of polynomial vector fields. BIT, 44:513–538, (2004).   
[QD97] G. R. W. Quispel and C. P. Dyt: Solving ODE’s numerically while preserving symmetries, Hamiltonian structure, phase space volume, or first integrals. In A. Sydow, editor, Proceedings of the 15th IMACS World Congress, pages 601–607. Wissenschaft & Technik, Berlin, (1997).   
[QD98] G. R. W. Quispel and C. P. Dyt: Volume-preserving integrators have linear error growth. Physics Letters A, 202:25–30, (1998).   
[QL00] M. Z. Qin and H. W. Li: Volume preserving R–K methods for linear systems. Acta Applicandae Mathematicae, 16:430–434, (2000).   
[QM03] G. R. W. Quispel and D. I. McLaren: Explicit volume-preserving and symplectic integrators for trigonometric polynomial flows. J. of Comp. Phys., 186(1):308–316, (2003).   
[Qui95] G. R. W. Quispel: Volume-preserving integrators. Physics Letters A, 206:26–30, (1995).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[QZ93] M. Z. Qin and W. J. Zhu: Volume-preserving schemes and numerical experiments. Computers Math. Applic., 26:33–42, (1993).   
[Sco91] C. Scovel: Symplectic numerical integration of Hamiltonian systems. In T. Ratiu, editor, The Geometry of Hamiltonian Systems, pages 463–496. Springer, New York, (1991).   
[Sha94a] Z Shang: Construction of volume-preserving difference schemes for source-free systems via generating functions. J. Comput. Math., 12:265–272, (1994).   
[Sha94b] Z. Shang: Generating functions for volume-preserving mappings and Hamilton– Jacobi equations for source-free dynamical systems. Science in China (series A), 37:1172– 1188, (1994).   
[Sun95] G. Sun: Construction of high order symplectic Partitioned–Runge–Kutta methods. J. Comput. Math., 13(1):40–50, (1995).   
[Sur96] Y. B. Suris: Partitioned–Runge–Kutta methods a phase volume preserving integrators. Physics Letters A, 220:63–69, (1996).   
[TH85] A. Thyagaraja and F.A. Haas: Representation of volume-preserving maps induced by solenoidal vector fields. Phys. Fluids, 28:1005, (1985).   
[Wey40] H. Weyl: The method of orthogonal projection in potential theory. Duke Math. J., 7:411–444, (1940).
