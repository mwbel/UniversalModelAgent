# Chapter III. Order Conditions,Treesand B-Series

Inthis chapter we present acompact theory of the order conditions of the methodspresented in Chap.II, in particular Runge-Kutta methods,partitioned Runge-Kuttamethods,and composition methods by using the notion of rooted trees and B-series.These ideas lead to algebraic structureswhich haverecently found interestingapplications inquantum field theory.The chapter terminateswith the Baker-Campbell-Hausdorff formula,which allowsanother access to the order properties ofcomposition and splitting methods.

Someparts of this chapter are rather short,but nevertheless self-contained.For more detailed presentations werefer to the monographs of Butcher(1987),of Hairer, Ngrsett&Wanner(1993）,andofHairer&Wanner(1996).Readersmainlyinterested in geometric properties of numerical integrators may continue with ChaptersIV,VorVI beforereturningtothe technically moredifficult jungleof trees.

# III.1Runge-Kutta Order Conditions and B-Series

Even the standard notation has been found to be too heavy indealingwith fourthand higher order processes,... (R.H.Merson 1957）

Inthis section we derive the order conditions of Runge-Kutta methods by comparing the Taylor series of the exact solution of（1.1）with that of thenumerical solution.The computation ismuch simplified,first by consideringan autonomous system of equations(Gill 1951),and second,by the use of rooted trees (connected graphswithout cycles and a distinguished vertex;Merson 1957).The theory has beendeveloped by Butcherin theyears 1963-72(seeButcher(1987),Sect.30)and byHairer&Wannerin1973-74（seeHairer,Ngrsett&Wanner（1993)SectionsII.2 andII.12).Herewe give new simplified proofs.

# III.1.1 Derivation of the Order Conditions

We consider an autonomous problem

$$
\dot { y } = f ( y ) , \qquad y ( t _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ issufficientlydifferentiable.Aproblem $\dot { \boldsymbol { y } } = \boldsymbol { f } ( t , \boldsymbol { y } )$ can be brought into this form by appending the equation $i = 1$ .We develop the subsequent theory in four steps.


<!-- chunk 0002: pages 71-140 -->
Er sagte es klarund angenehm, waserstens,zweitensund drittens kam'.

First Step.We compute the higher derivatives of the solution $y$ at the initial point $t _ { 0 }$ .For this,we have from(1.1)

$$
y ^ { ( q ) } = \left( f ( y ) \right) ^ { ( q - 1 ) }
$$

and compute the latter derivatives by using the chain rule,the product rule,the symmetry of partial derivatives,and the notation $f ^ { \prime } ( y )$ forthederivativeasa linear map (the Jacobian）, $f ^ { \prime \prime } ( y )$ thesecond derivativeasabilinear mapand similarly for higherderivatives.This gives

$$
\begin{array} { r l } { { \dot { y } ~ = ~ f ( y ) } } & { { } } \\ { { \dot { y } ~ = ~ f ^ { \prime } ( y ) \dot { y } } } & { { } } \\ { { y ^ { ( 3 ) } ~ = ~ f ^ { \prime \prime } ( y ) ( \dot { y } , \dot { y } ) + f ^ { \prime } ( y ) \ddot { y } } } & { { } } \\ { { y ^ { ( 4 ) } ~ = ~ f ^ { \prime \prime \prime } ( y ) ( \dot { y } , \dot { y } , \dot { y } ) + 3 f ^ { \prime \prime } ( y ) ( \dot { y } , \dot { y } ) + f ^ { \prime } ( y ) y ^ { ( 3 ) } } } & { { } } \\ { { y ^ { ( 5 ) } ~ = ~ f ^ { ( 4 ) } ( y ) ( \dot { y } , \dot { y } , \dot { y } ) + 6 f ^ { \prime \prime \prime } ( y ) ( \ddot { y } , \dot { y } , \dot { y } ) + 4 f ^ { \prime \prime } ( y ) ( y ^ { ( 3 ) } , \ddot { y } ) } } & { { } } \\ { { } } & { { } } & { { + 3 f ^ { \prime \prime } ( y ) ( \ddot { y } , \ddot { y } ) + f ^ { \prime } ( y ) y ^ { ( 4 ) } { } _ { \ast } } } \end{array}
$$

and so on. The coefficients $3 , 6 , 4 , 3 , \ldots$ appearing in these expressions haveacertaincombinatorial meaning(number of partitions of a setof $q - 1$ elements),but for the moment we need not know their values.

Second Step.We insert in（1.3)recursively thecomputed derivatives $\dot { y }$ ， $\ddot { y } , \dots$ into theright side ofthe subsequent formulas.This gives for the first few

$$
\begin{array} { r l } { \dot { y } ~ = ~ f } & { } \\ { \ddot { y } ~ = ~ f ^ { \prime } f } & { } \\ { \dot { y } ^ { ( 3 ) } ~ = ~ f ^ { \prime \prime } ( f , f ) + f ^ { \prime } f ^ { \prime } f } & { } \\ { \dot { y } ^ { ( 4 ) } ~ = ~ f ^ { \prime \prime \prime } ( f , f , f ) + 3 f ^ { \prime \prime } ( f ^ { \prime } f , f ) + f ^ { \prime } f ^ { \prime \prime } ( f , f ) + f ^ { \prime } f ^ { \prime } f ^ { \prime } f , } \end{array}
$$

where the arguments $( y )$ have been suppressed.The expressionswhich appear in these formulas,denoted by $F ( \tau )$ ,willbecalled theelementarydifferentials.We represent each of them bya suitable graph $\tau$ (arooted tree) as follows:

Each $f$ becomesavertex,a firstderivative $f ^ { \prime }$ becomesa vertexwith one branch,anda $k$ thderivative $f ^ { ( k ) }$ becomesa vertex with $k$ branches pointing upwards.The arguments of the $k$ -linearmapping $f ^ { ( k ) } ( y )$ correspond totrees that areattached on theupper ends of these branches.The tree to the right correspondsto $f ^ { \prime \prime } ( f ^ { \prime } f , f ) .$ Other trees are plotted in Table 1.1.In theabove process,each insertion ofanalready known derivative consists of grafting the corresponding trees upon a new root as in Definition1.1below,and inserting thecorresponding elementarydiferentialsas arguments of $f ^ { ( m ) } ( y )$ as in Definition 1.2.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/9abeeec815008a436d62b43effd83c78cd1e88629d6a4ec5b64159484db11758.jpg)

Table1.1.Trees,elementarydifferentials,andcoefficients   

<table><tr><td rowspan=1 colspan=1>|</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>a（T）</td><td rowspan=1 colspan=1>F(r)</td><td rowspan=1 colspan=1>(）</td><td rowspan=1 colspan=1>（)</td><td rowspan=1 colspan=1>（）</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>f</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>∑b</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>、</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ff</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Mbiaij</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>[][·1]</td><td rowspan=1 colspan=1>,Y&gt;</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>f&quot;(f,f)ff&#x27;f</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>∑ijkbiaijaik∑ykbiaijajk</td><td rowspan=1 colspan=1>21</td></tr><tr><td rowspan=1 colspan=1>4444</td><td rowspan=1 colspan=1>[,][·]][·，1]·</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1311</td><td rowspan=1 colspan=1>f&quot;(f,f.f)f&quot;(s&#x27;f,f)f&#x27;f&quot;(f,f)f&#x27;f&#x27;sf</td><td rowspan=1 colspan=1>481224</td><td rowspan=1 colspan=1>∑ijkibiaijaikail∑ijktbiaijaikaji£ijkibaijajkajl∑ijkbiaijajkakl</td><td rowspan=1 colspan=1>6121</td></tr></table>

Definition1.1 (Trees).The set of(rooted) trees $T$ is recursively defined as follows: a)thegraph·with onlyonevertex(called theroot) belongsto $T$ ;

b)if $\tau _ { 1 } , . . . , \tau _ { m } \in T$ ,then the graph obtained by grafting the roots of $\tau _ { 1 } , \ldots , \tau _ { m }$ toanew vertexalso belongs to $x _ { * }$ It is denoted by

$$
\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] ,
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/6f5d3747bd1bafa3a7bfc12bcae000da8c733fc5984df89c6dd612e78fb34b02.jpg)

and thenewvertex is therootof $\gamma$ .

We further denote by $| \tau |$ the order of $\tau$ (thenumber of vertices),and by $\alpha ( \tau )$ the coefficients appearing inthe formulas(1.4).We remark that some of the trees among $\tau _ { 1 } , \dots , \tau _ { m }$ may be equal and that $\tau$ does not depend on the ordering of $\tau _ { 1 } , . . . , \tau _ { m }$ Forexample,we do not distinguish between $[ [ \bullet ] , \bullet ]$ and $[ \bullet , [ \bullet ] ]$ .

Definition1.2 (Elementary Differentials).Foratree $\tau \in \mathcal { I }$ theelementarydifferentialisamapping $\begin{array} { r } { F ( \tau ) : \mathbb { R } ^ { n }  \mathbb { R } ^ { n } } \end{array}$ ,defined recursively by $F ( \bullet ) ( y ) = f ( y )$ and

$$
F ( \tau ) ( y ) = f ^ { ( m ) } ( y ) \Bigl ( F ( \tau _ { 1 } ) ( y ) , \ldots , F ( \tau _ { m } ) ( y ) \Bigr ) \qquad \mathrm { f o r } \quad \tau = [ \tau _ { 1 } , \ldots , \tau _ { m } ] ,
$$

Examples of these constructions and the corresponding coeficients are seen in [able1.1.With these definitions,weobtain from(1.4）:

Theorem1.3.Theqthderivativeoftheexact solutionis givenby

$$
y ^ { ( q ) } ( t _ { 0 } ) = \sum _ { | \tau | = q } \alpha ( \tau ) F ( \tau ) ( y _ { 0 } ) ,
$$

where $\alpha ( \tau )$ arepositive integer coefficients.

Third Step.We now turn to the numerical solution of the Runge-Kutta method (II.1.4),which,byputting $h k _ { i } = g _ { i }$ ,wewrite as

$$
g _ { i } = h f ( u _ { i } )
$$

and

$$
u _ { i } = y _ { 0 } + \sum _ { j } a _ { i j } g _ { j } , \qquad y _ { 1 } = y _ { 0 } + \sum _ { i } b _ { i } g _ { i } ,
$$

where $u _ { i } , \textit { g } _ { i }$ and $y _ { 1 }$ are functions of $h$ Wedevelop the derivatives of(1.6),by Leibniz'rule,and obtaing $g _ { i } ^ { ( q ) } = h ( f ( u _ { i } ) ) ^ { ( q ) } + q \cdot ( f ( u _ { i } ) ) ^ { ( q - 1 ) }$ This gives,for $h = 0$ ，

$$
g _ { i } ^ { ( q ) } = q \cdot ( f ( u _ { i } ) ) ^ { ( q - 1 ) } ,
$$

the same expression as in (1.2),with $y$ just replaced by $u _ { i }$ and with an extra factor $q$ .Consequently,exactlyasin(1.3）,

$$
\begin{array} { r l } { \dot { g } _ { i } = 1 \cdot f ( y _ { 0 } ) } & { } \\ { \dot { g } _ { i } = 2 \cdot f ^ { \prime } ( y _ { 0 } ) \dot { u } _ { i } } & { ( 1 - f ^ { \prime \prime } ( y _ { 0 } ) \dot { u } _ { i } ) } \\ { \dot { g } _ { i } ^ { ( 3 ) } = 3 \cdot \big ( f ^ { \prime \prime } ( y _ { 0 } ) ( \dot { u } _ { i } , \dot { u } _ { i } ) + f ^ { \prime } ( y _ { 0 } ) \ddot { u } _ { i } \big ) } & { } \\ { \dot { g } _ { i } ^ { ( 4 ) } = 4 \cdot \big ( f ^ { \prime \prime \prime } ( y _ { 0 } ) ( \dot { u } _ { i } , \dot { u } _ { i } , \dot { u } _ { i } ) + 3 f ^ { \prime \prime } ( y _ { 0 } ) ( \ddot { u } _ { i } , \dot { u } _ { i } ) + f ^ { \prime } ( y _ { 0 } ) u _ { i } ^ { ( 3 ) } \big ) } & { } \\ { \dot { g } _ { i } ^ { ( 5 ) } = 5 \cdot \big ( f ^ { ( 4 ) } ( y _ { 0 } ) ( \dot { u } _ { i } , \dot { u } _ { i } , \dot { u } _ { i } ) + 6 f ^ { \prime \prime \prime } ( y _ { 0 } ) ( \ddot { u } _ { i } , \dot { u } _ { i } , \dot { u } _ { i } ) + 4 f ^ { \prime \prime } ( y _ { 0 } ) ( u _ { i } ^ { ( 3 ) } , \dot { u } _ { i } ) } & { } \\ & { } & { + 3 f ^ { \prime \prime } ( y _ { 0 } ) ( \ddot { u } _ { i } , \ddot { u } _ { i } ) + f ^ { \prime } ( y _ { 0 } ) u _ { i } ^ { ( 4 ) } \big ) , } \end{array}
$$

and so on.Here,the derivatives of $g _ { i }$ and $u _ { i }$ are evaluated at $h = 0$ ,

Fourth Step.We now insert recursively the derivatives $\dot { u } _ { i }$ , ${ \ddot { u } } _ { i } , \dots$ into (1.9). This will give the next higherderivative of $g _ { i }$ ,and,using

$$
u _ { i } ^ { ( q ) } = \sum _ { j } a _ { i j } \cdot g _ { j } ^ { ( q ) } ,
$$

which follows from(1.7),also the next higher derivative of $u _ { i }$ .This process begins as

$$
\begin{array} { c c } { { \dot { g } _ { i } = 1 \cdot f } } & { { \ddot { u } _ { i } = 1 \cdot \left( \sum _ { j } a _ { i j } \right) \cdot f } } \\ { { \ddot { g } _ { i } = \left( 1 \cdot 2 \right) \left( \sum _ { j } a _ { i j } \right) f ^ { \prime } f } } & { { \ddot { u } _ { i } = \left( 1 \cdot 2 \right) \left( \sum _ { j k } a _ { i j } a _ { j k } \right) f ^ { \prime } f } } \end{array}
$$

and so on.If we compare these formulaswith the first lines of(1.4),we see that the resultsareprecisely the same,apart from the extra factors.Wedenote theinteger factors $1$ ， $1 \cdot 2 , \ldots$ by $\gamma ( \tau )$ and the factors containing the $a _ { i j }$ 'sby $\mathbf { g } _ { i } ( \tau )$ and ${ \mathbf { u } } _ { i } ( \tau )$ ， respectively.We obtain byinduction that the same happens in general,i.e. that,in contrast to（1.5）,

$$
\begin{array} { l } { { \displaystyle g _ { i } ^ { ( q ) } \big | _ { h = 0 } = \sum _ { | \tau | = q } \gamma ( \tau ) \cdot \mathbf { g } _ { i } ( \tau ) \cdot \boldsymbol \alpha ( \tau ) F ( \tau ) ( y _ { 0 } ) } } \\ { { \displaystyle u _ { i } ^ { ( q ) } \big | _ { h = 0 } = \sum _ { | \tau | = q } \gamma ( \tau ) \cdot \mathbf { u } _ { i } ( \tau ) \cdot \boldsymbol \alpha ( \tau ) F ( \tau ) ( y _ { 0 } ) , } } \end{array}
$$

where $\alpha ( \tau )$ and $F ( \tau )$ are the same quantities as before.This is seen by continuing theinsertionprocessoftederitives $u _ { i } ^ { ( q ) }$ intotheright-handsideof(1.9).For example,if $\dot { u } _ { i }$ and $\ddot { u } _ { i }$ are inserted into $3 f ^ { \prime \prime } ( \ddot { u } _ { i } , \dot { u } _ { i } )$ ,wewill obtain the corresponding expressionasin(1.4),multipliedby the two extra factors ${ \bf u } _ { i } ( \boldsymbol { \zeta } )$ ,broughtin by $\ddot { u } _ { i }$ , and $\mathbf { u } _ { i } ( \cdot , )$ from $\dot { u } _ { i } .$ Fora general tree $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ]$ thiswill be

$$
\mathbf { g } _ { i } ( \tau ) = \mathbf { u } _ { i } ( \tau _ { 1 } ) \cdot \dots \cdot \mathbf { u } _ { i } ( \tau _ { m } ) .
$$

Second,the factors $\gamma ( \tilde { \mathcal { J } } )$ and $\gamma ( \bullet )$ will receive the additional factor $q = | \tau |$ from (1.9),i.e.,wewill have in general

$$
\gamma ( \tau ) = | \tau | \gamma ( \tau _ { 1 } ) \cdot \dots \cdot \gamma ( \tau _ { m } ) .
$$

Then,by (1.10),

$$
\mathbf { u } _ { i } ( \tau ) = \sum _ { j } a _ { i j } \mathbf { g } _ { j } ( \tau ) = \sum _ { j } a _ { i j } \cdot \mathbf { u } _ { j } ( \tau _ { 1 } ) \cdot \ldots \cdot \mathbf { u } _ { j } ( \tau _ { m } ) .
$$

This formula can be re-used repeatedly,as longas some of the trees $\tau _ { 1 } , \ldots , \tau _ { m }$ are of order $> 1$ Finally,we havefromthelast formulaof(1.7),that thecoefficients for thenumerical solution,which we denote by $\phi ( \tau )$ andcall the elementaryweights, satisfy

$$
\phi ( \tau ) = \sum _ { i } b _ { i } \mathbf { g } _ { i } ( \tau ) .
$$

We summarize the result as follows:

Theorem1.4.Thederivativesof thenumerical solution ofa Runge-Kuttamethod (I1.1.4),for $h = 0$ ,aregiven by

$$
y _ { 1 } ^ { ( q ) } \big | _ { h = 0 } = \sum _ { | \tau | = q } \gamma ( \tau ) \cdot \phi ( \tau ) \cdot \alpha ( \tau ) F ( \tau ) ( y _ { 0 } ) ,
$$

where $\alpha ( \tau )$ and $F ( \tau )$ arethesameas in Theorem1.3,thecoeffcients $\gamma ( \tau )$ satisfy $\gamma ( \bullet ) = 1$ and(1.14).The elementaryweights $\phi ( \tau )$ areobtained fromthetree $\tau$ as follows:attachtoevery vertexa summationletter(" $\boldsymbol { \imath }$ "totheroot),then $\phi ( \tau )$ isthe sum,over all summation indices,ofa product composedof $b _ { i }$ ,andfactors $a _ { j k }$ for eachvertex" $\jmath$ "directlyconnected with" $k$ "byanupwardsdirectedbranch.

Proof.Repeated application of(1.15)followedby(1.16) shows that the elementary weight $\phi ( \tau )$ is the collection of $\sum _ { i } b _ { i }$ from (1.16)and all $\sum _ { j } a _ { i j }$ of (1.15). □

Theorem1.5.TheRunge-Kuttamethodhas orderpifandonlyif

$$
\phi ( \tau ) = { \frac { 1 } { \gamma ( \tau ) } } \qquad f o r \quad | \tau | \leq p .
$$

Proof.The comparison of Theorem1.3with Theorem 1.4proves the sufficiency ofcondition(1.18).The necessity of(1.18) follows from the independence of the elementarydifferentials(seee.g.,Hairer,Ngrsett&Wanner(1993),Exercise4of Sect.II.2). □

Example1.6.For the followingtree of order9we have

or,by using $\begin{array} { r } { \sum _ { j } a _ { i j } = c _ { i } , } \end{array}$

$$
\sum _ { i , j , k , l } b _ { i } c _ { i } a _ { i j } c _ { j } a _ { i k } c _ { k } a _ { k l } c _ { l } ^ { 2 } = \frac { 1 } { 2 7 0 } .
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/b549ee22a6c42d8f0895b8ac821fec9761d5a423d82f03ca6f20a2fd842c4c5b.jpg)

Thequantities $\phi ( \tau )$ and $\gamma ( \tau )$ forall treesupto order4are given inTable1.1.This alsoverifies the formulas(II.1.6)stated previously.

# III.1.2 B-Series

Wenow introduce the concept of B-series,which gives further insight into the behaviour of numerical methods and allows extensions to more general classes of methods.

Motivated by formulas(1.12) and(1.17)above,we consider the corresponding seriesas the objects of our study.This means,we study power series in $\displaystyle h ^ { ( \tau | }$ containingelementarydifferentials $F ( \tau )$ andarbitrary coefficientswhichare nowwritten in theform $a ( \tau )$ Such serieswill becalledB-series.Tomovefrom(1.6) to(1.13）we need to prove a result stating that a $B$ -seriesinsertedinto $h f ( \cdot )$ isagain a $B$ -series. We startwith

$$
B ( a , y ) = y + a ( \bullet ) h f ( y ) + a ( \underline { { I } } ) h ^ { 2 } ( f ^ { \prime } f ) ( y ) + \ldots = y + \delta ,
$$

and get by Taylor expansion

$$
h f \big ( B ( a , y ) \big ) = h f ( y + \delta ) = h f ( y ) + h f ^ { \prime } ( y ) \delta + \frac { h } { 2 ! } f ^ { \prime \prime } ( y ) ( \delta , \delta ) \mp \ldots .
$$

Inserting $\delta$ from(1.19)and multiplyingout,we obtain the expression

$$
\begin{array} { c } { { h f \big ( B ( a , y ) \big ) = h f + h ^ { 2 } a ( { \bullet } ) f ^ { \prime } f + h ^ { 3 } a ( { \underline { { { f } } } } ^ { \prime } ) f ^ { \prime } f ^ { \prime } f + \displaystyle \frac { h ^ { 3 } } { 2 ! } a ( { \bullet } ) ^ { 2 } f ^ { \prime \prime } ( f , f ) } } \\ { { + h ^ { 4 } a ( { \bullet } ) a ( \underline { { { f } } } ) f ^ { \prime \prime } ( f ^ { \prime } f , f ) \mp \ldots \qquad } } \end{array}
$$

This beautiful formulais not yetperfect for two reasons.First,there isadenominator 2!inthe fourth term.Theorigin of this lies in the symmetry of the tree $8$ We thus introduce the symmetry coefficients of Definition 1.7(following Butcher1987, Theorem 144A).Second,there is nofirstterm $y$ We thereforeallow the factor $a ( \emptyset )$ in Definition 1.8.

Definition1.7 (Symmetry coefficients).Thesymmetry coefficients $\sigma ( \tau )$ aredefined by $\sigma ( \cdot ) = 1$ and,for ${ \boldsymbol { \tau } } = [ \tau _ { 1 } , \dots , \tau _ { m } ]$ ，

$$
\sigma ( \tau ) = \sigma ( \tau _ { 1 } ) \cdot \ldots \cdot \sigma ( \tau _ { m } ) \cdot \mu _ { 1 } ! \mu _ { 2 } ! \cdot \ldots \ ,
$$

where the integers $\mu _ { 1 } , \mu _ { 2 } , \ldots$ count equal trees among $\mathbf { \psi } ^ { \prime } 1 , \dots , \mathbf { \psi } ^ { \prime } m$

Definition 1.8 (B-Series).Fora mapping $a : T \cup \{ \varnothing \} \to \mathbb { R }$ a formal series of the form

$$
B ( a , y ) = a ( \emptyset ) y + \sum _ { \tau \in T } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } a ( \tau ) F ( \tau ) ( y )
$$

iscalled a $B$ -series.

Themain results of the theory of B-series have their originin the paper of Butcher(1972),although series expansions were not used there.B-serieswere then introduced by Hairer&Wanner(1974).The normalizationused inDefinition 1.8 isdueto Butcher& Sanz-Serna(1996).The following fundamental lemma gives a second way of finding the order conditions.

Lemma 1.9. Let $a : T \cup \{ \varnothing \}  \mathbb { R }$ bea mapping satisfying $a ( \emptyset ) = 1$ Thenthe corresponding $B$ -seriesinsertedinto $h f ( \cdot )$ isagain $u$ $B$ -series.Thatis

$$
h f \Big ( B ( a , y ) \Big ) = B ( a ^ { \prime } , y ) ,
$$

where $a ^ { \prime } ( \varnothing ) = 0$ $a ^ { \prime } ( \bullet ) = 1 ,$ and

$$
a ^ { \prime } ( \tau ) = a ( \tau _ { 1 } ) * \ldots \cdot a ( \tau _ { m } ) { \mathrm { ~ } } f o r = [ \tau _ { 1 } , \ldots , \tau _ { m } ] .
$$

Proof.Since $a ( \emptyset ) = 1$ we have $B ( a , y ) = y + \mathcal { O } ( h )$ ,sothat $h f \left( B ( a , y ) \right)$ can be expanded intoa Taylor series around $y$ Asinformulas(1.20)and(1.21),weget

$$
\begin{array} { r l } & { \displaystyle h f \big ( B ( a , y ) \big ) = h \sum _ { m \geq 0 } \frac { 1 } { m ! } \frac { 1 } { m ! } f ^ { ( m ) } \big ( y \big ) \Big ( B ( a , y ) - y \Big ) ^ { m } } \\ & { \qquad = h \sum _ { m \geq 0 } \frac { 1 } { m ! } \frac { 1 } { m ! c ! } \cdots \sum _ { v _ { m } \in T } \frac { h ^ { [ r _ { 1 } ] + \ldots + [ r _ { m } ] } } { \tau ( \tau ( \tau ) ) \cdot \dots \cdot \sigma ( \tau _ { m } ) } \cdot a ( \tau _ { 1 } ) \cdot \dots \cdot a ( \tau _ { m } ) } \\ & { \qquad \cdot f ^ { ( m ) } \big ( y \big ) \Big ( F ( \tau _ { 1 } ) ( y ) , \dots , F ( \tau _ { m } ) ( y ) \Big ) } \\ & { \displaystyle = \sum _ { m \geq 0 } \sum _ { \tau \in T } \cdots \sum _ { \tau _ { m } \in T } \frac { h ^ { [ r _ { 1 } ] } } { \sigma ( \tau ) } \frac { \mu _ { 1 } ! \mu _ { 2 } ! \cdots \dots } { m ! } \cdot a ^ { \prime } ( \tau ) F ( \tau ) ( y ) } \\ & { \qquad \mathrm { w i t h ~ } \tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] } \\ & { \displaystyle = \sum _ { \tau \in T } \frac { h ^ { [ r ] } } { \sigma ( \tau ) } a ^ { \prime } ( \tau ) F ( \tau ) ( y ) = B ( a ^ { \prime } , y ) . } \end{array}
$$

Thelast equality follows from the fact that there are $\binom { m } { \mu _ { 1 } , \mu _ { 2 } , \dots }$ possibilities for writing the tree $\tau$ inthe form $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ]$ Forexample,the trees $[ \bullet , \bullet , [ \bullet ] ]$ , $[ \bullet , [ \circ ] , \bullet ]$ and $\left[ \left( \bullet \right] , \bullet , \bullet \right]$ appearasdifferent termsintheuppersum,but onlyas oneterm in the lowersum. □

