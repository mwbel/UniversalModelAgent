$J = - 3 / 2 C _ { 2 0 }$ is the largest geopotential coefficient aside from $C _ { 0 0 }$ , and its value is approximately given by

$$
J \approx f - \frac { \omega ^ { 2 } R ^ { 2 } / 2 } { G M / R } \quad ,
$$

where the flattening $f$ measures the difference between the polar and the equatorial diameter in units of the equatorial diameter, while $M$ , $R$ and $\omega$ are the mass, radius and rotational velocity of the body, respectively. The relation follows from the condition that the sum of the gravitational potential and the centrifugal potential must be constant on the surface of a fluid body, and is derived in standard textbooks on geodesy (e.g. Bomford 1980, Torge 1991). Using appropriate values

$f$ 二 1/298.257  
$G M _ { \oplus }$ = $3 9 8 6 0 0 . 4 4 0 5 \mathrm { k m } ^ { 3 } \mathrm { s } ^ { - 2 }$ $R _ { \oplus }$ = $6 3 7 8 . 1 3 7 \mathrm { k m }$   
$\omega _ { \oplus }$ $0 . 7 2 9 2 1 1 5 { \cdot } 1 0 ^ { - 4 } \mathrm { r a d s } ^ { - 1 }$

for the Earth, one finds that $J { = } 0 . 0 0 1 6 2 ^ { 1 }$ .

The Earth is not an ideal rotational ellipsoid, however, which gives rise to additional tesseral and sectorial geopotential coefficients. Approximate values of the Earth’s low-order potential coefficients can be found in Table 3.2.

Table 3.2. Geopotential coefficients up to degree and order three   

<table><tr><td>Cnm</td><td>m=0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>n=0 1 2 3</td><td>+1.00 0.00 -1.08.10-3 +2.53.10-6</td><td>0.00 0.00 +2.18.10-6</td><td>+1.57.10-6 +3.11:10-7</td><td>1.02.10-7</td></tr><tr><td>Snm</td><td>m=0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>n=0</td><td>0.00</td><td></td><td></td><td></td></tr><tr><td>1</td><td>0.00</td><td>0.00</td><td></td><td></td></tr><tr><td>2</td><td>0.00</td><td>0.00</td><td>-9.03.10-7</td><td></td></tr><tr><td></td><td>0.00</td><td>+2.68.10-7</td><td>-2.12:10-7</td><td>1.98-10-7</td></tr></table>

Aside from the coefficients $S _ { n 0 }$ , which are zero by definition, there are five other coefficients that vanish as a consequence of a special choice of the coordinate system. By choosing the center of mass

$$
\bar { r } = \left( \begin{array} { c } { { \bar { x } } } \\ { { \bar { y } } } \\ { { \bar { z } } } \end{array} \right) = \frac { 1 } { M _ { \oplus } } \int s \rho ( s ) d ^ { 3 } s
$$

as the origin of the coordinate system, one may always observe that the three coefficients

$$
\begin{array} { l } { { { \displaystyle C _ { 1 0 } = \frac { 1 } { M _ { \oplus } R _ { \oplus } } \int s \sin \phi ^ { \prime } \rho ( s ) d ^ { 3 } s = \frac { 1 } { M _ { \oplus } R _ { \oplus } } \int z ^ { \prime } \rho d ^ { 3 } s = \frac { \bar { z } } { R _ { \oplus } } } } } \\ { { { \displaystyle C _ { 1 1 } = \frac { \bar { x } } { R _ { \oplus } } } } } \\ { { { \displaystyle S _ { 1 1 } = \frac { \bar { y } } { R _ { \oplus } } } } } \end{array}
$$

of degree one are equal to zero. Similarly $C _ { 2 1 }$ and $S _ { 2 1 }$ , vanish as long as the $z$ -axis is aligned with the Earth’s main axis of inertia.

# 3.2.3 Gravity Models

Because the internal mass distribution of the Earth is not known, the geopotential coefficients cannot be calculated from the defining equation (3.11), but have to be determined indirectly. Three principal types of measurements and observations are currently used to improve Earth gravity models

Satellite Tracking: From the very beginning of spaceflight, ground-based observations of artificial satellites allowed scientists to determine the Earth’s gravity field through the perturbations seen in the satellite orbits. The first observations mainly used Baker–Nunn wide angle telescopes, which provided pictures of the satellites’ orbital tracks. Subsequently, it turned out that radiometric Doppler tracking led to models superior to those based on optical data. The development of satellite laser ranging (SLR) systems around 1965, and their continuous refinement up to a precision of better than $1 \mathrm { c m }$ , significantly improved the knowledge of the gravity field. In the beginning of the 1990s, the French DORIS system with a Doppler precision of $0 . 4 ~ \mathrm { m m / s }$ , as well as the German PRARE system with a range noise of $7 \mathrm { c m }$ , provided further advanced tracking systems with a high potential for satellite geodesy. Latest enhancements in the gravity field recovery from satellite tracking are due to the inclusion of satellite-to-satellite (SST) tracking. Especially the GPS tracking of satellites, starting with the TOPEX/POSEIDON spacecraft in 1992, may significantly improve the gravity models due to its nearly continuous, high-precision and three-dimensional information. The global coverage of the Earth’s surface with satellite tracks allows the retrieval of global information on the long-wavelength gravity field of the Earth.

Surface Gravimetry: Static spring gravimeters measure the local gravitational acceleration with an accuracy of $1 0 ^ { - 3 } \mathrm { m G a l }$ (Torge 1991) $\mathrm { 1 ~ m G a l = }$ $1 0 ^ { - 5 } \mathrm { m } / \mathrm { s } ^ { 2 } )$ , and thus provide precise local and regional (short-wavelength) information on the gravity field. Relative gravimetry measures the gravity differences from point to point by sensing the inertial reaction of a test mass in response to the change in gravitational acceleration. Since gravimetry is always limited by geographic and political inaccessibility, ship-borne or airborne gravimeters may supplement terrestrial measurements at a reduced accuracy of $0 . 1 { - } 5 ~ \mathrm { m G a l }$ , with a $1 0 { - } 2 0 ~ \mathrm { k m }$ resolution for airborne measurements (Nerem et al. 1995). Even though these data describe the small scale variations of the Earth’s gravitational field very well, a careful inclusion into global gravity models is required due to their inhomogeneous distribution over the whole surface of the Earth.

Altimeter Data: Altimeters measure the height of a satellite above sea level, and can be used for a high-precision determination of the mean sea surface level. Since this is closely related to the equipotential surface, altimeter data provide detailed information about the form of the geoid, which may in turn be used to derive geopotential coefficients. The first satellite altimeter was launched aboard the GEOS 3 satellite in 1975, followed by Seasat in 1978 and TOPEX/POSEIDON in 1992. Satellite altimeter data provide an accuracy better than $1 5 \mathrm { { c m } }$ for a typical resolution of $5 { - } 3 0 \mathrm { k m }$ , which allows a short wavelength resolution of the marine geoid.

The combined use of satellite tracking, terrestrial gravimetry and altimetry measurements for gravity field determination is described in e.g. Rapp (1989).

![](images/dae90477767decd37ea542b8ee0fa936aadcde3cdea33ab297c40c56e707b8f2.jpg)  
Fig. 3.3. Evolution of the complexity of Earth gravity models

In Fig. 3.3 the evolution of the Earth gravity models, as derived from satellite tracking data, is depicted in terms of the characteristic order of the models. The launches of Sputnik 1 in 1957, and of Vanguard 1 in 1959, allowed the first precise determination of $J _ { 2 }$ , and led to the detection of the $J _ { 3 }$ coefficient, which indicates the north-south asymmetry of the geoid. A major improvement in gravity field models was achieved in 1966 by Anderle, using radiometric Doppler data instead of the camera data, that had been previously applied (Nerem et al. 1995). Between 1966 and 1977, the leading models were those derived by Gaposchkin and colleagues at the Smithonian Astrophysical Observatory (SAO).

As a reaction to the military classification of Doppler-based gravity models, NASA’s Goddard Space Flight Center (GSFC) started in 1972 to develop a series of models GEM 1–GEM 10 (Goddard Earth Model) of degree 12–22. Here the oddnumbered models are exclusively based on satellite observations, the corresponding even-numbered models have been derived using additional surface gravimetry data. While the satellite tracking data determine the long-wavelength components of the gravity field of degree $n$ , according to a spatial resolution of $2 \pi R _ { \oplus } / ( 2 n )$ or $\sim 2 0 0 0 0 \mathrm { k m } / n$ , the altimeter and surface gravimetry data allow a much higher resolution at shorter wavelength. An example is the GEM 10C model of degree and order 180, while at the same time the GEM 10B model of degree and order 36 was developed using a less dense grid of surface gravimetry and altimetry data (Lerch et al. 1981). The models GEM-T1 (Marsh et al. 1988) and GEM-T2 (Marsh et al. 1990), both complete to order and degree 36, were entirely based on satellite tracking data from 17 and 31 satellites, respectively. In addition to a small augmentation of satellite tracking data, the GEM-T3 model (Lerch et al. 1994) also applied altimeter data from GEOS 3, Seasat and Geosat, and was complete to degree and order 50.

The oceanographic mission TOPEX/POSEIDON (T/P), with its challenging requirement on the radial orbit accuracy of $1 3 \ \mathrm { c m }$ , led to a cooperation between NASA’s GSFC, the University of Texas Center for Space Research (CSR) and the Centre National d’Études Spatiales (CNES) for gravity field determination. As a result, the final prelaunch T/P gravity model JGM-1 (Joint Gravity Model) of order and degree 70 was issued in 1994 (Nerem et al.). It reiterated the GEM-T3 gravity model solution by processing all of the data with improved models and constants. Its successor JGM-2 (Nerem et al. 1994) was a first postlaunch T/P model, which included a six-month set of T/P SLR and DORIS data. A further improvement in accuracy was obtained with JGM-3 (Tapley et al. 1996), which comprised new T/P SLR, DORIS, as well as for the first time GPS tracking data of T/P. In addition, new LAGEOS 1, LAGEOS 2 and Stella laser tracking, as well as DORIS tracking of the SPOT 2 satellite, were included. A subset of the JGM-3 model (Tapley et al. 1996) is reproduced in Table 3.3.

Although JGM-3 is a very elaborate global gravity model for precision orbit determination, new models are continuously being developed. This is demonstrated by a collaboration of NASA’s Goddard Space Flight Center (GSFC), the National Imagery and Mapping Agency (NIMA) and the Ohio State University (OSU), that published the EGM96S (Earth Gravity Model) of degree and order 70, and the EGM96 model of degree and order 360 (Lemoine et al. 1998). The inclusion of tracking data from 40 satellites, with more continuous data from GPS and TDRSS satellite-to-satellite tracking, contributes to a further improvement of the gravity field model.

Table 3.3. JGM-3 normalized gravitational coefficients up to degree and order 20, in units of $1 0 ^ { - 6 }$ ( $G M _ { \oplus } = 3 9 8 6 0 0 . 4 4 1 5 \mathrm { k m } ^ { 3 } \mathrm { s } ^ { - 2 }$ , $R _ { \oplus } = 6 3 7 8 . 1 3 6 3 0 \mathrm { k m } )$ (Tapley et al. 1996)   

