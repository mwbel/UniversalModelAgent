# 270 Choice of method

Many differential equation solvers have been constructed, based on a variety of computational schemes, from Runge–Kutta and linear multistep methods, to Taylor series and extrapolation methods. In this introduction to implementation of initial value solvers, we will use an ‘Almost Runge– Kutta’ (ARK) method. We will equip this method with local error estimation, variable stepsize and interpolation. It is intended for non-stiff problems but can be used also for delay problems, because of its reliable and accurate builtin interpolation.

Many methods are designed for variable order, but this is a level of complexity which we will avoid in this introduction. The method to be presented has order 3 and, because it is a multivalue method, it might be expected to require an elaborate starting sequence. However, it is a characteristic property of ARK methods that starting will present a negligible overhead on the overall costs and will involve negligible complication in the design of the solver.

Recall from Subsection 263 the notation used for formulating a general linear method. In the case of the new experimental method, the coefficient matrix is

$$
[ A \ U ] = [ { \begin{array} { c c c c } { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 3 - 3 } & { 2 } \end{array} } [ { \begin{array} { c c c } { 1 } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 1 8 } } } \\ { 1 } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 1 8 } } } \\ { 1 } & { { \frac { 1 } { 4 } } } & { 0 } \\ { 1 } & { { \frac { 1 } { 4 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { - 2 } & { 0 } \end{array} } ] .
$$

Because general linear methods have no specific interpretation, we need to state the meaning of the various quantities which play a role in the formulation of the method. Approximate values of these are as follows:

α A single step using an ARK method   

<table><tr><td>function [xout，yout] = ARKstep(x,y,f,h) Uy = y*[1,1,1;1/3,1/6,1/4;1/18,1/18,0] ;</td></tr><tr><td>hF = h*f(x+(1/3)*h,Uy(:,1));</td></tr><tr><td></td></tr><tr><td>hF = [hF,h*f(x+(2/3)*h,Uy(:,2)+(1/2)*hF)];</td></tr><tr><td>xout = x+h;</td></tr><tr><td>y1out = Uy(:,3)+hF*[0;3/4]; hF = [hF,h*f(xout,y1out)];</td></tr></table>

$$
\begin{array} { r l } & { y _ { 0 } ^ {[ n - 1 ] } = y ( x _ { n - 1 } ) , } \\ & { y _ { 2 } ^ { [ n - 1 ] } = h y ^ { \prime } ( x _ { n - 1 } ) , } \\ & { y _ { 3 } ^ { [ n - 1 ] } = h ^ { 2 } y ^ { ( \prime \prime ) } ( x _ { n - 1 } ) , } \\ & { Y _ { 1 } = y ( x _ { n - 1 } + \frac { 1 } { 3 } h ) , } \\ & { Y _ { 2 } = y ( x _ { n - 1 } + \frac { 2 } { 3 } h ) , } \\ & { Y _ { 3 } = y ( x _ { n - 1 } + h ) , } \\ & { y _ { 1 } ^ { [ n ] } = y ( x _ { n } ) , } \\ & { y _ { 2 } ^ { [ n ] } = h y ^ { \prime } ( x _ { n } ) , } \\ & { y _ { 3 } ^ { [ n ] } = h ^ { 2 } y ^ { ( \prime \prime ) } ( x _ { n } ) . } \end{array}
$$

The method is third order and we would expect that, with precise input values, the output after a single step would be correct to within $O ( h ^ { 4 } )$ . With the interpretation we have introduced, this is not quite correct because the third output value is in error by $O ( h ^ { 3 } )$ from its target value. We can correct this by writing down a more precise formula for $y _ { 3 } ^ { [ n - 1 ] }$ , and correspondingly for $y _ { 3 } ^ { [ n ] }$ . However, we can avoid having to do this, by remarking that the method satisfies what are called ‘annihilation conditions’ which cause errors and $O ( h ^ { 3 } )$ $y _ { 2 } ^ { [ n ] }$ in the input 3 1. For this method, the stages are all computed correctly to within $y _ { 3 } ^ { [ n - 1 ] }$ to be cancelled out in the values computed for $y _ { 1 } ^ { \lfloor n \rfloor }$ $O ( h ^ { 3 } )$ , rather than only to first order accuracy as in an explicit Runge–Kutta method. The computations constituting a single step of the method in the solution of a differential equation $y ^ { \prime } = f ( x , y )$ are shown in Algorithm $2 7 0 \alpha$ . The array y as a parameter for the function ARKstep consists of three columns with the values of $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { [ n - 1 ] }$ , $y _ { 3 } ^ { \lfloor n - 1 \rfloor }$ , respectively. The updated values of these quantities, at the end of step $n$ , are embedded in a similar way in the output result yout.

Variation in the stepsize as the integration proceeds, is needed to deal with changes in behaviour in the apparent accuracy of individual steps. If, in addition to computing the output results, an approximation is computed to the error committed in each step, a suitable strategy is to adjust $h$ to maintain the error estimates close to a fixed value, specified by a user-imposed tolerance.

In the case of the ARK method introduced in Subsection 270, we propose to compute an alternative approximation to $y$ at the end of the step and to regard their difference as an error estimate. This alternative approximation will be defined as

$$
\begin{array} { r } { \widehat { y } _ { n } = y _ { 1 } ^ { [ n - 1 ] } + \frac { 1 } { 8 } y _ { 2 } ^ { [ n - 1 ] } + \frac { 3 } { 8 } ( h F _ { 1 } + h F _ { 2 } ) + \frac { 1 } { 8 } h F _ { 3 } , } \end{array}
$$

based on the three-eighths rule quadrature formula. It is known that the difference between ${ \widehat { y } } _ { n }$ and $y _ { 1 } ^ { [ n ] }$ is $O ( h ^ { 4 } )$ , and this fact will be used in stepsize adjustments.

Because of the asymptotic behaviour of the error estimate, we can increase or decrease the error predicted in the following step, by multiplying $h$ by

$$
r = \bigg ( \frac { T } { \lVert \widehat { y } - y _ { 1 } ^ { [ n ] } \rVert } \bigg ) ^ { 1 / 4 } .
$$

This assumes that the error, or at least the quantity we are estimating, is changing slowly from step to step. If $\lVert \widehat { y } - y _ { 1 } ^ { [ n ] } \rVert \leq T$ is used as a criterion for accepting the current step, then the use of (271b) to predict the next stepsize allows the possibility of obtaining an unwanted rejection in the new step. Hence it is customary to insert a safety factor, equal to 0.9 for example, in (271a). Furthermore, to avoid violent swings of $h$ in exceptional circumstances, the stepsize ratio is usually forced to lie between two bounds, such as 0.5 and 2.0. Thus we should refine (271b) by multiplying $h$ not by $r$ , but by $\operatorname* { m i n } ( \operatorname* { m a x } ( 0 . 5 , 0 . 9 r ) , 2 . 0 )$ . For robust program design, the division in (271b) must be avoided when the denominator becomes accidentally small.

In modern solvers, a more sophisticated stepsize adjustment is used, based on PI control (Gustafsson, Lundh and S¨oderlind, 1988; Gustafsson, 1991). In the terminology of control theory, P control refers to ‘proportional control’, whereas PI or ‘proportional integral control’ uses an accumulation of values of the controller, in this case a controller based on error estimates, over recent time steps.

To illustrate the ideas of error estimation and stepsize control, a modified version of Algorithm $2 7 0 \alpha$ is presented as Algorithm $2 7 1 \alpha$ . The additional parameter T denotes the tolerance; the additional outputs hout and reject are, respectively, the proposed stepsize in the succeeding step and an indicator as to whether the current step apparently achieved sufficient accuracy. In the case $\mathtt { r e j e c t } = 1$ , signifying failure, the variables xout and yout retain the corresponding input values x and y.

α An ARK method step with stepsize control   

<table><tr><td>function [xout,yout,hout,reject] = ARKstep(x,y,f,h,T) Uy = y*[1,1,1;1/3,1/6,1/4;1/18,1/18,0]; hF = h*f(x+(1/3)*h,Uy(:,1)); hF = [hF,h*f(x+(2/3)*h,Uy(:,2)+(1/2)*hF)];</td></tr><tr><td>xout = x+h; y1out = Uy(:,3)+hF*[0;3/4];</td></tr><tr><td>hF = [hF,h*f(xout,y1out)];</td></tr><tr><td>y3out = hF*[3;-3;2]-2*y(:,2);</td></tr><tr><td>yout = [y1out,hF(:,3),y3out];</td></tr><tr><td>err = norm(hF*[3/8;-3/8;1/8]-y(:,2)/8);</td></tr><tr><td>reject = err &gt; T;</td></tr><tr><td>if err &lt; 0.04*T</td></tr><tr><td>r=2;</td></tr><tr><td>else</td></tr><tr><td>r = (T/err)^0.25; r = min(max(0.5，0.9*r),2.0); end</td></tr></table>