Back to the Order Conditions.We present nowa new derivation of the order conditions that issolely based onB-seriesand onLemma 1.9.LetaRunge-Kutta method,say formulas(1.6)and(1.7),be given.All quantities inthedefiningformulasare set upas B-series, $g _ { i } = B ( \mathbf { g } _ { i } , y _ { 0 } )$ ， $u _ { i } = B ( \mathbf { u } _ { i } , y _ { 0 } )$ , $y _ { 1 } = B ( \phi , y _ { 0 } )$ Then, eitherthe linearityand/orLemma 1.9,translatetheformulasofthemethod into corresponding formulas for the coefficients(1.13),(1.15),and(1.16).Thisrecursively justifies the ansatz asB-series.

Assuming the exact solution to be a B-series $B ( \mathbf { e } , y _ { 0 } )$ ,aterm-by-termderivation ofthisseriesandanapplication ofLemma1.9to(1.1)yields

$$
\mathbf { e } ( \tau ) = { \frac { 1 } { | \tau | } } \mathbf { e } ( \tau _ { 1 } ) \cdot \ldots \cdot \mathbf { e } ( \tau _ { m } ) .
$$

Together with definition(1.14)of $\gamma ( \tau )$ we thus obtain

$$
{ \bf e } ( \tau ) = \frac { 1 } { \gamma ( \tau ) } .
$$

Acomparison of the coefficients of the B-series $y _ { 1 } = B ( \varphi , y _ { 0 } )$ with those of the exact solution gives(1.18)and proves Theorem 1.5again.

Comparing the B-series $B ( \mathbf { e } , y _ { 0 } )$ for the exact solution with Theorem 1.3,we getasabyproductthe formula

$$
\alpha ( \tau ) = \frac { | \tau | ! } { \sigma ( \tau ) \cdot \gamma ( \tau ) } .
$$

Iftheavailabletools areenriched bythe more general composition law ofTheorem1.10 below,thisprocedure can be applied to yet larger classes of methods.

# II.1.3Composition of Methods

The order theory for the composition of methods goes back to 1969,when Butcher used ittocircumvent the orderbarrier forexplicit 5th order5stage methods.Itled to theseminal publication of Butcher(1972),where the general composition formula in(1.34) was expressed recursively.

Composition of Runge-Kutta Methods.Suppose that,starting from an initial value $y _ { 0 }$ ,wecompute a numerical solution $y _ { 1 }$ usinga Runge-Kutta method with coefficients $a _ { i j } , b _ { i }$ and step size $h$ Then,continuing from $y _ { 1 }$ ,we computeavalue $y _ { 2 }$ using another method with coefficients $a _ { i j } ^ { * } , b _ { i } ^ { * }$ and the same step size.This composition of twomethods isnow considered asa single method(withcoefficients ${ \widehat { a } } _ { i j } , { \widehat { b } } _ { i } )$ .Theproblemis to derive the order properties of this newmethod,inparticular to express the elementary weights $\hat { \phi } ( \tau )$ in terms of those of the original two methods.

If thevalue $y _ { 1 }$ fromthe first method is insertedinto the starting value for the second method,one sees that the coefficients of the combined methodare given by (herewritten for two-stage methods)

$$
| \begin{array} { c c c c c } { { \hat { a } _ { 1 1 } } } & { { \hat { a } _ { 1 2 } } } & { { } } & { { } } & { { } } \\ { { \hat { a } _ { 2 1 } } } & { { \hat { a } _ { 2 2 } } } & { { } } & { { } } & { { } } \\ { { \hat { a } _ { 3 1 } } } & { { \hat { a } _ { 3 2 } } } & { { \hat { a } _ { 3 3 } } } & { { \hat { a } _ { 3 4 } } } & { { } } \\ { { \hat { a } _ { 4 1 } } } & { { \hat { a } _ { 4 2 } } } & { { \hat { a } _ { 4 3 } } } & { { \hat { a } _ { 4 4 } } } & { { } } \\ { { \widehat b _ { 1 } } } & { { \widehat b _ { 2 } } } & { { \widehat b _ { 3 } } } & { { \widehat b _ { 4 } } } & { { } } \end{array} | \begin{array} { c c c c c } { { \hat { a } _ { 1 1 } } } & { { \hat { a } _ { 1 2 } } } & { { } } & { { } } & { { } } \\ { { \hat { a } _ { 2 1 } } } & { { \hat { a } _ { 2 2 } } } & { { } } & { { } } & { { } } \\ { { \hat { b } _ { 1 } } } & { { \hat { b } _ { 2 } } } & { { \hat { a } _ { 1 1 } ^ { * } } } & { { \hat { a } _ { 1 2 } ^ { * } } } & { { } } \\ { { \hat { b } _ { 1 } } } & { { \hat { b } _ { 2 } } } & { { \hat { a } _ { 2 1 } ^ { * } } } & { { \hat { a } _ { 2 2 } ^ { * } } } & { { } } \\ { { \hat { b } _ { 1 } } } & { { \hat { b } _ { 2 } } } & { { \hat { b } _ { 1 } ^ { * } } } & { { \hat { b } _ { 2 } ^ { * } } } & { { } } \end{array} |
$$

and our problem is to compute the elementary weights of this scheme.

DerivationTheetiuf $\hat { \phi } ( \tau )$ sayfor thetree $\oint$ , i fuleal

$$
\widehat { \phi } ( \dot { \mathbb { V } } ) = \sum _ { i = 1 } ^ { 4 } \sum _ { j = 1 } ^ { 4 } \sum _ { k = 1 } ^ { 4 } \sum _ { l = 1 } ^ { 4 } \widehat { b } _ { i } \widehat { a } _ { i j } \widehat { a } _ { i k } \widehat { a } _ { k l } = \dots .
$$

$2 ^ { | \tau | }$ -2 $\begin{array} { r l } & { \sum _ { i = 1 } ^ { 2 } \sum _ { j = 1 } ^ { 2 } \sum _ { k = 1 } ^ { 2 } \sum _ { l = 1 } ^ { 2 } . / . + \sum _ { i = 3 } ^ { 4 } \sum _ { j = 1 } ^ { 2 } \sum _ { k = 1 } ^ { 2 } \sum _ { l = 1 } ^ { 2 } . / . + } \end{array}$ ∑²=1∑=3∑²=1∑²=1·/.+...We symbolizeeach expression by drawing the corresponding vertex of $\tau$ asabullet forthe first index set and asa star for the second.However,due to the zero pattern in the matrix in（1.28)(the upper right corner ismissing),each term with“star above bulletcan be omitted,since the corresponding $\widehat { a } _ { i j }$ 'sare zero.So the only combinations to be considered are those of Fig.1.1. Wefinally insert thequantities from theright tableau in（1.28),

$$
\begin{array} { r l } & { \hat { \rho } ( \hat { \bigstar } ) } \\ & { \qquad + \sum b _ { i } a _ { i j } a _ { i k } a _ { k l } + \sum b _ { i } ^ { * } b _ { j } b _ { k } a _ { k l } + \sum b _ { i } ^ { * } a _ { i j } ^ { * } b _ { k } a _ { k l } + \sum b _ { i } ^ { * } b _ { j } a _ { i k } ^ { * } b _ { l } } \\ & { \qquad + \sum b _ { i } ^ { * } a _ { i j } ^ { * } a _ { i k } ^ { * } b _ { l } + \sum b _ { i } ^ { * } b _ { j } a _ { i k } ^ { * } a _ { k l } ^ { * } + \sum b _ { i } ^ { * } a _ { i j } ^ { * } a _ { i k } ^ { * } a _ { k l } ^ { * } , } \end{array}
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/fc6389268a746fbcafd29a350a881e7a474ce26251b8dbcc333ab6be6fa3fedc.jpg)  
Fig.1.1.Combinations with nonzero product

and we observe that each factor of the type $b _ { j }$ interrupts the summation,so that the terms decompose into factors of elementary weights of the individual methods as follows:

$$
\begin{array} { r l } & { \widehat { \phi } ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) = \phi ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) + \phi ^ { * } ( \bullet ) \cdot \phi ( \bullet ) \phi ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) + \phi ^ { * } ( \overset { \prime } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) \cdot \phi ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) + \phi ^ { * } ( \overset { \prime } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) \cdot \phi ( \bullet ) \phi ( \bullet ) } \\ & { \qquad + \phi ^ { * } ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) \cdot \phi ( \bullet ) + \phi ^ { * } ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) \cdot \phi ( \bullet ) + \phi ^ { * } ( \overset { * } { \underset { \mathbf { \theta } } { \big \Updownarrow } } ) . } \end{array}
$$

The trees composed of the“star”nodes of $\tau$ in Fig.1.1 constitute all possible“subtrees” $\theta$ (from the empty tree to $\tau$ itself) having the samerootas $\tau$ Thisisthekey forunderstanding the general result.

Ordered Trees.Inorder to formalize theprocedureofFig.1.1,we introduce the set $O T$ ofordered trees recursively as follows: $\bullet \in O T$ and

if $\omega _ { 1 } , \ldots , \omega _ { m } \in O T$ ,then also the ordered $_ { m }$ -tuple $( \omega _ { 1 } , \ldots , \omega _ { m } ) \in O T .$

Asthe name suggests,in the graphical representation of an ordered tree the order of thebranches leaving cannot be permuted.Neglecting the ordering,atree $\tau \in { \mathcal { I } }$ can beconsidered as an equivalence class of ordered trees,denoted $\tau = \omega$ .

Forexample,the treeof Fig.1.1 hastwo orderings,namely $\grave { \updownarrow }$ and $\ell$ We denote by $\nu ( \tau )$ the number of possible orderings of the tree $^ \mathrm { ~ \textit ~ { ~ T ~ } ~ } { } _ { \mathrm { ~ \scriptsize ~ . ~ } }$ It is given by $\nu ( \bullet ) =$ 1and

$$
\nu ( \tau ) = \frac { m ! } { \mu _ { 1 } ! \mu _ { 2 } ! \dots . } \nu ( \tau _ { 1 } ) \cdot \dots \cdot \nu ( \tau _ { m } )
$$

for $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ]$ where the integers $\mu _ { 1 } , \mu _ { 2 } , \ldots$ are the numbers of equal trees among $\tau _ { 1 } , \dots , \tau _ { m } .$ This number is closely related tothesymmetrycoefficient $\sigma ( \tau )$ , because the product $\kappa ( \tau ) = \sigma ( \tau ) \nu ( \tau )$ satisfies the recurrence relation

$$
\kappa ( \tau ) = m ! \kappa ( \tau _ { 1 } ) \cdot \ldots \cdot \kappa ( \tau _ { m } ) .
$$

We introduce the set $O S T ( \omega )$ of ordered subtrees ofan orderedtree $\omega \in O I$ by

$$
\begin{array} { r l r } { O S T ( \bullet ) } & { = } & { \{ 0 , \bullet \} } \\ { O S T ( \omega ) } & { = } & { \{ \emptyset \} \cup \{ ( \theta _ { 1 } , \ldots , \theta _ { m } ) ; \theta _ { i } \in O S T ( \omega _ { i } ) \} \quad \mathrm { f o r ~ } \omega = ( \omega _ { 1 } , \ldots , \omega _ { m } ) . } \end{array}
$$

Each ordered subtree $\theta \in O S T ( \omega )$ is naturally associated with a tree $\theta \in T$ obtained byneglecting the ordering and the $\varnothing$ -components of $\theta$ Foreverytree $\tau \in T$ we choose,once and forall,anordering.Wedenote this ordered tree by $\omega ( \tau )$ ,andwe put $O S T ( \tau ) = O S T ( \omega ( \tau ) )$ .

Forthe treeof Fig.1.1,considered asan ordered tree,the ordered subtrees correspond to the trees composed of the“star"nodes.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/7dfcda78acd2cb331542c54513d8e260e8c4948ad76a834a70f2bccb57ff53b6.jpg)

TheGeneral Rule. The general composition rule now becomes visible:for $\theta \in O S T ( \omega )$ wedenote by $\omega \backslash \theta$ the"forest"collecting the trees left over when $\theta$ has been removed from the ordered tree $\omega$ .For brevity we set $\tau \backslash \theta : = \omega ( \tau ) \backslash \theta$ . With the conventions $\phi ^ { * } ( \theta ) = \phi ^ { * } ( \theta )$ and $\phi ^ { * } ( \emptyset ) = 1$ we then have

$$
\widehat { \phi } ( \tau ) = \sum _ { \theta \in O S T ( \tau ) } \left( \phi ^ { * } ( \theta ) \cdot \prod _ { \delta \in \tau \setminus \theta } \phi ( \delta ) \right) .
$$

This composition formula for the treesup to order 3reads:

$$
\begin{array} { r l } & { \widehat { \phi } ( \bullet ) = \phi ^ { \ast } ( \emptyset ) \cdot \phi ( \bullet ) + \phi ^ { \ast } ( \bullet ) } \\ & { \widehat { \phi } ( \pmb { \mathscr { J } } ) = \phi ^ { \ast } ( \emptyset ) \cdot \phi ( \pmb { \mathscr { J } } ) + \phi ^ { \ast } ( \bullet ) \cdot \phi ( \bullet ) + \phi ^ { \ast } ( \pmb { \mathscr { J } } ) } \\ & { \widehat { \phi } ( \pmb { \mathscr { V } } ) = \phi ^ { \ast } ( \emptyset ) \cdot \phi ( \pmb { \mathscr { V } } ) + \phi ^ { \ast } ( \bullet ) \cdot \phi ( \bullet ) ^ { 2 } + 2 \phi ^ { \ast } ( \pmb { \mathscr { J } } ) \cdot \phi ( \bullet ) + \phi ^ { \ast } ( \pmb { \mathscr { V } } ) } \\ & { \widehat { \phi } ( \pmb { \mathscr { J } } ) = \phi ^ { \ast } ( \emptyset ) \cdot \phi ( \pmb { \mathscr { J } } ) + \phi ^ { \ast } ( \bullet ) \cdot \phi ( \pmb { \mathscr { J } } ) + \phi ^ { \ast } ( \pmb { \mathscr { J } } ) \cdot \phi ( \bullet ) + \phi ^ { \ast } ( \pmb { \mathscr { J } } ) } \end{array}
$$

Thetree $\tau = \mathbb { V }$ hasthe subtrees displayed inFig.1.2.Itcontainssymmetries in that thethird and fourth subtrees are topologically equivalent.This explains the factor2 inthe expression for the elementary weight.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/5b1e38a91815937cc4011b73931e9327d154871ee402ed01534e35a4f7cfc34c.jpg)  
Fig.1.2.A tree with symmetry

# III.1.4 Composition of B-Series

Wenow extend the above composition law to general B-series,i.e.,we insert the B-series themselves into each other,as sketched in Fig.1.3.Thisallowsus to generalizeLemma 1.9(because $h f ( y )$ isaspecial B-series).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/cd7effffd25b15f5db2c2ae7399c3f02f10d85f2498c110a456e743c2b80688f.jpg)  
Fig.1.3.Composition of B-series

We start with anobservation ofMurua (see,e.g.,Murua& Sanz-Serna(1999), p.1083),namely that theproof ofLemma1.9remainsthesame if the function $h f ( y )$ isreplacedwith any other function $h g ( y )$ ;inthiscase（1.21）isreplacedwith

$$
\begin{array} { c } { { \displaystyle h g \big ( B ( a , y ) \big ) = h g + h ^ { 2 } a ( \bullet ) g ^ { \prime } f + h ^ { 3 } a ( \underline { { { f } } } ^ { \prime } ) g ^ { \prime } f ^ { \prime } f + \displaystyle \frac { h ^ { 3 } } { 2 ! } a ( \bullet ) ^ { 2 } g ^ { \prime \prime } ( f , f ) } } \\ { { + h ^ { 4 } a ( \bullet ) a ( \underline { { { f } } } ) g ^ { \prime \prime } ( f ^ { \prime } f , f ) + \ldots . } } \end{array}
$$

Such series will reappear in Sect.I.3.1below.Extending thisidea furtherto,say $f ^ { \prime \prime } ( y ) ( v _ { 1 } , v _ { 2 } )$ ,where $\boldsymbol { v } _ { 1 } , \boldsymbol { v } _ { 2 }$ are two fixed vectors,we obtain