<table><tr><td rowspan=1 colspan=11>nm   Cn.m      Snm   nm  Cn.m     Snm   nm  Cn.m     Snm</td></tr><tr><td rowspan=17 colspan=11>20-484.1653680.00000021-0.0001870.001195222.439261 -1.40026630  0.9571710.000000312.0301370.2481313 2 0.904706-0.61892333  0.7211451.41420440  0.5397770.00000041-0.536244-0.4737724 2 0.350670 0.66257143  0.990869 -0.20098744 -0.1884810.30884850  0.0686590.00000051-0.062727 -0.094195520.652459-0.32333453-0.451837 -0.21495454-0.2951230.049741550.174832-0.66939360 -0.1496720.00000061-0.0761040.026900620.048328 -0.37381663  0.0570210.0088906 4 -0.086228 -0.47140565 -0.267112 -0.53641066  0.009502 -0.23726270  0.0907230.000000710.2802870.094777720.3297600.09319473  0.250502-0.21732074-0.2755411-0.124142750.0016440.01807576 -0.3588430.151778770.0013800.02412980  0.0491180.000000810.0233340.058499820.0800710.065519</td></tr><tr><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=3>312.030137</td></tr><tr><td rowspan=1 colspan=3>33  0.721145</td><td rowspan=1 colspan=3>1.414204</td><td rowspan=2 colspan=3></td><td rowspan=3 colspan=1>0.308848</td></tr><tr><td rowspan=1 colspan=3>40  0.539777</td><td rowspan=1 colspan=3>0.000000</td></tr><tr><td rowspan=3 colspan=3>43  0.990869 -0.20098750  0.068659</td><td rowspan=1 colspan=3>0.990869 -0.200987</td><td rowspan=3 colspan=3>44 -0.18848151-0.062727 -0.094195</td></tr><tr><td rowspan=2 colspan=3>0.000000</td></tr><tr><td rowspan=1 colspan=1>-0.094195</td></tr><tr><td rowspan=1 colspan=3>53-0.451837 -0.214954</td><td rowspan=1 colspan=3>-0.451837 -0.214954</td><td rowspan=1 colspan=3>54-0.2951230.049741</td><td rowspan=2 colspan=1>0.049741</td></tr><tr><td rowspan=1 colspan=3>60 -0.149672</td><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=3>61-0.0761040.026900</td></tr><tr><td rowspan=1 colspan=3>63  0.057021</td><td rowspan=1 colspan=3>0.008890</td><td rowspan=1 colspan=3>6 4 -0.086228 -0.471405</td><td rowspan=1 colspan=1>-0.471405</td></tr><tr><td rowspan=2 colspan=3>66</td><td rowspan=2 colspan=3>0.009502 -0.237262</td><td rowspan=2 colspan=3></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>720.329760</td></tr><tr><td rowspan=1 colspan=3>70  0.090723</td><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=3>710.280287</td><td rowspan=1 colspan=1>0.094777</td><td rowspan=1 colspan=1>72</td></tr><tr><td rowspan=1 colspan=3>73  0.250502</td><td rowspan=1 colspan=3>-0.217320</td><td rowspan=1 colspan=3>74-0.275541</td><td rowspan=1 colspan=1>1-0.124142</td><td rowspan=1 colspan=1>75</td></tr><tr><td rowspan=2 colspan=3>76 -0.358843</td><td rowspan=1 colspan=3>0.151778</td><td rowspan=2 colspan=2>77</td><td rowspan=2 colspan=1>0.001380</td><td rowspan=2 colspan=1>0.024129</td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=2>80</td><td rowspan=1 colspan=1>0.049118</td><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=2>81</td><td rowspan=1 colspan=1>0.023334</td><td rowspan=1 colspan=1>0.058499</td><td rowspan=1 colspan=1>82</td></tr><tr><td rowspan=1 colspan=2>83</td><td rowspan=1 colspan=1>-0.019252-</td><td rowspan=1 colspan=3>-0.086286</td><td rowspan=1 colspan=3>84-0.244358</td><td rowspan=1 colspan=1>0.069857</td><td rowspan=1 colspan=1>85</td></tr><tr><td rowspan=2 colspan=2>8690</td><td rowspan=2 colspan=1>-0.0658590.027385</td><td rowspan=1 colspan=3>0.308921</td><td rowspan=1 colspan=3>870.067263</td><td rowspan=1 colspan=1>0.074813</td><td rowspan=12 colspan=1>88 -0.1239710.120441920.022621-0.03217595-0.016325-0.054272980.187984-0.0030150.000000 10 1 0.083759-0.131554 10 2 -0.093558-0.0514160.016107-0.027892 11 2 0.018430-0.09845250.049828</td></tr><tr><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>910.142230</td><td rowspan=1 colspan=1>0.021910</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>-0.161064-</td><td rowspan=1 colspan=3>-0.074546</td><td rowspan=1 colspan=2>94</td><td rowspan=1 colspan=1>94-0.008202</td><td rowspan=1 colspan=1>0.020068</td><td rowspan=1 colspan=1>95</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0.062833</td><td rowspan=1 colspan=3>0.222677</td><td rowspan=1 colspan=2>97</td><td rowspan=1 colspan=1>-0.118159</td><td rowspan=1 colspan=1>-0.096899</td><td rowspan=1 colspan=1>98</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>-0.047725</td><td rowspan=2 colspan=3>0.096586</td><td rowspan=2 colspan=2></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>100</td><td rowspan=1 colspan=1>0.054130</td><td rowspan=1 colspan=3>0.000000</td><td rowspan=1 colspan=2>101</td><td rowspan=1 colspan=1>0.083759</td><td rowspan=1 colspan=1>-0.131554</td><td rowspan=1 colspan=1>102</td></tr><tr><td rowspan=1 colspan=2>103</td><td rowspan=1 colspan=1>-0.007197</td><td rowspan=1 colspan=3>-0.154180</td><td rowspan=1 colspan=2>104</td><td rowspan=1 colspan=1>-0.084335</td><td rowspan=1 colspan=1>-0.078485</td><td rowspan=1 colspan=1>105</td></tr><tr><td rowspan=1 colspan=2>106</td><td rowspan=1 colspan=1>-0.037419</td><td rowspan=1 colspan=3>-0.079464</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.008208</td><td rowspan=1 colspan=1>-0.003149</td><td rowspan=1 colspan=1>108</td></tr><tr><td rowspan=1 colspan=2>109</td><td rowspan=1 colspan=1>0.125403</td><td rowspan=1 colspan=3>-0.037737</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.100382 -0.023809</td><td rowspan=1 colspan=1>0.100382 -0.023809</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>110</td><td rowspan=1 colspan=1>-0.050161</td><td rowspan=1 colspan=3>0.000000 111</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.016107</td><td rowspan=1 colspan=1>-0.027892</td></tr><tr><td rowspan=1 colspan=2>[113</td><td rowspan=1 colspan=1>-0.030561</td><td rowspan=1 colspan=3>-0.148803</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-0.040024</td><td rowspan=1 colspan=1>-0.063596</td></tr><tr><td rowspan=1 colspan=2>116</td><td rowspan=1 colspan=1>-0.001461</td><td rowspan=1 colspan=3>0.034173</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0.004706</td><td rowspan=1 colspan=1>-0.089777</td><td rowspan=3 colspan=1>0.0245720.046227 -0.0695930.0139860.031048</td></tr><tr><td rowspan=2 colspan=2>119[120</td><td rowspan=2 colspan=1>-0.0314560.036383</td><td rowspan=2 colspan=3>0.042041</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>-0.052129</td><td rowspan=1 colspan=1>-0.018302</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=2>1 -0.054192</td><td rowspan=1 colspan=1>-0.042012</td></tr><tr><td rowspan=1 colspan=2>123</td><td rowspan=1 colspan=1>0.038979</td><td rowspan=1 colspan=3>0.024577</td><td rowspan=1 colspan=3>124-0.068420</td><td rowspan=1 colspan=1>0.002954125</td><td rowspan=1 colspan=1>0.0311070.007639</td></tr><tr><td rowspan=1 colspan=2>126</td><td rowspan=1 colspan=1>0.003324</td><td rowspan=1 colspan=3>0.039369</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=2>127 -0.018603</td><td rowspan=1 colspan=1>0.035571</td><td rowspan=4 colspan=1>0.035571 12 8 -0.0257030.0166670.011321 -0.0063440.0398771320.056039 -0.0626990.065846</td></tr><tr><td rowspan=1 colspan=2>129</td><td rowspan=1 colspan=1>0.041793</td><td rowspan=1 colspan=3>0.025325</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=2>12 10 -0.006169</td><td rowspan=1 colspan=1>0.030986</td></tr><tr><td rowspan=1 colspan=3>1212 -0.002349 -0.010959130  0.039946</td><td rowspan=1 colspan=3>-0.002349 -0.0109590.000000</td><td rowspan=1 colspan=3>）131-0.052967</td><td rowspan=1 colspan=1>0.039877132</td></tr><tr><td rowspan=1 colspan=2>133</td><td rowspan=1 colspan=1>-0.021817</td><td rowspan=1 colspan=3>0.098209</td><td rowspan=1 colspan=3>134-0.001471</td><td rowspan=1 colspan=1>-0.012614</td></tr><tr><td rowspan=1 colspan=2>136</td><td rowspan=2 colspan=9>136 -0.035312 -0.0060581370.002706-0.007711138 -0.009887 -0.009729139  0.0247540.04535913100.040892 -0.037099 13 11 -0.044739 -0.0048331312 -0.0314100.088106 13 13 -0.0612110.068409</td></tr><tr><td rowspan=1 colspan=3>139  0.024754</td><td rowspan=1 colspan=3>0.045359</td><td rowspan=1 colspan=3>1310</td><td rowspan=1 colspan=1>-0.037099</td></tr></table>

Table 3.3. (continued)   

<table><tr><td rowspan=1 colspan=11>nm  Cn.m      Sn.m   nm  Cn,m      Sn.m   nm  Cn.m     Snm</td></tr><tr><td rowspan=1 colspan=11>140-0.0218040.000000141-0.0190240.02747214 2 -0.036979 -0.002989</td></tr><tr><td rowspan=1 colspan=3>1430.036809</td><td rowspan=1 colspan=1>0.020313</td><td rowspan=1 colspan=2>144</td><td rowspan=1 colspan=1>0.001712</td><td rowspan=1 colspan=1>2-0.020688</td><td rowspan=1 colspan=3>1450.029900-0.016858</td></tr><tr><td rowspan=1 colspan=3>146 -0.019401</td><td rowspan=1 colspan=1>0.002413</td><td rowspan=1 colspan=2>147</td><td rowspan=1 colspan=1>0.036851</td><td rowspan=1 colspan=1>-0.004222</td><td rowspan=1 colspan=3>148 -0.034867 -0.014888</td></tr><tr><td rowspan=1 colspan=3>1490.032377</td><td rowspan=1 colspan=1>0.028698</td><td rowspan=1 colspan=2>14 10</td><td rowspan=1 colspan=1>0.038839</td><td rowspan=1 colspan=1>9-0.001466</td><td rowspan=1 colspan=3>14110.015357 -0.039039</td></tr><tr><td rowspan=1 colspan=3>14 120.008505 -0.030922</td><td rowspan=1 colspan=1>0.008505 -0.030922</td><td rowspan=1 colspan=2>14 13</td><td rowspan=1 colspan=1>0.032167</td><td rowspan=1 colspan=1>0.045200</td><td rowspan=1 colspan=3>14 14 -0.051783 -0.005014</td></tr><tr><td rowspan=2 colspan=3>1500.003166</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>0.008173</td><td rowspan=2 colspan=3>152 -0.021746-0.031733</td></tr><tr><td rowspan=1 colspan=1>0.000000</td><td rowspan=1 colspan=2>151</td><td rowspan=1 colspan=1>0.012019</td></tr><tr><td rowspan=1 colspan=2>153</td><td rowspan=1 colspan=1>0.052403</td><td rowspan=1 colspan=1>0.015160</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>154-0.042163</td><td rowspan=1 colspan=1>0.007827</td><td rowspan=1 colspan=2>1550.013451</td><td rowspan=1 colspan=1>0.008982</td></tr><tr><td rowspan=1 colspan=2>156</td><td rowspan=1 colspan=1>0.033463</td><td rowspan=1 colspan=1>-0.037753</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0.059913</td><td rowspan=1 colspan=1>0.006056</td><td rowspan=1 colspan=1>158</td><td rowspan=1 colspan=1>158 -0.031990</td><td rowspan=1 colspan=1>0.022271</td></tr><tr><td rowspan=1 colspan=2>159</td><td rowspan=1 colspan=1>0.013027</td><td rowspan=1 colspan=1>0.037876</td><td rowspan=1 colspan=2>15 10</td><td rowspan=1 colspan=1>0.010311</td><td rowspan=1 colspan=1>0.014956</td><td rowspan=1 colspan=1>1511</td><td rowspan=1 colspan=1>15 11 -0.000952</td><td rowspan=1 colspan=1>0.018716</td></tr><tr><td rowspan=1 colspan=2>1512</td><td rowspan=1 colspan=1>15 12 -0.032729</td><td rowspan=1 colspan=1>0.015720</td><td rowspan=1 colspan=2>1513</td><td rowspan=1 colspan=1>-0.028289</td><td rowspan=1 colspan=1>-0.004294</td><td rowspan=1 colspan=1>1514</td><td rowspan=1 colspan=1>0.005305</td><td rowspan=1 colspan=1>-0.024443</td></tr><tr><td rowspan=1 colspan=2>15 15</td><td rowspan=1 colspan=1>-0.019228</td><td rowspan=1 colspan=1>-0.004704</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>160</td><td rowspan=1 colspan=1>160-0.005430</td><td rowspan=1 colspan=1>0.000000</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.027534</td><td rowspan=1 colspan=1>0.033708</td><td rowspan=1 colspan=1>162</td><td rowspan=1 colspan=1>162 -0.022395</td><td rowspan=1 colspan=1>0.026207</td></tr><tr><td rowspan=1 colspan=2>163</td><td rowspan=1 colspan=1>-0.035101</td><td rowspan=1 colspan=1>-0.023242</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.041219</td><td rowspan=1 colspan=1>0.046057</td><td rowspan=1 colspan=1>165</td><td rowspan=1 colspan=1>-0.013495</td><td rowspan=1 colspan=1>-0.001679</td></tr><tr><td rowspan=1 colspan=2>166</td><td rowspan=1 colspan=1>0.014321</td><td rowspan=1 colspan=1>-0.034445</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>167 -0.007813</td><td rowspan=1 colspan=1>3-0.008510</td><td rowspan=1 colspan=1>168</td><td rowspan=1 colspan=1>168 -0.021538</td><td rowspan=1 colspan=1>80.005248</td></tr><tr><td rowspan=1 colspan=2>169</td><td rowspan=1 colspan=1>-0.022777</td><td rowspan=1 colspan=1>-0.038924</td><td rowspan=1 colspan=2>1610</td><td rowspan=1 colspan=1>16 10 -0.012129</td><td rowspan=1 colspan=1>0.012065</td><td rowspan=1 colspan=1>16 11</td><td rowspan=1 colspan=1>0.019266-0.002975</td><td rowspan=1 colspan=1>0.019266-0.002975</td></tr><tr><td rowspan=1 colspan=2>1612(</td><td rowspan=1 colspan=1>0.019698</td><td rowspan=1 colspan=1>0.006915</td><td rowspan=1 colspan=1>16 13</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>0.013837</td><td rowspan=1 colspan=1>0.000994</td><td rowspan=1 colspan=1>16 14</td><td rowspan=1 colspan=1>-0.019126</td><td rowspan=1 colspan=1>-0.038862</td></tr><tr><td rowspan=1 colspan=2>16 15</td><td rowspan=1 colspan=1>-0.014461</td><td rowspan=1 colspan=1>-0.032699</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>16 16 -0.037529</td><td rowspan=1 colspan=1>0.003591</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0.018108</td><td rowspan=1 colspan=1>0.000000</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1 -0.026389</td><td rowspan=1 colspan=1>）-0.029853</td><td rowspan=1 colspan=1>172</td><td rowspan=1 colspan=1>172 -0.017379</td><td rowspan=1 colspan=1>0.009197</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0.007423</td><td rowspan=1 colspan=1>0.008195</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.007520</td><td rowspan=1 colspan=1>0.023382</td><td rowspan=1 colspan=1>175</td><td rowspan=1 colspan=1>17 5-0.017058</td><td rowspan=1 colspan=1>0.005353</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>-0.013467</td><td rowspan=1 colspan=1>-0.028275</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0.024011</td><td rowspan=1 colspan=1>-0.005884</td><td rowspan=1 colspan=1>178</td><td rowspan=1 colspan=1>1780.037625</td><td rowspan=1 colspan=1>0.003761</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0.003291 -0.028586</td><td rowspan=1 colspan=1>0.003291 -0.028586</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>17 10 -0.004304</td><td rowspan=1 colspan=1>0.018038</td><td rowspan=1 colspan=1>1711</td><td rowspan=1 colspan=1>17 11 -0.015726</td><td rowspan=1 colspan=1>0.011021</td></tr><tr><td rowspan=1 colspan=1>17 12</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>0.028689</td><td rowspan=1 colspan=1>0.020744</td><td rowspan=1 colspan=2>17 13</td><td rowspan=1 colspan=1>0.016603</td><td rowspan=1 colspan=1>0.020305</td><td rowspan=1 colspan=1>17 14</td><td rowspan=1 colspan=1>17 14 -0.014061</td><td rowspan=1 colspan=1>0.011376</td></tr><tr><td rowspan=1 colspan=1>17 15</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.005332</td><td rowspan=1 colspan=1>0.005387</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>17 16 -0.030061</td><td rowspan=1 colspan=1>0.003724</td><td rowspan=1 colspan=1>17 17</td><td rowspan=1 colspan=1>-0.034064</td><td rowspan=2 colspan=1>-0.019733</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0.007269</td><td rowspan=1 colspan=1>0.000000</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.004210</td><td rowspan=1 colspan=1>-0.039076</td><td rowspan=1 colspan=1>182</td><td rowspan=1 colspan=1>0.012828</td><td rowspan=1 colspan=1>0.013586</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>183-0.003760</td><td rowspan=1 colspan=1>-0.003109</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.053092</td><td rowspan=1 colspan=1>0.001460</td><td rowspan=1 colspan=1>185</td><td rowspan=1 colspan=1>0.007314</td><td rowspan=1 colspan=1>0.024650</td></tr><tr><td rowspan=1 colspan=1>186</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0.013378</td><td rowspan=1 colspan=1>-0.015661</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0.006529</td><td rowspan=1 colspan=1>0.006280</td><td rowspan=1 colspan=1>188</td><td rowspan=1 colspan=1>0.031066</td><td rowspan=1 colspan=1>0.002470</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>18 9-0.019183</td><td rowspan=1 colspan=1>0.036144</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.005566</td><td rowspan=1 colspan=1>-0.004595</td><td rowspan=1 colspan=1>1811</td><td rowspan=1 colspan=1>-0.007643</td><td rowspan=1 colspan=1>0.002117</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>-0.029603</td><td rowspan=1 colspan=1>-0.016193</td><td rowspan=1 colspan=2>1813</td><td rowspan=1 colspan=1>-0.006380</td><td rowspan=1 colspan=1>）-0.034980</td><td rowspan=1 colspan=1>1814</td><td rowspan=1 colspan=1>4-0.008003</td><td rowspan=1 colspan=1>-0.013078</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>-0.040536</td><td rowspan=1 colspan=1>-0.020249</td><td rowspan=1 colspan=2>18 16</td><td rowspan=1 colspan=1>0.010671</td><td rowspan=1 colspan=1>0.006965</td><td rowspan=1 colspan=1>1817</td><td rowspan=1 colspan=1>0.003600</td><td rowspan=1 colspan=1>0.004510</td></tr><tr><td rowspan=3 colspan=2>18 18</td><td rowspan=3 colspan=1>190-0.003519</td><td rowspan=1 colspan=1>-0.010810</td><td rowspan=2 colspan=2></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=2 colspan=1>0.000000</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1 -0.006968</td><td rowspan=1 colspan=1>0.000158</td><td rowspan=1 colspan=1>192</td><td rowspan=1 colspan=1>0.031435</td><td rowspan=1 colspan=1>-0.004330</td></tr><tr><td rowspan=1 colspan=2>193</td><td rowspan=1 colspan=1>193-0.009900</td><td rowspan=1 colspan=1>-0.000988</td><td rowspan=1 colspan=2>194</td><td rowspan=1 colspan=1>0.015827</td><td rowspan=1 colspan=1>-0.005662</td><td rowspan=1 colspan=1>195</td><td rowspan=1 colspan=1>0.012058</td><td rowspan=1 colspan=1>0.027204</td></tr><tr><td rowspan=1 colspan=2>196</td><td rowspan=1 colspan=1>196-0.002385</td><td rowspan=1 colspan=1>0.017952</td><td rowspan=1 colspan=2>197</td><td rowspan=1 colspan=1>0.007368</td><td rowspan=1 colspan=1>3-0.008665</td><td rowspan=1 colspan=1>198</td><td rowspan=1 colspan=1>0.031052 -0.010463</td><td rowspan=1 colspan=1>0.031052 -0.010463</td></tr><tr><td rowspan=1 colspan=2>199</td><td rowspan=1 colspan=1>0.003031</td><td rowspan=1 colspan=1>0.006452</td><td rowspan=1 colspan=2>1910</td><td rowspan=1 colspan=1>19 10 -0.033378</td><td rowspan=1 colspan=1>-0.007090</td><td rowspan=1 colspan=1>19 11</td><td rowspan=1 colspan=1>0.016081</td><td rowspan=1 colspan=1>0.011000</td></tr><tr><td rowspan=1 colspan=2>1912</td><td rowspan=1 colspan=1>19 12 -0.002989</td><td rowspan=1 colspan=1>0.009310</td><td rowspan=1 colspan=2>1913</td><td rowspan=1 colspan=1>-0.007447</td><td rowspan=1 colspan=1>-0.028398</td><td rowspan=1 colspan=1>1914</td><td rowspan=1 colspan=1>-0.004529</td><td rowspan=1 colspan=1>-0.013114</td></tr><tr><td rowspan=1 colspan=2>19 15</td><td rowspan=1 colspan=1>-0.017839</td><td rowspan=1 colspan=1>-0.014106</td><td rowspan=1 colspan=2>1916</td><td rowspan=1 colspan=1>-0.021421</td><td rowspan=1 colspan=1>-0.006958</td><td rowspan=1 colspan=1>1917</td><td rowspan=1 colspan=1>0.029106</td><td rowspan=1 colspan=1>-0.015153</td></tr><tr><td rowspan=1 colspan=2>19 18</td><td rowspan=1 colspan=1>0.034714 -0.009439</td><td rowspan=1 colspan=1>0.034714 -0.009439</td><td rowspan=1 colspan=2>19 19</td><td rowspan=1 colspan=1>19 19 -0.002371</td><td rowspan=1 colspan=1>0.004780</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=2 colspan=2>200</td><td rowspan=2 colspan=1>0.018790</td><td rowspan=2 colspan=1>0.000000</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>201</td><td rowspan=1 colspan=1>0.008348</td><td rowspan=1 colspan=1>0.006245</td><td rowspan=1 colspan=1>5202</td><td rowspan=1 colspan=1>0.020030</td><td rowspan=1 colspan=1>0.014885</td></tr><tr><td rowspan=1 colspan=2>203</td><td rowspan=1 colspan=1>-0.005935</td><td rowspan=1 colspan=1>0.035571</td><td rowspan=1 colspan=2>204</td><td rowspan=1 colspan=1>0.005457</td><td rowspan=1 colspan=1>-0.022410</td><td rowspan=1 colspan=1>205</td><td rowspan=1 colspan=1>-0.011452</td><td rowspan=1 colspan=1>-0.006935</td></tr><tr><td rowspan=1 colspan=2>206</td><td rowspan=1 colspan=1>0.011565</td><td rowspan=1 colspan=1>-0.000423</td><td rowspan=1 colspan=2>207</td><td rowspan=1 colspan=1>-0.020302</td><td rowspan=1 colspan=1>-0.000130</td><td rowspan=1 colspan=1>208</td><td rowspan=1 colspan=1>0.004922</td><td rowspan=1 colspan=1>0.004067</td></tr><tr><td rowspan=1 colspan=2>209</td><td rowspan=1 colspan=1>0.018044</td><td rowspan=1 colspan=1>0.018044 -0.005865</td><td rowspan=1 colspan=2>2010</td><td rowspan=1 colspan=1>20 10-0.032549</td><td rowspan=1 colspan=1>-0.005760</td><td rowspan=1 colspan=1>2011</td><td rowspan=1 colspan=1>0.014563 -0.018930</td><td rowspan=1 colspan=1>0.014563 -0.018930</td></tr><tr><td rowspan=1 colspan=2>2012</td><td rowspan=1 colspan=1>20 12 -0.006409</td><td rowspan=1 colspan=1>0.018154</td><td rowspan=1 colspan=2>2013</td><td rowspan=1 colspan=1>0.027324</td><td rowspan=1 colspan=1>0.007033</td><td rowspan=1 colspan=1>2014</td><td rowspan=1 colspan=1>0.011894 -0.014472</td><td rowspan=1 colspan=1>0.011894 -0.014472</td></tr><tr><td rowspan=1 colspan=2>2015</td><td rowspan=1 colspan=1>-0.025833</td><td rowspan=1 colspan=1>-0.000766</td><td rowspan=1 colspan=2>20 16</td><td rowspan=1 colspan=1>-0.012064</td><td rowspan=1 colspan=1>0.000330</td><td rowspan=1 colspan=1>2017</td><td rowspan=1 colspan=1>0.004435 -0.013703</td><td rowspan=1 colspan=1>0.004435 -0.013703</td></tr><tr><td rowspan=1 colspan=2>2018</td><td rowspan=1 colspan=1>0.014917</td><td rowspan=1 colspan=1>-0.000984</td><td rowspan=1 colspan=2>2019</td><td rowspan=1 colspan=1>-0.002963</td><td rowspan=1 colspan=1>0.010960</td><td rowspan=1 colspan=2>）2020 0.004045-0.012347</td><td rowspan=1 colspan=1>0.004045-0.012347</td></tr></table>

# 3.2.4 Recursions

In the computation of the Earth’s gravity potential at a given point, several recurrence relations for the evaluation of Legendre polynomials can be used. Starting with $P _ { 0 0 } = 1$ , all polynomials $P _ { m m }$ up to the desired degree and order are first calculated from

$$
P _ { m m } ( u ) = ( 2 m - 1 ) ( 1 - u ^ { 2 } ) ^ { 1 / 2 } P _ { m - 1 , m - 1 } ,
$$

where $u$ and $( 1 - u ^ { 2 } ) ^ { 1 / 2 }$ stand for $\sin \phi$ and $\cos \phi$ , respectively. With these results the remaining values may be obtained from

$$
P _ { m + 1 , m } ( u ) = ( 2 m + 1 ) u P _ { m m } ( u )
$$

and from the recursion

$$
P _ { n m } ( u ) = \frac { 1 } { n - m } ( ( 2 n - 1 ) u P _ { n - 1 , m } ( u ) - ( n + m - 1 ) P _ { n - 2 , m } ( u ) )
$$

for $n > m + 1$

The above relations for the Legendre polynomials may, according to Cunningham (1970), be favorably combined with the addition theorems

$$
\begin{array} { r c l } { { \cos ( ( m + 1 ) \lambda ) } } & { { = } } & { { \cos ( m \lambda ) \cos ( \lambda ) - \sin ( m \lambda ) \sin ( \lambda ) } } \\ { { } } & { { } } & { { } } \\ { { \sin ( ( m + 1 ) \lambda ) } } & { { = } } & { { \sin ( m \lambda ) \cos ( \lambda ) + \cos ( m \lambda ) \sin ( \lambda ) } } \end{array}
$$

for the angular functions of the longitude-dependent terms into a single recursion. This allows an efficient computation of the geopotential and the resulting acceleration as a function of the Cartesian coordinates $( x , y , z )$ of the satellite. Defining

$$
\begin{array} { l c r } { { V _ { n m } = \left( \displaystyle { \frac { R _ { \oplus } } { r } } \right) ^ { n + 1 } \cdot P _ { n m } ( \sin \phi ) \cdot \cos m \lambda } } \\ { { { } } } \\ { { W _ { n m } = \left( \displaystyle { \frac { R _ { \oplus } } { r } } \right) ^ { n + 1 } \cdot P _ { n m } ( \sin \phi ) \cdot \sin m \lambda } } \end{array}
$$

the gravity potential may be written as

$$
U = { \frac { G M _ { \oplus } } { R _ { \oplus } } } \sum _ { n = 0 } ^ { \infty } \sum _ { m = 0 } ^ { n } ( C _ { n m } V _ { n m } + S _ { n m } W _ { n m } ) ~ .
$$

The $V _ { n m }$ and $W _ { n m }$ satisfy the recurrence relations

$$
\begin{array} { r c l } { { V _ { m m } } } & { { = } } & { { ( 2 m - 1 ) \left\{ \displaystyle \frac { x R _ { \oplus } } { r ^ { 2 } } V _ { m - 1 , m - 1 } - \displaystyle \frac { y R _ { \oplus } } { r ^ { 2 } } V _ { m - 1 , m - 1 } \right\} } } \\ { { } } & { { } } & { { } } \\ { { W _ { m m } } } & { { = } } & { { ( 2 m - 1 ) \left\{ \displaystyle \frac { x R _ { \oplus } } { r ^ { 2 } } W _ { m - 1 , m - 1 } + \displaystyle \frac { y R _ { \oplus } } { r ^ { 2 } } V _ { m - 1 , m - 1 } \right\} } } \end{array}
$$

and

$$
\begin{array} { r c l } { { V _ { n m } } } & { { = } } & { { \displaystyle \left( \frac { 2 n - 1 } { n - m } \right) \cdot \frac { z R _ { \oplus } } { r ^ { 2 } } \cdot V _ { n - 1 , m } - \left( \frac { n + m - 1 } { n - m } \right) \cdot \frac { R _ { \oplus } ^ { 2 } } { r ^ { 2 } } \cdot V _ { n - 2 , m } } } \\ { { W _ { n m } } } & { { = } } & { { \displaystyle \left( \frac { 2 n - 1 } { n - m } \right) \cdot \frac { z R _ { \oplus } } { r ^ { 2 } } \cdot W _ { n - 1 , m } - \left( \frac { n + m - 1 } { n - m } \right) \cdot \frac { R _ { \oplus } ^ { 2 } } { r ^ { 2 } } \cdot W _ { n - 2 , m } } } \end{array}
$$

which follow immediately from the above relations for the Legendre polynomials and the trigonometric functions. The second set of equations holds for $n = m + 1$ , too, if $V _ { m - 1 , m }$ and $W _ { m - 1 , m }$ are set to zero. Furthermore,

$$
V _ { 0 0 } = \frac { R _ { \oplus } } { r } \mathrm { a n d } W _ { 0 0 } = 0
$$

are known.

In order to calculate all $V _ { n m }$ and $W _ { n m }$ $0 \leq m \leq n \leq n \sin \alpha \mathrm { { m a x } } ,$ ), one first obtains the zonal terms $V _ { n 0 }$ by using (3.30) with $m = 0$ . The corresponding values $W _ { n 0 }$ are all identical to zero. Now, (3.29) yields the first tesseral terms $V _ { 1 1 }$ and $W _ { 1 1 }$ from $V _ { 0 0 }$ , which allows all $V _ { n 1 }$ $1 \leq n \leq n _ { \mathrm { m a x } } $ to be determined. Thus the recursions are used according to the following scheme:

$$
\begin{array} { c c c c c c c c c c c c c c c } { V _ { 0 0 } , W _ { 0 0 } } & & & & & & & & & & & & & & \\ & { \downarrow } & & & & & & & & & & & & & \\ & { V _ { 1 0 } , W _ { 1 0 } } & & & & & & & & & & & & & \\ & & & { V _ { 1 1 } , W _ { 1 1 } } & & & & & & & & & & & \\ { \downarrow } & & & { \downarrow } & & & & & & & & & & & \\ { V _ { 2 0 } , W _ { 2 0 } } & & & { V _ { 2 1 } , W _ { 2 1 } } & & & { V _ { 2 2 } , W _ { 2 2 } } & & & & & & \\ { \downarrow } & & & { \downarrow } & & & { \downarrow } & & & & & & \\ { \vdots } & & { \vdots } & & { \vdots } & & & { \ddots } & & & & & \\ & & { \downarrow } & & & & { \downarrow } & & & & & { \ddots } & & \\ { V _ { n 0 } , W _ { n 0 } } & & { V _ { n 1 } , W _ { n 1 } } & & & { V _ { n 2 } , W _ { n 2 } } & & & { \ldots } & & & & { V _ { n n } , W _ { n n } } \end{array}
$$

Finally it should be noted that many other recursion formulas exist for the calculation of Legendre polynomials, and may be looked up in standard text books or mathematical tables (Abramowitz & Stegun 1965). Not all of these are, however, equally well suited for the numerical computation, especially if high-order polynomials are required (cf. Lundberg 1985). The recursions presented here are stable, which means that small numerical errors in the computation of low-order terms do not lead to meaningless results for high orders. As was shown by Deuflhard (1976), recurrence relations for $P _ { n m }$ that keep either order $( m )$ or degree $( n )$ constant are more stable than others. This is the case for (3.25) and applies equally well to the formulas for $V _ { n m }$ and $W _ { n m }$ . As a rule of thumb, one can expect to loose 2–3, 4–5, and 5–6 digits when evaluating these functions up to orders 15, 50, and 100, respectively.

# 3.2.5 Acceleration

The acceleration $\ddot { r }$ , which is equal to the gradient of $U$ , may be directly calculated from the $V _ { n m }$ and $W _ { n m }$ as

$$
\ddot { x } = \sum _ { n , m } \ddot { x } _ { n m } , \ddot { y } = \sum _ { n , m } \ddot { y } _ { n m } , \ddot { z } = \sum _ { n , m } \ddot { z } _ { n m }
$$

with the partial accelerations

$$
\begin{array} { r c l } { \check { S } _ { \mathrm { i n t } } } & { \stackrel { \mathrm { ( i n - 0 ) } } { = } } & { \displaystyle \frac { G ^ { 2 } M } { R _ { 0 } ^ { 2 } } \{ - \mathcal { L } _ { 0 } \nu _ { k + 1 } \} , } \\ & { \stackrel { \mathrm { ( i n - 0 ) } } { = } } &  \displaystyle \frac { G ^ { 2 } M } { R _ { 0 } ^ { 2 } } \frac { 1 } { 2 } \cdot \{ ( - \mathcal { L } _ { 0 } \nu _ { k + 1 } , \mathrm { [ w _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } , ~ R _ { k + 1 } ,   } \\ & & {   \quad \quad + \frac { ( 1 ) } { ( \mu - m ) ! } \lambda _ { 1 } , \frac { 1 } { ( \mu - m ) ! } , \frac { 1 } { ( \mu - m ) ! } , \frac { 1 } { ( \mu - m ) ! } , \frac { 1 } { ( \mu - m ) ! } , \frac { 1 } { ( \mu - m ) ! }   } \\ & { \displaystyle  \check { S } _ { \mathrm { i n t } } } & { \stackrel { \mathrm { ( i n - 0 ) } } { = } } & { \displaystyle \frac { G ^ { 3 } M } { R _ { 0 } ^ { 2 } } \cdot \{ \begin{array} { c } { \mathcal { L } _ { 0 } \nu _ { k + 1 } , \hfill \mathrm { [ } \mathcal { L } _ { 0 } , \hfill \mathrm { o u t } _ { k + 1 } , \hfill \mathrm { ] } } \\ { \mathcal { L } _ { 0 } \sim \mathcal { L } _ { 0 } , \hfill \mathrm { [ } \mathcal { L } _ { 0 } , \hfill \mathrm { f i } , \mathrm { o u t } _ { k + 1 } , \hfill \mathrm { ] } } \end{array}  } \\ &  \displaystyle  \begin{array} { c }  \mathrm { ~ o u t ~ } R _ { 0 } ^ { 2 } , \hfill \mathrm { [ } \mathcal { L } _ { 0 } , \hfill \mathrm \end{array} \end{array}
$$

$$
\ddot { z } _ { n m } \quad = \quad \ \frac { G M } { R _ { \oplus } ^ { 2 } } \cdot \left\{ ( n - m + 1 ) \cdot ( - C _ { n m } V _ { n + 1 , m } - S _ { n m } W _ { n + 1 , m } ) \right\} \quad .
$$

The derivation of these equations is given in Cunningham (1970), together with similar relations for the second-order partial derivatives of the potential. It is noted that the $V _ { \nu \mu }$ and $W _ { \nu \mu }$ terms are required up to degree and order $n { \mathrel { + { 1 } } }$ if the partial accelerations due to geopotential coefficients up to $C _ { n n }$ and $S _ { n n }$ are to be calculated.

The formulas given so far yield the acceleration $\pmb { \ddot { r } } = ( \ddot { x } , \ddot { y } , \ddot { z } )$ in an Earth-fixed coordinate system as a function of the Earth-fixed position vector $\boldsymbol { r } = ( x , y , z )$ . Some coordinate transformations are therefore required to obtain the acceleration in an inertial or Newtonian coordinate system which is consistent with the equation of motion (3.1). Using indices $\mathrm { e f }$ and $\mathrm { s f }$ to distinguish Earth-fixed from space-fixed coordinates, one has

$$
\pmb { r } _ { \mathrm { e f } } = \pmb { U } ( t ) \cdot \pmb { r } _ { \mathrm { s f } } \quad \mathrm { a n d } \quad \pmb { \ddot { r } } _ { \mathrm { s f } } = \pmb { U } ^ { T } ( t ) \cdot \pmb { \ddot { r } } _ { \mathrm { e f } } \quad ,
$$

where $U ( t )$ is a time-dependent matrix that describes the Earth’s rotation. The rigorous computation of $U ( t )$ , furthermore, has to account for the long and shortterm perturbations of the Earth’s axis, known as precession and nutation, that are described in detail in Chap. 5.

# 3.3 Sun and Moon

# 3.3.1 Perturbing Acceleration

According to Newton’s law of gravity, the acceleration of a satellite by a point mass $M$ is given by

$$
{ \ddot { r } } = G M \cdot { \frac { s - r } { | s - r | ^ { 3 } } } ,
$$

where $r$ and $\pmb { S }$ are the geocentric coordinates of the satellite and of $M$ , respectively. Some care is required, however, before this expression can be used for describing the satellite’s motion with respect to the center of the Earth. The value of $\ddot { r }$ in (3.35) refers to an inertial or Newtonian coordinate system in which the Earth is not at rest, but is itself subject to an acceleration

$$
{ \ddot { r } } = G M \cdot { \frac { s } { | s | ^ { 3 } } }
$$

due to $M$ . Both values have to be subtracted to obtain the second derivative

$$
{ \ddot { r } } = G M \cdot \left( { \frac { s - r } { | s - r | ^ { 3 } } } - { \frac { s } { | s | ^ { 3 } } } \right)
$$

of the satellite’s Earth-centered position vector.

Since both the Sun and the Moon are much further away from the Earth than most of the satellites, one may derive a simple approximation from (3.37) which gives an insight into the structure of the acceleration in an Earth-centered reference frame, and is often used for analytical perturbation theories. For this purpose the denominator of (3.35) is expanded as

$$
\frac { 1 } { | s - r | ^ { 3 } } = \frac { 1 } { s ^ { 2 } + r ^ { 2 } - 2 s r ( e _ { s } e _ { r } ) } ^ { 3 / 2 } \approx \frac { 1 } { s ^ { 3 } } \left( 1 + 3 \frac { r } { s } ( e _ { s } e _ { r } ) \right) ,
$$

with the unit vectors

$$
e _ { s } = { \frac { s } { s } } \quad { \mathrm { a n d } } \quad e _ { r } = { \frac { r } { r } }
$$

pointing in the direction of $\pmb { S }$ and $r$ . This yields the approximate relation

$$
\ddot { r } \approx \frac { G M r } { s ^ { 3 } } \cdot ( - e _ { r } + 3 e _ { s } ( e _ { s } e _ { r } ) )
$$

which reduces to

$$
\ddot { r } \approx \frac { 2 G M } { s ^ { 3 } } r
$$

for $\pm e _ { r } = \pm e _ { s }$ , and to

$$
\ddot { r } \approx - \frac { G M } { s ^ { 3 } } r
$$

![](images/059a77ec7701f47961d80ee84c4767a1d72bb0e0cddf31bfae34db6841294b13.jpg)  
Fig. 3.4. Tidal forces due to the gravitational attraction of a distant point-like mass

for $\begin{array} { r } { e _ { r } e _ { s } = 0 . } \end{array}$ Therefore the satellite experiences an acceleration away from the Earth whenever it is collinear with the Earth and the perturbing body, but is attracted towards the Earth whenever it is perpendicular to this line (cf. Fig. 3.4).

One may further see from (3.40) that the acceleration increases linearly with the satellite’s distance $r$ from the center of the Earth, while it decreases with the third power of the distance of the perturbing body.

# 3.3.2 Low-Precision Solar and Lunar Coordinates

Since the forces exerted by the Sun and the Moon are much smaller than the central attraction of the Earth, it is not necessary to know their coordinates to the highest precision when calculating the perturbing acceleration acting on a satellite. For many purposes it is even sufficient to use simple equations for the solar and lunar coordinates that are accurate to about $0 . 1 \mathrm { - } 1 \%$ and follow from more advanced analytical theories for the motion of the Sun and the Moon (see e.g. van Flandern & Pulkkinen 1979, Montenbruck 1989, Montenbruck & Pfleger 2000 for further references).

Geocentric solar coordinates can easily be obtained from the assumption of an unperturbed motion of the Earth around the Sun. Appropriate mean orbital elements, which approximate the Sun’s elliptic orbit with respect to the Earth and the ecliptic for some decades around the year 2000, are given by

$$
\begin{array} { l c l } { a } & { = } & { 1 4 9 6 0 0 0 0 0 0 \mathrm { k m } } \\ { e } & { = } & { 0 . 0 1 6 7 0 9 } \\ { i } & { = } & { 0 . 0 0 0 0 } \\ { \Omega + \omega } & { = } & { 2 8 2 . 9 4 0 0 } \\ { M } & { = } & { 3 5 7 . 5 2 5 6 + 3 5 9 9 9 \% 0 4 9 \cdot T } \end{array}
$$

where

$$
T = ( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 . 0
$$

is the number of Julian centuries since 1.5 January 2000 (J2000), and JD is the Julian Date (cf. Annex A.1). The position coordinates may be found from these elements using the equations for Keplerian orbits that were derived in the previous chapter. Due to the small eccentricity and inclination, the use of some simple series expansions is, however, recommended to speed up the calculation without loss of accuracy. This results in the expressions

$$
\begin{array} { l l l } { { \lambda _ { \odot } } } & { { = } } & { { \Omega + \omega + M + 6 8 9 2 ^ { \prime \prime } \sin M + 7 2 ^ { \prime \prime } \sin 2 M } } \\ { { } } & { { } } & { { } } \\ { { r _ { \odot } } } & { { = } } & { { ( 1 4 9 . 6 1 9 - 2 . 4 9 9 \cos M - 0 . 0 2 1 \cos 2 M ) \cdot 1 0 ^ { 6 } \mathrm { k m } } } \end{array}
$$

for the Sun’s ecliptic longitude $\lambda _ { \odot }$ and distance $r _ { \odot }$ , whereas the ecliptic latitude $\beta _ { \odot }$ vanishes within an accuracy of $1 ^ { \prime }$ (cf. Montenbruck 1989).

These values may be converted to Cartesian coordinates referring to the equator by applying an appropriate rotation

$$
\begin{array} { r } { r _ { \odot } = { \bf R } _ { x } ( - \varepsilon ) \left( \begin{array} { l } { r _ { \odot } \cos \lambda _ { \odot } \cos \beta _ { \odot } } \\ { r _ { \odot } \sin \lambda _ { \odot } \cos \beta _ { \odot } } \\ { r _ { \odot } \sin \beta _ { \odot } } \end{array} \right) \quad , } \end{array}
$$

where

is the obliquity of the ecliptic, i.e. the inclination of the ecliptic relative to the Earth’s equator. Since $\beta _ { \odot } { = } 0$ , the expression for $r _ { \odot }$ may further be simplified to give

$$
r _ { \odot } = \left( \begin{array} { l } { r _ { \odot } \cos \lambda _ { \odot } } \\ { r _ { \odot } \sin \lambda _ { \odot } \cos \varepsilon } \\ { r _ { \odot } \sin \lambda _ { \odot } \sin \varepsilon } \end{array} \right) ~ .
$$

To be precise, the longitude $\lambda _ { \odot }$ , the latitude $\beta _ { \odot }$ , and the position vector $r _ { \odot }$ in (3.44) refer to the mean equinox and ecliptic of J2000 (EME2000). Precession, which is a result of perturbing forces of the Sun, Moon and planets, gives rise to a slow motion of both the ecliptic and the equinox. While the ecliptic changes its orientation by less than $1 ^ { \prime }$ per century, the motion of the equinox is more pronounced, however, and amounts to $5 0 3 0 ^ { \prime \prime }$ per century. Referred to the mean equinox of 1950, for example, the Sun’s longitude is smaller than the above value by about $2 5 1 5 ^ { \prime \prime }$ . In order to refer the coordinates to the equinox of some epoch $T _ { \mathrm { e q x } }$ (measured in centuries since the epoch 2000), one has to add a correction of

$$
1 . 3 9 7 2 \cdot T _ { \mathrm { e q x } }
$$

to the value of $\lambda _ { \odot }$ given above. The ecliptic latitude need not be changed since it varies by less than one arcminute within a full century.

Series expansions similar to those for the Sun exist for the lunar coordinates as well. Due to the strong solar and terrestrial perturbations, a larger number of terms are, however, needed to describe the lunar motion in terms of the mean arguments of the lunar and solar orbit. The following relations allow the computation of lunar longitude and latitude with a typical accuracy of several arcminutes and about $5 0 0 \mathrm { k m }$ in the lunar distance. The calculation of the perturbations is based on five fundamental arguments: the mean longitude $L _ { 0 }$ of the Moon, the Moon’s mean anomaly $l$ , the Sun’s mean anomaly $l ^ { \prime }$ , the mean angular distance of the Moon from the ascending node $F$ , and the difference $D$ between the mean longitudes of the Sun and the Moon. The longitude of the ascending node $\varOmega$ is not explicitly employed. It is obtained from the difference $\varOmega = L _ { 0 } - F$ .

$$
\begin{array} { r l r } { D } & { { } = } & { 2 9 7 . 8 5 0 2 7 + 4 4 5 2 6 7 . 1 1 1 3 5 \cdot T } \end{array}
$$

Using these values the Moon’s longitude with respect to the equinox and ecliptic of the year 2000 may be expressed as

$$
\begin{array} { r } { \begin{array} { r l } { \mathrm {  ~ { \cal ~ M } ~ } = } & { L _ { 0 } + 2 2 6 4 0 ^ { \prime \prime } \cdot \sin ( l ) + 7 6 9 ^ { \prime \prime } \cdot \sin ( 2 l ) } \\ & { \quad \quad - 4 5 8 6 ^ { \prime \prime } \cdot \sin ( l - 2 D ) + 2 3 7 0 ^ { \prime \prime } \cdot \sin ( 2 D ) } \\ & { \quad \quad - 6 6 8 ^ { \prime \prime } \cdot \sin ( l ^ { \prime } ) - 4 1 2 ^ { \prime \prime } \cdot \sin ( 2 F ) } \\ & { \quad \quad - 2 1 2 ^ { \prime \prime } \cdot \sin ( 2 l - 2 D ) - 2 0 6 ^ { \prime \prime } \cdot \sin ( l + l ^ { \prime } - 2 D ) } \\ & { \quad \quad + 1 9 2 ^ { \prime \prime } \cdot \sin ( l + 2 D ) - 1 6 5 ^ { \prime \prime } \cdot \sin ( l ^ { \prime } - 2 D ) } \\ & { \quad \quad + 1 4 8 ^ { \prime \prime } \cdot \sin ( l - l ^ { \prime } ) - 1 2 5 ^ { \prime \prime } \cdot \sin ( D ) } \\ & { \quad \quad - 1 1 0 ^ { \prime \prime } \cdot \sin ( l + l ^ { \prime } ) - 5 5 ^ { \prime \prime } \cdot \sin ( 2 F - 2 D ) . } \end{array} } \end{array}
$$

Here, the first two terms describe the motion in an ellipse of eccentricity $e = 0 . 0 5 5$ whereas the remaining terms denote the various perturbations. The lunar latitude is given by

$$
\begin{array} { r c l } { { \beta _ { \mathrm { M } } } } & { { = } } & { { 1 8 5 2 0 ^ { \prime \prime } \sin ( F { + } \lambda _ { \mathrm { M } } { - } L _ { 0 } { + } 4 1 2 ^ { \prime \prime } \cdot \sin 2 F { + } 5 4 1 ^ { \prime \prime } \cdot \sin l ^ { \prime } ) } } \\ { { } } & { { } } & { { - 5 2 6 ^ { \prime \prime } \cdot \sin ( F { - } 2 D ) + 4 4 ^ { \prime \prime } \cdot \sin ( l { + } F { - } 2 D ) } } \\ { { } } & { { } } & { { - 3 1 ^ { \prime \prime } \cdot \sin ( - l { + } F { - } 2 D ) - 2 5 ^ { \prime \prime } \cdot \sin ( - 2 l { + } F ) } } \\ { { } } & { { } } & { { - 2 3 ^ { \prime \prime } \cdot \sin ( l ^ { \prime } { + } F { - } 2 D ) + 2 1 ^ { \prime \prime } \cdot \sin ( - l { + } F ) } } \\ { { } } & { { } } & { { + 1 1 ^ { \prime \prime } \cdot \sin ( - l ^ { \prime } { + } F { - } 2 D ) ~ , } } \end{array}
$$

where the leading term is due to the inclination of the Moon’s orbit relative to the ecliptic, which amounts to approximately $5 . 1 ^ { \circ }$ . Finally the Moon’s distance from the center of the Earth is

$$
\begin{array} { r l } { r _ { \mathrm { M } } = ( } & { 3 8 5 0 0 0 - 2 0 9 0 5 \cos ( l ) - 3 6 9 9 \cos ( 2 D - l ) } \\ & { - 2 9 5 6 \cos ( 2 D ) - 5 7 0 \cos ( 2 l ) + 2 4 6 \cos ( 2 l - 2 D ) } \\ & { - 2 0 5 \cos ( l ^ { \prime } - 2 D ) - 1 7 1 \cos ( l + 2 D ) } \\ & { - 1 5 2 \cos ( l + l ^ { \prime } - 2 D ) ) \mathrm { k m ~ \Omega ~ , } } \end{array}
$$

where terms smaller than $1 5 0 \mathrm { k m }$ have been neglected.

The spherical ecliptic coordinates may again be converted to equatorial Cartesian coordinates using the transformation

$$
\begin{array} { r } { r _ { \mathrm { M } } = R _ { x } ( - \varepsilon ) \left( \begin{array} { l } { r _ { \mathrm { M } } \cos \lambda _ { \mathrm { M } } \cos \beta _ { \mathrm { M } } } \\ { r _ { \mathrm { M } } \sin \lambda _ { \mathrm { M } } \cos \beta _ { \mathrm { M } } } \\ { r _ { \mathrm { M } } \sin \beta _ { \mathrm { M } } } \end{array} \right) } \end{array} .
$$

A change of the reference system from EME2000 to the equator and equinox of some epoch $T _ { \mathrm { e q x } }$ is further accounted for in the same way as for the Sun’s coordinates.

# 3.3.3 Chebyshev Approximation

The above description of the solar and lunar motion is well suited for deriving analytical expressions of the perturbations exerted on a satellite by these bodies, or for low accuracy requirements. If, however, one requires accurate numerical values of the solar and lunar coordinates very frequently, approximations by Chebyshev polynomials may be more adequate. These polynomials are defined as

$$
T _ { n } ( \tau ) = \cos ( n \cdot \operatorname { a r c c o s } \tau )
$$

for $| \tau | \leq 1$ , and may recursively be computed by

$$
\begin{array} { l c l } { { T _ { 0 } ( \tau ) } } & { { = } } & { { 1 } } \\ { { T _ { 1 } ( \tau ) } } & { { = } } & { { \tau } } \\ { { T _ { n + 1 } ( \tau ) } } & { { = } } & { { 2 \tau T _ { n } ( \tau ) - T _ { n - 1 } ( \tau ) \mathrm { f o r } n \geq 1 . } } \end{array}
$$

The property which makes these polynomials so well suited for the approximation of functions is their behaviour within the interval $[ - 1 , + 1 ]$ . As can be seen from Fig. 3.5, the absolute value of each polynomial $T _ { n } ( \tau )$ is always less than or equal to one for $- 1 \leq \tau \leq 1$ . Therefore, given an approximation

$$
f ( t ) \approx \sum _ { i = 0 } ^ { n - 1 } a _ { i } T _ { i } ( \tau )
$$

![](images/e2d76029935ab080b471d7b53c24d87cdb0b2bcc169a866b4b4bcbdc9a4e6708.jpg)  
Fig. 3.5. The Chebyshev polynomials $T _ { 1 }$ to $T _ { 5 }$

of some function $f ( t )$ over a finite time interval $[ t _ { 1 } , t _ { 2 } ]$ that is mapped to $[ - 1 , + 1 ]$ by the transformation

$$
\tau = 2 { \frac { t - t _ { 1 } } { t _ { 2 } - t _ { 1 } } } - 1 ,
$$

one may easily judge the contribution of each individual term to the total accuracy of the approximation. If, for example, one would like to neglect the final term $a _ { n - 1 } T _ { n - 1 }$ , then one would produce an error that varies uniformly between $t _ { 1 }$ and $t _ { 2 }$ , and never exceeds the absolute value of $a _ { n - 1 }$ . If, on the other hand, one had chosen a Taylor series approximation

$$
f ( t ) \approx \sum _ { i = 0 } ^ { n - 1 } b _ { i } \tau ^ { i }
$$

of equal order, the error of neglecting $b _ { n - 1 } \tau ^ { n - 1 }$ would be negligible in the middle of the approximation interval, but most pronounced at the beginning and the end. Furthermore, the coefficients $b _ { i }$ are generally found to be much larger than $a _ { i }$ , so that a higher number of terms would be needed for a similar degree of approximation.

The way in which the coefficients for the approximation of a function $f$ may be calculated depends on the form in which this function is available. If $f$ is known analytically, then one may use the relation

$$
a _ { i } = \frac { 2 - \delta _ { i 0 } } { n } \sum _ { k = 0 } ^ { n - 1 } f ( t _ { k } ^ { n } ) T _ { i } ( \tau _ { k } ^ { n } ) i = 0 , \dots , n - 1
$$

(see Press et al. 1992), to construct an approximation of order $n - 1$ from $n$ values of $f$ at predefined times $t _ { k } ^ { n }$ that correspond to the $n$ roots

$$
\tau _ { k } ^ { n } = \cos \left( \pi \frac { 2 k + 1 } { 2 n } \right) \quad \quad k = 0 , \dots , n - 1
$$

of $T _ { n }$ . This algorithm is not, however, feasible for the approximation of a function that is only known at a number of evenly spaced times. In this case one has to use standard least-squares fit techniques to obtain the desired coefficients for the approximation of $f .$ . In the case of JPL’s Development Ephemerides, a least-squares fit is used to obtain the $n$ coefficients $( a _ { 0 } , \ldots , a _ { n - 1 } )$ from equally spaced positions generated by the numerical integration (Newhall 1989). By using a constrained least-squares adjustment it is, furthermore, assured that continuous position and velocity values are obtained from the Chebyshev approximations at the interval boundaries.

In order to evaluate a given Chebyshev approximation it is not necessary to calculate the Chebyshev polynomials explicitly. An algorithm due to Clenshaw is recommended instead, which minimizes the total number of multiplications required. To start with, $f _ { n }$ and $f _ { n + 1 }$ are set equal to zero. Subsequently the values

$$
f _ { i } = 2 \tau f _ { i + 1 } - f _ { i + 2 } + a _ { i } \mathrm { f o r } i = n - 1 , n - 2 , \ldots , 1
$$

are computed using the normalized time $\tau$ . The approximate value of $f$ is then given by

$$
f ( t ) = \tau f _ { 1 } - f _ { 2 } + a _ { 0 } .
$$

For some applications, e.g. for the computation of the spacecraft velocity from the Chebyshev approximation of the spacecraft position, the derivative of a given Chebyshev approximation is required. To this end, one may obtain the coefficients of the approximation

$$
\frac { d } { d t } f ( t ) \approx \frac { 2 } { t _ { 2 } - t _ { 1 } } \sum _ { i = 0 } ^ { n - 2 } a _ { i } ^ { \prime } T _ { i } ( \tau )
$$

of the time derivative of $f$ from the set of coefficients $( a _ { 0 } , a _ { 1 } , \ldots , a _ { n - 1 } )$ approximating $f ( t )$ itself, using the recurrence relation

$$
\begin{array} { l c l } { { a _ { i } ^ { \prime } } } & { { = } } & { { a _ { i + 2 } ^ { \prime } + 2 ( i + 1 ) a _ { i + 1 } ~ ( i = n - 2 , \ldots , 1 ) } } \\ { { } } & { { } } & { { } } \\ { { a _ { 0 } ^ { \prime } } } & { { = } } & { { a _ { 2 } ^ { \prime } / 2 + a _ { 1 } } } \end{array}
$$

with $a _ { n } ^ { \prime } = a _ { n - 1 } ^ { \prime } = 0 .$ The same method would yield Chebyshev approximations of the higher order derivatives of $f ( t )$ if required.

# 3.3.4 JPL Ephemerides

The Jet Propulsion Laboratory (JPL) provides a series of solar system ephemerides in the form of Chebyshev approximations. The Development Ephemerides (DE) are publicly available and have emerged as a standard for high-precision planetary and lunar coordinates (Seidelmann 1992). Currently the DE200 (Standish 1982, 1990) and DE405 (Standish 1998) ephemerides are most widely used for general applications. They cover a total of roughly 600 years from 1600 to 2170. An extended version of DE405 is, furthermore, available for historical purposes. It is known as DE406 and covers the time span $- 3 0 0 0$ to $+ 3 0 0 0$ .

While the B1950 reference system has been employed in ephemerides with series numbers of less than 200 (e.g. DE118), the DE200 series uses the dynamical equator and equinox of J2000 (EME2000) as reference system. In the recent DE400 series all data are referred to the International Celestial Reference Frame (ICRF, cf. Sect. 5.2), which is realized through a catalog of radio sources. The difference between the dynamical J2000 reference frame and the ICRF is at a level of $0 . { } ^ { \prime \prime } 0 1$ , and determined with an accuracy of $0 { ^ { \prime \prime } } 0 0 3$ (Standish et al. 1995).

All ephemerides are based on a rigorous numerical integration of the respective equations of motion (Newhall et al. 1983, Seidelmann 1992). In addition to the point-mass interactions among the Moon, the planets and the Sun, the perturbations from selected asteroids are considered, as well as relativistic post-Newtonian corrections to the equations of motion. Furthermore, the lunisolar torques on the figure of the Earth, and the Earth’s and Sun’s torques on the figure of the Moon, are taken into account. The observational database for the development of DE405 comprises mainly optical transit measurements of the Sun and the planets since 1911, radar ranging to Mercury and Venus since 1964, tracking of deep space probes, planetary orbiters and landers since 1971, and lunar laser ranging since 1970.

Table 3.4. Number of Chebyshev coefficients $( n )$ per coordinate, number of sub-intervals $( k )$ , and sub-interval size $( \varDelta t )$ in days, used in DE200 and DE405. EMB denotes the Earth-Moon-Barycenter.   

<table><tr><td rowspan="2"># Body</td><td rowspan="2"></td><td colspan="3">DE200</td><td colspan="3">DE405</td></tr><tr><td>n</td><td>k</td><td>△t</td><td>n</td><td>k</td><td>△t</td></tr><tr><td>1</td><td>Mercury</td><td>12</td><td>4</td><td>8</td><td>14</td><td>4</td><td>8</td></tr><tr><td>2</td><td>Venus</td><td>12</td><td>1</td><td>32</td><td>10</td><td>2</td><td>16</td></tr><tr><td>3</td><td>EMB</td><td>15</td><td>2</td><td>16</td><td>13</td><td>2</td><td>16</td></tr><tr><td>4</td><td>Mars</td><td>10</td><td>1</td><td>32</td><td>11</td><td>1</td><td>32</td></tr><tr><td>5</td><td>Jupiter</td><td>9</td><td>1</td><td>32</td><td>8</td><td>1</td><td>32</td></tr><tr><td>6</td><td>Saturn</td><td>8</td><td>1</td><td>32</td><td>7</td><td>1</td><td>32</td></tr><tr><td>7</td><td>Uranus</td><td>8</td><td>1</td><td>32</td><td>6</td><td>1</td><td>32</td></tr><tr><td>8</td><td>Neptune</td><td>6</td><td>1</td><td>32</td><td>6</td><td>1</td><td>32</td></tr><tr><td>9</td><td>Pluto</td><td>6</td><td>1</td><td>32</td><td>6</td><td>1</td><td>32</td></tr><tr><td>10</td><td>Moon</td><td>12</td><td>8</td><td>4</td><td>13</td><td>8</td><td>4</td></tr><tr><td>11</td><td>Sun</td><td>15</td><td>1</td><td>32</td><td>11</td><td>2</td><td>16</td></tr><tr><td>12 13</td><td>Nutation Libration</td><td>10</td><td>4</td><td>8</td><td>10 10</td><td>4 4</td><td>8 8</td></tr></table>

In addition to planetary and lunar coordinates, nutation angles and lunar libration angles are available with some of the ephemerides. In order to obtain a compact representation of the ephemeris data, the discrete positions are replaced by Chebyshev approximations, which allow a direct interpolation of the position and velocity of each body. The complete ephemeris is blocked into data records, where each record covers a fixed time interval of typically 32 days, and contains coefficients for the Chebyshev polynomial approximation of the positions of eleven solar system bodies. As shown in Table 3.4, the order and the time covered by each polynomial has been chosen in accordance with the period of revolution of the individual bodies. An evaluation of the polynomials yields Cartesian coordinates $x , y , z$ in km for the planets, the Earth-Moon barycenter and the Sun with respect to the barycenter of the solar system, while lunar positions are given with respect to the center of the Earth.

While the lunar coordinates $r _ { \mathrm { M } }$ of the JPL ephemerides are already given in the desired form for perturbation calculations (i.e. with respect to the Earth’s center), the geocentric position of the Sun $r _ { \odot }$ is not directly available from the ephemeris but may be computed as

$$
{ \pmb r } _ { \odot } = \hat { { \pmb r } } _ { \odot } - { \pmb r } _ { \mathrm { E M B } } + \frac { 1 } { 1 + \mu ^ { * } } \cdot { \pmb r } _ { \mathrm { M } }
$$

from the position vector of the Sun’s center with respect to the solar barycenter $\hat { r } _ { \odot }$ the position of the Earth-Moon barycenter $r _ { \mathrm { E M B } }$ and the geocentric lunar coordi-

nates $r _ { \mathrm { M } }$ . Here $\mu ^ { * } \approx 8 1 . 3$ denotes the ratio of the Earth’s and the Moon’s masses. For compatibility with the generation of the ephemeris, the value of $\mu ^ { * }$ used in the transformation should be retrieved from the DE file.

# 3.4 Solar Radiation Pressure

A satellite that is exposed to solar radiation experiences a small force that arises from the absorption or reflection of photons. In contrast to the gravitational perturbations discussed up to now, the acceleration due to the solar radiation depends on the satellite’s mass and surface area.

The size of the solar radiation pressure is determined by the solar flux

$$
\varPhi = \frac { \varDelta E } { \ A \varDelta t } ,
$$

i.e. by the energy $\varDelta E$ that passes through an area $A$ in a time interval $\varDelta t$ . A single photon of energy $E _ { \nu }$ carries an impulse

$$
p _ { \nu } = \frac { E _ { \nu } } { c } ,
$$

where $c$ is the velocity of light. Accordingly, the total impulse of an absorbing body that is illuminated by the Sun changes by

$$
\varDelta p = \frac { \varDelta E } { c } = \frac { \varPhi } { c } A \varDelta t
$$

during the time $\varDelta t$ . This means that the satellite experiences a force

$$
F = { \frac { \varDelta p } { \varDelta t } } = { \frac { \varPhi } { c } } A
$$

that is proportional to the cross-section $A$ or, equivalently, a pressure

$$
P = \frac { \phi } { c } .
$$

In a distance of one Astronomical Unit $( 1 ~ \mathrm { A U } \approx 1 4 9 . 6 ~ \mathrm { M i o } ~ \mathrm { k m } )$ ) from the Sun – i.e., at the mean orbital radius of the Earth around the Sun – the solar flux amounts to

$$
\Phi \approx 1 3 6 7 \mathrm { W m } ^ { - 2 }
$$

(McCarthy 1996), and the solar radiation pressure is, therefore, given by

$$
P _ { \odot } \approx 4 . 5 6 { \cdot } 1 0 ^ { - 6 } \mathrm { N m } ^ { - 2 }
$$

if one assumes that the satellite’s surface $A$ absorbs all photons and is perpendicular to the incoming radiation.

The more general case of a satellite surface with an arbitrary orientation is illustrated in Fig. 3.6 for the cases of complete absorption (reflectivity $\varepsilon = 0$ ) and complete specular reflection (reflectivity $\varepsilon = 1$ ). In contrast to specular reflection,

![](images/6ae1ae467a3fedcb1bc8219efa01caf2752b118c63533ecfe9e7a98d618f57ac.jpg)  
Fig. 3.6. The force due to solar radiation pressure for absorbing $\varepsilon = 0$ ) and reflecting $\left. \varepsilon = 1 \right.$ ) surface elements

the diffuse reflection of light is neglected in the sequel. The normal vector $\pmb { n }$ gives the orientation of the surface $A$ . It is inclined at an angle $\theta$ to the vector $e _ { \odot }$ which points into the direction of the Sun.

For an absorbing surface, it follows from the consideration given above that the force $F _ { \mathrm { a b s } }$ is equal to

$$
F _ { \mathrm { a b s } } = - P _ { \odot } \cos ( \theta ) A e _ { \odot }
$$

where $\cos ( \theta ) A$ is the cross-section of the bundle of light that illuminates $A$ . For a reflecting surface, the force is not, in general, directed away from the Sun, since no impulse is transferred in the direction parallel to the surface. Due to the reflected light rays, the impulse transferred in the direction of $\pmb { n }$ is twice as large, however, as in the case of pure absorption, and the resulting force is, therefore, given by

$$
F _ { \mathrm { r e f l } } = - 2 P _ { \odot } \cos ( \theta ) A \cos ( \theta ) { \pmb { n } } ~ .
$$

Both formulas may be combined for a body that reflects a fraction $\varepsilon$ of the incoming radiation $\varDelta E$ , while it absorbs the remaining energy $( 1 - \varepsilon ) \varDelta E$ :

$$
\mathbf { \cal F } = - P _ { \odot } \cos ( \theta ) { \cal A } \left[ ( 1 - \varepsilon ) e _ { \odot } + 2 \varepsilon \cos ( \theta ) { \cal n } \right] \ \mathrm { ~ . ~ }
$$

For typical materials used in the construction of satellites, the reflectivity $\varepsilon$ lies in the range from 0.2 to 0.9 (see Table 3.5).

Table 3.5. Reflectivity, absorption and radiation pressure coefficient of selected satellite components (cf. van der Ha & Modi 1977)   

<table><tr><td>Material</td><td>8</td><td>1-ε</td><td>CR~1+ε</td></tr><tr><td>Solar panel</td><td>0.21</td><td>0.79</td><td>1.21</td></tr><tr><td>High-gain antenna</td><td>0.30</td><td>0.70</td><td>1.30</td></tr><tr><td>Aluminum coated mylar solar sail</td><td>0.88</td><td>0.12</td><td>1.88</td></tr></table>

Due to the eccentricity of the Earth’s orbit, the distance between an Earth-orbiting satellite and the Sun varies between $1 4 7 . 1 0 ^ { 6 } \mathrm { k m }$ and $1 5 2 . 1 0 ^ { 6 } \mathrm { k m }$ during the course of a year. This results in an annual variation of the solar radiation pressure by about $\pm 3 . 3 \%$ , since the solar flux decreases with the square of the distance from the Sun. Accounting for this dependence, one finally obtains the following expression for the acceleration of a satellite due to the solar radiation pressure:

$$
\ddot { r } = - P _ { \odot } \frac { 1 \mathrm { A U } ^ { 2 } } { r _ { \odot } ^ { 2 } } \frac { A } { m } \cos ( \theta ) \left[ ( 1 - \varepsilon ) e _ { \odot } + 2 \varepsilon \cos ( \theta ) \pmb { n } \right] .
$$

Here $m$ means the satellite’s mass and cos $\theta$ may be calculated from

$$
\cos \theta = \pmb { n } ^ { T } \pmb { e } _ { \odot } \quad ,
$$

since both $\pmb { n }$ and $e _ { \odot }$ are unit vectors.

For many applications (e.g. satellites with large solar arrays) it suffices, however, to assume that the surface normal $\pmb { n }$ points in the direction of the Sun. In this case (3.73) may further be simplified, yielding

$$
\ddot { r } = - P _ { \odot } C _ { R } \frac { A } { m } \frac { r _ { \odot } } { r _ { \odot } ^ { 3 } } \mathrm { A U } ^ { 2 } ~ ,
$$

where the radiation pressure coefficient $C _ { R }$ stands for

$$
C _ { R } = 1 + \varepsilon .
$$

Equation (3.75) is commonly used in orbit determination programs with the option of estimating $C _ { R }$ as a free parameter. Orbital perturbations due to the solar radiation pressure may thus be accounted for with high precision, even if no details of the satellites structure, orientation and reflectivity are known.

For high-precision applications, which are required for geodetic space missions, the simple model of Equation (3.75) no longer suffices. In this case the complex satellite structure, as well as the various surface properties, have to be treated. To avoid an excessive computational effort during orbit determination, a complex micro model may be established prior to the mission, which is used to adjust parameters of a simplified macro model, applied during routine spacecraft operations (Marshall et al. 1991). To this end, a finite element method is applied to model the complex spacecraft shape and orientation, the optical and thermal properties of the surfaces, and the impinging radiation. The definition of a simplified macro satellite model may then consist of a “box-wings” satellite shape, with six flat plates as the satellite body, and four flat plates for the front and back of the two connected solar arrays. The adjustable parameters of the macro model consist of the area and specular and diffuse reflectivities of the individual plates; the individual vector accelerations are finally summed to compute the total acceleration on the satellite’s center-of-mass.

# 3.4.1 Eclipse Conditions

So far, the size of the solar radiation pressure has been derived under the assumption of full illumination by the Sun. For most Earth-orbiting satellites, however, partial or total eclipses occur when the satellite passes the night side of the Earth. Apart from occultations of the Sun by the Earth, the Moon may also cast a shadow on the satellite, even though these events occur less frequently and in a “random” fashion. Although the computation of eclipse conditions is generally applied for the Earth as occulting body, the following models are generic and may well be adapted to other cases.

![](images/001fe0fbc405ce1272ed9e411099fe4301dffd148107f02f83b42c5f450ced1c.jpg)  
Fig. 3.7. Conical shadow model

Neglecting the atmosphere or oblateness of the occulting body, eclipse conditions may be derived from a conical shadow model as illustrated in Fig. 3.7. Let

$$
s _ { \odot } = r _ { \odot } - r _ { \mathrm { B } }
$$

and

$$
s = r - r _ { \mathrm { B } }
$$

denote the coordinates of the Sun and the spacecraft with respect to the occulting body at $r _ { \mathrm { B } }$ . The fundamental plane, which is perpendicular to the shadow axis and passes through the satellite, then intersects the shadow axis at a distance

$$
s _ { 0 } = ( - s ^ { T } s _ { \odot } ) / | s _ { \odot } |
$$

from the center of the occulting body in anti-Sun direction. Accordingly,

$$
l = \sqrt { s ^ { 2 } - s _ { 0 } ^ { 2 } }
$$

is the distance of the spacecraft from the shadow axis.

Making use of the solar radius $R _ { \odot }$ and the body radius $R _ { \mathrm { B } }$ , the generating angles of the shadow cones are given by

$$
\begin{array} { l c l } { { \sin f _ { 1 } } } & { { = } } & { { ( R _ { \odot } + R _ { \mathrm { B } } ) / s _ { \odot } } } \\ { { \sin f _ { 2 } } } & { { = } } & { { ( R _ { \odot } - R _ { \mathrm { B } } ) / s _ { \odot } ~ . } } \end{array}
$$

Here and in the sequel, the index $1$ denotes quantities related to the shadow cone of the penumbra, whereas the index $^ 2$ refers to the cone of the umbra. When the occulting body is the Earth, the half cone angle of the umbra is $0 . 2 6 4 ^ { \circ }$ and $0 . 2 6 9 ^ { \circ }$ for the penumbra. This yields the distances

$$
\begin{array} { r l r } { c _ { 1 } } & { = } & { s _ { 0 } + R _ { \mathrm { B } } / \sin f _ { 1 } } \\ { c _ { 2 } } & { = } & { s _ { 0 } - R _ { \mathrm { B } } / \sin f _ { 2 } } \end{array}
$$

(measured in anti-Sun direction) of the fundamental plane from the vertices $V _ { 1 }$ and $V _ { 2 }$ of the shadow cones, as well as the radii

$$
\begin{array} { r l r } { l _ { 1 } } & { { } = } & { c _ { 1 } \tan f _ { 1 } } \\ { l _ { 2 } } & { { } = } & { c _ { 2 } \tan f _ { 2 } } \end{array}
$$

of the shadow cones in the fundamental plane. Regarding the sign of $l _ { 2 }$ , it is noted that $l _ { 2 }$ is negative between the occulting body and the vertex of the umbral cone (total eclipse region). Behind the vertex $V _ { 2 }$ $( c _ { 2 } > 0 , l _ { 2 } > 0 )$ , with a geocentric distance of $1 . 3 8 4 \cdot 1 0 ^ { 6 } \mathrm { k m }$ for the Earth, the apparent diameter of the occulting body is less than that of the Sun, implying an annular eclipse if the spacecraft is inside the umbral cone.

# 3.4.2 Shadow Function

The orbital perturbations resulting from shadow transits may be treated by generalizing (3.73) according to

$$
\ddot { r } = - \nu P _ { \odot } \frac { 1 \mathrm { A U } ^ { 2 } } { r _ { \odot } ^ { 2 } } \frac { A } { m } \cos ( \theta ) \left[ ( 1 - \varepsilon ) e _ { \odot } + 2 \varepsilon \cos ( \theta ) n \right]
$$

where $\nu$ is the shadow function, such that

$\nu = 0$ if the satellite is in umbra $\nu = 1$ if the satellite is in sunlight $0 < \nu < 1$ if the satellite is in penumbra.

The degree of the Sun’s occultation by a body like the Earth or the Moon is computed from the angular separation and diameters of the respective bodies. Due to the smal

![](images/c11848bfed0c388e7463b6a605b1027dbbe176e23f23e7c6ca7b954ecc68eb6d.jpg)  
Fig. 3.8. Occultation of the Sun by a spherical body.

apparent diameter of the Sun, it is sufficient to model the occultation by overlapping circular disks. Let

$$
a = \arcsin { \frac { R _ { \odot } } { | r _ { \odot } - r | } }
$$

be the apparent radius of the occulted body (i.e. the Sun),

$$
b = \arcsin { \frac { R _ { \mathrm { B } } } { s } }
$$

be the apparent radius of the occulting body, and

$$
c = \operatorname { a r c c o s } { \frac { - s ^ { T } ( { \pmb r } _ { \odot } - { \pmb r } ) } { s | { \pmb r } _ { \odot } - { \pmb r } | } }
$$

be the apparent separation of the centers of both bodies (cf. Fig. 3.8). Then the area of the occulted segment of the apparent solar disk is

$$
A = A _ { \mathrm { C F C } } , + A _ { \mathrm { C D C } } ,
$$

provided that

$$
| a - b | < c < a + b .
$$

The occulted area may be expressed as

$$
A = 2 ( A _ { \mathrm { B C F } } - A _ { \mathrm { B C E } } ) + 2 ( A _ { \mathrm { A C D } } - A _ { \mathrm { A C E } } ) .
$$

Using the notation ${ \overline { { A E } } } = x$ , ${ \overline { { E C } } } = y$ , and $\angle C A E = \alpha$ , the individual areas are given by

$$
\begin{array} { l c l } { { A _ { \mathrm { A C D } } } } & { { = } } & { { { \frac { 1 } { 2 } } \alpha a ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { A _ { \mathrm { A C E } } } } & { { = } } & { { { \frac { 1 } { 2 } } x y } } \end{array}
$$

with similar relations for the other area sections. Finally we end up with

$$
A = a ^ { 2 } \cdot \operatorname { a r c c o s } ( x / a ) + b ^ { 2 } \cdot \operatorname { a r c c o s } ( ( c - x ) / b ) - c \cdot y
$$

where

$$
x = { \frac { c ^ { 2 } + a ^ { 2 } - b ^ { 2 } } { 2 c } } \ \quad { \mathrm { ~ a n d ~ } } \quad y = { \sqrt { a ^ { 2 } - x ^ { 2 } } } .
$$

The remaining fraction of Sun light is thus given by

$$
\nu = 1 - \frac { A } { \pi a ^ { 2 } } .
$$

If the condition (3.89) is not satisfied, no occultation takes place $( a + b \leq c )$ or the occultation is total $( c < b - a$ implying that $a \textless b$ ) or partial but maximum $( c < a - b$ implying that $a > b$ ). It is noted that shadow transits violate the assumption of continuous high-order derivatives of the force function, which is made by all common algorithms for the numerical integration of the equation of motion. Especially if the penumbra regime is not sampled by the integration algorithm due to a large stepsize, an apparent discontinuity is noted, leading to numerical integration errors. In some cases, the error when entering the shadow is opposite to the error when exiting the shadow, but an error cancellation will not inevitably occur. Hence, for long-term orbit prediction, the integration step size should not be in resonance with the shadow entry period (i.e. the time interval between shadow entries in subsequent orbits) to avoid an accumulation of numerical integration errors (Lundberg 1996).

# 3.5 Atmospheric Drag

Atmospheric forces represent the largest non-gravitational perturbations acting on low altitude satellites. However, accurate modeling of aerodynamic forces is difficult from three points of view. Firstly, the physical properties of the atmosphere, in this case especially the density of the upper atmosphere, are not known very accurately. Secondly, the modeling of these forces requires detailed knowledge of the interaction of neutral gas, as well as charged particles, with the different spacecraft surfaces. Thirdly, the varying attitude of non-spherical satellites with respect to the atmospheric particle flux has to be taken into account.

The dominant atmospheric force acting on low altitude satellites, called drag, is directed opposite to the velocity of the satellite motion with respect to the atmospheric flux, hence decelerating the satellite. Minor contributions to atmospheric forces are the lift force and binormal forces, acting perpendicular to this relative velocity. In most cases they can safely be neglected. The dependence of the drag force on the velocity of the object relative to the atmosphere ${ \pmb v } _ { r }$ can be derived in a simple way. Consider a small mass element $\varDelta m$ of an atmosphere column that hits the satellite’s cross-sectional area $A$ in some time interval $\varDelta t$

$$
\varDelta m = \rho A v _ { r } \varDelta t \quad ,
$$

where $\rho$ is the atmospheric density at the location of the satellite. The impulse $d p$ exerted on the satellite is then given by

$$
\varDelta p = \varDelta m v _ { r } = \rho A v _ { r } ^ { 2 } \varDelta t \quad ,
$$

which is related to the resulting force $F$ by $F = \varDelta p / \varDelta t$ . The satellite acceleration due to drag can therefore be written as

$$
\ddot { r } = - \frac { 1 } { 2 } C _ { D } \frac { A } { m } \rho v _ { r } ^ { 2 } { \pmb e } _ { v } \quad ,
$$

where $m$ is the spacecraft mass. The drag coefficient $C _ { D }$ is a dimensionless quantity that describes the interaction of the atmosphere with the satellite’s surface material. Typical values of $C _ { D }$ range from 1.5–3.0, and are commonly estimated as free parameters in orbit determination programs. The direction of the drag acceleration is always (anti-)parallel to the relative velocity vector as indicated by the unit vector $e _ { v } = { v _ { r } } / { v _ { r } }$ . Here the factor of $\frac { 1 } { 2 }$ has been introduced to preserve a consistent notation in all branches of aerodynamics, since $\scriptstyle { \frac { 1 } { 2 } } \rho A v ^ { 2 } A t$ is the increase in pressure when low-speed air is stopped.

The drag coefficient $C _ { D }$ depends on the interaction of the atmospheric constituents with the satellite surface. In the free molecular flow regime, where the satellites usually move, the particles re-emitted from the satellite do not interfere with the incident molecules, i.e. the mean free path $\lambda$ is much greater than the typical satellite dimension l. This regime can be characterized by a so-called Knudsen number $K = \lambda / l \geq 1 0$ . At lower altitudes $\lambda$ decreases, and a situation with $K \ : < 0 . 1$ may occur which is then called the hypersonic continuum flow. In this regime, which is entered in most cases only near the end of low-Earth satellite lifetimes, the $C _ { D }$ coefficient is reduced from about 2.3 to about 1.0, since the reemitted molecules partially shield the satellite from the incident flow. In Fig. 3.9 the Knudsen numbers depending on the satellite dimension and altitude are shown.

![](images/ae66f4425eb497148413d9c670d41cad12b04b8f95bd54eeaa0c6ff031c8f03f.jpg)  
Fig. 3.9. Knudsen numbers depending on satellite dimension and altitude

Two principally different scattering mechanisms are possible: a specular, elastic reflection of the impinging particles, and a diffuse reflection (Fig. 3.10). Diffuse reflection occurs when the atmospheric particles penetrate the satellite surface, interact with the body molecules, and are finally re-emitted in a random manner, producing forces tangential to the local surface element. In fact, both types of scattering appear to various degrees. A variety of different algorithms for computing the gas-surface interaction has been established. In Schamberg’s model (Schamberg 1959), for example, this interaction is parameterized by the relation of incident and reflection angle, the speed of reflected molecules, and the angular width of the reflected beam.

![](images/374d960540c9c36f054173a9276088a5a80ae58acce4c38e3ad5754e8b8b17c8.jpg)  
Fig. 3.10. Two principally different scattering mechanisms: specular and diffuse reflection

The a priori knowledge of $C _ { D }$ is generally not very good, because the drag coefficient depends in a complex way on the spacecraft surface material, the chemical constituents of the atmosphere, the molecular weight, and temperature of the impinging particles . Therefore, if possible, the drag coefficient is estimated during the orbit determination process. A crude approximation is $C _ { D } = 2$ in the case of a spherical body, whereas typical values for non-spherical convex-shaped spacecraft range from 2.0 to 2.3.

The area-to-mass ratio in principle requires the knowledge of the spacecraft attitude. A constant area-to-mass ratio can, however, be assumed in the Earthpointing mode, where one of the satellite’s main axes of inertia is permanently aligned with the radial direction vector.

The relative velocity of the satellite with respect to the atmosphere depends on the complex atmospheric dynamics. However, a reasonable approximation of the relative velocity is obtained with the assumption that the atmosphere co-rotates with the Earth. Therefore one can write

$$
\pmb { v } _ { r } = \pmb { v } - \pmb { \omega } _ { \oplus } \times \pmb { r } \quad ,
$$

with the inertial satellite velocity vector $v$ , the position vector $r$ , and the Earth’s angular velocity vector $\omega _ { \oplus }$ of size $0 . 7 2 9 2 { \cdot } 1 0 ^ { - 4 } \mathrm { r a d / s }$ . Maximum observed deviations from this assumption are of the order of $40 \%$ (King-Hele 1987), leading to uncertainties in the drag force of less than $5 \%$ . A global atmospheric wind model above $2 2 0 \mathrm { k m }$ was established by Hedin et al. (1988) using a limited set of vector spherical harmonics.

As the drag force depends on the atmospheric density $\rho$ at the satellite location, the modeling of the complex properties and dynamics of the Earth’s atmosphere is a challenging task of modern precision orbit determination. A variety of more or less complicated atmospheric models have been established recently, with typical density differences for different models of about $20 \%$ at a lower altitude of $3 0 0 \mathrm { k m }$ , even increasing at higher altitudes. It is remarkable that the accuracy of empirical drag models has not significantly improved during the past two decades (see e.g. Marcos et al. 1989).

# 3.5.1 The Upper Atmosphere

The density of the upper atmosphere depends in a complex way on a variety of different parameters. The most evident dependency, however, is its decrease with increasing altitude. A very rough estimate of this dependency is expressed in the strongly simplified formula

$$
\rho = \rho _ { 0 } \mathrm { e } ^ { - h / H _ { 0 } } \quad ,
$$

where $\rho _ { 0 }$ is the atmospheric density at some reference height, and $H _ { 0 }$ is the density scale height, which is $7 . 9 \mathrm { k m }$ at mean sea level and increases with geodetic height. According to the theory of thermodynamics, the hydrostatic equation together with the gas law can be used to derive $H _ { 0 }$ as

$$
H _ { 0 } = \frac { \mathcal { R } T } { \mu g } \mathrm { ~ . ~ }
$$

Here, $\mathcal { R }$ denotes the universal gas constant, $T$ the absolute temperature, $g =$ $G M _ { \oplus } / r ^ { 2 }$ the Earth’s gravitational acceleration, and $\mu$ the molecular weight of the atmospheric constituents. From (3.100) it is seen that the partial densities of the different gas constituents decrease at different rates. Therefore, the distribution of chemical constituents in the atmosphere has to be taken into account. While below $1 0 0 \mathrm { k m }$ the atmospheric species are in a state of turbulent mixing, called homosphere, the molecular dissociation and diffusion leads to an inhomogeneous species distribution in the heterosphere. Below $1 7 0 \mathrm { k m }$ altitude, nitrogen is dominant (cf. Fig. 3.11), whereas up to $5 0 0 { - } 6 0 0 \mathrm { k m }$ , depending on solar activity, the atmosphere mainly consists of atomic oxygen. In the regime from $5 0 0 \mathrm { k m }$ to $9 0 0 \mathrm { k m }$ helium dominates, followed by atomic hydrogen at higher altitudes.

![](images/97810836ed8f6e573837631410646f284a8e73da60a91dbffb23624a973b486b.jpg)  
Fig. 3.11. Number density of atmospheric constituents at $T _ { \infty } = 1 0 0 0 \mathrm { K }$

![](images/bfc2abec7bd74bee388d2eaaaa1a7bd2c0e2e38a1c1a7b88e01f53d139654e47.jpg)  
Fig. 3.12. Temperature stratification in the atmosphere with respect to altitude

From (3.100) it is also evident that a model of the atmospheric temperature variation is required. In Fig. 3.12 the temperature stratification in the Earth’s atmosphere with respect to geodetic height is shown. The lower atmosphere is divided into the troposphere, stratosphere and mesosphere. At mean sea level the typical temperature is $2 9 0 ~ \mathrm { K }$ , which decreases with increasing height to $2 2 0 ~ \mathrm { K }$ . A local temperature maximum of $2 8 0 \mathrm { K }$ is reached at a height of $5 0 \mathrm { k m }$ , due to the absorption of solar ultraviolet radiation in an ozone layer. Again, the temperature drops to a minimum of about $1 8 0 ~ \mathrm { K }$ at the mesopause, the transition from the mesosphere to thermosphere at $9 0 \mathrm { k m }$ height. The thermosphere is characterized by a rapid increase in temperature, approaching the exospheric temperature at the thermopause at $4 5 0 { \mathrm { - } } 6 0 0 { \mathrm { k m } }$ altitude. As indicated in Fig. 3.12, the exospheric temperature is no longer dependent on the height, therefore it is often denoted by $T _ { \infty }$ . However, the exospheric temperature is strongly dependent on many parameters, and varies in a regime of typically $4 0 0 \mathrm { K }$ to $2 0 0 0 \mathrm { K }$ . Once the exospheric temperature is known, the temperature stratification in the thermosphere can be derived. This fact explains the great importance of the exospheric temperature in atmospheric density modeling, such as e.g. in the Jacchia models.

There are mainly three effects of solar radiation that affect the upper atmosphere. Firstly, the diurnal or day-night effect, resulting from the solar ultraviolet radiation heating, produces a diurnal variation of the atmospheric density. The maximum density occurs two hours after local noon, approximately at the latitude of the sub-solar point, while a minimum density is found three hours past midnight near the same latitude but in the opposite hemisphere. This density variation is therefore dependent on the geographical latitude. The second effect results from the extreme ultraviolet radiation of the Sun, varying on different time scales. Besides a short-term 27-day period, related to the rotation period of the Sun, the Sun’s activity is characterized by the 11-year Sun spot cycle. It has been discovered that variations in the solar decimeter flux are related to the extreme ultraviolet radiation from the Sun. Therefore, the $1 0 . 7 ~ \mathrm { c m }$ radiation index denoted by $F _ { 1 0 . 7 }$ is introduced, which accounts for extreme ultraviolet radiation effects. $F _ { 1 0 . 7 }$ is measured in units of $1 0 ^ { - 2 2 } \mathrm { W / m } ^ { 2 } / \mathrm { s } = 1 0 ^ { 4 }$ Jansky (Jy). Since 1947, measurements of this flux line have been recorded by the National Research Council in Ottawa on a daily basis, and from 1991 on by a radio telescope in Penticton, British Columbia. These values appear in printed form as “Solar-Geophysical Data prompt reports” as well as electronically, published by the National Geophysical Data Center (NGDC) in Boulder, Colorado. Finally, the third effect results from the corpuscular solar wind, which is responsible for short-term fluctuations in the atmospheric density.

Table 3.6. Relation of geomagnetic $a _ { p }$ to $K _ { p }$ values (Mayaud 1980)   

<table><tr><td>a</td><td>0 00</td><td>2 0+</td><td>3 1-</td><td>4 10</td><td>5 1+</td><td>6 2-</td><td>7 20</td><td>8 2+</td><td>12 3-</td><td>15 30</td><td>18 3+</td><td>22 4-</td><td>27 40</td><td>32 4+</td></tr><tr><td>ap Kp</td><td>39 5-</td><td>48 50</td><td>56 5+</td><td>67 6-</td><td>80 60</td><td>94 6+</td><td>111 7-</td><td>132 70</td><td>154 7+</td><td>179 8-</td><td>207 80</td><td>236 8+</td><td>300 9-</td><td>400 90</td></tr></table>

Geomagnetic storms affecting the thermosphere have been observed for many years. They increase the temperature, as well as the total density, associated with chemical composition changes on a timescale of one or two days. Although a large number of satellite acceleration measurements are available (Berger at al. 1988) the basic physical processes are not yet known precisely. It is, however, evident that the interaction of the solar wind and the Earth’s magnetic field plays a major role in perturbations of the geomagnetic field. The “three-hourly planetary geomagnetic index” $K _ { p }$ is used as a global measure of a three-hour variation in the Earth’s magnetic field. It is obtained from $K$ -indices that are measured at 12 observatories situated at locations ranging from $4 8 ^ { \circ }$ to $6 3 ^ { \circ }$ geomagnetic latitude. The $K$ -indices, integers in the range 0 to 9, correspond to variations in the horizontal component of the geomagnetic field with respect to a quiet day, as measured by magnetometers. These variations amount up to $4 0 0 ~ \mathrm { n T }$ , compared to the Earth’s magnetic field of about $3 0 0 0 0 { \mathrm { n T } } .$ In some cases geomagnetic data are given as $a _ { p }$ values, the “threehourly planetary amplitude index”, which is related to $K _ { p }$ as given in Table 3.6. Note that $K _ { p }$ is a one-digit number, subdivided into units of 1/3.

A collation of minimum, typical and maximum numbers of the daily $F _ { 1 0 . 7 }$ index, the $\bar { F } _ { 1 0 . 7 }$ , averaged over 90 days, and the geomagnetic $K _ { p }$ index, is given in Table 3.7. The short- and long-term evolution of solar flux values and prediction algorithms are discussed in Sect. 3.5.5.

Table 3.7. Solar flux values and geomagnetic indices   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>F10.7</td><td rowspan=1 colspan=1>F10.7</td><td rowspan=1 colspan=1>Kp</td></tr><tr><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>00</td></tr><tr><td rowspan=1 colspan=1>Typical</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>155</td><td rowspan=1 colspan=1>40</td></tr><tr><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>330</td><td rowspan=1 colspan=1>240</td><td rowspan=1 colspan=1>80</td></tr></table>

A lag of 6.7 hours in the response of temperature changes to geomagnetic storms, indicated by $K _ { p }$ values from 6 to 9, has been observed. Along with the solar flux values, geomagnetic data are also available in the above-mentioned “Solar-Geophysical Data prompt reports”.

Semi-annual variations in the atmospheric density show a strong height dependence and periodic variations throughout the year. However, these variations seem not to be connected with the solar activity, and the geophysical mechanisms behind these variations are not well understood.

At lower altitudes of $9 0 { - } 1 2 0 \mathrm { k m }$ , latitudinal density fluctuations have been observed in the thermosphere related to seasonal variations. The amplitude of these variations attains a maximum at about $1 1 0 \mathrm { k m }$ height, and is assumed to decrease rapidly with increasing height.

Seasonal-latitudinal variations of the helium density in the upper atmosphere have been observed, resulting from helium migration towards the winter pole. No major height-dependency seems to exist.

Additionally, there are a number of further atmospheric processes that affect the density, as e.g. variations in the hydrogen density and pressure waves in the atmosphere. However, as accurate modeling of global atmospheric properties is lacking, these smaller effects are neglected in most cases.

# 3.5.2 The Harris–Priester Density Model

Although the dynamics of the upper atmosphere shows a significant temporal and spatial variation, there exist relatively simple atmospheric models that already allow for a reasonable atmospheric density computation. Thus, prior to a description of elaborate and complex models, we consider the algorithm of Harris–Priester (Harris & Priester 1962, see also Long et al. 1989), which is still widely used as a standard atmosphere and may be adequate for many applications.

The Harris–Priester model is based on the properties of the upper atmosphere as determined from the solution of the heat conduction equation under quasihydrostatic conditions. While neglecting the explicit dependence of semi-annual and seasonal latitude variations, it has been extended to consider the diurnal density bulge. As the atmospheric heating due to the solar radiation leads to a gradual increase of the atmospheric density, the apex of this bulge is delayed by approximately 2 hours, equivalent to a location $3 0 ^ { \circ }$ to the east of the subsolar point (Long et al. 1989). The antapex and apex density $\rho _ { m } ( h )$ and $\rho _ { M } ( h )$ at a given altitude $h$ is computed through the exponential interpolation between tabulated minimum and maximum density values $\rho _ { m } ( h _ { i } )$ and $\rho _ { M } ( h _ { i } )$ according to

$$
\begin{array} { r c l l } { { \rho _ { m } ( h ) } } & { { = } } & { { \rho _ { m } ( h _ { i } ) \exp { ( \displaystyle \frac { h _ { i } - h } { H _ { m } } ) } } } & { { ( h _ { i } \leq h \leq h _ { i + 1 } ) } } \\ { { \rho _ { M } ( h ) } } & { { = } } & { { \rho _ { M } ( h _ { i } ) \exp { ( \displaystyle \frac { h _ { i } - h } { H _ { M } } ) } } } & { { , } } \end{array}
$$

where $h$ is the height above the Earth’s reference ellipsoid. The corresponding scale heights are given as

$$
\begin{array} { r c l } { { H _ { m } ( h ) } } & { { = } } & { { \displaystyle \frac { h _ { i } - h _ { i + 1 } } { \ln ( \rho _ { m } ( h _ { i + 1 } ) / \rho _ { m } ( h _ { i } ) ) } \ } } \\ { { H _ { M } ( h ) } } & { { = } } & { { \displaystyle \frac { h _ { i } - h _ { i + 1 } } { \ln ( \rho _ { M } ( h _ { i + 1 } ) / \rho _ { M } ( h _ { i } ) ) } . } } \end{array}
$$

The diurnal density variation from the apex to the antapex due to the solar radiation is accomplished through a cosine variation according to

$$
\rho ( h ) = \rho _ { m } ( h ) + ( \rho _ { M } ( h ) - \rho _ { m } ( h ) ) \cdot \cos ^ { n } \left( \frac { \psi } { 2 } \right) ~ ,
$$

where $\psi$ is the angle between the satellite position vector and the apex of the diurnal bulge. In practice, the latitudinal density variations are roughly taken into account by the declination-dependent angle $\psi$ and by the exponent $n$ , which has a numerical value of 2 for low-inclination orbits, and 6 for polar orbits. Using trigonometric calculus and the definition of $\psi$ we derive

$$
\cos ^ { n } \left( \frac { \psi } { 2 } \right) = \left( \frac { 1 + \cos \psi } { 2 } \right) ^ { \frac { n } { 2 } } = \left( \frac { 1 } { 2 } + \frac { e _ { r } \cdot e _ { b } } { 2 } \right) ^ { \frac { n } { 2 } } ,
$$

with the unit satellite position vector $e _ { r }$ . The unit vector $e _ { b }$ to the apex of the diurnal bulge is given as

$$
\begin{array} { r } { \pmb { e } _ { b } = = \left( \begin{array} { l } { \cos \delta _ { \odot } \cos ( \alpha _ { \odot } + \lambda _ { l } ) } \\ { \cos \delta _ { \odot } \sin ( \alpha _ { \odot } + \lambda _ { l } ) } \\ { \sin \delta _ { \odot } } \end{array} \right) } \end{array}
$$

with the Sun’s right ascension $\alpha _ { \odot }$ , declination $\delta _ { \odot }$ and the lag angle in longitude $\lambda _ { l } \approx 3 0 ^ { \circ }$ .

In Table 3.8 the minimum and maximum density values are given for an altitude regime of $1 0 0 \mathrm { k m }$ to $1 0 0 0 \mathrm { k m }$ and mean solar activity. In addition to its computational simplicity, the benefit of the Harris–Priester density model is that it can easily be tailored or extended to other altitude regimes or to other solar flux conditions. A multi-parametric comparison with the Jacchia 1971 model shows a mean deviation in density of about $40 \%$ for mean solar flux conditions, which increases to $60 \%$ for maximum solar activity. Since considerably higher deviations have been observed for minimum solar flux conditions, the tabular coefficients should be modified suitably for low solar activity phases.

Table 3.8. Harris–Priester atmospheric density coefficients valid for mean solar activity (Long et al. 1989)   

<table><tr><td>h [km]</td><td>pm [g/km³]</td><td>PM [g/km3]</td><td>h [km]</td><td>pm [g/km3]</td><td>PM [g/km³]</td></tr><tr><td>100</td><td>497400.0</td><td>497400.0</td><td>420</td><td>1.558</td><td>5.684</td></tr><tr><td>120</td><td>24900.0</td><td>24900.0</td><td>440</td><td>1.091</td><td>4.355</td></tr><tr><td>130</td><td>8377.0</td><td>8710.0</td><td>460</td><td>0.7701</td><td>3.362</td></tr><tr><td>140</td><td>3899.0</td><td>4059.0</td><td>480</td><td>0.5474</td><td>2.612</td></tr><tr><td>150</td><td>2122.0</td><td>2215.0</td><td>500</td><td>0.3916</td><td>2.042</td></tr><tr><td>160</td><td>1263.0</td><td>1344.0</td><td>520</td><td>0.2819</td><td>1.605</td></tr><tr><td>170</td><td>800.8</td><td>875.8</td><td>540</td><td>0.2042</td><td>1.267</td></tr><tr><td>180</td><td>528.3</td><td>601.0</td><td>560</td><td>0.1488</td><td>1.005</td></tr><tr><td>190</td><td>361.7</td><td>429.7</td><td>580</td><td>0.1092</td><td>0.7997</td></tr><tr><td>200</td><td>255.7</td><td>316.2</td><td>600</td><td>0.08070</td><td>0.6390</td></tr><tr><td>210</td><td>183.9</td><td>239.6</td><td>620</td><td>0.06012</td><td>0.5123</td></tr><tr><td>220</td><td>134.1</td><td>185.3</td><td>640</td><td>0.04519</td><td>0.4121</td></tr><tr><td>230</td><td>99.49</td><td>145.5</td><td>660</td><td>0.03430</td><td>0.3325</td></tr><tr><td>240</td><td>74.88</td><td>115.7</td><td>680</td><td>0.02632</td><td>0.2691</td></tr><tr><td>250</td><td>57.09</td><td>93.08</td><td>700</td><td>0.02043</td><td>0.2185</td></tr><tr><td>260</td><td>44.03</td><td>75.55</td><td>720</td><td>0.01607</td><td>0.1779</td></tr><tr><td>270</td><td>34.30</td><td>61.82</td><td>740</td><td>0.01281</td><td>0.1452</td></tr><tr><td>280</td><td>26.97</td><td>50.95</td><td>760</td><td>0.01036</td><td>0.1190</td></tr><tr><td>290</td><td>21.39</td><td>42.26</td><td>780</td><td>0.008496</td><td>0.09776</td></tr><tr><td>300</td><td>17.08</td><td>35.26</td><td>800</td><td>0.007069</td><td>0.08059</td></tr><tr><td>320</td><td>10.99</td><td>25.11</td><td>840</td><td>0.004680</td><td>0.05741</td></tr><tr><td>340</td><td>7.214</td><td>18.19</td><td>880</td><td>0.003200</td><td>0.04210</td></tr><tr><td>360</td><td>4.824</td><td>13.37</td><td>920</td><td>0.002210</td><td>0.03130</td></tr><tr><td>380</td><td>3.274</td><td>9.955</td><td>960</td><td>0.001560</td><td>0.02360</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>400</td><td>2.249</td><td>7.492</td><td>1000</td><td>0.001150</td><td>0.01810</td></tr></table>

# 3.5.3 The Jacchia 1971 Density Model

A number of different atmospheric density models have been published since 1965 by L. G. Jacchia (1965, 1970, 1971, 1977) and Jacchia & Slowey (1981). The first model, called J65, was solely based upon the primary parameters geodetic height and temperature, with the latter determining the atmospheric conditions. When further density-related data became available from the analysis of satellite accelerations due to drag, an improved atmospheric model was established (Jacchia 1971). The J71 model includes density variations as a function of time, and covers the altitude interval from $9 0 \mathrm { k m }$ to $2 5 0 0 \mathrm { k m }$ . It was adopted by the COSPAR (Committee on Space Research) working group as the International Reference Atmosphere in 1972, for heights ranging from $1 1 0 \mathrm { k m }$ to $2 0 0 0 \mathrm { k m }$ (see CIRA 1972).

In 1977 Jacchia published the atmospheric model J77 (Jacchia 1977), which was based upon measurements of the acceleration of satellites, and additionally upon analyses of mass spectrometer data. The J77 model was revised once more in 1981 (Jacchia et al. 1981).

All Jacchia models employ the exospheric temperature $T _ { \infty }$ as a basic parameter for the computation of the atmospheric density. The models are based upon the assumption that the chemical constituents of the atmosphere are in a state of mixing below heights of $1 0 0 \mathrm { k m }$ . The density for altitudes from 90 to $1 0 0 \mathrm { k m }$ is computed by integration of the barometric equation. At higher altitudes the atmosphere is assumed to be in diffusion equilibrium, where the constituents $\Nu _ { 2 }$ , $\mathrm { O } _ { 2 }$ , O, Ar, He and $\mathrm { H } _ { 2 }$ are taken into account. These two assumptions cause the Jacchia models to be static in nature. Therefore, temperature and density predictions will be poor when dynamical variations with time scales shorter than those typical for diffusion are present in the atmosphere. The densities from $1 0 0 \mathrm { k m }$ upwards are computed by integration of the differential equations for diffusion.

The J71 model offers a reasonable description of the atmospheric density at moderate computational expense, and is therefore widely used in the fields of orbit determination and prediction. The computation of atmospheric densities in the J71 model is performed in three steps:

1. The exospheric temperature $T _ { \infty }$ is computed from data on solar activity and from the geomagnetic index, in combination with a model of the diurnal variations in the atmosphere.   
2. Once $T _ { \infty }$ is known, a temperature profile is assumed, which is input for the integration of the barometric or diffusion equation (whichever is applicable). It is this integration in particular that turns out to be time-consuming. As an alternative, use is made of the coefficients of a bi-polynomial fit for the computation of the standard density values.   
3. Time-dependent corrections are applied to the density, which account for various observed density variations.

# Exospheric Temperature

In the J71 model, the minimum global exospheric temperature without solar radiation or geomagnetic activity is assumed to be $T _ { C } ~ = ~ 3 7 9 . 0 ^ { \circ }$ . The exospheric temperature with the effect of solar radiation included is given by

$$
T _ { C } = 3 7 9 . 0 ^ { \circ } + 3 . 2 4 ^ { \circ } \bar { F } _ { 1 0 . 7 } + 1 . 3 ^ { \circ } ( F _ { 1 0 . 7 } - \bar { F } _ { 1 0 . 7 } ) ,
$$

(Jacchia 1971), where $F _ { 1 0 . 7 }$ is the actual solar flux at $1 0 . 7 \mathrm { c m }$ , and $\bar { F } _ { 1 0 . 7 }$ the average solar flux (both measured in Solar Flux Units of $1 0 ^ { - 2 2 } \mathrm { W } / ( \mathrm { m } ^ { 2 } \mathrm { H z } ) )$ at this wavelength. In this model the actual flux is taken to be the average over the day before the date under consideration. The mean flux $\bar { F } _ { 1 0 . 7 }$ is found by taking an average over three solar rotations of 27 days. The last term in (3.106) thus represents daily variations around the mean global exospheric temperature.

The actual exospheric temperature is a function of local time or, in other words, depends on the local hour angle of the Sun with respect to the satellite. It also depends, however, on the declination of the Sun and the geographic latitude of the satellite. The actual exospheric temperature $T _ { 1 }$ with the diurnal variations included can be computed from

$$
T _ { 1 } = T _ { C } \left[ 1 + 0 . 3 \left( \sin ^ { 2 . 2 } | \theta | + ( \cos ^ { 2 . 2 } | \eta | - \sin ^ { 2 . 2 } | \theta | ) \cos ^ { 3 . 0 } \left( \frac { \tau } { 2 } \right) \right) \right] ~ ,
$$

(Jacchia 1971) with the angles $\tau$ $- 1 8 0 ^ { \circ } < \tau < + 1 8 0 ^ { \circ } ) , \theta , i$ $\eta$ given by

$$
\begin{array} { l } { { \tau \ = \ H - 3 7 . 0 ^ { \circ } + 6 . 0 ^ { \circ } \sin ( H + 4 3 . 0 ^ { \circ } ) } } \\ { { \ } } \\ { { \theta \ = \ \displaystyle \frac { 1 } { 2 } \ ( \varphi + \delta _ { \odot } ) } } \\ { { \eta \ = \ \displaystyle \frac { 1 } { 2 } \ ( \varphi - \delta _ { \odot } ) . } } \end{array}
$$

In these equations $\delta _ { \odot }$ denotes the Sun’s declination, $\varphi$ the geographic latitude and $H$ the local hour angle of the Sun with respect to the satellite. The additional terms in (3.108) which modify the hour angle $H$ , account for asymmetric effects in the temperature variation relative to the position of the Sun. The difference between the geographic and the geocentric latitude is always less than $1 2 ^ { \prime }$ and can therefore be neglected. The local hour angle $H$ is simply given by

$$
H = \alpha _ { \mathrm { S A T } } - \alpha _ { \odot } \quad ,
$$

where $\alpha _ { \mathrm { S A T } }$ and $\alpha _ { \odot }$ are the right ascension of the satellite and of the Sun respectively. Jacchia’s original representation (3.107) can further be amended by

$$
{ \begin{array} { r l r } { \sin ^ { 2 . 2 } \left( { \frac { | \alpha | } { 2 } } \right) } & { = } & { \left( { \frac { 1 } { 2 } } \left( 1 - \cos \alpha \right) \right) ^ { 1 . 1 } } \\ & { } & \\ { \cos ^ { 2 . 2 } \left( { \frac { | \alpha | } { 2 } } \right) } & { = } & { \left( { \frac { 1 } { 2 } } \left( 1 + \cos \alpha \right) \right) ^ { 1 . 1 } } \end{array} }
$$

to avoid the norm of the angles.

Geomagnetic activities are taken into account by using the three-hourly planetary geomagnetic index $K _ { p }$ for a time 6.7 hours earlier than the time under consideration (Jacchia 1971). The resulting change in exospheric temperature can be written as

$$
\begin{array} { r c l } { { \varDelta T _ { \infty } ^ { H } } } & { { = } } & { { 2 8 . 0 ^ { \circ } K _ { p } + 0 . 0 3 ^ { \circ } e ^ { K _ { p } } ( Z > 3 5 0 \mathrm { k m } ) } } \\ { { } } & { { } } & { { } } \\ { { \varDelta T _ { \infty } ^ { L } } } & { { = } } & { { 1 4 . 0 ^ { \circ } K _ { p } + 0 . 0 2 ^ { \circ } e ^ { K _ { p } } ( Z < 3 5 0 \mathrm { k m } ) } } \end{array}
$$

for high and low altitude $( Z )$ respectively. In order to retain continuity of the temperature correction at $3 5 0 \mathrm { k m }$ , Jacchia introduced a transition function $f$

$$
f = \frac { 1 } { 2 } ( \operatorname { t a n h } ( 0 . 0 4 ( Z - 3 5 0 \mathrm { k m } ) ) + 1 ) ~ .
$$

The temperature correction due to geomagnetic activity can then be written as

$$
\varDelta T _ { \infty } = f \varDelta T _ { \infty } ^ { H } + ( 1 - f ) \varDelta T _ { \infty } ^ { L } \quad .
$$

It should be noted that in the J71 model, geomagnetic perturbations affect the density in a twofold hybrid manner. Firstly, the temperature perturbations are directly reflected in the density and, secondly, an additional geomagnetic density correction term is added.

Finally, the full expression for the exospheric temperature, with solar and geomagnetic terms included, becomes

$$
T _ { \infty } = T _ { 1 } + \varDelta T _ { \infty } \quad ,
$$

which, together with the height $Z$ , determines the standard density values.

# Standard Density Computation

The standard Jacchia 1971 model is based upon an empirical temperature profile which starts from a fixed value $T _ { 0 } = 1 8 3 \mathrm { K }$ at $9 0 \mathrm { k m }$ . The temperature increases with altitude in a transition region until it reaches $T _ { \infty }$ asymptotically (Jacchia 1965). The standard density is obtained by integration of the barometric differential equation below $1 0 0 \mathrm { k m }$ and of the diffusion differential equation above this height. The molecular weights, and the fraction by volume of the atmospheric species nitrogen $( \mathrm { N } _ { 2 } )$ , oxygen $( \mathbf { O } _ { 2 } )$ , argon (Ar), and helium (He) at sea level, are input parameters to the model.

The Fortran source code provided in CIRA (1972) uses a Newton–Cotes fivepoint quadrature formula for the numerical integration of the individual constituent number densities. The advantage of this approach is that only few input data are necessary in order to get the full information content of the Jacchia model. The inherent drawback, however, is the computational effort, because each time a density is calculated, the equations must be integrated. It is estimated that more than $90 \%$ of the processing time is consumed by the computation of the standard density in this method. A graphical presentation of the J71 standard density as a function of altitude and exospheric temperature is given in Figure 3.13.

Considerable savings in processing time may be obtained by interpolating the standard density from precomputed tabular values or corresponding polynomials. A sophisticated bi-polynomial representation

$$
\log \rho ( Z , T _ { \infty } ) = \sum _ { i = 0 } ^ { 5 } \sum _ { j = 0 } ^ { 4 } c _ { i j } \left( \frac { Z } { 1 0 0 0 \mathrm { k m } } \right) ^ { i } \left( \frac { T _ { \infty } } { 1 0 0 0 \mathrm { K } } \right) ^ { j }
$$

of the standard density $\rho$ (in $[ \mathrm { k g } / \mathrm { m } ^ { 3 } ]$ ) as a function of height and exospheric temperature was developed by Gill (1996). It achieves a representative accuracy of $7 \%$ with coefficients $c _ { i j }$ given in Tables 3.9 and 3.10. The approximation is applicable within the altitude range $9 0 { - } 2 5 0 0 \mathrm { k m }$ and the temperature range $5 0 0 { - } 1 9 0 0 \mathrm { K }$ , which is divided into $4 \times 2$ subintervals. In order to ensure continuous density values and first-order derivatives at the sub-interval boundaries, the polynomial coefficients were obtained from a constrained least-squares fit that is described in detail in Gill (1996).

![](images/3d905981291dae3e2079f8c26f725e1aa735a2e01cbaf94579344b034980f0e0.jpg)  
Fig. 3.13. Logarithm of the standard density in the J71 model as a function of temperature and altitude

Density Corrections

In addition to the computation of the standard density, several density corrections have to be applied to account for various observed density variations. Below $3 5 0 \mathrm { k m }$ there is an additional geomagnetic term

$$
\begin{array} { r } { \varDelta \log \rho _ { \mathrm { G M } } = \left( 0 . 0 1 2 K _ { p } + 1 . 2 { \cdot } 1 0 ^ { - 5 } e ^ { K _ { p } } \right) ( 1 - f ) } \end{array}
$$

as part of the hybrid Jacchia geomagnetic algorithm.

The semi-annual density variation in the thermosphere and the lower exosphere is only considered by temperature corrections in the Jacchia 1965 model. Large discrepancies with this model were found, however, when actual data of the drag force on satellites became available. This forced Jacchia to the assumption that those density variations are not primarily caused by variations in temperature. Hence, an empirical relationship

$$
\varDelta \log \rho _ { \mathrm { S A } } = f ( Z ) g ( t )
$$

for the density correction was assumed, where $g ( t )$ represents the temporal variation, and $f ( Z )$ is the amplitude of the density variation at a given altitude. A best fit to the available data was found with the functions

$$
\begin{array} { r c l } { { f ( Z ) } } & { { = } } & { { \left( 5 . 8 7 6 \cdot 1 0 ^ { - 7 } ( Z / \mathrm { k m } ) ^ { 2 . 3 3 1 } + 0 . 0 6 3 2 8 \right) e ^ { ( - 0 . 0 0 2 8 6 8 Z / \mathrm { k m } ) } } } \\ { { } } & { { } } & { { } } \\ { { g ( t ) } } & { { = } } & { { 0 . 0 2 8 3 5 + } } \\ { { } } & { { } } & { { ( 3 . 1 7 \cdot 0 . 1 7 8 2 9 \sin ( 2 \pi \tau _ { \mathrm { S A } } + 4 . 1 3 7 ) ) \times \sin ( 4 \pi \tau _ { \mathrm { S A } } + 4 . 2 5 9 ) ~ . } } \end{array}
$$

Table 3.9. Coefficients $c _ { i j }$ of Jacchia 1971 standard density polynomials in temperature (index $j$ ) and height (index $i$ ) below $5 0 0 \mathrm { k m }$   

<table><tr><td colspan="5">90 km&lt;Z&lt;180km 500K&lt;To&lt;850K</td></tr><tr><td>0</td><td></td><td>1 2</td><td>3</td><td>4</td></tr><tr><td>i 0</td><td>-0.3520856:10² +0.3912622.101</td><td></td><td>1-0.8649259.10² +0.1504119.10</td><td>-0.7109428.102</td></tr><tr><td>1</td><td>+0.1129210.104 +0.1198158.104</td><td>+0.8633794.103</td><td>-0.3577091.104</td><td>+0.1970558.104</td></tr><tr><td>2</td><td>-0.1527475.105 -0.3558481.105</td><td>+0.1899243.105</td><td>+0.2508241.105</td><td>-0.1968253.105</td></tr><tr><td>3</td><td>+0.9302042.105 +0.3646554.106</td><td>-0.3290364.106</td><td>-0.1209631·105</td><td>+0.8438137.105</td></tr><tr><td>4</td><td>-0.2734394.106 -0.1576097.107</td><td>+0.1685831-107</td><td>-0.4282943.106</td><td>-0.1345593.106</td></tr><tr><td>5</td><td>+0.3149696.106 +0.2487723.107 -0.2899124.107 +0.1111904-107 +0.3294095.104</td><td></td><td></td><td></td></tr><tr><td>90 km&lt;Z&lt;180km</td><td></td><td>850K&lt;T&lt;1900K</td><td></td><td></td></tr><tr><td colspan="5"></td></tr><tr><td>ij</td><td>0 1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>-0.5335412.10² +0.2900557.102</td><td>2-0.2046439.102+0.7977149.101</td><td></td><td>-0.1335853.101</td></tr><tr><td>1</td><td>+0.1977533.104 -0.7091478.10² +0.4398538·103</td><td></td><td>-0.1568720.103</td><td>+0.2615466.102</td></tr><tr><td>2</td><td>-0.2993620.105 +0.5187286-104 -0.1989795.104</td><td></td><td></td><td>+0.3643166:103 -0.5700669.102</td></tr><tr><td>3</td><td>+0.2112068.106 -0.4483029.104</td><td>-0.1349971.105</td><td>+0.9510012.104</td><td>-0.1653725.104</td></tr><tr><td>4</td><td>-0.7209722.106-0.7684101:105</td><td></td><td></td><td>+0.1256236-106-0.6805699.105 +0.1181257.105</td></tr><tr><td>5</td><td>+0.9625966.106 +0.2123127-106-0.2622793.10+0.1337130.106 -0.2329995.105</td><td></td><td></td><td></td></tr><tr><td></td><td>180km&lt;Z&lt;500km</td><td>500K&lt;To&lt;850K</td><td></td><td></td></tr><tr><td>ij 0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>+0.2311910·102 +0.1355298:103 -0.8424310·103 +0.1287331-104 -0.6181209.103</td><td></td><td></td><td></td></tr><tr><td>1</td><td>-0.1057776.104 +0.6087973.103</td><td></td><td>+0.8690566.104 -0.1715922.105</td><td>+0.9052671.104</td></tr><tr><td>2</td><td>+0.1177230.105 -0.3164132.105</td><td>-0.1076323-104</td><td>+0.6302629.105</td><td>-0.4312459.105</td></tr><tr><td>3</td><td>-0.5827663.105 +0.2188167.106-0.2422912.106 +0.2461286.105 +0.6044096.105</td><td></td><td></td><td></td></tr><tr><td>4</td><td>+0.1254589.106 -0.5434710.106 +0.8123016.106 -0.4490438·106 +0.5007458.105</td><td></td><td></td><td></td></tr><tr><td>5</td><td>-0.9452922.105 +0.4408026:106 -0.7379410.106 +0.5095273:106-0.1154192.106</td><td></td><td></td><td></td></tr><tr><td></td><td>180km&lt;Z&lt;500km</td><td>850K&lt;To&lt;1900K</td><td></td><td></td></tr><tr><td>i</td><td>0 1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>+0.4041761.10² -0.1305719.10 +0.1466809.10 -0.7120296:10² +0.1269605.10²</td><td></td><td></td><td></td></tr><tr><td>1</td><td>-0.8127720.103 +0.2273565:104 -0.2577261-104 +0.1259045:104 -0.2254978·103</td><td></td><td></td><td></td></tr><tr><td>2</td><td>+0.5130043.104</td><td>-0.1501308:105+0.1717142.105</td><td>-0.8441698.104 +0.1518796.104</td><td></td></tr><tr><td>3</td><td>-0.1600170.105 +0.4770469·10 -0.5473492.105 +0.2699668.105</td><td></td><td></td><td>-0.4870306.104</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>+0.2384718.105 -0.7199064:10 +0.8284653.105 -0.4098358.105 +0.7411926.104</td><td></td><td></td><td></td></tr><tr><td>5</td><td>-0.1363104.105 +0.4153499.105 -0.4793581-105 +0.2377854-105 -0.4310233·104</td><td></td><td></td><td></td></tr></table>

Here the time-dependent parameter is

$$
\tau _ { \mathrm { { S A } } } = \phi + 0 . 0 9 5 4 4 \left\{ \left( { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } } \sin ( 2 \pi \phi + 6 . 0 3 5 ) \right) ^ { 1 . 6 5 } - { \frac { 1 } { 2 } } \right\}
$$

with

$$
\Phi = { \frac { ( t - 3 6 2 0 4 ) } { 3 6 5 . 2 4 2 2 } } ~ .
$$

In equation (3.120), $t$ is the time expressed in Modified Julian Days $\mathrm { ( M J D ~ = ~ }$ $\mathrm { J D } - 2 4 0 0 0 0 0 . 5$ . Hence, $\phi$ is the number of tropical years since January 1, 1958. The maximum semi-annual density correction is $\varDelta \log \rho ^ { \mathrm { m a x } } \vert _ { \mathrm { S A } } \approx 0 . 2 1$ .

Table 3.10. Coefficients $c _ { i j }$ of Jacchia 1971 standard density polynomials in temperature (index $j$ ) and height (index $i$ ) above $5 0 0 \mathrm { k m }$   

<table><tr><td colspan="5"></td></tr><tr><td colspan="5">500km&lt;Z&lt;1000km 500K&lt;To&lt;850K 1</td></tr><tr><td></td><td>0</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>-0.1815722:104 +0.9792972.104 -0.1831374.105</td><td>+0.9993169.105</td><td>+0.1385255.105 -0.7259456.105</td><td>-0.3451234.104 +0.1622553·105</td></tr><tr><td>1</td><td>+0.9851221.104 -0.5397525.105 -0.1822932.105 +0.1002430.106</td><td>-0.1784481.106</td><td>+0.1145178.106</td><td>-0.1641934.105</td></tr><tr><td>2</td><td>+0.1298113:105 -0.7113430.105 +0.1106375:106-0.3825777-105</td><td></td><td></td><td>-0.1666915.105</td></tr><tr><td>3 4</td><td>-0.1533510.104 +0.7815537-104</td><td>+0.7037562.104 -0.4674636.105</td><td></td><td>+0.3516949.105</td></tr><tr><td>5</td><td>-0.1263680.104 +0.7265792.104 -0.2092909.105 +0.2936094.105 -0.1491676·105</td><td></td><td></td><td></td></tr><tr><td colspan="5">500km&lt;Z&lt;1000km 850K&lt;To&lt;1900K</td></tr><tr><td></td><td colspan="4">0 1 2 3 4</td></tr><tr><td>0</td><td>-0.4021335.102 -0.1326983:103</td><td>+0.3778864.103 -0.2808660.103</td><td></td><td>+0.6513531.102</td></tr><tr><td>1</td><td>+0.4255789.103 -0.1821662:104 +0.7905357.10 +0.3934271.104 -0.3969334.104</td><td>+0.3528126-103 -0.2077888·104 +0.1726543.104</td><td></td><td>-0.4191477.103 +0.1027991.104</td></tr><tr><td>2</td><td>+0.3070231:104</td><td>-0.2941540.104 -0.3276639.104</td><td>+0.4420217.104</td><td>-0.1230778.104</td></tr><tr><td>3 4</td><td>-0.2196848.104 +0.2585118.104 +0.1382776:104 -0.2533006:104</td><td></td><td></td><td>+0.7451387.103</td></tr><tr><td>5</td><td>+0.5494959.103 -0.6604225.103 -0.3328077-103 +0.6335703.103 -0.1879812.103</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>500K&lt;To&lt;850K</td><td></td><td></td></tr><tr><td colspan="5">1000 km&lt; Z&lt;2500km 0</td></tr><tr><td>i</td><td>1</td><td>2 -0.2508685-104 +0.6252742.104 -0.6755376.104 +0.2675763·104</td><td>3</td><td>4</td></tr><tr><td>0 1</td><td>+0.3548698.103 -0.5370852.103</td><td>+0.4182586:104 -0.1151114.105 +0.1338915:105</td><td></td><td>-0.5610580.104</td></tr><tr><td>2</td><td>-0.2349586.10²</td><td>-0.8941841:103 +0.4417927:104 -0.6732817-104</td><td></td><td>+0.3312608.104</td></tr><tr><td>3</td><td>+0.3407073.103 -0.1531588.104</td><td>+0.2179045-104 -0.8841341:103</td><td></td><td>-0.1369769.103</td></tr><tr><td>4</td><td>-0.1698471·10 +0.8985697.103</td><td>3-0.1704797.104 +0.1363098.104</td><td></td><td>-0.3812417-103</td></tr><tr><td>5</td><td>+0.2497973.102 -0.1389618.103</td><td>+0.2820058-10 -0.2472862.10 +0.7896439.102</td><td></td><td></td></tr><tr><td></td><td>1000km&lt;Z&lt;2500km</td><td>850K&lt;To&lt;1900K</td><td></td><td></td></tr><tr><td></td><td colspan="4">0 1 2 3</td></tr><tr><td>0</td><td colspan="4">+0.1281061:102 -0.3389179.103 +0.6861935:103 -0.4667627.103</td></tr><tr><td>1</td><td>+0.2024251.103</td><td>+0.1668302.103-0.1147876.104</td><td>+0.9918940.103</td><td>+0.1029662.103 -0.2430215.103</td></tr><tr><td>2</td><td>-0.5750743.103 +0.8259823.103</td><td>+0.2329832.103</td><td>-0.6503359.103</td><td>+0.1997989.103</td></tr><tr><td></td><td>+0.5106207-10 -0.1032012.104 +0.4851874.10</td><td></td><td>+0.8214097.102</td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td>-0.6527048.102</td></tr><tr><td>4</td><td>-0.1898953:10² +0.4347501:10 -0.2986011:10 +0.5423180.10²</td><td></td><td></td><td>+0.5039459.101</td></tr><tr><td></td><td>+0.2569577:102 -0.6282710.102 +0.4971077-102-0.1404385.10²</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>+0.8450500-100</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

So far, the model gives a constant density over the globe at $9 0 \mathrm { k m }$ . This contradicts observations of density variations below $1 2 0 \mathrm { k m }$ , which indicate a seasonallatitudinal density dependence with a maximum amplitude at $Z \approx 1 1 0 \mathrm { k m }$ . In terms of the latitude, $\varphi$ , and the deviation from the reference height, $\Delta Z _ { 9 0 } = Z - 9 0 \mathrm { k m }$ , the deviation in density can be written as

$$
\left. \Delta \log \rho _ { \mathrm { S L } } = 0 . 0 1 4 \Delta Z _ { 9 0 } e ^ { ( - 0 . 0 0 1 3 \Delta Z _ { 9 0 } ^ { 2 } ) } \sin ( 2 \pi \phi + 1 . 7 2 ) \frac { \sin ^ { 3 } \varphi } { \mid \sin \varphi \mid } \right. \ .
$$

In a computer application $\sin ^ { 3 } \varphi / | \sin \varphi |$ should be replaced by $\mathtt { S I G N } ( \sin ^ { 2 } \varphi , \varphi )$ .

A strong increase of the helium concentration above the winter pole has been found from mass-spectrometer data, as well as from satellite drag data. This phenomenon is accounted for in the Jacchia 1971 model by an empirical seasonallatitudinal correction

$$
\varDelta \log n _ { \mathrm { H e } } = 0 . 6 5 \left| \frac { \delta _ { \odot } } { \epsilon } \right| \left( \sin ^ { 3 } \left( \frac { \pi } { 4 } - \frac { \varphi } { 2 } \frac { \delta _ { \odot } } { | \delta _ { \odot } | } \right) - 0 . 3 5 3 5 5 \right)
$$

to the helium number density $n _ { \mathrm { H e } }$ (in $[ 1 / \mathrm { m } ^ { 3 } ] ,$ ), where $\epsilon$ is the obliquity of the ecliptic. The maximum helium density contribution to the standard density is given by $\begin{array} { r } { \varDelta \log \rho _ { \mathrm { H e } } ^ { \mathrm { m a x } } \approx 0 . 8 8 . } \end{array}$ It is straightforward to compute this correction from the integration of the diffusion equation, which yields the number density of the individual species. However, a standard density computation from tabular data now requires additional table values for the helium number density as a function of altitude and of exospheric temperature.

Therefore, a polynomial approximation, similar to the one for the standard density, is also made for the helium density. To this end the helium density correction is written as

$$
\varDelta \rho _ { \mathrm { H e } } = 1 0 ^ { \log n _ { \mathrm { H e } } } \frac { m _ { \mathrm { H e } } } { A _ { v } } \left( 1 0 ^ { \varDelta \log n _ { \mathrm { H e } } } - 1 \right)
$$

with the helium number density

$$
\log n _ { \mathrm { H e } } ( Z , T _ { \infty } ) = \sum _ { i = 0 } ^ { 5 } \sum _ { j = 0 } ^ { 4 } h _ { i j } \left( \frac { Z } { \mathrm { k m } } \right) ^ { i } \left( \frac { T _ { \infty } } { \mathrm { K } } \right) ^ { j } \quad ,
$$

the helium molecular weight $m _ { \mathrm { H e } } = 4 . 0 0 2 6$ , and the number of Avogadro $A _ { v }$ . Coefficients $h _ { i j }$ for a smooth and continuous approximation of the helium number density as derived by Gill (1996) are collated in Table 3.11.

# 3.5.4 A Comparison of Upper Atmosphere Density Models

Only after the advent of the space age, with the launch of the Sputnik satellite in 1957, could information on the physical properties of the upper atmosphere above $1 5 0 \mathrm { k m }$ be deduced. In particular, atmospheric densities can be derived from the evolution and decay of the satellite orbits, assuming a given drag coefficient. This method was primarily used for the density model development up to the mid seventies. Its inherent drawback is, however, that only integrated drag effects over several orbit revolutions may be resolved from orbit determination, and thus the method is restricted to a limited spatial and temporal resolution. Its benefit, on the other hand, is that density models derived from these observations can consistently be applied to other space missions, being free from any further instrument calibration.

Rapid developments in satellite and ground system instrumentation considerably improved the knowledge of detailed atmospheric properties in the seventies. The use of spacecraft accelerometers directly monitored the non-inertial forces acting on the satellite. Mass spectrometers were integrated into the satellite hardware that produced in-situ measurements of the chemical composition and temperature at upper atmospheric altitudes. Incoherent radar scattering techniques from groundbased antennas provided measurements of atmospheric electron and ion properties that could be related to the neutral atmospheric density and composition. More recent atmospheric models, such as the J77 model, or the series of MSIS (Mass Spectrometer and Incoherent Scatter) models, make extensive use of those data. The spatial and temporal resolution of these models is therefore high, at the cost of increased complexity and CPU time.

Table 3.11. Coefficients $h _ { i j }$ of Jacchia 1971 logarithmic helium number density polynomials in temperature (index $j$ ) and height (index $i$ )   

<table><tr><td colspan="5">90km&lt;Ｚ&lt;500km</td></tr><tr><td>ij</td><td>0 1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td colspan="4">+1.831549.10+01 +5.887556.10-03-4.813257-10-06 +1.701738.10-09-2.128374-10-13 -7.374008.10-02-1.251077.10-04 +1.039269.10-07 -3.679280.10-11 +4.555258:10-15</td></tr><tr><td>1</td><td colspan="4">+4.384164.10-04 +8.657027.10-07-7.216946.10-10 +2.481534.10-13-2.859074.10-17</td></tr><tr><td>２３４5</td><td colspan="4">-1.411195:10-06-2.483834.10-09 +2.004107.10-12-6.244985.10-16 +5.561004.10-20 +2.153639.10-09 +3.421944.10-12-2.628961.10-15 +7.085655.10-193.279804-10-23 -1.255139.10-12 -1.827253.10-15 +1.321581.10-18 -2.887398.10-22 -7.827178.10-27</td></tr><tr><td></td><td colspan="4">500km&lt; Z&lt;1000km</td></tr><tr><td>ij</td><td colspan="4">0 1 2 3 4 +1.627089.10+01 -1.786816.10-02 +3.079079.10-05 -2.043431.10-08 +4.643419.10-12</td></tr><tr><td>0 1 24</td><td colspan="4">-1.958297.10-02 +1.386126.10-04 -2.532463.10-07 +1.714183.10-10 -3.934230.10-14 +2.514251-10-05-3.806339.10-07+7.692376:10-10-5.394766:10-13 +1.260304.10-16 -2.983314.10-08 +5.855851-10-10 -1.210663.10-12 +8.561632.10-16 -2.009030.10-19 +1.802028:10-11 -4.382878.10-13 +9.201530.10-16 -6.543935.10-19 +1.540220.10-22</td></tr><tr><td>5</td><td colspan="4">-4.243067.10-15 +1.268830.10-16 -2.695807.10-19 +1.925469.10-22 -4.542329.10-26 1000km&lt; Z&lt;2500km</td></tr><tr><td></td><td colspan="4">0 1 2 3 4</td></tr><tr><td>四</td><td colspan="4">+1.873346:10+01 +2.285683.10-02 -6.860776:10-05 +5.379623.10-08-1.327559.10-11</td></tr><tr><td>0</td><td colspan="4">-2.362530.10-02 -6.907613.10-05 +2.251680.10-07 -1.795937.10-10 +4.463659.10-14</td></tr><tr><td>1</td><td colspan="4"></td></tr><tr><td></td><td colspan="4">+1.893899.10-05 +1.145960.10-07 -3.183259.10-10 +2.461076.10-13 -6.040423.10-17</td></tr><tr><td>2</td><td colspan="4">-1.132198.10-08-7.438326.10-11 +2.040288.10-13-1.573191.10-16 +3.857032.10-20</td></tr><tr><td>4</td><td colspan="4">+3.465014.10-12 +2.308943.10-14 -6.320466.10-17 +4.871419.10-20 -1.194139.10-23 -4.156710.10-16 -2.791930.10-18 +7.632792.10-21 -5.881112.10-24 +1.441455.10-27</td></tr></table>

Apart from the well-known and frequently applied J71 model, a variety of other density models of the upper atmosphere exists. These range from very simple, easy to implement algorithms to elaborate theories, which either require much CPU time, or refer to a large number of numerical coefficients. A brief summary of the various models is given in this section, and a comparison is made in terms of computation time and of relative density difference with respect to the original J71 model provided in CIRA (1972).

The Jacchia–Roberts model of the atmosphere (Roberts 1971) was originally derived from J70. Later on it was modified according to J71 (Long et al. 1989). Roberts’ method is based upon analytical solutions of the barometric and diffusion differential equations, which are obtained by integration of partial fractions. The original Jacchia temperature profile (exospheric temperature computed as in J70) is used between 90 and $1 2 5 \mathrm { k m }$ . Above $1 2 5 \mathrm { k m }$ a different temperature profile is assumed, which results in a diffusion equation that can be integrated analytically. Hence, Roberts’ results match Jacchia’s exactly between 90 and $1 2 5 \mathrm { k m }$ , and are in close agreement above $1 2 5 \mathrm { k m }$ . The mean relative difference in density and the maximum relative differences with respect to J71 are $1 \%$ and $3 \%$ respectively. According to Long et al. (1989) the maximum density difference amounts to $6 . 7 \%$ . This demonstrates the close agreement between both models. The CPU performance is better by a factor of almost five compared to J71, as can be seen from Table 3.12. The advantage of the Roberts model is that numerical integration is avoided, and storage of a large number of coefficients is also unnecessary. At the same time the computational speed is good.

Table 3.12. Comparison of density models. Relative CPU time performance, mean, and maximum difference in density relative to J71   

<table><tr><td rowspan=1 colspan=1>Model</td><td rowspan=1 colspan=1>CPU</td><td rowspan=1 colspan=1>△pmean</td><td rowspan=1 colspan=1>△pmax</td></tr><tr><td rowspan=2 colspan=1>Jacchia71Jacchia-Roberts</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>0.22</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.03</td></tr><tr><td rowspan=2 colspan=1>Jacchia-LineberryJacchia-Gill</td><td rowspan=1 colspan=1>0.43</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>0.35</td></tr><tr><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.08</td></tr><tr><td rowspan=1 colspan=1>Jacchia 77</td><td rowspan=1 colspan=1>10.69</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>0.35</td></tr><tr><td rowspan=1 colspan=1>Jacchia-Lafontaine</td><td rowspan=1 colspan=1>0.86</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>0.36</td></tr><tr><td rowspan=1 colspan=1>MSIS 77</td><td rowspan=1 colspan=1>0.06</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>0.53</td></tr><tr><td rowspan=1 colspan=1>MSIS 86</td><td rowspan=1 colspan=1>0.32</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>1.45</td></tr><tr><td rowspan=1 colspan=1>TD88</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.91</td><td rowspan=1 colspan=1>7.49</td></tr><tr><td rowspan=1 colspan=1>DTM</td><td rowspan=1 colspan=1>0.03</td><td rowspan=1 colspan=1>0.40</td><td rowspan=1 colspan=1>1.22</td></tr></table>

The Jacchia–Lineberry model (Mueller 1982) assumes that the logarithm of the density can be computed as a truncated Laurent series in temperature and altitude. The altitude is split into nine intervals at most, and the necessary number of coefficients in this model is about a hundred. However, the seasonal-latitudinal helium variation is not included. Density differences between the Jacchia–Lineberry model and J71 are typically $13 \%$ , and the gain in computational speed is moderate.

The model of Jacchia–Gill (Gill 1996), as described above, uses a bi-polynomial approximation of the Jacchia 1971 standard density model. It is based upon polynomials of $4 ^ { \mathrm { t h } }$ order in temperature and of $5 ^ { \mathrm { t h } }$ degree in altitude. The temperature interval from 500 to $1 9 0 0 \mathrm { K }$ and the altitude interval from 90 to $2 5 0 0 \mathrm { k m }$ are divided into eight sections, each with its own bi-polynomial fit. A continuous transition between the several height intervals is ensured by the use of a constrained least-squares fit. The helium number density is obtained in a similar way. The total number of coefficients required in the Jacchia–Gill model is 330. Typical differences with J71 are $2 \%$ and the maximum deviation is $8 \%$ . The computing time is reduced by a factor of nine.

In 1977 Jacchia published an updated atmosphere model, J77, which was revised once more in 1981 (Jacchia et al. 1981). These models are based upon measurements of satellite acceleration and, additionally, upon analyses of mass spectrometer data. Similar to the older Jacchia models a physical description of the upper atmosphere with regard to satellite drag is attempted by the integration of the barometric and diffusion equations. However, a greater complexity is introduced through a species-dependent pseudo-temperature in order to account for the fact that the density of different constituents peaks at different hours of the day. Furthermore, the mean solar flux is replaced by a weighted mean value which is centered around the epoch. Finally, the time at which the $K _ { p }$ index is required is corrected for the geomagnetic latitude of the satellite position. These extensions make the model significantly more complex. This is of course directly reflected in the CPU time, which is ten times higher than for the J71 model. Yet, the J77 model does not significantly improve the accuracy of density modeling for satellite orbit prediction and determination.

Modifications of the temperature profile at low altitudes in the J77 model, as compared to the J70 and J71 models, caused Roberts’ approach to be no longer applicable. This situation was resolved by de Lafontaine & Hughes (1983). They modified Jacchia’s temperature profile below $1 2 5 \mathrm { k m }$ and extended Roberts’ exponential temperature profile above $1 2 5 \mathrm { k m }$ in order to obtain an analytical version of the J77 model. Their approach is more general than Roberts’ method and it is not restricted to the J77 model, but can also be applied to the J70 and J71 models. The computational efficiency is considerably better than that of the original J77 formulation and, in contrast to Roberts’ method, continuity of the first derivative of the density is guaranteed for all exospheric temperatures. The mean and maximum deviations relative to the J71 density are $13 \%$ and $36 \%$ respectively.

A different class of models was published in papers by A. E. Hedin. These models are entirely based upon in-situ data from satellites and sounding rockets, as well as incoherent scatter measurements. The first model was published in 1977 by Hedin et al. and is known as MSIS-77 (Mass Spectrometer and Incoherent Scatter). When more data became available, this model was upgraded yielding MSIS-83 (Hedin 1983) and MSIS-86 (Hedin 1987) models. The latter model was adopted as the CIRA 1986 reference atmosphere. MSIS-86 is based on a complex function, which has to be evaluated to compute the density, as well as other atmospheric quantities. More than 850 coefficients have to be provided, which, in turn, allows a detailed modeling of the complex atmospheric properties.

Barlier et al. (1978) published the thermospheric density model, DTM, which is based upon total density data derived from satellite drag observations. An expansion in terms of spherical harmonics is performed for the exospheric temperature and for the density of the main atmospheric constituents helium, atomic oxygen, and nitrogen comprising up to terdiurnal and semi-annual terms. The total density depends in a simple analytical form upon the altitude and is obtained from the integration of the diffusion equation with an empirical temperature profile. About 150 parameters are required for the evaluation of the model, which requires extremely little computer time. However, very high density differences of typically $40 \%$ relative to the J71 model are found. The maximum difference lies at $123 \%$ .

The simple atmospheric model TD88 was derived by Sehnal & Pospíšilová (1988) mainly by fitting an analytical series of exponential functions in height and of trigonometric functions in time to the density values from the DTM model. The resulting model requires only 40 parameters and is according to Sehnal applicable for altitudes between 150 and $7 5 0 \mathrm { k m }$ . Compared to the performance of J71 a runtime gain of a factor of a hundred is obtained. The density differences, however, seem to be unacceptably high, lying on the average at $91 \%$ . In Table 3.12 the maximum density deviation of $74 \%$ with respect to J71 was due to an evaluation at $1 3 0 \mathrm { k m }$ altitude, which is just outside the validity interval of the model given by Sehnal.

There have been a number of publications which analyze and compare the performance of different density models (e.g. Gaposchkin & Coster 1990, Marcos et al. 1989). The conclusion is that the models have statistical accuracies of about $1 5 \%$ and that there has been no significant improvement in density models over the last two decades. The profit achieved by the application of complex atmosphere models in the field of satellite orbit determination and prediction is therefore questionable. It appears fully justified to select density models with a moderate complexity only, which essentially minimize the computational effort and coefficient storage requirements.

# 3.5.5 Prediction of Solar and Geomagnetic Indices

Low-Earth satellite orbits are severely affected by atmospheric drag, which strongly varies with the solar flux and geomagnetic activity. While the measured solar and geomagnetic activity indices can be applied in orbit determination, orbit forecasts have to rely on predictions of these parameters. Short-term to mid-term predictions are required for spacecraft operations, especially for ground station scheduling and maneuver planning of low-Earth satellites. In particular, remote sensing missions require the control of orbit equator crossings within specified equatorial longitude bands, which are maintained by orbit raising or lowering maneuvers. Hence, the orbit maneuver schedule depends on the evolution of the semi-major axis within periods of typically some weeks, while the semi-major axis evolution itself is governed by the evolution of the solar and geomagnetic flux in that time frame. Long-term predictions of the solar and geomagnetic flux, on the other hand, are important for mission planning and analysis. The knowledge of the profile and magnitude of the next solar cycle, for example, is crucial for the logistic planning of the assembly of the International Space Station. Furthermore, mission planning requires long-term forecasts for estimates of the expected satellite lifetime.

It is therefore adequate to distinguish three different time scales for solar and geomagnetic index forecast, namely

1. Short-term predictions (days)   
2. Mid-term predictions (months)   
3. Long-term forecasts (years)

![](images/b9e3919224ffca7964a7e9eccdf0611aa8942245de60e51b66fc53e298ac731f.jpg)  
Fig. 3.14. Short-term variation of solar flux values due to solar rotation

each of which may apply mathematical methods or physical models or a combination thereof as forecast algorithms.

Short-term predictions have to account for the 27-day periodicity of the solar activity that results from the synodic solar rotation with this period (Fig. 3.14). The periodic variation in the $F _ { 1 0 . 7 }$ index may be forecasted using a regression algorithm (Nostrand 1984) that compares the long-term trend from three solar rotations with a recent trend from the past three days. Supposing that the two trends are directed opposite, the prediction follows the recent trend with a later regression towards the long-term trend. This method assures that the predicted values evolve smoothly from the observed values and it leads to a particularly good prediction accuracy for the first 7–10 days (Frauenholz & Shapiro 1991).

Mathematical methods are in general applied to mid-term predictions. The linear-regression technique of McNish & Lincoln (1949) makes use of the relation between the solar flux $F _ { 1 0 . 7 }$ values and the sunspot numbers to compute a mean solar cycle. This approach considerably improves the database, since $F _ { 1 0 . 7 }$ data are available only from 1947 onwards, whereas the first sunspot numbers date back to 1749. Departures of the current cycle from the mean cycle are then based on the assumption that they are related to deviations of the previous cycle from the mean cycle (Mugellesi & Kerridge 1991). This method provides monthly smoothed $F _ { 1 0 . 7 }$ values and can correspondingly be applied to geomagnetic index predictions. The drawback of this method is that the prediction accuracy deteriorates with increasing forecast periods and that no understanding of the involved physical mechanisms is achieved.

The long-term evolution of solar flux values is governed by the 11-year solar cycle as depicted in Fig. 3.15. Among various prediction methods, the precursor models have shown the best performance. Here, it is assumed that the solar cycle actually starts in the declining phase of the previous cycle, where the next cycle manifests itself in the occurrence of coronal holes and the strength of the polar magnetic field of the Sun. According to the solar dynamo model, the Sun’s polodial magnetic field at solar minimum is transformed by differential rotation to a toroidal field that gives rise to phenomena such as sunspot numbers and solar activity for the next cycle (Schatten et al. 1978, Schatten & Pesnell 1993). Although the model allows a physical connection between the Sun’s polar magnetic field, and coronal holes, as well as solar and geomagnetic activity, a drawback of this method is that the Sun’s polar magnetic field is difficult to measure and that the assumed physical model might be oversimplified.

![](images/5d24aa8568c8ff0dfdd8332c01cf1c59bb1f72379b2cf9f0f0a1c99753d84885.jpg)  
Fig. 3.15. Monthly averages of the solar flux for solar cycles 20–23. Predicted average values and $\pm 2 \sigma$ uncertainties in the predicted average are due to Schatten (1999).

# 3.6 Thrust Forces

Aside from the natural forces discussed so far, the motion of a spacecraft may also be affected by the action of an onboard thruster system. Thrusters are frequently applied for orbit control, attitude control, or a combination of both, and exhibit a variety of performance levels (cf. Table 3.13) and burn durations. In view of a significant impact on the spacecraft orbit, thrust forces must be taken into account in the trajectory prediction using an adequate mathematical model. In turn, thruster and maneuver parameters may be calibrated by adjusting them along with other parameters in an orbit determination.

While attitude thrusters are ideally burned in pairs to produce a pure momentumfree torque, changes in the shape and orientation of the orbit are accomplished by thrusters acting primarily in the along-track and cross-track directions. In the case of orbital maneuvers the overall thruster activity is generally confined to a finite time interval, ranging from seconds or minutes for ground track control of remote sensing satellites to several hours for inclination control of geostationary satellites with ionic propulsion. Whereas maneuvers may conveniently be treated as instantaneous velocity increments

Table 3.13. Representative values of the thrust level, the ejection velocity, the specific impulse $( I _ { \mathrm { s p } } = v _ { \mathrm { e } } / 9 . 8 1 \mathrm { m } / \mathrm { s } ^ { 2 } )$ , and the mass flow rate for various thrust systems   

<table><tr><td>Propulsion system</td><td>F</td><td>Ue</td><td>1sp</td><td>|m|</td></tr><tr><td>Solid propellant boost motor Liquid propellant boost motor</td><td>40kN</td><td>3000 m/s</td><td>300 s</td><td>1.3 kg/s</td></tr><tr><td rowspan="2">Station keeping thruster</td><td>400 N</td><td>3500 m/s</td><td>350 s</td><td>130 g/s</td></tr><tr><td>10N</td><td>3500 m/s</td><td>350 s</td><td>3g/s</td></tr><tr><td>Ion thruster</td><td>20mN</td><td>25 km/s</td><td>2500 s</td><td>0.8 mg/s</td></tr></table>

$$
v ( t _ { \mathrm { m } } ^ { + } ) = v ( t _ { \mathrm { m } } ^ { - } ) + \varDelta v ( t _ { \mathrm { m } } )
$$

occurring at the impulsive maneuver time $t _ { \mathrm { m } }$ whenever the thrust duration is small as compared to the orbital period, an adequate thrust model is required for extended maneuvers. This is particularly true for orbital transfers with large boost maneuvers that are applied e.g. in the positioning of geostationary satellites (see Fig. 2.4). Here, a substantial amount of propellant is consumed during a single maneuver, which results in a continuous change of the spacecraft mass along the burn.

Despite the variety of spacecraft propulsion systems, a simple, constant thrust model is often sufficient to describe the motion of a spacecraft during thrust arcs. The model described in the sequel is applicable to most types of extended orbit maneuvers ranging from high-thrust orbital transfer maneuvers to low-thrust orbit corrections. To ensure compatibility with commonly employed impulsive maneuver models, a formulation in terms of velocity increments is chosen.

Under the action of a propulsion system which ejects a mass $| d m | = | { \dot { m } } | d t$ of propellant per time interval $d t$ at a velocity $v _ { \mathrm { e } }$ , a spacecraft of mass m experiences a thrust

$$
F = | \dot { m } | v _ { \mathrm { e } }
$$

which results in an acceleration

$$
a = \frac { F } { m } = \frac { | \dot { m } | } { m } v _ { \mathrm { e } } .
$$

Upon integration over the burn time $\varDelta t$ , the total velocity increment is given by

$$
\begin{array} { c } { \Delta v = \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + \Delta t } a ( t ) d t = - v _ { \mathrm { e } } \displaystyle \int _ { m _ { 0 } } ^ { m ( t _ { 0 } + \Delta t ) } \frac { 1 } { m } d m = - v _ { \mathrm { e } } \ln \frac { m ( t _ { 0 } + \Delta t ) } { m _ { 0 } } } \end{array}
$$

or

$$
\Delta v = - \frac { F } { | \dot { m } | } \ln \left( 1 - \frac { | \dot { m } | \varDelta t } { m _ { 0 } } \right)
$$

assuming a constant mass-flow rate $| { \dot { m } } |$ .

Making use of the total velocity increment $\varDelta v$ , the acceleration may be expressed as

$$
a ( t ) = \frac { | \dot { m } | } { m ( t ) } \frac { 1 } { - \ln \left( 1 - \frac { | \dot { m } | \varDelta t } { m _ { 0 } } \right) } { \varDelta v } ,
$$

which approaches the limiting value

$$
a ( t ) \approx { \frac { \varDelta v } { \varDelta t } }
$$

in the case of negligible mass flow $( | \dot { m } | \varDelta t \ll m _ { 0 } )$ .

The one-dimensional motion considered so far may be generalized by introducing a time-dependent set of orthogonal unit vectors $e _ { 1 } , e _ { 2 }$ and $e _ { 3 }$ with constant projected thrust vector components $F _ { 1 } , F _ { 2 }$ and $F _ { 3 }$ . The resulting acceleration vector is given by

$$
{ \pmb a } ( t ) = \frac { 1 } { m } { \pmb E } \left( \begin{array} { c } { { F _ { 1 } } } \\ { { F _ { 2 } } } \\ { { F _ { 3 } } } \end{array} \right)
$$

or

$$
{ \pmb a } ( t ) = \frac { | \dot { m } | } { m ( t ) } \frac { 1 } { - \ln \left( 1 - \frac { | \dot { m } | \varDelta t } { m _ { 0 } } \right) } { \cal E } \varDelta { \pmb v } \quad .
$$

Here

$$
\Delta { \pmb v } ( t ) = \left( \begin{array} { c } { { \Delta v _ { 1 } } } \\ { { \Delta v _ { 2 } } } \\ { { \Delta v _ { 3 } } } \end{array} \right)
$$

is the vector of velocity increments in the chosen thrust reference frame, while the rotation matrix

$$
\pmb { { \cal E } } ( t ) = ( \pmb { \mathscr { e } } _ { 1 } , \pmb { \mathscr { e } } _ { 2 } , \pmb { \mathscr { e } } _ { 3 } )
$$

performs the transformation into the inertial reference frame used to describe the spacecraft motion.

In most cases the spacecraft maintains a constant orientation during the thrust phase, either with respect to the orbital frame or the inertial reference system. In the orbital frame the unit vectors $e _ { 1 }$ and $e _ { 3 }$ are aligned with the radial direction and the angular momentum vector. $e _ { 2 }$ completes the right-handed system and is parallel to the velocity vector for circular orbits:

$$
{ \begin{array} { l } { \displaystyle e _ { 1 } ~ = ~ { \frac { r } { | r | } } } \\ { \displaystyle e _ { 2 } ~ = ~ e _ { 3 } \times e _ { 1 } } \\ { \displaystyle e _ { 3 } ~ = ~ { \frac { r \times v } { | r \times v | } } ~ . } \end{array} }
$$

The orbital frame is a co-moving frame, which is particularly suited to separate in-plane thrust components, which change the size and shape of the orbit, and out-of-plane components, which affect the orbit’s spatial orientation.

The inertial thrust direction model is e.g. applicable to spin-stabilized spacecraft. Here, the inertially fixed spacecraft attitude results in a constant thrust direction vector and the transformation matrix $E = I$ is simply the identity matrix.

It should be noted that for a numerical treatment of accelerations due to thrust, both instantaneous and extended maneuvers lead to discontinuities in the equations of motion. Thus, a proper maneuver treatment requires the restart of the numerical integration algorithm at the beginning and end of each thrust phase.

# 3.7 Precision Modeling

For a wide range of applications, the accelerations described so far are fully sufficient for a precise description of the satellite orbit. However, there are missions with challenging accuracy requirements, such as in satellite geodesy, which have to account for even more and smaller perturbations. A prominent example is the US/French TOPEX/POSEIDON mission, which requests a radial position error of less than $1 0 \mathrm { c m }$ . Such high-precision modeling needs to account for additional perturbations like the radiation pressure of the Earth, tidal forces that modify the Earth’s gravity field, as well as general relativistic deviations to the Newtonian equations of motion. Finally empirical accelerations may be introduced to account for effects that cannot suitably be described by physical models.

# 3.7.1 Earth Radiation Pressure

In addition to the direct solar radiation pressure, the radiation emitted by the Earth leads to a small pressure on the satellite. Two components are distinguished: the shortwave optical radiation and the longwave infrared radiation. In both cases the acceleration on the satellite decreases slightly with increasing altitude. This is caused by the inverse square law of the emitted radiation pressure, which is partially compensated for by an increase of the illuminating surface section of the Earth with altitude. The amplitude of the typical albedo acceleration for low-Earth satellites is $10 \%$ to $3 5 \%$ of the acceleration due to direct solar radiation pressure (Knocke et al. 1988).

The optical albedo radiation is produced by reflection and scattering of incident solar radiation on the Earth’s surface. This reflection is described by the albedo factor $a$ , defined as the fraction of the shortwave radiation reflected from the Earth to space to the incident shortwave solar radiation. The average global albedo value is $a \approx 0 . 3 4$ , equivalent to a radiation of $4 5 9 \mathrm { W } / \mathrm { m } ^ { 2 }$ of the Earth surface elements. The optical albedo radiation has essentially the same spectral distribution as the direct solar radiation pressure. It is emitted only by the daylight side of the Earth and may vary significantly due to different surface characteristics and cloud coverage.

In contrast to the optical radiation, the infrared radiation is a near isotropic reemission of the direct solar radiation absorbed by the Earth and its atmosphere. The average emissivity $\epsilon$ is approximately 0.68. Its contribution to the flux is, however, reduced by a factor of 4 due to the ratio of the irradiated Earth cross-section $\pi R _ { \oplus } ^ { 2 }$ to the total radiating Earth surface $4 \pi R _ { \oplus } ^ { 2 }$ . Hence, the effective radiation of Earth ⊕surface elements due to infrared emission is $0 . 1 7 \phi$ or $2 3 0 \mathrm { W } / \mathrm { m } ^ { 2 }$ .

The acceleration of the spacecraft due to Earth radiation is summed up from $j \left( j = 1 , \ldots , N \right)$ individual terms, corresponding to different Earth area elements $d A _ { j }$

$$
\ddot { r } = \sum _ { j = 1 } ^ { N } C _ { R } \left( \nu _ { j } a _ { j } \cos \theta _ { j } ^ { E } + \frac { 1 } { 4 } \epsilon _ { j } \right) P _ { \odot } \frac { A } { m } \cos \theta _ { j } ^ { S } \frac { d A _ { j } } { \pi r _ { j } ^ { 2 } } e _ { j }
$$

where the $\nu _ { j }$ denote the Earth element shadow functions and $\theta _ { j } ^ { E }$ and $\theta _ { j } ^ { S }$ are the angles of the Earth surface or satellite surface normals to the incident radiation. The unit vector $e _ { j }$ points from the Earth surface element to the satellite, while the distance is $r _ { j }$ . The albedo and emissivity may be expressed using a second-degree zonal spherical harmonic model (Knocke et al. 1988). Typically about 20 Earth surface elements are considered.

# 3.7.2 Earth Tides

The gravitation of the Sun and the Moon exerts a direct force on Earth satellites, as discussed in Sect. 3.3. In addition, those forces are also acting on the body of the Earth and thus lead to a time-varying deformation of the Earth. The small periodic deformations of the solid body of the Earth are called solid Earth tides, while the oceans respond in a different way to lunisolar tidal perturbations, known as ocean tides. As a consequence, the Earth’s gravity field is no longer static in nature, but exhibits small periodic variations, which also affect the motion of satellites.

In a co-rotating frame, the gravitational field of the Sun or the Moon of mass $M$ implies a potential $U$ at a point $\mathrm { P }$ on the Earth’s surface, which is given by

$$
U = { \frac { G M } { | s - R | } } + { \frac { 1 } { 2 } } n ^ { 2 } d ^ { 2 }
$$

where $\pmb { R }$ and $\pmb { S }$ are the geocentric coordinates of $\mathrm { P }$ and of the tide generating body, respectively. Furthermore, $n$ is the mean motion of the body about an axis through the system’s center of mass and $d$ is the distance of $\mathrm { P }$ to this axis. Since $s \gg R$ for the Sun and the Moon, the denominator of (3.138) is expanded as

$$
{ \frac { 1 } { | s - R | } } \approx { \frac { 1 } { s } } \left( 1 + { \frac { R } { s } } \cos \gamma - { \frac { 1 } { 2 } } { \frac { R ^ { 2 } } { s ^ { 2 } } } + { \frac { 3 } { 2 } } { \frac { R ^ { 2 } } { s ^ { 2 } } } \cos ^ { 2 } \gamma \right)
$$

where $\gamma$ is the angle between $\pmb { S }$ and $\pmb { R }$ . The distance $d$ may furthermore be expressed as

$$
\begin{array} { r c l } { { d ^ { 2 } } } & { { = } } & { { d _ { c } ^ { 2 } + R ^ { 2 } { \cos } ^ { 2 } \phi - 2 d _ { c } R \cos \phi \cos ( \varDelta \lambda ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { d _ { c } ^ { 2 } + R ^ { 2 } { \cos } ^ { 2 } \phi - 2 d _ { c } R \cos \gamma \quad , } } \end{array}
$$

where $d _ { c } = M s / ( M + M _ { \oplus } )$ is the geocentric distance of the center of mass of the system, $\phi$ is the geocentric latitude and $\varDelta \lambda$ is the difference of the East longitudes of $\mathrm { P }$ and the perturbing body. With the above relations and $n ^ { 2 } s ^ { 3 } = G ( M + M _ { \oplus } )$ the potential may thus be written as (Bertotti & Farinella 1990)

$$
U = \frac { G M } { s } \Biggl ( 1 + \frac { 1 } { 2 } \frac { M } { M + M _ { \oplus } } \Biggr ) + \frac { G M R ^ { 2 } } { 2 s ^ { 3 } } \bigl ( 3 \cos ^ { 2 } \gamma - 1 \bigr ) + \frac { n ^ { 2 } R ^ { 2 } } { 2 } \cos ^ { 2 } \phi \ .
$$

While the first term is constant, the third term describes the rotational potential about an axis through the Earth’s center and perpendicular to the orbital plane. It adds a small permanent equatorial bulge to the Earth, similar to the one produced by the rotation of the Earth, but of a much smaller size, since $n ^ { 2 } \ll \omega _ { \oplus } ^ { 2 }$ .

The second term in (3.141) is called the tidal potential $U _ { 2 }$ . It is a second-order zonal harmonic that deforms the equipotential to a prolate, axisymmetric ellipsoid, aligned along the direction to the Moon or to the Sun. Its amplitude is proportional to $G M / s ^ { 3 }$ and thus the lunar tides are about twice as strong as the solar tides. The dominant periodicity of the tidal acceleration is nearly semi-diurnal according to the dependence of $U _ { 2 }$ on $\cos ^ { 2 } \gamma$ , which itself is a function of cos $2 \lambda$ .

The tidal potential essentially leads to an elastic deformation of the Earth. This may mathematically be described by a linear relation of the tidal potential $U _ { 2 }$ and the resulting perturbed gravity potential $U _ { T }$ , the ratio of both potentials being the Love number $\kappa \approx 0 . 3$ . A completely stiff body would therefore have a vanishing Love number. As the tidal potential is a second-order harmonic, the perturbed gravity potential falls off with $1 / r ^ { 3 }$ and can finally be expressed as

$$
U _ { T } = \frac 1 2 \kappa { \frac { G M R _ { \oplus } ^ { 5 } } { s ^ { 3 } r ^ { 3 } } } \left( 3 \cos ^ { 2 } \gamma - 1 \right) .
$$

The Earth is, however, only elastic to first order. Deviations from an elastic tidal response are due to the rate-dependent behavior of terrestrial fluids, like the Earth’s inner core and the oceans, as well as friction, i.e. energy dissipation in matter. The latter causes phase lags of the tidal bulge with respect to the position of the Sun and the Moon. The tidal-induced gravity potential contains many different periods, as the angle $\gamma$ depends on the position of the Sun and the Moon with respect to the rotating Earth. Moreover, the potential varies with $1 / s ^ { 3 }$ and accordingly the variation in the eccentricity of the Sun’s and Moon’s orbit leads to monthly and annual periods.

The perturbations of satellite orbits from the lunisolar solid Earth tides are derived by an expansion of the tidal-induced gravity potential using spherical harmonics in a similar way as for the static gravity field of the Earth. For practical purposes, the time-dependent corrections to the unnormalized geopotential coefficients can be computed according to

$$
\left\{ \begin{array} { l } { \Delta C _ { n m } } \\ { \Delta S _ { n m } } \end{array} \right\} = 4 k _ { n } \left( \frac { G M } { G M _ { \oplus } } \right) \left( \frac { R _ { \oplus } } { s } \right) ^ { n + 1 } \sqrt { \frac { ( n + 2 ) ( n - m ) ! ^ { 3 } } { ( n + m ) ! ^ { 3 } } } P _ { n m } ( \sin \phi ) \left\{ \begin{array} { l } { \cos ( m \lambda ) } \\ { \sin ( m \lambda ) } \end{array} \right\}
$$

(Sanchez 1974) for the Sun and the Moon respectively, where $k _ { n }$ are the Love numbers of degree $n$ , $\phi$ is the Earth-fixed latitude and $\lambda$ the Earth-fixed longitude of the disturbing body. As the acceleration due to solid Earth tides falls off at least with $1 / r ^ { 4 }$ , a careful evaluation of an adequate force model is required especially for low altitude missions, depending on the accuracy requirements.

Ocean tides also play an important role in satellite geodesy, although their amplitudes are about one order of magnitude smaller than that of solid Earth tides. Their contributions can be expressed by an ocean tide potential, which is expanded in terms of spherical harmonics and mapped to time-varying geopotential coefficients

$$
\left\{ \begin{array} { c } { { \Delta C _ { n m } } } \\   \Delta S _ { n m } \right\} = \frac { 4 \pi G R _ { \oplus } ^ { 2 } \rho _ { w } } { G M _ { \oplus } } \frac { 1 + k _ { n } ^ { \prime } } { 2 n + 1 } \left\{ \begin{array} { c } { { \displaystyle { \sum _ { s n m } ( C _ { s n m } ^ { + } + C _ { s n m } ^ { - } ) \cos \theta _ { s } + ( S _ { s n m } ^ { + } + S _ { s n m } ^ { - } ) \sin \theta _ { s } } } } \\ { { \displaystyle { \sum _ { s ( n , m ) } ( S _ { s n m } ^ { + } - S _ { s n m } ^ { - } ) \cos \theta _ { s } - ( C _ { s n m } ^ { + } - C _ { s n m } ^ { - } ) \sin \theta _ { s } } } } \end{array} \right\} \end{array}
$$

(Eanes et al. 1983) where $\rho _ { w }$ is the density of seawater, $k _ { n } ^ { \prime }$ are the load deformation coefficients and $C _ { s n m } ^ { \pm }$ and $S _ { s n m } ^ { \pm }$ n are the ocean tide coefficients in meters for the tide constituent $s$ . Moreover, $\theta _ { s }$ is the weighted sum of the six Doodson variables. Doodson variables denote fundamental arguments of the Sun’s and Moon’s orbit, being closely related to the arguments of the nutation series. An alternative representation of ocean tide harmonics may be found in Schwiderski (1983). For a rigorous computation of the solid Earth and ocean tides, the Love numbers may no longer be treated as constant values, leading to a dual-step approach in the evaluation of the geopotential coefficient corrections. The practical computation of the solid Earth and ocean tides is therefore a complex task, which is described in detail in Seidelmann (1992) and McCarthy (1996).

# 3.7.3 Relativistic Effects

A rigorous treatment of the satellite’s motion should be formulated in accordance with the theory of general relativity. While the special theory of relativity considers a flat four-dimensional space-time, this is no longer true in the vicinity of the Earth. Instead, the Earth’s mass $M _ { \oplus }$ with the potential $U = G M _ { \oplus } / r$ and the Earth’s angular momentum vector $\scriptstyle { l _ { \oplus } }$ with the potential $V = G / 2 ( l _ { \oplus } \times r ) / r ^ { 3 }$ lead to a curvature of the four-dimensional space-time. Making use of the standard coordinates $x ^ { \mu } = ( c t , x ^ { 1 } , x ^ { 2 } , x ^ { 3 } )$ the post-Newtonian space-time can be described using the invariant element

$$
\begin{array} { l } { { d s ^ { 2 } = - c ^ { 2 } d \tau ^ { 2 } } } \\ { { \ = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } } } \\ { { \ = - \left( 1 - \displaystyle \frac { 2 U } { c ^ { 2 } } + \displaystyle \frac { 2 U ^ { 2 } } { c ^ { 4 } } \right) ( d x ^ { 0 } ) ^ { 2 } - 4 \displaystyle \frac { V _ { i } } { c ^ { 3 } } d x ^ { 0 } d x ^ { i } + \left( 1 + \displaystyle \frac { 2 U } { c ^ { 2 } } \right) \delta _ { i j } d x ^ { i } d x ^ { j } } } \end{array} ( 1 - \mathrm { h } \left( { \frac { 2 U } { c ^ { 2 } } } \right) )
$$

between two events (Soffel 1989). Here, Einstein’s summation convention is applied, which states that summation is assumed, when a literal index is repeated in a term, both as a subscript and a superscript. The Greek indices run from 0 . . . 3 and the Roman indices from 1 . . . 3. The time $\tau$ is the proper time that would be measured by an atomic clock comoving with the satellite, while the coordinate time $t$ may be associated with an atomic clock located at the geocenter. In (3.143) the so-called gravito-electric contributions stem from the curvature of space-time due to the Earth’s mass, which is $( G M _ { \oplus } ) / ( c ^ { 2 } R _ { \oplus } ) \approx 7 { \cdot } 1 0 ^ { - 1 0 }$ at the Earth’s surface. The gravito-magnetic contributions, on the other hand, stem from a dragging of spacetime due to the rotation of the Earth with a magnitude of $( G L _ { \oplus } ) / ( c ^ { 3 } R _ { \oplus } ^ { 2 } ) \approx 4 { \cdot } 1 0 ^ { - 1 6 }$ .

According to the theory of general relativity, the motion of a satellite can be expressed using the geodesic equation (Weinberg 1972)

$$
{ \frac { d ^ { 2 } x ^ { \mu } } { d \tau ^ { 2 } } } + \Gamma _ { \nu \sigma } ^ { \mu } { \frac { d x ^ { \nu } } { d \tau } } { \frac { d x ^ { \sigma } } { d \tau } } = 0
$$

where the Christoffel symbols $T _ { \nu \sigma } ^ { \mu }$ are obtained from derivatives of the space-time metric gμν

$$
{ \cal { T } } _ { \nu \sigma } ^ { \mu } = { \frac { 1 } { 2 } } g ^ { \alpha \mu } \left( { \frac { \partial g _ { \alpha \nu } } { \partial x ^ { \sigma } } } + { \frac { \partial g _ { \alpha \sigma } } { \partial x ^ { \nu } } } - { \frac { \partial g _ { \nu \sigma } } { \partial x ^ { \alpha } } } \right) .
$$

Here $g ^ { \alpha \mu }$ can be computed as elements of the matrix inverse of $g _ { \alpha \mu }$

Based on the given metric in the vicinity of the Earth, the geodesic equation may be expanded to first order in the relativistic terms $U / c ^ { 2 }$ and $V / c ^ { 3 }$ . This procedure leads to the Newtonian equation of motion with additional post-Newtonian correction terms. Following McCarthy (1996), the coordinate time $t$ is associated with the Terrestrial Time TT (see Sect. 5.1) and dropping the gravito-magnetic contributions leads to the post-Newtonian correction of the acceleration

$$
\ddot { \boldsymbol { r } } = + \frac { G M _ { \oplus } } { r ^ { 2 } } \left( \left( 4 \frac { G M _ { \oplus } } { c ^ { 2 } r } - \frac { v ^ { 2 } } { c ^ { 2 } } \right) \boldsymbol { e } _ { r } + 4 \frac { v ^ { 2 } } { c ^ { 2 } } ( \boldsymbol { e } _ { r } \cdot \boldsymbol { e } _ { v } ) \boldsymbol { e } _ { v } \right)
$$

where $e _ { r }$ and $e _ { v }$ denote the unit positon and velocity vector. For a circular orbit $G M _ { \oplus } / r = v ^ { 2 }$ and the velocity is perpendicular to the radius vector. Accordingly the relativistic correction of the acceleration

$$
\ddot { \pmb { r } } = + \frac { G M _ { \oplus } } { r ^ { 2 } } \pmb { e } _ { r } \left( 3 \frac { v ^ { 2 } } { c ^ { 2 } } \right)
$$

is equal to the product of the Newtonian acceleration and a factor of $3 v ^ { 2 } / c ^ { 2 }$ which is roughly $3 { \cdot } 1 0 ^ { - 1 0 }$ for a typical satellite velocity.

As a rough rule, the size of general relativistic effects is given by the Schwarzschild radius of the Earth $( 2 G M _ { \oplus } ) / c ^ { 2 } \approx 1 { \mathrm { c m } }$ . Any application in satellite geodesy that approaches this level of accuracy must carefully consider the effects of general relativity. The relativistic effects due to the mass of the Sun on the orbit of an Earth satellite show up as post-Newtonian corrections to the third-body (tidal) forces of the Sun and lead to a relativistic satellite distance variation of

$$
\frac { G M _ { \odot } } { { \mathrm { A U } } ^ { 3 } } \cdot \frac { r } { n } \cdot \frac { G M _ { \odot } } { c ^ { 2 } \mathrm { A U } } \approx 0 . 1 \mathrm { m m } ~ ,
$$

where $n$ is the mean motion of the satellite.

# 3.7.4 Empirical Forces

Despite the tremendous improvements of force models applied within orbit determination, further progress is getting more and more difficult. This is, in general, caused by the growing complexity and computational load of these models. In particular, the imperfect non-conservative force models impose major limitations to a high-precision force modeling of Earth observing platforms. Even the most detailed models for the satellite’s surface forces are limited by uncertainties in the knowledge of the time-varying orientation, material properties, and surface temperatures.

Based on a highly precise force model, small unmodeled forces may be accounted for using the concept of empirical accelerations. Much of this mismodeling occurs at a frequency of one-cycle-per-orbital-revolution (1CPR). Accordingly, constant and 1CPR empirical accelerations

$$
\ddot { r } = E \left( { \pmb a } _ { 0 } + { \pmb a } _ { 1 } \sin \nu + { \pmb a } _ { 2 } \cos \nu \right)
$$

are employed to accommodate the effect. Here, $\pmb { a } _ { 0 }$ is a constant acceleration bias, while ${ \pmb a } _ { 1 }$ and $\pmb { a } _ { 2 }$ are the 1CPR coefficients and $\nu$ is the true anomaly. The direction of the empirical acceleration is commonly specified in the local orbital frame, with principal axes in the radial, cross-track, and along-track direction, which is transformed into the inertial system by the matrix $E$ . In order to provide an optimum compensation of unmodelled forces, the empirical acceleration coefficients have to be adjusted along with other parameters in an orbit determination.

Empirical accelerations have successfully been employed to mitigate the effects of force model errors and spacecraft momentum unloads of GPS satellites (Colombo 1989, Bertiger et al. 1994) as well as for TOPEX/POSEIDON (Tapley et al. 1994). While this technique is especially well suited for an a posteriori high-precision orbit restitution, care must be taken to apply the empirical acceleration parameters for orbit prediction purposes, since this may lead to a substantial degradation of the position accuracy.

# Exercises

Exercise 3.1 (Gravity Field) The processor time required to compute the satellite acceleration due to the Earth’s gravity field is to be determined as a function of the model’s order using the Cunningham algorithm and a maximum order of 20. Compare the observed times with the assumption of a quadratic increase of the workload with the order of the gravity field.

Solution: In a sample test run the CPU times have been determined for 10 000 evaluations of the gravity field at a given order and are marked in Fig. 3.16. As can be seen the CPU times may be modelled by a parabola that intersects the abscissa at a value of about $0 . 3 \mathrm { s }$ , which reflects a computational overhead for function calls, initialization, and other computations performed independently of the actual Cunningham recursions. As a consequence, the evaluation of a $1 0 \times 1 0$ gravity field takes only 3 times longer than that of a $4 \times 4$ field. This is about two time less than would be expected for a purely quadratic increase.

![](images/45eb99d1adbf463efef02e27185f309c50ea164e893b3cafa2a814398763503f.jpg)  
Fig. 3.16. Sample CPU times for 10 000 evaluations of the gravity field

Exercise 3.2 (Moon ephemerides) The Moon ephemeris is to be computed and evaluated. To this end the geocentric Cartesian position coordinates of the Moon are to be computed from 2006/03/14 00:00 to 2006/03/18 00:00 (Terrestrial Time) in steps of one day. A comparison of low-precision analytic lunar coordinates is to be made with positions as derived from the Chebyshev coefficients of JPL’s DE405. A listing of the 39 Chebyshev coefficients (13 per coordinate) is given below, which covers the DE405 subinterval size of 4 days.

<table><tr><td>i</td><td>ax [km]</td><td>ay [km]</td><td>az [km]</td></tr><tr><td>0</td><td>-0.383089044877.10+06</td><td>-0.379891721705.10+05</td><td>-0.178496690739.10+05</td></tr><tr><td>1</td><td>0.218158411755.10+05</td><td>-0.143611643157.10+06</td><td>-0.788257550332.10+05</td></tr><tr><td>2</td><td>0.179067292901.10+05</td><td>0.187126702787.10+04</td><td>0.880684692614.10+03</td></tr><tr><td>3</td><td>-0.836928063412.10+02</td><td>0.112734362473.10+04</td><td>0.618395886330.10+03</td></tr><tr><td>4</td><td>-0.628266733052.10+02</td><td>0.932891213817.10+00</td><td>0.103331218595.10+01</td></tr><tr><td>5</td><td>-0.459274434235.10+00</td><td>-0.191932684131.10+01</td><td>-0.104949867328.10+01</td></tr><tr><td>6</td><td>0.491167202820.10-01</td><td>-0.266517663332.10-01</td><td>-0.150337371963:10-01</td></tr></table>

Solution: The Cartesian position coordinates of the Moon using the analytic equations are given as   

<table><tr><td>7</td><td>0.770804039288.10-03 -0.125935992206:10-03</td><td>0.104558913449.10-02 -0.359077689124.10-04</td><td>0.569056416308.10 -03 -0.186297523287.10-04</td></tr><tr><td>8 9</td><td>0.500271026611:10-05</td><td>-0.123405162037.10-04</td><td>-0.680012420654.10-05</td></tr><tr><td>10</td><td>0.107044869186.10-05</td><td>0.180479239596.10-06</td><td>0.902057208454.10-( -07</td></tr><tr><td>11</td><td>0.172472464344.10-08</td><td>0.525522632334.10-07</td><td>0.287891446432.10-07</td></tr><tr><td>12</td><td>-0.269667589577.10-08</td><td>0.543313967009.10-09</td><td>0.319822827700.10-09</td></tr></table>

In comparison, the position coordinates as derived from the Chebyshev coefficients of the Development Ephemeris DE405 are   

<table><tr><td>Date</td><td>TT</td><td>x [km]</td><td>y[km]</td><td>z [km]</td></tr><tr><td>2006/03/14</td><td>00:00:00.0</td><td>-387105.185</td><td>106264.577</td><td>61207.474</td></tr><tr><td>2006/03/15</td><td>00:00:00.0</td><td>-403080.629</td><td>33917.735</td><td>21704.832</td></tr><tr><td>2006/03/16</td><td>00:00:00.0</td><td>-401102.631</td><td>-39906.188</td><td>-18757.478</td></tr><tr><td>2006/03/17</td><td>00:00:00.0</td><td>-381055.373</td><td>-111853.486</td><td>-58337.911</td></tr><tr><td>2006/03/18</td><td>00:00:00.0</td><td>-343564.315</td><td>-178551.672</td><td>-95178.733</td></tr></table>

<table><tr><td>Date</td><td>TT</td><td>x [km]</td><td>y[km]</td><td>z [km]</td></tr><tr><td>2006/03/14</td><td>00:00:00.0</td><td>-386976.783</td><td>106369.219</td><td>61240.442</td></tr><tr><td>2006/03/15</td><td>00:00:00.0</td><td>-403002.331</td><td>34008.826</td><td>21741.255</td></tr><tr><td>2006/03/16</td><td>00:00:00.0</td><td>-401058.650</td><td>-39859.480</td><td>一 -18729.305</td></tr><tr><td>2006/03/17</td><td>00:00:00.0</td><td>-381019.563</td><td>-111859.423</td><td>-58322.341</td></tr><tr><td>2006/03/18</td><td>00:00:00.0</td><td>-343513.403</td><td>-178603.217</td><td>-95176.374</td></tr></table>

The position differences in the above interval amount to $1 6 9 ~ \mathrm { k m }$ at maximum, consistent with the relative accuracy of the analytic theory of $1 0 ^ { - 3 }$ .

Exercise 3.3 (Accelerations) The selection of an appropriate force model for a specific satellite orbit requires an assessment of the various perturbations acting on the satellite. To first order the analytical acceleration equations may be evaluated and the altitude regimes determined, where certain perturbations exceed others.

Determine the altitudes where the acceleration from the Earth’s dominant zonal gravity term $J _ { 2 0 }$ and sectorial term $J _ { 2 2 }$ equals the acceleration due to the Moon and Sun. In addition, determine the altitude, where the non-conservative accelerations due to atmospheric drag and solar radiation pressure balance $C _ { R } = 1 . 3 , C _ { D } = 2 . 3 )$ .

Hint: Make use of the following simplified relations

$$
\begin{array} { r c l } { { a _ { \mathrm { J n m } } } } & { { = } } & { { ( n + 1 ) \displaystyle \frac { G M _ { \oplus } } { r ^ { 2 } } \displaystyle \frac { R _ { \oplus } ^ { n } } { r ^ { n } } \sqrt { \bar { C } _ { n m } ^ { 2 } + \bar { S } _ { n m } ^ { 2 } } } } \\ { { } } & { { } } & { { } } \\ { { a _ { \mathrm { S / M } } } } & { { = } } & { { \displaystyle \frac { 2 G M } { s ^ { 3 } } r } } \\ { { } } & { { } } & { { } } \\ { { a _ { \mathrm { S R P } } } } & { { = } } & { { C _ { R } \displaystyle \frac { A } { m } P _ { \odot } } } \\ { { } } & { { } } & { { } } \\ { { a _ { \mathrm { D R G } } } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } C _ { D } \displaystyle \frac { A } { m } \rho \displaystyle \frac { G M _ { \oplus } } { a } } } \end{array}
$$

that are derived from (3.15), (3.41), (3.75), and (3.97), respectively.

Solution: The geocentric distance, where the lunar and solar acceleration balances that of the Earth’s gravity field, is

$$
r ^ { n + 3 } = { \frac { n + 1 } { 2 } } { \frac { G M _ { \oplus } } { G M } } R _ { \oplus } ^ { n } s ^ { 3 } \sqrt { \bar { C } _ { n m } ^ { 2 } + \bar { S } _ { n m } ^ { 2 } } .
$$

The density $\rho$ , where the solar radiation pressure is balanced by the atmospheric drag, is given as

$$
\rho = 2 \frac { C _ { R } } { C _ { D } } P _ { \odot } \frac { a } { G M _ { \oplus } } .
$$

The associated altitude may be determined from the difference of the two accelerations using a conventional root-finding algorithm. The following relations are obtained:

Note that the dependence of the various acceleration sources on the altitude is depicted in Fig. 3.1.

Exercise 3.4 (Orbit Perturbations) The orbit perturbations due to the nonspherical gravity field of the Earth, the third-body forces of the Sun and the Moon, as well as the solar radiation pressure and the atmospheric drag are to be evaluated. To this end, the equations of motion of the satellite are to be numerically integrated for a reference (truth) orbit that takes into account all relevant perturbations and is based on a gravity model of the Earth complete to order and degree 20. To compute the orbit perturbations, the satellite position using a restricted force model with individual perturbations switched off is computed and the difference with respect to the reference trajectory is derived.

The orbit perturbations are to be computed for a remote sensing satellite of area $5 \mathrm { m } ^ { 2 }$ and mass $1 0 0 0 \mathrm { k g }$ with the initial orbital elements at epoch 1999/03/01 00:00:00.0 UTC of

Semi-major axis a 7178.0 km Eccentricity e 0.001 Inclination i $9 8 . 5 7 ^ { \circ }$ RA ascend. node $\varOmega$ $0 . 0 ^ { \circ }$ Arg. of perigee ω $0 . 0 ^ { \circ }$ Mean anomaly M 0.0◦

for a propagation period of one revolution as well as for a one-day period. The considered perturbations are to describe the position errors arising, when the Earth’s gravity model is restricted to $J _ { 2 0 } , \ J _ { 2 2 } , \ J _ { 4 4 } , \ J _ { 1 0 , 1 0 }$ and when Sun, Moon, solar radiation pressure and drag are neglected, respectively.

In addition, the orbital perturbations are to be computed for a geostationary satellite of area $1 0 \mathrm { m } ^ { 2 }$ and mass $1 0 0 0 \mathrm { k g }$ with initial orbital elements

Semi-major axis a 42166.0 km Eccentricity $e$ 0.0004 Inclination $i$ $0 . 0 2 ^ { \circ }$ RA ascend. node $\varOmega$ $0 . 0 ^ { \circ }$ Arg. of perigee $\omega$ $0 . 0 ^ { \circ }$ Mean anomaly M 0.0◦

for propagation periods of one and two days. Both satellites are supposed to have a solar radiation pressure coefficients of 1.3 and a drag coefficient of 2.3.

Solution: The equations of motion are numerically integrated over the specified time intervals, both with the reference force model and the restricted models. The resulting position differences exhibit both a steady increase and periodic variations. Below, the maximum position differences within the propagation interval are tabulated.

<table><tr><td>Restricted force model</td><td colspan="2">Remote sensing</td><td colspan="2">Geostationary</td></tr><tr><td></td><td>1 rev</td><td>1 day</td><td>1 day</td><td>2 days</td></tr><tr><td></td><td>[m]</td><td>[m]</td><td>[m]</td><td>[m]</td></tr><tr><td>J20</td><td>600</td><td>5028</td><td>671</td><td>2534</td></tr><tr><td>J22</td><td>224</td><td>3038</td><td>2</td><td>10</td></tr><tr><td>J44</td><td>148</td><td>1925</td><td>0</td><td>0</td></tr><tr><td>J10,10</td><td>23</td><td>459</td><td>0</td><td>0</td></tr><tr><td>Sun</td><td>3</td><td>34</td><td>3143</td><td>4834</td></tr><tr><td>Moon</td><td>6</td><td>66</td><td>5080</td><td>5438</td></tr><tr><td>Radiation pressure</td><td>1</td><td>14</td><td>415</td><td>830</td></tr><tr><td>Atmospheric drag</td><td>1</td><td>105</td><td>0</td><td>0</td></tr></table>

It should be noted that the position differences for a restricted gravity field model in the above table describe the position errors arising from a neglect of the respective higher-order terms.

# 4. Numerical Integration

The high accuracy that is nowadays required in the computation of satellite orbits can only be achieved by using numerical methods for the solution of the equation of motion (cf. Gendt & Sorokin 1978). A variety of methods has been developed for the numerical integration of ordinary differential equations and many of them have successfully been applied in the field of celestial mechanics. Since each method has its own inherent advantages and drawbacks, it is in general not possible to simply select one method as best suited for the prediction of satellite motion.

The present chapter describes the basic principles and properties of the most important integration methods and assesses their usefulness for orbit computation purposes:

• Runge–Kutta methods that are particularly easy to use and may be applied to a wide range of different problems,   
• multistep methods that provide a high efficiency but require a storage of past data points, and   
• extrapolation methods that are famous for their high accuracy.

Special attention is also given to methods for the direct integration of second-order equations of motion. These methods may be preferable in those cases where the forces acting on a satellite do not depend on its velocity.

The discussion of numerical integration methods is by no means exhaustive, however, and the reader who wants to study the matter in more detail should consult one of the various textbooks published on this subject, e.g. Lambert (1973), Shampine & Gordon (1975), Stoer & Bulirsch (1983) or Hairer et al. (1987). For further reading the reviews of integration methods by Gupta et al. (1985) and by Kinoshita & Nakai (1989) are recommended.

To start with, it is assumed that the differential equations to be solved are $n$ -dimensional first-order equations of the form

$$
\dot { \boldsymbol { y } } = \boldsymbol { f } ( t , \boldsymbol { y } ) \quad \boldsymbol { y } , \dot { \boldsymbol { y } } , \boldsymbol { f } \in \mathbb { R } ^ { n } \quad ,
$$

where dotted symbols denote derivatives with respect to time $t$ . This form can always be obtained from the second-order differential equation

$$
\ddot { \pmb { r } } = \pmb { a } ( t , \pmb { r } , \dot { \pmb { r } } )
$$

for the acceleration of a satellite by combining position $r$ and velocity $\dot { \boldsymbol { r } }$ into the 6-dimensional state vector

$$
{ \bf \it y } = \left( { \sum _ { \dot { r } } ^ { r } } \right) { \bf \epsilon } ,
$$

which satisfies

$$
\dot { \boldsymbol { y } } = \boldsymbol { f } ( t , \boldsymbol { y } ) = \left( \begin{array} { c } { \dot { r } } \\ { \boldsymbol { a } ( t , r , \dot { r } ) } \end{array} \right) \mathrm { ~ . ~ }
$$

# 4.1 Runge–Kutta Methods

# 4.1.1 Introduction

Starting from initial values $\mathbf { y } _ { 0 } ~ = ~ \mathbf { y } ( t _ { 0 } )$ at time $t _ { 0 }$ one may calculate a simple approximation of $\boldsymbol { \mathbf { y } }$ at some later time $t _ { 0 } + h$ from a first-order Taylor expansion

$$
\begin{array} { r c l } { { { \mathbf { y } } ( t _ { 0 } + h ) } } & { { \approx } } & { { { \mathbf { y } } _ { 0 } + h { \dot { \mathbf { y } } } _ { 0 } } } \\ { { } } & { { = } } & { { { \mathbf { y } } _ { 0 } + h f ( t _ { 0 } , { \mathbf { y } } _ { 0 } ) , } } \end{array}
$$

which is known as a Euler step. The geometrical interpretation of this equation is to start with $( t _ { 0 } , y _ { 0 } )$ and to proceed with a time-step of size $h$ along the tangent to the graph of $\textbf {  { y } }$ . Performing a series of subsequent Euler steps (see Fig. 4.1) one obtains approximate values $\eta _ { i }$ of the solution at distinct times $t _ { i } = t _ { 0 } + i h$ $( i = 1 , 2 , \dots )$ .

![](images/e0cb05f9e49c512c064f131f7de257c483ad4f63e60a4fbeb9d920f4bac290fa.jpg)  
Fig. 4.1. Approximate solution of a differential equation $\dot { y } = f ( t , y )$ using Euler steps of size $h$

Obviously the stepsize has to be very small if one wants to follow the solution curve over several steps and it seems worthwhile to look for better approximations. Using the general notation

$$
\begin{array} { r } { { \mathbf { { y } } } ( t _ { 0 } + h ) \approx { \mathbf { { y } } } _ { 0 } + h \cdot \pmb { \phi } = \pmb { \eta } ( t _ { 0 } + h ) } \end{array}
$$

for the approximate solution $\eta ( t _ { 0 } + h )$ , it is evident that $\Phi$ , the increment function, should closely approximate the slope of the secant through $( t _ { 0 } , y _ { 0 } )$ and $( t _ { 0 } +$ $h$ , ${ \bf y } ( t _ { 0 } + h ) )$ which may deviate considerably from the slope $f$ of the tangent used in the Euler step.

To overcome this deficiency, the mathematicians Carl Runge and Wilhelm Kutta developed improved expressions around the end of the 19th century, which are based on the slopes at various points within the integration step. In the classical RK4 Runge–Kutta method, the increment function $\Phi$ is calculated as the weighted mean

$$
\pmb { \phi } _ { \mathrm { R K 4 } } = \frac { 1 } { 6 } ( \pmb { k } _ { 1 } + 2 \pmb { k } _ { 2 } + 2 \pmb { k } _ { 3 } + \pmb { k } _ { 4 } )
$$

of four slopes

$$
\begin{array} { r c l } { { k _ { 1 } } } & { { = } } & { { f ( t _ { 0 } , y _ { 0 } ) } } \\ { { k _ { 2 } } } & { { = } } & { { f ( t _ { 0 } + h / 2 , y _ { 0 } + h k _ { 1 } / 2 ) } } \\ { { k _ { 3 } } } & { { = } } & { { f ( t _ { 0 } + h / 2 , y _ { 0 } + h k _ { 2 } / 2 ) } } \\ { { k _ { 4 } } } & { { = } } & { { f ( t _ { 0 } + h , y _ { 0 } + h k _ { 3 } ) . } } \end{array}
$$

This formula is designed to approximate the exact solution up to terms of order $h ^ { 4 }$ , provided that $\mathbf { \boldsymbol { y } } ( t )$ is sufficiently smooth and differentiable, and the RK4 method is therefore called a 4th-order method. Its local truncation error

$$
e _ { \mathrm { R K } 4 } = | { \boldsymbol { y } } ( t _ { 0 } + h ) - { \boldsymbol { \eta } } ( t _ { 0 } + h ) | \leq \mathrm { c o n s t } \cdot h ^ { 5 }
$$

is bound by a term of order $h ^ { 5 }$ .

The accuracy of the RK4 method is comparable to that of a 4th-order Taylor polynomial

$$
{ \bf { y } } _ { 0 } + h { \dot { \bf { y } } } _ { 0 } + \frac { h ^ { 2 } } { 2 ! } { \bf { y } } _ { 0 } ^ { ( 2 ) } + \frac { h ^ { 3 } } { 3 ! } { \bf { y } } _ { 0 } ^ { ( 3 ) } + \frac { h ^ { 4 } } { 4 ! } { \bf { y } } _ { 0 } ^ { ( 4 ) } ,
$$

where the superscripts in brackets indicate the order of derivatives with respect to time. However, the Runge–Kutta method avoids the calculation of the derivatives

$$
\begin{array} { l } { { { \dot { y } } _ { 0 } } = f ( t _ { 0 } , y _ { 0 } ) } \\ { { { \dot { y } } _ { 0 } ^ { ( 2 ) } = \displaystyle \frac { d } { d t } { \dot { y } } _ { 0 } = \displaystyle \frac { \partial { \dot { y } } _ { 0 } } { \partial t _ { 0 } } + \frac { \partial { \dot { y } } _ { 0 } } { \partial y _ { 0 } } { \dot { y } } _ { 0 } = \displaystyle \frac { \partial f ( t _ { 0 } , y _ { 0 } ) } { \partial t _ { 0 } } + \frac { \partial f ( t _ { 0 } , y _ { 0 } ) } { \partial y _ { 0 } } { \dot { y } } _ { 0 } } } \\ { { { \dot { y } } _ { 0 } ^ { ( 3 ) } = \displaystyle \frac { d } { d t } { y } _ { 0 } ^ { ( 2 ) } = \displaystyle \frac { \partial { y } _ { 0 } ^ { ( 2 ) } } { \partial t _ { 0 } } + \frac { \partial { y } _ { 0 } ^ { ( 2 ) } } { \partial y _ { 0 } } { \dot { y } } _ { 0 } } } \\ { { { \dot { y } } _ { 0 } ^ { ( 4 ) } = \displaystyle \frac { d } { d t } { y } _ { 0 } ^ { ( 3 ) } = \displaystyle \frac { \partial { y } _ { 0 } ^ { ( 3 ) } } { \partial t _ { 0 } } + \frac { \partial { y } _ { 0 } ^ { ( 3 ) } } { \partial y _ { 0 } } { \dot { y } } _ { 0 } ~ , } } \end{array}
$$

which may be pretty cumbersome and replaces them by evaluations of the function $f$ . This makes Runge–Kutta methods an easy to use standard technique for the numerical solution of ordinary differential equations.

# 4.1.2 General Runge–Kutta Formulas

The RK4 method presented so far is the prototype of Runge–Kutta formulas all of which share the same common structure1. In an $s$ -stage RK formula, $s$ function evaluations

$$
\begin{array} { l c l } { { k _ { 1 } } } & { { = } } & { { f ( t _ { 0 } + c _ { 1 } h , { \bf y } _ { 0 } ) } } \\ { { } } & { { } } & { { } } \\ { { k _ { i } } } & { { = } } & { { f ( t _ { 0 } + c _ { i } h , { \bf y } _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } k _ { j } ) ~ ( i = 2 \ldots s ) } } \end{array}
$$

are used to form the increment function

$$
\pmb { \phi } = \sum _ { i = 1 } ^ { s } b _ { i } \pmb { k } _ { i }
$$

which yields an approximation

$$
\pmb { \eta } ( t _ { 0 } + h ) = \pmb { y } _ { 0 } + h \pmb { \varPhi } .
$$

Each method is fully described by the coefficients

$$
\begin{array} { r } { \left. \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} \right| \left. \begin{array} { l l l l l l } { a _ { 2 1 } } & { } & { } & { } & { } & { } \\ { a _ { 3 1 } } & { } & { } & { } & { } & { } \\ { \vdots } & { \vdots } & { \ddots } & { } & { } & { } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \ldots } & { a _ { s , s - 1 } } & { } & { } \\ { b _ { 1 } } & { b _ { 2 } } & { \ldots } & { b _ { s - 1 } } & { b _ { s } } & { } \end{array} \right. \ , } \end{array}
$$

