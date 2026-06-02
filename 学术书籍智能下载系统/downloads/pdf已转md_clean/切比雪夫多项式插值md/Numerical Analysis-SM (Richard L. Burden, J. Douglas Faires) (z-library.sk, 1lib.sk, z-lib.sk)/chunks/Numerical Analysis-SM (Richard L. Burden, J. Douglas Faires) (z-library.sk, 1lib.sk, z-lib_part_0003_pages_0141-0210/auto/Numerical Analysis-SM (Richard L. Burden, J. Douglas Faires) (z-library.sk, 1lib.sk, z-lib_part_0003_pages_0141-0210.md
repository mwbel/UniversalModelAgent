<table><tr><td>i</td><td>t</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.1633541</td><td>-1.8380836</td><td>0.1633541</td><td>-1.8380836</td></tr><tr><td>5</td><td>0.7585763</td><td>-1.3597623</td><td>0.1266248</td><td>-1.3597624</td></tr><tr><td>9</td><td>1.1930325</td><td>-1.1684827</td><td>0.1048224</td><td>-1.1684830</td></tr><tr><td>13</td><td>1.6229351</td><td>-1.0749509</td><td>0.1107510</td><td>-1.0749511</td></tr><tr><td>17</td><td>2.1074733</td><td>-1.0291158</td><td>0.1288897</td><td>-1.0291161</td></tr><tr><td>23</td><td>3.0000000</td><td>-1.0049450</td><td>0.1264618</td><td>-1.0049452</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.3986051</td><td>0.3108201</td><td>0.3986051</td><td>0.3108199</td></tr><tr><td>3</td><td>0.9703970</td><td>0.2221189</td><td>0.2866710</td><td>0.2221186</td></tr><tr><td>5</td><td>1.5672905</td><td>0.1133085</td><td>0.3042087</td><td>0.1133082</td></tr><tr><td>8</td><td>2.0000000</td><td>0.0543454</td><td>0.0902302</td><td>0.0543455</td></tr></table>

4. Steps 3 and 6 must use the new equations. Step 4 must now use

$$
R = \frac { 1 } { h } \bigg | - \frac { 1 } { 1 6 0 } K _ { 1 } - \frac { 1 2 5 } { 1 7 9 5 2 } K _ { 3 } + \frac { 1 } { 1 4 4 } K _ { 4 } - \frac { 1 2 } { 1 9 5 5 } K _ { 5 } - \frac { 3 } { 4 4 } K _ { 6 } + \frac { 1 2 5 } { 1 1 5 9 2 } K _ { 7 } + \frac { 4 3 } { 6 1 6 } K _ { 8 } \bigg | ,
$$

and in Step 8 we must change to $\delta = 0 . 8 7 1 ( T O L / R ) ^ { 1 / 5 }$ . Repeating Exercise 3 using the Runge-Kutta-Verner method gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.42087564</td><td>1.05149775</td><td>0.42087564</td><td>1.05150868</td></tr><tr><td>3</td><td>2.28874724</td><td>1.25203709</td><td>0.50000000</td><td>1.25204675</td></tr><tr><td>5</td><td>3.28874724</td><td>1.50135401</td><td>0.50000000</td><td>1.50136369</td></tr><tr><td>7</td><td>4.00000000</td><td>1.67622922</td><td>0.21125276</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.27377960</td><td>0.31440170</td><td>0.27377960</td><td>0.31440111</td></tr><tr><td>4</td><td>1.93610139</td><td>1.50471956</td><td>0.20716801</td><td>1.50471717</td></tr><tr><td>7</td><td>2.48318866</td><td>3.19129592</td><td>0.17192536</td><td>3.19129017</td></tr><tr><td>11</td><td>3.00000000</td><td>5.87411325</td><td>0.05925262</td><td>5.87409998</td></tr></table>

(c)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.50000000</td><td>-1.53788271</td><td>0.50000000</td><td>-1.53788284</td></tr><tr><td>5</td><td>1.26573379</td><td>-1.14736319</td><td>0.17746598</td><td>-1.14736283</td></tr><tr><td>9</td><td>1.99742532</td><td>-1.03615509</td><td>0.19229794</td><td>-1.03615478</td></tr><tr><td>14</td><td>3.00000000</td><td>-1.00494544</td><td>0.10525374</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.50000000</td><td>0.29875168</td><td>0.50000000</td><td>0.29875178</td></tr><tr><td>2</td><td>1.00000000</td><td>0.21662609</td><td>0.50000000</td><td>0.21662642</td></tr><tr><td>4</td><td>1.74337091</td><td>0.08624885</td><td>0.27203938</td><td>0.08624932</td></tr><tr><td>6</td><td>2.00000000</td><td>0.05434531</td><td>0.03454832</td><td>0.05434551</td></tr></table>

5. (a) The number of infectives is $y ( 3 0 ) \approx 8 0 2 9 5 . 7$ . (b) The limiting value for the number of infectives for this model is $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } y ( t ) = 1 0 0 , 0 0 0 } \end{array}$ .

6. With $T O L = 0 . 0 1$ , $H M I N = 0 . 0 1$ , $H M A X = 1$ , we have

$$
z ( 3 0 ) \approx 8 1 , \quad x ( 3 0 ) \approx 1 9 7 5 4 , \quad \mathrm { a n d } \quad y ( 3 0 ) \approx 8 0 1 6 5 .
$$

# Exercise Set 5.6, page 314

1. The Adams-Bashforth methods give the results in the following tables.

\*(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td></tr><tr><td>0.4</td><td>0.1200522</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td></tr><tr><td>0.6</td><td>0.4153551</td><td>0.4613866</td><td>0.4960196</td><td>0.4960196</td><td>0.4960196</td></tr><tr><td>0.8</td><td>1.1462844</td><td>1.2512447</td><td>1.2961260</td><td>1.3308570</td><td>1.3308570</td></tr><tr><td>1.0</td><td>2.8241683</td><td>3.0360680</td><td>3.1461400</td><td>3.1854002</td><td>3.2190993</td></tr><tr><td>2.2</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td></tr><tr><td>2.4</td><td>1.6750000</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td></tr><tr><td>2.6</td><td>1.9632431</td><td>1.9794407</td><td>1.9750000</td><td>1.9750000</td><td>1.9750000</td></tr><tr><td>2.8</td><td>2.2323184</td><td>2.2488759</td><td>2.2423065</td><td>2.2444444</td><td>2.2444444</td></tr><tr><td>3.0</td><td>2.4884512</td><td>2.5051340</td><td>2.4980306</td><td>2.5011406</td><td>2.5000000</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2734823</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9567107</td><td>3.9514231</td><td>3.9520058</td><td>3.9520058</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6647738</td><td>4.6569191</td><td>4.6582078</td><td>4.6580160</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3949416</td><td>5.3848058</td><td>5.3866452</td><td>5.3862177</td><td>5.3862944</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5986417</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.9386951</td><td>1.8827238</td><td>1.8750869</td><td>1.8750869</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.1766821</td><td>2.0844122</td><td>2.0698063</td><td>2.0789180</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.2369407</td><td>2.1115540</td><td>2.0998117</td><td>2.1180642</td><td>2.1179795</td></tr></table>

2. The Adams-Bashforth methods give the results in the following tables.

(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.349857812</td><td></td><td></td><td></td><td>1.346153846</td></tr><tr><td>0.4</td><td>1.556590819</td><td>1.548505437</td><td>1.551742825</td><td></td><td>1.551724138</td></tr><tr><td>0.6</td><td>1.618098483</td><td>1.613103414</td><td>1.618495896</td><td>1.618045413</td><td>1.617647059</td></tr><tr><td>0.8</td><td>1.581123788</td><td>1.581537429</td><td>1.586784646</td><td>1.585534486</td><td>1.585365854</td></tr><tr><td>1.0</td><td>1.493132968</td><td>1.497482321</td><td>1.501365685</td><td>1.499907131</td><td>1.5</td></tr></table>

(b)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>-1.270097903</td><td></td><td></td><td></td><td>-1.268299404</td></tr><tr><td>1.4</td><td>-1.145585721</td><td>-1.14555416</td><td>-1.142395930</td><td></td><td>-1.142245242</td></tr><tr><td>1.6</td><td>-1.050436722</td><td>-1.045646519</td><td>-1.046822255</td><td>-1.046486051</td><td>-1.046559939</td></tr><tr><td>1.8</td><td>-0.9752223844</td><td>-0.9702763545</td><td>-0.9715163192</td><td>-0.9711385301</td><td>-0.9712326550</td></tr><tr><td>2.0</td><td>-0.9141608282</td><td>-0.9093053788</td><td>-0.9105163922</td><td>-0.9101442242</td><td>-0.9102392264</td></tr></table>

(c)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t）</td></tr><tr><td>1.4</td><td>-1.608147341</td><td></td><td></td><td></td><td>-1.555555556</td></tr><tr><td>1.8</td><td>-1.1429612993</td><td>-1.359101590</td><td>-1.404013030</td><td></td><td>-1.384615385</td></tr><tr><td>2.2</td><td>-1.331187984</td><td>-1.269164344</td><td>-1.314903737</td><td>-1.283404253</td><td>-1.294117647</td></tr><tr><td>2.6</td><td>-1.268712599</td><td>-1.217326056</td><td>-1.253881487</td><td>-1.229097787</td><td>-1.238095238</td></tr><tr><td>3.0</td><td>-1.225776866</td><td>-1.182688385</td><td>-1.212496957</td><td>-1.192208061</td><td>－1.200000000</td></tr></table>

(d)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td> 5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.058717655</td><td></td><td></td><td></td><td>1.057181007</td></tr><tr><td>0.4</td><td>1.207722688</td><td>1.202476610</td><td>1.200816932</td><td></td><td>1.201486010</td></tr><tr><td>0.6</td><td>1.389363032</td><td>1.381043540</td><td>1.379947852</td><td>1.381296110</td><td>1.380931216</td></tr><tr><td>0.8</td><td>1.562852894</td><td>1.554374654</td><td>1.554384988</td><td>1.555455875</td><td>1.555031423</td></tr><tr><td>1.0</td><td>1.707692156</td><td>1.700926322</td><td>1.701562220</td><td>1.702136018</td><td>1.701870053</td></tr></table>

3. The Adams-Bashforth methods give the results in the following tables.

(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>1.0161982</td><td>1.0149520</td><td>1.0149520</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.4</td><td>1.0497665</td><td>1.0468730</td><td>1.0477278</td><td>1.0475336</td><td>1.0475339</td></tr><tr><td>1.6</td><td>1.0910204</td><td>1.0875837</td><td>1.0887567</td><td>1.0883045</td><td>1.0884327</td></tr><tr><td>1.8</td><td>1.1363845</td><td>1.1327465</td><td>1.1340093</td><td>1.1334967</td><td>1.1336536</td></tr><tr><td>2.0</td><td>1.1840272</td><td>1.1803057</td><td>1.1815967</td><td>1.1810689</td><td>1.1812322</td></tr><tr><td>1.4</td><td>0.4867550</td><td>0.4896842</td><td>0.4896842</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.8</td><td>1.1856931</td><td>1.1982110</td><td>1.1990422</td><td>1.1994320</td><td>1.1994386</td></tr><tr><td>2.2</td><td>2.1753785</td><td>2.2079987</td><td>2.2117448</td><td>2.2134792</td><td>2.2135018</td></tr><tr><td>2.6</td><td>3.5849181</td><td>3.6617484</td><td>3.6733266</td><td>3.6777236</td><td>3.6784753</td></tr><tr><td>3.0</td><td>5.6491203</td><td>5.8268008</td><td>5.8589944</td><td>5.8706101</td><td>5.8741000</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.5</td><td>-1.5357010</td><td>-1.5381988</td><td>-1.5379372</td><td>-1.5378676</td><td>-1.5378828</td></tr><tr><td>1.0</td><td>-1.2374093</td><td>-1.2389605</td><td>-1.2383734</td><td>-1.2383693</td><td>-1.2384058</td></tr><tr><td>1.5</td><td>-1.0952910</td><td>-1.0950952</td><td>-1.0947925</td><td>-1.0948481</td><td>-1.0948517</td></tr><tr><td>2.0</td><td>-1.0366643</td><td>-1.0359996</td><td>-1.0359497</td><td>-1.0359760</td><td>-1.0359724</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>0.1739041</td><td>0.1627655</td><td>0.1627655</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.4</td><td>0.2144877</td><td>0.2026399</td><td>0.2066057</td><td>0.2052405</td><td>0.2051118</td></tr><tr><td>0.6</td><td>0.3822803</td><td>0.3747011</td><td>0.3787680</td><td>0.3765206</td><td>0.3765957</td></tr><tr><td>0.8</td><td>0.6491272</td><td>0.6452640</td><td>0.6487176</td><td>0.6471458</td><td>0.6461052</td></tr><tr><td>1.0</td><td>1.0037415</td><td>1.0020894</td><td>1.0064121</td><td>1.0073348</td><td>1.0022460</td></tr></table>

4. The Adams-Moulton methods give the results in the following tables.

(1a)

<table><tr><td>ti</td><td>2-step</td><td>3-step</td><td>4-step</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td></tr><tr><td>0.4</td><td>0.1533627</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td></tr><tr><td>0.6</td><td>0.5030068</td><td>0.4979042</td><td>0.4960196</td><td>0.4960196</td></tr><tr><td>0.8</td><td>1.3463142</td><td>1.3357923</td><td>1.3322919</td><td>1.3308570</td></tr><tr><td>1.0</td><td>3.2512866</td><td>3.2298092</td><td>3.2227484</td><td>3.2190993</td></tr><tr><td>1.2</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2711394</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9521454</td><td>3.9519886</td><td>3.9520058</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6582064</td><td>4.6579866</td><td>4.6580211</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3865293</td><td>5.3862558</td><td>5.3863027</td><td>5.3862944</td></tr></table>

(1d)

<table><tr><td>ti</td><td>2-step</td><td>3-step</td><td>4-step</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5700866</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.8738414</td><td>1.8757546</td><td>1.8750869</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.0787117</td><td>2.0803067</td><td>2.0789471</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.1196912</td><td>2.1199024</td><td>2.1178679</td><td>2.1179795</td></tr></table>

5. Algorithm 5.4 gives the results in the following tables.

<table><tr><td rowspan="2">*（a)</td><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.2</td><td>0.0269059</td><td>0.0268128</td></tr><tr><td></td><td>0.4</td><td>0.1510468</td><td>0.1507778</td></tr><tr><td></td><td>0.6</td><td>0.4966479</td><td>0.4960196</td></tr><tr><td></td><td>0.8</td><td>1.3408657</td><td>1.3308570</td></tr><tr><td></td><td>1.0</td><td>3.2450881</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.2</td><td>1.3666610</td><td>1.3666667</td></tr><tr><td>2.4</td><td>1.6857079</td><td>1.6857143</td></tr><tr><td>2.6</td><td>1.9749941</td><td>1.9750000</td></tr><tr><td>2.8</td><td>2.2446995</td><td>2.2444444</td></tr><tr><td>3.0</td><td>2.5003083</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>2.6187787</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2710491</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9519900</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6579968</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3862715</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="2">(d)</td><td>y(ti)</td></tr><tr><td>ti</td><td>Wi</td><td></td></tr><tr><td>0.2</td><td>1.2529350</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5712383</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.8751097</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.0796618</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.1192575</td><td>2.1179795</td></tr></table>

6. Algorithm 5.4 gives the results in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td></td></tr><tr><td>ti Wi</td></tr><tr><td>0.2</td><td>1.3461536</td></tr><tr><td>0.4</td><td>1.5516984</td></tr><tr><td>0.6</td><td>1.6175240</td></tr><tr><td>0.8</td><td>1.5851977</td></tr><tr><td>1.0</td><td>1.4998499</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td></td></tr><tr><td>1.2</td><td>-1.2682994</td></tr><tr><td>1.4</td><td>-1.1422321</td></tr><tr><td>1.6</td><td>-1.0465369</td></tr><tr><td>1.8</td><td>-0.9712077</td></tr><tr><td>2.0</td><td>-0.9102149</td></tr></table>

<table><tr><td rowspan="3">C</td><td></td></tr><tr><td></td></tr><tr><td>ti Wi</td></tr><tr><td>1.2</td><td>-1.7142452</td></tr><tr><td>1.6</td><td>-1.4545197</td></tr><tr><td>2.0</td><td>-1.3312918</td></tr><tr><td>2.4</td><td>-1.2614431</td></tr><tr><td>2.8</td><td>-1.2159883</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2"></td></tr><tr><td>ti</td><td>Wi</td></tr><tr><td>0.2</td><td>1.0571822</td></tr><tr><td>0.4</td><td>1.2015654</td></tr><tr><td>0.6</td><td>1.3810423</td></tr><tr><td>0.8</td><td>1.5550968</td></tr><tr><td>1.0</td><td>1.7018941</td></tr></table>

7. The Adams Fourth-order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td>(a) t</td><td>y(t) w</td></tr><tr><td>1.2 1.0149520</td><td>1.0149523</td></tr><tr><td>1.4 1.0475227</td><td>1.0475339</td></tr><tr><td>1.6 1.0884141</td><td>1.0884327</td></tr><tr><td>1.8</td><td>1.1336331 1.1336536</td></tr><tr><td>2.0 1.1812112</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td>t</td><td>w</td><td>y(t)</td></tr><tr><td>.4</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.8</td><td>1.1994245</td><td>1.1994386</td></tr><tr><td>2.2</td><td>2.2134701</td><td>2.2135018</td></tr><tr><td>2.6</td><td>3.6784144</td><td>3.6784753</td></tr><tr><td>3.0</td><td>5.8739518</td><td>5.8741000</td></tr></table>

<table><tr><td colspan="2"></td></tr><tr><td colspan="2"></td></tr><tr><td>t</td><td>w</td></tr><tr><td>0.5</td><td>-1.5378788 -1.5378828</td></tr><tr><td>1.0</td><td>-1.2384134 -1.2384058</td></tr><tr><td>1.5</td><td>-1.0948609 -1.0948517</td></tr><tr><td>2.0</td><td>-1.0359757 -1.0359724</td></tr></table>

<table><tr><td>(d) t</td><td>y(t) w</td></tr><tr><td>0.2 0.1627655</td><td>0.1626265</td></tr><tr><td>0.4 0.2048557</td><td>0.2051118</td></tr><tr><td>0.6 0.3762804</td><td>0.3765957</td></tr><tr><td>0.8 0.6458949</td><td>0.6461052</td></tr><tr><td>1.0 1.0021372</td><td>1.0022460</td></tr></table>

8. The new algorithm gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>Wi(p= 2)</td><td>Wi(p = 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149520</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672499</td><td>1.0672499</td><td>1.0672499</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106394</td><td>1.1106394</td><td>1.1106394</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812154</td><td>1.1812154</td><td>1.1812154</td><td>1.1812322</td></tr></table>

<table><tr><td>ti</td><td>Wi(p = 2)</td><td>Wi(p= 3)</td><td>wi(p = 4)</td><td>y(ti)</td></tr><tr><td>1.4</td><td>0.4896842</td><td>0.4896842</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>2.0</td><td>1.6613427</td><td>1.6613509</td><td>1.6613517</td><td>1.6612818</td></tr><tr><td>2.4</td><td>2.8767835</td><td>2.8768112</td><td>2.8768140</td><td>2.8765514</td></tr><tr><td>3.0</td><td>5.8754422</td><td>5.8756045</td><td>5.8756224</td><td>5.8741000</td></tr></table>

<table><tr><td>ti</td><td>Wi(p= 2)</td><td>wi(p = 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6200494</td><td>-1.6200494</td><td>-1.6200494</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2384104</td><td>-1.2384105</td><td>-1.2384105</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1146533</td><td>-1.1146536</td><td>-1.1146536</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0359139</td><td>-1.0359740</td><td>-1.0359740</td><td>-1.0359724</td></tr></table>

<table><tr><td>ti</td><td>Wi(p=2)</td><td>Wi(p= 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1627655</td><td>0.1627655</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2774037</td><td>0.2773333</td><td>0.2773468</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5000772</td><td>0.5000259</td><td>0.5000356</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0022473</td><td>1.0022273</td><td>1.0022311</td><td>1.0022460</td></tr></table>

9. (a) With $h = 0 . 0 1$ , the three-step Adams-Moulton method gives the values in the following table.

<table><tr><td>i</td><td>ti</td></tr><tr><td>10 0.1</td><td>1.317218</td></tr><tr><td>20</td><td>0.2 1.784511</td></tr></table>

(b) Newton’s method will reduce the number of iterations per step from three to two, using the stopping criterion

$$
| w _ { i } ^ { ( k ) } - w _ { i } ^ { ( k - 1 ) } | \leq 1 0 ^ { - 6 } .
$$

10. Milne-Simpson’s Predictor-Corrector method gives the results in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>1.2</td><td>1.01495200</td><td>1.01495231</td></tr><tr><td>5</td><td>1.5</td><td>1.06725997</td><td>1.06726235</td></tr><tr><td>7</td><td>1.7</td><td>1.11065221</td><td>1.11065505</td></tr><tr><td>10</td><td>2.0</td><td>1.18122584</td><td>1.18123222</td></tr></table>

<table><tr><td rowspan="2">(b)</td><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>2</td><td>1.4</td><td>0.48968417</td><td>0.48968166</td></tr><tr><td></td><td>5</td><td>2.0</td><td>1.66126150</td><td>1.66128176</td></tr><tr><td></td><td>7</td><td>2.4</td><td>2.87648763</td><td>2.87655142</td></tr><tr><td></td><td>10</td><td>3.0</td><td>5.87375555</td><td>5.87409998</td></tr></table>

<table><tr><td rowspan="2">(c)</td><td rowspan="2"></td><td colspan="6">(d)</td></tr><tr><td>Wi</td><td>y(ti)</td><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>5</td><td>0.5</td><td>-1.53788255</td><td>-1.53788284</td><td>2</td><td>0.2</td><td>0.16276546</td><td>0.16262648</td></tr><tr><td>10</td><td>1.0</td><td>-1.23840789</td><td>-1.23840584</td><td>5</td><td>0.5</td><td>0.27741080</td><td>0.27736167</td></tr><tr><td>15</td><td>1.5</td><td>-1.09485532</td><td>-1.09485175</td><td>7</td><td>0.7</td><td>0.50008713</td><td>0.50006579</td></tr><tr><td>20</td><td>2.0</td><td>-1.03597247</td><td>-1.03597242</td><td>10</td><td>1.0</td><td>1.00215439</td><td>1.00224598</td></tr></table>

11. $^ *$ (a) For some $\xi _ { i }$ in $( t _ { i - 1 } , t _ { i } )$ ,

$$
f ( t , y ( t _ { i } ) ) = P _ { 1 } ( t ) + \frac { f ^ { \prime \prime } ( \xi _ { i } , y ( \xi _ { i } ) ) } { 2 } ( t - t _ { i } ) ( t - t _ { i - 1 } ) ,
$$

where $P _ { 1 } ( t )$ is the linear Lagrange polynomial

$$
P _ { 1 } ( t ) = \frac { ( t - t _ { i - 1 } ) } { ( t _ { i } - t _ { i - 1 } ) } f ( t _ { i } , y ( t _ { i } ) ) + \frac { ( t - t _ { i } ) } { ( t _ { i - 1 } - t _ { i } ) } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) .
$$

Thus

$$
\begin{array} { l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } P _ { 1 } ( t ) ~ d t = \frac { f ( t _ { i } , y ( t _ { i } ) ) } { t _ { i } - t _ { i - 1 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ~ d t + \frac { f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } { t _ { i - 1 } - t _ { i } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ~ d t } \\ { \displaystyle \qquad = \frac { 3 h } { 2 } f ( t _ { i } , y ( t _ { i } ) ) - \frac { h } { 2 } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) . } \end{array}
$$

Since $( t - t _ { i } ) ( t - t _ { i - 1 } )$ does not change sign on $\left( { { t } _ { i } } , { { t } _ { i + 1 } } \right)$ , the Mean Value Theorem for Integrals gives

$$
\begin{array} { r l } & { \int _ { t _ { i } } ^ { t _ { i + 1 } } \frac { f ^ { \prime \prime } ( \xi _ { i } , y ( \xi _ { i } ) ) ( t - t _ { i } ) ( t - t _ { i - 1 } ) } { 2 } d t = \frac { f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 2 } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ( t - t _ { i - 1 } ) d t } \\ & { \qquad = \frac { 5 h ^ { 2 } f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 1 2 } . } \end{array}
$$

Replacing $y ( t _ { j } )$ with $w _ { j }$ , for $j = i - 1 , i$ , and $i + 1$ in the formula

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t
$$

gives

$$
w _ { i + 1 } = w _ { i } + { \frac { h \left[ 3 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) \right] } { 2 } } ,
$$

and the local truncation error is

$$
\tau _ { i + 1 } ( h ) = \frac { 5 h ^ { 2 } y ^ { \prime \prime \prime } ( \mu ) } { 1 2 } ,
$$

for some $\mu$ in $( t _ { i - 1 } , t _ { i + 1 } )$

(b) Using the backward difference polynomial with $m = 4$ gives

$$
\begin{array} { l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = \sum _ { k = 0 } ^ { 3 } \nabla ^ { k } f ( t _ { i } , y ( t _ { i } ) ) h ( - 1 ) ^ { k } \int _ { 0 } ^ { 1 } \left( \begin{array} { c } { - s } \\ { k } \end{array} \right) d s } \\ { \displaystyle \qquad + \frac { h ^ { 5 } } { 2 4 } \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) f ^ { ( 4 ) } ( \xi _ { i } , y ( \xi _ { i } ) ) \ d s . } \end{array}
$$

From Table 5.10 we have,

$$
\begin{array} { r l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = h \biggl [ f ( t _ { i } , y ( t _ { i } ) ) + \frac { 1 } { 2 } \nabla f ( t _ { i } , y ( t _ { i } ) ) + \frac { 5 } { 1 2 } \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) } & { } \\ { \displaystyle } & { \qquad + \frac { 3 } { 8 } \nabla ^ { 3 } f ( t _ { i } , y ( t _ { i } ) ) \biggr ] } \\ { \displaystyle } & { \qquad + \frac { h ^ { 5 } } { 2 4 } \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) f ^ { ( 4 ) } ( \xi _ { i } , y ( \xi _ { i } ) ) \ d s . } \end{array}
$$

Since

$$
\begin{array} { r l } & { \nabla f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) , } \\ & { \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - 2 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) , } \\ & { \nabla ^ { 3 } f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - 3 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 3 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) - f ( t _ { i - 3 } , y ( t _ { i - 3 } ) ) , } \end{array}
$$

