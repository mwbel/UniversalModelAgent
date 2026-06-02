# CHAPTER X.

# PERTURBATIONS-ANALYTICAL METHOD.

203.Introductory Remarks. The subject of the mutual pertui bations of the motions of the heavenly bodies has been one to which many of the great mathematicians, from Newton's time on,have devoted a great dcal of attention. It is needless to say that the problem is very diffeult and that many mothods of attacking it have been devised. Since the geneial solulions of the problem have not been obtained it has been necessary to ti cat special classes of perturbations by special methodsIt has becn found convenient to divide the cases which arisc in the solar system into three geneial classes, (a) the Lunar Theoly and satelhte theories,(b) the mutual pei turbations of the planets,and (c) the perturbations of comets by planetsThe method which will be given in this chapter is applicable to the planetary theories,and it will be shown n the proper places why il is nol applicable to the other cases， References were given in the Iast chaptci to treatises on the Lunar Theory,especially to those of Tisserand and Brown, Some hints will be given in this chapter on the method of computing the pertuibations of comets.

The chief difficultics which arise in getting an understanding ot the theories of perturbations come from the laige number of variables which it 1s necessary to usc， and the very long transformations which must be made,in oder to put thc equations in & foim suitable for numerical computations. It is not possible, because of the lack of spaco, to develop heie m detail tho explicit expressions adapted to computation；and,mdecd,it is not desired to emphasize this part, fol it is much more important to get an accurate understandng of the nature of the pioblem, thc mathematcal features of the methods employed, the lmitations whch ae necessary, the exact places wheie approximalions aie intioduced,if at all,and their character,the ouigin of the vaiious sorts of terms,and the foundations upon which the celebiated theoicms regarding the stabilty of the solai system rest

Thero are two general methods of considering perlurbations, (a) as the variations of the coordinates of tho various bodies.

and (b) as the variations of the elements of their oibits. These two conceptions weie explaned in the beginning of the preceding chapterThcir analytical development was begun by Eulei and Clanaut and was caiied to a high degiee of perfection by Lagrange and Laplace,Yet thcie were pomts at which pure assumpttons weie inade, it having become possible to establish completcly the legitimacy of the procecdings，undel the proper iestrctions,only durng the lattei half of the nneteenth century by the aid of the woik in pure Mathemalics of Cauchy, Weierstrass, and Poincai6

204.Illustrative Example.Tho mathematical basis for the theory of pertuibations is oftcn obscuicd by the large number of variables and tho compleated foimulas which must be used. Many of the cssential fealurcs of tho method of computing pertui bations can be illustiatcd by sunplor examples which aie not subjcct to tho complexilics of many vaiiables and mvolved formulas.Onc will bo sclccted in which the physieal relations are also simplo

Consider the solution of

$$
\frac { d ^ { 2 } v } { d l ^ { 2 } } + h ^ { 2 } v = - \mu \left( \frac { d v } { d l } \right) ^ { 3 } + \nu \cos l t ,
$$

where k²,μ, v,and laio positivc constantsIf μ and y were zero tho differcntial cqualion would be that which defines simple harmonc motion. Il arises in many physical problems, such as that of the simplo pcndulum,and of all classes of musical inslruments In order to mako thc mterprolation defimle, supposc it bolongs to thc problom of lho vibiations of a tunmg fork．The fitst teim in tle right membel may bo interpreted as being due to the rosistance of lho mcdium m which tho tuning fork vibrates It is not assor lcd, of couise, that tho iesistance to tho vibrations of a tunmg fork varics as the third power of the velocityAn odd power is takcn so ihal tho differential cquation will have the same foim whether the molion i in thc posilivo or negative direction,and the firsl powor is nol laken becauso then the differontial cquation would bc lincar and could be completely integiated in finito torms withoul any dimculty

Thc loft member of cquation (1） will bo considered as defining the undisturbed molion of the tuning fork. Tho firsl term on the right introduccs a pcrturbation which depends upon the velocity of the tuning fork, the second teim on the iight introduces a perturbation which is independont of the position and velocity of the tuning foik The first is analogous to the mutual perturbations of the planets,which depend upon thcir relative positions,the second is more of the natuie of the foices which produco the tides,for they are exterior to the carth．The tides are defined by equations analogous to (1)

In order to have cquation (1) in the form of tho equations which arise in the thcory of perturbations, Iet

$$
\begin{array} { r l } { \mathfrak { x } = { \mathfrak { x } } _ { 1 } , \ } & { { } \ \frac { d { \mathfrak { x } } } { d t } = { \mathfrak { x } } _ { 2 } . } \end{array}
$$

Then (1) becomes

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } - x _ { 3 } = 0 , } \\ { \displaystyle \frac { d x _ { 3 } } { d t } + k ^ { 2 } x _ { 1 } = - \omega _ { 3 } ^ { 3 } + \nu \cos { \it \mathcal { U } } . } \end{array} \right.
$$

The corresponding diffeential equations for undisturbed motion are

$$
\left\{ \begin{array} { c } { \displaystyle { \frac { d x _ { 1 } } { d t } } - x _ { 2 } = 0 , } \\ { \displaystyle { \frac { d x _ { 2 } } { d t } } + k ^ { 2 } x _ { 1 } = 0 . } \end{array} \right.
$$

Equations (4)areeasily integrated,and their general stii

$$
\begin{array} { r l } { \cdot } & { { } \left\{ \begin{array} { l } { x _ { 1 } = { } + \alpha \cos \ k t + \beta \sin \ k t , } \\ { x _ { 2 } = { } - k \alpha \sin \ k t + k \beta \cos \ k t , } \end{array} \right. } \end{array}
$$

where α and β are the arbitrary constants of integration, In the terminology of Celestial Mechanics, $\pmb { \alpha }$ and $\beta$ are the elements of the orbit of the tuning fork

Now consider the problem of finding the solutions of equationg (3).Physically speaking, the elemnts $\pmb { \alpha }$ and $\beta$ must be so varied that the equations shall be satusfied for all values of t. Mathcmatically considered, equations (5） are relations betwecn the original dependent variables α1 and xz,and the new depcndont variablcs $_ { \pmb { \alpha } }$ and $\beta$ which make it possble to transform the differential equations (3) fiom one sel of variables to the other.This would be true whether (5) wcre solutions of (4) or not,but since (5)are solutions of (4) and (4) are a part of (3),a number of terms drop out after thc taansformation has been mado. On regarding

It is observed that the solution (9) is in reality a power sories in tho parameter μ,and the coefficients involve t If it 1s desired cquation (8) can be integiated directly as a powel series m $\mu _ { 0 }$ The piocess is, in fact, $\clubsuit$ general one which can be used in solving (7),and cquationg (1O),which follow,are the first terms of the solution The conditions of valdity of this method of inlegiation a10 given in Art. 207.

The fact that when $\pmb { \mu }$ is very small $\pmb { \alpha }$ and $\beta$ may be regarded as conslants m the right membeis of (7) fol not too gicat values of $\pmb { \mathscr { t } }$ can bo seen from $\mathfrak { a }$ physical illustration Considol the perturbalion theory. The changes in the clements of an oibit depond upon the elements of the orbits of the mutually disturbing bodies and upon the ielativo positions of the bodies in their oibitsIl is mtuilionally clear that only a slight erior m the computation of lho mutual disturbances of two plancts would be committed if constant clements were uscd which differ & lttlc,say& degico in the case of angular elements, from the tiue slowly changing ones.

If cquations (7） are integrated regarding α and β as constants im ihe right members,it is found that

$$
\begin{array}{c} \begin{array} { r } { \left\{ \alpha = \alpha a _ { 2 } - \nu \beta a ^ { \dagger } \left\{ \frac { \partial \alpha } { \partial t } ( \theta + \theta ) i + \frac { \beta } { \Delta t } ( \theta \alpha ^ { \dagger } + i \beta ) ( \log \alpha \log 2 i \beta - 1 ) \right\} \right.} \\ { - \frac { \beta } { \Delta t } ( \theta \alpha ^ { \dagger } - \theta ) ( \log \alpha \log 1 / \exp ( \alpha 4 \mu - 1 ) ) } \\ { - \frac { \alpha ^ { \dagger } } { \Delta t } \operatorname* { m a x } _ { i = 1 } ^ { 2 \pi } \frac { \partial \alpha } { \partial t } ( \theta + \frac { \alpha } { \partial t } \phi ^ { \dagger } \alpha - 3 i \beta ) \operatorname* { m a x } \Delta t \Big \} } \\ { + \frac { \beta } { \frac { \sqrt { \alpha } } { \sqrt { \beta } } } ( \log \alpha + i \beta ) \operatorname* { m a x } \delta ( - 1 ) i } \\ { - \frac { \beta } { 2 \sqrt { \alpha } } ( \theta \alpha - \theta ) ( \log ( 1 - i \beta ) - 1 ) } \\ { \beta = \beta _ { 2 } + \theta \beta ^ { \dagger } \left\{ - \frac { \beta } { \sqrt { \alpha } } ( \theta + \theta ) i - \frac { \beta } { \sqrt { \alpha } } ( \theta \alpha ^ { \dagger } + 3 \beta ) ( \log 2 i \beta - 1 ) \right\} } \\ { + \frac { \beta } { \Delta t } ( \alpha ^ { \dagger } - \theta ) ( \log 3 i \alpha - 1 ) } \\ { - \frac { \beta ^ { \dagger } } { \sqrt { \alpha } } i \alpha 2 \lambda t + \frac { \beta } { \sqrt { \alpha } } ( \theta \alpha ^ { \dagger } - \theta ) \circledast \alpha i \alpha ^ { \dagger } \} } \end{array}   \end{array}
$$

(5) as a sct of equations relating the variables x1 and xz to α and β, and makig direct substitulionm (3),it is found that

$$
\left\{ \begin{array} { l } { \displaystyle + \cos h t \frac { d \alpha } { d t } + \sin h t \frac { d \beta } { d t } = 0 , } \\ { \displaystyle - \sin h t \frac { d \alpha } { d t } + \cos h t \frac { d \beta } { d t } = \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } + \frac { \nu } { k } \mathfrak { c o s } l t } \end{array} \right.
$$

The eqatons re inar in $\frac { d \alpha } { d \ell } \ \mathrm { a n d } \ \frac { d \beta } { d t }$ and can be solved for these derivatives because tho detoimimant of their coefficients is unity. The solution is

$$
\begin{array} { r } { \left\{ \frac { d \alpha } { d t } = - \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } \sin k t - \frac { \nu } { \tilde { k } } \cos l t \sin k t _ { \prime } \right. } \\ { \left. \frac { d \beta } { d \tilde { l } } = + \mu k ^ { 2 } [ \alpha \sin k t - \beta \cos k t ] ^ { 3 } \cos k t + \frac { \nu } { \tilde { k } } \cos l t \cos k t _ { \prime } \right. } \end{array}
$$

The problem of solvng (7) is as diffcult as that of solving (3) because their iight members involve the unknown quantities α and β in as complcatcd manncr as xi and aa enter the iighl members of (3)But supposc μ and v are vcry small, then, since they enter as factorg in tho right membois of equations (7),the dependent variablcs α and β chango very slowly. Consequently,for a considerable time they will bo given with suffcient approximation if equations (7) aro intcgralcd regardmg lhem as constants in the right members. To assist in scoing this mathematically consider the simpler equation

$$
\frac { d \alpha } { d t } = \mu \alpha ( 1 + k \cos { k t } ) .
$$

The solution of this cquation is

$$
\alpha = C e ^ { \mu ( \ell + \ell \ln k \ell ) } ,
$$

wheie C is tho constant of inlcgration, If the right member of this equation is oxpanded, the cxprossion for α bocomes

$$
\alpha = C \left[ 1 + \mu ( \iota + \sin k \iota ) + \frac { \mu ^ { 2 } } { 2 } ( \iota + \sin k \iota ) ^ { 2 } + \ \cdot \cdot \right]
$$

If μ is vcry small and if t is nol too great tho right mcmber of this equation is nearly cqunl to its first two tormsIf it wcro not for the term t which is nol in tho trigonometrio function no limitations on t would bo nccessary. But in geneial such lmitations are necessary,and m most cascs,though not in thc prcsent ono, they arc nccessary in order lo soouto convorgonco of tho series.

whore α and βo are the values of α and β respectively at t = 0. When thcso values of α and β are substituted in (b) the values of x and m arc dotermined approximately for all values of t which arc not too remote from the initial time.

Consider cquations (10)．The right member of each of them has n term which contains lonly as a simple factor,while elsewhere $\pmb { \ell }$ appears only in the sine and cosine terms.The terms which are proportional to $\pmb { \ell }$ seem to indicate that $\pmb { \alpha }$ and $\beta$ increase or deorcase indofinitcely with the time；but it must be remembered that equations (10) are only approximate expressions for α and β, which are useful only for $\mathfrak { a }$ limited time.It might be that the rigorous expressions would contain higher powerg of $\mathbf { f } ,$ and that tho sums would havo bounded values, just as

$$
\sin i = i - { \frac { t ^ { 3 } } { 3 ! } } + { \frac { t ^ { 5 } } { 5 ! } } - \cdots
$$

is an oxpression whog numerical value does not exceed unity, though $\mathfrak { a }$ consideration of the first term alone would lead to the conclusion that it becomes indefinitely great with t. On the othcr hand tlio prcsenco of terms which increase proportionally to the timo may indicatc an actual indefinite ·increase of the clemonts $\pmb { \alpha }$ and $\beta$ For oxample, it was found in·the preceding chaptcr that the lino of nodes and the apsides of the moon's orbit respootively rcgrcss and advance continually. The terms which change proportionally to $\pmb { \ell }$ nrc called secular terms.

The right mombers of cquations (10) also contain periodic terms having tho periods and $\frac { 2 \pi } { l - k }$ These are known as periodic lerms. If land h are noarly equal the terms which involvo sines or cogines of (l-k)t have very long periods,and are called long period lerms, Sometimes torms arise which are the products of l and poriodic torms. These mixed terms are called Poisson terins bocauso thoy wero cncountered by Poisson in the discussion of the variations of thc major axes of the planetary orbits. If (10) are substitutcd in (b) tho resulting expressions for x1 and x2 contain Poisson terms but no secular terms.

The physical interprotation of cquations (1O) is simple. The elements α and β continually decrease because of the secular terms; that is,tho gmplitudeg of the oscillations indicated in (5） continually diminish. This reduction is entirely due to the resistance to the motion as is shown by the fact that these terms contain the ttettwunt nun fuotTur Ho tn r nmt to jurod tt nnl h uhtmn n wih m alo l trl:u\l tli nlt thdulmmy tet mt dutmrmud tmpwiuutm l t u rnai gdfmbog hennl n t thrnmal prusl ftlaiuutg frhBut it intd imt Iu to tw totwlr tuy intxlute iut tlt.pon for.,nul .,nt I atl .f tlu dutuhng for m t mnturn ui of tung touh

205.Equntlons i the Problen of Three Bodie.' er unoumafwnpn4.man m,wih .:l.t." Tnheiunter of temmn og tut h1 ttmdmtf m lm(r nl. ntl nf m、（.\~）l1 tt tn uf mx a mg from lh sit I .. nml tt smt.m ltt 7. v rgr Hnt tlitnufon mtm.Tuntthfenml.qtt mom,nderivrmAr！X,nr

$$
\begin{array} { r l } & { \begin{array} { r l } { ( - I ^ { T } \ell _ { 4 } ) } & { 1 \ell ^ { T } ( \ell _ { 4 } ) } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { = \begin{array} { r l } { ( 1 - I ^ { T } \ell _ { 4 } ) } & { ( 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 1 } ) ^ { T } \ell _ { 1 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 1 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 1 } , } \\ { i \ell ^ { T } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 2 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 2 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 1 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { = \begin{array} { r l } { ( 1 - I ^ { T } \ell _ { 4 } ) } & { ( 1 \ell ^ { T } \ell _ { 4 } ) \ell _ { 2 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 4 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 3 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 4 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 4 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 4 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 4 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \\ & { \begin{array} { r l } { i \ell _ { 4 } } & { 1 \ell ^ { T } ( \ell _ { 4 } ) \ell _ { 2 } , } \\ { i \ell ^ { T } } & { 1 } \end{array} } \end{array}
$$

Thright mmr of unio（1）nr trl the faeturk m nu mwhie nr very nml rrrd tuStrefore they wi l of rght nmrnin umrin with t tm on tf wnel rmfron tnitrartim of thesnnt lnt for AconiderabimIf $m _ { 1 }$ mm $m _ { 1 } , _ { \tt S }$ nmun Lg xr n the right mm, ho rt thr ution nnd hn eml thre foim two sets which aie independent of each other，and the pioblem for each set of thee equations reduces to that of two bodies,and can be completely solved

It will bc advantageous to icduce the six equations (11) of the second ordel to twelve of the frst oiderLet

$$
\mathfrak { a } ^ { \prime } = \frac { d \mathfrak { r } } { d t } , \qquad \mathfrak { y } ^ { \prime } = \frac { d \mathfrak { y } } { d t } , \qquad \mathfrak { z } ^ { \prime } = \frac { d \mathfrak { z } } { d t } ,
$$

thon cquations (11) become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d t } - { \it z } _ { 1 } \mathrm { ' } = 0 , } & { \quad \displaystyle \frac { d x _ { 1 } \mathrm { ' } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } \mathrm { ' } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 1 } } , } \\ { \displaystyle \frac { d y _ { 1 } } { d t } - y _ { 1 } \mathrm { ' } = 0 , } & { \quad \displaystyle \frac { d y _ { 1 } \mathrm { ' } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { y _ { 1 } } { r _ { 1 } \mathrm { ' } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y _ { 1 } } , } \\ { \displaystyle \frac { d z _ { 1 } } { d t } - z _ { 1 } \mathrm { ' } = 0 , } & { \quad \displaystyle \frac { d z _ { 1 } \mathrm { ' } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { z _ { 1 } } { r _ { 1 } \mathrm { ' } } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 1 } } , } \end{array} \right.
$$

and similai cquations in which the subsciipt is 2.

If tho molions of $\boldsymbol { \mathscr { m } } _ { 1 }$ and $\pmb { m _ { 2 } }$ were not distuibed by each other equalions (12) would become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d x _ { 1 } } { d l } - x _ { 1 } { ' } = 0 , \quad } & { \displaystyle \frac { d x _ { 1 } { ' } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } = 0 , } \\ { \displaystyle \frac { d y _ { 1 } } { d l } - y _ { 1 } { ' } = 0 , \quad } & { \displaystyle \frac { d y _ { 1 } { ' } } { d l } + k ^ { 2 } ( S + m _ { 1 } ) \frac { y _ { 1 } } { r _ { 1 } ^ { 3 } } = 0 , } \\ { \displaystyle \frac { d z _ { 1 } } { d l } - z _ { 1 } { ' } = 0 , \quad } & { \displaystyle \frac { d z _ { 1 } { ' } } { d t } + k ^ { 2 } ( S + m _ { 1 } ) \frac { z _ { 1 } } { r _ { 1 } ^ { 3 } } = 0 , } \end{array} \right.
$$

and an indepondent systcm of similar cquations in which the Bubserpt is 2. Let S=(x+y²+z）-²(S+m）， ihon cqualions (13) take the form

$$
\begin{array} { r l } { \left\{ \begin{array} { l l } { \displaystyle \frac { d \mathfrak { u } _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial \mathfrak { x } _ { 1 } ^ { \prime } } , \quad } & { \displaystyle \frac { d \mathfrak { u } _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { \partial \mathfrak { x } _ { 1 } } , } \\ { \displaystyle \frac { d \mathfrak { u } _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial \mathfrak { y } _ { 1 } ^ { \prime } } , \quad } & { \displaystyle \frac { d \mathfrak { y } _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { d \mathfrak { y } _ { 1 } } , } \\ { \displaystyle \frac { d \mathfrak { z } _ { 1 } } { d t } = \frac { \partial \Omega _ { 1 } } { \partial \mathfrak { z } _ { 1 } ^ { \prime } } , \quad } & { \displaystyle \frac { d \mathfrak { z } _ { 1 } ^ { \prime } } { d t } = - \frac { \partial \Omega _ { 1 } } { \partial \mathfrak { z } _ { 1 } } , } \end{array} \right. } \end{array}
$$

This form of the differential equations is convenient in connection with tho problem of transforming equations so that the ellptie emnt lon tl depemt vaable whoe vatue  ert oftme lequned.

206.Trnsformntion of VarlabloB.In mdertu avod onfuion m the nuulyn,d to b nlte to mny wher nnd how t nppoi mtum ne utuettmol of tvnmtmn ofpmrnm peA mn e gardel m tlt fiat msnne n timply n ttnii fommlton of vaallen,whieh P perfeeily lextmmnte fo nll val o t tm for wleh the eguatios of tnfomtton ue vuhel. From thinpomt.of vi te wlol pruet  pntlumnttenll nmp ml lue,t oly ttouble immg fton the mmnnr of vanblen nvolve nnd tu onplte elntto nnogm

In ehnpter v.it w Hhown low to tme tle endmnte m Proben of Two Bxlien m trm of the elemrntn nni ihe line.Let tx, :.,ra ieprenent lhe clementn of thr mlnt m1 nnlp.Ha thomof mThen tluemattmn for t cordumten m tln Piolkn of Two Bolie nny bo written

$$
\begin{array} { r }  \{ \begin{array} { l l } { \varepsilon _ { 1 } , \quad \varsigma ( \sigma _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \it ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \psi ~ } ) , } & { \quad { x } _ { 1 } ^ { \prime } , \quad \vartheta ( \sigma _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \ell ~ } ) , } \\ { \eta _ { 1 } , \quad \varsigma _ { 1 } , ( \sigma ( { \sigma } _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \psi ~ } ) , } & { \quad \eta _ { 1 } ^ { \prime } , \quad \mathrm {  ~ \cdot ~ } \phi ( { \sigma } _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \psi ~ } _ { 0 } , \mathrm {  ~ \ell ~ } ) , } \\ { \varepsilon _ { 1 } , \quad \varsigma _ { 1 } , \quad h ( \sigma _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \psi ~ } ) , } & { \quad \Xi _ { 1 } ^ { \prime } , \quad \psi ( { \sigma } _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \psi ~ } _ { 0 } , \mathrm {  ~ \ell ~ } ) , } \\ { \quad \quad \cdot \sigma _ { 2 } , \quad \varsigma ( \tilde { \mu } _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \psi ~ } ) , } & { \quad { x } _ { 2 } ^ { \prime } , \quad \sigma _ { 1 } ( \beta _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \beta ~ } _ { 0 } , \mathrm {  ~ \ell ~ } ) , } \\ { \quad \quad \cdot \eta _ { 1 } , \quad \cdot \langle \tilde { \mu } _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \gamma ~ } _ { 0 } , \mathrm {  ~ \gamma ~ } \rangle , } & { \quad \eta _ { 1 } ^ { \prime } , \quad \cdot \mathrm {  ~ \cdot ~ } \phi ( \beta _ { 1 } , \mathrm {  ~ \cdots ~ } , \mathrm {  ~ \beta ~ } _ { 0 } , \mathrm {  ~ \ell ~ } ) , } \\  \varepsilon _ { 1 } , \quad \cdot \ h ( \tilde { \beta } _ { 1 } , \mathrm    \end{array} \end{array}
$$

$\pmb { \Lambda }$ trannformtion of vnriallrn m untionn （i2）wil now lttmle.Lot nt bn forgotten for t momnt thnt mqtationn（ls）aroho molutionn of  Poblem of Two Btdir,nnd that t$\mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha } \mathbf { \alpha \alpha \alpha } \mathbf { \alpha \alpha \alpha \beta \alpha \mathbf \alpha } \mathbf  \alpha \alpha \alpha \alpha \alpha \beta \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \beta \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \mathbf \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \alpha \ c o \alpha \ c o \ c o \ c o \ c o \ c o \ c o \ c o \ c o \ c o \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r \ c o r a \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r a n \ c o r$ mm $\beta _ { i }$ nrtl clomrnta of he wo obitx;hut r（l） tntonmered n being tho ualionn wluh tranforn quntiong（i） into old vuinblen $r _ { 1 } , i _ { 1 } , i _ { 1 } , i _ { 1 } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 1 } , i _ { 1 } , i _ { 1 } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 1 } ^ { \prime } , i _ { 2 } ^ { \prime } , i _ { 2 } ^ { \prime } ,$ jtonuivniet yslem  he new vntiables $( \Upsilon _ { 1 } , \quad \cdots , \Upsilon _ { n } , / \} _ { 1 } ,$ ：，Thn tiannformntionn are ceeted by onputing te drivntiveocourrng m （l2） nnd mnking dneet sulntiutonTh drivnven of cquntion（lo） wih teniet lol nrg

$$
\begin{array}{c} \begin{array} { r } { \{ \begin{array} { l l } { d t _ { 1 } } & { \mathrm { i } \Omega _ { 1 } } \\ { d t } & { \mathrm { i } \Omega _ { \ell } } \end{array}  \{ \begin{array} { l l } { \sum _ { i = 1 } ^ { 6 } \mathrm { i } \partial x _ { i } \ d t _ { \ell } } \\ { \sum _ { i = 1 } ^ { 6 } \mathrm { i } \partial x _ { i } \ \cdot d t _ { \ell } } \end{array}  , } \\ { \cdot \begin{array} { r } { \cdot \cdot \cdot \cdot \ \cdot } \\ { d t _ { 1 } \cdot \ \cdot } \\ { d t _ { \ell } } \end{array}  \partial _ { i } x _ { 1 } ^ { \prime } \ } \\ { \{ \begin{array} { l l } { d t } & { \mathrm { i } \Omega _ { \ell } } \\ { \cdot \cdot \cdot } \\ { \cdot \cdot } \end{array}  \partial t \ \cdot \{ \begin{array} { l l } { \frac { b } { \ell } \cdot \widehat { \mathrm { i } } \partial x _ { 1 } \ \cdot \widehat { \mathrm { i } } ^ { \ell } \ d t _ { \ell } } \\ { \cdot \cdot \cdot \cdot } \\ { \cdot \cdot } \end{array}  \ } \end{array}   \end{array}
$$

The dircct substitution of (16) m (12) gives

$$
\begin{array} { r } { [ \begin{array} { l } { \frac { \partial \tau _ { 1 } } { \partial l } - \alpha _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } \alpha _ { 1 } , } \\ { \frac { \partial \tau _ { 1 } } { \partial l } - \gamma _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } - 0 , } \\ { \frac { \partial \tau _ { 1 } } { \partial l } - \gamma _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } - 0 , } \\ { \frac { \partial \tau _ { 1 } } { \partial l } - \alpha _ { 1 } ^ { \prime } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } - 0 , } \end{array} ] _ { \frac { \partial \tau _ { 1 } } { \partial l } } \frac { \partial \tau _ { 1 } } { \partial l } , } \\  [ \begin{array} { l } { \frac { \partial \tau _ { 1 } } { \partial l } + k ^ { 2 } ( S + m ) \frac { \tau _ { 1 } } { \gamma _ { 1 } ^ { 2 } } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 1 } } , } \\ { \frac { \partial \tau _ { 1 } } { \partial l } + k ^ { 2 } ( S + m ) \frac { \tau _ { 1 } } { \gamma _ { 1 } ^ { 2 } } + \frac { \delta } { 2 } \frac { \partial \tau _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \tau _ { 1 } } { \partial l } - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \gamma _ { 1 } } , } \\  \frac { \partial \tau _ { 1 } } { \partial l } + k ^ { 2 } ( S + m ) \frac { \tau _ { 1 } } { \gamma _ { 1 } ^ { 2 } } + \frac { \delta } { 2 } \frac  \partial \tau _ { 1 } ^ \end{array} \end{array}
$$

and similar equations in ${ \mathfrak { R } } _ { 2 } , \cdots , { z } _ { 2 } { } ^ { \prime } , \operatorname { a n d } \ \beta _ { 1 } ,$ ， $\beta _ { \emptyset }$ These equations aro linonr in the dorvatives $\frac { d \alpha _ { * } } { d t }$ and can be solved for them,expressing them in terms of $\pmb { \alpha _ { 1 } } ,$ ：， $\alpha _ { \mathfrak { G } } , \beta _ { \mathfrak { l } } ,$ ：， $\beta _ { 8 } ,$ and $t ,$ provided the determinant of thcir cocfficients is distinct from zero

Bul if cquations (15) are the solution of the problem of undisturbed clhptie motion cquations (17) are greatly simplfied, for it is scon from (13) that,when $\alpha _ { 1 } , ~ \cdot ~ , ~ \alpha _ { 0 }$ are constant, $\frac { \langle \mathcal { l } \mathfrak { v } _ { 1 } } { \bar { d } \mathfrak { l } } - \mathfrak { a } _ { 1 } ^ { \prime } = 0$ forllert $\frac { \partial x _ { 1 } } { \partial t }$ ， whon $\alpha _ { 1 } , \ldots , \alpha _ { 0 }$ are icgarded as variables,1s identical with $\frac { d x _ { 1 } } { d t }$ when thoy aroregarcodasconstantsTherefoe $\frac { \partial { \boldsymbol { \mathfrak { x } } } _ { 1 } } { \partial t } - { \boldsymbol { \mathfrak { x } } } _ { 1 } ^ { \prime } \equiv 0 ,$ and similarly $\frac { \partial { x _ { 1 } } ^ { \prime } } { \partial l } + k ^ { 2 } ( S + m _ { 1 } ) \frac { x _ { 1 } } { r _ { 1 } ^ { 3 } } \equiv 0 ,$ and similar equations n V and z. As a conscquenco of these relations equations (17) rcduco to

$$
\begin{array} { r l } { \mathrm { ~  ~ \gamma ~ } } & { \left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { 1 } } { d \ell } = 0 , \quad } & { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial x _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { d \alpha _ { 1 } } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \lambda _ { 1 } } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial y _ { 1 } } { \partial \alpha _ { i } } \frac { d \alpha _ { 1 } } { d \ell } = 0 , \quad } & { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial y _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { d \alpha } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y _ { 1 } } , } \end{array} \right. } \\ & { \left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial z _ { 1 } } { \partial \alpha _ { 1 } } \frac { d \alpha _ { 1 } } { d \ell } = 0 , \quad } & { \displaystyle \sum _ { i = 1 } ^ { 6 } \frac { \partial z _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { d \alpha _ { 1 } } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 1 } } , } \end{array} \right. } \end{array}
$$

and similar equations in the β. These cquations are lnear in the doivntiv $\begin{array} { c } { { t h \thinspace \thinspace , } } \\ { { \nmid t \thinspace , } } \end{array}$ mdran be bolvrd fou them nnte u deteninant of ther eoelieens pi zmoBut tlur detntmnd of nvtem（x）t the daolmn of tle tunt set of tquatot（i）with peet to maul emot vam t tuefumu ne mdepenenl mul ge n Huple nm mqe ttetemim o tl cloentu.\*T't fumt ltor ne depmdent,ml t yetal lh vo Huple nu mmqte vul fo t eement mme t me t itoin for tho rommt m th 'mtdem nt Tw Hol Theptoble of tetemmmg the eent fom tnb .of ih coottntey m rompmen of rtwnn tal m ehp

Img"0 eqnito（l）me hn mu toog unm to detemmant mnot /eo tley ean h mtmkt o by $\begin{array} { c c } { { 1 2 0 0 , } } & { { } } \\ { { 1 1 1 } } & { { } } \end{array} 1 1 ,$ （1,,0)Tmt n, l elemeut me tntntantu, wlneh, of

On Bolvmg ommtkm（18）,iti foml thl

$$
\left\{ \begin{array} { l l } { d i v _ { i } } & { m _ { 2 } \psi _ { i } \left( \boldsymbol { r } _ { 1 } , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \psi _ { 0 } , \beta _ { 1 } , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \beta _ { 0 } , l \right) , \mathrm { ~  ~ { ~ \gamma ~ } ~ } \left( \boldsymbol { r } \mid - 1 , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \uparrow \right) , } \\ { d i J _ { i } } & { , } \\ { d l } & { , \quad m _ { 1 } \psi _ { i } \left( \boldsymbol { r } \psi _ { 1 } , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \psi _ { 0 } ; \beta _ { 1 } , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \beta _ { 0 } ; l \right) , \mathrm { ~  ~ { ~ \gamma ~ } ~ } \left( \boldsymbol { r } \cdot 1 , \mathrm { ~  ~ { ~ \gamma ~ } ~ } , \parallel \right) . } \end{array} \right.
$$

I wl b tenpt th it detemnng  nntm hPoblem ofTwo itlen ihan ntpvi,Iu.ommtntonof Lle menn nnomnly, involved te menn moton, dehmrt by the equntion

$$
u _ { 1 } \quad , h \downarrow \downarrow \downarrow m _ { I } , \qquad ( \jmath \cdot + 1 , / ) ,
$$

Hinee the ${ \boldsymbol { n } } _ { \boldsymbol { \imath } }$ iuvolve t ma of tluplnmta ll tight mnr of（b),amd eequently qf （），mvoive m nt $m _ { \parallel }$ mplimtly.