which are chosen in such a way that the order $p$ of the local truncation error is as high as possible. Usually the coefficients are determined such that they obey the relations

$$
\sum _ { i = 1 } ^ { s } b _ { i } = 1 \quad , \qquad c _ { 1 } = 0 \quad , \qquad c _ { i } = \sum _ { j = 1 } ^ { i - 1 } a _ { i j } \quad ( i > 1 ) \quad .
$$

For the RK4 method described above the number $s$ of function evaluations is just equal to the order $p$ of the local truncation error, but this is not generally the case. Butcher (1964, 1965, 1985) has shown that at least one additional evaluation is required for methods of order 5 and 6, that two additional evaluations are required for order 7 and three for order 8 and upwards. These rules are known as Butcher barriers. Only few methods of higher order are currently known, since the derivation of appropriate coefficients becomes increasingly difficult. The tenth-order method of Hairer (1978) requires a total of 17 function evaluations per step.

Since the coefficients are not uniquely determined by the condition of maximum order, one may find various Runge–Kutta methods with an equal number of stages. Furthermore it is possible to construct methods of neighboring order that are based on the same set of function evaluations. These methods are known as embedded Runge–Kutta methods and allow an easy estimation of the local truncation error which is a prerequisite for an efficient stepsize control during the integration. An embedded method of $s$ stages yields two independent approximations