and $s ( s + 1 ) ( s + 2 ) ( s + 3 )$ does not change sign on $( 0 , 1 )$ , we can simplify this and use the Mean Value Theorem for Integrals to obtain

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = h \biggl [ 5 5 f ( t _ { i } , y ( t _ { i } ) ) - 5 9 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 3 7 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) } \\ & { \qquad \quad - \ 9 f ( t _ { i - 3 } , y ( t _ { i - 3 } ) ) \biggr ] + \frac { h ^ { 5 } } { 2 4 } f ^ { ( 4 ) } ( \mu , y ( \mu ) ) \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) \ d s } \end{array}
$$

for some $\mu$ in $( t _ { i - 3 } , t _ { i + 1 } )$ . The local truncation error form follows from the fact that

$$
\int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) \ d s = { \frac { 2 5 1 } { 3 0 } } .
$$

$^ { \ast } 1 2$ . Using the notation $y = y ( t _ { i } )$ $\mathsf { \Phi } = y ( t _ { i } ) , f = f ( t _ { i } , y ( t _ { i } ) ) , f _ { t } = f _ { t } ( t _ { i } , y ( t _ { i } ) )$ , etc., we have

$$
\begin{array} { l } { { \displaystyle y + h f + \frac { h ^ { 2 } } { 2 } ( f _ { t } + f f _ { y } ) + \frac { h ^ { 3 } } { 6 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) } } \\ { { \displaystyle \quad = y + a h f + b h \left[ f - h ( f _ { t } + f f _ { y } ) + \frac { h ^ { 2 } } { 2 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) \right] } } \\ { { \displaystyle \quad + c h \left[ f - 2 h ( f _ { t } + f f _ { y } ) + 2 h ^ { 2 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) \right] . } } \end{array}
$$

Thus

$$
a + b + c = 1 , \quad - b - 2 c = \frac { 1 } { 2 } , \quad \mathrm { a n d } \quad \frac { 1 } { 2 } b + 2 c = \frac { 1 } { 6 } .
$$

This system has the solution

$$
a = { \frac { 2 3 } { 1 2 } } , \quad b = - { \frac { 1 6 } { 1 2 } } , \quad { \mathrm { a n d } } \quad c = { \frac { 5 } { 1 2 } } .
$$

13. Newton’s divided-difference formula gives

$$
\begin{array} { l } { \displaystyle f ( t , y ( t ) ) = \frac { 1 } { 2 h ^ { 2 } } ( t - t _ { i } ) ( t - t _ { i + 1 } ) f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) \ - \frac { 1 } { h ^ { 2 } } ( t - t _ { i - 1 } ) ( t - t _ { i + 1 } ) f ( t _ { i } , y ( t _ { i } ) ) } \\ { \displaystyle \qquad + \frac { 1 } { 2 h ^ { 2 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) + \frac { 1 } { 6 } \frac { d ^ { 3 } } { d t ^ { 3 } } f ( \xi , y ( \xi ) ) ( t - t _ { i - 1 } ) ( t - t _ { i } ) ( t - t _ { i + 1 } ) } \end{array}
$$

so

$$
\int _ { t _ { i } } ^ { t _ { i + 1 } } y ^ { \prime } ( t ) d t = \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t
$$

and

$$
\begin{array} { l }  { + 1 ) - y ( t _ { i } ) = { \displaystyle \frac { f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } { 2 h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ( t - t _ { i + 1 } ) d t - { \displaystyle \frac { f ( t _ { i } , y ( t _ { i } ) ) } { h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } } } \\ { { \displaystyle ~ + ~ { \displaystyle \frac { f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) } { 2 h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } + { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } \frac { f ^ { \prime \prime \prime } ( \xi , y ( \xi ) ) } { 6 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } } \\ { { \displaystyle ~ = { \displaystyle \frac { - h } { 1 2 } } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + { \displaystyle \frac { 2 h } { 3 } } f ( t _ { i } , y ( t _ { i } ) ) + { \displaystyle \frac { 5 h } { 1 2 } } f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) } } \\ { { \displaystyle ~ + ~ { \displaystyle \frac { f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 6 } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) ( t - t _ { i + 1 } ) d t } . } } \end{array}
$$

The last part follows from Theorem 4.2. Further integration yields Formula (5.37) and the local truncation error.

$^ { * } 1 4$ . We have

$$
\begin{array} { l } { { \displaystyle y ( t _ { i + 1 } ) - y ( t _ { i - 1 } ) = \int _ { t _ { i - 1 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t } } \\ { { \displaystyle \qquad = \frac { h } { 3 } \left[ f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 4 f ( t _ { i } , y ( t _ { i } ) ) + f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) \right] - \frac { h ^ { 5 } } { 9 0 } f ^ { ( 4 ) } ( \xi , y ( \xi ) ) . } } \end{array}
$$

This leads to the difference equation

$$
w _ { i + 1 } = w _ { i - 1 } + \frac { h \left[ f ( t _ { i - 1 } , w _ { i - 1 } ) + 4 f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i + 1 } ) \right] } { 3 } ,
$$

with local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { - h ^ { 4 } y ^ { ( 5 ) } ( \xi ) } { 9 0 } .
$$

15. To derive Milne’s method, integrate $y ^ { \prime } ( t ) = f ( t , y ( t ) )$ on the interval $[ t _ { i - 3 } , t _ { i + 1 } ]$ to obtain

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \int _ { t _ { i - 3 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t .
$$

Using the open Newton-Cotes formula (4.31) on page 201, we have

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \frac { 4 h [ 2 f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 2 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) ] } { 3 } + \frac { 1 4 h ^ { 5 } f ^ { ( 4 ) } ( \xi , y ( \xi ) ) } { 4 5 } .
$$

The difference equation becomes

$$
w _ { i + 1 } = w _ { i - 3 } + \frac { h [ 8 f ( t _ { i } , w _ { i } ) - 4 f ( t _ { i - 1 } , w _ { i - 1 } ) + 8 f ( t _ { i - 2 } , w _ { i - 2 } ) ] } { 3 } ,
$$

with local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { 1 4 h ^ { 4 } y ^ { ( 5 ) } ( \xi ) } { 4 5 } .
$$

$^ { * } 1 6$ . The entries are generated by evaluating the following integrals:

$$
\begin{array} { l } { { k = 0 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } d s = 1 , } } \\ { { k = 1 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } - s d s = \displaystyle \frac { 1 } { 2 } , } } \\ { { k = 2 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } \frac { s \left( s + 1 \right) } { 2 } d s = \displaystyle \frac { 5 } { 1 2 } , } } \\ { { k = 3 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } \frac { - s \left( s + 1 \right) \left( s + 2 \right) } { 6 } d s = \displaystyle \frac { 3 } { 8 } , } } \\ { { k = 4 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } \frac { s \left( s + 1 \right) \left( s + 2 \right) \left( s + 3 \right) } { 2 4 } d s = \displaystyle \frac { 2 5 1 } { 7 2 0 } , \quad \mathrm { a n d } } } \\ { { k = 5 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } - s \left( s + 1 \right) \left( s + 2 \right) \left( s + 3 \right) \left( s + 4 \right) } d s = \displaystyle \frac { 9 5 } { 2 8 8 } . }  \end{array}
$$

# Exercise Set 5.7, page 320

1. The Adams Variable Step-Size Predictor-Corrector Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.04275596</td><td>0.00096891</td><td>0.04275596</td><td>0.00096887</td></tr><tr><td>5</td><td>0.22491460</td><td>0.03529441</td><td>0.05389076</td><td>0.03529359</td></tr><tr><td>12</td><td>0.60214994</td><td>0.50174348</td><td>0.05389076</td><td>0.50171761</td></tr><tr><td>17</td><td>0.81943926</td><td>1.45544317</td><td>0.04345786</td><td>1.45541453</td></tr><tr><td>22</td><td>0.99830392</td><td>3.19605697</td><td>0.03577293</td><td>3.19602842</td></tr><tr><td>26</td><td>1.00000000</td><td>3.21912776</td><td>0.00042395</td><td>3.21909932</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>2.06250000</td><td>1.12132350</td><td>0.06250000</td><td>1.12132353</td></tr><tr><td>5</td><td>2.31250000</td><td>1.55059834</td><td>0.06250000</td><td>1.55059524</td></tr><tr><td>9</td><td>2.62471924</td><td>2.00923157</td><td>0.09360962</td><td>2.00922829</td></tr><tr><td>13</td><td>2.99915773</td><td>2.49895243</td><td>0.09360962</td><td>2.49894707</td></tr><tr><td>17</td><td>3.00000000</td><td>2.50000535</td><td>0.00021057</td><td>2.50000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.06250000</td><td>2.18941363</td><td>0.06250000</td><td>2.18941366</td></tr><tr><td>4</td><td>1.25000000</td><td>2.77892931</td><td>0.06250000</td><td>2.77892944</td></tr><tr><td>8</td><td>1.85102559</td><td>4.84179835</td><td>0.15025640</td><td>4.84180141</td></tr><tr><td>12</td><td>2.00000000</td><td>5.38629105</td><td>0.03724360</td><td>5.38629436</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.06250000</td><td>1.06817960</td><td>0.06250000</td><td>1.06817960</td></tr><tr><td>5</td><td>0.31250000</td><td>1.42861668</td><td>0.06250000</td><td>1.42861361</td></tr><tr><td>10</td><td>0.62500000</td><td>1.90768386</td><td>0.06250000</td><td>1.90767015</td></tr><tr><td>13</td><td>0.81250000</td><td>2.08668486</td><td>0.06250000</td><td>2.08666541</td></tr><tr><td>16</td><td>1.00000000</td><td>2.11800208</td><td>0.06250000</td><td>2.11797955</td></tr></table>

\*(a)

2. The Adams Variable Step-Size Predictor-Corrector Algorithm gives the results in the following tables.   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.05000000</td><td>1.10385717</td><td>0.05000000</td><td>1.10385738</td></tr><tr><td>2</td><td>1.10000000</td><td>1.21588587</td><td>0.05000000</td><td>1.21588635</td></tr><tr><td>3</td><td>1.15000000</td><td>1.33683848</td><td>0.05000000</td><td>1.33683925</td></tr><tr><td>4</td><td>1.20000000</td><td>1.46756885</td><td>0.05000000</td><td>1.46756957</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.20000000</td><td>0.20120278</td><td>0.20000000</td><td>0.20120267</td></tr><tr><td>2</td><td>0.40000000</td><td>0.40861919</td><td>0.20000000</td><td>0.40861896</td></tr><tr><td>3</td><td>0.60000000</td><td>0.62585310</td><td>0.20000000</td><td>0.62585275</td></tr><tr><td>4</td><td>0.80000000</td><td>0.85397394</td><td>0.20000000</td><td>0.85396433</td></tr><tr><td>5</td><td>1.00000000</td><td>1.09183759</td><td>0.20000000</td><td>1.09181825</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>5</td><td>1.16289739</td><td>-1.75426113</td><td>0.03257948</td><td>-1.75426455</td></tr><tr><td>10</td><td>1.32579477</td><td>-1.60547206</td><td>0.03257948</td><td>-1.60547731</td></tr><tr><td>15</td><td>1.57235777</td><td>-1.46625721</td><td>0.04931260</td><td>-1.46626230</td></tr><tr><td>20</td><td>1.92943707</td><td>-1.34978308</td><td>0.07694168</td><td>-1.34978805</td></tr><tr><td>25</td><td>2.47170180</td><td>-1.25358275</td><td>0.11633076</td><td>-1.25358804</td></tr><tr><td>30</td><td>3.00000000</td><td>-1.19999513</td><td>0.10299186</td><td>-1.20000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.06250000</td><td>1.00583097</td><td>0.06250000</td><td>1.00583095</td></tr><tr><td>5</td><td>0.31250000</td><td>1.13099427</td><td>0.06250000</td><td>1.13098105</td></tr><tr><td>10</td><td>0.62500000</td><td>1.40361751</td><td>0.06250000</td><td>1.40360196</td></tr><tr><td>12</td><td>0.81250000</td><td>1.56515769</td><td>0.09375000</td><td>1.56514800</td></tr><tr><td>14</td><td>1.00000000</td><td>1.70186884</td><td>0.09375000</td><td>1.70187005</td></tr></table>

3. The following tables list representative results from the Adams Variable Step-Size Predictor-Corrector Algorithm.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.10431651</td><td>1.00463041</td><td>0.02086330</td><td>1.00463045</td></tr><tr><td>15</td><td>1.31294952</td><td>1.03196889</td><td>0.02086330</td><td>1.03196898</td></tr><tr><td>25</td><td>1.59408142</td><td>1.08714711</td><td>0.03122028</td><td>1.08714722</td></tr><tr><td>35</td><td>2.00846205</td><td>1.18327922</td><td>0.04824992</td><td>1.18327937</td></tr><tr><td>45</td><td>2.66272188</td><td>1.34525123</td><td>0.07278716</td><td>1.34525143</td></tr><tr><td>52</td><td>3.40193112</td><td>1.52940900</td><td>0.11107035</td><td>1.52940924</td></tr><tr><td>57</td><td>4.00000000</td><td>1.67623887</td><td>0.12174963</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.18519603</td><td>0.20333499</td><td>0.03703921</td><td>0.20333497</td></tr><tr><td>15</td><td>1.55558810</td><td>0.73586642</td><td>0.03703921</td><td>0.73586631</td></tr><tr><td>25</td><td>1.92598016</td><td>1.48072467</td><td>0.03703921</td><td>1.48072442</td></tr><tr><td>35</td><td>2.29637222</td><td>2.51764797</td><td>0.03703921</td><td>2.51764743</td></tr><tr><td>45</td><td>2.65452689</td><td>3.92602442</td><td>0.03092051</td><td>3.92602332</td></tr><tr><td>55</td><td>2.94341188</td><td>5.50206466</td><td>0.02584049</td><td>5.50206279</td></tr><tr><td>61</td><td>3.00000000</td><td>5.87410206</td><td>0.00122679</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.16854008</td><td>-1.83303780</td><td>0.03370802</td><td>-1.83303783</td></tr><tr><td>17</td><td>0.64833341</td><td>-1.42945306</td><td>0.05253230</td><td>-1.42945304</td></tr><tr><td>27</td><td>1.06742915</td><td>-1.21150951</td><td>0.04190957</td><td>-1.21150932</td></tr><tr><td>41</td><td>1.75380240</td><td>-1.05819340</td><td>0.06681937</td><td>-1.05819325</td></tr><tr><td>51</td><td>2.50124702</td><td>-1.01335240</td><td>0.07474446</td><td>-1.01335258</td></tr><tr><td>61</td><td>3.00000000</td><td>-1.00494507</td><td>0.01257155</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.28548652</td><td>0.32153668</td><td>0.05709730</td><td>0.32153674</td></tr><tr><td>15</td><td>0.85645955</td><td>0.24281066</td><td>0.05709730</td><td>0.24281095</td></tr><tr><td>20</td><td>1.35101725</td><td>0.15096743</td><td>0.09891154</td><td>0.15096772</td></tr><tr><td>25</td><td>1.66282314</td><td>0.09815109</td><td>0.06236118</td><td>0.09815137</td></tr><tr><td>29</td><td>1.91226786</td><td>0.06418555</td><td>0.06236118</td><td>0.06418579</td></tr><tr><td>33</td><td>2.00000000</td><td>0.05434530</td><td>0.02193303</td><td>0.05434551</td></tr></table>

\*4. Change the following steps:

STEP 1 Set up an algorithm, denoted $R K 5$ , for the Runge Kutta Method of Order 5. STEP 3 Call $R K 5 ( h , w _ { 0 } , t _ { 0 } , w _ { 1 } , t _ { 1 } , w _ { 2 } , t _ { 2 } , w _ { 3 } , t _ { 3 } , w _ { 4 } , t _ { 4 } )$ :

$$
\begin{array} { r l } { \mathrm { S e t } } & { N F L A G = 1 ; } \\ & { i = 5 ; } \\ & { t = t _ { 4 } + h . } \end{array}
$$

STEP 5 Set

$$
\begin{array} { r l } & { W P = w _ { i - 1 } + \frac { h } { 7 2 0 } \bigg [ 1 9 0 1 f ( t _ { i - 1 } , w _ { i - 1 } ) - 2 7 7 4 f ( t _ { i - 2 } , w _ { i - 2 } ) } \\ & { \qquad + 2 6 1 6 f ( t _ { i - 3 } , w _ { i - 3 } ) - 1 2 7 4 f ( t _ { i - 4 } , w _ { i - 4 } ) + 2 5 1 f ( t _ { i - 5 } , w _ { i - 5 } ) \bigg ] ; } \\ & { W C = w _ { i - 1 } + \frac { h } { 7 2 0 } \bigg [ 2 5 1 f ( t , W P ) + 6 4 6 f ( t _ { i - 1 } , w _ { i - 1 } ) - 2 6 4 f ( t _ { i - 2 } , w _ { i - 2 } ) } \\ & { \qquad + 1 0 6 f ( t _ { i - 3 } , w _ { i - 3 } ) - 1 9 f ( t _ { i - 4 } , w _ { i - 4 } ) \bigg ] ; } \\ & { \sigma = 2 7 | W C - W P | / ( 5 0 2 ) h . } \end{array}
$$

$\begin{array} { l } { S T E P ~ \delta } \\ { S T E P ~ \mathit { 1 2 } } \\ { S T E P ~ \mathit { 1 5 } } \\ { S T E P ~ \mathit { 1 6 } } \end{array}$ If $N F L A G = 1$ then for $j = i - 4 , i - 3 , i - 2 , i - 1 , i$ Set $q = ( 0 . 5 T O L / \sigma ) ^ { \frac { 1 } { 5 } }$ If $t _ { i - 1 } + 5 h > b$ , then set $h = ( b - t _ { i - 1 } ) / 5$ Call $R K 5 ( h , w _ { i - 1 } , t _ { i - 1 } , w _ { i } , t _ { i } , w _ { i + 1 } , t _ { i + 1 } , w _ { i + 2 } , t _ { i + 2 } , w _ { i + 3 } , t _ { i + 3 } ) ;$

Set $N F L A G = 1$ ; $i = i + 4$ . STEP 17 Set $q = ( 0 . 5 T O L / \sigma ) ^ { \frac { 1 } { 5 } }$ .

STEP 19 else

The following are the results obtained by applying the new algorithm to the problems in Exercise 3.