In oderto mtfy mntlumttelly h mcenetl of mt gratmg equnttonn （i） wielt 1 ployel hy ntotenr,m 1emarkn iu nomry upo mt  ml thom pla wiute thoy oeeur mpketly m h furtt  md  teyWll eguded u fil men，n try mprt fm f thr ml $\pmb { \varphi } _ { \pmb { \ell } }$ Htvey tluy w Itrdt n pnranrter  wrra of whieh th olutton may be xpnndkd.Murh  prnhatin of prnte N culv rmh lnu,fn fneto nvolve Apramerr m two dfeent wny, here IN no tenon why it mny nol be expanded with 1espeet to the parameter so far as it 1s involved in ono way and not with respeet to It as it is involved in the otherIf the function, instead of being given explcitly,is defincd by a set of difleiential equations the same things regarding thc expansiong in teims of palameters aie trueIf the attiactions of bodies depended on something besides thel masses (measured by lheir imertias) and their distances,ag for example, on their rates of 1otalion o tempeiatures, then $m _ { 1 }$ and $m _ { 2 }$ so fai as they enter in thc $\varphi _ { \ell }$ and $\psi _ { \cdot }$ imphcitly thnough $\pmb { n } _ { 1 }$ and $\scriptstyle n _ { 2 } ,$ where they would be defincd numeiically by their individual mutual attractions for the sun,would be different from their values where they oceur as factors of the $\varphi _ { \imath }$ and $\psi _ { \pmb { \imath } }$ ， for in the latter places they would be defined by their attractions for each other

Henco, the values of the masses $\mathbf { \boldsymbol { m } } _ { \mathbf { \ell } }$ and $\mathbf { \nabla } m _ { 2 }$ entering implcitly m cquations (15) and (19) are treated as fixed numbers,given in advancc, and do not need to be retained explcitly；on the other hand, thc $\pmb { m } _ { \pmb { 1 } }$ and $m _ { 2 }$ which are factors of the pertuibing terms of the cquations are retained explicitly, being supposed capable of takng any valucs not exceeding certain limits.

207.Méthod of Solutlon. Equations (11） are the general diferential cquations of motion for the Problem of Three Bodies Equations (12) are equally general. No approximations were inlroduced m making thc transfoimation of variables by (15), theicforo cquations (19) aie general and rigorousThe difference is that if (19) wele integrated the elements would be found instead of thc cobrdinates as in (11)，but as the latter can always be founrl from tho former this must be regarded as the solution of the problem.

Instead of intcrrupting the course of mathematical reasoning by working oul tho cxpleil foims of (19),it will be preferable to show fist by whut methods they aie solved Explicit mention will be mado at tho appiopriate times of all points at which assumptaons or apmoximationg ae made.

When mi and mz are very small compared to S,as they are in tho Bolar system， the orhits are very nearly fixcd ellpses,and thcroforo α and B,chango very slowly Consequently if they wele lcgaidcd as constanls in the lght members of (19) and the cqualons integrated, appioximate values of the α. and the β, would be obtained fon values of t not too iemote fiom the initial timcThs is the method adopled in the ilustrative example of thepeedng nttee,nnd lu lwp ttue potnt of vew often taken by mfionpm,utlm lh pomer ny of（ dal MeehanteBnt nn(eowheh ii oulv nyuotnnter houph itv muaenllndeat, totmot nunue np to t enn of mtowe

Equntou（o） me of th(ype whl（nuehs nt Pmme lnve Htown ci l ntepintel a powe Mn m m nnt $m _ { \lambda }$ （uely poved ut $m _ { 1 } , m _ { 2 } ,$ nl7rnn nll Ie tnken  moll mt tt conveigePomme jnoved te moe pmial ltolt $1 1 1 ^ { * }$ tif the otbit in whteh e hodt atmnttnwol mvng nt th mtinl tme do not mlet,ten fo n tmte tage of valua of t,th  mm $m _ { \mathbb { Z } }$ canlenken ml thtftl oo conveige tor rvry vaine of $1$ m the mtmvnlHower. lhe mneH euunol e chrtn nlat:nly am Imt mrgvn by Natmo.Hene. the prnefieal impotnm tf l nelitul ttt oren tlul, whatpvei ihe snlue nf $m _ { 1 }$ $m _ { k _ { 1 } }$ twe nt n tmige forRo tetetedl thnt the Holntom of cnttons （in） n finwer Heie n topnmeton $m _ { 1 }$ mm $m \mathfrak { g }$ eonvetge fu evrv vai of/m tho rangoln gerd, th lgr the viuen of tt pnten ho noro eeied lhe angT $\mathbf { \mu } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf { \mu } } _ { \mathbf \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mathbf } { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu }  _ _ { { \mu \mu } } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } _ { \mu } { \mu } _ { \mu } _ { \mu } \mu _ { } \mu \mu \mu { } _ \mu { } \mu \mu  _ { \mu \mu } _ { \mu \mu } _ { \mu \mu } { \mu } _ { \mu \mu } \mu { \mu \mu } \mu _ { \mu } \mu \mu { } \mu \mu \mu \mu { } \mu \mu \mu \mu \mu \mu  { \mu \mu \mu } { \mu \mu \mu \mu \mu \mu } \mu { \mu \mu \mu \mu } \mu \mu \mu \mu \mu \mu \mu { } \mu \mu \mu \mu \mu \mu \mu \mu \mu \mu \mu \mu \mu  \mu \mu \mu \mu \mu \mu \ u \ u $ nfrtnmnlcnf B geernl lwoe topeeting l 'pumdon of moutta of hm entnl equaton of th tvpe to which （lu） lrlong n Jnwer reu4 m pnrnmeter t

Ifoikw on th inut oen quoted tlat,fte range ofin nottoo gent,tle noluton of ution（l）cnm bt cxpred in convorgont power Herie in $m _ { 1 }$ $m _ { \lambda ) }$ oftlue form

$$
\begin{array} { r }  \{ \begin{array} { l l } { ( v _ { l } \cdot v _ { \ell } ) ^ { n } \rule { 0 ex } { 5 ex } \} _ { 0 } ^ { n } \sum _ { 6 } ^ { n } ( \gamma _ { \ell } ^ { \ell j _ { \ell } k _ { 1 } } m _ { l } ^ { j _ { l l } } m _ { l } ^ { k _ { 1 } } ) } \\ { \beta _ { \ell } ^ { \ell } \cdot \{ \begin{array} { l l } { \beta _ { \ell } ^ { \ell } \sum _ { \ell = 0 } ^ { m } \beta _ { \ell } ^ { \ell } ( \ell ^ { j _ { \ell } k _ { 1 } } m _ { l } ^ { j _ { l l } } m _ { l } ^ { k _ { 1 } } , } \\ { \beta _ { \ell } ^ { \ell } \cdot \ell ^ { \ell } \end{array}  } \end{array}  } \end{array}
$$

whoro thoupmfxes on tt $t ( t _ { 1 }$ ml $\beta _ { 0 }$ rimply muliente t ordernf ho cofliientTe $v ( \beta , \lambda )$ $1 1 _ { 1 } ^ { t 1 , 2 1 }$ Rrenetomf tine whieh are to l dotermued.I n I n cutumry in tmtory ofperurbnlion to nxune without prof tnt thin expunin in valid for y deuired longth of tu.An hn lo nfntri,it cn ln pioved Ihal i i vald fo n nuflieiently mmnl intervnl nf time but nn the metlol of deonomttntion give uniy a limit witton which tho merien crtnly eonverge, and not th longrt timn

Mhten Nortadrln Meanqun ttrntrvul 1pt. HeoPwardu TratedAnalye,voln,enp xid vol m duing which they conveige,and as the hmit is almost certainly far too small,it has never been computedIt is to be understood, thclefoic, that thc method which Is just to be explamed,is vahd for ${ \mathfrak { a } }$ ceitain intcival of timc,which in the planetary theories 1s doubtless seveial hundreds of years

On substituting (20) m (19) and developing with respect to $\pmb { m } _ { \pmb { 1 } }$ and ${ \mathcal { m } } _ { \mathfrak { L } } ,$ it is found that

$$
\begin{array} { r l } {  { \{ \frac { d \alpha _ { 1 } \mathfrak { o } _ { 1 } \mathfrak { o } _ { 0 } } { d t } + \frac { d \alpha _ { 1 } \mathfrak { o } _ { 1 } \mathfrak { o } _ { 1 } } { d t } m _ { 2 } + \frac { d \alpha _ { 1 } \mathfrak { o } _ { 1 } \mathfrak { o } _ { 1 } } { d t } m _ { 1 } + \frac { d \alpha _ { 1 } \mathfrak { o } _ { 1 } \mathfrak { o } _ { 1 } } { d t } m _ { 1 } m _ { 2 }  } } \quad  & { } \\ & {  \vphantom { m m m _ { 2 } \mathfrak { o } _ { 1 } } { + \frac { d \alpha _ { 1 } \mathfrak { o } _ { 2 } \mathfrak { o } _ { 2 } } { d t } m _ { 2 } \mathfrak { z } + \frac { d \alpha _ { 1 } \mathfrak { o } _ { 2 } \mathfrak { o } _ { 3 } } { d t } m _ { 1 } \mathfrak { z } + \mathfrak { c } }  } \\ & { = \operatorname* { m } _ { 2 } \mathfrak { p } _ { \mathfrak { o } } ( \alpha _ { 1 } \mathfrak { o } _ { 0 } , \mathfrak { o } , \mathfrak { \alpha } , \mathfrak { \alpha } , \mathfrak { o } _ { 6 } \mathfrak { o } , \mathfrak { \alpha } , \mathfrak { \alpha } , \mathfrak { \alpha } , \mathfrak { \beta } _ { 6 } \mathfrak { o } , \mathfrak { \alpha } ) } \\ & { \quad +  m _ { 2 } \frac { \mathfrak { s } } { \partial \mathfrak { o } _ { 2 } } \frac { \partial \mathfrak { d } _ { \mathfrak { s } } } { \partial \mathfrak { \alpha } _ { 2 } } ( \alpha _ { 2 } \mathfrak { o } _ { 1 } \mathfrak { n } _ { 2 } + \alpha _ { 2 } \mathfrak { o } _ { 1 } \mathfrak { n } _ { 1 } )  } \\ &  \quad  \vphantom { m m m _ { 2 } \mathfrak { p } _ { \mathfrak { o } } } { +  \frac { \mathrm { d } \mathfrak { s } } { \partial \mathfrak { p } _ { \mathfrak { o } } } } { \partial \mathfrak { \alpha } _ { 1 } \mathfrak { o } _ { 2 } \mathfrak { o } _ { 1 } } { \partial \mathfrak { z } _ { 2 } } { +  \frac { \mathrm { d } \mathfrak { s } } { \partial \mathfrak { s } _ { 2 } \mathfrak { o } _ { 1 } } { \partial \mathfrak { s } _ { 2 } } | \mathfrak { z } _ { 1 } \mathfrak { o } _ { 2 } \mathfrak { s } _ { 3 } \mathfrak { n } _ { 3 } \} } \end{array}
$$

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \begin{array} { r l } & { \mathrm { ~ + ~ h q b o r ~ p o w e r 1 s ~ i n ~ m i n ~ m a d ~ m _ 3 , } } \\ { \displaystyle \frac { d \beta _ { 1 } ( \theta _ { 0 } , \theta _ { 0 } ) } { d t } + \frac { d \beta _ { 0 } ( \theta _ { 1 } , \theta _ { 1 } ) } { d t } m _ { \alpha } + \frac { d \beta _ { 1 } ( \theta _ { 1 } , \theta _ { 1 } ) } { d t } m _ { 1 } + \frac { d \beta _ { 0 } ( \theta _ { 1 } , \theta _ { 1 } ) } { d t } m _ { 1 } m _ { 2 } } \end{array} } \\ { \begin{array} { r l } & { \mathrm { ~ + ~ } \frac { d \beta _ { 0 } ( \theta _ { 0 } , \theta _ { 0 } ) } { d t } m _ { 2 } + \frac { d \beta _ { 1 } ( \theta _ { 1 } , \theta _ { 0 } ) } { d t } m _ { 1 } ^ { 2 } + ~ . } \\ & { \mathrm { ~ - ~ } m _ { 1 } \eta _ { * } ^ { \prime } ( \alpha _ { 1 } 0 , \theta _ { 0 } ) ~ , ~ . ~ } \end{array} } \\ { \begin{array} { r l } & { \mathrm { ~ + ~ } m _ { 1 } \frac { \beta _ { 1 } } { \beta _ { 2 } \mathrm { i n } } \frac { \partial \beta _ { 1 } } { \partial \alpha _ { 2 } } ( \theta _ { 0 } , \theta _ { 1 } ) m _ { 2 } + \alpha _ { 1 } ( \theta _ { 1 } , \theta _ { 1 } ) } \\ & { \mathrm { ~ + ~ } m _ { 1 } \frac { \beta _ { 2 } } { \beta _ { 1 } \mathrm { i n } } \frac { \partial \beta _ { 2 } } { \partial \beta _ { 1 } } ( \theta _ { 0 } , 0 , m _ { 2 } ) } \end{array} } \end{array} \right. , } \end{array}
$$

In tho partial derivativeg it is to be understood that αi and βtare rcplaced by α(o,o) and β.(.o) respectively If m1 and mz were nol regarded as fixed numbers in the left members of equatons (11), $\phi _ { i } , \phi _ { i } , \frac { \partial \phi _ { i } } { \partial \alpha _ { i } } , \frac { \partial \phi _ { i } } { \partial \beta _ { j } }$ etcoudetedeeooer te.mmt $m _ { d } ,$ tu abp gaflto tunpktf iht wk

Wnn tle hmt tof rovciprp tnfnbnt.of hkuwt $m _ { 1 }$ ul $m$ tt lwo tt .of the eqotmp ue ul nmg tt folltw th

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \end{array} \begin{array} { r l } { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \end{array} \begin{array} { r l } & { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \\ { \mathrm { i n } } \end{array} \end{array}
$$

Onmtegraling qntton 2） nm nuitntng the nnf $\alpha _ { 1 } \eta _ { 0 } , \theta ]$ m $\smash { \{ \beta _ { 1 } ^ { ( 1 ) , \{ 1 \} } \} }$ thn tnid n 2the ntter nr r qundratne nn cm  ntegaeron intepnting （2）nnd nt Htttutng th exprmox for $i \in \{ 1 , \ 1 \} , \ o x _ { 4 } ^ { \{ 1 , n _ { i } \} } , \beta _ { i } ^ { \{ 0 , \ 1 \} } , \beta _ { i } ^ { \{ 1 , n _ { i } \} }$ in 121, the nter  ued to iurnmre nnd an h mgrnt nd tu proe can t ontmed mleintey.In tnn m the coeficients of the_series (20) can be determined,and the values of ${ \pmb { \alpha } } _ { \pmb { \nu } }$ and $\beta _ { \imath }$ can be found to any desned degree of precision for values of tho time fol which the seiies converge

208.Determination of the Constants of Integration. A new constant of mtegialion 15 intioduced whcn equatiops (22), (23), me mlegraled for cach $\alpha _ { 1 } ( \ i , \hbar )$ ， $\beta _ { \bullet } ( \iota , \hbar )$ These constants will now be determmed

Let thc constant which is intioduced with the $\alpha _ { 4 } ( \pmb { \mathscr { s } } , \pmb { \mathscr { k } } )$ be denoted $\mathrm { b y } \ - \ a _ { 1 } ( \Omega ^ { \textit { h } } )$ und with tho $\beta _ { \ast } ( \pmb { \imath } ^ { \textit { t } } )$ ， ${ \mathfrak { b y } } - { \mathfrak { b } } _ { \mathfrak { s } } ( \colon ^ { 1 ) } \ { } ^ { \mathfrak { s } } )$ Since the fist set of difteicntial cqualions have $\mathfrak { M } \mathfrak { a }$ as a factol in then right members, whilo the second sel have $m _ { 1 }$ as a factor,it follows that

$$
\begin{array} { c l c r } { { \alpha _ { \mathfrak { s } } ^ { ( \eta , 0 ) } = a _ { \mathfrak { t } } { } ^ { ( \eta , 0 ) } , \quad } } & { { ( \jmath = 0 , \quad } } & { { \infty ) , } } \\ { { \beta _ { \mathfrak { s } } ^ { ( 0 , k ) } = b _ { \mathfrak { t } } { } ^ { ( 0 , k ) } , \quad } } & { { ( \bar { h } = 0 , \quad } } & { { \infty ) } } \end{array}
$$

Since thc $\alpha _ { \bullet } ( \pmb { \imath } , \hbar )$ and $\beta _ { \cdot } ( \cdot \mathbf { \delta } ^ { k ) }$ aie defined by quadratures all the conslanls of mtegiation aic simply added to fumctions of t That 18,tho $\alpha _ { \bullet } ( \iota , \lambda )$ and $\beta _ { \cdot } ^ { \cdot ( \cdot , \lambda ) }$ have the foim

$$
\left\{ \begin{array} { l l } { \alpha _ { \mathfrak { t } } { } ^ { ( \ i , k ) } = \int _ { \mathfrak { t } } ( \ i , k ) ( t ) - a _ { \mathfrak { t } } { } ^ { ( \ i , k ) } , } \\ { \beta _ { \mathfrak { t } } { } ^ { ( \ i , k ) } = \ g _ { \mathfrak { t } } { } ^ { ( \ i , k ) } ( t ) - b _ { \mathfrak { t } } { } ^ { ( \ i , k ) } } \end{array} \right.
$$

Thereforo cquations (20) become

$$
\begin{array} { r } { \left\{ \alpha _ { 4 } = \displaystyle \sum _ { j = 0 } ^ { \infty } a _ { 4 } ^ { ( \imath , 0 ) } m _ { 1 ^ { \prime } } + \displaystyle \sum _ { j = 0 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \big ( f _ { * } ( \imath , k ) - a _ { * } ^ { ( \imath , k ) } \big ) m _ { 1 } \imath \eta _ { 2 } k , \right. } \\ { \left\{ \beta _ { * } = \displaystyle \sum _ { k = 0 } ^ { \infty } b _ { * } ^ { ( 0 , k ) } m _ { 2 } \imath + \displaystyle \sum _ { j = 1 } ^ { \infty } \sum _ { k = 0 } ^ { \infty } \big ( g _ { i } ( \imath , k ) - b _ { * } ^ { ( \imath , k ) } \big ) m _ { 1 } \imath \eta _ { 2 } k \right. } \end{array}
$$

Lct lhe valucs of α,and β,al t = l bcα and β, respectively Then,at l= to, cquations (2b) become

$$
\begin{array}{c} \begin{array} { r } { \left\{ \alpha _ { \mathfrak { e } } ^ { ( 0 ) } = \displaystyle \sum _ { j = 0 } ^ { \infty } a _ { \mathfrak { i } } ^ { ( j , 0 ) } m _ { \mathfrak { i } } ^ { \prime } + \displaystyle \sum _ { j = 0 } ^ { \infty } \displaystyle \sum _ { k = 1 } ^ { \infty } \big ( f _ { \mathfrak { i } } ^ { ( j , k ) } - a _ { \mathfrak { i } } ^ { ( j , k ) } \big ) _ { 0 } m _ { 1 } \cdot m _ { 2 } k , \right.} \\ { \beta _ { \mathfrak { i } } ^ { ( 0 ) } = \displaystyle \sum _ { k \ne 0 } ^ { \infty } b _ { \mathfrak { i } } ^ { ( 0 , k ) } m _ { \mathfrak { i } } ^ { k } + \displaystyle \sum _ { j = 1 } ^ { \infty } \displaystyle \sum _ { k = 0 } ^ { \infty } \big ( g _ { \mathfrak { i } } ^ { ( j , k ) } - b _ { \mathfrak { i } } ^ { ( j , k ) } \big ) _ { 0 } m _ { 1 } \cdot m _ { 2 } k , } \end{array}   \end{array}
$$

Sinco lhcse cqualions must be truc for all values of mi and mz bolow cerlain limils, the coefficients of coicspondmg powers of miand mz in tho right and lefl members are cqual, whence

$$
\left\{ \begin{array} { l l } { \alpha _ { 1 } ^ { \prime ( 0 , 0 ) } = \alpha _ { 1 } ^ { ( 0 ) } , \qquad \alpha _ { \ast } ^ { ( \ i , 0 ) } = 0 , \qquad ( \ j = 1 , \cdot \quad \infty ) , } \\ { \beta _ { \ast } ^ { ( 0 , 0 ) } = \beta _ { \ast } ^ { ( 0 ) } , \qquad \beta _ { \ast } ^ { ( 0 , k ) } = 0 , \qquad ( \ j = 1 , \cdot \quad \infty ) , } \\ { \int _ { \ast } ( \ - i , k ) \big ( l _ { 0 } \big ) - a _ { \ast } ^ { ( \ i , k ) } = 0 , \qquad ( \ j = 1 , \qquad \infty ; \ j = 1 , } \\ { \qquad \big ) _ { \ast } ( \ i , k ) \big ( l _ { 0 } \big ) - b _ { \ast } ^ { ( \ i , k ) } = 0 , \qquad ( \ j = 1 , \cdot \quad \infty , \ h = 1 , } \end{array} \right.
$$

Nmee ull tu totmta thr mrht rum+ol t"1 p th tt vnub n $\ell _ { \mathfrak { d } _ { \mathfrak { r } } }$ tollow :tal "" nuq.me lu. ntng tk nt.t.totl mats of $m _ { 1 }$ m..tk i $l _ { 0 _ { 1 } }$ alttut tlut tflunnt:otcnieth tlmth mttgat ol tlnoentul eptato:wtrt d htlnttnken luween tmlumt:iuat//

200.The Terms of the rittt Oderllu ton  af tlm tn t tdr wth teqnt to llo utt .. nte tfmd le runtom.(\* Se tlp lemn of aet /etg  flu'onuattg tk tnt i nt $\ell _ { 1 1 , }$ deentmlcqnto mot

$$
\left\{ \begin{array} { l l } { d t \sigma _ { i } ^ { \mathrm { \tiny ~ t i ~ 0 } } } & { \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 0 } } , \quad \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 0 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ , ~ \psi ~ } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ / i ~ 1 } } } \\ { d t \beta _ { i } ^ { \mathrm { \tiny ~ t i ~ 0 } } } & { \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 0 } } , \quad \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } , \ \mathrm { ~ \psi ~ } _ { i } ^ { \mathrm { \tiny ~ t i ~ 1 } } } \end{array} \right.
$$

T'hpht memeofto qntonnpogntonlt tttat nt wlneh tlu nrvsal rlrno u ot Uu lnt . ol tis Iso plaset Wonld vnn nny te/.t tlu two ptmp b wrmoing at tltmi mniAnt ntetly m te ottpunml tlhp..‘l sntepinlnf .i) t, mefur,tlu amof tlvmdnntantoun re.t..,molo. w heynet mmn of rtnnp whihwoubl lmnlft for nnd tlun mrifnntno taltw.ie nlwn..ts.qunl totlow m tn plpulod .nt：o atttr gwimttnttu tolfy eo cntu nprnb mtonav，trttor.ntut lghe mter eltert4'Tluy ntr mlpbol in i t llunnt nf ligr powea of mnm m,co）

Theqmttnn rnu/omuunlbd mfuetin of llu thal ptkrwth. qut1 to thc u.；\*ti 1t nn u rbmk beeme they n th podinfstf flttpt t n in Ht（t）intluplntmthotitttmt nui Ko to itmbntior n ngn det r:g nt tt .th lgpaniwlutk ntmtnh ttundn gnuatis fow lrmn tr f cngi to lu:pbtlrt numm tmn sa.fujtetnytlumntntht.t  th tirdodecepm tomtnlmbatmof.diutn.

lfen of thee ln tmt tw ee el tqn itor ate eightplmetn nd th mtn tlt h ntou ts.ttd qate Honpe tlmtwhteh l len mfhmd.t,nwalldon tlinen ronpty cou :l lerfmsot of higtrr mtdelf e wen lhid ptm nt ld Liu nlrnu...vunn mi ht

$$
\begin{array} { r l } & { \begin{array} { r l } & { \langle \frac { d \hat { \sigma } _ { \beta \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } } - 0 , } \\ & {  \frac { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } }  ^ { 2 } } \end{array} } \\ &  \begin{array} { r l } & {  \frac { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } } - \frac { 1 } { \sqrt { 6 6 6 6 } } \langle \frac { \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } { \sqrt { 6 6 6 } } , \frac { 1 } { \sqrt { 6 6 6 } } , \frac { 1 } { \sqrt { 6 6 6 } } \rangle , } \\ &   \frac { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } } + \frac { 1 } { \sqrt { 6 6 6 } } \langle \frac { \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } } { d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } } , \frac { 1 } { \sqrt { 6 6 6 } } \rangle , \frac { d ^ { 2 } ( \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } , \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ) } \\ &   \frac  d \hat { \sigma } _ { \alpha \beta } ^ { ( 1 ) } ( \hat { \sigma } _ { \alpha \beta } \end{array} \end{array}
$$

If there wero morc planets more equations of the same type would be added. Consider lhe perturbations of the first order of tho clements of tho orbils mi, they are composed of two distinct parls given by thc second and third equations of (28),one coming fom the nlliaction of $\mathbf { \Delta } m _ { 2 } ,$ and the olher fiom the attiaction of $\pmb { m _ { 3 } }$ Thoroforo,tho statomcnt of astronomers that the perturbing effocls of thc various plancls may be consideicd sepaiately,is tiue for lho perlurbalions of tho fnst oider with respect to the masses

210.The Terms of the Second Order. It has been shown that α(1.o）= α(2,0）= β,(0,1） = β,(.2)= O； therefoie it follows fiom (24) thal the terms of thc sccond order with respect to the masses are delerimined by tho cquations

$$
\begin{array} { l } { \displaystyle \left\{ \begin{array} { l l } { \displaystyle \frac { d \alpha _ { \mathrm { t } } ( 1 , 1 ) } { d \mathcal { U } } = \sum _ { j = 1 } ^ { \emptyset } \frac { \partial \phi _ { \mathrm { t } } ( \alpha _ { 1 } ^ { ( 0 ) } , \cdots , \alpha _ { 0 } w ^ { ( 0 ) } ; \beta _ { 1 } ^ { ( 0 ) } , \cdot , \beta _ { 0 } ^ { ( 0 ) } , t ) } { \partial \beta _ { j } } \beta _ { j } ^ { ( 1 , 0 ) } , } \\ { \displaystyle \frac { d \alpha _ { \mathrm { t } } ( 0 , \cdot , 0 ) } { d \mathcal { U } } = \sum _ { j = 1 } ^ { \emptyset } \frac { \partial \phi _ { \mathrm { t } } ( \alpha _ { 1 } ^ { ( 0 ) } , \cdot \cdot \cdot , \cdot , \alpha _ { 0 } w ^ { ( 0 ) } , \beta _ { 1 } ^ { ( 0 ) } , \cdot , \cdot , \beta _ { 0 } ^ { ( 0 ) } , t ) } { \partial \alpha _ { j } } \alpha _ { l } ^ { ( 0 , 1 ) } , } \\ { \displaystyle \frac { d \beta _ { \mathrm { t } } ( 1 , 1 ) } { d \mathcal { U } } = \sum _ { j = 1 } ^ { \emptyset } \frac { \partial \psi _ { \mathrm { t } } ( \alpha _ { 1 } ^ { ( 0 ) } , \cdot \cdot \cdot , \alpha _ { 0 } w ^ { ( 0 ) } , \beta _ { 1 } ^ { ( 0 ) } , \cdot \cdot \cdot , \beta _ { 0 } ^ { ( 0 ) } , t ) } { \partial \alpha _ { j } } \alpha _ { j } ^ { ( 0 , 1 ) } , } \\ { \displaystyle \frac { d \beta _ { \mathrm { t } } ( \alpha , 0 ) } { d \mathcal { U } } = \sum _ { j = 1 } ^ { \emptyset } \frac { \partial \psi _ { \mathrm { t } } ( \alpha _ { 1 } ^ { ( 0 ) } , \cdot \cdot , \alpha _ { \mathrm { t } } ^ { ( 0 ) } ; \beta _ { 1 } ^ { ( 0 ) } , \cdot \cdot \cdot , \beta _ { 0 } ^ { ( 0 ) } ; t ) } { \partial \beta _ { l } } \beta _ { l } ^ { ( 1 , 0 ) } , } \end{array} \right. } \end{array}
$$

The peituibations of the fist ordel are those which would iesult if the distuibing forccs at evciy instant were the same as thcy would bo if the bodics weie movimg in the oliginal ellipsesIf tho bodies $m _ { 1 }$ and $\mathbf { \Delta } m _ { 2 }$ move in curves differmg from tho oiiginal cllipses tho rates at which the elements change at eveiy instant are diffeient fiom the valucs given by equations (27)The pcrtui bations of the clements of the oibit of $m _ { 1 }$ due to the fact that $\pmb { m _ { 2 } }$ depai ts fiom its original ellpse by peituibations of the first oider aie given by the equations of thc type of the fist of (29),for,if $\beta _ { \ i } ^ { \ ( 1 , 0 ) } = 0 ,$ it follows that $\alpha _ { \ast } ^ { } ( 1 , 1 ) \ \simeq \ 0$ alsoThe poiturbations of the elements of the oibit of $m _ { 1 }$ duc to lhe fact that $m _ { 1 }$ dcpal ts f1om its original ellipse by perturbations of the first order aie given by the equations of the type of the socond of (29),fol,if $\alpha _ { 1 } ^ { ( 0 , 1 ) } = 0 _ { ; }$ it follows thal $\alpha _ { \nu } ^ { ( 0 , 2 ) } = 0$ also The terms $\beta _ { \mathfrak { r } } ^ { ( 1 , \ 1 ) }$ and $\beta _ { 1 } ^ { \ ( 2 , 0 ) } \ \mathrm { m }$ the elements of the orbit of $\mathbf { m _ { 2 } }$ alise from similar causesThus tho pertuibations of the second oider coriect the enoig in the terms of the first ordei,and those of the third oider corroct the crrors in the second,and so on

As has bcen said, the solutions cxpressed as power seies in the masses converge if the interval of time is taken not too gieat In a general way, the smaller the masses of the planets the longer the time during which the series converge. In the Lunar Thcoiy the sun plays the role of the distuibing planetSimce its mass is very gleat compared to that of the central body,the earth,the serics in powers of the masses as given above would convcrgc for only $\mathfrak { a }$ veiy shoit time,probably only a few months instead of years. Such a Lunar Thooiy would be entirely unsatisfactoiy. On this account the perturbations in the Lunar Theory aro developed in powcls of the ratio of the distances of the moon and the sun from the eaith,and special artifices are cmploycd to avoid secular terms inallthe elements except the nodes and perigee.

If there Is a third planet the perturbalions of the sccond order ae consideiably moie complicatedLet tle planets be $m _ { 1 } , ~ m _ { 2 } ,$ and $\mathbf { \Delta } m _ { 3 } ,$ and consider the perturbations of the second ordei of tho elements of the oibit of m From purely physical considcrations it 1s seon that the following soits of tcrms will arise. $( a )$ terms arising from the disturbing action of $m _ { 2 }$ and $\mathbf { \Delta } m _ { 3 } ,$ due respectively to the perturbations of the first order of the clemonts of $m _ { 2 }$ and $\pmb { m } _ { 3 }$ by m1, (b) terms arising from the disturbing action of mz and ms, due to the pertubations of the frst order of the elomonts of the orbit of mi by mg and ma，(c) terms arising from the disturbing action of $m _ { 2 } ,$ due lo the perturbations of the fist order of the clementy of tho oibit of $m _ { 1 }$ by $\mathbf { \nabla } m _ { 3 }$ ， $( d )$ teims alsing from the disturlung action of ${ \mathfrak { m } } _ { 2 } ,$ duc to the perturbations of the first order of the element4 of the orbit of $m _ { 2 }$ by $\pmb { m } _ { \mathbf { 3 } }$ ,(e) teims arising from the disturbing aclion of ${ \mathfrak { M } } _ { 3 } ,$ due to the peituibationg of the fnst oder of the clementgof the obit of $\pmb { \eta } _ { \pmb { 1 } }$ by $\mathbf { \Delta } m _ { 2 }$ and $( f )$ terms arising from tho distubmg aetion of $\mathfrak { m } _ { 3 }$ due to theperturbations of the fist odel of the elenents of ${ \bf \gamma } m _ { 3 }$ by $m _ { 2 }$

Undei the supposition Chal lhcre are thee planets, the terms of the second oilei withiespcet to the massesaie found from equations (19) and (20) to bc

$$
\begin{array} { r }  \{ \begin{array} { l l } { d \alpha _ { \mathrm { { S } } } , u _ { \mathrm { S } } , \frac { \mu _ { \mathrm { S } } } { \mu _ { \mathrm { S } } } , \omega _ { \mathrm { { S } } } , \frac { \mu _ { \mathrm { { S } } } \omega _ { \mathrm { { S } } } } { 2 } , \frac { \omega _ { \mathrm { { S } } } \omega _ { \mathrm { { S } } } } { 2 } , \frac { \omega _ { \mathrm { { S } } } \omega _ { \mathrm { { S } } } } { \omega _ { \mathrm { { S } } } } , \frac { \mu _ { \mathrm { S } } w _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { { S } } } w _ { \mathrm { S } } } { \beta _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { \beta _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { S } } } { \beta _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { S } } } { \beta _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { S } } } { \omega _ { \mathrm { S } } } , } \\  \mathrm { ~ i f ~ } \omega _ { \mathrm { { S } } } , \frac { \omega _ { \mathrm { S } } } { 2 } , \frac { \mu _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { { S } } } } { \omega _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { { S } } } \omega _ { \mathrm { { S } } } } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { \beta _ { \mathrm { S } } } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { \omega _ { \mathrm { S } } } , \frac { \mu _ { \mathrm { S } } w _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } { 2 } , \frac { \omega _ { \mathrm { S } } \omega _ { \mathrm { S } } } \\  d \alpha _ { \mathrm { S } } , \frac { \mu _ { \mathrm { S } } \omega _ { \mathrm { S } } } { d } ,  \end{array} \end{array}
$$

and simlnr quatio or $\frac { d \beta _ { i } } { d t } \mathrm { a n d } \frac { d \gamma _ { \mathrm { * } } } { d t }$

Tho firsl two cqualions give tha pertuibations of the class (a), for，Φi(α,β) and i(α,r) are the portions of the perturbative function given by ma and mg respectively， while β,(,o.o and Y,(.0.o) aro tho porlurbations of Che first oider of the elements of tho orbits of m and mg by m1 Similarly,the thid and fourth equntions givo lho portuubations of tho class (b)， the first term of lhe fiflh cqualion, thosr of class (c),the second term, of class (d);tho third icim,of class (e),and the fourth term,of the class (f)

It appeais fiom this that the teims of the socond oider cannot be computed separately for cach of the dislur bing planets

The types of tcrms which will arise in the perturbations of the third order can bo similarly piedictcd from physical considerations,and the prcdictions can be veiified by $\mathfrak { a }$ detailed discussion of the equations.

1 In cqualons (3) take thc tcrm $\nu \cos \mathit { l t }$ to tho left membor bofoio staiting the integration,and include it im cquations (4） Cany out tho wholo procc8s of integiation with this vaiiation m tho proccduo

2 If cquations (7) ao integiated as power solies in $\pmb { \mu }$ and $\pmb { \nu } _ { \pmb { \mathscr { s } } }$ whal typcs of functions of $\pmb { \ell }$ will nuiso in tho teims of the second oide？

3Wiite the equations defining tho toims of oidel zeio,ono,and iwo in thc mngscg when cquations (11） aie mtegrnled as sclies m ml and m Show thal the tcims of oidcr zero ao the cooidinatcs thal $\pmb { m } _ { 1 }$ and $\textcircled { \ m }$ would have if they weie particles moving aiound thc sun In cllpses defincd by then initial conditions Show thal the cqunlions defining tho toimg of tho first and higher oders are lnear and non-homogencous,mstead of being ieduced to qundratures as they aio after tho mothod of tho variation of parainete18 has been uscd

4 Suppoge thero auo four planets, $m _ { 1 } , m _ { 2 } , m _ { 3 } , m _ { 4 } ,$ writo all tho tei ms of tho second oder with respect to tho masses accoiding to (3o) and intci pret cach

5 Suppose theie are two planets $\pmb { m _ { 1 } }$ and $m _ { 2 }$ writo all of the texmg of lhg thmd ordei with respect to tho masses and interpiot ench

6 Suppose $m _ { 1 } = \ d _ { m } \ d _ { 2 } = \ d _ { m }$ and that tho planets aro aiianged m the ordor mi,mz, m with respect to thoir distanco from tho sunShow thal of tho perturbations defined by cquations (3O) the mosl important aio tloge given by the first and thnd oqualions and tho second teim of tho fflh,lhat tho peiturbations next in importance ao givcn by lhe first, thmd, and fourth tcims of the fiflh equntion,and that the least imporlanl aro given by the Becond and fourth cquations.

211.Choice of Elements.In oider to exhibit the manner in which the valious solts of leims enter in the per turbations of the ft st ordei,il will be ncccssay to develop equations (19) explcitly This wag defeiicd,on account of the length of the tiansformations whjch aic necessaiy, until $\mathfrak { a }$ geneial view of the mathematical principles mvolvcd could be given

If teims of tlc fist oider alone aie consideied the functions $\phi _ { \ast } ( \alpha , \beta )$ ean be consilercd mdependently of $\psi _ { \imath } ( \alpha , \beta )$ Any independent functions of the clements may be used in place of the odinaiy clementsIn fact,one of the eleinents aleady employed, ${ \pi } = \omega + \delta \lambda$ ，1s the sum of two geomcliically simple1 elements Now thc foim of $\phi _ { \imath } ( \alpha , \beta )$ will depend upon the clements chosen, with ceilun clcments lhey aic iather simple,and with others very compheutcdThcy will bc taken in the fist example which follows so thal lhosc functions shall become as simple as possible

212. Lagrange's Brackets, Lagrange lag made the following transfoi malion which greatly facilitates the computation of (19) Multiply (18) $\begin{array} { r } { \mathrm { b y } - \frac { \partial { \sf z } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } , - \frac { \partial { \cal y } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } , - \frac { \partial { \sf z } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } , \frac { \partial \tau _ { 1 } } { \partial \alpha _ { 1 } } , \frac { \partial \boldsymbol { y } _ { 1 } } { \partial \alpha _ { 1 } } , \frac { \partial { \boldsymbol { z } _ { 1 } } } { \partial \alpha _ { 1 } } } \end{array}$ respeetvoly and add The icsult 1s

$$
\{ \begin{array} { l l } { \displaystyle \frac { d \alpha _ { 0 } } { d t } \{ \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } - \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 2 } } + \frac { \partial \hat { y } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { y } _ { \ell } ^ { \prime } } { \partial \alpha _ { 2 } } - \frac { \partial \hat { y } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \hat { y } _ { \ell } } { \partial \alpha _ { 1 } } } \\ { \qquad \quad \cdot } \\ { \displaystyle + \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 2 } } - \frac { \partial \hat { y } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } } \\ { \displaystyle + \frac { d \alpha _ { 0 } } { d t } \{ \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 3 } } - \frac { \partial \hat { y } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 2 } } + \dots \} . } \\ { \qquad \cdot } \\  \displaystyle + \frac { d \alpha _ { 0 } } { d t } \{ \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } - \frac { \partial \hat { x } _ { \ell } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 3 } } + \} \\ { \qquad \quad \cdot } \\  \displaystyle + \frac { m _ { 0 } } { d t } \{ \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } \frac { \partial \hat { x } _ { \ell } } { \partial \alpha _ { 1 } } - \ \end{array}
$$