$$
\begin{array} { r l r } { h f ^ { \prime \prime } \big ( B ( a , y ) \big ) ( v _ { 1 } , v _ { 2 } ) } & { = } & { h f ^ { \prime \prime } ( v _ { 1 } , v _ { 2 } ) + h ^ { 2 } a ( \bullet ) f ^ { \prime \prime \prime } ( v _ { 1 } , v _ { 2 } , f ) \quad \quad ( 1 } \\ & { + } & { h ^ { 3 } a ( \underline { { I } } ) f ^ { \prime \prime \prime } ( v _ { 1 } , v _ { 2 } , f ^ { \prime } f ) + \frac { 1 } { 2 ! } h ^ { 3 } a ( \bullet ) ^ { 2 } f ^ { \prime \prime \prime \prime } ( v _ { 1 } , v _ { 2 } , f , } \\ & { + } & { h ^ { 4 } a ( \bullet ) a ( \underline { { I } } ) f ^ { \prime \prime \prime \prime } ( v _ { 1 } , v _ { 2 } , f ^ { \prime } f , f ) + . . . . . } \end{array}
$$

Thisidea will lead toadirect proof of the following theoremof Hairer&Wanner (1974).

Theorem 1.10. Let $a : T \cup \{ \varnothing \} \longrightarrow \mathbb { R }$ beamapping satisfying $a ( \emptyset ) = 1$ andlet $b : T \cup \{ \varnothing \} \to \mathbb { R }$ bearbitrary. Then the $B$ -series $B ( \boldsymbol { a } , \boldsymbol { y } )$ insertedinto $B ( \boldsymbol { b } , \cdot )$ is again a $B$ -series

$$
B \Big ( b , B ( a , y ) \Big ) = B ( a b , y ) ,
$$

where the group operation $a b ( \tau )$ is as in (1.34), i.e.,

$$
a b ( \tau ) = \sum _ { \theta \in O S T ( \tau ) } b ( \theta ) \cdot a ( \tau \setminus \theta ) \qquad w i t h \qquad a ( \tau \setminus \theta ) = \prod _ { \delta \in \tau \setminus \theta } a ( \delta ) .
$$

Proof.(a) In part (c) below we prove by induction on $\left| \vartheta \right|$ , $\vartheta \in T$ that

$$
\frac { h ^ { | \vartheta | } } { \sigma ( \vartheta ) } F ( \vartheta ) \Big ( B ( a , y ) \Big ) = \sum _ { ( \tau , \theta ) \in A ( \vartheta ) } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } a ( \tau \setminus \theta ) F ( \tau ) ( y ) ,
$$

where

$$
A ( \vartheta ) = \big \{ ( \tau , \theta ) ; \tau \in T , \theta \in O S T ( \tau ) , \overline { { \theta } } = \vartheta \big \} .
$$

Multiplying（1.39）by $b ( \vartheta )$ and summing over all $\vartheta \in \mathcal I$ yields the statement（1.37） (1.38）,because

$$
\sum _ { \vartheta \in T } \sum _ { ( \tau , \theta ) \in A ( \vartheta ) } \cdot / : = \sum _ { \tau \in T } \sum _ { \theta \in O S T ( \tau ) } \cdot / \cdot .
$$

(b)Choosing a different orderingof $\tau$ in the definition of $O S T ( \tau )$ yieldsthe same sum in(1.39).Therefore(1.39) isequivalent to

$$
\frac { h ^ { | \vartheta | } } { \sigma ( \vartheta ) } F ( \vartheta ) \Big ( B ( a , y ) \Big ) = \sum _ { ( \omega , \theta ) \in \varOmega ( \vartheta ) } \frac { h ^ { | \omega | } } { \sigma ( \omega ) \nu ( \omega ) } a ( \omega \setminus \theta ) F ( \omega ) ( y ) ,
$$

where

$$
\begin{array} { r } { \Omega ( \vartheta ) = \big \{ ( \omega , \theta ) ; \omega \in O T , \theta \in O S T ( \omega ) , \overline { { \theta } } = \vartheta \big \} , } \end{array}
$$

and $\nu ( \tau )$ is the number of orderings of the tree $\tau$ ,see（1.31）.Functions defined on treesarenaturally extendedto ordered trees.In(1.4O)weuse $| \omega | = | \tau |$ , $\sigma ( \omega ) =$ $\sigma ( \tau )$ , $\nu ( \omega ) = \nu ( \tau )$ , $a ( \omega \setminus \theta ) = a ( \tau \setminus \theta )$ ,and $F ( \omega ) ( y ) = F ( \tau ) ( y )$ for $\overline { { \omega } } = \tau$ ,

(c）For $\vartheta = \circ$ and $\omega = ( \omega _ { 1 } , \ldots , \omega _ { m } )$ wehave $\begin{array} { r } { a ( \omega \setminus \theta ) = a ( \omega _ { 1 } ) \cdot \ldots \cdot a ( \omega _ { m } ) } \end{array}$ if $\bar { \theta } = \bullet$ Since we have a one-to-one correspondence $( \omega , \theta )  \omega$ between $\varOmega ( \bullet )$ and $O T$ ,and since the expressionin the sum of(1.4O)is independent of the ordering of $\boldsymbol { \omega }$ ,formula(1.40)ispreciselyLemma1.9.

To prove(1.40) forageneral tree $\boldsymbol { \vartheta } = [ \vartheta _ { 1 } , \ldots , \vartheta _ { l } ]$ ,weapply the idea put forward in(1.36)to $h f ^ { ( l ) } \left( B ( a , y ) \right) ( v _ { 1 } , \ldots , v _ { l } )$ with fixed $v _ { 1 } , \ldots , v _ { l }$ ,and obtain as in theproof ofLemma 1.9

$$
k _ { l } f ^ { ( l ) } \bigl ( B ( a , y ) \bigr ) ( v _ { 1 } , \ldots , v _ { l } ) = \sum _ { m \ge 0 } \frac { 1 } { m ! } \sum _ { \tau _ { l + 1 } \in T } \cdots \sum _ { \tau _ { l + m } \in T } \frac { h ^ { | \tau _ { l + 1 } | + \ldots + | \tau _ { l + m } | + 1 } } { \sigma ( \tau _ { l + 1 } ) \cdot \ldots \cdot \sigma ( \tau _ { l + m } ) }
$$

$$
\cdot a ( \tau _ { l + 1 } ) \cdot \cdot \cdot \cdot a ( \tau _ { l + m } ) \cdot f ^ { ( l + m ) } ( y ) \Bigl ( v _ { 1 0 } ^ { - } , \ldots , v _ { l } , F ( \tau _ { l + 1 } ) ( y ) , \ldots , F ( \tau _ { l + m } ) ( y ) \Bigr )
$$

Changingthe sums over trees to sums over ordered treeswe obtain

$$
h f ^ { ( l ) } \big ( B ( a , y ) \big ) ( v _ { 1 } , \ldots , v _ { l } ) = \sum _ { m \ge 0 } \frac { 1 } { m ! } \sum _ { \omega _ { l + 1 } \in O T } \cdots \sum _ { \omega _ { l + m } \in O T } \frac { h ^ { | \omega _ { l + 1 } | + \ldots + | \omega _ { l + m } | + \ldots } } { \kappa ( \omega _ { l + 1 } ) \cdot \ldots \cdot \kappa ( \omega _ { l + m } | + \ldots , \omega _ { l } ) }
$$

$$
a ( \omega _ { l + 1 } ) \cdot \ldots \cdot a ( \omega _ { l + m } ) \cdot f ^ { ( l + m ) } ( y ) \left( { \bar { v } } _ { 1 } , \ldots , { \bar { v } } _ { l } , F ( \omega _ { l + 1 } ) ( y ) , \ldots , F ( \omega _ { l + m } ) ( y ) \right)
$$

We insert $\begin{array} { r } { v _ { j } = \frac { h ^ { \vert \boldsymbol { v } _ { j } \vert } } { \sigma ( \boldsymbol { \vartheta } _ { j } ) } F ( \boldsymbol { \vartheta } _ { j } ) \big ( B ( \boldsymbol { a } , \boldsymbol { y } ) \big ) } \end{array}$ intothisrelatol hypothesis

$$
v _ { j } = \frac { h ^ { | \vartheta _ { j } | } } { \sigma ( \vartheta _ { j } ) } F ( \vartheta _ { j } ) \Big ( B ( a , y ) \Big ) = \sum _ { ( \omega _ { j } , \theta _ { j } ) \in \varOmega ( \vartheta _ { j } ) } \frac { h ^ { | \omega _ { j } | } } { \kappa ( \omega _ { j } ) } a ( \omega _ { j } \setminus \theta _ { j } ) F ( \omega _ { j } ) ( y ) .
$$

We then use therecursive definitions of $\sigma ( \vartheta )$ and $F ( \vartheta ) ( y )$ on the left-hand side.On the right-hand side we use the multilinearity of $f ^ { ( l + m ) }$ ,therecursive definitions of 1w1, $\kappa ( \omega )$ , $F ( \omega ) ( y )$ for $\omega = ( \omega _ { 1 } , \ldots , \omega _ { l + m } )$ ,and the facts that

$$
a ( \omega \backslash \theta ) = a ( \omega _ { 1 } \backslash \theta _ { 1 } ) \cdot \ldots \cdot a ( \omega _ { l } \backslash \theta _ { l } ) \cdot a ( \omega _ { l + 1 } ) \cdot \ldots \cdot a ( \omega _ { l + m } )
$$

and

$$
\sum _ { \substack { i _ { 1 } , \theta _ { 1 } ) \in \Omega ( \vartheta _ { 1 } ) \ ( \omega _ { l } , \theta _ { l } ) \in \Omega ( \vartheta _ { l } ) \quad \omega _ { l + 1 } \in O T \quad \omega _ { l + m } \in O T } } \cdot \Big | \cdot = \frac { m ! \mu _ { 1 } ! \mu _ { 2 } ! \cdot \cdot \cdot \cdot } { ( l + m ) ! \quad ( \omega , \theta ) \in \Omega _ { l + m } ( \vartheta ) } \cdot \Big | ^ { \prime }
$$

where $\mu _ { 1 } , \mu _ { 2 } , \ldots$ count equal trees among $\mathcal { V } _ { 1 } , \ldots , \mathcal { V } _ { l }$ ,and $\Omega _ { l + m } ( \vartheta )$ consists of thosepairs $( \omega , \theta ) \in \Omega ( \vartheta )$ forwhich $\boldsymbol { \omega }$ isof the form $\omega = ( \omega _ { 1 } , \ldots , \omega _ { l + m } ) .$ The factorialsappear,because to every $( l + m )$ -tupleof the left-hand sumcorrespond $\begin{array}{c} \binom { 1 + m } { m , \mu _ { 1 } , \mu _ { 2 } , . . . } \end{array}$ elements in $\Omega _ { l + m } ( \boldsymbol { \vartheta } )$ ,obtained by permutingthe order.Thisyields formula(1.40)and hence（1.39). □

Example1.11.The composition laws for the trees of order $\leq 4$ are

$$
\begin{array} { r l } & { \quad \alpha ( k ^ { * } + 1 ) - B ( \emptyset ) \cdot \alpha ( * ) + b ( * ) } \\ & { \quad + b ( k ^ { * } ) - ( k ( \emptyset ) ) - ( a ( k ^ { * } ) - a ( k ^ { * } ) + b ( k ^ { * } ) + b ( k ^ { * } ) } \\ & { \quad \alpha b ( k ^ { * } ) - b ( \emptyset ) \cdot \alpha ( * ) \big \} + b ( * ) \cdot \alpha ( * ) + 2 \beta ( k ^ { * } ) \cdot a ( * ) + b ( k ^ { * } ) } \\ & { \quad \alpha b ( k ^ { * } ) - b ( \emptyset ) \cdot \alpha ( k ^ { * } ) + b ( k ^ { * } ) \cdot \alpha ( * ) \big \} + b ( k ^ { * } ) \cdot a ( * ) + b ( k ^ { * } ) } \\ & { \quad \alpha b ( k ^ { * } ) - b ( \emptyset ) \cdot \alpha ( * ) \big \langle \Phi ( * ) \cdot \Phi ( * ) \cdot \Phi ( * ) \big \rangle } \\ & { \quad \quad + b ( k ^ { * } ) \big \langle \Phi ( * ) \cdot \Phi ( * ) \big \rangle + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + 3 \beta ( k ^ { * } ) \cdot \alpha ( * ) ^ { 2 } + 3 \beta ( k ^ { * } ) \cdot \alpha ( * ) } \\ & { \quad \quad \quad + b ( k ^ { * } ) } \\ & { \quad \alpha b ( k ^ { * } ) - ( k ( \Psi ) ) + b ( k ^ { * } ) - ( a ( k ^ { * } ) ) \cdot \alpha ( * ) \beta ( k ^ { * } ) + b ( \tilde { k } ) \cdot \alpha ( * ) ^ { 2 } } \\ & { \quad \quad \quad + b ( k ^ { * } ) \big \rangle _ { 1 } \cdot a ( * ) + b ( k ^ { * } ) \cdot \alpha ( * ) } \\ & { \quad \quad \quad + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + b ( k ^ { * } ) \cdot \alpha ( k ) + b ( k ^ { * } ) } \\ & { \quad \quad \quad + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + 2 b ( k ^ { * } ) \cdot \alpha ( * ) } \\ & { \quad \quad \quad + b ( k ^ { * } ) } \\ & { \quad \quad \quad + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + b ( k ^ { * } ) \cdot \alpha ( k ^ { * } ) + b ( k ^ { * } ) } \\ &  \quad \quad \quad + b ( k ^ { * } ) \cdot \alpha \end{array}
$$

Remark 1.12.The composition law(1.38）canalternatively beobtained from the corresponding formula(1.34) for Runge-Kutta methodsbyusing the fact that Bserieswhich representRunge-Kutta methodsare“dense"inthe space of all B-series (see Theorem 306A of Butcher 1987).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/b89dac3d6cf7756c2a8d87cce63707b1e215040fe533f270fed3e8dae764e991.jpg)  
III.1.5 The Butcher Group   
John C.Butcher, born:31March1933inAuckland (New Zealand)

The composition law(1.38)can be turned into agroup operation,by introducinga unit element

$$
e ( \varnothing ) = 1 , \quad e ( \tau ) = 0 \quad \mathrm { f o r } \tau \in T ,
$$

andby computing the inverse element ofa given $a$ Thisis obtained recursivelyfrom thetableof Example1.11,byrequiring $a a ^ { - 1 } ( \tau ) = 0$ andby inserting thepreviously known values of $a ^ { - 1 } ( \vartheta )$ This gives for the first orders

$$
\begin{array} { l } { { a ^ { - 1 } ( \bullet ) = - a ( \bullet ) } } \\ { { a ^ { - 1 } ( { \pmb \bigwedge } ) = - a ( { \pmb \bigwedge } ) + a ( \bullet ) ^ { 2 } } } \\ { { a ^ { - 1 } ( { \pmb \bigvee } ) = - a ( { \pmb \bigvee } ) + 2 a ( { \pmb \bigwedge } ) a ( \bullet ) - a ( \bullet ) ^ { 3 } } } \\ { { a ^ { - 1 } ( { \pmb \bigwedge } ) = - a ( { \pmb \bigwedge } ) + 2 a ( { \pmb \bigwedge } ) a ( \bullet ) - a ( \bullet ) ^ { 3 } } } \end{array}
$$

Wecan distinguish several realizations of this group:

$G _ { \mathrm { R K } }$ the set of Runge-Kutta schemes with composition (1.28);

$G _ { \mathrm { E W } }$ the set of elementary weights of Runge-Kutta schemes with the composition law (1.34)；

$G _ { \mathrm { T M } }$ the set of tree mappings $a : T \cup \{ \varnothing \} \  \ \mathbb { R }$ satisfying $a ( \emptyset ) = 1$ with composition(1.38)；

$G _ { \mathrm { B S } }$ theset of B-series(1.23)satisfying $a ( \emptyset ) = 1$ with composition (1.37).

A technical difficulty concerns the group $G _ { \mathrm { R K } }$ ,where“reducible”schemes must be identified(by deleting unnecessary stages or by combining stages that give identical results)to the same“irreducible"method(seeButcher(1972),or Butcher&Wanner (1996),p.140).The definition of $\phi ( \tau )$ in Theorem 1.4 describes a group isomorphism from $G _ { \mathrm { R K } }$ to $G _ { \mathrm { E W } }$ ,further, $G _ { \mathrm { E W } }$ isa subgroup of $G _ { \mathrm { T M } }$ and Theorem1.10 shows that formula（1.23)constitutesa group homomorphism from $G _ { \mathrm { T M } }$ to $G _ { \mathrm { B S } }$ Because the elementarydifferentialsare independent (see,e.g.,Hairer,Ngrsett& Wanner(1993),Exercise4of Sect.II.2),the last two groups are isomorphic.The group $G _ { \mathrm { R K } }$ canalso be extended byallowing"continuous”Runge-Kutta schemes with“infinitelymany stages”(seeButcher(1972),or Butcher&Wanner(1996), p.141).The term“Butcher group”was introduced by Hairer&Wanner(1974).

Thispaper tells the story ofa mathematical object thatwas created by JohnButcherin 1972 and wasrediscovered by Alain Connes,Henri Moscovici and Dirk Kreimer in 1998. (Ch.Brouder 2004)

Connection with HopfAlgebras and Quantum Field Theory.A surprising connection between Runge-Kutta theory and renormalization in quantum field theory hasbeendiscoveredbyBrouder(2Ooo).Onedenotesbya Hopfalgebraa graded algebra which,besides the usual product,also possessesa coproduct,a tool used by H.Hopf(1941）²in his topological classification of certainmanifolds.Hopf algebras generated by families of rooted trees proved to be extremely useful forsimplifying theintricate combinatorics of renormalization(Kreimer 1998).Kreimer'sHopf algebra $\mathcal { H }$ isthespace generated by linear combinations of families of rooted trees and thecoproduct is amapping $\triangle : \mathcal { H }  \mathcal { H } \otimes \mathcal { H }$ whichis,for the first trees,given bv

$$
\begin{array} { r l } & { \Delta ( \bullet ) = \bullet \otimes 1 + 1 \otimes \bullet } \\ & { \Delta ( \pmb { \mathring { I } } ) = \pmb { \mathring { I } } \otimes 1 + \bullet \otimes \bullet + 1 \otimes \pmb { \mathring { I } } } \\ & { \Delta ( \pmb { \mathring { V } } ) = \pmb { \mathring { V } } \otimes 1 + \bullet \bullet \otimes \bullet + 2 \bullet \otimes \pmb { \mathring { I } } + 1 \otimes \pmb { \mathring { V } } } \\ & { \Delta ( \pmb { \mathring { I } } ) = \pmb { \mathring { I } } \otimes 1 + \pmb { \mathring { I } } \otimes \bullet + \bullet \otimes \pmb { \mathring { I } } + 1 \otimes \pmb { \mathring { I } } } \end{array}
$$

Itcan be clearly seen,that thisalgebraic structureis precisely the one underlying thecomposition law of Example1.11,so that the Butcher group $G _ { \mathrm { T M } }$ becomes the correspondingcharacter group.The so-called antipodes of trees $\tau \in \mathcal { H }$ ,denotedby $S ( \tau )$ ,are for the first trees

$$
\begin{array} { l } { { S ( \bullet ) = - } } \\ { { S ( \underline { { { \bar { f } } } } ) = - \underline { { { \bar { f } } } } + \bullet \bullet } } \\ { { S ( \underline { { { \mathsf { V } } } } ) = - \underline { { { \mathsf { V } } } } + 2 \underline { { { \bar { f } } } } \bullet \quad \ldots } } \\ { { S ( \underline { { { \bar { f } } } } ) = - \Big \} + 2 \underline { { { \bar { f } } } } \bullet \quad \ldots } } \end{array}
$$

and,apparently,describestheinverseelement(1.42)intheButchergroup.

# III.2 Order Conditions for Partitioned Runge-Kutta Methods

Wenow apply the ideas of the previous section to the creation of the order conditions forpartitioned Runge-Kutta methods(II.2.2) of Sect.II.2.These results can then also be applied toNystrom methods.

# III.2.1 Bi-Coloured Trees and P-Series

Let us consider a partitioned system

$$
\begin{array} { r } { \dot { y } = f ( y , z ) , \qquad \dot { z } = g ( y , z ) } \end{array}
$$

(non-autonomous problems can be brought into this form by appending $t = 1$ ). Westart bycomputing the derivatives of its exact solution,which are to beinserted into the Taylor series expansion.Byanalogywith(1.4）we obtain in this case the derivatives of $_ y$ at $t _ { 0 }$ asfollows:

$$
\begin{array} { r l } & { \quad \dot { y } = f } \\ & { \quad \ddot { y } = f _ { y } f + f _ { z } g } \\ & { \quad \dot { y } ^ { ( 3 ) } = f _ { y y } ( f , f ) + 2 f _ { y z } ( f , g ) + f _ { z z } ( g , g ) + f _ { y } f _ { y } f + f _ { y } f _ { z } g + f _ { z } g _ { y } f + f _ { z } } \end{array}
$$

Here, $f _ { y } , f _ { z } , f _ { y z } , \ldots$ denotepartial derivativesandall termsare to be evaluated at $( y _ { 0 } , z _ { 0 } )$ Similar expressionsare obtained for thederivatives of $z ( t )$

The terms occurring in these expressions are again called theelementary differentials $F ( \tau ) ( y , z )$ Fortheir graphical representation asa tre $\tau$ ,wedistinguish between“black”vertices forrepresenting an $f$ and“white” vertices for a $g$ .Upwards pointing branches represent partial derivatives,with respect to $y$ if the branch leads toa black vertex,and with respect to $z$ if it leads to a white vertex.With thisconvention,the graph totheright corresponds to the expression $f _ { z y } \left( g _ { y z } ( f , g ) , f \right)$ (see Table2.1 for more examples).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/666b58f647b9a64ab7fe013293eb0b8eee59bbb4e1d02a51cbea2b9835caf1df.jpg)

Wedenote by $T P$ the set of graphs obtained by the above procedure,and we call them (rooted) bi-coloured trees.The first graphsare·ando.Byanalogywith Definition 1.1,we denote by

Table2.1.Bi-coloured trees,elementarydifferentials,andcoefficients   

<table><tr><td rowspan=1 colspan=1>|</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>a（t）</td><td rowspan=1 colspan=1>F(T）</td><td rowspan=1 colspan=1>(（）</td><td rowspan=1 colspan=1>（）</td><td rowspan=1 colspan=1>（)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>f</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Ωbi</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>[]y[o]u</td><td rowspan=1 colspan=1>！！</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>Juffg</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>∑ibiaij£ibaij</td><td rowspan=1 colspan=1>11</td></tr><tr><td rowspan=2 colspan=1>3333333</td><td rowspan=2 colspan=1>[，·lu[,olu[，olu[·lulu[oluly[·12lu[0]2lu</td><td rowspan=2 colspan=1>YY838</td><td rowspan=2 colspan=1>1211111</td><td rowspan=2 colspan=1>fy(f，f)fy2（f,g）f22（g,g）fufyffufzgfgyffgzg</td><td rowspan=1 colspan=1>33</td><td rowspan=2 colspan=1>∑ijaijaik∑ijkbiaijaik∑ikbiaijaik∑ijkbiaijajk∑ijkbiaijajk∑ijkbiaijajkEijkbiaijajk</td><td rowspan=2 colspan=1>2121111</td></tr><tr><td rowspan=1 colspan=1>36666</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>。</td><td rowspan=1 colspan=1>。</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>g</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>[]2etc</td><td rowspan=1 colspan=1>！etc</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>gufetc</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>∑iyhaietc</td><td rowspan=1 colspan=1>1</td></tr></table>

$$
[ \tau _ { 1 } , \ldots , \tau _ { m } ] _ { y } \qquad \mathrm { a n d } \qquad [ \tau _ { 1 } , \ldots , \tau _ { m } ] _ { z ; \cdot } \qquad \tau _ { 1 } , \ldots , \tau _ { m } \in T P
$$

the bi-coloured trees obtained by connecting the roots of $\tau _ { 1 } , \ldots , \tau _ { m }$ toanew root, which is $^ { \circ }$ in the first case,and $^ \circ$ in the second.Furthermore,we denote by $T P _ { y }$ and $T P z$ the subsets of $_ { T P }$ which are formed by treeswith black and white roots, respectively.Hence,the trees of $T { \mathcal { P } } _ { y }$ correspond to derivatives of $y ( t )$ ,whereas those of ${ \it T P } _ { z }$ correspond to derivatives of $z ( t )$

Asin Definition 1.2 we denote the number of vertices of $\tau \in \textit { I P }$ by $| \tau |$ ,the orderof $\gamma$ .Thesymmetrycoefficient $\sigma ( \tau )$ isagain defined by

$$
\begin{array} { r } { \sigma ( \bullet ) = \sigma ( \circ ) = 1 , } \end{array}
$$

and,for $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] _ { y }$ or $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] _ { z }$ by

$$
\sigma ( \tau ) = \sigma ( \tau _ { 1 } ) \cdot \ldots \cdot \sigma ( \tau _ { m } ) \cdot \mu _ { 1 } ! \mu _ { 2 } ! \ldots ,
$$

where the integers $\mu _ { 1 } , \mu _ { 2 } , \ldots$ count equal trees among $\tau _ { 1 } , \ldots , \tau _ { m } \in \mathrm { ~ } T P .$ Thisis formally the same definition asin Sect.II.1.Observe,however,that $\sigma ( \tau )$ depends onthecolouring of the vertices.For example,we have $\sigma ( \mathbb { V } ) = 2$ ,but $\sigma ( \mathbb { V } ) = 1$ . Byanalogy withDefinition 1.8we have:

Definition2.1 (P-Series).Fora mapping $a : T P \cup \{ \varnothing _ { y } , \varnothing _ { z } \}  \mathbb { R }$ aseries of the form

$$
P \Big ( a , ( y , z ) \Big ) = \left( \begin{array} { l } { { a ( \emptyset _ { y } ) y + \displaystyle \sum _ { \tau \in T P _ { y } } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } a ( \tau ) F ( \tau ) ( y _ { \mathfrak { v } } z ) } } \\ { { a ( \emptyset _ { z } ) z + \displaystyle \sum _ { \tau \in T P _ { z } } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } a ( \tau ) F ( \tau ) ( y , z ) } } \end{array} \right)
$$

iscalled a $P$ -series.

Thefollowingresultscorrespond toLemma 1.9and formula(1.26).They are obtained in exactly the samemanner as the corresponding results for non-partitioned Runge-Kutta methods(Sect.III.1).We therefore omit their proofs.

Lemma 2.2.Let $\iota : T P \cup \{ \varnothing _ { y } , \varnothing _ { z } \}  \mathbb { R }$ satisfy $a ( \emptyset _ { y } ) = a ( \emptyset _ { z } ) = 1 .$ Then

$$
h \left( { \small f \big ( } P \big ( a , ( y , z ) \big ) \big ) \right) = P \Big ( a ^ { \prime } , ( y , z ) \Big ) ,
$$

where $a ^ { \prime } ( \emptyset _ { y } ) = a ^ { \prime } ( \emptyset _ { z } ) = 0$ ， $a ^ { \prime } ( \circ ) = a ^ { \prime } ( \circ ) = 1 ,$ and

$$
a ^ { \prime } ( \tau ) = a ( \tau _ { 1 } ) \cdot \ldots \cdot a ( \tau _ { m } ) ,
$$

ifeither $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] _ { y }$ or $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ] _ { z } .$

Theorem 2.3 (P-Series of Exact Solution).The exact solution of(2.1) is a $P$ -series $( y ( t _ { 0 } + h ) , z ( t _ { 0 } + h ) ) = P \big ( \mathbf { e } , ( y _ { 0 } , z _ { 0 } ) \big )$ ,where $\mathbf { e } ( \varnothing _ { y } ) = \mathbf { e } ( \varnothing _ { z } ) = 1$ and

$$
\mathbf { e } ( \tau ) = { \frac { 1 } { \gamma ( \tau ) } } \qquad f o r a l l \quad t \in T P
$$

wherethe $\gamma ( \tau )$ have the same valuesas formono-coloured trees.

# III.2.2 Order Conditions for Partitioned Runge-Kutta Methods

Thenext result corresponds to Theorem 1.4 and isa consequence ofLemma2.2.

Theorem2.4 (P-Series of Numerical Solution).The numerical solution ofapartitionedRunge-Kuttamethod(Il.2.2)isa $P$ -series $( y _ { 1 } , z _ { 1 } ) = P ( \phi , ( y _ { 0 } , z _ { 0 } ) )$ ,where $\phi ( \emptyset _ { y } ) = \phi ( \emptyset _ { z } ) = 1$ and

$$
\phi ( \tau ) = \left\{ \begin{array} { l l } { \sum _ { i = 1 } ^ { s } b _ { i } \phi _ { i } ( \tau ) } & { \quad f o r \quad \tau \in T P _ { y } } \\ { \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } \phi _ { i } ( \tau ) } & { \quad f o r \quad \tau \in T P _ { z } . } \end{array} \right.
$$

Theexpression $\phi _ { i } ( \tau )$ isdefined by $\phi _ { i } ( \bullet ) = \phi _ { i } ( \circ ) = 1$ and by

$$
\phi _ { i } ( \tau ) = \psi _ { i } ( \tau _ { 1 } ) \backslash { , . . . } \psi _ { i } ( \tau _ { m } ) \quad w i t h \quad \psi _ { i } ( \tau _ { k } ) = \left\{ \begin{array} { l l } { \sum _ { j k = 1 } ^ { s } a _ { i j k } \phi _ { j k } ( \tau _ { k } ) } & { i f \tau _ { k } \in \Omega _ { i } } \\ { \sum _ { j k = 1 } ^ { s } \widehat a _ { i j k } \phi _ { j k } ( \tau _ { k } ) } & { i f \tau _ { k } \in \Omega _ { i } } \end{array} \right.
$$

Proof.These formulasresult fromLemma 2.2bywriting $( h k _ { i } , h \ell _ { i } )$ from the formulas(II.2.2)asa P-series $\left( h k _ { i } , h \ell _ { i } \right) = P \left( \phi _ { i } , ( y _ { 0 } , z _ { 0 } ) \right)$ so that

$$
( h \sum _ { j } a _ { i j } k _ { j } , h \sum _ { j } \widehat { a } _ { i j } \ell _ { j } ) = P \big ( \psi _ { i } , ( y _ { 0 } , z _ { 0 } ) \big )
$$

is alsoaP-series.Observe that equation (2.6) corresponds to(1.16)(where $\mathbf { g } _ { i }$ hasto bereplaced with $\phi _ { i }$ and that formula(2.7) comprises(1.13)and(1.15),wherewe nowwrite $\psi _ { i }$ instead of $\mathbf { u } _ { i }$ . □

The expressions $\phi ( \tau )$ areshown in Table2.1 for all trees in $T P _ { y }$ upto order $| \tau | \le 3$ Asimilar tablemust be added fortrees in ${ \it T P z }$ ,where all rootsarewhite and all $b _ { i }$ are replaced with $\widehat { b _ { i } }$ The general rule is thefollowing:attach to every vertexa summation index.Then,theexpression $\phi ( \tau )$ isasum overall summation indiceswith the summand beinga product of $b _ { i }$ or $\widehat { b } _ { i }$ (depending on whether the root“ $\boldsymbol { \imath }$ is black or white)and of $a _ { j k }$ (if“ $k$ ”isblack)or $\widehat { a } _ { j k }$ (if $k$ ”iswhite),for eachvertex“ $k$ ”directlyabove" $\mathcal { I }$ ”

Theorem2.5 (OrderConditions).Apartitioned Runge-Kuttamethod(II.2.2) has order $r$ i.e., $y _ { 1 } - y ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { r + 1 } )$ , $z _ { 1 } - z ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { r + 1 } ) ,$ ifand onlyif

$$
\phi ( \tau ) = \frac { 1 } { \gamma ( \tau ) } \qquad f o r \tau \in T P _ { y } \cup T P _ { z } \mathrm { ~ } w i t h \ | \tau | \leq r .
$$

Proof.This corresponds to Theorem 1.5and is seen by comparingthe expansions ofTheorems2.4and2.3. □

Example 2.6.We see that not onlydoes every individual Runge-Kutta method have to beof order $r$ ,butalso the so-called coupling conditions between the coefficients ofboth methods must hold.The order conditionsmentioned above (see formulas (II.2.3)and(II.2.5)) correspond to thetrees $8 , 8 , 8$ and $\}$ .For the tree sketched belowwe obtain

$$
\sum _ { i , j , k , l , m , n , p , q , r } b _ { i } \widehat { a } _ { i j } \widehat { a } _ { j m } \widehat { a } _ { i n } a _ { i k } \widehat { a } _ { k l } a _ { l q } a _ { l r } a _ { k p } = \frac { 1 } { 9 \cdot 2 \cdot 5 \cdot 3 } \qquad \underbrace { \bullet } _ { m } \quad \int _ { - \infty } ^ { q } \int _ { - \infty } ^ { q } \int _ { - \infty } ^ { q } \left( \frac { \partial \ln \left( \sqrt { 3 } \cdot \widehat { a } _ { \mathrm { e } } \right) } { \partial \cdot \sqrt { 3 } \cdot \sqrt { 3 } } - \frac { \partial \ln \left( \sqrt { 3 } \cdot \widehat { a } _ { \mathrm { e } } \right) } { \partial \cdot \sqrt { 3 } \cdot \sqrt { 3 } } \right)
$$

or,by using $\textstyle \sum _ { j } a _ { i j } = c _ { i }$ and $\textstyle \sum _ { j } { \widehat { a } } _ { i j } = { \widehat { c } } _ { i }$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/55d5353137d7b62e48ce5ab6a2d7d4345aad2ff2182751b9ca6eccfc8b25bcd8.jpg)

