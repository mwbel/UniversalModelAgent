# 220 Introduction

As we have seen, in our discussion of the Euler method in Sections 20 and 21, this simplest of all numerical methods enjoys many desirable properties but, at the same time, suffers from some limitations. In the present section, we consider generalizations, which will yield improved numerical behaviour but will retain, as much as possible, its characteristic property of simplicity.

An important aim will be to obtain methods for which the asymptotic errors behave like high powers of the stepsize $h$ . For such methods, the gain in accuracy, resulting from a given reduction in stepsize, would be greater than for the Euler method, because for this method, the error behaves only like the first power of $h$ . We also examine the stability characteristics of these various more general methods. As we saw in Subsection 216, the Euler method does

Errors in the numerical solution of the orbital problem (201d) with zero eccentricity through a half period using (221a) and (221b)

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y1 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y2 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.014790210.003727810.000922330.000228520.000056820.00001416</td><td rowspan=1 colspan=1>3.96764.04174.03614.02194.0119</td><td rowspan=1 colspan=1>-0.04016858-0.01012098-0.00253020-0.00063190-0.00015785-0.00003945</td><td rowspan=1 colspan=1>3.96884.00014.00414.00314.0018</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y3 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y4 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.040386360.010225250.002547930.000634400.000158180.00003949</td><td rowspan=1 colspan=1>3.94974.01324.01634.01054.0059</td><td rowspan=1 colspan=1>-0.01548159-0.00372585-0.00091636-0.00022742-0.00005666-0.00001414</td><td rowspan=1 colspan=1>4.15524.06594.02944.01384.0067</td></tr></table>

not work well for stiff problems, because of stability considerations. We would like to find methods that have better stability.

The two major aims, greater accuracy and better stability, have to be balanced against the need to avoid additional computational costs, associated for example, with starting and stepsize-changing mechanisms. In the next few subsections, we explore some of the approaches used to achieve these aims.