Lagrnngo's bracketg $[ \alpha _ { 1 } , \alpha _ { l } ] \mathrm { a } \ i 0$ defined by

$$
\begin{array} { r } { [ \alpha _ { 1 1 } \alpha _ { 1 } ] \equiv \frac { \partial x _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \langle \boldsymbol { \mathrm {  ~ \hat { \sigma } ~ } } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } - \frac { \partial \langle \boldsymbol { \mathrm {  ~ \hat { \sigma } ~ } } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial x _ { 1 } } { \partial \alpha _ { 1 } } + \frac { \partial \langle \boldsymbol { \mathrm {  ~ \hat { \sigma } ~ } } _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial \langle \boldsymbol { \mathrm {  ~ \hat { \sigma } ~ } } _ { 1 } ^ { \prime } } { \partial \alpha _ { i } } - \frac { \partial \langle \boldsymbol { \mathrm {  ~ \hat { \sigma } ~ } } _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial y _ { 1 } } { \partial \alpha _ { i } } } \\ { + \frac { \partial z _ { 1 } } { \partial \alpha _ { 1 } } \frac { \partial z _ { 1 } ^ { \prime } } { \partial \alpha _ { i } } - \frac { \partial z _ { 1 } ^ { \prime } } { \partial \alpha _ { 1 } } \frac { \partial z _ { 1 } } { \partial \alpha _ { i } } } \end{array}
$$

Foim the equations conesponding to (31) in $\alpha _ { 2 } ,$ ：， $\alpha _ { \beta }$ ,the result ing syslem of equations is

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { 0 } \left[ \alpha _ { 1 } , \alpha _ { 1 } \right] \frac { d \alpha _ { 1 } } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 } , } { \partial \alpha _ { 1 } } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 8 } \left[ \alpha _ { 2 } , \alpha _ { 1 } \right] \frac { d \alpha _ { 1 } } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 2 } } , } \\ { \displaystyle \qquad , } \\ { \displaystyle \sum _ { i = 1 } ^ { 8 } \left[ \alpha _ { 0 } , \alpha _ { 1 } \right] \frac { d \alpha _ { 1 } } { d \ell } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \alpha _ { 0 } } } \end{array} \right.
$$

These equations are cquivalent to the system (18) and will be uscl in place of them

213.Properties of Lagrange's Brackets. It follows at oncc from the definitions of Lagrangc's biackets that

$$
\left\{ \begin{array} { l l } { \left[ \alpha _ { \iota } , \alpha _ { \iota } \right] = 0 , } \\ { \left[ \alpha _ { \iota } , \alpha _ { \iota } \right] = - \left[ \alpha _ { \iota } , \alpha _ { \iota } \right] } \end{array} \right.
$$

A moie important pioperty is that they do nol contain the timc explcitly, thal is,

$$
\frac { \partial [ \alpha _ { 1 } , \alpha _ { 2 } ] } { \partial t } = 0 , \qquad ( \ i = 1 , \qquad , \ i ; \ j = 1 , \cdot \quad , \ 0 ) ,
$$

as will be ploved immediately.

Many complicalcd cxprcssions will arise in the following discussion which aie syinmelrical n $\mathfrak { L } , \mathfrak { Y } _ { \mathrm { i } }$ and $\pmb { \mathscr { z } }$ 。In order to abbieviate the wiiting lel $\pmb { \ S }$ ,standing before a function of $\pmb { x } ,$ mdicate thal the same functions of ${ \pmb y }$ and $\pmb { \mathscr { z } }$ are to be addcd Thus,for oxample,

$$
\mathcal { S } ( \mathfrak { v } _ { 1 } \mathfrak { v } _ { 2 } { ' } - \mathfrak { x } _ { 2 } \mathfrak { x } _ { 1 } { ' } ) \equiv ( \mathfrak { v } _ { 1 } \mathfrak { v } _ { 2 } { ' } - \mathfrak { x } _ { 2 } \mathfrak { x } _ { 1 } { ' } ) + ( \mathfrak { y } _ { 1 } \mathfrak { y } _ { 2 } { ' } - \mathfrak { y } _ { 2 } \mathfrak { y } _ { 1 } { ' } ) + ( \mathfrak { z } _ { 1 } \mathfrak { z } _ { 2 } { ' } - \mathfrak { z } _ { 2 } \mathfrak { z } _ { 1 } ^ { \prime } )
$$

In slaiting from the dofinitions of the brackets and omilting tho subscripts of $\boldsymbol { \mathscr { x } } , \quad \cdot \cdot , \boldsymbol { \mathscr { z } ^ { \prime } }$ ,which will not be of uso in whal follows, it is found that

$$
\begin{array} { r } { \frac { \partial [ \alpha _ { \mathfrak { c } } , \alpha _ { \mathfrak { f } } ] } { \partial \ell } =  { \mathcal { S } } \{ \frac { \partial ^ { 2 } \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } \partial \mathcal { \bar { d } } } \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } } + \frac { \partial \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } } \frac { \partial ^ { 2 } \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } \partial \mathcal { \bar { d } } } - \frac { \partial ^ { 2 } \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } \partial \mathcal { \bar { d } } } \frac { \partial \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } } - \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } } \frac { \partial ^ { 2 } \mathfrak { c } _ { 3 } } { \partial \alpha _ { \mathscr { d } } \partial \mathcal { \bar { d } } } \} } \\ { = \frac { \partial } { \partial \alpha _ { \mathfrak { c } } }  { \mathcal { S } } \{ \frac { \partial \mathfrak { c } } { \partial \mathcal { \bar { d } } } \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } } - \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \mathcal { \bar { d } } } \frac { \partial \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } } \} +  { \mathcal { S } } \{ - \frac { \partial \mathfrak { c } } { \partial \mathcal { \bar { d } } } \frac { \partial ^ { 2 } \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } \partial \alpha _ { \mathfrak { d } } } + \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \mathcal { \bar { L } } } \frac { \partial ^ { 2 } \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } \partial \alpha _ { \mathfrak { c } } } \} } \\  + \  { \mathcal { S } } \{ \frac { \partial \mathfrak { c } } { \partial \alpha _ { \mathfrak { c } } } \frac { \partial ^ { 2 } \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } \partial \mathcal { \bar { d } } } - \frac { \partial \mathfrak { c ^ { \prime } } } { \partial \alpha _ { \mathfrak { c } } } \frac { \partial ^ { 2 } \mathfrak { c } }  \partial  \end{array}
$$

The parlial dleiivaliveg of the coordmates with iespect to the time ao tho same in distuibed motion as the total deiivatives in undisturbcd motion Theicfoic this equation becomes as a consequence of (14)

$$
\begin{array} { r l } & { \frac { \partial [ \alpha \mathfrak { c } _ { 1 1 } , \alpha \mathfrak { c } _ { l } ] } { \partial \mathcal { V } } = \frac { \partial } { \partial \alpha _ { 1 } } \mathbb { S } \left\{ \frac { \partial \Omega } { \partial \lambda } \frac { \partial \mathfrak { c } } { \partial \alpha _ { l } } + \frac { \partial \Omega } { \partial \mathfrak { c } ^ { \prime } } \frac { \partial \mathfrak { c } ^ { \prime } } { \partial \alpha _ { l } } \right\} - \frac { \partial } { \partial \alpha _ { 1 } } S \left\{ \frac { \partial \Omega } { \partial \mathfrak { c } } \frac { \partial \mathfrak { c } } { \partial \alpha _ { \mathfrak { \mathfrak { 1 } } } } + \frac { \partial \Omega } { \partial \mathfrak { c } ^ { \prime } } \frac { \partial \mathfrak { c } ^ { \prime } } { \partial \alpha _ { \mathfrak { \mathfrak { 1 } } } } \right\} } \\ & { \qquad = \frac { \partial } { \partial \alpha _ { \mathfrak { 1 } } } \left( \frac { \partial \Omega } { \partial \alpha _ { i } } \right) - \frac { \partial } { \partial \alpha _ { j } } \left( \frac { \partial \Omega } { \partial \alpha _ { \mathfrak { 1 } } } \right) = \frac { \partial ^ { \circ } \Omega } { \partial \alpha _ { \mathfrak { 1 } } \partial \alpha _ { j } } - \frac { \partial ^ { 2 } \Omega } { \partial \alpha _ { j } \partial \alpha _ { \mathfrak { 1 } } } = 0 , } \end{array}
$$

which provcg the thcorcm that the biackets do not contain $\pmb { \delta }$ oxplcitly.Thig would haidly be anticipated since each of the quantitieg which appcais in the biackets is an explcit function of $\pmb { t }$

Snco lhc brackcls do not contain the time cxplcitly they may bo compulcd fol any cpoch whatever,and in particular fol $t = t _ { 0 }$ Tho cqualions become vciy simplc if the cooidmates at the time $t = l _ { 0 }$ are taken foi lho clements $\alpha _ { \parallel } ,$ ： $\alpha _ { \delta }$ This is permissible Bincc tho oldinaiy olemcnls aie defined by these quantities,and convorsely.Il musl nol be supposed that they are constants, thoy auc such quantities that if thc elemcnts aie computed from them,and lhen if tho cooidinatcs at any time $\pmb { t }$ arc computed using lhcso clomcnts,the coiicct icsults will be obtamed Since in dislurbcd molion lho clements vaiy with the time, the values of the coordnalcs nt $\iota = \iota _ { 0 }$ also vary. Otherwise considered, if the osculatng clemenlg at $\pmb { \ell }$ arc uscd and if the coordinates at the limc $\ell = t _ { 0 }$ αc coimpulcd, il will be found in the case of disturbed molion lhat tho coordinatcs at t = to vary,and these values of tho cooidinnles are the ones in qucstion

Lot tho couidmales at the timo $\ell = \ell _ { 0 }$ be $\approx 0 ,$ ： ${ z _ { 0 } } ^ { \prime }$ ，then

$$
[ { \mathfrak { a } } _ { 0 } , y _ { 0 } ] = S \left\{ { \frac { \partial { \mathfrak { c } } _ { 0 } } { \partial { \mathfrak { x } } _ { 0 } } } { \frac { \partial { \mathfrak { x } } _ { 0 } } { \partial } } - { \frac { \partial { \mathfrak { x } } _ { 0 } } { \partial { \mathfrak { x } } _ { 0 } } } { \frac { \partial { \mathfrak { x } } _ { 0 } } { \partial y _ { 0 } } } \right\} ,
$$

whtch cquais zero beause ve' Is independent of yo and ao Similarly，

$$
{ \begin{array} { r } { \{ \left[ { \boldsymbol { \eta } } , \tilde { { \boldsymbol { \pi } } } _ { 0 } \right] = [ { \boldsymbol { \pi } } _ { 0 } , \mathrm { ~ } { \boldsymbol { \lambda } } _ { 0 } ] = [ { \boldsymbol { \lambda } } _ { 0 } , ^ { \prime } , { \boldsymbol { \mathcal { Y } } } _ { 0 } ^ { \prime } ] = [ { \boldsymbol { y } } _ { 0 } , \tilde { \boldsymbol { \pi } } _ { 0 } ^ { \prime } ] = [ z _ { 0 } , \mathrm { ~ } { \boldsymbol { \mathcal { X } } } _ { 0 } ^ { \prime } ] = [ \tilde { \boldsymbol { \pi } } _ { 0 } , \mathrm { ~ } { \boldsymbol { \mathcal { Y } } } _ { 0 } ] = 0 , } \\ { \left[ \{ \boldsymbol { \lambda } \right]} _ { 0 } , { \boldsymbol { y } } _ { 0 } ^ { \prime }  = [ z _ { 0 } , \mathrm { ~ } z _ { 0 } ^ { \prime } ] = [ { \boldsymbol { y } } _ { 0 } , \mathrm { ~ } { \boldsymbol { \pi } } _ { 0 } ^ { \prime } ] = [ { \boldsymbol { y } } _ { 0 } , \mathrm { ~ } { \boldsymbol { \pi } } _ { 0 } ^ { \prime } ] = [ z _ { 0 } , \mathrm { ~ } { \boldsymbol { \pi } } _ { 0 } ^ { \prime } ] = [ z _ { 0 } , \mathrm { ~ } { \boldsymbol { \mathcal { Y } } } _ { 0 } ^ { \prime } ] = 0 . } \end{array} 
$$

But

$$
[ v _ { 0 } , v _ { 0 } ^ { \prime } ] = [ y _ { 0 } , y _ { 0 } ^ { \prime } ] = [ z _ { 0 } , z _ { 0 } ^ { \prime } ] = 1 ,
$$

Thcioforc equations (33） become in this case

$$
\begin{array} { r l r } & { } & { \{ \frac { d z _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { z _ { 0 } } ^ { \prime } } , ~ \frac { d x _ { 0 } { ' } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x _ { 0 } } ,  } \\ & { } & { \{ \frac { d y _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { y _ { 0 } } ^ { \prime } } , ~ \frac { d y _ { 0 } { ' } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { y _ { 0 } } } ,  } \\ & { } & {  ( \frac { d z _ { 0 } } { d t } = m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial { z _ { 0 } } ^ { \prime } } , ~ \frac { d z _ { 0 } { ' } } { d t } = - m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z _ { 0 } } .  } \end{array}
$$

/

Any system of differential equations of the form (38) is known asa canonical system,and thcy possess properties which make them particulaily valuable in theoictical investigationsThcie is $\mathfrak { a }$ theorem that any dynamical pioblem in which the foices can bc represented as pal tial derivatives of a potential function can be eYpressed in this form，and if it is possible to put & problcm in tho canonical form it 1s possible to do so in infinitely many systems of dependent variables

If equations (38) were solved they would give thc values of thc coordinates at $\scriptstyle t _ { 0 }$ which would have to be used to obtain the true coordinates at the time $\mathbf { \delta } _ { t , \tiny { \begin{array} { r l } \end{array} } } t _ { \star }$ under the supposition that thc planet moved in an undisturbed ellpse during $t - t _ { 0 }$ 、If the variablcs were the elliptic elements the solutions of the equations would give the elements which would have to be uscd to compute tho cobrdinates at the time $\ell ,$ when they are supposed to have been constant duimg the interval $t - t _ { 0 }$ Thus,when the elements have been found the remainder of the computation is that of undisturbed motion

214.Transformation to the Ordinary Elements. The elements used in Astionomy are not the coordinates at $t = t _ { 0 } ,$ but $\delta \delta , \pmb { \imath } , \pmb { a } ,$ $e , \pi ,$ and $\pmb { T }$ (or $\epsilon = \pi - n T$ ,which werc exprcssed in terms of tho initial conditions in Arts 86,87,and 88It will be necessary, theiefoie, to transform equations (38) to tho corresponding oncs which involve only the elements which are actually in use by astronomcrs

Let s represent any one of the elemcnts $\Omega , i , a , e , \pi , \epsilon .$ It may be expressed symbolically in terms of the initial conditions by

$$
\begin{array} { r } { s = f ( \mathfrak { c } _ { 0 } , \mathfrak { Y } _ { 0 } , \mathfrak { z } _ { 0 } , \mathfrak { x } _ { 0 } ^ { \prime } , \mathfrak { Y } _ { 0 } ^ { \prime } , \mathfrak { z } _ { 0 } ^ { \prime } ) . } \end{array}
$$

Hence it follows that

$$
\frac { d \boldsymbol { s } } { d t } = \boldsymbol { S } \left\{ \frac { \partial f } { \partial \boldsymbol { x _ { 0 } } } \frac { d \boldsymbol { x _ { 0 } } } { d t } + \frac { \partial f } { \partial \boldsymbol { x _ { 0 } } ^ { \prime } } \frac { d \boldsymbol { x _ { 0 } } ^ { \prime } } { d t } \right\} ;
$$

or, because of (38),

$$
\frac { d s } { d t } = m _ { 2 } \mathrm { S } \left\{ \frac { \partial f } { \partial \mathfrak { x } _ { 0 } } \frac { \partial \mathcal { R } _ { 1 , ~ 2 } } { \partial \mathfrak { x } _ { 0 } \mathrm { \Gamma } ^ { \prime } } - \frac { \partial \int } { \partial \mathfrak { x } _ { 0 } } \frac { \partial \mathcal { R } _ { 1 , ~ 2 } } { \partial \mathfrak { x } _ { 0 } } \right\} .
$$

The paitial derivatves of $\smash { \mathbb { R } _ { 1 , 3 } }$ are expressed in terms of the partial deiivatives with respcct to the new variables by the equations

$$
\left\{ \begin{array} { l } { \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial { \tau _ { 0 } } } = \frac { \partial R _ { 1 , 2 } } { \partial \delta _ { 0 } } \frac { \partial \delta _ { 0 } } { \partial { \tau _ { 0 } } } + \frac { \partial R _ { 1 , 2 } } { \partial \delta _ { 0 } } \frac { \partial \lambda _ { 0 } } { \partial { z _ { 0 } } } + \frac { \partial R _ { 1 , 2 } } { \partial a } \frac { \partial \alpha } { \partial \tau _ { 0 } } + \frac { \partial R _ { 1 , 2 } } { \partial \varrho } \frac { \partial \alpha } { \partial \tau _ { 0 } } } \\ { \displaystyle \qquad + \frac { \partial R _ { 1 , 2 } } { \partial \tau } \frac { \partial \pi } { \partial { z _ { 0 } } } + \frac { \partial R _ { 1 , 2 } } { \partial \epsilon } \frac { \partial \epsilon } { \partial { z _ { 0 } } } , } \\ { \displaystyle \qquad \cdot \quad \cdot \quad \cdot \quad \cdot } \\ { \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial { z _ { 0 } } ^ { \prime } } = \frac { \partial R _ { 1 , 2 } } { \partial \delta _ { 0 } } \frac { \partial \delta _ { 0 } } { \partial { z _ { 0 } ^ { \prime } } } + \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { z } } \frac { \partial \tau } { \partial { z _ { 0 } ^ { \prime } } } + \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { z } } \frac { \partial \alpha } { \partial \tau _ { 0 } ^ { \prime } } + \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { z } } \frac { \partial \alpha } { \partial \tau _ { 0 } ^ { \prime } } } \\ { \displaystyle \qquad + \frac { \partial R _ { 1 , 2 } } { \partial \pi } \frac { \partial \pi } { \partial { z _ { 0 } ^ { \prime } } } + \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { z } } \frac { \partial \epsilon } { \partial { z _ { 0 } ^ { \prime } } } . } \end{array} \right.
$$

On carrymg out tho complcated computations of $\frac { \partial \mathscr { s } } { \partial \mathscr { v } _ { 0 } } , \qquad , \frac { \partial \mathscr { s } } { \partial \mathscr { z } _ { 0 } }$ by means of the cquations given in Aits.86,87,and 88,and cx" pressing all the pai tial derivatives in terms of the ncw variables, the partial derivatives $\frac { \partial { R _ { 1 , ~ 2 } } } { \partial { { \lambda } _ { 0 } } }$ ， $\underbrace { \partial R _ { 1 , \ 2 } } _ { \partial z _ { 0 } ^ { \prime } } \underbrace { \partial \mathrm { r e } } _ { \partial \mathrm { t r e } }$ found in terms of the elements &ad $\begin{array} { r } { \frac { \partial \ R _ { 1 , ~ 2 } } { \partial \otimes } , \quad \cdots , \ \frac { \partial \ R _ { 1 , ~ 2 } } { \partial \epsilon } . } \end{array}$ On substituting in (40) and expressing $\frac { \partial f } { \partial \mathfrak { x } _ { 0 } } , \cdot \mathbf { \nabla } \cdot , \frac { \partial { f } } { \partial \mathfrak { z } _ { 0 } ^ { \prime } } \ln$ te1ms of the clments, $\frac { d \vartheta } { d t }$ is found in terms of tho elcments and tho derivatives of the peiturbative function, $\mathcal { R } _ { 1 , ~ 2 } ,$ with respcct to tho olemonts.

215.Method of Direct Computation of Lagrange's Brackets. The transformations required in the method of the preceding article are vory laborious,and the dirccl computation of the brackets, though considorably involvcd,is to be preferred from a practical point of view.Al of the computalion in the transformatrons of ths sort mght be avoided by using canoncal varrables; but,in order to employ them, a longthy digression upon the properties of canonical systems would bc necessaiy,and such & discugsion 1s outside the lmits of thg work. Stll, the labor may be nolably reduced by first taking elomonts somewhat diffcient fiom those defined in chapter v，and then transforming to thosc in more ordinary use. The following is based on Tisserand's exposition of Lagrange's method.\*

\*Tisgerand's Mecamque Celeste,vol I,p.170.

Let the xy-plane be the plane of the ecliptic, $\Omega \mathcal { P }$ the projection of the orbit upon the celeslial sphere, $\pi$ the projection of the perihelion pont,and $\mathcal { P }$ the piojeclion of the position of the planet at the time $\pmb { t }$ In place of $\pmb { \pi }$ and $\epsilon ,$ adopt the new elements $\pmb { \omega }$ and $\pmb { \sigma }$ defined by tho equations

$$
\left\{ { \begin{array} { l } { \omega = \pi - \Omega , } \\ { \sigma = - n T } \end{array} } \right.
$$

![](../chunks/An-Introduction-To-Celestial-Mechanics_part_0006_pages_0351-0420/auto/images/aa3e5b894d538e53ee4a5cadf32a08097e7e1b9008aa8deffebbde1f104f2103.jpg)  
Fig 60.

The following equations are either given in Art.98,or are obtaned from Fig.60 by the fundamental formulas of Trigonometry:

$$
\begin{array} { r } { \begin{array} { r l } & { \mathcal { B } - \epsilon \sin \mathcal { R } = n + a + \sigma , } \\ & { ~ } \\ { { \boldsymbol { r } } = a ( 1 - \epsilon \cos \mathcal { B } ) , } \\ & { ~ } \\ { ~ } \\ { \sin \frac { \theta } { 2 } = \sqrt { \frac { 1 + \theta } { 1 - \theta } } \tan \frac { \mathcal { B } } { 2 } , } \\ & { } \\ { \cos \theta = \frac { \cos \mathcal { B } - \epsilon } { 1 - \theta \cos \mathcal { B } } , } \\ & { ~ } \\ { { \bf s u p } = \frac { \sqrt { 1 - \epsilon } } { 1 - \epsilon \cos \mathcal { B } } \frac { \mathcal { B } } { 2 } , } \\ & { ~ } \\ { { \boldsymbol { v } } = { \boldsymbol { r } } [ \cos \left( \theta + \omega \right) \cos \mathcal { B } \odot \cos \mathrm { ~ c a v } \left( v + \omega \right) \sin \mathrm { ~ } \otimes \cos \mathfrak { s } ] , } \\ & { ~ } \\ { { \boldsymbol { y } } = { \boldsymbol { r } } [ \cos \left( \theta + \omega \right) \sin \mathrm { ~ } \partial \sin \mathrm { ~ } \otimes \cos \mathrm { ~ d } \mathrm { ~ s } ] , } \\ & { ~ } \\ { { \boldsymbol { g } } = { \boldsymbol { r } } \sin \left( v + \omega \right) \sin \mathfrak { v } . } \end{array} } \end{array}
$$

From these equations and theil derivatives with respect to the time the partial derivatives of the cooidinates with iespect to the elements can be computed The elements have been chosen in such a mannei that they aie divided mto two groups having distinct popc tics, $\Omega , \ell ,$ and $\omega$ define thc position of the plane of motion and the ouientation of the orbit in the plane,and $a , \ e _ { \gimel }$ and $\pmb { \sigma }$ define the dimensions and shape of the oibit and the position of the planet m its oibil.Therefoie the cooidinates m the orbit can be cxprcssed in tcims of thc clements of the second group alonc,and from thcm,the coordinates in space can be found by means of thc first gioup alone

Take a now systcm of axcs with the oiigin at the sun, the positive end of the $\pmb { \xi }$ -axis dncctcd to the peihelion point, the $\pmb { \eta }$ axis ${ \mathfrak { g } } { \mathfrak { Q } } ^ { \circ }$ forward in the planc of the orbit,and the $\pmb { \zeta }$ -axis peipendiculal to the plane of thc oibit.Let the dncction cosines between the x-axis and the ,n,and {-axes be α,α',a",between the y-axis and the 5,n, and {-axes be β,β',β"；and between the z-axis and the ,n,and 5-axes be y,Y',Y".Then it follows from Fig 60 that

$$
{ \left\{ \begin{array} { l l } { \alpha = 0 . 0 8 \implies 0 . 3 - 8 1 \implies 0 . 8 1 \implies 0 . 0 8 \implies 0 . 3 } \\ { \beta = 0 . 0 8 \implies \mathrm { s i n } \otimes \lambda = \mathrm { s i n } \otimes \mathrm { s i n } \otimes \mathrm { s i n } \otimes \mathfrak { s } , } \\ { \gamma = \mathrm { s i n } \otimes \mathrm { s i n } \ \tau _ { \tau } } \\ { \alpha ^ { \prime } = - \mathrm { s i n } \otimes \mathrm { c o s } \ \delta \to \mathrm { - c o s } \ \omega \mathrm { s i n } \ \otimes \mathrm { c o s } \ \mathfrak { s } , } \\ { \beta ^ { \prime } = - \mathrm { s i n } \otimes \mathrm { s i n } \ \delta \to \mathrm { - c o s } \ \omega \mathrm { c o s } \ \otimes \mathrm { c o s } \ \mathfrak { s } , } \\ { \gamma ^ { \prime } = 0 . 0 8 \implies \mathrm { s i n } \ \delta , } \\ { \alpha ^ { \prime \prime } = \mathrm { s i n } \ \otimes \mathrm { s i n } \ \delta , } \\ { \beta ^ { \prime \prime } = - \mathrm { c o s } \ \delta \dim \ \delta , } \\ { \gamma ^ { \prime \prime } = \mathrm { c o s } \ \delta } \end{array} \right. }
$$

There oxist among these nine dircction cosines,as can easily be verificd,the ielations

$$
\left\{ \begin{array} { l l } { \qquad \alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { 2 } = 1 , \qquad \alpha \alpha ^ { \prime } + \beta \beta ^ { \prime } + \gamma \gamma ^ { \prime } = 0 , } & \\ { \alpha ^ { \prime 2 } + \beta ^ { \prime 2 } + \gamma ^ { \prime 2 } = 1 , \qquad \alpha ^ { \prime } \alpha ^ { \prime \prime } + \beta ^ { \prime } \beta ^ { \prime \prime } + \gamma ^ { \prime } \gamma ^ { \prime \prime } = 0 , } & \\ { \alpha ^ { \prime \prime 2 } + \beta ^ { \prime \prime 2 } + \gamma ^ { \prime \prime 2 } = 1 , \qquad \alpha ^ { \prime \prime } \alpha + \beta ^ { \prime \prime } \beta + \gamma ^ { \prime \prime } \gamma = 0 , } & \\ { \alpha = \beta ^ { \prime } \gamma ^ { \prime \prime } - \gamma ^ { \prime } \beta ^ { \prime \prime } , \quad \alpha ^ { \prime } = \beta ^ { \prime \prime } \gamma - \gamma ^ { \prime \prime } \beta , \quad \alpha ^ { \prime \prime } = \beta \gamma ^ { \prime } - \gamma \beta ^ { \prime } , } & \\ { \beta = \gamma ^ { \prime } \alpha ^ { \prime \prime } - \alpha ^ { \prime } \gamma ^ { \prime \prime } , \quad \beta ^ { \prime } = \gamma ^ { \prime \prime } \alpha - \alpha ^ { \prime \prime } \gamma , \quad \beta ^ { \prime \prime } = \gamma \alpha ^ { \prime } - \alpha \gamma ^ { \prime } , } & \\ { \gamma = \alpha ^ { \prime } \beta ^ { \prime \prime } - \beta ^ { \prime } \alpha ^ { \prime \prime } , \quad \gamma ^ { \prime } = \alpha ^ { \prime \prime } \beta - \beta ^ { \prime \prime } \alpha _ { 1 } \quad \gamma ^ { \prime \prime } = \alpha \beta ^ { \prime } - \beta \alpha ^ { \prime } . } & \end{array} \right.
$$

It follows fiom (43) and (44) and the dcfinition of the new system of axes that

$$
\left\{ \begin{array} { l } { { \displaystyle { \frac { { \bf \Phi } _ { k } } { \partial { \cal U } } = r \cos \vartheta = a ( \cos \mathcal { B } - \theta ) , ~ \eta = a \sqrt { 1 - e ^ { 2 } } \sin \mathcal { B } , } } } \\ { { \displaystyle { \frac { \partial \mathcal { B } } { \partial { \cal U } } = \frac { n } { 1 - e \cos \mathcal { B } } , } } } \\ { { \displaystyle { \xi ^ { \prime } = \frac { - n a \sin \mathcal { B } } { 1 - e \cos \mathcal { B } } \frac { - k \sqrt { S + m _ { 1 } } \sin \mathcal { B } } { \sqrt { a } ( 1 - e \cos \mathcal { B } ) } , } } } \\ { { \displaystyle { \eta ^ { \prime } = \frac { n a \sqrt { 1 - e ^ { 2 } } \cos \mathcal { B } } { 1 - e \cos \mathcal { B } } = \frac { k \sqrt { S + m _ { 1 } } \sqrt { 1 - e ^ { 2 } } \cos \mathcal { B } } { \sqrt { a } ( 1 - e \cos \mathcal { B } ) } , } } } \\ { { \displaystyle { \alpha = \alpha \xi + \alpha ^ { \prime } \eta , ~ \eta = \beta \xi + \beta ^ { \prime } \eta , ~ \tau = \gamma \xi + \gamma ^ { \prime } \eta , } } } \\ { { \displaystyle x ^ { \prime } = \alpha \xi ^ { \prime } + \alpha ^ { \prime \prime } \eta ^ { \prime } , ~ \eta ^ { \prime } = \beta \xi ^ { \prime } + \beta ^ { \prime \prime } , ~ \tau ^ { \prime } = \gamma \xi ^ { \prime } + \gamma ^ { \prime \prime } , } } \end{array} \right.
$$

where the accents on $x , y , z , \xi , \eta ,$ and $\boldsymbol { \xi }$ indicate first dorivatives with respect to $\pmb { t }$

The partial derivatives of ${ \pmb { \alpha } } _ { \pmb { \alpha } }$ ，， $\gamma ^ { \prime \prime }$ with respcct to tho elemcnts may be computcd once foi all,they are found fiom (44) to be

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \omega } = \alpha ^ { \prime } , } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \omega } = - \alpha , \quad \quad \frac { \partial \alpha ^ { \prime \prime } } { \partial \omega } = 0 , } \\ { \displaystyle \frac { \partial \beta } { \partial \omega } = \beta ^ { \prime } , } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \omega } = - \beta , \quad \quad \frac { \partial \beta ^ { \prime \prime } } { \partial \omega } = 0 , } \\ { \displaystyle \frac { \partial \gamma } { \partial \omega } = \gamma ^ { \prime } , } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \omega } = - \gamma , \quad \quad \frac { \partial \gamma ^ { \prime \prime } } { \partial \omega } = 0 , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \boldsymbol { \otimes } } = - \ \beta , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \boldsymbol { \otimes } } = \ - \ \beta ^ { \prime } , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime \prime } } { \partial \boldsymbol { \otimes } } = \ - \ \beta ^ { \prime \prime } , } \\ { \displaystyle \frac { \partial \beta } { \partial \boldsymbol { \otimes } } = \alpha , \quad } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \boldsymbol { \otimes } } = \alpha ^ { \prime } , \quad } & { \displaystyle \frac { \partial \beta ^ { \prime \prime } } { \partial \boldsymbol { \otimes } } = \alpha ^ { \prime \prime } , } \\ { \displaystyle \frac { \partial \gamma } { \partial \boldsymbol { \otimes } } = 0 , \quad } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \boldsymbol { \otimes } } = 0 , \quad } & { \displaystyle \frac { \partial \gamma ^ { \prime \prime } } { \partial \boldsymbol { \otimes } } = 0 , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \lambda } = \alpha ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \lambda } = \alpha ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \alpha ^ { \prime \prime } } { \partial \lambda } = + \sin \Omega \cos \dot { \omega } , } \\ { \displaystyle \frac { \partial \beta } { \partial \dot { \iota } } = \beta ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \beta ^ { \prime } } { \partial \dot { \iota } } = \beta ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \beta ^ { \prime \prime } } { \partial \dot { \iota } } = - \cos \Omega \cos \dot { \omega } , } \\ { \displaystyle \frac { \partial \gamma } { \partial \lambda } = \gamma ^ { \prime \prime } \sin \omega , } & { \displaystyle \frac { \partial \gamma ^ { \prime } } { \partial \dot { \iota } } = \gamma ^ { \prime \prime } \cos \omega , \quad \displaystyle \frac { \partial \gamma ^ { \prime \prime } } { \partial \dot { \iota } } = - \sin \dot { \iota } . } \end{array} \right.
$$

