# 386 Recursive formula for the product

We consider a formalism for the product on $G _ { 1 } \times G \to G$ , based on the second of the recursive constructions of trees defined in Subsection 300. That is, for

two trees $t$ , $u$ , we define $t u$ as the tree formed by joining the roots of $t$ and $u$ with the root of $t$ regarded as the root of the product. Corresponding to $t \in T ^ { \# }$ , we define $\widehat { t } : G _ { 1 } \to \mathbb { R }$ by the formula

$$
{ \widehat { t } } ( \alpha ) = \alpha ( t ) , \qquad \alpha \in G _ { 1 } .
$$

The set of all $\hat { \boldsymbol { t } }$ , for $t \in T$ , will be denoted by $\widehat { T }$ . We extend the dot-product notation from $T \times T  T$ to ${ \widehat { T } } \times { \widehat { T } }  { \widehat { T } }$ by the formula

$$
\widehat { t } \cdot \widehat { u } = \widehat { t } \widehat { u } .
$$

Since $\widehat { T } ^ { \# }$ denotes a set of linear functionals on $G$ , it is natural to consider also the vector space spanned by such functionals and extend the dot-product notation to make the product of two functionals bilinear. We denote this set of functionals by $G ^ { * }$ .

We can now define a special function, $\lambda : G _ { 1 } \times T \to G ^ { * }$ , by the recursion

$$
\begin{array} { c } { { \lambda ( \alpha , \tau ) = \widehat { \tau } , } } \\ { { \lambda ( \alpha , t u ) = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) . } } \end{array}
$$

This enables us to generate expressions for $\alpha \beta$ for all trees.

Theorem 386A For $\alpha \in G _ { 1 }$ and $\beta \in G$ ,

$$
\begin{array} { l } { { ( \alpha \beta ) ( \emptyset ) = \beta ( \emptyset ) , } } \\ { { ( \alpha \beta ) ( t ) = \lambda ( \alpha , t ) ( \beta ) + \alpha ( t ) \beta ( \emptyset ) . } } \end{array}
$$

Proof. In this proof only, we introduce the notation $R { \dot { < } } S$ to denote $R \triangleleft S$ , with $R \neq \emptyset$ . If a tree $t$ is represented by the set $S$ of vertices, with an implied set of edges, then the notation $t _ { R }$ , where $R \triangleleft S$ , will denote the tree formed from the elements of $R$ , with the induced set of edges. With this terminology, we can write (383a) in the form

$$
( \alpha \beta ) ( t ) = \sum _ { R \doteq S } \alpha ( S \setminus R ) \beta ( R ) + \alpha ( t ) \beta ( \emptyset ) .
$$

Hence, we need to show that

$$
\lambda ( \alpha , t ) = \sum _ { R \mathbin { \dot { \times } } \colon S } \alpha ( S \setminus R ) \widehat { t } _ { R } .
$$

This is obvious in the case $t = \tau$ . We now consider a tree $t u$ with $t$ represented by $S$ and $u$ represented by $Q$ . This means that $t u$ can be represented by the graph $( V , E )$ , where $V$ is the union of the vertex sets associated with $S$ and

The function $\lambda$ for trees of orders 1 to 5   

<table><tr><td>t</td><td></td><td>r(t) λ(α,t)</td><td></td></tr><tr><td>·</td><td>T</td><td>1</td><td></td></tr><tr><td>：</td><td>TT</td><td>2</td><td>T+a（T）</td></tr><tr><td>?</td><td>TT·T</td><td>3</td><td>+2a(T)+a(T)²</td></tr><tr><td>：</td><td>T·TT</td><td>3</td><td>.竹+a(T)T+a(TT)T</td></tr><tr><td>Y</td><td>(TT·T)T</td><td>4</td><td>(T.T)T+3a(T).↑+3a(T)²T+a(T)↑</td></tr><tr><td></td><td>· TT·TT</td><td>4</td><td>T+a(T)T.+a(T).TT+ (a(T)²+a(TT))TT+a(T)a(TT)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT·T)4 T(T.T)+2a(T)T.T+α(T)²TT+α(TT·T)T</td></tr><tr><td></td><td></td><td></td><td>T(T:TT)4 T(T.TT)+α(T)T.T+α(TT)TT+α(T·TT)T</td></tr><tr><td>W</td><td></td><td></td><td>(TT:T)T·T 5 (TT.T)T.T+4a(T)(TT.T)T+6a(T)².T+ 4a(t)+a(T)T</td></tr><tr><td></td><td></td><td></td><td>(TT·T)·TT 5 (TT.T).TT+2α(T)TT.TT+a(T)(TT.T)T+ 2a(T)².↑+(a(T)²+a(TT)).T+</td></tr><tr><td>?</td><td></td><td></td><td>(a(τ)³+2a(T)a(τT))TT+α(τ)²a(TT)T TT·(TT·T) 5 TT.(TT.T)+2a(T)TT.TT+α(T)T(TT.T)+ a(T)².↑+2a(T)².T+</td></tr><tr><td></td><td></td><td></td><td>(a(T)³+α(TT·T))TT+α(T)a(TT·T)T TT·(T.TT） 5 T.(T.TT)+a(T)TT.T+a(T)(T.TT)+ a(TT)TT.↑+a(T)².T+</td></tr><tr><td>V</td><td></td><td></td><td>(a(T)a(TT)+α(T:TT))TT+a(T)a(T·TT)T (T:TT).TT 5 (T.TT).TT+2a(T)TT.T+a(T)².T+ 2a(TT)T.TT+2a(T)a(TT)+α(TT)²↑</td></tr><tr><td></td><td></td><td></td><td>YT·(TT·T)T 5 T.(TT.T)T+3a(T)T(T.T)+3a(T)²TT+ a(T)³TT+a((TT.T)T)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT:TT)5 T(TT.T)+a(T)T(TT.T)+α(T)T(T.TT)+</td></tr><tr><td></td><td></td><td></td><td>(a(T)²+α(TT))T.TT+a(T)a(TT)TT+α(TT·TT)T T·T(TT.T） 5 T.T(.T)+2a(T)T(T.TT)+α(T)²T.TT+</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>α(TT·T)TT+α(T(TT·T))T</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T·T(T·TT) 5 T.T(T.TT)+a(T)T(T.TT)+α(TT)T.TT+</td></tr></table>

$Q$ , and $E$ is the union of the corresponding edge sets together with additional edge connecting the two roots. Temporarily we write $( V , E ) = S Q$ . If $R { \dot { < } } S$ and $P \mathcal { \hat { A } } Q$ then the set of subgraphs related to $S Q$ by the relation $X { \dot { \triangle } } S Q$ are of the form $X = R P$ or of the form $X = R$ . Hence,

Formulae for $( \alpha \beta ) ( t _ { i } )$ up to trees of order 5   

<table><tr><td>ti(αβ)(ti)</td><td>ir(ti)</td><td></td><td></td></tr><tr><td>0</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td>β+α1β0</td></tr><tr><td>2</td><td>2</td><td></td><td>β+α1β1+a2βo</td></tr><tr><td>3</td><td>3</td><td>?</td><td>β+2a1β2+α²β1+α3βo</td></tr><tr><td>4</td><td>3</td><td>…</td><td>β4+α1β+α2β1+a4βo</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>β5 + 3α1β+3a²β+a³β1+α5β0</td></tr><tr><td>6</td><td>4</td><td></td><td>β6+α1β4+α1β+(a²+a2)β+a1a2β1 +a6βo</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>β7 +2α1β4+a²β2+α3β1+α7β0</td></tr><tr><td>8</td><td>4</td><td>：</td><td>β8+a1β4 +a2β2+α4β1 +a8β0</td></tr><tr><td>9</td><td>5</td><td>E</td><td>βg+4a1β5+6a²β+4a³β+a𝑖β1+agβo</td></tr><tr><td>10</td><td>5</td><td></td><td>β10+2α1β6+α1β5 +a²β4+(2a² +α2)β3+ (2α1α2+α²)β+α²α2β1+α10β0</td></tr><tr><td></td><td>115</td><td></td><td>β11 +α1β7+2α1β6+2a²β4+α²β+(a²+α3)β²+</td></tr><tr><td></td><td>125</td><td></td><td>α1α3βi+α11β</td></tr><tr><td></td><td></td><td></td><td>α1α4β1+α12β0</td></tr><tr><td></td><td>135V</td><td></td><td>β13 +2α1β6+2a2β4+α²β+2α1α2β2+α²β1+α13β0</td></tr><tr><td></td><td>145</td><td></td><td>Yβ14+3α1β7+3a²β4+α³β+α5β1+α14/0</td></tr><tr><td>15</td><td>5</td><td></td><td>β15 +α1β8+α1β7+(a²+α2)β4+α1α2β+α6β1+α15β</td></tr><tr><td>165</td><td></td><td></td><td></td></tr><tr><td>17</td><td>5</td><td></td><td>β17 +α1β8+a2β4+α4β2+α8β1+α17β0</td></tr></table>

$$
\begin{array} { r l } { \displaystyle \sum _ { X \mathbin { \vrule d S Q } } \alpha ( S Q \setminus X ) \widehat { t } _ { X } = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P d \setminus P } } \alpha ( S Q \setminus P R ) \widehat { t } _ { P R } + \displaystyle \sum _ { R \mathbin { \vrule d S \widehat { X } } } \alpha ( S Q \setminus R ) \widehat { t } _ { R } } & { } \\ { = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P \widehat { t } _ { P } } } \alpha ( Q \setminus P ) \widehat { t } _ { P } \displaystyle \sum _ { R \mathbin { \vrule d S } } \alpha ( S \setminus R ) \widehat { t } _ { R } + \alpha ( ( S \setminus R ) Q ) \displaystyle \sum _ { R \mathbin { \vrule h } } \widehat { t } _ { R } } & { } \\ { = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) } & { } \\ { = \lambda ( \alpha , t u ) . } \end{array}
$$