$$
\sum _ { i , j , k , l } \bar { b } _ { i } \widehat { c } _ { i } \widehat { a } _ { i j } \widehat { c } _ { j } a _ { i k } c _ { k } \widehat { a } _ { k l } c _ { l } ^ { 2 } = \frac { 1 } { 2 7 0 } .
$$

# III.2.3 Order Conditions for Nystrom Methods

A“modern”order theory forNystrom methods (II.2.11）of Sect.II.2.3was first givenin1976byHairer&Wanner(seeSect.II.14ofHairer,Ngrsett&Wanner

1993).Later it turned out that these conditions are obtained easily byapplying the theory of partitionedRunge-Kuttamethodstothe system

$$
\dot { y } = z \qquad \dot { z } = g ( y , z ) ,
$$

which is of the form(2.1).This function has thepartial derivative $f _ { z } = I$ and all other derivatives of $f$ arezero.Asaconsequence,many elementary differentials are zero and the corresponding order conditions can be omitted.The only trees remainingare those forwhich

Example2.7.The tree sketched belowapparently satisfies condition(2.10) and the corresponding order condition becomes,by Theorem 2.4and formula(2.8),

$$
\sum _ { i , j , k , \ldots , v } b _ { i } \widehat { a } _ { i j } \widehat { a } _ { j k } a _ { k m } a _ { k n } \widehat { a } _ { k p } \widehat { a } _ { j q } a _ { q r } \widehat { a } _ { r s } a _ { j \ell } \widehat { a } _ { \ell t } a _ { t u } a _ { t v } = \frac { 1 } { 1 3 \cdot 1 2 \cdot 4 \cdot 3 \cdot 2 \cdot 4 \cdot 3 } .
$$

Due to property(2.10）,each $a _ { \imath } k$ inside the tree comes with a corresponding $\widehat { \boldsymbol { a } _ { k j } }$ ,andby(2.1O),both factorscontract toan $a _ { i j }$ ；similarly,theblack root isonlyconnected toonewhite vertex,the corresponding $b _ { i } \hat { a _ { i j } }$ simplifies to $b _ { j }$ We thus get

$$
\sum _ { j , k , q , s , t } \overline { { { b } } } _ { j } \widehat { a } _ { j k } c _ { k } ^ { 2 } \widehat { c } _ { k } \widehat { a } _ { j q } \overline { { { a } } } _ { q s } \overline { { { a } } } _ { j t } c _ { t } ^ { 2 } = \frac { 1 } { 1 3 \cdot 3 4 5 6 } .
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/2ebcd9eb8bfab3dd69bd07521ef83ee11f1bfd2ad3111ee2a794d1ebdb113380.jpg)

Each of the above order conditions for a tree in $T P _ { y }$ hasa“twin”in $T P _ { z }$ ofone orderlowerwith the root cut off.For the above example this twin becomes

$$
\sum _ { j , k , q , s , t } b _ { j } \widehat { a } _ { j k } c _ { k } ^ { 2 } \widehat { c } _ { k } \widehat { a } _ { j q } \overline { { { a } } } _ { q s } \overline { { { a } } } _ { j t } c _ { t } ^ { 2 } = \frac { 1 } { 3 4 5 6 } .
$$

Weneed only consider the trees in $T P _ { z }$ if

$$
\overline { { b } } _ { i } = b _ { i } ( 1 - c _ { i } )
$$

is satisfied(seeLemmaII.14.13ofHairer,Ngrsett&Wanner(1993),Sect.II.14).

Remark 2.8.Strictly speaking,the theory of partitioned methodsis applicable to Nystrommethods onlyif thematrix（ $\widehat { a } _ { i j }$ ）isinvertible.However,since we arriveat expansionswitha finite number of algebraic conditions,we canrecover the singular casebyacontinuousperturbation of the coefficients.

Equationswithout Friction.Although condition (2.1O) already eliminates many order conditions,Nystrom methods for the general problem $\boldsymbol { \ddot { y } } = \boldsymbol { g } ( \boldsymbol { y } , \boldsymbol { \dot { y } } )$ cannot be much better than an excellent Runge-Kutta method applied pairwise to system (2.9).

Thereis,however,an important special case where much more progress is possible, namely equationsof the type

$$
{ \ddot { y } } = g ( y ) ,
$$

which corresponds to motion without friction.In this case,the function for $\dot { z }$ in (2.9) isindependent of $z$ ,andinaddition to(2.1O)wehaveasecond condition,namely

$$
" w h i t e \ v e r t i c e s \ h a \nu e \ o n l y \ b l a c k \ s o n s " ,
$$

Both conditions reduce the remaining trees drastically.Along each branch,there occur alternating black andwhite vertices.Ramifications only happen at white vertices.This case allows the construction of excellent numerical methods of high orders.For example,the following13trees

assure order5,whereas ordinary Runge-Kutta theory requires17conditions for this order.SeeHairer,Ngrsett&Wanner(1993),pages291f,fortables,examplesand references.

# III.3 Order Conditions for Composition Methods

Wehave seen in the preceding chapter that composition methods of arbitrarily high ordercan be obtainedwith theuse of TheoremII.4.1.However,as demonstrated in Fig.II.4.4,thesemethodsare notatractive for high orders.Thissection is devoted tothe derivation of order conditions,which then allow the construction of optimal high order composition methods.

Theorderconditions for these methods are oftenderived via the Baker-Campbell-Hausdorff formula.Thiswill be thesubject of Sect.II.5below.Only very recently, Murua& Sanz-Serna(1999) have found an elegant theory based on the idea ofBseries.This paper has largely inspired the subsequent presentation.

# II1.3.1 Introduction

The principal tool in this section is the Taylor series expansion

$$
\Phi _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + h ^ { 3 } d _ { 3 } ( y ) + . . . .
$$

of the basic method.The only hypothesiswhich werequire for this method is consistency，i.e.,that

$$
d _ { 1 } ( y ) = f ( y ) .
$$

All other functions $d _ { i } ( y )$ are arbitrary.

Theunderlying idea for obtaining the expansions for composition methods is,in fact,very simple:we just insert the series(3.1）,with varyingvalues of $h$ ,into itself. All our experience from Sect.II.1.2 with theinsertion of aB-series intoa function will certainly be helpful.Wedemonstrate this for the case of the composition $\psi _ { h } =$ $\phi _ { \alpha _ { 2 } h } \circ \phi _ { \alpha _ { 1 } h } .$ Applied toan initial value $y _ { 0 }$ ,this gives with (3.1）

$$
\begin{array} { r l } & { y _ { 1 } \equiv \varPhi _ { \alpha _ { 1 } h } ( y _ { 0 } ) = y _ { 0 } + h \alpha _ { 1 } d _ { 1 } ( y _ { 0 } ) + h ^ { 2 } \alpha _ { 1 } ^ { 2 } d _ { 2 } ( y _ { 0 } ) + \dots } \\ & { y _ { 2 } = \varPhi _ { \alpha _ { 2 } h } ( y _ { 1 } ) = y _ { 1 } + h \alpha _ { 2 } d _ { 1 } ( y _ { 1 } ) + h ^ { 2 } \alpha _ { 2 } ^ { 2 } d _ { 2 } ( y _ { 1 } ) + \dots . } \end{array}
$$

Wenow insert the first series into the second,in the same wayaswe did in(1.35). Then,for example,the term $h ^ { 2 } \alpha _ { 2 } ^ { 2 } d _ { 2 } ( y _ { 1 } )$ becomes

$$
\begin{array} { l } { { y _ { 2 } = \ldots + \ } } \\ { { \displaystyle + \ h ^ { 2 } \alpha _ { 2 } ^ { 2 } d _ { 2 } ( y _ { 0 } ) + h ^ { 3 } \alpha _ { 2 } ^ { 2 } \alpha _ { 1 } d _ { 2 } ^ { \prime } ( y _ { 0 } ) d _ { 1 } ( y _ { 0 } ) } } \\ { { \displaystyle + \ } } \end{array} \qquad ( 3 \eqno { ( 3 ) }
$$

Wesee thatwearriveat“generalized"B-series,where theelementarydifferentials contain not only one function,but are composed ofinfinitely many functions and theirderivatives.We symbolize the four termswrittenin(3.4）bythe trees

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/0b0bca7c1dba691cac1ca55854fef011f26e4837c698ee3531be0da21093bb8c.jpg)

This leads us to the following definition.

Definition 3.1 $\infty$ -Trees, $\mathbf { B } _ { \infty }$ -series).WeextendDefinitions1.1and1.2 to $T _ { \infty }$ ， theset ofall rootedtreeswhere each vertexbearsa positive integerwithout any further restriction,and use the notation

①,②,③,...= the trees with one vertex;

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } _ { [ 1 , \cdots , \tau _ { m } ] _ { i } = } \mathrm { t h e ~ t r e e ~ } \tau \mathrm { ~ f o r m e d ~ b y ~ a ~ n e w ~ r o o t ~ } \ @ \mathrm { ~ c o n n e c t e d ~ t o ~ } \tau _ { 1 } , } \\ & { \mathrel { \phantom { = } } _ { F } ( \textcircledast ) ( y ) = d _ { i } ( y ) ; } \\ & { \mathrel { \phantom { = } } F ( \tau ) ( y ) = d _ { i } ^ { ( m ) } ( y ) ( F ( \tau _ { 1 } ) ( y ) , . . . , F ( \tau _ { m } ) ( y ) ) \mathrm { ~ f o r ~ } \tau \mathrm { ~ a s ~ a b o v e } ; } \\ & { \mathrel { \phantom { = } } _ { | \tau | = } 1 + | \tau _ { 1 } | + . . . + | \tau _ { m } | , \quad \mathrm { t h e ~ n u m b e r ~ o f ~ v e r t i c e s ~ o f ~ } \tau ; } \\ & { \mathrel { \phantom { = } } _ { | \tau | = } i + | | \tau _ { 1 } | | + . . . + | | \tau _ { m } | | , \quad \mathrm { t h e ~ s u m ~ o f ~ t h e ~ l a b e l s ~ o f ~ } \tau ; } \\ & { \mathrel { \phantom { = } } _ { \sigma } ( \tau ) = \mu _ { 1 } | \mu _ { 2 } | \cdot . . . \cdot \sigma ( \tau _ { 1 } ) \cdot . . . \cdot \sigma ( \tau _ { m } ) , } \end{array}
$$

Foramap $a : T _ { \infty } \cup \{ \varnothing \}  \mathbb { R }$ wewrite

$$
B _ { \infty } ( a , y ) \equiv a ( \emptyset ) y + \sum _ { \tau \in T _ { \infty } } \frac { h ^ { [ | \tau | | } } { \sigma ( \tau ) } a ( \tau ) F ( \tau ) ( y )
$$

which extends the notion of $B$ -seriestothe newsituation.

Example 3.2. For the tree

$$
\tau = \bigotimes _ { \mathcal { Y } } ^ { \bigodot \bigodot \bigodot } \bigotimes _ { \mathcal { Y } } ^ { \bigodot } \Leftrightarrow \tau = [ \tau _ { 1 } , \tau _ { 2 } ] _ { 4 } \quad \mathrm { w h e r e } \quad \tau _ { 1 } = \mathbb { O } , \tau _ { 2 } = \bigodot \bigodot _ { \mathcal { Y } } ^ { \bigodot } \bigodot
$$

wehave

$$
F ( \tau ) ( y ) = d _ { 4 } ^ { \prime \prime } ( y ) \big ( d _ { 1 } ( y ) , d _ { 7 } ^ { \prime \prime \prime } ( y ) \big ( d _ { 5 } ( y ) , d _ { 6 } ( y ) , d _ { 6 } ( y ) \big ) \big )
$$

$$
\tau = [ \mathbb { O } , [ \mathbb { O } , \mathbb { O } , \mathbb { O } ] \tau ] _ { 4 } , \quad | \tau | = 6 , ~ | | \tau | | = 2 9 , ~ \sigma ( \tau ) = 2 , ~ i ( \tau ) = 4 .
$$

Theabove calculations for(3.4)are governed by the following lemma.

Lemma3.3.Foraseries $B _ { \infty } ( a , y )$ with $a ( \emptyset ) = 1$ wehave

$$
h ^ { i } d _ { i } \Big ( B _ { \infty } ( a , y ) \Big ) = \sum _ { \tau \in T _ { \infty } , i ( \tau ) = i } \frac { h ^ { | | \tau | | } } { \sigma ( \tau ) } a ^ { \prime } ( \tau ) F ( \tau ) ( y ) ,
$$

where $a ^ { \prime } ( \textcircled { i } ) = 1$ and

$$
a ^ { \prime } ( \tau ) = a ( \tau _ { 1 } ) * \ldots * a ( \tau _ { m } ) \qquad f o r \ \tau = [ \tau _ { 1 } , \ldots , \tau _ { m } ] _ { i } ,
$$

Proof.Thisisa straightforward extension ofLemma 1.9with exactly the same proof. □

Thepreceding lemma leads directly to the order conditions for composition methods.However,ifwe continue with compositions of the type(II.4.1),we arrive at conditions without real solutions.We therefore turn to compositions including the adjoint method as well.

# III.3.2The General Case

As in (IL.4.6),we consider

$$
\varPsi _ { h } = \varPhi _ { \alpha _ { s } h } \circ \varPhi _ { \beta _ { s } h } ^ { * } \circ \phantom { \dagger } _ { \cdots } \circ \varPhi _ { \alpha _ { 2 } h } \circ \varPhi _ { \beta _ { 2 } h } ^ { * } \circ \varPhi _ { \alpha _ { 1 } h } \circ \varPhi _ { \beta _ { 1 } h } ^ { * } ,
$$

and we obtain with the help of the above lemma thecorresponding $B _ { \infty }$ -series.

Lemma 3.4 (RecurrenceRelations).The following compositionsare $B _ { \infty }$ -series

$$
\begin{array} { r l } { \left( \Phi _ { \beta _ { k } h } ^ { * } \circ \dots \circ \Phi _ { \alpha _ { 1 } h } \circ \Phi _ { \beta _ { 1 } h } ^ { * } \right) ( y ) } & { = \ B _ { \infty } ( b _ { k } , y ) } \\ { \left( \Phi _ { \alpha _ { k } h } \circ \Phi _ { \beta _ { k } h } ^ { * } \circ \dots \circ \Phi _ { \alpha _ { 1 } h } \circ \Phi _ { \beta _ { 1 } h } ^ { * } \right) ( y ) } & { = \ B _ { \infty } ( a _ { k } , y ) . } \end{array}
$$

Theircoefficientsare recursively given by $a _ { k } ( \emptyset ) = 1$ $b _ { k } ( 0 ) = 1$ ， $a _ { 0 } ( \tau ) = 0$ forall $\tau \in { \cal { I } } _ { \infty }$ and

$$
\begin{array} { r c l } { { b _ { k } ( \tau ) ~ = ~ a _ { k - 1 } ( \tau ) - ( - \beta _ { k } ) ^ { i ( \tau ) } b _ { k } ^ { \prime } ( \tau ) , } } \\ { { a _ { k } ( \tau ) ~ = ~ b _ { k } ( \tau ) + { \alpha _ { k } ^ { i ( \tau ) } } b _ { k } ^ { \prime } ( \tau ) . } } \end{array}
$$

Proof.Thecoefficients $a _ { 0 } ( \tau )$ correspond to the identity map $B _ { \infty } ( a _ { 0 } , y ) = y .$ The second formulaof(3.11) followsfrom

$$
B _ { \infty } ( a _ { k } , y ) = \varPhi _ { \alpha _ { k } h } \Bigl ( B _ { \infty } ( b _ { k } , y ) \Bigr ) = B _ { \infty } ( b _ { k } , y ) + \sum _ { i \ge 1 } \alpha _ { k } ^ { i } h ^ { i } d _ { i } \Bigl ( B _ { \infty } ( b _ { k } , y ) \Bigr ) ,
$$

and froman application of Lemma 3.3.

Therelation $B _ { \infty } ( b _ { k } , y ) ~ = ~ \varPhi _ { \beta _ { k } h } ^ { * } \left( B _ { \infty } ( a _ { k - 1 } , y ) \right)$ ,whichinvolvesthe adjoint method,needsa little trick:we write itas $B _ { \infty } ( a _ { k - 1 } , y ) = \varPhi _ { - \beta _ { k } h } \bigl ( B _ { \infty } ( b _ { k } , y ) \bigr )$ (remember that $\varPhi _ { h } ^ { * } = \varPhi _ { - h } ^ { - 1 }$ ),applyLemma3.3again,and reverse theformula.This gives the first equation of(3.11). □

Addingthe equations of (3.11),we get

$$
a _ { k } ( \tau ) = a _ { k - 1 } ( \tau ) + \bigl ( \alpha _ { k } ^ { i ( \tau ) } - ( - \beta _ { k } ) ^ { i ( \tau ) } \bigr ) b _ { k } ^ { \prime } ( \tau ) .
$$

Because of $b _ { k } ^ { \prime } ( \textcircled { i } ) = 1$ ,we obtain

$$
\begin{array} { l } { { \displaystyle a _ { k } ( \textcircled { \cdot } ) = \sum _ { \ell = 1 } ^ { k } \bigl ( \alpha _ { \ell } ^ { i } - ( - \beta _ { \ell } ) ^ { i } \bigr ) } } \\ { { \displaystyle b _ { k } ( \textcircled { \cdot } ) = \sum _ { \ell = 1 } ^ { k - 1 } \alpha _ { \ell } ^ { i } - \sum _ { \ell = 1 } ^ { k } ( - \beta _ { \ell } ) ^ { i } = \sum _ { \ell = 1 } ^ { k } \bigl ( \alpha _ { \ell } ^ { i } - ( - \beta _ { \ell } ) ^ { i } \bigr ) . } } \end{array}
$$

The fact that, for $b _ { k } ( \textcircled { i } )$ ,thesumof $( - \beta _ { \ell } ) ^ { \ i }$ isfrom $^ { 1 }$ to $k$ ,but the sum of $\alpha _ { \ell } ^ { 2 }$ is only from1 to $k - 1$ ,hasbeen indicatedbyaprimeattachedtothe summation symbol. Continuing toapply the formulas(3.11) and(3.12) to more and more complicated trees,we quicklyunderstand the general rule for the coefficients of anarbitrary tree.

Example 3.5.The tree $\gamma$ in (3.6) gives

$$
\begin{array} { l c r } { { \displaystyle { \stackrel { n } { \bigotimes } } } { \bigotimes } ^ { p } { \bigotimes } ^ { q } } & { { \displaystyle { a } } _ { s } ( \tau ) = \displaystyle { \sum _ { k = 1 } ^ { s } } ( \alpha _ { k } ^ { 4 } = \beta _ { k } ^ { 4 } ) \displaystyle { \sum _ { \ell = 1 } ^ { k } } ( \alpha _ { \ell } + \beta _ { \ell } ) }  \\ { { \displaystyle { \bigoplus _ { k } } } } & { { \qquad \cdot \sum _ { m = 1 } ^ { k } } { \big ( } \alpha _ { m } ^ { 7 } + \beta _ { m } ^ { 7 } { \big ) } \displaystyle { \sum _ { n = 1 } ^ { m } } { \big ( } \alpha _ { n } ^ { 5 } + \beta _ { n } ^ { 5 } { \big ) } { \Big ( } { \sum _ { p = 1 } ^ { m } } ^ { \prime } ( \alpha _ { p } ^ { 6 } - \beta _ { p } ^ { 6 } ) { \Big ) } ^ { 2 } . }  \end{array}
$$

The Order Conditions.The exact solution of $\dot { y } = f ( y )$ isa $B$ -series $y ( t _ { 0 } + h ) =$ $B ( \mathbf { e } , y _ { 0 } )$ (see (1.26)).Since $d _ { 1 } ( y ) = f ( y )$ ,every $B$ -seriesisalsoa $B _ { \infty }$ -serieswith $\mathbf { e } ( \tau ) = 0$ fortreeswithatleast one label different from1.Therefore,wealso have $y ( t _ { 0 } + h ) = B _ { \infty } ( \mathbf { e } , y _ { 0 } )$ ,where the coefficients ${ \bf e } ( \tau )$ satisfy ${ \bf e } ( \odot ) = 1 , { \bf e } ( \tau ) = 0$ if $i ( \tau ) > 1$ ,and

$$
\mathbf { e } ( \tau ) = \frac { 1 } { | \tau | } \mathbf { e } ( \tau _ { 1 } ) \dots . . . \mathbf { e } ( \tau _ { m } ) \qquad \mathrm { f o r } ~ \tau = [ \tau _ { 1 } , . . . , \tau _ { m } ] _ { 1 } ,
$$

Theorem3.6.Thecompositionmethod $\varPsi _ { h } ( y ) = B _ { \infty } ( a _ { s } , y )$ of(3.9)has orderpif

$$
a _ { s } ( \tau ) = \mathbf { e } ( \tau ) \qquad f o r \ \tau \in T _ { \infty } \ w i t h \ | | \tau | | \tau \leq p .
$$

Proof. This follows fromacomparison of the $B _ { \infty }$ -series forthe numerical and the exact solution.For the necessity of(3.16),the independence of the elementary differentials hasto be studied as in Exercise3. □

# III.3.3 Reduction of the Order Conditions

Theorder conditionsof the foregoing section are indeed beautiful,but for the moment they are not ofmuch use,because of theenormousnumber of trees in $x _ { \infty }$ of acertain order.For example,thereare 166 trees in $x _ { \infty }$ with $| | \tau | | \leq 6$ Fortunately, the equations are not all independent,as we shall see now.

Definition 3.7(Butcher1972,Murua&Sanz-Serna1999).Fortwo trees in $T _ { \infty }$ ， $u = [ u _ { 1 } , \dots , u _ { m } ] _ { i }$ and $v = [ v _ { 1 } , \ldots , v _ { l } ] _ { j }$ wedenote

$$
\begin{array} { r } { u \circ v : = [ u _ { 1 } , \ldots , u _ { m } , v ] _ { i } \ , \qquad u \times v : = [ u _ { 1 } , \ldots , u _ { m } , v _ { 1 } , \ldots , v _ { l } ] _ { i + j } } \end{array}
$$

andcall them the Butcher product and merging product,respectively (see Fig.3.1).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/13776d3eb9f8949a321ef8eb0aaafe406dd6a54ed9fb0c3884d9e23573ccc7df.jpg)  
Fig.3.1.The Butcher product and the merging product