\*(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.17529879</td><td>1.01186066</td><td>0.03505976</td><td>1.01186063</td></tr><tr><td>15</td><td>1.56737794</td><td>1.08139480</td><td>0.05580055</td><td>1.08139470</td></tr><tr><td>25</td><td>2.25808774</td><td>1.24445586</td><td>0.08897663</td><td>1.24445574</td></tr><tr><td>35</td><td>3.51328927</td><td>1.55692781</td><td>0.14118166</td><td>1.55692763</td></tr><tr><td>40</td><td>4.00000000</td><td>1.67623932</td><td>0.09734215</td><td>1.67623914</td></tr><tr><td>5</td><td>1.33993400</td><td>0.40368020</td><td>0.06798680</td><td>0.40368021</td></tr><tr><td>15</td><td>2.13987639</td><td>2.03689764</td><td>0.07343117</td><td>2.03689764</td></tr><tr><td>25</td><td>2.78633514</td><td>4.58497685</td><td>0.05029339</td><td>4.58497677</td></tr><tr><td>30</td><td>2.99000695</td><td>5.80662141</td><td>0.00249826</td><td>5.80662127</td></tr><tr><td>34</td><td>3.00000000</td><td>5.87410012</td><td>0.00249826</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.32371968</td><td>-1.68713369</td><td>0.06474394</td><td>-1.68713361</td></tr><tr><td>15</td><td>0.98679855</td><td>-1.24400623</td><td>0.08248419</td><td>-1.24400610</td></tr><tr><td>20</td><td>1.39921950</td><td>-1.11481699</td><td>0.08248419</td><td>-1.11481718</td></tr><tr><td>25</td><td>1.81164045</td><td>-1.05200140</td><td>0.08248419</td><td>-1.05200171</td></tr><tr><td>29</td><td>2.23962447</td><td>-1.02242929</td><td>0.13150782</td><td>-1.02242946</td></tr><tr><td>33</td><td>2.76565574</td><td>-1.00789049</td><td>0.13150782</td><td>-1.00789033</td></tr><tr><td>39</td><td>3.00000000</td><td>-1.00494544</td><td>0.02056729</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.49509708</td><td>0.29938376</td><td>0.09901942</td><td>0.29938377</td></tr><tr><td>15</td><td>1.27560008</td><td>0.16486635</td><td>0.03572768</td><td>0.16486623</td></tr><tr><td>20</td><td>1.65480865</td><td>0.09938119</td><td>0.10258441</td><td>0.09938111</td></tr><tr><td>25</td><td>1.94399098</td><td>0.06049879</td><td>0.02800451</td><td>0.06049858</td></tr><tr><td>27</td><td>2.00000000</td><td>0.05434569</td><td>0.02800451</td><td>0.05434551</td></tr></table>

5. The current after 2 seconds is approximately $i ( 2 ) = 8 . 6 9 3$ amperes.

# Exercise Set 5.8, page 327

1. The Extrapolation Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.25</td><td>0.04543132</td><td>0.25</td><td>3</td><td>0.04543123</td></tr><tr><td>2</td><td>0.50</td><td>0.28361684</td><td>0.25</td><td>3</td><td>0.28361652</td></tr><tr><td>3</td><td>0.75</td><td>1.05257634</td><td>0.25</td><td>4</td><td>1.05257615</td></tr><tr><td>4</td><td>1.00</td><td>3.21909944</td><td>0.25</td><td>4</td><td>3.21909932</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>2.25</td><td>1.44999987</td><td>0.25</td><td>3</td><td>1.45000000</td></tr><tr><td>2</td><td>2.50</td><td>1.83333321</td><td>0.25</td><td>3</td><td>1.83333333</td></tr><tr><td>3</td><td>2.75</td><td>2.17857133</td><td>0.25</td><td>3</td><td>2.17857143</td></tr><tr><td>4</td><td>3.00</td><td>2.49999993</td><td>0.25</td><td>3</td><td>2.50000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.25</td><td>2.77892942</td><td>0.25</td><td>3</td><td>2.77892944</td></tr><tr><td>2</td><td>1.50</td><td>3.60819763</td><td>0.25</td><td>3</td><td>3.60819766</td></tr><tr><td>3</td><td>1.75</td><td>4.47932759</td><td>0.25</td><td>3</td><td>4.47932763</td></tr><tr><td>4</td><td>2.00</td><td>5.38629431</td><td>0.25</td><td>3</td><td>5.38629436</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>1.32914981</td><td>0.25</td><td>3</td><td>1.32914981</td></tr><tr><td>2</td><td>0.50</td><td>1.73048976</td><td>0.25</td><td>3</td><td>1.73048976</td></tr><tr><td>3</td><td>0.75</td><td>2.04147203</td><td>0.25</td><td>3</td><td>2.04147203</td></tr><tr><td>4</td><td>1.00</td><td>2.11797954</td><td>0.25</td><td>3</td><td>2.11797955</td></tr></table>

2. The Extrapolation Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.05</td><td>1.10385729</td><td>0.05</td><td>2</td><td>1.10385738</td></tr><tr><td>2</td><td>1.10</td><td>1.21588614</td><td>0.05</td><td>2</td><td>1.21588635</td></tr><tr><td>3</td><td>1.15</td><td>1.33683891</td><td>0.05</td><td>2</td><td>1.33683925</td></tr><tr><td>4</td><td>1.20</td><td>1.46756907</td><td>0.05</td><td>2</td><td>1.46756957</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>0.25228680</td><td>0.25</td><td>3</td><td>0.25228680</td></tr><tr><td>2</td><td>0.50</td><td>0.51588678</td><td>0.25</td><td>3</td><td>0.51588678</td></tr><tr><td>3</td><td>0.75</td><td>0.79594460</td><td>0.25</td><td>2</td><td>0.79594458</td></tr><tr><td>4</td><td>1.00</td><td>1.09181828</td><td>0.25</td><td>3</td><td>1.09181825</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.50</td><td>-1.50000055</td><td>0.50</td><td>5</td><td>-1.50000000</td></tr><tr><td>2</td><td>2.00</td><td>-1.33333435</td><td>0.50</td><td>3</td><td>-1.33333333</td></tr><tr><td>3</td><td>2.50</td><td>-1.25000074</td><td>0.50</td><td>3</td><td>-1.25000000</td></tr><tr><td>4</td><td>3.00</td><td>-1.20000090</td><td>0.50</td><td>2</td><td>-1.20000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>1.08708817</td><td>0.25</td><td>3</td><td>1.08708823</td></tr><tr><td>2</td><td>0.50</td><td>1.28980537</td><td>0.25</td><td>3</td><td>1.28980528</td></tr><tr><td>3</td><td>0.75</td><td>1.51349008</td><td>0.25</td><td>3</td><td>1.51348985</td></tr><tr><td>4</td><td>1.00</td><td>1.70187009</td><td>0.25</td><td>3</td><td>1.70187005</td></tr></table>

3. The Extrapolation Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.50</td><td>1.06726237</td><td>0.50</td><td>4</td><td>1.06726235</td></tr><tr><td>2</td><td>2.00</td><td>1.18123223</td><td>0.50</td><td>3</td><td>1.18123222</td></tr><tr><td>3</td><td>2.50</td><td>1.30460372</td><td>0.50</td><td>3</td><td>1.30460371</td></tr><tr><td>4</td><td>3.00</td><td>1.42951608</td><td>0.50</td><td>3</td><td>1.42951607</td></tr><tr><td>5</td><td>3.50</td><td>1.55364771</td><td>0.50</td><td>3</td><td>1.55364770</td></tr><tr><td>6</td><td>4.00</td><td>1.67623915</td><td>0.50</td><td>3</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.50</td><td>0.64387537</td><td>0.50</td><td>4</td><td>0.64387533</td></tr><tr><td>2</td><td>2.00</td><td>1.66128182</td><td>0.50</td><td>5</td><td>1.66128176</td></tr><tr><td>3</td><td>2.50</td><td>3.25801550</td><td>0.50</td><td>5</td><td>3.25801536</td></tr><tr><td>4</td><td>3.00</td><td>5.87410027</td><td>0.50</td><td>5</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.50</td><td>-1.53788284</td><td>0.50</td><td>4</td><td>-1.53788284</td></tr><tr><td>2</td><td>1.00</td><td>-1.23840584</td><td>0.50</td><td>5</td><td>-1.23840584</td></tr><tr><td>3</td><td>1.50</td><td>-1.09485175</td><td>0.50</td><td>5</td><td>-1.09485175</td></tr><tr><td>4</td><td>2.00</td><td>-1.03597242</td><td>0.50</td><td>5</td><td>-1.03597242</td></tr><tr><td>5</td><td>2.50</td><td>-1.01338570</td><td>0.50</td><td>5</td><td>-1.01338570</td></tr><tr><td>6</td><td>3.00</td><td>-1.00494526</td><td>0.50</td><td>4</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.50</td><td>0.29875177</td><td>0.50</td><td>4</td><td>0.29875178</td></tr><tr><td>2</td><td>1.00</td><td>0.21662642</td><td>0.50</td><td>4</td><td>0.21662642</td></tr><tr><td>3</td><td>1.50</td><td>0.12458565</td><td>0.50</td><td>4</td><td>0.12458565</td></tr><tr><td>4</td><td>2.00</td><td>0.05434552</td><td>0.50</td><td>4</td><td>0.05434551</td></tr></table>

\*4. The population after five years is $y ( 5 ) \approx 5 6 , 7 5 1$ .

# Exercise Set 5.9, page 337

1. The Runge-Kutta for Systems Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.200</td><td>2.12036583</td><td>2.12500839</td><td>1.50699185</td><td>1.51158743</td></tr><tr><td>0.400</td><td>4.44122776</td><td>4.46511961</td><td>3.24224021</td><td>3.26598528</td></tr><tr><td>0.600</td><td>9.73913329</td><td>9.83235869</td><td>8.16341700</td><td>8.25629549</td></tr><tr><td>0.800</td><td>22.67655977</td><td>23.00263945</td><td>21.34352778</td><td>21.66887674</td></tr><tr><td>1.000</td><td>55.66118088</td><td>56.73748265</td><td>56.03050296</td><td>57.10536209</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td></tr><tr><td>0.500</td><td>0.95671390</td><td>0.95672798</td><td>-1.08381950</td><td>-1.08383310</td></tr><tr><td>1.000</td><td>1.30654440</td><td>1.30655930</td><td>-0.83295364</td><td>-0.83296776</td></tr><tr><td>1.500</td><td>1.34416716</td><td>1.34418117</td><td>-0.56980329</td><td>-0.56981634</td></tr><tr><td>2.000</td><td>1.14332436</td><td>1.14333672</td><td>-0.36936318</td><td>-0.36937457</td></tr></table>

(c)

<table><tr><td>ti</td><td>W1i</td><td>Uli</td><td>W2i</td><td>u2i</td><td>W3i</td><td>U3i</td></tr><tr><td>0.5</td><td>0.70787076</td><td>0.70828683</td><td>-1.24988663</td><td>-1.25056425</td><td>0.39884862</td><td>0.39815702</td></tr><tr><td>1.0</td><td>-0.33691753</td><td>-0.33650854</td><td>-3.01764179</td><td>-3.01945051</td><td>-0.29932294</td><td>-0.30116868</td></tr><tr><td>1.5</td><td>-2.41332734</td><td>-2.41345688</td><td>-5.40523279</td><td>-5.40844686</td><td>-0.92346873</td><td>-0.92675778</td></tr><tr><td>2.0</td><td>-5.89479008</td><td>-5.89590551</td><td>-8.70970537</td><td>-8.71450036</td><td>-1.32051165</td><td>-1.32544426</td></tr></table>

(d)

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.2</td><td>1.38165297</td><td>1.38165325</td><td>1.00800000</td><td>1.00800000</td><td>-0.61833075</td><td>-0.61833075</td></tr><tr><td>0.5</td><td>1.90753116</td><td>1.90753184</td><td>1.12500000</td><td>1.12500000</td><td>-0.09090565</td><td>-0.09090566</td></tr><tr><td>0.7</td><td>2.25503524</td><td>2.25503620</td><td>1.34300000</td><td>1.34000000</td><td>0.26343971</td><td>0.26343970</td></tr><tr><td>1.0</td><td>2.83211921</td><td>2.83212056</td><td>2.00000000</td><td>2.00000000</td><td>0.88212058</td><td>0.88212056</td></tr></table>

(a)

2. The Runge-Kutta for Systems Algorithm gives the results in the following tables.   

<table><tr><td>t</td><td>W1</td><td>W2</td><td>U1</td><td>u2</td></tr><tr><td>0.2</td><td>-0.80590898</td><td>0.28590898</td><td>-0.8059123490</td><td>0.2859123490</td></tr><tr><td>0.4</td><td>-0.65276041</td><td>0.77276041</td><td>-0.652770464</td><td>0.772770464</td></tr><tr><td>0.6</td><td>-0.60003597</td><td>1.52003597</td><td>-0.600058462</td><td>1.520058462</td></tr><tr><td>0.8</td><td>-0.73647147</td><td>2.61647147</td><td>-0.736516212</td><td>2.616516212</td></tr><tr><td>1.0</td><td>-1.19444462</td><td>4.19444462</td><td>-1.194528050</td><td>4.194528050</td></tr></table>

(b)

<table><tr><td>t</td><td>W1</td><td>W2</td><td>u1</td><td>U2</td></tr><tr><td>0.2</td><td>-3.62420001</td><td>5.28560000</td><td>-3.624208274</td><td>5.285611032</td></tr><tr><td>0.6</td><td>-5.10631940</td><td>6.48842582</td><td>-5.106356400</td><td>6.488475200</td></tr><tr><td>1.0</td><td>-7.15475346</td><td>8.87300454</td><td>-7.154845484</td><td>8.87312731</td></tr><tr><td>1.4</td><td>-10.20540766</td><td>13.02054346</td><td>-10.20559990</td><td>13.02079987</td></tr><tr><td>1.8</td><td>-14.90857362</td><td>19.79809804</td><td>-14.90894239</td><td>19.79858986</td></tr></table>

(c)

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>U1</td><td>u2</td><td>u3</td></tr><tr><td>0.2</td><td>2.82820001</td><td>-1.36717100</td><td>1.29430535</td><td>2.828199216</td><td>-1.367172763</td><td>1.294303950</td></tr><tr><td>0.4</td><td>2.34715282</td><td>-1.70213314</td><td>1.35096843</td><td>2.347150799</td><td>-1.702138886</td><td>1.350962985</td></tr><tr><td>0.6</td><td>1.61165492</td><td>-2.06862759</td><td>1.12031748</td><td>1.611651361</td><td>-2.068641364</td><td>1.120303523</td></tr><tr><td>0.8</td><td>0.68019035</td><td>-2.55506790</td><td>0.53282506</td><td>0.680185091</td><td>-2.555096786</td><td>0.532795132</td></tr><tr><td>1.0</td><td>-0.38623048</td><td>-3.28594071</td><td>-0.51207026</td><td>-0.386237443</td><td>-3.285996825</td><td>-0.512128574</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>u1</td><td>u2</td><td>U3</td></tr><tr><td>0.2</td><td>5.85399925</td><td>-6.58493690</td><td>-5.51120222</td><td>6.655197738</td><td>-6.582587709</td><td>-5.507713390</td></tr><tr><td>0.6</td><td>13.58890681</td><td>-2.95418927</td><td>-4.51808620</td><td>14.00287757</td><td>-2.921029767</td><td>-4.45343131</td></tr><tr><td>1.0</td><td>41.49825592</td><td>13.88034475</td><td>26.10907731</td><td>41.57707969</td><td>14.18586490</td><td>26.71881714</td></tr><tr><td>1.4</td><td>134.58778600</td><td>135.26098840</td><td>267.46411360</td><td>134.5550923</td><td>137.5527145</td><td>272.0466805</td></tr><tr><td>1.8</td><td>443.12659480</td><td>882.03172470</td><td>1760.52619100</td><td>443.8948036</td><td>897.3731894</td><td>1791.208540</td></tr></table>

3. The Runge-Kutta for Systems Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>ti</td><td>W1i</td><td>Yi</td></tr><tr><td>0.200</td><td>0.00015352</td><td>0.00015350</td></tr><tr><td>0.500</td><td>0.00742968</td><td>0.00743027</td></tr><tr><td>0.700</td><td>0.03299617</td><td>0.03299805</td></tr><tr><td>1.000</td><td>0.17132224</td><td>0.17132880</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>Yi</td></tr><tr><td>1.200</td><td>0.96152437</td><td>0.96152583</td></tr><tr><td>1.500</td><td>0.77796897</td><td>0.77797237</td></tr><tr><td>1.700</td><td>0.59373369</td><td>0.59373830</td></tr><tr><td>2.000</td><td>0.27258237</td><td>0.27258872</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>yi</td></tr><tr><td>1.000</td><td>3.73162695</td><td>3.73170445</td></tr><tr><td>2.000</td><td>11.31424573</td><td>11.31452924</td></tr><tr><td>3.000</td><td>34.04395688</td><td>34.04517155</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>W2i</td></tr><tr><td>1.200</td><td>0.27273759</td><td>0.27273791</td></tr><tr><td>1.500</td><td>1.08849079</td><td>1.08849259</td></tr><tr><td>1.700</td><td>2.04353207</td><td>2.04353642</td></tr><tr><td>2.000</td><td>4.36156675</td><td>4.36157780</td></tr></table>

(a)

4. The Runge-Kutta for Systems Algorithm gives the results in the following tables.   

<table><tr><td>t</td><td>W1</td><td>W2</td><td>y(t)</td></tr><tr><td>0.2</td><td>2.58096738</td><td>3.92714601</td><td>2.580977391</td></tr><tr><td>0.4</td><td>3.62954528</td><td>6.73995658</td><td>3.629577204</td></tr><tr><td>0.6</td><td>5.36685193</td><td>10.90938990</td><td>5.366926682</td></tr><tr><td>0.8</td><td>8.12969935</td><td>17.13695552</td><td>8.129852884</td></tr><tr><td>1.0</td><td>12.42741665</td><td>26.46948024</td><td>12.42770981</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>y(t)</td></tr><tr><td>1.2</td><td>4.77485600</td><td>4.64248546</td><td>4.774444444</td></tr><tr><td>1.6</td><td>7.11125088</td><td>6.91189139</td><td>7.110625000</td></tr><tr><td>2.0</td><td>10.25079116</td><td>8.75041113</td><td>10.25000000</td></tr><tr><td>2.4</td><td>14.09462248</td><td>10.45592060</td><td>14.09361111</td></tr><tr><td>2.8</td><td>18.60884185</td><td>12.10964620</td><td>18.60755102</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>y(t)</td></tr><tr><td>0.2</td><td>2.98086667</td><td>0.82393333</td><td>9.46726667</td><td>2.980875497</td></tr><tr><td>0.6</td><td>4.16962578</td><td>5.48759308</td><td>15.03205266</td><td>4.170122771</td></tr><tr><td>1.0</td><td>7.89009498</td><td>14.13487020</td><td>30.45672422</td><td>7.892270823</td></tr><tr><td>1.4</td><td>16.74506147</td><td>32.50687231</td><td>66.24043865</td><td>16.75205379</td></tr><tr><td>1.8</td><td>36.77072349</td><td>72.93612397</td><td>146.58698330</td><td>36.79085705</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>y(t)</td></tr><tr><td>1.2</td><td>3.73466631</td><td>9.41446279</td><td>8.04259896</td><td>3.734666667</td></tr><tr><td>1.4</td><td>5.78971770</td><td>11.19022983</td><td>9.67114868</td><td>5.789714286</td></tr><tr><td>1.6</td><td>8.23100886</td><td>13.27065559</td><td>11.11173381</td><td>8.231000000</td></tr><tr><td>1.8</td><td>11.11645980</td><td>15.62867678</td><td>12.45708169</td><td>11.11644444</td></tr><tr><td>2.0</td><td>14.50002275</td><td>18.25003892</td><td>13.75001862</td><td>14.50000000</td></tr></table>

$^ { * } 5$ . To approximate the solution of the $m$ th–order system of first–order initial–value problems

$$
u _ { j } ^ { \prime } = f _ { j } ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) , j = 1 , 2 , \ldots , m , \mathrm { f o r } a \leq t \leq b , u _ { j } ( a ) = \alpha _ { j } , j = 1 , 2 , \ldots , m ,
$$

at $( n + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ;

INPUT endpoints $a , b$ ; number of equations $m$ ; integer $N$ ; initial conditions $\alpha _ { 1 } , \ldots , \alpha _ { m }$ .   
OUTPUT approximations $w _ { i , j }$ to $u _ { j } ( t _ { i } )$ . STEP 1 Set $h = ( b - a ) / N$ ;   
STEP 2 For $j = 1 , 2 , \dots , m$ set $w _ { 0 , j } = \alpha _ { j }$ .   
STEP 3 OUTPUT $( t _ { 0 } , w _ { 0 , 1 } , w _ { 0 , 2 } , \ldots , w _ { 0 , m } )$ .

$S T E P 4$ For $i = { 1 , 2 , 3 }$ do Steps 5–11.

$$
\begin{array} { r l } & { k _ { 1 , j } = h f _ { j } ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } ) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 2 , j } = h f _ { j } \left( t _ { i - 1 } + \frac { h } { 2 } , w _ { i - 1 , 1 } + \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { i - 1 , 2 } + \frac { 1 } { 2 } k _ { 1 , 2 } , \ldots , w _ { i - 1 , m } + \frac { 1 } { 2 } k _ { 1 , m } \right) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 3 , j } = h f _ { j } \left( t _ { i - 1 } + \frac { 1 } { 2 } , w _ { i - 1 , 1 } + \frac { 1 } { 2 } k _ { 2 , 1 } , w _ { i - 1 , 2 } + \frac { 1 } { 2 } k _ { 2 , 2 } , \ldots , w _ { i - 1 , m } + \frac { 1 } { 2 } k _ { 2 , m } \right) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 4 , j } = h f _ { j } ( t _ { i - 1 } + h , w _ { i - 1 , 1 } + k _ { 3 , 1 } , w _ { i - 1 , 2 } + k _ { 3 , 2 } , \ldots , w _ { i - 1 , m } + k _ { 3 , m } ) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { w _ { i , j } = w _ { i - 1 , j } + ( k _ { 1 , j } + 2 k _ { 2 , j } + 2 k _ { 3 , j } + k _ { 4 , j } ) / 6 . } \\ & { \mathrm { ~ S e t ~ } t _ { i } = { } _ { i } + h . } \end{array}
$$

STEP 12 For $i = 4 , \ldots , N$ do Steps 13–16. STEP 13 Set $t _ { i } = a + i h$ . STEP 14 For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { l } { w _ { i , j } ^ { ( 0 ) } = w _ { i - 1 , j } + h \bigg [ 5 5 f _ { j } \big ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } \big ) - 5 9 f _ { j } \big ( t _ { i - 2 } , w _ { i - 2 , 1 } , \ldots , w _ { i - 2 , m } \big ) } \\ { \qquad + 3 7 f _ { j } \big ( t _ { i - 3 } , w _ { i - 3 , 1 } , \ldots , w _ { i - 3 , m } \big ) - 9 f _ { j } \big ( t _ { i - 4 } , w _ { i - 4 , 1 } , \ldots , w _ { i - 4 , m } \big ) \bigg ] \bigg / 2 4 . } \end{array}
$$

STEP 15 For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { r } { w _ { i , j } = w _ { i - 1 , j } + h \bigg [ 9 f _ { j } \left( t _ { i } , w _ { i , 1 } ^ { ( 0 ) } , \ldots , w _ { i , m } ^ { ( 0 ) } \right) + 1 9 f _ { j } ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } ) } \\ { - \left. 5 f _ { j } ( t _ { i - 2 } , w _ { i - 2 , 1 } , \ldots , w _ { i - 2 , m } ) + f _ { j } ( t _ { i - 3 } , w _ { i - 3 , 1 } , \ldots , w _ { i - 3 , m } ) \right] \bigg / 2 4 . } \end{array}
$$

STEP 17 STOP

6. The Adams Fourth-Order Predictor-Corrector method for systems applied to the problems in Exercise 2 gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td></tr><tr><td>0.2</td><td>-0.80590898</td><td>-0.80591235</td><td>0.28590898</td><td>0.28591235</td></tr><tr><td>0.4</td><td>-0.65276394</td><td>-0.65277046</td><td>0.77276394</td><td>0.77277046</td></tr><tr><td>0.6</td><td>-0.60005208</td><td>-0.60005846</td><td>1.52005208</td><td>1.52005846</td></tr><tr><td>0.8</td><td>-0.73651161</td><td>-0.73651621</td><td>2.61651161</td><td>2.61651621</td></tr><tr><td>1.0</td><td>-1.19452854</td><td>-1.19452805</td><td>4.19452854</td><td>4.19452805</td></tr></table>

(b)

<table><tr><td>ti</td><td>W1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td></tr><tr><td>0.2</td><td>-3.62420001</td><td>-3.62420827</td><td>5.28560000</td><td>5.28561103</td></tr><tr><td>0.8</td><td>-5.10631940</td><td>-5.10635640</td><td>6.48842583</td><td>6.48847520</td></tr><tr><td>1.0</td><td>-7.15480610</td><td>-7.15484549</td><td>8.87307476</td><td>8.87312731</td></tr><tr><td>1.4</td><td>-10.20556525</td><td>-10.20559990</td><td>13.02075362</td><td>13.02079987</td></tr><tr><td>1.8</td><td>-14.90892678</td><td>-14.90894239</td><td>19.79856900</td><td>19.79858986</td></tr></table>

(c)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td><td>w3(ti)</td><td>u3(ti)</td></tr><tr><td>0.2</td><td>2.82820001</td><td>2.82819922</td><td>-1.36717100</td><td>-1.36717276</td><td>1.29430535</td><td>1.29430395</td></tr><tr><td>0.4</td><td>2.34715270</td><td>2.34715080</td><td>-1.70213589</td><td>-1.70213889</td><td>1.35096690</td><td>1.35096298</td></tr><tr><td>0.6</td><td>1.61165288</td><td>1.61165136</td><td>-2.06863957</td><td>-2.06864136</td><td>1.12030805</td><td>1.12030352</td></tr><tr><td>0.8</td><td>0.68018456</td><td>0.68018509</td><td>-2.55509734</td><td>-2.55509679</td><td>0.53279799</td><td>0.53279513</td></tr><tr><td>1.0</td><td>-0.38624142</td><td>-0.38623744</td><td>-3.28600244</td><td>-3.28599682</td><td>-0.51213132</td><td>-0.51212857</td></tr></table>

(d)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>W2(ti)</td><td>u2(ti)</td><td>W3(ti)</td><td>u3(ti)</td></tr><tr><td>0.2</td><td>5.85399925</td><td>6.65519774</td><td>-6.58493690</td><td>-6.58258771</td><td>-5.51120222</td><td>-5.50771339</td></tr><tr><td>0.8</td><td>13.58890681</td><td>14.00287756</td><td>-2.95418927</td><td>-2.92102977</td><td>-4.51808620</td><td>-4.45343131</td></tr><tr><td>1.0</td><td>41.45180376</td><td>41.57707970</td><td>13.61528979</td><td>14.18586491</td><td>25.57139128</td><td>26.71881709</td></tr><tr><td>1.4</td><td>134.28466702</td><td>134.55509227</td><td>132.41529876</td><td>137.55271457</td><td>261.76615143</td><td>272.04668062</td></tr><tr><td>1.8</td><td>441.61837376</td><td>443.89480356</td><td>860.12763808</td><td>897.37318983</td><td>1716.71350110</td><td>1791.20854020</td></tr></table>

7. The Adams Fourth-Order Predictor-Corrector method for systems applied to the problems in Exercise 1 gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.200</td><td>2.12036583</td><td>2.12500839</td><td>1.50699185</td><td>1.51158743</td></tr><tr><td>0.400</td><td>4.44122776</td><td>4.46511961</td><td>3.24224021</td><td>3.26598528</td></tr><tr><td>0.600</td><td>9.73913329</td><td>9.83235869</td><td>8.16341700</td><td>8.25629549</td></tr><tr><td>0.800</td><td>22.52673210</td><td>23.00263945</td><td>21.20273983</td><td>21.66887674</td></tr><tr><td>1.000</td><td>54.81242211</td><td>56.73748265</td><td>55.20490157</td><td>57.10536209</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.500</td><td>0.95675505</td><td>0.95672798</td><td>-1.08385916</td><td>-1.08383310</td></tr><tr><td>1.000</td><td>1.30659995</td><td>1.30655930</td><td>-0.83300571</td><td>-0.83296776</td></tr><tr><td>1.500</td><td>1.34420613</td><td>1.34418117</td><td>-0.56983853</td><td>-0.56981634</td></tr><tr><td>2.000</td><td>1.14334795</td><td>1.14333672</td><td>-0.36938396</td><td>-0.36937457</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>uli</td><td>W2i</td><td>u2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.5</td><td>0.70787076</td><td>0.70828683</td><td>-1.24988663</td><td>-1.25056425</td><td>0.39884862</td><td>0.39815702</td></tr><tr><td>1.0</td><td>-0.33691753</td><td>-0.33650854</td><td>-3.01764179</td><td>-3.01945051</td><td>-0.29932294</td><td>-0.30116868</td></tr><tr><td>1.5</td><td>-2.41332734</td><td>-2.41345688</td><td>-5.40523279</td><td>-5.40844686</td><td>-0.92346873</td><td>-0.92675778</td></tr><tr><td>2.0</td><td>-5.88968402</td><td>-5.89590551</td><td>-8.72213325</td><td>-8.71450036</td><td>-1.32972524</td><td>-1.32544426</td></tr></table>

(d)

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.2</td><td>1.38165297</td><td>1.38165325</td><td>1.00800000</td><td>1.00800000</td><td>-0.61833075</td><td>-0.61833075</td></tr><tr><td>0.5</td><td>1.90752882</td><td>1.90753184</td><td>1.12500000</td><td>1.12500000</td><td>-0.09090527</td><td>-0.09090566</td></tr><tr><td>0.7</td><td>2.25503040</td><td>2.25503620</td><td>1.34300000</td><td>1.34300000</td><td>0.26344040</td><td>0.26343970</td></tr><tr><td>1.0</td><td>2.83211032</td><td>2.83212056</td><td>2.00000000</td><td>2.00000000</td><td>0.88212163</td><td>0.88212056</td></tr></table>

8. The approximations for the swinging pendulum problems are given in the tables:

<table><tr><td colspan="2">(a)</td></tr><tr><td colspan="2"></td></tr><tr><td>ti</td><td>0</td></tr><tr><td colspan="2">1.0 -0.365903 2.0 -0.0150563</td></tr></table>

<table><tr><td rowspan="3">(b)</td><td></td></tr><tr><td></td></tr><tr><td>ti 0</td></tr><tr><td>1.0</td><td>-0.338253</td></tr><tr><td>2.0</td><td>-0.0862680</td></tr></table>

9. The predicted number of prey, $x _ { 1 i }$ , and predators, $x _ { 2 i }$ , are given in the following table.

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>X1i</td><td>X2i</td></tr><tr><td>10</td><td>1.0</td><td>4393</td><td>1512</td></tr><tr><td>20</td><td>2.0</td><td>288</td><td>3175</td></tr><tr><td>30</td><td>3.0</td><td>32</td><td>2042</td></tr><tr><td>40</td><td>4.0</td><td>25</td><td>1258</td></tr></table>

10. The predicted number of prey, $x _ { 1 i }$ , and predators, $x _ { 2 i }$ , are given in the following table.

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>W1i</td><td>W2i</td></tr><tr><td>6</td><td>1.2</td><td>2211</td><td>11469</td></tr><tr><td>12</td><td>2.4</td><td>175</td><td>17492</td></tr><tr><td>18</td><td>3.6</td><td>2</td><td>19704</td></tr></table>

A stable solution is $x _ { 1 } = 8 0 0 0$ and $x _ { 2 } = 4 0 0 0$ .

# Exercise Set 5.10, page 347

1. Let $L$ be the Lipschitz constant for $\phi$ . Then

$$
u _ { i + 1 } - v _ { i + 1 } = u _ { i } - v _ { i } + h [ \phi ( t _ { i } , u _ { i } , h ) - \phi ( t _ { i } , v _ { i } , h ) ] _ { \mathrm { t } }
$$

so

$$
\begin{array} { r } { \left| u _ { i + 1 } - v _ { i + 1 } \right| \leq ( 1 + h L ) | u _ { i } - v _ { i } | \leq ( 1 + h L ) ^ { i + 1 } | u _ { 0 } - v _ { 0 } | . } \end{array}
$$

2. $^ { * } ( \mathrm { a } )$ For the Adams-Bashforth Method,

F $^ { \ast } ( t _ { i } , h , w _ { i + 1 } , w _ { i } , w _ { i - 1 } , w _ { i - 2 } , w _ { i - 3 } ) = \frac { 1 } { 2 4 } \bigg [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 1 } ) \bigg ]$ 3, wi−3), so if $f \equiv 0$ , then $F \equiv 0$ . The same result holds for the Adams-Moulton method.

(b) If $f$ has Lipschitz constant $L$ , then

$$
\begin{array} { r l r } {  { \vert F ( t _ { i } , h , w _ { i + 1 } , \dots , w _ { i - 3 } ) - F ( t _ { i } , h , v _ { i + 1 } , \dots , v _ { i - 3 } ) \vert \leq \frac { L } { 2 4 } \bigg [ 5 5 \vert w _ { i } - v _ { i } \vert + 5 9 \vert w _ { i - 1 } - v _ { i - 1 } \vert } } \\ & { } & { \qquad + 3 7 \vert w _ { i - 2 } - v _ { i - 2 } \vert + 9 \vert w _ { i - 3 } - v _ { i - 3 } \vert \bigg ] , } \end{array}
$$

so C $\begin{array} { r } { C = \frac { 5 9 } { 2 4 } L } \end{array}$ will suffice. A similar result holds for the Adams-Moulton method, but with $\begin{array} { r } { C = \frac { \mathrm { { 1 9 } } } { 2 4 } L } \end{array}$ .

3. By Exercise 31 in Section 5.4, we have

$$
\begin{array} { l c l } { \phi ( t , w , h ) } & { = } & { \displaystyle \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) } \\ & & { \displaystyle + \frac { 1 } { 3 } f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) \biggr ) } \\ & & { \displaystyle + \frac { 1 } { 6 } f \biggl ( t + h , w + h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) \biggr ) \biggr ) , } \end{array}
$$

so

$$
\phi ( t , w , 0 ) = \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 6 } f ( t , w ) = f ( t , w ) .
$$

$^ { * } 4$ . (a) Expand $y ( t _ { i + 1 } )$ and $y ( t _ { i + 2 } )$ in Taylor polynomials and simplify.

(b) $w _ { 2 } = 0 . 1 8 0 6 5 \approx y ( 0 . 2 ) = 0 . 1 8 1 2 7 , w _ { 5 } = 0 . 3 5 7 8 5 \approx y ( 0 . 5 ) = 0 . 3 9 3 4 7$ , $w _ { 7 } = 0 . 1 5 3 4 0 \approx$ $y ( 0 . 7 ) = 0 . 5 0 3 4 1$ , and $w _ { 1 0 } = - 9 . 7 8 2 2 \approx y ( 1 . 0 ) = 0 . 6 3 2 1 2$   
(c) $w _ { 2 0 } = - 6 0 . 4 0 2 \approx y ( 0 . 2 )$ , $w _ { 5 0 } = - 1 . 3 7 \times 1 0 ^ { 1 7 } \approx y ( 0 . 5 )$ , $w _ { 7 0 } = - 5 . 1 1 \times 1 0 ^ { 3 2 6 } \approx y ( 0 . 7 )$ , and $w _ { 1 0 0 } = - 1 . 1 6 \times 1 0 ^ { 4 1 } \approx y ( 1 . 0 )$   
(d) The method is consistent but not stable or convergent.

