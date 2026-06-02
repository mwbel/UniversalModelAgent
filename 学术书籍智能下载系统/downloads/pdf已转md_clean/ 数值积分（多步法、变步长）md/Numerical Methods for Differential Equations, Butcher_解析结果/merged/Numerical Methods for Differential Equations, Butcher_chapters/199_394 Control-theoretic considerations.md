# 394 Control-theoretic considerations

Controlling the stepsize, using a ratio of $h$ in one step to $h$ in the previous step, based on (391a), can often lead to undesirable behaviour. This can come about because of over-corrections. An error estimate in one step may be accidentally low and this can lead to a greater increase in stepsize than is justified by the estimate found in the following step. The consequent rejection of this second step, and its re-evaluation with a reduced stepsize, can be the start of a series of similarly disruptive and wasteful increases and decreases.

In an attempt to understand this phenomenon and to guard against its damaging effects, an analysis of stepsize management using the principles of control theory was instituted by Gustafsson, Lundh and S¨oderlind (1988). The basic idea that has come out of these analyses is that PI control should be used in preference to I control. Although these concepts are related to continuous control models, they have a discrete interpretation. Under the discrete analogue, I control corresponds to basing each new stepsize on the most recently available error estimate, whereas PI control would make use of the estimates found in the two most recently completed steps.

If we were to base a new stepsize on a simplified alternative to (391a), using the ratio $r = ( \mathrm { e s t / t o l } ) ^ { 1 / ( p + 1 ) }$ , this would correspond to what is known in control theory as ‘dead-beat’ control. On the other hand, using the ratio $r = ( \mathrm { t o l } / \mathrm { e s t } ) ^ { \alpha / ( p + 1 ) }$ , where $0 < \alpha < 1$ , would correspond to a damped version of this control system. This controller would not respond as rapidly to varying accuracy requirements, but would be less likely to change too quickly for future behaviour to deal with. Going further, and adopting PI control, would give a stepsize ratio equal to

$$
r _ { n } = \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 1 } } } \right) ^ { \alpha / ( p + 1 ) } \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 2 } } } \right) ^ { \beta / ( p + 1 ) } .
$$

In this equation, $r _ { n }$ is the stepsize ratio for determining the stepsize $h _ { n }$ to be used in step $n$ . That is, if $h _ { n - 1 }$ is the stepsize in step $n - 1$ , then $h _ { n } = r _ { n } h _ { n - 1 }$ . The quantities $\mathrm { e s t } _ { n - 1 }$ and $\mathrm { e s t } _ { n - 2 }$ , denote the error estimates found in steps $n - 1$ and $n - 2$ , respectively.

For convenience, we work additively, rather than multiplicatively, by dealing with $\log ( h _ { n } )$ and $\log ( r _ { n } )$ rather than with $h _ { n }$ and $r _ { n }$ themselves. Let $\xi _ { n - 1 }$ denote the logarithm of the stepsize that would be adopted in step $n$ , if deadbeat control were to be used. That is,

$$
\xi _ { n - 1 } = \log ( h _ { n - 1 } ) + \frac { 1 } { p + 1 } ( \log ( \mathrm { t o l } ) - \log ( \mathrm { e s t } _ { n - 1 } ) ) .
$$

Now let $\eta _ { n }$ denote the logarithm of the stepsize actually adopted in step $n$ . Thus we can write dead-beat control as

$$
\eta _ { n } = \xi _ { n - 1 }
$$

and the modification with damping factor $\alpha$ as

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } + \alpha \xi _ { n - 1 } .
$$

For the PI controller (394a), we have

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } - \beta \eta _ { n - 2 } + \alpha \xi _ { n - 1 } + \beta \xi _ { n - 2 } .
$$

Appropriate choices for the parameters $\alpha$ and $\beta$ have been discussed by the original authors. Crucial considerations are the stable behaviour of the homogeneous part of the difference equation (394b) and the ability of the control system to respond sympathetically, but not too sensitively, to changing circumstances. For example, $\alpha = 0 . 7$ and $\beta = - 0 . 4$ , as proposed by Gustafsson (1991), works well. Recently, further work has been done on control-theoretic approaches to stepsize control by S¨oderlind (2002).
