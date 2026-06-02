# 403 Stability

For a general initial value problem, the computed solution satisfies

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } + h \sum _ { i = 0 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ) .
$$

However, for the one-dimensional problem for which $f ( x , y ) = 0$ , we have the simpler difference equation

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } .
$$

Definition 403A A linear multistep method $\lfloor \alpha , \beta \rfloor$ is ‘stable’ if the difference equation (403a) has only bounded solutions.

Because stability concepts of one sort or another abound in the theory of initial value problems, ‘stability’ is often referred to as ‘zero-stability’ $^ -$ for example, in Lambert (1991)) $-$ or as ‘stability in the sense of Dahlquist’.