<table><tr><td>ir(ti）</td><td></td><td></td><td>ti(a-1)(ti)</td></tr><tr><td>1</td><td>1</td><td>.</td><td>-α1</td></tr><tr><td>2</td><td>2</td><td></td><td>a²-a2 ：</td></tr><tr><td>3</td><td>3</td><td>Y</td><td>2α1α2 -α² -a3</td></tr><tr><td>4</td><td>3</td><td></td><td>三 2α1α2 -α² -α4</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>3α1α3 -3α2a² +α4 -α5</td></tr><tr><td>6</td><td>4</td><td></td><td>√ a1a3 +α1a4+a²- 3a2a² +a4 -a6</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>2α1α4 +α1α3 -3a²α2 +α𝑖 -α7</td></tr><tr><td>8</td><td>4</td><td></td><td>2α1α4+a²-3a²a2+a4-α8</td></tr><tr><td>9</td><td></td><td>√</td><td>4α1α5 -6a²α3 + 4a²α2 -α𝑖 -α9</td></tr><tr><td>10</td><td>5</td><td></td><td> 2α1a6 +α1a5 +α2a3 -a²α4 - 3a²α3 + 4α1α2 -α− - α10</td></tr><tr><td></td><td></td><td>115</td><td>α1α7 + 2α1α6 +α2α3-2a1α² -α²α3 - 2α²α4+ 4a³α2 -α -α11</td></tr><tr><td></td><td>125</td><td></td><td>4α²α2 -ai -α12</td></tr><tr><td></td><td></td><td>135</td><td>2α1a6+2α2α4-a²ag-2a²α4-3α1α²+4α³α2-a -α13</td></tr><tr><td></td><td>145</td><td></td><td>Y 3α1a7 +α1a5 - 3a²α4 -3a²αg +4a³α2 -α− - α14</td></tr><tr><td></td><td></td><td></td><td>α1a8 +α1α7 +α1a6 +α2α4 - 2α1a² -α²α3 -3a²α4+ 4α²α2 -α -α15</td></tr><tr><td></td><td>165</td><td></td><td>4α²α2 -α -α16</td></tr><tr><td>175</td><td></td><td></td><td>2α1α8 +2a2α4-3a1α² + 4α²α2 -α -α17</td></tr></table>

As examples of the use of the algorithm for evaluating $\lambda$ , and thence values of the product on $G _ { 1 } \times G$ , we find

$$
\begin{array} { r l } & { \quad \quad \lambda ( \alpha , \tau ) = \hat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \tau ) = \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } , } \\ & { \lambda ( \alpha , \tau \tau \cdot \tau ) = ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) \cdot \widehat { \tau } + \alpha ( t ) ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) } \\ & { \quad \quad \quad \quad = \widehat { \tau \tau } \cdot \widehat { \tau } + 2 \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau ) ^ { 2 } \widehat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \cdot \tau \tau ) = \widehat { \tau } \cdot ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) + \alpha ( \tau \tau ) \widehat { \tau } } \\ & { \quad \quad \quad = \widehat { \tau } \cdot \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau \tau ) \widehat { \tau } . } \end{array}
$$