Theie aie as many brackets to be computed as there are combinations of the six clements taken two at ${ \mathfrak { a } } ,$ time, or $\frac { 6 ! } { 2 ! 4 ! } = 1 5$ Thrce of them imvolve elements of only the first gioup,nne, one element of the first gioup and one of the second,and three,elements of only thc second gioup Let $\kappa$ and $I$ leplesent any of the elements of the fist gioup, $\textstyle \mathbf { \ 6 6 } , \mathbf { \ 1 } , \mathbf { \ 6 }$ and $\pmb { P }$ and $\mathcal { Q }$ any of the elemcnts of the second gioup, $a , \ e , \ \sigma$ ，Then the Lagiangian brackets to be computed aic

$$
\left\{ \begin{array} { l l } { ( a ) } & { [ K , L ] = \displaystyle \delta \left\{ \frac { \partial \cdot } { \partial K } \frac { \partial \cdot ^ { \prime } } { \partial L } - \frac { \partial \cdot ^ { \prime } } { \partial K } \frac { \partial \cdot } { \partial L } \right\} , ~ ( 3 \mathrm { ~ e q u a t i o n s } ) , } \\ { ( b ) } & { [ K , P ] = \displaystyle \mathcal { S } \left\{ \frac { \partial \cdot } { \partial K } \frac { \partial \cdot ^ { \prime } } { \partial P } - \frac { \partial \cdot ^ { \prime } } { \partial K } \frac { \partial \cdot } { \partial P } \right\} , ~ ( 9 \mathrm { ~ e q u a t i o n s } ) , } \\ { ( c ) } & { [ P , ~ Q ] = \displaystyle \mathcal { S } \left\{ \frac { \partial \cdot } { \partial P } \frac { \partial \cdot ^ { \prime } } { \partial Q } - \frac { \partial \cdot ^ { \prime } } { \partial P } \frac { \partial \cdot } { \partial Q } \right\} , ~ ( 3 \mathrm { ~ e q u a t i o n s } ) , } \end{array} \right.
$$

It is found from (46） that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \alpha } { \partial \widetilde { X } } = \xi \frac { \partial \alpha } { \partial \widetilde { X } } + \eta \frac { \partial \alpha ^ { \prime } } { \partial \widetilde { X } } , \quad } & { \displaystyle \frac { \partial \alpha ^ { \prime } } { \partial \widetilde { K } } = \xi ^ { \prime } \frac { \partial \alpha } { \partial \widetilde { X } } + \eta ^ { \prime } \frac { \partial \alpha ^ { \prime } } { \partial \widetilde { K } } , } \\ { \displaystyle \frac { \partial \alpha } { \partial P } = \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial \widetilde { P } } , \quad } & { \displaystyle \frac { \partial \tau ^ { \prime } } { \partial P } = \alpha \frac { \partial \xi ^ { \prime } } { \partial \widetilde { P } } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial P } , } \end{array} \right.
$$

and similar equations in $\pmb { \imath }$ and $\pmb { \mathscr { z } } .$

216.Computation of [ω,&],[&,e],[z,ω]. Let S mdicate that the sum of thc functions,symmetiical in α,β,and γ,is to be takcn. Thon the first cquation of (5o) bccomeg as $\mathfrak { a }$ consequence of (51)

$$
[ { \cal X } , L ] = ( \xi \eta ^ { \prime } - \eta \xi ^ { \prime } ) { \cal S } \left\{ \frac { \partial \alpha } { \partial { \cal I } } \frac { \partial \alpha ^ { \prime } } { \partial \bar { L } } - \frac { \partial \alpha ^ { \prime } } { \partial \bar { L } } \frac { \partial \alpha } { \partial \bar { L } } \right\}
$$

But the law of areas [Arl.89] gives

$$
\xi \eta ^ { \prime } - \eta \xi ^ { \prime } = \xi \frac { d \eta } { d \ell } - \eta \frac { d \xi } { d \ell } = l \wedge \sqrt { ( S + m _ { 1 } ) a ( 1 - e ^ { 2 } ) } = n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } .
$$

Therefore

$$
[ { \vec { X } } , { \vec { L } } ] = n a ^ { 2 } { \sqrt { 1 - \vartheta ^ { 2 } } } S \left\{ { \frac { \partial \alpha } { \partial { \vec { X } } } } { \frac { \partial \alpha ^ { \prime } } { \partial { \vec { L } } } } - { \frac { \partial \alpha ^ { \prime } } { \partial { \vec { X } } } } { \frac { \partial \alpha } { \partial { \vec { L } } } } \right\} .
$$

On computing the right momber of this equation by means of (47),

(48),and (49),and icducing by means of (45),the biackets involving elements of only the first gioup aic found to be

$$
\{ \begin{array} { l l } { [ { \omega , \bigotimes } ] = n a ^ { \circ } { \sqrt { 1 - { \epsilon } ^ { 2 } } } ( - \alpha \beta - \alpha ^ { \prime } \beta ^ { \prime } + \alpha \beta + \alpha ^ { \prime } \beta ^ { \prime } ) = 0 , } \\ { [ \otimes , { \iota } ] = n a ^ { \prime } { \sqrt { 1 - { \epsilon } ^ { 2 } } } \{ ( \alpha \beta ^ { \prime \prime } - \beta \alpha ^ { \prime \prime } )  \} \cos { \omega } } \\ { \qquad \quad + ( \beta ^ { \prime } \alpha ^ { \prime \prime } - \alpha ^ { \prime } \beta ^ { \prime \prime } ) \sin { \omega } \} } \\ { \qquad \quad = n a ^ { 2 } { \sqrt { 1 - { \epsilon } ^ { 2 } } } ( - \gamma ^ { \prime } \cos { \omega } - \gamma \sin { \omega } ) } \\ { \qquad = - n a ^ { 2 } { \sqrt { 1 - { \epsilon } ^ { 2 } } } \sin { \eta _ { * } } , } \\ { [ \quad { \iota } , \ { \omega } ] = - n a ^ { 2 } { \sqrt { 1 - { \epsilon } ^ { 2 } } } \{ ( \alpha ^ { \prime } \alpha ^ { \prime \prime } + \beta ^ { \prime } \beta ^ { \prime \prime } + \gamma ^ { \prime } \gamma ^ { \prime \prime } ) \cos { \omega }  } \\ { \qquad \quad \quad +  ( \alpha ^ { \prime \prime } \alpha + \beta ^ { \prime \prime } \beta + \gamma ^ { \prime \prime } \gamma ) \sin { \omega } \} = } \end{array} 
$$

217.Computation of [K,P]. The second equations of (b0) become, as $\mathfrak { a }$ consequence of (51),

$$
\begin{array} { r l } { \langle K _ { 1 } , P \rangle = \mathcal { S } \Bigg \{ \Bigg [ \xi \frac { \partial \alpha } { \partial K } + \eta \frac { \partial \alpha ^ { \prime } } { \partial K } \Bigg ] \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial P } \right] } & { } \\ { - \left[ \ell ^ { \prime } \frac { \partial \alpha } { \partial K } + \eta \frac { \partial \alpha ^ { \prime } } { \partial K } \right] \Bigg [ \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial P } \Bigg ] \Bigg \} } & { } \\ { = + \left[ \alpha \frac { \partial \alpha } { \partial K } + \beta \frac { \partial \beta } { \partial K } + \gamma \frac { \partial \gamma } { \partial K } \right] \Bigg [ \xi \frac { \partial \xi ^ { \prime } } { \partial P ^ { \prime } } - \xi ^ { \prime } \frac { \partial \xi } { \partial P } \Bigg ] } & { } \\ { + \left[ \alpha ^ { \prime } \frac { \partial \alpha ^ { \prime } } { \partial K } + \rho ^ { \prime } \frac { \partial \beta ^ { \prime } } { \partial K } + \gamma \frac { \partial \gamma ^ { \prime } } { \partial K } \right] \Bigg [ \eta \frac { \partial \eta ^ { \prime } } { \partial P ^ { \prime } } - \eta ^ { \prime } \frac { \partial \eta } { \partial P } \Bigg ] } & { } \\ { + \left[ \alpha \frac { \partial \alpha ^ { \prime } } { \partial K } + \beta \frac { \partial \beta ^ { \prime } } { \partial K } + \gamma \frac { \partial \gamma ^ { \prime } } { \partial K } \right] \Bigg [ \eta \frac { \partial \xi ^ { \prime } } { \partial P ^ { \prime } } - \eta ^ { \prime } \frac { \partial \xi } { \partial P } \Bigg ] } & { } \\ { + \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial K } + \rho ^ { \prime } \frac { \partial \beta } { \partial K } + \gamma ^ { \prime } \frac { \partial \gamma ^ { \prime } } { \partial K } \right] \Bigg [ \xi \frac { \partial \eta ^ { \prime } } { \partial P } - \gamma ^ { \prime } \frac { \partial \xi } { \partial P } \Bigg ] . } & { } \end{array}
$$

It follows from equalions (45),(47), (48),and (49) that

$$
\begin{array} { r } { \alpha \frac { \partial \alpha } { \partial \widetilde { X } } + \beta \frac { \partial \beta } { \partial \widetilde { X } } + \gamma \frac { \partial \gamma } { \partial \widetilde { X } } = 0 , \qquad } \\ { \alpha ^ { \prime } \frac { \partial \alpha ^ { \prime } } { \partial \widetilde { X } } + \beta ^ { \prime } \frac { \partial \beta ^ { \prime } } { \partial \widetilde { X } } + \gamma ^ { \prime } \frac { \partial \gamma ^ { \prime } } { \partial \widetilde { X } } = 0 , \qquad } \\ { \alpha \frac { \partial \alpha ^ { \prime } } { \partial \widetilde { X } } + \beta \frac { \partial \beta ^ { \prime } } { \partial \widetilde { X } } + \gamma \frac { \partial \gamma ^ { \prime } } { \partial \widetilde { X } } = - \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \widetilde { X } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \widetilde { X } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \widetilde { X } } \right] . } \end{array}
$$

Therefore

$$
\left\{ \begin{array} { l } { { [ K , P ] = \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \widetilde { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \widetilde { K } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \widetilde { K } } \right] } } \\ { { \qquad \times \left[ \ell \frac { \partial \eta ^ { \prime } } { \partial \widetilde { P } } + \eta ^ { \prime } \frac { \partial \xi } { \partial \widetilde { P } } - \xi ^ { \prime } \frac { \partial \eta } { \partial \widetilde { P } } - \eta \frac { \partial \xi ^ { \prime } } { \partial \widetilde { P } } \right] } } \\ { { \qquad = \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \widetilde { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \widetilde { K } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \widetilde { K } } \right] \frac { \partial ( \xi \eta ^ { \prime } - \eta \xi ^ { \prime } ) } { \partial P } } } \\ { { \qquad = \widetilde { k } \sqrt { \widetilde { S } + m _ { 1 } } \left[ \alpha ^ { \prime } \frac { \partial \alpha } { \partial \widetilde { K } } + \beta ^ { \prime } \frac { \partial \beta } { \partial \widetilde { K } } + \gamma ^ { \prime } \frac { \partial \gamma } { \partial \widetilde { K } } \right] \frac { \partial \sqrt { p } } { \partial \widetilde { P } } } } \end{array} \right.
$$

Lct $\boldsymbol { P } = \boldsymbol { a } , \boldsymbol { e } , \boldsymbol { \sigma }$ in sueccssion Then it is found that

$$
\left\{ \begin{array} { l l } { { { h \sqrt { S + m _ { 1 } } } { \displaystyle { \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial a } } } = { \displaystyle { \frac { n a } { 2 } } } \sqrt { 1 - e ^ { 2 } } , } } \\ { { { h \sqrt { S + m _ { 1 } } } { \displaystyle { \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial e } } } = - { \displaystyle { \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } } } , } } \\ { { { h \sqrt { S + m _ { 1 } } } { \displaystyle { \frac { \partial \sqrt { a ( 1 - e ^ { 2 } ) } } { \partial \sigma } } } = 0 } } \end{array} \right.
$$

Let K = ω,&, in lurn in (54),and make use of (55),then it 1s found that

$$
\left\{ \begin{array} { l l } { \displaystyle [ \omega , a ] = \frac { n a } { 2 } \sqrt { 1 - e ^ { a } } , \qquad \displaystyle [ \omega , e ] = \frac { - n a ^ { 2 } e } { \sqrt { 1 - e ^ { a } } } , \qquad \displaystyle [ \omega , \sigma ] = 0 , } \\ { \displaystyle [ \delta , a ] = \frac { n a } { 2 } \sqrt { 1 - e ^ { 2 } } \cos { i _ { \star } } , \qquad \displaystyle [ i _ { \star } a ] = 0 , \qquad \displaystyle [ i _ { \star } \ e ] = 0 , } \\ { \displaystyle [ \delta , a ] = \frac { - n a ^ { 2 } o } { \sqrt { 1 - e ^ { a } } } \cos { i _ { \star } } , \qquad \displaystyle [ \otimes , \sigma ] = 0 , \qquad \displaystyle [ i _ { \star } \ e ] = 0 } \end{array} \right.
$$

218.Computatlon of [a，el, [e,o],[g，a].The third equation of (b0) bccomes,as a consequonco of (51),

$$
\begin{array} { c } { { \left[ P , Q \right] = \delta \Bigg \{ \left[ \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \stackrel { \partial \eta } { \partial \widetilde { P } } \right] \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial Q } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial Q } \right] } } \\ { { \mathrm { , } } } \\ { { \mathrm { - } \left[ \alpha \frac { \partial \xi ^ { \prime } } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial P } \right] \left[ \alpha \frac { \partial \xi } { \partial Q } + \alpha ^ { \prime } \frac { \partial \eta ^ { \prime } } { \partial Q } \right] \Bigg \} } } \\ { { \mathrm { } } } \\ { { \mathrm { = + } \left( \alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { \prime } \right) \Bigg [ \frac { \partial \xi } { \partial P } \frac { \partial \xi ^ { \prime } } { \partial Q } - \frac { \partial \xi } { \partial Q } \frac { \partial \xi ^ { \prime } } { \partial P } \Bigg ] } } \\ { { \mathrm { } + \left( \alpha ^ { \prime 2 } + \beta ^ { 2 } + \gamma ^ { \prime } \right) \Bigg \{ \frac { \partial \eta } { \partial P } \frac { \partial \eta ^ { \prime } } { \partial Q } - \frac { \partial \eta } { \partial Q } \frac { \partial \eta ^ { \prime } } { \partial P } \Bigg \} } } \\ { { \mathrm { } + \left( \alpha \alpha ^ { \prime } + \beta \beta ^ { \prime } + \gamma \gamma ^ { \prime } \right) \Bigg [ \frac { \partial \xi } { \partial P } \frac { \partial \eta ^ { \prime } } { \partial Q } - \frac { \partial \xi } { \partial Q } \frac { \partial \eta ^ { \prime } } { \partial P } + \frac { \partial \xi ^ { \prime } } { \partial Q } \frac { \partial \eta } { \partial P } - \frac { \partial \xi ^ { \prime } } { \partial P } \frac { \partial \eta } { \partial Q } \Bigg ] } } \end{array}
$$

Asa congequencc of equations (45),the right member of this equation reduces to

$$
[ P , \ Q ] = { \frac { \partial \xi } { \partial P } } { \frac { \partial \xi ^ { \prime } } { \partial Q } } - { \frac { \partial \xi } { \partial Q } } { \frac { \partial \xi ^ { \prime } } { \partial P } } + { \frac { \partial \eta } { \partial P } } { \frac { \partial \eta ^ { \prime } } { \partial Q } } - { \frac { \partial \eta } { \partial Q } } { \frac { \partial \eta ^ { \prime } } { \partial P } }
$$

Since the brackets do not contan the time explicitly t may be given any value after the partial derivatives have been foimed The partial deuvatives become the simplest when t = T, the time of pcrihelion passage.Foi this value of t,E = O,r= a(1 - e), and il is found from equations (46) that\*

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \xi } { \partial a } = 1 - e _ { \star } \frac { \partial \eta } { \partial a } = 0 , } & { \displaystyle \frac { \partial \xi ^ { \prime } } { \partial a } = 0 , \quad \displaystyle \frac { \partial \eta ^ { \prime } } { \partial a } = - \frac { n } { 2 } \sqrt { \frac { 1 + e } { 1 - e } } , } \\ { \displaystyle \frac { \partial \xi } { \partial a } = - a , \quad \displaystyle \frac { \partial \eta } { \partial e } = 0 , \quad \displaystyle \frac { \partial \xi ^ { \prime } } { \partial e } = 0 , \quad \displaystyle \frac { \partial \eta ^ { \prime } } { \partial e } = \frac { 1 } { 1 - e } \cdot \frac { n a } { \sqrt { 1 - e ^ { 2 } } } , } \\ { \displaystyle \frac { \partial \xi } { \partial \sigma } = 0 , \quad \displaystyle \frac { \partial \eta } { \partial \sigma } = a \sqrt { \frac { 1 + e } { 1 - e } } , \quad \displaystyle \frac { \partial \xi ^ { \prime } } { \partial \sigma } = \frac { - n a } { ( 1 - e ) ^ { 2 } } , \quad \displaystyle \frac { \partial \eta ^ { \prime } } { \partial \sigma } = 0 } \end{array} \right.
$$

Then equation (（67） gives

$$
\{ a , e \} = 0 , \ \quad \ [ e , \sigma ] = 0 , \ \quad \ [ \sigma , a ] = \frac { n a } { 2 }
$$

On making use of the fact that [α αjl = -[αj,α]and equataons (53)，(56),and (59),equations (33) become

$$
\left\{ \begin{array} { l } { { \displaystyle { \frac { n a } { 2 } } \sqrt { 1 - e ^ { 2 } } { \frac { d a } { d t } } - { \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } } { \frac { d e } { d t } } = m _ { 2 } { \frac { \partial R _ { 1 , 2 } } { \partial \omega } } , } } \\ { { \displaystyle ~ \cdot = \cdot \sqrt { 1 - e ^ { 2 } } \sin i { \frac { d a } { d t } } + { \frac { n a } { 2 } } \sqrt { 1 - e ^ { 2 } } \cos i { \frac { d a } { d t } } } } \\ { { \displaystyle ~ - { \frac { n a ^ { 2 } e } { \sqrt { 1 - e ^ { 2 } } } } \cos i { \frac { d a } { d t } } = m _ { 2 } { \frac { \partial R _ { 1 } } { \partial \vartheta } } , } } \\ { { \displaystyle n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin i { \frac { d \vartheta } { d t } } = m _ { 2 } { \frac { \partial R _ { 1 , 2 } } { \partial \vartheta } } , } } \end{array} \right. ,
$$

\*It should be iomembered that a and e enter oxplcitly and also impliotly through Eandn,for isdefined by tho cquation

$$
E - e \sin \it { \Delta } E = n ( { \it \Delta } l - T ) \it { \Delta } = \frac { k \sqrt { S + m _ { 1 } } } { a ^ { 2 } } ( { \it \Delta } l - T ) .
$$

Then,eg, = cos E-e- a nin $\mathcal { B } \frac { \partial \mathcal { B } } { \partial \mathcal { a } } = \mathbf { 1 } - \boldsymbol { \mathscr { e } }$ whon $\ell = \pmb { \mathcal { Z } } ,$ eto

$$
\left\{ \begin{array} { l l } { - \displaystyle \frac { n a } { 2 } \sqrt { 1 - { \varrho } ^ { 2 } } \displaystyle \frac { d \omega } { d \ell } - \displaystyle \frac { n a } { 2 } \sqrt { 1 - { \varrho } ^ { 2 } } \cos \ast \displaystyle \frac { d \Omega } { \partial \ell } - \displaystyle \frac { n a } { 2 } \displaystyle \frac { d \sigma } { d \ell } = m _ { 2 } \displaystyle \frac { \partial { \cal R } _ { 1 , 2 } } { \partial a } , } \\ { \displaystyle \frac { n a ^ { 2 } \varrho } { \sqrt { 1 - { \varrho } ^ { 2 } } } \displaystyle \frac { d \omega } { d \ell } + \displaystyle \frac { n a ^ { 2 } \varrho \cos \ast } { \sqrt { 1 - { \varrho } ^ { 2 } } } \displaystyle \frac { d \Omega } { d \ell } = m _ { 2 } \displaystyle \frac { \partial { \cal R } _ { 1 , 2 } } { \partial \varrho } , } \\ { \displaystyle \displaystyle \frac { n a } { 2 } \displaystyle \frac { d a } { d \ell } = m _ { 2 } \displaystyle \frac { \partial { \cal R } _ { 1 , 2 } } { \partial \sigma } } \end{array} \right.
$$

These equations are easily solved for the deiivatives, and give

$$
\begin{array} { r } { \left\{ \frac { d \Delta } { d t } = \frac { \eta \alpha _ { \alpha } } { \pi a ^ { 2 } \sqrt { 1 - \varrho } ^ { 6 } \sin \alpha } \frac { \partial \widehat { L } _ { 1 , 2 } } { \partial t } , \right. } \\ { \left\{ \frac { d \Delta } { d t } \right. = \frac { \eta \alpha _ { 0 } \cos \alpha _ { 1 } } { \pi a ^ { 2 } \sqrt { 1 - \varrho } ^ { 6 } \sin \alpha } \frac { \partial \widehat { L } _ { 1 , 4 } } { \partial \alpha } - \frac { \eta \alpha _ { 0 } } { \pi a ^ { 2 } \sqrt { 1 - \varrho } ^ { 6 } \sin \alpha } \frac { \partial \widehat { L } _ { 1 , 4 } } { \partial \beta } , } \\ { \left. \frac { d \omega } { d t } \right. = \frac { - \eta \alpha _ { 0 } \cos \alpha _ { 1 } } { \pi a ^ { 2 } \sqrt { 1 - \varrho } ^ { 6 } \sin \alpha } \frac { \partial \widehat { L } _ { 1 , 2 } } { \partial t } + \frac { \eta \alpha _ { 0 } \sqrt { 1 - \varrho } } { \pi a ^ { 3 } \varrho } \frac { \partial \widehat { L } _ { 1 , 2 } } { \partial \varrho } , } \\ { \left. \frac { d \alpha } { d t } \right. = \frac { 2 m _ { 0 } } { \pi a } \frac { \partial \widehat { L } _ { 1 , 2 } } { \partial \sigma } , } \\ { \left\{ \frac { d \theta } { d t } \right. } = \frac { \pi a ( 1 - \mathfrak { e } ) } { \pi a ^ { 6 } \sigma } \frac { \partial \widehat { L } _ { 1 , 2 } } { \partial \sigma } - \frac { \eta \alpha _ { 0 } \sqrt { 1 - \varrho } } { \pi a ^ { 2 } \sigma } \frac { \partial \widehat { B } _ { 1 , 1 } } { \partial \sigma } ,  \\ { \left. \frac { d \alpha } { d t } \right. = - \frac { \eta \alpha ( 1 - \mathfrak { e } ) } { \pi a ^ { 2 } \sigma } \frac { \partial \widehat { R } _ { 1 , 2 } } { \partial \mathfrak { e } } - \frac { 2 m _ { 0 } } { \pi a } \frac { \partial \widehat { R } _ { 1 , 2 } } { \partial \mathfrak { e } } , } \end{array}
$$

The perturbative function Ri, involves the element a explicitly, and also implicitly thr'ough n which ente1s only in the combnation nt +o.Consequcntly the last cquation of (61） becomes

$$
\frac { d \sigma } { d t } = - \frac { m _ { 2 } ( 1 - e ^ { 2 } ) } { n a ^ { 2 } e } \frac { \partial R _ { 1 , 2 } } { \partial e } - \frac { 2 m _ { 2 } } { n a } \bigg ( \frac { \partial R _ { 1 , 2 } } { \partial a } \bigg ) - \frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , 2 } } { \partial n } \frac { \partial n } { \partial a } ,
$$

where the partial doiivalive in parenthesis mdicates the derivative is taken only so far as thc paiametel appears expliaitly.

It follows from lhe combinalion nt +g that

$$
\frac { 2 m _ { 2 } } { n a } \frac { \partial R _ { 1 , ~ 2 } } { \partial n } = \frac { 2 m _ { 2 } \ell } { n a } \frac { \partial R _ { 1 , ~ 2 } } { \partial \sigma } = t \frac { \dot { d } a } { \dot { d t } }
$$

It will bo shown [Arts.225-227] that R2 is sum of periodic terms;therefore g,as defined by (02), contains terms which are the products of t and trigonometiic termsIt is obvious'that such an element is inconvenienl when large values of t are to be used.

In order to avoid this dlifficulty Leverrier used\* in place of $\pmb { \sigma }$ the mean longitude from the perhelion as an element It is defined by

$$
l = \int n d t + \sigma ,
$$

whence

$$
\begin{array} { r } { \frac { d \vec { l } } { d ^ { \prime } } = n + l \frac { d n } { d \vec { t } } + \frac { d \sigma } { d \vec { t } } . } \end{array}
$$

Simee $n = { \frac { k { \sqrt { S + m _ { 1 } } } } { a ^ { \sharp } } }$ ,it folows that

$$
\frac { \partial n } { \partial a } = - \frac { 3 } { 2 } \frac { n } { a } , \quad \quad \quad \frac { d n } { d t } = - \frac { 3 n } { 2 a } \frac { d a } { d t } .
$$

Thereforo cquation (6b) becomcs, on making use of (62),

$$
\frac { d l } { d t } = n - \frac { m _ { 2 } ( 1 - e ^ { 2 } ) } { n a ^ { 2 } e } \frac { \partial R _ { 1 , 2 } } { \partial \theta } - \frac { 2 m _ { 2 } } { n a } \left( \frac { \partial R _ { 1 , 2 } } { \partial a } \right) .
$$

Since $\frac { \partial { R _ { 1 , ~ 2 } } } { \partial { \sigma } } = \frac { \partial { R _ { 1 , ~ 2 } } } { \partial { l } }$ tfortdfa the paitial derivative of $\scriptstyle R _ { 1 , \ 2 }$ with iespecl to $\pmb { \sigma }$ occurs, will not be changed in forin Hence,if $\downharpoonright$ 1s used in place of $\pmb { \sigma }$ throughout (61), the équations will be unchanged in form,and the partial derivative of $R _ { 1 , \mathrm { ~ 2 ~ } }$ with respect to $\pmb { a }$ is to bc taken only so far as $\pmb { a }$ occu1s explicitly.

219.Change from $\delta \phi , \ \omega ,$ and $\pmb { \sigma }$ to $6 6 , \pi ,$ and $\bullet$ The transformation from the elements $\begin{array} { r l } { \Omega , } & { { } \omega , } \end{array}$ and $\pmb { \sigma }$ to $\pmb { \Omega }$ ， ${ \pmb { \pi } } _ { ; }$ and $\pmb { \ 6 }$ 1s readily made because the relationg between the ω and $\pmb { \sigma }$ and tho $\pmb { \pi }$ and eare very simple It follows from the definitions of Arts. 214 and 215 that

$$
\left\{ \begin{array} { l l } { \delta \mathbb { 3 } = \mathbb { \delta } , } \\ { \omega = \pi - \mathbb { \delta } , } \\ { \sigma = \epsilon - \pi ; } \end{array} \right.
$$

whence

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d \Omega \delta } { d t } = \frac { d \Omega } { d t } , } \\ { \displaystyle \frac { d \omega } { d t } = \frac { d \pi } { d t } - \frac { d \Omega } { d t } , } \\ { \displaystyle \frac { d \sigma } { d t } = \frac { d \epsilon } { d t } - \frac { d \pi } { d t } . } \end{array} \right.
$$

On solving (68) for $\Omega , \pi ,$ and e in terms of $\Omega , \omega ,$ and $\pmb { \sigma } _ { i }$ it is found that

\*Annales de P'Obseruatore de Pars, vol $\texttt { I } , \texttt { p }$ 255

$$
\left\{ \begin{array} { l l } { \delta = \ \delta , } \\ { \pi = \omega + \Omega , } \\ { \epsilon = \sigma + \pi = \sigma + \omega + \Omega . } \end{array} \right.
$$

Henco the tiansfoimalions m the partaal deiivatives aie given by the cquations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial \Omega } \sim \left( \frac { \partial R _ { 1 , 2 } } { \partial \Delta } \right) \frac { \partial \Delta } { \partial \partial } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \tau } \right) \frac { \partial \tau } { \partial \Delta } + \left( \frac { \partial R _ { 1 , 1 } } { \partial \varepsilon } \right) \frac { \partial \varepsilon } { \partial \Delta } } \\ { \displaystyle \qquad - \left( \frac { \partial R _ { 1 , 2 } } { \partial \Delta } \right) + \left( \frac { \partial R _ { 1 , 2 } } { \partial \tau } \right) + \left( \frac { \partial R _ { 1 , 5 } } { \partial \varepsilon } \right) , } \\ { \displaystyle \frac { \partial R _ { 1 , 2 } } { \partial \omega } = \left( \frac { \partial R _ { 1 , 2 } } { \partial \Delta } \right) \frac { \partial \Delta } { \partial \omega } + \left( \frac { \partial R _ { 1 , 2 } } { \partial \tau } \right) \frac { \partial \tau } { \partial \omega } + \left( \frac { \partial R _ { 1 , 1 } } { \partial \varepsilon } \right) \frac { \partial \varepsilon } { \partial \omega } } \\ { \displaystyle \qquad - \left( \frac { \partial R _ { 1 , 2 } } { \partial \pi } \right) + \left( \frac { \partial R _ { 1 , 2 } } { \partial \varepsilon } \right) , } \\ { \displaystyle \frac { \partial R _ { 1 , 3 } } { \partial \omega } = \left( \frac { \partial R _ { 1 , 2 } } { \partial \Delta } \right) \frac { \partial \Delta } { \partial \sigma } + \left( \frac { \partial R _ { 1 , 3 } } { \partial \varepsilon } \right) \frac { \partial \tau } { \partial \sigma } + \left( \frac { \partial R _ { 1 , 3 } } { \partial \varepsilon } \right) \frac { \partial \varepsilon } { \partial \omega } } \\ { \displaystyle \qquad - \left( \frac { \partial R _ { 1 , 2 } } { \partial \varepsilon } \right) } \end{array} \right.
$$

