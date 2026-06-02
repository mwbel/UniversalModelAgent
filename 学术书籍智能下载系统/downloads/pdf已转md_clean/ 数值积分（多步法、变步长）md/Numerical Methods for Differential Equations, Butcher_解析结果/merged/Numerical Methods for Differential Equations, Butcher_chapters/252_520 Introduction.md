# 520 Introduction

The linear stability analysis of general linear methods, as for the special cases of Runge–Kutta and linear multistep methods, is based on the differential equation

$$
y ^ { \prime } ( x ) = q y ( x ) .
$$

The idea will be to consider the influence of a single step of the method on an incoming vector $y ^ { \lfloor n - 1 \rfloor }$ . We obtain a relation of the form

$$
y ^ { [ n ] } = M ( z ) y ^ { [ n - 1 ] } ,
$$

where $z = h q$ and $M ( z )$ is an $r \times r$ matrix-valued function of the complex variable $z$ .

Definition 520A For a general linear method $( A , U , B , V )$ , the ‘stability matrix’ $M ( z )$ is defined by

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U .
$$

As we have anticipated, we have the following result:

Theorem 520B Let $M ( z )$ denote the stability matrix for a general linear method. Then, for a linear differential equation (520a), (520b) holds with $z = h q$ .

Proof. For the special problem defined by $f ( y ) = q y$ , the vector of stage derivatives $F$ is related to the vector of stage values $Y$ by $F = q Y$ . Hence, (500c) reduces to the form

$$
\left[ \begin{array} { c } { { Y } } \\ { { y ^ { [ n ] } } } \end{array} \right] = \left[ \begin{array} { c c } { { A } } & { { U } } \\ { { B } } & { { V } } \end{array} \right] \left[ \begin{array} { c } { { z Y } } \\ { { y ^ { [ n - 1 ] } } } \end{array} \right] .
$$

It follows that $Y = ( I - z A ) ^ { - 1 } U y ^ { \lfloor n - 1 \rfloor }$ , and that

$$
y ^ { [ n ] } = z B Y + V y ^ { [ n - 1 ] } = M ( z ) y ^ { [ n - 1 ] } .
$$

If the method is stable, in the sense of Section 51, then $M ( 0 ) = V$ will be power-bounded. The idea now is to extend this to values of $z$ in the complex plane where $M ( z )$ has bounded powers.

Just as for Runge–Kutta and linear multistep methods, associated with each method is a stability region. This, in turn, is related to the characteristic polynomial of $M ( z )$ .

Definition 520C Let $( A , U , B , V )$ denote a general linear method and $M ( z )$ the corresponding stability matrix. The ‘stability function’ for the method is the polynomial $\Phi ( w , z )$ given by

$$
\Phi ( w , z ) = \operatorname* { d e t } ( w I - M ( z ) ) ,
$$

and the ‘stability region’ is the subset of the complex plane such that if $z$ is in this subset, then

$$
\operatorname* { s u p } _ { n = 1 } \| M ( z ) ^ { n } \| < \infty .
$$

We refer to the ‘instability region’ as the complement of the stability region.

Note that in applications of these definitions, $\Phi ( w , z )$ may be a rational function. Quite often, the essential properties will be contained in just the numerator of this expression. We equally refer to the numerator of this rational function as the stability function.

We state the following obvious result without proof.

Theorem 520D The instability region for $( A , U , B , V )$ is a subset of the set of points $z$ , such that $\Phi ( w , z ) = 0$ , where $| w | \geq 1$ . The instability region is a superset of the points defined by $\Phi ( w , z ) = 0$ , where $| w | > 1$ .

The unanswered question in this result is: ‘Which points on the boundary of the stability region are actually members of it?’ This is not always a crucial question, and we quite often interpret the stability region as the ‘strict stability region’, consisting of those $z$ for which

$$
\operatorname* { l i m } _ { n \to \infty } \| M ( z ) ^ { n } \| = 0 .
$$

This will correspond to the set of $z$ values such that $| w | < 1$ , for any $w$ satisfying $\Phi ( w , z ) = 0$ .

In particular, we can define A-stability.

Definition 520E A general linear method is ‘A-stable’ if $M ( z )$ is powerbounded for every $z$ in the left half complex plane.

Just as for Runge–Kutta and linear multistep methods, A-stability is the ideal property for a method to possess for it to be applicable to stiff problems. Corresponding to the further requirement for Runge–Kutta methods that $R ( \infty ) = 0$ , we have the generalization of L-stability to general linear methods.

Definition 520F A general linear method is L-stable if it is A-stable and $\rho ( M ( \infty ) ) = 0$ .