Themerging product is associative and commutative,the Butcher product is neither of the two.To simplify the notation,we write products of several factors without parentheses,when we mean evaluation from left to right:

$$
\textcircled { 1 } \stackrel { \widehat { v _ { 1 } } } { \cup } \stackrel { \widehat { v _ { 2 } } } { \cup } \stackrel { \widehat { v _ { 3 } } } { \cup } \quad _ { u \textmd { o v } _ { 1 } \textmd { o v } _ { 2 } \textmd { o . c . } \textmd { o } v _ { s } } = ( ( ( u \textmd v _ { 1 } ) \textcircled { v _ { 2 } } ) \textcircled { \scriptsize { \cdot } } \hdots \big ) \textcircled { \scriptsize { v _ { s } } } .
$$

Here the factors $v _ { 1 } , \dots , v _ { s }$ can be freely permuted.

All subsequent results concern properties of $a _ { k } ( \tau )$ aswell as $b _ { k } ( \tau )$ ,valid forall $k$ Toavoid writingallformulas twice,we replace $a _ { k } ( \tau )$ and $b _ { k } ( \tau )$ everywhere by aneutral symbol $c ( \tau )$

Lemma 3.8 (Switching Lemma).All $a _ { k } , b _ { k }$ ofLemma3.4satisfyforall $u , v \in$ $L _ { \infty }$ ,therelation

$$
c ( u \circ v ) + c ( v \circ u ) = c ( u ) \cdot c ( v ) - c ( u \times v ) .
$$

Proof. Therecursion formulas (3.11)are of the form

$$
a ( \tau ) = b ( \tau ) + \alpha ^ { i ( \tau ) } b ^ { \prime } ( \tau ) .
$$

Wearrange this formula,forall fivetrees ofFig.3.1,as follows:

$$
\begin{array} { r c l c r c l } { { } } & { { a ( u \circ v ) } } & { { + } } & { { a ( v \circ u ) } } & { { \mp } } & { { a ( u \times v ) } } & { { - } } & { { a ( u ) a ( v ) } } \\ { { } } & { { = } } & { { b ( u \circ v ) } } & { { + } } & { { b ( v \circ u ) } } & { { + } } & { { b ( u \times v ) } } & { { - } } & { { b ( u ) b ( v ) } } \\ { { } } & { { + } } & { { \alpha ^ { i ( u ) } b ^ { \prime } ( u \circ v ) + \alpha ^ { i ( v ) } b ^ { \prime } ( v \circ u ) + \alpha ^ { i ( u ) + i ( v ) } b ^ { \prime } ( u \times v ) } } & { { } } & { { } } & { { } } \\ { { - } } & { { \alpha ^ { i ( u ) } b ^ { \prime } ( u ) b ( v ) - \alpha ^ { i ( v ) } b ^ { \prime } ( v ) b ( u ) - \alpha ^ { i ( u ) } \alpha ^ { i ( v ) } b ^ { \prime } ( u ) b ^ { \prime } ( v ) . } } & { { } } & { { } } & { { } } \end{array}
$$

Because of $b ^ { \prime } ( u \circ v ) = b ^ { \prime } ( u ) b ( v )$ and $b ^ { \prime } ( u \times v ) = b ^ { \prime } ( u ) b ^ { \prime } ( v )$ ,the last two rows cancel,hence

$$
a ( \tau ) \mathrm { ~ s a t i s f i e s } ( 3 . 1 9 ) \Leftrightarrow b ( \tau ) \mathrm { ~ s a t i s f i e s } ( 3 . 1 9 ) .
$$

Thus,beginning with $a _ { 0 }$ ,then $b _ { 1 }$ ,then $a _ { 1 }$ ,etc.,all $a _ { k }$ and $b _ { k }$ must satisfy (3.19).□

The SwitchingLemma 3.8 reduces considerably the number of order conditions. Since the right-hand expression involves only trees with $| \tau | < | u \circ v |$ ,andsince relation (3.19)isalso satisfied by ${ \bf e } ( \tau )$ ,aninduction argument shows that the order conditions (3.16) for the trees $u \circ v$ and $v \circ u$ areequivalent.The operation $u \circ v \mapsto$ $\upsilon \odot u$ consists simplyin switching the root from one vertex to the next.Byrepeating thisargument,we see that we can freely move theroot inside the graph,and of all these trees,only one needs to beretained.For order6,for example,thereremain 68 conditions out of the original 166.

Ournext results show howrelation(3.19)also generates aconsiderable amount ofreductions of the order conditions.These ideas(for the special situation of symplecticmethods) havealready been exploitedbyCalvo&Hairer(1995b).

Lemma 3.9.Assumethatall $b _ { k }$ ofLemma3.4 satisfyarelationoftheform

$$
\sum _ { i = 1 } ^ { N } A _ { i } \prod _ { j = 1 } ^ { m _ { i } } c ( u _ { i j } ) = 0
$$

with all $m _ { i } > 0$ .Then,forany tree $w$ ,all $a _ { k }$ and $b _ { k }$ satisfy therelation

$$
\sum _ { i = 1 } ^ { N } A _ { i } c ( w \circ u _ { i 1 } \circ u _ { i 2 } \circ . . . \circ u _ { i , m _ { i } } ) = 0 .
$$

Proof.Therelation (3.20),writenfor the tree $w \circ u _ { i 1 } \circ u _ { i 2 } \circ . . . \circ u _ { i , m _ { i } }$ is

$$
\begin{array} { r } { \begin{array} { l } { a ( w \circ u _ { i 1 } \circ \dots \circ u _ { i , m _ { i } } ) \ = \ b ( w \circ u _ { i 1 } \circ \dots \circ u _ { i , m _ { i } } ) } \\ { \ } \\ { \qquad + \ \alpha ^ { i ( w ) } b ^ { \prime } ( w ) b ( u _ { i 1 } ) \cdot \dots \cdot b ( \dot { u } _ { i , m _ { i } } ) . } \end{array} } \end{array}
$$

Multiplyingwith $A _ { i }$ and summing over $i$ ,thisshows that,under the hypothesis (3.22） for $b$ ,therelation（3.23）holds for $b$ ifandonly if itholds for $a$ .Thecoefficients $a _ { 0 } ( \tau ) = 0$ forthe identitymap satisfy(3.22)and(3.23） because $m _ { i } > 0$ .. Starting from this,we again conclude(3.23)recursively forall $a _ { k }$ and $b _ { k }$ □

Thefoilowinglemma³extendsformula(3.19)to thecase of several factors.

Lemma 3.10. For any three trees $u , v , w$ all $a _ { k } , b _ { k }$ ofLemma3.4satisfyarelation

$$
c ( u \circ v \circ w ) + c ( v \circ u \circ w ) + c ( w \circ u \circ v ) = c ( u ) \cdot c ( v ) \cdot c ( w ) + \ldots ~ ,
$$

wherethedots indicatea linearcombination ofproducts $\begin{array} { r } { \prod _ { j } c ( v _ { j } ) w i t h | v _ { 1 } | + | v _ { 2 } | + } \end{array}$ $\ldots < | u | + | v | + | w |$ and,foreach term,atleast oneof the $v _ { j }$ possesses $\alpha$ label largerthan one.Thegeneral formula,formtrees $u _ { 1 } , \ldots , u _ { m } ,$ is

$$
\sum _ { i = 1 } ^ { m } c ( u _ { i } \circ u _ { 1 } \circ _ { \cdots } \circ u _ { i - 1 } \circ u _ { i + 1 } \circ _ { \cdots } \circ u _ { m } ) = \prod _ { i = 1 } ^ { m } c ( u _ { i } ) + \dots ,
$$

Proof.We applyLemma3.9to(3.19)and obtain

$$
c ( w \circ ( u \circ v ) ) + c ( w \circ ( \bar { v } \circ u ) ) = c ( w \circ u \circ v ) - c ( w \circ ( u \times v ) ) .
$$

Next,we apply the SwitchingLemma 3.8 to the trees to the leftand get

$$
\begin{array} { r l } & { c ( w \circ ( u \circ v ) ) + c ( u \circ v \circ w ) = c ( w ) \cdot c ( u \circ v ) - c ( w \times ( u \circ v ) ) } \\ & { c ( w \circ ( v \circ u ) ) + c ( v \circ u \circ w ) = c ( w ) \cdot c ( v \circ u ) - c ( w \times ( v \circ u ) ) . } \end{array}
$$

Adding these formulas and subtracting(3.26)gives

$$
( u \circ v \circ w ) + c ( v \circ u \circ w ) + c ( w \circ u \circ v ) = c ( w ) { \big ( } c ( u \circ v ) + c ( v \circ u ) { \big ) } + \dots .
$$

which becomes (3.24) after another use of the SwitchingLemma.Thereby,everything which goes into“+..."contains somewhere a merging product,whose roots introduce necessarily labels larger than one.

Continuing like this,we get recursively (3.25) for all m.

In order that the further simplifications do not turn into chaos,we fix,once and forall,a total order relation(written $<$ ）on ${ \mathit { 1 } } _ { \infty }$ ,wherewe onlyrequire that the orderrespectsthe number of vertices,i.e.,that

$$
u < v \quad { \mathrm { w h e n e v e r } } \quad | u | < | v | .
$$

Similar to the strategy introduced byHall(195O) for simplifyingbracket expressions inLiealgebras,we define the following subset of $T _ { \infty }$

Definition 3.11 (Hall Set). The Hall set corresponding to an order relation (3.27) isasubset $\mathcal { H } \subset T _ { \infty }$ defined by

$$
\begin{array} { l l } { \textcircled { ! } \in { \mathcal { H } } } & { \mathrm { f o r } i = 1 , 2 , 3 , \ldots } \\ { \tau \in { \mathcal { H } } } & { \Leftrightarrow \quad \mathrm { t h e r e ~ e x i s t } u , v \in { \mathcal { H } } , u > v , \mathrm { s u c h ~ t h a t } \tau = u \circ v . } \end{array}
$$

Example 3.12.The treesin the subsequent tableare ordered from left to right with respect to $| \tau |$ ,and from toptobottom within fixed $| \tau |$ .Thereremain finally22 conditions for order 6.

A Hall set $\mathcal { H }$ with|||/≤6:

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/66cb0389bbeb9c1cb4bdceeedc23ea445ee763ba7b1583dad103e48064031b2e.jpg)

Not inHare,for example:

8   
8   
8

because $u = v = \textcircled { 1 }$ ； because $\overset { \textcircled { 1 } } { \boldsymbol { u } } = \overset { \textcircled { 1 } } { \boldsymbol { \psi } }$ is not in $\mathcal { H }$ ; because $u = \textcircled { 1 } < v = \frac { \textcircled { 2 } } { \textcircled { 3 } }$ because $u = \frac { \textcircled { 1 } } { 1 }$ is not in $\mathcal { H }$ ; becauseu=v=

Theorem3.13(Murua& Sanz-Serna1999).Foreach $\tau \in T _ { \infty }$ there are constants $A _ { i i }$ integers $m _ { i }$ andtrees $u _ { i j } \in \mathcal { H }$ such that for all $a _ { k } , b _ { k }$ ofLemma3.4wehave

$$
c ( \tau ) = \sum _ { i = 1 } ^ { N } A _ { i } \prod _ { j = 1 } ^ { m _ { i } } c ( u _ { i j } ) , \qquad u _ { i j } \in { \mathcal { H } } , | u _ { i 1 } | + . . . + | u _ { i , m _ { i } } | \leq | \tau | .
$$

Proof.We proceed by induction on $| \tau |$ .For $\tau = \left( i \right)$ thestatementistrivial,bece $\textcircled { i } \in \mathcal { H } .$ We thus consider $\tau \in T _ { \infty }$ with $| \tau | \geq 2$ ,writeit as $\tau = u \cup v$ ,and conclude through the following two steps.

First Step.We apply the induction hypothesis (3.28) to $\boldsymbol { v }$ ,i.e.,

$$
c ( v ) = \sum _ { i } B _ { i } \prod _ { j } c ( v _ { i j } ) , \qquad v _ { i j } \in \mathcal { H } , \quad \sum _ { j } | v _ { i j } | \leq | v | .
$$

To this,we applyLemma 3.9 followed by the SwitchingLemma3.8:

$$
\begin{array} { l } { c ( \tau ) = c ( \boldsymbol { u } \circ \boldsymbol { v } ) = \displaystyle \sum _ { i } B _ { i } c ( \boldsymbol { u } \circ v _ { i 1 } \circ v _ { i 2 } \dots \circ v _ { i , n _ { i } } ) } \\ { \qquad = \displaystyle - \sum _ { i } B _ { i } c \big ( v _ { i n _ { i } } \circ ( \boldsymbol { u } \circ v _ { i 1 } \circ \dots \circ v _ { i , n _ { i } - 1 } ) \big ) + \dots , . } \end{array}
$$

The $^ { 6 6 } + \dots$ ”indicate terms containing trees to which we can apply our induction hypothesis.Inside the above expressions,we apply the induction hypothesis to the trees $\boldsymbol { u } \circ v _ { i 1 } \circ \dots \circ v _ { i , n _ { i } - 1 }$ ,followed once again byLemma 3.9.We arrive ata huge double sum which constitutesa linear combination of expressions of the form

$$
c \big ( u _ { 1 } \circ u _ { 2 } \circ \dots \circ u _ { m } \big )
$$

and of terms“ $+ \ldots$ ”covered bythe induction hypothesis.The point of the above dodgeswastomakesure that all $u _ { 1 } , u _ { 2 } , \ldots , u _ { m }$ arein $\mathcal { H }$

Second Step.It remains to reducean expression (3.30)to the form required by (3.28).The trees $u _ { 2 } , \ldots , u _ { m }$ can bepermuted arbitrarily；we arrange them in increasing order $u _ { 2 } \leq \ldots \leq u _ { m }$ ，

Case $I .$ If $u _ { 1 } > u _ { 2 }$ ,thenbydefinition $u _ { 1 } \circ u _ { 2 } = w \in \mathcal { H }$ andwe absorb the second factor into the first and obtainaproduct $w \circ u _ { 3 } \circ \ldots \circ u _ { m }$ with fewer factors.

Case2.If $u _ { 1 } < u _ { 2 } \leq . . . ,$ we shuffle the factorswith the help of Lemma 3.10 and obtain for（3.30) the expression

$$
- \sum _ { i = 2 } ^ { m } c ( u _ { i } \circ u _ { 1 } \circ \ldots ) + \prod _ { i = 1 } ^ { m } c ( u _ { i } ) + \ldots .
$$

With the first termswe return to Case1,the second term is precisely as in (3.28), and the terms $\div \cdot \cdot$ ”arecoveredby the induction hypothesis.

Case3.Now let $u _ { 1 } = u _ { 2 } < \ldots$ .In this case,the formula(3.25)ofLemma 3.10 contains the term(3.30) twice.We group both together,so that(3.30) becomes

$$
- \frac { 1 } { 2 } \sum _ { i = 3 } ^ { m } c ( u _ { i } \circ u _ { 1 } \circ u _ { 1 } \circ . . . ) + \frac { 1 } { 2 } \prod _ { i = 1 } ^ { m } c ( u _ { i } ) + . . . .
$$

and we go back toCase 1.If the first three trees areequal,we group three equal terms together and so on.

The whole reduction process is repeated until all Butcher products have disappeared. □

Theorem3.14 (Murua& Sanz-Serna 199).The compositionmethod $\varPsi _ { h } ( y ) =$ $B _ { \infty } ( a _ { s } , y )$ of(3.9)has orderpifand onlyif

$$
a _ { s } ( \tau ) = \mathbf { e } ( \tau ) \qquad f o r \ \tau \in \mathcal { H } w i t h \ \lVert \tau \rVert \ x 
$$

The coefficients ${ \bf e } ( \tau )$ are those ofTheorem3.6.

Proof.We have seen in Sect.II.4 that compositionmethods of arbitrarily high order exist.Since the coefficients $A _ { i }$ of（3.28）do not depend onthemapping $c ( \tau )$ ,this togetherwith Theorem 3.6impliesthat therelation(3.28)isalso satisfiedby the mappinge for the exact solution.This proves the statement. □

Example 3.15.The order conditions for orders $p = 1 , \ldots , 4$ become,with the trees ofExample3.12andtheruleof(3.14),asfollows:

$$
\begin{array} { r l } { \mathrm { O o d e r 1 1 } } & { { } \quad \mathfrak { O } } \\ { \mathrm { O d e r 2 1 } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ) = 1 } \\ { \mathrm { O d e r 2 2 } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } - \beta _ { k } ^ { 2 } ) = 0 } \\ { \mathrm { O d e r 3 } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { 3 } + \beta _ { k } ^ { 2 } ) = 0 } \\ { \mathrm { O d e r 4 } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) = 0 } \\ { \quad \mathbb { \tilde { Q } } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } - \beta _ { k } ^ { 2 } ) \underset { k = 1 } { \overset {  } { \longrightarrow } } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) = 0 } \\ { \mathrm { O d e r 4 . } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) = 0 } \\ { \quad \mathbb { \tilde { Q } } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) \underset { k = 1 } { \overset {  } { \longrightarrow } } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) = 0 } \\ { \quad \mathbb { \tilde { Q } } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) \underset { k = 1 } { \overset {  } { \longrightarrow } } ( a _ { k } ^ { - } + \beta _ { k } ) } \\ { \quad \mathbb { \tilde { Q } } } & { { } \quad \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { - } + \beta _ { k } ^ { 2 } ) \underset { k = 1 } { \overset {  } { \longrightarrow } } ( a _ { k } ^ { - } + \beta _ { k } ) ^ { 2 } . } \end{array}
$$

where,as above,aprime attached toa summationsymbol indicates that thesumof $\alpha _ { \ell } ^ { 2 }$ is only from1 to $k = 1$ ,whereas the sum of $( - \beta _ { \ell } ) ^ { 2 }$ isfrom $1$ to $k$ Similarly,the remaining treesofExample 3.12with $| | \tau | | = 5$ and $| | \tau | | = 6$ give the additional conditionsfororder5and6.

Weshall see in Sect.V.3 how further reductions and numerical values are obtainedunder various assumptions of symmetry.

# III.3.4Order Conditions for Splitting Methods