On substatuting (69) and (71) m (61)and omitting the paienthescs alound the partial derivalivcs,and on solvmg for the derivatives ot tho clements wilh icspcct to t,it is found that

$$
\begin{array} { r l } & { \begin{array} { r l } & { \{ \frac { \partial G } { \partial t } = - \frac { m _ { k - 1 } } { \omega ^ { 2 } } , \frac { \partial M _ { k - 2 } } { \partial t } , } \\ & { \{ \frac { \partial G } { \partial t } = - \frac { m _ { k - 1 } } { \omega ^ { 2 } } , \frac { \partial M _ { k - 1 } } { \partial t } + \frac { \partial m _ { k - 1 } } { \partial t } , } \\ & { \{ \frac { \partial G } { \partial t } = - \frac { - m _ { k - 1 } } { \omega ^ { 2 } } , \frac { \partial M _ { k - 2 } } { \partial t } , + \frac { \partial m _ { k - 1 } } { \partial t } , - \frac { \partial m _ { k - 1 } } { \partial t } , \frac { \partial M _ { k - 2 } } { \partial t } + \frac { \partial \overline { { M } } _ { k + 2 } } { \partial t } , \} , } \end{array}  } \\ & { \begin{array} { r l } & { \{ \frac { \partial M _ { k } } { \partial t } = - \frac { m _ { k - 1 } } { \omega ^ { 2 } } , \frac { \partial M _ { k - 1 } } { \partial t } , } \\ & { \{ \frac { \partial M _ { k } } { \partial t } = - \frac { m _ { k - 1 } } { \omega ^ { 2 } } \} , } \\ & {  { \partial M _ { k } } { \partial t } = - \frac { \partial m _ { k - 1 } } { \omega ^ { 2 } } , } \end{array}  } \end{array}  \\ &  \begin{array} { r l } & { \{ \frac { \partial M _ { k } } { \partial t } = - \frac { \partial m _ { k - 1 } } { \partial t } , \frac { \partial M _ { k - 1 } } { \partial t } , + \frac { \partial m _ { k } } { \partial t } , \frac { \partial m _ { k - 2 } } { \partial t } , \frac { \partial M _ { k - 1 } } { \partial t } , } \\ & { \{ \frac { \partial M _ { k } } { \partial t } = - \frac { m _ { k - 1 } } { \omega ^ { 2 } } , \frac { \partial M _ { k - 1 } } { \partial t } , \frac { \partial m _ { k - 1 } } { \partial t } , - \frac { \partial m _ { k - 1 } } { \partial t } , \frac { \partial m _ { k - 1 } } { \partial t } , \frac { \partial m _ { k - 2 } } { \partial t } , } \\ &  \{ \frac { \partial G } { \partial t } = - \frac  m _ \end{array}
$$

These cquations,\* together with the coircspondmg ones foi the elements of the planct $m _ { 2 } ,$ constitute a rigorous systom of diffelential cquations for the detcimination of the motion ol tho planets ${ \mathit { n } } _ { \mathit { 1 } }$ and $\pmb { m _ { 2 } }$ with iespcct to the sun whcn theie &ic no other forces than the mutual altiactions of the thiee bodics

If $R _ { 1 , 2 }$ 1s cxpiessed in teims of the time and the osculating elements at the cpoch $\mathbf { \delta } _ { t _ { 0 } , \ldots } ^ { t _ { \phantom { + } } }$ equations (72） become the explicit expressions for the fist half of the system (27),and dcfinc the perturbations of the clements which are of the first order with respect to thc masses

220.Introduction of Rectangular Components of the Disturbing Acceleration. Equations (72) icqulc fol thcir application that, $R _ { 1 , \cdot 2 }$ shall be exprcssed fisl in leims of the clements,after which the partial deiivatives must bc foimed In somc cascs, cspecially in the obits of comcts,it 1s advantageous to have the ratcs of vaiiation of the elements expicssed in terms of thrce iectangulai components of the disturbing acccleiation

The distubing acceleiation will bc resolved into threc icctangulal components W，S, $R$ ，whcie W is the componcnt of accelcration peipendicular to the plane of the oibit with thc positive duection toward the north polc, $\pmb { \ S }$ 1s the componeni m thc planc of the orbit which acts at right angles lo the radius vector with tho posilive ducction making an angle less than $9 0 ^ { \circ }$ with the diection of motion, $\scriptstyle { R }$ is thc component acting along thc ladius vcctol with the positivc dncction away from tho sun. The components uscd in the preceding chaplcr cvidontly might be employed heie instead of these,but the iesulting equations would be less simple

In oider to obtain the desired cquations it is only necessary to expiess the paitial deiivativcs of ${ \displaystyle R _ { 1 , 2 } }$ with respeot to thc elements in terms of $W , \ S ,$ and ${ \mathbf { } } R ,$ and to substitute them in (61) or (72),depending upon the set of elements uscd The tiansformation willbe made fo1 the eloments uscd m cquations (61)

The quantites $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial x }$ 1 $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial y }$ $m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial z }$ are the components of the disturbing acceleiation parallel to the fixed axes of referenco.It follows from the elementary properties of the resolution and composition of accolerations that mg ${ { m } _ { 2 } } \frac { \partial R _ { 1 , 2 } } { \partial x }$ 1s equal to the sum of the piojections of W,S,and R upon the v-axis, and simlaily fon the otheis

Let u iepicsent the agument of thc latitude,or the distance fiom the ascending node to the planet P,Fig 61Then it follows fiom the fundamental formulag of Trigonometry that

![](../chunks/An-Introduction-To-Celestial-Mechanics_part_0006_pages_0351-0420/auto/images/2086b2e7e3866a7b3514ce51c566a375a7d329f51d75e97f5630f5255812f45f.jpg)  
Fig 61

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \nu } = + R ( \cos \mathrm { ~ } u \mathrm { ~ e o s ~ } \Omega \mathrm { ~ - } \sin \mathrm { ~ } u \mathrm { ~ s i n ~ } \Omega \mathrm { ~ e o s ~ } \imath ) } \\ { \qquad - \mathrm { ~ } \delta ( \sin \mathrm { ~ } u \mathrm { ~ e o s ~ } \Omega \mathrm { ~ - } \cos u \mathrm { ~ s i n ~ } \Omega \mathrm { ~ e o s ~ } \imath ) } \\ { \qquad + W \mathrm { ~ s i n ~ } \Omega \mathrm { ~ s i n ~ } \imath , } \\ { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \mathcal { Y } } = + R ( \cos \mathrm { ~ } u \mathrm { ~ s i n ~ } \Omega \mathrm { ~ + ~ } \sin \mathrm { ~ } u \mathrm { ~ c o s ~ } \Omega \mathrm { ~ s o ~ } \imath ) } \\ { \qquad - \mathrm { ~ } \delta ( \sin \mathrm { ~ } u \mathrm { ~ s i n ~ } \Omega \mathrm { ~ - } \cos u \mathrm { ~ c o s ~ } \otimes \mathrm { ~ c o s ~ } \imath ) } \\ { \qquad - \mathrm { ~ } W \mathrm { ~ e o s ~ } \otimes \mathrm { ~ s i n ~ } \imath , } \\ { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \mathcal { Z } } = + R \sin \mathrm { ~ } u \mathrm { ~ s i n ~ } \imath + S \cos u \mathrm { ~ s i n ~ } \imath + W \cos \mathrm { ~ } \imath } \end{array} \right. } \end{array}
$$

Let s repiesent any of thc elements &,· ,g, then

$$
\small \frac { \partial R _ { 1 , 2 } } { \partial s } = \frac { \partial R _ { 1 , 2 } } { \partial \tau } \frac { \partial z } { \partial s } + \frac { \partial R _ { 1 , 2 } } { \partial y } \frac { \partial y } { \partial s } + \frac { \partial R _ { 1 , 2 } } { \partial z } \frac { \partial z } { \partial s } .
$$

The dervataves $\frac { \partial R _ { 1 , 2 } } { \partial x } , \frac { \partial R _ { 1 , 2 } } { \partial y } , \frac { \partial R _ { 1 , 2 } } { \partial z } \approx \mathrm { r e }$ givep in（73） and when $\frac { \partial \mathfrak { x } } { \partial \mathfrak { s } } , \frac { \partial \mathfrak { y } } { \partial \mathfrak { s } }$ ， and $\frac { \partial { z } } { \partial { s } }$ have beon found, tho transformation can be completed at once.

It follows from cquations (51） that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \mathfrak { c } } { \partial \mathcal { K } } = \xi \frac { \partial \alpha } { \partial \mathcal { K } } + \eta \frac { \partial \alpha ^ { \prime } } { \partial \mathcal { K } } , \quad } & { \displaystyle \frac { \partial \mathfrak { x } } { \partial P } = \alpha \frac { \partial \xi } { \partial P } + \alpha ^ { \prime } \frac { \partial \eta } { \partial P } , } \\ { \displaystyle \frac { \partial \eta } { \partial \mathcal { K } } = \xi \frac { \partial \beta } { \partial \mathcal { K } } + \eta \frac { \partial \beta ^ { \prime } } { \partial \mathcal { K } } , \quad } & { \displaystyle \frac { \partial \mathcal { V } } { \partial P } = \beta \frac { \partial \xi } { \partial P } + \beta ^ { \prime } \frac { \partial \eta } { \partial P } , } \\ { \displaystyle \frac { \partial z } { \partial \mathcal { K } } = \xi \frac { \partial \gamma } { \partial \mathcal { K } } + \eta \frac { \partial \gamma ^ { \prime } } { \partial \mathcal { K } } , \quad } & { \displaystyle \frac { \partial z } { \partial P } = \gamma \frac { \partial \xi } { \partial P } + \gamma ^ { \prime } \frac { \partial \eta } { \partial P } , } \end{array} \right.
$$

where $\kappa$ is any of the elements $\begin{array} { r } { \big \Omega , \textit { \textbf { \ i } } _ { \mathbf { \omega } } \omega , } \end{array}$ and $P$ any of the clcments $a , e , \sigma$ The quanlities $\alpha , \mathrm { ~ \pmb ~ { \mathscr { I } } ~ } , \tau ^ { \prime }$ ae defined in (44),and their deivatives aie given in (47),(48),and (-9),the dorivatives $\frac { \partial \xi } { \partial \bar { P } }$ and $\frac { \partial \eta } { \partial P }$ are to be computed from (46).

It is found after some iather long but simple icductions that

$$
\begin{array} { r } { \{ \begin{array} { l l } { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \Delta } = \mathcal { S } r \cos \mathfrak { s } - W r \cos \mathfrak { s } \mathrm { ~ a n ~ } \mathfrak { s } , } \\ { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { s } } -  \mathcal { V } r \sin \mathfrak { u } , } \\ { m _ { 3 } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { s } } - \mathcal { S } r , } \\ { m _ { 4 } \frac { \partial R _ { 1 , 2 } } { \partial \omega } = \mathcal { S } , } \\ { m _ { 2 } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { u } } = \mathcal { R } \frac { \mathcal { T } } { \mathfrak { a } } , } \\ { m _ { 3 } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { s } } = - \mathcal { T } a \cos \mathfrak { s } + \mathcal { S } [ 1 + \frac { 1 } { p } ] a \sin \mathfrak { v } , } \\ { m _ { 4 } \frac { \partial R _ { 1 , 2 } } { \partial \mathfrak { v } } = \frac { \mathcal { T } a \omega } { \sqrt { 1 - \mathfrak { s } } ^ { \circ } } \frac { \sin \mathfrak { s } } { \nu \mathrm { I - \mathfrak { s } } ^ { \circ } } + \delta \frac { \partial \mathfrak { s } } { \mathcal { T } } \sqrt { 1 - \mathfrak { e } ^ { 2 } } } \end{array}  } \end{array}
$$

Therefore equations (61） become

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \Omega } { d t } = \frac { \gamma \sin u } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin i } \cdot \dot { W } , } & \\ { \displaystyle \frac { d \dot { u } } { d t } = \frac { r \cos u } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } W , } & \\ { \displaystyle \frac { d \omega } { d t } = \frac { - \sqrt { 1 - e ^ { 2 } } \cos v } { n a e } R + \frac { \sqrt { 1 - e ^ { 2 } } } { n a e } \bigg [ 1 + \frac { r } { p } \bigg ] \sin v \mathrm { \mathcal { S } } } & \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - \frac { r \sin u \cos \omega } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \dot { W } , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d a } { d l } = \frac { 2 e \sin v } { n \sqrt { 1 - e ^ { 2 } } } R + \frac { 2 a \sqrt { 1 - e ^ { 2 } } } { n \eta } S , } \\ { \displaystyle \frac { d \theta } { d l } = \frac { \sqrt { 1 - e ^ { 2 } } \sin v } { n a } R + \frac { \sqrt { 1 - e ^ { 2 } } } { n a ^ { 2 } e } \Big [ \frac { a ^ { 2 } ( 1 - e ^ { 2 } ) } { \eta } - \mathrm { \ } \mathrm { \ } \Big ] S , } \\ { \displaystyle \frac { d \sigma } { d t } = - \frac { 1 } { n a } \Big [ \frac { 2 a } { a } - \frac { 1 - e ^ { 2 } } { \theta } \mathrm { c o s } v \Big ] R } \\ { \displaystyle \qquad - \frac { ( 1 - e ^ { 2 } ) } { n a e } \Big [ 1 + \frac { 2 } { \eta } \Big ] \sin v . } \end{array} \right.
$$

# XXVI PROBLEMS

1 Fnd tho componcnlg S andl R of this chaptei im terms of T' and N, which wero uscd im chaplol Ix,Ait 174

$$
\left\{ \begin{array} { l l } { S = \displaystyle \frac { ( 1 + c \cos { \vartheta } ) } { \sqrt { 1 + c ^ { 2 } + 2 } \theta \cos { \upsilon } } + \frac { e \sin { \vartheta } } { \sqrt { 1 + \vert c \vert + 2 c \cos { \upsilon } } } N , } \\ { R = \displaystyle \frac { o \sin { \upsilon } } { \sqrt { 1 + c ^ { 2 } + 2 c \cos { \upsilon } } } \frac { r } { \cos { \vartheta } } - \frac { 1 + e \cos { \upsilon } } { \sqrt { 1 + e ^ { 2 } + 2 e \cos { \upsilon } } } \widetilde { N } } \end{array} \right.
$$

2 By mcang of tho cquations of problem 1 cpiesg tho vaiintions ot tne cloments $\pmb { \Omega }$ ,gin torms of T and N,and venfy all tho iesultg contained in the Table ofAit 182

3 Explain why $\frac { d \omega } { d t }$ conlang a toim depending upon W

4Suppose the diatubed body moveg in n resisting medium，find the eantiong fol thc vaiiations of the eloments

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \frac { d \Delta \alpha } { d t } = 0 , } \\ { \frac { d \Delta } { d t } = 0 , } \\ { \frac { d \alpha } { d t } = \frac { 2 \sqrt { 1 - e ^ { - \alpha } } } { n \omega } \frac { \sinh { \theta } } { \sqrt { 1 + e ^ { - \alpha } + 2 \cos v } } \mathcal { P } , } \\ { \frac { d \alpha } { d t } = \frac { 2 \sqrt { 1 + e ^ { - \alpha } + 2 \cos v } } { n \sin v + 1 - e ^ { - \alpha } } \mathcal { P } , } \\ { \frac { d \alpha } { d t } = \frac { 2 \sqrt { 1 - e ^ { - \alpha } + ( \cos v + \frac { \theta } { 2 } ) } } { n \omega \sqrt { 1 + e ^ { - \alpha } + 2 \cos v } } \mathcal { P } , } \\ { \frac { d \alpha } { d t } = \frac { 2 \sqrt { 1 - e ^ { - \alpha } + ( \cos v + \frac { \theta } { 2 } ) } } { n \omega \sqrt { 1 + e ^ { - \alpha } + 2 \cos v } } , } \\ { \frac { d \alpha } { d t } = - \frac { 2 ( 1 - e ^ { \alpha } ) ( 1 + \frac { \alpha } { 2 } + \frac { \alpha } { 4 } - \cos v \sin { \theta } ) \sin v } { n \omega ( 1 + e ^ { - \alpha } + \cos v \sin v ) \sqrt { 1 + e ^ { - \alpha } + 2 e \cos v } } \mathcal { I } } \\ { \frac { d \alpha } { d t } = - \frac { 2 ( 1 - e ^ { \alpha } ) ( 1 + 1 - e ^ { - \alpha } ) } { n \omega ( 1 + e ^ { \alpha } + \cos v \sin v ) \sqrt { 1 - e ^ { - \alpha } + \frac { 2 \cos v } { 2 } + \frac { \sin v } { 2 } + \frac { \sin v } { 2 } + \frac { \sin v } { 2 } + \cos v } } \mathcal { I } } \end{array} \right. } \end{array}
$$

5 Discus the wny in whieh tho clementg vay m tho lasl pioblem, mcluding the values of v foi which the mnxima and mimima in then iates of change occur,when T'1s a constant, and when il varicg ns tho squnte of tho velocity.

6.Derive the cquations coriesponding to (77) for the elementa $\delta \delta , \uparrow , \pi _ { \uparrow }$ ${ \mathfrak { a } } , e _ { 3 }$ and e