5. (a) The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } = \frac { 1 } { 4 } h ^ { 3 } y ^ { ( 4 ) } ( \xi _ { i } ) } \end{array}$ , for some $\xi$ , where $t _ { i - 2 } < \xi _ { i } < t _ { i + 1 }$ . (b) The method is consistent but unstable and not convergent.

6. For $h = 0 . 1$ :

$w _ { 1 0 } = 0 . 3 6 7 8 8 2 6 \approx y ( 1 ) = 0 . 3 6 7 8 7 9 4$ , a $\mathrm { \Delta \ n d ~ } \ w _ { 1 0 0 } = 3 . 8 4 9 1 7 \approx y ( 1 0 ) = 0 . 0 0 0 0 4 5 4 .$ . For $h = 0 . 0 1$ : $w _ { 1 0 0 } = 0 . 3 6 7 8 7 9 4 \approx y ( 1 ) = 0 . 3 6 7 8 7 9 4$ and $w _ { 1 0 0 0 } = 0 . 0 0 0 1 0 9 1 \approx y ( 1 0 ) = 0 . 0 0 0 0 4 5 4$ .

7. The method is unstable.

\*8. $w _ { 2 } = 4 \varepsilon$ , $w _ { 3 } = 1 3 \varepsilon$ , $w _ { 4 } = 4 0 \varepsilon$ , $w _ { 5 } = 1 2 1 \varepsilon$ , $w _ { 6 } = 3 6 4 \varepsilon$

# Exercise Set 5.11, page 354

1. Euler’s method gives the results in the following tables.

<table><tr><td rowspan="7">*(a) 0.500</td><td>ti Wi</td><td>Yi</td></tr><tr><td>0.200 0.027182818</td><td>0.449328964</td></tr><tr><td>0.000027183</td><td>0.030197383</td></tr><tr><td>0.700 0.000000272</td><td>0.004991594</td></tr><tr><td>1.000 0.000000000</td><td>0.000335463</td></tr><tr><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td><td rowspan="2">yi</td></tr><tr><td>ti</td><td>Wi</td></tr><tr><td>0.200</td><td>0.373333333</td><td>0.046105213</td></tr><tr><td>0.500</td><td>-0.093333333</td><td>0.250015133</td></tr><tr><td>0.700</td><td>0.146666667</td><td>0.490000277</td></tr><tr><td>1.000</td><td>1.333333333</td><td>1.000000001</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td>0.500</td><td>16.47925</td><td>0.479470939</td></tr><tr><td>1.000</td><td>256.7930</td><td>0.841470987</td></tr><tr><td>1.500</td><td>4096.142</td><td>0.997494987</td></tr><tr><td>2.000</td><td>65523.12</td><td>0.909297427</td></tr></table>

<table><tr><td rowspan="2">ti</td><td>Wi</td><td>Yi</td></tr><tr><td>6.128259</td><td>1.000000001</td></tr><tr><td>0.200</td><td>-378.2574</td><td>1.000000000</td></tr><tr><td>0.500 0.700</td><td>-6052.063</td><td>1.000000000</td></tr><tr><td></td><td>387332.0</td><td>1.000000000</td></tr><tr><td>1.000</td><td></td><td></td></tr></table>

2. Euler’s method gives the results in the following tables.

<table><tr><td colspan="2">(a) ti Wi</td><td>Yi</td></tr><tr><td>0.2</td><td>1.4631026</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.5421118</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.8223081</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.2104643</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.6960402</td><td>2.7250198</td></tr></table>

<table><tr><td colspan="2">(b)</td><td></td></tr><tr><td>ti</td><td>Wi 0.2</td><td>yi 0.56787944</td></tr><tr><td colspan="3">0.2</td></tr><tr><td rowspan="2">0.4 0.6</td><td>0.4</td><td>0.44978707</td></tr><tr><td>0.6</td><td>0.60673795</td></tr><tr><td>0.8</td><td>0.8 1.00012341</td><td>0.80091188</td></tr><tr><td colspan="3">1.0 1.0</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td>1.25</td><td>0.2500008</td><td>0.48848225</td></tr><tr><td>1.75</td><td>-1.5816058</td><td>0.18657591</td></tr><tr><td>2.25</td><td>-13.2433087</td><td>0.08779149</td></tr><tr><td>2.75</td><td>-100.7565966</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="2">ti Wi</td><td>yi</td></tr><tr><td>0.25</td><td>5.0000000</td><td>0.96217447</td></tr><tr><td>0.75</td><td>65.137212</td><td>0.73168856</td></tr><tr><td>1.25</td><td>1030.7344</td><td>0.31532236</td></tr><tr><td>1.75</td><td>16486.497</td><td>-0.17824606</td></tr></table>

3. The Runge-Kutta fourth order method gives the results in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>Wi</td><td>Yi</td></tr><tr><td colspan="2"></td><td>0.45881186</td><td>0.44932896</td></tr><tr><td colspan="2">0.200 0.500</td><td>0.03181595</td><td>0.03019738</td></tr><tr><td colspan="2">0.700</td><td>0.00537013</td><td>0.00499159</td></tr><tr><td colspan="2">1.000</td><td>0.00037239</td><td>0.00033546</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>yi</td></tr><tr><td colspan="2"></td><td>0.07925926</td><td>0.04610521</td></tr><tr><td colspan="2">0.200 0.500</td><td>0.25386145</td><td>0.25001513</td></tr><tr><td colspan="2">0.700</td><td>0.49265127</td><td>0.49000028</td></tr><tr><td colspan="2">1.000</td><td>1.00250560</td><td>1.00000000</td></tr><tr><td colspan="4">(c)</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td></td><td>0.500</td><td>188.3082</td><td>0.47947094</td></tr><tr><td></td><td>1.000</td><td>35296.68</td><td>0.84147099</td></tr><tr><td></td><td>1.500</td><td>6632737</td><td>0.99749499</td></tr><tr><td>2.000</td><td></td><td>1246413200</td><td>0.90929743</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td>0.200</td><td>-215.7459</td><td>1.00000000</td></tr><tr><td>0.500</td><td>-555750.0</td><td>1.00000000</td></tr><tr><td>0.700</td><td>-104435653</td><td>1.00000000</td></tr><tr><td>1.000</td><td>-269031268010</td><td>1.00000000</td></tr></table>

4. The Runge-Kutta fourth order method gives the results in the following tables.

<table><tr><td rowspan=1 colspan=1>(a)</td><td rowspan=1 colspan=1>ti       Wi           Yi</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2  1.5895980  1.5892822</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4  1.6274132  1.6271500</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  1.8720749  1.8719059</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8  2.2439777  2.2438566</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0 2.7251239  2.7250198</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti 0.2</td><td></td><td>Wi 0.5822584</td><td>Yi 0.56787944</td></tr><tr><td>0.4</td><td></td><td>0.4537551</td><td>0.44978707</td></tr><tr><td>0.6</td><td></td><td>0.6075593</td><td>0.60673795</td></tr><tr><td></td><td>0.8</td><td>0.8010630</td><td>0.80091188</td></tr><tr><td></td><td>1.0</td><td>1.0001495</td><td>1.00012341</td></tr></table>

<table><tr><td colspan="2">(c) ti</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Wi</td><td>yi</td></tr><tr><td colspan="2">1.25</td><td>0.8240614</td><td>0.48848225</td></tr><tr><td colspan="2">1.75</td><td>4.9786559</td><td>0.18657591</td></tr><tr><td colspan="2">2.25</td><td>66.9187958</td><td>0.08779149</td></tr><tr><td colspan="2">2.75</td><td>930.8525134</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="4">d</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td></td><td>0.25</td><td>-12.8205769</td><td>0.96217447</td></tr><tr><td></td><td>0.75</td><td>-2591.69792</td><td>0.73168856</td></tr><tr><td></td><td>1.25</td><td>-487165.725</td><td>0.31532236</td></tr><tr><td></td><td>1.75</td><td>-91547464.8</td><td>-0.17824606</td></tr></table>

5. The Adams Fourth-Order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td colspan="2">(a) ti Wi</td><td></td><td>yi</td></tr><tr><td></td><td>0.200</td><td>0.4588119</td><td>0.4493290</td></tr><tr><td></td><td>0.500</td><td>-0.0112813</td><td>0.0301974</td></tr><tr><td></td><td>0.700</td><td>0.0013734</td><td>0.0049916</td></tr><tr><td></td><td>1.000</td><td>0.0023604</td><td>0.0003355</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>Yi</td></tr><tr><td rowspan="3"></td><td>0.200</td><td>0.0792593</td><td>0.0461052</td></tr><tr><td>0.500</td><td>0.1554027</td><td>0.2500151</td></tr><tr><td>0.700</td><td>0.5507445</td><td>0.4900003</td></tr><tr><td></td><td>1.000</td><td>0.7278557</td><td>1.0000000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti 0.500</td><td>Wi 188.3082</td><td>Yi 0.4794709</td></tr><tr><td>1.000</td><td>38932.03</td><td>0.8414710</td></tr><tr><td>1.500</td><td>9073607</td><td>0.9974950</td></tr><tr><td></td><td></td><td></td></tr><tr><td>2.000</td><td>2115741299</td><td>0.9092974</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td>0.200</td><td>-215.7459</td><td>1.000000001</td></tr><tr><td>0.500</td><td>-682637.0</td><td>1.000000000</td></tr><tr><td>0.700</td><td>-159172736</td><td>1.000000000</td></tr><tr><td>1.000</td><td>-566751172258</td><td>1.000000000</td></tr></table>

6. The Adams Fourth-Order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.5895980</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.6263206</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.8709345</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.2432194</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.7246942</td><td>2.7250198</td></tr></table>

<table><tr><td rowspan=2 colspan=1>(b)</td><td rowspan=1 colspan=1>ti       Wi          y(ti)</td></tr><tr><td rowspan=1 colspan=1>0.2  0.5822584  0.56787944</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4  0.3911238  0.44978707</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  0.5971191  0.60673795</td></tr><tr><td rowspan=1 colspan=2>0.8  0.7826888  0.80091188</td></tr><tr><td rowspan=1 colspan=2>1.0  1.0082013  1.00012341</td></tr></table>

<table><tr><td colspan="3">(c)</td></tr><tr><td>ti</td><td>Wi 0.8240614</td><td>y(ti) 0.48848225</td></tr><tr><td>1.25 1.75</td><td>4.9786559</td><td>0.18657591</td></tr><tr><td>2.25</td><td>200.8236197</td><td>0.08779149</td></tr><tr><td>2.75</td><td>10272.0539300</td><td>0.04808415</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>-12.820577</td><td>0.96217447</td></tr><tr><td>0.75</td><td>-2591.6979</td><td>0.73168856</td></tr><tr><td>1.25</td><td>-598288.88</td><td>0.31532236</td></tr><tr><td>1.75</td><td>-139504990</td><td>-0.17824606</td></tr></table>

7. The Trapezoidal Algorithm gives the results in the following tables.

<table><tr><td rowspan="7">*(a)</td><td colspan="4"></td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.200</td><td>0.39109643</td><td>2</td><td>0.44932896</td></tr><tr><td>0.500</td><td>0.02134361</td><td>2</td><td>0.03019738</td></tr><tr><td>0.700</td><td>0.00307084</td><td>2</td><td>0.00499159</td></tr><tr><td>1.000</td><td>0.00016759</td><td>2</td><td>0.00033546</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.200</td><td>0.04000000</td><td>2</td><td>0.04610521</td></tr><tr><td>0.500</td><td>0.25000000</td><td>2</td><td>0.25001513</td></tr><tr><td>0.700</td><td>0.49000000</td><td>2</td><td>0.49000028</td></tr><tr><td>1.000</td><td>1.00000000</td><td>2</td><td>1.00000000</td></tr><tr><td colspan="4">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.500</td><td>0.66291133</td><td>2</td><td>0.47947094</td></tr><tr><td>1.000</td><td>0.87506346</td><td>2</td><td>0.84147099</td></tr><tr><td>1.500</td><td>1.00366141</td><td>2</td><td>0.99749499</td></tr><tr><td>2.000</td><td>0.91053267</td><td>2</td><td>0.90929743</td></tr></table>

<table><tr><td colspan="2">(d) ti 0.200</td><td>Wi k</td><td></td><td>Yi</td></tr><tr><td colspan="2"></td><td>-1.07568307</td><td>4</td><td>1.00000000</td></tr><tr><td colspan="2">0.500</td><td>-0.97868360</td><td>4</td><td>1.00000000</td></tr><tr><td colspan="2">0.700</td><td>-0.99046408</td><td>3</td><td>1.00000000</td></tr><tr><td colspan="2">1.000</td><td>-1.00284456</td><td>3</td><td>1.00000000</td></tr></table>

8. The Trapezoidal Algorithm gives the results in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.58152229</td><td>2</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.62161373</td><td>2</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.86902118</td><td>2</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.24264359</td><td>2</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.72470482</td><td>2</td><td>2.7250198</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.50203131</td><td>2</td><td>0.56787944</td></tr><tr><td>0.4</td><td>0.43355903</td><td>2</td><td>0.44978707</td></tr><tr><td>0.6</td><td>0.60372878</td><td>2</td><td>0.60673795</td></tr><tr><td>0.8</td><td>0.80041431</td><td>2</td><td>0.80091188</td></tr><tr><td>1.0</td><td>1.00004603</td><td>2</td><td>1.00012341</td></tr></table>

<table><tr><td colspan="4">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>1.25</td><td>0.49787835</td><td>2</td><td>0.48848225</td></tr><tr><td>1.75</td><td>0.18503499</td><td>2</td><td>0.18657591</td></tr><tr><td>2.25</td><td>0.08754204</td><td>2</td><td>0.08779149</td></tr><tr><td>2.75</td><td>0.04802381</td><td>2</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.39753016</td><td>2</td><td>0.96217447</td></tr><tr><td>0.75</td><td>0.81057360</td><td>2</td><td>0.73168856</td></tr><tr><td>1.25</td><td>0.33002435</td><td>2</td><td>0.31532236</td></tr><tr><td>1.75</td><td>-0.17533094</td><td>2</td><td>-0.17824606</td></tr></table>

9. The Runge-Kutta fourth-order method gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.100</td><td>-96.33011</td><td>0.66987648</td><td>193.6651</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>-28226.32</td><td>0.67915383</td><td>56453.66</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>-8214056</td><td>0.69387881</td><td>16428113</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>-2390290586</td><td>0.71354670</td><td>4780581173</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>-695574560790</td><td>0.73768711</td><td>1391149121600</td><td>-0.36884355</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td></tr><tr><td>0.100</td><td>0.61095960</td><td>0.66987648</td><td>-0.21708179</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>0.66873489</td><td>0.67915383</td><td>-0.31873903</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>0.69203679</td><td>0.69387881</td><td>-0.34325535</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>0.71322103</td><td>0.71354670</td><td>-0.35612202</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>0.73762953</td><td>0.73768711</td><td>-0.36872840</td><td>-0.36884355</td></tr></table>

10. Since $y ^ { \prime } = \lambda y$ , we have

$$
k _ { 1 } = h \lambda w _ { i } , \quad k _ { 2 } = h \lambda \big ( w _ { i } + h \lambda w _ { i } / 2 \big ) , \quad k _ { 3 } = h \lambda \big ( w _ { i } + h \lambda w _ { i } / 2 + h ^ { 2 } \lambda ^ { 2 } w _ { i } / 4 \big ) ,
$$

and

$$
k _ { 4 } = h \lambda \left( w _ { i } + h \lambda w _ { i } + h ^ { 2 } \lambda ^ { 2 } w _ { i } / 2 + h ^ { 3 } \lambda ^ { 3 } w _ { i } / 4 \right) .
$$

Thus

$$
\begin{array} { l } { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 } + 2 k _ { 2 } + 2 k _ { 3 } + k _ { 4 } ) } } \\ { { \mathrm { } = w _ { i } + \displaystyle \frac { w _ { i } } { 6 } \left( h \lambda + 2 h \lambda + h ^ { 2 } \lambda ^ { 2 } + 2 h \lambda + h ^ { 2 } \lambda ^ { 2 } + h ^ { 3 } \lambda ^ { 3 } / 2 + h \lambda + h ^ { 2 } \lambda ^ { 2 } + \displaystyle \frac { 1 } { 2 } h ^ { 3 } \lambda ^ { 3 } + \displaystyle \frac { 1 } { 4 } h ^ { 4 } \lambda ^ { 4 } \right) } } \\ { { \mathrm { } = \left( 1 + h \lambda + \displaystyle \frac { 1 } { 2 } h ^ { 2 } \lambda ^ { 2 } + \displaystyle \frac { 1 } { 6 } h ^ { 3 } \lambda ^ { 3 } + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } \lambda ^ { 4 } \right) w _ { i } . } } \end{array}
$$

$^ *$ 11. Using Eq. (4.25) gives $\begin{array} { r } { \tau _ { i + 1 } = \frac { - y ^ { \prime \prime \prime } ( \xi _ { i } ) } { 1 2 } h ^ { 2 } } \end{array}$ , for some $t _ { i } < \xi _ { i } < t _ { i + 1 }$ , and by Definition 5.18, the Trapezoidal method is consistent. Once again using Eq. (4.25) gives

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + { \frac { h } { 2 } } [ f ( t _ { i } , y ( t _ { i } ) ) + f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) ] - { \frac { y ^ { \prime \prime \prime } ( \xi _ { i } ) } { 1 2 } } h ^ { 3 } .
$$

Subtracting the difference equation and using the Lipschitz constant $L$ for $f$ gives

$$
| y ( t _ { i + 1 } ) - w _ { i + 1 } | \leq | y ( t _ { i } ) - w _ { i } | + \frac { h L } { 2 } | y ( t _ { i } ) - w _ { i } | + \frac { h L } { 2 } | y ( t _ { i + 1 } ) - w _ { i + 1 } | + \frac { h ^ { 3 } } { 1 2 } | y ^ { \prime \prime \prime } ( \xi _ { i } ) | .
$$

Let $M = \mathrm { m a x } _ { a \leq x \leq b } | y ^ { \prime \prime \prime } ( x ) |$ . Then, assuming $h L \neq 2$ ,

$$
| y ( t _ { i + 1 } ) - w _ { i + 1 } | \leq \frac { 2 + h L } { 2 - h L } | y ( t _ { i } ) - w _ { i } | + \frac { h ^ { 3 } } { 6 ( 2 - h L ) } M .
$$

Using Lemma 5.8, we have

$$
\left| y ( t _ { i + 1 } ) - w _ { i + 1 } \right| \leq e ^ { 2 ( b - a ) L / ( 2 - h L ) } \bigg [ \frac { M h ^ { 2 } } { 1 2 L } + | \alpha - w _ { 0 } | \bigg ] - \frac { M h ^ { 2 } } { 1 2 L } .
$$

So if $h L \neq 2$ , the Trapezoidal method is convergent, and consequently stable.

12. The Backward Euler method applied to $y ^ { \prime } = \lambda y$ gives

$$
w _ { i + 1 } = { \frac { w _ { i } } { 1 - h \lambda } } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 1 } { 1 - h \lambda } } .
$$

13. The following tables list the results of the Backward Euler method applied to the problems in Exercise 1.

(1a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.75298666</td><td>2</td><td>0.44932896</td></tr><tr><td>5</td><td>0.5</td><td>0.10978082</td><td>2</td><td>0.03019738</td></tr><tr><td>7</td><td>0.7</td><td>0.03041020</td><td>2</td><td>0.00499159</td></tr><tr><td>10</td><td>1.0</td><td>0.00443362</td><td>2</td><td>0.00033546</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.08148148</td><td>2</td><td>0.04610521</td></tr><tr><td>5</td><td>0.5</td><td>0.25635117</td><td>2</td><td>0.25001513</td></tr><tr><td>7</td><td>0.7</td><td>0.49515013</td><td>2</td><td>0.49000028</td></tr><tr><td>10</td><td>1.0</td><td>1.00500556</td><td>2</td><td>1.00000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.5</td><td>0.50495522</td><td>2</td><td>0.47947094</td></tr><tr><td>4</td><td>1.0</td><td>0.83751817</td><td>2</td><td>0.84147099</td></tr><tr><td>6</td><td>1.5</td><td>0.99145076</td><td>2</td><td>0.99749499</td></tr><tr><td>8</td><td>2.0</td><td>0.90337560</td><td>2</td><td>0.90929743</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>1.00348713</td><td>3</td><td>1.00000000</td></tr><tr><td>5</td><td>0.5</td><td>1.00000262</td><td>2</td><td>1.00000000</td></tr><tr><td>7</td><td>0.7</td><td>1.00000002</td><td>1</td><td>1.00000000</td></tr><tr><td>10</td><td>1.0</td><td>1.00000000</td><td>1</td><td>1.00000000</td></tr></table>

14. The following tables list the results of the Backward Euler method applied to the problems in Exercise 2.   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>1.67216224</td><td>2</td><td>1.58928220</td></tr><tr><td>4</td><td>0.4</td><td>1.69987544</td><td>2</td><td>1.62715998</td></tr><tr><td>6</td><td>0.6</td><td>1.92400672</td><td>2</td><td>1.87190587</td></tr><tr><td>8</td><td>0.8</td><td>2.28233119</td><td>2</td><td>2.24385657</td></tr><tr><td>10</td><td>1.0</td><td>2.75757631</td><td>2</td><td>2.72501978</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.87957046</td><td>2</td><td>0.56787944</td></tr><tr><td>4</td><td>0.4</td><td>0.56989261</td><td>2</td><td>0.44978707</td></tr><tr><td>6</td><td>0.6</td><td>0.64247315</td><td>2</td><td>0.60673795</td></tr><tr><td>8</td><td>0.8</td><td>0.81061829</td><td>2</td><td>0.80091188</td></tr><tr><td>10</td><td>1.0</td><td>1.00265457</td><td>2</td><td>1.00012341</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.25</td><td>0.55006309</td><td>2</td><td>0.51199999</td></tr><tr><td>3</td><td>1.75</td><td>0.19753128</td><td>2</td><td>0.18658892</td></tr><tr><td>5</td><td>2.25</td><td>0.09060118</td><td>2</td><td>0.08779150</td></tr><tr><td>7</td><td>2.75</td><td>0.04900207</td><td>2</td><td>0.04808415</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>0.79711852</td><td>2</td><td>0.96217447</td></tr><tr><td>3</td><td>0.75</td><td>0.72203841</td><td>2</td><td>0.73168856</td></tr><tr><td>5</td><td>1.25</td><td>0.31248267</td><td>2</td><td>0.31532236</td></tr><tr><td>7</td><td>1.75</td><td>-0.17796016</td><td>2</td><td>-0.17824606</td></tr></table>

15. (a) The Trapezoidal method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { 1 + { \frac { h \lambda } { 2 } } } { 1 - { \frac { h \lambda } { 2 } } } } ~ w _ { j } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 2 + h \lambda } { 2 - h \lambda } } .
$$

Thus, $| Q ( h \lambda ) | < 1$ , whenever $\mathrm { R e } ( h \lambda ) < 0$ .

(b) The Backward Euler method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { w _ { j } } { 1 - h \lambda } } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 1 } { 1 - h \lambda } } .
$$

Thus, $| Q ( h \lambda ) | < 1$ , whenever $\mathrm { R e } ( h \lambda ) < 0$ .

# Direct Methods for Solving Linear Systems

# Exercise Set 6.1, page 368

1. \*(a) Intersecting lines with solution $x _ { 1 } = x _ { 2 } = 1$ . (b) One line, so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = \frac { 3 } { 2 } - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ . (c) One line, so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ . \*(d) Intersecting lines with solution $\textstyle x _ { 1 } = { \frac { 2 } { 7 } }$ and $\textstyle x _ { 2 } = - { \frac { 1 1 } { 7 } }$ .

2. (a) Intersecting lines whose solution is $x _ { 1 } = x _ { 2 } = 0$ . (b) Parallel lines, so there is no solution. (c) Three lines in the plane that do not intersect at a common point. (d) Two planes in space which intersect in a line with $\textstyle x _ { 1 } = - { \frac { 5 } { 4 } } x _ { 2 }$ and $\begin{array} { r } { x _ { 3 } = \frac { 3 } { 2 } x _ { 2 } + 1 } \end{array}$

3. Gaussian elimination gives the following solutions.

(a) $x _ { 1 } = 1 . 0$ , $x _ { 2 } = - 0 . 9 8$ , x3 = 2.9 (b) $x _ { 1 } = 1 . 1$ , $x _ { 2 } = - 1 . 1$ , $x _ { 3 } = 2 . 9$

4. Gaussian elimination gives the following solutions.

$$
\begin{array} { l l } { { x _ { 1 } = - 0 . 7 0 , x _ { 2 } = 1 . 1 , x _ { 3 } = 2 . 9 } } \\ { { \nonumber } } \\ { { x _ { 1 } = - 0 . 8 8 , x _ { 2 } = 0 . 7 4 , x _ { 3 } = 3 . 0 } } \end{array}
$$

5. Gaussian elimination gives the following solutions.

\*(a) $x _ { 1 } = 1 . 1 8 7 5 , x _ { 2 } = 1 . 8 1 2 5 , x _ { 3 } = 0 . 8 7 5$ with one row interchange required (b) $x _ { 1 } = - 1 , x _ { 2 } = 0 , x _ { 3 } = 1$ with no interchange required (c) $x _ { 1 } = 1 . 5 , x _ { 2 } = \mathrm { { ^ 2 } } , x _ { 3 } = - 1 . 2 , x _ { 4 } = \mathrm { { ^ 3 } }$ with no interchange required (d) No unique solution

6. Gaussian elimination gives the following solutions.

(a) $x _ { 1 } = - 4$ , $x _ { 2 } = - 8$ , $x _ { 3 } = - 6$ with one row interchange required (b) $\textstyle x _ { 1 } = { \frac { 2 2 } { 9 } }$ , $\textstyle x _ { 2 } = - { \frac { 4 } { 9 } }$ , $x _ { 3 } = { \textstyle { \frac { 4 } { 3 } } } , x _ { 4 } = 1$ with one row interchange required

(c) $x _ { 1 } = 1 3$ , $x _ { 2 } = 8$ , $x _ { 3 } = 8 , x _ { 4 } = 5$ with one row interchange required.   
(d) $x _ { 1 } = - 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = 0 , x _ { 4 } = 1$ with one row interchange required.

7. Gaussian elimination with Digits:=10 gives the following solutions:

(a) $x _ { 1 } = - 2 2 7 . 0 7 6 9$ , $x _ { 2 } = 4 7 6 . 9 2 3 1$ , $x _ { 3 } = - 1 7 7 . 6 9 2 3$ ;   
(b) $x _ { 1 } = 1 . 0 0 1 2 9 1$ , $x _ { 2 } = 1$ , $x _ { 3 } = 1 . 0 0 1 5 5$ ;   
(c) $x _ { 1 } = - 0 . 0 3 1 7 4 6 0 0$ , $x _ { 2 } = 0 . 5 9 5 2 3 7 7$ , $x _ { 3 } = - 2 . 3 8 0 9 5 1$ , $x _ { 4 } = 2 . 7 7 7 7 7 7 7$ ;   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 9$ , $x _ { 2 } = 1 . 9 6 4 9 1 2$ , $x _ { 3 } = - 0 . 9 8 8 3 0 4 1$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$ .

8. Gaussian elimination with Digits:=10 gives the following solutions:

(a) $x _ { 1 } = 0 . 9 7 9 8 6 5 7 7 2 0$ , $x _ { 2 } = 4 . 2 8 1 8 7 9 1 9 1$ , $x _ { 3 } = 1 7 . 4 8 3 2 2 1 4 7$ ;   
(b) $x _ { 1 } = 6 . 4 6 1 4 4 7 6 2 0$ , $x _ { 2 } = 8 . 3 9 4 3 2 1 0 9 2$ , $x _ { 3 } = - 0 . 0 1 3 4 7 3 6 8 6 1 8$ ;   
(c) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9$ , $x _ { 2 } = - 4 . 6 7 7 9 8 7 7 6$ , $x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9$ , $x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2$ ;   
(d) $x _ { 1 } = 1 3 . 4 9 9 9 9 9 9 8$ , $x _ { 2 } = - 1 1 . 5 0 0 0 0 0 0 0 0 0 0$ , $x _ { 3 } = 2 3 . 7 5 0 0 0 0 0 3$ , $x _ { 4 } = 1 2 1 . 5 0 0 0 0 3 , x _ { 5 } =$ 97.75000025.

$^ { * } 9$ . (a) When $\alpha = - 1 / 3$ , there is no solution. (b) When $\alpha = 1 / 3$ , there is an infinite number of solutions with $x _ { 1 } = x _ { 2 } + 1 . 5$ , and $x _ { 2 }$ is arbitrary. (c) If $\alpha \neq \pm 1 / 3$ , then the unique solution is

$$
x _ { 1 } = \frac { 3 } { 2 ( 1 + 3 \alpha ) } \quad \mathrm { a n d } \quad x _ { 2 } = \frac { - 3 } { 2 ( 1 + 3 \alpha ) } .
$$

10. (a) $\alpha = 1$ (b) $\alpha = - 1$ (c) $x _ { 1 } = - 1 / ( 1 - \alpha ) , x _ { 2 } = 1 , x _ { 3 } = 1 / ( 1 - \alpha )$

11. Suppose $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ is a solution to the linear system (6.1).

(i) The new system becomes

$$
\begin{array} { c } { E _ { 1 } : a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + . . . + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \ \qquad \vdots } \\ { E _ { i } : \lambda a _ { i 1 } x _ { 1 } + \lambda a _ { i 2 } x _ { 2 } + . . . + \lambda a _ { i n } x _ { n } = \lambda b _ { i } } \\ { \ \qquad \vdots } \\ { E _ { n } : a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + . . . + a _ { n n } x _ { n } = b _ { n } . } \end{array}
$$

Clearly, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies this system. Conversely, if $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ satisfies the new system, dividing $E _ { i }$ by $\lambda$ shows $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ also satisfies (6.1).

(ii) The new system becomes

$$
\begin{array} { c } { E _ { 1 } : a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + . . . + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \ } \\ { \vdots } \\ { E _ { i } : ( a _ { i 1 } + \lambda a _ { j 1 } ) x _ { 1 } + ( a _ { i 2 } + \lambda a _ { j 2 } ) x _ { 2 } + . . . + ( a _ { i n } + \lambda a _ { j n } ) x _ { n } = b _ { i } + \lambda b _ { j } } \\ { \ } \\ { \vdots } \\ { E _ { n } : a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + . . . + a _ { n n } x _ { n } = b _ { n } . } \end{array}
$$

Clearly, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies all but possibly the $i$ th equation. Multiplying $E _ { j }$ by $\lambda$ gives

$$
\lambda a _ { j 1 } x _ { 1 } ^ { \prime } + \lambda a _ { j 2 } x _ { 2 } ^ { \prime } + . . . + \lambda a _ { j n } x _ { n } ^ { \prime } = \lambda b _ { j } ,
$$

which can be subtracted from $E _ { i }$ in the new system results in the system (6.1). Thus, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies the new system. Conversely, if $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ is a solution to the new system, then all but possibly $E _ { i }$ of (6.1) are satisfied by $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ . Multiplying $E _ { j }$ of the new system by $- \lambda$ gives

$$
- \lambda a _ { j 1 } x _ { 1 } ^ { * } - \lambda a _ { j 2 } x _ { 2 } ^ { * } - . . . - \lambda a _ { j n } x _ { n } ^ { * } = - \lambda b _ { j } .
$$

Adding this to $E _ { i }$ in the new system produces $E _ { i }$ of (6.1). Thus, $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ is a solution of (6.1).

(iii) The new system and the old system have the same set of equations to satisfy. Thus, they have the same solution set.

\*12. Change Algorithm 6.1 as follows:

STEP 1 For $i = 1 , \ldots , n$ do STEPS 2, 3, and 4.   
STEP 4 For $j = 1 , \dotsc , i - 1 , i + 1 , \dotsc , n$ do STEPS 5 and 6.   
STEP 8 For $i = 1 , \ldots , n$ set $x _ { i } = a _ { i , n + 1 } / a _ { i i }$ .

In addition, delete STEP 9.

13. The Gauss-Jordan method gives the following results.

(a) $x _ { 1 } = 0 . 9 8 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$ (b) $x _ { 1 } = 1 . 1 , x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

14. The Gauss-Jordan method with single precision arithmetic gives the following solutions.

(a) $x _ { 1 } = - 2 2 7 . 0 7 8 7$ , $x _ { 2 } = 4 7 6 . 9 2 6 \div 2$ , $x _ { 3 } = - 1 7 7 . 6 9 3 4$   
(b) $x _ { 1 } = 1 . 0 0 0 0 3 6$ , $x _ { 2 } = 0 . 9 9 9 9 9 9 1$ , $x _ { 3 } = 0 . 9 9 8 6 0 5 2$   
(c) $x _ { 1 } = - 0 . 0 3 1 7 7 1 2 0$ , $x _ { 2 } = 0 . 5 9 5 5 5 7 2$ , $x _ { 3 } = - 2 . 3 8 1 7 6 8$ , $x _ { 4 } = 2 . 7 7 8 3 2 9$   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 9$ , $x _ { 2 } = 1 . 9 6 4 9 1 2$ , $x _ { 3 } = - 0 . 9 8 8 3 0 3 6$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$

\*15. The results for are listed in the following table. (The abbreviations M/D and A/S are used for multiplications/divisions and additions/subtractions, respectively.)   

<table><tr><td colspan="3">Gaussian elimination</td><td colspan="2">Gauss-Jordan</td></tr><tr><td>n</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td></tr><tr><td>3</td><td>17</td><td>11</td><td>21</td><td>12</td></tr><tr><td>10</td><td>430</td><td>375</td><td>595</td><td>495</td></tr><tr><td>50</td><td>44150</td><td>42875</td><td>64975</td><td>62475</td></tr><tr><td>100</td><td>343300</td><td>338250</td><td>509950</td><td>499950</td></tr></table>

\*16. (a) The Gaussian elimination procedure requires

and

$$
{ \frac { n ^ { 3 } - n } { 3 } } ~ \mathrm { A d d i t i o n s } / \mathrm { S u b t r a c t i o n s } .
$$

The additional elimination steps are:

$$
\mathrm { F o r } \ i = n , n - 1 , . . . , 2
$$

$$
\mathrm { s e t } a _ { j , n + 1 } = a _ { j , n + 1 } - \frac { a _ { j i } a _ { i , n + 1 } } { a _ { i i } } .
$$

This requires

and

$$
\frac { n ( n - 1 ) } { 2 } \mathrm { \ A d d i t i o n s / S u b t r a c t i o n s } .
$$

Solving for

$$
x _ { i } = \frac { a _ { i , n + 1 } } { a _ { i i } }
$$

requires $n$ divisions. Thus, the totals are

$$
\mathrm { ~ \frac { \it { n ^ { 3 } } } { 3 } + \frac { 3 \it { n ^ { 2 } } } { 2 } - \frac { 5 \it { n } } { 6 } M u l t i p l i c a t i o n s / D i v i s i o n s }
$$

and

$$
{ \frac { n ^ { 3 } } { 3 } } + { \frac { n ^ { 2 } } { 2 } } - { \frac { 5 n } { 6 } } ~ { \mathrm { A d d i t i o n s / S u b t r a c t i o n s } } .
$$

(b) The results are listed in the following table. In this table the abbreviations M/D and A/S are used for Multiplications/Divisions and for Additions/Subtractions, respectively.   

<table><tr><td colspan="3">Gaussian Elimination</td><td colspan="2">Gauss-Jordan</td><td colspan="2">Hybrid</td></tr><tr><td>n</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td></tr><tr><td>3</td><td>17</td><td>11</td><td>21</td><td>12</td><td>20</td><td>11</td></tr><tr><td>10</td><td>430</td><td>375</td><td>595</td><td>495</td><td>475</td><td>375</td></tr><tr><td>50</td><td>44150</td><td>42875</td><td>64975</td><td>62475</td><td>45375</td><td>42875</td></tr><tr><td>100</td><td>343300</td><td>338250</td><td>509950</td><td>499950</td><td>348250</td><td>338250</td></tr></table>

17. The Gaussian-Elimination–Gauss-Jordan hybrid method gives the following results.

(a) $x _ { 1 } = 1 . 0 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$ (b) $x _ { 1 } = 1 . 0 , x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

18. The Gauss-Jordan hybrid method with single-precision arithmetic gives the following solutions.

(a) 227.0788, 476.9262, 177.6934   
(b) 0.9990999, 0.9999991, 0.9986052   
(c) −0.03177060, 0.5955554, −2.381768, 2.778329   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 6$ , $x _ { 2 } = 1 . 9 6 4 9 1 6$ , $x _ { 3 } = - 0 . 9 8 8 3 0 2 7$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$

19. (a) There is sufficient food to satisfy the average daily consumption.

(b) We could add 200 of species 1, or 150 of species 2, or 100 of species 3, or 100 of species 4.   
(c) Assuming none of the increases indicated in part (b) was selected, species 2 could be increased by 650, or species 3 could be increased by 150, or species 4 could be increased by 150.   
(d) Assuming none of the increases indicated in parts (b) or (c) were selected, species 3 could be increased by 150, or species 4 could be increased by 150.

$^ *$ 20. (a) For the Trapezoidal rule $m = n = 1$ , $x _ { 0 } = 0$ , $x _ { 1 } = 1$ so that for $i = 0$ and 1, we have

$$
\begin{array} { l } { { \displaystyle u ( x _ { i } ) = f ( x _ { i } ) + \int _ { 0 } ^ { 1 } K ( x _ { i } , t ) u ( t ) ~ d t } } \\ { { \displaystyle \quad = f ( x _ { i } ) + \frac { 1 } { 2 } \left[ K ( x _ { i } , 0 ) u ( 0 ) + K ( x _ { i } , 1 ) u ( 1 ) \right] . } } \end{array}
$$

Substituting for $x _ { i }$ gives the desired equations.

(b) We have $n = 4$ , $\begin{array} { r } { h = \frac { 1 } { 4 } } \end{array}$ , $x _ { 0 } = 0$ , $\textstyle x _ { 1 } = { \frac { 1 } { 4 } }$ , $\begin{array} { r } { x _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , $\textstyle x _ { 3 } = { \frac { 3 } { 4 } }$ , and $x _ { 4 } = 1$ , so

$$
\begin{array} { l } { { \displaystyle u ( x _ { i } ) = f ( x _ { i } ) + \frac { h } { 2 } \biggl [ K ( x _ { i } , 0 ) u ( 0 ) + 2 K \left( x _ { i } , \frac 1 4 \right) u \left( \frac 1 4 \right) } } \\ { { \displaystyle \phantom { \frac { 1 } { 1 } } + 2 K \left( x _ { i } , \frac 1 2 \right) u \left( \frac 1 2 \right) + 2 K \left( x _ { i } , \frac 3 4 \right) u \left( \frac 3 4 \right) + K ( x _ { i } , 1 ) u ( 1 ) \biggr ] , } } \end{array}
$$

for $i = { 0 , 1 , 2 , 3 , 4 }$ . This gives

$$
( x _ { i } ) = x _ { i } ^ { 2 } + \frac { 1 } { 8 } \left[ e ^ { x _ { i } } u ( 0 ) + 2 e ^ { \left| x _ { i } - \frac { 1 } { 4 } \right| } u \left( \frac { 1 } { 4 } \right) + 2 e ^ { \left| x _ { i } - \frac { 1 } { 2 } \right| } u \left( \frac { 1 } { 2 } \right) + 2 e ^ { \left| x _ { i } - \frac { 3 } { 4 } \right| } u \left( \frac { 3 } { 4 } \right) + e ^ { \left| x _ { i } - 1 \right| } u ( 1 ) \right] ,
$$

for each $i = 1 , \ldots , 4$ . The $5 \times 5$ linear system has solution $u ( 0 ) = - 1 . 1 5 4 2 5 5$ , $\begin{array} { l } { { u \left( \frac 1 4 \right) = } } \end{array}$ $- 0 . 9 0 9 3 2 9 8$ , $\begin{array} { r } { u \left( \frac { 1 } { 2 } \right) = - 0 . 7 1 5 3 1 4 5 } \end{array}$ , $\begin{array} { r } { u \left( \frac { 3 } { 4 } \right) = - 0 . 5 4 7 2 9 4 9 } \end{array}$ , and $u ( 1 ) = - 0 . 3 9 3 1 2 6 1$ .

(c) The Composite Simpson’s rule gives

$$
\begin{array} { c l l } { \displaystyle \int _ { 0 } ^ { 1 } K ( x _ { i } , t ) u ( t ) \ d t = \frac { h } { 3 } \left[ K ( x _ { i } , 0 ) u ( 0 ) + 4 K \left( x _ { i } , \frac 1 4 \right) u \left( \frac 1 4 \right) + 2 K \left( x _ { i } , \frac 1 2 \right) u \left( \frac 1 2 \right) + \right. } \\ { \displaystyle \left. 4 K \left( x _ { i } , \frac 3 4 \right) u \left( \frac 3 4 \right) + K ( x _ { i } , 1 ) u ( 1 ) \right] , } \end{array}
$$

which results in the linear equations

$$
( x _ { i } ) = x _ { i } ^ { 2 } + { \frac { 1 } { 1 2 } } \left[ e ^ { x _ { i } } u ( 0 ) + 4 e ^ { \left| x _ { i } - { \frac { 1 } { 4 } } \right| } u \left( { \frac { 1 } { 4 } } \right) + 2 e ^ { \left| x _ { i } - { \frac { 1 } { 2 } } \right| } u \left( { \frac { 1 } { 2 } } \right) + 4 e ^ { \left| x _ { i } - { \frac { 3 } { 4 } } \right| } u \left( { \frac { 3 } { 4 } } \right) + e ^ { \left| x _ { i } - 1 \right| } u ( 1 ) \right] .
$$

The $5 \times 5$ linear system has solutions $u ( 0 ) = - 1 . 2 3 4 2 8 6$ , $\begin{array} { r } { u \left( \frac { 1 } { 4 } \right) = - 0 . 9 5 0 7 2 9 2 } \end{array}$ , $\begin{array} { l } { { u \left( \frac 1 2 \right) = } } \end{array}$ $- 0 . 7 6 5 9 4 0 0$ , $\begin{array} { r } { u \left( \frac { 3 } { 4 } \right) = - 0 . 5 8 4 4 7 3 7 } \end{array}$ , and $u ( 1 ) = - 0 . 4 4 8 4 9 7 5$ .

# Exercise Set 6.2, page 379

1. The following row interchanges are required for these systems.

(a) none   
\*(b) Interchange rows 2 and 3. (c) none   
(d) Interchange rows 1 and 2.

2. The following row interchanges are required for these systems.

(a) none (b) none (c) none (d) none

3. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2. \*(b) Interchange rows 1 and 3. (c) Interchange rows 1 and 2, then interchange rows 2 and 3. (d) Interchange rows 1 and 2.

4. The following row interchanges are required for these systems.

(a) Interchange rows 2 and 3.   
(b) Interchange rows 1 and 3.   
(c) Interchange rows 1 and 3, then interchange rows 2 and 3.   
(d) Interchange rows 1 and 2.

5. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 3, then interchange rows 2 and 3.   
\*(b) Interchange rows 2 and 3.   
(c) Interchange rows 2 and 3.   
(d) Interchange rows 1 and 3, then interchange rows 2 and 3.

6. The following row interchanges are required for these systems.

(a) Interchange rows 2 and 3.  
(b) none  
(c) Interchange rows 1 and 2, then interchange rows 2 and 3.(d) none

7. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3, and columns 2 and 3.   
\*(b) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3.   
(c) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3. (d) Interchange rows 1 and 2, and columns 1 and 2, then interchange rows 2 and 3; and columns 2 and 3.

8. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2, and columns 1 and 3.   
(b) Interchange rows 1 and 2, and columns 1 and 2, then interchange rows 2 and 3.   
(c) Interchange rows 1 and 3, and columns 1 and 2, then interchange rows 2 and 3, and columns 2 and 3.   
(d) Interchange rows 1 and 2.

9. Gaussian elimination with three-digit chopping arithmetic gives the following results.

$$
\begin{array} { l l } { { } } & { { x _ { 1 } = 3 0 . 0 , x _ { 2 } = 0 . 9 9 0 } } \\ { { } } & { { x _ { 1 } = 0 . 0 0 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 1 4 2 } } \\ { { } } & { { x _ { 1 } = 0 . 2 0 6 , x _ { 2 } = 0 . 0 1 5 4 , x _ { 3 } = - 0 . 0 1 5 6 , x _ { 4 } = - 0 . 7 1 6 } } \\ { { } } & { { x _ { 1 } = 0 . 8 2 8 , x _ { 2 } = - 3 . 3 2 , x _ { 3 } = 0 . 1 5 3 , x _ { 4 } = 4 . 9 1 } } \end{array}
$$

10. Gaussian elimination with three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$

(b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 2 , x _ { 3 } = - 9 . 7 8$ (c) $\begin{array} { l } { { \begin{array} { r l } & { \cdots \mathrm { ~ s - y ~ } , \cdots } \\ & { x _ { 1 } = - 8 . 2 5 , x _ { 2 } = - 8 . 0 0 , x _ { 3 } = - 0 . 0 3 3 9 , x _ { 4 } = 0 . 0 5 6 6 } \end{array} } } \\ { { \begin{array} { r l } & { x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } \end{array} } } \end{array}$ (d)

11. Gaussian elimination with three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = - 1 0 . 0$ , $x _ { 2 } = 1 . 0 1$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 8 5$ , $x _ { 2 } = 0 . 0 1 0 3$ , $x _ { 3 } = - 0 . 0 2 0 0$ , $x _ { 4 } = - 1 . 1 2$ (d) $x _ { 1 } = 0 . 7 9 9$ , $x _ { 2 } = - 3 . 1 2$ , $x _ { 3 } = 0 . 1 5 1$ , $x _ { 4 } = 4 . 5 6$

12. Gaussian elimination with three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 9$ , $x _ { 3 } = - 1 . 9 8$ (c) x1 = 0.0896, x2 = −0.0639, x3 = −0.0361, x4 = 0.0467 (d) $\mathfrak { c } _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5$

13. Gaussian elimination with partial pivoting and three-digit chopping arithmetic gives the following results.

\*(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = - 0 . 1 6 3$ , $x _ { 2 } = 9 . 9 8 , x _ { 3 } = 0 . 1 4 2$ (c) $x _ { 1 } = 0 . 1 7 7$ , $x _ { 2 } = - 0 . 0 0 7 2$ , $x _ { 3 } = - 0 . 0 2 0 8$ , $x _ { 4 } = - 1 . 1 8$ (d) $x _ { 1 } = 0 . 7 7 7$ , $x _ { 2 } = - 3 . 1 0$ , $x _ { 3 } = 0 . 1 6 1$ , $x _ { 4 } = 4 . 5 0$

14. Gaussian elimination with partial pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 5 0 4$ , $x _ { 3 } = - 9 . 7 8$ (d) (c) $\begin{array} { l } { { x _ { 1 } = 0 . 0 9 2 8 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 5 6 , x _ { 4 } = 0 . 0 4 6 8 } } \\ { { \nonumber } } \\ { { x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } } \end{array}$

15. Gaussian elimination with partial pivoting and three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 7 8$ , $x _ { 2 } = 0 . 0 1 2 7$ , $x _ { 3 } = - 0 . 0 2 0 4$ , $x _ { 4 } = - 1 . 1 6$ (d) $x _ { 1 } = 0 . 8 4 5$ , $x _ { 2 } = - 3 . 3 7$ , $x _ { 3 } = 0 . 1 8 \mathrm { { 2 } }$ , $x _ { 4 } = 5 . 0 7$

16. Gaussian elimination with partial pivoting and three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 9$ , $x _ { 3 } = - 1 . 9 8$

$$
\begin{array} { l } { { x _ { 1 } = 0 . 0 9 2 7 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 6 2 , x _ { 4 } = 0 . 0 4 6 5 } } \\ { { \nonumber } } \\ { { x _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5 } } \end{array}
$$

17. Gaussian elimination with scaled partial pivoting and three-digit chopping arithmetic gives the following results.

$$
\begin{array} { l } { { = 1 0 . 0 , x _ { 2 } = 1 . 0 0 } } \\ { { = - 0 . 1 6 3 , x _ { 2 } = 9 . 9 8 , x _ { 3 } = 0 . 1 4 2 } } \\ { { = 0 . 1 7 1 , x _ { 2 } = 0 . 0 1 0 2 , x _ { 3 } = - 0 . 0 2 1 7 , x _ { 4 } = - 1 . 2 7 } } \\ { { = 0 . 6 8 7 , x _ { 2 } = - 2 . 6 6 , x _ { 3 } = 0 . 1 1 7 , x _ { 4 } = 3 . 5 9 } } \end{array}
$$

18. Gaussian elimination with scaled partial pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$   
(b) $x _ { 1 } = 0 . 9 9 3$ , $x _ { 2 } = 0 . 5 0 0$ , $x _ { 3 } = - 1 . 0 0$   
(c) $\begin{array} { l } { { x _ { 1 } = 0 . 0 9 3 0 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 5 9 , x _ { 4 } = 0 . 0 4 6 \tilde { \iota } } } \\ { { \phantom { x _ { 1 } = } } } \\ { { x - 1 = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } } \end{array}$   
(d)

19. Gaussian elimination with scaled partial pivoting and three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 8 0$ , $x _ { 2 } = 0 . 0 1 2 8$ , $x _ { 3 } = - 0 . 0 2 0 0$ , $x _ { 4 } = - 1 . 1 3$ (d) $x _ { 1 } = 0 . 7 8 3$ , $x _ { 2 } = - 3 . 1 2$ , $x _ { 3 } = 0 . 1 4 7$ , $x _ { 4 } = 4 . 5 3$

20. Gaussian elimination with scaled partial pivoting and three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 . 0 3$ , $x _ { 2 } = 0 . 5 0 2$ , $x _ { 3 } = - 1 . 0 1$ (c) $x _ { 1 } = 0 . 0 9 2 7 , x _ { 2 } = - 0 . 0 6 3 0 , x _ { 3 } = - 0 . 0 3 6 0 , x _ { 4 } = 0 . 0 4 6 7$ (d) $x _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5$

21. Using Algorithm 6.1 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 3 3$ , $x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 1 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $c _ { 1 } = 0 . 1 7 6 8 2 5 2 9 5 8 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 1 3 , x _ { 3 } = - 0$ $x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 1 3 , x _ { 3 } = - 0 . 0 2 0 6 5 4 0 5 0 3 , x _ { 4 } =$ −1.182608714   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 4 2 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 7 2 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 5 1 , x _ { }$ $x _ { 4 } = 4 . 5 5 7 0 0 2 5 2 1$

22. Using Algorithm 6.1 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 3 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 1 , x _ { 3 } = - 1 . 0 0 0 0 0 0 3 0 6$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 6 7 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 2 6 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 7 , x _ { 4 } = 0 . 0 4 6 7 0 9 4 3 3 9 2 6 , x _ { 5 } = - 0 . 0 3 6 3 5 2 2 6 7 9 4 9 4 6 7 0 .$ 801939

(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 , x _ { 5 } = - 4 . 7 5 6 9 6 7 5 9 7 9 9 .$

23. Using Algorithm 6.2 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2$   
(c) $s _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 5 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 9 , x _ { 3 } = - ($ 0.0206540502, x4 = −1.182608696   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 6 3 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 8 0 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 8 0 , x _ { 4 } = 4 . 5 5 7 0 0 2 5 1$

24. Using Algorithm 6.2 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 3 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 1 , x _ { 3 } = - 1 . 0 0 0 0 0 0 3 0 6$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 4 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 1 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 4 , x _ { 4 } =$ 0.04670801938   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 6 7 5 9 .$

25. Using Algorithm 6.3 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $s _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 7 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 9 , x _ { 3 } = - 0$ 0.0206540501, $x _ { 4 } = - 1 . 1 8 2 6 0 8 6 9 3$   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 4 2$ , $x _ { 2 } = - 3 . 1 2 5 4 1 3 6 7 2 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 5 2 , x _ { 4 } =$ $x _ { 4 } = 4 . 0 5 5 7 0 0 2 5 2$

26. Using Algorithm 6.3 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 0 , x _ { 3 } = - 1 . 0 0 0 0 0 0 0 0$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 5 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 1 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 4 ,$ $x _ { 4 } = 0 . 0 4 6 7 0 8 0 1 9 3 8$   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 5 6 , x _ { 5 } = - 4 . 7 5 7 7 3 8 7 7 7 9 9 9 .$

27. Using Gaussian elimination with complete pivoting gives:

(a) $x _ { 1 } = 9 . 9 8 , x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 7 2 4 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 0 9 5 2$ (c) $\mathfrak { c } _ { 1 } = 0 . 1 6 1 , x _ { 2 } = 0 . 0 1 2 5 , x _ { 3 } = - 0 . 0 2 3 2 , x _ { 4 } = - 1$ .42 (d) $x _ { 1 } = 0 . 7 1 9 , x _ { 2 } = - 2 . 8 6 , x _ { 3 } = 0 . 1 4 6 , x _ { 4 } = 4 . 0 0$

28. Gaussian elimination with complete pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0 , x _ { 2 } = 9 . 9 8$ (b) $x _ { 1 } = 0 . 9 8 2 , x _ { 2 } = 0 . 5 0 0 , x _ { 3 } = - 0 . 9 9 4$ (c) $x _ { 1 } = 0 . 0 9 3 3 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 6 0 , 0 . 0 4 6 4$ 4 (d) $x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 5$

29. Using Gaussian elimination with complete pivoting and three-digit rounding arithmetic gives:

(a) $x _ { 1 } = 1 0 . 0 , x _ { 2 } = 1 . 0 0$

$$
\begin{array} { l } { x _ { 1 } = 0 . 0 0 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 1 4 3 } \\ { x _ { 1 } = 0 . 1 7 9 , x _ { 2 } = 0 . 0 1 2 7 , x _ { 3 } = - 0 . 0 2 0 3 , x _ { 4 } = - 1 . 1 5 } \\ { x _ { 1 } = 0 . 8 7 4 , x _ { 2 } = - 3 . 4 9 , x _ { 3 } = 0 . 1 9 2 , x _ { 4 } = 5 . 3 3 } \end{array}
$$

30. Gaussian elimination with complete pivoting and three-digit rounding gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$   
(b) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$   
(c) $x _ { 1 } = 0 . 0 9 2 6$ $; x _ { 2 } = - 0 . 0 6 \div 2 9 , x _ { 3 } = - 0 . 0 3 6 1 , x _ { 4 } = 0 . 0 4 6 6$   
(d) $x _ { 1 } = 1 . 3 3$ , $x _ { 2 } = - 4 . 6 8$ , $x _ { 3 } = - 4 . 0 6$ , $x _ { 4 } = - 1 . 6 5$

$^ { * } 3 1$ . The only system which does not require row interchanges is (a), where $\alpha = 6$

$^ { * } 3 2$ . Change Algorithm 6.2 as follows:

Add to STEP 1.

$$
N C O L ( i ) = i
$$

Replace STEP 3 with the following.

Let $p$ and $q$ be the smallest integers with $i \le p$ , $q \leq n$ and

$$
\begin{array} { r } { | a ( N R O W ( p ) , N C O L ( q ) ) | = \operatorname* { m a x } _ { i \leq k , j \leq n } | a ( N R O W ( k ) , N C O L ( j ) ) | . } \end{array}
$$

Add to STEP 4.

$$
A ( N R O W ( p ) , N C O L ( q ) ) = 0
$$

Add to STEP 5.

If $N C O L ( q ) \neq N C O L ( i )$ then set

Replace STEP 7 with the following.

Set

$$
m ( N R O W ( j ) , N C O L ( i ) ) = \frac { a ( N R O W ( j ) , N C O L ( i ) ) } { a ( N R O W ( i ) , N C O L ( i ) ) } .
$$

Replace in STEP 8:

$$
m ( N R O W ( j ) , i ) \mathrm { b y } m ( N R O W ( j ) , N C O L ( i ) )
$$

Replace in STEP 9:

$$
a ( N R O W ( n ) , n ) \mathrm { b y } a ( N R O W ( n ) , N C O L ( n ) )
$$

Replace STEP 10 with the following.

Set

$$
X ( N C O L ( n ) ) = { \frac { a ( N R O W ( n ) , n + 1 ) } { a ( N R O W ( n ) , N C O L ( n ) ) } } .
$$

Replace STEP 11 with the following.

Set

$$
X ( N C O L ( i ) ) = \frac { a ( N R O W ( i ) , n + 1 ) - \sum _ { j = i + 1 } ^ { n } a ( N R O W ( i ) , N C O L ( j ) ) \cdot X ( N C O L ( j ) ) } { A ( N R O W ( i ) , N C O L ( i ) ) } .
$$

Replace STEP 12 with the following.

33. Using the Complete Pivoting Algorithm in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $\begin{array} { r } { \mathfrak { c } _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 4 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 8 7 , x _ { 3 } = - } \end{array}$ $\begin{array} { r } { x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 8 7 , x _ { 3 } = - 0 . 0 2 0 6 5 4 0 5 0 1 5 , } \end{array}$ $x _ { 4 } = - 1 . 1 8 2 6 0 8 6 9 7$   
(d) $x _ { 1 } = 0 . 1 7 8 8 3 9 3 7 8 4 0 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 6 9 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 7 1 , x _ { 4 } = 4 . 5 5 7 0 0 2 5 1 6$

34. Using the Complete Pivoting Algorithm in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 1 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 0 0 , x _ { 3 } = - 1 . 0 0 0 0 0 0 0 1$   
(c) $\begin{array} { r } { \mathfrak { c } _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 1 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 0 , x _ { 3 } = } \end{array}$ $1 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 0 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 7 .$ , $x _ { 4 } = 0 . 0 4 6 7 0 8 0 1 9 3 7$   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 7 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 0 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 8 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 , x _ { 5 } = - 4 . 0 9 6 9 3 7 8 7 8 7 9 .$

# Exercise Set 6.3, page 390

1. (a) $\left[ - 1 8 \right]$ (b) "00# (c) 


4
3
7

 (d) -−4 8 −16

2. (a) $\begin{array} { r } { \left[ \begin{array} { l } { 3 } \\ { 0 } \end{array} \right] } \end{array}$ (b) "12# $* ( \mathrm { c } ) \quad \left[ \begin{array} { c } { { 9 } } \\ { { - 1 } } \\ { { 1 4 } } \end{array} \right]$ (d) -10 −9 −4

3. (a) $\left[ { \begin{array} { r r } { - 4 } & { 1 0 } \\ { 1 } & { 1 5 } \end{array} } \right]$ (b) " $\begin{array} { r } { \left[ \begin{array} { r r r } { 1 1 } & { 4 } & { - 8 } \\ { 6 } & { 1 3 } & { - 1 2 } \end{array} \right] \quad \mathrm { ( c ) } \quad \left[ \begin{array} { r r r } { - 1 } & { 5 } & { - 3 } \\ { 3 } & { 4 } & { - 1 1 } \\ { - 6 } & { - 7 } & { - 4 } \end{array} \right] \quad \mathrm { ( d ) } \quad \left[ \begin{array} { r r } { - 2 } & { 1 } \\ { - 1 4 } & { 7 } \\ { 6 } & { 1 } \end{array} \right] } \end{array}$

$$
\left[ { \begin{array} { r r } { - 1 9 } & { 1 6 } \\ { - 1 5 } & { 6 } \end{array} } \right] \qquad { \begin{array} { r r } { * ( \mathrm { b } ) } & { \left[ { \begin{array} { r r } { - 1 1 } & { 8 } & { 3 } \\ { - 1 6 } & { 1 2 } & { 2 } \end{array} } \right] } \end{array} } \qquad ( \mathrm { c } ) \left[ { \begin{array} { r r } { 5 } & { - 1 6 } & { 1 5 } \\ { - 1 4 } & { 2 4 } & { - 1 8 } \\ { - 2 3 } & { 1 4 } & { - 1 } \end{array} } \right] ( \mathrm { d } )  &  \left[ { \begin{array} { r r } { - 7 } & { 7 } \\ { - 1 } & { - 9 } \\ { 1 8 } & { - 2 5 } \end{array} } \right]
$$

5. Determine if the matrices are nonsingular, and if so, find the inverse.

(a) The matrix is singular.

$$
* ( \mathrm { b } ) \quad \left[ \begin{array} { r r r } { { - \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \\ { { \frac { 5 } { 8 } } } & { { - \frac { 1 } { 8 } } } & { { - \frac { 1 } { 8 } } } \\ { { \frac { 1 } { 8 } } } & { { - \frac { 5 } { 8 } } } & { { \frac { 3 } { 8 } } } \end{array} \right]
$$

(c) The matrix is singular.

$$
\left[ { \begin{array} { r r r r } { { \frac { 1 } { 4 } } } & { 0 } & { 0 } & { 0 } \\ { - { \frac { 3 } { 1 4 } } } & { { \frac { 1 } { 7 } } } & { 0 } & { 0 } \\ { { \frac { 3 } { 2 8 } } } & { - { \frac { 1 1 } { 7 } } } & { 1 } & { 0 } \\ { - { \frac { 1 } { 2 } } } & { 1 } & { - 1 } & { 1 } \end{array} } \right]
$$

6. Determine if the matrices are nonsingular, and if so, find the inverse.

(a)

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 0 } & { 1 } & { 2 } \\ { - 1 } & { 4 } & { 3 } \end{array} \right] } ^ { - 1 } = { \left[ \begin{array} { l l l } { { \frac { 1 } { 2 } } } & { 1 } & { - { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 5 } } } & { - { \frac { 1 } { 5 } } } & { { \frac { 1 } { 5 } } } \\ { - { \frac { 1 } { 1 0 } } } & { { \frac { 3 } { 5 } } } & { - { \frac { 1 } { 1 0 } } } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { 0 } \\ { 2 } & { 1 } & { - 1 } \\ { 3 } & { 1 } & { 1 } \end{array} \right] } ^ { - 1 } = { \left[ \begin{array} { l l l } { - { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \\ { { \frac { 5 } { 8 } } } & { - { \frac { 1 } { 8 } } } & { - { \frac { 1 } { 8 } } } \\ { { \frac { 1 } { 8 } } } & { - { \frac { 5 } { 8 } } } & { { \frac { 3 } { 8 } } } \end{array} \right] }
$$

(c) The matrix is singular.

$$
\left[ { \begin{array} { c c c c } { 2 } & { 0 } & { 0 } & { 2 } \\ { 1 } & { 1 } & { 0 } & { 2 } \\ { 2 } & { - 1 } & { 3 } & { 1 } \\ { 3 } & { - 1 } & { 4 } & { 3 } \end{array} } \right] ^ { - 1 } = \left[ { \begin{array} { c c c c } { 1 } & { 0 } & { 1 } & { - 1 } \\ { - 1 } & { { \frac { 5 } { 3 } } } & { { \frac { 5 } { 3 } } } & { - 1 } \\ { - 1 } & { { \frac { 2 } { 3 } } } & { { \frac { 2 } { 3 } } } & { 0 } \\ { 0 } & { - { \frac { 1 } { 3 } } } & { - { \frac { 4 } { 3 } } } & { 1 } \end{array} } \right]
$$

7. The solutions to the linear systems obtained in parts (a) and (b) are, from left to right,

$$
3 , - 6 , - 2 , - 1 \quad { \mathrm { a n d } } \quad 1 , 1 , 1 , 1 .
$$

8. The solutions to the linear systems obtained in parts (a) and (b) are, from left to right and top to bottom:

$$
- \frac { 2 } { 7 } , - \frac { 1 3 } { 1 4 } , - \frac { 3 } { 1 4 } ; \quad \frac { 1 7 } { 7 } , - \frac { 1 9 } { 1 4 } , - \frac { 4 1 } { 1 4 } ; \quad 1 , 1 , 1 \quad \mathrm { a n d } \quad \left. - \frac { 1 } { 7 } , \frac { 2 } { 7 } , \frac { 1 } { 7 } . \right.
$$

9. (a) Suppose $\ddot { A }$ and $\hat { A }$ are both inverses of $A$ . Then $A { \tilde { A } } = { \tilde { A } } A = I$ and $A { \hat { A } } = { \hat { A } } A = I$ . Thus,

$$
\tilde { A } = \tilde { A } I = \tilde { A } ( A \hat { A } ) = ( \tilde { A } A ) \hat { A } = I \hat { A } = \hat { A } .
$$

(b) We have

$$
( A B ) ( B ^ { - 1 } A ^ { - 1 } ) = A ( B B ^ { - 1 } ) A ^ { - 1 } = A I A ^ { - 1 } = A A ^ { - 1 } = I
$$

and

$$
( B ^ { - 1 } A ^ { - 1 } ) ( A B ) = B ^ { - 1 } ( A ^ { - 1 } A ) B = B ^ { - 1 } I B = B ^ { - 1 } B = I .
$$

So $( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 }$ since the inverse is unique.

(c) Since $A ^ { - 1 } A = A A ^ { - 1 } = I$ , it follows that $A ^ { - 1 }$ is nonsingular. Since the inverse is unique, we have $( A ^ { - 1 } ) ^ { - 1 } = A$ .

10. (a) Not true. Let

$$
A = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } \quad { \mathrm { a n d } } \quad B = { \left[ \begin{array} { l l } { 1 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] } . \quad { \mathrm { T h e n } } \quad A B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] }
$$

is not symmetric.

(b) True. Let $A$ be a nonsingular symmetric matrix. By Theorem 6.13 (d), $\left( A ^ { - 1 } \right) ^ { t } = \left( A ^ { t } \right) ^ { - 1 }$ . Thus, $\left( A ^ { - 1 } \right) ^ { t } = \left( A ^ { t } \right) ^ { - 1 } = A ^ { - 1 }$ and $A ^ { - 1 }$ is symmetric.

(c) Not true. Use the matrices $A$ and $B$ from part (a).

11. (a) If $C = A B$ , where $A$ and $B$ are lower triangular, then $a _ { i k } = 0$ if $k > i$ and $b _ { k j } = 0$ if $k < j$ . Thus

$$
c _ { i j } = \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } = \sum _ { k = j } ^ { i } a _ { i k } b _ { k j } ,
$$

which will have the sum zero unless $j \le i$ . Hence $C$ is lower triangular.

(b) We have $a _ { i k } = 0$ if $k < i$ and $b _ { k j } = 0$ if $k > j$ . The steps are similar to those in part (a). (c) Let $L$ be a nonsingular lower triangular matrix. To obtain the $i$ th column of $L ^ { - 1 }$ , solve $n$ linear systems of the form

$$
\begin{array} { r l } & { \begin{array} { c c c c c c c c } { l _ { 1 1 } } & { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } \\ { l _ { 2 1 } } & { l _ { 2 2 } } & & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \vdots } \\ { \vdots } & { \vdots } & { \ddots } & & & & & { \vdots } \\ { l _ { i 1 } } & { l _ { i 2 } } & { \cdots } & & & & & { \vdots } \\ { l _ { i 1 } } & { l _ { i 2 } } & { \cdots } & { l _ { i i } } & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \ddots } & & \\ { l _ { n 1 } } & { l _ { n 2 } } & { \cdots } & { \cdots } & { \cdots } & { l _ { n n } } \end{array} \} \begin{array} { c } { [ x _ { 1 } ] } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \end{array} \} = [ \begin{array} { c } { [ 0 ] } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \\ { 0 } \end{array} ] , } \\ &  \begin{array} { c } { \vdots } \\ { \vdots } \\ { \vdots } \\ { l _ { n 1 } } \end{array} \begin{array} { c } { [ \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { r } \end{array} } \end{array} ] } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} ] } \\  [ \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { r } \end{array} } \end{array} } \\ { \vdots } \\ { \vdots } \\ { \ddots } \\ { 0 } \end{array} ] } \end{array} \end{array} \end{array}
$$