$$
\begin{array} { r c l } { { \displaystyle \eta ( t _ { 0 } + h ) } } & { { = } } & { { \displaystyle y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } } } \\ { { } } & { { } } & { { } } \\ { { \hat { \eta } ( t _ { 0 } + h ) } } & { { = } } & { { \displaystyle y _ { 0 } + h \sum _ { i = 1 } ^ { s } \hat { b } _ { i } k _ { i } } } \end{array}
$$

of orders $p$ and $p { + 1 }$ with local truncation errors

$$
\begin{array} { r c l c l } { { e } } & { { = } } & { { | { \bf y } ( t _ { 0 } + h ) - { \boldsymbol \eta } ( t _ { 0 } + h ) | } } & { { \le } } & { { c h ^ { p + 1 } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \hat { e } } } & { { = } } & { { | { \bf y } ( t _ { 0 } + h ) - \hat { \pmb \eta } ( t _ { 0 } + h ) | } } & { { \le } } & { { \hat { c } h ^ { p + 2 } . } } \end{array}
$$

Now, since $\hat { e }$ is smaller than $e$ by the order of $h$ (which we assume to be a small quantity), one has

$$
e = | { \boldsymbol y } - { \boldsymbol \eta } | \approx | \hat { \pmb \eta } - { \boldsymbol \eta } | \quad ,
$$

