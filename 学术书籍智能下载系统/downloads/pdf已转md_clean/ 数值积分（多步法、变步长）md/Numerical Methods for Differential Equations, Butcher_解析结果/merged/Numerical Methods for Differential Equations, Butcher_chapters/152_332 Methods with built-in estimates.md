# 332 Methods with built-in estimates

Instead of using the Richardson technique it is possible to combine two methods into one by constructing a tableau with common stages but two alternative output coefficient vectors. The following method, due to Merson (1957), seems to have been the first attempt at constructing this type of stepsize control mechanism:

<table><tr><td>1</td><td>R 1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>0 0</td><td>GR 0</td><td>2 2</td><td>1</td></tr><tr><td></td><td>1</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

The interpretation of this tableau, which contains two $b ^ { \scriptscriptstyle 1 }$ vectors, is that it combines two methods given by

<table><tr><td rowspan=1 colspan=1>0 1-3:1-3:1-2 1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1  0    0    2  1</td></tr></table>

and by

<table><tr><td>0 N</td><td></td><td>1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>BU</td><td>0</td><td>G</td><td>2</td><td></td></tr><tr><td></td><td>1 10</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/a11978509f5592fc936d87d83461fb155c52032813e0ec83d846e80c2154f654.jpg)  
Two alternative stepsize control mechanisms based on Richardson (dashed line) and built-in (solid line) error estimates

In Merson’s derivation of this method, (332a) was shown to be of order 4. Although (332b) has order only 3, it becomes effectively of order 5 if used to solve linear problems with constant coefficients. The difference between the results computed by the two methods can, it is suggested, be used as a local error estimator. To show how well the method works in practice, an experiment using this technique has been carried out and the results summarized in Figure 332(i). The three problems attempted are the Kepler orbit problem with eccentricities $e = 0 . 1$ , $e = 0 . 5$ and $e = 0 . 9$ , respectively.