where the 1 appears in the $i$ th position to obtain the $i$ th column of $L ^ { - 1 }$ .

$^ *$ 12. (a) Following the steps of Algorithm 6.1 with $m - 1$ additional columns in the augmented matrix gives the following:

Reduction Steps 1–6: Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + ( m + n - i ) \right\} = \displaystyle \sum _ { i = 1 } ^ { n - 1 } \left\{ n ( m + n + 1 ) - ( m + 2 n + 1 ) i + i ^ { 2 } \right\} } } \\ { { = \displaystyle \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n + \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 3 } n } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ m + n - i \right\} = \sum _ { i = 1 } ^ { n - 1 } \left\{ n ( m + n ) - ( m + 2 n ) i + i ^ { 2 } \right\} } } \\ { { = \displaystyle \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n + \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 2 } n ^ { 2 } + \frac { 1 } { 6 } n } } \end{array}
$$

Backward Substitution Steps 8–9:

Multiplications/Divisions:

$$
m \left[ 1 + \sum _ { i = 1 } ^ { n - 1 } ( n - i + 1 ) \right] = m \left[ 1 + \frac { n ( n + 1 ) } { 2 } - 1 \right] = \frac 1 2 m n ^ { 2 } + \frac 1 2 m n
$$

Additions/Subtractions:

$$
m \left[ \sum _ { i = 1 } ^ { n - 1 } ( n - i ) \right] = \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n
$$

Total:

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 3 } } n } \end{array} }$ Additions/Subtractions: $\textstyle { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n ^ { 2 } - m n + { \frac { 1 } { 6 } } n$

(b) For the reduction phase: Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle { \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \left\{ 1 + \sum _ { k = i + 1 } ^ { n + m } 1 \right\} = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } ( m + n + 1 - i ) = \sum _ { i = 1 } ^ { n } \{ ( n - 1 ) ( m + n + 1 ) - ( n - 1 ) i \} } } } \\ { { = \displaystyle { \frac { 1 } { 2 } { n } ^ { 3 } + m n ^ { 2 } - m n - \frac { 1 } { 2 } n } } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } \sum _ { k = i + 1 } ^ { n + m } 1 = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } ( n + m - i ) = \sum _ { i = 1 } ^ { n } \{ ( n - 1 ) ( m + n ) - ( n - 1 ) i \} } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } n ^ { 3 } + m n ^ { 2 } - m n - n ^ { 2 } + \frac { 1 } { 2 } n } } \end{array}
$$

Backward Substitution Steps:

Multiplications/Divisions:

$$
\sum _ { k = 1 } ^ { m } \sum _ { i = 1 } ^ { n } 1 = m n
$$

Additions/Subtractions: none

Totals:

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n } \end{array} }$ Additions/Subtractions: $\textstyle { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - n ^ { 2 } - m n + { \frac { 1 } { 2 } } n$

(c) When $m = n$ we have the following:

Gaussian Elimination

Multiplications/Divisions: $\textstyle { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 3 } } n = { \frac { 4 } { 3 } } n ^ { 3 } - { \frac { 1 } { 3 } } n$ Additions/Subtractions: ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } + m n ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } n ^ { 2 } - m n + { \textstyle { \frac { 1 } { 6 } } } n = { \textstyle { \frac { 4 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 3 } { 2 } } } n ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } n$

Gauss-Jordan Elimination

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n = { \frac { 3 } { 2 } } n ^ { 3 } - { \frac { 1 } { 2 } } n } \end{array} }$ Additions/Subtractions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - n ^ { 2 } - m n + { \frac { 1 } { 2 } } n = { \frac { 3 } { 2 } } n ^ { 3 } - 2 n ^ { 2 } + { \frac { 1 } { 2 } } n } \end{array} }$

(d) To find the inverse of the $n \times n$ matrix $A$

INPUT $n \times n$ matrix $A = \left( a _ { i j } \right)$ .

OUTPUT $n \times n$ matrix $B = A ^ { - 1 }$

Step 1 Initialize the $n \times n$ matrix $B = ( b _ { i j } )$ to

$$
b _ { i j } = { \left\{ \begin{array} { l l } { 0 } & { i \neq j , } \\ { 1 } & { i = j } \end{array} \right. }
$$

Step 2 For $i = 1 , \ldots , n - 1$ do Steps 3, 4, and 5.

Step 3 Let $p$ be the smallest integer with $i \le p \le n$ and $a _ { p , i } \neq 0$ . If no integer $p$ can be found then OUTPUT ( $A$ is singular’); STOP.

Step 4 If $p \neq i$ then perform $( E _ { p } )  ( E _ { i } )$

Step 5 For $j = i + 1 , \ldots , n$ do Steps 6 through 9.

Step 6 Set $m _ { j i } = a _ { j i } / a _ { i i }$ .   
Step 7 For $k = i + 1 , \ldots , n$ set $a _ { j k } = a _ { j k } - m _ { j i } a _ { i k }$ ; $a _ { i j } = 0$   
Step 8 For $k = 1 , \ldots , i - 1$ set $b _ { j k } = b _ { j k } - m _ { j i } b _ { i k }$ .   
Step 9 Set $b _ { j i } = - m _ { j i }$ .

Step 10 If $a _ { n n } = 0$ then OUTPUT ( $A$ is singular’);

STOP.

Step 11 For $j = 1 , \dotsc , n$ do Steps 12, 13 and 14.

Step 12 Set $b _ { n j } = b _ { n j } / a _ { n n }$ . Step 13 For set $i = n - 1 , \dotsc , j$ $\begin{array} { r } { b _ { i j } = \left( b _ { i j } - \sum _ { k = i + 1 } ^ { n } a _ { i k } b _ { k j } \right) / a _ { i i } } \end{array}$ Step 14 set $\begin{array} { r } { b _ { i j } = - \left\lfloor \sum _ { k = i + 1 } ^ { n } a _ { i k } b _ { k j } \right\rfloor / a _ { i i } } \end{array}$ $i = j - 1 , \ldots , 1$ .

Step 15 OUTPUT ( $B$ ); STOP.

Reduction Steps 2–9:

Multiplications/Divisions:

$$
\sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 + \sum _ { k = 1 } ^ { i - 1 } 1 \right\} = \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + n - i + i - 1 \right\} = { \frac { n ^ { 2 } ( n - 1 ) } { 2 } }
$$

Additions/Subtractions:

$$
\sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ \sum _ { k = i + 1 } ^ { n } 1 + \sum _ { k = 1 } ^ { i - 1 } 1 \right\} = \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \{ n - i + i - 1 \} = { \frac { n ( n - 1 ) ^ { 2 } } { 2 } }
$$

Backward Substitution Steps 11–14:

Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n } \left\{ 1 + \sum _ { i = j } ^ { n - 1 } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 \right\} + \sum _ { i = 1 } ^ { j - 1 } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 \right\} \right\} = \sum _ { j = 1 } ^ { n } \left\{ 1 + \sum _ { i = j } ^ { n - 1 } ( n + 1 - i ) + \sum _ { i = 1 } ^ { j - 1 } ( n + 1 - i ) \right\} = \displaystyle \sum _ { i = 1 } ^ { j - 1 } ( n + 1 - i ) ^ { i } = \sum _ { j = 1 } ^ { n } ( n - 1 - i ) ^ { j } } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \left[ 1 + \sum _ { i = 1 } ^ { n - 1 } ( n + 1 - i ) \right] } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \frac { n ( n + 1 ) } { 2 } = \frac { n ^ { 2 } ( n + 1 ) } { 2 } = \frac { n ^ { 2 } ( n + 1 ) } { 2 } = \frac { ( n + 1 ) } { 2 } } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 1 } ^ { n } \left\{ \sum _ { i = j } ^ { n - 1 } ( 1 + n - i - 1 ) + \sum _ { i = 1 } ^ { j - 1 } ( n - i - 1 ) \right\} = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n - 1 } ( n - i ) - j + 1 } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \left[ \frac { n ( n - 1 ) } { 2 } + 1 - j \right] } } \\ { { = \displaystyle \frac { n ^ { 2 } ( n - 1 ) } { 2 } + n - \frac { n ( n + 1 ) } { 2 } } } \\ { { = \displaystyle \frac { n ^ { 3 } } { 2 } - n ^ { 2 } + \frac { 1 } { 2 } n } } \end{array}
$$

Totals:

Multiplications/Divisions: ${ \frac { n ^ { 2 } ( n - 1 ) } { 2 } } + { \frac { n ^ { 2 } ( n + 1 ) } { 2 } } = n ^ { 3 }$ Additions/Subtractions: ${ \frac { n ( n - 1 ) ^ { 2 } } { 2 } } + { \frac { n ^ { 3 } } { 2 } } - n ^ { 2 } + { \frac { 1 } { 2 } } n = n ^ { 3 } - 2 n ^ { 2 } + n$

(e) Let $\left\lfloor A ^ { - 1 } \right\rfloor _ { i , j }$ denote the entries of $A ^ { - 1 }$ , for $1 \leq i , j \leq n$ . For each $i = 1 , \ldots , n$ , we have

$$
x _ { i } = \sum _ { j = 1 } ^ { n } [ A ^ { - 1 } ] _ { i , j } b _ { j } .
$$

This requires $_ { n }$ multiplications and $n - 1$ additions for each $i$ . The total number of computations is:

$n ^ { 2 }$ Multiplications/Divisions and ${ n ^ { 2 } } - n$ Additions/Subtractions.

(f) For $m$ linear systems, we have $m n ^ { 2 }$ Multiplications/Divisions and $m ( n ^ { 2 } \mathrm { ~ - ~ } n )$ Additions/Subtractions.

(g)

<table><tr><td colspan="3">Gaussian Elimination (part a)</td><td colspan="2">Inverting A and forming A-1b</td></tr><tr><td>n</td><td>Multiplications Divisions</td><td>Additions Subtractions</td><td>Multiplications Divisions</td><td>Additions Subtractions</td></tr><tr><td>3</td><td>9m+8</td><td>6m+5</td><td>9m+27</td><td>6m+12</td></tr><tr><td>10</td><td>100m + 330</td><td>90m+285</td><td>100m +1000</td><td>90m+810</td></tr><tr><td>50</td><td>2500m +41650</td><td>2450m + 40425</td><td>2500m +125000</td><td>2450m +120050</td></tr><tr><td>100</td><td>10000m +333300</td><td>9900m + 328350</td><td>10000m+1000000</td><td>9900m + 980100</td></tr></table>

13. The answers are the same as those in Exercise 1.

\*14. No, since the products $A _ { i j } B _ { j k }$ , for $1 \leq i$ , $j$ , $k \leq 2$ , cannot be formed.

(c) The following are necessary and sufficient conditions:

(i) The number of columns of $A$ is the same as the number of rows of $B$ . (ii) The number of vertical lines of $A$ equals the number of horizontal lines of $B$ . (iii) The placement of the vertical lines of $A$ is identical to placement of the horizontal lines of $B$ .

$$
A ^ { 2 } = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \\ { { \frac { 1 } { 6 } } } & { 0 } & { 0 } \end{array} \right] } , \quad A ^ { 3 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } , \quad A ^ { 4 } = A , \quad A ^ { 5 } = A ^ { 2 } , \quad A ^ { 6 } = I , \ldots A
$$

(b)

<table><tr><td></td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td></tr><tr><td>Age 1</td><td>6000</td><td>36000</td><td>12000</td><td>6000</td></tr><tr><td>Age 2</td><td>6000</td><td>3000</td><td>18000</td><td>6000</td></tr><tr><td>Age 3</td><td>6000</td><td>2000</td><td>1000</td><td>6000</td></tr></table>

(c) We have

$$
A ^ { - 1 } = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \\ { { \frac { 1 } { 6 } } } & { 0 } & { 0 } \end{array} \right] } ~ .
$$

The $i , j$ -entry is the number of beetles of age $i$ necessary to produce one beetle of age $j$ .

