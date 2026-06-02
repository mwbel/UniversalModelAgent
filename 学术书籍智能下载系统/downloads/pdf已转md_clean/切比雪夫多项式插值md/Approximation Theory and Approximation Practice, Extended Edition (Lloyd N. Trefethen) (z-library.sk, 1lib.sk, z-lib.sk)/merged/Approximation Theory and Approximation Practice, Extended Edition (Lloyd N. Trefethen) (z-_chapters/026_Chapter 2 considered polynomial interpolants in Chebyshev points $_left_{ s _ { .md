Chapter 2 considered polynomial interpolants in Chebyshev points $\left\{ s _ { k } \right\}$ . With the transformation $g$ , $f$ is interpolated by transformed polynomials $p ( g ^ { - 1 } ( x ) )$ in the points $\{ g ( s _ { k } ) \}$ . We illustrate the difference between Chebyshev and transformed Chebyshev points by adapting a code segment from Chapter 17. The squares show the transformed points.

ss $=$ chebpts(10); plot(ss,.9,'.b'), hold on, plot(g(ss),.8,'sm') ss $=$ chebpts(20); plot(ss,.5,'.b'), plot(g(ss),.4,'sm') ss $=$ chebpts(50); plot(ss,.12,'.b'), plot(g(ss),0,'sm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/6189e1c158c916011fb303df42912e4cb1a9182a823869043c26f7e997bc8a1c.jpg)

Note that the squares are more evenly distributed than the dots, and in particular, they are denser in the middle, providing finer resolution.