Splitting methods,introduced inSect.II.5,arebased ondifferential equations of the form

$$
\dot { y } = f _ { 1 } ( y ) + f _ { 2 } ( y ) ,
$$

where the flows $\varphi _ { t } ^ { [ 1 ] }$ nd[2 of the systems $\dot { y } = f _ { 1 } ( y )$ and $\dot { y } = f _ { 2 } ( y )$ are assumed to beknown exactly.In this situation,the method

$$
\varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] }
$$

is of first order and,together with its adjoint $\varPhi _ { h } ^ { * } = \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h } ^ { [ 1 ] }$ can be used as the basic method in the composition (3.9).This yields

$$
\varPsi _ { h } = \varphi _ { a _ { s + 1 } h } ^ { [ 1 ] } \circ \varphi _ { b _ { s } h } ^ { [ 2 ] } \circ \varphi _ { a _ { s } h } ^ { [ 1 ] } \circ \cdots \circ \varphi _ { b _ { 2 } h } ^ { [ 2 ] } \circ \varphi _ { a _ { 2 } h } ^ { [ 1 ] } \circ \varphi _ { b _ { 1 } h } ^ { [ 2 ] } \circ \varphi _ { a _ { 1 } h } ^ { [ 1 ] }
$$

where

$$
b _ { i } = \alpha _ { i } + \beta _ { i } , \qquad a _ { i } = \alpha _ { i - 1 } + \beta _ { i }
$$

with the conventions $\alpha _ { 0 } = 0$ and $\beta _ { s + 1 } = 0$ .Consequently,the spliting method (3.33)is aspecial case of(3.9)and we have the following obvious result.

Theorem3.16.Supposethatthe compositionmethod(3.9) isoforder $p$ forall basicmethods $\phi _ { h }$ ,thenthesplittingmethod(3.33)with $a _ { i } , b _ { i }$ givenby(3.34）isof thesame order $p$ . □

We now want to establish the reciprocal result.To every consistent splitting method(3.33),i.e.,with coefficients satisfying $\textstyle \sum _ { i } a _ { i } = \sum _ { i } b _ { i } = 1$ ,thereexist unique $\alpha _ { i } , \beta _ { i }$ such that (3.34） holds.Does the corresponding composition method havethe same order?

Theorem3.17.Ifa consistentsplitingmethod(3.33）isoforder $p$ at least for problemsoftheform(3.32)withtheintegrablesplitting

$$
f _ { 1 } ( y ) = \left( { g _ { 1 } ( y _ { 2 } ) } \right) , \quad f _ { 2 } ( y ) = \left( { 0 \atop g _ { 2 } ( y _ { 1 } ) } \right) \quad w h e r e \quad y = \left( { y _ { 1 } \atop y _ { 2 } } \right) ,
$$

thenthe corresponding composition method has the same order $p$ foranarbitrary basicmethod $\varPhi _ { h }$

Proof.McLachlan(1995)provesthis result in thesettingofLiealgebras.Wegive herea proof using the tools of this section.

a) The flows corresponding to the two vector fields $f _ { 1 }$ and $f _ { 2 }$ of(3.35）are $\varphi _ { t } ^ { [ 1 ] } ( y ) = y + t f _ { 1 } ( y )$ and $\varphi _ { t } ^ { [ 2 ] } ( y ) = y + t f _ { 2 } ( y )$ respectively.Consequentlythe method $\varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] }$ can be writen in the form (3.1) with

$$
d _ { 1 } ( y ) = f _ { 1 } ( y ) + f _ { 2 } ( y ) , \qquad d _ { k + 1 } ( y ) = \frac { 1 } { k ! } f _ { 1 } ^ { ( k ) } ( y ) \Big ( f _ { 2 } ( y ) _ { \ast } . . . , f _ { 2 } ( y ) \Big ) .
$$

The idea is toconstruct,for every tree $\tau \in \mathcal { H }$ ,functions $g _ { 1 } ( y _ { 2 } )$ and $g _ { 2 } ( y _ { 1 } )$ such that the first component of $F ( \tau ) ( 0 )$ is non-zero whereas the first component of $F ( \sigma ) ( 0 )$ vanishes forall $\sigma \in { \cal T } _ { \infty }$ different from $\gamma$ .This construction will be explained in part(b)below.Since thelocal error of the compositionmethod isa $B _ { \infty }$ -serieswith coefficients $a _ { s } ( \tau ) - { \bf e } ( \tau )$ ,thisimplies that the order conditions for $\tau \in \mathcal { H }$ with $\| \tau \| \leq p$ arenecessaryalready for thisvery special class of problems.Theorem3.14 thus proves the statement.

b)For the construction of the functions $g _ { 1 } ( y _ { 2 } )$ and $g _ { 2 } ( y _ { 1 } )$ we have to understand the structure of $F ( \tau ) ( y )$ with $d _ { k } ( y )$ givenby(3.36).Consider for example the tree $\tau \in { \cal I } _ { \infty } ^ { \mathrm { ~ ~ } }$ of Fig.3.2,for which we have $F ( \tau ) ( y ) = d _ { 2 } ^ { \prime \prime } ( y ) ( d _ { 1 } ( y ) , d _ { 3 } ( y ) )$ .Inserting $d _ { k } ( y )$ from(3.36),we get byLeibniz'rulea linear combination of eight expressions ( $i \in \{ 1 , 2 \}$ ）

$$
\begin{array} { r l r } { f _ { 1 } ^ { \prime \prime \prime } \big ( f _ { 2 } , f _ { i } , f _ { 1 } ^ { \prime \prime } ( f _ { 2 } , f _ { 2 } ) \big ) , } & { \qquad } & { f _ { 1 } ^ { \prime \prime } \big ( f _ { 2 } ^ { \prime } f _ { i } , f _ { 1 } ^ { \prime \prime } ( f _ { 2 } , f _ { 2 } ) \big ) , } \\ { f _ { 1 } ^ { \prime \prime } \big ( f _ { i } , f _ { 2 } ^ { \prime } f _ { 1 } ^ { \prime \prime } ( f _ { 2 } , f _ { 2 } ) \big ) , } & { \qquad } & { f _ { 1 } ^ { \prime } f _ { 2 } ^ { \prime \prime } \big ( f _ { i } , f _ { 1 } ^ { \prime \prime } ( f _ { 2 } , f _ { 2 } ) \big ) , } \end{array}
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/028e0edd22d39ae32400bb62d26cc9d456ecee6f70978f74bb4e46f094b0fff7.jpg)  
Fig.3.2.Trees for illustrating the equivalence of the order conditions between composition and splitting methods

eachof which can be identified with a bi-coloured tree(see Sect.II.2.1,a vertex ·corresponds to $f _ { 1 }$ and $^ \circ$ to $f _ { 2 }$ .The trees corresponding to these expressions with $i = 1$ areshowninFig.3.2.Due to the special formof $d _ { k } ( y )$ in（3.36）and due to the fact that intrees of theHall set $\mathcal { H }$ thevertex $\textcircled{1}$ canappear only at the end of a branch,there isalwaysatleast one bi-coloured treewhere the vertices· areseparated by those of $^ \circ$ and vice versa.We now select such a tree,denoted by $\boldsymbol { \tau } _ { b }$ ,andwe label the black andwhite vertices with $\{ 1 , 2 , \ldots \}$ We then let $y _ { 1 } =$ $( y _ { 1 } ^ { 1 } , \dots , y _ { n } ^ { 1 } ) ^ { T }$ and $y _ { 2 } = ( y _ { 1 } ^ { 2 } , \dots , y _ { m } ^ { 2 } ) ^ { I }$ ,where $\boldsymbol { n }$ and $m$ are the numbers of vertices ·and $^ \circ$ in $_ { \textit { n } }$ ,respectively.Inspired by“Exercise4”ofHairer,Norsett&Wanner （1993),page 155,we define the $\textit { \textbf { l } }$ thcomponentof $g _ { 1 } ( y _ { 2 } )$ as the product of all $y _ { j } ^ { 2 }$ where $j$ runsthrough the labels of the verticesdirectly above the vertex·with label $\textit { i }$ Thefunction $g _ { 2 } ( y _ { 1 } )$ isdefined similarly.FortheexampleofFig.3.2,the tree $_ { \tau _ { b } }$ yields

$$
g _ { 1 } ( y _ { 2 } ) = \left( \begin{array} { c } { { y _ { 1 } ^ { 2 } } } \\ { { y _ { 2 } ^ { 2 } y _ { 3 } ^ { 2 } } } \\ { { 1 } } \end{array} \right) , \qquad g _ { 2 } ( y _ { 1 } ) = \left( \begin{array} { c } { { y _ { 2 } ^ { 1 } y _ { 3 } ^ { 1 } } } \\ { { 1 } } \\ { { 1 } } \end{array} \right) .
$$

One can check that with this construction the bi-coloured tree $T _ { b }$ is the only one forwhich the first component of theelementary differential evaluated at $y = 0$ is different from zero.Thisin turn implies that amongall treesof $T _ { \infty }$ only the tree $\tau$ hasanon-vanishing first component in itselementarydifferential. $\sqcap$

Necessity of Negative Steps for Higher Order. One notices that allthe compositionmethods(II.4.6) ofoder higher thantwo with $\phi _ { h }$ givenby（II.5.7） lead toa splitting(II.5.6）where at least one ofthe coefficients $a _ { i }$ and $b _ { i }$ is negative.This $\varphi _ { t } ^ { [ i ] }$ originates fromapartial differentialequation that isill-posed for negative time progression.The following result has beenproved independently by Sheng（1989)and Suzuki(1991) (see also Goldman &Kaper(1996)).Wepresent the elegant prooffound by Blanes&Casas (2005).

Theorem3.18.Ifthe splittingmethod(I1.5.6)isoforder $p \geq 3$ forgeneral $f ^ { [ 1 ] }$ and $f ^ { [ 2 ] }$ ,thenatleast oneof the $a _ { i }$ andat least one of the $b _ { i }$ are strictly negative.

Proof.The condition in equation (3.31) for the tree $\textcircled{3}$ reads

$$
\sum _ { k = 1 } ^ { s } ( \alpha _ { k } ^ { 3 } + \beta _ { k } ^ { 3 } ) = 0 \qquad \mathrm { o r ~ a l s o } \qquad \sum _ { k = 1 } ^ { s + 1 } ( \alpha _ { k - 1 } ^ { 3 } + \beta _ { k } ^ { 3 } ) = 0
$$

(remember that $\alpha _ { 0 } = 0$ and $\beta _ { s + 1 } = 0$ .Nowapplythefactthat $x ^ { 3 } + y ^ { 3 } < 0$ implies $x + y < 0$ and conclude with formulas (3.34). □

# III.4 The Baker-Campbell-Hausdorff Formula

This section treats the Baker-Campbell-Hausdorff(short BCH orCBH) formulaon the composition of exponentials.Itwasproposedin 1898 by J.E.Campbell and proved independentlybyBaker(1905）and Hausdorff(19O6).This formulawill provide an alternative approach to the order conditions of composition (Sect.II.4) and splitting methods(Sect.II.5).For its derivation we shall use the inverse of the derivative of the exponential function.

# III.4.1 Derivative of the Exponential and Its Inverse

Elegantformulas for the derivative of expand for its inverse can be obtained by theuse ofmatrix commutators $\left[ \Omega , A \right] = \Omega A - A \Omega$ Ifwe suppose $\varOmega$ fixed,this expression defines a linear operator $A \mapsto [ \varOmega , A ]$

$$
\operatorname { a d } _ { \Omega } ( A ) = [ \Omega , A ] ,
$$

which iscalled the adjoint operator(see Varadarajan(1974),Sect.2.13).Let us start by computing the derivatives of $\Omega ^ { k } .$ The productrule for differentiation becomes

$$
\Big ( \frac { d } { d \Omega } \Omega ^ { k } \Big ) H = H \Omega ^ { k - 1 } + \Omega H \Omega ^ { k - 2 } + . . . , + \Omega ^ { k - 1 } H ,
$$

and this equals $k H \varOmega ^ { k - 1 }$ if $\varOmega$ and $H$ commute.Therefore,itis natural to write (4.2)as $k H \Omega ^ { k - 1 }$ to which are added correction terms involving commutators and iterated commutators.In the cases $k = 2$ and $k = 3$ wehave

$$
\begin{array} { r c l } { { H \Omega + \Omega H } } & { { = } } & { { 2 H \Omega + { \sf a d } _ { \Omega } ( H ) } } \\ { { } } & { { } } & { { } } \\ { { H \Omega ^ { 2 } + \Omega H \Omega + \bar { \Omega } ^ { 2 } H } } & { { = } } & { { 3 H \Omega ^ { 2 } + 3 \bigl ( { \sf a d } _ { \Omega } ( H ) \bigr ) \Omega + { \sf a d } _ { \Omega } ^ { 2 } ( H ) , } } \end{array}
$$

where $\operatorname { a d } _ { \Omega } ^ { i }$ denotes the iterated application of the linear operator ad $\Omega$ With the convention ad $\mathbf { \Omega } _ { \Omega } ^ { 0 } ( H ) = H$ we obtain by induction on $k$ that

$$
\Big ( \frac { d } { d \Omega } \Omega ^ { k } \Big ) H = \sum _ { i = 0 } ^ { k - 1 } \binom { k } { i + 1 } \Big ( \mathrm { a d } _ { \Omega } ^ { i } ( H ) \Big ) \Omega ^ { k - i - 1 } .
$$

This isseenbyapplyingLeibniz'rule to $\Omega ^ { k + 1 } = \Omega \cdot \Omega ^ { k }$ and by using the identity $\Omega \big ( \mathrm { a d } _ { \Omega } ^ { i } ( H ) \big ) = \big ( \mathrm { a d } _ { \Omega } ^ { i } ( H ) \big ) \Omega + \mathrm { a d } _ { \Omega } ^ { i + 1 } ( H )$

Lemma4.1.Thederivativeof $\begin{array} { r } { \exp { \mathcal { Q } } = \sum _ { k \geq 0 } { \frac { 1 } { k ! } } \varOmega ^ { k } } \end{array}$ is given by

$$
\left( { \frac { d } { d \Omega } } \exp { \Omega } \right) H = \left( d \exp _ { \varOmega } ( H ) \right) \exp { \varOmega } ,
$$

where

$$
d \exp _ { \Omega } ( H ) = \sum _ { k \geq 0 } \frac { 1 } { ( k + 1 ) ! } \operatorname { a d } _ { \Omega } ^ { k } ( H ) .
$$

Theseries(4.4)converges forallmatrices $\Omega$ .

Proof.Multiplying(4.3by $( k ! ) ^ { - 1 }$ and summing,then exchanging the sumsand putting $\begin{array} { r } { j = k - i - 1 } \end{array}$ yields

$$
\begin{array} { r c l } { \displaystyle \left( \frac { d } { d \Omega } \exp \varOmega \right) H } & { = } & { \displaystyle \sum _ { k \geq 0 } \frac { 1 } { k ! } \sum _ { i = 0 } ^ { k - 1 } \binom { k } { i + 1 } \left( \mathsf { a d } _ { \Omega } ^ { i } ( H ) \right) \varOmega ^ { k - i - 1 } } \\ & { = } & { \displaystyle \sum _ { i \geq 0 } \sum _ { j \geq 0 } \frac { 1 } { ( i + 1 ) ! j ! } \left( \mathsf { a d } _ { \Omega } ^ { i } ( H ) \right) \varOmega ^ { j } . } \end{array}
$$

The convergence of the series follows from the boundedness of the linear operator ad $\Omega$ (wehave $\| \mathbf { a d } _ { \Omega } \| \leq 2 \| \Omega \| )$ . □

Lemma 4.2(Baker19o5).Iftheeigenvaluesofthelinear operatorad $^ { \small \int } { }$ aredifferent from 2lπiwith $\ell \in \{ \pm 1 , \pm 2 , \dots \}$ ,then $d \exp _ { \varOmega }$ isinvertible.Furthermore,we havefor $\| \Omega \| < \pi$ that

$$
d \exp _ { \varOmega } ^ { - 1 } ( H ) = \sum _ { k \geq 0 } \frac { B _ { k } } { k ! } \ a \mathrm { d } \mathbf { \Sigma } _ { \varOmega } ^ { k } ( H ) ,
$$

where $B _ { k }$ aretheBernoullinumbers,definedby $\begin{array} { r } { \sum _ { k \geq 0 } ( B _ { k } / k ! ) x ^ { k } = x / ( e ^ { x } - 1 ) . } \end{array}$

Proof.The eigenvalues of $d \exp _ { \varOmega }$ are $\begin{array} { r } { \mu = \sum _ { k \geq 0 } \lambda ^ { k } / ( k + 1 ) ! = ( e ^ { \lambda } - 1 ) / \lambda } \end{array}$ ， where $\lambda$ isan eigenvalue of ad $\Omega$ Byourassumption,the values $\mu$ are non-zero,so that $d \exp _ { \varOmega }$ isinvertible.Bydefinition of the Bernouli numbers,the composition of (4.5)with(4.4) gives the identity.Convergence for $\| \Omega \| < \pi$ follows from $\left| \left| \operatorname { a d } _ { \mathcal { S } } \right| \right| \leq$ $2 \| \boldsymbol { \Omega } \|$ and from the fact that the radius of convergence of the series for $x / ( e ^ { x } - 1 )$ is $2 \pi$ . □

# II1.4.2The BCHFormula

Let $A$ and $B$ betwoarbitrary(in general non-commuting)matrices.The problem is to find amatrix $C ( t )$ ,suchthat

$$
\exp ( t A ) \exp ( t B ) = \exp { C ( t ) } .
$$

Inorder to geta first idea of the form of $C ( t )$ ,wedevelopthe expression to theleft in aseries: $\begin{array} { r } { \exp ( t A ) \exp ( t B ) = I + t ( A + B ) + \frac { t ^ { 2 } } { 2 } ( A ^ { 2 } + 2 A B + B ^ { 2 } ) + { \mathcal O } ( t ^ { 3 } ) = : I + X . } \end{array}$ Forsufficiently small $t$ (hence $\| X \|$ issmall),the series expansion of the logarithm $\log ( I + X ) = X - X ^ { 2 } / 2 + \ldots$ yieldsamatrix $C ( t ) = \log ( I + X ) = t ( A + B ) +$ $\begin{array} { r } { \frac { t ^ { 2 } } { 2 } \big ( A ^ { 2 } + 2 A B + B ^ { 2 } - ( A + B ) ^ { 2 } \big ) + { \mathcal O } ( t ^ { 3 } ) } \end{array}$ ,which satisfies (4.6).This series has apositiveradius of convergence,because it is obtained by elementary operationsof convergent series.

Themainproblem of thederivation of theBCHformula isto get explicit formulas for the coefficients of the series for $C ( t )$ ,andto express the coefficientsof $t ^ { 2 } , t ^ { 3 } , \ldots$ intermsofcommutators.Withthehelpofthefollowinglemma,recurrence relations for these coefficientswill be obtained,which allow for an easy computation of the first terms.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/16533b341749b2cba66268cb0bb9c47f23984b97a310c12c0ebc80d294f289af.jpg)  
Lemma 4.3.Let $A$ and $B$ be(non-commuting)matrices.Then,(4.6) holds,where $C ( t )$ isthesolution of thedifferential equation

$$
\dot { C } = A + B + \frac { 1 } { 2 } \left[ A - B , C \right] + \sum _ { k \geq 2 } \frac { B _ { k } } { k ! } \operatorname { a d } _ { C } ^ { k } ( A + B )
$$

with initialvalue $C ( 0 ) = 0$ Recall thatad $\begin{array} { r } { \mathbf { \boldsymbol { c } } \mathbf { \boldsymbol { A } } = \left[ \boldsymbol { C } , \boldsymbol { A } \right] = \boldsymbol { C } \mathbf { \boldsymbol { A } } - \boldsymbol { A } \boldsymbol { C } } \end{array}$ ,andthat $B _ { k }$ denotethe Bernoulli numbersasinLemma4.2.

Proof.We followVaradarajan (1974),Sect.2.15,andwe consider for small $s$ and $t$ a smooth matrix function $Z ( s , t )$ such that

$$
\exp ( s A ) \exp ( t B ) = \exp { Z } ( s , t ) .
$$

UsingLemma4.1,thederivative of（4.8）with respect to $s$ is

$$
A \exp ( s A ) \exp ( t B ) = d \exp _ { Z ( s , t ) } \Bigl ( \frac { \partial Z } { \partial s } ( s , t ) \Bigr ) \exp Z ( s , t ) ,
$$

so that

$$
{ \frac { \partial Z } { \partial s } } = d \exp _ { Z } ^ { - 1 } ( A ) = 4 - { \frac { 1 } { 2 } } \left[ Z , A \right] + \sum _ { k \geq 2 } { \frac { B _ { k } } { k ! } } \operatorname { a d } _ { Z } ^ { k } ( A ) .
$$

We next take the inverse of (4.8)

$$
\exp ( - t B ) \exp ( - s A ) = \exp \bigl ( - Z ( s , t ) \bigr ) ,
$$

and differentiate thisrelation with respect to $t$ Asaboveweget

$$
\frac { \partial Z } { \partial t } = d \exp _ { - Z } ^ { - 1 } ( B ) = B + \frac { 1 } { 2 } \left[ Z , B \right] + \sum _ { k \geq 2 } \frac { B _ { k } } { k ! } \mathrm { a d } _ { Z } ^ { k } ( B ) ,
$$

becausead ${ \bf \underline { { { \boldsymbol { k } } } } } _ { Z } ( B ) = ( - 1 ) ^ { k } \mathsf { a d } { \mathsf { \boldsymbol { \Sigma } } } _ { Z } ^ { k } ( B )$ andthe Bernoulli numbers satisfy $B _ { k } = 0$ forodd $k > 2$ Acomparison of(4.6）with（4.8)gives $C ( t ) = Z ( t , t )$ Thestated diferentialequationfor $C ( t )$ therefore follows from $\begin{array} { r } { { \dot { C } } ( t ) = \frac { \partial { \cal Z } } { \partial s } ( t , t ) + \frac { \partial { \cal Z } } { \partial t } ( t , t ) , } \end{array}$ and from adding therelations (4.9)and(4.10). $\sqcup$

UsingLemma 4.3we can compute the first Taylor coefficients of $C ( t )$ ，

$$
\exp ( t A ) \exp ( t B ) = \exp \Bigl ( t C _ { 1 } + t ^ { 2 } C _ { 2 } + t ^ { 3 } C _ { 3 } + t ^ { 4 } C _ { 4 } + t ^ { 5 } C _ { 5 } + . . . \Bigr ) .
$$

Inserting this expansion of $C ( t )$ into (4.7) and comparing like powers of $t$ gives

$$
\begin{array} { r l r } { C _ { 2 } } & { = } & { A + B } \\ { C _ { 2 } } & { = } & { \frac { 1 } { 4 } [ A - B , A + B ] = \frac { 1 } { 2 } [ A , B ] } \\ { C _ { 3 } } & { = } & { \frac { 1 } { 6 } [ A - B , \frac { 1 } { 2 } [ A , B ] ] = \frac { 1 } { 1 2 } [ A , [ A , B ] ] + \frac { 1 } { 1 2 } [ B , [ B , A ] ] } \\ { C _ { 4 } } & { = } & { \dots = \frac { 1 } { 2 4 } \Big [ A , [ B , [ B , A ] ] \Big ] } \\ { C _ { 5 } } & { = } & { \dots = \dots = \frac { 1 } { 7 2 0 } \Big [ A , [ A , [ A , [ A , B ] ] ] \Big ] - \frac { 1 } { 7 2 0 } \Big [ B , [ B , [ B , [ B , A ] ] ] \Big ] } \\ & { } & { + \frac { 1 } { 3 6 0 } \Big [ A , [ B , [ B , [ B , A ] ] ] \Big ] + \frac { 1 } { 3 6 0 } \Big [ B , [ A , [ A , [ A , B ] ] \Big ] \Big ] } \\ & { } & { + \frac { 1 } { 1 2 0 } \Big [ A , [ A , [ B , [ B , A ] ] ] \Big ] + \frac { 1 } { 1 2 0 } \Big [ B , [ B , [ A , [ A , [ A , B ] ] ] \Big ] \Big ] . } \end{array}
$$

Here,the dots $\cdot \cdot \cdot$ in the formulas for $C _ { 4 }$ and $C _ { 5 }$ indicate simplifications with the help of theJacobi identity

$$
\left[ A , \left[ B , C \right] \right] + \left[ C , \left[ A , B \right] \right] + \left[ B , \left[ C , A \right] \right] = 0 ,
$$

whichisverified by straightforward calculation.For higher order the expressions soon become very complicated.

TheSymmetric BCH Formula. For theconstruction of symmetric splitting methodsit isconvenient to usea formula for the composition

$$
\exp \Bigl ( { \frac { t } { 2 } } A \Bigr ) \exp \bigl ( t B \bigr ) \exp \Bigl ( { \frac { t } { 2 } } A \Bigr ) = \exp \Bigl ( t S _ { 1 } + t ^ { 3 } S _ { 3 } + t ^ { 5 } S _ { 5 } + . . . \Bigr ) .
$$

Sincethe inverse of the left-hand side is obtained by changing the sign of $t$ ,the same must be true for the right-hand side.This explainswhy only odd powers of

$t$ arepresent in (4.14).Applying the BCH formula(4.11） to $\begin{array} { r l } { \exp ( { \frac { t } { 2 } } A ) \exp ( { \frac { t } { 2 } } B ) = ~ } & { { } } \end{array}$ $\exp C ( t )$ andasecond time to $\exp ( C ( t ) ) \exp ( - C ( - t ) )$ yields for thecoefficients of(4.14)(Yoshida1990)

$$
\begin{array} { r l } { S _ { 1 } } & { = \ A + B } \\ { S _ { 3 } } & { = \ - \frac 1 { 2 4 } \Big [ A , [ A , B ] \Big ] + \frac 1 { 1 2 } \Big [ B , [ B , A ] \Big ] } \\ { S _ { 5 } } & { = \ \frac { 7 } { 5 7 6 0 } \Big [ A , \big [ A , \big [ A , [ A , B ] \big ] \big ] \Big ] - \frac 1 { 7 2 0 } \Big [ B , \big [ B , \big [ B , [ B , A ] \big ] \Big ] \Big ] } \\ & { \quad + \frac 1 { 3 6 0 } \Big [ A , \big [ B , \big [ B , [ B , A ] \big ] \Big ] \Big ] + \frac 1 { 3 6 0 } \Big [ B , \big [ A , \big [ A , [ A , B ] \big ] \Big ] \Big ] } \\ & { \quad - \frac 1 { 4 8 0 } \Big [ A , \big [ A , \big [ B , [ B , A ] \big ] \Big ] \Big ] + \frac 1 { 1 2 0 } \Big [ B , \big [ B , \big [ A , [ A , B ] \big ] \Big ] \Big ] . } \end{array}
$$

# III.5 Order Conditions via the BCH Formula

Using the BCH formula we present an alternative approach to the order conditions of splittingand compositionmethods.Themainideais towrite the flow ofadifferential equation formallyasthe exponential oftheLiederivative.

# III.5.1 Calculusof Lie Derivatives

Foradifferential equation

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y ) ,
$$

it is convenient to study the composition of the flowst and $\varphi _ { t } ^ { [ 2 ] }$ of the systems

$$
\dot { y } = f ^ { [ 1 ] } ( y ) , \qquad \dot { y } = f ^ { [ 2 ] } ( y ) ,
$$

respectively.We introduce the differential operators(Liederivative)

$$
D _ { i } = \sum _ { j } f _ { j } ^ { [ i ] } ( y ) \frac { \partial } { \partial y _ { j } }
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/3031b13e70cc3cd68aafaa701d75b6c2ac5af5148efad9d803a4cc767a83d582.jpg)  
Wolfgang Grobner7

which means that fordifferentiable functions $F : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ wehave

$$
D _ { i } F ( y ) = F ^ { \prime } ( y ) f ^ { [ i ] } ( y ) .
$$

Itfollowsfomthechainruletatforthesoutions $\varphi _ { t } ^ { [ i ] } ( y _ { 0 } )$ of (5.1),

$$
\frac { d } { d t } F \big ( \varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) \big ) = \big ( D _ { i } F \big ) \big ( \varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) \big ) ,
$$