The values of $\lambda ( \alpha , t )$ are continued in Table 386(I) up to trees of order 5. For convenience, each tree is given in product form as well as in pictorial form.

From (386a)–(386d), we find

$$
\begin{array} { r l } & { \quad ( \alpha \beta ) ( \tau ) = \beta ( \tau ) + \alpha ( \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau ) = \beta ( \tau \tau ) + \alpha ( \tau ) \beta ( \tau ) + \alpha ( \tau \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau \cdot \tau ) = \beta ( \tau \tau \cdot \tau ) + 2 \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau ) ^ { 2 } \beta ( \tau ) + \alpha ( \tau \tau \cdot \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \cdot \tau \tau ) = \beta ( \tau \cdot \tau \tau ) + \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau \tau ) \beta ( \tau ) + \alpha ( \tau \cdot \tau \tau ) \beta ( \emptyset ) . } \end{array}
$$

It will be convenient to extend these formulae up to trees of order 5, and we present this in Table 386(II). For convenience, we denote the empty tree by $t _ { 0 }$ and the trees of order 1 to 5 by $t _ { i }$ , $i = 1 , 2 , \dots , 1 7 .$ . We also write $\alpha _ { i }$ and $\beta _ { i }$ for $\alpha ( t _ { i } )$ and $\beta ( t _ { i } )$ , respectively. Note that $\alpha _ { 0 }$ does not appear in this table because it always has the value $\alpha ( \varnothing ) = 1$ .

Because Table 386(II) has reference value, we supplement the information it contains with Table 386(III), which gives the formulae for $( \alpha ^ { - 1 } ) ( t )$ where $r ( t ) \leq 5$ and $\alpha \in G _ { 1 }$ .
