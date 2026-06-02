# 252 An example of a Taylor series solution

We consider the example problem, already introduced in Subsection 201,

$$
y ^ { \prime } ( x ) = { \frac { y + x } { y - x } } , \qquad y ( 0 ) = 1 .
$$

Algorithm $\mathbf { 2 5 2 } \alpha$ A Taylor step for problem (252a)   

<table><tr><td>a(1)=y; b(1)= y + x; c(1)= y - x; for i=O:m- 1, temp = b(i+1); for j= 1:i, temp = temp - d(1+i-j)*c(1+j); end; d(i+1)= temp/c(1); a(i+2)= d(i+1)/(i+1); if i == 0, b(i+2)= a(i+2) + 1; c(i+2)= a(i+2) - 1; else b(i+2)= a(i+2); c(i+2)= a(i+2); end; end; x=x+h;</td></tr></table>

Let $a _ { 0 } , a _ { 1 } , \ldots , a _ { m }$ denote Taylor coefficients for $y ( x _ { n - 1 } + h )$ , $b _ { 0 } , b _ { 1 } , \ldots , b _ { m }$ be the corresponding coefficients for $y + x$ , and $c _ { 0 } , c _ { 1 } , \ldots , c _ { m }$ be the coefficients for $y - x$ . If $d _ { 0 } , d _ { 1 } , \ldots , d _ { m }$ are the coefficients for $( y + x ) / ( y - x )$ , then Algorithm $2 5 2 \alpha$ , written in MATLAB, can be used to update the value of $x \ = \ x _ { n - 1 }$ and $y = y _ { n - 1 }$ to the values at the end of a step, $x = x _ { n }$ , $y = y _ { n }$ . Note that $a _ { 0 } , a _ { 1 } , \ldots , a _ { m }$ are represented in this program by $\mathsf { a } ( 1 )$ , a(2), . . . , $\mathsf { a } \left( \mathtt { m } ^ { + 1 } \right)$ , because MATLAB subscripts start from 1 (and similarly for the $b _ { i }$ , etc.).

Numerical experiments based on this program have been made for a sequence of $m$ values from 1 to 10 and using stepsizes $h = 0 . 1 0 \times 2 ^ { - k }$ , with $k = 1 , 2 , \ldots .$ . The errors in the approximations to $y ( 0 . 5 )$ are presented in Figure 252(i). It can be seen that the rate of increase in accuracy, as smaller and smaller steps are taken, becomes more and more impressive as $m$ increases. The results found for $m = 9$ and $m = 1 0$ are not included because, even for 10 steps with $h = 0 . 0 5$ , the numerical results in these cases are accurate to approximately 15 decimal places.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/8c5bea5252a96e8713163da748b07e949917b6e4235ee870fc261e0bd359d7fc.jpg)  
Taylor series calculations

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/257fdd7d955ce6611a3e81d089c5b55613a343c1d171d3cdeed690ecc5ecfbbd.jpg)  
Taylor series calculations with cost correction

Since high values of $m$ are more time-consuming, the favourable impression of their advantages shown in this figure is an exaggeration. Since the cost is approximately proportional to $m$ , a fairer comparison would be to plot the errors against $h / m$ . This weighted comparison is shown in Figure 252(ii).

The advantage of high order methods over low order methods is still evident from this more balanced comparison.

Coefficients defined by (253c)   

<table><tr><td>m</td><td>α1</td><td>α2</td><td>Q3</td><td>α4</td><td>β1</td><td>β2</td><td>β</td><td>β4</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>3-21-215265</td><td>花</td><td></td><td></td><td>中</td><td></td><td>49</td><td></td></tr><tr><td></td><td></td><td>10</td><td>3</td><td></td><td></td><td></td><td>120</td><td></td></tr><tr><td>4</td><td></td><td>515</td><td>107</td><td></td><td></td><td></td><td>239</td><td>117</td></tr><tr><td></td><td></td><td></td><td></td><td>769</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td>28</td><td>28</td><td>1680</td><td></td><td>28</td><td>84</td><td>560</td></tr></table>

Coefficients defined by (253d)   

<table><tr><td>m</td><td>1</td><td>72</td><td>73</td><td>4</td><td>81</td><td>82</td><td>83</td><td>84</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>中</td><td>1</td><td></td><td></td><td>立共</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td>面</td><td></td><td></td><td></td><td>路 1</td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>1680</td><td></td><td></td><td></td><td>1680</td></tr></table>