which means that one is able to get an estimate of the local truncation error of the $p$ th-order formula from the difference of the two solutions. While this would also be possible with arbitrary methods of neighboring order, using an embedded method has the advantage of requiring only $s$ instead of $2 s { - 1 }$ function evaluations.

As an example Table 4.1 lists the coefficients of the embedded RK8(7)-13M method2 of Prince & Dormand (1981) which can be recommended as a general purpose method for a wide range of applications. A Fortran implementation (DO-PRI8) of this method is described in Hairer et al. (1987). Even though methods up to an order of 10 have been developed by some authors (Curtis 1975, Hairer 1978) they have not become widely accepted due to the lack of an embedded lower-order formula for stepsize control. Except for very high accuracies there seems to be no advantage of using them instead of DOPRI8 (Hairer et al. 1987).

# 4.1.3 Stepsize Control

During the numerical integration of a differential equation the stepsize should be chosen in such a way that each step contributes uniformly to the total integration error. While obviously a single step should not be too large, it should not be too short either, since this might increase the total number of steps, round-off errors, and the computational effort considerably. A common technique of stepsize control for Runge–Kutta methods is based on the error estimate available with embedded methods. It tries to limit the local truncation error $e$ , an estimate of which can be computed in each step.

Table 4.1. Coefficients of the RK8(7)-13 Runge–Kutta method for first-order differential equations by Prince & Dormand (1981).   