andapplying this operator iterativelywe get

$$
\frac { d ^ { k } } { d t ^ { k } } F \big ( \varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) \big ) = \big ( D _ { i } ^ { k } F \big ) \big ( \varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) \big ) .
$$

Consequently,the Taylor series of $F \left( \varphi _ { t } ^ { \left| i \right. } \left( y _ { 0 } \right) \right)$ ,developedat $t = 0$ ,becomes

$$
F \bigl ( \varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) \bigr ) = \sum _ { k \geq 0 } \frac { t ^ { k } } { k ! } ( \mathscr { D } _ { i } ^ { k } F ) ( y _ { 0 } ) = \exp ( t D _ { i } ) F ( y _ { 0 } ) .
$$

Now,putting $F ( y ) = \operatorname { I d } ( y ) = y ,$ ,theidentitymap,thisisthe Taylor seriesof the solution itself

$$
\varphi _ { t } ^ { [ i ] } ( y _ { 0 } ) = \sum _ { k \geq 0 } \frac { t ^ { k } } { k ! } ( D _ { i } ^ { k } \mathrm { I d } ) ( y _ { 0 } ) = \exp ( t D _ { i } ) \mathrm { I d } ( y _ { 0 } ) .
$$

If the functions $f ^ { \left[ i \right] } \left( y \right)$ arenot analytic,but only $N$ -timescontinuouslydifferentiable,the series (5.6)has to be truncated anda $\mathcal { O } ( h ^ { N } )$ remainder term has to be included.

Lemma5.1(Grobner1960).Let $\varphi _ { s } ^ { [ 1 ] }$ and $\varphi _ { t } ^ { [ 2 ] }$ bethefowsofthedifferentialequa tions $\dot { y } = f ^ { [ 1 ] } ( y )$ and $\dot { y } = f ^ { \left[ 2 \right] } ( y )$ ,respectively.For theircompositionwethen have

$$
\left( \varphi _ { t } ^ { [ 2 ] } \circ \varphi _ { s } ^ { [ 1 ] } \right) ( y _ { 0 } ) = \exp ( s D _ { 1 } ) \exp ( t D _ { 2 } ) \operatorname { I d } ( y _ { 0 } ) .
$$

Proof.This is precisely formula(5.5) with $i = 1$ ， $t$ replaced with $s$ ,andwith $F ( y ) =$ $\varphi _ { t } ^ { [ 2 ] } ( y ) = \exp ( t D _ { 2 } ) \mathrm { I d } ( y _ { 0 } )$ $\sqsubset$

Remark 5.2.Notice that the indices1and 2aswell as $s$ and $t$ to theleft and right intheidentity ofLemma5.1 arepermuted.Grobner calls thisphenomenon,which sometimes leads to some confusion in the literature,the“Vertauschungssatz".

Remark 5.3.Thestatement ofLemma5.1can be extended tomore thantwo flows. If $\varphi _ { t } ^ { [ j ] }$ istheflowofadiferentialequation ${ \dot { y } } = f ^ { [ j ] } ( y )$ ,thenwehave

$$
\left( \varphi _ { u } ^ { [ m ] } \circ \dots \circ \varphi _ { t } ^ { [ 2 ] } \circ \varphi _ { s } ^ { [ 1 ] } \right) ( y _ { 0 } ) = \exp ( s D _ { 1 } ) \exp ( t D _ { 2 } ) \cdot \dots \cdot \exp ( u D _ { m } ) \mathrm { I d } ( y _ { 0 } )
$$

This follows by induction on $m$

Ingeneral, the two operators $D _ { 1 }$ and $\boldsymbol { D } _ { 2 }$ do not commute,so that the composition $\exp ( t D _ { 1 } ) \exp ( t D _ { 2 } ) \mathrm { I d } ( y _ { 0 } )$ is different from $\exp \big ( t ( D _ { 1 } + D _ { 2 } ) \big ) \mathrm { I d } ( y _ { 0 } ) ,$ which represents the solution $\varphi _ { t } ( y _ { 0 } )$ of $\dot { y } = f ( y ) = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y )$ Therelation of Lemma5.1 suggeststheuseof theBCH formula.However, $D _ { 1 }$ and $D _ { 2 }$ areunbounded differential operators so that the series expansions that appear cannot be expected to converge.A formalapplication of the BCH formula with $t A$ and $t B$ replacedwith $s { \cal D } _ { 1 }$ and $t D _ { 2 }$ ,respectively,yields

$$
\exp ( s D _ { 1 } ) \exp ( t D _ { 2 } ) = \exp \bigl ( D ( s , t ) \bigr ) ,
$$

where the differential operator $D ( s , t )$ is obtained from (4.11)as

$$
\begin{array} { l } { { \displaystyle { \cal D } ( s , t ) ~ = ~ s D _ { 1 } + t D _ { 2 } + \frac { s t } { 2 } [ D _ { 1 } , D _ { 2 } ] + \frac { s ^ { 2 } t } { 1 2 } \Big [ D _ { 1 } , [ D _ { 1 } , D _ { 2 } ] \Big ] } } \\ { { \displaystyle ~ + \frac { s t ^ { 2 } } { 1 2 } \Big [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] \Big ] + \frac { s ^ { 2 } t ^ { 2 } } { 2 4 } \Big [ D _ { 1 } , \big [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] \big ] \Big ] + \dots . } } \end{array}
$$

TheLie bracket for differential operators is calculated exactly as for matrices, namely, $[ D _ { 1 } , D _ { 2 } ] = D _ { 1 } D _ { 2 } - D _ { 2 } D _ { 1 }$ But how canweinterpret（5.7） rigorously? Expanding both sidesin Taylor serieswe see that

$$
\exp ( s D _ { 1 } ) \exp ( t D _ { 2 } ) = I + s D _ { 1 } + t D _ { 2 } + \frac { 1 } { 2 } \Bigl ( s ^ { 2 } D _ { 1 } ^ { 2 } + 2 s t D _ { 1 } D _ { 2 } + t ^ { 2 } D _ { 2 } ^ { 2 } \Bigr ) + . . . .
$$

and

$$
\begin{array} { l } { \displaystyle \mathrm { x p } \big ( D ( s , t ) \big ) \ = \ I + D ( s , t ) + \frac { 1 } { 2 } D ( s , t ) ^ { 2 } + \ldots } \\ { \displaystyle = \ I + s D _ { 1 } + t D _ { 2 } + \frac { 1 } { 2 } \Big ( ( s D _ { 1 } + t D _ { 2 } ) ^ { 2 } + s t [ D _ { 1 } , D _ { 2 } ] \Big ) + \ldots \ . } \end{array}
$$

Byderivation of theBCH formulawehavea formal identity,i.e.,both series have exactly the same coefficients.Moreover,every finite truncation of the series can be applied without any diffculties to sufficiently differentiable functions $F ( y )$ .Consequently, for $N$ -timesdifferentiable functionstherelation(5.7)holdstrue,ifboth sidesarereplacedbytheir truncated Taylor seriesand ifa $\mathcal { O } ( h ^ { N } )$ remainderisadded $h = \operatorname* { m a x } ( | s | , | t | ) )$ .

# II1.5.2Lie Brackets and Commutativity

Ifwe apply $D _ { 2 }$ toa function $F ^ { \prime }$ ,followed byanapplication of $D _ { 1 }$ ,wewill obtain partial derivatives of $F$ offirst and second orders.However,if we subtract from this the same expression with $D _ { 1 }$ and $D _ { 2 }$ reversed,the second derivatives will cancel (thiswasalreadyremarkedupon by Jacobi（1862）,p.39:“differentialiapartialia secunda functionis $f$ noncontinere") and we see that theLie bracket

$$
[ D _ { 1 } , D _ { 2 } ] = D _ { 1 } D _ { 2 } - D _ { 2 } D _ { 1 } = \sum _ { i } \left( \sum _ { j } \left( \frac { \partial f _ { i } ^ { [ 2 ] } } { \partial y _ { j } } f _ { j } ^ { [ 1 ] } - \frac { \partial f _ { i } ^ { [ 1 ] } } { \partial y _ { j } } f _ { j } ^ { [ 2 ] } \right) \right) \frac { \partial } { \partial y _ { i } }
$$

isagainalinear diferential operator.So,from two vector fields $f ^ { [ 1 ] }$ and $f ^ { [ 2 ] }$ we obtainathird vector field $f ^ { [ 3 ] }$ ,

$$
\begin{array} { r l r } & { \mathrm { T h e ~ } g e o m e t r i c ~ m e a n i n g ~ o f ~ t h e ~ n e w ~ v e c t o r }  & \\ & { \mathrm { e l d ~ c a ~ n b e ~ d e d u c e d ~ f r o m ~ L e m m a ~ 5 . 1 . ~ W e ~ s e e } } & \\ & { \mathrm { \ y ~ s u b t r a c t i n g ~ ( 5 . 9 ) ~ f r o m ~ i t s e l f , ~ o n c e ~ a s ~ i t ~ s t a n d s } } & \\ & { \mathrm { n d ~ o n c e ~ w i t h ~ } s D _ { 1 } \mathrm { ~ a n d ~ } t D _ { 2 } \mathrm { ~ p e r m u t e d , ~ t h a t ~ } } & \\ & { \mathrm { \ y } _ { t } ^ { [ 2 ] } \circ \varphi _ { s } ^ { [ 1 ] } ( y _ { 0 } ) - \varphi _ { s } ^ { [ 1 ] } \circ \varphi _ { t } ^ { [ 2 ] } ( y _ { 0 } ) = s t [ D _ { 1 } , D _ { 2 } ] \mathrm { ~ l d } ( y _ { 0 } ) + . . . = s t f ^ { [ 3 ] } ( y _ { 0 } ) + . . . } \end{array}
$$

(seethepicture),where“+.."are terms oforder $\geq 3 .$ This leads us to the following result.

Lemma5.4.Let $f ^ { [ 1 ] } ( y )$ and $f ^ { [ 2 ] } ( y )$ bedefined onan open set.The corresponding fows $\varphi _ { s } ^ { [ 1 ] }$ and $\varphi _ { t } ^ { [ 2 ] }$ commuteeverefallfentys $t$ ifandonly if

$$
\left[ D _ { 1 } , D _ { 2 } \right] = 0 .
$$

Proof.The“onlyif”partisclear from(5.11).Forproving the“if”part,wetake $s$ and $t$ fixed,and subdivide,fora given $n$ ,theintegration intervals into $\boldsymbol { n }$ equidistant parts $\varphi _ { s } ^ { [ 1 ] } \left( y _ { 0 } \right)$ $\varDelta s = s / n$ byadiserete homotopy in and Thisallowsustotransformthesolution $n ^ { 2 }$ stepsino the solution $\varphi _ { s } ^ { [ 1 ] } \circ \varphi _ { t } ^ { [ 2 ] } ( y _ { 0 } )$ $\varphi _ { t } ^ { [ 2 ] }$ each 。 timeappending a small rectangle of size $O ( n ^ { - 2 } ) .$ If we denote such an intermediate stageby

$$
{ \cal T } _ { k } = \ldots \circ \varphi _ { j _ { 2 } \Delta t } ^ { [ 2 ] } \circ \varphi _ { i _ { 2 } \Delta s } ^ { [ 1 ] } \circ \varphi _ { j _ { 1 } \Delta t } ^ { [ 2 ] } \circ \varphi _ { i _ { 1 } \Delta s } ^ { [ 1 ] } ( y _ { 0 } )
$$

then we have $\varGamma _ { 0 } = \varphi _ { t } ^ { [ 2 ] } \circ \varphi _ { s } ^ { [ 1 ] } ( y _ { 0 } )$ and ${ \varGamma _ { n ^ { 2 } } = \varphi _ { s } ^ { [ 1 ] } \circ \varphi _ { t } ^ { [ 2 ] } ( y _ { 0 } ) }$ (see Fig.5.1).Now, for $u \longrightarrow \infty$ ,we have the estimate

$$
| T _ { k + 1 } - T _ { k } | \leq \mathcal { O } ( n ^ { - 3 } ) ,
$$

because theerror terms in(5.11）areof order3at least,and because of the differentiability of the solutionswith respect to initial values.Thus,by the triangle inequality $| T _ { n ^ { 2 } } - T _ { 0 } | \leq \mathcal { O } ( n ^ { - 1 } )$ and theresult is proved. □

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/f00caf57b243f9065151404c1ac7bf52a19aa5b3d53b54e7d03c85f92242750b.jpg)  
Fig.5.1.Estimation of commuting solutions

# III.5.3 Splitting Methods

Wefollow the approach of Yoshida（199O) for obtaining the order conditions of splitting methods (II.5.6).Theidea is the following:with the use ofLemma5.1we write the method asaproduct of exponentials,thenwe apply formally theBaker-Campbell-Hausdorff formula to get one exponential of a series in powers of $h$ Finally,we compare this series with $h ( D _ { 1 } + D _ { 2 } )$ ,which correspondsto theexact solution of (5.1).

The splitting method (II.5.6),viz.,

$$
\varPsi _ { h } = \varphi _ { b _ { m } h } ^ { [ 2 ] } \circ \varphi _ { a _ { m } h } ^ { [ 1 ] } \circ \varphi _ { b _ { m - 1 } h } ^ { [ 2 ] } \circ \dots \circ \varphi _ { a _ { 2 } h } ^ { [ 1 ] } \circ \varphi _ { b _ { 1 } h } ^ { [ 2 ] } \circ \varphi _ { a _ { 1 } h } ^ { [ 1 ] } ,
$$

isacomposition of expressions $\varphi _ { b , h } ^ { [ 2 ] } \circ \varphi _ { a , h } ^ { [ 1 ] }$ hich,byd.7) bewritten as an exponential

$$
\begin{array} { r } { \varphi _ { b _ { j } \hbar } ^ { [ 2 ] } \circ \varphi _ { a _ { j } \hbar } ^ { [ 1 ] } = \exp \Bigl ( a _ { j } \hbar E _ { 1 } ^ { 1 } + b _ { j } \hbar E _ { 2 } ^ { 1 } + a _ { j } b _ { j } \hbar ^ { 2 } E _ { 1 } ^ { 2 } } \\ { \qquad + a _ { j } ^ { 2 } \hat { b } _ { j } \hbar ^ { 3 } E _ { 1 } ^ { 3 } + a _ { j } \hat { b } _ { j } ^ { 2 } \hbar ^ { 3 } E _ { 2 } ^ { 3 } + a _ { j } ^ { 2 } b _ { j } ^ { 2 } \hbar ^ { 4 } E _ { 1 } ^ { 4 } + . . . \Bigr ) \mathrm { I d } , } \end{array}
$$

wherewe use the abbreviations

$$
\begin{array} { r l } { { } } & { { E _ { 1 } ^ { 1 } = D _ { 1 } , \quad E _ { 2 } ^ { 1 } = D _ { 2 } , \quad E _ { 1 } ^ { 2 } = \displaystyle \frac { 1 } { 2 } [ D _ { 1 } , D _ { 2 } ] _ { \nu } \quad E _ { 1 } ^ { 3 } = \displaystyle \frac { 1 } { 1 2 } \big [ D _ { 1 } , [ D _ { 1 } , D _ { 2 } ] \big ] , } } \\ { { } } & { { E _ { 2 } ^ { 3 } = \displaystyle \frac { 1 } { 1 2 } \big [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] \big ] , \quad E _ { 1 } ^ { 4 } = \displaystyle \frac { 1 } { 2 4 } \big [ D _ { 1 } [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] ] \big ] , } } \end{array}
$$

and the dots indicate $\mathcal { O } ( h ^ { 5 } )$ expressions.

We next define $\varPsi ^ { ( j ) }$ recursively by

$$
\varPsi ^ { ( 0 ) } = \mathrm { I d } , \qquad \varPsi ^ { ( j ) } = \varphi _ { b _ { j } h } ^ { [ 2 ] } \circ \varphi _ { a _ { j } h } ^ { [ 1 ] } \circ \varPsi ^ { ( j - 1 ) } ,
$$

so that $\varPsi ^ { ( m ) }$ is equal to our method (5.13).Aiming to write $\varPsi ^ { ( j ) }$ also as an exponentialof differential operators,we are confronted with computing commutators of the expressions $E _ { i } ^ { j } .$ Wesee that $\left[ E _ { 1 } ^ { 1 } , E _ { 2 } ^ { 1 } \right] = 2 E _ { 1 } ^ { 2 }$ $\left[ E _ { 1 } ^ { 1 } , E _ { 1 } ^ { 2 } \right] = 6 E _ { 1 } ^ { 3 } ,$ $[ E _ { 2 } ^ { \scriptscriptstyle 1 } , E _ { 1 } ^ { \scriptscriptstyle 2 } ] = - 6 E _ { 2 } ^ { 3 }$ ， $[ E _ { 1 } ^ { 1 } , E _ { 2 } ^ { 3 } ] = 2 E _ { 1 } ^ { 4 }$ ,and $\left[ E _ { 2 } ^ { 1 } , \alpha _ { 1 } ^ { 3 } \right] = - 2 E _ { 1 } ^ { 4 }$ asaconsequence of the Jacobi identity (4.13).But the other commutators cannot be expressed in terms of $E _ { i } ^ { \mathcal { I } } .$ We therefore introduce

$$
E _ { 2 } ^ { 4 } = \frac { 1 } { 2 4 } \big [ D _ { 1 } , [ D _ { 1 } , [ D _ { 1 } , D _ { 2 } ] ] \big ] , \quad E _ { 3 } ^ { 4 } = \frac { 1 } { 2 4 } \big [ D _ { 2 } , [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] ] \big ] .
$$

This allows us to formulate the following result.

Lemma5.5.Themethod $\varPsi ^ { ( j ) }$ ,definedby(5.15),canbeformallywrittenas

$$
\begin{array} { r } { \varPsi ^ { ( j ) } = \exp \Bigl ( c _ { 1 , j } ^ { 1 } h E _ { 1 } ^ { 1 } + c _ { 2 , j } ^ { 1 } h E _ { 2 } ^ { 1 } + c _ { 1 , j } ^ { 2 } h ^ { 2 } E _ { 1 } ^ { 2 } + c _ { 1 , j } ^ { 3 } h ^ { 3 } E _ { 1 } ^ { 3 } } \\ { + c _ { 2 , j } ^ { 3 } h ^ { 3 } E _ { 2 } ^ { 3 } + c _ { 1 , j } ^ { 4 } h ^ { 4 } E _ { 1 } ^ { 4 } + c _ { 2 , j } ^ { 4 } h ^ { 4 } E _ { 2 } ^ { 4 } + c _ { 3 , j } ^ { 4 } h ^ { 4 } E _ { 3 } ^ { 4 } + . . . \Bigr ) \mathrm { I d } , } \end{array}
$$

