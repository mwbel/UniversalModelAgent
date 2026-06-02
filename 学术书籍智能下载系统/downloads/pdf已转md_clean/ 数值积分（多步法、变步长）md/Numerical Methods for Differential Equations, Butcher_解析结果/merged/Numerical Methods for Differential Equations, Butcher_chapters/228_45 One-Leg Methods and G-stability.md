# 45 One-Leg Methods and G-stability

450 The one-leg counterpart to a linear multistep method

In Dahlquist (1976) one-leg methods were introduced. Given a linear multistep method defined by the generating polynomial pair $\lfloor \alpha , \beta \rfloor$ , an alternative method can be found by replacing the weighted sum of derivative values

$$
h \beta _ { 0 } f ( x _ { n } , y _ { n } ) + h \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + h \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ,
$$

by the single term

$$
h \bigg ( \sum _ { i = 0 } ^ { k } \beta _ { i } \bigg ) f \bigg ( x _ { n } - \theta h , \bigg ( \sum _ { i = 0 } ^ { k } \beta _ { i } \bigg ) ^ { - 1 } \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } \bigg ) ,
$$

where $\theta$ is a weighted combination of the step numbers

$$
\theta = \frac { \sum _ { i = 0 } ^ { k } i \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } .
$$

For convenience, we write

$$
\widehat { \beta } _ { i } = \frac { \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } , \qquad i = 0 , 1 , 2 , \ldots , k .
$$

It is obvious that the linear stability of a one-leg method is the same as for the corresponding linear multistep method. However, it is possible to investigate the stability of numerical solutions of non-linear dissipative equations in a relatively simple way if the computation is carried out using one-leg methods. By contrast, the corresponding analysis for linear multistep methods becomes hopelessly complicated because of the occurrence of the same derivative terms in several steps in sequence.

Even though these stability results are derived for one-leg methods, they can be regarded as having a relevance to linear multistep method, because of a transformation that links them.

In later papers by Dahlquist and others (Dahlquist, 1983; Wantanabe and Sheikh, 1984; Hundsdorfer and Steininger, 1991), the feasibility of using oneleg methods directly, as a practical numerical algorithm, came into serious consideration. In this brief introduction to these methods, we also discuss an interpretation in terms of effective order, and review the main results on G-stability.