<table><tr><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>61911199</td><td rowspan=1 colspan=1>832553555</td><td rowspan=1 colspan=2>1155515115</td><td rowspan=1 colspan=3>985368895    3555555551</td><td rowspan=2 colspan=6>951000945                                    4555555550          0          0  0958611808                                    11551515</td><td rowspan=4 colspan=1>qq</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>33533555</td><td rowspan=1 colspan=1>898588555</td><td rowspan=1 colspan=2>3854515551</td><td rowspan=1 colspan=1>335555</td><td rowspan=1 colspan=2>1114445444</td></tr><tr><td rowspan=1 colspan=1>4222474711</td><td rowspan=1 colspan=1>183835355</td><td rowspan=1 colspan=1>1111151155</td><td rowspan=1 colspan=2>1711511355</td><td rowspan=1 colspan=1>111155451</td><td rowspan=1 colspan=2>11198855</td><td rowspan=1 colspan=1>111555</td><td rowspan=2 colspan=4>0          0          0  0</td><td rowspan=2 colspan=1>55335411445555</td></tr><tr><td rowspan=1 colspan=1>[55444814</td><td rowspan=1 colspan=1>115053844</td><td rowspan=1 colspan=1>111444555</td><td rowspan=1 colspan=2>115911150</td><td rowspan=1 colspan=1>58555555</td><td rowspan=1 colspan=2>L9L909181</td><td rowspan=1 colspan=1>33533556</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1111511555</td><td rowspan=1 colspan=1>955535555</td><td rowspan=1 colspan=2>0896408661</td><td rowspan=1 colspan=1>4111144545</td><td rowspan=1 colspan=2>955555555</td><td rowspan=1 colspan=1>409996446</td><td rowspan=1 colspan=2>553355555</td><td rowspan=1 colspan=2>44444444</td><td rowspan=1 colspan=1>61139551</td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>223359555</td><td rowspan=1 colspan=1>671855555</td><td rowspan=1 colspan=1>3555599939</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>11555551511</td><td rowspan=1 colspan=2>1181735555</td><td rowspan=1 colspan=1>55533555</td><td rowspan=1 colspan=1>451414411</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>333555335</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>44335355</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>180016585</td><td rowspan=1 colspan=1>1115555555</td><td rowspan=1 colspan=1>805889855</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>355995555</td><td rowspan=1 colspan=1>1115555555</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>235335311</td><td rowspan=1 colspan=1>1115555555</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>951151191</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1111515</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8598959</td><td rowspan=1 colspan=1>5553131551</td><td rowspan=1 colspan=2>2315535555</td><td rowspan=1 colspan=1>3535558352</td><td rowspan=1 colspan=1>5535555151</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>733553555</td><td rowspan=1 colspan=1>4444551144</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5555555511</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>111555111</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>517555355</td><td rowspan=1 colspan=2>939595833</td><td rowspan=1 colspan=1>1174538144</td><td rowspan=1 colspan=2>3553595555</td><td rowspan=1 colspan=1>1111531355</td><td rowspan=1 colspan=1>112443</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>55555552</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>500085954</td><td rowspan=1 colspan=1>86L6106671</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3855335553</td><td rowspan=1 colspan=2>48484884411</td><td rowspan=1 colspan=1>15555353145</td><td rowspan=1 colspan=2>6151555155</td><td rowspan=1 colspan=1>17765054155</td><td rowspan=1 colspan=1>1155111115</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3832553355</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>6818958505</td><td rowspan=1 colspan=1>1111411111</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>6816701001</td><td rowspan=1 colspan=1>1155393515</td><td rowspan=1 colspan=2>6981468015</td><td rowspan=1 colspan=1>116995555</td><td rowspan=1 colspan=1>1181553555</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>1557996544</td><td rowspan=1 colspan=1>1144451</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>111533311</td><td rowspan=1 colspan=1>35573331</td><td rowspan=1 colspan=2>365055555</td><td rowspan=1 colspan=1>11376655</td><td rowspan=1 colspan=1>505414541</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0  05575555515</td><td rowspan=1 colspan=1>266314545</td><td rowspan=1 colspan=1>m1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>8833331</td><td rowspan=1 colspan=2>83333</td><td rowspan=1 colspan=1>7133535</td><td rowspan=1 colspan=1>239659355</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>139111585</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>583555535</td><td rowspan=1 colspan=1>178691616</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>055555550</td><td rowspan=1 colspan=2>491440464</td><td rowspan=1 colspan=1>108030551</td><td rowspan=1 colspan=2>445711155</td><td rowspan=1 colspan=1>93335355</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>883553359</td><td rowspan=1 colspan=1>5453744544</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>1155531555</td><td rowspan=1 colspan=1>277115111</td><td rowspan=1 colspan=2>5544115</td><td rowspan=1 colspan=1>115533315</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16769961</td><td rowspan=1 colspan=1>000</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>199065185</td><td rowspan=1 colspan=1>53553555</td><td rowspan=1 colspan=2>22278315</td><td rowspan=1 colspan=1>18155559</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>1119111</td><td rowspan=1 colspan=1>£6</td></tr><tr><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>000000008I</td><td rowspan=1 colspan=2>1111000000</td><td rowspan=1 colspan=1>553335556</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>9566959</td><td rowspan=1 colspan=1>400</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>28245355</td><td rowspan=1 colspan=2>38833558</td><td rowspan=1 colspan=1>8155553</td><td rowspan=1 colspan=1>0  0</td><td rowspan=1 colspan=1>2483461</td><td rowspan=1 colspan=1>6</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>91</td><td rowspan=2 colspan=1>0  0</td><td rowspan=2 colspan=1>08m</td><td rowspan=2 colspan=1>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>m</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>91</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>SL</td><td rowspan=1 colspan=1>0SL</td><td rowspan=1 colspan=1>s</td><td rowspan=1 colspan=1>s</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>20m</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>911</td><td rowspan=1 colspan=1>81</td><td rowspan=1 colspan=1>181一0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>15</td></tr></table>

Suppose that a single integration step has been performed with a given stepsize $h$ yielding an estimate

$$
e ( h ) \approx | \hat { \pmb { \eta } } - \pmb { \eta } |
$$

for the local truncation error of the lower-order formula. If this value is larger than a tolerance $\varepsilon$ , the step has to be repeated with a smaller stepsize $h ^ { * }$ . Knowing that $e ( h )$ is proportional to $h ^ { p + 1 }$ for the method of order $p$ , the local truncation error will then be equal to

$$
e ( h ^ { * } ) = e ( h ) \left( \frac { h ^ { * } } { h } \right) ^ { p + 1 } \approx | \widehat { \eta } - \eta | \left( \frac { h ^ { * } } { h } \right) ^ { p + 1 }
$$

for the new stepsize. Requiring this to be smaller than $\varepsilon$ and solving for $h ^ { * }$ yields the maximum allowed stepsize

$$
h ^ { * } = { \sqrt [ { p + 1 } ] { \frac { \varepsilon } { e ( h ) } } } \cdot h \approx { \sqrt [ { p + 1 } ] { \frac { \varepsilon } { | { \hat { \eta } } - \eta | } } } \cdot h
$$

for repeating the step. In practice about 0.9 times this maximum value is commonly used for safety reasons to avoid another unsuccessful step. If the step was successful one may use $h ^ { * }$ for the next step. In order to avoid rapid oscillations of the stepsize, $h$ should not, however, be changed by more than a factor of 2 to 5 from one step to the next.

While this kind of stepsize control is well capable of adapting the current stepsize to the behavior of the differential equation, it does not relieve the user from supplying an initial guess of the starting stepsize. As long as one is concerned with a special type of problem, some test calculations and a bit of experience will certainly help to find a reasonable value. For the integration of a satellite orbit one may e.g. start with $h$ equal to 1/100 of the time of revolution, integrate over several orbits and monitor the stepsize calculated by the stepsize control. The obtained value may then be used as starting stepsize for similar calculations. Aside from this approach some methods have been devised to calculate an initial stepsize guess from several evaluations of the function $f$ (Watts 1983, Gladwell et al. 1987).

# 4.1.4 Runge–Kutta–Nyström Methods

Many problems in physics and especially the motion of artificial satellites and celestial bodies may be described by a second-order differential equation

$$
\ddot { \pmb { r } } = \pmb { a } ( t , \pmb { r } , \dot { \pmb { r } } )
$$

for the acceleration $\ddot { r }$ as a function of time $t$ , position $r$ and velocity $v = { \dot { r } }$ .

If one rewrites this second-order equation as a system of first-order equations, applies a standard Runge–Kutta method and keeps in mind the relation $c _ { i } = \sum a _ { i j }$ , one arrives at

$$
\begin{array} { r c l } { { r ( t _ { 0 } + h ) } } & { { = } } & { { { \displaystyle r _ { 0 } + h { \pmb v } _ { 0 } + h ^ { 2 } \sum _ { i } \bar { b } _ { i } { \pmb k } _ { i } ^ { \prime } } } } \\ { { } } & { { } } & { { } } \\ { { { \displaystyle v ( t _ { 0 } + h ) } } } & { { = } } & { { { \displaystyle v _ { 0 } + h \sum _ { i } b _ { i } { \pmb k } _ { i } ^ { \prime } } } } \end{array}
$$

with

$$
k _ { i } ^ { \prime } = a \left( t _ { 0 } + c _ { i } h , r _ { 0 } + c _ { i } h v _ { 0 } + h ^ { 2 } \sum _ { j } \bar { a } _ { i j } k _ { j } ^ { \prime } , v _ { 0 } + h \sum _ { j } a _ { i j } k _ { j } ^ { \prime } \right)
$$

and coefficients

$$
\bar { a } _ { i j } = \sum _ { k } a _ { i k } a _ { k j } \quad , \qquad \bar { b } _ { i } = \sum _ { j } b _ { j } a _ { j i } \quad .
$$

Runge–Kutta–Nyström methods differ from standard Runge–Kutta methods by using (4.23) and (4.24) in combination with coefficients that are especially adapted to the direct integration of second-order differential equations and do not necessarily obey equation (4.25). Several methods of this type have been developed by Fehlberg (1975), the highest of which is of order 7 and requires a total of 13 stages.

The advantages of Runge–Kutta–Nyström formulas over standard Runge– Kutta methods are most pronounced if the acceleration

$$
\pmb { \ddot { r } } = \pmb { a } ( t , \pmb { r } )
$$

does not depend on the velocity of the body. In this case special Runge–Kutta– Nyström methods may be derived that usually need a smaller number of stages to provide a given order of the local truncation error. An embedded 6(4)th-order method may be realized e.g. using 6 function evaluations (Dormand & Prince 1987), only, instead of 7 evaluations required by the Butcher barriers for standard Runge–Kutta methods.

Runge–Kutta–Nyström methods of order $p + 1 ( p )$ which allow for an easy stepsize control and are well suited for high accuracy requirements have been developed by Dormand & Prince (1978), Filippi & Gräf (1986) and Dormand et al. (1987). They are described by the equations

$$
\begin{array} { l c l } { \displaystyle k _ { i } } & { = } & { \displaystyle \vphantom { \displaystyle } a \left( { \displaystyle t _ { 0 } + \sum _ { i } h _ { i } } , { \bf r } _ { 0 } + c _ { i } h v _ { 0 } + h ^ { 2 } \sum _ { j = 0 } ^ { i - 1 } a _ { i j } k _ { j } \right) } \\ { \displaystyle } \\ { \displaystyle r ( t _ { 0 } + h ) } & { = } & { \displaystyle r _ { 0 } + h v _ { 0 } + h ^ { 2 } \sum _ { i = 0 } ^ { s } b _ { i } k _ { i } } & { \displaystyle e = O ( h ^ { p + 1 } ) } \\ { \displaystyle \vphantom { \displaystyle \frac { b } { b } } \hat { r } ( t _ { 0 } + h ) } & { = } & { \displaystyle r _ { 0 } + h v _ { 0 } + h ^ { 2 } \sum _ { i = 0 } ^ { s } \hat { b } _ { i } k _ { i } \hat { \quad \mathrm { ~ } } \hat { e } = O ( h ^ { p + 2 } ) } \\ { \displaystyle \hat { \upsilon } ( t _ { 0 } + h ) } & { = } & { \displaystyle \upsilon _ { 0 } + h \sum _ { i = 0 } ^ { s } \hat { b } _ { i } k _ { i } } \end{array}
$$

and coefficients

$$
\begin{array} { r }  \frac { \ C _ { s } = 1 } { \left| \begin{array} { l l l l l } { a _ { s 0 } } & { a _ { s 1 } } & { \dots } & { a _ { s , s - 1 } = 0 } \\ { b _ { 0 } = a _ { s 0 } } & { b _ { 1 } = a _ { s 1 } } & { \dots } & { b _ { s - 1 } = - \lambda } & { b _ { s } = \lambda } \\ { \hat { b } _ { 0 } = b _ { 0 } } & { \hat { b } _ { 1 } = b _ { 1 } } & { \dots } & { \hat { b } _ { s - 1 } = 0 } & { \hat { b } _ { s } = 0 } \\ { \hat { b } _ { 0 } } & { \hat { b } _ { 1 } } & { \dots } & { \hat { b } _ { s - 1 } } & { \hat { b } _ { s } } \end{array} \right. } \end{array}
$$

The formulas for $\hat { r }$ and $\hat { \pmb { v } }$ yield an approximation of position and velocity at $t _ { 0 } { + } h$ of order $p { + 1 }$ while $r$ gives an estimate of the local truncation error

$$
e \approx | \hat { \pmb { r } } - \pmb { r } | = \lambda h ^ { 2 } | \pmb { k } _ { s - 1 } - \pmb { k } _ { s } |
$$

of the embedded $p$ th-order formulas. This may then be used to control the stepsize using the same strategy that led to (4.21) for the classical Runge–Kutta methods:

$$
h ^ { \ast } = \sqrt [ p + 1 ] { \frac { \varepsilon } { e ( h ) } } \cdot h = \sqrt [ p + 1 ] { \frac { \varepsilon } { \lambda h ^ { 2 } | k _ { s - 1 } - k _ { s } | } } \cdot h \quad .
$$

The coefficient $\hat { b } _ { s } = \lambda > 0$ is a free parameter which is not determined by the order conditions. It does not affect the solution $r$ and $\pmb { v }$ , since it only appears in the stepsize control formula. By changing the value of $\lambda$ one may influence the estimation of the truncation error and adjust the value of $\varepsilon$ required to obtain a certain stepsize and error. Recommended values are usually given together with the other coefficients of the methods.

The special conditions $c _ { s } = 1$ and $b _ { i } = a _ { s i }$ for $i = 0 , \ldots , s - 1$ which are part of the design of these methods result in a saving of one evaluation of the function $\pmb { a }$ per step. This is due to the fact that the final function evaluation

$$
k _ { s } = \pmb { a } \left( t _ { 0 } + c _ { s } h , \pmb { r } _ { 0 } + c _ { s } h \pmb { v } _ { 0 } + h ^ { 2 } \sum _ { i = 0 } ^ { s - 1 } a _ { s i } \pmb { k } _ { i } \right)
$$

in the step from $t _ { 0 }$ to $t _ { 0 } + h$ is just the same as the first evaluation

$$
\begin{array} { l l l } { { k _ { 0 } } } & { { = } } & { { { \pmb a } \left( t _ { 0 } + h , { \pmb r } ( t _ { 0 } + h ) \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { { \pmb a } \left( t _ { 0 } + h , { \pmb r } _ { 0 } + h { \pmb v } _ { 0 } + h ^ { 2 } \displaystyle \sum _ { i = 0 } ^ { s - 1 } b _ { i } { \pmb k } _ { i } \right) } } \end{array}
$$

of the next step starting at $t _ { 0 } + h$ . It is, therefore, common to speak of $s$ -stage methods, even though an individual step actually requires $s + 1$ function values. As an example, the coefficients of the seventh-order method of Dormand & Prince (1978) are listed in Table 4.2. A Fortran subroutine that implements this method may be found in Hairer et al. (1987).

Table 4.2. Coefficients of the RKN7(6)-8 Runge–Kutta–Nyström method for special second-order differential equations by Dormand & Prince (1978).   

<table><tr><td></td><td colspan="8">[t）</td></tr><tr><td>0 1 10 1 3 8</td><td colspan="6"></td><td></td><td></td><td></td></tr><tr><td rowspan="12"></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>150</td><td>75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>171 8192</td><td>45 4096</td><td>315 8192</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>25</td><td>25</td><td>16</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>288</td><td>528</td><td>672</td><td>693</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7-√21</td><td>1003-205√21</td><td>751-173√21 -25-</td><td>624-137√21 25</td><td>361-79√21 -128</td><td>3411-745√21</td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>12348</td><td>90552</td><td>43218</td><td>237699</td><td></td><td>24696</td><td>581+ 127√21</td><td></td><td></td></tr><tr><td>7 +√21 14</td><td>793 + 187√21</td><td>331+113√21 -25</td><td>1044 + 247√21 25</td><td>14885+ 3779√21 -128</td><td></td><td>3327+ 797√21</td><td>1722</td><td></td><td></td></tr><tr><td></td><td>12348</td><td>90552</td><td>43218</td><td>9745659</td><td>24696</td><td></td><td>1777 + 377√21</td><td>5-√21</td><td></td></tr><tr><td rowspan="4">1</td><td>157-3√21 378</td><td>143-10√21 25 2772</td><td>876+55√21 -25</td><td>913+18√21 1280 596673</td><td>1353+26√21 2268</td><td></td><td>4428</td><td>36</td><td></td></tr><tr><td>1</td><td></td><td>3969</td><td></td><td></td><td>8</td><td></td><td></td><td></td></tr><tr><td>20</td><td>0</td><td>0</td><td>0</td><td></td><td>45</td><td>77+21 7 360</td><td>0 360</td><td></td></tr><tr><td>bi</td><td></td><td></td><td></td><td>0</td><td>8</td><td>77+21</td><td>77-21</td><td>0 0</td></tr><tr><td rowspan="4">bi</td><td>1</td><td>0</td><td>0</td><td></td><td></td><td>45</td><td>360</td><td>360</td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 20</td><td>0</td><td>0</td><td>0</td><td>8 45</td><td>77+√21 360</td><td>7-√21 7 360</td><td></td><td>-+λ</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b</td><td>1 20</td><td>0</td><td>0</td><td></td><td>0</td><td>16 45</td><td>49 180</td><td>49 1 180 20</td><td>0</td></tr></table>

# 4.1.5 Continuous Methods

In the discussion of stepsize control for Runge–Kutta methods no notice was taken of the fact that the solution of a differential equation is often required at predefined output points. This does not cause major problems as long as the difference between two subsequent points is considerably larger than the stepsize proposed by the stepsize control. If, however, the stepsize has to be truncated very often to reach predefined output points, the use of a Runge–Kutta method turns to be very ineffective. Considering the case of satellite orbits the problem of dense output may, for example, arise from ephemeris printout requirements or from the need for a smooth graphical representation of the orbit. Dense satellite position points are furthermore required for an iterative search for special events like shadow entries of a satellite.

The straightforward way to cope with this problem is to calculate the solution of the differential equation at widely spaced time steps and to interpolate it to the desired dense output points by means of an appropriate polynomial. A major disadvantage of this method is, however, that the results of subsequent Runge–Kutta integration steps have to be stored for interpolation similar to common multistep methods.

Within the last decades several authors (e.g. Horn 1981, 1983, Shampine 1985, Dormand & Prince 1986, 1987, Sharp & Verner 1998) have, therefore, been concerned with the design of interpolation formulas for Runge–Kutta methods that preserve the character of a single-step method. The idea of these formulas is to use the function values $k _ { i }$ (which have already been calculated to obtain the increment function $\Phi$ ) and a few additional evaluations to construct an interpolating polynomial valid between $\mathbf { \boldsymbol { y } } ( t _ { 0 } )$ and $\mathbf { y } ( t _ { 0 } + h )$ .

As an example of an interpolant, one of the first continuous methods, which has been proposed by Horn (1981, 1983), is described in what follows. It is based on the embedded 6-stage Runge–Kutta–Fehlberg method RKF4(5)

$$
\begin{array} { l c l c l } { { } } & { { } } & { { } } & { { } } & { { { } } } \\ { { } } & { { } } & { { } } & { { { k _ { i } } } } & { { { } } } & { { { } = } } & { { f ( t _ { 0 } + c _ { i } h , y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } k _ { j } ) \quad ( i = 1 \ldots 6 ) } } \\ { { } } & { { } } & { { } } & { { } } & { { { } } } \\ { { \hat { \eta } ( t _ { 0 } + h ) } } & { { = } } & { { \displaystyle y _ { 0 } + h \displaystyle \sum _ { i = 1 } ^ { 6 } \hat { b } _ { i } k _ { i } } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { { } } } \\ { { \eta ( t _ { 0 } + h ) } } & { { = } } & { { \displaystyle y _ { 0 } + h \displaystyle \sum _ { i = 1 } ^ { 5 } b _ { i } k _ { i } } } & { { } } & { { } } \end{array}
$$

which is defined by the coefficients of Table 4.3.

In addition to $\pmb { k } _ { 1 } \ldots \pmb { k } _ { 6 }$ , the method of Horn requires the value

$$
k _ { 7 } = f \left( t _ { 0 } + h , y _ { 0 } + h \left( { \frac { 1 } { 6 } } k _ { 1 } + { \frac { 1 } { 6 } } k _ { 5 } + { \frac { 2 } { 3 } } k _ { 6 } \right) \right)
$$

![](images/6c0971234bcabeba047b08b29ad2d72500bac8116b32eece750a75d4e6c71c22.jpg)  
Table 4.3. Coefficients of the 6-stage Runge–Kutta–Fehlberg method RKF4(5) for use with the interpolant of Horn (1981, 1983)

to compute the solution at any point between $t _ { 0 }$ and $t _ { 0 } + h$ . For $0 \textless \sigma \textless 1$ an approximation at $t = t _ { 0 } + \sigma h$ may be obtained from

$$
\pmb { \eta } ( t _ { 0 } + \sigma h ) = \mathbf { y } _ { 0 } + \sigma h \sum _ { i = 1 } ^ { 7 } b _ { i } ^ { * } ( \sigma ) \mathbf { k } _ { i }
$$

where the coefficients $b _ { i } ^ { * }$ are polynomials in the independent variable $\sigma$ . They are defined as:

$$
\begin{array} { r c l } { { b _ { 1 } ^ { * } } } & { { = } } & { { 1 - \sigma \left( \frac { 3 0 1 } { 1 2 0 } + \sigma \left( - \frac { 2 6 9 } { 1 0 8 } + \sigma \frac { 3 1 1 } { 3 6 0 } \right) \right) } } \\ { { b _ { 2 } ^ { * } } } & { { = } } & { { 0 } } \\ { { b _ { 3 } ^ { * } } } & { { = } } & { { \sigma \left( \frac { 7 1 6 8 } { 1 4 2 5 } + \sigma \left( - \frac { 4 0 9 6 } { 5 1 3 } + \sigma \frac { 1 4 8 4 8 } { 4 2 7 5 } \right) \right) } } \\ { { b _ { 4 } ^ { * } } } & { { = } } & { { \sigma \left( - \frac { 2 8 5 6 1 } { 8 3 6 0 } + \sigma \left( \frac { 1 9 9 9 2 7 } { 2 2 5 7 2 } - \sigma \frac { 3 7 1 2 9 3 } { 7 5 2 4 0 } \right) \right) } } \\ { { b _ { 5 } ^ { * } } } & { { = } } & { { \sigma \left( \frac { 5 7 } { 5 0 } + \sigma \left( - 3 + \sigma \frac { 4 2 } { 2 5 } \right) \right) } } \\ { { b _ { 6 } ^ { * } } } & { { = } } & { { \sigma \left( - \frac { 9 6 } { 5 5 } + \sigma \left( \frac { 4 0 } { 1 1 } - \sigma \frac { 1 0 2 } { 5 5 } \right) \right) } } \\ { { b _ { 7 } ^ { * } } } & { { = } } & { { \sigma \left( \frac { 3 } { 2 } + \sigma \left( - 4 + \sigma \frac { 5 } { 2 } \right) \right) . } } \end{array}
$$

Intermediate values of the solution may thus be obtained at the expense of evaluating several polynomials instead of $f$ which usually results in a considerable saving of computing time if dense output is required.

The algorithm of Horn is given here as a simple example of an interpolation formula for Runge–Kutta methods. It is intended to illustrate the basic ideas but is not necessarily the most efficient solution for practical applications. A different approach that is based on the RKF4(5) method, too, but uses $\scriptstyle { y _ { 0 } }$ and $\eta ( t _ { 0 } + h )$ in addition to the $k _ { i }$ is e.g. described in Enright et al. (1986).

Up to some time ago interpolants were only available for several methods of intermediate order. Recently, however, a 7th-order interpolant based on an embedded 8(6)th-order/12-stage Runge–Kutta pair has been announced by Dormand & Prince (1989). This interpolation formula requires four function evaluations in addition to those of the basic method.

Dense output formulas have also been developed for several Runge–Kutta– Nyström methods. A 6th-order interpolant is, for example, available for the RKN6(4) pair of Dormand & Prince (1987) and the authors are concerned with the search for an interpolant for their 12(10)th-order pair (see Brankin et al. 1989).

# 4.1.6 Comparison of Runge–Kutta Methods

For the assessment of different numerical integration methods several sets of test problems have been developed by Hull et al. (1972) which greatly facilitate the comparison of performance data obtained by different authors. From the various test problems proposed by Hull et al. the plane two-body problem is frequently used by many authors and describes the main aspects of satellite motion very well. Even though it is not possible to cover all aspects that might affect the choice of an integration method by such a simple example, one can get a first idea of the performance of the Runge–Kutta methods discussed so far. For further discussion the reader is referred to Sect. 4.4.

The differential equation of the two-body problem is given by

$$
\begin{array} { r c l } { { \dot { y } _ { 1 } } } & { { = } } & { { y _ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { \dot { y } _ { 2 } } } & { { = } } & { { y _ { 4 } } } \\ { { } } & { { } } & { { } } \\ { { \dot { y } _ { 3 } } } & { { = } } & { { - y _ { 1 } / ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { \dot { y } _ { 4 } } } & { { = } } & { { - y _ { 2 } / ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } ~ , } } \end{array}
$$

which results from writing $\ddot { r } = - r / r ^ { 3 }$ as a first-order equation with $\boldsymbol { r } = ( y _ { 1 } , y _ { 2 } )$ and $\pmb { v } = ( y _ { 3 } , y _ { 4 } )$ . Initial values for $t = 0$ that describe an orbit with semi-major axis $a = 1$ and eccentricity $e$ starting at pericenter are given by

$$
\begin{array} { l c l } { { y _ { 1 } ( 0 ) } } & { { = } } & { { 1 - e } } \\ { { y _ { 2 } ( 0 ) } } & { { = } } & { { 0 } } \\ { { y _ { 3 } ( 0 ) } } & { { = } } & { { 0 } } \\ { { y _ { 4 } ( 0 ) } } & { { = } } & { { \sqrt { ( 1 + e ) / ( 1 - e ) } \enspace . } } \end{array}
$$

Since the velocity variations in an eccentric orbit are a crucial test for the capability of a numerical integration method to change its stepsize, Hull et al. (1972) defined the distinct test problems D1 to D5 with eccentricities ranging from $e = 0 . 1$ to $e { = } 0 . 9$ in steps of 0.2. The stop time is defined as $t = 2 0$ in all cases, corresponding