whereall coefficientsare zero for $j = 0$ andwherefor $j \geq 1$

$$
\begin{array} { r l } & { c _ { 1 , j } ^ { 1 } = c _ { 1 , j - 1 } ^ { 1 } + a _ { j } , \qquad c _ { 2 , j } ^ { 1 } = c _ { 2 , j - 1 } ^ { 1 } + b _ { j } , } \\ & { c _ { 1 , j } ^ { 2 } = c _ { 1 , j - 1 } ^ { 2 } + a _ { j } b _ { j } + c _ { 1 , j - 1 } ^ { 1 } b _ { j } - c _ { 2 , j - 1 } ^ { 1 } a _ { j } , } \\ & { c _ { 1 , j } ^ { 3 } = c _ { 1 , j - 1 } ^ { 3 } + a _ { j } ^ { 2 } b _ { j } + 2 c _ { 1 , j - 1 } ^ { 1 } a _ { j } b _ { j } - 3 c _ { 1 , j - 1 } ^ { 2 } a _ { j } } \\ & { \qquad + ( c _ { 1 , j - 1 } ^ { 1 } ) ^ { 2 } b _ { j } - c _ { 1 , j - 1 } ^ { 1 } c _ { 2 , j - 1 } ^ { 1 } a _ { j } + c _ { 2 , j - 1 } ^ { 1 } a _ { j } ^ { 2 } , } \\ & { c _ { 2 , j } ^ { 3 } = c _ { 2 , j - 1 } ^ { 3 } + a _ { j } b _ { j } ^ { 2 } - 4 c _ { 2 , j - 1 } ^ { 1 } a _ { j } b _ { j } + 3 c _ { 1 , j - 1 } ^ { 2 } b _ { j } } \\ & { \qquad + ( c _ { 2 , j - 1 } ^ { 1 } ) ^ { 2 } a _ { j } - c _ { 1 , j - 1 } ^ { 1 } c _ { 2 , j - 1 } ^ { 1 } b _ { j } + c _ { 1 , j - 1 } ^ { 1 } b _ { j } ^ { 2 } , } \end{array}
$$

andsimilarbutmorecomplicatedformulasfor $c _ { i , j } ^ { 4 } .$

Proof.Due to thereversed orderinLemma5.1we have to compute $\exp ( A ) \exp ( B )$ ， where $A$ is theargument of the exponential for $\varPsi ^ { ( j - 1 ) }$ and $B$ is that of（5.14).The restisa tedious but straightforward application of the BCH formula.One has touse repeatedly the formulas for $[ E _ { i } ^ { \mathcal { I } } , E _ { k } ^ { l } ]$ ,stated beforeLemma5.5. □

Theorem5.6.Thesplittingmethod(5.13)isoforderpif

$$
c _ { 1 , m } ^ { 1 } = c _ { 2 , m } ^ { 1 } = 1 \ , \qquad c _ { \ell , m } ^ { k } = 0 \quad f o r \ k = 2 , . . . , p \ a n d a l l \ \ell .
$$

$c _ { \ell , m } ^ { k }$

ProofThis isan immediate consequence ofLemma 5.5,because the conditions of order $p$ imply that the Taylor series expansion of $\Psi ^ { ( m ) } ( y _ { 0 } )$ coincides with that of the solution $\varphi _ { h } ( y _ { 0 } ) = \exp \big ( h ( D _ { 1 } + D _ { 2 } ) \big ) y _ { 0 }$ up to terms of size $\mathcal { O } ( h ^ { p } )$ □

Asimplification in the order conditions arises for symmetric methods (5.13), thatis,forcoeficients satisfying $a _ { m + 1 - i } = a _ { i }$ and $b _ { m - i } = b _ { i }$ for all $i$ (and $b _ { m } = 0$ ). By Theorem II.3.2,it is suficient to consider the order conditions(5.16) for odd $k$ only.

# II1.5.4 Composition Methods

We nowconsider composition methods (II.4.6),viz.,

$$
\varPsi _ { h } = \varPhi _ { \alpha , h } \circ \varPhi _ { \beta _ { s } h } ^ { * } \circ \varepsilon . . . \circ \varPhi _ { \beta _ { 2 } h } ^ { * } \circ \varPhi _ { \alpha _ { 1 } h } \circ \varPhi _ { \beta _ { 1 } h } ^ { * } ,
$$

where $\phi _ { h }$ isafirst-order method for ${ \dot { y } } = f ( y )$ and $\boldsymbol { \varPhi } _ { h } ^ { * }$ is its adjoint.We assume

$$
\varPhi _ { h } = \exp \Bigl ( h C _ { 1 } + h ^ { 2 } C _ { 2 } + h ^ { 3 } C _ { 3 } + . . . \Bigr ) \mathrm { I d }
$$

with differential operators $C _ { i } ,$ and such that $C _ { 1 }$ istheLiederivative operator corresponding to $\dot { y } = f ( y )$ For thesplitingmethod $\varPhi _ { h } = \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h } ^ { [ 1 ] }$ this follows from(5.14),and for general one-step methods this is aconsequence of Sect.IX.1 on backward error analysis.The adjoint method then satisfies

$$
\varPhi _ { h } ^ { * } = \exp \Bigl ( h C _ { 1 } - h ^ { 2 } C _ { 2 } + h ^ { 3 } C _ { 3 } - \ldots \Bigr ) \mathrm { I d } .
$$

Fromnow on the procedure is similar to that of Sect.II.5.3.We define $\varPsi ^ { ( j ) }$ recursivelyby

$$
\psi ^ { ( 0 ) } = \mathrm { I d } , \qquad \psi ^ { ( j ) } = \varPhi _ { \alpha _ { j } h } \circ \varPhi _ { \beta _ { j } h } ^ { * } \circ \varPsi ^ { ( j - 1 ) } ,
$$

so that $\varPsi ^ { ( m ) }$ becomes (5.17).We apply theBCH formula to obtain

$$
\begin{array} { r l } { \mathrm { \Lambda } _ { x j } \Lambda ^ { \circ } \Phi _ { \beta _ { j } h } ^ { * } \ = \ \mathrm { e x p } \Big ( \beta _ { j } h C _ { 1 } - \beta _ { j } ^ { 2 } h ^ { 2 } C _ { 2 } + \ldots \Big ) \exp \Big ( \alpha _ { j } h C _ { 1 } + \alpha _ { j } ^ { 2 } h ^ { 2 } C _ { 2 } + \ldots \Big ) \mathrm { I } } \\ { \ = \ } & { \exp \Big ( ( \alpha _ { j } + \beta _ { j } ) h E _ { 1 } ^ { 1 } + ( \alpha _ { j } ^ { 2 } - \beta _ { j } ^ { 2 } ) h ^ { 2 } E _ { 1 } ^ { 2 } } \\ { \ } & { \qquad + ( \alpha _ { j } ^ { 3 } + \beta _ { j } ^ { 3 } ) h ^ { 3 } E _ { 1 } ^ { 3 } + \frac { 1 } { 2 } \alpha _ { j } \beta _ { j } ( \alpha _ { j } + \beta _ { j } ) h ^ { 3 } E _ { 2 } ^ { 3 } + \ldots \Big ) \mathrm { I d } } \end{array}
$$

where

$$
E _ { 1 } ^ { k } = C _ { k } , ~ E _ { 2 } ^ { 3 } = [ C _ { 1 } , C _ { 2 } ] .
$$

We then have the following result.

Lemma5.7.Themethod $\varPsi ^ { ( j ) }$ of(5.20)can beformally writtenas

$$
\varPsi ^ { ( j ) } = \exp \Bigl ( \gamma _ { 1 , j } ^ { 1 } h E _ { 1 } ^ { 1 } + \gamma _ { 1 , j } ^ { 2 } h ^ { 2 } E _ { 1 } ^ { 2 } + \gamma _ { 1 , j } ^ { 3 } h ^ { 3 } E _ { 1 } ^ { 3 } + \gamma _ { 2 , j } ^ { 3 } h ^ { 3 } E _ { 2 } ^ { 3 } + . . . \Bigr ) \mathrm { I d } ,
$$

whereallcoeffcientsarezero for $j = 0$ andwhere for $j = 1 , \ldots , m$

$$
\begin{array} { l } { { \gamma _ { 1 , j } ^ { 1 } ~ = ~ \gamma _ { 1 , j - 1 } ^ { 1 } + \alpha _ { j } + \beta _ { j } } } \\ { { \gamma _ { 1 , j } ^ { 2 } ~ = ~ \gamma _ { 1 , j - 1 } ^ { 2 } + \alpha _ { j } ^ { 2 } - \beta _ { j } ^ { 2 } } } \\ { { \gamma _ { 1 , j } ^ { 3 } ~ = ~ \gamma _ { 1 , j - 1 } ^ { 3 } + \alpha _ { j } ^ { 3 } + \beta _ { j } ^ { 3 } } } \\ { { \gamma _ { 2 , j } ^ { 3 } ~ = ~ \gamma _ { 2 , j - 1 } ^ { 3 } + \frac { 1 } { 2 } \alpha _ { j } \beta _ { j } ( \alpha _ { j } + \beta _ { j } ) + \frac { 1 } { 2 } \gamma _ { 1 , j - 1 } ^ { 1 } ( \alpha _ { j } ^ { 2 } - \beta _ { j } ^ { 2 } ) - \frac { 1 } { 2 } \gamma _ { 1 , j - 1 } ^ { 2 } ( \alpha _ { j } + \beta _ { j } ) . } } \end{array}
$$

Proof.Similar toLemma5.5,theresult followsusing theBCH formula.

Theorem 5.8.Thecomposition method(5.17)isoforderpif

$$
\gamma _ { 1 , m } ^ { 1 } = 1 , \qquad \gamma _ { \ell , m } ^ { k } = 0 \quad f o r k = 2 , \ldots , p a n d a l l \ell .
$$

The coeffcients $\gamma _ { \ell , m } ^ { k }$ are those definedin Lemma 5.7.

$\gamma _ { 1 , m } ^ { 1 } = 1$ dind $\gamma _ { 1 , m } ^ { 2 } = \gamma _ { 1 , m } ^ { 3 } = 0$ are baied tothe first three order conditions of Example 3.15.The remaining condition for order3, $\gamma _ { 2 , m } ^ { 3 } = 0$ reads

$$
\begin{array} { l }   \displaystyle \sum _ { = 1 } ^ { n } \alpha _ { k } \beta _ { k } ( \alpha _ { k } + \beta _ { k } ) + \sum _ { k = 1 } ^ { m } ( \alpha _ { k } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k - 1 } ( \alpha _ { i } + \beta _ { i } ) - \sum _ { k = 1 } ^ { m } ( \alpha _ { k } + \beta _ { k } ) \sum _ { i = 1 } ^ { k - 1 } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k - 1 } ( \beta _ { i } + \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k - 1 } ( \beta _ { i } + \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { k } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k - 1 } ( \beta _ { i } - \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k } ( \beta _ { i } - \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { k } ( \alpha _ { i } ^ { 2 } - \beta _ { i } ^ { 2 } ) \sum _ { k = 1 } ^ { m } ( \alpha _ { i } ^ { 2 } - \beta _ { k } ^ { 2 } ) \sum _ { i = 1 } ^ { m } ( \alpha _ { i } ^  2  \end{array}
$$

Thiscondition is just the difference of the order conditions for the trees $\textcircled{2} \textcircled{0} \textcircled{1}$ and $\textcircled{1} \textcircled{0} \textcircled{2}$ $\gamma _ { 2 , m } ^ { 3 } = 0$ ,whose sumis zero by the SwitchingLemma 3.8.Thereforethecondition istoo Example3.15.

Symmetric Composition of Symmetric Methods.Consider now acomposition

$$
\varPsi _ { h } = \varPhi _ { \gamma _ { m } h } \circ \dots \circ \varPhi _ { \gamma _ { 2 } h } \circ \varPhi _ { \gamma _ { 1 } h } \circ \varPhi _ { \gamma _ { 2 } h } \circ \dots \circ \varPhi _ { \gamma _ { m } h } ,
$$

where $\phi _ { h }$ isasymmetric method that can be written as

$$
\varPhi _ { h } = \exp \Big ( h S _ { 1 } + h ^ { 3 } S _ { 3 } + h ^ { 5 } S _ { 5 } + . . . \Big ) \mathrm { I d }
$$

with $S _ { 1 }$ theLie derivative operator corresponding to $\dot { y } ~ = ~ f ( y )$ For the Strang splittingΦh=h/2 $\varPhi _ { h } = \varphi _ { h / 2 } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h / 2 } ^ { [ 1 ] }$ such an expansion follows from the symmetric BCH formula(4.14),and for general symmetric one-stepmethods from Sect.IX.2. Thederivation of the order conditions is similar totheabove with $\varPsi ^ { ( j ) }$ defined by

$$
\varPsi ^ { ( 1 ) } = \varPhi _ { \gamma _ { 1 } h } , \qquad \varPsi ^ { ( j ) } = \varPhi _ { \gamma _ { j } h } \circ \varPsi ^ { ( j - 1 ) } \circ \varPhi _ { \gamma _ { j } h } ,
$$

so that $\varPsi ^ { ( m ) }$ becomes (5.22).

Lemma5.9.Themethod $\varPsi ^ { ( j ) }$ canbe formally written as

$$
\varPsi ^ { ( j ) } = \exp \Bigl ( \sigma _ { 1 , j } ^ { 1 } h E _ { 1 } ^ { 1 } + \sigma _ { 1 , j } ^ { 3 } h ^ { 3 } E _ { 1 } ^ { 3 } + \sigma _ { 1 , j } ^ { 5 } h ^ { 5 } E _ { 1 } ^ { 5 } + \sigma _ { 2 , j } ^ { 5 } h ^ { 5 } E _ { 2 } ^ { 5 } + . . . . \Bigr )  { \mathrm { I d } } ,
$$

where $E _ { 1 } ^ { k } = S _ { k }$ $E _ { 2 } ^ { 5 } = \left[ S _ { 1 } [ S _ { 1 } , S _ { 3 } ] \right]$ ,and where $\sigma _ { 1 , 1 } ^ { k } = \gamma _ { 1 } ^ { k }$ ， $\sigma _ { 2 , 1 } ^ { 5 } = 0$ and

$$
\begin{array} { l } { { \sigma _ { 1 , j } ^ { k } \ = \ \sigma _ { 1 , j = 1 } ^ { k } + 2 \gamma _ { j } ^ { k } } } \\ { { \sigma _ { 2 , j } ^ { 5 } \ = \ \sigma _ { 2 , j = 1 } ^ { 5 } + \frac { 1 } { 6 } \Big ( \gamma _ { j } ^ { 3 } ( \sigma _ { 1 , j - 1 } ^ { 1 } ) ^ { 2 } - \gamma _ { j } \sigma _ { 1 , j - 1 } ^ { 1 } \sigma _ { 1 , j - 1 } ^ { 3 } - \gamma _ { j } ^ { 2 } \sigma _ { 1 , j - 1 } ^ { 3 } + \gamma _ { j } ^ { 4 } \sigma _ { 1 , j - 1 } ^ { 1 } \Big ) } } \end{array}
$$

Proof.Theresult isaconsequence ofthe symmetric BCH formula（4.14）with $\gamma _ { j } h S _ { 1 } + \gamma _ { j } ^ { 3 } h ^ { 3 } S _ { 3 } + \ldots$ and $\sigma _ { 1 , j - 1 } ^ { 1 } h E _ { 1 } ^ { 1 } + \sigma _ { 1 , j - 1 } ^ { 3 } h E _ { 1 } ^ { 3 } + \dots$ in the rolesof $\textstyle { \frac { t } { 2 } } A$ and $^ { t B }$ ,respectively. □

Theorem5.10.Thecompositionmethod(5.22)isoforderpif

$$
\sigma _ { 1 , m } ^ { 1 } = 1 , \quad \quad \sigma _ { \ell , m } ^ { k } = 0 \quad f o r o d d k = 3 , \ldots , p \ a n d a l l \ \ell .
$$

The coefcients $\sigma _ { \ell , m } ^ { k }$ are thosedefined in Lemma 5.9.

Symmetric composition methodsup to order 10 will be constructed and discussed in Sect.V.3.

# III.6 Exercises

1.Find all trees of orders 5 and 6.

2.(A.Cayley 1857).Denote the number of trees of order $q$ by $\boldsymbol { a } _ { q }$ Prove that

$$
a _ { 1 } + a _ { 2 } x + a _ { 3 } x ^ { 2 } + a _ { 4 } x ^ { 3 } + \dots = ( 1 - x ) ^ { - a _ { 1 } } ( 1 - x ^ { 2 } ) ^ { - a _ { 2 } } ( 1 - x ^ { 3 } ) ^ { - a _ { 3 } } \cdot ,
$$

$$
\frac { 9 }  \begin{array} { c c c c c c c c c c c c c c c c } { { q } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } & { { 8 } } & { { 9 } } & { { 1 0 } } & { { 9 } } & { { 9 } } & { { 7 } } & { { 9 } } & { { 9 } } & { { 7 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } & { { 9 } } &  { 1 0 } & { 9 } & { { 1 0 } } & { { 1 0 } } & { { 1 0 } } & { { 1 0 } } &  { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } & { 1 0 } &  1 \end{array}
$$

3.Independency of the elementarydifferentials:show that for every $\tau \in T$ there isa system(1.1) such that the first component of $F ( \tau ) ( 0 )$ equals1,and thefirst component of $F ( u ) ( 0 )$ is zero for all trees $u \neq t$ ,

Hint.Consider a monotonic labelling of $\tau$ ,anddefine $y _ { i } ^ { \prime }$ as the product over all $y _ { j }$ ,where $j$ runsthroughalllabels ofvertices that liedirectlyabove the vertex $\bar { \iota }$ .For the first labellingof the treeof Exercise4 this would be $\dot { y } _ { 1 } = y _ { 2 } y _ { 3 }$ $\dot { y } _ { 2 } = 1$ , ${ y _ { 3 } } = y _ { 4 }$ ,and ${ \dot { y } } _ { 4 } = 1$ .

4.Prove that the coefficient $\alpha ( \tau )$ ofDefinition1.2 is equal to the number of possible monotonic labellings of the vertices of $\tau$ ,startingwith thelabel1 for the root.For example,the tree $[ [ \bullet ] , \bullet ]$ has three different monotonic labellings.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/75883eb09fe265854afad123260359612df8b63fb104d942238d9aea5bbefbc6.jpg)

Inaddition,deduce,from(1.22),therecursion formula

$$
\alpha ( \tau ) = \binom { | \tau | - 1 } { | \tau _ { 1 } | , \dots , | \tau _ { m } | } \alpha ( \tau _ { 1 } ) \cdots \alpha ( \tau _ { m } ) \frac { 1 } { \mu _ { 1 } ! \mu _ { 2 } ! \dots , } ,
$$

where the integers $\mu _ { 1 } , \mu _ { 2 } , \ldots$ count equal trees among $\cdots , 1 1 \cdots$ and

$$
{ \binom { | \tau | - 1 } { | \tau _ { 1 } | , \dots , | \tau _ { m } | } } = { \frac { ( | \tau | - 1 ) ! } { | \tau _ { 1 } | ! \cdots \cdot | \tau _ { m } | ! } }
$$

denotes the multinomial coefficient.

Remark.In the theoretical physics literature,the coefficients $\alpha ( \tau )$ arewritten $C M ( \tau )$ andcalled"Connes-Moscovici weights".

5.If we denote by $N ( \tau )$ thenumber of elements in $O S T ( \tau )$ ,then show that

$$
N ( \bullet ) = 2 , \qquad N ( [ \tau _ { 1 } , \dots , \tau _ { m } ] ) = 1 + N ( \tau _ { 1 } ) \cdot \dots \cdot N ( \tau _ { m } ) .
$$

Use this result to compute the number of subtrees of the christmas tree decoratingformula(1.34).Answer:6865.

6.Prove that theelementarydifferentials forpartitioned problemsare independent.Fora given tree（ $\tau \in \mathit { \Delta } I P$ ,findaproblem(2.1） such that acertaincomponent of $F ( \tau ) ( p , q )$ vanishes forall $u \in \mathit { 1 } P$ except for $\tau$ ，

Hint.Consider the construction of Exercise 3,anddefine the partitioning of $y$ into $( p , q )$ according to the colours of the vertices.

7.The number of order conditions for partitioned Runge-Kutta methods (II.2.2) is $2 a _ { r }$ for order $r$ ,where $a _ { r }$ is given by(seeHairer,Norsett&Wanner(1993), page311)

<table><tr><td>r</td><td>2 3 4 5 6 7 8 9 10</td></tr><tr><td>1 1 ar</td><td>2 7 26 107 458 2058 9498</td></tr></table>

Find a formula similar to that of Exercise 2.

8.For the special second order differential equation $\ddot { y } = g ( y ) ,$ and fora Nystrom method

$$
\begin{array} { l } { { \ell _ { i } ~ = ~ g \Bigl ( y _ { 0 } + c _ { i } h \dot { y } _ { 0 } + h ^ { 2 } \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \ell _ { j } \Bigr ) , } } \\ { { y _ { 1 } ~ = ~ y _ { 0 } + h \dot { y } _ { 0 } + h ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { s } \beta _ { i } \ell _ { i } , ~ \dot { y } _ { 1 } ~ = ~ \dot { y } _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } \ell _ { i } , } } \end{array}
$$

consider the simplifying assumption

$$
\begin{array} { c l } { { \displaystyle C N ( \eta ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 2 } = \frac { c _ { i } ^ { k } } { k ( k - 1 ) } , \quad k = 2 , . . . , \eta , } } \\ { { \displaystyle D N ( \zeta ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } a _ { i j } = b _ { j } \Big ( \frac { c _ { j } ^ { k } } { k ( k - 1 ) } - \frac { c _ { j } } { k - 1 } + \frac { 1 } { k } \Big ) , \quad k = 2 , . . . , \zeta . } } \end{array}
$$

Prove that if thequadrature formula $( b _ { i } , c _ { i } )$ is of order $p$ ,if $\beta _ { i } = b _ { i } ( 1 - c _ { i } )$ forall $\boldsymbol { \imath }$ ,and if the simplifyingassumptions $C N ( \eta )$ , $D N ( \zeta )$ are satisfied with $2 \eta + 2 \geq p$ and $\zeta + \eta \geq p$ ,then theNystrommethod has order $p$ .

9.Nystrommethods ofmaximal order $2 s$ .Prove that there existsaone-parameter familyof $s$ -stageNystrommethods(6.2) for $\ddot { y } = g ( y )$ ,which have order $2 s$ .. Hint.Consider the Gaussian quadrature formula and define the coefficients $a _ { i j }$ by $C N ( s )$ andby

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } a _ { i s } = b _ { j } \bigg ( \frac { c _ { s } ^ { k } } { k ( k - 1 ) } - \frac { c _ { s } } { k - 1 } + \frac { 1 } { k } \bigg )
$$

for $k = 2 , \ldots , s$

10.Prove that the coefficient $C _ { 4 }$ inthe series (4.11）of the Baker-Campbell-Hausdorff formula is given by $C _ { 4 } = [ A , [ B , [ B , A ] ] ] / 2 4$

1.Prove that the series (4.11) converges for $| t | < \ln 2 / ( | | A | | + | | B | | )$

12.By Theorem 5.1O four order conditions haveto be satisfied such that the symmetriccomposition method(5.22) is of order6.Prove that these conditionsare equivalent to thefourconditions of ExampleV.3.15.(Care has to be taken due to thedifferent meaning of the $\gamma _ { i }$ .)