$$
\left\{ \begin{array} { l l } { \frac { d \Omega } { d t } = \frac { \gamma \sin { u } } { \pi \sin { \psi } _ { 1 } } \frac { u } { - \tilde { \sigma } \sin { \psi } _ { 1 } } } \\ { \frac { d \Omega } { d t } = \frac { \gamma \cos { u } } { \pi \sin { \psi } _ { 1 } - \tilde { \sigma } } w , } \\ { \frac { d \pi } { d t } = 2 \cos { u } \frac { 1 } { 2 } \frac { d \Omega } { d t } + \frac { \sqrt { 1 - e } } { n u \cos { \psi } } \Big \{ - R \cos { v } + \mathcal { S } \Big ( 1 + \frac { \gamma } { \overline { { p } } } \Big ) \sin { v } \Big \} , } \\ { \frac { d \alpha } { d t } = \frac { 2 } { n \sqrt { 1 - e ^ { 2 } } } \Big ( R e \sin { v } + \mathcal { S } _ { 1 } ^ { D } \Big ) \ , } \\ { \frac { d \alpha } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { n \alpha } \Big \{ R \sin { v } + \mathcal { S } \Big ( \frac { e + \cos { v } } { 1 + \tilde { \sigma } \cos { v } } + \cos { v } \Big ) \Big \} , } \\ { \frac { d \alpha } { d t } = - \frac { 2 \gamma L } { n \alpha ^ { 2 } } + \frac { e ^ { 3 } } { 1 + \mathcal { I } _ { 1 } ^ { 3 } - e ^ { \frac { \alpha } { \sqrt { d t } } } } + \mathcal { I } _ { 1 } ^ { D } - \vec { \sigma } \sin { n } ^ { 3 } \frac { \partial \tilde { d } _ { 0 } ^ { 3 } } { 2 \tilde { d t } } . } \end{array} \right.
$$

221 Development of the Perturbative Function. In ordcr lo apply cquations (72) the perturbative function Ri,² must be doveloped cxphcitly in terms of the elements and the timeFiom this pomt on only perturbations of the first order will be considered，therefore,m accordancc with Lhe iesults of Ait.208, the elements which appear in Ri,² are the osculating eloments at thc timc $\smash { t _ { 0 } }$

In the notation of Art 2O5 tho perturbative function is

$$
\left\{ \begin{array} { l l } { \displaystyle R _ { 1 , 2 } = k ^ { 2 } \left[ \frac { 1 } { \gamma _ { 1 , 2 } } - \frac { \chi _ { 1 } \chi _ { 2 } + \gamma _ { 1 } \chi _ { 2 } + \chi _ { 1 } \chi _ { 2 } } { \gamma _ { 2 } \mathrm { s } ^ { 8 } } \right] , } \\ { \displaystyle r _ { 1 , 2 } = \sqrt { ( \chi _ { 2 } - \chi _ { 1 } ) ^ { 2 } + ( \chi _ { 2 } - \chi _ { 1 } ) ^ { 2 } + ( z _ { 2 } - z _ { 1 } ) ^ { 2 } } , } \\ { \displaystyle r _ { 2 } = \sqrt { \chi _ { 2 } \mathrm { s } ^ { 2 } + \chi _ { 2 } \mathrm { s } ^ { 2 } + z _ { 2 } \mathrm { s } ^ { 2 } } , } \end{array} \right.
$$

The perturbmg forces evidently depend upon the mutual inchnations of the orbits,rathel than upon thcir inclnation8 Independently to the fixed plane of reference.It will be convenient,theiefore, to develop R1,a in terms of the mutual imclination Smcc this anglc 1s expressible in lcrms of , 2z, &1,and &, the partial derivatives of Ri,& with respect to these elements will depend in part on their occurring implicitly in this anglc.

The development of the perturbative function consists of thrcc steps:\*

\*There are many moro or leas important variationg of the method outhined here,which 1 bascd on the work of Levorrier in tho Annales dc l'Obseruatoire de Par8,vol 1

(a) Devclopment of Ri, as a power series in the square of tho $( a )$ sine of half thc mutual inelination of the orbits. Ju vi

(b） Development of the cocfficients of the series obtainea in 'into nowerserics in e and ez.

(c） Development of thc coeficients of tho preceding series nuo Fourier serics in.the mean longitudes of the two planets and the anrular variables π1, π2,&i,and &2. 1larihln tn iv

In the little space available here it will not be posspie w givu more than a general outline of the operations which are necessary to effcct the complete development. A detailed discussion is givcn in Tisserand's Mecanique Celesle, vol. 1., chapters xil. to XvII.inclusive.

222.(a) Development of Ri,² in the Mutual Inclination.. Let S represent the angle between the radii ri and rz；then

$$
\frac { 1 } { r _ { 1 , 2 } } = ( r _ { 1 } { } ^ { 2 } + r _ { 2 } { } ^ { 3 } - 2 r _ { 1 } r _ { 2 } \cos \beta ) ^ { - 1 } .
$$

![](../chunks/An-Introduction-To-Celestial-Mechanics_part_0006_pages_0351-0420/auto/images/dfc30a0d4c31e0f55279cab6eac7a6f68591e909e67f08fe3246fbd8e5a7c978.jpg)  
Fig. 62.

Let the angles betweon r1 and the x, V, and z-axes be α1, β, γ1 respectively,and in thc case of r,αz,β,and Y2.. Then it follows that

$$
\begin{array} { r l } & { x _ { 1 } = r _ { 1 } \cos { \alpha _ { 1 } } , ~ y _ { 1 } = r _ { 1 } \cos { \beta _ { 1 1 } } , ~ z _ { 1 } = r _ { 1 } \cos { \gamma _ { 1 } } , ~ \mathrm { e t c . } , } \\ & { x _ { 1 } x _ { 2 } + y _ { 1 } y _ { 2 } + z _ { 1 } z _ { 2 } = r _ { 1 } r _ { 2 } ( \cos { \alpha _ { 1 } } \cos { \alpha _ { 2 } } + \cos { \beta _ { 1 } } \cos { \beta _ { 2 } } } \\ & { ~ + \cos { \gamma _ { 1 } } \cos { \gamma _ { 2 } } ) = r _ { 1 } r _ { 2 } \cos { \delta } . } \end{array}
$$

Let I represent the angle between the two orbits, and ri and r1

the distances fiom their ascendmg nodes to thel pont of inte1- section From the spherical tiianglc $\pmb { P _ { 1 } P _ { 2 } C }$ the value of cos $\pmb { \mathscr { s } }$ 18 found to be

$$
\left\{ \begin{array} { l l } { \cos \mathrm { ~  { \mathcal { S } } = \cos \left( u _ 1 - \tau _ 1 \right) ~ } \cos \left( u _ { \mathrm { 2 } } - \tau _ { 2 } \right) } \\ { \qquad \quad + \sin \left( u _ { \mathrm { 1 } } - \tau _ { 1 } \right) \sin \left( u _ { \mathrm { 2 } } - \tau _ { 2 } \right) \cos \tilde { I } , ~ \mathrm { ~ a n ~ } } \\ { \cos \mathrm { ~  { \mathcal { S } } = \cos \left( u _ 1 - u _ 2 + \tau _ 2 - \tau _ 1 \right) ~ } } \\ { \qquad \quad - 2 \sin \left( u _ { \mathrm { 1 } } - \tau _ { 1 } \right) \sin \left( u _ { \mathrm { 2 } } - \tau _ { 2 } \right) \sin ^ { 2 } \frac { \tilde { I } } { 2 } , } \\ { u _ { \mathrm { 1 } } - \tau _ { 1 } = v _ { \mathrm { 1 } } + \pi _ { 1 } - \delta _ { 1 } - \tau _ { 1 } , } \\ { u _ { \mathrm { 2 } } - \tau _ { 2 } = v _ { \mathrm { 2 } } + \pi _ { 2 } - \delta _ { 2 } - \tau _ { 2 } } \end{array} \right.
$$

The quantitics I,7i, and r2 aie deteimined by the formulas of Gauss appled to the triangle $\begin{array} { r } { \Omega _ { 1 } \partial _ { \aa } \partial _ { \aa } C ^ { \phantom { ' } } } \end{array}$

$$
\left\{ \begin{array} { l l } { \sin I \sin \tau _ { 1 } = \sin \tau _ { 2 } \sin \big ( \bigotimes _ { 1 } - \bigotimes _ { 2 } \big ) , } \\ { \sin I \sin \tau _ { 2 } = \sin \tau _ { 1 } \sin \big ( \bigotimes _ { 1 } - \bigotimes _ { 2 } \big ) , } \\ { \sin I \cos \tau _ { 1 } = \sin \tau _ { 1 } \cos \tau _ { 2 } - \cos \tau _ { 1 } \sin \tau _ { 2 } \cos \big ( \bigotimes _ { 1 } - \bigotimes _ { 2 } \big ) , } \\ { \sin I \cos \tau _ { 2 } = - \cos \tau _ { 1 } \sin i _ { 2 } + \sin \tau _ { 1 } \cos i _ { 2 } \cos \big ( \bigotimes _ { 1 } - \bigotimes _ { 2 } \big ) , } \\ { \cos I = \cos \tau _ { 1 } \cos \tau _ { 2 } + \sin i _ { 1 } \sin i _ { 2 } \cos \big ( \bigotimes _ { 1 } - \bigotimes _ { 2 } \big ) } \end{array} \right.
$$

For smplicity $I , \tau _ { 1 } ,$ and $\pmb { \tau _ { 2 } }$ will be retaimed,but il must bo iemombeicd when the partial deiivatives of $\scriptstyle R _ { 1 , \atop 2 }$ aie taken that they ae functions ot $i _ { 1 } , \ldots , \ldots$ and $\mathbf { \delta } \partial \mathbf { \delta } _ { 2 }$ ·

As a consequencc of (79)，(81)，and (82)，the peilurbativofunction can be wiitten in the foim

$$
\{ \begin{array} { l l } { R _ { 1 , 2 } = \{  \eta _ { 1 } ^ { 2 } + \eta _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos ( u _ { 1 } - u _ { 2 } + r _ { 2 } - r _ { 1 } ) \} ^ { - \sharp } } \\ { \qquad \times [ 1 + \frac { 4 r _ { 1 } r _ { 2 } \sin ( u _ { 1 } - r _ { 1 } ) \sin ( u _ { 2 } - r _ { 2 } ) \sin ^ { 2 } \frac { I } { 2 } } { \eta _ { 1 } ^ { 2 } + \eta _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos ( u _ { 1 } - u _ { 2 } + r _ { 2 } - r _ { 1 } ) } ] ^ { - \sharp } } \\ { \qquad - \frac { \eta _ { 1 } } { \eta _ { 2 } ^ { 2 } } \Big [ \cos ( u _ { 1 } - u _ { 2 } + r _ { 2 } - r _ { 1 } ) } \\ { \qquad \quad -  2 \sin ( u _ { 1 } - \tau _ { 1 } ) \sin ( u _ { 2 } - \tau _ { 2 } ) \sin ^ { 2 } \frac { I } { 2 } \Big ] } \end{array} 
$$

The iadn $\pmb { r _ { 1 } }$ and $\uparrow \uparrow$ aic indopendent of $\boldsymbol { \mathit { I } }$ The socond factor of the first term of the ught mcmbei of this cqualion can bo cxpanded by the binomial theorem into an absolutcly convcrging powcr series in sm2 $\sin ^ { 2 } { \frac { I } { 2 } }$ so long as the numcrical valueof


<!-- chunk 0007: pages 421-450 -->
$$
\frac { 4 r _ { 1 } r _ { 2 } \sin ( u _ { 1 } - \tau _ { 1 } ) \sin ( u _ { 2 } - \tau _ { 2 } ) \sin ^ { 2 } \frac { I } { 2 } } { r _ { 1 } \mathrm { ' } + r _ { 2 } \mathrm { ' } - 2 r _ { 1 } r _ { 2 } \cos ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) }
$$

is less than unity. This fraction is less than, or at most equal to,

$$
{ \frac { 4 r _ { 1 } r _ { 2 } \sin ^ { 2 } { \frac { I } { 2 } } } { ( r _ { 1 } - r _ { 1 } ) ^ { 2 } } } .
$$

If this expression is less than unity for all the values which 1 and rg can take in the given ellipses the evpansion of (84) is valid for all values of the time In the case of the major planets it is always very small, the greatest value of sin $\sin ^ { 2 } { \frac { I } { 2 } }$ being for Mercury and Mars, O Ol18 In the perturbations of the planetoids by Jupiter it often fails, for Iis sometimes of considerable magnitude while r2 - r1 may become very small In the case of Mars and Eros r - '1 may actually vanish and this mode of development consequently fails. It is needless to say that it is not generally applcable in the cometary orbits

In those cases in which the expansion of (84) does not fall, the expression for Ri,a becomes

$$
\{ \begin{array} { l l } { R _ { 1 , 2 } = + [ \eta _ { 1 } ^ { 2 } + r _ { 2 } ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) ] ^ { \frac { 1 } { 4 } } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times 2 \mathrm { ~ s i n ~ } ( u _ { 1 } - \tau _ { 1 } ) \sin ( u _ { 2 } - \tau _ { 2 } ) \sin ^ { \frac { T } { 2 } } \frac { \ d \ d \ d } { \ d t } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times 2 - 2 r _ { 1 } r _ { 2 } \cos ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) \sin ^ { \frac { T } { 2 } } \frac { \ d \ d } { \ d t } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

223. (b) Development of the Coefcients in powers of e1 and e2: The radu rand rz vary from a(1 - ei) and az(1 - ez) to a1(1 + e) and az(1 + e2) respectively. Let

$$
\begin{array} { r } { \left\{ { r _ { 1 } = a _ { 1 } ( 1 + \rho _ { 1 } ) } , \right. } \\ { \left. \qquad \right\} { r _ { 2 } = a _ { 2 } ( 1 + \rho _ { 2 } ) } . } \end{array}
$$

The angles ${ \pmb u } _ { 1 }$ and ${ \pmb u } _ { \mathbf { 2 } }$ aic expicsscd in teims of the tiuc anomalics, U1and vz,and the elements by (82)The true anomalies are equal to the mean anomalics plus the equations of the center, which may be denoted by wl and waLot l and l iepicsent the mean longitudcs counted fiom the x-axis [Fig (62)], then

$$
\left\{ \begin{array} { l l } { u _ { 1 } \ - \tau _ { 1 } = l _ { 1 } - \Omega _ { 1 } - \tau _ { 1 } + w _ { 1 } , } \\ { u _ { 2 } - \tau _ { 2 } = l _ { 2 } - \Omega _ { 2 } - \tau _ { 2 } + w _ { 2 } } \end{array} \right.
$$

It follows from (81) that Ri,a can be written in the form

$$
R _ { 1 , ~ 2 } = \bar { F } [ a _ { 1 } ( 1 + \rho _ { 1 } ) , a _ { 2 } ( 1 + \rho _ { 2 } ) ] ,
$$

where $\pmb { \mathscr { F } }$ is a homogeneous function of ${ { \mathfrak { a } } _ { 1 } }$ and ${ \pmb q } _ { \pmb { \mathrm { = } } }$ of degiee -1. Therefore

$$
R _ { 1 , 2 } = \frac { 1 } { 1 + \rho _ { 2 } } R \left[ a _ { 1 } + a _ { 1 } \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } , a _ { 2 } \right] .
$$

The right member of this cquation can bc developed by Tayloi's formula, giving

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } \displaystyle \frac { 1 } { R _ { 1 , 2 } } = \frac { 1 } { 1 + \rho _ { 2 } } \bigg \{ F ( a _ { 1 } , ~ a _ { 2 } ) + \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \frac { a _ { 1 } } { 1 } \frac { \partial \bar { F } ( a _ { 1 } , ~ a _ { 2 } ) } { \partial a _ { 1 } } } \\ & { \qquad \quad + \left( \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \right) ^ { 2 } \frac { { a _ { 1 } } ^ { 2 } } { 1 2 } \frac { \partial ^ { 2 } \bar { F } ( a _ { 1 } , ~ a _ { 2 } ) } { \partial { a _ { 1 } } ^ { 2 } } + \cdots \bigg \} . } \end{array}
$$

Thc expressions $\displaystyle \left( \frac { \rho _ { 1 } - \rho _ { 2 } } { 1 + \rho _ { 2 } } \right) ^ { }$ can be developedaspowereres p1 and p2 But in Ait 100,cquation (62),p 1s givcn as a power seiics in e whose coefficients aue cosmes of multiples of the mcan anomaly On making lhese expansions and substitulions in (91), $\scriptstyle { R _ { 1 , \ 2 } }$ can be arranged as a powcr selics in e1 and ez Thesc operations arc to be actually pefoimed upon the sepaiatc lcims of the sciics (87),so the 1esulting selies is aliangcd according to powcls of $\pmb { e _ { 1 } } , \pmb { e _ { 2 } } ,$ and $\sin ^ { 2 } \frac { I } { 2 }$ The angles $\boldsymbol { w } _ { 1 }$ and ${ \mathfrak { w } } _ { 2 }$ also dcpend upon ${ \pmb { \mathscr { e } } } _ { 1 }$ and eziespectively, but thcir devclopments will not bc introduccd until after the next step

224.(c) Developments in Fourier Series. The frst term within the biacket of (91) 1s obtained by icplacing $\pmb { r _ { 1 } }$ and $\boldsymbol { \mathscr { I } } _ { 2 }$ by ${ a } _ { 1 }$ and az lespectively in (87) The higher torms involve the derivativcs of the fist with respect to ${ \pmb a } _ { 1 }$ On ieferring to the exphcit se1es in (87),it is seen that the developmont of the expiessions of the type

$$
( a _ { 1 } a _ { 2 } ) ^ { \frac { \nu - 1 } { 2 } } [ a _ { 1 } ^ { \ : 2 } + a _ { 2 } ^ { \ : 2 } - 2 a _ { 1 } a _ { 2 } \cos { ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) } ] ^ { - \frac { \nu } { 2 } } ,
$$

where ${ \pmb \nu }$ Is an odd mtegei, must be consideied

Let $u _ { 1 } - u _ { 2 } + \tau _ { 2 } - r _ { 1 } = \psi$ It 1s known from the theoiy of Pouier selics when ${ \pmb a } _ { 1 }$ and $a _ { 2 }$ aie unequal, as is ssumed, that $[ ( { { \iota _ { 1 } } } ^ { 2 } + { { \iota _ { 2 } } } ^ { 2 } - 2 a _ { 1 } a _ { 2 } \cos \psi ] ^ { - \frac { \nu } { 2 } }$ can be developed into a series of cosines of multuplos of $\psi ,$ which is convei gent foi all values of $\psi$ That is,

$$
( a _ { 1 } a _ { 2 } ) ^ { \frac { \nu - 1 } { 2 } } [ a _ { 1 } { } ^ { 2 } + a _ { 2 } { } ^ { 2 } - 2 a _ { 1 } a _ { 2 } \cos \psi ] ^ { - \frac { \nu } { 2 } } = \frac { 1 } { 2 } \sum _ { i = - \infty } ^ { + \infty } B _ { \nu } { } ^ { ( i ) } \cos \imath \psi ,
$$

whero $B _ { \nu } ^ { ( \ell ) }  B _ { \nu } { } ^ { ( - \ell ) }$

Tho cocefficicnts $B , \Cup$ are of courge given by Fourier's integral

$$
B _ { \nu } ^ { ~ ( i ) } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \big ( a _ { 1 } a _ { 2 } \big ) ^ { \frac { \nu - 1 } { 2 } } \big [ a _ { 1 } { } ^ { 2 } - \big | - \ b _ { 2 } { } ^ { 2 } - 2 a _ { 1 } a _ { 2 } \cos \psi \big ] ^ { - \frac { \nu } { 2 } } \cos \upsilon \psi d \psi ,
$$

bul tho difficully of finding the integral makes it advisable in this particular pioblen to piocced other wise

Lcl $z = e ^ { \sqrt { - 1 } \psi }$ ,whclo e represents the Napierian base，Then

$$
2 \cos \psi = z + z ^ { - 1 } , ~ 2 \cos \imath \psi = z ^ { 4 } + z ^ { - 4 } .
$$

Suppose $a _ { 2 } > a _ { 1 }$ and $\operatorname* { l c t } { \frac { a _ { 1 } } { a _ { 2 } } } = \alpha _ { 2 }$ then （92） becomes

$$
\frac { \alpha ^ { \frac { \nu - 1 } { 2 } } } { 4 _ { 2 } } \left( 1 + \alpha ^ { 2 } - 2 \alpha \cos \psi \right) ^ { - \frac { \nu } { 2 } } = \frac { 1 } { 2 } \sum _ { i = - \omega } ^ { + \infty } B _ { \nu } ^ { ( i ) } \cos \psi
$$

Lol

$$
B _ { \nu } ^ { ( 4 ) } = \frac { \alpha ^ { \frac { \nu - 1 } { 2 } } } { a _ { 2 } } b _ { \nu } ^ { ( 4 ) }
$$

Smco tho absolute values of αz and αz-1 are less than umty for all rcal valucs of Φ, tho factors (1- az)- and (1 - αz-1)- can bo oxpanded by lho binomial theorom into convergent power go1cs in αz and αz-1. Tho coeffcient of x in the pioduct of these serieg is b,(，after which B( is obtained fiom (94)The gencral torm of thc product of the expansions is easily found to be

$$
\begin{array} { r l r }  \frac { 1 } { 2 } b _ { \nu } ^ { \nu } ^ { ( \nu ) } = \frac { \displaystyle \frac { \frac { \nu } { 2 } \left( \frac { \nu } { 2 } + 1 \right) \ \cdot \ \left( \frac { \nu } { 2 } + \imath - 1 \right) } { \imath ! } \alpha ^ { * } \left[ \mathrm { 1 } + \frac { \frac { \nu } { 2 } } { 1 } \frac { \frac { \nu } { 2 } + \imath } { \imath + 1 } \alpha ^ { 2 } \right. } & { } & \\  \left. \qquad + \frac { \displaystyle \frac { \frac { \nu } { 2 } \left( \frac { \nu } { 2 } + 1 \right) } { 1 } \cdot \frac { \left( \frac { \nu } { 2 } + \imath \right) \left( \frac { \nu } { 2 } + \imath + 1 \right) } { ( \nu + 1 ) ( \imath + 2 ) } \alpha ^ { * } + \mathrm { ~ \right] } , } & { } & \end{array}
$$

ae de-But thesc functions are mulliplied by the factois sin $( u _ { 1 } - \tau _ { 1 } )$ sin $( u _ { 2 } - \tau _ { 2 } )$ raised to different powers [cquation (87)] Thcse powcrs of sines aie to be reduced to sines and cosincs of multiples of the arguments,and the products formed with cos r(u1 - uz + rz - 7i), and the reduction again made to sincs and cosincs of multiples of arcs. The final trigonomotrical terms will have the foim cos $( \jmath _ { 1 } u _ { 1 } + \jmath _ { 2 } u _ { 2 } + h _ { 1 } \tau _ { 1 } + h _ { 2 } \tau _ { 2 } )$ ,whc1c $j _ { 1 } , \ j _ { 2 } , \ k _ { 1 } ,$ and $\displaystyle \mathbf { \mathit { k } _ { 2 } }$ aic intcgers. As $\mathfrak { a }$ consequence of (89) this cxpiession can be developed into

$$
\begin{array} { r } { \{ \begin{array} { l l } { \cos { ( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Delta _ { 1 } - j _ { 2 } \Delta _ { 2 } + k _ { 1 } r _ { 1 } + k _ { 2 } r _ { 2 } + j _ { 1 } w _ { 1 } + j _ { 2 } w } } \\ { = \cos { ( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Delta _ { 1 } - j _ { 2 } \Delta _ { 2 } + k _ { 1 } r _ { 1 } + k _ { 2 } r _ { 2 } ) } } \\ { \qquad \times \{ \cos { ( j _ { 1 } w _ { 1 } ) } \cos { ( j _ { 2 } w _ { 2 } ) } - \sin { ( j _ { 1 } w _ { 1 } ) } \sin { ( j _ { 2 } w _ { 2 } ) } \} } \\ { \qquad - \sin { ( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - j _ { 1 } \Delta _ { 1 } - j _ { 2 } \Delta _ { 2 } + k _ { 1 } r _ { 1 } + k _ { 2 } r _ { 2 } ) } } \\ { \qquad \times \{ \sin { ( j _ { 1 } w _ { 1 } ) } \cos { ( j _ { 2 } w _ { 2 } ) } + \cos { ( j _ { 1 } w _ { 1 } ) } \sin { ( j _ { 2 } w _ { 2 } ) } \} . } \\ { \qquad \{ l _ { 1 } = \sin { ( j _ { 1 } w _ { 1 } ) } + m _ { 1 } ( t _ { 0 } - T _ { 1 } ) + n _ { 1 } ( t - t _ { 0 } ) = n _ { 1 } t + \epsilon _ { 1 } ,  } \\ {  \{ l _ { 2 } = \delta _ { 3 } + \omega _ { 2 } + n _ { 2 } ( t _ { 0 } - T _ { 2 } ) + n _ { 2 } ( t - t _ { 0 } ) = n _ { 2 } t + \epsilon _ { 2 } ,  } \end{array}  } \end{array}
$$

Since

the first factors of the terms in the right mcmber of this equation are independent of e1 and ez. Cos (jiwi),etc.,are to be expanded into power series in Wi and wz by the usual mcthods Now W1=Vi- Mi, w2 = vz - M,and thcse quantities weio developcd into power series in e1 and ez [Art.10o,eq (64)] whose coefficients were Fourier series with multiples of the mcan anomaly as arguments. On substituting thcse series for w1 and wg in the expansions of the second factors of the terms of the right member of (96),and reducing the powers of sines and cosines of the mean anomaly to sines and cosines of multiples of the mean anomaly，and mulliplying by the factors

$$
( j _ { 1 } l _ { 1 } + j _ { 2 } l _ { 2 } - \gamma _ { 1 } \Delta _ { 1 } - j _ { 2 } \Delta _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } )
$$

and

$$
\sin { ( \jmath _ { 1 } l _ { 1 } + \jmath _ { 2 } l _ { 2 } - \jmath _ { 1 } \Omega _ { 1 } - \jmath _ { 2 } \Omega _ { 2 } + h _ { 1 } T _ { 1 } + h _ { 2 } \tau _ { 2 } ) } ,
$$

and again reducing to sines and cosineg of multiples of the aiguments, the expicsson (96) is devcloped as a powel Beries in e1 and ez whose cocffcients aie sciies in smcs and cosincs of sums of multiples of l, l2,&1, &2, T1,72,M, MBut M= l- π1, M=l-πz,thcicforc the aiguments will be l, l，&i，&2, T1, T2,T1, T2, whcic r1 and  acfunctions of &1, &z, l,and 2z defined by (83)

Whcn tho scvcral cxpansions and icductions which,have been desclbcd have all been made,Ri,2 will be developed in & powel solics in Ci，C2,and sin $\sin ^ { 2 } { \frac { I } { 2 } }$ ,thesf sincg and cosincs of multiples of l,l2,&1,&z,T1,T2,T1,n2, the coefficient of cach tiigonomoliic teim depending upon the iatio of tho major scmi-axcs If the signs of &1, &o2, π1, "2, T1, T2, e1, ez,and t are changcd the value of Rt,, as defined in (84), obviously is unchanged，thcrefoic thc expansion in question contains only cosincs of thc aigument. IIence

$$
\left\{ \begin{array} { l l } { R _ { 1 , \mathrm { ~ 2 ~ } } = \Sigma C \cos D , } \\ { \qquad D = \jmath _ { 1 } ( n _ { 1 } l + \epsilon _ { 1 } ) + j _ { 2 } ( n _ { 2 } ^ { \prime } l + \epsilon _ { 2 } ) - \jmath _ { 1 } ^ { \prime } \Omega _ { 1 } - \jmath _ { 2 } ^ { \prime } \Omega _ { 2 } } \\ { \qquad \qquad \quad + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } + k _ { 1 } \tau _ { 1 } + k _ { 2 } \tau _ { 2 } , } \\ { \qquad \quad C = f \left( a _ { 1 } , \ a _ { 2 } , \ e _ { 1 } , \ o _ { 2 } , \ \sin ^ { 2 } \frac { I } { 2 } \right) , } \end{array} \right.
$$

in whieh j，·,kea'tako allintegral valucs,positive,negativo,and zeio.the summation boing exlondcd ovcl all of these terms.

It is clear from lhe foicgoing that tho serics for R1,2 is very complcatcd and that much labor is requncd to expand it in any particular caso, Lovorrier has carried oul the liteial development 1 $e _ { 1 } , \ e _ { 3 } , \ \mathrm { s i n ^ { 2 } } \ \frac { \tilde { I } } { 2 } ,$ of all termg up to the sovonth ordor mclusivo in e1,ca，sm² and tho lenglh of tho work is such lhat ffty-three quarlo pages of the first volume of the Annales de l'Obseivatoire de Parrs are required n ordor to writo oul tho result.

225.Periodic Variations, It followg from cquations （72） and (97) that the rates of chango of lho elemonts of m are given by

$$
\{ \begin{array} { l l } { \frac { \mathrm { d } \Omega _ { \mathrm { c } } } { \mathrm { ~ d } t } = \frac { m _ { \mathrm { d } } } { \pi \mathrm { d } \mathrm { d } t ^ { 3 } \sqrt { \mathrm { 1 - ~ } \omega _ { \mathrm { c } } ^ { \mathrm { g } } \sin _ { \mathrm { d } } } } \sum \{ \frac { \partial C } { \mathrm { d } t }  } \\ & { \qquad \quad - [ k \frac { \partial T _ { \mathrm { c } } } { \partial \mathrm { d } t } + k \frac { \partial T _ { \mathrm { c } } } { \partial \mathrm { d } t } ] \mathcal { O } \mathrm { m } b \Bigg \} , } \\ { \frac { \mathrm { d } \Omega _ { \mathrm { c } } } { \mathrm { d } t } = \frac { - m _ { \mathrm { d } } } { \pi \mathrm { d } t ^ { 3 } \sqrt { \mathrm { 1 - ~ } \omega _ { \mathrm { c } } ^ { \mathrm { g } } \sin _ { \mathrm { d } } } } \sum \{ \mathrm { ~ d } ^ { \prime } - k \frac { \partial T _ { \mathrm { c } } } { \partial \mathrm { d } \mathrm { d } t } - k \frac { \partial \mathrm { d } \mathrm { d } \mathrm { d } t } { \partial \mathrm { d } t } \} } \\ & { \qquad \times \mathcal { O } \mathrm { m } D } \\ & { \qquad \quad + \frac { m _ { \mathrm { d } } \mathrm { d } \mathrm { d } \mathrm { m } \frac { 1 } { 2 } } { \pi \mathrm { d } t ^ { 3 } \sqrt { \mathrm { 1 - ~ } \omega _ { \mathrm { c } } ^ { \mathrm { g } } \sin _ { \mathrm { d } } } } \sum \{ \mathrm { ~ L } _ { \mathrm { f } } ^ { \prime } + 2 { \mathrm { i } } + k \frac { \partial T _ { \mathrm { c } } } { \partial \mathrm { T _ { \mathrm { c } } } } + k \frac { \partial T _ { \mathrm { c } } } { \partial \mathrm { d } t } \} } \\ & { \qquad \times \mathcal { O } \sin _ { \mathrm { d } } D , } \\  \frac { \mathrm { d } \Omega _ { \mathrm { c } } } { \mathrm { d } t } = \frac { m _ { \mathrm { d } } \sin _ { \mathrm { d } } ^ { \mathrm { ~ \frac { 1 } { 2 } } } } { \pi \mathrm { d } t ^ { 3 } \sqrt { \mathrm { i } } - \omega _ { \mathrm { c } } ^ { \mathrm { g } } } \sum \{ \frac { \partial C } { \partial t } \cos { \mathrm { D } } - [ k \frac { \partial T _ { \mathrm { c } } }  \partial t  \end{array}
$$$$
\begin{array} { r } { \widetilde { \mathcal { A } } ^ { - } \frac { m _ { \mathrm { A } } } { n _ { \mathrm { A } } a _ { 1 } ^ { 2 } } \sqrt { 1 - \frac { n _ { \mathrm { A } } } { n _ { \mathrm { A } } a _ { 1 } ^ { 2 } } } \frac { 1 } { n _ { \mathrm { A } } ^ { 2 } } \sum _ { i = 1 } ^ { n _ { \mathrm { A } } - n _ { \mathrm { A } } } \frac { 1 } { \widetilde { \omega } _ { \mathrm { A } } } \frac { \partial } { \partial a _ { 1 } } \int } \\ { + \frac { m _ { \mathrm { A } } } { n _ { \mathrm { A } } a _ { 1 } ^ { 2 } } \frac { 1 } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } } \sum _ { i = 1 } ^ { n _ { \mathrm { A } } } \frac { \partial } { \partial a _ { 1 } ^ { 2 } } \frac { 1 } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } + \widetilde { \omega } _ { \mathrm { A } } \widetilde { \omega } _ { \mathrm { A } } } } \\ { + \frac { m _ { \mathrm { A } } } { n _ { \mathrm { A } } a _ { 1 } ^ { 4 } } \frac { 1 } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } } \sum _ { i = 1 } ^ { n _ { \mathrm { A } } ^ { 2 } } \frac { 1 } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } } \sum _ { i \in \mathrm { A } } \frac { \partial \Gamma _ { i } } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } + \widetilde { \omega } _ { \mathrm { A } } \widetilde { \omega } _ { \mathrm { A } } } } \\  \frac { d \widetilde { \mathbf { e } } _ { 1 } } { d t } - \frac { m _ { \mathrm { A } } \sin \frac { 1 } { 2 } } { n _ { \mathrm { A } } a _ { 1 } ^ { 2 } } \sum _ { i = 1 } ^ { n _ { \mathrm { A } } } \sum _ { j = 1 } ^ { n _ { \mathrm { A } } } \frac { 1 } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } + \widetilde { \mathbf { e } } \frac { \partial \Gamma _ { i } } { \sqrt { 1 - \omega _ { \mathrm { A } } a _ { 1 } ^ { 2 } } } } \\  + \frac  m _ { \mathrm { A } } \end{array}
$$

$$
\{ \begin{array} { l l } { \frac { d \sigma _ { 3 } } { d t } = \frac { m _ { 1 } \hbar \langle \mathbf { t } \cdot \mathbf { u } \cdot \mathbf { u } ^ { \frac { 1 } { 2 } } \rangle } { \hbar \omega _ { 1 } ^ { 2 } - \hbar \omega _ { 1 } ^ { 2 } } \sum \{ \frac { \langle \mathbf { t } \rangle \langle \mathbf { t } \rangle } { \langle \mathbf { u } \cdot \mathbf { u } \rangle } - [ \mathbf { k } _ { 1 } \frac { \langle \mathbf { t } \rangle } { \langle \mathbf { t } \rangle } + \mathbf { b } \frac { \langle \mathbf { t } \rangle } { \langle \mathbf { t } \rangle } ]  } \\ { \frac { d \sigma _ { 3 } } { d t } = \frac { m _ { 1 } \hbar \langle \mathbf { t } \rangle } { \hbar \omega _ { 1 } ^ { 2 } - \hbar \omega _ { 1 } } \sum ( \mathbf { r } \otimes \mathbf { r } ) + \frac { m _ { 2 } \hbar \langle \mathbf { t } \rangle - \hbar \omega _ { 1 } } { \hbar \omega _ { 1 } ^ { 2 } + \hbar \omega _ { 1 } } \sum \frac { \partial \langle \mathbf { r } \rangle } { \partial \mathbf { d } _ { 0 } } \exp { \langle \mathbf { r } \rangle } , } \\ { \frac { d \sigma _ { 4 } } { d t } = - \frac { 2 m _ { 1 } \langle \mathbf { r } \rangle } { \hbar \omega _ { 1 } } \sum \gamma ( \mathbf { r } \otimes \mathbf { r } ) , } \\ { \frac { d \sigma _ { 4 } } { d t } = \hbar \alpha _ { 1 } \sqrt { - \omega _ { 1 } } \frac { 1 - \hbar \langle \mathbf { r } \rangle - \langle \mathbf { u } \cdot \mathbf { u } \rangle } { \hbar \omega _ { 1 } \omega _ { 2 } } \sum _ { \gamma \leq \gamma \leq \gamma \leq \gamma \leq \gamma } } \\ { \quad } & { + \frac { m _ { 1 } \hbar \langle \mathbf { r } \rangle - \langle \mathbf { r } \rangle } { \hbar \omega _ { 1 } \omega _ { 2 } \hbar \omega _ { 1 } } \sum \{ \hbar \^ { 1 } + \frac { \partial \langle \mathbf { r } \rangle } { \partial \mathbf { r } \omega _ { 1 } } + \mathbf { b } \frac { \partial \langle \mathbf { r } \rangle } { \partial \mathbf { r } \omega _ { 1 } } \} \zeta \mathbf { m } \mathbf { D } , } \\  \frac { d \mathbf { u } \cdot \mathbf { u } \cdot \mathbf { u } \cdot \mathbf { u } \cdot \mathbf { u } ^ { \frac { 1 } { 2 } } }  \hbar \omega _ { 1 } ^   \end{array}
$$

The perturbations of the elements of the orbit of mi of the first order with respect to the mass mz are the integrals of thesc equations regarding the elements as constants in the Iight mombers. Similar terms must be added for each disturbing planot.

There are terms im Rt,² of thiee classes (a) those in which Jim1+J2nz is distinct from zero and not small；(b) those in which jm+jnz is very small, but distinct from zero,and (c) those in which jmi + Jn equals zero Denote the fact that Ri,& contains these three sorts of terms by writing

R,²= ∑Cocos Do+ ΣC1cOs Di+ ΣC cos D2, whoro tho thicc suims in the iight member include these three clasges of torms lcspectively Ience the pertuibations of the clements of mi by mz of thc fnst ordci and of the fist class are

$$
\begin{array} { r }  \operatorname* { m a x } _  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta  \theta \theta  \theta  \theta  \theta \theta  \theta  \theta \theta  \theta \theta  \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \theta \theta  \ \end{array}
$$$$
\begin{array} { r l } { \times \sum \{ \bar { x } ^ { \prime } - \bar { k } _ { 1 } \frac { \partial \bar { x } _ { 1 } } { \partial \bar { \alpha } _ { 1 } } - \bar { k } _ { 2 } \frac { \partial \bar { x } _ { 2 } } { \partial \bar { \alpha } _ { 1 } } \frac { C _ { 4 } \cos D _ { 0 } } { \bar { y } _ { 1 } \bar { x } _ { 1 } + \bar { y } _ { 2 } \bar { x } _ { 2 } }  } & { } \\  - \frac { m \sin \frac { \bar { x } _ { 2 } } { 2 } } { \bar { x } _ { 1 } \omega _ { 1 } ^ { 4 - \frac { 3 } { \sqrt { 1 - \omega ^ { 2 } } } } \sum \{ \bar { k } _ { 1 } ^ { \omega } + \bar { y } _ { 1 } + \bar { k } _ { 1 } \frac { \partial \bar { x } _ { 1 } } { \partial \bar { x } _ { 1 } } + \bar { k } _ { 2 } \frac { \partial \bar { x } _ { 2 } } { \partial \bar { x } _ { 1 } }  \frac { C _ { 4 } \cos D _ { 0 } } { \bar { y } _ { 1 } \bar { x } _ { 1 } ( \omega _ { 1 } + \bar { y } _ { 2 } ) } , } & { } \\ {  \frac { m \sin \frac { \bar { x } _ { 1 } } { \omega _ { 1 } } } { \sqrt { 1 + \omega ^ { 2 } } } - ( \pi _ { * } \frac { \partial \bar { x } _ { 1 } } { \omega _ { 1 } } ) _ { \bar { \alpha } _ { 1 } } = \frac { m _ { 2 } \sin \frac { \bar { x } _ { 2 } } { \sqrt { 1 - \omega ^ { 2 } } } } { \bar { x } _ { 1 } \omega _ { 1 } ^ { 3 - \frac { 3 } { \sqrt { 1 - \omega ^ { 2 } } } } } \sum \{ \frac { \bar { \alpha } ( \bar { Q } _ { g } } { \bar { x } _ { 1 } } , \frac { \sin \bar { y } _ { 1 } } { \sqrt { 1 + \frac { 2 \nu \bar { x } _ { 2 } } } } + \bar { y } _ { 2 }   } & { } \\  +   [ \frac { \bar { k } _ { 1 } \bar { \alpha } _ { 1 } } { \bar { \alpha } _ { 1 } } + \bar { k } _ { 2 } \frac { \partial \bar { x } _ { 1 } } { \partial \bar { x } _ { 1 } } ] \frac  \end{array}
$$

$$
\begin{array} { r l } & { \quad - \quad - \eta _ { k } \alpha _ { k } ^ { \beta } = \frac { 1 } { \beta \alpha _ { k } ^ { 3 } } \sum _ { \beta = 1 } ^ { \nu _ { k } } \frac { 1 } { \beta \alpha _ { k } ^ { 3 } + \beta \eta _ { k } ^ { 3 } } + \frac { 3 \eta _ { k } \beta _ { k } } { 3 \eta _ { k } ^ { 3 } } , } \\ & { \quad \quad \quad - ( \alpha _ { k } ^ { 1 , 3 } \alpha _ { k } ^ { 3 } ) \zeta _ { \alpha } = - \eta _ { k } \zeta _ { \alpha } ^ { 1 , 3 } \sum _ { \beta = 1 } ^ { \nu _ { k } } \frac { \zeta _ { \alpha } \alpha _ { k } \Delta \rho _ { k } } { 3 \eta _ { k } + \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } } \\ & { \quad \quad - ( \alpha _ { k } ^ { 1 , 3 } \alpha _ { k } ^ { 3 } ) \zeta _ { \alpha } = - \eta _ { k } \zeta _ { \alpha } ^ { 1 , 3 } \sum _ { \beta = 1 } ^ { \nu _ { k } } \frac { \zeta _ { \alpha } \alpha _ { k } \Delta \rho _ { k } } { 3 \eta _ { k } + \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } \sum _ { \beta = 1 } ^ { \nu _ { k } } \exp ( - \beta \zeta _ { \alpha } \zeta _ { \alpha } \zeta _ { \alpha } \zeta _ { \alpha } ) } \\ &  \quad \quad \quad - \frac { 2 \eta _ { k } \alpha _ { k } ^ { 3 } - \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } { 3 \eta _ { k } + \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } \sum _ { \alpha _ { k } ^ { 3 } \ge 1 } ^ { \nu _ { k } } \sum _ { \beta = 1 } ^ { \nu _ { k } } \frac { \zeta _ { \alpha } \alpha _ { k } \Delta \rho _ { k } } { 3 \eta _ { k } + \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } \sum _ { \beta = 1 } ^ { \nu _ { k } } \frac { \zeta _ { \alpha } \alpha _ { k } \Delta \rho _ { k } } { 3 \eta _ { k } + \sqrt { \pi _ { k } \alpha _ { k } ^ { 3 } } } \\ &  \quad \quad \quad ( \alpha _ { k } \beta \alpha _ { k } ^ { 3 } ) - ( \alpha _ { k } ^ { 1 , 3 } \alpha _ { k } ^  \end{array}
$$

Thesc terms aie purely periodic with periods n+gn,and constitute the perodic vaiiations Every element 1s subject to them， dlepending upon an infinity of such terms whose periods are diffeicnt The laigel Jm+Jng is, the shoiter is tho period of the term and in geneial the smaller 1s its coefficient

The mcthod of repiesenting the motion of the planets by a selies of periodic terms is somewhat analogous to the epicycloid theory of Ptolemy,for each term alone is equivalent to the adding of a small clcular motion lo that pieviously cxisting， This theoly 18 moie complex than thal of Ptolemy in that it adds cpicycloid upon epicycloid without limit,it is simpler than that of Ptolemy in that it flowg fiom one simple principle, the law of giavitation.

226.Long Period Variations. The letters J1 and Ja represont all positive and negalive integeis and zeroThereforo,unless ni and nz are mcommensurable Ji and g& exist such that Jimi + 7n= O,where jiand J& aic not zero But then D is a constant and the integial is not foimed this wayIIowever,whethcr ni and nz are incommensurable or not, such a pair of numbers can be found that Jmi + Jn2 1s veiy small The corresponding term will be large unless its C js very smallIt is shown in a complete discussion of the development of $\mathcal { R } _ { 1 , \ 2 }$ that the order of $\pmb { C }$ m $\pmb { \mathcal { C } } _ { 1 } , \ \pmb { \mathcal { C } } _ { 2 } ,$ $\sin ^ { 2 } \frac { l } { 2 }$ 1s at the least equal to the numerical value of Ji +Jz (see Tisserand's Mec. Cel.,vol I,p. 308) Since ni and nz are both positive, one of the numbers Ji, Ja must be posilive and the other negative n order that the sum Jimi + Jzna shall be small. Tho more nearly equal Ji and Jz are numerically the smaller the numerical value of Ji +jz is,and consequently,the larger C will be. When the mean motions of the two planets are such that they are nearly commensurable with the ratio of ni to nz expressible in small ntegers, then large terms m the perturbations will arise from the presence of these small divisorsThe period of such a term 1s $\frac { 2 \pi } { \mathcal { 1 } ^ { n _ { 1 } } + \dot { \mathcal { j } } _ { 2 } \mathcal { n } _ { 2 } }$ ,whchiBverygreatwenceeein long perrod. These terms are given by equations of the same form as (99),but with the restriction that jimi+ Janz shall be very small

Geometrically considered, the condition that the periods shall be nearly commensurable with the ratio expressible in small integers means that the points of conjunction oocur at nearly tho same part of tho olbits with only a few other conjunctions intervening. The extieme case is that in which there aie no conjunctions intei vening,1.e,when $\pmb { \jmath _ { 1 } }$ and $\pmb { \mathscr { s } } _ { \mathbf { 2 } }$ differ in numerical value by umty

The mcan molions of Jupitei and Saturn aie nearly in the ratio of fivo to two Consequently ${ \mathfrak { J } } _ { 1 } \simeq { \mathfrak { L } } _ { 1 }$ $\ j _ { 2 } = - 5$ gives a long poriod loim,and thc oidcl of the coefficient $\mathtt { \mathtt { C } }$ 1s the absolute valuc of ${ \mathfrak { 2 } } - { \mathfrak { 5 } }$ 013The causc of the long period imequality of Jupiter and Satuin was discovered by Laplace in 1784 in computing the peituibations of thee thid order in ${ \pmb \theta } _ { 1 }$ and $\pmb { \ell _ { 2 } }$ The longth of thc poliod in thc case of these two planets is about 850 years

227.Secular Variattons. The expression $\pmb { D }$ 1sindependent of tho time for all of those teims in which $\ j _ { 1 } = \ j _ { 2 } = 0$ The partial doivatives of $\mathcal { D }$ with respect to the elements are also mdopondont of the lime,hence, on taking these terms of (98) and inlcgrating,it is found that

$$
\begin{array} { r }  \{ \begin{array} { l l } { \{ \Omega _ { \mathrm { i } } ^ { \mathrm { n } , \mathrm { n } , \mathrm { i } } \} = \frac { m _ { \mathrm { m } } } { \Omega _ { \mathrm { i } } \Omega _ { \mathrm { i } } ^ { \mathrm { s } , \mathrm { i } } \sin _ { \mathrm { i } } \Omega _ { \mathrm { i } } } \sum _ { \{ \vphantom { \frac { \partial } { \frac { \partial } { \partial } } \Omega _ { \mathrm { i } } ^ { \mathrm { n } } \} } = \frac { m _ { \mathrm { m } } } { \Omega _ { \mathrm { i } } } } \\ { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { \{ \mathrm {  ~ \frac { \partial } { \partial } ~ \Lambda _ { \mathrm { i } } ^ { \mathrm { a } , \mathrm { n } } \frac { \partial \Sigma _ { \mathrm { i } } ^ { \mathrm { n } } } { \partial \mathrm { i } } \mathrm { i } \Lambda _ { \mathrm { i } } ^ { \mathrm { a } , \mathrm { i } } \Lambda _ { \mathrm { i } } ^ { \mathrm { a } , \mathrm { i } } } \mathrm { \Lambda _ { \mathrm { i } } ^ { \mathrm { a } , \mathrm { i } } \Sigma _ { \mathrm { i } } ^ { \mathrm { n } } \Sigma _ { \mathrm { i } } ^ { \mathrm { n } } } \{ \vphantom { \frac { \partial } { \partial } \Omega _ { \mathrm { i } } ^ { \mathrm { n } } \biggr \} } ( t - \mathrm { i } \phi _ { \mathrm { i } } ) , } \\  \{ \mathrm {  ~ \frac { \partial } { \partial } ~ \Lambda _ { \mathrm { i } } ^ { \mathrm { a } , \mathrm { n } } \biggr \} } \mathrm { \Lambda _ { \mathrm { - } \mathrm { \Sigma } } } \mathrm { \Sigma } _ { \mathrm { - } \mathrm { \Sigma } } ^ { \mathrm { m } , \mathrm { i } } \mathrm { \Sigma } _ { \mathrm { i } } ^ { \mathrm { m } , \mathrm { i } } \mathrm { \Sigma } _ { \mathrm { i } } ^ { \mathrm { n } } \mathrm { \Sigma } _ { \mathrm { i } } ^ { \mathrm { n } } \{ \begin{array} { l l }  \mathrm { \Sigma } _ { \mathrm { - } \mathrm { \Sigma } } ^ { \mathrm { a } } \mathrm { \Sigma } _  \mathrm { - } \mathrm { \Sigma } \mathrm { + } \mathrm { i } \Lambda _ { \mathrm { i } } ^  \mathrm  \end{array} \end{array} \end{array}
$$

$$
\begin{array} { r }  \{ \begin{array} { c } { m _ { 1 } \alpha _ { 1 } \tan \frac { \hat { \pi } _ { 1 } } { 2 } , } \\ { + \frac { m _ { 1 } \tan \frac { \hat { \pi } _ { 1 } } { 2 } } { \gamma _ { 1 } ( \alpha _ { 1 } ^ { 4 } \sin ^ { 4 } \pi ) 1 - \epsilon _ { 1 } ! } \sum \{ k _ { 1 } ^ { \prime } + k _ { 1 } \frac { \partial \tau _ { 1 } } { \partial \tau _ { 1 } }  } \\ {  + k _ { 3 } \frac { \partial \tau _ { 1 } } { \partial \tau _ { 1 } } \} C _ { 1 } \sin D _ { 1 } \cdot ( \ell - k _ { 9 } ) , } \\ {  \frac { m _ { 3 } \tan \frac { \hat { \pi } _ { 3 } } { \partial \tau _ { 1 } } } { \gamma _ { 1 } ( \alpha _ { 1 } ^ { 2 } \sin ^ { 4 } \pi ) 1 - \sqrt { \pi } \sin ^ { 2 } } \sum \{ \frac { \partial C _ { 3 } } { \partial \tau _ { 1 } } \cos D _ { 2 }  } \\ {  \frac { \partial \tau _ { 1 } ( \lambda _ { 1 } ^ { ( 1 ) } + k _ { 3 } \frac { \partial \tau _ { 1 } } { \partial \tau _ { 1 } } ) \big ( \alpha _ { 1 } \sin D _ { 2 } \} ( \ell - k _ { 9 } ) } \\ { + \frac { m _ { 3 } \sqrt { 1 } - \cos ^ { 4 } \pi \big ) } { \gamma _ { 1 } \alpha _ { 1 } \alpha _ { 1 } ^ { 3 } \epsilon _ { 1 } } \sum \frac { \partial C _ { 3 } } { \partial \tau _ { 1 } } \cos D _ { 2 } \cdot ( \ell - k _ { 9 } ) , } \end{array}  } \end{array}
$$

$$
\begin{array} { r }  \{ \begin{array} { l l } { \{ a _ { 1 } ^ { ( 1 , n ) , 0 } = 0 , \} } \\ { \{ b _ { 2 } ^ { ( 1 , n ) , 1 } = \frac { \eta _ { 0 } ^ { ( 1 , 1 ) } - ( \alpha _ { 0 } ^ { ( 1 , n ) } ) } { \sin { \theta _ { 1 } } + 1 } \sum _ { i = 1 } ^ { n } \frac { ( b _ { 1 } ^ { ( 1 , i ) } + b _ { 1 } ^ { ( 1 , i ) } ) } { \sin { \theta _ { 1 } } } } \\ { \qquad \quad + b _ { 2 } ^ { ( 1 , n ) } \sum _ { i = 1 } ^ { n } \frac { ( b _ { 2 } ^ { ( 1 , i ) } + b _ { 2 } ^ { ( 1 , i ) } ) } { \sin { \theta _ { 1 } } } ( c - b _ { 2 } ^ { ( 1 , i ) } ) , } \\ { \qquad \quad + \frac { \eta _ { 0 } ^ { ( 1 , i ) } - ( b _ { 2 } ^ { ( 1 , i ) } + b _ { 1 } ^ { ( 1 , i ) } ) } { \sin { \theta _ { 1 } } + 1 } \sum _ { i = 1 } ^ { n } \frac { ( b _ { 2 } ^ { ( 1 , i ) } + b _ { 2 } ^ { ( 1 , i ) } ) } { \sin { \theta _ { 1 } } } } \\ { \qquad \quad - [ b _ { 2 } ^ { ( 1 , i ) } \frac { 1 } { \sin { \theta _ { 1 } } } + b _ { 2 } ^ { ( 1 , i ) } ] ( c _ { 4 } \sin { D _ { h } } ) } \\ { \qquad \quad + m _ { \mathrm { e } } \sqrt { 1 - \frac { \alpha _ { 0 } ^ { ( 1 , i ) } } { \sin { \theta _ { 1 } } } } \frac { 1 - \sqrt { 1 - \alpha _ { 0 } ^ { ( 1 , i ) } } } { \sin { \theta _ { 1 } } } ( c _ { 4 } \sin { D _ { h } } ) } \\ { \qquad \quad \times \{ \frac { \alpha _ { 0 } ^ { ( 1 , i ) } - ( b _ { 2 } ^ { ( 1 , i ) } + b _ { 1 } ^ { ( 1 , i ) } ) } { \sin { \theta _ { 1 } } } \frac { 1 - \sqrt { 1 - \alpha _ { 0 } ^ { ( 1 , i ) } } } { \sin { \theta _ { 1 } } } ( c - b _ { 2 } ^ { ( 1 , i ) } )  } \\  \qquad \quad  - \frac  \sqrt  1 - \alpha _  0 \end{array} \end{array}
$$

It follows that there are no secular terms of this type of the firsl oider with respect to the masses in the pertuibations of $^ { a }$ This constitutes the fiist theoiem on the stability of the solar system. It was piovcd up to the second powcrs of thc cccentiicitics by Laplace in $^ { 1 7 7 3 , * }$ when he was but twenty-foul yeais of age, in a memoir upon the mutual peiturbations of Jupilei and Saturn, it was shown by Lagrange in 1776 that it is true for all powcrs of the eccentricities $\dagger$ It was proved by Po1sson in 1809 that thci0 are no seculai teims in $\pmb { a }$ in the pel turbations of the socond oider with respect to the masses, but lhat lhere aic teims of the type $\pmb { \mathscr { t } }$ cos $\mathcal { D }$ ，where $\mathcal { D }$ contains the time.t·Teims of this type are commonly called Posson terms

All of the elements except $\pmb { a }$ have secular toims. It appears to have been supposed that the secular terms,which apparcntly cause the elements to change without lmit,alone prcvcnt the usc of equations (72) fol computing the peilurbations for any timc howevel gieat Many methods of computing perturbations have been devised in ordei to avoid the appearancc of socular terms; yet it is clear that, whether or not terms propollional to the time appear,the method is staictly vald fol only those values of the timo for which the serics (20) of Art 207 aie convergent

Secular terns inay entcl in anothel way, usually not considered. If Jn+gn=O with ji≠0,Ja≠O,D1g independent of the time and thc coiiesponding teims aie seculai In this case D is nol mdepondent of $\pmb { \epsilon _ { 1 } }$ and thcie will be secula1 terms n the perlurbalions of a. As has becn iemaiked, this condition will always be fulhilled by an mfinity of valucs of $\pmb { \mathscr { I } } \mathbf { 1 }$ and $\pmb { \jmath _ { 2 } }$ if $\pmb { n _ { 1 } }$ and $\pmb { n _ { 2 } }$ are not mcommeusurable But it is impossible to determime from observalions whcthcr ol nol ${ \boldsymbol { \mathscr { n } } } _ { 1 }$ and $\pmb { n _ { 2 } }$ a1o incommensurable, for there is always $\mathfrak { a }$ lnit to thc accuiacy with which observations can be mado,and within this limil there cxist infinitely many commensunablo and incommensuiable numbeisThere is as much roason, thcrcforo, lo say that secular teims im $\pmb { a }$ of this type exist as that thoy do not. Howcver， they are of no practical importance becauso the iatio of $\pmb { n _ { 1 } }$ to $\boldsymbol { n } _ { 2 }$ cannot be expressed in small inlogors,and the cooflioients of these teims, if they do exist,are 8o small that lhcy arc nol sensible for such values of the time as are o dinarily used

228.Terms of the Second Order with Respect to the Masses. Tho toums of tho second odel aic dcfined by equations (29), Arl.21o. Tho right mcmbeis of these equations are the products of tho partial derivatives,with respect to the elements,of the iight momborg whioh occur in thc terms of the first order,and the perturbationg of tho fnst order of the corresponding elements Thus, lhe second order peturbations of the node are determined by the oquations

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d \Omega _ { 1 } ( 0 , 2 ) } { d l } = \frac { m _ { 2 } } { \displaystyle { n _ { 1 } a _ { 1 } ^ { 2 } \sqrt { 1 - \varrho _ { 1 } ^ { 2 } } \mathrm { 8 l n } \mathrm { \Omega } _ { 1 } } } \sum _ { i _ { 1 } } \frac { \partial ^ { 2 } R _ { 1 , 2 } } { \partial i _ { 1 } \partial s _ { 1 } } \mathrm { \Omega } _ { s _ { 1 } } ^ { \mathrm { i } ( 0 , 1 ) } , } \\ { \displaystyle \frac { d \Omega _ { 3 } ( 1 , 1 ) } { d l } = \frac { m _ { 2 } } { \displaystyle { n _ { 1 } a _ { 1 } ^ { 2 } \sqrt { 1 - \varrho _ { 1 } ^ { 2 } } \mathrm { 8 l n } \mathrm { \Omega } _ { 1 } } } \sum _ { i _ { 2 } } \frac { \partial ^ { 2 } R _ { 1 , 2 } } { \partial i _ { 1 } \partial s _ { 2 } } \mathrm { \Omega } _ { 2 } \mathrm { \Omega } _ { 3 } ^ { \mathrm { i } ( 1 , 0 ) } , } \end{array} \right.
$$

whcre s1 and sg ropresont lho clemcnts of the orbits of m1 and mz rcspeclivcly. Tho partial derivativo $\frac { \partial ^ { 2 } R _ { 1 , ~ 2 } } { \partial \iota _ { 1 } \partial \delta _ { 1 } }$ 1s $\mathfrak { a }$ sum of periodic and conslant lerms； st(o.) and sz(1.o) aie sums of periodic terms and torms coniaining thc time to the first degree as a factor The produets $\frac { \partial ^ { 2 } R _ { 1 , ~ 2 } } { \partial \iota _ { 1 } \partial \vartheta _ { 1 } } \vartheta _ { 1 } ^ { ( 0 , 1 ) }$ and $\frac { \partial ^ { 2 } R _ { 1 , ~ 2 } } { \partial \ i \partial \delta _ { 2 } } \ \delta _ { 2 } ^ { ~ ( 1 , ~ 0 ) }$ thcrefore ontan ters of four types $( a ) _ { \mathrm { \ c o s } } ^ { \mathsf { s m } } \mathscr { D } ,$ whe1e $\mathcal { D }$ contains the lime； (b) $t _ { \cos } ^ { \sin } \mathcal { D } _ { \mathrm { : } }$ ${ \bf \Phi } ( c ) \mathsf { \Pi } _ { \mathsf { c o s } } ^ { \mathsf { s u n } } D _ { \mathsf { 2 } } ,$ where $\scriptstyle { D _ { 2 } }$ 1B ndependent of the time,and $( d ) \textit { t } _ { \mathrm { c o s } } ^ { \mathrm { s i n } } D _ { 2 }$ The integials of these foui types aro iespectivcly,

$$
\begin{array} { r l r l } { { ) } } & { \frac { - \displaystyle \cos ^ { } D } { \jmath _ { 1 } n _ { 1 } + \jmath _ { 2 } n _ { 2 } } , \quad } & { ( b ) } & { \frac { - \displaystyle \cos ^ { } D } { \jmath _ { 1 } n _ { 1 } + \jmath _ { 2 } n _ { 2 } } + \frac { \displaystyle \cos ^ { } D } { ( \jmath _ { 1 } n _ { 1 } + \jmath _ { 2 } n _ { 2 } ) ^ { 2 } } ; } \\ { { ) } } & { \boldsymbol { t } _ { \mathrm { c o s } } ^ { \mathrm { s u n } } D _ { 2 } , \quad } & { ( d ) } & { \frac { \boldsymbol { t } ^ { 2 } \displaystyle \sin ^ { } D _ { 2 } } { \sum \mathrm { c o s } } D _ { 2 } } \end{array}
$$

Therefore, the perturbations of the second order with respect to the masses havc purely periodic terms， Poisson terms.or terms in which the trigonometic teims are multiplicd by the time; secular terms wheie the timo occuis lo the first degiee,and secular terms where the time ocouis to the socond degiee This is truo for all of the elements except the major semi-axis, in the caso of which the coofficients of the teims of the third and fouith types ale zero,as Poisson firsl proved.

In the terms of the third order with respect lo the magses thero are secular terms in the perturbations of all tho elements except ${ \pmb { a } } _ { 1 } ,$ which are proportional to the third powor of the time,and so on.

229. Lagrange's Treatment of the Secular Variations. The prescnce of the secular terms in the expressions for the clements seems to indicate that, if it is assumed that the series reprcsent the elements for all values of the time, then the elements change without limit with the time. But this conclusion is by no means necessarily true. For example, consider the function

$$
\sin { \left( c m t \right) } = c m t - \frac { c ^ { 3 } m ^ { 3 } t ^ { 3 } } { 3 ! } + \cdot ,
$$

where c ig & constant and m & very small factor whiqh may take the place of $\mathbf { \widetilde { a } }$ massThe series in the right member converges for all values of t. This function is never greater than unity for any value of the time, yet if its expansion in powers of m were given, and if the first few terms were considered without the law of the coefficients being known,it might seem that the series represents a function which increascs indefinitely in numerical value with the time.

On following out the idea that the seoular terms may be expansions of functions which ale always finite, Lagiange has shown (scc Collected Wmks,vols v and v1),undei certain assumptions which have not bcen logically juglified,that the secular teims aiQ m ieality the cpansions of petiodic teims of very long period Thcse teims difer fiom the long peiiod vaiiations (Art 226) in that they come fiom the small uncompensatcd paits of the peiiodic variations, mstead of dncctly from special conditions of conjunctionsAs a iule these icims aie vcry sinall,and then periods aie much longei than thosc of the sensible long peiiod teimsIt will not be possiblo lo give here moie than a veiy geneial idca of the method of Lagiange

The fist slep n thc method of Lagiange is a transfoimation of vaiiables by tho equaliong

$$
\left\{ \begin{array} { l l } { h _ { \iota } = e _ { \iota } \sin \pi _ { \acute { \iota } } , } \\ { l _ { \iota } = e _ { \iota } \cos \pi _ { \acute { \iota } } , } \end{array} \right.
$$

and

$$
\begin{array} { r } { \int \eta _ { \eta } = \tan \iota _ { \eta } \sin \vartheta \dot { \iota } ; } \\ { \quad \ q _ { \eta } = \tan \iota _ { j } \cos \vartheta \dot { \iota } ; } \end{array}
$$

whero ei,π, ctc.,are thc cloments of tho orbit of m,,and l is a now vaiiablo not to bo confugcd with tho mean longiude. These tansfoimations aro to bo mado simultancously m tho clements of thc oibits of all of tho planots. The elemonls a, and e, 1cman without lransformation. On omitting lho subscripts,il is found from (103) and(104) that

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { d h } { d t } = + e \cos \pi \frac { d \pi } { d t } + \sin \pi \frac { d \theta } { d t } , } \\ { \displaystyle \frac { d \theta } { d t } = - e \sin \pi \frac { d \pi } { d t } + \cos \pi \frac { d \theta } { d t } , } \\ { \displaystyle \frac { d R } { d \theta } = \frac { \partial L } { \partial t } \frac { \partial h } { \partial \theta } + \frac { \partial R } { \partial t } \frac { \partial L } { \partial \theta } = \sin \pi \frac { \partial R } { \partial h } + \cos \pi \frac { \partial L } { \partial t } , } \\ { \displaystyle \frac { \partial L } { \partial \pi } = \frac { \partial L } { \partial t } \frac { \partial h } { \partial \pi } + \frac { \partial R } { \partial t } \frac { \partial L } { \partial \pi } = \cos \pi \frac { \partial R } { \partial h } - e \sin \pi \frac { \partial R } { \partial t } , } \\ { \displaystyle \frac { d p } { d t } = + \tan \textrm { s t o n s } \frac { d \otimes } { d t } + \sec ^ { \mathrm { 3 } } \downarrow \sin \bigotimes \frac { d s } { d t } , } \\ { \displaystyle \frac { d \theta } { d t } = - \tan i \textrm { s t a n } \frac { d \Delta } { d t } - \sec ^ { \mathrm { 3 } } \downarrow \cos \bigotimes \frac { d \Delta } { d t } , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \displaystyle \frac { \partial R } { \partial \Omega } = \frac { \partial R } { \partial \boldsymbol { p } } \frac { \partial \boldsymbol { p } } { \partial \Delta } + \frac { \partial R } { \partial q } \frac { \partial q } { \partial \Delta } } \\ { \displaystyle \qquad = \tan \iota \cos \Delta \frac { \partial R } { \partial \boldsymbol { p } } - \tan \iota \sin \Delta \frac { \partial R } { \partial q } , } \\ { \displaystyle \frac { \partial R } { \partial \boldsymbol { s } } = \frac { \partial R } { \partial \boldsymbol { p } } \frac { \partial \boldsymbol { p } } { \partial \boldsymbol { \lambda } } + \frac { \partial R } { \partial q } \frac { \partial q } { \partial \boldsymbol { i } } } \\ { \displaystyle \qquad = 8 0 ^ { 2 } \iota \sin \Delta \frac { \partial R } { \partial \boldsymbol { p } } + \sec ^ { 2 } \iota \cos \Delta \frac { \partial R } { \partial q } . } \end{array} \right.
$$

Then il follows from (72) that

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \Delta a = \sin \theta , } \\ { \frac { \sin \theta } { \sin \theta } , } \\ { \frac { \sin \theta } { \sin \theta } , } \\ { - \frac { \sin \theta } { \sin \theta } , } \\ { \frac { \sin \theta } { \sin \theta } , } \end{array} \right. \frac { \sin \theta } { \sin \theta } } \\ { \left\{ \begin{array} { l l } { \frac { \sin \theta } { \sin \theta } , } \\ { \frac { \sin \theta } { \sin \theta } , } \\ { \frac { \sin \theta } { \sin \theta } , } \end{array} \right. } \end{array}
$$$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \qquad + \frac { 1 } { n \omega ^ { 6 } } \Pi - \hbar ^ { 6 } - \frac { \hbar \omega ^ { 4 } } { 3 \omega ^ { 6 } } , } \\ { \frac { d } { d \omega } = \frac { - m _ { 1 } \hbar \omega ^ { 4 } - \hbar ^ { 6 } - \beta \Delta \theta } { 3 \omega ^ { 6 } } } \\ { - \frac { \hbar \omega ^ { 4 } } { 3 \omega ^ { 6 } } - \frac { \hbar \omega ^ { 4 } } { 3 \omega ^ { 6 } } } \\ { \qquad - \frac { \hbar \omega ^ { 4 } - \hbar ^ { 6 } - \Gamma } { 3 \omega ^ { 6 } } - \frac { \hbar \omega } { 1 + \sqrt { 3 - ( \Gamma - \Gamma ) ^ { 6 } } } \frac { d \Delta \theta } { d \omega } } \\ { \qquad - \frac { \hbar \omega \Gamma \omega } { 3 \omega ^ { 6 } } } \\ { \frac { d \theta } { d \omega } = \frac { \hbar \omega } { 3 \omega ^ { 6 } - \hbar \omega ^ { 3 } } \frac { \hbar \omega } { 3 \omega ^ { 6 } } , } \\ { \frac { d \theta } { d \omega } = \frac { \hbar \omega } { 3 \omega ^ { 6 } - \hbar \omega ^ { 4 } - \Gamma \omega \omega ^ { 5 } } \frac { \hbar \omega } { d \omega } } \\ { - \frac { \hbar \omega } { 2 \omega ^ { 6 } + \Gamma - \Gamma \omega \omega ^ { 6 } } \frac { \hbar \omega } { 3 \omega ^ { 6 } + \omega ^ { 6 } } \frac { \hbar \omega } { 3 \omega ^ { 6 } } + \frac { \hbar \omega } { 3 \omega ^ { 6 } } \Bigg [ \frac { d \Delta \theta } { d \omega } + \frac { \partial \theta } { 3 \omega } \Bigg ] , } \\ { \frac { d \lambda } { d \omega } = \frac { - m _ { 1 } \hbar \omega } { 3 \omega ^ { 6 } + \hbar \omega ^ { 6 } - \Gamma \omega \omega ^ { 6 } + \omega } \frac { \hbar \omega } { 3 \omega ^ { 6 } } } \\ { \frac { d \lambda } { d \omega } = \frac { - \hbar \omega } { 3 \omega ^ { 6 } + \Gamma - \Gamma \omega \omega \Gamma \omega } \frac { \hbar \omega } { d \omega } } \end{array} \right. } \end{array}
$$

On developing the right membeis of thcse equations and neglecting all terms of degice higher than the fnst\*inh,l,p,and q,thcse

\*The termg of ordcr higher than the frat are neglccted throughout in $\clubsuit$ later stop in tho method

equntions reduce to

$$
\begin{array} { r } { \left\{ \begin{array} { l } { \frac { d \hat { h } } { d t } = + \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial \hat { R } } { \partial l } , } \\ { \frac { d \hat { l } } { d t } = - \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial \hat { R } } { \partial \hat { h } } , } \\ { \frac { d p } { d \hat { l } } = + \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial \hat { R } } { \partial q } , } \\ { \frac { d q } { d \hat { l } } = - \frac { m _ { 2 } } { n a ^ { 2 } } \frac { \partial \hat { R } } { \partial p } . } \end{array} \right. } \end{array}
$$

Tho lerms which involve the denvativc of $\scriptstyle { \mathcal { R } }$ with respect to $\epsilon , \lambda _ { 1 }$ amd $\pmb { \pi }$ do not appeai in thcse cquations because they involve $\lambda , l ,$ ${ \mathfrak { p } } ,$ 01 $\pmb q$ ag $\mathfrak { a }$ farlor This fact follows fiom the propeities of $\mathfrak { C }$ given m Ail 226 and thc form of equalions (1o3) and (104)

Each pei lubmg planet conliibutcs terms m the nght membeis of cqualions (1o7) sunilar Lo thc oncs wiitten which come from $m _ { 2 }$ These diffeienlinl cquations aie not stnctly coiect, simce the fnsl uppioxumalion has ahcady bcen made in neglecting the higher powers of tho variables

Tho Hocond slep is in the method of tieating the difteiential cqualions.Tho cxpansions of the R,，contam certain terms which aro independenl of thc time,which m the odinary method give rixo to tho sccului teimsLet Ro,repiesent these teims Lugiango lhen trealed the diffoiential equations by neglecting the poriodic terma in $\smash { R _ { 1 , n } }$ and wnlimg

$$
\left\{ \begin{array} { l } { { d h _ { i } } } \\ { { \displaystyle { d \bar { l } ^ { i } } = + \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial { R ^ { ( 0 ) } } _ { 1 , j } } { \partial l _ { + } } , \qquad ( \dot { \iota } = 1 , { \bf \sigma } \cdot { \bf \sigma } , n ; \ j \ne i ) , } } \\ { { d l _ { i } } } \\ { { d \mathcal { U } = - \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial { R ^ { ( 0 ) } } _ { i , j } } { \partial h } , } } \\ { { d p _ { i } } } \\ { { d l } } \\ { { d l _ { i } } } \\ { { \displaystyle { d \bar { l } ^ { i } } = - \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial { R ^ { ( 0 ) } } _ { 1 , j } } { \partial p _ { i } } , } } \\ { { \displaystyle { d \bar { l } ^ { i } } = - \sum _ { j = 1 } ^ { n } m _ { i } \frac { \partial { R ^ { ( 0 ) } } _ { 1 , j } } { \partial p _ { i } } . } } \end{array} \right.
$$

Tho valucs of h, l, p，and q, determined from equations (108) are uscd instcad of thc sccular teims obtained by the mcthod of Ail 227. The process of breaking up a differential cqunlion in lhis manncr is nol permissible except as a first approximation,and any conclusions based on it are open to suspicion.

In spitc of the logical defects of the mcthod and the fact lhat it cannot be geneially appled, theie is ltle doubt that in the piescnt case it gives an accurate idea of the actual mannel in which thc elemcnts valy

The nght membeis of cquations (1o8) arc expandlcd in poweis of h,l,P,and q.,and all of tho terms excopt those of the fist degice aic neglected,consequcntly the terms omittcd in (107) would have disappeared here if they had been rctaincd up to this point. The system becomes lineai，and the detailed discussion of tho R., shows that it is homogeneous, giving equations of the form

$$
\begin{array} { r }  \{ \begin{array} { l l } { \frac { d \lambda _ { 1 } } { d t } - \frac { \lambda _ { 2 } } { 2 } \tilde { c } _ { 1 , 2 } = 0 , } \\ { \{ \begin{array} { l l } { \frac { d \lambda _ { 1 } } { d t } + \frac { \lambda _ { 2 } } { \tilde { c } _ { 1 , 4 } } \tilde { c } _ { 1 , 4 } = 0 , } \\ { \frac { d \lambda _ { 2 } } { d t } - \frac { \lambda _ { 3 } } { 2 } \tilde { c } _ { 2 , 4 } = 0 , } \end{array}  } \\ { \{ \begin{array} { l l } { \frac { d b _ { 2 } } { d t } - \frac { \lambda _ { 3 } } { 2 } \tilde { c } _ { 2 , 4 } = 0 , } \\ { \frac { d b _ { 3 } } { d t } + \frac { \lambda _ { 3 } } { 2 } \tilde { c } _ { 3 , 4 } = 0 , } \end{array}  } \\ { \{ \begin{array} { l l } { \frac { d b _ { 4 } } { d t } + \frac { \lambda _ { 4 } } { \tilde { c } _ { 3 , 4 } } \tilde { c } _ { 3 , 4 } = 0 , } \\ { \frac { d b _ { 4 } } { d t } - \frac { \lambda _ { 3 } } { 2 } \tilde { c } _ { 4 , 4 } = 0 , } \end{array}  } \\ { \{ \begin{array} { l l } { \frac { d b _ { 4 } } { d t } - \frac { \lambda _ { 4 } } { \tilde { c } _ { 5 , 4 } } \tilde { c } _ { 4 , 4 } = 0 , } \\ { \frac { d b _ { 6 } } { d t } - \frac { \lambda _ { 5 } } { 2 } \tilde { c } _ { 6 , 4 } \tilde { d } _ { 4 } = 0 , } \end{array}  } \end{array} \end{array}
$$

and a similar system of equations in the $\pmb { \eta } _ { \pmb { \mathscr { I } } }$ and tho ${ \pmb q } _ { \pmb { i } } .$

The cocfficicnts c, dopcnd only on the major axes (tho e not appearing in the secular terms) which aie consideicd as bcing constants, since the major axes have no secular terms in tho peiturbations of the fist and second ordors with iespeet to the masses. It is to be noled here that the assumplion that the cj are constants is not strictly true becauso the major axes have periodic perturbations which may be of considerablc magnitude

When these lmear cquations are solved by tho method uscd in Art.160, the values of the variables are found in the form

$$
\begin{array} { l l } { { \displaystyle { \hat { h } } _ { * } = \sum _ { j = 1 } ^ { n } H _ { \eta } e ^ { \lambda j \ell } , } } & { { \qquad l _ { i } = \sum _ { j = 1 } ^ { n } { \cal Z } _ { i \eta } e ^ { \lambda j \ell } , } } \\ { { \displaystyle { p } _ { * } = \sum _ { j = 1 } ^ { n } P _ { \eta } e ^ { \mu _ { j } \ell } , } } & { { \qquad g _ { i } = \sum _ { j = 1 } ^ { n } Q _ { i _ { 2 } } e ^ { \mu _ { j } \ell } , } } \end{array}
$$

wheie thec Iu, Ly, P, and Q, ao constants depending upon the mtial conditionsA detuled discussion shows that the X, and μ αic all pure imaginatics with veiy small absolute values, therefoie the h, l P, and qoscillate around mean values with very long per10d4. $( ) { \mathfrak { r } }$ Hnce the $\theta _ { 3 }$ and tan $\iota _ { \mathfrak { i } }$ ale expiessible as the Bums of nquaies of the $h _ { 1 } , l _ { 1 } , p _ { 1 } ,$ and ${ \bf \mathit { q } } _ { \mathfrak { N } }$ it follows that they also perfotm amnll osemllations with long peuiods, for example, the corentieity of tho carth's oibit 1s how deereasing and will continue to decreugo for aboul 24,000 yearg

Iquations (1og) admil mtcgials first found by Laplace in 1784, which lead piarlically to the samc theorem They are

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } { n _ { j } a _ { i } } ^ { 2 } ( { h _ { j } } ^ { 2 } + { l _ { j } } ^ { 2 } ) = \mathrm { C o n s t a n t } = C , } \\ { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } { n _ { j } a _ { i } } ^ { 2 } ( { p _ { i } } ^ { 2 } + { q _ { j } } ^ { 2 } ) = C ^ { \prime } ; } \end{array} \right.
$$

or, becauso of (103) nnd (104),

$$
\begin{array} { r } { \left\{ \begin{array} { c } { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { j } m _ { i } { } _ { i } { } ^ { 2 } e _ { j } { } ^ { 2 } = C _ { j } } , } \\ { \displaystyle { \sum _ { j = 1 } ^ { n } m _ { i } n _ { i } a _ { j } ^ { } \tan ^ { 2 } { i _ { j } } = C ^ { \prime } } , } \end{array} \right. } \end{array}
$$

whero ny is tho moan motion of mj. The constants C and C' as dotorminerl by lho intial conditions are very small,and snce thc lofl membors of (112) aio mado up of positive terms alone, no $\pmb { e } _  \pmb { \} }$ or if cani ovor becomo vory great. There might be an exception f lho corresponding my woio vory small compared to the others,

Equntions （112) givo tho cclobrated lheoiems of Laplace that lho oecenlricilics and inelinations cannot vary exeept withn very narrow limils. Alhough tho demonstration lacks complete iigor, yol tho resulls must bo consideicd as romaikable and significant. lqunlions (i2) do nol givo tho peiiods and amplitudes of the OHcillalions as do cquations (110).

230.Computatlon of Perturbations by Mechanical Quadratures. I tho neaond lerm of lhc second faclor of (84) in absolute value is grealor lhun unity,tho serles (87) does not converge and cannot bo used in computimg pciturbations. The expansions may fail beausn r and r aro vory noarly cqual; or,sometimes when they nro nol nenrly equal bccauso I is large.In the latter case another mode of oxpansion somotimes can be employed,\* but there are cases in which neither method leads to vald results. They both fail if the two orbits placed in the same plane would intersect, for n this case

$$
{ r ^ { 2 } } _ { 1 , 2 } = { r _ { 1 } } ^ { 2 } + { r _ { 2 } } ^ { 2 } - 2 i \mathrm { r } _ { 2 } \cos { ( u _ { 1 } - u _ { 2 } + \tau _ { 2 } - \tau _ { 1 } ) } ,
$$

would vanish when the two bodies arrive at a point of intersection of their oibits at the same timeUnless the periods are commensurable in & special way this would always happen. Of course,it is not ncccssary that ri,z should actually vanish in ordei that the expansion of (84) should fal to converge. 1

Perturbations can be computed by the mcthod of mcchanical quadratuies without expanding the perturbative function explicitly in terms of the time Consequently, this method can be used in computing the distuibing cfects of planels on comets and m other cases wheic the cxpansion of Ri,2 fails altogelher or converges slowlyLet s iepiesent an elcmcnt of the orbil of m1，then cauations (77) can be written in the form

$$
\frac { d s } { d t } = f _ { s } ( t ) ,
$$

and the perturbations of the first ordei in the interval tn - to are

$$
s = s _ { 0 } + \int _ { t _ { 0 } } ^ { t _ { n } } f _ { \bullet } ( t ) d t ,
$$

where so is the value of satt = tn

The only dificulty in computing pertuibations ig in forming tne integials indicated in (113). When the peltuibativc function cannot be expanded explcitly in terms of t the primitive of the function f.(t) cannot be found． But in any caso tho valucs of f.(t) can be found fol any values of t,and fom tho valucs of f.() for special values of t an approximation to tho intcgral can be obtamed．Geoimetrically considered, the inicgral (113） is tho area comprised between the t-axis and tho curvef=f.(t) and the ordinates to and tn An approximate valuc of the integral is

$\pm \ : s _ { 0 } + f _ { 4 } ( t _ { 0 } ) ( t _ { 1 } - t _ { 0 } ) + f _ { a } ( t _ { 1 } ) ( t _ { 2 } - t _ { 1 } ) + \cdot \ : \cdot + f _ { a } ( t _ { n - 1 } ) ( t _ { n } - t _ { n - 1 } ) .$ The intervals t- to,t - ti，‘,tn - tn-1 can bc laken so small that the approximation will be as close as may be dcsncd.

Another method of obtaining an approximate value of the inte-\*Tisgerand, Mcanque Celeate, vol,1,chap l, grnl is to replaee tho cu vo $f _ { \gimel } ( t ) ,$ whose expicit value in convenient foim may nol bo oblainable, by $\mathfrak { a }$ polynomial cuve of the nth degree whieh ngiees m valuc with $f _ { o } ( t )$ at $t = t _ { 0 } , t _ { 1 } , \cdot \cdot , t _ { n }$ The quution of thng polynomial is

$$
\begin{array} { r } { f _ { s } = + \frac { ( \ell - l _ { 1 } ) ( \ell - l _ { 2 } ) \cdot \cdot } { ( l _ { 0 } - l _ { 1 } ) ( l _ { 0 } - l _ { 2 } ) } \frac { ( \ell - l _ { n } ) } { ( l _ { 0 } - l _ { n } ) } f _ { s } ( t _ { 0 } ) } \\ { + \frac { ( \ell - l _ { 0 } ) ( \ell - l _ { 2 } ) } { ( l _ { 1 } - l _ { 0 } ) ( l _ { 1 } - l _ { 2 } ) } \frac { ( \ell - l _ { n } ) } { \cdot \cdot } \widehat { ( l _ { 1 } - l _ { n } ) } f _ { s } ( t _ { 1 } ) } \end{array}
$$

$$
+ \cdot ( { \frac { ( t - t _ { 0 } ) ( t - t _ { 1 } ) } { ( l _ { 1 } - l _ { 0 } ) ( l _ { n } - l _ { 1 } ) } } \cdot ( { \bar { t } } - t _ { n - 1 } ) \cdot ) f _ { s } ( t _ { n } )
$$

Snco thore is no lroublc m foiming the integral of $\mathfrak { a }$ polynomial thele 14 no trouble m computing tho pci turbation of s for the intmval $t _ { n } - t _ { 0 }$ If the valuo of thc function $f _ { s } ( t )$ 1s not changing very rapidly or uregulaily, ils opresentation by a polynomial is very exnet piovided lhe inlcrvalg l - to, · ·, tn - tn-1 are not too genl.

IIowovm,tho arcn belween the polynomial, the $\scriptstyle t .$ -axis,and the lmttng ordmntey s nol lho best approximalion to the valuc of lho inlegrul lhal can bo obtained fiom thc values of fe(t) at to, .,ln. The values of lho funclion give infoimation respectig tho naluo of lho cuivaiuro of tho cuive betwecn thc ordinates (this bemg lruc, of courso, only beeause thc function f.(t) is a reguiar function of t),and corrections of the area due to these cu valuues can cauly bo made. Oidinauly they would involve the dorivativeH of f.(l) nt lo, · ,ln, wheh would iequne a vast amount of labor to compule； but tho derivativcs can be expressed with fufhoont upproxinaiion m terms of thc successive differences of tho funclion,and tho difforences arc obtained duectly from the labular vnlueg by simplo subtraclion. Thc derivation of the mosl convonicnl oxplcit formulas is a lengthy matter and must bo omttcd \*

Supposo lho computalion of tho integrals from the vaiues ot f(l）all= lo， ,ln has nol given resullg which are suffciently cxact. Moro oxnet oneg can bc obtaincd by dividing the interval ln-lo inlo n gronter nuinbor of sub-inteivals. A lttle experience usually makcs il unnccessary to subdivide the intervals frst chosen.

\*Sec Tgeranl' Mcanque Celeato, vol.iv，chaps x and xi； and Char Hr'g Mechamk des Immls, vol 1., chap.1

Theie is a second icason why the results obtained by mcchanical quadatues may not be sufficicntly cxact It has so far bccn assumed thatf(t) isa function of t alone,oi,in othel woids, thal tho elemcnts of the oibits on whch it depends aic constants This is thc assumption in computing peituibations of tho fiist oiderIf it 1s not cxact enough,ncw valucs of $f _ { \theta } ( t _ { 1 } )$ ，， $f _ { \theta } ( t _ { n } )$ can be computcd, on using im them thc icspectivc valucs of the cleinents s which welc found by thc fisl imtcgiation From thc ncw valucs of $f _ { \mathfrak { g } } ( t _ { 1 } )$ 、， $\int _ { \theta } \bigl ( t _ { n } \bigr )$ a mole appioximate valuo of the integral can bc obtained. Unlcss the inteival ln - to is too great this process conveiges and the intcgial can be found with any desircd degicc of appioximalion,bccause this mcthod 1s simply Picaid's method of succcssivc appioxiinations whose valdity has bcen cstabhshcd \* In practice it 1s always advisable to choose the interval tn - to so short that no repetition of tho compulation with impioved values of thc function al thc onds of the sub-intcrvals will be rcqunedAl cach ncw glage of tho intcgration the values of the clementg at thc cnd of thc picrcding step ao cmploycd It follows lhat the method,as just cxplaincd, enableg onc to computc not only the pei turbations of the first oidel, but peituibations of all oideis cxcept for the lmitations thal the mtervals cannot be takcn indcfiniicly small and the compuiation cannot bc made with mdefimitcly many places

The piocess of computing pcituibations by thc mothod of mechanical quadiatuies, as compaicd with that of using the expanded form of the pei tuibalivc funetion, has ils advantages and its dsadvanlages. It is an advaniage that in cmploymg mechancal quadialuies it is not ncccssaiy lo cxpicss tho peiturbing forces explicilly m teims of the clcmcnts and thc lime This is somelimes of great importancc,for,in cases wheio the eccentiieities and inclnations aie laigc,as in some of tho astcroid orbits,these cxpiessions,which are sciics,aio very slowly con\~ vergent；and m the case of orbits whose ecccntrcitics excccd 0 6627,or of orbits which have any radius of ono cqual to any radius of tho othcr the scrics aie diveigent and cannol bo uscd. The method of mechanical quadiatuies is cqually apphcablo lo all kinds of orbils,the only iestiiction being that the mlcrvals shall be taken sufficiently shoit It is the method actually cmployed,in one of its many foims,in compuling the poituibationg of the orbits of comets

\*Picard's Trate d'Analyse, vol 1, chap,xI,bection 2

The digadvantages aie that,in odei to find by mechamcal quadiatuics thc valucs of the elements at any paiticular time, it is neccssaiy to compute them at all of the inteimcdiate epochs. Bcing puicly nuinciical, il thiows no lght whatever on the general chaiaclei of peilubalions,and leads to no geneial theorems iegatding the stability of a syslemThese aie questions of gicnt inteicst,and somc of lhe most billant discoveries in Celestal Mcchanies have been made iespecting them

231.General Reflections.Astionomy is the oldest science and m n coi lain sonse thc paient of all the othersThe relatively simple and iegulauly iccuiing cclcstial phenomena fnst taught men,im thc days of thc ancient Giceks, that Nature is systematic and ordeilyThc importance of tlis lesson can be inferred from tho fact that it is the foundation on which all science is based For a long time progiess was painfully slowCenturies of observalions and ntiempts at thcorics fo1 explaining them were necessaiy befoic il was finally possible for Kepler to derive the Iaws which aio a fiist appioximalion to the dcscription of the way in which tlo planets move. The wonder is that,in spite of the distractions of tho constant sliuggles incident to an unstable Bocial ordel, thcre should have bcen so many men who found their greatest plensuro In pationtly making the laboiious observations which weio ncccssaiy to cstablsh the laws of the celestial motions

Tho woik of Keplcr closed the piclimmaiy epoch of two thousand ycars,or moro,and the billiant discoveries of Newton opened anothcr. Tho invention of the Calculus by Newton and Leibnitz fu nishcd for the firal time mathematical machinery which was al all sulable for grappling wilh such difficult problems as the disturbing cffccls of the sun on tho motion of the moon, or the mutual pcrturbalions of the planets. It was fortunate that the lelescopo was inventcd about the same time,for,without its use, it would nol havo bcen possible lo have made the accurate observations which furnishcd tho numerical data for the mathematical lhcorics and by which they were tested The history of Celestial Mechanics during thc cighicenth century is one of a continuous series of triumphs Tho analytical foundations laid by Clairaut, d'Alemboll,and Euler foimed the basis for the splendid achievemonls of Lagrange 'and Laplace. Their successors in the ninelconth centuiy pushcd forward,by the same methods on the whole,the lhcoiics of the motions of the moon and planets to highor oiders of approximation and compared them with more and better observations. In this connection the names of Leverrier,Delaunay,Hansen, and Newcomb will be espocially icmembered Near the close of the nineteenth contury a thnd epoch was entered. It is distinguished by new poinis of vicw and new methods whioh,in power and mathematical rigor,cnoimously surpass all those used beforeIt was inauguatcd by IIill m his Researches on the Lunar Theory,but owes most to the bnlliant contributions of Poincare to the Problem of Thico Bodics 1.1

At the present time Celestial Mechanics is entitlcd to be lcgaiaca is the most pelfeot scicnce and one of the most splendid achiovenents of the human mind. No othcr science is bascd on so many observations extending over so long a time. In no othci scicnco s it possible to test so critically its conclusions,and im no othcr are theory and expeiience in so perfect accord Tlore aic thousandg of small deviations fiom conic section motion in the orbits of the planets,satellites,and comcts where theoiy and the obscrvationg exactly agico,while the only unexplamcd iricgularitics (probably due to unknown foices) are a veiy fcw small oncs in the motion of the moon and the motion of the pciihelion of the orbit of Mercury. Over and over again theory has outrun practiso and indicated tho existcnce of pecularitics of motion which had not yet been dorived from obscrvations. Its perfection duing the time covered by experiencc inspics confidencc in following it back into the past to a time befoie observations began, and into the future to a time when perhaps they shall have ccasedAt the telescope has brought wilhin the range of thc cye of man thc wonders of an cnormous space, so Celestial Mcchamcs has bioughl within reach of his reason the no lesser wondcrs of a coriespond. ingly enormous time. It is not to be marvcled at that ho find: profound satisfaotion in a domain where he is largcly fiecd frorx the restrictions of both spaco and time.

# XXVII. PROBLEMS.

1 Supposo (a） that Ri, is largo and nearly constant,(） lhat Ri, is large and changing rapidly， (c) that Ri,a is gmall and nearly constantI the perturbations aro computcd by mechanical qundraluics how Bhould tho tn-to bo chosen relntively in the three cages,and how ghould lho numbors of Bubdivisions of tn-to compare？

2.The perturbative funotion involves tho reoiprocal of the distanco from the disturbing to the disturbed planete Thng is called tho prenmpal parl and mves tho most difficulty im the developmont. Iow many Boparate reaiproal dietaneea must bc dovcloped in ordet to compute,in a system of ono gun and n planels, ${ ( a ) }$ tho peitubations of the first order of one planet, $( b )$ the perturbaliona of lho fial oidei of two planetg,(c) the pertmbations of the second o de of ono plnnet, and $\mathit { ( d ) }$ tho pet tubatona of the third oider of one planet?

3Whal minphfintions would there bo m the development of the pere tuibntivo funtion if te mutunl nclnations of the orbits weie zeroand if the obils woro oirelen?

4 Wlnt HoltA of loims willin general appeal in perturbations of the third orde wilh icspect to tho masses?

# IISTORICAL SKETCII AND BIBLIOGRAPIY

Tho theoy of peitmbatons,ag apphed to tho Lunar Theory,was doveloped from tho gromotnenl Btundpont by Newton The memoirs of Clauaut and J'Alembeit m i747 comtamed unpoitanl advanceg,making,the Bolutions depond upon the integiataou of tho hiffeiontial cqmationg in sones Clairaut Hoom had ornylon to upply hrg piocesgcs of intcgiation to the pertubationg of IIalloy's comcl by the pluuels Jupite and Salurn This comet had been obyeived m 1531,1607,and 1682 If its period were constanl it would pas8 to pehchon agun about tho imidle of 17b9Clanaut computed the pettu buhons dno to tho alraetions of Jupter and Satun,and piedicted that tho poihehon pango wmld bo Amil 13,17b9 Io iemaked thnt the time wna uim eitan to tho oxtent of a month becanso of the uncei taintieg in the manney of Jupilol and Hutmn and tho pogabihty of peitubations from unknown planela boyond thoue bwo Tio comct pagsed the penhehon March 13, ivmg a ntnking pioof of tho valuo of Clraut'a methods

The theory of tho pertubauonB of tho planotg was begun by Euler,whose momoun on the muual potuibniong of Jupitei and Saluin gained the prizes of tho Fiench Atndomy in l748 nnd I7b2 In thcgo momons was given tho li8l nmmlylual devclopment of tho method of the vmiation of paramoterg Tho cqunliong wota nol eninoly gencial na ho hnd not conadcred the elements asbong all simulluneously vnuablea Tho fisl steps in the development of tho pm tubntive funelion wero ntso given by Eulel

Lugttnge, whoyo contnbntion lo Coleshal Mechanes were of tho most bmlliant chactei,wiole his hrsl mcnon m I7Go on the potubations of Jupitor nnd Sniun In tlg wmk h developed still furthei the mcthod of lho vumtion of pinmotoin,levng h final cquntionahowever,still mcrreet by iepaiding tho mujoi nxen and the cporhs of tho penhehon pagsage8 ag ronstanfg in dmivmg Lho equniiona for the vnriationgThe cquations for tho mehnnfiou, notle,und longitude of tho porihchon fom the node were pcfeetly rolicelJn lho oxpicaylonn fol tho mean longitudes of tho planeta theto wme teims nopoiaonal to lho fist nnd serond powee of the time Thcsu woro ontncly duo to tho unpofeetong of the method,their true form being thnt of tho long peniod totms, ns was shown by Laplace m 1784 by considoring tomg of tho tlnd odel n Cho eecentrieiticsThe method of the varintion of parnmcteia wns completely dovoloped foi the fist time in 1782 bv Lnuianuo m a plizo meinon on tho porturbations of comets moving in ellptical orbits By far tho most extensive use of the method of variation ol paramoteis i8 due to Delaunay,whoso Lunm Theory 1s cssentially a long Buccession of the applications of tho process, each stop of it reinoving a term from the perturbative function

In 1773 Laplace picsented his first memoir to tho Iionch Academy ot Sciences In it ho proved his celebrated theoiem that,up to tho sccond powers of tho cccentiieities, tho major axc8, and conscquently tho mean motions of tho planets, have no scoular teimsThis theorein was oxtended byLagrange in 1774 and 1776 to all powers of the cccentriciticg and of tho sine of theangle of the mutual inclnation, fol pertuibations of the firal order with respect to tho magscs Poisson proved in 18o9 that the major aves have no purely seoular terms in the pertu bations of the Becond order with icepect to tho masses Haretu piovcd m his Disseitation al Sorbonne m 1878 that there arc seculnr' vaiiationg in the oxpicsgions foi the major axcs in thc tei mg of the third order with icspcct to the mhsses In vol xix of Annales de l'Observalorre de Parus, Eginitis congideied teims of Blill higher ordor with respect to tho mas8cs

Lagrange began tho study of tho secular torms in 1774, introducing tne variables h,l, p, and q Tho mvestigations were caried on by Lagrango and Laplace, cach supplemonting and extending tho work of tho othor,until 1784 when thcir work bccamo complete by Laplaco'B dhscovery of his colobrated enuations

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { j } ^ { 2 } a _ { j } ^ { 2 } = C , } \\ { \displaystyle \sum _ { j = 1 } ^ { n } m _ { j } n _ { j } a _ { j } ^ { 2 } \tan ^ { 2 } \tau _ { j } = C ^ { \prime } . } \end{array} \right.
$$

Thego equations were dorived by using only tho lincar termB in the differentinl equatons.Loverrier,IIill,and othors have extendcd tho work by mothods of Bucccssive approximations to lcrms of highcr degrco Nowcomb (Smthsonzan Contrrbutrons to Scrence, vol xxi,1876) hag cstabhshed iho moro fa-ronohing results that it 18 possiblo,in tho case of tho planelary portubations, to reprc-Bent the elomonts by purely periodio functions of the timo whioh formally Batisfy the differential cquations of motion If thege serics woro convergont the stability of the solar systom would be assuied；but Poincar6 has shown that they aro in genornl divorgent (Les Mtthodes Nouvelles do la Mccanique Celeste, chap.ix） Lndstedt and Gyldon havo also sucoccded in integrating tho equations of tho motion of n bodies in periodic gerics,which, howover, are in general divergenl

Gaueg,Airy，Adams, Leverrier, Iangen,and many otherg havo mado important contributions to the planetary thoory in Bome of its many aspoots. Adams and Leverrier are notoworthy foi having predicted the oxistonco and apparent position of Neptune from tho unexplamcd iriegulniitics in tho motion of Uranus More recontly Poincare turned his attontion to Celestial Mechanicg, publishing a pri7e memoir in the Acla Malhemalica, vol xur Thig momoir waB enlarged and publshcd in book foim with the title Les Mehodes Nouvelles de la Mlcanque Celeste Pomcar6 appled to lho problom all tho regourcca of modern mathematics with unrivnled genius,ho brought inio the invcstiga tion such a wealth of ideas,and ho devised methode of suoh immonso power that the subjeet in its theoietical agpecta has been entuely revolutionzed in hishandeItcannol be doubted that much of the work of the next fifty yearg willbe in anplifying and applying the procesges which he explained

The following wolks should be consulted

Laplace's Aecannque Cleste, containing practically all that was known of Celestial Mechnnics at thc time it was writlen (1799-1805)

On the varintion of parnmetes-Annales de l'Obseruatore de Pars, vol 1, Tisgerand's Mleanque Celeste,vol 1,Brown's Lunar Theory，Dzobek's Planeten-Bewegungen

On the development of tho pcrturbalive funetion-Annales de t'Observatore do Paig,vol 1,Trand's Mcanque Celeste,vol1nsen's Entmckeug des Pioducly ciney Potenz des Radiug-Vectors mit dem Sinus oder Cosrnus eines Viclfachen der wahen Anomale,clo,Abh d K Sachs Ges zu Lerpzg,vol I, Nowcomb's Incmoir on the Goncinl Integrals of Planetaiy Motion,Poncar6, LcsMethodes Nouvellcs,vol 1,chap VI

On the stabilty of tho solar syatem-Tsgoinnd's Mecanque Celesle,vol 1, chapa x1，xv，xvi,and vol Iv,chap xxvi,Gylden,Traité Analyhque les Oibites absolucs,vol 1,Nowcomb,Smthsonian Cont,vol xxi,Poncré, Le8 Melhodes Nouvelles de la Mecanque Celeste,vol I,chap

On tho subject of Celestinl Mechamc8 ng & whole there is no better work avnilablo than lhat of Tsserand,whtoh should boin the posseaaion of every ono givmg spccial attention to thie subject.Another noteworthy work 1s Chailor'a Mechanzh des Iimmels, which,besideg maintaininga high order of gencial oxcellonco,is unoqualcd by olher troaliscs inits digaussion of periodic solutions of tho Problom of Thrco Bodtcs.

# INDEX.

Abbott,66   
Acceloration in rectiincnr motion,9 curvilnearmotion,1i   
Adams,363,432   
Airy,363,306,432   
Albategnius,32   
Allegict,319   
Almagest,32   
Al-Sufi,32   
Anaximander,31   
Annual cquation,348   
Anomaly,ccconi,159 mean,159 truo,155   
Appell,7,10,35,97,162   
Archimedeg,33   
Arealvclocity,15 Argument of ntitudo,162 Aristaichus,31 A1istotlo,3i Atmosphercs capo of,46 Attraction of circulardiscs,108 lpsoid99,122,127 Bpheicg,99,101,104, 114 Bpheroids,119,12,1   
Backhouge,305   
Ball,WWR,3   
Bnltzer,376   
Barker'B tnblea,166   
Barnard,305   
Bauschmgor,260   
Bernouli m,190 J,67   
Berry,35   
Bertiand,97   
Boltzmann,3,67   
Bour,319   
Broraon，305   
Brown,351,362,365,433   
Bruns,218,276,281   
Buchanan,Daniel,2   
Buchholz,222,260   
Buck,320 Budde,35 Burbury，07 Burnham,85 Cajor, 35 Calory,60 Canonical cquations, 890 Cantor,35   
Carmichaol,35   
Cauchy,367,378   
Center of giavity22 m,10,20,24   
Central forco,69   
Chaldacans,31   
Chambetln and Sahsbury，68   
Charle1,216,259,427,433   
Chaslcg138,139   
Chauvcnot,190,197   
Circularorbits fo thrce bodieg，300   
Clanaut,366,303,364,367,429,481   
Clnusus,07   
Contraolion thcory of sun's hoat, 03   
Copoinicus, 33   
d'Alombert,3,7,363,429,431   
Dnmoiscnu,304   
Darboux,97,18   
Darwin,68,139,280,281,805,320 Delambie,36 Delnunny,364,430,432 DoPontcooulant,304 Degcnitcs/190 Despcy1ous,97,18 Drentilce,2,220 Differential oquations of orbit,80 Duichlct,138 Disturbingfoccscoluton of,324 Doolttle,ric,361 Doublepoints of surfaccs of zoro vo locity,290 Doublo stai orbits,85 Duhng35 Dziobek,433 Eccentric Anomnly,159 Eginitis,432 Egyptians,30 Eements of orbts,146,148,183 Elemente,temeda192 Enery， Equations ofrolativ motion,142 Equpotentil curyc283 rfacc，118 Eratosthenes,31 Eacapo of atmospherea,46 Euclid,2 Euler24,34,138,158,190,258,303, 864,367,429,431 Eulo cquaon17,275 Eveotion,the,69

d1gtnnce, 92   
fftlpower   
ofdi8   
tanco,93   
alileo,3,33,34,07   
u88,138,130,153,154,188,190,   
193,194,281,238,240,242,243,   
244,249,259,200,300,361,432   
ggcquaon238,240   
egengchon,305   
ibbs,260   
3ashicr,07   
Jrnnl,36   
eek phlogophea,30,420   
rn100,181   
Grfin,88,97,320   
Gyldon,305,432   
Halley,268,348,363   
Halphen,97   
mton,3,275   
IInnkel,35   
nsen,804,430,42,4   
ou,42   
Harknes andorloy，202   
Iarzo,231,232,259   
cnt of sun,59   
Ioght ofprojeoton,4   
Iclmholtz,0,68   
Ierodolug,30   
Herehe，on,325,305   
Willam,86   
Iorlz,3,35   
Ilbeit,07   
L08,280,281,287,310,361,352,   
350,361,365,430,432   
Hpparcg,1,32,   
Iolineg，08   
Homorod,100   
Iuyglon,34   
Idoler, 36   
Indopendent star-numbora,194   
Infinitcsimal body,277   
Intogal ofre144264   
conlei of masg 141,262   
Intogral of onoigy,207   
Interonrics,172200,202   
227,877   
Invarfable plno，266   
Ivory，11,127,12,18   
Jacob1,139,207,274,275,280,281   
310   
Jacobi'snlegral,280   
Jcans,07   
Joulo,60

Kopler33,82,83,152,190,429   
Kope859,1,165 lawg,82 third law,152   
netie thcoy of ga8c46   
Kirchhoff,3   
Klnkeifueg222,260   
Koengs,35,07   
nertius,30   
rnngo,7,34,107,132,138,161, 103,227,259,277,312,319,363, 304387,418,421,423,420,481, 432   
Lagrango's biackets, 387 quntic cquation, 12   
Lagrnnginn golutions of tho pioblem ofthreebodeg，277,291,309,313   
Lambo1t,158,268,259   
Lano,68   
Laplnco,34,132,138,172,193,194, 231,249,258,259,206,275,319, 348,350,352,362,304,367,418, 425,420,431,432,433   
Lnuo,35   
Law of arong, 69 convelse of,73 forcen binary star,86   
Laws ofangulai nndlinearvelocty,73 Kopler,82 motion,3   
Lobon,35   
Legondro,97.138   
Lohmann-Fihs,319   
Leibmitz,429   
Lconaido da Vinc33   
Lcngohncr,222,231,232,259   
Lovol sufaccs,113   
Loverr10r，361，303,400,406,413, 430,482   
Lovi-Civita,208   
Lingtcd,310,432   
Louvillo, 19   
Longpeiiod inequalities 361,371, 416   
Longley，320 Lovo,35 Lubbock,884   
Lunai thcory,337 MarCullagh,138 Mnch,3,6,35 Maclurn34132139 McMilln1 Mm1,5 Mathicu,319 Maxwell,67 Mnyer,Robeit,68 Tobins,304 McCormack,36 Mcnn nomaly,159   
Mechanical qundratuicg,425   
Metcorio theory of sun's heat,62   
Melon,31   
Motoniccyclo,31   
MoyeOE,67   
Molion of apgidcs,362 center ofmasg,141,262 fallng puiticleg,30   
Neumann,139   
Newcomb,276,361,430,432,438   
Newton,IIA,02,305   
Nowton3,5,67,29,33,3467,82, 84,97,09,101,138,190,258,275, 320,327,350,356,365,429,431   
Nowton'B w of gvitaion,82,84 lawe of molion,3   
Normal form of difeiental equationg, 76   
Node,ascending, descending, 182   
Nyren,318   
Olbers,259   
Omar,32   
Oppolzor,150,222,242,260,370   
Orderof difforentinl cquaions74   
Osculaling conic, 322   
Parabolic motion,56   
Parallacto mcqualily,352   
Paiallelogram of foices,5   
Pcodiertong71,41   
Perturbationg,mcaning of,321 by oblato body,333 resisting mcdium,333 ofpsidcs，52 lement,322,382 fitst o1do,382 inclination,348 maoras,346 nodo,342 peuod,348 Perturbative function,272 rosolulion of,387 338,345,402 dovelopment of,406 Peurbach,32 Picad,378,428 Plana,364 Planck,35 Plummer,302 Poncar6,35,139,207,268,275,270 281,320,367,378,432,433 Posson,6,138,871,418,420,42 Posson terms,371 Position in clliptc oibits,168 hyperbolie obits,177 parabohc orbits,165 Potontial,109,261 Precession of oqumoxes,344 Preston,60

Problom of two bodies,140   
thrco bodics,277   
nbodicg，261   
Ptolomy,32,350   
Pythagorns,31   
Qucstion of now integiale,208   
Radau,274,319   
Ratios of triangleg,233,237   
Reatilneai molion,36   
togiomontanug,32   
Regions of ionl and unaginaiy ve  
locity，286   
Relalvity，principleof,4   
Rcsolution of disturbing forcc,387,   
338   
Ristcen,07   
3tto1,68   
Rodiiguoz,138   
Routh,35,139   
Rowlnnd,60   
Ruthcrfoid.68

3almon,88   
Saacons,32   
Saros,31   
Secular acceloiation of inoon's molion, 348   
Seculal vaiations,360,371, 417   
Sold angles,08   
Solution of linoa cqualiong by oxponontials, 41   
Solutions of pioblom of thico bodies, 290,300,313   
Spccd,8   
Spence,59   
Stability of solutions,298,300   
Stadc1,97   
Sevinus,33,07   
Surling,138   
Stoncy,46   
Surm,1   
Suifaces of zoro rolative velooity,281   
Suter,35   
Tut,35   
Tait and Stcele, 35,97   
Tannery，6   
Temporaturo of motcors,61   
Thales,30,31   
Thomson,139   
Thomsonand Tmt,3,104,189,283 Time nbeiation,226 TB8ond,97,130,190,260,267,270 205,296,312,319,365,301,407 426,427,433 Tigserand's critorion for idenlly o comcts.296 Truoanomaly,155 Tycho Brahe,33,348,850   
Unifoim motion, 8   
Ulugh Beigh,32   
Umils,153 canonicnl, 164   
Vaiinlon,tho,50   
Vauation of cooidnates,321 clemonts,322 paiamotcrg 50,322   
Vertor,6   
Velocity,8 acal, 15 fommfinty,45,40 of csoapo,48   
Villarccau, 260

Vgvivtogral78,7   
Voltaire,190   
Waltheius,32   
Walcrson,162   
Watgon,156,242,260   
WeioLaia,367   
Whowell,   
Willmson,161   
Wolf，35   
Woodwmd,4   
Work,50   
Young,184