16. (a) For each $k = 1 , 2 , \ldots , m$ , the number $a _ { i k }$ represents the total number of plants of type $v _ { i }$ eaten by herbivores in the species $h _ { k }$ . The number of herbivores of types $h _ { k }$ eaten by species $c _ { j }$ is $b _ { k j }$ . Thus, the total number of plants of type $v _ { i }$ ending up in species $c _ { j }$ is $a _ { i 1 } b _ { 1 j } + a _ { i 2 } b _ { 2 j } + . . . + a _ { i m } b _ { m j } = ( A B ) _ { i j }$ .

(b) We first assume $n = m = k$ so that the matrices will have inverses. Let $x _ { 1 } , . . . , x _ { n }$ represent the vegetations of type $v _ { 1 } , . . . , v _ { n }$ , l ${ \mathfrak { x } } y _ { 1 } , . . . , y _ { n }$ represent the number of herbivores of species $h _ { 1 } , . . . , h _ { n }$ , and let $z _ { 1 } , . . . , z _ { n }$ represent the number of carnivores of species $c _ { 1 } , . . . , c _ { n }$ . If

$$
{ \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] } = A { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } , \quad { \mathrm { t h e n } } \quad \quad { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } = A ^ { - 1 } \left[ { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} } \right] .
$$

Thus, $( A ^ { - 1 } ) _ { i , j }$ represents the amount of type $v _ { j }$ plants eaten by a herbivore of species $h _ { i }$ .

Similarly, if

$$
{ \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } = B { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } , \quad { \mathrm { t h e n } } \quad { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } = B ^ { - 1 } { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } .
$$

Thus, $\left( B ^ { - 1 } \right) _ { i , j }$ represents the number of herbivores of species $h _ { j }$ eaten by a carnivore of species $c _ { i }$ . If $x = A y$ and $y = B z$ , then $x = A B z$ and $z = ( A B ) ^ { - 1 } x$ . But, $y = A ^ { - 1 } x$ and $z = B ^ { - 1 } y$ , so $z = B ^ { - 1 } A ^ { - 1 } x$ .

17. (a) We have

$$
\left[ { \begin{array} { r r r r } { 7 } & { 4 } & { 4 } & { 0 } \\ { - 6 } & { - 3 } & { - 6 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] \left[ { \begin{array} { r r r r } { 2 ( x _ { 0 } - x _ { 1 } ) + \alpha _ { 0 } + \alpha _ { 1 } } \\ { 3 ( x _ { 1 } - x _ { 0 } ) - \alpha _ { 1 } - 2 \alpha _ { 0 } } \\ { \alpha _ { 0 } } \\ { x _ { 0 } } \end{array} } \right] = \left[ { \begin{array} { r r r r } { 2 ( x _ { 0 } - x _ { 1 } ) + 3 \alpha _ { 0 } + 3 \alpha _ { 1 } } \\ { 3 ( x _ { 1 } - x _ { 0 } ) - 3 \alpha _ { 1 } - 6 \alpha _ { 0 } } \\ { 3 \alpha _ { 0 } } \\ { x _ { 0 } } \end{array} } \right]
$$

$$
B = A ^ { - 1 } = { \left[ \begin{array} { l l l l } { - 1 } & { - { \frac { 4 } { 3 } } } & { - { \frac { 4 } { 3 } } } & { 0 } \\ { 2 } & { { \frac { 7 } { 3 } } } & { 2 } & { 0 } \\ { 0 } & { 0 } & { { \frac { 1 } { 3 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$^ *$ 18. (a) In component form:

$$
\begin{array} { r } { ( a _ { 1 1 } x _ { 1 } - b _ { 1 1 } y _ { 1 } + a _ { 1 2 } x _ { 2 } - b _ { 1 2 } y _ { 2 } ) + ( b _ { 1 1 } x _ { 1 } + a _ { 1 1 } y _ { 1 } + b _ { 1 2 } x _ { 2 } + a _ { 1 2 } y _ { 2 } ) i = c _ { 1 } + i d _ { 1 } , } \\ { ( a _ { 2 1 } x _ { 1 } - b _ { 2 1 } y _ { 1 } + a _ { 2 2 } x _ { 2 } - b _ { 2 2 } y _ { 2 } ) + ( b _ { 2 1 } x _ { 1 } + a _ { 2 1 } y _ { 1 } + b _ { 2 2 } x _ { 2 } + a _ { 2 2 } y _ { 2 } ) i = c _ { 2 } + i d _ { 2 } , } \end{array}
$$

which yields

$$
\begin{array} { r l } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } - b _ { 1 1 } y _ { 1 } - b _ { 1 2 } y _ { 2 } = c _ { 1 } , } \\ & { b _ { 1 1 } x _ { 1 } + b _ { 1 2 } x _ { 2 } + a _ { 1 1 } y _ { 1 } + a _ { 1 2 } y _ { 2 } = d _ { 1 } , } \\ & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } - b _ { 2 1 } y _ { 1 } - b _ { 2 2 } y _ { 2 } = c _ { 2 } , } \\ & { b _ { 2 1 } x _ { 1 } + b _ { 2 2 } x _ { 2 } + a _ { 2 1 } y _ { 1 } + a _ { 2 2 } y _ { 2 } = d _ { 2 } . } \end{array}
$$

(b) The system

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 3 } & { 2 } & { - 2 } \\ { - 2 } & { 2 } & { 1 } & { 3 } \\ { 2 } & { 4 } & { - 1 } & { - 3 } \\ { 1 } & { 3 } & { 2 } & { 4 } \\ & & & \end{array} \right] } \quad { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l } { 5 } \\ { 2 } \\ { 4 } \\ { - 1 } \\ { } \end{array} \right] }
$$

has the solution $x _ { 1 } = - 1 . 2$ , $x _ { 2 } = 1$ , $y _ { 1 } = 0 . 6$ , and $y _ { 2 } = - 1$ .

# Exercise Set 6.4, page 399

1. The determinants of the matrices are:

\*(a) $^ { - 8 }$ (b) 14 (c) 0 (d) 3

2. The determinants of the matrices are:

(a) 8 $\mathrm { ( b ) } \ - 8$ (c) 0 (d) 0

3. The answers are the same as in Exercise 1.

4. The answers are the same as in Exercise 2.

$^ { * } 5$ . The matrix is singular when $\alpha = - \frac { 3 } { 2 }$ and when $\alpha = 2$

6. The matrix is singular when $\alpha = 6$ .

$^ { * } 7$ . The system has no solutions when $\alpha = - 5$

8. The system has no solutions when $\alpha = - 5$ .

$^ { * } 9$ . When $n = 2$ , $\operatorname* { d e t } A = a _ { 1 1 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 1 }$ requires 2 multiplications and 1 subtraction. Since

$$
2 ! \sum _ { k = 1 } ^ { 1 } { \frac { 1 } { k ! } } = 2 \quad { \mathrm { ~ a n d ~ } } 2 ! - 1 = 1 ,
$$

the formula holds for $n = 2$ . Assume the formula is true for $n = 2 , . . . , m$ , and let $A$ be an $( m + 1 ) \times ( m + 1 )$ matrix. Then

$$
\operatorname * { d e t } A = \sum _ { j = 1 } ^ { m + 1 } a _ { i j } A _ { i j } ,
$$

for any $i$ , where $1 \leq i \leq m + 1$ . To compute each $A _ { i j }$ requires

$$
m ! \sum _ { k = 1 } ^ { m - 1 } \frac { 1 } { k ! } \mathrm { m u l t i p l i c a t i o n s } \mathrm { a n d } m ! - 1 \mathrm { a d d i t i o n s / s u b t r a c t i o n s } .
$$

Thus, the number of multiplications for $\operatorname { d e t } A$ is

$$
( m + 1 ) \left[ m ! \sum _ { k = 1 } ^ { m - 1 } { \frac { 1 } { k ! } } \right] + ( m + 1 ) = ( m + 1 ) ! \left[ \sum _ { k = 1 } ^ { m - 1 } { \frac { 1 } { k ! } } + { \frac { 1 } { m ! } } \right] = ( m + 1 ) ! \sum _ { k = 1 } ^ { m } { \frac { 1 } { k ! } } ,
$$

and the number of additions/subtractions is

$$
( m + 1 ) \left[ m ! - 1 \right] + m = ( m + 1 ) ! - 1 .
$$

By the principle of mathematical induction, the formula is valid for any $n \geq 2$ .

10. Let

$$
A = \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] \quad \mathrm { a n d } \quad \tilde { A } = \left[ \begin{array} { l l l } { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] .
$$

Expanding along the third rows gives

$$
{ \begin{array} { r l } { \operatorname* { d e t } A = a _ { 3 1 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 2 } } & { a _ { 2 3 } } \end{array} \right] } - a _ { 3 2 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 3 } } \end{array} \right] } + a _ { 3 3 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 2 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } \end{array} \right] } } \\ { = a _ { 3 1 } { \left( a _ { 1 2 } a _ { 2 3 } - a _ { 1 3 } a _ { 2 2 } \right) } - a _ { 3 2 } { \left( a _ { 1 1 } a _ { 2 3 } - a _ { 1 3 } a _ { 2 1 } \right) } + a _ { 3 3 } { \left( a _ { 1 1 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 1 } \right) } } \end{array} }
$$

and

$$
\begin{array} { r l } & { \operatorname* { d e t } \tilde { A } = a _ { 3 1 } \operatorname* { d e t } \left[ \frac { a _ { 2 2 } } { a _ { 1 2 } } \quad a _ { 2 3 } \right] - a _ { 3 2 } \operatorname* { d e t } \left[ \frac { a _ { 2 1 } } { a _ { 1 1 } } \quad a _ { 2 3 } \right] + a _ { 3 3 } \operatorname* { d e t } \left[ \begin{array} { l l } { a _ { 2 1 } } & { a _ { 2 2 } } \\ { a _ { 1 1 } } & { a _ { 1 2 } } \end{array} \right] } \\ & { \qquad = a _ { 3 1 } ( a _ { 1 3 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 3 } ) - a _ { 3 2 } ( a _ { 1 3 } a _ { 2 1 } - a _ { 1 1 } a _ { 2 3 } ) + a _ { 3 3 } ( a _ { 1 2 } a _ { 2 1 } - a _ { 1 1 } a _ { 2 2 } ) = - \operatorname* { d e t } A . } \end{array}
$$

The other two cases are similar.

$^ *$ 11. The result follows from $\operatorname* { d e t } A B = \operatorname* { d e t } A \cdot \operatorname* { d e t } B$ and Theorem 6.17.

12. (a) The solution is $x _ { 1 } = 0$ , $x _ { 2 } = 1 0$ , and $x _ { 3 } = 2 6$ . (b) We have $D _ { 1 } = - 1$ , $D _ { 2 } = 3$ , $D _ { 3 } = 7$ , and $D = 0$ , and there are no solutions. (c) We have $D _ { 1 } = D _ { 2 } = D _ { 3 } = D = 0$ , and there are infinitely many solutions. (d) Cramer’s rule requires 39 Multiplications/Divisions and 20 Additions/Subtractions.

$^ *$ 13. (a) If $D _ { i }$ is the determinant of the matrix formed by replacing the $i$ th column of $A$ with b and if $D = \det A$ , then

$$
x _ { i } = D _ { i } / D , \mathrm { ~ f o r ~ } i = 1 , \ldots , n .
$$

(b) $( n + 1 ) ! \left( \sum _ { k = 1 } ^ { n - 1 } { \frac { 1 } { k ! } } \right) + n$ multiplications/divisions; $( n + 1 ) ! - n - 1$ additions/subtractions.

# Exercise Set 6.5, page 409

1. The solutions to the linear systems are as follows.

\*(a) $x _ { 1 } = - 3$ , $x _ { 2 } = 3$ , $x _ { 3 } = 1$ (b) $\begin{array} { r } { x _ { 1 } = \frac { 1 } { 2 } } \end{array}$ , $x _ { 2 } = - \frac { \mathsf { y } } { 2 }$ , $\begin{array} { r } { x _ { 3 } = \frac { 7 } { 2 } } \end{array}$

2. The solutions to the linear systems are as follows.

(a) $x _ { 1 } = 1 1 / 2 0$ , $x _ { 2 } = 3 / 1 0$ , x3 = 2 / 5 (b) $x _ { 1 } = 1 7 6$ , $x _ { 2 } = - 5 0$ , $x _ { 3 } = 2 4$

3. (a) $P = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }$ \* $( \mathrm { b } ) ~ P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }$ (c) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }$ (d) $P = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right] }$

4. (a) $P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { } & { } & { } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }$ (b) $P = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }$ (c) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] }$ (d) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }$

5. \*( ${ \mathrm { ~ a ) ~ } } L = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 1 . 5 } & { 1 } & { 0 } \\ { 1 . 5 } & { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } U = { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 1 } \\ { 0 } & { 4 . 5 } & { 7 . 5 } \\ { 0 } & { 0 } & { - 4 } \end{array} \right] }$ (b) $\begin{array}{c} { \begin{array} { r l } & { L = { \Biggl [ } { \mathrm { - } } 2 . 1 0 6 7 1 9 \qquad \ 0 \qquad 0 { \mathrm { } } { \mathrm { } } } \\ & { \left. 3 . 0 6 7 1 9 3 \qquad 1 . 1 9 7 7 5 6 \ 1 { \mathrm { } } ^ { \mathrm { } } \right] \ { \mathrm { a n d } } \ U = { \Biggl [ } { \begin{array} { c c c c } { 1 . 0 1 2 } & { - 2 . 1 3 2 } & { 3 . 1 0 4 } \\ { 0 } & { - 0 . 3 9 5 5 2 5 7 } & { - 0 . 4 7 3 7 4 4 3 } \\ { 0 } & { 0 } & { - 8 . 9 3 9 1 4 1 } \end{array} } { \Biggl ] } } \\ & { L = { \Biggl [ } 0 . 5 \qquad 0 \qquad 0 \qquad 0 } \\ { 0 . \qquad 1 \qquad 1 \qquad 0 \qquad 0 } \\ { 0 \qquad \quad - 2 \qquad 1 \ 1 0 } & { 0 } \\ { 1 \qquad \quad - 1 . 3 3 3 3 3 \ 2 \ 1 4 } \end{array} \qquad { \mathrm { a n d } } \ U = { \Biggl [ } { \begin{array} { c c c c } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 . 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 . 5 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } { \Biggr ] } } \end{array} $ (c)   
(d) $L = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 1 . 8 4 9 1 9 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 0 . 4 5 9 6 4 3 3 } } & { { - 0 . 2 5 0 1 2 1 9 } } & { { 1 } } & { { 0 } } \\ { { 2 . 7 6 8 6 6 1 } } & { { - 0 . 3 0 7 9 4 3 5 } } & { { - 5 . 3 5 2 2 8 3 } } & { { 1 } } \end{array} \right]$ and $U = \left[ \begin{array} { c c c c } { { 2 . 1 7 5 6 0 0 } } & { { 4 . 0 2 3 0 9 9 } } & { { - 2 . 1 7 3 1 9 9 } } & { { 5 . 1 9 6 7 0 0 } } \\ { { 0 } } & { { 1 3 . 4 3 9 4 7 } } & { { - 4 . 0 1 8 6 6 0 } } & { { 1 0 . 8 0 6 9 8 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 8 9 2 9 5 1 0 } } & { { 5 . 0 9 1 6 9 2 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 2 . 0 3 6 1 4 } } \end{array} \right]$   
6. (a) $L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 / 2 } & { 1 } \end{array} } \right] { \mathrm { ~ a n d ~ } } U = \left[ { \begin{array} { c c c } { 1 } & { - 1 } & { 0 } \\ { 0 } & { 4 } & { 3 } \\ { 0 } & { 0 } & { 1 / 2 } \end{array} } \right]$   
(b) $L = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 3 / 5 } & { 1 } & { 0 } \\ { 6 / 5 } & { - 3 8 / 1 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } U = { \left[ \begin{array} { l l l } { 1 / 3 } & { 1 / 2 } & { - 1 / 4 } \\ { 0 } & { 1 1 / 3 0 } & { 2 1 / 4 0 } \\ { 0 } & { 0 } & { 2 4 1 / 8 8 } \end{array} \right] }$ (c) $L = \left[ { \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 / 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { - 6 / 7 } & { 1 } & { 0 } \\ { - 1 } & { 6 / 7 } & { - 4 / 2 5 } & { 1 } \end{array} } \right]$ and   
(d) ${ \begin{array} { l } { U = { \left[ \begin{array} { l l l l l } { 2 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 7 / 2 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 2 5 / 7 } & { 4 } \\ { 0 } & { 0 } & { 0 } & { 1 4 1 / 2 5 } \end{array} \right] } } \\ { L = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { - 0 . 6 0 6 1 9 6 } & { - 0 . 1 6 8 4 6 5 } & { 1 } & { 0 } \\ { 0 . 4 1 3 2 8 9 } & { 0 . 7 7 8 8 1 6 } & { - 0 . 7 0 7 7 2 3 } & { 1 } \end{array} \right] } } \end{array} }$ and $U = \left[ \begin{array} { c c c c } { { 5 . 1 3 1 2 } } & { { 1 . 4 1 4 } } & { { 3 . 1 4 1 } } & { { 0 } } \\ { { 0 } } & { { 5 . 1 9 3 } } & { { - 2 . 1 9 7 } } & { { 5 . 9 2 0 5 6 } } \\ { { 0 } } & { { 0 } } & { { 4 . 2 5 1 9 5 } } & { { 4 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 2 . 6 8 2 8 } } \end{array} \right]$

7. The modified $L U$ algorithm gives the following:

(a) $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1$   
(b) $x _ { 1 } = 1$ , $x _ { 2 } = 1$ , $x _ { 3 } = 1$   
(c) $x _ { 1 } = 1 . 5$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1 . 1 9 9 9 9 8$ , $x _ { 4 } = 3$   
(d) $x _ { 1 } = 2 . 9 3 9 8 5 1$ , $x _ { 2 } = 0 . 0 7 0 6 7 7 7 0$ , $x _ { 3 } = 5 . 6 7 7 7 3 5$ , $x _ { 4 } = 4 . 3 7 9 8 1 2$

8. The modified $L U$ algorithm gives the following:

(a) $x _ { 1 } = - 1 2 , x _ { 2 } = - 1 4 , x _ { 3 } = 1 7$ (b) $x _ { 1 } = - 4 9 5 / 2 4 1$ , $x _ { 2 } = 8 4 0 / 2 4 1$ , x3 =56/241 (c) $x _ { 1 } = - 2 9 / 4 7$ , $x _ { 2 } = 5 8 / 4 7$ , $x _ { 3 } = 3 2 / 1 4 1$ , x4 =52/141 (d) $x _ { 1 } = - 0 . 7 0 6 1 2 3$ , $x _ { 2 } = - 0 . 1 8 7 4 1 0$ , $x _ { 3 } = 0 . 5 6 9 1 8 8$ , $x _ { 4 } = 0 . 5 2 8 7 0 4$

9. \*(a) $P ^ { t } L U = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { - { \frac { 1 } { 2 } } } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 1 } \\ { 0 } & { 2 } & { 3 } \\ { 0 } & { 0 } & { { \frac { 5 } { 2 } } } \end{array} \right] }$

$$
P ^ { t } L U = [ { \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} } [ { \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \end{array} } ] [ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 0 } & { - 5 } & { 6 } \\ { 0 } & { 0 } & { 4 } \end{array} } ]
$$

$$
P ^ { t } L U = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \\ { 3 } & { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { - 2 } & { 3 } & { 0 } \\ { 0 } & { 5 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { - 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } & { 3 } \end{array} \right] }
$$

$$
P ^ { t } L U = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { - 2 } & { 3 } & { 0 } \\ { 0 } & { 5 } & { - 3 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$^ { * } 1 0$ . (a) To compute $P ^ { t } L U$ requires ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 1 } { 3 } } } n$ Multiplications/Divisions and ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 1 } { 2 } } } n ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } n$ Additions/Subtractions. (b) If $\ddot { P }$ is obtained from $P$ by a simple row interchange, then $\operatorname* { d e t } \tilde { P } = - \operatorname* { d e t } P$ . Thus, if $\ddot { P }$ is obtained from $P$ by $k$ interchanges, we have $\operatorname* { d e t } \tilde { P } = ( - 1 ) ^ { k } \operatorname* { d e t } P$ . (c) Only $n - 1$ multiplications are needed in addition to the operations in part (a). (d) We have det $A = - 7 4 1$ . Factoring and computing det $A$ requires 75 Multiplications/Divisions and 55 Additions/Subtractions.

\*11. (a) The steps in Algorithm 6.4 give the following:   

<table><tr><td>Multiplications/Divisions</td><td>Additions/Subtractions</td></tr><tr><td>Step 2 n-1 n-1：</td><td>0 n-1</td></tr><tr><td>Step 4</td><td>∑=i-1 i2i-1</td></tr><tr><td>Step 5 £i=2 -n-1 n ∑j=i+1 [2(𝑖-1) +1]</td><td>n-1 Cj=i+12(i-1) In i=2</td></tr><tr><td>Step 6</td><td>n-1 n-1</td></tr><tr><td>Totals</td><td>n-n n²-n²+n</td></tr></table>

(b) The equations are given by

$$
y _ { 1 } = \frac { b _ { 1 } } { l _ { 1 1 } } \quad \mathrm { a n d } \quad y _ { i } = b _ { i } - \sum _ { j = 1 } ^ { i - 1 } \frac { l _ { i j } y _ { j } } { l _ { i i } } , \quad \mathrm { f o r } i = 2 , \dots , n .
$$

If we assume that $l _ { i i } ~ = ~ 1$ , for each $i = 1 , 2 , \dots , n$ , then the number of Multiplications/Divisions is

$$
\sum _ { i = 2 } ^ { n } ( i - 1 ) = { \frac { n ( n - 1 ) } { 2 } } ,
$$

and the number of Additions/Subtractions is the same.

(c)

<table><tr><td></td><td>Multiplications/divisionsAdditions/subtractions</td></tr><tr><td>Factoring into LU</td><td>n n²-n²+n</td></tr><tr><td>Solving Ly = b</td><td>n²-n</td></tr><tr><td>Solving Ux = y</td><td>n²-n n²+n n²-n</td></tr><tr><td>Total</td><td>n³+n²-n n+n²-n</td></tr></table>

(d)

<table><tr><td></td><td>Multiplications/divisions</td><td>Additions/subtractions</td></tr><tr><td>Factoring into LU</td><td>n-n</td><td>n-n²+n</td></tr><tr><td>Solving Ly(k) = b(k)</td><td>(n²-n)m</td><td>(n²-n)m</td></tr><tr><td>Solving Ux(k) = y(k)</td><td>(n²+n）m</td><td>(n²-n)m</td></tr><tr><td>Total</td><td>n³+mn²-n</td><td>n³+(m-)n²-(m-)n</td></tr></table>

# Exercise Set 6.6, page 425

1. (i) The only symmetric matrix is (a). (ii) All are nonsingular. (iii) Matrices (a) and (b) are strictly diagonally dominant. (iv) The only positive definite matrix is (a).

2. (i) Matrices (a) and (c) are symmetric. (ii) Matrices (a), (b), and (c) are nonsingular. (iii) Matrices (a) and (b) are strictly diagonally dominant. (iv) Matrices (b) and (c) are positive definite.

3. The $L D L ^ { t }$ factorization of the matrices $A$ have the following forms.

$$
L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { 0 } & { - { \frac { 2 } { 3 } } } & { 1 } \end{array} } \right] , D = \left[ { \begin{array} { c c c } { 2 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 2 } } } & { 0 } \\ { 0 } & { 0 } & { { \frac { 4 } { 3 } } } \end{array} } \right]
$$

$$
L = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 4 5 4 5 4 5 4 5 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 2 7 2 7 2 7 } & { 0 . 0 7 6 9 2 3 0 7 7 } & { 1 } \end{array} \right] } , \quad D = { \left[ \begin{array} { l l l l } { 4 . 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 . 1 8 1 8 1 8 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 . 5 3 8 4 6 1 5 } \end{array} \right] }
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { - 0 . 2 5 } & { - 0 . 2 7 2 7 2 7 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 . 4 4 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 4 . 5 4 5 4 5 4 5 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 3 . 1 2 } \end{array} \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 3 3 3 3 3 3 3 } & { 1 } & { 0 } & { 0 } \\ { 0 . 1 6 6 6 6 6 7 } & { 0 . 2 } & { 1 } & { 0 } \\ { - 0 . 1 6 6 6 6 6 7 } & { 0 . 1 } & { - 0 . 2 4 3 2 4 3 2 4 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 6 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 . 3 3 3 3 3 3 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 3 . 7 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 2 . 5 8 1 0 8 1 1 } \end{array} \right]
$$

4. The $L D L ^ { t }$ factorization of the matrices $A$ have the following forms.

$$
L = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 0 . 2 5 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 0 9 0 9 0 9 } & { 1 } \end{array} \right] , D = \left[ \begin{array} { c c c } { 4 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } \\ { 0 } & { 0 } & { 1 . 7 2 7 2 7 2 7 3 } \end{array} \right]
$$

$$
L = \left[ { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 . 5 } & { 1 } & { 0 } \\ { 0 . 5 } & { 0 . 2 } & { 1 } \end{array} } \right] , \quad D = \left[ { \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 5 } & { 0 } \\ { 0 } & { 0 } & { 3 . 6 } \end{array} } \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 . 5 } & { - 0 . 3 3 3 3 3 3 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 3 3 3 3 3 3 3 } & { 0 . 6 . 0 7 1 4 2 8 6 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 4 . 6 6 6 6 7 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 5 . 6 9 6 4 2 9 } \end{array} \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 9 0 9 0 9 0 9 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 4 5 4 5 4 5 5 } & { 0 . 3 6 8 4 2 1 1 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 . 7 2 7 2 7 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 2 . 9 4 7 3 6 8 } \end{array} \right]
$$

5. Cholesky’s Algorithm gives the following results.

(a) $L = \left[ \begin{array} { c c c } { { 1 . 4 1 4 2 1 3 } } & { { 0 } } & { { 0 } } \\ { { - 0 . 7 0 7 1 0 6 9 } } & { { 1 . 2 2 4 7 4 3 } } & { { 0 } } \\ { { 0 } } & { { - 0 . 8 1 6 4 9 7 2 } } & { { 1 . 1 5 4 6 9 9 } } \end{array} \right]$   
(b) $L = \left[ \begin{array} { c c c c } { { 2 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 . 5 } } & { { 1 . 6 5 8 3 1 1 } } & { { 0 } } & { { 0 } } \\ { { 0 . 5 } } & { { - 0 . 7 5 3 7 7 8 5 } } & { { 1 . 0 8 7 1 1 3 } } & { { 0 } } \\ { { 0 . 5 } } & { { 0 . 4 5 2 2 6 7 1 } } & { { 0 . 0 8 3 6 2 4 4 2 } } & { { 1 . 2 4 0 3 4 6 } } \end{array} \right]$   
(c) $L = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 . 5 } & { 1 . 6 5 8 3 1 1 } & { 0 } & { 0 } \\ { - 0 . 5 } & { - 0 . 4 5 2 2 6 7 1 } & { 2 . 1 3 2 0 0 6 } & { 0 } \\ { 0 } & { 0 } & { 0 . 9 3 8 0 8 3 3 } & { 1 . 7 6 6 3 5 1 } \end{array} \right]$ 2.449489 0 0 0   
(d) L = 0.4082483 0.8164966 1.825741 0.3651483 0 1.923538 0 0 0.4082483 0.1825741 0.4678876 1.606574

