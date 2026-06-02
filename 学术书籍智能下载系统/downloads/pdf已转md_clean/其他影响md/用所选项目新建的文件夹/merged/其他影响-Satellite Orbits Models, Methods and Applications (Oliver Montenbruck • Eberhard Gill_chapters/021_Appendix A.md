# Appendix A

# A.1 Calendrical Calculations

The civilian calendar which measures time in terms of years, months, and days provides a convenient and well-established time scale for our daily life. It is not, however, well suited to finding the time difference between two dates or advancing a date by a certain time increment. To cope with this difficulty, a continuous day count is often used in astronomical computations, which is known as the Julian Date. It is attributed to Joseph Justus Scaliger, who introduced a “Julian Period” of 7 980 Julian years for chronological purposes (see Derwshowitz & Reingold 1997, Moyer 1981).

The Julian Date (JD) is the number of days since noon January 1, 4 713 BC including the fraction of day. It thus provides a continuous time scale which, for all practical purposes, is always positive. Counting starts at noon for historical reasons, to avoid a change of date in the middle of astronomical observations. Presently, the Julian Day numbers are already quite large (well over two millions) and it is also desirable to start counting at midnight. Therefore, a Modified Julian Date (MJD) is defined as:

$$
\mathrm { M J D } = \mathrm { J D } - 2 4 0 0 0 0 0 . 5 .
$$

A table of Modified Julian Dates for the beginning of each month between 1975 and 2020 is given in Table A.1.

Interconversion to civil calendar date and time is often done by tables, however, there also exist a number of numerical algorithms. The method described here is based upon Meeus (1978, 1991) and requires several points to be considered:

• Civil time is expressed in year $( Y )$ , month $( M )$ , and day $( D )$ . Both $D$ and Julian Day may include fraction of days.   
The years BC are counted astronomically in all formulas. E.g. 1 BC would be the year $Y = 0$ and $1 0 \mathrm { B C }$ corresponds to the year $Y = - 9$ .   
The Julian Day begins at $1 2 ^ { \mathrm { h } }$ o’clock midday.   
The Julian calendar is used until $4 ^ { \mathrm { t h } }$ October 1582 AD, which corresponds to $\mathrm { J D } < 2 2 9 9 1 6 0 . 5$ . The average length of the year in the Julian calendar was taken as 365.25 days which implied one extra day every fourth year. The true length of the mean solar year, however, is about eleven minutes less. By

Table A.1. Modified Julian Date at day 0.0 of each month. To obtain the MJD of a given date, add the day and fractions of day to the tabulated value for the respective month and year. Example: $\mathrm { M J D } ( \dot { 2 } 0 0 0 \mathrm { J a n . } 1 , 1 2 ^ { \mathrm { h } } ) = 5 \dot { 1 } 5 4 3 + 1 . 5 = 5 1 5 4 4 . 5$ .   

<table><tr><td rowspan=1 colspan=1>Year</td><td rowspan=1 colspan=11>JanFebMarAprMay JunJulAugSep OctNov Dec</td></tr><tr><td rowspan=1 colspan=1>19751976</td><td rowspan=10 colspan=11>42412 42443 42471 42502 42532 42563 42593 42624 42655 42685 42716 4274642777 42808 42837 42868 42898 42929 42959 42990 43021 43051 43082 4311243143 43174 43202 43233 43263 43294 43324 43355 43386 43416 43447 4347743508 43539 43567 43598 43628 43659 43689 43720 4375143781 43812 4384243873 43904 43932 43963 43993 44024 44054 44085 44116 44146 44177 4420744238 44269 44298 44329 44359 44390 44420 44451 44482 44512 44543 4457344604 44635 44663 44694 44724 44755 44785 44816 44847 44877 44908 4493844969 45000 45028 45059 45089 45120 45150 45181 45212 45242 45273 4530345334 45365 45393 45424 45454 45485 45515 45546 45577 45607 45638 4566845699 45730 45759 45790 45820 45851 45881 45912 45943 45973 46004 4603446065 46096 46124 46155 46185 46216 46246 46277 46308 46338 46369 46399</td></tr><tr><td rowspan=1 colspan=1>1977</td></tr><tr><td rowspan=1 colspan=1>1978</td></tr><tr><td rowspan=1 colspan=1>1979</td></tr><tr><td rowspan=1 colspan=1>1980</td></tr><tr><td rowspan=1 colspan=1>1981</td></tr><tr><td rowspan=1 colspan=1>1982</td></tr><tr><td rowspan=1 colspan=1>1983</td></tr><tr><td rowspan=1 colspan=1>1984</td></tr><tr><td rowspan=1 colspan=1>1985</td><td rowspan=3 colspan=11>46065 46096 46124 46155 46185 46216 46246 46277 46308 46338 46369 4639946430 46461 46489 46520 46550 46581 46611 46642 46673 46703 46734 4676446795 46826 46854 46885 46915 46946 46976 47007 47038 47068 47099 47129</td></tr><tr><td rowspan=1 colspan=1>1986</td></tr><tr><td rowspan=1 colspan=1>1987</td></tr><tr><td rowspan=1 colspan=1>1988</td><td rowspan=6 colspan=11>47160 47191 47220 4725147281 47312 47342 47373 47404 47434 47465 4749547526 47557 47585 47616 47646 47677 47707 47738 47769 47799 47830 4786047891 47922 47950 47981 48011 48042 48072 48103 48134 48164 48195 4822548256 48287 48315 48346 48376 48407 48437 48468 48499 48529 48560 4859048621 48652 48681 48712 48742 48773 48803 48834 48865 48895 48926 48956</td></tr><tr><td rowspan=1 colspan=1>1989</td><td rowspan=1 colspan=1>475264755747585</td></tr><tr><td rowspan=1 colspan=1>1990</td><td rowspan=1 colspan=1>4789147922 47950</td><td rowspan=6 colspan=4>48256 48287 48315 48346 48376 48407 48437 48468 48499 48529 48560 4859048621 48652 48681 48712 48742 48773 48803 48834 48865 48895 48926 4895648987 49018 49046 49077 49107 49138 49168 49199 49230 49260 49291 49321</td><td rowspan=1 colspan=2>44819548225</td></tr><tr><td rowspan=2 colspan=1>1991</td><td rowspan=2 colspan=1>482564828748315</td></tr><tr><td rowspan=1 colspan=2>485604859</td></tr><tr><td rowspan=1 colspan=1>1992</td><td rowspan=1 colspan=1>486214865248681</td><td rowspan=1 colspan=1>48712</td><td rowspan=2 colspan=5>49742 48773 49803</td></tr><tr><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>489874901849046</td><td rowspan=1 colspan=1>49077</td></tr><tr><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>493524938349411</td><td rowspan=1 colspan=1>49442</td><td rowspan=1 colspan=5>494724950349533</td></tr><tr><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>497174974849776</td><td rowspan=1 colspan=1>49807</td><td rowspan=1 colspan=3>4983749868</td><td rowspan=1 colspan=3>4986849898</td><td rowspan=3 colspan=3>50082 50113 50142 50173 50203 50234 50264 50295 50326 50356 50387 50417</td></tr><tr><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>50082 5011350142</td><td rowspan=1 colspan=1>50173</td><td rowspan=1 colspan=3>5020350234</td><td rowspan=1 colspan=2>50264</td><td></td></tr><tr><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>50448 50479 50507</td><td rowspan=1 colspan=1>50538</td><td rowspan=1 colspan=1>50568</td><td rowspan=1 colspan=2>50599</td><td rowspan=1 colspan=2>50629</td><td></td><td rowspan=3 colspan=3>310563148651171141</td><td rowspan=1 colspan=1>50782</td></tr><tr><td rowspan=1 colspan=1>1998</td><td rowspan=1 colspan=1>50813 5084450872</td><td rowspan=1 colspan=1>50903</td><td rowspan=1 colspan=1>50933</td><td rowspan=1 colspan=2>50964</td><td rowspan=1 colspan=2>50994</td><td rowspan=1 colspan=1>51025</td><td rowspan=1 colspan=2>5105651086 51117 51</td></tr><tr><td rowspan=1 colspan=1>1999</td><td rowspan=1 colspan=1>51178 51209 51237</td><td rowspan=1 colspan=1>51268</td><td rowspan=1 colspan=1>51298</td><td rowspan=1 colspan=2>51329</td><td rowspan=1 colspan=2>51359</td><td rowspan=1 colspan=1>51390</td></tr><tr><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>515435157451603</td><td rowspan=1 colspan=1>51634</td><td rowspan=1 colspan=1>51664</td><td rowspan=2 colspan=4>51695 51725</td><td rowspan=1 colspan=1>51756</td><td rowspan=2 colspan=3>51787 51817 51843 51878</td></tr><tr><td rowspan=1 colspan=1>2001</td><td rowspan=1 colspan=1>51909 51940 51968</td><td rowspan=1 colspan=1>51999</td><td rowspan=1 colspan=1>52029</td><td rowspan=1 colspan=1>52121</td></tr><tr><td rowspan=1 colspan=1>2002</td><td rowspan=1 colspan=1>5227452305 52333</td><td rowspan=1 colspan=1>52364</td><td rowspan=1 colspan=1>52394</td><td rowspan=1 colspan=2>52425</td><td rowspan=1 colspan=2>52455</td><td rowspan=1 colspan=1>52486</td><td rowspan=1 colspan=3>52517525475257852608</td></tr><tr><td rowspan=1 colspan=1>2003</td><td rowspan=1 colspan=1>526395267052698</td><td rowspan=1 colspan=1>52729</td><td rowspan=1 colspan=1>52759</td><td rowspan=1 colspan=4>5279052820</td><td rowspan=1 colspan=1>52851</td><td rowspan=1 colspan=3>52882529125294352973</td></tr><tr><td rowspan=1 colspan=1>2004</td><td rowspan=1 colspan=1>530045303553064</td><td rowspan=1 colspan=6>53095531255315653186</td><td rowspan=1 colspan=1>53217</td><td rowspan=1 colspan=3>53248532785330953339</td></tr><tr><td rowspan=1 colspan=1>2005</td><td rowspan=1 colspan=1>53370 53401 53429</td><td rowspan=1 colspan=6>53460 53490 53521 53551</td><td rowspan=1 colspan=1>53582</td><td rowspan=1 colspan=3>：53613 53643536745370</td></tr><tr><td rowspan=1 colspan=1>2006</td><td rowspan=1 colspan=1>537355376653794</td><td rowspan=1 colspan=1>53825</td><td rowspan=1 colspan=5>538555388653916</td><td rowspan=1 colspan=1>53947</td><td rowspan=1 colspan=3>53978540085403954069</td></tr><tr><td rowspan=1 colspan=1>2007</td><td rowspan=1 colspan=1>54100 54131 54159</td><td rowspan=1 colspan=1>54190</td><td rowspan=1 colspan=5>54220 54251 54281</td><td rowspan=1 colspan=1>54312</td><td rowspan=2 colspan=3>5434354373 54470 54434</td></tr><tr><td rowspan=1 colspan=1>2008</td><td rowspan=1 colspan=1>54465 54496 54525</td><td rowspan=1 colspan=7>5455654586546175464754678</td></tr><tr><td rowspan=1 colspan=1>2009</td><td rowspan=1 colspan=1>548315486254890</td><td rowspan=1 colspan=6>54921549515498255012</td><td rowspan=1 colspan=1>55043</td><td rowspan=1 colspan=3>55074551045513555165</td></tr><tr><td rowspan=1 colspan=1>2010</td><td rowspan=2 colspan=8>55196 55227 55255 55286 55316 55347 55377 55408 55439 55469 55500 5553055561 55592 55620 55651 55681 55712 55742 55773 55804 55834 55865 55895</td><td rowspan=1 colspan=1>55408</td><td rowspan=2 colspan=2>55439 55469 55500536</td></tr><tr><td rowspan=1 colspan=1>2011</td><td></td></tr><tr><td rowspan=1 colspan=1>2012</td><td rowspan=1 colspan=8>55926 55957 55986 56017 56047 56078 56108 56139 56170 56200 56231 56261</td><td rowspan=9 colspan=3>55926 55957 55986 56017 56047 56078 56108 56139 56170 56200 56231 5626156292 56323 56351 56382 56412 56443 56473 56504 56535 56565 56596 5662656657 56688 56716 56747 56777 56808 56838 56869 56900 56930 56961 5699157022 57053 57081 57112 57142 57173 57203 57234 57265 57295 57326 5735657387 57418 57447 57478 57508 57539 57569 57600 57631 57661 57692 5772257753 57784 57812 57843 57873 57904 57934 57965 57996 58026 58057 5808758118 58149 58177 58208 58238 58269 58299 58330 58361 58391 58422 5845258483 58514 58542 58573 58603 58634 58664 58695 58726 58756 58787 5881758848 58879 58908 58939 58969 59000 59030 59061 59092 59122 59153 59183</td></tr><tr><td rowspan=1 colspan=1>2013</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2014</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2015</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2016</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2017</td><td rowspan=1 colspan=5>57753 5778457812578435787357904</td><td rowspan=1 colspan=2>04579</td><td></td></tr><tr><td rowspan=2 colspan=1>20182019</td><td rowspan=1 colspan=4>581185814958177582085823858</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=5>58483 58514 58542 58573 58603 58634 58664 58695 58726 58756 58787 58817</td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2020</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

1582 AD the error in the Julian calendar, which was introduced in $4 5 ~ \mathrm { B C }$ , had accumulated to more than ten days. This led to the calendar reform under Pope Gregory XIII.

The Gregorian calendar is used from $1 5 ^ { \mathrm { t h } }$ October 1582 AD onwards corresponding to $\mathrm { J D } \geq 2 2 9 9 1 6 0 . 5 .$ The average length of the year in this calendar is 365.2425 days which deviates by less than half a minute from the mean solar year of 365.2422 days. In practice this is accomplished by inserting one extra day every fourth year, but omitting this three times per four hundred years. By convention, every year whose number can be divided by four is a leap year except when it is also divisible by one hundred. However, those years where the year number is divisible by four hundred are again leap years. In leap years the intercalary day $2 9 ^ { \mathrm { t h } }$ February is inserted.

The function entier $( x )$ or, briefly, $[ x ]$ will be used extensively in the subsequent algorithms. It is defined as the smallest integer which is smaller than or equal to $x$ , i.e.

$$
[ x ] \leq x < [ x ] + 1 .
$$

For positive numbers $[ x ]$ is equal to the integral part $\operatorname { i n t } ( x )$ of $x$ . For negative (noninteger) numbers, however, it is the integral part of $x$ minus one. Negative arguments have been carefully avoided in the expressions given below. The entier $( x )$ function can therefore also be written as $\operatorname { i n t } ( x )$ for all permitted dates.

# A.1.1 Modified Julian Date from the Calendar Date

The handling of leap years in the computation of the Modified Julian Date is facilitated by letting the year run from March 1 until the end of February. To this end $Y$ and $M$ are replaced by the quantities

$$
y = { \left\{ \begin{array} { l l } { Y - 1 } & { { \mathrm { i f ~ } } M \leq 2 } \\ { Y } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

and

$$
m = \left\{ \begin{array} { l l } { { M + 1 2 } } & { { \mathrm { i f } \ M \leq 2 } } \\ { { M } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. .
$$

The number of days since March 1 at the beginning of a month $M$ can then be expressed as $[ 3 0 . 6 ( m + 1 ) ] - 1 2 2$ as illustrated in Table A.2.

Leap days in the Julian and Gregorian Calendar are taken into account by the auxiliary quantity

$$
B = \left\{ \begin{array} { l l } { { - 2 + [ ( y + 4 7 1 6 ) / 4 ] - 1 1 7 9 } } & { { \mathrm { u n t i l ~ } 4 \mathrm { O c t . ~ } 1 5 8 2 } } \\ { { + [ y / 4 0 0 ] - [ y / 1 0 0 ] + [ y / 4 ] } } & { { \mathrm { f r o m ~ } 1 0 \mathrm { O c t . ~ } 1 5 8 2 } } \end{array} \right. .
$$

The Modified Julian Date including the fraction of day, is then given by:

$$
\mathrm { M J D } = 3 6 5 y - 6 7 9 0 0 4 + B + [ 3 0 . 6 0 0 1 ( m + 1 ) ] + D
$$

Table A.2. Annual day count   

<table><tr><td>Month</td><td>Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M</td><td>34</td><td>5</td><td>678</td><td></td><td></td><td>8 9</td><td>1011</td><td></td><td>12</td><td></td><td></td></tr><tr><td>Days</td><td>31</td><td>30 31</td><td></td><td>30313</td><td>31</td><td></td><td>3031</td><td>30 </td><td></td><td>3131</td><td></td></tr><tr><td>[30.6(m+1)]- 122</td><td>0</td><td>31 61</td><td></td><td></td><td></td><td>92 122 153 184 214 245 275 306 337</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Here, the multiplication factor of $m + 1$ is taken as 30.6001 rather than 30.6 in order to avoid numerical errors in case of limited floating-point accuracy.

Some simplifications are possible, if only a limited time interval is considered. E.g. $B$ can be replaced by a fixed value of $- 1 5 + [ Y / 4 ]$ between 1 March 1900 and 28 February 2100, because the year 2000 is a regular leap year.

# A.1.2 Calendar Date from the Modified Julian Date

The computation of the calendar date from the Modified Julian Date requires a number of intermediate steps. First, the integer Julian Day (i.e. the Julian Date at noon) is determined:

$$
a = [ \mathrm { M J D } ] + 2 4 0 0 0 0 1 ~ .
$$

At the same time the fraction of day, $q$ , is given by the decimal part of the Modified Julian Date:

$$
q = \mathrm { M J D } - \mathrm { [ M J D ] } \quad .
$$

Two auxiliary quantities $b$ and $c$ are defined as

$$
b = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } a < 2 2 9 9 1 6 1 { \mathrm { ~ ( J u l i a n ~ c a l e n d a r ) } } } \\ { \operatorname { [ } ( a - 1 8 6 7 2 1 6 . 2 5 ) / 3 6 5 2 4 . 2 5 { \mathrm { ] } } } & { { \mathrm { o t h e r w i s e ~ ( G r e g o r i a n ~ c a l e n d a r ) } } } \end{array} \right. }
$$

and

$$
c = { \left\{ \begin{array} { l l } { a + 1 5 2 4 } & { { \mathrm { ~ i f ~ } } a < 2 2 9 9 1 6 1 { \mathrm { ~ ( J u l i a n ~ c a l e n d a r ) } } } \\ { a + b - [ b / 4 ] + 1 5 2 5 } & { { \mathrm { ~ o t h e r w i s e ~ ( G r e g o r i a n ~ c a l e n d a r ) } } \quad . } \end{array} \right. }
$$

The next step is to calculate the auxiliary quantities

$$
\begin{array} { l } { d = \left[ \left( c - 1 2 1 . 1 \right) / 3 6 5 . 2 5 \right] } \\ { \ } \\ { e = \left[ 3 6 5 . 2 5 d \right] } \end{array} \mathrm { ~ , ~ }
$$

and

$$
f = [ ( c - e ) / 3 0 . 6 0 0 1 ] ~ .
$$

Finally, the calendar date is obtained from the following three steps: the day of the month $( D )$ is given by

$$
D = c - e - [ 3 0 . 6 0 0 1 f ] + q ,
$$

the month of the year $( M )$ follows from

$$
M = f - 1 - 1 2 [ f / 1 4 ]
$$

and the year $( Y )$ in astronomical reckoning is determined by

$$
Y = d - 4 7 1 5 - [ ( 7 + M ) / 1 0 ] .
$$

It is again possible to simplify the computation somewhat if only a limited time interval is considered. E.g. the computation of the auxiliary quantities $a , b$ , and $c$ can be focussed into $c = [ ( \mathrm { J D } + 0 . 5 ) ] + 1 5 3 7$ if only the interval March 1900 until 2100 is taken into account.

# A.2 GPS Orbit Models

The Global Positioning System (GPS) makes use of two dedicated representations of the GPS satellite orbits, which are known as almanac and (broadcast) ephemeris1. Both parameter sets are transmitted as part of the GPS navigation message and enable a GPS receiver to compute positions of the GPS satellites with different levels of accuracy. Almanac data are mainly used to determine the constellation of visible satellites above the horizon, to select the best satellites for navigation, and to determine approximate Doppler shifts for improved signal acquisition. The ephemeris parameters, on the other hand, provide a much more accurate description of the spacecraft trajectory that is essential for the computation of precise user-position fixes. In accord with the envisaged usage, the low-accuracy almanac parameters are always provided for the full constellation of active satellites, whereas each satellite transmits ephemeris parameters for itself, only.

Conceptionally, both the almanac and the ephemeris model are based on a Keplerian elements representation of the orbit with a suitably chosen set of correction terms modeling any deviation from an unperturbed ellipse. This enables a particularly compact parameter set at the price of a moderate computational burden. For further details the reader is referred to the respective Navstar GPS Interface Control Document (ICD-GPS-200 1997) as well as van Dierendonck et al. (1978). The latter reference addresses the rational behind the design of the GPS navigation message and the recommended computational algorithms.

Table A.3. Conventional values of specific constants employed in GPS almanac and ephemeris models (ICD-GPS-200, 1997)   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>GM</td><td rowspan=2 colspan=1>398600.5.109 m/s²7.2921151467:10-5s-13.1415926535898</td><td rowspan=2 colspan=1>WGS84 Gravitational coefficientWGS84 Earth rotation rate</td></tr><tr><td rowspan=1 colspan=1>Wπ</td></tr></table>

By convention a specific set of constants based on the (old) WGS84 system is to be applied in both the almanac and ephemeris models that is reproduced in Table A.3. Readers should be aware that the latest refinement of WGS84 constants (NIMA 1997) has not resulted in an update of the above standard.

Times are referred to the GPS system time, which differs from TAI by a constant offset of $1 9 \mathrm { s }$ and matched UTC when it was introduced in January 1980. The standard epoch 6.0 January 1980 GPS Time (JD(GPS) 2 444 244.5) serves as origin for the GPS specific week count. A GPS week starts on Sunday 0.00 GPS Time and the first week, starting at the standard epoch, is assigned the week count 0.

Accordingly, the week number for arbitrary dates is given by

$$
\mathrm { W N } = \left[ { \frac { \mathrm { J D } ( \mathrm { G P S } ) - 2 4 4 4 2 4 4 . 5 } { 7 } } \right]
$$

where brackets denote the entier function introduced in (A.2). Vice versa, GPS week WN starts at Julian Date

$$
\mathrm { J D } ( \mathrm { G P S } ) = 2 4 4 4 2 4 4 . 5 + 7 \cdot \mathrm { W N } .
$$

Within a GPS week, times are typically specified in seconds past the start of week, yielding a count of at most $6 0 4 8 0 0 { \mathrm { s } }$ .

# A.2.1 Almanac Model

Aside from the reference epoch, the almanac message of each satellite comprises a total of seven orbit-related parameters (Table A.4). These resemble the classical Keplerian elements but differ in various GPS-specific details. Instead of the semimajor axis, its square root is given in the almanac to simplify computation of the mean motion. The inclination is specified relative to a reference value of $i _ { \mathrm { r e f } } =$ $5 4 ^ { \circ }$ , which is about one degree smaller than the nominal inclination of the GPS constellation. All angular elements are given in units of semi-circles equivalent to $\pi$ radians or $1 8 0 ^ { \circ }$ . Special care is required in the interpretation of $\varOmega _ { 0 }$ which must not be confused with the inertial right ascension $\varOmega$ of the ascending node as used with classical Keplerian elements. To be precise, $\varOmega _ { 0 }$ defines the orientation of the orbital plane at the almanac reference epoch, but referred to the Greenwich meridian at the start of the respective GPS week. The parameter is thus related to the right ascension of the ascending node $\varOmega$ and the Greenwich Sidereal Time $\Theta$ by the expression

$$
\varOmega _ { 0 } = \varOmega ( t _ { \mathrm { a } } ) - \theta ( t _ { 0 } ) \quad ,
$$

where $t _ { 0 }$ denotes the start of the GPS week and $t _ { \mathrm { a } }$ is the almanac reference epoch (as defined by the $\mathrm { W N _ { o a } }$ and $t _ { \mathrm { o a } }$ counts). Due to the Earth’s oblateness the inertial right ascension of the ascending node experiences a secular change of $\dot { \Omega } \approx - 0 . 0 4 ^ { \circ } / \mathrm { d }$ , which is also specified as part of the almanac message. This allows the instantaneous Greenwich longitude $\lambda _ { \varOmega }$ of the ascending node to be computed from

$$
\begin{array} { l l l } { \lambda _ { \Omega } ( t ) } & { = } & { \Omega ( t ) - \theta ( t ) } \\ & { \approx } & { \Omega ( t _ { \mathrm { a } } ) + \dot { \Omega } ( t - t _ { \mathrm { a } } ) - \theta ( t _ { 0 } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \\ & { = } & { \Omega _ { 0 } + \dot { \Omega } ( t - t _ { \mathrm { a } } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \end{array}
$$

for arbitrary times $t$ . After solving Kepler’s equation

$$
E - e \sin ( E ) = M = M _ { 0 } + { \sqrt { \frac { G M _ { \oplus } } { a ^ { 3 } } } } ( t - t _ { \mathrm { a } } )
$$

Table A.4. GPS almanac parameters   

<table><tr><td>Parameter</td><td>Description</td><td>Units</td></tr><tr><td>WNoa</td><td>Almanac reference epoch (part 1): GPS week number (mod 256) Almanac reference epoch (part 2):</td><td>[s]</td></tr><tr><td>√a</td><td>fraction of current GPS week Square root of semi-major axis</td><td>[√m]</td></tr><tr><td>e Si</td><td>Eccentricity Inclination offset from reference value of</td><td>[semi-circles]</td></tr><tr><td></td><td>iref = O.3 semi-circles</td><td></td></tr><tr><td>小</td><td>Longitude of the ascending node at the weekly epoch</td><td>[semi-circles]</td></tr><tr><td></td><td>Rate of change of the right ascension of the ascending node</td><td>[semi-circles/s]</td></tr><tr><td>w Mo</td><td>Argument of perigee Mean anomaly at reference epoch</td><td>[semi-circles] [semi-circles]</td></tr><tr><td>ao a1</td><td>Spacecraftclock offset from GPS time Clock frequency offset</td><td>[s] [s/s]</td></tr></table>

for the eccentric anomaly at the time of interest, the position of the GPS satellite in the Earth-fixed WGS84 system can be computed from the common expressions

$$
r _ { \mathrm { W G S 8 4 } } = R _ { z } ( - \lambda _ { \itOmega } ) R _ { x } ( - i _ { \mathrm { r e f } } - \delta _ { i } ) R _ { z } ( - \omega ) \left( \begin{array} { c } { { a \left( \cos { E } - e \right) } } \\ { { a \sqrt { 1 - e ^ { 2 } } \sin { E } } } \\ { { 0 } } \end{array} \right)
$$

of the two-body problem (cf. Chap. 2). An alternative, but mathematically equivalent computational scheme is specified in ICD-GPS-200 (1997) for use within GPS receivers. It takes care of the GPS specific data representation and should be used instead of the generalized formulation introduced above whenever full consistency with the ICD is desired.

# A.2.2 Broadcast Ephemeris Model

The model associated with the GPS ephemeris parameters is essentially similar to the almanac model introduced above, but provides for a better representation of the GPS orbits by additional secular and periodic perturbations. For reference, the full parameters set is reproduced in Table A.5.

The ephemeris model first applies a correction $\varDelta n$ to the computed mean motion. Accordingly, Kepler’s equation for the eccentric anomaly is solved with a value

$$
M = M _ { 0 } + \left( \sqrt { \frac { G M _ { \oplus } } { a ^ { 3 } } } + \varDelta n \right) \left( t - t _ { \mathrm { e } } \right)
$$

Table A.5. GPS broadcast ephemeris parameters   

<table><tr><td rowspan=1 colspan=3>Parameter</td><td rowspan=1 colspan=4>Description</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=3>WNoe</td><td rowspan=2 colspan=4>Ephemeris reference epoch (part 1):GPS week number (mod 1024)Ephemeris reference epoch (part2):fraction of current GPS week</td><td rowspan=2 colspan=1>[s]</td></tr><tr><td rowspan=1 colspan=3>toe</td></tr><tr><td rowspan=1 colspan=3>√a</td><td rowspan=2 colspan=4>Square root of semi-major axisCorrection to mean motion</td><td rowspan=2 colspan=1>[√m][semi-circles/s]</td></tr><tr><td rowspan=1 colspan=3>△n</td></tr><tr><td rowspan=1 colspan=3>e</td><td rowspan=2 colspan=4>EccentricityInclination at reference epoch</td><td rowspan=2 colspan=1>[semi-circles]</td></tr><tr><td rowspan=1 colspan=3>io</td></tr><tr><td rowspan=1 colspan=3>di/dt</td><td rowspan=3 colspan=4>Rate of change of inclinationLongitude of the ascending node at theweekly epoch</td><td rowspan=3 colspan=1>[semi-circles/s][semi-circles]</td></tr><tr><td rowspan=1 colspan=3>20</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=3 colspan=1></td><td rowspan=3 colspan=4>Rate of change of the right ascension of theascending node</td><td rowspan=4 colspan=1>[semi-circles/s][semi-circles]</td></tr><tr><td></td><td></td><td rowspan=2 colspan=2></td></tr><tr><td></td><td></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=3>w</td><td rowspan=1 colspan=4>Argument of perigee</td></tr><tr><td rowspan=1 colspan=3>Mo</td><td rowspan=1 colspan=4>Mean anomaly at reference epoch</td><td rowspan=3 colspan=1>[semi-circles][m][rad]</td></tr><tr><td rowspan=1 colspan=3>Crc,Crs</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the orbital radius</td></tr><tr><td rowspan=1 colspan=3>Cuc,Cus</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the argument of latitude</td></tr><tr><td rowspan=1 colspan=3>Cic,Cis</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the inclination</td><td rowspan=1 colspan=1>[rad]</td></tr><tr><td rowspan=1 colspan=3>afo</td><td rowspan=1 colspan=4>Spacecraft clock offset from GPS time</td><td rowspan=1 colspan=1>[s]</td></tr><tr><td rowspan=1 colspan=3>af1</td><td rowspan=1 colspan=4>Clock frequency offset</td><td rowspan=1 colspan=1>[s/s]</td></tr><tr><td rowspan=1 colspan=3>af2</td><td rowspan=1 colspan=4>Clock frequency drift</td><td rowspan=1 colspan=1>[s/s2]</td></tr></table>

of the mean anomaly. Here $t _ { \mathrm { e } }$ is the ephemeris reference epoch as defined by the counters $\mathrm { W N _ { o e } }$ and $t _ { \mathrm { o e } }$ . Based on the perifocal coordinates

$$
\begin{array} { l c l } { { \hat { x } } } & { { = } } & { { a \left( \cos E - e \right) } } \\ { { \hat { y } } } & { { = } } & { { a { \sqrt { 1 - e ^ { 2 } } } \sin E } } \end{array}
$$

one obtains the (uncorrected) argument of latitude

$$
\bar { u } = \omega + \arctan ( \hat { y } / \hat { x } )
$$

from which the periodic corrections

$$
\begin{array} { c c c c c } { { \delta r } } & { { = } } & { { C _ { r s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { r c } \cos ( 2 \bar { u } ) } } \\ { { \delta u } } & { { = } } & { { C _ { u s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { u c } \cos ( 2 \bar { u } ) } } \\ { { \delta i } } & { { = } } & { { C _ { i s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { i c } \cos ( 2 \bar { u } ) } } \end{array}
$$

to the argument of latitude $( u )$ , the radius $( r )$ , and the inclination $( i )$ can be computed. Making use of the appropriately corrected elements

$$
\begin{array} { l c l } { r } & { = } & { a \left( 1 - e \cos E \right) + \delta r } \\ { u } & { = } & { \bar { u } + \delta u } \\ { i } & { = } & { i _ { 0 } + d i / d t \left( t - t _ { \mathrm { e } } \right) + \delta i } \\ { \lambda _ { \Omega } } & { = } & { \Omega _ { 0 } + \dot { \Omega } ( t - t _ { \mathrm { e } } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \end{array}
$$

one finally obtains the desired position

$$
r _ { \mathrm { W G S 8 4 } } = R _ { z } ( - \lambda _ { \itOmega } ) { \bf R } _ { x } ( - i ) \left( \begin{array} { c } { { r \cos u } } \\ { { r \sin u } } \\ { { 0 } } \end{array} \right) .
$$

Again, a slightly different, but mathematically equivalent formulation is specified in ICD-GPS-200 (1997). It should be applied whenever full consistency with the ICD is desired.
