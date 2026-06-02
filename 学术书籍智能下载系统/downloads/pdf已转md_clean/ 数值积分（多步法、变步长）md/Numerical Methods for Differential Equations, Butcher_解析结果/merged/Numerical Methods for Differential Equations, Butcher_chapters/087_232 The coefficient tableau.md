# 232 The coefficient tableau

It is convenient to represent a Runge–Kutta method by a partitioned tableau, of the form

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

in which the vector $c$ indicates the positions, within the step, of the stage values, the matrix $A$ indicates the dependence of the stages on the derivatives found at other stages, and $b ^ { \intercal }$ is a vector of quadrature weights, showing how the final result depends on the derivatives, computed at the various stages.

In the case of explicit methods, such as those we have considered so far in this section, the upper triangular components of $A$ are left blank, because they have zero value.

The first two of the following examples of Runge–Kutta tableaux are, respectively, for the Euler method and the general second order method, parameterized by an arbitrary non-zero $\theta$ . The special cases, which are also given, are for the trapezoidal rule method, designated here as RK21 and the mid-point rule method, RK22, correspond to $\theta = 1$ and $\textstyle \theta = { \frac { 1 } { 2 } }$ , respectively:

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/57cf80dcaabe0f5f6d86baffcfb75220d62b2c10b4151be0032ca52563a610b2.jpg)