6. Cholesky’s Algorithm gives the following results.

$$
L = \left[ \begin{array} { c c c } { { 2 } } & { { 0 } } & { { 0 } } \\ { { - 1 / 2 } } & { { \sqrt { 1 1 } / 2 } } & { { 0 } } \\ { { 1 / 2 } } & { { \sqrt { 1 1 } / 2 2 } } & { { \sqrt { 2 0 9 } / 1 1 } } \end{array} \right]
$$

$$
L = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 1 } & { { \sqrt { 5 } } } & { 0 } \\ { 1 } & { { \sqrt { 5 } } / 5 } & { { \sqrt { 9 5 } } / 5 } \end{array} \right] }
$$

$$
L = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { \sqrt { 3 } } & { 0 } & { 0 } \\ { 1 } & { - \sqrt { 3 } / 3 } & { \sqrt { 4 2 } / 3 } & { 0 } \\ { 1 / 2 0 } & { \sqrt { 3 } / 3 } & { 1 7 \sqrt { 4 2 } / 8 4 } & { \sqrt { 4 4 6 6 } / 2 8 } \end{array} \right]
$$

$$
L = { \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 1 / 2 } & { { \sqrt { 1 1 } } / 2 } & { 0 } & { 0 } \\ { 1 / 2 } & { - { \sqrt { 1 1 } } / 2 2 } & { { \sqrt { 2 0 9 } } / 1 1 } & { 0 } \\ { 1 / 2 } & { - 5 { \sqrt { 1 1 } } / 2 2 } & { 7 { \sqrt { 2 0 9 } } / 2 0 9 } & { 2 { \sqrt { 2 6 6 } } / 1 9 } \end{array} \right] }
$$

7. The modified factorization algorithm gives the following results.

(a) $x _ { 1 } = 1$ , $x _ { 2 } = - 1$ , $x _ { 3 } = 0$ (b) $x _ { 1 } = 0 . 2$ , $x _ { 2 } = - 0 . 2$ , $x _ { 3 } = - 0 . 2$ , $x _ { 4 } = 0 . 2 5$ (c) $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1$ , $x _ { 4 } = 2$

(d) $x _ { 1 } = - 0 . 8 5 8 6 3 8 7$ , $x _ { 2 } = 2 . 4 1 8 8 4 8$ , $x _ { 3 } = - 0 . 9 5 8 1 1 5 2$ , $x _ { 4 } = - 1 . 2 7 2 2 5 1$

8. The modified factorization algorithm gives the following results.

(a) $x _ { 1 } = - 1 3 / 1 9 , x _ { 2 } = 2 1 / 1 9 , x _ { 3 } = 5 4 / 1 9$ (b) $x _ { 1 } = - 3 / 3 8$ , $x _ { 2 } = 4 / 1 9$ , $x _ { 3 } = - 1 / 1 9$ (c) $x _ { 1 } = - 4 5 2 / 3 1 9$ , $x _ { 2 } = 3 7 3 / 3 1 9$ , $x _ { 3 } = 7 6 3 / 3 1 9$ , $x _ { 4 } = - 3 5 6 / 3 1 9$ (d) $x _ { 1 } = 5 / 2 8$ , $x _ { 2 } = 5 / 7$ , $x _ { 3 } = 1 / 4$ , $x _ { 4 } = 9 / 2 8$

9. The modified Cholesky’s algorithm gives the following results.

(a) $x _ { 1 } = 1 , x _ { 2 } = - 1 , x _ { 3 } = 0$   
(b) $x _ { 1 } = 0 . 2 , x _ { 2 } = - 0 . 2 , x _ { 3 } = - 0 . 2 , x _ { 4 } = 0 . 2 5$   
(c) $x _ { 1 } = 1 , x _ { 2 } = 2 , x _ { 3 } = - 1 , x _ { 4 } = : 2$   
(d) $x _ { 1 } = - 0 . 8 5 8 6 \div 3 8 7 4 , x _ { 2 } = 2 . 4 1 8 8 4 8 \div 2 , x _ { 3 } = - 0 . 9 5 8 1 1 5 1 8 , x _ { 4 } = - 1 . 2 7 2 2 5$

10. (a) $x _ { 1 } = - 0 . 6 8 4 2 1 0 5 2 6 5 , x _ { 2 } = 1 . 1 0 5 2 6 3 1 5 8 , x _ { 3 } = 2 . 8 4 2 1 0 5 2 6 3$ (b) $x _ { 1 } = - 0 . 0 7 8 9 4 7 3 6 8 9 0 , x _ { 2 } = 0 . 2 1 0 5 2 6 3 1 5 8 , x _ { 3 } = - 0 . 0 5 2 6 3 1 5 7 8 9 5$ 5 (c) $\mathfrak { c } _ { 1 } = - 1 . 4 1 6 9 2 7 9 0 0 , x _ { 2 } = 1 . 1 6 9 2 7 8 9 9 7 , x _ { 3 } = 2 . 3$ $x _ { 2 } = 1 . 1 6 9 2 7 8 9 9 7 , x _ { 3 } = 2 . 3 9 1 8 4 9 5 3 0 , x _ { 4 } = - 1 . 1$ 15987461 (d) $x _ { 1 } = 0 . 1 7 8 5 7 1 4 2 8 6 , x _ { 2 } = 0 . 7 1 4 2 8 5 7 1 4 2 , x _ { 3 } = 0 . 2 5 , x _ { 4 } = 0 . 3 2 1 4 2 8 5 7 1 4 2 , x _ { 5 } = 0 . 2 4 2 , x _ { 6 } = 0 . 2 5 , x _ { 7 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 9 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 .$

11. The Crout Factorization Algorithm gives the following results.

$^ *$ (a) $x _ { 1 } = 0 . 5$ , $x _ { 2 } = 0 . 5$ , $x _ { 3 } = 1$   
(b) $x _ { 1 } = - 0 . 9 9 9 9 9 9 5$ , $x _ { 2 } = 1 . 9 9 9 9 9 9 9$ , $x _ { 3 } = 1$   
(c) $x _ { 1 } = 1$ , $x _ { 2 } = - 1$ , $x _ { 3 } = 0$   
(d) $x _ { 1 } = - 0 . 0 9 3 5 7 7 9 8$ , $x _ { 2 } = 1 . 5 8 7 1 5 6$ , $x _ { 3 } = - 1 . 1 6 7 4 3 1$ , $x _ { 4 } = 0 . 5 4 1 2 8 4 4$

12. The Crout Factorization Algorithm gives the following results.

(a) $x _ { 1 } = 3 . 6 0 0 0 0 0 0 0 0$ , $x _ { 2 } = - 4 . 2 0 0 0 0 0 0 0 0$ , $x _ { 3 } = 2 . 8 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 3 . 9 4 4 4 4 4 4 4 4$ , $x _ { 2 } = 2 . 8 8 8 8 8 8 8 9$ , $x _ { 3 } = - 0 . 7 2 2 2 2 2 2 2 2 2$   
(c) $x _ { 1 } = 2 . 3 8 0 9 5 2 3 8 1$ , $x _ { 2 } = 1 . 7 6 1 9 0 4 7 6 2$ , $x _ { 3 } = 1 . 9 0 4 7 6 1 9 0 5$ , $x _ { 4 } = 2 . 0 4 7 6 1 9 0 4 8$   
(d) $x _ { 1 } ~ = ~ 0 . 6 6 6 6 6 6 6 6 7$ , $x _ { 2 } ~ = ~ 0 . 3 3 3 3 3 3 3 3 3 4$ , $x _ { 3 } ~ = ~ - 0 . 6 6 6 6 6 6 6 6 6 6$ , $x _ { 4 } ~ = ~ - 1 . 0 0 0 0 0 0 0 0 0$ , $x _ { 5 } = 0 . 0 0 0 0 0 0 0 0$

13. We have $x _ { i } = 1$ , for each $i = 1 , \ldots , 1 0$ .

14. The modified $L D L ^ { t }$ factorization gives the following results.

(a)

$$
L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } \\ { 2 } & { 1 } & { 1 } \end{array} } \right] , \qquad D = \left[ { \begin{array} { c c c } { 3 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} } \right]
$$

$$
L = \left[ { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { - 2 } & { 1 } & { 0 } \\ { 3 } & { - 1 } & { 1 } \end{array} } \right] , \qquad D = \left[ { \begin{array} { l l l } { 3 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right]
$$

$$
L = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 2 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { - 1 } } & { { 1 } } & { { 4 } } & { { 1 } } \end{array} \right] , \qquad D = \left[ \begin{array} { c c c c } { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { - 4 } } \end{array} \right]
$$

$$
L = \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { 0 } \\ { 2 } & { 0 } & { 1 } & { 0 } \\ { - 2 } & { 1 } & { - 1 } & { 1 } \end{array} \right] , \qquad D = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 3 } \end{array} \right]
$$

15. Only the matrix in (d) is positive definite.

16. When $\begin{array} { r } { \alpha > { \frac { 8 } { 7 } } } \end{array}$ the matrix is positive definite.

$^ *$ 17. When $\textstyle - 2 < \alpha < { \frac { 3 } { 2 } }$ the matrix is positive definite.

18. When $0 < \beta < \frac { \perp } { 2 }$ and $\beta + 2 < | \alpha | < 3$ the matrix is strictly diagonally dominant.

$^ { * } 1 9$ . When $0 < \beta < 1$ and $3 < \alpha < 5 - \beta$ the matrix is strictly diagonally dominant.

$^ { * } 2 0$ . (a) Yes. (b) $\begin{array} { r l } & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { 3 } & { 4 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { l l } { - 2 } & { 1 } \\ { 1 } & { - 2 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { 3 } & { 4 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] . } \end{array}$ (c) (d) (e)

21. (a) No; for example, consider $\left[ { \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right]$ . (b) Yes, since $A = A ^ { t }$ . (c) Yes, since $\mathbf { x } ^ { t } ( A + B ) \mathbf { x } = \mathbf { x } ^ { t } A \mathbf { x } + \mathbf { x } ^ { t } B \mathbf { x }$ . (d) Yes, since $\mathbf { x } ^ { t } A ^ { 2 } \mathbf { x } = \mathbf { x } ^ { t } A ^ { t } A \mathbf { x } = ( A \mathbf { x } ) ^ { t } ( A \mathbf { x } ) \geq 0$ , and because $A$ is nonsingular, equality holds only if $\mathbf { x } = \mathbf { 0 }$ . (e) No; for example, consider $A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }$ and $B = { \left[ \begin{array} { l l } { 1 0 } & { ~ 0 } \\ { 0 } & { 1 0 } \end{array} \right] }$ .

\*22. (a) When $\alpha = 2$ the matrix is singular. (b) The matrix $A$ cannot be strictly diagonally dominant regardless of $\alpha$ . (c) The matrix is symmetric for all values of $\alpha$ . (d) The matrix is positive definite when $\alpha > 2$ .

23. (a) Since $\operatorname* { d e t } A = 3 \alpha - 2 \beta$ , the matrix $A$ is singular if and only if $\alpha = 2 \beta / 3$ . (b) The matrix is strictly diagonally dominant when $| \alpha | > 1$ and $| \beta | < 1$ . (c) The matrix is symmetric when $\beta = 1$ . (d) The matrix is positive definite when $\alpha > \frac { 2 } { 3 }$ and $\beta = 1$ .

24. Yes, since $A ^ { t } B ^ { t } = ( B A ) ^ { t } = ( A B ) ^ { t } = B ^ { t } A ^ { t }$ .

25. One example is $A = \left[ \begin{array} { l l } { 1 . 0 } & { 0 . 2 } \\ { 0 . 1 } & { 1 . 0 } \end{array} \right]$ .

26. Partition $A ^ { ( k ) }$ into the form

$$
\begin{array} { r } { A ^ { ( k ) } = \left[ \begin{array} { c c c c c c c c } { a _ { 1 1 } ^ { ( 1 ) } } & { a _ { 1 2 } ^ { ( 1 ) } } & { \ldots } & { a _ { 1 , k } ^ { ( 1 ) } } & { a _ { 1 , k + 1 } ^ { ( 1 ) } } & { \ldots } & { a _ { l , n } ^ { ( 1 ) } } \\ { 0 } & { a _ { 2 2 } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 k } ^ { ( 2 ) } } & { a _ { 2 k + 1 } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 n } ^ { ( 2 ) } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { \ldots } & { 0 } & { a _ { k , k } ^ { ( k ) } } & { a _ { k , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { k , n } ^ { ( k ) } } \\ & & & & & & { a _ { k + 1 , k } ^ { ( k ) } } & { \ldots } & { a _ { k + 1 , n } ^ { ( k ) } } \\ { 0 } & { \ldots } & { 0 } & { a _ { k + 1 , k } ^ { ( k ) } } & { a _ { k + 1 , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { k + 1 , n } ^ { ( k ) } } \\ { \vdots } & { \ddots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { \ldots } & { 0 } & { a _ { n , k } ^ { ( k ) } } & { a _ { n , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { n , n } ^ { ( k ) } } \end{array} \right] = \left[ \begin{array} { c c } { A _ { 1 1 } ^ { ( k ) } } & { A _ { 1 2 } ^ { ( k ) } } \\ { A _ { 2 1 } ^ { ( k ) } } & { A _ { 2 2 } ^ { ( k ) } } \end{array} \right] . } \end{array}
$$

The multiplier matrix $M ^ { ( k - 1 ) }$ and $A ^ { ( k - 1 ) }$ can be similarly partitioned into

$$
\begin{array} { r } { \mathbb { M } ^ { ( k - 1 ) } = \left[ \begin{array} { l l l l l l l l l } { 1 } & { 0 } & { \cdots } & { \cdots } & { 0 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { \ddots } & { \ddots } & { } & { } & { \vdots } & { \vdots } & { } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { } & { } & { \vdots } & { \vdots } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 1 } & { 0 } & { \vdots } & { } & { \vdots } & { } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k , k - 1 } } & { 1 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k + 1 , k - 1 } } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k + 1 , k - 1 } } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { 0 } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { n , k - 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] = \left[ \begin{array} { l } { M _ { 1 1 } ^ { ( k - 1 ) } } \\ { M _ { 2 1 } ^ { ( k - 1 ) } } \\ { M _ { 2 1 } ^ { ( k - 1 ) } } \end{array} \right] , } \end{array}
$$

where $M _ { 1 1 } ^ { ( k - 1 ) }$ is a $k \times k$ lower triangular matrix, $O$ is a $k \times ( n - k )$ block of zeros, $M _ { 2 1 } ^ { ( k - 1 ) }$ is $( n - k ) \times k$ matrix, $I$ identity matrix, and

$$
A ^ { ( k - 1 ) } = \left[ \begin{array} { l l } { A _ { 1 1 } ^ { ( k - 1 ) } } & { A _ { 1 2 } ^ { ( k - 1 ) } } \\ { A _ { 2 1 } ^ { ( k - 1 ) } } & { A _ { 2 2 } ^ { ( k - 1 ) } } \end{array} \right] .
$$

Here A(k−11 is $k \times k$ , $A _ { 1 2 } ^ { ( k - 1 ) }$ is $k \times ( n - k )$ , $A _ { 2 1 } ^ { ( k - 1 ) }$ is $( n - k ) \times k$ , and $A _ { 2 2 } ^ { ( k - 1 ) }$ is $( n - k ) \times ( n - k )$ . The formation of ${ A } _ { 1 1 } ^ { ( k ) }$ can be obtained from the partitioned product of $M ^ { ( k - 1 ) }$ and $A ^ { ( k - 1 ) }$ and is given by

$$
A _ { 1 1 } ^ { ( k ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } + 0 \cdot A _ { 2 1 } ^ { ( k - 1 ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } .
$$

In a similar manner, each of $M ^ { ( k - 2 ) } , \ldots , M ^ { ( 1 ) }$ and $A ^ { ( k - 2 ) } , \ldots , A ^ { ( 1 ) }$ can be partitioned to obtain

$$
A _ { 1 1 } ^ { ( k ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } = M _ { 1 1 } ^ { ( k - 1 ) } M _ { 1 1 } ^ { ( k - 2 ) } A _ { 1 1 } ^ { ( k - 2 ) } = \ldots = M _ { 1 1 } ^ { ( k - 1 ) } M _ { 1 1 } ^ { ( k - 2 ) } \ldots M _ { 1 1 } ^ { ( 1 ) } A _ { 1 1 } ^ { ( 1 ) } ,
$$

where $A _ { 1 1 } ^ { ( 1 ) } = A _ { 1 1 }$ is the $k \times k$ leading principal submatrix of $A$ . Assume all leading principal submatrices of $A$ are nonsingular. Then $a _ { 1 1 } \neq 0$ , and the elimination process can be started. For the inductive hypothesis, assume that $k - 1$ elimination steps can be performed without row interchanges. It follows that $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { k - 1 , k - 1 } ^ { ( k - 1 ) }$ are all nonzero and the above equation holds. Taking determinants produces

$$
a _ { 1 1 } ^ { ( 1 ) } a _ { 2 2 } ^ { ( 2 ) } \ldots a _ { k - 1 , k - 1 } ^ { ( k - 1 ) } a _ { k , k } ^ { ( k ) } = \operatorname* { d e t } A _ { 1 1 } ^ { ( k ) } = \operatorname* { d e t } M _ { 1 1 } ^ { ( k - 1 ) } \operatorname* { d e t } M _ { 1 1 } ^ { ( k - 2 ) } \ldots \operatorname* { d e t } M _ { 1 1 } ^ { ( 1 ) } \operatorname* { d e t } A _ { 1 1 } \neq 0 .
$$

Hence, $a _ { k , k } ^ { ( k ) } \neq 0$ and the process can continue. By mathematical induction all pivot elements $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n , n } ^ { ( n ) }$ are nonzero and Gaussian elimination can be performed without row interchanges.

Conversely, suppose Gaussian elifollows that all the pivot elements $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n , n } ^ { ( n ) }$ be performed without row interchanges. It are nonzero. Thus,

$$
\operatorname* { d e t } A _ { 1 1 } = a _ { 1 1 } ^ { ( 1 ) } a _ { 2 2 } ^ { ( 2 ) } \cdot . . a _ { k , k } ^ { ( k ) } \neq 0 ,
$$

and the $k \times k$ principal leading submatrix is nonsingular, for each $k = 1 , 2 , \ldots , n$ .

\*27. The Crout Factorization Algorithm can be rewritten as follows:

STEP 1 Set $l _ { 1 } = a _ { 1 } ; u _ { 1 } = c _ { 1 } / l _ { 1 }$ .   
STEP 2 For $i = 2 , \ldots , n - 1$ set $l _ { i } = a _ { i } - b _ { i } u _ { i - 1 } ; u _ { i } = c _ { i } / l _ { i }$ .   
STEP 3 Set ln = an − bnun 1.   
STEP 4 Set $z _ { 1 } = d _ { 1 } / l _ { 1 }$ .   
STEP 5 For $i = 2 , \ldots , n$ set $z _ { i } = ( d _ { i } - b _ { i } z _ { i - 1 } ) / l _ { i }$ .   
STEP 6 Set $x _ { n } = z _ { n }$ .   
STEP 7 For i = n − 1, . . . , 1 set xi = zi − uixi+1.   
STEP 8 OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ;   
STOP.

\*28. First, $\left| l _ { 1 1 } \right| = \left| a _ { 1 1 } \right| > 0$ and $\begin{array} { r } { | u _ { 1 2 } | = \frac { | a _ { 1 2 } | } { | l _ { 1 1 } | } < 1 } \end{array}$ . In general, assume $| l _ { j j } | > 0$ and $| u _ { j , j + 1 } | < 1$ , for $j = 1 , \ldots , i - 1$ . Then

$$
\left| l _ { i i } \right| = \left| a _ { i i } - l _ { i , i - 1 } u _ { i - 1 , i } \right| = \left| a _ { i i } - a _ { i , i - 1 } u _ { i - 1 , i } \right| \geq \left| a _ { i i } \right| - \left| a _ { i , i - 1 } u _ { i - 1 , i } \right| > \left| a _ { i i } \right| - \left| a _ { i , i - 1 } \right| > 0 ,
$$

and

$$
\left| u _ { i , i + 1 } \right| = \frac { \left| a _ { i , i + 1 } \right| } { \left| l _ { i i } \right| } < \frac { \left| a _ { i , i + 1 } \right| } { \left| a _ { i i } \right| - \left| a _ { i , i - 1 } \right| } \leq 1 ,
$$

for $i = 2 , \ldots , n - 1$ . Further,

$$
\left| l _ { n n } \right| = \left| a _ { n n } - l _ { n , n - 1 } u _ { n - 1 , n } \right| = \left| a _ { n n } - a _ { n , n - 1 } u _ { n - 1 , n } \right| \geq \left| a _ { n n } \right| - \left| a _ { n , n - 1 } \right| > 0 .
$$

So

$$
\operatorname* { d e t } A = \operatorname* { d e t } L \cdot \operatorname* { d e t } U = l _ { 1 1 } \cdot l _ { 2 2 } \ldots l _ { n n } \cdot 1 > 0 .
$$

$$
i _ { 1 } = 0 . 6 7 8 5 0 4 7 , \quad i _ { 2 } = 0 . 4 2 1 4 9 5 3 , \quad i _ { 3 } = 0 . 2 5 7 0 0 9 3 , \quad i _ { 4 } = 0 . 1 5 4 2 0 5 6 , \quad i _ { 5 } = 0 . 1 0 2 8 0 3 7
$$

30. The Crout Factorization Algorithm requires $5 n - 4$ Multiplications/Divisions and $3 n - 3$ Additions/Subtractions.

31. (a) Mating male $i$ with female $j$ produces offspring with the same wing characteristics as mating male $j$ with female $i$ . (b) No. Consider, for example, $\mathbf { x } = ( 1 , 0 , - 1 ) ^ { t }$ .

\*32. (a)

$$
D ^ { 1 / 2 } D ^ { 1 / 2 } = \left[ \begin{array} { c c c c c } { \sqrt { d _ { 1 1 } } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \sqrt { d _ { 2 2 } } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { } \\ { 0 } & { \cdots } & { 0 } & { \sqrt { d _ { n n } } } \end{array} \right] \cdot \left[ \begin{array} { c c c c c } { \sqrt { d _ { 1 1 } } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \sqrt { d _ { 2 2 } } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { \sqrt { d _ { n n } } } \end{array} \right] = \left[ \begin{array} { c c c c c } { d _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { d _ { 2 2 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { d _ { n n } } \end{array} \right] .
$$

(b) We have

$$
\left( \hat { L } D ^ { 1 / 2 } \right) \left( \hat { L } D ^ { 1 / 2 } \right) ^ { t } = \hat { L } D ^ { 1 / 2 } \left( D ^ { 1 / 2 } \right) ^ { t } \hat { L } ^ { t } = \hat { L } D ^ { 1 / 2 } D ^ { 1 / 2 } \hat { L } ^ { t } = \hat { L } D \hat { L } ^ { t } = A .
$$

Since $L L ^ { t } = A$ , we have $\hat { L } D ^ { 1 / 2 } = L$

# Iterative Techniques in Matrix Algebra

Exercise Set 7.1, page 441

1. (a) We have $| | \mathbf { x } | | _ { \infty } = 4$ and $| | \mathbf { x } | | _ { 2 } = 5 . 2 2 0 1 5 3$ . (b) We have $| | \mathbf { x } | | _ { \infty } = 4$ and $| | \mathbf { x } | | _ { 2 } = 5 . 4 7 7 2 2 6$ . (c) We have $| | \mathbf { x } | | _ { \infty } = 2 ^ { k }$ and $| | \mathbf { x } | | _ { 2 } = ( 1 + 4 ^ { k } ) ^ { 1 / 2 }$ . (d) We have $| | \mathbf { x } | | _ { \infty } = 4 / ( k + 1 )$ and $| | \mathbf { x } | | _ { 2 } = ( 1 6 / ( k + 1 ) ^ { 2 } + 4 / k ^ { 4 } + k ^ { 4 } e ^ { - 2 k } ) ^ { 1 / 2 } .$

2. $^ { * } ( \mathrm { a } )$ Since $\begin{array} { r } { \| \mathbf { x } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } | \geq 0 } \end{array}$ with equality only if $x _ { i } = 0$ for all $i$ , properties $( i )$ and $( i i )$ in Definition 7.1 hold. Also,

$$
\| \alpha \mathbf { x } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | \alpha x _ { i } | = \sum _ { i = 1 } ^ { n } | \alpha \| x _ { i } | = | \alpha | \sum _ { i = 1 } ^ { n } | x _ { i } | = | \alpha | \| \mathbf { x } \| _ { 1 } ,
$$

so property $( i i i )$ holds.

Finally,

$$
\| \mathbf { x } + \mathbf { y } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | \leq \sum _ { i = 1 } ^ { n } ( | x _ { i } | + | y _ { i } | ) = \sum _ { i = 1 } ^ { n } | x _ { i } | + \sum _ { i = 1 } ^ { n } | y _ { i } | = \| \mathbf { x } \| _ { 1 } + \| \mathbf { y } \| _ { 1 } ,
$$

so property ( $_ { \mathit { l v } }$ ) also holds.

(b) (1a) 8.5 (1b) $1 0 \quad \mathrm { ~ ( 1 c ) ~ } \ : \ : \left| \sin k \right| + | \cos k | + e ^ { k } \quad \mathrm { ~ ( 1 d ) ~ } \ : \ : 4 / ( k + 1 ) + 2 / k ^ { 2 } + k ^ { 2 } e ^ { - k }$ (c) We have

$$
\begin{array} { l } { \displaystyle \| \mathbf { x } \| _ { 1 } ^ { 2 } = \left( \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | \right) ^ { 2 } = \left( | x _ { 1 } | + | x _ { 2 } | + \cdot \cdot \cdot + | x _ { n } | \right) ^ { 2 } } \\ { \displaystyle \geq | x _ { 1 } | ^ { 2 } + | x _ { 2 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { n } | ^ { 2 } = \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } . } \end{array}
$$

Thus, $\| \mathbf { x } \| _ { 1 } \geq \| \mathbf { x } \| _ { 2 }$ .